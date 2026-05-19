---
name: dora-ikt-vertragspruefung
description: Prüft IKT-Drittdienstleisterverträge eines Finanzunternehmens auf die Mindestanforderungen der EU-Verordnung 2022/2554 (DORA) und ergänzender RTS/ITS/EBA-/ESA-Leitlinien. Liefert eine tabellarische Lückenanalyse mit konkreten Verbesserungsvorschlägen und Klauselentwürfen.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - DORA
  - IKT-Vertrag
  - ICT third-party
  - Auslagerung Bank
  - Cloud Bank
  - BAIT MaRisk DORA
  - VO 2022/2554
  - Article 30 DORA
---

# DORA-IKT-Vertragsprüfung

## Zweck

Dieser Skill prüft Verträge mit IKT-Drittdienstleistern, die ein **Finanzunternehmen** i. S. v. Art. 2 DORA (Kreditinstitute, Zahlungs-/E-Geld-Institute, Wertpapierfirmen, Versicherer, Verwalter alternativer Investmentfonds, KVGen, OGAW, Zentralverwahrer, ZGP, Handelsplätze, Krypto-Dienstleister u. a.) abgeschlossen hat oder abschließen will, auf die Anforderungen der **Verordnung (EU) 2022/2554** (Digital Operational Resilience Act – "DORA") sowie der **dazu erlassenen RTS/ITS und EBA-/ESA-Leitlinien**.

Ergebnis ist eine tabellarische Lückenanalyse mit:

- Klauseltext (Ist),
- DORA-Anker (Soll),
- Lückenbewertung (konform / teilkonform / nicht konform / fehlt),
- konkretem Verbesserungsvorschlag inkl. Klausel-Entwurf,
- Kritikalitäts-Score (1 = niedrig … 5 = "kritisch oder wichtig" i. S. v. Art. 28 III DORA, § 28 BaFin-Auslegungshilfe).

Anwendungsfälle: Vertragsanbindung eines neuen IKT-Dienstleisters; Re-Papering bestehender Cloud-/SaaS-/Outsourcing-Verträge zum Geltungsbeginn 17. Januar 2025; ad-hoc-Prüfung im Rahmen einer BaFin-Sonderprüfung nach § 44 KWG / § 306 VAG.

## Eingaben

1. **Vertragsdokument** (PDF/DOCX/MD) inkl. aller Anlagen, SLAs, DPAs, Sub-Outsourcing-Listen.
2. **Klassifikation der Funktion** (kritisch / wichtig / sonstige) gem. Art. 28 II DORA i. V. m. RTS (Delegierte VO (EU) 2024/1773).
3. **Finanzunternehmens-Profil:** Aufsichtsregime (KWG, ZAG, KAGB, VAG, MiCAR), Größe (Art. 2 IV DORA – Verhältnismäßigkeitsklausel).
4. **Dienstart:** Cloud (IaaS/PaaS/SaaS), Managed Service, Software-Lizenz, Datenanalyse, Konnektivität.
5. **Datenkategorien:** personenbezogene Daten (DSGVO), Kundengeheimnis (§ 9 KWG / § 311 VAG), Berufsgeheimnis (§ 203 StGB).

## Rechtlicher Rahmen

### Primärrecht
- **DORA-Verordnung:** VO (EU) 2022/2554 v. 14.12.2022, ABl. L 333/1; Geltungsbeginn 17.01.2025 (Art. 64 II).
- **DORA-Änderungs-RL:** RL (EU) 2022/2556 (Anpassung sektoraler Rechtsakte).
- **Art. 28 DORA** – allgemeine Grundsätze für Vertragsvereinbarungen mit IKT-Drittdienstleistern.
- **Art. 29 DORA** – Vorabbewertung des IKT-Konzentrationsrisikos.
- **Art. 30 DORA** – **Pflichtinhalte** des IKT-Drittdienstleistervertrags.
- **Art. 30 III DORA** – verschärfte Pflichtinhalte bei **kritischen oder wichtigen Funktionen**.
- **Art. 31–44 DORA** – Aufsichtsrahmen kritischer Drittdienstleister (Lead Overseer ESA).

