# Datenmodell – Literaturquellen

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)

## Felder (Spalten)

### ID
*ID*, **erforderlich**

Eindeutiger Identifier der Literaturquelle. Beginnt mit dem Buchstaben `Q` (Quelle) und ist gefolgt von sieben Ziffern.  
- `Q0000001`


### Kurzform
*String*

Kurze zitierfähige Referenzform, wie in der Forschung üblich.  
- `Becker 2005`  
- `Scholler 1774`


### Langform
*String*, **erforderlich**

Vollständige bibliographische Angabe (ohne URL).  
- `Ludwig Becker: "Die Pflege der Naturwissenschaften in der Herrnhuter Brüdergemeine", in: Unitas Fratrum 55/56 (2005), S. 17–51.`  
- `E. R. Meyer: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905.`


### Link
*URL*

Stabiler Link zur Publikation.

