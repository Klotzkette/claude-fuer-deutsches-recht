---
name: versetzung-kommandierung-vorlaeufige
description: "Versetzung Kommandierung Vorlaeufige: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versetzung Kommandierung Vorlaeufige

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versetzung Kommandierung Vorlaeufige** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versetzung-kommandierung-abordnung` | Versetzung, Kommandierung, Abordnung: prüft SG §§ 22–27, Voraussetzungen, Rechtsbehelfe und Besoldungsfolgen. Norm-/Quellenanker: SG §§ 22–27, WBO, TGV. |
| `vorlaeufige-dienstenthebung-einbehaltung-bezuege` | Vorläufige Dienstenthebung und Einbehaltung Bezüge: prüft WDO §§ 126–131, Voraussetzungen, Rechtsbehelf und Vollzugsaussetzung. Norm-/Quellenanker: WDO §§ 126–131. |
| `wehrdisziplinarordnung-einfache-disziplinarmassnahme` | Wehrdisziplinarordnung einfache Disziplinarmaßnahme: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Versetzung Kommandierung Vorlaeufige**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versetzung-kommandierung-abordnung`

**Fokus:** Versetzung, Kommandierung, Abordnung: prüft SG §§ 22–27, Voraussetzungen, Rechtsbehelfe und Besoldungsfolgen. Norm-/Quellenanker: SG §§ 22–27, WBO, TGV.

# Versetzung, Kommandierung und Abordnung

## Fachkern: Versetzung, Kommandierung und Abordnung
- **Spezialgegenstand:** Versetzung, Kommandierung und Abordnung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Versetzung (§ 22 SG), Kommandierung (§ 24 SG) und Abordnung sind die häufigsten organisatorischen Maßnahmen in der Bundeswehr. Sie unterscheiden sich in Dauer, Zweck und Rechtsfolgen.

Der Soldat hat Rechtsschutz (WBO), Versetzungen müssen dienstlich notwendig sein und dürfen nicht willkürlich erfolgen.

## Einschlägige Normen und Quellen

- § 22 SG — Versetzung
- § 24 SG — Kommandierung
- § 25 SG — Abordnung (zivile Beschäftigte)
- WBO — Beschwerderecht
- TGV, BUKG — Besoldungsfolgen
- Art. 6 GG — Familienschutz

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welche Maßnahme liegt vor (Versetzung, Kommandierung, Abordnung)?
- Ist die Maßnahme dienstlich notwendig oder erscheint sie willkürlich?
- Familiäre Belange berücksichtigt?
- Frist WBO-Beschwerde noch offen?
- Besoldungs- und Umzugsfolgen?

## Prüf- und Arbeitslogik

### Schritt 1 — Versetzung § 22 SG

Dauerhafter Wechsel des Dienstortes.
Voraussetzung: dienstliches Interesse.
Personalrat (BPersVG) oder Vertrauensmann: nur für zivile Beschäftigte relevant.
Schutz Familienleben Art. 6 GG: berücksichtigen, aber kein absolutes Recht.

### Schritt 2 — Kommandierung § 24 SG

Vorübergehende Zuweisung zu anderer Einheit/Dienststelle.
Regelmäßig ohne Umzugszweck.
Trennungsgeld TGV: je nach Dauer und Entfernung.
Keine dauerhafte Statusänderung.

### Schritt 3 — Rechtsbehelfe

WBO-Beschwerde gegen Versetzungsverfügung: 1 Monat.
Vollzugsaussetzung § 9 WBO sofort beantragen (bei drohendem Umzug).
Inhalt der Beschwerde: fehlende dienstliche Notwendigkeit, Willkür, Verstoß Art. 6 GG.
Gerichtlicher Antrag TDG.

### Schritt 4 — Besoldungs- und Sozialfolgen

