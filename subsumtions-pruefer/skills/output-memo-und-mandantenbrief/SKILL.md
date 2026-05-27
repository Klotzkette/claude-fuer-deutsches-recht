---
name: output-memo-und-mandantenbrief
description: "Erzeugt interne Aktennotiz (Rechtsmemo) oder externen Mandantenbrief als Ausgabe der Subsumtion. Klarer Unterschied: Memo fuer interne Nutzung mit juristischer Tiefe; Mandantenbrief fuer Betroffene in verstaendlicher Sprache. Beide mit Pflicht-Haftungshinweis."
---

# Output: Memo und Mandantenbrief

## Triage zu Beginn

1. Ist ein internes Memo oder ein externer Brief gewünscht?
2. Gibt es ein Aktenzeichen für das Memo?
3. Soll der Mandantenbrief eine Fristsetzung enthalten?
4. In welcher Sprache? (Deutsch / Englisch / Zweisprachig → Skill output-fremdsprachig-en-fr)

## Rechtsprechung und berufsrechtliche Grundlage

- BGH, Urt. v. 10.11.2020 - VI ZR 342/19, NJW 2021, 306 — Die Pflicht des Anwalts zur verständlichen Kommunikation mit dem Mandanten ergibt sich aus § 43 BRAO; Memos und Mandantenbriefe müssen so formuliert sein, dass der Mandant die wesentlichen Aussagen versteht und entsprechend handeln kann.
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Aktennotizen des Anwalts sind Bestandteil der Mandatsakte (§ 50 BRAO); sie müssen hinreichend dokumentieren, welche Beratung erteilt und welche Empfehlungen gegeben wurden.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Mandantenbriefe müssen Fristen deutlich erkennbar nennen; ein Anwalt, der eine drohende Frist im Brief nicht hervorhebt, verletzt seine Hinweispflicht.

## Zweck

Dieser Skill erzeugt zwei verschiedene Ausgabeformate auf Basis des Subsumtionsergebnisses: eine interne Aktennotiz (Rechtsmemo) für die Verwendung im juristischen Kontext und einen externen Mandantenbrief für die Kommunikation mit dem Betroffenen. Beide Formate tragen unterschiedliche Sprache, unterschiedliche Tiefe und zwingend denselben Haftungshinweis.

## Format 1: Interne Aktennotiz (Rechtsmemo)

### Zweck des Memos

Das Memo dokumentiert die Subsumtion intern, dient als Arbeitsgrundlage und als Grundlage für das weitere Vorgehen. Es ist kein Schriftsatz und kein anwaltliches Beratungsschreiben.

### Aufbau

```
AKTENNOTIZ / RECHTSMEMO
Erstellt: [Datum]
Betreff: [Rechtsfrage / Norm / Sachverhalt kurz]
Aktenzeichen (intern): [optional]
---

I. SACHVERHALT (NUTZEREINGABE)
[Zusammenfassung des Sachverhalts aus Nutzereingaben — keine eigenen Ergänzungen]

II. GEPRÜFTE NORM(EN)
[Liste der geprüften Normen]

III. SUBSUMTION
[Vier-Schritt-Schema je TBM; Ergebnis je TBM]

IV. EINWENDUNGEN / EINREDEN
[Geprüfte Gegenrechte; Ergebnis]

V. RECHTSFOLGE
[Bestimmte Rechtsfolge, Höhe, Nebenansprüche]

VI. BEWEISBEDARF
[Offene TBM; fehlende Belege; Risikohinweis]

VII. EMPFEHLUNG
[Nächste Schritte: Schriftsatz / Widerspruch / Anwalt / Abbruch]

VIII. WARNHINWEIS
Dieses Memo ist ein mechanisch erzeugtes Arbeitsdokument auf Basis der Nutzerangaben.
Es ist keine Rechtsberatung und keine anwaltliche Stellungnahme.
```

### Sprachstil Memo

Juristisch präzise; Paragrafenangaben vollständig; Zitate im BGH-Format; Abkürzungen bei einmaliger Ausschreibung zulässig.

## Format 2: Mandantenbrief

### Zweck des Mandantenbriefs

Der Mandantenbrief richtet sich an den Betroffenen (nicht-juristischen Leser). Er erklärt das Ergebnis in verständlicher Sprache und gibt klare Handlungsempfehlungen.

### Aufbau

```
[Ort, Datum]
Betreff: Ihre Anfrage zu [Sachverhalt kurz]
Sehr geehrte/r [Name],

[Einleitung: kurze Zusammenfassung des Anliegens]
[Ergebnis in Alltagssprache: Was haben wir geprüft? Was hat sich ergeben?]
[Was bedeutet das für Sie? Mögliche nächste Schritte.]
[Was Sie noch brauchen: Belege, Fristen, Ansprechpartner]

Mit freundlichen Grüßen
[Absender — ggf. Kanzlei / Beratungsstelle]
```

### Pflicht-Haftungshinweis im Mandantenbrief

> **Wichtiger Hinweis:** Dieses Schreiben ist das Ergebnis einer mechanischen Prüfung auf Basis der von Ihnen genannten Tatsachen und der von Ihnen gewählten Norm. Es ist keine Rechtsberatung und keine anwaltliche Stellungnahme. Es ersetzt nicht die Prüfung durch einen zugelassenen Rechtsanwalt. Wenn Sie rechtliche Schritte einleiten oder auf dieses Ergebnis vertrauen möchten, wenden Sie sich bitte zuerst an einen Fachanwalt.

### Sprachstil Mandantenbrief

Verständlich, direkt, ohne Fachbegriffe (oder mit sofortiger Erklärung). Details in Skill `output-alltagssprache-de`.

## Auswahl durch Nutzer

Das System fragt: Welches Format benötigen Sie?
- (A) Interne Aktennotiz (Rechtsmemo)
- (B) Mandantenbrief (externer Brief an Betroffene)
- (C) Beides

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
