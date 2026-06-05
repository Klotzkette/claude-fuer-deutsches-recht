---
name: livecheck-sg-mandantenbrief-soldat-mobbing
description: "Livecheck SG Mandantenbrief Soldat Mobbing: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Livecheck SG Mandantenbrief Soldat Mobbing

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Livecheck SG Mandantenbrief Soldat Mobbing** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `livecheck-sg-wbo-wdo-wpflg-svg` | Live-Check SG, WBO, WDO, WPflG, SVG: prüft aktuellen Normstand, Änderungen und Verweisungen. Norm-/Quellenanker: gesetze-im-internet.de, dejure.org. |
| `mandantenbrief-soldat-verstaendlich` | Mandantenbrief Soldat verständlich: erstellt klare, nicht-juristische Erläuterungen komplexer Rechtssituationen für Soldaten. Norm-/Quellenanker: WBO, WDO, SG, SVG. |
| `mobbing-fuersorgepflicht-bundeswehr` | Mobbing und Fürsorgepflicht Bundeswehr: prüft §§ 10 und 12 SG, Beschwerdewege, Schadensersatz und WBO. Norm-/Quellenanker: §§ 10 und 12 SG, SoldGG, WBO. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Livecheck SG Mandantenbrief Soldat Mobbing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `livecheck-sg-wbo-wdo-wpflg-svg`

**Fokus:** Live-Check SG, WBO, WDO, WPflG, SVG: prüft aktuellen Normstand, Änderungen und Verweisungen. Norm-/Quellenanker: gesetze-im-internet.de, dejure.org.

# Live-Check SG, WBO, WDO, WPflG, SVG

## Fachkern: Live-Check SG, WBO, WDO, WPflG, SVG
- **Spezialgegenstand:** Live-Check SG, WBO, WDO, WPflG, SVG. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Normen im Bundeswehrrecht ändern sich regelmäßig. Live-Check-Fähigkeit ist essenziell, bevor tragfähige Rechtsmeinung gebildet wird.

Dieser Skill gibt Anleitungen, wie aktueller Normstand zu prüfen ist, und stellt eine Priorisierungsliste wichtiger Normen bereit.

## Einschlägige Normen und Quellen

- SG — Soldatengesetz (aktuell prüfen)
- WBO — Wehrbeschwerdeordnung
- WDO — Wehrdisziplinarordnung 2002 i.d.F. aktuell
- WPflG — Wehrpflichtgesetz (aktuell i.d.F. nach Aussetzung)
- SVG — Soldatenversorgungsgesetz
- BBesG — Bundesbesoldungsgesetz

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welche Norm soll auf aktuelle Fassung geprüft werden?
- Liegt ein konkreter Paragraf mit Normwortlaut vor?
- Wurden Änderungen seit einer bestimmten Referenzfassung gesucht?
- Soll auf EUR-Lex für EU-Bezüge geprüft werden?

## Prüf- und Arbeitslogik

### Schritt 1 — Primärquellen für Live-Check

gesetze-im-internet.de: amtliche aktuelle Normtexte.
dejure.org: Verlinkungen, Änderungshistorie, Rechtsprechungsübersicht.
bundeswehr.de: Vorschriften und ZDv (eingeschränkt öffentlich).
EUR-Lex: EU-Sekundärrecht (z. B. NATO-Truppenstatut-Umsetzungen).

### Schritt 2 — Änderungen und Verweisungen

SG: zuletzt geändert durch Gesetz zur Stärkung der Bundeswehr — Datum live prüfen.
WDO: Reformgesetz 2002, seitdem mehrfach geändert.
BBesG: jährliche Besoldungsanpassungen durch Besoldungsanpassungsgesetz.
SVG: EinsatzWVG-Änderungen.

### Schritt 3 — Wichtige aktuelle Prüfpunkte

§ 58b SG (FWDL): aktuelle Dienstzeit-Grenzen.
§ 17a SG (Impfpflicht): aktuelle Fassung.
WDO § 38 (Bemessung): BVerwG-Rspr. zu neueren Maßstäben.
BBesG Anlage IV: aktuelle Grundgehaltstabelle nach letztem Besoldungsanpassungsgesetz.

### Schritt 4 — Zitierstandard

Norm: Gesetz, Paragraf, Absatz, Satz (z. B. § 11 Abs. 1 S. 3 SG).
Veröffentlichung: BGBl. oder dejure.org.
Kein Zitieren aus Kommentaren ohne Prüfung des Primärtexts.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Checkliste: Live-Check-Quellen (5 Primärquellen)
- Tabelle: Wichtige Normen und ihre letzten Änderungsdaten
- Muster: Normzitat mit Quellenverweis

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de — Amtliche Normtexte
- https://dejure.org — Verlinkungen und Änderungshistorie
- https://eur-lex.europa.eu — EU-Recht
- https://www.bverwg.de
- https://www.bverfg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `mandantenbrief-soldat-verstaendlich`

**Fokus:** Mandantenbrief Soldat verständlich: erstellt klare, nicht-juristische Erläuterungen komplexer Rechtssituationen für Soldaten. Norm-/Quellenanker: WBO, WDO, SG, SVG.

# Mandantenbrief Soldat — Verständlich erläutern

## Fachkern: Mandantenbrief Soldat — Verständlich erläutern
- **Spezialgegenstand:** Mandantenbrief Soldat — Verständlich erläutern. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Soldaten sind oft mit komplexen Rechtssituationen konfrontiert, ohne juristische Ausbildung. Der Mandantenbrief muss verständlich, klar strukturiert und handlungsorientiert sein — ohne Fachvokabular ohne Erklärung.

Kernformat: Situation → Was bedeutet das für Sie → Ihre Optionen → Empfehlung → Fristen.

