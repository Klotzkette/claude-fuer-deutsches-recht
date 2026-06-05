---
name: bwbes-besoldung-reservist-kdv
description: "Bwbes Besoldung Reservist KDV: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bwbes Besoldung Reservist KDV

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bwbes Besoldung Reservist KDV** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bwbes-neu-009-besoldung-reservist-wehruebung-und-arbeitgeberausg` | Besoldung Reservisten, Wehrübung, Arbeitgeberausgleich: prüft ArbPlSchG, UhSiG, Freistellungspflicht und Kündigungsschutz. Norm-/Quellenanker: ArbPlSchG, UhSiG, WSG. |
| `bwbes-neu-011-kdv-und-besoldungsfolgen-bei-statuswechsel` | KDV und Besoldungsfolgen Statuswechsel: prüft Art. 4 Abs. 3 GG, KDVG, Entlassungsrecht und Ausbildungskostenrückforderung. Norm-/Quellenanker: KDVG, SG §§ 46 und 56, Art. 4 GG. |
| `bwbes-neu-012-disziplinarbusse-kuerzung-und-besoldung` | Disziplinarbuße, Gehaltskürzung, Besoldungsfolgen: prüft WDO §§ 22–30, Bemessung, Vollstreckung und Rechtsbehelfe. Norm-/Quellenanker: WDO, BBesG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Bwbes Besoldung Reservist KDV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bwbes-neu-009-besoldung-reservist-wehruebung-und-arbeitgeberausg`

**Fokus:** Besoldung Reservisten, Wehrübung, Arbeitgeberausgleich: prüft ArbPlSchG, UhSiG, Freistellungspflicht und Kündigungsschutz. Norm-/Quellenanker: ArbPlSchG, UhSiG, WSG.

# Besoldung Reservist: Wehrübung und Arbeitgeberausgleich

## Fachkern: Besoldung Reservist: Wehrübung und Arbeitgeberausgleich
- **Spezialgegenstand:** Besoldung Reservist: Wehrübung und Arbeitgeberausgleich. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Reservisten haben während Wehrübung Anspruch auf Wehrsold (WSG) und Unterhaltssicherung (UhSiG). Ihr Arbeitgeber ist zur Freistellung verpflichtet (ArbPlSchG) und darf nicht kündigen (§ 4 ArbPlSchG).

Kleine Arbeitgeber können Erstattung beantragen. Benachteiligungen am Arbeitsplatz wegen Reservedienst sind unzulässig.

## Einschlägige Normen und Quellen

- ArbPlSchG — Arbeitsplatzschutzgesetz
- UhSiG — Unterhaltssicherungsgesetz
- WSG — Wehrsoldgesetz
- § 4 ArbPlSchG — Kündigungsverbot
- AGG — Diskriminierungsverbot

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Freiwillige Wehrübung, Bündnisfall oder Spannungsfall-Heranziehung?
- Arbeitgeber Freistellung verweigert oder gekündigt?
- Unterhaltssicherung beansprucht?
- Selbstständiger oder Arbeitnehmer?
- Nachteile am Arbeitsplatz wegen Reservistentätigkeit?

## Prüf- und Arbeitslogik

### Schritt 1 — Freistellungspflicht ArbPlSchG

§ 1 ArbPlSchG: Freistellung für Dauer der Wehrübung.
Entgelt ruht (nicht verloren).
§ 4 ArbPlSchG: Kündigungsverbot ab Zustellung Einberufungsbescheid bis 2 Wochen danach.
Ausnahme dringendes betriebliches Bedürfnis: sehr eng.

### Schritt 2 — Unterhaltssicherung UhSiG

Arbeitnehmer und Selbstständige.
Höhe: Nettoverdienst abzüglich Wehrsold.
Selbstständige: Einkommensnachweise 3 Jahre.
Antrag: Karrierecenter/BAPersBw.

### Schritt 3 — Diskriminierungsverbot und Mobbing

