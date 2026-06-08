---
name: ropa-en-controller-template
description: "Full English-language template for the Records of Processing Activities (RoPA) of the controller under Article 30(1) GDPR. Seven mandatory contents, cover sheet, three worked examples (HR, client files, CRM with US sub-processor), and a versioning footer. Suitable for German law firms with international clients."
---

# Records of Processing Activities (RoPA) – Controller Template (English)

## Purpose

This skill provides a ready-to-use English-language template for the Records of Processing Activities (RoPA) of a controller pursuant to Article 30(1) GDPR. It is intended for German law firms, in-house counsel, and data protection officers who need to provide a RoPA in English to international clients, US group entities, or supervisory authorities in cross-border investigations.

## When you need this skill

- A multinational client requires an English-language RoPA.
- A US parent company asks for the EU subsidiary's processing records.
- A supervisory authority requests the RoPA in English in a cross-border case.
- A vendor audit (SOC 2, ISO 27001) reviews the RoPA.
- A first-time build of a RoPA in an internationally facing organisation.

## Legal framework

Article 30(1) GDPR requires the controller to maintain a record containing:

a) the name and contact details of the controller and, where applicable, the joint controller, the controller's representative, and the Data Protection Officer;
b) the purposes of the processing;
c) a description of the categories of data subjects and of the categories of personal data;
d) the categories of recipients to whom the personal data have been or will be disclosed, including recipients in third countries or international organisations;
e) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
f) where possible, the envisaged time limits for erasure of the different categories of data;
g) where possible, a general description of the technical and organisational measures referred to in Article 32(1) GDPR.

Article 30(3) requires written or electronic form; Article 30(4) makes the RoPA available to the supervisory authority on request; Article 30(5) provides a narrow SME exemption that rarely applies in practice.

## / Checklist

1. Fill in the cover sheet with controller details, representative (if applicable), and DPO.
2. One row per processing activity (one business process = one row).
3. Populate the seven mandatory columns.
4. For third-country transfers, identify the transfer tool (Adequacy Decision, SCCs, BCRs, DPF).
5. State retention periods concretely; avoid "as required by law".
6. Keep TOMs in a separate annex; reference only.
7. Add a versioning footer.
8. Schedule annual review.

## Template

### Cover Sheet

```
Controller: [Company / Firm Name]
Address: [...]
Representative (Art. 27): [if applicable]
Data Protection Officer: [Name, contact]
Supervisory Authority: [competent DPA]
Created: [date]
Last amended: [date]
Version: [v1.0]
```

### Table (mandatory columns)

| No. | Processing activity | Purpose | Legal basis | Categories of data subjects | Categories of personal data | Categories of recipients | Third country / safeguards | Retention period | TOM reference |
|---|---|---|---|---|---|---|---|---|---|
| 1 | HR administration | Establishment, performance, and termination of employment | Art. 6(1)(b) GDPR; Sec. 26 BDSG | Employees, applicants | Master data, contract data, payroll, sick leave | Social security, tax authority, payroll provider | none | 10 years after termination (Sec. 257 HGB, Sec. 147 AO); applicants 6 months | TOM Annex 1, 3, 5 |
| 2 | Client matter administration | Engagement, performance, and billing of legal services | Art. 6(1)(b) and (f) GDPR; Sec. 50 BRAO | Clients, opposing parties, witnesses | Master data, correspondence, briefs, fee data | Courts, authorities, opposing counsel, insurers | none | 6 years after end of mandate (Sec. 50(1) BRAO); tax-relevant documents 10 years | TOM Annex 1, 2, 4, 6 |
| 3 | Website contact form | Responding to inquiries | Art. 6(1)(b) or (f) GDPR | Prospective clients | Name, email, phone, message | Hosting provider (DPA in place) | none | 6 months after closure | TOM Annex 1, 5 |
| 4 | CRM sales | Customer relationship, business development | Art. 6(1)(b) and (f) GDPR | Existing customers, prospects | Master data, contact history, revenue data | CRM SaaS provider (USA) | USA – EU-US Data Privacy Framework (active listing on file, see DPF Annex) | 3 years after last contact | TOM Annex 1, 2, 5 |

### Versioning footer

```
Version 1.0 – Initial draft – [date, author]
Version 1.1 – [change] – [date, author]
```

## Common mistakes

- Mixing "purpose" and "legal basis" in one column.
- Listing individual recipients ("Ms. Smith, accountant") instead of categories ("Tax advisory firms").
- Stating "USA" without naming the transfer tool.
- Generic retention "10 years" without differentiation by data category.
- Copying the full Art. 32 wording into the TOM column instead of referring to a TOM annex.
- Failing to list a DPO where one is mandatory under Sec. 38 BDSG.

## Cross-references

- `ropa-art-30-dsgvo-grundlagen` for the German-language framework.
- `ropa-en-processor-template` for the processor counterpart.
- `ropa-konzernumlauf-und-multi-entity` for multi-entity groups.
- `dpa-en-template-controller-processor` for English DPA templates.
- `tia-en-template-full` for the English Transfer Impact Assessment template.

## Sources as of 06/2026

- Regulation (EU) 2016/679 (GDPR), in particular Article 30(1), Recitals 13 and 82.
- BDSG (German Federal Data Protection Act), Sec. 26, 38.
- BRAO (Federal Lawyers' Act), Sec. 50.
- HGB Sec. 257; AO Sec. 147.
- DSK Short Paper No. 1 "Records of Processing Activities" (Status 17 December 2018).
- EDPB Position Paper on Article 30(5) GDPR (19 April 2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
