---
name: zag-vorstandsvorlage-gutachten-wpig
description: "ZAG Vorstandsvorlage Gutachten Wpig: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZAG Vorstandsvorlage Gutachten Wpig

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **ZAG Vorstandsvorlage Gutachten Wpig** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vorstandsvorlage-gutachten` | Vorstandsvorlage und juristisches Gutachten für eine Bank erstellen: Entscheidungssatz, Risikoampel, Handlungsoptionen, Beschlussvorschlag, Annahmen, Quellen und Anlagenverzeichnis. |
| `wpig-wertpapierinstitut-schnittstelle` | WpIG-Schnittstellen prüfen, wenn Bankgruppe, Wertpapierinstitut, Vermittler oder Tochtergesellschaft beteiligt sind: Rollen, Erlaubnis, Eigenmittel, Auslagerung und Governance abgrenzen. |
| `zag-agenten-auslagerung-register` | ZAG-Agenten, E-Geld-Agenten und Auslagerung prüfen: Register, Haftung, Weisungen, Schulungen, AML, Kundenkommunikation, Passporting und Abgrenzung zum bloßen Dienstleister. |
| `zag-ausnahmen-limited-network-commercial-agent` | ZAG-Ausnahmen tief prüfen: begrenztes Netz, begrenzte Produktpalette, Handelsvertreterausnahme, technische Dienstleister, Konzernprivileg und digitale Plattformrisiken. |
| `zag-e-geld-institut-emoney` | E-Geld-Institut und E-Geld-Geschäft nach ZAG prüfen: Ausgabe, Rücktausch, monetärer Wert, Akzeptanzstellen, Sicherungsmittel, Eigenmittel, Vertrieb und Abgrenzung zu Gutschein, Token und Einlage. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **ZAG Vorstandsvorlage Gutachten Wpig**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vorstandsvorlage-gutachten`

**Fokus:** Vorstandsvorlage und juristisches Gutachten für eine Bank erstellen: Entscheidungssatz, Risikoampel, Handlungsoptionen, Beschlussvorschlag, Annahmen, Quellen und Anlagenverzeichnis.

# Vorstandsvorlage

## Fachkern: Vorstandsvorlage
- **Spezialgegenstand:** Vorstandsvorlage. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Legal soll für Vorstand, Bereichsleitung oder Gremium eine prägnante Vorlage erstellen.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Entscheidung, Sachverhalt, Optionen, Zahlen, Risiken, Frist, Fachbereiche, gewünschter Beschluss.
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

Erzeuge Executive Summary, Beschlussvorschlag, juristische Würdigung, Risiken und nächste Schritte.

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

## 2. `wpig-wertpapierinstitut-schnittstelle`

**Fokus:** WpIG-Schnittstellen prüfen, wenn Bankgruppe, Wertpapierinstitut, Vermittler oder Tochtergesellschaft beteiligt sind: Rollen, Erlaubnis, Eigenmittel, Auslagerung und Governance abgrenzen.

# WpIG-Schnittstelle

## Fachkern: WpIG-Schnittstelle
- **Spezialgegenstand:** WpIG-Schnittstelle. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Eine Tochter, Kooperation oder Vertriebseinheit ist Wertpapierinstitut oder nah an WpIG-/KWG-Schnittstellen.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Rolle, Dienstleistungen, Kundentyp, Gruppenstruktur, Erlaubnisstatus, Auslagerungen.
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

Liefer Abgrenzungsnotiz KWG/WpIG, Risiken, Zuständigkeiten und nächste Behördenfragen.

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

## 3. `zag-agenten-auslagerung-register`

**Fokus:** ZAG-Agenten, E-Geld-Agenten und Auslagerung prüfen: Register, Haftung, Weisungen, Schulungen, AML, Kundenkommunikation, Passporting und Abgrenzung zum bloßen Dienstleister.

# ZAG-Agenten, E-Geld-Agenten und Auslagerung

## Worum es geht

Dieser Skill prüft den Einsatz von Agenten und die Auslagerung bei ZAG-Instituten: Registrierungspflicht, Haftungsverantwortung des Hauptinstituts, AML-Integration, Auslagerungsanzeige und Anforderungen an ICT-Drittparteien nach DORA. Die Abgrenzung zwischen erlaubnispflichtigem Agenten und erlaubnisfreiem technischen Dienstleister ist zentral.

## Kernnormen

