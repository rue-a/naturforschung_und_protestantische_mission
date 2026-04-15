from pathlib import Path

from projectlibs.py.enrich_utils import load_json

INDEX_FILE = Path("index.html")
PERSONS_FILE = Path("data/geopersons.json")
ROUTE_BASE_TAG = '    <base href="../">\n'


def build_route_html(index_html: str) -> str:
    if "<base " in index_html:
        return index_html

    return index_html.replace("<head>\n", f"<head>\n{ROUTE_BASE_TAG}", 1)


def main() -> None:
    print()
    print("Running generate_person_routes.py")
    print(f"index template: {INDEX_FILE}")
    print(f"persons input: {PERSONS_FILE}")

    persons = load_json(PERSONS_FILE)
    route_html = build_route_html(INDEX_FILE.read_text(encoding="utf-8"))

    for person_id in persons:
        route_dir = Path(person_id)
        route_dir.mkdir(exist_ok=True)
        route_file = route_dir / "index.html"
        route_file.write_text(route_html, encoding="utf-8")
        print(f"wrote {route_file}")

    print(f"Finished. routes={len(persons)}")


if __name__ == "__main__":
    main()
