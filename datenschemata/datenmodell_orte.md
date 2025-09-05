# Datenmodell – Orte

## Präambel

Das Datenmodell für den Gazeteer basiert weitestgehend auf dem Linked Places Format in der tabellarischen Variante ([LP-TSV v0.5](https://github.com/LinkedPasts/linked-places-format/blob/main/tsv_0.5.md)). Dieses Modell wird um einige zusätzliche Felder ergänzt. Die Bezeichnung der Originalfelder aus LP-TSV v0.5 werden in englischer Sprache beibehalten und um weitere projektspezifische Felder in deutscher Sprache ergänzt. 

## Felder (Spalten)

### id 
*ID*, **erforderlich**

Eindeutiger Identifier des Ortes. Beginnt mit dem Buchstaben `L` (Location) und ist gefolgt von sieben Ziffern. 
- `L0012000`


### title
*String*, **erforderlich**

Ein einzelner _bevorzugter_ Ortsname, der als Titel für den Datensatz dient.


### title_source
*String*, **bedingt erforderlich**

_Erforderlich, wenn **Titelquelle** keien Wert enthält_

Bezeichnung oder kurze Quellenangabe für die Herkunft des Titel-Typonyms, in beliebigem Zitierstil.  
Beispiele:  
- `An Historical Atlas of Central Asia (Bregel, 2003)`  
- `The Historical Sample of the Netherlands (https://iisg.amsterdam/nl/hsn)`

### attestation_year
*Structured String*, **bedingt erforderlich**

_Jede Zeile muss mindestens ein **attestation_year** oder einen **start**-Wert oder einen **ISO8601-2_Period**-Wert enthalten._

Veröffentlichungsjahr der **title_source** im Format YYYY.


### Quelle
*Reference*

Angabe der Quelle nach Projektschema, also Verweis in die Quellentabellen.


### fclasses 
*List of Strings from Codelist*, **bedingt erforderlich**

_Jede Zeile muss entweder einen **fclasses**-Wert oder einen **aat_types**-Wert enthalten._

Ein oder mehrere der sieben einbuchstabigen *GeoNames Feature Classes*.  
- `P`
- `P | A`

| Code | Beschreibung                                                        |
|------|----------------------------------------------------------------------|
| `A`  | Verwaltungseinheiten (z. B. Länder, Provinzen, Gemeinden)            |
| `H`  | Gewässer (z. B. Flüsse, Seen, Buchten, Meere)                        |
| `L`  | Regionen, Landschaftsbereiche (kulturell, geografisch, historisch)   |
| `P`  | Siedlungen (z. B. Städte, Dörfer, Weiler)                           |
| `R`  | Straßen, Routen, Schienenwege                                       |
| `S`  | Stätten (z. B. archäologische Stätten, Gebäude, Anlagen)            |
| `T`  | Landformen (z. B. Berge, Täler, Kaps)                               |



### aat_types 
*List of Integers from Codelist*, **bedingt erforderlich**

_Jede Zeile muss entweder einen **fclasses**-Wert oder einen **aat_types**-Wert enthalten._

Ein oder mehrere AAT-Integer-IDs aus der WHG-Teilliste von 176 Orts-Typkonzepten (Tabellenblatt `AAT-Codelist`).  

**Regeln:**  
- Ein Datensatz kann einen **types**-Wert ohne zugehörigen **aat_types**-Wert haben, aber nicht umgekehrt.  
- Für jeden Wert in **aat_types** muss es einen entsprechenden Wert in **type** geben (1:1).  
- Wenn für einen **type** kein **aat_type** existiert, die Position leer lassen.  
- Keine AAT-Hierarchien duplizieren – nur den spezifischen Typ verwenden.

### types
*List of Strings*

Ein oder mehrere Begriffe für den Ortstyp, in der Regel wortwörtlich aus der Quelle übernommen.  


### start
*Structured String*, **bedingt erforderlich**

_Jede Zeile muss mindestens einen **attestation_year**-Wert, einen **start**-Wert oder einen **Dauer**-Wert enthalten._

Die Felder **start** und **end** geben den bekannten Gültigkeitszeitraum des Ortsnamens an.  
Die Werte müssen im ISO-8601-Format angegeben werden (YYYY-MM-DD), Monat und Tag dürfen weggelassen werden.  

> **Hinweise:**  
> - **start** + **end** kennzeichnen einen vollständigen Zeitraum.  
> - Nur **start** bedeutet „ab“, Ende unbekannt oder heute.


### end
*Structured String*

Die Felder **start** und **end** geben den bekannten Gültigkeitszeitraum des Ortsnamens an.  
Die Werte müssen im ISO-8601-Format angegeben werden (YYYY-MM-DD), Monat und Tag dürfen weggelassen werden.  

> **Hinweise:**  
> - **start** + **end** kennzeichnen einen vollständigen Zeitraum.  
> - Nur **start** bedeutet „ab“, Ende unbekannt oder heute.

### Dauer
*ISO8601-2_Period*

Zeitraum über den der Ort existierte.

### title_uri
*URL*

Permanenter Link zur Quelle des Titel-Typonyms, z. B.:  
- `http://www.worldcat.org/oclc/890934416`  
- `https://doi.org/10.7910/DVN/AMPGMW`  
- `https://www.davidrumsey.com/luna/servlet/s/em7n8q`


### ccodes
*List of Strings from Codelist*

Ein oder mehrere [ISO 3166 Alpha-2](https://www.iso.org/iso-3166-country-codes.html) Ländercodes (https://www.iso.org/obp/ui/#search), die den Ort abdecken oder schneiden.

---

### matches
*List of Structured Strings*

Ein oder mehrere URIs zu übereinstimmenden Datensätzen in Ortsnamenautoritäten.  
Die Kurzpräfixe laut WHG müssen anstelle der vollen Basis-URIs verwendet werden, z. B.:  
- `wd:Q5684` (Wikidata, Babylon)

Unterstützte Präfixe:  
```
    {"bnf": Bibliothèque nationale de France, "https://data.bnf.fr/"}
    {"cerl": Consortium of European Research Libraries, "https://data.cerl.org/thesaurus/"}
    {"dbp": DBpedia, "http://dbpedia.org/resource/"}
    {"gn": GeoNames, "http://www.geonames.org/"}
    {"gnd": Deutschen Nationalbibliothek, "http://d-nb.info/gnd/"}
    {"gov": The Geneaological Gazetteer, "http://gov.genealogy.net/" }
    {"loc": Library of Congress, "http://id.loc.gov/authorities/subjects/"}
    {"pl": Pleiades, "https://pleiades.stoa.org/places/"}
    {"tgn": Getty Thesaurus of Geographic Names, "http://vocab.getty.edu/page/tgn/"}
    {"viaf": Virtual International Authority File, "http://viaf.org/viaf/"}
    {"wd": Wikidata, "https://www.wikidata.org/wiki/"}
    {"wp": Wikipedia, "https://wikipedia.org/wiki/"}
```

### variants
*List of Structured Strings*

Namens- und/oder Sprachvarianten nach BCP 47-Standard:  
`{Name}@Sprache[-Schrift][-Region][-Variante]`  
Mehrere Namen durch Semikolon trennen.

Beispiele:  
- `Zanzibar@sw`  
- `زنجبار@ar`  
- `Zanzíbar@es-ES`  
- `Sansibar@de-DE-1901`  
- `蒙巴萨@zh-Hans-CN`


### parent_name
*String*

Übergeordnete Verwaltungseinheit oder Region (z. B. Provinz, Land).  
Für jedes `parent_name` muss auch ein `parent_id` angegeben werden.


### parent_id
*URL*

URI zu einem veröffentlichten Datensatz, der den `parent_name` beschreibt.  
Darf nicht ohne zugehöriges `parent_name` vorkommen.

---

### lon
*Decimal*

Längengrad in WGS84 (EPSG:4326), z. B. `85.3214` oder `-112.4536`.

### lat
*Decimal*

Breitengrad in WGS84 (EPSG:4326), z. B. `59.3345` oder `-12.7658`.


### geowkt
*Structured String*

Geometrie im [OGC-WKT-Format](https://www.ogc.org/standards/wkt-crs/). Insbesondere für Nicht-Punkt-Geometrien (Linien, Polygone)

> [!TIP]
>
> Well-known text (WKT) ist eine standardisierte Text-Markup-Sprache, mit der sich Vektor-Geometrieobjekte wie Punkte, Linien und Polygone in lesbarer Form beschreiben lassen.
> 
> Einfache Beispiele:
> | Geometry primitives (2D) | Examples                                                                 |
> |---------------------------|--------------------------------------------------------------------------|
> | Point                     | `POINT (30 10)`                                                         |
> | LineString                | `LINESTRING (30 10, 10 30, 40 40)`                                      |
>| Polygon                   | `POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))`                         |
>
> [Wikipedia](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry), [Visualiserungstool](https://wktmap.com/)

---

### geo_source
*String*

Quellenangabe der Geometrie, z. B. `GeoNames` oder `digitalisierte <title_source> Karte`.


### geo_id
*URL*

URI zur Quelle der Geometrie.


### approximation
*String oder Decimal*

- URI zur Angabe einer Ungenauigkeit, z. B. `gvp:containedWithin`  
- oder Wert in Kilometern als Toleranz für `gvp:approximateLocation`.


### end
*Date_ISO8601*

Spätestes relevantes Datum.


### description
*String*

Kurzer beschreibender Text zum Ort.


