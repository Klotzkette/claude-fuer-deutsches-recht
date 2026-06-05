---
name: dora-ict-einlagensicherung-kundenhinweise
description: "Dora ICT Einlagensicherung Kundenhinweise: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dora ICT Einlagensicherung Kundenhinweise

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Dora ICT Einlagensicherung Kundenhinweise** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dora-ict-vertraege-vorfall` | DORA-IKT-Verträge und IKT-Vorfälle: Pflichtklauseln, Register, Exit, Überwachungsrechte, Suboutsourcing, Incident-Klassifizierung, Meldewege und Managementbericht prüfen. |
| `einlagensicherung-kundenhinweise` | Einlagensicherung und Kundenhinweise: gesetzliche und institutsspezifische Sicherung, Informationsbogen, Produktabgrenzung, Markenauftritt, Filialhinweise und Beschwerdekommunikation prüfen. |
| `embedded-finance-kooperation` | Embedded-Finance-Kooperationen prüfen: Händler, Plattform, Bank, Zahlungsdienstleister, Kreditangebot, Vermittlung, Scoring, Datenschutz, Provision und Erlaubnisrisiken. |
| `esg-sustainable-finance` | ESG und Sustainable Finance in der Bank: Offenlegung, Taxonomie, Green Claims, Kreditpolitik, Anlageprodukte, Reputationsrisiko und Vorstandskommunikation prüfen. |
| `ewpg-emission-elektronische-wertpapiere` | Emission elektronischer Wertpapiere nach eWpG prüfen: Zentralregister, Kryptowertpapierregister, Emissionsbedingungen, Registerangaben, Prospekt, Depot, Vertrieb und Anlegerkommunikation. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **Dora ICT Einlagensicherung Kundenhinweise**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dora-ict-vertraege-vorfall`

**Fokus:** DORA-IKT-Verträge und IKT-Vorfälle: Pflichtklauseln, Register, Exit, Überwachungsrechte, Suboutsourcing, Incident-Klassifizierung, Meldewege und Managementbericht prüfen.

# DORA IKT-Verträge und Vorfälle

## Fachkern: DORA IKT-Verträge und Vorfälle
- **Spezialgegenstand:** DORA IKT-Verträge und Vorfälle. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Die Bank beschafft Cloud, Core Banking, Zahlungsverkehr, Cybersecurity oder andere IKT-Dienste oder ein IKT-Vorfall liegt vor.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Vertrag, SLA, Incident-Report, Kritikalität, betroffene Services, Daten, Wiederanlaufzeit, Anbieterkommunikation.
- **Institut:** Rechtsform, Erlaubnisstatus, SSM-/LSI-Status, Geschäftsmodell, Konzernbezug, relevante Tochter oder Zweigniederlassung.
- **Dokumente:** Vertrag, Aufsichtsschreiben, Kreditakte, Sanierungsgutachten, Richtlinie, Vorstandsvorlage, Rechnung, Beschwerde, Registerauszug, Datenraum oder Screenshot.
- **Frist und Forum:** BaFin, Bundesbank, EZB/SSM, FIU, Gericht, Ombudsstelle, Vorstand, Aufsichtsrat, HV, Prüfung, Closing oder interne Deadline.
- **Risikodimension:** Aufsicht, Zivilrecht, Straf-/OWi-Risiko, Organhaftung, Datenschutz, Bankgeheimnis, Reputation, Kosten, Operational Risk.

## Prüfworkflow

### 1. Kurzbild

Fasse in fünf bis acht Zeilen zusammen:

| Punkt | Inhalt |
| --- | --- |
| Vorgang | Was liegt auf dem Tisch? |
| Entscheider | Wer muss freigeben oder informiert werden? |
| Frist | Was läuft wann ab? |
| Primärrecht | Welche Normen oder Behördenstandards tragen die Prüfung? |
| Risiko | Rot, Gelb oder Grün mit einem Satz Begründung. |
| Nächster Schritt | Was sollte die Bank jetzt konkret tun? |

### 2. Rechts- und Governance-Karte

Prüfe je nach Fall insbesondere:

