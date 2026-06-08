---
name: dpma-interessen-einstweilige-euipo
description: "Dpma Interessen Einstweilige Euipo im Plugin Fachanwalt Gewerblicher Rechtsschutz: prüft konkret DPMA-Mehrparteienverfahren, Mandantenkommunikation im Eilverfahren, EUIPO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Dpma Interessen Einstweilige Euipo

## Arbeitsbereich

**Dpma Interessen Einstweilige Euipo** ordnet den Fall über die tragenden Prüfungslinien: DPMA-Mehrparteienverfahren, Mandantenkommunikation im Eilverfahren, EUIPO. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `spezial-dpma-mehrparteien-konflikt-und-interessen` | DPMA-Mehrparteienverfahren: Widerspruchsverfahren MarkenG §§ 41–43, Verfalls- und Nichtigkeitsverfahren, Beschwerde zum BPatG, Beteiligtenrechte, Kollidierende Interessen mehrerer Schutzrechtsinhaber, Prioritätskonflikte, Verfahrensstrategie. |
| `spezial-einstweilige-mandantenkommunikation-entscheidungsvorlage` | Mandantenkommunikation im Eilverfahren: Entscheidungsvorlage für einstweilige Verfügung, Risiko-Chancen-Abwägung, Kostenaufklärung § 49b BRAO, Mandantenbrief EV-Antrag oder Reaktion auf EV, Informationspflichten und Dokumentation. |
| `spezial-euipo-internationaler-bezug-und-schnittstellen` | EUIPO: Internationale Schnittstellen und Verfahren. Unionsmarke UMV, GGM-Verfahren, EUIPO-Beschwerdekammer, EuGH-Vorabentscheidungen, IR-Marke Madrider System, TM5/IP5, WIPO-Schnittstellen, nationale Designierung über Hague-System. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `spezial-dpma-mehrparteien-konflikt-und-interessen`

**Fokus:** DPMA-Mehrparteienverfahren: Widerspruchsverfahren MarkenG §§ 41–43, Verfalls- und Nichtigkeitsverfahren, Beschwerde zum BPatG, Beteiligtenrechte, Kollidierende Interessen mehrerer Schutzrechtsinhaber, Prioritätskonflikte, Verfahrensstrategie.

### DPMA-Mehrparteienverfahren: Konflikte und Interessen

## Aufgabe
Dieser Skill behandelt DPMA-Verfahren mit mehreren Beteiligten: Widerspruchsverfahren, Löschungsverfahren, Beschwerde beim BPatG und Strategiefragen bei kollidierenden Schutzrechten.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 41 MarkenG | Widerspruch gegen Markeneintragung |
| § 42 MarkenG | Widerspruchsfrist: 3 Monate ab Bekanntmachung |
| § 43 MarkenG | DPMA-Prüfung des Widerspruchs; Nichtbenutzungseinrede |
| § 49 MarkenG | Verfall der Marke (Nichtbenutzung, Freizeichen, Irreführung) |
| § 50 MarkenG | Nichtigkeit wegen absoluter Schutzhindernisse |
| § 51 MarkenG | Nichtigkeit wegen relativer Schutzhindernisse (ältere Rechte) |
| § 66 MarkenG | Beschwerde zum BPatG gegen DPMA-Entscheidungen |
| § 81 PatG | Beschränkungs- und Nichtigkeitsverfahren Patent |
| §§ 33, 36 DesignG | Nichtigkeitsverfahren Design beim DPMA |

## Widerspruchsverfahren Marke

### Ablauf

