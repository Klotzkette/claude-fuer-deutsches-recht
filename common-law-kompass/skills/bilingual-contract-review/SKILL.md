---
name: bilingual-contract-review
description: "Anwalt prüft deutschen und englischen Vertragstext auf Bedeutungsdrift Rangfolge Definitionskonflikte Haftungsrisiken. Anwendungsfall bilingualer SPA NDA oder Lizenzvertrag. Prüfraster Bedeutungsdrift-Analyse Rangfolgen-Klausel Definitions-Konsistenz Haftungs-Delta. Output Vergleichs-Tabelle Risi..."
---

# Bilingual Contract Review

## Regelungs- und Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `UCC § 2-201` — Statute of Frauds für Warenkauf.
- `UCC § 2-313` — express warranties.
- `UCC § 2-314` — implied warranty of merchantability.
- `Restatement (Second) of Contracts § 17` — formation by bargain.
- `Restatement (Second) of Contracts § 71` — consideration.
- `Restatement (Second) of Contracts § 90` — promissory estoppel.
- `CISG Art. 14` — Angebot.
- `CISG Art. 18` — Annahme.
- `CISG Art. 25` — wesentliche Vertragsverletzung.
- `CISG Art. 35` — Vertragsmaessigkeit der Ware.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: England Limitation Act 1980 (6 Jahre Contract, 6 Jahre Tort), US-Statutes of Limitations einzelstaatlich (oft 3-6 Jahre), ICC-Schiedsverfahren Antwort 30 Tage.
- Tragende Normen verifizieren: Englisches Recht (Common Law / Equity), US-Recht (Restatements, UCC), Vergleich BGB-System, IPR-Anknüpfung (Rom I, Rom II), HCCH-Konventionen, New Yorker Übereinkommen (Schiedssprüche) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant mit US/UK-Bezug, Solicitor, Barrister, US-Attorney, deutscher Anwalt, Schiedsgericht (ICC, LCIA, ICDR), High Court, Court of Appeal.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Letter of Engagement, Statement of Claim / Particulars of Claim, Defence, Affidavit, Witness Statement, Discovery/Disclosure, Settlement Agreement — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Wann verwenden

- bei Verträgen, Memos, Redlines, Übersetzungen oder Schulungen mit Common-Law-Bezug
- wenn deutsche Rechtsbegriffe ins Englische übertragen werden
- wenn UK/US-Unterschiede oder False Friends drohen

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

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

- German "Allgemeine Geschäftsbedingungen" (AGB) provisions (§§ 305-310 BGB) do not apply under English law — "terms and conditions" not subject to AGB-Kontrolle.
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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 29 VwVfG
- Art. 267 AEUV
- § 31 BVerfGG
- § 4 EuRAG
- Art. 15 DSGVO

### Leitentscheidungen

- BGH XI ZR 39/04
