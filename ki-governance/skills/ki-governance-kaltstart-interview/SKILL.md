---
name: ki-governance-kaltstart-interview
description: "KI-Governance-Plugin erstmalig einrichten oder Inventar der KI-Systeme im Unternehmen erfassen und AI-Act-Anwendungsbereich prüfen. Führt Erstgespraech durch ermittelt KI-Inventar Rolle im KI-Lieferkette (Anbieter/Betreiber Art. 3 KI-VO 2024/1689) regulatorischen Anwendungsbereich. Normen EU-KI-VO 2024/1689 Art. 3 Rolle Art. 6 Risikoklasse Hochrisiko-KI Anhang III. Output Praxisprofil in Konfiguration mit KI-Inventar Rollenklassifizierung und Governance-Framework. Abgrenzung: ki-governance-anpassen für spaetere Einzelaenderungen ki-inventar für laufende Inventar-Pflege."
---

# Erstgespräch KI-Governance

## Zweck

Ermittelt im Erstgespräch, wie das Unternehmen im KI-Ökosystem positioniert
ist — als Anbieter, Betreiber, Importeur oder Händler gem. Art. 3 KI-VO
(Verordnung (EU) 2024/1689) — und welche Rechtsregime tatsächlich anwendbar
sind. Ergebnis wird als Praxisprofil in die Plugin-Konfiguration geschrieben
und von allen anderen Skills gelesen.

Anbieter- und Betreiberpflichten nach dem AI Act sind grundverschieden:
Art. 9–15 KI-VO betreffen Anbieter, Art. 25–29 KI-VO Betreiber. Das
Erstgespräch klärt die Rolle systembezogen (nicht unternehmensweit).

## Eingaben

- Unternehmensname, Branche, Sitz und operative Jurisdiktionen
- Rolle im KI-Lieferkette per AI Act (Art. 3 KI-VO)
- Bestehende KI-Nutzungsrichtlinie, KI-Folgenabschätzungen, Anbieterverträge
- KI-Inventar oder Freigabe-/Sperrliste, soweit vorhanden
- Regulatorischer Anwendungsbereich (AI Act, DSGVO, DSA, Sektoren)
- Governance-Team, Eskalationsmatrix, Datenschutzbeauftragter

## Rechtlicher Rahmen

**Kernvorschriften**

- **Verordnung (EU) 2024/1689 (AI Act)**: In Kraft 01.08.2024; gestaffelte
  Anwendbarkeit. Art. 3: Anbieter, Betreiber, Importeur, Händler, bevoll-
  mächtigter Vertreter. Art. 5: verbotene Praktiken (ab 02.02.2025). Art. 6
  i.V.m. Anhang III: Hochrisiko-KI. Art. 9–15: Anbieterpflichten. Art. 25–29:
  Betreiberpflichten.
- **DSGVO Art. 22**: Automatisierte Einzelentscheidungen; Widerspruchsrecht
  Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **GeschGehG §§ 2, 4**: Schutz von Geschäftsgeheimnissen bei Trainingsdaten.
- **UrhG § 44b**: Text-und-Data-Mining-Schranke bei KI-Training.
- **BSI-Gesetz (BSIG)**: KI-Systeme in kritischer Infrastruktur.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmung des Betriebsrats bei KI-Tools
  zur Mitarbeiterüberwachung/-bewertung.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  Automatisiertes Profiling als Art. 22 Abs. 1 DSGVO-Entscheidung, wenn
  KI-Note maßgebliche Grundlage für Drittentscheidung ist.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  maßstäbe für automatisierte Informationssysteme, übertragbar auf KI.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
  Vergessen I): Grundrechtliche Schutzpflichten gegenüber algorithmischen
  Systemen.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 3 Rn. 12 ff.
  (Anbieter/Betreiber-Begriff).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 5 ff.
- Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 45 ff.
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
  Teil IV Rn. 88 ff.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 0 — Vorabprüfung**

1. `CLAUDE.md` lesen: fehlt → Erstgespräch starten; enthält `[PLATZHALTER]`
   → Neustart anbieten; vollständig ausgefüllt → überspringen (außer `--neu`).
2. Geteiltes Unternehmensprofil (`unternehmens-profil.md`) prüfen: vorhanden →
   Einzeiler zur Bestätigung, Unternehmensfragen überspringen.
