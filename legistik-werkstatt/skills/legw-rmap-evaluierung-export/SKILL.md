---
name: legw-rmap-evaluierung-export
description: "Legw Rmap Evaluierung Export: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Legw Rmap Evaluierung Export

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Legw Rmap Evaluierung Export** im Plugin Legistik-Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `legw-rmap-evaluierung-und-aenderung` | Lebenszyklus einer Rulemap-Norm: Versionierung; Aenderung im Builder per Drag-and-Drop; Evaluation nach NKRG und GGO; Wirkungskontrolle; Rueckkopplung aus dem Vollzug. Output Aenderungs- und Evaluationsplan mit Zustaendigkeiten; Auslaufdaten und KPI. Anschluss legw-rechtsfolgenabschaetzung-leitfaden. Abgrenzung zur reinen Gesetzgebungstechnik; hier wird die Pflege im Zeitverlauf organisiert. |
| `legw-rmap-export-und-systemintegration` | Export der Rulemap aus dem Builder; Integration in Fachverfahren; Schnittstellen zur eAkte; OZG-Service; Registerlandschaft. Output Integrations-blueprint mit Datenflussskizze und Pruefpunkten. Anschluss legw-rmap-anschluss-an-legw fuer die Rueckbindung an die uebrige Legistik-Werkstatt. Abgrenzung zur IT-Architektur im engeren Sinn; hier liegt der Schwerpunkt auf den juristischen Folgepflichten der Integration. |
| `legw-rmap-grundlagen` | Grundlagen der Rulemapping-Methode: Law as Code; Rulemap als visuelles Entscheidungsmodell; Wenn-Dann-Logik mit Tatbestand; Rechtsfolge; Ausnahme; Verweisung. Akteure (Rulemapping-Group; Prof. Breidenbach; SPRIN-D-Foerderung; BMJ als Anwender). Ziel: Norm parallel als Text und als Rulemap entwerfen; Bruecke zwischen Gesetz und Verwaltungsvollzug. Output: Grundbegriffsglossar und Methoden-Steckbrief. Anschluss legw-rmap-norm-zu-rulemap fuer das konkrete Vorgehen. Abgrenzung zur klassischen Begruendung und Folgenabschaetzung. |
| `legw-rmap-norm-zu-rulemap` | Praxisleitfaden Norm in Rulemap ueberfuehren: Capture (Norm erfassen); Model (Logikmodell zeichnen); Simulate (durchspielen); Verify (Entscheidungen pruefen); Integrate (in System einbinden); Improve (weiterentwickeln). Liefert ein iteratives Vorgehensmodell mit Eingaben; Ausgaben und Pruefpunkten je Schritt. Anschluss legw-rmap-tatbestand-und-rechtsfolge fuer die feine Knotenmodellierung. Abgrenzung zur Textentwurfsarbeit; die Rulemap ist die parallel gepflegte Logikfassung. |
| `legw-rmap-tatbestand-und-rechtsfolge` | Knotenmodellierung in der Rulemap: jeden Tatbestand als pruefbare Bedingung; jede Rechtsfolge als Aktionsknoten. Konjunktion; Disjunktion; Negation; Schwellenwerte sauber abbilden. Output Tatbestands-Rechtsfolge-Liste mit Knoten-IDs; Datentypen und Pruefnotizen. Anschluss legw-rmap-verweisungen-und-ausnahmen fuer Sonderkonstellationen und legw-rmap-entscheidungsbaum-validierung fuer die Pruefung der Pfade. |
| `legw-rmap-verweisungen-und-ausnahmen` | Verweisungen (statisch; dynamisch; Rueckverweisung) und Ausnahmen in der Rulemap sauber modellieren. Verkettung von Normen ueber Subrulemaps; Verweisungsketten dokumentieren; Ausnahmen als eigenstaendige Pfade. Output Verweisungs- und Ausnahmenkarte mit IDs und Pfadtiefen. Anschluss legw-rmap-entscheidungsbaum-validierung fuer die Pfadpruefung. Abgrenzung zur reinen Texterfassung; Verweisungen werden ausgerollt. |
| `legw-rmap-vollzugstauglichkeit` | Bruecke von der Rulemap in den Verwaltungsvollzug: Antragsverfahren; Bescheidstruktur; Akteneinsicht; Widerspruch und Klage; Schnittstelle zu Fachverfahren (z.B. Genehmigungsverfahren mit mehreren Fachbehoerden). Output Vollzugskarte mit Akteuren; Schnittstellen; IT-Anforderungen. Anschluss legw-rmap-export-und-systemintegration. Abgrenzung zur reinen Gesetzgebungsarbeit; hier wird die Vollzugsperspektive zur Norm zurueckgespielt. |
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Aenderung aussieht ohne Aenderungsmarkierungen. Einheitlich lesbar ohne Aenderungsmarkierung Datierung Stand nach Inkrafttreten. Format-Konventionen Inkrafttretens-Handling Verweis-Pflege DOCX-Ausgabe. Output Lesefassung pro Stammgesetz bereinigt datiert. Abgrenzung zu synopse-erstellen Gegenüberestellung alt und neu. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Legw Rmap Evaluierung Export**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `legw-rmap-evaluierung-und-aenderung`

