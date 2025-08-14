# Datentypen

Beschreibung der Datentypen, welche in den Datenschemata verwendet werden.

## Generische Datentypen

- **`Integer`**: Eine ganze Zahl ohne Dezimal- oder Bruchteile.
- **`String`**: Eine Abfolge von nicht näher bestimmten Zeichen.
- **`Structured String`**: Eine Zeichenkette, die einem bestimmten, vorhersehbaren Muster zur Darstellung von Informationen folgt (der unten beschriebene _Date_-Datentyp ist ein solcher strukturierter String). In mehreren Feldern verwendete Strukturierte Strings sind unter **Spezielle Datentypen** definiert, andernfalls erfolgt die Definition direkt in der Dokumentation des entsprechenden Feldes.

## Spezielle Datentypen

- **`ID`**: Eine ID ist ein alphanumerischer, innerhalb dieses Projekts eindeutiger, Identifikator für Objekte (Zeilen) in Tabellen dieses Objekts. Die Vergabe dieser Identifikatoren erlaubt eindeutige Link zwischen Tabellen. Jede *ID* beginnt mit einem Großbuchstaben, welcher die Tabelle in der die zu identifizierenden Objekte stehen anzeigt, danach folgt eine, innerhalb der entsprechenden Tabelle einmalige, Zahl mit 7 Ziffern.
	- `P1035000` (ID in der Personentabelle)
	- `R0010000` (ID in der Literaturquellentabelle)
	- `L0010500` (ID in der Ortstabelle)
    - `C0028000` (ID in der Sammlungstabelle)
Die Vergabe der IDs basiert auf der Idee des _Frational Indexing_.

> [!TIP]
> **Fractional Indexing Variante mit Ganzzahlen**
> Ein Verfahren zur Vergabe von Positionswerten (IDs) in einer sortierten Liste, bei dem initial große Abstände zwischen den Werten gelassen werden (z. B. 1000, 2000, 3000). Beim Einfügen neuer Einträge wird ein Wert zwischen zwei bestehenden gewählt – nicht zwingend der arithmetische Mittelwert, sondern ein beliebiger Wert innerhalb des freien Intervalls –, um die Reihenfolge beizubehalten, ohne bestehende IDs neu zu vergeben.
>
> _Strategie zur Wertvergabe:_
>
> Zwischen zwei bestehenden IDs wird zunächst das größte noch freie Intervall in Zehntelschritten genutzt. Sobald diese Zehntelschritte ausgeschöpft sind, wird rekursiv auf kleinere Einheiten innerhalb des verbleibenden Intervalls gewechselt (z. B. Hundertstel, Tausendstel). So wird der Zahlenraum planvoll von grob zu fein aufgeteilt, was langfristig viele Einfügungen ohne Umnummerierung erlaubt.
>
> _Beispiel, alphabetisch geoordnete Liste von Namen:_
> - 1000 – Albert
> - 2000 – Boris.
>
> Es soll der Name Almut zwischen Albert und Boris eingefügt werden.
> Es kann hier einfach der Mittelwert 1500 gewählt werden, _oder besser_, ein Wert näher an 1000 als an 2000, da Almut lexikographisch näher an Albert liegt als an Boris, z.B. 1200 oder 1300:
> - 1000 – Albert
> - 1200 – Almut
> - 2000 – Boris.
>
> Falls danach Alma zwischen Albert (1000) und Almut (1200) eingefügt werden soll, wird der nächste Zehntelschritt 1100 gewählt:
> - 1000 – Albert
> - 1100 – Alma
> - 1200 – Almut
> - 2000 – Boris.
>
> Soll nun ein weiter Name, Alda, zwischen Albert und Alma eingefügt werden soll, sind die Zehntelschritte zwischen diesen beiden Namen aufgebraucht und die ID im Bereich der Hundertstelschritte zwischen 1000 und 1100 gewählt:
> - 1000 – Albert
> - 1030 – Alda
> - 1100 – Alma
> - 1200 – Almut
> - 2000 – Boris.
>
> Sind die Hundertstelschritte zwischen zwei Werten auch aufgebraucht, geht es in Tausendstelschritten weiter. Im vorliegenden Beispiel schlägt das System an nach dem Auschöpfen der Tausendstelschritte fehl. Um das zu vermeiden, sollten Stellenzahl und Startabstände der initialen IDs so großzügig gewählt werden, dass ein späteres Ausschöpfen des Bereichs sehr unwahrscheinlich ist. Der Vorteil der Ganzzahl-Variante bleibt die gute Lesbarkeit und die einfache manuelle Handhabung.


