---
name: fa-verkehrsrecht-fristen-risiko-mandant
description: "FA Verkehrsrecht Fristen Risiko Mandant im Plugin Fachanwalt Verkehrsrecht: prüft konkret Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht, Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht, Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# FA Verkehrsrecht Fristen Risiko Mandant

## Arbeitsbereich

**FA Verkehrsrecht Fristen Risiko Mandant** ordnet den Fall über die tragenden Prüfungslinien: Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht, Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht, Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Verkehrsrechts-Fristen-Speziallage (alle Saeulen!)
- **Unfallregulierung:** Verjährung Schadenersatz § 195 BGB 3 Jahre; § 199 BGB Beginn ab Kenntnis. KH-Versicherer Direktanspruch § 115 VVG; 4 Wochen Zahlungsfrist § 14 PflVG bei klarer Haftung.
- **OWi-Einspruch § 67 OWiG: 2 Wochen** ab Zustellung Bussgeldbescheid; Rechtsbeschwerde §§ 79, 80 OWiG: 1 Woche / 1 Monat.
- **Verkehrsstrafrecht:** § 410 StPO Einspruch Strafbefehl 2 Wochen; § 314 StPO Berufung 1 Woche; §§ 341, 345 StPO Revision 1 Woche / 1 Monat.
- **Fuehrerschein:** § 25 StVG Fahrverbot 4-Monats-Antrittsfrist Ersttaeter; vorläufige Entziehung § 111a StPO ab Verfahren wegen § 315c, § 316, § 142 StGB; § 69 StGB Entziehung Fahrerlaubnis (Sperre § 69a StGB).
- **MPU-/FeV-Fristen:** Anhörung vor Anordnung; Vorlagefrist Gutachten regelmaessig 2-3 Monate (§ 11 IV FeV); Wiedererteilung Fahrerlaubnis fruehestens 6 Monate vor Ablauf Sperre (§ 20 FeV).
- **Versicherungsrecht VVG:** Anzeigeobliegenheit § 30 VVG unverzueglich; § 28 VVG Verletzung Obliegenheiten - Leistungsfreiheit Versicherer; Verjährung § 195 BGB.
- **Punkte FAER § 4 StVG:** 8 Punkte Entziehung; 4-5 Punkte Ermahnung; 6-7 Punkte Verwarnung mit Aufbauseminar-Hinweis.
- **Risikoampel:** Rot bei Frist Rechtsmittel, drohendem Fuehrerscheinverlust, Existenzgefaehrdung Berufskraftfahrer, MPU; Gelb bei Versicherungsstreit; Gruen bei dokumentierter Strategie.

## 2. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Verkehrsrechts-Mandantenkommunikation Speziallage
- **Entscheidungsfragen pro Saeule:**
 - **Unfallregulierung:** fiktive vs. konkrete Abrechnung; SV-Gutachten in Auftrag geben; Mietwagen vs. Nutzungsausfall; Vorschuss/Klage gegen Versicherer § 115 VVG.
 - **OWi:** Einspruch gegen Bussgeld trotz Kostenrisiko? Ziel: Punkte vermeiden, Fahrverbot abwenden, Geldbusse senken.
 - **Strafrecht:** Schweigerecht § 136 StPO; bei Trunkenheitsfahrt § 316 StGB nach Akteneinsicht; vorläufige Entziehung Fuehrerschein § 111a StPO.
 - **FeV:** MPU - Beratung Vorbereitungskurs, Abstinenznachweis (Haaranalyse, Urinkontrollen); Wiedererteilungsantrag rechtzeitig vor Ablauf Sperre § 20 FeV.
 - **Versicherung:** Anzeigeobliegenheit § 30 VVG; Schadensmeldung vollstaendig; Quotenregelung bei Eigenverschulden.
- **Berufliche Auswirkungen** stets explizit ansprechen: Berufskraftfahrer, Aussendienst, Pendler, Aerzte/Anwaelte (BZRG-Eintrag bei Verurteilung); Kammerpflicht-Meldungen pruefen.
- **Versicherungsrechtliche Beratung:** ggf. Erhoehung KH-Beitrag (Schadenfreiheitsrabatt), Insassenversicherung, Rechtsschutz pruefen (Selbstbeteiligung, Vorvertrag, Wartezeit).
- **Kostenhinweis RVG:** Verkehrsstrafsachen / Bussgeld: VV 4100 ff. RVG; Hauptverhandlungstermin auch Sonderkosten; Rechtsschutzversicherung Deckungszusage einholen.
- **Mandantenfreigabe schriftlich** für: Einspruchsruecknahme, Vergleich mit Versicherer, Strafrechtliche Deals § 257c StPO, MPU-Antritt.
- **Pflicht-Hinweise:** kein Schweigen gegenueber Polizei am Unfallort verpflichtend ueber Pflichtangaben (Name, Adresse, Kfz-Daten); aber keine Aussage zur Schuldfrage; Schweigerecht im Strafverfahren.

## 3. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Verkehrsrechts-Red-Team-Checks
- **Saeule-spezifischer Check:**
 - Verkehrszivilrecht: § 195 BGB Verjährung gepruefft? § 254 BGB Mitverschulden? § 17 StVG Quotenbildung?
 - OWi: § 67 OWiG 2 Wochen? § 26 III StVG Verjährung? Messverfahren-Pruefung dokumentiert?
 - Verkehrsstraf: § 410 / § 314 / § 341, § 345 StPO Fristen? Schweigerecht § 136 StPO belehrt?
 - FeV: Anhörungsfrist FE-Behörde? MPU-Vorlagefrist? Wiedererteilungsfristen § 20 FeV?
 - Versicherung: § 30 VVG unverzueglich Anzeige? § 28 VVG Leistungsfreiheit-Risiko?
- **Schadensermittlung Re-Check:**
 - Reparaturkosten vs. Wiederbeschaffungswert: 130 %-Grenze (BGH-Linie) bei konkreter Reparatur, 100 % bei fiktiver.
 - Wertminderung nur bei tatsaechlicher Reparatur und nicht zu altem Fahrzeug.
 - Nutzungsausfalldauer mit Schwacke / Frauenhofer-Tabelle.
 - Mietwagen: Anspruch nur in angemessenem Rahmen; Frauenhofer / Schwacke / Mittelwert.
- **Vollmachts-Check:** Mandat aus Vollmacht; ggf. Forderungsabtretung an SV / KFZ-Werkstatt sauber dokumentiert.
- **Konsequenzen-Re-Check:**
 - Eintragung FAER bei Verkehrs-OWi.
 - BZRG-Eintrag bei Verkehrsstrafrecht (ab 91 TS / Freiheitsstrafe).
 - Versicherungsrueckstufung (Schadenfreiheitsklassen).
 - MPU-Anordnung bei wiederholten OWi oder ab 1,6 Promille bzw. Drogen einmalig.
- **Halluzinations-Check:** Keine erfundenen BGH-/OLG-Az; "staendige Rspr." statt erfundener Fundstellen.
- **Berufliche Relevanz** stets ansprechen: Berufskraftfahrer, Pendler, Aerzte/Anwaelte (Berufsaufsicht), Beamte (Disziplinarrecht).
