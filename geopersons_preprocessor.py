from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.postprocessors.create_life_trajectory import (
    create_person_life_trajectory,
)
from projectlibs.py.postprocessors.renderers import replace_typed_nodes

PERSONS_FILE = Path("data/persons.json")
OUTPUT_FILE = Path("data/geopersons.json")


def main() -> None:
    print()
    print("Running create_geopersons.py")
    persons = load_json(PERSONS_FILE)

    transformed_persons = {}

    for person_id, person_record in persons.items():
        geoperson = create_person_life_trajectory(person_record)

        for person_field_id, person_field in geoperson.items():
            geoperson[person_field_id] = replace_typed_nodes(person_field)

        # if "member_of_moravians" in geoperson:
        #     geoperson["member_of_moravians"] = render_moravian_membership_field(
        #         geoperson["member_of_moravians"]
        #     )
        # geoperson = render_ids(geoperson, tables)
        transformed_persons[person_id] = geoperson

    save_json(OUTPUT_FILE, transformed_persons)
    print(f"Finished. output={OUTPUT_FILE}")


if __name__ == "__main__":
    main()
