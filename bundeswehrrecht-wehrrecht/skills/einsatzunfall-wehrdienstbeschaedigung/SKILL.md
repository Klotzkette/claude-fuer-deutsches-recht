---
name: einsatzunfall-wehrdienstbeschaedigung
description: "Einsatzunfall Wehrdienstbeschaedigung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Einsatzunfall Wehrdienstbeschaedigung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Einsatzunfall Wehrdienstbeschaedigung** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `einsatzunfall-wehrdienstbeschaedigung` | Einsatzunfall Wehrdienstbeschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `entlassung-auf-eigenen-antrag` | Entlassung auf eigenen Antrag: prüft § 46 SG, Antragsformalitäten, Widerruf, Versorgungsfolgen und Kostenrückforderung. Norm-/Quellenanker: § 46 SG, SVG, § 56 SG. |
| `ernennung-dienstgrad-laufbahnrecht` | Ernennung, Dienstgrad, Laufbahnrecht: prüft SG §§ 1–5, Laufbahngruppen, Beförderungsvoraussetzungen und Konkurrentenklage. Norm-/Quellenanker: SG, SLV, ZDv A-1340. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Einsatzunfall Wehrdienstbeschaedigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `einsatzunfall-wehrdienstbeschaedigung`

**Fokus:** Einsatzunfall Wehrdienstbeschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Einsatzunfall und Wehrdienstbeschädigung

## Fachkern: Einsatzunfall und Wehrdienstbeschädigung
- **Spezialgegenstand:** Einsatzunfall und Wehrdienstbeschädigung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Der Einsatzunfall ist eine besonders qualifizierte Form der Wehrdienstbeschädigung: Schädigung während eines besonderen Auslandseinsatzes oder einer gleichgestellten Verwendung (§ 81a SVG). Folge sind höhere Leistungen, insbesondere eine einmalige Entschädigung nach Einsatzversorgungs-Verbesserungsgesetz und besondere Berufsförderungsansprüche. Der Skill ordnet die Voraussetzungen, dokumentiert die Tatfeststellung und führt durch das Verwaltungsverfahren.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welcher konkrete Einsatz (KFOR, EUFOR, Resolute Support, Sea Guardian, EUTM, sonstige Mission)?
- Welche Verwendung (Truppe, Kontingent, Beobachter, Stab, NATO/EU)?
- Was war das auslösende Ereignis – Gefecht, Anschlag, Unfall, dienstliche Tätigkeit im Lager?
- Sofortige Meldung an Vorgesetzten erfolgt?
- Welche ärztlichen Befunde liegen vor (truppenärztlich, im Einsatzland, in Deutschland)?
- Ist die Verwendung als besonderer Einsatz nach § 63c SG anerkannt?

## Rechtlicher Rahmen

- § 81 SVG: Wehrdienstbeschädigung (Grundtatbestand).
- § 81a SVG: Einsatzunfall – Schädigung durch oder bei einem besonderen Auslandseinsatz (§ 63c SG) oder einer dem Wehrdienst eigentümlichen Gefahr.
- § 81e SVG: Einmalige Entschädigung – bis 150.000 Euro bei GdS 50 v.H. und mehr (Einsatzversorgungs-Verbesserungsgesetz).
- § 81b SVG: Erweiterte Heilbehandlung und Pflege.
- § 63c SG: Definition des besonderen Auslandseinsatzes.
- Bundestagsmandat: Anlage zur jeweiligen Bundestagsbeteiligung – Voraussetzung für Anerkennung als besonderer Einsatz.
- §§ 102 ff. SVG: Verwaltungsverfahren.
- Versorgungsmedizinische Grundsätze (VMG).
- Beweismaß: Vollbeweis Schädigung, Wahrscheinlichkeit der Kausalität.

## / Schritt für Schritt

