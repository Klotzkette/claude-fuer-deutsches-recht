---
name: prozesskostenhilfe-antrag-schriftsatzkern
description: "Prozesskostenhilfe Antrag Schriftsatzkern im Plugin Fachanwalt Sozialrecht: prüft konkret Anwalt erstellt PKH-Antrag für Sozialgerichtsverfahren und, Substantiierter Schriftsatzkern für Widerspruch + SG-Klage, Eilantrag § 86b SGG, Strukturierte Fallbesprechung für Schulung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Prozesskostenhilfe Antrag Schriftsatzkern

## Arbeitsbereich

**Prozesskostenhilfe Antrag Schriftsatzkern** ordnet den Fall über die tragenden Prüfungslinien: Anwalt erstellt PKH-Antrag für Sozialgerichtsverfahren und, Substantiierter Schriftsatzkern für Widerspruch + SG-Klage, Eilantrag § 86b SGG. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `prozesskostenhilfe-antrag` | Anwalt erstellt PKH-Antrag für Sozialgerichtsverfahren und muss alle Belege korrekt zusammenstellen. § 73a SGG iVm §§ 114 ff. ZPO. Prüfraster: Erklärung persönliche und wirtschaftliche Verhältnisse Formular ZP1a Nachweise Einkommen Vermögen Belastungen Miete Unterhalt. Beiordnungsantrag Rechtsanwalt kein Anwaltszwang vor SG aber Beiordnung möglich. Output: vollständiger PKH-Antrag mit Anlagenverzeichnis. Abgrenzung zu pkh-erfolgsaussicht-prüfen (Vorprüfung Erfolgsaussicht) und klage-sozialgericht. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Widerspruch + SG-Klage, Eilantrag § 86b SGG, Überprüfungsantrag § 44 SGB X: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `schulung-fallbesprechung` | Strukturierte Fallbesprechung für Schulung Inhouse-Fortbildung Referendariats-AG oder Prüfungs-Vorbereitung Fachanwalt Sozialrecht. Nimmt eine bestehende Akte (Bescheid plus medizinische Unterlagen plus Mandantenangaben) und führt die Teilnehmenden durch fuenf Stationen Fall-Triage Bescheidanalyse Strategiebesprechung Schriftsatzwerkstatt Rollenspiel Mandantengespraech. Pro Station kompetenzbasierte Lernziele Diskussionsfragen typische Stolperfallen und Erwartungshorizont. Eignet sich für 90-Minuten Halbtag oder Ganztag. Kompatibel mit der Arbeitsakte sozialrecht-rollstuhl-tannenberg, in der vier disparate Fälle einer Familie parallel bearbeitet werden. |
| `sozialrecht-fallaufnahme-routing` | Master-Routing-Skill der sozialrechtlichen Kanzlei. Nimmt einen frischen Fall an und entscheidet in drei Schritten welche weiteren Skills wann gezogen werden. Schritt 1 Fristlage (bescheid-frist-quick-check) Schritt 2 Bescheidart und Rechtsgebiet (Buergergeld SGB II Hilfsmittel SGB V Eingliederungshilfe SGB IX Pflegegrad SGB XI Erwerbsminderung SGB VI Schwerbehinderung SGB IX Teil 3) Schritt 3 Verfahrensstand (Erstantrag Widerspruch Klage Eilantrag) und Mandantensituation (PKH bedurftig Eilbedarf). Endet mit einer konkreten Skill-Reihenfolge für den vorliegenden Fall und einem Aktenanlage-Eintrag. Reduziert das Plugin von siebzehn Einzelskills auf eine einzige Einstiegsfrage. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGG §§ 51, 78, 87, 90, 130a, 144, 160, 183, 193, SGB I, II, III, V, VI, IX, X; § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch; § 84 SGG Klage; § 87 SGG Eilantrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `prozesskostenhilfe-antrag`

**Fokus:** Anwalt erstellt PKH-Antrag für Sozialgerichtsverfahren und muss alle Belege korrekt zusammenstellen. § 73a SGG iVm §§ 114 ff. ZPO. Prüfraster: Erklärung persönliche und wirtschaftliche Verhältnisse Formular ZP1a Nachweise Einkommen Vermögen Belastungen Miete Unterhalt. Beiordnungsantrag Rechtsanwalt kein Anwaltszwang vor SG aber Beiordnung möglich. Output: vollständiger PKH-Antrag mit Anlagenverzeichnis. Abgrenzung zu pkh-erfolgsaussicht-prüfen (Vorprüfung Erfolgsaussicht) und klage-sozialgericht.

