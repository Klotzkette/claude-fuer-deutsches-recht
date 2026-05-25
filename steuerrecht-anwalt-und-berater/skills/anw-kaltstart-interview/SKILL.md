---
name: anw-kaltstart-interview
description: "Kaltstart-Interview fuer die steuerrechtsanwaltliche Kanzlei. Erfragt Schwerpunktbereiche (Einkommensteuer / Umsatzsteuer / Koerperschaftsteuer / Gewerbesteuer / Erbschaftsteuer / Steuerstrafrecht) typische Mandate (Einspruch Klage Aussetzung der Vollziehung Aussenpruefungs-Begleitung Selbstanzeige) zustaendige Finanzaemter und Finanzgerichte Schnittstelle zum Steuerberater des Mandanten Aktenstruktur Versandwege ELSTER-Praxis fuer Finanzaemter und beA-Praxis fuer Finanzgerichte und Eskalation. Schreibt das Profil nach ~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/CLAUDE.md."
---

# /steuerrecht-anwalt-und-berater:anw-kaltstart-interview

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

- **ELSTER / ERiC** Pflichtkanal **gegenueber Finanzbehoerden** seit JStG 2024 (§ 87a Abs. 1 S. 2 AO n.F., 6.12.2024) — Einspruch AdV-Antrag verbindliche Auskunft Selbstanzeige Akteneinsicht. beA an Finanzamt unzulässig (Einspruch per beA formunwirksam; vgl. instanzgerichtlich etwa Nds. FG, Beschl. v. 12.2.2026 – 2 K 152/25; Zitat vor Übernahme in juris/beck-online verifizieren).
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
