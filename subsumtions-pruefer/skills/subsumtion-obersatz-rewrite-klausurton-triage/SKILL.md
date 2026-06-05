---
name: subsumtion-obersatz-rewrite-klausurton-triage
description: "Subsumtion Obersatz Rewrite Klausurton Triage: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Subsumtion Obersatz Rewrite Klausurton Triage

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Subsumtion Obersatz Rewrite Klausurton Triage** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `subsumtion-obersatz-definition-untersatz-ergebnis` | Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pro Tatbestandsmerkmal. |
| `subsumtions-rewrite-klausurton` | Schreibt falsche oder lueckenhafte Subsumtionen in einen knappen juristischen Klausurton um, ohne neue Tatsachen zu erfinden. Vier-Schritt-Schema: Obersatz, Definition, Subsumtion, Ergebnis je Tatbestandsmerkmal. |
| `triage-rechtsfrage-oder-norm` | Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill weiter. Warnt vor typischen Eingabefehlern. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Subsumtion Obersatz Rewrite Klausurton Triage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `subsumtion-obersatz-definition-untersatz-ergebnis`

**Fokus:** Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pro Tatbestandsmerkmal.

# Subsumtion: Obersatz – Definition – Untersatz – Ergebnis

## Triage zu Beginn — kläre vor dem Vier-Schritt

1. Ist die Norm in TBM zerlegt? → falls nein: zuerst `norm-zerlegen-in-tatbestandsmerkmale`
2. Welches TBM soll jetzt subsumiert werden? (Nummerierung aus TBM-Liste)
3. Hat der Nutzer konkrete Sachverhaltstatsachen für dieses TBM mitgeteilt?
4. Ist die Definition des TBM aus Gesetz, h.M. oder BGH-Rechtsprechung bekannt?
5. Ist das TBM ein unbestimmter Rechtsbegriff? → Skill `unbestimmte-rechtsbegriffe-pruefen` parallel

## Zweck

Dieses Vier-Schritt-Schema ist die Grundmethode juristischer Fallbearbeitung. Der Skill führt das Schema für jedes Tatbestandsmerkmal durch.

## Aktuelle Rechtsprechung zur Subsumtionsmethode

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Das Vier-Schritt-Schema

### Schritt 1 — Obersatz

**Struktur:** "[Person A] könnte gegen [Person B] einen Anspruch auf [Rechtsfolge] aus [§ Norm] haben."

**Beispiel:** "K könnte gegen V einen Anspruch auf Schadensersatz in Höhe von EUR 5.000 aus § 280 Abs. 1 BGB haben."

### Schritt 2 — Definition

Das TBM wird aus der herrschenden Meinung und/oder der Rechtsprechung definiert.

**Struktur:** "[TBM] liegt vor, wenn [Definition aus h.M./Rspr.]."

**Beispiel:** "Eine Pflichtverletzung liegt vor, wenn der Schuldner eine ihm obliegende Pflicht aus dem Schuldverhältnis nicht, nicht rechtzeitig oder nicht wie geschuldet erfüllt (§ 241 Abs. 1 BGB; BGH ständige Rechtsprechung)."

Das System gibt die Quelle der Definition an (Gesetz, BGH, EuGH, h.M.). Wenn die Definition unsicher ist, wird dies ausdrücklich markiert.

### Schritt 3 — Untersatz (Subsumtion)

Der Sachverhalt wird unter die Definition subsumiert.

**Struktur:** "Hier [hat A / liegt vor / fehlt es an]: [konkrete Sachverhaltsangabe des Nutzers]."

**Beispiel:** "Hier hat V die Lieferpflicht aus § 433 Abs. 1 BGB nicht erfüllt, indem er die Ware trotz Fälligkeit am 01.03.2025 nicht geliefert hat (Nutzerangabe: keine Lieferung erfolgt)."

