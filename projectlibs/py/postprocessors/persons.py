def extract_field_value(field):
    return field["value"]["value"]


def extract_field_source(field):
    source = field["value"].get("source")
    if not source:
        return None, None

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
    source_type,
    institution=None,
    occupation=None,
):
    return {
        "type": "Feature",
        "featureType": event_type,
        "geometry": geometry,
        "time": time,
        "properties": {
            "type": event_type,
            "source": source,
            "source_type": source_type,
            "institution": institution,
            "occupation": occupation,
        },
    }


def transform_person_life_trajectory(person_record, locations_by_id):
    raw_life_trajectory = person_record.get("life_trajectory")
    if not raw_life_trajectory:
        return person_record

    features = []

    for event_type in ("birth", "death"):
        if event_type not in raw_life_trajectory:
            continue

        event = raw_life_trajectory[event_type]
        if "date" not in event or "location" not in event:
            continue

        geometry = build_point_geometry(
            extract_field_value(event["location"]),
            locations_by_id,
        )
        if not geometry:
            continue

        source, source_type = extract_field_source(event["location"])
        if not source:
            source, source_type = extract_field_source(event["date"])

        features.append(
            build_life_trajectory_feature(
                geometry=geometry,
                time=extract_field_value(event["date"]),
                event_type=event_type,
                source=source,
                source_type=source_type,
            )
        )

    if "places_of_effect" in raw_life_trajectory:
        for feature_value in raw_life_trajectory["places_of_effect"]["value"]["value"]:
            values = feature_value["value"]["values"]
            geometry = build_point_geometry(values[1]["value"], locations_by_id)
            if not geometry:
                continue

            source = feature_value["value"].get("source")
            features.append(
                build_life_trajectory_feature(
                    geometry=geometry,
                    time=values[0]["value"],
                    event_type="place_of_effect",
                    source=source["value"] if source else None,
                    source_type=source["type"] if source else None,
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
