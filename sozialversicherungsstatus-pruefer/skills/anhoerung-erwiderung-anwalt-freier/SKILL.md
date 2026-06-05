---
name: anhoerung-erwiderung-anwalt-freier
description: "Anhoerung Erwiderung Anwalt Freier: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anhoerung Erwiderung Anwalt Freier

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Anhoerung Erwiderung Anwalt Freier** im Plugin Sozialversicherungsstatus Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anhoerung-erwiderung` | Reagiert auf Anhörungsschreiben vor belastendem Status- oder Beitragsbescheid. |
| `anwalt-freier-mitarbeiter` | Prüft freie anwaltliche Mitarbeit, Kanzleieingliederung, Versorgungswerk, Weisungen, Mandatskontakt und Abrechnung. |
| `arbeitnehmerueberlassung-abgrenzung` | Prüft Drittpersonaleinsatz zwischen Werk-/Dienstvertrag, selbständigem Einsatz und Arbeitnehmerüberlassung. |
| `arbeitsmittel` | Prüft eigene oder fremde Arbeitsmittel: Laptop, Instrumente, Fahrzeuge, Softwarelizenzen, Räume und Spezialgeräte. |

## Arbeitsweg

Im Plugin Sozialversicherungsstatus Pruefer gilt für **Anhoerung Erwiderung Anwalt Freier**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anhoerung-erwiderung`

**Fokus:** Reagiert auf Anhörungsschreiben vor belastendem Status- oder Beitragsbescheid.

# Anhörung und Erwiderung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Anhörung und Erwiderung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Anhörung und Erwiderung
- **Spezialgegenstand:** Anhörung und Erwiderung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Anhörung und Erwiderung** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB X Anhörung
- SGB IV

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Welche vorläufige Wertung enthält die Behörde?
- Welche Tatsachen fehlen oder sind falsch gewichtet?
- Welche Belege können kurzfristig nachgereicht werden?
- Welche Vergleichs-/Umstellungsoptionen laufen parallel?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Welche vorläufige Wertung enthält die Behörde?
- Welche Tatsachen fehlen oder sind falsch gewichtet?
- Welche Belege können kurzfristig nachgereicht werden?
- Welche Vergleichs-/Umstellungsoptionen laufen parallel?

**Mindest-Output:** Anhörungserwiderung mit Korrekturen, Belegen und Antrag.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 2. `anwalt-freier-mitarbeiter`

**Fokus:** Prüft freie anwaltliche Mitarbeit, Kanzleieingliederung, Versorgungswerk, Weisungen, Mandatskontakt und Abrechnung.

# Freier Mitarbeiter Anwalt

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freier Mitarbeiter Anwalt` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freier Mitarbeiter Anwalt
- **Spezialgegenstand:** Freier Mitarbeiter Anwalt wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Freier Mitarbeiter Anwalt** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7
- BRAO/BORA Schnittstelle
- Berufsständische Versorgung

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Arbeitet die Person auf eigenen Mandaten oder Kanzleimandaten?
- Wer bestimmt Arbeitszeit, Akten, Schriftsatzstil, Mandantenkontakt und Honorar?
- Gibt es eigenes Unternehmerrisiko, Kanzleisitz, Haftpflicht, Briefkopf und Akquise?
- Wie wirken Versorgungswerk und Befreiung von Rentenversicherung?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Arbeitet die Person auf eigenen Mandaten oder Kanzleimandaten?
- Wer bestimmt Arbeitszeit, Akten, Schriftsatzstil, Mandantenkontakt und Honorar?
- Gibt es eigenes Unternehmerrisiko, Kanzleisitz, Haftpflicht, Briefkopf und Akquise?
- Wie wirken Versorgungswerk und Befreiung von Rentenversicherung?

**Mindest-Output:** Anwaltsstatus-Memo mit Berufsrecht, Statusindizien und Versicherungszweigen.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 3. `arbeitnehmerueberlassung-abgrenzung`

**Fokus:** Prüft Drittpersonaleinsatz zwischen Werk-/Dienstvertrag, selbständigem Einsatz und Arbeitnehmerüberlassung.

# Arbeitnehmerüberlassung Abgrenzung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Arbeitnehmerüberlassung Abgrenzung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Arbeitnehmerüberlassung Abgrenzung
- **Spezialgegenstand:** Arbeitnehmerüberlassung Abgrenzung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Arbeitnehmerüberlassung Abgrenzung** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- AÜG
- SGB IV § 7
- BGB

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer erteilt fachliche und organisatorische Weisungen?
- Ist die Person in Kundenteams eingegliedert?
- Schuldet der Dienstleister Ergebnis oder Personalgestellung?
- Welche Erlaubnis-, Equal-Pay- und Fiktionsrisiken bestehen?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer erteilt fachliche und organisatorische Weisungen?
- Ist die Person in Kundenteams eingegliedert?
- Schuldet der Dienstleister Ergebnis oder Personalgestellung?
- Welche Erlaubnis-, Equal-Pay- und Fiktionsrisiken bestehen?

**Mindest-Output:** AÜG-/Statusmatrix mit Weisungsquelle, Eingliederung und Risiko.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.

## 4. `arbeitsmittel`

**Fokus:** Prüft eigene oder fremde Arbeitsmittel: Laptop, Instrumente, Fahrzeuge, Softwarelizenzen, Räume und Spezialgeräte.

# Arbeitsmittel und Equipment

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Arbeitsmittel und Equipment` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Arbeitsmittel und Equipment
- **Spezialgegenstand:** Arbeitsmittel und Equipment wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** SGB IV § 7/§ 7a, SGB VI, SGB III, SGB V, SGB XI, DRV-Statusfeststellung, Beitragsnachforderung, Säumniszuschläge und Lohnsteuer-Schnittstelle.
- **Entscheidende Weiche:** Prüfe Eingliederung, Weisungsrecht, Unternehmerrisiko, Vergütung, Exklusivität, Auftreten am Markt, Sperrminorität und gelebte Praxis.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck

