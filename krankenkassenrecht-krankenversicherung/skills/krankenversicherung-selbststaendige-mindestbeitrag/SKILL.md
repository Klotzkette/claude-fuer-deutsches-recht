---
name: krankenversicherung-selbststaendige-mindestbeitrag
description: "Selbststaendige Mindestbeitrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Selbststaendige Mindestbeitrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Selbststaendige Mindestbeitrag** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-043-selbststaendige-mindestbeitrag-und-einkommensteuerbeschei` | Krankenversicherungsbeitrag für freiwillig versicherte Selbstständige: Mindestbeitrag, Einkommensnachweise, Spitzabrechnung und Widerspruch bei überhöhten Beiträgen. |
| `kv-044-kuenstlersozialkasse-und-krankenversicherung` | Kranken- und Rentenversicherung über die KSK (KSVG): Versicherungspflicht, Beitragsbemessung, Einkünftemeldepflicht und Prüfungen durch KSK/Rentenversicherung. |
| `kv-045-studentische-krankenversicherung-altersgrenzen` | Pflichtversicherung Studierender (§ 5 Abs. 1 Nr. 9 SGB V): Altersgrenze 25 Jahre, Fachsemesterlimit, Urlaubssemester, Ende der Versicherung und Übergangsoptionen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Selbststaendige Mindestbeitrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-043-selbststaendige-mindestbeitrag-und-einkommensteuerbeschei`

**Fokus:** Krankenversicherungsbeitrag für freiwillig versicherte Selbstständige: Mindestbeitrag, Einkommensnachweise, Spitzabrechnung und Widerspruch bei überhöhten Beiträgen.

# Selbstständige: Mindestbeitrag und Einkommensteuerbescheid

## Skill-Zweck

Selbstständige sind in der GKV freiwillig versichert. Dieser Skill klärt **Beitragsbemessung, Mindestbeitrag, Nachweis­pflichten gegenüber der Kasse und Strategien bei überhöhten Beiträgen**.

## Rechtlicher Rahmen

- **§ 240 SGB V** – Beitragsbemessung freiwillig Versicherter; Einkommensbegriff
- **§ 236 SGB V** – Mindestbemessungsgrundlage (2025: 1.178,33 €/Monat)
- **§ 226 Abs. 2 SGB V** – Beitrag aus Arbeitseinkommen + weiteren Einkünften
- **GKV-Spitzenverband – Beitragsverfahrensgrundsätze Selbstzahler** (BVGdS)
- BSG B 12 KR 7/18 R (Beitragsbemessung Selbstständige), BSG B 12 KR 21/11 R
- BVerfG 1 BvR 209/07 (Beitrag freiwillig Versicherter, Verfassungsmäßigkeit)

## Beitragsbemessung Selbstständige

| Einkommensquelle | Beitragspflichtig? |
|-----------------|-------------------|
| Gewinn aus Gewerbebetrieb | Ja (§ 15 EStG) |
| Einkünfte aus selbstständiger Arbeit | Ja (§ 18 EStG) |
| Einkünfte aus Vermietung | Ja |
| Kapitalerträge | Ja, wenn Besteuerung nicht KapErtSt final |
| Kindergeld | Nein |
| Sozialhilfe | Nein |
| Mindestbemessungsgrundlage | 1.178,33 €/Monat (auch wenn Einkommen niedriger) |

## Prüfprogramm

### Schritt 1 – Einkommensnachweise
- Aktuellster Einkommensteuerbescheid als Grundlage (Beitragsverfahrensgrundsätze)
- Neugründung/Einkommensverschlechterung: Prognose-/Schätzungsantrag möglich
- Kasse setzt vorläufigen Beitrag; Spitzabrechnung nach Vorlage des ESt-Bescheids

### Schritt 2 – Mindestbeitrag
- Auch wenn Einkommen unter 1.178,33 €/Monat: Mindestbeitrag gilt
- Ausnahme: hauptberuflich Selbstständige mit sehr niedrigem Einkommen → Härtefallprüfung
- Neugründer: Prognose kann unter Mindestgrundlage liegen wenn glaubhaft; Nachweis erforderlich

### Schritt 3 – Spitzabrechnung
- Vorläufiger Beitrag aus Vorjahreseinkommen → Steueränderungsbescheid eingehen lassen
- Spitzabrechnung: Kasse verrechnet Soll-Beitrag mit tatsächlichem Einkommen
- Nachzahlung oder Erstattung; Verjährung 4 Jahre (§ 25 SGB IV)

### Schritt 4 – Widerspruch bei überhöhtem Beitrag
- Kasse setzt Beitrag auf Mindestbemessungsgrundlage oder höher fest
- Einkommen niedriger: glaubhaft machen + Nachweise
- BSG: Kasse muss alle Einkommensquellen berücksichtigen, aber auch nur diese

### Schritt 5 – Einkommensoptimierung
- Betriebsausgaben mindern Gewinn und damit Beitrag
- Verluste aus anderen Einkunftsarten: seit BSG-Rechtsprechung nicht uneingeschränkt verrechenbar
- Investitionen in Betrieb: steuerrechtliche Minderung wirkt sich auf GKV-Beitrag aus

## Typische Fallen

- **Kein ESt-Bescheid verfügbar**: Kasse setzt Maximalgrundlage; Prognose mit Kontoauszügen, BWA stellen.
- **Nebengewerbe bei Anstellung**: Wenn Nebentätigkeit hauptberuflich selbstständig → Versicherungsfreiheit prüfen (§ 5 Abs. 5 SGB V).
- **Verlustvortrag**: GKV-Beitragsrecht unterscheidet sich von Steuerrecht; Verluste nicht automatisch mindernd.
- **Jahresausgleich vergessen**: Ohne Spitzabrechnung zu viel gezahlter Beitrag verjährt nach 4 Jahren.

## Output-Formate

- Beitragsschätzungsantrag (Neugründung)
- Spitzabrechnungsantrag mit ESt-Bescheid
- Widerspruch gegen Beitragsfestsetzung
- Einkommens-Beitragsberechnung (Tabelle)
- Mindestbeitrag-Härtefallantrag

## Quellen

- [§ 240 SGB V – Beitragsbemessung](https://www.gesetze-im-internet.de/sgb_5/__240.html)
- [GKV-Spitzenverband Beitragsverfahrensgrundsätze](https://www.gkv-spitzenverband.de)
- [BSG B 12 KR 7/18 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [§ 236 SGB V – Mindestbeitrag](https://www.gesetze-im-internet.de/sgb_5/__236.html)
- [BVerfG 1 BvR 209/07](https://www.bverfg.de/entscheidungen.html)
- [dejure.org § 240 SGB V](https://dejure.org/gesetze/SGB_V/240.html)

## 2. `kv-044-kuenstlersozialkasse-und-krankenversicherung`

**Fokus:** Kranken- und Rentenversicherung über die KSK (KSVG): Versicherungspflicht, Beitragsbemessung, Einkünftemeldepflicht und Prüfungen durch KSK/Rentenversicherung.

# Künstlersozialkasse und Krankenversicherung

## Skill-Zweck

Die Künstlersozialkasse (KSK) ermöglicht selbstständigen Künstlern und Publizisten eine GKV-ähnliche Absicherung. Dieser Skill klärt **Versicherungspflicht, Beitragsberechnung und KSK-Prüfverfahren**.

## Rechtlicher Rahmen

- **KSVG** (Künstlersozialversicherungsgesetz) §§ 1–29
- **§ 1 KSVG** – Versicherungspflichtige Künstler und Publizisten
- **§ 15 KSVG** – Abgabepflicht der Vermarkter (KSK-Abgabe)
- **§ 3 KSVG** – Halbe Beiträge: Künstler zahlt 50 %, KSK und Vermarkter 50 %
- **§ 10 KSVG** – Meldepflicht Einkommen
- **§ 35 SGB IV** – Prüfpflichten Rentenversicherung (KSK-Arbeitgeberprüfung)
- BSG B 3 KS 2/16 R (KSK-Versicherungspflicht), BSG B 3 KS 5/12 R (Einkommensgrenze)

## KSK-Versicherungssystematik

| Beitragsanteil | Träger | Höhe |
|---------------|--------|------|
| Künstler/Publizist | Versicherter | ~50 % des KV-Beitrags |
| Künstlersozialabgabe | Verwerter/Vermarkter | ~25 % |
| Bundeszuschuss | Bund | ~25 % |

## Prüfprogramm

### Schritt 1 – Versicherungspflicht KSK
- Tätigkeit als Künstler oder Publizist (§ 1 KSVG): selbstständig, hauptberuflich
- Mindestjahreseinkommen: 3.900 € (2025); unter dieser Grenze keine KSK-Pflicht (§ 3 Abs. 1 KSVG)
- Berufsanfänger: erste 3 Jahre Ausnahme von der Mindesteinkommensgrenze
- Kein Beschäftigung von mehr als 1 sozialversicherungspflichtigem AN (dann gewerblich, nicht künstlerisch)

### Schritt 2 – Meldepflicht Einkommen (§ 10 KSVG)
- Jährliche Einkommensmeldung an KSK bis 1. Dezember des laufenden Jahres
- Basis: voraussichtliches Jahresarbeitseinkommen
- Bei wesentlicher Abweichung: unterjährige Korrektur möglich
- Unterschätzung: Nachzahlung; Überschätzung: Erstattung

### Schritt 3 – Beitragsberechnung
- Beitrag = 50 % des allgemeinen KV-Beitragssatzes + Zusatzbeitrag aus Jahresarbeitseinkommen / 12
- Mindestbemessungsgrundlage: wie § 236 SGB V (ca. 1.178 €/Monat)
- Maximum: Beitragsbemessungsgrenze GKV

### Schritt 4 – KSK-Prüfung durch Rentenversicherung
- Prüfung ob KSK-Abgabe korrekt gezahlt wurde (Verwerterprüfung)
- Auch Versicherungspflicht des Künstlers geprüft
- Nachforderungen möglich; Widerspruch gegen Beitragsbescheid

### Schritt 5 – Leistungen und GKV-Integration
- Versicherter ist Pflichtmitglied in gewählter GKV
- Gleiche GKV-Leistungen wie Pflichtmitglieder
- Kassenwahlrecht besteht

## Typische Fallen

- **Angestelltentätigkeit parallel**: KSK-Versicherung endet wenn Arbeitsentgelt aus Anstellung > Jahresarbeitsentgeltgrenze.
- **Mindesteinkommen unterschritten**: KSK-Mitgliedschaft endet; kein automatisches Auffangversicherung → freiwillige GKV binnen 3 Monaten.
- **Vermarkter-Abgabe vergessen**: Wer künstlerische Leistungen einkauft und vermarktet, schuldet KSK-Abgabe; gilt auch für Agenturen und Unternehmen.
- **Mehrfachbeschäftigung**: Wenn Gesamteinkommen überwiegend aus Anstellung → KSK-Pflicht entfällt.

## Output-Formate

- KSK-Aufnahmeantrag-Checkliste
- Einkommensmeldung-Vordruck
- Widerspruch gegen KSK-Ausschluss
- KSK-Beitragsberechnung
- Vermarkter-Abgabe-Überprüfungsanfrage

## Quellen

- [KSVG – Künstlersozialversicherungsgesetz](https://www.gesetze-im-internet.de/ksvg/)
- [Künstlersozialkasse – Bundesagentur](https://www.kuenstlersozialkasse.de)
- [BSG B 3 KS 2/16 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [§ 10 KSVG – Meldepflicht](https://www.gesetze-im-internet.de/ksvg/__10.html)
- [dejure.org KSVG](https://dejure.org/gesetze/KSVG)
- [GKV-Spitzenverband KSK](https://www.gkv-spitzenverband.de)

## 3. `kv-045-studentische-krankenversicherung-altersgrenzen`

**Fokus:** Pflichtversicherung Studierender (§ 5 Abs. 1 Nr. 9 SGB V): Altersgrenze 25 Jahre, Fachsemesterlimit, Urlaubssemester, Ende der Versicherung und Übergangsoptionen.

# Studentische Krankenversicherung: Altersgrenzen

## Skill-Zweck

Studierende sind zu günstigen Konditionen gesetzlich pflichtversichert – aber nur bis zu bestimmten Altersgrenzen. Dieser Skill klärt **Altersgrenzen, Fachsemesterlimits, Übergangslösungen und Folgen des Versicherungsendes**.

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 9 SGB V** – Versicherungspflicht Studierender an staatlich anerkannten Hochschulen
- **§ 5 Abs. 1 Nr. 9 Satz 2 SGB V** – Altersgrenzen und Semesterlimit
- **§ 190 Abs. 9 SGB V** – Ende der Mitgliedschaft bei Exmatrikulation
- **§ 9 SGB V** – Freiwillige Weiterversicherung nach Studienende
- **§ 226 SGB V** – Beitragsbemessung (Mindestbeitrag für Studierende)
- BSG B 12 KR 9/10 R (Studentische KV, Urlaubssemester), BSG B 12 KR 6/15 R

## Grenzwerte Studentische KV

| Parameter | Wert |
|-----------|------|
| Altersgrenze | 25. Lebensjahr (d.h. bis zum Ende des Semesters in dem 25 wird) |
| Fachsemesterlimit | 14. Fachsemester |
| Beitrag (2025) | Einheitlich ca. 106 €/Monat (ca. 14,6 % von Mindestbemessungsgrundlage) |
| Urlaubssemester | Zählen für Alters-/Semesterlimit |

## Prüfprogramm

### Schritt 1 – Altersgrenzen prüfen
- Vollendung des 25. Lebensjahres: Ende der studentischen KV zum Ende des Semesters
- Verlängerung bei Ableistung von Wehr-/Bundesfreiwilligendienst (§ 5 Abs. 1 Nr. 9 Satz 3 SGB V): je nach Dauer
- Behinderung: keine Altersgrenze wenn Behinderung Studium verzögert hat

### Schritt 2 – Fachsemesterlimit
- Nach dem 14. Fachsemester: Ende der studentischen KV, auch wenn unter 25
- Urlaubssemester zählen mit (BSG bestätigt)
- Ausnahmsweise Verlängerung: wenn studienzeitverlängernd gewirkt hat (Krankheit, Behinderung, Gremientätigkeit)

### Schritt 3 – Übergang nach Studienende
- Exmatrikulation oder Ablauf Grenzen → freiwillige Versicherung (§ 9 SGB V): 3 Monate Beitrittsfrist
- Noch kein Job? Freiwillig versichern mit Mindestbeitrag
- Job sofort: Pflichtmitglied als Arbeitnehmer (§ 5 Abs. 1 Nr. 1 SGB V)
- Familienversicherung möglich wenn Elternteil GKV und Einkommen unter 505 €/Monat

### Schritt 4 – Beitrag Studierender
- Einheitlicher Beitrag ca. 106 €/Monat (Beitrag + Zusatzbeitrag)
- Bei Nebentätigkeit: ab gewisser Höhe erhöhter Beitrag; unter 520 €/Monat kein Einfluss
- Hauptberufliche Selbstständigkeit neben Studium: Versicherungsfreiheit prüfen (§ 5 Abs. 5)

### Schritt 5 – Auslandssemester
- Pflichtversicherung gilt auch bei Auslandssemester an EU-Hochschule (EHIC)
- Außereuropäisches Ausland: prüfen ob EHIC gilt; ggf. Zusatzversicherung
- Auslandspraktikum > 3 Monate: Pflichtversicherung kann enden → freiwillige Weitervesicherung

## Typische Fallen

- **Urlaubssemester als Fachsemester**: Viele Studierende wissen nicht, dass Urlaubssemester zählen.
- **Exmatrikulations-Zeitpunkt**: Mitgliedschaft endet nicht mit Exmatrikulation, sondern mit Ende des Prüfungssemesters.
- **Abschluss und Lücke**: Wer abschlussarbeitet, aber noch eingeschrieben ist: Pflichtversicherung läuft; nach Exmatrikulation sofort handeln.
- **PKV für Studierende**: Günstiger als freiwillige GKV; aber Rückkehr schwieriger; Langzeitperspektive bedenken.

## Output-Formate

- Altersgrenzen-Fristenkalender
- Exmatrikulationsbescheinigung-Checkliste
- Freiwillige GKV-Antrag nach Studium
- Studierendenversicherungs-Berechnung
- Informationsblatt Auslandssemester-Versicherung

## Quellen

- [§ 5 SGB V Nr. 9 – Studierende](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 190 SGB V – Ende der Mitgliedschaft](https://www.gesetze-im-internet.de/sgb_5/__190.html)
- [§ 9 SGB V – Freiwillige Versicherung](https://www.gesetze-im-internet.de/sgb_5/__9.html)
- [BSG studentische KV](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband Studierende](https://www.gkv-spitzenverband.de)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)
