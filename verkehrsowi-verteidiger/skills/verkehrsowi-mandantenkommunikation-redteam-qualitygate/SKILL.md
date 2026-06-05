---
name: verkehrsowi-mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation Redteam Qualitygate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenkommunikation Redteam Qualitygate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenkommunikation Redteam Qualitygate** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin verkehrsowi-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin verkehrsowi-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `verkehrsowi-rechtsprechungsrecherche` | Rechtsprechungsrecherche für OWi-Verkehrsmandate: Anwalt sucht OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverbot. Normen: §§ 24 StVG, 25 StVG, 4 StVG; OWiG §§ 67 und 79 und 80. Prüfraster: OLG-Datenbanken (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang), Suchstrategien für Messverfahren/Rohmessdaten/Verjährung/Fahrverbot, Kernzitate BVerfG, BGH, OLGs. Output Fundstellen-Liste mit Aktenzeichen, Datum, Leitsatz, Verwertungsnotiz. Abgrenzung: Messverfahren-Details siehe verkehrsowi-messverfahren-geschwindigkeit; Corporate-Rspr-Recherche siehe corporate-kanzlei-rechtsprechungsrecherche. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Mandantenkommunikation Redteam Qualitygate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin verkehrsowi-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin verkehrsowi-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## OWi-Mandantenkommunikation Speziallage
- **Sofort-Aufklaerung Mandant:**
 - Schweigerecht des Betroffenen § 55 OWiG.
 - Halterauskunftspflicht § 31a StVZO bleibt (sonst Fahrtenbuchauflage moeglich).
 - Anhoerungsbogen kein Bescheid - keine Einspruchsfrist; trotzdem Reaktion entscheidet ueber weiteres Verfahren.
 - Bussgeldbescheid: 2 Wochen § 67 OWiG.
- **Entscheidungsfragen pro Konstellation:**
 - **Geldbusse moderat, keine Punkte:** Akzeptanz oft sinnvoller als Einspruch (Kostenrisiko Verfahren).
 - **Punkte FAER:** Pruefen Punktestand (Abfrage moeglich); 6+ Punkte = Risikobereich; 8 Punkte = Fahrerlaubnisentzug § 4 V StVG.
 - **Fahrverbot 1-3 Monate:** Bei Berufskraftfahrer/-Fahrerin oft existenzbedrohend; Antrag auf Wegfall Fahrverbot wegen unzumutbarer Haerte (regelmaessig restriktiv); ggf. Erhoehung Geldbusse als Kompensation moeglich (BGH-Linie).
 - **MPU-Risiko:** ab 1,6 Promille (§ 13 FeV), bei wiederholten Verstoessen, bei Drogen einmalig.
- **Berufliche Auswirkungen:** Berufskraftfahrer, Aussendienst, Aerzte/Beamte (Pflichtmeldung Disziplinarrecht), Polizei, Lehrer.
- **Kostenhinweis:** RVG VV 5100 ff. fuer OWi; Rechtsschutzversicherung-Deckung pruefen (Selbstbeteiligung; Wartezeit 3 Monate ueblich; Strafrechtsschutz nur bei nicht vorsaetzlichem Vorwurf).
- **Mandantenfreigabe schriftlich:** Einspruch / Einspruchsruecknahme / Beschraenkung / Antrag auf Hauptverhandlung statt schriftliches Verfahren § 72 OWiG.
- **Praxis-Tipp:** Bei sehr hohem Risiko (Fahrverbot bei Berufskraftfahrer) Hauptverhandlung statt schriftlicher Entscheidung; persoenlicher Eindruck Betroffener oft entscheidend.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin verkehrsowi-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin verkehrsowi-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## OWi-Red-Team-Checks
- **Frist-Re-Check:** Einspruch § 67 OWiG 2 Wochen ab Zustellung; Rechtsbeschwerde §§ 79, 80 OWiG 1 Woche / 1 Monat; Verjaehrung § 26 III StVG 3 Monate (bis Bescheid) / 6 Monate (bis 1. Instanz Urteil); Unterbrechung § 33 OWiG.
- **BKatV-Re-Check:** Aktuelle Anlage zur StVO und § 26a StVG; Regelbusse, Punkte, Fahrverbote stets gegen Tatzeit pruefen; bei Aenderungen lex mitior § 4 III OWiG.
- **Messverfahren-Check:**
 - **Eichschein** im Tatzeitraum gueltig?
 - **Bedienerschein** Messbeamter?
 - **Standardisiertes Messverfahren** (BGH-Linie zur Beweiskraft)?
 - **Toleranzwerte** zugunsten Betroffener abgezogen?
 - **Lichtbild Identifizierung** Fahrer?