ArbPlSchG Spezialregelung.
Mobbingschutz: § 12 AGG + allgemeines Schikaneverbot.
Kündigungsschutzklage bei unzulässiger Kündigung: ArbG, 3-Wochen-Frist.

### Schritt 4 — Arbeitgebererstattung

ArbPlSchG §§ 13–14: kleine Betriebe können Erstattung beantragen.
Antrag nach Ende Wehrübung.
Fristen einhalten.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Muster-Freistellungsschreiben für Arbeitgeber
- Checkliste: Unterlagen UhSiG-Antrag
- Tabelle: Rechte/Pflichten Arbeitgeber bei Wehrübung des Arbeitnehmers

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/arb-plschg/ — ArbPlSchG
- https://www.gesetze-im-internet.de/uhsig/ — UhSiG
- https://www.gesetze-im-internet.de/wsg/ — WSG
- https://www.bundeswehr.de/de/soldat-werden/reservisten

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `bwbes-neu-011-kdv-und-besoldungsfolgen-bei-statuswechsel`

**Fokus:** KDV und Besoldungsfolgen Statuswechsel: prüft Art. 4 Abs. 3 GG, KDVG, Entlassungsrecht und Ausbildungskostenrückforderung. Norm-/Quellenanker: KDVG, SG §§ 46 und 56, Art. 4 GG.

# KDV und Besoldungsfolgen bei Statuswechsel

## Fachkern: KDV und Besoldungsfolgen bei Statuswechsel
- **Spezialgegenstand:** KDV und Besoldungsfolgen bei Statuswechsel. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

KDV nach Art. 4 Abs. 3 GG ist für Wehrpflichtige im Spannungs-/Verteidigungsfall relevant. Für aktive Berufssoldaten ist der Weg zur Entlassung wegen Gewissenskonflikts (Art. 4 Abs. 1 GG) enger.

BVerwG: Entlassung wegen echten Gewissenskonflikts möglich, aber Ausbildungskostenrückforderung bleibt trotzdem möglich (§ 56 SG), da die Entlassung auf eigenen Antrag erfolgt.

## Einschlägige Normen und Quellen

- Art. 4 Abs. 3 GG — Kriegsdienstverweigerung
- KDVG — Kriegsdienstverweigerungsgesetz
- SG §§ 46, 58 — Entlassung auf eigenen Antrag
- § 56 SG — Rückforderung Ausbildungskosten
- Art. 4 Abs. 1 GG — Gewissensfreiheit

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- KDV beantragt oder Entlassungsantrag gestellt?
- Liegt echter Gewissenskonflikt vor?
- Droht Ausbildungskostenrückforderung?
- Spannungsfall-Wehrpflicht oder aktiver Dienst?
- Statuswechsel geplant (z. B. SaZ → FWD → Ausscheiden)?

## Prüf- und Arbeitslogik

### Schritt 1 — KDV-Recht im Grundsatz

Art. 4 Abs. 3 GG: Niemand darf gegen Gewissen zum Kriegsdienst mit Waffe gezwungen werden.
KDVG: Prüfungsausschuss-Verfahren für Wehrpflichtige im Spannungsfall.
Berufssoldat: kein KDVG-Antrag, sondern Entlassung nach SG.

### Schritt 2 — Entlassung wegen Gewissenskonflikt

§ 46 SG: Entlassung auf eigenen Antrag.
Art. 4 Abs. 1 GG kann Entlassungsanspruch begründen (BVerwG).
Kosten: § 56 SG-Rückforderung trotzdem möglich.
Verhältnismäßigkeitsprüfung und Härteerlass beantragen.

### Schritt 3 — Besoldungsfolgen bei Statuswechsel

Entlassung auf eigenen Antrag: Ansprüche enden mit Entlassungsdatum.
Übergangsgebührnisse SVG: wenn Dienstzeit erreicht.
Rückforderung Ausbildungskosten: lineare Staffelung nach geleisteter Dienstzeit.
Billigkeitserlass bei wirtschaftlicher Härte.

### Schritt 4 — Verfahren

