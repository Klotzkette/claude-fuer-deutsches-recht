---
name: wehrpflicht-wehrdienst-wehrpflichtgesetz
description: "Wehrpflicht Wehrdienst Wehrpflichtgesetz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wehrpflicht Wehrdienst Wehrpflichtgesetz

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Wehrpflicht Wehrdienst Wehrpflichtgesetz** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wehrpflicht-wehrdienst-reservist-routing` | Wehrpflicht, Wehrdienst, Reservist Routing: Überblick und Routing zu spezifischen Verfahren. Norm-/Quellenanker: WPflG, SG, UhSiG, ArbPlSchG. |
| `wehrpflichtgesetz-spannungs-und-verteidigungsfall` | Wehrpflichtgesetz Spannungs- und Verteidigungsfall: prüft Reaktivierung Wehrpflicht, Musterung, Heranziehung und Rechtsbehelfe. Norm-/Quellenanker: WPflG, Art. 12a GG, Art. 115a GG. |
| `wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle` | Wehrstrafrecht Fahnenflucht Gehorsamsverweigerung Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Wehrpflicht Wehrdienst Wehrpflichtgesetz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wehrpflicht-wehrdienst-reservist-routing`

**Fokus:** Wehrpflicht, Wehrdienst, Reservist Routing: Überblick und Routing zu spezifischen Verfahren. Norm-/Quellenanker: WPflG, SG, UhSiG, ArbPlSchG.

# Wehrpflicht, Wehrdienst und Reservist — Routing

## Fachkern: Wehrpflicht, Wehrdienst und Reservist — Routing
- **Spezialgegenstand:** Wehrpflicht, Wehrdienst und Reservist — Routing. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die allgemeine Wehrpflicht ist seit 2011 ausgesetzt. Im Spannungs- oder Verteidigungsfall lebt sie wieder auf (WPflG). Aktuell relevant: freiwilliger Wehrdienst (FWD), Reservistendienst, KDV.

Dieser Skill bietet Schnell-Routing zu den spezifischen Verfahren.

## Einschlägige Normen und Quellen

- WPflG — Wehrpflichtgesetz (aktuell suspendiert/Spannungsfall)
- SG §§ 58b, 60–69 — FWD und Reservistendienst
- UhSiG — Unterhaltssicherung
- ArbPlSchG — Arbeitgeberfreistellung
- Art. 12a GG — Wehrpflicht

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- FWD, Reservist oder Spannungsfall?
- Arbeitgeber informiert?
- Unterhaltssicherung beantragt?
- Heranziehung angefochten?
- KDV-Antrag gestellt?

## Prüf- und Arbeitslogik

### Schritt 1 — Wehrpflicht-Status aktuell

WPflG: ausgesetzt, aber nicht abgeschafft (Art. 12a GG bleibt).
Spannungsfall: Wehrpflicht reaktivierbar durch Bundestagsbeschluss.
FWD § 58b SG: freiwillig, 7–23 Monate.
Reservistendienst: §§ 60 ff. SG; freiwillig oder Pflicht.

### Schritt 2 — Routing FWD

→ [bwbes-neu-002]: Wehrsold, UhSiG.
→ [sanitaetsdienst-heilfuersorge]: Heilfürsorge während FWD.
→ [dienstzeit-soldat-auf-zeit-berufssoldat-fwdl]: Statusfragen.

### Schritt 3 — Routing Reservist

→ [reservistendienst-dienstleistungspflicht]: Heranziehungsbescheid anfechten.
→ [unterhaltssicherung-reservisten]: UhSiG.
→ [bwbes-neu-009]: Arbeitgeber-Freistellung.

### Schritt 4 — Routing Spannungsfall / KDV