- **§ 25 ZAG** – Agenten von Zahlungsinstituten: Registrierung vor Tätigkeitsaufnahme im BaFin-Agenten-Register; Angaben zu Identität, Diensten, Geschäftsgebiet; Haftung des Instituts für Agentenhandeln als eigenes
- **§ 26 ZAG** – Auslagerung bei Zahlungsinstituten: wesentliche operative Funktionen (inkl. IT-Kernfunktionen); Vorab-Risikoanalyse; Prüfungs- und Informationsrechte; keine Auslagerung der Gesamtverantwortung
- **§ 24 ZAG** – Auslagerung wesentlicher Funktionen: Anzeigepflicht an BaFin; Mindestvertragsinhalt (SLA, Ausstiegsklausel, Prüfungsrecht); Notfallplanung
- **§ 23a ZAG** – E-Geld-Agenten: analoge Anforderungen wie § 25 ZAG; zusätzlich Identitätsprüfung-Pflicht (KYC) im Agentenprozess; AML-Schulungspflicht
- **EBA/GL/2017/09** – Leitlinie zu Agenten und Auslagerung bei Zahlungsinstituten: Abgrenzungskriterien, Überwachungspflichten, Register-Inhalt, Passporting-Verfahren
- **DORA Art. 28–30** (VO 2022/2554) – ICT-Drittparteienmanagement: Register kritischer Drittparteien (Art. 28 Abs. 3), vertragliche Mindestklauseln (Art. 30), Konzentrations-Risikoüberwachung (Art. 29); gilt für ZAG-Institute als Finanzunternehmen
- **GwG §§ 17, 18** – AML-Pflichten bei Agentenvertrieb: Institut muss Agenten in AML-Compliance einbinden; regelmäßige Schulungen, Risikoklassifizierung Agenten
- **§ 38 ZAG** – Passporting: Notifizierungsverfahren für grenzüberschreitende Dienste; Agenten im Aufnahmestaat über dortige Behörde registrieren

## Prüfschritte

1. **Agent vs. Dienstleister** (§ 25 ZAG, EBA/GL/2017/09): Handelt die Partei im Namen des Instituts gegenüber Kunden? Übernimmt sie Zahlungsdienstleistungs-Risiko? Wenn ja = Agent, Registrierungspflicht.
2. **Agentenregistrierung** (§ 25 Abs. 1 ZAG): Vor Tätigkeitsaufnahme bei BaFin registrieren; Angaben: Name, Adresse, angebotene Zahlungsdienste, Zeitraum.
3. **Haftungsübernahme** (§ 25 Abs. 3 ZAG): Vertragliche Haftungsübernahme des Instituts für Agentenverhalten; keine Möglichkeit zur Haftungsauslagerung.
4. **AML-Integration** (GwG §§ 17, 18): Agenten in Risikomanagementsystem einbinden; regelmäßige Schulungen dokumentieren; Transaktionsmonitoring auch für Agenten-Transaktionen.
5. **Auslagerungsanzeige** (§ 24, § 26 ZAG): Wesentliche Funktion definieren (IT-Plattform, Compliance, Betriebsführung); Anzeige vor Vollzug an BaFin; Vertrag mit Mindestklauseln.
6. **DORA-Anforderungen** (Art. 28–30 VO 2022/2554): ICT-Dienstleister in Register eintragen; kritische Dienstleister identifizieren; Art. 30-Klauseln in Verträge aufnehmen (Ausstieg, Prüfungsrecht, Datenlokalisierung).
7. **Passporting** (§ 38 ZAG): Agenten in anderen EWR-Staaten über dortige Aufsicht registrieren; Notifizierung durch BaFin.

## Typische Fallkonstellationen

- Supermarkt als Zahlungsagent (Bargeld ein-/auszahlen): § 25 ZAG Registrierung, GwG-Schulung, Haftung des Instituts
- Cloud-Provider für Kernbanksystem: § 26 ZAG wesentliche Auslagerung, § 24 ZAG Anzeige, DORA Art. 28–30 kritischer ICT-Drittanbieter
- E-Geld-Vertrieb über Kiosknetz: § 23a ZAG E-Geld-Agenten, KYC-Pflicht, AML-Training, BaFin-Register
- Passporting: Deutsches ZAG-Institut expandiert nach Frankreich: § 38 ZAG Notifizierung; Agenten in Frankreich über AMF registrieren
- Ausgliederung Compliance-Funktion: § 26 ZAG Risikoanalyse; wesentliche Funktion; keine vollständige Delegation der Compliance-Verantwortung möglich

## Output

Agenten-Registrierungsanzeige-Vorlage § 25 ZAG; Auslagerungsvertrag-Mindestklausel-Checkliste (§ 24 ZAG, DORA Art. 30); DORA-ICT-Drittparteien-Register-Template; AML-Schulungsplan für Agenten; Risikoampel wesentliche vs. nicht-wesentliche Auslagerung.