3. Installations-Scope: bei Projekt-Scope einmaligen Hinweis ausgeben.

**Schritt 1 — Eröffnung und Kurzwahl**

Kurzstart (2 Min.): Rolle, Organisationsumfeld, Integrationscheck,
regulatorischer Anwendungsbereich; Konfiguration mit `[STANDARD]`-Markern.
Vollständig (15 Min.): vollständiger Gesprächsablauf unten.

**Schritt 2 — Wer nutzt das Plugin? Organisationsumfeld?**

Rolle: (1) Jurist/Syndikusrechtsanwalt (§ 46 BRAO), (2) Nicht-Jurist mit
Anwaltszugang, (3) Nicht-Jurist ohne. Bei 2/3 einmalig erklären:
Ausgaben als Arbeitsmaterial für anwaltliche Prüfung, nicht als
abschließende Rechtsauskunft.

Integrationscheck: nur `✓` bei erfolgreich getesteter Verbindung; `⚪`
konfiguriert-ungeprüft; `✗` nicht vorhanden.

**Schritt 3 — Anbieter, Betreiber oder beides? (Art. 3 KI-VO)**

Rollen systembezogen ermitteln. KI-Inventar: 1–3 Systeme sofort eintragen
oder auf später verschieben. Schatten-KI aktiv ansprechen (eingebettete
KI in genehmigten Tools, informell genutzte Tools, nicht bekannte
Anbieter-KI). Alles Entdeckte mit `[UNDOKUMENTIERT — TRIAGE AUSSTEHEND]`
ins Register.

**Schritt 4 — Regulatorischer Anwendungsbereich**

Nicht annehmen; tatsächlichen Anwendungsbereich recherchieren:
AI Act (Anhang III Hochrisiko, Art. 5 Verbote, gestaffelte Anwendbarkeit);
DSGVO Art. 22 (Scoring, HR, Kreditvergabe); DSA Art. 27/38 (Empfehlungs-
systeme sehr großer Plattformen); Sektoren (BaFin MaRisk, MDR/IVDR);
§ 87 BetrVG bei Mitarbeiter-KI; vertragliche Anforderungen von Kunden.

**Schritt 5 — Anwendungsfall-Register und Rote Linien**

Szenarien für Betreiber: Bewerbungs-Screening (Hochrisiko nach Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a),
HR-Zusammenfassungen, Kundendienst-Entwürfe, Spesen-Anomalieerkennung.
Rote-Linien-Frage: "Was wäre automatisch Nein?" Verbotene Praktiken
nach Art. 5 KI-VO als Ausgangspunkt (Social Scoring, subliminale
Manipulation, Echtzeitbiometrie, Emotionserkennung am Arbeitsplatz).

**Schritt 6 — Governance und Eskalation**

Governance-Team-Größe; Anbietervertrags-Eigentümer; Datenschutzbeauftragter
(§ 37 ff. DSGVO); Eskalationspfad (namentlich oder nach Funktion: GC,
Datenschutzbeauftragter, Geschäftsführung).

**Schritt 7 — Quelldokumente**

KI-Nutzungsrichtlinie; Folgenabschätzung; KI-Anbieterverträge (AVV + KI-Annex);
KI-Inventar; Freigabe-/Sperrliste. Bei fehlendem Dokument: Basispraxisprofil
aus Gesprächsangaben, alle Abschnitte als `[ANGABEN AUS INTERVIEW]` kennzeichnen.

## Ausgabeformat

Praxisprofil als `CLAUDE.md`, Abschnitte: Unternehmensprofil (KI-Rolle gem.
Art. 3 KI-VO, regulatorischer Fußabdruck); KI-Anwendungsfall-Register
(Tabelle: Anwendungsfall, Status, Bedingungen, Rote-Linie-Grund); Rote Linien;
Governance-Stufen; Folgenabschätzungs-Hausstandard; KI-Anbieter-Governance;
KI-Richtlinien-Verpflichtungen; Governance-Team und Eskalation.

Nach dem Schreiben: Zusammenfassung zeigen, erste Aufgaben vorschlagen
(Anwendungsfall triagieren, Anbietervertrag prüfen, Richtlinie entwerfen),
Lücken explizit benennen (kein KI-Inventar = kein systematisches Assessment
möglich; keine Anbieter-KI-Klauseln = Anbieter kann auf Daten trainieren).

