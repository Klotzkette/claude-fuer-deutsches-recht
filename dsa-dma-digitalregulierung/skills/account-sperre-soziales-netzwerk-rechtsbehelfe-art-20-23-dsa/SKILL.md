---
name: account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa
description: "Workflow-Skill zu account sperre soziales netzwerk rechtsbehelfe art 20 23 dsa. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Account-Sperre — Rechtsbehelfe nach Art. 20 bis 23 DSA

## Ausgangslage

Nutzer wird auf einer Online-Plattform gesperrt (Account-Sperre, Schattensperre, Inhaltsentfernung, Demonetarisierung, Reichweitenbeschränkung). Plattform sitzt regelmäßig im Ausland; deutsche Niederlassung oder Vertreter nach Art. 13 DSA vorhanden.

## Pflicht-Stufen der Plattform

### Stufe 1 — Begründung (Art. 17 DSA)

- **Klare und spezifische Begründung** der Beschränkung, in präziser, leicht verständlicher Sprache
- Inhalt der Begründung Art. 17 Abs. 3:
  - Art der Beschränkung (Sichtbarkeit, Geldwert, Bezahlung, Hosting, Account-Sperre)
  - Sachverhalt und Umstände
  - **Rechtliche oder vertragliche Grundlage** und Erklärung warum sie passt
  - Information über **Beschwerdemöglichkeiten** (Art. 20, 21)
- Versand in **DSA Transparency Database** (öffentlich)
- **Fehlt eine wirksame Begründung, ist die Sperre formal rechtswidrig** — schon hier ansetzen

### Stufe 2 — Internes Beschwerdesystem (Art. 20 DSA)

- Plattform muss **wirksames, leicht zugängliches, kostenfreies, sechsmonatiges Beschwerdesystem** bereithalten
- **Menschliche Überprüfung** in nicht-automatisierter Form bei manueller Beschwerde
- Frist: zügig zu entscheiden; keine starre Frist im DSA, aber **unverzüglich** und in der Regel innerhalb weniger Wochen
- Entscheidung wieder begründet und mit Hinweis auf Art. 21

### Stufe 3 — Außergerichtliche Streitbeilegung (Art. 21 DSA)

- **Zertifizierte ADR-Stellen** vom DSC
- Plattform muss sich beteiligen; Entscheidung jedoch **nicht bindend**
- Kosten: für Nutzer bei Obsiegen erstattungsfähig; Plattform trägt Kosten der ADR-Stelle
- Stand 2026: in Deutschland mehrere zertifizierte Stellen; Bundesnetzagentur als DSC führt Liste

### Stufe 4 — Gerichtlicher Weg

#### Hauptsache

- **Anspruchsgrundlage:** Wiederherstellung des Accounts / Freischaltung des Beitrags aus dem **Nutzungsvertrag** (positive Vertragsverletzung, § 280 BGB; Erfüllungsanspruch)
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Die BGH-Linie ist mit dem DSA kompatibel und wird ergänzt — Art. 14 Abs. 4 DSA verlangt **sorgfältige, objektive und verhältnismäßige Anwendung** der AGB unter Berücksichtigung der Grundrechte

#### Eilrechtsschutz

- **§§ 935, 940 ZPO** — einstweilige Verfügung auf Wiederherstellung des Zugangs / Reichweitenfreigabe
- Verfügungsgrund regelmäßig zu bejahen, insbesondere bei:
  - Wirtschaftlicher Abhängigkeit (Creator, Händler)
  - Wahlnähe und politischer Kommunikation
  - Drohender irreversibler Reichweitenverlust
- Streitwert orientiert sich an wirtschaftlicher Bedeutung, oft 5 000 bis 25 000 EUR

#### Internationale Zuständigkeit

- **Verbrauchersache:** Art. 17 ff. Brüssel-Ia-VO — Klage am Wohnsitz des Verbrauchers
- **Gewerbliche Sache:** Erfüllungsort, Art. 7 Nr. 1 Brüssel-Ia
- Wenn Plattform außerhalb EU: nationale Zustellungsregeln; **Art. 13 DSA-Vertreter** dient nicht zwingend als Zustellungsadresse für Zivilklagen, kann aber als Anhaltspunkt für Niederlassung dienen (siehe Skill `zustellung-und-vertreter-art-13-dsa-art-37-dma`)

## Anspruchspaket

1. **Wiederherstellung** des Accounts oder des Inhalts
2. **Unterlassung** zukünftiger gleichartiger Sperre
3. **Auskunft** über Sperrgrund und beteiligte automatische Systeme (DSGVO Art. 15, ggf. Art. 22)
4. **Löschung** unrichtiger interner Daten (DSGVO Art. 16, 17)
5. **Schadensersatz** bei nachweisbarem Vermögensschaden (entgangene Einnahmen, Folgeschäden); Geldentschädigung wegen Persönlichkeitsrechtsverletzung möglich, aber Hürden hoch
6. **Erstattung** außergerichtlicher Rechtsanwaltskosten

## Praktischer Mandantenfahrplan

1. **Beweissicherung**: Screenshots, E-Mails, Sperrmitteilung, betroffene Beiträge archiviert (Wayback / lokale Speicherung)
2. **Begründung anfordern** (falls nicht ausreichend nach Art. 17)
3. **Interne Beschwerde** einlegen (Art. 20) — Frist und Inhalt dokumentieren
4. **Parallele DSGVO-Auskunft** Art. 15 zu Sperrgrund und Profiling
5. Bei Eilbedürftigkeit: **Eilantrag** vorbereiten; ADR-Schritt darf nicht vorausgesetzt werden, weil DSA Eilrechtsschutz nicht ausschließt
6. ADR-Verfahren oder Klage je nach Aussicht und wirtschaftlichem Volumen

