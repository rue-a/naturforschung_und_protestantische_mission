# Datenmodell – Sammlungen

## Präambel

> So hervorgehobene Textteile sind Kommentare.

Diese Tabelle beschreibt die Spalten des Tabellenblatts _Sammlungen_, welches der Erfassung von Sammlungen dient, in denen welchen Herbarbelege, die im Zuge der Herrnhutschen Mission angefertigt wurden, aufbewahrt werden. 

__In diesem Schema sind nur die Felder *ID* und *Name der Sammlung* erforderlich, alle anderen sind optional. Jedoch gilt immer: Je mehr Felder ausgefüllt sind, desto besser.__

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)

## Felder (Spalten)

### ID

*ID*, **erforderlich**

Eindeutiger Identifier der Sammlung. Beginnt mit dem Präfix `C-` (Collection) gefolgt von einer Buchstabenkombination. Ist die betreffende Sammlung im NYBG indexiert (2. Spalte), ist die Buchstabenkombination gleich dem NYBG Herbarcode (alles Großbuchstaben). Ist die Sammlung jedoch nicht im NYBG indexiert und somit kein NYBG Herbarcode vorhanden, wird stattdessen eine beliebige, in der Tabelle einzigartige, Folge von Kleinbuchstaben verwendet, z.B. `hz` für Herrnhuter Zoologische Sammlung.

- `C-hz`
- `C-B`
- `C-DR`
- `C-COI`

### NYBG Herbarcode

*String*

Sammlungs- oder Herbarcode, sofern vorhanden. Dieser dient der eindeutigen Identifikation in internationalen Registern.
Die Codes werden vom New York Botanical Garden (NYBG) vergeben und sind im [Index Herbariorum](https://sweetgum.nybg.org/science/ih/) nachschlagbar.

- ``
- `B`
- `DR`
- `COI`

### Name der Sammlung

*String*, **erforderlich**

Name der Sammlung oder des Herbars.

- `Herrnhuter Zoologische Sammlung (aus Barby)`
- `Herbarium Berolinense`
- `Herbarium Dresdense`
- `Herbarium of the University of Coimbra`

### Teilsammlung von

*ID*

ID (aus der Sammlungen-Tabelle) der übergeordneten Sammlung, falls diese Sammlung Teil einer anderen Sammlung ist.
- `C-ANSP`


### Sammlungshaltende Institution

*List of Strings*

Name(n) der Institution(en), zu der/denen die Sammlung gehört. Mehrere Werte sind durch `|` getrennt.

- `ZE Botanischer Garten und Botanisches Museum, Freie Universität Berlin`
- `Institut für Botanik, Technische Universität Dresden`
- `Herbarium of the University of Coimbra, Department of Life Sciences`

### Webseite

*URL*

Offizielle Webseite der Sammlung oder der Institution.

- `http://www.botanicalcollections.be`
- `https://tu-dresden.de/mn/biologie/botanik/herbarium`
- `https://coicatalogue.uc.pt/`


### Anmerkungen

*String*

Freitextfeld für ergänzende Hinweise oder Kontextinformationen.






