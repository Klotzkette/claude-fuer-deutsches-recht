---
name: verl-fachbuch-verlagsinsolvenz
description: "Verl 022 Fachbuch Aktualisierung Loseblatt Und Online Datenbank, Verl 025 Verlagsinsolvenz Rechte Rueckfall Und Lagerbestand: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 022 Fachbuch Aktualisierung Loseblatt Und Online Datenbank, Verl 025 Verlagsinsolvenz Rechte Rueckfall Und Lagerbestand

## Arbeitsbereich

Dieser Skill bündelt **Verl 022 Fachbuch Aktualisierung Loseblatt Und Online Datenbank, Verl 025 Verlagsinsolvenz Rechte Rueckfall Und Lagerbestand** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-022-fachbuch-aktualisierung-loseblatt-und-online-datenbank` | Verlagsrecht: Fachbuch-Aktualisierungen, Loseblattwerke und Online-Datenbanken — Nutzungsrechte, Datenbankrecht, Aktualisierungspflichten, Lizenzmodelle und Preisbindung. |
| `verl-025-verlagsinsolvenz-rechte-rueckfall-und-lagerbestand` | Verlagsrecht: Verlagsinsolvenz — Rückfall von Nutzungsrechten an Autoren, Lagerbestandsverwertung, InsO §§ 103–119, UrhG §§ 41–42 und praktische Schritte für betroffene Autoren. |

## Arbeitsweg

Für **Verl 022 Fachbuch Aktualisierung Loseblatt Und Online Datenbank, Verl 025 Verlagsinsolvenz Rechte Rueckfall Und Lagerbestand** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-022-fachbuch-aktualisierung-loseblatt-und-online-datenbank`

**Fokus:** Verlagsrecht: Fachbuch-Aktualisierungen, Loseblattwerke und Online-Datenbanken — Nutzungsrechte, Datenbankrecht, Aktualisierungspflichten, Lizenzmodelle und Preisbindung.

# Verl-022 · Fachbuch, Aktualisierung, Loseblatt und Online-Datenbank

## Zweck dieses Skills

Juristische, medizinische und wissenschaftliche Fachbücher stellen besondere Anforderungen an **Aktualität, Rechteketten und Lizenzmodelle**. Loseblattwerke und Online-Datenbanken haben eigene Rechtsregimes (Datenbankrecht, Lizenzvertragsrecht). Dieser Skill systematisiert diese Besonderheiten und klärt Aktualisierungspflichten, Haftungsfragen und Preisbindung.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 4 | Sammelwerke und Datenbankwerke | https://dejure.org/gesetze/UrhG/4.html |
| UrhG § 87a | Datenbankrecht: Sui-generis-Schutz | https://dejure.org/gesetze/UrhG/87a.html |
| UrhG § 87b | Ausschließlichkeitsrecht des Datenbankerstellers | https://dejure.org/gesetze/UrhG/87b.html |
| UrhG § 87c | Schranken des Datenbankrechts | https://dejure.org/gesetze/UrhG/87c.html |
| BGB § 536 | Mietmängel bei Dauerschuldverhältnis (Online-Lizenz) | https://dejure.org/gesetze/BGB/536.html |
| BGB §§ 305 ff. | AGB-Recht für Online-Datenbankverträge | https://dejure.org/gesetze/BGB/305.html |
| BuchPrG § 2 | Geltungsbereich: Bücher, auch Loseblatt | https://www.gesetze-im-internet.de/buchprg/__2.html |

## Loseblattwerke

### Charakteristika
- Loseblattwerke (z.B. juristische Kommentare, Steuerhandbücher) erscheinen in Mappen mit austauschbaren Seiten.
- **Aktualisierungslieferungen**: Periodische Lieferungen ersetzen veraltete Seiten; Grundwerk + Ergänzungslieferungen.
- Jede Lieferung ist ein eigenständiges Erscheinen; eigene ISBN oder EAN für Abonnements.

