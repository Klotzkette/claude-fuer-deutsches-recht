---
name: aufsichtsrat-protokoll
description: >
  Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG,
  § 107 AktG) und Gesellschafterversammlungen (GmbH, § 48 GmbHG) im Hausformat.
  Erkennt bevorstehende Organsitzungen aus dem Kalender, fragt nach Tagesordnung
  und Materialien und erstellt einen vollständigen Entwurf. Trigger: „Protokoll",
  „Vorstandssitzung", „Aufsichtsratssitzung", „Gesellschafterversammlung",
  „Protokollentwurf", „Sitzungsprotokoll".
language: de
triggers:
  - "Protokoll"
  - "Vorstandssitzung"
  - "Aufsichtsratssitzung"
  - "Gesellschafterversammlung"
  - "Protokollentwurf"
  - "Sitzungsprotokoll"
  - "Hauptversammlung"
---

# Vorstands- und Aufsichtsratsprotokoll (AG: § 107 AktG; GmbH: § 48 GmbHG)

## Zweck

Sitzungsprotokolle sind Rechtsurkunden. Sie müssen inhaltlich korrekt, vollständig und in einem Format sein, das einer späteren Prüfung standhält – ob im Rahmen einer M&A-Due-Diligence, eines Rechtsstreits oder einer behördlichen Anfrage. Dieser Skill erstellt Protokolle im Hausformat, damit der Anwalt nur prüft und korrigiert, anstatt zu formatieren und neu zu tippen.

## Rechtlicher Rahmen

- **AG – Vorstand:** § 77 AktG (Geschäftsführung), § 84 AktG (Bestellung), keine gesetzliche Protokollpflicht; empfohlen aus Beweiszwecken.
- **AG – Aufsichtsrat:** § 107 Abs. 2 AktG – Über jede Sitzung ist eine Niederschrift aufzunehmen, die Ort und Tag, die Teilnehmer, die Gegenstände der Tagesordnung, den wesentlichen Inhalt der Verhandlungen und die Beschlüsse des Aufsichtsrats enthält. Unterzeichnung durch den Vorsitzenden.
- **AG – Hauptversammlung:** § 130 AktG – Beurkundung durch Notar (§ 130 Abs. 1 AktG für börsennotierte AG), sonst § 130 Abs. 4 AktG für nicht börsennotierte AG.
- **GmbH – Gesellschafterversammlung:** § 48 GmbHG – Beschlüsse in der Gesellschafterversammlung; Protokollpflicht nicht gesetzlich normiert, aber durch Gesellschaftsvertrag und Praxis. § 48 Abs. 2 GmbHG: schriftliches Abstimmungsverfahren mit Einvernehmen aller Gesellschafter.
- **Beschlussmängel AG:** §§ 243 ff. AktG – Anfechtungsklage (§ 243), Nichtigkeitsgründe (§ 241), Heilung (§ 244). Frist: 1 Monat ab Beschlussfassung (§ 246 Abs. 1 AktG).
- **Beschlussmängel GmbH:** §§ 243 ff. AktG analog (h.M.); BGH, Urt. v. 17.02.1997 – II ZR 41/96, BGHZ 134, 364 (Gelatine); BGH, Urt. v. 21.06.1999 – II ZR 47/98, NJW 1999, 3113.

## Eingaben

- Praxisprofil: `## Organe & Protokoll` (Protokollformat, Zusammensetzung, Mitbestimmung, Beschlusssprache, Seed-Protokolle)
- Organgremium: Vorstand / Aufsichtsrat / Gesellschafterversammlung / Hauptversammlung
- Tagesordnung und Sitzungsmaterialien (Präsentationen, Berichte, Beschlussvorlagen)
- Anwesenheitsliste (Mitglieder anwesend / entschuldigt)
- Beschlüsse und Abstimmungsergebnisse

## Ablauf

### Schritt 1: Sitzung identifizieren

