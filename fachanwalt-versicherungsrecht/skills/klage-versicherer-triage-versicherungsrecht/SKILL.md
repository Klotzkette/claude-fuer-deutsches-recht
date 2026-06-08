---
name: klage-versicherer-triage-versicherungsrecht
description: "Klage Versicherer Triage Versicherungsrecht im Plugin Fachanwalt Versicherungsrecht: prüft konkret Klagestrategie gegen Versicherer nach erfolgloser, Strukturierte Eingangs-Abfrage für versicherungsrechtliche, Substantiierter Schriftsatzkern für Deckungsklage, Klage BU/UB. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Klage Versicherer Triage Versicherungsrecht

## Arbeitsbereich

**Klage Versicherer Triage Versicherungsrecht** ordnet den Fall über die tragenden Prüfungslinien: Klagestrategie gegen Versicherer nach erfolgloser, Strukturierte Eingangs-Abfrage für versicherungsrechtliche, Substantiierter Schriftsatzkern für Deckungsklage. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `klage-versicherer-strategie` | Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz. Anwendungsfall alle außergerichtlichen Einigungsversuche sind gescheitert und Klage muss strategisch vorbereitet werden. Normen § 14 VVG Fälligkeit Verzug § 215 VVG örtliche Zuständigkeit § 204 BGB Hemmung § 256 ZPO Feststellungsantrag GVG Streitwert. Prüfraster Streitwert Zuständigkeit Klageantrag Substantiierung Beweisangebote Sachverständiger Zeugen Urkundenbeweis Mahnverfahren Zinsen Anwaltskosten. Output Klage-Strategie-Memo mit Antragsformulierung Beweiskonzept Kostenrisikobewertung. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und schriftsatzkern-substantiierung. |
| `mandat-triage-versicherungsrecht` | Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues Versicherungsmandat geht ein und muss schnell triagiert werden. Normen § 195 BGB Verjährung drei Jahre §§ 12 14 VVG Fälligkeit Schadensmeldung AVB-Klagefristen. Prüfraster Sparte Ereignis Stichtag Deckungsablehnung Hoehe Frist-Sofort-Check Eskalation bei BU-Ablehnung oder lebensbedrohlichen Krankheitskosten. Output Triage-Ergebnis mit Routing zu deckungsanfrage-prüfen und Fristen-Eskalationshinweis. Abgrenzung zu deckungsanfrage-prüfen und erstgespraech-mandatsannahme. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `klage-versicherer-strategie`

**Fokus:** Klagestrategie gegen Versicherer nach erfolgloser außergerichtlicher Korrespondenz. Anwendungsfall alle außergerichtlichen Einigungsversuche sind gescheitert und Klage muss strategisch vorbereitet werden. Normen § 14 VVG Fälligkeit Verzug § 215 VVG örtliche Zuständigkeit § 204 BGB Hemmung § 256 ZPO Feststellungsantrag GVG Streitwert. Prüfraster Streitwert Zuständigkeit Klageantrag Substantiierung Beweisangebote Sachverständiger Zeugen Urkundenbeweis Mahnverfahren Zinsen Anwaltskosten. Output Klage-Strategie-Memo mit Antragsformulierung Beweiskonzept Kostenrisikobewertung. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und schriftsatzkern-substantiierung.

# Klage gegen Versicherer — Strategie

## Zweck

Nach erfolgloser außergerichtlicher Phase die Klage strukturieren — bezifferter Hauptantrag plus Hilfsanträge plus Beweisangebote. Dieser Skill deckt alle Spartenspezifika ab (Sachversicherung, BU, Lebensversicherung, Haftpflicht, Cyber) und führt durch die prozessualen Besonderheiten des Versicherungsprozesses.

## Kaltstart-Rückfragen

