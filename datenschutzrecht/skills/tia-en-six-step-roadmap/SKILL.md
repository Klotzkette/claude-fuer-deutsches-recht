---
name: tia-en-six-step-roadmap
description: "English-language version of the EDPB Recommendation 01/2020 six-step roadmap for Transfer Impact Assessment. Step 1 know your transfers; Step 2 identify transfer tool; Step 3 assess law and practice; Step 4 adopt supplementary measures; Step 5 procedural steps; Step 6 re-evaluate. With checklists and sample entries for use with international counsel."
---

# Transfer Impact Assessment – EDPB Six-Step Roadmap (English)

## Purpose

This skill provides the English-language operational walk-through of EDPB Recommendation 01/2020 (Final Version 18 June 2021). It is the standard architecture for a TIA document and should be used together with the EU-US DPF status check, the FISA 702 / EO 12333 assessment, and the supplementary measures catalogue.

## When you need this skill

- Drafting a first TIA for a specific transfer with an English-speaking team.
- Coordinating with US in-house counsel.
- Filing a TIA with a supervisory authority in a cross-border case.
- Vendor diligence (SOC 2, ISO 27001) requesting evidence of TIA compliance.
- Training internal reviewers in English-speaking entities.

## Legal framework

- **CJEU C-311/18** Schrems II of 16 July 2020.
- **EDPB Recommendation 01/2020** "Recommendations on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data" (adopted 10 November 2020; Final Version 18 June 2021).
- **EDPB Recommendation 02/2020** "European Essential Guarantees for surveillance measures" of 10 November 2020.
- Articles 44–49 GDPR.

## / Checklist

### Step 1 – Know your transfers

Aim: map every transfer.

Verify:

- What data are transferred? Direct export, remote access, onward transfers?
- Who is exporter (controller or processor)?
- Who is importer (country, legal entity, group affiliation)?
- Which data categories? Special categories (Art. 9 GDPR)?
- Sub-processors and sub-sub-processors?
- Processing purposes and data flows (including internal flows at the importer).

Output: a transfer inventory table.

### Step 2 – Identify transfer tool

Aim: determine the legal basis for the transfer.

Options:

- **Article 45 GDPR – Adequacy decision** (e.g. UK, Switzerland, Japan, South Korea, EU-US DPF for listed importers).
- **Article 46 GDPR – Appropriate safeguards**:
 - Standard Contractual Clauses (Decision (EU) 2021/914, modules 1-4),
 - Binding Corporate Rules (Art. 47),
 - Approved Codes of Conduct or certifications,
 - DPA-issued contractual clauses.
- **Article 49 GDPR – Derogations** (consent, contract performance, legal claims) – strict reading; not for routine flows.

If Art. 45 applies, the TIA may be limited to Steps 1, 2, and 6 for the covered scope.

### Step 3 – Assess law and practice

Aim: evaluate third-country law and actual practice.

Check:

- Which authorities have access powers?
- What is the intensity of access? What safeguards exist (judicial control, suspicion-based access)?
- Apply Recommendation 02/2020 – European Essential Guarantees (EEG):
 - Guarantee A: rules must be clear, precise, and foreseeable.
 - Guarantee B: necessity and proportionality.
 - Guarantee C: independent oversight mechanism.
 - Guarantee D: effective remedies for the data subject.
- Are the guarantees met in law **and** in practice?

Sources for assessment: official reports, importer transparency reports, EDPB guidance, peer-reviewed public analyses.

### Step 4 – Adopt supplementary measures

If Step 3 negative: implement supplementary measures.

Three categories:

- **Technical measures** (often decisive): strong encryption with key management outside the third country; pseudonymisation with un-correlated keys; split processing; no clear-text access by the importer.
- **Contractual measures**: enhanced audit and transparency rights, reporting obligations on government requests, warrant canary, immediate suspension obligations.
- **Organisational measures**: staff training, escalation processes, vendor reviews, documented challenge policy.

Annex 2 of Recommendation 01/2020 lists Use Cases 1-7 (Use Cases 6 and 7 are scenarios where no effective measures are possible).

### Step 5 – Procedural steps

If supplementary measures are required:

- Update the DPA.
- Complete SCC Annexes I, II, III.
- Where SCCs are supplemented (added clauses, not deleted) – consider supervisory authority consultation.
- For BCRs – notify the Lead DPA of updates.
- Obtain authorisation where required.

### Step 6 – Re-evaluate

Re-assess on triggers:

- Changes in third-country law (statutes, court rulings).
- Changes in agency practice.
- Importer changes (group structure, sub-processors, services).
- Exporter changes (new data categories, new purposes).
- At minimum annually.

## Template

### TIA chapter headings

```
1. Know your transfers
 1.1 Transfer parties
 1.2 Data categories
 1.3 Sub-processors and onward transfers
 1.4 Data flow diagram

2. Transfer tool
 2.1 Chosen instrument
 2.2 Reasoning

3. Assessment of third-country law and practice
 3.1 Government access powers
 3.2 EEG assessment (A, B, C, D)
 3.3 Importer transparency reports and operational experience

4. Supplementary measures
 4.1 Technical
 4.2 Contractual
 4.3 Organisational
 4.4 Effectiveness analysis

5. Procedural steps
 5.1 Contractual implementation
 5.2 Supervisory authority consultation (where applicable)
 5.3 Sign-off

6. Re-evaluation
 6.1 Triggers for re-assessment
 6.2 Next review date
 6.3 Emergency suspension process
```

## Common mistakes

- Step 1 incomplete: only direct transfers identified; onward transfers ignored.
- Step 2: DPF chosen but the importer is not actively listed.
- Step 3: only abstract legal analysis without checking actual practice.
- Step 4: contractual measures alone without technical underpinning – per EDPB usually inadequate.
- Step 5: SCC text altered substantively rather than merely supplemented.
- Step 6: no review schedule.
- TIA prepared but not formally placed on file.

## Cross-references

- `tia-schrems-ii-eugh-c-311-18-grundlagen` (German) for legal background.
- `tia-edpb-roadmap-6-schritte-deutsch` (German) operational version.
- `tia-us-fisa-702-und-eo-12333-bewertung` for US specifics.
- `tia-zusaetzliche-schutzmassnahmen-encryption-pseudonymisierung` for Step 4.
- `tia-laender-bewertung-china-india-brazil-uk` for other countries.
- `tia-en-template-full` for the full TIA template in English.

## Sources as of 06/2026

- CJEU C-311/18 of 16 July 2020 (Schrems II), ECLI:EU:C:2020:559.
- EDPB Recommendations 01/2020 (Final Version 18 June 2021).
- EDPB Recommendations 02/2020 of 10 November 2020 (European Essential Guarantees).
- Commission Implementing Decision (EU) 2021/914 of 4 June 2021 (SCCs).
- Commission Implementing Decision (EU) 2023/1795 of 10 July 2023 (EU-US DPF).
- Articles 44–49 GDPR.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
