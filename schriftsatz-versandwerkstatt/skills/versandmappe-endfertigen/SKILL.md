---
name: versandmappe-endfertigen
description: "Macht einen fertigen Schriftsatz mit gemischten Anlagen technisch versandbereit: PDF-Konvertierung, Anlagenstempel, Dateinamen, Paketgrenzen und Signaturroute. Liefert getrennte Versanddateien und einen Prüfbericht; ersetzt keine inhaltliche Rechtsprüfung und versendet nichts."
---

# Versandmappe endfertigen

## 1. Einsatz

Nutze diesen Skill als Standardroute, sobald der Nutzer einen fertigen oder nahezu fertigen Schriftsatz und einen Ordner mit Anlagen für die elektronische Gerichtseinreichung vorbereitet haben will. Nutze ihn auch bei Formulierungen wie „mach versandfertig“, „alles liegt im Ordner“, „PDF-Paket“, „Anlagen stempeln“ oder „beA-Mappe“.

Keine inhaltliche Rechtsprüfung eröffnen. Keine Rechtsprechung recherchieren. Den Schriftsatz nicht neu schreiben, solange der Nutzer das nicht ausdrücklich verlangt.

## 2. Direktstart

Wenn ein Ordner oder Dateien vorliegen, beginne ohne Interview:

1. Dateinamen und Formate im freigegebenen Ordner inventarisieren, ohne Originale zu verändern. Bei großen Ablagen zuerst Schriftsatzfassungen und darin zitierte Anlagen auswählen, nicht jede Datei vollständig laden.
2. wahrscheinlichstes Hauptdokument nach Dateiname, Änderungsdatum und Inhalt erkennen.
3. Anlagenkennungen aus Schriftsatz und Dateinamen abgleichen.
4. sofort eine Produktionsmatrix mit Status `bereit`, `prüfen`, `fehlt` oder `stop` ausgeben.
5. nur Angaben nachfragen, die sich nicht aus dem Material ergeben und den nächsten Schritt sperren.

Blockierende Angaben sind Empfängergericht, Aktenzeichen oder Neueingang, Frist, gewünschter Nummernkreis, verantwortender Anwalt, tatsächlicher Versender und Signaturroute. Fasse offene Punkte in höchstens zwei Fragen zusammen.

## 3. Produktionslauf

1. `ordneraufnahme-und-produktionsmatrix` für Inventar, Fassungen und Konflikte.
2. `hauptdokument-pdf-endfertigen` für die unveränderte finale Schriftsatz-PDF.
3. `anlagen-konvertieren-und-sichtpruefen` für Office, Tabellen, Bilder, E-Mail und Textformate.
4. `anlagen-nummerieren-und-stempeln` für K, B, AST oder AG und den Stempel auf jeder Seite.
5. `dateinamen-und-paketgrenzen-pruefen` für ASCII-Namen, 80-Zeichen-Profil und Paketierung.
6. `signaturweg-und-absender-pruefen` für verantwortende Person, Versender und Formroute.
7. `versandfreigabe-und-eingang-sichern` für Schlusskontrolle und Eingangsnachweis.
8. Nur bei technischer Störung oder gerichtlichem Formhinweis `stoerung-und-nachreichung-dokumentieren` zuschalten.

Arbeite die Schritte in einem Durchgang ab. Wiederhole keine bereits aus Dateien beantwortete Frage.

## 4. Produktionsmatrix

| Position | Quelle | Zielformat | Anlagenkennung | Seiten | Sichtkontrolle | Versandname | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | Datei und Fassung | PDF | keine | Zahl | offen oder geprüft | `00_...pdf` | Status |
| Anlage | Datei | PDF | K/B/AST/AG | Zahl | offen oder geprüft | `01_...pdf` | Status |

Kennzeichne jede automatische Konvertierung bis zur Sichtkontrolle als `prüfen`. Aus Dateierweiterung oder erfolgreichem Programmende folgt noch keine inhaltlich richtige Wiedergabe.

## 5. Werkzeuglauf

Nutze nach Sichtung das mitgelieferte Werkzeug `werkzeuge/build_versandmappe.py`. Verwende `--strict`. Arbeite in einem neuen Zielordner und überschreibe niemals Originale. Übergib Signaturroute, verantwortende Person und Versender ausdrücklich.

Das Werkzeug darf nur dann als technisch erfolgreich gelten, wenn:

1. der Prozess mit Status null endet,
2. keine Stop-Befunde im Preflight stehen,
3. jede erzeugte PDF geöffnet und visuell geprüft wurde,
4. Seitenzahlen und erwartete Dokumentgrenzen stimmen,
5. die Versanddateien dem Anlagenverzeichnis entsprechen.

Office-Dateien werden mit einem eigenen temporären Profil konvertiert. Nach 120 Sekunden wird die betroffene Konvertierung abgebrochen; unter Linux und macOS werden auch die zugehörigen Kindprozesse beendet. Eine alte PDF im Zielordner zählt nicht als neue Ausgabe. Andere lesbare Anlagen dürfen weiter vorbereitet werden, aber die fehlgeschlagene Datei bleibt ein Stop-Befund. Wiederhole denselben fehlgeschlagenen Aufruf nicht unverändert in einer Schleife: benenne Quelldatei und Fehler und fordere für diese Anlage eine reparierte Datei oder einen manuell erzeugten PDF-Export an.

## 6. Ausgabe

Liefere:

```text
ausgang/
  versandfertig/
    00_..._Schriftsatz_....pdf
    01_..._AnlageK1_....pdf
  intern/
    Anlagenverzeichnis.md
    Anlagenverzeichnis.pdf
    Anlagenkonvolut_Prueffassung.pdf
    Versandmanifest.csv
    Versandmanifest.json
    Preflight-Bericht.md
    Freigabevermerk.md
    Eingangskontrolle.md
```

`intern/` wird nicht versandt, sofern sein Inhalt nicht ausdrücklich eingereicht werden soll.

## 7. Stop-Regeln

Stoppe die Freigabe bei unklarem Empfänger, offener Frist, nicht finalem Hauptdokument, unlesbarer oder verschlüsselter PDF, fehlender Anlage, Nummernkollision, ungeklärtem Versender, ungeklärter Signaturroute, fehlender Sichtkontrolle oder überschrittener Paketgrenze. Liefere dann die bereits erzeugbaren Dateien plus eine kurze, priorisierte Stop-Liste. Löse niemals selbst einen Versand aus.
