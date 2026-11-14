# Quellenprüfung vom 14. November 2026

Die Runde verbindet eine Bestandsaufnahme aller **315 Pluginprofile** mit gezielten fachlichen Korrekturen. Für **elf gerichtliche Entscheidungen** wurden die jeweils tragenden Passagen im amtlichen Volltext gelesen und mit begrenzten Aussagen verarbeitet. Hinzu kommen Normtexte, eine Behördenleitlinie und gesondert gekennzeichnete Leitsatz- und Pressequellen. Das ist keine neue Volltextprüfung sämtlicher Rechtsprechungsangaben oder aller Plugininhalte.

## 1. Bestandsaufnahme und Metadaten

Die [maschinenlesbare Bestandsübersicht](quellenbestand-uebersicht.json) enthält 315 Plugin-Einträge, 143 Themenfamilien, 3.183 Quellenangaben in Profilen, 2.641 unterschiedliche URLs aus Profilen und Werkstatt-Prompts sowie 942 registrierte Entscheidungsanker. Diese Zahlen beschreiben den dokumentierten Bestand vor der parallelen Skillkonsolidierung, bezogen auf Commit `dbfbb6f63b15bf52110e8db06b4bb78e953f6db3`. Vorhandene Abrufdaten wurden übernommen, nicht auf den 14. November fortgeschrieben. Die dortigen Skillzahlen sind historische Inventarangaben, keine Zählung der jetzt aktiven Arbeitswege.

Der dazugehörige heuristische Metadatenlauf erfasste **26.756 Dateien** und 10.658 ausdrücklich datierte Zitierstellen. Seine unterschiedlichen Kombinationen aus Gericht, Datum und Aktenzeichen verteilen sich so:

| Amtlicher Index | Passende Metadaten | Ohne Indexeintrag | Abweichendes Indexdatum |
| --- | ---: | ---: | ---: |
| Bundesindex | 1.107 | 336 | 3 |
| EU-Publikationsamt | 301 | 1 | 1 |

Ein Treffer bestätigt weder die behauptete Rechtsfolge noch deren Übertragbarkeit. Ein fehlender Treffer beweist keinen Zitierfehler. Die vier Datumsabweichungen betreffen bereits eingeordnete Berichtigungen, weitere Entscheidungen unter demselben Aktenzeichen oder verbundene Verfahren. 27 zusätzlich markierte Datumsstellen wurden im Kontext gesichtet; daraus ergab sich kein neuer belegter Zitierfehler. Einzelheiten und Speicherorte der Arbeitsnachweise stehen im [Bestands- und Delta-Bericht](verfassungs-europa-produkt.md). Die [Runde vom 10. November](../2026-11-10/README.md) bleibt als eigener früherer Prüfstand erhalten.

## 2. Tatsächlich gelesene Entscheidungsgründe

„Volltext“ bezeichnet hier die amtliche Quelle; geprüft wurden die dokumentierten Passagen und ihr Entscheidungskontext. Es wird nicht behauptet, jede Randnummer aller elf Entscheidungen neu ausgewertet zu haben. Die folgende Auswahl umfasst sieben Entscheidungen aus den Kerngebieten und vier aus Verfassungs-, Europa- und Produktrecht:

