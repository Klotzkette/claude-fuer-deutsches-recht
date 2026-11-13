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

6. Kennzeichne eine rein rechnerische Unterdeckung als solche, solange vollständige Passiva, rechtzeitige Verfügbarkeit oder die Ausnahmen nicht geprüft sind. Weise den Betrag einer offenen Position und beide Ergebnisvarianten aus. Bei weniger als zehn Prozent im Fenster darf ein eigenständig tragfähiger Nachweis der Zahlungseinstellung nicht stillschweigend verworfen werden. Prüfe den scheinbaren Widerspruch anhand der Tage und Quellen.
7. Speichere neben der Ergebnisdarstellung die normalisierten Einzelposten mit Belegstellen. Lege für jede Änderung fest, ob sie einen Betrag, eine Fälligkeit oder einen Ansatzgrund betrifft. Eine spätere Stundung wirkt nur nach ihrer rechtlichen Reichweite und ihrem Zeitpunkt; der Nutzer muss die alte und die neue Rechnung vergleichen können.
## 1.4. Quellenpflicht

Prüfe § 17 Abs. 2 Satz 1 InsO. Halte die gesetzliche Vermutung nach Satz 2 als eigenständigen Nachweisweg getrennt.

- [BGH, Urteil vom 28. Juni 2022 – Az. II ZR 112/21, Rn. 12–17](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2021/II_ZR_112-21.pdf?__blob=publicationFile&v=1).
- [BGH, Urteil vom 19. Dezember 2017 – Az. II ZR 88/16, Rn. 50–62](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2016/II_ZR__88-16.pdf?__blob=publicationFile&v=1).
- [BGH, Urteil vom 24. Mai 2005 – Az. IX ZR 123/04, PDF-S. 7–10 und 13–18 sowie Leitsätze](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2004/IX_ZR_123-04.pdf?__blob=publicationFile&v=1).

Die [amtliche Quellenübersicht](../../references/insolvenzreife-quellen.md) ordnet die Volltexte und ihre Grenzen ein. Zitiere nur fallbezogen geprüfte Fundstellen. Nenne für jede entscheidende Tatsache die Belegdatei und genaue Stelle.

## 1.5. Ausgabeformat

Gib Cut-off, Fensterende, vier Summen, anfängliche Lücke, Fensterlücke, Nenner und Quote mit Rechnung an. Füge eine Subsumtion zu Ausnahmen und den wesentlichen Tagesbewegungen an. Liefere den Vermerk gemäß der Ausformulierungspflicht in vollständigen Sätzen. Skelette, Halbsätze und reine Aufzählungen ersetzen kein Endprodukt. Der Formatstandard ist Times New Roman, 11 pt, soweit technisch möglich, mit ausschließlich dezimaler Gliederung. Die Quellenprüfung folgt den im Repository geltenden Regeln aus `references/zitierweise.md`: verifizierte Rechtsprechung mit Datum, Aktenzeichen und genauer Stelle, Literatur nur aus bereitgestellter oder tatsächlich zugänglicher Quelle.

## 1.6. Beispiel

Aktiva I 90.000 EUR, Aktiva II 45.000 EUR, Passiva I 100.000 EUR, Passiva II 50.000 EUR ergeben 15.000 EUR Lücke bei 150.000 EUR Passiva. Genau zehn Prozent liegen im Regelfall der Zahlungsunfähigkeit. Prüfe, ob eine belegte Ausnahme greift.
