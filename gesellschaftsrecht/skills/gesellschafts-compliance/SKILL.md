---
name: gesellschafts-compliance
description: "Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger und Rechtsordnung und zeigt auf, was in den nächsten 30/60/90 Tagen f..."
---

# Gesellschafts-Compliance (Paragraf 325 HGB Bilanzpublizität; Paragraf 20 GwG Transparenzregister)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafts-Compliance (Paragraf 325 HGB Bilanzpublizität; Paragraf 20 GwG Transparenzregister)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG Paragraf 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG Paragraf 76, 93, 111, 119, 130, 243 ff.; HGB Paragraf 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Rechtsprechungsanker:** BGH, 21.04.1997 - II ZR 175/95 für Organpflichten und Informationsgrundlage; BGH, 20.11.2018 - II ZR 12/17 für Listen- und Legitimationsfragen. Weitere Entscheidungen nur mit frei prüfbarer Quelle.
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Gesellschafts-Compliance (Paragraf 325 HGB Bilanzpublizität; Paragraf 20 GwG Transparenzregister)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Kernsachverhalt

Kapitalgesellschaften und Personengesellschaften unterliegen einer Vielzahl periodisch wiederkehrender gesellschaftsrechtlicher und handelsrechtlicher Pflichten: Jahresabschluss-Offenlegung beim Unternehmensregister (Paragraf 325 HGB), Einreichung der aktuellen Gesellschafterliste beim Handelsregister (Paragraf 40 GmbHG), Meldung wirtschaftlich Berechtigter beim Transparenzregister (Paragraf 20 GwG) sowie — bei prüfungspflichtigen Gesellschaften — Jahresabschlussprüfung (Paragraf 316 HGB). Verstöße gegen diese Pflichten haben unterschiedliche Konsequenzen: Ordnungsgeldverfahren (Paragraf 335 HGB), Bußgelder (Paragraf 56 f. GwG), strafrechtliche Risiken (Paragraf 331 HGB) und — bei veralteter Gesellschafterliste — Gefährdung des gutgläubigen Erwerbs (Paragraf 16 Abs. 3 GmbHG).

Dieser Skill pflegt einen einzigen YAML-Tracker für alle Gesellschaften eines Mandanten und berechnet, was wann und für wen fällig ist.

## Kaltstart-Rückfragen

Vor der Tracker-Initialisierung sind folgende Angaben erforderlich:

1. **Gesellschaftstabelle:** Welche Gesellschaften sind zu erfassen (Name, Rechtsform, Handelsregisternummer, Registergericht, Gründungsdatum, Geschäftsjahresende)?
2. **Größenklassen:** Bilanzsumme, Umsatzerlöse, Arbeitnehmerzahl für jede GmbH/AG (Paragraf 267 HGB) — um Prüfungspflicht und Offenlegungsumfang zu bestimmen?
3. **Letzter Einreichungsstand:** Wann wurde der Jahresabschluss zuletzt beim Bundesanzeiger eingereicht? Liegt die aktuelle Gesellschafterliste beim Handelsregister?
4. **Transparenzregister:** Sind wirtschaftlich Berechtigte (Paragraf 3 GwG) im Transparenzregister eingetragen oder gilt eine Eintragungsausnahme nach Paragraf 20 Abs. 2 GwG (Eintragung im Handelsregister)?
5. **Konzernstruktur:** Gibt es Mutter-Tochter-Verhältnisse, die einen Konzernabschluss nach Paragraf 290 ff. HGB auslösen könnten?
6. **Ruhende oder aufzulösende Gesellschaften:** Sind Gesellschaften betrieblich inaktiv? Sollen sie aufgelöst werden (Paragraf 65 GmbHG, Paragraf 264 ff. AktG)?
7. **Ausländische Tochtergesellschaften:** Gibt es Paragraf 325a HGB-Pflichten für ausländische Tochtergesellschaften?
8. **Berichtszeitraum:** 30, 60 oder 90 Tage für den Fälligkeitsbericht?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte mit Auszügen

**Paragraf 325 Abs. 1 HGB — Bilanzpublizität (Offenlegungspflicht)**
> "Die gesetzlichen Vertreter von Kapitalgesellschaften haben [...] den Jahresabschluss und den Lagebericht [...] beim Betreiber des Bundesanzeigers elektronisch einzureichen."

Frist: Paragraf 325 Abs. 1a HGB — spätestens 12 Monate nach Ende des Geschäftsjahres. Kleine Kapitalgesellschaften (Paragraf 267 Abs. 1 HGB) können vereinfachte Unterlagen einreichen; nur Bilanz und Anhang, kein GuV-Ausweis.

**Paragraf 335 HGB — Ordnungsgeldverfahren**
> Wer Paragraf 325 HGB verletzt, kann vom Bundesamt für Justiz (BfJ) zur Einreichung angehalten und mit Ordnungsgeld belegt werden. Mindestordnungsgeld: 2.500 EUR; Maximum: 25.000 EUR je Verstoß. Verfahren beginnt von Amts wegen, sobald fristgerecht keine Einreichung erfolgt.