1. Wurde das vollständige außergerichtliche Verfahren durchlaufen — Schadensanzeige, Stellungnahme, endgültige Ablehnung?
2. Welche Sparte — Sachversicherung (Hausrat/Gebäude), BU, Leben, Haftpflicht, Rechtsschutz, Cyber, D&O?
3. Ist die Hauptforderung bezifferbar (Leistungsklage) oder handelt es sich um künftige Rentenleistungen (Feststellungsklage § 256 ZPO)?
4. Streitwert: unter EUR 10000 (AG) oder darüber (LG)? Bei BU-Rente: 3,5-facher Jahreswert § 9 ZPO.
5. Besteht Rechtsschutzversicherung oder ist PKH (§ 114 ZPO) zu beantragen?
6. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
7. Wurde die Ombudsstelle eingeschaltet — Hemmungswirkung § 204 BGB dokumentiert?
8. Droht Verjährung (3 Jahre §§ 195, 199 BGB)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 1 VVG** — Versicherungspflicht; Grundlage der Leistungsklage.
- **§ 14 VVG** — Fälligkeit nach Abschluss nötiger Erhebungen; Abschlagszahlung § 14 Abs. 2 VVG.
- **§ 28 VVG** — Obliegenheitsverletzung; Leistungsfreiheit bei Vorsatz; quotal bei grober Fahrlässigkeit; Kausalität § 28 Abs. 3 VVG.
- **§ 81 VVG** — Herbeiführung Versicherungsfall grob fahrlässig; quotale Kürzung.
- **§ 215 VVG** — Gerichtsstand Wohnsitz des VN; Verbraucherschutz; alternativ allgemeiner Gerichtsstand Versicherer § 17 ZPO.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 9 ZPO** — Streitwert bei wiederkehrenden Leistungen: 3,5-facher Jahreswert (deckelnder Wert bei kürzerer Restlaufzeit).
- **§§ 280, 286, 288 BGB** — Verzug; Zinsen 5 Prozentpunkte über Basiszinssatz; Ersatz Verzugsschadens (Anwaltskosten).
- **§§ 195, 199, 203, 204 BGB** — Verjährung 3 Jahre; Hemmung durch Verhandlungen, Ombudsstelle.
- **§ 114 ZPO** — Prozesskostenhilfe bei wirtschaftlicher Bedürftigkeit und hinreichenden Erfolgsaussichten.
- **§§ 305–310 BGB** — AGB-Kontrolle; § 305c Abs. 2 BGB Unklarheitenregel gegen Versicherer.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Klageart: Leistungsklage oder Feststellungsklage? | §§ 253, 256 ZPO | BU-Dauerleistung → Feststellungsantrag |
| 2 | Sachliche Zuständigkeit (Streitwert)? | §§ 23, 71 GVG; § 9 ZPO | AG bis EUR 10000; LG ab EUR 10000 |
| 3 | Örtliche Zuständigkeit? | § 215 VVG | Wohnsitz VN (Verbraucherschutz) |
| 4 | Verjährung noch nicht abgelaufen? | §§ 195, 199, 203, 204 BGB | Hemmung durch Ombudsstelle dokumentieren |
| 5 | Vollständige außergerichtliche Phase? | § 14 VVG | Pflicht zur Abmahnung vor Klage bei noch laufender Prüfung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 7 | Beweisführung Versicherungsfall? | Urkundenbeweis, SV, Zeugen | Alle Beweismittel benennen |
| 8 | Obliegenheitsverletzung des VN? | § 28 VVG | Kausalitätsdefense § 28 Abs. 3 VVG |
| 9 | Grob fahrlässige Herbeiführung? | § 81 VVG | Quotale Kürzung; Verschuldensgrad |
| 10 | Risikoausschluss-Klausel wirksam? | §§ 305c, 307 BGB | Unwirksam wenn intransparent |
| 11 | Verzug und Zinsen berechnet? | §§ 280, 286, 288 BGB | Ab Fälligkeit § 14 VVG oder Mahnung |
| 12 | Anwaltskosten außergerichtlich einklagbar? | § 249 BGB | Ab Verzugseinritt erstattungsfähig |
| 13 | Sachverständige bestellt / vorgesehen? | § 411 ZPO; § 379 ZPO | Bei BU: medizinischer SV; bei Sachschaden: technischer SV |
| 14 | PKH-Antrag oder Rechtsschutz-Deckung? | § 114 ZPO | Deckungszusage RS-Versicherung vorab |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Klage gegen Versicherer strategisch planen | Klagestrategie nach Pruefschema; Template unten |
| Variante A — Aussichten gut aber Vergleich schneller | Vergleichsverhandlung vor Klageerhebung einleiten |
| Variante B — Beweislage unsicher Sachverstaendiger noetig | Selbstaendiges Beweisverfahren zuerst; Klage nach Gutachten |
| Variante C — Mehrere Versicherer beteiligt Abstimmung noetig | Federführungs-Versicherer bestimmen; Klagen koordiniert stellen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Klageschrift Sachversicherung (Leistungsklage)

