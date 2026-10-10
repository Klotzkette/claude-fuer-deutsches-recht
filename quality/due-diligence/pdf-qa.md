# DD – Due Diligence: PDF-Sichtprüfung

## 1. Prüfstand und Reichweite

Geprüft am 10. Oktober 2026: die sechs PDF-Dateien aus dem lokalen Release-Build `/tmp/dd-release-dist`, erstellt zwischen 19:07:24 und 19:07:59 Uhr Europe/Berlin. Die Prüfung umfasst 680 Seiten. Sie ist eine technische Vollprüfung der extrahierbaren Textspans mit begrenzter visueller Stichprobe, keine juristische Inhaltsfreigabe und kein vollständiges visuelles Durchlesen aller Seiten.

Die Werkstattfassung hatte zum Prüfzeitpunkt 15 Seiten. Ein angekündigter Neubau wegen der Überschriftenhierarchie ist von diesem Erstbefund nicht erfasst. Auch ein nachträglich erneuerter Bankaktenexport muss gesondert nachgeprüft werden. Die unten dokumentierten Hashes grenzen den tatsächlich geprüften Stand ab.

Verwendet wurden PyMuPDF über `fitz`, die vorhandene Python-Laufzeit und die vorhandenen Abhängigkeiten; es wurde nichts installiert. Die Quelldateien, Testakten und PDF-Builder wurden bei dieser Prüfung nicht geändert.

## 2. Prüfverfahren

Auf jeder Seite wurden die Bounding-Boxes sämtlicher nicht leerer Textspans gegen die MediaBox geprüft; die Toleranz betrug einen Punkt. Bei allen Seiten entsprachen die Seitenrechtecke der MediaBox, ohne Seitenrotation. Zusätzlich wurden textleere Seiten, Vorkommen des Unicode-Ersatzzeichens U+FFFD beziehungsweise des schwarzen Quadrats U+25A0 sowie Textspans mit einer Schriftgröße unter sieben Punkten erfasst.

Diese Zeichenprüfung erkennt zwei häufige Fehlersignaturen. Sie beweist weder die Vollständigkeit aller Glyphen noch die richtige Wiedergabe jedes Sonderzeichens. Die Bounding-Box-Prüfung erfasst Text; sie ersetzt keine flächendeckende Sichtkontrolle von Bildern, Linien oder sich überlagernden Objekten. Kleine Fußzeilen wurden nicht mit winzigen Datentabellen gleichgesetzt.

Vier Seiten wurden gerendert und tatsächlich visuell angesehen: Berlin Seite 5, Silberfalke Seiten 122 und 186 sowie Erfurt Seite 17. Die vier PNG-Stichproben beanspruchten zusammen rund 335 KB; es wurde kein großer Bildexport angelegt.

## 3. Technische Ergebnisse

Alle sechs geprüften PDF-Dateien enthalten **keinen Textspan außerhalb der MediaBox** und **keines der beiden gesuchten Ersatzzeichen**.

| PDF | Seiten | Textleere Seiten | Kleine Schrift |
| --- | ---: | --- | --- |
| `dd-arbeitsvertraege-innovation-berlin_gesamt.pdf` | 296 | Keine | Minimum 8 pt; keine Spans unter 7 pt |
| `dd-corporate-silberfalke_gesamt.pdf` | 197 | Seite 122 | Minimum 8 pt; keine Spans unter 7 pt |
| `dd-bankfiliale-verbraucherdarlehen-erfurt_gesamt.pdf` | 167 | Keine | Minimum rund 4,498 pt; 14.352 Spans unter 7 pt |
| `due-diligence-werkstatt.pdf` | 15 | Keine | Minimum 8 pt; keine Spans unter 7 pt |
| `due-diligence-schnellstart.pdf` | 2 | Keine | Minimum 8 pt; keine Spans unter 7 pt |
| `due-diligence-hauptproblem.pdf` | 3 | Keine | Minimum 8 pt; keine Spans unter 7 pt |

## 4. Visuelle Stichproben und Einzelfunde

### 4.1. Berlin: Arbeitsvertrag

