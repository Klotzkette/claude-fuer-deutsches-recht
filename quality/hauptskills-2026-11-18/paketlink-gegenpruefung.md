# Unabhängige Codeprüfung der Paketlink-Nachführung

## 1. Ergebnis und Umfang

Prüfung am 18. November 2026: `package_link_revisions.py`, seine Einbindung in `main_skill_revisions.py` und die beiden Regressionstests vollständig gelesen. Zusätzlich wurden die nachgelagerten Hashvergleiche in `quality_lab.validate_file_hashes` und `consolidate-skill-cap.verify_source_map` kontrolliert. Kein konkreter Fehler und kein allgemeiner Hash-Bypass in diesem geprüften Änderungsweg festgestellt. Keine Produktdatei wurde im Rahmen dieser Gegenprüfung geändert.

## 2. Entscheidende Sicherungen

2.1. Die Quelldatei wird anhand des benannten Plugins und seines Marketplace-Verzeichnisses zugeordnet. Zulässig sind ausschließlich Markdown-Dateien unter dessen `skills/` oder `references/`. Absolute Nachweispfade, `..`, Rückstriche, direkte Symlinks und aufgelöste Pfadausbrüche werden abgewiesen. Archivpfad, Archivbytes und aktuelle Datei sind separat durch den vorgesehenen Pfad und ihre Hashes gebunden.

2.2. Jede ursprüngliche Linkadresse muss auf das tatsächlich vorhandene dokumentierte Repositoryziel auflösen. Neue Adressen werden aus diesem Ziel deterministisch gebildet. Die drei Fälle sind begrenzt: zentrale Zitierweise als bytegleiche Kopie im selben Plugin; eigene vorhandene Promptdatei am Pages-Download; vorhandene Testakte beziehungsweise Qualitätsdatei unter der festgelegten GitHub-Adresse. Anker bleiben erhalten. Bei Zitierweisen bindet zusätzlich `copied_sha256` die Kopie, sodass eine gemeinsam geänderte Quelle und Kopie nicht allein wegen ihrer Gleichheit durchgehen.

2.3. Der Validator ersetzt nur Treffer des mit dem Paketbuilder übereinstimmenden Linkmusters. Doppelte alte Ziele sind unzulässig; jede deklarierte Ersetzung muss tatsächlich vorkommen. Der vollständig rekonstruierte UTF-8-Dateiinhalt muss bytegleich zur aktuellen Datei sein. Eine zusätzliche Rechtsbehauptung oder sonstige Änderung wird deshalb auch dann zurückgewiesen, wenn jemand nur den aktuellen Hash im Linknachweis nachführt.

2.4. Der Hauptskillpfad bleibt gesondert an registrierten Einstieg, historischen Bestand, konkrete redaktionelle Prüfung, Fortsetzungsszenario und Quellenkarten gebunden. Bei anderen Dateien wird der eng begrenzte Paketlinknachweis verwendet. Die Gesamtvalidierung prüft zusätzlich sämtliche Paketlinkdatensätze. `historical_bytes` liefert eine Vorfassung nur bei Übereinstimmung mit dem angefragten historischen Hash; bei fehlender Übereinstimmung bleiben die aktuellen Bytes zurück. Die aufrufenden Qualitäts- und SourceMap-Prüfer vergleichen den erwarteten Hash anschließend erneut. Historische Originalrekonstruktion und Prüfbelege werden nicht umgeschrieben oder allgemein freigestellt.

## 3. Ausgeführte Gegenproben

Mit dem vorhandenen Venv-Python wurden acht Tests aus `test-package-link-revisions.py` und 15 Tests aus `test-main-skill-revisions.py` erfolgreich ausgeführt. Abgedeckt sind unter anderem Zusatztext trotz nachgeführtem Hash, veränderte beziehungsweise gemeinsam veränderte Zitierweisen, falsches Ziel, verändertes Archiv, falsches Plugin, unzulässige Hauptskillzuordnung und fremder erwarteter Hash.

Vier zusätzliche isolierte Prüfungen in temporären Verzeichnissen bestanden: Paketfallback mit passendem historischen Hash; Zurückweisung eines unpassenden historischen Hashs durch erneuten Vergleich; Ablehnung doppelter alter Ziele; zulässiger Prompt-Download mit unverändertem Anker und Ablehnung eines geänderten Ankers. Diese Proben änderten keine Repository-Testdateien.

## 4. Bewusste Grenzen

Das Linkmuster ist der bestehende Builder-Ausdruck und kein vollständiger Markdown-Parser. Die Prüfung bestätigt den exakten Austausch der von ihm erkannten Zielzeichenfolgen. Sie prüft keine Netzwerkauslieferung der öffentlichen URLs. Testakten- und Promptziele werden auf Identität und lokale Existenz, nicht auf einen dauerhaften Inhaltsstand gehasht; das ist die festgelegte begrenzte Reparatur. Die Prüfung ersetzt keine unabhängige inhaltliche Bewertung der Hauptskilländerungen und keine allgemeine Sicherheitsprüfung des gesamten Repositorys.

## 5. Gelesene Dateistände

- `scripts/package_link_revisions.py`: SHA-256 `efb62e9b0702c1902e9c1958619e66a1531c5a7509d2949b1ef4906383777808`.
- `scripts/main_skill_revisions.py`: SHA-256 `94bf73683b4cad53c620ca2bdcfa2fd66614b50f23eea6d5f21f174864d66ac8`.
- `scripts/test-package-link-revisions.py`: SHA-256 `bbfd13733c9a66db83b94542c410f0da3d7f528fd693d57356b6ba0fcb2b53a6`.
- `scripts/test-main-skill-revisions.py`: SHA-256 `52dd5748d316e6ae681c6f16d30d9bac592531279ac8d85ff75c95b0f7182d16`.

## 6. Zusatzprüfung der belegten Hauptskill-Fortsetzung

Die spätere Ergänzung `main_revision_followup` wurde am selben Tag gesondert gelesen. Sie lässt die rein mechanische Linkprüfung auf einer eigenen Zwischenfassung laufen: fester Archivpfad, ursprünglicher `after_sha256` und vollständiges Link-Replay müssen weiterhin übereinstimmen. Zuvor muss der aktuelle Text als registrierter Hauptskill seine vollständige Vorfassungs-, Einzelreview-, Szenario- und Quellenbindung durch `main_skill_revisions.previous_bytes` bestehen. Die Ausweichroute kann deshalb weder einen unregistrierten Skill noch einen ungeprüften aktuellen Text freistellen. Kein konkreter Fehler oder allgemeiner Hash-Bypass in dieser Ergänzung festgestellt.

Alle zwölf aktuellen Paketlinktests bestanden, einschließlich nachträglicher Textänderung, manipulierter Zwischenfassung und fehlender Hauptskillregistrierung. Diese Zusatzprüfung ist eine Code- und Regressionstestprüfung; sie wiederholt keine fachliche Bewertung der drei redaktionell fortgeführten Hauptskills. Die früheren acht Tests und Dateistände oben bleiben als historischer Prüfstand erhalten.

- `scripts/package_link_revisions.py`: SHA-256 `08fc59346ffa80c594754a1817ab6a008fe570117a0338d7dd477be91a1d5a17`.
- `scripts/main_skill_revisions.py`: SHA-256 `94bf73683b4cad53c620ca2bdcfa2fd66614b50f23eea6d5f21f174864d66ac8`.
- `scripts/test-package-link-revisions.py`: SHA-256 `692149a045bb16b64921ea190383e649a065cac8898939eb6b30832d07f0ccdd`.
