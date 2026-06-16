---
name: fachanwalt-insolvenz-idw-s6-sanierungskonzept
description: "Erstellt und prüft Sanierungskonzepte auf IDW-S-6-Niveau aus anwaltlicher Sicht. Führt durch Fortbestehensprognose, Sanierungsfähigkeit, Krisenursachen, Leitbild des sanierten Unternehmens, Maßnahmenpakete, integrierte Planung, kleinere Unternehmen, Dokumentation, Haftungs- und Verhandlungsrisiken. Output: Mandantenmemo, Bank-/Gläubigerunterlage, Datenanforderung, Red-Team-Liste und Entscheidungsampel."
---

# Sanierungskonzept auf IDW-S-6-Niveau

## Aufgabe

Dieser Skill macht aus einer unsortierten Krisenakte ein anwaltlich belastbares Sanierungskonzept oder prüft ein vorgelegtes Konzept auf Schwachstellen. Er arbeitet pragmatisch: erst Insolvenzreife und Fristen sichern, dann Sanierungsfähigkeit prüfen, dann den richtigen Output für Mandant, Bank, Gläubiger, Gericht oder Investor erstellen.

Der Skill erstellt keine Prüfungsbescheinigung. Er unterstützt die anwaltliche Strukturierung, Plausibilisierung, Dokumentation und Verhandlungsfähigkeit.

## Kaltstart

Wenn der Nutzer nur "Sanierungskonzept", "IDW S 6", "Bank will Konzept" oder "Schutzschirm" schreibt, starte so:

1. **Eilt es insolvenzrechtlich?** Liegt Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit oder Überschuldung im Raum?
2. **Wer braucht das Konzept?** Geschäftsleitung, Bank, Warenkreditversicherer, Gläubigerausschuss, Investor, Gericht, Restrukturierungsbeauftragter?
3. **Welche Route?** außergerichtlich, StaRUG, Eigenverwaltung, Schutzschirm, Insolvenzplan, Distressed M&A?
4. **Welche Zahlen liegen vor?** Liquiditätsplan, BWA, SuSa, Jahresabschlüsse, OPOS, Bankauszüge, Auftragsbestand, Planrechnung?
5. **Welche Maßnahmen sind schon verbindlich?** Stundung, Verzicht, Rangrücktritt, Patronat, Kapitalzufuhr, Kreditlinie, M&A, Personal, Standort, Preise?
6. **Welcher Output?** Kurzvermerk, Mandantenmemo, Bankunterlage, Datenanforderung, Red-Team-Prüfung, Planbaustein.

Wenn akute Insolvenzreife möglich ist, zuerst `fachanwalt-insolvenz-sanierungsrecht-orientierung` oder den passenden Antragspflicht-/Liquiditätsskill vorschlagen.

## Prüflogik

### 1. Insolvenzrechtliche Mindestprüfung

Vor jeder Sanierungserzählung:

- Zahlungsunfähigkeit nach § 17 InsO stichtagsbezogen prüfen.
- Drohende Zahlungsunfähigkeit nach § 18 InsO für StaRUG und Frühwarnung prüfen.
- Überschuldung nach § 19 InsO mit Fortbestehensprognose prüfen.
- Antragspflichten, Zahlungsverbote und Haftungsrisiken dokumentieren.

Eine Sanierungsidee heilt keine bereits eingetretene Insolvenzreife. Maßnahmen dürfen erst in die Prognose, wenn sie rechtzeitig, konkret und hinreichend verbindlich sind.

### 2. Fortbestehensprognose

Prüfe, ob die Zahlungsfähigkeit über den Prognosezeitraum mit überwiegender Wahrscheinlichkeit gesichert ist. Dafür muss der Liquiditätsplan mit Fälligkeiten, verfügbaren Mitteln, verbindlichen Finanzierungsquellen und Sensitivitäten arbeiten. Reine Hoffnung, "Pipeline", weiche Patronage oder unverhandelte Stundung trägt die Prognose nicht.

### 3. Nachhaltige Sanierungsfähigkeit

Prüfe anschließend, ob das Unternehmen nach Umsetzung der Maßnahmen wieder dauerhaft im Markt bestehen kann. Dazu gehören:

- tragfähiges Geschäftsmodell,
- positive oder klar erreichbare Ertragskraft,
- realistische Finanzierung,
- beherrschbare Abhängigkeiten,
- Management- und Umsetzungsfähigkeit,
- beseitigte oder kontrollierte Krisenursachen.

## Kernbestandteile

Erstelle oder prüfe das Konzept entlang dieser Struktur:

1. Auftrag, Adressat, Stichtag, Verwendungsgrenzen.
2. Rechtliche, wirtschaftliche und steuerliche Ausgangslage des Unternehmens.
3. Vermögens-, Finanz- und Ertragslage mit belegter Datenbasis.
4. Krisenstadium und Krisenursachenanalyse.
5. Leitbild des sanierten Unternehmens.
6. Maßnahmenpakete mit Verantwortlichen, Timing, Kosten, Effekt und Abhängigkeiten.
7. Integrierte Planung aus GuV, Bilanz und Liquidität.
8. Szenarien und Sensitivitäten.
9. Ergebnis zur Fortbestehensprognose und Sanierungsfähigkeit.
10. Dokumentation, Annahmenregister, Belegliste und offene Punkte.

