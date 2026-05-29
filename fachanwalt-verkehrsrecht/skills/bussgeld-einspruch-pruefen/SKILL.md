---
name: bussgeld-einspruch-pruefen
description: "Workflow-Skill zu bussgeld einspruch pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Bußgeldbescheid prüfen und Einspruch

## Zweck

Bußgeldbescheide haben oft Verteidigungspotenzial — Messfehler, Identitätszweifel, Verjährung, Härtefall-Argumentation beim Fahrverbot. Der Skill führt systematisch durch alle Prüfschritte vom Fristbeginn bis zur Verhandlungs-Strategie.

## Kaltstart-Rückfragen

1. Wann war die Tatzeit und wann wurde der Bußgeldbescheid zugestellt? Einspruchsfrist zwei Wochen ab Bekanntgabe § 67 OWiG; Vier-Tages-Zustellungsfiktion seit 01.01.2025 (PostModG, § 51 Abs. 1 OWiG i.V.m. § 4 Abs. 2 VwZG).
2. Welche Ordnungswidrigkeit liegt zugrunde — Geschwindigkeitsüberschreitung, Rotlichtverstoß, Abstand, Handy § 23 Abs. 1a StVO, Alkohol § 24a StVG?
3. Welches Messverfahren wurde eingesetzt — PoliScan, TraffiStar, Lidar, ProViDa, Section Control, Multanova, ESO? Liegt Eichschein vor?
4. Wurde der Mandant als Fahrer anhand des Lichtbilds eindeutig identifiziert, oder nur als Halter angeschrieben?
5. Ist ein Fahrverbot festgesetzt? Gibt es berufliche Abhängigkeit vom Führerschein (Außendienst, Pflege, Handwerk) — Härtefall § 4 Abs. 4 BKatV?
6. Gibt es Voreintragungen im Fahreignungsregister innerhalb der letzten 12 Monate, die eine Erhöhung des Bußgelds oder das Fahrverbot auslösen?
7. Wurde der Mandant vor Erlass des Bußgeldbescheids angehört § 55 OWiG? Wurde Anhörungsbogen ausgefüllt und eingesandt?
8. Bestehen formelle Fehler im Bescheid — falsche Tatzeit, falscher Tatort, falsche Geschwindigkeit, fehlerhafte Rechtsbehelfsbelehrung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 26 Abs. 3 StVG** — Verjährung drei Monate ab Tatzeit (bei Geschwindigkeitsüberschreitung etc.); Unterbrechung durch Anhörungsmaßnahmen § 33 OWiG.
- **§ 33 OWiG** — Unterbrechungsgründe: Bekanntgabe der Einleitung des Verfahrens, Erlass des Bußgeldbescheids; Klageerhebung; nach Unterbrechung neue volle Verjährungsfrist.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 55 OWiG** — Anhörung: Betroffener muss vor Erlass des Bußgeldbescheids Gelegenheit zur Stellungnahme erhalten; Verletzung kann zu Verfahrenshindernis führen.
- **§ 67 Abs. 1 OWiG** — Einspruch innerhalb zwei Wochen nach Bekanntgabe bei der erlassenden Behörde; schriftlich oder zur Niederschrift.
- **§ 52 OWiG** — Wiedereinsetzung in den vorigen Stand bei unverschuldetem Fristversäumnis; unverzüglicher Antrag.
- **§ 24 StVG** — Ordnungswidrigkeiten im Straßenverkehr; Bußgeldkatalogverordnung (BKatV) als Ausfüllung.
- **§ 24a StVG** — Fahren unter Einfluss berauschender Mittel; Cannabisgrenzwerte seit Legalisierung gesondert.
- **§ 25 StVG** — Fahrverbot; Regelfahrverbot bei Tatbeständen der Anlage 1 BKatV; Ermessen bei atypischem Fall.
- **§ 25 Abs. 2a StVG** — Aufschub des Fahrverbotseintritts auf bis zu vier Monate nach Rechtskraft; Wahlrecht Betroffener.
- **§ 4 Abs. 4 BKatV** — Wegfall Fahrverbot bei außergewöhnlicher Härte (Existenzgefährdung beruflich); Erhöhung Geldbuße auf bis zum Dreifachen.

### Messverfahren — Zulässigkeit und Fehlerquellen

