# 1. Prüfung von Mandatsjournal und Exporthilfen

Prüfdatum: 7. Oktober 2026. Geprüft wurden ausschließlich die neuen lokalen Hilfen der SI-nativen Kanzlei. Es fand kein Versand, keine Bankhandlung und keine produktive Finanzbuchung statt. Die Prüfungen sind ausgeführte Softwaretests und eine gezielte PDF-Sichtprüfung; sie sind keine beobachteten Modelltests und keine vollständige Prüfung des Repositorys.

## 1.1. Ausgeführte Tests

| Prüfgruppe | Ergebnis | Tatsächlich geprüfter Umfang |
| --- | --- | --- |
| `scripts/test-si-native-kanzlei.py` | 19 von 19 bestanden | Honorararten, echte Nullwerte und offene Zeitangaben, Bestätigungsstand, Deckel einschließlich Auslagen, RVG nur mit separater Berechnung, Festpreis, Storno, Idempotenz, Eingabegrenzen, CSV-Schutz und Zahlungsabgrenzung. |
| Darin: echter CLI-Durchlauf | Bestanden | Acht parallele Prozesse mit verschiedenen Zeitbuchungen in derselben Akte; alle acht Einträge und Journalrevision 10 erhalten. Wiederholte ID erzeugt keine zweite Buchung. Gelöschte Ansichten werden aus dem Journal identisch neu erzeugt. |
| `scripts/test-si-native-kanzlei-exporte.py` | 16 von 16 bestanden | Sechs beA-Tests, sieben XRechnung-Tests und drei begrenzte Testakten-Filterprüfungen. |

Reproduktion bei vorhandenen Abhängigkeiten:

```bash
python3 scripts/test-si-native-kanzlei.py -v
python3 scripts/test-si-native-kanzlei-exporte.py -v
```

Die Exporttests benötigen `pypdf` und `reportlab`; der ausgeführte Lauf verwendete die vorhandene gebündelte Python-Laufzeit. Die Journaltests benötigen nur die Python-Standardbibliothek.

## 1.2. Relevante Grenz- und Fehlerfälle

Offene Zeiteinträge ohne `minutes` oder `billable` werden als unbekannte Werte normalisiert, nicht als null Minuten oder kostenlose Tätigkeit. Der Export bleibt möglich; ausgelassene und ausdrücklich auf `null` gesetzte Felder werden bei der Wiederholung derselben ID als gleicher Stand behandelt. Bestätigte Zeit ohne Dauer oder Abrechenbarkeit wird abgewiesen.

Bei einem gemeinsamen Gebühren- und Auslagendeckel bleiben der tatsächliche Auslagenwert und der nicht angesetzte Überschuss sichtbar. Der geprüfte Gegenfall enthält 150 Euro Auslagen bei einem Deckel von 100 Euro und keine Zeitposition. 50 Euro werden als Überschuss benannt; sie verschwinden nicht aus dem Nachweis.

Für beA wurden die tatsächlichen Paketgrenzen einschließlich übergebener Zusatzdateien geprüft: 1.000 Dateien werden akzeptiert, 1.001 führen im strengen Modus zum Stop. 200.000.000 Bytes werden akzeptiert, 200.000.001 führen zum Stop. Die Größenprüfung benutzt eine temporäre Sparse-Datei als reinen Größenprüfling; sie ist kein inhaltlich validiertes Versand-PDF. Die erzeugten PDFs wurden dagegen tatsächlich gelesen. Zusatzdateien werden gezählt, aber nicht inhaltlich als Signatur oder XJustiz-Datensatz validiert.

Geprüft wurden Dateinamenprofile mit höchstens 84 beziehungsweise 60 Zeichen, längenüberschreitende Zusatzdateien mit 84 beziehungsweise 90 Zeichen Grenze, Originalhashes, unveränderte Seitenzahlen, Stempel nur auf der ersten Anlagenseite und ungestempeltes Hauptdokument. Eingangs-/Ausgangsüberlappung und unbeabsichtigtes Ersetzen einer vorhandenen Ausgabe werden abgewiesen.

XRechnung-Tests prüfen den dokumentierten Standardfall EUR, inländische Parteien und 19 Prozent Umsatzsteuer, bekannte Beispielbeträge 208,00 Euro netto, 39,52 Euro Steuer und 247,52 Euro brutto. Ein als freigegeben bezeichneter Export benötigt das ausdrückliche Prüfungsfeld; das Feld selbst ist kein Nachweis einer materiellen Prüfung. Geprüft wurden außerdem unzulässige Steuer-/Währungs-/Länderkonstellationen, Datumsfolgen, Pflichtfelder, doppelte Positionen, negative und nicht endliche Zahlen, Einheiten, IBAN-Prüfziffer, E-Mail-Format und Schutz vorhandener Ausgabedateien.

Die drei zusätzlichen Filterregressionen prüfen die ausdrücklich verlangten ergänzbaren Entwürfe: Alle 24 tatsächlichen Root-Dateien `09_Fachlicher_Dokumententwurf.docx` werden exportiert. Datumsfelder sind nur für genau diese Datei in einer Akte mit dem Präfix `si-kanzlei-` zulässig; andere DOCX-Dateien, Unterordner, fremde Akten und TXT-Kopien erhalten keine Ausnahme. Musterlösungs-, Prüfer-, Erwartungshorizont- und andere inhaltliche Sperrmarker bleiben auch in der vorgesehenen Entwurfsdatei gesperrt. Insgesamt wurden damit 35 Tests ausgeführt und bestanden.

