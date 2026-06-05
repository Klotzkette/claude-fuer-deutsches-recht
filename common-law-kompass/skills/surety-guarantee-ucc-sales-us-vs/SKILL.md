---
name: surety-guarantee-ucc-sales-us-vs
description: "Surety Guarantee UCC Sales US VS: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Surety Guarantee UCC Sales US VS

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Surety Guarantee UCC Sales US VS** im Plugin Common Law Kompass. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `common-law-surety-guarantee-indemnity` | Anwalt prüft Sicherheitenklausel und muss zwischen Buergschaft Garantie suretyship guarantee indemnity primary obligation accessory liability unterscheiden. Prüfraster Klausel-Typ-Identifikation Akzessorietaet Durchsetzbarkeit Regress. Output Sicherheiten-Klassifikation Risikomatrix Klausel-Empfehlung. Abgrenzung zu common-law-representations-warranties-covenants (Vertragsklauseln) und common-law-remedies-damages-equity (Rechtsfolgen). |
| `common-law-ucc-sales-goods` | Anwalt prüft Warenkaufvertrag nach UCC oder Sale of Goods Act: title risk warranties perfect tender remedies. Anwendungsfall US-Kaufvertrag oder UK-Warengeschäft. Prüfraster UCC Art. 2 Sale-of-Goods-Act-Prüfung Title-Risk-Transfer Warranty-Typen Perfect-Tender-Rule. Output Kaufvertrags-Analyse Risikomatrix Empfehlungen. Abgrenzung zu common-law-contract-formation-consideration (Allgemein) und common-law-representations-warranties-covenants (Klauseln). |
| `common-law-us-vs-uk-drafting` | Anwalt muss zwischen British English English Law US contract style Delaware/New York-Konventionen und Business-English unterscheiden. Anwendungsfall Vertrag für UK- oder US-Gegenpartei. Prüfraster Jurisdiction-Style-Matching Drafting-Konventionen Sprachebene. Output Drafting-Empfehlung Stil-Hinweise Klausel-Beispiele. Abgrenzung zu common-law-false-friends-scanner (Begriffe) und common-law-governing-law-jurisdiction (Rechtswahl). |

## Arbeitsweg

Im Plugin Common Law Kompass gilt für **Surety Guarantee UCC Sales US VS**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `common-law-surety-guarantee-indemnity`

**Fokus:** Anwalt prüft Sicherheitenklausel und muss zwischen Buergschaft Garantie suretyship guarantee indemnity primary obligation accessory liability unterscheiden. Prüfraster Klausel-Typ-Identifikation Akzessorietaet Durchsetzbarkeit Regress. Output Sicherheiten-Klassifikation Risikomatrix Klausel-Empfehlung. Abgrenzung zu common-law-representations-warranties-covenants (Vertragsklauseln) und common-law-remedies-damages-equity (Rechtsfolgen).

# Surety, Guarantee und Indemnity

## Zweck

Akzessorische Sicherheit, selbständige Zahlungspflicht, indemnity und support letter werden getrennt.

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
1. Is it a guarantee (secondary obligation — only liability if principal fails) or indemnity (primary, independent obligation)?
2. UK or US context — different rules on writing requirements and discharge?
3. Is the guarantee being altered/discharged by variation of principal debt?

## Key Case Law

- **Holme v Brunskill** (1878) 3 QBD 495 (CA) — Guarantee discharge by material variation: any variation in principal contract without guarantor's consent discharges guarantor unless variation is evidently insubstantial or beneficial.
- **Moschi v Lep Air Services** [1973] AC 331 (HL) — Distinction guarantee/indemnity: indemnor is primarily liable independent of principal; guarantor liable only if principal defaults; indemnity survives variation of principal contract.
- **Trafalgar House v General Surety** [1996] AC 199 (HL) — Demand guarantee: on-demand bonds are payable on demand without proof of default; court will not inquire into underlying dispute.
- **Marubeni Hong Kong v Mongolian Government** [2005] 1 WLR 2497 (CA) — State guarantee interpretation: same principles as commercial; clear words needed to override Holme v Brunskill rule for state guarantees.

## Normen und Quellen

