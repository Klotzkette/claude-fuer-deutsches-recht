---
name: triage-rechtsfrage-oder-norm
description: "Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill weiter. Warnt vor typischen Eingabefehlern im Subsumtions Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Triage: Rechtsfrage oder Norm?

## Arbeitsbereich

Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill weiter. Warnt vor typischen Eingabefehlern. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — erste Einordnung des Nutzeranliegens

1. Was bringt der Nutzer mit? → Sachverhalt / Norm / Frage / Kombinationen
2. Welches Rechtsgebiet ist wahrscheinlich einschlägig? (Zivilrecht / Strafrecht / Öffentl. Recht / EU)
3. Hat der Nutzer bereits eine Norm benannt oder sucht er noch eine?
4. Besteht Dringlichkeit (Fristen, Zustellungen, Vollstreckungshandlungen)? → Notfristen prüfen
5. Sind Mehrparteienkonstellationen oder ausländische Beteiligte erkennbar? → IPR-Hinweis

## Zweck

Dieser Skill ist der erste Schritt im Subsumtions-Workflow. Er stellt sicher, dass das System versteht, was der Nutzer mitgebracht hat: eine abstrakte Rechtsfrage, einen konkreten Lebenssachverhalt, eine benannte Norm oder eine Kombination davon.

## Zentrale Normen für häufige Triage-Situationen

- §§ 195 ff. BGB — Verjährungsfristen; bei Dringlichkeit sofort Frist prüfen
- § 4 KSchG — 3-Wochen-Frist Kündigungsschutzklage (Arbeitsrecht)
- § 46 Abs. 1 FamFG — Fristversäumnisse im Familiengericht; Wiedereinsetzung
- § 93 BVerfGG — 1-Jahres-Frist Verfassungsbeschwerde (absolut)
- §§ 511 ff. ZPO — Berufungsfristen (1 Monat ab Zustellung)

## Aktuelle Rechtsprechung zu Triage-Pflichten

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ablauf

**Schritt 1 — Eingabeerfassung**

Das System stellt folgende Eingangsfragen:

1. Was haben Sie konkret? Bitte wählen Sie:
 - (A) Konkreter Lebenssachverhalt (Ereignis, Streit, Vertrag, Handlung, Bescheid)
 - (B) Abstrakte Rechtsfrage (z.B. "Darf mein Arbeitgeber …?")
 - (C) Ich weiß bereits, welche Norm ich prüfen will
 - (D) Beides: Sachverhalt und Norm
 - (E) Ich weiß es nicht genau — bitte führe mich

2. Falls (A) oder (D): Sachverhalt in knappen Stichpunkten. Wer? Wann? Was? Dokumente?
3. Falls (B): Frage so präzise wie möglich formulieren
4. Falls (C) oder (D): Welche Norm genau (§, Absatz, Satz, Nr., Buchstabe)?

**Schritt 2 — Plausibilitätsprüfung**

Das System prüft:
- Ist die genannte Norm vollständig bezeichnet?
- Passt der Sachverhalt auf den ersten Blick zur Norm?
- Gibt es Rechtsgebiets-Fehlzuordnungen?

**Schritt 3 — Routing (Entscheidungsbaum)**

```
Sachverhalt ohne Norm?
├─ Ja → einschlaegige-normen-vorschlagen-de / -eu
Norm bereits bekannt?
├─ Ja → norm-zerlegen-in-tatbestandsmerkmale
Unklares Ziel?
├─ Ja → ziel-und-rechtsweg-bestimmung
Komplexitätsgrenze?
├─ Ja → mandatsabbruch-empfehlung-an-fachanwalt
```

## Fehlereingaben

- Norm ohne Paragrafenzeichen: System ergänzt und bestätigt beim Nutzer
- Sachverhalt zu allgemein: System stellt konkretisierende Rückfragen (Wer? Wann? Wo? Was?)
- Mehrere Normen gleichzeitig: System behandelt sie nacheinander und weist auf Konkurrenzfragen hin

## Output-Template Triage-Ergebnis

**Adressat:** Nutzer — Tonfall klar und verständlich

```
Ihr Sachverhalt wurde wie folgt erfasst:
- Rechtsgebiet: [Zivilrecht / Strafrecht / öffentl. Recht]
- Beteiligte: [A] vs. [B]
- Relevante Norm (Vorschlag): [§ Norm]
- Nächster Schritt: [Skill-Name]

Wichtige Fristen in Ihrem Fall:
- [Frist 1]: [Datum] — [§ Norm]
- [Frist 2]: ...

Bitte bestätigen Sie, dass ich den Sachverhalt richtig erfasst habe.
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
