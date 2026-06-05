---
name: krankenversicherung-haushaltshilfe-fahrkosten-besondere
description: "Haushaltshilfe Fahrkosten Besondere: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Haushaltshilfe Fahrkosten Besondere

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Haushaltshilfe Fahrkosten Besondere** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-011-haushaltshilfe-fahrkosten-und-besondere-lebenslagen` | GKV-Leistungen für Haushaltshilfe (§ 38 SGB V), Fahrkosten (§ 60 SGB V) und besondere Lebenslagen: Anspruchsvoraussetzungen, Genehmigung und Widerspruch. |
| `kv-012-zahnersatz-heil-und-kostenplan-bonusheft-festzuschuss` | Zahnersatzversorgung in der GKV: Heil- und Kostenplan, Regelversorgung, Festzuschuss, Bonusheft-Regelungen und Mehrkosten bei Privatleistungen. |
| `kv-013-kinderleistungen-sozialpaediatrie-therapie-und-schulbegle` | Krankenversicherungsleistungen für Kinder: sozialpädiatrische Zentren, Therapien, Schulbegleitung – Abgrenzung GKV, Eingliederungshilfe (SGB IX/SGB XII), Schnittstellen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Haushaltshilfe Fahrkosten Besondere**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-011-haushaltshilfe-fahrkosten-und-besondere-lebenslagen`

**Fokus:** GKV-Leistungen für Haushaltshilfe (§ 38 SGB V), Fahrkosten (§ 60 SGB V) und besondere Lebenslagen: Anspruchsvoraussetzungen, Genehmigung und Widerspruch.

# Haushaltshilfe, Fahrkosten und besondere Lebenslagen

## Skill-Zweck

Dieser Skill bearbeitet **ergänzende GKV-Leistungen** neben der Krankenbehandlung: Haushaltshilfe bei Krankenhausaufenthalt oder ambulanter Behandlung sowie Fahrkostenerstattung. Beide Leistungen werden häufig abgelehnt, obwohl die rechtlichen Voraussetzungen vorliegen.

## Rechtlicher Rahmen

- **§ 38 SGB V** – Haushaltshilfe: bei stationärer Behandlung oder Behandlung mit Haushalt, minderjähriges Kind vorhanden
- **§ 60 SGB V** – Fahrkosten: medizinisch notwendiger Transport zur Behandlung
- **§ 61 SGB V** – Zuzahlungsregeln Fahrkosten
- **§ 62 SGB V** – Belastungsgrenze (2 %/1 % des Bruttoeinkommens)
- **Krankentransport-Richtlinie des G-BA** (KT-RL)
- BSG B 1 KR 4/20 R (Fahrkosten, Notwendigkeit), BSG B 3 KR 5/17 R (Haushaltshilfe)

## Haushaltshilfe – Prüfschema

| Voraussetzung | Inhalt |
|--------------|--------|
| Hauswirtschaftliche Versorgung | Versicherter kann Haushalt nicht führen (Krankheit, Behandlung) |
| Minderjähriges Kind | Kind unter 12 oder mit Behinderung im Haushalt |
| Niemand sonst kann versorgen | Keine Person im Haushalt die Haushaltsführung übernehmen kann |
| Stationäre oder ambulante Behandlung | § 38 Abs. 1 und 2 SGB V |

## Fahrkosten – Prüfschema

| Fahrttyp | Voraussetzung | Genehmigung |
|----------|--------------|-------------|
| Krankenfahrt mit KTW/RTW | Medizinische Notwendigkeit des Fahrzeugs | Ja, vorab oder Notfall |
| Krankenfahrt mit Taxi | Gehdauer > 2 km oder Fahruntüchtigkeit | Genehmigung KT-RL |
| PKW-Fahrt | Ausnahmsweise bei Pflegegrad 3–5, Schwerbehinderten | Vorab-Genehmigung |
| Öffentliche Verkehrsmittel | Kein Anspruch auf Erstattung bei Zumutbarkeit | – |

## Prüfprogramm

### Schritt 1 – Haushaltshilfe (§ 38 SGB V)
- Stationärer Aufenthalt oder ambulante Behandlung mit Haushaltsunfähigkeit?
- Minderjähriges Kind unter 12 im Haushalt? Oder Kind mit Behinderung ohne Altersgrenze?
- Keine andere Person im Haushalt die einspringen kann?
- Antrag bei Kasse mit ärztlichem Attest und Erklärung über Haushaltsmitglieder

### Schritt 2 – Fahrkosten (§ 60 SGB V)
- Schritt A: Ist Transport überhaupt erforderlich? (kein eigenständiges Gehen möglich)
- Schritt B: Welches Beförderungsmittel ist medizinisch notwendig und wirtschaftlich?
- Schritt C: Genehmigung vorab bei Kasse oder Arztentscheidung (Notfall)?
- Zuzahlung: 10 % je Fahrt, mind. 5 €, max. 10 €, Belastungsgrenze beachten

