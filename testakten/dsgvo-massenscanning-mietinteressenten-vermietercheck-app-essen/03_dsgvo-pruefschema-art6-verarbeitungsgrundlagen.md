# 03 — DSGVO-Prüfschema: Verarbeitungsgrundlagen Art. 6 DSGVO

**Aktenzeichen:** DSB-NW-44/26
**Bearbeiter:** RA Dr. Cornelius Specht
**Datum:** 16. Januar 2026
**Betreff:** Rechtmaessigkeitspruefung der Datenverarbeitung durch ProspectScore Pro

---

## 1. Prüfungsgegenstand

Die LDI NRW prüft im Rahmen des Aufsichtsverfahrens DSB-NW-44/26, ob VermieterCheck Solutions GmbH (VCS) die personenbezogenen Daten von Mietinteressenten auf einer rechtmaessigen Grundlage nach Art. 6 Abs. 1 DSGVO verarbeitet hat. Das vorliegende Memorandum analysiert sämtliche in Betracht kommenden Erlaubnistatbestaende und kommt zu einer Bewertung der Verteidigungsposition.

---

## 2. Verarbeitungsvorgänge im Überblick

ProspectScore Pro verarbeitet folgende Datenkategorien:

| Datenkategorie | Herkunft | Sensitivität |
|----------------|----------|---------------|
| Schufa-Score und Negativmerkmale | Schufa Holding AG (B2B-API) | Hoch |
| Voreigentum / Miethistorie | Mandantin eigene Abfragen | Mittel |
| Beruf und Einkommenssituation | Mietinteressent (Selbstauskunft) | Mittel |
| Familienstatus und Haushaltsgroesse | Mietinteressent (Selbstauskunft) | Mittel |
| Automatisierter Risiko-Score (0–100) | ProspectScore Pro (KI-Ausgabe) | Sehr hoch |

Die Verarbeitung dient der automatisierten Entscheidungsunterstützung für Privatvermieter bei der Mietinteressenten-Auswahl.

---

## 3. Prüfschema Art. 6 Abs. 1 DSGVO — Erlaubnistatbestaende

### 3.1 Art. 6 Abs. 1 lit. a DSGVO — Einwilligung

**Tatbestand:** Die betroffene Person hat ihre Einwilligung zu der Verarbeitung der sie betreffenden personenbezogenen Daten für einen oder mehrere bestimmte Zwecke gegeben.

**Prüfungsschritte:**

**Schritt 1 — Freiwilligkeit (Art. 7, ErwGr. 42, 43 DSGVO):**
Mietinteressenten befinden sich in einer typischen Machtasymmetrie: Sie können die Plattform nicht umgehen, wenn Vermieter ausschliesslich über VCS Auskünfte einholen. Nach EDSA-Leitlinien 05/2020 (Consent) ist Freiwilligkeit ausgeschlossen, wenn die Verweigerung der Einwilligung zu einem erheblichen Nachteil führt. Ergebnis: Freiwilligkeit zweifelhaft.

**Schritt 2 — Informiertheit (Art. 13, 14 DSGVO):**
Die VCS-Datenschutzerklärung (Version 2.1 vom 01.03.2023) erwähnt den Betrieb von ProspectScore Pro nicht explizit; das Profiling wird als „Bonitätsabfrage" bezeichnet, ohne die KI-basierte Scoring-Komponente offenzulegen. Ergebnis: Informiertheit nicht gegeben.

**Schritt 3 — Eindeutigkeit (Art. 7 Abs. 2, ErwGr. 32 DSGVO):**
Die Einwilligung wird über ein Koppelungs-Checkbox-Modell eingeholt (Einwilligung an AGB-Akzeptanz geknüpft). Nach Art. 7 Abs. 4 DSGVO ist eine solche Koppelung unzulässig. Ergebnis: Eindeutigkeit nicht gegeben.

**Schritt 4 — Widerruflichkeit (Art. 7 Abs. 3 DSGVO):**
Ein Widerrufsmechanismus ist technisch nicht implementiert. Ergebnis: Widerrufsmechanismus fehlt.

**Gesamtergebnis Art. 6 Abs. 1 lit. a DSGVO:** Einwilligung rechtmaessig nicht erteilt. Die vorhandenen Einwilligungserklärungen sind nicht DSGVO-konform und daher unwirksam. **Ergebnis: Keine wirksame Einwilligung.**

---

### 3.2 Art. 6 Abs. 1 lit. b DSGVO — Vertragserfüllung

**Tatbestand:** Die Verarbeitung ist für die Erfüllung eines Vertrags, dessen Vertragspartei die betroffene Person ist, oder zur Durchführung vorvertraglicher Massnahmen, die auf Anfrage der betroffenen Person erfolgen, erforderlich.

**Pruefung:**
Zwischen VCS und den Mietinteressenten besteht kein Vertrag. VCS unterhalt Vertraege mit den Privatvermietern (B2B-SaaS-Abonnement). Die Mietinteressenten sind keine Vertragsparteien. Das EDSA-Leitlinien 02/2019 (Art. 6 Abs. 1 lit. b) stellt klar, dass der Betroffene selbst Vertragspartei sein muss.

**Gesamtergebnis Art. 6 Abs. 1 lit. b DSGVO:** Tatbestand nicht erfullt. **Ergebnis: Nicht anwendbar.**

---