→ [bwbes-neu-011]: KDV und Statusfolgen.
→ [befehl-verweigern-gewissensnot-rechtswidrigkeit]: Gewissenskonflikt.
Musterungsverfahren: DV 46/1.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Routing-Tabelle: Wehrpflicht-Thema → zuständiger Skill
- Checkliste: Erste Schritte nach Einberufungsbescheid

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wpflg/ — WPflG
- https://www.gesetze-im-internet.de/sg/ — §§ 58b, 60 ff. SG
- https://dejure.org/gesetze/GG/12a.html
- https://www.bundeswehr.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `wehrpflichtgesetz-spannungs-und-verteidigungsfall`

**Fokus:** Wehrpflichtgesetz Spannungs- und Verteidigungsfall: prüft Reaktivierung Wehrpflicht, Musterung, Heranziehung und Rechtsbehelfe. Norm-/Quellenanker: WPflG, Art. 12a GG, Art. 115a GG.

# Wehrpflichtgesetz: Spannungs- und Verteidigungsfall

## Fachkern: Wehrpflichtgesetz: Spannungs- und Verteidigungsfall
- **Spezialgegenstand:** Wehrpflichtgesetz: Spannungs- und Verteidigungsfall. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Im Spannungs- oder Verteidigungsfall (Art. 115a GG) lebt die allgemeine Wehrpflicht wieder auf. WPflG regelt Musterung, Einberufung und Zurückstellungsgründe.

KDV-Verfahren läuft parallel; Zurückstellungen für bestimmte Berufsgruppen und persönliche Gründe sind vorgesehen.

## Einschlägige Normen und Quellen

- Art. 12a GG — Wehrpflicht
- Art. 115a GG — Verteidigungsfall
- WPflG — Wehrpflichtgesetz
- SG §§ 60 ff. — Reservisten im Verteidigungsfall
- KDV-Verfahren

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Liegt Spannungs- oder Verteidigungsfall formal vor?
- Einberufungsbescheid erhalten?
- KDV beantragt?
- Zurückstellungsantrag (beruflich, persönlich)?
- Tauglichkeitsfeststellung?

## Prüf- und Arbeitslogik

### Schritt 1 — Wehrpflicht-Reaktivierung

Art. 12a GG i.V.m. WPflG: allgemeine Wehrpflicht für männliche Staatsbürger.
Verteidigungsfall Art. 115a GG: formeller Beschluss Bundestag und Bundesrat erforderlich.
Spannungsfall Art. 80a GG: Vorstufe.
Pflicht: ab Vollendung 18. Lebensjahr bis 45 (ggf. 60) Jahre.

### Schritt 2 — Musterung und Tauglichkeit

Musterungsbehörde: Karrierecenter der Bundeswehr.
Tauglichkeitsstufen T1–T5.
Widerspruch gegen Musterungsbescheid: 1 Monat.
Tauglichkeitsgutachten anfechten.

### Schritt 3 — Zurückstellungsgründe

§ 12 WPflG: Zurückstellung aus beruflichen und persönlichen Gründen.
Systemrelevante Berufe, Pflegepersonen.
Antrag: bei Kreiswehrersatzamt/Karrierecenter.
Zeitlich begrenzte Zurückstellung.

### Schritt 4 — KDV im Spannungsfall

