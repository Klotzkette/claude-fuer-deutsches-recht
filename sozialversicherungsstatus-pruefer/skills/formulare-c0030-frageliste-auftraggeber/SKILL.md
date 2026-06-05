---
name: formulare-c0030-frageliste-auftraggeber
description: "Formulare C0030 Frageliste Auftraggeber: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Formulare C0030 Frageliste Auftraggeber

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Formulare C0030 Frageliste Auftraggeber** im Plugin Sozialversicherungsstatus Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `formulare-c0030-v0027-v0028` | Ordnet DRV-Formulare, Tätigkeitsbeschreibungen, Verträge, Anlagen und Belege für Statusanträge. |
| `frageliste-auftraggeber` | Erstellt präzise Fragen an Auftraggeber/Unternehmen für Statusprüfung und Sanierung. |
| `frageliste-auftragnehmer` | Erstellt präzise Fragen an Auftragnehmer/Freelancer/Geschäftsführer für Statusprüfung. |
| `freie-zeiteinteilung` | Prüft Zeitsouveränität, Dienstpläne, Kernzeiten, Deadlines, Verfügbarkeit und Abwesenheitsregeln. |

## Arbeitsweg

Im Plugin Sozialversicherungsstatus Pruefer gilt für **Formulare C0030 Frageliste Auftraggeber**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `formulare-c0030-v0027-v0028`

**Fokus:** Ordnet DRV-Formulare, Tätigkeitsbeschreibungen, Verträge, Anlagen und Belege für Statusanträge.

# DRV-Formulare und Anlagen

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DRV-Formulare und Anlagen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: DRV-Formulare und Anlagen
- **Spezialgegenstand:** DRV-Formulare und Anlagen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **DRV-Formulare und Anlagen** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- DRV Formularcenter
- SGB IV § 7a

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welches Formular/Anlage ist aktuell für Auftraggeber, Auftragnehmer oder Geschäftsführer einschlägig?
- Welche Tätigkeitsbeschreibung ist konkret genug ohne nachteilig zu übertreiben?
- Welche Belege gehören dazu: Vertrag, Rechnungen, Projektplan, Organigramm, Mailpraxis?
- Welche Angaben dürfen nicht widersprüchlich sein?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welches Formular/Anlage ist aktuell für Auftraggeber, Auftragnehmer oder Geschäftsführer einschlägig?
- Welche Tätigkeitsbeschreibung ist konkret genug ohne nachteilig zu übertreiben?
- Welche Belege gehören dazu: Vertrag, Rechnungen, Projektplan, Organigramm, Mailpraxis?
- Welche Angaben dürfen nicht widersprüchlich sein?

**Mindest-Output:** Formularpaket mit Anlagenliste, Widerspruchsprüfung und Nachweisverzeichnis.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 2. `frageliste-auftraggeber`

**Fokus:** Erstellt präzise Fragen an Auftraggeber/Unternehmen für Statusprüfung und Sanierung.

# Frageliste Auftraggeber

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Frageliste Auftraggeber` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Frageliste Auftraggeber
- **Spezialgegenstand:** Frageliste Auftraggeber wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Frageliste Auftraggeber** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer steuert Tagesgeschäft und Qualität?
- Welche Systeme, Räume, Teams und Prozesse nutzt die Person?
- Welche Freiheit besteht bei Vertretung, Preisen, Arbeitszeit und Kunden?
- Welche Dokumente belegen Auftraggeberangaben?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer steuert Tagesgeschäft und Qualität?
- Welche Systeme, Räume, Teams und Prozesse nutzt die Person?
- Welche Freiheit besteht bei Vertretung, Preisen, Arbeitszeit und Kunden?
- Welche Dokumente belegen Auftraggeberangaben?

**Mindest-Output:** Auftraggeberfragebogen mit Beleganforderung und Warnhinweisen.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 3. `frageliste-auftragnehmer`

**Fokus:** Erstellt präzise Fragen an Auftragnehmer/Freelancer/Geschäftsführer für Statusprüfung.

# Frageliste Auftragnehmer

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Frageliste Auftragnehmer` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Frageliste Auftragnehmer
- **Spezialgegenstand:** Frageliste Auftragnehmer wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Frageliste Auftragnehmer** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche eigenen Kunden, Betriebsmittel, Mitarbeiter und Marktaktivitäten bestehen?
- Wie frei ist die Person im Alltag wirklich?
- Welche Vorgaben akzeptiert sie warum?
- Welche Belege kann sie liefern?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche eigenen Kunden, Betriebsmittel, Mitarbeiter und Marktaktivitäten bestehen?
- Wie frei ist die Person im Alltag wirklich?
- Welche Vorgaben akzeptiert sie warum?
- Welche Belege kann sie liefern?

**Mindest-Output:** Auftragnehmerfragebogen mit Statusindizien und Belegen.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 4. `freie-zeiteinteilung`

**Fokus:** Prüft Zeitsouveränität, Dienstpläne, Kernzeiten, Deadlines, Verfügbarkeit und Abwesenheitsregeln.

# Freie Zeiteinteilung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freie Zeiteinteilung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freie Zeiteinteilung
- **Spezialgegenstand:** Freie Zeiteinteilung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Freie Zeiteinteilung** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Kann die Person Arbeitstage und Zeiten frei bestimmen?
- Gibt es Dienstplan, Kernzeit, Rufbereitschaft, Daily Meetings oder Genehmigung von Urlaub?
- Sind Deadlines sachlich projektbedingt oder arbeitszeitähnlich?
- Welche Nachweise zeigen echte oder nur behauptete Freiheit?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Kann die Person Arbeitstage und Zeiten frei bestimmen?
- Gibt es Dienstplan, Kernzeit, Rufbereitschaft, Daily Meetings oder Genehmigung von Urlaub?
- Sind Deadlines sachlich projektbedingt oder arbeitszeitähnlich?
- Welche Nachweise zeigen echte oder nur behauptete Freiheit?

**Mindest-Output:** Zeitfreiheits-Check mit Terminlogik, Abwesenheitsregeln und Indizien.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.
