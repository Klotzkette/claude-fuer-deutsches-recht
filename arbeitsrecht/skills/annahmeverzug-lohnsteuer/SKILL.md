---
name: annahmeverzug-lohnsteuer
description: "Kueschk Annahmeverzug Lohnsteuer im Plugin Arbeitsrecht: prüft konkret Annahmeverzugslohn nach § 615 BGB und § 11 KSchG, Beurteilt den sozialversicherungsrechtlichen Status, § 7a, Arbeitgeber will Arbeitnehmer abmahnen oder Arbeitnehmer. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Kueschk Annahmeverzug Lohnsteuer

## Arbeitsbereich

**Kueschk Annahmeverzug Lohnsteuer** ordnet den Fall über die tragenden Prüfungslinien: Annahmeverzugslohn nach § 615 BGB und § 11 KSchG, Beurteilt den sozialversicherungsrechtlichen Status, § 7a. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `kueschk-annahmeverzug-loehne-anrechnung-zwischenverdienst` | Annahmeverzugslohn nach § 615 BGB und § 11 KSchG; Anrechnung anderweitigen Verdienstes; boeswiches Unterlassen; Berechnung Nettolohnvorteil; Schadensminderungspflicht; Auswirkung auf Vergleichsdruck; steuerliche Behandlung. |
| `lohnsteuer-sozialversicherung` | Beurteilt den sozialversicherungsrechtlichen Status (Scheinselbständigkeit, § 7a SGB IV) und lohnsteuerliche Fragen im Arbeitsverhältnis. Lädt, wenn ein Statusfeststellungsverfahren, Scheinselbständigkeit, Nachzahlungspflichten (§ 28e SGB IV), strafrechtliche Risiken (§ 266a StGB) oder die Abgrenzung Arbeitnehmer/Selbständiger zu prüfen ist. |
| `abmahnung-arbeitsrecht` | Arbeitgeber will Arbeitnehmer abmahnen oder Arbeitnehmer hat Abmahnung erhalten und will sie anfechten. Prüfraster Warnfunktion Ruegefunktion Dokumentationsfunktion nach BAG-Rspr. § 314 Abs. 2 BGB § 241 Abs. 2 BGB. Inhaltliche Anforderungen Bestimmtheit Konkretheit des Vorwurfs Verhältnismäßigkeit. Prüfung ob Abmahnung entbehrlich (verhaltensbedingte Kündigung). Output Abmahnungsschreiben oder Gegendarstellung Widerspruchsschreiben Löschungsantrag. Abgrenzung: Kündigungsprüfung bei kueschk-skills; BR-Anhörung bei betriebsrat-anhoerung. |
| `agg-pruefung-bewerber-und-beschaeftigte` | AGG-Prüfung bei Bewerbung und Beschäftigung: Diskriminierungsmerkmale § 1 AGG, Benachteiligungsverbot § 7 AGG, Entschädigungs- und Schadensersatzansprüche § 15 AGG, Beweislastumkehr § 22 AGG, Geltendmachungsfrist § 15 Abs. 4 AGG (zwei Monate). Stellenausschreibung, Auswahlverfahren, Beschäftigungsbedingungen, Beförderung, Entlohnung, Kündigung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `kueschk-annahmeverzug-loehne-anrechnung-zwischenverdienst`

**Fokus:** Annahmeverzugslohn nach § 615 BGB und § 11 KSchG; Anrechnung anderweitigen Verdienstes; boeswiches Unterlassen; Berechnung Nettolohnvorteil; Schadensminderungspflicht; Auswirkung auf Vergleichsdruck; steuerliche Behandlung.

### Annahmeverzugslöhne und Zwischenverdienst

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Annahmeverzugslöhne und Zwischenverdienst` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor der Berechnung

1. Wann wurde das Arbeitsverhältnis durch den Arbeitgeber beendet? (Beginn des Annahmeverzugs)
2. Hat der Arbeitnehmer ein neues Arbeitsverhältnis begründet? (Anrechnung § 11 KSchG)
3. Falls ja: Wie hoch ist der neue Verdienst im Vergleich zum alten?
4. Hat die Agentur für Arbeit ALG I gezahlt? (Forderungsübergang § 115 SGB X beachten)
5. Bis zu welchem Datum wird Annahmeverzug geltend gemacht? (Rechtskraft / Vergleich)

## Zentrale Normen

- § 615 BGB — Annahmeverzugslohn (Vergütung ohne Arbeit)
- § 11 KSchG — Anrechnung anderweitigen Verdienstes (analog zu § 615 Satz 2 BGB)
- § 11 Nr. 2 KSchG — böswilliges Unterlassen zumutbarer Arbeit (Anrechnung fiktiven Verdienstes)
- § 11 Nr. 3 KSchG — kein Übergang von ALG-I-Zahlungen (§ 115 SGB X)
- § 615 Satz 2 BGB — anderweitiger Erwerb: Arbeitnehmer muss sich anrechnen lassen
- § 297 BGB — Annahmeverzug entfällt wenn Arbeitnehmer nicht leistungsfähig/-willig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Annahmeverzug § 615 BGB

**Voraussetzungen:**
1. Arbeitgeber gerät in Annahmeverzug durch Ausspruch der Kündigung
2. Arbeitnehmer war leistungswillig und leistungsfähig (§ 297 BGB)
3. Bei Kündigung: Arbeitsangebot gilt als entbehrlich (kein wörtliches Angebot nötig)

**Rechtsfolge:** Arbeitgeber schuldet das vereinbarte Arbeitsentgelt einschließlich aller Zulagen, Boni und Sonderzahlungen, ohne dass der Arbeitnehmer Arbeit nachleisten muss.

## Anrechnung anderweitigen Verdienstes § 11 KSchG

Nach § 11 Nr. 1 KSchG muss sich der Arbeitnehmer auf den Annahmeverzugslohn anrechnen lassen:
- Bruttoverdienst aus neuem Arbeitsverhältnis
- Selbständige Tätigkeit / freiberufliche Einnahmen

**Nicht angerechnet:**
- Arbeitslosengeld I (§ 11 Nr. 3 KSchG — Forderungsübergang auf Agentur für Arbeit nach § 115 SGB X)
- Eigenleistungen (Hausarbeit, Urlaub)
- Vermögenserträge

### Böswilliges Unterlassen § 11 Nr. 2 KSchG

Arbeitnehmer muss sich auch dasjenige anrechnen lassen, was er **böswillig** nicht verdient hat.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Berechnung (Beispiel)

```
Vereinbartes Monatsgehalt: 4000 Euro brutto
Annahmeverzugszeitraum: 8 Monate
Zwischenverdienst: 2500 Euro brutto/Monat

Berechnung:
 Gesamt-Annahmeverzugslohn: 4000 × 8 = 32000 Euro brutto
 Anzurechnender Zwischenverdienst: 2500 × 8 = 20000 Euro
 Netto-Forderung: 32000 - 20000 = 12000 Euro brutto
