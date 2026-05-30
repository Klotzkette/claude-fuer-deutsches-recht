---
name: stb-dba-regionenrouter-nichteu
description: "DBA-Regionenrouter für Nicht-EU- und Sonderstaaten: USA, Kanada, UK, Schweiz, Türkei, Israel, China, Indien, Japan, Australien, Lateinamerika, Afrika, Nahost, Zentralasien, Alt-DBA und fortgeltende UdSSR/Jugoslawien-Abkommen."
---

# DBA-Regionenrouter Nicht-EU

## Aufgabe

Wenn kein Einzel-Länderskill existiert, baut dieser Skill einen länderbezogenen Prüfpfad aus Matrix, DBA-Text und Einkunftsart.

## Regionale Risikomuster

| Region | Typische Edge-Cases |
| --- | --- |
| USA/Kanada | LLC/Hybrid, branch profits, Limitation on Benefits, Pension/RRSP/401(k), Stock Options, Quellensteuerformulare |
| Schweiz | Grenzgänger Art. 15a, 60-Tage-Regel, Verwaltungsrat, Quellensteuer, Wegzug |
| UK | Brexit, keine EU-Richtlinien, LLP/Partnerships, Pensions, Remittance-/Non-dom-Fragen als ausländische Vorschicht |
| China/Japan/Korea | Betriebsstätten, Service PE, Lizenz/Know-how, Entsendung, Quellensteuerentlastung |
| Indien | Service-/Software-Abgrenzung, Quellensteuer, Permanent Establishment, Equalisation-/Digitalthemen als nationale Vorschicht |
| Lateinamerika | Quellensteuer, technische Dienstleistungen, lokale Formulare, Treaty-Override im Quellenstaat prüfen |
| Afrika/Nahost | ältere DBA, Bauausführung, Personalentsendung, Sicherheit/Exportkontrolle als Nebenthema |
| UdSSR/Jugoslawien-Fortgeltung | Staatennachfolge und Anwendbarkeit besonders streng prüfen |

## Output

- Länderfahrplan.
- Artikel-Mapping.
- Belegliste.
- Edge-Case-Hinweise.
- Warnung, wenn nur ein Sonderabkommen und kein aktuelles Einkommensteuer-DBA greift.

## Praktiker-Tipps "Schnell zum Bescheid"

- **DBA-Text live ueber bundesfinanzministerium.de**: jeder Drittstaaten-DBA wird im PDF-Format gehalten; ohne Originaltext kein finalisiertes Memo.
- **MLI-Wirkung bei Drittstaaten**: nicht alle Drittstaaten haben MLI ratifiziert (USA nicht; Indien, China, Australien ja — vom Anwender mit aktuellem OECD-Verzeichnis abzugleichen). Wirksamkeitsdatum pro Staat und pro Norm separat.
- **Ansaessigkeitsbescheinigungen Drittstaaten**: USA IRS Form 6166 (ueber Form 8802, 6-8 Wochen); UK HMRC Certificate (4-6 Wochen); CH ESTV-Bescheinigung; Israel ITA-Bescheinigung. Bei VAE: Ministry of Finance Tax Residency Certificate.
- **Apostille / Konsularbeglaubigung**: USA, Australien, viele lateinamerikanische und afrikanische Staaten — Vorlaufzeit 6-10 Wochen.
- **Brexit-Spezifika UK**: keine MTRL und keine ZinsLizenzRL mehr — DBA-Hoechstsatz greift; Pension Protection unter UK-DBA pruefen.
- **Russland-Suspendierung 30.12.2023**: keine BZSt-Entlastung; siehe `stb-dba-russland-suspendierung-2024`.
- **VAE**: kein DBA seit Kuendigung 31.12.2021 — nationales Recht beider Seiten allein.
- **Iran / Belarus / Nordkorea / Syrien**: Sanktionsrechtliche Pruefung BAFA + EU-Sanktions-Listen vor jeder steuerlichen Beratung.
- **Hong Kong / Singapur**: eigene DBA seit 2013/2004 — nicht das CN-DBA anwendbar.
- **Taiwan**: kein "DBA" im klassischen Sinne, sondern Steuervereinbarung 2011 — eigene Pruefung notwendig.

