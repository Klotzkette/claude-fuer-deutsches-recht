---
name: aufenthaltstitel-ausweisung-start
description: "Aufenthaltstitel Ausweisung Start im Migrationsrecht: prüft konkret Aufenthaltstitel-Router, Ausweisung Start, Behördenkommunikation, Bescheid verstehen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Aufenthaltstitel Ausweisung Start

## Arbeitsbereich

**Aufenthaltstitel Ausweisung Start** ordnet den Fall über die tragenden Prüfungslinien: Aufenthaltstitel-Router, Ausweisung Start, Behördenkommunikation. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-aufenthaltstitel-router` | Aufenthaltstitel-Router: Prüfungslinie für Migrationsrecht; wählt Visum, Aufenthaltserlaubnis, Blaue Karte, ICT, Chancenkarte, NE, Daueraufenthalt; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-ausweisung-start` | Ausweisung Start: Prüfungslinie für Migrationsrecht; prüft Ausweisungsinteresse, Bleibeinteresse, Verhältnismäßigkeit und EMRK; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-behoerdenkommunikation` | Behördenkommunikation: Prüfungslinie für Migrationsrecht; formuliert knappe Schreiben an ABH, BAMF, Botschaft oder Gericht; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-bescheid-verstehen` | Bescheid verstehen: Prüfungslinie für Migrationsrecht; erkennt aus Bescheid, Rechtsbehelfsbelehrung und Zustellung die nächsten Schritte; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-blaue-karte-start` | Blaue Karte EU Start: Prüfungslinie für Migrationsrecht; prüft Gehalt, Abschluss, Beruf, Arbeitgeber, Mobilität und Familiennachzug; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AsylG §§ 13-19, 24-26a, 27-30, 71-74, 77; AufenthG §§ 4, 5, 7-9, 16a-d, 18a-c, 19-21, 28-36, 53-55, 60, 81, 95; AufenthG, AsylG, FreizügG/EU, StAG; AufenthG § 18b Abs. 2, § 18g, EU-Richtlinie 2021/1883; Dublin-III-VO (EU) 604/2013 Art. 3, 7-15, 17, 21-23, 29; StAG §§ 8, 9, 10, 11, 12a, 13, 16, 17, 25, 30; AufenthG §§ 18, 18a, 18b, 18c, 18d, 18g, 19c, FachkräfteEG 2023; AufenthG §§ 27-36; EU-Asylpaket (GEAS-Reform 2024): Asylverfahrens-VO, Asylkrisen-VO, Eurodac, AMMR; Genfer Flüchtlingskonvention Art. 1A, 31, 33; StAG §§ 4, 5, 8-17, 25, 27, 30; AufenthG, AsylG, StAG, FreizügG/EU, AsylbLG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-aufenthaltstitel-router`

**Fokus:** Aufenthaltstitel-Router: Prüfungslinie für Migrationsrecht; wählt Visum, Aufenthaltserlaubnis, Blaue Karte, ICT, Chancenkarte, NE, Daueraufenthalt; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Aufenthaltstitel-Router

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: wählt Visum, Aufenthaltserlaubnis, Blaue Karte, ICT, Chancenkarte, NE, Daueraufenthalt.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `workflow-ausweisung-start`

**Fokus:** Ausweisung Start: Prüfungslinie für Migrationsrecht; prüft Ausweisungsinteresse, Bleibeinteresse, Verhältnismäßigkeit und EMRK; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Ausweisung Start

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: prüft Ausweisungsinteresse, Bleibeinteresse, Verhältnismäßigkeit und EMRK.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 3. `workflow-behoerdenkommunikation`

**Fokus:** Behördenkommunikation: Prüfungslinie für Migrationsrecht; formuliert knappe Schreiben an ABH, BAMF, Botschaft oder Gericht; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Behördenkommunikation

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: formuliert knappe Schreiben an ABH, BAMF, Botschaft oder Gericht.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 4. `workflow-bescheid-verstehen`

