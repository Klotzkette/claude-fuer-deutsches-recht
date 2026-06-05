---
name: dienstunfaehigkeit-entlassung-dienstzeit
description: "Dienstunfaehigkeit Entlassung Dienstzeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dienstunfaehigkeit Entlassung Dienstzeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Dienstunfaehigkeit Entlassung Dienstzeit** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dienstunfaehigkeit-entlassung-zurruhesetzung` | Dienstunfähigkeit Entlassung Zurruhesetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `dienstzeit-soldat-auf-zeit-berufssoldat-fwdl` | Dienstzeiten SaZ, BeruSold, FWDL: prüft SG §§ 23–32, Verlängerung, Verpflichtungszeiten und Statusübergänge. Norm-/Quellenanker: SG §§ 23–32. |
| `einsatz-unfall-versorgung-dokumentenplan` | Einsatz, Unfall, Versorgung Dokumentenplan: prüft erforderliche Unterlagen für Einsatz-WDB-Anträge, Fristen und Beweissicherung. Norm-/Quellenanker: SVG §§ 27 und 63a ff., EinsatzWVG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Dienstunfaehigkeit Entlassung Dienstzeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dienstunfaehigkeit-entlassung-zurruhesetzung`

**Fokus:** Dienstunfähigkeit Entlassung Zurruhesetzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Dienstunfähigkeit – Entlassung und Zurruhesetzung

## Fachkern: Dienstunfähigkeit – Entlassung und Zurruhesetzung
- **Spezialgegenstand:** Dienstunfähigkeit – Entlassung und Zurruhesetzung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Verliert der Soldat seine Dienstfähigkeit, führt dies zu unterschiedlichen Folgen je nach Statusgruppe: Soldat auf Zeit – Entlassung; Berufssoldat – Zurruhesetzung mit Ruhegehalt nach BeamtVG/SVG. Maßstab ist die Wehrdienstfähigkeit (Tauglichkeitsgrade T1–T5) und die spezifische Verwendungsfähigkeit. Der Skill ordnet medizinische Begutachtung, Verfahren der Statusentscheidung, Versorgung und Rechtsbehelfe.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Status: Berufssoldat, Soldat auf Zeit, FWDL?
- Diagnose, Behandlung, Heilungsperspektive?
- Vorläufige oder dauernde Dienstunfähigkeit?
- Bisherige Begutachtungen (Truppenarzt, Bundeswehrkrankenhaus, fachärztlich)?
- Steht Wiedereingliederung im Raum (Begrenzte Dienstfähigkeit)?
- Welche Versorgungsfolgen (Ruhegehalt, Beschädigtenversorgung)?

## Rechtlicher Rahmen

- § 44 III SG: Dienstunfähigkeit des Berufssoldaten – Zurruhesetzung.
- § 55 II SG: Entlassung des Soldaten auf Zeit wegen Dienstunfähigkeit.
- § 47 SG: Begrenzte Dienstfähigkeit (analog BeamtStG).
- § 18 SVG i.V.m. BeamtVG: Ruhegehalt des Berufssoldaten.
- §§ 81 ff. SVG: Beschädigtenversorgung bei WDB-Kausalität.
- ZDv A-1340/1 (ärztliche Begutachtung) – nur nach Vorlage.
- Tauglichkeitsgrade T1–T5 nach Wehrmedizinischer Dienstvorschrift.
- WBO-Beschwerderecht und § 17 WBO Verfahren.

## / Schritt für Schritt

1. **Sachstand klären.** Diagnose, Behandlungsplan, Verlauf, Prognose.
2. **Begutachtung.** Truppenarzt - BwKrhs - Spezialist. Eigenes Gutachten möglich.
3. **Statusfolge prüfen.**
 - Berufssoldat: Zurruhesetzung § 44 III SG plus Ruhegehalt.
 - Soldat auf Zeit: Entlassung § 55 II SG plus ggf. Übergangsgebührnisse.
 - Begrenzte Dienstfähigkeit: § 47 SG analog – Weiterverwendung mit reduzierter Belastung.
4. **WDB-Frage.** Ist die Dienstunfähigkeit Folge einer Wehrdienstbeschädigung / eines Einsatzunfalls? Wenn ja: § 81 ff. SVG-Versorgung zusätzlich.
5. **Verfahrensgang.** Anhörung des Soldaten, Stellungnahme, ärztliche Kontrolluntersuchung, Verfügung mit Rechtsbehelfsbelehrung.
6. **Beschwerde** § 1 WBO – 1 Monat. Eilantrag bei vorläufiger Maßnahme.
7. **Versorgungsrechnung.** Mindestversorgung, Ruhegehaltssatz nach Dienstzeit, Erhöhung bei Dienstbeschädigung.
8. **Wiedereingliederung** parallel: Reha, Berufsförderungsdienst (BFD).

## Trade-off-Matrix

| Status | Folge | Versorgung |
| --- | --- | --- |
| Berufssoldat dauerhaft unfähig | Zurruhesetzung § 44 III SG | Ruhegehalt § 18 SVG + ggf. WDB |
| SaZ dauerhaft unfähig | Entlassung § 55 II SG | Übergangsgebührnisse, BFD |
| Begrenzt dienstfähig | Weiterverwendung § 47 SG | volles Gehalt mit Reduzierung |
| WDB-bedingt | Zusätzlich SVG-Versorgung | Beschädigtenrente |

## Praxistipps

- Begutachtung möglichst durch Spezialisten – Truppenärzte sind Generalisten.
- "Verwendungsfähigkeit für besondere Auslandseinsätze" ist Sonderkriterium – Tauglichkeit T2 reicht häufig nicht.
- Vor Zurruhesetzung Wiedereingliederung versuchen (§ 47 SG analog) – Erhalt des Status hat erhebliche Versorgungsvorteile.
- Ruhegehalt setzt 5 Dienstjahre voraus (§ 4 BeamtVG entsprechend) – darunter Mindestversorgung oder Anrechnung in gesetzliche Rente.
- WDB-Kausalität verdoppelt häufig die Versorgungsbasis (Schadenausgleich + Grundversorgung).

## Mustertexte

**Stellungnahme zum Zurruhesetzungsverfahren:**
"Zur beabsichtigten Zurruhesetzung nehme ich wie folgt Stellung: 1. Diagnose, Therapie und Prognose siehe ärztliche Berichte Anl. 1–3. 2. Begrenzte Dienstfähigkeit nach § 47 SG ist möglich; vorgeschlagen wird Verwendung [...]. 3. Hilfsweise: Zurruhesetzung mit gleichzeitiger WDB-Feststellung nach § 81 SVG, weil die Dienstunfähigkeit Folge des Einsatzes [...] vom [Datum] ist."

**WBO-Beschwerde gegen Entlassungsverfügung:**
"Gegen die Entlassungsverfügung vom [Datum] lege ich fristwahrend Beschwerde ein. Rügen: 1. Begutachtung lückenhaft – Spezialgutachten nicht eingeholt. 2. Begrenzte Dienstfähigkeit (§ 47 SG analog) nicht geprüft. 3. WDB-Kausalität übersehen – § 81 SVG-Verfahren parallel einzuleiten. Antrag: Aufhebung der Entlassungsverfügung, hilfsweise Zurruhesetzung mit Anerkennung der WDB."

## Typische Fehler

- Truppenärztliche Beurteilung pauschal akzeptiert.
- Begrenzte Dienstfähigkeit nicht geprüft – sofortige Zurruhesetzung statt Erhalt des Status.
- WDB-Kausalität getrennt vom Statusverfahren prüfen – Versorgungslücke.
- Übergangsgebührnisse SaZ nicht beantragt.
- Frist § 6 WBO verpasst.

## Querverweise

- soldatenversorgungsgesetz-beschaedigtenversorgung
- aerztliche-begutachtung-dienstfaehigkeit
- entlassung-auf-eigenen-antrag
- ptbs-einsatzfolge-beweisfuehrung
- einsatzunfall-wehrdienstbeschaedigung
- dienstzeit-soldat-auf-zeit-berufssoldat-fwdl

## Quellen Stand 06/2026

- §§ 44, 47, 55 SG – Volltext gesetze-im-internet.de.
- SVG, BeamtVG – Volltexte gesetze-im-internet.de.
- ZDv A-1340/1 – nur nach Vorlage.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zur Dienstunfähigkeit (Az. nach Verifikation).
- BAPersBw – Verwaltungspraxis und Formulare.
- Versorgungsmedizinische Grundsätze – BMAS.

## 2. `dienstzeit-soldat-auf-zeit-berufssoldat-fwdl`

**Fokus:** Dienstzeiten SaZ, BeruSold, FWDL: prüft SG §§ 23–32, Verlängerung, Verpflichtungszeiten und Statusübergänge. Norm-/Quellenanker: SG §§ 23–32.

# Dienstzeit: Soldat auf Zeit, Berufssoldat, FWDL

## Fachkern: Dienstzeit: Soldat auf Zeit, Berufssoldat, FWDL
- **Spezialgegenstand:** Dienstzeit: Soldat auf Zeit, Berufssoldat, FWDL. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die Dienstzeit ist statusdefinierend: FWDL (7–23 Monate), SaZ (2–20 Jahre in Abschnitten), Berufssoldat (bis Pensionsalter). Statusübergänge (z. B. SaZ zu BeruSold) erfordern gesondertes Verfahren.

Verpflichtungszeiten binden an bestimmte Ausbildungen. Verlängerungen und Verkürzungen sind unter engen Voraussetzungen möglich.

## Einschlägige Normen und Quellen

- §§ 23–32 SG — Dienstzeiten und Verpflichtungen
- § 40 SG — Dienstzeit Berufssoldat
- § 58b SG — FWDL
- SG § 3 — Ernennung und Statusübergänge
- SVG — Versorgungszeiten

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- FWDL, SaZ oder BeruSold? Aktueller Status?
- Wie lang ist die laufende Verpflichtung?
- Verlängerungsantrag gestellt?
- Statuswechsel SaZ → BeruSold angestrebt?
- Drohende Entlassung vor Ablauf?

## Prüf- und Arbeitslogik

### Schritt 1 — Statusarten und Dienstzeiten

FWDL: § 58b SG, 7–23 Monate, keine BBesG-Besoldung, WSG.
SaZ: §§ 23 ff. SG, 2–20 Jahre (Mindest 2 Jahre, max. 20 Jahre).
BeruSold: § 40 SG, bis Pensionsalter (Offiziere i.d.R. bis 62).

### Schritt 2 — Verlängerung SaZ

§ 28 Abs. 2 SG: Verlängerung bis max. Dienstzeitgrenze.
Antrag rechtzeitig stellen (6 Monate vor Ablauf).
Dienstherr hat Entscheidungsspielraum; Rechtsmittel: WBO bei Ablehnung.

### Schritt 3 — Statusübergang SaZ → BeruSold

Ernennung zum BeruSold: § 40 SG; Altersgrenze prüfen.
Konkurrentenstreit bei Planstellen.
Rechtsweg: WBO-Beschwerde gegen Ablehnung.

### Schritt 4 — Vorzeitige Entlassung und Dienstzeitfolgen

§ 55 SG: Entlassung SaZ aus verschiedenen Gründen.
Versorgungsansprüche: SVG-Übergangsgebührnisse ab 4 Jahren.
Rückforderung Ausbildungskosten: § 56 SG bei eigener Veranlassung.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Dienstzeit-Statusarten im Überblick
- Prüfschema: Verlängerungsantrag SaZ
- Flussdiagramm: Statusübergänge FWDL → SaZ → BeruSold

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — SG §§ 23–32, 40, 55, 58b
- https://dejure.org/gesetze/SG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `einsatz-unfall-versorgung-dokumentenplan`

**Fokus:** Einsatz, Unfall, Versorgung Dokumentenplan: prüft erforderliche Unterlagen für Einsatz-WDB-Anträge, Fristen und Beweissicherung. Norm-/Quellenanker: SVG §§ 27 und 63a ff., EinsatzWVG.

# Einsatz, Unfall, Versorgung — Dokumentenplan

## Fachkern: Einsatz, Unfall, Versorgung — Dokumentenplan
- **Spezialgegenstand:** Einsatz, Unfall, Versorgung — Dokumentenplan. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Nach Einsatz und Unfall müssen zahlreiche Dokumente gesichert und rechtzeitig eingereicht werden. Fehlende Unterlagen führen häufig zu Ablehnungen trotz berechtigter Ansprüche.

Der Dokumentenplan stellt sicher, dass alle relevanten Unterlagen systematisch erfasst und dem BAPersBw fristgerecht vorgelegt werden.

## Einschlägige Normen und Quellen

- SVG §§ 27, 63a–63h — WDB und Einsatzversorgung
- EinsatzWVG — Weiterverwendung
- § 17 SG — Personalakte und Befunde
- BAPersBw — Antragsverfahren
- SGB XIV — ab 2024

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welcher Schaden ist eingetreten (Verletzung, Erkrankung, PTBS)?
- Wann und wo ereignete sich der Einsatz/Unfall?
- Wurden sanitätsdienstliche Befunde dokumentiert?
- Liegt eine Einsatzbescheinigung vor?
- Welche Stellen müssen informiert werden?

## Prüf- und Arbeitslogik

### Schritt 1 — Kategorien der Unterlagen

Einsatzbescheinigung: Kontingentführer, Zeitraum, Region, Vorkommnisse.
Sanitätsdienstliche Befunde: Truppenarzt, SanZ, BwKrhs, externe Ärzte.
Unfallbericht: Dienstunfallmeldung an BAPersBw.
Zeugenerklärungen: Kameraden zu Kampfereignissen.

### Schritt 2 — Fristen und Meldepflichten

Dienstunfall: unverzügliche Meldung (spätestens innerhalb von 2 Wochen).
PTBS/späte Schäden: keine starre Frist, aber frühzeitig melden.
WDB-Antrag: möglichst innerhalb 2 Jahre nach Schaden.
EinsatzWVG: nach Entlassung stellen.

### Schritt 3 — Beweissicherung im Einsatz

Einsatztagebuch, Lagekarten, Funkprotokolle.
Fotos von Verletzungen.
Ärztliche Erstdokumentation sichern.
PTBS: psychologische Erstbetreuung dokumentieren lassen.

### Schritt 4 — Einreichung beim BAPersBw

Ansprechpartner: Referat Einsatzversorgung, BAPersBw.
Vollständige Unterlagen = schnellere Bearbeitung.
Bestätigung des Eingangs verlangen.
Widerspruch bei Ablehnung: 1 Monat.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Dokumenten-Checkliste: Einsatz-WDB-Antrag (vollständige Liste)
- Muster: Dienstunfallmeldung
- Zeitstrahl: Fristen nach Einsatz/Unfall

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/svg/ — SVG §§ 27, 63a ff.
- https://www.gesetze-im-internet.de/einsatzwvg/ — EinsatzWVG
- https://www.bundeswehr.de/de/organisation/personal/bundesamt-fuer-das-personalmanagement

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