Versetzung → BUKG-Ansprüche (Umzugszusage einholen!).
Kommandierung → TGV (Trennungsgeld).
Beihilfe für Familie: ggf. Anpassung.
Schule der Kinder: Berücksichtigung bei Versetzungsentscheidung?

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Versetzung vs. Kommandierung vs. Abordnung
- Muster-WBO-Beschwerde gegen Versetzung
- Checkliste: Umzugszusage und BUKG bei Versetzung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — §§ 22–27 SG
- https://www.gesetze-im-internet.de/wbo/ — WBO
- https://www.gesetze-im-internet.de/tgv/ — TGV
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `vorlaeufige-dienstenthebung-einbehaltung-bezuege`

**Fokus:** Vorläufige Dienstenthebung und Einbehaltung Bezüge: prüft WDO §§ 126–131, Voraussetzungen, Rechtsbehelf und Vollzugsaussetzung. Norm-/Quellenanker: WDO §§ 126–131.

# Vorläufige Dienstenthebung und Einbehaltung von Bezügen

## Fachkern: Vorläufige Dienstenthebung und Einbehaltung von Bezügen
- **Spezialgegenstand:** Vorläufige Dienstenthebung und Einbehaltung von Bezügen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die vorläufige Dienstenthebung (§§ 126–131 WDO) ist die schwerste Sofortmaßnahme im Disziplinarrecht: der Soldat wird vom Dienst ferngehalten, bevor ein Disziplinarurteil ergeht.

Sie darf nur bei schwerwiegenden Fällen angeordnet werden und ist sofort mit WBO angreifbar. Gleichzeitig können Bezüge um bis zu 50% einbehalten werden.

## Einschlägige Normen und Quellen

- §§ 126–131 WDO — Vorläufige Dienstenthebung
- § 38 WDO — Verhältnismäßigkeit
- § 9 WBO — Vollzugsaussetzung
- BBesG § 9a — Besoldungskonsequenzen
- StPO — Paralleles Strafverfahren

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Wurde vorläufige Dienstenthebung angeordnet?
- Wurde Einbehaltung von Bezügen angeordnet?
- Was ist der zugrundeliegende Tatvorwurf?
- Ist die Anordnung verhältnismäßig?
- WBO-Beschwerde und Vollzugsaussetzung bereits eingereicht?

## Prüf- und Arbeitslogik

### Schritt 1 — Voraussetzungen §§ 126–131 WDO

Voraussetzungen: schwerwiegender Tatvorwurf, Beeinträchtigung des dienstlichen Interesses bei Verbleib.
Ermessen: Anordnung setzt Ermessensausübung voraus.
Verhältnismäßigkeit: milderes Mittel (Verwendungswechsel) prüfen!
Zuständigkeit: Einleitungsbehörde oder übergeordnete Stelle.

### Schritt 2 — Einbehaltung von Bezügen

§ 126 Abs. 2 WDO: bis zu 50% der Dienstbezüge können einbehalten werden.
Voraussetzung: hinreichende Verdachtslage, Verhältnismäßigkeit.
Versorgungsunterhalt muss sichergestellt sein.
Rückzahlung: wenn Verfahren eingestellt oder Freispruch.

### Schritt 3 — Rechtsbehelfe

WBO-Beschwerde: sofort, Frist 1 Monat.
Vollzugsaussetzung § 9 WBO: sofort und dringend!
Antrag auf Aufhebung der Dienstenthebung beim Disziplinarvorgesetzten.
Gerichtlicher Antrag TDG (§ 17a WBO analog).

### Schritt 4 — Parallelverfahren Strafrecht

Strafverfahren kann Grundlage für Dienstenthebung sein.
§ 125 WDO: Einstellung Disziplinarverfahren bis Strafverfahren abgeschlossen.
Recht auf Strafverteidiger neben WDO-Verteidiger.
Auswirkungen eines Freispruchs auf WDO-Verfahren.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Prüfschema: Vorläufige Dienstenthebung — Rechtmäßigkeit
- Checkliste: Sofortmaßnahmen nach Dienstenthebung
- Muster-Vollzugsaussetzungsantrag § 9 WBO

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wdo_2002/ — WDO §§ 126–131
- https://www.gesetze-im-internet.de/wbo/ — § 9 WBO
- https://www.bverwg.de
- https://openjur.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `wehrdisziplinarordnung-einfache-disziplinarmassnahme`

