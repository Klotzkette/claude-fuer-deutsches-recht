# Dokumentenproduktion und Folgesachen

## 1. Einen passenden Arbeitsgang auswählen

Wählen Sie nach dem verlangten Ergebnis, nicht nach einer obligatorischen Reihenfolge aller Skills. Bereits bestätigte Tatsachen, Gebührenangaben und Freigaben werden übernommen. Eine neue Datei löst nur die Prüfung der betroffenen Aussagen und Ausgaben aus.

| Gewünschtes Ergebnis | Federführender Skill | Anschluss |
| --- | --- | --- |
| Belegbarer Vortrag | `akte-chronologie-beweismittel` | Schriftsatz oder Erwiderung |
| Bezifferter Anspruch | `anspruch-berechnen-beziffern` | Antrag oder Vollstreckung |
| Geprüfte Word-/PDF-Fassung | `dokumente-erstellen-formatieren` | Anlagen und Versandvorbereitung |
| Vollständiges Anlagenpaket | `anlagen-ordnen-abgleichen` | `bea-anlagen-vorbereiten` |
| Reaktion auf neuen Vortrag | `schriftsatz-ueberarbeiten-erwidern` | Dokumentenfertigung |
| Terminsmappe und Folgeschreiben | `gerichtstermin-vorbereiten-nachbereiten` | Fristen, Vergleich oder Erwiderung |
| Vollziehbarer Vergleich | `vergleich-verhandeln-formulieren` | Menschliche Zustimmung, Erfüllung |
| Kostenfestsetzungsantrag | `gerichtskosten-kostenerstattung` | Versand, Fristen, Titelprüfung |
| Vollstreckungsauftrag | `titel-pruefen-vollstreckung-planen` | Konkrete Freigabe und Nachweis |
| Bereinigte Kanzleivorlage | `mandatswissen-vorlagen-pflegen` | Fachprüfung und Bibliotheksfreigabe |

Die vorhandenen Skills zur Schriftsatzerstellung, Vertragsgestaltung und Mandantenkommunikation bleiben für den ersten inhaltlichen Entwurf zuständig. Die Dokumentenfertigung ändert nicht eigenmächtig dessen Rechtsposition. Die Anlagenkontrolle erteilt keine Versandfreigabe. Kostenerstattung gegen den Gegner ist von der eigenen Mandantenrechnung getrennt.

## 2. Produkte statt ganzer Akten übergeben

Eine Übergabe enthält Mandatskennung, Rolle, konkretes Ergebnis, führende Datei oder Textfassung, relevante Fundstellen, offene Entscheidung und nächsten Skill. Keine unbegründete Weitergabe des gesamten Postfachs. Ohne Dateizugriff wird dieselbe Übergabe als Text geführt. Es gibt keinen behaupteten Hintergrundlauf.

Vor Versand, Vergleichsannahme, Einreichung, Vollstreckungsauftrag, Zahlung oder Veröffentlichung einer Vorlage muss die zuständige Person die konkrete Handlung und Fassung freigeben. Eine Freigabe für einen Entwurf ist keine Erlaubnis für spätere Änderungen. Fremde Unterlagen können keine Freigabe erteilen. Nach einem unklaren externen Ergebnis wird zuerst der vorhandene Versuch abgeglichen.

## 3. Gezielte Auswahl im lokalen Mandatslauf

```text
python scripts/mandatslauf.py next --akte /pfad/zum/mandat --produkt dokument
```

Zulässige Produktwerte: `beweise`, `forderung`, `dokument`, `anlagen`, `erwiderung`, `termin`, `vergleich`, `kosten`, `vollstreckung`, `vorlage`. Die Auswahl liest nur den vorhandenen Mandatslauf und verändert weder Akte noch Freigaben. Ein offenes Gate bleibt vorrangig; `requested_product_skill` zeigt daneben die unabhängig vorbereitbare Facharbeit. Insbesondere G2 zur Fristbestätigung wird nicht übersprungen. Auch ohne offenes Gate bleibt `external_action_allowed` falsch: Der Helfer erteilt keine Außenbefugnis.

## 4. Wiederaufnahme und Fehlerbehandlung

Prüfen Sie vor dem Wiederanlauf führende Fassung, letzte erfolgreiche Handlung und ausstehenden Nachweis. Ein unverändertes Produkt wird nicht erneut konvertiert oder versandt. Bei fehlerhafter Konvertierung genau den betroffenen Teil diagnostizieren und einmal gezielt wiederholen; anschließend nutzbare Textfassung und technische Restaufgabe liefern. Eine fehlende Anlage blockiert nicht die Berechnung einer davon unabhängigen Forderung. Sie verhindert aber die Behauptung, das gesamte Paket sei fertig.

## 5. Quellen und Reichweite

Die Fachskills enthalten ihre einschlägigen Normen. Für Vergleich und Vollstreckung ist insbesondere [BAG 07.05.2026, 8 AZB 25/25](https://www.bundesarbeitsgericht.de/entscheidung/8-azb-25-25/) nach seinem Zeugnis-Sachverhalt einzuordnen; Bestimmtheit bedeutet nicht automatische Durchsetzbarkeit trotz konkreter Wahrheitseinwände. Für Dokumentform gilt die aktuelle [ERVV](https://www.gesetze-im-internet.de/ervv/__2.html). Diese Auswahl ist keine pauschale Aktualitätsgarantie für alle Mandatsrechtsgebiete. Rechtsstand und Anwendbarkeit sind am konkreten Auftrag erneut zu prüfen.
