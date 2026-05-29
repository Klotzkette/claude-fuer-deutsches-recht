---
name: examens-prognose
description: "Examensprognose auf Basis bisheriger JPA-Klausuren und BMJV-Statistiken: Anwendungsfall Student will Lernzeit auf wahrscheinliche Themen konzentrieren und fragt welche Schwerpunkte das Justizprüfungsamt bisher prüfte. Examensvorbereitung 1. und 2. Staatsexamen, JAG Bundesland, BMJV-Statistiken. Prüfraster vergangene JPA-Klausuren analysieren, Häufigkeits-Statistik erstellen, Schwerpunktbereiche gewichten, Prognose mit Konfidenz versehen. Output gewichtete Themenliste mit Lernprioritaet und Trefferwahrscheinlichkeit je Rechtsgebiet. Abgrenzung zu Examensvorbereitung-Fragen für Uebungsklausuren und zu Lernplan."
---

# Examensprognose / JPA-Statistik

## Zweck

Dieser Skill analysiert **vergangene Examsklausuren** desselben Justizprüfungsamts (JPA) und erstellt eine **gewichtete Prognose** für kommende Prüfungen. Er hilft dabei, Lernzeit auf examensrelevante Themen zu konzentrieren, statt gleichmäßig über alle Rechtsgebiete zu verteilen.

Grundlage:
- Vom Nutzer hochgeladene **JPA-Klausuren** aus dem Lernprofil
- Öffentlich bekannte **Statistiken des BMJV** (Bundesministerium der Justiz) zur Bestehensquote und Fächerverteilung
- **JPA-spezifische Schwerpunkte** (bekannte Präferenzen einzelner Prüfungsämter)
- **Aktuelle Rechtsentwicklungen** (z. B. BGB-Reformen, neue BGH-Leitentscheidungen)

**Wichtiger Vorbehalt:** Eine Prognose ist eine Gewichtungshilfe für die Lernzeitplanung, keine Vorhersage. Alle Prognosepunkte werden mit `[UNSICHER – Prognose]` markiert.

## Eingaben

1. Lernprofil (`~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`) → Bundesland/JPA, Prüfungsziel, hochgeladene Klausuren
2. Optional: Pfad zu spezifischen Altklausuren (selbes JPA oder vergleichbares JPA)
3. Optional: `--statistik` → zeigt BMJV-Statistiken und bekannte Bundesland-Daten
4. Rechtsgebiet (Argument oder interaktiv)

## Ablauf

### Schritt 1: Materialprüfung

Das Plugin prüft, welche JPA-Klausuren vorliegen:
- Weniger als 5 Klausuren vom selben JPA → Ausgabe mit `WENIG MATERIAL`-Hinweis
- Klausuren von einem anderen JPA desselben Bundeslandes → verwendbar, aber mit Hinweis
- Keine eigenen Klausuren → reine BMJV-Statistik und bekannte Muster, stark generisch

### Schritt 2: Klausuranalyse

Für jede vorliegende Klausur:
- Welches Rechtsgebiet? Welche Normen stehen im Mittelpunkt?
- Welcher Aufbautyp (Anspruchsgrundlagenprüfung / Straftatprüfung / Verwaltungsakt)?
- Welche Streitstände wurden abgefragt?
- Wiederholungsmuster: Was kam in 2 oder mehr Klausuren vor?

### Schritt 3: Gewichtungsmatrix

Das Plugin erstellt eine gewichtete Themenmatrix:

| Thema | Häufigkeit (eigene Klausuren) | BMJV-Relevanz | Letzte Prüfung | Gewicht |
|---|---|---|---|---|
| § 280 Abs. 1 BGB – Schadensersatz | hoch | hoch | 2023 | ⬆⬆ |
| § 823 Abs. 1 BGB – Deliktsrecht | mittel | hoch | 2022 | ⬆ |
| § 812 BGB – Bereicherungsrecht | niedrig | mittel | 2021 | ↔ |
| § 985 BGB – Herausgabeanspruch | niedrig | niedrig | 2020 | ⬇ |

`[UNSICHER – Prognose]` auf alle Gewichtungen.

### Schritt 4: Aktuelle Rechtsentwicklungen

Das Plugin prüft bekannte aktuelle Themen:
- **BGB-Reform 2022** (Sachmangelbegriff § 434, Verbrauchsgüterkauf): examensrelevant seit 2022/2023
- **DSA/DDG:** relevant in Medien- und IT-rechtlichen Schwerpunkten
- **BGH-Leitentscheidungen** der letzten 2 Jahre im jeweiligen Rechtsgebiet

Alle aktuellen Angaben: `[Modellwissen – prüfen; Stand des Trainings kann veraltet sein]`

### Schritt 5: Lernempfehlung

Auf Basis der Gewichtungsmatrix:
- **Priorität A:** Themen mit hoher Häufigkeit + hoher BMJV-Relevanz → höchste Lernzeit
- **Priorität B:** Mittel-Häufigkeit + aktuelle BGH-Relevanz → zweite Lernphase
- **Priorität C:** Selten + bereits gut beherrscht → nur Auffrischung nötig