**Fokus:** Lebenszyklus einer Rulemap-Norm: Versionierung; Aenderung im Builder per Drag-and-Drop; Evaluation nach NKRG und GGO; Wirkungskontrolle; Rueckkopplung aus dem Vollzug. Output Aenderungs- und Evaluationsplan mit Zustaendigkeiten; Auslaufdaten und KPI. Anschluss legw-rechtsfolgenabschaetzung-leitfaden. Abgrenzung zur reinen Gesetzgebungstechnik; hier wird die Pflege im Zeitverlauf organisiert.

# Evaluierung und Aenderung von Rulemap-Normen

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Validierte Rulemap im Echtbetrieb
- Berichte aus Vollzug und Gerichtsbarkeit
- Evaluationsklausel der Norm (sofern vorhanden)

## Kern der Methode

Rulemaps werden im Builder per No-Code gepflegt; Aenderungen sind versionierbar und reviewbar. Die Evaluation orientiert sich an Wirkungskontrolle und Erfuellungsaufwand (NKRG-Anforderungen) und stellt fest; ob das Regelungsziel erreicht wird.

## Vorgehen

1. Versionierungsschema festlegen (z.B. semantisch; Datum; Zustaendige)
2. Aenderungsanlass dokumentieren (Vollzug; Gericht; politischer Auftrag)
3. Aenderung im Builder vornehmen; Validierung erneut durchlaufen
4. Evaluation nach Standardrahmen NKRG durchfuehren
5. Bericht an Hausleitung und ggf. Parlament uebermitteln

## Pruefpunkte

Pruefen: ist jede Aenderung rueckverfolgbar? Bleibt der parlamentarische Vorbehalt gewahrt? Wird die Norm trotz Modellpflege materiell richtig gehalten?

## Output

```
Skill: legw-rmap-evaluierung-und-aenderung
Thema: Evaluierung und Aenderung von Rulemap-Normen
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 2. `legw-rmap-export-und-systemintegration`

**Fokus:** Export der Rulemap aus dem Builder; Integration in Fachverfahren; Schnittstellen zur eAkte; OZG-Service; Registerlandschaft. Output Integrations-blueprint mit Datenflussskizze und Pruefpunkten. Anschluss legw-rmap-anschluss-an-legw fuer die Rueckbindung an die uebrige Legistik-Werkstatt. Abgrenzung zur IT-Architektur im engeren Sinn; hier liegt der Schwerpunkt auf den juristischen Folgepflichten der Integration.

# Export und Integration in Vollzugs-IT

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Validierte Rulemap in Endfassung
- Bestandsaufnahme der Vollzugs-IT (eAkte; Register; OZG)
- Rechtsgrundlagen fuer Datenverarbeitung (DSGVO; BDSG; Fachgesetz)

## Kern der Methode

Der Rulemap Builder exportiert ausfuehrbare Modelle; sie werden ueber die Rulemapping Automation Platform an Fachverfahren angebunden. Juristisch zu klaeren sind: Rechtsgrundlage der Datenverarbeitung; Registerzugriffe; Auftragsverarbeitung; Loeschkonzept; Protokollierung.

## Vorgehen

1. Export-Format und Versionsstand festhalten
2. Schnittstellenvertrag mit Vollzugs-IT abschliessen
3. Datenschutz-Folgenabschaetzung beim Bedarf (Art. 35 DSGVO)
4. Auftragsverarbeitung und Hosting klaeren
5. Inbetriebnahme dokumentieren und der Aufsicht melden

## Pruefpunkte

Pruefen: Zustaendigkeitsverteilung Norm und IT; Folgepflichten aus DSGVO; Anschluss an Bundes-IT-Standards (z.B. BSI-Vorgaben; OZG-Vorgaben).

## Output

```
Skill: legw-rmap-export-und-systemintegration
Thema: Export und Integration in Vollzugs-IT
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 3. `legw-rmap-grundlagen`

