# Konvertierungsprotokoll

## 1. Laufkopf

| Feld | Wert |
|---|---|
| Paket-ID | [eintragen] |
| Projektordner | [relativer Pfad] |
| Laufzeit | [Beginn und Ende] |
| Maximal parallele Arbeitsaufträge | [1 bis 4] |

## 2. Quellen und Delta-Entscheidung

| Quelle | SHA-256 Quelle | Format | Größe | Delta | Grund |
|---|---|---|---:|---|---|
| [relativer Pfad] | [64 Hexzeichen] | [Format] | [Bytes] | [unverändert/geändert/neu/fehlt/unklar] | [eintragen] |

## 3. Konvertierungen

| Quelle | Ziel-Arbeitskopie | Seiten | Sichtstatus | Ergebnis |
|---|---|---:|---|---|
| [eintragen] | [relativer Pfad] | [Zahl] | [grün/gelb/rot] | [neu/wiederverwendet/gestoppt] |

| Quelle | Werkzeug und Version | Profil | SHA-256 Ausgabe | Delta-Entscheidung |
|---|---|---|---|---|
| [eintragen] | [eintragen] | [Export/OCR/Kennzeichnung] | [64 Hexzeichen] | [Grund] |

Eine Arbeitskopie darf nur als `wiederverwendet` gelten, wenn Quellhash, Profil, Werkzeugversion, Ausgabehash und früherer grüner Sichtstatus exakt übereinstimmen. Der finale Paketcheck bleibt unabhängig davon Pflicht.

## 4. Abweichungen

| Datei/Seite | Befund | Status | Nächster Schritt |
|---|---|---|---|
| [eintragen] | [eintragen] | [gelb/rot] | [konkret eintragen] |
