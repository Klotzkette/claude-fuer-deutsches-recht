# Compliance-Abteilung im Großkonzern

Das Plugin unterstützt Rechts- und Compliance-Teams eines Industriekonzerns bei konkreten Entscheidungen. Es ordnet Zuständigkeiten und Belege, bereitet Freigaben, Ermittlungen, Kontrollentscheidungen und Organvorlagen vor und hält die Grenzen der jeweiligen Freigabe fest.

In 39 fiktiven Fällen übernehmen Sie die Rolle der Konzern-Compliance. Die meisten Akten spielen bei Merrensteg Elektrosysteme SE, einem Hersteller von Industrieantrieben und Schalttechnik in Hameln. Die Schokoladenakte führt in eine eigenständige Lebensmittelfabrik der Region. Jeder Fall beginnt mit einer lesbaren Geschichte über Betrieb, Beteiligte, Konflikt und anstehende Entscheidung. Der Einstieg führt in der Reihenfolge der Bearbeitung zu den Originalstücken und erklärt, wo die digitale Auswertung oder der Prozess in die Irre führen kann.

## 1 Einstieg

| Produkt | Zugriff |
| --- | --- |
| Installierbares Plugin | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/compliance-abteilung-grosskonzern-v445.35.13/compliance-abteilung-grosskonzern.zip) |
| Ausführlicher Prompt | [MD herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/compliance-abteilung-grosskonzern-werkstatt.md) |
| Master-Prompt | [MD herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=testakten/megaprompts/compliance-abteilung-grosskonzern.md) |
| Kompakter Prompt | [MD herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/compliance-abteilung-grosskonzern-schnellstart.md) |
| Quellen | [Zitierweise und amtliche Fundstellen](references/zitierweise.md) |

