---
name: nebentaetigkeit-geschenkannahme-personalakte
description: "Nebentaetigkeit Geschenkannahme Personalakte: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nebentaetigkeit Geschenkannahme Personalakte

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Nebentaetigkeit Geschenkannahme Personalakte** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nebentaetigkeit-geschenkannahme-compliance` | Nebentätigkeit Geschenkannahme Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG. |
| `personalakte-einsicht-datenschutz` | Personalakte, Einsicht, Datenschutz: prüft § 17 SG, Aufnahmerecht, Löschungsansprüche und DSGVO-Rechte. Norm-/Quellenanker: § 17 SG, DSGVO, BDSG. |
| `personalvertretung-zivile-beschaeftigte-schnittstelle` | Personalvertretung zivile Beschäftigte Schnittstelle: prüft BPersVG-Mitbestimmung, Abgrenzung zu Soldatenbeteiligung, SBG und Verfahren. Norm-/Quellenanker: BPersVG, SBG, BetrVG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Nebentaetigkeit Geschenkannahme Personalakte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nebentaetigkeit-geschenkannahme-compliance`

**Fokus:** Nebentätigkeit Geschenkannahme Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung 2025, Wehrpflichtgesetz, Soldatenversorgungsgesetz, Soldatenbeteiligungsgesetz, SÜG.

# Nebentätigkeit und Geschenkannahme – Compliance des Soldaten

## Fachkern: Nebentätigkeit und Geschenkannahme – Compliance des Soldaten
- **Spezialgegenstand:** Nebentätigkeit und Geschenkannahme – Compliance des Soldaten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Soldaten dürfen Nebentätigkeiten nur eingeschränkt und nur nach vorheriger Genehmigung ausüben (§ 20 SG). Die Annahme von Belohnungen, Geschenken und sonstigen Vorteilen ist nach § 19 SG grundsätzlich verboten. Der Skill ordnet die Genehmigungspflichten, prüft Versagungsgründe, dokumentiert Compliance-Verstöße und schützt vor strafrechtlichen Konsequenzen (§§ 331 ff. StGB Vorteilsannahme/Bestechlichkeit).

## Wann dieses Modul hilft / Kaltstart-Fragen

- Welche Tätigkeit (selbständig, abhängig, ehrenamtlich)?
- Art der Vergütung, Zeitumfang, dienstlicher Zusammenhang?
- Geschenk: von wem, Anlass, Wert?
- Bereits Genehmigung erteilt oder versagt?
- Verfahren eingeleitet (Anhörung, Strafanzeige § 331 ff. StGB)?
- Funktion des Soldaten (Beschaffung, Auftragsvergabe, militärischer Dienst)?

## Rechtlicher Rahmen

- § 19 SG: Verbot der Annahme von Belohnungen, Geschenken und sonstigen Vorteilen in Bezug auf das Amt – Zustimmung der obersten Dienstbehörde erforderlich.
- § 20 SG: Nebentätigkeiten – Genehmigungspflicht; Versagungsgründe.
- § 21 SG: Anzeigepflichtige Nebentätigkeiten.
- § 21a SG: Nebentätigkeit nach Beendigung des Dienstverhältnisses (Karenzzeit).
- §§ 331–337 StGB: Vorteilsannahme und Bestechlichkeit von Amtsträgern.
- Vergaberecht: Schnittstelle BAAINBw / Beschaffung.
- ZDv A-2614/1 (Nebentätigkeit) – nur nach Vorlage.
- BHO-Geschenkrichtlinien.

## / Schritt für Schritt

1. **Tätigkeit oder Geschenk klassifizieren.** Selbständig, Anstellung, Ehrenamt, einmalige Aufmerksamkeit, regelmäßige Zuwendung?
2. **Genehmigungsbedarf prüfen.** Pflicht-Anzeige oder Pflicht-Genehmigung?
3. **Versagungsgründe nach § 20 SG prüfen:**
 - Wesentliche Beeinträchtigung dienstlicher Pflichten,
 - Konkurrenz zum Dienstherrn,
 - Beeinträchtigung der Unparteilichkeit,
 - Sittenwidrigkeit.
4. **Schriftlicher Antrag** mit Tätigkeitsbeschreibung, Zeitaufwand, Vergütung, Auftraggeber.
5. **Geschenkannahme:** Sofortmeldung an Vorgesetzten, Schriftliche Anzeige, ggf. Rückgabe oder Hinterlegung.
6. **Compliance-Folgen.** Strafanzeige (§ 331/332 StGB), WDO-Verfahren parallel.
7. **Karenzzeit nach Dienstende** (§ 21a SG) für Beschaffungs- und Führungspositionen.

## Trade-off-Matrix

| Situation | Vorgehen |
| --- | --- |
| Bagatelle (Kaffee, Werbeartikel) | Anzeige, ggf. nicht genehmigungspflichtig |
| Einladung Industrievertreter | Schriftliche Genehmigung; alternativ Ablehnung |
| Tätigkeit als Reservist-Berater | Genehmigung mit Auflagen |
| Politisches Mandat | § 36 SG (Wahlrecht) – Sonderregelung |
| Nach Pension Beschaffung-Beratungsfirma | § 21a SG-Karenzzeit prüfen |

