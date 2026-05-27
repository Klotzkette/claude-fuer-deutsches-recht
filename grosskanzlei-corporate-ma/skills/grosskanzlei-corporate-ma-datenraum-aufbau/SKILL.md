---
name: grosskanzlei-corporate-ma-datenraum-aufbau
description: "Due Diligence Datenraum strukturieren und bestücken: Anwendungsfall Mandant bereitet Verkaufsprozess vor oder Buyer-Team benoetigt strukturierten Datenraum fuer Private M&A, Public M&A, Carve-out oder Distressed-Prozesse. §§ 433 ff. BGB, SPA DD-Pflichten, MAR Vertraulichkeit. Pruefraster Ordnerstruktur nach Workstreams, Zugriffsrechte, NDA-Gate, Versionierung, Document Management. Output Datenraum-Blueprint mit Ordnertaxonomie, Berechtigungsmatrix, Index und Upload-Protokoll. Abgrenzung zu Datenraum-Gap-Clean-Room und zu DD-Legal und DD-Commercial."
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

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
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

- EuGH, Urt. v. 31.05.2018 - C-633/16, NZKart 2018, 321 — Clean Room: kartellrechtlich sensibler Informationsaustausch vor Freigabe ist verbotener Vollzug nach Art. 7 FKVO; Clean Room muss technisch und rechtlich nachweislich getrennt sein
- BGH, Urt. v. 14.03.2003 - V ZR 64/02, NJW 2003, 1811 — Datenraum-Offenlegung: Dokumente im Datenraum gelten nur dann als offengelegt, wenn sie bei sorgfaeltiger Pruefung erkennbar und verstaendlich sind; verschwommener Hinweis genuegt nicht (Fair Disclosure)
- BGH, Urt. v. 04.04.2001 - VIII ZR 32/00, NJW 2001, 2163 — Datenraum-Kenntnis: Kaeuf er muss sich Kenntnis seines DD-Teams aus dem Datenraum zurechnen lassen

## Kommentarliteratur

- Picot, Unternehmenskauf, Kapitel 2 (Due Diligence, Datenraum, Vertraulichkeit), 5. Auflage
- Beisel/Klumpp, Unternehmenskauf, Kapitel 2 § 2 (Datenraum, NDA, IRL), 8. Auflage

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
