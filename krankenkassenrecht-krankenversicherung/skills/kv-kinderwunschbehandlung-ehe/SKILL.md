---
name: kv-kinderwunschbehandlung-ehe
description: "KV Kinderwunschbehandlung EHE: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KV Kinderwunschbehandlung EHE

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **KV Kinderwunschbehandlung EHE** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-017-kinderwunschbehandlung-ehe-alter-und-kostenquote` | GKV-Leistungen für Kinderwunschbehandlung (§ 27a SGB V): Eheerfordernis, Altersgrenzen, 50-%-Kostenquote, Versuche und Widerspruch. |
| `kv-018-auslandsbehandlung-eu-s2-formular-und-notfall` | GKV-Leistungen im Ausland: EHIC-Karte, S2-Genehmigungsverfahren, Notfallbehandlung, Kostenerstattung und EU-Patientenrechte-Richtlinie. |
| `kv-019-grenzgaenger-auslandskrankenversicherung-und-koordinierun` | Krankenversicherungsrecht für Grenzgänger, EU-Koordinierungsverordnung 883/2004, S1-/S2-Formulare, Doppelversicherung und zuständige Träger. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **KV Kinderwunschbehandlung EHE**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-017-kinderwunschbehandlung-ehe-alter-und-kostenquote`

**Fokus:** GKV-Leistungen für Kinderwunschbehandlung (§ 27a SGB V): Eheerfordernis, Altersgrenzen, 50-%-Kostenquote, Versuche und Widerspruch.

# Kinderwunschbehandlung: Ehe, Alter und Kostenquote

## Skill-Zweck

Dieser Skill klärt den **GKV-Anspruch auf Kinderwunschbehandlung**: Welche Paare sind anspruchsberechtigt, welche Methoden werden bezuschusst, wie hoch ist der GKV-Anteil und was passiert nach Erschöpfung der Versuche?

## Rechtlicher Rahmen

- **§ 27a SGB V** – Leistungen bei Sterilität (Kinderwunschbehandlung)
- **§ 12 SGB V** – Wirtschaftlichkeitsgebot
- **§ 92 SGB V i.V.m. Kinderwunsch-Richtlinie (KiWu-RL)** – G-BA-Richtlinie zu Methoden und Verfahren
- Familienzuschuss-Programme der Bundesländer (ergänzen GKV-Leistungen)
- BSG B 1 KR 7/17 R (Kinderwunschbehandlung, Altersgrenzen), BSG B 1 KR 30/02 R (Eheerfordernis verfassungskonform)
- BVerfG: Eheerfordernis nach § 27a SGB V von BGH als nicht diskriminierend bestätigt

## Anspruchsvoraussetzungen § 27a SGB V

| Kriterium | Voraussetzung |
|-----------|--------------|
| Versicherungsstatus | Beide Partner GKV-versichert (§ 27a Abs. 3) |
| Familienstand | Verheiratet (Eheerfordernis) |
| Alter Frau | 25–40 Jahre |
| Alter Mann | 25–50 Jahre |
| Diagnose | Medizinisch begründete Sterilität |
| Kostentragung | GKV übernimmt 50 % der Kosten für max. 3 Versuche (IVF, ICSI) |

## Prüfprogramm

### Schritt 1 – Grundvoraussetzungen prüfen
- Beide Partner gesetzlich krankenversichert? (Mischpaare PKV/GKV: GKV zahlt nur für eigenes Mitglied)
- Verheiratet? (Eheerfordernis besteht nach aktueller Rechtslage)
- Altersgrenzen: Frau 25–40, Mann 25–50 am Behandlungsbeginn
- Sterilität medizinisch diagnostiziert: tubarer Befund, Spermastatus, anovulatorischer Zyklus

### Schritt 2 – Behandlungsmethoden
- GKV-fähig: IVF (In-vitro-Fertilisation), ICSI (Intracytoplasmatische Spermieninjektion)
- IUI (Intrauterine Insemination): nur unter bestimmten Voraussetzungen, KiWu-RL prüfen
- Kryokonservierung: grundsätzlich nicht GKV-Leistung; Ausnahmen bei krebsbedingter Unfruchtbarkeit (§ 27a Abs. 4 SGB V)

### Schritt 3 – Kostenberechnung
- GKV zahlt 50 % der genehmigten Kosten
- Bundeslandprogramme: viele Länder zahlen zusätzliche 25 %, sodass effektiv 75 % übernommen werden
- Private Zuzahlung: 50 % mindestens (bei bundesweitem Standardprogramm)
- Genehmigte Methode prüfen: nur G-BA-konforme Maßnahmen

