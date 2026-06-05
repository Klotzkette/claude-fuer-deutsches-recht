---
name: verl-manuskriptablieferung-honorar
description: "Verl 004 Manuskriptablieferung Abnahme Lektorat Und Verzug, Verl 005 Honorar Vorschuss Absatzhonorar Und Abrechnung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 004 Manuskriptablieferung Abnahme Lektorat Und Verzug, Verl 005 Honorar Vorschuss Absatzhonorar Und Abrechnung

## Arbeitsbereich

Dieser Skill bündelt **Verl 004 Manuskriptablieferung Abnahme Lektorat Und Verzug, Verl 005 Honorar Vorschuss Absatzhonorar Und Abrechnung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-004-manuskriptablieferung-abnahme-lektorat-und-verzug` | Verlagsrecht: Manuskriptablieferung, Lektorat, Abnahme und Verzug nach VerlG §§ 2–4, BGB §§ 280 und 286 — Pflichten, Fristen, Rechtsfolgen bei Verzug und Mängelrüge. |
| `verl-005-honorar-vorschuss-absatzhonorar-und-abrechnung` | Verlagsrecht: Autorenhonorar, Vorschuss, Absatzhonorar, Nachvergütung und Abrechnungspflicht nach VerlG §§ 22–28, UrhG §§ 32 und 32a, 32d — Berechnung, Angemessenheit und Auskunft. |

## Arbeitsweg

Für **Verl 004 Manuskriptablieferung Abnahme Lektorat Und Verzug, Verl 005 Honorar Vorschuss Absatzhonorar Und Abrechnung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-004-manuskriptablieferung-abnahme-lektorat-und-verzug`

**Fokus:** Verlagsrecht: Manuskriptablieferung, Lektorat, Abnahme und Verzug nach VerlG §§ 2–4, BGB §§ 280 und 286 — Pflichten, Fristen, Rechtsfolgen bei Verzug und Mängelrüge.

# Verl-004 · Manuskriptablieferung, Lektorat, Abnahme und Verzug

## Zweck dieses Skills

Dieser Skill behandelt den **Ablieferungsprozess** im Verlagsvertrag: Was der Autor abliefern muss (Form, Inhalt, Qualität), wie der Verlag die Abnahme oder Zurückweisung handhaben darf, welche Lektoratspflichten entstehen und wie Verzug und Mängel rechtlich abgewickelt werden. Grundlage ist VerlG §§ 1–8 zusammen mit den allgemeinen BGB-Regelungen zu Leistungsstörungen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| VerlG § 2 | Ablieferungspflicht des Autors: Form, Frist, Vollständigkeit | https://www.gesetze-im-internet.de/verlg/__2.html |
| VerlG § 3 | Mängel des abgelieferten Manuskripts | https://www.gesetze-im-internet.de/verlg/__3.html |
| VerlG § 4 | Änderungen am Manuskript durch den Verlag | https://www.gesetze-im-internet.de/verlg/__4.html |
| VerlG § 5 | Erscheinungspflicht des Verlags | https://www.gesetze-im-internet.de/verlg/__5.html |
| BGB § 280 | Schadensersatz wegen Pflichtverletzung | https://dejure.org/gesetze/BGB/280.html |
| BGB § 286 | Schuldnerverzug | https://dejure.org/gesetze/BGB/286.html |
| BGB § 633 | Mangelbegriff beim Werkvertrag (analog) | https://dejure.org/gesetze/BGB/633.html |

## Ablieferungspflicht des Autors (§ 2 VerlG)

### Was ist abzuliefern?
1. **Druckfertige Vorlage** — das Manuskript muss zur direkten Verwendung in der Produktion geeignet sein, sofern nicht anders vereinbart.
2. **Vereinbarte Form** — Dateiformat (z.B. DOCX, RTF), Zeichensatz, Bilddateien in Druckauflösung (i.d.R. 300 dpi).
3. **Vereinbarter Umfang** — Seiten-/Zeichenzahl; erhebliche Abweichungen berechtigen den Verlag zur Nachfrist oder Ablehnung.
4. **Vollständige Teile** — Text, Fußnoten, Bibliografie, Register, Widmung, Anhänge, Abbildungsvorlagen, Bildunterschriften.
5. **Rechtsklarheit** — Alle Nutzungsrechte an Drittmaterial (Bilder, Zitate > erlaubte Zitatlänge, Tabellen) müssen vom Autor eingeholt worden sein.