- **Bankaufsicht:** KWG, MaRisk, DORA, CRR/CRD, WpHG, WpIG, ZAG, GwG, BaFin-/Bundesbank-/EBA-/EZB-Vorgaben.
- **Zivilrecht:** BGB-Vertrag, AGB-Kontrolle, Darlehen, Kündigung, Sicherheiten, Haftung, Datenschutz, Geschäftsgeheimnis und Bankgeheimnis.
- **Gesellschaftsrecht:** AktG, GmbHG, Satzung, Geschäftsordnung, Vorstand, Aufsichtsrat, Ausschüsse, HV, Interessenkonflikte und Business Judgment Rule.
- **Kredit und Krise:** Sanierungsgutachten, Fortbestehensprognose, Liquiditätsplanung, Forbearance, Sicherheiten, Insolvenzanfechtung, StaRUG-/InsO-Schnittstelle.
- **Vertrieb:** Handelsvertreterrecht, Vermittler, Provision, WpHG-Vertriebspflichten, Beschwerden, Ombudsmann, Produktfreigabe.
- **Operations:** Auslagerung, IT, Cloud, DORA, Dienstleistersteuerung, interne Richtlinien, Datenraum, Rechnungsreview, Litigation.

### 3. Beleg- und Lückenmatrix

Erstelle eine Tabelle:

| Behauptung oder Risiko | Beleg vorhanden? | Fehlender Beleg | Warum wichtig? | Owner |
| --- | --- | --- | --- | --- |
| ... | ja/nein | ... | ... | ... |

### 4. Entscheidungsvorbereitung

Erzeuge DORA-Klauselcheck, Incident-Triage, Meldefahrplan und Management Summary.

Baue das Ergebnis so, dass ein Syndikus es intern weitergeben kann:

- **Für Vorstand:** stark verdichtete Entscheidung, Optionen, Risiko, Empfehlung, Kosten und Zeitplan.
- **Für Fachbereich:** klare To-dos, keine juristische Überwältigung, aber präzise rote Linien.
- **Für Aufsicht:** faktenstark, vollständig, konsistent, ohne unnötige Selbstbezichtigung oder Spekulation.
- **Für externe Kanzlei:** enger Scope, konkrete Fragen, Budget, Deadline und erwartetes Arbeitsergebnis.

## Stilregeln

- Kurz starten, dann sauber vertiefen.
- Keine Textwüste: Tabellen, Ampeln, Checklisten und Entscheidungssätze nutzen.
- Bei hoher Unsicherheit die Unsicherheit verwertbar machen: welche Tatsache fehlt, wer kann sie liefern, bis wann.
- Keine pauschalen Haftungsausschlüsse in jedem Absatz. Einmal sauber markieren, dann arbeiten.
- Rechtsprechung nur verwenden, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und freie oder amtliche Quelle geprüft sind.

## Ausgabeformate

Wähle passend oder biete maximal drei Optionen an:

1. **Legal Note** mit Kurzbild, Prüfung, Risikoampel, Empfehlung.
2. **Vorstandsvorlage** mit Beschlussvorschlag und Alternativen.
3. **BaFin-/Bundesbank-Antwortentwurf** mit Tatsachenmatrix.
4. **Vertrags- oder Klauselcheck** mit Änderungsvorschlägen.
5. **Unterlagenliste** für Fachbereich, Kanzlei, Prüfer oder Datenraum.
6. **Red-Team-Check** gegen Aufsicht, Prozessgegner, Verwalter oder interne Revision.


### Anschluss-Skills

- Bei ungeklärter Ausgangslage: `bankrechtsabteilung-kaltstart-routing`.
- Bei Aufsichtsbezug: `bankaufsichtsrecht-kwg-marisk-triage`, `bafin-kommunikation-und-anhoerung` oder `ssm-bundesbank-aufsichtsbrief`.
- Bei kleinen oder spezialisierten Finanzunternehmen zuerst `dora-art16-vereinfachter-ikt-rahmen` prüfen; bei allgemeiner Cyber-Abgrenzung `nis2-cybersecurity-compliance:dora-art16-finanzunternehmen-simplified-framework`.
- Bei Kredit- und Krisenbezug: `kreditentscheidung-weiterfinanzierung`, `stundung-standstill-waiver`, `sanierungsgutachten-idw-s6-bewertung` oder `restrukturierung-kreditengagement`.
- Bei Gremienbezug: `vorstandsvorlage-gutachten`, `aufsichtsrat-vorlage-bank` oder `organhaftung-business-judgment`.
- Bei Dienstleistern und Kanzleien: `outsourcing-externe-dienstleister`, `externe-anwaelte-steuerung` oder `anwaltliche-rechnungen-review`.


## Quellenanker

