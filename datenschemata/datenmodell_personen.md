# Datenmodell – Personen

## Präambel

> So hervorgehobene Textteile sind Kommentare.

Die hier beschreibene Tabelle hat zwei Funktionen: 1) Arbeitswerkzeug zur Sammlung übergeordneter Informationen zu relevanten Personen und 2) Quelle zur Erzeugung einer Website, welche relevante Teile der gesammelten Informationen für eine breite Öffentlichkeit zugänglich darstellt. Alle Informationen, die dem zweiten Zweck dienen, müssen strukturiert erfasst werden. Dieses Dokument beschreibt alle Spalten, welche diesem zweiten Zweck dienen.

Sofern nicht anders angegeben gilt für jedes Feld die _**Open World Assumption**_, d.h. das Nicht-Vorhandensein einer Information bedeuten _nicht_, dass es keine Informationen gibt (1) **und** das Vorhandensein von Informationen bedeutet nicht, dass die Informationen vollständig sind (2). Bsp.: (1) Sind im Feld _Angehörige - Eheparner_ keine Informationen eingetragen, heißt das nicht, dass die Person nicht verheiratet war. Oder: Ist das Feld _Geburt - Ort - Geburtsorte_ leer, heißt das nicht, dass es keinen Geburtsort gibt. (2) Ist im Feld _Angehörige - Kinder_ eine Liste mit drei Werten eingetragen, heisst das nciht, dass die Person nur drei Kinder hatte, sondern, dass sie mindestens diese drei Kinder hatte.

In diesem Schema sind nur die Felder _ID_ und _Name - Vorzugsname_ erforderlich, alle anderen sind optional. Jedoch gilt immer: Je mehr Felder ausgefüllt sind, desto besser.

> Farbkodierung der Spalten:
> - weiß: Informationen werden auf der Website präsentiert
> - rot-orange: wird gelöscht, enthält aber noch Informationen für andere Spalten
> - gelb: Bezeichnung wird noch geändert
> - blau: Information ist implizit in anderen Tabellen enthalten, kann gelöscht werden, wenn sonst nicht notwendig. Kann auch als Arbeitsspalte umfunktioniert werden. 
> - grau: Arbeitsspalte, wird nirgends mit angezeigt oder ausgewertet. Kann beliebig befüllt werden.

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
*List of ID*

Ungeordnete Liste der (für das Projekt) relevanten Geschwistern der Person. Die Angabe der Geschwister erfolgt mittels einer Personen-ID, d.h. die Geschwister müssen in dieser Tabelle erfasst sein.

### Angehörige - Ehepartner
*List of ID*

Geordnete Liste der Ehepartner der Person entsprechend der zeitl. Abfolge der Heiraten. Die Angabe der Ehepartner erfolgt mittels einer Personen-ID, d.h. die Ehepartner müssen in dieser Tabelle erfasst sein.

### Angehörige - Kinder
*List of ID*

Ungeordnete Liste der (für das Projekt) relevanten Kinder der Person. Die Angabe der Kinder erfolgt mittels einer Personen-ID, d.h. die Kinder müssen in dieser Tabelle erfasst sein.

### Angehörige - Anmerkungen
*String*

Freitextfeld für Anmerkungen in Bezug auf die Angehörigen, z.B. Gründe für mehrere Ehepartner.

### Zugehörigkeit Herrnhuter Brüdergemeine
*List of String from Codelist*


| Code        | Beschreibung                                                                                                   |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| `ja(a)`     | qua Geburt und Erziehung, in einer Herrnhuter Gemeinschaft bzw. von Herrnhuter Eltern geboren und aufgewachsen |
| `ja(b)`     | als Erwachsene aufgenommen, z.B. Konvertitien oder Missionierte |
| `ja(c)`     | Übernahme von Funktionen und Ausübung von Ämtern innerhalb der Brüdergemeine                                   |
| `nein(a)`   | ausgetreten                                                                                       |
| `nein(b)`   | aber wichtig im Netzwerk                                                                                       |
| `nein(c)`   | um Verwechslung auszuschließen                                                                                 |
| `unbekannt` | Zugehörigkeit kann nicht ausgeschlossen werden.                                                                |
- `ja(a)`
- `nein(a) | nein (b)`

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

Link zum Eintrag der Person in Säbi. Die URL beginnt immer mit `https://saebi.isgv.de/biografie/`. Wenn nichts eingetragen ist, heißt das, dass es keinen Säbi-Eintrag gibt.

### Links - Lebenslauf Unitätsarchiv
*URL*

> zu prüfen ob URL der richtige Datentyp ist.

