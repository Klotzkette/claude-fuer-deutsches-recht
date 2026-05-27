---
name: kyc-aml-geldwaesche
description: "KYC- und AML-Anforderungen bei Wandeldarlehensmandat pruefen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Pruefraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft Kapital Dokumentation. Output: KYC-Checkliste Risikoeinschaetzung Dokumentationspaket. Abgrenzung: nicht fuer Vertragspruefung oder Wandlungsmechanik."
---

# KYC / AML / Geldwäscheprävention

## Zweck

Dieser Skill führt die vollständige KYC-Prüfung nach dem Geldwäschegesetz (GwG) für alle Parteien des Wandeldarlehens durch: wirtschaftlich Berechtigte, PEP-Status, Sanktionslisten, Mittelherkunft des Darlehensbetrags. Phase B des Lebenszyklus.

## Eingaben

- Alle Parteien mit vollständigen Identifikationsdaten (aus `parteien-erfassen`)
- Darlehensbetrag und Herkunft der Mittel (Lender)
- HR-Auszüge, Gesellschafterlisten, Organogramme der beteiligten Unternehmen
- Berufsausübungserlaubnis des Beraters (Rechtsanwalt: Pflicht nach § 2 Abs. 1 Nr. 10 GwG)

## Rechtlicher Rahmen

### Primärnormen
- § 2 Abs. 1 Nr. 10 GwG (Rechtsanwälte als Verpflichtete bei Unternehmenstransaktionen)
- § 3 GwG (Wirtschaftlich Berechtigter – natürliche Person mit mehr als 25 % Anteilen/Stimmrechten)
- §§ 10, 11, 12, 13 GwG (Allgemeine, vereinfachte, verstärkte Sorgfaltspflichten)
- § 19 GwG (Transparenzregister – Abgleich und Unstimmigkeitsmeldung)
- § 43 GwG (Verdachtsmeldepflicht bei Geldwäscheverdacht)
- § 47 GwG (Dokumentationspflicht – fünf Jahre nach Vertragsende)
- Art. 2 VO (EU) 765/2006 (EU-Konsolidierte Sanktionsliste)

### Rechtsprechung
- BGH, Urt. v. 15. November 2023 – 1 StR 184/22 (Geldwäsche im GmbH-Anteilserwerb – KYC-Pflicht des Beraters)
- OLG Frankfurt, Urt. v. 15. Dezember 2020 – 5 U 22/20 (Haftung für Sanktionsverstoß ohne ausreichendes Screening)

## Vorgehen

### 1. Verpflichtetenprüfung
Rechtsanwalt als Berater bei Gründung, Kauf oder Verkauf von Gesellschaftsanteilen: Verpflichteter nach § 2 Abs. 1 Nr. 10 GwG. Allgemeine Sorgfaltspflichten nach § 10 GwG verpflichtend.

### 2. Wirtschaftlich Berechtigte ermitteln
Gesellschaft: Wer hält mehr als 25 % der Anteile direkt oder über eine Kette? Beispiel Sonnenglas: Dr. Schöneck (40 %) und Habersaat (35 %) sind wirtschaftlich Berechtigte. Darlehensgeber (GmbH & Co. KG): Wer sind die Kommanditisten, wer hält mehr als 25 %? Transparenzregister prüfen.

### 3. Transparenzregisterabgleich (§ 19 GwG)
Abruf Transparenzregister für alle beteiligten Gesellschaften. Abgleich mit tatsächlichen Eigentumsverhältnissen. Unstimmigkeit? → Meldepflicht § 23a GwG.

### 4. PEP-Screening
Alle natürlichen Personen prüfen: Amtsträger in herausgehobener Position (§ 1 Abs. 12 GwG; z. B. Regierungsmitglieder, höhere Justizbeamte, Führungskräfte staatlicher Unternehmen)? Familienangehörige und enge Vertraute einbeziehen. Treffer: verstärkte Sorgfalt, GF-Freigabe.

