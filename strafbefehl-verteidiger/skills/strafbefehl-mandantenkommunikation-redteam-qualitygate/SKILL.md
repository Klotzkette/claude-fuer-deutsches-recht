---
name: strafbefehl-mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation Redteam Qualitygate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenkommunikation Redteam Qualitygate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenkommunikation Redteam Qualitygate** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin strafbefehl-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin strafbefehl-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `strafbefehl-rechtsprechungsrecherche` | Rechtsprechung zum Strafbefehlsverfahren recherchieren für Schriftsaetze oder Argumentation in der Hauptverhandlung. Prüfraster BGH OLG-Rspr zu §§ 407-412 StPO Einspruch Wiedereinsetzung Strafzumessung. Normen §§ 407 408 410 412 StPO. Datenbankrecherche juris beck-online OpenJur Suchstrategien Normenkette. Output aufbereitete Kernzitate für Schriftsaetze mit Aktenzeichen und Leitsatz. Abgrenzung: strafbefehl-beweis-und-einlassung für die inhaltliche Verteidigungsstrategie. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Mandantenkommunikation Redteam Qualitygate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin strafbefehl-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin strafbefehl-verteidiger: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Strafbefehl-Mandantenkommunikation Speziallage
- **Pflicht-Aufklaerung sofort:**
 - **Verteidigerbestellung** § 137 StPO; Schweigerecht § 136 StPO.
 - **Frist § 410 StPO: 2 Wochen** ab Zustellung - bei Versaeumnis Rechtskraft und Vollstreckung; Wiedereinsetzung § 44 StPO oft nicht moeglich.
 - **Rechtsfolgen Akzeptanz Strafbefehl:** wird **rechtskraeftig wie Urteil** (§ 410 III StPO); BZRG-Eintrag; FAER-Punkte bei Verkehrsdelikten; berufsrechtliche Folgen.
- **Entscheidungsmatrix Einspruch ja/nein:**
 - **Tatsachenstreit:** wenn Mandant die Tat bestreitet oder erhebliche Beweisluecken bestehen - Einspruch sinnvoll, ggf. Beweisaufnahme in Hauptverhandlung.
 - **Strafmass-Streit:** Einspruch beschraenkt auf Rechtsfolgenausspruch § 410 II StPO; nur Tagessatzhoehe / Fahrverbot streitig.
 - **Einstellung anstreben:** §§ 153, 153a StPO im Strafbefehlsverfahren noch moeglich - Verhandlung mit StA / Gericht.
 - **Akzeptanz:** wenn Strafmass im Rahmen, keine erheblichen Nebenfolgen, Hauptverhandlung wuerde Beweise gegen Mandant erbringen.
- **Berufsspezifische Konsequenzen** stets ansprechen:
 - **Beamte/Soldaten:** Disziplinarrecht, Anzeigepflicht; ab Geldstrafe oft Verfahren.
 - **Aerzte/Anwaelte/Steuerberater/Apotheker:** Berufsaufsicht.
 - **Lehrer:** Schulaufsicht.
 - **Fuehrungsfunktionen Wirtschaft:** Reputation.
- **Kostenhinweis RVG:** VV 4100 (Grundgebuehr), 4106 (Verfahrensgebuehr Strafbefehlsverfahren), 4108 (Verfahrensgebuehr Einspruch), 4112 ff. (Terminsgebuehr); Pflichtverteidigergebuehren bei Verurteilung als Verfahrenskosten dem Mandant.
- **Mandantenfreigabe schriftlich** fuer: Einspruch, Einspruchsruecknahme, Beschraenkung, Annahme Auflagen § 153a StPO, Verstaendigung § 257c StPO.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin strafbefehl-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin strafbefehl-verteidiger: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Strafbefehl-Red-Team-Checks
- **Frist-Re-Check § 410 StPO:** Zustellungsdatum aus Postzustellungsurkunde / Empfangsbekenntnis verifizieren; **2 Wochen Einspruchsfrist** nicht verwechseln mit 1 Woche Beschwerde.
- **Strafbefehlsvoraussetzungen § 407 StPO** re-check: nur Vergehen (§ 12 II StGB); Strafrahmen passend? Freiheitsstrafe ueber 1 Jahr im Strafbefehl unzulaessig - Verteidiger und Bewaehrung Pflicht bei 6 Monate bis 1 Jahr Freiheitsstrafe.
- **Einspruchsbeschraenkung § 410 II StPO** geprueft? Beschraenkung auf Rechtsfolgenausspruch oft strategisch sinnvoll (z. B. nur Tagessatzhoehe oder Fahrverbot).
- **Verfahrensalternativen geprueft?** §§ 153, 153a StPO Einstellung gegen Auflagen; § 154 StPO Teileinstellung; § 154a StPO Beschraenkung; § 257c StPO Verstaendigung - oft bessere Loesung als Hauptverhandlung.
- **Konsequenz-Re-Check:** BZRG-Eintrag (regelmaessig ab 91 TS / Freiheitsstrafe); FAER bei Verkehrsdelikten; berufsrechtliche Folgen (Beamte, Aerzte, Anwaelte) - Mandant informiert?
- **Halluzinations-Check:** keine erfundenen Az BGH; "staendige Rspr." statt konkret Az aus Modellwissen.
- **Vollmachts-Check:** Vertretungsvollmacht fuer § 411 II StPO Hauptverhandlung? Sonst Versaeumnisurteil moeglich (§ 412 StPO).
- **Halterauskunft / Fahrtenbuchauflage** Risiko angesprochen bei Verkehrs-Strafbefehl mit nicht ermittelbarem Fahrer?