[Repository-Start](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Alphabetische Skill-Liste](../skills-index/compliance-abteilung-grosskonzern.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [Plugin-Dateien](.)

### 1.1 Eigenständige Fachskills

Jeder Fachskill kann direkt aufgerufen werden. Er verarbeitet die vorhandenen Unterlagen und liefert das bestellte Arbeitsprodukt mit der erforderlichen Beleg- und Entscheidungsgrundlage.

| Fachskill | Arbeitsprodukt | Schwerpunktakte |
| --- | --- | --- |
| [Interne Untersuchung entscheiden](skills/interne-untersuchung-entscheiden/SKILL.md) | Schutz- und Sicherungsanordnung, Anhörung und vertraulicher Befund je Vorwurf | [ME-22 · Der Hinweis aus der Nachtschicht](../testakten/compliance-hameln-meldung-nachtschicht/README.md) |
| [Geschäftspartnerfreigabe entscheiden](skills/geschaeftspartner-freigabe-entscheiden/SKILL.md) | Begründeter Entscheid je Vertrag, Leistung und Zahlungsweg mit prüfbaren Freigabebedingungen | [ME-24 · Acht Prozent für eine Türöffnung](../testakten/compliance-hameln-vertriebspartner-marktstart/README.md) |
| [Kontrollversagen und Organentscheidung](skills/kontrollversagen-und-organentscheidung/SKILL.md) | Nachgerechneter Kontrollbefund, Organvorlage und Kriterien für den Wiederanlauf | [ME-28 · 98 Prozent grün und vier ungeklärte Freigaben](../testakten/compliance-hameln-wirksamkeit-nachtest/README.md) |
| [KI-System zur Betriebsfreigabe prüfen](skills/ki-system-betriebsfreigabe-entscheiden/SKILL.md) | Einstufung, dokumentierte Abnahmekriterien und Entscheidung über Pilot, Betrieb oder Aussetzung | [ME-35 · Der Score vor der ersten Nachtschicht](../testakten/compliance-hameln-personalscore-vor-start/README.md) |

## 2 KI in Recht und Compliance

| Vorgang | Fall | Thema | Word-Vorlage |
| --- | --- | --- | --- |
| ME-01 | [Drei Systeme für die Rechtsabteilung](../testakten/compliance-hameln-ki-toolpilot/README.md) | Beschaffung und Vergleich allgemeiner und juristischer KI | [Vorlage](templates/compliance-hameln-ki-toolpilot.docx) |
| ME-02 | [Die Arbeitsanweisung aus dem alten Ordner](../testakten/compliance-hameln-prompt-register/README.md) | Prompt-Verwaltung, Testfälle und praktische Befähigung | [Vorlage](templates/compliance-hameln-prompt-register.docx) |
| ME-03 | [Ein Vermerk im falschen Arbeitsbereich](../testakten/compliance-hameln-vertraulicher-testtenant/README.md) | Berufsgeheimnis und Datenschutz bei externer KI | [Vorlage](templates/compliance-hameln-vertraulicher-testtenant.docx) |
| ME-04 | [Zwei Belege und ein schnelles Urteil](../testakten/compliance-hameln-zweite-rechnung/README.md) | Quellenprüfung, Halluzinationen und tragfähige Rechtsbegriffe | [Vorlage](templates/compliance-hameln-zweite-rechnung.docx) |
| ME-05 | [Der Knopf für die automatische Vorauswahl](../testakten/compliance-hameln-freigabe-personalassistent/README.md) | Nutzungsgrenzen des Anbieters und menschliche Aufsicht | [Vorlage](templates/compliance-hameln-freigabe-personalassistent.docx) |
| ME-06 | [Die falsche Fassung in der Ausgangsmappe](../testakten/compliance-hameln-schriftsatz-version/README.md) | Fehlerfolgen, Berichtigung und Verantwortung bei KI-Einsatz | [Vorlage](templates/compliance-hameln-schriftsatz-version.docx) |
| ME-07 | [Kühlung für den umgebauten Antrieb](../testakten/compliance-hameln-retrofit-beratung/README.md) | Rechtsrecherche, Beratungsalternativen und Prüfung konkurrierender Einschätzungen | [Vorlage](templates/compliance-hameln-retrofit-beratung.docx) |
| ME-08 | [Zwei Termine im Regulierungsmonitor](../testakten/compliance-hameln-meldefrist-firmware/README.md) | Monitoring regulatorischer Änderungen und technischer Rechtsbegriffe | [Vorlage](templates/compliance-hameln-meldefrist-firmware.docx) |
| ME-09 | [Ein Update und drei Meldezeiten](../testakten/compliance-hameln-wartungsvertrag-redline/README.md) | Vertrags- und Policy-Vergleich, Bearbeitung und Zusammenfassung | [Vorlage](templates/compliance-hameln-wartungsvertrag-redline.docx) |
| ME-10 | [Ein Muss auf drei Sprachen](../testakten/compliance-hameln-sprache-im-werk/README.md) | Compliance-Content, Übersetzung und Veröffentlichung | [Vorlage](templates/compliance-hameln-sprache-im-werk.docx) |
| ME-11 | [Die Schicht ohne Lernnachweis](../testakten/compliance-hameln-training-nachtschicht/README.md) | Compliance-Training und Awareness | [Vorlage](templates/compliance-hameln-training-nachtschicht.docx) |
| ME-12 | [Der Freigabestempel nach dem Auftrag](../testakten/compliance-hameln-kontrollen-vor-freigabe/README.md) | Risiken, Kontrollen und Prozessauswertung | [Vorlage](templates/compliance-hameln-kontrollen-vor-freigabe.docx) |
| ME-13 | [Der Treffer mit zwei Adressen](../testakten/compliance-hameln-treffer-im-lieferantencheck/README.md) | Third-Party-Screening und Maßnahmen | [Vorlage](templates/compliance-hameln-treffer-im-lieferantencheck.docx) |
| ME-14 | [Die sechs Rechnungen für eine Nachtschicht](../testakten/compliance-hameln-untersuchung-servicekonto/README.md) | Interne Untersuchung und Beweissicherung | [Vorlage](templates/compliance-hameln-untersuchung-servicekonto.docx) |
| ME-15 | [Das fehlende Wort im Interview](../testakten/compliance-hameln-interview-und-transkript/README.md) | KI-Interviewtranskripte und menschlicher Abgleich | [Vorlage](templates/compliance-hameln-interview-und-transkript.docx) |
| ME-36 | [Die Auskunft mit den roten Markierungen](../testakten/compliance-hameln-auskunft-mit-schwaerzungen/README.md) | Kundenauskunft, KI-Schwärzungen und Bildbeifang | [Word-Vorlage](../testakten/compliance-hameln-auskunft-mit-schwaerzungen/07_Vorlage_Auskunftsschreiben.docx) |
| ME-16 | [Drei rote Punkte vor dem Ausschuss](../testakten/compliance-hameln-vorstandsreport-mit-ki/README.md) | KI-unterstütztes Organreporting | [Vorlage](templates/compliance-hameln-vorstandsreport-mit-ki.docx) |
| ME-17 | [Der Assistent am Aufsichtsratstisch](../testakten/compliance-hameln-aufsichtsrat-eigener-assistent/README.md) | KI-Nutzung durch das Organ | [Vorlage](templates/compliance-hameln-aufsichtsrat-eigener-assistent.docx) |

## 3 Arbeit des Compliance-Managements

| Vorgang | Fall | Thema | Word-Vorlage |
| --- | --- | --- | --- |
| ME-18 | [Der Schichttausch nach der Beschwerde](../testakten/compliance-hameln-schichttausch-kodex/README.md) | Werte, Führung, Kodex und verhältnismäßige Personalmaßnahmen | [Vorlage](templates/compliance-hameln-schichttausch-kodex.docx) |
| ME-19 | [Dreimal dieselbe Seriennummer](../testakten/compliance-hameln-seriennummer-fruehwarnung/README.md) | Prävention, Früherkennung und Reputationsschutz | [Vorlage](templates/compliance-hameln-seriennummer-fruehwarnung.docx) |
| ME-20 | [Vier Werke und nur 320 Prüfstunden](../testakten/compliance-hameln-vier-werke-risikobudget/README.md) | Konzernweite Compliance-Risikoanalyse und Ressourcensteuerung | [Vorlage](templates/compliance-hameln-vier-werke-risikobudget.docx) |
| ME-21 | [Drei Einladungen am Vorabend der Vergabe](../testakten/compliance-hameln-abendessen-messe/README.md) | Richtlinienberatung und dokumentierter Ausnahmeantrag | [Vorlage](templates/compliance-hameln-abendessen-messe.docx) |
| ME-22 | [Der Hinweis aus der Nachtschicht](../testakten/compliance-hameln-meldung-nachtschicht/README.md) | Hinweisaufnahme, Vertraulichkeit und Schutz vor Nachteilen | [Vorlage](templates/compliance-hameln-meldung-nachtschicht.docx) |
| ME-23 | [Zwei Rechnungen für dieselbe Prüffahrt](../testakten/compliance-hameln-wartungsvertrag-doppelbuchung/README.md) | Interne Untersuchung, Belegsicherung und Fallregister | [Vorlage](templates/compliance-hameln-wartungsvertrag-doppelbuchung.docx) |
| ME-24 | [Acht Prozent für eine Türöffnung](../testakten/compliance-hameln-vertriebspartner-marktstart/README.md) | Geschäftspartnerprüfung und Korruptionsselbstbewertung je Rechtsträger | [Vorlage](templates/compliance-hameln-vertriebspartner-marktstart.docx) |
| ME-25 | [Der Zukauf mit zwei offenen roten Linien](../testakten/compliance-hameln-zukauf-schaltservice/README.md) | M&A-Due-Diligence und Integration nach Vollzug | [Vorlage](templates/compliance-hameln-zukauf-schaltservice.docx) |
| ME-26 | [Die Akte zwischen zwei Sitzungen](../testakten/compliance-hameln-bericht-zwischen-sitzungen/README.md) | Konzern-Governance, Zuständigkeiten und Berichte an das Aufsichtsorgan | [Vorlage](templates/compliance-hameln-bericht-zwischen-sitzungen.docx) |
| ME-27 | [Gelesen ist noch nicht verstanden](../testakten/compliance-hameln-kampagne-werkstattdialog/README.md) | Compliance-Kommunikation, Training und Dialog für interne und externe Adressaten | [Vorlage](templates/compliance-hameln-kampagne-werkstattdialog.docx) |
| ME-28 | [98 Prozent grün und vier ungeklärte Freigaben](../testakten/compliance-hameln-wirksamkeit-nachtest/README.md) | Wirksamkeitsprüfung, Audit, Befragung, Benchmark und Nachtest | [Vorlage](templates/compliance-hameln-wirksamkeit-nachtest.docx) |

## 4 KI-Einführung und Arbeit

[Master-Prompt zur Einführung und Qualifizierung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=testakten/megaprompts/compliance-abteilung-grosskonzern.md) · [Prüfreihenfolge](references/ki-arbeit-pruefpfad.md)

| Vorgang | Fall | Thema | Vorlage |
| --- | --- | --- | --- |
| ME-29 | [Vier Minuten schneller und zweimal falsch](../testakten/compliance-hameln-vorstand-freigabefenster/README.md) | Vorstandssorgfalt, Pilotnachweis und Grenzen einer KI-Nutzungsvorgabe | [Word-Vorlage](templates/compliance-hameln-vorstand-freigabefenster.docx) |
| ME-30 | [Ein Haken im System und ein Fehler beim Kunden](../testakten/compliance-hameln-freigabehaken-im-service/README.md) | Persönliche Arbeitsleistung, Qualitätsanforderung, Abmahnung und Belegkette | [Word-Vorlage](templates/compliance-hameln-freigabehaken-im-service.docx) |
| ME-31 | [Der Gastzugang mit der Stückliste](../testakten/compliance-hameln-offenes-fenster-fuer-stuecklisten/README.md) | Geschäftsgeheimnis, öffentlicher KI-Dienst, Datenschutzvorfall und § 626 BGB | [Word-Vorlage](templates/compliance-hameln-offenes-fenster-fuer-stuecklisten.docx) |
| ME-32 | [Alle mussten klicken und keiner konnte stoppen](../testakten/compliance-hameln-pflichtbetrieb-ohne-ausgang/README.md) | Verbindlicher KI-Einsatz, Organisationsverantwortung, KI-Kompetenz und Aufsicht | [Word-Vorlage](templates/compliance-hameln-pflichtbetrieb-ohne-ausgang.docx) |
| ME-33 | [Sechs Wochen Kurs und zwei unbesetzte Stellen](../testakten/compliance-hameln-freie-stelle-nach-dem-kurs/README.md) | KI-bedingter Arbeitsplatzabbau, zumutbare Qualifizierung und Sozialauswahl | [Word-Vorlage](templates/compliance-hameln-freie-stelle-nach-dem-kurs.docx) |
| ME-34 | [Die alte Linie und der leere Schulungsraum](../testakten/compliance-hameln-montageinsel-sozialplan/README.md) | Betriebsänderung, Interessenausgleich, Qualifizierungs-Sozialplan und § 97 BetrVG | [Word-Vorlage](templates/compliance-hameln-montageinsel-sozialplan.docx) |
| ME-35 | [Der Score vor der ersten Nachtschicht](../testakten/compliance-hameln-personalscore-vor-start/README.md) | Beschäftigungs-KI nach Anhang III, Art. 26 Abs. 7, DSGVO und Betriebsrat | [Word-Vorlage](templates/compliance-hameln-personalscore-vor-start.docx) |

## 4.1 Produkt- und Personal-Compliance

| Fall | Anlass |
| --- | --- |
| ME-37 · [Die Tafel aus Charge K17](../testakten/compliance-hameln-schokolade-charge-k17/README.md) | Rezepturänderung, Süßstoffe, Kennzeichnung, Chargen und Maßnahmen im Handel |
| ME-38 · [Das Wochenende des Geschäftsführers](../testakten/compliance-hameln-geschenk-geschaeftsfuehrung/README.md) | Einladung an den Geschäftsführer, Vergabeentscheidung, Interessenkonflikt und Kontrollspur |
| ME-39 · [Das Sicherheitsrelais mit der falschen Freigabe](../testakten/compliance-hameln-sicherheitsrelais-hinweis/README.md) | Sicherheitsrelais, widersprüchliche Prüfbelege, Feldmaßnahmen und Schutz nach einem Hinweis |

## 5 Workshop-Downloads

Jede Aktenseite führt zu Originalformat-ZIP, Einzel-PDF-ZIP und einer Gesamt-PDF mit Lesezeichen. Die Materialien enthalten EML, DOCX, XLSX, CSV, PNG und PDF. Ausgewählte Besprechungen enthalten zusätzlich bearbeitbare PowerPoint-Folien.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Datei |
| --- | --- |
| 39 Arbeitsakten in Originalformaten mit Gesamt-PDFs und bearbeitbaren Vorlagen | [Workshop-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/compliance-hameln-praxis-v1.0.0/Hameln_Compliance_39_Praxisakten.zip) |
| 35 getrennte fallbezogene Prüfblätter aus den beiden Reihen | [Nachbesprechung als ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/compliance-abteilung-grosskonzern-v445.35.13/Hameln_Compliance_Nachbesprechung_35.zip) |
| ME-36 · Auskunft nach Art. 15 DSGVO | [Akten-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/compliance-hameln-praxis-v1.0.0/testakte-compliance-hameln-auskunft-mit-schwaerzungen.zip) · [Fall und Moderationsmaterial](../testakten/compliance-hameln-auskunft-mit-schwaerzungen/README.md) |

Die Nachbesprechung enthält die bisherigen Prüfblätter der beiden Fallreihen. Die ergänzenden Stellungnahmen und Sicherungsprotokolle sind im eigenen Durchlauf zusätzlich gegen die ursprünglichen Belege zu prüfen. Die Aktenseiten bieten die jeweiligen Originalformat-ZIPs und Einzel-PDF-ZIPs; die Nachbesprechung liegt getrennt von diesen Arbeitsunterlagen.

## 6 Ablauf der Vorführung

Lesen Sie gemeinsam den Sachverhalt am Anfang. Klären Sie in einem Satz, wer heute über was entscheiden muss. Laden Sie für die erste Runde nur die dort benannten Ausgangsbelege. Fordern Sie eine Erklärung in Alltagssprache und eine vorläufige Entscheidung. Legen Sie die widersprechende Unterlage erst dann nach. Die Prüfmatrix gehört an das Ende des Durchlaufs. Sie verknüpft die entscheidenden Aussagen mit Originalstellen und zeigt, was noch fehlt.

| Wenn Sie vorführen möchten, wie … | Öffnen Sie … | Woran Sie den Nutzen erkennen |
| --- | --- | --- |
| … man ein KI-Werkzeug für den Betrieb auswählt | [ME-01 · KI-Toolpilot](../testakten/compliance-hameln-ki-toolpilot/README.md) | Der Entwurf legt fest, was ein Pilot beweisen muss und welche Daten dabei verwendet werden dürfen. |
| … ein Ranking in die Personalauswahl eingreift | [ME-35 · Der Score vor der ersten Nachtschicht](../testakten/compliance-hameln-personalscore-vor-start/README.md) | Die Gruppe findet heraus, ob die zuständige Schichtleitung ausgeblendete Bewerbungen sehen und berücksichtigen kann. |
| … ein unzulässiges Produkt aus dem Handel genommen werden kann | [ME-37 · Die Tafel aus Charge K17](../testakten/compliance-hameln-schokolade-charge-k17/README.md) | Die Gruppe verbindet Rezeptur, Labor und Lieferdaten und formuliert eine konkrete Entscheidung für die betroffene Charge. |
| … ein Interessenkonflikt vor dem Zuschlag aufgeklärt wird | [ME-38 · Geschenk und Vergabe](../testakten/compliance-hameln-geschenk-geschaeftsfuehrung/README.md) | Die Gruppe prüft Einladung, Empfänger, Rolle und Genehmigungsstand vor der Entscheidung über den Anbieter. |
| … Produktsicherheit und der Schutz einer hinweisgebenden Person parallel bearbeitet werden | [ME-39 · Sicherheitsrelais und Hinweis](../testakten/compliance-hameln-sicherheitsrelais-hinweis/README.md) | Die Gruppe verfolgt Seriennummern, Prüfstände und Schichtentscheidung in den Originaldaten. |

Bei ME-22, ME-24, ME-28 und ME-35 folgt eine zusätzliche Runde mit den Stücken 14 bis 16. Legen Sie den ersten Entwurf neben die neuen Belege. Lassen Sie die Änderung an der Handlungsempfehlung begründen und nutzen Sie die Fortsetzungsseite der jeweiligen Word-Vorlage. [Leitfaden für die Moderation](../quality/compliance-vertiefung/fachvertiefung-moderation.md).



<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`compliance-auftrag-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/compliance-auftrag-steuern/SKILL.md) | Steuert konkrete Aufträge der Konzernrechts- und Compliance-Abteilung bis zum fertigen Arbeitsprodukt. Für Richtlinienauskunft, Ausnahmeentscheidung, Rechtsrecherche und Regulierungsmonitoring sowie die Zuordnung zu KI-Freigabe, Meldeste... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/compliance-auftrag-steuern/SKILL.md) |
| [`geschaeftspartner-freigabe-entscheiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/geschaeftspartner-freigabe-entscheiden/SKILL.md) | Entwirft eine nachprüfbare Freigabe, Auflage oder Zurückstellung für eine konkrete Bestellung, Lieferung, Zahlung, Vermittlung oder Erwerbsphase. Klärt Geschäftspartneridentität, Eigentum und Kontrolle, Sanktionen, Vergütung und Korrupti... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/geschaeftspartner-freigabe-entscheiden/SKILL.md) |
| [`geschaeftspartner-und-transaktionen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/geschaeftspartner-und-transaktionen/SKILL.md) | Bearbeitet Integritätsprüfung und Freigaben bei Lieferanten, Vermittlern, Bewirtungen und Unternehmenskäufen. Für Identitäts- und Trefferklärung, Leistungs- und Zahlungsabgleich, Korruptionsrisiko, ausformulierte Auflagen, Vertragsbeding... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/geschaeftspartner-und-transaktionen/SKILL.md) |
| [`interne-untersuchung-entscheiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/interne-untersuchung-entscheiden/SKILL.md) | Erarbeitet eine belastbare Zwischen- oder Abschlussentscheidung in internen Compliance-Untersuchungen. Führt Vorwürfe, Originalbelege, Gegenbelege, Anhörung und Datenschutz zu einem entscheidungsreifen Befund zusammen und trennt geschütz... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/interne-untersuchung-entscheiden/SKILL.md) |
| [`ki-einsatz-und-freigabe`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/ki-einsatz-und-freigabe/SKILL.md) | Prüft KI-Beschaffung und konkrete Nutzung in Legal, Compliance und Beschäftigung. Für belastbare Pilottests, Prompt-Versionierung, Datenflüsse, Quellenkorrektur, menschliche Kontrolle, Fehlerzurechnung, Kompetenzmaßnahmen, Qualifizierung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/ki-einsatz-und-freigabe/SKILL.md) |
| [`ki-system-betriebsfreigabe-entscheiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/ki-system-betriebsfreigabe-entscheiden/SKILL.md) | >- | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/ki-system-betriebsfreigabe-entscheiden/SKILL.md) |
| [`kontrollen-und-organberichte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/kontrollen-und-organberichte/SKILL.md) | Erstellt risikobasierte Kontrollpläne, belastbare Kennzahlen, Wirksamkeitstests, Schulungs- und Kommunikationsprodukte sowie Organvorlagen. Für Rohdatenabgleich, Nennerfehler, Stichprobengrenzen, lokale Zuständigkeit, Maßnahmenverfolgung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/kontrollen-und-organberichte/SKILL.md) |
| [`kontrollversagen-und-organentscheidung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/kontrollversagen-und-organentscheidung/SKILL.md) | >- | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/kontrollversagen-und-organentscheidung/SKILL.md) |
| [`meldungen-und-untersuchungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/meldungen-und-untersuchungen/SKILL.md) | Bearbeitet interne Meldungen, Schutzmaßnahmen und Untersuchungen bis zu verwendbaren Schreiben und Abschlussvermerken. Für HinSchG-Fristen, Vertraulichkeit, Beweissicherung, Gegenbelege, Interviews, korrigierte KI-Transkripte, Anhörung u... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=compliance-abteilung-grosskonzern/skills/meldungen-und-untersuchungen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
