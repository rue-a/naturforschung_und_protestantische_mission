# Datenmodell – Personen

## Präambel

> So hervorgehobene Textteile sind Kommentare.

Die hier beschreibene Tabelle hat zwei Funktionen: 1) Arbeitswerkzeug zur Sammlung übergeordneter Informationen zu relevanten Personen und 2) Quelle zur Erzeugung einer Website, welche relevante Teile der gesammelten Informationen für eine breite Öffentlichkeit zugänglich darstellt. Alle Informationen, die dem zweiten Zweck dienen, müssen strukturiert erfasst werden. Dieses Dokument beschreibt alle Spalten, welche diesem zweiten Zweck dienen.

Sofern nicht anders angegeben gilt für jedes Feld die _**Open World Assumption**_, d.h. das Nicht-Vorhandensein einer Information bedeuten _nicht_, dass es keine Informationen gibt (1) **und** das Vorhandensein von Informationen bedeutet nicht, dass die Informationen vollständig sind (2). Bsp.: (1) Sind im Feld _Angehörige - Eheparner_ keine Informationen eingetragen, heißt das nicht, dass die Person nicht verheiratet war. Oder: Ist das Feld _Geburt - Ort - Geburtsorte_ leer, heißt das nicht, dass es keinen Geburtsort gibt. (2) Ist im Feld _Angehörige - Kinder_ eine Liste mit drei Werten eingetragen, heisst das nicht, dass die Person nur drei Kinder hatte, sondern, dass sie mindestens diese drei Kinder hatte.

__In diesem Schema sind nur die Felder _ID_ und _Name - Vorzugsname_ erforderlich, alle anderen sind optional. Jedoch gilt immer: Je mehr Felder ausgefüllt sind, desto besser.__

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)

## Felder (Spalten)


### ID 
*ID*, **erforderlich**

Eindeutiger Identifier der Person. Beginnt mit dem Buchstaben `P` (Person) und ist gefolgt von sieben Ziffern. 
- `P0012000`

### Name - Vorzugsname
*String*, **erforderlich**

Dient der Darstellung, z.B. auf der Website.
- `Johann Baptist von Albertini`.
- `Alexander Becker` 
- `Carl Gustav von Brinkmann`
- `Dr. August Herrmann Francke`
- `Constantin Theodor Glitsch`

### Name - Nachname(n)
*String*

Nachname(n) der Person inkl. Adels-/Namenszusatz. Verschiedene Schreibweisen eines Namens sind durch `/` (ohne umgebende Leerzeichen) anzuzeigen, wobei die relevanteste Schreibweise vorn stehen sollte. Abkürzungen sind erlaubt (auch als relevanteste Schreibweise).
- `von Albertini`
- `Becker`
- `von Brinkmann/Brinckmann`
- `Francke`
- `Glitsch`

### Name - Vornamen(n)
*String*

Vorname(n) der Person. Verschiedene Schreibweisen eines Namens sind durch `/` (ohne umgebende Leerzeichen) zu trennen, wobei die relevanteste Schreibweise vorn stehen sollte. Abkürzungen sind erlaubt.
- `Johann Baptist`
- `Alexander`
- `Carl Gustav`
- `August Herrmann`
- `Constantin/Konstantin Theodor`

### Name - Titel
*String*

Etwaige Titel der Personen (abgekürzt).
- `Dr.`

### Name - Anmerkungen
*String*

Freitextfeld für Anmerkungen in Bezug auf den Namen, z.B. weitere Informationen zu alternativen Schreibweisen oder Auflösung von Abkürzungen.

### Angehörige - Geschwister
*List of IDs*

Ungeordnete Liste der (für das Projekt) relevanten Geschwistern der Person. Die Angabe der Geschwister erfolgt mittels einer Personen-ID, d.h. die Geschwister müssen in dieser Tabelle erfasst sein.

### Angehörige - Ehepartner
*List of IDs*

Geordnete Liste der Ehepartner der Person entsprechend der zeitl. Abfolge der Heiraten. Die Angabe der Ehepartner erfolgt mittels einer Personen-ID, d.h. die Ehepartner müssen in dieser Tabelle erfasst sein.

