---
name: 06-anspruchstriage-fallstrategie
description: "Zentrale Weiche nach vorhandenem Fallkern. Wählt Anspruchsspur und wirtschaftliche Strategie, zeigt Stopps und nennt genau einen nächsten Skill. Fehlende Einzeldaten lösen nur den dafür zuständigen Fachskill aus."
---

# Anspruchstriage und Fallstrategie

## Zweck und Anwendungsfall

Dieser Skill ist die zentrale Weiche des Plugins: Er nimmt Kaufakte, Chronologie und Betroffenheitsbefund und entscheidet, welche Anspruchsgrundlage trägt, welche Strategie wirtschaftlich vernünftig ist und welcher Skill als nächstes arbeitet. Er bündelt Anspruchslinie, Verjährungs- und Kostenrisiko, Prozessfinanzierung und Vergleichsbereitschaft — und rät ehrlich ab, wenn der Fall nicht trägt.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst die Anspruchs- und Strategieweiche mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei weichenrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Anspruchsspuren oder wiederkehrenden Feldern, sonst vollständige Absätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort liefert sofort eine vorläufige, aber vollständig ausformulierte Anspruchstriage und Strategiekarte: tragende Spur, Ampelgrund, stärkstes Gegenargument, wirtschaftliche Wirkung und genau ein nächster Schritt. Ab mindestens drei ernsthaft konkurrierenden Anspruchsspuren werden sie tabellarisch verglichen; bei ein oder zwei Spuren genügen getrennte vollständige Absätze. Fehlende Kernstücke erscheinen als präzise Lücken mit Beschaffungsweg und Auswirkung auf Freigabe oder Abraten, nie als leere Platzhalterzeile. Verboten sind Theorie-Vorträge, Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen. Werkzeuge sind Beschleuniger: Bei Ausfall ohne Meldungslärm manuell weiterarbeiten; ein Werkzeugfehler blockiert nie die Triage.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Kaufakte (Skill 01), Belegmatrix (Skill 02), Chronologie (Skill 03).
- Betroffenheitsmatrix (Skill 04) und Einordnungsbefund (Skill 05), soweit vorhanden; sonst vorläufige Angaben.
- Rolle und Ziel der anfragenden Person: Geld zurück und Fahrzeug behalten, Rückabwicklung, nur Prüfung.

## Ablauf / Checkliste

1. Anspruchsgrundlage einordnen:

| Befund | Anspruchsgrundlage | Rechtsfolge | Nächster Skill |
|---|---|---|---|
| Prüfstandserkennung (z. B. EA189) | § 826 BGB i.V.m. § 31 BGB | Großer Schadensersatz, Rückabwicklung Zug um Zug | 08 dann 14 |
| Fahrzeugbezogen belegtes, objektiv unzulässiges Thermofenster | § 823 Abs. 2 BGB i.V.m. § 6 Abs. 1, § 27 Abs. 1 EG-FGV | Differenzschaden 5 bis 15 Prozent vor Vorteilsausgleich | 08; nur nach Freigabe 15 |
| EA288 mit fahrzeugbezogen belegter Einrichtungsspur (Thermofenster, Fahrkurve, Druck/Höhe) | § 823 Abs. 2 BGB i.V.m. § 6 Abs. 1, § 27 Abs. 1 EG-FGV; § 826 BGB nur bei Vorsatzspur | Differenzschaden nach Verschuldens-, Kausalitäts- und Aufzehrungsprüfung | 05 dann 08/15 |
| Späteres Update mit eigener unzulässiger Einrichtung und Schaden | eigenständige Haftungsspur nach einschlägigem nationalem Recht unter Beachtung `C-666/23`; §§ 826, 31 BGB nur bei zusätzlichen Wissenstatsachen | eigener Update-Schaden ohne Doppelkompensation; eigener Streitgegenstand, eigene Verjährung | 05 dann 07/08/15 |
| Fiat/Ducato mit Timer/Thermofenster, italienische Typgenehmigung | § 826 BGB nur nach Gegenprüfung der KBA-/MIT-Chronologie; § 823 Abs. 2 BGB strikt getrennt | hohes Vorsatzrisiko; Differenzschaden eigenständig prüfbar | 04/05 dann 15/17 |
| Primäranspruch mutmaßlich verjährt, Herstellerzufluss möglich | § 852 BGB (Restschadensersatz) | begrenzte Herausgabe des Erlangten, nicht der volle Schaden | 07 |
| Finanzierungsfall mit Widerrufsansatz | §§ 495, 355, 358 BGB | Rückabwicklung über den Verbund | 12 |
| Betroffenheit offen | offen | sachverständigenabhängig | 04/05 |

