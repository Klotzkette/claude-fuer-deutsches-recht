---
name: fremdgeschaeftsfuehrer-gmbh-geringfuegigkeit
description: "Fremdgeschaeftsfuehrer Gmbh Geringfuegigkeit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fremdgeschaeftsfuehrer Gmbh Geringfuegigkeit

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Fremdgeschaeftsfuehrer Gmbh Geringfuegigkeit** im Plugin Sozialversicherungsstatus Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fremdgeschaeftsfuehrer-gmbh` | Prüft Sozialversicherungsstatus eines GmbH-Fremdgeschäftsführers ohne Kapitalbeteiligung. |
| `geringfuegigkeit-minijob` | Prüft geringfügige Beschäftigung als Alternative oder Fehleinordnung zur Selbständigkeit. |
| `gesellschafter-gf-mehrheit` | Prüft beherrschenden Gesellschafter-Geschäftsführer mit Kapitalmehrheit und Statusfolgen. |
| `gitarrenlehrer-und-instrumentalunterricht` | Prüft privaten Instrumentalunterricht, Musikschulen, Räume, Schülerzuteilung und eigene Unterrichtsorganisation. |

## Arbeitsweg

Im Plugin Sozialversicherungsstatus Pruefer gilt für **Fremdgeschaeftsfuehrer Gmbh Geringfuegigkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fremdgeschaeftsfuehrer-gmbh`

**Fokus:** Prüft Sozialversicherungsstatus eines GmbH-Fremdgeschäftsführers ohne Kapitalbeteiligung.

# Fremdgeschäftsführer GmbH

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fremdgeschäftsführer GmbH` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Fremdgeschäftsführer GmbH
- **Spezialgegenstand:** Fremdgeschäftsführer GmbH wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Fremdgeschäftsführer GmbH** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- GmbHG
- BSG Geschäftsführerrechtsprechung verifizieren

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer bestellt/abberuft und wer kann Weisungen erteilen?
- Gibt es Alleinvertretung, Befreiung § 181 BGB oder faktische Autonomie und wie stark wiegt sie?
- Besteht Unternehmerrisiko oder nur Organstellung mit Gehalt?
- Welche Gesellschaftsdokumente belegen die Machtverteilung?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer bestellt/abberuft und wer kann Weisungen erteilen?
- Gibt es Alleinvertretung, Befreiung § 181 BGB oder faktische Autonomie und wie stark wiegt sie?
- Besteht Unternehmerrisiko oder nur Organstellung mit Gehalt?
- Welche Gesellschaftsdokumente belegen die Machtverteilung?

**Mindest-Output:** Fremd-GF-Statusmemo mit Organstellung, Weisungsrechten, Vergütung und Risiko.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 2. `geringfuegigkeit-minijob`

**Fokus:** Prüft geringfügige Beschäftigung als Alternative oder Fehleinordnung zur Selbständigkeit.

# Geringfügigkeit und Minijob

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Geringfügigkeit und Minijob` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Geringfügigkeit und Minijob
- **Spezialgegenstand:** Geringfügigkeit und Minijob wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Geringfügigkeit und Minijob** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 8
- Minijob-Regeln live prüfen

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Liegt Beschäftigung vor, aber nur geringfügig?
- Welche Entgeltgrenzen und Zeitgrenzen gelten aktuell?
- Ist die Tätigkeit regelmäßig, vorhersehbar oder kurzfristig?
- Welche Meldungen und Pauschalbeiträge sind nötig?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Liegt Beschäftigung vor, aber nur geringfügig?
- Welche Entgeltgrenzen und Zeitgrenzen gelten aktuell?
- Ist die Tätigkeit regelmäßig, vorhersehbar oder kurzfristig?
- Welche Meldungen und Pauschalbeiträge sind nötig?

**Mindest-Output:** Minijob-Check mit Entgelt/Zeit, Meldung und Abgrenzung.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 3. `gesellschafter-gf-mehrheit`

**Fokus:** Prüft beherrschenden Gesellschafter-Geschäftsführer mit Kapitalmehrheit und Statusfolgen.

# Mehrheits-Gesellschafter-Geschäftsführer

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mehrheits-Gesellschafter-Geschäftsführer` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Mehrheits-Gesellschafter-Geschäftsführer
- **Spezialgegenstand:** Mehrheits-Gesellschafter-Geschäftsführer wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Mehrheits-Gesellschafter-Geschäftsführer** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- GmbHG Stimmrechte
- BSG nur verifiziert

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Kann der GF ihm unangenehme Beschlüsse kraft Beteiligung verhindern?
- Welche Satzungsmehrheiten gelten für Weisung, Abberufung, Geschäftsordnung und Gewinn?
- Sind Stimmrechtsbindungen oder Sonderrechte relevant?
- Welche Änderungen der Beteiligung verändern den Status?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Kann der GF ihm unangenehme Beschlüsse kraft Beteiligung verhindern?
- Welche Satzungsmehrheiten gelten für Weisung, Abberufung, Geschäftsordnung und Gewinn?
- Sind Stimmrechtsbindungen oder Sonderrechte relevant?
- Welche Änderungen der Beteiligung verändern den Status?

**Mindest-Output:** Mehrheits-GF-Prüfung mit Stimmrechtsmacht, Satzung und Statusfolge.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 4. `gitarrenlehrer-und-instrumentalunterricht`

**Fokus:** Prüft privaten Instrumentalunterricht, Musikschulen, Räume, Schülerzuteilung und eigene Unterrichtsorganisation.

# Gitarrenlehrer und Instrumentalunterricht

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gitarrenlehrer und Instrumentalunterricht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Gitarrenlehrer und Instrumentalunterricht
- **Spezialgegenstand:** Gitarrenlehrer und Instrumentalunterricht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Gitarrenlehrer und Instrumentalunterricht** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- SGB VI § 2
- SGB IV § 127

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer akquiriert Schüler und legt Preise fest?
- Wer stellt Räume, Instrumente, Stundenplan, Vertretung und Unterrichtsmaterial?
- Ist Unterricht pädagogisch frei oder institutionell eingebunden?
- Welche Rentenversicherungspflicht kann trotz Selbständigkeit bestehen?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer akquiriert Schüler und legt Preise fest?
- Wer stellt Räume, Instrumente, Stundenplan, Vertretung und Unterrichtsmaterial?
- Ist Unterricht pädagogisch frei oder institutionell eingebunden?
- Welche Rentenversicherungspflicht kann trotz Selbständigkeit bestehen?

**Mindest-Output:** Instrumentallehrer-Check mit Eingliederung, eigener Marktposition und SGB-VI-Pflicht.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.
