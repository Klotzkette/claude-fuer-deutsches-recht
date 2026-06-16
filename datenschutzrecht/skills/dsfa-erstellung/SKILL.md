---
name: dsfa-erstellung
description: "Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit Verhältnismäßigkeit Maßnahmen Restrisiko Vorabkonsultation. Output: DSFA-Dokument Massnahm..."
---

# DSFA – Datenschutz-Folgenabschätzung Art. 35 DSGVO

## Eingaben

- Beschreibung des Verarbeitungsvorhabens (Zweck, Datenarten, Betroffene, Technologie)
- Vorabklassifikation aus `anwendungsfall-triage` (falls bereits erfolgt)
- Praxisprofil aus `CLAUDE.md` (Systemliste, Hausformat, Freigabe-Eskalation)
- Optional: technische Spezifikation, Dienstleisterbeschreibung, AVV-Entwurf

## Ablauf

1. **Schwellwertanalyse (Muss-DSFA-Prüfung).**

 Art. 35 Abs. 1 DSGVO: DSFA erforderlich bei voraussichtlich hohem Risiko. Mindestens zwei der folgenden Kriterien aus EDSA-Leitlinien 09/2022 treffen zu:

 | Kriterium | Prüfung |
 |---|---|
 | Bewertung / Scoring | Ja / Nein |
 | Automatisierte Entscheidung mit Rechtswirkung (Art. 22 DSGVO) | Ja / Nein |
 | Systematische Überwachung | Ja / Nein |
 | Verarbeitung sensibler Daten (Art. 9/10 DSGVO) | Ja / Nein |
 | Verarbeitung großer Mengen oder im großen Umfang | Ja / Nein |
 | Abgleich oder Zusammenführung von Datensätzen | Ja / Nein |
 | Verarbeitung betreffend schutzbedürftige Personen (Kinder, Patienten) | Ja / Nein |
 | Einsatz neuer Technologien (KI, Biometrie, IoT) | Ja / Nein |
 | Verarbeitung verhindert Betroffenenrechte oder Dienstnutzung | Ja / Nein |

 Art. 35 Abs. 3 DSGVO: In jedem Fall DSFA bei systematischer umfangreicher Verarbeitung besonderer Kategorien, umfangreicher Überwachung öffentlicher Bereiche, oder wenn auf der BfDI-Blacklist aufgeführt.

2. **BfDI-Blacklist-Abgleich.**
 Abgleich gegen die Blacklist des BfDI (§ 67 BDSG i.V.m. Art. 35 Abs. 4 DSGVO). `[Modellwissen – aktuellen Stand auf bfdi.bund.de prüfen]`
 Typische Blacklist-Einträge: Biometrische Erfassungssysteme zur eindeutigen Identifizierung, Videoüberwachung öffentlicher Bereiche im großen Umfang, Scoring-Systeme für Kreditwürdigkeit, Gesundheitsdaten-Plattformen für Forschung.

 BfDI-Whitelist (§ 67 Abs. 2 BDSG): Wenn Verarbeitungsart auf Whitelist, entfällt DSFA-Pflicht. `[Modellwissen – prüfen]`

3. **Beschreibung der Verarbeitungstätigkeit (Art. 35 Abs. 7 lit. a DSGVO).**
 - Zweck und Art der Verarbeitung
 - Datenkategorien und betroffene Personengruppen
 - Empfänger, Übermittlungen (inkl. Drittland)
 - Aufbewahrungsfristen
 - Technische Umgebung (Hosting, Sub-AVs)
 - Eigentümer der Verarbeitung (Fachabteilung, Produkt)

4. **Notwendigkeit und Verhältnismäßigkeit (Art. 35 Abs. 7 lit. b DSGVO).**
 - Ist die Verarbeitung für den Zweck erforderlich (Erforderlichkeit)?
 - Werden nicht mehr Daten verarbeitet als nötig (Datenminimierung Art. 5 Abs. 1 lit. c DSGVO)?
 - Ist die Zweckbindung eingehalten (Art. 5 Abs. 1 lit. b DSGVO)?
 - Ist die Rechtsgrundlage klar (Art. 6, 9 DSGVO)?
 - Ist die Speicherfrist verhältnismäßig (Art. 5 Abs. 1 lit. e DSGVO)?

5. **Risikoidentifikation und -bewertung (Art. 35 Abs. 7 lit. c DSGVO).**
 Für jeden identifizierten Risikotyp: Eintrittswahrscheinlichkeit × Schwere des Schadens:

 | Risiko | Kategorie | Eintrittsws. | Schwere | Risikostufe |
 |---|---|---|---|---|
 | Unbefugter Zugriff | Vertraulichkeit | [hoch/mittel/gering] | [hoch/mittel/gering] | 🔴/🟠/🟡/🟢 |
 | Datenverlust | Verfügbarkeit | … | … | … |
 | Profiling ohne Kenntnis | Transparenz | … | … | … |
 | Diskriminierung | Schaden Betroffener | … | … | … |
 | Identitätsdiebstahl | Sicherheit | … | … | … |

 Referenz: EDSA-Leitlinien 09/2022, Abschn. 6; ENISA-Leitfaden DSFA.

