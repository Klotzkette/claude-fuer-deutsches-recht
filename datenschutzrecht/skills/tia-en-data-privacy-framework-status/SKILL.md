---
name: tia-en-data-privacy-framework-status
description: "English-language assessment of the current EU-US Data Privacy Framework (DPF) as Art. 45 GDPR transfer instrument. Commission Implementing Decision (EU) 2023/1795 of 10 July 2023, Executive Order 14086 basis, listing process, HR/Non-HR coverage, onward transfers, Schrems III. Test criteria for DPF reliance and residual risk."
---

# EU-US Data Privacy Framework – Current Status (English)

## Purpose

This skill provides an English-language assessment of the EU-US Data Privacy Framework (DPF) as a transfer instrument under Article 45 GDPR. It is intended for use with international counsel, US in-house teams, or supervisory authorities in cross-border investigations.

## When you need this skill

- Reviewing whether a TIA is still required for a US importer.
- Documenting DPF listing in the RoPA / TIA.
- Strategic choice between DPF and SCCs.
- HR data transfers to a US parent; checking HR coverage.
- Preparing for potential CJEU invalidation (Schrems III).

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
- The Schrems III action (NOYB) is pending; key issue: independence of the DPRC.
- If the decision is invalidated, DPF reliance ends; SCCs + TIA must take over (a return to the pure Schrems II landscape).

### EU review

- The Commission periodically reviews the effectiveness of the DPF; the **first review in summer 2024** confirmed the decision; further reviews are scheduled approximately every four years, with ad hoc reviews possible.

## / Checklist

1. **Verify the exact name** of the US entity in the DPF list.
2. **Check status** "Active"; if "Inactive" -> no DPF reliance.
3. Note **certification date** and **next re-certification**; capture a dated screenshot/PDF for the file.
4. Check **HR / Non-HR coverage**; HR must be separately elected.
5. Check **product / service coverage** against DPF declaration and privacy notice.
6. Review **onward transfer clauses** in the DPA (sub-processors outside the USA or outside the listing).
7. Add **DPRC notice** to data subject communications.
8. Add a **residual-risk memo** noting FISA 702 / EO 12333 and ongoing Schrems III observation.
9. Include a **fallback clause** in the contract: on revocation of the adequacy decision, automatic switch to SCCs + TIA.

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
> Residual risk arising from FISA Section 702 and Executive Order 12333 remains. The Schrems III proceedings at the General Court of the European Union are pending; in the event of invalidation, the contractual fallback clause activates the Standard Contractual Clauses under Decision (EU) 2021/914 with corresponding TIA (see Annex Fallback Transfer Tool).

## Common mistakes

- "Our parent company is listed" – the subsidiary is a separate legal entity and must be listed individually.
- HR data transferred but the listing only covers Non-HR.
- The entity is on the list but the privacy policy refers to data categories not included in the declaration.
- Re-certification date has passed – listing is inactive but transfer continues.
- Onward transfer to a further third country is missed.
- No fallback clause; on Schrems III invalidation the transfer has no basis.
- Confusing Swiss-US DPF with EU-US DPF.

## Cross-references

- `tia-schrems-ii-eugh-c-311-18-grundlagen` for Schrems II background.
- `tia-us-fisa-702-und-eo-12333-bewertung` for the FISA / EO assessment.
- `tia-eu-us-data-privacy-framework-aktueller-stand` for the German version.
- `tia-en-template-full` for the full English TIA template.
- `us-transfer-tia-dokumentation` for the German output package skill.

## Sources as of 06/2026

- Commission Implementing Decision (EU) 2023/1795 of 10 July 2023.
- US Executive Order 14086 of 7 October 2022.
- US Department of Commerce: DPF Principles and Supplemental Principles.
- CJEU C-311/18 of 16 July 2020 (Schrems II).
- European Commission, First Review of the EU-US DPF (Summer 2024) – verify against the official report.
- Schrems III proceedings (NOYB) at the General Court of the EU – check current case status.
- DPF list: dataprivacyframework.gov.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