```

## Strategische Bedeutung für den Vergleich

- Annahmeverzugslöhne wachsen mit Dauer des Prozesses — **erhöhen Vergleichsdruck auf den Arbeitgeber**
- Im Vergleich wird oft ein Pauschalabfindungsbetrag vereinbart, der Annahmeverzugsansprüche mit abgilt
- Steuerfrage: Annahmeverzugslöhne sind lohnsteuerpflichtig; keine Fünftel-Regelung (§ 34 EStG)
- Annahmeverzug-Risiko bei langen Prozessen: Arbeitgeber hat Anreiz für frühen Vergleich

## Output-Template — Annahmeverzugsberechnung

```
ANNAHMEVERZUGSBERECHNUNG (Schätzung)
Mandant: [NAME]
Beendigungsdatum (laut AG): [DATUM]
Vereinbartes Bruttomonatsgehalt: [BETRAG] Euro
(inkl. regelmäßiger Sonderzahlungen: [BETRAG] Euro)

Annahmeverzugszeitraum: [DATUM] bis [DATUM] = [MONATE] Monate
Gesamt-Annahmeverzugslohn: [MONATE] × [BETRAG] = [ERGEBNIS] Euro brutto

Abzüge § 11 KSchG:
 Zwischenverdienst: [BETRAG] Euro (Monate × neues Gehalt)
 Böswilliges Unterlassen: [ggf. — Begründung]
 ALG I: NICHT anzurechnen (§ 11 Nr. 3 KSchG)

Netto-Annahmeverzugsforderung: [ERGEBNIS] Euro brutto

Hinweis: Annahmeverzugslöhne sind lohnsteuerpflichtig (keine Fünftel-Regelung).
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 2. `lohnsteuer-sozialversicherung`

**Fokus:** Beurteilt den sozialversicherungsrechtlichen Status (Scheinselbständigkeit, § 7a SGB IV) und lohnsteuerliche Fragen im Arbeitsverhältnis. Lädt, wenn ein Statusfeststellungsverfahren, Scheinselbständigkeit, Nachzahlungspflichten (§ 28e SGB IV), strafrechtliche Risiken (§ 266a StGB) oder die Abgrenzung Arbeitnehmer/Selbständiger zu prüfen ist.

