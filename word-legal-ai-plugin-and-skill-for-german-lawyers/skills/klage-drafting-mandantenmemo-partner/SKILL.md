---
name: klage-drafting-mandantenmemo-partner
description: "Klage Drafting Mandantenmemo Partner: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klage Drafting Mandantenmemo Partner

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Klage Drafting Mandantenmemo Partner** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klage-drafting-253-zpo` | Drafting einer Klageschrift nach § 253 Abs. 2 ZPO. Bestimmter Antrag plus Sachverhaltsdarstellung mit Rechtsschutzbegehren und Streitgegenstand. Aufbau: Rubrum (Parteien, Vertretung, Anschriften, Gericht), Anträge (Zahlung, Feststellung, Hilfsantrag), tatsächliches Vorbringen chronologisch oder thematisch, rechtliche Würdigung, Beweisangebote, Anlagenverzeichnis. Mit § 130 ZPO Schriftsatz-Anforderungen, Streitwertberechnung nach § 3 ZPO, Bestimmtheit der Anträge nach BGH-Rechtsprechung sowie Mustertext für Zahlungsklage. |
| `mandantenmemo-und-partner-update` | Erstellt Mandantenmemos, Partner-Updates und Management Notes aus juristischer Prüfung. Liefert Executive Summary, klare Empfehlung, Risikoampel, Entscheidungsoptionen, offene Punkte, Fristen und nächste Schritte. Vermeidet Lehrbuch-Gutachten und übersetzt Rechtsfragen in handlungsfähige Kanzleisprache. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Klage Drafting Mandantenmemo Partner**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klage-drafting-253-zpo`

**Fokus:** Drafting einer Klageschrift nach § 253 Abs. 2 ZPO. Bestimmter Antrag plus Sachverhaltsdarstellung mit Rechtsschutzbegehren und Streitgegenstand. Aufbau: Rubrum (Parteien, Vertretung, Anschriften, Gericht), Anträge (Zahlung, Feststellung, Hilfsantrag), tatsächliches Vorbringen chronologisch oder thematisch, rechtliche Würdigung, Beweisangebote, Anlagenverzeichnis. Mit § 130 ZPO Schriftsatz-Anforderungen, Streitwertberechnung nach § 3 ZPO, Bestimmtheit der Anträge nach BGH-Rechtsprechung sowie Mustertext für Zahlungsklage.

# Klage-Drafting nach § 253 ZPO

## Zweck

Eine Klageschrift muss zwei Wirksamkeitsvoraussetzungen erfüllen: einen bestimmten Antrag und eine Sachverhaltsdarstellung, die Rechtsschutzbegehren und Streitgegenstand erkennen lässt. § 253 Abs. 2 ZPO ist die zentrale Norm. Wer hier zu unbestimmt schreibt, riskiert die Unzulässigkeit der Klage. Dieser Skill führt Sie durch den Aufbau, prüft die Bestimmtheit Ihres Antrags und liefert einen Mustertext für eine Zahlungsklage.

Der Skill richtet sich an Drafter, die eine erste Fassung erzeugen oder einen Entwurf prüfen. Er erklärt keine Prozessrechtsdogmatik, sondern operationalisiert die formalen Anforderungen.

## Eingaben

- Mandantenrolle (Klägerseite, Streitgenosse)
- Anspruchsgrundlage und Anspruchshöhe oder Antragsziel
- Sachverhalt in Stichpunkten oder Akten
- Zuständiges Gericht (sachlich nach §§ 23, 71 GVG; örtlich nach §§ 12 ff. ZPO)
- Gegenseite (Name, Anschrift, Vertretungsverhältnisse)
- Vorhandene Beweismittel (Urkunden, Zeugen, Sachverständige)
- Frist (Verjährung, Verfallklausel)

## Rechtlicher und methodischer Rahmen

- § 253 Abs. 2 ZPO: Bestimmter Antrag und bestimmte Angabe von Gegenstand und Grund.
- § 253 Abs. 3 ZPO: Wert des Streitgegenstands soll angegeben werden, wenn der Anspruch nicht auf eine bestimmte Geldsumme gerichtet ist.
- § 130 ZPO: Allgemeine Anforderungen an vorbereitende Schriftsätze (Parteien, Anträge, Tatsachen, Beweismittel, Urkunden, Unterschrift).
- § 3 ZPO: Streitwertfestsetzung durch das Gericht nach freiem Ermessen.
- §§ 23, 71 GVG: Sachliche Zuständigkeit AG bis 5000 Euro, sonst LG.
- §§ 12 ff. ZPO: Örtliche Zuständigkeit.
- §§ 78 ff. ZPO: Anwaltszwang vor Landgericht und höheren Instanzen.
- Methodik: Urteilsstil. Knapp, indikativ, ohne Lehrbuchprosa.