Nutze vor tragenden Aussagen bevorzugt amtliche oder frei zugängliche Quellen: Gesetze im Internet für KWG, ZAG, WpHG, GwG, HGB, BGB und AktG; BaFin für MaRisk, Merkblätter und Aufsichtsinformationen; EUR-Lex für DORA, CRR/CRD und MiFID; EBA/EZB/Bundesbank für Leitlinien und Aufsichtspraxis. Das Quellenverzeichnis des Plugins liegt in `references/QUELLEN.md`.

## DORA-Art.-16-Spezialkern

Wenn Artikel 16 DORA im Raum steht, nicht den vollen Standard mechanisch übertragen und nicht zu wenig verlangen. Erzeuge eine Scope-Entscheidung und prüfe: Leitungsorgan, IKT-Risikorahmen, Asset-Inventar, Need-to-use/IAM, Schwachstellen, Change, Backup, BCP, Incident, Drittparteien, Subdienstleister, Exit und Nachweisordner. Die BaFin-Hinweise vom 21.08.2025 sind als Verwaltungspraxis live zu prüfen.

## 2. `einlagensicherung-kundenhinweise`

**Fokus:** Einlagensicherung und Kundenhinweise: gesetzliche und institutsspezifische Sicherung, Informationsbogen, Produktabgrenzung, Markenauftritt, Filialhinweise und Beschwerdekommunikation prüfen.

# Einlagensicherung

## Fachkern: Einlagensicherung
- **Spezialgegenstand:** Einlagensicherung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Neue Kontoprodukte, Fusion, Markenwechsel, Kundenbrief oder Beschwerde berührt Einlagensicherung oder Anlegerentschädigung.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Produkt, Kundengruppe, Sicherungssystem, Vertragsunterlagen, Website, Kundenkommunikation.
- **Institut:** Rechtsform, Erlaubnisstatus, SSM-/LSI-Status, Geschäftsmodell, Konzernbezug, relevante Tochter oder Zweigniederlassung.
- **Dokumente:** Vertrag, Aufsichtsschreiben, Kreditakte, Sanierungsgutachten, Richtlinie, Vorstandsvorlage, Rechnung, Beschwerde, Registerauszug, Datenraum oder Screenshot.
- **Frist und Forum:** BaFin, Bundesbank, EZB/SSM, FIU, Gericht, Ombudsstelle, Vorstand, Aufsichtsrat, HV, Prüfung, Closing oder interne Deadline.
- **Risikodimension:** Aufsicht, Zivilrecht, Straf-/OWi-Risiko, Organhaftung, Datenschutz, Bankgeheimnis, Reputation, Kosten, Operational Risk.

## Prüfworkflow

### 1. Kurzbild

Fasse in fünf bis acht Zeilen zusammen:

| Punkt | Inhalt |
| --- | --- |
| Vorgang | Was liegt auf dem Tisch? |
| Entscheider | Wer muss freigeben oder informiert werden? |
| Frist | Was läuft wann ab? |
| Primärrecht | Welche Normen oder Behördenstandards tragen die Prüfung? |
| Risiko | Rot, Gelb oder Grün mit einem Satz Begründung. |
| Nächster Schritt | Was sollte die Bank jetzt konkret tun? |

### 2. Rechts- und Governance-Karte

Prüfe je nach Fall insbesondere:

- **Bankaufsicht:** KWG, MaRisk, DORA, CRR/CRD, WpHG, WpIG, ZAG, GwG, BaFin-/Bundesbank-/EBA-/EZB-Vorgaben.
- **Zivilrecht:** BGB-Vertrag, AGB-Kontrolle, Darlehen, Kündigung, Sicherheiten, Haftung, Datenschutz, Geschäftsgeheimnis und Bankgeheimnis.
- **Gesellschaftsrecht:** AktG, GmbHG, Satzung, Geschäftsordnung, Vorstand, Aufsichtsrat, Ausschüsse, HV, Interessenkonflikte und Business Judgment Rule.
- **Kredit und Krise:** Sanierungsgutachten, Fortbestehensprognose, Liquiditätsplanung, Forbearance, Sicherheiten, Insolvenzanfechtung, StaRUG-/InsO-Schnittstelle.
- **Vertrieb:** Handelsvertreterrecht, Vermittler, Provision, WpHG-Vertriebspflichten, Beschwerden, Ombudsmann, Produktfreigabe.
- **Operations:** Auslagerung, IT, Cloud, DORA, Dienstleistersteuerung, interne Richtlinien, Datenraum, Rechnungsreview, Litigation.

### 3. Beleg- und Lückenmatrix

Erstelle eine Tabelle:

