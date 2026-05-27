---
name: entscheidungsbaum-ki-vo-gesamt-workflow
description: "Anwalt oder Compliance-Beauftragter startet eine vollstaendige KI-VO-Pruefung und fragt: Womit fange ich an und welche Skills werden in welcher Reihenfolge benoetigt? Master-Workflow KI-VO. Art. 2 Anwendungsbereich Art. 3 Rollenzuordnung Art. 5 Verbote Art. 6 Hochrisiko Art. 50 begrenztes Risiko. Pruefraster: zehn Schluesselfragen in Reihenfolge mit klaren Verzweigungen. Output: strukturierter Pruefpfad mit Verweisen auf Folge-Skills. Abgrenzung zu triage-ki-vo-vorpruefung (kurzer Schnellcheck) und risikoklassen-uebersicht-und-triage (Risikoklassen-Fokus)."
---

# Master-Workflow: Vollständiger KI-VO-Entscheidungsbaum

## Zweck und Verwendung

Dieser Skill ist der zentrale Master-Workflow des KI-VO-Prüfers. Er stellt zehn Fragen in logischer Reihenfolge und leitet je nach Antwort zum passenden Detail-Skill weiter. Am Ende steht ein vollständiges Prüfergebnis.

**Verwendung:** Starten Sie hier, wenn Sie eine vollständige KI-VO-Prüfung durchführen möchten. Der Workflow führt Sie Schritt für Schritt — Sie können auch einzelne Fragen direkt über die jeweiligen Detail-Skills prüfen.

---

## PFLICHT-DISCLAIMER

**Keine Rechtsberatung. Mechanischer Workflow. Alle Ergebnisse basieren ausschließlich auf den vom Nutzer gemachten Angaben.**

---

## Schritt 0 — Vorprüfung: Was prüfe ich?

Vor Beginn des Entscheidungsbaums: kurze Situationserfassung.

→ Skill: `triage-ki-vo-vorpruefung`

**Weiter zu Frage 1 nach Abschluss der Vorprüfung.**

---

## FRAGE 1: Liegt ein KI-System im Sinne von Art. 3 Nr. 1 KI-VO vor?

**Kern:** Ist das System maschinengestützt, mit einem gewissen Autonomiegrad, und generiert es aus Eingaben Ausgaben wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen?

→ Skill zur Prüfung: `liegt-ki-system-vor-art-3-nr-1`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — KI-System bestätigt | → Frage 2 |
| **NEIN** — Konventionelle Software | → Workflow endet. KI-VO nicht anwendbar. Andere Rechtsgebiete prüfen. |
| **UNKLAR** — Grenzfall | → `abgrenzung-konventionelle-software-vs-ki-system` → dann zurück zu Frage 1 |

---

## FRAGE 2: Ist der territoriale Anwendungsbereich der KI-VO eröffnet (Art. 2 KI-VO)?

**Kern:** Wird das System in der EU in Verkehr gebracht, in der EU genutzt, oder werden Ausgaben in der EU verwendet?

→ Skill zur Prüfung: `territorialer-anwendungsbereich-art-2`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Anwendungsbereich eröffnet | → Frage 3 |
| **NEIN** — Kein EU-Bezug | → Workflow endet. KI-VO nicht anwendbar. Drittstaatenrecht prüfen. |
| **SACHLICHE AUSNAHME** möglich | → `sachlicher-ausschluss-art-2-abs-3-bis-12` → dann ggf. Workflow-Ende oder Frage 3 |

---

## FRAGE 3: Bin ich Anbieter im Sinne von Art. 3 Nr. 3 KI-VO?

**Kern:** Habe ich das System entwickelt oder entwickeln lassen und bringe es unter eigenem Namen in Verkehr oder nehme es in Betrieb?