### Prozesskostenhilfe-Antrag (Sozialgericht)

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Prozesskostenhilfe-Antrag (Sozialgericht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Rechtsgrundlagen

- **§ 73a SGG** Verweis auf ZPO-Regeln.
- **§ 114 ZPO** PKH-Voraussetzungen.
- **§ 121 ZPO** Beiordnung eines Rechtsanwalts.
- **§ 117 ff. ZPO** Verfahren und Erklärung.

## Voraussetzungen

### 1. Bedürftigkeit

- Klagepartei kann die Kosten der Prozessführung nicht ganz nicht zum Teil oder nur in Raten aufbringen.
- Prüfung anhand Einkommen Vermögen und unterhaltsberechtigter Personen.
- Sozialleistungsbezug (Bürgergeld Grundsicherung) typisch ausreichend für volle PKH ohne Raten.

### 2. Erfolgsaussicht

- Hinreichende Aussicht auf Erfolg in der Hauptsache (§ 114 Abs. 1 Satz 1 ZPO).
- Maßstab nicht überspannt — es reicht die nicht entfernt liegende Möglichkeit des Erfolgs.

### 3. Nicht Mutwilligkeit

- Die Rechtsverfolgung muss notwendig erscheinen aus Sicht eines verständigen unbedürftigen Drittens.

## Formular ZP1a — Erklärung über die persönlichen und wirtschaftlichen Verhältnisse

Pflichtfelder:

- Persönliche Daten
- Familienverhältnisse Unterhaltspflichten
- Erwerbstätigkeit Einkommen
- Sonstige Einnahmen (Sozialleistungen Kindergeld Unterhalt Rente)
- Vermögen (Konten Bargeld Wertpapiere Lebensversicherung Grundbesitz Fahrzeuge)
- Belastungen (Schulden Unterhalt Wohnen Versicherung Pflege)
- Wohnverhältnisse mit Miete
- Unterschrift mit Belehrung Wahrheit / Strafbarkeit § 124 ZPO

## Pflichtbelege

- Bei Sozialleistungsbezug: aktueller Bewilligungsbescheid.
- Bei Erwerbstätigkeit: letzte drei Lohnabrechnungen.
- Kontoausuege der letzten drei Monate (alle Konten).
- Mietvertrag und Nebenkostenabrechnung.
- Belege Versicherungen und Schulden.
- Bei Schwerbehinderung: Nachweis (kann Vermögensfreibetrag erhöhen).

## Antragstexte

```
An das Sozialgericht XYZ
- Az ...

In der Streitsache ... gegen ...

beantrage ich namens und im Auftrag des Klägers:

1. Bewilligung von Prozesskostenhilfe ohne Ratenzahlung;
2. Beiordnung des unterzeichnenden Rechtsanwalts gemäß § 121 ZPO.

Die Erklärung über die persönlichen und wirtschaftlichen Verhältnisse
(Formular ZP1a) nebst Belegen ist beigefuegt.

Erfolgsaussichten: Begründung siehe Klageschrift vom (Datum) Az (...).

Mutwilligkeit liegt nicht vor.
```

## Sonderfälle

- **Beratungshilfe** § 1 BerHG für das Vorverfahren (Widerspruch) — separater Antrag beim Amtsgericht des Wohnorts.
- **Vereinheitlichte PKH** wenn mehrere zusammenhängende Verfahren — Antrag in jedem Verfahren erforderlich.

## Ausgabe

- `pkh-antrag-<az>-<datum>.docx`.
- ZP1a-Formular ausgefüllt zur Unterschrift des Mandanten.
- Belegliste mit Prüfer-Flag für fehlende Belege.
- Eintrag im Fristenbuch — PKH-Antrag sollte zeitgleich mit Klage oder Widerspruch eingereicht werden.

## Hinweis Prüfer

PKH-Bescheid des Gerichts mit Akte aufheben. Bei Ablehnung: Beschwerde § 127 ZPO iVm § 73a SGG (binnen einer Woche).

## Triage — kläre vor Antragstellung

1. Sozialleistungsbezug (Bürgergeld, Grundsicherung, AsylbLG)? — typischerweise direkt Vollbewilligung ohne Raten
2. Alle Pflichtbelege vollständig? — fehlendes ZP1a-Formular oder Kontoauszüge blockieren PKH-Bewilligung
3. PKH-Antrag zeitgleich mit Klageschrift einreichen? — Antrag vor Urteil muss gestellt sein
4. Beratungshilfe für Vorverfahren (Widerspruch) separat beantragt beim zuständigen AG?
5. PKH-Bescheid nach Bewilligung aufheben? — Änderungspflicht bei Verbesserung der wirtschaftlichen Lage (§ 120 ZPO)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `schriftsatzkern-substantiierung`

**Fokus:** Substantiierter Schriftsatzkern für Widerspruch + SG-Klage, Eilantrag § 86b SGG, Überprüfungsantrag § 44 SGB X: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau.

### Schriftsatzkern und Substantiierung im Sozialrecht (SGB I-XIV)

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Schriftsatzkern und Substantiierung im Sozialrecht (SGB I-XIV)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor Schriftsatz-Erstellung
1. Klage-, Widerspruchs- oder Einspruchsfrist gesichert (Kalender, beA-Sendebestätigung)?
2. Klageart korrekt: Anfechtungs- + Leistungsklage (§ 54 Abs. 4 SGG) für abgelehnte Leistung; reine Anfechtungsklage bei Aufhebungsbescheid?
3. Zuständiges SG (Wohnort des Klägers, § 57 SGG)?
4. Beweisangebote vorhanden (Atteste, Gutachten, Zeugen)? Sozialrecht: Amtsermittlungsgrundsatz (§ 103 SGG), aber Darlegungsobliegenheit bleibt.
5. Prozesskostenhilfe für Mandant erforderlich (§ 73a SGG i.V.m. § 114 ZPO)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Schriftsatz im Bereich Sozialrecht (SGB I-XIV) erstellt werden, typischerweise: Widerspruch + SG-Klage, Eilantrag § 86b SGG, Ueberpruefungsantrag § 44 SGB X.
- Die Mandatsannahme und ggf. Vergleichsverhandlung sind abgeschlossen oder gescheitert.
- Klage-, Widerspruchs-, Einspruchs-, Rechtsmittel-Frist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Parteien (Bezeichnung wie im Vorprozess oder Bescheid, exakte Schreibweise!).
- Zustellungsanschrift Bevollmaechtigte.
- Gericht/Behörde (Zuständigkeit pruefen und im Schriftsatz darstellen, wenn streitig).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Streitwert/Gegenstandswert.

### B. Antraege

Klassischer Antrag-Block; je nach Verfahrenstyp:

- Leistungsantrag (zu zahlen, zu unterlassen, zu beseitigen, herauszugeben).
- Feststellungsantrag (Feststellungsinteresse darlegen).
- Gestaltungsantrag (Aufhebung, Anfechtung, Scheidung).
- Hilfsantraege staffeln (von eng nach weit oder von hoch nach niedrig).

### C. Tatsachenvortrag

Der Substantiierungs-Kern; pro Anspruchsgrundlage in SGB I-XIV, SGG, AsylbLG, BVG, SchwbVwV eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen).
2. **Mandantenseitige Tatsachenbehauptungen** mit Beweisangeboten.
3. **Gegnerisches Verhalten** mit Belegen (Schreiben, Aussage, Verhalten).
4. **Schaden/Folgen** bezifferbar (Hauptforderung, Nebenforderung, Zinsen, Folgekosten).

