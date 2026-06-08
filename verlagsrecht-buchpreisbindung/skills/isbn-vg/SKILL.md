---
name: isbn-vg
description: "Verlagsrecht und Buchhandel: ISBN-Vergabe, Metadatenpflege, VLB-Meldeprozesse und bibliothekarische Pflichtablieferung — rechtliche Anforderungen und Praxisstandards im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung."
---

# Verl-016 · ISBN, Metadaten, VLB und Meldeprozesse

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck dieses Skills

ISBN, Metadaten und VLB-Einträge sind das **operative Rückgrat** des deutschen Buchhandels. Fehlerhafte oder fehlende Metadaten führen zu Lieferproblemen, Preisbindungsmängeln und rechtlichen Risiken. Dieser Skill klärt alle Pflichten, Standards und Prozesse rund um Buchidentifikation und Metadateninfrastruktur.

## Rechtsgrundlagen und Standards

| Grundlage | Inhalt | Quelle |
|-----------|--------|-------|
| Pflichtablieferungsgesetz (PflABG) | Pflichtablieferung an Deutsche Nationalbibliothek | https://www.gesetze-im-internet.de/pflabg/ |
| Landesgesetze zur Pflichtablieferung | Ablieferung an Staatsbibliotheken der Länder | (länderspezifisch) |
| BuchPrG § 3 | Preisfestsetzung; VLB-Meldung als faktischer Standard | https://www.gesetze-im-internet.de/buchprg/__3.html |
| ISO 2108 | Internationale Norm für ISBN-Vergabe | https://www.iso.org/standard/36563.html |
| ONIX for Books | Internationaler Metadatenstandard | https://www.editeur.org/83/Overview/ |
| Börsenverein VLB-Richtlinien | Pflichtfelder und Qualitätsstandards | https://www.vlb.de |

## ISBN-System

### Was ist eine ISBN?
- ISBN (International Standard Book Number): 13-stellige eindeutige Kennzeichnung jedes Buchtitels.
- Aufbau: Präfix (978 oder 979) + Gruppen-ID (978-3 für deutschsprachige Verlage) + Verlags-ID + Titel-ID + Prüfziffer.
- **Jede Ausgabe** (Hardcover, Paperback, E-Book EPUB, E-Book PDF, Hörbuch) erhält eine eigene ISBN.
- Neuauflage: Neue ISBN, da veränderter Inhalt.

### ISBN-Vergabe
- In Deutschland: Deutsche ISBN-Agentur der Deutschen Nationalbibliothek (ISBN-Agentur Frankfurt).
- Verlag beantragt ISBN-Kontingent (Blocks) bei der ISBN-Agentur.
- Self-Publishing-Autoren: Eigene ISBN über VLB-Direktregistrierung oder über Plattform (KDP, BoD vergeben ISBNs).

### ISBN-Pflicht
- Gesetzliche Pflicht zur ISBN-Nutzung besteht nicht; aber Buchhandel und Bibliotheken ohne ISBN nicht handhabbar.
- De-facto-Standard für alle im Buchhandel vertriebenen Bücher.

## VLB — Verzeichnis Lieferbarer Bücher

### Was ist das VLB?
- Buchbranchen-Datenbank des Börsenvereins: über 1,4 Millionen lieferbare Titel.
- Kernfunktion: Händler und Bibliotheken recherchieren Lieferbarkeit, Preis, Bezugsquelle.
- Verlagsvertrieb und Auslieferung füttern VLB mit Titeldaten.

### Pflichtfelder im VLB
- ISBN-13
- Titel, Untertitel, Reihentitel
- Autor(en), Herausgeber
- Verlag, Erscheinungsjahr
- Preisgebundener Ladenpreis (inkl. MwSt.)
- Ausgabetyp (Hardcover, Paperback, E-Book EPUB etc.)
- Warengruppe (ONIX / Börsenverein-Warengruppen-Systematik)
- Lieferstatus: lieferbar, vergriffen, erscheint, vorbestellbar

### ONIX-Standard
- ONIX for Books (v2.1 und v3.0): Internationaler XML-Metadatenstandard.
- VLB und alle großen Buchhandels-IT-Systeme akzeptieren ONIX.
- Verlag oder Auslieferung sendet ONIX-Feed → VLB, Händler-Systeme, Amazon-Katalog.

## Pflichtablieferung an die Deutsche Nationalbibliothek

