---
name: kanzlei-cowork-kaltstart-interview
description: "Kaltstart-Interview fuer das generische Kanzlei-Cowork-Plugin. Erfragt Kanzleiprofil (Solo / Sozietaet / GmbH / Partnerschaft) Rechtsgebiete-Mix Sekretariat (vorhanden Stellen) Aktenstruktur-Konvention beA-Profil Versandwege Buchhaltungssoftware (DATEV Lexware sevDesk RA-MICRO Advoware) Vorgehensweise Fristenbuch und Tagesbrief Honorarpraxis (RVG / Vereinbarung) Mahnpraxis Mandantenstamm-Pflege Geburtstags- und Weihnachtsverteiler. Schreibt Profil nach ~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-cowork/CLAUDE.md."
---

# /kanzlei-cowork:kanzlei-cowork-kaltstart-interview

## Ablauf

1. Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-cowork/CLAUDE.md` prüfen.
2. Falls vorhanden ohne Platzhalter: bestätigen.
3. Andernfalls Interview unten durchführen.

## Kaltstart-Interview

### 1. Kanzleiprofil

- **Rechtsform** Einzelanwalt / Sozietät GbR / Partnerschaftsgesellschaft / Rechtsanwalts-GmbH / Rechtsanwalts-AG
- **Anzahl Anwälte** und Mitarbeiterstellen
- **Sekretariat** vorhanden ja / nein Anzahl Stellen
- **Standort** Ort und Kammerbezirk

### 2. Rechtsgebiete und Schwerpunkte

- Liste der Rechtsgebiete der Kanzlei.
- Hauptmandantenstamm (B2B / B2C / öffentliche Hand / Mischung).
- Fachanwaltsbezeichnungen der Anwälte.

### 3. Aktenstruktur

- **Aktennummernsystem** (z. B. `<Jahr>/<lfd. Nr.>` oder `<Rechtsgebiet>-<Jahr>-<Nr>`)
- **Verzeichnis-Konvention** unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-cowork/mandate/<az>/`
- **Standardunterordner** wie `01_stammdaten 02_korrespondenz 03_schriftsaetze 04_anlagen 05_fristen 06_honorar`

### 4. beA und Versandwege

- **beA-Profil** vorhanden (Pflicht für RA seit 01.01.2022)
- **Signaturkarte** vorhanden und gültig
- **EGVP** zusätzlich verwendet
- **Versandwege** beA (Behörde Gericht RA-zu-RA) / Post / Mandanten-E-Mail / sicherer Mandantenübergang

### 5. Fristenbuch und Tagesbrief

- **Fristenbuch** zentral (Pflicht nach BRAO-Berufsregeln)
- **Vorfrist-Standard** (typisch fünf Tage vor Hauptfrist)
- **Tagesbrief** vom Sekretariat morgens ja / nein

### 6. Honorarpraxis

- **Standardabrechnung** RVG / Honorarvereinbarung / Mischung
- **RVG-Software** vorhanden (DATEV RA-MICRO Advoware) ja / nein
- **Rechnungsstellung** Zeitpunkt (Mandatsende oder Zwischenrechnungen)
- **Honorarvereinbarung** Stundensätze typisch

### 7. Mahnpraxis

- Mahnstufen (zwei Stufen / drei Stufen)
- Mahnfristen und Mahngebuehren
- Eskalation: Inkasso / Klage / Vergleich

### 8. Mandantenpflege

- **Geburtstags-Verteiler** ja / nein
- **Weihnachtskarten** Verteiler (digital / Post)
- **Newsletter** Mandantenrundschreiben

### 9. Buchhaltung

- **Software** DATEV / Lexware / sevDesk / SAP / RA-MICRO Finanz / sonstig
- **Steuerberater** der Kanzlei mit Name Kontakt
- **USt-Voranmeldung** monatlich / vierteljaehrlich

## Ausgabe

Profil wird geschrieben. Nächste sinnvolle Skills:

- `/kanzlei-cowork:fristenbuch-fuehren` — Hauptfristen pflegen
- `/kanzlei-cowork:sekretariats-tagesbrief` — Tagesbrief morgens
- `/kanzlei-cowork:versand-vor-check` — vor jedem Versand

## Rechtlicher Rahmen

- **BRAO** § 43a Verschwiegenheit § 50 Aktenführung § 51 Berufshaftpflicht § 31a beA-Pflicht
- **RVG** Gebührentabelle Anlage 1 Anlage 2 VV RVG
- **BORA** Berufsordnung der Rechtsanwälte (BRAK)
- **DSGVO** Art. 5 6 9 Auftragsverarbeitung Art. 28

## Hinweise

Mandantenkommunikation und folgenreiche Versandhandlungen verbleiben in anwaltlicher Verantwortung. Vor jedem Versand `versand-vor-check`.
