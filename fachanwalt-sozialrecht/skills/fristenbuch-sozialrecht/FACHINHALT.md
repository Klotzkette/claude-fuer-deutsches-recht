---
name: fristenbuch-sozialrecht
description: "Für Anwalt oder Sekretariat muss Fristen in Sozialrechtsverfahren erfassen und überwachen: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel."
---

# Anwalt oder Sekretariat muss Fristen in Sozialrechtsverfahren erfassen und ueberwachen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: Nur das im Skill betroffene Sozialgesetzbuch und die konkrete Verfahrensnorm heranziehen. Widerspruchsfrist nach Paragraf 84 SGG, Klagefrist nach Paragraf 87 SGG und einstweiliger Rechtsschutz nach Paragraf 86b SGG strikt trennen; Rechtsweg, Statthaftigkeit, aufschiebende Wirkung und Rechtsmittel gesondert prüfen.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

Fokus: Fristen in Sozialrechtsverfahren erfassen und überwachen. Widerspruch, Klage und Beschwerde haben unterschiedliche Auslöser und Sonderregeln; bei Untätigkeit gelten nach Paragraf 88 SGG grundsätzlich sechs Monate für den Antrag und drei Monate für den Widerspruch. Bekanntgabe nach Paragraf 37 SGB X und förmliche Zustellung getrennt feststellen. Ergebnis ist ein Fristenbucheintrag mit belegtem Auslöser, Hauptfrist und Vorfristen. Abgrenzung zu bescheid-frist-quick-check (Schnellprüfung) und widerspruchsfrist-und-zustellung-sgb (Detailprüfung).

### Fristenbuch Sozialrecht

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristenbuch Sozialrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zentralablage

`~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/fristenbuch.yaml`

Pro Eintrag:

```yaml
- mandat-az: SR-2026-0042
 mandant: Mueller, Hans
 vorgang: Bürgergeld-Bescheid 12.03.2026
 fristart: widerspruchsfrist
 rechtsgrundlage: "§ 84 Abs. 1 SGG"
 fristbeginn: 2026-03-16 # Zugang nach Vier-Tages-Fiktion § 37 Abs. 2 SGB X n.F. (PostModG, seit 1.1.2025): Aufgabe zur Post 12.03.2026 + 4 Tage = 16.03.2026
 hauptfrist: 2026-04-16
 vorfrist-tage: 5
 vorfrist: 2026-04-11
 zuständig: RA Mueller
 status: offen
 bemerkung: Widerspruchsbegründung benoetigt Akteneinsicht
```

## Standardfristen

### SGG

| Frist | Norm | Dauer |
|---|---|---|
| Widerspruchsfrist | § 84 Abs. 1 SGG | ein Monat ab Bekanntgabe; ein Jahr bei fehlender Rechtsbehelfsbelehrung § 66 Abs. 2 SGG |
| Klagefrist nach Widerspruchsbescheid | § 87 Abs. 1 SGG | ein Monat |
| Untätigkeitsklage | Paragraf 88 SGG | grundsätzlich sechs Monate nach Antrag, drei Monate nach Widerspruch; zureichenden Grund prüfen |
| Beschwerde gegen Beschlüsse des SG | § 173 SGG | ein Monat |
| Berufung gegen Urteile des SG | § 151 SGG | ein Monat |
| Revisionsfrist | § 164 SGG | ein Monat |
| Wiedereinsetzung | Paragraf 67 SGG | ein Monat ab Wegfall des Hindernisses |

### SGB X / SGB V

| Frist | Norm | Bedeutung |
|---|---|---|
| Vier-Tages-Fiktion der Bekanntgabe (seit 1.1.2025) | Paragraf 37 Absatz 2 SGB X | einfacher Brief im Inland: vierter Tag nach Aufgabe zur Post; fehlenden oder späteren Zugang gesondert prüfen |
| Genehmigungsfiktion Krankenkasse | § 13 Abs. 3a SGB V | drei Wochen (fünf Wochen bei MDK) |
| Entscheidungsfrist Reha-Antrag | § 18 SGB IX | zwei Monate |
| Überprüfungsantrag | § 44 SGB X | keine eigentliche Frist aber Wirkung nur für Vergangenheit |

