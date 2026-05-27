---
name: klage-sozialgericht
description: "Nach negativem Widerspruchsbescheid muss Klage zum Sozialgericht erhoben werden. §§ 87 ff. SGG Klagefrist. Pruefraster: Klagefrist 1 Monat nach Widerspruchsbescheid § 87 Abs. 1 SGG kein Anwaltszwang vor SG beA-Versandpflicht sachliche Zustaendigkeit § 8 SGG oertliche Zustaendigkeit § 57 SGG PKH-Antrag § 73a SGG. Output: Klageschrift SG mit Anlagenverzeichnis Beweisangeboten und PKH-Antrag. Abgrenzung zu eilantrag-sozialrecht (Eilrechtsschutz) und fachanwalt-sozialrecht-widerspruch-sozialleistung (Widerspruchsstufe)."
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

Über beA — vor Versand der Skill `versand-vor-check` aus `kanzlei-allgemein`.

## Triage — kläre vor Klageerhebung

1. Vorverfahren abgeschlossen? — Widerspruchsbescheid oder Untätigkeit über sechs Monate (§ 88 SGG)?
2. Klagefrist (ein Monat § 87 SGG) gewahrt? — Datum Zustellung Widerspruchsbescheid + Vier-Tages-Fiktion berechnen
3. PKH erforderlich? — Prüfung Skill `pkh-erfolgsaussicht-pruefen`, Antrag zeitgleich einreichen
4. Eilantrag § 86b SGG parallel nötig? — bei Existenzbedrohung oder dringendem Hilfsmittelbedarf
5. Sachlich und örtlich zuständiges Sozialgericht ermittelt? (§§ 8, 57 SGG)

## Aktuelle Rechtsprechung

- BSG, Urt. v. 12.09.2018 - B 4 AS 39/17 R, SozR 4-4200 § 22 Nr. 97 Rn. 14 — Das Sozialgericht ist nach § 103 SGG verpflichtet, den Sachverhalt von Amts wegen zu ermitteln; die Beteiligten sind zur Mitwirkung verpflichtet, ein Beweisantrag muss aber konkrete Tatsachen bezeichnen, die das Gericht klären soll.
- BSG, Urt. v. 14.02.2018 - B 14 AS 17/17 R, SozR 4-1500 § 87 Nr. 3 Rn. 18 — Die Klagefrist des § 87 SGG beginnt mit der Bekanntgabe des Widerspruchsbescheids; bei fehlerhafter Rechtsbehelfsbelehrung gilt die Jahresfrist des § 66 Abs. 2 SGG auch für den Widerspruchsbescheid.
- BSG, Urt. v. 27.09.2011 - B 4 AS 155/10 R, SozR 4-4200 § 7 Nr. 25 Rn. 21 — Im Sozialgerichtsprozess trägt grundsätzlich der Kläger die objektive Beweislast für anspruchsbegründende Tatsachen; bei Amtsermittlung (§ 103 SGG) werden Beweisanträge jedoch nicht mit strikter Beweislast verknüpft.
- BSG, Urt. v. 29.03.2022 - B 4 AS 8/21 R, SozR 4-1500 § 193 Nr. 8 Rn. 11 — Kostenentscheidungen nach § 193 SGG stehen im billigen Ermessen des Gerichts; bei Obsiegen im Wesentlichen ist dem Kläger Kostenerstattung zuzusprechen, auch wenn einzelne Anträge abgewiesen wurden.

## Kommentarliteratur

- Krasney/Udsching, Handbuch des Sozialgerichtsprozesses, Kap. III Rn. 1 ff. (Klageerhebung, Klagearten)
- Meyer-Ladewig/Keller/Leitherer/Schmidt, SGG, § 54 Rn. 1 ff. (Klagarten) und § 103 Rn. 1 ff. (Amtsermittlung)