### D. Rechtliche Wuerdigung

Anspruchsaufbau klassisch:

1. **Anspruchsgrundlage** nennen (z.B. § X iVm § Y).
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal wird gegen den Tatsachenvortrag gespiegelt.
3. **Einwendungen** der Gegenseite vorwegnehmen und entkraeften.
4. **Rechtsprechungs-Verweise:** BAG/BGH/BVerfG/EuGH/BFH je nach Fachgebiet; bei Sozialrecht (SGB I-XIV) typischerweise die letzte hoechstrichterliche Linie zitieren.
5. **Subsumtion-Ergebnis** klar formulieren.

### E. Beweisangebote

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- Urkundenbeweis: konkrete Anlage Kxx benennen, Inhalt nicht nur "Vertrag" sondern "Vertrag vom TT.MM.JJJJ, dort § X Abs. Y, Anlage K1".
- Zeugenbeweis: Name, ladungsfaehige Anschrift, Beweisthema in einem Satz.
- Sachverstaendigenbeweis: ggf. Privatgutachten mit anfuegen, gerichtliches Gutachten beantragen.
- Parteivernehmung als letzte Stufe, mit Antrag § 448 ZPO und Indiziengeruest.
- Inaugenscheinnahme: bei Sache vor Ort (Mietraum, Baustelle, Fahrzeug, Hardware).

