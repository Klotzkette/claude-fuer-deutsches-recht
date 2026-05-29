---
name: zeilenprompts-definieren
description: "Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Zeilentyp, Normverankerung, Eindeutigkeit. Output: Zeilenprompts-Dokument. Abgrenzung: nicht Spaltenprompts."
---

# /tabellenreview-3d:zeilenprompts-definieren

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Spaltenprompts machen alle Dokumente vergleichbar. Zeilenprompts erlauben genau die Sonderbehandlung dort wo ein Dokument abweicht. Der Würfel bleibt strukturiert aber die Genauigkeit pro Dokument steigt.

## Typische Zeilenprompt-Muster

### Konzern- und Gruppenkontext

"Dieser Vertrag läuft zwischen Mutter- und Tochtergesellschaft im 100-Prozent-Konzern — AktG Paragraph 311 und Paragraph 312 (Konzernrecht und Abhängigkeitsbericht) zusätzlich prüfen. Marktüblichkeit der Konditionen ist Pflichtspalte."

### Fehlende Anlagen

"Anlage 7 (Leistungsbeschreibung) ist im Datenraum nicht enthalten — als Datenraum-Lücke in der Spalte Vollständigkeit markieren und im Disclosure-Letter abfragen."

### Sprachfremde Dokumente

"Vertrag in englischer Sprache. Bei Zitat: Originalwortlaut PLUS deutsche Arbeitsübersetzung in Klammern. Auslegungsmaßstab nach BGB Paragraph 133 und Paragraph 157 trotz Englisch."

### Älterer Vertrag

"Erstunterzeichnung älter als 5 Jahre. Prüfen ob Änderungsvereinbarungen Nachtraege oder muendliche Änderungen aktenkundig sind. Schriftformklausel beachten BGB Paragraph 125 Satz 2."

### Insolvenzbezogene Sonderklausel

"Klausel vorhanden die im Insolvenzfall eine Kündigung oder Aufrechnung erlaubt. Prüfen ob diese nach InsO Paragraph 119 unwirksam ist (insolvenzabhängige Lösungsklausel)."

### Konsumentenrelevanz

"Vertragspartner ist Verbraucher gemäß BGB Paragraph 13. Daher AGB-Kontrolle nach BGB Paragraph 305 ff. strenger; Klauselverbote BGB Paragraph 308 und Paragraph 309 zusätzlich prüfen."

### Datenraum-Disclosure

"Im Disclosure-Letter offengelegt — Disclosure-Bezug in der Spalte Garantiebezug eintragen."

## Pflichtfelder pro Zeilenprompt

```yaml
- zeile-id: vertrag-042
  pfad: "vdr/kunden/042-kundenvertrag-mueller-gmbh.pdf"
  hash: "sha256:..."
  zeilenprompt: |
    Konzernvertrag (Tochter zur Muttergesellschaft).
    Zusätzlich: AktG Paragraph 311 / Paragraph 312 (Konzernrecht).
    Marktüblichkeit der Vergütung in der Spalte 'Vergütung' bewerten.
  ueberschreibt-spalten: ["vergütung"]
  ergaenzt-spalten: ["change-of-control"]
```

## Ausgabe

- `zeilenprompts.yaml` mit pro Zeile (Dokument) der jeweiligen Sonderanweisung
- Konflikt-Prüfung: wenn ein Zeilenprompt einer Pflicht-Spalte widerspricht meldet der Skill den Konflikt zur Prüfer-Entscheidung.

## Grenzen

Wenn die meisten Zeilen einen ähnlichen Zeilenprompt brauchen ist das ein Hinweis dass die Spaltenprompts angepasst werden müssen — der Effekt soll in den Spalten landen nicht in 80 Zeilenprompts.

## Audit-Hinweise

<!-- AUDIT 27.05.2026 -->
- Geprüft: 27.05.2026 (Halluzinations-Reparatur, Task 234)
- Frontmatter unveraendert. Keine Komma-Zahlen eingefuehrt. Kein Kyrillisch vorhanden.
