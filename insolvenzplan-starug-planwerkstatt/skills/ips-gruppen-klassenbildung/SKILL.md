---
name: ips-gruppen-klassenbildung
description: "Ips Gruppen Klassenbildung / Ips Insolvenzplan Architektur / Ips Integrierte Planung: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Ips Gruppen Klassenbildung / Ips Insolvenzplan Architektur / Ips Integrierte Planung

## Arbeitsbereich

Dieser Skill bündelt **Ips Gruppen Klassenbildung / Ips Insolvenzplan Architektur / Ips Integrierte Planung**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ips-gruppen-klassenbildung` | Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden. §§ 222 223 InsO §§ 9 10 StaRUG Klassenbildung. Prüfraster: Rechtsstellung Absonderung Insolvenzgläubiger Nachrang Anteilsinhaber Gruppeninterne wirtschaftliche Interessen Gleichbehandlung. Output: Gruppenmatrix Klassenmatrix Kriterienbegrundung. Abgrenzung: nicht für Abstimmungssimulation (ips-abstimmung-mehrheiten). |
| `ips-insolvenzplan-architektur` | Vollständigen Insolvenzplan nach §§ 217 ff. InsO strukturieren und alle Pflichtbestandteile verbinden. §§ 217 220 221 InsO Planarchitektur §§ 222 229 InsO Gruppen und Anlagen. Prüfraster: Planvorlageberechtigung darstellender gestaltender Teil Anlagen Gruppen Sicherheiten Planvollzug Überwachung. Output: Insolvenzplan-Skelett Bausteinliste Schnittstellenrisiken. Abgrenzung: nicht für StaRUG-Plan (ips-starug-plan-architektur). |
| `ips-integrierte-planung` | Integrierte Planrechnung aus GuV Liquiditaet und Bilanz für Insolvenzplan oder StaRUG erstellen. §§ 220 229 InsO §§ 14 StaRUG Finanzplanung. Prüfraster: Ist-Zahlen Planannahmen Base-Case Stressszenarien Brückenrechnung Annahmenregister Konsistenz. Output: Planungsmodell als CSV-Struktur Szenariovergleich. Abgrenzung: nicht für Vergleichsrechnung (ips-vergleichsrechnung). |

## Arbeitsweg

Für **Ips Gruppen Klassenbildung / Ips Insolvenzplan Architektur / Ips Integrierte Planung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insolvenzplan-starug-planwerkstatt` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ips-gruppen-klassenbildung`

**Fokus:** Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden. §§ 222 223 InsO §§ 9 10 StaRUG Klassenbildung. Prüfraster: Rechtsstellung Absonderung Insolvenzgläubiger Nachrang Anteilsinhaber Gruppeninterne wirtschaftliche Interessen Gleichbehandlung. Output: Gruppenmatrix Klassenmatrix Kriterienbegrundung. Abgrenzung: nicht für Abstimmungssimulation (ips-abstimmung-mehrheiten).

# Gruppen- und Klassenbildung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gruppen- und Klassenbildung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Abstimmungsarchitektur belastbar machen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Rechtsstellungen trennen: Absonderung, Insolvenzgläubiger, Nachrang, Anteilsinhaber, gruppeninterne Drittsicherheiten, StaRUG-Forderungen.
2. Wirtschaftliche Interessen prüfen: Banken, Lieferanten, Arbeitnehmer, Kleingläubiger, Gesellschafter, strategische Gläubiger, Versicherer.
3. Kriterien transparent dokumentieren und Manipulationsrisiken red-teamen.
4. Stimmrechte, Ausfälle, Sicherheitenwerte und Planwirkungen in einer Matrix abbilden.

## Ausgabe

- Gruppenmatrix
- Klassenmatrix
- Kriterienbegründung
- Stimmrechtsgrundlage

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

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — bestätigt die grundsätzliche Zulässigkeit der Gruppenbildung im StaRUG-Plan einschließlich Trennung der Aktionärsgruppe. <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — kapitalmarktrechtliche Aktionärsschadensersatzansprüche separieren (Nachrang); ggf. eigene Gruppe oder Ausschluss aus den einfachen Insolvenzforderungen.
- Konkrete BGH-/LG-Linien zur Gruppenbildung (§ 222 InsO, § 10 StaRUG: gleiche Rechte und Interessen) vor Ausgabe über dejure.org / openjur.de verifizieren.

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

## 2. `ips-insolvenzplan-architektur`

**Fokus:** Vollständigen Insolvenzplan nach §§ 217 ff. InsO strukturieren und alle Pflichtbestandteile verbinden. §§ 217 220 221 InsO Planarchitektur §§ 222 229 InsO Gruppen und Anlagen. Prüfraster: Planvorlageberechtigung darstellender gestaltender Teil Anlagen Gruppen Sicherheiten Planvollzug Überwachung. Output: Insolvenzplan-Skelett Bausteinliste Schnittstellenrisiken. Abgrenzung: nicht für StaRUG-Plan (ips-starug-plan-architektur).

# Insolvenzplan-Architektur

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzplan-Architektur` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Einen vollständigen InsO-Plan strukturieren. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Planziel, Planvorlageberechtigung, Verfahrensstand und Einreichungszeitpunkt aufnehmen.
2. Darstellenden und gestaltenden Teil mit Anlagen, Gruppen und Rechtswirkungen verzahnen.
3. Sicherheiten, Nachrang, Altmassegläubiger, Anteilsrechte und Drittsicherheiten als Fachmodule prüfen.
4. Planvollzug, Überwachung, Bedingungen und Registerfolgen vorab mitdenken.

## Ausgabe

- Insolvenzplan-Skelett
- Bausteinliste
- Schnittstellenrisiken
- Einreichungscheck

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

- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA AG) — Bestätigt die grundsätzliche Verfassungsmäßigkeit von Plänen mit Eingriff in Aktionärsrechte. <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Bei Aktiengesellschaften: kapitalmarktrechtliche Aktionärs-Schadensersatzansprüche sind nachrangig (Auswirkung auf Klassenbildung im Plan und Quotenermittlung).
- Konkrete BGH/LG-Entscheidungen zur Plan-Architektur (§§ 217 ff. InsO) vor Ausgabe über offene Quellen verifizieren.

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

## 3. `ips-integrierte-planung`

**Fokus:** Integrierte Planrechnung aus GuV Liquiditaet und Bilanz für Insolvenzplan oder StaRUG erstellen. §§ 220 229 InsO §§ 14 StaRUG Finanzplanung. Prüfraster: Ist-Zahlen Planannahmen Base-Case Stressszenarien Brückenrechnung Annahmenregister Konsistenz. Output: Planungsmodell als CSV-Struktur Szenariovergleich. Abgrenzung: nicht für Vergleichsrechnung (ips-vergleichsrechnung).

# Integrierte Planrechnung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Integrierte Planrechnung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Zahlen konsistent, nachvollziehbar und gerichtsfähig machen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Ist-Zahlen importieren und auf Stichtage normalisieren.
2. Planannahmen für Umsatz, Rohertrag, Personal, Fixkosten, Working Capital, Investitionen und Finanzierung erfassen.
3. Base Case, Plan Case, Fortführung ohne Plan, Liquidation und Stress Case anlegen.
4. Bilanzielle und liquiditätsseitige Brücken erklären, statt nur Tabellen zu liefern.

## Ausgabe

- Planungsmodell als CSV-Struktur
- Annahmenregister
- Szenariovergleich
- Sensitivitätenliste

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