| Entscheidung | Wesentliches Ergebnis der Prüfung |
| --- | --- |
| BAG 5 AZR 37/25, 26.08.2026 | Der inzwischen verfügbare Volltext ersetzt den bisherigen Pressebeleg. Vermittlungsauskunft verlangt keine Wahrscheinlichkeit einer Anrechnung; Auskunft, sekundäre Darlegungslast und Lohnanspruch bleiben getrennt. |
| BFH X B 2/26, 23.10.2026 | Angebotenen Buchhaltungszugriff und Akteninhalt berücksichtigen. Die Nichtigkeit der Schätzung blieb offen; Zurückverweisung ist kein abschließendes Nichtigkeitsurteil. |
| EuGH C-205/25, 05.11.2026 | Auskunft über eigene Daten auch bei der Aufsichtsbehörde; kein allgemeiner Anspruch auf die gesamte Verwaltungsakte, Drittbelange konkret prüfen. |
| EuGH C-484/24, 18.06.2026 | Art. 17 Abs. 3 Buchst. e DSGVO ist keine eigene Verarbeitungsgrundlage. Gerichtliche Beweisverwendung erlaubt nicht allgemein vorgelagerte Datenerhebung oder KI-Uploads. |
| BGH IX ZR 150/25, 05.11.2026 | Insolvenzfeststellungsbescheid und Leistungsbescheid unterscheiden. Der maßgebliche Krisenbeginn für Säumniszuschläge ist nicht pauschal die Verfahrenseröffnung. |
| BGH IX ZR 65/25, 24.09.2026 | Eine konkrete Nichtzahlungserklärung kann Zahlungseinstellung und Kenntnis indizieren. Daraus folgen nicht automatisch Vorsatz nach § 133 InsO oder Überschuldung. |
| BGH IX ZR 114/23, 19.12.2024 | Identität von angemeldeter, geprüfter und eingeklagter Forderung bei Rückabtretung; keine allgemeine Doppelanmeldungspflicht für Zedent und Zessionar. |
| BVerfG 2 BvE 7/20, 2 BvR 420/21, 14.10.2026 | Substantiierung einer Ultra-vires-Rüge anhand der einschlägigen Maßstäbe und begründeten Gegenpositionen. Unzulässigkeit ist keine materielle Pauschalfreigabe des PEPP. |
| BVerfG 2 BvR 927/25, 15.10.2026 | Auslagenerstattung nach Erledigung anhand des konkreten Abhilfegrundes und nach Billigkeit; kein Automatismus. |
| EuG T-523/24, 11.11.2026 | Sicherheitsnachweis bei Zulassung bzw. Verlängerung von Raucharoma-Primärprodukten. Keine Entscheidung über Schokolade und keine allgemeine Beweislastregel für Produktrückrufe. |
| EuGH C-512/23, 12.11.2026 | Rechtsgrundlage der CBAM-Verordnung nach Ziel, Inhalt und Kontext. Keine Entscheidung über einzelne Importberechnungen oder sämtliche späteren Pflichtenänderungen. |

Die [Kerngebietsprüfung](kerngebiete.md) nennt die amtlichen Fundstellen, gelesenen Randnummern und Grenzen der ersten sieben Entscheidungen. Für die weiteren vier enthält der [Fachbericht](verfassungs-europa-produkt.md) dieselben Angaben; der [JSON-Nachweis](delta-verfassungs-europa-produkt.json) dokumentiert Abruf-Hashes und sieben geänderte Werkstatt-Prompts. Quellen- und Fassungsbindungen der Kerngebiete stehen außerdem in den Profilen [Arbeitsrecht](../../evals/fachanwalt-arbeitsrecht.json), [Datenschutz](../../evals/datenschutzrecht.json), [Steuerrecht](../../evals/steuerrecht-anwalt-und-berater.json) und [Insolvenzrecht](../../evals/insolvenzrecht.json). Gesicherte Downloads allein zählen nicht als fachlich gelesene Entscheidungen.

## 3. Echte Fehlerkorrekturen

- **Insolvenzforderungen:** Die behauptete allgemeine Doppelanmeldungspflicht wurde anhand von IX ZR 114/23 berichtigt. Hinzu kamen konkrete Normkorrekturen zu Verfolgungslast, Zuständigkeit, Monats- und Nachweisfristen, Sicherheiten, Regress, bedingten Forderungen und Aufrechnung. Die [Kerngebietsprüfung](kerngebiete.md) grenzt den Umfang gegenüber den unverändert übernommenen Sonderfällen ab.
- **DSGVO-Auskunft:** Die unzutreffende Fristberechnung anhand der EuGH-Verfahrensordnung wurde berichtigt. Datenkopie und Datenübertragbarkeit sowie Art. 15 Abs. 1 Buchst. a bis h, Abs. 2 und Abs. 3 werden unterschieden. Die EDSA-Leitlinien sind als Behördenleitlinie ausgewiesen, nicht als Urteil.
- **Historischer § 370a AO:** Eine erfundene BVerfG-Nichtigerklärung wurde entfernt. Belegt ist die gesetzgeberische Aufhebung zum 01.01.2008; der herangezogene BVerfG-Beschluss vom 23.06.2010 betrifft Untreue. Auch Regelbeispielnummern, Zeitvergleich, Verjährung und Registerfolgen wurden differenziert. Der [eigene Korrekturbericht](steuerstrafrecht-370a.md) trennt gelesene Normen, BVerfG-Leitsätze und nur eingeschränkt zugängliche Rechtsprechung.

