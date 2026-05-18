# DORA – Rechtsquellen-Snapshot

> Diese Datei führt die einschlägigen Rechtsquellen für die DORA-IKT-Vertragsprüfung. Vor jedem Mandat per EUR-Lex-Connector den aktuellen Stand ziehen und das Versionsdatum in den Output schreiben.

## Primärrecht

| Quelle | CELEX | Inhalt |
| --- | --- | --- |
| VO (EU) 2022/2554 | 32022R2554 | DORA – Digital Operational Resilience Act |
| RL (EU) 2022/2556 | 32022L2556 | DORA-Änderungs-Richtlinie (sektorale Anpassungen) |
| VO (EU) 2022/2554 konsolidiert | 02022R2554-YYYYMMDD | konsolidierte Fassung – immer den jüngsten Datumsstempel verwenden |

Anhänge der DORA-VO:
- Anhang I – Mapping der harmonisierten Begriffe.
- Anhang II – Aufsichtsmaßnahmen.

## Delegierte Verordnungen (RTS) und Durchführungsverordnungen (ITS)

| Quelle | CELEX | Gegenstand |
| --- | --- | --- |
| Del. VO (EU) 2024/1772 | 32024R1772 | RTS zur Klassifizierung schwerwiegender IKT-Vorfälle und erheblicher Cyberbedrohungen |
| Del. VO (EU) 2024/1773 | 32024R1773 | RTS zu Subunternehmer-Ketten kritischer/wichtiger IKT-Dienste (Art. 30 V DORA) |
| Del. VO (EU) 2024/1774 | 32024R1774 | RTS zum IKT-Risikomanagementrahmen und vereinfachten Rahmen |
| Del. VO (EU) 2024/1505 | 32024R1505 | RTS-Bündel ESAs zu IKT-Drittparteienrisiken |
| DurchfVO (EU) 2024/2956 | 32024R2956 | ITS Informationsregister IKT-Drittdienstleister |
| Del. VO (EU) 2024/3172 | 32024R3172 | RTS zu TLPT (Threat-Led Penetration Testing) |
| Del. VO (EU) 2025/xxxx | (laufend) | weitere RTS-/ITS-Pakete der ESAs |

Hinweis: Die ESA-Roadmap 2024–2026 enthält weitere RTS/ITS-Entwürfe (z. B. zu Joint Examination Teams, Aufsichtsgebühren, Konzentrations-Schwellen). Vor Audit immer EUR-Lex-Snapshot ziehen.

## Soft Law

| Quelle | Stelle | Gegenstand |
| --- | --- | --- |
| ESA Final Report on RTS Article 28 DORA | JC 2024/02 | Hintergrundbegründung |
| ESA Q&A on DORA | rolling | Auslegungsfragen |
| BaFin-Merkblatt DORA | BaFin-Webseite | nationale Anwendungshinweise |
| EBA Guidelines on Outsourcing (EBA/GL/2019/02) | EBA | Auslegungshilfe Restbestand |
| EIOPA Outsourcing Guidelines | EIOPA | Versicherer |
| BaFin BAIT/VAIT/KAIT/ZAIT | BaFin | bisherige Aufsichtspraxis (Aufhebung läuft) |

## Flankierendes nationales Recht

- § 25b KWG (Auslagerung)
- § 24 ZAG, § 32 VAG, § 36 KAGB
- DORA-Durchführungsgesetz (Bund) – BGBl. I Nr. XX/2024
- § 203 III StGB (mitwirkende Personen)
- § 9 KWG (Verschwiegenheit), § 311 VAG

## Aufrufmuster (Konnektor)

```text
eur-lex://celex/02022R2554              # konsolidierte DORA-VO
eur-lex://celex/32024R1772              # RTS Major Incidents
eur-lex://celex/32024R1773              # RTS Subunternehmer
eur-lex://celex/32024R1774              # RTS Risikomanagement
eur-lex://celex/32024R1505              # RTS-Bündel
eur-lex://celex/32024R2956              # ITS Informationsregister
eur-lex://celex/32024R3172              # RTS TLPT
bafin://dora                            # BaFin-Hub
esa-feeds://jc                          # ESA-Roadmap und Q&A
```

Stand dieser Referenzdatei: 2026-05-18. Bei Abweichungen Vorrang des EUR-Lex-Snapshot.
