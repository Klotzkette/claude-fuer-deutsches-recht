---
name: mietpreisueberhoehung-wistrg
description: "Mietpreisueberhoehung Wistrg: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mietpreisueberhoehung Wistrg

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mietpreisueberhoehung Wistrg** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mietpreisueberhoehung-wistrg-1954-mietwucher` | Prueft ueberhoehte Wohnraummiete dreistufig: Mietpreisbremse §§ 556d ff. BGB, Mietpreisueberhoehung § 5 WiStrG 1954 als Ordnungswidrigkeit und Mietwucher § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rueckforderungs- und Behoerdenpfad. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung als Ordnungswidrigkeit) und § 291 StGB (Mietwucher als Straftat). Erzeugt eine qualifizierte Rüge nach § 556g Abs. 2 BGB mit Berechnung der zulässigen Miete, Bezugnahme auf den amtlichen Mietspiegel und Aufforderung zur Rückzahlung. |
| `mietspiegel-quellen` | Operationalisiert die Prüfung der ortsueblichen Vergleichsmiete und der Mietpreisbremse anhand der mitgelieferten Referenz references/mietspiegel-quellen.md. Dieses Fachmodul greift, wenn für eine konkrete Adresse die ortsuebliche Vergleichsmiete, die Wohnlage, die Mietpreisbremse oder die Kappungsgrenze geprüft werden soll. Liefert ein strukturiertes Datenblatt für die Folgeskills mieterhoehung-prüfen-widersprechen und klageentwurf-amtsgericht. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **Mietpreisueberhoehung Wistrg**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mietpreisueberhoehung-wistrg-1954-mietwucher`

**Fokus:** Prueft ueberhoehte Wohnraummiete dreistufig: Mietpreisbremse §§ 556d ff. BGB, Mietpreisueberhoehung § 5 WiStrG 1954 als Ordnungswidrigkeit und Mietwucher § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rueckforderungs- und Behoerdenpfad.

