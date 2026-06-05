---
name: insolvenzplan-starug-ips-redteam-qualitygate-sanierungskonzept
description: "IPS Redteam Qualitygate Sanierungskonzept: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IPS Redteam Qualitygate Sanierungskonzept

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **IPS Redteam Qualitygate Sanierungskonzept** im Plugin Insolvenzplan / StaRUG. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ips-redteam-qualitygate` | Insolvenzplan oder StaRUG-Plan vor Einreichung aus Gegnersicht und Gerichtssicht prüfen. §§ 231 245 251 InsO Versagungsgründe § 64 StaRUG. Prüfraster: Vollständigkeit Bewertungswiderspruch Gruppenmissbrauch fehlende Anlagen unbestimmte Klauseln Bestätigungsrisiken. Output: Red-Team-Bericht Fehlerliste Heilungsliste. Abgrenzung: Quality Gate für alle ips-Skills. |
| `ips-sanierungskonzept` | Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Ausgangslage, Krisenstadium, Krisenursachen, Leitbild, Maßnahmenpakete, Stakeholderbeiträge, integrierte GuV-/Bilanz-/Liquiditätsplanung, Szenarien und Dokumentation. Output: Sanierungskonzept-Gliederung, Maßnahmenplan, Plausibilitätsfragen, Lückenliste. Abgrenzung: nicht für integrierte Finanzplanung (ips-integrierte-planung). |
| `ips-sicherheiten-drittsicherheiten` | Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO §§ 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister Eingriffsbeschreibung Ausfallwertrechnung gruppeninterne Drittsicherheiten Finanzsicherheiten Eingriffsstopper. Output: Sicherheitenregister Ausfallwertrechnung Drittsicherheitenmodul. Abgrenzung: nicht für allgemeine Gruppenbildung. |

## Arbeitsweg

Im Plugin Insolvenzplan / StaRUG gilt für **IPS Redteam Qualitygate Sanierungskonzept**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ips-redteam-qualitygate`

**Fokus:** Insolvenzplan oder StaRUG-Plan vor Einreichung aus Gegnersicht und Gerichtssicht prüfen. §§ 231 245 251 InsO Versagungsgründe § 64 StaRUG. Prüfraster: Vollständigkeit Bewertungswiderspruch Gruppenmissbrauch fehlende Anlagen unbestimmte Klauseln Bestätigungsrisiken. Output: Red-Team-Bericht Fehlerliste Heilungsliste. Abgrenzung: Quality Gate für alle ips-Skills.

# Red Team und Quality Gate

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Red Team und Quality Gate` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Den Plan vor Gegnern und Gericht hart prüfen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Plan wie ein opponierender Gläubiger, Gericht und Investor lesen.
2. Klarheit, Vollständigkeit, Widerspruchsfreiheit, Bestimmtheit, Anlagen, Zahlenbrücken und Offenlegung prüfen.
3. Top-Fehler, Heilungsvorschläge, Risiko nach Schwere und verantwortliche Person ausgeben.
4. Freigabe erst empfehlen, wenn kritische Punkte bearbeitet oder bewusst akzeptiert sind.

## Ausgabe

- Red-Team-Bericht
- Fehlerliste
- Heilungsliste
- Go/No-go-Vermerk

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

## 2. `ips-sanierungskonzept`

**Fokus:** Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Ausgangslage, Krisenstadium, Krisenursachen, Leitbild, Maßnahmenpakete, Stakeholderbeiträge, integrierte GuV-/Bilanz-/Liquiditätsplanung, Szenarien und Dokumentation. Output: Sanierungskonzept-Gliederung, Maßnahmenplan, Plausibilitätsfragen, Lückenliste. Abgrenzung: nicht für integrierte Finanzplanung (ips-integrierte-planung).

# Sanierungskonzept

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungskonzept` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Das wirtschaftliche Fundament des Plans herstellen. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Auftrag, Stichtag, Verfahrensroute und Adressat klären.
2. Unternehmenslage und Datenbasis erfassen: Recht, Wirtschaft, Steuern, Vermögen, Finanzierung, Ergebnis.
3. Krisenstadium, Ursachen und Managementmaßnahmen trennen.
4. Leitbild des sanierten Unternehmens, Marktannahmen, Ertragslogik, Organisation und Liquiditätslogik formulieren.
5. Maßnahmenpakete mit Verantwortlichen, Wirkung, Kosten, Timing, Abhängigkeiten und Belegstatus erfassen.
6. Plausibilitätsbrücken zur integrierten GuV-/Bilanz-/Liquiditätsplanung und Vergleichsrechnung herstellen.
7. Fortbestehensprognose und nachhaltige Sanierungsfähigkeit getrennt bewerten.

