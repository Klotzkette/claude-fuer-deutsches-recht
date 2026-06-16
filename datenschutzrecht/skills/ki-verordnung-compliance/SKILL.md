---
name: ki-verordnung-compliance
description: "KI-Systeme auf Anforderungen der KI-VO und Datenschutz prüfen. KI-VO Risikoklassen Art. 5 9 DSGVO Einwilligung. Prüfraster: Risikoklasse Verbote Hochrisiko-KI Dokumentationspflichten DSGVO-Schnittmengen Transparenzpflichten. Output: KI-Compliance-Prüfmemo Maßnahmenliste. Abgrenzung: nicht für al..."
---

# KI-Verordnung — Compliance-Prüfung

## Eingaben

- Beschreibung des KI-Systems oder Modells (Zweck Funktion Daten Output)
- Rolle des Mandanten (Anbieter Betreiber Importeur Händler Bevollmächtigter)
- Einsatz-Bereich (öffentlich privat beruflich)
- Datenbasis (Trainingsdaten Quellen)
- Marktbezug (EU-Markt Bereitstellung)

## Schritt 1 — Anwendungsbereich Art. 2 KI-VO

### Sachlich

- **KI-System** Art. 3 Nr. 1 KI-VO — maschinengestütztes System mit autonomem Verhalten, Anpassung, Ausgabe-Erzeugung (Vorhersage Empfehlung Entscheidung)
- **General Purpose AI Model** Art. 3 Nr. 63 — universelles Modell (LLM Foundation Model)

### Persönlich (Art. 2 Abs. 1)

- **Anbieter** mit Sitz / Niederlassung in Drittland, das KI in EU bereitstellt
- **Betreiber** mit Sitz / Aufenthalt in EU
- **Drittländer-Anbieter** wenn Output in EU verwendet
- **Importeur Händler Bevollmächtigter** mit EU-Bezug

### Ausnahmen Art. 2 Abs. 3-12

- Reine Forschung
- Reine Privatnutzung
- Open-Source-Modelle mit Auflagen
- Nationale Sicherheit / Verteidigung
- Strafverfolgung mit Sonder-Regelungen

## Schritt 2 — Rollen-Bestimmung Art. 3 Nrn. 3-7

| Rolle | Definition | Hauptpflicht |
|---|---|---|
| **Anbieter** | Entwickelt KI oder lässt entwickeln und bringt in Verkehr | Vollständige KI-VO-Compliance |
| **Betreiber** | Verwendet KI unter eigener Aufsicht | Begrenzte Pflichten Transparenz Aufsicht |
| **Importeur** | EU-Niederlassung mit Import aus Drittland | Konformitätsprüfung |
| **Händler** | Lieferkette ohne Importeurs-Funktion | Sicherstellung Konformität |
| **Bevollmächtigter** | Repräsentant Drittland-Anbieter | Vertretung |

### Bei Modifikation Art. 25 KI-VO

- **Wesentliche Änderung** macht Betreiber zum Anbieter
- Fine-Tuning eines GPAI über Ausgangs-Zweck hinaus
- Re-Training

## Schritt 3 — Risiko-Klassifikation

### Stufe 1 — Verbotene Praktiken Art. 5 KI-VO

**Geltungsbeginn 2.2.2025** — bereits aktiv.

Verbote (Auswahl):
- **Subliminale Manipulation** zum Schaden
- **Ausnutzung Schwachstellen** (Alter Behinderung soziale Lage)
- **Social Scoring** durch staatliche oder private Akteure
- **Prädiktive Polizeiarbeit** zur Profilierung
- **Emotions-Erkennung am Arbeitsplatz und in Bildung** (Ausnahmen medizinisch)
- **Biometrische Kategorisierung** nach sensitiven Merkmalen
- **Real-Time-Biometrie im öffentlichen Raum** durch Strafverfolgung (mit eng-bezeichneten Ausnahmen)
- **Untargeted Scraping** für Gesichtserkennungs-Datenbanken