# Mietpreisüberhöhung, WiStrG 1954 und Mietwucher

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietpreisüberhöhung, WiStrG 1954 und Mietwucher` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Einsatz

Dieses Fachmodul greift, wenn eine Wohnraummiete deutlich über der ortsüblichen Vergleichsmiete liegt oder der Nutzer Wörter wie "Mietwucher", "Mietpreisüberhöhung", "zu hohe Miete", "20 Prozent", "50 Prozent", "Wohnungsnot", "Zwangslage" oder "Anzeige gegen Vermieter" verwendet. Der Skill trennt sauber zwischen zivilrechtlicher Mietpreisbremse, ordnungswidrigkeitenrechtlicher Mietpreisüberhöhung und strafrechtlichem Wucher.

## Sofort klären

1. Geht es um **Wohnraum** oder Gewerberaum? § 5 WiStrG 1954 und § 291 Abs. 1 Nr. 1 StGB betreffen Wohnräume.
2. Wann wurde der Mietvertrag geschlossen und ab wann wurde die Miete gezahlt?
3. Welche Nettokaltmiete pro Quadratmeter, Wohnfläche, Lage, Ausstattung, Baujahr und Modernisierung sind belegt?
4. Gibt es einen amtlichen Mietspiegel oder andere belastbare Vergleichsmieten?
5. Gab es Wohnungsnot, drohende Obdachlosigkeit, Aufenthaltssicherung, Sprach-/Unerfahrenheitsprobleme oder andere Schwächesituationen?
6. Was ist das Ziel: Mietsenkung, Rückforderung, anwaltliches Schreiben, Anzeige, Bußgeldhinweis, Verteidigung des Vermieters?

## Dreistufige Prüfung

### 1. Mietpreisbremse §§ 556d ff. BGB

- Nur bei Wiedervermietung in einem Gebiet mit wirksamer Landesverordnung nach § 556d Abs. 2 BGB.
- Grundregel: höchstens 10 Prozent über ortsüblicher Vergleichsmiete, soweit keine Ausnahme greift.
- Ausnahmen und Korrekturen: Vormiete § 556e BGB, Modernisierung § 556e Abs. 2 BGB, Neubau und umfassende Modernisierung § 556f BGB.
- Rückforderung regelmäßig erst nach qualifizierter Rüge nach § 556g Abs. 2 BGB und nur im gesetzlichen Rahmen.

### 2. Mietpreisüberhöhung § 5 WiStrG 1954

§ 5 WiStrG 1954 ist keine Straftat, sondern eine Ordnungswidrigkeit. Der Skill darf daher nie automatisch von "Strafbarkeit" sprechen.

Prüfe:

1. **Entgelt für Wohnraum oder Nebenleistungen.**
2. **Unangemessen hohes Entgelt:** mehr als 20 Prozent über den üblichen Entgelten für vergleichbare Räume in der Gemeinde oder vergleichbaren Gemeinden.
3. **Vergleichszeitraum:** übliche Entgelte der letzten sechs Jahre, von Betriebskostenerhöhungen abgesehen.
4. **Ausnutzung eines geringen Angebots:** nicht jede hohe Miete genügt; die Mangellage muss konkret für die Preisbildung verwertet worden sein.
5. **Vorsatz oder Leichtfertigkeit.**
6. **Bußgeldrahmen:** bis 50.000 Euro nach § 5 Abs. 3 WiStrG 1954.
7. **Mehrerlös:** § 8 WiStrG 1954 sieht die Abführung des Mehrerlöses an das Land vor, soweit nicht aufgrund rechtlicher Verpflichtung zurückerstattet wurde.

### 3. Mietwucher § 291 StGB

§ 291 StGB ist die strafrechtliche Stufe. Sie verlangt mehr als eine überhöhte Miete.

Prüfe:

1. Vermietung von Wohnräumen oder Nebenleistungen nach § 291 Abs. 1 Nr. 1 StGB.
2. Auffälliges Missverhältnis zwischen Vermögensvorteil und Leistung.
3. Ausbeutung einer Zwangslage, Unerfahrenheit, eines Mangels an Urteilsvermögen oder erheblicher Willensschwäche.
4. Vorsatz hinsichtlich Schwächesituation, Missverhältnis und Ausbeutung.
5. Besonders schwerer Fall § 291 Abs. 2 StGB: wirtschaftliche Not des anderen durch die Tat, gewerbsmäßiges Handeln oder Wechselwucher.

## Abgrenzungsmatrix

| Spur | Schwelle | Zusatzelement | Rechtsfolge |
|---|---:|---|---|
| Mietpreisbremse §§ 556d ff. BGB | 10 Prozent über Vergleichsmiete | Gebiet mit Landesverordnung; keine Ausnahme | Rüge, Mietsenkung, Rückforderung |
| § 5 WiStrG 1954 | mehr als 20 Prozent über üblichen Entgelten | Ausnutzung geringen Angebots; Vorsatz oder Leichtfertigkeit | Ordnungswidrigkeit, Bußgeld, Mehrerlös |
| § 291 StGB | auffälliges Missverhältnis | Ausbeutung individueller Schwächesituation; Vorsatz | Straftat, Geldstrafe/Freiheitsstrafe, Einziehung/weitere Folgen |

## Beweis- und Unterlagenmatrix

- Mietvertrag, Staffelmiet-/Indexklauseln, Nachträge.
- Wohnfläche, Grundriss, Übergabeprotokoll, Fotos, Ausstattung, Modernisierungsbelege.
- Amtlicher Mietspiegel mit Lage-, Ausstattungs- und Baujahresmerkmalen.
- Vergleichsangebote nur als Indiz, nicht als Ersatz für amtliche Mietspiegelprüfung.
- Schriftverkehr zur Wohnungssuche, Absagen, Fristdruck, Sozial-/Jobcenter-/Aufenthaltsbezug.
- Zahlungen, Rückstände, Mahnungen, Nebenkostenpositionen.

## Output

Erstelle je nach Ziel:

- eine Mietpreis-Ampel mit `grün / gelb / rot`,
- eine Berechnungstabelle Vergleichsmiete / zulässige Miete / Ist-Miete,
- eine Rüge nach § 556g Abs. 2 BGB,
- ein behördentaugliches Hinweis- oder Anzeigeschreiben zu § 5 WiStrG 1954,
- eine strafrechtliche Ersteinschätzung zu § 291 StGB,
- oder ein Verteidigungsmemo für Vermieterseite mit Angriff auf Vergleichsmiete, Mangellage, Ausnutzung und Vorsatz.

## Quellen-Gate

- § 5 WiStrG 1954: https://www.gesetze-im-internet.de/wistrg_1954/__5.html
- § 8 WiStrG 1954: https://www.gesetze-im-internet.de/wistrg_1954/__8.html
- § 291 StGB: https://www.gesetze-im-internet.de/stgb/__291.html
- §§ 556d-556g BGB und § 558 BGB vor konkreter Ausgabe immer aktuell prüfen.
- Mietspiegel nur aus amtlicher Quelle verwenden; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle zitieren.

## 2. `mietsenkungsverlangen`

**Fokus:** Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung als Ordnungswidrigkeit) und § 291 StGB (Mietwucher als Straftat). Erzeugt eine qualifizierte Rüge nach § 556g Abs. 2 BGB mit Berechnung der zulässigen Miete, Bezugnahme auf den amtlichen Mietspiegel und Aufforderung zur Rückzahlung.

# Mietsenkungsverlangen (Mietpreisbremse, WiStrG 1954, Wucher)

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietsenkungsverlangen (Mietpreisbremse, WiStrG 1954, Wucher)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Disclaimer (Schlüsselstelle)

Mietsenkungsverlangen sind streitanfällig. Die Mietpreisbremse gilt nur in Gebieten mit Landesverordnung (§ 556d Abs. 2 BGB). Vor Versand der qualifizierten Ruege eine anwaltliche oder mietervereinsseitige Prüfung einholen. Fehlerhafte Ruegen können Anspruechen entgegengehalten werden.

## Workflow

### Schritt 1 — Anwendbarkeit der Mietpreisbremse

- Vertragsschluss **nach dem 1. Juni 2015** (§ 556d BGB ist seit dem 1. Juni 2015 in Kraft).
- Wohnung liegt in einem Gebiet mit Landesverordnung nach § 556d Abs. 2 BGB — Prüfung anhand `references/mietspiegel-quellen.md`.
- Verordnung zum Zeitpunkt des Vertragsschlusses gültig.

### Schritt 2 — Ausnahmen prüfen (§§ 556e und 556f BGB)

- **Vormiete** wenn höher, darf weitergegeben werden (§ 556e Abs. 1 BGB).
- **Modernisierung** nach § 556e Abs. 2 BGB.
- **Neubau** Erstbezug nach dem 1. Oktober 2014 ausgenommen (§ 556f Satz 1 BGB).
- **Umfassende Modernisierung** nach § 556f Satz 2 BGB ausgenommen.

### Schritt 3 — Zulässige Miete berechnen

- Ortsübliche Vergleichsmiete nach Mietspiegel ermitteln (Spanne, Einordnung).
- Zulässig: ortsübliche Vergleichsmiete plus **zehn Prozent** (§ 556d Abs. 1 BGB).
- Differenz zur tatsächlich gezahlten Miete berechnen.

### Schritt 4 — Qualifizierte Ruege (§ 556g Abs. 2 BGB)

- **Textform** ausreichend.
- **Tatsachen** angeben, auf denen die Beanstandung beruht (Mietspiegelwerte, Wohnlage, Ausstattung).
- **Rückforderung** erst ab Zugang der Ruege (§ 556g Abs. 1 Satz 3 BGB) — auf zu viel gezahlte Miete.

### Schritt 5 — Auskunftsanspruch (§ 556g Abs. 3 BGB)

- Mieter kann vom Vermieter Auskunft verlangen über Tatsachen, die für die Ausnahmen nach §§ 556e und 556f BGB massgebend sind.

### Schritt 6 — Mietpreisüberhöhung (§ 5 WiStrG 1954)

- **Mehr als 20 Prozent** über den üblichen Entgelten für vergleichbare Wohnräume bei **Ausnutzung eines geringen Angebots** (§ 5 Abs. 2 WiStrG 1954).
- Ordnungswidrigkeit, keine Straftat; Bußgeld bis 50.000 Euro (§ 5 Abs. 3 WiStrG 1954).
- Zusätzlich § 8 WiStrG 1954 prüfen: Abführung des Mehrerlöses an das Land, soweit nicht aufgrund rechtlicher Verpflichtung zurückerstattet wurde.

### Schritt 7 — Wucher (§ 291 StGB)

- **Auffälliges Missverhältnis** Miete zu Leistung **plus** Ausbeutung einer Zwangslage, Unerfahrenheit, Mangel an Urteilsvermögen oder erheblicher Willensschwaeche.
- Straftatbestand — Anzeige möglich, aber nur bei individueller Schwächesituation und vorsätzlicher Ausbeutung; bloß angespannter Wohnungsmarkt reicht dafür nicht.

## Schreiben-Entwurf

Strukturiere die Ruege in Abschnitte:

1. Bezeichnung als qualifizierte Ruege nach § 556g Abs. 2 BGB.
2. Sachverhalt (Mietvertrag, Mietsache, Datum, Höhe der Miete).
3. Gebiet der Mietpreisbremse mit Verordnung (Link).
4. Berechnung der ortsüblichen Vergleichsmiete mit Mietspiegelauszug.
5. Berechnung der zulässigen Miete (plus zehn Prozent).
6. Beanstandeter Mehrbetrag und Aufforderung zur Senkung sowie Rückzahlung ab Zugang.
7. Hilfsweise Hinweise auf § 5 WiStrG 1954 und § 291 StGB falls einschlägig.
8. **Disclaimer am Ende** — kein anwaltliches Schreiben, Empfehlung Rechtsrat einzuholen.

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

§§ 556d, 556e, 556f, 556g BGB — Mietpreisbremse und Rüge; § 5 WiStrG 1954 — Mietpreisüberhöhung; § 8 WiStrG 1954 — Abführung des Mehrerlöses; § 291 StGB — Wucher.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `mietspiegel-quellen`

**Fokus:** Operationalisiert die Prüfung der ortsueblichen Vergleichsmiete und der Mietpreisbremse anhand der mitgelieferten Referenz references/mietspiegel-quellen.md. Dieses Fachmodul greift, wenn für eine konkrete Adresse die ortsuebliche Vergleichsmiete, die Wohnlage, die Mietpreisbremse oder die Kappungsgrenze geprüft werden soll. Liefert ein strukturiertes Datenblatt für die Folgeskills mieterhoehung-prüfen-widersprechen und klageentwurf-amtsgericht.

# Mietspiegel-Quellen (amtlich)

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietspiegel-Quellen (amtlich)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill macht aus einer Mandantenadresse ein **strukturiertes Datenblatt zur ortsüblichen Vergleichsmiete**, mit dem die Folgeskills `mieterhoehung-pruefen-widersprechen`, `klageentwurf-amtsgericht`, `mieterhoehungsverlangen-erstellen` und `mietsenkungsverlangen` unmittelbar weiterrechnen können.

Die vollständige amtliche Quellensammlung steht in der mitgelieferten Referenz:

- [references/mietspiegel-quellen.md](../../references/mietspiegel-quellen.md) — Bundesweite Rechtsgrundlagen, 16 Bundesländer, 20 größte Städte, 25 Universitätsstädte.

## Wann diesen Skill verwenden

- Wenn die ortsübliche Vergleichsmiete für eine konkrete Adresse zu prüfen ist (Mieterhöhungsverlangen, Mietsenkungsverlangen, Klage auf Zustimmung zur Mieterhöhung).
- Wenn die Wohnlagen-Zuordnung (einfach, mittel, gut) anhand des amtlichen Straßenverzeichnisses benötigt wird.
- Wenn die Anwendbarkeit der Mietpreisbremse (§§ 556d ff. BGB), Kappungsgrenze (§ 558 Abs. 3 BGB) oder Kündigungssperrfrist (§ 577a BGB) im konkreten Bundesland geklärt werden muss.
- Wenn die Quellenangabe in einem Schreiben, Klageentwurf oder einer Beratung **amtlich** belegt werden soll (private Datenbanken sind im Zweifel nicht ausreichend).

## Sechs-Schritte-Workflow

### Schritt 1 — Adresse und Mietverhältnis erfassen

Pflichtangaben vom Nutzer:

- **Adresse** (Straße, Hausnummer, PLZ, Stadt).
- **Wohnfläche** in m² (laut Mietvertrag und/oder nach WoFlV gemessen).
- **Baujahr** des Gebäudes.
- **Mietverhältnis-Beginn** (für Mietpreisbremse-Anwendung und Kappungsgrenze-Zeitraum relevant).
- **Aktuelle Nettokaltmiete** (€/m² oder gesamt).
- **Frage**: geht es um Bestandsmiete (Erhöhung/Senkung) oder um Neuvermietung (Mietpreisbremse)?

Wenn etwas fehlt, einmal nachfragen — niemals raten.

### Schritt 2 — Bundesland und Stadt in der Referenz aufschlagen

In `references/mietspiegel-quellen.md`:

1. Bundesland-Abschnitt aufschlagen — landesweite Mietpreisbremse-, Kappungsgrenzen- und Kündigungssperrfrist-Verordnung notieren.
2. Stadt im Abschnitt "20 größte Städte" oder "25 Universitätsstädte" suchen. Wenn nicht enthalten: Bundesland-Sektion nutzen und die amtliche Stadtseite über die dort verlinkte Landesseite suchen.
3. Mietspiegel-Typ (qualifiziert nach § 558d BGB / einfach nach § 558c BGB) und Stand-Jahr ablesen.

Wenn das Stand-Jahr in der Referenz mit "Stand-Jahr bitte amtliche Stadtdokumente vor Ort prüfen" notiert ist: einmal die verlinkte amtliche Stadtseite öffnen und das aktuelle Stand-Jahr nachtragen — die Referenz ist Stand Mai 2026 und wird zu jedem Halbjahres-Release nachgepflegt.

### Schritt 3 — Wohnlage und Ausstattung ermitteln

1. **Wohnlagen-Zuordnung** über das amtliche Straßenverzeichnis / Geoportal der jeweiligen Stadt (Link in der Referenz pro Stadt). Ergebnis: einfache / mittlere / gute Wohnlage.
2. **Ausstattung erfassen** (Sondermerkmale nach jeweiligem Mietspiegel — typische Achsen): Bad (modernisiert/Standard/einfach), Küche (Einbauküche mitvermietet ja/nein), Heizung (Zentralheizung/Etagen/Ofen), Wohnung (Bodenbelag, Fenster, Balkon/Terrasse), Gebäude (Aufzug, Stellplatz/Garage).
3. Wenn Sondermerkmals-Bewertung unklar: an den Skill `lage-und-ausstattung-erheben` übergeben.

### Schritt 4 — Spanne und Mittelwert aus dem Mietspiegel ablesen

1. Tabelle aufschlagen (Größenklasse × Baujahresklasse × Wohnlage).
2. **Spannenwerte** (von / bis €/m²) und **Mittelwert** notieren.
3. Sondermerkmals-Zu- und -Abschläge in der Orientierungshilfe des jeweiligen Mietspiegels ablesen.
4. **Konkrete ortsübliche Vergleichsmiete** für diese Wohnung berechnen.

### Schritt 5 — Mietpreisbremse prüfen (nur Neuvermietung)

Nur, wenn das Mietverhältnis nach Inkrafttreten der einschlägigen Landes-Mietenbegrenzungsverordnung neu begründet wurde.

1. Liegt die Adresse in einem Gebiet mit "angespanntem Wohnungsmarkt" nach Landesverordnung? Verordnung aus der Referenz heraussuchen.
2. **Höchstmiete** = ortsübliche Vergleichsmiete (Schritt 4) + 10 % (§ 556d Abs. 1 BGB).
3. **Vormiete** (§ 556e BGB) und **Modernisierungs-Ausnahme** (§ 556e Abs. 2 BGB) und **Erstvermietung-nach-Neubau-Ausnahme** (§ 556f BGB, Baufertigstellung ab 01.10.2014 / umfassend modernisiert) prüfen — Ergebnis kann höher liegen als 10 % über ortsüblicher Vergleichsmiete.
4. Wenn die vereinbarte Miete die Höchstmiete übersteigt: Rüge nach § 556g Abs. 2 BGB ist erforderlich; die Folgeskills `mieteranfragen-beantworten` und `klageentwurf-amtsgericht` setzen darauf auf.

### Schritt 6 — Kappungsgrenze prüfen (nur Bestandsmiete)

Nur bei einer Mieterhöhung im Bestand nach § 558 BGB.

1. **Regelobergrenze**: 20 % in drei Jahren (§ 558 Abs. 3 Satz 1 BGB).
2. **Verschärfte Grenze**: 15 % in drei Jahren, wenn die Gemeinde durch Landesverordnung ("Kappungsgrenzenverordnung") als angespannt ausgewiesen ist (§ 558 Abs. 3 Satz 2 BGB). Verordnung aus der Referenz heraussuchen.
3. **Wartefrist** (§ 558 Abs. 1 Satz 2 BGB): 12 Monate seit der letzten Mieterhöhung und 15 Monate seit Mietbeginn.
4. **Begründungsmittel** (§ 558a Abs. 2 BGB): qualifizierter oder einfacher Mietspiegel, Sachverständigengutachten, drei Vergleichswohnungen.

## Übergabe-Datenblatt

Am Ende von Schritt 6 wird ein strukturiertes Datenblatt erzeugt, das die Folgeskills direkt lesen können:

```yaml
mietspiegel_pruefung:
 stand_der_pruefung: "JJJJ-MM-TT"

 adresse:
 strasse: ""
 hausnummer: ""
 plz: ""
 stadt: ""
 bundesland: ""

 wohnung:
 flaeche_qm: 0.0
 baujahr: 0
 wohnlage: "" # einfach | mittel | gut
 ausstattung:
 bad: ""
 kueche: ""
 heizung: ""
 bodenbelag: ""
 fenster: ""
 balkon_terrasse: ""
 aufzug: false
 stellplatz: false

 mietspiegel:
 quelle_url: ""
 typ: "" # qualifiziert | einfach
 stand_jahr: 0
 tabellen_zelle: "" # z. B. "60–80 qm, BJ 1949–1977, mittlere Wohnlage"
 spanne_von_eur_qm: 0.0
 spanne_bis_eur_qm: 0.0
 mittelwert_eur_qm: 0.0
 zuschlaege_abschlaege_eur_qm: 0.0
 ortsuebliche_vergleichsmiete_eur_qm: 0.0

 mietverhaeltnis:
 beginn: "JJJJ-MM-TT"
 aktuelle_nettokaltmiete_eur_gesamt: 0.0
 aktuelle_nettokaltmiete_eur_qm: 0.0
 neuvermietung_oder_bestand: "" # neuvermietung | bestand

 mietpreisbremse: # nur bei neuvermietung
 landesverordnung: ""
 angespannter_markt: false
 hoechstmiete_eur_qm: 0.0
 ausnahmen_geprueft: []

 kappungsgrenze: # nur bei bestand
 verschaerft_durch_landesverordnung: false
 obergrenze_prozent: 0 # 20 oder 15
 wartefrist_eingehalten: true

 ergebnis:
 bewertung: "" # zulaessig | unzulaessig | grenzfall
 differenz_eur_qm: 0.0
 naechster_schritt: "" # uebergabe an mieterhoehung-pruefen-widersprechen, klageentwurf-amtsgericht, etc.