## Ausgabe

- Sanierungskonzept-Gliederung
- Maßnahmenplan
- Plausibilitätsfragen
- Management Summary
- Datenanforderung und Lückenliste
- Sanierungsfähigkeits-Ampel

## Kernbestandteile

Ein belastbares Sanierungskonzept braucht:

1. Auftrag, Stichtag, Verwendungszweck.
2. Unternehmensprofil und Ausgangslage.
3. Vermögens-, Finanz- und Ertragslage mit belegter Datenbasis.
4. Krisenstadium und Krisenursachen.
5. Leitbild des sanierten Unternehmens.
6. Maßnahmenprogramm mit Kosten, Timing, Wirkung, Verantwortlichen und Nachweisen.
7. Integrierte Planung aus GuV, Bilanz und Liquidität.
8. Szenarien und Sensitivitäten.
9. Ergebnis zur positiven Fortbestehensprognose und zur nachhaltigen Sanierungsfähigkeit.
10. Dokumentation von Quellen, Annahmen, Planversionen und offenen Punkten.

Bei kleineren Unternehmen darf die Darstellung schlanker sein. Die Kernbestandteile entfallen dadurch nicht; sie werden nur angemessen fokussiert.

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.
- Liquidität, GuV und Planbilanz müssen rechnerisch geschlossen sein.
- Eine positive Fortbestehensprognose ersetzt nicht die Prüfung nachhaltiger Sanierungsfähigkeit.
- Maßnahmen ohne Belegstatus, Verantwortlichen und Timing sind nicht tragend.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.


## Rechtliche Grundlagen und Leitentscheidungen (Stand Mai 2026)

- IDW S 6 (Sanierungskonzept) und IDW S 11 (Insolvenzeröffnungsgründe) als methodische Mindeststandards.
- **BGH IX ZR 122/23 vom 05.12.2024** — Bei Bargeschäften im Sanierungskontext: Unlauterkeit (§ 142 Abs. 1 Hs. 2 InsO) muss konkret nachgewiesen werden; bloße Verlustsituation genügt nicht. Relevanz: Sanierungsbausteine ohne gezielte Gläubigerbenachteiligung sind anfechtungsfest. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Sanierungsversuche entkräften Vorsatz iSd § 133 InsO bei konkretem belastbarem Sanierungskonzept. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>

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

## 3. `ips-sicherheiten-drittsicherheiten`

**Fokus:** Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO §§ 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister Eingriffsbeschreibung Ausfallwertrechnung gruppeninterne Drittsicherheiten Finanzsicherheiten Eingriffsstopper. Output: Sicherheitenregister Ausfallwertrechnung Drittsicherheitenmodul. Abgrenzung: nicht für allgemeine Gruppenbildung.

# Sicherheiten und Drittsicherheiten

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sicherheiten und Drittsicherheiten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Besicherte Positionen planfest und wertklar behandeln. Der Skill arbeitet freistehend und setzt keine anderen Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Sicherheiteninventar erstellen: Gegenstand, Sicherungszweck, Rang, Wert, Verwertungsbefugnis, Drittgeber.
2. Eingriffe in Sicherheiten explizit beschreiben und Ausfallwerte nachvollziehbar schätzen.
3. Gruppeninterne Drittsicherheiten gesondert mit Auswirkungen auf Sicherungsgeber und Entschädigung prüfen.
4. Finanzsicherheiten und unzulässige Eingriffe als harte Stopper markieren.

## Ausgabe

- Sicherheitenregister
- Ausfallwertrechnung
- Drittsicherheitenmodul
- Eingriffs- und Entschädigungsvorschlag

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
