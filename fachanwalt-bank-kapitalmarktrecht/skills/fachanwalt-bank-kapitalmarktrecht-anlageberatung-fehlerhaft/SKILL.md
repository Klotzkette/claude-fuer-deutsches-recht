---
name: fachanwalt-bank-kapitalmarktrecht-anlageberatung-fehlerhaft
description: "Workflow-Skill zu fachanwalt bank kapitalmarktrecht anlageberatung fehlerhaft. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Anlageberatung fehlerhaft

## Kaltstart-Rückfragen

1. Welches Anlageprodukt wurde empfohlen (Aktie, Anleihe, Zertifikat, geschlossener Fonds, Schiffsfonds, Immobilienfonds)?
2. Wann erfolgte die Beratung und wann wurde der Erwerb getätigt? Liegt eine Geeignetheitserklärung § 64 Abs. 4 WpHG (bis 02.01.2018: Beratungsprotokoll § 34 Abs. 2a WpHG aF) vor?
3. Welche Risikoklasse hat der Mandant in seinem WpHG-Bogen angegeben? Wurde Risikobereitschaft und Anlageziel erfragt?
4. Hat die Bank über Rückvergütungen (Kick-backs) oder Innenprovisionen aufgeklärt?
5. Wie hoch ist der eingetretene Schaden (Erwerbsschaden, entgangener Gewinn)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Anspruchsgrundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anleger- und anlagegerechte Beratung — Pflicht zur vollständigen, richtigen und verständlichen Information.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anspruchsgrundlage: §§ 280 Abs. 1, 311 Abs. 2 BGB i.V.m. Beratungsvertrag (Schadensersatz wegen Pflichtverletzung).
- Bei Vorsatz oder Sittenwidrigkeit zusätzlich § 826 BGB und § 31 BGB für Organhaftung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweislast und Frist

- Anleger trägt Darlegungs- und Beweislast für Beratungsfehler und Schaden.
- Bank trägt Beweislast für rechtzeitige und ordnungsgemäße Aufklärung.
- Bei festgestellter Pflichtverletzung wird Ursächlichkeit für Anlageentscheidung vermutet (Vermutung aufklärungsrichtigen Verhaltens).
- Verjährung Regelfrist § 195 BGB drei Jahre ab Kenntnis Schaden und Schädiger; Höchstfrist zehn Jahre § 199 Abs. 3 Nr. 1 BGB ab Anspruchsentstehung.

## Prüfschema

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


```
1. Beratungssituation (Beratungsvertrag konkludent?)
2. Pflicht zu anleger- und anlagegerechter Beratung
3. Aufklaerungsmaengel identifizieren
   - Risikoaufklaerung
   - Rueckverguetung/Kick-back
   - Innenprovision >= 15%
   - Totalverlustrisiko (geschlossene Fonds)
4. Geeignetheitserklaerung § 64 Abs. 4 WpHG analysieren (bzw. § 34 Abs. 2a WpHG aF bis 02.01.2018)
5. Schaden berechnen (Erwerbsschaden + entgangener Gewinn)
6. Verjaehrung pruefen (3 Jahre Kenntnis / 10 Jahre Hoechstfrist)
```

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — fehlerhafte Anlageberatung ruegen und Schadensersatz fordern | Anspruchsschreiben nach Schreibvorlage unten |
| Variante A — Verjährung droht | Verjährungshemmung (Klage/Verhandlungsaufnahme) sofort; keine Aussergerichts-Zeit |
| Variante B — Bank zeigt Einigungsbereitschaft | Aussergerichtliche Einigung bevorzugen; schnellere Auszahlung |
| Variante C — Schadenshoehe unklar | Stufenklage oder Feststellungsklage als Alternative |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schreibvorlage Anspruchsschreiben

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft machen wir Schadensersatz
wegen fehlerhafter Anlageberatung aus dem Beratungsvertrag vom [Datum]
und §§ 280 Abs. 1 311 Abs. 2 BGB geltend.

Unsere Mandantschaft erwarb am [Datum] auf Empfehlung Ihres Hauses das
Anlageprodukt [Produktbezeichnung WKN/ISIN] zu einem Erwerbspreis von
EUR [Betrag].

Beratungsfehler liegen in folgenden Punkten:
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
   510/07 Beschl. v. 20.01.2009 Rn. 12 ff.)
2. unterlassene Aufklaerung ueber Innenprovision von [...] Prozent
   Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. anlegerunabhaengige Empfehlung trotz Risikoklasse [...]

Wir fordern Sie auf bis [Datum vier Wochen] Zug um Zug gegen Rueckgabe
der Wertpapiere den Erwerbspreis EUR [Betrag] zuzueglich entgangener
Gewinn in Hoehe von EUR [Betrag] zu erstatten.

Andernfalls werden wir Klage erheben.

Mit freundlichen Gruessen
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Übergabe

- Bei Ablehnung: Klage am Sitz der Bank bzw. Wohnsitz des Anlegers § 32b ZPO bei kapitalanlegerrechtlichem Musterverfahren prüfen.
- Verjährungsfrist im Aktenkalender notieren — Hemmung durch Verhandlungen § 203 BGB sichern.
- Bei Vergleichsverhandlungen Hemmungsschriftverkehr dokumentieren.

## Vertiefung: Leitsaetze und Workflow-Ergaenzung

### Triage — Bevor losgelegt wird, klaere:

1. Wann fand die Beratung statt? → Verjaebrung 3 Jahre ab Kenntnis + max. 10 Jahre absolut.
2. Liegt Beratungsprotokoll (§ 83 WpHG / § 34 WpHG aF) oder Geeignetheitserklaerung (§ 64 WpHG) vor? → Fehlende Dokumentation = Beweisschwaeche Bank.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. Schadenshoehe: Differenzhypothese oder negatives Interesse berechnen?

### Ergaenzende Leitsaetze
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt-fuer-Schritt-Workflow Anlageberatungsfehler
1. **Mandantengespräch:** Produkt, Datum Beratung, Risikoprofil, Verlusthoehe dokumentieren.
2. **Beratungsprotokoll anfordern** (§ 83 WpHG, § 64 Abs. 4 WpHG): 3-Tage-Frist auf Herausgabe.
3. **Pruefung Kickbacks:** Bank-interne Vertriebsprovision vom Emittenten = aufklaerungspflichtig.
4. **Schadensberechnung:** Eingesetztes Kapital minus aktueller Wert + entgangene 4 %-Verzinsung.
5. **Ausforderungsschreiben** an Bank mit 4-Wochen-Frist, Schadensaufstellung, Klageandrohung.
6. **Ombudsmann** einschalten (hemmt Verjaebrung § 204 BGB).
7. **Klage** bei Ablehnung: LG (§ 23 GVG Streitwert ab EUR 5.000).