**Fokus:** Bescheid verstehen: Prüfungslinie für Migrationsrecht; erkennt aus Bescheid, Rechtsbehelfsbelehrung und Zustellung die nächsten Schritte; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Bescheid verstehen

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: erkennt aus Bescheid, Rechtsbehelfsbelehrung und Zustellung die nächsten Schritte.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Bescheid-Anatomie Migrationsrecht

- **Bezeichnung:** BAMF-Bescheid (Asyl), Ausländerbehörde (Aufenthalt), Botschaft (Visum), Bundesverwaltungsamt (Einbürgerung).
- **Tenor:** Ablehnung gesondert prüfen — als offensichtlich unbegründet (§ 30 AsylG) löst Wochen-Frist aus (§ 36 AsylG); als einfach unbegründet 2-Wochen-Frist (§ 74 AsylG).
- **Rechtsbehelfsbelehrung:** Fehler oder fehlende RBB → 1-Jahres-Frist (§ 58 Abs. 2 VwGO); ABER Asyl-Sondervorschriften haben oft kürzere Fristen unabhängig (§ 74 AsylG, § 36 AsylG).
- **Zustellung:** Datum maßgeblich nicht Bescheiddatum; Postzustellungsurkunde bzw. Zustellung an Bevollmächtigten (Vollmacht!) prüfen — § 41 VwVfG/§ 31 AsylG, § 7 VwZG.
- **Abschiebungsandrohung:** Im Asylbescheid regelmäßig mit Ausreisefrist (i. d. R. 30 Tage, bei offensichtlich unbegründet 1 Woche, § 36 AsylG).
- **Sofortvollzug § 80 Abs. 2 VwGO:** Bei Asyl-Bescheiden kraft Gesetzes; Eilantrag § 80 Abs. 5 VwGO i. V. m. § 36 Abs. 3 AsylG bzw. § 34a Abs. 2 AsylG.
- **Einreise- und Aufenthaltsverbot § 11 AufenthG:** Befristung beachten — Antrag auf Verkürzung möglich.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 5. `workflow-blaue-karte-start`

**Fokus:** Blaue Karte EU Start: Prüfungslinie für Migrationsrecht; prüft Gehalt, Abschluss, Beruf, Arbeitgeber, Mobilität und Familiennachzug; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Blaue Karte EU Start

## Aufgabe
Prüfungslinie im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: prüft Gehalt, Abschluss, Beruf, Arbeitgeber, Mobilität und Familiennachzug.

## Einstieg
Wenn Unterlagen vorhanden sind, zuerst auswerten. Frage nur, was die nächste Weiche verändert:
1. Rolle, Ziel und gewünschte Sprache der Erklärung.
2. Staatsangehörigkeit, Herkunfts-/Transitstaaten, aktueller Aufenthaltsort und Status.
3. Frist, Zustellung, Termin, Ablaufdatum oder Abschiebungsrisiko.
4. Vorhandene Dokumente und fehlende Nachweise.
5. Gewünschter Output: einfache Erklärung, spanische Zusammenfassung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgebermemo oder Dokumentenliste.

## Arbeitsworkflow
1. **Statusmatrix:** Person, Staat/Gebiet, Dokumente, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist sichern:** Klage/Eilantrag, Dublin/GEAS, Fiktionswirkung, Visumtermin, Ausreisefrist, Abschiebung.
3. **Rechtsgrundlage:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, GFK/EMRK und Verwaltungspraxis live prüfen.
4. **Staatenbezug:** Bei Herkunfts-, Transit- oder Zielstaat passenden `staat-...-migrationscheck` ergänzen.
5. **Belege:** Dokumente, Urkunden, Übersetzungen, Atteste, Arbeitsvertrag, Abschluss, Behördenpost in eine Lückenliste bringen.
6. **Output:** Risikoampel, nächste Schritte, Entwurf und Anschluss-Skills.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
