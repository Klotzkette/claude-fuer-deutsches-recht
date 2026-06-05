---
name: solo-steuerluecke-erkennen-steuernummer-ust
description: "Steuerluecke Erkennen Steuernummer UST: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuerluecke Erkennen Steuernummer UST

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Steuerluecke Erkennen Steuernummer UST** im Plugin Solo-/Selbstständigenpraxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `solo-steuerluecke-erkennen` | Solo-Selbstständige: ordnet Steuerschulden, Stundung, Vollstreckung und Kommunikation; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-steuernummer-und-ust-id` | Solo-Selbstständige: klärt Steuernummer, USt-IdNr., Auslandskunden und Rechnungsstart; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-stundensatz-kalkulation` | Solo-Selbstständige: berechnet Stundensatz aus Kosten, Auslastung, Steuer, Urlaub und Risiko; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-ug-oder-gmbh-wechsel` | Solo-Selbstständige: bewertet Haftung, Kosten, Steuern, Register und Außenwirkung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-abmahnung-erhalten` | Solo-Selbstständige: sortiert UWG/Urheber/Marke/DSGVO-Abmahnung und Fristen; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-abschluss-vor-abgabe` | Solo-Selbstständige: macht den finalen Selbstcheck vor Vertrag, Rechnung, Behördenantwort oder Upload; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-agb-fuer-kleine-selbststaendige` | Solo-Selbstständige: erstellt schlanke AGB ohne unwirksame Überdehnung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |
| `solo-agenturmodell` | Solo-Selbstständige: prüft Leadagentur, Durchreichen, Marge, Haftung und Subunternehmer; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis. |

## Arbeitsweg

Im Plugin Solo-/Selbstständigenpraxis gilt für **Steuerluecke Erkennen Steuernummer UST**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `solo-steuerluecke-erkennen`

**Fokus:** Solo-Selbstständige: ordnet Steuerschulden, Stundung, Vollstreckung und Kommunikation; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Krise Schulden und Neustart: Ordnet steuerschulden

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Krise Schulden und Neustart**. Schwerpunkt: ordnet Steuerschulden, Stundung, Vollstreckung und Kommunikation. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 2. `solo-steuernummer-und-ust-id`

**Fokus:** Solo-Selbstständige: klärt Steuernummer, USt-IdNr., Auslandskunden und Rechnungsstart; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Anmeldung und Behörden: Klärt steuernummer

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Anmeldung und Behörden**. Schwerpunkt: klärt Steuernummer, USt-IdNr., Auslandskunden und Rechnungsstart. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 3. `solo-stundensatz-kalkulation`

**Fokus:** Solo-Selbstständige: berechnet Stundensatz aus Kosten, Auslastung, Steuer, Urlaub und Risiko; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Pricing Liquidität und Wachstum: Berechnet stundensatz aus kosten

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Pricing Liquidität und Wachstum**. Schwerpunkt: berechnet Stundensatz aus Kosten, Auslastung, Steuer, Urlaub und Risiko. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 4. `solo-ug-oder-gmbh-wechsel`

**Fokus:** Solo-Selbstständige: bewertet Haftung, Kosten, Steuern, Register und Außenwirkung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Wachstum Zusammenarbeit und Rechtsform: Bewertet haftung

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Wachstum Zusammenarbeit und Rechtsform**. Schwerpunkt: bewertet Haftung, Kosten, Steuern, Register und Außenwirkung. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 5. `solo-abmahnung-erhalten`

**Fokus:** Solo-Selbstständige: sortiert UWG/Urheber/Marke/DSGVO-Abmahnung und Fristen; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Marketing E-Commerce und Plattformen: Sortiert uwg/urheber/marke/dsgvo-abmahnung und fristen

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Marketing E-Commerce und Plattformen**. Schwerpunkt: sortiert UWG/Urheber/Marke/DSGVO-Abmahnung und Fristen. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 6. `solo-abschluss-vor-abgabe`

**Fokus:** Solo-Selbstständige: macht den finalen Selbstcheck vor Vertrag, Rechnung, Behördenantwort oder Upload; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Grenzen Compliance und Selbstschutz: Macht den finalen selbstcheck vor vertrag

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Grenzen Compliance und Selbstschutz**. Schwerpunkt: macht den finalen Selbstcheck vor Vertrag, Rechnung, Behördenantwort oder Upload. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 7. `solo-agb-fuer-kleine-selbststaendige`

**Fokus:** Solo-Selbstständige: erstellt schlanke AGB ohne unwirksame Überdehnung; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Verträge und AGB: Erstellt schlanke agb ohne unwirksame überdehnung

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Verträge und AGB**. Schwerpunkt: erstellt schlanke AGB ohne unwirksame Überdehnung. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.

## 8. `solo-agenturmodell`

**Fokus:** Solo-Selbstständige: prüft Leadagentur, Durchreichen, Marge, Haftung und Subunternehmer; mit Abfrage von Tätigkeit, Status, Belegen, Fristen, Geldfolge und konkretem nächstem Arbeitsergebnis.

# Wachstum Zusammenarbeit und Rechtsform: Prüft leadagentur

## Einsatz

Dieser Skill hilft Solo-Selbstständigen beim Themenfeld **Wachstum Zusammenarbeit und Rechtsform**. Schwerpunkt: prüft Leadagentur, Durchreichen, Marge, Haftung und Subunternehmer. Er sortiert die tatsächlichen Unterlagen, den Handlungsdruck und die wirtschaftliche Folge.

## Arbeitsweise

1. Klär zuerst Tätigkeit, Kundentyp, Bundesland/Ort, Haupt- oder Nebenerwerb, Umsatzgrößen, Fristdruck und vorhandene Dokumente.
2. Trenne Muss-Pflichten von Klugheitsmaßnahmen: Anmeldung, Steuer, Vertrag, Sozialversicherung, Datenschutz, Geldfluss und Beweis.
3. Baue eine Ampel mit Sofortmaßnahme, sauberer Dokumentation, optionaler Optimierung und Punkten für Steuerberater, Anwalt oder Behörde.
4. Formuliere am Ende genau ein brauchbares Artefakt: Checkliste, Mail, Vertragsbaustein, Widerspruchsskizze, Fristenlog, Rechnungstext oder Entscheidungsmemo.

## Ergebnis

- Kurzdiagnose in normalem Deutsch
- To-do-Liste mit Fristen und Belegen
- Risiko-/Geldfolge-Ampel
- konkreter Textbaustein oder Dokumentenplan

## Quellen- und Qualitätsregeln

- Prüfe aktuelle Beträge, Grenzwerte und Fristen in amtlichen Quellen, insbesondere Gesetze im Internet, ELSTER, DRV, KSK, Bundesagentur für Arbeit und BMWK-Existenzgründungsportal.
- Keine Steuer- oder Sozialversicherungsentscheidung ohne Hinweis, welche Angaben geschätzt sind und welche Belege fehlen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglichem Fundlink ausgeben; keine BeckRS-/Juris-/Kommentar-Blindzitate.