### Urheberrecht und Datenbankrecht
- Loseblattwerk als Ganzes: Sammelwerkschutz (§ 4 UrhG) beim Herausgeber.
- Datenbank-Sui-generis-Schutz (§ 87a UrhG): Wenn systematische Sammlung mit erheblicher Investition → Datenbankersteller hat Ausschließlichkeitsrecht.
- Einzelbeiträge: Urheberrecht der Beitragsautoren bleibt.

### Aktualisierungspflicht
- Keine gesetzliche Pflicht zur Aktualisierung; abhängig von Vertrags- und AGB-Gestaltung.
- Abonnementvertrag: Implizite Pflicht, Aktualisierungen pünktlich und inhaltlich korrekt zu liefern.
- Ausfall einer Lieferung → Mängelansprüche des Abonnenten (§§ 536 ff. BGB analog).

### Haftung für veraltete Fachbuch-Inhalte
- Nutzer verlässt sich auf Rechts- oder Medizinfachbuch → berufsfehlerhafter Rat auf Basis veralteter Information.
- Haftung des Verlags: Grundsätzlich kein Beratungsvertrag; Verlag haftet nur bei besonderer Vertrauenswerbung oder arglistigem Verschweigen von Veraltung.
- **Disclaimer**: Verlag empfiehlt Eigenprüfung und schließt Haftung für konkrete Beratungsfolgen aus (AGB-rechtlich weitgehend zulässig bei B2B-Verträgen).

## Online-Datenbanken

### Datenbankrecht (§§ 87a ff. UrhG)
- Voraussetzung: Wesentliche Investition in Beschaffung, Überprüfung oder Darstellung der Inhalte.
- **Schutzinhalt**: Verbot der wesentlichen Entnahme aus der Datenbank (§ 87b UrhG).
- Schranken (§ 87c UrhG): Entnahme für private Nutzung, wissenschaftliche Forschung.
- Schutzfrist: 15 Jahre ab Fertigstellung; bei wesentlicher Investition in Aktualisierung neu beginnend.

### Lizenzmodelle für Online-Fachdatenbanken

| Modell | Charakteristika | Preisbindung |
|--------|----------------|-------------|
| Einzelabonnement | Jahres-Lizenz pro Nutzer | Nein (Dienstleistung) |
| Institutionslizenz | Organisationsweiter Zugang; Concurrent-User-Modell | Nein |
| Transaktionslizenz | Zahlung pro Abruf / Dokument | Nein |
| Open-Access-Datenbank | Kostenloser Zugang | Nein |
| Hybrid-Modell | Print + Online-Zugang | BuchPrG für Print-Anteil |

### Vertragsgestaltung Online-Lizenz
- Definitionen: Authorized Users, Berechtigter Verwendungszweck, IP-Ranges, Walk-in-User.
- Zugangssteuerung: IP-basiert, Login-basiert, Shibboleth (Hochschulen).
- Verbotene Nutzungen: Systematisches Herunterladen (Harvesting), Text-Mining ohne Lizenz, Weitergabe an Dritte.
- SLA (Service Level Agreement): Verfügbarkeitsgarantie (z.B. 99,5 %); Konsequenzen bei Ausfall.
- Kündigung: Mindestlaufzeit, Kündigungsfristen; Daten-Export nach Kündigung.

## Fachbuch-Preisbindung

- Gedruckte Loseblattwerke: Unterliegen BuchPrG (Bücher i.S.d. § 2 BuchPrG).
- Ergänzungslieferungen: Jede Lieferung ist selbständig preisgebunden oder wird im Abonnementpreis gebunden; Verlag legt Abonnementpreis fest.
- Online-Datenbank: **Kein Anwendungsbereich** des BuchPrG; keine Buchpreisbindung für rein digitale Datenbanken.
- Kombinationsprodukte (Print + Online-Zugang): Print-Anteil preisgebunden; Online-Anteil nicht → getrennte Preisauszeichnung empfohlen.

## Aktualisierungsbedingte Nutzungsrechte

