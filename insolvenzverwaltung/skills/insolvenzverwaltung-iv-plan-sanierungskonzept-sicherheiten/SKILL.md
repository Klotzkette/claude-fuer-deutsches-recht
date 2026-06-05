---
name: insolvenzverwaltung-iv-plan-sanierungskonzept-sicherheiten
description: "IV Plan Sanierungskonzept Sicherheiten: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Plan Sanierungskonzept Sicherheiten

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Plan Sanierungskonzept Sicherheiten** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-plan-sanierungskonzept` | Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Unternehmenslage, Krisenstadium, Krisenursachen, Leitbild, Maßnahmenpakete, Stakeholderbeiträge, integrierte GuV-/Bilanz-/Liquiditätsplanung, Dokumentation und Plausibilitätsbrücken. Output: Sanierungskonzept-Gliederung, Maßnahmenplan, Lückenliste, Management Summary. Abgrenzung: Detailmodellierung in iv-plan-integrierte-planung; Sanierungsfähigkeits-Gate in iv-idw-s6-sanierungsfaehigkeit-gate. |
| `iv-plan-sicherheiten-drittsicherheiten` | Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO Absonderung § 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister Eingriffsbeschreibung Ausfallwertrechnung Finanzsicherheiten unzulässige Eingriffe. Output: Sicherheitenregister Ausfallwertrechnung Drittsicherheitenmodul. Abgrenzung: nicht für allgemeine Gruppenbildung. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Plan Sanierungskonzept Sicherheiten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-plan-sanierungskonzept`

**Fokus:** Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Unternehmenslage, Krisenstadium, Krisenursachen, Leitbild, Maßnahmenpakete, Stakeholderbeiträge, integrierte GuV-/Bilanz-/Liquiditätsplanung, Dokumentation und Plausibilitätsbrücken. Output: Sanierungskonzept-Gliederung, Maßnahmenplan, Lückenliste, Management Summary. Abgrenzung: Detailmodellierung in iv-plan-integrierte-planung; Sanierungsfähigkeits-Gate in iv-idw-s6-sanierungsfaehigkeit-gate.

# Sanierungskonzept für Insolvenzplan und StaRUG

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungskonzept für Insolvenzplan und StaRUG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Das wirtschaftliche Fundament des Plans herstellen. Der Skill baut aus Zahlen, Maßnahmen, Krisenursachen und Stakeholderbeiträgen ein Sanierungskonzept, das als Grundlage für Insolvenzplan, StaRUG, Eigenverwaltung oder Schutzschirm genutzt werden kann. Er arbeitet innerhalb dieses ZIPs freistehend und setzt keine weiteren Plugins voraus.

Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an. Bei hohem Risiko wird zuerst `iv-idw-s6-sanierungsfaehigkeit-gate` vorgeschlagen, damit nicht aus einer lückenhaften Planung versehentlich ein belastbares Konzept gemacht wird.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. **Auftrag und Verwendungszweck klären:** Wer braucht das Konzept, wofür, mit welchem Stichtag und welcher Verbindlichkeit?
2. **Unternehmenslage erfassen:** rechtliche Struktur, wirtschaftliche Ausgangslage, Vermögens-, Finanz- und Ertragslage, Steuer-/SV-Risiken, Datenstand.
3. **Krisenstadium und Krisenursachen trennen:** Symptome nicht mit Ursachen verwechseln; Liquiditätsdruck, Ergebniskrise und strategische Krise getrennt darstellen.
4. **Leitbild des sanierten Unternehmens formulieren:** Zielgeschäftsmodell, Marktposition, Ertragslogik, Organisation, Finanzierung und Risikoprofil.
5. **Maßnahmenpakete bauen:** Maßnahme, Ursache, Eigentümer, Kosten, Wirkung, Timing, Abhängigkeiten, Belegstatus.
6. **Integrierte Planung anbinden:** GuV, Bilanz und Liquidität müssen rechnerisch geschlossen sein; reine Cash-Sicht reicht nicht.
7. **Sanierungsfähigkeit bewerten:** positive Fortbestehensprognose plus nachhaltige Wettbewerbs- und Renditefähigkeit.
8. **Dokumentation herstellen:** Quellen, Annahmen, Rechenwege, Planversionen und offene Punkte so dokumentieren, dass Dritte den Arbeitsstand nachvollziehen können.

## Ausgabe