### F. Anlagenverzeichnis

- K1, K2 ... durchnummeriert (Antragstellerin/Klaegerin).
- Bei Beklagten B1, B2 ...
- Jede Anlage mit Datum, Absender, Empfaenger, Inhaltsbeschreibung in einem Satz.
- Pflicht-Erwaehnung im Tatsachenvortrag.

## Substantiierungs-Fallen im Sozialrecht (SGB I-XIV)

- **Pauschaltatsachen** ohne konkrete Daten ("seit Jahren", "regelmaessig", "in mehreren Faellen") werden vom Gericht uebergangen.
- **Beweisangebot zur falschen Tatsache:** Beweisthema deckt nur Teilaussage ab.
- **Selbst-widersprueche** zwischen Schriftsatz und Anlage ("Im Vertrag steht doch was anderes").
- **Verspaeteter Vortrag** § 296 ZPO/§ 87b VwGO: Rueglich-Fristen beachten, Verschulden vermeiden.
- **Anspruchskonkurrenz** zwischen mehreren Grundlagen: nicht eine wegfallen lassen.

## Pruefkette vor Versand

1. Antragsformulierung tenoriert (urteilstauglich, vollstreckbar)?
2. Jede Tatbestandsmerkmal-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Eingangsstempel/elektronische Uebermittlung)?
4. Zuständigkeit positiv festgestellt?
5. Streitwert plausibel, ggf. mit Anlage Streitwert-Berechnung?
6. Anlagenverzeichnis vollstaendig und nummerisch konsistent?
7. beA-/EGVP-/EBO-Konformitaet (PDF/A, ERVV-Signatur)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Anwaeltin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG, BGH, BAG, BFH, BVerwG, EuGH und die jeweils massgeblichen Fachsenate für Sozialrecht (SGB I-XIV).
- SGB I-XIV, SGG, AsylbLG, BVG, SchwbVwV sowie Verordnungen/Richtlinien dazu.
- Aktuelle Reform- und Gesetzgebungslage einbeziehen.

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisangeboten, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht, EB).
4. **Streitwertskizze** (eigenes Memo, falls > 1 Anspruch).
5. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger?).

## Beispiel-Anspruchsgrundlagen im Sozialrecht (SGB I-XIV)

Drei haeufig gebrauchte Anspruchsgrundlagen aus SGB I-XIV, SGG, AsylbLG, BVG, SchwbVwV und ihre Substantiierungs-Anforderungen:

### Grundlage 1

- Tatbestandsmerkmal 1: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 2: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 3: konkrete Tatsache + Beweis.
- Rechtsfolge: konkreter Antrag.

### Grundlage 2

Analog - jede Tatsache braucht ein Beweisangebot.

### Grundlage 3 (Auffanggrundlage / Sekundaeranspruch)

Hilfsweise vortragen, klar als Hilfsantrag/Hilfsvortrag kennzeichnen.

## Antrags-Muster nach Verfahrenstyp

Typische Antraege in Sozialrecht (SGB I-XIV) (Widerspruch + SG-Klage, Eilantrag § 86b SGG, Ueberpruefungsantrag § 44 SGB X):

- Hauptantrag (Leistung/Feststellung/Gestaltung).
- Hilfsantrag (z.B. für den Fall, dass Hauptforderung verjaehrt ist).
- Annex-Antraege (Zinsen, Nebenforderungen, Kosten).
- Streitwert-Antrag (falls Streitwert streitig).

## Beweisaufnahme - was das Gericht sehen will

### Urkundenbeweis

- Anlage K1: Bezeichnung, Datum, kurze Inhaltsbeschreibung.
- Im Tatsachenvortrag: "Diese Behauptung beruht auf dem als Anlage K1 vorgelegten Schreiben der Beklagten vom TT.MM.JJJJ, dort Seite Y, Absatz Z."

### Zeugenbeweis

- Form: "Beweis: Aussage der Zeugin Name, ladungsfaehige Anschrift, zum Beweisthema (konkret in einem Satz)."
- Mehrere Zeuginnen zum gleichen Thema: Indiziengeruest staerken.
- Keine Beweisermittlung ueber Zeugnis - das Beweisthema muss konkret sein.

### Sachverstaendigenbeweis

- Bei Sozialrecht (SGB I-XIV)-typischen Streitfaellen oft notwendig (Bauwerk, IT-System, Anlagebewertung, medizinische Frage).
- Privatgutachten als Anlage K vorlegen + zugleich gerichtliches Gutachten beantragen.
- Verfahrensoekonomie: Sachverstaendigen-Kosten frueh mit Mandantin besprechen.

