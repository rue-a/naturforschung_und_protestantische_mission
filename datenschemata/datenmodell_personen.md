# Datenmodell – Personen

## Präambel

> So hervorgehobene Textteile sind Kommentare.

Die hier beschreibene Tabelle hat zwei Funktionen: 1) Arbeitswerkzeug zur Sammlung übergeordneter Informationen zu relevanten Personen und 2) Quelle zur Erzeugung einer Website, welche relevante Teile der gesammelten Informationen für eine breite Öffentlichkeit zugänglich darstellt. Alle Informationen, die dem zweiten Zweck dienen, müssen strukturiert erfasst werden. Dieses Dokument beschreibt alle Spalten, welche diesem zweiten Zweck dienen.


> Farbkodierung der Spalten:
> - weiß: Informationen werden auf der Website präsentiert
> - rot-orange: wird gelöscht, enthält aber noch Informationen für andere Spalten
> - gelb: Bezeichnung wird noch geändert
> - blau: Information ist implizit in anderen Tabellen enthalten, kann gelöscht werden, wenn sonst nicht notwendig. Kann auch als Arbeitsspalte umfunktioniert werden. 
> - grau: Arbeitsspalte, wird nirgends mit angezeigt oder ausgewertet. Kann beliebig befüllt werden.

## Felder (Spalten)


### ID
*ID*

Eindeutiger Identifier der Person.

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

### Name - Vorzugsname
*String*

Dient der Darstellung, z.B. auf der Website.
- `Johann Baptist von Albertini`.
- `Alexander Becker` 
- `Carl Gustav von Brinkmann`
- `Dr. August Herrmann Francke`
- `Constantin Theodor Glitsch`

### Name - Anmerkungen
*String*

Freitextfeld für Notizen in Bezug auf den Namen, z.B. weitere Informationen zu alternativen Schreibweisen oder Auflösung von Abkürzungen.

### Zugehörigkeit Herrnhuter Brüdergemeine
*List of String from Codelist*

> Die Codelist ist noch zu definieren, Vorschlag:

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

### Geburt - Datum - Notizen
*String*

### Geburt - Ort - Geburtsorte
*List of ID*

Liste möglicher Geburtsorte der Person. Die Geburtsorte sind in absteigender Plausibilität zu ordnen. Die Angabe der Orte erfolgt mittels Verweis auf einen Eintrag in der Gazetteer-Tabelle, d.h. über eine *ID*, welche mit dem Buchstaben *L* beginnt.

### Geburt - Ort - Quellen
*List of Reference*

Liste der Quellen der Geburtsorte in der Reihenfolge der entsprechenden Geburtsorte.

### Geburt - Ort - Notizen
*String*

### Tod - Datum - Todesdaten
*List of Date_ISO8601-2*

Liste möglicher Todesdaten der Person. Die Todesdaten sind in absteigender Plausibilität zu ordnen.

### Tod - Datum - Quellen
*List of Reference*

Liste der Quellen der Todesdaten in der Reihenfolge der entsprechenden Todesdaten.

### Tod - Datum - Notizen
*String*

### Tod - Ort - Todesorte
*List of ID*

Liste möglicher Todesorte der Person. Die Todesorte sind in absteigender Plausibilität zu ordnen. Die Angabe der Orte erfolgt mittels Verweis auf einen Eintrag in der Gazetteer-Tabelle, d.h. über eine *ID*, welche mit dem Buchstaben *L* beginnt.

### Tod - Ort - Quellen
*List of Reference*

Liste der Quellen der Todesorte in der Reihenfolge der entsprechenden Todesorte.

### Tod - Ort - Notizen
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