### Lohnsteuer und Sozialversicherung – Statusfeststellung und Scheinselbständigkeit

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lohnsteuer und Sozialversicherung – Statusfeststellung und Scheinselbständigkeit` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill dient der Beurteilung des sozialversicherungsrechtlichen Beschäftigtenstatus sowie damit zusammenhängender lohnsteuerlicher Fragen. Er ist einschlägig, wenn die Abgrenzung zwischen abhängiger Beschäftigung (§ 7 Abs. 1 SGB IV) und selbständiger Tätigkeit rechtlich zu klären ist, ein Statusfeststellungsverfahren nach § 7a SGB IV eingeleitet werden soll oder bereits von der Deutschen Rentenversicherung Bund (DRV) durchgeführt wird, ein Verdacht auf Scheinselbständigkeit besteht (mit Nachzahlungsrisiken nach § 28e SGB IV, § 28p SGB IV) oder strafrechtliche Risiken nach § 266a StGB zu bewerten sind. Der Skill berücksichtigt die BSG-Rechtsprechung zu den Abgrenzungskriterien sowie die steuerrechtliche Einordnung (Lohnsteuer vs. Einkommensteuer / Umsatzsteuer).

## Eingaben

1. **Vertragsgestaltung**: Freier-Mitarbeiter-Vertrag, Dienstvertrag, Werkvertrag – Vertragsurkunde
2. **Tatsächliche Durchführung**: Wie ist die Zusammenarbeit in der Praxis ausgestaltet? (Weisungen, Arbeitszeit, Ort, Eingliederung)
3. **Auftraggeberstruktur**: Wie viele Auftraggeber hat der "Selbständige"? Umsatzverteilung?
4. **Unternehmerisches Risiko**: Eigene Betriebsmittel, eigene Arbeitnehmer, Haftungsrisiko des Auftragnehmers?
5. **Bisherige steuerliche und SV-Behandlung**: Wie wurden Beiträge bisher abgeführt?
6. **Zeitraum**: Seit wann besteht die Zusammenarbeit? (Nachzahlungszeitraum!)
7. **Vorliegen eines DRV-Bescheids**: Statusfeststellungsbescheid vorhanden?
8. **Widerspruch / Klage**: Rechtsmittel eingelegt?
9. **Steuerrechtliche Einordnung**: Gewerbe- oder Freiberufler-Einordnung nach EStG, Umsatzsteuer-Behandlung

## Rechtlicher Rahmen

### Kernvorschriften

- § 7 Abs. 1 SGB IV: Definition der Beschäftigung (nicht selbständige Arbeit; Merkmale: Weisungsgebundenheit, Eingliederung in fremde Organisation)
- § 7a SGB IV: Statusfeststellungsverfahren bei der DRV Bund; Antrag möglich, aber kein Muss; Bescheid mit aufschiebender Wirkung in laufenden Beschäftigungen (§ 7a Abs. 6 SGB IV)
- § 28e SGB IV: Haftung des Arbeitgebers für Gesamtsozialversicherungsbeitrag (Arbeitgeber- und Arbeitnehmeranteil; bei Scheinselbständigkeit: Arbeitgeber trägt Nachzahlung alleine, kein Rückgriff auf Arbeitnehmer für > 3 Monate zurückliegende Zeiträume)
- § 28p SGB IV: Prüfbefugnis der Rentenversicherungsträger bei Arbeitgebern (Betriebsprüfung)
- § 266a StGB: Vorenthalten und Veruntreuen von Arbeitsentgelt (bei vorsätzlichem Nichtabführen von SV-Beiträgen; Strafbarkeit des Arbeitgebers)
- § 19 Abs. 1 EStG: Einkünfte aus nichtselbständiger Arbeit → Lohnsteuerpflicht
- § 15, § 18 EStG: Gewerbliche bzw. freiberufliche Einkünfte bei Selbständigen
- § 41a EStG: Lohnsteuer-Anmeldungspflicht des Arbeitgebers
- §§ 1, 3 LStDV: Arbeitnehmer-Begriff im Lohnsteuerrecht (enger gefasst als SV-Recht, aber in der Praxis weitgehend parallel)

### Leitentscheidungen (BGH-Stil)

- **Abgrenzungskriterien abhängige Beschäftigung / Selbständigkeit:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Einzelfallabwägung / unternehmerisches Risiko:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Rückwirkung des Statusfeststellungsbescheids:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **§ 266a StGB / Vorsatz:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 – Abgrenzungsprüfung: Abhängige Beschäftigung oder Selbständigkeit?

**Prüfschema (Gesamtbildbetrachtung nach § 7 Abs. 1 SGB IV):**

| Kriterium | Für abhängige Beschäftigung | Für Selbständigkeit |
|---|---|---|
| Weisungsgebundenheit | Weisungen zu Zeit, Ort, Art der Tätigkeit | Freie Zeiteinteilung, eigene Methodenfreiheit |
| Eingliederung | In Betriebsorganisation eingebunden; Dienstplan, Arbeitskleidung, IT des AG | Eigene Betriebsstruktur, eigene IT |
| Eigene Betriebsmittel | Fehlen wesentlicher eigener Betriebsmittel | Erhebliche eigene Investitionen |
| Unternehmerisches Risiko | Monatlich fixer Vergütungsanspruch | Variables Entgelt, Verlustrisiko |
| Mehrere Auftraggeber | Nur ein Auftraggeber (Indiz für Scheinselbständigkeit) | Viele Auftraggeber |
| Eigene Arbeitnehmer | Keine eigenen AN | Beschäftigt eigene AN |
| Auftreten am Markt | Kein Auftritt als Unternehmer | Eigene Werbung, Kunden etc. |

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Vertragswortlaut ist nicht maßgeblich**, wenn tatsächliche Durchführung abweicht.

### Schritt 2 – Statusfeststellungsverfahren (§ 7a SGB IV)

- **Antragsberechtigt**: Auftraggeber oder Auftragnehmer, ggf. Einzugsstelle.
- **Zuständig**: Deutsche Rentenversicherung Bund (DRV Bund), Clearingstelle.
- **Verfahrensablauf**: Antragstellung → Anhörung beider Parteien → Bescheid; aufschiebende Wirkung für laufende Aufträge bis Entscheidung (§ 7a Abs. 6 SGB IV, kein Beitragsrisiko für Übergangszeit, wenn Antrag rechtzeitig gestellt).
- **Bindungswirkung**: Bescheid bindet alle Sozialversicherungsträger; Widerspruch und Klage zum Sozialgericht (§§ 84, 87 SGG) möglich.
- **Strategische Empfehlung**: Proaktive Antragstellung bei Zweifeln minimiert Nachzahlungsrisiko und strafrechtliche Exposition.

### Schritt 3 – Folgen bei Feststellung als abhängige Beschäftigung

**Sozialversicherung:**
- Nachzahlungspflicht für Gesamtsozialversicherungsbeitrag (Arbeitgeber- + Arbeitnehmeranteil) nach § 28e SGB IV; **Verjährung: 4 Jahre** (§ 25 Abs. 1 SGB IV), bei Vorsatz 30 Jahre.
- Kein Rückgriff des Arbeitgebers auf den Arbeitnehmer für mehr als **3 Monate** rückwirkend (§ 28g Satz 3 SGB IV).
- Säumniszuschläge § 24 SGB IV (1 % pro angefangenem Kalendermonat).

**Lohnsteuer:**
- Pflicht zur Lohnsteuer-Anmeldung (§ 41a EStG); Nachzahlung mit Haftung des Arbeitgebers (§ 42d EStG).
- Bereits gezahlte Einkommensteuer des Auftragnehmers wird angerechnet.

**Strafrechtlich:**
- § 266a StGB: Strafbarkeit des Arbeitgebers (Geschäftsführer, Vorstand) bei vorsätzlichem Vorenthalten von Beiträgen; Freiheitsstrafe bis zu 5 Jahren oder Geldstrafe.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Selbstanzeige / Nachentrichten: Bei § 266a StGB existiert – anders als bei § 371 AO – keine strafbefreiende Selbstanzeige; freiwillige Nachzahlung ist aber strafmildernd.

### Schritt 4 – Gestaltungsoptionen und Risikominimierung

1. **Vertragsgestaltung anpassen**: Weisungsrechte vertraglich und praktisch reduzieren, mehrere Auftraggeber fördern.
2. **Statusfeststellungsverfahren proaktiv stellen** → schützt vor rückwirkenden Forderungen für Zeitraum ab Antragstellung.
3. **Umwandlung in Arbeitsverhältnis**: Wenn Scheinselbständigkeit nahe liegt, geordnete Überführung in abhängige Beschäftigung mit klaren Verträgen.
4. **Betriebsprüfung (§ 28p SGB IV)**: Auf kommende Prüfungen durch DRV vorbereiten; Dokumentation der tatsächlichen Verhältnisse.
5. **Steuerberatung**: Lohnsteuerliche Folgen (§§ 41a, 42d EStG) mit Steuerberater abstimmen.

### Schritt 5 – Besonderheiten Freiberufler

- Freiberufler nach § 18 EStG unterliegen keiner Gewerbesteuer, jedoch ggf. der SV-Pflicht als Beschäftigte, wenn Eingliederung vorliegt.
- Künstlerische und publizistische Tätigkeiten → Künstlersozialversicherung (KSVG) prüfen: Abgabepflicht des Auftraggebers (§§ 24, 25 KSVG).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

- **Standardausgabe**: Rechtliches Memo (Gutachtenstil) mit tabellarischer Kriterienprüfung und Risikoabschätzung.
- **Auf Anforderung**: Antrag auf Statusfeststellung nach § 7a SGB IV (Entwurf).
- **Auf Anforderung**: Checkliste Kriterien Scheinselbständigkeit als Tabelle.
- **Auf Anforderung**: Strafbarkeitsrisiko § 266a StGB als separate Bewertung.

## Beispiel

**Sachverhalt:** Unternehmen U-GmbH beschäftigt seit 3 Jahren Herr F als "freien IT-Berater" auf Honorarbasis (Monatshonorar 7.500 €). F arbeitet ausschließlich für U-GmbH, nutzt U-GmbHs IT-Infrastruktur, ist in den Projektmanagementprozess eingebunden und erhält Weisungen vom Projektleiter der U-GmbH. Ein eigenes Büro oder eigene Arbeitnehmer hat F nicht.

**Ergebnis:** Erhebliche Indizien sprechen für abhängige Beschäftigung, Scheinselbständigkeit liegt nahe.

**Bewertung:**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Eingliederung:* F ist in die Organisation der U-GmbH eingebunden (Projektmanagement, fremde IT).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

*Empfehlung:* Statusfeststellungsverfahren nach § 7a SGB IV sofort prüfen; SV-Beitragsrisiko nach § 25 SGB IV sauber zeitlich aufbauen (regelmäßige Verjährung vier Jahre, bei vorsätzlich vorenthaltenen Beiträgen dreißig Jahre), Säumniszuschläge und strafrechtliches Risiko § 266a StGB getrennt dokumentieren. Keine Kommentarstelle aus Modellwissen zitieren; für Rechtsprechung `rechtsstand-mai-2026-faktenbank` laden.

## Risiken und typische Fehler

| Fehler | Konsequenz | Abhilfe |
|---|---|---|
| Kein Statusfeststellungsverfahren trotz Zweifeln | Rückwirkende Nachzahlung; § 266a StGB | Proaktiv § 7a SGB IV beantragen |
| Vertrag "Freier Mitarbeiter" ohne tatsächliche Umsetzung | Scheinselbständigkeit; Nachzahlungspflicht § 28e SGB IV | Vertragsgestaltung und tatsächliche Durchführung abstimmen |
| Vorsätzliches Nichtabführen | § 266a StGB, Freiheitsstrafe bis 5 Jahre | Sofortige Klärung und Nachentrichten |
| Vergessen: KSVG-Abgabepflicht | Nachzahlung KSVG-Abgabe | Künstler/Publizisten gesondert prüfen |
| Falsche Steuererklärung des Auftragnehmers | § 370 AO; Nachzahlung; Berichtigungspflicht | Steuerberater einschalten |
| Keine Dokumentation der tatsächlichen Verhältnisse | Beweisproblem bei Betriebsprüfung | Tatsächliche Leistungserbringung laufend dokumentieren |
| § 203 StGB / Datenschutz | Strafbarkeit bei unbefugter Datenweitergabe | Personalstammdaten nur in zulässigen Systemen |
| Rückgriff auf Arbeitnehmer > 3 Monate | § 28g Satz 3 SGB IV schließt das aus | Nur bis 3 Monate rückwirkender Rückgriff zulässig |

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Quellenpflicht

Jede juristische Aussage in jedem auf diesem Skill basierenden Dokument ist nach **references/zitierweise.md** zu belegen:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Steuerrechtliche Aussagen mit BFH-Nachweis (BStBl.-Fundstelle).
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bei umstrittenen Fragen (z. B. Abgrenzung tatsächliche vs. vertragliche Verhältnisse) h. M. und Gegenauffassung getrennt nennen.
- Halluzinationsrisiko: Alle Aktenzeichen und Fundstellen vor Einreichung bei DRV, Sozialgericht oder Finanzgericht verifizieren.

## 3. `abmahnung-arbeitsrecht`

**Fokus:** Arbeitgeber will Arbeitnehmer abmahnen oder Arbeitnehmer hat Abmahnung erhalten und will sie anfechten. Prüfraster Warnfunktion Ruegefunktion Dokumentationsfunktion nach BAG-Rspr. § 314 Abs. 2 BGB § 241 Abs. 2 BGB. Inhaltliche Anforderungen Bestimmtheit Konkretheit des Vorwurfs Verhältnismäßigkeit. Prüfung ob Abmahnung entbehrlich (verhaltensbedingte Kündigung). Output Abmahnungsschreiben oder Gegendarstellung Widerspruchsschreiben Löschungsantrag. Abgrenzung: Kündigungsprüfung bei kueschk-skills; BR-Anhörung bei betriebsrat-anhoerung.

### Abmahnung im Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Abmahnung im Arbeitsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill dient dem Entwurf und der rechtlichen Bewertung von Abmahnungen im Arbeitsverhältnis. Er ist einschlägig, wenn ein Arbeitgeber eine Abmahnung aussprechen will (Wirksamkeitsvoraussetzungen, Formulierung), ein Arbeitnehmer eine erhaltene Abmahnung anfechten oder deren Entfernung aus der Personalakte begehrt, oder wenn eine verhaltensbedingte Kündigung vorbereitet wird und die Frage der vorherigen Abmahnung zu klären ist. Die Abmahnung ist regelmäßig notwendige Vorstufe einer verhaltensbedingten ordentlichen oder außerordentlichen Kündigung (§§ 1 KSchG, 626 BGB) und deshalb in ihrer formellen wie inhaltlichen Anforderung sorgfältig zu behandeln.

## Eingaben

1. **Sachverhalt**: Beschreibung des beanstandeten Verhaltens (Datum, Ort, konkrete Handlung/Unterlassung)
2. **Arbeitsvertrag** oder einschlägige Dienstanweisung (Pflichtenregelung)
3. **Perspektive**: Arbeitgeber (Abmahnung aussprechen) oder Arbeitnehmer (Gegenwehr, Entfernung)
4. **Vorherige Abmahnungen**: Datum, Inhalt, Reaktion des Arbeitnehmers
5. **Folgeziel**: Kündigung vorbereiten, Verhaltensänderung herbeiführen, reine Dokumentation
6. **Betriebsrat vorhanden?** (Beteiligungsrechte bei Personalaktenmaßnahmen, § 83 BetrVG)
7. **Personalakte**: Bisherige Einträge, Gegendarstellungen

## Rechtlicher Rahmen

### Kernvorschriften

- § 241 Abs. 2 BGB: Nebenpflichten des Arbeitsverhältnisses (Treuepflicht des Arbeitnehmers)
- § 314 Abs. 2 BGB: Abmahnung als Voraussetzung der außerordentlichen Kündigung aus Dauerschuldverhältnis (analog / direkt)
- § 1 Abs. 2 KSchG: Verhältnismäßigkeit der Kündigung; verhaltensbedingte Kündigung setzt i. d. R. vorherige Abmahnung voraus
- § 626 Abs. 1 BGB: Außerordentliche Kündigung; Abmahnung i. d. R. erforderlich, außer bei Vertrauensbruch oder bewusster/beharrlicher Pflichtverletzung
- § 83 BetrVG: Einsichtsrecht des Arbeitnehmers in die Personalakte
- § 84 BetrVG: Recht zur Gegendarstellung
- §§ 43a Abs. 2 BRAO, 203 StGB: Verschwiegenheitspflichten bei der Verarbeitung der Abmahnung

### Leitentscheidungen (BGH-Stil)

- **Warnfunktion / Bestimmtheit:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Entbehrlichkeit der Abmahnung:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Abmahnung als Kündigung vorbereitende Maßnahme:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Entfernung aus Personalakte:**
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 – Prüfung: Ist eine Abmahnung erforderlich / sinnvoll?

1. Liegt eine **arbeitsvertragliche Pflichtverletzung** vor (Hauptleistungspflicht, Nebenpflicht nach § 241 Abs. 2 BGB)?
2. Ist die Pflichtverletzung **schuldhaft** (Verschulden des Arbeitnehmers)?
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - Beharrliche oder wiederholte Pflichtverletzung trotz vorangegangener Abmahnungen?
 - Schwerwiegender Vertrauensbruch (z. B. Betrug, Diebstahl zu Lasten des Arbeitgebers)?
 - Dann: direkte Kündigung ggf. möglich.
4. **Folgeziel**: Verhaltensänderung herbeiführen → Abmahnung aussprechen. Nur Dokumentation ohne Kündigung → Abmahnung möglich, aber sachlich beschränkt.

### Schritt 2 – Wirksamkeitsvoraussetzungen prüfen (Checkliste)

| Anforderung | Erläuterung |
|---|---|
| Konkrete Bezeichnung des Verhaltens | Datum, Uhrzeit, Ort, Handlung/Unterlassung – keine Pauschalvorwürfe |
| Benennung der verletzten Pflicht | Vertragspflicht, Dienstanweisung, Betriebsvereinbarung |
| Rügefunktion | Klarstellen, dass das Verhalten als Pflichtverletzung bewertet wird |
| Warnfunktion | Androhung arbeitsrechtlicher Konsequenzen (i. d. R. Kündigung) |
| Aufforderung zur Verhaltensänderung | Konkrete Anforderung an künftiges Verhalten |
| Schriftform empfohlen | Keine Pflicht, aber Beweissicherung (§ 126 BGB analog); mündlich möglich, jedoch riskant |
| Zugang | Nachweis des Zugangs beim Arbeitnehmer sicherstellen |
| Zeitnah zum Vorfall | Längere Zeitspanne kann Wirkung entwerten (keine Ausschlussfrist, aber Verhältnismäßigkeit) |

### Schritt 3 – Formulierung des Abmahnungsschreibens

**Aufbau (Muster-Gliederung):**
```
[Betrieb / Arbeitgeber-Briefkopf]
[Datum]