**Kalendererkennung** (wenn Kalender-Connector autorisiert): Suche nach bevorstehenden Ereignissen mit:
- „Vorstandssitzung", „Aufsichtsratssitzung", „AR-Sitzung", „Gesellschafterversammlung", „GV", „Hauptversammlung", „HV", „Beiratssitzung", „Präsidiumssitzung"
- Zeitfenster: 30 Tage voraus; bei Nichtfund 14 Tage rückwärts (Protokolle häufig nachträglich erstellt).

Falls kein Connector: direkt fragen – welches Organ, welches Datum, welcher Typ?

**Sitzungsmetadaten bestätigen:**
- Organ und Gesellschaft
- Datum und Uhrzeit
- Ort oder Plattform (physisch / Videokonferenz nach § 108 Abs. 4 AktG / telefonisch)
- Ordnungsgemäße Einladung? (AG Aufsichtsrat: § 110 Abs. 1 AktG – Einladungsfrist mind. 14 Tage; Verzicht möglich)
- Form der Sitzungsniederschrift: Vollprotokoll (§ 107 Abs. 2 AktG) / Beschlussprotokoll / Hybridform

### Schritt 2: Anwesenheit und Beschlussfähigkeit

**Mitglieder anwesend:**
- Ausgangspunkt: Organ-Zusammensetzung aus Praxisprofil
- Wer war tatsächlich anwesend / entschuldigt?
- Aufsichtsrat: § 108 Abs. 2 AktG – Beschlussfähigkeit wenn mind. die Hälfte der Mitglieder anwesend; Mindestens 3 Mitglieder müssen bei der Abstimmung mitwirken.
- GmbH-Gesellschafterversammlung: Quorum nach Gesellschaftsvertrag; gesetzlicher Standard: § 47 GmbHG (Mehrheit der abgegebenen Stimmen).

**Wenn Beschlussfähigkeit nicht gegeben:** STOPP. Keine Protokollierung einer gültigen Beschlussfassung. Abhilfemaßnahmen (Erneuerung, Umlaufverfahren, Verzicht) mit Anwalt klären.

**Vorsitz und Protokollführer:**
- Aufsichtsrat: Vorsitzender (§ 107 Abs. 1 AktG)
- GmbH: Versammlungsleiter (nach GV oder Gesellschaftsvertrag)
- Wer unterzeichnet das Protokoll?

**Interessenkonflikte:**
- Aufsichtsrat: § 34 BGB analog; § 136 AktG analog (Stimmverbot bei Entlastung); Beschlussgegenstand prüfen.
- GmbH: § 47 Abs. 4 GmbHG – Stimmverbot des Gesellschafters bei Beschlüssen über Vornahme/Einleitung von Rechtsgeschäften/Rechtsstreitigkeiten mit ihm.

### Schritt 3: Materialien

Tagesordnung und Sitzungsmaterialien anfordern:

> Bitte Tagesordnung und alle Sitzungsmaterialien bereitstellen – auch ein grober Entwurf reicht zur Strukturierung des Protokolls. Falls Präsentationen oder Berichte vorlagen, diese bitte hochladen – ich nutze sie zur Zusammenfassung der Tagesordnungspunkte.
>
> Wenn keine Materialien vorlagen, bitte Tagesordnungspunkte mitteilen, und ich erstelle Platzhalter.

Aus Tagesordnung und Materialien extrahieren:
- Tagesordnungspunkte in Reihenfolge
- Vorgeschlagene Beschlüsse (Formulierung, Abstimmungsergebnis)
- Anlagen (Präsentationen, Berichte, Gutachten, Bewertungen)
- Abstimmungen und Stimmverhältnisse

### Schritt 4: Protokoll erstellen

Hausformat aus Praxisprofil verwenden. Kein generisches Format.

**Standard-Struktur (an Hausformat anpassen):**

```
PROTOKOLL DER [ORGANGREMIUM]
DER [GESELLSCHAFTSNAME]

[Datum], [Uhrzeit], [Ort / Videokonferenz]

Vorsitz: [Name]
Protokollführer: [Name]
```

