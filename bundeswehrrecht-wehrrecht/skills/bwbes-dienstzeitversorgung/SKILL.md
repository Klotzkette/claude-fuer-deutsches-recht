---
name: bwbes-dienstzeitversorgung
description: "Bwbes Dienstzeitversorgung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bwbes Dienstzeitversorgung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bwbes Dienstzeitversorgung** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bwbes-neu-006-dienstzeitversorgung-berufsfoerderungsdienst` | Dienstzeitversorgung und BFD: prüft SVG §§ 1–26, Übergangsgebührnisse, Übergangsbeihilfe, BFD-Ansprüche und Rentenrecht. Norm-/Quellenanker: SVG, BFD-Richtlinien. |
| `bwbes-neu-007-soldatenversorgung-dienstunfall-wehrdienstbeschaed` | Dienstunfall und WDB: prüft § 27 SVG, Kausalitätsmaßstab, Leistungsarten und Verfahren. Norm-/Quellenanker: SVG §§ 27–38, SGB XIV. |
| `bwbes-neu-008-heilfuersorge-truppenaerztliche-versorgung-und-pkv` | Heilfürsorge, truppenärztliche Versorgung, PKV: prüft § 70 BBesG, Leistungsumfang, PKV-Übergang und SVG-Heilbehandlung. Norm-/Quellenanker: BBesG § 70, SVG §§ 69–74, BBhV. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Bwbes Dienstzeitversorgung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bwbes-neu-006-dienstzeitversorgung-berufsfoerderungsdienst`

**Fokus:** Dienstzeitversorgung und BFD: prüft SVG §§ 1–26, Übergangsgebührnisse, Übergangsbeihilfe, BFD-Ansprüche und Rentenrecht. Norm-/Quellenanker: SVG, BFD-Richtlinien.

# Dienstzeitversorgung und Berufsförderungsdienst

## Fachkern: Dienstzeitversorgung und Berufsförderungsdienst
- **Spezialgegenstand:** Dienstzeitversorgung und Berufsförderungsdienst. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Soldaten auf Zeit erhalten nach Entlassung Übergangsgebührnisse (§ 5 SVG) und haben Anspruch auf Berufsförderung (BFD). Berufssoldaten erhalten ab bestimmten Dienstzeiten Ruhegehalt (§§ 13 ff. SVG).

Die Verzahnung mit GRV und Versorgungsausgleich bei Scheidung ist komplex.

## Einschlägige Normen und Quellen

- §§ 1–26 SVG — Dienstzeitversorgung
- § 5 SVG — Übergangsgebührnisse (SaZ)
- § 9 SVG — Übergangsbeihilfe
- §§ 39–48 SVG — Berufsförderungsdienst
- § 26a SVG — Erhöhung bei WDB
- SGB VI — Rentenrecht (Schnittstelle)

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- SaZ oder Berufssoldat? Wie lange Dienstzeit?
- Wann endet/endete das Dienstverhältnis?
- Übergangsgebührnisse beantragt?
- BFD in Anspruch genommen?
- Streit über Dauer, Höhe oder Anrechnung?
- Wehrdienstbeschädigung (WDB-Zuschlag)?

## Prüf- und Arbeitslogik

### Schritt 1 — Übergangsgebührnisse § 5 SVG

Anspruch: SaZ nach mind. 4-jähriger Dienstzeit.
Dauer: 1–5 Jahre abhängig von Dienstzeit.
Höhe: 75% letztes Grundgehalt.
Wegfall/Anrechnung bei Erwerbstätigkeit § 5 Abs. 6 SVG.

### Schritt 2 — Übergangsbeihilfe § 9 SVG

Einmalzahlung bei Entlassung nach mind. 4 Jahren.
Höhe gestaffelt nach Dienstjahren.
Nicht voll kumulierbar mit Übergangsgebührnissen.

### Schritt 3 — Berufsförderungsdienst §§ 39–48 SVG

Anspruch ab 4 Jahren SaZ.
Leistungen: Schulbildung, Berufsausbildung, Studium, Umschulung.
Fristen: Antrag innerhalb bestimmter Frist nach Entlassung.
BFD-Fördermittel, Unterhaltsbeihilfe.

### Schritt 4 — Rentenrecht und Versorgungsausgleich

SaZ: Pflichtbeitragszeiten GRV (§ 3 SGB VI).
BeruSold: kein paralleler GRV-Anspruch (§ 55 SVG).
Versorgungsausgleich Scheidung: militärische Versorgung fließt ein.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Übergangsgebührnisse nach Dienstzeit (Dauer und Höhe)
- Checkliste: Unterlagen BFD-Antrag
- Prüfschema: Pensionsanspruch Berufssoldat § 13 SVG

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/svg/ — SVG
- https://dejure.org/gesetze/SVG
- https://www.bundeswehr.de/de/organisation/personal
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `bwbes-neu-007-soldatenversorgung-dienstunfall-wehrdienstbeschaed`

**Fokus:** Dienstunfall und WDB: prüft § 27 SVG, Kausalitätsmaßstab, Leistungsarten und Verfahren. Norm-/Quellenanker: SVG §§ 27–38, SGB XIV.

# Soldatenversorgung: Dienstunfall und Wehrdienstbeschädigung

## Fachkern: Soldatenversorgung: Dienstunfall und Wehrdienstbeschädigung
- **Spezialgegenstand:** Soldatenversorgung: Dienstunfall und Wehrdienstbeschädigung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Eine WDB liegt vor, wenn ein Soldat durch wehrdienstliche Verrichtung einen Körperschaden erleidet (§ 27 SVG). Kausalitätsmaßstab: 'hinreichende Wahrscheinlichkeit' (> 50%). Bei Auslandseinsätzen: erleichterte Kausalitätsvermutung.

Das Verfahren ist komplex: BAPersBw, Versorgungsämter, ggf. Sozialgerichte.

## Einschlägige Normen und Quellen

- § 27 SVG — Wehrdienstbeschädigung
- §§ 30–38 SVG — Versorgungsleistungen
- §§ 63a–63h SVG — Einsatzversorgung
- SGB XIV — Soziales Entschädigungsrecht (ab 2024)
- OEG — Opferentschädigungsgesetz (Abgrenzung)

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was ist der Schaden (körperlich, psychisch, PTBS)?
- Wie und wann entstanden (Unfall, schleichend, Einsatz)?
- Besteht Zusammenhang mit Wehrdienst?
- Welche Leistungen beansprucht (Ausgleich, Rente, Heilbehandlung)?
- WDB bereits anerkannt oder streitig?
- Gutachterlicher Streit über Kausalität?

## Prüf- und Arbeitslogik

### Schritt 1 — Tatbestand WDB § 27 SVG

Schädigungsfolge: körperliche, seelische oder geistige Gesundheitsstörung.
Wehrdienstliche Verrichtung: Ausübung des Wehrdienstes oder damit zusammenhängende Tätigkeit.
Kausalität: 'hinreichende Wahrscheinlichkeit'.
Ausschluss: vorsätzliche Selbstschädigung.

### Schritt 2 — Kausalitätsprüfung

Vollbeweis für Schaden; Wahrscheinlichkeitsbeweis für Kausalität.
Gutachten: BwKrhs, externer Gutachter.
Gegengutachten bei Ablehnung beauftragen.
Vorerkrankungen: Mitverursachung ausreichend (§ 27 Abs. 3 SVG).

### Schritt 3 — Leistungsarten SVG

§ 85 SVG: Ausgleich/Rente nach MdE.
Grundrente §§ 30 ff. SVG analog BVG.
Heilbehandlung kostenlos.
Pflegezulage, Schwerstbeschädigtenzulage bei hohem GdS.

### Schritt 4 — Verfahren und Rechtsbehelfe

Antrag: BAPersBw Versorgungsreferat.
Gutachtenverfahren, Recht auf Gegengutachten.
Widerspruch 1 Monat.
Klage: Sozialgericht (seit SGB XIV 2024 prüfen).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Prüfschema: WDB § 27 SVG (Schaden → Tätigkeit → Kausalität)
- Checkliste: Unterlagen WDB-Antrag
- Tabelle: Leistungsarten nach SVG und MdE-Graden

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/svg/ — SVG §§ 27–38
- https://www.gesetze-im-internet.de/sgb_xiv/ — SGB XIV
- https://www.bverwg.de
- https://www.bundessozialgericht.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `bwbes-neu-008-heilfuersorge-truppenaerztliche-versorgung-und-pkv`

**Fokus:** Heilfürsorge, truppenärztliche Versorgung, PKV: prüft § 70 BBesG, Leistungsumfang, PKV-Übergang und SVG-Heilbehandlung. Norm-/Quellenanker: BBesG § 70, SVG §§ 69–74, BBhV.

# Heilfürsorge, truppenärztliche Versorgung und PKV

## Fachkern: Heilfürsorge, truppenärztliche Versorgung und PKV
- **Spezialgegenstand:** Heilfürsorge, truppenärztliche Versorgung und PKV. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Aktive Soldaten haben Anspruch auf unentgeltliche Heilfürsorge (§ 70 BBesG). Nach Entlassung endet die Heilfürsorge sofort; PKV-Pflicht entsteht.

Probleme entstehen bei PKV-Aufnahme nach langer Dienstzeit (Vorerkrankungen, Wartezeiten) und bei WDB-Heilbehandlungsansprüchen nach Entlassung.

## Einschlägige Normen und Quellen

- BBesG § 70 — Heilfürsorge aktive Soldaten
- SVG §§ 69–74 — Heilbehandlung bei WDB
- BBhV — Bundesbeihilfeverordnung (nach Entlassung)
- SG § 30 — Fürsorge- und Treuepflicht
- GOÄ/GOZ — Gebührenordnungen

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Aktiver Soldat (Heilfürsorge) oder entlassen (PKV/Beihilfe)?
- Welche Leistung abgelehnt oder unzureichend erstattet?
- Streit über Wahlleistungen (Chefarzt, Einzelzimmer)?
- Einsatzbedingte Erkrankung → SVG-Heilbehandlung?
- PKV-Aufnahme nach Entlassung gescheitert?

## Prüf- und Arbeitslogik

### Schritt 1 — Heilfürsorge aktive Soldaten § 70 BBesG

Umfang: ärztliche/zahnärztliche Behandlung, Arzneimittel, Krankenhaus, Heilmittel.
Behandlung über Sanitätszentren/BwKrhs oder Vertragsärzte.
Wahlleistungen: gesondert beantragen, Zuzahlung möglich.
Keine Erstattung ohne vorherige Genehmigung bei Privatärzten.

### Schritt 2 — Entlassung und PKV-Übergang

Heilfürsorge endet mit Entlassung sofort.
PKV-Kontrahierungszwang: bei langer Dienstzeit Öffnungsklausel.
Beihilfe: nach Entlassung BBhV analog.
Übergangsbeihilfe SVG: keine Kostenfortsetzung für PKV.

### Schritt 3 — SVG-Heilbehandlung § 69 SVG

Einsatzbedingte Erkrankungen: Heilbehandlung auf Bundeskosten.
Keine zeitliche Begrenzung für anerkannte WDB-Folgen.
Antrag: BAPersBw Versorgungsreferat.

### Schritt 4 — Rechtsbehelfe

Ablehnung Heilfürsorge-Leistung: WBO-Beschwerde + ggf. VG.
PKV-Streit: Zivilgericht.
SVG-Heilbehandlung abgelehnt: Widerspruch + Sozialgericht.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Checkliste: Heilfürsorge-Genehmigung Wahlleistung
- Tabelle: Heilfürsorge vs. Beihilfe vs. SVG-Heilbehandlung
- Merkblatt: PKV-Übergang nach Entlassung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bbesg/ — § 70 BBesG
- https://www.gesetze-im-internet.de/svg/ — §§ 69–74 SVG
- https://www.gesetze-im-internet.de/bbhv/ — BBhV
- https://www.bundeswehr.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
