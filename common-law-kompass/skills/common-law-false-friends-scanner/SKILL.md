---
name: common-law-false-friends-scanner
description: "Anwalt oder Uebersetzer sucht missverstaendliche deutsch-englische Rechtsbegriffe im Vertragstext oder Memo. Anwendungsfall Vertragsentwurf mit False-Friend-Risiko. Pruefraster Begriff-Scan Risikoeinstufung sichere Alternativen Jurisdiktion-Check. Output False-Friends-Liste Korrekturvorschlaege sichere Formulierungen. Abgrenzung zu common-law-begriffe-uebersetzung (Uebersetzung) und common-law-bilingual-contract-review (Vergleich)."
---

# False-Friends-Scanner

## Zweck

Bürgschaft, Garantie, Gewährleistung, Rücktritt, Vertretung, Schadensersatz, Eigentum, Besitz, Kündigung, Verzug und ähnliche Begriffe werden funktional statt wörtlich geprüft.

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
1   | [guarantee] | Clause 5.2 | HIGH — no discharge clause | Add: "primary indemnity" or add Holme v Brunskill waiver
2   | [good faith] | Clause 8 | HIGH — unenforceable English law | Remove or replace with specific obligations
3   | [condition] | Clause 3 | MEDIUM — correct usage but confirm | Confirm classification intended
```
