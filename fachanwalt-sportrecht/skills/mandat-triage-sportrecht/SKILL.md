---
name: mandat-triage-sportrecht
description: "Sportrechtliches Mandat eintrifft und muss strukturiert erfasst werden: Mandantenrolle Sachgebiet Sofort-Fristen. Verbandsfrist gegen Sanktion typisch 1-2 Wochen. Normen je nach Routing. Prüfraster Mandanten-Typ Sachgebiets-Zuordnung Fristen-Sofort-Check Eskalation bei Spielsperre oder Doping-Verdacht. Output Mandat-Karte Routing-Empfehlung Handlungsweichen. Abgrenzung zu erstgespraech-mandatsannahme (Vollaufnahme) und fachanwalt-sportrecht-orientierung (Überblick)."
---

# Mandat-Triage Sportrecht

## Zweck

Sportrechts-Mandate sind oft saison- und turnierbezogen — eine Sperre vor einem Spiel oder einer Olympia-Qualifikation ist existenziell. Triage stellt Eilbedürftigkeit fest.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Profisportler (Amateur Bundesliga National Olympia)
- Amateur-Sportler
- Verein (Bundesliga Profi Amateur)
- Verband (Landes Bundes International)
- Trainer / Funktionär
- Sponsor / Werbe-Partner
- Medienpartner
- Wettanbieter

### Frage 2 — Sachgebiet?

- Verbandsstrafe (Spielsperre Geldstrafe Vereinslizenz-Entzug)
- Doping (NADA WADA Anti-Doping-Gesetz)
- Spielervertrag / Anstellungsvertrag
- Transferstreit / Spielerwechsel
- Sponsoringvertrag
- Werbung Marketing Persönlichkeitsrechte
- Berichterstattungs-Konflikt
- Wettkampfmanipulation
- Streit innerhalb Verein/Verband
- Schiedsgerichtsbarkeit CAS
- Olympia-Nominierung / Mannschaftsaufstellung
- Stadionverbot

### Frage 3 — Akute Eilbedürftigkeit?

- **Sperre vor entscheidendem Spiel** binnen Tagen
- **Doping-Verdacht** A-Probe positiv — B-Probe Termin
- **Lizenz-Verlust** Bundesliga Termin droht
- **Transferfenster** Schließung droht
- **Verbandsberufung** Frist eng (oft eine Woche)
- **CAS-Berufung** zwingend binnen 21 Tagen
- **Olympia-Nominierung** Stichtag

### Frage 4 — Verfahrensstadium?

- Beratungsbedarf
- Verbands-Verfahren laufend (Anhörung Beweisaufnahme)
- Erstinstanzlicher Verbandsbescheid
- Verbands-Berufung
- CAS-Verfahren
- Schweizerisches Bundesgericht (gegen CAS-Spruch)
- Staatliche Gerichte (parallel oder Restzuständigkeit)

### Frage 5 — Verbandsstruktur?

- Welcher Verband ist zuständig?
- Welche Stufe (Landesverband Bundesverband Internationale Föderation)?
- Schiedsklausel CAS in Mitgliedschaft / Lizenz enthalten?

### Frage 6 — Frist?

- **Verbandsberufung** typisch sieben bis vierzehn Tage je Disziplinar-Ordnung
- **CAS-Berufung** einundzwanzig Tage Art. R49 CAS Code
- **Schweizerisches Bundesgericht** dreißig Tage
- **Staatliche Gerichte** Verjährung drei Jahre § 195 BGB
- **Sponsoringvertrag** vertragliche Fristen

### Frage 7 — Wirtschaftliche Verhältnisse?

- Berufssportler-Einkommen
- Sponsoringverträge
- Werbeverträge
- Rechtsschutz Sportverband
- Persönliche Rechtsschutz-Versicherung
- CAS-Kosten erheblich

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Verbandsstrafe-Anfechtung | `verbandsstrafe-anfechten` |
| Doping-Verfahren | `verbandsstrafe-anfechten` plus NADA/WADA-Spezifika |
| Spielervertrag-Streit | (Skill spielervertrag — perspektivisch) |
| Transferstreit | (Skill transferstreit — perspektivisch) |
| Sponsoringvertrag | weiter an `vertragsrecht`-Plugin |
| Persönlichkeitsrechte Sportler | weiter an `mandat-triage-urheber-medienrecht` |
| Verein-Vorstand-Streit | weiter an `gesellschaftsrecht`-Plugin |
| Wettkampfmanipulation Strafrecht | weiter an `mandat-triage-strafrecht` (§ 265c § 265d StGB) |
| Stadionverbot | (Skill stadionverbot — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — kein Doppelmandat Verband/Sportler
- **Streitwert** Sponsoring-Verlust Berufsausübungs-Wert
- **Komplexität** Schiedsverfahren CAS Englisch-Sprachig
- **Versicherungs-Deckung** Berufshaftpflicht Sportler oder Verein

## Eilmodus

- **Sperre vor wichtigem Spiel:**
  1. Verbandsberufung
  2. Antrag aufschiebende Wirkung
  3. Parallel staatliches Eilverfahren § 935 ZPO
  4. Pressekommunikation strategisch
- **Doping-Verdacht:**
  1. Beratung vor B-Probe
  2. B-Probe-Anfechtung Termin organisieren
  3. NADA-Verfahren steuern
  4. Verteidigungs-Strategie WADA Code

## Eskalation

- **Telefon-Sofort** Sperre vor entscheidendem Spiel Doping-Befund
- **Binnen einer Stunde** Verbandsberufung-Frist CAS-Frist
- **Heute** Eilantrag staatliches Gericht
- **Diese Woche** Schriftsatz-Erstentwurf Verteidigungsstrategie

## Ausgabe

- `triage-protokoll-sportrecht.md`
- Aktenanlage mit Verband-Struktur und Schiedsklausel
- Frist im Fristenbuch
- Verbandsberufung-Entwurf bei akutem Bedarf
- Mandatsvereinbarung mit Honorar (CAS oft Honorarvereinbarung)
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 21 25 305 ff. 823 242
- AGG §§ 19 ff.
- GG Art. 9 12
- AntiDopG
- StGB §§ 265c 265d
- ZPO §§ 935 1029 1033
- WADA-Code NADA-Verfahrensordnung
- CAS Code
- BGH II. VI. Zivilsenat
- Adolphsen Sportrecht