### Schritt 4 – Versuchsbegrenzung
- 3 Versuche maximal (§ 27a Abs. 1 Satz 2 SGB V)
- „Versuch" = vollständiger Behandlungszyklus inkl. Transfer
- Abbruch durch Komplikation (keine Befruchtung, kein Transfer): zählt in der Regel nicht als Versuch (BSG)

### Schritt 5 – Genehmigungsverfahren
- Vor Behandlungsbeginn: Antrag bei Kasse mit ärztlichem Befundbericht
- Kasse entscheidet innerhalb 3 Wochen (§ 13 Abs. 3a SGB V)
- Ablehnung: Widerspruch mit Diagnosen, Leitliniennachweis, Behandlungsplan

## Typische Fallen

- **Mischpaar PKV/GKV**: GKV zahlt nur 50 % ihrer eigenen Behandlungskosten für das GKV-Mitglied; PKV-Partner zahlt vollständig privat.
- **Eheerfordernis und Lebenspartnerschaft**: Gesetzliche gleichgeschlechtliche Ehe erfüllt Eheerfordernis seit 2017 (Ehe für alle).
- **Altersgrenze überschritten**: Strenge Auslegung; Behandlung noch im 40. Lebensjahr der Frau beginnen.
- **Kryokonservierung bei Krebs**: Sonderfall § 27a Abs. 4: GKV zahlt Einfrieren vor Chemotherapie.

## Output-Formate

- Genehmigungsantrag Kinderwunschbehandlung
- Widerspruch gegen Ablehnung
- Kostenplan (GKV-Anteil, Landesförderung, Eigenanteil)
- Versuchszähler-Dokumentation
- Informationsblatt Altersgrenzen und Eheerfordernis

## Quellen

