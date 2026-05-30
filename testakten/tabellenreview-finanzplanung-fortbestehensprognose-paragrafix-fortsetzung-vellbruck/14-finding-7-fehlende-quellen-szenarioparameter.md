# 14 — Finding 7: Fehlende Quellen für Szenarioparameter

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-07
**Schwere:** Mittel
**Entdeckt:** 12. Januar 2026

---

## Sachverhalt

Das Blatt `ANNAHMEN` enthält narrative Beschreibungen der Planungsannahmen, jedoch fehlen für 11 von 19 wesentlichen Parametern die Quellenangaben bzw. Begründungen:

| Parameter | Blatt / Zelle | Wert v23 | Quelle angegeben? |
|---|---|---|---|
| Umsatzwachstum 2027 | PARAM!B5 | 17,1 % | Nein — Annahme CFO ohne Beleg |
| Zinssatz KK | ZINS-SCHULDEN!C5 | 4,9 % | Nein (hardcoded, Finding 4) |
| DSO (Forderungslaufzeit) | PARAM!B19 | 42 Tage | Nein |
| Stellenabbau FTE | PARAM!B31 | 8 FTE | Ja (Organigramm-Entwurf) |
| Abfindungsmonate | PERSONAL!G18 | 3 | Nein (hardcoded) |
| Mietkosten 2026 | PLAN-GuV!C44 | 184 TEUR | Ja (Mietvertrag) |
| IT-Wartung | PLAN-GuV!C52 | 210 TEUR | Nein |
| Sanierungskredit-Zinssatz | PARAM!B28 | 5,75 % | Nein — keine Bankbestätigung |
| Liquiditätsmindestbestand | PARAM!B25 | 350 TEUR | Nein — interne Annahme |
| Recovery Neuverträge 2027 | PLAN-GuV!E15 | 110 Stück | Nein — kein Vertriebsplan |
| Pensionsrückstellung Zuführung | PERSONAL!G55 | 480 TEUR | Nein (Finding 5) |

---

## IDW-S-11-Anforderung

IDW S 11 Tz. 34 verlangt explizit: "Die der Prognose zugrunde liegenden Annahmen sind vollständig darzustellen und zu belegen. Sind Annahmen nicht durch externe Quellen belegbar, ist dies zu erläutern und die Angemessenheit der Annahme zu begründen."

Das Modell v23 erfüllt diese Anforderung für 11 von 19 wesentlichen Parametern nicht.

---

## Empfehlung

Für jeden Parameter ohne Quellenangabe ist entweder: (a) eine externe Quelle (Marktbericht, Bankschreiben, Gutachten, Vertrag) nachzureichen, oder (b) eine explizite schriftliche Begründung der Annahme im Modell zu dokumentieren.

**Verantwortlich:** CFO Pellbach-Roosendaal.
**Frist:** 5 Arbeitstage.

**Quellen:** IDW S 11 Tz. 34–38, [https://www.idw.de](https://www.idw.de).
