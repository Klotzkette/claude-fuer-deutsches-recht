---
name: pfueb-arbeitsentgelt
description: "Für PfÜB Arbeitsentgelt: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# PfÜB Arbeitsentgelt

## Arbeitsbereich

Der Gläubiger will Arbeitseinkommen beim Arbeitgeber als Drittschuldner pfänden. Erst Titel, Klausel und Zustellung, dann Arbeitgeberbezeichnung, Forderungsumfang, unpfändbare Bezüge, Zusammenrechnung, Unterhaltspflichten und die vom 1. Juli 2026 bis 30. Juni 2027 geltende Tabelle prüfen. Output ist ein einreichungsfähiger Pfändungs- und Überweisungsantrag mit gesondertem Berechnungsblatt.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Titel + Klausel + Zustellung grün
- Arbeitgeber bekannt (sonst `vermoegensauskunft-gv`)
- Schuldner nicht in Insolvenz

## Rechtsgrundlagen

- §§ 829, 835 ZPO – Pfändung und Überweisung
- § 850 ZPO – Pfändbarkeit von Arbeitseinkommen
- § 850a ZPO – unpfändbare Bezüge (50 % Mehrarbeit, voll Urlaubsgeld, Weihnachten bis Hälfte des Monatsverdienstes, Aufwand)
- Paragraf 850c ZPO und Pfändungsfreigrenzenbekanntmachung 2026: aktuelle Tabelle ab 1. Juli 2026
- § 850d ZPO – privilegierte Unterhaltsforderungen, abweichende Berechnung
- § 850e ZPO – Zusammenrechnung mehrerer Einkommen
- § 850f ZPO – Erhöhung des Freibetrags durch Vollstreckungsgericht
- Paragraf 850k sowie Paragrafen 899 ff. ZPO: nur für den anschließenden Kontoschutz, nicht für die Berechnung beim Arbeitgeber
- § 87 InsO bei laufender Insolvenz

## Workflow

1. **Drei-Säulen-Prüfung**.
2. **Arbeitgeber als Drittschuldner** bezeichnen – nicht "die Firma X", sondern die juristische Person.
3. **Forderung** definieren: laufendes Arbeitseinkommen, einschließlich künftiger Erhöhungen, einschließlich Sonderzuwendungen soweit pfändbar.
4. Pfändbaren Betrag mit `werkzeuge/pfaendungsrechner.py` nach der Tabelle ab 1. Juli 2026 berechnen; Nettoeinkommen, berücksichtigte gesetzliche Unterhaltspflichten und gerichtliche Abweichungen dokumentieren.
5. **Privilegierte Unterhaltsforderung** § 850d ZPO: deutlich niedrigerer Freibetrag, vom Vollstreckungsgericht festzusetzen.
6. **Antragsformular** ZVFV nutzen. Ab 1.10.2026 neue Muster und XML-Antrag möglich.
7. **Einreichen** beim Vollstreckungsgericht am Schuldnerwohnsitz.
8. **Zustellung** an Arbeitgeber durch Gerichtsvollzieher (Papier) oder elektronisch.
9. **Drittschuldnererklärung § 840 ZPO** abwarten.
10. **Anschlusspfändung** prüfen, wenn weitere Gläubiger pfänden (Rangfrage § 804 Abs. 3 ZPO).

## Pfändungstabelle ab 1. Juli 2026

Die Pfändungsfreigrenzenbekanntmachung 2026 gilt vom 1. Juli 2026 bis 30. Juni 2027. Paragraf 850c Absatz 4 ZPO sieht eine jährliche Anpassung zum 1. Juli vor. Aktuelle Werte stehen im Werkzeug; die amtliche Tabelle ist vor Einreichung gegenzulesen.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Qualitätsgates

- Niemals Bruttoeinkommen pfänden – pfändbar ist der Nettoteil.
- Niemals Sonderzuwendungen § 850a ZPO ohne Prüfung in den pfändbaren Teil rechnen.
- Bei mehreren Einkommen (Lohn + Rente, Lohn + Selbstständigkeit) Zusammenrechnung § 850e ZPO ausdrücklich beantragen.
- Bei privilegierten Unterhaltsforderungen § 850d ZPO eigene Festsetzung beantragen.
- Bei Sterbe-/Krankengeld besondere Pfändbarkeitsgrenzen prüfen.