## Quellen und Zitierweise

→ `../references/zitierweise.md`

**Für Prognosearbeit relevante Quellen:**
- BMJV, *Statistik der Rechtspflege* (jährlich, online), Bestehensquoten und Fächerverteilung
- NJW: jährliche Examensbesprechungen und Berichte zu Schwerpunktthemen
- JuS: regelmäßige Aufsätze zu examensrelevanten Problemkreisen
- RÜ (Repetitorium – Examensfälle): aktuelle Fallbesprechungen aus echten Examensklausuren

**Für Bundesland-spezifische Daten:**
- JPA-Websites (Bayern: www.justizexamen.de; NRW: www.jpa.nrw.de; BW: www.justiz.bwl.de)
- Öffentlich zugängliche Klausurensammlungen der Universitäten

**Für inhaltliche Kontrolle:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

### Examensprognose (Vollformat)

```
**Examensprognose – [Rechtsgebiet] – [Bundesland] / JPA [X]**
Stand: [Datum der Analyse]

⚠️ Hinweis: Diese Prognose ist eine Lernzeit-Gewichtungshilfe, keine Vorhersage.
Alle Punkte mit [UNSICHER – Prognose] markiert.

**Datenbasis:**
- [N] eigene JPA-Klausuren analysiert [WENIG MATERIAL falls <5]
- BMJV-Statistik [Jahr]
- Bekannte JPA-Präferenzen [Bundesland]

**Gewichtungsmatrix:**
[Tabelle]

**Priorität A – Schwerpunkt Lernzeit:**
1. [Thema]: [Begründung] [UNSICHER – Prognose]
2. [Thema]: …

**Priorität B – Zweite Lernphase:**
[…]

**Aktuelle Rechtsentwicklungen die du kennen solltest:**
- [Thema]: [Kurzbeschreibung] [Modellwissen – prüfen]

**Verknüpfte Skills:**
→ /jurastudium:lernplan (Prognose in Lernplan übertragen)
→ /jurastudium:examensvorbereitung-fragen --bundesland [X] [Rechtsgebiet]
```

## Beispiel

**Anfrage:** Examensprognose BGB Schuldrecht, Bayern, basierend auf 7 JPA-Klausuren

**Ausgabe (Auszug):**

Gewichtungsmatrix (Auszug):

| Thema | Klausur-Häufigkeit | BMJV-Relevanz | Gewicht |
|---|---|---|---|
| Leistungsstörungen §§ 280, 281, 323 BGB | 6/7 | sehr hoch | ⬆⬆ `[UNSICHER – Prognose]` |
| Kaufrecht §§ 433, 434, 437 BGB n. F. | 5/7 | hoch (seit Reform 2022) | ⬆⬆ |
| Deliktsrecht § 823 BGB | 4/7 | hoch | ⬆ |
| Stellvertretung §§ 164 ff. BGB | 3/7 | mittel | ↔ |
| Bereicherungsrecht §§ 812 ff. BGB | 2/7 | mittel | ↔ |

Priorität A: Leistungsstörungsrecht – kommt in fast jeder BGB-Klausur vor. Fokus auf §§ 280 Abs. 1, 3, 281 BGB; Fristlosigkeit § 323 Abs. 2 BGB; Rücktritt vs. Schadensersatz. lizenzpflichtige Literaturquelle/Ernst, §§ 280, 281 beherrschen. `[UNSICHER – Prognose]`

Aktuelle Rechtsentwicklungen:  
BGB-Reform 2022 (VerbrRRL): Neuer § 434 BGB – subjektiver, objektiver und montagebezogener Mangelbegriff. In Bayern erstmals in Klausuren ab Frühjahr 2023 abgefragt. `[Modellwissen – prüfen]`

## Risiken / typische Fehler

- **Prognose als Gewissheit behandeln:** `[UNSICHER – Prognose]` ist kein Disclaimer-Floskeln, sondern echter Vorbehalt. JPAs können spontan Schwerpunkte wechseln.
- **Altklausuren von anderem JPA als gleichwertig behandeln:** Zwischen NRW-JPA Düsseldorf und Bayern bestehen erhebliche Unterschiede im Klausurstil (NRW: sehr langer Sachverhalt; Bayern: kompakter mit vielen Prüfungspunkten).
- **Aktualitätslücken:** BGH-Entscheidungen der letzten 12 Monate sind im Modell möglicherweise nicht vollständig. Vor dem Examen: NJW und JuS der letzten zwei Hefte prüfen.
- **Nur Priorität-A-Themen lernen:** Examsklausuren enthalten bewusst seltene Normen als Differenzierungspunkte. Priorität-C-Themen nicht weglassen.
- **BMJV-Statistik fehlinterpretieren:** Bestehensquoten sagen nichts über Themenverteilung aus. Nur Klausuranalyse ergibt Themengewichtung.
