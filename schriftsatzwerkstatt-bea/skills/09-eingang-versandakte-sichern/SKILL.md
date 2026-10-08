---
name: 09-eingang-versandakte-sichern
description: "Nach realem beA-Versand mit Nachricht, Exportprotokoll oder Eingangsbestätigung: prüft Gericht, Aktenzeichen, Zeitstempel, Dateiliste, Fehler und Hashstand. Sichert Versandfassung, erstellt Eingangsvermerk und bereitet DMS-Ablage sowie Wiedervorlage vor. Der Status gesendet allein belegt keinen Gerichtseingang."
---

# Eingang prüfen und Versandakte sichern

## Zweck und Anwendungsfall

Dieser Skill schließt die technische Werkstatt nach dem von einer realen Person ausgelösten Versand. Maßgeblich ist die automatisierte Eingangsbestätigung des Gerichts, nicht allein die Anzeige `gesendet` im Ausgangssystem.

## Eingaben

- gesendete Nachricht beziehungsweise Export aus beA/Kanzleisystem.
- automatisierte Eingangsbestätigung.
- finaler Versandauftrag und `versandmanifest.csv`.
- Upload-PDFs und deren Hashwerte.
- Ziel-DMS/Akten-ID und Wiedervorlageregel.

## Ablauf / Checkliste

1. Gesendete Nachricht und Eingangsbestätigung unverändert sichern.
2. Gericht, SAFE-Empfänger, Aktenzeichen/Neueingang, Betreff, Übermittlungs- und Eingangszeitpunkt vergleichen.
3. Bestätigte Dateinamen und Dateizahl gegen Versandauftrag und Manifest prüfen.
4. Fehlermeldung, Warnung, abgewiesene Datei oder Größenabweichung rot markieren.
5. Soweit das System Hash-/Prüfdaten liefert, mit dem finalen Manifest abgleichen. Andernfalls Versandpaket samt Manifest unverändert archivieren. Die Aktenkette muss Quelle, geprüfte Renderfassung, Upload-Datei und bestätigtes Empfangsartefakt unterscheidbar halten.
6. Einreichungsstatus nur bei plausibler automatisierter Eingangsbestätigung auf `EINGANG TECHNISCH BESTÄTIGT` setzen.
7. Fehlt die Bestätigung oder ist ein Dokument ungeeignet, sofort verantwortliche Person informieren. Erstfassung, Meldung, Korrekturfassung und Zeitpunkte getrennt sichern; keine stille Überschreibung.
8. DMS-Ablage vorbereiten: gesendete Nachricht, Upload-PDFs, Manifest, Prüfprotokoll, Versandauftrag, Validatorprotokoll, Eingangsbestätigung und Fehlerprotokolle. Empfangsartefakte unverändert und mit Hash sichern.
9. Aktenzeichenrücklauf, gerichtliche Kostenanforderung, Zustellung oder sonstige Folge als konkrete Wiedervorlage erfassen.
10. Eingangsvermerk nach der [Vorlage](../../templates/eingangsvermerk.md) mit realer prüfender Person und Zeitpunkt abschließen.

## Quellenpflicht

Der Eingangszeitpunkt und der Umgang mit ungeeigneten Dokumenten folgen dem [ERV-Versandstandard](../../references/erv-versandstandard.md) mit den amtlichen Verweisen auf § 130a Abs. 5 und 6 ZPO; Archiv- und Hashkette folgen [Inhaltstreue und Renderabgleich](../../references/inhaltstreue-und-renderabgleich.md), die Abschlusskontrollen dem [100-Punkte-Fehlerkatalog](../../references/100-punkte-fehlerkatalog.md). Keine Rechtsprechungsanker.

## Ausgabeformat

1. Eingangsvermerk mit Gericht, Aktenzeichen, Zeitstempel und Prüfperson.
2. Abgleichstabelle Soll-Dateien zu bestätigten Dateien.
3. Fehler-/Abweichungsliste mit sofortigem nächsten Schritt.
4. DMS-Ablageplan mit unveränderbaren Artefakten.
5. Wiedervorlage mit Anlass und Datum.

Der Eingangsvermerk wird vollständig ausformuliert. Ohne automatisierte Bestätigung darf kein erfolgreicher Gerichtseingang behauptet werden.

## Beispiele

- Ausgang zeigt `gesendet`, Eingangsbestätigung fehlt: rot und sofortige Nachprüfung.
- Bestätigung nennt 12 statt 13 Dateien: rot; Dateiliste und Nachricht prüfen.
- Gericht und Dateiliste stimmen, Zeitstempel vorhanden: technischen Eingang dokumentieren und DMS-Paket ablegen.