**Paragraf 40 GmbHG — Gesellschafterliste**
> "Notare, die in Angelegenheiten der Gesellschaft tätig werden, haben [...] eine von ihnen unterschriebene, aktualisierte Gesellschafterliste [...] zum Handelsregister einzureichen."

Frist: unverzüglich nach jeder Änderung (Abtretung, Kapitalerhöhung, Erbfolge). Pflicht des Notars bei notarieller Beurkundung; sonst Geschäftsführer (Paragraf 40 Abs. 2 GmbHG). Konsequenz veralteter Liste: Gutgläubiger Erwerb nach Paragraf 16 Abs. 3 GmbHG kann zustande kommen, wenn Erwerber auf die unrichtige Liste vertraut.

**Paragraf 16 Abs. 3 GmbHG — Gutgläubiger Erwerb**
> "Ist die im Handelsregister eingetragene Gesellschafterliste unrichtig, so kann ein Erwerber, der auf die Richtigkeit der Liste vertraut, gutgläubig Anteile erwerben."

Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

**Paragraf 18 ff., 20 GwG — Transparenzregister**
> Paragraf 20 GwG verpflichtet juristische Personen des Privatrechts und eingetragene Personengesellschaften, die wirtschaftlich Berechtigten (Paragraf 3 GwG) beim Transparenzregister anzumelden.

Frist: 2 Wochen nach Änderung der Beteiligungsverhältnisse. Ausnahme: Paragraf 20 Abs. 2 GwG — Eintragungspflicht gilt nicht, wenn die wirtschaftlich Berechtigten bereits aus öffentlich zugänglichen Registern (Handelsregister, Genossenschaftsregister) erkennbar sind. Seit 01.08.2021 ist das Transparenzregister ein Vollregister (keine reine Auffangfunktion mehr); Paragraf 59 Abs. 1 GwG: Übergangsfrist bis 31.03.2022 für GmbH.

**Paragraf 267 HGB — Größenklassen**

| Klasse | Bilanzsumme | Umsatzerlöse | Arbeitnehmer (Jahresdurchschnitt) |
|---|---|---|---|
| Klein (Paragraf 267 Abs. 1 HGB) | ≤ 7.500.000 EUR | ≤ 15.000.000 EUR | ≤ 50 |
| Mittelgroß (Paragraf 267 Abs. 2 HGB) | ≤ 25.000.000 EUR | ≤ 50.000.000 EUR | ≤ 250 |
| Groß (Paragraf 267 Abs. 3 HGB) | > 25.000.000 EUR | > 50.000.000 EUR | > 250 |

Zwei von drei Merkmalen müssen an zwei aufeinanderfolgenden Abschlussstichtagen erfüllt sein (Paragraf 267 Abs. 4 HGB). `[Modellwissen — Schwellenwerte beim BfJ/Unternehmensregister bestätigen]`

**Paragraf 316 HGB — Prüfungspflicht**
> "Der Jahresabschluss und der Lagebericht von Kapitalgesellschaften, die nicht kleine Kapitalgesellschaften sind, sind durch einen Abschlussprüfer zu prüfen."

Gilt für alle AG (keine Größenklassenausnahme). GmbH: Prüfungspflicht ab mittelgroß. Ohne Testierung darf der Abschluss nicht festgestellt werden.

**Paragraf 290 HGB — Konzernabschlusspflicht**
> "Die gesetzlichen Vertreter einer Kapitalgesellschaft haben einen Konzernabschluss und einen Konzernlagebericht aufzustellen, wenn diese Kapitalgesellschaft auf eine andere Gesellschaft einen beherrschenden Einfluss ausüben kann."

**Paragraf 325a HGB — Zweigniederlassungen ausländischer Gesellschaften**
> Bestimmte ausländische Gesellschaften mit Zweigniederlassung in Deutschland müssen Jahresabschlüsse in Deutschland offenlegen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Compliance-Initialisierung und laufender Betrieb

