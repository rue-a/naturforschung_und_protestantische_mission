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
*String*, **erforderlich**

Bezeichnung der Institution, in der die Quelle aufbewahrt wird. Die Struktur der Archivbezeichung ist nicht vorgegeben, jedoch gilt folgende Empfehlung: `<ausgeschriebener Name> (<Abkürzung>)`. 
Es ist darauf zu achten, dass die Bezeichung ein und desselben Archivs in verschiedenen Einträgen konsistent ist. 
- `Unitätsarchiv Herrnhut (UAH)`
- `Moravian Archives, Winston-Salem, N.C.`

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
