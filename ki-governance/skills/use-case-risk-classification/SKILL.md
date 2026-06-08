---
name: use-case-risk-classification
description: "Use-Case-Risikoklassifizierung nach KI-VO und DSGVO: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Ki Governance."
---

# Use-Case-Risikoklassifizierung nach KI-VO und DSGVO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Use-Case-Risikoklassifizierung nach KI-VO und DSGVO** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## KI-VO-Klassifizierungslogik (VO (EU) 2024/1689)
- **Verboten (Art. 5 KI-VO, gilt ab 02.02.2025)**: u. a. Social Scoring durch öffentliche Stellen, manipulative Techniken, biometrische Kategorisierung nach sensiblen Merkmalen, Echtzeit-Fernidentifikation im öffentlichen Raum.
- **Hochrisiko (Art. 6 i. V. m. Anhang III, gilt ab 02.08.2026)**: u. a. Bildung, Beschäftigung (Recruiting, Performance), kritische Infrastruktur, Strafverfolgung, biometrische Identifikation, Migration, Justiz und demokratische Prozesse, Gesundheits-/Lebensversicherungs-Risikoscoring.
- **Begrenztes Risiko mit Transparenzpflicht (Art. 50)**: Chatbots, Emotionserkennung, biometrische Kategorisierung, Deepfakes.
- **Minimales Risiko**: alle übrigen Systeme.

## Schnittstelle zur DSGVO
- **Art. 35 DSGVO DSFA** ist regelmäßig erforderlich, wenn Hochrisiko-KI-VO-System personenbezogene Daten verarbeitet.
- **Art. 22 DSGVO** Verbot automatisierter Einzelentscheidungen mit rechtlicher Wirkung; Ausnahmen (Vertragserfordernis, Einwilligung, gesetzliche Erlaubnis) erfordern menschliche Aufsicht.
- **Art. 27 KI-VO**: Folgenabschätzung für Grundrechte durch Betreiber (Fundamental Rights Impact Assessment, FRIA) zusätzlich zur DSGVO-DSFA.

## Klassifizierungs-Trade-offs
- "Empfehlungssystem im HR" — meistens **Hochrisiko** nach Anhang III Nr. 4 ("Beschäftigung, Personalverwaltung").
- "Reiner Übersetzer" mit Kundendaten — typischerweise **minimales Risiko**, aber DSGVO-Schiene voll relevant.
- "RAG-System mit Mandantenakten in Kanzlei" — kein KI-VO-Hochrisiko, aber Berufsrecht und § 203 StGB greifen.
- "Foundation Model intern aufgesetzt" — als GPAI nach Art. 51 ff. KI-VO eigene Kategorie, ab 10²⁵ FLOP systemisches Risiko.

## Output für Inventar
- Use-Case-ID, Kurzbeschreibung, Geschäftsbereich
- KI-VO-Klassifizierung mit Norm und Begründung
- DSGVO-Rechtsgrundlage Art. 6, ggf. Art. 9
- Rolle (Anbieter Art. 3 Nr. 3 vs. Betreiber Art. 3 Nr. 4)
- Status DSFA, FRIA
- Verantwortliche Person und Review-Frist

## Trade-off
Frühzeitige sorgfältige Klassifizierung ist günstiger als spätere Reklassifizierung; ein als "minimal" eingestuftes System, das später als Hochrisiko erkannt wird, erzwingt nachträgliche Konformitätsbewertung (Art. 43 KI-VO), Logging-Aufbau (Art. 12) und technische Dokumentation (Art. 11) — oft mit Marktrückzug oder kostspieliger Anpassung.