## Ablauf / Checkliste

1. **Rubrum aufbauen.** Klägerseite mit voller Bezeichnung, Anschrift, Prozessvertretung. Beklagtenseite ebenso. Gericht in der ersten Zeile. Aktenzeichen leer (vom Gericht zu vergeben).
2. **Antrag formulieren.** Zahlungsantrag mit konkreter Summe in Euro, Zinsbeginn, Zinssatz. Bei Feststellungsanträgen: konkretes Rechtsverhältnis. Hilfsanträge nur, wenn der Hauptantrag ausfallen kann.
3. **Bestimmtheit prüfen.** Wer schuldet wem was wann woraus. Vier Fragen, vier Antworten.
4. **Sachverhalt darstellen.** Chronologisch bei einfachen Sachverhalten, thematisch bei komplexen. Konnexität zwischen Vorbringen und Antrag muss erkennbar sein.
5. **Rechtliche Würdigung.** Anspruchsgrundlage nennen, Tatbestandsmerkmale unter den Sachverhalt subsumieren. Im Urteilsstil. Auf Kommentar- oder Aufsatzfundstellen aus Modellwissen verzichten.
6. **Beweisangebote einfügen.** Hinter jeder beweisbedürftigen Tatsache "Beweis: Zeuge X, geladen über Anschrift Y" oder "Anlage K1". Keine pauschalen "Beweis: alle".
7. **Anlagenverzeichnis.** K1, K2, K3 fortlaufend. Bezeichnung der Anlage.
8. **Streitwert angeben.** Bei Zahlungsklagen identisch mit Hauptforderung (Zinsen und Kosten zählen nicht; § 4 ZPO).
9. **Unterschrift.** Anwaltliche Unterschrift gemäß § 130 Nr. 6 ZPO; elektronisch über beA.

### Aufbauschema der Klageschrift

| Abschnitt | Inhalt |
|---|---|
| Rubrum | Gericht, Parteien, Vertreter, Aktenzeichen |
| Anträge | Hauptantrag, ggf. Hilfsantrag, ggf. Feststellungsantrag |
| Begründung | Sachverhalt (I), Rechtliche Würdigung (II), Beweisangebote (III) |
| Streitwert | Angabe nach § 3 ZPO |
| Anlagenverzeichnis | K1 ff. |
| Unterschrift | Anwältin, Anwalt |

## Typische Drafting-Fehler

- **Unbestimmter Antrag.** "Angemessene Entschädigung" ohne Betrag. "Auskunft zu erteilen" ohne Gegenstand der Auskunft.
- **Konnexitätslücke.** Sachverhalt erzählt eine Geschichte, aber kein Tatsachenkern stützt den Antrag.
- **Beweisflut.** Pauschale Beweisangebote wie "Beweis: Zeugnis aller Beteiligten" sind wertlos.
- **Anspruchskumulation ohne Trennung.** Mehrere Ansprüche müssen einzeln dargestellt werden; Streitgegenstandsidentität sonst unklar.
- **Falsches Gericht.** Sachliche oder örtliche Unzuständigkeit übersehen. Vor Klageerhebung prüfen.
- **Streitwert vergessen.** Kann zur Verzögerung führen.

## Ausgabeformat

- Vollständige Klageschrift im Schriftsatzformat.
- Bei nur Antragsentwurf: Antragstext mit Subsumtionsskizze.
- Stets mit Anlagenverzeichnis.

## Beispiele

### Mustertext Zahlungsklage (Auszug)

