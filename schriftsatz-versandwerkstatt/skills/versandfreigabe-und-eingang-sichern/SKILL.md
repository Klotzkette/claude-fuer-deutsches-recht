---
name: versandfreigabe-und-eingang-sichern
description: "Führt die letzte technische und organisatorische Freigabe der Versandmappe durch: öffnet jede Enddatei, gleicht Empfänger, Aktenzeichen, Frist, Schriftsatzfassung, Anlagenfolge, Bytes, Hashes, Signaturroute und Nachrichtenteile ab, erzeugt einen unterschriftsreifen Freigabevermerk und bereitet die Prüfung und Ablage der automatisierten Eingangsbestätigung."
---

# Versandfreigabe und Eingang sichern

## 1. Vorversandkontrolle

Öffne die finalen Dateien aus `versandfertig/`, nicht die Quellen. Prüfe:

1. richtiges Gericht und richtiges Aktenzeichen oder eindeutig `Neueingang`,
2. finale Schriftsatzfassung und sichtbare einfache Signatur,
3. lückenlose Anlagenfolge und Übereinstimmung mit dem Schriftsatz,
4. jede PDF lesbar, unverschlüsselt, druckbar und ohne aktive Inhalte,
5. Dateinamen, Anzahl und Gesamtbytes,
6. verantwortende Person, tatsächlicher Versender und Signaturroute,
7. Frist mit Datum, Uhrzeit und Sicherheitsreserve,
8. bei mehreren Nachrichten Teilfolge und Anlagenbereich.

## 2. Ampel

- `rot`: Formroute, Empfänger, Frist, Hauptdokument oder Anlage offen; keine Freigabe.
- `gelb`: rein organisatorischer Punkt mit ausreichend Zeit offen; Verantwortlichen und Termin nennen.
- `grün`: technische Produktion abgeschlossen und anwaltliche Freigabe dokumentiert; Versand bleibt eine bewusste Handlung außerhalb des Werkzeugs.

## 3. Freigabevermerk

Erzeuge aus `assets/freigabevermerk.md` einen konkreten Vermerk. Keine Kästchen als erledigt markieren, wenn der Prüfschritt nicht tatsächlich erfolgt ist. Nenne Hauptdokument, Anlagenbereich, Dateien, Bytes, Hash des Hauptdokuments, Frist, Signaturroute, Verantwortlichen und Versender.

## 4. Eingangskontrolle

Bereite vor dem Versand eine Zeile je Nachricht vor:

| Teil | Empfänger | Versandzeit | Eingangszeit | Status | Dateien | Prüfender | Frist erledigt |
| --- | --- | --- | --- | --- | --- | --- | --- |

Nach Versand die automatisierte Eingangsbestätigung auf richtigen Empfänger, Zeitstempel, positiven Status und vollständige Nachricht prüfen. Speichere Exportnachricht, Eingangsbestätigung, Versanddateien und Freigabevermerk gemeinsam. Eine Frist darf erst nach positiver Prüfung erledigt werden.

## 5. Ausgabe

Liefere Freigabeampel, ausgefüllten Freigabevermerk, offene Stop-Punkte und Eingangskontrollblatt. Löse niemals selbst einen Versand aus.
