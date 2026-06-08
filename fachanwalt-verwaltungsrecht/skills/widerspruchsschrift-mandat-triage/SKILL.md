---
name: widerspruchsschrift-mandat-triage
description: "Widerspruchsschrift Mandat Triage im Plugin Fachanwalt Verwaltungsrecht: prüft konkret Widerspruchsschrift nach §§ 68 ff, Eingangs-Triage für verwaltungsrechtliche Mandate, Substantiierten Schriftsatzkern für verwaltungsrechtliche. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Widerspruchsschrift Mandat Triage

## Arbeitsbereich

**Widerspruchsschrift Mandat Triage** ordnet den Fall über die tragenden Prüfungslinien: Widerspruchsschrift nach §§ 68 ff, Eingangs-Triage für verwaltungsrechtliche Mandate, Substantiierten Schriftsatzkern für verwaltungsrechtliche. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-verwaltungsrecht-widerspruchsschrift` | Widerspruchsschrift nach §§ 68 ff. VwGO gegen belastenden Verwaltungsakt formulieren: Mandant hat Bescheid erhalten und will innerhalb der Frist Widerspruch einlegen. Normen: § 68 VwGO (Vorverfahren), § 70 Abs. 1 VwGO (Frist 1 Monat), § 80 Abs. 1 VwGO (aufschiebende Wirkung), § 58 Abs. 2 VwGO (Jahresfrist ohne Rechtsbehelfsbelehrung). Prüfraster: Statthaftigkeit (Bundesland?), Fristberechnung, aufschiebende Wirkung vs. sofortige Vollziehung, Begründung. Output Widerspruchsschrift. Abgrenzung: Anfechtungsklage direkt (kein Widerspruch statthaft) siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Eilantrag siehe eilantrag-80-abs-5-vwgo. |
| `mandat-triage-verwaltungsrecht` | Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks. Normen: § 70 VwGO (Widerspruch 1 Monat), § 74 VwGO (Klage 1 Monat), § 75 VwGO (Untätigkeitsklage 3 Monate). Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht, Schule, Subventionen, Auslaender), Behördenebene, Verfahrensstand, Frist-Sofort-Check, Eskalation bei drohendem Vollzug. Output Triage-Protokoll mit Fristen-Ampel, Routing-Empfehlung. Abgrenzung: Detailprüfung siehe widerspruch-oder-klage-erstprüfung; Schriftsatz siehe schriftsatzkern-substantiierung. |
| `schriftsatzkern-substantiierung` | Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspruch, Anfechtungsklage, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO. Normen: §§ 42 und 80 VwGO sowie §§ 28 und 48 VwVfG. Prüfraster: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. Output Schriftsatz-Geruest mit Klagepunkten und Begründungs-Bausteine. Abgrenzung: Fertige Klageschrift siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Vergabe-Schriftsatz siehe fachanwalt-vergaberecht-Plugin. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-verwaltungsrecht-widerspruchsschrift`

**Fokus:** Widerspruchsschrift nach §§ 68 ff. VwGO gegen belastenden Verwaltungsakt formulieren: Mandant hat Bescheid erhalten und will innerhalb der Frist Widerspruch einlegen. Normen: § 68 VwGO (Vorverfahren), § 70 Abs. 1 VwGO (Frist 1 Monat), § 80 Abs. 1 VwGO (aufschiebende Wirkung), § 58 Abs. 2 VwGO (Jahresfrist ohne Rechtsbehelfsbelehrung). Prüfraster: Statthaftigkeit (Bundesland?), Fristberechnung, aufschiebende Wirkung vs. sofortige Vollziehung, Begründung. Output Widerspruchsschrift. Abgrenzung: Anfechtungsklage direkt (kein Widerspruch statthaft) siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Eilantrag siehe eilantrag-80-abs-5-vwgo.

# Widerspruchsschrift

## Kernsachverhalt

Gegen einen belastenden Verwaltungsakt ist als Vorverfahren — sofern nicht durch Bundes- oder Landesrecht ausgeschlossen — zunächst Widerspruch einzulegen. Erst nach Erlass des Widerspruchsbescheids oder Ablauf der Entscheidungsfrist ist die Anfechtungsklage zulässig. Das Widerspruchsverfahren bietet die Chance der vollständigen Überprüfung des Verwaltungsakts auf Rechtmäßigkeit und Zweckmäßigkeit und ermöglicht eine frühzeitige Einigung ohne Klageverfahren.

