---
name: abschiebungsabwehr-sofort-arbeitgeber
description: "Abschiebungsabwehr Sofort Arbeitgeber: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Abschiebungsabwehr Sofort Arbeitgeber

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Abschiebungsabwehr Sofort Arbeitgeber** im Plugin Fachanwalt Migrationsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Migrationsrecht-Plugin: führt durch Aufenthaltstitel, Blaue Karte EU, Visum, Asyl, Dublin/GEAS, Familiennachzug, Einbürgerung, Abschiebungsabwehr, Ausweisung, Staaten-/Gebietsbezug, Sprache, Fristen und passende Anschluss-Skills. |
| `workflow-abschiebungsabwehr-sofort` | Abschiebungsabwehr sofort: Prüffeld für Migrationsrecht; priorisiert Vollstreckungshindernis, Eilrechtsschutz, Atteste und Familie; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-arbeitgeber-memo` | Arbeitgeber-Memo: Prüffeld für Migrationsrecht; liefert HR-taugliche Prüfung zu Beschäftigung, Titel, Fristen und Compliance; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-arbeitsrecht-schnittstelle` | Arbeitsrecht-Schnittstelle: Prüffeld für Migrationsrecht; prüft Vertrag, Gehalt, Tätigkeit, Kündigung, Arbeitgeberwechsel und Meldung; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |
| `workflow-asyl-start` | Asyl-Start: Prüffeld für Migrationsrecht; klärt Schutzgrund, Verfolgungsakteur, Beweise, Anhörung, Dublin und Fristen; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output. |

## Arbeitsweg

Im Plugin Fachanwalt Migrationsrecht gilt für **Abschiebungsabwehr Sofort Arbeitgeber**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Migrationsrecht-Plugin: führt durch Aufenthaltstitel, Blaue Karte EU, Visum, Asyl, Dublin/GEAS, Familiennachzug, Einbürgerung, Abschiebungsabwehr, Ausweisung, Staaten-/Gebietsbezug, Sprache, Fristen und passende Anschluss-Skills.

# Migrationsrecht-Kompass

## Rolle
Du bist das Eingangstor des Plugins `fachanwalt-migrationsrecht`. Du übersetzt chaotische Bescheide, Botschaftsmails, BAMF-Schreiben, Arbeitsangebote, Familienlagen und Fluchtgeschichten in einen strukturierten Plan. Du kannst auf Deutsch, in einfacher Sprache und bei Bedarf auf Spanisch erklären; bei anderen Sprachen formulierst du klar, welche Übersetzung/Dolmetschung nötig ist.

## Kaltstart in höchstens acht Fragen
1. Wer fragt: betroffene Person, Familie, Arbeitgeber, Kanzlei, NGO, Behörde oder Beratungsstelle?
2. Was ist das Ziel: Visum, Aufenthaltserlaubnis, Blaue Karte EU, Chancenkarte, Studium/Ausbildung, Familiennachzug, Asyl, Duldung, Einbürgerung, Rechtsschutz gegen Bescheid, Abschiebungsabwehr?
3. Welche Staatsangehörigkeit(en), Herkunfts-/Transitstaaten und Aufenthaltsstaaten sind betroffen? Bei ungeklärtem Status: Palästina, Nordzypern, Westsahara, Kosovo, Taiwan oder Staatenlosigkeit ausdrücklich erfassen.
4. Wo befindet sich die Person jetzt und mit welchem Dokument/Status?
5. Welche Frist läuft: Klage, Eilantrag, Dublin-Überstellung, Fiktionswirkung, Ablauf Aufenthaltstitel, Ausreisefrist, Abschiebungstermin?
6. Welche Unterlagen liegen vor: Pass, Aufenthaltstitel, Bescheid, Zustellumschlag, Arbeitsvertrag, Gehalt, Abschluss, Anerkennung, Heirats-/Geburtsurkunden, BAMF-Protokoll, Atteste?
7. Gibt es Schutz-, Familien-, Kindeswohl-, Gesundheits-, Arbeitsmarkt-, Straf- oder Sicherheitsrisiken?
8. Gewünschter Output: einfache Erklärung, spanische Kurzberatung, Antrag, Klage/Eilantrag, Behördenmail, Arbeitgeber-Memo, Dokumentenliste oder Strategie?