1. **Einsatzstatus klären.** Bundestagsmandat? Einsatz nach § 63c SG anerkannt? OPLAN/Einsatzbefehl beibringen.
2. **Ereignisdokumentation.** Unfallmeldung, Funkspruch, Sanitätsbuch, Patientenkarte, Kameradenbericht, ggf. JET (Joint Operations Centre Logs).
3. **Medizinische Befundkette.** Erstversorgung Einsatzland → Repatriierung → Bundeswehrkrankenhaus → Reha → Privatarzt.
4. **Kausalität herausarbeiten.** Direkte Kampfhandlung? "Eigentümliche Gefahr" des Einsatzlandes (Tropen, Sprengfallen, Verkehr, psychische Belastung)?
5. **Antrag auf Anerkennung als Einsatzunfall** beim BAPersBw mit allen Belegen.
6. **Begutachtung** durch versorgungsmedizinische Stelle; eigene Stellungnahme/Gegengutachten.
7. **GdS-Festsetzung** – ab 50 v.H. einmalige Entschädigung § 81e SVG; gestaffelt.
8. **Berufsförderung.** §§ 4 ff. SVG i.V.m. einsatzversorgungsrechtlichen Regelungen.
9. **Widerspruch** § 70 ff. VwGO entsprechend – 1 Monat. Klage Sozialgericht/Verwaltungsgericht.

## Trade-off-Matrix

| Konstellation | Strategie A | Strategie B |
| --- | --- | --- |
| Klare Kampfverletzung | Sofortantrag, hohe einmalige Entschädigung | Eilentscheidung beantragen |
| Krankheit nach Tropenaufenthalt | Tropenmedizinisches Gutachten | Indizien aus Einsatzberichten |
| PTBS Jahre später | Belastungsanamnese, Zeugen, Tagebücher | Spezialgutachten Psychotraumatologie |
| Unfall im Lager / nicht Kampfhandlung | "Eigentümliche Gefahr" begründen | reguläre WDB statt Einsatzunfall |

## Praxistipps

- Bundestagsmandate sind nicht statisch – ein Einsatz kann anerkannt oder nicht anerkannt sein. Aktuelle Mandatsliste prüfen.
- "Eigentümliche Gefahr" reicht aus – kein Direkttreffer erforderlich. Verkehrsunfall auf Patrouille, Malariainfektion, Hitzschlag im Lager fallen darunter.
- Einmalige Entschädigung § 81e SVG ist neben Rente und Heilbehandlung möglich.
- Bei kritischen Diagnosen Reha- und Pflegeleistungen früh beantragen (§ 81b SVG).
- Vertraulichkeit der Einsatzberichte: Schwärzungen sind häufig – beantragen Sie nur die relevanten Teile.

## Mustertexte

**Antrag auf Anerkennung als Einsatzunfall:**
"Beim BAPersBw beantrage ich die Anerkennung eines Einsatzunfalls nach § 81a SVG sowie Leistungen nach § 81e SVG. Sachverhalt: Mein Mandant war im Rahmen des Einsatzes [Bezeichnung] vom [Datum bis] in [Einsatzland] eingesetzt. Am [Datum] erlitt er [Diagnose] durch [Ereignis]. Beweismittel: 1. Einsatzbefehl/OPLAN-Auszug, 2. Sanitätsbuch (Anl. 2), 3. Berichte BwKrhs [...] (Anl. 3–5), 4. Zeugen Stbsf [Name], Hptm [Name]."

**Widerspruch gegen Ablehnung des Einsatzunfallstatus:**
"Der Bescheid ordnet die Schädigung als reguläre WDB ein. Tatsächlich liegt ein Einsatzunfall im Sinne des § 81a SVG vor: 1. Bundestagsmandat [Drucksache] erfasste die Verwendung. 2. Die Schädigung ist eine eigentümliche Gefahr des Einsatzes, weil [...]. 3. Die Versorgungsmedizinischen Grundsätze begründen einen GdS von [%]."

## Typische Fehler

