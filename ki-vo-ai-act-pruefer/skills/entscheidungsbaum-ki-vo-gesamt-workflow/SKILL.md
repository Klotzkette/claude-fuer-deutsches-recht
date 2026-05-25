---
name: entscheidungsbaum-ki-vo-gesamt-workflow
description: "Master-Workflow: Sequenzieller Entscheidungsbaum durch die gesamte KI-VO-Pruefung. Zehn Schlusselfragen in Reihenfolge mit klaren Verzweigungen Wenn-Antwort-A-gehe-zu-Skill-X. Startpunkt des gesamten KI-VO-Pruefers fuer strukturierte Vollpruefung."
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