Abmahnung

Sehr geehrte/r Herr/Frau [Name],

wir rügen folgendes Verhalten:

Am [Datum] um [Uhrzeit] haben Sie [konkrete Handlung/Unterlassung] entgegen
Ihrer arbeitsvertraglichen Pflicht aus [§ X Arbeitsvertrag / Dienstanweisung
vom ...]. [Ggf.: Dies ist nicht der erste Vorfall dieser Art, vgl. Abmahnung
vom ...]

Wir fordern Sie auf, dieses Verhalten künftig zu unterlassen / die Pflichten
gemäß [Regelung] zu erfüllen.

Wir weisen Sie ausdrücklich darauf hin, dass wir im Wiederholungsfall
arbeitsrechtliche Konsequenzen bis hin zur Kündigung des Arbeitsverhältnisses
in Betracht ziehen werden.

[Unterschrift des Arbeitgebers / bevollmächtigte Person]
```

### Schritt 4 – Zugang und Dokumentation

- Übergabe gegen **Empfangsbestätigung** oder per Einschreiben mit Rückschein.
- Zeugenübergabe als Alternative (zwei Zeugen notieren Datum, Inhalt, Übergabeperson).
- Kopie zur **Personalakte** (§ 83 BetrVG: Einsichtsrecht des Arbeitnehmers).
- Hinweis: Arbeitnehmer kann **Gegendarstellung** verlangen (§ 84 BetrVG); diese ist gleichfalls zur Akte zu nehmen, ohne inhaltliche Anerkennung.

### Schritt 5 – Arbeitnehmerperspektive: Gegenwehr und Entfernung

- **Inhaltliche Prüfung**: Ist der Sachverhalt zutreffend? Liegt tatsächlich eine Pflichtverletzung vor?
- **Verfahrensfehler**: Wurde der Betriebsrat beteiligt (soweit erforderlich)? Zugang nachweisbar?
- **Anspruch auf Entfernung** (§ 242 BGB): bei sachlich unrichtiger oder inhaltlich unzumutbarer Abmahnung; Klage zum Arbeitsgericht (§ 46 ArbGG).
- **Gegendarstellung** gemäß § 84 BetrVG sofort verfassen und übergeben.
- **Verjährung**: Anspruch auf Entfernung verjährt nach § 195 BGB (3 Jahre); Entfernung kann auch im laufenden Kündigungsschutzprozess geltend gemacht werden.

### Schritt 6 – Verhältnis zur Kündigung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Mehrere Abmahnungen wegen gleichartiger Verstöße erhöhen die Kündbarkeit der Pflichtverletzung.

## Ausgabeformat

- **Standardausgabe**: Memo im Gutachtenstil mit Wirksamkeitsprüfung (Aufbau vgl. references/methodik-buergerliches-recht.md Ziff. 6).
- **Auf Anforderung**: Vollständiges Abmahnungsschreiben (Urteilsstil, direkte Formulierung).
- **Auf Anforderung**: Widerspruchsschreiben / Gegendarstellung (Arbeitnehmerperspektive).
- **Auf Anforderung**: Checkliste Wirksamkeitsvoraussetzungen als Tabelle.

## Beispiel

**Sachverhalt:** Arbeitnehmer B erscheint am 03.03.2025 trotz vorangehender Ermahnung erneut 45 Minuten verspätet zur Arbeit, ohne vorherige Abmeldung. Sein Arbeitsvertrag verpflichtet ihn zur pünktlichen Aufnahme der Arbeit um 08:00 Uhr.

**Abmahnungsentwurf (Auszug):**

> "Wir rügen folgendes Verhalten: Am 03.03.2025 haben Sie Ihre Arbeitsleistung nicht wie vertraglich geschuldet um 08:00 Uhr, sondern erst um 08:45 Uhr aufgenommen, ohne uns vorher über die Verspätung zu informieren. Sie haben dadurch gegen Ihre arbeitsvertragliche Pflicht zur pünktlichen Erbringung der Arbeitsleistung verstoßen. Wir fordern Sie auf, Ihre Arbeit künftig pünktlich um 08:00 Uhr aufzunehmen und uns bei absehbaren Verspätungen rechtzeitig zu informieren. Wir weisen Sie ausdrücklich darauf hin, dass wir im Wiederholungsfall arbeitsrechtliche Konsequenzen bis hin zur Kündigung des Arbeitsverhältnisses in Betracht ziehen werden."

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken und typische Fehler

| Fehler | Konsequenz | Abhilfe |
|---|---|---|
| Pauschale Vorwürfe ohne konkrete Sachverhaltsangaben | Abmahnung unwirksam, kein Kündigungsgrund | Datum, Ort, Handlung exakt benennen |
| Fehlende Kündigungswarnung | Warnfunktion nicht erfüllt; Kündigung ohne vorherige Abmahnung angreifbar | Warnhinweis stets aufnehmen |
| Kein Zugangsnachweis | Beweisproblem im Prozess | Übergabe gegen Bestätigung oder mit Zeugen |
| Zeitlich überlanger Abstand zum Vorfall | Abmahnung verliert Wirkung für Kündigung | Zeitnah nach Vorfall abmahnen |
| Abmahnung wegen anderen Pflichtenkreises | Fehlende Gleichartigkeit zur Kündigung | Pflichtenkreis konsistent halten |
| Keine Kopie in Personalakte | Beweisverlust | Aktenführung sicherstellen (§ 83 BetrVG) |
| Inhaltlich falsche Tatsachen | Anspruch auf Entfernung (§ 242 BGB) | Sachverhalt vor Abmahnung sorgfältig aufklären |
| Datenschutz / § 203 StGB | Strafbarkeit bei unbefugter Weitergabe | Abmahnungsinhalt nicht an Dritte ohne Rechtsgrundlage |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenpflicht

Jede juristische Aussage in jedem auf diesem Skill basierenden Dokument ist nach **references/zitierweise.md** zu belegen:

- Rechtsprechungsbelege im BGH-Stil (Gericht, Entscheidungsform, Datum, AZ, Fundstelle, Rn.).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Bei der Frage der Entbehrlichkeit der Abmahnung h. M. und Gegenauffassung getrennt benennen.
- Halluzinationsrisiko: Alle zitierten Entscheidungen vor Verwendung in Schriftsätzen durch Datenbankrecherche verifizieren.

<!-- AUDIT 27.05.2026 | Bundle 012 | Task 1
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund: AZ korrekt eingesetzt. Thema laut dejure.org und bundesarbeitsgericht.de bestätigt als
"Entfernung Abmahnung aus Personalakte; Wirkungslosigkeit durch Zeitablauf; Warnfunktion/Dokumentationsfunktion"
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Claimed_topic "Weiterbeschäftigungsanspruch" nicht im SKILL-Text vorhanden; kein Änderungsbedarf.
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+AZR+782%2F11
-->

## 4. `agg-pruefung-bewerber-und-beschaeftigte`

**Fokus:** AGG-Prüfung bei Bewerbung und Beschäftigung: Diskriminierungsmerkmale § 1 AGG, Benachteiligungsverbot § 7 AGG, Entschädigungs- und Schadensersatzansprüche § 15 AGG, Beweislastumkehr § 22 AGG, Geltendmachungsfrist § 15 Abs. 4 AGG (zwei Monate). Stellenausschreibung, Auswahlverfahren, Beschäftigungsbedingungen, Beförderung, Entlohnung, Kündigung.

### AGG-Prüfung bei Bewerbern und Beschäftigten

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `AGG-Prüfung bei Bewerbern und Beschäftigten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Das Allgemeine Gleichbehandlungsgesetz (AGG) schützt Bewerber und Beschäftigte vor Benachteiligungen wegen Rasse oder ethnischer Herkunft, Geschlecht, Religion oder Weltanschauung, Behinderung, Alters oder sexueller Identität (§ 1 AGG). Anwendungsfall: wenn - ein Bewerber eine Absage erhalten hat und eine AGG-widrige Selektion vermutet,
- ein Beschäftigter bei Vergütung, Beförderung oder Arbeitsbedingungen benachteiligt wird,
- ein Arbeitgeber ein Stelleninserat, ein Auswahlverfahren oder eine Personalmaßnahme AGG-konform gestalten will,
- eine Entschädigungsforderung nach § 15 AGG droht oder gestellt worden ist,
- die Zwei-Monats-Frist des § 15 Abs. 4 AGG zu überwachen ist.

