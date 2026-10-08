# 1. Plugin-Anbindung des vertiefenden Arbeitsbuchs

Bearbeitungsstand: 8. Oktober 2026. Dieser Bericht betrifft die eng begrenzte Anbindung des vom Hauptlauf erzeugten Arbeitsbuchs an das bestehende Plugin. Er ist kein Bericht über einen Live-Test in Word oder über die erfolgreiche Ausführung der neu definierten Verhaltensfälle.

## 1.1. Durchgeführte Änderungen

Der Werkstatt-Einstieg erklärt nun in verständlicher Sprache Ziel, benötigte Unterlagen und die anschließenden fertigen Schreiben. Die ausführbare Anweisung bleibt unmittelbar anschließbar und benötigt beim Hochladen keine Startformel. Die Navigation verweist auf die in derselben Datei enthaltenen Kapitel 20 bis 23; der generierte Handbuchblock wurde in diesem Teilauftrag nicht redaktionell verändert.

Der Plugin-Einstieg und acht einschlägige Fachskills verweisen gezielt auf die mitgelieferte Referenz. Jeder Verweis ist mit der Fortsetzung in die konkrete Prüfung beziehungsweise den bestellten Entwurf verbunden. Fehlende Referenz- oder Browserfunktionen werden nicht als Erlaubnis zu erfundener Lektüre behandelt und stoppen nicht die unabhängig mögliche Arbeit. Entscheidungsaussagen und eigene Anwendungsbeispiele bleiben getrennt.

Für Word wird zwischen Gesamttext und Markierung, Lesen, Kommentieren und tatsächlicher Änderung unterschieden. Ein Prüfauftrag führt nicht zum ungesicherten Überschreiben des einzigen Originals. Es werden weder Änderungsverfolgung noch Speicherung, Export, Signaturprüfung oder Zeugnisneuerteilung behauptet, die nicht tatsächlich bestätigt sind. Ohne Dokumentwerkzeuge bleiben Analyse, Ersatztexte und beide geschuldeten Schreiben vollständig im Chat zu liefern.

Der Schlussformelskill unterscheidet die verschiedenen Bindungsansätze. Im vorgefundenen Plugintext wurde BAG 9 AZR 352/04 nicht als pauschal tragende Bindungsentscheidung zitiert; eine entsprechende bestehende Fehlzuordnung war dort nicht zu korrigieren. Die Erläuterung der in BAG 9 AZR 272/22 offengelassenen zusätzlichen Selbstbindung bleibt erhalten. Der neue Prüffall verlangt ausdrücklich eine eigenständige und begrenzte Auswertung der älteren Entscheidung.

## 1.2. Tatsächlich ausgeführte Prüfungen

1. Der Skill-Creator-Validator `quick_validate.py` wurde für sämtliche 31 Skillverzeichnisse ausgeführt. Alle 31 Meldungen lauteten „Skill is valid!“. Diese Prüfung bewertet Struktur und Frontmatter, nicht das tatsächliche juristische Verhalten.
2. Das Qualitätsprofil wurde mit `jq` eingelesen. Es enthält nun 19 Fälle mit eindeutigen Kennungen und nichtleeren Kriterien. Die drei neuen Fälle betreffen den portablen Textchat bis zu beiden Schreiben, einen Word-Markierungszugriff ohne gesicherte Originalkopie und die Abgrenzung der Bindung an ein Endzeugnis.
3. Die neun neu eingefügten Handbuchlinks in Skills wurden auf vorhandene relative Zielpfade geprüft; alle zeigen auf `arbeitszeugnispruefer/references/arbeitszeugnis-handbuch.md`.
4. Der Schnellstart ist gegenüber dem Ausgangsstand unverändert und hat weiterhin 7.491 UTF-8-Bytes.
5. Die zwischen den Erzeugungsmarken stehenden Handbuchblöcke in Werkstatt und Pluginreferenz wurden auf Textidentität geprüft: identisch. Ein erster Vergleich der bloßen Blockinhalte gegen die ganze Referenzdatei war wegen deren zusätzlicher Überschrift nicht passend; die wiederholte Prüfung verglich korrekt beide markierten Blöcke.
6. `git diff --check` für Plugin und Qualitätsprofil meldete keine Leerraumfehler.

Es wurden keine globalen Generatoren, keine Veröffentlichung, kein Commit und kein Push ausgeführt. Die Pluginversion und die Paketkonfiguration wurden in diesem Teilauftrag nicht geändert. Etwaige parallele Änderungen des Hauptlaufs sind davon zu unterscheiden.

## 1.3. Nicht durchgeführte oder noch offene Prüfungen

Die drei neuen Qualitätsfälle sind Prüfvorgaben, keine bestandenen Tests. Es fand in diesem Teilauftrag kein unabhängiger Modell-Forward-Test, kein Live-Word-Test und kein neues Packen oder Installieren statt. Paketinhalt und Veröffentlichung bleiben dem Hauptlauf vorbehalten. Die redaktionelle Anbindung allein belegt nicht, dass ein beliebiger fremder Chat die gesamte Werkstatt aufnehmen oder mit Word interagieren kann.

## 1.4. Dateien dieses Teilauftrags

1. `arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md`: nur eigener Einstieg und Abschnitt 10 außerhalb des generierten Blocks.
2. `arbeitszeugnispruefer/README.md`: manuelle Arbeitsbuch-Ergänzung außerhalb automatisch erzeugter Blöcke.
3. `arbeitszeugnispruefer/skills/einfuehrung-pruefauftrag/SKILL.md`.
4. `arbeitszeugnispruefer/skills/beweislast-bag-9-azr-584-13/SKILL.md`.
5. `arbeitszeugnispruefer/skills/auslassungen-erkennen/SKILL.md`.
6. `arbeitszeugnispruefer/skills/fuehrungskraft-verhalten-pruefen/SKILL.md`.
7. `arbeitszeugnispruefer/skills/taetigkeitsabschnitt-wertigkeit-pruefen/SKILL.md`.
8. `arbeitszeugnispruefer/skills/schlussformel-pruefen/SKILL.md`.
9. `arbeitszeugnispruefer/skills/aeussere-form-und-briefkopf/SKILL.md`.
10. `arbeitszeugnispruefer/skills/klagestrategie-und-vollstreckung/SKILL.md`.
11. `arbeitszeugnispruefer/skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md`.
12. `quality/evals/arbeitszeugnispruefer.json`: drei konkrete neue Prüffälle; frühere Quellenprüfungsdaten und Prüfberichte unverändert.
13. `quality/arbeitszeugnispruefer/handbuch-2026-10-08/plugin-anbindung.md`: dieser Bericht.
