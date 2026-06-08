---
name: grundsteuerwert-bewertung-bewg-218ff
description: "Grundsteuerwert nach BewG §§ 218 ff. prüfen: Bundesmodell, Ertragswert, Sachwert, Bodenrichtwert, Grundstücksart, Steuermesszahl, Hauptfeststellung 01.01.2022, Fehlerdiagnose und Bescheidbegründung."
---

# Grundsteuerwert: Bewertung nach BewG §§ 218 ff.

## Fachlicher Anker

- **Normen:** §§ 218, § 6a, § 218.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Aufgabe

Prüfe den Grundsteuerwertbescheid im Bundesmodell. Dieser Skill arbeitet nicht als Rechner ohne Unterlagen, sondern als Bewertungsdiagnose: Welche Eingabe bestimmt den Wert, welche ist falsch, welche ist nur belastend, aber rechtlich vorgesehen?

## Prüfschritte

1. **Anwendungsbereich**: Bundesmodell oder Landesmodell? Bei Landesmodell an `anw-grundsteuer-landesmodell-routing` abgeben.
2. **wirtschaftliche Einheit**: Grundstück, Betrieb der Land- und Forstwirtschaft, Wohnungs-/Teileigentum, Erbbaurecht.
3. **Bewertungsverfahren**: Ertragswertverfahren oder Sachwertverfahren.
4. **Datenbasis**: Bodenrichtwert, Fläche, Grundstücksart, Baujahr, Wohn-/Nutzfläche, statistische Nettokaltmiete, Mietniveaustufe, Restnutzungsdauer.
5. **Messbetrag**: Steuermesszahl und mögliche Ermäßigungen im Messbescheid gesondert prüfen.
6. **Gemeinderolle**: Hebesatz erst im Grundsteuerbescheid.

## Fehlerbilder

- Objekt ist kein reines Wohnobjekt, wurde aber so behandelt.
- Gewerbefläche, Lager oder Atelier wurde falsch als Wohnfläche erfasst.
- Bodenrichtwertzone passt nicht zur Lage oder zum Stichtag.
- Denkmalschutz oder sozialer Wohnungsbau wurde nicht berücksichtigt.
- Baujahr/Kernsanierung verzieht Restnutzungsdauer.
- Einheiten wurden wegen gemeinsamer Zufahrt oder Tiefgarage falsch zusammengefasst.

## Begründungsstruktur

Arbeite in dieser Reihenfolge:

1. angefochtener Bescheid mit Datum und Aktenzeichen,
2. konkrete falsche Besteuerungsgrundlage,
3. richtiger Wert und Beleg,
4. rechtliche Relevanz für BewG/GrStG,
5. Antrag auf Änderung beziehungsweise Einspruchsziel.

## Output

- Bewertungsfehler-Matrix.
- Priorisierte Angriffspunkte.
- Entwurf eines Beleganschreibens.
- Kurzer Einspruchsbaustein.
- Hinweis, ob zusätzlich gemeiner Wert/gutachterlicher Nachweis geprüft werden soll.

## Quellen

Gesetzestext vor Ausgabe öffnen: BewG §§ 218 ff., GrStG, ggf. amtliche Grundsteuer-Hinweise. Keine Kommentarzitate ohne Nutzerquelle.

## Norm-Bezug konkret

- § 218 BewG: Verfahrensgliederung Grundsteuerwert.
- § 219 BewG: Feststellung des Grundsteuerwerts auf den Hauptfeststellungszeitpunkt 01.01.2022.
- §§ 243-247 BewG: unbebaute Grundstücke (Bodenwertverfahren mit Bodenrichtwert).
- §§ 248-260 BewG: bebaute Grundstücke - Ertragswertverfahren (Wohnen) und Sachwertverfahren (Geschäft, gemischte Nutzung, Sonderfälle).
- § 257 BewG: Liegenschaftszinssätze typisiert nach Grundstücksart.
- § 15 GrStG: Steuermesszahlen (regelmäßig 0,31 ‰ für Wohnen, 0,34 ‰ für Nichtwohnen, Ermäßigungen z. B. für sozialen Wohnungsbau, Denkmal).

## Praktischer Tipp

- ELSTER-Erklärung hat den Wert getrieben. Erste Diagnose: hat Mandant Wohnflächen "geschätzt" angegeben? Häufige Falle: Dachgeschoss zur Wohnfläche dazugerechnet, obwohl < 1 m Schräge nach Wohnflächenverordnung gar nicht zählt.
- Mietniveaustufe (Anlage 39 BewG für die jeweilige Gemeinde) prüfen; Großstadt-Mandanten landen oft in Stufe 6, obwohl der konkrete Stadtteil deutlich darunter liegt - hier ist eine Anpassung nicht ohne Weiteres möglich, aber bei Mischlagen Vergleichsbeleg sammeln.
- Liegenschaftszinssatz ist typisiert - kein Angriffspunkt für den Einzelfall, nur über den Modellangriff. Real angreifbar sind: Wohnfläche, Grundstücksfläche, Bodenrichtwert (über die Zonenzugehörigkeit, ggf. Vergleich mit Auskunft des Gutachterausschusses), Baujahr (Kernsanierung wird oft als Neubau eingetragen).

## Trade-off: Welche Fehlerklasse zuerst angreifen?

| Fehlerart | Hebel | Aufwand |
|---|---|---|
| Wohnfläche falsch | direkt änderbar bei Beleg | Wohnflächenberechnung anfertigen lassen (ca. 300-600 EUR) |
| Bodenrichtwertzone falsch | hoher Hebel | Gutachterausschussauskunft (oft kostenpflichtig 50-150 EUR) |
| Grundstücksart falsch | hoher Hebel über Steuermesszahl | Teilungserklärung, Bauakte |
| gemeiner Wert deutlich niedriger | Eilverfahrenshebel über BFH II B 78/23 / II B 79/23 | Belegtreppe, ggf. Gutachten - Bewertungsstichtag 01.01.2022 (Quellen live auf bundesfinanzhof.de verifizieren) |

Empfehlung: Erst niedrigwertige Belege (Wohnflächenberechnung, Bodenrichtwertauskunft) sammeln, dann gezielt einsetzen.

## Typische Fehler

- Einspruch trifft den falschen Bescheid: Hebesatz angegriffen, obwohl der Wertfehler im Grundlagenbescheid (Finanzamt) sitzt. § 351 Abs. 2 AO sperrt den Folgebescheid.
- Einspruchsfrist von einem Monat wird übersehen, weil der Bescheid an die ELSTER-Postfachadresse zugestellt und nicht abgerufen wurde; § 122 Abs. 2a AO regelt elektronische Bekanntgabe nach drei Tagen.