```
Landgericht Berlin Berlin, den 30. Mai 2026
Tegeler Weg 17-21
10589 Berlin

 Klage

der Frau Anna Muster, Beispielstraße 1, 12345 Beispielstadt
 - Klägerin -
Prozessbevollmächtigte: Rechtsanwältin Marta Stern,
Musterallee 4, 12345 Musterstadt

 gegen

die Firma Beklagt GmbH, vertreten durch den Geschäftsführer Hans Schmidt,
Industrieweg 5, 12345 Beispielstadt
 - Beklagte -

wegen Kaufpreisforderung

Streitwert: 25.000,00 Euro

Namens und in Vollmacht der Klägerin erheben wir Klage und werden beantragen:

Die Beklagte wird verurteilt, an die Klägerin 25.000,00 Euro nebst Zinsen
in Höhe von neun Prozentpunkten über dem Basiszinssatz seit dem 1. März 2026
zu zahlen.

 Begründung

I. Sachverhalt

Die Klägerin und die Beklagte schlossen am 15. Januar 2026 einen Kaufvertrag
über die Lieferung von zehn Industriemaschinen Typ A-100 zum Gesamtpreis
von 25.000 Euro netto.

Beweis: Kaufvertrag vom 15. Januar 2026, Anlage K1.

Die Klägerin lieferte die Maschinen vereinbarungsgemäß am 1. Februar 2026.
Die Beklagte bestätigte den Empfang ohne Beanstandungen.

Beweis: Lieferschein und Empfangsbestätigung vom 1. Februar 2026, Anlage K2.

II. Rechtliche Würdigung

Der Anspruch ergibt sich aus § 433 Abs. 2 BGB. Die Parteien haben einen
wirksamen Kaufvertrag geschlossen. Die Klägerin hat geliefert; die Beklagte
schuldet den vereinbarten Kaufpreis. Die Forderung wurde mit Ablauf der
Zahlungsfrist am 28. Februar 2026 fällig. Verzug ist mit dem 1. März 2026
eingetreten (§ 286 Abs. 2 Nr. 1 BGB).

Anlagenverzeichnis:
K1 Kaufvertrag vom 15. Januar 2026
K2 Lieferschein vom 1. Februar 2026

Marta Stern
Rechtsanwältin
```

## Querverweise

- `klageerwiderung-substantiiertes-bestreiten`
- `dokumentarchitektur-vertrag-und-schriftsatz`
- `anwaltsschreiben-aussergerichtlich` für die vorprozessuale Mahnung
- `revisions-prozess-redlines-comparison` für Schriftsatzwechsel mit dem Mandanten

## Quellen (Stand 05/2026)

- §§ 253, 130, 3, 4 ZPO; gesetze-im-internet.de.
- §§ 23, 71 GVG; §§ 78 ff. ZPO für Anwaltszwang.
- § 286 BGB für Verzugszinsen; § 288 BGB für Verzugszinssatz.
- Rechtsprechung des BGH zur Bestimmtheit von Anträgen: vom Nutzer zu verifizieren. Keine Aktenzeichen aus Modellwissen.
- `references/zitierweise.md` für Belegpflicht.

## 2. `mandantenmemo-und-partner-update`

**Fokus:** Erstellt Mandantenmemos, Partner-Updates und Management Notes aus juristischer Prüfung. Liefert Executive Summary, klare Empfehlung, Risikoampel, Entscheidungsoptionen, offene Punkte, Fristen und nächste Schritte. Vermeidet Lehrbuch-Gutachten und übersetzt Rechtsfragen in handlungsfähige Kanzleisprache.

# Mandantenmemo und Partner-Update

## Zweck

Ein Memo ist kein Aktenfriedhof. Es muss einer Person mit Zeitdruck eine Entscheidung ermöglichen. Dieser Skill baut aus Prüfung, Akte oder Entwurf ein lesbares Memo für Mandant, Partnerin oder Management.

## Formate

| Format | Länge | Wann |
|---|---:|---|
| Partner-Update | fünf bis zehn Bullet Points | interne Steuerung, schnell |
| Mandantenmemo kurz | eine bis drei Seiten | Entscheidungsvorlage |
| Management Note | eine Seite plus Anlagen | Vorstand, Geschäftsführung, Inhouse |
| Legal Memo tief | fünf bis 15 Seiten | komplexe Rechtsfrage |

## Standardaufbau

1. **Executive Summary:** Ergebnis in drei Sätzen.
2. **Empfehlung:** Was soll der Mandant jetzt tun?
3. **Sachstand:** Nur entscheidungserhebliche Fakten.
4. **Rechtslage:** knapp, belegt, ohne Blindzitate.
5. **Risikoampel:** grün, gelb, rot mit Grund.
6. **Optionen:** mindestens zwei, wenn realistisch.
7. **Nächste Schritte:** Owner, Deadline, Dokumente.

## Sprachregeln

- Ergebnis zuerst.
- Normen nur nennen, wenn sie helfen.
- Keine langen Fußnotenketten.
- Bei unsicherer Rechtslage: Unsicherheit benennen, nicht verstecken.
- Für Nichtjuristen: "Das bedeutet praktisch ..." ergänzen.

## Output

- Gewähltes Memo-Format.
- Vollständiger Memo-Entwurf.
- Optional: Partner-E-Mail zur Weiterleitung.
- Offene Punkte als Checkliste.

## Querverweise

- `gutachten-memo-internes-drafting`
- `deutscher-kanzleistil-kalibrieren`
- `finaler-writing-quality-gate`


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
