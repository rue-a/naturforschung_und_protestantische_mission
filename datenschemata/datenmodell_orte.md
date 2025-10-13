# Datenmodell – Orte

## Präambel

Das Datenmodell für den Gazeteer basiert auf dem Linked Places Format in der tabellarischen Variante ([LP-TSV v0.5](https://github.com/LinkedPasts/linked-places-format/blob/main/tsv_0.5.md)). **Die Felder _ID_ und _Name_ sowie entweder _GeoNames-Typ_ oder _AAT-Typ_ sind verpflichtend.**

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)

## Felder (Spalten)

### ID
*ID*, **erforderlich\***

Eindeutiger Identifier des Ortes. Beginnt mit dem Buchstaben `L` (Location) und ist gefolgt von sieben Ziffern. 
- `L0012000`


### Name
*String*, **erforderlich\***

Ein einzelner _bevorzugter_ Ortsname, der als Titel für den Datensatz dient.

- `Sansibar`

### Varianten
*List of Structured Strings*

Namens- und/oder Sprachvarianten nach BCP 47-Standard:  
`{Name}@Sprache[-Schrift][-Region][-Variante]`  

Beispiele:  
- `Zanzibar@sw | Zanzíbar@es-ES | Sansibar@de-DE-1901 | 蒙巴萨@zh-Hans-CN`


### GeoNames-Typ
*List of Strings from Codelist*, **bedingt erforderlich°**

_Jede Zeile muss entweder einen **GeoNames-Typ**-Wert oder einen **AAT-Typ**-Wert enthalten._

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



### AAT-Typ
*List of Integers from Codelist*, **bedingt erforderlich°**

_Jede Zeile muss entweder einen **GeoNames-Typ**-Wert oder einen **AAT-Typ**-Wert enthalten._

Ein oder mehrere AAT-Integer-IDs aus der WHG-Teilliste von 176 Orts-Typkonzepten (**Tabellenblatt `AAT-Codelist`**).  

- `300387272`
- `300120599 | 300008372`


### Beginn
*ISO8601-2_Date*


Die Felder **Start** und **Ende** geben den bekannten Gültigkeitszeitraum des Ortsnamens an. **Beginn** + **Ende** kennzeichnen einen vollständigen Zeitraum. Nur **Beginn** bedeutet „ab“, existiert bis heute.

> [!TIP]
> - Das [ISO8601-2_Date](https://github.com/rue-a/naturforschung_und_protestantische_mission/blob/main/datenschemata/datentypen.md#iso8601-2_date) Format erlaubt auch sehr grobe/ungenaue Schätzungen.


### Ende
*ISO8601-2_Date*

Die Felder **Start** und **Ende** geben den bekannten Gültigkeitszeitraum des Ortsnamens an. **Beginn** + **Ende** kennzeichnen einen vollständigen Zeitraum. Nur **Ende** bedeutet „bis“, Beginn unbekannt.

> [!TIP]
> - Das [ISO8601-2_Date](https://github.com/rue-a/naturforschung_und_protestantische_mission/blob/main/datenschemata/datentypen.md#iso8601-2_date) Format erlaubt auch sehr grobe/ungenaue Schätzungen.



### Links
*List of URL*

Ein oder mehrere URLs zu übereinstimmenden Datensätzen in Ortsnamenautoritäten.  

> [!TIP]
> **Bekannte Ortsnamenautoritäten:**
> - Bibliothèque nationale de France, "https://data.bnf.fr/"
> - Consortium of European Research Libraries, "https://data.cerl.org/thesaurus/"
> - DBpedia, "http://dbpedia.org/resource/"
> - GeoNames, "http://www.geonames.org/"
> - Deutschen Nationalbibliothek, "http://d-nb.info/gnd/"
> - The Geneaological Gazetteer, "http://gov.genealogy.net/"
> - Library of Congress, "http://id.loc.gov/authorities/subjects/"
> - Pleiades, "https://pleiades.stoa.org/places/"
> - Getty Thesaurus of Geographic Names, "http://vocab.getty.edu/page/tgn/"
> - Virtual International Authority File, "http://viaf.org/viaf/"
> - Wikidata, "https://www.wikidata.org/wiki/"
> - Wikipedia, "https://wikipedia.org/wiki/"



### Longitude
*Decimal*

Längengrad in WGS84 (EPSG:4326), z. B. `85.3214` oder `-112.4536`.

> [!TIP]
> Bei Längen- und Breitengraden in WGS84 entsprechen 3 Nachkommastellen einer Genauigkeit der Ortsangabe auf etwa 100 Meter, 4 Nachkommastellen einer Genauigkeit auf etwa 10 Meter und 5 Nachkommastellen einer Genauigkeit auf etwa 1 Meter. Die Zur Verortung von Siedlungen reichen 4 Nachkommastellen vollkommen aus, i.d.R. auch 3. Insbesondere, wenn Koordinaten aus georeferenzierten alten Karten bestimmt werden, sollten nicht mehr Kommastellen angegeben werden, als man an Genauigkeit in der Karte ablesen kann.

### Latitude
*Decimal*

Breitengrad in WGS84 (EPSG:4326), z. B. `59.3345` oder `-12.7658`.

> [!TIP]
> Bei Längen- und Breitengraden in WGS84 entsprechen 3 Nachkommastellen einer Genauigkeit der Ortsangabe auf etwa 100 Meter, 4 Nachkommastellen einer Genauigkeit auf etwa 10 Meter und 5 Nachkommastellen einer Genauigkeit auf etwa 1 Meter. Die Zur Verortung von Siedlungen reichen 4 Nachkommastellen vollkommen aus, i.d.R. auch 3. Insbesondere, wenn Koordinaten aus georeferenzierten alten Karten bestimmt werden, sollten nicht mehr Kommastellen angegeben werden, als man an Genauigkeit in der Karte ablesen kann.

### Geometrie
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

### Geometriequelle
*Reference*

L- oder M-ID aus der Literatur- oder Manuskripte-Tabelle; oder URL zur Quelle der Koordinaten/Geometrie.


### Qualität der Ortsangabe
*String*

Möglichst ausführliche Angaben zur Qualität der Koordinatenangabe. Insbesondere wenn die Angabe in irgendeiner Art und Weise unsicher ist.
- Ort liegt im Umkreis von etwa 10 km um die genannten Koordinaten
- Der Ortsname war auf der Quellkarte schlecht zu lesen. Die ermittelten Koordinaten also gehören eventuell nicht zum hier aufgeführten Ort.



### Beschreibung
*String*

Kurzer beschreibender Text zum Ort.