**Eröffnung:**
- Sitzung eröffnet durch [Vorsitz] um [Uhrzeit]
- Einladung: [ordnungsgemäß erfolgt / verzichtet – Einladungsverzicht als Anlage]
- Beschlussfähigkeit festgestellt: [N von M Mitgliedern anwesend]
- Genehmigung des Protokolls der letzten Sitzung vom [Datum]

**Anwesenheit:**
- Anwesende Mitglieder: [Liste]
- Entschuldigte Mitglieder: [Liste, falls vorhanden]
- Gäste/Berater: [Externe, Anwälte, Wirtschaftsprüfer – mit Funktion; ggf. nur für bestimmte TOP]

**Tagesordnungspunkte – je einen Abschnitt pro Punkt:**

```
TOP [N]: [Bezeichnung]

[Vorstandsmitglied / GF / Berater] berichtete über / erläuterte [Gegenstand].

[Diskussion – nach Hausformat: vollständig / Beschlusskürzel / hybrid]

[Falls Beschluss:]
Der [Aufsichtsrat / die Gesellschafterversammlung] fasste sodann einstimmig /
mit [N] Ja-Stimmen gegen [N] Nein-Stimmen bei [N] Enthaltungen folgenden Beschluss:

BESCHLUSS:
[Beschlusstext im Hausformat]

Anlage [Buchstabe]: [Beschreibung der Anlage]
```

**Schließung:**
- Es lagen keine weiteren Tagesordnungspunkte vor.
- Die Sitzung wurde um [Uhrzeit] geschlossen.

**Unterschriftenblock:**
- Aufsichtsrat: Vorsitzender allein (§ 107 Abs. 2 Satz 3 AktG)
- GmbH: Versammlungsleiter / Protokollführer (je nach GV)

### Schritt 4.5: Folgenreiche-Handlung-Sperre (Protokoll verabschieden)

**Vor Verabschiedung als endgültig:** `## Wer dieses Plugin nutzt` im Praxisprofil prüfen. Falls Rolle **Nichtjurist**:

> Beschlossene Protokolle sind die offizielle Aufzeichnung der Organentscheidungen – sie sind das primäre Beweismittel für Ermächtigungen. Wurden diese mit einem Rechtsanwalt überprüft?
>
> Besonders achten auf:
> - Beschlussmängel (§§ 243, 241 AktG; analog GmbH)
> - Interessenkonflikte (§ 47 Abs. 4 GmbHG; § 136 AktG)
> - Einladungsfristen und Beschlussfähigkeit
> - Ordnungsgemäße Unterzeichnung (§ 107 Abs. 2 AktG)

### Schritt 5: Ausgabe und Prüfcheckliste

```
VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS

PRÜFCHECKLISTE — bitte vor Versand/Unterzeichnung prüfen:

□ Alle anwesenden/entschuldigten Mitglieder korrekt erfasst
□ Beschlussfähigkeit korrekt festgestellt und dokumentiert
□ Beschlusstexte stimmen mit tatsächlich gefassten Beschlüssen überein
□ Abstimmungsergebnisse korrekt (ggf. Stimmverbote § 47 Abs. 4 GmbHG / § 136 AktG geprüft?)
□ Anlagen korrekt nummeriert und referenziert
□ Interessenkonflikte / Stimmverbote vermerkt (falls zutreffend)
□ Executive Sessions / vertrauliche Tagesordnungspunkte getrennt protokolliert?
□ Unterzeichnungszeitpunkt und Unterschriftenblock korrekt
□ Externer Anwalt / Wirtschaftsprüfer anwesend? Deren Anwesenheit und ggf. Bericht vermerkt?
```

## Quellen und Zitierweise

- § 107 Abs. 2 AktG (Niederschriftspflicht Aufsichtsrat)
- § 48 GmbHG (Gesellschafterversammlung)
- § 130 AktG (Hauptversammlungsprotokoll)
- §§ 241, 243, 246 AktG (Beschlussmängel und -anfechtung)
- § 47 Abs. 4 GmbHG (Stimmverbot GmbH)

