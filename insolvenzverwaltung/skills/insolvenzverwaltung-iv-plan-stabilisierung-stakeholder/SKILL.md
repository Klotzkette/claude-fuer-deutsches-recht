---
name: insolvenzverwaltung-iv-plan-stabilisierung-stakeholder
description: "IV Plan Stabilisierung Stakeholder: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Plan Stabilisierung Stakeholder

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Plan Stabilisierung Stakeholder** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-plan-stabilisierung-starug` | StaRUG-Stabilisierungsmassnahmen und Vollstreckungssperre beantragen wenn Vollstreckungsdruck die Sanierung gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit Gläubiger Dauer Verlaengerung Insolvenznaehe Organpflichten. Output: Stabilisierungsantrag Betroffenenliste Verhältnismäßigkeitsnotiz. Abgrenzung: nicht für Insolvenzantragsstellung oder Schutzschirmverfahren. |
| `iv-plan-stakeholder-kommunikation` | Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO Planeroerterung §§ 17 20 StaRUG Gläubigerinfo. Prüfraster: Stakeholdergruppen Sorgen Botschaften Q and A One-Pager Terminskript. Output: Kommunikationsmatrix Gläubiger-Q-A Terminskript. Abgrenzung: nicht für Gerichtsschriftsaetze (iv-plan-gerichtliche-schritte). |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Plan Stabilisierung Stakeholder**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-plan-stabilisierung-starug`

**Fokus:** StaRUG-Stabilisierungsmassnahmen und Vollstreckungssperre beantragen wenn Vollstreckungsdruck die Sanierung gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit Gläubiger Dauer Verlaengerung Insolvenznaehe Organpflichten. Output: Stabilisierungsantrag Betroffenenliste Verhältnismäßigkeitsnotiz. Abgrenzung: nicht für Insolvenzantragsstellung oder Schutzschirmverfahren.

# IV-integrierte StaRUG-Stabilisierung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IV-integrierte StaRUG-Stabilisierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Zeit kaufen, ohne die Planroute zu beschädigen. Der Skill ist vollständig in das Insolvenzverwaltungs-Plugin integriert, arbeitet innerhalb dieses ZIPs freistehend und setzt keine weiteren Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

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

## 2. `iv-plan-stakeholder-kommunikation`

**Fokus:** Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO Planeroerterung §§ 17 20 StaRUG Gläubigerinfo. Prüfraster: Stakeholdergruppen Sorgen Botschaften Q and A One-Pager Terminskript. Output: Kommunikationsmatrix Gläubiger-Q-A Terminskript. Abgrenzung: nicht für Gerichtsschriftsaetze (iv-plan-gerichtliche-schritte).

# IV-integrierte Stakeholder-Kommunikation

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IV-integrierte Stakeholder-Kommunikation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Akzeptanz für den Plan organisieren. Der Skill ist vollständig in das Insolvenzverwaltungs-Plugin integriert, arbeitet innerhalb dieses ZIPs freistehend und setzt keine weiteren Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

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