- Reguläre WDB beantragen, obwohl Einsatzunfall einschlägig wäre.
- Bundestagsmandat nicht beigebracht – Anerkennung als besonderer Einsatz scheitert.
- Kausalität nur behauptet, nicht mit Zeugen/Berichten belegt.
- Einmalige Entschädigung § 81e SVG nicht ausdrücklich beantragt.
- GdS unter 50 v.H. akzeptiert, obwohl Folgeschäden den Wert erhöhen.

## Querverweise

- soldatenversorgungsgesetz-beschaedigtenversorgung
- einsatz-unfall-versorgung-dokumentenplan
- ptbs-einsatzfolge-beweisfuehrung
- auslandseinsatz-mandat-einsatzregeln
- aerztliche-begutachtung-dienstfaehigkeit
- statusrechte-im-einsatz-urlaub-betreuung

## Quellen Stand 06/2026

- SVG §§ 81, 81a, 81b, 81e – Volltext gesetze-im-internet.de.
- SG § 63c – Volltext gesetze-im-internet.de.
- Bundestagsmandate – Drucksachen des Deutschen Bundestages, einsehbar bei bundestag.de.
- Versorgungsmedizinische Grundsätze – BMAS.
- BSG/BVerwG zu § 81a SVG – ständige Rechtsprechung; Az. nach Verifikation.

## 2. `entlassung-auf-eigenen-antrag`

**Fokus:** Entlassung auf eigenen Antrag: prüft § 46 SG, Antragsformalitäten, Widerruf, Versorgungsfolgen und Kostenrückforderung. Norm-/Quellenanker: § 46 SG, SVG, § 56 SG.

# Entlassung auf eigenen Antrag

## Fachkern: Entlassung auf eigenen Antrag
- **Spezialgegenstand:** Entlassung auf eigenen Antrag. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die Entlassung auf eigenen Antrag (§ 46 SG) ist das Recht des Soldaten, sein Dienstverhältnis zu beenden. Sie löst eine Reihe von Folgen aus: Versorgungsansprüche, Kostenrückforderungen, Ende der Heilfürsorge.

Der Antrag kann in engen Grenzen widerrufen werden. Einschneidend sind die Ausbildungskostenrückforderungen nach § 56 SG.

## Einschlägige Normen und Quellen

- § 46 SG — Entlassung auf eigenen Antrag
- § 55 SG — Entlassung aus anderen Gründen
- § 56 SG — Rückforderung Ausbildungskosten
- SVG §§ 5, 9 — Versorgungsfolgen
- §§ 6–11 WBO — Rechtsbehelfe

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- SaZ oder BeruSold? Wie lange gedient?
- Antrag schriftlich gestellt?
- Wann soll Entlassung wirksam werden?
- Gibt es eine Ausbildungskostenrückforderung?
- Kann der Antrag noch widerrufen werden?
- Sind Versorgungsansprüche gesichert (SVG)?

## Prüf- und Arbeitslogik

### Schritt 1 — Antragsformalitäten § 46 SG

Schriftlichkeit: Antrag muss schriftlich gestellt werden.
Frist: Dienstherr entscheidet binnen angemessener Zeit.
Entlassungstermin: frühestens zum Ende des Monats nach Antragstellung.
Besonderheiten: Einsatz/Verwendung im Ausland kann Aufschub rechtfertigen.

### Schritt 2 — Widerruf des Antrags

Widerruf möglich, solange Entlassung nicht bestandskräftig verfügt.
Widerruf schriftlich erklären.
Zustimmung des Dienstherrn erforderlich (Ermessensentscheidung).
WBO-Beschwerde bei Verweigerung der Widerrufsannahme.

### Schritt 3 — Versorgungsfolgen

SaZ: Übergangsgebührnisse § 5 SVG (ab 4 Jahren), Berufsförderungsdienst.
BeruSold: Anspruch auf Ruhegehalt nur nach Mindestdienstzeit § 13 SVG.
Heilfürsorge endet mit Entlassung.
PKV prüfen.

### Schritt 4 — Rückforderung Ausbildungskosten

