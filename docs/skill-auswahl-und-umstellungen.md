# Skills nach Aufgabe auswählen

## 1. Mit dem gewünschten Ergebnis beginnen

Ein Skill bezeichnet eine konkrete Arbeit: etwa ein Zeugnis erstellen, Unterhalt gegenrechnen oder die Zustimmung einer finanzierenden Bank vorbereiten. Ein Plugin bündelt solche Aufgaben für ein Fachgebiet. Wähle zuerst die passende Aufgabe und stelle die vorhandenen Unterlagen bereit; die einzelnen Prüffragen und Nachschlagewerke müssen nicht vorab ausgewählt werden.

Beispiele für einen direkten Einstieg:

- Arbeitszeugnis: „Erstelle aus Aufgabenliste und Beurteilung ein qualifiziertes Zwischenzeugnis. Markiere nur die noch fehlenden Tatsachen.“
- Familienrecht: „Prüfe die gegnerische Unterhaltsrechnung für die genannten Monate. Zeige jede Abweichung mit Beleg und rechne die vertretbaren Varianten.“
- Erbrecht: „Lies Testament, Personenstandsurkunden und Nachlassunterlagen. Bearbeite zunächst die im Anschreiben bezeichnete Frage, nicht alle denkbaren Erbfälle.“
- Unternehmenskauf: „Prüfe die Kontrollwechselklausel im Kreditvertrag und entwirf die erforderliche Zustimmungsanfrage.“
- Historisches Landrecht: „Bestimme die einschlägige historische Normfassung und erläutere den Fall aus ihr. Trenne heutiges Recht ausdrücklich davon.“

Ist bereits ein Entwurf vorhanden, gehört er zum Ausgangsmaterial. Eine bloße Bitte um Überarbeitung soll kein erneutes Vollinterview auslösen. Rückfragen betreffen nur Informationen, die sich weder aus den zugänglichen Unterlagen noch aus dem bisherigen Auftrag ergeben und den nächsten Bearbeitungsschritt tatsächlich ändern.

## 2. Weniger Auswahlpunkte, gezielte Vertiefung

Die Überarbeitung bündelt besonders überlappende Arbeitswege in sechs Bereichen. Eigenständige Rechtsbehelfe und unterschiedliche Anspruchsarten bleiben unterscheidbar. Detailmaterial liegt, soweit erforderlich, in verlinkten Referenzen beim jeweiligen Skill. Diese Referenzen sind keine weiteren auswählbaren Skills.

| Bereich | Zusammengeführte Aufgaben | Fachliche Grenze |
| --- | --- | --- |
| Arbeitszeugnisgenerator | Zeugnis erstellen; Ausbildung und Praktikum; Leistung und Verhalten; Berichtigung; Abschluss und Form | Rechtsvermerke und Rechtsprechungsnachweise gehören nicht in den auszugebenden Zeugnistext. |
| AGB-Prüfung | Transparenz; Inhaltskontrolle; Klauselfolgen; Varianten; Haftung; Rechtswahl; Schiedsvereinbarung; Vertragsänderung | Verbrauchervertrag, Unternehmergeschäft und individuell ausgehandelte Vereinbarung bleiben getrennte Prüfweichen. |
| Familienrecht | Mandatsaufnahme; Akten und Belege; Unterhaltsrechnung; Versorgungsausgleich und Auskünfte | Neue Rechnung, Gegenrechnung und gerichtlicher Antrag werden nicht miteinander verwechselt. |
| Erbrecht | Erbfall und Sofortsicherung; Nachlassaufklärung; Gestaltung; Pflichtteil; Abwicklung und Verfahren | Pflichtteil, Ergänzung, Auskunft, Erbenhaftung und Steuerverfahren behalten jeweils eigene Voraussetzungen. |
| Großkanzlei M&A | Fusionskontrolle; Finanzierungszustimmungen; Organbeschlüsse; Beteiligungskette; Due-Diligence-Bericht | Gesellschaftsinterne Freigabe ersetzt weder Vertretungsmacht noch Zustimmung eines Kreditgebers oder einer Behörde. |
| Preußisches Allgemeines Landrecht | Historische Quellenarbeit und zusammenhängende Fallgebiete | Historische Normen sind keine aktuelle Rechtsgrundlage. Fundstelle, Fassung, Geltungsraum und heutiger Bezug werden getrennt ausgewiesen. |

## 3. Bestehende Aufrufe umstellen

Die vollständige Zuordnung alter zu neuen Aufrufnamen steht im [Umstellungsregister](../scripts/skill-selection-migrations.json). Das Register dokumentiert die Änderung; es richtet keine technischen Weiterleitungen ein. Alte gespeicherte Direktaufrufe müssen daher auf den neuen Namen umgestellt werden. Die aktuellen Namen und Markdown-Downloads stehen in der [Skill-Gesamtübersicht](../SKILLS.md) und auf den dort verlinkten Plugin-Detailseiten.

Eine Oberfläche mit ausdrücklich unterstützten Direktaufrufen verwendet den Plugin-Namen einmal als Namensraum, gefolgt vom tatsächlichen Skill-Namen. Beispiel: `/arbeitszeugnisgenerator:arbeitszeugnis-erstellen`. Ein vorhandener Name wird nicht durch zusätzliches Voranstellen des Plugin-Namens ergänzt. In einer Oberfläche mit Auswahlmenü ist die dort angebotene Aufgabe maßgeblich.

## 4. Werkstatt und Schnellstart bleiben eigenständig

Die ausführliche Werkstatt und der kompakte Schnellstart sind selbstständige Markdown-Arbeitsdateien. Sie müssen auch ohne installierte Nachbarskills einen nutzbaren Kernworkflow bieten. Sie werden nicht als zusätzliche Wrapper-Skills in das Plugin aufgenommen. Die [Promptübersicht](./werkstatt-und-schnellstart-coverage.md) enthält die einzelnen Downloads.

Längere Fachinformationen sind sinnvoll, wenn sie eine konkrete Entscheidung verbessern. Unnötige Vorabinterviews, parallele Vollprüfungen und das pauschale Laden aller Referenzen erhöhen dagegen den Aufwand. Die neue Auswahlstruktur reduziert solche Überschneidungen; tatsächliche Antwortzeit und automatische Auswahl hängen weiterhin von Oberfläche, Modell, Kontext und verfügbaren Werkzeugen ab.

## 5. Umfang der Prüfung

Die Auswahlprüfung erfasst Namen, sichtbare Titel und erreichbare Umstellungsziele im gesamten Marketplace. Gleichlautende Titel sind ein Anlass zur fachlichen Prüfung, kein automatischer Löschgrund. Die vertiefte Zusammenführung und Quellenprüfung dieser Runde betrifft die sechs oben genannten Bereiche. Das ist keine Behauptung, jede Rechtsaussage der gesamten Sammlung erneut vollständig verifiziert zu haben.

Manifestprüfungen und Navigationstests sichern technische Voraussetzungen ab. Sie ersetzen weder einen tatsächlichen Import in der verwendeten Oberfläche noch die fachliche Prüfung eines konkreten Arbeitsergebnisses.
