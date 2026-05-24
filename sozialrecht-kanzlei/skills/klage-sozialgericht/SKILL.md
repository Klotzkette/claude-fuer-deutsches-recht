---
name: klage-sozialgericht
description: Entwurf einer Klage zum Sozialgericht nach §§ 87 ff. SGG. Klagefrist ein Monat nach Zustellung des Widerspruchsbescheids (§ 87 Abs. 1 SGG; bei fehlender Rechtsbehelfsbelehrung ein Jahr § 66 Abs. 2 SGG). Sachliche Zustaendigkeit Sozialgericht (§ 8 SGG) oertlich gewoehnlicher Aufenthaltsort des Klaegers (§ 57 SGG). Kein Anwaltszwang vor dem SG aber Versand ueber beA Pflicht. PKH-Antrag inkludiert (§ 73a SGG iVm §§ 114 ff. ZPO). Erzeugt Klageschrift Anlagenverzeichnis Beweisangebote.
---

# Klage zum Sozialgericht

## Voraussetzungen

- **Vorverfahren** durchgeführt — Widerspruchsbescheid liegt vor (§ 78 SGG).
- **Untätigkeitsklage** alternativ möglich nach drei Monaten Untätigkeit der Widerspruchsbehörde (§ 88 SGG).
- **Klagefrist** ein Monat ab Zustellung des Widerspruchsbescheids (§ 87 Abs. 1 SGG); ein Jahr bei fehlender Rechtsbehelfsbelehrung (§ 66 Abs. 2 SGG).

## Zuständigkeit

- **Sachlich** Sozialgericht (§ 8 SGG) für Streitigkeiten in den Angelegenheiten der gesetzlichen Sozialversicherung der Grundsicherung für Arbeitsuchende des Asylbewerberleistungsgesetzes und in den überwiegenden Bereichen des SGB.
- **Örtlich** das SG des gewöhnlichen Aufenthaltsorts des Klägers (§ 57 Abs. 1 SGG); bei juristischen Personen Sitz (§ 57 Abs. 2 SGG).

## Klagearten

- **Anfechtungsklage** § 54 Abs. 1 Var. 1 SGG — Aufhebung eines belastenden Bescheids.
- **Verpflichtungsklage** § 54 Abs. 1 Var. 2 SGG — Erlass eines abgelehnten Leistungsbescheids.
- **Leistungsklage** § 54 Abs. 4 / § 54 Abs. 5 SGG — wenn Höhe streitig.
- **Feststellungsklage** § 55 SGG — Rechtsverhältnis.
- **Untätigkeitsklage** § 88 SGG — Behörde untätig.

## Klageaufbau

### 1. Rubrum

- Klagepartei mit Vertretung (Anwalt mit beA-Adresse).
- Beklagte Behörde mit Aktenzeichen Widerspruchsbescheid.
- Streitgegenstand kurz.

### 2. Anträge

Eindeutige vollstreckbare Anträge:

1. Aufhebung des angefochtenen Bescheids und Widerspruchsbescheids;
2. Verurteilung der Beklagten zur Gewährung der konkret bezifferten Leistung;
3. Kostenantrag § 193 SGG (Gerichtskosten- und Auslagenfreiheit in Sozialgerichtsverfahren regelmäßig);
4. ggf. Antrag auf Bewilligung von Prozesskostenhilfe und Beiordnung;
5. ggf. Antrag auf Anordnung der aufschiebenden Wirkung (§ 86b Abs. 1 SGG) oder einstweilige Anordnung (§ 86b Abs. 2 SGG) — Eilantrag dann über Skill `eilantrag-sozialrecht`.

### 3. Sachverhalt

Knapp und chronologisch — Antrag Bescheid Widerspruch Widerspruchsbescheid.

### 4. Rechtliche Würdigung

- Anspruchsgrundlage(n).
- Tatbestandsmerkmale mit Subsumtion.
- BSG-Rechtsprechung mit Pinpoint.
- Auseinandersetzung mit der Begründung des Widerspruchsbescheids.

### 5. Beweisangebote

Beweismittel im Sozialgerichtsverfahren (§ 103 SGG Untersuchungsgrundsatz):

- Urkunden (Verwaltungsakte beizuziehen § 119 SGG).
- Zeugen mit ladungsfähiger Anschrift.
- Sachverständige (häufig medizinische SV bei SGB IX SGB V).
- Augenschein.
- Parteivernehmung.

### 6. Anlagenverzeichnis

Mit Sigel K1 K2 K3. Siehe Skill `anlagen-erstellen`.

## Sonderregeln SGG

- **Kein Anwaltszwang** vor dem SG (§ 73 Abs. 4 SGG).
- **beA-Pflicht** für Rechtsanwälte (§ 65d SGG iVm § 31a BRAO).
- **Kostenfreiheit** für Versicherte Leistungsempfänger Behinderte (§ 183 SGG).
- **Untersuchungsgrundsatz** (§ 103 SGG) — Gericht ermittelt von Amts wegen.

## PKH-Antrag

Bei wirtschaftlicher Bedürftigkeit: PKH nach § 73a SGG iVm §§ 114 ff. ZPO. Verweis auf Skill `prozesskostenhilfe-antrag`.

## Ausgabe

- `klage-<sg>-<az>-<datum>.docx` und Markdown-Spiegel.
- Anlagenkonvolut nach Skill `anlagen-erstellen`.
- Fristen in Fristenbuch eingetragen — siehe Skill `fristenbuch-sozialrecht`.

## Versand

Über beA — vor Versand der Skill `versand-vor-check` aus `kanzlei-cowork`.
