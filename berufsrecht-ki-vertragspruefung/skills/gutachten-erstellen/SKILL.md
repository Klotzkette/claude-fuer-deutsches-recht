---
name: gutachten-erstellen
description: "Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern..."
---

# Vorprüfungs-Gutachten erstellen

## Fachkern: Vorprüfungs-Gutachten erstellen

- **KI-/Berufsrechtsproblem (Vorprüfungs-Gutachten erstellen):** Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern strukturierte Argumentationshilfe für das Anbietergespräch.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Dienstleisterregelungen der freien Berufe, Auftragsverarbeitung und technische Geheimnisschutzrealität.
- **Entscheidende Weiche:** Mustertext, Anbieterbehauptung, technische Wirklichkeit, Berufsgeheimnis und Datenschutzrolle müssen getrennt bleiben.
- **Arbeitsprodukt:** Vertragsbaustein, Gutachtenstruktur, Redline oder Anbieter-Fragenliste; Ergebnis bleibt Vorprüfung und wird nicht als fertige Berufsrechtsfreigabe ausgegeben.

## Aufbau

### 1. Eingangsdaten

Aus `berufsrecht-ki-vertragspruefung-kaltstart-interview`. Beruf, Anbieter, Produkt, Datenarten, Vertragstyp, Anlagen.

### 2. Norm-Adapter

Aus `parallelnormen-andere-berufe`. Tabelle der einschlägigen Normen. Hinweis auf § 203 StGB als Klammer.

### 3. Maßstab

Maßstab sind zuerst die geltenden Normen und ihre Gesetzesmaterialien. Berufsrechtliche Stellungnahmen, Kammerhinweise und Fachdebatten werden nur als Auslegungshilfe verarbeitet und in ihrer Bindungswirkung kenntlich gemacht.

### 4. Einzelne Prüfpunkte

Pro Skill ein Abschnitt:

- **Erforderlichkeit** (`erforderlichkeit-dokumentieren`)
- **Verschwiegenheitsklausel** (`verschwiegenheitsklausel-pruefen`)
- **Strafrechtliche Belehrung** (`strafrechtliche-belehrung-pruefen`)
- **Subunternehmer-Regelung** (`subunternehmer-regelung-pruefen`)
- **Strafprozessuale Regelung** (`strafprozessuale-regelung-pruefen`)
- **TOM und Zertifizierungen** (`tom-und-zertifizierungen-pruefen`)
- **Cloud Act und Drittstaat** (`cloud-act-und-drittstaat-pruefen`)
- **AVV-Grenzprüfung Datenschutz** (`avv-grenzpruefung-datenschutz`) — als Schnittstelle

Jeder Abschnitt enthält:

- die einschlägige Norm
- die vertretbare Auslegungslinie und Gegenpositionen
- die konkrete Bewertung am vorgelegten Vertrag (Ampel grün/gelb/rot)
- Lücken und offene Punkte

### 5. Gesamtampel

| Bereich | Ampel | Bemerkung |
|---|---|---|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel | | |
| Strafrechtliche Belehrung | | |
| Subunternehmer | | |
| Strafprozessuale Absicherung | | |
| TOM und Zertifizierungen | | |
| Drittstaat | | |
| AVV (Schnittstelle) | | |

### 6. Handlungsempfehlung

Drei Stufen:

- **Annehmbar** (alles grün, gelbe Punkte dokumentieren) — Vertrag nutzbar nach Annahme
- **Nachverhandelbar** (überwiegend grün/gelb, klare rote Punkte) — Rückfragebrief und Klauselvorschläge versenden
- **Nicht annehmbar** (mehrere rote Punkte, strukturelle Probleme) — Anbieterwechsel oder grundlegende Vertragsneuverhandlung

### 7. Anlagen

- Tabellarische Bewertung pro Prüfpunkt
- Lückenliste (priorisiert)
- Verweise auf Rückfragebrief und Klauselvorschläge

## Schlussklausel im Gutachten

Am Ende jedes Gutachtens steht:

