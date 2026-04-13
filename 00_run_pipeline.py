from create_geopersons import main as create_geopersons
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


if __name__ == "__main__":
    main()