```
Markeneintragung wird im Markenblatt bekannt gemacht
 ↓
Widerspruchsfrist: 3 Monate ab Bekanntmachung (§ 42 Abs. 1 MarkenG)
 ↓
Widerspruch einlegen (§ 41 MarkenG):
 - Schriftlich beim DPMA; Gebühr 250 €
 - Älteres Recht bezeichnen (Marke, Unternehmenskennzeichen, etc.)
 ↓
DPMA gibt Widerspruch dem Markeninhaber bekannt
 ↓
Nichtbenutzungseinrede möglich (§ 43 Abs. 1 MarkenG) nach Fristablauf
 ↓
Verhandlung / Entscheidung durch DPMA
 ↓
Beschwerde beim BPatG (§ 66 MarkenG) → Rechtsbeschwerde BGH
```

### Nichtbenutzungseinrede (§ 43 Abs. 1 MarkenG)
- Ältere Widerspruchsmarke muss **5 Jahre** vor dem maßgeblichen Zeitpunkt ernsthaft benutzt worden sein.
- Beweislast: Widersprechender muss Benutzung glaubhaft machen (Umsatzzahlen, Kataloge, Rechnungen).
- Einrede greift nur, wenn Marke überhaupt 5 Jahre eingetragen war.

### Mehrere Widersprüche gegen eine Marke

| Situation | Strategie |
|---|---|
| Mehrere ältere Marken des gleichen Inhabers | Widersprüche bündeln; Synergien nutzen |
| Widersprüche verschiedener Inhaber | DPMA koordiniert; Abstimmung sinnvoll |
| Gegeneinander widersprechende ältere Rechte | Prioritätsprinzip; ältestes Recht entscheidet |

## Löschungsverfahren (Verfall und Nichtigkeit)

### Verfallsverfahren § 49 MarkenG

| Verfallsgrund | Norm | Antragsteller |
|---|---|---|
| Nichtbenutzung 5 Jahre | § 49 Abs. 1 MarkenG | Jedermann |
| Marke zur Gattungsbezeichnung geworden | § 49 Abs. 2 Nr. 1 | Jedermann |
| Täuschungsgeeignetheit | § 49 Abs. 2 Nr. 2 | Jedermann |
| Gebühr: 100 € (DPMA) | | |

### Nichtigkeitsverfahren §§ 50–51 MarkenG

| Nichtigkeitsgrund | Norm |
|---|---|
| Absolute Schutzhindernisse § 8 MarkenG | § 50 Abs. 1 MarkenG |
| Bösgläubige Anmeldung | § 10 MarkenG (ältere Markenpolitik) |
| Älteres Recht des Antragstellers | § 51 Abs. 1 MarkenG |

## Mehrparteienkonflikte: Strategiefragen

### Prioritätskonflikt
- Älteres Recht schlägt jüngeres (§ 6 MarkenG, § 9 MarkenG).
- Parallele Koexistenzvereinbarung möglich: schriftliche Abgrenzungsvereinbarung.

### Abgrenzungsvereinbarung
- Regelt, welche Waren/Dienstleistungen jede Partei nutzen darf.
- Wettbewerbsrechtliche Zulässigkeit prüfen (GWB, Art. 101 AEUV bei spürbarer Marktbeschränkung).
- Schriftlich; mit klaren Geltungsbereichen (Branchen, Territorien).

### Gerichtsschutz zusätzlich zu DPMA-Verfahren
- Parallelklage vor LG möglich (§ 55 MarkenG: Unterlassung; § 51 Abs. 4 MarkenG: Nichtigkeit).
- Abstimmung DPMA-Verfahren und Zivilprozess (Aussetzung, §§ 148, 246 ZPO analog).

## Checkliste Mehrparteienverfahren

| Schritt | Erledigt? |
|---|---|
| Älteres Recht identifiziert und Registerauszug vorhanden | ☐ |
| Widerspruchsfrist berechnet und eingetragen | ☐ |
| Nichtbenutzungsrisiko der eigenen älteren Marke bewertet | ☐ |
| Benutzungsnachweise gesichert und geordnet | ☐ |
| Mehrere Widersprüche abgestimmt | ☐ |
| Abgrenzungsvereinbarung geprüft (Möglichkeit, Risiken) | ☐ |
| Beschwerdestrategie bei DPMA-Niederlage vorbereitet | ☐ |