**Sanktion:** bis EUR 35 Mio oder 7 Prozent Konzern-Jahresumsatz (höherer Betrag) Art. 99 Abs. 3

### Stufe 2 — Hochrisiko-System Art. 6 + Anhang III

**Geltungsbeginn 2.8.2026** (Anhang III), 2.8.2027 (Anhang I).

**Bereiche Anhang III:**
1. Biometrie (außer eindeutige Identitäts-Überprüfung)
2. Kritische Infrastruktur
3. Bildung und Berufsausbildung
4. Beschäftigung und Personalverwaltung (z.B. Auswahl-Tools)
5. Zugang zu wesentlichen privaten/öffentlichen Diensten und Leistungen (Kredit-Scoring Sozialhilfe Notfall-Triage)
6. Strafverfolgung
7. Migration und Grenzkontrolle
8. Justiz und demokratische Prozesse

**Pflichten Anbieter Hochrisiko:**
- Risikomanagementsystem Art. 9
- Daten-Governance Art. 10
- Technische Dokumentation Art. 11
- Aufzeichnungs-Pflichten Art. 12
- Transparenz und Informations-Bereitstellung Art. 13
- Menschliche Aufsicht Art. 14
- Genauigkeit Robustheit Cybersicherheit Art. 15
- Konformitätsbewertungs-Verfahren Art. 43
- CE-Kennzeichnung
- Registrierung in EU-Datenbank Art. 71

**Pflichten Betreiber Hochrisiko Art. 26:**
- Verwendung gemäß Anweisung
- Menschliche Aufsicht durch geschultes Personal
- Eingangs-Daten relevant und repräsentativ
- Protokollierung
- Information Betroffener bei Entscheidungen
- DSFA-Pflicht Art. 27

### Stufe 3 — Transparenz-System Art. 50 KI-VO

**Geltungsbeginn 2.8.2026.**

- **Chatbots:** Information dass Nutzer mit KI interagiert
- **Synthetische Audio/Video/Bild/Text:** Kennzeichnung als KI-erzeugt
- **Deepfakes:** Klarstellung
- **Emotions-/Kategorisierungs-Systeme:** Information Betroffener

### Stufe 4 — Minimales Risiko

- Keine spezifischen Verpflichtungen
- Freiwillige Codes-of-Conduct

## Schritt 4 — GPAI-Modelle Art. 51 ff. KI-VO

**Geltungsbeginn 2.8.2025.**

### Standard-GPAI-Anbieter-Pflichten Art. 53

- Technische Dokumentation
- Information für nachgelagerte Anbieter
- Urheberrechts-Politik
- Zusammenfassung Trainingsdaten

### GPAI mit systemischem Risiko Art. 55

- **Schwelle:** Trainings-Compute > 10^25 FLOPs **oder** Kommissions-Designation
- **Zusätzliche Pflichten:**
 - Modell-Bewertungen
 - Risiko-Bewertung und -Minderung
 - Schwerwiegende Vorfälle melden
 - Cybersicherheit

## Schritt 5 — Zeitlicher Anwendungs-Plan

| Datum | Anwendbar |
|---|---|
| **1.8.2024** | KI-VO in Kraft |
| **2.2.2025** | Kapitel I (Allgemein), Kapitel II (Verbotene Praktiken) |
| **2.8.2025** | GPAI-Modelle, Governance-Struktur, Sanktionen |
| **2.8.2026** | Hochrisiko Anhang III, Transparenz Art. 50, Reallabore |
| **2.8.2027** | Hochrisiko Anhang I (Produktsicherheits-Bezug) |

## Schritt 6 — Schnittstelle zur DSGVO

### DSFA bei KI-Hochrisiko Art. 27 KI-VO iVm Art. 35 DSGVO

- **Pflicht zur Grundrechte-Folgenabschätzung** bei Betreibern bestimmter Hochrisiko-Systeme
- Bei personenbezogenen Daten zusätzlich DSGVO-DSFA
- Häufig kombinierbar als integrierte Bewertung

