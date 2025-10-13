# Datenmodell – Manuskripte

## Präambel


Diese Tabelle beschreibt die Spalten der Tabelle Manuskripte. Im Kontext dieses Projekts bezeichnet ein Manuskript, einen handgeschriebenen Text. 


__In diesem Schema sind die Felder *ID* und *Archiv* und *Signatur* erforderlich, alle anderen sind optional. Jedoch gilt immer: Je mehr Felder ausgefüllt sind, desto besser.__

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)



## Felder (Spalten)



### ID
*ID*, **erforderlich**  

Eindeutiger Identifier. Beginnt mit dem Buchstaben `M` (Manuscript) und ist gefolgt von sieben Ziffern.  
- `M0000010`  
- `M0020000`

### Archiv
*ID*, **erforderlich**

ID (aus er Archive-Tabelle) des Archivs, in dem das Manuskript aufbewahrt wird. 
- `A0001000`

### Signatur
*String*, **erforderlich**

Signatur/Bestandsangabe, unter der die Quelle im Archiv auffindbar ist.
- `ThS.A.132.a`
- `Sig. 1944`

### Titel
*String*, **erforderlich**

Vollständige Bezeichnung der Quelle. Kann Autor:innen, Entstehungsort und Datum enthalten. Die Struktur des Titels ist nicht vorgegeben, jedoch gilt folgende Empfehlung: 
`<Autor:innen (Vornamen Nachnamen), semikolongetrennt>: <Titel>, <Entstehungsort> (<Entstehungsdatum>)`.
- `Johann Jakob Bossart: Tagebuch Botanischer Exkursionen (1766)`
- `Philip Christian Gottlieb Reuter: Hortus Medicus (1761)`


### Permalink
*URL*  

Stabiler Link zu einem Digitalisat oder Katalogeintrag, falls verfügbar.  

### Beschreibung
*String*

Weitere Informationen zur Quelle. Was ist ihr Inhalt? Weist sie Besonderheiten auf? Gibt es vielleicht Abschriften?
