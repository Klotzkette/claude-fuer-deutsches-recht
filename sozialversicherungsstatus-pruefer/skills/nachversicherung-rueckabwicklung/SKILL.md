---
name: nachversicherung-rueckabwicklung
description: "Nachversicherung Rueckabwicklung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nachversicherung Rueckabwicklung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Nachversicherung Rueckabwicklung** im Plugin Sozialversicherungsstatus Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nachversicherung-rueckabwicklung` | Prüft arbeits-, steuer-, beitrags- und vertragspraktische Rückabwicklung nach Statusänderung. |
| `plattformverhaeltnis` | Prüft digitale Plattformen als Auftraggeber, Vermittler oder Algorithmus-Steuerer. |
| `steuerberater-wp-freier-mitarbeiter` | Prüft freie Mitarbeit in Steuerberater- oder Wirtschaftsprüferkanzleien mit Berufsrecht und Statusindizien. |
| `therapeuten-praxen` | Prüft Physio-, Ergo-, Logo- und Psychotherapie-Praxen mit Raum-/Gerätenutzung, Patientensteuerung und Abrechnung. |

## Arbeitsweg

Im Plugin Sozialversicherungsstatus Pruefer gilt für **Nachversicherung Rueckabwicklung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nachversicherung-rueckabwicklung`

**Fokus:** Prüft arbeits-, steuer-, beitrags- und vertragspraktische Rückabwicklung nach Statusänderung.

# Rückabwicklung nach Umqualifizierung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rückabwicklung nach Umqualifizierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Rückabwicklung nach Umqualifizierung
- **Spezialgegenstand:** Rückabwicklung nach Umqualifizierung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Rückabwicklung nach Umqualifizierung** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV
- Arbeitsrecht
- Steuerrecht Schnittstelle

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche Zahlungen werden beitragspflichtiges Arbeitsentgelt?
- Müssen Verträge, Rechnungen, Umsatzsteuer und Payroll korrigiert werden?
- Welche arbeitsrechtlichen Ansprüche werden behauptet?
- Wie wird Vergleich oder Übergangsvertrag gestaltet?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche Zahlungen werden beitragspflichtiges Arbeitsentgelt?
- Müssen Verträge, Rechnungen, Umsatzsteuer und Payroll korrigiert werden?
- Welche arbeitsrechtlichen Ansprüche werden behauptet?
- Wie wird Vergleich oder Übergangsvertrag gestaltet?

**Mindest-Output:** Rückabwicklungsplan mit Payroll, Steuern, Vertrag und Kommunikation.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 2. `plattformverhaeltnis`

**Fokus:** Prüft digitale Plattformen als Auftraggeber, Vermittler oder Algorithmus-Steuerer.

# Plattformverhältnis

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Plattformverhältnis` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Plattformverhältnis
- **Spezialgegenstand:** Plattformverhältnis wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Plattformverhältnis** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- EU Plattformarbeit live prüfen

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Bestimmt die Plattform Preis, Zugang, Ranking, Sanktionen oder Arbeitsweise?
- Wer besitzt Kundenzugang und Daten?
- Kann der Worker Unternehmerrisiko und eigene Marktchance entfalten?
- Welche AGB/Algorithmus-Belege braucht die Akte?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Bestimmt die Plattform Preis, Zugang, Ranking, Sanktionen oder Arbeitsweise?
- Wer besitzt Kundenzugang und Daten?
- Kann der Worker Unternehmerrisiko und eigene Marktchance entfalten?
- Welche AGB/Algorithmus-Belege braucht die Akte?

**Mindest-Output:** Plattformstatus-Memo mit Algorithmic-Control-Indizien und Belegen.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 3. `steuerberater-wp-freier-mitarbeiter`

**Fokus:** Prüft freie Mitarbeit in Steuerberater- oder Wirtschaftsprüferkanzleien mit Berufsrecht und Statusindizien.

# Freier Mitarbeiter Steuerberater/WP

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freier Mitarbeiter Steuerberater/WP` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freier Mitarbeiter Steuerberater/WP
- **Spezialgegenstand:** Freier Mitarbeiter Steuerberater/WP wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Freier Mitarbeiter Steuerberater/WP** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- StBerG/WPO Schnittstellen

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer trägt Mandatsverantwortung und Haftung?
- Ist die Person in Kanzleiorganisation, Fristen, Software und Weisungen integriert?
- Hat sie eigene Mandanten, Büro, Mitarbeiter oder nur Stundenhonorar?
- Welche Berufsrechts- und Datenschutzfragen laufen parallel?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer trägt Mandatsverantwortung und Haftung?
- Ist die Person in Kanzleiorganisation, Fristen, Software und Weisungen integriert?
- Hat sie eigene Mandanten, Büro, Mitarbeiter oder nur Stundenhonorar?
- Welche Berufsrechts- und Datenschutzfragen laufen parallel?

**Mindest-Output:** StB/WP-Statuscheck mit Kanzleipraxis, Haftung und Eingliederung.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 4. `therapeuten-praxen`

**Fokus:** Prüft Physio-, Ergo-, Logo- und Psychotherapie-Praxen mit Raum-/Gerätenutzung, Patientensteuerung und Abrechnung.

# Therapeuten in Praxen

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Therapeuten in Praxen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Therapeuten in Praxen
- **Spezialgegenstand:** Therapeuten in Praxen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Therapeuten in Praxen** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- Heilmittel-/Berufsrecht

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer akquiriert Patienten und rechnet ab?
- Nutzt die Person Räume, Terminplan, Rezeptverwaltung und Personal der Praxis?
- Gibt es eigene Zulassung, Betriebsmittel, Ausfallrisiko und Vertretung?
- Welche Verträge verschleiern tatsächliche Praxisintegration?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer akquiriert Patienten und rechnet ab?
- Nutzt die Person Räume, Terminplan, Rezeptverwaltung und Personal der Praxis?
- Gibt es eigene Zulassung, Betriebsmittel, Ausfallrisiko und Vertretung?
- Welche Verträge verschleiern tatsächliche Praxisintegration?

**Mindest-Output:** Therapeutenstatus-Memo mit Praxisindizien, Abrechnung und Sanierung.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.