### Automatisierte Entscheidungen Art. 22 DSGVO

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Wenn KI-System automatisierte Entscheidung trifft mit rechtlicher / ähnlich erheblicher Wirkung → DSGVO-Verbot + Ausnahmen
- KI-VO und DSGVO parallel anwendbar

### Datenschutz beim Training Art. 10 KI-VO

- Trainingsdaten-Governance — Verhältnis zu Art. 5 DSGVO (Datenminimierung Zweckbindung)

## Schritt 7 — Konformitätsbewertungs-Verfahren Hochrisiko Art. 43

### Selbst-Bewertung

- Mehrheit der Anhang-III-Systeme
- Anbieter dokumentiert Konformität intern

### Benannte Stelle

- Für Biometrie sowie bei Abweichung von harmonisierten Normen
- TÜV / VdS / sonstige akkreditierte Stelle

### CE-Kennzeichnung

- Nach erfolgreicher Konformitätsbewertung
- Anbringung am System

### Registrierung Art. 71

- EU-Datenbank Hochrisiko-Systeme
- Öffentlich einsehbar (mit Ausnahmen)

## Schritt 8 — Aufsicht und Sanktionen in Deutschland

### Marktüberwachungs-Behörden

- **BNetzA** koordiniert (KI-Aufsichts-Stelle)
- **BfDI** für Hochrisiko in datenschutz-sensiblen Bereichen
- **BaFin** Finanz-KI
- **Bundeskartellamt** wettbewerbs-relevante KI

### Sanktionen Art. 99 KI-VO

| Verstoß | Höchst-Strafe |
|---|---|
| Verbotene Praktiken Art. 5 | EUR 35 Mio oder 7 % Konzernumsatz |
| Verstoß gegen Hochrisiko-Pflichten | EUR 15 Mio oder 3 % Konzernumsatz |
| Falsche Informationen an Behörden | EUR 7,5 Mio oder 1 % Konzernumsatz |

### Verbandsklage

- Konsumenten-Schutzverbände
- Aufsichtsbehörden-Klage

## Schritt 9 — Konkrete Prüfungs-Sequenz

1. **Anwendungsbereich** — Ist KI-System / GPAI vorliegend?
2. **Rolle** — Anbieter Betreiber Importeur Händler?
3. **Verbotene Praktiken** — Art. 5 prüfen → ggf. Stopp
4. **Hochrisiko** — Anhang III Tatbestand erfüllt?
5. **Transparenz** — Art. 50 Pflicht?
6. **GPAI** — Modell mit systemischem Risiko?
7. **Compliance-Plan** mit Fristen
8. **DSGVO-Kompatibilität** parallel

## Schritt 10 — Compliance-Programm-Bausteine

### Governance

- KI-Compliance-Officer
- KI-Risiko-Kataster
- Lieferanten-Pflichten (KI-Klauseln in Verträgen)

### Dokumentation

- Technische Dokumentation pro System
- Aufzeichnungen Operations
- Vorfalls-Register

### Schulung

- Personal das Hochrisiko-KI betreibt
- AI Literacy Art. 4 KI-VO

## Schritt 11 — Verzahnung mit anderen Skills

- **dsfa-erstellung** — bei personenbezogenen Daten kombinierte Folgenabschätzung
- **avv-prüfung** — wenn KI durch Dienstleister
- **drittlandstransfer-prüfung** — bei Cloud-KI außerhalb EU
- **anwendungsfall-triage** — wenn KI-VO-Bezug → hier herleiten
- **mandantendaten-ki** (Kanzlei-intern) — bei eigener KI-Nutzung

## Ausgabe