## Eingaben

- Sachverhaltschilderung: Art der Benachteiligung (Absage, Nichtbeförderung, Gehaltsungleichbehandlung, Kündigung, Belästigung usw.)
- Diskriminierungsmerkmal: Welches Merkmal des § 1 AGG wird behauptet?
- Beweismittel: Ausschreibungstext, Korrespondenz, Interviewnotizen, Vergleichspersonen
- Zeitpunkt: Wann wurde die benachteiligende Maßnahme mitgeteilt bzw. bekannt? (Fristberechnung § 15 Abs. 4 AGG)
- Perspektive: Arbeitnehmer-/Bewerberseite (Anspruchsdurchsetzung) oder Arbeitgeberseite (Verteidigung, präventive Prüfung)
- Betriebsgröße und Betriebsrat vorhanden?
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Einstellungs- und HR-Richtlinien

## Rechtlicher Rahmen

### Primärnormen

- **§ 1 AGG** – Diskriminierungsmerkmale: Rasse, ethnische Herkunft, Geschlecht, Religion, Weltanschauung, Behinderung, Alter, sexuelle Identität
- **§ 2 AGG** – Sachlicher Anwendungsbereich: Beschäftigungs- und Arbeitsbedingungen, Zugang zu Beschäftigung, Sozialschutz, Bildung, soziale Vergünstigungen
- **§ 3 AGG** – Unmittelbare und mittelbare Benachteiligung; Belästigung (§ 3 Abs. 3 AGG), sexuelle Belästigung (§ 3 Abs. 4 AGG)
- **§ 7 AGG** – Benachteiligungsverbot gegenüber Beschäftigten i.S.d. § 6 AGG (auch Bewerber und Leiharbeitnehmer)
- **§ 11 AGG** – Diskriminierungsfreie Ausschreibung: keine Merkmale nach § 1 AGG, keine mittelbar ausschließenden Formulierungen
- **§ 12 AGG** – Arbeitgeberpflichten: Maßnahmen zur Prävention, Schulung, Aushang; Beschwerderecht § 13 AGG
- **§ 15 Abs. 1 AGG** – Schadensersatz (Vermögensschaden): bei Verschulden des Arbeitgebers
- **§ 15 Abs. 2 AGG** – Entschädigung (immaterieller Schaden): ohne Verschuldenserfordernis, max. drei Monatsgehälter bei Nichteinstellung
- **§ 15 Abs. 4 AGG** – Geltendmachungsfrist: zwei Monate ab Kenntnis der Benachteiligung; Verfall bei Fristversäumung
- **§ 15 Abs. 6 AGG** – Kein Anspruch auf Begründung; aber Auskunftspflicht aus Treu und Glauben (§ 242 BGB) diskutiert
- **§ 22 AGG** – Beweislastverteilung: Beweislastumkehr, wenn Bewerber Indizien glaubhaft macht; dann Arbeitgeber muss beweisen, kein Verstoß gegen das Benachteiligungsverbot vorgelegen
- **§ 24 AGG** – Anwendung auf öffentlichen Dienst

