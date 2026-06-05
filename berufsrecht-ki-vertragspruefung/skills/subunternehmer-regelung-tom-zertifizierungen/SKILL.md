---
name: subunternehmer-regelung-tom-zertifizierungen
description: "Subunternehmer Regelung TOM Zertifizierungen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Subunternehmer Regelung TOM Zertifizierungen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Subunternehmer Regelung TOM Zertifizierungen** im Plugin Berufsrecht Ki Vertragspruefung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `subunternehmer-regelung-pruefen` | Prüfe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste Weiterverpflichtung in Textform Belehrung. Strafrechtliche Sekundaerpflicht nach § 203 Absatz vier Satz zwei Nummer eins StGB. Modellanbieter und Hoster als typische Subunternehmer. |
| `tom-und-zertifizierungen-pruefen` | Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für Berufsrecht no training Zero-Retention EU-Hosting Verschluesselung Löschkonzept Audit-Recht. berufsrechtliche KI-Debatte Seite dreizehn vierzehn. |

## Arbeitsweg

Im Plugin Berufsrecht Ki Vertragspruefung gilt für **Subunternehmer Regelung TOM Zertifizierungen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `subunternehmer-regelung-pruefen`

**Fokus:** Prüfe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste Weiterverpflichtung in Textform Belehrung. Strafrechtliche Sekundaerpflicht nach § 203 Absatz vier Satz zwei Nummer eins StGB. Modellanbieter und Hoster als typische Subunternehmer.

# Subunternehmer-Regelung prüfen

## Fachkern: Subunternehmer-Regelung prüfen

- **KI-/Berufsrechtsproblem (Subunternehmer-Regelung prüfen):** Prüfe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste Weiterverpflichtung in Textform Belehrung. Strafrechtliche Sekundaerpflicht nach § 203 Absatz vier Satz zwei Nummer eins StGB. Modellanbieter und Hoster als typische Subunternehmer.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

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

Ein **Zustimmungsvorbehalt der Kanzlei vor Hinzunahme oder Wechsel von Subunternehmern** ist nicht durch das Berufsrecht zwingend gefordert, aber sehr empfehlenswert. Die berufsrechtliche KI-Debatte stellt klar, dass die Kanzlei für die Auswahl die berufsrechtliche Verantwortung trägt (Sorgfaltsanforderung Abs. 2 der Dienstleisterregelung).

### Weiterverpflichtung in Textform

Der Vertrag muss den Dienstleister verpflichten, jeden Subunternehmer **in Textform** zur Verschwiegenheit zu verpflichten — mit denselben inhaltlichen Anforderungen, die für den Dienstleister selbst gelten (gegenüber jedermann, zeitlich unbegrenzt, alle Berufsgeheimnisse, Belehrung).

### Belehrung über strafrechtliche Folgen

Auch die Subunternehmer müssen über §§ 203, 204 StGB belehrt werden (Abs. 4 Satz 2 Nr. 1 StGB).

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 43e Abs. 3 Nr. 3 BRAO, 62a Abs. 3 Nr. 3 StBerG, 50a Abs. 3 Nr. 3 WPO, 39c Abs. 3 Nr. 3 PAO, 26a Abs. 3 Nr. 3 BNotO — Subunternehmer-Weiterverpflichtung
- Art. 28 Abs. 4 DSGVO — Unterauftragnehmer in der AVV
- § 203 Abs. 4 Satz 2 Nr. 1 StGB — Sekundärpflicht des Dienstleisters

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## 2. `tom-und-zertifizierungen-pruefen`

**Fokus:** Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für Berufsrecht no training Zero-Retention EU-Hosting Verschluesselung Löschkonzept Audit-Recht. berufsrechtliche KI-Debatte Seite dreizehn vierzehn.

# TOM und Zertifizierungen prüfen

## Fachkern: TOM und Zertifizierungen prüfen

- **KI-/Berufsrechtsproblem (TOM und Zertifizierungen prüfen):** Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für Berufsrecht no training Zero-Retention EU-Hosting Verschluesselung Löschkonzept Audit-Recht. berufsrechtliche KI-Debatte Seite dreizehn vierzehn.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm und Rahmen