**Vorab:** Das folgende Prüfschema ist eine Standardlinie. Wenn die Mandantenlage abweicht, werden die Schritte gekürzt, umgestellt oder an einen Spezialskill übergeben. Maßgeblich ist ein belastbares Ergebnis, nicht das Abarbeiten einer Tabelle.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Gesellschaftserfassung | Alle Gesellschaften mit Rechtsform, HR-Nummer, Gründungsdatum, GJ-Ende erfasst? | Vollständige Gesellschaftsliste als Basis des Trackers |
| 2 | Größenklassenbestimmung | Paragraf 267 HGB: Bilanzsumme, Umsatz, Arbeitnehmer für jede GmbH/AG; zwei-Kriterien-Test an zwei aufeinanderfolgenden Stichtagen | Festlegung der Offenlegungspflicht und des Prüfungsumfangs |
| 3 | Prüfungspflicht | Paragraf 316 HGB: AG (immer); GmbH mittelgroß/groß; Stiftungen / Genossenschaften nach Paragraf 340, 341 HGB? | Bestellung Abschlussprüfer vor GJ-Ende; Listenmandant: Jahresplan |
| 4 | Offenlegungsfrist Paragraf 325 HGB | 12 Monate nach GJ-Ende; bei börsennotierter AG: 4 Monate (Paragraf 325 Abs. 4 HGB)? | Fälligkeitsdaten in Tracker eintragen; Frühwarnung 90 Tage vor Frist |
| 5 | Gesellschafterliste Paragraf 40 GmbHG | Letzte Einreichung beim HR; Änderungen seit letzter Einreichung (Abtretungen, Kapitalerhöhungen, Erbfolgen)? | Unverzügliche Einreichung bei Änderung; Stichtag des aktuellen Standes notieren |
| 6 | Transparenzregister Paragraf 20 GwG | Wirtschaftlich Berechtigte eingetragen? Eintragungsausnahme Paragraf 20 Abs. 2 GwG geprüft? | Bei fehlender oder veralteter Eintragung: 2-Wochen-Frist nach Änderung beachten |
| 7 | Konzernabschluss Paragraf 290 HGB | Beherrschender Einfluss auf andere Gesellschaften? Befreiungsmöglichkeit Paragraf 291–293 HGB (Konzern-Muttergesellschaft im Ausland)? | Konzernabschluss-Pflicht oder Befreiungssachverhalt dokumentieren |
| 8 | Ruhende Gesellschaften | Gesellschaft operativ inaktiv? Auflösung geplant? Tragekosten berechnet (HR-Gebühren, Steuer, RA-Honorar)? | Auflösung bei wirtschaftlich sinnloser Fortführung empfehlen (Paragraf 65 GmbHG) |
| 9 | Ordnungsgeldgefahr | Einreichungsfrist überschritten ohne Einreichung? BfJ-Verfahren bereits eingeleitet? | Sofortige Nachreichung + Stellungnahme zum Ordnungsgeldantrag |
| 10 | Status-Pflege | Alle erledigten Pflichten im Tracker mit Datum und Nachweis (Bundesanzeiger-Veröffentlichungsnummer, HR-Eintragungsdatum) aktualisiert? | Lückenloser Einreichungsnachweis für M&A-Due-Diligence und Behörden |
| 11 | 30/60/90-Tage-Vorschau | Welche Pflichten werden in den nächsten 30, 60 oder 90 Tagen fällig? | Fälligkeitsbericht für Mandant und Kanzleikalender |
| 12 | Jahresabschluss-Feststellung | Feststellung des Jahresabschlusses vor Offenlegung: bei GmbH durch Gesellschafterversammlung (Paragraf 46 Nr. 1 GmbHG); bei AG durch Vorstand + AR oder HV (Paragraf 172 f. AktG)? | Organübergreifende Terminplanung: Prüfung → Feststellung → Offenlegung |
| 13 | Jahresabschluss-Feststellungsfrist | Paragraf 264 Abs. 1 HGB: Kaufmännischer Jahresabschluss muss innerhalb der einem ordnungsgemäßen Geschäftsgang entsprechenden Zeit aufgestellt werden | Bei GmbH: spätestens in 3 Monaten nach GJ-Ende (Paragraf 264 Abs. 1 S. 3 HGB, i.d.F. BilMoG) |
| 14 | Export und Reporting | Tracker exportiert als CSV / Tabelle für Mandant, Steuerberater, WP? | Jahresplanung mit externen Beratern abgestimmt |
| 15 | Audit-Nachverfolgung | Letzte Audit-Überprüfung > 12 Monate zurück? Transparenzregister nicht geprüft? | Gesundheits-Audit durchführen (Modus 4) |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Fristgerechte Offenlegung Paragraf 325 HGB | Gesellschaft / gesetzlicher Vertreter | Nachweis durch Bundesanzeiger-Veröffentlichungsnummer und Datum |
| Gutgläubiger Erwerb Paragraf 16 Abs. 3 GmbHG | Erwerber muss Gutgläubigkeit darlegen | Unrichtigkeit der Liste: objektiv; Kenntnis des Erwerbers: subjektiv (Erwerber muss fehlendes Wissen beweisen) |
| Ordnungsgemäße Transparenzregister-Eintragung | Gesellschaft (Transparenzregister-Auszug als Nachweis) | Bußgeldverfahren: Behörde trägt Beweislast für den Verstoß; Gesellschaft muss Eintragung nachweisen |
| Prüfungspflicht besteht nicht (Paragraf 316 HGB) | Gesellschaft (Nachweis Kleinunternehmen nach Paragraf 267 HGB) | Nachweis durch Jahresabschluss der zwei vorangegangenen Geschäftsjahre |
| Gesellschafterliste aktuell (Paragraf 40 GmbHG) | Notar / Geschäftsführer | Nachweis durch aktuellen HR-Auszug mit Datumsangabe der letzten Änderung |

## Fristen und Verjährung