| Behauptung oder Risiko | Beleg vorhanden? | Fehlender Beleg | Warum wichtig? | Owner |
| --- | --- | --- | --- | --- |
| ... | ja/nein | ... | ... | ... |

### 4. Entscheidungsvorbereitung

Erzeuge Hinweis-Check, Risikostellen, Kundenfassung und interne Freigabeliste.

Baue das Ergebnis so, dass ein Syndikus es intern weitergeben kann:

- **Für Vorstand:** stark verdichtete Entscheidung, Optionen, Risiko, Empfehlung, Kosten und Zeitplan.
- **Für Fachbereich:** klare To-dos, keine juristische Überwältigung, aber präzise rote Linien.
- **Für Aufsicht:** faktenstark, vollständig, konsistent, ohne unnötige Selbstbezichtigung oder Spekulation.
- **Für externe Kanzlei:** enger Scope, konkrete Fragen, Budget, Deadline und erwartetes Arbeitsergebnis.

## Stilregeln

- Kurz starten, dann sauber vertiefen.
- Keine Textwüste: Tabellen, Ampeln, Checklisten und Entscheidungssätze nutzen.
- Bei hoher Unsicherheit die Unsicherheit verwertbar machen: welche Tatsache fehlt, wer kann sie liefern, bis wann.
- Keine pauschalen Haftungsausschlüsse in jedem Absatz. Einmal sauber markieren, dann arbeiten.
- Rechtsprechung nur verwenden, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und freie oder amtliche Quelle geprüft sind.

## Ausgabeformate

Wähle passend oder biete maximal drei Optionen an:

1. **Legal Note** mit Kurzbild, Prüfung, Risikoampel, Empfehlung.
2. **Vorstandsvorlage** mit Beschlussvorschlag und Alternativen.
3. **BaFin-/Bundesbank-Antwortentwurf** mit Tatsachenmatrix.
4. **Vertrags- oder Klauselcheck** mit Änderungsvorschlägen.
5. **Unterlagenliste** für Fachbereich, Kanzlei, Prüfer oder Datenraum.
6. **Red-Team-Check** gegen Aufsicht, Prozessgegner, Verwalter oder interne Revision.


### Anschluss-Skills

- Bei ungeklärter Ausgangslage: `bankrechtsabteilung-kaltstart-routing`.
- Bei Aufsichtsbezug: `bankaufsichtsrecht-kwg-marisk-triage`, `bafin-kommunikation-und-anhoerung` oder `ssm-bundesbank-aufsichtsbrief`.
- Bei Kredit- und Krisenbezug: `kreditentscheidung-weiterfinanzierung`, `stundung-standstill-waiver`, `sanierungsgutachten-idw-s6-bewertung` oder `restrukturierung-kreditengagement`.
- Bei Gremienbezug: `vorstandsvorlage-gutachten`, `aufsichtsrat-vorlage-bank` oder `organhaftung-business-judgment`.
- Bei Dienstleistern und Kanzleien: `outsourcing-externe-dienstleister`, `externe-anwaelte-steuerung` oder `anwaltliche-rechnungen-review`.


## Quellenanker

Nutze vor tragenden Aussagen bevorzugt amtliche oder frei zugängliche Quellen: Gesetze im Internet für KWG, ZAG, WpHG, GwG, HGB, BGB und AktG; BaFin für MaRisk, Merkblätter und Aufsichtsinformationen; EUR-Lex für DORA, CRR/CRD und MiFID; EBA/EZB/Bundesbank für Leitlinien und Aufsichtspraxis. Das Quellenverzeichnis des Plugins liegt in `references/QUELLEN.md`.

## 3. `embedded-finance-kooperation`

**Fokus:** Embedded-Finance-Kooperationen prüfen: Händler, Plattform, Bank, Zahlungsdienstleister, Kreditangebot, Vermittlung, Scoring, Datenschutz, Provision und Erlaubnisrisiken.

# Embedded Finance

## Fachkern: Embedded Finance
- **Spezialgegenstand:** Embedded Finance. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank integriert Finanzprodukte in fremde Plattformen, Shops, Apps oder B2B-Workflows.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Produkt, Plattform, Kundenreise, Vermittlerrolle, Daten, Vergütung, Kreditentscheidung, Zahlungsfluss.
- **Institut und Rolle:** Bank, Zahlungsinstitut, E-Geld-Institut, Wertpapierinstitut, CRR-Kreditinstitut, FinTech-Tochter, Vermittler, Agent, Registerführer, CASP, Emittent oder Dienstleister.
- **Produkt oder Vorgang:** Zahlungsdienst, E-Geld, Kredit, Wertpapier, Token, Register, Organwechsel, Auslagerung, Betrugsfall, Trade Finance oder Kooperation.
- **Aufsicht und Einreichweg:** BaFin, Bundesbank, EZB/SSM, EBA, FIU, Register, MVP, IMAS, Bundesanzeiger, Handelsregister oder interner Ausschuss.
- **Dokumente:** Produktbeschreibung, Flow-of-Funds, Vertragsentwurf, API-Doku, Token Terms, Organ-CV, Eignungsmatrix, Registerauszug, Kundenkommunikation, Logs oder Vorstandsvorlage.

