---
name: formular-erzeugung
description: "Referenz: VERALTET — bitte `/entwurf` verwenden. Diese Skill wurde in die Draft-Skill überführt, die die gesamte Schriftstück-Erstellung der Rechtsberatungsstelle einschließlich Formularausfüllung übernimmt. Lädt, wenn ein Studierender Formulare ausfüllen, Antragsvordrucke erstellen oder Formulargenerierung durchführen möchte."
---

# [VERALTET] Formularerstellung → siehe `/entwurf`

## Zweck

Diese Skill wurde im Rahmen des Umbaus auf Version 2 vollständig in `skills/entwurf/` überführt. Der Befehl `/entwurf` übernimmt alle Aufgaben, die zuvor hier lagen: Erstellung von Erstentwürfen für Antragsformulare (Beratungshilfe-Antrag BerH 1, PKH-Antrag nach § 117 ZPO, Widerspruchsvordrucke, Behördenformulare), Ausfüllen aus Fallnotizen, Rechtsgebiet-spezifische Muster und formvorschriftengerechte Formatierung.

Die Skill nimmt keine Eingaben mehr entgegen und erzeugt keine Ausgaben. Sie verbleibt im Dateisystem als Migrationshinweis für ältere Dokumentationen und Semesterskripte.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Formular- und Schriftstückaufgaben: `/entwurf [Schriftstücktyp]`.

## Rechtlicher Rahmen

### Hintergrund der Zusammenführung

Die Trennung zwischen „Formularerstellung" und „Schriftsatzerstellung" war in der Praxis studentischer Rechtsberatungsstellen künstlich: Ein Beratungshilfe-Antrag (BerH 1) ist juristisch kein anderes Arbeitsergebnis als ein Widerspruchsschreiben — beide erfordern Sachverhaltsaufnahme, Normprüfung und Supervisoren-Freigabe nach § 6 Abs. 2 RDG.

### Relevante Normen für die Nachfolge-Skill `/entwurf`

- **§ 1 BerHG** — Voraussetzungen der Beratungshilfe: BerH 1-Antrag ist vor Leistungserbringung beim Amtsgericht einzureichen; Studierende müssen die Voraussetzungen (Bedürftigkeit, keine anderweitige Beratungsmöglichkeit) prüfen.
- **§ 117 ZPO** — PKH-Antrag: Einreichung mit Klage oder gesondertem Schriftsatz; wirtschaftliche Verhältnisse vollständig darlegen (Erklärung über persönliche und wirtschaftliche Verhältnisse, Formular bewilligen PKH-Schein).
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Ausgefüllte Formulare, die Rechtspositionen des Mandanten begründen oder geltend machen, sind keine formale Routineaufgabe — sie erfordern inhaltliche Supervisoren-Prüfung.
- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht: Formulare enthalten sensitive Mandantendaten; strenge Vertraulichkeit.

### Leitentscheidungen

- BGH, Urt. v. 14.01.2016 – IX ZR 115/15, NJW 2016, 957 Rn. 12 — Beratungshilfe: Anwaltliche Pflicht zur vollständigen Prüfung der Anspruchsvoraussetzungen vor Antragstellung; kein bloßes „Ausfüllen" eines Formulars.
- BGH, Urt. v. 10.10.2013 – IX ZR 337/12, NJW 2014, 145 Rn. 8 — PKH-Antrag: Vollständige Darlegung der wirtschaftlichen Verhältnisse als Wirksamkeitsvoraussetzung; unvollständige Angaben führen zu Ablehnung.
- BVerfG, Beschl. v. 14.07.1987 – 1 BvR 537/81, NJW 1988, 191 — Recht auf Zugang zu Rechtsberatung; Beratungshilfe als Grundlage für die Formularerstellung im sozialen Bereich.
- BVerwG, Urt. v. 25.03.2019 – 2 C 11/18, NVwZ 2019, 1050 Rn. 10 — Formvoraussetzungen behördlicher Antragsformulare; fehlerhafte Formulare können Fristen versäumen lassen.

### Kommentarliteratur

- Schütz, Das Recht der Beratungshilfe, 3. Aufl. 2020, § 1 BerHG Rn. 5 ff. — Voraussetzungen; Antragstellung; Formular BerH 1.
- Vorwerk, in: BeckOK ZPO, 53. Ed. (Stand 01.03.2025), § 117 Rn. 5 — PKH-Antrag: Inhalt, Form, Beilagen.
- Deckenbrock/Henssler, RDG, 5. Aufl. 2021, § 6 Rn. 20 — Aufsichtspflicht auch bei vermeintlich formalen Tätigkeiten wie Formularausfüllung (Doppelautoren-Kommentar).
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 242 Rn. 18 — Treu und Glauben bei der Antragstellung; keine unvollständigen oder irreführenden Angaben.

## Ablauf

**Stattdessen `/entwurf [Schriftstücktyp]` verwenden.**

```
/entwurf beratungshilfe-antrag
/entwurf pkh-antrag
/entwurf widerspruch-nebenkostenabrechnung
/entwurf mahnschreiben
```

Vollständiger Ablauf in `skills/entwurf/SKILL.md`:

1. Schriftstücktyp identifizieren und dem Musterbestand zuordnen
2. Sachverhalt aufnehmen; fehlende Angaben kennzeichnen (`[TATSACHE FEHLT: ...]`)
3. Formvorschriften und Einreichungsweg prüfen
4. Entwurf erstellen mit `[PRÜFEN]`- und `[UNSICHER]`-Flags
5. Supervisoren-Routing nach § 6 Abs. 2 RDG

## Ausgabeformat

Keine Ausgabe — diese Skill ist inaktiv. Weiterleitung auf `/entwurf`.

## Beispiel

Statt `/formular-erzeugung beratungshilfeantrag`:

```
/entwurf beratungshilfe-antrag
```

Der Befehl `/entwurf` füllt das Formular BerH 1 aus den Fallnotizen, kennzeichnet fehlende Pflichtangaben mit `[TATSACHE FEHLT: ...]` (z. B. Kontonummer für Bedürftigkeitsnachweis), und leitet nach Fertigstellung in die Supervisoren-Prüfung.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Unterlagen:** Bestehende Handreichungen, Semesterskripte oder Tutorenmaterialien, die auf `/formular-erzeugung` verweisen, auf `/entwurf` umschreiben.
- **Formularausfüllung als Routineaufgabe unterschätzen:** Formulare, die Rechtspositionen des Mandanten geltend machen (PKH, Beratungshilfe, Widerspruch), sind rechtliche Arbeitsergebnisse und unterliegen der Supervisoren-Prüfpflicht nach § 6 Abs. 2 RDG.
- **Falsche Angaben im BerH 1-Antrag:** Unvollständige oder unrichtige Angaben zur Bedürftigkeit können zu Ablehnung und ggf. zur Rückforderung bereits gewährter Beratungshilfe führen (§ 9 BerHG).

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben bei konkreten Schriftstücken und Formularen: `skills/entwurf/SKILL.md`, Sektion „Quellenpflicht".

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