### Tertiärrecht / RTS / ITS
- Delegierte VO (EU) 2024/1773 v. 13.03.2024 (RTS zu Subunternehmer-Ketten, Art. 30 V DORA).
- Delegierte VO (EU) 2024/1772 (RTS Klassifizierung schwerwiegender IKT-Vorfälle).
- Delegierte VO (EU) 2024/1505 (ergänzende RTS-Pakete der ESAs).
- DurchführungsVO (EU) 2024/2956 (ITS zum Informationsregister).
- Vollständiger RTS-/ITS-Bestand siehe `references/dora-rechtsquellen.md` und Live-Abruf via EUR-Lex-Connector.

### Soft Law
- ESA Joint Final Reports zu RTS/ITS DORA (JC 2023/Y).
- BaFin-Merkblatt "DORA – Hinweise zur Anwendung", Stand 2024 (laufend aktualisiert).
- EBA Outsourcing Guidelines EBA/GL/2019/02 (für CRR-Institute; durch DORA überlagert, aber Auslegungshilfe).
- EIOPA Outsourcing Guidelines (Versicherungen).
- BaFin BAIT/VAIT/KAIT/ZAIT – soweit nicht durch DORA verdrängt (Stand: BaFin-Konsultation zur Aufhebung 2024/2025).

### Deutsches Aufsichtsrecht (flankierend)
- § 25b KWG (Auslagerung; weiterhin Auffanglinie für Nicht-IKT-Auslagerungen).
- § 24 ZAG; § 32 VAG; § 36 KAGB.
- FISG 2021 (Verschärfung Auslagerungsrecht).
- Datenschutz: Art. 28 DSGVO AVV, § 11 BDSG.

### Leitentscheidungen / Auslegung
- EuGH, Urt. v. 09.02.2023 – C-555/21 (UniCredit Bank Austria), BeckRS 2023, 1697 Rn. 31 (zur Reichweite finanzregulatorischer Vorgaben).
- BVerwG, Urt. v. 22.09.2020 – 10 C 21.19, BVerwGE 169, 313 Rn. 18 (Aufsichtsbehördliche Anordnungsbefugnis).
- BGH, Urt. v. 29.06.2023 – I ZR 211/22, NJW 2023, 3083 Rn. 24 – zur AGB-Kontrolle B2B-Cloudverträge.
- Nemeczek, in: Boos/Fischer/Schulte-Mattler, KWG/CRR-VO, 6. Aufl. 2022, § 25b KWG Rn. 142.
- Brock, in: BeckOK Bankrecht, 12. Ed. (Stand 01.02.2025), § 25b KWG Rn. 88.
- Zetzsche/Anker-Sørensen, EuZW 2023, 645 (648) – DORA und vertragsrechtliche Konsequenzen.
- Hingst/Lösing, BKR 2024, 1 (8) – DORA-Vertragsklauseln in der Praxis.

## Ablauf

1. **Dokumentenaufnahme.** Vertrag, Anlagen, DPA, SLA, Sub-Listen einlesen; Funktionsklassifikation (kritisch/wichtig vs. sonstige) festhalten.
2. **Konnektor aufrufen.** EUR-Lex-Connector: aktuellste konsolidierte Fassung VO 2022/2554 inkl. aller Anhänge + delegierter RTS/ITS abrufen (siehe Abschnitt "Konnektor & Datenquellen"). Versionsstand im Output dokumentieren.
3. **Pflichtklausel-Matrix anwenden.** Jede Pflicht aus Art. 30 II DORA (alle Verträge) und Art. 30 III DORA (kritische/wichtige Funktionen) sowie aus den RTS gegen den Vertrag mappen. Vorlage in `references/dora-klauselmatrix.md`.
4. **Lücken markieren.** Für jede Pflicht: zitierte Vertragsstelle (Klausel-Nr., Wortlaut) oder "fehlt"; Bewertung; Kritikalitätsstufe.
5. **Verbesserungsvorschläge formulieren.** Pro Lücke konkreter Klauselentwurf (DE), bei Bedarf EN-Übersetzung; Berücksichtigung Verhältnismäßigkeit Art. 4 DORA.
6. **Sekundärthemen prüfen.** Datenschutz (Art. 28 DSGVO, § 203 III StGB Berufsgeheimnis-Klausel), AGB-Kontrolle (§§ 305 ff. BGB, B2B-Strahlwirkung), § 9 KWG Kundengeheimnis, Exit-/Wiederherstellbarkeit, Subunternehmer-Kette gemäß RTS 2024/1773.
7. **Konzentrationsrisiko (Art. 29).** Wenn Lead-Overseer-Kandidat oder erheblicher Marktanteil: gesonderter Abschnitt mit Konzentrationsanalyse, Multi-Vendor-Empfehlung.
8. **Output erzeugen.** Tabular Review (siehe unten) + Executive Summary für die Geschäftsleitung + Klausel-Patch-Liste für Rechtsabteilung/Procurement.
9. **Aufnahme in Informationsregister.** Hinweis: Pflichtfelder gem. DurchführungsVO 2024/2956 (Register of Information) im Output identifizieren und mappen.

