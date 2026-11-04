# Vorlagen und Vergleichsmaterial zu Insolvenztestakten

Die fallbezogenen Unterlagen stehen auf den jeweiligen Aktenseiten unter „Vorlagen und Vergleichsmaterial“. Bei der Anfechtung stehen eine ausfüllbare Word-Klagevorlage und ein internes PDF-Gutachten zur Verfügung. Die Planakten bieten die bearbeitbaren ODT-Blankos und fallbezogen ausgefüllte Word-Fassungen. Wo die Akte keine Bestätigungsreife belegt, zeigen diese Fassungen die noch offenen Voraussetzungen oder den historischen Stand.

## 1 Vorlagenquellen

- Die [Anfechtungsklage der Vorlagensammlung](../../docs/experimentell/vorlagensammlung-recht/insolvenzrecht/klage-insolvenzanfechtung/README.md) ist die Grundlage der Word-Vorlage. Die Fassung für die Testakten unterscheidet Geld- und Sachrückgewähr, die verschiedenen Anfechtungstatbestände sowie die stichtagsbezogenen Beweisangebote.
- Die Blankos übernehmen die bearbeitbaren Originale der [Insolvenzplanvorlage](../../docs/experimentell/vorlagensammlung-recht/insolvenzrecht/insolvenzplan-darstellender-und-gestaltender-teil/README.md) und der [StaRUG-Planvorlage](../../docs/experimentell/vorlagensammlung-recht/restrukturierungsrecht-starug/restrukturierungsplan-starug/README.md). Die ausgefüllten Fassungen verwenden ihre Trennung in darstellenden und gestaltenden Teil und übertragen die für den Fall belegten Regelungen, Zahlen und Bedingungen.

## 2 Vergleich nach einem Testlauf

1. Laden Sie die Arbeitsakte und die passende Blankovorlage in die zu prüfende Anwendung. Geben Sie die Rolle und den gewünschten Stichtag vor. Halten Sie Modell, Promptfassung, Aktenstand und Datum des Laufs fest.
2. Bei einer Anfechtung lassen Sie jede Handlung mit Datum und Empfänger erfassen. Vergleichen Sie danach die Würdigung der Benachteiligung, der Zahlungsunfähigkeit, des Schuldnervorsatzes und der Gegnerkenntnis mit dem internen Gutachten. Prüfen Sie die benannten Anlagen im Original. Achten Sie bei abweichenden Ergebnissen darauf, ob die Anwendung den konkreten Gegenbeleg oder nur eine allgemeine Regel nennt.
3. Bei einem Plan vergleichen Sie die vorgeschlagene Rechtsgestaltung je Gruppe und Gläubiger. Rechnen Sie Zahlungszeitpunkt, Quote, Ausfall, Vergleichsszenario, Stimmrechte und Planfinanzierung nach. Unterscheiden Sie zwischen einer nachgewiesenen Bedingung, einer Annahme und einem tatsächlich eingetretenen Planereignis.
4. Wiederholen Sie den Lauf nach einer Änderung der Akte oder der Anwendung mit derselben Aufgabenstellung. Dokumentieren Sie Abweichungen mit der betreffenden Datei, Fundstelle und dem Grund. Das Vergleichsmaterial hilft bei der Gegenprüfung und ersetzt die Würdigung der Originale nicht.

## 3 Pflege und automatische Prüfung

Der Workflow „Insolvenztestakten und Vergleichsmaterial“ prüft bei Änderungen und auf manuellen Aufruf den Dateibestand, die Verweise, die Trennung von Arbeitsakten-Exporten und Vergleichsmaterial sowie die Prüfsummen der nativen Aktenunterlagen. Ein geänderter Aktenstand verlangt eine fachliche Gegenlese und gegebenenfalls neue Fassungen. Der technische Check bewertet keine rechtliche Schlussfolgerung.

Nach dem fachlichen Abgleich werden die Ausgaben mit `python3 scripts/insolvenz-testakten-material.py --build` gesetzt. Ohne `--build` prüft der Befehl den hinterlegten Stand. Die Ausgaben verwenden dieselben Quellen wie der [Bestandsnachweis](bestand.json).

## 4 Akten mit Vergleichsmaterial

