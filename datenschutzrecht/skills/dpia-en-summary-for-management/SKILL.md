---
name: dpia-en-summary-for-management
description: "Concise English DPIA management summary aligned with Art. 35 GDPR for board executive committee or non-legal stakeholders. Output: one-pager covering processing necessity risk measures residual risk approval recommendation."
---

# DPIA Management Summary in English

## Purpose

Concise English-language management summary of a Data Protection Impact Assessment (DPIA) under Art. 35 GDPR. Designed for board members, executive committees, group risk officers and other non-legal stakeholders who require a defensible one-pager rather than the full DPIA document. The summary follows the six-step methodology and ends with an explicit approval recommendation.

## When to use

- When a DPIA is on the agenda of a board, executive committee or steering committee
- For investor due diligence covering high-risk processing
- For internal audit and group risk reporting in English
- For exchange with English-speaking parent companies, joint controllers or processors
- For cross-border consultation drafts that later are translated into national language

## Legal framework

- Art. 35(7) GDPR mandatory content of a DPIA
- Art. 35(2) GDPR DPO consultation
- Art. 36 GDPR prior consultation if residual risk remains high
- Art. 5(2) GDPR accountability principle
- EDPB Guidelines WP 248 rev.01 on DPIA
- For AI-related processing: Regulation (EU) 2024/1689 Art. 26 and Art. 27

## 6-step structure of the management summary

1. **Description of processing.** One paragraph: purpose, data, subjects, technology, transfers.
2. **Necessity and proportionality assessment.** One paragraph: legal basis, minimisation, alternatives.
3. **Risk to data subjects.** Short risk table with the top scenarios.
4. **Measures to mitigate risk.** Short list of key measures.
5. **Residual risk.** Risk rating before and after measures.
6. **Approval recommendation.** Approve, approve with conditions, prior consultation under Art. 36, do not approve.

## Template (English management summary)

```
DPIA MANAGEMENT SUMMARY
Confidential — for internal management use

Reference: [DPIA-YYYY-NN]
Date: [DD-MM-YYYY]
Controller: [Entity, legal representative]
DPO: [Name, contact]

1. PROCESSING IN ONE PARAGRAPH
[What is processed, for what purpose, on which legal basis, for which categories of data subjects, with which key technology, including transfers to third countries.]

2. NECESSITY AND PROPORTIONALITY
- Legal basis: [Art. 6 / Art. 9 GDPR with national law]
- Data minimisation: [Brief assessment]
- Less intrusive alternatives considered: [Yes / No, with note]
- Storage period: [Period, justification]
- Data subject rights: [Implemented mechanisms]

3. TOP RISKS TO DATA SUBJECTS (BEFORE MEASURES)
| Scenario | Likelihood | Severity | Rating |
| Unauthorised access | [h/m/l] | [h/m/l] | [R/O/Y/G] |
| Covert profiling | | | |
| Data leakage / transfer exposure | | | |
| Discrimination of data subjects | | | |
| Identity theft / fraud | | | |

4. KEY MEASURES
- Technical: [encryption, pseudonymisation, access control, logging, key management]
- Organisational: [training, four-eyes principle, authorisation concept, incident response]
- Contractual: [DPA Art. 28, SCC for transfers, TIA]
- AI-specific (if applicable): [human oversight, logging Art. 26(6) AI Act, transparency Art. 50 AI Act]

5. RESIDUAL RISK
| Scenario | Rating after measures |
| Unauthorised access | [R/O/Y/G] |
| Covert profiling | |
| ... | |

Overall residual risk: [HIGH / MEDIUM / LOW]

6. APPROVAL RECOMMENDATION
[ ] Approve — proceed with processing
[ ] Approve with conditions — see action items
[ ] Prior consultation under Art. 36 GDPR required
[ ] Do not approve — redesign processing

Action items
| No | Action | Owner | Deadline |

Next review: [DATE]

Sign-off
Controller representative: ____________________ Date: ____________________
DPO: ____________________ Date: ____________________
```

## Typical mistakes

- Management summary uses different wording than the full DPIA — inconsistency creates legal risk.
- Risk table is reduced to a single rating without scenarios — board cannot challenge.
- Approval recommendation is hidden in narrative — should be a binary choice.
- DPO opinion is not referenced — looks like a controller-only decision.
- Cross-border or AI specifics omitted in the summary even though they are key in the full DPIA.
- No action items with owner and deadline — recommendation is not actionable.
- Confidentiality classification missing — risk of unintended disclosure.

## Cross-references

- `datenschutzrecht/skills/dpia-en-template-full-version/SKILL.md` — Full English DPIA template
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — German full template
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Art. 36 procedure
- `datenschutzrecht/skills/dsfa-für-internationale-datentransfers/SKILL.md` — Transfers
- `datenschutzrecht/skills/dsfa-für-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` — AI interface
- `references/zitierweise.md` — Citation rules

## Sources as of 06/2026

- Art. 5(2), 35, 36 GDPR
- Regulation (EU) 2024/1689 (AI Act), Art. 26 and 27
- EDPB Guidelines WP 248 rev.01 on DPIA
- EDPB Opinion 28/2024 on AI models
- Case law: do not cite from model knowledge; verify with official sources
- Literature: only cite from user-provided source or licensed live access

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
