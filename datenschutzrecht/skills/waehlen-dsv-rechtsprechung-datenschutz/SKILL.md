---
name: waehlen-dsv-rechtsprechung-datenschutz
description: "Wählen DSV Rechtsprechung Datenschutz im Datenschutzrecht: prüft konkret Output wählen im Plugin datenschutzrecht, Red-Team Qualitygate im Plugin datenschutzrecht, Analysiert die deutsche Rechtsprechung zum immateriellen, Bußgeldverteidigung nach Art. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Wählen DSV Rechtsprechung Datenschutz

## Arbeitsbereich

**Wählen DSV Rechtsprechung Datenschutz** ordnet den Fall über die tragenden Prüfungslinien: Output wählen im Plugin datenschutzrecht, Red-Team Qualitygate im Plugin datenschutzrecht, Analysiert die deutsche Rechtsprechung zum immateriellen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-output-waehlen` | Output wählen im Plugin datenschutzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin datenschutzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `dsv-rechtsprechung-immaterieller-schaden-bgh-olg` | Analysiert die deutsche Rechtsprechung zum immateriellen Schadensersatz nach Art. 82 DSGVO im Lichte der EuGH-Vorgaben. Behandelt: BGH-Entscheidungen zur Substantiierung; OLG-Linien zur Bagatellschwelle; OLG-Entscheidungen zur Beweislast bei Kontrollverlust; LG-Streuung bei Datenleck-Massenklagen; Schmerzensgeldgrößen; Kausalitäts-anforderungen. Output: Rechtsprechungs-Übersicht mit Begründungslinien. Abgrenzung: keine konkrete Verteidigung. |
| `datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung` | Bußgeldverteidigung nach Art. 83 DSGVO bis 4 Prozent Jahresumsatz oder 20 Mio. EUR. EDSA-Leitlinien 04/2022 zur Bemessung. Sieben-Fragen-Diagnose: Anhörung oder Bußgeldbescheid, Aufsichtsbehörde, Norm DSGVO/BDSG, Bezugsumsatz, Vorwurf, Verschulden, Maßnahmenlage. Schritt-für-Schritt: Akteneinsicht, keine vorschnelle Stellungnahme, dynamische Geldbemessung, EDSA-Methodik, § 41 BDSG, OWiG/StPO-Verfahrensgarantien. Einspruch nach § 67 OWiG binnen zwei Wochen. EuGH C-807/21 Deutsche Wohnen und C-683/21: Unternehmensgeldbuße ohne Identifizierung einer natürlichen Person, aber nicht ohne Vorsatz oder Fahrlässigkeit. Mustertexte Einspruch, Stellungnahme, Erledigungsvorschlag. Abgrenzung: keine zivilrechtliche Schadensersatzabwehr. |
| `dsv-sanktion-beschlussverfahren-72-owig` | Datenschutzrecht-Brückenskill: Beschlussverfahren § 72 OWiG: Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-output-waehlen`

**Fokus:** Output wählen im Plugin datenschutzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung.

# Output wählen

## Aufgabe
Dieses Modul bearbeitet: Output wählen im Plugin datenschutzrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung..

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

## Outputformen Datenschutz
- **Auskunftsentwurf nach Art. 15 DSGVO** mit Datenkopie, Empfängerliste, Speicherdauer, Widerspruchsrechten.
- **DSFA-Bericht** nach Art. 35 DSGVO mit Bewertungsmethodik, Risiken, Schutzmaßnahmen, Restrisikobewertung.
- **AVV-Redline** nach Art. 28 Abs. 3 DSGVO mit Markierungen für TOM-Anlage, Subunternehmer, Audit-Rechte.
- **Meldung nach Art. 33 DSGVO** (Datenpanne) — Standardformular der zuständigen Aufsichtsbehörde verwenden (BfDI / LfD-Portal).
- **Benachrichtigung der Betroffenen** nach Art. 34 DSGVO mit klarer Sprache, Beschreibung, Kontakt DSB.
- **Datenschutzhinweise** nach Art. 13/14 DSGVO mit allen Pflichtangaben.
- **Drittlandstransfer-Doku**: SCC-Modul-Auswahl + TIA + ggf. supplementary measures.