### Europarechtlicher Rahmen

- RL 2000/43/EG (Antirassismusrichtlinie)
- RL 2000/78/EG (Rahmenrichtlinie Beschäftigung)
- RL 2006/54/EG (Gleichbehandlungsrichtlinie Arbeit und Beschäftigung – Geschlecht)
- Art. 19 AEUV (Antidiskriminierungskompetenz der EU)

### Rechtsprechung (Stand Mai 2026)

- **BAG, Urteil vom 23.10.2025 - 8 AZR 300/24** (Paarvergleich bei Entgeltdiskriminierung): Zur Begruendung der Vermutung einer geschlechtsbezogenen Entgeltdiskriminierung (§ 22 AGG) genuegt der Paarvergleich mit einem einzelnen Vergleichskollegen des anderen Geschlechts, der für gleiche oder gleichwertige Arbeit hoehere Verguetung erhaelt. Auf Mediane, Vergleichsgruppengroessen oder Durchschnittsbetrachtungen kommt es nicht an. Auch der bestverdienende maennliche Kollege kann Vergleichsperson sein. Vorinstanz: LAG Baden-Wuerttemberg. Quellen: dejure.org-Vernetzung BAG 23.10.2025 - 8 AZR 300/24; BAG-Pressemitteilung "Anspruch auf Entgeltdifferenz wegen Geschlechtsdiskriminierung - Paarvergleich".
- **BAG, Urteil vom 20.02.2025 - 8 AZR 61/24** (DSGVO-Schadensersatz bei verspaeteter Auskunft): Allein ein "Stoergefuehl" oder negativer Gemuetszustand begruendet keinen Kontrollverlust i.S.v. Art. 82 DSGVO; erforderlich ist eine konkret begruendete Furcht vor Datenmissbrauch oder ein tatsaechlicher Kontrollverlust. Quellen: dejure.org-Vernetzung BAG 20.02.2025 - 8 AZR 61/24; Volltext-PDF auf bundesarbeitsgericht.de verfuegbar.
- Weitere aktuelle Rechtsprechung vor Schriftsatzverwendung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de) verifizieren.

## Ablauf

### 1. Anwendungsbereich klären (§§ 2, 6 AGG)

