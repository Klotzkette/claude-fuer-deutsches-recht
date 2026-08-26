---
name: pfaendungstabelle-pfueb-arbeitsentgelt
description: "Für Pfändungstabelle ab 1. Juli 2026: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Pfändungstabelle ab 1. Juli 2026

## Arbeitsbereich

Bei einer Lohn- oder Rentenpfändung den pfändbaren Betrag nach der vom 1. Juli 2026 bis 30. Juni 2027 geltenden Bekanntmachung berechnen. Vor der Zahl immer Einkommensart, Bereinigungspositionen nach Paragraf 850e ZPO, unpfändbare Bezüge nach Paragraf 850a ZPO, tatsächlich gewährten gesetzlichen Unterhalt und eine gerichtliche Anordnung prüfen. P-Konto-Schutz nach Paragrafen 899 und 902 ZPO und privilegierte Unterhaltspfändung nach Paragraf 850d ZPO sind getrennte Rechenwege.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Handelt es sich um Arbeitseinkommen (§ 850c ZPO) oder selbstständiges Einkommen (§ 850i ZPO)?
2. Wie viele unterhaltsberechtigte Personen sind zu berücksichtigen?
3. Handelt es sich um privilegierte Unterhaltspfändung (§ 850d ZPO) oder reguläre Pfändung?
4. Hat der Schuldner ein P-Konto? Dann Einrichtung nach Paragraf 850k ZPO, Sockel nach Paragraf 899 ZPO, bescheinigte Erhöhungen nach Paragrafen 902 und 903 ZPO sowie Nachzahlungen gesondert erfassen.

## Zentrale Normen

- § 850a ZPO — Unpfändbare Bezüge (Sonderzuwendungen, Aufwandsentschädigungen)
- § 850c ZPO — Pfändungsfreigrenze (Tabelle, jährlich angepasst)
- § 850d ZPO — privilegierte Unterhaltspfändung (geringerer Selbstbehalt)
- § 850f ZPO — Erhöhung durch Gericht aus persönlichen Gründen
- § 850i ZPO — Pfändung bei selbstständigem Einkommen
- Paragraf 850k ZPO: Einrichtung und Beendigung des Pfändungsschutzkontos
- Paragrafen 899, 902 bis 906 ZPO: Sockelbetrag, Erhöhungsbeträge, Nachweis und gerichtliche Festsetzung

## Startet bei

- Lohnpfändung in Vorbereitung (`pfueb-arbeitsentgelt`)
- Kontopfändung mit P-Konto-Berechnung (`pfueb-bank` + § 850k ZPO)
- Schuldnerseite verlangt Anpassung der Freibeträge (`abwehr-schuldner`)

## Rechtsgrundlagen

- § 850c ZPO – Pfändungsfreigrenze für Arbeitseinkommen
- § 850d ZPO – Unterhaltsforderungen (privilegiert, geringerer Freibetrag, vom Gericht festgesetzt)
- § 850f ZPO – Erhöhung durch Gericht aus persönlichen Gründen
- Paragraf 850k sowie Paragrafen 899, 902 bis 906 ZPO: P-Konto, Grundbetrag, Erhöhungen und gerichtliche Festsetzung
- Pfändungsfreigrenzenbekanntmachung 2026 vom 19. März 2026, BGBl. 2026 I Nr. 80, in Kraft vom 1. Juli 2026 bis 30. Juni 2027
- Amtliche Quelle: https://www.gesetze-im-internet.de/pf_ndfreigrbek_2026/
- Nächste Anpassung zum 1. Juli 2027 nach Paragraf 850c Absatz 4 ZPO

## Gültigkeit der aktuellen Tabelle

Die Bekanntmachung gilt vom 1. Juli 2026 bis 30. Juni 2027. Das Werkzeug warnt in den letzten dreißig Tagen und sperrt keine Berechnung, kennzeichnet nach Fristablauf aber jede Ausgabe unübersehbar als veraltet. Vor Verwendung in einem Antrag sind Tagesdatum und amtliche Tabelle abzugleichen.