| Pflicht | Frist | Norm | Konsequenz bei Versäumnis |
|---|---|---|---|
| Jahresabschluss-Offenlegung | 12 Monate nach GJ-Ende | Paragraf 325 Abs. 1a HGB | Ordnungsgeldverfahren BfJ (Paragraf 335 HGB); mind. 2.500 EUR |
| Jahresabschluss-Offenlegung börsennotierte AG | 4 Monate nach GJ-Ende | Paragraf 325 Abs. 4 HGB | Zusätzlich WpHG-Sanktionen, MAR-Pflichten |
| Gesellschafterliste | Unverzüglich nach Änderung | Paragraf 40 GmbHG | Gutgläubiger Erwerb (Paragraf 16 Abs. 3 GmbHG); Haftung Geschäftsführer |
| Transparenzregister-Eintragung | 2 Wochen nach Änderung | Paragraf 20 GwG | Bußgeld Paragraf 56 f. GwG bis 1.000.000 EUR (vorsätzlich) oder 500.000 EUR (fahrlässig) |
| Jahresabschluss-Aufstellung GmbH | 3 Monate nach GJ-Ende | Paragraf 264 Abs. 1 S. 3 HGB | Pflichtverletzung Geschäftsführer; Schadensersatz Paragraf 43 GmbHG |
| HV-Einberufung AG | Binnen 8 Monate nach GJ-Ende | Paragraf 175 AktG | Ordnungswidrigkeitenrisiko; Aktionärsrechte gefährdet |
| Konzernabschluss-Offenlegung | 12 Monate nach GJ-Ende | Paragraf 325 HGB i.V.m. Paragraf 290 HGB | Ordnungsgeldverfahren BfJ |
| Ordnungsgeld-Widerspruch | 1 Monat nach Zustellung | Paragraf 335 Abs. 3 HGB | Ordnungsgeld wird bestandskräftig |
| Verjährung Ordnungsgeldbescheid | 3 Jahre (Verjährungsfrist OWiG) | Paragraf 31 OWiG | Nach Ablauf kein Vollzug mehr |

## Typische Gegenargumente

| Einwand | Begründung Gegenseite | Erwiderung |
|---|---|---|
| Kleine GmbH muss keinen GuV offenlegen | Paragraf 326 HGB: kleine GmbH nur Bilanz + Anhang | Richtig — aber Bilanz + Anhang müssen trotzdem fristgerecht eingereicht werden; häufig wird auch die verkürzte Offenlegung versäumt |
| Gesellschafterliste ist aktuell — Notar hat nicht gehandelt | Pflicht liegt beim Notar (Paragraf 40 Abs. 1 GmbHG) | Bei eigener Erkenntnis der Änderung trifft den Geschäftsführer Subsidiärpflicht (Paragraf 40 Abs. 2 GmbHG); Haftungsrisiko des GF prüfen |
| Transparenzregister-Eintragung entbehrlich wegen HR-Eintragung | Paragraf 20 Abs. 2 GwG: Mitteilung entbehrlich, wenn Angaben aus anderen Registern erkennbar | Seit 01.08.2021 Vollregister; Ausnahme gilt nur noch für exakt übereinstimmende Angaben; im Zweifel aktiv eingetragen lassen |
| Offenlegung verspätet, aber Ordnungsgeldverfahren noch nicht eingeleitet | Kein Schaden eingetreten | BfJ leitet Verfahren von Amts wegen ein; nachträgliche Einreichung mindert das Ordnungsgeld, hebt es aber nicht auf; unverzügliche Nachreichung + Erklärung einreichen |
| GJ nicht zum 31.12 — Frist läuft anders | Richtig: 12 Monate nach individuellem GJ-Ende | Tracker muss GJ-Ende je Gesellschaft individuell erfassen; Standardannahme 31.12. kann falsch sein |
| Prüfungspflicht entfällt, weil Gesellschaft geschrumpft | Paragraf 267 Abs. 4 HGB: Größenklassenwechsel erst nach zwei aufeinanderfolgenden Abschlussstichtagen | Prüfungspflicht besteht noch ein weiteres Jahr nach Unterschreiten der Schwellen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Compliance-Programm initialisierten oder prüfen | Compliance-Schema nach Checkliste; Template unten |
| Variante A — Kleines Unternehmen kein Budget für umfangreiches Programm | Minimalanforderungen-Compliance-Set statt Vollprogramm |
| Variante B — Branchenspezifische Anforderungen GwG DSGVO | Branchen-spezifisches Compliance-Modul einsetzen |
| Variante C — Bereits Ermittlungsverfahren laeuft | Compliance-Untersuchung als Verteidigung; Kooperation mit Behörden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Widerspruch gegen Ordnungsgeldbescheid (Paragraf 335 HGB)