**Kennzeichnung von Lücken:** Fehlt eine Tatsachenangabe, markiert das System das TBM als "offen" und listet auf, welche Beweise erforderlich sind.

### Schritt 4 — Ergebnis

Das System schließt mit einem Ergebnis für das jeweilige TBM:
- "TBM [Name] ist erfüllt."
- "TBM [Name] ist nicht erfüllt, weil [Grund]."
- "TBM [Name] ist fraglich; Ergebnis hängt von weiteren Tatsachen / Beweisen / Auslegung ab."

## Gesamtergebnis

Nach Durchlauf aller TBM bildet das System ein Gesamtergebnis:
- Alle TBM erfüllt → Anspruch/Tatbestand besteht dem Grunde nach (vorbehaltlich Einreden)
- Ein oder mehrere TBM nicht erfüllt → Anspruch/Tatbestand scheitert an [TBM-Name]
- TBM fraglich → Ergebnis offen; Hinweis auf Klärungsbedarf

## Entscheidungsbaum

```
TBM-Definition bekannt?
├─ Ja (Gesetz/BGH) → Definition formulieren → Untersatz → Ergebnis
└─ Nein / unsicher → h.M. recherchieren → Kommentarhinweis geben
 → Untersatz mit Vorbehalt → Ergebnis fraglich
```

## Output-Template Vier-Schritt (Auszug)

