---
name: steuerrecht-kanzlei-kaltstart-interview
description: "Kaltstart-Interview fuer die steuerrechtsanwaltliche Kanzlei. Erfragt Schwerpunktbereiche (Einkommensteuer / Umsatzsteuer / Koerperschaftsteuer / Gewerbesteuer / Erbschaftsteuer / Steuerstrafrecht) typische Mandate (Einspruch Klage Aussetzung der Vollziehung Aussenpruefungs-Begleitung Selbstanzeige) zustaendige Finanzaemter und Finanzgerichte Schnittstelle zum Steuerberater des Mandanten Aktenstruktur Versandwege beA-Praxis und Eskalation. Schreibt das Profil nach ~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-kanzlei/CLAUDE.md."
---

# /steuerrecht-kanzlei:steuerrecht-kanzlei-kaltstart-interview

## Ablauf

1. Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-kanzlei/CLAUDE.md` prüfen.
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

- **Hauptfinanzaemter** mit beA-/EGVP-Postfach
- **Finanzgericht** des Bundeslandes mit beA-Postfach
- **BFH München** (Revisionsinstanz)

### 5. Schnittstellen

- **Steuerberater des Mandanten** — Mandatsabgrenzung Steuererklärung vs Rechtsstreit
- **Wirtschaftsprüfer** bei Bilanzthemen
- **Buchhaltung** des Mandanten

### 6. Versandwege

- **beA** Pflicht für Rechtsanwälte gegenüber Behörden und Gerichten (§ 31a BRAO).
- **ELSTER** bei Steuererklärungen und Steueranmeldungen (nur wenn Mandant das Plugin gleichzeitig für eigene Steuererklärungen nutzt — eher Steuerberater-Werkzeug).
- **EGVP** Finanzgericht.

### 7. Standort und Eskalation

- **Bundesland** (entscheidet über Finanzgerichtszuständigkeit)
- **Eskalationspartner** bei strafsteuerrechtlichen Sonderfällen

## Ausgabe

Profil wird geschrieben. Nächste Skills:

- `/steuerrecht-kanzlei:steuerbescheid-analyse` — bei eingegangenem Bescheid
- `/steuerrecht-kanzlei:einspruch-finanzamt` — bei Bescheid und Einspruchsfrist
- `/steuerrecht-kanzlei:fristenbuch-steuerrecht` — Fristen-Check

## Rechtlicher Rahmen

- **AO** Abgabenordnung — Hauptverfahrensrecht.
- **FGO** Finanzgerichtsordnung — Klageverfahren.
- **EStG KStG GewStG UStG ErbStG GrStG** materielles Steuerrecht.
- **BRAO** § 31a beA-Pflicht.
- **StBerG** Abgrenzung Steuerberater / Rechtsanwalt.

## Hinweise

Steuerrechtliche Beratung für Erstellung von Steuererklärungen ist im Schwerpunkt Tatigkeit des Steuerberaters (StBerG § 3). Anwaltliche Steuerberatung ist zulässig (§ 3 Nr. 1 StBerG); die Erstellung von Erklärungen erfolgt aber regelmäßig durch den Steuerberater des Mandanten. Dieses Plugin fokussiert auf den streitbezogenen Teil.