- Sanierungskonzept-Gliederung
- Maßnahmenplan
- Plausibilitäts- und Lückenliste
- Management Summary
- Datenanforderung
- Red-Team-Fragen für Gericht, Gläubigerausschuss, Banken und opponierende Gläubiger

## Gliederung für das Konzept

1. Auftrag, Stichtag, Rolle und Verwendungszweck.
2. Kurzfazit mit Go/Conditional Go/No-go.
3. Unternehmensprofil und Datenbasis.
4. Aktuelle Vermögens-, Finanz- und Ertragslage.
5. Insolvenzrechtliche Lage: §§ 17, 18, 19 InsO, Antragspflichten, Zahlungsverbote.
6. Krisenstadium und Krisenursachen.
7. Leitbild des sanierten Unternehmens.
8. Maßnahmenprogramm mit Verantwortlichen, Timing, Kosten und Wirkung.
9. Integrierte Planung: GuV, Bilanz, Liquidität, Working Capital, Finanzierung.
10. Szenarien, Sensitivitäten und Mindestliquidität.
11. Stakeholderbeiträge und rechtliche Umsetzung.
12. Ergebnis zur Sanierungsfähigkeit.
13. Monitoring, Covenants, Berichtstakt und Planvollzug.
14. Anlagen-, Quellen- und Annahmenregister.

## Leitbild und Maßnahmen verzahnen

Das Leitbild muss so konkret sein, dass jede Maßnahme daran gemessen werden kann:

- Welche Produkte oder Dienstleistungen bleiben Kern des sanierten Geschäfts?
- Welche Kunden, Regionen und Vertriebskanäle tragen den Plan?
- Welche Kostenbasis und welche Marge sind nach der Sanierung erreichbar?
- Welche Organisation, Geschäftsleitung, IT und Kontrolle sind erforderlich?
- Welche Finanzierung und Kapitalstruktur trägt das Zielbild?
- Welche Abhängigkeiten oder Transformationsrisiken bleiben?

Maßnahmen ohne Bezug zu Krisenursache und Leitbild werden als `nicht tragend` markiert.

## Integrierte Planung als Pflichtbrücke

Das Konzept muss seine Maßnahmen in Zahlen übersetzen:

- **GuV:** Umsatz, Rohertrag, Personal, sonstige Kosten, Zinsen, Steuern, Ergebnis.
- **Bilanz:** Working Capital, Anlagevermögen, Rückstellungen, Verbindlichkeiten, Eigenkapital.
- **Liquidität:** direkte Ein- und Auszahlungen, Linien, Tilgungen, Mindestliquidität, Engpassmonate.
- **Brücken:** Jahresergebnis ins Eigenkapital, Working Capital in Cashflow, Finanzierungsmaßnahmen in Bilanz und Zinslast.
- **Szenarien:** Base Case plus plausible Downside; bei hoher Unsicherheit zusätzliche Sensitivität zu Umsatz, Marge, Forderungseinzug, Maßnahmenverzug.

Bei kleineren Unternehmen ist eine schlankere Darstellung zulässig. Die Kernlogik bleibt aber erhalten: Ausgangslage, Ursachen, Leitbild, Maßnahmen, integrierte Planung, Ergebnis und Dokumentation.

## Qualitätsgates

- Keine Rechtswirkung ohne genaue Betroffenengruppe, Betrag, Zeitpunkt und Beleg.
- Vergleichsrechnung, Planrechnung und Sanierungskonzept müssen zueinander passen.
- Annahmen, Schätzungen und fehlende Quellen werden sichtbar markiert.
- Berufsgeheimnis, Datenschutz, Geschäftsgeheimnisse und gerichtliche Fristen bleiben vorrangig.
- Positive Fortbestehensprognose nicht mit voller Sanierungsfähigkeit verwechseln.
- Einmalige Liquiditätshilfe nicht als nachhaltige Sanierung behandeln.
- Steuer-, Sozialversicherungs-, Zins- und Working-Capital-Effekte nicht aus der Planung herauslassen.
- Maßnahmen nur als tragend werten, wenn Status, Verantwortlicher, Zeitpunkt und Nachweis erkennbar sind.

## Rückfragen

Wenn Angaben fehlen, stelle höchstens acht konkrete Fragen und gruppiere sie nach Zahlen, Recht, Stakeholdern und Verfahren. Bei Eilfällen liefere zuerst eine Minimalroute mit Stoppern.

