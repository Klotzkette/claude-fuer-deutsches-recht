---
name: ropa-en-processor-template
description: "Full English-language template for the Records of Processing Activities (RoPA) of the processor under Article 30(2) GDPR. Four mandatory contents, controller list, processing categories, third-country transfers, sub-processor annex. For hosting providers, payroll, IT outsourcing, and cloud vendors with German clients."
---

# Records of Processing Activities (RoPA) – Processor Template (English)

## Purpose

This skill provides a ready-to-use English-language template for the Records of Processing Activities of a processor pursuant to Article 30(2) GDPR. Unlike the controller record, only four mandatory contents apply. Intended for cloud providers, IT outsourcing companies, payroll bureaus, hosting providers, printing services, external DPOs, and law firms acting in a processor role.

## When you need this skill

- An English-speaking processor builds its first RoPA.
- A multinational client requests a copy of the processor's records.
- Audit (SOC 2, ISO 27001, supervisory authority) requires English-language documentation.
- A law firm performs processor functions for a client (e.g. payroll, document management, eDiscovery hosting).

## Legal framework

Article 30(2) GDPR requires each processor and, where applicable, the processor's representative, to maintain a record containing:

a) the name and contact details of the processor or processors and of each controller on behalf of which the processor is acting, and, where applicable, of the controller's or the processor's representative, and the Data Protection Officer;
b) the categories of processing carried out on behalf of each controller;
c) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
d) where possible, a general description of the technical and organisational measures referred to in Article 32(1) GDPR.

One row per controller. Multiple processing categories can be grouped where TOMs are identical.

## / Checklist

1. Cover sheet with processor details.
2. Maintain a controller list (each customer relationship).
3. Per controller, describe processing categories (not individual activities).
4. Identify third-country transfers and the applicable transfer instrument.
5. Reference a TOM annex; do not repeat Art. 32 wording.
6. Maintain a separate sub-processor annex (Art. 28(4) GDPR) showing transfer chains.
7. Add versioning footer.

## Template

### Cover Sheet

```
Processor: [Company name]
Address: [...]
Representative (Art. 27): [if applicable]
Data Protection Officer: [Name, contact]
Created: [date]
Last amended: [date]
Version: [v1.0]
```

### Table (mandatory columns)

| No. | Controller | Categories of processing | Third country / safeguards | TOM reference |
|---|---|---|---|---|
| 1 | [Client A GmbH] | Hosting of accounting software, backups, patch management | none | TOM Annex A |
| 2 | [Client B AG] | Payroll processing, wage tax filings, social security filings | none | TOM Annex A |
| 3 | [Client C KG] | Email hosting, spam filtering | USA – sub-processor (SCCs + TIA in Annex B) | TOM Annex A |
| 4 | [Client D e.V.] | Membership administration, direct debit collection | none | TOM Annex A |

### Sub-processor annex

| Sub-processor | Location | Service | Transfer tool |
|---|---|---|---|
| [Hyperscaler Cloud] | USA | Infrastructure as a Service | EU-US DPF (active listing on file in Annex B) |
| [Email filter service] | Ireland | Spam filtering | EU/EEA – no transfer safeguards required |
| [Backup provider] | Germany | Offsite backup | EU/EEA – no transfer safeguards required |

### Versioning footer

```
Version 1.0 – Initial draft – [date, author]
Version 1.1 – [change] – [date, author]
```

## Common mistakes

- Confusing "categories of processing" (processor view) with "purpose" (controller responsibility).
- Omitting sub-processors that introduce third-country transfers.
- Maintaining redundant TOM descriptions per controller where the operational baseline is uniform.
- Missing the controller's DPO contact.
- Copying the full text of Article 32 into the TOM column instead of referencing a TOM annex.
- Overlooking second-tier sub-processor transfers (e.g. when a sub-processor uses a sub-sub-processor in the USA).

## Cross-references

- `ropa-art-30-dsgvo-grundlagen` for the German framework.
- `ropa-en-controller-template` for the controller counterpart.
- `dpa-en-template-controller-processor` for English DPA template.
- `dpa-en-tom-annex-template` for the TOM annex.
- `tia-en-template-full` for the English Transfer Impact Assessment.

## Sources as of 06/2026

- Regulation (EU) 2016/679 (GDPR), Article 30(2), Article 28.
- DSK Short Paper No. 1 "Records of Processing Activities" (Status 17 December 2018).
- DSK Short Paper No. 13 "Processor Agreements" (Status 16 January 2018).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (adopted 7 July 2021).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