6. **Maßnahmen zur Risikominimierung (Art. 35 Abs. 7 lit. d DSGVO).**
 Für jedes Risiko ≥ 🟡 konkrete Maßnahme:
 - Technische Maßnahmen (Verschlüsselung, Pseudonymisierung, Zugriffskontrolle)
 - Organisatorische Maßnahmen (Schulungen, Vier-Augen-Prinzip, Berechtigungskonzept)
 - Vertragsmaßnahmen (AVV, SCC)
 - Restrisiko nach Maßnahmen (bleibt 🔴? → Vorab-Konsultation Art. 36 DSGVO)

7. **Vorab-Konsultation Art. 36 DSGVO.**
 Wenn nach Maßnahmen ein hohes Restrisiko verbleibt: Pflicht zur Vorab-Konsultation bei der zuständigen Aufsichtsbehörde (Art. 36 Abs. 1 DSGVO). Frist: Aufsichtsbehörde hat 8 Wochen zur Antwort (Art. 36 Abs. 2 DSGVO), verlängerbar um 6 Wochen.

8. **DSB-Beteiligung.**
 DSB ist bei der DSFA zu beteiligen (Art. 35 Abs. 2 DSGVO). Stellungnahme des DSB einholen und dokumentieren.

9. **Freigabe und Dokumentation.**
 Freigabeprozess aus `CLAUDE.md`; DSFA im Verarbeitungsverzeichnis vermerken (Art. 30 Abs. 1 DSGVO). DSFA ist bei wesentlicher Änderung der Verarbeitung zu wiederholen (Art. 35 Abs. 11 DSGVO).

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 35 DSGVO (DSFA: Pflicht, Inhalt, Vorab-Konsultation)
- Art. 36 DSGVO (Vorab-Konsultation Aufsichtsbehörde)
- Art. 5 Abs. 1 lit. b, c, e DSGVO (Zweckbindung, Datenminimierung, Speicherbegrenzung)
- § 67 BDSG (Blacklist/Whitelist BfDI)
- EDSA-Leitlinien 09/2022 zur DSFA und Bestimmung von "voraussichtlich hohem Risiko"
- Artikel-29-Datenschutzgruppe, WP 248 rev.01 (DSFA-Methodik, heute EDSA-Referenz)
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Martini, in: Paal/Pauly, DSGVO/BDSG, 3. Aufl. 2021, Art. 35 Rn. 1 ff.
- Klabunde, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 35 Rn. 1 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — DSFA für neue Verarbeitung durchfuehren | Schwellenwertanalyse und vollstaendige DSFA nach Template unten |
| Variante A — Verarbeitung schon laeuft ohne DSFA | Nachtraegliche DSFA; Maßnahmen-Umsetzungsplan erstellen |
| Variante B — Ergebnis der DSFA negativ (hohes Restrisiko) | Verarbeitung anpassen oder Aufsichtsbehoerde konsultieren |
| Variante C — DSFA für mehrere aehnliche Verarbeitungen | Muster-DSFA-Dokument erstellen; individuell anpassen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Beispiel (Schwellwertanalyse)

**Vorhaben:** Einführung eines KI-gestützten Bewerberscreenings mit automatischer Vorauswahl.

**Schwellwertanalyse:**
- Bewertung/Scoring: **Ja** (Bewerber werden automatisch bewertet und gereiht)
- Automatisierte Entscheidung mit Rechtswirkung: **Ja** (Vorauswahl entscheidet über Einladung zum Gespräch → erhebliche Beeinträchtigung i.S.d. Art. 22 Abs. 1 DSGVO, sofern keine Menschenentscheidung zwischengeschaltet)
- Einsatz neuer Technologien (KI): **Ja**
- Schutzbedürftige Personen: ggf. (Bewerber in angespannter Arbeitsmarktsituation)

**Ergebnis Schwellwert:** Mindestens 3 Kriterien erfüllt → **DSFA erforderlich**. Zusätzlich: § 26 Abs. 1 BDSG (Beschäftigtendaten) und Art. 22 DSGVO (automatisierte Einzelentscheidung) sind eigenständige Schutznormen, die eine DSFA unabhängig von der Schwellwertanalyse nahelegen.

## Risiken / typische Fehler

