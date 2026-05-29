---
name: kyc-aml-geldwaesche
description: "KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Prüfraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft Kapital Dokumentation. Output: KYC-Checkliste Risikoeinschaetzung Dokumentationspaket. Abgrenzung: nicht für Vertragsprüfung oder Wandlungsmechanik."
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 10, 11 GwG (KYC-Pflichten, Identifizierung wirtschaftlich Berechtigter) → § 43 GwG (Meldepflicht) → § 56 GwG (Bußgeld bei Pflichtverletzung) → § 261 StGB (Geldwäsche n.F.) → Art. 3 EU-Geldwäsche-RL 2018/843 (5. AMLD) → § 42 AO (Steuerlicher Gestaltungsmissbrauch)