## Trade-off-Tabelle

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| Aktuelles DBA (z.B. UK 2010) vs. Fortwirkungs-Altabkommen | aktuelles DBA, MLI-modifiziert | Altabkommen (z.B. UdSSR-DBA fuer ehemalige UdSSR-Staaten) | bei Mandat Klarheit ueber zeitliche Anwendung schaffen |
| Direkter Bezug Drittstaat vs. EU-Zwischengesellschaft | Direktbezug — DBA-Hoechstsatz | EU-Holding mit MTRL/ZinsLizenzRL | bei Substanz Pfad B; bei reiner Steuergestaltung scheitert an § 50d Abs. 3 EStG |
| Anrechnung § 34c EStG vs. MAP | unilateral nach DE-Erklaerung | bilateral bei Streitfaellen | bei klarem DBA-Anspruch Pfad A; bei strittiger Qualifikation MAP |
| Sanktionsrecht hinnehmen vs. Beratung verweigern | technische Steuerberatung trotz Sanktionsfolgen | Mandatsablehnung wegen Sanktionsrisiko | bei Iran/Belarus/Russland: erst Sanktionsrecht klaeren (BAFA, OFAC) |

## Was Reviewer/Pruefer triggert

- **Falsches DBA zitiert**: bei Hongkong nicht das CN-DBA; bei Taiwan kein DBA, sondern Steuervereinbarung.
- **Fortwirkungs-Altabkommen uebersehen** bei Nachfolgestaaten der UdSSR oder Jugoslawiens.
- **MLI-Status uebersehen** — auch wenn USA MLI nicht ratifiziert haben, gehoert das ins Memo.
- **Sanktionsrechtliche Beschraenkung uebersehen**: EU-Verordnungen 2014/833, 2022/263 (Russland-Sanktionen), Belarus-Sanktionen — gehen DBA vor.
- **VAE-DBA noch zitiert** trotz Kuendigung 31.12.2021.
- **Brexit-Folgen nicht beruecksichtigt**: keine MTRL/ZinsLizenzRL fuer UK-Verbindungen.
- **Service-Permanent-Establishment** bei Indien/China nicht geprueft — eigene Tatbestaende.
- **Limitation-on-Benefits (LOB)** bei US-DBA nicht geprueft — eigenstaendiger Anti-Missbrauchs-Tatbestand neben PPT.

## Regionale Pruef-Checklisten

### USA / Kanada
- LOB-Klausel pruefen (DBA-USA Art. 28; DBA-Kanada Art. 28).
- US-LLC: Qualifikationskonflikt (transparent in DE? — BMF 26.09.2014); Kanada LLP / Lim. Partnership.
- Pension Protection: IRA, 401(k), RRSP, RRIF — DBA-USA Protokoll 2006 Art. 18A.
- Stock Options/RSU: Vesting ueber mehrere Jahre, Aufteilung Lohnsteuer Tagesproporz.
- Branch Profits Tax (USA): zusaetzliche Steuer auf BS-Gewinn.

### Schweiz
- Grenzgaenger Art. 15a DBA-CH (60-Tage-Rueckkehrregel).
- Verwaltungsratsverguetungen Art. 16 (Sitzstaat).
- Wegzug: Schweizer Steuersystem (Bund, Kanton, Gemeinde) — Wegzugsbesteuerung § 6 AStG i.V.m. CH-Status.

### UK
- Brexit: keine MTRL/ZinsLizenzRL.
- LLP/Partnership: Qualifikationskonflikt.
- Non-Domiciled / Remittance Basis: deutsche Sicht — auslaendische Einkuenfte in UK nur bei Remittance besteuert; § 50d Abs. 9 EStG-Pruefung.
- Pension: UK-DBA 2010 Sonderregelungen pruefen.