**Fokus:** Grundlagen der Rulemapping-Methode: Law as Code; Rulemap als visuelles Entscheidungsmodell; Wenn-Dann-Logik mit Tatbestand; Rechtsfolge; Ausnahme; Verweisung. Akteure (Rulemapping-Group; Prof. Breidenbach; SPRIN-D-Foerderung; BMJ als Anwender). Ziel: Norm parallel als Text und als Rulemap entwerfen; Bruecke zwischen Gesetz und Verwaltungsvollzug. Output: Grundbegriffsglossar und Methoden-Steckbrief. Anschluss legw-rmap-norm-zu-rulemap fuer das konkrete Vorgehen. Abgrenzung zur klassischen Begruendung und Folgenabschaetzung.

# Rulemapping - Grundlagen und Begriffe

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Normvorhaben oder bestehende Norm
- Ergebnis aus legistik-auftragsaufnahme
- Sachfeld-Kompass aus legw-<ressort>-<thema>

## Kern der Methode

Rulemapping ist eine Methode, juristische Logik in strukturierte digitale Entscheidungsmodelle (Rulemaps) zu ueberfuehren. Die Methode wurde von Prof. Dr. Stephan Breidenbach entwickelt und wird durch die Bundesagentur fuer Sprunginnovationen SPRIN-D gefoerdert. Sie wird unter anderem im Bundesministerium der Justiz eingesetzt und bildet vollstaendige Wenn-Dann-Logik einer Norm ab; einschliesslich Tatbestaenden; Rechtsfolgen; Ausnahmen und Verweisen.

## Vorgehen

1. Methoden-Steckbrief des Vorhabens anlegen
2. Begriffsglossar (Tatbestand; Rechtsfolge; Ausnahme; Verweisung) sauber definieren
3. Akteurskreis benennen (Rulemapping-Group; BMJ; SPRIN-D; eigene Ressortrolle)
4. Erste Skizze der Wenn-Dann-Struktur der Norm anlegen
5. Uebergabe an legw-rmap-norm-zu-rulemap

## Pruefpunkte

Pruefen: passt die Methode zum Vorhaben? Komplexitaet hoch genug fuer Rulemap? Anschluss an Vollzugs-IT erforderlich? Welche Aufsichtsentscheidung soll spaeter automatisierbar sein?

## Output