### Parteivernehmung (§ 448 ZPO)

- Letzte Stufe, nur wenn andere Beweismittel ausgeschoepft.
- Indiziengeruest vortragen, das eine gewisse Wahrscheinlichkeit der Behauptung tragt.

## Replik-/Duplik-Vorausschau

Schon im Klageschriftsatz die wahrscheinlichen Einwaende der Gegenseite vorwegnehmen:

- Verjährung -> Hemmungstatbestand vortragen.
- Erfuellung/Aufrechnung -> rechtzeitige Tatsachenbasis schaffen.
- Formmangel -> Heilung/Schutz-Argument bereit halten.
- Treuwidrigkeit -> Indiziengeruest gegen Treuwidrigkeits-Vorwurf.

## Elektronische Einreichung (beA, EGVP, EBO, ELSTER)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- 1.10.2026 / 1.10.2027 - ZVollstrDigitG-Aenderungen im Vollstreckungsbereich; in Sozialrecht (SGB I-XIV) ggf. spezifische ERV-Pflichten beachten.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln ("Die Klage ist zulaessig und begruendet" als Ueberschrift, aber dann substantiieren).
- Mandanten- und Beweismittel-Zitate woertlich, in Anfuehrungszeichen, mit Anlage-Verweis.
- Keine Gefuehlsausbrueche - sachlich auch bei provokanter Gegenseite.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag tenorierungsfaehig
- [ ] Frist gewahrt mit Reserve
- [ ] Jede Tatsache hat Beweis
- [ ] Anlagen vollstaendig und nummeriert
- [ ] Rechtsprechungs-Zitat aktuell
- [ ] Streitwert plausibel
- [ ] beA/EGVP-konform
- [ ] Senior-/Sozius-Freigabe

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Tatsachen-Grundlage und Streitwertskizze.
- `vergleichsverhandlung-strategie` (im selben Plugin) für parallelen Vergleichsversuch (Gueteverhandlung, Mediation).

## 3. `schulung-fallbesprechung`

**Fokus:** Strukturierte Fallbesprechung für Schulung Inhouse-Fortbildung Referendariats-AG oder Prüfungs-Vorbereitung Fachanwalt Sozialrecht. Nimmt eine bestehende Akte (Bescheid plus medizinische Unterlagen plus Mandantenangaben) und führt die Teilnehmenden durch fuenf Stationen Fall-Triage Bescheidanalyse Strategiebesprechung Schriftsatzwerkstatt Rollenspiel Mandantengespraech. Pro Station kompetenzbasierte Lernziele Diskussionsfragen typische Stolperfallen und Erwartungshorizont. Eignet sich für 90-Minuten Halbtag oder Ganztag. Kompatibel mit der Arbeitsakte sozialrecht-rollstuhl-tannenberg, in der vier disparate Fälle einer Familie parallel bearbeitet werden.

