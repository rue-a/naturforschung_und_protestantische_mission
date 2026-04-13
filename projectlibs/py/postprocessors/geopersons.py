from projectlibs.py.postprocessors.utils import extract_field_value


def extract_field_source(field):
    source = field["value"].get("source")
    if not source:
        return None, None

    if isinstance(source, str):
        return source, None

    return source["value"], source["type"]


def build_point_geometry(location_id, locations_by_id):
    location = locations_by_id.get(location_id)
    if not location:
        return None

    longitude = extract_field_value(location.get("longitude"))
    latitude = extract_field_value(location.get("latitude"))
    if longitude is None or latitude is None:
        return None

    return {
        "type": "Point",
        "coordinates": [
            longitude,
            latitude,
        ],
    }


def build_life_trajectory_feature(
    *,
    geometry,
    time,
    event_type,
    source,
    place=None,
    institution=None,
    occupation=None,
):
    properties = {
        "source": source,
    }

    if place:
        properties["place"] = place

    if event_type == "place_of_effect":
        properties["institution"] = institution
        properties["occupation"] = occupation

    return {
        "type": "Feature",
        "featureType": event_type,
        "geometry": geometry,
        "time": build_time_object(time),
        "properties": properties,
    }


def build_time_object(raw_time):
    if "/" in raw_time:
        start, end = raw_time.split("/", 1)
        return {
            "interval": [
                start or "..",
                end or "..",
            ]
        }

    if "T" in raw_time:
        return {"timestamp": raw_time}

    return {"date": raw_time}


def build_place_properties(location_id, locations_by_id):
    location = locations_by_id.get(location_id)
    if not location:
        return None

    place_properties = {
        "start": extract_field_value(location.get("start")),
        "end": extract_field_value(location.get("end")),
        "founder": None,
    }

    founder_values = extract_field_value(location.get("founder"))
    if founder_values is not None:
        place_properties["founder"] = [
            founder["value"]
            for founder in founder_values
            if isinstance(founder, dict) and "value" in founder
        ]

    return place_properties


def create_person_life_trajectory(person_record, tables):
    person_id = extract_field_value(person_record["id"])
    person_name = extract_field_value(person_record["name"]["preferred"])
    locations_by_id = tables["locations"]

    features = []

    for event_type in ("birth", "death"):
        if event_type not in person_record:
            print(
                f"Warning: skipping {event_type} for {person_id} ({person_name}): "
                "event is missing"
            )
            continue

        event = person_record[event_type]
        if "date" not in event:
            print(
                f"Warning: skipping {event_type} for {person_id} ({person_name}): "
                "missing required part: date"
            )
            continue

        if "location" not in event:
            print(
                f"Warning: skipping {event_type} for {person_id} ({person_name}): "
                "missing required part: location"
            )
            continue

        location_id = extract_field_value(event["location"])
        geometry = build_point_geometry(location_id, locations_by_id)
        if not geometry:
            print(
                f"Warning: skipping {event_type} for {person_id} ({person_name}): "
                f"no point geometry could be built for location {location_id}"
            )
            continue

        source, _ = extract_field_source(event["location"])
        if not source:
            source, _ = extract_field_source(event["date"])

        features.append(
            build_life_trajectory_feature(
                geometry=geometry,
                time=extract_field_value(event["date"]),
                event_type=event_type,
                source=source,
                place=build_place_properties(
                    location_id,
                    locations_by_id,
                ),
            )
        )

    if "places_of_effect" in person_record:
        for index, feature_value in enumerate(
            person_record["places_of_effect"]["value"]["value"],
            start=1,
        ):
            values = feature_value["value"]["values"]
            location_id = values[1]["value"]
            geometry = build_point_geometry(location_id, locations_by_id)
            if not geometry:
                print(
                    f"Warning: skipping place_of_effect #{index} for "
                    f"{person_id} ({person_name}): "
                    f"no point geometry could be built for location {location_id}"
                )
                continue

            source = feature_value["value"].get("source")
            features.append(
                build_life_trajectory_feature(
                    geometry=geometry,
                    time=values[0]["value"],
                    event_type="place_of_effect",
                    source=source,
                    place=build_place_properties(
                        location_id,
                        locations_by_id,
                    ),
                    institution=values[2]["value"],
                    occupation=values[3]["value"],
                )
            )

    person_record["life_trajectory"] = {
        "type": "FeatureCollection",
        "features": features,
    }

    return person_record
