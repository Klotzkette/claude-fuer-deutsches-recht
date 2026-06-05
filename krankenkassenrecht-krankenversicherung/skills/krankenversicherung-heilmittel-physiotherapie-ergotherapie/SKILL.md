---
name: krankenversicherung-heilmittel-physiotherapie-ergotherapie
description: "Heilmittel Physiotherapie Ergotherapie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Heilmittel Physiotherapie Ergotherapie

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Heilmittel Physiotherapie Ergotherapie** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-007-heilmittel-physiotherapie-ergotherapie-und-genehmigung` | Heilmittelanspruch nach § 32 SGB V: Heilmittel-Richtlinie, Verordnungsmengen, Langfristgenehmigung, Wirtschaftlichkeitsprüfung und Widerspruch. |
| `kv-008-arzneimittel-off-label-und-lifestyle-abgrenzung` | GKV-Arzneimittelversorgung: Zulassung, Off-Label-Use nach BSG-Maßstäben, Lifestyle-Ausschluss, AMNOG, Nutzenbewertung und Einzelfallentscheidung. |
| `kv-009-krankenhausabrechnung-drg-zuzahlung-und-md-pruefung` | Krankenhausabrechnung im DRG-System: Kodierung, Zuzahlungspflicht, MD-Prüfverfahren, Kürzungen und Widerspruchsstrategien. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Heilmittel Physiotherapie Ergotherapie**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-007-heilmittel-physiotherapie-ergotherapie-und-genehmigung`

**Fokus:** Heilmittelanspruch nach § 32 SGB V: Heilmittel-Richtlinie, Verordnungsmengen, Langfristgenehmigung, Wirtschaftlichkeitsprüfung und Widerspruch.

# Heilmittel: Physiotherapie, Ergotherapie und Genehmigung

## Skill-Zweck

Heilmittel (Physiotherapie, Ergotherapie, Logopädie, Podologie) sind häufig Gegenstand von Ablehnungen und Mengenbeschränkungen. Dieser Skill klärt den **Anspruch, die Verordnungssystematik und Genehmigungsverfahren** nach der Heilmittel-Richtlinie (HM-RL) des G-BA.

## Rechtlicher Rahmen

- **§ 32 SGB V** – Heilmittelanspruch (Physiotherapie, Ergotherapie, Sprachtherapie, Podologie)
- **§ 12 SGB V** – Wirtschaftlichkeitsgebot
- **§ 73 SGB V** – Vertragsärztliche Versorgung; Verordnungsrecht des Arztes
- **§ 92 SGB V** – G-BA: Heilmittel-Richtlinie (HM-RL)
- **Heilmittel-Richtlinie des G-BA** (aktuell 2024): Diagnoseliste, Verordnungsmengen, Langfristversorgung
- **§ 106b SGB V** – Wirtschaftlichkeitsprüfung der Verordnungen (KV-Regressgefahr für Arzt)
- BSG B 3 KR 10/21 R (Heilmittel Langfristversorgung)

## Heilmittel-Systematik (HM-RL)

| Kategorie | Bedeutung |
|-----------|-----------|
| Orientierende Behandlungsmenge | Regelfall; innerhalb dieser keine Genehmigung nötig |
| Gesamtverordnungsmenge | Maximalmenge je Diagnosengruppe |
| Langfristversorgung | Bei chronisch-schweren Erkrankungen, Genehmigung durch Kasse erforderlich |
| Besonderer Verordnungsbedarf | Diagnosen, die außerhalb der Regelmengen liegen |

## Prüfprogramm

### Schritt 1 – Verordnungsinhalt prüfen
- Liegt eine gültige Verordnung vor (Formular Muster 13, Muster 18)?
- Indikationsschlüssel korrekt? Behandlungsart und Frequenz angegeben?
- Ausnahmetatbestand eingetragen (z.B. besonderer Verordnungsbedarf)?