## Leitbild des sanierten Unternehmens

Das Leitbild muss konkret genug sein, damit man Maßnahmen und Planung dagegen testen kann. Formuliere deshalb immer:

- Was verkauft das Unternehmen künftig an wen und warum profitabel?
- Welche Standorte, Produkte, Kunden und Lieferanten bleiben tragend?
- Welche Fixkostenbasis ist nach Umsetzung realistisch?
- Welche Finanzierung und Kapitalstruktur trägt das Zielbild?
- Welche Governance, IT, Cyber-, ESG- oder Compliance-Risiken müssen beherrscht werden?
- Welche Personen oder Gremien müssen die Umsetzung führen?

## Maßnahmenmatrix

Nutze diese Tabelle:

| Maßnahme | Krise/Ursache | Effekt GuV | Effekt Liquidität | Effekt Bilanz | Kosten | Frist | Verantwortlich | Nachweis | Abhängigkeit |
|---|---|---:|---:|---:|---:|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] |

Wichtig: Keine Maßnahme ohne Belegstatus. Kennzeichne `verbindlich`, `verhandelt`, `plausibel`, `ungeklärt` oder `nicht tragfähig`.

## Integrierte Planung

Ein Sanierungskonzept braucht mehr als eine Liquiditätsvorschau. Verlange die Verzahnung von:

- **GuV:** Umsatz, Rohertrag, Personal, sonstige Kosten, Zinsen, Steuern, Ergebnis.
- **Bilanz:** Working Capital, Anlagevermögen, Rückstellungen, Verbindlichkeiten, Eigenkapital, Finanzschulden.
- **Liquidität:** Anfangsbestand, Einzahlungen, Auszahlungen, Linien, Tilgung, Mindestliquidität.

Prüfe rechnerische Brücken:

- Jahresergebnis verändert Eigenkapital.
- Working-Capital-Veränderungen erklären Cashflow-Abweichungen zur GuV.
- Endbestand Liquidität stimmt mit Planbilanz überein.
- Finanzierungsmaßnahmen wirken gleichzeitig auf Cash, Schulden, Zins und Covenants.

## Kleinere Unternehmen

Bei kleineren Unternehmen gilt Proportionalität. Das Konzept darf kürzer sein, aber nicht lückenhaft. Mindestniveau:

- klare Krisenursache,
- nachvollziehbares Geschäftsmodell,
- echte Maßnahmen mit Umsetzungsverantwortung,
- integrierte Planung in angemessener Detailtiefe,
- dokumentierte Annahmen und Belege,
- transparente Aussage zur Sanierungsfähigkeit.

## Output-Module

### Mandantenmemo

- Ergebnis in fünf Sätzen.
- Insolvenzrechtliche Sofortrisiken.
- Tragende Sanierungsannahmen.
- Fehlende Unterlagen.
- Entscheidungsvorschlag: Go, Conditional Go, No-go.

### Bank-/Gläubigerunterlage

- Ausgangslage ohne Schönfärbung.
- Maßnahmenpaket mit Beiträgen aller relevanten Stakeholder.
- Planungslogik und Liquiditätsreichweite.
- Monitoring-Kennzahlen und Reporting-Takt.
- Offene Punkte mit Terminplan.

### Red-Team-Liste

Formuliere die stärksten Gegenargumente:

- "Die Krise ist nur verschoben."
- "Die Planannahmen sind nicht belegt."
- "Das Leitbild passt nicht zur Marktposition."
- "Der Gesellschafterbeitrag ist nicht sicher."
- "Die Liquidität kippt bei kleinen Abweichungen."
- "Steuern, Sozialversicherung oder Zinsen fehlen."
- "Management kann die Maßnahmen nicht umsetzen."

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Typische Fehler

- Sanierungskonzept wird mit Fortbestehensprognose verwechselt.
- Liquiditätsplan wird ohne Planbilanz vorgelegt.
- Krisenursachen werden beschrieben, aber nicht durch Maßnahmen beseitigt.
- Maßnahmen stehen im Text, aber nicht in der Planung.
- Einmalige Finanzspritze wird als Geschäftsmodellreparatur behandelt.
- Kleine Unternehmen werden methodisch unterprüft statt proportional geprüft.
- Datenstand, Annahmen und Versionen bleiben unklar.

## Anschluss-Skills

- `fachanwalt-insolvenz-sanierung-starug-plan` bei StaRUG-Route.
- `fachanwalt-insolvenz-sanierungsrecht-schutzschirmverfahren` bei Schutzschirm/Eigenverwaltung.
- `fachanwalt-insolvenz-glaeubigerverhandlung-sanierung` für Banken- und Gläubigerverhandlungen.
- `fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan` für Planarchitektur.

## Quellenregel

Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben. Berufsständische Standards methodisch verwenden, aber nicht als Ersatz für Gesetz, Rechtsprechung und Subsumtion.