### Schulungs-Fallbesprechung — Trainerleitfaden

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Schulungs-Fallbesprechung — Trainerleitfaden` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

Du fuehrst eine Schulung. Dieser Skill macht aus jedem Realfall oder einer Testakte ein nachvollziehbares Training mit fünf Stationen.

## Setup

- Teilnehmende: 3 bis 15 (mehr — Untergruppen)
- Dauer: 90 Minuten (Kurz) / 4 Stunden (Halbtag) / 7 Stunden (Ganztag)
- Material: Bescheid, Atteste, Mandanteninfo, Flipchart, Skill-Plugin geladen
- Vorbereitung: 30 Minuten Trainer-Vorbereitung

## Fünf Stationen

### Station 1 — Fall-Triage (15 Minuten)

**Lernziel:** Teilnehmende koennen aus rohen Mandanteninformationen die rechtlich relevanten Achsen identifizieren.

**Methode:** Teilnehmende lesen die Mandantennotiz ohne den Bescheid. Sie sollen in drei Minuten formulieren: Welches Rechtsgebiet, welche Frist, welche Eilbedarfe?

**Skill-Bezug:** `sozialrecht-fallaufnahme-routing` und `bescheid-frist-quick-check`

**Stolperfallen:**
- Mehrere Rechtsgebiete gleichzeitig (Tannenberg-Familie hat vier)
- Frist wird mit Bescheid-Datum verwechselt statt mit Zugang
- Eilbedarf wird unterschaetzt (Hilfsmittel als Standardfall)

**Diskussionsfrage:** "Was waere die schlechteste Entscheidung in dieser Stunde?"

**Erwartungshorizont:** Routing-Karte ausfuellen.

### Station 2 — Bescheidanalyse (30 Minuten)

**Lernziel:** Teilnehmende koennen formell und materiell systematisch prüfen.

**Methode:** Jede Untergruppe analysiert je einen Bescheid. Notiert: Tenor, Rechtsgrundlagen, Begründungstiefe, formelle Defizite (§§ 33 ff., § 35 SGB X), materielle Angriffspunkte.

**Skill-Bezug:** `bescheidanalyse`, je nach Fall `hilfsmittelantrag-pruefen`, `pflegegrad-widerspruch`, `erwerbsminderungsrente-pruefen`, `schwerbehindertenausweis-gdb`, `eingliederungshilfe-schule`

**Stolperfallen:**
- Anhörung § 24 SGB X vergessen
- Begründung der Begründung — überlasen Standardformeln
- Wechselwirkungen zwischen Bescheiden derselben Familie nicht erkannt

**Erwartungshorizont:** Bescheid-Prüfraster pro Fall.

### Station 3 — Strategiebesprechung (20 Minuten)

**Lernziel:** Teilnehmende entscheiden zwischen Widerspruch, Eilantrag, Akteneinsicht, PKH-Antrag, ergänzendem Antrag § 44 SGB X.

**Methode:** Mandantengespräch-Simulation am Tisch. Wer ist die Person hinter dem Bescheid? Was ist das tatsächliche Ziel? Ist Geld da für Anwalt?

**Skill-Bezug:** `pkh-erfolgsaussicht-pruefen`, `eilantrag-sozialrecht`, `akteneinsicht-anfordern`

**Stolperfallen:**
- Eilantrag ohne Anordnungsgrund
- PKH ohne Erfolgsaussichten-Prüfung beantragt
- Strategie ohne Mandanten-Ressourcen-Check

**Diskussionsfragen:**
- Was hätte die Anwältin am ersten Tag tun müssen?
- Wann macht man eine Sammel-Strategie über mehrere Familienmitglieder hinweg?
- Wann lieber Einzel-Akten?

### Station 4 — Schriftsatzwerkstatt (45 Minuten Halbtag / 90 Minuten Ganztag)

**Lernziel:** Teilnehmende schreiben einen Widerspruch.

**Methode:** Jeder Teilnehmende erhaelt einen Fall plus die Bescheidanalyse aus Station 2. Schreibt einen Widerspruch dem Grunde nach (15 Minuten), dann mit Begründung (30 Minuten), dann mit Anlagenverzeichnis (15 Minuten).

**Skill-Bezug:** `widerspruch-formulieren`, `anlagen-erstellen`

**Stolperfallen:**
- Antrag fehlt oder ist unklar
- Begründung wiederholt nur die Mandantenklage statt zu argumentieren
- Anlagen falsch nummeriert (W1 W2 W3 vs. K1 K2)
- Vollmacht vergessen

**Trainerfeedback:** Nach 30 Minuten Tauschpartner, gegenseitig korrigieren.

### Station 5 — Rollenspiel Mandantengespräch (20 Minuten)

**Lernziel:** Teilnehmende koennen den eigenen Schriftsatz dem Mandanten erklären.

**Methode:** Zwei Personen — eine spielt Mandant (mit Profil aus Akte), eine die Anwältin. Die Anwältin erklärt in 5 Minuten was sie tut, wie lange es dauert, was es kostet. Wechsel.

**Skill-Bezug:** `mandantenbrief-leichte-sprache`

**Stolperfallen:**
- Fachsprache ohne Erklärung
- Erfolgsaussichten geschoent
- Kostenrisiko nicht erwaehnt
- Kein konkreter nächster Schritt für den Mandanten

## Trainer-Werkzeuge

### Eisbrecher zum Start

"Wenn ein Bescheid in Ihrer Kanzlei eingeht — was tun Sie in den ersten 60 Sekunden? Drei Worte." (Sammlung an Flipchart — Frist, Zugang, Mandant, Rechtsgebiet …)

### Auflocker

"Welcher Skill aus dem Plugin würden Sie noch erfinden?"

### Abschlussfrage

"Was nehmen Sie morgen Vormittag in Ihre Kanzlei mit?"

## Bewertungsraster für Trainer

| Kompetenz | Anfaenger | Fortgeschritten | Expert |
|---|---|---|---|
| Fristberechnung | Datum auf dem Bescheid | Bekanntgabe-Fiktion einbezogen | Wiedereinsetzung mitgedacht |
| Bescheidanalyse | Tenor erfasst | Anhörung und Begründung geprüft | Wechselwirkung mehrerer Bescheide erkannt |
| Widerspruchsbegründung | Verweist auf Norm | Subsumtion sauber | Beweisanträge strukturiert |
| Mandantenkommunikation | Verstaendlich | Verfahrenstransparent | Empathisch und gerechnet |

## Anwendungs-Setting Tannenberg

Die Testakte `sozialrecht-rollstuhl-tannenberg` ist auf vier Familienmitglieder ausgelegt — Olaf (Rollstuhl, SGB V), Margarete Mutter (Pflegegrad, SGB XI), Lena Tochter (Schulbegleitung, SGB VIII/IX), Bodo Schwager (EM-Rente, SGB VI). Eine Schulung kann eine 90-Minuten-Variante mit einem Fall oder eine 4-Stunden-Variante mit allen vier durchspielen. Im Workflow-Vermerk der Testakte sind die Stationen mit konkreten Materialhinweisen verknuepft.

## Anschluss-Skills

- alle aufgerufenen Skills je Station
- `fristenbuch-sozialrecht` als Eintrag "heute Schulung durchgeführt"

## Triage — kläre vor der Schulung

1. Zielgruppe (Referendare, Fachanwalt-Lehrgang, Inhouse-Fortbildung, Beratungsstellenmitarbeiter)?
2. Wieviel Zeit steht zur Verfügung (90 Minuten / Halbtag / Ganztag)?
3. Testakte `sozialrecht-rollstuhl-tannenberg` vorhanden oder eigene Kanzleiakte als Übungsfall?
4. Wird Rollenspiel Station 5 durchgeführt? — dann mindestens sechs Teilnehmende empfohlen
5. Werden Schriftsätze aus Station 4 benotet oder nur als Feedback besprochen?

## Aktuelle Rechtsprechung — didaktische Querschnittsnormen für Schulungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 4. `sozialrecht-fallaufnahme-routing`

**Fokus:** Master-Routing-Skill der sozialrechtlichen Kanzlei. Nimmt einen frischen Fall an und entscheidet in drei Schritten welche weiteren Skills wann gezogen werden. Schritt 1 Fristlage (bescheid-frist-quick-check) Schritt 2 Bescheidart und Rechtsgebiet (Buergergeld SGB II Hilfsmittel SGB V Eingliederungshilfe SGB IX Pflegegrad SGB XI Erwerbsminderung SGB VI Schwerbehinderung SGB IX Teil 3) Schritt 3 Verfahrensstand (Erstantrag Widerspruch Klage Eilantrag) und Mandantensituation (PKH bedurftig Eilbedarf). Endet mit einer konkreten Skill-Reihenfolge für den vorliegenden Fall und einem Aktenanlage-Eintrag. Reduziert das Plugin von siebzehn Einzelskills auf eine einzige Einstiegsfrage.

### Master-Routing — Sozialrechtskanzlei

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Master-Routing — Sozialrechtskanzlei` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

