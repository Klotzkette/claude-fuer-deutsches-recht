---
name: spezial-bundesverfassungsgericht-livequellen-check
description: "Für Bundesverfassungsgericht: Livequellen-Check: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Bundesverfassungsgericht: Livequellen-Check

## Zweck des Skills

Dieser Skill wird aufgerufen, wenn ein Text bereits ein BVerfG-Zitat enthält oder ein solches benötigt. Er prüft, ob die Fundstelle echt, aktuell, richtig datiert und für die konkrete Aussage tragfähig ist.

## Normenanker

- § 31 BVerfGG für Bindungswirkung und Gesetzeskraft.
- § 30 BVerfGG für Entscheidung und Sondervotum.
- § 23 Abs. 1 BVerfGG für Begründungsanforderungen.
- § 92 BVerfGG für die Bezeichnung verletzter Rechte in der Verfassungsbeschwerde.
- § 93a BVerfGG für Annahmegründe.
- Art. 93 GG für die Verfahrenszuständigkeit.

## Livecheck

1. Suche zuerst auf bundesverfassungsgericht.de nach Aktenzeichen und Datum.
2. Prüfe, ob der Treffer die Entscheidung selbst oder nur eine Pressemitteilung ist.
3. Vergleiche Entscheidungsdatum, Veröffentlichungsdatum und Pressemitteilungsdatum.
4. Extrahiere Randnummer und tragenden Satz.
5. Prüfe, ob die Entscheidung noch gilt oder durch spätere Rechtsprechung präzisiert wurde.
6. Markiere, ob das Zitat eine Leitsatz-, Tenor-, Gründe- oder obiter-Stelle ist.

## Typischer Fehler

Bei neueren Entscheidungen wird oft das Veröffentlichungs- oder Pressemitteilungsdatum übernommen. Das ist falsch. Für Trojaner I und II lautet das Entscheidungsdatum jeweils 24.06.2025; die amtlichen Volltexte stehen unter den Aktenzeichen 1 BvR 2466/19 und 1 BvR 180/23.

## Output

Erzeuge eine Quellenkarte mit Gericht, Entscheidungsform, Datum, Aktenzeichen, URL, Randnummer, zitierfähigem Kernsatz und Übertragbarkeitsnotiz. Wenn keine tragfähige Quelle gefunden wird, schreibe ausdrücklich: "Nicht zitierfähig; Quelle fehlt oder trägt die Aussage nicht."
