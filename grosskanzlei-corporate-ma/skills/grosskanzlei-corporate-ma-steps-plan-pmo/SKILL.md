---
name: grosskanzlei-corporate-ma-steps-plan-pmo
description: "Deal-PMO und Steps-Plan für Pre-Signing bis Post-Closing: Anwendungsfall Transaktion braucht praezisen Aufgaben- und Zeitplan aus Vertraegen, DD-Unterlagen und Gremienunterlagen extrahiert. SPA Closing Conditions, CPs Conditions Precedent. Prüfraster Pflichten Fristen Bedingungen und Deliverables aus Dokumenten extrahieren, Owner zuordnen, Eskalation dokumentieren, woechentliche PMO-Ansicht. Output Steps-Plan mit Aufgaben, Owner, Fristen und Statusampel für alle Deal-Phasen. Abgrenzung zu Fristen-CP-Kalender für Kalender-Ansicht und zu Post-Closing-Integration."
---

# Deal-PMO und Steps Plan

## Zweck

Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing.

## Arbeitsmodus

- Pflichten, Fristen, Bedingungen und Deliverables aus Dokumenten ziehen.
- Owner, Status, Beleg und Eskalation zuweisen.
- Woechentliche Deal-PMO-Ansicht erzeugen.
- Entscheidungen und Annahmen dokumentieren.

## Rote Schwellen

- Pflicht ohne Frist.
- Keine Eskalation für rote Punkte.
- Plan nicht mit Vertragsversion verknuepft.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/deal-pmo-weekly.md
- assets/templates/signing-closing-steps-plan.md

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Pflichten: Sorgfalt, Vollstaendigkeit, Unabhaengigkeit
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung
- § 17 GeschGehG — Schutz von Geschaeftsgeheimnissen; gilt fuer alle Mandatsinhalte
- Art. 17 MAR — bei boersennotierten Zielobjekten: Ad-hoc-Pflicht und Vertraulichkeit

### Leitsaetze aus der Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior
