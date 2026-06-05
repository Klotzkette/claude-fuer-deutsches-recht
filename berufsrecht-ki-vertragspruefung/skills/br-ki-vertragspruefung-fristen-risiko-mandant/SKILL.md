---
name: br-ki-vertragspruefung-fristen-risiko-mandant
description: "BR KI Vertragspruefung Fristen Risiko Mandant: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# BR KI Vertragspruefung Fristen Risiko Mandant

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **BR KI Vertragspruefung Fristen Risiko Mandant** im Plugin Berufsrecht Ki Vertragspruefung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

Im Plugin Berufsrecht Ki Vertragspruefung gilt für **BR KI Vertragspruefung Fristen Risiko Mandant**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin berufsrecht-ki-vertragspruefung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Berufsrecht-KI-typische Risiken
- **§ 203 StGB**: Strafrechtliche Schweigepflichtverletzung — Freiheitsstrafe bis 1 Jahr oder Geldstrafe; Antragsdelikt § 205 StGB.
- **§ 43a Abs. 2 BRAO / § 43e BRAO**: Berufsrechtliche Verschwiegenheit, anwaltsgerichtliche Maßnahmen § 113 BRAO bis Ausschluss aus der Anwaltschaft.
- **DSGVO**: Art. 33 Datenpannenmeldung 72h, Bußgelder bis 20 Mio. EUR / 4 %.
- **KI-VO**: Schulungspflicht Art. 4 KI-VO seit 02.02.2025; Verbotene Praktiken Art. 5 (z. B. Social Scoring) — bis 35 Mio. EUR / 7 %.
- **Haftung**: zivilrechtliche Haftung gegenüber Mandantschaft (§§ 280, 611, 675 BGB), Anwaltshaftpflicht § 51 BRAO.

## Ampelkriterien
- **Rot**: Mandantendaten in nicht AVV-bewehrtes KI-Tool eingeführt; US-Cloud ohne TIA; Verstoß § 203 StGB sichtbar; aktuelle Beschwerde Rechtsanwaltskammer.
- **Gelb**: AVV vorhanden, aber TOM-Anlage fehlt; KI-Tool ohne dokumentierte Klassifizierung; Schulungsnachweis Art. 4 KI-VO offen.
- **Grün**: AVV + TOM + ggf. SCC + TIA; dokumentierte KI-Klassifizierung; Schulung; intern verabschiedete KI-Richtlinie.

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

## 2. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin berufsrecht-ki-vertragspruefung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Berufsrechtskonforme Mandantenkommunikation (Kanzlei-intern bei KI-Tool-Prüfung)
- **Adressat:** Kanzleileitung / Partnerschaft / IT-Leitung / DSB.
- **Sachstand kurz:** Tool, Anbieter, Hosting, geplanter Einsatzbereich, betroffene Datenarten.
- **Bewertung:** Schweigepflicht (§ 203 StGB, § 43e BRAO bzw. § 62a StBerG, § 50a WPO, § 26a BNotO), AVV-Vollständigkeit, Drittlandstransfer (DPF/SCC/TIA).
- **Empfehlung:** Freigabe ja/nein/bedingt mit konkreten Auflagen (z. B. "ohne Mandantendaten", "nur intern", "nach Nachverhandlung AVV-Klausel X").
- **Risikoampel:** Rot/Gelb/Grün mit Begründung.
- **Frist und Verantwortlicher:** wer entscheidet final, wann.

## Externe Mandantenkommunikation (wenn KI-Einsatz im Mandat erfolgt)
- **Aufklärungstextbaustein für Mandatsvereinbarung** mit Hinweis auf KI-Nutzung, Anbieter, Datenfluss.
- **Ggf. Einwilligungsformular** bei besonders sensiblen Datenarten oder fehlender Anonymisierung.

## Praxis-Tipp
Die berufsrechtliche Aufklärungspflicht über KI-Einsatz wird in Rechtsprechung und Standesvertretung noch diskutiert — vorsichtig sein und im Zweifel transparent kommunizieren. Die berufsrechtliche KI-Debatte zur KI-Nutzung in Kanzleien (frei zugänglich auf anwaltverein.de) gibt eine Orientierung, ist aber nicht bindend.

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

## 3. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin berufsrecht-ki-vertragspruefung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Red-Team-Prüfpunkte Berufsrecht-KI
1. **Schweigepflicht-Trias:** § 203 StGB + § 43a Abs. 2 / § 43e BRAO (bzw. § 62a StBerG, § 50a WPO, § 26a BNotO) + AVV Art. 28 DSGVO — alle drei adressiert?
2. **Mitwirkenden-Klausel:** Wurde § 203 Abs. 4 StGB im AVV ausdrücklich umgesetzt? Verpflichtung des Anbieter-Personals?
3. **Datenkategorien:** Werden tatsächlich Mandantendaten verarbeitet? Selbst Metadaten (Mandantenname, Aktenzeichen, Verfahrensart) können Schweigepflicht-relevant sein.
4. **Drittlandstransfer:** Bei US-Cloud DPF-Status (zum Zeitpunkt der Prüfung), SCC-Modul, TIA dokumentiert? Cloud Act-Risiko beschrieben?
5. **Konkretisierung:** Welches konkrete KI-Tool, welche konkrete Funktion? Pauschalfreigaben sind berufsrechtlich nicht haltbar.
6. **Aufklärung Mandant:** Falls erforderlich (Sensibelheit, Marktstandards): Hinweis in Mandatsvereinbarung oder gesondertes Schreiben?
7. **Halluzinations-Check:** Keine erfundenen BGH-Az. (Zivilrechtsweg) oder AnwG-Entscheidungen; keine Vermischung BRAO/BGB/StGB.

## Praxis-Tipp
Die zentrale Empfehlung für KI-Vertragsprüfung bei Berufsträgern: Kategorisiere zuerst die Datenarten (a) keine Mandantendaten, b) anonymisierte/pseudonymisierte Mandantendaten, c) identifizierbare Mandantendaten). Für (c) reicht Standard-AVV nicht — es braucht zusätzlich die Mitwirkenden-Verpflichtung nach § 203 Abs. 4 StGB und ggf. Mandanteneinwilligung. Default für (c) bei US-Cloud: nicht freigeben.

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