- `ki-vo-pruefung-{system}.md` mit Risiko-Klassifikation und Pflichten-Plan
- Compliance-Roadmap mit Fristen-Linie
- Lieferanten-Anforderungen
- DSFA-Schnittstelle
- Aufsichts-Korrespondenz-Vorbereitung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- VO (EU) 2024/1689 (KI-Verordnung)
- DSGVO Art. 22 35
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BNetzA-Verlautbarungen (KI-Aufsicht)
- EDSA Empfehlungen zu KI und Datenschutz
- EU-Kommission KI-Leitlinien
- Lambrecht/Stürner KI-Verordnung

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **Stufenweise Anwendung KI-VO (Art. 113):** 02.02.2025 — Verbote Art. 5 und Art. 4 KI-Kompetenz; 02.08.2025 — GPAI-Pflichten Art. 51-55, Sanktionsregime Art. 99; 02.08.2026 — Hochrisiko Anhang III, Art. 50 Transparenzpflichten; 02.08.2027 — Hochrisiko Anhang I. Quelle: VO (EU) 2024/1689, eur-lex.europa.eu/eli/reg/2024/1689/oj.
- **EDSA-Schnittstelle KI-VO / DSGVO:** EDSA-Stellungnahme 28/2024 (Modelle, die mit personenbezogenen Daten trainiert wurden) — verbindliche Auslegungshilfe zur DSGVO-Grundlage bei KI-Training und -Deployment. Quelle: edpb.europa.eu.
- **GPAI Code of Practice:** seit 2025 verfuegbar; Anbieter, die zeichnen, geniessen Vermutung der Compliance (Art. 56 KI-VO). Live-Status der Saeulen (Transparenz, Urheberrecht, Safety/Security) über digital-strategy.ec.europa.eu prüfen.
- **EU AI Office:** seit Anfang 2025 voll operativ; zuständig für GPAI, Koordination mit nationalen Behörden, Code of Practice.
- **Nationale Aufsicht Deutschland:** Bundesnetzagentur (BNetzA) als koordinierende KI-Aufsichtsbehoerde; sektorale Zuständigkeiten (BfDI, BaFin, BAuA, Bundeskartellamt) bleiben bestehen. Konkretisierende Gesetzgebung (KI-Marktueberwachungsgesetz / KI-VO-Durchfuehrungsgesetz) live über bundestag.de prüfen.
- **Schnittstelle Art. 22 DSGVO / KI-VO:** Bei automatisierten Einzelentscheidungen mit erheblicher Wirkung (Scoring, Personalauswahl, Kredit) parallele Prüfung Art. 22 DSGVO + Art. 26 KI-VO + ggf. FRIA Art. 27 KI-VO erforderlich.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über curia.europa.eu verifizieren.

## Triage zu Beginn

1. Ist das System ein KI-System im Sinne von Art. 3 Nr. 1 KI-VO?
2. Welche Risikoklasse liegt vor? (Verboten Art. 5 / Hochrisiko Art. 6 iVm Anhang III / Begrenzt Art. 50 / Minimal)
3. Wer ist der Mandant: Anbieter / Betreiber / Importeur / Händler?
4. Geltungsbereich: Übergangsfrist beachten (Verbotene Praktiken ab 02.02.2025; Hochrisiko ab 02.08.2026)?

## Output-Template — KI-VO-Compliance-Check

**Adressat:** Compliance-Abteilung / Management — Tonfall: sachlich-juristisch

```
KI-VO Compliance-Check [DATUM]
System: [SYSTEMNAME]
Mandant-Rolle: Anbieter / Betreiber / Importeur / Haendler

Einstufung:
Ist KI-System (Art. 3 Nr. 1 KI-VO): ja / nein
Risikoklasse: Verboten / Hochrisiko / Begrenzt / Minimal
Rechtsgrundlage: Art. [X] KI-VO [Anhang I/III/...Nr. X]

Anwendbarer Zeitplan:
Erste Pflichten ab: [DATUM]

Kernpflichten:
| Pflicht | Norm | Status |
|-------------------------------|-------------|------------|
| Konformitaetsbewertung | Art. 43 ff. | |
| Technische Dokumentation | Art. 11 | |
| Menschliche Aufsicht | Art. 14 | |
| Transparenz gegenueber Nutzern| Art. 13/50 | |
| DSGVO/DSFA (Schnittstelle) | Art. 35 DSGVO| |

Ergebnis: Konform / Anpassungsbedarf (bis [DATUM]) / Verboten
```