- **UK:** Statute of Frauds 1677 s 4 (guarantee in writing); Misrepresentation Act 1967
- **US:** UCC § 3-419 (accommodation party); Restatement (Third) Suretyship and Guaranty (1996)
- Andrews & Millett, Law of Guarantees (8th ed. 2020)

## Output Template: Guarantee / Indemnity Classification

```
GUARANTEE / INDEMNITY REVIEW
Date: [DATE] — Instrument: [DESCRIPTION]
Jurisdiction: [England/Wales / New York]

1. CLASSIFICATION
 [ ] Guarantee: secondary liability; principal must default first
 [ ] On-demand bond: payable on demand; no proof of default required
 [ ] Indemnity: primary independent liability; variation does not discharge

2. FORMAL REQUIREMENTS
 UK: Writing under Statute of Frauds 1677 s 4: [YES — signed / NO — invalid]
 US: Statute of Frauds applicable state: [YES / NO]

3. DISCHARGE RISKS (Holme v Brunskill)
 Material variation without consent: [YES — RISK / NO]
 Extension of time to principal: [YES — RISK if no reservation of rights / NO]
 Release of co-guarantor: [YES — RISK / NO]
 Reservation of rights clause present: [YES / NO — ADD]

4. DEMAND REQUIREMENTS
 Notice required: [YES — [X] business days / NO — on demand]
 Conforming demand: [documentary requirements met?]

5. RECOMMENDED ACTION
[...]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `common-law-ucc-sales-goods`

**Fokus:** Anwalt prüft Warenkaufvertrag nach UCC oder Sale of Goods Act: title risk warranties perfect tender remedies. Anwendungsfall US-Kaufvertrag oder UK-Warengeschäft. Prüfraster UCC Art. 2 Sale-of-Goods-Act-Prüfung Title-Risk-Transfer Warranty-Typen Perfect-Tender-Rule. Output Kaufvertrags-Analyse Risikomatrix Empfehlungen. Abgrenzung zu common-law-contract-formation-consideration (Allgemein) und common-law-representations-warranties-covenants (Klauseln).

# UCC und Sale of Goods

## Zweck

Title, risk, acceptance, rejection, implied warranties und battle of forms werden rechtsordnungsspezifisch geprüft.

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
1. Which US state — UCC Article 2 applies but states may vary; NY has followed UCC closely.
2. Are both parties merchants (stricter rules apply under UCC § 2-207 battle of forms)?
3. Is there a warranty disclaimer — conspicuousness requirement under UCC § 2-316?
4. Has there been an anticipatory repudiation — UCC § 2-610 adequate assurance?

## Key Case Law

- **Frigaliment Importing v BNS International Sales** 190 F Supp 116 (SDNY 1960) — Classic UCC interpretation: meaning of "chicken" — extrinsic evidence, trade usage, course of dealing; subjective intent insufficient.
- **Nanakuli Paving v Shell Oil** 664 F 2d 772 (9th Cir 1981) — Course of performance and trade usage as part of UCC contract; express term may be displaced by established trade practice.
- **ProCD v Zeidenberg** 86 F 3d 1447 (7th Cir 1996) — Shrinkwrap licenses valid under UCC; acceptance by conduct after opportunity to read; rolling contract theory.
- **Jacob & Youngs v Kent** 230 NY 239 (1921) — Substantial performance doctrine (NY): deviation from specification in good faith entitles contractor to contract price minus diminution in value (not cost of completion if grossly disproportionate).

## Normen und Quellen

- **UCC Article 2** (Sale of Goods) — adopted in all US states except Louisiana (civil law)
- **CISG** (Vienna Convention 1980) — for international sales between CISG contracting states; may be displaced by UCC if US domestic
- White, Summers, Hillman, Uniform Commercial Code (6th ed. 2012)
- Farnsworth, Contracts (4th ed. 2004)

## Output Template: UCC Sales Contract Checklist

**Addressee:** Deal team or client
**Tone:** US-commercial; plain English

```
UCC ARTICLE 2 SALES CONTRACT CHECKLIST
Date: [DATE] — Goods: [DESCRIPTION] — State: [STATE]

1. FORMATION
 Both parties merchants?: [YES / NO — special rules apply]
 Battle of forms (§ 2-207): [YES — terms differ / NO]
 Outcome: [last-shot rule / knockout rule / ...]

