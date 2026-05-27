---
name: subsumtion-obersatz-definition-untersatz-ergebnis
description: "Fuehrt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pro Tatbestandsmerkmal."
---

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

- BGH, Urt. v. 17.10.2019 - III ZR 42/19, NJW 2020, 399 — Die juristische Subsumtion erfordert zunächst eine genaue Definition des TBM aus Gesetz, h.M. und Rechtsprechung; erst dann kann der Sachverhalt unter die Definition gebracht werden; eine „freie Wertung" ohne Normtext-Anbindung ist methodisch unzulässig.
- BVerfG, Beschl. v. 06.06.2018 - 1 BvL 7/14, NJW 2018, 2542 — Das Bestimmtheitsgebot (Art. 103 Abs. 2 GG im Strafrecht; Art. 20 Abs. 3 GG allgemein) verlangt, dass die Subsumtion intersubjektiv nachvollziehbar ist; reine Wertungssubsumtionen ohne normativen Anknüpfungspunkt sind verfassungsrechtlich bedenklich.
- BGH, Urt. v. 09.04.2019 - VI ZR 89/18, NJW 2019, 2162 — Ungeschriebene Merkmale (z.B. Verkehrspflichten) sind als zusätzliche TBM im Vier-Schritt zu prüfen; sie werden als richterrechtlich entwickeltes Tatbestandsmerkmal behandelt.
- BGH, Urt. v. 19.11.2014 - VIII ZR 79/14, NJW 2015, 473 — Im Untersatz ist ausschließlich auf die vom Tatsachengericht festgestellten (oder vom Nutzer behaupteten) Tatsachen abzustellen; hypothetische Sachverhaltsvarianten werden im Untersatz nicht berücksichtigt.

## Das Vier-Schritt-Schema

### Schritt 1 — Obersatz

**Struktur:** „[Person A] könnte gegen [Person B] einen Anspruch auf [Rechtsfolge] aus [§ Norm] haben."

**Beispiel:** „K könnte gegen V einen Anspruch auf Schadensersatz in Höhe von EUR 5.000 aus § 280 Abs. 1 BGB haben."

### Schritt 2 — Definition

Das TBM wird aus der herrschenden Meinung und/oder der Rechtsprechung definiert.

**Struktur:** „[TBM] liegt vor, wenn [Definition aus h.M./Rspr.]."

**Beispiel:** „Eine Pflichtverletzung liegt vor, wenn der Schuldner eine ihm obliegende Pflicht aus dem Schuldverhältnis nicht, nicht rechtzeitig oder nicht wie geschuldet erfüllt (§ 241 Abs. 1 BGB; BGH ständige Rechtsprechung)."

Das System gibt die Quelle der Definition an (Gesetz, BGH, EuGH, h.M.). Wenn die Definition unsicher ist, wird dies ausdrücklich markiert.

### Schritt 3 — Untersatz (Subsumtion)

Der Sachverhalt wird unter die Definition subsumiert.

**Struktur:** „Hier [hat A / liegt vor / fehlt es an]: [konkrete Sachverhaltsangabe des Nutzers]."

**Beispiel:** „Hier hat V die Lieferpflicht aus § 433 Abs. 1 BGB nicht erfüllt, indem er die Ware trotz Fälligkeit am 01.03.2025 nicht geliefert hat (Nutzerangabe: keine Lieferung erfolgt)."

**Kennzeichnung von Lücken:** Fehlt eine Tatsachenangabe, markiert das System das TBM als „offen" und listet auf, welche Beweise erforderlich sind.

### Schritt 4 — Ergebnis

Das System schließt mit einem Ergebnis für das jeweilige TBM:
- „TBM [Name] ist erfüllt."
- „TBM [Name] ist nicht erfüllt, weil [Grund]."
- „TBM [Name] ist fraglich; Ergebnis hängt von weiteren Tatsachen / Beweisen / Auslegung ab."

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

## Kommentarliteratur

- Larenz/Canaris Methodenlehre der Rechtswissenschaft (Vier-Schritt-Methode — theoretisch)
- Rüthers/Fischer/Birk Rechtstheorie (Subsumtionslehre — dogmatisch)
- Grüneberg BGB Einl. (Anspruchsaufbau in der Praxis)

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