```
An das [Amtsgericht / Landgericht] [Ort]

KLAGESCHRIFT

[Vorname Nachname], [Adresse]
 — Kläger —
Prozessbevollmächtigte: Rechtsanwältinnen/Rechtsanwälte [Kanzlei]

gegen

[Versicherungs-AG], vertreten durch den Vorstand
 — Beklagte —

wegen Versicherungsleistung (Hausrat/Gebäude/[Sparte])
Streitwert: EUR ____

I. ANTRÄGE

1. Die Beklagte wird verurteilt, an den Kläger EUR [Hauptforderung]
 nebst Zinsen in Höhe von 5 Prozentpunkten über dem Basiszinssatz
 seit [Datum Verzugseinritt] zu zahlen.

2. Die Beklagte wird verurteilt, an den Kläger vorgerichtliche
 Anwaltskosten in Höhe von EUR [Betrag] (1,3 Geschäftsgebühr
 Nr. 2300 VV RVG aus EUR [Gegenstandswert] + USt + Auslagen)
 zu zahlen.

3. Die Kosten des Rechtsstreits trägt die Beklagte.

4. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
 des zu vollstreckenden Betrags vorläufig vollstreckbar.

II. SACHVERHALT

Am [Datum] ereignete sich [Versicherungsfall] an dem vom Kläger
bei der Beklagten versicherten Objekt / in dem versicherten
Haushalt / bei dem versicherten Unternehmen. Einzelheiten [Anlage K1
Polizeibericht / Schadensprotokoll].

Der Kläger unterhält bei der Beklagten eine [Hausrat-/Gebäude-/
Kfz-]Versicherung, Police Nr. [Nr.], Anlage K2.

Die Beklagte lehnte die Leistung mit Schreiben vom [Datum],
Anlage K3, ab.

III. RECHTLICHE WÜRDIGUNG

1. Versicherungsfall liegt vor (vgl. § [X AVB])
 [Subsumtion]

2. Ablehnungsgrund trägt nicht
 [Obliegenheitsverletzung fehlt / Risikoausschluss unwirksam /
 Kausalität fehlt § 28 Abs. 3 VVG]
 BGH-Rechtsprechung zu Transparenzgebot (§ 307 Abs. 1 S. 2 BGB).

3. Fälligkeit und Verzug
 Der Anspruch ist gemäß § 14 VVG fällig. Verzug trat am
 [Datum] ein (Ablauf der Frist aus Anwaltsschreiben Anlage K4).

IV. BEWEISANGEBOTE

- Anlage K1: [Schadensnachweis]
- Anlage K2: Versicherungsschein mit AVB
- Anlage K3: Ablehnungsschreiben
- Sachverständigengutachten zum Nachweis des Schadens:
 Sachverständiger [Name] oder gerichtlich zu bestellen
- Zeuge: [Name, Anschrift, Beweisthema]

[Rechtsanwälte]
```

### Baustein 2 — Klageschrift Berufsunfähigkeitsversicherung (Feststellungsklage)

```
II. ANTRÄGE BU-VERSICHERUNG

1. Es wird festgestellt, dass die Beklagte verpflichtet ist, dem
 Kläger ab dem [Datum] aus dem Versicherungsvertrag (Police Nr.
 [Nr.]) eine monatliche Berufsunfähigkeitsrente in Höhe von
 EUR [X] sowie Beitragsbefreiung zu gewähren, solange Berufs-
 unfähigkeit von mindestens 50 % im Beruf des Klägers als
 [Berufsbezeichnung] besteht.

2. Die Beklagte wird verurteilt, die aufgelaufenen Rückstände
 für den Zeitraum [Beginn] bis [aktuell] in Höhe von EUR [X]
 nebst Zinsen von 5 % über Basiszinssatz ab [Datum] zu zahlen.

III. VERSICHERUNGSFALL BERUFSUNFÄHIGKEIT

Der Kläger ist seit [Datum] infolge [Diagnose, ICD-Code] zu
mindestens 50 % außerstande, seinen Beruf als [Bezeichnung]
auszuüben. Sein konkretes Berufsbild umfasste folgende Tätigkeiten:
[Detailbeschreibung der Haupttätigkeiten mit Zeitanteilen].

Beweis: Sachverständigengutachten bezogen auf die konkrete
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Eine Verweisung auf Vergleichsberufe ist nach § [X] AVB
ausgeschlossen / nach aktuellen AVB nicht vorgesehen.

IV. FESTSTELLUNGSINTERESSE

Feststellungsinteresse besteht, da die Beklagte die Leistungspflicht
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

### Baustein 3 — Antrag auf Prozesskostenhilfe

```
ANTRAG AUF PROZESSKOSTENHILFE
gemäß § 114 ZPO

