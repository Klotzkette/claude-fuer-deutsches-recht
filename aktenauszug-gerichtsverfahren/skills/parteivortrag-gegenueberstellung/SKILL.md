---
name: parteivortrag-gegenueberstellung
description: "Parteivortrag Gegenueberstellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Parteivortrag Gegenueberstellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Parteivortrag Gegenueberstellung** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `parteivortrag-gegenueberstellung` | Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und Beklagtenseite) für streitige Sachverhaltsangaben Punkt für Punkt. Jeder Streitpunkt wird als eigene Zeile gegenübergestellt. Fundstellen in Schriftsaetzen werden angegeben. Keine Wertung welcher Vortrag zutreffend ist. Massstab §§ 138 286 ZPO. |
| `rechtsargumente-gegenueberstellung` | Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einreden Verjährungsthema und Pinpoint-Zitate aus Rechtsprechung (BGH OLG EuGH). Keine Wertung welches Argument ueberzeugt. Normen §§ 195-218 BGB Verjährung §§ 280 ff. BGB Schadensersatz. |
| `sachverhaltschronologie` | Erstellt eine chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen: Vertragsschluss Vorfaelle vorgerichtliche Korrespondenz Schadensereignisse und Behoerdenakte. Datum fett vorangestellt knappe Beschreibung ohne Wertung. Fundstellen in der Akte werden angegeben. Normen §§ 145-157 BGB Vertragsschluss §§ 280 631 BGB. |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Parteivortrag Gegenueberstellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `parteivortrag-gegenueberstellung`

**Fokus:** Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und Beklagtenseite) für streitige Sachverhaltsangaben Punkt für Punkt. Jeder Streitpunkt wird als eigene Zeile gegenübergestellt. Fundstellen in Schriftsaetzen werden angegeben. Keine Wertung welcher Vortrag zutreffend ist. Massstab §§ 138 286 ZPO.

# Parteivortrag — Gegenüberstellung

## Zweck

Die Parteivortrag-Tabelle stellt streitige Sachverhaltsangaben der Kläger- und der Beklagtenseite Punkt für Punkt gegenüber. Sie ermöglicht dem Anwalt, auf einen Blick zu erkennen, was tatsächlich streitig ist und was als unstreitig gilt.

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

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## 2. `rechtsargumente-gegenueberstellung`

**Fokus:** Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einreden Verjährungsthema und Pinpoint-Zitate aus Rechtsprechung (BGH OLG EuGH). Keine Wertung welches Argument ueberzeugt. Normen §§ 195-218 BGB Verjährung §§ 280 ff. BGB Schadensersatz.

# Rechtsargumente — Gegenüberstellung

## Zweck

Die Rechtsargumenten-Tabelle stellt die juristischen Positionen beider Parteien gegenüber. Sie zeigt, auf welche Anspruchsgrundlagen, Einwendungen, Einreden und Rechtsprechungsnachweise sich die Parteien berufen.

## Triage — kläre vor Erstellung

1. Welche Anspruchsgrundlagen benennt die Klägerseite explizit?
2. Welche Einwendungen und Einreden erhebt die Beklagtenseite?
3. Ist Verjährung im Raum? (§§ 195-218 BGB — regelmässig 3 Jahre ab Jahresende Entstehung/Kenntnis)
4. Zitieren die Parteien konkrete BGH- oder OLG-Entscheidungen?

## Zentrale Normen (Ansprüche und Einreden)

- §§ 280-285 BGB — Schadensersatz (Pflichtverletzung, Schuldverhältnis, Verschulden)
- §§ 195-218 BGB — Verjährung (regelmässig 3 Jahre §195 BGB; Hemmung §§ 203-211; Neubeginn § 212)
- § 254 BGB — Mitverschulden
- §§ 387-396 BGB — Aufrechnung
- §§ 273-274 BGB — Zurückbehaltungsrecht
- §§ 633-634a BGB — Mängelhaftung Werkvertrag; §§ 434-442 BGB — Kaufrechtliche Mängel
- §§ 305-310 BGB — AGB-Kontrolle (Einbeziehung, unangemessene Benachteiligung)

## Rechtsprechung zu Anspruchsgrundlagen und Einreden

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Tabellenstruktur