## Einschlägige Normen und Quellen

- WBO — Verfahrensrechte
- WDO — Disziplinar
- SG — Statusrecht
- SVG — Versorgung
- BBesG — Besoldung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was soll dem Soldaten erklärt werden?
- Welcher Bildungsstand und Vorwissen darf angenommen werden?
- Soll ein Empfehlungsschreiben oder eine kurze Erklärung entstehen?
- Gibt es spezifische Dokumente, auf die Bezug genommen werden soll?

## Prüf- und Arbeitslogik

### Schritt 1 — Sprachliche Anforderungen

Kein Fachjargon ohne Erklärung.
Kurze Sätze, aktive Formulierungen.
Konkrete Zahlen und Fristen.
Klare Handlungsempfehlungen (Bullet Points).
Worst-Case und Best-Case nennen.

### Schritt 2 — Standardformat Mandantenbrief

1. Ihre Situation: kurze sachliche Zusammenfassung.
2. Was das bedeutet: rechtliche Konsequenzen in Alltagssprache.
3. Ihre Optionen: A, B, C — mit Pro/Contra.
4. Empfehlung: Prioritätsmaßnahme.
5. Fristen und nächste Schritte.

### Schritt 3 — Typische Themen für Mandantenbriefe

Beschwerde gegen Versetzung: 'Sie können Widerspruch einlegen — Frist ist X.'
Rückforderung Ausbildungskosten: 'Die Bundeswehr will Y zurück — hier ist was Sie tun können.'
Disziplinarverfahren: 'Sie werden beschuldigt — Ihre Rechte sind...'

### Schritt 4 — Rechtssicherheitshinweise

Immer darauf hinweisen: 'Dies ist eine Ersteinschätzung, kein verbindlicher Rechtsrat.'
Auf weitergehende anwaltliche Beratung hinweisen.
Datum und Aktualitätsvorbehalt.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Vorlage: Mandantenbrief-Format für Disziplinarfall
- Vorlage: Mandantenbrief-Format für Besoldungsstreit
- Vorlage: Mandantenbrief-Format für Entlassung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wbo/ — WBO
- https://www.gesetze-im-internet.de/sg/ — SG
- https://www.bundeswehr.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `mobbing-fuersorgepflicht-bundeswehr`

**Fokus:** Mobbing und Fürsorgepflicht Bundeswehr: prüft §§ 10 und 12 SG, Beschwerdewege, Schadensersatz und WBO. Norm-/Quellenanker: §§ 10 und 12 SG, SoldGG, WBO.

# Mobbing und Fürsorgepflicht Bundeswehr

## Fachkern: Mobbing und Fürsorgepflicht Bundeswehr
- **Spezialgegenstand:** Mobbing und Fürsorgepflicht Bundeswehr. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die Bundeswehr ist als Dienstherr zur Fürsorge verpflichtet (§ 36 SG). Mobbing im Dienstverhältnis verletzt sowohl § 12 SG (Kameradschaft) als auch die allgemeine Fürsorgepflicht.

Opfer haben Ansprüche: WBO-Beschwerde, Schadensersatz (BGBl Amtshaftung), Disziplinarmaßnahmen gegen Täter.

## Einschlägige Normen und Quellen

- § 10 SG — Fürsorgepflicht Vorgesetzte
- § 12 SG — Kameradschaft
- SoldGG — Diskriminierungsschutz
- § 36 SG — Fürsorge des Dienstherrn
- BGB §§ 823, 826 — Schadensersatz
- WBO — Beschwerdeverfahren

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was ist das konkrete Mobbing-Verhalten (Ausgrenzung, Demütigung, Schikane)?
- Wer ist Täter (Vorgesetzter, Gleichrangiger)?
- Wie lange besteht das Verhalten?
- Wurde der Dienstherr informiert und hat er gehandelt?
- Gibt es Gesundheitsschäden?

## Prüf- und Arbeitslogik

### Schritt 1 — Fürsorgepflicht § 36 SG

Dienstherr hat aktive Schutzpflicht bei Mobbing.
Untätigkeit trotz Kenntnis = Pflichtverletzung.
Amtshaftung (Art. 34 GG, § 839 BGB) bei nachgewiesenem Versagen.
Parallele WBO-Beschwerde gegen untätige Vorgesetzte.

### Schritt 2 — Mobbing-Definition und Nachweisführung

Systematisches, wiederholtes feindseliges Verhalten über längeren Zeitraum.
Einzelne Vorfälle regelmäßig nicht ausreichend.
Beweis: Tagebuch, Zeugen, ärztliche Bescheinigungen.
Kausalität Mobbing → Gesundheitsschaden prüfen.

### Schritt 3 — Beschwerdewege und Rechtsbehelfe

1. Vorgesetzter (wenn nicht Täter). 2. WBO-Beschwerde. 3. Gleichstellungsbeauftragte (wenn Diskriminierung). 4. BAPersBw. 5. Klage VG (Amtshaftung) oder LG (§ 839 BGB i.V.m. Art. 34 GG).

### Schritt 4 — Disziplinar gegen Täter

Meldung des Mobbings als Pflichtverletzung des Täters.
Disziplinaranzeige bei zuständigem Vorgesetzten.
WDO-Verfahren.
Strafrecht: § 185 StGB (Beleidigung), § 240 StGB (Nötigung), § 223 StGB (Körperverletzung).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Mobbing-Tagebuch-Vorlage
- Muster-WBO-Beschwerde bei Mobbing
- Checkliste: Schadensersatzklage — Anforderungen

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — §§ 10, 12, 36 SG
- https://www.gesetze-im-internet.de/soldgg/ — SoldGG
- https://www.gesetze-im-internet.de/wbo/ — WBO
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