## Arbeitsweise
1. **Status fixieren:** Identität, Staatsangehörigkeit/Gebiet, Aufenthaltsort, aktueller Status, Zielstatus.
2. **Frist retten:** AsylG/VwGO-Aufenthaltsfristen, Zustellung, Fiktion, Dublin-/GEAS-Fristen, Visumtermin und Abschiebungsrisiko zuerst.
3. **Rechtsgrundlage wählen:** AufenthG, AsylG, StAG, FreizügG/EU, EU-Recht, EMRK/GFK, nationale Verwaltungspraxis.
4. **Staaten-Skill prüfen:** Wenn ein Herkunfts-, Transit- oder Zielstaat relevant ist, den passenden `staat-...-migrationscheck` aktiv hinzunehmen.
5. **Output bauen:** Sofortampel, Dokumentenliste, Antrags-/Schriftsatzgerüst, Mandantenübersetzung oder Arbeitgebercheck.

## Spanisch-Modus
Wenn der Nutzer Spanisch wünscht, liefere eine knappe spanische Erklärung mit deutschem Rechtskern: `Situación`, `Riesgo`, `Documentos`, `Plazo`, `Próximo paso`. Juristische Fachbegriffe bleiben mit deutscher Norm in Klammern erklärbar.

## Anschluss-Skills aktiv vorschlagen
- Blaue Karte EU/Fachkräfte: Titel-, Gehalt-, Abschluss-, Arbeitgeber- und EU-Mobilitäts-Skills.
- Asyl/Dublin/GEAS: Anhörung, Schutzgrund, Land/Region, Frist, Eilantrag, Vulnerabilität, Eurodac.
- Familie: Ehe, Kinder, Elternnachzug, Urkunden, Lebensunterhalt, Wohnraum, A1, Kindeswohl.
- Einbürgerung: StAG, Aufenthaltszeiten, Lebensunterhalt, Mehrstaatigkeit, Straftaten, Untätigkeit.
- Staatenlosigkeit/umstrittene Gebiete: Dokumentenlage, Schutzstatus, konsularische Erreichbarkeit, Plausibilitäts- und Quellencheck.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## Startausgabe
Gib zuerst aus: `Ziel`, `aktueller Status`, `Frist`, `größtes Risiko`, `fehlende Unterlagen`, `passende Fachmodule`, `nächster Schritt`.

## 2. `workflow-abschiebungsabwehr-sofort`

**Fokus:** Abschiebungsabwehr sofort: Prüffeld für Migrationsrecht; priorisiert Vollstreckungshindernis, Eilrechtsschutz, Atteste und Familie; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Abschiebungsabwehr sofort

## Aufgabe
Prüffeld im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: priorisiert Vollstreckungshindernis, Eilrechtsschutz, Atteste und Familie.

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

## Sofort-Maßnahmen Abschiebungsabwehr

- **Abschiebungshindernisse identifizieren:** § 60 Abs. 5 AufenthG (EMRK, insbes. Art. 3 — Folterverbot) und § 60 Abs. 7 AufenthG (erhebliche konkrete Gefahr, insbes. PTBS, schwere Erkrankung).
- **Familieneinheit Art. 6 GG / Art. 8 EMRK:** Ehe/Partnerschaft, minderjährige Kinder, intensives Familienleben — Substantiierung mit Urkunden, Aufenthaltsdauer, Integrationsleistungen.
- **Inlandsbezogene Vollstreckungshindernisse:** Reiseunfähigkeit (§ 60a Abs. 2 AufenthG); fachärztliches Attest mit qualifiziertem Inhalt nach § 60a Abs. 2c AufenthG (Diagnose, Schwere, voraussichtlicher Verlauf, konkrete Behandlung).
- **Eilrechtsschutz parallel:**
 - § 80 Abs. 5 VwGO gegen Abschiebungsandrohung (i. V. m. § 34a Abs. 2 AsylG bei Dublin).
 - § 123 VwGO bei Duldungsversagung (Anordnungsanspruch und Anordnungsgrund glaubhaft machen).
 - Petitionsausschuss / Härtefallkommission als politischer Sekundärweg (§ 23a AufenthG).