```

## Gerechnetes Beispiel (zur Plausibilisierung)

**Sachverhalt:** Wohnung in München, Maxvorstadt, 78 m², Baujahr 1962, gute Wohnlage, modernisiertes Bad, Einbauküche mitvermietet, Zentralheizung, Aufzug, kein Stellplatz. Mietverhältnis seit 01.06.2018 (Bestand). Aktuelle Nettokaltmiete 1.150,00 € (= 14,74 €/m²). Der Vermieter verlangt Erhöhung auf 1.380,00 € (= 17,69 €/m², +20,0 %).

**Schritt 2** — Bayern hat eine Mietenbegrenzungsverordnung und eine Kappungsgrenzenverordnung. München ist ein angespannter Markt; Kappungsgrenze daher 15 %. Mietspiegel München: qualifiziert nach § 558d BGB, Stand 2025.

**Schritt 3** — Wohnlage "gut" (über das städtische Geoportal verifiziert). Ausstattung: drei Sondermerkmale erfüllt (mod. Bad, EBK, Aufzug).

**Schritt 4** — Tabellenzelle "70–90 m², Baujahr 1949–1977, gute Wohnlage" Mittelwert (illustrativ) 15,80 €/m², Spanne 13,40–17,20 €/m². Sondermerkmals-Zuschlag (illustrativ) +0,90 €/m². Ortsübliche Vergleichsmiete für diese Wohnung: **ca. 16,70 €/m²**.

**Schritt 6** — Kappungsgrenze: 14,74 €/m² × 1,15 = **16,95 €/m²** (verschärfte 15-%-Grenze in München). Die verlangte Miete von 17,69 €/m² übersteigt die Kappungsgrenze. Ergebnis: **unzulässig** in der Höhe. Maximal zulässig wären rechnerisch 16,70 €/m² (Vergleichsmiete) bzw. 16,95 €/m² (Kappungsgrenze), Untergrenze gewinnt → **ca. 16,70 €/m² = 1.302,60 € Gesamtmiete**.

Der Skill übergibt an `mieterhoehung-pruefen-widersprechen` mit `ergebnis.bewertung: "unzulaessig"`, `differenz_eur_qm: -0,99`, `naechster_schritt: "Teilzustimmung bis 16,70 €/m², Widerspruch im Übrigen"`.

**Die Zahlen sind illustrativ.** Die tatsächlichen Spannenwerte sind vor der Mandantenkommunikation aus dem aktuellen amtlichen Mietspiegel München abzulesen.

## Was dieser Skill bewusst NICHT tut

- **Keine Anwendung privater Datenbanken** (Conny, immowelt, immoscout). Auch wenn diese methodisch den gleichen Datenpool nutzen, ersetzen sie keine amtliche Quelle.
- **Keine eigenständige Wohnflächen-Messung.** Wenn die Wohnflächenangabe im Mietvertrag streitig ist, an `lage-und-ausstattung-erheben` übergeben.
- **Keine Sachverständigenbewertung.** Wenn der einschlägige Mietspiegel nicht qualifiziert ist oder bestritten wird, kommt § 558a Abs. 2 Nr. 3 BGB (Sachverständigengutachten) oder Nr. 4 BGB (drei Vergleichswohnungen) ins Spiel — das ist ein eigener Workflow.
- **Keine Index- oder Staffelmiete.** Bei Index- oder Staffelmietverträgen gilt der Mietspiegel nicht direkt — eigene Anspruchsgrundlage in §§ 557a, 557b BGB.

## Disclaimer

Diese Quellensammlung ersetzt keine Rechtsberatung. Sie ist ein Werkzeug zur Recherche amtlicher Quellen. Vor jeder Verwendung den Aktualitätsstand auf der jeweiligen amtlichen Seite prüfen. Die Letztverantwortung für die Anwendung im Einzelfall liegt beim Anwalt.

## Aktueller Gesetzgebungsstand zur Mietpreisbremse (Bund)

- **Verlängerungsgesetz vom 17.07.2025** — BGBl. 2025 I Nr. 163. § 556d Abs. 2 Satz 4 BGB wurde dahingehend geaendert, dass die Ermächtigung der Landesregierungen zum Erlass von Mietpreisbremse-Verordnungen bis zum 31.12.2029 verlängert wurde. Ohne diese Verlängerung wären die Landesverordnungen spätestens Ende 2025 ausgelaufen. Verfassungsgerichtliche Pruefung dieses Verlaengerungsgesetzes 2025 steht zum Stand Mai 2026 noch aus.
- **BVerfG, Nichtannahmebeschluss vom 08.01.2026 – Az. 1 BvR 183/25** — Wichtige Klarstellung: Diese Entscheidung betrifft **nicht** das Verlaengerungsgesetz 2025, sondern die **vorangegangene Verlaengerung von 2020** (§ 556d BGB in der Fassung vom 19.03.2020) sowie mittelbar die Berliner Mietenbegrenzungsverordnung vom 19.05.2020. Die Verfassungsbeschwerde einer Berliner Wohnungsgesellschaft blieb erfolglos. Das BVerfG haelt an seiner Linie aus 1 BvL 1/18 vom 18.07.2019 fest: §§ 556d ff. BGB sind mit Art. 14 GG vereinbar; die Mietpreisbremse stellt keinen unverhaeltnismaessigen Eingriff in die Eigentumsgarantie dar.
- **Folgerung fuer das 2025er Gesetz**: Der Beschluss bestaetigt zwar die generelle verfassungsrechtliche Tragfaehigkeit der Mietpreisbremse-Konstruktion, traegt das 2025er Verlaengerungsgesetz jedoch nicht ausdruecklich mit. Aussagen wie "die Verlaengerung bis 2029 ist bereits verfassungsrechtlich gepruefte" sind unzutreffend; richtig ist nur, dass die Argumentationslinie aus 1 BvL 1/18 und 1 BvR 183/25 auf das 2025er Gesetz uebertragbar erscheint.
- **Praxisfolge**: Für Neuvermietungen ab dem 01.01.2026 in Bundesländern mit Mietpreisbremse-Verordnung gilt die Begrenzung auf 110 Prozent der ortsueblichen Vergleichsmiete fort. Vor Beratung pruefen, ob die jeweilige Landesverordnung selbst noch in Kraft ist oder verlängert wurde — die Bundesregelung ermächtigt nur, sie verpflichtet nicht.
- Quellen: BGBl. 2025 I Nr. 163 — https://www.recht.bund.de/bgbl/1/2025/163 ; BVerfG, Beschluss vom 08.01.2026 – 1 BvR 183/25 — https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2026/01/rk20260108_1bvr018325.html

## Aktuelle Rechtsprechung — Leitsaetze Mietspiegel

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---
<!-- AUDIT 27.05.2026 -->