§ 56 SG: Rückforderung bei Entlassung auf eigenen Antrag.
Zeitstaffelung: linear nach geleisteter Dienstzeit.
Härteerlass und Billigkeitsklausel beantragen.
Widerspruch 1 Monat.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Muster: Entlassungsantrag § 46 SG
- Checkliste: Folgen der Entlassung (Versorgung, PKV, Kosten)
- Prüfschema: Kann der Antrag widerrufen werden?

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — § 46 SG
- https://www.gesetze-im-internet.de/svg/ — SVG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `ernennung-dienstgrad-laufbahnrecht`

**Fokus:** Ernennung, Dienstgrad, Laufbahnrecht: prüft SG §§ 1–5, Laufbahngruppen, Beförderungsvoraussetzungen und Konkurrentenklage. Norm-/Quellenanker: SG, SLV, ZDv A-1340.

# Ernennung, Dienstgrad und Laufbahnrecht

## Fachkern: Ernennung, Dienstgrad und Laufbahnrecht
- **Spezialgegenstand:** Ernennung, Dienstgrad und Laufbahnrecht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Ernennung und Beförderung erfordern Eignung, Befähigung und fachliche Leistung (Art. 33 Abs. 2 GG). Die SLV regelt Laufbahngruppen (Mannschaften, Unteroffiziere, Offiziere), Voraussetzungen und Wartezeiten.

Fehlende Beförderungen und Fehlentscheidungen bei der Ernennung sind mit WBO-Beschwerde anfechtbar.

## Einschlägige Normen und Quellen

- §§ 1–5 SG — Status und Ernennung
- SLV — Soldatenlaufbahnverordnung
- ZDv A-1340 — Laufbahnvorschriften
- Art. 33 Abs. 2 GG — Bestenauslese
- §§ 6, 17 WBO — Rechtsbehelfe

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welcher Dienstgrad und welche Laufbahn?
- Wurde eine Beförderung abgelehnt oder verzögert?
- Liegt ein Konkurrentenstreit vor?
- Welche Eignungsvoraussetzungen sind streitig?
- Wurden Auswahlentscheidungen dokumentiert?

## Prüf- und Arbeitslogik

### Schritt 1 — Ernennungsvoraussetzungen

SG § 4: Ernennung durch Bundesminister der Verteidigung (oder Delegation).
SLV: Laufbahngruppen und Zugangsbedingungen.
Dienstgradfolge: geregelt in SLV Anlagen.
Statusbegründung: Aushändigung der Ernennungsurkunde.

### Schritt 2 — Laufbahngruppen SLV

Mannschaften: Stabsunteroffizier ist Beförderungsziel ohne Offiziersausbildung.
Unteroffiziere: Aufstiegsmöglichkeiten, Portepée, Feldwebel.
Offiziere: Leutnant bis General.
Sanitätsoffiziere, Militärmusik: Sonderlaufbahnen.

### Schritt 3 — Beförderungsvoraussetzungen

Mindestdienstzeit in Dienstgrad (SLV).
Positive Beurteilung (Notenschwelle).
Planstelle muss vorhanden sein (Stellenplan).
Auswahlentscheidung nach Art. 33 Abs. 2 GG.

### Schritt 4 — Konkurrentenklage und einstweiliger Rechtsschutz

WBO-Beschwerde: 1 Monat nach Bekanntgabe Auswahlentscheidung.
TDG: Besetzungsstopp beantragen — sofort!
Akteneinsicht: Auswahlvermerk und Beurteilungen Mitbewerber.
BVerwG Wehrdienstsenat: Grundsatzfragen.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Laufbahngruppen und Beförderungsstufen (SLV)
- Prüfschema: Beförderungsvoraussetzungen
- Muster-WBO-Beschwerde gegen Nichtbeförderung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — SG §§ 1–5
- https://www.gesetze-im-internet.de/slv_2002/ — SLV
- https://dejure.org/gesetze/GG/33.html
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