## Quellenregel

gesetze-im-internet.de (ZAG, GwG), eur-lex.europa.eu (DORA VO 2022/2554), eba.europa.eu (EBA/GL/2017/09 Agenten und Auslagerung), bafin.de (Merkblatt ZAG-Auslagerung). Live-Check: DORA gilt seit 17.01.2025; EBA DORA-ITS/RTS auf eba.europa.eu; EBA/GL/2017/09 überarbeitet nach DORA.

## 4. `zag-ausnahmen-limited-network-commercial-agent`

**Fokus:** ZAG-Ausnahmen tief prüfen: begrenztes Netz, begrenzte Produktpalette, Handelsvertreterausnahme, technische Dienstleister, Konzernprivileg und digitale Plattformrisiken.

# ZAG-Ausnahmen

## Fachkern: ZAG-Ausnahmen
- **Spezialgegenstand:** ZAG-Ausnahmen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Ein Geschäftsmodell soll ohne Erlaubnis laufen oder beruft sich auf Limited Network, Commercial Agent oder technische Ausnahme.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Akzeptanzstellen, Warenkreis, Agentenrolle, Vertragsbefugnis, Kundengelder, Plattform, Schwellen, Meldungen.
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

Erzeuge Ausnahmeampel, Meldepflichten, Red Flags, Alternativstruktur und BaFin-taugliche Begründung.

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

## Enger Ausnahme-Check

Ausnahmen nach § 2 ZAG erst prüfen, wenn der mögliche Zahlungsdienst beschrieben ist. Die Begründung muss BaFin-tauglich sein:

| Ausnahme | Beleg, der wirklich hilft | Red Flag |
| --- | --- | --- |
| Handelsvertreter | echte Vertretungs-/Abschlussbefugnis nur für eine Marktseite | Plattform steuert Preis, Zahlung und Streitbeilegung für beide Seiten |
| Technischer Dienstleister | kein Besitz an Geld, keine Entscheidung über Zahlung, nur technische Weiterleitung | Dienstleister hält Treuhandkonto, kann Auszahlung stoppen oder zahlt selbst aus |
| Limited Network | geschlossene Akzeptanzstellenliste, professioneller Emittent, Monitoring | ständig wachsendes Partnernetz, allgemeines Zahlungsmittelgefühl |
| Limited Range | sehr enger Waren-/Dienstleistungskreis mit SKU-/MCC-Logik | Marktplatz, breites Sortiment, Lifestyle-Karte |
| Konzernintern | ausschließlich gruppeninterne Zahlungsvorgänge | Kunden, Händler, Franchise- oder Plattformteilnehmer sind beteiligt |
| Sozial/Steuer | zweckgebundene öffentliche oder steuerlich eingehegte Nutzung | kommerzielle Benefit-Karte ohne echte Zweckbindung |

Gib am Ende immer aus: Ausnahme tragfähig, Ausnahme nur mit Anzeige/Monitoring, BaFin-Vorabklärung oder Stop bis Erlaubnisanalyse.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 5. `zag-e-geld-institut-emoney`

**Fokus:** E-Geld-Institut und E-Geld-Geschäft nach ZAG prüfen: Ausgabe, Rücktausch, monetärer Wert, Akzeptanzstellen, Sicherungsmittel, Eigenmittel, Vertrieb und Abgrenzung zu Gutschein, Token und Einlage.

# E-Geld-Institut und E-Geld-Geschäft nach ZAG

## Worum es geht

Dieser Skill prüft das E-Geld-Geschäft nach ZAG: ob ein Produkt E-Geld im Sinne von § 1 Abs. 2 ZAG ist, welche Erlaubnisanforderungen gelten und wie Eigenmittel, Sicherung, Ausgabe und Rücktausch rechtssicher ausgestaltet werden. Abgrenzungen zu Gutscheinen, Kryptowerten (MiCAR) und Bankeinlagen (KWG) werden durchgeführt.

## Kernnormen

