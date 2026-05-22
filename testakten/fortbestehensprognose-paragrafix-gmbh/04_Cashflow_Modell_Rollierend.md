# Vorschau: 04_Cashflow_Modell_Rollierend

> Markdown-Vorschau der gleichnamigen XLSX-Datei. Berechnungen, Formeln und Formatierung nur im Original.

## Sheet: Inputs

| Spalte 1 | CASHFLOW-MODELL ROLLIEREND — Paragrafix GmbH — Eingabeparameter | Spalte 3 | Spalte 4 |
|---|---|---|---|
|  | Planungshorizont: Mai 2026 – April 2027 \| Stichtag Ist-Start: 30.04.2026 \| Erstellt: 02.05.2026 |  |  |
|  |  |  |  |
|  | LIQUIDITÄTSPARAMETER |  |  |
|  | Kassenbestand 30.04.2026 | 1870000 | EUR — tatsächlicher Cash-Bestand (Commerzbank, DB, Penta, Wise) |
|  | MRR April 2026 (Ist) | 187400 | EUR — Monthly Recurring Revenue |
|  | MoM-Wachstumsrate Umsatz (Base) | 0.06 | % — konservativ (war 12 %, halbe Rate für Planung) |
|  | MoM-Wachstumsrate Umsatz (Stress) | 0.03 | % — Stress-Szenario: halbe Base-Rate |
|  | BETRIEBSKOSTEN (MONATLICH) |  |  |
|  | Personalkosten brutto inkl. AG-Anteil | 247000 | EUR / Monat — 28 Festangestellte + GF |
|  | LLM-Tokenkosten (OpenAI 38 %, Anthropic 42 %, Mistral 20 %) | 38000 | EUR / Monat |
|  | AWS Cloud eu-central-1 | 22500 | EUR / Monat |
|  | SaaS-Lizenzen (Linear, Notion, GitHub, Sentry, Datadog, Slack) | 8400 | EUR / Monat |
|  | Gewerbemiete Heidestraße 78 + NK | 18700 | EUR / Monat |
|  | Steuerberatung + Rechtsberatung | 6200 | EUR / Monat |
|  | Marketing und Sales (LinkedIn, Konferenzen) | 24000 | EUR / Monat |
|  | Sonstige Aufwendungen | 7700 | EUR / Monat |
|  | USt-Vorauszahlung (Saldo netto) | 7500 | EUR / Monat |
|  | FINANZIERUNGSPARAMETER |  |  |
|  | Series-A Tranche 2 — Betrag | 3000000 | EUR — wird in Aug 2026 (Base) erwartet |
|  | Series-A Tranche 2 — Stressreduktion | 0.5 | Anteil, um den Tranche 2 im Stress-Szenario reduziert wird |
|  | Wandeldarlehen Earlybird (möglich) | 1500000 | EUR — diskutiert, noch nicht unterschrieben |
|  | Monat Tranche 2 Eingang (Base) | 4 | Monatsindex ab Mai = 1; Index 4 = August 2026 |
|  | Monat Tranche 2 Eingang (Stress) | 7 | Monatsindex; Index 7 = November 2026 (verzögert) |

## Sheet: Base Case

| Spalte 1 | ROLLIERENDER 12-MONATS-CASHFLOW — BASE CASE — Paragrafix GmbH | Spalte 3 | Spalte 4 | Spalte 5 | Spalte 6 | Spalte 7 | Spalte 8 | Spalte 9 | Spalte 10 | Spalte 11 | Spalte 12 | Spalte 13 | Spalte 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Planungsannahme: Series-A Tranche 2 (3,0 Mio. EUR) im August 2026 erwartet \| Stand: 02.05.2026 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Position | Mai 2026 | Jun 2026 | Jul 2026 | Aug 2026 | Sep 2026 | Okt 2026 | Nov 2026 | Dez 2026 | Jan 2027 | Feb 2027 | Mär 2027 | Apr 2027 |
|  | EINZAHLUNGEN |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Abo-Umsatz (MRR, brutto) | 198644 | 210,562.64 | 223,196.3984 | 236,588.1823 | 250,783.4732 | 265,830.4816 | 281,780.3105 | 298,687.1292 | 316,608.3569 | 335,604.8583 | 355,741.1498 | 377,085.6188 |
|  | Professional Services / Onboarding | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 |
|  | Series-A Tranche 2 (Finanzierung) | 0 | 0 | 0 | 3000000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Summe Einzahlungen | 205144 | 217,062.64 | 229,696.3984 | 3,243,088.1823 | 257,283.4732 | 272,330.4816 | 288,280.3105 | 305,187.1292 | 323,108.3569 | 342,104.8583 | 362,241.1498 | 383,585.6188 |
|  | AUSZAHLUNGEN |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Personalkosten brutto inkl. AG-Anteil | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 |
|  | LLM-Tokenkosten (OpenAI, Anthropic, Mistral) | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 |
|  | AWS Cloud (eu-central-1) | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 |
|  | SaaS-Lizenzen | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 |
|  | Miete Heidestraße 78 + NK | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 |
|  | Steuerberatung + Rechtsberatung | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 |
|  | Marketing / Sales | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 |
|  | Sonstige Aufwendungen | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 |
|  | USt-Vorauszahlung (Saldo) | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 |
|  | Summe Auszahlungen | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 |
|  | LIQUIDITÄT |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Anfangsbestand | 1870000 | 1695144 | 1,532,206.64 | 1,381,903.0384 | 4,244,991.2207 | 4,122,274.6939 | 4,014,605.1756 | 3,922,885.4861 | 3,848,072.6153 | 3,791,180.9722 | 3,753,285.8305 | 3,735,526.9804 |
|  | Netto-Cashflow | -174856 | -162,937.36 | -150,303.6016 | 2,863,088.1823 | -122,716.5268 | -107,669.5184 | -91,719.6895 | -74,812.8708 | -56,891.6431 | -37,895.1417 | -17,758.8502 | 3,585.6188 |
|  | Endbestand | 1695144 | 1,532,206.64 | 1,381,903.0384 | 4,244,991.2207 | 4,122,274.6939 | 4,014,605.1756 | 3,922,885.4861 | 3,848,072.6153 | 3,791,180.9722 | 3,753,285.8305 | 3,735,526.9804 | 3,739,112.5992 |
|  | Ampel-Status | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN |

## Sheet: Stress Case

| Spalte 1 | ROLLIERENDER 12-MONATS-CASHFLOW — STRESS-SZENARIO — Paragrafix GmbH | Spalte 3 | Spalte 4 | Spalte 5 | Spalte 6 | Spalte 7 | Spalte 8 | Spalte 9 | Spalte 10 | Spalte 11 | Spalte 12 | Spalte 13 | Spalte 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Planungsannahme: Tranche 2 auf 1,5 Mio. EUR reduziert und auf November 2026 verzögert \| Stand: 02.05.2026 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Position | Mai 2026 | Jun 2026 | Jul 2026 | Aug 2026 | Sep 2026 | Okt 2026 | Nov 2026 | Dez 2026 | Jan 2027 | Feb 2027 | Mär 2027 | Apr 2027 |
|  | EINZAHLUNGEN |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Abo-Umsatz (MRR, brutto) | 193022 | 198,812.66 | 204,777.0398 | 210,920.351 | 217,247.9615 | 223,765.4004 | 230,478.3624 | 237,392.7133 | 244,514.4946 | 251,849.9295 | 259,405.4274 | 267,187.5902 |
|  | Professional Services / Onboarding | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 | 6500 |
|  | Series-A Tranche 2 (Finanzierung) | 0 | 0 | 0 | 0 | 0 | 0 | 1500000 | 0 | 0 | 0 | 0 | 0 |
|  | Summe Einzahlungen | 199522 | 205,312.66 | 211,277.0398 | 217,420.351 | 223,747.9615 | 230,265.4004 | 1,736,978.3624 | 243,892.7133 | 251,014.4946 | 258,349.9295 | 265,905.4274 | 273,687.5902 |
|  | AUSZAHLUNGEN |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Personalkosten brutto inkl. AG-Anteil | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 | 247000 |
|  | LLM-Tokenkosten (OpenAI, Anthropic, Mistral) | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 | 38000 |
|  | AWS Cloud (eu-central-1) | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 | 22500 |
|  | SaaS-Lizenzen | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 | 8400 |
|  | Miete Heidestraße 78 + NK | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 | 18700 |
|  | Steuerberatung + Rechtsberatung | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 | 6200 |
|  | Marketing / Sales | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 | 24000 |
|  | Sonstige Aufwendungen | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 | 7700 |
|  | USt-Vorauszahlung (Saldo) | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 | 7500 |
|  | Summe Auszahlungen | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 | 380000 |
|  | LIQUIDITÄT |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Anfangsbestand | 1870000 | 1689522 | 1,514,834.66 | 1,346,111.6998 | 1,183,532.0508 | 1,027,280.0123 | 877,545.4127 | 2,234,523.7751 | 2,098,416.4883 | 1,969,430.983 | 1,847,780.9125 | 1,733,686.3398 |
|  | Netto-Cashflow | -180478 | -174,687.34 | -168,722.9602 | -162,579.649 | -156,252.0385 | -149,734.5996 | 1,356,978.3624 | -136,107.2867 | -128,985.5054 | -121,650.0705 | -114,094.5726 | -106,312.4098 |
|  | Endbestand | 1689522 | 1,514,834.66 | 1,346,111.6998 | 1,183,532.0508 | 1,027,280.0123 | 877,545.4127 | 2,234,523.7751 | 2,098,416.4883 | 1,969,430.983 | 1,847,780.9125 | 1,733,686.3398 | 1,627,373.93 |
|  | Ampel-Status | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN | GRÜN |

## Sheet: Sensitivity

| Spalte 1 | SENSITIVITÄTSANALYSE — Cash-Runway bei variierenden Annahmen | Spalte 3 | Spalte 4 | Spalte 5 | Spalte 6 |
|---|---|---|---|---|---|
|  | Zeigt verbleibenden Cash-Bestand am 30.04.2027 unter verschiedenen Wachstums- und Finanzierungsszenarien |  |  |  |  |
|  |  |  |  |  |  |
|  | Wachstum / Szenario | Ohne Tranche 2 | Tranche 2 1,5 Mio (Aug) | Tranche 2 3,0 Mio (Aug) | Tranche 2 3,0 Mio + Bridge |
|  | 0 % | -363200 | 1136800 | 2636800 | 4136800 |
|  | 3 % | 127,373.93 | 1,627,373.93 | 3,127,373.93 | 4,627,373.93 |
|  | 6 % | 739,112.5992 | 2,239,112.5992 | 3,739,112.5992 | 5,239,112.5992 |
|  | 9 % | 1,502,064.2702 | 3,002,064.2702 | 4,502,064.2702 | 6,002,064.2702 |
|  | 12 % | 2,453,255.076 | 3,953,255.076 | 5,453,255.076 | 6,953,255.076 |
