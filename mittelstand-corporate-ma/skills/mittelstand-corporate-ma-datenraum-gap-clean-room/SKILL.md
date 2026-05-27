---
name: mittelstand-corporate-ma-datenraum-gap-clean-room
description: "Datenraum-Gap-Analyse und Clean Room: Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Luecken, Widersprueche, Dubletten und Clean-Room-Bedarf."
---

# Datenraum-Gap-Analyse und Clean Room

## Zweck

Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf.

## Arbeitsmodus

- Datenraum gegen IRL und IM abgleichen.
- Referenzierte, aber fehlende Dokumente finden.
- Widersprüche zwischen Legal, Tax, Finance, ESG und Commercial markieren.
- Clean-Room-Zugriffe und kartellrechtliche Sensibilitaet protokollieren.

## Rote Schwellen

- Antitrust-sensible Daten offen zugänglich.
- Wichtige Dokumente nur implizit oder unklar benannt.
- KI-sortierter Datenraum ohne menschliches Gate.

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

- assets/templates/datenraum-gap-analysis.md
- assets/templates/clean-room-access-log.md
- assets/templates/data-quality-gate.md

## Triage

1. Liegt ein vollstaendiger Datenraum-Index vor oder muss dieser erst erstellt werden?
2. Gibt es einen Information Request Letter (IRL) — welche Dokumente fehlen noch?
3. Sind kartellrechtlich sensible Informationen im Datenraum (Preise, Kundenlisten, Marktanteile) — ist ein Clean Room erforderlich?
4. Stimmen Teaser und IM mit dem Datenraum-Inhalt ueberein — gibt es wesentliche Abweichungen?

## Zentrale Rechtsgrundlagen

- Art. 7 FKVO; § 41 GWB — Clean-Room-Pflicht bei kartellrechtlich sensiblen Informationen vor Fusionskontrollfreigabe
- §§ 17-18 GeschGehG — Schutz von Geschaeftsgeheimnissen: Datenraum-Inhalte unterliegen Geheimhaltung; Clean Room schutzt Wettbewerber-Informationen
- §§ 311, 241 Abs. 2 BGB — Offenbarungspflicht des Verkaeuf ers: wesentliche Risiken muessen offengelegt werden; Fair Disclosure nach BGH
- Art. 7, 17 MAR — bei boersennotiertem Zielobjekt: Insiderinformationen im Datenraum erfordern MAR-konforme Zugangsprotokollierung

## Aktuelle Rechtsprechung

- EuGH, Urt. v. 31.05.2018 - C-633/16, NZKart 2018, 321 — Clean Room: kartellrechtlich sensitiver Austausch vor Fusionskontrollfreigabe ist verboten; Clean Room muss technisch und rechtlich nachweisbar abgegrenzt sein
- BGH, Urt. v. 30.09.2011 - V ZR 17/11, NJW 2012, 56 — Fair Disclosure: Informationen gelten nur dann als discloset, wenn sie klar und deutlich sind; blosse Zugaenglichkeit im Datenraum ohne erkennbaren Hinweis auf das Risiko genuegt nicht

## Kommentarliteratur

- Picot, Unternehmenskauf, Kapitel 2 (Datenraum, Gap-Analyse, Clean Room), 5. Auflage

## Schritt-fuer-Schritt-Workflow

1. **Datenraum-Index auswerten:** Kategorien, Vollstaendigkeit, Duplikate, Versionierung
2. **IRL-Luecken identifizieren:** fehlende Dokumente je Workstream aufführen; Prioritaet High/Medium
3. **Widerspruchsanalyse:** Teaser vs. IM vs. Datenraum — wesentliche Abweichungen → Red Flag
4. **Clean Room pruefen:** kartellrechtlich sensitive Informationen? → Clean Room einrichten; Zugangsproto koll
5. **Disclosure-Konzept bewerten:** allgemeine Disclosure vs. spezifische Disclosure; Fair-Disclosure-Standard pruefen

## Rote Schwellen

- Kartellrechtlich sensible Infos im normalen Datenraum: Clean-Room-Pflicht verletzt
- IM-Widersprueche: Misrepresentation-Risiko des Verkaeuf ers
- Fehlende wesentliche Dokumente ohne IRL: DD unvollstaendig; Garantierisiko
