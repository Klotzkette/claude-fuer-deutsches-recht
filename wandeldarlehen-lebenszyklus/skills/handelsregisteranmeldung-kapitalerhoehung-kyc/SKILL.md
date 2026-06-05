---
name: handelsregisteranmeldung-kapitalerhoehung-kyc
description: "Handelsregisteranmeldung Kapitalerhoehung KYC: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Handelsregisteranmeldung Kapitalerhoehung KYC

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Handelsregisteranmeldung Kapitalerhoehung KYC** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `handelsregisteranmeldung-kapitalerhoehung` | Handelsregisteranmeldung nach Kapitalerhohung durch Wandlung vorbereiten. § 57 GmbHG Anmeldepflicht §§ 54 55 GmbHG Kapitalerhohung. Prüfraster: Anmeldungsinhalt Unterlagen Notar Einreichungspflicht Eintragungsvoraussetzungen. Output: Anmeldungsentwurf Unterlagencheckliste. Abgrenzung: nicht für Gesellschafterliste (gesellschafterliste-aktualisieren). |
| `kyc-aml-geldwaesche` | KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Prüfraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft Kapital Dokumentation. Output: KYC-Checkliste Risikoeinschaetzung Dokumentationspaket. Abgrenzung: nicht für Vertragsprüfung oder Wandlungsmechanik. |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Handelsregisteranmeldung Kapitalerhoehung KYC**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `handelsregisteranmeldung-kapitalerhoehung`

**Fokus:** Handelsregisteranmeldung nach Kapitalerhohung durch Wandlung vorbereiten. § 57 GmbHG Anmeldepflicht §§ 54 55 GmbHG Kapitalerhohung. Prüfraster: Anmeldungsinhalt Unterlagen Notar Einreichungspflicht Eintragungsvoraussetzungen. Output: Anmeldungsentwurf Unterlagencheckliste. Abgrenzung: nicht für Gesellschafterliste (gesellschafterliste-aktualisieren).

# Handelsregisteranmeldung Kapitalerhöhung

## Zweck

Dieser Skill begleitet die Handelsregisteranmeldung der Kapitalerhöhung nach vollzogener Wandlung. Er prüft die Vollständigkeit der Unterlagen, koordiniert mit dem Notar und verfolgt den Eintragungsprozess. Phase D des Lebenszyklus.

## Eingaben

- Vollständiges Notar-Paket (aus `notar-paket-uebermittlung`)
- Zuständiges Amtsgericht / Handelsregister (nach Sitz der Gesellschaft)
- Handelsregisternummer (HRB)
- Beauftragter Notar

## Rechtlicher Rahmen

### Primärnormen
- § 57 GmbHG (Anmeldung der Kapitalerhöhung: durch Geschäftsführerin, notarielle Beglaubigung)
- § 57a GmbHG (Inhalt der Anmeldung: neue Gesellschafterliste, Nachweis Sacheinlage)
- § 9c GmbHG (Prüfung durch das Registergericht – materielle Prüfung)
- § 382 FamFG (Registerverfahren – Bearbeitungsfrist)
- § 19 GwG (Transparenzregister-Anmeldepflicht nach HR-Änderung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Einreichung beim Handelsregister
Der Notar reicht die Anmeldung inklusive aller Anlagen elektronisch über das ERV (Elektronischer Rechtsverkehr) beim zuständigen Amtsgericht ein. Kosten: nach GNotKG (Eintragungsgebühr + Notargebühr).

### 2. Standardunterlagen Anmeldung § 57 GmbHG
a) Beschluss über Kapitalerhöhung (notariell beurkundet)
b) Übernahmeerklärung Lender (notariell beurkundet)
c) Sacheinlagebericht
d) Neue Gesellschafterliste (§ 40 GmbHG)
e) Versicherung der Geschäftsführerin nach § 8 Abs. 3 GmbHG (keine Hindernisse)
f) Anmeldungstext (von Notar vorbereitet, notariell beglaubigt)

### 3. Prüfung durch Registergericht (§ 9c GmbHG)
Registergericht prüft: formelle Voraussetzungen (Beschluss, Beurkundung, Unterlagen), materielle Voraussetzungen (Werthaltigkeit Sacheinlage), Vollständigkeit Gesellschafterliste. Häufige Beanstandungen: fehlende Angaben in Gesellschafterliste, unzureichender Sacheinlagebericht, formelle Mängel im Beschluss.

### 4. Bearbeitungsdauer
Standard: zwei bis acht Wochen. Überlastete Gerichte (z. B. AG Charlottenburg/Berlin): bis zu zwölf Wochen. Beschleunigte Eintragung auf Antrag bei wirtschaftlichem Interesse (§ 381 FamFG).

### 5. Nach Eintragung
Eintragungsbenachrichtigung an alle Parteien. Gesellschafterliste jetzt im elektronischen HR abrufbar. Lender hat volle Gesellschafterrechte (§ 16 GmbHG).

### 6. Transparenzregister-Folge-Meldung (§ 19 GwG)
Unmittelbar nach HR-Eintragung: Prüfung ob Lender wirtschaftlich Berechtigter (mehr als 25 % nach Kapitalerhöhung). Falls ja: Meldung an Transparenzregister (www.transparenzregister.de). Frist: unverzüglich.

## Häufige Beanstandungsgründe und Abhilfen

| Beanstandung | Abhilfe |
|---|---|
| Gesellschafterliste unvollständig (fehlendes Geburtsdatum) | Liste korrigieren und neu einreichen |
| Sacheinlagebericht ohne Werthaltigkeitsbegründung | Ergänzte Fassung nachreichen |
| Übernahmeerklärung ohne notarielle Beurkundung | Erneute Beurkundung erforderlich |
| Beschluss ohne Satzungsänderungstext | Beschluss nachbeurkunden |
| Versicherung Geschäftsführerin fehlt | Nachreich der Versicherung |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Registergericht beanstandet Sacheinlagebericht | Verzögerung, Nachbesserung | Eine Beanstandung | Keine Beanstandung |
| Bearbeitungsdauer über zwölf Wochen | Gesellschafterrechte Lender verzögert | Acht bis zwölf Wochen | Unter acht Wochen |
| Transparenzregister vergessen | § 56 GwG-Bußgeld bis EUR 150000 | Frist läuft | Unmittelbar gemeldet |
| Notar-Fehler in Unterlagen | Rücknahme und Neueinreichung | Kleiner Formfehler | Alle Unterlagen korrekt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/notar-paket-uebermittlung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/post-eintragung-checkliste/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 57/9c oder FamFG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 57 GmbHG (Anmeldung Kapitalerhöhung zum Handelsregister) → § 57a GmbHG (vereinfachte Kapitalerhöhung) → § 12 HGB i.V.m. §§ 374 ff. FamFG (elektronische Anmeldung) → § 56 Abs. 2 GmbHG (Sacheinlagebericht) → § 8 HGB (Inhalt Handelsregisteranmeldung)

## 2. `kyc-aml-geldwaesche`

**Fokus:** KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Prüfraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft Kapital Dokumentation. Output: KYC-Checkliste Risikoeinschaetzung Dokumentationspaket. Abgrenzung: nicht für Vertragsprüfung oder Wandlungsmechanik.

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