- **Beweisanforderungs-Check Akteneinsicht § 49 OWiG i.V.m. § 147 StPO:** Vollstaendigkeit Akte; Messprotokoll; Lebensakte Geraet; Rohdaten (BVerfG-Linie zur fair-trial-Garantie); Schulungs-/Sachkundenachweis Bediener.
- **Toleranzwerte:**
 - Geschwindigkeit < 100 km/h: 3 km/h, ab 100 km/h: 3 %.
 - Abstand: 10 % der Standard-Messung.
 - Atemalkohol: 0,1 mg/l Toleranz.
- **Konsequenzen-Re-Check:** Punkte FAER 1-3? Fahrverbot 1-3 Monate? 8-Punkte-Grenze (§ 4 V StVG = Fahrerlaubnisentzug)? Wiederholungstaeter § 4 II StVG?
- **Berufliche Relevanz** angesprochen? Berufskraftfahrer, Aerzte, Anwaelte, Beamte - existenzielles Risiko Fahrverbot.
- **Halluzinations-Check:** Keine erfundenen OLG-Az; "OLG-Linie" / "staendige Rspr." statt erfundener Fundstellen.

## 3. `verkehrsowi-rechtsprechungsrecherche`

**Fokus:** Rechtsprechungsrecherche für OWi-Verkehrsmandate: Anwalt sucht OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverbot. Normen: §§ 24 StVG, 25 StVG, 4 StVG; OWiG §§ 67 und 79 und 80. Prüfraster: OLG-Datenbanken (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang), Suchstrategien für Messverfahren/Rohmessdaten/Verjährung/Fahrverbot, Kernzitate BVerfG, BGH, OLGs. Output Fundstellen-Liste mit Aktenzeichen, Datum, Leitsatz, Verwertungsnotiz. Abgrenzung: Messverfahren-Details siehe verkehrsowi-messverfahren-geschwindigkeit; Corporate-Rspr-Recherche siehe corporate-kanzlei-rechtsprechungsrecherche.

# Rechtsprechungsrecherche OWi-Verkehrsrecht

## Triage zu Beginn

1. **Konkrete Rechtsfrage?** — "Darf der Betroffene Rohmessdaten anfordern?" vs. "War die Eichung gueltig?" — Suchstrategien verschieden.
2. **Gericht?** — OLG des jeweiligen Bundeslandes fuer Rechtsbeschwerde-Entscheidungen; BGH fuer grundsaetzliche Fragen; BVerfG fuer Grundrechtsfragen.
3. **Verifikation Pflicht:** Aktenzeichen, Datum und Leitsatz vor Verwendung in offener Quelle (bundesverfassungsgericht.de, bundesgerichtshof.de, openjur.de, dejure.org) aufrufen — nicht aus Modellwissen.
4. **Messgeraet-spezifische Rspr.?** — Fuer PoliScan, ESO, TraffiStar gibt es geraetespezifische OLG-Entscheidungen.

## Zentrale Rechtsprechungs-Kette OWi (Stand Mai 2026)

Alle Zitate vor Versand in offener Quelle (BGH-Datenbank, openjur.de, dejure.org, nrwe.de) verifizieren. Fundstellen wie NZV nicht aus Modellwissen.

### Standardisiertes Messverfahren
- BGH BGHSt 39, 291 (1993) — Grundsatz standardisiertes Verfahren ohne Detailbegruendung. Volltext über bundesgerichtshof.de prüfen.
- OLG Bamberg, Beschl. v. ... (NZV 2017, 494 — Aktenzeichen vor Versand in offener Quelle aufrufen): Sachverstaendigenantrag bei konkreten Angriffspunkten.

### Rohmessdaten
- BVerfG, Beschl. v. 12.11.2020, 2 BvR 1616/18 — Recht des Betroffenen auf Zugang zu vorhandenen Messdaten. Quelle: bundesverfassungsgericht.de
- BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20 — Keine Pflicht zur Speicherung von Rohmessdaten (Leivtec XV3). Quelle: bundesverfassungsgericht.de
- OLG Köln, Beschl. v. ... (NZV 2021, 42 — Aktenzeichen vor Versand verifizieren): Vollständige Messakte einschließlich Rohmessdaten.

### Verjährung
- OLG Hamm, NZV 2020, 418 — 3-Monats-Frist § 26 Abs. 3 StVG (Aktenzeichen vor Versand in offener Quelle prüfen)
- OLG Düsseldorf, NZV 2020, 526 — Verjährung bei Verkehrs-OWi (Aktenzeichen vor Versand prüfen)