## Kaltstart-Rückfragen

1. Welcher Verwaltungsakt — welche Behörde, Datum, Zustellungsdatum? Ist die Rechtsbehelfsbelehrung ordnungsgemäß?
2. Ist das Widerspruchsverfahren im Bundesland und Sachgebiet vorgesehen — oder wurde es durch Landesgesetz ausgeschlossen (§ 68 Abs. 1 Satz 2 VwGO i.V.m. Landesrecht; z.B. NRW, Bayern, Niedersachsen für bestimmte Gebiete)?
3. Hat der Verwaltungsakt aufschiebende Wirkung — oder entfällt sie nach § 80 Abs. 2 VwGO (öffentliche Abgaben, Polizei, gesetzlicher Ausschluss, Sofortvollzug)?
4. Welche formellen Mängel sind erkennbar — fehlende Anhörung § 28 VwVfG, mangelhafte Begründung § 39 VwVfG, Zuständigkeitsmangel?
5. Welche materiellen Mängel bestehen — Tatbestand nicht erfüllt, Ermessensfehler §§ 40 VwVfG, 114 VwGO, Unverhältnismäßigkeit?
6. Soll parallel Eilrechtsschutz beantragt werden — § 80 Abs. 5 VwGO bei Sofortvollzug oder § 80 Abs. 4 VwGO Antrag bei Behörde?
7. Ist eine Hinzuziehung des Bevollmächtigten für das Vorverfahren nach Landesrecht erforderlich und kostenpflichtig?
8. Ist ein Widerspruchsgebühr-Regime im Bundesland anwendbar — Kosten des Vorverfahrens nach VwVfG oder Landesgebührengesetz?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 68 Abs. 1 VwGO** — Vor Erhebung der Anfechtungsklage sind Rechtmäßigkeit und Zweckmäßigkeit des Verwaltungsakts in einem Vorverfahren nachzuprüfen. Einer solchen Nachprüfung bedarf es nicht, wenn ein Gesetz dies bestimmt oder wenn der Abhilfebescheid oder der Widerspruchsbescheid erstmalig eine Beschwer enthält.

**§ 70 Abs. 1 VwGO** — Der Widerspruch ist innerhalb eines Monats, nachdem der Verwaltungsakt dem Beschwerten bekanntgegeben worden ist, schriftlich, in elektronischer Form nach § 3a VwVfG oder zur Niederschrift bei der Behörde zu erheben, die den Verwaltungsakt erlassen hat.

**§ 58 Abs. 2 VwGO** — Ist die Rechtsbehelfsbelehrung unterblieben oder unrichtig erteilt, so ist die Einlegung des Rechtsbehelfs innerhalb eines Jahres seit Zustellung zulässig.

**§ 79 Abs. 1 VwGO** — Gegenstand der Anfechtungsklage ist der ursprüngliche Verwaltungsakt in der Gestalt, die er durch den Widerspruchsbescheid gefunden hat.

**§ 28 Abs. 1 VwVfG** — Bevor ein Verwaltungsakt erlassen wird, der in Rechte eines Beteiligten eingreift, ist diesem Gelegenheit zu geben, sich zu den für die Entscheidung erheblichen Tatsachen zu äußern.

**§ 39 Abs. 1 VwVfG** — Ein schriftlicher oder elektronischer sowie ein schriftlich oder elektronisch bestätigter Verwaltungsakt ist mit einer Begründung zu versehen.

**§ 40 VwVfG** — Ist die Behörde ermächtigt, nach ihrem Ermessen zu handeln, hat sie ihr Ermessen entsprechend dem Zweck der Ermächtigung auszuüben und die gesetzlichen Grenzen des Ermessens einzuhalten.

**§ 45 Abs. 1 Nr. 3 VwVfG** — Eine Verletzung von Verfahrens- oder Formvorschriften, die nicht den Verwaltungsakt nach § 44 nichtig macht, ist unbeachtlich, wenn … die erforderliche Begründung nachträglich gegeben wird; dies gilt auch nach § 28 (Anhörung).

