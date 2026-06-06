---
name: ki-archivierung
description: "Prueft Insiderrecht-Risiken beim Einsatz von KI-Prognosemodellen: Informationsasymmetrie, Modell-Output als Insiderinformation und Compliance-Anforderungen im Insiderrecht Compliance: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# KI-Prognosemodelle und Insiderrecht

## Arbeitsbereich

Prueft Insiderrecht-Risiken beim Einsatz von KI-Prognosemodellen: Informationsasymmetrie, Modell-Output als Insiderinformation und Compliance-Anforderungen. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG §§ 13, 14, 15-15b (i.d.F. MAR), Marktmissbrauchs-VO (MAR) 596/2014, KWG, EU-VO 600/2014 (MiFIR), BörsG; WpHG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Der Einsatz von KI-Modellen (maschinelles Lernen, LLMs, Forecasting-Modelle) zur Prognose
von Unternehmensergebnissen, Marktentwicklungen oder zur Entdeckung von Insiderinformationen
ist insiderrechtlich nicht explizit geregelt. MAR Art. 7 gilt unabhängig davon, wie die
Information gewonnen wurde. Wenn ein KI-Modell auf Basis nicht-öffentlicher Eingangsdaten
eine kursrelevante Prognose generiert, kann der Modell-Output eine Insiderinformation sein.

Rechtsgrundlagen:
- Art. 7 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-628/13 (Lafonta): https://curia.europa.eu/juris/document/document.jsf?docid=162388
- KI-Verordnung (EU) 2024/1689 (AI Act): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill klärt, unter welchen Umständen KI-generierte Prognosen oder Analysen
Insiderinformationen darstellen und wie der Zugang zu solchen Modellen kontrolliert werden muss.

## Arbeitsprogramm

### Schritt 1 – KI-Modell-Input-Analyse

- Welche Daten werden in das Modell eingespeist?
 - Ausschließlich öffentliche Daten: Kein Insiderrecht-Problem beim Output
 - Nicht-öffentliche Unternehmensdaten (interne Finanzdaten, Vertriebsdaten, Produktionsdaten):
 Modell-Output kann Insiderinformation sein

### Schritt 2 – Modell-Output als Insiderinformation

- Generiert das Modell eine Prognose, die erheblich von der veröffentlichten Guidance oder
 dem Analystenkonsensus abweicht?
- Ist der Modell-Output hinreichend präzise? (nicht nur Wahrscheinlichkeiten, sondern
 konkrete Zahlenwerte)
- Würde ein verständiger Anleger diesen Output bei seiner Investitionsentscheidung nutzen?
 Wenn ja → Modell-Output ist Insiderinformation

### Schritt 3 – Zugangskontrollen

- Wer hat Zugang zu dem KI-Modell und seinen Outputs?
- Alle Zugangspersonen sind potenzielle Insider → Insiderliste, Handelsverbot
- Chinese Walls: Handelsabteilung darf keinen Zugang zu internen Forecasting-Modellen haben

### Schritt 4 – Modell-Governance und Dokumentation

- AI-Act-Anforderungen für Hochrisiko-KI: Falls das Modell für Investitions- oder
 Finanzentscheidungen eingesetzt wird, können AI Act Art. 9 ff. gelten
- Modell-Dokumentation: Input-Daten, Algorithmus-Beschreibung, Output-Interpretation
- Audit-Trail: Wer hat wann welche Prognosen aus dem Modell abgerufen?

### Schritt 5 – Compliance-Empfehlungen

- Trennung: Internes Forecasting-System (Insiderinformation) vs. extern veröffentlichte Prognose
- Ad-hoc-Pflicht: Wenn Modell-Output wesentliche Abweichung von Guidance signalisiert →
 Prüfung ob Profit-Warning-Ad-hoc erforderlich
- Schulung der Modell-Nutzer auf Insiderrecht

## Red-Team-Fragen

- Verarbeitet das Modell nicht-öffentliche Daten, die zu einer Insiderinformation führen?
- Haben alle Modell-Nutzer eine Insiderrecht-Schulung erhalten?
- Gibt es Chinese Walls zwischen Modell-Zugang und Handelsabteilung?
- Wird der Modell-Output auf Ad-hoc-Relevanz geprüft?
- Sind AI-Act-Anforderungen bekannt und berücksichtigt?

## Ausgabeformat

Erzeuge:
1. KI-Modell-Risikobewertung (Input × Output × Insiderinformationsrisiko)
2. Zugangskontrollen-Matrix (Nutzergruppe × Zugangsberechtigung × Insiderstatus)
3. Modell-Governance-Dokumentationsvorlage
4. Schulungsmodul: „KI-Prognosen und Insiderrecht"

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, dejure.org.