[Kläger] beantragt Prozesskostenhilfe unter Beiordnung der
unterzeichneten Rechtsanwältinnen / Rechtsanwälte.

I. Wirtschaftliche Bedürftigkeit
[Kläger] ist nicht in der Lage, die Prozesskosten aufzubringen.
PKH-Erklärung mit Belegen liegt bei (Anlage PKH 1).

II. Hinreichende Erfolgsaussichten
[Zusammenfassung der Klagebegründung]

Die Klage hat hinreichende Erfolgsaussichten, da [...]
und der Beklagte keine tragfähige Ablehnung begründet hat.

III. Ratenzahlung
Ratenzahlung in Höhe von EUR [Betrag] monatlich wird angeboten.

[Rechtsanwälte]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Versicherungsfall — Eintritt | Kläger (VN) |
| Schadenshöhe, Leistungsumfang | Kläger |
| Obliegenheitsverletzung | Beklagte (Versicherer) |
| Kausalität Obliegenheit → Schaden fehlt | Kläger (Exkulpation § 28 Abs. 3 VVG) |
| Grob fahrlässige Herbeiführung | Versicherer |
| AVB-Klausel unwirksam (Transparenz) | Gericht von Amts wegen; Kläger regt an |
| Verjährung / Hemmung | Kläger für Hemmung; Beklagte für Ablauf |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung Versicherungsanspruch | 3 Jahre | Jahresende der Kenntnis | §§ 195, 199 BGB |
| Hemmung Ombudsstelle | Dauer des Verfahrens + 6 Monate | Einleitung | § 204 Abs. 1 Nr. 4 BGB |
| Hemmung Verhandlungen | Dauer | Verhandlungsbeginn | § 203 BGB |
| Antwortfrist Versicherer | keine gesetzliche Frist | ggf. setzen: 4 Wochen | § 14 VVG analog |
| Zustellung der Klageschrift | alsbald nach Einreichung § 167 ZPO | Klageeinreichung hemmt Verjährung | § 204 Abs. 1 Nr. 1 BGB |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| Versicherungsfall nicht eingetreten | AVB-Definition schmal auslegen versuchen; § 305c Abs. 2 BGB gegen Versicherer |
| Obliegenheitsverletzung — Verspätete Anzeige | § 28 Abs. 3 VVG: Kausalität; fehlende Kausalität beseitigt Leistungsfreiheit |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Forderung verjährt | Hemmungszeiträume (Ombudsstelle, Verhandlungen) in Rechnung stellen |
| AVB-Ausschluss eindeutig | Transparenztest § 307 Abs. 1 S. 2 BGB; Auslegung § 305c Abs. 2 BGB |
| Mahnverfahren zumutbar | Bei BU oder Feststellungsklage: Mahnverfahren ungeeignet; direkte Klage |

## Streitwert und Kosten

- Sachversicherung: Streitwert = Hauptforderung; RVG-Gebühren danach.
- BU-Versicherung: 3,5-facher Jahreswert der Rente (§ 9 ZPO); bei kurzer Restlaufzeit weniger.
- Gerichtskostenvorschuss: bei LG-Verfahren oft EUR 500–3000; bei PKH von Staatskasse.
- Sachverständigenkostenvorschuss § 379 ZPO: medizinischer SV ca. EUR 2000–5000; bei PKH Staatskasse.
- Anwaltsgebühren außergerichtlich erstattungsfähig ab Verzug.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Klarer Versicherungsfall, endgültige Ablehnung | Direkt Klage; kein weiteres Schreiben |
| BU — streitig über Grad | SV-Gutachten vor Klage einholen; Feststellungsantrag kombiniert mit Rückstandsantrag |
| Vergleich möglich | Schriftliches Vergleichsangebot vor Klagezustellung; Verhandlung hemmt Verjährung |
| Streitwert unter EUR 5000 | Ombudsstelle-Empfehlung bindend bis EUR 10000; weniger kostspielig |
| AVB-Klausel zweifelhaft | Transparenzargument schon im Klageschriftsatz ausführlich begründen |

## Anschluss-Skills