## Einstieg
1. Welches Verfahren ist konkret anstehend (Widerspruch, Löschung, Nichtigkeit)?
2. Welche älteren Rechte stehen zur Verfügung?
3. Gibt es mehrere Widersprecher oder kollidierenden Interessen?
4. Sind Fristen bekannt (Widerspruchsfrist, Beschwerdegrenze)?
5. Output: Verfahrensstrategie-Memo, Checkliste, Abgrenzungsvereinbarungs-Entwurf?

## Anschluss-Skills
- `spezial-euipo-internationaler-bezug-und-schnittstellen` – EUIPO-Widerspruch.
- `spezial-markeng-risikoampel-und-gegenargumente` – Risikoampel Markenrecht.
- `fachanwalt-gewerblicher-rechtsschutz-marken-widerspruch` – Vollständiger Widerspruchsworkflow.

## Quellenregel
- MarkenG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de/markeng/); DPMA: [dpma.de](https://www.dpma.de).
- BPatG: [bundespatentgericht.de](https://www.bundespatentgericht.de); BGH: [bgh.de](https://www.bundesgerichtshof.de).
- Rechtsprechung: [dejure.org](https://dejure.org), [openjur.de](https://openjur.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine vollständige Beurteilung ohne Kenntnis der konkreten Marken und Registerauszüge.
- Kein Ersatz für vollständige Mandantenberatung.

## 2. `spezial-einstweilige-mandantenkommunikation-entscheidungsvorlage`

**Fokus:** Mandantenkommunikation im Eilverfahren: Entscheidungsvorlage für einstweilige Verfügung, Risiko-Chancen-Abwägung, Kostenaufklärung § 49b BRAO, Mandantenbrief EV-Antrag oder Reaktion auf EV, Informationspflichten und Dokumentation.

### Mandantenkommunikation: Entscheidungsvorlage Eilverfügung

## Aufgabe
Dieser Skill unterstützt die Mandantenkommunikation in Eilsituationen: strukturierte Entscheidungsvorlage für oder gegen eine einstweilige Verfügung, Kostenaufklärung und mandantengerechte Darstellung der Optionen.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 49b BRAO | Vergütungsvereinbarung und Kostentransparenz |
| § 11 BORA | Informations- und Aufklärungspflichten des Anwalts |
| § 935 ZPO | Einstweilige Verfügung: Verfügungsanspruch + Verfügungsgrund |
| § 945 ZPO | Schadensersatzpflicht bei ungerechtfertigter EV |
| § 12 Abs. 1 UWG | Dringlichkeitsvermutung UWG |

## Entscheidungsvorlage: Für oder gegen EV-Antrag

### Struktur

**1. Ausgangslage (max. 5 Sätze)**
- Was ist passiert (Verletzungshandlung, Schutzrecht)?
- Wer ist betroffen (Mandant als Angreifer oder Verteidiger)?
- Welche Frist läuft (Dringlichkeit)?

**2. Optionen mit Kosten und Risiken**

| Option | Beschreibung | Vorteile | Nachteile / Risiken | Kosten (ca.) |
|---|---|---|---|---|
| EV-Antrag | Sofortiger gerichtlicher Schutz; Unterlassungsgebot | Schnell (1–3 Tage); keine Anhörung | Kosten; § 945 ZPO-Risiko | Streitwert-abhängig |
| Abmahnung zuerst | Gegenseite zur Unterlassung auffordern | Günstiger; Kostenerstattung möglich | Dringlichkeit: Frist genau setzen | RVG 1,3 Geschäftsgebühr |
| Keine Reaktion | Beobachten | Kostensparend | Verletzung setzt sich fort | 0 |
| Negative Feststellungsklage (Abgemahnte) | Gerichtsstand sichern | Eigene Zuständigkeit | Kosten; Risiko bei Verlust | Streitwert-abhängig |

**3. Empfehlung des Anwalts**
- Begründete Empfehlung mit Hinweis auf entscheidende Punkte (Dringlichkeit, Beweislage, Gegenseite).

**4. Kostenaufklärung (§ 49b BRAO)**
- Konkrete Kostenschätzung:
 - Anwaltsgebühren (Streitwert × Gebührenfaktor).
 - Gerichtsgebühren GKG.
 - Ggf. Sicherheitsleistung.
- Kostenrisiko bei Unterliegen (gegnerische Anwaltskosten).

**5. Freigabe / Zustimmung Mandant**
- Klare Frage an den Mandanten: Freigabe für EV-Antrag erteilen?
- Protokollierung der Entscheidung (Memo an Akte).

## Muster-Mandantenbrief: EV-Antrag (kurz)

```
[Briefkopf Kanzlei] [Ort, Datum]

An [Mandant Name] - vertraulich -

Beratungsschreiben: Einstweilige Verfügung [Ihr Sachverhalt]

Sehr geehrte/r [Mandant],

1. Sachverhalt
[Kurze Zusammenfassung: Verstoß, wann bekannt, wann eingestellt]

2. Unsere Empfehlung
Wir empfehlen, unverzüglich eine einstweilige Verfügung zu beantragen.

Begründung: [2–3 Sätze zur Dringlichkeit, Beweislage, Schutzrecht]

3. Kosten und Risiken
Unsere Gebühren: ca. [Betrag] €
Gerichtsgebühren: ca. [Betrag] €
Kostenrisiko bei Aufhebung der EV (§ 945 ZPO): [Einschätzung]

4. Ihr nächster Schritt
Bitte geben Sie uns bis [Datum, Uhrzeit] Ihre Freigabe.
Ohne Freigabe können wir die Frist nicht wahren.

Mit freundlichen Grüßen
[Kanzlei]
```

## Muster-Mandantenbrief: Reaktion auf EV (kurz)

```
Sehr geehrte/r [Mandant],

gegen Sie wurde eine einstweilige Verfügung erlassen / angedroht.

1. Lage
[EV-Beschluss erhalten am X; Inhalt: Unterlassung von Y]

2. Ihre Optionen
A) Unterlassungserklärung abgeben → Verfahren erledigt; Marke des Angriffs anerkennen
B) Widerspruch einlegen → Mündliche Verhandlung; teurer, aber Gegenargumente möglich
C) Abschlussschreiben abwarten → Zuwarten bis Gegner Abschluss fordert

3. Empfehlung
Wir empfehlen [Option] weil [Begründung].

4. Kosten
[Kosten je Option]

5. Frist für Ihre Entscheidung: [Datum]
[Kanzlei]
```

## Dokumentationspflichten

| Schritt | Dokumentation |
|---|---|
| Beratungsgespräch | Beratungsprotokoll / E-Mail-Bestätigung |
| Mandantenfreigabe | E-Mail-Bestätigung oder schriftliche Vollmacht |
| Kostenaufklärung | Aktennotiz mit Datum, Betrag, Mandantenkenntnis |
| Entscheidung gegen EV | Aktennotiz mit Mandantenwunsch |

## Einstieg
1. Ist der Mandant Angreifer (EV beantragen) oder Verteidiger (auf EV reagieren)?
2. Wie viel Zeit bleibt bis zum Fristablauf?
3. Soll eine Entscheidungsvorlage oder ein Mandantenbrief erstellt werden?
4. Welcher Streitwert ist realistisch (Kostenabschätzung)?
5. Output: Entscheidungsvorlage, Mandantenbrief, Kostenübersicht, Freigabe-Checkliste?

## Anschluss-Skills
- `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung` – Vollziehung nach Freigabe.
- `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` – Qualitätsgate.
- `spezial-bezuege-zahlen-schwellen-und-berechnung` – Kostenberechnung.

## Quellenregel
- BRAO, BORA: [gesetze-im-internet.de](https://www.gesetze-im-internet.de); ZPO: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- RVG, GKG: [gesetze-im-internet.de/rvg](https://www.gesetze-im-internet.de/rvg/), [gesetze-im-internet.de/gkg](https://www.gesetze-im-internet.de/gkg/).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine verbindliche Kostenberechnung ohne vollständige Daten.
- Kein Ersatz für vollständige Mandantenberatung und individuelle Aufklärung.

## 3. `spezial-euipo-internationaler-bezug-und-schnittstellen`

**Fokus:** EUIPO: Internationale Schnittstellen und Verfahren. Unionsmarke UMV, GGM-Verfahren, EUIPO-Beschwerdekammer, EuGH-Vorabentscheidungen, IR-Marke Madrider System, TM5/IP5, WIPO-Schnittstellen, nationale Designierung über Hague-System.

### EUIPO: Internationale Bezüge und Schnittstellen

## Aufgabe
Dieser Skill behandelt EUIPO-Verfahren mit internationalem Bezug: Unionsmarken, GGM, IR-Marken, Beschwerdekammer, EuGH-Vorabentscheidungen und Schnittstellen zu WIPO.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| UMV (VO 2017/1001) | Unionsmarkenverordnung: Anmeldung, Verletzung, Widerspruch, Nichtigkeit |
| GGV (VO 6/2002) | Gemeinschaftsgeschmacksmuster-Verordnung |
| Art. 165 ff. UMV | Schnittstelle IR-Marke (Madrider Protokoll) |
| Madrider Protokoll (PMMA) | Internationale Markenanmeldung über WIPO |
| Haager System (HMA) | Internationale Designanmeldung über WIPO |
| Art. 267 AEUV | EuGH-Vorabentscheidungsverfahren |
| RL 2015/2436 | Markenrechts-Richtlinie (Angleichung nationale Markenrechte) |

## EUIPO-Verfahrensübersicht

### Anmeldeverfahren Unionsmarke

```
Online-Einreichung bei EUIPO (euipo.europa.eu)
 ↓
Formelle Prüfung (Klassen, Abbildung, Beschreibung)
 ↓
Absolute Schutzhindernisse prüfen (Art. 7 UMV)
 ↓
Bekanntmachung im EUIPO-Amtsblatt
 ↓
Widerspruchsfrist: 3 Monate ab Bekanntmachung
 ↓
Eintragung oder Widerspruchsverfahren
 ↓
Gültig in allen 27 EU-Mitgliedstaaten
```

### Widerspruchsverfahren EUIPO

| Aspekt | Inhalt |
|---|---|
| Grundlage | Art. 46 UMV |
| Frist | 3 Monate ab Bekanntmachung |
| Gebühr | 320 € |
| Ältere Rechte | Unionsmarke, nationale Marke, bekannte Marke, Unternehmenskennzeichen |
| Beweispflicht | Inhaberschaft + Schutzrechtsnachweis |
| Nichtbenutzungseinrede | Wenn ältere Marke > 5 Jahre: Benutzungsnachweis durch Widersprechenden |

### Nichtigkeits- und Verfallsverfahren EUIPO

| Verfahren | Norm | Kosten |
|---|---|---|
| Nichtigkeit (absolute Gründe) | Art. 59 UMV | 1.000 € |
| Nichtigkeit (relative Gründe) | Art. 60 UMV | 1.000 € |
| Verfall | Art. 58 UMV | 1.000 € |
| GGM-Nichtigkeit | Art. 52 GGV | 350 € |

## Beschwerdekammer EUIPO

- Beschwerde gegen Entscheidungen der Prüfungsabteilung oder Widerspruchsabteilung: Frist 2 Monate.
- Gebühr: 720 € (Marken).
- Entscheidungen der BK: Beschwerde zum **EuG** (Gericht der EU), dann EuGH.
- Rechtsprechung der Beschwerdekammern: [euipo.europa.eu/tunnel-web/secure/webdav/guest/document_library/contentPdfs/about_euipo/who_we_are/consolidated_decisions_en.pdf](https://euipo.europa.eu/ohimportal/en/decisions)

## IR-Marke: Schnittstelle WIPO / EUIPO

### Zentralanmeldung über WIPO
1. Basismarke in Heimatland (z.B. DPMA-Marke) als Ausgangspunkt.
2. IR-Antrag beim DPMA als Übermittlungsbehörde (§§ 119 ff. MarkenG).
3. WIPO registriert IR-Marke und notifiziert gewählte Länder.
4. Länder haben 12–18 Monate Zeit zur Zurückweisung (provisorische Ablehnung).
5. Wenn kein Widerspruch: Schutz entsteht im jeweiligen Land.

### Designierung EU über IR-Marke
- EU kann als Designierungsland benannt werden.
- EUIPO prüft wie bei direkter UM-Anmeldung.
- Vorteil: Eine IR-Marke deckt DE + EU + weitere Länder ab.

## Haager System: Internationale Designanmeldung

| Aspekt | Inhalt |
|---|---|
| Grundlage | Haager Abkommen + WIPO |
| Verwaltung | WIPO (ipportal.wipo.int) |
| Designierbarkeit EU | Ja; EUIPO prüft GGV-Anforderungen |
| Gebühren | WIPO-Grundgebühr + Designierungsgebühr je Land/Region |
| Schutzfrist | Je nach Land; EU: 5 Jahre verlängerbar bis 25 Jahre |

## EuGH-Leitentscheidungen (ausgewählte Themen)

| Thema | Aussage | Quelle |
|---|---|---|
| Verwechslungsgefahr | Gesamtabwägung; Ähnlichkeit Zeichen + Waren; Wechselwirkungsgrundsatz | EuGH, Rs. C-39/97 – Canon |
| Bekannte Marke | Schutz auch ohne Verwechslungsgefahr bei Rufausbeutung / Schädigung | EuGH, Rs. C-292/00 – Davidoff |
| Erschöpfung | Erstmaliges IVB im EWR; kein Verbot bei Reimport aus EWR | EuGH, Rs. C-355/96 – Silhouette |

*Alle Entscheidungen live prüfen: [curia.europa.eu](https://curia.europa.eu)*

## Einstieg
1. Welches Schutzrecht ist betroffen (Unionsmarke / GGM / IR-Marke)?
2. In welchem Verfahrensstadium steht die Sache (Anmeldung / Widerspruch / Nichtigkeit / Beschwerde)?
3. Gibt es eine internationale Komponente (IR-Marke, Hague System)?
4. Welche Fristen laufen (Widerspruchsfrist, Beschwerdegrenze)?
5. Output: Verfahrensübersicht, Strategie-Memo, Beschwerdeschreiben-Gerüst?

## Anschluss-Skills
- `spezial-dpma-mehrparteien-konflikt-und-interessen` – DPMA-Widerspruchsverfahren.
- `gr-uebersetzung-marke-osterreich-schweiz-spezial` – DACH-Schnittstellen.
- `faevvollzug-neu-007-grenzueberschreitende-ip-eilverfuegung` – Grenzüberschreitende EV.

## Quellenregel
- UMV, GGV: [eur-lex.europa.eu](https://eur-lex.europa.eu).
- EUIPO: [euipo.europa.eu](https://euipo.europa.eu).
- WIPO: [wipo.int](https://www.wipo.int).
- EuGH: [curia.europa.eu](https://curia.europa.eu).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine länderspezifische IP-Beratung für Nicht-EU-Länder ohne Quellenverifizierung.
- Kein Ersatz für vollständige Mandantenberatung.