### Frist und Verzug (§§ 2 VerlG, 286 BGB)
- **Kalendarische Frist im Vertrag**: Autor gerät ohne Mahnung in Verzug (§ 286 Abs. 2 Nr. 1 BGB).
- **Keine Frist vereinbart**: Angemessene Frist; Verlag muss mahnen.
- **Rechtsfolgen des Autorenverzugs**:
 - Schadensersatzanspruch des Verlags (§ 280 BGB)
 - Fristsetzung mit Rücktrittsdrohung
 - Rücktritt nach fruchtlosem Ablauf (§ 7/8 VerlG i.V.m. §§ 346 ff. BGB)
 - Rückzahlung des Vorschusses (streitig, je nach Vertragsgestaltung)

## Lektorat und Manuskript-Mängel

### § 3 VerlG — Mängelrecht des Verlags
- Weist das abgelieferte Manuskript Mängel auf (unvollständig, fehlerhaft, nicht druckfertig), darf der Verlag:
 - Nacherfüllung verlangen (Nachlieferung des fehlenden Teils)
 - Nachbesserungsfrist setzen
 - Bei erheblichem Mangel: Rücktritt und Schadensersatz (§ 8 VerlG)
- **Kein stilistisches Änderungsrecht**: Der Verlag darf inhaltliche und sprachliche Entscheidungen des Autors nicht eigenmächtig ändern (§ 14 UrhG — Entstellungsverbot).

### § 4 VerlG — Änderungen durch den Verlag
- Änderungen nur mit Zustimmung des Autors, soweit nicht im Vertrag ausdrücklich anders vereinbart.
- Lektorate (Kommentare, Vorschläge) sind keine Änderungen; erst die tatsächliche Abänderung löst das Zustimmungserfordernis aus.
- **Rotes Exemplar / Track Changes**: Best Practice — jede Änderung dokumentieren und Zustimmung einholen.

### Abnahme
- VerlG kennt keine förmliche Abnahme wie das Werkvertragsrecht (§ 640 BGB).
- Verlag nimmt Manuskript durch Weiterleitung an Produktion konkludent an.
- **Rügepflicht**: Verlag sollte Mängel unverzüglich nach Erhalt rügen (analog § 377 HGB bei kaufmännischen Verlagsverträgen).

## Erscheinungspflicht des Verlags (§ 5 VerlG)

- Nach ordnungsgemäßer Ablieferung muss der Verlag das Werk **binnen angemessener Frist** erscheinen lassen.
- Angemessen: je nach Werktyp 6–18 Monate üblich; Fachbücher und Lehrbücher mit Saisonbindung kürzer.
- **Verzug des Verlags**:
 - Autor setzt Nachfrist (3–6 Monate; schriftlich).
 - Nach fruchtlosem Ablauf: Rücktritt nach § 7 VerlG; Rechte fallen zurück.
 - Schadensersatzanspruch bei Verschulden (§ 8 VerlG i.V.m. § 280 BGB).

## Druckfahnen und Korrektur

- Autor hat Anspruch auf Einsicht in Druckfahnen und Korrekturabzüge, sofern vereinbart.
- **Autorenkorrektur**: Inhaltliche Änderungen über das vereinbarte Maß hinaus → Verlag kann Mehrkosten in Rechnung stellen (Autorenkorrektur-Klausel im Vertrag prüfen).
- Kürzliche digitale Verlagsprozesse: PDF-Korrektur, CMS-basierte Redaktionssysteme — vertraglich regeln, wer Korrekturstand kontrolliert.

