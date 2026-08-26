---
name: datenschutz-dsgvo-im-lizenzvertrag
description: "Für Datenschutz — DSGVO im Lizenzvertrag: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Datenschutz — DSGVO im Lizenzvertrag

## Wann DSGVO einschlaegig?

| Konstellation | DSGVO-relevant |
|---|---|
| Lizenz Software, die personenbezogene Daten verarbeitet | ja (AVV Art. 28 DSGVO) |
| Lizenz Datenbank mit personenbezogenen Daten | ja (Datentransfer) |
| Lizenz KI-Modell, trainiert mit personenbezogenen Daten | mittel - Trainingsdaten-Schutz, ggf. Modellausgaben |
| Lizenz Marke + Kundendaten | wie Marken-Lizenz mit Datenuebermittlung im Asset Deal |
| Reine Patent-Lizenz ohne Datenfluss | nein |
| Reine Marken-Lizenz ohne Datenfluss | nein |

## Drei Rollenkonstellationen

### A. Verantwortlicher / Auftragsverarbeiter (Art. 28 DSGVO)

Lizenzgeber liefert Software/SaaS; Lizenznehmer ist Verantwortlicher; Lizenzgeber Auftragsverarbeiter. → Pflicht-AVV nach Art. 28 III DSGVO.

### B. Joint Controllership (Art. 26 DSGVO)

Beide Parteien bestimmen gemeinsam Zweck und Mittel der Verarbeitung; typisch bei Cross-License/Forschungspartnerschaft. → Vereinbarung mit Verantwortlichkeitsabgrenzung.

### C. Eigenstaendige Verantwortliche

Überträgt eine Lizenzgestaltung Daten vom Lizenzgeber an den Lizenznehmer, ist die Verantwortlichkeit beider Seiten getrennt zu bestimmen. Artikel 6 Absatz 1 Buchstabe f DSGVO verlangt ein rechtmäßiges Interesse, Erforderlichkeit einschließlich Datenminimierung und eine konkrete Interessenabwägung; Artikel 14 DSGVO ist gesondert zu prüfen. EuGH, Urteil vom 04.10.2024 - C-621/22 (KNLTB) dient nur als Anker dafür, dass ein kommerzielles Interesse grundsätzlich berechtigt sein kann.

## Drittlands-Uebermittlung Art. 44 ff. DSGVO

Bei Datenuebermittlung in Drittlaender:

1. Angemessenheitsbeschluss (z. B. EU-USA Data Privacy Framework seit 2023)
2. Standard Contractual Clauses (SCCs) - neue Version 2021/914
3. Binding Corporate Rules
4. Ad-hoc-Klauseln

→ Nach Schrems II (EuGH C-311/18): Transfer Impact Assessment (TIA) bei jedem Drittlandstransfer Pflicht.

## Klausel-Bausteine

**A. Auftragsverarbeitung-Klausel:**
> "Paragraf 18 Datenschutz.
> (1) Soweit der Lizenzgeber im Rahmen dieses Vertrages personenbezogene Daten des Lizenznehmers im Auftrag verarbeitet, schliessen die Parteien einen Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO ab (**Anlage D**).
> (2) Der Lizenzgeber verpflichtet sich, technische und organisatorische Maßnahmen nach Art. 32 DSGVO einzuhalten.
> (3) Der Lizenzgeber wird bei Anfragen von Aufsichtsbehoerden oder bei Datenpannen den Lizenznehmer unverzueglich informieren."

**B. Drittlandstransfer:**
> "(4) Eine Uebermittlung personenbezogener Daten in Drittlaender erfolgt nur auf der Grundlage eines Angemessenheitsbeschlusses, der Standard-Vertragsklauseln (SCC 2021/914) oder anderer geeigneter Garantien nach Art. 46 DSGVO."

**C. Joint Controllership:**
> "Sofern die Parteien gemeinsam über Zwecke und Mittel der Verarbeitung entscheiden, gilt zwischen ihnen die in **Anlage E** beigefuegte Joint-Controllership-Vereinbarung gem. Art. 26 DSGVO."

**D. Bei Kunden-Daten-Lizenz (z. B. CRM-Daten als Asset):**
> "Die Uebermittlung personenbezogener Daten von Endkunden des Lizenzgebers an den Lizenznehmer erfolgt auf Grundlage des berechtigten Interesses (Art. 6 I lit. f DSGVO). Die Endkunden werden gem. Art. 14 DSGVO informiert; ihnen wird eine 30-Tage-Widerspruchsfrist eingeraeumt. Bei Widerspruch werden die jeweiligen Datensaetze binnen 7 Werktagen vom Lizenznehmer geloescht."

## Anschluss

- Kunden-Daten-Behandlung im Asset Deal: siehe `testakten/insolvenz-asset-deal-chaincortex-ai-berlin/07_kundendaten-dsgvo-analyse.md`
- EuGH, Urteil vom 04.10.2024 - C-621/22 (KNLTB) - vor Zitierung im Volltext auf `curia.europa.eu` verifizieren; die Entscheidung ersetzt weder Erforderlichkeits- noch Abwägungsprüfung.