## Eckwerte (aus Tabelle, dezimal mit Punkt)

Aktuelle Eckdaten (Tabelle 1. Juli 2026 bis 30. Juni 2027, BGBl. 2026 I Nr. 80):

- Grundfreibetrag ohne Unterhaltspflichten: 1.587,40 Euro netto monatlich.
- Erhöhung für die erste berücksichtigte Person: 597,42 Euro.
- Erhöhung für jede weitere Person bis zur fünften: 332,83 Euro.
- Vollpfändungsgrenze: 4.866,30 Euro; nur der Mehrbetrag ist vollständig pfändbar.
- Für die Tabellenberechnung wird der Betrag bis zur Vollpfändungsgrenze nach Paragraf 850c Absatz 5 ZPO auf volle zehn Euro abgerundet; der Mehrbetrag über 4.866,30 Euro bleibt centgenau hinzuzurechnen.
- P-Konto-Grundbetrag nach Paragraf 899 Absatz 1 ZPO: 1.590,00 Euro; Erhöhungen setzen die Tatbestände und Nachweise der Paragrafen 902 und 903 ZPO voraus.
- Centbeträge folgen der amtlichen Tabelle; keine pauschale Abrundung des Endergebnisses.
- Alle exakten Werte im `werkzeuge/pfaendungsrechner.py` (Single Source of Truth).

Die Werte sind im Werkzeug zentral hinterlegt; dieses Dokument nennt sie zur Sichtkontrolle. Die amtliche Tabelle bleibt für den konkreten Antrag maßgeblich.

## Workflow

1. **Inputs einholen**: Nettoeinkommen, Anzahl unterhaltsberechtigter Personen, ggf. Sonderzuwendungen, Privileg § 850d ZPO ja/nein.
2. **Python-Werkzeug aufrufen**: `python zwangsvollstreckung/werkzeuge/pfaendungsrechner.py --netto 2500 --unterhalt 1`.
3. **Output**: Freibetrag, pfändbarer Betrag, Pfändungsstufen, Hinweise zu § 850a ZPO Sonderzuwendungen.
4. Paragraf 850d ZPO: nur mit einem konkret begründeten oder gerichtlich festgesetzten Selbstbehalt rechnen, etwa `--privileg --selbstbehalt 1500`; das Werkzeug setzt keinen Pauschalwert ein.
5. P-Konto: Grundbetrag nach Paragraf 899 ZPO und nachgewiesene Erhöhungen nach Paragrafen 902 und 903 ZPO getrennt ausgeben.
6. **Antragstext** für den PfÜB ergänzen.

## Privilegierte Unterhaltspfändung § 850d ZPO

- Der notwendige Unterhalt wird vom Vollstreckungsgericht fallbezogen belassen. Die unterhaltsrechtlichen Selbstbehalte der Düsseldorfer Tabelle dürfen nicht ohne Begründung als Vollstreckungsfreibetrag übernommen werden.
- Ohne konkreten Eingabewert verweigert das Werkzeug die privilegierte Berechnung.

## P-Konto-Schutz § 850k ZPO – Erhöhungen

Erhöhungen müssen durch Bescheinigung (Schuldnerberatung, anerkannter Berater, Arbeitgeber, Familienkasse, Sozialleistungsträger) belegt werden:

- pro unterhaltsberechtigter Person
- Kindergeld
- einmalige Sozialleistungen
- Nachzahlungen

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Qualitätsgates

- Keine abgelaufene Tabelle als aktuellen Rechtsstand verwenden.
- Niemals Bruttobetrag in die Tabelle einsetzen.
- Niemals § 850d ZPO ohne richterliche Festsetzung als feste Zahl ausgeben.
- Bei selbstständigem Einkommen Berechnung § 850i ZPO statt § 850c ZPO.
- Bei Sozialleistungen § 54 SGB I prüfen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