| Messgerät | Typ | Toleranz | Bekannte Fehlerquellen | Status |
|---|---|---|---|---|
| PoliScan FM1 / Speed | Laserscan | 3 km/h bis 100; 3 % über 100 | Auswertungssoftware-Fehler in bestimmten Versionen | Standardisiert (OLG-Anerkennung erforderlich) |
| TraffiStar S350 | Radar | 3 km/h bis 100; 3 % über 100 | Falschidentifikationen bei Schattenmessung | Standardisiert |
| ES 3.0 / ESO | Radar | 3 km/h bis 100; 3 % über 100 | Witterungsempfindlichkeit | Standardisiert |
| Lidar-Messgeräte | Laser-Handgerät | 1 km/h bis 100; 1 % über 100 | Handhabungsfehler; schlechtes Lichtverhältnis | Standardisiert |
| Section Control | Streckenradar | 5 km/h | Fahrzeugtausch-Erkennungsprobleme | In DE ab 2024 in Betrieb |
| ProViDa 2000 | Video-Nachfahren | variabel | Abstandsberechnung fehleranfällig | Fallweise zu prüfen |
| Multanova 6F | Radar | 3 km/h bis 100; 3 % über 100 | Schlechter Einstel-lungsnachweis | Standardisiert |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Bußgeldkatalog-Übersicht (Auszug, Stand 2024)

| Verstoß | Bußgeld EUR | Punkte | Fahrverbot |
|---|---|---|---|
| Geschwindigkeit +16-20 km/h innerorts | 70 | 1 | — |
| Geschwindigkeit +21-25 km/h innerorts | 115 | 1 | — |
| Geschwindigkeit +31-40 km/h innerorts | 200 | 1 | 1 Monat |
| Geschwindigkeit +41-50 km/h innerorts | 320 | 2 | 1 Monat |
| Geschwindigkeit +51-60 km/h innerorts | 480 | 2 | 2 Monate |
| Einfacher Rotlichtverstoß (<1 Sek.) | 90 | 1 | — |
| Qualifizierter Rotlichtverstoß (≥1 Sek.) | 200 | 2 | 1 Monat |
| Abstandsverstoß <5/10 bei 130 km/h | 240–400 | 1–2 | 1–3 Monate |
| Handy am Steuer § 23 Abs. 1a StVO | 100 | 1 | — |
| Alkohol 0,5–1,09 Promille § 24a StVG | 500 | 2 | 1 Monat |

## Prüfschema in Tabellenform


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Einspruchsfrist gewahrt? (2 Wochen + 4-Tage-Zustellungsfiktion) | § 67 OWiG; PostModG § 4 Abs. 2 VwZG | Bei Versäumnis: Wiedereinsetzung § 52 OWiG prüfen |
| 2 | Verjährung eingetreten (3 Monate ab Tatzeit)? | § 26 Abs. 3 StVG; § 33 OWiG | Unterbrechungen prüfen; bei Ablauf: Einstellung § 46 OWiG |
| 3 | Anhörung ordnungsgemäß durchgeführt? | § 55 OWiG | Fehlt: formeller Fehler, ggf. Verwertungsverbot |
| 4 | Fahrer eindeutig identifiziert? | Darlegungslast Behörde | Lichtbild-Vergleich; bei Zweifeln: Sachverständiger |
| 5 | Messverfahren standardisiert? | BGHSt 39, 291 | Nicht standardisiert: volle Beweislast Behörde |
| 6 | Eichschein gültig zur Tatzeit? | § 31 MessEG | Abgelaufene Eichung: Beweisverwertungsverbot möglich |
| 7 | Schulungsnachweis Messbeamter vorhanden? | Gerätebedienungsanleitung | Fehlt: Fehler im Messverfahren rügbar |
| 8 | Toleranzabzug korrekt vorgenommen? | BGHSt 39, 291 | Zu geringe Toleranz: Abzug erhöhen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 10 | Bußgeld-Höhe und Punkte korrekt nach BKatV? | BKatV Anlage 1, 2 | Fehler: unmittelbare Rüge |
| 11 | Fahrverbot regelkonform angeordnet? | § 25 StVG; BKatV | Kein Regelfall → Ermessen AG prüfen |
| 12 | Härtefall Fahrverbot darlegbar? | § 4 Abs. 4 BKatV | Existenzgefährdung → Ersatz durch erhöhte Geldbuße |
| 13 | § 25 Abs. 2a StVG-Wahlrecht bekannt? | § 25 Abs. 2a StVG | Aufschub bis 4 Monate nach Rechtskraft wählbar |
| 14 | Punkte im FAER korrekt — Tilgungsfristen? | § 29 StVG | 2,5 Jahre ab Rechtskraft bei 1-2 Punkten |
| 15 | Verfahrenseinstellung § 47 OWiG möglich? | § 47 OWiG | Behörde / Gericht kann bei geringem öffentlichen Interesse einstellen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Mandant will Einspruch gegen Bussgeldbescheid pruefend | Pruefung auf Formfehler + Einspruchsschriftsatz; Template unten |
| Variante A — Bussgeldbescheid akzeptieren guenstiger als Prozess | Keine weiteren Schritte; Bussgeldbescheid akzeptieren |
| Variante B — Fahrverbot droht Haertefall moeglich | Haertefall-Argumentation vorbereiten; Absehen vom Fahrverbot beantragen |
| Variante C — Messverfahren angreifbar Sachverstaendiger sinnvoll | Einspruch + Antrag auf Sachverstaendigen-Gutachten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Einspruch mit Akteneinsichtsantrag