**Fokus:** Wehrdisziplinarordnung einfache Disziplinarmaßnahme: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Wehrdisziplinarordnung – Einfache Disziplinarmaßnahme

## Fachkern: Wehrdisziplinarordnung – Einfache Disziplinarmaßnahme
- **Spezialgegenstand:** Wehrdisziplinarordnung – Einfache Disziplinarmaßnahme. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Die Wehrdisziplinarordnung (WDO) unterscheidet einfache Disziplinarmaßnahmen (durch den Disziplinarvorgesetzten verhängt) und gerichtliche Disziplinarmaßnahmen (durch das Truppendienstgericht). Einfache Maßnahmen reichen von Verweis bis Disziplinararrest. Der Skill ordnet die Schwere ein, prüft formelle Voraussetzungen und führt durch Anhörung und Beschwerdeweg.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welches Dienstvergehen wird vorgeworfen (konkrete Norm aus SG)?
- Welche Maßnahme steht im Raum (Verweis, strenger Verweis, Disziplinarbuße, Ausgangsbeschränkung, Disziplinararrest)?
- Ist bereits eine Disziplinarverfügung ergangen oder droht eine Anhörung?
- Welche Dienststellung hat der Soldat (Mannschaft, Unteroffizier, Offizier)?
- Liegt parallel ein WStG-Strafverfahren oder ein gerichtliches Disziplinarverfahren vor?
- Gibt es eine Personalakte mit Vorbelastungen?

## Rechtlicher Rahmen

- § 22 WDO: Disziplinarbefugnis – der Disziplinarvorgesetzte.
- § 23 WDO: Arten einfacher Disziplinarmaßnahmen – Verweis, strenger Verweis, Disziplinarbuße, Ausgangsbeschränkung bis zu drei Wochen, Disziplinararrest bis zu drei Wochen.
- § 24 WDO: Bemessung – Schwere des Dienstvergehens, Persönlichkeit, bisheriges dienstliches und außerdienstliches Verhalten.
- § 32 WDO: Anhörungspflicht.
- § 38 WDO: Disziplinarverfügung – schriftliche Form, Begründung, Rechtsbehelfsbelehrung.
- §§ 39 ff. WDO: Beschwerde gegen die Disziplinarmaßnahme an den nächsten Disziplinarvorgesetzten.
- § 42 WDO: Antrag auf gerichtliche Entscheidung beim Truppendienstgericht.
- § 17 SG, §§ 7 ff. SG: Dienstpflichten als materielle Grundlage.

## / Schritt für Schritt

1. **Vorwurf konkretisieren.** Welche Dienstpflicht aus dem SG soll verletzt worden sein? Tatzeit, -ort, Zeugen.
2. **Anhörungstermin prüfen.** Anhörung nach § 32 WDO ist Pflicht. Recht zur schriftlichen Stellungnahme. Schweigerecht (Verbot des Selbstbezichtigungszwangs).
3. **Akteneinsicht.** Disziplinarvorgang vollständig anfordern; Beweismittel sichten.
4. **Verteidigungsstrategie.**
 - Bestreiten der Tat.
 - Bestreiten des Dienstvergehenscharakters.
 - Verfahrensfehler (fehlende Anhörung, sachlich falsche Zuständigkeit).
 - Bemessung (Verhältnismäßigkeit, Vorbelastungen, Tatschwere).
