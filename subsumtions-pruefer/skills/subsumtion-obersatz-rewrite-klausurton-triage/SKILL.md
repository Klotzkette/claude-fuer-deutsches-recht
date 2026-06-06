---
name: subsumtion-obersatz-rewrite-klausurton-triage
description: "Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pro Tatbestandsmerkmal im Subsumtions Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Subsumtion: Obersatz – Definition – Untersatz – Ergebnis

## Arbeitsbereich

Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pro Tatbestandsmerkmal. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
