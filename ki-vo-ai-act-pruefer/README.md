# ki-vo-ai-act-pruefer



<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`ki-vo-ai-act-pruefer`) | [`ki-vo-ai-act-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-vo-ai-act-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte: KI-VO-Konformitätsprüfung MedAssist v4 — Hochrisiko-KI, Marktüberwachung, GPAI-Komponente** (`ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck`) | [Gesamt-PDF lesen](../testakten/ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck/gesamt-pdf/ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck_gesamt.pdf) | [`testakte-ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **KI-VO-Konformitätsprüfung MedAssist v4 — Hochrisiko-KI, Marktüberwachung, GPAI-Komponente** (`ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck`) | [Gesamt-PDF lesen](../testakten/ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck/gesamt-pdf/ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-vo-konformitaet-medassist-hochrisiko-pruefung-vellbruck.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Vollständiger Mechanik-Workflow zur Verordnung (EU) 2024/1689 (KI-VO): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Pflichten, GPAI-Modelle, Konformitätsbewertung, Konformitäts-Evidence-Pack, Sanktionen und Entscheidungsbaum-Workflow.

**Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.**

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| ki-vo-ai-act-pruefer | [ki-vo-ai-act-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-vo-ai-act-pruefer.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **KI-VO: BewerberPilot TalentRank** ([`testakten/ki-vo-konformitaetsbescheinigung-bewerberpilot/`](../testakten/ki-vo-konformitaetsbescheinigung-bewerberpilot/)).

Direkt-Download als ZIP: [testakte-ki-vo-konformitaetsbescheinigung-bewerberpilot.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-vo-konformitaetsbescheinigung-bewerberpilot.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `ki-vo-ai-act-pruefer.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe ein KI-System für Bewerbungsauswahl nach der KI-VO.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install ki-vo-ai-act-pruefer@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Überblick

Der KI-VO-Prüfer ist ein interaktives Mechanik-Plugin für die vollständige Prüfung von KI-Systemen nach der Verordnung (EU) 2024/1689. Er führt den Nutzer in einem sequenziellen Entscheidungsbaum durch alle relevanten Fragen und dokumentiert besonders Zweckbestimmung, tatsächliche Nutzung, GPAI-/Chatbot-Abgrenzung und Hochrisiko-Einordnung nach Art. 6 Abs. 2 i.V.m. Anhang III:

1. Liegt ein KI-System vor? (Art. 3 Nr. 1 KI-VO)
2. Ist der territoriale Anwendungsbereich eröffnet? (Art. 2 KI-VO)
3. Welche Rolle nehme ich ein? (Anbieter / Betreiber / Einführer / Händler / Bevollmächtigter)
4. Liegt eine verbotene Praktik vor? (Art. 5 KI-VO)
5. Ist das System Hochrisiko? (Art. 6 i.V.m. Anhang I oder III KI-VO)
6. Greift eine Rückausnahme? (Art. 6 Abs. 3 KI-VO)
7. Liegt ein GPAI-Modell vor? (Art. 3 Nr. 63 KI-VO)
8. Welche Pflichten treffen mich?
9. Konformitätsbewertung und Registrierung?
10. Welche **End-to-End-Roadmap** brauche ich danach?

Drei mögliche Diagnose-Ergebnisse, drei Workflows:

- **Hochrisiko bestätigt** → `hochrisiko-bestaetigt-end-to-end-roadmap` führt durch zwölf Schritte von Risikomanagement (Art. 9) bis CE-Kennzeichnung, EU-DB-Registrierung und Marktbeobachtung.
- **Hochrisiko verneint über Rückausnahme** (Art. 6 Abs. 3 KI-VO) → `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` dokumentiert Negativ-Diagnose und Restpflichten.
- **Anhang I/III nicht zutreffend** → ebenfalls `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` mit Pflichten zu Art. 5 (Verbot), Art. 50 (Transparenz), Art. 4 (KI-Kompetenz), GPAI.

---

## Skills (48 Stück)

### Einstieg

- **`entscheidungsbaum-ki-vo-gesamt-workflow`** — Master-Workflow: Start hier für vollständige Prüfung
- **`triage-ki-vo-vorpruefung`** — Erfassung des Sachverhalts

### End-to-End-Roadmaps nach Diagnose

- **`hochrisiko-bestaetigt-end-to-end-roadmap`** — zwölf Schritte vom Risikomanagement bis zu CE-Kennzeichnung, EU-DB-Registrierung und Marktbeobachtung; mit Aufwandsschätzung, Akteur-Übersicht (notifizierte Stelle, Marktaufsicht, AI Office, Sektor-Regulatoren) und Markteintritts-Checkliste.
- **`nicht-hochrisiko-bestaetigt-end-to-end-roadmap`** — drei Wege zur Negativ-Diagnose (Anhang nicht zutreffend / Rückausnahme Art. 6 Abs. 3 / kein KI-System), Restpflichten Art. 4, Art. 5, Art. 50, GPAI, sektoral, Dokumentationspflicht und Re-Evaluation-Trigger.

### A. KI-System-Definition

- `liegt-ki-system-vor-art-3-nr-1` — Kernskill: Definition KI-System mit sieben Elementen, Automation/Autonomie/Inferenz und dokumentierbarem Art.-3-Vermerk
- `abgrenzung-konventionelle-software-vs-ki-system` — Grenzfälle: klassische Automation, Statistik, Expertensystem, LLM/API-Komponente
- `falsche-wiese-warnung-ki-vo` — Verwechslung mit DSGVO, MDR, Produkthaftung
- `mandatsabbruch-empfehlung-komplexe-faelle` — Fachanwalt-Bedarf

### B. Anwendungsbereich

- `territorialer-anwendungsbereich-art-2` — EU-Bezug
- `persoenlicher-anwendungsbereich-rollen-art-3` — Rollenübersicht
- `sachlicher-ausschluss-art-2-abs-3-bis-12` — Ausnahmen
- `verhaeltnis-zu-anderen-unionsrechtsakten` — DSGVO, MDR, Maschinenverordnung
- `zeitlicher-geltungsbereich-uebergangsfristen` — Fristen und Datum

### C. Rollenprüfung (Entscheidungsbaum)

- `rolle-anbieter-pruefen-art-3-nr-3` — Bin ich Anbieter?
- `rolle-betreiber-pruefen-art-3-nr-4` — Bin ich Betreiber?
- `anbieter-werden-art-25` — Re-Provisioning: Rollenwechsel zum Anbieter

### D. Risikoklassen (Entscheidungsbaum)

- `risikoklassen-uebersicht-und-triage` — Gesamtüberblick
- `verbotene-praktiken-art-5` — Alle acht Verbote (Entscheidungsbaum)
- `hochrisiko-art-6-abs-1-sicherheitsbauteil` — Pfad 1: Anhang I
- `hochrisiko-art-6-abs-2-anhang-iii` — Pfad 2: Anhang III (alle acht Bereiche samt Untertatbeständen, Zweckbestimmung, Chatbot/GPAI und Mitarbeitenden-Fehlgebrauch)
- `rueckausnahme-art-6-abs-3` — Vier Fallgruppen + Profiling-Sicherungsklausel + Art.-6-Abs.-4-Dokumentation
- `hochrisiko-zuordnung-art-6-und-anhang-i-iii` — Übersicht mit Zweckbestimmung statt Tool-Label
- `begrenztes-risiko-art-50-transparenzpflichten` — Chatbot, Deepfake, KI-Text

### E. Hochrisiko-Pflichten Anbieter

- `hochrisiko-risikomanagementsystem-art-9`
- `hochrisiko-datenqualitaet-und-data-governance-art-10`
- `hochrisiko-technische-dokumentation-art-11-und-anhang-iv`
- `hochrisiko-aufzeichnungspflichten-logging-art-12`
- `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13`
- `hochrisiko-menschliche-aufsicht-art-14`
- `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15`
- `hochrisiko-konformitaetsbewertung-art-43-bis-49` — Selbstbewertung vs. benannte Stelle

### F. Pflichten weiterer Rollen

- `betreiber-deployer-pflichten-art-26` — inkl. Grundrechte-Folgenabschätzung Art. 27
- `einfuehrer-importer-pflichten-art-23`
- `haendler-distributor-pflichten-art-24`
- `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

### G. GPAI-Modelle

- `gpai-vorliegen-art-3-nr-63` — Definition und Abgrenzung: allgemeiner Chatbot/GPAI ist nicht automatisch Hochrisiko
- `gpai-modelle-art-51-bis-55` — Anbieterpflichten
- `gpai-systemisches-risiko-schwelle-10e25-flop` — Schwellenwert und Zusatzpflichten
- `code-of-practice-und-harmonisierte-normen` — harmonisierte Normen, gemeinsame Spezifikationen, GPAI Code of Practice und ISO/IEC-Standards ohne falsche Vermutungswirkung

### H. Governance und Sanktionen

- `governance-aufsichtsbehoerden-art-70`
- `sanktionen-art-99-bis-101`
- `marktueberwachung-meldung-vorfaelle-art-72-bis-79`

### I. Registrierung

- `eu-datenbank-registrierung-art-49-und-71` — Wann und wie registrieren?

### J. Output-Dokumente

- `output-pruefdokument-ki-vo-mit-warnhinweisen`
- `output-konformitaetserklaerung-eu-anhang-v`
- `output-konformitaetsbescheinigung-evidence-pack` — interne Konformitätsbescheinigung/Readiness-Vermerk, EU-Konformitätserklärung, Art.-43-Nachweis, Evidence Index und Lückenliste ohne falsche finale Bescheinigung
- `output-betreiber-checkliste-und-folgenabschaetzung`

### Zum Ausprobieren: Testakte

- [`testakten/ki-vo-konformitaetsbescheinigung-bewerberpilot`](../testakten/ki-vo-konformitaetsbescheinigung-bewerberpilot/) — fiktive Hochrisiko-Recruiting-KI mit Art.-3-/Art.-6-Vermerk, Risikoregister, Daten-Governance, Human Oversight, Art.-43-Checkliste, Konformitätsvermerk, EU-Konformitätserklärung-Entwurf und Lückenliste.
- Download: [testakte-ki-vo-konformitaetsbescheinigung-bewerberpilot.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-vo-konformitaetsbescheinigung-bewerberpilot.zip)

---

## Wichtige Hinweise

- **Keine Rechtsberatung.** Dieses Plugin liefert mechanische Prüfungen, keine anwaltliche Beratung.
- **Dynamisches Rechtsgebiet.** Die KI-VO wird durch Leitlinien der Kommission, harmonisierte Normen und Durchführungsrechtsakte laufend konkretisiert.
- **Zweckbestimmung entscheidet.** Ein allgemeiner Chatbot oder ein GPAI-System ist nicht automatisch Hochrisiko; der konkrete Einsatz in Anhang-III-Kontexten kann die Einstufung aber auslösen.
- **Übergangsfristen beachten.** Nicht alle Pflichten sind bereits anwendbar — siehe `zeitlicher-geltungsbereich-uebergangsfristen`.
- **Fachanwalt bei Hochrisiko.** Bei verbotenen Praktiken, Hochrisiko-KI und GPAI-Modellen mit systemischem Risiko ist ein Fachanwalt für IT-Recht hinzuzuziehen.
- **Konformität sauber bezeichnen.** Eine interne Bescheinigung oder Readiness-Bestätigung ist keine behördliche Zertifizierung. Finale EU-Konformitätserklärungen und CE-/EU-DB-Aussagen erst nach abgeschlossenem Art.-43-Pfad und belegter Akte ausgeben.

---

## Lizenz

Apache-2.0 OR MIT

Autor: Klotzkette

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 48 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abgrenzung-konventionelle-software-vs-ki-system` | Grenzfall-Skill zur Abgrenzung konventioneller Software, Automation, Statistik, Expertensystemen, Workflows und KI-Systemen nach Art. 3 Nr. 1 KI-VO. Problematisiert Automation, Autonomie, Inferenz, gelernte Parameter, LLM/API-Komponenten... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im KI VO AI Act Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspla... |
| `anbieter-werden-art-25` | Betreiber Einführer oder Haendler fragt: Werde ich durch mein Verhalten selbst zum Anbieter eines KI-Systems mit allen daraus folgenden Pflichten? Art. 25 KI-VO Re-Provisioning. Prüfraster: vier Fallgruppen wesentliche Aenderung des Syst... |
| `begrenztes-risiko-art-50-transparenzpflichten` | Unternehmen setzt Chatbot Deepfake-Tool oder KI-Textgenerator ein und fragt: Welche Hinweispflichten treffen uns gegenüber Nutzern? Art. 50 KI-VO begrenztes Risiko. Prüfraster: Chatbot-Hinweispflicht Art. 50 Abs. 1 KI-VO Deepfake-Kennzei... |
| `betreiber-deployer-pflichten-art-26` | Unternehmen oder Behoerde setzt ein Hochrisiko-KI-System, GPAI-System oder allgemeinen Chatbot ein und fragt nach Betreiberpflichten. Art. 26 KI-VO: bestimmungsgemaesse Verwendung, menschliche Aufsicht, Eingabedaten, Protokolle, Vorfallm... |
| `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25` | Drittstaaten-Anbieter ohne EU-Niederlassung oder Produkthersteller fragt: Wer vertritt uns in der EU und wer haftet für integrierte KI-Komponenten? Art. 22 KI-VO Bevollmaechtigter Art. 25 Produkthersteller. Prüfraster: Bevollmaechtigter... |
| `code-of-practice-und-harmonisierte-normen` | Normen- und Standards-Landkarte fuer KI-VO-Compliance: Art. 40 harmonisierte Normen, Art. 41 gemeinsame Spezifikationen, Art. 56 GPAI Code of Practice, ISO/IEC 42001 / 23894 / 22989 / 23053 sowie Sicherheits- und Datenschutzstandards. Er... |
| `einfuehrer-importer-pflichten-art-23` | Importeur von KI-Systemen aus Drittstaaten fragt: Was muss ich prüfen bevor ich ein Hochrisiko-KI-System in der EU in Verkehr bringe? Art. 23 KI-VO Einführer-Pflichten. Prüfraster: Konformitätsbewertung durch Anbieter bereits durchgeführ... |
| `entscheidungsbaum-ki-vo-gesamt-workflow` | Master-Workflow fuer die vollstaendige KI-VO-Pruefung. Fuehrt von Art. 3 KI-System-Definition ueber Anwendungsbereich, Rollen, Art. 6 Abs. 2/Anhang III-Hochrisiko, Rueckausnahme, GPAI/Chatbot-Abgrenzung, Betreiber-Fehlgebrauch, Pflichten... |
| `eu-datenbank-registrierung-art-49-und-71` | Anbieter oder Betreiber von Hochrisiko-KI fragt: In welcher EU-Datenbank muss ich mein KI-System registrieren und wann? Art. 49 und 71 KI-VO Registrierungspflichten. Prüfraster: Anbieter vor Inverkehrbringen Pflicht Art. 49 Abs. 1 öffent... |
| `falsche-wiese-warnung-ki-vo` | Nutzer fragt eine KI-VO-Frage die eigentlich unter DSGVO Produkthaftung MDR oder Maschinenverordnung faellt. Warnt vor typischen Rechtsgebiets-Verwechslungen KI-VO versus DSGVO versus Produkthaftungsrichtlinie versus Medizinprodukteveror... |
| `governance-aufsichtsbehoerden-art-70` | Unternehmen oder Behoerde fragt: An wen muss ich mich in Deutschland und Europa wenden wenn ich Fragen zur KI-VO-Aufsicht habe oder eine Meldepflicht erfullen muss? Art. 70 ff. KI-VO Governance. Prüfraster: nationale Aufsichtsbehoerden A... |
| `gpai-modelle-art-51-bis-55` | Entwickler oder Anbieter eines Sprachmodells oder Basismodells fragt: Fallen wir unter die GPAI-Pflichten der KI-VO und was muessen wir konkret tun? Art. 51 bis 55 KI-VO GPAI-Modelle. Prüfraster: technische Dokumentation Anhang XI Urhebe... |
| `gpai-systemisches-risiko-schwelle-10e25-flop` | Anbieter eines sehr grossen Basismodells fragt: Haben wir die Schwelle für systemisches Risiko ueberschritten und welche Zusatzpflichten gelten dann? Art. 51 und 55 KI-VO GPAI systemisches Risiko. Prüfraster: Schwellenwert 10 hoch 25 FLO... |
| `gpai-vorliegen-art-3-nr-63` | Prueft, ob ein Modell oder Dienst ein General-Purpose-AI-Modell oder GPAI-System nach der KI-VO ist und grenzt GPAI von Hochrisiko-KI ab. Behandelt ChatGPT-aehnliche Systeme, Foundation Models, API-Nutzung, GPAI-System Art. 3 Nr. 66, sys... |
| `haendler-distributor-pflichten-art-24` | Distributeur oder Grosshaendler von KI-Systemen fragt: Welche Sorgfaltspflichten habe ich beim Weitervertrieb von Hochrisiko-KI? Art. 24 KI-VO Haendler-Pflichten. Prüfraster: Plausibilitaetsprüfung CE-Kennzeichnung vorhanden EU-Konformit... |
| `hochrisiko-art-6-abs-1-sicherheitsbauteil` | Unternehmen integriert KI-Komponente in ein reguliertes Produkt (Medizinprodukt Maschine Fahrzeug) und fragt: Wird das Gesamtprodukt dadurch zum Hochrisiko-KI-System? Art. 6 Abs. 1 KI-VO Sicherheitsbauteil Anhang I. Prüfraster: ist Produ... |
| `hochrisiko-art-6-abs-2-anhang-iii` | Vertiefter Hochrisiko-Checker fuer Art. 6 Abs. 2 i.V.m. Anhang III KI-VO. Prueft alle acht Anhang-III-Bereiche mit Untertatbestaenden, Zweckbestimmung, konkretem Einsatzkontext, GPAI/Chatbot-Abgrenzung und Mitarbeitenden-Fehlgebrauch. Er... |
| `hochrisiko-aufzeichnungspflichten-logging-art-12` | Anbieter von Hochrisiko-KI fragt: Was muss unser System automatisch aufzeichnen und wie lange muessen wir die Logs aufbewahren? Art. 12 KI-VO Logging-Pflichten. Prüfraster: Mindestinhalte der Logs Zeitstempel Eingabedaten Ausgaben Fehler... |
| `hochrisiko-bestaetigt-end-to-end-roadmap` | Anbieter hat Hochrisiko-Einstufung des eigenen KI-Systems bestätigt und fragt: Was sind jetzt alle noetigen Schritte bis zur CE-Kennzeichnung und Marktfreigabe? End-to-End-Roadmap Hochrisiko-KI Art. 9 bis 49 KI-VO. Prüfraster: zwoelf Sch... |
| `hochrisiko-datenqualitaet-und-data-governance-art-10` | Anbieter von Hochrisiko-KI fragt: Welche Anforderungen gelten für unsere Trainings- Validierungs- und Testdaten und wie dokumentieren wir unsere Data Governance? Art. 10 KI-VO Datenqualitaet und Data Governance. Prüfraster: Relevanz Repr... |
| `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15` | Anbieter von Hochrisiko-KI fragt: Welche Leistungsstandards für Genauigkeit Robustheit und Cybersicherheit muessen wir nachweisen und dokumentieren? Art. 15 KI-VO Mindeststandards. Prüfraster: Genauigkeitsmetriken und Leistungserklärung... |
| `hochrisiko-konformitaetsbewertung-art-43-bis-49` | Anbieter von Hochrisiko-KI fragt: Muessen wir eine benannte Stelle einschalten oder koennen wir die Konformitätsbewertung selbst durchführen? Art. 43 bis 49 KI-VO Konformitätsbewertung. Prüfraster: Entscheidungsbaum Selbstbewertung Modul... |
| `hochrisiko-menschliche-aufsicht-art-14` | Anbieter oder Betreiber fragt: Wie stellen wir sicher dass Menschen das Hochrisiko-KI-System wirksam beaufsichtigen und uebersteuerung ist möglich? Art. 14 KI-VO menschliche Aufsicht. Prüfraster: Verstehen der Systemfähigkeiten und Grenz... |
| `hochrisiko-risikomanagementsystem-art-9` | Anbieter von Hochrisiko-KI fragt: Wie setzen wir ein KI-VO-konformes Risikomanagementsystem auf und was muss es enthalten? Art. 9 KI-VO Risikomanagementsystem. Prüfraster: kontinuierlicher iterativer Prozess Risikoidentifikation Risikoab... |
| `hochrisiko-technische-dokumentation-art-11-und-anhang-iv` | Anbieter von Hochrisiko-KI fragt: Was muss die technische Dokumentation enthalten und wie aktuell muss sie sein? Art. 11 i.V.m. Anhang IV KI-VO. Prüfraster: vollständiger Inhaltskatalog nach Anhang IV Systembeschreibung Entwicklungsproze... |
| `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13` | Anbieter von Hochrisiko-KI fragt: Welche Informationen muessen wir dem Betreiber in der Gebrauchsanweisung zur Verfuegung stellen? Art. 13 KI-VO Transparenz und Informationspflichten. Prüfraster: Gebrauchsanweisung Mindestinhalt Art. 13... |
| `hochrisiko-zuordnung-art-6-und-anhang-i-iii` | Gesamtuebersicht zur Hochrisiko-Zuordnung nach Art. 6 KI-VO: Art. 6 Abs. 1 Sicherheitsbauteil/Anhang I und Art. 6 Abs. 2/Anhang III. Erklaert Zweckbestimmung, allgemeine Chatbots/GPAI, Mitarbeitenden-Fehlgebrauch, Rueckausnahme Art. 6 Ab... |
| `liegt-ki-system-vor-art-3-nr-1` | Erster Schritt jeder KI-VO-Pruefung: Ist die Software, API, App, Automatisierung oder Modellkette ein KI-System nach Art. 3 Nr. 1 KI-VO? Prueft maschinenbasiertes System, Autonomie, optionale Adaptivitaet, Ziele, Inferenz, Output-Typen u... |
| `mandatsabbruch-empfehlung-komplexe-faelle` | Mechanik-Workflow erkennt Anzeichen von Faellen die anwaltliche Spezialkenntnisse erfordern und empfiehlt Eskalation. Indikatoren für Komplexitaet jenseits des KI-VO-Prüfers: multijurisdiktionelle Lieferketten marktbeherrschende Stellung... |
| `marktueberwachung-meldung-vorfaelle-art-72-bis-79` | Anbieter oder Betreiber hat einen schwerwiegenden Vorfall mit einem Hochrisiko-KI-System und fragt: Was muss gemeldet werden an wen und innerhalb welcher Fristen? Art. 72 bis 79 KI-VO Post-Market-Monitoring und Meldepflichten. Prüfraster... |
| `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` | Prüfung hat ergeben: kein Hochrisiko. Unternehmen fragt: Welche KI-VO-Pflichten gelten trotzdem und wie dokumentieren wir das Negativ-Ergebnis rechtssicher? Drei Pfade Anhang I/III nicht zutreffend Rückausnahme Art. 6 Abs. 3 oder verbote... |
| `output-betreiber-checkliste-und-folgenabschaetzung` | Betreiber von Hochrisiko-KI benoetigt fertige Compliance-Dokumentation für interne Zwecke oder Aufsichtsbehoerde. Art. 26 und 27 KI-VO Betreiber-Compliance-Output. Zwei Output-Dokumente: Betreiber-Compliance-Checkliste Art. 26 mit allen... |
| `output-konformitaetsbescheinigung-evidence-pack` | Druckreifes KI-VO-Konformitätspaket erzeugen: interne Konformitätsbescheinigung, EU-Konformitätserklärung nach Art. 47/Anhang V, Art.-43-Bewertungsnachweis, CE-/EU-DB-/Post-Market-Check, Evidence Index und Lückenliste ohne falsche Besche... |
| `output-konformitaetserklaerung-eu-anhang-v` | Anbieter benoetigt das fertige Musterdokument für die EU-Konformitätserklärung zum Ausfuellen und Unterzeichnen. Art. 47 i.V.m. Anhang V KI-VO EU-Konformitätserklärung. Pflichtinhalt Anhang V: eindeutige Systemidentifikation Anbieter Bev... |
| `output-pruefdokument-ki-vo-mit-warnhinweisen` | Erzeugt das abschliessende KI-VO-Pruefdokument mit Warnhinweisen, Tatsachenbasis und dokumentierbarer Begruendung. Deckt Art. 3 KI-System-Vermerk, Zweckbestimmung, GPAI/Chatbot-Abgrenzung, Art. 6 Abs. 2/Anhang III, Art. 6 Abs. 3-Rueckaus... |
| `persoenlicher-anwendungsbereich-rollen-art-3` | Erster Schritt der KI-VO-Prüfung: Wer ist betroffen? Unternehmen fragt welche Rolle es in der KI-VO einnimmt. Art. 3 KI-VO Rollendefinitionen. Prüfraster: Anbieter Art. 3 Nr. 3 Betreiber Art. 3 Nr. 4 Einführer Art. 3 Nr. 6 Haendler Art.... |
| `risikoklassen-uebersicht-und-triage` | Schnelle Risikoklassen-Triage nach KI-VO mit Fokus auf Art. 6 Abs. 2 und Anhang III. Prueft verboten, Hochrisiko nach Art. 6 Abs. 1/2, Rueckausnahme Art. 6 Abs. 3, begrenztes Risiko Art. 50, GPAI und minimales Risiko. Behandelt allgemein... |
| `rolle-anbieter-pruefen-art-3-nr-3` | Unternehmen das Software oder KI entwickelt fragt: Sind wir Anbieter im Sinne der KI-VO und welche Pflichten treffen uns deshalb? Art. 3 Nr. 3 KI-VO Anbieter-Definition. Prüfraster: Entwicklung oder Beauftragung Entwicklung Inverkehrbrin... |
| `rolle-betreiber-pruefen-art-3-nr-4` | Unternehmen kauft oder lizenziert ein KI-System von einem Anbieter und fragt: Sind wir Betreiber im Sinne der KI-VO und was muessen wir tun? Art. 3 Nr. 4 KI-VO Betreiber-Definition. Prüfraster: Verwendung in eigener Verantwortung Abgrenz... |
| `rueckausnahme-art-6-abs-3` | Prueft nach positiver Anhang-III-Zuordnung, ob ein KI-System ausnahmsweise nicht Hochrisiko ist. Art. 6 Abs. 3 KI-VO: kein erhebliches Risiko fuer Gesundheit, Sicherheit oder Grundrechte, vier enge Fallgruppen, Profiling-Sperre, Begruend... |
| `sachlicher-ausschluss-art-2-abs-3-bis-12` | Unternehmen fragt: Faellt unser KI-System möglicherweise voellig aus dem Anwendungsbereich der KI-VO heraus? Art. 2 Abs. 3 bis 12 KI-VO sachliche Ausnahmen. Prüfraster: Militaer und nationale Sicherheit Art. 2 Abs. 3 wissenschaftliche Fo... |
| `sanktionen-art-99-bis-101` | Unternehmen moechte die Kostenrisiken einer KI-VO-Verletzung einschaetzen oder Vorstand über Bußgelddimensionen informieren. Art. 99 bis 101 KI-VO Sanktionen. Prüfraster: bis 35 Mio EUR oder 7 Prozent Konzernumsatz bei verbotenen Praktik... |
| `territorialer-anwendungsbereich-art-2` | Nicht-EU-Unternehmen oder Exporteur fragt: Gilt die KI-VO auch für uns obwohl wir außerhalb der EU sind? Art. 2 KI-VO territorialer Anwendungsbereich. Prüfraster: Inverkehrbringen in der EU Nutzung in der EU durch Betreiber Ausgaben die... |
| `triage-ki-vo-vorpruefung` | Nutzer kommt mit unklarer KI-VO-Frage oder möglicherweise betroffener Software und fragt: Wie starte ich die KI-VO-Prüfung? Eingangs-Triage-Skill. Prüfraster: Erfassung ob eigene Softwareentwicklung fremder Dienst Produktintegration oder... |
| `verbotene-praktiken-art-5` | Unternehmen prüft ob ein KI-Einsatz in den Bereich der absolut verbotenen KI-Praktiken faellt. Art. 5 KI-VO Verbotskatalog. Prüfraster: alle acht verbotenen Praktiken subliminale Techniken Vulnerabilitaetsausnutzung Social Scoring Predic... |
| `verhaeltnis-zu-anderen-unionsrechtsakten` | Anwalt oder Compliance-Beauftragter fragt: Gilt neben der KI-VO noch ein anderes EU-Gesetz für das gleiche System und wie interagieren die Pflichten? Art. 2 Abs. 2 KI-VO Verhältnis zu anderen Rechtsakten. Prüfraster: DSGVO Maschinenveror... |
| `zeitlicher-geltungsbereich-uebergangsfristen` | Compliance-Beauftragter oder Unternehmen fragt: Ab wann muessen welche KI-VO-Pflichten eingehalten werden und welche Systeme sind schon heute betroffen? KI-VO Übergangsfristen und Zeitplan. Prüfraster: Inkrafttreten 1. August 2024 Verbot... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