- Neue Autoren für Aktualisierungslieferungen: Neue Verträge nötig oder bestehender Vertrag schließt laufende Aktualisierungen ein.
- Übernahme von Passagen aus alten Auflagen durch neue Autoren: Klärung der Rechtekette (alte Autoren vs. neue Autoren).
- Redaktionelle Überarbeitung ohne neue Schöpfungshöhe: Kein neues Urheberrecht des Bearbeiters.

## Typische Fallen

- **Datenbankschutz vergessen**: Wettbewerber extrahiert systematisch Daten aus Online-Datenbank → Verleger hat keine Klage eingeleitet, weil § 87a UrhG nicht bekannt.
- **Kündigung ohne Daten-Export-Klausel**: Nutzer kündigt Online-Datenbank; Verlag sperrt Zugang; Nutzer verliert alle Annotationen → Vertragsstreit.
- **Loseblatt: Preisänderung für Ergänzungslieferungen nicht kommuniziert**: Abonnent bestellt unter altem Preis, zahlt nicht → Mahnung und Lieferstopp; VerlG §§ 24, 7 analog.
- **Haftungsdisclaimer unwirksam bei B2C**: Verbraucher-AGB-Recht (§ 309 BGB) schränkt Haftungsausschluss ein.

## Checkliste Fachbuch / Datenbank

- [ ] Datenbankschutz (§ 87a UrhG) geprüft und ggf. geltend gemacht
- [ ] Lizenzvertrag für Online-Datenbank: Authorized Users, Verbote, SLA
- [ ] Aktualisierungslieferungen: Preisänderungen kommuniziert
- [ ] Haftungsdisclaimer AGB-rechtskonform (B2B vs. B2C)
- [ ] Rechtekette bei neuen Autoren für Aktualisierungen gesichert
- [ ] Kündigung: Daten-Export-Klausel im Online-Lizenzvertrag

## Quellenreferenzen

- UrhG §§ 87a–87c: https://dejure.org/gesetze/UrhG/87a.html
- BuchPrG § 2: https://www.gesetze-im-internet.de/buchprg/__2.html
- EuGH C-444/02 (Datenbankrecht): https://eur-lex.europa.eu
- BGH „Datenbank-Harvesting" I ZR 48/13: https://www.bgh.de
- BGB §§ 305–310: https://dejure.org/gesetze/BGB/305.html

## Output-Formate

- **Datenbankrechts-Check**: Schutzvoraussetzungen § 87a UrhG bejaht / verneint
- **Online-Lizenzvertrag-Muster**: Authorized Users, SLA, Verbote, Kündigung
- **Aktualisierungsplan**: Lieferfristen und Preise für nächste Ergänzungslieferungen
- **Haftungsdisclaimer-Check**: AGB-Konformität
- **Daten-Export-Klausel** für Lizenzverträge

## 2. `verl-025-verlagsinsolvenz-rechte-rueckfall-und-lagerbestand`

**Fokus:** Verlagsrecht: Verlagsinsolvenz — Rückfall von Nutzungsrechten an Autoren, Lagerbestandsverwertung, InsO §§ 103–119, UrhG §§ 41–42 und praktische Schritte für betroffene Autoren.

# Verl-025 · Verlagsinsolvenz: Rechterückfall und Lagerbestand

## Zweck dieses Skills

Die **Insolvenz eines Verlags** ist für Autoren ein Worst-Case-Szenario: Honorare bleiben aus, Bücher werden nicht mehr vertrieben, Nutzungsrechte sind unklar. Dieser Skill klärt die Rechtslage beim Verlagsinsolvenzverfahren, die Möglichkeiten des Rechterückfalls, den Umgang mit Lagerbeständen und die Schritte, die betroffene Autoren unternehmen müssen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| InsO § 103 | Wahlrecht des Insolvenzverwalters bei gegenseitigen Verträgen | https://www.gesetze-im-internet.de/inso/__103.html |
| InsO § 108 | Fortsetzung von Dienst- und Arbeitsverhältnissen | https://www.gesetze-im-internet.de/inso/__108.html |
| InsO § 119 | Unwirksamkeit von Lösungsklauseln | https://www.gesetze-im-internet.de/inso/__119.html |
| InsO § 35 | Insolvenzmasse: alle pfändbaren Rechte des Schuldners | https://www.gesetze-im-internet.de/inso/__35.html |
| UrhG § 41 | Rückruf wegen Nichtausübung | https://dejure.org/gesetze/UrhG/41.html |
| VerlG § 7 | Rücktritt bei Nichterscheinen | https://www.gesetze-im-internet.de/verlg/__7.html |
| BGB § 346 | Rücktrittsfolgen: Rückgewähr | https://dejure.org/gesetze/BGB/346.html |

