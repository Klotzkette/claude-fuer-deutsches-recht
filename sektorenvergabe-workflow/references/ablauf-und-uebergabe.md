# 1. Elf Skills als übertragbare Arbeitsfolge

## 1.1. Zwei Abschnitte, eine Akte

Das Paket enthält fünf Schritte zur Unterlagenerstellung und fünf Schritte zur Durchführung/Überwachung. Der Hauptskill `sektorenvergabe-steuern` verbindet sie, muss aber nicht vor jeder Einzelaufgabe ausgeführt werden. Rügen und Nachprüfung sind Ereignisse, keine ausschließlich am Ende auftretenden Stationen. Es wird keine laufende Hintergrundüberwachung behauptet: Neue Nachrichten müssen bereitgestellt oder über eine ausdrücklich eingerichtete Verbindung abrufbar sein.

Die einzelnen `SKILL.md` enthalten Zweck, Eingaben, Arbeitsfolge, Normen/Entscheidungen, Ergebnis und Beispiel. Sie funktionieren ohne die optionale gemeinsame Referenzlektüre. In einer anderen Oberfläche kann jede Datei als eigene Arbeitsanweisung eingesetzt werden. YAML-Frontmatter identifiziert den Skill; falls ein Textfeld es nicht verarbeitet, nur den Markdown-Inhalt unterhalb des Frontmatters als Anweisung übernehmen. Es gibt keinen universellen Importstandard für sämtliche Anbieter.

## 1.2. Ein- und Ausgänge

| Schritt | Notwendiger Eingang | Auszugebendes Arbeitsprodukt | Fortsetzung |
| --- | --- | --- | --- |
| 1 Auftrag | Rechtsträger, Nutzung, Bedarf, Laufzeit/Optionen | Beschaffungsvermerk und Wertschätzung | 2; bei falschem Regime anderen Vergabeweg klären |
| 2 Leistung | Bestätigter Bedarf, Objekt-/Flächendaten, Betrieb | Leistungsbeschreibung, LV, Mengenbuch | 3; unklare Menge gezielt bestätigen lassen |
| 3 Bedingungen | Leistung, Lose, Risiko, Verfahrenswahl | Eignung, Kriterien, Vertragsentwurf | 4; betriebliche Entscheidung nachholen |
| 4 Abgleich | Sämtliche maßgeblichen Entwürfe | Bereinigte Fassungen und Freigabevermerk | 5; nach Veröffentlichung zusätzlich 7 |
| 5 Bekanntmachung | Freigabe, Plattform-/Organisationsdaten | Bekanntmachungsdaten, Fristen, Versandvorlage | 6 und ereignisbezogen 7 |
| 6 Eingang | Originaleinreichungen und Plattformprotokolle | Prüfvermerk und Nachforderung | 8; Einwand gegen Unterlagen zu 7 |
| 7 Einwände | Nachricht, angegriffene Fassung, Termine | Antwort, Abhilfe und Änderungsfassung | 2 bis 6 oder 8/9; bei Kammermitteilung 10 |
| 8 Wertung | Zulässige Angebote, Kriterien, Aufklärung | Wertung, Vergabevermerk, Zuschlagsvorschlag | 9; offener Fehler zu 7 |
| 9 Zuschlag | Freigabe, Gründe, Versand-/Sperrbelege | Vorabinformationen und Zuschlagsentwurf | Vertragsübergabe; bei Nachprüfung 10 |
| 10 Rechtsschutz | Antrag, Mitteilung, Vergabeakte, Rechtsstand | Stellungnahme und Fortsetzungsvorlage | Maßnahme nach Entscheidung, nicht blind zu 9 |

## 1.3. Minimale Übergabenotiz

Die Notiz ist internes Arbeitsmaterial, keine Pflichtgliederung des späteren Vergabevermerks:

```text
Projekt / Los:
Verfahrensbeginn und anzuwendender Rechtsstand:
Bearbeiteter Schritt:
Maßgebliche Dateien und Fassungen:
Fertiges Dokument / Bearbeitungsstand:
Getroffene Entscheidung und Beleg:
Noch offene Tatsache mit zuständigem Ansprechpartner:
Nächste Frist, Auslöser und Nachweis:
Nächster erforderlicher Schritt:
Externe Handlung / erforderliche Freigabe:
```

Nicht sämtliche Angebote in jede Stufe kopieren. Für eine Mengenberichtigung reichen regelmäßig betroffenes Objektbuch, LV, Preisblatt und letzte Bieterinformation. Vertrauliche Einzelangebotsinformationen nur der zuständigen Wertungs- oder Rechtsschutzbearbeitung übergeben. Bei fehlenden Dateien keine Abgeschlossenheit vortäuschen.

## 1.4. Startformulierungen

Unterlagen: „Die Objektliste und der Altvertrag sind freigegeben. Erstelle zuerst den Beschaffungsvermerk und danach die Reinigungsunterlagen. Frage nur nach Angaben, die du daraus nicht sicher ermitteln kannst. Veröffentliche nichts.“

Einzelschritt: „Nutze nur den Skill für Unterlagenabgleich. Maßgeblich sind LV 03 und Vertragsentwurf 02. Liefere die bereinigten Entwürfe und eine gesonderte Freigabenotiz.“

Fortsetzung: „Die Antwort zum Nachtzugang liegt jetzt vor. Übernimm sie in die offenen Positionen und prüfe anschließend die Fristfolgen. Wiederhole keine bereits abgeschlossene Aufnahme.“

Rechtsschutz: „Der Nachprüfungsantrag und die Mitteilung der Kammer sind hinzugekommen. Prüfe zunächst Rechtsstand, Zustellung und Zuschlagssperre. Bereite dann die Auftraggeberstellungnahme vor; reiche nichts ein.“

## 1.5. Grenzen

Markdown-Arbeitsanweisungen sind keine geprüfte technische Verbindung zu Vergabeplattformen, TED oder einem bestimmten Dokumentensystem. Es gibt keine Zusicherung automatischer Skill-Auswahl oder gleicher Modellleistung in jeder Oberfläche. Fehlende Werkzeuge werden offengelegt, Entscheidungen mit Rechts-/Tatsachenrisiko fachlich geprüft und externe Schritte ausdrücklich freigegeben. Die eingebaute Recherche- und Übergabelogik bleibt auch bei manueller Verwendung erhalten.
