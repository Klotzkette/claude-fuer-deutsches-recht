---
name: ki-training-mit-datenbankbestand
description: "Rechtliche Analyse des KI-Trainings mit Datenbankbeständen: §§ 44b und 60d UrhG (Text- und Data-Mining-Schranken), Verhältnis zu §§ 87a-87e UrhG, Opt-out-Pflichten nach § 44b Abs. 3 UrhG und DSM-RL Art. 4. Bewertet kommerzielle vs. wissenschaftliche TDM-Nutzung und erstellt Compliance-Plan für KI-Unternehmen und Datenbankbetreiber im Datenbankrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# KI-Training mit Datenbankbeständen — Datenbankrecht und TDM-Schranken

## Arbeitsbereich

Rechtliche Analyse des KI-Trainings mit Datenbankbeständen: §§ 44b und 60d UrhG (Text- und Data-Mining-Schranken), Verhältnis zu §§ 87a-87e UrhG, Opt-out-Pflichten nach § 44b Abs. 3 UrhG und DSM-RL Art. 4. Bewertet kommerzielle vs. wissenschaftliche TDM-Nutzung und erstellt Compliance-Plan für KI-Unternehmen und Datenbankbetreiber. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- KI-Startup möchte eine kommerzielle Sprachmodell-Trainingsdatenbank aus lizenzierten und öffentlichen Quellen zusammenstellen und benötigt Rechtssicherheit zur TDM-Schranke.
- Datenbankbetreiber fragt, wie er sein Opt-out gegen KI-Training technisch und rechtlich wirksam dokumentieren kann.
- Forschungsinstitut will eine Datenbanksammlung für nicht-kommerzielle Textanalyse nutzen und prüft, ob § 60d UrhG die Nutzung erlaubt.

## Erste Schritte

1. Nutzungsart bestimmen: Kommerzielles KI-Training (§ 44b UrhG) oder wissenschaftliche Forschung (§ 60d UrhG)?
2. Datenbankschutz der Quelle prüfen: Greift §§ 87a ff. UrhG für die Quelldatenbank? Ist eine Lizenz oder Schranke erforderlich?
3. Opt-out der Rechteinhaber prüfen: Hat der Datenbankbetreiber einen maschinenlesbaren Opt-out erklärt (§ 44b Abs. 3 UrhG)?
4. Vertragslage analysieren: Lizenzbedingungen der Quelldatenbank, AGB, API-Nutzungsbedingungen — erlauben sie Training?
5. Technische Umsetzung des Opt-outs dokumentieren: robots.txt-Einträge, HTTP-Header, Metadaten — reichen diese als maschinenlesbarer Vorbehalt?
6. DSGVO-Schnittmenge prüfen: Enthält die Trainingsdatenbank personenbezogene Daten (§ 12 DSGVO, Art. 6 Abs. 1 DSGVO)?

## Rechtsrahmen

- § 44b UrhG: TDM-Schranke für kommerzielle Zwecke — erlaubt Vervielfältigung für TDM, es sei denn, Rechteinhaber hat Opt-out erklärt.
- § 60d UrhG: TDM-Schranke für wissenschaftliche Forschung — weitgehend zwingend, kaum Opt-out möglich.
- § 87b UrhG: Datenbankherstellerrecht — TDM-Schranken gelten auch gegenüber dem sui-generis-Recht (§ 87c Abs. 1 Nr. 4 UrhG).
- DSM-RL Art. 3-4 (RL 2019/790): Europäische Grundlage der TDM-Schranken; Art. 4 für kommerzielle TDM mit Opt-out.
- § 87c UrhG: Erlaubte Handlungen — Verweis auf § 44b und § 60d als Schranken.
- Art. 6 Abs. 1 DSGVO: Rechtsgrundlage für Verarbeitung personenbezogener Trainingsdaten.

## Prüfraster

- Dient das KI-Training einem kommerziellen oder wissenschaftlichen Zweck?
- Wurde ein wirksamer maschinenlesbarer Opt-out durch den Datenbankbetreiber erklärt?
- Enthält die Datenbank urheberrechtlich oder durch Herstellerrecht geschützte Inhalte?
- Erlauben vorhandene Lizenzverträge die Nutzung für KI-Training explizit oder schließen sie diese aus?
- Werden personenbezogene Daten für das Training verwendet — welche DSGVO-Rechtsgrundlage gilt?
- Sind die erzeugten KI-Modelle selbst als abgeleitete Datenbankwerke einzuordnen?
- Welche Dokumentationspflichten gelten für den Trainingsdatensatz (Transparenz, DSM-RL Erwägungsgrund 18)?

## Typische Fallstricke

- Opt-out nach § 44b Abs. 3 UrhG muss maschinenlesbar sein — ein allgemeines AGB-Verbot reicht nicht aus.
- Kommerzielle TDM-Schranke schützt nicht, wenn der Opt-out vor dem Abruf wirksam erklärt wurde.
- Auch öffentlich zugängliche Datenbanken können durch Herstellerrecht geschützt sein — öffentlich ≠ frei nutzbar.
- § 60d UrhG gilt nur für originär wissenschaftliche Forschung, nicht für Forschungs-Spin-offs mit kommerziellem Fokus.
- Das erzeugte KI-Modell kann Datenbankschutz der Quelldatenbank weitertragen, wenn Trainingsdaten direkt abrufbar sind.

## Output

- TDM-Compliance-Prüfbericht (kommerziell/wissenschaftlich, Opt-out-Status)
- Opt-out-Implementierungsguide für Datenbankbetreiber (robots.txt, HTTP-Header)
- Lizenz-Checkliste für Trainingsdaten-Beschaffung
- Datenschutz-Kurzprüfung (DSGVO-Rechtsgrundlage für personenbezogene Trainingsdaten)
- Vertragsmuster für KI-Trainingsdaten-Lizenz

## Quellen

- [§ 44b UrhG TDM-Schranke — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [§ 60d UrhG wissenschaftliches TDM — dejure.org](https://dejure.org/gesetze/UrhG/60d.html)
- [§ 87c UrhG erlaubte Handlungen — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [DSM-Richtlinie 2019/790 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [Art. 6 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