## Verlagsinsolvenz: Basisszenarien

### Szenario 1: Verlag stellt Betrieb ein (vorläufige Insolvenz)
- Vorläufiger Insolvenzverwalter übernimmt; prüft ob Fortführung oder Zerschlagung.
- Bis zur Eröffnung: Verlag kann keine neuen Verträge eingehen; laufende Verträge bleiben bestehen.

### Szenario 2: Insolvenzeröffnung
- Insolvenzverwalter (IV) tritt in alle Verlagsverträge ein (§ 103 InsO).
- IV hat **Wahlrecht**: Verlagsvertrag erfüllen (Honorar zahlen, Buch weiter vertreiben) oder nicht erfüllen (Vertrag gilt als nicht erfüllt; Autor hat Schadensersatzanspruch als einfache Insolvenzforderung).

### Szenario 3: Masselosigkeit / Scheitern der Fortführung
- Insolvenzverfahren wird mangels Masse eingestellt.
- Autor erhält keine Honorare; Nutzungsrechte fallen zurück (§ 41 UrhG nach Wartefrist).

## Das Wahlrecht des Insolvenzverwalters (§ 103 InsO)

- IV kann für jeden Verlagsvertrag wählen:
 - **Erfüllung wählen**: IV zahlt ausstehende Honorare aus Insolvenzmasse und kann Nutzungsrechte weiterhin ausüben.
 - **Nichterfüllung wählen / schweigen**: Der Verlagsvertrag gilt als nicht erfüllt; Autor hat Schadensersatzanspruch; Nutzungsrechte fallen zurück.
- **Wichtig**: Schweigen des IV = Nichterfüllung nach Fristsetzung durch den Autor (§ 103 Abs. 2 InsO).
- **Fristsetzung durch Autor**: Autor schreibt IV an und fordert ihn auf, binnen angemessener Frist (2–4 Wochen) zu wählen.

## Rechterückfall an Autor

### Nach Nichterfüllungswahl des IV
- Nutzungsrechte fallen kraft Gesetzes an Autor zurück; keine gesonderte Erklärung nötig.
- Autor kann Rechte an neuen Verlag weiterlizenzieren.
- Schadensersatz (ausstehende Honorare, entgangener Gewinn): Als einfache Insolvenzforderung zur Tabelle anmelden.

### UrhG § 41 — Rückruf wegen Nichtausübung (zusätzliches Instrument)
- Wenn IV die Nutzungsrechte nicht ausübt und Interessen des Autors erheblich beeinträchtigt: § 41 UrhG-Rückruf möglich.
- Frist: Rückruf nach 2 Jahren Nichtausübung; Ankündigung 3 Monate vorher.
- Praktisch: Oft schneller als § 103 InsO-Weg; hängt von tatsächlichem Vertriebsstopp ab.

## Forderungsanmeldung zur Insolvenztabelle

### Was anmelden?
- Ausstehende Honoraransprüche.
- Vorschüsse, die noch nicht durch Tantiemen verdient sind (nicht rückzahlbar, wenn Verlag die Erscheinungspflicht nicht erfüllt hat).
- Schadensersatz aus Rücktritt.

### Wie anmelden?
- Formular: Forderungsanmeldung beim Insolvenzverwalter.
- Frist: Anmeldefrist in Bekanntmachung des Insolvenzverfahrens (Bundesanzeiger); typisch 3 Monate.
- Quote: Einfache Forderungen erhalten typisch 2–20 % der Forderungssumme; Masseverbindlichkeiten werden vorrangig befriedigt.

