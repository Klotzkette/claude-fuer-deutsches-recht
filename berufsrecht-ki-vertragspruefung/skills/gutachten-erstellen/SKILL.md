---
name: gutachten-erstellen
description: "Erstelle das zusammenfassende Forpruefungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Pruefpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lueckenliste Handlungsempfehlung. Ausdruecklich keine Rechtsberatung sondern strukturierte Argumentationshilfe fuer das Anbietergespraech."
---

# Forprüfungs-Gutachten erstellen

## Disclaimer

**Diese Forprüfung ist keine Rechtsberatung.** Sie ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Zweck

Das Gutachten fasst alle Einzelprüfungen zu einem strukturierten Dokument zusammen. Es ist intern für die Kanzlei bestimmt, kann aber auszugsweise als Argumentationsgrundlage gegenüber dem Anbieter verwendet werden.

## Aufbau

### 1. Eingangsdaten

Aus `berufsrecht-ki-vertragspruefung-kaltstart-interview`. Beruf, Anbieter, Produkt, Datenarten, Vertragstyp, Anlagen.

### 2. Norm-Adapter

Aus `parallelnormen-andere-berufe`. Tabelle der einschlägigen Normen. Hinweis auf § 203 StGB als Klammer.

### 3. Maßstab

Goldstandard: DAV-Stellungnahme Nr. 32/2025. BRAK-Leitfaden Dezember 2024 wird kurz erwähnt — zurückhaltend.

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
- die DAV-Lesart
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

> Dieses Forprüfungs-Gutachten ist keine Rechtsberatung. Es ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten. Quellen: Memorandum zu § 43e BRAO und § 203 StGB; DAV-Initiativstellungnahme Nr. 32/2025; BT-Drs. 18/12940; einschlägige Gesetzestexte (BRAO StBerG WPO PAO BNotO StGB StPO DS-GVO).

## Stil

- Sachlich, kurz
- Tabellen wo möglich
- Keine Marketing-Sprache
- Disclaimer am Anfang und am Ende
- Bezeichne Anbieterversprechen klar als "Aussage Anbieter, noch nicht im Vertrag" oder "im Vertrag (Fundstelle)"

## Output-Format

Markdown, ca. 5 bis 10 Seiten. PDF-Export optional via Plugin `office`.

## Aktuelle Rechtsprechung

- BVerfG, Beschl. v. 12.10.2021 — 2 BvR 1368/21, NJW 2022, 55 Rn. 44–55: Anwaltliches Berufsgeheimnis als verfassungsrechtlich geschütztes Gut; Kanzleien tragen eigenständige Verantwortung für die Einhaltung der Verschwiegenheitspflicht gegenüber Dritten.
- BGH, Urt. v. 15.06.2021 — AnwSt (R) 1/21, NJW 2021, 2883 Rn. 28: Verschwiegenheitspflicht gilt für alle anvertrauten oder bekanntgewordenen Tatsachen; Verstoß kann zu berufsrechtlichen Sanktionen (Rüge, Geldbuße, Verbot) führen.
- BGH, Urt. v. 22.02.2022 — StB 7/21, NJW 2022, 1524 Rn. 14: Berufshelfer nach § 53a StPO muss zur Berufsausübung mitwirken; nur dann greift das Zeugnisverweigerungsrecht und Beschlagnahmeschutz.
- EuGH, Urt. v. 26.06.2007 — C-305/05 (Ordre des barreaux francophones), NJW 2007, 2413 Rn. 31: Anwaltliches Berufsgeheimnis als fundamentales Prinzip; Eingriffe durch Auskunftspflichten bedürfen europarechtlicher Rechtfertigung.

## Zentrale Normen (Paragrafenkette)

- §§ 43a Abs. 2, 43e BRAO; §§ 57, 62a StBerG; §§ 43, 50a WPO; §§ 39a, 39c PAO; §§ 18, 26a BNotO
- §§ 203, 204 StGB — Straftatbestände
- §§ 53a, 97 StPO — Strafprozessuale Absicherung
- Art. 28, 32 DSGVO — Datenschutzrechtliche Parallelprüfung

## Kommentarliteratur

- Henssler/Prütting BRAO, 5. Aufl. 2023, § 43e Rn. 1–80: Gesamtdarstellung der Dienstleisterregelung mit Anforderungsprofil.
- Fischer StGB, 71. Aufl. 2024, § 203 Rn. 50–80: Zur Strafbarkeit nach § 203 StGB bei Einschaltung von IT-Dienstleistern; Abgrenzung von § 203 Abs. 3 Satz 2 StGB (Berufshelfer) und § 203 Abs. 4 StGB (bei Offenlegung ohne Rechtfertigung).

## Triage zu Beginn

1. Wurden alle Einzelprüfungen aus den Teilskills (Verschwiegenheit, Belehrung, Subunternehmer, Strafprozess, TOM, Drittstaat) durchgeführt?
2. Liegen alle Vertragsdokumente vor (Hauptvertrag, AGB, AVV, Subunternehmerliste, TOM-Anlage)?
3. Sind offene Punkte aus dem Rückfragebrief beantwortet?
4. Welches Ergebnis soll das Gutachten haben (Freigabe / Nachverhandlung / Ablehnung)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — datenschutzrechtliches Gutachten erstellen | Vollgutachten-Format nach Template unten |
| Variante A — nur kurze Stellungnahme noetig | Kurzgutachten-Format; Normenkette komprimieren |
| Variante B — politisch heikle Einschaetzung fuer Mandanten | Ergebnis-offen formulieren; Risiken deutlich benennen |
| Variante C — internes Compliance-Memo ohne externe Wirkung | Schlankeres Format; auf Vollzitierung teilweise verzichten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Forprüfungs-Gutachten (Auszug)

**Adressat:** Kanzlei intern (ggf. auszugsweise für Anbieter) — Tonfall: sachlich-juristisch

```
Forpruefungs-Gutachten KI-Anbietervertrag
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
| Pruefpunkt              | Ampel | Begruendung |
|-------------------------|-------|-------------|
| Erforderlichkeit        |       |             |
| Verschwiegenheitsklausel|       |             |
| Belehrung §§ 203/204    |       |             |
| Subunternehmer          |       |             |
| Strafprozess §§ 53a/97  |       |             |
| TOM / Zertifizierungen  |       |             |
| Drittstaat / CLOUD Act  |       |             |
| AVV Art. 28 DSGVO       |       |             |

IV. Gesamtergebnis
[GRUEN / GELB / ROT]

V. Handlungsempfehlung
[Annehmbar / Nachverhandelbar / Nicht annehmbar]
[Konkrete naechste Schritte]

VI. Disclaimer
Dieses Forpruefungs-Gutachten ist keine Rechtsberatung. Es ist strukturierte
Argumentationshilfe. Abschliessende Beurteilung bleibt der inhabilen Kanzlei
beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.
Quellen: DAV-Stellungnahme Nr. 32/2025; BRAO, StBerG, WPO, PAO, BNotO; StGB; StPO; DSGVO.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