## Sonderfälle

- **Sperre durch VLOP**: schärfere Pflichten (z. B. Risikobewertung, Transparenz). Gerichtsentscheidungen heben oft auf Inkonsistenz zwischen AGB und gelebter Moderation ab
- **Schattensperre** (Reichweitenreduktion): von Art. 17 Abs. 1 lit. a) erfasst — Pflicht zur Begründung trotzdem
- **Algorithmische Entscheidung ohne menschliche Überprüfung**: Art. 22 DSGVO und Art. 20 Abs. 6 DSA — Anspruch auf menschliche Überprüfung
- **Politische Werbung**: zusätzliche Pflichten nach VO (EU) 2024/900
- **Bot-Verdacht**: Plattform behauptet Bot — Mandant muss Echtheit nachweisen; trotzdem Begründungs- und Beschwerdesystem-Pflicht

## Schnittstelle Strafrecht

Bei Sperrgrund "illegal content" prüfen, ob tatsächlich Straftatbestand erfüllt (§§ 185 ff., 86, 86a, 130 StGB, § 33 BDSG). Anwaltsstrategie: Sperre angreifen, ohne dem Mandanten neuen Strafvorwurf zu generieren.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 17, 20, 21, 23 DSA (VO 2022/2065) — Begründungspflicht, internes Beschwerdesystem, außergerichtliche Streitbeilegung, Transparenzberichte
- §§ 307, 241 Abs. 2 BGB — AGB-Kontrolle und Rücksichtnahmepflichten
- §§ 935, 940 ZPO — Einstweilige Verfügung
- Art. 11 GRCh — Meinungsfreiheit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Faktische Updates (Stand 05/2026)

- **DSA — vollumfaenglich anwendbar:** DSA-Pflichten sind seit dem 17.02.2024 verbindlich. Art. 20-23 DSA (interne Beschwerde, ADR, vetted flaggers, Massnahmen gegen Missbrauch) gelten fuer alle Online-Plattformen und Hosting-Dienste.
- **DDG (Digitale-Dienste-Gesetz):** Das deutsche DDG ist 14.05.2024 in Kraft getreten (BGBl 2024 I Nr. 149); enthaelt nationale Durchfuehrungsbestimmungen, Bestimmung der BNetzA als DSC, Sanktionsregime, Klagebefugnisse, Verbraucher- und Datenschutz-Schnittstellen. Quelle: bgbl.de, bundesnetzagentur.de.
- **ADR-Stellen Art. 21 DSA:** Liste der von der BNetzA zertifizierten Streitbeilegungsstellen live ueber bundesnetzagentur.de pruefen.
- **BGH-Linie zu Account-Sperren:** Aktuelle Rechtsprechung zur AGB-Kontrolle der Sperr-Klauseln (BGH III. ZS) live ueber dejure.org pruefen. DSA ergaenzt die BGH-Linie (insb. zu Verfahrenspflichten, Begruendungstiefe, Art. 14 Abs. 4 DSA).
- **Schnittstelle MStV / TDDDG:** Bei medienrechtlich relevanten Plattformen zusaetzlich § 18, § 19 MStV (Medien­staats­vertrag) beachten.

## Triage zu Beginn

1. Art der Maßnahme: Account-Sperrung / Inhaltsdeaktivierung / Einschränkung?
2. Plattform VLOP/VLOSE (Art. 33 DSA) → erweiterte Pflichten Art. 20, 21, 22 DSA?
3. Begründung durch Plattform erhalten (Art. 17 DSA)?
4. Frist für internes Beschwerdeverfahren noch offen (Art. 20 DSA: 6 Monate ab Maßnahme)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Account-Sperre anfechten (Art. 20-23 DSA) | Stufenweiser Rechtsbehelfs-Fahrplan unten |
| Variante A — interne Beschwerde ausreichend | Stufe 2 DSA-Beschwerde ohne gerichtlichen Weg |
| Variante B — Eilsache (Existenzgefaehrdung durch Sperre) | Direkt Eilrechtsschutz; eAVV beim LG Berlin o.ae. |
| Variante C — Sperre wegen rechtswidriger Nutzerbedingung | DSA-Beschwerdestelle einschalten; Normwidrigkeitspruefung Art. 14 DSA |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Account-Sperre-Mandat

**Adressat:** Gericht / Plattform — Tonfall: sachlich-juristisch

```
Verfügungsantrag / Klage wegen Account-Sperre [DATUM]
Antragsteller/Klaeger: [NAME MANDANT, ANSCHRIFT]
Antragsgegnerin/Beklagte: [PLATTFORM, EU-VERTRETER]
Az.: [AKTENZEICHEN]

Sachverhalt:
[KURZBESCHREIBUNG SPERRE, DATUM, BEGRUENDUNG PLATTFORM]

DSA-Beschwerdeverfahren:
Interne Beschwerde eingereicht am: [DATUM] / nicht moeglich
Ergebnis: [BESCHREIBUNG] / ausstehend

Rechtliche Wuerdigung:
1. AGB-Kontrolle § 307 BGB: [ARGUMENT]
2. Begründungspflicht Art. 17 DSA: [ARGUMENT]
3. Verhältnismäßigkeit / Art. 11 GRCh: [ARGUMENT]

Antrag: Wiederherstellung des Accounts / Inhalts unverzüglich
Streitwert: [BETRAG EUR]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

