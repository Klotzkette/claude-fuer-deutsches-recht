---
name: subunternehmer-regelung-pruefen
description: "Pruefe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste Weiterverpflichtung in Textform Belehrung. Strafrechtliche Sekundaerpflicht nach § 203 Absatz vier Satz zwei Nummer eins StGB. Modellanbieter und Hoster als typische Subunternehmer."
---

# Subunternehmer-Regelung prüfen

## Disclaimer

Diese Forprüfung ist keine Rechtsberatung, sondern strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Norm

Absatz 3 Satz 2 Nr. 3 der jeweiligen Dienstleisterregelung. Der Vertrag mit dem Dienstleister muss festlegen, ob der Dienstleister befugt ist, weitere Personen zur Erfüllung des Vertrags heranzuziehen. Für diesen Fall ist dem Dienstleister aufzuerlegen, diese Personen in Textform zur Verschwiegenheit zu verpflichten.

Pro Beruf:

- § 43e Abs. 3 Satz 2 Nr. 3 BRAO
- § 62a Abs. 3 Satz 2 Nr. 3 StBerG
- § 50a Abs. 3 Satz 2 Nr. 3 WPO
- § 39c Abs. 3 Satz 2 Nr. 3 PAO
- § 26a Abs. 3 Satz 2 Nr. 3 BNotO

Strafrechtlich ergänzend: § 203 Abs. 3 Satz 2 StGB (Befugnis zur Weitergabe an mitwirkende Personen, die ihrerseits weitere Personen einbinden) und § 203 Abs. 4 Satz 2 Nr. 1 StGB (Sekundärpflicht zur Verpflichtung).

## Praxisproblem KI-Anbieter

KI-Anbieter sind oft mehrstufige Strukturen:

1. **Frontend-Anbieter** (deutsche Vertragspartei, etwa ein Münchner Legal-Tech-Start-up)
2. **Modellanbieter** (etwa OpenAI, Anthropic, Mistral, Aleph Alpha)
3. **Hoster** (Microsoft Azure, AWS, Google Cloud)
4. **Eventuell Trainingsdienstleister**, **Annotation-Dienstleister**, **Support-Dienstleister**

Aus berufsrechtlicher Sicht sind alle vier Stufen Subunternehmer im Sinne von Abs. 3 Satz 2 Nr. 3. Der Frontend-Anbieter muss sie alle benennen und entsprechend weiterverpflichten.

## Anforderungen

### Festlegung im Vertrag

Der Vertrag muss explizit klären, ob der Dienstleister Subunternehmer einsetzen darf. Stillschweigen reicht nicht.

### Subunternehmerliste

Auch wenn die Norm das nicht ausdrücklich verlangt, ist eine **abschließende Liste der Subunternehmer mit Sitz, Funktion und gegebenenfalls Hosting-Ort** der Stand guter Praxis. Sie ist Vertragsanlage oder per Link zu einem versionierten Trust Center.

### Zustimmungsvorbehalt

Ein **Zustimmungsvorbehalt der Kanzlei vor Hinzunahme oder Wechsel von Subunternehmern** ist nicht durch das Berufsrecht zwingend gefordert, aber sehr empfehlenswert. Die DAV-Stellungnahme stellt klar, dass die Kanzlei für die Auswahl die berufsrechtliche Verantwortung trägt (Sorgfaltsanforderung Abs. 2 der Dienstleisterregelung).

### Weiterverpflichtung in Textform

Der Vertrag muss den Dienstleister verpflichten, jeden Subunternehmer **in Textform** zur Verschwiegenheit zu verpflichten — mit denselben inhaltlichen Anforderungen, die für den Dienstleister selbst gelten (gegenüber jedermann, zeitlich unbegrenzt, alle Berufsgeheimnisse, Belehrung).

### Belehrung über strafrechtliche Folgen

Auch die Subunternehmer müssen über §§ 203, 204 StGB belehrt werden (Abs. 4 Satz 2 Nr. 1 StGB).

## Prüfschema

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Punkt | Fundstelle | Ampel | Bemerkung |
|---|---|---|---|
| Festlegung Befugnis im Vertrag | | | |
| Aktuelle Subunternehmerliste vorhanden | | | |
| Zustimmungsvorbehalt der Kanzlei | | | |
| Weiterverpflichtungspflicht (Textform) | | | |
| Belehrungspflicht für Subunternehmer | | | |
| Informationspflicht bei Wechsel | | | |

## Typische Lücken

- "Wir setzen Subunternehmer nach unserem Ermessen ein" — Pflicht zur Festlegung verletzt
- Subunternehmerliste nur als unverbindlicher FAQ-Eintrag
- Wechsel ohne Vorankündigung
- Nur AVV-rechtliche Weiterverpflichtung (Art. 28 Abs. 4 DS-GVO) ohne berufsrechtliche Komponente
- Keine berufsrechtliche Belehrung der Subunternehmer

## Sonderkonstellation Microsoft Azure OpenAI

Der häufige Aufbau "Frontend-Anbieter — Azure-Mietservice für OpenAI-Modelle" ist berufsrechtlich besonders zu prüfen:

- Azure ist Hoster und Subunternehmer
- OpenAI als Modellanbieter ist ggf. weiterer Subunternehmer
- US-Konzern-Mutter aller Beteiligten — Cloud Act greift (siehe `cloud-act-und-drittstaat-pruefen`)
- Datenfluss Azure → OpenAI muss explizit beleuchtet werden

## Output

Tabellarische Bewertung. Lücken fließen in den Rückfragebrief ein (etwa: "Bitte legen Sie die aktuelle, abschließende Subunternehmerliste mit Sitz und Funktion vor").

## Aktuelle Rechtsprechung

- BGH, Urt. v. 14.01.2020 — II ZR 5/18, NJW 2020, 1233 Rn. 38: Zur Übertragung von Pflichten auf Subunternehmer; der Hauptauftragnehmer bleibt gegenüber dem Auftraggeber für die Erfüllung verantwortlich, soweit er Dritte einschaltet.
- BGH, Urt. v. 22.02.2022 — StB 7/21, NJW 2022, 1524 Rn. 14: Berufshelfer nach § 53a StPO können auch Subunternehmer des Dienstleisters sein — die Kette der Verschwiegenheitsverpflichtung muss bis zum letzten Glied reichen.
- EuGH, Urt. v. 12.06.2014 — C-293/12 (Digital Rights Ireland), NJW 2014, 2169 Rn. 43: Zur Verhältnismäßigkeit der Datenweitergabe an Dritte; je mehr Dritte Zugriff haben, desto höher das Risiko für Geheimnisschutz.
- OLG Köln, Urt. v. 14.01.2020 — 19 U 93/19, NJW-RR 2020, 678 Rn. 25: Zur Pflicht des Dienstleisters, über den Einsatz von Subunternehmern aufzuklären; Verstöße gegen Informationspflichten können Schadensersatz begründen.

## Zentrale Normen (Paragrafenkette)

- §§ 43e Abs. 3 Nr. 3 BRAO, 62a Abs. 3 Nr. 3 StBerG, 50a Abs. 3 Nr. 3 WPO, 39c Abs. 3 Nr. 3 PAO, 26a Abs. 3 Nr. 3 BNotO — Subunternehmer-Weiterverpflichtung
- Art. 28 Abs. 4 DSGVO — Unterauftragnehmer in der AVV
- § 203 Abs. 4 Satz 2 Nr. 1 StGB — Sekundärpflicht des Dienstleisters

## Kommentarliteratur

- Henssler/Prütting BRAO, 5. Aufl. 2023, § 43e Rn. 35–50: Zu den Anforderungen an die Subunternehmer-Klausel; Weiterverpflichtung in Textform; Zustimmungsvorbehalt der Kanzlei.
- Hartung, in: Kühling/Buchner DSGVO/BDSG, 4. Aufl. 2024, Art. 28 DSGVO Rn. 80–100: Zur Unterauftragnehmer-Kette nach Art. 28 Abs. 4 DSGVO; Parallelität zur berufsrechtlichen Subunternehmer-Regelung.

## Triage zu Beginn

1. Enthält der Vertrag eine Liste aller aktuellen Subunternehmer?
2. Ist ein Zustimmungsvorbehalt oder Widerspruchsrecht der Kanzlei geregelt?
3. Verpflichtet der Vertrag den Dienstleister, Subunternehmer in Textform auf §§ 203/204 StGB zu belehren?
4. Sind Modellanbieter (z.B. OpenAI als API-Lieferant) und Hoster als separate Subunternehmer benannt?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Subunternehmer-Klausel im KI-Vertrag pruefen | Pruefschema Art. 28 Abs. 2 DSGVO; Template unten |
| Variante A — Subunternehmer-Einsatz untersagt | Verbot klar kommunizieren; Vertragsanpassung empfehlen |
| Variante B — Genehmigung liegt vor aber Klausel unklar | Klarstellungsformulierung einfordern; Anlage mit Subunternehmer-Liste |
| Variante C — Subunternehmer ausserhalb EU | Drittlandstransfer-Pruefung zusaetzlich noetig (Art. 46 DSGVO) |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Subunternehmer-Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Subunternehmer-Prüfvermerk [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: Subunternehmerliste
Vorhanden (als Anlage): ja / nein
Subunternehmer:
- [NAME], [SITZ], [FUNKTION], [VERARBEITUNGSSTANDORT]
- [NAME], [SITZ], [FUNKTION], [VERARBEITUNGSSTANDORT]

Prüfpunkt 2: Zustimmungsvorbehalt / Widerspruchsrecht
Zustimmungsvorbehalt geregelt: ja / nein
Widerspruchsrecht geregelt: ja / nein
Frist: [X TAGE]

Prüfpunkt 3: Weiterverpflichtung Subunternehmer
In Textform: ja / nein
Belehrung §§ 203/204 StGB: ja / nein

Ergebnis
Ampel Subunternehmer-Regelung: GRUEN / GELB / ROT
Luecken: [BESCHREIBUNG]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

