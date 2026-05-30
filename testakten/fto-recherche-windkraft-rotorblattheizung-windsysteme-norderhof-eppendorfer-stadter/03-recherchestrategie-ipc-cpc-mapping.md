# 03 — Recherchestrategie: IPC/CPC-Klassifikationsmapping

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Eppendorfer / Klose | Stand: 23.01.2026

---

## 1. Ziel der Klassifikationsanalyse

Vor Erstellung der Suchprofile wird eine systematische Klassifikationsanalyse (IPC/CPC-Mapping) durchgeführt, um sicherzustellen, dass alle technologisch relevanten Felder der Patentklassifikation abgedeckt werden. Fehlende Klassifikationscodes sind eine Hauptquelle für falsch-negative FTO-Ergebnisse.

## 2. IPC-Klassifikation (International Patent Classification)

### Primäre IPC-Codes für Rotorblattheizung Windkraft

| IPC-Code | Bezeichnung | Relevanz |
|---|---|---|
| F03D 80/40 | Wind motors — Details, components not provided for in groups F03D 1/00–F03D 17/00 — Heating, ice protection | HOCH — Direktklasse |
| F03D 80/00 | Details, components, or accessories not provided for in other groups | MITTEL — Überklasse |
| H05B 3/84 | Electric heating elements — Resistance heating elements — adapted for surface mounting | HOCH — Heizelemente |
| H05B 3/20 | Electric heating elements — Resistance heating elements — Flexible / foil heating elements | HOCH — Folie/Vlies |
| H05B 1/02 | Electric heating — Control of electric heating — Responsive to temperature | MITTEL — Regelung |
| F03D 17/00 | Monitoring or testing of wind motors | MITTEL — Sensorik |
| G01N 27/22 | Measuring electric or magnetic properties by measuring impedance — Capacitance | MITTEL — Kapazitive Sensorik |
| B64D 15/12 | Aircraft equipment — Ice protecting — Electrical heating | REFERENZ — Luftfahrt analog |
| H02J 50/10 | Circuit arrangements for power conversion — Wireless power transfer using inductive coupling | MITTEL — Induktiv |

### Sekundäre IPC-Codes (erweiterte Abdeckung)

| IPC-Code | Bezeichnung | Relevanz |
|---|---|---|
| G05D 23/19 | Control of temperature — Responsive to temperature | NIEDRIG |
| G06N 20/00 | Machine learning | NIEDRIG — Algorithmus |
| H05B 6/10 | Induction heating | MITTEL — Induktionsheizung |
| F03D 1/06 | Wind motor — Rotors — Blades | MITTEL — Rotorblatt allg. |

## 3. CPC-Klassifikation (Cooperative Patent Classification)

Die CPC ist eine Erweiterung der IPC mit höherer Granularität, gepflegt durch EPO und USPTO gemeinsam.

### Direkt relevante CPC-Codes

| CPC-Code | Bezeichnung | Relevanz |
|---|---|---|
| F03D 80/40 | Wind motor components — Ice protection / heating | HOCH |
| H05B 2203/014 | Heating elements — Laminated heating elements | HOCH |
| H05B 3/84 | Surface mounting heating elements | HOCH |
| H05B 2203/016 | Heating elements using carbon fibers | SEHR HOCH |
| H05B 3/26 | Electric heating — Resistance heating elements — using graphite or carbon | HOCH |
| Y02E 10/723 | Energy generation — Wind energy — Offshore wind; onshore wind | REFERENZ |
| Y02E 10/74 | Wind energy — Combined wind + ice protection | MITTEL |

### CPC-Codes für Detektion und Steuerung

| CPC-Code | Bezeichnung | Relevanz |
|---|---|---|
| G01N 27/228 | Measuring properties by measuring impedance — capacitance sensing for ice | HOCH |
| G05B 13/026 | Adaptive control systems using learning systems | MITTEL |
| G08B 21/04 | Alarm systems — Ice alarm | MITTEL |

## 4. Rechtsraum-spezifische Klassifikationsdatenbanken

| Rechtsraum | Datenbank | Klassifikation | Besonderheit |
|---|---|---|---|
| EP/WO | Espacenet | CPC | Vollständigste CPC-Abdeckung |
| DE | DEPATISnet | IPC + CPC | DPMA-Klassifikation, DE-Volltexte |
| US | USPTO PatFT/AppFT | CPC + USPC | USPC als Legacy, CPC aktuell |
| CN | CNIPA / SooPAT | IPC + CPC | Chin. Anmeldungen oft nur IPC |
| WO | WIPO PATENTSCOPE | IPC | PCT-Anmeldungen |

## 5. Technologische Abgrenzungsfelder (Nicht-Recherche)

Folgende Felder werden explizit nicht recherchiert, um die Treffermenge beherrschbar zu halten:

- Allgemeine Windkraftanlagen (F03D 1/00 ff.) ohne Bezug zu Heizung/Enteisungr
- Allgemeine Gebäudeheizungstechnik (F24D, F24H)
- Photovoltaik-Enteisungssysteme (H02S 40/42)
- Enteisungssysteme für Luftfahrt (B64D 15/xx) — nur als Referenz/Stand der Technik

## 6. Prioritätsreihenfolge Recherche

**Priorität 1** (vollständige Lektüre Volltext): F03D 80/40 + H05B 3/84 + H05B 2203/016
**Priorität 2** (Abstract-Screening): H05B 3/20, H05B 3/26, G01N 27/228, H02J 50/10
**Priorität 3** (Stichwortsuche ergänzend): G05B 13/026, Y02E 10/74

## 7. Suchzeitraum

Anmeldetag: Suche ab 2010 (technologisch relevante Periode). Vorveröffentlichungen für Nichtigkeitsrecherche: Suche ab 2000 (Stand der Technik vor Prioritätstag EP 3 218 922 B1 = 15.06.2018).

Quellen: [IPC-Klassifikation WIPO](https://www.wipo.int/ipc/en/) | [CPC EPO/USPTO](https://www.cooperativepatentclassification.org) | [DEPATISnet DPMA](https://depatisnet.dpma.de)