2. WARRANTIES
 Express warranty (§ 2-313): [YES — basis of bargain: ...]
 Implied warranty merchantability (§ 2-314): [YES / DISCLAIMED conspicuously]
 Implied fitness (§ 2-315): [YES — seller knew purpose / DISCLAIMED]
 Disclaimer conspicuous (§ 2-316): [YES — caps, bold / NO — RISK]

3. RISK OF LOSS
 Shipment contract (F.O.B. origin): risk passes on delivery to carrier
 Destination contract (F.O.B. destination): risk passes on tender at destination
 Current clause: [VERBATIM] — classification: [shipment / destination]

4. REMEDIES (Buyer)
 Cover (§ 2-712): buy substitute; recover difference
 Market price damages (§ 2-713): contract price minus market price at breach
 Specific performance (§ 2-716): unique goods or other proper circumstances
 Rejection (§ 2-601): perfect tender rule — any non-conformity allows rejection
 Revocation of acceptance (§ 2-608): substantial impairment after acceptance

5. CISG APPLICABLE?
 Both parties in CISG states?: [YES — CISG governs unless excluded / NO]
 Exclusion clause: [present / NOT present — add Art. 6 CISG opt-out]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `common-law-us-vs-uk-drafting`

**Fokus:** Anwalt muss zwischen British English English Law US contract style Delaware/New York-Konventionen und Business-English unterscheiden. Anwendungsfall Vertrag für UK- oder US-Gegenpartei. Prüfraster Jurisdiction-Style-Matching Drafting-Konventionen Sprachebene. Output Drafting-Empfehlung Stil-Hinweise Klausel-Beispiele. Abgrenzung zu common-law-false-friends-scanner (Begriffe) und common-law-governing-law-jurisdiction (Rechtswahl).

# UK vs US Drafting

## Zweck

Mischenglisch aus Schulenglisch, US-Templates und Londoner Klauseln wird geglättet.

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

## Triage vor UK-vs-US-Drafting-Analyse

Kläre vor der Vergleichsanalyse:

1. Liegt ein Dokument vor, das gemischt UK/US-Stil aufweist, oder soll ein neues sauber in einer Tradition entworfen werden?
2. Governing Law: English law (London), New York, Delaware, oder anderer US-Staat?
3. Vertragstyp: SPA, Darlehensvertrag, Services Agreement, IP-Lizenz, JV-Agreement?
4. Counterparty-Erwartung: US-Firm oder Magic-Circle-UK-Firm? (Das praegt Styleerwartungen stark.)
5. Welche Klauseln wurden bereits als problematisch identifiziert?

## Key Case Law — Interpretation UK vs US

- *Arnold v Britton* [2015] UKSC 36, [2015] AC 1619 — UK Supreme Court betont: klarer Vertragswortlaut schlaegt kontextuelle Auslegung; englisches Recht tendiert zu wortgetreuer Auslegung bei gut gedrafteten Texten.
- *Investors Compensation Scheme v West Bromwich* [1998] 1 WLR 896 (HL) — Lord Hoffmann: Kontext und Hintergrundwissen beeinflussen Bedeutung; englische Auslegung ist kontextuell, aber nicht rewriting.
- *Frigaliment Importing Co v BNS International Sales Corp* 190 F Supp 116 (SDNY 1960) — US-Klassiker zu Vertragsauslegung ("What is chicken?"): Trade usage, course of dealing und course of performance als Auslegungsquellen nach UCC.
- *Pacific Gas & Electric Co v GW Thomas Drayage* 69 Cal 2d 33 (Cal 1968) — US (California) Parol Evidence Rule: extrinsic evidence grundsaetzlich zulaessig zur Klaerung von Ambiguities — ein fundamentaler Unterschied zu klassischer englischer plain-meaning-Auslegung.

## UK vs US Drafting-Vergleichsmatrix

