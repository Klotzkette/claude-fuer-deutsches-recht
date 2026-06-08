---
name: dpa-en-tom-annex-template
description: "English language technical and organisational measures (TOM) annex template for a DPA under Article 32 GDPR. Covers pseudonymisation encryption confidentiality integrity availability resilience recoverability and regular testing. Output: complete English TOM annex template suitable for ISO 27001 SOC 2 and BSI C5 alignment."
---

# TOM Annex – English Template (Article 32 GDPR)

## Zweck / Purpose

English-language annex template setting out the technical and organisational measures (TOM) required under Article 32 GDPR and incorporated by reference into the DPA. Purpose (DE): Englischsprachige TOM-Anlage zum DPA nach Art. 32 DSGVO.

## Wann dieses Modul hilft

- Cross-border or English-language DPA needs a TOM annex.
- Processor offers ISO 27001 / SOC 2 / BSI C5 alignment and the annex must reflect this.
- Periodic refresh of the TOM annex is due (recommended annually).

## Rechtlicher Rahmen

- Article 32 (1) (a) GDPR – Pseudonymisation and encryption.
- Article 32 (1) (b) GDPR – Ongoing confidentiality, integrity, availability, resilience.
- Article 32 (1) (c) GDPR – Ability to restore availability and access in a timely manner.
- Article 32 (1) (d) GDPR – Process for regularly testing, assessing and evaluating effectiveness.
- Article 25 GDPR – Data protection by design and by default.

## Ablauf / Checkliste

1. Confirm the processing risk profile.
2. Map measures against Article 32 (1) (a)-(d) GDPR.
3. Reference certifications (ISO 27001, SOC 2, BSI C5).
4. Define test cadence (penetration testing, vulnerability scanning).
5. Ensure sub-processor measures are consistent (Article 28 (4) GDPR).
6. Sign annex with date stamp; refresh annually or upon material change.

## Mustertext / Template

```
ANNEX II TO THE DATA PROCESSING AGREEMENT
TECHNICAL AND ORGANISATIONAL MEASURES (Article 32 GDPR)

Effective date: [DATE]
Processor: [NAME]
Review cycle: annually and upon material change

1. PSEUDONYMISATION (Art. 32 (1) (a) GDPR)
 1.1 Personal data shall be pseudonymised in development and test environments.
 1.2 The mapping table shall be stored separately, with access limited to the
 Data Protection Officer.

2. ENCRYPTION (Art. 32 (1) (a) GDPR)
 2.1 In transit: TLS 1.3 with forward secrecy, configured in accordance with
 industry guidance (e.g. BSI TR-02102 or NIST SP 800-52 Rev. 2).
 2.2 At rest: AES-256 (CBC or GCM) for all databases and backups.
 2.3 Key management: hardware security module (HSM) or equivalent; keys rotated
 at least annually.

3. CONFIDENTIALITY (Art. 32 (1) (b) GDPR)
 3.1 Physical access controls: 24/7 guarded data centres with multi-factor
 physical access.
 3.2 Logical access: multi-factor authentication for all privileged accounts.
 3.3 Authorisation: role-based access control on a least-privilege basis;
 periodic recertification.
 3.4 Segregation: multi-tenant logical separation with tenant-scoped access
 control.

4. INTEGRITY (Art. 32 (1) (b) GDPR)
 4.1 Transfer controls: documented interfaces; audit logging of all data
 exports.
 4.2 Input controls: write-operation logging with attribution to authenticated
 identities.
 4.3 Hashing: SHA-256 or stronger for integrity verification.

5. AVAILABILITY AND RESILIENCE (Art. 32 (1) (b) GDPR)
 5.1 Backups: daily incremental, weekly full; retention thirty (30) days.
 5.2 Recovery Point Objective (RPO): twenty-four (24) hours or less.
 5.3 Recovery Time Objective (RTO): eight (8) hours or less for critical
 processing.
 5.4 Geographic redundancy: synchronous replication across at least two EEA
 data centres.
 5.5 DDoS protection: upstream filtering with provider SLA.

6. RECOVERABILITY (Art. 32 (1) (c) GDPR)
 6.1 Incident response runbook; tabletop exercises at least annually.
 6.2 Documented restoration procedures.
 6.3 Restoration drills with actual data restoration tests at least semi-annually.

7. REGULAR TESTING (Art. 32 (1) (d) GDPR)
 7.1 Independent third-party penetration testing at least annually.
 7.2 Vulnerability scanning monthly.
 7.3 Internal ISMS audits annually; external ISO 27001 audits annually.
 7.4 TOM annex review at least annually.

8. ORGANISATIONAL MEASURES
 8.1 Data Protection Officer designated; contact details in Annex IV.
 8.2 Confidentiality undertakings from all personnel processing personal data
 (Article 28 (3) (b) GDPR).
 8.3 Annual data protection training with attendance records.
 8.4 Joiner-mover-leaver process; immediate revocation of access on exit.
 8.5 Incident response procedure with notification to the Controller within
 forty-eight (48) hours of becoming aware of a personal data breach
 (Article 33 GDPR).

9. CERTIFICATIONS AND STANDARDS
 9.1 ISO/IEC 27001:2022 – certified on [DATE] by [BODY].
 9.2 BSI C5:2020 Type 2 – report dated [DATE].
 9.3 SOC 2 Type II – report period [PERIOD].

10. SUB-PROCESSORS
 10.1 Sub-processors are required to implement measures at least equivalent
 to those set out in this Annex II (Article 28 (4) GDPR).
 10.2 Sub-processor audit reports shall be provided to the Controller on
 request.

Signed by: Date:
________________________________ ____________________________
[Processor representative]
```

## Typische Drafting-Fehler

- Marketing copy instead of concrete measures.
- "State of the art" without specifics.
- No update since initial signing.
- Pseudonymisation omitted, even though Article 32 (1) (a) GDPR mentions it.
- No RPO/RTO.
- No test cadence.
- Sub-processor consistency not addressed.

## Querverweise

- `datenschutzrecht/skills/avv-tom-art-32-dsgvo-anlage/SKILL.md`
- `datenschutzrecht/skills/dpa-en-template-controller-processor/SKILL.md`
- `datenschutzrecht/skills/avv-audit-und-kontrollrechte/SKILL.md`
- `datenschutzrecht/skills/avv-cloud-und-subverarbeitung-art-28-iv/SKILL.md`

## Quellen Stand 06/2026

- GDPR Article 25, Article 28 (3) (c), Article 32, Article 33.
- BSI TR-02102 (cryptographic guidance).
- NIST SP 800-52 Rev. 2.
- ISO/IEC 27001:2022.
- BSI C5:2020.
- SOC 2 Trust Services Criteria (AICPA, 2017, as amended).
- Citation rules: `../../../references/zitierweise.md`.
```

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
