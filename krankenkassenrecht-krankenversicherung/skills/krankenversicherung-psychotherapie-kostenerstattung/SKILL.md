---
name: krankenversicherung-psychotherapie-kostenerstattung
description: "Psychotherapie Kostenerstattung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Psychotherapie Kostenerstattung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Psychotherapie Kostenerstattung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-014-psychotherapie-kostenerstattung-systemversagen-und-akutbe` | GKV-Psychotherapie: Richtlinienpsychotherapie, Systemversagen und Kostenerstattung privater Therapeuten, Akutbehandlung nach § 92 SGB V. |
| `kv-015-long-covid-post-vac-und-beweisprobleme` | Krankenversicherungsrechtliche Ansprüche bei Long Covid und Post-Vac-Syndrom: Leistungsansprüche, Beweisschwierigkeiten, MDK-Problematik und Kausalitätsfragen. |
| `kv-016-transidentitaet-geschlechtsangleichende-behandlung` | GKV-Leistungspflicht für geschlechtsangleichende Maßnahmen: Hormontherapie, operative Eingriffe, Diagnostik, MDK-Prüfung und aktuelle BSG-Rechtsprechung. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Psychotherapie Kostenerstattung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-014-psychotherapie-kostenerstattung-systemversagen-und-akutbe`

**Fokus:** GKV-Psychotherapie: Richtlinienpsychotherapie, Systemversagen und Kostenerstattung privater Therapeuten, Akutbehandlung nach § 92 SGB V.

# Psychotherapie: Kostenerstattung, Systemversagen und Akutbehandlung

## Skill-Zweck

Dieser Skill bearbeitet **GKV-Psychotherapieleistungen**: Anspruch auf Richtlinienpsychotherapie, die Systemversagen-Rechtsprechung des BSG bei Wartezeiten und die Kostenerstattung für Privattherapie.

## Rechtlicher Rahmen

- **§ 27 Abs. 1 SGB V** – Psychotherapie als Krankenbehandlung
- **§ 92 SGB V i.V.m. Psychotherapie-Richtlinie (PT-RL)** – G-BA-Richtlinie: Verfahren, Indikationen, Stundenkontingente
- **§ 13 Abs. 3 SGB V** – Kostenerstattung bei Systemversagen (Selbstbeschaffung)
- **§ 28 Abs. 3 SGB V** – Akutbehandlung durch Psychotherapeuten
- **§ 92 Abs. 6a SGB V** – Psychotherapeutische Sprechstunde
- **§ 73b SGB V** – Hausarztzentrierte Versorgung (Schnittstelle)
- BSG B 1 KR 6/14 R (Systemversagen), BSG B 1 KR 10/11 R (Wartezeit)
- BVerfG Beschl. v. 26.03.2019 – 1 BvR 673/17 (Zugang zu Psychotherapie)

## Psychotherapie-Systematik (PT-RL)

| Verfahren | Stundenkontingent GKV | Voraussetzung |
|-----------|----------------------|---------------|
| Verhaltenstherapie (VT) | Bis 80 h (Einzeltherapie) | Richtlinienindikation |
| Tiefenpsychologisch fundierte PT | Bis 100 h | Richtlinienindikation |
| Analytische PT | Bis 300 h | Richtlinienindikation |
| Systemische PT | Bis 48 h (seit 2020) | Richtlinienindikation |
| Akutbehandlung | 12 Sitzungen | Akute Notlage |

## Prüfprogramm

### Schritt 1 – Anspruch prüfen
- Indikation gemäß PT-RL (Depressionen, Angststörungen, PTBS, Persönlichkeitsstörungen etc.)?
- Therapeut mit Kassenzulassung? (Kassenzulassung = Zulassung zur vertragsärztlichen Versorgung)
- Probatorische Sitzungen (max. 4–8) vor Antragstellung absolviert?

### Schritt 2 – Systemversagen feststellen
- Kasse schuldet zeitnahe Versorgung; Wartezeit > 3 Monate gilt nach BSG als systemisches Versagen
- Dokumentation der Wartezeit: mindestens 5 erfolglose Anfragen bei Kassenzugelassenen Therapeuten dokumentieren
- Kasse auffordern, kassenärztliche Vereinigung einzuschalten (§ 75 Abs. 1 SGB V: KV-Sicherstellungsauftrag)

### Schritt 3 – Kostenerstattungsantrag (§ 13 Abs. 3 SGB V)
- Antrag bei Kasse: Systemversagen belegen, Privattherapeut benennen, Kosten vorlegen
- Kasse muss Kostenerstattung in Höhe des Kassensatzes zahlen (nicht GOÄ-Privatpreis)
- BSG B 1 KR 6/14 R: Erstattung muss auf Kassenleistungsniveau begrenzt sein

### Schritt 4 – Akutbehandlung (§ 28 Abs. 3 SGB V)
- Psychotherapeutische Sprechstunde: bis 6 Sitzungen ohne Antrag, Erstabklärung
- Akutbehandlung: 12 Sitzungen à 50 Minuten bei akuter Krise
- Kein Gutachterverfahren nötig; Therapeut entscheidet über Indikation

### Schritt 5 – Stationäre Psychotherapie
- Bei schwerer psychischer Erkrankung: stationäre/tagesklinische psychosomatische Behandlung
- § 39 SGB V: Krankenhausbehandlung bei stationärer Psychotherapie
- Psychiatrische Klinik vs. Psychosomatik: unterschiedliche Versorgungsstrukturen

## Typische Fallen

- **Kein Kassenzugelassener Therapeut gefunden**: Dokumentation der Suche essentiell; Kasse kann sonst Systemversagen ablehnen.
- **Probatorische Sitzungen beim Privattherapeuten**: Begründen keinen Anspruch auf Kostenerstattung; erst nach Systemversagensnachweis.
- **Gutachterverfahren**: Bei Kurzzeittherapie (bis 24 h) kein Gutachten; bei Langzeittherapie Therapeut stellt Antrag an Kasse.
- **Rezidivprophylaxe**: Neue Therapieepisode nach Ablauf der Sperrfrist möglich; kein automatisches neues Recht.

## Output-Formate

- Systemversagen-Dokumentationsbogen
- Kostenerstattungsantrag § 13 Abs. 3 SGB V
- Widerspruch gegen Ablehnungsbescheid
- KV-Beschwerdeschreiben (Sicherstellungsauftrag)
- Eilantrag SG (akute psychische Erkrankung)

## Quellen

- [§ 13 SGB V – Kostenerstattung](https://www.gesetze-im-internet.de/sgb_5/__13.html)
- [Psychotherapie-Richtlinie G-BA](https://www.g-ba.de/richtlinien/20/)
- [§ 28 SGB V – Akutbehandlung](https://www.gesetze-im-internet.de/sgb_5/__28.html)
- [BSG B 1 KR 6/14 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [BVerfG 1 BvR 673/17](https://www.bverfg.de/entscheidungen.html)
- [dejure.org § 13 SGB V](https://dejure.org/gesetze/SGB_V/13.html)
- [Kassenärztliche Bundesvereinigung PT](https://www.kbv.de/html/psychotherapie.php)

## 2. `kv-015-long-covid-post-vac-und-beweisprobleme`

**Fokus:** Krankenversicherungsrechtliche Ansprüche bei Long Covid und Post-Vac-Syndrom: Leistungsansprüche, Beweisschwierigkeiten, MDK-Problematik und Kausalitätsfragen.

# Long Covid, Post-Vac und Beweisprobleme

## Skill-Zweck

Long Covid und Post-Vac-Syndrom stellen **neue Beweisherausforderungen** im Krankenversicherungsrecht dar: fehlende Laborwerte, unklare Kausalität, skeptische MDK-Gutachten. Dieser Skill entwickelt Strategien zur Anspruchsdurchsetzung.

## Rechtlicher Rahmen

- **§ 27 SGB V** – Krankenbehandlungsanspruch (Anspruch auf Diagnostik und Therapie)
- **§ 44 SGB V** – Krankengeld (Arbeitsunfähigkeit bei Long Covid)
- **§ 33 SGB V** – Hilfsmittel (z.B. bei Fatigue: Rollator, Gehhilfe)
- **§ 40 SGB V** – Reha-Leistungen
- **§ 2 Abs. 1a SGB V** – Grundrechtsorientierte Auslegung bei lebensbedrohlichen Erkrankungen
- **§ 275 SGB V** – MDK-Prüfung (kritisch zu begleiten)
- WHO-Definition Long Covid (Oktober 2021), S1-Leitlinie Long COVID (AWMF 020-027)
- BSG-Grundsätze zur Kausalitätslehre im Sozialrecht: Vollbeweis der Erkrankung, Wahrscheinlichkeit des Kausalzusammenhangs
- OEG § 1 (Post-Vac als Impfschaden, ggf. Versorgungsamt)

## Beweisrechtliche Grundlagen

| Beweisstandard | Inhalt |
|---------------|--------|
| Vollbeweis | Erkrankung muss mit an Sicherheit grenzender Wahrscheinlichkeit vorliegen |
| Wahrscheinlichkeitsmaßstab | Kausalzusammenhang: mehr Gründe sprechen dafür als dagegen |
| Glaubhaftmachung | Nur im einstweiligen Rechtsschutz ausreichend |
| Non-liquet | Beweislast beim Anspruchsteller; Ausnahmen bei Beweisnot |

## Prüfprogramm

### Schritt 1 – Diagnose und Dokumentation
- ICD-10: U09.9 (Post-Covid-Zustand), U12.9 (Unerwünschte Wirkung Impfstoff)
- Ärztliche Dokumentation: Vorgeschichte (positiver Test), Symptomverlauf, Ausschlussdiagnostik
- Befundberichte: Erschöpfungssymptomatik (Fatigue), kognitive Störungen, Dyspnoe, Schmerzen
- CPET (Spiroergometrie), Tilt-Table-Test, neuropsychologische Testung als Objektivierungsbausteine

### Schritt 2 – Leistungsansprüche identifizieren
- Krankenbehandlung (§ 27): Diagnostik, Medikamente (auch Off-Label bei fehlenden Zulassungen)
- Krankengeld: Arbeitsunfähigkeit durch Long Covid, Blockfrist 78 Wochen beachten
- Hilfsmittel: bei Mobilitätseinschränkung oder Fatigue
- Reha (§ 40): Long-Covid-Rehaprogramme; Rentenversicherung häufig federführend

### Schritt 3 – MDK-Gutachten begleiten
- MDK-Gutachten häufig skeptisch bei unsichtbaren Symptomen
- Gegengutachten durch Spezialambulanz (Uniklinik Long Covid-Ambulanz)
- Akteneinsicht: MDK-Gutachten und -Unterlagen anfordern (§ 25 SGB X)
- Sachverständigen im Sozialgerichtsverfahren beantragen

### Schritt 4 – Post-Vac und Impfschaden
- Rechtsgrundlage Impfschaden: § 60 IfSG, OEG-Entschädigung
- Zuständig: Versorgungsamt (Landesversorgungsamt), nicht GKV
- GKV bleibt für Behandlung zuständig; Schaden wird über Versorgungsrecht erstattet
- Beweisschwierigkeiten noch ausgeprägter als bei Long Covid

### Schritt 5 – Eilverfahren bei akuter Not
- Krankengeld-Einstellung während Long Covid → Eilantrag SG § 86b SGG
- Reha-Verweigerung → einstweilige Anordnung

## Typische Fallen

- **Fehldiagnose Depression**: MDK wertet Long Covid-Fatigue als psychisch; richtige Diagnose und Abgrenzung wichtig.
- **Blockfrist Krankengeld**: 78 Wochen können erschöpft sein; Übergangsgeld Reha als Alternative prüfen.
- **Impfschaden vs. Long Covid**: Andere Rechtsträger (Versorgungsamt vs. GKV); Doppelantragstellung empfehlen.
- **Beweissicherung versäumt**: Symptomtagebuch, Arztbriefe sichern, Krankheitsverlauf dokumentieren.

## Output-Formate

- Dokumentationsleitfaden für Betroffene
- Widerspruch gegen Krankengeldeinstellung
- MDK-Gegengutachten-Briefing
- Eilantrag SG (Mustertext)
- Übersicht Leistungsträger Long Covid

## Quellen

- [§ 27 SGB V – Krankenbehandlung](https://www.gesetze-im-internet.de/sgb_5/__27.html)
- [§ 44 SGB V – Krankengeld](https://www.gesetze-im-internet.de/sgb_5/__44.html)
- [S1-Leitlinie Long COVID (AWMF)](https://www.awmf.org/leitlinien/detail/ll/020-027.html)
- [§ 60 IfSG – Impfschaden](https://www.gesetze-im-internet.de/ifsg/__60.html)
- [BSG Kausalitätslehre](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 44 SGB V](https://dejure.org/gesetze/SGB_V/44.html)
- [WHO Long Covid Definition](https://www.who.int/publications/i/item/9789240025035)

## 3. `kv-016-transidentitaet-geschlechtsangleichende-behandlung`

**Fokus:** GKV-Leistungspflicht für geschlechtsangleichende Maßnahmen: Hormontherapie, operative Eingriffe, Diagnostik, MDK-Prüfung und aktuelle BSG-Rechtsprechung.

# Transidentität: Geschlechtsangleichende Behandlung

## Skill-Zweck

Dieser Skill bearbeitet **GKV-Leistungsansprüche für transidente Personen**: Hormontherapie, Epithesenversorgung, operative Eingriffe zur Geschlechtsangleichung und zugehörige Diagnostik.

## Rechtlicher Rahmen

- **§ 27 SGB V** – Krankenbehandlung (Transidentität als Erkrankung anerkannt)
- **§ 11 Abs. 1 Nr. 4 SGB V** – Anspruch auf Krankenbehandlung einschließlich operativer Maßnahmen
- **§ 33 SGB V** – Hilfsmittel (Epithesen, Prothesen)
- **§ 12 SGB V** – Wirtschaftlichkeitsgebot
- **§ 275 SGB V** – MDK-Begutachtung
- BSG B 1 KR 14/12 R (Transidentität, Krankenbehandlung), BSG B 1 KR 31/15 R (operative Maßnahmen)
- BVerfG 1 BvR 2556/15 (Grundrecht auf Selbstbestimmung)
- ICD-11 HA60 (Geschlechtsinkongruenz, seit 2022 nicht mehr als psychische Störung klassifiziert)
- AWMF S3-Leitlinie Geschlechtsinkongruenz/Transsexualismus

## Leistungsübersicht GKV

| Leistung | Anspruchsgrundlage | MDK-Erfordernis |
|---------|-------------------|-----------------|
| Hormontherapie | § 27 SGB V | Ärztliche Verordnung; kein MDK erforderlich |
| Mastektomie/Brustaufbau | § 27 SGB V i.V.m. § 12 | MDK-Gutachten |
| Genitalangleichung | § 27 SGB V | MDK-Gutachten, Leitlinie |
| Stimmtherapie | § 32 SGB V (Heilmittel) | Verordnung |
| Epithesen (Brust, genital) | § 33 SGB V | Hilfsmittelantrag |
| Psychotherapeutische Begleitung | § 27 i.V.m. PT-RL | Regelverfahren |

## Prüfprogramm

### Schritt 1 – Diagnose und Behandlungsplanung
- Diagnose ICD-11 HA60 (Geschlechtsinkongruenz) oder ICD-10 F64.0 (Transsexualismus, bis 2024)
- Diagnostik durch qualifizierten Facharzt (Psychiatrie, Psychosomatik, Endokrinologie)
- AWMF S3-Leitlinie als Behandlungsmaßstab: Real-Life-Experience, Mindestdauer etc.

### Schritt 2 – Hormontherapie beantragen
- Verordnung durch Endokrinologen oder Gynäkologen/Urologen
- Kostenübernahme: GKV zahlt Standardhormone; Off-Label-Präparate gesondert prüfen
- MDK-Einschaltung bei strittigen Fällen; Gegengutachten vorbereiten

### Schritt 3 – Operative Maßnahmen
- Kostenantrag mit ärztlichem Befundbericht, Diagnostik, Leitlinien-Konformitätsnachweis
- MDK prüft: medizinische Notwendigkeit, Ausschlussdiagnostik, Leitlinienkonformität
- BSG-Maßstab: nicht Heilung, sondern Behandlung der Erkrankung (Transidentität ist Erkrankung)
- Bei Ablehnung: Widerspruch mit psychiatrischem/endokrinologischem Gegengutachten

### Schritt 4 – Aktueller Rechtszustand (ICD-11)
- ICD-11 HA60: Entpathologisierung; keine psychische Störung mehr
- Auswirkung auf GKV: BSG und Kassen müssen anpassen; Krankheitsbegriff § 27 SGB V weiter erfüllt
- Übergangsrechtsprechung beobachten

### Schritt 5 – Diskriminierungsschutz
- AGG § 1: Diskriminierung wegen Geschlechtsidentität verboten
- Kasse darf nicht anders behandeln als cisgender Versicherte mit vergleichbarer medizinischer Indikation

## Typische Fallen

- **Real-Life-Experience veraltet**: Aktuelle Leitlinie sieht nicht mehr verpflichtende Real-Life-Phase vor; MDK-Anforderungen entsprechend angreifen.
- **Epilator/Laser-Haarentfernung**: Umstrittene Kassenleistung; BGH und BSG unterschiedlich; Antrag stellen und dokumentieren.
- **Stimmbandoperation**: Kassenleistung nur bei medizinischer Indikation; reine Klangveränderung umstritten.
- **Minderjährige**: Besondere Voraussetzungen, elterliche Zustimmung, Kinderpsychiatrische Abklärung.

## Output-Formate

- Antragsschreiben operative Maßnahmen
- Widerspruch gegen MDK-gestützte Ablehnung
- Gegengutachten-Briefing für Arzt
- Akteneinsichtsantrag MDK
- Übersicht GKV-Leistungen Transidentität

## Quellen

- [§ 27 SGB V – Krankenbehandlung](https://www.gesetze-im-internet.de/sgb_5/__27.html)
- [BSG B 1 KR 14/12 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [AWMF S3-Leitlinie Geschlechtsinkongruenz](https://www.awmf.org/leitlinien/detail/ll/138-001.html)
- [BVerfG 1 BvR 2556/15](https://www.bverfg.de/entscheidungen.html)
- [dejure.org § 27 SGB V](https://dejure.org/gesetze/SGB_V/27.html)
- [G-BA Richtlinien](https://www.g-ba.de/richtlinien/)
- [ICD-11 WHO](https://icd.who.int/browse11)