2. Update-Dreispur aus Skill 05 übernehmen: Der Erwerbsschaden wird nicht geheilt; Update-Folgen können die ursprüngliche Kausalkette fortsetzen; nur eine eigene Herstellerhandlung mit eigenem Schaden und Kausalität bildet einen gesonderten Streitgegenstand. Keine Einordnung startet die alte Verjährung neu.
3. Verjährung je Streitgegenstand überschlägig prüfen (Entstehung, Kenntnis, Hemmung); bei Zweifel zwingend Skill 07 vor jeder Klagevorbereitung. Die Mitteilung vom 22.09.2015 belegt keine Kenntnis einer später installierten Update-Funktion.
4. Erwerbsinformation prüfen: Ein Kauf nach der Ad-hoc-Mitteilung vom 22.09.2015 kann die EA189-§-826-Linie ausschließen oder schwächen; keine pauschale Sperre für andere Motorfamilien, spätere Funktionen, Kaufrecht oder Differenzschaden. Konkrete Information und Erwerbskausalität belegen.
5. EA288-Anhaltspunkte qualifizieren: Motorfamilie oder Modellliste allein genügt nicht; stärker sind Behörden-/Maßnahmentreffer, technische Herstellerunterlage, Gutachten oder belegter Vortrag zu identischer Konfiguration. Fehlender Rückruf schließt die Spur nicht aus; die 131 veröffentlichten Entscheidungen ersetzen den Fahrzeugbezug nicht.
6. Herstellerrolle und Normzeitpunkt voranstellen: Fahrzeughersteller laut CoC/Typgenehmigung, Motorhersteller, Verkäufer und Finanzierer trennen; Typgenehmigungs-, Herstellungs-, Kauf-, Update- und Schadensdatum bestimmen die Regelungsschicht. Die historische BGH-Spur über §§ 6, 27 EG-FGV nicht schematisch auf post-transitionelle Genehmigungen übertragen; Euro 7 wirkt nicht auf Euro-5/6-Fälle zurück. Die Differenzschadensspur nicht allein aus der Motorlieferung ableiten; CURIA führt `C-408/25` seit dem 21.07.2026 als geschlossen, ohne dass am 30.09.2026 eine veröffentlichte Abschlussentscheidung oder die genaue Erledigungsart feststellbar war. Das Verfahren ist weder Sachentscheidung noch offener Aussetzungsanker. `C-9/26` wurde am 04.08.2026 ohne Sachantwort gestrichen.
7. Rechtsprechungsarbeitsset bauen: höchstens sechs Treffer aus `diesel-fuenfjahre-query.py --arbeitsset` mit zwei höchstrichterlichen Ankern, bis zu zwei Instanzen, einer Gegenlinie und höchstens einem Statusanker; Quellenrang und Verwendungsgrenze bleiben sichtbar.
8. Strategiekarte bauen: Erfolgsaussicht je Spur, Streitwert, Kostenrisiko über zwei Instanzen, Sachverständigenbedarf, Dauer, Vergleichswahrscheinlichkeit und Ziel. Für den Differenzschaden sofort Kaufpreis, Kilometerstand, Gesamtlaufleistung und Restwert erfassen; drohende Aufzehrung ist ein Stopprisiko.
9. Wirtschaftlichkeit ehrlich rechnen: Bei schwacher Beleglage, falschem Gegner, drohender Aufzehrung oder unverhältnismäßigem Gutachtenrisiko ist begründetes Abraten das richtige Ergebnis; Alternativen und Fristen benennen.
10. Vertretung und Finanzierung klären: Landgericht bedeutet Anwaltszwang; Rechtsschutz, Prozessfinanzierer oder Legal-Tech-Abtretung über Skill 10; kollektive Spur über Skill 11.
11. Startkarte ausgeben: Fallart, Ampel, Grund, fehlende Kernstücke, Frist und genau ein nächster Skill; bei mehreren Wegen höchstens drei Optionen.
12. Rückfragen begrenzen: maximal drei, je mit Grund und Folge; bei Gelb vorläufig weiterarbeiten, bei Rot stoppen und eskalieren.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Anspruchsspur, Einwendungen, Beweisrisiko und Wirtschaftlichkeit elementweise vergleichen und auch ein begründetes Abraten als vollwertiges Ergebnis liefern.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Für jede Spur stehen Tatbestandsstatus, stärkstes Gegenargument, Netto-Wirkung und genau ein nächster Schritt fest.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Prüfstandserkennung (EA189) führt zur Vorsatzlinie mit großem Schadensersatz — volle Rückabwicklung, aber Verjährungs- und Nutzungsrisiko. | Bestätigt |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Bei nachgewiesener unzulässiger Abschalteinrichtung und erfüllten weiteren Voraussetzungen führt die Fahrlässigkeitslinie zum Differenzschaden von 5 bis 15 Prozent des Kaufpreises; ein fehlender Vorsatznachweis allein genügt nicht. | Bestätigt |
| EuGH, Urt. v. 21.03.2023 - C-100/21 | Die unionsrechtlichen Typgenehmigungs- und CoC-Regeln schützen auch Käuferinteressen und verlangen bei schuldhaft verursachtem Schaden wirksamen Ersatz; deutsche Anspruchsgrundlage, Fahrlässigkeitsmaßstab und Schadenshöhe folgen aus der BGH-Umsetzung. | Bestätigt |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | EG-Typgenehmigung oder hypothetische Behördenbestätigung trägt einen daraus hergeleiteten unvermeidbaren Verbotsirrtum nicht; § 823 Abs. 2 und § 826 BGB getrennt bewerten. | Amtlich geprüft |
| BGH, Urt. v. 28.07.2026 - VIa ZR 545/23; VIa ZR 151/23 | Konkreter Thermofenstervortrag kann die Differenzschadenprüfung eröffnen; die Zurückverweisungen beweisen weder Betroffenheit noch Haftung. | Amtlich geprüft |
| Fünfjahreskorpus 26.08.2021 bis 26.08.2026: 135 Entscheidungen und Statusakten | Das kleine Arbeitsset kombiniert höchstrichterliche Anker, vergleichbare Instanzen, Gegenlinie und Behörden-/Statusanker; Quellenrang bleibt Teil der Triage. | Kuratierter Arbeitskorpus mit Quellenrängen |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbaustein: Strategiekarte