Seite 5 zeigt den Beginn des Arbeitsvertrags P002 für Alexander Meyer. Fließtext und nummerierte Überschriften sind gut lesbar, die Ränder frei und die Fußzeile eindeutig. In dieser Stichprobe waren keine abgeschnittenen Textteile, Überlagerungen oder auffällig kleinen Tabellen erkennbar. Die Seite setzt sich im nächsten Vertragsblatt fort; die Sichtprüfung bewertet die Darstellung, nicht die rechtliche Richtigkeit der bewusst prüfbedürftigen Vertragsklauseln.

### 4.2. Silberfalke: Finanzunterlage

Seite 186 zeigt die Dreiwochen-Liquiditätsvorschau der Delta Service GmbH. Tabellenbeschriftungen und Geldbeträge sind in dieser Stichprobe gut lesbar; Tabellenränder und Spalten bleiben innerhalb der Seite. Die Fortsetzung der Tabelle ist kein Abschneiden. Aus der lesbaren Darstellung folgt keine Bestätigung der Berechnung oder der zugrunde liegenden Verkäuferangaben.

### 4.3. Silberfalke: übernommene Leerseite

Seite 122 enthält lediglich eine blaue horizontale Linie und keinen Sachtext. Sie ist durch die PDF-Lesezeichen eindeutig der Schlussseite von `09_spa_markup_disclosure/spa_auszug_key_provisions.docx` zugeordnet: Dieser Dokumentteil beginnt auf Seite 120; die folgende Quelle `spa_key_issues.docx` beginnt auf Seite 123.

Die schreibgeschützt gelesene DOCX-Struktur endet nach dem letzten Sachabsatz mit einem leeren Absatz, einem Absatz mit blauem unteren Rahmen und einem Absatz mit einem Leerzeichen. Die zusätzliche PDF-Seite ist damit als übernommenes Umbruchartefakt erklärbar. Eine absichtliche Leerseitenfunktion ist aus der Quelle nicht belegt. Die inhaltlich unveränderte Spiegelung der historischen Testakte wurde deshalb nicht bearbeitet. Befund: kosmetische Leerseite, kein nachgewiesener Textverlust.

### 4.4. Erfurt: Nachbesserung der Tabellen erforderlich

Die Schriftgrößenauffälligkeiten konzentrieren sich auf die Seiten 17 bis 44. Die visuell geprüfte Seite 17 enthält einen sehr breiten Loan-Tape-Auszug mit elf Spalten auf A4 quer. Namen, Statusangaben und Quellenverweise sind bei normaler Seitengröße erheblich zu klein. Die technische Einhaltung der Seitengrenzen genügt hier nicht für eine gut lesbare Druckfassung.

Dieser Bankaktenexport ist hinsichtlich der Tabellendarstellung **nachzubessern**. Geeignet sind mehrere lesbare Spaltengruppen mit durchgehend sichtbarer Kreditkennung und eindeutiger Zuordnung zur ungekürzten Excel-Datei. Die übrigen Daten dürfen dabei nicht entfallen. Der angekündigte neue Export wird von diesem Erstbefund noch nicht freigegeben; insbesondere sind Seitenzahl, Schriftgrößen und repräsentative Tabellen danach erneut zu prüfen.

## 5. Abgrenzung der geprüften Fassungen

| Datei | SHA-256 |
| --- | --- |
| `dd-arbeitsvertraege-innovation-berlin_gesamt.pdf` | `38d032a09da9b2b79ecebcae4d48ae4f9f60f4b7997034805745e8c649dc8850` |
| `dd-corporate-silberfalke_gesamt.pdf` | `d4a722c69fd9f7a8789b24d6f17594fdbba0c5f5eaa2b1cb5970cc5dcebe9794` |
| `dd-bankfiliale-verbraucherdarlehen-erfurt_gesamt.pdf` | `887e9fb49fb23bb0991e860c8e30ae961bb23f6267e39e49bfc0f9263802178f` |
| `due-diligence-werkstatt.pdf` | `be114f8c17da6619ede955cb9db4d5fc344f6045070e7ded79838a01a54de4c5` |
| `due-diligence-schnellstart.pdf` | `20b11630d894ba66e2a96e79db0661f2682bcc35d4bed397145b7ed6529816c5` |
| `due-diligence-hauptproblem.pdf` | `30199e0f310cb88f69369362eeeca4be3f5e92b11590f94f915768c455630bb4` |