- [§ 27a SGB V – Kinderwunsch](https://www.gesetze-im-internet.de/sgb_5/__27a.html)
- [Kinderwunsch-Richtlinie G-BA](https://www.g-ba.de/richtlinien/85/)
- [BSG B 1 KR 7/17 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband Kinderwunsch](https://www.gkv-spitzenverband.de)
- [dejure.org § 27a SGB V](https://dejure.org/gesetze/SGB_V/27a.html)
- [Bundesministerium für Gesundheit Kinderwunsch](https://www.bundesgesundheitsministerium.de)

## 2. `kv-018-auslandsbehandlung-eu-s2-formular-und-notfall`

**Fokus:** GKV-Leistungen im Ausland: EHIC-Karte, S2-Genehmigungsverfahren, Notfallbehandlung, Kostenerstattung und EU-Patientenrechte-Richtlinie.

# Auslandsbehandlung: EU, S2-Formular und Notfall

## Skill-Zweck

Dieser Skill klärt **GKV-Leistungen für Behandlungen im Ausland**: Notfallversorgung mit EHIC, geplante Behandlung mit S2-Genehmigung und Kostenerstattung nach EU-Patientenrechterichtlinie.

## Rechtlicher Rahmen

- **§ 13 SGB V** – Kostenerstattung (Auslandsbehandlung als Sonderfall)
- **§ 18 SGB V** – Auslandsbehandlung: GKV zahlt wenn Behandlung im Inland nicht möglich/unzumutbar
- **VO (EG) 883/2004** – Koordinierung der Systeme sozialer Sicherheit (EU)
- **VO (EG) 987/2009** – Durchführungsverordnung
- **Richtlinie 2011/24/EU** – EU-Patientenrechterichtlinie (grenzüberschreitende Gesundheitsversorgung)
- **§ 140e SGB V** – Inanspruchnahme von Leistungen in EU/EWR (Umsetzung der Richtlinie)
- S2-Formular (Genehmigung geplanter Behandlung im EU-Ausland)
- Europäische Krankenversicherungskarte (EHIC) – Notfall und notwendige Behandlung

## Fallübersicht

| Situation | Rechtgrundlage | Anspruch |
|-----------|---------------|----------|
| Notfall im EU-Ausland | EHIC, VO 883/2004 | Wie Inländer im Behandlungsland |
| Geplante Behandlung EU/EWR | S2-Formular (§ 18 SGB V analog) | Nur bei Genehmigung oder Kostenerstattung |
| EU-Patientenrechterichtlinie | § 140e SGB V | Kostenerstattung auf dt. Kassenniveau |
| Nicht-EU-Ausland | § 13 SGB V | Ausnahme: unaufschiebbar, notwendig |
| Auslandsstudium, Entsendung | VO 883/2004 | Sonderregelungen, S1-Formular |

## Prüfprogramm

### Schritt 1 – Notfallbehandlung im Ausland
- EHIC-Karte gültig? (Ausgestellt von Kasse, kostenlos)
- Im EU/EWR: Behandlung wie gesetzlich Versicherter des Gastlandes; kein Vorschuss nötig
- Kosten direkt zwischen Kassen abgerechnet; Eigenanteil des Gastlandes trägt Versicherter
- Nachträgliche Erstattung: wenn Notfall bezahlt wurde, Antrag bei Heimatkasse

### Schritt 2 – Geplante Behandlung (S2-Formular)
- S2-Antrag bei Heimatkasse stellen: ärztliche Begründung, Behandlungsplan, Kostenvoranschlag
- Kasse genehmigt wenn Behandlung in Deutschland nicht zeitgerecht möglich (§ 20 VO 883/2004)
- Ablehnung: Widerspruch; BSG-Maßstab: unzumutbare Wartezeit im Inland
- S2 deckt Kosten ab, die im Gastland gesetzlich versicherte zahlen würden

### Schritt 3 – EU-Patientenrechterichtlinie (§ 140e SGB V)
- Recht auf Behandlung in jedem EU/EWR-Staat ohne S2-Genehmigung
- Erstattung: in Höhe der deutschen Kassenleistung (nicht mehr als im Inland)
- Kein Recht auf Erstattung über deutsches Leistungsniveau hinaus
- Antrag nach Behandlung mit Rechnungen, Arztberichten

### Schritt 4 – Nicht-EU-Ausland (§ 13 SGB V, § 18 SGB V)
- § 18 SGB V: Behandlung im Ausland wenn in Deutschland nicht oder nicht rechtzeitig möglich
- Sehr enge Voraussetzungen: Vorab-Genehmigung fast immer erforderlich
- Notfall: unverzügliche Notfallversorgung, Erstattung auf deutschem Kassenniveau

### Schritt 5 – Grenzgänger und entsandte Arbeitnehmer
- S1-Formular: für Grenzgänger, entsandte AN, Rentner die im Ausland wohnen
- Doppelter Leistungsanspruch möglich; Koordinierungsrecht beachten (skill kv-019)

## Typische Fallen

- **EHIC ≠ Reisekrankenversicherung**: EHIC deckt keinen Rücktransport, keine Repatriierung; separate Reisekrankenversicherung sinnvoll.
- **Eigenanteil im Gastland**: Zuzahlungen des Gastlandes sind vom Versicherten zu tragen, auch wenn im Inland befreit.
- **Nicht-kassenzugelassene Behandlung im EU-Ausland**: EU-Richtlinie deckt nur EU-Leistungen ab; experimentelle Therapien nicht erstattet.
- **Zahnbehandlung im Ausland**: Grundsätzlich erstattungsfähig nach EU-Richtlinie; aber nur bis deutschem Festzuschuss.

## Output-Formate

- S2-Antrag (Mustertext)
- Erstattungsantrag EU-Behandlung
- Widerspruch gegen S2-Ablehnung
- EHIC-Nutzungsanleitung
- Kostenvergleich: Ausland vs. Inland

## Quellen

- [§ 18 SGB V – Auslandsbehandlung](https://www.gesetze-im-internet.de/sgb_5/__18.html)
- [§ 140e SGB V – EU-Patientenrechte](https://www.gesetze-im-internet.de/sgb_5/__140e.html)
- [VO (EG) 883/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004R0883)
- [Richtlinie 2011/24/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32011L0024)
- [GKV-Spitzenverband Ausland](https://www.gkv-spitzenverband.de)
- [Europäische Kommission EHIC](https://ec.europa.eu/social/main.jsp?catId=559)
- [dejure.org § 18 SGB V](https://dejure.org/gesetze/SGB_V/18.html)

## 3. `kv-019-grenzgaenger-auslandskrankenversicherung-und-koordinierun`

**Fokus:** Krankenversicherungsrecht für Grenzgänger, EU-Koordinierungsverordnung 883/2004, S1-/S2-Formulare, Doppelversicherung und zuständige Träger.

# Grenzgänger, Auslandskrankenversicherung und Koordinierungsrecht

## Skill-Zweck

Dieser Skill bearbeitet **komplexe grenzüberschreitende Krankenversicherungssituationen**: Grenzgänger (wohnen in einem Land, arbeiten im anderen), entsandte Arbeitnehmer, EU-Koordinierungsrecht und Doppelversicherungsproblematik.

## Rechtlicher Rahmen

- **VO (EG) 883/2004** – Koordinierung der sozialen Sicherungssysteme der EU
- **VO (EG) 987/2009** – Durchführungsverordnung
- **Art. 11 VO 883/2004** – Grundsatz: nur ein Mitgliedstaat zuständig (lex loci laboris)
- **Art. 19 VO 883/2004** – Sachleistungen im Wohnmitgliedstaat für Beschäftigte
- **Art. 20 VO 883/2004** – Genehmigung geplanter Behandlung (S2-Formular)
- **S1-Formular** – Registrierung im Wohnstaat
- **§ 4 SGB IV** – Ausstrahlung (Entsendung, deutsches Recht bleibt anwendbar)
- **§ 5 SGB IV** – Einstrahlung (ausländischer AN kommt nach Deutschland)

## Grundprinzipien

| Prinzip | Inhalt |
|---------|--------|
| Beschäftigungslandprinzip | Versicherung im Land des Arbeitsplatzes (Art. 11 VO 883/2004) |
| Ausnahme Grenzgänger | Voller Leistungsanspruch im Wohnland (S1-Formular) |
| Entsendung | Bis 24 Monate: deutsches Recht bleibt anwendbar (Art. 12 VO 883/2004) |
| Gleichbehandlung | Ausländer haben gleiche Rechte wie Inländer im Beschäftigungsland |

## Prüfprogramm

### Schritt 1 – Welches Land ist zuständig?
- Beschäftigung in Deutschland → deutsches Recht (GKV oder PKV)
- Beschäftigung in EU-Ausland, Wohnsitz Deutschland → ausländisches System primär
- Entsendung: < 24 Monate → deutsches Recht beibehaltbar (A1-Bescheinigung erforderlich)
- Selbstständige: Wohnort-Prinzip gilt häufig; Art. 13 VO 883/2004

### Schritt 2 – S1-Formular für Grenzgänger
- Grenzgänger: Arbeit in EU-Land, Wohnsitz in anderem EU-Land
- S1 beim ausländischen Träger (Arbeitsstaat) beantragen
- Registrierung im Wohnstaat → volle Leistungen des Wohnstaates (Sachleistungsprinzip)
- Kasse in Deutschland als Anlaufstelle; Kostenabrechnung zwischen Trägern

### Schritt 3 – A1-Bescheinigung Entsendung
- A1 = Nachweis dass deutsches Sozialversicherungsrecht gilt
- Antrag: Arbeitgeber bei zuständigem Sozialversicherungsträger (GKV-Kasse)
- Fehlendes A1: Doppelversicherung im Ausland möglich; Bußgelder in manchen EU-Ländern
- Verlängerung nach 24 Monaten: Ausnahmevereinbarung notwendig

### Schritt 4 – Doppelversicherungsproblematik
- Nie zulässig: gleichzeitige Pflichtversicherung in zwei EU-Staaten
- Überprüfung: Verbindungsstellen der EU-Mitgliedstaaten
- Erstattung zu viel gezahlter Beiträge: § 26 SGB IV, ausländische Rechtsgrundlagen

### Schritt 5 – Nicht-EU-Ausland
- Bilaterale Sozialversicherungsabkommen (z.B. Deutschland-USA, Deutschland-Schweiz)
- Ohne Abkommen: kein gegenseitiger Leistungsanspruch; private Zusatzversicherung ratsam
- Auslandsentsendung in Nicht-Abkommensland: freiwillige Weiterversicherung in Deutschland prüfen

## Typische Fallen

- **Grenzgänger und Kassenwahl**: Grenzgänger in Deutschland wohnhaft aber in Frankreich arbeitend → Pflichtversicherung in Frankreich; Registrierung bei GKV-Kasse in Deutschland.
- **A1 vergessen**: Verursacht erhebliche administrative Probleme und Nachzahlungen.
- **Rente im Ausland**: Rentner, die im EU-Ausland leben, erhalten S1 vom deutschen Rentenversicherungsträger; Leistungen im Wohnstaat.
- **Schweiz**: EFZ-Abkommen; ähnlich EU-Koordinierungsrecht, aber spezifische bilaterale Regelungen.

## Output-Formate

- A1-Antrag (Muster)
- S1-Erklärungsschreiben
- Koordinierungsübersicht (Tabelle Zuständigkeit je Szenario)
- Doppelversicherungs-Überprüfungsantrag
- Beratungsschreiben Grenzgänger

## Quellen

- [VO (EG) 883/2004](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004R0883)
- [GKV-Spitzenverband EU-Koordinierung](https://www.gkv-spitzenverband.de)
- [§ 4 SGB IV – Ausstrahlung](https://www.gesetze-im-internet.de/sgb_4/__4.html)
- [Europäische Kommission Koordinierung](https://ec.europa.eu/social/main.jsp?catId=849)
- [Deutsche Verbindungsstelle Krankenversicherung – Ausland (DVKA)](https://www.dvka.de)
- [dejure.org SGB IV § 4](https://dejure.org/gesetze/SGB_IV/4.html)