Berufsrechtlich verlangt die Sorgfaltspflicht bei der Dienstleisterauswahl (Abs. 2 der jeweiligen Dienstleisterregelung), dass die technische und organisatorische Sicherheit des Anbieters überzeugt. Datenschutzrechtlich präzisiert das Art. 32 DS-GVO. Die berufsrechtliche KI-Debatte 32/2025 (Seite 13) stellt klar: Die Verschlüsselung darf nicht so weit gefordert werden, dass sie die KI-Dienstleistung entwertet. Eine Ende-zu-Ende-Verschlüsselung, die das KI-System-Inferencing unmöglich macht, ist berufsrechtlich nicht zu verlangen.

## "no training" — Zentralfrage

Nach DAV S. 14 ist die Übermittlung von Mandatsdaten zu Trainingszwecken nicht von der Erforderlichkeitsschwelle des Abs. 1 gedeckt. Daher muss der Vertrag eine **"no training"-Klausel** enthalten — eine ausdrückliche Verpflichtung des Anbieters, eingegebene Mandatsdaten nicht zum Training des Modells zu verwenden. Bei API-Aufrufen an Drittmodelle (etwa OpenAI Azure Service) ist zusätzlich der "no training"-Status des Drittmodells nachzuweisen.

## Zero Retention

Die Speicherdauer eingegebener Mandatsdaten beim Anbieter ist möglichst gering zu halten. Optimal: "Zero Retention" — die Daten werden nach der Verarbeitung sofort gelöscht (typisch 0 oder 30 Sekunden nach Abschluss der API-Anfrage). Andernfalls eine konkrete kurze Frist (24 Stunden, sieben Tage). Pauschalfristen wie "bis zu 90 Tage" sind problematisch.

## Zertifizierungen

### ISO 27001

Internationaler Standard für Informationssicherheitsmanagementsysteme. **Mindeststandard**. Prüfen: Geltungsbereich (alle relevanten Standorte und Systeme), Zertifizierungsstelle (akkreditiert), Ausstellungsdatum (höchstens drei Jahre alt), Anhang A Controls relevant.

### BSI C5 (Cloud Computing Compliance Criteria Catalogue)

Vom BSI entwickelter Standard für Cloud-Anbieter. Für Berufsgeheimnisträger besonders aussagekräftig, weil deutsche behördliche Standardkriterien. Es gibt Typ-1- und Typ-2-Testate; Typ 2 ist der Goldstandard.

### SOC 2 Typ 2

US-Standard, oft bei US-Anbietern vorhanden. Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, Privacy. Bei US-Anbietern Mindestnachweis, aber nicht spezifisch genug für deutsches Berufsrecht.

### TISAX

Branchenstandard der Automobilindustrie. Für Legal-AI selten einschlägig, aber bei Mandanten aus der Automotive-Branche relevant.

### EU Cloud Code of Conduct

DSGVO-spezifisches Konformitätsverfahren nach Art. 40 DS-GVO. Hilfreich, aber keine eigenständige Sicherheitszertifizierung.

## Konkrete Prüfpunkte

### EU-Hosting

- Speicherort der Daten ausschließlich in EU/EWR?
- Auch Backups in EU/EWR?
- Verarbeitung (Inferencing) in EU/EWR?
- Vertraglich abgesichert oder nur als Selbstauskunft?

### Verschlüsselung

- Transportverschlüsselung TLS aktuell (mindestens TLS einskommadrei)
- Verschlüsselung im Ruhezustand (AES 256)
- Schlüsselverwaltung: Anbieter oder Kanzlei (Bring-your-own-key)?

### Zugriffskontrolle

- Rollenbasierte Zugriffskontrolle beim Anbieter
- Audit-Logs aller Zugriffe auf Mandatsdaten
- Vier-Augen-Prinzip bei Administratorenzugriffen
- Mitarbeiter-Verpflichtungen (Verschwiegenheit, Background Check)

### Löschkonzept

- Auf Anforderung der Kanzlei
- Automatisch nach Vertragsende
- Bestätigung der Löschung durch Anbieter (Löschprotokoll)
- Auch in Backups und Logs

