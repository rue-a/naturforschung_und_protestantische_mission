# Parsing Errors

## Personen

### P0010000

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0010000:
  - Error Message: **`PersonID must start with 'P': Christlieb Reichel`**
  - Causing raw value: `Christlieb Reichel {R0000900} `
  - Full field: _P1430000 {R0000900} |
Christlieb Reichel {R0000900} |
P0300000 {R0000900} | 
Ferdinand Wunderling {R0000900} | 
P1500000 {R0000900} | _

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0010000:
  - Error Message: **`PersonID must start with 'P': Ferdinand Wunderling`**
  - Causing raw value: ` 
Ferdinand Wunderling {R0000900} `
  - Full field: _P1430000 {R0000900} |
Christlieb Reichel {R0000900} |
P0300000 {R0000900} | 
Ferdinand Wunderling {R0000900} | 
P1500000 {R0000900} | _

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`Invalid format for ManuscriptID: M0004700 : Flora Nieskiensis (unsichere Zuschreibung zu Albertini durch R0001600)]`**
  - Causing raw value: `M0004700 [1815: J.B.v. Albertini: Vorwort. in: [anonym]: Flora Nieskiensis (unsichere Zuschreibung zu Albertini durch R0001600)] `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`Invalid format for ManuscriptID: M0004900 1814-1817 ]`**
  - Causing raw value: `M0004900 [1814-1817: J.B.v. Albertini: Flora Montis Gratiarum [Gnadenberg] 1814-1817 ]`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`Invalid format for ManuscriptID: M0005000 1814-1817]`**
  - Causing raw value: `M0005000 [1819: J.B.v. Albertini: Flora montis Gratiarum [Gnadenberg] 1814-1817] `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`Invalid format for ManuscriptID: M0005100 1814]`**
  - Causing raw value: `M0005100 [1814ff.: J.B.v. Albertini: Adnota ad Floram Montis Gratiarum [Gnadenberg] 1814] `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`Invalid format for ManuscriptID: M0005200 : Albertini’s Flora Gnadenfrei’s 1819-1821]`**
  - Causing raw value: `M0005200 [1842: [anonym]: Albertini’s Flora Gnadenfrei’s 1819-1821] `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`Invalid format for ManuscriptID: M0005400 : Flora Albertini Gnadenfreyensis (Verändert nach Cur. 4. Aufl. 1840.)]`**
  - Causing raw value: `M0005400 [nach 1840: [anonym]: Flora Albertini Gnadenfreyensis (Verändert nach Cur. 4. Aufl. 1840.)] `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`ManuscriptID must start with 'M': , 1819, 90 Seiten, 73 mit Text, (Stolz, 1916, 112), Cim.II.16.II „NOTAMINA ad Floram Gnadenfreiensem. Inde a vere 1819.“; , 1819, 202 Seiten, dazwischen Leerseiten mit Text, gebunden (Stolz, 1916, 112), Cim.II.16.III „FLORA GNADENFREYENSIS 1819. 1820. pp.“, , 1819, geheftet,Einleitung mit Angabe des Gebietes der Flora Gnadenfreiensis, und der Referenzliteratur, Gesamtbestand der Flora am „5. Jul. 1821“ 1.355 Arten, Cim.II.16.III „Diarium botanicum, numerans Stirpens quoquo die inventas.“ ; lose, deutsch Aufistung Botanischer Exkursionen, mit Datum und Route und neu gefundenem Bestand, 1819, 117 Exkursionen mit 957 Arten, 1820, 90 Exkursionen mit 398 Arten plus Ergänzungen am „30.Sept. 1820“ 1354 Arten`**
  - Causing raw value: `[1821:  „Flora Gnadenfreyensis. 1819/20. 8°. Dazu: Catalogi auxiliares tres ad Fl. G.“ 2 Exemplare; a) (Mspt., datirt vom 5. Juli 1821. Mspt. Sammlung der Schles. Ges.) (Karl Gustav Limpricht: "Nachträge zu den Laub- und Lebermoosen", in: Ferdinand Cohn, Kryptogamen-Flora von Schlesien, Beslau: J.U. Kern's Verlag 1876, S. 413-444, 444, ebenfalls erwähnt in Körber: "Verzeichniss der dem Henschel'schen Globus aggregirten botanischen Manuscript-Sammlung der Schlesischen Gesellschaft", in: Bericht über die Thätigkeit der Botanischen Section der Schlesischen Gesellschaft für Vaterländische Kultur, 1871, S. 88-93, 88); b) UA, Cim.II.16. Flora Gnadenfreiensis, 1819-1821, Johann Baptist von Albertini, 3 Hefte; Gnadenfrei/ Piława Górna/ Ober-Peilau in Schlesien, 3 separate Hefte mit Signatur: Cim.II.16.I „FLORA GNADENFREIENSIS, Inde a vere 1819.“; [J.B.v. Albertini], 1819, 90 Seiten, 73 mit Text, (Stolz, 1916, 112), Cim.II.16.II „NOTAMINA ad Floram Gnadenfreiensem. Inde a vere 1819.“; [J.B.v. Albertini], 1819, 202 Seiten, dazwischen Leerseiten mit Text, gebunden (Stolz, 1916, 112), Cim.II.16.III „FLORA GNADENFREYENSIS 1819. 1820. pp.“, [J.B.v. Albertini], 1819, geheftet,Einleitung mit Angabe des Gebietes der Flora Gnadenfreiensis, und der Referenzliteratur, Gesamtbestand der Flora am „5. Jul. 1821“ 1.355 Arten, Cim.II.16.III „Diarium botanicum, numerans Stirpens quoquo die inventas.“ [Ein botanisches Tagebuch, das jeden Tag den gefundenen Bestand zählt]; lose, deutsch Aufistung Botanischer Exkursionen, mit Datum und Route und neu gefundenem Bestand, 1819, 117 Exkursionen mit 957 Arten, 1820, 90 Exkursionen mit 398 Arten plus Ergänzungen am „30.Sept. 1820“ 1354 Arten `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`ManuscriptID must start with 'M': 1822: Kryptogamische Gewächse um Gnadenberg, 1814-1817 und um Gnadenfrey, 1820-1821 gesammelt, 4°, Manuskr. 1822, im Archiv der Schlesischen Gesellschaft für vaterländische Cultur Breslau (erwähnt von: Körber: "Verzeichniss der dem Henschel'schen Globus aggregirten botanischen Manuscript-Sammlung der Schlesischen Gesellschaft", in: Bericht über die Thätigkeit der Botanischen Section der Schlesischen Gesellschaft für Vaterländische Kultur, 1871, S. 88-93, 88; Funkenachlass HB Dresdense Scan 10)`**
  - Causing raw value: `1822: Kryptogamische Gewächse um Gnadenberg, 1814-1817 und um Gnadenfrey, 1820-1821 gesammelt,  4°, Manuskr. 1822, im Archiv der Schlesischen Gesellschaft für vaterländische Cultur Breslau (erwähnt von: Körber: "Verzeichniss der dem Henschel'schen Globus aggregirten botanischen Manuscript-Sammlung der Schlesischen Gesellschaft", in: Bericht über die Thätigkeit der Botanischen Section der Schlesischen Gesellschaft für Vaterländische Kultur, 1871, S. 88-93, 88; Funkenachlass HB Dresdense Scan 10)`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`ManuscriptID must start with 'M': weitere Floren über Riesengebirge, Gnadenberg, Böhmische Berge, Leitmeritzer Gegend`**
  - Causing raw value: `weitere Floren über Riesengebirge, Gnadenberg, Böhmische Berge, Leitmeritzer Gegend `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`ManuscriptID must start with 'M': Kopien/Anschriften von Thust : UA NB VI.185.7 , Albertini: „Res Botanicae“, „Albertini’s Flora Gnadenfrei’s“, aus dem Nachlass von Thust, Absch. um 1842, Abschrift kompiliert aus: Albertini: „Flora Gnadenfreiensis, Indea vere 1819“ und Albertini: „Notamina ad Floram Gnadenfr. Indea vere 1819; 153 gez. S. plus ungez. 1 kolol. Zeichnung dat. „Okt. 1842“; UA NB VI.185.8 Albertini: „Flora Albertini Gnadenfreyensis“, Abschrift nach der 4. Aufl. 1840, aus dem Nachlass von Thust, 48 S. von 1018 Arten, plus Pilze und Vergleich Pilze Gnadenfrei und Gnadenfeld`**
  - Causing raw value: ` 
[1842] Kopien/Anschriften von Thust : UA NB VI.185.7 , Albertini: „Res Botanicae“, „Albertini’s Flora Gnadenfrei’s“, aus dem Nachlass von Thust, Absch. um 1842, Abschrift kompiliert aus: Albertini: „Flora Gnadenfreiensis, Indea vere 1819“ und Albertini: „Notamina ad Floram Gnadenfr. Indea vere 1819; 153 gez. S. plus ungez. 1 kolol. Zeichnung dat. „Okt. 1842“; UA NB VI.185.8  Albertini: „Flora Albertini Gnadenfreyensis“, Abschrift nach der 4. Aufl. 1840, aus dem Nachlass von Thust, 48 S. von 1018 Arten, plus Pilze und Vergleich Pilze Gnadenfrei und Gnadenfeld `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0010000:
  - Error Message: **`ManuscriptID must start with 'M': ]`**
  - Causing raw value: `]`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0010000:
  - Error Message: **`LiteratureID must start with 'R': Verzeichniß der in der Oberlausitz und den angrenzenden Theilen Schlesiens und Böhmens wildwachsenden Farrenkräutern", in: Neues Lausitzisches Magazin 3 (1824), S. 62–74`**
  - Causing raw value: `Verzeichniß der in der Oberlausitz und den angrenzenden Theilen Schlesiens und Böhmens wildwachsenden Farrenkräutern", in: Neues Lausitzisches Magazin 3 (1824), S. 62–74 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0010000:
  - Error Message: **`LiteratureID must start with 'R': Verzeichniß der in der Ober-Lausitz wachsenden Orchideen", in: Neues Lausitzisches Magazin 5 (1826), S. 509-515`**
  - Causing raw value: `Verzeichniß der in der Ober-Lausitz wachsenden Orchideen", in: Neues Lausitzisches Magazin 5 (1826), S. 509-515 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0010000:
  - Error Message: **`LiteratureID must start with 'R': Ueber die in der Ober-Lausitz wild wachsenden Pflanzen aus der Familie der Asperifolien, in: Neues Lausitzisches Magazin 7 (1828), S. 356-360`**
  - Causing raw value: `Ueber die in der Ober-Lausitz wild wachsenden Pflanzen aus der Familie der Asperifolien, in: Neues Lausitzisches Magazin 7 (1828), S. 356-360 `

- [ ] Error in Col: **Wichtige Werke der Person ohne botanischen Kontext** and row with ID P0010000:
  - Error Message: **`Invalid work id: 402 Gedichte (should be R-ID, or M-ID)`**
  - Causing raw value: `402 Gedichte {R0000900}`

### P0011000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0011000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0011000:
  - Error Message: **`Invalid work id: UA, R.22.95.1 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, R.22.95.1`

### P0020000

- [ ] Error in Col: **Links - GND** and row with ID P0020000:
  - Error Message: **`URL is not valid: nein (2025-04-17)`**
  - Causing raw value: `nein (2025-04-17)`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0020000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Tod - Ort** and row with ID P0020000:
  - Error Message: **`Invalid format for LocationID: L1500000 (UA, Dienerblätter A-Bl, S. 53)`**
  - Causing raw value: `L1500000 (UA, Dienerblätter A-Bl, S. 53)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0020000:
  - Error Message: **`Expected 4 parts, got 7: 1829/1832; ; Knabenanstalt; Aufseher (UA, Dienerblätter A-Bl. S. 53)1832/1835; L1200000 ; Missionar;`**
  - Causing raw value: `1829/1832; [Königsfeld]; Knabenanstalt; Aufseher (UA, Dienerblätter A-Bl. S. 53)
1832/1835; L1200000 [Hopedal]; Missionar; {R0000700} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0020000:
  - Error Message: **`Expected 4 parts, got 7: 1838/1839; ; ; (UA, Dienerblätter A-Bl. S. 53)1835/1845; L2100000 ; Missionar;`**
  - Causing raw value: `1838/1839; [Europa]; ; (UA, Dienerblätter A-Bl. S. 53)
1835/1845; L2100000 [Nain]; Missionar; {R0000700} `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0020000:
  - Error Message: **`Invalid work id: UA, Dienerblätter A-Bl, S. 53 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, Dienerblätter A-Bl, S. 53`

### P0030000

- [ ] Error in Col: **Links - GND** and row with ID P0030000:
  - Error Message: **`URL is not valid: nein (2024-09-11)`**
  - Causing raw value: `nein (2024-09-11)`

- [ ] Error in Col: **Links - Bionomia** and row with ID P0030000:
  - Error Message: **`URL is not valid: nein (2024-09-11)`**
  - Causing raw value: `nein (2024-09-11)`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0030000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0030000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1813-02-08 (UA, Dienerblätter A-Bl, S. 68-69)`**
  - Causing raw value: `1813-02-08 (UA, Dienerblätter A-Bl, S. 68-69)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0030000:
  - Error Message: **`Invalid format for LocationID: L2290000 (UA, Dienerblätter A-Bl, S. 68-69)`**
  - Causing raw value: `L2290000 (UA, Dienerblätter A-Bl, S. 68-69)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0030000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1899-09-28 (UA, Dienerblätter A-Bl, S. 68-69)`**
  - Causing raw value: `1899-09-28 (UA, Dienerblätter A-Bl, S. 68-69)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0030000:
  - Error Message: **`Invalid format for LocationID: L1120000 (UA, Dienerblätter A-Bl, S. 68-69)`**
  - Causing raw value: `L1120000 (UA, Dienerblätter A-Bl, S. 68-69)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0030000:
  - Error Message: **`Invalid work id: UA, Dienerblätter A-Bl, S. 68-69 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, Dienerblätter A-Bl, S. 68-69`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0030000:
  - Error Message: **`Invalid work id: UA NB.VI. 63,nr.1UA NB.VI. 63,nr.2, S. 93 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA NB.VI. 63,nr.1
UA NB.VI. 63,nr.2, S. 93`

### P0040000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0040000:
  - Error Message: **`URL is not valid: nein (2024-09-11)`**
  - Causing raw value: `nein (2024-09-11)`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0040000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0040000:
  - Error Message: **`Expected 4 parts, got 3: 1796/1809; Ebersdorf; Gemeinvorsteher in Ebersdorf`**
  - Causing raw value: `1796/1809; Ebersdorf; Gemeinvorsteher in Ebersdorf {https://d-nb.info/gnd/1081213442}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0040000:
  - Error Message: **`Invalid work id: UA, R.22.31.01 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, R.22.31.01`

### P0040500

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0040500:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0040500:
  - Error Message: **`Invalid Reference Document value: UA, R.22.20.12 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `1788-04-05 {UA, R.22.20.12}`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0040500:
  - Error Message: **`Invalid Reference Document value: UA, R.22.20.12 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Steinbach {UA, R.22.20.12}`

- [ ] Error in Col: **Tod - Datum** and row with ID P0040500:
  - Error Message: **`Invalid ISO8601-2_Date format: 1815-08-05 (UA, R.22.20.12)`**
  - Causing raw value: `1815-08-05 (UA, R.22.20.12)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0040500:
  - Error Message: **`Invalid Reference Document value: UA, R.22.20.12 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `L0800000 {UA, R.22.20.12}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0040500:
  - Error Message: **`Expected 4 parts, got 1: Ebersdorf (Apotheker)`**
  - Causing raw value: `Ebersdorf (Apotheker)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0040500:
  - Error Message: **`Invalid work id: UA, R.22.20.12 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, R.22.20.12`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0040500:
  - Error Message: **`PersonID must start with 'P': Breutel`**
  - Causing raw value: `Breutel [Botanik in Ebersdorf]`

### P0050000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0050000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `; Niesky;; {R0006500} `
  - Full field: _; Niesky;; {R0006500} |
; Rossitten;; {R0006500} |
 ;L2450000; {R0006600} | _

- [ ] Error in Col: **Wirkungsorte** and row with ID P0050000:
  - Error Message: **`LocationID must start with 'L': Rossitten`**
  - Causing raw value: `; Rossitten;; {R0006500} `
  - Full field: _; Niesky;; {R0006500} |
; Rossitten;; {R0006500} |
 ;L2450000; {R0006600} | _

- [ ] Error in Col: **Wirkungsorte** and row with ID P0050000:
  - Error Message: **`Expected 4 parts, got 3: ;L2450000;`**
  - Causing raw value: ` ;L2450000; {R0006600} `
  - Full field: _; Niesky;; {R0006500} |
; Rossitten;; {R0006500} |
 ;L2450000; {R0006600} | _

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0050000:
  - Error Message: **`Invalid work id: UA. Cim.V.15-7: Anfrage an die Herrnhuter in Grönland und Labrdor um nach Säugetieren und Schädeln für Museum Niesky und Verkauf mit Angabe von Inuitnamen und Preisen und Präparerungshinweisen (should be R-ID, or M-ID)`**
  - Causing raw value: `UA. Cim.V.15-7: Anfrage an die Herrnhuter in Grönland und Labrdor um nach Säugetieren und Schädeln für Museum Niesky und Verkauf mit Angabe von Inuitnamen und Preisen und Präparerungshinweisen`

### P0060000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0060000:
  - Error Message: **`Provided string is not in codelist: ja (aufgenomen 1831)`**
  - Causing raw value: `ja (aufgenomen 1831)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0060000:
  - Error Message: **`LocationID must start with 'L': Skerhuus (Schleswig) (UA, Dienerblätter A-Bl, S. 234)`**
  - Causing raw value: `Skerhuus (Schleswig) (UA, Dienerblätter A-Bl, S. 234)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0060000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1893-04-24 (UA, Dienerblätter A-Bl. S, 234)`**
  - Causing raw value: `1893-04-24 (UA, Dienerblätter A-Bl. S, 234) {R0004100}`

- [ ] Error in Col: **Tod - Ort** and row with ID P0060000:
  - Error Message: **`Invalid Reference Document value: UA, Dienerblätter A-Bl, S. 234 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `L1120000 {UA, Dienerblätter A-Bl, S. 234}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0060000:
  - Error Message: **`Cannot parse as date or period: '1836-1842'`**
  - Causing raw value: `1836-1842; Hopedale/Hoffenthal Labrador; ; Missionar (UA, Dienerblätter A-Bl, S. 234) {R0004100} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0060000:
  - Error Message: **`Cannot parse as date or period: '1842-1843'`**
  - Causing raw value: `1842-1843; Europa; ; (UA, Dienerblätter A-Bl, S. 234) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0060000:
  - Error Message: **`Cannot parse as date or period: '1843-1847'`**
  - Causing raw value: `1843-1847; Hopedale/Hoffenthal Labrador; ; Missionar (UA, Dienerblätter A-Bl, S. 234) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0060000:
  - Error Message: **`Cannot parse as date or period: '1847-1851'`**
  - Causing raw value: `1847-1851; Hebron Labrador; ; Missionar (UA, Dienerblätter A-Bl. S. 234) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0060000:
  - Error Message: **`Cannot parse as date or period: '1851-1866'`**
  - Causing raw value: `1851-1866; Okak Labrador; ; Missionar (UA, Dienerblätter A-Bl. S. 234) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0060000:
  - Error Message: **`Cannot parse as date or period: '1866-1893'`**
  - Causing raw value: `1866-1893; Herrnhut; ; Ruhestand (UA, Dienerblätter A-Bl. S. 234)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0060000:
  - Error Message: **`Invalid work id: UA, Dienerblätter A-Bl, S. 234 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, Dienerblätter A-Bl, S. 234`

### P0070000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0070000:
  - Error Message: **`Expected 4 parts, got 1: um 1900 Lehrerseminar Niesky`**
  - Causing raw value: `um 1900 Lehrerseminar Niesky`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0070000:
  - Error Message: **`Invalid work id: Otto Uttendörfer: "Aus dem naturkundlichen Tagebuche des Nieskyer Lehrerseminars. (Botanische Beobachtungen)", in: Aus der Heimat. Eine Naturwissenschaftliche Zeitschrift, Organ des Deutschen Lehrer-Vereins für Naturkunde, 1901, S. 152-158, 157 (should be R-ID, or M-ID)`**
  - Causing raw value: `Otto Uttendörfer: "Aus dem naturkundlichen Tagebuche des Nieskyer Lehrerseminars. (Botanische Beobachtungen)", in: Aus der Heimat. Eine Naturwissenschaftliche Zeitschrift, Organ des Deutschen Lehrer-Vereins für Naturkunde, 1901, S. 152-158, 157`

### P0080000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0080000:
  - Error Message: **`Cannot parse as date or period: '-1908'`**
  - Causing raw value: `-1908; Niesky; Lehrerseminar; Studendt (wikipedia) `
  - Full field: _-1908; Niesky; Lehrerseminar; Studendt (wikipedia) |
1908-1913; Neuwied; Knabenanstalt; Lehrer (wikipedia) |
1913-1914; Niesky; Pädagogium; Lehrer (Wikipedia) |
1914-1944; Gnadenfeld; Ortschule; Direktor (wikipedia) |
1945-1967; Königsfeld; ; Lehrer (wikipedia)_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0080000:
  - Error Message: **`Cannot parse as date or period: '1908-1913'`**
  - Causing raw value: `1908-1913; Neuwied; Knabenanstalt; Lehrer (wikipedia) `
  - Full field: _-1908; Niesky; Lehrerseminar; Studendt (wikipedia) |
1908-1913; Neuwied; Knabenanstalt; Lehrer (wikipedia) |
1913-1914; Niesky; Pädagogium; Lehrer (Wikipedia) |
1914-1944; Gnadenfeld; Ortschule; Direktor (wikipedia) |
1945-1967; Königsfeld; ; Lehrer (wikipedia)_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0080000:
  - Error Message: **`Cannot parse as date or period: '1913-1914'`**
  - Causing raw value: `1913-1914; Niesky; Pädagogium; Lehrer (Wikipedia) `
  - Full field: _-1908; Niesky; Lehrerseminar; Studendt (wikipedia) |
1908-1913; Neuwied; Knabenanstalt; Lehrer (wikipedia) |
1913-1914; Niesky; Pädagogium; Lehrer (Wikipedia) |
1914-1944; Gnadenfeld; Ortschule; Direktor (wikipedia) |
1945-1967; Königsfeld; ; Lehrer (wikipedia)_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0080000:
  - Error Message: **`Cannot parse as date or period: '1914-1944'`**
  - Causing raw value: `1914-1944; Gnadenfeld; Ortschule; Direktor (wikipedia) `
  - Full field: _-1908; Niesky; Lehrerseminar; Studendt (wikipedia) |
1908-1913; Neuwied; Knabenanstalt; Lehrer (wikipedia) |
1913-1914; Niesky; Pädagogium; Lehrer (Wikipedia) |
1914-1944; Gnadenfeld; Ortschule; Direktor (wikipedia) |
1945-1967; Königsfeld; ; Lehrer (wikipedia)_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0080000:
  - Error Message: **`Cannot parse as date or period: '1945-1967'`**
  - Causing raw value: `1945-1967; Königsfeld; ; Lehrer (wikipedia)`
  - Full field: _-1908; Niesky; Lehrerseminar; Studendt (wikipedia) |
1908-1913; Neuwied; Knabenanstalt; Lehrer (wikipedia) |
1913-1914; Niesky; Pädagogium; Lehrer (Wikipedia) |
1914-1944; Gnadenfeld; Ortschule; Direktor (wikipedia) |
1945-1967; Königsfeld; ; Lehrer (wikipedia)_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0080000:
  - Error Message: **`Invalid work id: Walter Bau: Pädagoge, Geologe, Paläontologe und Zoologe, In: Jahreshefte des Vereins für vaterländische Naturkunde in Württemberg 123, S. 18–19, Stuttgart 1968 (mit Abbildung) (should be R-ID, or M-ID)`**
  - Causing raw value: `Walter Bau: Pädagoge, Geologe, Paläontologe und Zoologe, In: Jahreshefte des Vereins für vaterländische Naturkunde in Württemberg 123, S. 18–19, Stuttgart 1968 (mit Abbildung)`

### P0090000

- [ ] Error in Col: **Geburt - Datum** and row with ID P0090000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1825-09-14 (UA, Dienerblätter A-Bl. S. 335)`**
  - Causing raw value: `1825-09-14 (UA, Dienerblätter A-Bl. S. 335)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0090000:
  - Error Message: **`Invalid format for LocationID: L0800000 (UA, Dienerblätter A-Bl, S. 335)`**
  - Causing raw value: `L0800000 (UA, Dienerblätter A-Bl, S. 335)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0090000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1889-08-26 (UA, Dienerblätter A-Bl, S. 335)`**
  - Causing raw value: `1889-08-26 (UA, Dienerblätter A-Bl, S. 335)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0090000:
  - Error Message: **`Invalid Reference Document value: UA, Dienerblätter A-Bl, S. 335 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Queenstown, South Africa|
Gösen, South Africa {UA, Dienerblätter A-Bl, S. 335}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0090000:
  - Error Message: **`Cannot parse as date or period: '?-1855'`**
  - Causing raw value: `?-1855; Capstadt, Südafrika; ; Apotheker (UA, Dienerblätter A-Bl, S. 335) `
  - Full field: _?-1855; Capstadt, Südafrika; ; Apotheker (UA, Dienerblätter A-Bl, S. 335) |
1855-1858; Castadt, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)
1858-?; Silo, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335) | 
? -?; Baziya, Südafrika;  ;  Missionar  (UA, Dienerblätter A-Bl, S. 335) |
1875-?;  Silo, Südafrika;  ; Missionsvorsteher (UA, Dienerblätter A-Bl, S. 335) | _

- [ ] Error in Col: **Wirkungsorte** and row with ID P0090000:
  - Error Message: **`Expected 4 parts, got 7: 1855-1858; Castadt, Südafrika; ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)1858-?; Silo, Südafrika; ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)`**
  - Causing raw value: `1855-1858; Castadt, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)
1858-?; Silo, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335) `
  - Full field: _?-1855; Capstadt, Südafrika; ; Apotheker (UA, Dienerblätter A-Bl, S. 335) |
1855-1858; Castadt, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)
1858-?; Silo, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335) | 
? -?; Baziya, Südafrika;  ;  Missionar  (UA, Dienerblätter A-Bl, S. 335) |
1875-?;  Silo, Südafrika;  ; Missionsvorsteher (UA, Dienerblätter A-Bl, S. 335) | _

- [ ] Error in Col: **Wirkungsorte** and row with ID P0090000:
  - Error Message: **`Cannot parse as date or period: '? -?'`**
  - Causing raw value: ` 
? -?; Baziya, Südafrika;  ;  Missionar  (UA, Dienerblätter A-Bl, S. 335) `
  - Full field: _?-1855; Capstadt, Südafrika; ; Apotheker (UA, Dienerblätter A-Bl, S. 335) |
1855-1858; Castadt, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)
1858-?; Silo, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335) | 
? -?; Baziya, Südafrika;  ;  Missionar  (UA, Dienerblätter A-Bl, S. 335) |
1875-?;  Silo, Südafrika;  ; Missionsvorsteher (UA, Dienerblätter A-Bl, S. 335) | _

- [ ] Error in Col: **Wirkungsorte** and row with ID P0090000:
  - Error Message: **`Cannot parse as date or period: '1875-?'`**
  - Causing raw value: `1875-?;  Silo, Südafrika;  ; Missionsvorsteher (UA, Dienerblätter A-Bl, S. 335) `
  - Full field: _?-1855; Capstadt, Südafrika; ; Apotheker (UA, Dienerblätter A-Bl, S. 335) |