## 3. `strafbefehl-rechtsprechungsrecherche`

**Fokus:** Rechtsprechung zum Strafbefehlsverfahren recherchieren für Schriftsaetze oder Argumentation in der Hauptverhandlung. Prüfraster BGH OLG-Rspr zu §§ 407-412 StPO Einspruch Wiedereinsetzung Strafzumessung. Normen §§ 407 408 410 412 StPO. Datenbankrecherche juris beck-online OpenJur Suchstrategien Normenkette. Output aufbereitete Kernzitate für Schriftsaetze mit Aktenzeichen und Leitsatz. Abgrenzung: strafbefehl-beweis-und-einlassung für die inhaltliche Verteidigungsstrategie.

# Rechtsprechungsrecherche im Strafbefehlsverfahren

## Triage zu Beginn

1. **Was ist die Rechtsfrage?** — Zulaessigkeit des Strafbefehls? Einspruchsfrist? Tagessatz? Fahrerlaubnis? Rechtsfrage klar formulieren.
2. **Welches Gericht ist zustaendig?** — BGH fuer grundsaetzliche Fragen; OLG fuer Revisionsentscheidungen vom AG; jeweilige Ober- und Bundesgerichte.
3. **Zeitraum der Recherche?** — Aktuelle Rechtsprechung (letzte 5 Jahre) hat Prioritaet; aeltere BGH-Grundsatzentscheidungen bleiben aber relevant.
4. **Datenbank verfuegbar?** — amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, OpenJur (kostenlos), LexisNexis, Wolters Kluwer.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen-Recherchekette

```
Strafbefehlsverfahren §§ 407-412 StPO:
§ 407 StPO → Zulaessigkeit
§ 408 StPO → Richterliche Entscheidung
§ 409 StPO → Pflichtinhalt
§ 410 StPO → Einspruch, Frist, Beschraenkung
§ 411 StPO → Hauptverhandlung nach Einspruch
§ 412 StPO → Verwerfung bei Ausbleiben

Querschnitt:
§ 44 StPO → Wiedereinsetzung
§ 140 StPO → Notwendige Verteidigung
§ 244 StPO → Beweisantragsrecht
§ 257c StPO → Verstaendigung
§§ 40, 46 StGB → Strafzumessung
§ 69, 69a StGB → Fahrerlaubnis-Entziehung
§ 44 StGB → Fahrverbot
```

## Suchstrategien fuer Datenbanken

**amtliche/freie Quellen oder lizenzierte Datenbanken:**
- Normen-Suche: "§ 410 StPO" + "Einspruch" + "Frist"
- Aktenzeichen-Suche direkt wenn vorhanden
- Freitext: "Strafbefehl Wiedereinsetzung Verschulden"
- Gericht-Filter: BGH, OLGs, BVerfG

**OpenJur (kostenlos):**
- URL: openjur.de → Suchbegriff eingeben
- Volltext-Suche nach Normen

**Google Scholar (Rechtsprechung):**
- "§ 410 StPO Einspruchsfrist BGH"
- Zeitraum-Filter setzen

## Kernrechtsprechung Strafbefehlsverfahren

