---
name: ampel-zahlen-schwellenwerte-berechnung
description: "Berechnet Status, Bilanzlücke und operativen Finanzierungsbedarf. Verhindert die Gleichsetzung von Tabellenfarben und Insolvenzgründen."
---

# 1. Liquiditätskennzahlen berechnen und rechtlich einordnen

## 1.1. Zweck und Anwendungsfall

Berechne die beauftragten Kennzahlen aus belegten Zahlungsdaten und erkläre ihre Aussagegrenzen. Eine Ampel darf operativen Handlungsbedarf oder Prüfstatus anzeigen; sie stellt keine Insolvenzreife fest. Den tatsächlichen Auftrag und vorhandene Zahlen zuerst bearbeiten.

## 1.2. Eingaben

Erforderlich sind Gesellschaft, Stichtag, betrachteter Zeitraum, freie Mittel, Kreditverfügbarkeit und einzeln belegte Verpflichtungen/Zuflüsse mit Fälligkeits- und Zahlungstag. Fehlende Werte bleiben unbekannt. Leere Eingaben liefern weder eine Nullquote noch Entwarnung. Eine bestätigte Null ausdrücklich von einem leeren Feld unterscheiden. Bei OCR Vorzeichen, Dezimalstellen, Salden und Belegstelle prüfen.

## 1.3. Berechnung und Einordnung

Ein reiner Stichtagsstatus vergleicht AI mit PI. Die zeitraumbezogene Dreiwochenbilanz vergleicht AI+AII mit PI+PII. Das gesamte kalendergenaue Fenster berücksichtigen, einschließlich neuer Fälligkeiten der ersten Woche. Zahlungen auf alte PI nicht nochmals als neue PII erfassen. Für die Bilanzmethode gilt `Lücke=max(0,PI+PII−AI−AII)` und `Quote=Lücke/(PI+PII)` bei positivem Nenner. Bei null keine Quote berechnen. Die eigene Forderung wird nicht durch Titulierung zur verfügbaren Liquidität; auf der Passivseite Titel und Vollstreckung getrennt prüfen.

Die operative Wochenrechnung lautet `Endbestand=Anfangsbestand+Einzahlungen−Auszahlungen`. Endbestand in die nächste Periode übernehmen, unterwöchige Engpässe sichtbar machen. Finanzierung und operativen Cashflow trennen. Ein negativer Bestand bezeichnet Bedarf. Freie Linien nicht doppelt zählen, geplante Stundungen nicht als bereits wirksam behandeln. Eine nur teilweise vorhandene Folgeperiode nicht als vollständigen Dreiwochentest ausgeben.

Wende die [Prüfregeln](../../references/insolvenzpruefung.md) an: Unter zehn Prozent regelmäßig Zahlungsfähigkeit, aber keine Entwarnung bei absehbarer erheblicher Vergrößerung; ab zehn Prozent regelmäßig Zahlungsunfähigkeit mit der eng begrenzten Ausnahme baldiger fast vollständiger Schließung und zumutbaren Zuwartens. Die Dreiwochenbetrachtung ist keine Warteerlaubnis. Ein einziges starkes Indiz kann Zahlungseinstellung tragen; die Anzahl angekreuzter Hinweise entscheidet nicht. Gegenindizien würdigen.

Für § 18 InsO in aller Regel 24 Monate, für § 19 InsO zwölf Kalendermonate und gegebenenfalls einen eigenständigen Überschuldungsstatus prüfen. Weder ein 110-Prozent-Puffer noch ein hypothetischer Worst Case entscheidet den Tatbestand. Positive Fortbestehensprognose, operative Deckung und nachhaltige Sanierungsfähigkeit nicht gleichsetzen. Sofortige Krisenprüfung bei konkreten Signalen, ohne eine vollständige idealtypische Tabelle abzuwarten.

## 1.4. Quellenpflicht

[Entscheidungskarte](../../references/rechtsprechung/INDEX.md): BGH IX ZR 123/04, Leitsätze b/c; II ZR 88/16, Rn. 50–62; IX ZR 48/21, Rn. 27–33; II ZR 112/21, Rn. 12–16. Für Prognose/Rangrücktritt II ZR 84/20 und IX ZR 133/14; Grenzen und heutige Normen beachten. Keine Literatur- oder IDW-Fundstellen aus Modellwissen.

## 1.5. Ausgabeformat

Zeige Formel, Einzelwerte, Nenner, Zeitraum, Annahmen, fehlende Daten und Ergebnis getrennt. Liefere einen vollständig ausformulierten Rechen-/Prüfvermerk, wenn beauftragt; keine Stichwortskelette. Times New Roman 11 pt für formatierte Texte, dezimale Gliederung. Keine Insolvenzfreigabe aus einem grünen Rechenfeld. Bei Datenlücken konkrete Rückfrage und belastbaren Zwischenstand liefern; nach Antwort aktualisieren.

## 1.6. Kontrollbeispiel

Bank 0 EUR, innerhalb eines belegten Fensters rechtzeitiger Eingang 100 EUR und danach neue Fälligkeit 100 EUR, keine Altschulden: AI0+AII100 gegen PI0+PII100 ergibt keine Bilanzlücke. Fällt die Zahlung erst nach der Fälligkeit an, ist der vorherige Engpass zusätzlich zu untersuchen. Sind die Angaben lediglich in derselben KW zusammengefasst, darf rechtzeitige Deckung nicht behauptet werden.