1 Spur

Für das Fahrzeug mit der FIN [FIN] trägt nach Aktenlage [Anspruchsgrundlage], weil [tragender Befund]; die Spur [Alternative] wird zurückgestellt, weil [Grund].

2 Erfolgsaussicht und Wirtschaftlichkeit

Die Erfolgsaussicht ist [hoch / mittel / gering]; dem stärksten Gegenargument [Gegenargument] wird mit [Beleg] begegnet. Der Streitwert beträgt [Betrag in EUR]; der Nettoerwartungswert nach Vorteilsausgleich beträgt [Betrag in EUR]; das Kostenrisiko über zwei Instanzen wird beziffert.

3 Empfehlung

Empfohlen wird [Anspruchsschreiben / Klagevorbereitung / begründetes Abraten]; zuvor ist die Verjährung über Skill 07 abzuschließen. Genau ein nächster Skill: [Skill]; Entscheidung bis zum [Datum TT.MM.JJJJ], weil [Fristgrund].

### Rechenbeispiel: Überschlag Differenzschaden

Kaufpreis 32.500,00 EUR, Quote 10 Prozent nach § 287 ZPO: brutto 3.250,00 EUR. Nutzungsvorteil: 32.500,00 EUR mal 98.400 km geteilt durch 250.000 km Restlaufleistung gleich 12.792,00 EUR; plus Restwert 18.500,00 EUR gleich 31.292,00 EUR. Fahrzeugwert bei Erwerb 29.250,00 EUR; Überhang 2.042,00 EUR; netto 1.208,00 EUR. Ergebnis-Satz: Bei 1.208,00 EUR netto und laufender Aufzehrung steht die Ampel auf Gelb; ohne fixierten Restwertbeleg ist Abraten oder Vergleich das ehrliche Ergebnis.

### Entscheidungstabelle: Kernweiche

| Befund | Rechtsfolge / Pfad | Weiter |
| --- | --- | --- |
| Prüfstandserkennung, Erwerb vor dem 22.09.2015, unverjährt | großer Schadensersatz § 826 BGB, Zug um Zug | 08, dann 14 |
| Thermofenster fahrzeugbezogen belegt | Differenzschaden 5 bis 15 Prozent, § 287 ZPO | 08, dann 15 |
| Erwerb nach dem 22.09.2015 | Vorsatzlinie regelmäßig gesperrt; Differenzschaden gesondert | 07 und 08 |
| Primäranspruch mutmaßlich verjährt | § 852 BGB nur bei Herstellerzufluss | 07 |
| Finanzierungsfall mit Widerrufsansatz | Verbund §§ 495, 355, 358 BGB | 12 |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Anspruchslinien aus `references/gepruefte-anker-dieselgate.md`, Normstand aus `references/rechtsstand-2026-gesetzgebung.md`, aktuelles Arbeitsset und Gegenrechtsprechung aus `references/diesel-rechtsprechung-2021-2026.md`; Behörden-/Kanzleiquellen nach `references/behoerden-und-praxisquellen-diesel.md`. EA288-Treffer bleiben Nutzermaterial und sind technisch sowie am Volltext zu prüfen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Startkarte und Strategiekarte mit Spur, Erfolgsaussicht, Kostenrisiko, Empfehlung und Ampel in vollständigen, ausformulierten Sätzen. Ab mindestens drei ernsthaft konkurrierenden Spuren wird eine ausgefüllte Vergleichstabelle verwendet; sonst genügen getrennte Absätze oder eine kurze Liste. Bloße Stichwortsammlungen und leere Tabellenzeilen sind als Endprodukt unzulässig.

## Beispiele

- Eingang: EA189, Kauf 2014, Mandat 2026. Kernbefund: Regelverjährung und §-852-Zehnjahresgrenze dominieren. Erste Antwort: Triage-Tabelle mit roter Ampel für § 826 und §-852-Zeile mit Platzhalter, nächster Skill 07.
- Eingang: bloßer Verdacht ohne Rückruf. Kernbefund: keine Spur trägt. Erste Antwort: ausformuliertes Abraten mit roter Ampel und Alternativplan.