```
Skill: legw-rmap-grundlagen
Thema: Rulemapping - Grundlagen und Begriffe
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 4. `legw-rmap-norm-zu-rulemap`

**Fokus:** Praxisleitfaden Norm in Rulemap ueberfuehren: Capture (Norm erfassen); Model (Logikmodell zeichnen); Simulate (durchspielen); Verify (Entscheidungen pruefen); Integrate (in System einbinden); Improve (weiterentwickeln). Liefert ein iteratives Vorgehensmodell mit Eingaben; Ausgaben und Pruefpunkten je Schritt. Anschluss legw-rmap-tatbestand-und-rechtsfolge fuer die feine Knotenmodellierung. Abgrenzung zur Textentwurfsarbeit; die Rulemap ist die parallel gepflegte Logikfassung.

# Von der Norm zur Rulemap - Vorgehensmodell

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Konkrete Norm oder Normentwurf
- Sachfeld-Kompass aus legw-<ressort>-<thema>
- Begriffsglossar aus legw-rmap-grundlagen

## Kern der Methode

Sechs Schritte des Rulemap Builders nach dem Modell der Rulemapping-Group: Capture; Model; Simulate; Verify; Integrate; Improve. Jeder Schritt produziert ein eigenes Artefakt; alle Artefakte sind versionierbar und im Builder ohne Programmierung pflegbar.

## Vorgehen

1. Capture: Normtext erfassen; Strukturparser anwerfen; Tatbestaende; Rechtsfolgen; Ausnahmen markieren
2. Model: Knoten und Kanten der Rulemap zeichnen; Entscheidungspfade abbilden
3. Simulate: realistische Faelle durchspielen; Pfaddeckung pruefen
4. Verify: automatisierte Entscheidungen gegen juristische Soll-Vorgabe pruefen
5. Integrate: Schnittstelle zur Vollzugs-IT der Verwaltung; ohne Programmierung
6. Improve: Feedback aus Vollzug und Gerichtsbarkeit zurueckspielen; Rulemap iterieren

## Pruefpunkte

Pruefen: ist jede Entscheidungspfad-Variante abgedeckt? Sind Ausnahmen explizit modelliert und nicht implizit? Liegt die Verantwortung fuer die Logik beim Normgeber oder beim IT-Dienstleister?

## Output

```
Skill: legw-rmap-norm-zu-rulemap
Thema: Von der Norm zur Rulemap - Vorgehensmodell
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 5. `legw-rmap-tatbestand-und-rechtsfolge`

**Fokus:** Knotenmodellierung in der Rulemap: jeden Tatbestand als pruefbare Bedingung; jede Rechtsfolge als Aktionsknoten. Konjunktion; Disjunktion; Negation; Schwellenwerte sauber abbilden. Output Tatbestands-Rechtsfolge-Liste mit Knoten-IDs; Datentypen und Pruefnotizen. Anschluss legw-rmap-verweisungen-und-ausnahmen fuer Sonderkonstellationen und legw-rmap-entscheidungsbaum-validierung fuer die Pruefung der Pfade.

# Tatbestand und Rechtsfolge als Knoten modellieren

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Konkrete Normfassung
- Ergebnis aus legw-rmap-norm-zu-rulemap (Capture)

## Kern der Methode

Jeder Tatbestand wird zum pruefbaren Bedingungsknoten mit klarem Datentyp (boolean; Schwellenwert; Datum; Aufzaehlung). Jede Rechtsfolge wird zum Aktionsknoten mit eindeutigem Effekt (Bewilligung; Versagung; Auflage; Frist setzen). Konjunktion (und); Disjunktion (oder); Negation; Vergleichsoperator werden explizit gemacht; nicht durch Sprache verschleiert.

## Vorgehen

1. Tatbestand 1 bis n extrahieren und als Knoten anlegen
2. Rechtsfolgen extrahieren und mit Tatbestaenden verbinden
3. Konjunktionen und Disjunktionen explizit kennzeichnen
4. Datentypen je Knoten festlegen
5. Konfliktfreiheit pruefen; widerspruechliche Pfade ausschliessen

## Pruefpunkte

Pruefen: ist jede Voraussetzung als eigener Knoten modelliert? Sind unbestimmte Rechtsbegriffe (zumutbar; angemessen; ueberwiegendes Interesse) entweder konkretisiert oder als gesonderter Beurteilungsknoten markiert?

## Output

