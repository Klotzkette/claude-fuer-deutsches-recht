---
name: kaltstart-interview
description: "Kaltstart-Interview fuer das Fluggastrechte-Plugin. Klaert Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reiseplan-Konvention. Schreibt das Profil nach ~/.claude/plugins/config/claude-fuer-deutsches-recht/fluggastrechte/CLAUDE.md. Bei Erstinstallation laufen lassen. Mit --redo neu interviewen. Disclaimer Selbstmandat ersetzt nicht anwaltliche Pruefung im Streitfall."
---

# /fluggastrechte:kaltstart-interview

## Ablauf

1. Datei `~/.claude/plugins/config/claude-fuer-deutsches-recht/fluggastrechte/CLAUDE.md` pruefen.
2. Falls befuellt: bestaetigen.
3. Andernfalls Interview unten.

## Disclaimer

Dieses Plugin unterstuetzt das eigene Geltendmachen von Fluggastrechten als Verbraucher. Es ist **keine Rechtsberatung**. Bei komplexen Faellen (mehrere Passagiere mit unterschiedlichen Anspruechen Gesellschafts-Bezuegen Verspaetungs-Lawinen Schlichtungsstelle vor Gericht) anwaltliche Hilfe einholen — z. B. ueber die Schlichtungsstelle Luftverkehr (SOEP).

## Interview

### 1. Wer nutzt das Plugin

- Eigener Fluggast / Mitreisender Familie / Vertretung Bekannter / kleine Anwaltskanzlei?
- Anzahl betroffener Personen (Passagiere) pro Fall typisch.

### 2. Buchungsstammdaten

- **Name** wie in der Buchung steht (wichtig fuer Schriftverkehr — Airline-Datenabgleich).
- **Bevorzugte Sprache** im Schriftverkehr Deutsch / Englisch.
- **Wohnsitz und Adresse** (fuer Gerichtsstand bei Klage).
- **Bevorzugter Zustellweg** der Forderungsschreiben — Post (Einschreiben) oder E-Mail an Airline-Service-Postfach.

### 3. Reiseplan-Konvention

- **Buchungsbestaetigung** liegt vor (PDF Boardingpass E-Mail).
- **Tickets** der Mitreisenden ebenfalls vorhanden (Vollmachten Skill `vollmacht-familienmitglieder`).
- **Schlichtungsstelle** SOEP bereits angeschrieben? Wenn ja: SOEP-Verfahren vorhanden.

### 4. Eskalation

- Bei Ausbleiben einer Reaktion oder bei Streitstand zur Schlichtungsstelle Luftverkehr **SOEP** (Schlichtungsstelle fuer den oeffentlichen Personenverkehr e. V.) — kostenfrei fuer Verbraucher. Voraussetzung: keine Klage anhaengig.
- Bei Erfolglosigkeit Klage zum Amtsgericht — Skill `klage-amtsgericht-fluggast`.

## Ausgabe

Profil wird geschrieben. Empfohlene naechste Skills:

- `/fluggastrechte:ticket-und-fluginformationen-erfassen` — Daten zum Fall sammeln
- `/fluggastrechte:annullierung-oder-verspaetung-einordnen` — Rechtskategorie zuordnen
- `/fluggastrechte:airline-standardausreden-pruefen` — typische Gegenargumente kennen

## Rechtlicher Rahmen — Ueberblick

- **VO (EG) Nr. 261/2004** — Fluggastrechteverordnung des Europaeischen Parlaments und des Rates.
- **EuGH-Rechtsprechung** — Auslegungsmassstab fuer alle Mitgliedstaaten.
- **BGB §§ 631 ff.** — Reisevertrag bei Pauschalreisen ergaenzend.
- **§§ 12 13 ZPO** Gerichtsstand allgemein, **EuGH C-204/08 Rehder** Wahlrecht Abflug- oder Zielort fuer EU-Fluege.
- **Verjaehrung** drei Jahre § 195 BGB (Ende Kalenderjahr Kenntnis § 199 Abs. 1 BGB).

## Hinweise

Auch nach der Brexit-Anpassung gilt die VO 261/2004 in der EU. Fluege ab Drittstaat zu einem EU-Flughafen mit Nicht-EU-Airline fallen **nicht** unter die VO; Fluege ab EU mit Nicht-EU-Airline schon. Pruefkriterium: Art. 3 VO 261/2004.