### Schritt 3 – Besondere Lebenslagen
- Schwangerschaft/Geburt: Haushaltshilfe nach § 24h SGB V (ohne Alterserfordernis)
- Pflegegrade: Schnittstelle § 36 SGB XI (Pflegesachleistung) vs. § 38 SGB V
- Onkologische Behandlung: G-BA-Kriterien für Langzeit-Fahrkosten

### Schritt 4 – Widerspruchsstrategie
- Ablehnung Haushaltshilfe: fehlende andere Versorgungsperson dokumentieren; eidesstattliche Erklärung möglich
- Ablehnung Fahrkosten: ärztliche Bescheinigung medizinische Notwendigkeit des Transports, Nachweis Fahruntüchtigkeit

## Typische Fallen

- **Haushaltshilfe und erwachsene Kinder**: Erwachsene Kinder im Haushalt werden als Versorgungsperson gewertet – explizit klarstellen wenn diese berufstätig/nicht verfügbar sind.
- **Taxi vs. KTW**: Taxifahrt braucht eigene Genehmigung; KTW-Fahrt zusätzliche medizinische Begründung (Liegendtransport etc.).
- **Eigenständige PKW-Fahrt**: Kasse erstattet nur bei spezifischen Ausnahmen (§ 60 Abs. 2 SGB V); allgemeiner Führerscheinbesitz schließt Anspruch nicht aus wenn medizinische Begründung vorliegt.
- **Rückwirkend**: Fahrkosten können rückwirkend geltend gemacht werden, Verjährung 4 Jahre.

## Output-Formate

- Haushaltshilfe-Antrag mit Mustertext
- Fahrkostenerstattungsantrag
- Widerspruch gegen Ablehnung
- Fahrtenbuch (Nachweis)
- Belastungsgrenze-Berechnung

## Quellen

