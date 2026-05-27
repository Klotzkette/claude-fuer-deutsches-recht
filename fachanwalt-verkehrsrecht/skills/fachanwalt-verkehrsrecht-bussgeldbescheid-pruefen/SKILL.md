---
name: fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen
description: "Mandant hat OWi-Bussgeldbescheid erhalten und Anwalt prueft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjaehrung. Pruefraster: Form- und Verfahrensfehler Verjaehrung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren standardisiert/nicht-standardisiert Toleranzabzug Anhoerung § 55 OWiG Akteneinsicht Fahrverbot § 25 StVG Ausnahmen. Output: Bescheid-Pruefprotokoll und Einspruchsempfehlung. Abgrenzung zu bussgeld-einspruch-pruefen (Schnell-Triage) und fachanwalt-verkehrsrecht-fahrerlaubnis-entzug."
---

# Bußgeldbescheid prüfen

## Kaltstart-Rückfragen

1. Welche Tat liegt zugrunde — Geschwindigkeitsüberschreitung, Rotlichtverstoß, Abstandsverstoß, Handyverstoß, Alkohol § 24a StVG, Drogen?
2. Wann war die Tatzeit und wann wurde der Bußgeldbescheid zugestellt? Einspruchsfrist § 67 Abs. 1 OWiG zwei Wochen; Verjährungsprüfung § 26 Abs. 3 StVG drei Monate ab Tatzeit.
3. Welches Messverfahren wurde eingesetzt — Lasergerät, Radar, ProViDa, Section Control, ESO, PoliScan, TraffiStar? Liegt Eichschein und Schulungsnachweis des Bedieners vor?
4. Wurde der Mandant als Fahrer anhand des Lichtbilds identifiziert oder nur als Halter angeschrieben?
5. Ist ein Fahrverbot festgesetzt und besteht berufliche Härte (Existenzgefährdung)? Gibt es Voreintragungen im FAER?
6. Wurde eine Anhörung gemäß § 55 OWiG vor Bescheiderlass durchgeführt? Anhörungsbogen ausgefüllt?
7. Bestehen formelle Fehler im Bescheid — fehlerhafte Tatzeit, Tatort, Geschwindigkeit, Rechtsbehelfsbelehrung?
8. Liegt die Tat bereits nahe der Verjährungsgrenze (3 Monate Basis + Unterbrechungen nach § 33 OWiG)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 26 Abs. 3 StVG** — Verjährungsfrist drei Monate ab Tatzeit bei Ordnungswidrigkeiten im Straßenverkehr; nach Erlass des Bußgeldbescheids verlängerte Frist.
- **§ 33 OWiG** — Unterbrechungsgründe: Bekanntgabe Verfahrenseinleitung an Betroffenen; schriftliche Aufnahme Sachverhalt für Protokoll; Anordnung Auskunft über Betroffenen; Erlass Bußgeldbescheid; Einlegung Einspruch. Nach jeder Unterbrechung beginnt neue volle Frist.
- **§ 49 OWiG** — Akteneinsichtsrecht des Verteidigers; umfasst alle Verfahrensakten; Anspruch auf Herausgabe Mess-Rohdaten nach BVerfG 2 BvR 1167/20.
- **§ 55 OWiG** — Anhörungsrecht Betroffener; Verletzung kann zur Rechtswidrigkeit des Bußgeldbescheids führen; Heilung möglich wenn Betroffener im Einspruchsverfahren gehört wird.
- **§ 65 OWiG** — Bußgeldbescheid; Mindestinhalt: Personalien, Tatbeschreibung, Tatzeit, Tatort, angewandte Vorschriften, Bußgeldhöhe, Fahrverbot.
- **§ 67 Abs. 1 OWiG** — Einspruch innerhalb zwei Wochen nach Bekanntgabe; schriftlich oder zur Niederschrift bei erlassender Behörde.
- **§ 24a StVG** — Alkohol- und Drogenfahrt als OWi; 0,5 bis 1,09 Promille EUR 500, 2 Punkte, 1 Monat Fahrverbot; Drogen-Grenzwert nach Verordnung.
- **§ 25 StVG** — Fahrverbot; Regelfahrverbot nach BKatV; Wegfall bei atypischem Fall und erhöhter Geldbuße.
- **§ 25 Abs. 2a StVG** — Fahrverbotsbeginn frei wählbar bis 4 Monate nach Rechtskraft.
- **§ 4 Abs. 4 BKatV** — Absehen vom Fahrverbot bei Verhängung höherer Geldbuße.

