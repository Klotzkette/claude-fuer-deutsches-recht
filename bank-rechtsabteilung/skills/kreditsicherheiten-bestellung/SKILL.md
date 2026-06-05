---
name: kreditsicherheiten-bestellung
description: "Kreditsicherheiten Bestellung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kreditsicherheiten Bestellung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Kreditsicherheiten Bestellung** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kreditsicherheiten-bestellung-verwertung` | Kreditsicherheiten bestellen, prüfen und verwerten: Grundschuld, Bürgschaft, Garantie, Globalzession, Sicherungsübereignung, Pfandrechte, Rang, Freigabe und Verwertungsschritte. |
| `kreditwesengesetz-erlaubnis-inhaberkontrolle` | KWG-Erlaubnis, Erlaubniserweiterung, Inhaberkontrolle und qualifizierte Beteiligung prüfen: Geschäftsmodell, Schwellen, Anzeige, Fit-and-Proper und BaFin-Erwartungen strukturieren. |
| `liquiditaetsbruecke-firmenkunde-bankinstrumente` | Bankinstrumente als Liquiditätsbrücke für Firmenkunden strukturieren: Aval, Kontokorrent, Factoring, Forfaitierung, Akkreditiv, Lieferantenkredit, Stundung, Waiver und Sanierungsnähe mit Rechts- und Risikomatrix. |
| `ma-risk-compliance-funktion` | MaRisk-Compliance-Funktion und zweite Verteidigungslinie prüfen: Aufgaben, Unabhängigkeit, Compliance-Plan, Monitoring, Findings, Berichtslinie und Verhältnis zu Recht, Risk und Revision. |
| `marisk-auslagerungen-at9-dora` | MaRisk-Auslagerung und DORA-Schnittstelle: AT 9, § 25b KWG, Auslagerungsregister, Risikoanalyse, wesentliche Auslagerung, IKT-Drittanbieter und Exit-Plan zusammen prüfen. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **Kreditsicherheiten Bestellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kreditsicherheiten-bestellung-verwertung`

**Fokus:** Kreditsicherheiten bestellen, prüfen und verwerten: Grundschuld, Bürgschaft, Garantie, Globalzession, Sicherungsübereignung, Pfandrechte, Rang, Freigabe und Verwertungsschritte.

# Kreditsicherheiten

## Fachkern: Kreditsicherheiten
- **Spezialgegenstand:** Kreditsicherheiten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Neue Finanzierung, Prolongation, Covenant-Bruch, Enforcement oder Sicherheitenfreigabe steht an.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Sicherheitenvertrag, Register, Grundbuch, Forderungen, Warenlager, Rang, Valutierung, Verwertungsanlass.
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

Erzeuge Sicherheitenmatrix, Vollzugscheck, Defect-Liste, Enforcement-Fahrplan und Freigabevermerk.

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

## 2. `kreditwesengesetz-erlaubnis-inhaberkontrolle`

**Fokus:** KWG-Erlaubnis, Erlaubniserweiterung, Inhaberkontrolle und qualifizierte Beteiligung prüfen: Geschäftsmodell, Schwellen, Anzeige, Fit-and-Proper und BaFin-Erwartungen strukturieren.

# KWG-Erlaubnis und Inhaberkontrolle

## Worum es geht

Dieser Skill analysiert, ob ein Geschäftsmodell einer KWG-Erlaubnis bedarf, welche Tatbestandsmerkmale einschlägig sind und welche Inhaberkontrollverfahren bei qualifizierten Beteiligungen ablaufen. Die Normenstruktur folgt § 1 KWG (Tatbestände), § 32 KWG (Erlaubnispflicht) und § 2c KWG (Inhaberkontrolle). Fit-and-Proper-Anforderungen für Geschäftsleiter und Aufsichtsorgane sind eingebettet.

## Kernnormen

- **§ 1 Abs. 1 KWG** – abschließender Katalog der Bankgeschäfte (Nr. 1–12): Einlagengeschäft, Kreditgeschäft, Diskontgeschäft, Finanzkommissionsgeschäft u.a.; Abs. 1a: Finanzdienstleistungen (Nr. 1–11)
- **§ 32 KWG** – Erlaubnispflicht: schriftlicher Antrag, Inhalt des Geschäftsplans, BaFin-Entscheidungsfrist (12 Monate bei vollständigem Antrag)
- **§ 33 KWG** – Versagungsgründe: Abs. 1 Nr. 1 (Anfangskapital), Nr. 2 (Zuverlässigkeit), Nr. 3 (Eignung), Nr. 4 (Geschäftsplan), Abs. 2 (Inhaberkontrolle)
- **§ 2c KWG** – Inhaberkontrolle bei qualifizierten Beteiligungen: Schwellen 10 %, 20 %, 30 %, 50 % oder Mehrheitsbeteiligung; Anzeigepflicht Erwerb und Veräußerung; BaFin-Untersagungsrecht; Abs. 1b Fristen
- **§ 24 KWG** – Anzeigepflichten: Abs. 1 Nr. 1 (Organbestellung), Nr. 11 (qualifizierte Beteiligung), Nr. 12 (Unterschreiten 10 %); AnzV-Formulare
- **§ 25c KWG** – Fit-and-Proper Geschäftsleiter: Abs. 1 Zuverlässigkeit und Sachkunde, Abs. 2 Zeitbudget (Vollzeitäquivalent), Abs. 4 Abs. 4a Doppelmandate
- **§ 35 KWG** – Aufhebung der Erlaubnis: Abs. 1 (Antrag), Abs. 2 (Amts-wegen bei dauerhafter Nichtausübung, Versagungsgründen, Insolvenz)
- **§ 36 KWG** – Abberufung von Geschäftsleitern durch BaFin bei dauerhafter Ungeeignetheit oder Unzuverlässigkeit

## Prüfschritte

1. **Tatbestandssubsumtion** (§ 1 Abs. 1 und 1a KWG): Welches Bankgeschäft oder welche Finanzdienstleistung liegt vor? Greift eine Ausnahme (§ 2 KWG Konzernprivileg, Nebenleistung)?
2. **Anfangskapital** (§ 33 Abs. 1 Nr. 1 KWG, CRD-V-Verweis): Mindestkapital je Institutstyp ermitteln; für Kredit-Institute gemäß § 10 Abs. 1 KWG i.V.m. CRR Art. 92.
3. **Geschäftsplan** (§ 32 Abs. 1 Satz 2 KWG): Drei-Jahres-Plan, IT-Konzept, Organisationsplan, Angaben zu Inhabern, Auslagerungen.
4. **Inhaberkontrolle** (§ 2c KWG, InhKontrollV): Schwellenwert berechnen, Absichtsanzeige vorbereiten, Fristen wahren (BaFin 60 Werktage), Verlängerungsoption prüfen.
5. **Fit-and-Proper** (§ 25c KWG, EBA/GL/2021/06): Lebenslauf, Selbstauskunft, Führungszeugnis, Zeitbudget-Nachweis für jeden Geschäftsleiter.
6. **Erlaubnisantrag einreichen** (§ 32 KWG): vollständige Unterlagen an BaFin per MVPportal; 12-Monatsfrist läuft ab Vollständigkeit.
7. **Versagungsrisiko** (§ 33 KWG): Prüfe alle Versagungsgründe vorab; unvollständiger Antrag hemmt Fristlauf.

## Typische Fallkonstellationen

- FinTech-Gründung plant Einlagen: § 1 Abs. 1 Nr. 1 KWG Erlaubnispflicht, § 32 KWG Antrag, Mindestkapital 5 Mio. Euro (CRD V)
- Gesellschafter-Einstieg bei 15 %: § 2c KWG Inhaberkontrolle, Anzeigepflicht vor Vollzug, InhKontrollV-Formular
- Erweiterung Erlaubnis (neues Kreditgeschäft): § 32 KWG Erweiterungsantrag, § 33 Nr. 4 (Geschäftsplan), BaFin-Abstimmung
- Abberufungsverlangen BaFin: § 36 KWG, vorherige Anhörung, aufschiebende Wirkung nur bei Antrag
- Unterschreiten 10 %-Schwelle: § 24 Abs. 1 Nr. 12 KWG Anzeige nachträglich, AnzV § 18

## Output

Erlaubnisantrags-Checkliste mit Normbezug; Inhaberkontroll-Absichtsanzeige (Entwurf); Fit-and-Proper-Selbstauskunftsbogen; Vermerk zu Versagungsrisiken mit Risikoampel.

## Quellenregel

gesetze-im-internet.de (KWG, InhKontrollV, AnzV), bafin.de (Merkblatt Inhaberkontrolle, Formular-Center), eba.europa.eu (EBA/GL/2021/06 Fit-and-Proper). Live-Check: BaFin-Merkblätter zu Erlaubnispflicht werden nach Gesetzesänderungen aktualisiert.

## 3. `liquiditaetsbruecke-firmenkunde-bankinstrumente`

**Fokus:** Bankinstrumente als Liquiditätsbrücke für Firmenkunden strukturieren: Aval, Kontokorrent, Factoring, Forfaitierung, Akkreditiv, Lieferantenkredit, Stundung, Waiver und Sanierungsnähe mit Rechts- und Risikomatrix.

# Liquiditätsbrücke durch Bankinstrumente

## Fachkern: Liquiditätsbrücke durch Bankinstrumente
- **Spezialgegenstand:** Liquiditätsbrücke durch Bankinstrumente. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Zeige praktisch, wie Banken den Geschäftsverkehr mit Liquidität schmieren, ohne ihre Kreditakte zu ruinieren: nicht nur Darlehen, sondern Avale, Akkreditive, Factoring, Forfaitierung, Stundung, Waiver, Supply-Chain-Finance und Sicherheitenumbau.

## Instrumentenkarte

| Instrument | Liquiditätseffekt | Hauptprüfung |
| --- | --- | --- |
| Aval/Kautionsaval | Barkaution wird ersetzt | Abruf- und Regressrisiko |
| Kontokorrentlinie | Zahlungsfähigkeit kurzfristig | Kündigung, Limit, Covenants |
| Factoring | Forderungen werden zu Liquidität | Abtretbarkeit, Debitoren, Delkredere |
| Forfaitierung | Einzelforderung wird verkauft | Rechtsbestand, Einwendungen, Export |
| Akkreditiv | Lieferant erhält Sicherheit | Dokumentenstrenge, Sanktionen |
| Stundung/Waiver | Abfluss wird verschoben | Forbearance, NPE, Anfechtung |
| Lieferantenfinanzierung | Working Capital wird entlastet | Rollen, ZAG/KWG, Transparenz |

## Prüfworkflow

1. **Liquiditätslücke:** Betrag, Zeitpunkt, Ursache, einmalig oder strukturell.
2. **Instrument passend wählen:** Welches Instrument löst die Lücke mit geringstem Rechts-/Aufsichtsrisiko?
3. **Kreditakte:** Rating, Limit, Sicherheiten, Covenants, Forbearance, Beschlusskompetenz.
4. **Rechtsrisiken:** AGB, Abtretungsverbote, Insolvenzanfechtung, ZAG/KWG, Datenschutz, Sanktionen.
5. **Dokumentation:** Warum ist die Entscheidung bankmäßig vertretbar?

## Ergebnis

Liefere eine **Liquiditätsbrücken-Matrix**:

| Option | Liquidität | Risiko Bank | Risiko Kunde | Aufwand | Empfehlung |
| --- | --- | --- | --- | --- | --- |

Ergänze:

- konkrete nächste Unterlagen,
- Beschluss-/Kompetenzweg,
- Kundentext,
- Red-Team-Fragen von Risk, Revision und BaFin.

## Anschluss-Skills

- `avalrahmenlinie-kautionsaval-praxis`
- `dokumentengeschaeft-akkreditiv-inkasso-standby`
- `stundung-standstill-waiver`
- `forbearance-npe-risikoklassifizierung`
- `sanierungsgutachten-idw-s6-bewertung`

## 4. `ma-risk-compliance-funktion`

**Fokus:** MaRisk-Compliance-Funktion und zweite Verteidigungslinie prüfen: Aufgaben, Unabhängigkeit, Compliance-Plan, Monitoring, Findings, Berichtslinie und Verhältnis zu Recht, Risk und Revision.

# MaRisk Compliance-Funktion

## Fachkern: MaRisk Compliance-Funktion
- **Spezialgegenstand:** MaRisk Compliance-Funktion. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Compliance-Struktur, Jahresplan, Bericht, Finding oder Abgrenzung zwischen Legal und Compliance soll bewertet werden.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Organigramm, Richtlinien, Jahresplan, Berichte, Findings, Ressourcenausstattung, Eskalationen.
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

Erzeuge Rollenklärung, Gap-Liste, Reporting-Vorschlag und Maßnahmenplan.

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

## 5. `marisk-auslagerungen-at9-dora`

**Fokus:** MaRisk-Auslagerung und DORA-Schnittstelle: AT 9, § 25b KWG, Auslagerungsregister, Risikoanalyse, wesentliche Auslagerung, IKT-Drittanbieter und Exit-Plan zusammen prüfen.

# Auslagerung und DORA

## Fachkern: Auslagerung und DORA
- **Spezialgegenstand:** Auslagerung und DORA. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** IT-, Cloud-, Zahlungs-, Callcenter-, KYC-, Backoffice- oder Gruppenleistungen werden ausgelagert oder wesentlich geändert.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Leistungsbeschreibung, Anbieter, Kritikalität, Daten, Subdienstleister, SLA, Exit, Registereintrag.
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

Liefer Entscheidung wesentliche Auslagerung ja/nein, Klausellücken, Melde- und Registerlogik, Umsetzungsplan.

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

## DORA-Drittparteien-Vertiefung

Bei IKT-Dienstleistern den gesamten Lebenszyklus prüfen: Ex-ante-Risikoanalyse, Due Diligence, Vertragsklauseln, Register-of-Information-Daten, Monitoring, Subdienstleister, Konzentrationsrisiko, Incident-Unterstützung und Exit. Bei Artikel-16-Unternehmen die Erleichterungen dokumentieren, aber Kontrollrechte, Informationsrechte, Krisenfähigkeit und Nachweise nicht wegdefinieren.
