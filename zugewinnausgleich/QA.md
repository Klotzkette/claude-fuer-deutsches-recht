# 1. Qualitätsprüfung des Plugins Zugewinnausgleich

Prüfstand: 22.09.2026. Version `444.8.0`. Dieser Nachweis betrifft ausschließlich das neue Spezialplugin und sein individuelles Prüfprofil. Die separate Familienakte, zentrale Generatoren, Paketierung und Veröffentlichung werden durch die übergeordnete Bearbeitung geprüft. Hier wurden keine Modellläufe durchgeführt.

## 1.1. Ausgeführte Strukturprüfungen

Die gezielte lokale Prüfung mit echtem YAML-Parser und JSON-Parser bestand. Genau zehn Skills sind vorhanden; jeder hat ausschließlich `name` und `description` im Frontmatter, einen zum Verzeichnis passenden ASCII-Slug von höchstens 64 Zeichen und sechs nummerierte Hauptabschnitte. Beschreibungen umfassen 167 bis 201 Zeichen und enthalten weder Ziffer-Komma-Ziffer noch spitze Klammern. Die Skilldateien umfassen 5.067 bis 8.511 UTF-8-Bytes und sind individuell fachlich ausgearbeitet.

Manifestname, Version `444.8.0`, Autor Klotzkette und ASCII-Beschreibung wurden geprüft. Eigene Markdown-Texte verwenden dezimale Überschriften, ausgeschriebenen Paragrafen, echte Umlaute und ß sowie den Ausgabehinweis Times New Roman 11 pt. Die lokale `references/zitierweise.md` ist eine byteidentische Kopie der Wurzelreferenz; deren bestehende Originalgliederung wird unverändert übernommen. Relative Inhaltslinks wurden auf vorhandene Ziele geprüft. Veröffentlichungslinks sind keine Behauptung bereits gebauter Release-Dateien.

## 1.2. Endgültige Promptgrößen und Hashes

| Datei | UTF-8-Bytes | SHA-256 |
| --- | --- | --- |
| `zugewinnausgleich-schnellstart.md` | 7.461 | `3c8c0279f7ec82ba0e2300d74524f6f7d9d8402b776a8e816e627e70184a03ec` |
| `zugewinnausgleich-hauptproblem.md` | 7.475 | `bcf53a03ab90b55ac1406c04cccfe10e913add4eb315708c4b75cd7a8e9319fc` |
| `zugewinnausgleich-werkstatt.md` | 23.757 | `70ee8b1386302a07c3302ce57cc75d6ad844ce3c74c6546d8eb2353b15dc9e78` |

Schnellstart und Hauptproblem bleiben jeweils unter 7.500 Bytes. Die Werkstatt liegt im gewünschten Bereich von etwa 16 bis 24 KB. Alle drei Prompts stehen außerhalb von `skills/`. Der korrespondierende Hauptskill `vermoegensbelege-bis-zur-gesamtberechnung` enthält eine eigene vollständige Rechenkette und ist kein Verweis-Wrapper. Sein Umfang beträgt 8.511 Bytes; für Skills gilt hier nicht die Grenze der beiden kompakten Prompts.

Die gemeinsame Zitierreferenz hat in Wurzel und Plugin denselben SHA-256-Wert: `134a0dd88187582587142f592497ca0d08f55a3d2b9b6dad8ccb91ea23ef7c9e`.

## 1.3. Fachliche Quellenprüfung

Das [Quellenregister](references/zugewinn-quellen.md) dokumentiert geprüfte BGB- und FamFG-Normen, Paragraf 254 ZPO, die Abgrenzung nach Paragraf 2 VersAusglG und amtliche Destatis-Indexdaten. Die drei verwendeten BGH-Entscheidungen wurden anhand unmittelbar abgerufener amtlicher PDFs gelesen:

- BGH, Beschluss vom 13.11.2024, Az. XII ZB 558/23, insbesondere Randnummern 17 bis 23: erfüllende Trennungsauskunft, abweichender tatsächlicher Trennungstag und Beweis statt bloßer Behauptung.
- BGH, Urteil vom 09.02.2011, Az. XII ZR 40/09, insbesondere Randnummern 16 bis 37 sowie 50 bis 58: Praxiswert, individueller Unternehmerlohn, latente Steuern, Doppelverwertung und Gesamtschuld.
- BGH, Beschluss vom 06.05.2015, Az. XII ZB 306/14, insbesondere Randnummern 19 bis 27: Abschmelzen und Wertanstieg eines Nießbrauchs, kein zusätzlicher negativer gleitender Erwerb.

Einige Web-Volltextabrufe waren gesperrt; die Verifikation erfolgte ergänzend durch erfolgreichen direkten Abruf der amtlichen PDFs und Textauswertung. Keine verwechselte Senatsbezeichnung „XIII“, keine ungeprüften weiteren Urteile und keine erfundenen Parallelfundstellen. Die Quellenprüfung behauptet keine Vollständigkeit der aktuellen Rechtsprechung. Konkrete Steuersätze, internationale Sonderfälle und historische Übergangslagen benötigen gegebenenfalls zusätzliche Recherche.

