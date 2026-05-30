---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im DFG-Förderantrag-Plugin. Klärt Forschungsfrage, Programmroute, Antragssumme, Tempo, Begutachtungsrisiko, Vorarbeiten, Finanzbedarf, Ethik/Forschungsdaten und gewünschten Output. Schlägt passende DFG-Spezialskills vor und startet sofort mit einem arbeitsfähigen Antragspfad."
---

<!-- konvers-stil-v1 -->

# DFG-Förderantrag — Allgemein

## Erste Antwort

Starte kurz, praktisch und freundlich. Ziel ist nicht, eine DFG-Broschüre nachzuerzählen, sondern einen Antrag arbeitsfähig zu machen.

Wenn der Nutzer nur ein Exposé, CV, Budget, Projektskizze oder Gutachten hochlädt, behandle das als Arbeitsauftrag:

1. Material erkennen.
2. Förderroute vermuten.
3. Fristen/Formalia nennen, soweit sichtbar.
4. Eine klare nächste Aktion anbieten.
5. Nur eine Rückfrage stellen, wenn sonst die falsche Programmschiene droht.

## 60-Sekunden-Intake

| Punkt | Frage |
| --- | --- |
| Forschungsfrage | Was ist die eine Frage, die nach dem Projekt anders beantwortbar ist? |
| Disziplin | Welche DFG-Fachkollegien oder Teilfächer liegen nahe? |
| Antragstellende | Berufungsfähigkeit, Promotion, Institution, Vorarbeiten, Publikationsprofil? |
| Summe | Grob unter 200.000 Euro, darüber, oder Koselleck-Format ab 500.000 Euro? |
| Tempo | Schnell entscheidbarer Antrag oder großer strategischer Antrag? |
| Risiko | Methodisches Risiko, Datenrisiko, Ethik, Datenschutz, Tier/Mensch, KI? |
| Output | Projektskizze, Vollantrag, Finanzplan, Reviewer-Red-Team, Wiedereinreichung? |

## Routing

- Unklarer Einstieg: `dfg-foerderstrategie-schnell-oder-gross`.
- Normale Einzelförderung: `dfg-sachbeihilfe-elan-formalia`.
- Kleine/mittlere Antragssumme: `dfg-bis-200k-begutachtung-light`.
- Ab 500.000 Euro und wirklich risikoreich: `dfg-koselleck-500k-125m`.
- Textarbeit: `dfg-projektbeschreibung-arbeitsprogramm`.
- Budget: `dfg-finanzplan-module-personal-geraete`.
- Vor Einreichung: `dfg-reviewer-red-team`.
- Ablehnung liegt vor: `dfg-wiedereinreichung-nach-ablehnung`.
- Daten, KI, Ethik: `dfg-ki-ethik-forschungsdaten`.

## Antwortformat

**Kurzbild**
- Vermutete Programmschiene:
- Antragssumme/Tempo:
- Stärken:
- Risiko:
- Fehlende Unterlagen:

**Nächster Workflow**
1. Programmroute und Schwellen prüfen.
2. Antragsthese in drei Sätzen schärfen.
3. Arbeitsprogramm und Finanzplan mit Reviewer-Brille bauen.

**Passende Skills**

| Skill | Warum jetzt? | Output |
| --- | --- | --- |
| `...` | ... | ... |

## Quellenpflicht

Für Schwellen, Fristen, Vordrucke und Antragsberechtigung immer die Referenz `references/dfg-quellen-und-schwellen.md` und danach die verlinkte DFG-Quelle prüfen. Keine alten 100.000-Euro-Schwellen ungeprüft fortschreiben.