- `deckungsanfrage-pruefen` — Vorprüfung Deckungsablehnung
- `fachanwalt-versicherungsrecht-deckungsklage` — formale Klageschrift-Details
- `fachanwalt-versicherungsrecht-regress-abwehr` — Abwehr von Regress-Ansprüchen

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 286 Abs. 2 Nr. 3 BGB (Verzug durch Ablehnungsschreiben ohne Mahnung) → § 288 BGB (Verzugszinsen) → § 204 BGB (Hemmung durch Klage, Mahnbescheid, Schlichtungsantrag) → § 215 VVG (örtliche Zuständigkeit Klage VN) → § 281 ZPO (Mahnverfahren, Widerspruch, Abgabe) → § 256 ZPO (Feststellungsklage BU/laufende Leistung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `mandat-triage-versicherungsrecht`

**Fokus:** Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues Versicherungsmandat geht ein und muss schnell triagiert werden. Normen § 195 BGB Verjährung drei Jahre §§ 12 14 VVG Fälligkeit Schadensmeldung AVB-Klagefristen. Prüfraster Sparte Ereignis Stichtag Deckungsablehnung Hoehe Frist-Sofort-Check Eskalation bei BU-Ablehnung oder lebensbedrohlichen Krankheitskosten. Output Triage-Ergebnis mit Routing zu deckungsanfrage-prüfen und Fristen-Eskalationshinweis. Abgrenzung zu deckungsanfrage-prüfen und erstgespraech-mandatsannahme.

# Mandat-Triage Versicherungsrecht

## Zweck

Versicherungsmandate sind sparten-spezifisch — KFZ-Vollkasko ist anders als BU oder Industrieversicherung. Strukturierte Triage stellt sicher dass die richtige Bedingungslage zugrunde gelegt wird.

## Ablauf — sieben Fragen

### Frage 1 — Versicherungsnehmer oder Anspruchsteller?

- Versicherungsnehmer gegen eigene Versicherung (Erstrisikomandant)
- Geschädigter gegen Haftpflichtversicherer (Direktanspruch § 115 VVG)
- Versicherer als Mandant (Deckungsklage)
- Vermittler-Haftung

### Frage 2 — Sparte?

- KFZ-Vollkasko / Teilkasko / Haftpflicht
- Privathaftpflicht
- Hausrat / Gebäude
- Berufshaftpflicht
- Lebensversicherung (Erlebensfall Todesfall)
- Berufsunfähigkeit BU
- Krankenversicherung gesetzlich / privat
- Krankentagegeld
- Pflegeversicherung
- Rechtsschutz
- Insassenunfallversicherung
- Rentenversicherung (privat)
- Industrieversicherung Sonder-Industriedeckungen
- D&O Direktoren- und Manager-Haftpflicht
- Cyber-Versicherung

### Frage 3 — Akute Eilbedürftigkeit?

- BU-Ablehnung — kein Einkommen drohend
- Krankenversicherung weigert lebenswichtige Behandlung
- Hausrat-Brand kein Vorschuss
- Gewerbe-Betriebsunterbrechung
- Rechtsschutz-Deckungsablehnung mit drohender Verjährung Hauptverfahren

### Frage 4 — Versicherungsfall genau?

- Datum Ereignis
- Schadens-Höhe geschätzt
- Anzeige beim Versicherer Datum
- Bisherige Reaktion (Ablehnung Stillschweigen Teilzahlung)

### Frage 5 — Bedingungswerk?

- Police vorhanden?
- AVB welche Fassung?
- Tarif konkret bezeichnet?
- Risikofragebogen beim Vertragsschluss vorhanden?
- Versicherungsbeginn — technisch / formell

### Frage 6 — Frist?

- **Verjährung Versicherungsleistung** drei Jahre § 195 BGB ab Schluss des Jahres der Anspruchsentstehung und Kenntnis (§ 199 BGB)
- **AVB-Klagefrist** früher § 12 Abs. 3 VVG sechs Monate — seit VVG-Reform 2008 entfallen; aber manche älteren Verträge prüfen
- **Anzeigefrist** Schaden je nach AVB sieben Tage bis sofort
- **Wahrung der Frist durch Klage** bei Verjährung

### Frage 7 — Hauptaktenstand?

- Vollständiger Schriftwechsel?
- Bedingungswerk komplett?
- Schadensgutachten vorhanden?
- Bei BU ärztliches Gutachten?

## Routing-Matrix

| Sparte/Vorgang | Folge-Skill | Frist |
|---|---|---|
| Deckungsablehnung Sachsparte | `deckungsanfrage-pruefen` | drei Jahre Verjährung |
| BU-Ablehnung | `deckungsanfrage-pruefen` plus medizinische Gegenbegutachtung | drei Jahre |
| Leben Todesfall | `deckungsanfrage-pruefen` | drei Jahre |
| Krankenversicherung medizinische Notwendigkeit | (Skill kv-prüfung — perspektivisch) | drei Jahre |
| Rechtsschutz Deckungsablehnung | (Skill rs-deckung — perspektivisch) | drei Jahre |
| Direktanspruch Geschädigter | Skill aus `fachanwalt-verkehrsrecht` `unfall-haftungsquote-berechnen` | drei Jahre |
| Vermittlerhaftung | (Skill vermittler-haftung — perspektivisch) | drei Jahre |
| Industrieversicherung | (Skill industriedeckung — perspektivisch) | drei Jahre |

## Mandatsannahme

- **Konflikt-Check** — keine Mandate auf beiden Seiten der Versicherungs-Beziehung
- **Streitwert** ab EUR 10000 LG
- **Rechtsschutz-Deckungsanfrage** prüfen vor Mandatsannahme
- **Komplexität** AVB-Auslegung BGH-Urteilskette

## Eskalation

- **Telefon-Sofort** lebensbedrohliche KV-Ablehnung
- **Binnen einer Stunde** drohende Verjährung
- **Heute** Stellungnahme an Versicherung Rechtsschutz-Deckungsanfrage
- **Diese Woche** Klage-Erstentwurf

## Ausgabe

- `triage-protokoll-versicherungsrecht.md`
- Aktenanlage
- Rechtsschutz-Deckungsanfrage als Entwurf
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorarvereinbarung über RVG
- Empfehlung Folge-Skill

## Quellen

- VVG §§ 1 ff.
- BGB §§ 195 199 305 ff.
- BGH IV. Zivilsenat
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Vertiefung — Rechtsprechung und Normenkette Triage

### Leitsatz-Zitate (Stand Mai 2026)

Vor Versand jeweils Volltext in juris.bundesgerichtshof.de oder dejure.org aufrufen:

- BGH IV ZR 32/24, Urt. v. 12.3.2025 — Krankentagegeld; Klauselersetzung nach Intransparenz unzulässig (Pressemitteilung Nr. 47/25 v. 12.3.2025)
- BGH IV ZR 70/25 — PKV-Beitragsanpassung; Mitteilungspflicht
- BGH IV ZR 86/24, Urt. v. 15.10.2025 — PKV-Beitragsanpassung; Prüfungsmaßstab
- BGH IV ZR 153/20, Urt. v. 14.7.2021 — Versicherungsfall BU nach Ablauf der sechs-monatigen Prognosezeit
- BGH VI ZR 183/22, Urt. v. 28.1.2025 — DSGVO-Schadensersatz Art. 82 hat nur Ausgleichs-, keine Straffunktion

### Normen-Ergänzung

§ 195 BGB (Verjährung 3 Jahre) i.V.m. § 199 BGB (Kenntnis-Beginn) → § 203 BGB (Hemmung Verhandlungen) → § 28 VVG (Obliegenheit Schadensanzeige) → § 115 VVG (Direktklage Haftpflicht) → § 204 BGB (Hemmung Mahnbescheid, Klage, Schlichtungsantrag) → § 214 VVG (Ombudsmann-Verjährungshemmung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `schriftsatzkern-substantiierung`

**Fokus:** Substantiierter Schriftsatzkern für Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau.

# Schriftsatzkern und Substantiierung im Versicherungsvertragsrecht (Personen- und Sachversicherung)

## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Schriftsatz im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung) erstellt werden, typischerweise: Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage.
- Die Mandatsannahme und ggf. Vergleichsverhandlung sind abgeschlossen oder gescheitert.
- Klage-, Widerspruchs-, Einspruchs-, Rechtsmittel-Frist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Parteien (Bezeichnung wie im Vorprozess oder Bescheid, exakte Schreibweise!).
- Zustellungsanschrift Bevollmaechtigte.
- Gericht/Behörde (Zuständigkeit pruefen und im Schriftsatz darstellen, wenn streitig).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Streitwert/Gegenstandswert.

### B. Antraege

Klassischer Antrag-Block; je nach Verfahrenstyp:

- Leistungsantrag (zu zahlen, zu unterlassen, zu beseitigen, herauszugeben).
- Feststellungsantrag (Feststellungsinteresse darlegen).
- Gestaltungsantrag (Aufhebung, Anfechtung, Scheidung).
- Hilfsantraege staffeln (von eng nach weit oder von hoch nach niedrig).

### C. Tatsachenvortrag

Der Substantiierungs-Kern; pro Anspruchsgrundlage in VVG, AVB, BU-/UV-Bedingungen, ARB, PflVG eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen).
2. **Mandantenseitige Tatsachenbehauptungen** mit Beweisangeboten.
3. **Gegnerisches Verhalten** mit Belegen (Schreiben, Aussage, Verhalten).
4. **Schaden/Folgen** bezifferbar (Hauptforderung, Nebenforderung, Zinsen, Folgekosten).

### D. Rechtliche Wuerdigung

Anspruchsaufbau klassisch:

1. **Anspruchsgrundlage** nennen (z.B. § X iVm § Y).
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal wird gegen den Tatsachenvortrag gespiegelt.
3. **Einwendungen** der Gegenseite vorwegnehmen und entkraeften.
4. **Rechtsprechungs-Verweise:** BAG/BGH/BVerfG/EuGH/BFH je nach Fachgebiet; bei Versicherungsvertragsrecht (Personen- und Sachversicherung) typischerweise die letzte hoechstrichterliche Linie zitieren.
5. **Subsumtion-Ergebnis** klar formulieren.

### E. Beweisangebote

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- Urkundenbeweis: konkrete Anlage Kxx benennen, Inhalt nicht nur "Vertrag" sondern "Vertrag vom TT.MM.JJJJ, dort § X Abs. Y, Anlage K1".
- Zeugenbeweis: Name, ladungsfaehige Anschrift, Beweisthema in einem Satz.
- Sachverstaendigenbeweis: ggf. Privatgutachten mit anfuegen, gerichtliches Gutachten beantragen.
- Parteivernehmung als letzte Stufe, mit Antrag § 448 ZPO und Indiziengeruest.
- Inaugenscheinnahme: bei Sache vor Ort (Mietraum, Baustelle, Fahrzeug, Hardware).

### F. Anlagenverzeichnis

- K1, K2 ... durchnummeriert (Antragstellerin/Klaegerin).
- Bei Beklagten B1, B2 ...
- Jede Anlage mit Datum, Absender, Empfaenger, Inhaltsbeschreibung in einem Satz.
- Pflicht-Erwaehnung im Tatsachenvortrag.

## Substantiierungs-Fallen im Versicherungsvertragsrecht (Personen- und Sachversicherung)

- **Pauschaltatsachen** ohne konkrete Daten ("seit Jahren", "regelmaessig", "in mehreren Faellen") werden vom Gericht uebergangen.
- **Beweisangebot zur falschen Tatsache:** Beweisthema deckt nur Teilaussage ab.
- **Selbst-widersprueche** zwischen Schriftsatz und Anlage ("Im Vertrag steht doch was anderes").
- **Verspaeteter Vortrag** § 296 ZPO/§ 87b VwGO: Rueglich-Fristen beachten, Verschulden vermeiden.
- **Anspruchskonkurrenz** zwischen mehreren Grundlagen: nicht eine wegfallen lassen.

## Pruefkette vor Versand

1. Antragsformulierung tenoriert (urteilstauglich, vollstreckbar)?
2. Jede Tatbestandsmerkmal-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Eingangsstempel/elektronische Uebermittlung)?
4. Zuständigkeit positiv festgestellt?
5. Streitwert plausibel, ggf. mit Anlage Streitwert-Berechnung?
6. Anlagenverzeichnis vollstaendig und nummerisch konsistent?
7. beA-/EGVP-/EBO-Konformitaet (PDF/A, ERVV-Signatur)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Anwaeltin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG, BGH, BAG, BFH, BVerwG, EuGH und die jeweils massgeblichen Fachsenate für Versicherungsvertragsrecht (Personen- und Sachversicherung).
- VVG, AVB, BU-/UV-Bedingungen, ARB, PflVG sowie Verordnungen/Richtlinien dazu.
- Aktuelle Reform- und Gesetzgebungslage einbeziehen.

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisangeboten, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht, EB).
4. **Streitwertskizze** (eigenes Memo, falls > 1 Anspruch).
5. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger?).

