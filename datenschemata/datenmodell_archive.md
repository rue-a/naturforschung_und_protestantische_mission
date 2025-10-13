# Datenmodell – Manuskripte

## Präambel


Diese Tabelle beschreibt die Spalten der Tabelle Archive. 

__In diesem Schema sind die Felder *ID* und *Name* erforderlich, alle anderen sind optional. Jedoch gilt immer: Je mehr Felder ausgefüllt sind, desto besser.__

## Datentypen

[Die Datentypen sind hier definiert](./datentypen.md)



## Felder (Spalten)

### ID
*ID*, **erforderlich**  

Eindeutiger Identifier. Beginnt mit dem Buchstaben `A` (Archive) und ist gefolgt von sieben Ziffern.  
- `A0000100`  
- `A0000300`

### Name
*String*, **erforderlich**

Name des Archivs. 
- `Unitätsarchiv Herrnhut`
- `Moravian Archives`


### Abkürzungen
*List of Strings*

Eine oder mehrere Abküzungen des Archivs.
- `UA`


### Link
*String*

Link zur Website des Archivs.
- `https://www.unitaetsarchiv.de/`
- `https://moravianarchives.org/`
