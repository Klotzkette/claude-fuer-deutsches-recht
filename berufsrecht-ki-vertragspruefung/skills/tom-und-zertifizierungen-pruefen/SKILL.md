---
name: tom-und-zertifizierungen-pruefen
description: "Pruefe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral fuer Berufsrecht no training Zero-Retention EU-Hosting Verschluesselung Loeschkonzept Audit-Recht. DAV-Stellungnahme Seite dreizehn vierzehn."
---

# TOM und Zertifizierungen prüfen

## Disclaimer

Diese Forprüfung ist keine Rechtsberatung, sondern strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Norm und Rahmen

Berufsrechtlich verlangt die Sorgfaltspflicht bei der Dienstleisterauswahl (Abs. 2 der jeweiligen Dienstleisterregelung), dass die technische und organisatorische Sicherheit des Anbieters überzeugt. Datenschutzrechtlich präzisiert das Art. 32 DS-GVO. Die DAV-Stellungnahme 32/2025 (Seite 13) stellt klar: Die Verschlüsselung darf nicht so weit gefordert werden, dass sie die KI-Dienstleistung entwertet. Eine Ende-zu-Ende-Verschlüsselung, die das KI-System-Inferencing unmöglich macht, ist berufsrechtlich nicht zu verlangen.

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

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

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

- EuGH, Urt. v. 14.12.2023 — C-340/21 (Natsionalna agentsia za prihodite), NJW 2024, 685 Rn. 55–79: Technische und organisatorische Maßnahmen nach Art. 32 DSGVO müssen tatsächlich wirksam sein; unzureichende TOMs begründen keine automatische Haftung nach Art. 82 DSGVO, aber sie sind ein starkes Indiz für Pflichtverletzung.
- EuGH, Urt. v. 14.12.2023 — C-340/21 (Natsionalna agentsia za prihodite), NJW 2024, 1091: Immaterieller DSGVO-Schadensersatz nach Art. 82 Abs. 1 setzt Schaden + Kausalitaet + DSGVO-Verstoss kumulativ voraus; keine Bagatellgrenze; bereits begruendete Sorge vor Datenmissbrauch kann ersatzfaehig sein; Verantwortlicher muss Geeignetheit der TOMs nach Art. 32 DSGVO darlegen.
- OLG Dresden, Urt. v. 30.11.2021 — 4 U 1158/21, NJW 2022, 334 Rn. 22: Schadensersatzpflicht bei mangelnden TOMs nach Art. 32 DSGVO; Zertifizierungen (ISO 27001) erhöhen Beweislastchancen des Verantwortlichen erheblich.
- LG München I, Urt. v. 09.12.2021 — 31 O 16606/20, ZD 2022, 115 Rn. 18: Zum Zusammenhang zwischen unzureichenden TOMs und Schadensersatzpflicht nach Art. 82 DSGVO; fehlende Verschlüsselung trotz sensiblen Datenmaterials ist Pflichtverletzung.

## Zentrale Normen (Paragrafenkette)

- Art. 32 DSGVO — Technische und organisatorische Maßnahmen; Stand der Technik
- Art. 28 Abs. 3 lit. c DSGVO — TOM-Anlage als Pflichtbestandteil der AVV
- Art. 83 Abs. 4 DSGVO — Bußgeld bei Verstoß gegen Art. 32: bis 10 Mio. EUR oder 2 %

## Kommentarliteratur

- Bergt, in: Kühling/Buchner DSGVO/BDSG, 4. Aufl. 2024, Art. 32 DSGVO Rn. 1–60: Umfassend zu den Anforderungen an TOMs; Bezug auf BSI-Grundschutz, ISO 27001, BSI C5; Stand der Technik.
- DAV-Stellungnahme Nr. 32/2025, S. 13–14: Zu den TOM-Anforderungen bei KI-Anbietern; ISO 27001 und BSI C5 Typ 2 als Mindeststandards; no-training und Zero-Retention als berufsrechtlich relevante TOMs.

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