## Prüfaufbau

### 1. Kurzbild

| Punkt | Klärung |
| --- | --- |
| Ergebnisbedarf | Vermerk, Freigabe, BaFin-Anfrage, Vertrag, Vorstandsvorlage oder Prozessstrategie |
| Rechtsregime | KWG, ZAG, WpHG, WpIG, eWpG, MiCAR, DORA, GwG, BGB, HGB, AktG, SEPA-/EU-Regime oder Entwurf |
| Risiko | Aufsicht, Bußgeld, Zivilhaftung, Organhaftung, Kundenstreit, AML, Datenschutz, IT oder Reputation |
| Frist | Anzeige, Launch, Antwort, Rückgabe, Register, Gremium oder Verjährung |
| Entscheidung | Go, Go mit Auflagen, Stop, BaFin-Vorabklärung oder externe Spezialprüfung |

### 2. Subsumtion und Geschäftsmodell

Arbeite in dieser Reihenfolge:

1. Lebenssachverhalt und Rollen in einfachen Sätzen festhalten.
2. Geld-, Daten-, Wertpapier- oder Tokenfluss als Tabelle beschreiben.
3. Tatbestandsmerkmale einzeln prüfen.
4. Ausnahmen, Privilegierungen, Bestandsschutz, Übergangsregeln oder Entwurfsstand gesondert behandeln.
5. Gegenargumente und Red-Team-Sicht der Aufsicht formulieren.
6. Praktische Auflagen für Launch, Fortführung, Korrektur oder Ablehnung schreiben.

### 3. Beleg- und Unterlagenliste

| Frage | Beleg | Fehlt | Owner | Wirkung |
| --- | --- | --- | --- | --- |
| Wer erbringt welche Leistung? | Vertrag, Produktbild, Prozess | ... | Legal/Produkt | Regimewahl |
| Fließen Kundengelder oder Kryptowerte? | Flow-of-Funds, Wallet-/Kontoauszug | ... | Operations/Risk | Erlaubnis/Haftung |
| Gibt es Aufsichtskontakt? | Schreiben, Ticket, Portalnachweis | ... | Legal/Compliance | Frist/Strategie |
| Sind Kunden betroffen? | AGB, FAQ, Beschwerde, Marketing | ... | Vertrieb/Legal | Transparenz/Haftung |

### 4. Ergebnis

Erzeuge Kooperationsmatrix, Erlaubnischeck, Vertragslücken, Datenschutzfragen und Launch-Auflagen.

Baue das Ergebnis mit diesen Elementen:

- **Entscheidungssatz:** Ein Satz, der intern zitiert werden kann.
- **Risikoampel:** Rot/Gelb/Grün mit kurzer Begründung.
- **Auflagen:** Welche Bedingungen müssen vor Go-Live oder vor Antwort erfüllt sein?
- **Offene Punkte:** konkrete Rückfragen statt allgemeiner Rechercheaufträge.
- **Anschluss-Skills:** passende Skills aus `bank-rechtsabteilung` nennen, insbesondere `bafin-kommunikation-und-anhoerung`, `bankaufsichtsrecht-kwg-marisk-triage`, `dora-ict-vertraege-vorfall`, `gwg-aml-kyc-verdachtsmeldung`, `vorstandsvorlage-gutachten` oder `produktfreigabe-new-product-process`.

## Spezialhinweise

- **PSD3/PSR:** Als EU-Gesetzgebungsvorschau behandeln, bis finaler Text und nationale Umsetzung/Anpassung greifbar sind. Keine Scheingeltung behaupten.
- **eWpG/MiCAR:** Immer zuerst trennen, ob der Token ein Finanzinstrument, elektronisches Wertpapier, Kryptowert, E-Geld-Token, vermögenswertreferenzierter Token oder etwas anderes ist.
- **ZAG:** Zahlungsfluss und Besitz an Kundengeldern sind zentral. Grafische Flow-of-Funds-Logik in Worte übersetzen.
- **Geschäftsleiter/FAP:** Nicht nur Einzelperson prüfen, sondern Kollektiveignung, Zeitverfügbarkeit, Interessenkonflikte und Einreichkanal.
- **Tokenisierung:** Keine Technikromantik. Rechtsposition, Register, Verwahrung, Übertragung, Verlustfall, Kundenschutz und Aufsicht zuerst.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 4. `esg-sustainable-finance`