Du bist die zentrale Triage. Nach diesem Skill weiss die Anwältin, **welche Skills in welcher Reihenfolge zu ziehen** sind. Nie wieder "welches Werkzeug zuerst?" — diese Frage beantwortest du.

## Eingangs-Frage an Mandantin oder Anwältin

Stelle die folgenden vier Fragen, sofort und kompakt, eine nach der anderen — keine Sammelabfrage:

1. **Datum des Bescheids und Datum des Zugangs?** (oder: kein Bescheid, sondern Erstantrag)
2. **Welche Behörde, welche Leistung?** (Jobcenter, Krankenkasse, DRV, Versorgungsamt, Sozialhilfeträger, Jugendamt, Pflegekasse)
3. **Verfahrensstand?** (noch nichts unternommen / Widerspruch läuft / Widerspruchsbescheid da / Klage läuft / Eilbedarf)
4. **Bedraengnis?** (sofortige Existenznot, Hilfsmittel dringend, Verlust Schulplatz, Kündigung Wohnung wegen Heizkostenstreit, Pflege bricht zusammen)

## Entscheidungsbaum

### Schritt 1 — Fristlage zuerst

Ziehe **`bescheid-frist-quick-check`** sofort. Ergebnisse:

| Fristlage | Sofortiger nächster Skill |
|---|---|
| Frist offen, mehr als 14 Tage | `bescheidanalyse` → `widerspruch-formulieren` |
| Frist offen, weniger als 14 Tage | `widerspruch-formulieren` (Kurzfassung) parallel `akteneinsicht-anfordern` |
| Frist verstrichen, weniger als 14 Tage drüber | `widerspruch-formulieren` plus Wiedereinsetzung § 67 SGG |
| Frist verstrichen, mehr als 14 Tage | Prüfen Überprüfungsantrag § 44 SGB X — eigenständiger Pfad |
| Eilbedarf (Existenz, Hilfsmittel, Schule) | `eilantrag-sozialrecht` **parallel** zum Widerspruch |