```
An die [Bußgeldstelle]
[Adresse]
Aktenzeichen: [Az]

EINSPRUCH § 67 OWiG

In der Bußgeldsache gegen
[Name], [Adresse], geb. [Datum]

Sehr geehrte Damen und Herren,

namens und in Vollmacht des Betroffenen lege ich gegen den
Bußgeldbescheid vom [Datum], zugestellt am [Datum], hiermit

                    EINSPRUCH

ein.

Auf den Einspruch wird zunächst nicht näher eingegangen; dies
bleibt nach Akteneinsicht vorbehalten.

ANTRÄGE

1. Vollständige Akteneinsicht gemäß § 49 OWiG wird beantragt,
   einschließlich:
   a) Messprotokoll und vollständige Falldatensätze (alle
      Rohmessdaten, nicht nur das Tatfoto), gemäß BVerfG,
      Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
   b) Eichschein des eingesetzten Messgeräts, gültig zur Tatzeit;
   c) Schulungsnachweis des messenden Beamten (Bedienerlaubnis
      für das konkrete Gerät);
   d) Lebensakte des Messgeräts soweit vorhanden;
   e) Aufstellungsprotokolle und Messbedingungen.

2. Aussetzung der Vollziehung des Fahrverbots bis zur
   rechtskräftigen Entscheidung, da berufliche Härte besteht
   (Begründung folgt nach Akteneinsicht).

Mit freundlichen Grüßen
[Rechtsanwalt]
```

### Baustein 2 — Begründung Einspruch nach Akteneinsicht (Messverfahren)

```
Begründung des Einspruchs

I. Sachverhalt

Dem Betroffenen wird vorgeworfen, am [Datum] gegen [Uhrzeit]
auf der [Straße] in [Ort] die zulässige Höchstgeschwindigkeit
von [X] km/h um [Y] km/h überschritten zu haben (nach Toleranz-
abzug). Als Messgerät wurde [Gerätebezeichnung] eingesetzt.

II. Messung nicht verwertbar

1. Eichschein: Die Eichgültigkeit des Messgeräts ist nicht
   durch den vorgelegten Eichschein belegt. [Entweder: Eichschein
   liegt nicht in der Akte / war zur Tatzeit abgelaufen — Anlage K1.]
   Ohne gültigen Eichschein § 31 MessEG fehlt die Grundlage für
   eine verwertbare Messung.

2. Schulungsnachweis: Ein Schulungsnachweis des Bedieners [Name]
   für das konkrete Gerät [Bezeichnung] liegt nicht in der Akte.
   Nach der Bedienungsanleitung des Herstellers ist eine
   gerätetyp-spezifische Ausbildung Voraussetzung für den Einsatz.

3. Rohmessdaten: Trotz Akteneinsichtsantrags wurden die Rohmess-
   daten des Falldatensatzes nicht vorgelegt. Nach BVerfG
   Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
   eine effektive Verteidigung notwendigen Mess-Rohdaten zu
   erhalten. Die Verweigerung der Herausgabe begründet ein
   Beweisverwertungsverbot.

III. Nicht Fahrer

[Alternativ, bei Identitätszweifel:]
Das dem Bußgeldbescheid beigefügte Lichtbild zeigt eine
Person, die mit dem Betroffenen nicht hinreichend sicher
identifizierbar ist. Die Behörde trägt die Beweislast für
die Fahreridentität; ein pauschaler Verweis auf Halterschaft
genügt nicht. Es wird angeregt, einen Sachverständigen für
Fahrzeugidentifikation (Lichtbild-Gutachter) zu bestellen.

IV. Ergebnis

Der Einspruch ist begründet. Der Bußgeldbescheid ist aufzuheben.

[Rechtsanwalt]
```

### Baustein 3 — Härtefall-Argumentation Fahrverbot