```
Skill: legw-rmap-tatbestand-und-rechtsfolge
Thema: Tatbestand und Rechtsfolge als Knoten modellieren
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 6. `legw-rmap-verweisungen-und-ausnahmen`

**Fokus:** Verweisungen (statisch; dynamisch; Rueckverweisung) und Ausnahmen in der Rulemap sauber modellieren. Verkettung von Normen ueber Subrulemaps; Verweisungsketten dokumentieren; Ausnahmen als eigenstaendige Pfade. Output Verweisungs- und Ausnahmenkarte mit IDs und Pfadtiefen. Anschluss legw-rmap-entscheidungsbaum-validierung fuer die Pfadpruefung. Abgrenzung zur reinen Texterfassung; Verweisungen werden ausgerollt.

# Verweisungen und Ausnahmen in der Rulemap

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Knotenmodell aus legw-rmap-tatbestand-und-rechtsfolge
- Liste der Verweisungen und Ausnahmen aus der Norm

## Kern der Methode

Statische Verweisungen werden direkt aufgeloest. Dynamische Verweisungen (auf jeweils gueltige Fassung) sind als Verweisknoten mit Versionspflege umzusetzen. Rueckverweisungen sind als Schleifenpfade explizit zu markieren und auf Endlichkeit zu pruefen. Ausnahmen sind eigene Pfade; keine versteckten Negationen in Tatbestandsknoten.

## Vorgehen

1. Alle Verweisungen aus dem Normtext extrahieren
2. Statisch vs. dynamisch klassifizieren
3. Subrulemaps fuer aufgeloeste Verweisungen anlegen
4. Ausnahmen als eigene Pfade modellieren
5. Verweisungs- und Ausnahmenkarte dokumentieren

## Pruefpunkte

Pruefen: gibt es zirkulaere Verweisungen? Welche EU-Vorgaben sind zu verlinken? Sind Ausnahmen verhaeltnismaessig zugeschnitten? Stehen Ausnahmen im Einklang mit Gleichheitssatz und Bestimmtheitsgebot?

## Output

```
Skill: legw-rmap-verweisungen-und-ausnahmen
Thema: Verweisungen und Ausnahmen in der Rulemap
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 7. `legw-rmap-vollzugstauglichkeit`

**Fokus:** Bruecke von der Rulemap in den Verwaltungsvollzug: Antragsverfahren; Bescheidstruktur; Akteneinsicht; Widerspruch und Klage; Schnittstelle zu Fachverfahren (z.B. Genehmigungsverfahren mit mehreren Fachbehoerden). Output Vollzugskarte mit Akteuren; Schnittstellen; IT-Anforderungen. Anschluss legw-rmap-export-und-systemintegration. Abgrenzung zur reinen Gesetzgebungsarbeit; hier wird die Vollzugsperspektive zur Norm zurueckgespielt.

# Vollzugstauglichkeit der Rulemap im Verwaltungsverfahren

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Rulemap mit validierten Pfaden
- Beschreibung des Verwaltungsverfahrens (Bundes-; Landes-; Kommunalebene)

## Kern der Methode

Eine Rulemap wirkt erst im Verwaltungsverfahren. Die Vollzugstauglichkeit fragt: welche Behoerde welche Stufe; welcher Bescheid; welche Begruendung; welche Rechtsmittelbelehrung; welcher Antrag; welche Schnittstellen zu Fachverfahren (BImSchG-Verfahren; Wind-Genehmigung; OZG-Service). Die SPRIND-Argumentation: Genehmigungsverfahren von Jahren auf Wochen verkuerzen; Parallelarbeit mehrerer Aemter.

## Vorgehen

1. Behoerdenkette des Vollzugs auflisten
2. Antragsmaske und Datenkatalog aus der Rulemap ableiten
3. Bescheidvorlage mit Begruendungsblock je Pfad anlegen
4. Rechtsmittelpfade in der Rulemap reflektieren
5. Schnittstellen zu Fachverfahren benennen (z.B. eAkte; Fachregister)

## Pruefpunkte

Pruefen: wo bleibt die Letztverantwortung beim Menschen (Art. 22 DSGVO)? Sind alle Beteiligungsrechte abgebildet (Drittbeteiligung; UVP)? Bleibt die Aktenfuehrung nachvollziehbar?

## Output