## Typische Fallen

- **Verzug trotz Krankheit oder Verhinderung**: § 275 BGB (Unmöglichkeit) greift nur bei echter dauerhafter Unmöglichkeit; Krankheit allein reicht nicht.
- **Autor liefert Teile vor, Rest fehlt**: Verlag darf nicht teilweise erscheinen; muss Gesamtablieferung abwarten, sofern das Werk unteilbar ist.
- **Lektoratsänderungen ohne Zustimmung**: Stellt Verletzung des § 14 UrhG dar; Autor kann Unterlassung fordern.
- **Verzug des Verlags ignoriert**: Autor versäumt Fristsetzung und damit das Rücktrittsrecht nach § 7 VerlG.
- **Mehrkosten-Klausel vergessen**: Ohne vertraglich geregelte Autorenkorrektur-Toleranz (üblich 10 % der Satzkosten) sind Mehrkosten nicht eindeutig zugeordnet.

## Checkliste Ablieferungsprozess

- [ ] Ablieferungsfrist im Vertrag kalendarisch bestimmt
- [ ] Formatvorgaben und Vollständigkeitsliste beigefügt
- [ ] Mängelrüge des Verlags: schriftlich, unverzüglich nach Eingang
- [ ] Lektorate: alle Änderungsvorschläge als Track Changes, keine vollendeten Tatsachen
- [ ] Druckfahnenrecht des Autors vertraglich geregelt
- [ ] Autorenkorrektur-Toleranz-Klausel vorhanden

## Quellenreferenzen

- VerlG §§ 2–5: https://www.gesetze-im-internet.de/verlg/
- BGB §§ 280, 286: https://dejure.org/gesetze/BGB/286.html
- UrhG § 14 (Entstellungsverbot): https://dejure.org/gesetze/UrhG/14.html
- BGH, Urt. v. 03.07.1997 – I ZR 52/95 (Autorenvertrag Verzug): https://www.bgh.de
- Schricker/Loewenheim, Urheberrecht, § 31 Rn. 12 ff. (Nutzungsrechte im Verlagsvertrag)

## Output-Formate

- **Verzugs-Checkliste**: Status Ablieferung, Mängelrüge, Nachfrist, Rücktritt
- **Mängelprofil**: Mängel klassifiziert nach Schwere und Behebbarkeit
- **Fristenplan**: Ablieferung, Lektorat, Korrekturfristen, Erscheinungstermin
- **Entwurf Mängelrüge** (Verlag an Autor)
- **Entwurf Nachfrist** (Autor an Verlag wegen Nichterscheinen)

## 2. `verl-005-honorar-vorschuss-absatzhonorar-und-abrechnung`

**Fokus:** Verlagsrecht: Autorenhonorar, Vorschuss, Absatzhonorar, Nachvergütung und Abrechnungspflicht nach VerlG §§ 22–28, UrhG §§ 32 und 32a, 32d — Berechnung, Angemessenheit und Auskunft.

# Verl-005 · Honorar, Vorschuss, Absatzhonorar und Abrechnung

## Zweck dieses Skills

Dieser Skill klärt alle vergütungsrechtlichen Fragen im Verlagsvertrag: Wie wird das Honorar berechnet? Was gilt als angemessene Vergütung? Wann ist ein Vorschuss fällig? Wie funktioniert die Absatzhonorar-Abrechnung? Wann entsteht ein Nachvergütungsanspruch (Bestseller-Paragraf)? Grundlage sind VerlG §§ 22–28 und UrhG §§ 32, 32a, 32d.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| VerlG § 22 | Honoraranspruch des Autors; Entstehung | https://www.gesetze-im-internet.de/verlg/__22.html |
| VerlG § 23 | Berechnung des Honorars nach Auflage | https://www.gesetze-im-internet.de/verlg/__23.html |
| VerlG § 24 | Abrechnung: Fristen und Form | https://www.gesetze-im-internet.de/verlg/__24.html |
| VerlG § 28 | Neue Auflagen: neuer Honoraranspruch | https://www.gesetze-im-internet.de/verlg/__28.html |
| UrhG § 32 | Angemessene Vergütung; Anpassungsanspruch | https://dejure.org/gesetze/UrhG/32.html |
| UrhG § 32a | Nachvergütung bei besonderem Erfolg | https://dejure.org/gesetze/UrhG/32a.html |
| UrhG § 32d | Auskunftsanspruch des Urhebers | https://dejure.org/gesetze/UrhG/32d.html |
| UrhG § 36 | Gemeinsame Vergütungsregeln | https://dejure.org/gesetze/UrhG/36.html |
| DSM-RL Art. 18 | Angemessenheitsprinzip für Urheber | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |
| DSM-RL Art. 20 | Vertragsanpassungsmechanismus | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Honorartypen im Überblick