KDVG: Antragsrecht auf Anerkennung als Kriegsdienstverweigerer.
Prüfungsausschuss.
Zivildienst-Äquivalent (falls reaktiviert).
Frist: rechtzeitig vor Einberufung.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Zurückstellungsgründe § 12 WPflG
- Prüfschema: Wehrpflicht-Heranziehung anfechten
- Zeitstrahl: Verteidigungsfall — rechtliche Folgen

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wpflg/ — WPflG
- https://dejure.org/gesetze/GG/12a.html
- https://dejure.org/gesetze/GG/115a.html
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle`

**Fokus:** Wehrstrafrecht Fahnenflucht Gehorsamsverweigerung Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Wehrstrafrecht – Schnittstelle Fahnenflucht und Gehorsamsverweigerung

## Fachkern: Wehrstrafrecht – Schnittstelle Fahnenflucht und Gehorsamsverweigerung
- **Spezialgegenstand:** Wehrstrafrecht – Schnittstelle Fahnenflucht und Gehorsamsverweigerung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Das Wehrstrafgesetz (WStG) ergänzt das StGB um spezifische soldatische Tatbestände: eigenmächtige Abwesenheit (§ 15), Fahnenflucht (§ 16), Selbstverstümmelung (§ 17), Dienstpflichtverletzung (§ 18), Ungehorsam (§ 19), Gehorsamsverweigerung (§ 20). Diese Delikte stehen häufig in Schnittstelle zu einem WDO-Verfahren. Der Skill ordnet ein, in welchem Verfahren der Mandant sich befindet, klärt das Verhältnis von Strafrecht und Disziplinarrecht und gibt Verteidigungsstrategien an die Hand.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welcher konkrete Vorwurf (§ 15, 16, 19, 20 WStG, sonstige Norm)?
- Stand des Strafverfahrens: Anzeige, Ermittlung, Anklage, Hauptverhandlung?
- Welche Staatsanwaltschaft (Spezialdezernate für Wehrstrafsachen)?
- Läuft parallel ein WDO-Verfahren?
- Wie lange dauerte die Abwesenheit (für § 15 vs. § 16)?
- Welche Motive (Rückkehrwille bei § 16, Gewissensnot, persönliche Notlage)?

## Rechtlicher Rahmen

- § 15 WStG: Eigenmächtige Abwesenheit – Freiheitsstrafe bis 3 Jahre, bei längerer oder Wiederholung höher.
- § 16 WStG: Fahnenflucht – Entfernung mit Absicht, sich der Verpflichtung zum Wehrdienst dauernd oder für die Zeit eines bewaffneten Einsatzes zu entziehen.
- § 17 WStG: Selbstverstümmelung zur Dienstuntauglichkeit.
- § 18 WStG: Dienstpflichtverletzung mit Folgenrisiko.
- § 19 WStG: Ungehorsam – Befehl nicht befolgt, schwere Folge eingetreten.
- § 20 WStG: Gehorsamsverweigerung – ausdrückliche Weigerung, einen Befehl zu befolgen.
- § 5 WStG: Handeln auf Befehl als Schuldausschließungsgrund (nur bei nicht erkennbarer Rechtswidrigkeit).
- § 16 WDO: Aussetzung des Disziplinarverfahrens bei parallel laufender Strafsache.
- § 50 SG: Entlassung aus dem Dienstverhältnis bei strafrechtlicher Verurteilung (Berufssoldat: Verlust der Rechte als Soldat ab 1 Jahr Freiheitsstrafe).

## / Schritt für Schritt

1. **Tatbestand sortieren.** § 15 (zeitliche Dauer, kein Entziehungswille) vs. § 16 (Entziehungsabsicht). Bei Rückkehr binnen drei Tagen vermutet die Rspr. regelmäßig keine Entziehungsabsicht.
2. **Anhörung/Vernehmung sichern.** Soldatischer Beschuldigtenstatus – Schweigerecht, Verteidigerkonsultation vor jeder Vernehmung.
3. **Akteneinsicht.** § 147 StPO – Verteidiger nimmt Einsicht; eigene Akteneinsicht durch Beschuldigten begrenzt.
4. **Parallelverfahren managen.** WDO-Verfahren beantragen ruhen zu lassen (§ 16 WDO) bis Strafverfahren abgeschlossen.
5. **Materielle Verteidigung.**
 - § 16: Bestreiten der Entziehungsabsicht.
 - § 19/20: Befehlsrechtmäßigkeit, Remonstration nachweisen, § 5 WStG prüfen.
 - § 15: Notwehr/Notstand bei familiärer/medizinischer Sondersituation.
6. **Folgenfrage.** § 50 SG-Schwelle: Bei 1 Jahr Freiheitsstrafe ohne Bewährung tritt die Entlassung kraft Gesetzes ein.
7. **Versorgungsfolgen.** Verlust von Versorgungsansprüchen bei Verurteilung (§ 38 SVG entsprechend).

## Trade-off-Matrix

| Konstellation | Strategie A | Strategie B |
| --- | --- | --- |
| Kurze Abwesenheit, Rückkehrwille | § 15 statt § 16 herausarbeiten | Geständnis und Strafmaß |
| Befehlsverweigerung mit Remonstration | § 5 WStG als Verteidigung | Disziplinar statt Strafrecht |
| Strafanzeige + WDO parallel | § 16 WDO Aussetzung | beides parallel verteidigen |
| Bewährung möglich | Auf Bewährungsmilderung hinarbeiten, § 50 SG vermeiden | Berufung |

## Praxistipps

- Schnittstelle § 11 SG (Gehorsam) und § 19/20 WStG: Wer remonstriert und den Befehl als offensichtlich strafbar erkennt, ist nach § 11 II SG zur Verweigerung verpflichtet – § 20 WStG erfüllt sich nicht.
- Bei § 16 WStG: Entziehungsabsicht ist subjektiv – Indizien wie Mitnahme persönlicher Sachen, Abmeldung, Reisepapiere relevant.
- § 5 WStG schützt nur bei nicht erkennbarer Rechtswidrigkeit; "blinder Gehorsam" ist seit den Nürnberger Prozessen kein Freibrief.
- Bei Auslandseinsatz NATO-Truppenstatut beachten – nationale Gerichtsbarkeit primär, gegebenenfalls Entsendestaatregelung.
- Wehrbeauftragten parallel einschalten (Art. 45b GG), wenn strukturelle Vorgesetztenprobleme erkennbar sind.

## Mustertexte

**Schweigeerklärung in der Vernehmung:**
"Ich mache von meinem Schweigerecht Gebrauch und werde zur Sache keine Angaben machen, bevor ich mit meinem Verteidiger gesprochen habe. Ich beantrage Akteneinsicht durch meinen Verteidiger."

**Antrag auf Aussetzung des WDO-Verfahrens:**
"Ich beantrage nach § 16 WDO die Aussetzung des Disziplinarverfahrens bis zur rechtskräftigen Entscheidung der Strafsache [Az. der StA]. Der Sachverhalt ist identisch. Eine Doppelung führt zu widersprüchlichen Beweiswürdigungen und ist nicht prozessökonomisch."

## Typische Fehler

- Geständnis in der polizeilichen Vernehmung ohne Verteidiger.
- § 16 WStG anstelle § 15 WStG aufgrund unzureichender Klarstellung des Rückkehrwillens.
- WDO-Verfahren ohne Aussetzungsantrag parallel laufen lassen – widersprüchliche Tatsachenfeststellung möglich.
- § 50 SG-Schwelle übersehen – Verurteilung von 1 Jahr Freiheitsstrafe führt zum Verlust der Rechte als Soldat kraft Gesetzes.
- Versorgungsfolgen (§ 38 SVG) im Strafmaß nicht thematisiert.

## Querverweise

- gehorsam-befehl-und-rechtswidriger-befehl
- befehl-verweigern-gewissensnot-rechtswidrigkeit
- entlassung-auf-eigenen-antrag
- gerichtliches-disziplinarverfahren-soldat
- truppendienstgericht-zustaendigkeit-verfahren
- kriegsdienstverweigerung-verfahren

## Quellen Stand 06/2026

- Wehrstrafgesetz (WStG) – Volltext gesetze-im-internet.de.
- § 50 SG, § 38 SVG – Volltext gesetze-im-internet.de.
- BGH zu § 16 WStG – ständige Rechtsprechung zur Entziehungsabsicht.
- BVerwG Wehrdienstsenate – Rechtsprechung zur § 50 SG-Schwelle.
- NATO-Truppenstatut (BGBl. II 1961 S. 1190 ff.) und Zusatzabkommen – Volltext bei BGBl-Online.
- Keine Kommentar- oder Aufsatzfundstellen aus Modellwissen.
