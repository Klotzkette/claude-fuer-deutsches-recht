---
name: kanzlei-cowork-kaltstart-interview
description: "Kaltstart-Interview für das generische Kanzlei-Cowork-Plugin. Erfragt Kanzleiprofil (Solo / Sozietaet / GmbH / Partnerschaft) Rechtsgebiete-Mix Sekretariat (vorhanden Stellen) Aktenstruktur-Konvention beA-Profil Versandwege Buchhaltungssoftware (DATEV Lexware sevDesk RA-MICRO Advoware) Vorgehensw..."
---

# /kanzlei-allgemein:kanzlei-cowork-kaltstart-interview

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

## Triage zu Beginn
1. Existiert bereits eine CLAUDE.md-Konfigurationsdatei oder wird erstmalig eingerichtet?
2. Welche Rechtsform hat die Kanzlei (Einzelanwalt, GbR, PartG, GmbH, AG) und wie viele Anwaelte?
3. Welche Buchhaltungssoftware ist im Einsatz (DATEV, Lexware, sevDesk, RA-MICRO, Advoware) oder keine?
4. Sind beA, E-Mail-Integration und Fristenbuch bereits eingerichtet oder müssen diese konfiguriert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 43, 43a BRAO — Allgemeine Berufspflichten: gelten ab Kanzleigruendung
- § 31a BRAO — beA-Einrichtungspflicht: sofort bei Zulassung
- § 51 BRAO — Berufshaftpflichtversicherung: Pflichtnachweis bei Kanzleigruendung
- § 8 PartGG — Haftungsstruktur in der Partnerschaftsgesellschaft

## Ablauf

1. Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/CLAUDE.md` prüfen.
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
- **Verzeichnis-Konvention** unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandate/<az>/`
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

- `/kanzlei-allgemein:fristenbuch-fuehren` — Hauptfristen pflegen
- `/kanzlei-allgemein:sekretariats-tagesbrief` — Tagesbrief morgens
- `/kanzlei-allgemein:versand-vor-check` — vor jedem Versand

## Rechtlicher Rahmen

- **BRAO** § 43a Verschwiegenheit § 50 Aktenführung § 51 Berufshaftpflicht § 31a beA-Pflicht
- **RVG** Gebührentabelle Anlage 1 Anlage 2 VV RVG
- **BORA** Berufsordnung der Rechtsanwälte (BRAK)
- **DSGVO** Art. 5 6 9 Auftragsverarbeitung Art. 28

## Hinweise

Mandantenkommunikation und folgenreiche Versandhandlungen verbleiben in anwaltlicher Verantwortung. Vor jedem Versand `versand-vor-check`.