### Angehörige - Kinder
*List of IDs*

Ungeordnete Liste der (für das Projekt) relevanten Kinder der Person. Die Angabe der Kinder erfolgt mittels einer Personen-ID, d.h. die Kinder müssen in dieser Tabelle erfasst sein.

### Angehörige - Anmerkungen
*String*

Freitextfeld für Anmerkungen in Bezug auf die Angehörigen, z.B. Gründe für mehrere Ehepartner.

### Zugehörigkeit Herrnhuter Brüdergemeine
*List of Strings from Codelist*


| Code        | Beschreibung                                                                                                   |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| `ja(a)`     | qua Geburt und Erziehung, in einer Herrnhuter Gemeinschaft bzw. von Herrnhuter Eltern geboren und aufgewachsen |
| `ja(b)`     | als Erwachsene aufgenommen, z.B. Konvertitien oder Missionierte |
| `ja(c)`     | Übernahme von kirchlichen Ämtern innerhalb der Brüdergemeine                                   |
| `ja(d)`     | Übernahme von Ämtern im Erziehungswesen der Brüdergemeine                                  |
| `nein(a)`   | ausgetreten                                                                                       |
| `nein(b)`   | aber wichtig im Netzwerk                                                                                       |
| `nein(c)`   | um Verwechslung auszuschließen                                                                                 |
| `unbekannt` | Zugehörigkeit kann nicht ausgeschlossen werden.                                                                |
- `ja(a)`
- `nein(a) | nein(b)`

### Links - Wikidata
*URL*

Link zum Eintrag der Person in Wikidata. Die URL beginnt immer mit `https://www.wikidata.org/wiki/`. Wenn nichts eingetragen ist, heißt das, dass es keinen Wikidata-Eintrag gibt.


### Links - GND
*URL*

Link zum Eintrag der Person in der GND. Die URL beginnt immer mit `https://d-nb.info/gnd/`. Wenn nichts eingetragen ist, heißt das, dass es keinen GND-Eintrag gibt.


### Links - FactGrid
*URL*

Link zum Eintrag der Person in FactGrid. Die URL beginnt immer mit `https://database.factgrid.de/wiki/`. Wenn nichts eingetragen ist, heißt das, dass es keinen FactGrid-Eintrag gibt.

### Links - Bionomia
*URL*

Link zum Eintrag der Person in Bionomia. Die URL beginnt immer mit `https://bionomia.net/`. Wenn nichts eingetragen ist, heißt das, dass es keinen Bionomia-Eintrag gibt. (Belegedaten werden von JACQ zu GBIF gespiegelt und von dort von Bionomia abgerufen; biographische Daten werden von wikidata abgerufen)

### Links - Säbi
*URL*

Link zum Eintrag der Person in Säbi. Die URL beginnt immer mit `https://saebi.isgv.de/person/`. Wenn nichts eingetragen ist, heißt das, dass es keinen Säbi-Eintrag gibt.

### Handschriftlicher Brüdergemeine
*ID*

Für jeden Herrenhuter wurde ein Lebenslauf angefertigt. Diese Lebensläufe liegen i.d.R. als handschriftliche Manuskripte vor, d.h. es ist eine Manuskript-ID (beginnend mit `M`) einzutragen.  

### Geburt - Datum - Geburtsdaten
*List of ISO8601-2_Dates*

Liste möglicher Geburtsdaten der Person. Die Geburtsdaten sind in absteigender Plausibilität zu ordnen.

### Geburt - Datum - Quellen
*List of References*

Liste der Quellen der Geburtsdaten in der Reihenfolge der entsprechenden Geburtsdaten.

### Geburt - Datum - Anmerkungen
*String*

### Geburt - Ort - Geburtsorte
*List of IDs*

Liste möglicher Geburtsorte der Person. Die Geburtsorte sind in absteigender Plausibilität zu ordnen. Die Angabe der Orte erfolgt mittels Verweis auf einen Eintrag in der Orte-Tabelle, d.h. über eine *ID*, welche mit dem Buchstaben `L` beginnt.

### Geburt - Ort - Quellen
*List of References*