## Praxis-Tipp
Bei einer Datenpannenmeldung nach Art. 33 stets das Online-Meldeformular der zuständigen Behörde (z. B. BfDI-Meldeportal, LDI NRW-Formular) verwenden und parallel intern eine Aktennotiz mit Zeitlinie führen — die 72-Stunden-Frist verläuft schnell, eine spätere Rekonstruktion ist mühsam.

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

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin datenschutzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin datenschutzrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Red-Team-Prüfpunkte Datenschutz
1. **Rollenklarheit:** Verantwortlicher (Art. 4 Nr. 7) vs. Auftragsverarbeiter (Art. 4 Nr. 8) vs. gemeinsame Verantwortlichkeit (Art. 26) klar?
2. **Rechtsgrundlage:** Art. 6 DSGVO einzeln benannt (Buchstaben a-f), nicht pauschal? Bei besonderen Datenkategorien Art. 9 zusätzlich?
3. **Drittlandstransfer:** DPF-Status zum Zeitpunkt der Prüfung gecheckt, SCC-Modul richtig, TIA dokumentiert?
4. **Fristen:** Art. 33 (72h), Art. 12 Abs. 3 (1 Monat), Art. 17 (Vergessen unverzüglich) richtig benannt?
5. **Beschäftigtendaten:** § 26 BDSG vs. Art. 88 DSGVO i.V.m. Tarifvertrag oder Betriebsvereinbarung?
6. **Verzeichnis Art. 30:** vollständig (Verantwortlicher + Auftragsverarbeiter)?
7. **Cookies/Tracking:** § 25 TDDDG (Einwilligung) vs. Art. 6 DSGVO (Verarbeitung) klar getrennt?
8. **Halluzinations-Check:** Keine erfundenen Aufsichtsbehörden-Stellungnahmen, keine BeckRS-Az. ohne Live-Quelle.

## Praxis-Tipp
Häufiger Fehler in der DSGVO-Beratung: Vermischung von TDDDG-Einwilligung (Endgerätezugriff, § 25 TDDDG) und DSGVO-Rechtsgrundlage (Verarbeitung pbD nach Art. 6). Beide sind kumulativ erforderlich für werbliche Cookies — Einwilligung nach TDDDG ersetzt nicht die Rechtsgrundlage nach DSGVO.

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

## 3. `dsv-rechtsprechung-immaterieller-schaden-bgh-olg`

**Fokus:** Analysiert die deutsche Rechtsprechung zum immateriellen Schadensersatz nach Art. 82 DSGVO im Lichte der EuGH-Vorgaben. Behandelt: BGH-Entscheidungen zur Substantiierung; OLG-Linien zur Bagatellschwelle; OLG-Entscheidungen zur Beweislast bei Kontrollverlust; LG-Streuung bei Datenleck-Massenklagen; Schmerzensgeldgrößen; Kausalitäts-anforderungen. Output: Rechtsprechungs-Übersicht mit Begründungslinien. Abgrenzung: keine konkrete Verteidigung.

# Rechtsprechung BGH und OLG zum immateriellen Schaden Art. 82 DSGVO

## Triage — kläre vor der Bearbeitung

1. Welche Sachverhaltskonstellation liegt vor (Kontrollverlust; Phishing-Folge; Identitätsdiebstahl)?
2. Welche OLG-Region ist relevant?
3. Welche EuGH-Entscheidungen sind seit C-300/21 ergangen?
4. Welche Schmerzensgeldgrößen werden zugesprochen?
5. Welche Beweisanforderungen stellt das Gericht?
- Was will der Mandant wirklich erreichen? (rechtssichere Argumentation; passende Präzedenzen)

## Rechtsgrundlagen

- **Art. 82 DSGVO** Schadensersatz.
- **EuGH C-300/21 Österreichische Post** Auslegung Schadensbegriff.
- **EuGH C-687/21 Saturn** geringe Schwelle für Schadenseintritt.
- **EuGH C-456/22 Gemeinde Ummendorf** keine Bagatellgrenze für Schaden, aber Substantiierung erforderlich.
- **BGH VI ZR-Rechtsprechung** zur immateriellen Schadenshöhe.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; jede zitierte Entscheidung vor Ausgabe über bundesgerichtshof.de; openjur.de; eur-lex.europa.eu verifizieren mit Aktenzeichen Datum und Tenor.

