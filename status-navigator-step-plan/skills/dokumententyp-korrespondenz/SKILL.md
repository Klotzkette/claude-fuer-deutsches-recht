---
name: dokumententyp-korrespondenz
description: "Erkennt Korrespondenz: E-Mails, Briefe, Aktenvermerke, Faxprotokolle, Telefonnotizen. Erfasst Absender, Empfaenger, Datum, Betreff und Bezug zu Vertraegen und Erklaerungen."
---

# Dokumententyp Korrespondenz

## Rolle und Fokus
Erkennt Korrespondenz: E-Mails, Briefe, Aktenvermerke, Faxprotokolle, Telefonnotizen. Erfasst Absender, Empfaenger, Datum, Betreff, Bezug.

## Vorgehen

1. **Trennung Erklaerung vs. Korrespondenz** — Eine Kuendigungsmail ist Erklaerung, eine Antwortmail meist Korrespondenz; im Zweifel als Erklaerung behandeln.
2. **Threading rekonstruieren** — E-Mail-Threads chronologisch sortieren; Anhaenge separat erfassen.
3. **Bezug auf Vertraege herstellen** — Welche Klausel, welche Erklaerung, welche Frist ist Gegenstand?
4. **Aktennotiz-Qualitaet** — Wer hat den Vermerk verfasst, wann, mit welchen Anwesenden?
5. **Beweiseignung notieren** — Brief mit Empfangsbestaetigung, E-Mail ohne Signatur, Fax mit OK-Protokoll.

## Anwendungsbeispiel
E-Mail-Korrespondenz LEAG vom 19.05.2026: Drohung mit Pachtvertragskuendigung wegen verspaeteter Vorlage der BImSchG-Genehmigungsunterlagen. Thread enthaelt vier Mails, einen Anhang (Auflistung der vermissten Unterlagen), keine Empfangsbestaetigung; im Bezug steht § 12 Abs. 3 Pachtvertrag (Beibringungspflicht).

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Schreiben oder Korrespondenz
- Thread-Mapping in Anmerkungsspalte
- Querverweis an `dokumententyp-erklaerungen` falls Korrespondenz tatsaechlich eine Erklaerung enthaelt
