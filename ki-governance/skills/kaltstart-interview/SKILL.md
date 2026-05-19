---
name: kaltstart-interview
description: >
  Führt das Erstgespräch zur KI-Governance durch — ermittelt KI-Inventar,
  Rolle im KI-Lieferkette (Anbieter/Betreiber gem. Art. 3 KI-VO), regulatori-
  schen Anwendungsbereich und schreibt das Praxisprofil in die Konfiguration.
  Lädt, wenn der Nutzer „KI-Governance einrichten", „KI-Inventar erfassen",
  „Plugin konfigurieren", „Erstgespräch KI" oder „AI Act Anwendungsbereich
  prüfen" sagt oder die Konfigurationsdatei fehlt bzw. `[PLATZHALTER]` enthält.
language: de
triggers:
  - "KI-Governance einrichten"
  - "KI-Inventar erfassen"
  - "Plugin konfigurieren"
  - "Erstgespräch KI"
  - "Onboarding KI-Compliance"
  - "AI Act Anwendungsbereich prüfen"
  - "KI-Rolle Anbieter Betreiber"
  - "KI-Bestandsaufnahme"
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
  und Transparenzpflichten. Maßstab: EuGH C-634/21 (Schufa-Score).
- **GeschGehG §§ 2, 4**: Schutz von Geschäftsgeheimnissen bei Trainingsdaten.
- **UrhG § 44b**: Text-und-Data-Mining-Schranke bei KI-Training.
- **BSI-Gesetz (BSIG)**: KI-Systeme in kritischer Infrastruktur.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmung des Betriebsrats bei KI-Tools
  zur Mitarbeiterüberwachung/-bewertung.

**Leitentscheidungen**

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 (Schufa-Score):
  Automatisiertes Profiling als Art. 22 Abs. 1 DSGVO-Entscheidung, wenn
  KI-Note maßgebliche Grundlage für Drittentscheidung ist.
- EuGH, Urt. v. 04.10.2024 – C-203/22 (Dun & Bradstreet): Offenlegungs-
  pflicht für Algorithmus-Logik in verständlicher Form.
- BGH, Beschl. v. 26.11.2020 – I ZB 58/19, GRUR 2021, 612: Haftungs-
  maßstäbe für automatisierte Informationssysteme, übertragbar auf KI.
- BVerfG, Beschl. v. 06.11.2019 – 1 BvR 16/13, NJW 2020, 300 (Recht auf
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

Szenarien für Betreiber: Bewerbungs-Screening (Hochrisiko Anhang III Nr. 2),
HR-Zusammenfassungen, Kundendienst-Entwürfe, Spesen-Anomalieerkennung.
Rote-Linien-Frage: „Was wäre automatisch Nein?" Verbotene Praktiken
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

- Builder/Betreiber-Frage nicht überspringen; bei „beides" die Seite mit
  größerer Governance-Last zuerst bearbeiten.
- Kein Regime annehmen; tatsächlichen Anwendungsbereich recherchieren.
- Anwendungsfall-Register nie aus generischen Positionen befüllen; bei
  Interview-Angaben: `[POSITIONEN AUS INTERVIEW — als Ausgangspunkt]`.
- Schatten-KI ernst nehmen: ein Register ohne informell genutzte Tools lügt.
- KI-Governance- und Datenschutz-Interview nicht vermischen.

## Quellenpflicht

- **AI Act Art. 3, 5, 6 i.V.m. Anhang III, 9–15, 25–29** — VO (EU) 2024/1689.
- **DSGVO Art. 22** bei automatisierten Einzelentscheidungen.
- **EuGH C-634/21 (Schufa-Score)** bei Scoring-/Profiling-Anwendungsfällen.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 3 Rn. 12 ff.**
- **Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 5 ff.**
- Ausgaben auf Basis von Gesprächsangaben: `[ANGABEN AUS INTERVIEW —
  anwaltliche Prüfung empfohlen]` kennzeichnen.
