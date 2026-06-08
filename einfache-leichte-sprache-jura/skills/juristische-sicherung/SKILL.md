---
name: juristische-sicherung
description: "Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit Pflichten-Sicherung Fristen-Erhalt Rechtsfolgen-Klarheit Ausnahmen-Abbildung. Output juristische Sicherungs-Checkliste gesicherte Fassung. Abgrenzung zu elsj-einfache-sprache (Übertragung) und elsj-qualitaetsgate (Endprüfung)."
---

# Juristische Sicherung

Dieses Fachmodul vor und nach jeder Übertragung.

## Triage zu Beginn
1. Welche Fristen kommen im Originaltext vor — Datum, Fristbeginn, Fristende, Folgen?
2. Welche Pflichten (Muss-Handlungen) und welche Rechte (Kann-Optionen) sind enthalten?
3. Gibt es Ausnahmen oder Vorbehalte, die praktisch wichtig sein koennen?
4. Sind rechtliche Unsicherheiten oder offene Pruefungen im Originaltext erkennbar?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 58 VwGO — Rechtsbehelfsbelehrung und Fristverlaengerung bei fehlerhafter Belehrung
- § 355 BGB — Widerrufsrecht: Frist, Belehrung, Folgen bei fehlender Belehrung
- § 214 BGB — Wirkung der Verjährung
- § 130 BGB — Zugang als Fristbeginn

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Juristische Sicherungs-Matrix

```
## Juristische Sicherung — Pruefvermerk

Dokument: [TITEL / AKTENZEICHEN]
Geprueft am: [DATUM]

| Kategorie | Original | Erhalten? | Bemerkung |
|---|---|---|---|
| Frist | [Datum/Dauer] | ja/nein | [Fristbeginn, -ende, Folge] |
| Pflicht | [Muss-Handlung] | ja/nein | [Nicht abgeschwaecht?] |
| Recht | [Kann-Option] | ja/nein | [Als Option formuliert?] |
| Risiko | [Rechtsfolge] | ja/nein | [Klar aber nicht drohend?] |
| Ausnahme | [wenn vorhanden] | ja/nein | [Gesondert erklaert?] |
| Unsicherheit | [offene Fragen] | ja/nein | [Nicht als sicher dargestellt?] |

Gesamtbefund: freigabereif / nacharbeiten
Offene Punkte: [...]
```
## Bedeutungs-Matrix

Erstelle eine Tabelle:

| Original | Bedeutung | Muss erhalten bleiben? | Umsetzung |
| --- | --- | --- | --- |
| Frist | Datum, Beginn, Ende, Folge bei Versäumnis | immer | sichtbar und einfach |
| Pflicht | was die Person tun muss | immer | nicht abschwächen |
| Recht | was die Person tun darf oder kann | immer | als Option erklären |
| Risiko | Kosten, Klage, Vollstreckung, Sanktion | immer | klar, aber nicht drohend |
| Ausnahme | wann etwas nicht gilt | wenn praktisch relevant | gesondert erklären |
| Unsicherheit | Streit, fehlende Tatsachen, Prüfung offen | immer | nicht als sicher darstellen |

## Modalwörter sichern

Prüfe jedes Modalwort:

- **muss** bleibt muss.
- **kann** bleibt Möglichkeit.
- **darf** bleibt Erlaubnis.
- **soll** wird nicht automatisch zu muss.
- **unverzüglich** wird nicht einfach zu "bald", sondern erklärt.

## Fristen sichern

Bei jeder Frist:

- Datum nennen, wenn bekannt.
- Fristbeginn nennen.
- Fristende nennen.
- Folge nennen.
- Kontakt nennen, wenn die Person handeln soll.

## Rechtsbegriffe

Ein Rechtsbegriff darf ersetzt werden, wenn die Bedeutung vollständig erhalten
bleibt. Wenn nicht, bleibt der Begriff stehen und wird erklärt.

Beispiele für erklärungsbedürftige Wörter:

- Bescheid
- Widerspruch
- Klage
- Rechtskraft
- Vollstreckung
- Kündigung
- Widerruf
- Anfechtung
- Haftung
- Verjährung

## Prüfvermerk

Gib am Ende einen Vermerk aus:

```markdown
## Juristische Sicherung

- Fristen geprüft: ...
- Rechte und Pflichten geprüft: ...
- Risiken geprüft: ...
- Begriffe erklärt: ...
- Nicht geklärt: ...
```
