---
name: begriffe-uebersetzung-bilingual-contract
description: "Begriffe Uebersetzung Bilingual Contract: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Begriffe Uebersetzung Bilingual Contract

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Begriffe Uebersetzung Bilingual Contract** im Plugin Common Law Kompass. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `common-law-begriffe-uebersetzung` | Deutscher Anwalt uebersetzt Vertrags- oder Rechtsbegriffe ins Englische und will funktionale nicht wörtliche Übersetzung. Anwendungsfall Vertragsverhandlung mit UK/US-Gegenpartei Memo an englischsprachigen Mandanten. Prüfraster Zielrechtsordnung-Prüfung Klauselzweck Risiko-Aequivalent False-Friends-Check. Output uebersetzter Begriff mit Erklärung Alternativen. Abgrenzung zu common-law-false-friends-scanner (Fehler-Scan) und common-law-us-vs-uk-drafting (Drafting-Konventionen). |
| `common-law-bilingual-contract-review` | Anwalt prüft deutschen und englischen Vertragstext auf Bedeutungsdrift Rangfolge Definitionskonflikte Haftungsrisiken. Anwendungsfall bilingualer SPA NDA oder Lizenzvertrag. Prüfraster Bedeutungsdrift-Analyse Rangfolgen-Klausel Definitions-Konsistenz Haftungs-Delta. Output Vergleichs-Tabelle Risiko-Markierungen Korrekturvorschlaege. Abgrenzung zu common-law-false-friends-scanner (Begriffsebene) und common-law-ma-commercial-drafting (Drafting). |
| `common-law-client-explainer` | Mandant oder Business-Team versteht Common-Law-Konzepte nicht und braucht verstaendliche Erklärung. Anwendungsfall Deutsche kaufen UK-Unternehmen oder schließen US-Vertrag ab. Prüfraster Verstaendlichkeit Vollständigkeit Wesentliche-Punkte-Abdeckung Risiko-Klarheit. Output verstaendliches Erklärungsschreiben oder Memo für Mandanten. Abgrenzung zu common-law-begriffe-uebersetzung (Fachsprache) und common-law-humor-coach (Ton). |

## Arbeitsweg

Im Plugin Common Law Kompass gilt für **Begriffe Uebersetzung Bilingual Contract**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `common-law-begriffe-uebersetzung`

**Fokus:** Deutscher Anwalt uebersetzt Vertrags- oder Rechtsbegriffe ins Englische und will funktionale nicht wörtliche Übersetzung. Anwendungsfall Vertragsverhandlung mit UK/US-Gegenpartei Memo an englischsprachigen Mandanten. Prüfraster Zielrechtsordnung-Prüfung Klauselzweck Risiko-Aequivalent False-Friends-Check. Output uebersetzter Begriff mit Erklärung Alternativen. Abgrenzung zu common-law-false-friends-scanner (Fehler-Scan) und common-law-us-vs-uk-drafting (Drafting-Konventionen).

# Begriffs- und Übersetzungswerkstatt

## Zweck

Der Skill baut mandatsbezogene Glossare mit Do/Don't-Spalte und Formulierungen für deutsches Recht in englischer Sprache.

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

## Vertiefung: Kernbegriffe und Uebersetzungsfallen