→ Skill zur Prüfung: `rolle-anbieter-pruefen-art-3-nr-3`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Anbieter-Rolle bestätigt | → Frage 4 (Verbote) und dann Fragen 5-7 (Risikoklasse) → Pflichten: Art. 9-15, 43-49 KI-VO |
| **NEIN** — Kein Anbieter | → Frage 3b (Betreiber?) |
| **UNKLAR** — Rollenwechsel möglich | → `anbieter-werden-art-25` → dann zurück zu Frage 3 |

### FRAGE 3b: Bin ich Betreiber im Sinne von Art. 3 Nr. 4 KI-VO?

→ Skill zur Prüfung: `rolle-betreiber-pruefen-art-3-nr-4`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Betreiber-Rolle bestätigt | → Frage 4 (Verbote) → Pflichten: Art. 26, 27 KI-VO |
| **NEIN** | → `persoenlicher-anwendungsbereich-rollen-art-3` für weitere Rollen |

---

## FRAGE 4: Liegt eine verbotene Praktik nach Art. 5 KI-VO vor?

**Kern:** Weist das System eines der acht verbotenen Merkmale auf?

→ Skill zur Prüfung: `verbotene-praktiken-art-5`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Verbotene Praktik | → **STOPP. System ist verboten.** Einstellung des Betriebs. Bußgeldrisiko bis 35 Mio EUR / sieben Prozent. → `sanktionen-art-99-bis-101` → `mandatsabbruch-empfehlung-komplexe-faelle` |
| **NEIN** — Keine verbotene Praktik | → Frage 5 |

---

## FRAGE 5: Liegt Hochrisiko-KI nach Art. 6 Abs. 1 KI-VO vor?

**Kern:** Ist das System Sicherheitsbauteil eines Anhang-I-Produkts und erfordert dieses Produkt eine Konformitätsbewertung durch Dritte?

→ Skill zur Prüfung: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Hochrisiko Pfad 1 | → Frage 7 (Rückausnahme?) → Hochrisiko-Pflichten Anbieter |
| **NEIN** | → Frage 6 |

---

## FRAGE 6: Liegt Hochrisiko-KI nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO vor?

**Kern:** Ist das System in einem der acht Anhang-III-Hochrisikobereiche tätig?

→ Skill zur Prüfung: `hochrisiko-art-6-abs-2-anhang-iii`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Anhang-III-Bereich zutreffend | → Frage 7 (Rückausnahme?) |
| **NEIN** — Kein Anhang-III-Bereich | → Frage 8 (begrenztes Risiko?) und parallel `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` zur Dokumentation |

---

## FRAGE 7: Greift die Rückausnahme nach Art. 6 Abs. 3 KI-VO?

**Kern:** Fällt das System unter eine der vier Ausnahmen und betrifft es kein Profiling natürlicher Personen?

→ Skill zur Prüfung: `rueckausnahme-art-6-abs-3`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Rückausnahme greift | → **Kein Hochrisiko.** → `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` (drei mögliche Wege und Restpflichten). Dokumentationspflicht Art. 6 Abs. 4 KI-VO beachten. Weiter zu Frage 8. |
| **NEIN** — Rückausnahme greift nicht | → **Hochrisiko bestätigt.** → `hochrisiko-bestaetigt-end-to-end-roadmap` (zwölf-Schritte-Roadmap von Risikomanagement bis CE und EU-DB-Registrierung). Parallel: Frage 9-10 und Pflichten Anbieter Art. 9-15, 43-49; Betreiber Art. 26, 27 KI-VO |

---

## FRAGE 8: Liegt begrenztes Risiko nach Art. 50 KI-VO vor?

**Kern:** Ist das System ein Chatbot, erzeugt es Deepfakes oder KI-generierten Text von öffentlichem Interesse?

→ Skill zur Prüfung: `begrenztes-risiko-art-50-transparenzpflichten`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — Transparenzpflichten | → Transparenzpflichten nach Art. 50 KI-VO erfüllen. Parallel weiter zu Frage 9. |
| **NEIN** | → Frage 9 (GPAI?) |

---

## FRAGE 9: Liegt ein GPAI-Modell nach Art. 3 Nr. 63 KI-VO vor?

