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

### Übernahme in Personenlexikon
*Boolean*, **erforderlich**

Gibt an ob die Person in das Online-Personenlexikon als eigener Eintrag auftaucht, also an der botanischen Wissensproduktion beteiligt war (dann `ja`), oder ob die Person im Kontext dieses Projekts nur eine Netzwerkabbildungsrolle inne hat (dann `nein`).
- `ja`
- `nein`

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

### Name - Geburtsname(n)
*String*

Nur für weibliche Personen auszufüllen. Geburtsname(n) der Person inkl. Adels-/Namenszusatz. Verschiedene Schreibweisen eines Namens sind durch `/` (ohne umgebende Leerzeichen) anzuzeigen, wobei die relevanteste Schreibweise vorn stehen sollte. Abkürzungen sind erlaubt (auch als relevanteste Schreibweise). 

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

### Herrnhuter Lebenslauf
*ID: \<M-ID/R-ID\>* 

Für jeden Herrenhuter wurde ein Lebenslauf angefertigt. Diese Lebensläufe liegen als handschriftliche Manuskripte oder Drucke vor, d.h. es ist eine Manuskript-ID (beginnend mit `M`) oder Literatur-ID (beginnend mit `R`) einzutragen.  

### Geburt - Datum
*List of Structured Strings: \<ISO8601-2_Date\> (\<Reference\>)*

Geburtsdatum der Person mit Quellenangabe (_Reference_) in Klammern. Quellen können IDs aus anderen Tabellen oder URLs sein. Bei mehreren widersprüchlichen Geburtsdaten sind die Geburtsdaten mit Quellenangabe in absteigender Plausibilität als Liste zu ordnern.


### Geburt - Datum - Anmerkungen
*String*

### Geburt - Ort
*List of Structured Strings: \<L-ID\> (\<Reference\>)*

Geburtsort der Person mit Quellenangabe (_Reference_) in Klammern. Orte sind mittels ID in der Orte-Tabelle zu identifizieren (L-ID). Quellen können IDs aus anderen Tabellen oder URLs sein. Bei mehreren widersprüchlichen Geburtsorten sind die Geburtsorte mit Quellenangabe in absteigender Plausibilität als Liste zu ordnern.

### Geburt - Ort - Anmerkungen
*String*

### Tod - Datum
*List of Structured Strings: \<ISO8601-2_Date\> (\<Reference\>)*

Todessdatum der Person mit Quellenangabe (_Reference_) in Klammern. Quellen können IDs aus anderen Tabellen oder URLs sein. Bei mehreren widersprüchlichen Todessdaten sind die Todesdaten mit Quellenangabe in absteigender Plausibilität als Liste zu ordnern.

### Tod - Datum - Anmerkungen
*String*

### Tod - Ort
*List of Structured Strings: \<L-ID\> (\<Reference\>)*

Todesort der Person mit Quellenangabe (_Reference_) in Klammern. Orte sind mittels ID in der Orte-Tabelle zu identifizieren (L-ID). Quellen können IDs aus anderen Tabellen oder URLs sein. Bei mehreren widersprüchlichen Todesorten sind die Todesorte mit Quellenangabe in absteigender Plausibilität als Liste zu ordnern.

### Tod - Ort - Anmerkungen
*String*

### Tätigkeiten
*List of Structured Strings: \<String\> (\<Reference\>)*

