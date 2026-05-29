---
name: anw-kaltstart-interview
description: "Kaltstart-Interview für die steuerrechtsanwaltliche Kanzlei um Praxisprofil zu befuellen. Anwendungsfall Erstinstallation Plugin oder Konfiguration enthaelt noch Platzhalter-Marker. Erfragt Schwerpunktbereiche ESt USt KSt GewSt ErbSt Steuerstrafrecht typische Mandate Einspruch Klage AdV Aussenprüfungs-Begleitung Selbstanzeige zuständige Finanzaemter und Finanzgerichte Schnittstelle Steuerberater Aktenstruktur ELSTER-Praxis beA-Praxis. Output Kanzlei-Konfigurationsprofil unter CLAUDE.md Verzeichnis. Abgrenzung zu anw-mandat-triage-steuerrecht das mandatsbezogen arbeitet."
---

# /steuerrecht-anwalt-und-berater:anw-kaltstart-interview

## Rechtliche Grundlagen (Orientierung für das Interview)

### Zentrale Normen
- **AO** Abgabenordnung — Hauptverfahrensrecht
- **FGO** Finanzgerichtsordnung — Klageverfahren
- **EStG KStG GewStG UStG ErbStG GrStG** materielles Steuerrecht
- **BRAO** § 31a beA-Einrichtungspflicht
- **§ 87a Abs. 1 S. 2 AO n.F.** (JStG 2024, 6.12.2024) — ELSTER/ERiC-only für Finanzbehoerden
- **§ 52d FGO** — beA-Pflicht gegenüber Finanzgerichten

### Aktuelle Rechtsprechung (Versandwege)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md` prüfen.
2. Falls vorhanden ohne Platzhalter: bestätigen.
3. Andernfalls Interview unten durchführen und Datei schreiben.

## Kaltstart-Interview

### 1. Rolle und Kanzlei

- **Rolle:** Fachanwalt für Steuerrecht / RA mit steuerrechtlichem Schwerpunkt / Steueranwalt mit Steuerberater-Bestellung (dann auch Steuererklärungen) / Syndikus?
- **Abgrenzung zum Steuerberater des Mandanten** — wer rechnet wer streitet wer hat die Steuererklärung erstellt?
- **Kanzleigroesse** und Sekretariatslast

### 2. Schwerpunktbereiche

- Einkommensteuer / Lohnsteuer
- Umsatzsteuer (einschließlich Vorsteuerstreitigkeiten)
- Koerperschaft- und Gewerbesteuer
- Erbschaft- und Schenkungsteuer
- Bewertungs- und Grundsteuer
- Steuerstrafrecht (§§ 369 ff. AO)
- Internationales Steuerrecht (DBA Verrechnungspreise)

### 3. Mandatstypen

- Einspruch gegen Steuerbescheid (§§ 347 ff. AO)
- Klage zum Finanzgericht (§§ 40 ff. FGO)
- Antrag auf Aussetzung der Vollziehung (§ 361 AO / § 69 FGO)
- Außenprüfung Begleitung (§§ 193 ff. AO)
- Selbstanzeige (§ 371 AO)
- Verbindliche Auskunft (§ 89 Abs. 2 AO)
- Stundungs- und Erlassantrag (§§ 222 227 AO)

### 4. Zuständige Gerichte und Aemter

- **Hauptfinanzaemter** — elektronische Kommunikation über **ELSTER** (Mein ELSTER) bzw. ERiC; kein beA seit 6.12.2024 (§ 87a Abs. 1 S. 2 AO n.F.)
- **Finanzgericht** des Bundeslandes mit beA-Postfach (§ 52d FGO Pflicht)
- **BFH München** (Revisionsinstanz)

### 5. Schnittstellen

- **Steuerberater des Mandanten** — Mandatsabgrenzung Steuererklärung vs Rechtsstreit
- **Wirtschaftsprüfer** bei Bilanzthemen
- **Buchhaltung** des Mandanten

### 6. Versandwege

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **beA** Pflicht **gegenueber Gerichten** (§ 52d FGO) — Klage Finanzgericht AdV-Antrag FG Revision BFH.
- **EGVP** als Alternative zum beA gegenueber Gerichten.
- **Briefpost / Telefax** weiterhin in alle Richtungen zulaessig (§ 87a AO bezieht sich nur auf elektronische Wege).

### 7. Standort und Eskalation

- **Bundesland** (entscheidet über Finanzgerichtszuständigkeit)
- **Eskalationspartner** bei strafsteuerrechtlichen Sonderfällen

## Ausgabe

Profil wird geschrieben. Nächste Skills:

- `/steuerrecht-anwalt-und-berater:anw-steuerbescheid-analyse` — bei eingegangenem Bescheid
- `/steuerrecht-anwalt-und-berater:anw-einspruch-finanzamt` — bei Bescheid und Einspruchsfrist
- `/steuerrecht-anwalt-und-berater:anw-fristenbuch-steuerrecht` — Fristen-Check

## Rechtlicher Rahmen

- **AO** Abgabenordnung — Hauptverfahrensrecht.
- **FGO** Finanzgerichtsordnung — Klageverfahren.
- **EStG KStG GewStG UStG ErbStG GrStG** materielles Steuerrecht.
- **BRAO** § 31a beA-Einrichtungspflicht.
- **§ 87a Abs. 1 S. 2 AO n.F.** (JStG 2024, 6.12.2024) — ELSTER/ERiC-only fuer Finanzbehoerden; beA/beSt ausgeschlossen.
- **§ 52d FGO** — beA-Pflicht gegenueber Finanzgerichten.
- **StBerG** Abgrenzung Steuerberater / Rechtsanwalt.

## Hinweise

Steuerrechtliche Beratung für Erstellung von Steuererklärungen ist im Schwerpunkt Tatigkeit des Steuerberaters (StBerG § 3). Anwaltliche Steuerberatung ist zulässig (§ 3 Nr. 1 StBerG); die Erstellung von Erklärungen erfolgt aber regelmäßig durch den Steuerberater des Mandanten. Dieses Plugin fokussiert auf den streitbezogenen Teil.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 bestaetigt (Nds. FG Urt. v. 12.02.2026 – 2 K 152/25 instanzgerichtlich bestaetigt, BFH-NZB I B 28/25 anhängig) -->
