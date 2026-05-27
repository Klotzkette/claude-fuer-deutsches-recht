---
name: schwerpunktthemen-identifikation
description: "Anwalt braucht schnellen Ueberblick ueber drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten ohne Erfolgsprognose. Normen §§ 139 286 ZPO BGH-Leitsaetze. Pruefraster Streitpunkt-Relevanzbewertung Rechtsprechungs-Verankerung Fundstellen-Praezision. Output Streitpunkt-Liste Relevanz-Einschaetzung Leitsatz-Referenzen. Abgrenzung zu verfahrenszusammenfassung-absatz (Ueberblick) und rechtsargumente-gegenueberstellung (alle Argumente)."
---

# Schwerpunktthemen-Identifikation

## Zweck

Dieser Skill identifiziert die drei bis fünf zentralen Rechtsfragen, auf denen das Verfahren schwerpunktmäßig beruht. Er hilft dem Anwalt, die Prioritäten für die weitere Bearbeitung zu setzen, ohne eine Einschätzung des Ausgangs zu treffen.

## Triage — kläre vor Identifikation

1. Hat das Gericht bereits Hinweise nach § 139 ZPO erteilt, auf welche Punkte es ankommt?
2. Liegt ein Beweisbeschluss vor (§ 359 ZPO)? Beweisthemen sind automatisch Schwerpunkte.
3. Sind in der Akte BGH- oder OLG-Urteile von den Parteien zitiert? (Hinweis auf rechtlich umstrittene Punkte)
4. Welche Punkte sind in mehreren Schriftsätzen (Klageerwiderung, Replik, Duplik) ausführlich diskutiert?

## Zentrale Normen

- § 139 ZPO — Richterliche Hinweispflicht; Hinweise des Gerichts benennen die Schwerpunkte
- § 286 ZPO — Freie Beweiswürdigung; entscheidungserhebliche Tatsachen sind Schwerpunkte
- § 359 ZPO — Beweisbeschluss; benennt beweisbedürftige Tatsachen
- § 522 Abs. 2 ZPO — Berufungsverwerfung; Schwerpunkt in der Berufung ist Erfolgsaussicht

## Rechtsprechung zu Schwerpunktthemen im Zivilprozess

- BGH, Urt. v. 12.05.2016 - VII ZR 171/15, NJW-RR 2016, 853 — Zum richterlichen Hinweis nach § 139 ZPO: Gericht muss auf Punkte hinweisen, die eine Partei erkennbar übersehen hat; Verstoß begründet Verfahrensfehler.
- BGH, Urt. v. 19.11.2019 - VI ZR 141/18, NJW 2020, 545 — Entscheidungserheblichkeit einer Rechtsfrage als Voraussetzung für die Revisionszulassung (§ 543 Abs. 2 ZPO); nur grundsätzliche Rechtsfragen berechtigen zur Revision.
- BGH, Urt. v. 08.01.2019 - XI ZR 535/17, NJW 2019, 1296 — Zur Darlegungs- und Beweislastverteilung als zentralem Schwerpunktthema: die Partei, die sich auf einen anspruchsbegründenden Umstand beruft, trägt die Beweislast.
- BGH, Beschl. v. 26.06.2018 - VIII ZR 289/17, NJW-RR 2018, 966 — Erfordernis des Hinweises vor Klageabweisung; fehlender Hinweis kann Gehörsverletzung nach Art. 103 Abs. 1 GG begründen.

## Kommentarliteratur

- Zöller/Greger ZPO, § 139 Rn. 1 ff. (Materielle Prozessleitung, Hinweispflicht)
- MüKo ZPO/Becker-Eberhard § 286 Rn. 1 ff. (Entscheidungserheblichkeit und Beweislast)
- Thomas/Putzo ZPO, § 359 Rn. 1 ff. (Beweisbeschluss)

## Kriterien für ein Schwerpunktthema

Ein Thema ist Schwerpunkt, wenn:

- Es in mehreren Schriftsätzen kontrovers diskutiert wird
- Das Gericht einen ausdrücklichen Hinweis dazu erteilt hat
- Ein Beweisbeschluss zu diesem Punkt ergangen ist
- Rechtsprechung der Parteien zu diesem Punkt zitiert wird
- Die Entscheidung im Verfahren von diesem Punkt maßgeblich abhängt

## Anzahl

Drei bis fünf Schwerpunktthemen. Bei einfachen Verfahren können es weniger sein; bei komplexen Verfahren werden trotzdem nicht mehr als fünf ausgewiesen — die übrigen Fragen werden in den Tabellen erfasst.

## Outputformat

```markdown
## Schwerpunktthemen

### 1. [Bezeichnung des Schwerpunktthemas]

**Beschreibung:** [Kurze Darstellung der Rechtsfrage]

**Parteiposition Kläger:** [Position ohne Wertung]

**Parteiposition Beklagter:** [Position ohne Wertung]

**Einschlägige Rechtsprechung (aus Akte):** [Zitat mit Aktenzeichen und Datum soweit in Schriftsätzen genannt]

**Fundstellen:** [Schriftsatz Bl. ...]

---
```

## Beispiel

### 1. Verjährung des Mangelbeseitigungsanspruchs

**Beschreibung:** Streitig ist, ob der Schadensersatzanspruch der Klägerin nach § 634a Abs. 1 Nr. 1 BGB (zwei Jahre ab Abnahme) bereits verjährt ist.

**Parteiposition Klägerin:** Verjährungsfrist beginnt erst mit Kenntnis des verdeckten Mangels; Frist läuft noch. Gestützt auf BGH Urt. v. 08.07.2021 — VII ZR 149/20.

**Parteiposition Beklagte:** Fristbeginn ist objektiv der Abnahmezeitpunkt; zwei Jahresfrist bereits abgelaufen. Gestützt auf BGH Urt. v. 12.03.2015 — VII ZR 173/13.

**Fundstellen:** Klageschrift Bl. 30-32; Klageerwiderung Bl. 55-58.

---

### 2. Wirksamkeit der Abnahme unter Vorbehalt

**Beschreibung:** Streitig ist, ob das unterzeichnete Abnahmeprotokoll einen Vorbehalt enthält oder vorbehaltlos ist.

**Parteiposition Klägerin:** Abnahme erfolgte unter Vorbehalt nach § 640 Abs. 1 S. 2 BGB (Bl. 20-21 Anlage K 2).

**Parteiposition Beklagte:** Protokoll enthält keinen Vorbehalt; vorbehaltlose Abnahme liegt vor.

**Fundstellen:** Klageschrift Bl. 20-22; Klageerwiderung Bl. 48-50.

## Hinweis

Schwerpunktthemen werden neutral dargestellt. Die Identifikation eines Themas als Schwerpunkt bedeutet keine Einschätzung, welche Seite in dieser Frage Recht hat.