Das Sozialversicherungsstatus-Plugin prüft Beschäftigung, Selbständigkeit, Scheinselbständigkeit und Statusfeststellung für Geschäftsführer, Freelancer, Anwälte, Lehrer, Musikschulen, Plattformarbeit und andere Arbeitsformen nach deutscher Sozialversicherungssystematik.

Dieser Skill macht aus **Arbeitsmittel und Equipment** einen belastbaren Workflow: erst Rolle und Ziel, dann Rechtsanker, tatsächliche Praxis, Dokumente, Risiken, Gegenargumente und verwertbarer Output.

## Rechts- und Quellenanker

- SGB IV § 7

Aktuelle Fassungen, Behördenhinweise, Formulare, Guidance und Rechtsprechung vor konkreter Verwendung live prüfen. Keine Modellzitate als Beleg verwenden.

## Intake-Fragen

- Wer stellt wesentliche Arbeitsmittel und trägt Kosten?
- Sind fremde Tools aus Securitygründen zwingend oder Ausdruck von Eingliederung?
- Hat die Person eigene berufstypische Infrastruktur?
- Wie werden BYOD, Kundenzugänge und Lizenzpflichten dokumentiert?

## Workflow

1. Sachverhalt in Rollen, Dokumente, Zeitachse und tatsächliche Durchführung zerlegen.
2. Rechtsanker und zwingende Vorfragen live prüfen.
3. Pro- und Contra-Indizien gewichten, nicht nur sammeln.
4. Output als Memo, Matrix, Redline, Antragspaket oder Counsel-Briefing liefern.

## Tiefencheck für die Akte

- Wer stellt wesentliche Arbeitsmittel und trägt Kosten?
- Sind fremde Tools aus Securitygründen zwingend oder Ausdruck von Eingliederung?
- Hat die Person eigene berufstypische Infrastruktur?
- Wie werden BYOD, Kundenzugänge und Lizenzpflichten dokumentiert?

**Mindest-Output:** Arbeitsmittel-Matrix mit Kostenträger, Notwendigkeit, Statusgewicht und Belegen.

## Qualitäts- und Risikofilter

- Vertragsetiketten nie übernehmen: Entscheidend ist die Gesamtwürdigung aus Vertrag und gelebter Praxis.
- Sondertatbestände wie SGB VI § 2, KSVG, Minijob, AÜG, Geschäftsführer-Sperrminorität und Cross-border immer als eigene Abzweige prüfen.
- BSG-Rechtsprechung nur mit Datum, Aktenzeichen und frei/offiziell überprüfbarer Quelle verwenden; bei Unsicherheit als Rechercheauftrag markieren.
- Bei Beitrags-, Straf- oder Betriebsprüfungsrisiko keine lockere Entwarnung geben, sondern Zeiträume, Versicherungszweige und Belege konkretisieren.