### 3.3 Art. 6 Abs. 1 lit. c DSGVO — Rechtliche Verpflichtung

**Tatbestand:** Die Verarbeitung ist zur Erfüllung einer rechtlichen Verpflichtung erforderlich, der der Verantwortliche unterliegt.

**Pruefung:**
Keine rechtliche Verpflichtung zur Erstellung von Bonitaets-Profilen für Dritte erkennbar. § 505a BGB (Kreditwuerdigkeitspruefung) gilt nur für Kreditinstitute, nicht für Vermietungsplattformen.

**Gesamtergebnis Art. 6 Abs. 1 lit. c DSGVO:** Tatbestand nicht erfullt. **Ergebnis: Nicht anwendbar.**

---

### 3.4 Art. 6 Abs. 1 lit. f DSGVO — Berechtigtes Interesse

**Tatbestand:** Die Verarbeitung ist zur Wahrung der berechtigten Interessen des Verantwortlichen oder eines Dritten erforderlich, sofern nicht die Interessen oder Grundrechte und Grundfreiheiten der betroffenen Person, die den Schutz personenbezogener Daten erfordern, überwiegen.

**Dreistufiger Prüfungstest (LIA — Legitimate Interest Assessment):**

**Stufe 1 — Legitimes Interesse:**
VCS und angeschlossene Vermieter haben ein wirtschaftliches Interesse an Mietausfallprävention. Das Bundesverwaltungsgericht (BVerwG 6 C 12.18) erkennt Bonitätsprüfungen im Mietrecht als grundsätzlich legitim an. Ergebnis: Legitimes Interesse besteht.

**Stufe 2 — Erforderlichkeit:**
Die Erhebung von Familienstatus und Haushaltsinformationen für ein Risiko-Scoring überschreitet den Umfang einer klassischen Bonitätsprüfung. Weniger einschneidende Mittel (z.B. einfache Schufa-Anfrage ohne KI-Profiling) stehen zur Verfügung. Ergebnis: Erforderlichkeit teilweise verneint.

**Stufe 3 — Interessenabwägung:**
Die automatisierte Profilerstellung (Risiko-Score 0–100) greift erheblich in die Grundrechte der Mietinteressenten ein (Art. 8 GRCh, Recht auf informationelle Selbstbestimmung). Die Betroffenen haben keine Möglichkeit der Kenntnisnahme oder des Widerspruchs. Ergebnis: Interessen der Betroffenen überwiegen.

**Besonderheit Art. 22 DSGVO:** Bei automatisierten Einzelentscheidungen (Scoring als alleinige Grundlage für Vermieter-Entscheidung) ist Art. 6 Abs. 1 lit. f DSGVO als alleinige Grundlage in der Regel nicht ausreichend (s. Akte 04).

**Gesamtergebnis Art. 6 Abs. 1 lit. f DSGVO:** Interessenabwägung fällt zugunsten der Betroffenen aus. **Ergebnis: Nicht ausreichend.**

---

## 4. Gesamtbewertung

| Erlaubnistatbestand | Ergebnis |
|---------------------|----------|
| Art. 6 Abs. 1 lit. a (Einwilligung) | Unwirksam — Koppelung, fehlende Informiertheit |
| Art. 6 Abs. 1 lit. b (Vertrag) | Nicht anwendbar — kein Vertrag mit Betroffenen |
| Art. 6 Abs. 1 lit. c (Rechtspflicht) | Nicht anwendbar — keine Rechtspflicht |
| Art. 6 Abs. 1 lit. f (Berechtigtes Interesse) | Nicht ausreichend — LIA negativ |

**Gesamtergebnis:** Die Verarbeitung durch ProspectScore Pro entbehrt einer wirksamen Rechtsgrundlage nach Art. 6 Abs. 1 DSGVO. Dies stellt einen schwerwiegenden Verstoss dar, der eine Ordnungswidrigkeit nach Art. 83 Abs. 5 lit. a DSGVO begründet.

---

## 5. Verteidigungsstrategie

Angesichts des klaren Befundes empfiehlt RA Dr. Specht folgenden Ansatz gegenüber der LDI NRW:

1. **Einräumen des Verstosses** gegenüber LDI NRW (Milderungsgrund Art. 83 Abs. 2 lit. f — Kooperationsbereitschaft)
2. **Nachträgliche Sanierung:** Einwilligungsmanagement reformieren, Datenschutzerklärung aktualisieren, OptIn-Mechanismus implementieren
3. **Argumentation Art. 83 Abs. 2 lit. b:** Schaden für Betroffene gering (keine nachgewiesene missbilligende Nutzung des Scores durch Vermieter)
4. **Beantragung einer angemessenen Frist** zur Implementierung konformer Verarbeitungsgrundlagen vor Verhangung eines Bussgeldescheids

---

## Quellen

- DSGVO Art. 6, 7, 13, 14, 22, 83 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- EDSA-Leitlinien 05/2020 zur Einwilligung — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/documents/public-consultations/2020/guidelines-052020-consent-under-regulation_de)
- EDSA-Leitlinien 02/2019 zu Art. 6 Abs. 1 lit. b — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22019-processing-personal-data-article-61b-gdpr_de)
- BVerwG, Urt. v. 27.09.2019 — 6 C 12.18 — [openjur.de](https://openjur.de)
- OLG Hamm, Urt. v. 15.08.2023 — 7 U 19/23 — [openjur.de](https://openjur.de)
