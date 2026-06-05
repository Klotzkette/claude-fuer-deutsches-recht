---
name: fremd-mehrbesitzverbot-gefahrstoffe
description: "Fremd Mehrbesitzverbot Gefahrstoffe: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fremd Mehrbesitzverbot Gefahrstoffe

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Fremd Mehrbesitzverbot Gefahrstoffe** im Plugin Apothekenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fremd-und-mehrbesitzverbot-apothekenrecht` | Fremd- und Mehrbesitzverbot Apothekenrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `gefahrstoffe-chemikalien-ausgangsstoffe` | Gefahrstoffe Chemikalien Ausgangsstoffe: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |
| `hygiene-pandemie-infektionsschutz` | Hygiene Pandemie Infektionsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht. |

## Arbeitsweg

Im Plugin Apothekenrecht gilt für **Fremd Mehrbesitzverbot Gefahrstoffe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fremd-und-mehrbesitzverbot-apothekenrecht`

**Fokus:** Fremd- und Mehrbesitzverbot Apothekenrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Fremd- und Mehrbesitzverbot Apothekenrecht

## Fachkern: Fremd- und Mehrbesitzverbot Apothekenrecht
- **Spezialgegenstand:** Fremd- und Mehrbesitzverbot Apothekenrecht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Worum geht es konkret

Das Fremdbesitzverbot (§ 8 ApoG) untersagt es Nicht-Apothekern, Apotheken zu betreiben oder daran beteiligt zu sein. Das Mehrbesitzverbot (§ 1 Abs. 2 ApoG) begrenzt einen Apotheker auf eine Hauptapotheke plus maximal drei Filialen. Beide Verbote sind tragende Säulen des deutschen Apothekenrechts und durch Art. 12 GG sowie EU-Recht (EuGH, staend. Rspr.) ausdrücklich anerkannt.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Investor will sich an einer Apotheke beteiligen, etwa als stiller Gesellschafter oder Franchisegeber.
- Apotheker plant fünfte Filiale oder Erwerb mehrerer Apotheken.
- Gemeinsame Geschäftsführung mit nicht-pharmazeutischem Partner geplant.
- Holding-Struktur mit Apotheke und Drogerie soll aufgebaut werden.
- Behörde leitet Widerrufsverfahren wegen vermuteter Verstösse ein.

Eingaben:
- Gesellschaftsvertrag aller geplanten Beteiligten.
- Geplante Finanzierungsstruktur (Eigenkapital, Darlehen, stille Beteiligung, Genussrecht).
- Erbenfolge-Szenarien, sofern Inhaber-Tod im Raum steht.
- Bestehende und geplante Filialnetzwerke des Apothekers.

## Rechtlicher Rahmen

- **§ 1 Abs. 2 ApoG:** Mehrbesitzverbot — eine Hauptapotheke und bis zu drei Filialen pro Apotheker.
- **§ 7 ApoG:** Persönliche Leitungspflicht jeder Filiale.
- **§ 8 ApoG:** Fremdbesitzverbot — Erlaubnis nur an Apotheker; bei OHG müssen **alle** persönlich haftenden Gesellschafter Apotheker sein.
- **§§ 9, 10 ApoG:** Sondervorschriften für die Verpachtung — nur an Apotheker für sehr eingeschränkte Übergangskonstellationen.
- **§ 13 ApoG:** Erbenfortführung max. zwölf Monate.
- **Art. 12 GG:** Berufsfreiheit — BVerfG, staend. Rspr., insb. Apothekenurteil 1958.
- **EuGH** — staend. Rspr., insb. zur Vereinbarkeit des Fremdbesitzverbots mit EU-Recht (DocMorris, Apothekenkammer Saarland u. a.).

## / Schritt für Schritt

1. **Eigentumsstruktur abklären:** Wer ist Erlaubnisinhaber? Welche Beteiligungen sind geplant?
2. **Apotheker-Status aller Beteiligten:** Approbation vorhanden? Mitgliedschaft Apothekerkammer aktuell?
3. **Filialanzahl:** Wieviele Apotheken führt der Mandant bereits? Bei Erbschaft oder Übernahme: Schwelle vier nicht überschreiten.
4. **Verdeckte Konstruktionen erkennen:** Stille Beteiligung, Gewinnabführung, Darlehensgewährung mit Gewinnbeteiligung, Genussrechte, Franchise mit operativer Kontrolle.
5. **Mietverträge prüfen:** Umsatzbeteiligung des Vermieters kann mittelbar Fremdbeteiligung sein (kritisch ab 5–10 Prozent oder operativer Einflussnahme).
6. **Marketingverbund-Cooperationen:** Servicegesellschaften ohne Eigentumsanteil sind zulässig; Übergang zur operativen Steuerung wird kritisch.
7. **Stellungnahme an Behörde:** Bei drohendem Widerruf ausführliche Darlegung der Struktur — keine Verstrickung mit Nicht-Apothekern operativ.
8. **EU-Anwendbarkeit:** Apotheker aus EU-Mitgliedstaat: zulässig. Drittstaaten oder juristische Personen ohne Apothekerstatus: unzulässig.

## Trade-off-Matrix

| Modell | Zulässig? | Risiko | Praxisrelevanz |
|---|---|---|---|
| Einzelinhaber mit Filialen ≤ 3 | ja | gering | klassische Praxis |
| OHG aus zwei Apothekern | ja | gering | strukturierbar |
| Holding mit Apotheker als einzigem Geschäftsführer | nein | Widerruf | unzulässig |
| Investor als stiller Gesellschafter mit Gewinnanteil | nein | OWi / Widerruf | typische Falle |
| Mietvertrag mit Umsatzbeteiligung > 10 Prozent | grenzwertig | Aufsichtsrisiko | Einzelfall |
| Franchise mit operativer Steuerung | nein | Widerruf | unzulässig |
| Verpachtung an angestellten Apotheker (§ 9 ApoG) | ja, eng begrenzt | mittel | Übergangs-Konstruktionen |