```
An das
Bundesamt für Justiz
Referat IV 4
53094 Bonn

[Mandant / Gesellschaft]
[Anschrift]

[Ort, Datum]

Az. [Ordnungsgeldaktenzeichen]

Widerspruch gegen den Ordnungsgeldbescheid vom [Datum]

Sehr geehrte Damen und Herren,

wir vertreten die [Gesellschaft], [HR-Nummer], [Anschrift], in der oben bezeichneten
Angelegenheit. Gegen den Ordnungsgeldbescheid vom [Datum], der unserer Mandantin am
[Datum] zugegangen ist, legen wir hiermit

 W i d e r s p r u c h

ein.

Begründung:

Der Jahresabschluss der [Gesellschaft] für das Geschäftsjahr [Jahr] wurde am [Datum] beim
Betreiber des Bundesanzeigers eingereicht. Der Bundesanzeiger-Veröffentlichungscode lautet:
[Code].

Die verspätete Einreichung ist auf [konkrete Begründung: Prüfungsverzögerung durch
Wirtschaftsprüfer / IT-Umstellung / externe Umstände] zurückzuführen, für die der
gesetzliche Vertreter keine Verantwortung trägt. Wir bitten, dies bei der
Ordnungsgeldbemessung zu berücksichtigen.

Wir bitten höflich, das Ordnungsgeldverfahren einzustellen und den Bescheid aufzuheben.

Mit freundlichen Grüßen
[Kanzlei / Name]
Rechtsanwalt / Rechtsanwältin

Anlage: Bundesanzeiger-Veröffentlichungsbestätigung vom [Datum]
```

### Baustein 2: Aufforderungsschreiben an Geschäftsführer zur Einreichung Gesellschafterliste

```
An den Geschäftsführer
[Name GmbH]
[Anschrift]

[Ort, Datum]

Handelsregister-Einreichung der Gesellschafterliste (Paragraf 40 GmbHG) — dringende Fristsetzung

Sehr geehrter Herr/Frau [Name],

in Ihrer Eigenschaft als Geschäftsführer der [Name GmbH] sind Sie gemäß Paragraf 40 Abs. 2
GmbHG verpflichtet, nach jeder Änderung der Beteiligungsverhältnisse eine aktualisierte
Gesellschafterliste unverzüglich zum Handelsregister einzureichen.

Die Abtretung der Geschäftsanteile des Herrn [Name] an [Erwerber] wurde am [Datum]
notariell beurkundet und ist noch nicht in der beim Handelsregister hinterlegten
Gesellschafterliste (Stand: [Datum]) eingetragen.

Wir fordern Sie auf, spätestens bis zum [Datum = 10 Tage] die aktualisierte
Gesellschafterliste beim Amtsgericht [Registergericht] zur Aufnahme in das
Handelsregister einzureichen.

Wir weisen darauf hin, dass eine nicht ordnungsgemäß eingetragene Gesellschafterliste
das Risiko eines gutgläubigen Erwerbs gemäß Paragraf 16 Abs. 3 GmbHG begründet.

Mit freundlichen Grüßen
[Kanzlei / Name]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klärenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

### Baustein 3: Gesellschafts-Compliance-Tracker YAML (vollständig)

```yaml
### Gesellschafts-Compliance-Tracker
### Erstellt: [JJJJ-MM-TT]
### Zuletzt aktualisiert: [JJJJ-MM-TT]
### HINWEIS: Fristen sind nur Referenz — beim Bundesanzeiger/HR/TR bestätigen

metadaten:
 unternehmen: "[Konzern- / Mandantenname]"
 erstellt: "[Datum]"
 zuletzt_aktualisiert: "[Datum]"
 letztes_audit: null

gesellschaften:
 - name: "Alpha GmbH"
 typ: "GmbH"
 handelsregisternummer: "HRB 12345"
 registergericht: "Amtsgericht München"
 gruendungsdatum: "2015-01-10"
 status: "aktiv"
 groessenklasse: "mittelgroß Paragraf 267 Abs. 2 HGB"
 geschaeftsjahr_ende: "12-31"
 abschlusspruefung_pflicht: "ja"
 gesellschafter_liste_aktuell: "2025-11-15"
 notizen: "Abtretung März 2026 noch nicht eingetragen"

 pflichten:
 - typ: "Jahresabschluss Paragraf 325 HGB"
 faellig: "2026-12-31"
 faelligkeits_grundlage: "GJ-Ende 31.12.2025 + 12 Monate"
 zuletzt_eingereicht: "2025-10-15"
 status: "aktuell"
 notizen: "GJ 2025 bis 31.12.2026 einzureichen"

 - typ: "Gesellschafterliste Paragraf 40 GmbHG"
 faellig: "2026-04-05"
 faelligkeits_grundlage: "Unverzüglich nach Abtretung März 2026"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Abtretung v. 20.03.2026 noch nicht eingetragen; GF aufgefordert"

 - typ: "Transparenzregister Paragraf 20 GwG"
 faellig: "2026-04-03"
 faelligkeits_grundlage: "Änderung wirtschaftlich Berechtigter März 2026 + 2 Wochen"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Neuer wirtschaftlich Berechtigter nach Abtretung"

 - typ: "Jahresabschlussprüfung Paragraf 316 HGB"
 faellig: "2026-05-31"
 faelligkeits_grundlage: "Vor Feststellung und Offenlegung GJ 2025"
 zuletzt_eingereicht: null
 status: "bald_fällig"
 notizen: "Prüfungsauftrag an KPMG erteilt 01.02.2026"
