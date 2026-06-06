---
name: inventar-kontrollen-konformitaetsbewertung
description: "KI-Inventar, Governance und Kontrollen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Ki Governance: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# KI-Inventar, Governance und Kontrollen

## Arbeitsbereich

KI-Inventar, Governance und Kontrollen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `ki-governance`. Kontext des Plugins: EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

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
3. **Materielle Weichen:** Die Kernfragen zu **KI-Inventar, Governance und Kontrollen** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Pflichtelemente KI-Inventar
Das Inventar ist Voraussetzung für jede AI-Governance und Rückgrat der KI-VO-Konformität (Art. 12, 16, 49, 72 KI-VO):

- **Identifikation**: Use-Case-ID, interner Eigentümer, Geschäftsbereich, Status (Pilot, Produktion, abgeschaltet).
- **System-/Modellinformation**: Anbieter, Produktname, Version, Modellfamilie (z. B. GPAI gem. Art. 3 Nr. 63 KI-VO), Hosting-Region, Datenresidenz.
- **Rollenzuordnung**: Anbieter Art. 3 Nr. 3, Betreiber Art. 3 Nr. 4, Importeur Art. 3 Nr. 6, Händler Art. 3 Nr. 7. Wechselt die Rolle bei substantieller Modifikation (Art. 25 KI-VO)?
- **Risikoklassifizierung**: Verboten (Art. 5) / Hochrisiko (Anhang III) / Begrenztes Risiko (Art. 50) / Minimal.
- **Datenkategorien**: personenbezogen (Art. 4 Nr. 1 DSGVO), besondere Kategorien (Art. 9), Mandantengeheimnis, IP.
- **DSGVO-Status**: Rechtsgrundlage Art. 6, DSFA Art. 35 abgeschlossen, AVV Art. 28 abgeschlossen.
- **KI-VO-Status**: Risikomanagementsystem Art. 9, Datenqualität Art. 10, Technische Dokumentation Art. 11, Logging Art. 12, Transparenz Art. 13, Aufsicht Art. 14, Genauigkeit/Cyber Art. 15, Konformitätsbewertung Art. 43.

## Kontroll-Architektur
- **Governance-Komitee**: AI Officer, Datenschutzbeauftragte/r, CISO, Compliance, Fachbereich.
- **Three Lines of Defense**: Fachbereich → Compliance/Datenschutz → Interne Revision.
- **Lebenszyklus-Reviews**: Onboarding, jährlicher Review, anlassbezogene Reklassifizierung, Sunset/Off-Boarding mit Datenlöschung.
- **Vorfallmanagement**: Vorfälle Art. 73 KI-VO (Marktüberwachung-Meldung bei Hochrisiko), DSGVO Art. 33/34, NIS-2 falls einschlägig.

## Schnittstelle Kanzlei-Praxis
KI-Inventar ist auch für Berufsträger relevant (§§ 43e BRAO / 62a StBerG / 50a WPO): pro Tool dokumentieren, ob Mandantendaten verarbeitet werden, ob Verpflichtungserklärung gem. § 203 Abs. 4 StGB vorliegt, ob Trainingsausschluss vereinbart ist.

## Trade-off
Schlankes Inventar (Tabelle) ist schnell aufgesetzt, aber ohne Lebenszyklus- und Eskalations-Hooks substanzarm. Vollständige GRC-Tool-Integration (z. B. mit AIA/DPIA-Workflow) ist aufwendig, schafft aber Auditierbarkeit. Pragmatischer Mittelweg: Tabelle + Trigger-Mails bei Klassifizierungsänderung oder neuem Geltungstermin der KI-VO-Stufen.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.