### 1. Pauschalhonorar
- Einmalige Zahlung für alle Nutzungen oder eine bestimmte Auflage.
- Vorteil für Verlag: Planungssicherheit.
- Risiko für Autor: Kein Nachvergütungsanspruch, es sei denn, § 32a UrhG greift.

### 2. Absatzhonorar (Tantieme)
- Prozentualer Anteil am **Nettoladenpreis** (NLP) jedes verkauften Exemplars.
- Übliche Sätze nach gemeinsamen Vergütungsregeln (VS/Verleger):
 - Hardcover: 10–15 % NLP
 - Taschenbuch: 6–10 % NLP
 - E-Book: 20–25 % NLP (abhängig von Plattformgebühren)
- Berechnung: Menge × NLP × Prozentsatz = Honorar je Abrechnung.

### 3. Auflagenhonorar
- Pauschalzahlung pro Auflage oder pro 1.000 Exemplare (VerlG § 23).
- Neue Auflage → neuer Honoraranspruch (VerlG § 28).

### 4. Vorschuss (Advance)
- Zahlung bei Vertragsabschluss oder Manuskriptablieferung gegen zukünftige Honorare.
- Wird gegen zukünftige Tantiemen verrechnet (earn-out); nicht zurückzahlbar, sofern der Verlag das Werk erscheinen lässt (übliche Vertragsklausel).
- Rückzahlungspflicht: Nur bei Rücktritt wegen Autoren-Verschuldens; streitig bei Nichterscheinen des Verlags.

## Angemessene Vergütung (§ 32 UrhG)

### Prüfungsmaßstab
1. **Gemeinsame Vergütungsregeln** (§ 36 UrhG): Zwischen Berufsverbänden (VS — Verband der Schriftsteller, Verleger-Verbände) ausgehandelte Tarife gelten als Richtsatz.
2. **Branchenübliche Vergütung**: Wenn keine gemeinsamen Vergütungsregeln, dann Vergleich mit branchenüblicher Praxis.
3. **Anpassungsanspruch**: Ist vereinbarte Vergütung unangemessen niedrig → Autor kann Anpassung auf angemessene Vergütung verlangen (kein Rücktritt nötig).

### Berechnung der Unangemessenheit
- Verhältnis: vereinbarte Vergütung zu erzieltem Erlös des Verlags aus Werknutzung.
- BGH-Rechtsprechung: „Auffälliges Missverhältnis" bei Abweichung > 100 % gegenüber angemessenem Wert (BGH „Bestseller", I ZR 174/18).

## Nachvergütung (§ 32a UrhG — Bestseller-Paragraf)

### Voraussetzungen
- Vereinbarte Vergütung steht in **auffälligem Missverhältnis** zu tatsächlichen Erträgen.
- „Auffällig" = erhebliche Überschreitung der Erwartungen beim Vertragsabschluss.
- Erträge des Verlags aus Werknutzung (Tantiemen aus Lizenzen, Verlagserlös etc.) müssen bekannt oder ermittelbar sein.

### Geltendmachung
- Schriftliche Geltendmachung gegenüber Verlag.
- Ggf. vorherige Auskunft nach § 32d UrhG.
- Klage auf Abänderung des Vertrags auf angemessene Beteiligung.