| Akte | Anfechtung | Pläne |
| --- | --- | --- |
| [Akte: Bereicherungs-Dreiecksverhältnis / Doppelverkauf Oldtimer Bischof-Hellberg / Bonn](../../testakten/bereicherung-dreiecksverhaeltnis-doppelverkauf-oldtimer-bischof-bonn/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [<!-- decimal-headings -->](../../testakten/fintech-darlehen-vertragsuebernahme-bremen/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Vellnitz Kunststofftechnik — Bargeschäft und Vorkasse beim Rohstofflieferanten (Chemnitz)](../../testakten/insolvenzanfechtung-bargeschaeft-vorkasse-rohstofflieferant-chemnitz/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [1. Blechliebe und die letzte Stahllieferung](../../testakten/insolvenzanfechtung-blechliebe-bamberg/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [1. Faltenwurf zwischen Familie und Werkstatt](../../testakten/insolvenzanfechtung-faltenwurf-fuerth/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung — Gesellschafterdarlehen im Konzern-Cash-Pool (Regensburg)](../../testakten/insolvenzanfechtung-gesellschafterdarlehen-cash-pool-regensburg/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Vondering Metallform — Grundstücksverkauf und „Vermittlungsprovision" (Mönchengladbach)](../../testakten/insolvenzanfechtung-glaeubigerbenachteiligung-grundstuecksverkauf-moenchengladbach/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung — Warenlager an Erfüllungs statt an den Hauptlieferanten (Kassel)](../../testakten/insolvenzanfechtung-inkongruente-deckung-warenlager-an-erfuellungs-statt-kassel/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung — Inkongrünte Deckung durch Zwangsvollstreckung (Fürth)](../../testakten/insolvenzanfechtung-inkongruente-deckung-zwangsvollstreckung-fuerth/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Kiezflitzer — Gesellschafterdarlehen, Beraterhonorar und Vorschuss (Berlin)](../../testakten/insolvenzanfechtung-kiezflitzer-gesellschafterdarlehen-berlin/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Trave Clean — Beitragszahlung an die Krankenkasse nach Fremdantrag (Lübeck)](../../testakten/insolvenzanfechtung-kongruente-deckung-krankenkasse-nach-antrag-luebeck/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Teutoburger Möbelwerk — kongrünte Deckung, Mahnlauf und Kenntnisfrage (Bielefeld)](../../testakten/insolvenzanfechtung-kongruente-deckung-lieferant-mahnlauf-bielefeld/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Domblick Weinkellerei — Kontokorrent-Rückführung nach Linienherabsetzung (Mainz)](../../testakten/insolvenzanfechtung-kontokorrent-rueckfuehrung-kreditlinie-mainz/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Ruhrland Getränkegroßhandel — Kontokorrent-Verrechnungen bei geduldeter Überziehung (Dortmund)](../../testakten/insolvenzanfechtung-kontokorrent-verrechnungen-geduldete-ueberziehung-dortmund/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung Schenkung Familie — Hollmann Bau- und Sanierungs GmbH (Oldenburg)](../../testakten/insolvenzanfechtung-schenkung-familie-oldenburg/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Insolvenzanfechtung aufsteigende Konzernsicherheit — Feinwerk Präzisionswerkzeuge GmbH (Stuttgart)](../../testakten/insolvenzanfechtung-unentgeltlich-konzernsicherheit-upstream-stuttgart/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [1. Testakte VeedelWende: klare Darlehensrückzahlung an den 25-Prozent-Gesellschafter](../../testakten/insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [1. Testakte VeedelWende: alte Abtretung eines Gesellschafterdarlehens an einen Dritten](../../testakten/insolvenzanfechtung-veedelwende-zession-koeln/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Vorsatzanfechtung gegen das Finanzamt — 30 Raten im Vierjahreszeitraum (Augsburg)](../../testakten/insolvenzanfechtung-vorsatzanfechtung-finanzamt-ratenzahlung-augsburg/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Akte: Metallbau Hansa GmbH – Insolvenzplan und StaRUG-Restrukturierung](../../testakten/insolvenzplan-starug-planwerkstatt-metallbau-hansa/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | 2 |
| [MedTech Jena: Eigenverwaltung, Schutzschirm und Liquiditätsstatus](../../testakten/insolvenzrecht-eigenverwaltung-schutzschirm-medtech-jena/README.md#vorlagen-und-vergleichsmaterial) | – | 1 |
| [Forderungsprüfung Berlin: Mietkaution, Aufrechnung und Absonderungsrechte](../../testakten/insolvenzrecht-forderungspruefung-mietkaution-berlin/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Testakte: Mainbogen Laborsoftware GmbH](../../testakten/insolvenzverwaltung-mainbogen-laborsoftware-wuerzburg/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Akte Insolvenzverwaltung – Möbelwerk Havelberg GmbH](../../testakten/insolvenzverwaltung-moebelwerk-havelberg-regelverfahren/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | 1 |
| [Akte: Insolvenzverwaltung Nordlicht Handels GmbH](../../testakten/insolvenzverwaltung-nordlicht-handels-kiel/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | – |
| [Akte: Krisenfrüherkennung & StaRUG – Vier Varianten](../../testakten/krisenfrueherkennung-starug-vier-varianten/README.md#vorlagen-und-vergleichsmaterial) | – | 3 |
| [Sanierungsgewinn im Insolvenzplan — Grossbach Druckguss & Präzision GmbH & Co. KG Erfurt (2026)](../../testakten/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026/README.md#vorlagen-und-vergleichsmaterial) | – | 1 |
| [Sanierungsgewinn im StaRUG-Plan — Pellbach Windenergie GmbH Brandenburg (2026)](../../testakten/sanierungsgewinn-starug-plan-windenergie-pellbach-2026/README.md#vorlagen-und-vergleichsmaterial) | – | 1 |
| [Testakte: StaRUG-Aufhebung der Restrukturierungssache — Holding Düsseldorf (BGH IX ZB 18/25)](../../testakten/starug-aufhebung-holding-duesseldorf-ix-zb-18-25/README.md#vorlagen-und-vergleichsmaterial) | – | 1 |
| [Großbach Druckguss & Präzision GmbH & Co. KG — Schutzschirm und StaRUG-Optionen](../../testakten/starug-schutzschirm-grossbach-druckguss-erfurt/README.md#vorlagen-und-vergleichsmaterial) | Vorlage und Gutachten | 1 |
