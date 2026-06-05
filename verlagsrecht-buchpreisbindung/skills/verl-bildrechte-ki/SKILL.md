---
name: verl-bildrechte-ki
description: "Verl 018 Bildrechte Karten Tabellen Und Drittmaterial, Verl 019 Ki Generierte Inhalte Im Verlag: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 018 Bildrechte Karten Tabellen Und Drittmaterial, Verl 019 Ki Generierte Inhalte Im Verlag

## Arbeitsbereich

Dieser Skill bündelt **Verl 018 Bildrechte Karten Tabellen Und Drittmaterial, Verl 019 Ki Generierte Inhalte Im Verlag** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-018-bildrechte-karten-tabellen-und-drittmaterial` | Verlagsrecht: Bildrechte, Kartenrechte, Tabellen und sonstiges Drittmaterial im Buch — Nutzungsrechte einholen, Bildrechtsverträge, CC-Lizenzen und Haftung bei Fehlern. |
| `verl-019-ki-generierte-inhalte-im-verlag` | Verlagsrecht: KI-generierte Texte, Bilder und Übersetzungen im Verlag — Urheberrechtsstatus, Kennzeichnungspflichten, Vertragsklauseln und Haftungsrisiken (EU AI Act, UrhG). |

## Arbeitsweg

Für **Verl 018 Bildrechte Karten Tabellen Und Drittmaterial, Verl 019 Ki Generierte Inhalte Im Verlag** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-018-bildrechte-karten-tabellen-und-drittmaterial`

**Fokus:** Verlagsrecht: Bildrechte, Kartenrechte, Tabellen und sonstiges Drittmaterial im Buch — Nutzungsrechte einholen, Bildrechtsverträge, CC-Lizenzen und Haftung bei Fehlern.

# Verl-018 · Bildrechte, Karten, Tabellen und Drittmaterial

## Zweck dieses Skills

Bücher enthalten häufig **Drittmaterial**: Fotografien, Illustrationen, Grafiken, Karten, Tabellen aus anderen Quellen, Kunstabbildungen und Zitate. Für jede dieser Materialarten gelten eigene Rechteregeln. Dieser Skill kartiert alle Materialtypen, die Anforderungen an Nutzungsrechtseinholung und die Haftungsrisiken bei Fehlern.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 2 Abs. 1 Nr. 4–6 | Schutz von Lichtbildwerken, Landkarten, Darstellungen | https://dejure.org/gesetze/UrhG/2.html |
| UrhG § 51 | Zitatrecht: erlaubte Nutzung ohne Genehmigung | https://dejure.org/gesetze/UrhG/51.html |
| UrhG § 60a | Bildungsnutzung: begrenzte Nutzung für Lehre | https://dejure.org/gesetze/UrhG/60a.html |
| UrhG § 72 | Lichtbilder (ohne Schöpfungshöhe): Schutzfrist 50 Jahre | https://dejure.org/gesetze/UrhG/72.html |
| UrhG § 64 | Urheberrechtsschutz: 70 Jahre nach Tod des Urhebers | https://dejure.org/gesetze/UrhG/64.html |
| KUG § 22 | Recht am eigenen Bild | https://dejure.org/gesetze/KunstUrhG/22.html |
| DSGVO Art. 4 Nr. 1 | Personenfoto als personenbezogenes Datum | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679 |

## Materialtypen und ihre rechtliche Behandlung

### 1. Fotografien (Lichtbildwerke, § 2 Abs. 1 Nr. 5 UrhG)
- **Schutz**: 70 Jahre nach Tod des Fotografen (§ 64 UrhG).
- **Einfache Lichtbilder** (ohne Schöpfungshöhe, § 72 UrhG): Leistungsschutzrecht; Schutzfrist 50 Jahre ab Entstehung.
- **Nutzungsrechtseinholung**: Schriftlicher Bildrechtevertrag; Nutzungsarten (Print, E-Book, Online, Werbung) exakt benennen.
- **Bildagenturen**: Getty, iStock, Shutterstock bieten Lizenzen; RF (Royalty Free) vs. RM (Rights Managed) unterscheiden.
- **Personenfoto**: Zusätzlich Einwilligung der abgebildeten Person (KUG § 22, DSGVO Art. 4 Nr. 1).