### Asien (China, Japan, Korea, Indien)
- Service-PE-Tatbestand pruefen (China/Indien: 6 Monate / 183 Tage Service auch ohne feste Einrichtung).
- Entsendung: 183-Tage-Regel + lokale Sozialversicherungspflicht.
- Quellensteuer-Entlastung Indien: oft kompliziertes Verfahren mit lokalen Steuerbescheinigungen.
- Equalisation Levy Indien: Sonderlogik bei Digital Services — eigene Pruefung.

### Lateinamerika
- Quellensteuer auf technische Dienstleistungen: oft Sonderlogik (Brasilien, Argentinien, Mexiko).
- Treaty Override im Quellenstaat: Brasilien hat starke nationale Anti-DBA-Klauseln.
- Lokale Formulare oft Pflicht.

### Afrika / Nahost
- Aeltere DBA (1960er-1970er): MLI selten, BS-Schwellen niedrig.
- Bauausfuehrung: oft 6 Monate statt 12 Monate.
- Sicherheits-/Exportkontrolle als Nebenthema (BAFA).

### UdSSR / Jugoslawien-Fortgeltung
- Staatennachfolge im Einzelfall pruefen.
- Bosnien-Herzegowina, Nordmazedonien, Kosovo: Fortgeltung Jugoslawien-DBA pruefen.
- Belarus, Kasachstan, Usbekistan, Aserbaidschan: eigene DBA oder UdSSR-Fortgeltung.

## Mustertabelle Regionenpfad

| Region/Staat | Erste Anlaufstelle | Sonderpruefung | Querverweis |
|---|---|---|---|
| USA | DBA-USA 1989/Prot. 2006 | LOB Art. 28; § 50d Abs. 3 EStG; Pension Protection | `stb-dba-usa-1989-protokoll-2006` |
| Kanada | DBA-Kanada 2001 | LLP/RRSP/RRIF; Branch Profits | `stb-dba-kanada-2001` |
| UK | DBA-UK 2010 | Brexit, kein MTRL/ZinsLizenzRL; Non-Dom | `stb-dba-grossbritannien-2010` |
| Schweiz | DBA-CH | Grenzgaenger Art. 15a; Verwaltungsrat Art. 16 | `stb-dba-schweiz`, `stb-dba-grenzgaenger-schweiz-60-tage-rueckkehr` |
| China | DBA-China | Service-PE 6 Monate | live pruefen |
| Indien | DBA-Indien | Service-PE, Equalisation Levy, Software-Lizenz | live pruefen |
| Japan/Korea | DBA-Japan / DBA-Korea | Entsendung, lokale Sozialversicherung | live pruefen |
| Australien | DBA-Australien | Pension/Superannuation | live pruefen |
| Israel | DBA-Israel 2014 | Aliyah, Olim-Status | `stb-dba-israel-2014` |
| Tuerkei | DBA-Tuerkei 2011 | Kassenstaat Renten | `stb-dba-tuerkei-2011` |
| Brasilien | DBA-Brasilien | Treaty Override, Service als Lizenz | live pruefen |
| Russland | DBA suspendiert 30.12.2023 | keine Entlastung | `stb-dba-russland-suspendierung-2024` |
| VAE | DBA ausser Kraft seit 01.01.2022 | nationales Recht | live pruefen, kein DBA-Schutz |

## Drittstaat-Belegliste

| Beleg | USA | UK | CH | Indien | China |
|---|---|---|---|---|---|
| Ansaessigkeitsbescheinigung | IRS Form 6166 | HMRC CoR | ESTV-Bescheinigung | IT Form 10F | lokale CoR |
| Apostille / Konsularbeglaubigung | Apostille | nein (Haager Konvention) | nein | je nach Verwendung | Konsularbeglaubigung |
| Bearbeitungszeit | 6-8 Wochen | 4-6 Wochen | 2-4 Wochen | variabel | 4-8 Wochen |
| Online-Antrag | Form 8802 elektronisch | HMRC-Portal | kantonal variabel | TIN-Portal | nicht standardisiert |