- **Fehlende DSB-Beteiligung:** Art. 35 Abs. 2 DSGVO schreibt ausdrücklich Beteiligung vor; unterlassene Beteiligung ist ein eigenständiger Verstoß, selbst wenn die DSFA inhaltlich korrekt ist.
- **DSFA als Einmalvorgang:** Art. 35 Abs. 11 DSGVO – DSFA muss bei wesentlichen Änderungen der Verarbeitungstätigkeit wiederholt werden. Änderungsmanagement im Verfahren verankern.
- **Vorab-Konsultation übergangen:** Wenn Restrisiko nach Maßnahmen hoch bleibt, ist Art. 36 DSGVO keine Option, sondern Pflicht. Unterlassung ist eigenständiger Bußgeldtatbestand (Art. 83 Abs. 4 lit. a DSGVO).
- **BfDI-Blacklist-Stand nicht geprüft:** Blacklist kann aktualisiert werden. Immer aktuelle Fassung auf bfdi.bund.de prüfen.
- **KI-VO-Überschneidung (ab 2026):** Für KI-Systeme mit hohem Risiko nach VO (EU) 2024/1689 (KI-VO) ist eine Konformitätsprüfung nach KI-VO und eine DSFA nach Art. 35 DSGVO durchzuführen. Beide Instrumente ergänzen sich; die KI-VO-Konformitätsbewertung ersetzt die DSFA nicht. `[Modellwissen – Zeitplan KI-VO prüfen]`

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei EDSA-Aktualisierungen der Leitlinien 09/2022, neuen BfDI-Blacklist-Einträgen sowie KI-VO-Hochrisiko-Kategorien (VO (EU) 2024/1689, Anhang III).

**Querverweise:**
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Vorgelagerte DSFA-Pflichtprüfung
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — TIA als Bestandteil der DSFA bei Drittlandbezug
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` — Vorab-Konsultation Art. 36 DSGVO nach negativer DSFA

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **DSFA + FRIA (Art. 27 KI-VO) bei Hochrisiko-KI:** Ab 02.08.2026 müssen Betreiber bestimmter Hochrisiko-KI-Systeme (öffentliche Stellen, öffentlich-finanzierte Dienste, Kreditwuerdigkeitsbewertung, Kranken-/Lebensversicherungs-Risikobewertung) eine Grundrechte-Folgenabschaetzung (Fundamental Rights Impact Assessment, FRIA) durchfuehren. DSFA und FRIA können integriert werden, sind aber rechtlich eigenstaendig. Quelle: VO (EU) 2024/1689, Art. 27.
- **EDSA-Stellungnahme 28/2024 zu KI-Modellen:** verbindliche Auslegungshilfe zur DSGVO-Bewertung von KI-Modellen und KI-Diensten, insb. zu personenbezogenen Daten in Modell-Gewichten und Training. Quelle: edpb.europa.eu.
- **BfDI-/LfDI-Blacklist Art. 35 Abs. 4 DSGVO:** Aktuelle Liste verpflichtender DSFA-Faelle live über bfdi.bund.de prüfen; auch Landesdatenschutzbehoerden veröffentlichen Listen (z.B. LfDI BW, LDA Bayern).
- **Art. 36 DSGVO Vorab-Konsultation:** Bei Restrisiko nach DSFA Pflicht zur Konsultation der Aufsichtsbehoerde. Frist 8 Wochen, Verlaengerung 6 Wochen möglich.

## Triage zu Beginn

1. Liegt bereits ein Ergebnis aus `anwendungsfall-triage` vor (DSFA PFLICHT)?
2. Welche EDSA-Kriterien sind erfüllt? (Mindestens 2 für DSFA-Pflicht)
3. Ist die Verarbeitung auf der BfDI-Blacklist?
4. Gibt es ein Hausformat in CLAUDE.md?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — DSFA-Zusammenfassung

**Adressat:** DSB / Geschäftsführung / Aufsichtsbehörde — Tonfall: sachlich-juristisch

```
DSFA-Zusammenfassung [DATUM]
Verarbeitungsvorgang: [BEZEICHNUNG]
Verantwortlicher: [NAME]

Schwellwertanalyse: DSFA erforderlich: JA / NEIN
EDSA-Kriterien erfüllt: [X] von 9 ([LISTE])
BfDI-Blacklist: ja / nein

Rechtsgrundlage: Art. [X] DSGVO [§ BDSG]
Datenkategorien: [LISTE]
Betroffene: [GRUPPEN]

Risikobewertung (Vor Massnahmen):
- Wahrscheinlichkeit: hoch / mittel / gering
- Schwere: hoch / mittel / gering
- Gesamtrisiko: HOCH / MITTEL / GERING

Vorgesehene Massnahmen: [LISTE]

Restrisiko (Nach Massnahmen): AKZEPTABEL / NICHT AKZEPTABEL

Entscheidung: Freigabe / Vorab-Konsultation Art. 36 DSGVO erforderlich
Genehmigende Person: [NAME, FUNKTION]
Datum: [DATUM]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