| Englischer Begriff | Falsche dt. Uebersetzung | Richtige Einordnung | Fundstelle |
|---|---|---|---|
| Consideration | Gegenleistung | Verpflichtungselement; Bargain; kein Synallagma | Currie v Misa [1875] |
| Warranty | Garantie | Zusicharung im Vertrag; Verletzung = Schadensersatz (kein Ruecktritt) | SGA 1979 s 61 |
| Condition | Bedingung | Wesentliches Vertragselement; Verletzung = Kuendigung und Schadensersatz | Bunge v Tradax [1981] |
| Indemnity | Buergschaft | Primaere selbstaendige Haftung (kein Ausfallerfordernis) | Moschi v Lep [1973] |
| Guarantee | Garantie | Sekundaere Haftung; nur bei Ausfall des Hauptschuldners | Holme v Brunskill (1878) |
| Estoppel | Bestandskraft / Verwirkung | Rechtshinderungseinwand; verschiedene Arten (promissory, proprietary, common law) | Central London Property v High Trees [1947] |
| Tort | Delikt | Ausservertragliche Haftung; weiter als BGB-Deliktsrecht | Donoghue v Stevenson [1932] |
| Specific performance | Erfuellungsklage | Billigkeitsrechtsmittel; nur wenn Schadensersatz unzulaenglich; Ermessen | Co-op Insurance v Argyll [1997] |

## Key Case Law

- **Donoghue v Stevenson** [1932] AC 562 (HL) — Tort of negligence: duty of care; neighbour principle; manufacturer liable to ultimate consumer without privity.
- **Central London Property Trust v High Trees House** [1947] KB 130 — Promissory estoppel: promisor bound by promise relied upon; no consideration required for variation if reliance present.
- **Photo Production v Securicor Transport** [1980] AC 827 (HL) — Exclusion clauses and fundamental breach: no rule of law preventing exclusion of liability for fundamental breach; clear words suffice.

## Triage vor Uebersetzung

Bevor losgelegt wird, klaere:
1. In welchem Kontext steht der Begriff — Vertragsklausel, Schriftsatz, Mandantenmemo?
2. UK oder US Kontext — einige Begriffe divergieren erheblich.
3. Ist ein Rechtsbegriff gemeint oder ein umgangssprachlicher Begriff?

## Output-Template: Uebersetzungs-Matrix

```
UEBERSETZUNGSMATRIX COMMON LAW
Dokument: [BEZEICHNUNG] — Datum: [DATUM]

Begriff | Kontext | Empfohlene dt. Entsprechung | Risiko Fehluebers.
--------|---------|---------------------------|-------------------
[TERM] | [Klausel] | [ENTSPRECHUNG] | [RISIKO]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `common-law-bilingual-contract-review`

**Fokus:** Anwalt prüft deutschen und englischen Vertragstext auf Bedeutungsdrift Rangfolge Definitionskonflikte Haftungsrisiken. Anwendungsfall bilingualer SPA NDA oder Lizenzvertrag. Prüfraster Bedeutungsdrift-Analyse Rangfolgen-Klausel Definitions-Konsistenz Haftungs-Delta. Output Vergleichs-Tabelle Risiko-Markierungen Korrekturvorschlaege. Abgrenzung zu common-law-false-friends-scanner (Begriffsebene) und common-law-ma-commercial-drafting (Drafting).

# Bilingual Contract Review

## Zweck

Die Fassungen werden nicht Satz für Satz, sondern nach Rechtsfolge, Definitionsdrift und prevailing-language-Regel geprüft.

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
1. Which language is the controlling language — English or German (or both)?
2. Does the bilingual contract specify which version prevails in case of inconsistency?
3. Is there a CISG issue — German seller, English-law contract with English buyer?
4. Has the German-law influenced version introduced civil law concepts not recognized under English law?

## Key Case Law

- **Credit Suisse First Boston (Europe) v Seagate Trading** [1999] 1 Lloyd's Rep 784 — Bilingual contract interpretation: where two language versions conflict, the dominant language version prevails; "text agrees" approach only if both versions truly consistent.
- **Raiffeisen Zentralbank v Five Star General Trading** [2001] QB 825 (CA) — Choice of law in bilingual financial contracts: governing law clause controls even if German-influenced terms present; parties bound by English law consequences.

## Key Issues in German-English Contracts

- German "Allgemeine Geschaeftsbedingungen" (AGB) provisions (§§ 305-310 BGB) do not apply under English law — "terms and conditions" not subject to AGB-Kontrolle.
- English "entire agreement clause" does not incorporate Nebenabreden-Einschaenkungen of German law.
- German Treu und Glauben (§ 242 BGB) has no equivalent under English law — good faith obligation not implied in commercial contracts (Walford v Miles [1992] 2 AC 128 HL).

## Output Template: Bilingual Contract Review Memo

```
BILINGUAL CONTRACT REVIEW
Date: [DATE] — Contract: [DESCRIPTION]
Languages: English / German
Controlling language: [English / German / Both — per Clause X]

