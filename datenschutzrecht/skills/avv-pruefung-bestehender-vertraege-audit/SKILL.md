---
name: avv-pruefung-bestehender-vertraege-audit
description: "Prüfung bestehender AVV-Vertraege Vendor-Inventur AVV-Audit und Vertragsfolgemanagement. Behandelt die systematische Durchsicht eines AVV-Bestands die Identifikation veralteter Klauseln SCC-Altmuster fehlender DPF-Bezug und sub-AV-Listenpflege. Output: Audit-Bericht und Vertragsverbesserungsplan."
---

# AVV-Audit – Prüfung bestehender Verträge

## Zweck / Purpose

Systematische Inventur und Prüfung bestehender Auftragsverarbeitungsvertraege auf Aktualitaet, Vollstaendigkeit der Pflichtinhalte, Sub-AV-Pflege und Drittlandbezug. Purpose (EN): Vendor inventory and audit of existing DPAs.

## Wann dieses Modul hilft

- Mandant hat AVV-Bestand und will im Rahmen eines Compliance-Programms prüfen.
- Aufsichtsbehoerde hat eine Prüfung angekuendigt und der AVV-Bestand muss verteidigungsfaehig sein.
- Nach einer Datenpanne oder einem Aufsichtsanlass ist der AVV-Bestand systematisch nachzuziehen.
- Bei Unternehmenskauf (M&A) ist der AVV-Bestand Teil der Due Diligence.

## Rechtlicher Rahmen

- Art. 28 DSGVO – Pflicht zum AVV.
- Art. 30 DSGVO – Verarbeitungsverzeichnis.
- Art. 32 DSGVO – TOM (regelmaessig Anlage zum AVV).
- Art. 44 bis 49 DSGVO – Drittlandtransfer.
- Beschluss (EU) 2021/914 – SCC seit 27.06.2021; Altmuster (2001/497/EG, 2004/915/EG, 2010/87/EU) sind seit 27.12.2022 für Altbestand abgeloest.
- Beschluss (EU) 2023/1795 – DPF seit 10.07.2023.

## Ablauf / Checkliste

1. **Inventur.**
 - Vendor-Liste (Lieferanten mit Datenverarbeitung).
 - AVV-Status pro Vendor: vorhanden / nicht vorhanden / unklar.
 - Vertragsdatum, Vertragsversion.
 - Verarbeitungsumfang, Datenkategorien, Drittlandbezug.

2. **Rollenpruefung.**
 - Pro Vendor: ist die Rollenzuordnung korrekt (Art. 28 versus Art. 26 versus eigene Verantwortlichkeit)?
 - Querverweis: avv-rolemix-getrennt-vs-gemeinsam-verantwortlich.

3. **Pflichtinhalte-Check.**
 - Acht Pflichtklauseln nach Art. 28 Abs. 3 lit. a bis h DSGVO vollstaendig?
 - Rahmenangaben (Gegenstand, Dauer, Art, Zweck, Datenarten, Betroffene) konkret?
 - TOM-Anlage aktuell und konkret?
 - Querverweis: avv-art-28-mindestinhalte-checkliste.

4. **Sub-AV-Pflege.**
 - Liste vorhanden und aktuell?
 - Wechselbenachrichtigungsverfahren funktioniert?
 - Drittland-Sub-AV identifiziert und abgesichert?

5. **Drittlandbezug.**
 - Aktuelle SCC nach Beschluss (EU) 2021/914 oder noch Altmuster?
 - DPF-Listing aktuell?
 - TIA vorhanden und aktuell?

6. **Aktualitaet der TOM-Anlage.**
 - Letzte Prüfung?
 - Branchenuebliche Standards (ISO 27001, BSI C5, SOC 2) referenziert?
 - Pflichtmindestmassnahmen aus Art. 32 DSGVO abgedeckt?

7. **Verarbeitungsverzeichnis Art. 30 DSGVO.**
 - AVV-Vendoren im Verzeichnis dokumentiert?
 - Konsistenz zwischen Verzeichnis und AVV?

8. **Audit-Bericht.**
 - Bewertungsmatrix pro Vendor (Ampel: rot / orange / gelb / gruen).
 - Maßnahmenplan mit Fristen.
 - Eskalationsverfahren bei nicht behebbaren Maengeln.

## Mustertext / Template

AVV-Audit-Matrix-Vorlage:

```
AVV-Audit Bericht – Stand [DATUM]

Vendor: [NAME]
Vertragsstand: [DATUM, VERSION]
Verarbeitungsumfang: [BESCHREIBUNG]
Drittlandbezug: [JA/NEIN, LAND]

Pruefdimension | Status | Befund / Massnahme
-------------------------------------------------|--------|-----------------------------
Rollenzuordnung (Art. 28 / 26 / sep.) | [g/y/o/r] | [...]
Pflichtangaben Art. 28 Abs. 3 Satz 2 DSGVO | [g/y/o/r] | [...]
lit. a Weisungsgebundenheit | [g/y/o/r] | [...]
lit. b Vertraulichkeit | [g/y/o/r] | [...]
lit. c TOM Art. 32 DSGVO | [g/y/o/r] | [...]
lit. d Sub-AV Art. 28 Abs. 2 und 4 | [g/y/o/r] | [...]
lit. e Unterstuetzung Betroffenenrechte | [g/y/o/r] | [...]
lit. f Unterstuetzung Art. 32-36 | [g/y/o/r] | [...]
lit. g Loeschung / Rueckgabe | [g/y/o/r] | [...]
lit. h Audit / Inspektion | [g/y/o/r] | [...]
SCC Stand Beschluss (EU) 2021/914 | [g/y/o/r] | [...]
DPF (sofern US-Anbieter) | [g/y/o/r] | [...]
TIA (sofern Drittland) | [g/y/o/r] | [...]
TOM-Anlage aktuell | [g/y/o/r] | [...]
Art. 30 DSGVO-Verzeichnis konsistent | [g/y/o/r] | [...]

Gesamtbewertung Vendor: [g/y/o/r]
Empfohlene Massnahme: [Verlaengern / Nachverhandeln / Beenden]
Frist: [DATUM]
```

## Typische Drafting-Fehler

- AVV-Bestand wird nur per Stichprobe geprueft – für aufsichtsbehoerdliche Prüfung unzureichend.
- Altbestand mit SCC-Altmustern (2001/497/EG, 2010/87/EU) nicht umgestellt.
- DPF-Listing nicht periodisch geprueft.
- TOM-Anlage Stand 2018 ohne Aktualisierung.
- Sub-AV-Liste wird nicht gepflegt – Versionskonflikt zwischen Vendor-Webseite und Vertrag.
- Verarbeitungsverzeichnis Art. 30 DSGVO und AVV-Bestand laufen auseinander.
- Bei M&A: AVV-Bestand des Targets nicht in Due Diligence gewuerdigt.

## Quellen Stand 06/2026

- Art. 28, Art. 30, Art. 32 DSGVO.
- Beschluss (EU) 2021/914 – SCC seit 27.06.2021.
- Beschluss (EU) 2023/1795 – DPF seit 10.07.2023.
- EDSA-Leitlinien 07/2020 (Final 07.07.2021).
- EDSA-Empfehlungen 01/2020 (Version 2.0 Juni 2021).
- Zitierweise: `../../../references/zitierweise.md`.