## Lagerbestandsverwertung

- Lagerbestände (Bücher im Verlagslager) sind Teil der Insolvenzmasse.
- IV kann entscheiden: Bücher weiter verkaufen, Lager abverkaufen oder Bücher makulieren.
- **Preisbindung**: Auch in der Insolvenz gilt die Preisbindung für lieferbare Bücher, solange der Ladenpreis nicht förmlich aufgehoben wurde.
- Notverkauf zu Ramschpreisen: Nur zulässig, wenn Verlag den Preis zuvor aufgehoben hat oder wenn es sich um Mängelexemplare handelt.
- Übernahme des Verlagsprogramms durch Erwerber: Käufer tritt in bestehende Verlagsverträge ein (§ 25 UmwG analog oder vertragliche Gestaltung); Zustimmung der Autoren erforderlich.

## Schutzklauseln im Verlagsvertrag (präventiv)

1. **Insolvenzklausel (Vorsicht!)**: Klauseln, die den Vertrag bei Insolvenz des Verlags automatisch beenden, sind nach § 119 InsO unwirksam.
2. **Rückruf-Klausel**: Vertraglich vereinbartes Rückrufrecht bei Einstellung des Vertriebs, Insolvenzantrag oder Verstoß gegen Erscheinungspflicht.
3. **Treuhandkonto für Vorschüsse**: Vorschussbetrag auf Treuhandkonto; fällt nicht in Insolvenzmasse des Verlags.
4. **Mindestumsatzklausel**: Wenn Umsatz unter X → Autor kann Rücktritt erklären.

## Typische Fallen

- **Fristsetzung an IV vergessen**: Autor wartet passiv; IV wählt nicht → Limbo-Zustand über Monate.
- **Forderung nicht angemeldet**: Anmeldefrist versäumt → Forderung grundsätzlich ausgeschlossen (§ 177 InsO).
- **Nutzungsrecht-Rückfall nicht beansprucht**: Autor nimmt an, Rechte seien von allein zurückgefallen, wartet → Unklarheit; IV bestreitet Rückfall.
- **Verlagsübernahme ohne Zustimmung**: Erwerber des insolventen Verlags will weiter Bücher verkaufen; ohne Autorenvertragsübernahme ist dies rechtswidrig.

## Checkliste Verlagsinsolvenz

- [ ] Insolvenzbekanntmachung im Bundesanzeiger gefunden
- [ ] Fristsetzung an IV nach § 103 Abs. 2 InsO gesendet (Frist: 2–4 Wochen)
- [ ] Forderungsanmeldung zur Tabelle eingereicht (ausstehende Honorare, Schadensersatz)
- [ ] Anmeldefrist beachtet (aus Bekanntmachung)
- [ ] Bei Nichtausübung: § 41 UrhG-Rückruf-Ankündigung gesendet
- [ ] Neuen Verlag suchen / Selbstveröffentlichung prüfen

## Quellenreferenzen

- InsO §§ 103, 119: https://www.gesetze-im-internet.de/inso/__103.html
- UrhG § 41: https://dejure.org/gesetze/UrhG/41.html
- VerlG § 7: https://www.gesetze-im-internet.de/verlg/__7.html
- BGH, Urt. v. 25.10.2012 – IX ZR 207/11 (Insolvenz und Verlagsvertrag): https://www.bgh.de
- Insolvenzbekanntmachungen: https://www.insolvenzbekanntmachungen.de

## Output-Formate

- **Fristsetzungs-Schreiben** an Insolvenzverwalter (§ 103 Abs. 2 InsO)
- **Forderungsanmeldung**: Standardformular mit Berechnung
- **Rückruf-Ankündigung** nach § 41 UrhG
- **Nutzungsrecht-Rückfall-Erklärung** (für neuen Verlag)
- **Neuen-Verlagsvertrag-Briefing**: Was braucht der neue Verlag an Unterlagen