## Berechnung Fristbeginn

- Einfacher Brief im Inland: Bekanntgabe am vierten Tag nach Aufgabe zur Post nach Paragraf 37 Absatz 2 SGB X. Früherer tatsächlicher Zugang verkürzt die Fiktion nicht. Fehlenden oder späteren Zugang gesondert prüfen; im Zweifel muss die Behörde Zugang und Zeitpunkt nachweisen. Altfälle vor 2025 nach damaligem Recht beurteilen.
- Elektronische Übermittlung, Bereitstellung zum Abruf und förmliche Zustellung unterscheiden. Bei Paragraf 37 Absatz 2 beziehungsweise 2a SGB X gelten die jeweiligen Bekanntgaberegeln; ein technischer Übertragungsnachweis allein ersetzt keinen Zustellnachweis.
- **Bekanntgabe durch Aushaendigung** Tag der Aushaendigung.
- Widerspruchs- und Klagefristen nach Paragraf 64 SGG berechnen: Beginn grundsätzlich am Folgetag, Monatsende nach dem entsprechenden Tag beziehungsweise dem letzten Tag des Monats; Wochenende und gesetzlichen Feiertag nach Absatz 3 berücksichtigen. Paragraf 26 SGB X für verwaltungsverfahrensrechtliche Fristen getrennt prüfen.

## Vorfristen

- Standard fünf Werktage vor Hauptfrist.
- Bei Klagefristen Vorfrist mindestens sieben Tage (Akteneinsicht beA-Versand Anlagenkonvolut).
- Eskalation bei Vorfrist-Erreichung an zuständigen Anwalt.

## Pflege

- Bei Eingang Bescheid: sofort Eintrag im Fristenbuch.
- Bei Eingang Widerspruchsbescheid: Eintrag Klagefrist.
- Bei Untätigkeit: Antrag und Widerspruch trennen; sechs beziehungsweise drei Monate nach Paragraf 88 SGG als frühesten regulären Klagezeitpunkt erfassen, ohne damit einen Erfolg zu garantieren.
- Bei Bewilligung mit Änderungsvorbehalt: ggf. Wiedervorlage.

## Ausgabe

- `fristenbuch.yaml` aktualisiert
- `fristen-uebersicht.md` als Sekretariats-Bericht (Tagesbericht nächste sieben Tage)
- Bei Vorfristerreichung: Erinnerungs-Eintrag im Sekretariats-Tagesbrief (Plugin `kanzlei-allgemein`)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Sicherheit

- Niemals Fristen ändern ohne dokumentierte Begründung.
- Audit-Trail in der Aktenchronik.
- Sekretariat und Anwalt gegenseitig prüfen.

## Triage — kläre bei jedem neuen Fristeneintrag

1. Aufgabe zur Post belegt? Bescheiddatum und tatsächlichen Versand nicht gleichsetzen; Bekanntgabefiktion ab dem belegten Aufgabedatum berechnen.
2. Fehlender oder späterer Zugang vorgetragen? Beleglage und behördliche Nachweispflicht prüfen; früherer Zugang verkürzt die Fiktion nicht.
3. Rechtsbehelfsbelehrung vorhanden und korrekt? — bei Fehler Jahresfrist § 66 Abs. 2 SGG
4. Feiertag oder Wochenende am Ende einer SGG-Frist? Verschiebung nach Paragraf 64 Absatz 3 SGG prüfen; keine pauschale Vermischung mit Paragraf 26 SGB X.
5. Sekretariat und verantwortlicher Anwalt im Fristenbuch eingetragen? — Vier-Augen-Prinzip für Kanzleisicherung

## Aktuelle Rechtsprechung

Normabgleich vom 16.10.2026: [Paragraf 37 SGB X](https://www.gesetze-im-internet.de/sgb_10/__37.html), [Paragraf 67 SGG](https://www.gesetze-im-internet.de/sgg/__67.html) und [Paragraf 88 SGG](https://www.gesetze-im-internet.de/sgg/__88.html). Geprüft wurden Bekanntgabe, Wiedereinsetzungsfrist und Untätigkeit; keine neue Vollprüfung sämtlicher Fristen oder Leistungsgebiete.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
