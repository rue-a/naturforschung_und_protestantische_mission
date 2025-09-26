# Datenmodell – Literatur

## Präambel

> So hervorgehobene Textteile sind Kommentare.

Diese Tabelle beschreibt die Spalten des Tabellenblatts *Literatur*, welches der Erfassung von gedruckten Werken dient, die im Zusammenhang mit den in der Personentabelle erfassten Personen stehen.

**In diesem Schema sind nur die Felder *ID* und *Titel* erforderlich, alle anderen sind optional. Jedoch gilt immer: Je mehr Felder ausgefüllt sind, desto besser.**

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)

## Felder (Spalten)

### ID

*ID*, **erforderlich**

Eindeutiger Identifier des Werkes. Beginnt mit dem Buchstaben `R` (Literature Reference) und ist gefolgt von sieben Ziffern.

* `R0010000`
* `R0020000`
* `R0030000`

### Titel

*String*, **erforderlich**

Titel des Werkes in zitierfähiger Form. Hier soll ein in den historisch arbeitenden Fächern gängiger Zitierstil verwendet werden (Z.B. Chicago Manual of Style), der eine eindeutige Identifizierung ermöglicht.

* `Carl von Linné: Species Plantarum. Stockholm: Laurentius Salvius, 1753.`
* `John Smith: A History of Botany. London: Academic Press, 1890.`


### Permalink

*URL*

Stabile URL zu einem Digitalisat oder bibliografischen Nachweis des Werkes.

### Beschreibung

*String*

Freitextfeld für ergänzende Hinweise oder Kontextinformationen.

