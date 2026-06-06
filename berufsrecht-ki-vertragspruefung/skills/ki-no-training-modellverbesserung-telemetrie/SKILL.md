---
name: ki-no-training-modellverbesserung-telemetrie
description: "No-Training, Modellverbesserung und Telemetrie im KI-Vertrag prüfen: Mandatsdaten dürfen nicht für Training, Produktverbesserung, Benchmarks, Supportauswertung oder allgemeine Modelloptimierung abfließen; Klausel- und Rückfragebausteine."
---

# No-Training, Modellverbesserung und Telemetrie

## Leitgedanke

Die Dienstleistung darf Mandatsdaten verarbeiten, soweit das für den beauftragten Zweck nötig ist. Daraus folgt nicht, dass der Anbieter diese Daten für Training, allgemeine Produktverbesserung, Benchmarks, Qualitätsdatenbanken oder Vertriebsanalysen nutzen darf.

## Prüfungslinien

- **Training:** Fine-Tuning, Reinforcement Learning, supervised review, synthetische Trainingsdaten aus Mandatsinput.
- **Produktverbesserung:** Qualitätsmetriken, Fehleranalyse, Modellvergleiche, Prompt-/Output-Sammlungen.
- **Telemetrie:** Prompt-Logs, Nutzungsprofile, Tokenstatistik mit Inhaltsbezug, Abuse Monitoring.
- **Support:** Einsicht durch Supportteams, Screenshots, Debugging, Ticketanhänge.
- **Subunternehmer:** Modellhoster, Vektor-Datenbank, Logging-Dienst, Security-Provider.
- **Retention:** Speicherdauer für Inputs, Outputs, Embeddings, Metadaten, Backups.

## Rote Formulierungen

- "may use Customer Content to improve services" ohne Berufsgeheimnis-Ausnahme
- "de-identified data" ohne strenge Lösch-/Reidentifikationsregeln
- "analytics and product development" als offene Generalklausel
- Supportzugriff ohne Need-to-know, Protokollierung und Kanzleifreigabe
- Subprocessor-Liste ohne Zustimmungsvorbehalt

## Mindestklauseln

Fordere:

1. Keine Nutzung von Mandatsdaten für Training oder allgemeine Modellverbesserung.
2. Keine dauerhafte Speicherung von Prompts/Outputs außerhalb der vereinbarten Retention.
3. Supportzugriffe nur fallbezogen, protokolliert, möglichst nach Freigabe.
4. Embeddings und Vektor-Datenbanken mandats- oder mandantengetrennt.
5. Subunternehmer nur mit Weiterverpflichtung und Änderungsnotice.
6. Lösch- und Exportpfad bei Vertragsende.

## Output

Erstelle eine Vertragslückenliste mit:

- Fundstelle im Vertrag
- Risiko für § 43e BRAO, § 203 StGB, DSGVO
- konkrete Nachverhandlungsklausel
- Anbieterfrage in höflicher, aber unmissverständlicher Sprache