## Beispiel

Mittelständischer Softwarehersteller (500 MA, Sitz Deutschland, Kunden EU/UK):
- Als Anbieter einer KI-gestützten Dokumentenklassifizierungslösung → Anbieter
  nach Art. 3 Nr. 3 KI-VO; ggf. Hochrisiko nach Anhang III.
- Intern KI-Schreibassistenten → Betreiberrolle Art. 3 Nr. 4 KI-VO.
- DSGVO Art. 22 relevant weil Dokumentenklassifizierung für Kunden automatisch.
- Praxisprofil mit Anbieterpflichten (Art. 9–15 KI-VO) als Schwerpunkt.

## Risiken und typische Fehler

- Builder/Betreiber-Frage nicht überspringen; bei "beides" die Seite mit
  größerer Governance-Last zuerst bearbeiten.
- Kein Regime annehmen; tatsächlichen Anwendungsbereich recherchieren.
- Anwendungsfall-Register nie aus generischen Positionen befüllen; bei
  Interview-Angaben: `[POSITIONEN AUS INTERVIEW — als Ausgangspunkt]`.
- Schatten-KI ernst nehmen: ein Register ohne informell genutzte Tools lügt.
- KI-Governance- und Datenschutz-Interview nicht vermischen.

## Quellenpflicht

- **AI Act Art. 3, 5, 6 i.V.m. Anhang III, 9–15, 25–29** — VO (EU) 2024/1689.
- **DSGVO Art. 22** bei automatisierten Einzelentscheidungen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 3 Rn. 12 ff.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 5 ff.**
- Ausgaben auf Basis von Gesprächsangaben: `[ANGABEN AUS INTERVIEW —
  anwaltliche Prüfung empfohlen]` kennzeichnen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Definitionen Anbieter / Betreiber
- Art. 5 KI-VO — verbotene Praktiken (ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 9-15 KI-VO — Anbieterpflichten
- Art. 25-29 KI-VO — Betreiberpflichten

## Triage zu Beginn
1. Handelt das Unternehmen als Anbieter, Betreiber, Importeur oder Haendler (Art. 3 KI-VO)?
2. Welche KI-Systeme sind bereits produktiv — und welche sind in Planung?
3. Welche Regimes sind anwendbar — KI-VO, DSGVO, DSA, sektorale Regeln (BSIG, SGB V)?
4. Gibt es bereits eine KI-Nutzungsrichtlinie oder Folgenabschaetzungen?
5. Wer ist im Governance-Team — KI-Beauftragter, DSB, Betriebsrat, Eskalationskette?

## Output-Template — Praxisprofil-Ersterfassung
**Adressat:** KI-Beauftragter / Rechtsabteilung — Tonfall: strukturiert, vollstaendig
```
PRAXISPROFIL KI-GOVERNANCE — ERSTERFASSUNG
[DATUM] — [UNTERNEHMEN / NAME MANDANT]

1. UNTERNEHMENS-PROFIL
   Branche: [BRANCHE]
   Jurisdiktionen: [LAENDER]
   KI-Rolle nach Art. 3 KI-VO: [ANBIETER / BETREIBER / IMPORTEUR / HAENDLER]

2. KI-INVENTAR (Einstieg)
   | System | Zweck | Rolle | Risikoklasse | Status |
   |---|---|---|---|---|
   | [SYSTEM 1] | [ZWECK] | [ROLLE] | [KLASSE] | [STATUS] |

3. REGULATORISCHER FUSSABDRUCK
   - KI-VO: [Anwendbar — Hochrisiko: Ja/Nein / Nicht anwendbar]
   - DSGVO Art. 22: [Anwendbar / Nicht anwendbar]
   - DSA: [Anwendbar / Nicht anwendbar]
   - Sektorale Regeln: [BSIG / SGB V / ...]

4. GOVERNANCE-TEAM
   KI-Beauftragter: [NAME]
   DSB: [NAME]
   Eskalation: [NAME / ROLLE]

5. RISIKOEINSTELLUNG: [KONSERVATIV / MITTIG / PROGRESSIV]

6. NAECHSTE SCHRITTE
   1. [MASSNAHME bis DATUM]

Erstellt: [NAME], [DATUM]
Naechste Pruefung: [DATUM]
```
