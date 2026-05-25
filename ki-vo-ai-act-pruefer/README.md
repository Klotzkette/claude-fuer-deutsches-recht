# ki-vo-ai-act-pruefer

Vollständiger Mechanik-Workflow zur Verordnung (EU) 2024/1689 (KI-VO): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Pflichten, GPAI-Modelle, Sanktionen und Entscheidungsbaum-Workflow.

**Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.**

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| ki-vo-ai-act-pruefer | [ki-vo-ai-act-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-vo-ai-act-pruefer.zip) |

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

Der KI-VO-Prüfer ist ein interaktives Mechanik-Plugin für die vollständige Prüfung von KI-Systemen nach der Verordnung (EU) 2024/1689. Er führt den Nutzer in einem sequenziellen Entscheidungsbaum durch alle relevanten Fragen:

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

## Skills (44 Stück)

### Einstieg

- **`entscheidungsbaum-ki-vo-gesamt-workflow`** — Master-Workflow: Start hier für vollständige Prüfung
- **`triage-ki-vo-vorpruefung`** — Erfassung des Sachverhalts

### End-to-End-Roadmaps nach Diagnose

- **`hochrisiko-bestaetigt-end-to-end-roadmap`** — zwölf Schritte vom Risikomanagement bis zu CE-Kennzeichnung, EU-DB-Registrierung und Marktbeobachtung; mit Aufwandsschätzung, Akteur-Übersicht (notifizierte Stelle, Marktaufsicht, AI Office, Sektor-Regulatoren) und Markteintritts-Checkliste.
- **`nicht-hochrisiko-bestaetigt-end-to-end-roadmap`** — drei Wege zur Negativ-Diagnose (Anhang nicht zutreffend / Rückausnahme Art. 6 Abs. 3 / kein KI-System), Restpflichten Art. 4, Art. 5, Art. 50, GPAI, sektoral, Dokumentationspflicht und Re-Evaluation-Trigger.

### A. KI-System-Definition

- `liegt-ki-system-vor-art-3-nr-1` — Kernskill: Definition KI-System
- `abgrenzung-konventionelle-software-vs-ki-system` — Grenzfälle
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
- `hochrisiko-art-6-abs-2-anhang-iii` — Pfad 2: Anhang III (alle acht Bereiche)
- `rueckausnahme-art-6-abs-3` — Vier Fallgruppen + Profiling-Sicherungsklausel
- `hochrisiko-zuordnung-art-6-und-anhang-i-iii` — Übersicht
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

- `gpai-vorliegen-art-3-nr-63` — Definition und Abgrenzung
- `gpai-modelle-art-51-bis-55` — Anbieterpflichten
- `gpai-systemisches-risiko-schwelle-10e25-flop` — Schwellenwert und Zusatzpflichten
- `code-of-practice-und-harmonisierte-normen`

### H. Governance und Sanktionen

- `governance-aufsichtsbehoerden-art-70`
- `sanktionen-art-99-bis-101`
- `marktueberwachung-meldung-vorfaelle-art-72-bis-79`

### I. Registrierung

- `eu-datenbank-registrierung-art-49-und-71` — Wann und wie registrieren?

### J. Output-Dokumente

- `output-pruefdokument-ki-vo-mit-warnhinweisen`
- `output-konformitaetserklaerung-eu-anhang-v`
- `output-betreiber-checkliste-und-folgenabschaetzung`

---

## Wichtige Hinweise

- **Keine Rechtsberatung.** Dieses Plugin liefert mechanische Prüfungen, keine anwaltliche Beratung.
- **Dynamisches Rechtsgebiet.** Die KI-VO wird durch Leitlinien der Kommission, harmonisierte Normen und Durchführungsrechtsakte laufend konkretisiert.
- **Übergangsfristen beachten.** Nicht alle Pflichten sind bereits anwendbar — siehe `zeitlicher-geltungsbereich-uebergangsfristen`.
- **Fachanwalt bei Hochrisiko.** Bei verbotenen Praktiken, Hochrisiko-KI und GPAI-Modellen mit systemischem Risiko ist ein Fachanwalt für IT-Recht hinzuzuziehen.

---

## Lizenz

Apache-2.0 OR MIT

Autor: Klotzkette
