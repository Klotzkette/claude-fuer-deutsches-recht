---
name: output-antrag-beschwerde-klageschrift
description: "Erzeugt Tenor-Bausteine, Rubrum und formale Mindestanforderungen für Antrag, Beschwerde und Klageschrift nach ZPO, VwGO, SGG, FGO und BVerfGG. Gibt Pflichtangaben, Fristen und Einreichungshinweise. Kein anwaltlicher Schriftsatz ohne anwaltliche Prüfung."
---

# Output: Antrag, Beschwerde, Klageschrift

## Zweck

Dieser Skill erzeugt formale Dokument-Bausteine für Anträge, Beschwerden und Klageschriften bei deutschen Gerichten und Behörden. Er gibt Rubrum, Tenor und die formalen Mindestanforderungen vor, die nach der jeweiligen Verfahrensordnung zwingend sind. Das Ergebnis ist ein Entwurf.

## Klageschrift nach ZPO (§ 253 ZPO)

### Pflichtinhalt (§ 253 Abs. 2 ZPO)

1. **Rubrum:** Bezeichnung der Parteien (vollständiger Name, Anschrift), gesetzliche Vertreter, Prozessbevollmächtigte
2. **Gericht:** Zuständiges Gericht (Amtsgericht oder Landgericht nach Streitwert § 23 / § 71 GVG; örtliche Zuständigkeit §§ 12 ff. ZPO)
3. **Bestimmter Klageantrag** (§ 253 Abs. 2 Nr. 2 ZPO): vollstreckungsfähig formuliert
4. **Klagebegründung:** Sachverhalt, Anspruchsgrundlage, Beweisangebote

### Tenor-Bausteine

**Zahlungsklage:**
"Der Beklagte wird verurteilt, an den Kläger EUR [Betrag] nebst Zinsen in Höhe von 5 Prozent über dem jeweils gültigen Basiszinssatz seit dem [Datum] zu zahlen."

**Unterlassungsklage:**
"Der Beklagte wird verurteilt, es zu unterlassen, [genaue Handlung zu beschreiben]. Für jeden Fall der Zuwiderhandlung wird dem Beklagten ein Ordnungsgeld bis zu EUR 250000, ersatzweise Ordnungshaft bis zu sechs Monaten, angedroht."

**Feststellungsklage:**
"Es wird festgestellt, dass zwischen den Parteien ein [Rechtsverhältnis] besteht / nicht besteht."

## Verwaltungsgerichtliche Klage (VwGO)

### Anfechtungsklage (§ 42 Abs. 1 Alt. 1 VwGO)

**Pflichtinhalt:**
- Bezeichnung des angefochtenen Verwaltungsakts (Bescheid mit Datum und Aktenzeichen)
- Widerspruchsbescheid (soweit erforderlich)
- Klagefrist: 1 Monat nach Zustellung des Widerspruchsbescheids (§ 74 Abs. 1 VwGO)

**Tenor:** "Der Bescheid des [Behörde] vom [Datum], Az. [X], und der Widerspruchsbescheid vom [Datum] werden aufgehoben."

### Verpflichtungsklage (§ 42 Abs. 1 Alt. 2 VwGO)

**Tenor:** "Der Beklagte wird verpflichtet, dem Kläger [Verwaltungsakt] zu erteilen / zu bewilligen."

## Beschwerde an das BVerfG (§ 90 BVerfGG)

**Formale Mindestanforderungen:**
- Beschwerdebefugnis: Grundrechtsträger, unmittelbar und gegenwärtig betroffen
- Beschwerdegegner: Öffentliche Gewalt (Gesetz, Gerichtsentscheidung, VA)
- Rechtswegerschöpfung (§ 90 Abs. 2 S. 1 BVerfGG): alle Rechtsmittel ausgeschöpft
- Frist: 1 Monat nach Zustellung der letztinstanzlichen Entscheidung (§ 93 Abs. 1 BVerfGG)
- Gerügtes Grundrecht mit Artikel benennen
- Substantiierte Begründung der Grundrechtsverletzung

## Widerspruch (VwGO / SGB)

**Frist:** 1 Monat ab Bekanntgabe des Verwaltungsakts (§ 70 VwGO; § 84 SGG).

**Form:** Schriftlich oder zur Niederschrift bei der Behörde. Keine besondere Form sonst.

**Mindestinhalt:** Bezeichnung des Bescheids, Erklärung des Widerspruchs, Begründung (empfohlen, nicht zwingend).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Formale Dokumentbausteine generieren fuer Antrag Beschwerde oder Klageschrift | Ausgabe nach Schema; Bausteine unten |
| Variante A — Nur Tenor-Baustein noetig kein vollstaendiges Dokument | Nur Tenor generieren; Sachverhalt und Begruendung separat |
| Variante B — Verwaltungsrecht statt Zivilrecht andere Anforderungen | VwGO-Variante des Templates verwenden |
| Variante C — Dokument soll durch KI-Kennzeichnungspflicht versehen werden | Kennzeichnungs-Skill parallel; Baustein erganzen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Ausgabe

Das System erzeugt:
- Vollständiges Rubrum
- Antrag / Tenor (vollstreckungsfähig)
- Begründungsentwurf nach Vier-Schritt-Schema
- Beweismittelverzeichnis
- Hinweis auf Einreichungsfristen und -stellen

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

