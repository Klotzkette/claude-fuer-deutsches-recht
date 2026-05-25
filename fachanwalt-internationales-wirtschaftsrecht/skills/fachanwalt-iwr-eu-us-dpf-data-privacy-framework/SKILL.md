---
name: fachanwalt-iwr-eu-us-dpf-data-privacy-framework
description: "EU-US Data Privacy Framework (DPF) seit 10.7.2023 als Angemessenheitsbeschluss (EU) 2023/1795 nach Schrems II Aufhebung. Folge fuer Standard Contractual Clauses SCC und Transfer Impact Assessment TIA. Selbstzertifizierung US-Unternehmen ueber FTC. Liste DPF-zertifizierter Empfaenger. Workflow grenzueberschreitende Vertragsklauseln Updates."
---

# EU-US Data Privacy Framework — Folgen für Verträge

## Zweck

Spezial-Mandat: Mandant hat US-Dienstleister (Cloud, SaaS, AI-API) und muss EU-DSGVO-konformen Datentransfer absichern. Seit 10.7.2023 ist der **EU-US Data Privacy Framework (DPF)** mit Angemessenheitsbeschluss (EU) 2023/1795 in Kraft — als Ersatz für Privacy Shield (Schrems II EuGH C-311/18 aufgehoben).

## Eingaben

- US-Dienstleister (Microsoft, AWS, Google, OpenAI etc.)
- DPF-Zertifizierungs-Status (Liste DPF-Programm-Office)
- Datenarten (besondere Kategorien Art. 9 DSGVO?)
- Volumen / Umfang der Übermittlung
- Vorhandene SCC / BCR

## Rechtlicher Rahmen

- **Angemessenheitsbeschluss (EU) 2023/1795** vom 10.7.2023 — Grundlage
- **DSGVO Art. 45** — Übermittlung in Drittländer mit Angemessenheitsbeschluss
- **DSGVO Art. 46** — Geeignete Garantien (SCC, BCR) — Fallback wenn DPF nicht greift
- **EO 14086** Biden-Administration (Begrenzung US-Geheimdienst-Zugriff)
- **EuGH C-311/18 Schrems II** (16.7.2020) — Standard-Maßstab

## Workflow Vertragsklauseln-Update

### Phase 1 — DPF-Zertifizierungs-Check

- Prüfung [dataprivacyframework.gov](https://www.dataprivacyframework.gov/list) — ist Empfänger DPF-zertifiziert?
- Bei JA: DSGVO-Übermittlung zulässig ohne SCC
- Bei NEIN: SCC + TIA erforderlich

### Phase 2 — Vertrags-Klauseln anpassen

- **DPF-zertifiziert**: Klausel "Empfänger ist DPF-zertifiziert iSd Angemessenheitsbeschluss (EU) 2023/1795"
- **Nicht-DPF**: SCC 2021/914 (Module 2 oder 3) + TIA

### Phase 3 — Transfer Impact Assessment (TIA) wenn relevant

- Kategorisierung Daten (besondere Kategorien?)
- US-Geheimdienst-Zugriff: FISA Section 702, EO 12333 (eingeschränkt durch EO 14086)
- Technische Schutzmaßnahmen: Verschlüsselung at-rest und in-transit
- Vertragliche Maßnahmen: Streitbeilegungsklausel

### Phase 4 — Bei Streit / Klage gegen DPF

- Schrems III ist anhängig — DPF-Aufhebung möglich
- Fallback-Plan: SCC + zusätzliche Maßnahmen
- Bei Übergangsphase: Datenexport pausieren oder Anbieter wechseln

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| US-Dienstleister nicht DPF-zertifiziert | DSGVO-Verstoß Art. 44; Bußgeld | SCC + TIA in Vorbereitung | DPF-zertifiziert |
| Besondere Datenkategorien (Gesundheit, Biometrie) | strenge zusätzliche Anforderungen | TIA dünn | volle Risikoanalyse |
| Schrems III anhängig | DPF könnte aufgehoben werden | Notfall-Plan | Multi-Cloud mit EU-Optionen |
| Sub-Prozessor nicht DPF-zertifiziert | Kette unterbrochen | Prüfung Subprozessor | klare DPF-Kette |

## Querverweise

- `fachanwalt-internationales-wirtschaftsrecht-orientierung` — Triage
- `fachanwalt-it-recht-saas-vertrag-verhandlung` — Vertragsverhandlung
- `datenschutzrecht/skills/datenpanne-meldung` — bei Datenpanne mit US-Bezug
- `aussenwirtschaft-zoll-sanktionen` — bei Sanktions-Bezug

## Quellen und Updates

Stand: 05/2026. Angemessenheitsbeschluss (EU) 2023/1795 (10.7.2023). EO 14086. Schrems III anhängig — Stand prüfen. Bei DPF-Aufhebung dringend prüfen.