| Punkt | England & Wales | New York / Delaware | Deutsches Fallbeil-Risiko |
|---|---|---|---|
| Consideration | Erforderlich; past consideration ungueltig | Erforderlich; "valuable consideration" reicht | Fehler: deutschen Synallagma-Begriff anwenden |
| Conditions vs Warranties | Condition: Ruecktritt; Warranty: Schadensersatz | Rep & Warranty: oft zusammen, survival-Klausel entscheidend | Warranty als "Garantie i.S.v. § 443 BGB" fehldeuten |
| Indemnity | Verschuldensunabhaengig, enger Wortlaut | Verschuldensunabhaengig; NY: Anti-Indemnity-Statutes beachten | Als Schadensersatz i.S.v. § 249 BGB behandeln |
| Material Adverse Change | Court-sceptisch (Akorn v Fresenius - Delaware) | MAC-Trigger schwer auszuloesen; hohe Schwelle | MAC als Force-Majeure-Ersatz missverstehen |
| Entire Agreement Clause | Sperrt nur collateral warranties, nicht statutory misrep | Merger Clause sperrt Parol Evidence breiter | Als vollstaendigen Haftungsausschluss ueberschaetzen |
| Good Faith | Kein allgemeiner implied duty (Walford v Miles) | UCC § 1-304: duty of good faith bei UCC-Vertraegen | BGB-Treu-und-Glauben-Mastab anlegen |
| Limitation of Liability | UCTA reasonableness test | NY: Generally enforceable, aber gross negligence nicht ausschliessbar | Cap zu hoch oder zu niedrig ansetzen |
| Notice Provisions | Strict compliance gefordert | Substantial compliance oft ausreichend | Notice-Fristen als Formsache behandeln |

## Normen und Quellen

**UK**
- Sale of Goods Act 1979 ss 12-15 — implied terms conditions/warranties
- UCTA 1977 ss 2, 3, 11 — limits on exclusion clauses
- Misrepresentation Act 1967 — rep-Haftung neben Vertragsrecht
- Companies Act 2006 ss 39-41 — corporate capacity and authority

**US (New York / Delaware)**
- UCC Art. 1 (§ 1-304 good faith), Art. 2 (§§ 2-313 to 2-318 warranties)
- Restatement (Second) of Contracts §§ 201-203 (interpretation)
- DGCL § 102(b)(7) — limitation of director liability
- NY GOL § 5-1401 — NY choice of law enforceability

**Kommentar**
- McKendrick, *Contract Law*, 14th ed. 2021 (UK) — Standardlehrbuch
- Farnsworth, *Farnsworth on Contracts*, 3rd ed. 2004 (US) — Standardwerk

## Output-Template: UK-vs-US-Vergleichsmemo

**Adressat:** Partnerebene oder Mandant — **Tonfall:** praezise, tabellarisch, handlungsorientiert

```
UK VS US DRAFTING — VERGLEICHSMEMO
Datum: [DATUM]
Dokument: [VERTRAGSNAME]
Governing Law (aktuell): [...]
Ziel-Jurisdiktion (nach Anpassung): [...]
Bearbeiter: [NAME]

ZUSAMMENFASSUNG
Das vorliegende Dokument ist [ueberwiegend UK / ueberwiegend US / gemischt] und weist
[X] Stellen auf, die jurisdiktionsfremde Elemente enthalten.

KRITISCHE UK/US-KONFLIKTE

Nr. | Klausel | Aktueller Text | Problem | Empfohlene Aenderung | Prioritaet
----|---------|---------------|---------|---------------------|----------
 1 | [§/Abs.] | "[Auszug]" | [UK/US-Konflikt] | "[Neuer Text]" | HOCH
 2 | ...

STYLE-ANPASSUNGEN (Nicht-kritisch)
- [Liste formaler Stilanpassungen: Datumsformat, defined terms, Nummerierung, ...]

JURISDICTION-SPEZIFISCHE CHECKLISTE
[ ] Consideration/past consideration geprueft (UK)
[ ] Deed vs Simple Contract: Formerfordernis geklaert
[ ] UCTA-Reasonableness-Test bestanden (UK)
[ ] UCC-Warranty-Disclaimer § 2-316 eingehalten (US)
[ ] MAC-Definition: Delaware-Standard beruecksichtigt (US-M&A)
[ ] Walford v Miles: No good-faith-obligation clause beachtet (UK)

LOCAL-COUNSEL-EMPFEHLUNG: [Ja / Nein / Fuer Teilbereiche]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