1. CONSISTENCY REVIEW
 Key term in English: [TERM] — German equivalent: [TERM]
 Divergence: [YES — describe / NO]
 Risk: [significant / minor]

2. CIVIL LAW CONCEPTS IN ENGLISH LAW CONTEXT
 AGB-Kontrolle terms imported: [YES — RISK: not applicable under English law / NO]
 Treu und Glauben implied obligation: [YES — RISK: not recognized English law / NO]
 German Ruecktrittsrecht imported: [YES — check termination provisions / NO]

3. CHOICE OF LAW / CISG
 Governing law: [English / German]
 CISG applicable?: [YES — opt out required? / NO]

4. CORRECTIONS RECOMMENDED
 [List of specific clause amendments]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `common-law-client-explainer`

**Fokus:** Mandant oder Business-Team versteht Common-Law-Konzepte nicht und braucht verstaendliche Erklärung. Anwendungsfall Deutsche kaufen UK-Unternehmen oder schließen US-Vertrag ab. Prüfraster Verstaendlichkeit Vollständigkeit Wesentliche-Punkte-Abdeckung Risiko-Klarheit. Output verstaendliches Erklärungsschreiben oder Memo für Mandanten. Abgrenzung zu common-law-begriffe-uebersetzung (Fachsprache) und common-law-humor-coach (Ton).

# Mandanten-Erklärer

## Zweck

Management und Business-Team bekommen klare Entscheidungspunkte statt Wörterbuchdogmatik.

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
1. Who is the client — German-headquartered company, individual, or in-house counsel?
2. What common law concept needs explaining — and at what depth?
3. Is English the client's working language — or does a German explanation parallel work better?

## Key Concepts to Explain (Common Questions)

- **Consideration:** "Every contract needs something exchanged — a promise for a promise, or a payment. Unlike German law, a bare promise with no 'bargain' is not enforceable (unless in a deed)."
- **Precedent (stare decisis):** "Courts are bound by higher court decisions on the same legal point. The Supreme Court decision in [X] sets the rule for all UK courts below."
- **Disclosure/Discovery:** "Unlike German/civil-law procedure, common law litigation requires both sides to produce relevant documents — even ones that hurt their case. Costs can be very high."
- **Equity:** "Alongside common law, English courts apply 'equity' — flexible rules developed by the old Court of Chancery. Injunctions, specific performance, and trusts are equitable remedies."

## Key Case Law (for explanation context)

- **Donoghue v Stevenson** [1932] AC 562 — Used to explain duty of care concept; neighbour principle.
- **Carlill v Carbolic Smoke Ball** [1893] 1 QB 256 — Used to explain offer/acceptance/consideration; familiar for students.

## Output Template: Client Explainer Memo

**Addressee:** German client unfamiliar with common law
**Tone:** Clear, non-jargon; German equivalents provided where helpful

```
CLIENT EXPLAINER: [COMMON LAW CONCEPT]
Date: [DATE] — Prepared for: [CLIENT NAME]
Jurisdiction: [England/Wales / New York]

WHAT IT MEANS
[Plain English explanation in 3-5 sentences]

GERMAN EQUIVALENT (OR WHY THERE ISN'T ONE)
[Comparison: similar to [§ X BGB] BUT differs in [KEY WAY]]

WHY IT MATTERS FOR YOUR SITUATION
[Practical impact: deal / litigation / compliance]

WHAT TO DO
[Action point]

FURTHER READING
[Accessible reference / summary source]
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