Link zum Lebenslauf der Person in Unitätsarchiv. Wenn nichts eingetragen ist, heißt das, dass es keinen (öffentlich zugänglichen) Eintrag im Unitätsarchiv gibt.

### Geburt - Datum - Geburtsdaten
*List of Date_ISO8601-2*

Liste möglicher Geburtsdaten der Person. Die Geburtsdaten sind in absteigender Plausibilität zu ordnen.

### Geburt - Datum - Quellen
*List of Reference*

Liste der Quellen der Geburtsdaten in der Reihenfolge der entsprechenden Geburtsdaten.

### Geburt - Datum - Anmerkungen
*String*

### Geburt - Ort - Geburtsorte
*List of ID*

Liste möglicher Geburtsorte der Person. Die Geburtsorte sind in absteigender Plausibilität zu ordnen. Die Angabe der Orte erfolgt mittels Verweis auf einen Eintrag in der Gazetteer-Tabelle, d.h. über eine *ID*, welche mit dem Buchstaben *L* beginnt.

### Geburt - Ort - Quellen
*List of Reference*

Liste der Quellen der Geburtsorte in der Reihenfolge der entsprechenden Geburtsorte.

### Geburt - Ort - Anmerkungen
*String*

### Tod - Datum - Todesdaten
*List of Date_ISO8601-2*

Liste möglicher Todesdaten der Person. Die Todesdaten sind in absteigender Plausibilität zu ordnen.

### Tod - Datum - Quellen
*List of Reference*

Liste der Quellen der Todesdaten in der Reihenfolge der entsprechenden Todesdaten.

### Tod - Datum - Anmerkungen
*String*

### Tod - Ort - Todesorte
*List of ID*

Liste möglicher Todesorte der Person. Die Todesorte sind in absteigender Plausibilität zu ordnen. Die Angabe der Orte erfolgt mittels Verweis auf einen Eintrag in der Gazetteer-Tabelle, d.h. über eine *ID*, welche mit dem Buchstaben *L* beginnt.

### Tod - Ort - Quellen
*List of Reference*

Liste der Quellen der Todesorte in der Reihenfolge der entsprechenden Todesorte.

### Tod - Ort - Anmerkungen
*String*

### Tätigkeiten
*List of String*

Ungeordnete Liste von Tätigkeiten, die die Person im Laufe Ihres Lebens ausgeführt hat. Dieses Feld dient dem allgemeinen Überblick, genauere Angaben zum Kontext der Tätigkeiten (wo, wann, warum, etc.), werden im Lebenslauf der Person angegeben.

> Hier gilt es zu überlegen, ob die Verwendung einer Codelist nötig ist. Grundsätzlich soll sie vermeiden, dass bei der einen Person *Dichter* und bei der anderen *Lyriker* oder *Versschmied* steht. 

### Foki
*List of String*

Ungeordnete Liste von Fachgebieten, etc. denen sich die Person in besonderem Maße widmete.

### Literatur - Zitationen
*List of ID*

Ungeordnete Liste von IDs aus der Literaturquellentabelle. Dient der Angabe, in welchen Werken die Person (Publikationen der Person) zitiert wurde. 


### Literatur - Publikationen
*List of ID*

Ungeordnete Liste von IDs aus der Literaturquellentabelle. Dient der Erfassung von publizierten (wissenschaftlichen) Texterzeugnissen der Person.

### Literatur - Manuskripte
*List of ID*

Ungeordnete Liste von IDs aus der Literaturquellentabelle. Dient der Erfassung von unpublizierten (wissenschaftlichen) Texterzeugnissen der Person.

> hier ist zu prüfen, ob Manuskripte sinnvoll in der Literaturquellentabelle erfasst werden können.



### Sammlung - Exiccatenwerke
*List of ID*

Ungeordnete Liste von IDs aus der Sammlungen-Tabelle. Dient der Erfassung von Exiccatenwerken der Person.

> Es ist zu prüfen ob in die Spalten Exiccaten werke, Herbarien und Sontige Sammlungen etwas eingetragen werden muss. Theorethisch sollten in der Sammlungstabelle für jede Sammlung die Autoren über eine ID in diese Quelle erfasst werden. Damit sind die Sammlung implizit bekannt
### Sammlung - Herbarien
*List of ID*

Ungeordnete Liste von IDs aus der Sammlungen-Tabelle. Dient der Erfassung von Herbarien der Person.

### Sammlung - Sonstige Sammlungen
*List of ID*

Ungeordnete Liste von IDs aus der Sammlungen-Tabelle. Dient der Erfassung von sonstigen Sammlungen der Person.