## Beispiel-Anspruchsgrundlagen im Versicherungsvertragsrecht (Personen- und Sachversicherung)

Drei haeufig gebrauchte Anspruchsgrundlagen aus VVG, AVB, BU-/UV-Bedingungen, ARB, PflVG und ihre Substantiierungs-Anforderungen:

### Grundlage 1

- Tatbestandsmerkmal 1: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 2: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 3: konkrete Tatsache + Beweis.
- Rechtsfolge: konkreter Antrag.

### Grundlage 2

Analog - jede Tatsache braucht ein Beweisangebot.

### Grundlage 3 (Auffanggrundlage / Sekundaeranspruch)

Hilfsweise vortragen, klar als Hilfsantrag/Hilfsvortrag kennzeichnen.

## Antrags-Muster nach Verfahrenstyp

Typische Antraege in Versicherungsvertragsrecht (Personen- und Sachversicherung) (Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage):

- Hauptantrag (Leistung/Feststellung/Gestaltung).
- Hilfsantrag (z.B. für den Fall, dass Hauptforderung verjaehrt ist).
- Annex-Antraege (Zinsen, Nebenforderungen, Kosten).
- Streitwert-Antrag (falls Streitwert streitig).

## Beweisaufnahme - was das Gericht sehen will

### Urkundenbeweis