Vorbemerkung: Die unten genannten Fundstellen stammen aus geschlossenen Verlagsprodukten (NStZ, NStZ-RR, NZV). Sie dürfen nach der Quellen-Regel dieses Repositoriums nicht aus Modellwissen zitiert werden. Wer die Entscheidung verwenden will, verifiziert Aktenzeichen und Aussage vor Versand des Schriftsatzes in dejure.org oder openjur.de. Die folgenden Stichworte dienen nur als Recherche-Anker, nicht als Zitat.

### § 407/409 StPO — Zulaessigkeit und Inhalt
- Recherche-Anker: Verbrechen schliesst Strafbefehl aus (Nichtigkeit) — in dejure.org "§ 407 StPO Verbrechen Nichtigkeit" suchen
- Recherche-Anker: Freiheitsstrafe ohne Bewaehrung unzulaessig — in dejure.org "§ 407 Abs. 2 StPO Freiheitsstrafe Bewaehrung" suchen
- Recherche-Anker: Tatbeschreibung muss Art. 103 Abs. 2 GG genuegen — in dejure.org "§ 409 StPO Tatbeschreibung Bestimmtheit" suchen

### § 410 StPO — Einspruch und Frist
- Recherche-Anker: Zustellungsfiktion § 180 ZPO im Strafbefehlsverfahren — in dejure.org "§ 410 StPO § 180 ZPO Zustellungsfiktion" suchen
- Recherche-Anker: Beschraenkter Einspruch bindet das Gericht — in dejure.org "§ 410 Abs. 2 StPO beschraenkter Einspruch" suchen

### § 44 StPO — Wiedereinsetzung
- Recherche-Anker: Gericht-Fehler bei Fristberechnung schliesst Verschulden aus — in dejure.org "§ 44 StPO Wiedereinsetzung Gerichtsfehler" suchen

### Strafzumessung
- Recherche-Anker: Tagessatzhoehe nach tatsaechlichem Nettoeinkommen — in dejure.org "§ 40 StGB Tagessatz Nettoeinkommen" suchen
- Recherche-Anker: Schaetzungsrecht erst nach Ausschoepfung der Ermittlung — in dejure.org "§ 40 Abs. 3 StGB Schaetzung Ausschoepfung" suchen

### Aktualisierungen Stand Mai 2026
- BGH (GSSt) 03.02.2025 — GSSt 1/24 (KCanG, Cannabisbesitz/Handeltreiben, sanktionsfreie Mengen): Beim KCanG-Strafbefehl ist die sanktionsfreie Eigenkonsummenge sowohl bei der Schuldfrage als auch in der Einziehung zu berücksichtigen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- BGH 15.07.2025 — 2 StR 644/24 (KCanG-Strafzumessung): Die in § 1 Nr. 8 ff. KCanG enthaltene gesetzliche Wertung ist bestimmender Strafzumessungsgrund. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24

## Schritt-fuer-Schritt-Recherche-Workflow

1. **Rechtsfrage praezisieren:** "Wann beginnt die Einspruchsfrist bei Einwurf-Einschreiben?" (nicht pauschal: "Frist").
2. **Normenkette aufbauen:** §§ 410, 37 StPO, 180 ZPO.
3. **Datenbanksuche mit Normen-Kombination:** "§ 410 StPO" + "§ 180 ZPO" + "Zustellung".
4. **Treffer sichten:** 3-5 relevante Entscheidungen identifizieren; Aktenzeichen + Datum + Fundstelle notieren.
5. **Kernaussage paraphrasieren:** 1-2 Saetze verstaendlich; nie wortgleich kopieren.
6. **In Schriftsatz einbauen:** Aktenzeichen, Datum, Gericht, Fundstelle immer vollstaendig.

## Fundstellen-Abkuerzungen

| Abkuerzung | Zeitschrift |
|-----------|------------|
| NStZ | Neue Zeitschrift fuer Strafrecht |
| NStZ-RR | NStZ-Rechtsprechungs-Report |
| NJW | Neue Juristische Wochenschrift |
| NZV | Neue Zeitschrift fuer Verkehrsrecht |
| JZ | Juristenzeitung |
| StV | Strafverteidiger |
| BGHZ | Entscheidungen BGH Zivilsachen |
| BGHSt | Entscheidungen BGH Strafsachen |

## Harte Leitplanken

- Keine erfundenen Aktenzeichen oder Fundstellen verwenden.
- Wenn Entscheidung nicht auffindbar: konservativen Klassiker nennen oder weglassen.
- Paraphrase nicht wortgleich aus Urteil kopieren.
- Anwaltliche Endkontrolle bei allen Zitaten in Schriftsaetzen.