```
Skill: legw-rmap-vollzugstauglichkeit
Thema: Vollzugstauglichkeit der Rulemap im Verwaltungsverfahren
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

## 8. `lesefassung-konsolidiert`

**Fokus:** Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Aenderung aussieht ohne Aenderungsmarkierungen. Einheitlich lesbar ohne Aenderungsmarkierung Datierung Stand nach Inkrafttreten. Format-Konventionen Inkrafttretens-Handling Verweis-Pflege DOCX-Ausgabe. Output Lesefassung pro Stammgesetz bereinigt datiert. Abgrenzung zu synopse-erstellen Gegenüberestellung alt und neu.

# Lesefassung konsolidiert

> Wie sieht das Gesetz aus, wenn das neue Gesetz in Kraft getreten ist? Klipp und klar zum Mitlesen.

## Zweck

Die Lesefassung zeigt das Stammgesetz in der nach Inkrafttreten gültigen Form — **ohne** Änderungsmarkierung, **mit** allen Änderungen eingearbeitet. Adressaten (Bürger, Unternehmen) und Vollzugsbehörden brauchen diese Fassung, um zu sehen, "wie es ab Tag X heisst", ohne den Änderungs-Diff lesen zu müssen.

Komplementär zu:
- **Synopse**: zeigt alt vs. neu in zwei Spalten
- **Änderungsanordnung**: zeigt die Änderung als Befehl ("Paragraf 3 Absatz 2 wird wie folgt geändert: ...")
- **Lesefassung**: zeigt das fertige neue Gesetz

## 1) Inhalte pro Datei

Eine Datei je Stammgesetz. Bei einem Änderungsgesetz, das mehrere Stammgesetze beruehrt, entsprechend mehrere Lesefassungen.

### Header-Block

```
Lesefassung [Name des Stammgesetzes]
Stand nach Inkrafttreten des [Aenderungs-Gesetz-Name] vom [Datum BGBl. Fundstelle]
und der [Zugehoerigen Verordnung] vom [Datum BGBl. Fundstelle]

Konsolidiert auf den [Datum].
Erstellt durch: [Referat / Verantwortlicher / Pruefer]
```

### Format

- Markdown mit Überschrift pro Paragraf: `## § 3 Antragstellung`
- Absätze als Aufzaehlung mit Klammer-Zahl: `(1) ...`, `(2) ...`
- Sätze nicht nummeriert (auch wenn Gesetz Satz-Nr. hat — die folgen im Text)
- Aufzaehlungen mit `1.`, `a)`, `aa)` wie im Gesetz
- DOCX-Export für offizielle Versendung an Adressaten und Vollzugsbehörden

## 2) Was muss in die Lesefassung

### Geaenderte Paragrafen

Mit dem **neuen Wortlaut** komplett. Auch wenn nur ein Komma geändert wurde — der gesamte Paragraf, damit die Lesefassung in sich konsistent ist.

### Nicht-geänderte, aber bezugsrelevante Paragrafen

Bei sehr stark auf andere Paragrafen verweisenden Gesetzen ist es sinnvoll, **alle** Paragrafen aufzunehmen, damit der Adressat nicht zwischen zwei Dokumenten springen muss.

### Anlagen, soweit Bestandteil des Gesetzes

Mit Verweis und gegebenenfalls verlinkt. Bei umfangreichen Anlagen ggf. separate Datei.

### Inkrafttretens-Vorschriften

Am Ende der Lesefassung in einer Klar-Kennzeichnung:

```
Diese Lesefassung gilt ab dem [Datum].
Bis zum [Datum] gilt die vorherige Fassung (siehe Aenderungsanordnung vom ...).
```

### Stand und Datum

Das Datum des **Inkrafttretens** ist massgeblich. Bei stufenweisem Inkrafttreten mehrere Lesefassungen erstellen (z.B. "Lesefassung Stand 01.01.2026" und "Lesefassung Stand 01.07.2026").

## 3) Prüfliste vor Freigabe

### Vollständigkeit

