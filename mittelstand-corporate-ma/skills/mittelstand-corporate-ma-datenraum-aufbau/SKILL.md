---
name: mittelstand-corporate-ma-datenraum-aufbau
description: "Datenraum-Aufbau: Strukturiert und bestueckt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse."
---

# Datenraum-Aufbau

## Zweck

Strukturiert und bestückt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse.

## Arbeitsmodus

- Datenraumindex aus IRL, Deal-Typ und Workstreams erzeugen.
- Dokumente klassifizieren: Vertrag, Register, Steuer, HR, IP, IT, Litigation, ESG, Finance.
- Hauptdokumente, Anlagen und Verwandtschaftsgrade verknuepfen.
- Clean-Room- und Need-to-know-Zonen vorschlagen.

## Rote Schwellen

- Sensible Informationen im falschen Bereich.
- Datenraum ohne Inhaltslogik.
- Offenlegung wesentlicher Informationen an ungewoehnlicher Stelle ohne Hinweis.

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

- assets/templates/datenraum-index.md
- assets/templates/clean-room-access-log.md

## Triage — klaere vor Datenraum-Aufbau

1. Welcher Deal-Typ — Private M&A, Public M&A, Carve-out, Distressed, SPAC?
2. Sell-side oder Buy-side Datenraum? (Sell-side: strukturierter Bieterprozess; Buy-side: Gegenpruefung)
3. Clean Room erforderlich — bei sensiblen Wettbewerberinfos (Kartellrecht)?
4. Welche Datenraum-Plattform — Datasite, Intralinks, Merrill, Box, SharePoint?
5. Welche Zugangsgruppen sind vorgesehen — Bieter A/B/C, Management, Berater, Konsortien?

## Zentrale Rechtsgrundlagen

- Art. 7 FKVO; § 41 GWB — Vollzugsverbot und Clean-Room-Pflicht fuer kartellrechtlich sensibler Informationsaustausch vor Freigabe
- Art. 7, 17, 18 MAR — Vertraulichkeit von Insiderinformationen im Datenraum bei boersennotierten Zielunternehmen; Insiderliste bei Datenraumzugang
- § 47 GwG — Verschwiegenheitspflicht; keine Offenlegung geldwaescherelevanter Informationen
- §§ 17, 18 GeschGehG — Schutz von Geschaeftsgeheimnissen; Geheimhaltungsvereinbarung muss vor Datenraumzugang vorliegen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Deal-Typ und Zugriffsstruktur festlegen:** Bieter-Gruppen, Clean-Room-Bereich, Management-Zugang
2. **Index-Struktur erstellen:** Hauptkategorien Corporate, Legal, Finance/Tax, Commercial, HR, IP/IT, Litigation, Real Estate, ESG
3. **Dokumente hochladen und klassifizieren:** je Dokument: Vertragstyp, Parteien, Datum, Relevanz-Flag (High/Medium/Low)
4. **Geheimhaltungsprotokoll:** NDA-Liste, MAR-Insiderliste (falls boersennotiert), Clean-Room-Zugangspro tokoll
5. **IRl-Management:** fehlende Dokumente als Information Request List erfassen; Seller-Response verfolgen
6. **Datenraum-Gap-Analyse:** Vollstaendigkeit gegen Standard-DD-Checkliste pruefen

## Rote Schwellen

- Sensibler Wettbewerber-Datenraum ohne Clean Room: Kartellrechtsverstoss (Art. 7 FKVO)
- Datenraumzugang ohne NDA: Geschaeftsgeheimnisschutz verletzt (GeschGehG)
- Insiderinformationen ohne MAR-Insiderliste: Aufsichtsrisiko (MAR Art. 18)