### Schritt 2 — Bescheidart und Rechtsgebiet

Mappe das Rechtsgebiet auf den Fachmodul:

| Rechtsgebiet | Fachmodul | Hauptnormen |
|---|---|---|
| Bürgergeld SGB II | `buergergeld-pruefen` | §§ 19 ff. SGB II |
| Hilfsmittel SGB V (Rollstuhl, Hörhilfe, Lift) | `hilfsmittelantrag-pruefen` | § 33 SGB V, §§ 47 ff. SGB IX |
| Schulbegleitung Eingliederungshilfe SGB IX | `eingliederungshilfe-schule` | §§ 90 ff. SGB IX, § 35a SGB VIII |
| Pflegegrad SGB XI | `pflegegrad-widerspruch` | §§ 14, 15 SGB XI, MD-Begutachtung |
| Erwerbsminderungsrente SGB VI | `erwerbsminderungsrente-pruefen` | §§ 43, 240 SGB VI |
| Schwerbehinderung GdB Merkzeichen | `schwerbehindertenausweis-gdb` | § 152 SGB IX, VersMedV |
| Asylbewerberleistungen | (allgemein `bescheidanalyse` plus `widerspruch-formulieren`) | §§ 1a–3 AsylbLG |

### Schritt 3 — Verfahrensstand und Mandantensituation

Lege fest, ob folgende Querschnitt-Skills heute noch anzustoßen sind:

- **`akteneinsicht-anfordern`** — bei jedem Bescheid mit medizinischer oder gutachterlicher Grundlage, sofort parallel
- **`pkh-erfolgsaussicht-pruefen`** plus **`prozesskostenhilfe-antrag`** — wenn Klage absehbar und Mandant bedurftig
- **`fristenbuch-sozialrecht`** — Eintrag noch heute, kein Tag später
- **`anlagen-erstellen`** — sobald drei oder mehr Belege im Spiel sind
- **`mandantenbrief-leichte-sprache`** — wenn Mandant Bescheid nicht versteht oder kognitive Beeintraechtigung vorliegt

## Output-Format

Liefere eine **Routing-Karte** im folgenden Format:

```
ROUTING-KARTE — Az [intern] — [Mandant] — [Datum]

Fristlage: [offen / knapp / verstrichen / Eilbedarf]
Rechtsgebiet: [SGB X]
Verfahrensstand: [Erstbescheid / Widerspruch / Klage]
Eilbedarf: [ja / nein, Begruendung]

REIHENFOLGE HEUTE
1. [Skill A] — Ergebnis = X
2. [Skill B] — Ergebnis = Y
3. Fristenbuch-Eintrag

REIHENFOLGE DIESE WOCHE
4. [Skill C]
5. [Skill D]

PARALLEL
- Akteneinsicht (ja/nein + Begruendung)
- PKH (ja/nein)
- Eilantrag (ja/nein)

MANDANTENINFORMATION
- Naechste Rueckmeldung an Mandant bis [Datum]
- Pflichtinfo: [Frist X laeuft am Y ab]
```

## Anwendungsbeispiel — Familie Tannenberg

In der Testakte `sozialrecht-rollstuhl-tannenberg` liegen vier Fälle in einer Familie. Wende die Routing-Karte je Fall einmal an. Du wirst sehen: vier sehr unterschiedliche Pfade trotz einem Plugin.

## Hinweise

- Du sprichst die Anwältin direkt an, nicht den Mandanten.
- Nie raten — wenn ein Datum fehlt, frage nach.
- Wiedereinsetzung § 67 SGG ist Ausnahme, kein Standardpfad. Wirklich nur bei unverschuldeter Verzoegerung.
- Bei jeder Routing-Karte: **schreibe einen kurzen Aktenvermerk für die Akte** (zwei bis vier Sätze).
- Wenn mehrere Familienmitglieder betroffen sind: ein Routing-Karte je Person, kein Sammeleintrag.

## Aktuelle Rechtsprechung — Routing-Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