- [ ] Alle vom Änderungsgesetz beruehrten Paragrafen aufgenommen
- [ ] Anlagen aktualisiert
- [ ] Inkrafttretens-Datum klar dokumentiert
- [ ] Stand-Datum (Konsolidierung) klar dokumentiert

### Konsistenz

- [ ] Numerierung konsistent (keine doppelten Paragrafen, keine Lücken)
- [ ] Verweise innerhalb des Gesetzes aktualisiert (z.B. "Paragraf 3 Absatz 4" stimmt jetzt, nachdem Absatz 3 weggefallen ist)
- [ ] Verweise auf externe Normen aktualisiert (z.B. wenn EuGVVO geändert wurde, deren Verweise aktualisieren)
- [ ] Begriffsdefinitionen konsistent (wenn `Verbraucher` neu definiert ist, überall der neue Begriff)

### Format

- [ ] Markdown-Lesefassung erstellt
- [ ] DOCX-Lesefassung erstellt
- [ ] Header-Block vorhanden mit Stand und Inkrafttreten
- [ ] Gerichts-/Adressaten-tauglich (keine Entwurfs-Wasserzeichen, kein Track Changes)

### Kontrolle

- [ ] Stichprobe: 3-5 Paragrafen mit dem amtlichen BGBl-Text abgeglichen
- [ ] Änderungsanordnung gegengelesen — wurde alles umgesetzt?
- [ ] Zweitlesung durch zweite Person empfohlen

## 4) Typische Fehler

1. **Inkrafttretens-Verschachtelung übersehen.** Wenn das Änderungsgesetz mehrere Inkrafttretens-Daten hat (typisch bei Übergangsregelungen), braucht es mehrere Lesefassungen.
2. **Verweise nicht nachgezogen.** Wenn Paragraf 3 Absatz 3 entfaellt, muss in Paragraf 7 der Verweis auf "Paragraf 3 Absatz 3" angepasst werden.
3. **Anlagen vergessen.** Bei BGBl-Veröffentlichung sind Anlagen oft separat — leicht zu übersehen.
4. **Standard-Header fehlt.** Adressaten müssen erkennen koennen, **welcher** Stand vorliegt.
5. **DOCX mit Track Changes ausgegeben.** Lesefassung ist per Definition ohne Änderungsmarkierung — Word-Datei vor Export bereinigen.
6. **Zwei Stammgesetze in einer Datei.** Bei einem Änderungsgesetz, das BGB und HGB anpasst, **zwei** Lesefassungen — eine für BGB, eine für HGB.

## 5) Verhältnis zur amtlichen Konsolidierung

Die Lesefassung ist **kein** amtliches Dokument. Die amtliche Konsolidierung erfolgt durch das Bundesministerium der Justiz für die [www.gesetze-im-internet.de](https://www.gesetze-im-internet.de) — meist mit zeitlicher Verzoegerung von einigen Wochen bis Monaten nach Verkündung. Vorläufige Lesefassungen sind sinnvoll, weil:

- die Adressaten früher Klarheit brauchen
- die Vollzugsbehörden die Anwendung vorbereiten müssen
- der parlamentarische Beratungsbedarf ohne Lesefassung erschwert ist

**Wichtig im Header**: Klar machen, dass es sich um eine **Arbeits-Lesefassung** handelt, nicht um den amtlichen Wortlaut.

## 6) Anschluss

- `xml-paralleldarstellung` — bei XML-pflichtigen Veröffentlichungen
- `synopse-erstellen` — für den Änderungs-Diff alt vs. neu
- `dokumente-rendern-docx-pdf` — für den DOCX-/PDF-Export der Lesefassung
- `referentenentwurf-bauen` — bei aenderbarem Entwurfsstand
- `inkrafttreten-uebergangsrecht` — bei stufenweisem Inkrafttreten oder Übergangsregelungen
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 82 GG (Ausfertigung und Verkuendung) — § 1 BGBlG (Bundesgesetzblatt als amtliche Quelle) — §§ 1-5 NormDokVO (Normdokumentations-Verordnung) — Art. 20 Abs. 3 GG (Normklarheit als Rechtsstaatsprinzip)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
