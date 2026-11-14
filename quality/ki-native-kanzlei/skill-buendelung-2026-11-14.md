# 1. KI-native Kanzlei: Arbeitswege und erhaltene Fachmodule

Stand: 14. November 2026. Komponentenfassung `445.36.0`. Dies ist eine Struktur-, Runtime-, Paket- und PDF-Prüfung. Die bisherigen rechtlichen Quellenstände und offenen Grenzen bleiben erhalten; keine erneute Volltextprüfung der Rechtsprechung, kein tatsächlicher Modelllauf und keine Veröffentlichung werden behauptet.

## 1.1. Vollständiger Inhalt bei kompakter Auswahl

Das installierte Plugin hat acht aktive Arbeitswege einschließlich des Hauptskills. Alle dreißig bisherigen Fachmodule bleiben vollständig lesbar. Die Resolver lesen ausschließlich vorhandene oder ausdrücklich registrierte Fachtexte; kurze Router ersetzen keine langen Fachinhalte. Alte Fachnamen werden nicht wieder als zusätzliche aktive Skills angelegt.

Der Mandatslauf verwendet eine mit dem Plugin ausgelieferte Zuordnung. Er nennt den aktiven nächsten Skill sowie Fachmodul und Fachtextpfad getrennt. Mandatsakten behalten ihre bisherigen Modulkennungen. Fristenpriorität, benannte Verantwortliche, gebundene Fassungen und Freigaben werden nicht verändert. Ein isolierter Pluginlauf ohne Repository sowie eine fehlende Zuordnungsdatei sind getestet.

## 1.2. Tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| Mandatslauf einschließlich Freigabebindung | 30 Tests bestanden |
| Produktionsrouten, isoliertes Plugin, fehlendes Mapping und Originalakten | 8 Tests bestanden |
| Kanzleistart und Posteingang | 5 Tests bestanden |
| Umfangsvertrag: fehlende/duplizierte/verkürzte Module, falsche Version oder aktive Auswahl | 6 Tests bestanden |
| Arbeitszeugnisprüfung mit sämtlichen 31 ursprünglichen Fachtexten | 13 Tests bestanden |
| Kanzlei-Quellprüfung | Acht aktive Skills, dreißig vollständige Fachmodule, Promptpaare, Frontmatter, Gliederung, lokale Links, Versionsdaten und Quellhashes bestanden |
| Komponentenpaket | Flaches und portables Plugin quellidentisch; PDF-Seitenzahlen, Quelle-/PDF-Hashes, identisches ZIP-Manifest und Asset-Prüfsummen bestanden |
| Originalerhaltung | Alle 240 Aktenoriginale stimmen mit dem unveränderten Tag `si-native-kanzlei-v445.33.3` überein |

Das sind 62 lokale Unit-Tests plus Quellen- und Paketprüfungen. [Prüfprotokoll und genaue Befehle](skill-buendelung-2026-11-14/pruefung.json), [Testlogs](skill-buendelung-2026-11-14/logs/), [Quellbericht](struktur-pruefung.json), [Paketbericht](paket-pruefung.json).

Nach der abschließenden README-Leerzeilenbereinigung wurden Komponentenpaket, Quellen- und Paketprüfung nochmals gegen den endgültigen README-Hash ausgeführt. Die Berichte oben stammen aus diesem letzten Build; ihre vorherigen Fassungen sind im [gesonderten Nachweis](skill-buendelung-2026-11-14/final-readme/pruefung.json) gesichert. PDF und Einzel-PDF-ZIP blieben bytegleich. Dieser dokumentarische Nachlauf enthält keinen neuen PDF-Satz und keine zusätzliche Modell-, Rechtsquellen- oder Sichtprüfung; die 62 Unit-Tests werden dadurch nicht als nochmals ausgeführt gezählt.

Beim Arbeitszeugnis prüft der Test kurze, tatsächlich gleichwertige Formulierungen statt einen einzigen Satzwortlaut. Die Pflicht zur Erstlektüre, der Start ohne Zusatzformel, die HR-Abgrenzung und das Verbot vorgeschalteter Statusblöcke bleiben abgesichert. Ein zusätzlicher Negativtest verwirft partielle oder umgekehrte Statusverbote. Die Größenprüfung verwendet dieselbe inklusive Grenze von 7.500 Bytes wie die übrigen Kurzpromptprüfungen. Kein Prompt wurde dafür abgeschwächt.

## 1.3. PDF-Neusatz und Auslieferungsdateien

Der Builder hat mit den vorhandenen vier Times-New-Roman-TTFs dreißig vollständige Modul-PDFs erzeugt: insgesamt 322 Fachtextseiten. Eine neue Übersichtsseite erläutert acht aktive Arbeitswege, Fachmodule und Komponentenfassung. Das Handbuch umfasst 323 tatsächliche A4-Seiten. Die bisherigen modulspezifischen Mindestumfänge bleiben Prüfbedingung.

Alle erzeugten Textabsätze und Tabellenzellen wurden in ihrer Reihenfolge gegen die PDF-Extraktion geprüft. Die finale Übersicht und eine Fachtextseite wurden visuell angesehen; alle dreißig Modul-PDFs sind mit dem vorangegangenen visuell beprobten Satz byteidentisch. Eine Sichtprüfung aller 323 Seiten wird nicht behauptet. [Builderprotokoll](skill-buendelung-2026-11-14/pdf-build.log) und [Umfang, Quellen und Hashes](umfang.json).

Die neue [Handbuchfassung](../../docs/handbuecher/ki-native-kanzlei-v445.36.0/ki-native-kanzlei-skills-handbuch.pdf) und das [ZIP mit allen Modul-PDFs](../../docs/handbuecher/ki-native-kanzlei-v445.36.0/ki-native-kanzlei-skills-einzelpdfs.zip) liegen versioniert neben den erhaltenen älteren Artefakten. Das ZIP enthält genau dreißig PDFs, README und denselben Umfangsbericht. Der zentrale Releasebuilder prüft die tatsächlichen Quellen, aktiven Skills, Seiten und Prüfsummen vor Übernahme der beiden Dateien. Die früheren Berichte bleiben unter [previous](skill-buendelung-2026-11-14/previous/) erhalten.
