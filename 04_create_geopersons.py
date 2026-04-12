import argparse
import csv
from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.postprocessors.persons import transform_person_life_trajectory


def load_aat_feature_types(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return {
            row["aat_id"]: row["term"]
            for row in reader
            if row.get("aat_id") and row.get("term")
        }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transform persons life_trajectory into a FeatureCollection after location enrichment."
    )
    parser.add_argument(
        "--persons",
        type=Path,
        default="data/persons.json",
        help="Input persons JSON file.",
    )
    parser.add_argument(
        "--locations",
        type=Path,
        default="data/locations.json",
        help="Input locations JSON file.",
    )
    parser.add_argument(
        "--literature",
        type=Path,
        default="data/literature.json",
        help="Input literature JSON file.",
    )
    parser.add_argument(
        "--manuscripts",
        type=Path,
        default="data/manuscripts.json",
        help="Input manuscripts JSON file.",
    )
    parser.add_argument(
        "--archives",
        type=Path,
        default="data/archives.json",
        help="Input archives JSON file.",
    )
    parser.add_argument(
        "--collections",
        type=Path,
        default="data/collections.json",
        help="Input collections JSON file.",
    )
    parser.add_argument(
        "--aat-feature-types",
        type=Path,
        default="data/feature-types-AAT_20230609.tsv",
        help="CSV/TSV file mapping AAT feature type IDs to terms.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default="data/geopersons.json",
        help="Output persons JSON file.",
    )
    args = parser.parse_args()

    persons = load_json(args.persons)
    tables = {
        "locations": load_json(args.locations),
        "literature": load_json(args.literature),
        "manuscripts": load_json(args.manuscripts),
        "archives": load_json(args.archives),
        "collections": load_json(args.collections),
        "aat_feature_types": load_aat_feature_types(args.aat_feature_types),
    }

    transformed_persons = {
        person_id: transform_person_life_trajectory(person_record, tables)
        for person_id, person_record in persons.items()
    }

    save_json(args.output, transformed_persons)
    print(f"Finished. output={args.output}")


if __name__ == "__main__":
    main()