**§ 45 Abs. 2 VwVfG** — Handlungen nach Absatz 1 können bis zum Abschluss der letzten Tatsacheninstanz eines verwaltungsgerichtlichen Verfahrens nachgeholt werden.

**§ 114 VwGO** — Soweit die Verwaltungsbehörde ermächtigt ist, nach ihrem Ermessen zu handeln, prüft das Gericht auch, ob der Verwaltungsakt rechtswidrig ist, weil die gesetzlichen Grenzen des Ermessens überschritten sind oder von dem Ermessen in einer dem Zweck der Ermächtigung nicht entsprechenden Weise Gebrauch gemacht ist.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Widerspruch

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Norm | Inhalt |
|---|---|---|---|
| 1 | Statthaftigkeit Widerspruchsverfahren | § 68 VwGO + Landesrecht | Nicht ausgeschlossen durch Landes- oder Bundesrecht? |
| 2 | Klagebefugnis analog | § 42 Abs. 2 VwGO | Adressat oder Drittbetroffener mit möglicher Rechtsverletzung |
| 3 | Widerspruchsfrist | § 70 Abs. 1 VwGO | 1 Monat ab Bekanntgabe; § 58 Abs. 2: 1 Jahr bei Belehrungsfehler |
| 4 | Form des Widerspruchs | § 70 Abs. 1 VwGO | Schriftlich, elektronisch oder zur Niederschrift |
| 5 | Zuständige Ausgangsbehörde | § 70 VwGO | Widerspruch an Behörde, die VA erlassen hat |
| 6 | Aufschiebende Wirkung | § 80 Abs. 1 VwGO | Besteht sie? Entfällt nach § 80 Abs. 2 VwGO? |
| 7 | Formelle Rechtmäßigkeit des VA | §§ 28, 39 VwVfG | Anhörung, Begründung, Zuständigkeit, Form |
| 8 | Heilbarkeit formeller Fehler | § 45 VwVfG | Nachholbarkeit bis Abschluss Widerspruchsverfahren; Gefahr der Heilung |
| 9 | Materielle Rechtmäßigkeit | Spezialgesetze + BGB/VwVfG | Tatbestand der Ermächtigungsgrundlage erfüllt? |
| 10 | Ermessen | §§ 40 VwVfG, 114 VwGO | Nichtgebrauch, Überschreitung, Fehlgebrauch |
| 11 | Verhältnismäßigkeit | Art. 20 GG | Geeignet, erforderlich, angemessen |
| 12 | Zweckmäßigkeit | § 68 VwGO | Widerspruchsverfahren prüft auch Zweckmäßigkeit — Ermessen vollständig überprüfbar |
| 13 | Widerspruchsbehörde zuständig | § 73 VwGO | Ober- oder Aufsichtsbehörde? Oder Ausgangsbehörde selbst? |
| 14 | Hinzuziehungsantrag | §§ 80 VwVfG, Landesrecht | Notwendigkeit des Bevollmächtigten; Kostenfolge |
| 15 | Eilrechtsschutz parallel | §§ 80 Abs. 4, 80 Abs. 5 VwGO | Antrag bei Behörde oder VG |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Rechtmäßigkeit des Verwaltungsakts | Behörde (trägt Beweislast für anspruchsbegründende Tatsachen) | Verwaltungsakte, Gutachten, Stellungnahmen |
| Fehlende Anhörung § 28 VwVfG | Widerspruchsführer (Rügeobliegenheit) | Akte, eigene Erklärung |
| Mangelhafte Begründung § 39 VwVfG | Widerspruchsführer (aus dem Bescheid ersichtlich) | Bescheid selbst |
| Ermessensfehler | Widerspruchsführer (Rüge) / Behörde (Entlastung) | Begründung des VA, Verwaltungsvorgang |
| Verhältnismäßigkeit | Widerspruchsführer (milderes Mittel behaupten) | Sachverständige, eigene Berechnung |
| Fristversäumnis bei falscher Belehrung | Behörde (muss ordnungsgemäße Belehrung nachweisen) | Zustellungsurkunde, Bescheid |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Widerspruchsfrist | § 70 Abs. 1 VwGO | 1 Monat ab Bekanntgabe | Bekanntgabe ≠ Zustellung; ggf. Dreitagesfiktion § 41 Abs. 2 VwVfG |
| Verlängerte Widerspruchsfrist | § 58 Abs. 2 VwGO | 1 Jahr bei fehlerhafter oder fehlender Belehrung | Gilt auch bei fehlendem Hinweis auf Adresse der Behörde |
| Klage nach Widerspruch | § 74 VwGO | 1 Monat ab Zustellung Widerspruchsbescheid | Bei Untätigkeit: 3 Monate nach Einlegung Widerspruch → Untätigkeitsklage § 75 VwGO |
| Untätigkeitsklage | § 75 VwGO | 3 Monate nach Einlegung Widerspruch | Bei Fristversäumnis kein Rechtsverlust, aber beachten |
| Heilung formeller Fehler | § 45 Abs. 2 VwVfG | Bis Abschluss letzter Tatsacheninstanz | Behörde kann Anhörung und Begründung nachreichen |
| Verjährung materieller Schadensersatz | § 195 BGB | 3 Jahre ab Kenntnis | Parallelansprüche aus § 839 BGB i.V.m. Art. 34 GG |