### 2. Kunstabbildungen
- Kunstwerke sind urheberrechtlich geschützt (70 Jahre post mortem).
- **Museum / Galerie**: Eigenes Lichtbild-Leistungsschutzrecht an der Abbildung? (streitig nach EuGH, C-161/17 — „Preußischer Kulturbesitz"; BGH hat Leistungsschutzrecht für 2D-Abbildungen gemeinfreier Werke verneint).
- Nutzungsrecht beim Fotograf (der das Kunstwerk fotografiert hat) oder beim Museum (vertragliche Vereinbarung).

### 3. Illustrationen und Grafiken
- Schutz als Werke der bildenden Kunst oder angewandten Kunst.
- Auftragswerke: Kein automatischer Rechteübergang; ausdrückliche schriftliche Einräumung nötig.
- Infografiken, Diagramme: Können als Datenbankwerke (§ 4 UrhG) oder Schriftwerke schutzfähig sein.

### 4. Karten und kartografische Erzeugnisse
- Karten genießen Urheberrechtsschutz (§ 2 Abs. 1 Nr. 7 UrhG) und ggf. Datenbankschutz (§ 87b UrhG).
- Topografische Karten des BKG (Bundesamt für Kartographie): Lizenz erforderlich; Gebühren.
- OpenStreetMap: CC BY-SA 2.0; Share-Alike kann bei Buchveröffentlichung problematisch sein.
- Google Maps: Keine kommerzielle Nutzung ohne Lizenz.

### 5. Tabellen und Statistiken
- Daten selbst sind nicht urheberrechtsfähig; Darstellung (Tabelle) kann als Datenbankwerk geschützt sein.
- Amtliche Statistiken (Destatis, Eurostat): Häufig frei nutzbar mit Quellenangabe; Lizenzbedingungen prüfen.
- Unternehmensstatistiken: Urheberrecht beim Unternehmen; Lizenz erforderlich.

### 6. Zitate (§ 51 UrhG)
- **Zitat aus Sprachwerk**: Zur Erläuterung, Belegung, Kritik; Umfang muss durch Zweck gerechtfertigt sein.
- **Bildzitat**: Möglich, aber restriktiv; muss im Text inhaltlich behandelt werden.
- **Musikzitat**: In Büchern über Musik zulässig; Notenzitate erfordern i.d.R. Verlagserlaubnis.
- Grenze: Keine „Textzitate als Hauptinhalt"; keine Zitatensammlungen ohne Auseinandersetzung.

## Praxis der Bildrechtsverwaltung

### Bildrechte-Protokoll
Für jede Abbildung im Buch führen:
- Abbildungsnummer / Bezeichnung
- Urheber / Fotograf
- Quelle / Bildagentur
- Lizenzdatum und Vertragsreferenz
- Lizenzierte Nutzungsarten
- Gültigkeitsdauer der Lizenz
- Honorar / Lizenzgebühr

### Vertragliche Absicherung im Autorenvertrag
- Klausel: „Der Autor sichert zu, dass alle im Manuskript verwendeten Abbildungen, Tabellen und Zitate entweder in seinen eigenen Rechten stehen oder mit gültigen Nutzungsrechten versehen sind. Der Autor stellt den Verlag von Ansprüchen Dritter frei."
- Freistellungsklausel: Verlag kann Freistellungsanspruch gegen Autor geltend machen, wenn Bildrechts-Klage kommt.

## Verwaiste Werke (§ 79b UrhG)

- **Verwaiste Werke**: Urheberrechtlich geschützte Werke, deren Rechteinhaber nicht ermittelbar oder auffindbar ist.
- UrhG § 79b (seit 2014): Öffentliche Einrichtungen dürfen verwaiste Werke unter bestimmten Voraussetzungen (sorgfältige Suche, Registrierung beim EUIPO) nutzen.
- Für Verlage: Keine direkte Ausnahme; Verlage können verwaiste Werke nicht ohne weiteres nutzen.
- Empfehlung: Bei unbekanntem Rechteinhaber — Sorgfältige Suche dokumentieren, ggf. Treuhandkonto für Vergütung.

## Typische Fallen

- **Bildrechte für Print, nicht für E-Book**: Lizenz nur für Printausgabe → E-Book ist Verletzung.
- **Auftragsillustration ohne schriftliche Rechteeinräumung**: Mündliche Vereinbarung reicht nicht; UrhG § 31 verlangt keine Form, aber Beweis nötig.
- **Veraltete Bildlizenz**: Lizenz für 1. Auflage; 2. Auflage benötigt neue Lizenz (je nach Vertrag).
- **Personenfotos ohne Einwilligung**: DSGVO-Verstoß und KUG-Verletzung; insbesondere bei erkennbaren Personen in Reportage-Fotos.
- **„Creative Commons" falsch verstanden**: CC BY-SA zwingt zur ShareAlike-Lizenzierung des Gesamtwerks → nicht für kommerzielle Bücher geeignet.

## Checkliste Bildrechte

- [ ] Bildrechte-Protokoll für alle Abbildungen angelegt
- [ ] Nutzungsarten (Print, E-Book, Online, Werbung) vollständig lizenziert
- [ ] Personenfotos: Einwilligung der abgebildeten Personen (KUG, DSGVO) vorhanden
- [ ] Autorenvertrag enthält Bildrechts-Freistellungsklausel
- [ ] Creative-Commons-Abbildungen: Lizenztyp auf Kompatibilität geprüft
- [ ] Neue Auflage: Bildlizenzen verlängert / erneuert

## Quellenreferenzen

- UrhG §§ 2, 51, 72: https://dejure.org/gesetze/UrhG/2.html
- KUG § 22: https://dejure.org/gesetze/KunstUrhG/22.html
- EuGH C-161/17 (Preußischer Kulturbesitz / Kunstabbildungen): https://eur-lex.europa.eu
- BGH „Metall auf Metall" (Zitatrecht): https://www.bgh.de
- Getty Images Lizenzmodelle: https://www.gettyimages.de

## Output-Formate

- **Bildrechte-Protokoll**: Tabelle aller Abbildungen mit Rechtsstatus
- **Bildrechts-Lizenzvertrag-Muster**: Standardformular für Einzellizenzen
- **Risikoampel**: Fehlende oder abgelaufene Lizenzen
- **Freistellungsklausel** für Autorenvertrag
- **Verwaiste-Werke-Suchprotokoll**

## 2. `verl-019-ki-generierte-inhalte-im-verlag`

**Fokus:** Verlagsrecht: KI-generierte Texte, Bilder und Übersetzungen im Verlag — Urheberrechtsstatus, Kennzeichnungspflichten, Vertragsklauseln und Haftungsrisiken (EU AI Act, UrhG).

# Verl-019 · KI-generierte Inhalte im Verlag

## Zweck dieses Skills

KI-Werkzeuge (GPT-4, Claude, Midjourney, DeepL etc.) werden zunehmend in der Verlagsproduktion eingesetzt: für Textentwürfe, Bildgenerierung, Übersetzungen, Lektorat und Metadaten. Dieser Skill klärt den **Urheberrechtsstatus KI-generierter Inhalte**, die Kennzeichnungspflichten, die vertragsrechtlichen Anforderungen und die Haftungsrisiken nach aktuellem deutschem und EU-Recht.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 2 | Werkbegriff: Erfordert menschliche Schöpfung | https://dejure.org/gesetze/UrhG/2.html |
| UrhG § 7 | Urheber ist stets eine natürliche Person | https://dejure.org/gesetze/UrhG/7.html |
| EU AI Act Art. 50 | Transparenzpflichten für KI-generierte Inhalte | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689 |
| DSM-RL Art. 4 | Text- und Data-Mining (TDM) für Forschung | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |
| DSM-RL Art. 4 Abs. 3 | Opt-Out für Rechteinhaber (kein TDM an ihren Werken) | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |
| UrhG § 44b | Text- und Datamining (nationales Recht) | https://dejure.org/gesetze/UrhG/44b.html |

## Urheberrechtsstatus KI-generierter Inhalte

### Grundprinzip: Kein Urheberrecht ohne menschliche Schöpfung
- Deutsches Urheberrecht (§§ 2, 7 UrhG): Urheber ist ausschließlich eine **natürliche Person**.
- KI-generierter Text oder ein KI-generiertes Bild ohne menschliche Schöpfungshöhe ist **gemeinfrei** (kein Urheberrechtsschutz).
- Keine Schutzfähigkeit von reinen KI-Outputs, selbst wenn qualitativ hochwertig.

### Menschliche Bearbeitung kann Schutz begründen
- Wenn Mensch das KI-Ergebnis **schöpferisch bearbeitet, strukturiert, auswählt** → eigenes Urheberrecht an der Bearbeitungsleistung.
- Schwelle: Die schöpferische Eigenleistung des Menschen muss erkennbar und nicht trivial sein.
- Reine Prompt-Eingabe allein: Zu wenig; erhebliche redaktionelle Nachbearbeitung: ausreichend.

### Praktische Konsequenzen für Verlage
- Rein KI-generierter Text im Buch: Kein Urheberrechtsschutz → keine Nutzungsrechte des Verlags nötig; aber auch kein Schutz gegen Nachdruck durch Dritte.
- Menschlich nachbearbeiteter KI-Text: Urheberrecht beim bearbeitenden Autor; normaler Verlagsvertrag möglich.

## Kennzeichnungspflichten

### EU AI Act Art. 50 (ab 2025/2026)
- Betreiber von KI-Systemen, die Texte, Bilder oder audiovisuelle Inhalte erzeugen, müssen diese als **KI-generiert kennzeichnen**.
- Machine-readable Marking: KI-generierte Inhalte sollen mit maschinenlesbaren Markierungen versehen werden (Watermarking).
- Ausnahmen: Wenn Inhalte redaktionell bearbeitet wurden und die KI nur Hilfsmittel war (keine automatische Erzeugung).

### Verlagspraxis
- **Transparenzvermerk**: Bücher mit wesentlichem KI-Anteil sollten im Impressum einen Hinweis tragen: „Teile dieses Werks wurden mit KI-Unterstützung erstellt und redaktionell überarbeitet."
- **Keine gesetzliche Pflicht für Impressum** (noch) — aber Best Practice für Vertrauensschutz.
- Fotografien: Midjourney- oder DALL-E-Bilder ohne menschliche Nachbearbeitung → im Bildnachweis als KI-generiert kennzeichnen.

## Text- und Data-Mining (TDM)

### Trainingsdata-Problem
- Viele KI-Modelle wurden mit Texten aus dem Internet trainiert, die urheberrechtlich geschützt sind.
- Verlag als Rechteinhaber: Kann Opt-Out für TDM erklären (§ 44b Abs. 3 UrhG, DSM-RL Art. 4 Abs. 3).
- Opt-Out: Mittels maschinell lesbarer Erklärung auf der Website (z.B. robots.txt, AI-Crawler-Protokoll).

### Verlag als TDM-Betreiber
- Verlag möchte eigene Texte für KI-Training nutzen: Braucht Zustimmung der Urheber.
- KI-Training-Klausel im Autorenvertrag: Neu notwendig; viele Altverträge schweigen.

## Vertragsgestaltung

### Autorenvertrag: Neue Klauseln
1. **KI-Nutzungsklausel**: „Der Autor erklärt, dass er keine wesentlichen Teile des Manuskripts durch generative KI erzeugt hat, ohne diese zu kennzeichnen."
2. **TDM-Klausel**: „Der Autor stimmt zu / stimmt nicht zu, dass das Werk für das Training von KI-Systemen verwendet werden darf."
3. **KI-Bearbeitungs-Haftung**: „Der Autor sichert zu, dass KI-generierte Inhalte im Manuskript auf Plagiat, Faktentreue und Rechtskonformität geprüft wurden."

### Verlagsvertrag mit KI-Dienstleistern
- KI-Lektorate (Grammarly, DeepL Write): Datenschutz-Prüfung; Manuskript nicht ohne Datenschutzklausel hochladen.
- KI-Übersetzung (DeepL Pro): Nutzungsrechte an der maschinellen Übersetzung? → DeepL-AGB prüfen.

## Haftungsrisiken

### Halluzinationen und Faktenfehler
- KI-generierte Texte können falsche Fakten, Quellenangaben und Zitate enthalten.
- Verlag und Autor haften für Inhalte, die Dritte schädigen (§§ 823, 824 BGB, Presserecht).
- **Faktencheck-Pflicht**: Bei KI-unterstützten Werken erhöhte redaktionelle Sorgfalt.

### Plagiatrisiko
- KI kann Texte reproduzieren, die sie im Training gesehen hat → ungewolltes Plagiat.
- Verlag sollte KI-generierten Text durch Plagiatssoftware laufen lassen.

### Markenrechtsverletzung durch KI-Bilder
- Midjourney kann Bilder mit Ähnlichkeit zu bekannten Figuren / Markenprodukten erzeugen.
- Markenrechtsverletzung und ggf. UrhG-Verletzung möglich.

## Typische Fallen

- **KI-Bild ohne Kennzeichnung**: Covergestaltung mit KI-Bild; Leser beschwert sich über fehlende Transparenz; Abmahnpotenzial nach EU AI Act.
- **Autorenvertrag ohne KI-Klausel**: Autor liefert zu 80 % KI-Text; Verlag entdeckt dies erst im Lektorat; kein vertragliches Instrument.
- **TDM-Opt-Out vergessen**: Verlag hat keinen robots.txt für KI-Crawler → Texte werden für Training genutzt, ohne dass Verlag es merkt.
- **DeepL-Übersetzung als Übersetzerwerk deklariert**: KI-Übersetzung ohne menschliche Bearbeitung hat kein Urheberrecht; Übersetzer-Nennung ist irreführend.

## Checkliste KI im Verlag

- [ ] Autorenvertrag: KI-Erklärungsklausel und TDM-Opt-In/Out-Regelung
- [ ] Manuskript-Faktencheck bei KI-unterstützten Werken
- [ ] Plagiatsprüfung für KI-generierte Textanteile
- [ ] KI-Bilder im Bildnachweis als KI-generiert gekennzeichnet
- [ ] Website: robots.txt mit AI-Crawler-Opt-Out gepflegt
- [ ] Datenschutz bei KI-Dienstleistern: Manuskripte nur unter DSGVO-konformem Vertrag hochladen

## Quellenreferenzen

- EU AI Act: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689
- UrhG § 44b (TDM): https://dejure.org/gesetze/UrhG/44b.html
- DSM-RL Art. 4: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- BfJ, KI und Urheberrecht (Positionspapier 2023): https://www.bmj.de
- DeepL Pro Nutzungsbedingungen: https://www.deepl.com/de/pro-license

## Output-Formate

- **KI-Anteil-Protokoll**: Welche Teile des Werks KI-generiert / KI-unterstützt / menschlich verfasst
- **Vertragsklausel-Entwurf**: KI-Erklärung, TDM, Haftung
- **Kennzeichnungsvorschlag** für Impressum und Bildnachweis
- **TDM-Opt-Out-Erklärung** für Website (robots.txt-Snippet)
- **Risikoampel**: KI-Risiken für das konkrete Werk