## 6. Ergebnis und verbleibende Grenzen

Für Berlin, Silberfalke und die geprüften Promptfassungen ergab die technische Textprüfung keine Seitenüberläufe oder gesuchten Ersatzzeichen. Die zwei inhaltstragenden visuellen Stichproben aus Berlin und Silberfalke sind gut lesbar. Die kosmetische Silberfalke-Leerseite bleibt dokumentiert. Für die Bankakte besteht ein konkreter Lesbarkeitsmangel der Tabellen; für einen erneuerten Werkstattexport steht die Folgeprüfung aus.

Nicht behauptet werden eine Sichtprüfung sämtlicher 680 Seiten, eine vollständige Fontprüfung, ein Vergleich jedes PDF-Inhalts mit jedem Quelldokument, eine juristische Freigabe oder ein externer Modelltest. Die Originaldateien bleiben die bearbeitbaren Arbeitsunterlagen; der PDF-Export ist ihre Lesefassung.

## 7. Umgang mit erneuerten Exporten

Die Abschnitte 1 bis 6 dokumentieren den Erstbefund und werden durch spätere Exporte nicht rückwirkend umgeschrieben. Für eine geänderte Datei gilt ausschließlich der Nachtrag mit ihrem jeweiligen Hash. Unveränderte Dateien behalten den oben bezeichneten Prüfstand. Ein bestandener geometrischer Nachtest ersetzt auch beim Neubau keine vollständige visuelle Durchsicht.

## 8. Nachtrag: endgültige Werkstatt-Lesefassung

Am 10. Oktober 2026 wurde die neu gesetzte Datei `/tmp/dd-release-final/due-diligence-werkstatt.pdf` nachgeprüft. Sie umfasst weiterhin 15 Seiten. Ihr SHA-256 lautet `f592d6bcc52b6ea8de5260b1e28666fe514553f5de55018e3745dba2af7ceffe`. Dieser Nachtrag ersetzt den offenen Werkstatt-Nachprüfvermerk aus den Abschnitten 1 und 6 für genau diese Datei.

Auf allen 15 Seiten wurden sämtliche nicht leeren Textspans erneut gegen die MediaBox geprüft: keine Überschreitungen bei einem Punkt Toleranz, keine textleeren Seiten, keine Vorkommen von U+FFFD oder U+25A0. Die kleinste ermittelte Schriftgröße beträgt acht Punkte; kein Textspan liegt unter sieben Punkten.

Seite 1 wurde zusätzlich gerendert und tatsächlich visuell angesehen. Der Haupttitel, die nummerierten Hauptabschnitte und die Unterabschnitte sind unterscheidbar, der Fließtext ist lesbar, die Fußzeile bleibt frei, und in dieser Stichprobe sind keine abgeschnittenen Zeichen oder Überlagerungen erkennbar. Die Unterüberschrift 2.2 steht am Seitenende und ihr Text setzt auf der nächsten Seite fort; dies ist ein kosmetischer Umbruch, kein nachgewiesener Inhaltsverlust. Die zusätzliche Sichtprobe benötigt rund 130 KB und bleibt zusammen mit den bisherigen Stichproben unter zwei MB.

Die Nachprüfung bestätigt damit die unauffällige Textgeometrie und die Lesbarkeit der geprüften Titelseite. Sie bestätigt keine Sichtprüfung der übrigen 14 Seiten. Der Bankakten-Neuexport bleibt bis zu seinem gesonderten Nachtrag offen.

## 9. Abschlussnachtrag: Banktabellen und Werkstattumbruch

Am 10. Oktober 2026 wurden die folgenden abschließenden Dateien aus `/tmp/dd-release-publish` erneut geprüft. Die Hashes in diesem Abschnitt ersetzen für diese beiden Dateien die früheren Hashes und offenen Nachprüfvermerke.

