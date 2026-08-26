---
name: zeilenprompts-definieren
description: "Für Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Zeilentyp, Normverankerung, Eindeutigkeit. Output: Zeilenprompts-Dokument. Abgrenzung: nicht Spaltenprompts.

### /tabellenreview-3d:zeilenprompts-definieren

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen


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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Grenzen

Wenn die meisten Zeilen einen ähnlichen Zeilenprompt brauchen ist das ein Hinweis dass die Spaltenprompts angepasst werden müssen — der Effekt soll in den Spalten landen nicht in 80 Zeilenprompts.

## Audit-Hinweise

- Geprüft: 27.05.2026 (Halluzinations-Reparatur, Task 234)
- Frontmatter unveraendert. Keine Komma-Zahlen eingefuehrt. Kein Kyrillisch vorhanden.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
