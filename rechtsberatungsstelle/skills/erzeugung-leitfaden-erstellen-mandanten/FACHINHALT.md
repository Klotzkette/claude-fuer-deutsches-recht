---
name: erzeugung-leitfaden-erstellen-mandanten
description: "Für [VERALTET] Formularerstellung → siehe `/entwurf`: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen."
---

# [VERALTET] Formularerstellung → siehe `/entwurf`

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Formular- und Schriftstückaufgaben: `/entwurf [Schriftstücktyp]`.

## Rechtlicher Rahmen

### Hintergrund der Zusammenführung

Die Trennung zwischen "Formularerstellung" und "Schriftsatzerstellung" war in der Praxis studentischer Rechtsberatungsstellen künstlich: Ein Beratungshilfe-Antrag (BerH 1) ist juristisch kein anderes Arbeitsergebnis als ein Widerspruchsschreiben — beide erfordern Sachverhaltsaufnahme, Normprüfung und Supervisoren-Freigabe nach § 6 Abs. 2 RDG.

### Relevante Normen für die Nachfolge-Skill `/entwurf`

- **§ 1 BerHG** — Voraussetzungen der Beratungshilfe: BerH 1-Antrag ist vor Leistungserbringung beim Amtsgericht einzureichen; Studenten müssen die Voraussetzungen (Bedürftigkeit, keine anderweitige Beratungsmöglichkeit) prüfen.
- **§ 117 ZPO** — PKH-Antrag: Einreichung mit Klage oder gesondertem Schriftsatz; wirtschaftliche Verhältnisse vollständig darlegen (Erklärung über persönliche und wirtschaftliche Verhältnisse, Formular bewilligen PKH-Schein).
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Ausgefüllte Formulare, die Rechtspositionen des Mandanten begründen oder geltend machen, sind keine formale Routineaufgabe — sie erfordern inhaltliche Supervisoren-Prüfung.
- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht: Formulare enthalten sensitive Mandantendaten; strenge Vertraulichkeit.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

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

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben bei konkreten Schriftstücken und Formularen: `skills/entwurf/SKILL.md`, Sektion "Quellenpflicht".

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