- **§ 1 Abs. 2 ZAG** – E-Geld-Definition: elektronisch gespeicherter monetärer Wert in Form einer Forderung gegen den Emittenten, ausgegeben gegen Zahlung, zur Durchführung von Zahlungsvorgängen; drei kumulative Voraussetzungen
- **§ 11 Abs. 1 Nr. 1 ZAG** – E-Geld-Institut-Erlaubnis: Antrag bei BaFin, Inhalt wie § 10 ZAG; Erlaubnis umfasst Zahlungsdienste nach § 1 Abs. 1 Satz 2 Nr. 1–6 ZAG automatisch
- **§ 17 ZAG** – Anfangskapital E-Geld-Institut: 350 TEUR (gegenüber 50/125 TEUR bei reinen ZI); laufende Eigenmittel nach Methode D (2 % des durchschnittlichen E-Geld-Umlaufs)
- **§ 11a ZAG** – Ausgabe und Rücktausch: Ausgabe zum Nennwert, Rücktauschpflicht auf Verlangen des Inhabers, Entgeltbeschränkung beim Rücktausch
- **§ 23a ZAG** – E-Geld-Agenten: Vertrieb durch Agenten; Registrierung, Haftung des E-Geld-Instituts für Agentenverhalten, AML-Schulungspflichten
- **§ 16 ZAG** – Sicherung der Kundengelder (gilt auch für E-Geld-Institut): Treuhandkonto oder gleichwertige Sicherung für alle eingenommenen Gelder
- **§ 1 Abs. 2 ZAG i.V.m. § 1 Abs. 10 Nr. 10 ZAG** – Gutschein-Ausnahme: begrenzte Netze (Einkaufsgutschein, Tankkarte) sind kein E-Geld wenn Akzeptanzstellenkreis eng begrenzt
- **Art. 1 EMD2** (Richtlinie 2009/110/EG) – E-Geld-Definition europarechtliche Grundlage; harmonisierte Anforderungen; Umsetzung im ZAG

## Prüfschritte

1. **E-Geld-Definition** (§ 1 Abs. 2 ZAG): Ist der Wert elektronisch gespeichert, stellt er eine Forderung gegen den Emittenten dar, wird er gegen Zahlung ausgegeben und für Zahlungsvorgänge akzeptiert?
2. **Abgrenzung Einlage vs. E-Geld**: E-Geld ist keine rückzahlbare Einlage (§ 1 Abs. 2 Satz 3 ZAG); kein Zinsanspruch; kein Einlagensicherungsschutz (§ 11a Abs. 4 ZAG).
3. **Gutschein-Ausnahme** (§ 1 Abs. 10 Nr. 10 ZAG): Akzeptanzstellen auf klar definierten Kreis begrenzt? BaFin-Merkblatt E-Geld Abgrenzungsfälle beachten.
4. **Anfangskapital** (§ 17 ZAG): 350 TEUR nachweisen; laufende Eigenmittel 2 % des Durchschnitts-E-Geld-Umlaufs (Methode D).
5. **Sicherungskonzept** (§ 16 ZAG): Treuhandkonto für alle E-Geld-Kundengelder; getrennt von Eigengeldern des Instituts.
6. **Rücktauschpflicht** (§ 11a ZAG): Jederzeit auf Verlangen; Entgelt nur wenn vertraglich vereinbart und kostendeckend.
7. **Agenten** (§ 23a ZAG): Registrierung im BaFin-Register, Haftung des Instituts, AML-Schulungen nach GwG.
8. **MiCAR-Abgrenzung**: E-Geld-Token (EMT) unter MiCAR VO 2023/1114 Art. 48 ff. – spezifischer Regulierungsweg wenn Kryptowert; kein Doppelregime.

## Typische Fallkonstellationen

- Prepaid-Karte mit breitem Akzeptanznetz: § 1 Abs. 2 ZAG E-Geld, § 11 ZAG Erlaubnis, Anfangskapital 350 TEUR, § 16 Treuhand
- Supermarkt-Geschenkkarte (nur eigene Filialen): § 1 Abs. 10 Nr. 10 ZAG Ausnahme; kein E-Geld, keine Erlaubnispflicht
- Crypto-Stablecoin (EUR-backed): MiCAR Art. 48 ff. EMT-Regime statt ZAG; BaFin-Abstimmung empfehlen
- Mobile-Wallet mit E-Geld-Funktion: § 11 ZAG Erlaubnis, § 23a ZAG wenn Vertrieb über Agenten, § 16 Sicherung pro App-Nutzer
- Rücktauschverweigerung durch Institut: § 11a ZAG, zivilrechtlicher Anspruch des Inhabers; BaFin-Beschwerdeweg

## Output

E-Geld-Prüfungsschema (Definition-Checkliste); Erlaubnisantrags-Checkliste § 11 ZAG; Eigenmittelberechnung Methode D; Sicherungskonzept-Vorlage; Agenten-Registrierungsanforderungen § 23a ZAG.

## Quellenregel

gesetze-im-internet.de (ZAG), eur-lex.europa.eu (EMD2 2009/110/EG, MiCAR VO 2023/1114), bafin.de (Merkblatt E-Geld, Abgrenzungsfälle). Live-Check: BaFin-Merkblatt E-Geld zuletzt 2022; MiCAR EMT-Regime ab Juni 2024 in Kraft.
