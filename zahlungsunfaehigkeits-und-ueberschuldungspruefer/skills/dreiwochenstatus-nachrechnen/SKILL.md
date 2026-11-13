---
name: dreiwochenstatus-nachrechnen
description: "Berechnet den stichtagsbezogenen Status und die Liquiditätslücke aus Aktiva I, Aktiva II, Passiva I und Passiva II. Prüft Tagesverlauf, Zehnprozentregel, ihre beiden Ausnahmen und alternative Darlegungswege."
---

# 1. Liquiditätsbilanz und Dreiwochenrechnung nach § 17 InsO

## 1.1. Zweck und Anwendungsfall

Rechne die objektive Zahlungsfähigkeit am benannten Tag nach. Mache Ergebnis, Anknüpfungstatsachen und Grenzen der verwendeten Methode sichtbar.

## 1.2. Eingaben

Arbeite mit belegten Beträgen in einheitlicher Währung, eindeutiger Cut-off-Zeit, Datum und Fundstelle. Übernimm die Einzelposten aus den Prüfungen der Mittel und Verbindlichkeiten. Vermerke fehlende Gläubigergruppen und den Datenstand.

## 1.3. Ablauf

1. Rechne Status am Stichtag mit Aktiva I und Passiva I. Für die zeitraumbezogene Liquiditätsbilanz erfasse Aktiva II und Passiva II ab dem Folgetag bis einschließlich des 21. Kalendertags nach dem Stichtag. Dokumentiere bei entscheidenden gleichzeitigen Ereignissen den Zeitpunkt oder einen belastbaren Alternativlauf.
2. Berechne im Fenster `Lücke = max(0, PI + PII − AI − AII)`. Verwende für die Quote den Nenner `PI + PII`. Bei vollständig belegtem Nenner null bleibt die Quote ohne Wert. Bei fehlenden Positionen gilt der Status nur bedingt. Prüfe die Quote ungerundet, runde lediglich die Darstellung. Weise bei Bedarf den Verlauf je Tag aus, damit eine aggregierte Summe Zahlungsengpässe vor einem späteren Eingang sichtbar lässt.
3. Grenze die innerhalb von drei Wochen behebbare Stockung ab. Bleibt eine Lücke unter zehn Prozent, spricht das regelmäßig für Zahlungsfähigkeit. Prüfe aber, ob eine kurzfristige Überschreitung der Schwelle bereits absehbar ist. Ab zehn Prozent spricht der Regelfall für Zahlungsunfähigkeit. Die Ausnahme erfordert mit an Sicherheit grenzender Wahrscheinlichkeit baldige vollständige oder nahezu vollständige Schließung und zumutbares Zuwarten.
4. Für eine alternative Darlegung nach II ZR 112/21 lege den Stichtagsstatus mit tagesgenauem Finanzplan oder eine aussagekräftige Folge tagesgenauer Status vor. Begründe Abdeckung, tatsächliche Lückenentwicklung und wesentliche Zwischenereignisse. Der Zeitraum dient der Bewertung des Stichtags und bildet keine gesetzliche Wartefrist.
5. Rechne begründete Varianten für streitige Fälligkeit, Zugriff und verspätete Zuflüsse. Halte offen, welche Variante aufgrund der verfügbaren Belege trägt.

## 1.4. Quellenpflicht

BGH IX ZR 123/04, Leitsätze und PDF-S. 13–18, BGH II ZR 88/16 Rn. 50–62 und BGH II ZR 112/21 Rn. 12–17. Trenne von der gesetzlichen Vermutung des § 17 Abs. 2 Satz 2 InsO. Die [amtliche Quellenübersicht](../../references/insolvenzreife-quellen.md) führt zu Normen und Volltexten. Zitiere nur fallbezogen geprüfte Fundstellen und nenne Belegdatei und Stelle für jede entscheidende Tatsache.

## 1.5. Ausgabeformat

Gib Cut-off, Fensterende, vier Summen, anfängliche Lücke, Fensterlücke, Nenner und Quote mit Rechnung an. Füge eine Subsumtion zu Ausnahmen und den wesentlichen Tagesbewegungen an. Liefere den Vermerk in vollständigen Sätzen und mit dezimaler Gliederung. Für formatierten Export verwende soweit technisch möglich Times New Roman, 11 pt.

## 1.6. Beispiel

Aktiva I 90.000 EUR, Aktiva II 45.000 EUR, Passiva I 100.000 EUR, Passiva II 50.000 EUR ergeben 15.000 EUR Lücke bei 150.000 EUR Passiva. Genau zehn Prozent liegen im Regelfall der Zahlungsunfähigkeit. Prüfe, ob eine belegte Ausnahme greift.
