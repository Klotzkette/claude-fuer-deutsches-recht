---
name: erzeugung-leitfaden-erstellen-mandanten
description: "Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behörde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozialrecht Mietrecht Arbeitsrecht. Prüfraster Formular-Typ bestimmen, Pflichtfelder ermitteln, Rückfragen minimal halten, Fristen beachten. Output ausgefuelltes Formular oder Antragsentwurf mit Einreichungshinweisen. Abgrenzung zu Entwurf für individuelle Schriftsaetze und zu Mandantenbrief im Rechtsberatungsstelle: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# [VERALTET] Formularerstellung → siehe `/entwurf`

## Arbeitsbereich

Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behörde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozialrecht Mietrecht Arbeitsrecht. Prüfraster Formular-Typ bestimmen, Pflichtfelder ermitteln, Rückfragen minimal halten, Fristen beachten. Output ausgefuelltes Formular oder Antragsentwurf mit Einreichungshinweisen. Abgrenzung zu Entwurf für individuelle Schriftsaetze und zu Mandantenbrief. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Diese Skill wurde im Rahmen des Umbaus auf Version 2 vollständig in `skills/entwurf/` überführt. Der Befehl `/entwurf` übernimmt alle Aufgaben, die zuvor hier lagen: Erstellung von Erstentwürfen für Antragsformulare (Beratungshilfe-Antrag BerH 1, PKH-Antrag nach § 117 ZPO, Widerspruchsvordrucke, Behördenformulare), Ausfüllen aus Fallnotizen, Rechtsgebiet-spezifische Muster und formvorschriftengerechte Formatierung.

Die Skill nimmt keine Eingaben mehr entgegen und erzeugt keine Ausgaben. Sie verbleibt im Dateisystem als Migrationshinweis für ältere Dokumentationen und Semesterskripte.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Formular- und Schriftstückaufgaben: `/entwurf [Schriftstücktyp]`.

## Rechtlicher Rahmen

### Hintergrund der Zusammenführung

Die Trennung zwischen "Formularerstellung" und "Schriftsatzerstellung" war in der Praxis studentischer Rechtsberatungsstellen künstlich: Ein Beratungshilfe-Antrag (BerH 1) ist juristisch kein anderes Arbeitsergebnis als ein Widerspruchsschreiben — beide erfordern Sachverhaltsaufnahme, Normprüfung und Supervisoren-Freigabe nach § 6 Abs. 2 RDG.

### Relevante Normen für die Nachfolge-Skill `/entwurf`

- **§ 1 BerHG** — Voraussetzungen der Beratungshilfe: BerH 1-Antrag ist vor Leistungserbringung beim Amtsgericht einzureichen; Studierende müssen die Voraussetzungen (Bedürftigkeit, keine anderweitige Beratungsmöglichkeit) prüfen.
- **§ 117 ZPO** — PKH-Antrag: Einreichung mit Klage oder gesondertem Schriftsatz; wirtschaftliche Verhältnisse vollständig darlegen (Erklärung über persönliche und wirtschaftliche Verhältnisse, Formular bewilligen PKH-Schein).
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Ausgefüllte Formulare, die Rechtspositionen des Mandanten begründen oder geltend machen, sind keine formale Routineaufgabe — sie erfordern inhaltliche Supervisoren-Prüfung.
- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht: Formulare enthalten sensitive Mandantendaten; strenge Vertraulichkeit.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben bei konkreten Schriftstücken und Formularen: `skills/entwurf/SKILL.md`, Sektion "Quellenpflicht".

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund: GELOESCHT. Echtes Datum 22.10.2015 (Skill hatte 14.01.2016); echtes Thema Streitwert der Vollstreckungsgegenklage (§§ 3, 4 ZPO) — kein Bezug zu Beratungshilfe oder anwaltlicher Antragspruefungspflicht. Quelle: dejure.org/2015,32471. Ersatz: kein passender Beleg gefunden; Zeile entfernt.
-->