**Fokus:** ESG und Sustainable Finance in der Bank: Offenlegung, Taxonomie, Green Claims, Kreditpolitik, Anlageprodukte, Reputationsrisiko und Vorstandskommunikation prüfen.

# ESG Sustainable Finance

## Fachkern: ESG Sustainable Finance
- **Spezialgegenstand:** ESG Sustainable Finance. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Nachhaltigkeitsbezogenes Produkt, Kreditpolicy, Marketingaussage oder Reporting wird juristisch bewertet.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Produkt, Aussage, Datenbasis, Zielgruppe, Offenlegung, Taxonomiebezug, Kontrollen.
- **Institut:** Rechtsform, Erlaubnisstatus, SSM-/LSI-Status, Geschäftsmodell, Konzernbezug, relevante Tochter oder Zweigniederlassung.
- **Dokumente:** Vertrag, Aufsichtsschreiben, Kreditakte, Sanierungsgutachten, Richtlinie, Vorstandsvorlage, Rechnung, Beschwerde, Registerauszug, Datenraum oder Screenshot.
- **Frist und Forum:** BaFin, Bundesbank, EZB/SSM, FIU, Gericht, Ombudsstelle, Vorstand, Aufsichtsrat, HV, Prüfung, Closing oder interne Deadline.
- **Risikodimension:** Aufsicht, Zivilrecht, Straf-/OWi-Risiko, Organhaftung, Datenschutz, Bankgeheimnis, Reputation, Kosten, Operational Risk.

## Prüfworkflow

### 1. Kurzbild

Fasse in fünf bis acht Zeilen zusammen:

| Punkt | Inhalt |
| --- | --- |
| Vorgang | Was liegt auf dem Tisch? |
| Entscheider | Wer muss freigeben oder informiert werden? |
| Frist | Was läuft wann ab? |
| Primärrecht | Welche Normen oder Behördenstandards tragen die Prüfung? |
| Risiko | Rot, Gelb oder Grün mit einem Satz Begründung. |
| Nächster Schritt | Was sollte die Bank jetzt konkret tun? |

### 2. Rechts- und Governance-Karte

Prüfe je nach Fall insbesondere:

- **Bankaufsicht:** KWG, MaRisk, DORA, CRR/CRD, WpHG, WpIG, ZAG, GwG, BaFin-/Bundesbank-/EBA-/EZB-Vorgaben.
- **Zivilrecht:** BGB-Vertrag, AGB-Kontrolle, Darlehen, Kündigung, Sicherheiten, Haftung, Datenschutz, Geschäftsgeheimnis und Bankgeheimnis.
- **Gesellschaftsrecht:** AktG, GmbHG, Satzung, Geschäftsordnung, Vorstand, Aufsichtsrat, Ausschüsse, HV, Interessenkonflikte und Business Judgment Rule.
- **Kredit und Krise:** Sanierungsgutachten, Fortbestehensprognose, Liquiditätsplanung, Forbearance, Sicherheiten, Insolvenzanfechtung, StaRUG-/InsO-Schnittstelle.
- **Vertrieb:** Handelsvertreterrecht, Vermittler, Provision, WpHG-Vertriebspflichten, Beschwerden, Ombudsmann, Produktfreigabe.
- **Operations:** Auslagerung, IT, Cloud, DORA, Dienstleistersteuerung, interne Richtlinien, Datenraum, Rechnungsreview, Litigation.

### 3. Beleg- und Lückenmatrix

Erstelle eine Tabelle:

| Behauptung oder Risiko | Beleg vorhanden? | Fehlender Beleg | Warum wichtig? | Owner |
| --- | --- | --- | --- | --- |
| ... | ja/nein | ... | ... | ... |

### 4. Entscheidungsvorbereitung

Liefer ESG-Risikoampel, Greenwashing-Check, Dokumentationsliste und Textvorschläge.

Baue das Ergebnis so, dass ein Syndikus es intern weitergeben kann:

- **Für Vorstand:** stark verdichtete Entscheidung, Optionen, Risiko, Empfehlung, Kosten und Zeitplan.
- **Für Fachbereich:** klare To-dos, keine juristische Überwältigung, aber präzise rote Linien.
- **Für Aufsicht:** faktenstark, vollständig, konsistent, ohne unnötige Selbstbezichtigung oder Spekulation.
- **Für externe Kanzlei:** enger Scope, konkrete Fragen, Budget, Deadline und erwartetes Arbeitsergebnis.

## Stilregeln

- Kurz starten, dann sauber vertiefen.
- Keine Textwüste: Tabellen, Ampeln, Checklisten und Entscheidungssätze nutzen.
- Bei hoher Unsicherheit die Unsicherheit verwertbar machen: welche Tatsache fehlt, wer kann sie liefern, bis wann.
- Keine pauschalen Haftungsausschlüsse in jedem Absatz. Einmal sauber markieren, dann arbeiten.
- Rechtsprechung nur verwenden, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und freie oder amtliche Quelle geprüft sind.

## Ausgabeformate

Wähle passend oder biete maximal drei Optionen an:

1. **Legal Note** mit Kurzbild, Prüfung, Risikoampel, Empfehlung.
2. **Vorstandsvorlage** mit Beschlussvorschlag und Alternativen.
3. **BaFin-/Bundesbank-Antwortentwurf** mit Tatsachenmatrix.
4. **Vertrags- oder Klauselcheck** mit Änderungsvorschlägen.
5. **Unterlagenliste** für Fachbereich, Kanzlei, Prüfer oder Datenraum.
6. **Red-Team-Check** gegen Aufsicht, Prozessgegner, Verwalter oder interne Revision.


### Anschluss-Skills

- Bei ungeklärter Ausgangslage: `bankrechtsabteilung-kaltstart-routing`.
- Bei Aufsichtsbezug: `bankaufsichtsrecht-kwg-marisk-triage`, `bafin-kommunikation-und-anhoerung` oder `ssm-bundesbank-aufsichtsbrief`.
- Bei Kredit- und Krisenbezug: `kreditentscheidung-weiterfinanzierung`, `stundung-standstill-waiver`, `sanierungsgutachten-idw-s6-bewertung` oder `restrukturierung-kreditengagement`.
- Bei Gremienbezug: `vorstandsvorlage-gutachten`, `aufsichtsrat-vorlage-bank` oder `organhaftung-business-judgment`.
- Bei Dienstleistern und Kanzleien: `outsourcing-externe-dienstleister`, `externe-anwaelte-steuerung` oder `anwaltliche-rechnungen-review`.


## Quellenanker

Nutze vor tragenden Aussagen bevorzugt amtliche oder frei zugängliche Quellen: Gesetze im Internet für KWG, ZAG, WpHG, GwG, HGB, BGB und AktG; BaFin für MaRisk, Merkblätter und Aufsichtsinformationen; EUR-Lex für DORA, CRR/CRD und MiFID; EBA/EZB/Bundesbank für Leitlinien und Aufsichtspraxis. Das Quellenverzeichnis des Plugins liegt in `references/QUELLEN.md`.

## 5. `ewpg-emission-elektronische-wertpapiere`

**Fokus:** Emission elektronischer Wertpapiere nach eWpG prüfen: Zentralregister, Kryptowertpapierregister, Emissionsbedingungen, Registerangaben, Prospekt, Depot, Vertrieb und Anlegerkommunikation.

# eWpG-Emission

## Fachkern: eWpG-Emission
- **Spezialgegenstand:** eWpG-Emission. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank oder Kunde will Schuldverschreibung, Fondsanteil oder anderes Wertpapier elektronisch begeben.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Instrument, Emittent, Registertyp, Registerführer, Prospekt, Vertrieb, Depotanbindung, Anlegerkreis.
- **Institut und Rolle:** Bank, Zahlungsinstitut, E-Geld-Institut, Wertpapierinstitut, CRR-Kreditinstitut, FinTech-Tochter, Vermittler, Agent, Registerführer, CASP, Emittent oder Dienstleister.
- **Produkt oder Vorgang:** Zahlungsdienst, E-Geld, Kredit, Wertpapier, Token, Register, Organwechsel, Auslagerung, Betrugsfall, Trade Finance oder Kooperation.
- **Aufsicht und Einreichweg:** BaFin, Bundesbank, EZB/SSM, EBA, FIU, Register, MVP, IMAS, Bundesanzeiger, Handelsregister oder interner Ausschuss.
- **Dokumente:** Produktbeschreibung, Flow-of-Funds, Vertragsentwurf, API-Doku, Token Terms, Organ-CV, Eignungsmatrix, Registerauszug, Kundenkommunikation, Logs oder Vorstandsvorlage.