## Arbeitsstil

Freundlich, ruhig, präzise und planarchitektonisch. Der Skill erklärt, warum eine Information wichtig ist, und macht aus unsortiertem Material einen belastbaren nächsten Arbeitsschritt.

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (IV-Insolvenzplan)

§ 217 InsO (Plan-Option) → § 218 InsO (Vorlage durch IV) → §§ 220-221 InsO (Plan-Inhalte) → § 222 InsO (Gruppenbildung) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Bestaetigung) → § 254 InsO (Wirkung) → §§ 49-51 InsO (Absonderungsrechte in Plan)

## Triage — IV-Plan

Bevor losgelegt wird, klaere:
1. **Plan sinnvoller als Liquidation?** Vergleichsrechnung: Plan-Quote vs. Liquidationsquote.
2. **Gruppenbildung konsistent?** § 222 InsO: gesicherte, nicht gesicherte, Kleinglaeubieger, Arbeitnehmer.
3. **Mehrheiten realistisch?** Simulation Kopf- + Summenmehrheit je Gruppe.
4. **Cramdown-Szenario?** § 245 InsO: ablehnende Gruppe ueberstimmbar wenn Best-Interest-Test bestanden.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## IV-Einordnung

Diese integrierte Fassung ist fuer Insolvenzverwalter, Sachwalter und voraeufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfaehigkeit gegenueber Gericht und Glaeubigerausschuss sowie Planvollzugsfaehigkeit.

## Anschluss

- `iv-idw-s6-sanierungsfaehigkeit-gate` — Tragfähigkeit und Lücken vor Freigabe prüfen.
- `iv-plan-integrierte-planung` — GuV-/Bilanz-/Liquiditätsplanung modellieren.
- `iv-plan-vergleichsrechnung` — Planfall gegen Liquidationsszenario rechnen.
- `iv-plan-redteam-qualitygate` — Plan vor Einreichung hart testen.

## 2. `iv-plan-sicherheiten-drittsicherheiten`

**Fokus:** Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO Absonderung § 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister Eingriffsbeschreibung Ausfallwertrechnung Finanzsicherheiten unzulässige Eingriffe. Output: Sicherheitenregister Ausfallwertrechnung Drittsicherheitenmodul. Abgrenzung: nicht für allgemeine Gruppenbildung.

# IV-integrierte Sicherheiten und Drittsicherheiten

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IV-integrierte Sicherheiten und Drittsicherheiten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Besicherte Positionen planfest und wertklar behandeln. Der Skill ist vollständig in das Insolvenzverwaltungs-Plugin integriert, arbeitet innerhalb dieses ZIPs freistehend und setzt keine weiteren Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

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

## IV-Einordnung

Diese integrierte Fassung ist für Insolvenzverwalter, Sachwalter und vorläufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfähigkeit gegenüber Gericht und Gläubigerausschuss, Rollenreinheit, Dokumentation von Belegen und spätere Planvollzugsfähigkeit.

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (IV-Insolvenzplan)

§ 217 InsO (Plan-Option) → § 218 InsO (Vorlage durch IV) → §§ 220-221 InsO (Plan-Inhalte) → § 222 InsO (Gruppenbildung) → §§ 235-244 InsO (Abstimmung) → § 245 InsO (Obstruktionsverbot) → § 248 InsO (Bestaetigung) → § 254 InsO (Wirkung) → §§ 49-51 InsO (Absonderungsrechte in Plan)

## Triage — IV-Plan

Bevor losgelegt wird, klaere:
1. **Plan sinnvoller als Liquidation?** Vergleichsrechnung: Plan-Quote vs. Liquidationsquote.
2. **Gruppenbildung konsistent?** § 222 InsO: gesicherte, nicht gesicherte, Kleinglaeubieger, Arbeitnehmer.
3. **Mehrheiten realistisch?** Simulation Kopf- + Summenmehrheit je Gruppe.
4. **Cramdown-Szenario?** § 245 InsO: ablehnende Gruppe ueberstimmbar wenn Best-Interest-Test bestanden.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## IV-Einordnung

Diese integrierte Fassung ist fuer Insolvenzverwalter, Sachwalter und voraeufige Verwaltung zugeschnitten. Sie priorisiert Masseinteresse, Berichtsfaehigkeit gegenueber Gericht und Glaeubigerausschuss sowie Planvollzugsfaehigkeit.
