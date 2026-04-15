from geopersons_preprocessor import main as create_geopersons
from generate_person_routes import main as generate_person_routes
from enrich_from_bionomia import main as enrich_from_bionomia
from enrich_locations_from_wikidata import main as enrich_locations_from_wikidata
from enrich_persons_from_wikidata import main as enrich_persons_from_wikidata
from parse_excel import main as parse_excel


def main() -> None:
    parse_excel()
    enrich_locations_from_wikidata()
    enrich_persons_from_wikidata()
    # enrich_from_bionomia()
    create_geopersons()
    generate_person_routes()


if __name__ == "__main__":
    main()