**Kern:** Handelt es sich um ein großskalig trainiertes Modell mit allgemeiner Aufgabenerfüllung?

→ Skill zur Prüfung: `gpai-vorliegen-art-3-nr-63`

| Antwort | Nächster Schritt |
|---|---|
| **JA** — GPAI-Modell | → `gpai-modelle-art-51-bis-55` → Frage 9b (systemisches Risiko?) |
| **NEIN** | → Frage 10 (Registrierung?) |

### FRAGE 9b: Systemisches Risiko — Überschreitung 10e25 FLOP?

→ Skill: `gpai-systemisches-risiko-schwelle-10e25-flop`

| Antwort | Nächster Schritt |
|---|---|
| **JA** | → Zusätzliche Pflichten Art. 55 KI-VO |
| **NEIN** | → Standard-GPAI-Pflichten (Art. 51-54 KI-VO) |

---

## FRAGE 10: Wann und wie registriere ich in der EU-Datenbank?

**Kern:** Besteht Registrierungspflicht nach Art. 49 und 71 KI-VO?

→ Skill zur Prüfung: `eu-datenbank-registrierung-art-49-und-71`

| Rolle | Wann? | Was? |
|---|---|---|
| Anbieter Hochrisiko Anhang III | Vor Inverkehrbringen | Pflicht-Registrierung |
| Betreiber (öffentliche Stelle) | Vor Einsatz | Pflicht-Registrierung |
| GPAI-Anbieter | Vor Inverkehrbringen | Pflicht-Registrierung |

---

## SCHRITT FINAL: Prüfdokument generieren

Nach Durchlaufen aller relevanten Fragen:

→ Skill: `output-pruefdokument-ki-vo-mit-warnhinweisen`

Für Anbieter von Hochrisiko-KI zusätzlich:

→ Skill: `output-konformitaetserklaerung-eu-anhang-v`

Für Betreiber aus dem öffentlichen Sektor:

→ Skill: `output-betreiber-checkliste-und-folgenabschaetzung`

---

## Ergänzende Querverweise

| Thema | Skill |
|---|---|
| Rollenabgrenzung im Detail | `persoenlicher-anwendungsbereich-rollen-art-3` |
| Einführer-Pflichten | `einfuehrer-importer-pflichten-art-23` |
| Händler-Pflichten | `haendler-distributor-pflichten-art-24` |
| Übergangsfristen | `zeitlicher-geltungsbereich-uebergangsfristen` |
| Andere Rechtsgebiete | `verhaeltnis-zu-anderen-unionsrechtsakten` |
| Sanktionen | `sanktionen-art-99-bis-101` |
| Governance | `governance-aufsichtsbehoerden-art-70` |
| Fachanwalt-Bedarf | `mandatsabbruch-empfehlung-komplexe-faelle` |

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 49: KI-Scoring-System als automatisierte Einzelentscheidung nach Art. 22 DSGVO — Masstab fuer Hochrisiko-Klassifikation und Betreiberpflichten nach KI-VO.
- EuGH, Urt. v. 04.10.2024 — C-203/22 (Dun & Bradstreet), NJW 2025, 56 Rn. 38: Betreiber muss Entscheidungslogik offenlegen — Art. 13 KI-VO Transparenzpflicht und Art. 26 Abs. 6 Korrekturrecht.
- BGH, Urt. v. 19.06.2018 — VI ZR 184/17, NJW 2018, 2877 Rn. 15: Organisationspflichten bei technischen Systemen — massgeblich fuer KI-VO Betreiberpflichten und interne Governance.
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 87: Drittlandtransfer bei KI-APIs erfordert Schutzgarantien; Art. 28 DSGVO AVV in KI-Lieferkette.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Kommentarliteratur
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 2 Rn. 1: Anwendungsbereich und Pflichten.
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10: Wechselwirkung KI-VO und DSGVO.

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — ENTSCHEIDUNGSBAUM KI VO GESAMT WORKFLOW
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 2 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