- Anlage K1: Bezeichnung, Datum, kurze Inhaltsbeschreibung.
- Im Tatsachenvortrag: "Diese Behauptung beruht auf dem als Anlage K1 vorgelegten Schreiben der Beklagten vom TT.MM.JJJJ, dort Seite Y, Absatz Z."

### Zeugenbeweis

- Form: "Beweis: Aussage der Zeugin Name, ladungsfaehige Anschrift, zum Beweisthema (konkret in einem Satz)."
- Mehrere Zeuginnen zum gleichen Thema: Indiziengeruest staerken.
- Keine Beweisermittlung ueber Zeugnis - das Beweisthema muss konkret sein.

### Sachverstaendigenbeweis

- Bei Versicherungsvertragsrecht (Personen- und Sachversicherung)-typischen Streitfaellen oft notwendig (Bauwerk, IT-System, Anlagebewertung, medizinische Frage).
- Privatgutachten als Anlage K vorlegen + zugleich gerichtliches Gutachten beantragen.
- Verfahrensoekonomie: Sachverstaendigen-Kosten frueh mit Mandantin besprechen.

### Parteivernehmung (§ 448 ZPO)

- Letzte Stufe, nur wenn andere Beweismittel ausgeschoepft.
- Indiziengeruest vortragen, das eine gewisse Wahrscheinlichkeit der Behauptung tragt.

