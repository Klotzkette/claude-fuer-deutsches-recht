---
name: tia-en-data-privacy-framework-status
description: "Assesses whether an EU-US transfer can rely on an active Data Privacy Framework certification, records its scope and onward transfers, and tracks Latombe v Commission and the pending appeal without conflating them with Schrems litigation."
---

# EU-US Data Privacy Framework – Current Status (English)

## Purpose

This skill provides an English-language assessment of the EU-US Data Privacy Framework (DPF) as a transfer instrument under Article 45 GDPR. It is intended for use with international counsel, US in-house teams, or supervisory authorities in cross-border investigations.

## When you need this skill

- Reviewing whether a TIA is still required for a US importer.
- Documenting DPF listing in the RoPA / TIA.
- Strategic choice between DPF and SCCs.
- HR data transfers to a US parent; checking HR coverage.
- Monitoring the pending appeal in Latombe v Commission and preparing a lawful fallback if the adequacy decision later ceases to apply.

## Legal framework

### Basis

- **Commission Implementing Decision (EU) 2023/1795** of **10 July 2023** on the adequate protection of personal data under the EU-US Data Privacy Framework.
- US-side basis: **Executive Order 14086** of 7 October 2022 and DPF Principles issued by the Department of Commerce.
- Oversight: **Federal Trade Commission (FTC)** and, for transportation carriers, **Department of Transportation (DOT)**.
- Redress: two-step mechanism via **Civil Liberties Protection Officer (CLPO)** and **Data Protection Review Court (DPRC)**.

### Listing process

- Self-certification with the US Department of Commerce.
- Annual re-certification.
- Published on the official DPF list at dataprivacyframework.gov.
- Three tracks: EU-US DPF, Swiss-US DPF, UK Extension – each must be elected separately.
- HR and Non-HR data must be declared separately.

### Scope and limits

- Applies only to **actively listed** US legal entities.
- Group-affiliated entities are not automatically covered; each legal person must be checked separately.
- Sub-processors / onward transfers: DPF Principles require contractual safeguards.
- Data outside the listing scope (e.g. a product not included in the certification declaration) – DPF does **not** cover.

### Residual risk

- FISA 702 and EO 12333 remain in effect; EO 14086 narrows but does not abolish them.
- On 3 September 2025, the General Court dismissed the annulment action in Latombe v Commission, T-553/23, ECLI:EU:T:2025:831. On the pleas examined, it rejected the challenges concerning the DPRC's independence and bulk collection.
- The appeal filed on 31 October 2025, C-703/25 P, is pending before the Court of Justice. This is the Latombe litigation, not an action brought by NOYB and not an official proceeding named "Schrems III".
- Decision (EU) 2023/1795 remains in force while the appeal is pending. If DPF reliance later becomes unavailable, a transfer may continue only after a separately valid Chapter V mechanism and its factual prerequisites have been put in place; a contractual label does not itself complete that assessment.

### EU review

- The Commission published its first periodic review report on **9 October 2024**. Record that report as a monitoring source rather than describing it as a judicial confirmation of the adequacy decision.

## Checklist

1. **Verify the exact name** of the US entity in the DPF list.
2. **Check status** "Active"; if "Inactive" -> no DPF reliance.
3. Note **certification date** and **next re-certification**; capture a dated screenshot/PDF for the file.
4. Check **HR / Non-HR coverage**; HR must be separately elected.
5. Check **product / service coverage** against DPF declaration and privacy notice.
6. Review **onward transfer clauses** in the DPA (sub-processors outside the USA or outside the listing).
7. Add **DPRC notice** to data subject communications.
8. Add a **residual-risk memo** noting FISA 702 / EO 12333 and the current status of T-553/23 and C-703/25 P.
9. Include and operationalise a **fallback clause** before it is needed. Do not state that SCCs and a TIA become valid automatically merely because the contract names them.

## Template

### DPF check note

```
DPF Check – Importer: [exact name as listed on DPF list]
Retrieval date: [YYYY-MM-DD]
Retrieval URL: https://www.dataprivacyframework.gov/list
Retrieved by: [user]
Listing status: Active / Inactive
Certification date: [...]
Next re-certification: [...]
Track: EU-US DPF / Swiss-US DPF / UK Extension
HR data covered: Yes / No
Non-HR data covered: Yes / No
Listed services: [reconcile with privacy policy]
Independent Recourse Mechanism: [AAA / JAMS / EU DPA Panel]
Assessment: DPF reliable / partially reliable / not reliable
Residual risk: [...]
Fallback clause: [reference]
```

### TIA Step 2 wording

> The transfer relies on Article 45 GDPR in conjunction with Commission Implementing Decision (EU) 2023/1795. The importer is actively listed under the EU-US Data Privacy Framework as "..." with certification date [...] (see Annex DPF Check Note). The listing covers [HR / Non-HR] data and the services contractually rendered under this engagement.
>
> Residual risk arising from FISA Section 702 and Executive Order 12333 remains. The General Court dismissed the annulment action in T-553/23 on 3 September 2025; the appeal C-703/25 P is pending before the Court of Justice. Decision (EU) 2023/1795 remains the current transfer basis for an importer whose active certification covers this transfer. The SCC fallback under Decision (EU) 2021/914 may be used only after the correct module, annexes, transfer assessment and any necessary supplementary measures have been completed (see Annex Fallback Transfer Tool).

## Common mistakes

- "Our parent company is listed" – the subsidiary is a separate legal entity and must be listed individually.
- HR data transferred but the listing only covers Non-HR.
- The entity is on the list but the privacy policy refers to data categories not included in the declaration.
- Re-certification date has passed – listing is inactive but transfer continues.
- Onward transfer to a further third country is missed.
- Treating a named fallback clause as self-executing even though the correct SCC module, annexes and transfer assessment have not been completed.
- Confusing Swiss-US DPF with EU-US DPF.

## Cross-references

- `tia-schrems-ii-eugh-c-311-18-grundlagen` for Schrems II background.
- `tia-us-fisa-702-und-eo-12333-bewertung` for the FISA / EO assessment.
- `tia-eu-us-data-privacy-framework-aktueller-stand` for the German version.
- `tia-en-template-full` for the full English TIA template.
- `us-transfer-tia-dokumentation` for the German output package skill.

## Sources as of 09/2026

- [Commission Implementing Decision (EU) 2023/1795 of 10 July 2023](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023D1795).
- US Executive Order 14086 of 7 October 2022.
- US Department of Commerce: DPF Principles and Supplemental Principles.
- CJEU C-311/18 of 16 July 2020 (Schrems II).
- [European Commission, report on the first periodic review of the EU-US DPF, 9 October 2024, COM(2024) 451 final](https://commission.europa.eu/document/download/25695177-8073-4ce3-bf81-eb816dc6b468_en?filename=Report+on+the+first+periodic+review+of+the+functioning+of+the+adequacy+decision+on+the+EU-US+Data+Privacy+Framework.pdf).
- [General Court, judgment of 3 September 2025, Latombe v Commission, T-553/23, ECLI:EU:T:2025:831](https://curia.europa.eu/juris/liste.jsf?num=T-553/23).
- [Court of Justice, pending appeal filed on 31 October 2025, Latombe v Commission, C-703/25 P](https://curia.europa.eu/juris/liste.jsf?num=C-703/25%20P).
- [Official DPF list](https://www.dataprivacyframework.gov/list).
