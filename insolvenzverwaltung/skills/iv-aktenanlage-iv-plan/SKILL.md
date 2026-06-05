---
name: iv-aktenanlage-iv-plan
description: "IV Aktenanlage IV Plan: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Aktenanlage IV Plan

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Aktenanlage IV Plan** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-aktenanlage-verfahrenscockpit` | Neue Verfahrensakte anlegen und Verfahrenscockpit strukturieren wenn Insolvenzverwalter oder Sachwalter bestellt wird. §§ 56 80 InsO Verwalterbestellung und Verwaltungsbefugnis. Prüfraster: Aktenzeichen Beteiligtenregister Ordnerplan Massekonto Forderungstabelle Fristen Workstreams. Output: vollständiges Verfahrens-Cockpit mit Gliederung Rollenplan und Fristenliste. Abgrenzung: nicht für laufende Berichterstattung (iv-berichte) oder Forderungsprüfung (iv-forderungsanmeldung-prüfung). |
| `iv-plan-verfahrenswahl` | Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270a 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit Überschuldung Masse Zeitfenster Eingriffstiefe Gerichtsbedarf No-go-Schwellen. Output: Routenmatrix Empfehlung Risikoampel. Abgrenzung: nicht für Detailplanung der gewaehlten Route. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Aktenanlage IV Plan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-aktenanlage-verfahrenscockpit`

**Fokus:** Neue Verfahrensakte anlegen und Verfahrenscockpit strukturieren wenn Insolvenzverwalter oder Sachwalter bestellt wird. §§ 56 80 InsO Verwalterbestellung und Verwaltungsbefugnis. Prüfraster: Aktenzeichen Beteiligtenregister Ordnerplan Massekonto Forderungstabelle Fristen Workstreams. Output: vollständiges Verfahrens-Cockpit mit Gliederung Rollenplan und Fristenliste. Abgrenzung: nicht für laufende Berichterstattung (iv-berichte) oder Forderungsprüfung (iv-forderungsanmeldung-prüfung).

# Aktenanlage und Verfahrenscockpit

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aktenanlage und Verfahrenscockpit` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Eröffnet eine saubere Verfahrensakte mit eigenem Aktenzeichen, Rollen, Ordnerplan, Tabellenlogik und Workstream-Register.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- ein neuer Beschluss, Gutachtenauftrag oder Sachwalterauftrag vorliegt
- eine unstrukturierte Datenlieferung sortiert werden muss
- bestehende Akten nicht auswertbar sind

## Eingaben

- Beschluss, Antrag, Schuldnerfragebogen
- Beteiligte, Banken, Arbeitnehmer, Sicherungsgläubiger
- erste Dokumente und Dateiliste

## Workflow

1. **Aktenkern** - Gericht, Aktenzeichen, Schuldner, Verwalterrolle, Stichtage und Fristen erfassen.
2. **Ordnung** - Ordnerplan für Gericht, Masse, Tabelle, Personal, Verträge, Anfechtung und Berichte erzeugen.
3. **Register** - Beteiligtenregister, Gläubigerliste, Drittschuldnerliste und Zustellwege anlegen.
4. **Kontrollpunkte** - Wiedervorlagen und Verantwortlichkeiten setzen.

## Ausgabe

- Mandatskarte
- Ordnerplan
- Beteiligtenregister
- Fristen- und Workstreamliste

## Qualitätsgates

- keine Partei ohne Rolle
- jede Frist mit Quelle
- keine Vermischung von Masse und Kanzleidaten

## Rote Schwellen

- fehlender Bestellungsbeschluss
- unklare Zuständigkeit
- fehlender Zahlungsweg für Massekonto

## Interne Vorlagen

- assets/templates/iv-mandatskarte.md
- assets/templates/glaeubigerausschuss-bericht.md

## Amtliche Erstquellen

- InsO Gesamtfassung
- §§ 27, 28 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `iv-plan-verfahrenswahl`

**Fokus:** Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270a 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit Überschuldung Masse Zeitfenster Eingriffstiefe Gerichtsbedarf No-go-Schwellen. Output: Routenmatrix Empfehlung Risikoampel. Abgrenzung: nicht für Detailplanung der gewaehlten Route.

# IV-integrierte Verfahrenswahl und Routenentscheidung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `IV-integrierte Verfahrenswahl und Routenentscheidung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Den passenden Sanierungsrahmen auswählen. Der Skill ist vollständig in das Insolvenzverwaltungs-Plugin integriert, arbeitet innerhalb dieses ZIPs freistehend und setzt keine weiteren Plugins voraus. Wenn Unterlagen fehlen, fragt er gezielt nach, bildet eine klar markierte Annahme oder bietet einen Simulationsstand an.

## Startet bei

- neuem Planmandat oder Sanierungsprojekt
- unvollständiger Datenlage
- Vorbereitung von Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG
- Prüfung eines vorhandenen Planentwurfs

## Geführter Workflow

1. Drohende Zahlungsunfähigkeit, Zahlungsunfähigkeit, Überschuldung, Masse, Organpflichten und Zeitfenster erfassen.
2. Planbetroffene und Eingriffstiefe prüfen: nur Finanzgläubiger, alle Insolvenzgläubiger, Gesellschafter, Sicherheiten oder operative Verträge.
3. Gerichtsbedarf prüfen: Vorprüfung, Abstimmung, Stabilisierung, Planbestätigung oder Insolvenzverfahren.
4. No-go-Schwellen markieren, insbesondere Arbeitnehmerforderungen im StaRUG, Massefähigkeit, Insolvenzantragspflichten und ungesicherte Datenlage.

## Ausgabe

- Routenmatrix
- Empfehlung mit Bedingungen
- Risikoampel
- Entscheidungsnotiz

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
