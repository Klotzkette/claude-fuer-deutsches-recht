---
name: remedies-damages-representations-warranties
description: "Remedies Damages Representations Warranties: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Remedies Damages Representations Warranties

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Remedies Damages Representations Warranties** im Plugin Common Law Kompass. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `common-law-remedies-damages-equity` | Mandant erleidet Schaden aus UK/US-Vertrag oder Delikt und fragt nach Rechtsfolgen: damages specific performance injunction rescission restitution equitable relief punitive damages. Prüfraster Remedy-Auswahl Schadensmass Equity-Voraussetzungen Enforcement. Output Remedy-Analyse Schadensberechnung Klage-Strategie. Abgrenzung zu common-law-contract-formation-consideration (Vertragsschluss) und common-law-litigation-discovery (Prozess). |
| `common-law-representations-warranties-covenants` | Anwalt ordnet Klauseln in Common-Law-Transaktionsvertraegen ein: reps warranties covenants conditions undertakings indemnities. Anwendungsfall SPA NDA oder Commercial Agreement. Prüfraster Klausel-Typ-Zuordnung Haftungsfolgen Survical-Period Breach-Remedies. Output Klausel-Klassifikation Risikomatrix. Abgrenzung zu common-law-ma-commercial-drafting (Drafting) und common-law-surety-guarantee-indemnity (Sicherheiten). |
| `common-law-simulation-negotiation` | Anwalt oder Mandant will UK/US-Vertragsverhandlung oder Mandantengespraech simulieren und False-Friends-Lernkurve absolvieren. Prüfraster Verhandlungs-Simulation Issue-List-Erstellung Mandanten-Erklärung. Output Simulations-Szenario Verhandlungs-Script Lern-Feedback. Abgrenzung zu common-law-quality-gate (Qualitaet) und common-law-client-explainer (Erklärung). |

## Arbeitsweg

Im Plugin Common Law Kompass gilt für **Remedies Damages Representations Warranties**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `common-law-remedies-damages-equity`

**Fokus:** Mandant erleidet Schaden aus UK/US-Vertrag oder Delikt und fragt nach Rechtsfolgen: damages specific performance injunction rescission restitution equitable relief punitive damages. Prüfraster Remedy-Auswahl Schadensmass Equity-Voraussetzungen Enforcement. Output Remedy-Analyse Schadensberechnung Klage-Strategie. Abgrenzung zu common-law-contract-formation-consideration (Vertragsschluss) und common-law-litigation-discovery (Prozess).

# Remedies, Damages und Equity

## Zweck

Schadenskategorien, equitable relief, caps, carve-outs und indemnities werden nicht in deutsches Schadensersatzschema gepresst.

## Wann verwenden

- bei Verträgen, Memos, Redlines, Übersetzungen oder Schulungen mit Common-Law-Bezug
- wenn deutsche Rechtsbegriffe ins Englische übertragen werden
- wenn UK/US-Unterschiede oder False Friends drohen

## Arbeitsweise

1. **Jurisdiktion fixieren.** Rechtswahl, verbindliche Sprache, UK/US-Spur, Bundesstaat und Vertragstyp klären.
2. **Begriff funktional prüfen.** Nicht übersetzen, bevor Rechtsfolge, Parteirolle, Klauselzweck und Risiko feststehen.
3. **False Friends markieren.** Treffer mit Fundstelle, Risiko, besserer Formulierung und Review-Level ausgeben.
4. **Ton steuern.** Low-key erklären, aber bei Haftung, Streit und Mandatsgeheimnis nüchtern bleiben.
5. **Qualitätstor setzen.** Quellenstand, offene Annahmen, Local-Counsel-Bedarf und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Bürgschaft, guarantee, suretyship und indemnity nicht gleichsetzen.
- Consideration nicht als deutsche Gegenleistung behandeln.
- UK, USA, New York, Delaware und UCC nicht vermischen.
- Keine erfundenen Fälle oder Quellen verwenden.

## Ton

Common-Law-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage

Before proceeding, clarify:
1. Is the claim for breach of contract (expectation/reliance damages) or tort (compensatory/punitive)?
2. Is equitable relief sought — injunction, specific performance, rescission, account of profits?
3. Has the claimant mitigated loss?
4. Is remoteness / foreseeability an issue (Hadley v Baxendale line)?

## Key Case Law