Diese Tests ersetzen nicht den amtlichen KoSIT-Schematron-/XSD-Lauf. Der Export meldet selbst weiterhin `kosit_validated=false`; die offizielle Prüfung des Beispiels wird separat dokumentiert. Auch ein amtlicher technischer Prüflauf bestätigt keine tatsächliche Leistung, Steueridentität oder Honorarberechtigung.

# 2. Tatsächliche PDF-Sichtprüfung

Die gezielte Fixture wurde mit `scripts/test-si-native-kanzlei-exporte.py --visual-fixture <neuer-temporärer-Ordner>` erzeugt. Drei Original-PDFs ergeben drei Versanddateien mit insgesamt fünf Seiten. Alle fünf gerenderten Versandseiten wurden einzeln visuell angesehen: eine Hauptdokumentseite, zwei Seiten Anlage K1 im Hochformat und zwei Seiten Anlage K2 im Querformat.

Der Haupttext blieb vollständig sichtbar. Das Hauptdokument ist ungestempelt. Bei K1 und K2 trägt ausschließlich die erste Seite die richtige Bezeichnung; die Folgeseiten bleiben ungestempelt. Die kleinen fett gesetzten Stempel stehen in den freien oberen Rändern, ohne Inhalte zu überdecken. Fußzeilen und Betragsangaben sind vollständig. Die Originalhashes blieben unverändert.

Diese Sichtprüfung betrifft bewusst freie Ränder. Der Helfer erkennt weder Textkollisionen noch problematische Seitenboxen selbst zuverlässig. Skill und Werkstatt verlangen deshalb die Sichtprüfung vor und nach der Anwendung; bei ungeeigneter Seite ist ein anderes passendes PDF-Werkzeug erforderlich. Es wurde keine allgemeine Freigabe beliebiger PDFs, signierter Unterlagen oder tatsächlicher gerichtlicher Einreichungen erteilt.

| Versanddatei | SHA-256 |
| --- | --- |
| `01_20261007_AnlageK1_Pachtvertrag.pdf` | `1b79198fa0ef242ce1acd2b838e7f1d8d8368b4c0900496a1088853d31273870` |
| `02_20261007_AnlageK2_Abrechnung.pdf` | `15eae7e57caeb103f857a3b8fe343b45073c2f56d616c8eea5299f7440f02ed1` |
| `00_20261007_Schriftsatz_mit_Antraegen.pdf` | `7df76c8e33483f085f13cb249e2c31fe32f8fcec4d2c9c478f07b8d97712d5a7` |

# 3. Text- und Integrationsprüfung

Alle 16 Skills bestanden den Skill-Creator-Validator. Die sechs Hauptabschnitte, Namen, Frontmatter und referenzierten lokalen Dateien wurden kontrolliert. Fünfzehn Fachskills und ein Hauptskill halten die Nutzergrenze ein. Mini und Hauptproblem haben jeweils 7.484 UTF-8-Bytes; ihre TXT-Paare und das Werkstatt-Paar sind byteidentisch. Die Prompts enthalten die notwendigen Abläufe eigenständig und setzen kein unsichtbar geladenes Plugin voraus. Zugriff, Dateioperationen und Hintergrundausführung werden von den tatsächlichen Fähigkeiten der Oberfläche abhängig gemacht.

Claude- und Codex-Manifest sowie Marketplace-Eintrag nennen übereinstimmend Version 445.33.3. Die lokale Linkprüfung berücksichtigte im Sparse-Checkout auch getrackte Dateien, die nicht ausgecheckt sind. Bei 4.598 lokalen Verweisen und 42 neuen Download-Gateway-Zielen waren zum Prüfzeitpunkt nur 48 Verweise auf die 24 noch im Aufbau befindlichen Gesamt-PDFs offen. Deren Existenz und die öffentlichen Downloads sind vom abschließenden Paketlauf gesondert zu prüfen. Erkannte Restpunkte zu alphabetischer Einordnung, Zählwerten und ergänzenden Indexeinträgen wurden an die Integration zurückgegeben; dieser Bericht behauptet deren Abschluss nicht.

# 4. Geprüfte Programmstände

- `si-native-kanzlei/scripts/kanzlei.py`: `8da4ac20133de6325a4a093d0270e9d524bd560867fc2ef2bdc2e1c08caabda3`.
- `si-native-kanzlei/scripts/build_anlagenkonvolut.py`: `580de3a1101c2eb0bf9d03efdfcd18ff3c303a85287c22d275396ba19036dc7d`.
- `si-native-kanzlei/scripts/xrechnung.py`: `2ac1de5c818f78a732da7add493d0be7ebb3423483d4eef92a744b0eba8be729`.
- `scripts/test-si-native-kanzlei.py`: `46cde212610181e515b2a689ef84ce4475af25f8780254a6f5bdc1d200f260ca`.
- `scripts/test-si-native-kanzlei-exporte.py`: `148c8530532db5e3879858f24a41c0539eeda33ae88098c6eabfe82d8ff72f12`.
- `scripts/testakte_file_filter.py` (begrenzte neue Entwurfsausnahme): `bc5078b7f6520f58f693ca2a77332b9f928955091718ced6967b2d83343c2d39`.
