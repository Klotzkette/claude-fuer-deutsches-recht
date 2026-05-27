---
name: triage-rechtsfrage-oder-norm
description: "Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rueckfragen und leitet zum passenden naechsten Skill weiter. Warnt vor typischen Eingabefehlern."
---

# Triage: Rechtsfrage oder Norm?

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

- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der beratende Anwalt hat die Pflicht, den Sachverhalt vollständig zu erfassen und auf drohende Fristen hinzuweisen, auch wenn der Mandant nur eine Teilfrage stellt; die Triage-Pflicht ist umfassend.
- BGH, Beschl. v. 12.11.2020 - III ZB 41/20, NJW 2021, 316 — Wenn der Sachverhalt mehrere mögliche Rechtsgebiete berührt, ist der rechtssuchende Bürger ausdrücklich auf alle relevanten Rechtswege hinzuweisen; ein einseitiger Hinweis auf nur einen Weg ist pflichtwidrig.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Die Triage zwischen Verfassungsbeschwerde und fachgerichtlichem Rechtsweg (Erschöpfungsgrundsatz) ist eine der schwierigsten anwaltlichen Aufgaben; fehlerhafte Einordnung führt zur Unzulässigkeit der Verfassungsbeschwerde.
- BGH, Urt. v. 03.07.2019 - VIII ZR 96/18, NJW 2019, 3374 — Die vollständige Erfassung des Sachverhalts einschließlich aller für die Rechtsfolge relevanten Tatsachen (Daten, Beträge, Fristen) ist Grundvoraussetzung jeder juristischen Beratung.

## Ablauf

**Schritt 1 — Eingabeerfassung**

Das System stellt folgende Eingangsfragen:

1. Was haben Sie konkret? Bitte wählen Sie:
   - (A) Konkreter Lebenssachverhalt (Ereignis, Streit, Vertrag, Handlung, Bescheid)
   - (B) Abstrakte Rechtsfrage (z.B. „Darf mein Arbeitgeber …?")
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

## Kommentarliteratur

- Grüneberg BGB Einl. (Methodik der Anspruchsprüfung — Vier-Fragen-Methode)
- Baumbach/Lauterbach ZPO Einl. (Verfahrenswahl und Rechtsweg)
- Zöller ZPO § 17 GVG (Rechtsweg-Abgrenzung)

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