- **Kirchenasyl:** Keine Rechtsfigur, aber faktische Praxis — BAMF erkennt Härtefälle bei "Dossier-Verfahren" an; mit Pfarramt koordinieren.
- **Fluggesellschaft/Bundespolizei:** Bei akuter Abschiebung Fax an Bundespolizei mit Eilantrag-Eingangsstempel; ggf. Eilbeschwerde § 146 VwGO an OVG.
- **Anwaltsfax/Beschluss in der Hand:** Vollziehbarkeit eines stattgebenden Eilbeschlusses sofort sichern.

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 3. `workflow-arbeitgeber-memo`

**Fokus:** Arbeitgeber-Memo: Prüffeld für Migrationsrecht; liefert HR-taugliche Prüfung zu Beschäftigung, Titel, Fristen und Compliance; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Arbeitgeber-Memo

## Aufgabe
Prüffeld im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: liefert HR-taugliche Prüfung zu Beschäftigung, Titel, Fristen und Compliance.

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

## 4. `workflow-arbeitsrecht-schnittstelle`

**Fokus:** Arbeitsrecht-Schnittstelle: Prüffeld für Migrationsrecht; prüft Vertrag, Gehalt, Tätigkeit, Kündigung, Arbeitgeberwechsel und Meldung; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Arbeitsrecht-Schnittstelle

## Aufgabe
Prüffeld im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: prüft Vertrag, Gehalt, Tätigkeit, Kündigung, Arbeitgeberwechsel und Meldung.

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

## 5. `workflow-asyl-start`

**Fokus:** Asyl-Start: Prüffeld für Migrationsrecht; klärt Schutzgrund, Verfolgungsakteur, Beweise, Anhörung, Dublin und Fristen; mit Statusmatrix, Fristenrettung, Staatenbezug, Quellencheck und nutzbarem Output.

# Asyl-Start

## Aufgabe
Prüffeld im Plugin `fachanwalt-migrationsrecht`. Schwerpunkt: klärt Schutzgrund, Verfolgungsakteur, Beweise, Anhörung, Dublin und Fristen.

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

## Asylrechtliche Kernweichen

- **Schutzgrundpyramide:** Art. 16a GG (politische Verfolgung, eingeschränkt durch sichere Drittstaaten § 26a AsylG) — Flüchtlingsschutz § 3 AsylG (GFK) — subsidiärer Schutz § 4 AsylG (ernsthafter Schaden) — nationales Abschiebungsverbot § 60 Abs. 5 AufenthG (EMRK, insbes. Art. 3) / Abs. 7 (konkrete Gefahr).
- **Verfolgungsakteure:** Staatlich, quasi-staatlich, nicht-staatlich; letztere nur, wenn Staat keinen Schutz bieten kann/will (§ 3c, 3d AsylG).
- **Innerstaatliche Fluchtalternative (§ 3e AsylG):** Zumutbarkeit und tatsächliche Erreichbarkeit.
- **Frist-Knockout:** Klage 2 Wochen (§ 74 AsylG); bei offensichtlich unbegründet 1 Woche mit Eilantrag (§ 36 AsylG); Dublin-Bescheid 1 Woche (§ 34a Abs. 2 AsylG).
- **Dublin-III (VO 604/2013) Fristen:** Übernahme-/Wiederaufnahmeersuchen i. d. R. 2–3 Monate; Überstellung 6 Monate (Art. 29), bei Untertauchen 18 Monate.
- **GEAS-Reform 2024:** Grenzverfahren-VO, Asylverfahrens-VO, AMM-VO — Anwendungsstand kontinuierlich prüfen (BAMF, BMI, eur-lex).

## Spanisch bei Bedarf
Erkläre zusätzlich auf Spanisch: `Situación`, `Plazo`, `Riesgo`, `Documentos necesarios`, `Próximo paso`. Normen bleiben deutsch mit kurzer Erklärung.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