| Frage | Inhalt |
|---|---|
| Persönlicher Anwendungsbereich | Beschäftigter i.S.d. § 6 AGG? (Arbeitnehmer, Beamte, Auszubildende, arbeitnehmerähnliche Personen, Bewerber) |
| Sachlicher Anwendungsbereich | Maßnahme betrifft Zugang, Bedingungen, Aufstieg, Entgelt oder Kündigung (§ 2 Abs. 1 AGG)? |
| Merkmal | Liegt ein Merkmal des § 1 AGG vor? (Beweislastindiz, nicht Beweis) |

Falls kein AGG-Merkmal berührt: Prüfung beenden und Sachgebiet aufzeigen (z.B. allgemeines Arbeitsvertragsrecht, KSchG).

### 2. Benachteiligung subsumieren (§ 3 AGG)

**Unmittelbare Benachteiligung (§ 3 Abs. 1 AGG):**
Weniger günstige Behandlung wegen eines Merkmals des § 1 AGG als eine andere Person in einer vergleichbaren Situation erfährt, erfahren hat oder erfahren würde.

**Mittelbare Benachteiligung (§ 3 Abs. 2 AGG):**
Scheinbar neutrale Vorschrift, Kriterium oder Verfahren, das Personen mit einem Merkmal des § 1 AGG in besonderer Weise benachteiligen kann, es sei denn, es liegt eine sachliche Rechtfertigung vor.

**Belästigung (§ 3 Abs. 3 AGG):**
Unerwünschte Verhaltensweise, die Würde verletzt und ein einschüchterndes, feindseliges, entwürdigendes, beleidigendes oder belästigendes Umfeld schafft.

**Anweisung zur Benachteiligung (§ 3 Abs. 5 AGG):** Gilt selbst als Benachteiligung.

### 3. Rechtfertigung prüfen (§§ 5, 8–10 AGG)

- **§ 8 AGG** – Berufliche Anforderung: Merkmal ist wesentliche und entscheidende berufliche Anforderung; Ziel ist legitim; Anforderung ist verhältnismäßig.
- **§ 9 AGG** – Religionsgemeinschaften / Weltanschauungsgemeinschaften: besonderes Ethos.
- **§ 10 AGG** – Altersdiskriminierung: sachliche Gründe (z.B. Berufszugang, Berufsausbildung, Schutzziele, angemessene Beschäftigungspolitik, Vergütungs- und Rentensysteme).
- **Positive Maßnahmen (§ 5 AGG):** Bevorzugungsmaßnahmen zur Förderung von Benachteiligten zulässig, wenn bestehende Nachteile beseitigt werden sollen.

### 4. Beweislast analysieren (§ 22 AGG)

Das Gericht der Arbeit wendet eine zweistufige Beweislastverteilung an:

**Stufe 1 – Indizien (Bewerber/Beschäftigter):**
Glaubhaftmachung von Tatsachen, die eine Benachteiligung wegen eines AGG-Merkmals vermuten lassen:
- AGG-widrige Ausschreibung (§ 11 AGG Verstoß)
- Statistisch signifikante Unterrepräsentation
- Zeitliche Nähe zwischen Bekanntwerden des Merkmals und der benachteili­genden Maßnahme
- Abweichung vom üblichen Entscheidungsablauf
- Diskriminierende Äußerungen von Entscheidungsträgern

**Stufe 2 – Gegenbeweis (Arbeitgeber):**
Arbeitgeber muss beweisen (Vollbeweis), dass kein Verstoß gegen das Benachteiligungsverbot vorgelegen hat; rein sachliche Gründe, die die Entscheidung tragen, müssen dargelegt und bewiesen werden.

### 5. Ansprüche und Fristen

**Schadensersatz (§ 15 Abs. 1 AGG):**
- Voraussetzung: Verschulden des Arbeitgebers oder seiner Erfüllungsgehilfen (§ 278 BGB)
- Inhalt: Ersatz des Vermögensschadens (z.B. entgangenes Gehalt)
- Beweislast: Nach § 22 AGG

**Entschädigung (§ 15 Abs. 2 AGG):**
- Kein Verschulden erforderlich
- Bei Nichteinstellung: max. drei Monatsgehälter (§ 15 Abs. 2 S. 2 AGG); Richtwert – kann unterschritten werden
- Richterliche Schätzung nach § 287 ZPO; Faktoren: Schwere des Verstoßes, Wiederholungsgefahr, Genugtuungsfunktion, Präventionswirkung

**Geltendmachungsfrist (§ 15 Abs. 4 AGG):**
- Zwei Monate ab Kenntnis der Benachteiligung
- Schriftliche Geltendmachung beim Arbeitgeber genügt (kein Klageerhebungserfordernis, aber Vorsicht: AGB-Ausschlussfristen können kürzer sein)
- Fristbeginn: Zugang der Absage bzw. Bekanntwerden der benachteiligenden Maßnahme
- Fristversäumung: Anspruchsverlust (Ausschlussfrist, keine Verjährung)
- Wichtig: "zwei Monate" bedeutet zwei Monate — nicht "2,0 Monate" und nicht "60 Tage" pauschal (§ 188 BGB Abs. 2 BGB: Fristende an dem Tag des zweiten Monats, der durch Zahl dem Fristbeginn entspricht)

### 6. Präventive Arbeitgeberpflichten (§ 12 AGG)

- Schulungspflicht: Beschäftigte über Verbote des AGG unterrichten
- Aushangpflicht: AGG-Text oder Hinweis im Betrieb
- Beschwerdesystem (§ 13 AGG): Zugang zu Beschwerdestelle; Dokumentation
- Reaktionspflicht (§ 12 Abs. 3–4 AGG): Bei Belästigung geeignete Maßnahmen (Ermahnung, Abmahnung, Versetzung, Kündigung)
- Dokumentation des Auswahlverfahrens empfohlen (Stichwort: Auswahlgespräch-Protokoll, Bewertungsmatrix)

## Prüfschema

**Checkliste AGG-Prüfung:**

- [ ] Persönlicher Anwendungsbereich: Beschäftigter/Bewerber i.S.d. § 6 AGG?
- [ ] Sachlicher Anwendungsbereich: § 2 Abs. 1 Nr. 1–8 AGG?
- [ ] Merkmal des § 1 AGG identifiziert?
- [ ] Benachteiligungsform (unmittelbar / mittelbar / Belästigung)?
- [ ] Vergleichsperson oder Vergleichsgruppe konkretisiert?
- [ ] Rechtfertigungstatbestand (§§ 5, 8–10 AGG)?
- [ ] Indizien für § 22 AGG glaubhaft gemacht?
- [ ] Arbeitgeber-Gegenbeweis möglich?
- [ ] Frist § 15 Abs. 4 AGG: Zwei Monate ab Kenntnis – gewahrt?
- [ ] Betriebsinterne Beschwerde (§ 13 AGG) eingereicht?
- [ ] Schadensersatz § 15 Abs. 1 AGG (Vermögensschaden) bezifferbar?
- [ ] Entschädigung § 15 Abs. 2 AGG (max. drei Monatsgehälter) beansprucht?

## Risikoampel