### Audit-Recht

- Recht der Kanzlei zur Auditierung
- Vorhandene Testate als Surrogat (typisch)
- Mindestens jährliche Aktualisierung der Testate

### Meldepflichten

- Information bei Sicherheitsvorfällen (24 bis 48 Stunden)
- Information bei Behördenanfragen
- Information bei Subunternehmerwechsel

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Punkt | Status | Ampel | Bemerkung |
|---|---|---|---|
| "no training"-Klausel | | | |
| Zero Retention oder kurze Frist | | | |
| ISO 27001 (akt. Testat) | | | |
| BSI C5 (Typ 2 bevorzugt) | | | |
| SOC 2 Typ 2 | | | |
| EU-Hosting vertraglich | | | |
| Verschlüsselung TLS plus Rest | | | |
| Audit-Logs | | | |
| Löschkonzept | | | |
| Meldepflicht Sicherheitsvorfall | | | |
| Audit-Recht | | | |

## Typische Lücken

- "Wir nehmen Sicherheit ernst" ohne Zertifikat
- ISO-Zertifikat nur für Hauptsitz, nicht für Verarbeitungsstandort
- Trust Center mit Versprechen, die nicht im Vertrag stehen
- Löschung nur "auf Anforderung", keine automatische
- Keine "no training"-Klausel für das verwendete Modell

## Output

Tabellarische Bewertung. Defizite landen im Rückfragebrief mit der Aufforderung, Zertifikate, Geltungsbereiche und Vertragsklauseln vorzulegen.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 32 DSGVO — Technische und organisatorische Maßnahmen; Stand der Technik
- Art. 28 Abs. 3 lit. c DSGVO — TOM-Anlage als Pflichtbestandteil der AVV
- Art. 83 Abs. 4 DSGVO — Bußgeld bei Verstoß gegen Art. 32: bis 10 Mio. EUR oder 2 %

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Liegt eine aktuelle TOM-Anlage (mit Datum) zum Vertrag vor?
2. Ist eine ISO-27001-Zertifizierung vorhanden und aktuell (nicht älter als 12 Monate)?
3. Bei Cloud-Anbieter: BSI C5 Typ 2 Testat vorhanden?
4. Sind "no training" und Zero-Retention-Regelungen in den TOMs enthalten?
5. Gibt es ein Audit-Recht der Kanzlei?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — TOM-Abschnitt im Vertrag bewerten | Checkliste Art. 32 DSGVO; Template unten |
| Variante A — Zertifizierung ISO 27001 vorhanden | Zertifikat pruefen ob aktuell; Scope-Abdeckung beachten |
| Variante B — keine TOM-Anlage vorhanden | Ergaenzung fordern; Muster-TOM-Anlage als Verhandlungsgrundlage |
| Variante C — Hochrisiko-Verarbeitung | Erweiterte TOM-Anforderungen; ggf. Pen-Test-Pflicht vereinbaren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — TOM-Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
TOM-Prüfvermerk [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: TOM-Anlage
Vorhanden: ja / nein | Datum: [DATUM]
Verschlüsselung (Transport/Ruhezustand): [TLS 1.3 / AES-256 / unklar]
Zugangskontrolle / RBAC: [beschrieben / nicht beschrieben]
Löschkonzept: [beschrieben / nicht beschrieben]

Prüfpunkt 2: Zertifizierungen
ISO 27001: [vorhanden / nicht vorhanden] | Gültigkeit: [DATUM]
BSI C5 Typ 2: [vorhanden / nicht vorhanden]
SOC 2 Typ 2: [vorhanden / nicht vorhanden]

Prüfpunkt 3: Berufsrechtliche TOM-Besonderheiten
No-training-Klausel: [vorhanden / Lücke]
Zero-Retention: [vorhanden / Lücke]
EU-Hosting-Zusicherung: [vorhanden / Lücke]
Audit-Recht Kanzlei: [vorhanden / Lücke]

Ergebnis
Ampel TOM/Zertifizierungen: GRUEN / GELB / ROT
Luecken: [BESCHREIBUNG]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]