## Typische Gegenargumente

| Gegenargument der Behörde | Gegenstrategie |
|---|---|
| "Anhörungsmangel geheilt — Widerspruch ist Nachholung" | § 45 Abs. 1 Nr. 3 VwVfG: Heilung nur durch eigenständige, nicht nur pro forma erfolgte Anhörung; bloße Übersendung des Bescheids genügt nicht |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Widerspruchsverfahren ausgeschlossen" | Landespezifische Ausnahmen genau prüfen; bei Ausschluss nur in bestimmten Sachgebieten prüfen ob hier ein solches vorliegt |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch gegen Verwaltungsakt einlegen | Widerspruchsschrift nach Pruefschema; Template unten |
| Variante A — Widerspruchsverfahren nicht Pflicht direkter Klageweg | Klagefrist pruefen; ggf. direkt Anfechtungsklage ohne Widerspruch |
| Variante B — Mandant will Widerspruch nur zur Fristwahrung | Kurzwiderspruch ohne Begruendung zuerst; Begruendung nachreichen |
| Variante C — Behörde zeigt Kooperationsbereitschaft | Informelles Gespraech vor Widerspruch; Widerspruch als letzte Option |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Vollständige Widerspruchsschrift

```
[Kanzlei]
[Anschrift]
[Datum]

An die [Ausgangsbehörde]
[Anschrift]
Aktenzeichen der Behörde: [Az.]

Widerspruch nach § 68 VwGO

In der Verwaltungssache
des [Vorname Name]
[Anschrift]
— Widerspruchsführer —

Verfahrensbevollmächtigte: Rechtsanwältinnen und Rechtsanwälte [Kanzlei]

gegen

den Bescheid der [Behörde] vom [Datum], Aktenzeichen [Az.],
zugestellt am [Datum]

legen wir namens und in Vollmacht des Widerspruchsführers

Widerspruch

ein und beantragen:

1. Den Bescheid vom [Datum] aufzuheben.

2. [Hilfsweise: Bescheid mit folgendem Inhalt zu erlassen: ...]

3. Die Hinzuziehung des Bevollmächtigten für das Vorverfahren
 gemäß § 80 Abs. 2 VwVfG für notwendig zu erklären.

Begründung

I. Zulässigkeit
Der Widerspruch ist nach § 68 VwGO statthaft. Das
Widerspruchsverfahren ist im Land [X] im Sachgebiet [Y]
nicht ausgeschlossen. Der Bescheid wurde dem Widerspruchsführer
am [Datum] zugestellt. Die Widerspruchsfrist von einem Monat
(§ 70 Abs. 1 VwGO) ist daher bis zum [Datum] gewahrt.

II. Formelle Rechtswidrigkeit

1. Anhörungsmangel § 28 VwVfG
Vor Erlass des Bescheids wurde dem Widerspruchsführer keine
Gelegenheit zur Stellungnahme gegeben. Der Widerspruchsführer
hat zu keinem Zeitpunkt eine Anhörungsmitteilung erhalten.
Der Mangel ist beachtlich.

2. Begründungsmangel § 39 VwVfG
Der Bescheid enthält keine ausreichende rechtliche Begründung.
Die Behörde beschränkt sich auf den Hinweis, [Zitat]. Eine
Auseinandersetzung mit den konkreten Umständen des Einzelfalls
fehlt.

III. Materielle Rechtswidrigkeit

1. Tatbestand nicht erfüllt
Die Voraussetzungen des § [X Spezialgesetz] liegen nicht vor.
Die Behörde geht davon aus, dass [Sachverhaltsbehauptung Behörde].
Tatsächlich ist jedoch [zutreffender Sachverhalt]. Dies belegen
[Anlage X].

2. Ermessensfehler § 40 VwVfG / § 114 VwGO
Soweit der Bescheid auf Ermessen gestützt ist, wurde es nicht
oder fehlerhaft ausgeübt:
a) Ermessensnichtgebrauch: aus der Begründung ergibt sich, dass
 die Behörde keine Ermessenserwägungen angestellt hat.
b) Ermessensfehlgebrauch: relevante Belange wie [Belang] wurden
 nicht berücksichtigt.

3. Unverhältnismäßigkeit
Der Eingriff ist nicht verhältnismäßig:
— Geeignetheit: [ggf. bestreiten].
— Erforderlichkeit: Das mildere Mittel [Bezeichnung] wäre ebenso
 wirksam und weniger belastend.
— Angemessenheit: die Schwere des Eingriffs [Beschreibung] überwiegt
 das verfolgte Ziel.

IV. Eilrechtsschutz
Parallel hierzu wird beim Verwaltungsgericht [Ort] ein Antrag nach
§ 80 Abs. 5 VwGO eingereicht, da die sofortige Vollziehung die
[Existenz / wirtschaftliche Grundlage] des Widerspruchsführers
gefährdet.

Mit freundlichen kollegialen Grüßen

Anlagen:
- Bescheid (Anlage W1)
- Vollmacht (Anlage W2)
- Belege Sachverhalt (Anlagen W3 ff.)
```

