# 1. Zweck und führender Datenbestand

Die JSON-Datei ist die führende Fassung des Verzeichnisses. Excel dient der Bearbeitung definierter Sachfelder, Word der Lesefassung, HTML der lokalen Übersicht und XML dem dokumentierten Austausch. Die Dateien sind Momentaufnahmen eines bestimmten Registerstands. Die [Dateipflege](dateipflege.md) erläutert die tatsächlich implementierten Befehle und Importregeln des [Helfers](../scripts/vvt.py).

Das Schema ist eine eigene praktische Umsetzung von Register- und Pflegeanforderungen. Es ist kein amtliches Datenaustauschformat und kein Gesetzestext. Texte enthalten Kategorien, Zwecke und Quellenverweise. Personenbezogene Einzelakten, Zugangsdaten oder umfassende Kundenlisten werden nicht ohne sachliche Notwendigkeit eingebettet. Die technische Schemafreigabe bestätigt weder Wahrheit noch Rechtmäßigkeit eines Freitextfelds.

## 1.1. Registerebene

| Feld | Datentyp | Bedeutung |
|---|---|---|
| `schema_version` | Ganzzahl, aktuell 1 | Version des technischen Formats. |
| `register_id` | UUID als Text | Dauerhafte Identität dieses Registers. |
| `organization` | Objekt | Organisationsname, Kontakt, Vertreter und Datenschutzbeauftragter. |
| `revision` | Nichtnegative Ganzzahl | Stand des gesamten Registers; Änderungen und dokumentierte Prüfungen erhöhen ihn. |
| `updated_at` | Zeitangabe als Text | Letzter Bearbeitungsstand. |
| `activities` | Liste | Tätigkeitsdatensätze mit stabilen Kennungen. |
| `history` | Liste | Protokoll der Änderungen mit Anlass, Person und Vergleichsbezug. |

`organization` enthält genau die Textfelder `name`, `contact`, `representative` und `dpo`. Die Felder benennen tatsächliche Funktionen und Kontakte. Eine fehlende Benennung des Datenschutzbeauftragten wird nicht durch einen erfundenen Namen ausgefüllt; stattdessen wird der Stand beschrieben. Das Vertreterfeld betrifft gegebenenfalls den datenschutzrechtlichen Vertreter und ist nicht bloß eine Wiederholung irgendeiner internen Abwesenheitsvertretung.

Organisationsänderungen werden mit `update-org` durchgeführt. Ein geänderter Organisationskontext öffnet im Helfer die vorhandenen Prüfentscheidungen erneut. Diese konservative technische Behandlung bedeutet nicht, dass jeder Kontaktwechsel rechtlich eine vollständige neue DSFA erfordert. Die fachlich zuständige Person bestimmt den tatsächlich erforderlichen Umfang.

## 1.2. Tätigkeitsidentität und Status

| Feld | Werte | Bedeutung |
|---|---|---|
| `id` | `VT-` mit 4 bis 8 Ziffern | Dauerhafte Tätigkeitskennung, beispielsweise `VT-0001`. |
| `activity_revision` | Positive Ganzzahl im gespeicherten Datensatz | Revisionsstand der Tätigkeit. |
| `role` | `controller` oder `processor` | Verantwortlicher oder Auftragsverarbeiter für diesen Vorgang. |
| `status` | `geplant`, `aktiv`, `pausiert`, `beendet` | Tatsächlicher Betriebsstand; keine rechtliche Freigabe. |

Eine neu angelegte Tätigkeit beginnt standardmäßig als geplant. Ein positiver technischer Test oder eine DSFA-Entscheidung schaltet sie nicht automatisch aktiv. Ein geplanter Vorgang kann bereits genau beschrieben und geprüft werden. Beendete Tätigkeiten behalten ihren dokumentierten Verlauf; damit ist nicht behauptet, dass sämtliche ursprünglichen Daten oder Sicherungen bereits gelöscht sind.

# 2. Sachfelder und gesetzliche Zuordnung

Alle folgenden Felder sind Texte. Das ermöglicht konkrete, ausformulierte Erläuterungen ohne Scheingenauigkeit. Mehrere Werte werden verständlich bezeichnet und ihren jeweiligen Personen, Zwecken oder Datenkategorien zugeordnet. Leerer Text bedeutet noch nicht erhoben; `unbekannt` bezeichnet eine ausdrücklich festgehaltene Erkenntnislücke. Ein begründetes „nicht einschlägig“ ist eine andere Aussage.

## 2.1. Verantwortlichentätigkeit nach Artikel 30 Absatz 1 DSGVO