### Pflichtablieferungsgesetz (PflABG 2006)
- Jeder Verlag und jede Institution, die ein Werk in Deutschland veröffentlicht, muss **Pflichtexemplare** an die DNB abliefern.
- Umfang: 2 Pflichtexemplare (1× Frankfurt, 1× Leipzig) für körperliche Medien.
- E-Books und Online-Publikationen: DNB hat Recht auf Ablieferung eines digitalen Pflichtexemplars.
- Frist: Unverzüglich nach Erscheinen; spätestens bei Erscheinen gedruckter Ausgabe.

### Landesbibliotheken
- Viele Bundesländer haben eigene Pflichtablieferungsgesetze (z.B. Bayern, NRW, Hessen).
- Ablieferung an die jeweilige Staatsbibliothek des Erscheinungortes.
- Empfehlung: Verlagssitz als Erscheinungsort maßgeblich; alle für das Bundesland relevanten Bibliotheken checken.

### Folgen bei Nichtablieferung
- Bußgeld möglich; DNB kann Ablieferung anfordern.
- Für die meisten Verlage administrative Routine, aber bei Vergessen kann aufwendige Nachlieferung nötig werden.

## Metadatenqualität und -pflege

### Bedeutung für den Buchhandel
- Schlechte Metadaten → Buch nicht auffindbar → niedrige Verkaufszahlen.
- Falsche Preisangabe im VLB → Preisbindungsrisiko, Beschwerden vom Buchhandel.
- Fehlende Kategorisierung → falsche Platzierung in Buchhandel und Online-Regal.

### Best Practices
1. **Beschreibungstext (Klappentext)**: 200–400 Wörter; wichtig für SEO und Buchhandels-Webseiten.
2. **Schlagwörter / Keywords**: Sachgebiet, Thema, Zielgruppe; erhöhen Auffindbarkeit.
3. **Coverabbildung**: Hochauflösend (mind. 300 dpi oder 1500px), JPG oder PNG.
4. **Bisac / Thema-Codes**: International gebräuchliche Buchkategorien.
5. **Erscheinungsdatum**: Exact date für Vorbestellungs-Management.
6. **Autor-Bio und Foto**: Für Online-Buchhandel und Presse.

## Typische Fallen

- **E-Book ohne eigene ISBN**: E-Book und Print mit derselben ISBN → Kaufabwicklungs- und Preisbindungsprobleme.
- **Vergriffen-Status vergessen**: Buch vergriffen, aber VLB-Status immer noch „lieferbar" → Buchhandel bestellt und erhält keine Lieferung; Forderungen.
- **Preisänderung nur in der Buchhaltung, nicht im VLB**: Buchhandel kauft noch zum alten Preis; Differenz schwer klärbar.
- **Pflichtablieferung vergessen**: Erst nach Jahren fragt DNB nach.
- **Schlechte Metadaten für E-Books**: ISBN korrekt, aber falsches Format (MOBI statt EPUB) in ONIX → Amazon liefert falsches Format.

## Checkliste Metadaten und ISBN

- [ ] Eigene ISBN für jede Ausgabe vergeben
- [ ] VLB-Eintrag mit allen Pflichtfeldern vollständig
- [ ] Ladenpreis aktuell und korrekt im VLB
- [ ] Pflichtexemplare an DNB und Landesbibliotheken abgeliefert
- [ ] Coverabbildung hochauflösend vorhanden
- [ ] ONIX-Feed aktuell und fehlerfrei
- [ ] Lieferstatus korrekt gesetzt (lieferbar / vergriffen / Vorbestellung)

## Quellenreferenzen

- PflABG: https://www.gesetze-im-internet.de/pflabg/
- Deutsche Nationalbibliothek, Pflichtablieferung: https://www.dnb.de/pflichtablieferung
- VLB: https://www.vlb.de
- ONIX for Books: https://www.editeur.org/83/Overview/
- ISBN-Agentur Deutschland: https://www.dnb.de/isbn

## Output-Formate

- **Metadaten-Audit**: Alle ISBN × Pflichtfelder × Status
- **VLB-Update-Protokoll**: Geplante und durchgeführte Metadatenänderungen
- **Pflichtablieferungs-Checkliste**: DNB + Landesbibliotheken pro Titel
- **ONIX-Qualitätsprüfbericht**: Fehlende und fehlerhafte Felder
- **ISBN-Vergabe-Register**: Alle vergebenen ISBNs mit Zuordnung