### BGH und BVerfG-Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| BGH | 4 StR 627/92 (BGHSt 39, 291) | 19.08.1993 | Standardisiertes Messverfahren; Richtigkeitsvermutung; Toleranzabzug genügt |
| BVerfG | 2 BvR 1167/20 | 12.11.2020 | Anspruch auf Rohmessdaten für effektive Verteidigung; Verweigerung = Verwertungsverbot |
| OLG Zweibrücken | 1 OWi 2 SsBs 114/20 | 21.12.2020 | PoliScan FM1: Anerkennnung als standardisiertes Messverfahren trotz Softwarebesonderheiten |
| OLG Karlsruhe | 2 Rb 35 Ss 291/23 | 22.05.2023 | Rohmessdaten: konkrete Geltendmachung erforderlich; pauschaler Antrag unzureichend |
| BayObLG | 201 ObOWi 1296/22 | 20.01.2023 | Schulungsnachweis: fehlender Beleg führt nicht automatisch zur Unverwertbarkeit; Fehler muss kausal sein |

## Prüfschema in Tabellenform


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Verjährung geprüft? (3 Monate ab Tatzeit) | § 26 Abs. 3 StVG | Abgelaufen und keine Unterbrechung: Einstellung § 46 OWiG |
| 2 | Unterbrechungshandlungen belegt? | § 33 OWiG | Lücke in Unterbrechungskette → Verjährung |
| 3 | Einspruchsfrist gewahrt? (2 Wochen + 4-Tage-Fiktion) | § 67 OWiG; PostModG | Versäumt: Wiedereinsetzung § 52 OWiG prüfen |
| 4 | Anhörung ordnungsgemäß? | § 55 OWiG | Heilung im Einspruchsverfahren möglich |
| 5 | Mindestinhalt Bescheid vollständig § 65 OWiG? | § 65 OWiG | Fehlt wesentlicher Inhalt: Aufhebung rügbar |
| 6 | Fahreridentifizierung belegt? | Darlegungslast Behörde | Zweifelhaftes Lichtbild: Sachverständigen-Beweisangebot |
| 7 | Messverfahren standardisiert? | BGHSt 39, 291 | Nicht standardisiert: volle Beweislast Behörde |
| 8 | Eichschein gültig zur Tatzeit? | § 31 MessEG | Abgelaufen: Verwertungsverbot prüfen |
| 9 | Schulungsnachweis Bediener vorhanden? | Gerätebedienungsanleitung; BayObLG 201 ObOWi 1296/22 | Fehlt: Rüge; Kausalität darlegen |
| 10 | Rohmessdaten herausgegeben? | BVerfG 2 BvR 1167/20; OLG Karlsruhe 2 Rb 35 Ss 291/23 | Verweigert bei konkretem Antrag: Verwertungsverbot |
| 11 | Toleranzabzug korrekt vorgenommen? | BGHSt 39, 291; BKatV | Zu gering: Neuberechnung; ggf. anderes Tatbild |
| 12 | Bußgeld korrekt nach BKatV? | BKatV Anlage 1, 2 | Fehler: unmittelbare Rüge |
| 13 | Fahrverbot: Regelfall oder Atypik? | § 25 StVG; § 4 Abs. 4 BKatV | Härtefall: erhöhte Geldbuße statt Fahrverbot |
| 14 | § 25 Abs. 2a StVG-Aufschub genutzt? | § 25 Abs. 2a StVG | Bis 4 Monate nach Rechtskraft; Ferienzeit wählen |
| 15 | FAER-Punkte korrekt? Tilgungsfristen? | § 29 StVG | 2,5 Jahre Tilgung bei 1-2 Punkten |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Mandant will Bussgeldbescheid pruefen lassen | Formelle und materielle Pruefung; Schriftsatz unten |
| Variante A — Bescheid ohne Messfehler Akzeptanz guenstiger | Keine weiteren Massnahmen; Zahlung empfehlen |
| Variante B — Fahrverbot mit Haertefall Elternzeit Fernpendler | Einspruch nur wegen Fahrverbot; Geldbusse akzeptieren |
| Variante C — Standardisiertes Messverfahren fehlerhafte Geeichung | Einspruch mit technischer Ruege; Akte anfordern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Einspruch mit Akteneinsicht und Rohmessdaten-Antrag