| Feld | Inhalt | Zuordnung |
|---|---|---|
| `purpose` | Bestimmte Zwecke, getrennt nach tatsächlicher Nutzung. | Gesetzlicher Mindestinhalt. |
| `joint_controller` | Gegebenenfalls gemeinsam Verantwortliche mit Kontakt und Rollenbezug. | Gesetzlicher Mindestinhalt, soweit einschlägig. |
| `data_subjects` | Kategorien betroffener Personen. | Gesetzlicher Mindestinhalt. |
| `data_categories` | Kategorien personenbezogener Daten einschließlich Besonderheiten. | Gesetzlicher Mindestinhalt. |
| `recipients` | Kategorien von Empfängern einschließlich einschlägiger Auslandsbezüge. | Gesetzlicher Mindestinhalt. |
| `transfers` | Drittland oder internationale Organisation, Datenfluss und gegebenenfalls besondere Garantiedokumentation. | Gesetzlicher Mindestinhalt, soweit einschlägig; zusätzliche Instrumentenprüfung als Ergänzung. |
| `retention` | Vorgesehene Löschfristen je Kategorie, auslösendes Ereignis und Begründung. | Nach Artikel 30 wenn möglich anzugeben. |
| `toms` | Allgemeine Beschreibung tatsächlicher Schutzmaßnahmen, gegebenenfalls Nachweisverweis. | Nach Artikel 30 wenn möglich anzugeben. |

Kontaktdaten des Verantwortlichen, gegebenenfalls Vertreter und Datenschutzbeauftragter kommen aus `organization`. Fehlende Angaben werden nicht durch die Existenz eines Organisationsnamens kompensiert. „Wenn möglich“ ist keine freie Einladung, Löschlogik und Maßnahmen unerhoben zu lassen; die offene Ermittlung wird sichtbar gehalten.

## 2.2. Auftragsverarbeitung nach Artikel 30 Absatz 2 DSGVO

| Feld | Inhalt | Zuordnung |
|---|---|---|
| `controller_contacts` | Name und Kontakt jedes Verantwortlichen, für den der Anbieter tätig ist, sowie einschlägige Vertreter- und DSB-Angaben. | Rollenbezogener gesetzlicher Mindestinhalt. |
| `processing_categories` | Verarbeitungskategorien mit Zuordnung zum jeweiligen Verantwortlichen. | Rollenbezogener gesetzlicher Mindestinhalt. |
| `transfers` | Einschlägige Drittlandsübermittlungen und Dokumentation wie gesetzlich gefordert. | Rollenbezogener gesetzlicher Mindestinhalt, soweit einschlägig. |
| `toms` | Allgemeine Beschreibung der Schutzmaßnahmen. | Wenn möglich aufzunehmen. |

Die eigene Organisation ist in dieser Ansicht der Auftragsverarbeiter. Soweit weitere Auftragsverarbeiter mit Kontakten erforderlich zu benennen sind, werden sie mit eindeutigem Rollenbezug im einschlägigen Sachfeld beschrieben. Bei vielen Auftraggebern ist eine klar referenzierte Kontaktanlage zulässig, sofern sie zusammen mit dem Verzeichnis verfügbar bleibt und die Zuordnung vollständig ist. „Kunden aus der Gesundheitsbranche“ allein ersetzt nicht die einzelnen Verantwortlichen.

Eine freiwillige Erweiterung um Zwecke, Datenkategorien oder Löschung kann die Zusammenarbeit erleichtern. Daraus wird kein identischer gesetzlicher Mindestkatalog beider Rollen. Eigene Personalverwaltung oder Abrechnung des Dienstleisters gehört in getrennte `controller`-Datensätze.

## 2.3. Organisatorische Ergänzungen

| Feld | Inhalt | Grenze |
|---|---|---|
| `title`, `owner` | Verständliche Bezeichnung und intern zuständige Person. | `owner` ist nicht automatisch die juristische Person des Verantwortlichen. |
| `legal_basis` | Tragende Rechtsgrundlage, Begründung, besondere Kategorien und Verifikationsstand. | Ergänzt das VVT, schafft keine Verarbeitungserlaubnis. |
| `systems`, `processor_contracts` | Tatsächlich verwendete Systeme und Vertragsnachweise. | Ein Softwareprodukt ist nicht automatisch eine Tätigkeit. |
| `sources`, `next_review` | Belegstelle mit Stand sowie interne Wiedervorlage als ISO-Datum oder leer. | Die Wiedervorlage ist ohne gesonderten Beleg keine gesetzliche Frist. |

Die Lückenübersicht enthält auch interne Arbeitsanforderungen wie die zuständige Person. Sie ist deshalb weder eine abschließende juristische Prüfung sämtlicher Mindestangaben noch ein behördlicher Prüfbescheid. Beispielsweise kann sie nicht feststellen, ob eine eingetragene Löschfrist materiell richtig oder eine Sicherheitsmaßnahme tatsächlich umgesetzt ist.

