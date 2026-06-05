---
name: ips-stabilisierung-stakeholder
description: "Ips Stabilisierung Starug / Ips Stakeholder Kommunikation / Ips Starug Plan Architektur: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Ips Stabilisierung Starug / Ips Stakeholder Kommunikation / Ips Starug Plan Architektur

## Arbeitsbereich

Dieser Skill bündelt **Ips Stabilisierung Starug / Ips Stakeholder Kommunikation / Ips Starug Plan Architektur**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ips-stabilisierung-starug` | StaRUG-Stabilisierungsmassnahmen beantragen wenn Vollstreckungsdruck die Planarbeit gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit Gläubiger Dauer Insolvenznaehe Organpflichten Kommunikationslinie. Output: Stabilisierungsantrag Betroffenenliste Verhältnismäßigkeitsnotiz. Abgrenzung: nicht für Schutzschirmverfahren nach InsO. |
| `ips-stakeholder-kommunikation` | Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO §§ 17 20 StaRUG Gläubigerinfo. Prüfraster: Stakeholdergruppen Sorgen Botschaften Q and A One-Pager Terminskript ohne Überversprechungen. Output: Kommunikationsmatrix Gläubiger-Q-A Terminskript. Abgrenzung: nicht für Gerichtsschriftsaetze (ips-gerichtliche-schritte). |
| `ips-starug-plan-architektur` | Vollständigen StaRUG-Restrukturierungsplan strukturieren von Planbetroffenenauswahl bis Bestätigungspfad. §§ 6 7 8 StaRUG Planinhalt §§ 60 ff. StaRUG Abstimmung Gerichtsverfahren. Prüfraster: Restrukturierungsfähigkeit drohende ZU gestaltbare Rechtsverhältnisse Plananlagen Bestätigungsvoraussetzungen Abstimmung. Output: StaRUG-Plan-Skelett Planbetroffenenliste Anlagenpaket. Abgrenzung: nicht für InsO-Plan (ips-insolvenzplan-architektur). |

## Arbeitsweg

Für **Ips Stabilisierung Starug / Ips Stakeholder Kommunikation / Ips Starug Plan Architektur** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insolvenzplan-starug-planwerkstatt` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ips-stabilisierung-starug`

**Fokus:** StaRUG-Stabilisierungsmassnahmen beantragen wenn Vollstreckungsdruck die Planarbeit gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit Gläubiger Dauer Insolvenznaehe Organpflichten Kommunikationslinie. Output: Stabilisierungsantrag Betroffenenliste Verhältnismäßigkeitsnotiz. Abgrenzung: nicht für Schutzschirmverfahren nach InsO.

# StaRUG-Stabilisierung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `StaRUG-Stabilisierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Zeit kaufen, ohne die Planroute zu beschädigen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Stabilisierungsbedarf, Gläubigerkreis, Forderungen, Vollstreckungsdruck und Fortführungsinteresse aufnehmen.
2. Verhältnismäßigkeit, Dauer, Verlängerung, Sicherheiten und betroffene Rechte prüfen.
3. Kommunikationslinie für Banken, Lieferanten und Gericht vorbereiten.
4. Risiken bei Insolvenznähe und Organpflichten klar markieren.

## Ausgabe

- Stabilisierungsantrag
- Betroffenenliste
- Verhältnismäßigkeitsnotiz
- Kommunikationspaket

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und Leitentscheidungen (Stand Mai 2026)

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — StaRUG-Plan mit Eingriff in Aktionärsrechte verfassungsrechtlich grundsätzlich zulässig. Relevanz für Stabilisierungsanordnung (§ 49 StaRUG): Vollstreckungsschutz von bis zu drei Monaten ist verhältnismäßig, wenn die Stabilisierungsziele (Plan-Aufstellung, Verhandlung) konkret dokumentiert sind.
 <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- Restrukturierungsgerichts-Entscheidungen zu § 49 StaRUG (Stabilisierungsanordnung) und § 51 StaRUG (Voraussetzungen) vor Ausgabe über dejure.org / openjur.de verifizieren.

## Paragrafenkette (Insolvenzplan / StaRUG)

§ 217 InsO (Plan-Option) → § 218 InsO (Plan-Vorlage) → §§ 220-221 InsO (darstellender und gestaltender Teil) → § 222 InsO (Gruppen) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Planbestaetigung) → § 254 InsO (Planwirkung) → §§ 7-39 StaRUG (StaRUG-Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown)

## Triage — Plan-Vorarbeiten

Bevor losgelegt wird, klaere:
1. **Verfahrensart?** InsO-Plan (§§ 217 ff. InsO) oder StaRUG-Restrukturierungsplan (§§ 7-39 StaRUG)?
2. **Klassenbildung schluessig?** § 222 InsO / § 10 StaRUG — gleiche Rechte und Interessen je Gruppe.
3. **Mehrheits-Simulation?** Ist 75%-Schwelle (StaRUG) oder 50%+50% (InsO) realistisch?
4. **Vergleichsrechnung?** Liquidationswert als Referenz fuer Best-Interest-Test berechnen.
5. **Cramdown-Szenario?** Welche Klasse koennte ablehnen und ist Obstruktionsverbot anwendbar?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `ips-stakeholder-kommunikation`

**Fokus:** Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO §§ 17 20 StaRUG Gläubigerinfo. Prüfraster: Stakeholdergruppen Sorgen Botschaften Q and A One-Pager Terminskript ohne Überversprechungen. Output: Kommunikationsmatrix Gläubiger-Q-A Terminskript. Abgrenzung: nicht für Gerichtsschriftsaetze (ips-gerichtliche-schritte).