## Konnektor & Datenquellen

| Quelle | Zweck | Aufruf |
| --- | --- | --- |
| EUR-Lex | Konsolidierte Fassung VO (EU) 2022/2554 + Anhänge | `eur-lex://celex/02022R2554-<DATUM>` |
| EUR-Lex | Delegierte VOen 2024/1773, 2024/1772, 2024/1505, 2024/2956 | `eur-lex://celex/32024R1773` etc. |
| ESA-Webseiten | Final Reports / Q&A | https://www.eba.europa.eu, www.esma.europa.eu, www.eiopa.europa.eu |
| BaFin-Newsroom | nationale Auslegungshilfen, FAQ DORA | https://www.bafin.de/dora |
| Bundesanzeiger | nationale Umsetzungsakte FISG/DORA-DurchfG | https://www.bundesanzeiger.de |

Empfohlene MCP-Konnektoren (s. `CONNECTORS.md`):

```jsonc
{
  "mcpServers": {
    "eur-lex":   { "command": "node", "args": ["./mcp/eur-lex.js"] },
    "bafin":     { "command": "node", "args": ["./mcp/bafin.js"] },
    "esa-feeds": { "command": "node", "args": ["./mcp/esa-feeds.js"] }
  }
}
```

Vor jeder Prüfung: **immer** konsolidierte Fassung der DORA-VO frisch abrufen, Versions-/Stand-Datum in der Output-Kopfzeile mitführen.

## Pflichtklausel-Matrix (Auszug Art. 30 DORA)

| # | DORA-Anker | Pflichtinhalt (Soll) | Geltung |
| --- | --- | --- | --- |
| 1 | Art. 30 II lit. a | Vollständige und genaue Beschreibung aller Funktionen und Dienste, inkl. Sub-Funktionen | alle Verträge |
| 2 | Art. 30 II lit. b | Standorte (Region/Land) der Erbringung und Datenverarbeitung | alle |
| 3 | Art. 30 II lit. c | Verfügbarkeit, Authentizität, Integrität und Vertraulichkeit der Daten | alle |
| 4 | Art. 30 II lit. d | Zugriff, Wiederherstellung und Rückgabe (Exit) personenbezogener und nicht-personenbezogener Daten | alle |
| 5 | Art. 30 II lit. e | Service Level mit klaren Leistungszielen | alle |
| 6 | Art. 30 II lit. f | Unterstützung bei IKT-Vorfällen (mit/ohne Zusatzkosten) | alle |
| 7 | Art. 30 II lit. g | Volle Mitwirkung gegenüber zuständigen Behörden und Resolution Authority | alle |
| 8 | Art. 30 II lit. h | Kündigungsrechte und Mindestkündigungsfristen | alle |
| 9 | Art. 30 II lit. i | Teilnahme an IKT-Sicherheits-Awareness/Trainings (soweit relevant) | alle |
| 10 | Art. 30 III lit. a | Ausführliche Beschreibung Service-Level inkl. Updates, Versionen | nur kritisch/wichtig |
| 11 | Art. 30 III lit. b | Kündigungsfristen + Berichtspflichten zugunsten der Aufsicht | nur kritisch/wichtig |
| 12 | Art. 30 III lit. c | Recht zur **Überwachung der Leistung** des Dienstleisters fortlaufend | nur kritisch/wichtig |
| 13 | Art. 30 III lit. d | Operational and IKT-Sicherheitsanforderungen + Schulung | nur kritisch/wichtig |
| 14 | Art. 30 III lit. e | Beteiligung an **TLPT** (Threat-Led Penetration Testing) gem. Art. 26/27 DORA | kritisch/wichtig |
| 15 | Art. 30 III lit. f | **Uneingeschränkte Audit-/Einsichtsrechte** für Institut, externe Auditoren und zuständige Behörden, **inkl. Lead Overseer** | kritisch/wichtig |
| 16 | Art. 30 III lit. g | **Exit-Strategie** mit angemessenem Übergangszeitraum, Datenmigration, keine Schlechterstellung | kritisch/wichtig |
| 17 | Art. 30 III lit. h | Notfallpläne, Business Continuity, Wiederanlauf | kritisch/wichtig |
| 18 | Art. 30 II lit. j + RTS 2024/1773 | Vorgaben für Subunternehmer-Kette inkl. Genehmigungs-/Anzeigepflichten | nach Risiko |
| 19 | Art. 28 VII DORA | Keine vertragliche Verkürzung der Aufsichts-/Resolution-Rechte | alle |
| 20 | DurchfVO 2024/2956 | Datenpunkte für Informationsregister identifizierbar | alle |

