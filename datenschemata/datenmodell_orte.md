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


### Wikidata
*URL*

URL zum Eintrag des Orts in Wikidata.


### Beschreibung
*String*

Kurzer beschreibender Text zum Ort.