```

## Tracker-Datei (technische Beschreibung)

Pfad: `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/gesellschaften/compliance-tracker.yaml`

**Status-Werte:**
- `aktuell` — eingereicht für laufende Periode; nichts fällig in 90 Tagen
- `bald_fällig` — fällig innerhalb von 90 Tagen
- `überfällig` — Fälligkeitsdatum überschritten ohne eingetragenes Einreichungsdatum
- `unbekannt` — keine Information; manuelle Bestätigung erforderlich

## Wichtiger Hinweis zu Fristen

> Die Einreichungsfristen spiegeln öffentlich verfügbare gesetzliche Anforderungen wider. Fristen und Anforderungen können sich ändern. **Fristen immer mit dem Bundesamt für Justiz (Paragraf 335 HGB), dem Handelsregister oder dem Transparenzregister direkt bestätigen, bevor sie für Compliance-Zwecke verwendet werden.** `[Modellwissen — prüfen]`

## Modus 1: Initialisierung

Ohne Tracker oder mit `--rebuild`.

### Schritt 1: Gesellschaftstabelle laden

Aus Praxisprofil `## Gesellschafts-Compliance` → Gesellschaftstabelle. Falls vorhanden: direkt verwenden. Falls nicht: Kaltstart-Rückfragen stellen.

### Schritt 2: Für jede Gesellschaft Pflichten ermitteln

**GmbH — Standardpflichten:**

| Pflicht | Norm | Frist | Konsequenz bei Verstoß |
|---|---|---|---|
| Jahresabschluss Offenlegung | Paragraf 325 Abs. 1 HGB | 12 Monate nach GJ-Ende | Ordnungsgeld BfJ Paragraf 335 HGB (mind. 2.500 EUR) |
| Gesellschafterliste | Paragraf 40 GmbHG | Unverzüglich nach Änderung | Gutgläubiger Erwerb Paragraf 16 Abs. 3 GmbHG; Haftung GF Paragraf 43 GmbHG |
| Transparenzregister | Paragraf 20 GwG | 2 Wochen nach Änderung | Bußgeld Paragraf 56 f. GwG bis 1.000.000 EUR |
| Jahresabschlussprüfung | Paragraf 316 HGB | Vor Offenlegung (mittelgroß/groß) | Strafbarkeit Paragraf 331 HGB; keine Testierung |

**AG — Standardpflichten:**

| Pflicht | Norm | Frist |
|---|---|---|
| Jahresabschluss Offenlegung | Paragraf 325 HGB | 12 Monate; börsennotiert: 4 Monate |
| Prüfpflicht | Paragraf 316 HGB | Alle AG (keine Größenausnahme) |
| HV-Einberufung (Jahresabschluss) | Paragraf 175 AktG | Binnen 8 Monate nach GJ-Ende |
| Transparenzregister | Paragraf 20 GwG | 2 Wochen nach Änderung |

### Schritt 3: Tracker schreiben

Compliance-Tracker mit allen Gesellschaften und berechneten Pflichten generieren.

## Modus 2: Bericht

```
/gesellschaftsrecht:gesellschafts-compliance --bericht [--tage 30|60|90|180]
```

```
GESELLSCHAFTS-COMPLIANCE-BERICHT — [Datum]
[Unternehmensname]

ÜBERFÄLLIG ([N]):
 [Gesellschaft] / [Pflicht] — war fällig am [Datum]

FÄLLIG INNERHALB [N] TAGE ([N]):
 [Gesellschaft] / [Pflicht] — fällig [Datum]

KÜRZLICH EINGEREICHT ([N] in letzten 90 Tagen):
 [Gesellschaft] / [Pflicht] — eingereicht [Datum]

UNBEKANNTER STATUS ([N]):
 [Gesellschaft] / [Pflicht] — keine Information; direkt beim Registerführer bestätigen

TRANSPARENZREGISTER:
 Zuletzt geprüft: [Datum]
 Gesellschaften mit aktueller Eintragung: [N] von [N]
 Gesellschaften ohne Prüfung in letzten 12 Monaten: [Liste]
```

## Modus 3: Update

### Folgenreiche-Handlung-Sperre (Einreichung)

Falls Rolle **Nichtjurist**:
> Eine Jahresabschluss-Einreichung beim Bundesanzeiger oder eine Handelsregistereintragung hat rechtliche Konsequenzen. Vor Einreichung mit einem Rechtsanwalt oder Steuerberater besprechen. `[Prüfen]`

Manuelles Update:
> "Jahresabschluss der Alpha GmbH zum 31.12.2025 am 05.03.2026 beim Bundesanzeiger eingereicht."

Massen-Update: Wirtschaftsprüfer-Bericht oder HR-Auszug hochladen; Matching-Gesellschaften automatisch aktualisieren.

## Modus 4: Gesundheits-Audit

```
/gesellschaftsrecht:gesellschafts-compliance --audit
```

**Einreichungs-Compliance:** Überfällige und unbekannte Punkte.

**Gesellschaftsgesundheit:**
- Ruhende Gesellschaften: Auflösung (Paragraf 65 GmbHG) sinnvoller als Weiterbetrieb?
- Fehlende Gründungsdaten: Fristberechnung unzuverlässig.
- Gesellschafterliste veraltet: Risiko gutgläubiger Erwerb (Paragraf 16 Abs. 3 GmbHG).

**Transparenzregister-Lücken:** Gesellschaften ohne Eintragung oder ohne geprüfte Ausnahme.