### Schritt 2 – Genehmigungspflicht klären
- Innerhalb orientierende Behandlungsmenge (G-BA Heilmittelkatalog): keine Genehmigung nötig
- Langfristversorgung: Antrag an Kasse, spätestens 4 Wochen vor Ablauf der laufenden Versorgung
- Genehmigungsfiktion: § 13 Abs. 3a SGB V – bei fehlender Entscheidung innerhalb 5 Wochen gilt Genehmigung als erteilt

### Schritt 3 – Ablehnungsgründe analysieren
- **Wirtschaftlichkeit**: Verordnungsmenge überschritten → Heilmittelkatalog konsultieren, Ausnahmetatbestand dokumentieren
- **Indikationsschlüssel falsch**: Verordnung durch Arzt korrigieren lassen; keine Heilung im Nachhinein
- **MDK-Prüfung**: Gegengutachten des Therapeuten oder Facharztes

### Schritt 4 – Widerspruch und Klage
- Ablehnungsbescheid anfechtbar, § 84 SGG (1 Monat)
- Im Widerspruch: ärztliches Attest über Behandlungsnotwendigkeit, Befundberichte des Therapeuten
- Eilantrag (§ 86b SGG): bei akuter Verschlechterung ohne laufende Therapie

### Schritt 5 – Arztregress-Schnittstelle
- Arzt haftet bei Überverordnung aus wirtschaftlichen Gründen; Versicherte sind nicht betroffen
- Arzt darf Verordnung nicht aus Regressangst verweigern wenn medizinisch indiziert
- Bei Verordnungsverweigerung: Zweitmeinung oder Beschwerde an KV

## Typische Fallen

- **Verordnungsformular falsch**: Heilmittel auf Kassenrezept (Muster 13), nicht auf Privatrezept; Privatverordnung löst Kostenerstattungsverfahren aus.
- **Therapeutenwechsel**: Neue Verordnung erforderlich bei Wechsel des Therapeuten (außer Praxisübernahme).
- **Genehmigungsfiktion vergessen**: Kasse reagiert nicht innerhalb von 5 Wochen → schriftlich auf Fiktion hinweisen, Behandlung beginnen.
- **Zuzahlung**: 10 % je Verordnung + 10 € Rezeptgebühr; Befreiungsgrenze (2 % / 1 % des Bruttoeinkommens) prüfen.

## Output-Formate

- Antragsschreiben Langfristversorgung
- Widerspruch gegen Heilmittelablehnung
- Genehmigungsfiktion-Schreiben
- Arzt-Briefing zur korrekten Verordnung
- Fristenplan (Verlängerungsanträge)

## Quellen

