# Felder (Spalten)

## Erforderlich

### id
*String*

Interner Identifikator des Beitragenden.  
Muss innerhalb des Datensatzes eindeutig sein und bleibt während des gesamten Aufnahme-Workflows unverändert, einschließlich späterer Aktualisierungen.

---

### title
*String*

Ein einzelner „bevorzugter“ Ortsname, der als Titel für den Datensatz dient.

---

### title_source
*String*

Bezeichnung oder kurze Quellenangabe für die Herkunft des Titel-Typonyms, in beliebigem Zitierstil.  
Beispiele:  
- `An Historical Atlas of Central Asia (Bregel, 2003)`  
- `The Historical Sample of the Netherlands (https://iisg.amsterdam/nl/hsn)`

---

### fclasses *
*List of Strings from Codelist*

Jede Zeile muss entweder einen **fclasses**-Wert oder einen **aat_types**-Wert enthalten.  
Ein oder mehrere der sieben einbuchstabigen *GeoNames Feature Classes*, getrennt durch Semikolon.  
Beispiele: `P` oder `P;A`

Mögliche Werte:  
- **A:** Verwaltungseinheiten (z. B. Länder, Provinzen, Gemeinden)  
- **H:** Gewässer (z. B. Flüsse, Seen, Buchten, Meere)  
- **L:** Regionen, Landschaftsbereiche (kulturell, geografisch, historisch)  
- **P:** Siedlungen (z. B. Städte, Dörfer, Weiler)  
- **R:** Straßen, Routen, Schienenwege  
- **S:** Stätten (z. B. archäologische Stätten, Gebäude, Anlagen)  
- **T:** Landformen (z. B. Berge, Täler, Kaps)

> **Hinweis:** Die Angabe von fclasses verbessert die Qualität der automatischen Abgleichergebnisse, da irrelevante Objekte ausgeschlossen werden.

---

### aat_types *
*List of Integers from Codelist*

Jede Zeile muss entweder einen **fclasses**-Wert oder einen **aat_types**-Wert enthalten.  
Ein oder mehrere AAT-Integer-IDs aus der WHG-Teilliste von 176 Orts-Typkonzepten.  
Die Werte sind durch Semikolon getrennt.  

**Regeln:**  
- Ein Datensatz kann einen **types**-Wert ohne zugehörigen **aat_types**-Wert haben, aber nicht umgekehrt.  
- Für jeden Wert in **aat_types** muss es einen entsprechenden Wert in **type** geben (1:1).  
- Wenn für einen **type** kein **aat_type** existiert, die Position leer lassen.  
- Keine AAT-Hierarchien duplizieren – nur den spezifischen Typ verwenden.

---

### attestation_year und/oder start
*Date_ISO8601*

Die Felder **start** und **end** geben den bekannten Gültigkeitszeitraum des Ortsnamens an.  
Das Feld **attestation_year** enthält das Veröffentlichungsjahr der **title_source**.

Jede Zeile muss mindestens ein **attestation_year** oder einen **start**-Wert enthalten.  
Alle Werte müssen im ISO-8601-Format angegeben werden (YYYY-MM-DD), Monat und Tag dürfen weggelassen werden.  
BCE-Daten (v. Chr.) werden als negative Ganzzahl geschrieben, z. B. `-320`.

> **Hinweise:**  
> - **start** + **end** kennzeichnen einen vollständigen Zeitraum.  
> - Nur **start** bedeutet „ab“, Ende unbekannt oder heute.  
> - Die Werte entsprechen im Linked Places JSON-LD dem „when“-Objekt auf Datensatzebene.

---

## Empfohlen

### title_uri
*URL*

Permanenter Link zur Quelle des Titel-Typonyms, z. B.:  
- `http://www.worldcat.org/oclc/890934416`  
- `https://doi.org/10.7910/DVN/AMPGMW`  
- `https://www.davidrumsey.com/luna/servlet/s/em7n8q`

---

### ccodes
*List of Strings from Codelist*

Ein oder mehrere ISO-Alpha-2-Ländercodes (modern), die den Ort abdecken oder schneiden.  
- Werte durch Semikolon trennen.  
- Dienen der räumlichen Eingrenzung für Suchen; keine Aussage über administrative Zugehörigkeit.  
- Falls nicht angegeben, wird bei vorhandener Geometrie der Wert automatisch berechnet.

---

### matches
*List of Strings (URIs mit Präfix)*

Ein oder mehrere URIs zu übereinstimmenden Datensätzen in Ortsnamenautoritäten.  
Die Kurzpräfixe laut WHG müssen anstelle der vollen Basis-URIs verwendet werden, z. B.:  
- `wd:Q5684` (Wikidata, Babylon)

Unterstützte Präfixe:  
`bnf`, `cerl`, `dbp`, `gn`, `gnd`, `gov`, `loc`, `pl`, `tgn`, `viaf`, `wd`, `wp`

---

### variants
*List of Strings*

Namens- und/oder Sprachvarianten nach BCP 47-Standard:  
`{Name}@Sprache[-Schrift][-Region][-Variante]`  
Mehrere Namen durch Semikolon trennen.

Beispiele:  
- `Zanzibar@sw`  
- `زنجبار@ar`  
- `Zanzíbar@es-ES`  
- `Sansibar@de-DE-1901`  
- `蒙巴萨@zh-Hans-CN`

---

### types
*List of Strings*

Ein oder mehrere Begriffe für den Ortstyp, in der Regel wortwörtlich aus der Quelle übernommen.  
Mehrere Werte durch Semikolon trennen.

---

## Optional

### parent_name
*String*

Übergeordnete Verwaltungseinheit oder Region (z. B. Provinz, Land).  
Für jedes `parent_name` muss auch ein `parent_id` angegeben werden.

---

### parent_id
*URL*

URI zu einem veröffentlichten Datensatz, der den `parent_name` beschreibt.  
Darf nicht ohne zugehöriges `parent_name` vorkommen.

---

### lon
*Decimal*

Längengrad in WGS84 (EPSG:4326), z. B. `85.3214` oder `-112.4536`.

---

### lat
*Decimal*

Breitengrad in WGS84 (EPSG:4326), z. B. `59.3345` oder `-12.7658`.

---

### geowkt
*String (WKT-Format)*

Geometrie im OGC-WKT-Format.  
Falls vorhanden, wird geowkt gegenüber lon/lat bevorzugt.  

---

### geo_source
*String*

Quellenangabe der Geometrie, z. B. `GeoNames` oder `digitalisierte title_source-Karte`.

---

### geo_id
*URL*

URI zur Quelle der Geometrie.

---

### approximation
*String oder Decimal*

- URI zur Angabe einer Ungenauigkeit, z. B. `gvp:containedWithin`  
- oder Wert in Kilometern als Toleranz für `gvp:approximateLocation`.

---

### end
*Date_ISO8601*

Spätestes relevantes Datum.

---

### description
*String*

Kurzer beschreibender Text zum Ort.