# Stakeholder-Kommunikation

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Stakeholder-Kommunikation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Akzeptanz für den Plan organisieren. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Stakeholdergruppen, Sorgen, Informationsstand und harte rote Linien erfassen.
2. Botschaften für Gericht, Gläubiger, Banken, Arbeitnehmer, Lieferanten und Investoren trennen.
3. Q&A, One-Pager, Terminskript und Nachfassliste erzeugen.
4. Keine ungesicherten Erfolgsversprechen, sondern transparente Planlogik kommunizieren.

## Ausgabe

- Kommunikationsmatrix
- Gläubiger-Q&A
- Terminskript
- Nachfassliste

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Insolvenzplan / StaRUG)

§ 217 InsO (Plan-Option) → § 218 InsO (Plan-Vorlage) → §§ 220-221 InsO (darstellender und gestaltender Teil) → § 222 InsO (Gruppen) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Planbestaetigung) → § 254 InsO (Planwirkung) → §§ 7-39 StaRUG (StaRUG-Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown)

## Triage — Plan-Vorarbeiten

Bevor losgelegt wird, klaere:
1. **Verfahrensart?** InsO-Plan (§§ 217 ff. InsO) oder StaRUG-Restrukturierungsplan (§§ 7-39 StaRUG)?
2. **Klassenbildung schluessig?** § 222 InsO / § 10 StaRUG — gleiche Rechte und Interessen je Gruppe.
3. **Mehrheits-Simulation?** Ist 75%-Schwelle (StaRUG) oder 50%+50% (InsO) realistisch?
4. **Vergleichsrechnung?** Liquidationswert als Referenz fuer Best-Interest-Test berechnen.
5. **Cramdown-Szenario?** Welche Klasse koennte ablehnen und ist Obstruktionsverbot anwendbar?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `ips-starug-plan-architektur`

**Fokus:** Vollständigen StaRUG-Restrukturierungsplan strukturieren von Planbetroffenenauswahl bis Bestätigungspfad. §§ 6 7 8 StaRUG Planinhalt §§ 60 ff. StaRUG Abstimmung Gerichtsverfahren. Prüfraster: Restrukturierungsfähigkeit drohende ZU gestaltbare Rechtsverhältnisse Plananlagen Bestätigungsvoraussetzungen Abstimmung. Output: StaRUG-Plan-Skelett Planbetroffenenliste Anlagenpaket. Abgrenzung: nicht für InsO-Plan (ips-insolvenzplan-architektur).

# StaRUG-Plan-Architektur

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `StaRUG-Plan-Architektur` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Einen vollständigen Restrukturierungsplan strukturieren. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Restrukturierungsfähigkeit, drohende Zahlungsunfähigkeit und gestaltbare Rechtsverhältnisse prüfen.
2. Planbetroffene auswählen und Nichtbetroffene mit Begründung dokumentieren.
3. Darstellenden Teil, gestaltenden Teil, Bestandsfähigkeitserklärung, Vermögensübersicht sowie Ergebnis- und Finanzplan verbinden.
4. Abstimmung, gerichtliche Instrumente und Bestätigungspfad planen.

## Ausgabe

- StaRUG-Plan-Skelett
- Planbetroffenenliste
- Anlagen- und Checklistenpaket
- Gerichtsroute

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und Leitentscheidungen (Stand Mai 2026)

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — Verfassungsbeschwerde von Minderheitsaktionären gegen die gerichtliche Bestätigung eines StaRUG-Restrukturierungsplans als unzulässig zurückgewiesen. Bestätigung der grundsätzlichen Verfassungsmäßigkeit von Restrukturierungsplänen mit Eingriff in Aktionärsrechte; § 66 Abs. 2 Nr. 3 StaRUG (Schlechterstellungsprüfung) als zentrale Schutznorm.
 <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- Restrukturierungsgerichts- und OLG-Entscheidungen zu StaRUG-Plan-Architektur (§§ 7–39 StaRUG: darstellender Teil, gestaltender Teil, Gruppen, Mehrheiten, Cramdown) vor Ausgabe über dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen verifizieren.

## Paragrafenkette (Insolvenzplan / StaRUG)

§ 217 InsO (Plan-Option) → § 218 InsO (Plan-Vorlage) → §§ 220-221 InsO (darstellender und gestaltender Teil) → § 222 InsO (Gruppen) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Planbestaetigung) → § 254 InsO (Planwirkung) → §§ 7-39 StaRUG (StaRUG-Plan) → § 25 StaRUG (Mehrheiten) → § 26 StaRUG (Cramdown)

## Triage — Plan-Vorarbeiten

Bevor losgelegt wird, klaere:
1. **Verfahrensart?** InsO-Plan (§§ 217 ff. InsO) oder StaRUG-Restrukturierungsplan (§§ 7-39 StaRUG)?
2. **Klassenbildung schluessig?** § 222 InsO / § 10 StaRUG — gleiche Rechte und Interessen je Gruppe.
3. **Mehrheits-Simulation?** Ist 75%-Schwelle (StaRUG) oder 50%+50% (InsO) realistisch?
4. **Vergleichsrechnung?** Liquidationswert als Referenz fuer Best-Interest-Test berechnen.
5. **Cramdown-Szenario?** Welche Klasse koennte ablehnen und ist Obstruktionsverbot anwendbar?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
