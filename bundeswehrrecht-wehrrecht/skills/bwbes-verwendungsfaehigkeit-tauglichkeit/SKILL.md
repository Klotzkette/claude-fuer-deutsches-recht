---
name: bwbes-verwendungsfaehigkeit-tauglichkeit
description: "Bwbes Verwendungsfaehigkeit Tauglichkeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bwbes Verwendungsfaehigkeit Tauglichkeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bwbes Verwendungsfaehigkeit Tauglichkeit** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bwbes-neu-013-verwendungsfaehigkeit-tauglichkeit-und-finanzielle` | Verwendungsfähigkeit, Tauglichkeit, finanzielle Folgen: prüft Tauglichkeitsstufen, dienstrechtliche Konsequenzen und SVG-Versorgung. Norm-/Quellenanker: §§ 44–45 und 55 SG, SVG. |
| `bwbes-neu-014-auslandseinsatz-anerkennung-und-nachweise` | Auslandseinsatz Anerkennung und Nachweise: prüft Einsatzbescheinigungen, AVZ-Nachweise, WDB-Dokumentation und behördliche Verfahren. Norm-/Quellenanker: BBesG §§ 56–58, SVG, EinsatzWVG. |
| `bwbes-neu-015-ruhensregelungen-versorgung-und-erwerbseinkommen` | Ruhensregelungen Versorgung und Erwerbseinkommen: prüft SVG §§ 53–56, BeamtVG § 68, Anrechnungsgrenzen und Ausnahmen. Norm-/Quellenanker: SVG, BeamtVG analog, BBesG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Bwbes Verwendungsfaehigkeit Tauglichkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bwbes-neu-013-verwendungsfaehigkeit-tauglichkeit-und-finanzielle`

**Fokus:** Verwendungsfähigkeit, Tauglichkeit, finanzielle Folgen: prüft Tauglichkeitsstufen, dienstrechtliche Konsequenzen und SVG-Versorgung. Norm-/Quellenanker: §§ 44–45 und 55 SG, SVG.

# Verwendungsfähigkeit, Tauglichkeit und finanzielle Folgen

## Fachkern: Verwendungsfähigkeit, Tauglichkeit und finanzielle Folgen
- **Spezialgegenstand:** Verwendungsfähigkeit, Tauglichkeit und finanzielle Folgen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

T1–T5: Tauglichkeitsstufen bestimmen Verwendungsfähigkeit. Dauerhafte T5-Einstufung führt zu Entlassung (SaZ) oder Zurruhesetzung (BeruSold).

Die Versorgungsfolgen sind erheblich: Ruhegehalt, Übergangsgebührnisse, WDB-Zuschlag. Fehlerhafte Einstufungen sind anfechtbar.

## Einschlägige Normen und Quellen

- § 44 SG — Verwendungsunfähigkeit
- § 45 SG — Zurruhesetzung Berufssoldat
- § 55 Abs. 2 SG — Entlassung SaZ
- SVG §§ 1–26 — Versorgungsfolgen
- DV 46/1 — Begutachtungsrichtlinien

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Tauglichkeitsstufe festgestellt?
- Dauerhaft oder vorübergehend?
- Entlassung oder Zurruhesetzung droht?
- Versorgungsanspruch nach SVG?
- Gegengutachten beauftragt?

## Prüf- und Arbeitslogik

### Schritt 1 — Tauglichkeitsstufen im Detail

T1: voll tauglich. T2: beschränkt tauglich. T3: verwendungseingeschränkt. T4: nicht für alle Tätigkeiten. T5: dauerhaft dienstunfähig.
Sondereignungen (fliegerärztlich, ABC, Taucher) separat prüfen.

### Schritt 2 — Dienstrechtliche Folgen

SaZ T5: Entlassung § 55 Abs. 2 SG — kein Rückforderungsanspruch Ausbildungskosten!
BeruSold T5: Zurruhesetzung § 45 SG; Ruhegehalt nach Dienstzeit.
Frist: Entlassungsverfügung anfechten (WBO § 6).

### Schritt 3 — Versorgungsfolgen

BeruSold: Ruhegehalt § 26 SVG (Mindestversorgung, Prozentsatz nach Dienstzeit).
SaZ: Übergangsgebührnisse § 5 SVG.
WDB-Zuschlag § 26a SVG bei krankheitsbedingter Entlassung.
Einsatzbedingte Dienstunfähigkeit: erhöhte Versorgung.

### Schritt 4 — Rechtsbehelfe

WBO-Beschwerde gegen Entlassungsverfügung.
Gegengutachten beauftragen.
Versorgungsklage: VG (Rentenansprüche), Sozialgericht (WDB).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Tauglichkeitsstufen T1–T5 mit dienstrechtlichen Konsequenzen
- Prüfschema: Entlassung vs. Zurruhesetzung
- Checkliste: Gegengutachten beauftragen

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — §§ 44–45, 55 SG
- https://www.gesetze-im-internet.de/svg/ — SVG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `bwbes-neu-014-auslandseinsatz-anerkennung-und-nachweise`

**Fokus:** Auslandseinsatz Anerkennung und Nachweise: prüft Einsatzbescheinigungen, AVZ-Nachweise, WDB-Dokumentation und behördliche Verfahren. Norm-/Quellenanker: BBesG §§ 56–58, SVG, EinsatzWVG.

# Auslandseinsatz: Anerkennung und Nachweise

## Fachkern: Auslandseinsatz: Anerkennung und Nachweise
- **Spezialgegenstand:** Auslandseinsatz: Anerkennung und Nachweise. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Nach Auslandseinsätzen entstehen zahlreiche Anerkennungs- und Nachweisanforderungen: AVZ korrekt abgerechnet? Einsatzbescheinigung vollständig? WDB-Schäden gemeldet?

Häufige Probleme: fehlende Einsatzbescheinigungen, nachträgliche PTBS-Anerkennung, Streit über Einsatzzeitraum und Gefährdungsstufe.

## Einschlägige Normen und Quellen

- §§ 56–58 BBesG — AVZ (Nachweispflichten)
- SVG §§ 63a–63h — Einsatzversorgung (Anerkennungsverfahren)
- EinsatzWVG — Weiterverwendungsrecht
- SG § 30 — Fürsorge (Dokumentationspflicht Dienstherr)
- AuslVZV — Stufenzuordnung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Liegt vollständige Einsatzbescheinigung vor?
- Wurden alle Einsatztage korrekt erfasst?
- Wurde einsatzbedingte Erkrankung/Verletzung gemeldet und dokumentiert?
- AVZ-Abrechnung vollständig und korrekt?
- Wurden Versorgungsansprüche rechtzeitig angemeldet?

## Prüf- und Arbeitslogik

### Schritt 1 — Einsatzbescheinigungen und Dokumentation

Einsatzbescheinigung: ausgestellt vom Kontingentführer/Kommandeur.
Inhalt: Einsatzgebiet, Zeitraum, Gefährdungsstufe, besondere Vorkommnisse.
Aufbewahrung: für spätere WDB-Anträge!
Fehlende Bescheinigung: Anforderung beim BAPersBw, Einsatzarchiv.

### Schritt 2 — AVZ-Abrechnung und Nachweise

Tageweise Abrechnung; Einsatztage mit Bescheinigung belegen.
Stufenzuordnung nach AuslVZV: Region und Gefahrenlage.
Fehler: nachträglich korrigierbar, Ausschlussfrist beachten.
Widerspruch gegen fehlerhafte Abrechnung.

### Schritt 3 — WDB-Dokumentation

Schäden unverzüglich melden — im Einsatz und nach Rückkehr.
Sanitätsdienstliche Behandlung dokumentieren lassen.
PTBS: später auftretend — Kausalitätsvermutung bei Einsatzbescheinigung.
Zeugen für Kampfereignisse sichern.

### Schritt 4 — Verfahren und Fristen

AVZ-Nachforderung: 3 Jahre Verjährung, Ausschlussfristen prüfen.
WDB-Antrag: keine starre Frist, aber früh stellen (Beweissicherung).
EinsatzWVG-Antrag: nach Entlassung/Dienstunfähigkeit.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Checkliste: Nachweise Auslandseinsatz (AVZ, WDB, Einsatzbescheinigung)
- Muster: Antrag Einsatzbescheinigung beim BAPersBw
- Prüfschema: AVZ-Abrechnung nachrechnen

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bbesg/ — §§ 56–58 BBesG
- https://www.gesetze-im-internet.de/svg/ — SVG §§ 63a ff.
- https://www.bundeswehr.de/de/organisation/personal/bundesamt-fuer-das-personalmanagement

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `bwbes-neu-015-ruhensregelungen-versorgung-und-erwerbseinkommen`

**Fokus:** Ruhensregelungen Versorgung und Erwerbseinkommen: prüft SVG §§ 53–56, BeamtVG § 68, Anrechnungsgrenzen und Ausnahmen. Norm-/Quellenanker: SVG, BeamtVG analog, BBesG.

# Ruhensregelungen: Versorgung und Erwerbseinkommen

## Fachkern: Ruhensregelungen: Versorgung und Erwerbseinkommen
- **Spezialgegenstand:** Ruhensregelungen: Versorgung und Erwerbseinkommen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Soldatenversorgung (Ruhegehalt, Übergangsgebührnisse) trifft auf Erwerbseinkommen und Rentenbezüge. Ruhensregelungen (§§ 53–56 SVG) können zur erheblichen Kürzung führen.

Berufssoldaten im Ruhestand, die eine Erwerbstätigkeit aufnehmen, müssen Anrechnungsgrenzen kennen. Anzeigepflicht gegenüber BAPersBw!

## Einschlägige Normen und Quellen

- SVG §§ 53–56 — Ruhensregelungen
- § 55 SVG — Zusammentreffen Versorgung und Rentenansprüche
- BeamtVG § 68 — Ruhensregelung (analog)
- BBesG — Besoldung und Versorgung gleichzeitig
- SGB VI — Rentenrecht (Schnittstelle)

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Berufssoldat im Ruhestand mit Erwerbseinkommen?
- SaZ mit Übergangsgebührnissen und Erwerbstätigkeit?
- Höhe des Erwerbseinkommens, das angerechnet wird?
- Rentenansprüche vorhanden (§ 55 SVG)?
- Wurde Erwerbseinkommen gemeldet?
- Droht Rückforderung wegen unterlassener Meldung?

## Prüf- und Arbeitslogik

### Schritt 1 — Ruhensregelungen §§ 53–56 SVG

§ 53 SVG: Ruhegehalt ruht, soweit Ruhegehalt + Erwerbseinkommen Höchstgrenze übersteigt.
Höchstgrenze: letztes aktives Grundgehalt + Zulagen (gesetzlich festgelegt).
Ausnahmen: ehrenamtliche Tätigkeit, soziale Aktivitäten.
Anzeigepflicht: sofortige Meldung an BAPersBw.

### Schritt 2 — Zusammentreffen Versorgung und Rente § 55 SVG

Versorgung + GRV-Rente: Rente wird auf Versorgung angerechnet.
Anrechnungsfreier Betrag (Freibetrag).
Überprüfung: Jahresrentenanpassung kann Ruhens-Grenze verschieben.
Antrag: BAPersBw jährlich melden.

### Schritt 3 — Übergangsgebührnisse SaZ

§ 5 Abs. 6 SVG: Erwerbseinkommen wird auf Übergangsgebührnisse angerechnet.
Vollständiger Wegfall möglich bei hohem Einkommen.
Anzeigepflicht: monatliche Meldung.

### Schritt 4 — Rückforderung und Rechtsbehelfe

Unterlassene Meldung: Überzahlung rückforderbar (kein Gutglaubensschutz!).
Widerspruch gegen Ruhens-/Rückforderungsbescheid: 1 Monat.
Klage: VG.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Ruhensregelungen SVG — Grenzen und Ausnahmen
- Berechnungsbeispiel: Ruhegehalt + Erwerbseinkommen vs. Höchstgrenze
- Checkliste: Anzeigepflichten BAPersBw

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/svg/ — SVG §§ 53–56
- https://dejure.org/gesetze/SVG
- https://www.bverwg.de
- https://www.bundeswehr.de/de/organisation/personal/bundesamt-fuer-das-personalmanagement

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