## 1.4. Individuelles Prüfprofil

Das neue [Profil](../quality/evals/zugewinnausgleich.json) folgt dem bestehenden Schema und enthält genau zehn kurze Ergebnisfälle, jeweils einen für jeden Skill, mit je drei fachlichen Kriterien. Zwei positive und zwei negative Auswahlbeispiele grenzen Gesamtberechnung von bloßem Versorgungsausgleich und pauschaler Erbquote ab. Die Fälle sind unabhängig von der Familienakte; alle benötigten Übungsdaten stehen im jeweiligen Auftrag.

`validate_profile` aus `scripts/quality_lab.py` wurde ausschließlich für dieses Profil aufgerufen und bestand. Fallzahl, Kriterienzahl, vollständige Zuordnung zu den zehn Skills, Auswahlbeispiele und die Hashes von Schnellstart und Werkstatt wurden zusätzlich abgeglichen. `mini_review` und `workshop_review` dokumentieren redaktionelle Prüfung und Überarbeitung, keine Ausführung der Fälle.

Geprüfte fachliche Soll-Ergebnisse umfassen 30.000 EUR aus der vollständigen Grundrechnung, vorzeichenrichtige negative Anfangswerte, den Sonderfall steigenden Nießbrauchs, 180.000 EUR Nettoimmobilienwert je Beteiligtem, 420.000 EUR Nettoanteilswert ohne doppelte Praxisbank, 146.000 EUR abgestimmten liquiden Bestand sowie die nichtlineare Wirkung der Anspruchsbegrenzung. Diese Soll-Ergebnisse sind Rechenprüfungen der vorbereiteten Fälle, keine gemessene Modellleistung.

## 1.5. Umfang und offene Grenzen

Der Umfang beruht auf tatsächlich verschiedenen Aufgaben: historische Rekonstruktion, Erwerbsprivilegierung, Immobilienfinanzierung, Unternehmensbewertung, Bestandsabgleich, Beweislast, Auskunft, Vergleich und gerichtliche Ausformulierung. Wiederholungen wurden für die Werkstatt gekürzt; fachliche Entscheidungen wurden nicht durch Fülltext ersetzt. Vorhandene Unterlagen kommen zuerst, Rückfragen betreffen entscheidende Lücken, Nachreichungen führen zur aktualisierten Endfassung. Generische Pflichtmatrizen und ungefragte Verfahren sind nicht vorgesehen.

Nicht ausgeführt wurden Verhaltenstests mit einem Modell. Die technische Integration und die separate Akte wurden anschließend wie nachfolgend beschrieben geprüft. Nach Änderungen an den Prompts sind Größen und Hashes erneut aus den tatsächlichen Bytes zu bestimmen. Ein bestandener Strukturtest garantiert weder automatische Skill-Auswahl noch ein inhaltlich fehlerfreies Ergebnis in jeder Arbeitsoberfläche.

## 1.6. Technische Integration und Familienakte

Plugin-Struktur, Marketplace-Import, YAML-Frontmatter, Laufzeitbudgets, Fachrouten und Schwerpunktabdeckung bestanden. Sämtliche vorhandenen `test-*.py`-Skripte wurden lokal ausgeführt; die neue Zugewinnprüfung enthält 16 Regressionen. Sie kontrolliert insbesondere Kontensalden, 47 Übertragspaare, Darlehensrechnung, Kryptoteilverkauf, Erbschaftsbelege, A4-Word-Dateien, Excel-Quellgleichheit und gespeicherte Formelergebnisse sowie die dezimale README-Gliederung mit stabilen Sprungzielen. Die zentralen Dokumentqualitäts-, CSV- und Downloadprüfungen bestanden ebenfalls. Die strikte Manifestprüfung mit der offiziellen Plugin-CLI bestand für das neue Plugin und den gesamten Marketplace; sie ersetzt keinen praktischen Modelltest.

Die Familienakte enthält 118 Quelldateien. Das Originalformat-ZIP wurde byteweise gegen diese Dateien und das Gesamt-PDF abgeglichen; einschließlich Hinweisdokument enthält es 120 Einträge. Das Einzel-PDF-ZIP enthält 118 PDFs sowie den vorgeschriebenen Hinweis als `README.txt`. Beide Archive haben keine Unterordner; Markdown und Bewertungsrubrik werden nicht ausgeliefert. Die PDFs selbst enthalten keinen Warnvorspruch. Kontoauszüge, Bildanlagen, Word-Seiten und Excel-Druckfassungen wurden gerendert und visuell kontrolliert.

Die unabhängige Konsistenzprüfung führte zur Korrektur des Datums der Nachlassbankauskunft und zur Vereinheitlichung des Grundschuldlöschungsvermerks von 2019. Im gemeinsamen PDF-Renderer werden kurze Felder breiter Tabellen nun platzsparender dargestellt, ohne Datensätze wegzulassen. Ein Regressionstest prüft Vollständigkeit und begrenzten Seitenumfang. Alle drei handbearbeiteten Prompts blieben beim abschließenden Generatorlauf byteidentisch.