## Prüfaufbau

### 1. Kurzbild

| Punkt | Klärung |
| --- | --- |
| Ergebnisbedarf | Vermerk, Freigabe, BaFin-Anfrage, Vertrag, Vorstandsvorlage oder Prozessstrategie |
| Rechtsregime | KWG, ZAG, WpHG, WpIG, eWpG, MiCAR, DORA, GwG, BGB, HGB, AktG, SEPA-/EU-Regime oder Entwurf |
| Risiko | Aufsicht, Bußgeld, Zivilhaftung, Organhaftung, Kundenstreit, AML, Datenschutz, IT oder Reputation |
| Frist | Anzeige, Launch, Antwort, Rückgabe, Register, Gremium oder Verjährung |
| Entscheidung | Go, Go mit Auflagen, Stop, BaFin-Vorabklärung oder externe Spezialprüfung |

### 2. Subsumtion und Geschäftsmodell

Arbeite in dieser Reihenfolge:

1. Lebenssachverhalt und Rollen in einfachen Sätzen festhalten.
2. Geld-, Daten-, Wertpapier- oder Tokenfluss als Tabelle beschreiben.
3. Tatbestandsmerkmale einzeln prüfen.
4. Ausnahmen, Privilegierungen, Bestandsschutz, Übergangsregeln oder Entwurfsstand gesondert behandeln.
5. Gegenargumente und Red-Team-Sicht der Aufsicht formulieren.
6. Praktische Auflagen für Launch, Fortführung, Korrektur oder Ablehnung schreiben.

### 3. Beleg- und Unterlagenliste

| Frage | Beleg | Fehlt | Owner | Wirkung |
| --- | --- | --- | --- | --- |
| Wer erbringt welche Leistung? | Vertrag, Produktbild, Prozess | ... | Legal/Produkt | Regimewahl |
| Fließen Kundengelder oder Kryptowerte? | Flow-of-Funds, Wallet-/Kontoauszug | ... | Operations/Risk | Erlaubnis/Haftung |
| Gibt es Aufsichtskontakt? | Schreiben, Ticket, Portalnachweis | ... | Legal/Compliance | Frist/Strategie |
| Sind Kunden betroffen? | AGB, FAQ, Beschwerde, Marketing | ... | Vertrieb/Legal | Transparenz/Haftung |

### 4. Ergebnis

Liefer eWpG-Fahrplan, Registerentscheidung, Pflichtangaben, Prospekt-/WpHG-Schnittstelle und Closing-Check.

Baue das Ergebnis mit diesen Elementen:

- **Entscheidungssatz:** Ein Satz, der intern zitiert werden kann.
- **Risikoampel:** Rot/Gelb/Grün mit kurzer Begründung.
- **Auflagen:** Welche Bedingungen müssen vor Go-Live oder vor Antwort erfüllt sein?
- **Offene Punkte:** konkrete Rückfragen statt allgemeiner Rechercheaufträge.
- **Anschluss-Skills:** passende Skills aus `bank-rechtsabteilung` nennen, insbesondere `bafin-kommunikation-und-anhoerung`, `bankaufsichtsrecht-kwg-marisk-triage`, `dora-ict-vertraege-vorfall`, `gwg-aml-kyc-verdachtsmeldung`, `vorstandsvorlage-gutachten` oder `produktfreigabe-new-product-process`.

## Spezialhinweise

- **PSD3/PSR:** Als EU-Gesetzgebungsvorschau behandeln, bis finaler Text und nationale Umsetzung/Anpassung greifbar sind. Keine Scheingeltung behaupten.
- **eWpG/MiCAR:** Immer zuerst trennen, ob der Token ein Finanzinstrument, elektronisches Wertpapier, Kryptowert, E-Geld-Token, vermögenswertreferenzierter Token oder etwas anderes ist.
- **ZAG:** Zahlungsfluss und Besitz an Kundengeldern sind zentral. Grafische Flow-of-Funds-Logik in Worte übersetzen.
- **Geschäftsleiter/FAP:** Nicht nur Einzelperson prüfen, sondern Kollektiveignung, Zeitverfügbarkeit, Interessenkonflikte und Einreichkanal.
- **Tokenisierung:** Keine Technikromantik. Rechtsposition, Register, Verwahrung, Übertragung, Verlustfall, Kundenschutz und Aufsicht zuerst.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?
