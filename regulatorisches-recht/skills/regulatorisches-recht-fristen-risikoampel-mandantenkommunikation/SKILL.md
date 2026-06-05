---
name: regulatorisches-recht-fristen-risikoampel-mandantenkommunikation
description: "Fristen Risikoampel Mandantenkommunikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fristen Risikoampel Mandantenkommunikation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Fristen Risikoampel Mandantenkommunikation** im Plugin Regulatorisches Recht (Sektoren). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin regulatorisches-recht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin regulatorisches-recht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin regulatorisches-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

Im Plugin Regulatorisches Recht (Sektoren) gilt für **Fristen Risikoampel Mandantenkommunikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin regulatorisches-recht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin regulatorisches-recht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Regulatorische Sektoren — typische Fristen und Sanktionsrahmen (live verifizieren)

- **DSGVO (VO 2016/679):** Meldepflicht Datenpannen 72 Stunden (Art. 33); Auskunftsrecht innerhalb eines Monats (Art. 12 Abs. 3); Bußgeld bis 20 Mio. Euro oder 4 % weltweiter Jahresumsatz (Art. 83 Abs. 5).
- **AI Act / KI-VO (VO 2024/1689):** Stufenweises Inkrafttreten 2024–2027; Verbote bereits 2 Monate nach Inkrafttreten anwendbar; Hochrisiko-Systeme Compliance-Pflichten ab 2026; Bußgeld bis 35 Mio. Euro oder 7 % Jahresumsatz.
- **DSA (VO 2022/2065):** Anwendbar seit 17.02.2024 (für VLOP/VLOSE bereits seit 25.08.2023); Transparenzberichte halbjährlich; Bußgeld bis 6 % Jahresumsatz.
- **NIS-2 (RL 2022/2555) — Umsetzung NIS2UmsuCG:** Meldung erheblicher Cybersicherheitsvorfälle 24h Erstmeldung, 72h Update, 1 Monat Abschlussbericht; Bußgeld bis 10 Mio. Euro oder 2 % Jahresumsatz (Essential entities).
- **GwG/AML:** Meldepflicht "unverzüglich" bei Geldwäscheverdacht (§ 43 GwG); jährliche Risikoanalyse; Bußgelder bis 1 Mio. Euro oder 2-faches wirtschaftlichen Vorteils.
- **MaRisk / MaComp (BaFin):** Sofortige Meldung wesentlicher Vorfälle; Outsourcing-Anzeigepflicht; jährliche Selbstbeurteilung.
- **Produktsicherheit (ProdSG, GPSR VO 2023/988):** Meldung gefährliches Produkt unverzüglich, max. 2 Tage; Rückrufkampagne dokumentationspflichtig.
- **Praxis-Tipp:** Multijurisdiktionale Regulatoren häufig parallel zuständig (z. B. BaFin + BNetzA + LfDI + EU-Kommission) — Anzeige-Kanäle und Sprachfassungen früh abstimmen.

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

**Fokus:** Mandantenkommunikation im Plugin regulatorisches-recht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin regulatorisches-recht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Regulatorische Mandantenkommunikation — Spezifika

- **C-Suite-Adressaten:** Vorstand, Compliance, Datenschutzbeauftragte, Geschäftsführung; jede Rolle braucht andere Tiefe — Executive-Summary plus Anlagen mit Detail.
- **Eskalationsstufen abstufen:** Bei BaFin/BSI/BfDI-Anfragen geht es zuerst um Frist und Tonart; Behörde nicht mit unaufgefordertem Mehrmaterial überladen, aber Anhörungspflicht (§ 28 VwVfG) wahrnehmen.
- **Pflicht zur unverzüglichen Meldung vs. anwaltliche Beratung:** DSGVO Art. 33 (72h Datenpanne), NIS-2 (24h Initial), GwG § 43 ("unverzüglich") — interne Beratung darf Meldepflicht nicht unzulässig verzögern.
- **Reputation und Veröffentlichung:** Sanktionsbescheide werden regelmäßig veröffentlicht (z. B. BaFin §§ 60a, 60b KWG; BfDI im Tätigkeitsbericht). Kommunikationsstrategie mit PR/Investor Relations koordinieren.
- **Verfahrensrechte sichern:** Anhörung, Akteneinsicht (§ 29 VwVfG), Rechtsmittel (§§ 68 ff., 80 ff. VwGO bzw. § 71 GWB für Kartellbescheide); Rechtsbehelfsbelehrungen genau prüfen.
- **Sie-Form, sachlich; keine spekulativen Garantien:** Pflicht zur Information über Risiken (§ 49b BRAO, § 11 BORA); RVG-Hinweis Pflicht.

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

**Fokus:** Red-Team Qualitygate im Plugin regulatorisches-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin regulatorisches-recht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Regulatorische Red-Team-Checks

- **Zuständigkeitscluster:** Welcher Regulator ist primär, welcher subsidiär? Bei mehreren parallel zuständigen Behörden (BaFin + LfDI bei DSGVO im Finanzsektor; BNetzA + BSI bei TK/Cybersicherheit; EU-Kommission + nationale Behörden bei DMA-Gatekeepern) — Kollision/Vorrang prüfen.
- **Anwendungsrang:** EU-Verordnung > EU-Richtlinie (mit Umsetzungsgesetz) > nationales Gesetz; bei Konflikt unionsrechtskonforme Auslegung, sonst Anwendungsvorrang (EuGH C-6/64).
- **Schwellenwerte verifizieren:** AI Act, DSA, NIS-2 haben individuell unterschiedliche Schwellen — kein Modellwissen ohne Live-Quelle. CSRD-Schwellen sind anders als CSDDD-Schwellen.
- **Übergangsfristen:** Bei AI Act, DORA, NIS-2, CSRD gibt es gestaffelte Anwendungstermine — vor Aussage konkretes Inkrafttreten je Pflichtenbereich prüfen.
- **Sanktionsmodell:** Verwaltungsbußgeld vs. Strafbarkeit vs. zivilrechtliche Haftung; bei mehreren Regimen Kumulation und Doppelbestrafungsverbot (Art. 50 GRCh, ne bis in idem; EuGH C-117/20 bpost SA, sofern frei verifizierbar).
- **Veröffentlichung:** Bei Sanktionen häufig Veröffentlichungspflicht (Pillory-Effekt); Reputationsrisiko separat bewerten.
- **Kein erfundenes Aktenzeichen:** EuGH-/EuG-Az., BaFin-/BNetzA-Bescheid-Az., DSK-Beschluss-Az. immer live verifizieren.

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