- **`Date`**: Taggenaue Angabe eines Datums im Format `YYYY-MM-DD` (ISO 8601).
	- `YYYY`: Jahr mit vier Ziffern
	- `MM`: Monat mit zwei Ziffern
	- `DD`: Tag mit zwei Ziffern    
	- z. B.: `2025-04-08`

- **`ISO8601-2_Date`**: 
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
	
- **`ISO8601-2_Period`**: Angabe einer Zeitspanne, welche mithilfe zweier *ISO8601-2_Date* Strings konstruiert wird. Die beiden *ISO8601-2_Date* Strings repräsentieren den Anfang und das Ende der Zeitspanne und werden durch ein Solidus Symbol `/` (ohne umgebende Leerzeichen) getrennt.
	- `1872-06-06/1827-06-12?` ⇾ vom 6. Juni 1872 bis etwa 12. Juni 1872.
	- `1899/1907` ⇾ von 1899 bis 1907
	- `1698/1702-04-02` ⇾ Zeitspanne beginnt irgendwann im Jahr 1698 und endet am 2. April 1702.

- **`Temporal_ISO8601-2`**: In diesem Feld sind *ISO8601-2_Date* und *ISO8601-2_Period* Strings erlaubt.
 
- **`URL`**: Ein strukturierter String gemäß [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986), aber eingeschränkt auf das Schema `https` (oder notfalls `http`). URLs sollten immer aus der Browserleiste in das Dokument kopiert und nie per Hand eingetragen werden.

- **`Reference-analog`**: Dient dem Nachweis eines Sachverhalts, mittels eines gedruckten Werks unter Angabe der Seiten auf welchen der Nachweis zu finden ist. Der Nachweisstring ist wie folgt strukturiert `<ID aus Literaturquellentabelle, <Angabe der Seiten>`, d.h. die Quelle und die Angabe der Seiten sind durch *ein Komma und ein Leerzeichen* voneinander getrennt.
	-  `R13, p237ff` (Schriftliche Quelle, erfasst unter der *ID* R13, gesuchter Nachweis auf Seiten 237 und folgende)

- **`Reference`** In diesem Feld sind *URL* und *Reference-Printet*  Strings erlaubt.

## Listen

Wenn der Wertebereich eines Feldes Liste (`List`) ist, bedeutet das, dass mehrere Werte erlaubt sind. Die Werte müssen durch das Pipe Symbol, umgeben von zwei Leerzeichen getrennt werden (`a | b | c`). 

Wenn der Wertebereich eines Feldes `List of <datatype>` ist, müssen die Werte der Liste den obigen Definitionen entsprechen, z.B.: `List of Integers`.

Listen müssen nicht immer mehrere Elemente enthalten.

## Codelisten

Das Suffix `from Codelist` kann an einen generischen Datentyp angehängt werden. Es bedeutet, dass die Werte aus einer vordefinierten Liste von zulässigen Werten (einer Codeliste) ausgewählt werden müssen. Eine Codeliste könnte z.B. `Nadelbäume` heißen und die Werte `Fichte, Tanne, Kiefer, Lärche` enthalten. Ein Datentyp könnte dann `String from Nadelbäume` sein. Auch möglich wäre eine Liste mit Werten aus einer Codeliste, also z.B. `List of Strings from Nadelbäume`.

Codelisten sind im Tabellenblatt Codelisten zu definieren.