5. **Maßnahme prüfen.** § 23 WDO – formal richtige Maßnahmeart? § 24 WDO – Ermessensfehler bei Bemessung?
6. **Beschwerde.** § 39 WDO – 2 Wochen ab Zustellung der Disziplinarverfügung. Gerichtlicher Antrag § 42 WDO – 2 Wochen ab Beschwerdebescheid.
7. **Truppendienstgericht.** § 91 WDO – mündliche Verhandlung, Beweisaufnahme. Anwesenheitsrecht des Verteidigers § 90 WDO.

## Trade-off-Matrix

| Vorwurf | Schweigen | Aktive Verteidigung |
| --- | --- | --- |
| Beweisarm, Hörensagen | Schweigen, Verfahren scheitern lassen | Risiko: Vermutung der Tatbegehung |
| Beweisbar, aber Bemessung fraglich | – | Geständnis, Bemessungsfehler rügen |
| Mehrere Tatvorwürfe | Teilweises Einräumen, Kern bestreiten | Pauschal bestreiten |
| Strenger Verweis möglich | – | Disziplinarbuße als Tausch akzeptieren? |

## Praxistipps

- Anhörung nicht ohne Verteidiger und ohne Akteneinsicht durchführen. Recht auf Beistand § 90 WDO entsprechend.
- Disziplinararrest setzt richterliche Bestätigung voraus (§ 34 WDO) – dort liegt häufig ein Verfahrensfehler.
- Bei parallelem Strafverfahren: § 16 WDO Aussetzung des Disziplinarverfahrens.
- Personalakte einsehen – frühere getilgte Maßnahmen dürfen nicht mehr verwertet werden (Verwertungsverbot § 8 WDO).
- Beschwerdefrist 2 Wochen ist kürzer als die WBO-Frist – Verwechslungsgefahr.

## Mustertexte

**Schriftliche Stellungnahme zur Anhörung:**
"Sehr geehrter Herr [Dienstgrad], zur Anhörung vom [Datum] nehme ich wie folgt Stellung: Zur Sache mache ich derzeit keine Angaben (§ 32 II WDO). Ich beantrage Akteneinsicht und ergänzende Stellungnahme nach Vorlage des vollständigen Vorgangs. Hilfsweise rüge ich bereits jetzt [konkreter Verfahrensmangel]."

**Beschwerde gegen Disziplinarverfügung:**
"Gegen die Disziplinarverfügung vom [Datum], zugestellt am [Datum], lege ich Beschwerde nach § 39 WDO ein und beantrage, die Verfügung aufzuheben, hilfsweise die Maßnahme auf [...] zu reduzieren. Begründung: 1. Sachverhalt unzutreffend ermittelt. 2. Verfahrensmangel: keine ordnungsgemäße Anhörung. 3. Bemessung ermessensfehlerhaft."

## Typische Fehler

- Einlassung in der Anhörung ohne vorherige Akteneinsicht.
- Frist von 2 Wochen mit WBO-Frist 1 Monat verwechselt.
- Disziplinararrest akzeptiert, obwohl richterliche Bestätigung fehlte.
- Parallelverfahren übersehen – § 16 WDO wäre Aussetzung möglich.
- Bemessungsfehler nicht gerügt – Truppendienstgericht prüft Bemessung sonst nur eingeschränkt.

## Querverweise

- soldatengesetz-rechtsstellung-grundpflichten
- disziplinarverfahren-intake
- truppendienstgericht-zustaendigkeit-verfahren
- gerichtliches-disziplinarverfahren-soldat
- wehrstrafrecht-fahnenflucht-gehorsamsverweigerung-schnittstelle
- rechtsbeistand-im-disziplinarverfahren

## Quellen Stand 06/2026

- WDO 2025 – Volltext gesetze-im-internet.de.
- Soldatengesetz §§ 7 ff., 17 – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zur Bemessung von Disziplinarmaßnahmen (Az. verifizieren in BVerwG-Datenbank).
- Truppendienstgericht Süd/Nord – Verfahren und Spruchpraxis (publik bei den Truppendienstgerichten).
- Dienstvorschriften (ZDv) nur nach Vorlage durch Mandanten.