**Adressat:** Richter/Anwalt — Tonfall sachlich-juristisch
```
[Aktenzeichen / TBM Nr. X]

Obersatz:
[Person A] könnte gegen [Person B] einen Anspruch auf [RF] aus [§ Norm] haben.

Definition:
[TBM] liegt vor, wenn [Definition aus h.M./Rspr.].

Untersatz:
Hier [liegt vor / fehlt es an]: [Sachverhaltsbeschreibung].

Ergebnis:
TBM [Name] ist [erfüllt / nicht erfüllt / fraglich].
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `subsumtions-rewrite-klausurton`

**Fokus:** Schreibt falsche oder lueckenhafte Subsumtionen in einen knappen juristischen Klausurton um, ohne neue Tatsachen zu erfinden. Vier-Schritt-Schema: Obersatz, Definition, Subsumtion, Ergebnis je Tatbestandsmerkmal.

# Subsumtion im Klausurton neu schreiben

## Ziel

Dieser Skill schreibt fehlerhafte oder lückenhafte Subsumtionen in sauberen juristischen Klausurton um. Er fügt keine neuen Tatsachen hinzu und erfindet keine Belege. Er korrigiert Obersatz, Definition, Subsumtion und Ergebnis — je Tatbestandsmerkmal getrennt.

## Klausurton: Stilregeln

### Gutachtenstil (Standard für Klausur und Hausarbeit)

| Element | Stilregel | Beispiel |
|---|---|---|
| Obersatz | Konjunktiv; Anspruchsfrage | "A könnte gegen B einen Anspruch auf Zahlung von EUR X aus § 433 Abs. 2 BGB haben." |
| Definition | Abstrakt, ohne Bezug auf konkreten Fall; mit Quellenhinweis | "Unter einer Sache iSd § 90 BGB versteht man jeden körperlichen Gegenstand." |
| Subsumtion | Tatsachen des Falles unter Definition halten | "Hier ist der Pkw ein körperlicher Gegenstand und damit eine Sache iSd § 90 BGB." |
| Zwischenergebnis | Indikativ; klar | "Dieses Tatbestandsmerkmal ist erfüllt." |
| Gesamtergebnis | Indikativ; klar | "A hat gegen B einen Anspruch aus § 433 Abs. 2 BGB." |

### Urteilsstil (für Schriftsatz und Bescheid)

- Ergebnis steht am Anfang: "Die Klage ist begründet."
- Begründung folgt deduktiv: "Denn A hat gegen B einen Anspruch aus § 433 Abs. 2 BGB, weil ..."
- Kein Konjunktiv im Einstieg

## Typische Rewrite-Muster

### Fehler 1: Sprung-Subsumtion → Rewrite

**Vor:** "§ 433 Abs. 2 BGB: Der Kaufpreis ist zu zahlen. Hier ist er noch nicht gezahlt."

**Nach:** "Nach § 433 Abs. 2 BGB ist der Käufer verpflichtet, dem Verkäufer den vereinbarten Kaufpreis zu zahlen. Kaufpreis ist die im Kaufvertrag als Gegenleistung vereinbarte Geldsumme. Hier haben A und B im Kaufvertrag v. TT.MM.JJJJ einen Kaufpreis von EUR X vereinbart. Dieser ist nach Anlage K1 noch nicht bezahlt worden. Die Zahlungspflicht besteht daher."

### Fehler 2: Zirkelschluss → Rewrite

**Vor:** "Eine Pflichtverletzung liegt vor, weil B seine Pflichten verletzt hat."

**Nach:** "Eine Pflichtverletzung iSd § 280 Abs. 1 BGB ist jedes objektive Abweichen vom geschuldeten Verhalten. B schuldete nach dem Werkvertrag die Herstellung eines mangelfreien Werks (§ 631 Abs. 1 BGB). Die Lieferung erfolgte laut Abnahmeprotokoll (Anlage K2) mit Rissen in der Fassade. Dies weicht vom geschuldeten mangelfreien Zustand ab. Eine Pflichtverletzung liegt vor."

### Fehler 3: Konjunktiv im Schluss → Rewrite

**Vor:** "Das Tatbestandsmerkmal könnte vorliegen."

**Nach:** "Das Tatbestandsmerkmal liegt vor." oder "Das Tatbestandsmerkmal liegt nicht vor, weil [Begründung]."

### Fehler 4: Definition aus dem Sachverhalt → Rewrite

**Vor:** "Vereinbart" im Sinne der Parteienabsprache heißt, dass A und B das vereinbart haben.

**Nach:** "Vereinbart" iSd § 145 BGB setzt voraus, dass ein Angebot auf Abschluss eines Vertrags und eine Annahme vorliegen (§§ 145, 147 BGB). ...

## Rewrite-Workflow

1. **Fehlerdiagnose:** Obersatz, Definition, Subsumtion, Ergebnis je TBM markieren (vorhanden / fehlt / falsch).
2. **Priorität setzen:** Welcher Fehler ist am schwersten? (Sprung-Subsumtion, Zirkelschluss, falscher Stil)
3. **Rewrite:** Je TBM: Obersatz → Definition (mit Norm; Quelle als Prüfpunkt) → Tatsachen aus dem Sachverhalt → Zwischenergebnis.
4. **Stilkontrolle:** Konjunktiv im Obersatz? Indikativ im Zwischenergebnis? Tatsachen aus der Akte?
5. **Quellenkontrolle:** Jede Definition auf Norm oder (als Prüfpunkt) auf BGH-Linie gestützt?

## Quellen-Disziplin beim Rewrite

- Normtext aus gesetze-im-internet.de: live prüfen und exakt zitieren
- Rechtsprechungs-Definitionen: als Prüfpunkt markieren ("nach BGH [live zu prüfen unter dejure.org / bgh.de]")
- Keine Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen

## Ausgabe

Vollständige Rewrite-Passage je TBM; davor kurzer Fehlerhinweis ("Fehler: Sprung-Subsumtion → jetzt korrigiert"). Rechtsprechung nur mit live verifizierbarem Aktenzeichen.

## Quellenregel

- Normtext live prüfen: gesetze-im-internet.de.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, bgh.de).
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Nur Tatsachen aus der Akte verwenden; keine neuen Sachverhaltselemente erfinden.

## 3. `triage-rechtsfrage-oder-norm`

**Fokus:** Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill weiter. Warnt vor typischen Eingabefehlern.

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