**Bilanzpublizitäts-Lücken:** Offenlegung > 12 Monate zurück = Ordnungsgeldgefahr.

**Konzern-Pflichten:** Paragraf 290 HGB-Konzernabschluss-Pflicht; Paragraf 325a HGB für ausländische Töchter.

```
GESELLSCHAFTS-GESUNDHEITS-AUDIT — [Datum]

EINREICHUNGS-COMPLIANCE
 Überfällig: [N]
 Unbekannter Status: [N]

RUHENDE GESELLSCHAFTEN ([N])
 [Liste mit Alter und jährlichen Tragekosten]

TRANSPARENZREGISTER
 Nicht eingetragen / geprüft: [N] Gesellschaften

BILANZPUBLIZITÄT Paragraf 325 HGB
 Überfällig (>12 Monate): [N] Gesellschaften
 Ordnungsgeldgefahr BfJ: [Liste]

EMPFOHLENE MASSNAHMEN
 1. [Höchste Priorität]
 2. [etc.]
```

## Modus 5: Export

```
/gesellschaftsrecht:gesellschafts-compliance --export [--format csv|tabelle]
```

CSV-Spalten: `Gesellschaftsname, Typ, HR-Nummer, Registergericht, Gründungsdatum, Status, Größenklasse, GJ-Ende, Pflicht, Fällig, Zuletzt eingereicht, Notizen`

## Streitwert und Kosten

| Verstoß | Sanktionsrahmen | Rechtsgrundlage |
|---|---|---|
| Verspätete Offenlegung Paragraf 325 HGB | Ordnungsgeld 2.500 – 25.000 EUR je Verstoß; Wiederholung möglich | Paragraf 335 HGB |
| Verletzung Transparenzregisterpflicht (vorsätzlich) | Bußgeld bis 1.000.000 EUR | Paragraf 56 Abs. 1 GwG |
| Verletzung Transparenzregisterpflicht (fahrlässig) | Bußgeld bis 500.000 EUR | Paragraf 56 Abs. 1 GwG |
| Falsche Jahresabschlussunterlagen Paragraf 331 HGB | Freiheitsstrafe bis 3 Jahre oder Geldstrafe | Paragraf 331 HGB |
| Haftung GF für veraltete Gesellschafterliste | Schadensersatz nach Paragraf 43 GmbHG | Paragraf 43 GmbHG; Paragraf 16 Abs. 3 GmbHG |
| RA-Beratungshonorar Ordnungsgeldwiderspruch | Gegenstandswert = Ordnungsgeldbetrag; 2 Gebühren (Paragraf 13, 14 RVG) | RVG Nr. 2300 |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Mandant hat 10+ Gesellschaften und keine strukturierte Fristübersicht | Compliance-Tracker initialisieren; jährlicher Audit-Termin im Kanzleikalender; automatische 90-Tage-Frühwarnung |
| BfJ-Ordnungsgeldverfahren läuft | Sofortige Nachreichung + Widerspruch mit Begründung der Verspätungsursache; Ordnungsgeld wird bei unverzüglicher Nachreichung häufig reduziert |
| Abtretung ohne Notar / ohne Gesellschafterlisten-Update | Notar beauftragen; Gesellschafterliste unverzüglich einreichen; Transparenzregister-Meldung binnen 2 Wochen |
| M&A-Due-Diligence: Gesellschafterliste veraltet | Verkäufer-Garantie für ordnungsgemäße Gesellschafterliste verlangen; gutgläubigen Erwerb durch Dritte ausschließen; Closing-Bedingung: aktuelle HR-Liste |
| Größenklassenwechsel in Sichtweite | Paragraf 267 Abs. 4 HGB-Zweijahresregel prüfen; wenn zweites Jahr unter Schwellen: Prüfungspflicht entfällt; Prüfungsvertrag ggf. nicht verlängern |
| Ruhende Gesellschaft seit > 3 Jahren | Formale Auflösung (Paragraf 65 GmbHG) prüfen; Kostenersparnis (HR-Gebühren, Buchhaltung, Steuern) gegen Auflösungsaufwand abwägen |

## Output-Template

**Adressat:** Mandant / Geschäftsführer / Complianceverantwortlicher — Tonfall: sachlich-strukturiert, handlungsorientiert