Die vollständige Matrix mit allen Unterpunkten und Bewertungsschemata liegt in `references/dora-klauselmatrix.md`.

## Ausgabeformat

### A. Tabular Review (CSV/Markdown-Tabelle)

| Pflicht-# | DORA-Anker | Soll | Klausel (Ist) | Bewertung | Kritikalität (1–5) | Verbesserungsvorschlag | Klausel-Entwurf |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | Art. 30 II lit. d | Vollständige Rückgabe und Löschung der Daten in maschinenlesbarem Format binnen 30 Tagen | § 14.3 ("Daten werden auf Wunsch zurückgegeben") | teilkonform | 4 | Fristen, Format und Löschnachweis fehlen | "Der Auftragnehmer übergibt … binnen 30 Kalendertagen nach Vertragsbeendigung in einem branchenüblichen, maschinenlesbaren, nicht-proprietären Format und löscht alle Kopien einschließlich Backups innerhalb von 90 Tagen; die Löschung ist durch ein qualifiziertes Löschprotokoll nachzuweisen." |
| 15 | Art. 30 III lit. f | Audit-/Einsichtsrechte inkl. Lead Overseer, ohne Kostenbeteiligung des Instituts | § 17 ("Audit einmal jährlich, Selbstkosten anteilig") | nicht konform | 5 | Erweiterung auf Behörden + Lead Overseer; Kostenklausel anpassen | "Der Auftragnehmer gewährt dem Auftraggeber, von ihm benannten externen Prüfern sowie der zuständigen Aufsichts- und Resolution-Behörde einschließlich des Lead Overseers im Sinne von Art. 31 ff. DORA … uneingeschränkte und kostenfreie Audit- und Einsichtsrechte …" |

### B. Executive Summary (Memo, max. 1 Seite)

- Gesamtbewertung (Ampel + Score-Mittelwert)
- Top-3-Lücken (Kritikalität 5)
- Re-Papering-Aufwand (Schätzung)
- Empfehlung: vertraglich nachverhandelbar / Exit-/Alternativen-Prüfung notwendig
- Hinweis auf Aufnahme ins Informationsregister
- Quellenkopf mit Versionsstand der DORA-VO

### C. Klausel-Patch-Liste (DOCX/Markdown)

Pro Verbesserungsvorschlag ein Patch-Block mit:

- Klauselnummer alt / neu
- Diff (alt → neu)
- Begründung mit Zitat aus DORA / RTS / Kommentar (Bearbeiterstil)
- Verhandlungsschwere (1–3)

## Beispiel (Auszug Memo)