```markdown
| Rechtspunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| [Rechtsfrage] | [Position / Norm / Zitat Kläger] | [Position / Norm / Zitat Beklagter] |
```

## Kategorien

### Anspruchsgrundlagen

Welche Norm stützt das Klagebegehren? Welche Gegennorm beruft die Beklagte?

### Einwendungen (rechtshindernde / rechtsvernichtende)

Mängel der Anspruchsvoraussetzungen, Rücktritt, Aufrechnung, Unmöglichkeit.

### Einreden (rechtshemmende)

Verjährung, Zurückbehaltungsrecht, Stundung.

### Schadensrecht

Kausalität, Mitverschulden (§ 254 BGB), Schadenshöhe.

### Rechtsprechung

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiel

| Rechtspunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| Anspruchsgrundlage | § 634 Nr. 4 i.V.m. § 280 Abs. 1 BGB (Schadensersatz wegen Mangel) | Kein Mangel i.S.d. § 633 BGB; Abnahme erfolgte vorbehaltlos |
| Wirksamkeit Abnahme | Abnahme unter Vorbehalt gem. § 640 Abs. 1 S. 2 BGB | Abnahmeprotokoll ohne Vorbehalt unterzeichnet |
| Verjährung | Frist läuft noch; Fristbeginn erst mit Kenntnis des Mangels | Verjährungsfrist von zwei Jahren ab Abnahme (§ 634a Abs. 1 Nr. 1 BGB) bereits abgelaufen |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Schadenshöhe | Volle Kosten der Mängelbeseitigung nach § 635 BGB (EUR 45.000) | § 254 BGB: Mitverschulden wegen unterlassener Wartung mindert Anspruch |

## Umgang mit Rechtsprechung

- Nur in Schriftsätzen zitierte Entscheidungen aufnehmen
- Aktenzeichen und Entscheidungsdatum angeben
- Tenor oder tragende Aussage kurz paraphrasieren
- Keine eigene Rechtsprechungsrecherche im Aktenauszug — nur Wiedergabe des Parteivortrags

## Qualitätscheck

- [ ] Alle Anspruchsgrundlagen der Klägerseite erfasst?
- [ ] Alle Einwendungen und Einreden der Beklagtenseite erfasst?
- [ ] Verjährungsthema behandelt (falls relevant) — §§ 195-218 BGB?
- [ ] Rechtsprechungszitate mit Aktenzeichen und Datum?
- [ ] Keine eigene Rechtsbewertung enthalten?
- [ ] Mitverschulden § 254 BGB erwogen?

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- VI ZR 62/22: ersatzlos entfernt — kein Eintrag auf dejure.org (NOT_FOUND)
- VI ZR 136/20: ersatzlos entfernt — WRONG_TOPIC; reale Entscheidung 05.10.2021 betrifft Feststellungsklage VW-Abgasskandal (NJW-RR 2022, 23), nicht Verjährungsbeginn § 199 BGB; beanspruchte NJW 2022, 53 existiert nicht in dejure
- VI ZR 282/17: ersatzlos entfernt — kein Eintrag auf dejure.org (NOT_FOUND)
- VI ZR 259/17: ersatzlos entfernt — kein Eintrag auf dejure.org (NOT_FOUND)

## 3. `sachverhaltschronologie`

**Fokus:** Erstellt eine chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen: Vertragsschluss Vorfaelle vorgerichtliche Korrespondenz Schadensereignisse und Behoerdenakte. Datum fett vorangestellt knappe Beschreibung ohne Wertung. Fundstellen in der Akte werden angegeben. Normen §§ 145-157 BGB Vertragsschluss §§ 280 631 BGB.

# Sachverhaltschronologie

## Zweck

Die Sachverhaltschronologie listet alle wesentlichen außerprozessualen Ereignisse in zeitlicher Reihenfolge auf. Sie unterscheidet sich von der Verfahrenschronologie dadurch, dass sie ausschließlich materielle Tatsachen erfasst — also Ereignisse aus dem Leben des Rechtsverhältnisses selbst, nicht die prozessualen Schritte.

## Triage — kläre vor Erstellung

1. Liegt der Vertragsschluss klar dokumentiert vor? (Angebot § 145 BGB + Annahme § 147 BGB)
2. Gibt es widersprüchliche Datumsangaben in den Schriftsätzen der Parteien?
3. Existieren Behördenbescheide oder Protokolle, die in die Chronologie einzupflegen sind?
4. Welcher Zeitraum ist rechtserheblich? (Verjährungsfrist nach §§ 195-218 BGB beachten)