- [§ 38 SGB V – Haushaltshilfe](https://www.gesetze-im-internet.de/sgb_5/__38.html)
- [§ 60 SGB V – Fahrkosten](https://www.gesetze-im-internet.de/sgb_5/__60.html)
- [Krankentransport-Richtlinie G-BA](https://www.g-ba.de/richtlinien/33/)
- [§ 62 SGB V – Belastungsgrenze](https://www.gesetze-im-internet.de/sgb_5/__62.html)
- [BSG Entscheidungssuche](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 60 SGB V](https://dejure.org/gesetze/SGB_V/60.html)

## 2. `kv-012-zahnersatz-heil-und-kostenplan-bonusheft-festzuschuss`

**Fokus:** Zahnersatzversorgung in der GKV: Heil- und Kostenplan, Regelversorgung, Festzuschuss, Bonusheft-Regelungen und Mehrkosten bei Privatleistungen.

# Zahnersatz: Heil- und Kostenplan, Bonusheft, Festzuschuss

## Skill-Zweck

Dieser Skill klärt **Zahnersatzversorgung** in der GKV: Welche Leistung schuldet die Kasse, wie funktioniert der Festzuschuss, wie wirkt das Bonusheft und wann entstehen Mehrkosten für den Versicherten?

## Rechtlicher Rahmen

- **§ 55 SGB V** – Zahnersatz-Anspruch (Regelversorgung)
- **§ 56 SGB V** – Befundorientierte Festzuschüsse
- **§ 57 SGB V** – Eigenanteil und Kostentragung
- **§ 55 Abs. 2 SGB V** – Erhöhung des Festzuschusses bei langjährigem Bonusheft
- **§ 92 SGB V** – G-BA: Zahnersatz-Richtlinie (ZE-RL)
- **Zahnersatz-Richtlinie G-BA** (ZE-RL): Befundbeschreibungen und Regelversorgungen
- **GOZ** (Gebührenordnung Zahnärzte) §§ 1–12 für Privatleistungen
- BSG B 1 KR 11/14 R (Zahnersatz, Regelversorgung)

## Festzuschuss-Systematik

| Bonusheft-Status | Festzuschuss-Erhöhung |
|-----------------|----------------------|
| Kein Bonusheft | Basisfestzuschuss (50 % der Regelversorgungskosten) |
| 5 Jahre regelmäßig | Erhöhung auf 60 % |
| 10 Jahre regelmäßig | Erhöhung auf 65 % |
| Sozialhilfe/Grundsicherung | 100 % (§ 55 Abs. 2 SGB V) |

## Prüfprogramm

### Schritt 1 – Befund und Regelversorgung
- Heil- und Kostenplan (HKP) vom Zahnarzt: liegt er vor, von Kasse genehmigt?
- Befund gemäß ZE-RL: welcher Befund (z.B. B1–B6), welche Regelversorgung ist zugeordnet?
- Kasse muss Festzuschuss für Regelversorgung zahlen; Mehr-/Andersversorgung auf Kosten des Patienten

### Schritt 2 – Bonusheft prüfen
- Mindestens 1 Untersuchung/Jahr lückenlos dokumentiert?
- 5 Jahre: ab Bescheidung Anspruch auf erhöhten Festzuschuss
- Lücke im Bonusheft: Erhöhung verfällt; Kulanzantrag möglich
- Bonusheft-Nachweise: Zahnarztpraxis-Bestätigung, altes Zahnersatz-Bonusheft

### Schritt 3 – Gleichartige/Andersartige Versorgung
- Gleichartig: gleiche Funktion wie Regelversorgung, aber anderen Material/Technik → Festzuschuss wie Regelversorgung, Mehrkosten privat
- Andersartig: Implantat statt Brücke → kein Festzuschuss der Kasse (außer Ausnahmefälle)
- Ausnahme Implantat: G-BA kann in Einzelfällen zulassen (seltene Indikationen)

### Schritt 4 – Wirtschaftlichkeitsprüfung und Genehmigung
- HKP muss vor Behandlungsbeginn genehmigt sein (Ausnahme: Notfall)
- Kasse prüft Wirtschaftlichkeit; MDZ (Zahnärztlicher Dienst) kann eingeschaltet werden
- Ablehnung: Widerspruch mit zahnärztlicher Stellungnahme

### Schritt 5 – Sozialtarif und Härtefälle
- Sozialhilfe, Grundsicherung: Kasse übernimmt Eigenanteil → 100 % der Regelversorgung
- Antrag: Nachweis über SGB II/XII-Bezug, Attest, HKP

## Typische Fallen

- **HKP-Genehmigungsfehler**: Behandlung vor Genehmigung → Kasse kann Festzuschuss verweigern.
- **Bonusheft-Lücke durch Umzug/Arztwechsel**: Lücke entsteht oft; frühzeitig nachweisen oder Kulanzantrag.
- **Implantat als Standardversorgung**: Kasse zahlt in der Regel keinen Festzuschuss für Implantate; Ausnahmen sehr eng.
- **Mehrwertsteuer im HKP**: Zahntechniker-Laborkosten mit MwSt.; Kasse übernimmt anteilig; Kontrolle der Aufschlüsselung.

## Output-Formate

- HKP-Checkliste (vor Einreichung)
- Festzuschuss-Berechnung
- Widerspruch gegen HKP-Ablehnung
- Bonusheft-Rekonstruktionsantrag
- Antrag auf Härtefallregelung (Sozialtarif)

## Quellen

- [§ 55 SGB V – Zahnersatz](https://www.gesetze-im-internet.de/sgb_5/__55.html)
- [§ 56 SGB V – Festzuschüsse](https://www.gesetze-im-internet.de/sgb_5/__56.html)
- [Zahnersatz-Richtlinie G-BA](https://www.g-ba.de/richtlinien/23/)
- [GKV-Spitzenverband Zahnersatz](https://www.gkv-spitzenverband.de)
- [BSG Zahnersatzrecht](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 55 SGB V](https://dejure.org/gesetze/SGB_V/55.html)

## 3. `kv-013-kinderleistungen-sozialpaediatrie-therapie-und-schulbegle`

**Fokus:** Krankenversicherungsleistungen für Kinder: sozialpädiatrische Zentren, Therapien, Schulbegleitung – Abgrenzung GKV, Eingliederungshilfe (SGB IX/SGB XII), Schnittstellen.

# Kinderleistungen: Sozialpädiatrie, Therapie und Schulbegleitung

## Skill-Zweck

Kinder mit Entwicklungsstörungen, Behinderungen oder chronischen Erkrankungen benötigen oft komplexe Versorgung. Dieser Skill klärt **welche Leistungen die Krankenkasse schuldet** – und wo die Abgrenzung zu Eingliederungshilfe, Schule und Jugendhilfe liegt.

## Rechtlicher Rahmen

- **§ 43a SGB V** – Sozialpädiatrische Zentren (SPZ): Frühförderung, Diagnostik
- **§ 30 SGB V** – Krankenhausbehandlung für Kinder und Jugendliche
- **§ 32 SGB V** – Heilmittel: Ergo-, Logo-, Physiotherapie für Kinder
- **§ 37 SGB V** – Häusliche Krankenpflege, auch bei Kindern
- **§ 2 SGB IX** – Behinderungsbegriff, ICF-orientiert
- **§ 112 SGB IX** – Schulbegleitung als Eingliederungshilfe (nach SGB IX Teil 2)
- **§ 35a SGB VIII** – Eingliederungshilfe Jugendhilfe (seelische Behinderung)
- **Frühförderungs-VO** – Komplexleistung Frühförderung (GKV + Eingliederungshilfe)
- BSG B 3 KR 6/14 R (SPZ-Leistungen), BSG B 8 SO 23/17 R (Schulbegleitung)

## Leistungsabgrenzung

| Leistung | Rechtsträger | Rechtsgrundlage |
|---------|-------------|-----------------|
| Sozialpädiatrisches Zentrum (SPZ) | GKV | § 43a SGB V |
| Frühförderung (unter 6 J.) | GKV + Eingliederungshilfe (Komplexleistung) | Frühförderungs-VO |
| Schulbegleitung | Eingliederungshilfe (Landkreis/Stadt) | § 112 SGB IX |
| Logopädie, Ergo, PT | GKV | § 32 SGB V |
| Schulkindergarten/Förderschule | Land/Schulträger | Schulrecht |
| Psychotherapie | GKV | § 27 Abs. 1, § 92 SGB V |

## Prüfprogramm

### Schritt 1 – SPZ-Versorgung (§ 43a SGB V)
- SPZ durch Krankenkasse zu genehmigen
- Indikation: geistige Entwicklungsstörung, Zerebralparese, Autismus-Spektrum-Störung, ADHS (schwer)
- Ärztliche Überweisung durch Kinder- und Jugendarzt oder Kinderpsychiater
- Wartezeiten SPZ: oft 12–24 Monate; einstweiliger Rechtsschutz bei dringendem Bedarf

### Schritt 2 – Frühförderung (Frühförderungs-VO)
- Kind unter 6 Jahre
- Komplexleistung: GKV übernimmt medizinisch-therapeutische Anteile; Eingliederungshilfe übernimmt pädagogische Anteile
- Antrag beim örtlichen Frühförderzentrum oder Jugendamt

### Schritt 3 – Heilmittel für Kinder (§ 32 SGB V)
- Grundsätzlich gleiche Voraussetzungen wie bei Erwachsenen (Heilmittel-RL)
- Bei Kindern: Verordnungsmengen häufig höher; besonderer Verordnungsbedarf für chronische Verläufe
- Langfristversorgung: Antrag bei Kasse bis 4 Wochen vor Ablauf

### Schritt 4 – Schulbegleitung (§ 112 SGB IX)
- GKV ist NICHT zuständig für Schulbegleitung (außer in sehr engen Ausnahmen)
- Zuständig: Eingliederungshilfeträger (Landkreis/kreisfreie Stadt)
- Antrag beim Sozialamt, Jugendamt (§ 35a SGB VIII bei seelischer Behinderung) oder Schulamt
- Abgrenzung: rein pflegerische Maßnahmen in Schule können GKV-Leistung sein (§ 37 SGB V)

### Schritt 5 – Psychotherapie für Kinder
- Kinder und Jugendlichenpsychotherapeut: GKV-Kassenzulassung erforderlich
- ADHS: Diagnose, Ausschlussdiagnostik, Leitliniengerechte Behandlung
- Systemisches Versagen: § 13 Abs. 3 SGB V wenn kein Kassentherapeut innerhalb vertretbarer Frist verfügbar

## Typische Fallen

- **Schulbegleitung bei GKV beantragen**: GKV lehnt rechtmäßig ab; Antrag muss beim Eingliederungshilfeträger gestellt werden.
- **Frühförderungs-Komplexleistung**: Oft unklar wer federführend ist; Frühförderstelle koordiniert, nicht GKV direkt.
- **SPZ-Kapazität erschöpft**: Kasse muss auf Veranlassung des Arztes prüfen ob Alternativversorgung möglich; einstweiliger Rechtsschutz.
- **Psychotherapie-Warteliste**: Systemversagen bei > 3 Monaten Wartezeit → Kostenerstattung Privattherapeut möglich (BSG).

## Output-Formate

- SPZ-Antrag mit Begründung
- Widerspruch gegen Heilmittelablehnung bei Kind
- Schulbegleitungsantrag (Eingliederungshilfe, Muster)
- Systemversagen-Schreiben (Psychotherapie)
- Übersicht Zuständigkeiten (Tabelle)

## Quellen

- [§ 43a SGB V – Sozialpädiatrisches Zentrum](https://www.gesetze-im-internet.de/sgb_5/__43a.html)
- [§ 112 SGB IX – Schulbegleitung](https://www.gesetze-im-internet.de/sgb_9_2018/__112.html)
- [Frühförderungs-VO](https://www.gesetze-im-internet.de/fruehfoerdv/)
- [§ 35a SGB VIII – Jugendhilfe](https://www.gesetze-im-internet.de/sgb_8/__35a.html)
- [BSG Kinderleistungen](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [G-BA Heilmittel-Richtlinie](https://www.g-ba.de/richtlinien/12/)