Schriftlicher Entlassungsantrag.
Anhörung durch Dienstherrn.
WBO-Beschwerde bei Ablehnung.
Klage VG (dienstrechtliche Entscheidung).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Prüfschema: Gewissenskonflikt-Entlassung Berufssoldat
- Checkliste: Entlassungsantrag — notwendige Unterlagen
- Tabelle: Kostenfolgen nach Dienstzeitlänge § 56 SG

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/kdvg/ — KDVG
- https://www.gesetze-im-internet.de/sg/ — SG §§ 46, 56
- https://www.bverfg.de — Art. 4 GG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `bwbes-neu-012-disziplinarbusse-kuerzung-und-besoldung`

**Fokus:** Disziplinarbuße, Gehaltskürzung, Besoldungsfolgen: prüft WDO §§ 22–30, Bemessung, Vollstreckung und Rechtsbehelfe. Norm-/Quellenanker: WDO, BBesG.

# Disziplinarbuße, Gehaltskürzung und Besoldung

## Fachkern: Disziplinarbuße, Gehaltskürzung und Besoldung
- **Spezialgegenstand:** Disziplinarbuße, Gehaltskürzung und Besoldung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Einfache Disziplinarmaßnahmen: Verweis, strenger Verweis, Disziplinarbuße (bis 1 Monatsgehalt), Kürzung der Dienstbezüge (bis 1/5 für max. 3 Jahre), Beförderungsverbot.

Verhältnismäßigkeit ist zentrales Prüfkriterium. BVerwG-Rechtsprechung ist sehr kasuistisch.

## Einschlägige Normen und Quellen

- §§ 22–30 WDO — Einfache Disziplinarmaßnahmen
- § 28 WDO — Disziplinarbuße
- § 29 WDO — Kürzung der Dienstbezüge
- § 30 WDO — Beförderungsverbot
- § 38 WDO — Bemessungsgrundsätze
- BBesG — Besoldung bei Disziplinarmaßnahmen

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welche Disziplinarmaßnahme wurde verhängt?
- Wer hat sie erlassen (Disziplinarvorgesetzter)?
- Ist sie verhältnismäßig zur Pflichtverletzung?
- WBO-Beschwerdefrist versäumt?
- Vollzugsaussetzung beantragt?

## Prüf- und Arbeitslogik

### Schritt 1 — Arten einfacher Disziplinarmaßnahmen

Verweis: mildeste Form, keine Besoldungsfolgen.
Strenger Verweis: schärfer, aber ebenfalls keine Geldfolge.
Disziplinarbuße § 28 WDO: bis 1 Monatsgehalt.
Kürzung § 29 WDO: bis 1/5 Bezüge für 1–3 Jahre.

### Schritt 2 — Bemessung § 38 WDO

Schwere der Pflichtverletzung, Schuld, Persönlichkeit, Vorstrafen.
Verhältnismäßigkeit: Maßnahme muss zur Schwere passen.
Berücksichtigung: Vorstrafenfreiheit, dienstliche Leistungen.
BVerwG: enge Verhältnismäßigkeitsprüfung bei Kürzung.

### Schritt 3 — Vollstreckung und Besoldungsfolgen

Disziplinarbuße: Abzug vom Gehalt.
Kürzung: monatliche Absenkung für Kürzungszeitraum.
Beförderungsverbot: für bestimmten Zeitraum.
Eintragung in Personalakte.

### Schritt 4 — Rechtsbehelfe WBO

WBO-Beschwerde gegen einfache Maßnahme als dienstliche Maßnahme.
Frist: 1 Monat.
Vollzugsaussetzung § 9 WBO beantragen.
Gerichtlicher Antrag § 17 WBO beim TDG.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Einfache Disziplinarmaßnahmen und Besoldungsfolgen
- Prüfschema: Verhältnismäßigkeit Disziplinarbuße
- Muster-WBO-Beschwerde gegen Disziplinarmaßnahme

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wdo_2002/ — WDO
- https://dejure.org/gesetze/WDO
- https://www.bverwg.de — BVerwG Wehrdienstsenat

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
