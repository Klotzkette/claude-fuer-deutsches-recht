---
name: mietspiegel-quellen
description: "Operationalisiert die Pruefung der ortsueblichen Vergleichsmiete und der Mietpreisbremse anhand der mitgelieferten Referenz references/mietspiegel-quellen.md. Nutze diesen Skill, wenn fuer eine konkrete Adresse die ortsuebliche Vergleichsmiete, die Wohnlage, die Mietpreisbremse oder die Kappungsgrenze geprueft werden soll. Liefert ein strukturiertes Datenblatt fuer die Folgeskills mieterhoehung-pruefen-widersprechen und klageentwurf-amtsgericht."
---

# Mietspiegel-Quellen (amtlich)

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
2. Stadt im Abschnitt „20 größte Städte" oder „25 Universitätsstädte" suchen. Wenn nicht enthalten: Bundesland-Sektion nutzen und die amtliche Stadtseite über die dort verlinkte Landesseite suchen.
3. Mietspiegel-Typ (qualifiziert nach § 558d BGB / einfach nach § 558c BGB) und Stand-Jahr ablesen.

Wenn das Stand-Jahr in der Referenz mit „Stand-Jahr bitte amtliche Stadtdokumente vor Ort prüfen" notiert ist: einmal die verlinkte amtliche Stadtseite öffnen und das aktuelle Stand-Jahr nachtragen — die Referenz ist Stand Mai 2026 und wird zu jedem Halbjahres-Release nachgepflegt.

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

1. Liegt die Adresse in einem Gebiet mit „angespanntem Wohnungsmarkt" nach Landesverordnung? Verordnung aus der Referenz heraussuchen.
2. **Höchstmiete** = ortsübliche Vergleichsmiete (Schritt 4) + 10 % (§ 556d Abs. 1 BGB).
3. **Vormiete** (§ 556e BGB) und **Modernisierungs-Ausnahme** (§ 556e Abs. 2 BGB) und **Erstvermietung-nach-Neubau-Ausnahme** (§ 556f BGB, Baufertigstellung ab 01.10.2014 / umfassend modernisiert) prüfen — Ergebnis kann höher liegen als 10 % über ortsüblicher Vergleichsmiete.
4. Wenn die vereinbarte Miete die Höchstmiete übersteigt: Rüge nach § 556g Abs. 2 BGB ist erforderlich; die Folgeskills `mieteranfragen-beantworten` und `klageentwurf-amtsgericht` setzen darauf auf.

### Schritt 6 — Kappungsgrenze prüfen (nur Bestandsmiete)

Nur bei einer Mieterhöhung im Bestand nach § 558 BGB.

1. **Regelobergrenze**: 20 % in drei Jahren (§ 558 Abs. 3 Satz 1 BGB).
2. **Verschärfte Grenze**: 15 % in drei Jahren, wenn die Gemeinde durch Landesverordnung („Kappungsgrenzenverordnung") als angespannt ausgewiesen ist (§ 558 Abs. 3 Satz 2 BGB). Verordnung aus der Referenz heraussuchen.
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
    wohnlage: ""        # einfach | mittel | gut
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
    typ: ""             # qualifiziert | einfach
    stand_jahr: 0
    tabellen_zelle: ""  # z. B. "60–80 qm, BJ 1949–1977, mittlere Wohnlage"
    spanne_von_eur_qm: 0.0
    spanne_bis_eur_qm: 0.0
    mittelwert_eur_qm: 0.0
    zuschlaege_abschlaege_eur_qm: 0.0
    ortsuebliche_vergleichsmiete_eur_qm: 0.0

  mietverhaeltnis:
    beginn: "JJJJ-MM-TT"
    aktuelle_nettokaltmiete_eur_gesamt: 0.0
    aktuelle_nettokaltmiete_eur_qm: 0.0
    neuvermietung_oder_bestand: ""  # neuvermietung | bestand

  mietpreisbremse:                  # nur bei neuvermietung
    landesverordnung: ""
    angespannter_markt: false
    hoechstmiete_eur_qm: 0.0
    ausnahmen_geprueft: []

  kappungsgrenze:                   # nur bei bestand
    verschaerft_durch_landesverordnung: false
    obergrenze_prozent: 0           # 20 oder 15
    wartefrist_eingehalten: true

  ergebnis:
    bewertung: ""                   # zulaessig | unzulaessig | grenzfall
    differenz_eur_qm: 0.0
    naechster_schritt: ""           # uebergabe an mieterhoehung-pruefen-widersprechen, klageentwurf-amtsgericht, etc.
```

## Gerechnetes Beispiel (zur Plausibilisierung)

**Sachverhalt:** Wohnung in München, Maxvorstadt, 78 m², Baujahr 1962, gute Wohnlage, modernisiertes Bad, Einbauküche mitvermietet, Zentralheizung, Aufzug, kein Stellplatz. Mietverhältnis seit 01.06.2018 (Bestand). Aktuelle Nettokaltmiete 1.150,00 € (= 14,74 €/m²). Der Vermieter verlangt Erhöhung auf 1.380,00 € (= 17,69 €/m², +20,0 %).

**Schritt 2** — Bayern hat eine Mietenbegrenzungsverordnung und eine Kappungsgrenzenverordnung. München ist ein angespannter Markt; Kappungsgrenze daher 15 %. Mietspiegel München: qualifiziert nach § 558d BGB, Stand 2025.

**Schritt 3** — Wohnlage „gut" (über das städtische Geoportal verifiziert). Ausstattung: drei Sondermerkmale erfüllt (mod. Bad, EBK, Aufzug).

**Schritt 4** — Tabellenzelle „70–90 m², Baujahr 1949–1977, gute Wohnlage" Mittelwert (illustrativ) 15,80 €/m², Spanne 13,40–17,20 €/m². Sondermerkmals-Zuschlag (illustrativ) +0,90 €/m². Ortsübliche Vergleichsmiete für diese Wohnung: **ca. 16,70 €/m²**.

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

## Aktuelle Rechtsprechung — Leitsaetze Mietspiegel

- BGH, Urt. v. 14.12.2022 — VIII ZR 304/21, NJW 2023, 1289 Rn. 28: Ein qualifizierter Mietspiegel (§ 558d BGB) ist im Prozess als Sachverstaendigenzeugnis zu wuerdigen; er darf nur mit ernsthaften inhaltlichen Bedenken beiseitegelassen werden.
- BGH, Urt. v. 18.05.2022 — VIII ZR 214/21, NJW 2022, 2669 Rn. 22: Die Bezugnahme auf einen einfachen Mietspiegel (§ 558c BGB) genuegt als Begruendungsmittel, wenn der Vermieter den konkreten Tabellenplatz angibt und die Wohnwertmerkmale erlaeutert.
- BVerfG, Beschl. v. 18.07.2019 — 1 BvL 1/18, NJW 2019, 3164: Gesetzliche Mietpreisbremse und damit verbundene Mietspiegel-Anwendung sind verfassungskonform; der Eingriff in die Vertragsfreiheit ist verhaeltnismaessig.