## Zentrale Normen

Art. 82 DSGVO; § 253 Abs. 2 BGB; EuGH C-300/21; C-687/21; C-456/22.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Übersichtsraster

Spalte 1: Aktenzeichen und Gericht; Spalte 2: Datum; Spalte 3: Sachverhaltstyp; Spalte 4: Schadenshöhe zugesprochen; Spalte 5: tragende Argumente; Spalte 6: Quelle.

Verifikationsschritt: vor jeder Zitation prüfen — wegen Quellenregel keine Zitate aus Modellwissen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-schadensersatz-art-82` deckt die konkrete Verteidigung ab.

## 4. `datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung`

**Fokus:** Bußgeldverteidigung nach Art. 83 DSGVO bis 4 Prozent Jahresumsatz oder 20 Mio. EUR. EDSA-Leitlinien 04/2022 zur Bemessung. Sieben-Fragen-Diagnose: Anhörung oder Bußgeldbescheid, Aufsichtsbehörde, Norm DSGVO/BDSG, Bezugsumsatz, Vorwurf, Verschulden, Maßnahmenlage. Schritt-für-Schritt: Akteneinsicht, keine vorschnelle Stellungnahme, dynamische Geldbemessung, EDSA-Methodik, § 41 BDSG, OWiG/StPO-Verfahrensgarantien. Einspruch nach § 67 OWiG binnen zwei Wochen. EuGH C-807/21 Deutsche Wohnen und C-683/21: Unternehmensgeldbuße ohne Identifizierung einer natürlichen Person, aber nicht ohne Vorsatz oder Fahrlässigkeit. Mustertexte Einspruch, Stellungnahme, Erledigungsvorschlag. Abgrenzung: keine zivilrechtliche Schadensersatzabwehr.

# Datenschutz-Bußgeldverfahren — Verteidigung nach Art. 83 DSGVO

## Zweck

Dieser Skill verteidigt den Mandanten im Bußgeldverfahren wegen DSGVO-Verstoß — von der Anhörung bis zum Einspruch nach § 67 OWiG und zum gerichtlichen Verfahren. Ziel ist die Vermeidung des Bußgeldbescheids, hilfsweise die Reduzierung der Geldbuße nach Art. 83 Abs. 2 DSGVO und den EDSA-Leitlinien 04/2022.

Terminologie sauber halten: Das ist kein Zivilprozess und keine Anklage im engeren strafprozessualen Sinn. Die Stationen heißen regelmäßig Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Abgabe über die Staatsanwaltschaft an das zuständige Gericht, Hauptverhandlung oder Beschlussverfahren, Rechtsbeschwerde. Parallel können aufsichtsbehördliche Anordnungen nach Art. 58 Abs. 2 DSGVO verwaltungsgerichtlich anzugreifen sein.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen den Skill, sobald die Aufsichtsbehörde förmlich ein Bußgeldverfahren eingeleitet hat: Anhörung nach § 55 OWiG, Bußgeldbescheid nach § 65 OWiG oder laufende Einspruchsfrist nach § 67 OWiG.

Sieben-Fragen-Diagnose:

1. **Anhörung oder Bußgeldbescheid?** Andere Strategie pro Stand: Vor Bescheid Argumentationsspielraum, nach Bescheid Einspruchsfrist zwei Wochen ab Zustellung.
2. **Welche Aufsichtsbehörde?** Landesaufsicht oder BfDI? Federführend nach Art. 56 DSGVO (One-Stop-Shop)?
3. **Welche Norm wird verletzt?** Art. 5, 6, 9, 13, 14, 15, 17, 25, 28, 30, 32, 33, 34, 35, 37 DSGVO — und welche Sanktionsstufe Art. 83 Abs. 4 (10 Mio./2 Prozent) oder Art. 83 Abs. 5/6 (20 Mio./4 Prozent)?
4. **Bezugsumsatz:** Welcher Konzernumsatz wird zugrundegelegt — Mandantengesellschaft oder Mutter? EuGH C-807/21 Deutsche Wohnen relevant.
5. **Welche Vorwerfung?** Konkrete Handlung oder Unterlassen? Welcher Zeitraum?
6. **Verschulden:** Vorsatz, Fahrlässigkeit? Welche Organisation, welcher DSB, welche TOM?
7. **Maßnahmenlage:** Welche TOM Art. 32, welche DSFA Art. 35, welcher AVV Art. 28 lagen vor und sind dokumentiert?
8. **Parallelspur Art. 58 DSGVO?** Geht es nur um Geldbuße oder auch um Untersagung, Löschungsanordnung, Auskunftsauflage, Datenübermittlungsstopp oder sonstige aufsichtsbehördliche Maßnahme?

## Rechtlicher Rahmen

- **Art. 83 DSGVO** Bußgeldrahmen. Abs. 4 bis 10 Mio. EUR oder 2 Prozent. Abs. 5/6 bis 20 Mio. EUR oder 4 Prozent. Der jeweils höhere Wert gilt.
- **Art. 83 Abs. 2 DSGVO** Kriterien: Art, Schwere, Dauer, Vorsatz/Fahrlässigkeit, Schadensminderung, Verantwortlichkeit, Vorbelastung, Zusammenarbeit, Datenkategorien, Bekanntwerden, frühere Anordnungen, Zertifizierungen, finanzielle Vorteile.
- **EuGH C-807/21 Deutsche Wohnen** (Urteil 05.12.2023): Geldbuße gegen juristische Personen unmittelbar möglich, ohne dass eine natürliche Person identifiziert werden muss; erforderlich bleibt ein vorsätzlicher oder fahrlässiger Verstoß.
- **EuGH C-683/21 Nacionalinis visuomenės sveikatos centras** (Urteil 05.12.2023): Verantwortlichen-/Auftragsverarbeiterrollen, gemeinsame Verantwortlichkeit und Sanktionierbarkeit müssen unionsrechtlich sauber bestimmt werden; auch hier keine verschuldensunabhängige Geldbuße.
- **EDSA, Leitlinien 04/2022** zur Berechnung von Geldbußen (Final version 24.05.2023): harmonisierte Bemessungsmethodik, Startbetrag, Schweregrad, Umsatz-/Unternehmensgröße, erschwerende und mildernde Umstände, Höchstbetrag, Effektivität/Verhältnismäßigkeit/Abschreckung.
- **§ 41 BDSG** Anwendung OWiG.
- **§ 67 OWiG** Einspruch binnen zwei Wochen ab Zustellung.
- **§ 68 OWiG i.V.m. § 41 Abs. 1 BDSG** Gerichtliche Zuständigkeit: grundsätzlich Amtsgericht; bei festgesetzter DSGVO-Geldbuße über 100.000 EUR entscheidet nach § 41 BDSG das Landgericht.
- **§ 69 OWiG** Zwischenverfahren: Behörde prüft Rücknahme/Aufrechterhaltung; bei Aufrechterhaltung Übersendung über die Staatsanwaltschaft an das Gericht. Nach § 41 Abs. 2 BDSG kann die Staatsanwaltschaft nur mit Zustimmung der Aufsichtsbehörde einstellen.
- **§ 71 OWiG** Hauptverhandlung nach zulässigem Einspruch, sinngemäße Anwendung strafprozessualer Regeln.
- **§ 72 OWiG** Beschlussverfahren, wenn dafür die gesetzlichen Voraussetzungen vorliegen.
- **§ 73 OWiG** Anwesenheit/Entbindung des Betroffenen in der Hauptverhandlung, nicht der Name der Verhandlung selbst.
- **§ 79 OWiG** Rechtsbeschwerde.
- **§ 20 BDSG** Verwaltungsrechtsweg für Art.-78-Streitigkeiten gegen Aufsichtsbehörden; ausdrücklich nicht für Bußgeldverfahren. Relevant für Art.-58-Anordnungen, nicht für die Geldbuße selbst.

## Mandantenfuehrung Schritt-für-Schritt

1. **Zuerst: Frist sichern.** Einspruchsfrist nach § 67 I OWiG zwei Wochen ab Zustellung — sofort im Fristenkalender, Wiedereinsetzungspruefung bei Saeumnis.
2. **Akteneinsicht beantragen.** § 49 OWiG i.V.m. § 147 StPO. Erst danach Strategie.
3. **NICHT vorschnell Stellungnahme.** Auch nicht "kooperativ" Daten nachschieben — kann den Vorwurf verschaerfen.
4. **Prüfen: Zuständigkeit und Verfahrensweg.** § 41 BDSG-Sonderzuständigkeit bei Geldbußen über 100.000 EUR beachten; Bußgeldspur nicht mit verwaltungsgerichtlicher Art.-58-Spur vermischen.
5. **Prüfen: Bemessung nach EDSA 04/2022.** Prüfen, ob die Aufsicht die Methodik sauber angewendet hat. Bezugsumsatz richtig? Schweregrad richtig? Mildernde Umstände berücksichtigt?
6. **Verschuldensfrage:** Hat die Aufsicht Vorsatz oder Fahrlässigkeit konkret begründet? Nach EuGH C-807/21 muss kein Organ oder Beschäftigter namentlich identifiziert werden, aber ein schuldhafter Unternehmensverstoß muss tragfähig dargelegt sein.
7. **Einspruch einlegen.** Auch nur fristwahrend, Begründung nach Akteneinsicht.
8. **Erledigungsgespräch erwägen.** Insbesondere bei Erstverstoß, dokumentierter Selbstmeldung Art. 33, nachweislichem Maßnahmenplan und vertretbarer Bemessungskorrektur.

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Voller Einspruch + gerichtliches Verfahren | Sachprüfung, keine Bindung an Behördenbewertung | Hauptverhandlung/Öffentlichkeit, Kosten- und Reputationsrisiko |
| Beschlussverfahren § 72 OWiG anstreben | Schnelle, schriftliche Erledigung möglich | Nur bei passendem Verfahrensstand und Einverständnis-/Widerspruchslage sinnvoll |
| Einspruchsrücknahme nach Akteneinsicht/Termin | Begrenzung weiterer Risiken | Bestandskraft, kein Einfluss mehr |
| Selbstmeldung + Kooperation vor Bescheid | Bußgeldmilderung Art. 83 Abs. 2 lit. c/f/h DSGVO möglich | Selbstbelastungs- und Scope-Erweiterungsrisiko |
| Verschuldens-Bestreitung EuGH C-807/21/C-683/21 | Kernargument gegen schematische Unternehmenshaftung | Nur stark, wenn Compliance-Organisation, TOMs und Eskalationslogik belegbar sind |
| Verwaltungsgerichtliche Abwehr Art. 58 DSGVO | Stoppt/prüft Auflagen, Untersagungen, Löschungs- oder Transferanordnungen | Andere Fristen, anderer Rechtsweg, keine automatische Lösung des Bußgeldverfahrens |

## Mustertexte

### Einspruch (fristwahrend)

> An die [Aufsichtsbehörde]
> Aktenzeichen: [Az]
>
> Gegen den Bußgeldbescheid vom [Datum], zugestellt am [Datum], wird in vollem Umfang Einspruch eingelegt.
>
> Die Begruendung erfolgt nach Akteneinsicht.
>
> Wir beantragen Akteneinsicht in den vollstaendigen Vorgang nach § 49 OWiG in Verbindung mit § 147 StPO.

### Stellungnahme Anhörung — Strukturvorschlag

> 1. Verfahrensrechtliche Rügen (Zuständigkeit, Anhörung, Akteneinsicht).
> 2. Tatbestand (DSGVO-Norm konkret, Subsumtion mit Belegen).
> 3. Verschulden (EuGH C-807/21 — konkrete Pflichtverletzung des Unternehmens? Welche Organisation, welche Maßnahmen lagen vor?).
> 4. Bemessung nach EDSA 04/2022 (Bezugsumsatz, Schritte 1-5).
> 5. Mildernde Umstände Art. 83 Abs. 2 DSGVO (Maßnahmen, Kooperation, kein Vorteil, keine Vorbelastung).
> 6. Antrag: Einstellung; hilfsweise Verwarnung nach Art. 58 II b DSGVO; hilfsweise Reduzierung auf [Betrag].

### Erledigungsvorschlag (Anhörung)

> Sehr geehrte Damen und Herren,
>
> ohne Anerkennung einer Rechtspflicht und unter Beibehaltung sämtlicher Verteidigungsrechte schlägt unsere Mandantin folgende einvernehmliche Erledigung vor:
>
> 1. Umsetzung eines Maßnahmenplans bis [Datum] (Anlage).
> 2. Geldbuße [Betrag] in [Raten].
> 3. Verzicht auf Veröffentlichung der Entscheidung mit Namensnennung.
>
> Mit freundlichen Gruessen

## Typische Fehler

- Einspruchsfrist § 67 OWiG verpasst, weil Bescheid an alte Anschrift zugestellt.
- Verschuldensfrage nicht konkret gepruefte EuGH C-807/21 — Unternehmen muss vorsaetzlich oder fahrlaessig gehandelt haben, nicht eine namentlich benannte natuerliche Person.
- EDSA-Schritte unkommentiert akzeptiert.
- Vergleich ohne Vorbehalt der Verteidigungsrechte.
- Konzernumsatz-Bezugsfrage nicht angegriffen (Mandantengesellschaft vs Mutter).

**Was triggert die Aufsichtsbehörde besonders zur Höchststrafe?** Wiederholungstäter, Verletzung Art.-9-Daten, fehlende DSB-Bestellung trotz § 38 BDSG, fehlender AVV Art. 28 DSGVO, fehlende DSFA Art. 35 DSGVO.

## Querverweise

- `datenschutz-mandantenkommunikation-aufsichtsbehoerde`
- `datenschutz-datenpanne-art-33-34-72h-incident-response`
- `datenschutz-schadensersatz-art-82-dsgvo-gerichtsstreit`
- `datenschutz-erstgespraech-mandantenmatrix-7-fragen`

## Quellen Stand 06/2026

- DSGVO Art. 5, 6, 25, 32, 33, 35, 37, 58, 83.
- BDSG § 38, § 41, § 43.
- OWiG § 46, § 49, § 55, § 65, § 67, § 69, § 73, § 79.
- StPO § 147.
- EuGH C-807/21 Deutsche Wohnen, Urteil 05.12.2023.
- EDSA, Leitlinien 04/2022 zur Berechnung der Geldbussen nach DSGVO, Version 1.0, angenommen 24.05.2023.
- Keine Aufsatzfundstellen aus Modellwissen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `dsv-sanktion-beschlussverfahren-72-owig`

**Fokus:** Datenschutzrecht-Brückenskill: Beschlussverfahren § 72 OWiG: Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen. Fachmodul für Datenschutz-Sanktionsverfahren, Bußgeldverteidigung, Aufsichtsbehördenkommunikation und gerichtlichen Rechtsschutz. Bei ernstem Behörden- oder Bußgelddruck Spezialplugin datenschutz-sanktionsverfahren-verteidigung laden.

# Beschlussverfahren § 72 OWiG

## Aufgabe

Schriftliche Erledigung per Beschluss prüfen, wenn Tatsachen und Verfahrenslage dafür taugen.

Dieser Skill arbeitet als Brücke im allgemeinen Plugin `datenschutzrecht`. Er darf nicht austauschbar antworten: immer zuerst Verfahrensstand, Behörde, Frist, Rechtsweg, Beweisstand und gewünschtes Arbeitsprodukt klären.

## Kaltstart-Fragen

1. Welches Schreiben oder welcher Verfahrensschritt liegt vor: informelle Anfrage, Art.-58-Auskunftsverlangen, Anhörung, Bußgeldbescheid, Einspruch, gerichtliches Bußgeldverfahren, Art.-58-Anordnung, Verwaltungsgericht oder Rechtsmittel?
2. Welche Behörde handelt: Landesdatenschutzaufsicht, BfDI, kirchliche Datenschutzaufsicht, federführende EU-Aufsicht oder andere Spezialaufsicht?
3. Wer ist Adressat und in welcher Rolle: Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche, Konzernmutter, Tochter, öffentliche Stelle oder natürliche Person?
4. Welche Frist läuft und wie wurde zugestellt oder bekanntgegeben?
5. Welche Tatsachen sind durch Akte, Logs, Verträge, DSFA, TOM, AVV, DSB-Vermerk oder Zeugen belegbar?
6. Soll die Ausgabe Akteneinsicht, Fristverlängerung, Stellungnahme, Einspruch, Klage, Eilantrag, Terminsmappe oder Management-Briefing sein?

## Rechtsanker

- Art. 83 DSGVO
- § 41 BDSG
- §§ 49, 55, 65, 67, 68, 69, 71, 72, 73, 79 OWiG
- § 147 StPO

## Arbeitsprogramm

1. **Spur trennen.** Bußgeld nach Art. 83 DSGVO/§ 41 BDSG/OWiG ist nicht dasselbe wie Verwaltungsrechtsschutz gegen Art.-58-Anordnungen nach § 20 BDSG. Parallelspuren getrennt führen.
2. **Frist sichern.** Einspruchs- und Rechtsbehelfsfristen sofort mit Zustellnachweis notieren; weiche Behördenfristen separat behandeln.
3. **Akteneinsicht und Beweisstand.** Keine endgültige Tatsachenstellungnahme ohne Akteneinsicht, wenn ein Bußgeldverfahren erkennbar ist. Technische Behauptungen anhand Logs, Systemarchitektur und Verantwortlichkeiten prüfen.
4. **Materiell prüfen.** DSGVO-Norm, Verantwortlichenrolle, Pflichtverletzung, Vorsatz/Fahrlässigkeit, Art.-83-Bemessung oder Art.-58-Ermessensausübung sauber subsumieren.
5. **Taktisch schreiben.** Kooperativ, aber geschützt: keine unnötigen Schuldeingeständnisse, keine nicht belegten Behauptungen, keine Vermischung von Datenschutzberatung und Verteidigung.
6. **Nächsten Schritt auswerfen.** Immer mit Risikoampel, konkreten Unterlagen, Freigabeentscheidung und empfohlenen Anschlussskills schließen.

## Typische Fehler, die der Skill vermeiden muss

- Bußgeldverfahren als normales Verwaltungsverfahren behandeln.
- Art.-58-Anordnung und Bußgeldbescheid in denselben Rechtsweg werfen.
- "Anklage" sagen, wo es im OWiG um Bußgeldbescheid, Einspruch, Zwischenverfahren und gerichtliche Hauptverhandlung geht.
- § 73 OWiG als Bezeichnung der mündlichen Verhandlung missverstehen; die Hauptverhandlung steht in § 71 OWiG.
- EuGH C-807/21 als verschuldenslose Unternehmenshaftung lesen. Das ist falsch: keine Identifizierung einer natürlichen Person nötig, aber Vorsatz oder Fahrlässigkeit bleibt nötig.
- Rechtsprechung oder Behördenpraxis ohne live verifizierbare Quelle zitieren.

## Output

Verteidigungsbaustein für OWiG-Verfahren mit Akteneinsicht, Einspruch, Beweisthemen und Terminstrategie.

## Übergabe an das Spezialplugin

Bei substanziellem Bußgeld-, Art.-58- oder Gerichtsrisiko lade zusätzlich `datenschutz-sanktionsverfahren-verteidigung` und dort insbesondere `kaltstart-verfahrensstand-und-mandatsziel`, `akteneinsicht-49-owig-147-stpo`, `zuständigkeit-amtsgericht-landgericht-41-bdsg`, `art-83-abs-2-kriterien-einzeln` und `art-58-anordnung-verwaltungsakt`.

## Quellen- und Verifikationsregel

- Normen vor Ausgabe live prüfen, besonders DSGVO Art. 58, 78 und 83, BDSG § 20 und § 41 sowie OWiG §§ 49, 55, 65, 67, 68, 69, 71, 72, 73 und 79.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und offizieller oder frei zugänglicher Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.
- EuGH C-807/21 und C-683/21 nur mit sauberer Kernaussage nutzen: unmittelbare Unternehmensgeldbuße ja; verschuldenslose Haftung nein.
- Wenn ein Punkt nicht verifiziert ist, als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
