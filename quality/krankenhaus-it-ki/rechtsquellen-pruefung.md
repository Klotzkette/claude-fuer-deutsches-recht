# 1. Rechercheprüfung: Krankenhaus-IT und KI

**Prüfdatum:** 06.10.2026. **Umfang dieses Protokolls:** Datenschutz, Schweigepflicht, Forschung, Thüringer Krankenhausrecht, EHDS und Drittlandtransfers. KI-Verordnung, MDR und NIS2/BSIG sind eigene Prüffelder. Dieses Protokoll bestätigt keine vollständige Prüfung sämtlicher Plugin-Dateien.

**Ergebnis:** Die verwendeten acht Entscheidungen wurden anhand amtlicher Originaltexte geprüft, darunter zwei Entscheidungen von 2026. Normkarten unterscheiden Anwendungsvoraussetzungen, Rechtsfolge, Grenze und Workflow. Beim ThürKHG verbleibt eine ausdrücklich bezeichnete Primärquellenlücke der aktuellen Konsolidierung. Sie wird weder verschwiegen noch durch ein fiktives amtliches Prüfsiegel ersetzt.

# 2. Rechtsprechung: Kontrollliste

| Gericht / Form / Datum / Aktenzeichen | ECLI und geprüfte Stelle | Gegenstand der Kontrolle | Originalquelle |
|---|---|---|---|
| EuGH, Urt. v. 14.07.2026 – Az. C-474/24 | EU:C:2026:579, Rn. 57–73 | Aktuelles Urteil, Gesundheitsdaten abhängig von Inhalt und Kontext; keine direkte Klinik-KI-Freigabe | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62024CJ0474) |
| EuGH, Urt. v. 19.03.2026 – Az. C-526/24 | EU:C:2026:216, Rn. 29–45 | Hohe Anforderungen an Missbrauchseinwand bei Auskunft; Nachweislast beim Verantwortlichen | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62024CJ0526) |
| EuGH, Urt. v. 04.09.2025 – Az. C-413/23 P | EU:C:2025:645, Rn. 52, 68–80, 100–112 | Empfängerperspektive, Identifizierbarkeit und Informationspflicht nicht vermischen | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023CJ0413) |
| EuGH, Urt. v. 04.10.2024 – Az. C-21/23 | EU:C:2024:846, Rn. 76–90 | Arzneibestelldaten; Gesundheitsinferenz auch ohne sichere Diagnose | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023CJ0021) |
| EuGH, Urt. v. 26.10.2023 – Az. C-307/22 | EU:C:2023:811, Rn. 31–43, 75–79 | Kostenlose erste Kopie, Zweckneutralität, verständliche Dokumentwiedergabe | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0307) |
| EuGH, Urt. v. 01.08.2022 – Az. C-184/20 | EU:C:2022:601, Rn. 123–128 | Indirekte besondere Daten; Transfer auf Krankenhaus ausdrücklich begrenzt | [CURIA](https://juris.curia.europa.eu/juris/document/document.jsf?docid=263721&doclang=DE) |
| EuGH, Urt. v. 16.07.2020 – Az. C-311/18 | EU:C:2020:559, Rn. 134–135 | Wirksamer Schutz beim SCC-Transfer; Privacy Shield und DPF getrennt | [CURIA](https://juris.curia.europa.eu/juris/document/document.jsf?docid=228677&doclang=DE) |
| EuG, Urt. v. 03.09.2025 – Az. T-553/23 | EU:T:2025:831, Rn. 22, 204 | Klageabweisung, Beurteilungszeitpunkt und fehlende pauschale Zukunftsgarantie | [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023TJ0553) |

Alle Links wurden am Prüftag aufgerufen und die genannten Originalstellen gelesen. Bei einzelnen CURIA- beziehungsweise Gesetze-im-Internet-Seiten schlug der erste Textabruf fehl; der öffentlich zugängliche Originaltext wurde anschließend direkt abgerufen und als Text gelesen. Keine Zusammenfassung wurde als Volltext ausgegeben. Im amtlichen Register wurde C-703/25 P als anhängiges Rechtsmittel gegen T-553/23 geführt; das Register ersetzt kein Endurteil.

# 3. Normen: verifizierte Unterschiede

| Frage | Kontrollbefund | Folge für das Plugin |
|---|---|---|
| Behandlung oder Forschung? | DSGVO Art. 6 und 9 kumulativ; Art. 9 Abs. 2 Buchst. h/Abs. 3 ist kein allgemeiner Trainingstatbestand | Zwecke in einzelnen Projektkarten prüfen |
| Konzern-IT automatisch privilegiert? | Nein; Rollen sind funktional nach Art. 4, 26 und 28 zu bestimmen | Keine globale „Konzernfreigabe“ |
| § 203 StGB veraltet zitiert? | Aktuelle Abs. 3/4 im amtlichen Original geprüft | Mitwirkung, Erforderlichkeit und Verpflichtungskette statt überholter pauschaler Outsourcingverbote |
| GDNG § 6 oder § 6a? | Amtlicher Gesamttext enthält § 6, keinen § 6a | Keine erfundene Normbezeichnung |
| § 6 GDNG erlaubt jeden Forschungsdatentransfer? | Nein; Abs. 3 enthält Weitergabebegrenzung und besondere Bedingungen für öffentlich geförderte Zusammenschlüsse | Eigene Verarbeitung und externe Übermittlung getrennt |
| GDNG-Netzwerkfreigabe? | Zustimmung der zuständigen Datenschutzaufsicht bei dem besonderen Weg des § 6 Abs. 3 | Keine Verwechslung mit Ministerium oder Landesverwaltungsamt |
| 30 Jahre stets aufbewahren? | § 6 enthält eine äußerste Grenze, keine allgemeine Mindestfrist | Projektbezogene Löschentscheidung |
| Jede Studie zwingend WHO-registrieren? | § 8 berücksichtigt, ob das Register die Projektart aufnimmt, sowie besondere Ausnahmen | Keine unzutreffende pauschale Registerpflicht |
| EHDS erlaubt bereits 2026 Sekundärnutzung? | Art. 105 enthält gestaffelte Anwendung; Kapitel IV grundsätzlich 2029, mit einzelnen Ausnahmen | Heutige Grundlage und EHDS-Roadmap trennen |
| DPF plus automatisch SCC-TIA? | Ein von Art. 45 gedeckter Transfer verlangt nicht zusätzlich pauschal das SCC-Prüfprogramm; Empfänger/Deckung bleiben zu prüfen | Getrennte DPF- und SCC-Arbeitszweige |
| SCC nur unterschreiben? | Klauseln 14/15 verlangen konkrete Bewertung, Zusammenarbeit, Dokumentation und gegebenenfalls Unterbrechung | TIA plus wirksame Maßnahmen, kein Vertragsformalismus |
| Modelle/Embeddings stets anonym? | EDSA-Stellungnahme 28/2024 verlangt Einzelfallprüfung | Empfängerwissen, Memorisation und Extraktion berücksichtigen |

Amtliche Links und Abrufdatum stehen vollständig in [der Referenzdatei](../../krankenhaus-it-ki/references/rechtsquellen.md). Behördliche Leitlinien werden als Auslegung und nicht als Gerichtsurteile bezeichnet.

# 4. Offene Primärquellenprüfung ThürKHG

Die amtliche Landesrechtsdatenbank war unter `landesrecht.thueringen.de` erreichbar, lieferte im verfügbaren Lesezugang aber keinen auslesbaren konsolidierten Normkörper. Deshalb erfolgte der Abgleich mit zwei nichtamtlichen Konsolidierungen und der amtlichen datenschutzrechtlichen Änderung von 2018. Die Konsolidierungen verzeichnen die Änderung vom 30.12.2025, GVBl. 2026 S. 19. Die aktuelle amtliche Endfassung und Änderungsverarbeitung wurden hier **nicht vollständig verifiziert**.

In der anwalt24-Wiedergabe zu § 27 Abs. 3 fiel eine sprachliche Abweichung auf: Die amtliche Änderung 2018 ersetzt den früheren Verarbeitungskatalog durch „verarbeitet“; die umwelt-online-Konsolidierung entspricht dem. Es wird deshalb kein ungeprüftes wörtliches Zitat aus der abweichenden Wiedergabe verwendet.

Besonders folgenreiche, anhand der genannten Quellen abgeglichene Arbeitsregeln:

1. § 27b Abs. 1 Nr. 3: schriftliche Anzeige rechtzeitig **vor Auftragserteilung**, keine automatisch behauptete Genehmigungspflicht.
2. § 27b i. V. m. § 32 Abs. 2: Adressat **Landesverwaltungsamt**; nicht allein DSB oder Datenschutzaufsicht.
3. § 27b Abs. 3: Wartung/Fernwartung einschließen, wenn Datenzugriff nicht ausgeschlossen werden kann.
4. § 27a Abs. 2 Nr. 2 i. V. m. § 32 Abs. 1: konkrete Forschungsfeststellung beim **für das Krankenhauswesen zuständigen Ministerium**; weitere Voraussetzungen kumulativ.
5. Keine stillschweigende Gleichsetzung dieser Wege mit der **Datenschutzaufsichtszustimmung** nach § 6 Abs. 3 GDNG.

Für einen realen Cloudauftrag oder Forschungsdatentransfer ist diese Quellenlücke vor Einreichung/Produktivfreigabe anhand der amtlichen Endfassung zu schließen. Diese Beschränkung betrifft nicht das Erstellen der Testakte oder der vorbereitenden Entwürfe. Die konkrete Anwendung des allgemeinen Landesdatenschutzrechts beziehungsweise des BDSG auf den kommunalen Träger bleibt ebenfalls eine vom tatsächlichen Rechtsträger abhängige Subsumtion, keine durch den Zusatz „GmbH“ erledigte Feststellung.

# 5. Abnahmegrenze

Die Recherchedateien bestätigen weder eine bestimmte Anbieterkonfiguration noch eine tatsächliche Zertifizierung, Krankenhausgenehmigung, Behördenanzeige, Ethikfreigabe oder Betriebsaufnahme. Solche Nachweise müssen aus der konkreten Projektakte kommen. Fiktive Anbieter und Klinikunterlagen dürfen in der Testakte nicht als geprüfte reale Organisationen erscheinen. Sämtliche neuen Anker bleiben durch Gericht, Datum, Aktenzeichen, Fundstelle und konkreten Fallbezug überprüfbar; keine Literatur-Blindzitate wurden ergänzt.
