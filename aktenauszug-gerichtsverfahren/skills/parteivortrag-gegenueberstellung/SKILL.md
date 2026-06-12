---
name: parteivortrag-gegenueberstellung
description: "Erstellt eine Tabelle mit zwei Spalten (Klägerseite und Beklagtenseite) für streitige Sachverhaltsangaben Punkt für Punkt. Jeder Streitpunkt wird als eigene Zeile gegenübergestellt. Fundstellen in Schriftsaetzen werden angegeben. Keine Wertung welcher Vortrag zutreffend ist. Maßstab §§ 138 286..."
---

# Parteivortrag — Gegenüberstellung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Liegt bereits ein gerichtlicher Hinweis vor, was das Gericht für streitig und entscheidungserheblich hält?
2. Hat das Gericht einen Beweisbeschluss erlassen? (Streitpunkte sind dann für Gericht bereits benannt)
3. Welche Schriftsätze liegen vor? Klageerwiderung, Replik, Duplik?
4. Gibt es Präklusionsrisiken (§§ 296, 531 ZPO) durch verspäteten Vortrag?

## Zentrale Normen

- § 138 ZPO — Erklärungspflicht über Tatsachen des Gegners (Wahrheitspflicht, substantiiertes Bestreiten)
- § 286 ZPO — Freie Beweiswürdigung; Grundlage für Identifikation der streitigen Punkte
- § 296 Abs. 1 ZPO — Präklusion verspäteten Vortrags in erster Instanz
- § 531 Abs. 2 ZPO — Beschränktes Vorbringen neuer Angriffs- und Verteidigungsmittel in der Berufungsinstanz
- § 139 ZPO — Richterliche Hinweispflicht; Gericht weist auf Lücken im Vortrag hin

## Rechtsprechung zum Parteivortrag und Bestreiten

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Tabellenstruktur

```markdown
| Streitpunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| [Bezeichnung des Streitpunkts] | [Vortrag Kläger] | [Vortrag Beklagter] |
```

## Kategorien von Streitpunkten

- Vertragsinhalt (Leistungsumfang, Preis, Nebenabreden)
- Tatsächliche Leistungserbringung (wer hat was wann geliefert / erbracht)
- Mängel (ob Mangel vorliegt, wessen Ursache)
- Kenntnis und Verschulden
- Schaden und Schadenshöhe
- Vorgerichtliche Kommunikation (wer hat was gesagt)
- Fristen und Termine (Vereinbartes Lieferdatum etc.)

## Beispiel

| Streitpunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| Leistungsumfang | Auftrag umfasste vollständige Schlüsselübergabe inkl. Einweisung (K 1 Bl. 12) | Einweisung war nicht vereinbart sondern nur Lieferung (B 1 Bl. 40) |
| Mangel Dach | Dach war bei Abnahme undicht nachweislich Wassereintritt im Oktober (K 4 Bl. 26) | Undichtigkeit erst durch unsachgemäße Nutzung entstanden (B 3 Bl. 50) |
| Verschulden | Beklagte kannte Mangel und schwieg (K 5 Bl. 29) | Kein Arglistvorwurf; Mangel war nicht erkennbar (B 4 Bl. 53) |
| Schadenshöhe | Schaden EUR 45.000 belegt durch Gutachten (K 8 Bl. 60) | Überhöhte Schadensberechnung; tatsächlicher Schaden unter EUR 15.000 (B 6 Bl. 65) |

## Unstreitige Punkte

Unstreitige Sachverhaltselemente werden unterhalb der Tabelle als Block "Unstreitiger Sachverhalt" aufgeführt. Sie fließen nicht in die Streitpunkt-Tabelle ein.

## Hinweise

- Pro Zeile genau ein Streitpunkt — nicht mehrere Punkte in einer Zelle
- Vortrag neutral wiedergeben (paraphrasieren, nicht werten)
- Fundstelle in Schriftsatz oder Anlage angeben
- Wenn eine Partei zu einem Punkt schweigt: "Kein Vortrag" in die entsprechende Zelle
- Keine Prognose welcher Vortrag zutrifft

## Qualitätscheck

- [ ] Alle wesentlichen Streitpunkte erfasst?
- [ ] Keine Wertung enthalten?
- [ ] Fundstellen angegeben?
- [ ] Unstreitiger Sachverhalt separat ausgewiesen?
- [ ] Präkludierte Punkte (§§ 296 531 ZPO) als solche markiert?

<!-- AUDIT 27.05.2026 bundle_055
Halluzinations-Reparatur: BGH VII ZR 131/13 (WRONG_TOPIC) korrigiert.
Echtes Thema laut dejure.org: Anforderungen an die Bestimmtheit eines Architektenvertrages
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Beschreibung entsprechend angepasst.
-->
