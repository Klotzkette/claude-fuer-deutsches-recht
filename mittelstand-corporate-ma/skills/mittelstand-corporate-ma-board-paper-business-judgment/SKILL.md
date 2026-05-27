---
name: mittelstand-corporate-ma-board-paper-business-judgment
description: "Vorstand GF oder Aufsichtsrat braucht Entscheidungsunterlage fuer M&A-Beschluss: Board Paper Business-Judgment-Dokumentation KI-Einsatztransparenz. Normen §§ 93 AktG 43 GmbHG Business-Judgment Rule ARAG/Garmenbeck. Pruefraster Informationsgrundlage Alternativen-Abwaegung Risikodokumentation KI-Disclosure Protokollierungspflicht. Output Board-Paper-Entwurf Beschluss-Template Risikomatrix. Abgrenzung zu deal-team-staffing (Rollen) und ki-governance-berufsrecht (KI-Recht)."
---

# Board Paper und Business Judgment

## Zweck

Erstellt Entscheidungsunterlagen für Vorstand/Geschäftsführung/Aufsichtsrat mit Informationsgrundlage, Alternativen, Risiken und KI-Einsatztransparenz.

## Arbeitsmodus

- Entscheidung, Alternativen, Informationsquellen und Beraterbeitraege darstellen.
- Due-Diligence-Ergebnisse und Restrisiken knapp priorisieren.
- KI-Nutzung, Plausibilisierung und Datenlücken transparent machen.
- Business-Judgment- und Legalitaetspflicht-Aspekte als Prüfkarte ausgeben.

## Rote Schwellen

- Entscheidungsvorlage ohne Informationsgrundlage.
- KI-Analyse ohne Plausibilisierung.
- Legalitaetspflicht oder Freigabevorbehalt ignoriert.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/board-paper-bjr.md
- assets/templates/xai-quality-control-log.md

## Rechtliche Einbettung und Praxiswissen

### Zentrale Normen
- § 43a BRAO — anwaltliche Pflichten: vollstaendige Mandatsfuehrung; Sorgfaltspflichten gelten auch fuer automatisierte Prozesse
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung; gilt auch fuer Organisation und Monitoring
- § 49b BRAO — Honorarvereinbarung: Abrechnungsmodalitaeten muessen transparent und schriftlich vereinbart sein
- §§ 93, 116 AktG; § 43 GmbHG — Business Judgment Rule: Entscheidung auf ausreichender Informationsgrundlage; Dokumentationspflicht

### Leitsaetze
- BGH, Urt. v. 21.04.1997 - II ZR 175/95, BGHZ 135, 244 — Business Judgment Rule: Geschaeftsfuehrer handelt pflichtgemaess, wenn er bei einer unternehmerischen Entscheidung vernuenftigerweise annehmen durfte, zum Wohl der Gesellschaft zu handeln; Informationsgrundlage muss angemessen sein
- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — Beraterhaftung: vollstaendige Information des Mandanten ist Kernpflicht; Luecken koennen Schadensersatz ausloesen

### Kommentarliteratur
- MueKo GmbHG/Fleischer, § 43 Rn. 1-80 (Geschaeftsfuehrerhaftung, Business Judgment Rule)
- Schaub, Arbeitsrechts-Handbuch, § 12 (Mandate, Vollmachten, Honorare)

### Qualitaetssicherung
- Human-in-the-loop bei allen automatisierten Ausgaben
- Dokumentation: Datum, Methodik, Human-Check-Protokoll
