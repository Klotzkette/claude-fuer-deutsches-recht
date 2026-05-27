---
name: corporate-kanzlei-automation-monitoring
description: "Automationen und Monitoring: Entwirft Monitore fuer Datenraum-Neuzugaenge, Q&A-Status, CP-Deadlines, Registerupdates, MAR-Signale und PMI-Aufgaben im Corporate/M&A-Kontext. Normen: MAR Art. 17, § 41 GWB (Vollzugsverbot), § 56 AWV."
---

# Automationen und Monitoring

## Triage — klaere vor Einrichtung

1. Welche Monitoring-Ziele: CP-Fristen, Datenraum-Updates, Kartellrecht-Deadlines, MAR-Signale?
2. Wer ist Owner der Alerts: PMO, federf. Partner, Mandant?
3. Eskalationsschwellen definieren: Ab wann manuell eingreifen?
4. Darf das System auf sensible Daten zugreifen (Insider-Info, GwG-Daten)?
5. Automatische Aussenkommunikation: Nie ohne human-in-the-loop Freigabe.

## Zentrale Normen

- **Art. 17 MAR** — Ad-hoc-Pflicht; kein automatisches Versenden ohne Freigabe
- **§ 41 GWB** — Vollzugsverbot; Monitoring der Freigabe-Fristen zwingend
- **§ 56 AWV** — FDI-Anmeldefrist 2 Monate; automatischer Kalender
- **§ 158 BGB** — Bedingungseintritt; CP-Erfuellung; Fristen-Monitoring
- **Art. 5, 25 DSGVO** — Monitoring ohne unnoetigen Zugang auf personenbezogene Daten

## Aktuelle Rechtsprechung

- OLG Frankfurt, Urt. v. 13.10.2021 - 4 U 162/20, NZG 2022, 213 — Kaeufer hat aktive Foerderpflicht bei CP-Erfullung; passives Monitoring reicht nicht; Eskalationspflicht wenn Frist naht
- BGH, Urt. v. 21.06.2019 - V ZR 244/17, NJW 2019, 2988 — Pflicht zur Bedingungsfoerderung; Unterlassen kann Schadensersatz ausloesen

## Kommentarliteratur

- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9 — PMO und Fristenmanagement

## Monitoring-Typen und Konfiguration

| Monitor | Datenquelle | Frequenz | Eskalationsschwelle | Owner |
|---|---|---|---|---|
| CP-Fristen | CP-Tracker | Taeglich | 2 Wochen vor Faelligkeit | PMO |
| Kartellrecht Phase-I-Frist | Kalender + Behoerden-Kontakt | Woechentlich | 5 Werktage vor Ablauf | Regulatory |
| FDI-Anmeldefrist (§ 56 AWV) | Signing-Datum + 2 Monate | Automatisch | Sofort bei 14 Tagen vor Frist | Legal |
| Datenraum-Neuzugaenge | DR-Plattform API / E-Mail-Alert | Taegliche Zusammenfassung | Wenn Material-Dokument eingestellt | DD-Lead |
| Gesellschafterlisten-Update | HR-System / Notar | Post-Closing | Bei Aenderung | Corporate-Lead |
| Transparenzregister | Transparenzregister API | Quartalsweise | Bei Aenderung UBO | GwG-Officer |
| MAR-Signal | Nachrichten-Feed + Bloomberg | Echtzeit (werktags) | Bei Kursrelevanz-Verdacht | Kapitalmarkt-Partner |

## Schritt-fuer-Schritt-Workflow

1. **Monitor-Ziele festlegen** — welche Fristen, Dokumente, Signale; Owner definieren
2. **Datenquellen verbinden** — DR-Plattform Alert, Kalender, Behorderenkontakt-Liste
3. **Eskalationsregeln konfigurieren** — Ampelstatus; Benachrichtigung; SMS/E-Mail/Call
4. **Stoppschwellen einbauen** — automatische Aktion nur nach human-in-the-loop Freigabe
5. **Test-Durchlauf** — alle Alerts simuliert; Eskalationspfad pruefen
6. **Woechentlicher Review** — PMO prueft Monitor-Status; adjustiert bei Bedarf
7. **Archivierung** — Monitor-Protokolle als Teil Deal-Archivs

## Output-Template Monitoring-Plan

```
MONITORING-PLAN
Transaktion: [DEAL-NAME]
Stand: [DATUM]

| Monitor | Trigger | Frequenz | Benachrichtigung | Eskalation | Stoppschwelle |
|---------|---------|---------|-----------------|-----------|---------------|
| CP-Fristablauf | 14 Tage vor Faelligkeit | Taeglich | PMO E-Mail | Partner Call | Kein Automatik-Vollzug |
| Kartell-Frist | 5 Werktage vor Phase-I-Ende | Taeglich | Regulatory + Partner | Sofort | — |
| DR-Neuzugang | Neues Dokument | Sofort / Digest taeglich | DD-Lead E-Mail | Bei Material Finding | — |
```

## Rote Schwellen

- Automatische Aussenkommunikation ohne human-in-the-loop → MAR-, BRAO- und Datenschutzrisiko
- Monitor auf Insider-Informationen ohne zugangsbeschraenktes System → Art. 18 MAR
- CP-Frist ohne Monitor → Vollzug-Fehler; gun jumping; Schadensersatz
- Kein Stoppschwellen-Konzept → Fehl-Alerts und falsche Signale

## Quellen

- Art. 17, 18 MAR; § 41 GWB; § 56 AWV; Art. 5, 25 DSGVO
- OLG Frankfurt 4 U 162/20 (Foerderpflicht CPs); BGH V ZR 244/17 (Bedingungsfoerderung)
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 9