```
ANTRAG AUF ABSEHEN VOM FAHRVERBOT § 4 Abs. 4 BKatV

Der Betroffene ist als [Außendienstmitarbeiter / Handwerker /
Pflegedienstmitarbeiter / Selbstständiger] beruflich zwingend
auf seine Fahrerlaubnis angewiesen. Im Einzelnen:

1. Berufliche Abhängigkeit
   [Konkrete Darstellung: täglich [X] km dienstlich zurückgelegt;
   kein funktionierender öffentlicher Nahverkehr; Arbeitgeber-
   bestätigung Anlage K1; Fahrten zu [X] Kunden/Patienten täglich]

2. Existenzgefährdung
   Ein Fahrverbot von [X] Monat/en würde zur Kündigung des
   Arbeitsverhältnisses / zum Verlust wesentlicher Aufträge
   führen (Arbeitgeberbestätigung Anlage K2).

3. Unzumutbarkeit
   Eine Vertretung durch Kollegen ist nicht möglich, da [Gründe].
   Die Inanspruchnahme von Taxis oder Mietwagen ist weder
   wirtschaftlich tragbar noch betrieblich umsetzbar.

4. Geringes Verschulden
   Es handelt sich um einen Erstverstoß ohne Voreintragungen
   im Fahreignungsregister. Der Verstoß lag lediglich [X km/h]
   über dem Regelwert für ein Fahrverbot.

Es wird beantragt, vom Fahrverbot abzusehen und stattdessen
die Geldbuße gemäß § 4 Abs. 4 BKatV auf das Dreifache
[EUR X] zu erhöhen.
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
| Fahreridentität | Bußgeldbehörde / Staatsanwaltschaft |
| Messgenauigkeit bei standardisiertem Verfahren | Behörde legt Protokoll vor; Verteidigung muss konkrete Fehler behaupten |
| Verjährung, Unterbrechung | Behörde muss Unterbrechungshandlung belegen |
| Anhörung ordnungsgemäß | Behörde |
| Härtfall Fahrverbot | Betroffener |
| Fahreignungsregister-Eintrag korrekt | Kraftfahrt-Bundesamt |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Verjährung Ordnungswidrigkeit | 3 Monate ab Tatzeit | Tatzeit | § 26 Abs. 3 StVG |
| Verjährungsunterbrechung | neue Verjährung beginnt | Unterbrechungshandlung | § 33 OWiG |
| Einspruchsfrist | 2 Wochen | Zustellung (+ 4 Tage Fiktion) | § 67 OWiG; PostModG |
| Wiedereinsetzungsfrist | 2 Wochen | Hindernis entfallen | § 52 OWiG |
| Fahrverbotsaufschub | bis 4 Monate nach Rechtskraft | Rechtskraft | § 25 Abs. 2a StVG |
| Tilgung FAER (1-2 Punkte) | 2,5 Jahre | Rechtskraft | § 29 Abs. 1 Nr. 2 StVG |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Standardisiertes Messverfahren — keine Fehler | Konkret benennen: Eichschein fehlt / abgelaufen; Schulungsnachweis fehlt; Rohmessdaten verweigert |
| Lichtbild ausreichend identifizierbar | Sachverständigen-Beweisangebot für forensischen Lichtbildvergleich |
| Härtefall nicht glaubhaft | Arbeitgeberbestätigung + Routenplan + Lohnabrechnung = Existenzgefährdung belegt |
| Verjährung durch Anhörung unterbrochen | Anhörungsschreiben auf Zugang prüfen; war Mandant tatsächlich Adressat? |
| Vorige Eintragung im FAER erhöht Bußgeld | Tilgungsfrist prüfen (§ 29 StVG); wenn Tilgung bereits eingetreten: keine Erhöhung |

## Streitwert und Kosten

- OWiG-Verfahren: keine Gerichtsgebühren bei Einspruch bis Hauptverhandlung; bei Hauptverhandlung Gerichtsgebühren nach KV OWiG.
- Anwaltskosten: Grundgebühr Nr. 4100 VV RVG + Verfahrensgebühr + Terminsgebühr; in Summe ca. EUR 500–1500 bei normalem Bußgeldverfahren.
- Sachverständigenkosten Lichtbildgutachten: EUR 800–2000; bei Freispruch von Staatskasse erstattet.
- Erfolg Härtefall: Mehrkosten Geldbuße (bis 3-fach); im Gegenzug kein Fahrverbot (Gehaltsausfall verhindert).

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Klare Messung, Toleranz korrekt, keine Fehler | Auf Einspruch verzichten oder beschränkt einlegen (nur Fahrverbot); Geldbuße ist günstiger als Hauptverhandlungsrisiko |
| Identifikation zweifelhaft | Einspruch; Akteneinsicht; Lichtbild-SV anbieten |
| Messverfahren-Fehler erkennbar | Voll einlegen; SV-Gutachten beauftragen |
| Fahrverbot — Berufsfahrer | Immer Härtefall-Antrag; Arbeitgeberbestätigung sofort einholen |
| Verjährung nähert sich | Einspruch einlegen; Hemmung durch Einspruch klären |

## Anschluss-Skills

- `fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen` — zweites Prüfschema (Verfahrensdetails)
- `fachanwalt-verkehrsrecht-fahrerlaubnis-entzug` — bei Fahrerlaubnisproblemen
- `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` — Vorbereitung Amtsgerichtsverhandlung

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
