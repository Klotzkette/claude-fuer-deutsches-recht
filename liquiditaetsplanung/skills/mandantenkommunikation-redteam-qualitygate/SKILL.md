---
name: mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation Redteam Qualitygate im Plugin Liquiditaetsplanung: prüft konkret Mandantenkommunikation im Plugin liquiditaetsplanung, Red-Team Qualitygate im Plugin liquiditaetsplanung, Ausgabengruppen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Mandantenkommunikation Redteam Qualitygate

## Arbeitsbereich

**Mandantenkommunikation Redteam Qualitygate** ordnet den Fall über die tragenden Prüfungslinien: Mandantenkommunikation im Plugin liquiditaetsplanung, Red-Team Qualitygate im Plugin liquiditaetsplanung, Ausgabengruppen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin liquiditaetsplanung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin liquiditaetsplanung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `spezial-ausgabengruppen-fristennotiz-und-naechster-schritt` | Ausgabengruppen: Fristennotiz und nächster Schritt im Plugin liquiditaetsplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin liquiditaetsplanung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin liquiditaetsplanung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Kommunikation Liquiditätsplanung — wesentliche Pflichten
- **§ 1 StaRUG ist Geschäftsführungspflicht:** Die Krisenfrüherkennung ist nicht "schön zu haben", sondern Pflicht jedes Geschäftsleiters einer haftungsbeschränkten Gesellschaft. Verstoß kann § 43 GmbHG-Haftung auslösen.
- **§ 15a InsO Antragsfristen:** Bei Zahlungsunfähigkeit Höchstfrist drei Wochen, bei Überschuldung sechs Wochen (Stand prüfen) — nicht zur freien Verfügung; jeder Tag zählt für § 15b InsO Zahlungsverbot.
- **§ 15b InsO Zahlungsverbot:** Nach Eintritt der Insolvenzreife sind nur noch privilegierte Zahlungen erlaubt; Verstoß führt zu persönlicher Haftung des Geschäftsführers gegenüber der späteren Masse.
- **§ 266a StGB Sozialversicherung:** Arbeitnehmer-SV-Beiträge sind unverzüglich abzuführen; Stundungsantrag rechtzeitig stellen, sonst Strafbarkeit.
- **Klare Sprache:** "Sie haben am [Datum] eine Deckungslücke von X EUR. Nach BGH-Rechtsprechung liegt dann Zahlungsunfähigkeit vor, sofern keine Schließung binnen drei Wochen absehbar ist."
- **Honorar:** Beratungsvereinbarung mit Pauschal- oder Stundenhonorar; reine RVG-Abrechnung deckt Sanierungsberatung nicht.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin liquiditaetsplanung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin liquiditaetsplanung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Liquiditätsplanungs-Red-Team
- **Methodenprüfung:**
 - Direkte Methode (OPOS-basiert) oder indirekte Methode (GuV-basiert) — in der Krise zwingend direkte Methode.
 - Granularität angemessen? 13 Wochen wöchentlich, 24 Monate monatlich.
 - Saldenkonsistenz: Anfangsbestand + Cash-In − Cash-Out = Endbestand auf jeder Periode.
- **Zahlen-Plausibilität:**
 - Umsatzprognose mit Auftragsbestand und Vergangenheit abgeglichen?
 - Working-Capital-Annahmen (DSO, DPO, DIO) realistisch?
 - Steuern und SV-Beiträge mit Fälligkeit gepflegt?
 - Lohn und Gehalt mit Auszahlungstag, nicht nur Monatswert.
- **Sensitivität:**
 - Best/Base/Worst dokumentiert?
 - Worst-Case zeigt Liquiditätsdeckung? Wenn nein: drohende ZU § 18 InsO.
- **Rechtsbezogene Prüfung:**
 - § 17 InsO 10-Prozent-/3-Wochen-Linie sauber berechnet?
 - § 18 InsO 24-Monats-Horizont eingehalten?
 - Vorhandene Kreditlinien als sicher angenommen — Kündigung der Linie nicht eingerechnet?
 - Bei zugesagter Bankfinanzierung: schriftliche Zusage oder nur Absichtserklärung?
- **Halluzinations-Stopps:**
 - Keine erfundenen BGH-Az. zur 10-Prozent-Schwelle.
 - § 64 GmbHG a.F. (vor 2021) vs. § 15b InsO (seit SanInsFoG) sauber unterscheiden.
 - StaRUG (§ 1, § 18) gilt seit 1.1.2021 — keine Vor-Anwendung.

## Plan-Schwächen
- Plan zeigt nur grünen Bereich, aber Annahmen sind nicht plausibel → potenziell schwach für Haftungsabschirmung.
- Plan ohne Datum / Verantwortliche → Beweiskraft im Haftungsprozess fraglich.

## 3. `spezial-ausgabengruppen-fristennotiz-und-naechster-schritt`

**Fokus:** Ausgabengruppen: Fristennotiz und nächster Schritt im Plugin liquiditaetsplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Ausgabengruppen: Fristennotiz und nächster Schritt

## Fachkern: Ausgabengruppen: Fristennotiz und nächster Schritt
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ausgabengruppen** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Ausgabengruppen Liquiditätsplan — Fristen und Priorisierung
- **Personal (Pflicht):** Lohn/Gehalt zum Monatsende, Lohnsteuer & SV-Beiträge zum drittletzten Bankarbeitstag des Folgemonats. § 266a StGB strafbewehrt für AN-SV-Beiträge!
- **Steuern:** USt-Voranmeldung 10. des Folgemonats, Steuervorauszahlungen quartalsweise (10.3., 10.6., 10.9., 10.12.), Jahresvorauszahlungen nach Bescheid. Bei Insolvenzreife Aufrechnungsverbot § 96 InsO.
- **Sozialversicherung:** Beiträge gegenüber Krankenkasse — Krankenkasse-Beitragsbescheinigung zwingend (Vorlage Insolvenzgericht im Eröffnungsverfahren).
- **Banken:** Tilgungsrate, Zinszahlung, Kovenanten-Stichtage (idR Quartalsweise) — Kovenantenbruch löst regelmäßig sofortiges Kündigungsrecht aus.
- **Lieferanten:** Nach Zahlungsziel sortieren; Skontofrist (10–14 Tage) vs. Nettofrist (30–60 Tage). Eigentumsvorbehalt-Lieferanten gesondert priorisieren.
- **Vermieter:** Mietzins zum Monatsanfang; Sonderkündigungsrecht Verwalter § 109 InsO mit 3-Monats-Frist im Insolvenzverfahren.
- **Versicherungen:** Haftpflicht und Sach idR jährlich; bei Krise prüfen, ob Auszahlung bei Insolvenzfall in Masse oder beim Versicherungsnehmer landet.
- **Priorisierung in Krise (vor § 15a InsO-Antragspflicht):** SV-Beiträge AN-Anteil > Steuerschulden (Lohnsteuer) > Lohn > Lieferanten kritischer Lieferant > sonstige. Reine Liquiditätsschonung kann § 266a StGB-Strafbarkeit und § 15b InsO-Haftung auslösen.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