## Praxistipps

- Geschenkrückgabe innerhalb von 24 Stunden plus schriftliche Meldung – schützt vor § 331 StGB.
- Geringfügigkeitsgrenze nicht justiziabel im Sinne von "geringer Schaden" – Compliance-Regel: bei Zweifel anzeigen.
- Bei Beschaffungspositionen besondere Aufmerksamkeit – Vermutungsregel der Befangenheit.
- Vortrag bei Industriekonferenz nur mit Genehmigung; Honorar in Bundeskasse oder mit Auflagen.
- Karenzzeit nach Dienstende kann 5 Jahre erreichen (Schnittstelle § 105 BBG entsprechend).

## Mustertexte

**Genehmigungsantrag Nebentätigkeit:**
"Ich beantrage Genehmigung folgender Nebentätigkeit: 1. Art: [...]. 2. Auftraggeber: [...]. 3. Zeitaufwand: [...] Std/Monat. 4. Vergütung: [...] EUR. 5. Dienstlicher Bezug: keiner / [Erklärung]. 6. Beeinträchtigung dienstlicher Aufgaben: ausgeschlossen, weil [...]. Es wird zugesichert, dass Versagungsgründe nach § 20 III SG nicht vorliegen."

**Geschenkanzeige:**
"Hiermit zeige ich an, dass mir am [Datum] von [Person/Firma] anlässlich [...] ein [Gegenstand/Geldwert] im geschätzten Wert von [...] EUR angeboten wurde. Ich habe die Annahme [abgelehnt / vorbehaltlich der Genehmigung entgegengenommen]. Ich beantrage Entscheidung nach § 19 SG."

## Typische Fehler

- "Kleine Aufmerksamkeit" formlos angenommen – § 331 StGB-Risiko.
- Nebentätigkeit ohne Antrag aufgenommen – Disziplinarmaßnahme.
- Karenzzeit nach Dienstende ignoriert – Versorgungseingriff möglich.
- Industriekonferenz-Honorar versteckt – Compliance-Verstoß.
- Vermengung von zulässiger ehrenamtlicher Tätigkeit mit anzeigepflichtiger Nebentätigkeit.

## Querverweise

- soldatengesetz-rechtsstellung-grundpflichten
- pflicht-zum-treuen-dienen-7-sg
- extremismus-verdachtsfall-sicherheitsrecht
- entlassung-auf-eigenen-antrag
- besoldung-zulagen-auslandsverwendungszuschlag
- mandantenbrief-soldat-verstaendlich

## Quellen Stand 06/2026

- §§ 19, 20, 21, 21a SG – Volltext gesetze-im-internet.de.
- §§ 331–337 StGB – Volltext gesetze-im-internet.de.
- BVerwG Wehrdienstsenate – ständige Rechtsprechung zu § 20 SG.
- BGH-Rechtsprechung zur Amtsträgereigenschaft des Soldaten – ständige Rechtsprechung.
- ZDv A-2614/1 (Nebentätigkeit) – nur nach Vorlage durch Mandanten.

## 2. `personalakte-einsicht-datenschutz`

**Fokus:** Personalakte, Einsicht, Datenschutz: prüft § 17 SG, Aufnahmerecht, Löschungsansprüche und DSGVO-Rechte. Norm-/Quellenanker: § 17 SG, DSGVO, BDSG.

# Personalakte, Einsicht und Datenschutz

## Fachkern: Personalakte, Einsicht und Datenschutz
- **Spezialgegenstand:** Personalakte, Einsicht und Datenschutz. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

§ 17 SG regelt das Personalaktenrecht für Soldaten. Die Personalakte enthält alle für das Dienstverhältnis relevanten Unterlagen. Der Soldat hat das Recht auf vollständige Einsicht und kann unrichtige Eintragungen berichtigen lassen.

DSGVO-Rechte (Art. 15, 17) gelten ergänzend für personenbezogene Daten in der Akte.

## Einschlägige Normen und Quellen

- § 17 SG — Personalaktenrecht Soldaten
- § 29 SG — Aufnahme in Personalakte (Pflichten)
- DSGVO Art. 15–17 — Auskunft, Berichtigung, Löschung
- BDSG § 26 — Beschäftigtendatenschutz
- SÜG § 25 — Sicherheitsakte

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was soll eingesehen werden (vollständige Akte, bestimmte Unterlagen)?
- Wurde ein bestimmter Eintrag als unrichtig erkannt?
- Soll ein Eintrag gelöscht werden (z. B. nach Verjährung)?
- Besteht Streit über Inhalt der Personalakte?
- Sicherheitsakte separates Problem?

## Prüf- und Arbeitslogik

### Schritt 1 — Akteneinsicht § 17 SG

Recht auf vollständige Einsicht in eigene Personalakte.
Antrag: beim Personalführenden (BAPersBw).
Schriftlich, Empfangsbestätigung verlangen.
Umfang: alle Unterlagen — auch Beurteilungen, Verwarnungen, Disziplinarvorgänge.

