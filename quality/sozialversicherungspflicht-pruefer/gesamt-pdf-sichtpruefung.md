# Ergänzende visuelle Prüfung der Gesamtakten

## 1. Ergebnis

Prüfdatum: 30. September 2026. In den nachfolgend bezeichneten 23 Kontaktbögen mit sämtlichen 244 Seiten der fünf Nicht-AG-Gesamtakten wurden keine sichtbaren überlagerten oder am Seitenrand abgeschnittenen Inhalte festgestellt. Zusätzlich wurden fünf EML-/CSV-Inhaltsseiten, je eine pro Akte, einzeln in ihrer vorhandenen Auflösung von 1.132 × 1.600 Pixeln geöffnet und visuell geprüft. Auch dort zeigte sich kein solcher Fehler.

Dies ist eine ergänzende visuelle Sichtprüfung mit ausdrücklich begrenztem Umfang. Sie ist weder eine algorithmische Bounding-Box-Prüfung noch eine Behauptung, jede der 244 Seiten einzeln in voller Auflösung gelesen zu haben.

## 2. Persönlich geprüfter Umfang

Grundlage ist `qa-local/combined-qa/manifest.json`. Die folgenden Kontaktbögen wurden tatsächlich als Bilder geöffnet und betrachtet. Pfade in der Tabelle sind relativ zum Verzeichnis `combined-qa/`.

| Akte / Unterverzeichnis | Kontaktbögen | Abgedeckte Gesamt-PDF-Seiten | Zusätzlich einzeln geöffnete Inhaltsseite |
| --- | --- | --- | --- |
| `sozialversicherung-gmbh-fuenfzig-prozent-erfurt` | `contact-1.png` bis `contact-5.png` | 1–51 | `page-14.png`: CSV `25_Zahlungen_2026.csv` |
| `sozialversicherung-gmbh-zwanzig-prozent-berlin` | `contact-1.png` bis `contact-5.png` | 1–51 | `page-04.png`: EML `01_Auftrag_20260929.eml` |
| `sozialversicherung-musikakademie-prenzlauer-berg` | `contact-1.png` bis `contact-4.png` | 1–45 | `page-12.png`: CSV `26_Honorarkonto_2025.csv` |
| `sozialversicherung-programmierer-leipzig` | `contact-1.png` bis `contact-4.png` | 1–45 | `page-12.png`: CSV `26_Stunden_und_Rechnungen_2025.csv` |
| `sozialversicherung-syndikus-versorgungswerk-hamburg` | `contact-1.png` bis `contact-5.png` | 1–52 | `page-02.png`: EML `01_Mila_an_Kanzlei.eml` |

Geprüft wurden sichtbare Seitenränder, abgeschnittene Textblöcke, Überlagerungen zwischen Text und Tabellen, lesbare Tabellenzellen in den fünf Vollseiten sowie das Verhältnis von Inhalt und Fußzeile. Die Gesamtdokumente enthalten erwartete Trennseiten vor Originaldateien. Unterschiedliche Originalseitenformate und nur teilweise gefüllte Folgeseiten wurden nicht als Clipping gewertet.

Die CSV-Spaltenüberschriften und lange Wörter in schmalen Zellen werden teilweise innerhalb des Wortes umbrochen, zum Beispiel in der Musik- und Programmiererakte. In den geöffneten Vollseiten bleiben die Zeichen sichtbar, die Zeilen innerhalb ihrer Zellen und die Geldbeträge vollständig; es handelt sich im geprüften Umfang um einen Umbruch, nicht um abgeschnittenen Inhalt.

## 3. Abgrenzung zu anderen Prüfungen und Fassungen

Die fünf Kontaktbögen der AG-Organe-Akte Hannover wurden nach Mitteilung der Hauptbearbeitung bereits durch diese geprüft. Sie wurden von diesem Prüfagenten nicht nochmals geöffnet und zählen nicht zu den hier ausgewiesenen 23 Bögen. Ebenso wird die bereits durch andere Bearbeiter durchgeführte vollständige Einzelprüfung nativer Word-/PDF-Originale nicht als eigene Leistung dieses Berichts bezeichnet.

Die hier geöffneten Gesamt-PDF-Kontaktbögen enthalten bei Erfurt `06_Geschaeftsfuehrer_Anstellungsvertrag.docx` und Musik `03_Unterrichtsbetrieb_September_2025.docx` den Stand vor den abschließenden inhaltlichen Korrekturen. Deren aktuelle Fassungen werden separat neu gerendert und geprüft. Die aktuelle Musikdatei wurde durch diesen Prüfagenten textlich und rechnerisch nachgeprüft; die Schließung des ursprünglichen Befunds ist in Abschnitt 6 von `final-review.md` festgehalten. Die textliche Erfurt-Nachprüfung steht dort in Abschnitt 2.2. Dieser Kontaktbogenbericht ersetzt nicht die visuelle Prüfung jener neuen Fassungen und eines daraus neu gebauten Gesamt-PDFs.

Nicht durchgeführt wurden eine pixelgenaue Vollprüfung sämtlicher Seiten, algorithmische Layout-/Bounding-Box-Tests, ein neuer Renderlauf, native Tabellenneuberechnung oder eine neue Prüfung der publizierten ZIP- und Downloadbestände. Alle Befundaussagen beziehen sich auf die tatsächlich betrachteten Bilder. Es wurden keine Repositorydateien geändert; ausschließlich dieser Prüfbericht und der gesonderte fachliche Nachtrag wurden unter `qa-local/` geschrieben.