| Befund | Rot | Orange | Grün |
|--------|-----|--------|-------|
| Stellenausschreibung | Merkmal des § 1 AGG explizit genannt (§ 11 AGG-Verstoß) | Mittelbar ausschließendes Kriterium ohne Rechtfertigung | Diskriminierungsmerkmalsneutral, Anforderungen sachlich |
| Auswahlverfahren | Dokumentation fehlt, Entscheider hat diskriminierende Äußerungen gemacht | Lückenhaft dokumentiert, Merkmal bekannt geworden vor Entscheidung | Nachvollziehbarer, merkmalsneutraler Auswahlprozess dokumentiert |
| Entschädigungsforderung | Frist § 15 Abs. 4 AGG läuft; Indizien stark; kein Gegenbeweis möglich | Indizien vorhanden; Gegenbeweis möglich aber aufwendig | Frist abgelaufen oder kein Indiz glaubhaft gemacht |
| Präventionsmaßnahmen | Keine Schulung, kein Beschwerdesystem, keine Aushänge | Teilweise vorhanden, lückenhafte Dokumentation | Vollständig nach § 12 AGG, Beschwerdesystem aktiv |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Ausgabeformat

```
AGG-PRÜFUNG – [Position / Maßnahme] – [Datum]
VERTRAULICH – § 43a Abs. 2 BRAO / § 203 StGB

Ergebnis: [🟢 Kein AGG-Risiko / 🟡 Risiko – Maßnahmen erforderlich / 🔴 Hohes Diskriminierungsrisiko]

Fristenwarnung: § 15 Abs. 4 AGG – Ablauf [Datum] – noch [X] Tage

I. Anwendungsbereich [§§ 2, 6 AGG]
 Persönlich: [Ergebnis]
 Sachlich: [Ergebnis]
 Merkmal: [§ 1 AGG-Merkmal oder keines identifiziert]

II. Benachteiligungsform [§ 3 AGG]
 [Unmittelbar / Mittelbar / Belästigung / Keine]
 Subsumtion: [Kurze Würdigung]

III. Rechtfertigung [§§ 5, 8–10 AGG]
 [Einschlägig / Nicht einschlägig]
 Begründung: [Norm und Verhältnismäßigkeit]

IV. Beweislage [§ 22 AGG]
 Indizien Bewerber/Beschäftigter: [Ja / Nein / Teilweise]
 Gegenbeweis Arbeitgeber: [Möglich / Schwierig / Ausgeschlossen]

V. Ansprüche [§ 15 AGG]
 Schadensersatz (§ 15 Abs. 1): [Betrag / entfällt]
 Entschädigung (§ 15 Abs. 2): [Schätzung / entfällt]
 Frist gewahrt: [Ja/Nein – Datum]

VI. Risikoampel [🟢 / 🟡 / 🔴]

Handlungsempfehlungen:
 1. ...
 2. ...

Verwandte Skills:
 - arbeitsrecht/skills/einstellungspruefung/SKILL.md (Gesamtprüfung Einstellung inkl. AGG)
 - arbeitsrecht/skills/kuendigungs-pruefung/SKILL.md (AGG-Konformität bei Kündigung)
 - arbeitsrecht/skills/mandat-triage-arbeitsrecht/SKILL.md (Fristprüfung bei Mandatseingang)
```

## Kombination AGG-Entschädigung und DSGVO-Auskunft

**Typische Konstellation:** Bewerber oder Beschäftigte, die eine Diskriminierung geltend machen, stellen häufig zeitgleich mit oder unmittelbar nach der AGG-Entschädigungsklage (§ 15 Abs. 2 AGG) ein Auskunftsersuchen nach Art. 15 DSGVO. Ziel ist es, interne Auswahlunterlagen, Bewertungsbögen, Interviewprotokolle oder Vergleichsdaten zu erlangen, die als Indizienmittel im AGG-Verfahren dienen (§ 22 AGG).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Ein kumulativer Missbrauchsnachweis ist erforderlich:

1. **Objektives Element:** Äußere Umstände — z. B. zeitlicher Zusammenhang zwischen Absage, AGG-Geltendmachung (Zwei-Monats-Frist § 15 Abs. 4 AGG) und Auskunftsantrag; Legal-Tech-Vollmacht oder Muster massenhafter Antragstellung; fehlende inhaltliche Anbindung an Datenschutzinteressen.
2. **Subjektives Element:** Missbräuchliche Absicht — vorrangige Nutzung des Auskunftsanspruchs zur Beweisbeschaft­ung im AGG-Verfahren oder zur Druckerzeugung, nicht zum Schutz personenbezogener Daten.

Die Hürden bleiben **hoch**: Das Auskunftsrecht (Art. 8 GRCh) gilt; Ausnahmen sind eng auszulegen. Ein einziger Antrag ohne weitere Anhaltspunkte genügt nicht.

**Praxishinweise für den Arbeitgeber:**
- DSGVO-Auskunft (Art. 15 DSGVO) und AGG-Entschädigungsbegehren (§ 15 AGG) laufen auf verschiedenen Rechtsgebieten parallel: Auskunftsklage gehört vor das **Landgericht** (§ 44 BDSG i.V.m. Art. 79 DSGVO); AGG-Entschädigungsklage vor das **Arbeitsgericht** (§ 2 Abs. 1 Nr. 3 ArbGG).
- Auskunft innerhalb eines Monats erteilen (Art. 12 Abs. 3 DSGVO); andernfalls droht eigenständiger Schadensersatz nach Art. 82 DSGVO zusätzlich zur AGG-Haftung.
- Auswahlunterlagen und Bewertungsbögen sind personenbezogene Daten des Bewerbers — Offenlegungs- und Auskunftspflicht beachten; Geheimhaltungsinteressen Dritter (andere Bewerber) abwägen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Querverweis: `arbeitsrecht/skills/kuendigungs-pruefung/SKILL.md` (Abschnitt DSGVO-Auskunftsersuchen als Druckmittel).

## Quellen / Updates

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- AGG-Beweislast: § 22 AGG und frei verifizierte BAG-Rechtsprechung verwenden; keine Kommentarzitate aus Modellwissen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- AGG-Schutzmerkmale: §§ 1, 7, 15 AGG und freie Rechtsprechungsquellen verwenden; keine Kommentarzitate aus Modellwissen.

Bei wesentlichen Rechtsentwicklungen Skill aktualisieren. Stand: 05/2026.

<!-- AUDIT 27.05.2026 | Bundle 012 | Task 2
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund WRONG_TOPIC + falsche NZA-Fundstelle korrigiert.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
schwerbehinderte Bewerber zu Vorstellungsgespräch einzuladen (auch intern); Entschädigung § 15 Abs. 2 AGG"
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=8+AZR+75%2F19
Rn.-Angabe "Rn. 22" entfernt, da dejure-Auszug für dieses Thema Rn. 31 cc ausweist.
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 14 TzBfG
- § 102 BetrVG
- § 4 KSchG
- § 1 KSchG
- § 17 TzBfG
- § 26 BDSG
- § 12 KSchG
- § 9 KSchG
- § 7 KSchG
- § 15 AGG
- § 23 KSchG
- § 22 AGG

### Leitentscheidungen

- EuGH C-55/18