# 3. Risikovorprüfung und menschliche Entscheidung

## 3.1. Screening

| Feld | Zulässige Werte | Bedeutung |
|---|---|---|
| `high_risk` | `offen`, `ja`, `nein` | Voraussichtlich hohes Risiko nach begründeter Prüfung. |
| `art35_3` | `offen`, `ja`, `nein` | Einschlägigkeit eines Tatbestands aus Artikel 35 Absatz 3. |
| `positive_list` | `offen`, `ja`, `nein` | Einschlägigkeit der tatsächlich maßgeblichen DSFA-Pflichtliste. |
| `severity`, `likelihood` | `offen`, `gering`, `mittel`, `hoch` | Interne qualitative Einordnung von Schwere und Wahrscheinlichkeit. |
| `priority` | `offen`, `1`, `2`, `3` | Interne Bearbeitungspriorität, keine gesetzliche Risikoklasse. |
| `criteria`, `rationale`, `sources` | Text | Kriterien, Sachverhaltsbegründung und konkrete Quellen. |

Die Organisation soll erklären, wie sie ihre Prioritäten verwendet; beispielsweise 1 für vorrangig zu klärende Einführungshindernisse, 2 für zeitnah zu schließende Lücken und 3 für normale Pflege. Das Beispiel ist keine zwingende Rechtsregel. Keine Kombination dieser Zahlen entscheidet automatisch, dass eine DSFA entbehrlich ist. Schutzmaßnahmen und verbleibende Risiken werden in den Begründungen nachvollziehbar getrennt.

## 3.2. Entscheidung und Sachstandsbindung

`review` enthält `decision`, `reviewer`, `reviewed_at`, `rationale`, `sources` und `basis_sha256`. Die Entscheidung lautet `offen`, `erforderlich` oder `begruendet_nicht_erforderlich`. Der Helfer dokumentiert eine Entscheidung, erstellt dadurch aber nicht selbst die DSFA und führt keine Behördenkonsultation durch.

Eine negative Entscheidung ist technisch nur möglich, wenn die drei Pflichttrigger zuvor mit `nein` eingetragen wurden. Das ist eine Konsistenzkontrolle, keine materielle Verifikation dieser Einträge. Eine Person könnte falsche Tatsachen eingeben; deshalb bleiben tatsächliche Prüfung und Verantwortung erforderlich. Namen werden nicht durch Maschinenbezeichnungen ersetzt. Die technische Namensprüfung authentifiziert keine Person.

`basis_sha256` bindet die Entscheidung an die Sachfelder einschließlich Screening. Der berechnete Prüfstand lautet `offen`, `aktuell` oder `veraltet`; er wird nicht als zusätzlicher frei bearbeitbarer Wahrheitswert gespeichert. Jede Änderung eines einbezogenen Sachfelds entwertet im Helfer den bisherigen Hash-Bezug, auch eine redaktionelle Korrektur oder ein geändertes Wiedervorlagedatum. Der fachliche Umfang der erneuten Prüfung richtet sich weiterhin nach den tatsächlichen Auswirkungen. Die ursprüngliche Entscheidung bleibt erkennbar, trägt aber nicht unverändert die neue Fassung.

# 4. Rücklauf, Historie und Formate

Die sieben Excel-Blätter heißen `Uebersicht`, `Taetigkeiten`, `Art30`, `Screening`, `Organisation`, `Entscheidungen` und `_meta`. Die drei Eingabeblätter `Taetigkeiten`, `Art30` und `Screening` dienen der Sachpflege. Organisations- und Entscheidungsänderungen erfolgen mit eigenen Befehlen, damit sie nicht durch einen normalen Tabellenrücklauf unbemerkt ersetzt werden. Die detaillierten Regeln stehen in [Dateipflege](dateipflege.md).

Der XML-Export ist ein UTF-8-Container mit JSON-Nutzdaten und Referenz auf den Ausgangsstand. Er erhält die Struktur dieses Formats, behauptet aber keine Kompatibilität mit einem bestimmten fremden Produkt. Ein importierbarer Rücklauf bleibt an Registerkennung und Ausgangsstand gebunden. Der Helfer führt keine automatische Zusammenführung konkurrierender Versionen aus.

Vor Änderungen entstehen lokale Vorfassungen; das Protokoll hält Anlass, Person und Bezug zum Vorgängerstand fest. Diese Historie ist vertraulich und benötigt einen geregelten Aufbewahrungs- und Sicherungsprozess. Hashes sind Vergleichsmittel, keine digitale Signatur und kein unveränderliches Archiv. Der Dateispeicher, dessen Berechtigungen und ein möglicher Mehrbenutzerbetrieb bleiben organisatorisch zu regeln.