Die historischen Prüfstände bleiben erhalten. Ein neuer Hash bindet die konkret geprüfte Fassung; er ist kein Nachweis einer darüber hinausgehenden rechtlichen Vollprüfung.

## 4. Pressemitteilungen, Leitsätze und offene Kandidaten

- **BAG 5 AZR 37/25:** Pressegrundlage durch die oben ausgewerteten Volltextpassagen ersetzt.
- **BVerwG 8 C 11.25 und 8 C 10.25:** Amtliche Pressemitteilungen gelesen, neue Urteilsgründe hier nicht abgerufen. Ältere Zulassungsbeschlüsse werden nicht als diese Urteilsgründe ausgegeben.
- **EuGH C-395/25, Orkla Care:** Amtliche Pressemitteilung gefunden, Volltext noch nicht gelesen; daraus keine neue konkrete Rechtsaussage übernommen.
- **EuGH C-826/24 P, Google AdSense:** Schlussanträge, kein Urteil. Die für den 16.11.2026 angekündigte BVerfG-Entscheidung zu Telekommunikations-Bezugsverträgen wird am Prüfdatum ebenfalls nicht als ergangen behandelt.
- **§-370a-Korrektur:** Beim BVerfG-Beschluss vom 23.06.2010 wurden Leitsätze und Verfahrensgegenstand zur Aufklärung der Fehlzuordnung geprüft. Zu BGH 1 StR 373/15 war nur der amtliche Leitsatz im Suchergebnis zugänglich; keine Volltext- oder Randnummernverifikation behauptet.
- **Weitere Recherche:** BAG 2 AZR 89/25 und 2 AZR 184/25 wurden gesichert, hier nicht als neu geprüfte Anker gezählt. Zum aktuellen KI-Verordnungsänderungsakt gelang im betreffenden Teilauftrag kein belastbarer Volltextabruf; eine entsprechende Volltextaktualisierung unterblieb.

Die Fundstellen und Abrufgrenzen stehen in den drei verlinkten Fachberichten. Diese Liste beschreibt den Umfang dieser Runde, keine abschließende Liste aller offenen Quellenfragen des Repositorys.

## 5. Weiterhin offene Profile und Prüfgrenzen

Der aktuelle JSON-Abgleich bestätigt weiterhin vier Profile mit `file_review_status.status = needs_review` und insgesamt **31 offenen Dateireviews**:

| Profil | Offene Dateireviews |
| --- | ---: |
| [anwaltschaft-generell](../../evals/anwaltschaft-generell.json) | 2 |
| [corporate-contract-law](../../evals/corporate-contract-law.json) | 20 |
| [gesellschafterstreit](../../evals/gesellschafterstreit.json) | 3 |
| [wirtschaftsanwalt](../../evals/wirtschaftsanwalt.json) | 6 |

Historische Hashes decken deren heutigen Dateistand nicht ab; die vorgesehenen neuen Ergebnisläufe bleiben bis zur dokumentierten Nachprüfung gesperrt. Fehlende registrierte Werkstatt-Anker bei `grundstuecksrecherche` und `schriftsatzwerkstatt-bea` sind zusätzlich als Organisationshinweis erfasst, nicht als bewiesener Rechtsfehler.

Die [Nachprüfung der Bauwirtschaft-Visualisierung](bauwirtschaft-visualisierung-nachpruefung.md) und die [Längenredaktion dreier Mini-Prompts](mini-laengenredaktion.md) sind gesonderte redaktionelle Prüfungen ohne neue Primärquellenverifikation. Technische Struktur-, Workflow-, Paket- und Hashprüfungen ersetzen keine juristische Sachprüfung. In dieser Quellenrunde wurden **keine neuen Live-Modellläufe** durchgeführt; vorbereitete Auswertungsfälle bleiben von tatsächlich beobachteten Modellergebnissen getrennt. Die Skillkonsolidierung und die Übernahme erhaltener Fachtexte erweitern den fachlichen Prüfstatus nicht.
