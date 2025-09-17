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

Eindeutiger Identifier der Sammlung. Beginnt mit dem Buchstaben `C` (Collection) und ist gefolgt von sieben Ziffern.

- `C0040000`
- `C0080000`
- `C0130000`

### NYBG Herbarcode

*String*

Sammlungs- oder Herbarcode, sofern vorhanden. Dieser dient der eindeutigen Identifikation in internationalen Registern.
Die Codes werden vom New York Botanical Garden (NYBG) vergeben und sind im [Index Herbariorum](https://sweetgum.nybg.org/science/ih/) nachschlagbar.

- `B`
- `DR`
- `COI`

### Name der Sammlung

*String*, **erforderlich**

Name der Sammlung oder des Herbars.

- `Herbarium Berolinense`
- `Herbarium Dresdense`
- `Herbarium of the University of Coimbra`

### Name der Institution

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

### Charakter der Sammlung

*List of Strings from Codelist*

Liste zur Erfassung des Charakters/Zwecks der Sammlung. Die zulässigen Werte sind in der folgenden Codeliste definiert. 

> Die Codeliste ist noch unvollständig.

| Code        | Beschreibung                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| `Bildung`   | Die Sammlung dient(e) vorwiegend der Ausbildung und Lehre (z. B. Seminare, Pädagogien).              |
| `Sammlung`  | Die Sammlung dient(e) vorwiegend dem Aufbau und der Pflege von Herbarbelegen (z. B. Herbarien, Museen). |

### Anmerkungen

*String*

Freitextfeld für ergänzende Hinweise oder Kontextinformationen.