1855-1858; Castadt, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335)
1858-?; Silo, Südafrika;  ; Missionsgehilfe (UA, Dienerblätter A-Bl, S. 335) | 
? -?; Baziya, Südafrika;  ;  Missionar  (UA, Dienerblätter A-Bl, S. 335) |
1875-?;  Silo, Südafrika;  ; Missionsvorsteher (UA, Dienerblätter A-Bl, S. 335) | _

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0090000:
  - Error Message: **`Invalid work id: UA, Dienerblätter A-Bl, S. 335 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, Dienerblätter A-Bl, S. 335`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Datenbanknachweis)** and row with ID P0090000:
  - Error Message: **`CollectionID must start with 'C': https://plants.jstor.org/stable/10.5555/al.ap.person.bm000031005`**
  - Causing raw value: `https://plants.jstor.org/stable/10.5555/al.ap.person.bm000031005`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0090000:
  - Error Message: **`Invalid work id: R0001100 {https://www.s2a3.org.za/bio/Biograph_final.php?serial=179%20 (should be R-ID, or M-ID)`**
  - Causing raw value: ` R0001100 {https://www.s2a3.org.za/bio/Biograph_final.php?serial=179%20`
  - Full field: _M0001100 | M0001200| M0001300 | M0001400 | R0001100 {https://www.s2a3.org.za/bio/Biograph_final.php?serial=179%20|%20R0001100} |
R0008500 |R0008900_

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0090000:
  - Error Message: **`Invalid work id: %20R0001100} (should be R-ID, or M-ID)`**
  - Causing raw value: `%20R0001100} `
  - Full field: _M0001100 | M0001200| M0001300 | M0001400 | R0001100 {https://www.s2a3.org.za/bio/Biograph_final.php?serial=179%20|%20R0001100} |
R0008500 |R0008900_

- [ ] Error in Col: **Wichtige Werke der Person ohne botanischen Kontext** and row with ID P0090000:
  - Error Message: **`Invalid work id: UA, TS Bd.21.82.d.: Karte von Tembuland in Südafrika-Ost kolorierte Federzeichnung 340x470mm (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, TS Bd.21.82.d.: Karte von Tembuland in Südafrika-Ost [1862] kolorierte Federzeichnung 340x470mm`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0090000:
  - Error Message: **`Invalid work id: https://www.s2a3.org.za/bio/Biograph_final.php?serial=179 (should be R-ID, or M-ID)`**
  - Causing raw value: `https://www.s2a3.org.za/bio/Biograph_final.php?serial=179 `
  - Full field: _https://www.s2a3.org.za/bio/Biograph_final.php?serial=179 |
R0008600 |R0008700 |_

### P0100000

- [ ] Error in Col: **Geburt - Datum** and row with ID P0100000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1833-12-18 (wkd)`**
  - Causing raw value: `1833-12-18 (wkd)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0100000:
  - Error Message: **`Invalid format for LocationID: Lititz/USA (wkd)`**
  - Causing raw value: `Lititz/USA (wkd)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0100000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1928-09-19 (wkd)`**
  - Causing raw value: `1928-09-19 (wkd)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0100000:
  - Error Message: **`Invalid format for LocationID: Lititz, USA (wkd)`**
  - Causing raw value: `Lititz, USA (wkd)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0100000:
  - Error Message: **`Expected 4 parts, got 3: ?- 1885; Litiz, USA; teacher`**
  - Causing raw value: `?- 1885; Litiz, USA; teacher {https://de.findagrave.com/memorial/34844087/abraham-reincke-beck}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0100000:
  - Error Message: **`Invalid work id: offen/nein (should be R-ID, or M-ID)`**
  - Causing raw value: `offen/nein`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0100000:
  - Error Message: **`Invalid work id: https://de.findagrave.com/memorial/34844087/abraham-reincke-beck (should be R-ID, or M-ID)`**
  - Causing raw value: `https://de.findagrave.com/memorial/34844087/abraham-reincke-beck`

### P0110000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0110000:
  - Error Message: **`URL is not valid: nein (2024-10-15)`**
  - Causing raw value: `nein (2024-10-15)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0110000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1786-03-22 (UA, Dienerblätter A-Bl, S. 388)`**
  - Causing raw value: `1786-03-22 (UA, Dienerblätter A-Bl, S. 388)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0110000:
  - Error Message: **`Invalid format for LocationID: Lichtenfels/Grönland (UA, Dienerblätter A-Bl, S. 388)`**
  - Causing raw value: `Lichtenfels/Grönland (UA, Dienerblätter A-Bl, S. 388)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0110000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1859-10-04 (UA, Dienerblätter A-Bl, S. 388)`**
  - Causing raw value: `1859-10-04 (UA, Dienerblätter A-Bl, S. 388)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0110000:
  - Error Message: **`LocationID must start with 'L': Herrnhut (UA, Dienerblätter A-Bl, S. 388)`**
  - Causing raw value: `Herrnhut (UA, Dienerblätter A-Bl, S. 388)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '?-?'`**
  - Causing raw value: `?-?; L1500000; Knabenanstalt; Schüler (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '?-1817'`**
  - Causing raw value: `?-1817; L1500000;  ; Gerber (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '1817-1826'`**
  - Causing raw value: `1817-1826; Okak Labrador; ; Missionar (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '1826-1827'`**
  - Causing raw value: `1826-1827; Europa; ;  (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '1827-1831'`**
  - Causing raw value: `1827-1831; Hoffenthal, Labrador;  ; Missionar  (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '1831-1833'`**
  - Causing raw value: `1831-1833; Okak, Labrador; ; Missionar (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Expected 4 parts, got 3: 1833-1840?; Nain, Labrador; Missionar (UA, Dienerblätter A-Bl, S. 388)`**
  - Causing raw value: `1833-1840?; Nain, Labrador; Missionar (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '1840?-1851'`**
  - Causing raw value: `1840?-1851; Hoffenthal, Labrador; ; Missionar (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0110000:
  - Error Message: **`Cannot parse as date or period: '1851-1859'`**
  - Causing raw value: `1851-1859; Herrnhut; ; Ruhestand (UA, Dienerblätter A-Bl, S. 388) `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0110000:
  - Error Message: **`Invalid work id: UA, Dienerblätter A-Bl, S. 388 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, Dienerblätter A-Bl, S. 388`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0110000:
  - Error Message: **`PersonID must start with 'P': August Röntgen`**
  - Causing raw value: ` August Röntgen `
  - Full field: _P0020000 {R0000700} | August Röntgen | Michael Eberle_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0110000:
  - Error Message: **`PersonID must start with 'P': Michael Eberle`**
  - Causing raw value: ` Michael Eberle`
  - Full field: _P0020000 {R0000700} | August Röntgen | Michael Eberle_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0110000:
  - Error Message: **`Invalid work id: Richard Träger: "Ein Herbarium von Pflanzen aus Labrador", in: ders., "Trägermappe" Naturwissenschaft in der Brüdergemeine (Botanik, Ornithologie, Medizin) UA. IV/612, Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Ein Herbarium von Pflanzen aus Labrador", in: ders., "Trägermappe" Naturwissenschaft in der Brüdergemeine (Botanik, Ornithologie, Medizin) UA. IV/612, Herrnhut: Archiv der Herrnhuter Brüdergemeine.`

### P0120000

- [ ] Error in Col: **Geburt - Datum** and row with ID P0120000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1818-08-30 oder 1818-08-18 (UA, Dienerblätter A-Bl, S. 404)`**
  - Causing raw value: `1818-08-30 oder 1818-08-18 (UA, Dienerblätter A-Bl, S. 404)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0120000:
  - Error Message: **`LocationID must start with 'L': Old Sarepta (UA, Dienerblätter A-Bl. S, 404)`**
  - Causing raw value: `Old Sarepta (UA, Dienerblätter A-Bl. S, 404)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0120000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1901-04-03 oder 1901-04-16 (UA, Dienerblätter A-Bl, S. 404)`**
  - Causing raw value: `1901-04-03 oder 1901-04-16 (UA, Dienerblätter A-Bl, S. 404)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0120000:
  - Error Message: **`LocationID must start with 'L': Sarepta (UA, Dienerblätter A-Bl, S. 404)`**
  - Causing raw value: `Sarepta  (UA, Dienerblätter A-Bl, S. 404)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0120000:
  - Error Message: **`Expected 4 parts, got 1: Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0120000:
  - Error Message: **`Invalid work id: nein (should be R-ID, or M-ID)`**
  - Causing raw value: `nein `
  - Full field: _nein | 
UA, Dienerblätter A-Bl, S. 404_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0120000:
  - Error Message: **`Invalid work id: UA, Dienerblätter A-Bl, S. 404 (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
UA, Dienerblätter A-Bl, S. 404`
  - Full field: _nein | 
UA, Dienerblätter A-Bl, S. 404_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0120000:
  - Error Message: **`LiteratureID must start with 'R': 1868-1882: Veröffentlichungentomologischer Art in "Stettiner Entomologischer Zeitung"`**
  - Causing raw value: `1868-1882: 
Veröffentlichung
entomologischer Art in "Stettiner Entomologischer Zeitung" `
  - Full field: _1868-1882: 
Veröffentlichung
entomologischer Art in "Stettiner Entomologischer Zeitung" | Etliche Typen u.a. in: Beitr. Pflanzenk. Russ. Reiches 8: 266-267 (1851) | Bull. Soc. Imp. Naturalistes Moscou 31 (1): 13 (1858) | Bull. Soc. Imp. Naturalistes Moscou 57 (1): 52 (1882). _

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0120000:
  - Error Message: **`LiteratureID must start with 'R': Etliche Typen u.a. in: Beitr. Pflanzenk. Russ. Reiches 8: 266-267 (1851)`**
  - Causing raw value: ` Etliche Typen u.a. in: Beitr. Pflanzenk. Russ. Reiches 8: 266-267 (1851) `
  - Full field: _1868-1882: 
Veröffentlichung
entomologischer Art in "Stettiner Entomologischer Zeitung" | Etliche Typen u.a. in: Beitr. Pflanzenk. Russ. Reiches 8: 266-267 (1851) | Bull. Soc. Imp. Naturalistes Moscou 31 (1): 13 (1858) | Bull. Soc. Imp. Naturalistes Moscou 57 (1): 52 (1882). _

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0120000:
  - Error Message: **`LiteratureID must start with 'R': Bull. Soc. Imp. Naturalistes Moscou 31 (1): 13 (1858)`**
  - Causing raw value: ` Bull. Soc. Imp. Naturalistes Moscou 31 (1): 13 (1858) `
  - Full field: _1868-1882: 
Veröffentlichung
entomologischer Art in "Stettiner Entomologischer Zeitung" | Etliche Typen u.a. in: Beitr. Pflanzenk. Russ. Reiches 8: 266-267 (1851) | Bull. Soc. Imp. Naturalistes Moscou 31 (1): 13 (1858) | Bull. Soc. Imp. Naturalistes Moscou 57 (1): 52 (1882). _

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0120000:
  - Error Message: **`LiteratureID must start with 'R': Bull. Soc. Imp. Naturalistes Moscou 57 (1): 52 (1882).`**
  - Causing raw value: ` Bull. Soc. Imp. Naturalistes Moscou 57 (1): 52 (1882). `
  - Full field: _1868-1882: 
Veröffentlichung
entomologischer Art in "Stettiner Entomologischer Zeitung" | Etliche Typen u.a. in: Beitr. Pflanzenk. Russ. Reiches 8: 266-267 (1851) | Bull. Soc. Imp. Naturalistes Moscou 31 (1): 13 (1858) | Bull. Soc. Imp. Naturalistes Moscou 57 (1): 52 (1882). _

### P0130000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0130000:
  - Error Message: **`URL is not valid: nein (2024-10-23)`**
  - Causing raw value: `nein (2024-10-23)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0130000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1832-11-11 (UA, R.22.159.04)`**
  - Causing raw value: `1832-11-11 (UA, R.22.159.04)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0130000:
  - Error Message: **`Invalid format for LocationID: L1120000 (UA, R.22.159.04)`**
  - Causing raw value: `L1120000 (UA, R.22.159.04)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0130000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1862-08-02 (UA, R.22.159.04)`**
  - Causing raw value: `1862-08-02 (UA, R.22.159.04)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0130000:
  - Error Message: **`Invalid format for LocationID: L1120000 (UA, R.22.159.04)`**
  - Causing raw value: `L1120000 (UA, R.22.159.04)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0130000:
  - Error Message: **`Expected 4 parts, got 1: Herrnhut: Apotheker`**
  - Causing raw value: `Herrnhut: Apotheker `
  - Full field: _Herrnhut: Apotheker |
Penig (Sachsen): Apotheker _

- [ ] Error in Col: **Wirkungsorte** and row with ID P0130000:
  - Error Message: **`Expected 4 parts, got 1: Penig (Sachsen): Apotheker`**
  - Causing raw value: `Penig (Sachsen): Apotheker `
  - Full field: _Herrnhut: Apotheker |
Penig (Sachsen): Apotheker _

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0130000:
  - Error Message: **`Invalid work id: UA, R.22.159.04 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA, R.22.159.04`

### P0140000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0140000:
  - Error Message: **`URL is not valid: nein (2024-10-28)`**
  - Causing raw value: `nein (2024-10-28)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0140000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0140000:
  - Error Message: **`LiteratureID must start with 'R': Flora Niskiensis, HS , , 10 Abteilungen, 78 ungez. S. Oktav, UA NB.VI. 949`**
  - Causing raw value: `Flora Niskiensis, HS , [um 1800], 10 Abteilungen, 78 ungez. S. Oktav, UA NB.VI. 949`

### P0150000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0150000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0150000:
  - Error Message: **`Invalid Reference Document value: R0006800}1836/1842; L2250000; Pädagogium; Schüler {R0006800}1842/1844; L1101000; Seminar; Student {R0006800}1844/1848; L2250000; Knabenanstalt; Lehrer {R0006800}1848/1854; L1570000; Knabenanstalt; Geistlicher, Lehrer {R0006800}1854/1857; L1101000; Seminar; Lehrer {R0006800}1857/1864; L1950000; Knabenanstalt; Geistlicher, Direktor {R0006800}1864/1866; L0150000 ; Genesungsreise; {R0006800}1866/1869; L1500000; Knabenanstalt; Direktor {R0006800}1869/1879; L0400000 ; Unitätsältestenkonferenz; Helfer- und Erziehungsdepartment {R0006800}1879/1880; L0150000 ; Genesungsreise; {R0006800}1880/1883; L1101000; Seminar; Lehrer {R0006800}1883/1894; L0800000 ; ;Ruhestand {R0006800 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `1832/1836; L2250000; Knabenanstalt; Schüler {R0006800}
1836/1842; L2250000; Pädagogium; Schüler {R0006800}
1842/1844; L1101000; Seminar; Student {R0006800}
1844/1848; L2250000; Knabenanstalt; Lehrer {R0006800}
1848/1854; L1570000; Knabenanstalt; Geistlicher, Lehrer {R0006800}
1854/1857; L1101000; Seminar; Lehrer {R0006800}
1857/1864; L1950000; Knabenanstalt; Geistlicher, Direktor {R0006800}
1864/1866; L0150000 [Schweiz, Canstatt, Montreux am Genfer See, Cevennen in Südfrankreich, Marseilles, Cannes, Nizza, Genua, Schweizer Alpen, Gnadenberg, Westphalen, Rheinland, Holland, Belgien, Paris,  Schweiz, Berlin, Gnadenberg] ; Genesungsreise; {R0006800}
1866/1869; L1500000; Knabenanstalt; Direktor {R0006800}
1869/1879; L0400000 [jährliche Urlaube in den Alpen L0150000]; Unitätsältestenkonferenz; Helfer- und Erziehungsdepartment {R0006800}
1879/1880; L0150000 [Thüringer Wald, Osnabrück, Rhein, Mosel, Elsaß, Schweiz, Berner Oberland, Montmirail, Pranagin, Nizza, Italienreise, Alpen Schweiz]; Genesungsreise; {R0006800}
1880/1883; L1101000; Seminar; Lehrer {R0006800}
1883/1894; L0800000 [jährliche Urlaube in den Alpen L0150000]; ;Ruhestand {R0006800} `

### P0160000

- [ ] Error in Col: **Übernahme in Personenlexikon** and row with ID P0160000:
  - Error Message: **`Provided string is not in codelist: Vergleich P1660000`**
  - Causing raw value: `Vergleich P1660000`

- [ ] Error in Col: **Links - Bionomia** and row with ID P0160000:
  - Error Message: **`URL is not valid: nein (2024-10-23)`**
  - Causing raw value: `nein (2024-10-23)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0160000:
  - Error Message: **`Expected 4 parts, got 1: Barby, Niesky, Nordamerika`**
  - Causing raw value: `Barby, Niesky, Nordamerika`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0160000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0165000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0165000:
  - Error Message: **`Expected 4 parts, got 1: Suriname`**
  - Causing raw value: `Suriname`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0165000:
  - Error Message: **`Invalid work id: offen/nein (should be R-ID, or M-ID)`**
  - Causing raw value: `offen/nein`

### P0165500

- [ ] Error in Col: **Übernahme in Personenlexikon** and row with ID P0165500:
  - Error Message: **`Provided string is not in codelist: eventuell`**
  - Causing raw value: `eventuell`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0165500:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0165500:
  - Error Message: **`LocationID must start with 'L': Flensburg`**
  - Causing raw value: `Flensburg {R0015600}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0165500:
  - Error Message: **`Expected 4 parts, got 3: 1792; L2265000; Missionarsehefrau`**
  - Causing raw value: `1792; L2265000; Missionarsehefrau {R0015600}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0165500:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P0165500:
  - Error Message: **`PersonID must start with 'P': Sendung von "berries" aus Suriname an Familie und Bekannte in Christiansfeld, Dänemark`**
  - Causing raw value: `Sendung von "berries" aus Suriname an Familie und Bekannte in Christiansfeld, Dänemark {R0015600}`

### P0170000

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0170000:
  - Error Message: **`PersonID must start with 'P': viele, alle offen`**
  - Causing raw value: `viele, alle offen`
  - Full field: _P1280000 {M0004200}|
viele, alle offen_

### P0180000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0180000:
  - Error Message: **`URL is not valid: nein (2024-10-23)`**
  - Causing raw value: `nein (2024-10-23)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0180000:
  - Error Message: **`LocationID must start with 'L': Weberhof Orellen (Livland)`**
  - Causing raw value: `Weberhof Orellen (Livland)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0180000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1914-12-17 00:00:00`**
  - Causing raw value: `1914-12-17 00:00:00`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0180000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0190000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0190000:
  - Error Message: **`URL is not valid: nein (2024-10-23)`**
  - Causing raw value: `nein (2024-10-23)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0190000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P0190000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0190000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0200000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0200000:
  - Error Message: **`URL is not valid: nein (2024-10-23)`**
  - Causing raw value: `nein (2024-10-23)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0200000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0200000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0200000:
  - Error Message: **`LiteratureID must start with 'R': 1853: Avifauna von Neuwied`**
  - Causing raw value: `1853: Avifauna von 
Neuwied`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0200000:
  - Error Message: **`Invalid work id: Hardtke (should be R-ID, or M-ID)`**
  - Causing raw value: `Hardtke`

### P0210000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0210000:
  - Error Message: **`URL is not valid: nein (2024-10-23)`**
  - Causing raw value: `nein (2024-10-23)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0210000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1738-01-03 (Pringle 1991, 195)`**
  - Causing raw value: `1738-01-03 (Pringle 1991, 195)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0210000:
  - Error Message: **`LocationID must start with 'L': Ripen, Jutland (now Ribe, Denmark},`**
  - Causing raw value: `Ripen, Jutland (now Ribe, Denmark},`

- [ ] Error in Col: **Tod - Ort** and row with ID P0210000:
  - Error Message: **`LocationID must start with 'L': near Okak, Schiffbruch`**
  - Causing raw value: `near Okak, Schiffbruch`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0210000:
  - Error Message: **`Expected 4 parts, got 2: / ; Labrador -- Missionar`**
  - Causing raw value: `/ ; Labrador --  Missionar`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0210000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0210000:
  - Error Message: **`Invalid work id: R0006000 (?) (should be R-ID, or M-ID)`**
  - Causing raw value: ` R0006000 (?) `
  - Full field: _R0005800 | R0006000 (?) | R0011100_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0210000:
  - Error Message: **`Invalid work id: Gaston R. Demarée; Astrid E. J. Ogilvie: "Early Meteorological Observations in Greenland: The Contributions of David Cranz, Christian Gottlieb Kratzenstein and Christopher Brasen", in: Felicity Jensz; Christina Petterson (Hg.), Legacies of David Cranz's 'Historie von Grönland' (1765), London: Palgrave Macmillan 2021, S. 141-164, 144-145. (should be R-ID, or M-ID)`**
  - Causing raw value: `Gaston R. Demarée; Astrid E. J. Ogilvie: "Early Meteorological Observations in Greenland: The Contributions of David Cranz, Christian Gottlieb Kratzenstein and Christopher Brasen", in: Felicity Jensz; Christina Petterson (Hg.), Legacies of David Cranz's 'Historie von Grönland' (1765), London: Palgrave Macmillan 2021, S. 141-164, 144-145. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0210000:
  - Error Message: **`Invalid work id: Christian Gottlieb Kratzenstein: "Vaer Observationer for Aarene 1767. og 1768. anstillede i Grønland. Brägte i Orden og bekiendtgiorte af C.G. Kratzenstein.” “Skrifter som udi det Kiøbenhavnske Selskab af Laerdoms og Videnskabers Elskere ere fremlagte og oplaeste i Aarene 1765. 1766. 1767. 1768. og 1769.” (Tiende Deel, 1770): 373–92.", in: , 1770. (should be R-ID, or M-ID)`**
  - Causing raw value: `Christian Gottlieb Kratzenstein: "Vaer Observationer for Aarene 1767. og 1768. anstillede i Grønland. Brägte i Orden og bekiendtgiorte af C.G. Kratzenstein.” “Skrifter som udi det Kiøbenhavnske Selskab af Laerdoms og Videnskabers Elskere ere fremlagte og oplaeste i Aarene 1765. 1766. 1767. 1768. og 1769.” (Tiende Deel, 1770): 373–92.", in: , 1770. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0210000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. < (should be R-ID, or M-ID)`**
  - Causing raw value: `James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. <`

### P0215000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0215000:
  - Error Message: **`Expected 4 parts, got 2: / ; Surinam -- Missionar`**
  - Causing raw value: `/ ; Surinam -- Missionar `

### P0220000

- [ ] Error in Col: **Angehörige - Anmerkungen** and row with ID P0220000:
  - Error Message: **`Invalid Reference Document value: R0002550}; weitere Geschwister: Maria Magdalena Breutel (*1783-11-02 ; †1785-11-10 ); Johanna Catharina Breutel (*1785-09-08; †1785-11-10) {https://homepage.ruhr-uni-bochum.de/raphael.dammer/pafg443.htm#41082 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Verlobung mit Anna Sophia Röderer am 31.08.1824; Hochzeit am 16.09.1824  {R0002550}; weitere Geschwister: Maria Magdalena Breutel (*1783-11-02 ; †1785-11-10 ); Johanna Catharina Breutel (*1785-09-08; †1785-11-10) [Sterbedaten überprüfen, da gleich] {https://homepage.ruhr-uni-bochum.de/raphael.dammer/pafg443.htm#41082}`

- [ ] Error in Col: **Tod - Ort** and row with ID P0220000:
  - Error Message: **`Invalid format for LocationID: L0400000 {https://saebi.isgv.de/biografie/Johann_Christian_Breutel_(1788-1875})`**
  - Causing raw value: `L0400000 {https://saebi.isgv.de/biografie/Johann_Christian_Breutel_(1788-1875})`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0220000:
  - Error Message: **`Expected 4 parts, got 2: /;`**
  - Causing raw value: `/; [Herrnhut]`
  - Full field: _1840/1841; [Karibik (westindische Inseln: St. Thomas, St. Croix)]; ; Visitation |
1853/1854; [Südafrika] ; ; Visitation |
/; [Herrnhut]_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0220000:
  - Error Message: **`Invalid Reference Document value: R00072000 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: ` P0865000 [Kaspar Kögel] {R00072000} `
  - Full field: _P0227000 [J. G. Brey] {M0047000} | P0865000 [Kaspar Kögel] {R00072000} | P0290000 [Johann Gottfried Cunow] {M0048000}_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Datenbanknachweis)** and row with ID P0220000:
  - Error Message: **`CollectionID must start with 'C': herb:S-PA`**
  - Causing raw value: ` herb:S-PA {http://purl.oclc.org/net/edu.harvard.huh/guid/uuid/a219bc47-118f-4b20-91ba-7aa2af9e6e23} `

### P0222000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0222000:
  - Error Message: **`Expected 4 parts, got 2: 1860%/1869%;`**
  - Causing raw value: `1860%/1869%; `

### P0224000

- [ ] Error in Col: **Tod - Datum** and row with ID P0224000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1896-xx-xx`**
  - Causing raw value: `1896-xx-xx {https://homepage.ruhr-uni-bochum.de/raphael.dammer/pafg443.htm}`

### P0230000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0230000:
  - Error Message: **`URL is not valid: nein (2024-10-26)`**
  - Causing raw value: `nein (2024-10-26)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0230000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1764-02-25 (wkd)`**
  - Causing raw value: `1764-02-25 (wkd)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0230000:
  - Error Message: **`LocationID must start with 'L': Stockholm`**
  - Causing raw value: `Stockholm`

- [ ] Error in Col: **Tod - Ort** and row with ID P0230000:
  - Error Message: **`LocationID must start with 'L': Stockholm`**
  - Causing raw value: `Stockholm`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0230000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0230000:
  - Error Message: **`ManuscriptID must start with 'M': 1782: Flora Niskyensis; Das Manuskript wird oft erwähnt, ist aber nicht identifiziert. Wo sich das Manuskript eventuell befindet, ob im UA und ob und wo Objekte sind, ist offen.`**
  - Causing raw value: `1782: Flora Niskyensis; Das Manuskript wird oft erwähnt, ist aber nicht identifiziert. Wo sich das Manuskript eventuell befindet, ob im UA und ob und wo Objekte sind, ist offen.`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0230000:
  - Error Message: **`ManuscriptID must start with 'M': "Diese Brinkmansche Flora ist in den handschriftlichen Florä der Bibliothek des Pädagogiums häufig zitiert. Diese botanischen Studien gingen über dilettantische Liebhaberei weit hinaus und haben reiche Früchte" (S. 94, E. R. Meyer: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905.)`**
  - Causing raw value: `"Diese Brinkmansche Flora ist in den handschriftlichen Florä der Bibliothek des Pädagogiums häufig zitiert. Diese botanischen Studien gingen über dilettantische Liebhaberei weit hinaus und haben reiche Früchte" (S. 94, E. R. Meyer: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905.)`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0230000:
  - Error Message: **`ManuscriptID must start with 'M': Brinkmann wird erwähnt als botanischer Sammler in: Johann Baptist von Albertini: Flora Niskiensis. Columna sinistra. Flora Lusatiae Superioris, eiusque confinium Silesium, Bohemiae, Saxoniae, Lusatiae inferioris, regionum. Columnua dextra. Ordine alphabetico. 1798 et ultra, Herrnhut UA CIM II. 19, Nr. 816`**
  - Causing raw value: `Brinkmann wird erwähnt als botanischer Sammler in: Johann Baptist von Albertini: Flora Niskiensis. Columna sinistra. Flora Lusatiae Superioris, eiusque confinium Silesium, Bohemiae, Saxoniae, Lusatiae inferioris, regionum. Columnua dextra. Ordine alphabetico. 1798 et ultra, Herrnhut UA CIM II. 19, Nr. 816`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0230000:
  - Error Message: **`LiteratureID must start with 'R': Selmar : Gedichte von Selmar. Erster Band, Leipzig: in der Gräffschen Buchhandlung 1789.`**
  - Causing raw value: `Selmar [Carl Gustav von Brinkmann]: Gedichte von Selmar. Erster Band, Leipzig: in der Gräffschen Buchhandlung 1789.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: in Literatur Erwähnung eines botanischen Manuskripts von Brinkmann, einer Flora Niskyensis, 1782: (should be R-ID, or M-ID)`**
  - Causing raw value: `in Literatur Erwähnung eines botanischen Manuskripts von Brinkmann, einer Flora Niskyensis, 1782:`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Leske, Nathanael Gottfried: Reise durch Sachsen : in Rüksicht der Naturgeschichte und Oekonomie / unternommen und beschrieben von Nathanael Gottfried Leske, Leipzig: J. G. Müller 1785, S. 182-184. Das ist die erste Erwähnung dieses Manuskripts und Leske erhielt eine Kopie von Brinkmann. Leske beschreibt zugleich die Sammlung des Gemeinarztes Dr. Türstig aus Niesky, in der er die im Manuskript beschriebenen Arten als Herbabelege sah und nennt einige Arten. Leskes Herbarium und botanische Quellen gingen nach Dublin. E. Charles Nelson: "A CONTRIBUTION TOWARDS A CATALOGUE OF COLLECTORS IN THE FOREIGN PHANEROGAM SECTION OF THE HERBARIUM, NATIONAL BOTANIC GARDENS, GLASNEVIN (DBN).", in: Glasra 4 (1980), S. 31-68. In Dublin ist bisher nicht davon identifiziert wurden. (mehrere Anfragen von Ruhland 11. 2024) Antwort von Colin Kelleher (colin.kelleher@opw.ie) BSc MSc PhD National Botanic Gardensrech vor Ort, 14.08.2025: " I have checked our catalogue and databases and there is no mention of Leske or von Brinkmann or Flora Nisyensis. Although the herbarium was founded by the acquisition of botanical specimens in the Leskean cabinet (purchased in 1792), no specimens from this cabinet have been identified in our collection. We are steadily progressing the digitisation of the entire herbarium, but this will take many years. If we find anything in the process I will contact you again." wenn überhaupt, dann Recherche vor Ort nötig. (should be R-ID, or M-ID)`**
  - Causing raw value: `Leske, Nathanael Gottfried: Reise durch Sachsen : in Rüksicht der Naturgeschichte und Oekonomie / unternommen und beschrieben von Nathanael Gottfried Leske, Leipzig: J. G. Müller 1785, S. 182-184. Das ist die erste Erwähnung dieses Manuskripts und Leske erhielt  eine Kopie von Brinkmann. Leske beschreibt zugleich die Sammlung des Gemeinarztes Dr. Türstig aus Niesky, in der er die im Manuskript beschriebenen Arten als Herbabelege sah und nennt einige Arten. Leskes Herbarium und botanische Quellen gingen nach Dublin. E. Charles Nelson: "A CONTRIBUTION TOWARDS A CATALOGUE OF COLLECTORS IN THE FOREIGN PHANEROGAM SECTION OF THE HERBARIUM, NATIONAL BOTANIC GARDENS, GLASNEVIN (DBN).", in: Glasra 4 (1980), S. 31-68. In Dublin ist bisher nicht davon  identifiziert wurden. (mehrere Anfragen von Ruhland 11. 2024) Antwort von Colin Kelleher (colin.kelleher@opw.ie) BSc MSc PhD National Botanic Gardensrech vor Ort, 14.08.2025: " I have checked our catalogue and databases and there is no mention of Leske or von Brinkmann or Flora Nisyensis. Although the herbarium was founded by the acquisition of botanical specimens in the Leskean cabinet (purchased in 1792), no specimens from this cabinet have been identified in our collection. We are steadily progressing the digitisation of the entire herbarium, but this will take many years. If we find anything in the process I will contact you again." wenn überhaupt, dann Recherche vor Ort nötig.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Meyer, E. R.: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905, 194 (should be R-ID, or M-ID)`**
  - Causing raw value: `Meyer, E. R.: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905, 194`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Philipp, Guntram: "Herrnhuter Apotheker. Pioniere homöopathischer Arzneimittelherstellung", in: Medizin, Gesellschaft und Geschichte Jahrbuch des Instituts für Geschichte der Medizin der Robert Bosch Stiftung 22 (2004), S. 89-147, 128 (should be R-ID, or M-ID)`**
  - Causing raw value: `Philipp, Guntram: "Herrnhuter Apotheker. Pioniere homöopathischer Arzneimittelherstellung", in: Medizin, Gesellschaft und Geschichte Jahrbuch des Instituts für Geschichte der Medizin der Robert Bosch Stiftung  22 (2004), S. 89-147, 128`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Brinkmanns Bibliothek und Sammlungen vermachte er der Universität Uppsala (Ernst Rudolf Meyer: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905, 286) (should be R-ID, or M-ID)`**
  - Causing raw value: `Brinkmanns Bibliothek und Sammlungen vermachte er der Universität Uppsala (Ernst Rudolf Meyer: Schleiermachers und C.G. von Brinkmanns Gang durch die Brüdergemeine, Leipzig: Jansa 1905, 286)`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Marianne Doerfel: "John Hartley, a British Headmaster of a German Public School", in: British Journal for Eighteenth-Century Studies 12 (1989), Nr. 2, S. 145-164, 150 (should be R-ID, or M-ID)`**
  - Causing raw value: `Marianne Doerfel: "John Hartley, a British Headmaster of a German Public School", in: British Journal for Eighteenth-Century Studies 12 (1989), Nr. 2, S. 145-164, 150`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Hardke et al., 37 (should be R-ID, or M-ID)`**
  - Causing raw value: `Hardke et al., 37`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Hannah Lotte Lund: Der Berliner „jüdische Salon“ um 1800. Emanzipation in der Debatte, De Gruyter 2012, passim (should be R-ID, or M-ID)`**
  - Causing raw value: `Hannah Lotte Lund: Der Berliner „jüdische Salon“ um 1800. Emanzipation in der Debatte, De Gruyter  2012, passim`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Guntram Philipp: "Herrnhuter Apotheker. Pioniere homöopathischer Arzneimittelherstellung", in: Medizin, Gesellschaft und Geschichte. Jahrbuch des Instituts für Geschichte der Medizin der Robert Bosch Stiftung 22 (2003), S. 89-147, 128 (should be R-ID, or M-ID)`**
  - Causing raw value: `Guntram Philipp: "Herrnhuter Apotheker. Pioniere homöopathischer Arzneimittelherstellung", in: Medizin, Gesellschaft und Geschichte. Jahrbuch des Instituts für Geschichte der Medizin der Robert Bosch Stiftung  22 (2003), S. 89-147, 128`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0230000:
  - Error Message: **`Invalid work id: Darwin H. Stapleton, Carter, Edward C.: "'I Have the Itch of Botany, of Chemistry, of Mathematica... Strong upon Me': The Science of Benjamin Henry Latrobe", in: Proceedings of the American Philosophical Society 128 (1984), Nr. 3, S. 173-192, 174 (should be R-ID, or M-ID)`**
  - Causing raw value: `Darwin H. Stapleton, Carter, Edward C.: "'I Have the Itch of Botany, of Chemistry, of Mathematica... Strong upon Me': The Science of Benjamin Henry Latrobe", in: Proceedings of the American Philosophical Society 128 (1984), Nr. 3, S. 173-192, 174`

### P0240000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0240000:
  - Error Message: **`URL is not valid: nein (2024-10-26)`**
  - Causing raw value: `nein (2024-10-26)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0240000:
  - Error Message: **`Expected 4 parts, got 1: Tranquebar Südindien`**
  - Causing raw value: `Tranquebar Südindien`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0240000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0250000

- [ ] Error in Col: **Tod - Ort** and row with ID P0250000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0250000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0250000:
  - Error Message: **`LiteratureID must start with 'R': 1827: einführende Arbeitim ersten Heft derAbhandlungen derGörlitzer NaturforschendenGesellschaft und weitere Artikel https://www.senckenberg.de/de/wissenschaft/publikationen/diverses/abhandlungen-der-naturforschenden-gesellschaft-zu-goerlitz/`**
  - Causing raw value: `1827: einführende Arbeit
im ersten Heft der
Abhandlungen der
Görlitzer Naturforschenden
Gesellschaft und weitere Artikel https://www.senckenberg.de/de/wissenschaft/publikationen/diverses/abhandlungen-der-naturforschenden-gesellschaft-zu-goerlitz/ `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0250000:
  - Error Message: **`LiteratureID must start with 'R': Prodromus florae Lusatiae. In: Abhandlungen der Naturf. Gesellschaft Görlitz I. Band. 1827, 1. Heft, S. 41—83. 2. Heft, S. 61—82. II. Band. 1836, 1. Heft, S. 1—38., ?`**
  - Causing raw value: ` 
Prodromus florae Lusatiae. In: Abhandlungen der Naturf. Gesellschaft Görlitz I. Band.  
1827, 1. Heft, S. 41—83. 2. Heft, S. 61—82. II. Band. 1836, 1. Heft, S. 1—38., ? `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0250000:
  - Error Message: **`Invalid work id: Vgl. Barber: Flora der Oberlausitz (1898) (should be R-ID, or M-ID)`**
  - Causing raw value: `Vgl. Barber: Flora der Oberlausitz (1898) `
  - Full field: _Vgl. Barber: Flora der Oberlausitz (1898) | 
"Biographisches Denkmal. Christian Friuedrich Burkhard, Apotheker in Nisky in der Oberlausitz", in: Archiv der Pharmazie 129 (1854), Nr. 3, S. 345-349.| 
Erwähnt in Raberhorst Flora Lusatia, Leipzig 1839 als Zuträger S. VII_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0250000:
  - Error Message: **`Invalid work id: "Biographisches Denkmal. Christian Friuedrich Burkhard, Apotheker in Nisky in der Oberlausitz", in: Archiv der Pharmazie 129 (1854), Nr. 3, S. 345-349. (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
"Biographisches Denkmal. Christian Friuedrich Burkhard, Apotheker in Nisky in der Oberlausitz", in: Archiv der Pharmazie 129 (1854), Nr. 3, S. 345-349.`
  - Full field: _Vgl. Barber: Flora der Oberlausitz (1898) | 
"Biographisches Denkmal. Christian Friuedrich Burkhard, Apotheker in Nisky in der Oberlausitz", in: Archiv der Pharmazie 129 (1854), Nr. 3, S. 345-349.| 
Erwähnt in Raberhorst Flora Lusatia, Leipzig 1839 als Zuträger S. VII_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0250000:
  - Error Message: **`Invalid work id: Erwähnt in Raberhorst Flora Lusatia, Leipzig 1839 als Zuträger S. VII (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Erwähnt in Raberhorst Flora Lusatia, Leipzig 1839 als Zuträger S. VII`
  - Full field: _Vgl. Barber: Flora der Oberlausitz (1898) | 
"Biographisches Denkmal. Christian Friuedrich Burkhard, Apotheker in Nisky in der Oberlausitz", in: Archiv der Pharmazie 129 (1854), Nr. 3, S. 345-349.| 
Erwähnt in Raberhorst Flora Lusatia, Leipzig 1839 als Zuträger S. VII_

### P0260000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0260000:
  - Error Message: **`Expected 4 parts, got 1: L2280000`**
  - Causing raw value: `L2280000 {R0011300}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0260000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0260000:
  - Error Message: **`Invalid work id: Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" , Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" [UA. IV/612], Herrnhut: Archiv der Herrnhuter Brüdergemeine.`

### P0270000

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0270000:
  - Error Message: **`LiteratureID must start with 'R': 1757: Reisebeschreibung von Graubünden`**
  - Causing raw value: `1757: Reisebeschreibung von Graubünden `
  - Full field: _1757: Reisebeschreibung von Graubünden |
R0013700_

### P0280000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0280000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0280000:
  - Error Message: **`LocationID must start with 'L': Zeist`**
  - Causing raw value: `Zeist`

- [ ] Error in Col: **Tod - Ort** and row with ID P0280000:
  - Error Message: **`Invalid format for LocationID: Leipzig`**
  - Causing raw value: `Leipzig`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0280000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0290000

- [ ] Error in Col: **Tod - Ort** and row with ID P0290000:
  - Error Message: **`LocationID must start with 'L': Berthelsdorf`**
  - Causing raw value: `Berthelsdorf {R0013900}`

### P0300000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0300000:
  - Error Message: **`LocationID must start with 'L': Surinam`**
  - Causing raw value: `1835; Surinam; ; Visitation {R0009400}`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0300000:
  - Error Message: **`ManuscriptID must start with 'M': 1796: "Stammbucheintrag, Niesky, 12. Juni 1796", in: Lind (Hg.), Herrnhuter Stammbuch des Bruders Lind aus der Brüdergemeine Sarepta im Unterwolgagebiet`**
  - Causing raw value: `1796: "Stammbucheintrag, Niesky, 12. Juni 1796", in: Lind (Hg.), Herrnhuter Stammbuch des Bruders Lind aus der Brüdergemeine Sarepta im Unterwolgagebiet `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0300000:
  - Error Message: **`ManuscriptID must start with 'M': 1797: „Niesky'sche Flora im Umkreis von 3 Stunden", „gelangte später in den Besitz der Oberlausitzischen Gesellschaft der Wissenschaften in Görlitz (BARBER 1898), wo sie sich noch heute befindet. Ob es sich bei dem von STOLZ (1916) erwähnten, ebenfalls 1797 verfassten Manuskript „Pierre Frederic Curie, Nieskysche Flora, gesammelt in einem Umkreis von ungefähr drei Stunden. Bibliothek des Pädagogiums zu Niesky." um dasselbe Original oder um eine Kopie des Manuskriptes handelt, konnte bisher nicht geklärt werden.“ (H.-W. Otto; Peter Friedrich Cürie: " Peter Friedrich Curies "Flora Kleinwelkensis" - die zweitälteste Lokalflora der Oberlausitz. Veröffentlichung einer Handschrift aus den Jahren 1803/04", in: Abhandlungen und Berichte des Naturkundemuseums Görlitz 63 (1803/1990), Nr. 10, S. 1-64., S. 3`**
  - Causing raw value: `1797: „Niesky'sche Flora im Umkreis von 3 Stunden", „gelangte später in den Besitz der Oberlausitzischen Gesellschaft der Wissenschaften in Görlitz (BARBER 1898), wo sie sich noch heute befindet. Ob es sich bei dem von STOLZ (1916) erwähnten, ebenfalls 1797 verfassten Manuskript „Pierre Frederic Curie, Nieskysche Flora, gesammelt in einem Umkreis von ungefähr drei Stunden. Bibliothek des Pädagogiums zu Niesky." um dasselbe Original oder um eine Kopie des Manuskriptes handelt, konnte bisher nicht geklärt werden.“ (H.-W. Otto; Peter Friedrich Cürie: "[Flora Kleinwelkensis] Peter Friedrich Curies "Flora Kleinwelkensis" - die zweitälteste Lokalflora der Oberlausitz. Veröffentlichung einer Handschrift aus den Jahren 1803/04", in: Abhandlungen und Berichte des Naturkundemuseums Görlitz 63 (1803/1990), Nr. 10, S. 1-64., S. 3 `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0300000:
  - Error Message: **`Invalid format for ManuscriptID: M0035000 : Flora Kleinwelkiensis. , 98 Blätter, Latein, Stadtmuseum Bautzen: MB 3684 {http://digital.slub-dresden.de/id181011232X}, Ediert teilweise in: Hans-Werner Otto " Peter Friedrich Curies "Flora Kleinwelkensis" - die zweitälteste Lokalflora der Oberlausitz. Veröffentlichung einer Handschrift aus den Jahren 1803/04", in: Abhandlungen und Berichte des Naturkundemuseums Görlitz 63 (1803/04 1990), Nr. 10, S. 1-64`**
  - Causing raw value: `M0035000 [1803/1804]: Flora Kleinwelkiensis. [Kleinwelka], 98 Blätter, Latein, Stadtmuseum Bautzen:  MB 3684 {http://digital.slub-dresden.de/id181011232X}, Ediert teilweise in: Hans-Werner Otto "[Flora Kleinwelkensis] Peter Friedrich Curies "Flora Kleinwelkensis" - die zweitälteste Lokalflora der Oberlausitz. Veröffentlichung einer Handschrift aus den Jahren 1803/04", in: Abhandlungen und Berichte des Naturkundemuseums Görlitz 63 (1803/04 1990), Nr. 10, S. 1-64`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0300000:
  - Error Message: **`ManuscriptID must start with 'M': : Flora von Montmirail, nicht identifiziert, Bezug von Albertini darauf in seinen UA. Cim.I.16.3; identisch oder im Zusammenhang mit: Cim.V.14, Nr. 4 „Pflanzen“: a) „Supplementum Florae Montmiralensis lectum annis 1814-1816`**
  - Causing raw value: ` 
[vor 1814] : Flora von Montmirail, nicht identifiziert, Bezug von Albertini darauf in seinen UA. Cim.I.16.3; identisch oder im Zusammenhang mit: Cim.V.14, Nr. 4 „Pflanzen“: a) „Supplementum Florae Montmiralensis lectum annis 1814-1816 `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0300000:
  - Error Message: **`ManuscriptID must start with 'M': 1825: Analyse der norddeutschen Gräser, Manuskript, verschollen ehemals im Bestand. B. d. Päd. (Stolz 1916, 112)`**
  - Causing raw value: `1825: Analyse der norddeutschen Gräser, Manuskript, verschollen ehemals im Bestand. B. d. Päd. (Stolz 1916, 112) `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0300000:
  - Error Message: **`ManuscriptID must start with 'M': : Herbarverzeichnis von Curies Herbarium, 170 S., Fundortangaben von Grönland bis Südafrika, im Dez. 1947 aus dem Nieskyer Museum nach Herrnhut gebracht, (UA, Cim.II.6), zumindest die Mossbelege befindne sich heute in Dresden, versehen mit Stempel: "„ex Herbarium Herrnhuter Brüdergemeine“`**
  - Causing raw value: `[zw. 1830 – ca. 1860]: Herbarverzeichnis von Curies Herbarium, 170 S., Fundortangaben von Grönland bis Südafrika, im Dez. 1947 aus dem Nieskyer Museum nach Herrnhut gebracht, (UA, Cim.II.6), zumindest die Mossbelege befindne sich heute in Dresden, versehen mit Stempel: "„ex Herbarium Herrnhuter Brüdergemeine“ `

### P0310000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0310000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0310000:
  - Error Message: **`PersonID must start with 'P': Schweinitz`**
  - Causing raw value: `Schweinitz`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0310000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014`

### P0320000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0320000:
  - Error Message: **`Expected 4 parts, got 1: {M0007000}`**
  - Causing raw value: ` {M0007000} `
  - Full field: _ {M0007000} | _

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Literaturnachweis)** and row with ID P0320000:
  - Error Message: **`CollectionID must start with 'C': https://nansh.org/portal/collections/misc/collprofiles.php?collid=287`**
  - Causing raw value: `https://nansh.org/portal/collections/misc/collprofiles.php?collid=287`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0320000:
  - Error Message: **`LiteratureID must start with 'R': "Kramsch produced for the Pennsylvania area a ‘‘Flora Nazarethiana’’ dated 1787–1788, to which Denke added a supplement dated 1797–1799 (Pennell 1931; Phillips and Phillips 1963). These manuscript items are also at the Academy of Natural Sciences." Troyer 2009, 4`**
  - Causing raw value: `"Kramsch produced for the Pennsylvania area a ‘‘Flora Nazarethiana’’ dated 1787–1788, to which Denke added a supplement dated 1797–1799 (Pennell 1931; Phillips and Phillips 1963). These manuscript items are also at the Academy of Natural Sciences." Troyer 2009, 4`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0320000:
  - Error Message: **`LiteratureID must start with 'R': "Samuel Kramsch appears to have been the pioneer, and there has survived his manuscript "Flora Nazarethena spontanea collecta in annis 1787 et 1788", to which Christian Denke added a supplement in 1797." (Francis W. Pennell: "Botanical Collectors of the Philadelphia Local Area ", in: Bartonia 21 (1940-1941), S. 38-57, 40)`**
  - Causing raw value: `"Samuel Kramsch appears to have been the pioneer, and there has survived his manuscript "Flora Nazarethena spontanea collecta in annis 1787 et 1788", to which Christian Denke added a supplement in 1797." (Francis W. Pennell: "Botanical Collectors of the Philadelphia Local Area ", in: Bartonia 21 (1940-1941), S. 38-57, 40)`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0320000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 (Zugl.: Bamberg, Univ., Diss., 2012). (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 (Zugl.: Bamberg, Univ., Diss., 2012).`

### P0330000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0330000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Geburt - Ort** and row with ID P0330000:
  - Error Message: **`LocationID must start with 'L': Gnadenfeld`**
  - Causing raw value: `Gnadenfeld`

- [ ] Error in Col: **Tod - Ort** and row with ID P0330000:
  - Error Message: **`LocationID must start with 'L': Herrnhut,`**
  - Causing raw value: `Herrnhut, `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0330000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0330000:
  - Error Message: **`LiteratureID must start with 'R': Veröffentlichungen über Vögelder Oberlausitz`**
  - Causing raw value: `Veröffentlichungen über Vögel
der Oberlausitz`

### P0340000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0340000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0340000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0340000:
  - Error Message: **`Invalid work id: Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" , Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" [UA. IV/612], Herrnhut: Archiv der Herrnhuter Brüdergemeine.`

### P0350000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0350000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0350000:
  - Error Message: **`LocationID must start with 'L': Grönland`**
  - Causing raw value: `1804/1839; Grönland; ; Missionar`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0350000:
  - Error Message: **`Invalid work id: Richard Träger: "Ein Herbarium von Pflanzen aus Labrador", in: ders., "Trägermappe" Naturwissenschaft in der Brüdergemeine (Botanik, Ornithologie, Medizin) UA. IV/612, Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Ein Herbarium von Pflanzen aus Labrador", in: ders., "Trägermappe" Naturwissenschaft in der Brüdergemeine (Botanik, Ornithologie, Medizin) UA. IV/612, Herrnhut: Archiv der Herrnhuter Brüdergemeine.`

### P0355000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0355000:
  - Error Message: **`Invalid format for LocationID: Labrador`**
  - Causing raw value: `/; Labrador; ; Missionar `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0355000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0355500

- [ ] Error in Col: **Angehörige - Ehepartner** and row with ID P0355500:
  - Error Message: **`Invalid format for PersonID: P168400`**
  - Causing raw value: `P168400`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0355500:
  - Error Message: **`Invalid format for LocationID: Labrador`**
  - Causing raw value: `/; Labrador; ; Missionar {R0003600}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0355500:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0360000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0360000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Geburt - Ort** and row with ID P0360000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P0360000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0360000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0370000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0370000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0370000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0370000:
  - Error Message: **`LocationID must start with 'L': Königsberg`**
  - Causing raw value: `Königsberg`

- [ ] Error in Col: **Tod - Ort** and row with ID P0370000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0370000:
  - Error Message: **`Invalid Reference Document value: Klaus Künzel: "Theodor Erxlebens Moskaureise 1868. Zu Besuch im Sareptanischen Haus mit Aufenthalt in St. Petersburg", in: Unitas Fratrum 80 (2021), S. 101-153 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Niesky, Gnadenfeld, Niesky, Sarepta, Niesky, Herrnhut {Klaus Künzel: "Theodor Erxlebens Moskaureise 1868. Zu Besuch im Sareptanischen Haus mit Aufenthalt in St. Petersburg", in: Unitas Fratrum 80 (2021), S. 101-153}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0370000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0370000:
  - Error Message: **`LiteratureID must start with 'R': 1871: Niesky und Umgebung. Manuskript (ThS/A 132c)`**
  - Causing raw value: `1871: Niesky und Umgebung. Manuskript (ThS/A 132c) `
  - Full field: _1871: Niesky und Umgebung. Manuskript (ThS/A 132c) | 
Theodor von Erxleben: Kurzer Führer durch das ethnographisch-, natur- und kulturhistorische Museum zu Herrnhut, Herrnhut: Winter 3. Aufl.  1904._

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0370000:
  - Error Message: **`LiteratureID must start with 'R': Theodor von Erxleben: Kurzer Führer durch das ethnographisch-, natur- und kulturhistorische Museum zu Herrnhut, Herrnhut: Winter 3. Aufl. 1904.`**
  - Causing raw value: ` 
Theodor von Erxleben: Kurzer Führer durch das ethnographisch-, natur- und kulturhistorische Museum zu Herrnhut, Herrnhut: Winter 3. Aufl.  1904.`
  - Full field: _1871: Niesky und Umgebung. Manuskript (ThS/A 132c) | 
Theodor von Erxleben: Kurzer Führer durch das ethnographisch-, natur- und kulturhistorische Museum zu Herrnhut, Herrnhut: Winter 3. Aufl.  1904._

### P0380000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0380000:
  - Error Message: **`LocationID must start with 'L': Neu Herrnhut/ Nuuk (Grönland)`**
  - Causing raw value: `Neu Herrnhut/ Nuuk (Grönland)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0380000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1934-?-?`**
  - Causing raw value: `1934-?-?`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0380000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature`**
  - Causing raw value: ` Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: O`**
  - Causing raw value: ` 
herb: O `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: CMN`**
  - Causing raw value: ` herb: CMN  `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: NHMD`**
  - Causing raw value: `herb: NHMD `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: MU`**
  - Causing raw value: ` herb: MU `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: GH`**
  - Causing raw value: ` herb: GH `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: US`**
  - Causing raw value: ` herb: US `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: Uniwersytet Jagielloński`**
  - Causing raw value: ` herb: Uniwersytet Jagielloński `
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0380000:
  - Error Message: **`CollectionID must start with 'C': herb: WS {}"`**
  - Causing raw value: ` herb: WS {}"`
  - Full field: _C-DR {https://dr.jacq.org/DR055822} | C-C {https://www.gbif.org/occurrence/466631991} | C-US {http://n2t.net/ark:/65665/301eaec44-23cc-4b4e-87f8-760b3b204db4} | Greenland herbarium Copenhagen, Smithonian, Field Museum, NeyYork Botanical Garden, Canadian Museum of Nature | 
herb: O | herb: CMN  |herb: NHMD | herb: MU | herb: GH | herb: US | herb: Uniwersytet Jagielloński | herb: WS {}"_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0380000:
  - Error Message: **`Invalid work id: Martha Fleming: Johan Eugenius (1870-1934)Tafelausstellung, 2024. (should be R-ID, or M-ID)`**
  - Causing raw value: `Martha Fleming: Johan Eugenius (1870-1934)
Tafelausstellung,  2024.`

### P0385000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0385000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0386000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0386000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0390000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0390000:
  - Error Message: **`Expected 4 parts, got 1: L1500000`**
  - Causing raw value: `L1500000`
  - Full field: _L1500000|
Khalatse |
Keylong |
Leh_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0390000:
  - Error Message: **`Expected 4 parts, got 1: Khalatse`**
  - Causing raw value: `Khalatse `
  - Full field: _L1500000|
Khalatse |
Keylong |
Leh_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0390000:
  - Error Message: **`Expected 4 parts, got 1: Keylong`**
  - Causing raw value: `Keylong `
  - Full field: _L1500000|
Khalatse |
Keylong |
Leh_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0390000:
  - Error Message: **`Expected 4 parts, got 1: Leh`**
  - Causing raw value: `Leh`
  - Full field: _L1500000|
Khalatse |
Keylong |
Leh_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0390000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0400000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0400000:
  - Error Message: **`Expected 4 parts, got 1: vor 1854 Sarepta - Lehrer`**
  - Causing raw value: `vor 1854 Sarepta - Lehrer`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0400000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0400000:
  - Error Message: **`Invalid work id: Heinrich Benno Möschler: "Ein neuer Spanner Pericallia (Ennomos) Freitagaria. m.", in: Entomologische Zeitung 15 (1854), S. 143-145. (should be R-ID, or M-ID)`**
  - Causing raw value: `Heinrich Benno Möschler: "Ein neuer Spanner Pericallia (Ennomos) Freitagaria. m.", in: Entomologische Zeitung 15 (1854), S. 143-145.`

### P0410000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0410000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Geburt - Ort** and row with ID P0410000:
  - Error Message: **`Invalid format for LocationID: Lindheim (Livland)`**
  - Causing raw value: `Lindheim (Livland)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0410000:
  - Error Message: **`Invalid ISO8601-2_Date format: 14843??`**
  - Causing raw value: `14843??`

- [ ] Error in Col: **Tod - Ort** and row with ID P0410000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0410000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0410000:
  - Error Message: **`LiteratureID must start with 'R': Mitarbeit an Heuser’s Gnadenfelder Flora`**
  - Causing raw value: `Mitarbeit an Heuser’s 
Gnadenfelder Flora`

### P0420000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0420000:
  - Error Message: **`URL is not valid: nein (2024-11-20)`**
  - Causing raw value: `nein (2024-11-20) `

- [ ] Error in Col: **Geburt - Ort** and row with ID P0420000:
  - Error Message: **`LocationID must start with 'L': Barby`**
  - Causing raw value: `Barby`

- [ ] Error in Col: **Tod - Ort** and row with ID P0420000:
  - Error Message: **`LocationID must start with 'L': Jena`**
  - Causing raw value: `Jena`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0420000:
  - Error Message: **`Expected 4 parts, got 1: Heidelberg, Jena`**
  - Causing raw value: `Heidelberg, Jena`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0420000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0440000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0440000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0440000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0440000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P0450000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0450000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0450000:
  - Error Message: **`LocationID must start with 'L': Sichern (USA)`**
  - Causing raw value: `Sichern (USA) {R0014800}`

- [ ] Error in Col: **Tod - Ort** and row with ID P0450000:
  - Error Message: **`LocationID must start with 'L': Oochgelogy, Georgia (USA)`**
  - Causing raw value: `Oochgelogy, Georgia (USA) {R0014800}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0450000:
  - Error Message: **`Expected 4 parts, got 1: USA`**
  - Causing raw value: `USA`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0450000:
  - Error Message: **`LiteratureID must start with 'R': Bericht des Br. John Gambold von der Mission unter den Cherokees in Springplace, 1815 und 1816`**
  - Causing raw value: `Bericht des Br. John Gambold von der Mission unter den Cherokees in Springplace, 1815 und 1816 {https://www.wikidata.org/wiki/Q125072075} `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0450000:
  - Error Message: **`LiteratureID must start with 'R': Bericht des Br. John Gambold von der Mission unter den Cherokees in Springplace im Staat Georgien, vom October 1812 bis zu Ende des Jahres 1814`**
  - Causing raw value: ` Bericht des Br. John Gambold von der Mission unter den Cherokees in Springplace im Staat Georgien, vom October 1812 bis zu Ende des Jahres 1814 {https://www.wikidata.org/wiki/Q125069413} `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0450000:
  - Error Message: **`LiteratureID must start with 'R': Bericht des Bruders John Gambold von dem Indianer-Gemeinlein in Oochgeelogy, vom April 1821 bis gegen das Ende 1822`**
  - Causing raw value: ` Bericht des Bruders John Gambold von dem Indianer-Gemeinlein in Oochgeelogy, vom April 1821 bis gegen das Ende 1822 {https://www.wikidata.org/wiki/Q125132419}`

### P0460000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0460000:
  - Error Message: **`LocationID must start with 'L': Bethlehem (Pennsylvania)`**
  - Causing raw value: `Bethlehem (Pennsylvania)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0460000:
  - Error Message: **`LocationID must start with 'L': Spring Place (USA)`**
  - Causing raw value: `Spring Place (USA)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0460000:
  - Error Message: **`Expected 4 parts, got 1: USA`**
  - Causing raw value: `USA`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0460000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0460000:
  - Error Message: **`LiteratureID must start with 'R': Anna Rosina Gambold: "Plants of the Cherokee country: A list of plants found in the neighborhood of Conasarga River (Cherokee Country) where Springplace is situated; made by Mrs. Gambold, at the request of the Rev. Elias Cornelius", in: The American journal of science and arts 1 (1819), S. 245–251. a list of more than 300 plants and an ppendedlist of 38 plants used by the Cherokees for food,medicine, and manufacture`**
  - Causing raw value: `Anna Rosina Gambold: "Plants of the Cherokee country: A list of plants found in the neighborhood of Conasarga River (Cherokee Country) where Springplace is situated; made by Mrs. Gambold, at the request of the Rev. Elias Cornelius", in: The American journal of science and arts 1 (1819), S. 245–251. a list of more than 300 plants and an ppended
list of 38 plants used by the Cherokees for food,
medicine, and manufacture`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0460000:
  - Error Message: **`Invalid work id: Gotthilf Heinrich Ernst Mühlenberg: Catalogus Plantarum Americae Septentrionalis, Hoc Usque Cognitarum Indigenarum et Cicurum, or, A Catalogue of the Hitherto Known Native and Naturalized Plants of North America; Arranged According to the Sexual System of Linnaeus, Philadelphia, PA.: Solomon W. Conrad 2nd ed. Aufl. 1808. (should be R-ID, or M-ID)`**
  - Causing raw value: `Gotthilf Heinrich Ernst [Henry] Mühlenberg: Catalogus Plantarum Americae Septentrionalis, Hoc Usque Cognitarum Indigenarum et Cicurum, or, A Catalogue of the Hitherto Known Native and Naturalized Plants of North America; Arranged According to the Sexual System of Linnaeus, Philadelphia, PA.: Solomon W. Conrad 2nd ed. Aufl.  1808. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0460000:
  - Error Message: **`Invalid work id: Daniel L. McKinley: "ANNA ROSINA (KLIEST) GAMBOLD (1762-1821), MORAVIAN MISSIONARY TO THE CHEROKEES, WITH SPECIAL REFERENCE TO HER BOTANICAL INTERESTS ", in: Transactions of the Moravian Historical Society 28 (1994), S. 59-99 (should be R-ID, or M-ID)`**
  - Causing raw value: `Daniel L. McKinley: "ANNA ROSINA (KLIEST) GAMBOLD (1762-1821), MORAVIAN MISSIONARY TO THE CHEROKEES, WITH SPECIAL REFERENCE TO HER BOTANICAL INTERESTS ", in: Transactions of the Moravian Historical Society 28 (1994), S. 59-99 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0460000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014`

### P0470000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0470000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0470000:
  - Error Message: **`LocationID must start with 'L': Jeinsen`**
  - Causing raw value: `Jeinsen`

- [ ] Error in Col: **Tod - Ort** and row with ID P0470000:
  - Error Message: **`LocationID must start with 'L': Schwarren (Curland)`**
  - Causing raw value: `Schwarren (Curland)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0470000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0480000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0480000:
  - Error Message: **`URL is not valid: ?`**
  - Causing raw value: `?`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0480000:
  - Error Message: **`Expected 4 parts, got 1: Labrador -- Missionar?`**
  - Causing raw value: `Labrador -- Missionar?`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0480000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0485000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0485000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0485000:
  - Error Message: **`Expected 4 parts, got 1: Suriname`**
  - Causing raw value: `Suriname`

- [ ] Error in Col: **Wichtige Werke der Person ohne botanischen Kontext** and row with ID P0485000:
  - Error Message: **`Invalid work id: Wilhelm Christian Genth: "Bericht des Bruders Wilhelm Christian Genth von seiner Reise von seinem zeitherigen Posten an der Neukeer nach Paramaribo, im Jahr 1819", in: Nachrichten aus der Brüdergemeine (1820), Heft 4, S. 652-663. (should be R-ID, or M-ID)`**
  - Causing raw value: `Wilhelm Christian Genth: "Bericht des Bruders Wilhelm Christian Genth von seiner Reise von seinem zeitherigen Posten an der Neukeer nach Paramaribo, im Jahr 1819", in: Nachrichten aus der Brüdergemeine (1820), Heft 4, S. 652-663.`

### P0490000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0490000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0490000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1826-?-?`**
  - Causing raw value: `1826-?-?`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0490000:
  - Error Message: **`LocationID must start with 'L': Krasnoarmeysk (Wolgograd)`**
  - Causing raw value: `Krasnoarmeysk (Wolgograd)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0490000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0490000:
  - Error Message: **`Expected 4 parts, got 1: Krasnoarmeysk (Wolgograd)`**
  - Causing raw value: `Krasnoarmeysk (Wolgograd)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0490000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0500000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0500000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0500000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Tod - Ort** and row with ID P0500000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0500000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0500000:
  - Error Message: **`LiteratureID must start with 'R': SareptanerOrtsgeschichte`**
  - Causing raw value: `Sareptaner
Ortsgeschichte`

### P0510000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0510000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0510000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Tod - Ort** and row with ID P0510000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0510000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0520000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0520000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0520000:
  - Error Message: **`LocationID must start with 'L': Krasnoarmeysk (Wolgograd)`**
  - Causing raw value: `Krasnoarmeysk (Wolgograd)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0520000:
  - Error Message: **`LocationID must start with 'L': Königsfeld im Schwarzwald`**
  - Causing raw value: `Königsfeld im Schwarzwald`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0520000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0520000:
  - Error Message: **`LiteratureID must start with 'R': 1865: Beiträge zur Naturgeschichte der Saigaantilope`**
  - Causing raw value: `1865: Beiträge zur 
Naturgeschichte der Saigaantilope`

### P0530000

- [ ] Error in Col: **Geburt - Datum** and row with ID P0530000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1792-08-2`**
  - Causing raw value: `1792-08-2`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0530000:
  - Error Message: **`Invalid format for LocationID: Landhausen (Oberhessen)`**
  - Causing raw value: `Landhausen (Oberhessen)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0530000:
  - Error Message: **`LocationID must start with 'L': Herrnhut,`**
  - Causing raw value: `Herrnhut, `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0530000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0530000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. (should be R-ID, or M-ID)`**
  - Causing raw value: `James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222.`

### P0535000

- [ ] Error in Col: **Tod - Ort** and row with ID P0535000:
  - Error Message: **`Invalid format for LocationID: L2250000 oder Nisky auf St. Thomas?`**
  - Causing raw value: `L2250000 oder Nisky auf St. Thomas? {R0007000}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0535000:
  - Error Message: **`Cannot parse as date or period: '1819/1825 St. Jan, St. Croix'`**
  - Causing raw value: `1819/1825 St. Jan, St. Croix; ; ; {R0007000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0535000:
  - Error Message: **`Expected 4 parts, got 5: 1825/1831; L0800000; ; ;`**
  - Causing raw value: ` 1825/1831; L0800000; ; ; {R0007000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0535000:
  - Error Message: **`Expected 4 parts, got 5: 1831/; Kleinwelka; Knabenanstalt; Schüler;`**
  - Causing raw value: ` 1831/; Kleinwelka; Knabenanstalt; Schüler; {R0007000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0535000:
  - Error Message: **`Expected 4 parts, got 3: 1854/1865; Westindische Inseln; Missionar`**
  - Causing raw value: ` 1854/1865; Westindische Inseln; Missionar {R0007000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0535000:
  - Error Message: **`LocationID must start with 'L': Sachsen`**
  - Causing raw value: ` 1865/1866; Sachsen; ; {R0007000}`

### P0540000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0540000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0540000:
  - Error Message: **`LocationID must start with 'L': Augsburg`**
  - Causing raw value: `Augsburg`

- [ ] Error in Col: **Tod - Ort** and row with ID P0540000:
  - Error Message: **`LocationID must start with 'L': Wittenberg`**
  - Causing raw value: `Wittenberg`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0540000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0545000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0545000:
  - Error Message: **`Cannot parse as date or period: '1877-1888'`**
  - Causing raw value: `1877-1888; L1300000; ; {R0005600}`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0545000:
  - Error Message: **`CollectionID must start with 'C': GLM (111346?)`**
  - Causing raw value: `GLM (111346?) `
  - Full field: _GLM (111346?) | C-DR {https://dr.jacq.org/DR085524}?_

### P0550000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0550000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Tod - Ort** and row with ID P0550000:
  - Error Message: **`Invalid format for LocationID: London`**
  - Causing raw value: `London`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0550000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0555000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0555000:
  - Error Message: **`Provided string is not in codelist: nein`**
  - Causing raw value: `nein`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0555000:
  - Error Message: **`Expected 4 parts, got 1: Harz, Blankenburg`**
  - Causing raw value: `Harz, Blankenburg`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0555000:
  - Error Message: **`PersonID must start with 'P': Breutel`**
  - Causing raw value: `Breutel`

### P0560000

- [ ] Error in Col: **Angehörige - Kinder** and row with ID P0560000:
  - Error Message: **`Invalid format for PersonID: P056500`**
  - Causing raw value: `P056500 `
  - Full field: _P056500 | P057000_

- [ ] Error in Col: **Angehörige - Kinder** and row with ID P0560000:
  - Error Message: **`Invalid format for PersonID: P057000`**
  - Causing raw value: ` P057000`
  - Full field: _P056500 | P057000_

- [ ] Error in Col: **Links - Bionomia** and row with ID P0560000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0560000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P0560000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0560000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0565000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0565000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P0565000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0565000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0570000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0570000:
  - Error Message: **`LocationID must start with 'L': Neusalz`**
  - Causing raw value: `Neusalz`

- [ ] Error in Col: **Tod - Ort** and row with ID P0570000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0570000:
  - Error Message: **`Invalid work id: NEIN (should be R-ID, or M-ID)`**
  - Causing raw value: `NEIN`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0570000:
  - Error Message: **`PersonID must start with 'P': sein Schwager war`**
  - Causing raw value: `sein Schwager war `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0570000:
  - Error Message: **`Invalid work id: T. Küster: Register zur Flora von Herrnhut und Umgebung von Wilhelm Schultze, 1902, UA.NB.VI.63.nr.2, S. 93 (should be R-ID, or M-ID)`**
  - Causing raw value: `T. Küster: Register zur Flora von Herrnhut und Umgebung von Wilhelm Schultze, 1902, UA.NB.VI.63.nr.2, S. 93 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0570000:
  - Error Message: **`Invalid work id: Barber: Flora der Oberlausitz (1898) (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Barber: Flora der Oberlausitz (1898) `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0570000:
  - Error Message: **`Invalid work id: Frank Seeliger: „Einer prügelt uns und der andere bringt uns Religion ...“ Eine ethnohistorosche Studie über Fremdheitserfahrung in der zweiten Hälfte des 19. Jahrhunderts im Tibetisch-buddhistischen West-Himalaya-Gebiet Lahoul aus Sicht Herrnhuter Missionare, 2002 , 67 (should be R-ID, or M-ID)`**
  - Causing raw value: `Frank Seeliger: „Einer prügelt uns und der andere bringt uns Religion ...“ Eine ethnohistorosche Studie über Fremdheitserfahrung in der zweiten Hälfte des 19. Jahrhunderts im Tibetisch-buddhistischen West-Himalaya-Gebiet Lahoul aus Sicht Herrnhuter Missionare,  2002 [Beiheft der Unitas Fratrum], 67`

### P0580000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0580000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0580000:
  - Error Message: **`LocationID must start with 'L': Niesky auf St. Thomas`**
  - Causing raw value: `Niesky auf St. Thomas`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0580000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0590000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0590000:
  - Error Message: **`URL is not valid: https://de.bionomia.net/Q21514642 (Ist er das?)`**
  - Causing raw value: `https://de.bionomia.net/Q21514642 (Ist er das?)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0590000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0600000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0600000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0600000:
  - Error Message: **`LocationID must start with 'L': Paramaibo`**
  - Causing raw value: `Paramaibo`

- [ ] Error in Col: **Tod - Datum** and row with ID P0600000:
  - Error Message: **`Invalid ISO8601-2_Date format: 55?`**
  - Causing raw value: `55?`

- [ ] Error in Col: **Tod - Ort** and row with ID P0600000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0600000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0600000:
  - Error Message: **`Invalid work id: T. Küster: Register zur Flora von Herrnhut und Umgebung von Wilhelm Schultze, 1902, UA.NB.VI.63.nr.2, S. 93 (should be R-ID, or M-ID)`**
  - Causing raw value: `T. Küster: Register zur Flora von Herrnhut und Umgebung von Wilhelm Schultze, 1902, UA.NB.VI.63.nr.2, S. 93`

### P0610000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0610000:
  - Error Message: **`URL is not valid: nein (2024-11-21)`**
  - Causing raw value: `nein (2024-11-21)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0610000:
  - Error Message: **`LocationID must start with 'L': Norrköping Schweden`**
  - Causing raw value: `Norrköping Schweden`

### P0615000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0615000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0630000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0630000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0630000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 257 (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 257`

### P0640000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0640000:
  - Error Message: **`Expected 4 parts, got 10: 1884/1889; Surinam; ; 1892/1904; Surinam; ;1908/1911; Surinam; ;`**
  - Causing raw value: `1884/1889; Surinam; ; 
1892/1904; Surinam; ;
1908/1911; Surinam; ;`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0640000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0640000:
  - Error Message: **`Invalid work id: David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79 (should be R-ID, or M-ID)`**
  - Causing raw value: `David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79`
  - Full field: _David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79|
R0003600_

### P0650000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0650000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0650000:
  - Error Message: **`Invalid Reference Document value: R0000700} |1788/1789 {R0000600 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `1780 {R0000700} |
1788/1789 {R0000600}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0650000:
  - Error Message: **`Expected 4 parts, got 1: Labrador -- Missionar`**
  - Causing raw value: `Labrador -- Missionar`
  - Full field: _Labrador -- Missionar|
Wolgaregion, Schwarzes Meer, Sibirien ? Belegexemplare von 1816/1817 in Moskau_

- [ ] Error in Col: **Wirkungsorte** and row with ID P0650000:
  - Error Message: **`Expected 4 parts, got 1: Wolgaregion, Schwarzes Meer, Sibirien ? Belegexemplare von 1816/1817 in Moskau`**
  - Causing raw value: `Wolgaregion, Schwarzes Meer, Sibirien ? Belegexemplare von 1816/1817 in Moskau`
  - Full field: _Labrador -- Missionar|
Wolgaregion, Schwarzes Meer, Sibirien ? Belegexemplare von 1816/1817 in Moskau_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0650000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P0650000:
  - Error Message: **`PersonID must start with 'P': Michael Christian Sommer (Naturalienhändler) laut Label von Belegen in Hallehttps://de.wikipedia.org/wiki/Michael_Christian_Sommer`**
  - Causing raw value: `Michael Christian Sommer (Naturalienhändler) laut Label von Belegen in Halle
https://de.wikipedia.org/wiki/Michael_Christian_Sommer`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0650000:
  - Error Message: **`Invalid Reference Document value: https://www.botanicalcollections.be/specimen/BR0000036114139} {http://www.botanicalcollections.be/specimen/BR0000035702993 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: ` 
C-BR {https://www.botanicalcollections.be/specimen/BR0000036114139} {http://www.botanicalcollections.be/specimen/BR0000035702993} `
  - Full field: _C-B {https://herbarium.bgbm.org/object/B100241502}|
C-HAL {https://hal.jacq.org/HAL0084109}| 
C-BR {https://www.botanicalcollections.be/specimen/BR0000036114139} {http://www.botanicalcollections.be/specimen/BR0000035702993} |
C-MW {https://www.gbif.org/occurrence/5235292301} {https://www.gbif.org/occurrence/1697161971}_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0650000:
  - Error Message: **`Invalid Reference Document value: https://www.gbif.org/occurrence/5235292301} {https://www.gbif.org/occurrence/1697161971 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `C-MW {https://www.gbif.org/occurrence/5235292301} {https://www.gbif.org/occurrence/1697161971}`
  - Full field: _C-B {https://herbarium.bgbm.org/object/B100241502}|
C-HAL {https://hal.jacq.org/HAL0084109}| 
C-BR {https://www.botanicalcollections.be/specimen/BR0000036114139} {http://www.botanicalcollections.be/specimen/BR0000035702993} |
C-MW {https://www.gbif.org/occurrence/5235292301} {https://www.gbif.org/occurrence/1697161971}_

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0650000:
  - Error Message: **`Invalid work id: Dietrich Franz Leonhard von Schlechtendal: "Über die Flora von Labrador ", in: Linnaea : Ein Journal für die Botanik in ihrem ganzen Umfange 10 (1836), S. 76-114 (should be R-ID, or M-ID)`**
  - Causing raw value: `Dietrich Franz Leonhard von Schlechtendal: "Über die Flora von Labrador ", in: Linnaea : Ein Journal für die Botanik in ihrem ganzen Umfange 10 (1836), S. 76-114 `

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0650000:
  - Error Message: **`Invalid work id: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 (should be R-ID, or M-ID)`**
  - Causing raw value: `Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 `

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0650000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222.`

### P0655000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0655000:
  - Error Message: **`Expected 4 parts, got 1: L2160000`**
  - Causing raw value: `L2160000`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0655000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0660000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0660000:
  - Error Message: **`Expected 4 parts, got 1: Labrador -- Missionar`**
  - Causing raw value: `Labrador -- Missionar`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0660000:
  - Error Message: **`LiteratureID must start with 'R': Jahresberichte der Königl. Schwedischen Akademie der Wissenschaften über dis Fortschritte der Botanik im Jahre 1828 - https://www.yumpu.com/de/document/read/11778551/jahresbericht-der-konigl-schwedischen-akademie-der-`**
  - Causing raw value: `Jahresberichte der Königl. Schwedischen Akademie der Wissenschaften über dis Fortschritte der Botanik im Jahre 1828 - https://www.yumpu.com/de/document/read/11778551/jahresbericht-der-konigl-schwedischen-akademie-der- `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0660000:
  - Error Message: **`Invalid work id: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 (should be R-ID, or M-ID)`**
  - Causing raw value: `Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0660000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222 (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0660000:
  - Error Message: **`Invalid work id: Henry Fischer; Heike Heklau; Elfriede Wagner: "Botanischer Wissenstransfer in Briefen des 19. Jahrhunderts. Die Briefe des deutschen Botanikers Ernst Heinrich Friedrich Meyer (1791–1858) an Diederich Franz Leonhard von Schlechtendal (1794–1866) ", in: Schlechtendalia 40 (2023), S. 3-235, S. 42 in Brief E.H.F.Meyer an D.F.L.v. Schlechtendahl, 27.12.1825 (should be R-ID, or M-ID)`**
  - Causing raw value: `Henry Fischer; Heike Heklau; Elfriede Wagner: "Botanischer Wissenstransfer in Briefen des 19. Jahrhunderts. Die Briefe des deutschen Botanikers Ernst Heinrich Friedrich Meyer (1791–1858) an Diederich Franz Leonhard von Schlechtendal (1794–1866) ", in: Schlechtendalia 40 (2023), S. 3-235, S. 42 in Brief E.H.F.Meyer an D.F.L.v. Schlechtendahl, 27.12.1825`

### P0670000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0670000:
  - Error Message: **`URL is not valid: nein (2024-11-26)`**
  - Causing raw value: `nein (2024-11-26)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0670000:
  - Error Message: **`Expected 4 parts, got 1: Südafrika Genadenthal 1858-1894`**
  - Causing raw value: `Südafrika Genadenthal 1858-1894`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0670000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0670000:
  - Error Message: **`LiteratureID must start with 'R': Objekte und med. Beschreibung erwähnt in:Edward Morell Holmes: Catalogue of the Herbarium of Medical plants in the Museum of the Pharmaceutical Society of Great Britain, London 1896`**
  - Causing raw value: `Objekte und med. Beschreibung erwähnt in:
Edward Morell Holmes: Catalogue of the Herbarium of Medical plants in the Museum of the Pharmaceutical Society of Great Britain, London 1896 `
  - Full field: _Objekte und med. Beschreibung erwähnt in:
Edward Morell Holmes: Catalogue of the Herbarium of Medical plants in the Museum of the Pharmaceutical Society of Great Britain, London 1896 | 
Cape Colony, Sooth Africa: COLONIAL AND INDIAN EXHIBITION, LONDON, 1886. Catalogue of the Exhibits of the Colony of the Cape of Good Hope, London: Richards, Glanville & Co. 1886._

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0670000:
  - Error Message: **`LiteratureID must start with 'R': Cape Colony, Sooth Africa: COLONIAL AND INDIAN EXHIBITION, LONDON, 1886. Catalogue of the Exhibits of the Colony of the Cape of Good Hope, London: Richards, Glanville & Co. 1886.`**
  - Causing raw value: ` 
Cape Colony, Sooth Africa: COLONIAL AND INDIAN EXHIBITION, LONDON, 1886. Catalogue of the Exhibits of the Colony of the Cape of Good Hope, London: Richards, Glanville & Co. 1886.`
  - Full field: _Objekte und med. Beschreibung erwähnt in:
Edward Morell Holmes: Catalogue of the Herbarium of Medical plants in the Museum of the Pharmaceutical Society of Great Britain, London 1896 | 
Cape Colony, Sooth Africa: COLONIAL AND INDIAN EXHIBITION, LONDON, 1886. Catalogue of the Exhibits of the Colony of the Cape of Good Hope, London: Richards, Glanville & Co. 1886._

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0670000:
  - Error Message: **`Invalid work id: Gunn, M. & Codd, L.E. Bot. Explor. S. Afr. (1981): 187 (should be R-ID, or M-ID)`**
  - Causing raw value: `Gunn, M. & Codd, L.E. Bot. Explor. S. Afr. (1981): 187 `
  - Full field: _Gunn, M. & Codd, L.E. Bot. Explor. S. Afr. (1981): 187 | _

### P0680000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0680000:
  - Error Message: **`Expected 4 parts, got 14: 1898/1908; ; ;1909/1912; ; ;1912/1914; ; ;1914/1932 ; ;1932/1934 ; ;`**
  - Causing raw value: `1898/1908; [Hopedal] ; ;
1909/1912; [Okak] ; ;
1912/1914; [Hopedal] ; ;
1914/1932[Nain] ; ;
1932/1934 [Makkovik ; ;
1934/1947 [Nain] ; ;`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0680000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0690000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0690000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0690000:
  - Error Message: **`LocationID must start with 'L': Groß-Kniegnitz (Schlesien)`**
  - Causing raw value: `Groß-Kniegnitz (Schlesien)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0690000:
  - Error Message: **`LocationID must start with 'L': Brooklyn (New York)`**
  - Causing raw value: `Brooklyn (New York)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: Sept. 1862 in Ebersdorfmit Datum vom 24.9.1862 Verkaufanzeige für sein gesamtes Herbarium (Einiges über die Flora von Ebersdorf, 1862, S. 387f.)1762 Selbstbezeichnung als Cand. Theol. U. Fr. Einiges über die Flora von Ebersdorf, 1862, S. 387f.)`**
  - Causing raw value: `Sept. 1862 in Ebersdorf
mit Datum vom 24.9.1862 Verkaufanzeige für sein gesamtes Herbarium (Einiges über die Flora von Ebersdorf, 1862, S. 387f.)
1762 Selbstbezeichnung als Cand. Theol. U. Fr. Einiges über die Flora von Ebersdorf, 1862, S. 387f.)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: 1864 18. Juli Ankunft in New York`**
  - Causing raw value: ` 
1864 18. Juli Ankunft in New York `

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: ab Ende 1865 in New Orleans`**
  - Causing raw value: ` 
ab Ende 1865 in New Orleans`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: Universität Greifswald (Medizinstudium um in Indien Missionar zu werden (Bayerschmidt: 164)`**
  - Causing raw value: `Universität Greifswald (Medizinstudium um in Indien Missionar zu werden  (Bayerschmidt: 164)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: Kaiserswaldau Schlesien als Arzt, dort Heirat mit Laura Lenke (Bayerschmidt: 164)`**
  - Causing raw value: `Kaiserswaldau Schlesien als Arzt, dort Heirat mit Laura Lenke (Bayerschmidt: 164)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: 1884 Leipzig (Bayerschmidt: 164)`**
  - Causing raw value: `1884 Leipzig (Bayerschmidt: 164)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0690000:
  - Error Message: **`Expected 4 parts, got 1: 1889 Ausreise nach Amerika Brooklyn (Bayerschmidt: 164)`**
  - Causing raw value: `1889 Ausreise nach Amerika Brooklyn (Bayerschmidt: 164)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0690000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P0690000:
  - Error Message: **`PersonID must start with 'P': Mettetal, Gustav Wetschky und Max Wetschky in Gnadenfeld`**
  - Causing raw value: `Mettetal, Gustav Wetschky und Max Wetschky in Gnadenfeld {R0009800} `
  - Full field: _Mettetal, Gustav Wetschky und Max Wetschky in Gnadenfeld {R0009800} | P1690000 {R0010300}_

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0690000:
  - Error Message: **`ManuscriptID must start with 'M': 1859 Flora Gnadenfeldensis : neue Flora Gnadenfeldensis mit 1127 Arten, auf der Grundlage der Flora Gnadenfeldensis von F.W. Kölbing („Flora von Gnadenfeld inclusive der Flora von Troppau, Jägerndorf und des Annaberges Vierte Bearbeitung. Mit einer Karte. Gnadenfeld 1859“ UA ThS/L V 7). – bis 1898 immer wieder mit Nachträgen versehen, wurde Gemeinschaftswerk unter Mitarbeit von: A. Menzel, M. Wetschky, W. Schultze, G. Freytag`**
  - Causing raw value: `1859 Flora Gnadenfeldensis [Ms.]: neue Flora Gnadenfeldensis mit 1127 Arten, auf der Grundlage der Flora Gnadenfeldensis von F.W. Kölbing („Flora von Gnadenfeld inclusive der Flora von Troppau, Jägerndorf und des Annaberges […] Vierte Bearbeitung. Mit einer Karte. Gnadenfeld 1859“ UA ThS/L V 7). – bis 1898 immer wieder mit Nachträgen versehen, wurde Gemeinschaftswerk unter Mitarbeit von: A. Menzel, M. Wetschky,  W. Schultze, G. Freytag  `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser: "Einige Bemerkungen über interessante Pflanzen Schlesiens, im Anschlusse an die neue Bearbeitung der Flora von Schlesien von Dr. Wimmer 1857, mit Berücksichtigung von Koch’s Taschenbuch der deutschen Flora in der neuen Auflage vom Jahre 1856.", in: Oestereichisches Botanisches Wochenblatt 6 (1856), Nr. 28, S. 196-199.`**
  - Causing raw value: `Paul Heuser: "Einige Bemerkungen über interessante Pflanzen Schlesiens, im Anschlusse an die neue Bearbeitung der Flora von Schlesien von Dr. Wimmer 1857, mit Berücksichtigung von Koch’s Taschenbuch der deutschen Flora in der neuen Auflage vom Jahre 1856.", in: Oestereichisches Botanisches Wochenblatt 6 (1856), Nr. 28, S. 196-199.`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser; Samuel Weiz: "Einiges über Labrador und seine Flora", in: Österreichische Botanische Zeitschrift 9 (1859), S. 315-323.`**
  - Causing raw value: `Paul Heuser; Samuel Weiz: "Einiges über Labrador und seine Flora", in: Österreichische Botanische Zeitschrift 9 (1859), S. 315-323.`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser: "Einige Bemerkungen über interessante Pflanzen Schlesiens, VI Teile", in: Österreichische Botanische Zeitschrift 9 u. 10 (1859-1860), 1859 in Nr. 9. S. 196-199, 254-256; 1860 in Nr. 10, S. 9-13, 42-46, 186-189, 358-361.`**
  - Causing raw value: `Paul Heuser: "Einige Bemerkungen über interessante Pflanzen Schlesiens, VI Teile", in: Österreichische Botanische Zeitschrift 9 u. 10 (1859-1860),  1859 in Nr. 9. S. 196-199, 254-256; 1860 in Nr. 10, S. 9-13, 42-46, 186-189, 358-361.`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser: "Eine botanische Excursion in der Umgegend von Gnadau", in: Österreichische Botanische Zeitschrift 12 (1862), Nr. 2, S. 38-43.`**
  - Causing raw value: `Paul Heuser: "Eine botanische Excursion in der Umgegend von Gnadau", in: Österreichische Botanische Zeitschrift 12 (1862), Nr. 2, S. 38-43. `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser: "Einiges über die Flora von Ebersdorf", in: Österreichische Botanische Zeitschrift 12 (1862), Nr. 12, S. 387-395.`**
  - Causing raw value: `Paul Heuser: "Einiges über die Flora von Ebersdorf", in: Österreichische Botanische Zeitschrift 12 (1862), Nr. 12, S. 387-395.`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser: "Amerikanisches", in: Österreichische Botanische Zeitschrift 15 (1865), S. 38-48.`**
  - Causing raw value: `Paul Heuser: "Amerikanisches", in: Österreichische Botanische Zeitschrift 15 (1865), S. 38-48.`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0690000:
  - Error Message: **`LiteratureID must start with 'R': Paul Heuser: "Ein Gruss aus der neuen Welt", in: Österreichische Botanische Zeitschrift 16 (1866), Nr. 10, S. 301-314.`**
  - Causing raw value: `Paul Heuser: "Ein Gruss aus der neuen Welt", in: Österreichische Botanische Zeitschrift 16 (1866), Nr. 10, S. 301-314.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0690000:
  - Error Message: **`Invalid work id: Hardke u.a. 2004, S. 128 (should be R-ID, or M-ID)`**
  - Causing raw value: `Hardke u.a. 2004, S. 128 `
  - Full field: _Hardke u.a. 2004, S. 128 | 
Infos zu seinem Herbar: https://ia902909.us.archive.org/21/items/beiheftezumbotan3411unse/beiheftezumbotan3411unse.pdf | 
Im Funkenachlass DD |_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0690000:
  - Error Message: **`Invalid work id: Infos zu seinem Herbar: https://ia902909.us.archive.org/21/items/beiheftezumbotan3411unse/beiheftezumbotan3411unse.pdf (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Infos zu seinem Herbar: https://ia902909.us.archive.org/21/items/beiheftezumbotan3411unse/beiheftezumbotan3411unse.pdf `
  - Full field: _Hardke u.a. 2004, S. 128 | 
Infos zu seinem Herbar: https://ia902909.us.archive.org/21/items/beiheftezumbotan3411unse/beiheftezumbotan3411unse.pdf | 
Im Funkenachlass DD |_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0690000:
  - Error Message: **`Invalid work id: Im Funkenachlass DD (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Im Funkenachlass DD `
  - Full field: _Hardke u.a. 2004, S. 128 | 
Infos zu seinem Herbar: https://ia902909.us.archive.org/21/items/beiheftezumbotan3411unse/beiheftezumbotan3411unse.pdf | 
Im Funkenachlass DD |_

### P0700000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0700000:
  - Error Message: **`LocationID must start with 'L': Girlachsdorf (Schlesien)`**
  - Causing raw value: `Girlachsdorf (Schlesien)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0700000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0700000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0710000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0710000:
  - Error Message: **`LocationID must start with 'L': Döbra (Sachsen)`**
  - Causing raw value: `Döbra (Sachsen)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0710000:
  - Error Message: **`LocationID must start with 'L': Madras (Chennai) Indien`**
  - Causing raw value: `Madras (Chennai) Indien`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0710000:
  - Error Message: **`Expected 4 parts, got 1: Indien`**
  - Causing raw value: `Indien`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0710000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0710000:
  - Error Message: **`LiteratureID must start with 'R': Heyne (1814): Tracts, historical and statistical, on India: with journals of several tours through various parts of the peninsula: also, an account of Sumatra, in a series of letters", printed for R. Baldwin and Black, Parry and Co.`**
  - Causing raw value: `Heyne (1814): Tracts, historical and statistical, on India: with journals of several tours through various parts of the peninsula: also, an account of Sumatra, in a series of letters", printed for R. Baldwin and Black, Parry and Co.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0710000:
  - Error Message: **`Invalid work id: Roth (1821): Novae plantarum species praesertim Indiae orientalis (should be R-ID, or M-ID)`**
  - Causing raw value: `Roth (1821): Novae plantarum species praesertim Indiae orientalis`

### P0720000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0720000:
  - Error Message: **`URL is not valid: nein (2024-11-26)`**
  - Causing raw value: `nein (2024-11-26)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0720000:
  - Error Message: **`LocationID must start with 'L': Schmiedeberg`**
  - Causing raw value: `Schmiedeberg`

- [ ] Error in Col: **Tod - Ort** and row with ID P0720000:
  - Error Message: **`LocationID must start with 'L': Ebersdorf`**
  - Causing raw value: `Ebersdorf`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0720000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0730000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0730000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0735000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0735000:
  - Error Message: **`Expected 4 parts, got 5: 1875/1898; L1110000;;;{R0000600}`**
  - Causing raw value: `1875/1898; L1110000;;;{R0000600}`

### P0740000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0740000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0750000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0750000:
  - Error Message: **`URL is not valid: nein (2024-11-26)`**
  - Causing raw value: `nein (2024-11-26)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0750000:
  - Error Message: **`Expected 4 parts, got 1: Zeist, Leitung der dortigen Gemeine`**
  - Causing raw value: `Zeist, Leitung der dortigen Gemeine`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0750000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0750000:
  - Error Message: **`Invalid work id: David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79 (should be R-ID, or M-ID)`**
  - Causing raw value: `David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79`

### P075500

- [ ] Error in Col: **ID** and row with ID P075500:
  - Error Message: **`Invalid format for PersonID: P075500`**
  - Causing raw value: `P075500`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P075500:
  - Error Message: **`PersonID must start with 'P': {R0004100}`**
  - Causing raw value: `{R0004100}`

### P0760000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0760000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0770000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0770000:
  - Error Message: **`URL is not valid: nein (2024-11-27)`**
  - Causing raw value: `nein (2024-11-27)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0770000:
  - Error Message: **`Expected 4 parts, got 1: Nordamerika`**
  - Causing raw value: `Nordamerika`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0770000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0770000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P0780000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0780000:
  - Error Message: **`URL is not valid: nein (2024-11-27)`**
  - Causing raw value: `nein (2024-11-27)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0780000:
  - Error Message: **`Expected 4 parts, got 1: Nordamerika`**
  - Causing raw value: `Nordamerika`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0780000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0780000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P0790000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0790000:
  - Error Message: **`URL is not valid: nein (2024-11-27)`**
  - Causing raw value: `nein (2024-11-27)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0790000:
  - Error Message: **`Expected 4 parts, got 1: Nordamerika`**
  - Causing raw value: `Nordamerika`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0790000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0790000:
  - Error Message: **`CollectionID must start with 'C': Kontrolle im Nationalherbarium Belgien als Acession Nr. 100?`**
  - Causing raw value: `Kontrolle im Nationalherbarium Belgien als Acession Nr. 100?`

### P0800000

- [ ] Error in Col: **Tod - Ort** and row with ID P0800000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0800000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0800000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P0810000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0810000:
  - Error Message: **`URL is not valid: nein (2024-11-27)`**
  - Causing raw value: `nein (2024-11-27)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0810000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0820000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0820000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0820000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0820000:
  - Error Message: **`Expected 4 parts, got 1: Himalaya --`**
  - Causing raw value: `Himalaya -- {R0003600}`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0820000:
  - Error Message: **`Invalid work id: Frank Seeliger: „Einer prügelt uns und der andere bringt uns Religion ...“ Eine ethnohistorosche Studie über Fremdheitserfahrung in der zweiten Hälfte des 19. Jahrhunderts im Tibetisch-buddhistischen West-Himalaya-Gebiet Lahoul aus Sicht Herrnhuter Missionare, 2002 , 67 (should be R-ID, or M-ID)`**
  - Causing raw value: `Frank Seeliger: „Einer prügelt uns und der andere bringt uns Religion ...“ Eine ethnohistorosche Studie über Fremdheitserfahrung in der zweiten Hälfte des 19. Jahrhunderts im Tibetisch-buddhistischen West-Himalaya-Gebiet Lahoul aus Sicht Herrnhuter Missionare,  2002 [Beiheft der Unitas Fratrum], 67 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0820000:
  - Error Message: **`Invalid work id: John N. Bray: "Heinrich August Jaeschke: Pioneer Tibetan Scholar", in: Tibet Journal 8 (1983), Nr. 1, S. 50-55, 50 (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
John N. Bray: "Heinrich August Jaeschke: Pioneer Tibetan Scholar", in: Tibet Journal 8 (1983), Nr. 1, S. 50-55, 50 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0820000:
  - Error Message: **`Invalid work id: Theodor C. Bechler: Heinrich August Jaeschke, der geniale Sprachforscher der Mission der Brüdergemeine unter den Tibetern im westlichen Himalaya : eine Studie(Herrnhuter Missionsstudien Nr 25), Herrnhut: Missionsbuchhandlung 1930, 14f. (should be R-ID, or M-ID)`**
  - Causing raw value: ` Theodor C. Bechler: Heinrich August Jaeschke, der geniale Sprachforscher der Mission der Brüdergemeine unter den Tibetern im westlichen Himalaya : eine Studie
(Herrnhuter Missionsstudien Nr 25), Herrnhut: Missionsbuchhandlung 1930, 14f.`

### P0830000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0830000:
  - Error Message: **`URL is not valid: nein (2024-11-27)`**
  - Causing raw value: `nein (2024-11-27)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0830000:
  - Error Message: **`Expected 4 parts, got 1: Nordamerika`**
  - Causing raw value: `Nordamerika`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0830000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0830000:
  - Error Message: **`LiteratureID must start with 'R': "Kampman in 1815 provided a manuscript list of Latin botanical names to accompany a record of plants named in the language of the Lennape native Americans (Freeman 1966)." Troyer 2009, 4`**
  - Causing raw value: `"Kampman in 1815 provided a manuscript list of Latin botanical names to accompany a record of plants named in the language of the Lennape native Americans (Freeman 1966)." Troyer 2009, 4`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0830000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009 `
  - Full field: _Troyer 2009 |
Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0830000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014`
  - Full field: _Troyer 2009 |
Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014_

### P0835000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0835000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0835000:
  - Error Message: **`Invalid format for LocationID: L1200000/L1110000/L2100000`**
  - Causing raw value: `1850/1874; L1200000/L1110000/L2100000; Missionsstation; Missionar {R0014000} `
  - Full field: _1850/1874; L1200000/L1110000/L2100000; Missionsstation; Missionar {R0014000} | 1874/1876; L1120000; ; {R0014000} |_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0835000:
  - Error Message: **`Invalid Reference Document value: https://data.nhm.ac.uk/object/abba5040-0f30-436f-9d0b-a8364f63db07/1780304495491} C-K {http://specimens.kew.org/Herbarium/K006106805 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `C-BM {https://data.nhm.ac.uk/object/abba5040-0f30-436f-9d0b-a8364f63db07/1780304495491}  C-K {http://specimens.kew.org/Herbarium/K006106805} `
  - Full field: _C-BM {https://data.nhm.ac.uk/object/abba5040-0f30-436f-9d0b-a8364f63db07/1780304495491}  C-K {http://specimens.kew.org/Herbarium/K006106805} | C-B {https://herbarium.bgbm.org/object/B101113233}_

### P0840000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0840000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P0840000:
  - Error Message: **`LocationID must start with 'L': Zittau`**
  - Causing raw value: `Zittau`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0840000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0850000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0850000:
  - Error Message: **`Provided string is not in codelist: nein`**
  - Causing raw value: `nein`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0850000:
  - Error Message: **`LocationID must start with 'L': Tranquebar/Tarangambadi`**
  - Causing raw value: `Tranquebar/Tarangambadi`

- [ ] Error in Col: **Tod - Ort** and row with ID P0850000:
  - Error Message: **`LocationID must start with 'L': Tarangambadi`**
  - Causing raw value: `Tarangambadi`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0850000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0860000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0860000:
  - Error Message: **`URL is not valid: nein (2024-12-03)`**
  - Causing raw value: `nein (2024-12-03)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0860000:
  - Error Message: **`Invalid format for LocationID: Lichtenau (Grönland)`**
  - Causing raw value: `Lichtenau (Grönland)`

- [ ] Error in Col: **Tod - Ort** and row with ID P0860000:
  - Error Message: **`LocationID must start with 'L': Neuherrnhut (Grönland)`**
  - Causing raw value: `Neuherrnhut (Grönland)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0860000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P0860000:
  - Error Message: **`CollectionID must start with 'C': Als Sammler im Herbarium Reichel in Waldenburg`**
  - Causing raw value: `Als Sammler im Herbarium Reichel in Waldenburg`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0860000:
  - Error Message: **`LiteratureID must start with 'R': gab Lehrbücher über naturkundlichen Unterricht heraus`**
  - Causing raw value: `gab Lehrbücher über 
naturkundlichen 
Unterricht heraus`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0860000:
  - Error Message: **`Invalid work id: Sächsische Floristische Mitteilungen 15 2012 (should be R-ID, or M-ID)`**
  - Causing raw value: `Sächsische Floristische Mitteilungen 15 2012`

### P0870000

- [ ] Error in Col: **Tod - Ort** and row with ID P0870000:
  - Error Message: **`LocationID must start with 'L': Salem, Nazareth`**
  - Causing raw value: `Salem, Nazareth`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0870000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0870000:
  - Error Message: **`Invalid work id: Francis W. Pennell: "Botanical Collectors of the Philadelphia Local Area ", in: Bartonia 21 (1940-1941), S. 38-57, 48 (should be R-ID, or M-ID)`**
  - Causing raw value: `Francis W. Pennell: "Botanical Collectors of the Philadelphia Local Area ", in: Bartonia 21 (1940-1941), S. 38-57, 48`

### P0864000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0864000:
  - Error Message: **`LocationID must start with 'L': Grönland`**
  - Causing raw value: `1867/1896;Grönland;; {R0011100}`

### P0865000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0865000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

### P0875000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P0875000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Tod - Datum** and row with ID P0875000:
  - Error Message: **`Invalid ISO8601-2_Date format: nach 1868-12-20`**
  - Causing raw value: `nach 1868-12-20`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0875000:
  - Error Message: **`Expected 4 parts, got 1: Genadendal Südafrika (Beleg B 10 0167523)`**
  - Causing raw value: `Genadendal Südafrika (Beleg  B 10 0167523)`

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P0875000:
  - Error Message: **`PersonID must start with 'P': Herbarium Kapstadt`**
  - Causing raw value: `Herbarium Kapstadt`

### P0880000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0880000:
  - Error Message: **`Expected 4 parts, got 1: Labrador Missionar`**
  - Causing raw value: `Labrador Missionar`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: Ernesti Meyer : De Plantis Labradoricis Libri Tres, Lipsiae: Leopoldi Vossi 1830; XIV (should be R-ID, or M-ID)`**
  - Causing raw value: ` Ernesti Meyer [Ernst Heinrich Friedrich Meyer]: De Plantis Labradoricis Libri Tres, Lipsiae: Leopoldi Vossi 1830; XIV `
  - Full field: _R0005800 | Ernesti Meyer [Ernst Heinrich Friedrich Meyer]: De Plantis Labradoricis Libri Tres, Lipsiae: Leopoldi Vossi 1830; XIV |
R0006000_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: Jacques Cayouette: "Contribution des moraves à la bryologie du Labrador", in: Carnets de bryologie 3 (2013), S. 1-12. (should be R-ID, or M-ID)`**
  - Causing raw value: `Jacques Cayouette: "Contribution des moraves à la bryologie du Labrador", in: Carnets de bryologie 3 (2013), S. 1-12. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180. (should be R-ID, or M-ID)`**
  - Causing raw value: ` Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: James A. Mears: "Guide to Plant Collectors Represented in the Herbarium of the Academy of Natural Sciences of Philadelphia", in: Proceedings of the Academy of Natural Sciences of Philadelphia 133 (1981), S. 141-165. (should be R-ID, or M-ID)`**
  - Causing raw value: ` James A. Mears: "Guide to Plant Collectors Represented in the Herbarium of the Academy of Natural Sciences of Philadelphia", in: Proceedings of the Academy of Natural Sciences of Philadelphia 133 (1981), S. 141-165. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: Franz von Paula Schrank: "Aufzählung einiger Pflanzen aus Labrador, mit Anmerkung", in: Denkschriften der Königlich-Baierischen Botanischen Gesellschaft in Regensburg 1 (1818), Nr. 2, S. 1-30. (should be R-ID, or M-ID)`**
  - Causing raw value: ` Franz von Paula Schrank: "Aufzählung einiger Pflanzen aus Labrador, mit Anmerkung", in: Denkschriften der Königlich-Baierischen Botanischen Gesellschaft in Regensburg 1 (1818), Nr. 2, S. 1-30. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: James S. Pringle: "POSSIBLE EPONYMY OF THE GENERIC NAME BRASENIA SCHREB. (CABOMBACEAE)", in: SIDA, Contributions to Botany 16 (1995), Nr. 3, S. 597-600. (should be R-ID, or M-ID)`**
  - Causing raw value: ` James S. Pringle: "POSSIBLE EPONYMY OF THE GENERIC NAME BRASENIA SCHREB. (CABOMBACEAE)", in: SIDA, Contributions to Botany 16 (1995), Nr. 3, S. 597-600. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0880000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. (should be R-ID, or M-ID)`**
  - Causing raw value: ` James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222.`

### P0890000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0890000:
  - Error Message: **`Expected 4 parts, got 1: Gnadenfeld`**
  - Causing raw value: `Gnadenfeld {R0009800}`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0890000:
  - Error Message: **`ManuscriptID must start with 'M': 1824: Flora der Gegend von Gnadenfeld (Manuskript), später mit Nachträgen von Ernst Reichel und Rudolf Kölbing versehen`**
  - Causing raw value: `1824: Flora der Gegend von Gnadenfeld (Manuskript),  später mit Nachträgen von Ernst Reichel und Rudolf  Kölbing versehen `
  - Full field: _1824: Flora der Gegend von Gnadenfeld (Manuskript),  später mit Nachträgen von Ernst Reichel und Rudolf  Kölbing versehen |
1825-1827, zunächst als Manuskript, Flora der Oberlausitz, Beobachtungen von Albertini, Curie, Voullaire, Burkhardt miteingearbeitet – 1828 im Druck erschienen
Arbeitete an Vervollkommnung der Lausitzer Flora |
Gnadenfelder Flora – handschriftliche zweite Ausgabe |_

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0890000:
  - Error Message: **`ManuscriptID must start with 'M': 1825-1827, zunächst als Manuskript, Flora der Oberlausitz, Beobachtungen von Albertini, Curie, Voullaire, Burkhardt miteingearbeitet – 1828 im Druck erschienenArbeitete an Vervollkommnung der Lausitzer Flora`**
  - Causing raw value: `1825-1827, zunächst als Manuskript, Flora der Oberlausitz, Beobachtungen von Albertini, Curie, Voullaire, Burkhardt miteingearbeitet – 1828 im Druck erschienen
Arbeitete an Vervollkommnung der Lausitzer Flora `
  - Full field: _1824: Flora der Gegend von Gnadenfeld (Manuskript),  später mit Nachträgen von Ernst Reichel und Rudolf  Kölbing versehen |
1825-1827, zunächst als Manuskript, Flora der Oberlausitz, Beobachtungen von Albertini, Curie, Voullaire, Burkhardt miteingearbeitet – 1828 im Druck erschienen
Arbeitete an Vervollkommnung der Lausitzer Flora |
Gnadenfelder Flora – handschriftliche zweite Ausgabe |_

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P0890000:
  - Error Message: **`ManuscriptID must start with 'M': Gnadenfelder Flora – handschriftliche zweite Ausgabe`**
  - Causing raw value: `Gnadenfelder Flora – handschriftliche zweite Ausgabe `
  - Full field: _1824: Flora der Gegend von Gnadenfeld (Manuskript),  später mit Nachträgen von Ernst Reichel und Rudolf  Kölbing versehen |
1825-1827, zunächst als Manuskript, Flora der Oberlausitz, Beobachtungen von Albertini, Curie, Voullaire, Burkhardt miteingearbeitet – 1828 im Druck erschienen
Arbeitete an Vervollkommnung der Lausitzer Flora |
Gnadenfelder Flora – handschriftliche zweite Ausgabe |_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0890000:
  - Error Message: **`LiteratureID must start with 'R': Kölbing, Wilhelm: Flora der Oberlausitz oder Nachweisung der daselbst wild wachsenden phanerogamen Pflanzen mit Einschluß der Farrnkräuter nach Familien geordnet, Görlitz: C. G. Zobel 1828`**
  - Causing raw value: `Kölbing, [Friedrich] Wilhelm: Flora der Oberlausitz oder Nachweisung der daselbst wild wachsenden phanerogamen Pflanzen mit Einschluß der Farrnkräuter nach Familien geordnet, Görlitz: C. G. Zobel 1828`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0890000:
  - Error Message: **`Invalid work id: R0003200R0009800 (should be R-ID, or M-ID)`**
  - Causing raw value: `R0003200
R0009800`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0890000:
  - Error Message: **`Invalid work id: Hardtke (should be R-ID, or M-ID)`**
  - Causing raw value: `Hardtke`

### P0900000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0900000:
  - Error Message: **`URL is not valid: nein (2024-12-03)`**
  - Causing raw value: `nein (2024-12-03)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0900000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P0900000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0900000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0910000

- [ ] Error in Col: **Wirkungsorte** and row with ID P0910000:
  - Error Message: **`Expected 4 parts, got 1: Gndenfeld {R0009800}Gnadenthal (Südafrika)`**
  - Causing raw value: `Gndenfeld {R0009800}
Gnadenthal (Südafrika)`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0910000:
  - Error Message: **`LiteratureID must start with 'R': Mitarbeit zu Nachträgen zu Fr. W. Kölbing's Floren daher: Rudolf Kölbing: "Nachträge zur Kölbingschen Flora", in: Abhandlungen der naturforschenden Gesellschaft zu Görlitz 3 (1842), Nr. 2, S. 17-24.`**
  - Causing raw value: `Mitarbeit zu Nachträgen zu Fr. W. Kölbing's Floren daher: Rudolf Kölbing: "Nachträge zur Kölbingschen Flora", in: Abhandlungen der naturforschenden Gesellschaft zu Görlitz 3 (1842), Nr. 2, S. 17-24. `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0910000:
  - Error Message: **`LiteratureID must start with 'R': Zusammenstellung einer Sudetenflora, einer Karpatenflora,Ordnen der Flora der Oberlausitz nach Orten(Nach­träge zur Kölbingschen Flora. Abhandl. der Naturf. Ges. Görlitz, m, 2. 1842, S. 17—24 vgl. Barber: Flora der Oberlausitz (1898))`**
  - Causing raw value: `Zusammenstellung einer Sudetenflora, einer Karpatenflora,
Ordnen der Flora der Oberlausitz nach Orten
(Nach­träge zur Kölbingschen Flora. Abhandl. der Naturf. Ges. Görlitz, m, 2. 1842, S. 17—24 vgl. Barber: Flora der Oberlausitz (1898)) `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0910000:
  - Error Message: **`LiteratureID must start with 'R': Umfassende Mitarbeit an Roser, R.F. 1856: Naturhistorische Beobachtungen…`**
  - Causing raw value: ` 
Umfassende Mitarbeit an Roser, R.F. 1856: Naturhistorische Beobachtungen… `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0910000:
  - Error Message: **`LiteratureID must start with 'R': Abhandlungen der Naturforschenden Gesellschaft zu Görlitz Ein Brief von C. R. Kölbing in Gnadenthal am Kap der guten Hoffnung MBand 04 (Heft 02) 1847`**
  - Causing raw value: ` Abhandlungen der Naturforschenden Gesellschaft zu Görlitz Ein Brief von C. R. Kölbing in Gnadenthal am Kap der guten Hoffnung MBand 04 (Heft 02) 1847`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0910000:
  - Error Message: **`Invalid work id: R0003600R0009800 (should be R-ID, or M-ID)`**
  - Causing raw value: `R0003600
R0009800`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0910000:
  - Error Message: **`Invalid work id: NBG 1861, 1079, 1085; NBG 1856, 87, 95, 154, 191, 252 (should be R-ID, or M-ID)`**
  - Causing raw value: `NBG 1861, 1079, 1085; NBG 1856, 87, 95, 154, 191, 252 `
  - Full field: _NBG 1861, 1079, 1085; NBG 1856, 87, 95, 154, 191, 252 |
HArdtke_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0910000:
  - Error Message: **`Invalid work id: HArdtke (should be R-ID, or M-ID)`**
  - Causing raw value: `HArdtke`
  - Full field: _NBG 1861, 1079, 1085; NBG 1856, 87, 95, 154, 191, 252 |
HArdtke_

### P0920000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0920000:
  - Error Message: **`URL is not valid: nein (2024-12-03)`**
  - Causing raw value: `nein (2024-12-03)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0920000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Tod - Ort** and row with ID P0920000:
  - Error Message: **`LocationID must start with 'L': Berthelsdorf`**
  - Causing raw value: `Berthelsdorf`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0920000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0930000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0930000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0930000:
  - Error Message: **`LocationID must start with 'L': Moholz bei Niesky`**
  - Causing raw value: `Moholz bei Niesky`

- [ ] Error in Col: **Tod - Ort** and row with ID P0930000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0930000:
  - Error Message: **`Expected 4 parts, got 9: /; ; Schuhmacherlehre1882/1894; ; ; Missionsschüler 1894/; ; ;Missionar`**
  - Causing raw value: ` /; ; Schuhmacherlehre
1882/1894; [Niesky];  ; Missionsschüler 
1894/;  [Kolonie dt. Ostafrika];  ;Missionar `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0930000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0930000:
  - Error Message: **`Invalid work id: Barber: Flora der Oberlausitz (1898 ) (should be R-ID, or M-ID)`**
  - Causing raw value: `Barber: Flora der Oberlausitz (1898 )`

### P0940000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0940000:
  - Error Message: **`URL is not valid: nein (2024-12-03)`**
  - Causing raw value: `nein (2024-12-03)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0940000:
  - Error Message: **`LocationID must start with 'L': Ebenezer (Australien)`**
  - Causing raw value: `Ebenezer (Australien)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0940000:
  - Error Message: **`Invalid ISO8601-2_Date format: 18948?`**
  - Causing raw value: `18948?`

- [ ] Error in Col: **Tod - Ort** and row with ID P0940000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0940000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0950000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0950000:
  - Error Message: **`LocationID must start with 'L': Ramahyuk (Australien)`**
  - Causing raw value: `Ramahyuk (Australien)`

- [ ] Error in Col: **Tod - Datum** and row with ID P0950000:
  - Error Message: **`Invalid ISO8601-2_Date format: 12881?`**
  - Causing raw value: `12881?`

- [ ] Error in Col: **Tod - Ort** and row with ID P0950000:
  - Error Message: **`LocationID must start with 'L': Niederoderwitz`**
  - Causing raw value: `Niederoderwitz`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0950000:
  - Error Message: **`Expected 4 parts, got 3: Pädagogium Niesky, 1893 Hilfslehrer in Herrnhut; 1897 Lehrer in Großhennersdorf; 1905 Lehrer inNiederoderwitz`**
  - Causing raw value: `Pädagogium Niesky, 1893 Hilfslehrer in Herrnhut; 1897 Lehrer in Großhennersdorf; 1905 Lehrer in
Niederoderwitz`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0950000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0960000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0960000:
  - Error Message: **`URL is not valid: nein (2024-12-03)`**
  - Causing raw value: `nein (2024-12-03)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P0960000:
  - Error Message: **`Invalid ISO8601-2_Date format: 205`**
  - Causing raw value: `205`

- [ ] Error in Col: **Geburt - Ort** and row with ID P0960000:
  - Error Message: **`LocationID must start with 'L': Großhennersdorf`**
  - Causing raw value: `Großhennersdorf`

- [ ] Error in Col: **Tod - Datum** and row with ID P0960000:
  - Error Message: **`Invalid ISO8601-2_Date format: 16502?`**
  - Causing raw value: `16502?`

- [ ] Error in Col: **Tod - Ort** and row with ID P0960000:
  - Error Message: **`LocationID must start with 'L': Heidenheim`**
  - Causing raw value: `Heidenheim`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0960000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0970000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0970000:
  - Error Message: **`URL is not valid: nein (2024-12-03)`**
  - Causing raw value: `nein (2024-12-03)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0970000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P0980000

- [ ] Error in Col: **Geburt - Ort** and row with ID P0980000:
  - Error Message: **`LocationID must start with 'L': Rudelstadt`**
  - Causing raw value: `Rudelstadt`

- [ ] Error in Col: **Tod - Ort** and row with ID P0980000:
  - Error Message: **`LocationID must start with 'L': Salem (Nordcarolina)`**
  - Causing raw value: `Salem (Nordcarolina)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0980000:
  - Error Message: **`Expected 4 parts, got 1: 1772- 1782 Gnadenberg Apothekerlehre (Schönhofer 2014, 190)`**
  - Causing raw value: `1772- 1782 Gnadenberg Apothekerlehre (Schönhofer 2014, 190) `
  - Full field: _1772- 1782 Gnadenberg Apothekerlehre (Schönhofer 2014, 190) |_

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P0980000:
  - Error Message: **`PersonID must start with 'P': Humphry Marshall`**
  - Causing raw value: `Humphry Marshall {M0040000} `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0980000:
  - Error Message: **`LiteratureID must start with 'R': "Kramsch compiled three floras of the Salem area, two in 1789 and one dated 1789–91 (Spencer 1997). These are held in the Moravian archives in Winston-Salem." Troyer 2009, 4`**
  - Causing raw value: `"Kramsch compiled three floras of the Salem area, two in 1789 and one dated 1789–91 (Spencer 1997). These are held in the Moravian archives in Winston-Salem." Troyer 2009, 4 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0980000:
  - Error Message: **`LiteratureID must start with 'R': "Kramsch produced for the Pennsylvania area a ‘‘Flora Nazarethiana’’ dated 1787–1788, to which Denke added a supplement dated 1797–1799 (Pennell1931; Phillips and Phillips 1963). These manuscript items are also at the Academy of Natural Sciences." Troyer 2009, 4`**
  - Causing raw value: `"Kramsch produced for the Pennsylvania area a ‘‘Flora Nazarethiana’’ dated 1787–1788, to which Denke added a supplement dated 1797–1799 (Pennell1931; Phillips and Phillips 1963). These manuscript items are also at the Academy of Natural Sciences." Troyer 2009, 4`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P0980000:
  - Error Message: **`LiteratureID must start with 'R': "Samuel Kramsch appears to have been the pioneer, and there has survived his manuscript "Flora Nazarethena spontanea collecta in annis 1787 et 1788", to which Christian Denke added a supplement in 1797." (Francis W. Pennell: "Botanical Collectors of the Philadelphia Local Area ", in: Bartonia 21 (1940-1941), S. 38-57, 40)`**
  - Causing raw value: `"Samuel Kramsch appears to have been the pioneer, and there has survived his manuscript "Flora Nazarethena spontanea collecta in annis 1787 et 1788", to which Christian Denke added a supplement in 1797." (Francis W. Pennell: "Botanical Collectors of the Philadelphia Local Area ", in: Bartonia 21 (1940-1941), S. 38-57, 40)`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P0980000:
  - Error Message: **`Invalid work id: https://www.ncpedia.org/biography/kramsch-samuel-gottlieb (should be R-ID, or M-ID)`**
  - Causing raw value: `https://www.ncpedia.org/biography/kramsch-samuel-gottlieb `
  - Full field: _https://www.ncpedia.org/biography/kramsch-samuel-gottlieb | R0000400 | R0013600_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0980000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 `
  - Full field: _Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 |
Troyer 2009 |
 Lehman (1902) |
Barnhart (1935) |
Powell (1988)_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0980000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009 `
  - Full field: _Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 |
Troyer 2009 |
 Lehman (1902) |
Barnhart (1935) |
Powell (1988)_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0980000:
  - Error Message: **`Invalid work id: Lehman (1902) (should be R-ID, or M-ID)`**
  - Causing raw value: ` Lehman (1902) `
  - Full field: _Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 |
Troyer 2009 |
 Lehman (1902) |
Barnhart (1935) |
Powell (1988)_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0980000:
  - Error Message: **`Invalid work id: Barnhart (1935) (should be R-ID, or M-ID)`**
  - Causing raw value: `Barnhart (1935) `
  - Full field: _Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 |
Troyer 2009 |
 Lehman (1902) |
Barnhart (1935) |
Powell (1988)_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0980000:
  - Error Message: **`Invalid work id: Powell (1988) (should be R-ID, or M-ID)`**
  - Causing raw value: `Powell (1988)`
  - Full field: _Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014 |
Troyer 2009 |
 Lehman (1902) |
Barnhart (1935) |
Powell (1988)_

### P0990000

- [ ] Error in Col: **Links - Bionomia** and row with ID P0990000:
  - Error Message: **`URL is not valid: https://de.bionomia.net/Q68239 (ist er das?)`**
  - Causing raw value: `https://de.bionomia.net/Q68239 (ist er das?)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P0990000:
  - Error Message: **`Expected 4 parts, got 1: Zeist, Leitung der dortigen Gemeine`**
  - Causing raw value: `Zeist, Leitung der dortigen Gemeine`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P0990000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P0990000:
  - Error Message: **`Invalid work id: David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79 (should be R-ID, or M-ID)`**
  - Causing raw value: `David Elliston Allen: Moravian Naturalist, in: E. Charles Nelson (Hg.), History & Mystery. Notes and queries from newsletter of The Society for the History of Natural History, London: Society for the History of Natural History 2011, S. 78-80, 79`

### P1000000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1000000:
  - Error Message: **`Cannot parse as date or period: '1830-1840'`**
  - Causing raw value: ` 1830-1840; L1110000 [Hebron]; ; Missionar {R0000600} `
  - Full field: _1826; L1100000; ; {R0007700} | 1830-1840; L1110000 [Hebron]; ; Missionar {R0000600} | 1843-1846; L0950000, L1600000; ; Missionar {R0007700} | 1847; L1200000; ; Missionar {R0007700}_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1000000:
  - Error Message: **`Cannot parse as date or period: '1843-1846'`**
  - Causing raw value: ` 1843-1846; L0950000, L1600000; ; Missionar {R0007700} `
  - Full field: _1826; L1100000; ; {R0007700} | 1830-1840; L1110000 [Hebron]; ; Missionar {R0000600} | 1843-1846; L0950000, L1600000; ; Missionar {R0007700} | 1847; L1200000; ; Missionar {R0007700}_

### P1010000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1010000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1010000:
  - Error Message: **`LocationID must start with 'L': Gottesberg-Rothenbach (Polen)`**
  - Causing raw value: `Gottesberg-Rothenbach (Polen)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1010000:
  - Error Message: **`LocationID must start with 'L': Dresden`**
  - Causing raw value: `Dresden`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1010000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1010000:
  - Error Message: **`Invalid work id: Volker Otte: "Exotische Flechten aus der Sammlungstätigkeit der Herrnhuter Brüdergemeine im Görlitzer Herbarium ", in: (Hg.), Sammelband zu Botanik in und um Görlitz und Herrnhuter zu einer Tagung von 2005, unveröffentlicht (should be R-ID, or M-ID)`**
  - Causing raw value: `Volker Otte: "Exotische Flechten aus der Sammlungstätigkeit der Herrnhuter Brüdergemeine im Görlitzer Herbarium ", in:  (Hg.), Sammelband zu Botanik in und um Görlitz und Herrnhuter zu einer Tagung von 2005, unveröffentlicht`

### P1020000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1020000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1020000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1020000:
  - Error Message: **`LiteratureID must start with 'R': Theodor Küster: Register Zur Flora von Herrnhut und Umgebung von Wilhelm Schultze. angefertigt von Theodor Küster. 1902, UA NB.VI. 63.n.2`**
  - Causing raw value: `Theodor Küster: Register Zur Flora von Herrnhut und Umgebung von Wilhelm Schultze. angefertigt von Theodor Küster. 1902, UA NB.VI. 63.n.2`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1020000:
  - Error Message: **`Invalid work id: UA NB.VI. 63.n.2 (should be R-ID, or M-ID)`**
  - Causing raw value: `UA NB.VI. 63.n.2`

### P1030000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1030000:
  - Error Message: **`LocationID must start with 'L': Neusalz, Oder`**
  - Causing raw value: `Neusalz, Oder`

- [ ] Error in Col: **Tod - Ort** and row with ID P1030000:
  - Error Message: **`LocationID must start with 'L': Neudietendorf`**
  - Causing raw value: `Neudietendorf`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1030000:
  - Error Message: **`Expected 4 parts, got 1: Niesky 1811-1814 (ousch, S. 312)`**
  - Causing raw value: `Niesky 1811-1814 (ousch, S. 312)`
  - Full field: _Niesky 1811-1814 (ousch, S. 312)|
Neudietendorf, Apotheker_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1030000:
  - Error Message: **`Expected 4 parts, got 1: Neudietendorf, Apotheker`**
  - Causing raw value: `Neudietendorf, Apotheker`
  - Full field: _Niesky 1811-1814 (ousch, S. 312)|
Neudietendorf, Apotheker_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1030000:
  - Error Message: **`Invalid work id: NEIN (should be R-ID, or M-ID)`**
  - Causing raw value: `NEIN`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1030000:
  - Error Message: **`LiteratureID must start with 'R': Christian Theodor Lappe: "Conchylien, welche bisher im Umkreis von Neudietendorf im Herzogtum Gotha und den angrenzenden Ländern Thüringens, besonders auf der nordwestlichen Hälfte des Thüringer Waldes gefunden wurden. - Nachrichtenblatt d. Malakozool. Ges., 103 - 106.", in: 3 (1871), S. 103-106`**
  - Causing raw value: `Christian Theodor Lappe: "Conchylien, welche bisher im Umkreis von Neudietendorf im Herzogtum Gotha und den angrenzenden Ländern Thüringens, besonders auf der nordwestlichen Hälfte des Thüringer Waldes gefunden wurden. - Nachrichtenblatt d. Malakozool. Ges., 103 - 106.", in:  3 (1871), S. 103-106 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1030000:
  - Error Message: **`LiteratureID must start with 'R': Christian Theodor Lappe: "Einige Versuche über die chemische Beschaffenheit des Causticum", in: Archiv für homöopathische Heilkunst 19 (1841), Nr. 2, S. 10-17.`**
  - Causing raw value: ` Christian Theodor Lappe: "Einige Versuche über die chemische Beschaffenheit des Causticum", in: Archiv für homöopathische Heilkunst 19 (1841), Nr. 2, S. 10-17.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1030000:
  - Error Message: **`Invalid work id: Werner Rothmaler: "Biographien alter thüringischer Floristen", in: Mitteilungen des Thüringischen Botanischen Vereins, Neue Folge, 1933, S. 46-60. (should be R-ID, or M-ID)`**
  - Causing raw value: `Werner Rothmaler: "Biographien alter thüringischer Floristen", in: Mitteilungen des Thüringischen Botanischen Vereins, Neue Folge, 1933, S. 46-60. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1030000:
  - Error Message: **`Invalid work id: Thomas Gregor: "Galeopsis ladanum in Deutschland. Eine oft verkannte Sippe - oder: Wie gut sind unsere floristischen Kartierungen?", in: Tuexenia 25 (2005), S. 285-305, 302 (should be R-ID, or M-ID)`**
  - Causing raw value: ` Thomas Gregor: "Galeopsis ladanum in Deutschland. Eine oft verkannte Sippe - oder: Wie gut sind unsere floristischen Kartierungen?", in: Tuexenia 25 (2005), S. 285-305, 302 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1030000:
  - Error Message: **`Invalid work id: Reinhard Wylegalla: "Von der "Magenmedizin" zum "Aromatique" ", in: Deutsche ApothekerZeitung 44 (2008) (should be R-ID, or M-ID)`**
  - Causing raw value: ` Reinhard Wylegalla: "Von der "Magenmedizin" zum "Aromatique" ", in: Deutsche ApothekerZeitung 44 (2008) `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1030000:
  - Error Message: **`Invalid work id: Art.: Lappe, Christian Theodor: Jürgen Pusch; Klaus-Jörg Barthel; Wolfgang Heinrich (Hg.): Die Botaniker Thüringens, 2015 (Haussknechtia, Beiheft 18), 312-313 (mit Schriftprobe)=. (should be R-ID, or M-ID)`**
  - Causing raw value: ` Art.: Lappe, Christian Theodor: Jürgen Pusch; Klaus-Jörg Barthel; Wolfgang Heinrich (Hg.): Die Botaniker Thüringens,  2015 (Haussknechtia, Beiheft 18), 312-313 (mit Schriftprobe)=. `

### P1034000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1034000:
  - Error Message: **`Expected 4 parts, got 1: Suriname`**
  - Causing raw value: `Suriname`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P1034000:
  - Error Message: **`CollectionID must start with 'C': https://ans-images.ansp.org/botany/PH2/Fullsize/00591/PH00591404.jpg`**
  - Causing raw value: `https://ans-images.ansp.org/botany/PH2/Fullsize/00591/PH00591404.jpg`

### P1035000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1035000:
  - Error Message: **`Expected 4 parts, got 1: Surinam -- Missionar`**
  - Causing raw value: `Surinam -- Missionar {R0003600}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1035000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1036000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1036000:
  - Error Message: **`Expected 4 parts, got 1: EnglandAustralien`**
  - Causing raw value: `England
Australien`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1036000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1036000:
  - Error Message: **`PersonID must start with 'P': Steinhauer, H.`**
  - Causing raw value: `Steinhauer, H. `
  - Full field: _Steinhauer, H. |
Christian Ignatius Latrobe (Vater)_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1036000:
  - Error Message: **`PersonID must start with 'P': Christian Ignatius Latrobe (Vater)`**
  - Causing raw value: `Christian Ignatius Latrobe (Vater)`
  - Full field: _Steinhauer, H. |
Christian Ignatius Latrobe (Vater)_

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1036000:
  - Error Message: **`Invalid format for PersonID: Pastor Samuel Studer (Helen Bothman: "C J La Trobe: Jolimont Plantsman", in: LA TROBEANA 21 (2022), Nr. 1, S. 6-18, 7)`**
  - Causing raw value: `Pastor Samuel Studer (Helen Bothman: "C J La Trobe: Jolimont Plantsman", in: LA TROBEANA 21 (2022), Nr. 1, S. 6-18, 7)`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P1036000:
  - Error Message: **`CollectionID must start with 'C': https://www.latrobesociety.org.au/specimens`**
  - Causing raw value: `  https://www.latrobesociety.org.au/specimens`
  - Full field: _C-G {https://collections.geneve.ch/jardinbotaniquegeneve/herbier/adetail.php?id=232360} |  https://www.latrobesociety.org.au/specimens_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1036000:
  - Error Message: **`LiteratureID must start with 'R': Charles Joseph Latrobe: The Pedestrian: a summer’s ramble in the Tyrol and some of the adjacent provinces, 1830, London: R. B. Seeley & W. Burnside, 1832`**
  - Causing raw value: `Charles Joseph Latrobe: The Pedestrian: a summer’s ramble in the Tyrol and some of the adjacent provinces, 1830, London: R. B. Seeley & W. Burnside, 1832 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1036000:
  - Error Message: **`LiteratureID must start with 'R': Charles Joseph Latrobe: The Alpenstock: Or, Sketches of Swiss scenery and manners, 1825-1826, London: R. B. Seeley & W. Burnside 1829 (384-387: "Flora of the Chain of the Stockhorn. Canton of Berne";387-388: "Additional Flora of the opposite Chain of the Thurnen")`**
  - Causing raw value: `Charles Joseph Latrobe: The Alpenstock: Or, Sketches of Swiss scenery and manners, 1825-1826, London: R. B. Seeley & W. Burnside 1829 (384-387: "Flora of the Chain of the Stockhorn. Canton of Berne";
387-388: "Additional Flora of the opposite Chain of the Thurnen")`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1036000:
  - Error Message: **`Invalid work id: Helen Bothman: "C J La Trobe: Jolimont Plantsman", in: LA TROBEANA 21 (2022), Nr. 1, S. 6-18. (should be R-ID, or M-ID)`**
  - Causing raw value: `Helen Bothman: "C J La Trobe: Jolimont Plantsman", in: LA TROBEANA 21 (2022), Nr. 1, S. 6-18.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1036000:
  - Error Message: **`Invalid work id: Corinna Erckenbrecht: "German Moravian missionaries on western Cape York Peninsula and their perception of the local Aboriginal people and languages", in: Nicolas Peterson; Anna Kenny (Hg.), GERMAN ETHNOGRAPHY IN AUSTRALIA, Canberra, Australia: Australian National University Press (ANU) 2017, S. 137-165. (should be R-ID, or M-ID)`**
  - Causing raw value: `Corinna Erckenbrecht: "German Moravian missionaries on western Cape York Peninsula and their perception of the local Aboriginal people and languages", in: Nicolas Peterson; Anna Kenny (Hg.), GERMAN ETHNOGRAPHY IN AUSTRALIA, Canberra, Australia: Australian National University Press (ANU) 2017, S. 137-165.`

### P1036500

- [ ] Error in Col: **Wirkungsorte** and row with ID P1036500:
  - Error Message: **`Expected 4 parts, got 1: LondonSüdafrika (Visitation)`**
  - Causing raw value: `London
Südafrika (Visitation)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1036500:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1036500:
  - Error Message: **`PersonID must start with 'P': Hänsel, Johann Gottfried`**
  - Causing raw value: `Hänsel, Johann Gottfried `
  - Full field: _Hänsel, Johann Gottfried |_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1036500:
  - Error Message: **`LiteratureID must start with 'R': Christian Ignatius Latrobe: Des Evangelischen Predigers C. I. Latrobe Tagebuch einer Besuch-Reise nach Süd-Afrika in den Jahren 1815 und 1816 : nebst einigen Nachrichten von den zur Mission der Brüder-Gemeine gehörigen Niederlassungen am Vorgebirge der guten Hoffnung ; Mit einem Titelkupfer / Aus dem Englischen übersetzt, für Deutsche Leser bearbeitet und mit einigen Anmerkungen versehen von Friedrich Hesse, evang. Prediger, hg. v. Hesse, Friedrich, Halle ; Berlin: Buchhandlung des Hallischen Waisenhauses 1820 (S. 319-336: "Anhang. Systematische Benennungen einiger in diesem Tagebuche erwähnten Capischen Thiere und Pflanzen, nebst kurzen zur Naturgeschichte derselben gehörigen Bemerkungen"; S. 337-353: "Von der Verpflanzung Europäischer und sndrer ausländischen Gewächse, nach dem Vorgebierge der guten Hoffnung in Süd=Afrika").`**
  - Causing raw value: `Christian Ignatius Latrobe: [Tagebuch einer Besuchs-Reise nach Süd-Afrika in den Jahren 1815 und 1816] Des Evangelischen Predigers C. I. Latrobe Tagebuch einer Besuch-Reise nach Süd-Afrika in den Jahren 1815 und 1816 : nebst einigen Nachrichten von den zur Mission der Brüder-Gemeine gehörigen Niederlassungen am Vorgebirge der guten Hoffnung ; Mit einem Titelkupfer / Aus dem Englischen übersetzt, für Deutsche Leser bearbeitet und mit einigen Anmerkungen versehen von Friedrich Hesse, evang. Prediger, hg. v. Hesse, Friedrich, Halle ; Berlin: Buchhandlung des Hallischen Waisenhauses 1820 (S. 319-336: "Anhang. Systematische Benennungen einiger in diesem Tagebuche erwähnten Capischen Thiere und Pflanzen, nebst kurzen zur Naturgeschichte derselben gehörigen Bemerkungen"; S. 337-353: "Von der Verpflanzung Europäischer und sndrer ausländischen Gewächse, nach dem Vorgebierge der guten Hoffnung in Süd=Afrika"). `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1036500:
  - Error Message: **`LiteratureID must start with 'R': Johann Gottfried Hänsel: Letters on the Nicobar Islands, their natural Productions, and the Manners, Customs, and Superstitions of the Natives; With an Account of an Attempt made by the Church of the United Brethren, to convert them to Christianity. Admitted by the Rev. John Gottfried Haensel, (the only surviving Missionary) to the Rev. C. I. Latrobe, hg. v. Latrobe, Christian Ignatius, London: PRINTED FOR THE EDITOR, NO. 10, NEVIL'S COURT, FETTER LANE, BY W. M'DOWALL, PEMBERTON ROW 1812.`**
  - Causing raw value: `Johann Gottfried Hänsel: Letters on the Nicobar Islands, their natural Productions, and the Manners, Customs, and Superstitions of the Natives; With an Account of an Attempt made by the Church of the United Brethren, to convert them to Christianity. Admitted by the Rev. John Gottfried Haensel, (the only surviving Missionary) to the Rev. C. I. Latrobe, hg. v. Latrobe, Christian Ignatius, London: PRINTED FOR THE EDITOR, NO. 10, NEVIL'S COURT, FETTER LANE, BY W. M'DOWALL, PEMBERTON ROW 1812. `

### P1040000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1040000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1040000:
  - Error Message: **`Expected 4 parts, got 1: Barby -- Verleger`**
  - Causing raw value: `Barby -- Verleger`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1040000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1044000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1044000:
  - Error Message: **`Expected 4 parts, got 5: 1864-1916; L2270000; Salem Academy; Lehrerin;`**
  - Causing raw value: `1864-1916; L2270000; Salem Academy; Lehrerin; {M0043000} `
  - Full field: _1864-1916; L2270000; Salem Academy; Lehrerin; {M0043000} | 1916-1922;  L2270000;; {M0043000} _

- [ ] Error in Col: **Wirkungsorte** and row with ID P1044000:
  - Error Message: **`Cannot parse as date or period: '1916-1922'`**
  - Causing raw value: ` 1916-1922;  L2270000;; {M0043000} `
  - Full field: _1864-1916; L2270000; Salem Academy; Lehrerin; {M0043000} | 1916-1922;  L2270000;; {M0043000} _

### P1045000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1045000:
  - Error Message: **`Expected 4 parts, got 1: Elim (Südafrika) -- Missionar`**
  - Causing raw value: `Elim (Südafrika)  -- Missionar {R0003600}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1045000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1050000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1050000:
  - Error Message: **`LocationID must start with 'L': New Herrnhut. on the island of StThomas, Danish West Indies (now U .S. Virgin Islands).`**
  - Causing raw value: `New Herrnhut. on the island of St
Thomas, Danish West Indies (now U .S. Virgin Islands).`

- [ ] Error in Col: **Tod - Ort** and row with ID P1050000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1050000:
  - Error Message: **`Expected 4 parts, got 1: Labrador`**
  - Causing raw value: `Labrador`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1050000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1050000:
  - Error Message: **`Invalid work id: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 (should be R-ID, or M-ID)`**
  - Causing raw value: `Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1050000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222.`

### P1060000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1060000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1060000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1070000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1070000:
  - Error Message: **`LocationID must start with 'L': Gnadenfeld`**
  - Causing raw value: `Gnadenfeld`

- [ ] Error in Col: **Tod - Ort** and row with ID P1070000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1070000:
  - Error Message: **`Expected 4 parts, got 1: NieskyGnadenfrei bis 1884L1500000 bis 1887Nain 1888-1917ab 1889 Superintendet der LAbrador-Mission`**
  - Causing raw value: `Niesky
Gnadenfrei bis 1884
L1500000 bis 1887
Nain 1888-1917
ab 1889 Superintendet der LAbrador-Mission`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1070000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1080000

- [ ] Error in Col: **Tod - Ort** and row with ID P1080000:
  - Error Message: **`LocationID must start with 'L': Stuttgard`**
  - Causing raw value: `Stuttgard`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1080000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1090000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1090000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1090000:
  - Error Message: **`Invalid format for LocationID: Leh`**
  - Causing raw value: `Leh`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1090000:
  - Error Message: **`Expected 4 parts, got 1: Leh, Missionskrankenhaus`**
  - Causing raw value: `Leh, Missionskrankenhaus`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1090000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1095000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1095000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1095000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1100000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1100000:
  - Error Message: **`LocationID must start with 'L': Oberhem`**
  - Causing raw value: `Oberhem {R0009000}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1100000:
  - Error Message: **`Expected 4 parts, got 1: Suriname`**
  - Causing raw value: `Suriname`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1100000:
  - Error Message: **`LiteratureID must start with 'R': Be r i c h t des Bruders Menze von seinen Besuchenauf den Plantagen an der Suriname im Jahr 1856 https://collections.mun.ca/digital/collection/nachrichten/id/69517/rec/2`**
  - Causing raw value: `Be r i c h t des Bruders Menze von seinen Besuchen
auf den Plantagen an der Suriname im Jahr 1856 https://collections.mun.ca/digital/collection/nachrichten/id/69517/rec/2`

### P1110000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1110000:
  - Error Message: **`Expected 4 parts, got 1: Gnadenfeld`**
  - Causing raw value: `Gnadenfeld {R0009800}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1110000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1120000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1120000:
  - Error Message: **`URL is not valid: nein (2025-06-19)`**
  - Causing raw value: `nein (2025-06-19)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1120000:
  - Error Message: **`Invalid Reference Document value: Pringle 1991 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Labrador {Pringle 1991}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1120000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1130000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1130000:
  - Error Message: **`Expected 4 parts, got 1: 1869, Sep. Gnadenfeld`**
  - Causing raw value: `1869, Sep. Gnadenfeld`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1130000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1140000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1140000:
  - Error Message: **`URL is not valid: nein (2024-12-06)`**
  - Causing raw value: `nein (2024-12-06)`

- [ ] Error in Col: **Geburt - Datum** and row with ID P1140000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1797-03-15(1792-11-19)`**
  - Causing raw value: `1797-03-15
(1792-11-19)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1140000:
  - Error Message: **`LocationID must start with 'L': Basel`**
  - Causing raw value: `Basel`

- [ ] Error in Col: **Tod - Datum** and row with ID P1140000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1871-10-25(1856-01-07)`**
  - Causing raw value: `1871-10-25
(1856-01-07)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1140000:
  - Error Message: **`LocationID must start with 'L': Basel(Potsdam)`**
  - Causing raw value: `Basel
(Potsdam)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1140000:
  - Error Message: **`Expected 4 parts, got 1: 1807 Pädagogium Barby, 1808 Pädagogium Niesky, 1811 Theologisches Seminar Niesky, 1813 Lehrer an der Knabenanstalt Neuwied/Rhein, 1821 Konferenzschreiber der Brüderunität in Berthelsdorf, 1827 Schulinspektor in Neuwied, 1845 Inspektor der Pensionsschule in Zeist (Holland), 1847 Amtsniederlegung wegen Krankheit, 1850 Prediger der Brüdergemeine in Bremen, 1855 dito in Potsdam.`**
  - Causing raw value: `1807 Pädagogium Barby, 1808 Pädagogium Niesky, 1811 Theologisches Seminar Niesky, 1813 Lehrer an der Knabenanstalt Neuwied/Rhein, 1821 Konferenzschreiber der Brüderunität in Berthelsdorf, 1827 Schulinspektor in Neuwied, 1845 Inspektor der Pensionsschule in Zeist (Holland), 1847 Amtsniederlegung wegen Krankheit, 1850 Prediger der Brüdergemeine in Bremen, 1855 dito in Potsdam.`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1140000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1140000:
  - Error Message: **`Invalid work id: Biographien sächsischer Botaniker Hardtke et al 2004 (should be R-ID, or M-ID)`**
  - Causing raw value: `Biographien sächsischer Botaniker Hardtke et al 2004`

### P1145000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1145000:
  - Error Message: **`LocationID must start with 'L': Genf`**
  - Causing raw value: `Genf {R0009800}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1145000:
  - Error Message: **`Expected 4 parts, got 3: Gnadenfeld ; Knabenanstalt; Lehrer`**
  - Causing raw value: `Gnadenfeld ; Knabenanstalt; Lehrer {R0009800} `
  - Full field: _Gnadenfeld ; Knabenanstalt; Lehrer {R0009800} |
Gnadenfeld; ; {R0009800}_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1145000:
  - Error Message: **`Expected 4 parts, got 3: Gnadenfeld; ;`**
  - Causing raw value: `Gnadenfeld; ; {R0009800}`
  - Full field: _Gnadenfeld ; Knabenanstalt; Lehrer {R0009800} |
Gnadenfeld; ; {R0009800}_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1145000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1145000:
  - Error Message: **`PersonID must start with 'P': Max Wetschky`**
  - Causing raw value: `Max Wetschky {R0009800} `
  - Full field: _Max Wetschky {R0009800} |
Wilhelm Kölbing {R0009800}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1145000:
  - Error Message: **`PersonID must start with 'P': Wilhelm Kölbing`**
  - Causing raw value: `Wilhelm Kölbing {R0009800}`
  - Full field: _Max Wetschky {R0009800} |
Wilhelm Kölbing {R0009800}_

### P1150000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1150000:
  - Error Message: **`LocationID must start with 'L': Gröditz bei Bautzen`**
  - Causing raw value: `Gröditz bei Bautzen {R0010000}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1150000:
  - Error Message: **`Expected 4 parts, got 3: 1850/1854;;`**
  - Causing raw value: ` 1850/1854;; {R0012000} `
  - Full field: _1832/1844; L1500000; Schuhmacherei; {R0012000} |1844/1849; L2260000; Missionsstation; Missionar {R0012000} | 1850/1854;; {R0012000} | 1857/1861; L0850000; Missionsstation; Missionar; | 1861/1869; L1101500; Missionsstation; Missionar {R0012000} | 1869/1875; L1500000;; {R0012000}_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1150000:
  - Error Message: **`Expected 4 parts, got 5: 1857/1861; L0850000; Missionsstation; Missionar;`**
  - Causing raw value: ` 1857/1861; L0850000; Missionsstation; Missionar; `
  - Full field: _1832/1844; L1500000; Schuhmacherei; {R0012000} |1844/1849; L2260000; Missionsstation; Missionar {R0012000} | 1850/1854;; {R0012000} | 1857/1861; L0850000; Missionsstation; Missionar; | 1861/1869; L1101500; Missionsstation; Missionar {R0012000} | 1869/1875; L1500000;; {R0012000}_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1150000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1150000:
  - Error Message: **`LiteratureID must start with 'R': 1855: Reiseerinnerungen - basierend auf seiner Teilnahme an der Entdeckung der Nord-West-Passage auf der „Investigator“`**
  - Causing raw value: `1855: Reiseerinnerungen  - basierend auf seiner Teilnahme an der Entdeckung der Nord-West-Passage auf der „Investigator“`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1150000:
  - Error Message: **`LiteratureID must start with 'R': Johann August Miertsching: Reise-Tagebuch des Missionars Joh. Aug. Miertsching, welcher als Dolmetscher die Nordpol-Expedition zur Auffindung Sir John Franklins auf dem Schiff Investigator begleitete. In den Jahren 1850 bis 1854, Gnadau 1855 (Tagebuch http://digital.slub-dresden.de/id496161938`**
  - Causing raw value: `Johann August Miertsching: Reise-Tagebuch des Missionars Joh. Aug. Miertsching, welcher als Dolmetscher die Nordpol-Expedition zur Auffindung Sir John Franklins auf dem Schiff Investigator begleitete. In den Jahren 1850 bis 1854, Gnadau 1855 (Tagebuch http://digital.slub-dresden.de/id496161938 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1150000:
  - Error Message: **`LiteratureID must start with 'R': Johann August Miertsching: Reisetagebuch der Nordpol-Expedition zur Aufsuchung Sir John Franklins, 2021.`**
  - Causing raw value: `Johann August Miertsching: Reisetagebuch der Nordpol-Expedition zur Aufsuchung Sir John Franklins,  2021.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1150000:
  - Error Message: **`Invalid work id: Mechthild Opel: "Miertsching und die „herrlichen Blümchen“", in: Trimaris, 2022.07.24 (should be R-ID, or M-ID)`**
  - Causing raw value: `Mechthild Opel: "Miertsching und die „herrlichen Blümchen“", in: Trimaris, 2022.07.24`
  - Full field: _Mechthild Opel: "Miertsching und die „herrlichen Blümchen“", in: Trimaris, 2022.07.24|
Mechthild Opel; Wolfgang Opel: Weil ich ein Inuk bin. Johann August Miertsching. Ein Lebensbild, Berlin: Lukas Verlag 2022.| R0002400_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1150000:
  - Error Message: **`Invalid work id: Mechthild Opel; Wolfgang Opel: Weil ich ein Inuk bin. Johann August Miertsching. Ein Lebensbild, Berlin: Lukas Verlag 2022. (should be R-ID, or M-ID)`**
  - Causing raw value: `Mechthild Opel; Wolfgang Opel: Weil ich ein Inuk bin. Johann August Miertsching. Ein Lebensbild, Berlin: Lukas Verlag 2022.`
  - Full field: _Mechthild Opel: "Miertsching und die „herrlichen Blümchen“", in: Trimaris, 2022.07.24|
Mechthild Opel; Wolfgang Opel: Weil ich ein Inuk bin. Johann August Miertsching. Ein Lebensbild, Berlin: Lukas Verlag 2022.| R0002400_

### P1170000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1170000:
  - Error Message: **`URL is not valid: ?`**
  - Causing raw value: `?`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1170000:
  - Error Message: **`Expected 4 parts, got 1: Surinam`**
  - Causing raw value: `Surinam`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1170000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1180000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1180000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P1180000:
  - Error Message: **`LocationID must start with 'L': Kronförstchen`**
  - Causing raw value: `Kronförstchen`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1180000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1180000:
  - Error Message: **`LiteratureID must start with 'R': Erstlingsarbeit mit 16 Jahren veröffentlichtgefolt von neuen Veröffentlichungen fastjedes folgende Jahr`**
  - Causing raw value: `Erstlingsarbeit mit 16 Jahren veröffentlicht
gefolt von neuen Veröffentlichungen fast
jedes folgende Jahr`

- [ ] Error in Col: **Wichtige Werke der Person ohne botanischen Kontext** and row with ID P1180000:
  - Error Message: **`Invalid work id: Liste in R0011500 (should be R-ID, or M-ID)`**
  - Causing raw value: `Liste in R0011500`

### P1190000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1190000:
  - Error Message: **`LocationID must start with 'L': Kronförstchen`**
  - Causing raw value: `Kronförstchen`

- [ ] Error in Col: **Tod - Datum** and row with ID P1190000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1945 (vermißt Ende Januar 1945 Kurische Nehrung)`**
  - Causing raw value: `1945 (vermißt Ende Januar 1945 Kurische Nehrung)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1190000:
  - Error Message: **`LocationID must start with 'L': Kurische Nehrung`**
  - Causing raw value: `Kurische Nehrung`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1190000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1190000:
  - Error Message: **`LiteratureID must start with 'R': wichtige Veröffentlichungensowohl zu Vögeln als auch Bienen`**
  - Causing raw value: `wichtige Veröffentlichungen
sowohl zu Vögeln als auch Bienen`

### P1200000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1200000:
  - Error Message: **`URL is not valid: nein (2024-12-10)`**
  - Causing raw value: `nein (2024-12-10)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1200000:
  - Error Message: **`Expected 4 parts, got 1: Labrador`**
  - Causing raw value: `Labrador`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1200000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1210000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1210000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P1210000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1210000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1220000

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1220000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1225000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1225000:
  - Error Message: **`URL is not valid: Nein (2026-02-03)`**
  - Causing raw value: `Nein (2026-02-03)`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1225000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1225000:
  - Error Message: **`LocationID must start with 'L': Zauchenthal (Mähren)`**
  - Causing raw value: `Zauchenthal (Mähren)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1225000:
  - Error Message: **`LocationID must start with 'L': Bethlehem (Pennsyslvania)`**
  - Causing raw value: `Bethlehem (Pennsyslvania)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1225000:
  - Error Message: **`Expected 4 parts, got 1: ZauchenthalKunevand 1704-1725Herrnhut 1725-1734Saint Croix 1734-1737HerrnhutPilgeruhNazareth (Pennsyslvania) 1740-1741Bethlehem (Pennsylvania) 1741-1758`**
  - Causing raw value: `Zauchenthal
Kunevand 1704-1725
Herrnhut 1725-1734
Saint Croix 1734-1737
Herrnhut
Pilgeruh
Nazareth (Pennsyslvania) 1740-1741
Bethlehem (Pennsylvania) 1741-1758`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1225000:
  - Error Message: **`Invalid work id: ja (should be R-ID, or M-ID)`**
  - Causing raw value: `ja {http://bdhp.moravian.edu/personal_papers/memoirs/dnitschmann/dnitschmann.html} `
  - Full field: _ja {http://bdhp.moravian.edu/personal_papers/memoirs/dnitschmann/dnitschmann.html} | R0013100_

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1225000:
  - Error Message: **`Invalid work id: Inventarium Herrschaftsgarten 1734 (should be R-ID, or M-ID)`**
  - Causing raw value: `Inventarium Herrschaftsgarten 1734 `
  - Full field: _Inventarium Herrschaftsgarten 1734 |
KIndermann 2018_

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1225000:
  - Error Message: **`Invalid work id: KIndermann 2018 (should be R-ID, or M-ID)`**
  - Causing raw value: `KIndermann 2018`
  - Full field: _Inventarium Herrschaftsgarten 1734 |
KIndermann 2018_

### P1230000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1230000:
  - Error Message: **`URL is not valid: nein (2024-12-10)`**
  - Causing raw value: `nein (2024-12-10)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1230000:
  - Error Message: **`Invalid format for LocationID: Lafferde`**
  - Causing raw value: `Lafferde`

- [ ] Error in Col: **Tod - Ort** and row with ID P1230000:
  - Error Message: **`LocationID must start with 'L': Ebersdorf`**
  - Causing raw value: `Ebersdorf`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1230000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1230000:
  - Error Message: **`LiteratureID must start with 'R': 1777: Monographie über Grönland`**
  - Causing raw value: `1777: Monographie über Grönland`

### P1240000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1240000:
  - Error Message: **`URL is not valid: nein (2024-12-10)`**
  - Causing raw value: `nein (2024-12-10)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1240000:
  - Error Message: **`LocationID must start with 'L': Marienborn`**
  - Causing raw value: `Marienborn`

- [ ] Error in Col: **Tod - Ort** and row with ID P1240000:
  - Error Message: **`LocationID must start with 'L': Schulpforte`**
  - Causing raw value: `Schulpforte`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1240000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1250000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1250000:
  - Error Message: **`URL is not valid: nein (2024-12-10)`**
  - Causing raw value: `nein (2024-12-10)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1250000:
  - Error Message: **`LocationID must start with 'L': Tschenkowitz (Böhmen)`**
  - Causing raw value: `Tschenkowitz (Böhmen)`

- [ ] Error in Col: **Tod - Datum** and row with ID P1250000:
  - Error Message: **`Invalid ISO8601-2_Date format: 16482?`**
  - Causing raw value: `16482?`

- [ ] Error in Col: **Tod - Ort** and row with ID P1250000:
  - Error Message: **`LocationID must start with 'L': Gnadenberg`**
  - Causing raw value: `Gnadenberg`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1250000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1250000:
  - Error Message: **`PersonID must start with 'P': Jäschke`**
  - Causing raw value: `Jäschke {https://www.gbif.org/occurrence/5281299343}`

### P1260000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1260000:
  - Error Message: **`LocationID must start with 'L': Malmesbury, Wiltshire, United Kingdom`**
  - Causing raw value: `Malmesbury, Wiltshire, United Kingdom`

- [ ] Error in Col: **Tod - Datum** and row with ID P1260000:
  - Error Message: **`Invalid ISO8601-2_Date format: 18337?`**
  - Causing raw value: `18337?`

- [ ] Error in Col: **Tod - Ort** and row with ID P1260000:
  - Error Message: **`LocationID must start with 'L': Malmsbury`**
  - Causing raw value: `Malmsbury`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1260000:
  - Error Message: **`Expected 4 parts, got 1: Hopedal`**
  - Causing raw value: `Hopedal`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1260000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1260000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. (should be R-ID, or M-ID)`**
  - Causing raw value: `James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222.`

### P1280000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1280000:
  - Error Message: **`URL is not valid: nein (2024-12-12)`**
  - Causing raw value: `nein (2024-12-12)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1280000:
  - Error Message: **`LocationID must start with 'L': Osu`**
  - Causing raw value: `Osu`

- [ ] Error in Col: **Tod - Datum** and row with ID P1280000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1769-?-?`**
  - Causing raw value: `1769-?-?`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1280000:
  - Error Message: **`Expected 4 parts, got 1: Westafrika`**
  - Causing raw value: `Westafrika`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1280000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1280000:
  - Error Message: **`PersonID must start with 'P': Johann Jakob Bossart`**
  - Causing raw value: `Johann Jakob Bossart {M0004200}`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1280000:
  - Error Message: **`ManuscriptID must start with 'M': 03.03.1762, UA, R.15.N.8.1.c, no. 22. 1762 Mart. 3. Prottens Nachricht von einigen mitgebrachtenu. übergebenen africanischen Sachen mit 20 Nummern, darunter Samen`**
  - Causing raw value: `03.03.1762, UA, R.15.N.8.1.c, no. 22. 1762 Mart. 3. Prottens Nachricht von einigen mitgebrachten
u. übergebenen africanischen Sachen mit 20 Nummern, darunter Samen`

### P1290000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1290000:
  - Error Message: **`Expected 4 parts, got 1: Suriname -- Missionar, Barby`**
  - Causing raw value: `Suriname -- Missionar, Barby`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1290000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1290000:
  - Error Message: **`LiteratureID must start with 'R': Quandt, Christlieb: Nachricht von Suriname und seinen Einwohnern sonderlich den Arawacken, Warauen und Karaiben, von den nüzlichsten Gewächsen und Thieren des Landes, den Geschäften der dortigen Missionarien der Brüderunität und der Sprache der Arawacken. Nebst einer Charte und zwey Kupfern., Görlitz: J. G. Burghart .`**
  - Causing raw value: `Quandt, Christlieb: Nachricht von Suriname und seinen Einwohnern sonderlich den Arawacken, Warauen und Karaiben, von den nüzlichsten Gewächsen und Thieren des Landes, den Geschäften der dortigen Missionarien der Brüderunität und der Sprache der Arawacken. Nebst einer Charte und zwey Kupfern., Görlitz: J. G. Burghart [1807]. `

### P1310000

- [ ] Error in Col: **Geburt - Datum** and row with ID P1310000:
  - Error Message: **`Invalid Reference Document value: Meier, Herrnhuter Beiträge zur Erforschung Ladakhs (1997), S. 182 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `1838 {Meier, Herrnhuter Beiträge zur Erforschung Ladakhs (1997), S. 182}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1310000:
  - Error Message: **`Expected 4 parts, got 1: Himalayamission`**
  - Causing raw value: `Himalayamission {R0003600}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1310000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1310000:
  - Error Message: **`LiteratureID must start with 'R': F. Redslob: "Die Himalaya-Landschaften Rupschu und Ladak / Reiseskizzen von Missionar F. Redslob", in: Mitteilungen der Geographischen Gesellschaft für Thüringen zu Jena 4 (1886), S. 1-8.`**
  - Causing raw value: `F. Redslob: "Die Himalaya-Landschaften Rupschu und Ladak / Reiseskizzen von Missionar F. Redslob", in: Mitteilungen der Geographischen Gesellschaft für Thüringen zu Jena 4 (1886), S. 1-8.`

### P1320000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: ab 1818 Niesky, Pädagogium Niesky`**
  - Causing raw value: `ab 1818 Niesky, Pädagogium Niesky `
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: theolog. Seminar Gnadenfeldt`**
  - Causing raw value: `theolog. Seminar Gnadenfeldt `
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: 1834 - 1857 Nordamerika`**
  - Causing raw value: `1834 - 1857 Nordamerika `
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement`**
  - Causing raw value: `ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement `
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: 1857 Visitation Karibik`**
  - Causing raw value: `1857 Visitation Karibik`
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: 1861 Visitation Labrador`**
  - Causing raw value: `1861 Visitation Labrador `
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: 1869 Bischof und Präses der Generalsynode`**
  - Causing raw value: `1869 Bischof und Präses der Generalsynode`
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1320000:
  - Error Message: **`Expected 4 parts, got 1: 1876 Visitation Labrador`**
  - Causing raw value: `1876 Visitation Labrador `
  - Full field: _ab 1818 Niesky, Pädagogium Niesky |
theolog. Seminar Gnadenfeldt |
1834 - 1857 Nordamerika |
ab 1857 Europa als Mitgliededer Unitäts-Aeltestenconferenz im Missionsdepartement |
1857 Visitation Karibik|
1861 Visitation Labrador |
1869 Bischof und Präses der Generalsynode|
1876 Visitation Labrador |_

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1320000:
  - Error Message: **`PersonID must start with 'P': Reinhold Gundermann`**
  - Causing raw value: `Reinhold Gundermann {R0008200} `
  - Full field: _Reinhold Gundermann {R0008200} |
Adolf Bastian {R0008300}_

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1320000:
  - Error Message: **`PersonID must start with 'P': Adolf Bastian`**
  - Causing raw value: `Adolf Bastian {R0008300}`
  - Full field: _Reinhold Gundermann {R0008200} |
Adolf Bastian {R0008300}_

### P1330000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1330000:
  - Error Message: **`Expected 4 parts, got 1: Beschäftigung mit Botanik in Gnadenfeld`**
  - Causing raw value: `Beschäftigung mit Botanik in Gnadenfeld`

### P1340000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1340000:
  - Error Message: **`Expected 4 parts, got 1: Pharmazeut in Herrnhut`**
  - Causing raw value: `Pharmazeut in Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1340000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1340000:
  - Error Message: **`Invalid work id: BARBER 1898 (Flora der Oberlausitz), 346 (should be R-ID, or M-ID)`**
  - Causing raw value: `BARBER 1898 (Flora der Oberlausitz), 346`

### P1350000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1350000:
  - Error Message: **`URL is not valid: nein (2024-12-12)`**
  - Causing raw value: `nein (2024-12-12)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1350000:
  - Error Message: **`LocationID must start with 'L': Steinbach (Odenwald) | L1900000`**
  - Causing raw value: `Steinbach (Odenwald) | L1900000 {M0027000}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1350000:
  - Error Message: **`Expected 4 parts, got 1: Nordamerika`**
  - Causing raw value: `Nordamerika`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1350000:
  - Error Message: **`ManuscriptID must start with 'M': Reuter, Philip Christian Gottlieb: Der UpLand Gartten, 1759, pen and ink on paper. Moravian Church Archives, Northern Province, Bethlehem 0239 (1759)`**
  - Causing raw value: `Reuter, Philip Christian Gottlieb: Der UpLand Gartten, 1759, pen and ink on paper. Moravian Church Archives, Northern Province, Bethlehem 0239 (1759)`
  - Full field: _Reuter, Philip Christian Gottlieb: Der UpLand Gartten, 1759, pen and ink on paper. Moravian Church Archives, Northern Province, Bethlehem 0239 (1759)|
Reuter, Philip Christian Gottlieb: Hortus Medicus, 1761. Moravian Archives, Winston-Salem, N.C., Sig. 1944 (1761)|,._

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1350000:
  - Error Message: **`ManuscriptID must start with 'M': Reuter, Philip Christian Gottlieb: Hortus Medicus, 1761. Moravian Archives, Winston-Salem, N.C., Sig. 1944 (1761)`**
  - Causing raw value: `Reuter, Philip Christian Gottlieb: Hortus Medicus, 1761. Moravian Archives, Winston-Salem, N.C., Sig. 1944 (1761)`
  - Full field: _Reuter, Philip Christian Gottlieb: Der UpLand Gartten, 1759, pen and ink on paper. Moravian Church Archives, Northern Province, Bethlehem 0239 (1759)|
Reuter, Philip Christian Gottlieb: Hortus Medicus, 1761. Moravian Archives, Winston-Salem, N.C., Sig. 1944 (1761)|,._

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1350000:
  - Error Message: **`ManuscriptID must start with 'M': ,.`**
  - Causing raw value: `,.`
  - Full field: _Reuter, Philip Christian Gottlieb: Der UpLand Gartten, 1759, pen and ink on paper. Moravian Church Archives, Northern Province, Bethlehem 0239 (1759)|
Reuter, Philip Christian Gottlieb: Hortus Medicus, 1761. Moravian Archives, Winston-Salem, N.C., Sig. 1944 (1761)|,._

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1350000:
  - Error Message: **`LiteratureID must start with 'R': zwischen 1759 und 1764 vier Pflanzenlisten; u.a.Liste aller in der Gegend "wildwachsendenBlumen und Sträucher, auch der in den Gärten gezogenen Pflanzen, aller Vögel, wilder Tiere und Schlangen“`**
  - Causing raw value: `zwischen 1759 und 1764 vier Pflanzenlisten; u.a.
Liste aller in der Gegend "wildwachsenden
Blumen und Sträucher, 
auch der in den Gärten gezogenen Pflanzen, aller Vögel, wilder Tiere und Schlangen“ `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1350000:
  - Error Message: **`LiteratureID must start with 'R': Bynum, Flora Ann L.; Reuter, Philip Christian Gottlieb: Cultivated plants of the Wachovia tract in North Carolina, 1759-1764 : Christian Gottlieb Reuter's lists of plants grown at Bethabara, in the vegetable garden, the medical garden, and in the fields, Winston-Salem, N.C.: 1979.`**
  - Causing raw value: ` 
Bynum, Flora Ann L.; Reuter, Philip Christian Gottlieb: Cultivated plants of the Wachovia tract in North Carolina, 1759-1764 : Christian Gottlieb Reuter's lists of plants grown at Bethabara, in the vegetable garden, the medical garden, and in the fields, Winston-Salem, N.C.: [Old Salem, Inc.] 1979. `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1350000:
  - Error Message: **`Invalid format for LiteratureID: Reuter, Philip Christian Gottlieb: "1764 . WACHAU OR DOBBS PARISH [transl. aus dem deutschen)", in: Fries, Adelaide L. (Hg.), RECORDS OF THE MORAVIANS IN NORTH CAROLINA Volume II 1752-1775, RALEIGH EDWARDS & BROUGHTON PRINTING COMPANY STATE PRINTER 1925, S. 557-588.`**
  - Causing raw value: ` Reuter, Philip Christian Gottlieb: "1764 . WACHAU OR DOBBS PARISH [transl. aus dem deutschen)", in: Fries, Adelaide L. (Hg.), RECORDS OF THE MORAVIANS IN NORTH CAROLINA Volume II 1752-1775, RALEIGH EDWARDS & BROUGHTON PRINTING COMPANY STATE PRINTER 1925, S. 557-588.`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1350000:
  - Error Message: **`Invalid work id: Flora Ann L. Bynum; Philip Christian Gottlieb Reuter: Cultivated plants of the Wachovia tract in North Carolina, 1759-1764 : Christian Gottlieb Reuter's lists of plants grown at Bethabara, in the vegetable garden, the medical garden, and in the fields, Winston-Salem, N.C.: 1979 (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Flora Ann L. Bynum; Philip Christian Gottlieb Reuter: Cultivated plants of the Wachovia tract in North Carolina, 1759-1764 : Christian Gottlieb Reuter's lists of plants grown at Bethabara, in the vegetable garden, the medical garden, and in the fields, Winston-Salem, N.C.: [Old Salem, Inc.] 1979`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1350000:
  - Error Message: **`Invalid work id: Flora Ann L. Bynum; Philip Christian Gottlieb Reuter: "Appandix 7: Late Eighteenth Century Plan List 1979].", in: , Cultural Lanscape Report. National park service, Thomas Stone national historic site, , S. 135-140. (should be R-ID, or M-ID)`**
  - Causing raw value: `Flora Ann L. Bynum; Philip Christian Gottlieb Reuter: "Appandix 7: Late Eighteenth Century Plan List [Reuter, Philip Christian Gottlieb: Cultivated plants of the Wachovia tract in North Carolina, 1759-1764 : Christian Gottlieb Reuter's lists of plants grown at Bethabara, in the vegetable garden, the medical garden, and in the fields, hg. v. Bynum, Flora Ann L., Winston-Salem, N.C.: [Old Salem, Inc.] 1979].", in: , Cultural Lanscape Report. National park service, Thomas Stone national historic site, , S. 135-140. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1350000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009 `
  - Full field: _Troyer 2009 |
Becker Pflege, S. 26 |
Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 155._

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1350000:
  - Error Message: **`Invalid work id: Becker Pflege, S. 26 (should be R-ID, or M-ID)`**
  - Causing raw value: `Becker Pflege, S. 26 `
  - Full field: _Troyer 2009 |
Becker Pflege, S. 26 |
Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 155._

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1350000:
  - Error Message: **`Invalid work id: Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 155. (should be R-ID, or M-ID)`**
  - Causing raw value: `Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 155.`
  - Full field: _Troyer 2009 |
Becker Pflege, S. 26 |
Matthias Schönhofer: Letters from an American Botanist: The Correspondences of Gotthilf Heinrich Ernst Mühlenberg (1753–1815), Stuttgart: Frank Steiner 2014, 155._

### P1355000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1355000:
  - Error Message: **`Expected 4 parts, got 2: 1842-1873; Labrador`**
  - Causing raw value: `1842-1873; Labrador`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1355000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Datenbanknachweis)** and row with ID P1355000:
  - Error Message: **`CollectionID must start with 'C': GLM?`**
  - Causing raw value: `GLM?`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen - Anmerkungen** and row with ID P1355000:
  - Error Message: **`Invalid Reference Document value: https://data.biodiversitydata.nl/naturalis/specimen/L.1859326?}; Saxifraga cernua {https://data.biodiversitydata.nl/naturalis/specimen/L.1885330?} and S. rivularis at Nain (Engler & Irmscher, 1919) {R0000700 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `collected Cardamine bellidifolia (Schulz, 1903) {https://data.biodiversitydata.nl/naturalis/specimen/L.1859326?}; Saxifraga cernua {https://data.biodiversitydata.nl/naturalis/specimen/L.1885330?} and S. rivularis at Nain (Engler &  Irmscher, 1919) {R0000700}`

### P1355500

- [ ] Error in Col: **Wirkungsorte** and row with ID P1355500:
  - Error Message: **`Expected 4 parts, got 1: Himalaya --`**
  - Causing raw value: `Himalaya -- {R0003600}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1355500:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1360000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1360000:
  - Error Message: **`URL is not valid: nein (2024-12-12)`**
  - Causing raw value: `nein (2024-12-12)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1360000:
  - Error Message: **`LocationID must start with 'L': Champfleuri Lausanne`**
  - Causing raw value: `Champfleuri Lausanne`

- [ ] Error in Col: **Tod - Datum** and row with ID P1360000:
  - Error Message: **`Invalid ISO8601-2_Date format: 14807?`**
  - Causing raw value: `14807?`

- [ ] Error in Col: **Tod - Ort** and row with ID P1360000:
  - Error Message: **`LocationID must start with 'L': Fionnay Valais`**
  - Causing raw value: `Fionnay Valais`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1360000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1370000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1370000:
  - Error Message: **`URL is not valid: nein (2024-12-12)`**
  - Causing raw value: `nein (2024-12-12)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1370000:
  - Error Message: **`Expected 4 parts, got 1: 1836-1838 Studium Seminar Gnadenfeld`**
  - Causing raw value: `1836-1838 Studium Seminar Gnadenfeld `
  - Full field: _1836-1838 Studium Seminar Gnadenfeld | 1839-46 Lehrer in Christiansfeld_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1370000:
  - Error Message: **`Expected 4 parts, got 1: 1839-46 Lehrer in Christiansfeld`**
  - Causing raw value: ` 1839-46 Lehrer in Christiansfeld`
  - Full field: _1836-1838 Studium Seminar Gnadenfeld | 1839-46 Lehrer in Christiansfeld_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1370000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1370000:
  - Error Message: **`Invalid work id: Richard Träger: "Ein Herbarium von Pflanzen aus Labrador", in: ders., "Trägermappe" Naturwissenschaft in der Brüdergemeine (Botanik, Ornithologie, Medizin) (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Ein Herbarium von Pflanzen aus Labrador", in: ders., "Trägermappe" Naturwissenschaft in der Brüdergemeine (Botanik, Ornithologie, Medizin) [UA. IV/612]`

### P1380000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1380000:
  - Error Message: **`URL is not valid: nein (2024-12-15)`**
  - Causing raw value: `nein (2024-12-15)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1380000:
  - Error Message: **`LocationID must start with 'L': Neu-Zdany (Polen)`**
  - Causing raw value: `Neu-Zdany (Polen)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1380000:
  - Error Message: **`LocationID must start with 'L': Cairo (Ägypten)`**
  - Causing raw value: `Cairo (Ägypten)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1380000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1390000

- [ ] Error in Col: **Geburt - Datum** and row with ID P1390000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1819-4-12`**
  - Causing raw value: `1819-4-12`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1390000:
  - Error Message: **`LocationID must start with 'L': Stuttgart`**
  - Causing raw value: `Stuttgart`

- [ ] Error in Col: **Tod - Ort** and row with ID P1390000:
  - Error Message: **`LocationID must start with 'L': Stuttgart`**
  - Causing raw value: `Stuttgart `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1390000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1390000:
  - Error Message: **`Invalid format for PersonID: P0090000 ("In 1855, having decided to become a missionary, he gave up collecting and entrusted his specimens to Rudolph Roser, who eventually took them to Germany.")`**
  - Causing raw value: ` P0090000 ("In 1855, having decided to become a missionary, he [Leopold Richard Baur] gave up collecting and entrusted his specimens to Rudolph Roser, who eventually took them to Germany.") {https://plants.jstor.org/stable/10.5555/al.ap.person.bm000031005}`
  - Full field: _P0910000 | P0090000 ("In 1855, having decided to become a missionary, he [Leopold Richard Baur] gave up collecting and entrusted his specimens to Rudolph Roser, who eventually took them to Germany.") {https://plants.jstor.org/stable/10.5555/al.ap.person.bm000031005}_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1390000:
  - Error Message: **`LiteratureID must start with 'R': https://www.s2a3.org.za/bio/Biograph_final.php?serial=2398`**
  - Causing raw value: `https://www.s2a3.org.za/bio/Biograph_final.php?serial=2398`
  - Full field: _R0003700 |
https://www.s2a3.org.za/bio/Biograph_final.php?serial=2398_

### P1400000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1400000:
  - Error Message: **`URL is not valid: anlegen, wenn wikidata`**
  - Causing raw value: `anlegen, wenn wikidata`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1400000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Tod - Datum** and row with ID P1400000:
  - Error Message: **`Invalid ISO8601-2_Date format: nach 1891`**
  - Causing raw value: `nach 1891`

- [ ] Error in Col: **Tod - Ort** and row with ID P1400000:
  - Error Message: **`LocationID must start with 'L': Sarepta?`**
  - Causing raw value: `Sarepta?`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1400000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P1400000:
  - Error Message: **`CollectionID must start with 'C': https://www.gbif.org/occurrence/2250584142 ?`**
  - Causing raw value: `https://www.gbif.org/occurrence/2250584142 ?`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1400000:
  - Error Message: **`Invalid work id: Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" , Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" [UA. IV/612], Herrnhut: Archiv der Herrnhuter Brüdergemeine. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1400000:
  - Error Message: **`Invalid work id: Wilhelm Blasius: "Ellobius Tancréì nov. sp., ein neuer Moll-Lemming oder Wurfmoll aus dem Altai-Gebiete.", in: Zoologischer Anzeiger VII. Jahrgang (1884), Nr. 164, S. 197-201.als Ornithologe Ludwig Gebhardt: Die Ornithologen Mitteleuropas Haut und Ergänzungsband, Gießen: Brühl 1964, (should be R-ID, or M-ID)`**
  - Causing raw value: `Wilhelm Blasius: "Ellobius Tancréì nov. sp., ein neuer Moll-Lemming oder Wurfmoll aus dem Altai-Gebiete.", in: Zoologischer Anzeiger VII. Jahrgang (1884), Nr. 164, S. 197-201.
als Ornithologe Ludwig Gebhardt: Die Ornithologen Mitteleuropas Haut und Ergänzungsband, Gießen: Brühl 1964, `

### P1410000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1410000:
  - Error Message: **`URL is not valid: anlegen, wenn wikidata`**
  - Causing raw value: `anlegen, wenn wikidata`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1410000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1410000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1410000:
  - Error Message: **`Invalid work id: Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" , Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" [UA. IV/612], Herrnhut: Archiv der Herrnhuter Brüdergemeine.`

### P1420000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1420000:
  - Error Message: **`URL is not valid: anlegen, wenn wikidata`**
  - Causing raw value: `anlegen, wenn wikidata`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1420000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1420000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1420000:
  - Error Message: **`Invalid work id: Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" , Herrnhut: Archiv der Herrnhuter Brüdergemeine. (should be R-ID, or M-ID)`**
  - Causing raw value: `Richard Träger: "Notizen über den Sareptaner Naturalien-Sammler Rückbeil", in: ders., "Trägermappe" [UA. IV/612], Herrnhut: Archiv der Herrnhuter Brüdergemeine.`

### P1430000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1430000:
  - Error Message: **`URL is not valid: nein (2024-12-15)`**
  - Causing raw value: `nein (2024-12-15)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1430000:
  - Error Message: **`LocationID must start with 'L': Breslau`**
  - Causing raw value: `Breslau`

- [ ] Error in Col: **Tod - Ort** and row with ID P1430000:
  - Error Message: **`LocationID must start with 'L': Berlin`**
  - Causing raw value: `Berlin`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1430000:
  - Error Message: **`Expected 4 parts, got 1: Barby, Pädagogium -- Bildung -- (Meyer 1905)`**
  - Causing raw value: `Barby, Pädagogium -- Bildung -- (Meyer 1905) `
  - Full field: _Barby, Pädagogium -- Bildung -- (Meyer 1905) | Halle -- Professur (Theologie) -- 1804-1807 | Berlin -- Professur (Theologie) -- 1810-1834_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1430000:
  - Error Message: **`Expected 4 parts, got 1: Halle -- Professur (Theologie) -- 1804-1807`**
  - Causing raw value: ` Halle -- Professur (Theologie) -- 1804-1807 `
  - Full field: _Barby, Pädagogium -- Bildung -- (Meyer 1905) | Halle -- Professur (Theologie) -- 1804-1807 | Berlin -- Professur (Theologie) -- 1810-1834_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1430000:
  - Error Message: **`Expected 4 parts, got 1: Berlin -- Professur (Theologie) -- 1810-1834`**
  - Causing raw value: ` Berlin -- Professur (Theologie) -- 1810-1834`
  - Full field: _Barby, Pädagogium -- Bildung -- (Meyer 1905) | Halle -- Professur (Theologie) -- 1804-1807 | Berlin -- Professur (Theologie) -- 1810-1834_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1430000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1440000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1440000:
  - Error Message: **`URL is not valid: nein`**
  - Causing raw value: `nein`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1440000:
  - Error Message: **`Expected 4 parts, got 1: c. 1765 in Labrador`**
  - Causing raw value: `c. 1765 in Labrador`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1440000:
  - Error Message: **`PersonID must start with 'P': Bossart (Siehe email Rollmann vom 2.6.2026 an Sarah)`**
  - Causing raw value: `Bossart (Siehe email Rollmann vom 2.6.2026 an Sarah) `
  - Full field: _Bossart (Siehe email Rollmann vom 2.6.2026 an Sarah) |
Banks_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1440000:
  - Error Message: **`PersonID must start with 'P': Banks`**
  - Causing raw value: `Banks`
  - Full field: _Bossart (Siehe email Rollmann vom 2.6.2026 an Sarah) |
Banks_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1440000:
  - Error Message: **`Invalid work id: Kurzbio in: Thea Olsthoorn: Die Erkundungsreisen der Herrnhuter Missionare nach Labrador (1752-1770). Kommunikation mit Menschen einer nicht-schriftlichen Kultur, Hildesheim 2010. (should be R-ID, or M-ID)`**
  - Causing raw value: `Kurzbio in: Thea Olsthoorn: Die Erkundungsreisen der Herrnhuter Missionare nach Labrador (1752-1770). Kommunikation mit Menschen einer nicht-schriftlichen Kultur, Hildesheim 2010. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1440000:
  - Error Message: **`Invalid work id: zur Botanik: Averil M. Lysaght: Joseph Banks in Newfoundland and Labrador, 1766: His Diary, Manuscripts and Collections, Berkeley and Los Angeles: Univ. of California Press 1971 (should be R-ID, or M-ID)`**
  - Causing raw value: `zur Botanik: Averil M. Lysaght: Joseph Banks in Newfoundland and Labrador, 1766: His Diary, Manuscripts and Collections, Berkeley and Los Angeles: Univ. of California Press 1971`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1440000:
  - Error Message: **`Invalid work id: zu Botanik: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. zur Botanik: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180 (should be R-ID, or M-ID)`**
  - Causing raw value: `zu Botanik: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. 
zur Botanik: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180`

### P1450000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1450000:
  - Error Message: **`URL is not valid: nein (2024-12-15)`**
  - Causing raw value: `nein (2024-12-15)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1450000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1460000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1460000:
  - Error Message: **`Expected 4 parts, got 1: Herrnhut Schullehrer`**
  - Causing raw value: `Herrnhut Schullehrer`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1460000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1460000:
  - Error Message: **`Invalid work id: Julia Hammerschmidt: 200 Jahre Naturforschende Gesellschaft und Museum für Naturkunde Görlitz, hg. v. Willi E. R. Xylander, 2. überarbeitete. Aufl. 2018, 79 (should be R-ID, or M-ID)`**
  - Causing raw value: `Julia Hammerschmidt: 200 Jahre Naturforschende Gesellschaft und Museum für Naturkunde Görlitz, hg. v. Willi E. R. Xylander,  2. überarbeitete. Aufl.  2018, 79 `

### P1470000

- [ ] Error in Col: **Tod - Datum** and row with ID P1470000:
  - Error Message: **`Invalid Reference Document value: R001110 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `1885 {R001110}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1470000:
  - Error Message: **`Expected 4 parts, got 1: Umánaq (Grönland) -- Missionar`**
  - Causing raw value: `Umánaq (Grönland) -- Missionar`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1470000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P1470000:
  - Error Message: **`CollectionID must start with 'C': https://www.gbif.org/occurrence/3335968511 ?`**
  - Causing raw value: `https://www.gbif.org/occurrence/3335968511 ?`

### P1480000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1480000:
  - Error Message: **`Expected 4 parts, got 1: Barby, Seminar -- Professur -- ?`**
  - Causing raw value: `Barby, Seminar -- Professur -- ? `

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1480000:
  - Error Message: **`Invalid work id: UAH GN.A.232 http://digital.slub-dresden.de/id1789505143/477 (should be R-ID, or M-ID)`**
  - Causing raw value: ` UAH GN.A.232 http://digital.slub-dresden.de/id1789505143/477`
  - Full field: _R0012900 | UAH GN.A.232 http://digital.slub-dresden.de/id1789505143/477_

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Literaturnachweis)** and row with ID P1480000:
  - Error Message: **`CollectionID must start with 'C': c-barby`**
  - Causing raw value: `c-barby {R0005100}`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1480000:
  - Error Message: **`LiteratureID must start with 'R': 1763 (Manuskript)/1775 (erster Druck):Flora von Barby`**
  - Causing raw value: `1763 (Manuskript)/1775 (erster Druck):
Flora von Barby`

### P1480500

- [ ] Error in Col: **Übernahme in Personenlexikon** and row with ID P1480500:
  - Error Message: **`Provided string is not in codelist: offen/Kontrolle --> Anmerkung SW: im Findbuch UA gibt es eine Personalakte und einen LL zu einem Franz Eccarius Schramm`**
  - Causing raw value: `offen/Kontrolle --> Anmerkung SW: im Findbuch UA gibt es eine Personalakte und einen LL zu einem Franz Eccarius Schramm`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1480500:
  - Error Message: **`Provided string is not in codelist: offen muß geklärt werden!!ja, laut: Carlos Ossenbach: "ORCHIDS AND ORCHIDOLOGY IN CENTRAL AMERICA. 500 YEARS OF HISTORY", in: Lankesteriana 9 (2009), Nr. 1-2, S. 1-268, 173`**
  - Causing raw value: `offen muß geklärt werden!!
ja, laut: Carlos Ossenbach: "ORCHIDS AND ORCHIDOLOGY IN CENTRAL AMERICA. 500 YEARS OF HISTORY", in: Lankesteriana 9 (2009), Nr. 1-2, S. 1-268, 173`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1480500:
  - Error Message: **`Expected 4 parts, got 1: 1924 Nicaragua Carlos Ossenbach: "ORCHIDS AND ORCHIDOLOGY IN CENTRAL AMERICA. 500 YEARS OF HISTORY", in: Lankesteriana 9 (2009), Nr. 1-2, S. 1-268, 173`**
  - Causing raw value: ` 1924 Nicaragua Carlos Ossenbach: "ORCHIDS AND ORCHIDOLOGY IN CENTRAL AMERICA. 500 YEARS OF HISTORY", in: Lankesteriana 9 (2009), Nr. 1-2, S. 1-268, 173`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1480500:
  - Error Message: **`Invalid work id: Carlos Ossenbach: "ORCHIDS AND ORCHIDOLOGY IN CENTRAL AMERICA. 500 YEARS OF HISTORY", in: Lankesteriana 9 (2009), Nr. 1-2, S. 1-268, S. 173: "One of the few collections of Orchidaceae that we know from Nicaragua during this period is that of Franz Eccarius Schramm (1873-1949), a missionary of the Moravian Evangelical Church who in 1924 collected the type of Campylocentrum sullivannii Fawc. & Rendle (Schramm s.n., Costa de los Mosquitos)." (should be R-ID, or M-ID)`**
  - Causing raw value: `Carlos Ossenbach: "ORCHIDS AND ORCHIDOLOGY IN CENTRAL AMERICA. 500 YEARS OF HISTORY", in: Lankesteriana 9 (2009), Nr. 1-2, S. 1-268, S. 173: "One of the few collections of Orchidaceae that we know from Nicaragua during this period is that of Franz Eccarius Schramm (1873-1949), a missionary of the Moravian Evangelical Church who in 1924 collected the type of Campylocentrum sullivannii Fawc. & Rendle (Schramm s.n., Costa de los Mosquitos)."`

### P1485000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1485000:
  - Error Message: **`Provided string is not in codelist: nein`**
  - Causing raw value: `nein`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1485000:
  - Error Message: **`LocationID must start with 'L': Weißensee (Thüringen)`**
  - Causing raw value: `Weißensee (Thüringen)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1485000:
  - Error Message: **`LocationID must start with 'L': Erlangen`**
  - Causing raw value: `Erlangen`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1485000:
  - Error Message: **`Invalid work id: nein (should be R-ID, or M-ID)`**
  - Causing raw value: `nein`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1485000:
  - Error Message: **`PersonID must start with 'P': Johann Jakob Bossart`**
  - Causing raw value: `Johann Jakob Bossart {R0005300}`

### P1490000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1490000:
  - Error Message: **`LocationID must start with 'L': Hoheneggelsen`**
  - Causing raw value: `Hoheneggelsen`

- [ ] Error in Col: **Tod - Ort** and row with ID P1490000:
  - Error Message: **`LocationID must start with 'L': Berthelsdorf`**
  - Causing raw value: `Berthelsdorf`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1490000:
  - Error Message: **`Invalid work id: MadB.1895 (should be R-ID, or M-ID)`**
  - Causing raw value: `MadB.1895`
  - Full field: _MadB.1895| R.22.151.29_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1490000:
  - Error Message: **`Invalid work id: R.22.151.29 (should be R-ID, or M-ID)`**
  - Causing raw value: ` R.22.151.29`
  - Full field: _MadB.1895| R.22.151.29_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1490000:
  - Error Message: **`LiteratureID must start with 'R': Mitarbeit an Heusers Gnadenfelder Flora, 1859, UA ThS/L V 7`**
  - Causing raw value: `Mitarbeit an Heusers Gnadenfelder Flora, 1859, UA ThS/L V 7`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1490000:
  - Error Message: **`LiteratureID must start with 'R': "Nieskyer Flora", ca. 1865-68, 1876-77, Org. UA Cim.II.30, Abschr. in UA NB.VI.950`**
  - Causing raw value: ` 
"Nieskyer Flora", ca. 1865-68, 1876-77, Org. UA Cim.II.30, Abschr. in UA NB.VI.950 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1490000:
  - Error Message: **`LiteratureID must start with 'R': "Flora der Oberlausitz und Herrnhuter Umgebung", UA NB.VI.951.a+b = "Flora von Herrnhut und Umgebung", UA.NB.VI.63 nr.1+2 (als Typoskript im Herbarium DD), Orig. 1888-1893 verschollen`**
  - Causing raw value: `"Flora der Oberlausitz und Herrnhuter Umgebung", UA NB.VI.951.a+b =  
"Flora von Herrnhut und Umgebung", UA.NB.VI.63 nr.1+2 (als Typoskript im Herbarium DD), Orig. 1888-1893 verschollen `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1490000:
  - Error Message: **`LiteratureID must start with 'R': "Flora des Harzes 1885, Gnadau, Bernburg, Staßfurt, Magdeburg", UA.NB.VI.962 Kopie oder eventuell das Original (aus Lehrerinnenseminar in Gnadau in Sammlung E. Welk in Halle als Datei vorhanden ohne Signatur`**
  - Causing raw value: ` 
"Flora des Harzes 1885, Gnadau, Bernburg, Staßfurt, Magdeburg", UA.NB.VI.962  Kopie oder eventuell das Original (aus Lehrerinnenseminar in Gnadau in Sammlung E. Welk in Halle als Datei vorhanden ohne Signatur`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1490000:
  - Error Message: **`LiteratureID must start with 'R': Achtung Verwechslungsgefahr: es gibt wohl für 1888 eine Flora von Niesky und eine von Herrnhut!?!`**
  - Causing raw value: ` 

Achtung Verwechslungsgefahr: es gibt wohl für 1888 eine Flora von Niesky und eine von Herrnhut!?!`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1490000:
  - Error Message: **`Invalid work id: Bachelorarbeit bei Frank Müller, Botanik TU Dresden, Datei bei Frank und Sarah (should be R-ID, or M-ID)`**
  - Causing raw value: `Bachelorarbeit bei Frank Müller, Botanik TU Dresden, Datei bei Frank und Sarah `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1490000:
  - Error Message: **`Invalid work id: Sagorski: "Zwei neue Rubusformen (Sonderdruck)", in: Leimbach 12 (1894), Nr. 1 (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Sagorski: "Zwei neue Rubusformen (Sonderdruck)", in: Leimbach 12 (1894), Nr. 1 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1490000:
  - Error Message: **`Invalid work id: Helmut Passig: "Flora von Herrnhut und Umgebung", in: Berichte der Naturforschenden Gesellschaft der Oberlausitz Supplement zu Bd. 9 (2000): erwähnt 1 Original und 3 Abschriften (mit Ergänzungen) der Flora Herrnhuts von Schultze (should be R-ID, or M-ID)`**
  - Causing raw value: `Helmut Passig: "Flora von Herrnhut und Umgebung", in: Berichte der Naturforschenden Gesellschaft der Oberlausitz Supplement zu Bd. 9 (2000): erwähnt 1 Original und 3 Abschriften (mit Ergänzungen) der Flora Herrnhuts von Schultze`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1490000:
  - Error Message: **`Invalid work id: Hardtke (should be R-ID, or M-ID)`**
  - Causing raw value: `Hardtke`

### P1495000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1495000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1495000:
  - Error Message: **`LocationID must start with 'L': Grabow`**
  - Causing raw value: `Grabow`

- [ ] Error in Col: **Tod - Ort** and row with ID P1495000:
  - Error Message: **`LocationID must start with 'L': Pilgerhut (Berbice)`**
  - Causing raw value: `Pilgerhut (Berbice)`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1495000:
  - Error Message: **`Expected 4 parts, got 1: Berbice`**
  - Causing raw value: `Berbice`

- [ ] Error in Col: **Wichtige Werke der Person ohne botanischen Kontext** and row with ID P1495000:
  - Error Message: **`Invalid work id: 1 handschriftliches Manuskript („Polyglotta americana. 1. Grammatik der arawackischen Sprache (should be R-ID, or M-ID)`**
  - Causing raw value: `1 handschriftliches Manuskript („Polyglotta americana. 1. Grammatik der arawackischen Sprache `
  - Full field: _1 handschriftliches Manuskript („Polyglotta americana. 1. Grammatik der arawackischen Sprache |
 2. Lexikon der arawackischen Sprache“, o.O., 1880, 357 Blatt; Abschrift von Will. Herzog
beide in: https://www.iai.spk-berlin.de/sammlungen/ueber-die-sondersammlungen/nachlaesse/nachlass/schumann-theophilus-1719-1760.html_

- [ ] Error in Col: **Wichtige Werke der Person ohne botanischen Kontext** and row with ID P1495000:
  - Error Message: **`Invalid work id: 2. Lexikon der arawackischen Sprache“, o.O., 1880, 357 Blatt; Abschrift von Will. Herzogbeide in: https://www.iai.spk-berlin.de/sammlungen/ueber-die-sondersammlungen/nachlaesse/nachlass/schumann-theophilus-1719-1760.html (should be R-ID, or M-ID)`**
  - Causing raw value: ` 2. Lexikon der arawackischen Sprache“, o.O., 1880, 357 Blatt; Abschrift von Will. Herzog
beide in: https://www.iai.spk-berlin.de/sammlungen/ueber-die-sondersammlungen/nachlaesse/nachlass/schumann-theophilus-1719-1760.html`
  - Full field: _1 handschriftliches Manuskript („Polyglotta americana. 1. Grammatik der arawackischen Sprache |
 2. Lexikon der arawackischen Sprache“, o.O., 1880, 357 Blatt; Abschrift von Will. Herzog
beide in: https://www.iai.spk-berlin.de/sammlungen/ueber-die-sondersammlungen/nachlaesse/nachlass/schumann-theophilus-1719-1760.html_

### P1500000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1500000:
  - Error Message: **`LocationID must start with 'L': Bethlehem (Pennsylv.)`**
  - Causing raw value: `Bethlehem (Pennsylv.)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1500000:
  - Error Message: **`LocationID must start with 'L': Bethlehem`**
  - Causing raw value: `Bethlehem `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: Bethlehem und Nazareth (Pennsylvania)`**
  - Causing raw value: `Bethlehem und Nazareth (Pennsylvania)`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1787-1798 Niesky,mit Familie in Niesky`**
  - Causing raw value: `1787-1798 Niesky,mit Familie in Niesky  {R0001900}`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1798 Niesky, Seminar`**
  - Causing raw value: `1798 Niesky, Seminar`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1802 Niesky, Knabenanstalt - Lehrer`**
  - Causing raw value: `1802 Niesky, Knabenanstalt - Lehrer`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1807 Gnadenberg (Schlesien) - Pfleger Brüderchor`**
  - Causing raw value: `1807 Gnadenberg (Schlesien) - Pfleger Brüderchor`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1808 Gnadau - Vorsteher lediges Brüderchor`**
  - Causing raw value: `1808 Gnadau - Vorsteher lediges Brüderchor`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1812 Niesky - Eheschließung1812 -1821 Salem North-Carolina - Administrator`**
  - Causing raw value: `1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1500000:
  - Error Message: **`Expected 4 parts, got 1: 1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor`**
  - Causing raw value: `1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor`
  - Full field: _Bethlehem und Nazareth (Pennsylvania)|
1787-1798 Niesky,mit Familie in Niesky  {R0001900}|
1798 Niesky, Seminar|
1802 Niesky, Knabenanstalt - Lehrer|
1807 Gnadenberg (Schlesien) - Pfleger Brüderchor|
1808 Gnadau - Vorsteher lediges Brüderchor|
1812 Niesky - Eheschließung
1812 -1821 Salem North-Carolina - Administrator|
1821-1835 Bethlehem (Pennsylvania), Mädchenanstalt - Inspektor_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1500000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': 1796: "Stammbucheintrag 22. 5. 1796, Barby", in: Lind (Hg.), Herrnhuter Stammbuch des Bruders Lind aus der Brüdergemeine Sarepta im Unterwolgagebiet (Ansetzungssachtitel von Bearbeiter/in) Pädagogium Barby, Sächsische Landesbibliothek - Staats- und Universitätsbibliothek (Dresden) Signatur: Mscr.Dresd.App.2789, Bl., 1795-1814, S. Bl. 73r.`**
  - Causing raw value: ` 1796: "Stammbucheintrag 22. 5. 1796, Barby", in: Lind (Hg.), Herrnhuter Stammbuch des Bruders Lind aus der Brüdergemeine Sarepta im Unterwolgagebiet (Ansetzungssachtitel von Bearbeiter/in) Pädagogium Barby, Sächsische Landesbibliothek - Staats- und Universitätsbibliothek (Dresden)  Signatur: Mscr.Dresd.App.2789, Bl.,  1795-1814, S. Bl. 73r.`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': 1798–1802, ca.: Icones Fungorum Niskiensium`**
  - Causing raw value: `1798–1802, ca.: Icones Fungorum Niskiensium [Unpub. manuscript. Farlow Reference Library of Cryptogamic Botany, Harvard University, Cambridge, Massachusetts, U.S.A.] {https://doi.org/10.5962/bhl.title.137760} `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': 1802-1803: Fungorum Nieskiensium icones, 6 vol., Unpub. manuscript. Academy of Natural Sciences of Drexel University, Philadelphia, Pennsylvania, U.S.A., Academy Library and Archives. L.D. von Schweinitz papers, Collection no. 437`**
  - Causing raw value: `1802-1803: Fungorum Nieskiensium icones, 6 vol., Unpub. manuscript. Academy of Natural Sciences of Drexel University, Philadelphia, Pennsylvania, U.S.A., Academy Library and Archives. L.D. von Schweinitz papers, Collection no. 437 `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': : mit : „Icones Fungorum Nieskiensis“. Bd. 1. und 2., o.O., Folio m. getuschten Zeichnungen, 49 + 71, Vorarbeit zu "Conspectus fungorum", (UA, Cim.II.9.)`**
  - Causing raw value: `[1801-1803]: mit [Albertini, Johann Baptist (?)]: „Icones Fungorum Nieskiensis“. Bd. 1. und 2., o.O.,  Folio m. getuschten Zeichnungen,  49 + 71, Vorarbeit zu "Conspectus fungorum", (UA, Cim.II.9.) `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': Fungorum nieskiesium icones Pars IV,`**
  - Causing raw value: `[1805?] Fungorum nieskiesium icones Pars IV, {https://www.biodiversitylibrary.org/bibliography/122159} `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': 1821 ‘‘Flora Salemitana,’’ a manuscript now held at the Academy of Natural Sciences in Philadelphia (Pennell 1931)`**
  - Causing raw value: `1821 ‘‘Flora Salemitana,’’ a manuscript now held at the Academy of Natural Sciences in Philadelphia (Pennell 1931) `

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1500000:
  - Error Message: **`ManuscriptID must start with 'M': Lewis David von Schweinitz drawings of fungi (Q51398514)`**
  - Causing raw value: ` Lewis David von Schweinitz drawings of fungi (Q51398514) `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1500000:
  - Error Message: **`LiteratureID must start with 'R': mit Johann Baptist von Albertini: Conspectus fungorum in Lusatiae Superioris agro Niskiensi crescentium, e methodo Persooniana, Cum tabulis XII aeneis pictus, species novas XCIII sistentibus. Lipsiae: Sumtibus Kummerianis 1805`**
  - Causing raw value: `mit Johann Baptist von Albertini: Conspectus fungorum in Lusatiae Superioris agro Niskiensi crescentium, e methodo Persooniana, Cum tabulis XII aeneis pictus, species novas XCIII sistentibus. Lipsiae: Sumtibus Kummerianis 1805 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1500000:
  - Error Message: **`LiteratureID must start with 'R': Synopsis fungorum Carolinae superioris, Leipzig 1820`**
  - Causing raw value: `Synopsis fungorum Carolinae superioris, Leipzig 1820 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1500000:
  - Error Message: **`LiteratureID must start with 'R': Specimen florae Americae cryptogamicae, 1821`**
  - Causing raw value: `Specimen florae Americae cryptogamicae, 1821`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1500000:
  - Error Message: **`LiteratureID must start with 'R': Synopsis fungorum Carolinae superioris : secundum observationes, Leipzig: Barth 1822.`**
  - Causing raw value: `Synopsis fungorum Carolinae superioris : secundum observationes, Leipzig: Barth 1822.`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1500000:
  - Error Message: **`LiteratureID must start with 'R': Synopsis Fungorum in America Boreali Media Degentium, 1832 ?`**
  - Causing raw value: `Synopsis Fungorum in America Boreali Media Degentium, 1832 ?`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1500000:
  - Error Message: **`LiteratureID must start with 'R': Synopsis Fungorum in America Boreali media degentium , Philadelphia, PA 1834.`**
  - Causing raw value: `Synopsis Fungorum in America Boreali media degentium , Philadelphia, PA 1834.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1500000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1500000:
  - Error Message: **`Invalid work id: Jason M. Karakehian; Thomas Rödel; Ulrike Damm; Donald H. Pfister; Andrew N. Milkler; Camille Truong; Tom W. May (Hg.): "Specimens in the National Herbarium of Victoria, Australia (MEL) and in Naturalis Biodiversity Center of Leiden, Netherlands (L) associated with Albertini and Schweinitz’s Conspectus fungorum in Lusatiae superioris", in: Taxon 00 (2024), Nr. 00, S. 1-17. (should be R-ID, or M-ID)`**
  - Causing raw value: `Jason M. Karakehian; Thomas Rödel; Ulrike Damm; Donald H. Pfister; Andrew N. Milkler; Camille Truong; Tom W. May (Hg.): "Specimens in the National Herbarium of Victoria, Australia (MEL) and in Naturalis Biodiversity Center of Leiden, Netherlands (L) associated with Albertini and Schweinitz’s Conspectus fungorum in Lusatiae superioris", in: Taxon 00 (2024), Nr. 00, S. 1-17. {https://doi.org/10.1002/tax.13239} `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1500000:
  - Error Message: **`Invalid work id: Staffleu (should be R-ID, or M-ID)`**
  - Causing raw value: `Staffleu`

### P1505000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1505000:
  - Error Message: **`Provided string is not in codelist: nein`**
  - Causing raw value: `nein`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1505000:
  - Error Message: **`Invalid format for LocationID: Lübeck`**
  - Causing raw value: `Lübeck {https://www.wikidata.org/wiki/Q28731149}`

- [ ] Error in Col: **Tod - Ort** and row with ID P1505000:
  - Error Message: **`LocationID must start with 'L': Altona`**
  - Causing raw value: `Altona {https://www.wikidata.org/wiki/Q28731149}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1505000:
  - Error Message: **`Expected 4 parts, got 1: Hamburg`**
  - Causing raw value: `Hamburg {https://www.wikidata.org/wiki/Q28731149}`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1505000:
  - Error Message: **`Invalid format for PersonID: P0650000 (Belege in C-HAL)`**
  - Causing raw value: `P0650000 (Belege in C-HAL) `
  - Full field: _P0650000 (Belege in C-HAL) |
Prof. Hermann Bumeister im Halle, Schwiegersohn und wichtigster entomologischer Partner {https://www.wikidata.org/wiki/Q28731149}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1505000:
  - Error Message: **`Invalid format for PersonID: Prof. Hermann Bumeister im Halle, Schwiegersohn und wichtigster entomologischer Partner`**
  - Causing raw value: `Prof. Hermann Bumeister im Halle, Schwiegersohn und wichtigster entomologischer Partner {https://www.wikidata.org/wiki/Q28731149}`
  - Full field: _P0650000 (Belege in C-HAL) |
Prof. Hermann Bumeister im Halle, Schwiegersohn und wichtigster entomologischer Partner {https://www.wikidata.org/wiki/Q28731149}_

### P1505500

- [ ] Error in Col: **Angehörige - Geschwister** and row with ID P1505500:
  - Error Message: **`Invalid format for PersonID: P022000`**
  - Causing raw value: `P022000 [Johann Christian Breutel] `
  - Full field: _P022000 [Johann Christian Breutel] | P0215000 [Georg Samuel Breutel]_

### P1510000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1510000:
  - Error Message: **`LocationID must start with 'L': Eibau, Sachsen Germany`**
  - Causing raw value: `Eibau, Sachsen Germany`

- [ ] Error in Col: **Tod - Datum** and row with ID P1510000:
  - Error Message: **`Invalid ISO8601-2_Date format: 14353`**
  - Causing raw value: `14353`

- [ ] Error in Col: **Tod - Ort** and row with ID P1510000:
  - Error Message: **`LocationID must start with 'L': Tacoma, Washinton, USA`**
  - Causing raw value: `Tacoma, Washinton, USA`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1510000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1510000:
  - Error Message: **`PersonID must start with 'P': Herma`**
  - Causing raw value: `Herma`

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1510000:
  - Error Message: **`PersonID must start with 'P': https://www.wikidata.org/wiki/Q140913022`**
  - Causing raw value: `https://www.wikidata.org/wiki/Q140913022`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1510000:
  - Error Message: **`Invalid work id: James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. (should be R-ID, or M-ID)`**
  - Causing raw value: `James S. Pringle: "Contributions by Moravian missionaries to the knowledge of the flora of Labrador", in: CANADIAN HORTICULTURAL HISTORY an interdisciplinary journal / HISTOIRE DE L' HORTICULTURE AU CANADA revue interdisciplinaire 2 (1991), Nr. 4, S. 187-222. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1510000:
  - Error Message: **`Invalid work id: Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180. (should be R-ID, or M-ID)`**
  - Causing raw value: `Jacques Cayouette; Stephen J. Darbyshire: "Taxa Described by Steudel from the Labrador Plants Collected by the Moravian Missionary Albrecht and Distributed by Hohenacker", in: Taxon 43 (1994), Nr. 2, S. 169-180. `

### P1520000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1520000:
  - Error Message: **`LocationID must start with 'L': Wales`**
  - Causing raw value: `Wales`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1520000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1520000:
  - Error Message: **`LiteratureID must start with 'R': STEINHAUER, H. 1818. On fossil reliquia of unknown vegetables in the coal strata, Trans. Am. Phil. Soc., New Series 1:265–297`**
  - Causing raw value: `STEINHAUER, H. 1818. On fossil reliquia of unknown vegetables in the coal strata, Trans. Am. Phil. Soc., New Series 1:265–297`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1520000:
  - Error Message: **`LiteratureID must start with 'R': "Henry Steinhauer (1818) published an early paleobotanical paper on fossil plants of coalbearing strata in England; this work described 10 species of such plants with valid binomial names. His manuscript notes on fossils survive in Philadelphia (Phillips and Phillips 1963)." Troyer 2009, 4`**
  - Causing raw value: `"Henry Steinhauer (1818) published an early paleobotanical paper on fossil plants of coalbearing  strata in England; this work described 10 species of such plants with valid binomial names. His manuscript notes on fossils survive in Philadelphia (Phillips and Phillips 1963)." Troyer 2009, 4`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1520000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009 `
  - Full field: _Troyer 2009 |
Hugh S. Torrens: "The Moravian minister Rev. Henry Steinhauer (1782-1818); his work on fossil plants, their first 'scientific' description and the planned Mineral Botany", in: A. J.  Bowden (Hg.), History of Palaeobotany: Selected Essays, London: Geological Soc. 2005, S. 13-29._

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1520000:
  - Error Message: **`Invalid work id: Hugh S. Torrens: "The Moravian minister Rev. Henry Steinhauer (1782-1818); his work on fossil plants, their first 'scientific' description and the planned Mineral Botany", in: A. J. Bowden (Hg.), History of Palaeobotany: Selected Essays, London: Geological Soc. 2005, S. 13-29. (should be R-ID, or M-ID)`**
  - Causing raw value: `Hugh S. Torrens: "The Moravian minister Rev. Henry Steinhauer (1782-1818); his work on fossil plants, their first 'scientific' description and the planned Mineral Botany", in: A. J.  Bowden (Hg.), History of Palaeobotany: Selected Essays, London: Geological Soc. 2005, S. 13-29.`
  - Full field: _Troyer 2009 |
Hugh S. Torrens: "The Moravian minister Rev. Henry Steinhauer (1782-1818); his work on fossil plants, their first 'scientific' description and the planned Mineral Botany", in: A. J.  Bowden (Hg.), History of Palaeobotany: Selected Essays, London: Geological Soc. 2005, S. 13-29._

### P1530000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1530000:
  - Error Message: **`LocationID must start with 'L': Wales`**
  - Causing raw value: `Wales`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1530000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1530000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P1540000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1540000:
  - Error Message: **`URL is not valid: nein (2024-12-16)`**
  - Causing raw value: `nein (2024-12-16)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1540000:
  - Error Message: **`LocationID must start with 'L': gef. In Ostfrankreich`**
  - Causing raw value: `gef. In Ostfrankreich`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1540000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1550000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1550000:
  - Error Message: **`Expected 4 parts, got 1: Kyimbila / Nyassa-See (Deutsch-Ostafrika)`**
  - Causing raw value: `Kyimbila / Nyassa-See (Deutsch-Ostafrika) {R0004200}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1550000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1550000:
  - Error Message: **`LiteratureID must start with 'R': Orchideenkunde des Nyassalandes`**
  - Causing raw value: `Orchideenkunde des Nyassalandes`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1550000:
  - Error Message: **`Invalid work id: R. Schlechter: "Orchidaceae Stolzianae. Ein Beitrag zur Ochideenkunde des Nyassalandes", in: Botanische Jahrbücher für Systematik, Pflanzengeschichte und Pflanzengeographie 53 (1915), S. 477-605. mit 1146 neuen Arten von A.Stolz (should be R-ID, or M-ID)`**
  - Causing raw value: `R. Schlechter: "Orchidaceae Stolzianae. Ein Beitrag zur Ochideenkunde des Nyassalandes", in: Botanische Jahrbücher für Systematik, Pflanzengeschichte und Pflanzengeographie 53 (1915), S. 477-605. mit 1146 neuen Arten von A.Stolz`

### P1560000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1560000:
  - Error Message: **`LocationID must start with 'L': Gleina`**
  - Causing raw value: `Gleina`

- [ ] Error in Col: **Tod - Ort** and row with ID P1560000:
  - Error Message: **`LocationID must start with 'L': Trachenberge (Dresden)`**
  - Causing raw value: `Trachenberge (Dresden)`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1560000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1570000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1570000:
  - Error Message: **`URL is not valid: nein (2024-12-16)`**
  - Causing raw value: `nein (2024-12-16)`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1570000:
  - Error Message: **`PersonID must start with 'P': Albertini`**
  - Causing raw value: `Albertini {R0001500}`

### P1589000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1589000:
  - Error Message: **`LocationID must start with 'L': Neuwied`**
  - Causing raw value: `Neuwied {R0001200}`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1589000:
  - Error Message: **`Expected 4 parts, got 1: Grönland -- Missionar`**
  - Causing raw value: `Grönland -- Missionar`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1589000:
  - Error Message: **`Invalid work id: R0001200 (246-259) (should be R-ID, or M-ID)`**
  - Causing raw value: `R0001200 (246-259)`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1589000:
  - Error Message: **`Invalid format for PersonID: P0220000 (Johann Christian Breutel)`**
  - Causing raw value: `P0220000 (Johann Christian Breutel)`

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1589000:
  - Error Message: **`PersonID must start with 'P': Fürst Stolberg-Wernigerode`**
  - Causing raw value: `Fürst Stolberg-Wernigerode`

- [ ] Error in Col: **Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere** and row with ID P1589000:
  - Error Message: **`Invalid work id: MS in Sammlung Fürst Stolberg, Hirzenhain: Grönländische Pflanzen, gesammelt von dem Mefrionas Tietzen zu Lichtenfels in Grönland, Sporleder, Friedrich Wilhelm *1787-1875* - (should be R-ID, or M-ID)`**
  - Causing raw value: `MS in Sammlung Fürst Stolberg, Hirzenhain: Grönländische Pflanzen, gesammelt von dem Mefrionas Tietzen zu Lichtenfels in Grönland, Sporleder, Friedrich Wilhelm *1787-1875* - [o.J.] {https://kxp.k10plus.de/DB=9.1005/PPNSET?PPN=83529028X}`
  - Full field: _R0011100|MS in Sammlung Fürst Stolberg, Hirzenhain: Grönländische Pflanzen, gesammelt von dem Mefrionas Tietzen zu Lichtenfels in Grönland, Sporleder, Friedrich Wilhelm *1787-1875* - [o.J.] {https://kxp.k10plus.de/DB=9.1005/PPNSET?PPN=83529028X}| R0002000 | R0002100_

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1589000:
  - Error Message: **`Invalid work id: R0001400 Morten P. Porsild: "On some herbaria from Greenland and Labrador collected by the Moravian brethren", in: Meddelelser om Grønland 93 (1935), Nr. 3, S. 84-94, 85 (should be R-ID, or M-ID)`**
  - Causing raw value: `R0001400 Morten P. [Petersen] Porsild: "On some herbaria from Greenland and Labrador collected by the Moravian brethren", in: Meddelelser om Grønland [Medd. om Gronland] 93 (1935), Nr. 3, S. 84-94, 85`

### P1590000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1590000:
  - Error Message: **`URL is not valid: nein (2024-12-16)`**
  - Causing raw value: `nein (2024-12-16)`

- [ ] Error in Col: **Tod - Datum** and row with ID P1590000:
  - Error Message: **`Invalid ISO8601-2_Date format: nach 1883`**
  - Causing raw value: `nach 1883`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1590000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1595000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1804-1810'`**
  - Causing raw value: `1804-1810; L2250000; Pädagogium; Schüler {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1810-1812'`**
  - Causing raw value: `1810-1812; L2250000; Seminar; Student {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1812-1813'`**
  - Causing raw value: `1812-1813; L2250000; Knabenanstalt; Lehrer {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1813-1816'`**
  - Causing raw value: `1813-1816; L1120000; Knabenanstalt; Lehrer {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1816-1817'`**
  - Causing raw value: `1816-1817; L0800000; ; Lehrer {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1817-1824'`**
  - Causing raw value: `1817-1824; L1550000; ; Lehrer {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1824-1829'`**
  - Causing raw value: `1824-1829; L0600000; ; Brüderpfleger/Diacon {M0029000}  `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1830-1831'`**
  - Causing raw value: `1830-1831; L0900000 [Cedarhall/Antigua]; ; Missionar  {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1831-1838'`**
  - Causing raw value: `1831-1838; L1102000 [Gracehill/Antigua]; ; Missionar  {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1838-1841'`**
  - Causing raw value: `1838-1841; L2400000 [St. John's/Antigua]; ; Missionar  {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1841-1843'`**
  - Causing raw value: `1841-1843; L1102000 [Gracehill/Antigua]; ; Missionar  {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1843-1856'`**
  - Causing raw value: `1843-1856; L2400000 [St. John's/Antigua]; ; Missionar  {M0029000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595000:
  - Error Message: **`Cannot parse as date or period: '1856-1866'`**
  - Causing raw value: `1856-1866; L2250000; ; Ruhestand  {M0029000}`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1595000:
  - Error Message: **`PersonID must start with 'P': Hans, W.`**
  - Causing raw value: `Hans, W.`

### P1595500

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1595500:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595500:
  - Error Message: **`Cannot parse as date or period: '1801-1812'`**
  - Causing raw value: `1801-1812; L2150000; Apotheke der Herrnhuter; Lehrling {M0033000} `
  - Full field: _1801-1812; L2150000; Apotheke der Herrnhuter; Lehrling {M0033000} |
1812-1814; L2200000; Apotheke der Herrnhuter; Lehrling {R0000800} |
1814-1824; L2150000; Apotheke der Herrnhuter; Gehilfe {R0000800} |
1824-1827; L2150000; Apotheke der Herrnhuter; Leitung {R0000800}_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595500:
  - Error Message: **`Cannot parse as date or period: '1812-1814'`**
  - Causing raw value: `1812-1814; L2200000; Apotheke der Herrnhuter; Lehrling {R0000800} `
  - Full field: _1801-1812; L2150000; Apotheke der Herrnhuter; Lehrling {M0033000} |
1812-1814; L2200000; Apotheke der Herrnhuter; Lehrling {R0000800} |
1814-1824; L2150000; Apotheke der Herrnhuter; Gehilfe {R0000800} |
1824-1827; L2150000; Apotheke der Herrnhuter; Leitung {R0000800}_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595500:
  - Error Message: **`Cannot parse as date or period: '1814-1824'`**
  - Causing raw value: `1814-1824; L2150000; Apotheke der Herrnhuter; Gehilfe {R0000800} `
  - Full field: _1801-1812; L2150000; Apotheke der Herrnhuter; Lehrling {M0033000} |
1812-1814; L2200000; Apotheke der Herrnhuter; Lehrling {R0000800} |
1814-1824; L2150000; Apotheke der Herrnhuter; Gehilfe {R0000800} |
1824-1827; L2150000; Apotheke der Herrnhuter; Leitung {R0000800}_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1595500:
  - Error Message: **`Cannot parse as date or period: '1824-1827'`**
  - Causing raw value: `1824-1827; L2150000; Apotheke der Herrnhuter; Leitung {R0000800}`
  - Full field: _1801-1812; L2150000; Apotheke der Herrnhuter; Lehrling {M0033000} |
1812-1814; L2200000; Apotheke der Herrnhuter; Lehrling {R0000800} |
1814-1824; L2150000; Apotheke der Herrnhuter; Gehilfe {R0000800} |
1824-1827; L2150000; Apotheke der Herrnhuter; Leitung {R0000800}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1595500:
  - Error Message: **`PersonID must start with 'P': Botanisierte mit seinem jüngeren Bruder (nicht identifiziert, nicht Franz Ferdinand Thrän)`**
  - Causing raw value: `Botanisierte mit seinem jüngeren Bruder (nicht identifiziert, nicht Franz Ferdinand Thrän) {R0004300}`

### P1600000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1600000:
  - Error Message: **`URL is not valid: nein (2024-12-17)`**
  - Causing raw value: `nein (2024-12-17)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1600000:
  - Error Message: **`LocationID must start with 'L': Gnadenfrei`**
  - Causing raw value: `Gnadenfrei`

- [ ] Error in Col: **Tod - Ort** and row with ID P1600000:
  - Error Message: **`LocationID must start with 'L': Neusalz`**
  - Causing raw value: `Neusalz`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1600000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P1600000:
  - Error Message: **`CollectionID must start with 'C': GLM (111869?)`**
  - Causing raw value: `GLM (111869?) `
  - Full field: _GLM (111869?) | C-GOET {https://hdl.handle.net/21.11107/record_DE-MUS-069321_GOET040920}_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1600000:
  - Error Message: **`LiteratureID must start with 'R': Nachlass Thust mit umfassenden botanischen Manuskripten im UA: UA NB.VI. 63.b.Thust, Gustav Adolf: I Flora Sarepta’s und II. Meterologische Beobachtungen Sarepta, o.O., o.J. 365 S., okt. vgl. UA NB VI. 185`**
  - Causing raw value: `Nachlass Thust mit umfassenden botanischen Manuskripten im UA:  UA NB.VI. 63.b.
Thust, Gustav Adolf: I Flora Sarepta’s und II. Meterologische Beobachtungen Sarepta, o.O., o.J. 365 S., okt. vgl. UA NB VI. 185 `
  - Full field: _Nachlass Thust mit umfassenden botanischen Manuskripten im UA:  UA NB.VI. 63.b.
Thust, Gustav Adolf: I Flora Sarepta’s und II. Meterologische Beobachtungen Sarepta, o.O., o.J. 365 S., okt. vgl. UA NB VI. 185 | UA NB VI.185 Floren der Brüdergemeinen Nrm 1-11_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1600000:
  - Error Message: **`LiteratureID must start with 'R': UA NB VI.185 Floren der Brüdergemeinen Nrm 1-11`**
  - Causing raw value: ` UA NB VI.185 Floren der Brüdergemeinen Nrm 1-11`
  - Full field: _Nachlass Thust mit umfassenden botanischen Manuskripten im UA:  UA NB.VI. 63.b.
Thust, Gustav Adolf: I Flora Sarepta’s und II. Meterologische Beobachtungen Sarepta, o.O., o.J. 365 S., okt. vgl. UA NB VI. 185 | UA NB VI.185 Floren der Brüdergemeinen Nrm 1-11_

### P1610000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1610000:
  - Error Message: **`URL is not valid: nein (2024-12-17)`**
  - Causing raw value: `nein (2024-12-17)`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1610000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1610000:
  - Error Message: **`LocationID must start with 'L': Schönbrunn (Schlesien)`**
  - Causing raw value: `Schönbrunn (Schlesien)`

- [ ] Error in Col: **Tod - Ort** and row with ID P1610000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1610000:
  - Error Message: **`Expected 4 parts, got 1: Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1610000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Literaturnachweis)** and row with ID P1610000:
  - Error Message: **`CollectionID must start with 'C': eigenes Herbarium (Leske, 1785, S. 182)`**
  - Causing raw value: `eigenes Herbarium (Leske, 1785, S. 182)`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1610000:
  - Error Message: **`LiteratureID must start with 'R': Brief an Dr. Anton, Karl Gottlob von, Niesky 22. Juni 1785`**
  - Causing raw value: `Brief an Dr. Anton, Karl Gottlob von, Niesky 22. Juni 1785 {http://digital.slub-dresden.de/id453951775}`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1610000:
  - Error Message: **`Invalid work id: Nathanael Gottfried Leske: Reise durch Sachsen : in Rüksicht der Naturgeschichte und Oekonomie / unternommen und beschrieben von Nathanael Gottfried Leske, Leipzig: J. G. Müller 1785, S. 182f. (should be R-ID, or M-ID)`**
  - Causing raw value: `Nathanael Gottfried Leske: Reise durch Sachsen : in Rüksicht der Naturgeschichte und Oekonomie / unternommen und beschrieben von Nathanael Gottfried Leske, Leipzig: J. G. Müller 1785, S. 182f.`

### P1620000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1620000:
  - Error Message: **`URL is not valid: nein (2024-12-17)`**
  - Causing raw value: `nein (2024-12-17)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1620000:
  - Error Message: **`LocationID must start with 'L': Gnadenfeld`**
  - Causing raw value: `Gnadenfeld`

- [ ] Error in Col: **Tod - Ort** and row with ID P1620000:
  - Error Message: **`LocationID must start with 'L': Königsfeld`**
  - Causing raw value: `Königsfeld`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1620000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1630000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1630000:
  - Error Message: **`URL is not valid: nein (2024-12-17)`**
  - Causing raw value: `nein (2024-12-17)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1630000:
  - Error Message: **`LocationID must start with 'L': Neusalz`**
  - Causing raw value: `Neusalz`

- [ ] Error in Col: **Tod - Ort** and row with ID P1630000:
  - Error Message: **`LocationID must start with 'L': Northeim`**
  - Causing raw value: `Northeim`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1630000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1640000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1640000:
  - Error Message: **`LocationID must start with 'L': Königsfeld`**
  - Causing raw value: `Königsfeld`

- [ ] Error in Col: **Tod - Ort** and row with ID P1640000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1640000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1640000:
  - Error Message: **`Invalid work id: Uttendörfers botanische Kenntnisse zeigen sich in seiner Auswertung des Exkursionstagebuches von Barby 1766, wo er die Richtigkeit der Angaben bewertet (Uttendörfer 1916, 98ff.) (should be R-ID, or M-ID)`**
  - Causing raw value: ` Uttendörfers botanische Kenntnisse zeigen sich in seiner Auswertung des Exkursionstagebuches von Barby 1766, wo er die Richtigkeit der Angaben bewertet (Uttendörfer 1916, 98ff.) `
  - Full field: _R0006300 | Uttendörfers botanische Kenntnisse zeigen sich in seiner Auswertung des Exkursionstagebuches von Barby 1766, wo er die Richtigkeit der Angaben bewertet (Uttendörfer 1916, 98ff.) | 
Nachlass Uttendörfer im Unitätsarchiv "Lebenserinnerungen" von 668 Seiten._

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1640000:
  - Error Message: **`Invalid work id: Nachlass Uttendörfer im Unitätsarchiv "Lebenserinnerungen" von 668 Seiten. (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Nachlass Uttendörfer im Unitätsarchiv "Lebenserinnerungen" von 668 Seiten.`
  - Full field: _R0006300 | Uttendörfers botanische Kenntnisse zeigen sich in seiner Auswertung des Exkursionstagebuches von Barby 1766, wo er die Richtigkeit der Angaben bewertet (Uttendörfer 1916, 98ff.) | 
Nachlass Uttendörfer im Unitätsarchiv "Lebenserinnerungen" von 668 Seiten._

### P1650000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1650000:
  - Error Message: **`URL is not valid: nein (2024-12-17)`**
  - Causing raw value: `nein (2024-12-17)`

- [ ] Error in Col: **Tod - Datum** and row with ID P1650000:
  - Error Message: **`Invalid ISO8601-2_Date format: ?`**
  - Causing raw value: `?`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1650000:
  - Error Message: **`Expected 4 parts, got 1: Salem, North Carolinia, USA`**
  - Causing raw value: `Salem, North Carolinia, USA`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1650000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1650000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P1651000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1651000:
  - Error Message: **`Expected 4 parts, got 1: Labrador 1858 / Grönland 1859?`**
  - Causing raw value: `Labrador 1858 / Grönland 1859?`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1651000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Objektnachweis)** and row with ID P1651000:
  - Error Message: **`CollectionID must start with 'C': nur in Halle bekannt ca. 80 Belege alle von 1858/59 aus Stationrn in Labrador Grönland - unklar ob selbst Herrnhuter oder ein sammler, der diese Sachen bezogen hat`**
  - Causing raw value: `nur in Halle bekannt ca. 80 Belege alle von 1858/59 aus Stationrn in Labrador Grönland - unklar ob selbst Herrnhuter oder ein sammler, der diese Sachen bezogen hat`

### P1660000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1660000:
  - Error Message: **`Expected 4 parts, got 1: ...`**
  - Causing raw value: ` ... `
  - Full field: _1753/1754; L2000000; Pflegeanstalt für kleine Kinder; Schüler {R0011200} | 1754/1763; L0500000; Knäbchenanstalt; Schüler {R0011200} | ... | 1772/1775; L0200000; Seminar; Student {R0011200} | 1775/1778; L2250000; Unitäts-Knabenanstalt; {R0011200} | 1778; L0200000;; {R0011200} | 1779/; L0500000; ..._

- [ ] Error in Col: **Wirkungsorte** and row with ID P1660000:
  - Error Message: **`Expected 4 parts, got 3: 1779/; L0500000; ...`**
  - Causing raw value: ` 1779/; L0500000; ...`
  - Full field: _1753/1754; L2000000; Pflegeanstalt für kleine Kinder; Schüler {R0011200} | 1754/1763; L0500000; Knäbchenanstalt; Schüler {R0011200} | ... | 1772/1775; L0200000; Seminar; Student {R0011200} | 1775/1778; L2250000; Unitäts-Knabenanstalt; {R0011200} | 1778; L0200000;; {R0011200} | 1779/; L0500000; ..._

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1660000:
  - Error Message: **`Invalid work id: Troyer 2009 (should be R-ID, or M-ID)`**
  - Causing raw value: `Troyer 2009`

### P1670000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1670000:
  - Error Message: **`LocationID must start with 'L': Montmirail`**
  - Causing raw value: `Montmirail`

- [ ] Error in Col: **Tod - Ort** and row with ID P1670000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1670000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1670000:
  - Error Message: **`ManuscriptID must start with 'M': ca. 30 Tafeln mit kolorierten Zeichnungen, UA. Cim.II.7`**
  - Causing raw value: `[um 1803] ca. 30 Tafeln mit kolorierten Zeichnungen, [Cryptogamen. Zeichnungen] UA. Cim.II.7`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1670000:
  - Error Message: **`Invalid work id: Barber: Flora der Oberlausitz (1898) (should be R-ID, or M-ID)`**
  - Causing raw value: `Barber: Flora der Oberlausitz (1898) `

### P1680000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1680000:
  - Error Message: **`Expected 4 parts, got 1: nach Lebenslauf auflisten`**
  - Causing raw value: `nach Lebenslauf auflisten `
  - Full field: _nach Lebenslauf auflisten |
Labrador 1869 (laut Herbarbeleg DR087272); Matthäus Warmow war allerdings Missionar in Grönland laut den Verzeichnissen in NadB; in R0009200 Bericht Reise Cumberland Inlet_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1680000:
  - Error Message: **`Expected 4 parts, got 3: Labrador 1869 (laut Herbarbeleg DR087272); Matthäus Warmow war allerdings Missionar in Grönland laut den Verzeichnissen in NadB; in R0009200 Bericht Reise Cumberland Inlet`**
  - Causing raw value: `Labrador 1869 (laut Herbarbeleg DR087272); Matthäus Warmow war allerdings Missionar in Grönland laut den Verzeichnissen in NadB; in R0009200 Bericht Reise Cumberland Inlet`
  - Full field: _nach Lebenslauf auflisten |
Labrador 1869 (laut Herbarbeleg DR087272); Matthäus Warmow war allerdings Missionar in Grönland laut den Verzeichnissen in NadB; in R0009200 Bericht Reise Cumberland Inlet_

### P1683000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1683000:
  - Error Message: **`Expected 4 parts, got 1: Hopedale, Nain, Zoar,`**
  - Causing raw value: `Hopedale, Nain, Zoar, `
  - Full field: _Hopedale, Nain, Zoar, | 1878/1886; L2260000;; {R0010200}_

### P1690000

- [ ] Error in Col: **Angehörige - Kinder** and row with ID P1690000:
  - Error Message: **`Invalid format for PersonID: P168400`**
  - Causing raw value: ` P168400`
  - Full field: _P1685000 | P168400_

- [ ] Error in Col: **Geburt - Ort** and row with ID P1690000:
  - Error Message: **`LocationID must start with 'L': Königsfeld`**
  - Causing raw value: `Königsfeld`

- [ ] Error in Col: **Tod - Ort** and row with ID P1690000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1690000:
  - Error Message: **`LocationID must start with 'L': Okak`**
  - Causing raw value: `; Okak; Missionsstation; Missionar {R0010300}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1690000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1700000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1700000:
  - Error Message: **`Expected 4 parts, got 3: 1833/1840; L1101000; Knabenanstalt, Lehrer`**
  - Causing raw value: ` 1833/1840; L1101000; Knabenanstalt, Lehrer {M0036000} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1700000:
  - Error Message: **`Invalid format for LocationID: L0960000 L0300000`**
  - Causing raw value: ` 1841; L0960000 L0300000; Universität; Student {M0036000} `

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1700000:
  - Error Message: **`PersonID must start with 'P': Rudolf Kölbing`**
  - Causing raw value: `Rudolf Kölbing {R0009800} `
  - Full field: _Rudolf Kölbing {R0009800} | 
F.W. Kölbing {R0009800} |
Hasse, Ernst Reichel, Christian Gottfried Wetschky und Gustav Wetschky {R0009800}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1700000:
  - Error Message: **`PersonID must start with 'P': F.W. Kölbing`**
  - Causing raw value: ` 
F.W. Kölbing {R0009800} `
  - Full field: _Rudolf Kölbing {R0009800} | 
F.W. Kölbing {R0009800} |
Hasse, Ernst Reichel, Christian Gottfried Wetschky und Gustav Wetschky {R0009800}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1700000:
  - Error Message: **`PersonID must start with 'P': Hasse, Ernst Reichel, Christian Gottfried Wetschky und Gustav Wetschky`**
  - Causing raw value: `Hasse, Ernst Reichel, Christian Gottfried Wetschky und Gustav Wetschky {R0009800}`
  - Full field: _Rudolf Kölbing {R0009800} | 
F.W. Kölbing {R0009800} |
Hasse, Ernst Reichel, Christian Gottfried Wetschky und Gustav Wetschky {R0009800}_

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1700000:
  - Error Message: **`PersonID must start with 'P': Rudolf von Uechtritz (GLM 164640)`**
  - Causing raw value: `Rudolf von Uechtritz (GLM 164640)`

- [ ] Error in Col: **Botanik - Beitrag zu Sammlungen (Literaturnachweis)** and row with ID P1700000:
  - Error Message: **`CollectionID must start with 'C': R0014200`**
  - Causing raw value: `R0014200`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1700000:
  - Error Message: **`ManuscriptID must start with 'M': TU Darmstadt, Universitäts- und Landesbibliothek besitzt einen umfasenden Nachlass. Sig.: Nachlass 153`**
  - Causing raw value: `TU Darmstadt, Universitäts- und Landesbibliothek besitzt einen umfasenden Nachlass. Sig.: Nachlass 153 `
  - Full field: _TU Darmstadt, Universitäts- und Landesbibliothek besitzt einen umfasenden Nachlass. Sig.: Nachlass 153 | https://www.ulb.tu-darmstadt.de/finden_nutzen/historische_sammlungen/nachlaesse/index.de.jsp_

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1700000:
  - Error Message: **`ManuscriptID must start with 'M': https://www.ulb.tu-darmstadt.de/finden_nutzen/historische_sammlungen/nachlaesse/index.de.jsp`**
  - Causing raw value: ` https://www.ulb.tu-darmstadt.de/finden_nutzen/historische_sammlungen/nachlaesse/index.de.jsp`
  - Full field: _TU Darmstadt, Universitäts- und Landesbibliothek besitzt einen umfasenden Nachlass. Sig.: Nachlass 153 | https://www.ulb.tu-darmstadt.de/finden_nutzen/historische_sammlungen/nachlaesse/index.de.jsp_

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': In Niesky Empfänger zahlreicher missionarischer Sendungen, Status unklar`**
  - Causing raw value: `In Niesky Empfänger zahlreicher missionarischer Sendungen, Status unklar `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Ende 1880er: Bearbeitung einer Laubmoosflora der Oberlausitz`**
  - Causing raw value: ` 

Ende 1880er: Bearbeitung einer Laubmoosflora der Oberlausitz `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': bis Ende 1894 "Neubearbeitung der Flora der Lausitz" "5 starke Quartbände""Selbst das Vorwort war bereits geschrieben." "Zwei der Bände gelangten in den Besitz der Bibliothek des Pädagogiums der evangelischen Brüder-Unität zu Niesky, die übrigen nebst dem umfangreichen Herbar des Verstorbenen wurden der Naturforschenden Gesellschaft zu Görlitz überwiesen" (E. Barber: 1898, 344)Früher: Flora von Zeist und Umgebung (Manuskript) Ms in UA als Ergänzung 1831 zur Pflanzensammlung in NatKab (Niesky) UA.Cim.II.4`**
  - Causing raw value: ` 

bis Ende 1894 "Neubearbeitung der Flora der Lausitz" "5 starke Quartbände""Selbst das Vorwort war bereits geschrieben." "Zwei der Bände gelangten in den Besitz der Bibliothek des Pädagogiums der evangelischen Brüder-Unität zu Niesky, die übrigen nebst dem umfangreichen Herbar des Verstorbenen wurden der Naturforschenden Gesellschaft zu Görlitz überwiesen" (E. Barber: 1898, 344)

Früher: Flora von Zeist und Umgebung (Manuskript) Ms in UA als Ergänzung 1831 zur Pflanzensammlung in NatKab (Niesky) UA.Cim.II.4 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Manuskripte im Senckenberg Museum für Naturkunde Görlitz:Aufzeichnungen über Rosa, Rubus, Hieracium / Herrnhut : , 1890, ungez. S. handschriftl.: BOT 2002/0028`**
  - Causing raw value: ` 

Manuskripte im Senckenberg  Museum für Naturkunde Görlitz:
Aufzeichnungen über Rosa, Rubus, Hieracium / Herrnhut : [S.n.], 1890, ungez. S. handschriftl.: BOT 2002/0028 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Katalog des Wenckschen Herbars /Herrnhut : , 1887/88 309 S. handschriftl.: BOT 2002/0026`**
  - Causing raw value: `Katalog des Wenckschen Herbars /Herrnhut : [S.n.], 1887/88 309 S. handschriftl.: BOT 2002/0026 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Pilze : Tl. 1 u. 2 / Herrnhut : Selbstverl., 1877, handschr.: MYK 2001/0355`**
  - Causing raw value: `Pilze : Tl. 1 u. 2 / Herrnhut : Selbstverl., 1877, handschr.: MYK 2001/0355 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Synopsis Ruborum Germaniae / W.D. Focke, Bremen : , 1877, handschr. Auszug von E. Wenck, 20 Bl.: BOT 2002/0027`**
  - Causing raw value: `Synopsis Ruborum Germaniae / W.D. Focke,  Bremen : [S.n.], 1877, handschr. Auszug von E. Wenck, 20 Bl.: BOT 2002/0027 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Herbarverzeichnis / hrsg. von Ed. Wenck, Herrnhut : , 1869, ungez. S. handschriftl.: BOT 2002/0025`**
  - Causing raw value: `Herbarverzeichnis / hrsg. von Ed. Wenck, Herrnhut : [S.n.], 1869, ungez. S. handschriftl.: BOT 2002/0025 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Verzeichnis und Beschreibungen von Pflanzen aus Labrador und Grönland / : , 1857, 32 Hefte mit ungez. S. handschriftl.: BOT 2002/0024`**
  - Causing raw value: `Verzeichnis und Beschreibungen von Pflanzen aus Labrador und Grönland / [S.l.] : [S.n.], 1857,  32 Hefte mit ungez. S. handschriftl.: BOT 2002/0024 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Oberlausitzer Flora : mit Standortangaben I / Herrnhut 1886: 349 S. handschriftl. BOT 2002/0029`**
  - Causing raw value: `Oberlausitzer Flora : mit Standortangaben I / Herrnhut 1886: 349 S. handschriftl. BOT 2002/0029 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Oberlausitzer Flora : mit Standortangaben II / Herrnhut 1886, 185 S. handschriftl.: BOT 2002/0030`**
  - Causing raw value: `Oberlausitzer Flora : mit Standortangaben II / Herrnhut 1886, 185 S. handschriftl.: BOT 2002/0030 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': Oberlausitzer Flora : mit Standortangaben III / Herrnhut 1886, 497 S. handschriftl.: BOT 2002/0031`**
  - Causing raw value: `Oberlausitzer Flora : mit Standortangaben III / Herrnhut 1886, 497 S. handschriftl.: BOT 2002/0031 `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1700000:
  - Error Message: **`LiteratureID must start with 'R': da das die Drei Bände sind, müssen zwei noch in Herrnhut sein!!!`**
  - Causing raw value: `da das die Drei Bände sind, müssen zwei noch in Herrnhut sein!!!`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1700000:
  - Error Message: **`Invalid work id: : „Verzeichnis von Pflanzen von Grönland‘s u. Labrador’s, die v. den dort. Missionsplätzen der Brüder an Br. Wenk, eingesendet wurden – von Br. Wenk zusammgestellt. (UA NB VI.185.4) (should be R-ID, or M-ID)`**
  - Causing raw value: `[Thust]: „Verzeichnis von Pflanzen von Grönland‘s u. Labrador’s, die v. den dort. Missionsplätzen der Brüder an Br. Wenk, eingesendet wurden – von Br. Wenk zusammgestellt. (UA NB VI.185.4) `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1700000:
  - Error Message: **`Invalid work id: E. Barber: "Flora der Oberlausitz preussischen und sächsischen Anteils einschliesslich des nördlichen Böhmens. Auf Grund eigener Beobachtungen unter Berücksichtigung älterer Floristischer Arbeiten zusammengestellt", in: Abhandlungen der naturforschenden Gesellschaft zu Görlitz 22 (1898), S. 337-387, 344. (should be R-ID, or M-ID)`**
  - Causing raw value: `E. Barber: "Flora der Oberlausitz preussischen und sächsischen Anteils einschliesslich des nördlichen Böhmens. Auf Grund eigener Beobachtungen unter Berücksichtigung älterer Floristischer Arbeiten zusammengestellt", in: Abhandlungen der naturforschenden Gesellschaft zu Görlitz 22 (1898), S. 337-387, 344. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1700000:
  - Error Message: **`Invalid work id: Volker Otte: "Exotische Flechten aus der Sammlungstätigkeit der Herrnhuter Brüdergemeine im Görlitzer Herbarium ", in: (Hg.), Sammelband zu Botanik in und um Görlitz und Herrnhuter zu einer Tagung von 2005, nicht erschienen. (should be R-ID, or M-ID)`**
  - Causing raw value: ` 
Volker Otte: "Exotische Flechten aus der Sammlungstätigkeit der Herrnhuter Brüdergemeine im Görlitzer Herbarium ", in:  (Hg.), Sammelband zu Botanik in und um Görlitz und Herrnhuter zu einer Tagung von 2005, nicht erschienen. `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1700000:
  - Error Message: **`Invalid work id: Hardtke (should be R-ID, or M-ID)`**
  - Causing raw value: `Hardtke  `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1700000:
  - Error Message: **`Invalid work id: Restaurierung und Katalogisierung des Herbariums Leiner in Konstanz 2004 (should be R-ID, or M-ID)`**
  - Causing raw value: ` Restaurierung und Katalogisierung des Herbariums Leiner in Konstanz 2004`

### P1710000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1710000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1710000:
  - Error Message: **`LocationID must start with 'L': Gnadenfeld`**
  - Causing raw value: `Gnadenfeld`

- [ ] Error in Col: **Tod - Ort** and row with ID P1710000:
  - Error Message: **`LocationID must start with 'L': Gnadenfeld`**
  - Causing raw value: `Gnadenfeld`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1710000:
  - Error Message: **`Expected 4 parts, got 2: Gnadenfeld; Apotheker`**
  - Causing raw value: `Gnadenfeld; Apotheker  {R0009800}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1710000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1715000

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1715000:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1715000:
  - Error Message: **`Expected 4 parts, got 2: Gnadenfeld; Apotheker`**
  - Causing raw value: `Gnadenfeld; Apotheker  {R0009800}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1715000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1715000:
  - Error Message: **`PersonID must start with 'P': Rudolf Kölbing`**
  - Causing raw value: `Rudolf Kölbing {R0009800} `
  - Full field: _Rudolf Kölbing {R0009800} | 
Gustav Wetschky {R0009800}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1715000:
  - Error Message: **`PersonID must start with 'P': Gustav Wetschky`**
  - Causing raw value: ` 
Gustav Wetschky {R0009800}`
  - Full field: _Rudolf Kölbing {R0009800} | 
Gustav Wetschky {R0009800}_

### P1715500

- [ ] Error in Col: **Angehörige - Anmerkungen** and row with ID P1715500:
  - Error Message: **`Invalid Reference Document value: R0009800} |Vater von P171000 {R0009800 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Sohn von P1715000 {R0009800} |
Vater von P171000 {R0009800}`

- [ ] Error in Col: **Zugehörigkeit Herrnhuter Brüdergemeine** and row with ID P1715500:
  - Error Message: **`Provided string is not in codelist: ja`**
  - Causing raw value: `ja`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1715500:
  - Error Message: **`Expected 4 parts, got 1: Gnadenfeld Apotheker`**
  - Causing raw value: `Gnadenfeld Apotheker {R0009800}`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1715500:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1715500:
  - Error Message: **`PersonID must start with 'P': Rudolf Kölbing`**
  - Causing raw value: `Rudolf Kölbing {R0009800} `
  - Full field: _Rudolf Kölbing {R0009800} |
Christian Gottfried Wetschky  {R0009800}_

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1715500:
  - Error Message: **`PersonID must start with 'P': Christian Gottfried Wetschky`**
  - Causing raw value: `Christian Gottfried Wetschky  {R0009800}`
  - Full field: _Rudolf Kölbing {R0009800} |
Christian Gottfried Wetschky  {R0009800}_

### P1720000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1720000:
  - Error Message: **`LocationID must start with 'L': Paramaribo`**
  - Causing raw value: `Paramaribo `

- [ ] Error in Col: **Tod - Datum** and row with ID P1720000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1948-05-08 00:00:00`**
  - Causing raw value: `1948-05-08 00:00:00`

- [ ] Error in Col: **Wirkungsorte** and row with ID P1720000:
  - Error Message: **`Expected 4 parts, got 1: Juli 1899 Belege aus dem Riesengebierge`**
  - Causing raw value: `Juli 1899 Belege aus dem Riesengebierge `
  - Full field: _Juli 1899 Belege aus dem Riesengebierge |
1899-1905; L2250000; Lehrerseminar (Schüler) {R0003500} | 
1905-1912; L1550000; Knabenanstalt (Lehrer) {R0003500} | 
1912-1948; L1850000; Lateinschule (Lehrer) {R0003500} |
ab 1912 L1500000 [Kleinwelka]?_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1720000:
  - Error Message: **`Expected 4 parts, got 3: 1899-1905; L2250000; Lehrerseminar (Schüler)`**
  - Causing raw value: `1899-1905; L2250000; Lehrerseminar (Schüler) {R0003500} `
  - Full field: _Juli 1899 Belege aus dem Riesengebierge |
1899-1905; L2250000; Lehrerseminar (Schüler) {R0003500} | 
1905-1912; L1550000; Knabenanstalt (Lehrer) {R0003500} | 
1912-1948; L1850000; Lateinschule (Lehrer) {R0003500} |
ab 1912 L1500000 [Kleinwelka]?_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1720000:
  - Error Message: **`Expected 4 parts, got 3: 1905-1912; L1550000; Knabenanstalt (Lehrer)`**
  - Causing raw value: ` 
1905-1912; L1550000; Knabenanstalt (Lehrer) {R0003500} `
  - Full field: _Juli 1899 Belege aus dem Riesengebierge |
1899-1905; L2250000; Lehrerseminar (Schüler) {R0003500} | 
1905-1912; L1550000; Knabenanstalt (Lehrer) {R0003500} | 
1912-1948; L1850000; Lateinschule (Lehrer) {R0003500} |
ab 1912 L1500000 [Kleinwelka]?_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1720000:
  - Error Message: **`Expected 4 parts, got 3: 1912-1948; L1850000; Lateinschule (Lehrer)`**
  - Causing raw value: ` 
1912-1948; L1850000; Lateinschule (Lehrer) {R0003500} `
  - Full field: _Juli 1899 Belege aus dem Riesengebierge |
1899-1905; L2250000; Lehrerseminar (Schüler) {R0003500} | 
1905-1912; L1550000; Knabenanstalt (Lehrer) {R0003500} | 
1912-1948; L1850000; Lateinschule (Lehrer) {R0003500} |
ab 1912 L1500000 [Kleinwelka]?_

- [ ] Error in Col: **Wirkungsorte** and row with ID P1720000:
  - Error Message: **`Expected 4 parts, got 1: ab 1912 L1500000 ?`**
  - Causing raw value: `ab 1912 L1500000 [Kleinwelka]?`
  - Full field: _Juli 1899 Belege aus dem Riesengebierge |
1899-1905; L2250000; Lehrerseminar (Schüler) {R0003500} | 
1905-1912; L1550000; Knabenanstalt (Lehrer) {R0003500} | 
1912-1948; L1850000; Lateinschule (Lehrer) {R0003500} |
ab 1912 L1500000 [Kleinwelka]?_

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1720000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1720000:
  - Error Message: **`PersonID must start with 'P': F.W. Kölbing`**
  - Causing raw value: `F.W. Kölbing {R0009800} `
  - Full field: _F.W. Kölbing {R0009800} |_

- [ ] Error in Col: **Botanik - Foki** and row with ID P1720000:
  - Error Message: **`Invalid Reference Document value: Becker 2005 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: ` Eulen- und Raubvogelernährung, Untersuchungen über Ursprung der Lautäußerung der Bekassine {Becker 2005}`
  - Full field: _Botanik | Eulen- und Raubvogelernährung, Untersuchungen über Ursprung der Lautäußerung der Bekassine {Becker 2005}_

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1720000:
  - Error Message: **`ManuscriptID must start with 'M': im Pfalzmuseum für Naturkunde – POLLICHIA-Museum 67098 Bad Dürkheim und tw. auf Laufwerk als Kopie`**
  - Causing raw value: `im Pfalzmuseum für Naturkunde – POLLICHIA-Museum  67098 Bad Dürkheim  und tw. auf Laufwerk als Kopie`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1720000:
  - Error Message: **`ManuscriptID must start with 'M': Baer nennt ihn 1925 "Lieber Br Wiemann" (Brief vom 22.10.1925, Archiv Pfalzmuseum) - ebenso Fried 1743 - d.h. er war wohl weiterhin Herrnhuter`**
  - Causing raw value: `Baer nennt ihn 1925 "Lieber Br[uder] Wiemann" (Brief vom 22.10.1925, Archiv Pfalzmuseum) - ebenso Fried 1743 - d.h. er war wohl weiterhin Herrnhuter`

- [ ] Error in Col: **Botanik - Manuskripte der Person** and row with ID P1720000:
  - Error Message: **`ManuscriptID must start with 'M': Fried aus Kleinwelka schreibt 1943 mit Verweis auf Max Militzer, dieser wird Wiemann mehr, von der "romantischen Geschichte der Auffindung oder Errettung Deiner Flora schreiben" und dankt für Soende für Klienwelka (Fried an Wieman, 9.1.1943, Archiv Pfalzmuseum)`**
  - Causing raw value: `Fried aus Kleinwelka schreibt 1943 mit Verweis auf Max Militzer, dieser wird Wiemann mehr, von der "romantischen Geschichte der Auffindung oder Errettung Deiner Flora schreiben" und dankt für Soende für Klienwelka (Fried an Wieman, 9.1.1943, Archiv Pfalzmuseum)`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1720000:
  - Error Message: **`LiteratureID must start with 'R': Mit-Herausgeber der ersten in den "Görlitzer Abhandlungen" erschienenen Arbeit über Raubvogel- und Eulenernährung (Becker 2005)`**
  - Causing raw value: `Mit-Herausgeber der ersten in den "Görlitzer Abhandlungen" erschienenen Arbeit über Raubvogel- und Eulenernährung  (Becker 2005)`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1720000:
  - Error Message: **`LiteratureID must start with 'R': Flora von Königsfeld (Becker 2005) (Gottfried David Wiemann: Zur Geographie, Geologie und Flora von Königsfeld (in Baden). Führer für Königsfeld, KönigsfeId,: W. Dahl 1913)`**
  - Causing raw value: `Flora von Königsfeld  (Becker 2005) (Gottfried David Wiemann: Zur Geographie, Geologie und Flora von Königsfeld (in Baden). Führer für Königsfeld, KönigsfeId,: W. Dahl 1913)`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1720000:
  - Error Message: **`LiteratureID must start with 'R': D. Wiemann: "Unser Herbstspaziergang. (Botanische Beobachtungen)", in: Natur und Schule 2 (1906), S. 360-365`**
  - Causing raw value: ` 
D. Wiemann: "Unser Herbstspaziergang. (Botanische Beobachtungen)", in: Natur und Schule 2 (1906), S. 360-365`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1720000:
  - Error Message: **`LiteratureID must start with 'R': Gottfried David Wiemann: "Botanisches von der Donauversickerung", in: Aus der Heimat. Eine Naturwissenschaftliche Zeitschrift, Organ des Deutschen Lehrer-Vereins für Naturkunde, 1912, S. 78-80.`**
  - Causing raw value: `Gottfried David Wiemann: "Botanisches von der Donauversickerung", in: Aus der Heimat. Eine Naturwissenschaftliche Zeitschrift, Organ des Deutschen Lehrer-Vereins für Naturkunde, 1912, S. 78-80.`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1720000:
  - Error Message: **`Invalid work id: UA, MD 1125, UA. R.22.170.8Alfred Blaufuss: "Aus dem Leben und Werk David Wiemanns", in: Mitteilungen der Pollichia III. Reihe 20. Band (1793), S. 64 - 77.Hans Christoph Stamm: "Otto Uttendörfer und seine Arbeitsgemeinschaft zur Erforschung der Ernährungsbiologie bei Greifvögeln und Eulen - mit Auszügen aus den Lebenserinnerungen Uttendörfers", in: Mitteilungen des Vereins Sächsischer Ornithologen 8 (2001), S. 577-603, 582Sein Herbarium und der komplette Nachlass von Wiemann im: Pfalzmuseum für Naturkunde – POLLICHIA-Museum Hermann-Schäfer-Straße 17 (should be R-ID, or M-ID)`**
  - Causing raw value: ` UA, MD 1125, UA. R.22.170.8
Alfred Blaufuss: "Aus dem Leben und Werk David Wiemanns", in: Mitteilungen der Pollichia III. Reihe 20. Band (1793), S. 64 - 77.
Hans Christoph Stamm: "Otto Uttendörfer und seine Arbeitsgemeinschaft zur Erforschung der Ernährungsbiologie bei Greifvögeln und Eulen - mit Auszügen aus den Lebenserinnerungen Uttendörfers", in: Mitteilungen des Vereins Sächsischer Ornithologen 8 (2001), S. 577-603, 582
Sein Herbarium und der komplette Nachlass von Wiemann  im: Pfalzmuseum für Naturkunde – POLLICHIA-Museum Hermann-Schäfer-Straße 17 `

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1720000:
  - Error Message: **`Invalid work id: 67098 Bad DürkheimDie Feldtagebücher erst nach 1920. Ob im Nachlass direkte Zeugnisse seiner Herrnhuter Zeit sind, wurde nicht erruiert. Die Korrerspondenten sind zum Großteil nicht Herrnhuter Provenienz, dort finden sich aber auch die unter der Sp. Herrnhuter Kontakte erwähnten Personen mit relativ geringer Überlieferung von je einem Brief ,außer W. Baer mit 4 Schreiben. Diese könnten auch vor 1920 verfasst sein. (should be R-ID, or M-ID)`**
  - Causing raw value: ` 67098 Bad Dürkheim
Die Feldtagebücher erst nach 1920. Ob im Nachlass direkte Zeugnisse seiner Herrnhuter Zeit sind, wurde nicht erruiert. Die Korrerspondenten sind zum Großteil nicht Herrnhuter Provenienz, dort finden sich aber auch die unter der Sp. Herrnhuter Kontakte erwähnten Personen mit relativ geringer Überlieferung von je einem Brief ,außer W. Baer mit 4 Schreiben. Diese könnten auch vor 1920 verfasst sein.`

### P1730000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1730000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Tod - Ort** and row with ID P1730000:
  - Error Message: **`LocationID must start with 'L': Herrnhut`**
  - Causing raw value: `Herrnhut`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1730000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Kontakt - Mit Herrnhutern** and row with ID P1730000:
  - Error Message: **`PersonID must start with 'P': Hasse, Ernst Reichel, Christian Gottfried Wetschky Eduard Wenck`**
  - Causing raw value: `Hasse, Ernst Reichel, Christian Gottfried Wetschky Eduard Wenck {R0009800}`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1730000:
  - Error Message: **`LiteratureID must start with 'R': WOLLE, J., AND A. L. HUEBNER. 1839. Catalogue of botanicalspecimens collected by J. Wolle and A. L. Huebner during theyear 1837 in the vicinity of Bethlehem and other parts ofNorthampton County, Pennsylvania, in the order as they werefound in bloom. Am. J. Sci. 37:310–320.`**
  - Causing raw value: `WOLLE, J., AND A. L. HUEBNER. 1839. Catalogue of botanical
specimens collected by J. Wolle and A. L. Huebner during the
year 1837 in the vicinity of Bethlehem and other parts of
Northampton County, Pennsylvania, in the order as they were
found in bloom. Am. J. Sci. 37:310–320.`

### P1740000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1740000:
  - Error Message: **`LocationID must start with 'L': Pennsylvania`**
  - Causing raw value: `Pennsylvania`

- [ ] Error in Col: **Tod - Ort** and row with ID P1740000:
  - Error Message: **`LocationID must start with 'L': Pennsylvania`**
  - Causing raw value: `Pennsylvania`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1740000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1740000:
  - Error Message: **`LiteratureID must start with 'R': WOLLE, F. 1884. Desmids of the United States. Moravian Pub.Office, Bethlehem, PA. 168 p.WOLLE, F. 1887. Fresh-Water Algae of the United States. 2 vols.Comenius Press, Bethlehem, PA. 364, 157 p.WOLLE, F. 1890. Diatomaceae of North America. Comenius Press, Bethlehem, PA. 47 p.`**
  - Causing raw value: `WOLLE, F. 1884. Desmids of the United States. Moravian Pub.
Office, Bethlehem, PA. 168 p.
WOLLE, F. 1887. Fresh-Water Algae of the United States. 2 vols.
Comenius Press, Bethlehem, PA. 364, 157 p.
WOLLE, F. 1890. Diatomaceae of North America. Comenius Press, Bethlehem, PA. 47 p. `

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1740000:
  - Error Message: **`LiteratureID must start with 'R': "Whitford (1968) described how he hiredwidows of Moravian clergymen to hand tint with water colors the plates of his works for a payment of 10 centsper plate." Troyer 2009,4`**
  - Causing raw value: ` 
"Whitford (1968) described how he hired
widows of Moravian clergymen to hand tint with water colors the plates of his works for a payment of 10 cents
per plate." Troyer 2009,4`

### P1750000

- [ ] Error in Col: **Wirkungsorte** and row with ID P1750000:
  - Error Message: **`LocationID must start with 'L': Antigua`**
  - Causing raw value: ` 1844/1847;  Antigua;; {R0009100} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1750000:
  - Error Message: **`LocationID must start with 'L': Honduras?`**
  - Causing raw value: ` 1855; Honduras?;; {R0009100} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1750000:
  - Error Message: **`Invalid Reference Document value: 0009100 (should be URL, R-ID, or M-ID)`**
  - Causing raw value: ` 1858; Nordamerika;; {0009100} `

- [ ] Error in Col: **Wirkungsorte** and row with ID P1750000:
  - Error Message: **`Cannot parse as date or period: '1858-1864'`**
  - Causing raw value: `1858-1864;L0400000;; {R0009100}`

- [ ] Error in Col: **Kontakt - Mit Nicht-Herrnhutern** and row with ID P1750000:
  - Error Message: **`Invalid Reference Document value: Xenia orchidacea : Beiträge zur Kenntniss der Orchideen (should be URL, R-ID, or M-ID)`**
  - Causing raw value: `Reichenbach, Heinrich Gustav {Xenia orchidacea : Beiträge zur Kenntniss der Orchideen}`

### P1760000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1760000:
  - Error Message: **`LocationID must start with 'L': Zwickau`**
  - Causing raw value: `Zwickau`

- [ ] Error in Col: **Tod - Ort** and row with ID P1760000:
  - Error Message: **`LocationID must start with 'L': Sarepta`**
  - Causing raw value: `Sarepta`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1760000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1770000

- [ ] Error in Col: **Links - Bionomia** and row with ID P1770000:
  - Error Message: **`URL is not valid: nein (2024-12-17)`**
  - Causing raw value: `nein (2024-12-17)`

- [ ] Error in Col: **Geburt - Ort** and row with ID P1770000:
  - Error Message: **`LocationID must start with 'L': Düsseldorf`**
  - Causing raw value: `Düsseldorf`

- [ ] Error in Col: **Tod - Datum** and row with ID P1770000:
  - Error Message: **`Invalid ISO8601-2_Date format: 1916-02-02 00:00:00`**
  - Causing raw value: `1916-02-02 00:00:00`

- [ ] Error in Col: **Tod - Ort** and row with ID P1770000:
  - Error Message: **`Invalid format for LocationID: Limburg`**
  - Causing raw value: `Limburg`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1770000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

### P1780000

- [ ] Error in Col: **Geburt - Ort** and row with ID P1780000:
  - Error Message: **`LocationID must start with 'L': Gnadenberg`**
  - Causing raw value: `Gnadenberg`

- [ ] Error in Col: **Tod - Ort** and row with ID P1780000:
  - Error Message: **`LocationID must start with 'L': Niesky`**
  - Causing raw value: `Niesky`

- [ ] Error in Col: **Herrnhuter Lebenslauf** and row with ID P1780000:
  - Error Message: **`Invalid work id: offen (should be R-ID, or M-ID)`**
  - Causing raw value: `offen`

- [ ] Error in Col: **Botanik - Druckwerke der Person** and row with ID P1780000:
  - Error Message: **`LiteratureID must start with 'R': Wörterbuch und Grammatik der kalmückischen Sprache`**
  - Causing raw value: `Wörterbuch und Grammatik der 
kalmückischen Sprache`

- [ ] Error in Col: **Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere** and row with ID P1780000:
  - Error Message: **`Invalid work id: Karl Christian Traugott Friedemann Göbel: Reise in die Steppen des südlichen Russlands: unternommen von Fr. Goebel in Begleitung der Herren C. Claus und A. Bergmann. Erster Theil , Dorpat: C. A. Kluge 1837, 228 zur entomol. Sammlung (should be R-ID, or M-ID)`**
  - Causing raw value: `Karl Christian Traugott Friedemann Göbel: Reise in die Steppen des südlichen Russlands: unternommen von Fr. Goebel [...] in Begleitung der Herren C. Claus und A. Bergmann. Erster Theil  , Dorpat: C. A. Kluge 1837, 228 zur entomol. Sammlung`

## Manuskripte

### M0005500

- [ ] Error in Col: **Archiv** and row with ID M0005500:
  - Error Message: **`ArchiveID must start with 'A': P0980000`**
  - Causing raw value: `P0980000`

### M0007000

- [ ] Error in Col: **Archiv** and row with ID M0007000:
  - Error Message: **`ArchiveID must start with 'A': P0980000`**
  - Causing raw value: `P0980000`

### M0035000

- [ ] Error in Col: **Archiv** and row with ID M0035000:
  - Error Message: **`ArchiveID must start with 'A': Stadtmuseum Bautzen`**
  - Causing raw value: `Stadtmuseum Bautzen`

## Orte

### L1101000

- [ ] Error in Col: **Wikidata** and row with ID L1101000:
  - Error Message: **`URL is not valid: w.wikidata.org/wiki/Q570684`**
  - Causing raw value: `w.wikidata.org/wiki/Q570684`

## Sammlungen

### C-leiner

- [ ] Error in Col: **Teilsammlung von** and row with ID C-leiner:
  - Error Message: **`CollectionID must start with 'C': Städtische Museen Konstanz`**
  - Causing raw value: `Städtische Museen Konstanz`
