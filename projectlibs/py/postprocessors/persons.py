from projectlibs.py.postprocessors.utils import replace_reference_objects


def extract_field_value(field):
    return field["value"]["value"]


def extract_field_source(field):
    source = field["value"].get("source")
    if not source:
        return None, None

    if isinstance(source, str):
        return source, None

    return source["value"], source["type"]


def build_point_geometry(location_id, locations_by_id):
    location = locations_by_id.get(location_id)
    if not location or "longitude" not in location or "latitude" not in location:
        return None

    return {
        "type": "Point",
        "coordinates": [
            extract_field_value(location["longitude"]),
            extract_field_value(location["latitude"]),
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


def build_place_properties(location_id, locations_by_id, aat_feature_types):
    location = locations_by_id.get(location_id)
    if not location:
        return None

    place_properties = {
        "aat_feature_type": None,
        "start": None,
        "end": None,
        "founder": None,
    }

    if "aat_type" in location:
        aat_value = location["aat_type"]["value"]["value"]
        place_properties["aat_feature_type"] = [
            aat_feature_types.get(str(aat_value), str(aat_value))
        ]

    if "start" in location:
        place_properties["start"] = extract_field_value(location["start"])

    if "end" in location:
        place_properties["end"] = extract_field_value(location["end"])

    if "founder" in location:
        place_properties["founder"] = [
            founder["value"] for founder in location["founder"]["value"]["value"]
        ]

    return place_properties


def transform_person_life_trajectory(person_record, tables):
    person_record = replace_reference_objects(person_record, tables)

    raw_life_trajectory = person_record.get("life_trajectory")
    person_id = extract_field_value(person_record["id"])
    person_name = extract_field_value(person_record["name"]["preferred"])
    locations_by_id = tables["locations"]
    aat_feature_types = tables.get("aat_feature_types", {})

    if not raw_life_trajectory:
        print(
            f"Warning: skipping life_trajectory for {person_id} ({person_name}): "
            "person has no life_trajectory block"
        )
        return person_record

    features = []

    for event_type in ("birth", "death"):
        if event_type not in raw_life_trajectory:
            print(
                f"Warning: skipping {event_type} for {person_id} ({person_name}): "
                "event is missing"
            )
            continue

        event = raw_life_trajectory[event_type]
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
                    aat_feature_types,
                ),
            )
        )

    if "places_of_effect" in raw_life_trajectory:
        for index, feature_value in enumerate(
            raw_life_trajectory["places_of_effect"]["value"]["value"],
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
                        aat_feature_types,
                    ),
                    institution=values[2]["value"],
                    occupation=values[3]["value"],
                )
            )

    if "activities" in raw_life_trajectory:
        person_record["activities"] = raw_life_trajectory["activities"]

    person_record["life_trajectory"] = {
        "type": "FeatureCollection",
        "features": features,
    }

    return person_record