```
An die [Bußgeldstelle]
[Adresse]
Aktenzeichen: [Az]

EINSPRUCH § 67 OWiG

In der Bußgeldsache gegen
[Name, Adresse, geb. Datum]

namens und in Vollmacht des Betroffenen lege ich gegen den
Bußgeldbescheid vom [Datum], zugestellt am [Datum],

                    EINSPRUCH

ein. Eine Begründung bleibt nach Akteneinsicht vorbehalten.

ANTRÄGE

1. Akteneinsicht § 49 OWiG

Ich beantrage vollständige Akteneinsicht einschließlich:
a) Sämtlicher Rohmessdaten des Falldatensatzes und der
   Falldatensätze der Messreihe (konkret: alle Einzelmessungen,
   Gerätedaten, Kalibrierungsprotokolle) — BVerfG 2 BvR 1167/20;
b) Eichschein des Messgeräts mit Gültigkeitsdauer zur Tatzeit;
c) Schulungsnachweis des messenden Beamten (Name, Gerätekurs);
d) Messprotokoll mit Aufstellungsort, -bedingungen und -dauer;
e) Betriebsanleitung des eingesetzten Geräts [Bezeichnung].

2. Aussetzung der Vollziehung des Fahrverbots
   bis zur rechtskräftigen Entscheidung, da berufliche Härte
   droht (Begründung nach Akteneinsicht).

Mit freundlichen Grüßen
[Rechtsanwalt]
```

### Baustein 2 — Begründung nach Akteneinsicht: Verjährung

```
Begründung des Einspruchs

I. Verjährung

Die Ordnungswidrigkeit vom [Tatdatum] ist verjährt.

Gemäß § 26 Abs. 3 StVG beträgt die Verjährungsfrist drei Monate
ab Tatzeit ([Tatdatum]).

Die Akte enthält folgende Unterbrechungshandlungen:
- Anhörungsbogen versandt am [Datum]
- Eingang Anhörungsbogen am [Datum] (Unterschrift des Mandanten)
- Bußgeldbescheid erlassen am [Datum]

Nach der Unterbrechung durch Absendung des Anhörungsbogens am
[Datum] begann die neue 3-Monats-Frist. Diese lief ab am [Datum +
3 Monate]. Der Bußgeldbescheid wurde am [Datum] erlassen, also
NACH Ablauf der Verjährungsfrist.

Die Ordnungswidrigkeit ist verjährt. Der Einspruch ist begründet.
Das Verfahren ist einzustellen.
```

### Baustein 3 — Begründung Messfehler / Rohmessdaten