### Zustellung / Fristbeginn
- OLG Celle, NZV 2020, 523 — Fehlerhafte Zustellung = späterer Fristbeginn
- OLG Hamm, NZV 2021, 531 — Einwurf-Einschreiben gilt im OWi-Verfahren

### Alkohol / Drogen (Stand Mai 2026)
- BVerwG, Beschl. v. 8.1.2025, 3 B 2.24 — Cannabis und KCanG (1.4.2024); § 14 FeV neu zu lesen. Quelle: bverwg.de
- § 24a Abs. 1a StVG (THC 3.5 ng/ml seit 22.8.2024) — BGBl. I 2024 Nr. 274
- Hess. VGH, Beschl. v. 19.9.2025, 10 B 606/25 — Cannabis-Verstoss in Probezeit
- Bisherige OLG-Linien zu THC 1 ng/ml (z.B. OLG Bamberg) sind durch Grenzwertanpassung überholt — Volltext und Datum vor Versand prüfen.

### Fahrverbot Haertefall
- OLG Frankfurt, Beschl. v. 18.3.2021, 2 Ss OWi 148/21 (NZV 2021, 448) — Berufsbedingte Angewiesenheit allein kein Haertefall. Quelle: openjur.de bzw. Justiz Hessen.
- OLG München, NZV 2021, 54 — Vier-Monats-Frist § 25 Abs. 2a StVG (Aktenzeichen verifizieren)

### Fahreridentifikation
- BVerfG-Linie zu § 31a StVG (Fahrtenbuchauflage / Halterauskunft) konkret aus bundesverfassungsgericht.de aufrufen
- OLG Bamberg, NZV 2021, 92 — Sachverständigenantrag Lichtbild bei schlechter Qualität (Aktenzeichen verifizieren)

## Suchstrategien Datenbanken

**juris:**
- Normsuche: "§ 26 StVG" + "Verjaehrung" + "Verkehr"
- Normen-Kombination: "§ 25 StVG" + "Haertefall" + "Beruf"
- Volltext: "Rohmessdaten" + "Verwertungsverbot"
- Gericht-Filter: OLG + BVerfG; Zeitraum 2019-2024

**beck-online:**
- NZV durchsuchen (Neue Zeitschrift fuer Verkehrsrecht)
- DAR durchsuchen (Deutsches Autorecht)
- Themenfilter: Bussgeldbescheidverfahren

**OpenJur / Google Scholar:**
- "§ 24a StVG Drogen OLG" (Volltext)
- "Messverfahren Rohmessdaten Betroffener"
- Zeitraum-Filter setzen

## Fundstellen-Abkuerzungen OWi-Spezifisch

| Abkuerzung | Zeitschrift |
|-----------|------------|
| NZV | Neue Zeitschrift fuer Verkehrsrecht |
| DAR | Deutsches Autorecht |
| NZV-RR | NZV-Rechtsprechungs-Report |
| VRS | Verkehrsrechts-Sammlung |
| NJW | Neue Juristische Wochenschrift |
| NStZ | Neue Zeitschrift fuer Strafrecht |
| zfs | Zeitschrift fuer Schadensrecht |

## Schritt-fuer-Schritt-Recherche-Workflow

1. **Rechtsfrage praezisieren:** "Kann Betroffener Rohmessdaten verlangen?"
2. **Normenkette aufbauen:** Art. 103 GG, § 77 OWiG, § 49 OWiG, § 147 StPO.
3. **Datenbanksuche mit Normen:** "Art. 103 GG Rohmessdaten OWi".
4. **Verifikation in offener Quelle:** BVerfG-Datenbank (bundesverfassungsgericht.de), BGH-Datenbank, openjur.de, dejure.org; bei Bundesländern: nrwe.de, justiz.hessen.de, justiz.bayern.de etc. — niemals Modellwissen.
5. **Kernaussage paraphrasieren** fuer Schriftsatz.
6. **Vollstaendiges Zitat:** Gericht + Datum + Az + Fundstelle + Randnummer wenn vorhanden.

## Harte Leitplanken

- Keine erfundenen Aktenzeichen oder Fundstellen.
- Bei Unsicherheit: konservativen Klassiker nennen (BGH BGHSt 43, 277).
- OLG-Rspr. ist regional verschieden — passendes OLG des Bundeslandes pruefen.
- Anwaltliche Endkontrolle bei Zitaten in Schriftsaetzen.