> **Mandat:** Prüfung des Master Services Agreement zwischen X-Bank AG (CRR-Institut, BaFin-Aufsicht) und CloudCo Inc. (SaaS, Kernbanken-Modul). Funktionsklassifikation: **kritisch oder wichtig** i. S. v. Art. 28 II DORA.
>
> **Kurzantwort:** Der Vertrag ist in der aktuellen Fassung nicht DORA-konform. Von 20 Pflichtinhalten sind 7 vollständig, 9 teilkonform und 4 fehlend. Re-Papering bis 17.01.2025 erforderlich (Art. 64 II DORA).
>
> **Tragende Lücken:**
> 1. Audit-/Einsichtsrechte: § 17 MSA gewährt nur jährliche Audits mit 60 Tagen Vorlauf und Kostenbeteiligung. Art. 30 III lit. f DORA verlangt anlassbezogene, kostenfreie Prüfungen einschließlich Lead Overseer (Brock, in: BeckOK Bankrecht, 12. Ed. [Stand 01.02.2025], § 25b KWG Rn. 88; Hingst/Lösing, BKR 2024, 1 [8]).
> 2. Sub-Outsourcing-Liste ist statisch, ohne Anzeige- und Genehmigungspflichten. Delegierte VO (EU) 2024/1773 verlangt Materialitätsschwellen und Ex-ante-Anzeige.
> 3. Exit-Strategie fehlt; § 18 MSA enthält nur eine Datenrückgabeklausel ohne Migrationsunterstützung – Verstoß gegen Art. 30 III lit. g DORA. Vgl. Zetzsche/Anker-Sørensen, EuZW 2023, 645 (648).
> 4. Beteiligung an TLPT-Tests nicht vereinbart (Art. 30 III lit. e i. V. m. Art. 26, 27 DORA).
>
> **Empfehlung:** Klausel-Patch-Liste umsetzen (siehe Anlage); Eskalation bei CloudCo wegen Audit- und Exit-Klauseln; Aufnahme in Informationsregister (DurchfVO 2024/2956) vorbereiten.

## Risiken und typische Fehler

- **Fehlende Funktionsklassifikation.** Ohne Einstufung als "kritisch oder wichtig" werden Art.-30-III-Pflichten oft übersehen. Dokumentieren!
- **AGB-Übernahme.** Standard-Cloud-AGB (Microsoft, AWS, GCP) sind regelmäßig **nicht** DORA-konform. Nachverhandlung über DORA-Addendum/SCC-ähnliche Anhänge erforderlich.
- **Sub-Out-Ketten.** Mehrstufige Subunternehmer-Ketten müssen vollständig abgebildet werden (RTS 2024/1773). Materialitätsschwellen vereinbaren.
- **Berufsgeheimnis.** § 203 III StGB-Klausel ("mitwirkende Personen") fehlt häufig – kritisch bei Daten, die unter § 203 StGB fallen (Banken: § 9 KWG; Versicherer: § 311 VAG; Rechtsanwälte: § 43a Abs. 2 BRAO).
- **Datenschutz.** Art. 28 DSGVO AVV ist separat oder integriert, aber **immer** mitzuprüfen.
- **Kündigungsrechte.** Art. 28 VII DORA setzt zwingende außerordentliche Kündigungsrechte voraus (z. B. behördliche Anordnung, schwerwiegende IKT-Vorfälle, Verstoß gegen anwendbares Recht).
- **Verhältnismäßigkeit.** Art. 4 DORA – kleinere Institute (z. B. nach Art. 16 DORA "vereinfachter Rahmen") können geringere Anforderungen haben. Nicht überregulieren.
- **Aktualität.** RTS/ITS-Pakete werden laufend nachgeschoben (ESA-Roadmap 2024–2026). Vor Audit immer EUR-Lex-Snapshot ziehen.
- **Halluzinationsrisiko.** Bei jedem Klauselzitat: konkretes Aktenzeichen/Fundstelle prüfen.

## Quellenpflicht

Jede juristische Aussage in der tabellarischen Auswertung wird belegt nach [`../../../references/zitierweise.md`](../../../references/zitierweise.md). Mindestens:

- DORA-Artikel mit Absatz/Buchstabe und Anhang (sofern Anhang einschlägig).
- Einschlägige delegierte VO mit CELEX-Nr.
- Mindestens ein BaFin- oder ESA-Verlautbarungs-Beleg, sofern vorhanden.
- Bei umstrittenen Auslegungsfragen: h. M. und Gegenauffassung mit Bearbeiterzitat (BeckOK Bankrecht, Boos/Fischer/Schulte-Mattler, Schimansky/Bunte/Lwowski Bankrechts-Handbuch, jeweils Bearbeiter).

Reihenfolge der Belege: EU-Recht vor nationalem Recht; Verordnung vor Soft Law; Rspr. vor Literatur (Rspr. zur DORA selbst liegt nur vereinzelt vor – ausdrücklich kennzeichnen: "Rspr. zu DORA liegt soweit ersichtlich noch nicht vor, vgl. aber …").