Zitierweise nach `../../references/zitierweise.md`.

Kommentarliteratur:
- Hüffer/Koch, AktG, 16. Aufl. 2023, § 107 Rn. 10 ff.
- Schmidt/Lutter, AktG, 4. Aufl. 2020, § 243 Rn. 5 ff.
- Roth/Altmeppen, GmbHG, 10. Aufl. 2021, § 48 Rn. 3 ff.
- Scholz, GmbHG, 12. Aufl. 2018, § 47 Rn. 110 ff.
- BGH, Urt. v. 17.02.1997 – II ZR 41/96, BGHZ 134, 364 (Gelatine) – zur GmbH-Beschlussmängelklage analog AktG.
- BGH, Urt. v. 07.02.2012 – II ZR 230/09, NZG 2012, 427 – zur Protokollpflicht bei Aufsichtsratsbeschlüssen.

## Ausgabeformat

1. **Protokollentwurf** (im Hausformat; ENTWURF-Vermerk bis zur Genehmigung)
2. **Prüfcheckliste** (Checkliste für Rechtsanwalt)
3. **Genehmigungsversion** (nach Freigabe; ohne Entwurfsvermerk; ohne internen Kommentar)

## Beispiel

**AG-Aufsichtsratssitzung, § 107 AktG:**

> PROTOKOLL DER AUFSICHTSRATSSITZUNG
> DER MUSTER AG
> 15. März 2025, 10:00 Uhr, Frankfurt am Main
>
> Vorsitz: Dr. Anna Müller
> Protokollführerin: Rechtsanwältin Christine Weber, Kanzlei XY
>
> TOP 1: Bericht des Vorstands
> Vorstandsvorsitzender Max Huber berichtete über die Geschäftsentwicklung im Q1 2025 (Anlage A).
>
> TOP 2: Zustimmung zur Übernahme der Beta GmbH
> Der Vorstand erläuterte die geplante Übernahme der Beta GmbH zum Kaufpreis von 5 Mio. EUR. Die Transaktion unterfällt § 3 der Geschäftsordnung des Vorstands (Zustimmungspflicht bei Erwerben >1 Mio. EUR).
>
> *Nach eingehender Erörterung fasste der Aufsichtsrat einstimmig folgenden Beschluss:*
>
> **BESCHLUSS:** Der Aufsichtsrat stimmt dem Erwerb der Geschäftsanteile an der Beta GmbH zum Kaufpreis von bis zu 5.000.000 EUR gemäß dem Entwurf des Share Purchase Agreement (Anlage B) zu.
>
> Abstimmung: 5 Ja / 0 Nein / 0 Enthaltungen

## Risiken / typische Fehler

- **Fehlendes Protokoll = Beschlussbeweisnot:** Ohne Protokoll sind Beschlüsse schwer zu beweisen. Insbesondere für zustimmungspflichtige Maßnahmen (§ 111 Abs. 4 AktG) oder Entlastungen.
- **Stimmverbot übersehen:** § 47 Abs. 4 GmbHG / § 136 AktG – Beschluss anfechtbar oder nichtig, wenn stimmverbotenes Mitglied abgestimmt hat.
- **Einladungsfrist versäumt:** § 110 Abs. 2 AktG – AR-Sitzung ohne Einhaltung der Einladungsfrist kann zur Beschlussmängelanfechtung führen; Einladungsverzicht dokumentieren.
- **Anfechtungsfrist beachten:** § 246 Abs. 1 AktG – 1 Monat ab Beschlussfassung; nach BGH auch analog für GmbH (h.M.).
- **Notarielles Protokoll vergessen:** Bei börsennotierter AG (§ 130 Abs. 1 AktG) und bestimmten Beschlüssen (Satzungsänderungen § 179 AktG, Kapitalmaßnahmen) ist notarielle Beurkundung erforderlich. Skill erstellt keinen Entwurf für Notarbeurkundung.