> Dieses Vorprüfungs-Gutachten ist keine Rechtsberatung. Es ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der nutzenden Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten. Quellenbasis: geltende Gesetzestexte, Gesetzesmaterialien, verifizierbare Kammerhinweise, Rechtsprechung und aktueller berufsrechtlicher Debattenstand.

## Stil

- Sachlich, kurz
- Tabellen wo möglich
- Keine Marketing-Sprache
- Disclaimer am Anfang und am Ende
- Bezeichne Anbieterversprechen klar als "Aussage Anbieter, noch nicht im Vertrag" oder "im Vertrag (Fundstelle)"

## Output-Format

Markdown, ca. 5 bis 10 Seiten. PDF-Export optional via Plugin `office`.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 43a Abs. 2, 43e BRAO; §§ 57, 62a StBerG; §§ 43, 50a WPO; §§ 39a, 39c PAO; §§ 18, 26a BNotO
- §§ 203, 204 StGB — Straftatbestände
- §§ 53a, 97 StPO — Strafprozessuale Absicherung
- Art. 28, 32 DSGVO — Datenschutzrechtliche Parallelprüfung

## Triage zu Beginn

1. Wurden alle Einzelprüfungen aus den Teilskills (Verschwiegenheit, Belehrung, Subunternehmer, Strafprozess, TOM, Drittstaat) durchgeführt?
2. Liegen alle Vertragsdokumente vor (Hauptvertrag, AGB, AVV, Subunternehmerliste, TOM-Anlage)?
3. Sind offene Punkte aus dem Rückfragebrief beantwortet?
4. Welches Ergebnis soll das Gutachten haben (Freigabe / Nachverhandlung / Ablehnung)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — datenschutzrechtliches Gutachten erstellen | Vollgutachten-Format nach Template unten |
| Variante A — nur kurze Stellungnahme noetig | Kurzgutachten-Format; Normenkette komprimieren |
| Variante B — politisch heikle Einschaetzung für Mandanten | Ergebnis-offen formulieren; Risiken deutlich benennen |
| Variante C — internes Compliance-Memo ohne externe Wirkung | Schlankeres Format; auf Vollzitierung teilweise verzichten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Vorprüfungs-Gutachten (Auszug)

**Adressat:** Kanzlei intern (ggf. auszugsweise für Anbieter) — Tonfall: sachlich-juristisch

```
Vorpruefungs-Gutachten KI-Anbietervertrag
Datum: [DATUM] | Verfasser: [SACHBEARBEITER]
Anbieter: [NAME] | Produkt: [PRODUKT]
Beruf: [BERUF] | Norm-Adapter: § [NORM]

I. Eingangsdaten
[Aus Kaltstart-Interview]

II. Normrahmen
Berufsrecht: § [NORM] [GESETZ]
Strafrecht: §§ 203, 204 StGB
Datenschutz: Art. 28, 32 DSGVO
Strafprozess: §§ 53a, 97 StPO

III. Einzelprüfungen (Ampeltabelle)
| Pruefpunkt | Ampel | Begruendung |
|-------------------------|-------|-------------|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel| | |
| Belehrung §§ 203/204 | | |
| Subunternehmer | | |
| Strafprozess §§ 53a/97 | | |
| TOM / Zertifizierungen | | |
| Drittstaat / CLOUD Act | | |
| AVV Art. 28 DSGVO | | |

IV. Gesamtergebnis
[GRUEN / GELB / ROT]

V. Handlungsempfehlung
[Annehmbar / Nachverhandelbar / Nicht annehmbar]
[Konkrete naechste Schritte]

VI. Disclaimer
Dieses Vorpruefungs-Gutachten ist keine Rechtsberatung. Es ist strukturierte
Argumentationshilfe. Abschließende Beurteilung bleibt der nutzenden Kanzlei
beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.
Quellen: geltende Gesetzestexte, Gesetzesmaterialien, verifizierbare Kammerhinweise, Rechtsprechung und aktueller berufsrechtlicher Debattenstand.
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]