```
GESELLSCHAFTS-COMPLIANCE-BERICHT
Mandat/Praxis: [MANDATSCODE / PRAXISNAME]
Erstellt von: [NAME], [KANZLEI]
Datum: [TT.MM.JJJJ]
Berichtszeitraum: [DATUM] bis [DATUM]

> Vertraulich — Mandatsgeheimnis Paragraf 43a Abs. 2 BRAO.

--- PORTFOLIOÜBERSICHT ---
Gesellschaften gesamt: [N]
Status aktiv: [N] | ruhend: [N] | unbekannt: [N]

--- BILANZPUBLIZITAET Paragraf 325 HGB ---
Frist 12 Monate nach Geschaeftsjahresende

| Gesellschaft | GJ-Ende | Offenlegungsfrist | Eingereicht | Status |
|---|---|---|---|---|
| [NAME GmbH] | [TT.MM.JJJJ] | [TT.MM.JJJJ] | [TT.MM.JJJJ / OFFEN] | [OK / UEBERFAELLIG / ORDNUNGSGELD] |

Ordnungsgeldgefahr (Paragraf 335 HGB): [N] Gesellschaften
Hoechstes Risiko: [NAME], ueberfaellig seit [N] Tagen (drohendes Ordnungsgeld: bis [BETRAG] EUR)

--- GESELLSCHAFTERLISTE Paragraf 40 GmbHG ---
Zuletzt eingereicht: [DATUM] / noch nicht eingereicht
Aendering: [BESCHREIBUNG] am [DATUM]
Handlungsbedarf: [JA — Notar beauftragen bis TT.MM.JJJJ / NEIN]

--- TRANSPARENZREGISTER Paragraf 18 ff. GwG ---
Beguenstigter(wirtschaftlich Berechtigter): [NAME], [BETEILIGUNG] %
Letztes Update: [DATUM]
Status: [AKTUELL / AENDERUNG ERFORDERLICH bis TT.MM.JJJJ]

--- PRÜFUNGSPFLICHT Paragraf 316 HGB ---
| Gesellschaft | Groessenklasse | Pruefungspflichtig | Pruefungsauftrag erteilt |
|---|---|---|---|
| [NAME] | [Gross / Mittel / Klein] | [JA / NEIN] | [DATUM / OFFEN] |

--- EMPFOHLENE MASSNAHMEN (PRIORISIERT) ---
1. [HOECHSTE PRIORITAET] — Frist: [DATUM] — verantwortlich: [PERSON]
2. [MITTLERE PRIORITAET] — Frist: [DATUM] — verantwortlich: [PERSON]
3. [NIEDRIGE PRIORITAET] — keine akute Frist

--- NAECHSTER AUDIT-TERMIN ---
[DATUM] (Empfehlung: jaehrlich, 90 Tage vor GJ-Ende)
```

## Rote Schwellen

- **Bilanzpublizitaet Paragraf 325 HGB > 12 Monate ueberfaellig** — Ordnungsgeldverfahren BfJ laeuft oder droht (Paragraf 335 HGB: bis 25.000 EUR je Verstoß); sofort Jahresabschluss erstellen und einreichen.
- **Gesellschafterliste Paragraf 40 GmbHG nach Abtretung > 3 Wochen nicht eingereicht** — gutglaeuber Erwerb durch Dritte möglich (Paragraf 16 Abs. 3 GmbHG); Notar sofort beauftragen.
- **Transparenzregister-Eintrag nach Beteiligungsaenderung > 2 Wochen nicht aktualisiert** — Bußgeld bis 1.000.000 EUR (Paragraf 56 Abs. 1 GwG).
- **Groessenklassenwechsel zur großen Kapitalgesellschaft nicht erkannt** — Prüfungspflicht Paragraf 316 HGB gilt ab zweitem Jahr in Folge (Paragraf 267 Abs. 4 HGB); Prüfungsauftrag erteilen.

## Anschluss-Skills

- `gesellschaftsrecht:gesellschaftsrecht-mandat-arbeitsbereich` — Mandatsworkspace für die betroffene Gesellschaft
- `gesellschaftsrecht:vollzugs-checkliste` — Gesellschafterliste und Transparenzregister als Vollzugspflicht bei M&A
- `gesellschaftsrecht:aufsichtsrat-protokoll` — Jahresabschluss-Billigung nach Paragraf 172 AktG protokollieren
- `gesellschaftsrecht:tabellenpruefung` — Compliance-Tabelle aus Jahresabschlussdaten prüfen

## Quellen und Zitierweise

- Paragraf 325 HGB (Bilanzpublizität / Offenlegungspflicht)
- Paragraf 335 HGB (Ordnungsgeldverfahren Bundesamt für Justiz)
- Paragraf 40 GmbHG (Gesellschafterliste)
- Paragraf 18 ff., 20 GwG (Transparenzregister)
- Paragraf 267 HGB (Größenklassen)
- Paragraf 316 HGB (Prüfungspflicht)
- Paragraf 16 Abs. 3 GmbHG (Gutgläubiger Erwerb)
- Paragraf 290 HGB (Konzernabschlusspflicht)
- Paragraf 264 Abs. 1 HGB (Aufstellungsfrist)

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Scholz, GmbHG, 12. Aufl. 2018, Paragraf 40 Rn. 3 ff. (Gesellschafterliste).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle verwenden.

## Was dieser Skill nicht tut

- Er reicht keine Dokumente ein. Ausgabe ist Tracker und Aufgabenliste; Einreichung erfolgt durch Anwalt/Steuerberater.
- Er ruft keine Registerauszüge ab; er verfolgt, wann sie zuletzt bestätigt wurden.
- Er bestimmt nicht, ob eine Konzernabschluss-Pflicht besteht — das erfordert eine Analyse der tatsächlichen Konzernverhältnisse.
- Er ersetzt keine Steuerberatung (Paragraf 316 HGB-Prüfung = Steuerberater/Wirtschaftsprüfer).