## Praxistipps

- "Strohmann"-Konstrukte werden von der Aufsicht regelmässig durchschaut — Whistleblower, Steuerunterlagen, Mietvertrag, Versicherungsverträge.
- EuGH-Rspr. zum DocMorris-Komplex und Apothekenkammer Saarland: Fremdbesitzverbot bleibt zulässig, kein Anlass zur strategischen Hoffnung auf Lockerung.
- Beratungsleistungen durch Drittfirmen sind möglich, dürfen aber keine operative Steuerungsmacht ergeben.
- Erbenfortführung: Frist zwölf Monate aktiv überwachen, rechtzeitig Verkauf an Apotheker einleiten.
- Bei OHG-Gesellschafterwechsel: jeder neue Gesellschafter muss eigene Erlaubnis-Voraussetzungen erfüllen.

## Mustertexte

### Stellungnahme zur Anhörung "Verdacht Fremdbesitz" (Auszug)
"In der Anhörung vom [Datum] wird der Verdacht geäussert, dass die [Firma X GmbH] mittelbar an der Apotheke beteiligt ist. Hierzu legen wir folgende Sachverhalte dar: 1. Eigentumsstruktur: Erlaubnisinhaber ist Herr/Frau [Apotheker:in], 100 Prozent. 2. Vertragsbeziehungen: Mietvertrag mit [Vermieter] zu marktüblicher Festmiete (keine Umsatzbeteiligung, Anlage [Nr.]). 3. Beratungsvertrag mit [Servicefirma] beschränkt auf [Logistik / Marketing], ohne Weisungsrecht hinsichtlich pharmazeutischer Tätigkeit (Anlage [Nr.]). Eine operative Steuerung durch Nicht-Apotheker liegt nicht vor. Die Voraussetzungen des § 8 ApoG sind erfüllt."

### Hinweisschreiben an interessierten Investor (Auszug)
"Sehr geehrte:r [Investor:in], das deutsche Apothekenrecht ist durch das Fremdbesitzverbot (§ 8 ApoG) geprägt. Eine direkte oder mittelbare Beteiligung von Nicht-Apothekern an einer Apotheke ist unzulässig. Zulässig sind: (i) Erwerb durch Sie als approbierte:r Apotheker:in, (ii) marktübliche Mietverhältnisse mit Festmiete, (iii) reine Servicedienstleistungen ohne operative Steuerung. Eine Beteiligungsstruktur ist nur als OHG zwischen Apothekern, nicht als Kommanditist oder stiller Gesellschafter, zulässig."

## Typische Fehler

- "Beratungsvertrag" mit detaillierter Steuerung der Apothekenführung wird als verdecktes Fremdbesitzverhältnis qualifiziert.
- Darlehen mit Umsatzbeteiligung > 5 Prozent wird als Genussrecht eingestuft.
- Vier-Apotheken-Grenze wird durch Erbübernahme überschritten, ohne Veräusserung einzuleiten.
- Strohmann-Apotheker für Investor — bei Aufdeckung Widerruf der Erlaubnis und ggf. strafrechtliche Folgen wegen mittelbarer Tatherrschaft.
- Mietvertrag mit umsatzabhängiger Komponente nicht offengelegt — Behörde sieht verdeckte Beteiligung.

## Querverweise

- `apothekenerlaubnis-apog-persoenliche-voraussetzungen` (subjektive Voraussetzungen)
- `inhaberwechsel-kauf-apothekenbetrieb` (Übernahme)
- `filialapotheke-hauptapotheke-leitung-vertretung` (Filialgrenze)
- `widerruf-ruecknahme-ruhen-apothekenerlaubnis` (Folgen)
- `mietvertrag-apothekenstandort-konkurrenzschutz` (Mietvertragspraxis)
- `digitale-plattformen-marktplatz-apothekenrecht` (Plattform-Beteiligungen)

## Quellen Stand 06/2026

- ApoG §§ 1, 7, 8, 9, 10, 13.
- BVerfG, staend. Rspr. zur Apothekenfreiheit (Apothekenurteil 1958).
- EuGH, staend. Rspr. zum Fremdbesitzverbot (DocMorris-Verfahren, Apothekenkammer Saarland).
- BGH und OLG, staend. Rspr. zu verdeckten Fremdbesitzkonstellationen.
- Landesaufsichtsbehörden — Merkblätter zur Erlaubnisprüfung (vom Anwender zu verifizieren).

## 2. `gefahrstoffe-chemikalien-ausgangsstoffe`

**Fokus:** Gefahrstoffe Chemikalien Ausgangsstoffe: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Gefahrstoffe Chemikalien Ausgangsstoffe

## Fachkern: Gefahrstoffe Chemikalien Ausgangsstoffe
- **Spezialgegenstand:** Gefahrstoffe Chemikalien Ausgangsstoffe. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Gefahrstoffe Chemikalien Ausgangsstoffe** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 3. `hygiene-pandemie-infektionsschutz`

**Fokus:** Hygiene Pandemie Infektionsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht.

# Hygiene Pandemie Infektionsschutz

## Fachkern: Hygiene Pandemie Infektionsschutz
- **Spezialgegenstand:** Hygiene Pandemie Infektionsschutz. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Hygiene Pandemie Infektionsschutz** im Bereich **Apothekenrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