Ungeordnete Liste von Tätigkeiten, die die Person im Laufe Ihres Lebens ausgeführt hat. Dieses Feld dient dem allgemeinen Überblick, genauere Angaben zum Kontext der Tätigkeiten (wo, wann, warum, etc.), werden im Lebenslauf der Person angegeben. Für jede Tätigkeit sollte in Klammern die Quelle angegeben werden. Die Quellen entsprechen dem Datentyp _References_, d.h. IDs aus der Literatur-Tabelle (beginnend mit `R`, IDs aus der Manuskripte-Tabelle (beginnend mit `M`) oder permanente URLs.

- `Theologe (R0000015) | Erzieher (M0000250) | Lehrer (M0000250) | Seminardirektor (https://www.bsp-permalink.org/)`

### Kontakt – Mit Herrnhutern
*List of Structured Strings: \<P-ID\>; \<ISO8601_2_Temporal\> (\<Reference\>)*

Ungeordnete Liste von Personen-IDs innerhalb der Herrnhuter Brüdergemeine, mit denen diese Person nachweislich in Kontakt stand. Optional, kann, getrennt durch Semikolon, ein Zeitraum oder Zeitpunkt in/zu dem der Kontakt stattfand angegeben werden (-> `ISO8601_2_Temporal`). Zu jedem Kontakt ist eine Quelle in Klammern anzugeben. Die Quellen entsprechen dem Datentyp *References*, d. h. IDs aus der Literatur-Tabelle (beginnend mit `R`), IDs aus der Manuskripte-Tabelle (beginnend mit `M`) oder permanente URLs.

- `P0000123 (R0000456) | P0000789; 1806-04 (M0000102) |  P0000789; 1806/1809 (M0000102)`


### Kontakt – Mit Nicht-Herrnhutern
*List of Structured Strings: \<P-ID\>; \<ISO8601_2_Temporal\> (\<Reference\>)*

Ungeordnete Liste von Personen-IDs außerhalb der Herrnhuter Brüdergemeine, mit denen diese Person nachweislich in Kontakt stand. Optional, kann, getrennt durch Semikolon, ein Zeitraum oder Zeitpunkt in/zu dem der Kontakt stattfand angegeben werden (-> `ISO8601_2_Temporal`). Zu jedem Kontakt ist eine Quelle in Klammern anzugeben. Die Quellen entsprechen dem Datentyp *References*, d. h. IDs aus der Literatur-Tabelle (beginnend mit `R`), IDs aus der Manuskripte-Tabelle (beginnend mit `M`) oder permanente URLs.

- `P0000234 (https://www.example.org/permalink)`
- siehe auch `Kontakt - Mit Herrnhutern`


### Botanik - Foki
*List of Strings*

Ungeordnete Liste von Themen mit Botanikbezug denen sich die Person in besonderem Maße widmete.


### Botanik – Beitrag zu Sammlungen (Objektnachweis)
*List of Structured Strings: \<C-ID\> (\<URL\>)*

Persistenter Link zu einem konkreten Objekt, das von der Person gesammelt wurde und Teil der referenzierten Sammlung ist. Jede referenzierte Sammlung muss mit genau einem Objekt nachgewiesen werden. Einträge folgen diesem Muster: `<ID-aus-der-Sammlungstabelle> (<persistenter-Link-zum-Objekt>)`.

- `C-DR (https://dr.jacq.org/DR086086)`: Das von Albertini gesammelte Objekt, zu finden unter https://dr.jacq.org/DR086086, weist nach, dass Albertini zur Sammlung C-DR (DR, Herbarium Dresdense) beigetragen hat.


### Botanik – Beitrag zu Sammlungen (Datenbanknachweis)
*List of Structured Strings: \<C-ID\> (\<URL\>)*

Persistenter Link zu einem Personeneintrag in einer Datenbank, in dem vermerkt ist, zu welchen Sammlungen die Person beigetragen hat. Einträge folgen diesem Muster: `<ID-aus-der-Sammlungstabelle> (<persistenter-Link-zur-Datenbankseite>)`.

- `C-B (https://www.tropicos.org/person/791) | C-M (https://www.tropicos.org/person/791)`: Unter https://www.tropicos.org/person/791 ist vermerkt (bei _Speciality_), dass Albertini zu den Sammlungen C-B (B, Herbarium Berolinense), und C-M (M, Herbarium der Staatlichen Naturwissenschaftlichen Sammlungen Bayerns) beigetragen hat.



### Botanik – Beitrag zu Sammlungen (Literaturnachweis)
*List of Structured Strings: \<C-ID\> (\<R-ID\>)*

Verweis auf eine Literaturquelle, in der explizit erwähnt ist, dass die Person zu einer Sammlung beigetragen hat. Einträge folgen diesem Muster: `<ID-aus-der-Sammlungstabelle> (<ID-aus-der-Literaturtabelle>)`.




### Botanik – Beitrag zu Sammlungen – Anmerkungen
*String*

Freitextfeld für Hinweise zur Nachweisführung, z. B. mehrere mögliche Objektnachweise, Unsicherheiten zur Zuordnung oder Erläuterungen bei widersprüchlichen Quellen.


### Botanik - Manuskripte der Person
*List of IDs*

Ungeordnete Liste von IDs von Manuskripten mit Botanikbezug aus der Manuskripte-Tabelle deren Autor die Person ist. 

### Botanik - Druckwerke der Person
*List of IDs*

Ungeordnete Liste von IDs von Druckwerken mit Botanikbezug aus der Literatur-Tabelle deren Autor die Person ist. 

### Botanik - Erwähnung der Person durch Andere
*List of IDs: \<M-ID/R-ID\>*

Ungeordnete Liste von IDs von Manuskripten oder Druckwerken mit Botanikbezug in denen die Person erwähnt wird.


### Wichtige Werke der Person ohne botanischen Kontext
*List of IDs*

Ungeordnete Liste von IDs aus der Manuskripte- oder Literaturtabelle deren Autor die Person ist, welche aber keinen Botanikbezug aufweisen.

### Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere
*List of IDs*

Ungeordnete Liste von IDs aus der Manuskripte- oder Literaturtabelle in welchen die Person erwähnt ist, welche aber keinen Botanikbezug aufweisen.
