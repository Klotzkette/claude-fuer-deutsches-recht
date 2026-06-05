---
name: krankenversicherung-selbstbehalt-wahltarif-kuendigung
description: "Selbstbehalt Wahltarif Kuendigung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Selbstbehalt Wahltarif Kuendigung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Selbstbehalt Wahltarif Kuendigung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-059-selbstbehalt-wahltarif-und-kuendigung` | Wahltarife mit Selbstbehalt nach § 53 SGB V: Funktionsweise, Kündigung, Rückforderungsrisiko bei vorzeitigem Austritt und Interaktion mit anderen Leistungen. |
| `kv-060-beitragsbemessung-kapitalauszahlung-betriebsrente` | GKV-Beitragspflicht für Betriebsrenten und Kapitalzahlungen aus betrieblicher Altersversorgung: § 229 SGB V, BSG-Rechtsprechung und Doppelverbeitragung. |
| `kv-061-versorgungsbezuege-und-doppelverbeitragung` | Kritische Analyse der Doppelverbeitragung von Betriebsrenten in der GKV: Rechtslage, Reform 2020, Freibetrag, laufende Verfahren und Gestaltungsoptionen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Selbstbehalt Wahltarif Kuendigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-059-selbstbehalt-wahltarif-und-kuendigung`

**Fokus:** Wahltarife mit Selbstbehalt nach § 53 SGB V: Funktionsweise, Kündigung, Rückforderungsrisiko bei vorzeitigem Austritt und Interaktion mit anderen Leistungen.

# Selbstbehalt-Wahltarif und Kündigung

## Skill-Zweck

Selbstbehalt-Wahltarife bieten niedrigere Beiträge gegen einen Eigenanteil bei Leistungen. Dieser Skill klärt **Funktionsweise, 3-Jahres-Bindung, Kündigungsrechte und Rückforderungsrisiken bei Austritt**.

## Rechtlicher Rahmen

- **§ 53 Abs. 1 SGB V** – Selbstbehalt-Wahltarif: Eigenanteil, Beitragsrückerstattung
- **§ 53 Abs. 8 SGB V** – Bindungsfrist: 3 Jahre (Ausnahme: Kassenwechsel aus besonderem Grund)
- **§ 175 Abs. 4 SGB V** – Kündigung bei Beitragserhöhung (Sonderkündigungsrecht)
- **§ 53 Abs. 9 SGB V** – Rückforderungsrecht der Kasse bei vorzeitigem Austritt
- BSG B 1 KR 14/17 R (Wahltarife, Rückforderung und Bindungsfrist)

## Selbstbehalt-Tarif-Systematik

| Element | Inhalt |
|---------|--------|
| Selbstbehalt | Versicherter trägt erste X € der Kosten selbst (z.B. 300–900 €/Jahr) |
| Beitragsrabatt | Kasse reduziert Monatsbeitrag (z.B. um 10–15 %) |
| Break-even | Kassen-Ersparnis vs. Eigenkosten; sinnvoll wenn selten krank |
| Bindung | 3 Jahre ab Wahltarif-Wahl; keine ordentliche Kündigung |
| Rückforderung | Kasse kann bei vorzeitigem Austritt erhaltene Rabatte zurückfordern |

## Prüfprogramm

### Schritt 1 – Wahltarif-Analyse
- Wie hoch ist der Selbstbehalt? Welche Leistungen sind einbezogen?
- Welchen Rabatt gibt die Kasse? Lohnt sich der Tarif bei guter Gesundheit?
- Mindestbindung: 3 Jahre ab Eintritt in den Tarif

### Schritt 2 – Bindungsfrist und Kündigung
- Innerhalb der 3 Jahre: keine ordentliche Kündigung möglich
- Ausnahme Sonderkündigungsrecht: Beitragserhöhung der Kasse → Kündigung auch aus Wahltarif + Kasse
- Sonderkündigungsrecht gilt auch für Wahltarif allein (ohne Kassenwechsel) wenn Tarif sich nachteilig ändert

### Schritt 3 – Rückforderungsrisiko (§ 53 Abs. 9 SGB V)
- Wenn Versicherter Kasse wechselt vor Ablauf der 3 Jahre: Kasse kann Rabatte zurückfordern
- Höhe: abhängig von Tarif und verbleibender Laufzeit
- Zulässig nur wenn Versicherter selbst kündigt; nicht bei Kassenschließung

### Schritt 4 – Wechselwirkung mit Leistungsansprüchen
- Selbstbehalt: Versicherter trägt Kosten bis Schwellenwert selbst; GKV-Leistung greift erst danach
- Chronisch Kranke: Selbstbehalt-Tarif selten sinnvoll (hohe Eigenkosten)
- Zuzahlungsbefreiung und Selbstbehalt: Belastungsgrenze (§ 62 SGB V) beachten

### Schritt 5 – Interaktion mit anderen Tarifen
- Beitragsrückgewähr-Tarif: kein Anspruch wenn Selbstbehalt-Tarif und Leistung in Anspruch genommen
- Kostenerstattungstarif: neben Selbstbehalt möglich, aber selten kombiniert
- Hausarzttarif: oft kombinierbar mit Selbstbehalt-Tarif

## Typische Fallen

- **Kündigung nicht möglich**: Versicherter glaubt nach Kassenwechsel aus Wahltarif entlassen zu sein → Kasse fordert Rabatt zurück.
- **Chronische Erkrankung neu diagnostiziert**: Selbstbehalt belastet zusätzlich zum Stressfaktor der Erkrankung.
- **Sonderkündigungsrecht nicht genutzt**: Beitragserhöhung verpasst → Sonderkündigungsfrist verstrichen.
- **Kinder und Selbstbehalt**: Selbstbehalt gilt für Hauptmitglied; Kinder beitragsfrei in Familienversicherung; Selbstbehalt berührt Kinderleistungen nicht.

## Output-Formate

- Selbstbehalt-Tarif-Kalkulation (Break-even-Analyse)
- Sonderkündigung Wahltarif (Muster)
- Rückforderungs-Widerspruch (Kasse)
- Tariflaufzeit-Übersicht
- Kündigung Kasse + Wahltarif kombiniert

## Quellen

- [§ 53 SGB V – Wahltarife](https://www.gesetze-im-internet.de/sgb_5/__53.html)
- [§ 175 SGB V – Kassenwahlrecht](https://www.gesetze-im-internet.de/sgb_5/__175.html)
- [BSG B 1 KR 14/17 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 53 SGB V](https://dejure.org/gesetze/SGB_V/53.html)
- [GKV-Spitzenverband Wahltarife](https://www.gkv-spitzenverband.de)
## Hinweis: Prämienrückgewähr und Steuerrecht

- Prämienrückgewähr bei Inanspruchnahme: mindert Sonderausgabenabzug (§ 10 Abs. 1 Nr. 3 EStG)
- Beitragsrückerstattung der GKV: steuerlich zu berücksichtigen
- Wahltarif-Beiträge: nur insoweit absetzbar, als sie tatsächlich gezahlt wurden

## Weiterführende Quellen

- [§ 53 SGB V – Wahltarife](https://www.gesetze-im-internet.de/sgb_5/__53.html)
- [§ 175 SGB V – Wahlrecht, Kündigung](https://www.gesetze-im-internet.de/sgb_5/__175.html)
- [GKV-Spitzenverband – Wahltarife](https://www.gkv-spitzenverband.de)
- [BSG-Rechtsprechung Wahltarife](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)

## 2. `kv-060-beitragsbemessung-kapitalauszahlung-betriebsrente`

**Fokus:** GKV-Beitragspflicht für Betriebsrenten und Kapitalzahlungen aus betrieblicher Altersversorgung: § 229 SGB V, BSG-Rechtsprechung und Doppelverbeitragung.

# Beitragsbemessung: Kapitalauszahlung und Betriebsrente

## Skill-Zweck

Betriebsrenten und Kapitalzahlungen aus der betrieblichen Altersversorgung (bAV) sind in der GKV beitragspflichtig. Dieser Skill klärt **Beitragspflicht nach § 229 SGB V, Freibetrag, Kapitalzahlungs-Verteilung und das Problem der Doppelverbeitragung**.

## Rechtlicher Rahmen

- **§ 229 SGB V** – Versorgungsbezüge als beitragspflichtige Einnahmen
- **§ 226 Abs. 2 SGB V** – Freibetrag für Versorgungsbezüge (2025: 187,25 €/Monat)
- **§ 248 SGB V** – Beitragssatz Rentner: allgemeiner Satz (14,6 %) + Zusatzbeitrag
- BSG B 12 KR 13/10 R (Direktversicherung als Versorgungsbezug), BSG B 12 KR 17/20 R (Kapitalauszahlung)
- BVerfG 1 BvR 100/15 – Verfassungsbeschwerde Doppelverbeitragung (abgewiesen; aber Reform eingeleitet)
- **Betriebsrentenstärkungsgesetz 2019** – Freibetrag ab 2020

## Versorgungsbezüge-Typen

| Versorgungsart | Beitragspflichtig? | Bemessungsgrundlage |
|---------------|-------------------|---------------------|
| Direktpension (Rentenleistung) | Ja, ab Freibetrag | Monatsbetrag |
| Direktversicherung (Rentenzahlung) | Ja | Monatliche Rente |
| Direktversicherung (Kapitalzahlung) | Ja (auf 10 Jahre verteilt) | Einmalzahlung / 120 |
| Pensionskasse (Rente) | Ja | Monatsbetrag |
| Pensionsfonds (Rente) | Ja | Monatsbetrag |
| Entgeltumwandlungs-bAV (steuerlich gefördert) | Ja | Wie reguläre Versorgungsbezüge |

## Prüfprogramm

### Schritt 1 – Versorgungsbezug identifizieren
- Zahlung aus betrieblicher Altersversorgung (bAV)?
- Rechtsgrundlage: Betriebsrentengesetz (BetrAVG), Direktversicherungsvertrag, Versorgungsordnung?
- Direktzahlung durch ehemaligen Arbeitgeber oder aus Versicherungsvertrag?

### Schritt 2 – Freibetrag berücksichtigen (§ 226 Abs. 2 SGB V)
- Freibetrag 2025: 187,25 €/Monat
- Beitragspflicht erst ab Überschreitung des Freibetrags
- Mehrere Versorgungsbezüge: Freibetrag nur einmal abziehen (Gesamtbetrag)

### Schritt 3 – Kapitalzahlung (§ 229 Abs. 1 Satz 3 SGB V)
- Einmalige Kapitalzahlung: auf 10 Jahre (120 Monate) verteilen
- Monatlicher Betrag = Kapitalzahlung / 120
- Dieser Betrag ist als monatlicher Versorgungsbezug beitragspflichtig

### Schritt 4 – Doppelverbeitragungsproblem
- Entgeltumwandlung: Beiträge aus Nettogehalt gezahlt (nach GKV-Beitrag) → im Rentenalter wieder verbeitragt
- Reform 2020: Freibetrag mildert Problem; vollständige Lösung steht noch aus
- Verfassungsbeschwerde: BVerfG hat Doppelverbeitragung 2006 als verfassungskonform eingestuft; aber Reformdruck

### Schritt 5 – Widerspruch gegen Beitragsbescheid
- Kasse fordert Beiträge rückwirkend aus übersehenen Versorgungsbezügen
- Verjährung: 4 Jahre (§ 25 SGB IV)
- Überprüfung: Freibetrag korrekt angewendet? Kapitalzahlung korrekt auf 120 Monate verteilt?

## Typische Fallen

- **Direktversicherung vergessen**: Versicherter weiß nicht, dass private Lebensversicherung aus Entgeltumwandlung als Versorgungsbezug gilt.
- **Kapitalzahlung einmalig bezahlt**: Kasse setzt rückwirkend 120 Monate als beitragspflichtig fest; erhebliche Nachzahlung.
- **Freibetrag und Mehrfachbezüge**: Mehrere kleine Versorgungsbezüge übersteigen zusammen den Freibetrag.
- **Private Renten**: Rürup-Rente und Privatrente sind KEINE Versorgungsbezüge nach § 229 SGB V.

## Output-Formate

- Versorgungsbezugs-Beitragsberechnung
- Kapitalzahlungs-Verteilungsberechnung (120 Monate)
- Widerspruch gegen Beitragsfestsetzung
- Freibetrags-Überprüfungsantrag
- Doppelverbeitragung-Informationsblatt

## Quellen

- [§ 229 SGB V – Versorgungsbezüge](https://www.gesetze-im-internet.de/sgb_5/__229.html)
- [§ 226 SGB V – Freibetrag](https://www.gesetze-im-internet.de/sgb_5/__226.html)
- [BSG B 12 KR 13/10 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [BVerfG Doppelverbeitragung](https://www.bverfg.de/entscheidungen.html)
- [GKV-Spitzenverband Versorgungsbezüge](https://www.gkv-spitzenverband.de)
- [dejure.org § 229 SGB V](https://dejure.org/gesetze/SGB_V/229.html)

## 3. `kv-061-versorgungsbezuege-und-doppelverbeitragung`

**Fokus:** Kritische Analyse der Doppelverbeitragung von Betriebsrenten in der GKV: Rechtslage, Reform 2020, Freibetrag, laufende Verfahren und Gestaltungsoptionen.

# Versorgungsbezüge und Doppelverbeitragung

## Skill-Zweck

Die Doppelverbeitragung von Betriebsrenten ist ein politisch und rechtlich umstrittenes Thema. Dieser Skill analysiert **die aktuelle Rechtslage nach dem Freibetrag 2020, Verteidigungsstrategien und Gestaltungsoptionen zur Beitragsminimierung**.

## Rechtlicher Rahmen

- **§ 229 SGB V** – Versorgungsbezüge als beitragspflichtige Einnahmen
- **§ 226 Abs. 2 SGB V** – Freibetrag 2020: 1/20 der monatlichen Bezugsgröße (2025: 187,25 €)
- **Betriebsrentenstärkungsgesetz 2019** – Einführung des Freibetrags
- BVerfG 1 BvR 100/15 (Doppelverbeitragung verfassungskonform; aber politischer Reformdruck)
- BSG B 12 KR 5/21 R (Freibetrag-Berechnung bei mehreren Bezügen)
- **BMF-Schreiben** zur steuerlichen Behandlung von Entgeltumwandlung

## Doppelverbeitragung – Mechanismus

| Phase | Beitragsbelastung |
|-------|------------------|
| Erwerbsphase (Entgeltumwandlung) | Beiträge werden aus beitragspflichtigem Entgelt geleistet (BEREITS nach GKV-Beitragsabzug) |
| Rentenphase (Auszahlung) | Betriebsrente wieder als Versorgungsbezug verbeitragt |
| Doppeleffekt | Gleicher Betrag zweifach verbeitragt |
| Reform 2020 | Freibetrag 187,25 €/Monat mindert Doppelverbeitragung |

## Prüfprogramm

### Schritt 1 – Entgeltumwandlung identifizieren
- Wurde bAV durch Entgeltumwandlung finanziert (aus Bruttolohn steuerlich oder aus Nettolohn)?
- Bei Entgeltumwandlung aus Bruttolohn: GKV-Beitragsfreiheit in Ansparphase bis 4 % der BBG (2025: bis 3.624 €/Jahr)
- Bei Entgeltumwandlung aus Nettolohn (historisch): volle Doppelverbeitragung

### Schritt 2 – Freibetrag anwenden (§ 226 Abs. 2 SGB V)
- Freibetrag 187,25 €/Monat abziehen
- Nur einmal unabhängig von Anzahl der Versorgungsbezüge
- Beitrag nur auf Betrag über Freibetrag

### Schritt 3 – Gestaltungsoptionen
- Kapitalzahlung vs. Rente: Kapitalzahlung auf 10 Jahre verteilt → oft geringere Gesamtbelastung
- Riester-Entgeltumwandlung: andere Beitragsregeln; weniger Doppelverbeitragung
- Kombination verschiedener bAV-Wege wählen um Freibetrag optimal zu nutzen

### Schritt 4 – Laufende politische Diskussion
- Bundesregierung diskutiert vollständige Abschaffung der Doppelverbeitragung
- Aktueller Stand: Freibetrag aus 2020 bleibt; vollständige Abschaffung noch nicht beschlossen
- Monitoring: Gesetzgebungsverfahren verfolgen

### Schritt 5 – Rechtliche Überprüfung
- BVerfG hat Verfassungsmäßigkeit bestätigt
- Neue Verfassungsbeschwerden nach Reform 2020: noch anhängig oder abgewiesen
- Kein individueller Rechtsanspruch auf beitragsfreie Betriebsrente

## Typische Fallen

- **Beitragsbefreiung in Ansparphase verleitet zur Unterschätzung**: Beitragsfreiheit in Ansparphase führt zur größeren Auszahlung, die dann vollständig verbeitragt wird.
- **Freiwillig Versicherter vs. Pflichtmitglied**: Doppelverbeitragung trifft beide; unterschiedliche Beitragssätze.
- **Riester + Entgeltumwandlung**: Kombination kann steuerlich und sozialversicherungsrechtlich vorteilhaft sein.
- **Geschäftsführer als AG-Alleingesellschafter**: Direktversicherung: besondere Regeln (kein sozialversicherungspflichtiges Beschäftigungsverhältnis).

## Output-Formate

- Doppelverbeitragungsberechnung (Tabelle)
- Freibetrags-Kalkulation
- Gestaltungsoptionen-Übersicht
- Politisches Monitoring-Dokument
- Steuerberater-Briefing (bAV und GKV)

## Quellen

- [§ 229 SGB V – Versorgungsbezüge](https://www.gesetze-im-internet.de/sgb_5/__229.html)
- [§ 226 SGB V – Freibetrag](https://www.gesetze-im-internet.de/sgb_5/__226.html)
- [BVerfG 1 BvR 100/15](https://www.bverfg.de/entscheidungen.html)
- [BSG B 12 KR 5/21 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband Betriebsrente](https://www.gkv-spitzenverband.de)
- [dejure.org § 229 SGB V](https://dejure.org/gesetze/SGB_V/229.html)
## Hinweis: BVerfG-Entscheidung 2023 und Reaktion des Gesetzgebers

- BVerfG 1 BvL 3/18 (August 2023): Doppelverbeitragung von Direktversicherungen verfassungswidrig, soweit keine steuerliche Förderung in der Ansparphase erfolgte
- Gesetzgeber hat § 229 SGB V angepasst: Freigrenze für Versorgungsbezüge ab 2025 (1/20 der monatlichen Bezugsgröße)
- Versicherte sollten alle Versorgungsbezüge dokumentieren und prüfen, ob die Freigrenze greift
- Offene Erstattungsansprüche aus vergangenen Perioden: Prüfung empfohlen

## Weiterführende Quellen

- [§ 229 SGB V – Versorgungsbezüge](https://www.gesetze-im-internet.de/sgb_5/__229.html)
- [BVerfG 1 BvL 3/18 – Direktversicherung](https://www.bverfg.de/e/ls20230627_1bvl000318.html)
- [GKV-Spitzenverband – Beitragsrecht](https://www.gkv-spitzenverband.de)
