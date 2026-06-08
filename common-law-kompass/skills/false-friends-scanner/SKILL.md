---
name: false-friends-scanner
description: "Anwalt oder Übersetzer sucht missverstaendliche deutsch-englische Rechtsbegriffe im Vertragstext oder Memo. Anwendungsfall Vertragsentwurf mit False-Friend-Risiko. Prüfraster Begriff-Scan Risikoeinstufung sichere Alternativen Jurisdiktion-Check. Output False-Friends-Liste Korrekturvorschlaege sichere Formulierungen. Abgrenzung zu common-law-begriffe-uebersetzung (Übersetzung) und common-law-bilingual-contract-review (Vergleich) im Common Law Kompass."
---

# False-Friends-Scanner

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

## Key False Friends

| English Term | German False Friend | Correct Reading | Risk |
|---|---|---|---|
| "guarantee" | Garantie (absolute) | often secondary obligation (needs principal default) | HIGH |
| "indemnity" | Entschaedigung / Buergschaft | primary independent obligation; survives variation | HIGH |
| "warranty" | Gewaehrleistung | not Ruecktrittsrecht; damages only | MEDIUM |
| "condition" | Bedingung (§ 158 BGB) | fundamental term; breach = right to terminate | HIGH |
| "innominate term" | unklar | intermediate term; remedy depends on gravity of breach | MEDIUM |
| "consideration" | Gegenleistung | legal concept requiring bargain; inadequacy acceptable | HIGH |
| "estoppel" | Verwirkung (partial) | different types; does not extinguish right but precludes denial | MEDIUM |
| "good faith" | Treu und Glauben | NOT implied in English commercial contracts | HIGH |
| "specific performance" | Erfuellungsklage | equitable; discretionary; not available as of right | MEDIUM |
| "discovery" | Akteneinsicht | much broader; both sides must produce relevant docs | HIGH |
| "deed" | Urkunde | has legal effect without consideration | MEDIUM |

## Key Case Law

- **Walford v Miles** [1992] 2 AC 128 (HL) — No general obligation of good faith in English contract law; lock-out / lock-in agreements need independent consideration.
- **Bunge v Tradax** [1981] 1 WLR 711 (HL) — Condition vs. warranty: classification of term determines remedy; time stipulations in commercial contracts often conditions.
- **Hong Kong Fir Shipping v Kawasaki** [1962] 2 QB 26 (CA) — Innominate terms: seaworthiness clause; breach consequences determine remedy (not classification).

## Triage

Before proceeding, clarify:
1. Which contract and which term needs scanning?
2. Is the client German — likely to import civil law concepts unintentionally?
3. Is the language of the document German or English (or bilingual)?

## Output Template: False Friends Scan Report

```
FALSE FRIENDS SCAN REPORT
Document: [DESCRIPTION] — Date: [DATE]

No. | Term Found | Location | Risk | Recommended Change
----|-----------|----------|------|-------------------
1 | [guarantee] | Clause 5.2 | HIGH — no discharge clause | Add: "primary indemnity" or add Holme v Brunskill waiver
2 | [good faith] | Clause 8 | HIGH — unenforceable English law | Remove or replace with specific obligations
3 | [condition] | Clause 3 | MEDIUM — correct usage but confirm | Confirm classification intended
```