### 5. Sanktionslistenscreening
Listen: EU-Konsolidierte Sanktionsliste (eur-lex.europa.eu), OFAC SDN, UN-Sicherheitsratsliste 1267, HM Treasury Financial Sanctions. Alle Parteien mit vollständigen Namen und ggf. Geburtsdaten screenen. Vorsicht: Namensähnlichkeit ohne Treffer ist kein Treffer – prüfen und dokumentieren.

### 6. Mittelherkunftsnachweis
Darlehensbetrag: Woher stammt das Kapital? Kontoauszüge, Jahresabschluss des Lenders, Herkunftsnachweis. Bei Auffälligkeiten: Verdachtsmeldung § 43 GwG an Financial Intelligence Unit (FIU).

## Checkliste KYC-Dokumentation

| Prüfung | Status |
|---|---|
| Identifikationsdokumente aller natürlichen Personen | [ ] |
| HR-Auszüge aller beteiligten Gesellschaften | [ ] |
| Wirtschaftlich Berechtigte ermittelt und dokumentiert | [ ] |
| Transparenzregister abgeglichen | [ ] |
| PEP-Status geprüft, Ergebnis dokumentiert | [ ] |
| Sanktionslisten geprüft (EU/OFAC/UN/HMT) | [ ] |
| Mittelherkunft plausibilisiert | [ ] |
| Aufbewahrungsfrist fünf Jahre eingerichtet | [ ] |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sanktionslistentreffer | Vertrag darf nicht abgeschlossen werden | Namensähnlichkeit prüfen | Kein Treffer |
| Mittelherkunft ungeklärt | Verdachtsmeldepflicht § 43 GwG | Teilweise belegt | Vollständig belegt |
| PEP ohne verstärkte Sorgfalt | GwG-Verstoß | PEP-Status in Prüfung | Keine PEP |
| Transparenzregister-Unstimmigkeit | Meldepflicht § 23a GwG | Abweichung erklärbar | Konsistent |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/parteien-erfassen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlung-kommunikation-paketverteilung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. GwG in der Fassung 05/2026. Bei Änderung GwG oder EU-Sanktionsregime aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Beschl. v. 20.01.2022 — **5 StR 320/21**, NJW 2022, 1029 Rn. 12: § 261 StGB n.F. (Geldwäsche) erfasst seit 2021 alle Straftaten als Vortaten ohne Katalog; Wandeldarlehensverträge mit unbekannten Geldgebern oder Offshore-Konstruktionen erfordern daher eine sorgfältige AML-Prüfung des Darlehensgebers, da die Herkunft der Darlehensvaluta unklar sein kann.

BFH, Urt. v. 14.02.2022 — **VIII R 40/18**, BStBl. II 2022, 556 Rn. 16: Steuerlicher Gestaltungsmissbrauch (§ 42 AO) bei Wandeldarlehen liegt vor, wenn der Darlehensgeber ein naher Angehöriger ist und die Konditionen (Zinssatz, Cap, Discount) keinem Fremdvergleich standhalten; AML-Prüfung und steuerliche Fremdvergleichsprüfung sind parallel durchzuführen.

OLG Frankfurt, Urt. v. 12.01.2022 — **6 U 183/19**, NJW-RR 2022, 478 Rn. 14: Pflicht zur Identifizierung des wirtschaftlich Berechtigten nach §§ 10, 11 GwG gilt auch für Rechtsanwälte bei der Beratung zu Wandeldarlehensverträgen; fehlende GwG-Dokumentation ist eine Ordnungswidrigkeit nach § 56 GwG mit Bußgeld bis 100.000 EUR.

### Normen-Ergänzung

§§ 10, 11 GwG (KYC-Pflichten, Identifizierung wirtschaftlich Berechtigter) → § 43 GwG (Meldepflicht) → § 56 GwG (Bußgeld bei Pflichtverletzung) → § 261 StGB (Geldwäsche n.F.) → Art. 3 EU-Geldwäsche-RL 2018/843 (5. AMLD) → § 42 AO (Steuerlicher Gestaltungsmissbrauch)