### Baustein 2: Widerspruch mit Sofortvollzug-Antrag § 80 Abs. 4 VwGO

```
An die [Ausgangsbehörde]

Widerspruch und Antrag auf Aussetzung der sofortigen Vollziehung

I. Widerspruch
[wie Baustein 1]

II. Antrag nach § 80 Abs. 4 VwGO
Wir beantragen zugleich gemäß § 80 Abs. 4 VwGO, die Vollziehung
des angefochtenen Bescheids auszusetzen.

Die sofortige Vollziehung würde [konkrete Folgen schildern].
Angesichts der dargelegten erheblichen Erfolgsaussichten des
Widerspruchs und der schwerwiegenden Konsequenzen der sofortigen
Vollziehung überwiegt das Aussetzungsinteresse des
Widerspruchsführers.

Sollte die Behörde dem Antrag nicht innerhalb von [5] Werktagen
stattgeben, wird der Widerspruchsführer das Verwaltungsgericht
anrufen (§ 80 Abs. 5 VwGO).
```

### Baustein 3: Taktischer Hinweis-Schriftsatz bei drohender Heilung

```
An die [Ausgangsbehörde]

Stellungnahme zur nachgeholten Anhörung

Sehr geehrte Damen und Herren,

wir nehmen Stellung zu Ihrem Schreiben vom [Datum], mit dem Sie
nach Einlegung des Widerspruchs eine Anhörung nachgeholt haben.

1. Wir machen geltend, dass die nachgeholte Anhörung die formelle
 Rechtswidrigkeit des Bescheids im Kern nicht beseitigt, da
 [Begründung: z.B. Ermessenserwägungen grundlegend neu bewertet
 werden müssten / Sachverhalt nicht hinreichend aufgeklärt].

2. Wir halten an dem Widerspruch vollumfänglich fest.

3. Unabhängig von der Frage der Heilung bleibt der Bescheid aus
 den materiellen Gründen (s.o.) rechtswidrig.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Widerspruchsverfahren | § 52 GKG; Auffangwert EUR 5.000; bei beziffertem Anspruch der Anspruchsbetrag | Für Kostenerstattung aus § 80 VwVfG relevant |
| Gebühr Widerspruchsverfahren | Landesgebührenrecht; meist EUR 50–500 bei Abweisung; keine Gebühr bei Abhilfe | Wenn Widerspruch Erfolg hat: Erstattung der anwaltlichen Kosten |
| Hinzuziehungsantrag | § 80 VwVfG; notwendig wenn Sach- und Rechtslage komplex | Ohne Antrag kein Kostenerstattungsanspruch |
| Anwaltsvergütung | RVG Nr. 2300 VV (Geschäftsgebühr); 1,3 bis 2,5-fach je nach Schwierigkeit | Erstattungsfähig bei Obsiegen |
| Kosten Klageverfahren danach | GKG Anlage 1; plus RVG-Gebühren | Widerspruchsverfahren als Sachurteilsvoraussetzung unerlässlich |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Frist fast abgelaufen | Widerspruch ohne Begründung einlegen; Begründung nachreichen; Fristwahrung hat Vorrang |
| Anhörungsmangel erkannt | Rügen aber beachten: Behörde kann nachholen → eigene Einwendungen früh substanziieren |
| Sofortvollzug angeordnet | § 80 Abs. 4 VwGO-Antrag bei Behörde + § 80 Abs. 5 VwGO parallel VG |
| Ermessensfehler eindeutig | Substanziierte Rüge; keine allgemeine Formulierung; konkrete Erwägungen als fehlend bezeichnen |
| Widerspruchsverfahren ausgeschlossen | Unmittelbar Klage erheben; Frist § 74 VwGO einhalten |
| Chance auf Abhilfe hoch | Frühe Kontaktaufnahme mit Sachbearbeiter; einvernehmliche Lösung suchen; spart Kosten |

## Anschluss-Skills

- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Eilrechtsschutz parallel zum Widerspruch
- `eilantrag-80-abs-5-vwgo` — Vertiefung Schriftsatz § 80 Abs. 5 VwGO
- `energieanlagen-bimschg-genehmigung-verfahren` — Widerspruch gegen BImSchG-Bescheid
- `energietrassen-planfeststellung-rechtsschutz` — Einwendungen im Planfeststellungsverfahren

## Aktuelle Leitentscheidungen (v14.2 Ergaenzung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- VwGO §§ 42, 58, 68–79, 80, 113, 114
- VwVfG §§ 28, 35, 39, 40, 41, 43, 44, 45, 80
- GKG § 52
- RVG Nr. 2300 VV
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## 2. `mandat-triage-verwaltungsrecht`

**Fokus:** Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks. Normen: § 70 VwGO (Widerspruch 1 Monat), § 74 VwGO (Klage 1 Monat), § 75 VwGO (Untätigkeitsklage 3 Monate). Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht, Schule, Subventionen, Auslaender), Behördenebene, Verfahrensstand, Frist-Sofort-Check, Eskalation bei drohendem Vollzug. Output Triage-Protokoll mit Fristen-Ampel, Routing-Empfehlung. Abgrenzung: Detailprüfung siehe widerspruch-oder-klage-erstprüfung; Schriftsatz siehe schriftsatzkern-substantiierung.

# Mandat-Triage Verwaltungsrecht

## Zweck

Verwaltungsrecht ist hochheterogen — vom Bauantrag bis zur Asylklage. Triage ordnet das Mandat dem richtigen Sachgebiet und dem richtigen Verfahrensschritt zu.

## Ablauf — sieben Fragen

### Frage 1 — Wer und für wen?

- Bürger gegen Behörde
- Unternehmen gegen Behörde
- Behörde (selten — vertretbar nur unter strikter Trennung)
- Verband-Klagebefugnis

### Frage 2 — Sachgebiet?

- **Bau- und Planungsrecht** Baugenehmigung Nachbarklage Bebauungsplan
- **Gewerberecht** Gewerbeerlaubnis Untersagung Gaststätte Spielhalle
- **Polizei- und Ordnungsrecht** polizeiliche Maßnahme Versammlungsrecht
- **Beamten- und Soldatenrecht** Disziplinar Beurteilung Konkurrentenklage
- **Schule und Hochschule** Versetzung Abitur Zulassung
- **Subventionsrecht** Förderbescheid Rückforderung
- **Asyl- und Ausländerrecht** (an `fachanwalt-migrationsrecht` weiter)
- **Sozialrecht** (an `fachanwalt-sozialrecht` weiter)
- **Steuerrecht** (an `steuerrecht-anwalt-und-berater` weiter)
- **Vergaberecht** (an `fachanwalt-vergaberecht` weiter)
- **Umweltrecht**
- **Versammlungsrecht**
- **Kommunalrecht**

### Frage 3 — Akute Eilbedürftigkeit?

- Sofortige Vollziehung angeordnet
- Vollzug innerhalb Tage angekündigt
- Demonstrationsverbot ein-Tages-Vorlauf
- Räumung droht
- Untersagung erteilt — Geschäftsstillstand
- Bauleitplan-Aufstellung in der Beschlussphase

### Frage 4 — Stand?

- Vor Antragstellung (Beratung)
- Antrag eingereicht — wartet auf Bescheid
- Anhörung läuft § 28 VwVfG
- Bescheid liegt vor (Datum)
- Widerspruchsverfahren läuft
- Klage erhoben (Az VG)
- Berufung / Revision (OVG BVerwG)
- Verfassungsbeschwerde

### Frage 5 — Behörde?

- Bundesbehörde (z.B. BAMF Bundespolizei BfArM)
- Landesbehörde (z.B. Bezirksregierung Landratsamt)
- Kommunalbehörde
- Sondereinrichtung Anstalt öffentlichen Rechts

### Frage 6 — Frist?

- **Widerspruch** ein Monat § 70 VwGO; Bekanntgabe-Fiktion § 41 Abs. 2 VwVfG vier Tage seit 01.01.2025 (PostModG)
- **Klage** ein Monat § 74 VwGO ab Bekanntgabe Widerspruchsbescheid
- **Untätigkeitsklage** § 75 VwGO nach drei Monaten ohne Bescheid
- **Verfassungsbeschwerde** ein Monat § 93 BVerfGG
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr § 58 Abs. 2 VwGO

### Frage 7 — Wirtschaftliche Verhältnisse PKH?

- Prozesskostenhilfe § 166 VwGO iVm §§ 114 ff. ZPO
- Beratungshilfe für außergerichtlich

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Baugenehmigung Nachbarklage | (Skill bau-nachbarklage — perspektivisch) |
| Bauliche Untersagung | `widerspruch-oder-klage-erstpruefung` |
| Gewerbe-Erlaubnis-Streit | `widerspruch-oder-klage-erstpruefung` |
| Beamten-Konkurrentenklage | (Skill konkurrentenklage — perspektivisch) |
| Beurteilung Beamter | (Skill beurteilungsanfechtung — perspektivisch) |
| Schule Versetzung Zulassung | `widerspruch-oder-klage-erstpruefung` |
| Asyl Ausländerrecht | weiter an `mandat-triage-migrationsrecht` |
| Sozialleistung | weiter an `mandat-triage-sozialrecht` |
| Steuerrecht | weiter an `anw-mandat-triage-steuerrecht` |
| Polizei-Maßnahme | (Skill polizei-feststellungs-klage — perspektivisch) |
| Versammlungs-Verbot | `widerspruch-oder-klage-erstpruefung` plus § 80 Abs. 5 VwGO |

## Eilmodus

Bei sofortiger Vollziehung oder akutem Vollzug:

1. Mandantengespräch — Sachverhalt zwanzig Minuten
2. Bescheid einlesen — fünfzehn Minuten
3. Widerspruch einlegen (formloser Schriftsatz) — gleichzeitig
4. Eilantrag § 80 Abs. 5 VwGO oder § 123 VwGO formulieren
5. Bei VG einreichen — Eingang sicherstellen Empfangsbestätigung

## Eskalation

- **Telefon-Sofort** drohender Vollzug binnen Stunden
- **Binnen einer Stunde** Bescheid mit sofortiger Vollziehung
- **Heute** Widerspruchsschrift Eilantrag-Erstentwurf
- **Diese Woche** Klage-Erstentwurf Begründung

## Ausgabe

- `triage-protokoll-verwaltungsrecht.md`
- Frist im Fristenbuch
- Bei Eilmodus: Eilantrag-Entwurf im Anhang
- Mandatsvereinbarung mit Streitwertabschätzung § 52 GKG
- Empfehlung Folge-Skill

## Leitentscheidungen Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Quellen

- VwGO §§ 42 58 68 70 74 75 80 80a 123
- VwVfG §§ 28 35 41
- GKG § 52
- BVerwGE Std.Spruch
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## 3. `schriftsatzkern-substantiierung`

**Fokus:** Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspruch, Anfechtungsklage, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO. Normen: §§ 42 und 80 VwGO sowie §§ 28 und 48 VwVfG. Prüfraster: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. Output Schriftsatz-Geruest mit Klagepunkten und Begründungs-Bausteine. Abgrenzung: Fertige Klageschrift siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Vergabe-Schriftsatz siehe fachanwalt-vergaberecht-Plugin.

# Schriftsatzkern und Substantiierung im Allgemeines Verwaltungs- und Bauplanungsrecht

## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Schriftsatz im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht erstellt werden, typischerweise: Widerspruch, Anfechtungsklage VG, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO.
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

Der Substantiierungs-Kern; pro Anspruchsgrundlage in VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen).
2. **Mandantenseitige Tatsachenbehauptungen** mit Beweisangeboten.
3. **Gegnerisches Verhalten** mit Belegen (Schreiben, Aussage, Verhalten).
4. **Schaden/Folgen** bezifferbar (Hauptforderung, Nebenforderung, Zinsen, Folgekosten).

### D. Rechtliche Wuerdigung

Anspruchsaufbau klassisch:

1. **Anspruchsgrundlage** nennen (z.B. § X iVm § Y).
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal wird gegen den Tatsachenvortrag gespiegelt.
3. **Einwendungen** der Gegenseite vorwegnehmen und entkraeften.
4. **Rechtsprechungs-Verweise:** BAG/BGH/BVerfG/EuGH/BFH je nach Fachgebiet; bei Allgemeines Verwaltungs- und Bauplanungsrecht typischerweise die letzte hoechstrichterliche Linie zitieren.
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

## Substantiierungs-Fallen im Allgemeines Verwaltungs- und Bauplanungsrecht

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

- BVerfG, BGH, BAG, BFH, BVerwG, EuGH und die jeweils massgeblichen Fachsenate für Allgemeines Verwaltungs- und Bauplanungsrecht.
- VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG sowie Verordnungen/Richtlinien dazu.
- Aktuelle Reform- und Gesetzgebungslage einbeziehen.

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisangeboten, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht, EB).
4. **Streitwertskizze** (eigenes Memo, falls > 1 Anspruch).
5. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger?).

## Beispiel-Anspruchsgrundlagen im Allgemeines Verwaltungs- und Bauplanungsrecht

Drei haeufig gebrauchte Anspruchsgrundlagen aus VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG und ihre Substantiierungs-Anforderungen:

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

Typische Antraege in Allgemeines Verwaltungs- und Bauplanungsrecht (Widerspruch, Anfechtungsklage VG, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO):

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

- Bei Allgemeines Verwaltungs- und Bauplanungsrecht-typischen Streitfaellen oft notwendig (Bauwerk, IT-System, Anlagebewertung, medizinische Frage).
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
- 1.10.2026 / 1.10.2027 - ZVollstrDigitG-Aenderungen im Vollstreckungsbereich; in Allgemeines Verwaltungs- und Bauplanungsrecht ggf. spezifische ERV-Pflichten beachten.

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

## Leitentscheidungen Schriftsatz-Substantiierung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Tatsachen-Grundlage und Streitwertskizze.
- `vergleichsverhandlung-strategie` (im selben Plugin) für parallelen Vergleichsversuch (Gueteverhandlung, Mediation).
