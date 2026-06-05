---
name: verl-isbn-vg
description: "Verl 016 Isbn Metadaten Vlb Und Meldeprozesse, Verl 017 Vg Wort Meldung Beteiligung Und Ausschuettung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 016 Isbn Metadaten Vlb Und Meldeprozesse, Verl 017 Vg Wort Meldung Beteiligung Und Ausschuettung

## Arbeitsbereich

Dieser Skill bündelt **Verl 016 Isbn Metadaten Vlb Und Meldeprozesse, Verl 017 Vg Wort Meldung Beteiligung Und Ausschuettung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-016-isbn-metadaten-vlb-und-meldeprozesse` | Verlagsrecht und Buchhandel: ISBN-Vergabe, Metadatenpflege, VLB-Meldeprozesse und bibliothekarische Pflichtablieferung — rechtliche Anforderungen und Praxisstandards. |
| `verl-017-vg-wort-meldung-beteiligung-und-ausschuettung` | VG Wort: Werkmeldung, Ausschüttungsrecht von Autoren und Verlagen, Wahrnehmungsvertrag, VGG §§ 27 ff. — Fristen, Verteilungsplan und Praxis. |

## Arbeitsweg

Für **Verl 016 Isbn Metadaten Vlb Und Meldeprozesse, Verl 017 Vg Wort Meldung Beteiligung Und Ausschuettung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-016-isbn-metadaten-vlb-und-meldeprozesse`

**Fokus:** Verlagsrecht und Buchhandel: ISBN-Vergabe, Metadatenpflege, VLB-Meldeprozesse und bibliothekarische Pflichtablieferung — rechtliche Anforderungen und Praxisstandards.

# Verl-016 · ISBN, Metadaten, VLB und Meldeprozesse

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

## 2. `verl-017-vg-wort-meldung-beteiligung-und-ausschuettung`

**Fokus:** VG Wort: Werkmeldung, Ausschüttungsrecht von Autoren und Verlagen, Wahrnehmungsvertrag, VGG §§ 27 ff. — Fristen, Verteilungsplan und Praxis.

# Verl-017 · VG Wort: Meldung, Beteiligung und Ausschüttung

## Zweck dieses Skills

Die **VG Wort** (Verwertungsgesellschaft Wort) nimmt Vergütungsansprüche für Urheber von Sprachwerken wahr, die durch Gesetz entstehen (z.B. Kopiergeräte-Vergütung nach § 54 UrhG, Bibliothekstantieme nach § 27 UrhG). Dieser Skill klärt, wer der VG Wort beitreten kann, welche Werke gemeldet werden müssen, wie Ausschüttungen berechnet werden und welche Rolle Verlage dabei spielen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 27 | Bibliothekstantieme: Vergütung für Verleih | https://dejure.org/gesetze/UrhG/27.html |
| UrhG §§ 54–54h | Geräte- und Speichermedienvergütung (Kopiervergütung) | https://dejure.org/gesetze/UrhG/54.html |
| VGG § 1 | Aufgaben der Verwertungsgesellschaft | https://www.gesetze-im-internet.de/vgg/__1.html |
| VGG § 27 | Wahrnehmungsvertrag: Rechte und Pflichten | https://www.gesetze-im-internet.de/vgg/__27.html |
| VGG § 28 | Tarifaufstellung der VG Wort | https://www.gesetze-im-internet.de/vgg/__28.html |
| VGG §§ 26 ff. | Verteilung der Einnahmen | https://www.gesetze-im-internet.de/vgg/ |
| BGH „Verlegeranteil" | Verleger können keine eigenen Vergütungsansprüche bei VG Wort geltend machen | https://www.bgh.de |

## Struktur der VG Wort