- **Hadley v Baxendale** (1854) 9 Exch 341 — Two limbs of remoteness: (1) naturally arising damages; (2) special circumstances communicated at time of contract; standard foreseeability test in contract.
- **Robinson v Harman** (1848) 1 Exch 850 — Expectation measure: put the claimant in the position as if the contract had been performed.
- **Victoria Laundry v Newman Industries** [1949] 2 KB 528 (CA) — Reasonable foreseeability of type of loss; special profits only if communicated.
- **The Achilleas** [2008] UKHL 48, [2009] 1 AC 61 — Departure from Hadley: if parties intended loss to fall outside assumption of responsibility, no recovery even if foreseeable.
- **American Cyanamid v Ethicon** [1975] AC 396 (HL) — Injunction (interlocutory): (1) serious issue to be tried; (2) damages not adequate remedy; (3) balance of convenience.

## Normen und Quellen

- **UK:** Misrepresentation Act 1967 s 2; Sale of Goods Act 1979 ss 51-54; Senior Courts Act 1981 s 37 (injunctions)
- **US:** UCC § 2-711 to 2-715 (buyer's remedies); Restatement (Second) Contracts § 344-385
- McGregor on Damages (21st ed. 2021) — standard UK damages reference
- Farnsworth, Contracts (4th ed. 2004) — standard US reference

## Output Template: Damages Assessment Memo

**Addressee:** Client
**Tone:** Commercially focused; quantified where possible

```
DAMAGES ASSESSMENT MEMO
Date: [DATE] — Matter: [DESCRIPTION]
Jurisdiction: [England/Wales / New York]

1. MEASURE OF DAMAGES
 [ ] Expectation (put in position as if performed) — Est. value: GBP/USD [X]
 [ ] Reliance (expenses wasted in reliance on contract)
 [ ] Restitution (unjust enrichment; quantum meruit)
 [ ] Wasted expenditure

2. HEADS OF LOSS
 a. Direct loss: GBP/USD [X]
 b. Consequential loss (foreseeable?): [YES — Hadley limb 2 / NO]
 c. Loss of profit: [Recoverable if communicated: ...]
 d. Non-pecuniary / distress: [Limited in commercial contracts]

3. REMOTENESS
 Hadley v Baxendale test: [limb 1 / limb 2 — communicated?]
 Achilleas assumption of responsibility: [relevant / not relevant]

4. MITIGATION
 Claimant mitigated?: [YES / NO — steps taken: ...]
 Deduction for failure to mitigate: [est. GBP/USD X]

5. EQUITABLE RELIEF AVAILABLE?
 [ ] Injunction — American Cyanamid test: [serious issue / damages inadequate / balance of convenience]
 [ ] Specific performance — unique goods/property: [YES / NO]
 [ ] Account of profits — breach fiduciary duty: [applicable / not]

6. TOTAL ESTIMATED RECOVERY
 Low: GBP/USD [X] — High: GBP/USD [Y]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `common-law-representations-warranties-covenants`

**Fokus:** Anwalt ordnet Klauseln in Common-Law-Transaktionsvertraegen ein: reps warranties covenants conditions undertakings indemnities. Anwendungsfall SPA NDA oder Commercial Agreement. Prüfraster Klausel-Typ-Zuordnung Haftungsfolgen Survical-Period Breach-Remedies. Output Klausel-Klassifikation Risikomatrix. Abgrenzung zu common-law-ma-commercial-drafting (Drafting) und common-law-surety-guarantee-indemnity (Sicherheiten).

# Representations, Warranties und Covenants

## Zweck

M&A- und Commercial-Verträge werden nach Aussage, Zusicherung, Pflicht, Bedingung, Freistellung und Remedy zerlegt.

## Wann verwenden

- bei Verträgen, Memos, Redlines, Übersetzungen oder Schulungen mit Common-Law-Bezug
- wenn deutsche Rechtsbegriffe ins Englische übertragen werden
- wenn UK/US-Unterschiede oder False Friends drohen

## Arbeitsweise

1. **Jurisdiktion fixieren.** Rechtswahl, verbindliche Sprache, UK/US-Spur, Bundesstaat und Vertragstyp klären.
2. **Begriff funktional prüfen.** Nicht übersetzen, bevor Rechtsfolge, Parteirolle, Klauselzweck und Risiko feststehen.
3. **False Friends markieren.** Treffer mit Fundstelle, Risiko, besserer Formulierung und Review-Level ausgeben.
4. **Ton steuern.** Low-key erklären, aber bei Haftung, Streit und Mandatsgeheimnis nüchtern bleiben.
5. **Qualitätstor setzen.** Quellenstand, offene Annahmen, Local-Counsel-Bedarf und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Bürgschaft, guarantee, suretyship und indemnity nicht gleichsetzen.
- Consideration nicht als deutsche Gegenleistung behandeln.
- UK, USA, New York, Delaware und UCC nicht vermischen.
- Keine erfundenen Fälle oder Quellen verwenden.

## Ton

Common-Law-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage

Before proceeding, clarify:
1. Is this an M&A context (SPA reps/warranties/indemnities) or a commercial contract?
2. UK or US — fundamental difference in remedy for breach of warranty (UK: damages only) vs. US (varies by state)?
3. Is there a disclosure letter limiting warranty liability (UK SPA practice)?
4. Is there a limitation clause (basket, cap, time limit)?

## Key Case Law

- **Esso Petroleum v Mardon** [1976] QB 801 (CA) — Misrepresentation: pre-contractual representation becoming warranty requires: accuracy of information, reliance, negligence; damages under s 2(1) Misrepresentation Act 1967 as alternative to rescission.
- **Thomas Witter v TBP Industries** [1996] 2 All ER 573 — Entire agreement clauses do not automatically exclude liability for misrepresentation; explicit non-reliance wording required.
- **CBS Songs v Amstrad** [1988] AC 1013 (HL) — Covenant not to do something is absolute; a warranty is a statement of fact at time of contract; covenants run through time.
- **Hooper v Oates** [2013] EWCA Civ 91 — Representations in SPAs: precise language matters; "knowledge qualifier" reduces warranty scope significantly.

## Normen und Quellen

- **UK:** Misrepresentation Act 1967; Consumer Rights Act 2015 (implied warranties B2C); Sale of Goods Act 1979 s 12-15
- **US:** UCC § 2-312 to 2-315 (express/implied warranties); Restatement (Second) Contracts § 259-264 (covenants)
- Sinclair, Warranties and Indemnities on Share and Asset Sales (11th ed. 2022)
- Model M&A contract (ABA) — US SPA drafting reference

## Output Template: Reps/Warranties/Covenants Matrix

**Addressee:** Negotiation counterparty or internal deal team
**Tone:** Deal-practical; risk-flagging

```
REPS / WARRANTIES / COVENANTS MATRIX
Date: [DATE] — Deal: [DESCRIPTION]
Jurisdiction: [England/Wales / New York / Delaware]

No. | Type | Clause | Risk | Rec.
----|------|--------|------|-----
1 | Rep. | "[verbatim]" | [HIGH — no knowledge qualifier] | Add "to Seller's knowledge"
2 | Warranty | "[verbatim]" | [MEDIUM — broad; cap?] | Add basket EUR/GBP [X]; cap [Y]
3 | Covenant | "[verbatim]" | [LOW — time-limited 2 years] | OK
4 | Indemnity | "[verbatim]" | [HIGH — uncapped tax indemnity] | Cap at transaction value

GLOBAL ISSUES:
- Limitation period: [UK: 7 years from Completion / US: 18 months typical]
- Basket (de minimis): [EUR/GBP X — tipping or non-tipping?]
- Cap: [EUR/GBP X / % of purchase price]
- Disclosure letter: [comprehensive / not prepared yet]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `common-law-simulation-negotiation`

**Fokus:** Anwalt oder Mandant will UK/US-Vertragsverhandlung oder Mandantengespraech simulieren und False-Friends-Lernkurve absolvieren. Prüfraster Verhandlungs-Simulation Issue-List-Erstellung Mandanten-Erklärung. Output Simulations-Szenario Verhandlungs-Script Lern-Feedback. Abgrenzung zu common-law-quality-gate (Qualitaet) und common-law-client-explainer (Erklärung).

# Simulation und Verhandlungstraining

## Zweck

Fiktive Verhandlungsrunden trainieren junge Anwältinnen und Anwälte mit klar markierten Simulationsunterlagen.

## Wann verwenden

- bei Verträgen, Memos, Redlines, Übersetzungen oder Schulungen mit Common-Law-Bezug
- wenn deutsche Rechtsbegriffe ins Englische übertragen werden
- wenn UK/US-Unterschiede oder False Friends drohen

## Arbeitsweise

1. **Jurisdiktion fixieren.** Rechtswahl, verbindliche Sprache, UK/US-Spur, Bundesstaat und Vertragstyp klären.
2. **Begriff funktional prüfen.** Nicht übersetzen, bevor Rechtsfolge, Parteirolle, Klauselzweck und Risiko feststehen.
3. **False Friends markieren.** Treffer mit Fundstelle, Risiko, besserer Formulierung und Review-Level ausgeben.
4. **Ton steuern.** Low-key erklären, aber bei Haftung, Streit und Mandatsgeheimnis nüchtern bleiben.
5. **Qualitätstor setzen.** Quellenstand, offene Annahmen, Local-Counsel-Bedarf und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Bürgschaft, guarantee, suretyship und indemnity nicht gleichsetzen.
- Consideration nicht als deutsche Gegenleistung behandeln.
- UK, USA, New York, Delaware und UCC nicht vermischen.
- Keine erfundenen Fälle oder Quellen verwenden.

## Ton

Common-Law-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage vor Verhandlungssimulation

Kläre vor dem Training:

1. Reale oder fiktive Verhandlung — sollen echte Mandantendaten verwendet werden?
2. Welche Partei spielt der Trainee — Käufer, Verkäufer, Kreditgeber, Target?
3. Erfahrungsniveau: Erstes Jahr, Mittelstufe, Senior Associate?
4. Welche Schlüsselklauseln sind Gegenstand der Simulation (MAC, Indemnity, Reps & Warranties, Pricing)?
5. Soll die Simulation auf englisches Recht, New York Law oder einen hybriden Kontext ausgerichtet sein?

## Key Case Law — Verhandlung und Good Faith

- *Walford v Miles* [1992] 2 AC 128 (HL) — kein implied duty to negotiate in good faith im englischen Recht; Pre-Contractual-Verhandlungen binden grundsaetzlich nicht, Lock-Out-Agreements ohne bestimmbare Laufzeit sind nichtig — ein fundamentaler Unterschied zu § 311 II BGB.
- *Petromec Inc v Petroleo Brasileiro SA* [2005] EWCA Civ 891 — begrenzte Ausnahme: express duty of good faith in einem Teilvertrag kann bindend sein; wichtig fuer Trainingsszenarien mit NDA + Term Sheet.
- *Pitt v PHH Asset Management Ltd* [1994] 1 WLR 327 (CA) — Lock-Out-Agreement mit bestimmter Laufzeit ist wirksam und durchsetzbar; zeigt Gestaltungsalternative zu Good-Faith-Klauseln.
- *BCCI SA v Ali* [2001] UKHL 8 — weite Releases in Vergleichsverhandlungen; Parteien muessen klar und deutlich formulieren, wenn sie unbekannte Claims freigeben wollen — Lehrfall fuer Settlement-Training.

## Normen und Quellen — Verhandlungsrecht

**UK**
- Contract (Rights of Third Parties) Act 1999 — Drittbegünstigte in Verhandlungsszenarien
- Misrepresentation Act 1967 — vorvertragliche Falschangaben im Verhandlungsverlauf
- Civil Evidence Act 1995 — admissibility von Without-Prejudice-Kommunikation

**US**
- Restatement (Second) of Contracts §§ 161-164 — Misrepresentation in Negotiations
- UCC § 1-304 — obligation of good faith (bei UCC-Vertraegen, anders als Common Law)
- FRCP Rule 408 — settlement communications (Beweis-Ausschluss)

**Praxis**
- Fisher/Ury/Patton, *Getting to Yes*, 3rd ed. 2011 — BATNA-Konzept
- Mnookin/Peppet/Tulumello, *Beyond Winning*, 2000 — Lawyer-as-Negotiator

## Simulationsszenarien — Uebersicht

| Szenario | Governing Law | Knackpunkt | Typischer Trainee-Fehler |
|---|---|---|---|
| SPA-Verhandlung (Tech-M&A) | English Law | MAC-Definition, Locked-Box vs Completion Accounts | MAC zu eng definieren |
| NDA-Verhandlung | New York Law | Definition of Confidential Information, Residuals | "Residuals-Klausel" nicht bemerken |
| Kreditvertrag | English Law (LMA) | Financial Covenants, Cure Rights | Equity Cure nicht verhandeln |
| Settlement Agreement | English Law | Release-Breite, BCCI-Risiko | Unbekannte Claims freisetzen |
| JV-Term Sheet | DE + English Law | Good-Faith-Pflicht vs. Walford v Miles | BGB-Standard auf englischen Vertrag anwenden |

## Output-Template: Simulationsprotokoll

**Adressat:** Trainer / Supervisorin — **Tonfall:** strukturiert, lernorientiert

```
VERHANDLUNGSSIMULATION — PROTOKOLL
Datum: [DATUM]
Szenario: [BEZEICHNUNG]
Trainee: [NAME / ANONYMISIERT]
Partei: [KAEUFER / VERKAEUFER / ...]
Governing Law: [RECHTSORDNUNG]

ERGEBNIS DER SIMULATION
Einigungspunkte: [...]
Offene Punkte: [...]
Erreichtes BATNA-Ergebnis: [BESSER / SCHLECHTER / EINIGUNG]

BEOBACHTUNGEN
Staerken: [...]
Entwicklungsbereiche: [...]

FALSE-FRIENDS-VORFAELLE
- [Begriff] wurde falsch verwendet: [Beschreibung] — Korrekt: [...]

JURISTISCHE FEHLER
- [Punkt] — Richtige Regel: [Kurz] — Fundstelle: [...]

FEEDBACK-GESPRAECH
Kernbotschaft: [1-2 Saetze]
Naechster Uebungsschritt: [...]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