- [§ 32 SGB V – Heilmittel](https://www.gesetze-im-internet.de/sgb_5/__32.html)
- [Heilmittel-Richtlinie G-BA](https://www.g-ba.de/richtlinien/12/)
- [§ 13 Abs. 3a SGB V – Genehmigungsfiktion](https://www.gesetze-im-internet.de/sgb_5/__13.html)
- [§ 92 SGB V – G-BA](https://www.gesetze-im-internet.de/sgb_5/__92.html)
- [BSG Heilmittelrechtsprechung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 32 SGB V](https://dejure.org/gesetze/SGB_V/32.html)

## 2. `kv-008-arzneimittel-off-label-und-lifestyle-abgrenzung`

**Fokus:** GKV-Arzneimittelversorgung: Zulassung, Off-Label-Use nach BSG-Maßstäben, Lifestyle-Ausschluss, AMNOG, Nutzenbewertung und Einzelfallentscheidung.

# Arzneimittel: Off-Label-Use und Lifestyle-Abgrenzung

## Skill-Zweck

Dieser Skill klärt, wann die GKV Arzneimittelkosten übernimmt – und wann nicht. Schwerpunkte sind **Off-Label-Verschreibungen**, die Abgrenzung zu Lifestyle-Medikamenten und die AMNOG-Nutzenbewertung.

## Rechtlicher Rahmen

- **§ 27 Abs. 1 SGB V** – Anspruch auf Krankenbehandlung
- **§ 31 SGB V** – Arznei- und Verbandmittel; Ausschlüsse
- **§ 34 SGB V** – Ausgeschlossene Arznei-, Heil- und Hilfsmittel (Lifestyle-Ausschluss: § 34 Abs. 1 Satz 7-8)
- **§ 35 SGB V** – Festbetragsgruppen (Gemeinsamer Bundesausschuss)
- **§ 35a SGB V** – Nutzenbewertung (AMNOG-Verfahren)
- **§ 92 SGB V** – Arzneimittel-Richtlinie (AM-RL) des G-BA
- BSG B 1 KR 37/04 R – Grundsatzentscheidung Off-Label-Use: 3 Voraussetzungen
- BSG B 1 KR 10/12 R – Grundrechtsorientierte Auslegung § 2 Abs. 1a SGB V

## Off-Label-Use: BSG-Dreitest

| Voraussetzung | Inhalt |
|---------------|--------|
| 1. Lebensbedrohliche/schwerwiegende Erkrankung | Diagnose muss ernst und schwerwiegend sein |
| 2. Keine Behandlungsalternative | Keine zugelassene Therapie verfügbar oder wirksam |
| 3. Begründete Aussicht auf Behandlungserfolg | Wissenschaftliche Belege, Phase-III-Studien oder BSG-Kriterien |

## Prüfprogramm

### Schritt 1 – Zulassungsstatus des Arzneimittels
- AMG-Zulassung für die konkrete Indikation vorhanden? → Routinefall, Kasse muss zahlen
- Off-Label: Arzneimittel zugelassen, aber für andere Indikation als verordnet?
- Nicht zugelassen (unlicensed): gesonderte Prüfung, strengerer Maßstab

### Schritt 2 – Off-Label-Prüfung nach BSG-Maßstäben
- Schwerwiegende Erkrankung: lebensbedrohlich, nachhaltige Beeinträchtigung der Lebensqualität?
- Behandlungsalternative fehlt: alle zugelassenen Therapien ausgeschöpft oder kontraindiziert?
- Aussicht auf Erfolg: Phasen-II/III-Studien, Fachliteratur, systematische Reviews, Leitlinien → Belege zusammenstellen

### Schritt 3 – Lifestyle-Ausschluss (§ 34 SGB V)
- Ausgeschlossen: Medikamente zur Erhöhung der Lebensqualität ohne Krankheitswert (Potenzmittel, Schlankheitsmittel, Raucherentwöhnung außer Ausnahmen)
- Ausnahme: G-BA kann Ausnahmen zulassen (z.B. Nikotinersatz nach § 34 Abs. 1 Satz 7)
- Abgrenzung: Ist die Grunderkrankung Krankheit i.S.d. SGB V? Depression → Antidepressivum keine Lifestyle-Medizin

### Schritt 4 – AMNOG und Nutzenbewertung (§ 35a SGB V)
- Neues Arzneimittel seit 2011: AMNOG-Nutzenbewertung durch IQWiG, Beschluss G-BA
- Kein Zusatznutzen: Festbetrag oder Rabattverhandlung mit GKV-Spitzenverband
- Zusatznutzen: höherer Erstattungsbetrag, aber keine Leistungspflicht darüber hinaus

### Schritt 5 – Einzelfallentscheidung § 2 Abs. 1a SGB V
- Verfassungsrechtlicher Anspruch: lebensbedrohlich + keine Alternative + Behandlungsaussicht
- Kasse muss trotz fehlendem G-BA-Beschluss leisten (BVerfG 1 BvR 347/98)
- Antrag mit Arzt-Attest, Literaturrecherche, eigenem Fachbeitrag

## Typische Fallen

- **Verordnung auf Privatrezept**: Setzt Kostenerstattungsverfahren voraus (§ 13 Abs. 3 SGB V), aber nicht automatisch erfolgreich.
- **IGeL-Verwechslung**: Individuelle Gesundheitsleistungen sind keine Kassenleistungen; Arzt haftet wenn er sie als GKV-Leistung deklariert.
- **AMNOG-Frist**: G-BA hat 3 Monate für Nutzenbewertung; danach automatischer Festbetrag.
- **Zuzahlungsbefreiung bei Festbetrag**: Kasse zahlt nur bis Festbetrag; Arzt muss prüfen ob Wirkstoffidentikum unterhalb Festbetrag verfügbar.

## Output-Formate

- Off-Label-Antragsbrief mit Literaturnachweisen
- Widerspruchsbegründung (BSG-Dreitest-Struktur)
- Einzelfallanspruchsschreiben § 2 Abs. 1a SGB V
- AMNOG-Übersicht für konkrete Wirkstoffgruppe
- Lifestyle-Abgrenzungsanalyse

## Quellen

- [§ 31 SGB V – Arzneimittel](https://www.gesetze-im-internet.de/sgb_5/__31.html)
- [§ 35a SGB V – AMNOG](https://www.gesetze-im-internet.de/sgb_5/__35a.html)
- [Arzneimittel-Richtlinie G-BA](https://www.g-ba.de/richtlinien/3/)
- [BSG B 1 KR 37/04 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [BVerfG 1 BvR 347/98](https://www.bverfg.de/e/rs19990109_1bvr034798.html)
- [dejure.org § 34 SGB V](https://dejure.org/gesetze/SGB_V/34.html)
- [IQWiG Nutzenbewertungen](https://www.iqwig.de/methoden/nutzenbewertungen/)

## 3. `kv-009-krankenhausabrechnung-drg-zuzahlung-und-md-pruefung`

**Fokus:** Krankenhausabrechnung im DRG-System: Kodierung, Zuzahlungspflicht, MD-Prüfverfahren, Kürzungen und Widerspruchsstrategien.

# Krankenhausabrechnung: DRG, Zuzahlung und MD-Prüfung

## Skill-Zweck

Dieser Skill bearbeitet Streitigkeiten rund um **Krankenhausabrechnungen**: DRG-Kodierung, Zuzahlungspflicht des Versicherten, MD-Prüfverfahren der Kassen und Abrechnungskürzungen durch die Kasse gegenüber dem Krankenhaus.

## Rechtlicher Rahmen

- **§ 39 SGB V** – Krankenhausbehandlung: vollstationär, teilstationär, vorstationär, nachstationär
- **§ 108 SGB V** – Zugelassene Krankenhäuser
- **§ 109 SGB V** – Versorgungsvertrag
- **§ 275 SGB V** – MD-Prüfung (Wirtschaftlichkeit, Abrechnungsrichtigkeit, stationäre Notwendigkeit)
- **§ 275c SGB V** – Prüfquoten und Prüfverfahren (ab 2020); Aufwandspauschale
- **KHEntgG** (Krankenhausentgeltgesetz) §§ 1–22 – DRG-Systemgrundlagen
- **KHG** (Krankenhausfinanzierungsgesetz) §§ 1–18
- **PpUGV** – Pflegepersonaluntergrenzen (indirekte Auswirkung auf Verweildauer)
- BSG B 1 KR 2/15 R (Kodierung, Hauptdiagnose), BSG B 1 KR 28/17 R (MD-Prüfung)

## DRG-Grundstruktur

| Begriff | Bedeutung |
|---------|-----------|
| DRG | Diagnosis Related Group – Fallpauschale nach Hauptdiagnose und Prozedur |
| PCCL | Patient Clinical Complexity Level – Schweregrad durch Nebendiagnosen |
| Hauptdiagnose | Diagnose, die nach Analyse Hauptgrund für Behandlung war (ICD-10) |
| Zusatzentgelt | Ergänzung zur DRG bei besonders aufwändigen Leistungen |
| Verweildauer | Kürzung bei Unterschreitung, Zuschlag bei Überschreitung der Grenzverweildauer |

## Prüfprogramm

### Schritt 1 – Zuzahlungspflicht Versicherter
- Zuzahlung: 10 € je Krankenhaustag, max. 28 Tage/Jahr (§ 39 Abs. 4 SGB V)
- Zuzahlungsbefreiungsgrenze: 2 % des jährlichen Bruttoeinkommens, Chroniker 1 %
- Zuzahlung auch bei Kinderheilkunde? Nein: Kinder bis 18 sind zuzahlungsbefreit

### Schritt 2 – MD-Prüfverfahren (§ 275c SGB V)
- Kasse kann innerhalb von 6 Monaten nach Rechnungszugang MD einschalten (§ 275c Abs. 1)
- Prüfumfang: stationäre Notwendigkeit, Verweildauer, Kodierung, Zusatzentgelte
- Krankenhaus hat 8 Wochen Zeit für Stellungnahme/Unterlagen (§ 275c Abs. 3)
- MD-Gutachten: Krankenhaus kann Einleitung durch Sozialgericht überprüfen lassen

### Schritt 3 – Abrechnungsstreit Krankenhaus vs. Kasse
- Hauptdiagnose falsch kodiert: Kasse kürzt Rechnung → Krankenhaus widerspricht
- Richtigkeit der ICD-10/OPS-Kodierung nach DKR (Deutsche Kodierrichtlinien) prüfen
- Nebendiagnosen: Erhöhen Schweregrad (PCCL), wirken sich auf DRG-Erlös aus

### Schritt 4 – Versicherter als Drittbetroffener
- Versicherter hat keinen direkten Anspruch auf bestimmte DRG-Kodierung
- Wenn Kasse aufgrund MD-Gutachtens Krankenhausaufenthalt als ambulant behandelbar bewertet: Zuzahlung für ambulante Behandlung kann entstehen
- Wenn Kasse Kostenübernahme für Krankenhaus verweigert: Versicherter kann Anspruch auf Einweisung und Kostenübernahme (§ 39 SGB V) geltend machen

### Schritt 5 – Privatpatienten und Wahlleistungen
- Wahlleistungen (Chefarztbehandlung, Einzelzimmer): gesonderter Vertrag nach § 17 KHEntgG
- Arzthonorar: GOÄ-Abrechnung; Steigerungsfaktoren prüfen
- Krankenhaus darf Wahlleistungen nur gesondert berechnen wenn Vereinbarung vor Aufnahme

## Typische Fallen

- **Ambulantes Potential**: MD bewertet stationäre Behandlung als ambulant möglich → Kasse zahlt nur ambulante Pauschale; Differenz bleibt am Krankenhaus hängen, nicht am Versicherten.
- **Aufwandspauschale**: Kasse zahlt Krankenhaus 300 € wenn MD-Prüfung unbegründet war (§ 275c Abs. 3 Satz 4); hilft dem Versicherten nicht direkt.
- **Verlegungsfall**: Bei Verlegung innerhalb 24 Stunden: besondere DRG-Regeln; Zuzahlung bei beiden Krankenhäusern möglich.

## Output-Formate

- Zuzahlungsbefreiungsantrag
- Widerspruch gegen Krankenhauskosten-Ablehnung
- MD-Akteneinsichtsantrag
- Vergleichsrechnung DRG vs. Ist-Abrechnung
- Klage SG auf Kostenübernahme stationäre Behandlung

## Quellen

- [§ 39 SGB V – Krankenhausbehandlung](https://www.gesetze-im-internet.de/sgb_5/__39.html)
- [§ 275c SGB V – MD-Prüfung](https://www.gesetze-im-internet.de/sgb_5/__275c.html)
- [KHEntgG](https://www.gesetze-im-internet.de/khentgg/)
- [Deutsche Kodierrichtlinien (DKR)](https://www.drg-research-group.de/dkr)
- [BSG Krankenhausrecht](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 39 SGB V](https://dejure.org/gesetze/SGB_V/39.html)
- [G-BA Richtlinien Krankenhaus](https://www.g-ba.de/richtlinien/)