## Replik-/Duplik-Vorausschau

Schon im Klageschriftsatz die wahrscheinlichen Einwaende der Gegenseite vorwegnehmen:

- Verjährung -> Hemmungstatbestand vortragen.
- Erfuellung/Aufrechnung -> rechtzeitige Tatsachenbasis schaffen.
- Formmangel -> Heilung/Schutz-Argument bereit halten.
- Treuwidrigkeit -> Indiziengeruest gegen Treuwidrigkeits-Vorwurf.

## Elektronische Einreichung (beA, EGVP, EBO, ELSTER)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- 1.10.2026 / 1.10.2027 - ZVollstrDigitG-Aenderungen im Vollstreckungsbereich; in Versicherungsvertragsrecht (Personen- und Sachversicherung) ggf. spezifische ERV-Pflichten beachten.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln ("Die Klage ist zulaessig und begruendet" als Ueberschrift, aber dann substantiieren).
- Mandanten- und Beweismittel-Zitate woertlich, in Anfuehrungszeichen, mit Anlage-Verweis.
- Keine Gefuehlsausbrueche - sachlich auch bei provokanter Gegenseite.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag tenorierungsfaehig
- [ ] Frist gewahrt mit Reserve
- [ ] Jede Tatsache hat Beweis
- [ ] Anlagen vollstaendig und nummeriert
- [ ] Rechtsprechungs-Zitat aktuell
- [ ] Streitwert plausibel
- [ ] beA/EGVP-konform
- [ ] Senior-/Sozius-Freigabe

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Tatsachen-Grundlage und Streitwertskizze.
- `vergleichsverhandlung-strategie` (im selben Plugin) für parallelen Vergleichsversuch (Gueteverhandlung, Mediation).

## Vertiefung — Rechtsprechung Deckungsklage Schriftsatz

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 1 VVG (Hauptleistungsanspruch, Beweislast VN) → § 307 BGB (AVB-Kontrolle) → § 286 ZPO (freie Beweiswürdigung) → § 402 ZPO (Sachverständiger) → § 256 ZPO (Feststellungsklage BU/laufende Leistung) → § 215 VVG (Zuständigkeit) → § 114 ZPO (PKH)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