## Auskunftsanspruch (§ 32d UrhG)

- Autor kann **jährlich** Auskunft verlangen: Art und Umfang der Nutzung, Erlöse, weitere Sublizenzen.
- Gilt auch für Urheber, die Rechte an Verleger weiterübertragen haben (Kette).
- **DSM-RL Art. 19**: Stärkung des Transparenzanspruchs auf EU-Ebene; Mitgliedstaaten müssen angemessene Auskunftsmechanismen bereitstellen.
- Klagerecht: Bei Verweigerung der Auskunft → Auskunftsklage; ggf. Stufenklage (Auskunft + Zahlung).

## Abrechnungspflicht (VerlG § 24)

- Verlag muss **mindestens einmal jährlich** abrechnen (VerlG § 24), bei Absatzhonorar detailliert nach Ausgaben, Mengen, Preisen.
- Abrechnung muss enthalen: Auflage, verkaufte Exemplare, Remittenden, Belegexemplare, Freiexemplare, Nettoladenpreis, Honorarsatz.
- **Einsichtsrecht**: Autor kann Belegeinsicht in Verlagsbücher verlangen (§ 24 VerlG analog § 810 BGB).
- Frist für Einwände: Üblich 3–6 Monate nach Zugang der Abrechnung; Einwände schriftlich.

## Typische Fallen

- **Pauschalhonorare unterschätzen den Werterfolg**: Autor erhält einmalig Pauschale; bei Bestseller-Erfolg greift § 32a UrhG.
- **Verjährung der Auskunftsansprüche**: §§ 195, 199 BGB; regelmäßige Verjährungsfrist 3 Jahre ab Jahresende; monatliche Abrechnung schafft keine rückwirkenden Ansprüche.
- **NLP vs. Bruttoladenpreis**: MwSt. ist kein Teil des NLP; viele Verträge rechnen unklar; Klarheit verlangen.
- **Remittenden abgezogen**: Verlag darf nur tatsächlich remittierte Exemplare abziehen; fiktive Remittenden-Rückstellungen sind unzulässig.
- **Sublizenzerlöse vergessen**: Übersetzungslizenzen, Film-Optionen, E-Book-Plattform-Tantiemen — alle müssen in § 32d-Auskunft erscheinen.

## Checkliste Honorarprüfung

- [ ] Honorartyp (Pauschale, Absatz, Auflage) klar vereinbart
- [ ] Berechnungsbasis (NLP, gebundener Ladenpreis) definiert
- [ ] Abrechnungsrhythmus (mindestens jährlich) vereinbart
- [ ] Vorschuss: earn-out-Mechanismus und Rückzahlungsklausel geprüft
- [ ] § 32a UrhG Nachvergütungsklausel oder Ausschlussklausel geprüft
- [ ] § 32d Auskunftsrecht explizit geregelt
- [ ] Sublizenz-Beteiligungsquote vereinbart

## Quellenreferenzen

- VerlG §§ 22–28: https://www.gesetze-im-internet.de/verlg/
- UrhG § 32: https://dejure.org/gesetze/UrhG/32.html
- UrhG § 32a: https://dejure.org/gesetze/UrhG/32a.html
- UrhG § 32d: https://dejure.org/gesetze/UrhG/32d.html
- BGH „Klauseltausch" I ZR 174/18: https://www.bgh.de
- DSM-RL Art. 18–20: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- Börsenverein Honorartarife: https://www.boersenverein.de

## Output-Formate

- **Honorarberechnungssheet**: Absatzhonorar nach Auflagen und Ausgaben
- **Angemessenheitsprüfung**: Vergleich mit gemeinsamen Vergütungsregeln
- **Auskunftsschreiben** nach § 32d UrhG
- **Nachvergütungsklage-Vorprüfung**: Missverhältnis-Berechnung
- **Abrechnungsrüge**: Formelles Einwandsschreiben gegen Verlagsabrechnung