| Datei | Seiten | SHA-256 |
| --- | ---: | --- |
| `dd-bankfiliale-verbraucherdarlehen-erfurt_gesamt.pdf` | 349 | `2025402dd790ab0186ba5b9dc8b1f9bd6142fafac884ebe16cca4de9b0da53bc` |
| `due-diligence-werkstatt.pdf` | 15 | `b33c8189569b4e2b6941888fa088376d36dea3541e90f6f9a9a8f902e280d006` |

Auf sämtlichen 364 Seiten beider Dateien wurden die nicht leeren Textspans erneut gegen die MediaBox geprüft. Ergebnis: keine Überschreitungen bei einem Punkt Toleranz, keine textleeren Seiten, keine Vorkommen von U+FFFD oder U+25A0 und keine Textspans unter sieben Punkten. Die kleinste Schriftgröße beider Gesamtdokumente beträgt acht Punkte; dies schließt Fußzeilen anderer Dokumentteile ein.

Der neu gesetzte Excel-Druckteil der Bankakte erstreckt sich über die Gesamtseiten 16 bis 226, also 211 Seiten. Dort wurden ausschließlich Schriftgrößen von neun, elf und sechzehn Punkten ermittelt. Die Textdaten der Tabellen stehen mit elf Punkten zur Verfügung; die neun Punkte betreffen die Fußzeilen. Der zuvor ermittelte Tabellen-Minimalwert von rund 4,498 Punkten tritt in der neuen Fassung nicht mehr auf.

Drei Spaltengruppen wurden gerendert und tatsächlich visuell angesehen: Gesamtseite 18 zeigt Identität und Saldo, Seite 101 Verkäuferpreis, Status und Herkunft, Seite 201 die Aufteilung der Zahlung auf Kapital, Zinsen und Kosten. Alle drei Stichproben sind bei normaler Seitengröße gut lesbar. Die Darlehenskennung wird als erste Spalte wiederholt, sodass die getrennten Spaltengruppen zugeordnet werden können. In diesen Stichproben waren keine abgeschnittenen Inhalte, Überlagerungen oder zu eng gesetzten Werte sichtbar. **Der konkrete Lesbarkeitsmangel aus Abschnitt 4.4 ist damit in der abschließenden Bankfassung behoben.** Ein vollständiger inhaltlicher Zellenvergleich zwischen XLSX und PDF ist nicht Gegenstand dieser Sichtprüfung.

Die zweite Seite der abschließenden Werkstattfassung wurde zusätzlich gerendert und tatsächlich angesehen. Unterüberschrift 2.2 steht nun gemeinsam mit ihrem ersten Absatz am Seitenanfang. Der in Abschnitt 8 dokumentierte kosmetische Umbruch wurde damit behoben. Die weitere Überschriftenhierarchie und die Textdarstellung sind in dieser Stichprobe lesbar und ohne Überlagerungen.

Die Prüfung ist für diese beiden konkreten Dateien abgeschlossen. Die historischen Erstbefunde bleiben nachvollziehbar; die unverändert übernommene kosmetische Silberfalke-Leerseite bleibt als einzige dort dokumentierte Layoutbesonderheit bestehen. Die Grenzen der visuellen Stichprobe, Fontprüfung und juristischen Inhaltsprüfung aus Abschnitt 6 gelten weiter. Keine Quelldateien oder Builder wurden im Rahmen dieser Nachkontrolle geändert; sämtliche temporären Sichtproben bleiben zusammen unter zwei MB.

## 10. Nachprüfung der Importkorrektur 1.0.1

Am 10.10.2026 nach Neubau geprüft: Alle drei Gesamt-PDFs sind bytegleich mit 1.0.0. Die drei Prompt-PDFs unterscheiden sich durch die neue Versionsfußzeile; Seitenzahlen, Textbestand, Seitengrenzen und geprüfte Ersatzzeichen wurden erneut kontrolliert. Die erste Werkstattseite wurde einschließlich Fußzeile visuell gelesen. Die aktuellen Hashes stehen in `lesefassungen.json`.