### Mitglieder
- **Berechtigte**: Urheber von Sprachwerken (Autoren, Journalisten, Übersetzer, Wissenschaftler) und **Verleger**.
- **Mitgliedschaft**: Erfordert Wahrnehmungsvertrag mit VG Wort.
- Wichtige Einschränkung (BGH, I ZR 198/13 „Verlegeranteil"): Verlage sind keine Urheber; sie dürfen bei VG Wort keine Tantiemen auf Kosten der Autoren beanspruchen, die auf Urheberrechten basieren. Verlegeranteil im Verteilungsplan wurde 2016 nach BGH-Urteil reformiert.

### Reformierter Verteilungsplan nach 2016
- Nach BGH-Urteil 2016: VG Wort hat Verteilungsplan geändert; Verlage erhalten nur noch Anteil aus Rechten, die Autoren ihnen ausdrücklich übertragen haben.
- Verlag-Beteiligung: Autor kann in Wahrnehmungsvertrag oder Verlagsvertrag Verlag an VG-Wort-Erlösen beteiligen (Abtretungsklausel).

## Werkmeldung

### Meldepflichten des Autors
- Autoren müssen ihre Werke aktiv bei VG Wort **melden**, um an der Ausschüttung zu partizipieren.
- Meldeportal: METIS (Meldung für wissenschaftliche Texte), Belletristik-Portal, Onlineportal T.O.M.
- Meldefrist: Jährlich; Werke müssen bis zum 31. Januar des Folgejahres für das Vorjahr gemeldet sein.

### Was kann gemeldet werden?
- **Bücher**: Sprachwerke mit ISBN; gedruckte und digitale Ausgaben.
- **Zeitschriften- und Zeitungsbeiträge**: Einzelne Artikel mit Angabe der Publikation.
- **Online-Texte** (METIS): Seit 2007 können Online-Texte ab 1.800 Zeichen gemeldet werden.
- **Wissenschaftliche Texte**: Hochschulschriften, Fachaufsätze.

### Mindeststärke
- Bücher: Mindestumfang 4 Normseiten (ca. 5.600 Zeichen).
- Periodika-Beiträge: Mindestlänge 1.800 Zeichen.

## Ausschüttung

### Arten der Ausschüttungen
1. **Bücher / Buchkapitel**: Anteil an Kopiergeräte-Vergütung (§§ 54 ff. UrhG), Bibliothekstantieme (§ 27 UrhG).
2. **Presse**: Zeitungs- und Zeitschriftenartikel aus Presseverlagen.
3. **Wissenschaft**: Sonderausschüttungen für wissenschaftliche Autoren (METIS-Auswertung).
4. **Online-Texte**: METIS-basierte Erfassung von Zugriffen auf Online-Texte.

### Ausschüttungskalender
- Bücher: Jährliche Hauptausschüttung; i.d.R. im Frühjahr.
- Presse: Vierteljährliche oder halbjährliche Ausschüttung.
- Nachschüttung: Falls nach der Hauptausschüttung noch Mittel verbleiben.

### Berechnung
- Verteilungsplan der VG Wort legt Punktewerte für verschiedene Werkarten fest.
- Buch mit hoher Auflage erhält mehr Punkte als Nischentitel.
- Punkte × Punktewert (€/Punkt aus Gesamteinnahmen) = Ausschüttung.

## Verlegeranteil und Vertragsbeteiligung

### Rechtslage nach 2016
- Verlag kann VG-Wort-Erlöse nur dann beanspruchen, wenn Autor ihm ausdrücklich seine VG-Wort-Ansprüche abgetreten oder zur Wahrnehmung übertragen hat.
- Klausel im Verlagsvertrag: „Der Autor überträgt dem Verlag die Hälfte seiner Ansprüche gegenüber der VG Wort."
- Ohne solche Klausel: Verlag erhält nichts von der VG Wort.

### Empfehlung
- Neue Verlagsverträge: Explizite Regelung der VG-Wort-Beteiligung (Anteil, Abrechnungsmodalität).
- Altverträge: Prüfen, ob eine Beteiligungsklausel vorhanden und nach 2016-Rechtslage noch wirksam ist.

## METIS — Online-Text-Meldung

- METIS (Meldung elektronischer Texte) erfasst Abrufe von Online-Texten durch Bibliotheken und Hochschulen.
- Autoren melden Online-Texte inklusive URL.
- VG Wort prüft Abrufzahlen; Ausschüttung je nach Zugriffszahl.
- Wichtig: URL muss stabil und dauerhaft sein; Texte hinter Paywalls sind meldbar.

## Typische Fallen

- **Meldefrist versäumt**: Jahresfrist bis 31. Januar; nicht rückwirkend nachholbar.
- **Verlegeranteil-Klausel fehlt**: Alter Verlagsvertrag ohne explizite Abtretungsklausel → Verlag erhält nach 2016 nichts.
- **Doppelmeldung**: Autor meldet für Kapitel im Sammelwerk; Herausgeber meldet das Gesamtwerk → VG Wort-Richtlinie regelt Abgrenzung; Abstimmung notwendig.
- **Falsche Angaben**: Auflagenzahl oder Seitenumfang falsch → Korrektur über METIS möglich.
- **Online-Text-URL veraltet**: METIS-Meldung mit alter URL → keine Zugriffe zählbar.

## Checkliste VG Wort

- [ ] Wahrnehmungsvertrag mit VG Wort abgeschlossen (Autor)
- [ ] Alle Bücher, Artikel, Online-Texte des Vorjahres bis 31. Januar gemeldet
- [ ] Verlagsvertrag: Verleger-Beteiligungsklausel vorhanden und rechtswirksam (post-2016)
- [ ] METIS-Meldungen: URLs geprüft und aktuell
- [ ] Ausschüttungsbelege für Buchhaltung gespeichert
- [ ] Sammelwerk: Abgrenzung Autor-Kapitel / Herausgeber-Gesamtwerk koordiniert

## Quellenreferenzen

- VGG: https://www.gesetze-im-internet.de/vgg/
- UrhG §§ 54–54h: https://dejure.org/gesetze/UrhG/54.html
- VG Wort, Verteilungsplan: https://www.vgwort.de/verguetungen/verteilungsplan.html
- BGH „Verlegeranteil" I ZR 198/13: https://www.bgh.de
- VG Wort METIS: https://tom.vgwort.de

## Output-Formate

- **Meldeliste**: Alle Werke mit Meldefristen und -status
- **Ausschüttungsprognose**: Grobe Berechnung auf Basis von Auflage und Werkart
- **Verleger-Beteiligungscheck**: Vertragsklausel vorhanden / fehlt / reformbedürftig
- **METIS-Melde-Entwurf**: Strukturiertes Formular für Online-Texte
- **Jahresabschluss-Auswertung**: Tatsächliche Ausschüttungen vs. Erwartungen