## Zentrale Normen (materiell-rechtlicher Hintergrund)

- §§ 145-157 BGB — Vertragsschluss (Angebot, Annahme, Vertragsinhalt)
- §§ 280-285 BGB — Schadensersatz wegen Pflichtverletzung
- §§ 631-651 BGB — Werkvertrag (Errichtung, Abnahme, Mängelhaftung)
- §§ 433-442 BGB — Kaufvertrag (Übergabe, Mängelrechte)
- §§ 195-199 BGB — Verjährung und Verjährungsbeginn (Kenntnis von Anspruch und Person)
- § 307 BGB — Unwirksame AGB-Klauseln die Rechte des Vertragspartners beschneiden

## Rechtsprechung zur Sachverhalts-Dokumentation und Vertragsschluss

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Was gehört hinein

- Vertragsschlüsse, Angebote, Annahmen
- Leistungserbringung oder Nichtleistung
- Mängelrügen, Mahnungen, Zahlungen
- Schadensereignisse (Unfälle, Lieferausfälle, Datenverluste)
- Vorgerichtliche Korrespondenz (Schreiben, E-Mails, Protokolle)
- Behördliche Bescheide, Genehmigungen, Prüfprotokolle
- Verhandlungen und Einigungsversuche
- Kündigung oder Rücktritt
- Alle sonstigen tatsächlichen Handlungen, die für den Rechtsstreit erheblich sind

## Was nicht hinein gehört

- Schriftsätze, Klageschrift, Erwiderungen (→ Verfahrenschronologie)
- Gerichtstermine, Beschlüsse, Urteile (→ Verfahrenschronologie)
- Rechtliche Bewertungen

## Formatvorgabe

```
- **TT.MM.JJJJ** [Kurzbeschreibung des Ereignisses] (Fundstelle: [Anlage / Blatt])
```

## Beispiele

```
- **15.03.2021** Abschluss des Werkvertrags über Errichtung einer Lagerhalle für EUR 850.000 (K 1 Bl. 12-18)
- **02.09.2021** Übergabe der Lagerhalle durch Auftragnehmer; Abnahmeprotokoll unterzeichnet (K 3 Bl. 22-24)
- **14.10.2021** Schriftliche Mängelrüge des Auftraggebers wegen Undichtigkeit des Dachs (K 4 Bl. 26)
- **08.11.2021** Nachbesserungsversuch des Auftragnehmers; Mangel nach Vortrag des Auftraggebers nicht beseitigt (B 2 Bl. 45)
- **03.01.2022** Androhung des Rücktritts per anwaltlichem Schreiben (K 5 Bl. 30)
- **15.02.2022** Erklärung des Rücktritts vom Werkvertrag (K 6 Bl. 33)
```

## Arbeitsschritte

1. Alle Urkunden und Schriftsätze auf tatsächliche Ereignisse durchsehen
2. Jedes Ereignis mit Datum und Kurzbeschreibung erfassen
3. Chronologisch sortieren (ältestes Ereignis zuerst)
4. Fundstelle in der Akte hinzufügen (Anlagebezeichnung und Blattangabe)
5. Doppelte Nennungen zusammenführen
6. Wertende Formulierungen streichen
7. Verjährungsrelevante Ereignisse markieren (Beginn Frist §§ 195-199 BGB)

## Umgang mit unklaren Daten

- Ungenaues Datum: "ca. [Monat JJJJ]" oder "zwischen [Datum] und [Datum]"
- Datum nicht bekannt: "[Zeitraum unbekannt, nach Aktenlage ca. ...]"
- Widersprüchliche Daten in den Schriftsätzen: beide Versionen nennen und Partei angeben

## Qualitätscheck

- [ ] Alle wesentlichen außerprozessualen Ereignisse erfasst?
- [ ] Chronologisch sortiert?
- [ ] Datum fettgedruckt?
- [ ] Fundstelle angegeben?
- [ ] Keine prozessualen Schritte enthalten?
- [ ] Keine Wertung?
- [ ] Verjährungsrelevante Ereignisse besonders markiert?

---
