---
name: vkr-bussgeldverfahren-bussgeld-einspruch
description: "VKR Bussgeldverfahren Bussgeld Einspruch im Plugin Fachanwalt Verkehrsrecht: prüft konkret Bussgeldverfahren Grundzuege, Prüfungslinie für bussgeld einspruch pruefen, Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# VKR Bussgeldverfahren Bussgeld Einspruch

## Arbeitsbereich

**VKR Bussgeldverfahren Bussgeld Einspruch** ordnet den Fall über die tragenden Prüfungslinien: Bussgeldverfahren Grundzuege, Prüfungslinie für bussgeld einspruch pruefen, Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `vkr-bussgeldverfahren-grundzuege` | Bussgeldverfahren Grundzuege: Anhörungsbogen, Einspruch innerhalb 2 Wochen, Hauptverhandlung Amtsgericht, Rechtsbeschwerde OLG nach §§ 79 ff. OWiG. Strategien Verteidigung, Punkterabatt bei Punkteabbau-Seminar. Pruefraster. |
| `bussgeld-einspruch-pruefen` | Prüfungslinie für bussgeld einspruch pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen` | Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verjährung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren standardisiert/nicht-standardisiert Toleranzabzug Anhörung § 55 OWiG Akteneinsicht Fahrverbot § 25 StVG Ausnahmen. Output: Bescheid-Prüfprotokoll und Einspruchsempfehlung. Abgrenzung zu bußgeld-einspruch-prüfen (Schnell-Triage) und fachanwalt-verkehrsrecht-fahrerlaubnis-entzug. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StVG; PflVG; §§ 315c 316 StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `vkr-bussgeldverfahren-grundzuege`

**Fokus:** Bussgeldverfahren Grundzuege: Anhörungsbogen, Einspruch innerhalb 2 Wochen, Hauptverhandlung Amtsgericht, Rechtsbeschwerde OLG nach §§ 79 ff. OWiG. Strategien Verteidigung, Punkterabatt bei Punkteabbau-Seminar. Pruefraster.

# Verkehrsrecht: Bussgeldverfahren

## Spezialwissen: Verkehrsrecht: Bussgeldverfahren
- **Normen-/Quellenanker:** OLG, OWiG.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behördenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `bussgeld-einspruch-pruefen`

**Fokus:** Prüfungslinie für bussgeld einspruch pruefen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

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
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

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

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

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
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

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

## 3. `fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen`

**Fokus:** Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verjährung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren standardisiert/nicht-standardisiert Toleranzabzug Anhörung § 55 OWiG Akteneinsicht Fahrverbot § 25 StVG Ausnahmen. Output: Bescheid-Prüfprotokoll und Einspruchsempfehlung. Abgrenzung zu bußgeld-einspruch-prüfen (Schnell-Triage) und fachanwalt-verkehrsrecht-fahrerlaubnis-entzug.

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
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 26 Abs. 3 StVG** — Verjährungsfrist drei Monate ab Tatzeit bei Ordnungswidrigkeiten im Straßenverkehr; nach Erlass des Bußgeldbescheids verlängerte Frist.
- **§ 33 OWiG** — Unterbrechungsgründe: Bekanntgabe Verfahrenseinleitung an Betroffenen; schriftliche Aufnahme Sachverhalt für Protokoll; Anordnung Auskunft über Betroffenen; Erlass Bußgeldbescheid; Einlegung Einspruch. Nach jeder Unterbrechung beginnt neue volle Frist.
- Volltext-Verifikation: Rspr. zu § 33 OWiG (Unterbrechungswirkung) und zu standardisierten Messverfahren in BGH-eigener Datenbank, dejure.org oder openjur.de aufrufen; nicht aus Modellwissen zitieren.
- **§ 55 OWiG** — Anhörungsrecht Betroffener; Verletzung kann zur Rechtswidrigkeit des Bußgeldbescheids führen; Heilung möglich wenn Betroffener im Einspruchsverfahren gehört wird.
- **§ 65 OWiG** — Bußgeldbescheid; Mindestinhalt: Personalien, Tatbeschreibung, Tatzeit, Tatort, angewandte Vorschriften, Bußgeldhöhe, Fahrverbot.
- **§ 67 Abs. 1 OWiG** — Einspruch innerhalb zwei Wochen nach Bekanntgabe; schriftlich oder zur Niederschrift bei erlassender Behörde.
- **§ 24a StVG** — Alkohol- und Drogenfahrt als OWi; 0,5 bis 1,09 Promille EUR 500, 2 Punkte, 1 Monat Fahrverbot; Drogen-Grenzwert nach Verordnung.
- **§ 25 StVG** — Fahrverbot; Regelfahrverbot nach BKatV; Wegfall bei atypischem Fall und erhöhter Geldbuße.
- **§ 25 Abs. 2a StVG** — Fahrverbotsbeginn frei wählbar bis 4 Monate nach Rechtskraft.
- **§ 4 Abs. 4 BKatV** — Absehen vom Fahrverbot bei Verhängung höherer Geldbuße.

### BGH und BVerfG-Leitentscheidungen (Stand Mai 2026; offene Quellen)

| Gericht | Aktenzeichen | Datum | Kernaussage | Offene Quelle |
|---|---|---|---|---|
| BVerfG | 2 BvR 1167/20 | 20.6.2023 | Standardisierte Geschwindigkeitsmessung; keine Pflicht zur Speicherung von Rohmessdaten; Recht auf erweiterten Informationszugang im Einzelfall | bundesverfassungsgericht.de |
| BVerfG | 2 BvR 1616/18 | 12.11.2020 | Informationszugang OWi-Verfahren; Akteneinsicht in Messunterlagen | bundesverfassungsgericht.de |
| BVerwG | 3 B 2.24 | 8.1.2025 | KCanG ab 1.4.2024: Cannabis ist kein BtM mehr; § 14 FeV neu zu lesen | bverwg.de |

Hinweis: BGH (4. Strafsenat) zu Geschwindigkeitsmessverfahren ist standardisiert anerkannt; konkrete Mess-Fehler im Einzelfall müssen substantiiert vorgetragen werden. Aktenzeichen vor Versand in BGH-eigener Datenbank, dejure.org oder openjur.de verifizieren.

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

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
| 9 | Recht auf Akteneinsicht in Rohmessdaten geltend gemacht? | Art. 103 GG; BVerfG 2 BvR 1616/18 (12.11.2020), BVerfG 2 BvR 1167/20 (20.6.2023) | Antrag schriftlich; keine pauschale Speicherungspflicht, aber Anspruch auf vorhandene Daten |
| 10 | Cannabis-Beteiligung? | § 24a StVG, KCanG (seit 1.4.2024); BVerwG 3 B 2.24 (8.1.2025) | THC-Grenzwert 3.5 ng/ml im Serum (§ 24a Abs. 1a StVG seit 22.8.2024) |
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
 sofern vom Gerät gespeichert; vgl. BVerfG, Beschl. v. 12.11.2020,
 2 BvR 1616/18; BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20 — kein
 Anspruch auf nicht gespeicherte Daten, aber Anspruch auf alle
 vorhandenen Daten);
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
 Rohmessdaten des Falldatensatzes nicht vorgelegt. Nach der
 Rechtsprechung des BVerfG (Beschl. v. 12.11.2020, 2 BvR 1616/18;
 Beschl. v. 20.6.2023, 2 BvR 1167/20) hat der Betroffene einen
 Anspruch auf Zugang zu den vorhandenen Messdaten und
 Begleitunterlagen; jedenfalls bei konkret dargelegtem
 Aufklärungsbedarf greift ein Verwertungsverbot, wenn die
 Verteidigung nachvollziehbar darlegt, dass sie ohne diese
 Daten die Messung nicht überprüfen kann.
 (Volltext der Beschlüsse vor Versand in
 bundesverfassungsgericht.de aufrufen und Randnummern
 ergänzen.)

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
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

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

Verbindlich `references/zitierweise.md`. Erlaubte offene Quellen: bundesverfassungsgericht.de, bundesgerichtshof.de (juris.bundesgerichtshof.de), bverwg.de, dejure.org, openjur.de, BGBl. Beck-RS und juris-Fundstellen ohne offene Quelle sind nicht zu zitieren.

Aktueller Stand Mai 2026 (verifizierte Aktenzeichen):
- BVerfG, Beschl. v. 12.11.2020, 2 BvR 1616/18 — Akteneinsicht / Informationszugang OWi
- BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20 — Keine Rohmessdaten-Speicherungspflicht; aber Anspruch auf vorhandene Daten
- BVerwG, Beschl. v. 8.1.2025, 3 B 2.24 — Cannabis und KCanG ab 1.4.2024
- KCanG vom 27.3.2024, BGBl. I 2024 Nr. 109; § 24a Abs. 1a StVG i. d. F. vom 21.8.2024, BGBl. I 2024 Nr. 274 (3.5 ng/ml THC-Grenzwert)