### Schritt 2 — Aufnahmerecht und Gegendarstellung

§ 17 Abs. 4 SG: Soldat kann zu Einträgen schriftliche Stellungnahme einreichen.
Stellungnahme wird Bestandteil der Akte.
Berichtigung unrichtiger Tatsachen: Antrag auf Berichtigung.
Löschung veralteter Eintragungen nach Verjährung.

### Schritt 3 — DSGVO-Rechte

Art. 15 DSGVO: Auskunft über alle gespeicherten personenbezogenen Daten.
Art. 16 DSGVO: Berichtigungsanspruch.
Art. 17 DSGVO: Löschung (eingeschränkt im Beschäftigungsverhältnis).
Beschwerde: BfDI oder Datenschutzbeauftragter Bundeswehr.

### Schritt 4 — Sonderfall Sicherheitsakte

§ 25 SÜG: Sicherheitsakte ist von Personalakte getrennt; eigene Einsichtsregeln.
Auskunft über SÜG-Daten eingeschränkt.
BfDI-Beschwerde möglich.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Muster-Akteneinsichtsantrag § 17 SG
- Checkliste: Berichtigungs- und Löschungsanträge
- Tabelle: Personalakte vs. Sicherheitsakte

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — § 17 SG
- https://www.gesetze-im-internet.de/bdsg_2018/ — BDSG
- https://www.bfdi.bund.de
- https://dejure.org/gesetze/DSGVO/15.html

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `personalvertretung-zivile-beschaeftigte-schnittstelle`

**Fokus:** Personalvertretung zivile Beschäftigte Schnittstelle: prüft BPersVG-Mitbestimmung, Abgrenzung zu Soldatenbeteiligung, SBG und Verfahren. Norm-/Quellenanker: BPersVG, SBG, BetrVG.

# Personalvertretung zivile Beschäftigte — Schnittstelle

## Fachkern: Personalvertretung zivile Beschäftigte — Schnittstelle
- **Spezialgegenstand:** Personalvertretung zivile Beschäftigte — Schnittstelle. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Für zivile Beschäftigte gilt BPersVG (Personalrat), für Soldaten gilt SBG (Vertrauensmann). BetrVG ist für Bundesbehörden nicht anwendbar. Diese Abgrenzung ist praktisch wichtig.

Gemischte Dienststellen (Soldaten + Zivilpersonal) haben beide Gremien nebeneinander.

## Einschlägige Normen und Quellen

- BPersVG — Bundespersonalvertretungsgesetz
- SBG — Soldatenbeteiligungsgesetz
- § 75–79 BPersVG — Mitbestimmungsrechte
- §§ 36–37 SBG — Vertrauensmann Soldaten
- BetrVG (Abgrenzung) — nicht anwendbar auf Bundesbehörden

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Ist die Person Soldat oder ziviler Beschäftigter?
- Geht es um Mitbestimmung bei einer konkreten Personalmaßnahme?
- Hat der Personalrat zugestimmt oder Einwände erhoben?
- Gibt es Streit über Zuständigkeit (Personalrat vs. Vertrauensmann)?

## Prüf- und Arbeitslogik

### Schritt 1 — Personalrat BPersVG — Zuständigkeit und Mitbestimmung

§§ 75–79 BPersVG: Mitbestimmung bei Einstellung, Kündigung, Versetzung, Eingruppierung.
Frist: Personalrat hat 10 Arbeitstage.
Zustimmungsverweigerung: nur aus gesetzlichen Gründen.
Einigungsstellenverfahren bei Blockade.

### Schritt 2 — Vertrauensmann SBG — Soldatenvertretung

§§ 36–37 SBG: Vertrauensmann ist Ansprechpartner für Soldaten.
Beteiligungsrechte bei Versetzungen, Beurteilungen.
Kein Vetorecht — nur Anhörung und Stellungnahme.
Unterschied: BPersVG hat echtes Mitbestimmungsrecht.

### Schritt 3 — Abgrenzung in gemischten Dienststellen

Zivile Beschäftigte → Personalrat.
Soldaten → Vertrauensmann.
Paralleles Verfahren bei gemischten Maßnahmen.
Keine Zuständigkeit von BetrVG.

### Schritt 4 — Fehler bei Personalratsbeteiligung

Keine Beteiligung → Maßnahme rechtswidrig (Kündigung unwirksam).
Verspätete Beteiligung → wie keine Beteiligung.
Rechtsweg: VG für Personalvertretungsstreit (BPersVG).
Kündigungsschutzklage: ArbG.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Personalrat (BPersVG) vs. Vertrauensmann (SBG)
- Checkliste: Beteiligungsverfahren bei Kündigung ziviler Beschäftigter
- Flussdiagramm: Mitbestimmungsverfahren

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bpersvg/ — BPersVG
- https://www.gesetze-im-internet.de/sbg/ — SBG
- https://www.bundesarbeitsgericht.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
