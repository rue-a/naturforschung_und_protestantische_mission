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

### Generische Datentypen

- **`Integer`**: Eine ganze Zahl ohne Dezimal- oder Bruchteile.
- **`String`**: Eine Abfolge von nicht näher bestimmten Zeichen.
- **`Structured String`**: Eine Zeichenkette, die einem bestimmten, vorhersehbaren Muster zur Darstellung von Informationen folgt (der unten beschriebene _Date_-Datentyp ist ein solcher strukturierter String). In mehreren Feldern verwendete Strukturierte Strings sind unter **Spezielle Datentypen** definiert, andernfalls erfolgt die Definition direkt in der Dokumentation des entsprechenden Feldes.

### Spezielle Datentypen

- **`ID`**: Eine ID ist ein alphanumerischer, innerhalb dieses Projekts eindeutiger, Identifikator für Objekte (Zeilen) in Tabellen dieses Objekts. Die Vergabe dieser Identifikatoren erlaubt eindeutige Link zwischen Tabellen. Jede *ID* beginnt mit einem Großbuchstaben, welcher die Tabelle in der die zu identifizierenden Objekte stehen anzeigt, danach folgt eine, innerhalb der entsprechenden Tabelle einmalige, Zahl unbestimmter Länge.
	- `P1035` (ID in der Personentabelle)
	- `R1` (ID in der Literaturquellentabelle)
	- `L105` (ID in der Ortstabelle)
    - `C28` (ID in der Sammlungstabelle)

- **`Date`**: Taggenaue Angabe eines Datums im Format `YYYY-MM-DD` (ISO 8601).
	- `YYYY`: Jahr mit vier Ziffern
	- `MM`: Monat mit zwei Ziffern
	- `DD`: Tag mit zwei Ziffern    
	- z. B.: `2025-04-08`

- **`Date_ISO8601-2`**: 
	Angabe eines tag- bis jahrgenauen Zeitpunkts gemäß ISO 8601-1 ( [de](https://katalog.slub-dresden.de/id/211-DE30087040), [en](https://katalog.slub-dresden.de/id/211-IX30556316) ) und unter Verwendung der in ISO 8601-2 ([en](https://katalog.slub-dresden.de/id/211-IX30556317), Abschnitt 4.5) definierten Affixe zur Angabe von Unsicherheiten. 
	Die in ISO 8601-1 definierten Regeln werden eingeschränkt auf tag-, monat- und jahrgenau Angabe eines Zeitpunkts. Somit sind folgende Stringformate gültig:
	- `YYYY-MM-DD`, z.B. `2025-04-08` ⇾ ein Zeitpunkt am 8. April 2025,
	- `YYYY-MM`, z.B. `2025-04` ⇾ ein Zeitpunkt im April 2025,
	- `YYYY`, z.B. `2025` ⇾ ein Zeitpunkt im Jahr 2025.
	ISO 8601-2 definiert drei Affixe zur Angabe von Unsicherheiten bei der Angabe von Zeitpunkten:
	- `~`: Angabe geschätzt,
	- `?`: Angabe unsicher,
	- `%`: Angabe geschätzt und unsicher.
	Diese Symbole können entweder als Suffix verwendet, also an die einzelnen Elemente (Tag, Monat, Jahr) eines Zeitpunkts angehängt werden oder unter Verwendung als Präfix nur auf die folgende Ziffer.
	- `1872-06-12~` ⇾ `~` suffixiert: der Tag (12.) ist geschätzt (z.B. über Reisegeschwindigkeit). 
	- `1872-06?-12` ⇾ `?` suffixiert: der Monat Juni ist eine unsichere Angabe (z.B. nur implizit gegeben).
	- `1872-0?6-12` ⇾ `?` präfixiert: die zweite Ziffer in der Monatsangabe ist unsicher (z.B. im Original kaum lesbar)
	
- **`Period_ISO8601-2`**: Angabe einer Zeitspanne, welche mithilfe zweier *Date_ISO8601-2* Strings konstruiert wird. Die beiden *Date_ISO8601-2* Strings repräsentieren den Anfang und das Ende der Zeitspanne und werden durch ein Solidus Symbol `/` (ohne umgebende Leerzeichen) getrennt.
	- `1872-06-06/1827-06-12?` ⇾ vom 6. Juni 1872 bis etwa 12. Juni 1872.
	- `1899/1907` ⇾ von 1899 bis 1907
	- `1698/1702-04-02` ⇾ Zeitspanne beginnt irgendwann im Jahr 1698 und endet am 2. April 1702.

- **`Temporal_ISO8601-2`**: In diesem Feld sind *Date_ISO8601-2* und *Period_ISO8601-2* Strings erlaubt.
 
- **`URL`**: Ein strukturierter String gemäß [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986), aber eingeschränkt auf das Schema `https` (oder notfalls `http`). URLs sollten immer aus der Browserleiste in das Dokument kopiert und nie per Hand eingetragen werden.

- **`Reference-analog`**: Dient dem Nachweis eines Sachverhalts, mittels eines gedruckten Werks unter Angabe der Seiten auf welchen der Nachweis zu finden ist. Der Nachweisstring ist wie folgt strukturiert `<ID aus Literaturquellentabelle, <Angabe der Seiten>`, d.h. die Quelle und die Angabe der Seiten sind durch *ein Komma und ein Leerzeichen* voneinander getrennt.
	-  `R13, p237ff` (Schriftliche Quelle, erfasst unter der *ID* R13, gesuchter Nachweis auf Seiten 237 und folgende)

- **`Reference`** In diesem Feld sind *URL* und *Reference-Printet*  Strings erlaubt.

### Listen

Wenn der Wertebereich eines Feldes Liste (`List`) ist, bedeutet das, dass mehrere Werte erlaubt sind. Die Werte müssen durch das Pipe Symbol, umgeben von zwei Leerzeichen getrennt werden (`a | b | c`). 

Wenn der Wertebereich eines Feldes `List of <datatype>` ist, müssen die Werte der Liste den obigen Definitionen entsprechen, z.B.: `List of Integers`.

Listen müssen nicht immer mehrere Elemente enthalten.
### Codelisten

Das Suffix `from Codelist` kann an einen generischen Datentyp angehängt werden. Es bedeutet, dass die Werte aus einer vordefinierten Liste von zulässigen Werten (einer Codeliste) ausgewählt werden müssen. Eine Codeliste könnte z.B. `Nadelbäume` heißen und die Werte `Fichte, Tanne, Kiefer, Lärche` enthalten. Ein Datentyp könnte dann `String from Nadelbäume` sein. Auch möglich wäre eine Liste mit Werten aus einer Codeliste, also z.B. `List of Strings from Nadelbäume`.

Codelisten sind im Tabellenblatt Codelisten zu definieren.


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
| `ja(b)`     | Übernahme von Funktionen und Ausübung von Ämtern innerhalb der Brüdergemeine                                   |
| `nein(a)`   | aber wichtig im Netzwerk                                                                                       |
| `nein(b)`   | um Verwechslung auszuschließen                                                                                 |
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