Liste der Quellen der Geburtsorte in der Reihenfolge der entsprechenden Geburtsorte.

### Geburt - Ort - Anmerkungen
*String*

### Tod - Datum - Todesdaten
*List of ISO8601-2_Dates*

Liste möglicher Todesdaten der Person. Die Todesdaten sind in absteigender Plausibilität zu ordnen.

### Tod - Datum - Quellen
*List of References*

Liste der Quellen der Todesdaten in der Reihenfolge der entsprechenden Todesdaten.

### Tod - Datum - Anmerkungen
*String*

### Tod - Ort - Todesorte
*List of IDs*

Liste möglicher Todesorte der Person. Die Todesorte sind in absteigender Plausibilität zu ordnen. Die Angabe der Orte erfolgt mittels Verweis auf einen Eintrag in der Orte-Tabelle, d.h. über eine *ID*, welche mit dem Buchstaben `L` beginnt.

### Tod - Ort - Quellen
*List of References*

Liste der Quellen der Todesorte in der Reihenfolge der entsprechenden Todesorte.

### Tod - Ort - Anmerkungen
*String*

### Tätigkeiten
*List of Structured Strings*

Ungeordnete Liste von Tätigkeiten, die die Person im Laufe Ihres Lebens ausgeführt hat. Dieses Feld dient dem allgemeinen Überblick, genauere Angaben zum Kontext der Tätigkeiten (wo, wann, warum, etc.), werden im Lebenslauf der Person angegeben. Für jede Tätigkeit sollte in Klammern die Quelle angegeben werden. Die Quellen entsprechen dem Datentyp _References_, d.h. IDs aus der Literatur-Tabelle (beginnend mit `R`, IDs aus der Manuskripte-Tabelle (beginnend mit `M`) oder permanente URLs.

- `Theologe (R0000015) | Erzieher (M0000250) | Lehrer (M0000250) | Seminardirektor (https://www.bsp-permalink.org/)`

### Botanik - Foki
*List of Strings*

Ungeordnete Liste von Themen mit Botanikbezug denen sich die Person in besonderem Maße widmete.

### Botanik - Manuskripte
*List of IDs*

Ungeordnete Liste von IDs von Manuskripten mit Botanikbezug aus der Manuskripte-Tabelle deren Autor die Person ist. 

### Botanik - Druckwerke
*List of IDs*

Ungeordnete Liste von IDs von Druckwerken mit Botanikbezug aus der Literatur-Tabelle deren Autor die Person ist. 

### Botanik - Beitrag zu Sammlungen
*List of Structured Strings*

Die Person lieferte mindestens einem Beitrag zu den referenzierten Sammlungen. Jede referenzierte Sammlung ist mit **einem** Objekt zu belegen. Der Beleg erfolgt mit der Angabe einer URL, die zu einer Webrepräsentation eines Objekts führt, welches Teil der zu belegenden Sammlung ist und von der Person beigetragen wurde. Wenn möglich ist ein permanenter Link als URL anzugeben. Einträge in die Liste sind nach folgendem Muster zu strukturieren: `<ID-aus-der-Sammlungstabelle> (URL-zu-ausgewähltem-Beleg)`

- `GJO (https://www.gbif.org/occurrence/1935675557)`


### Botanik - Erwähnung in Manuskripten
*List of IDs*

Ungeordnete Liste von IDs von Manuskripten mit Botanikbezug aus der Manuskripte-Tabelle in denen die Person erwähnt ist.

### Botanik - Erwähnung in Druckwerken
*List of IDs*

Ungeordnete Liste von IDs von Druckwerken mit Botanikbezug aus der Literatur-Tabelle in denen die Person erwähnt ist.

### Nicht-Botanische Werke
*List of IDs*

Ungeordnete Liste von IDs aus der Manuskripte- oder Literaturtabelle deren Autor die Person ist, welche aber keinen Botanikbezug aufweisen.

### Erwähnungen in Nicht-Botanische Werken
*List of IDs*

Ungeordnete Liste von IDs aus der Manuskripte- oder Literaturtabelle in welchen die Person erwähnt ist, welche aber keinen Botanikbezug aufweisen.