```
II. Messung nicht verwertbar

Das eingesetzte Messgerät [Bezeichnung, Gerätenummer] misst nach
dem standardisierten Verfahren (BGHSt 39, 291). Allerdings sind
folgende Fehler zu verzeichnen:

1. Eichschein abgelaufen:
   Laut beigebrachtem Eichschein war das Gerät zuletzt am
   [Datum] geeicht. Die Eichgültigkeitsdauer beträgt nach
   § 32 MessEV 12 Monate. Die Tatzeit [Datum] liegt nach
   Ablauf der Eichgültigkeit. Das Messergebnis ist nicht
   verwertbar.

2. Rohmessdaten verweigert:
   Trotz konkretem Antrag vom [Datum] (Anlage K1) wurden die
   Rohmessdaten des Falldatensatzes nicht vorgelegt. Nach
   BVerfG 2 BvR 1167/20 begründet die Verweigerung ein
   Verwertungsverbot, wenn der Verteidiger konkret geltend
   macht, dass er ohne die Daten die Messung nicht überprüfen
   kann. Dieser Antrag liegt vor.

3. Sachverständigengutachten wird beantragt:
   Zum Nachweis der Unverwertbarkeit der Messung beantragen
   wir die Einholung eines Sachverständigengutachtens zur
   Frage, ob das eingesetzte Gerät am Tattag zuverlässige
   Messergebnisse liefern konnte.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Tatbestand, Schuld | Bußgeldstelle / Gericht |
| Fahreridentität | Bußgeldstelle; Halterschaft allein genügt nicht |
| Standardisiertes Messverfahren korrekt angewendet | Grundsatzvermutung BGHSt 39, 291; Verteidigung muss konkrete Fehler benennen |
| Verjährungsunterbrechung | Bußgeldstelle (Zugangsnachweise für Anhörung etc.) |
| Härtefall Fahrverbot | Betroffener (konkrete Existenzgefährdung) |
| Ordnungsgemäße Anhörung | Bußgeldstelle |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung OWi Straßenverkehr | 3 Monate ab Tatzeit | Tatzeit | § 26 Abs. 3 StVG |
| Verlängerte Verjährung nach Bußgeldbescheid | 6 Monate nach Rechtskraft | VerfH § 26 Abs. 3 StVG | |
| Einspruchsfrist | 2 Wochen (+ 4 Tage Zustellungsfiktion) | Zustellung | § 67 OWiG; PostModG |
| Wiedereinsetzung | 2 Wochen | Hindernis entfallen | § 52 OWiG |
| Fahrverbotsbeginn (Wahlrecht) | bis 4 Monate nach Rechtskraft | Rechtskraft | § 25 Abs. 2a StVG |
| Tilgung FAER | 2,5 / 5 / 10 Jahre | Rechtskraft | § 29 StVG |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Standardisiertes Verfahren — kein Fehler möglich | Konkrete Benennung: Eichablauf, fehlender Schulungsnachweis, Rohmessdaten-Verweigerung |
| Fahrerbild eindeutig | Sachverständigen-Lichtbildvergleich beantragen; Beweiswürdigung dem Gericht überlassen |
| Verjährung durch Anhörungsversand unterbrochen | Beweislast Bußgeldstelle für Zugangszeitpunkt; Versandtag ist nicht Zugangstag |
| Keine Anhörungspflichtverletzung — heilbar | Im Hauptverfahren Gelegenheit gegeben; aber: formelle Pflicht des Bescheids unberührt |
| Härtefall nicht beweisbar | Arbeitgeberbestätigung + Gehaltsnachweis + Routenplan + Bescheinigung ÖPNV-Unzumutbarkeit |

## Streitwert und Kosten

- Kein Kostenrisiko für Betroffenen bei Einspruch; Kosten bei Verurteilung nach OWiG-Gebührentabelle.
- Anwaltsgebühren: Nr. 5100 ff. VV RVG; Grundgebühr + Verfahrensgebühr + ggf. Terminsgebühr; gesamt ca. EUR 400–1500 nach Bußgeldhöhe.
- Sachverständigengutachten Messung: EUR 800–2500; bei Freispruch: Staatskasse trägt Kosten § 467 StPO i.V.m. § 46 OWiG.

## Strategische Empfehlung

- Bei klarer Messung ohne Fehler: Einspruch nur bezüglich Fahrverbot (§ 4 Abs. 4 BKatV); Geldbuße akzeptieren.
- Bei Identitätszweifel: Vollenspruch; Sachverständigen-Beweisangebot im Einspruch benennen.
- Bei Verjährungs-Verdacht: Fristberechnung exakt; Unterbrechungskette der Bußgeldstelle anfordern.
- Bei Messfehler-Verdacht: BVerfG-Antrag auf Rohmessdaten konkret formulieren; nach Verweigerung sofort Verwertungsverbot geltend machen.
- Bei Fahrverbot + Beruf: Immer § 4 Abs. 4 BKatV Antrag; Arbeitgeberbestätigung sofort einholen; § 25 Abs. 2a StVG-Aufschub erklären.

## Anschluss-Skills

- `bussgeld-einspruch-pruefen` — detailliertes Messverfahrens-Prüfschema
- `fachanwalt-verkehrsrecht-fahrerlaubnis-entzug` — bei Fahrerlaubnisfolgen
- `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` — Vorbereitung AG-Verhandlung

## Quellen

OWiG §§ 33, 46, 47, 49, 52, 55, 65, 67; StVG §§ 24, 24a, 25, 26, 29; BKatV; MessEG § 31; MessEV § 32; BGHSt 39, 291; BVerfG 2 BvR 1167/20; OLG Zweibrücken 1 OWi 2 SsBs 114/20; OLG Karlsruhe 2 Rb 35 Ss 291/23; BayObLG 201 ObOWi 1296/22; Burhoff Handbuch OWi-Verfahren 6. Aufl. 2022; KK-OWiG 6. Aufl. 2020.
