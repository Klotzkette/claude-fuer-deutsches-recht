---
name: anlagenverzeichnis-extrakt
description: "Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung Kurzbeschreibung Schriftsatz Blattangabe je Partei. Normen §§ 130 131 ZPO Schriftsatz-Anlagen. Prüfraster Vollständigkeit Fundstellen-Praezision Parteizuordnung. Output vollständiges Anlagenverzeichnis je Partei. Abgrenzung zu aktenauszug-erstellen (Gesamtauszug) und beweismittel-gegenüberstellung (Beweisuebersicht)."
---

# Anlagenverzeichnis-Extrakt

## Zweck

Umfangreiche Gerichtsakten enthalten oft Hunderte von Anlagen, die über verschiedene Schriftsätze verteilt sind. Dieser Skill erstellt ein geordnetes Anlagenverzeichnis, das alle Anlagen mit Bezeichnung, Inhalt und Fundstelle erfasst.

## Triage — kläre vor Erstellung

1. Liegt ein vollständiges Inhaltsverzeichnis der Akte vor?
2. Sind alle Schriftsätze in der Akte? Welche fehlen?
3. Besteht Streit über Übergabe oder Vollständigkeit bestimmter Anlagen?
4. Ist ein Anlageregister fuer Gericht oder fuer Mandant gedacht?

## Zentrale Normen

- § 130 Nr. 5 ZPO — Inhalt des Schriftsatzes: Anlagen müssen bezeichnet werden
- § 131 ZPO — Bezugnahme auf beigefügte Schriftstücke als Anlagen; Verlesen bei Bedarf
- § 141 ZPO — Persönliches Erscheinen; Vorlage von Unterlagen durch Partei
- § 142 ZPO — Anordnung der Urkundenvorlage durch Gericht (richterliche Vorlageanordnung)
- § 422 ZPO — Vorlegungspflicht für Urkunden (Parteibesitz)
- § 432 ZPO — Anforderung von Urkunden durch das Gericht bei Behörden

## Rechtsprechung zu Anlagen und Schriftsatz-Bezugnahmen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anlagenbezeichnungen

### Klägerseite

- K 1, K 2, K 3 ... (K = Kläger)
- AST 1, AST 2 ... (Antragsteller in Eilverfahren)

### Beklagtenseite

- B 1, B 2, B 3 ... (B = Beklagter)
- AG 1, AG 2 ... (Antragsgegner in Eilverfahren)

### Sonstige

- GA 1, GA 2 ... (Gericht, z. B. Sachverständigengutachten)
- SV 1, SV 2 ... (Sachverständiger)

## Tabellenstruktur

```markdown
| Anlage | Inhalt (kurz) | Datum des Dokuments | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag vom TT.MM.JJJJ | TT.MM.JJJJ | Klageschrift | 12-18 |
| K 2 | Abnahmeprotokoll | TT.MM.JJJJ | Klageschrift | 19-21 |
| K 3 | Mängelrüge (Schreiben) | TT.MM.JJJJ | Klageschrift | 22 |
```

## Schritt-für-Schritt-Workflow

1. **Jeden Schriftsatz** auf Anlagenverweise (K 1, B 1 etc.) durchsuchen
2. **Anlage mit Inhalt und Datum** erfassen; Originalbezeichnung übernehmen
3. **Schriftsatz und Blattangabe** notieren
4. **Alle Anlagen** nach Partei getrennt tabellarisch listen
5. **Lücken prüfen** — fehlende Nummern als [nicht in vorliegender Akte] markieren
6. **Doppelreferenzen** prüfen — gleiche Anlage in mehreren Schriftsätzen vermerken
7. **Vorlageanordnung prüfen** — falls § 142 ZPO-Beschluss in Akte: erfasste Anlagen abgleichen

## Entscheidungsbaum — Anlage fehlt in Akte

```
Anlage ist im Schriftsatz bezeichnet aber fehlt körperlich in Akte?
  → Handelt es sich um beweiserhebliche Urkunde? (§ 422 ZPO)
    → Ja: Schriftsatz an Gericht: Vorlage anfordern; Eintrag: [angefordert TT.MM.JJJJ]
    → Nein: Vermerk: [nicht in vorliegender Akte]
  → War Anlage Gegenstand einer Vorlageanordnung (§ 142 ZPO)?
    → Ja: Nachverfolgung ob Vorlage erfolgt — ggf. Antrag auf Ungehorsamssanktion
```

## Beispiel (vollständig)

### Klägeranlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag | 15.03.2021 | Klageschrift 08.02.2023 | 12-18 |
| K 2 | Abnahmeprotokoll | 02.09.2021 | Klageschrift 08.02.2023 | 19-21 |
| K 3 | Mängelrüge | 14.10.2021 | Klageschrift 08.02.2023 | 22 |
| K 4 | Nachbesserungsprotokoll | 08.11.2021 | Klageschrift 08.02.2023 | 23-24 |
| K 5 | Rücktrittsandrohung | 03.01.2022 | Klageschrift 08.02.2023 | 25 |
| K 6 | Rücktrittserklärung | 15.02.2022 | Klageschrift 08.02.2023 | 26 |

### Beklagtenanlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| B 1 | E-Mail-Korrespondenz | versch. | Klageerwiderung 14.04.2023 | 40-44 |
| B 2 | Wartungsprotokoll | 05.09.2021 | Klageerwiderung 14.04.2023 | 45-47 |

## Qualitätscheck

- [ ] Alle Anlagenbezeichnungen aus allen Schriftsätzen erfasst?
- [ ] Lücken in der Nummerierung als fehlend markiert?
- [ ] Inhalt kurz aber aussagekräftig beschrieben?
- [ ] Fundstelle (Schriftsatz und Blatt) angegeben?
- [ ] Vorlageanordnungen nach § 142 ZPO berücksichtigt?

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 396/18 (claimed: Fehlende Anlage kann nachgereicht werden, NJW 2020, 404): WRONG_TOPIC. Urteil existiert (dejure.org/2019,38295), behandelt aber Kfz-Unfall Beilackierungskosten/§287 ZPO Schaetzungsermessen, NJW 2020, 236. Kein Bezug zu ZPO-Anlagenrecht. Eintrag geloescht. -->
