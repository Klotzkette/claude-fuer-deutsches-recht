---
name: grundsteuer-ermittlungsbasis-flaeche
description: "Grundsteuer-Ermittlungsbasis prüfen: Wohnfläche, Nutzfläche, Grundstücksfläche, wirtschaftliche Einheit, Baujahr, Nutzung, Garagen, Stellplätze, Erbbaurecht, Teileigentum, Leerstand, Denkmalschutz und Schätzungen aus der Grundsteuererklärung herausarbeiten."
---

# Grundsteuer: Ermittlungsbasis Fläche, Nutzung und wirtschaftliche Einheit

## Fachlicher Anker

- **Normen:** § 6a.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Aufgabe

Dieser Skill zerlegt die tatsächliche Grundlage der Grundsteuerbewertung. Er eignet sich für Hausverwaltungen, Eigentümer und Berater, wenn Bescheide aus ELSTER-Erklärungen, Altunterlagen oder Schätzungen nicht nachvollziehbar sind.

## Dokumente anfordern

- Grundsteuererklärung und Übermittlungsprotokoll.
- Grundbuchauszug, Teilungserklärung, Aufteilungsplan.
- Wohnflächenberechnung, Mietflächenaufstellung, Bauakte.
- Flurkarte, Katasterauszug, Bodenrichtwertauskunft.
- Mietvertrag / Nutzungsliste / Leerstandsnachweise.
- Denkmalschutzbescheid, Baulasten, Erbbaurechtsvertrag.
- Fotos, Skizzen, Scan der Bescheide.

## Prüfraster

| Feld | Typischer Fehler | Beleg |
|---|---|---|
| Grundstücksfläche | Flurstücke zusammengezogen oder getrennt | Kataster, Grundbuch |
| Wohnfläche | Keller, Dachboden, Balkon, Gewerbe falsch | Wohnflächenberechnung |
| Nutzfläche | Laden, Lager, Werkstatt falsch eingeordnet | Mietvertrag, Bauplan |
| Baujahr | Kernsanierung als Neubau missverstanden | Bauakte, Sanierungsnachweis |
| Grundstücksart | Wohn-/Geschäftshaus, Teileigentum, gemischte Nutzung | Teilungserklärung |
| Bodenrichtwert | Zone oder Stichtag falsch | Gutachterausschuss |
| wirtschaftliche Einheit | mehrere Objekte zusammen oder getrennt | Grundbuch, Nutzung |
| Denkmalschutz / Ermäßigung | nicht berücksichtigt | Bescheid Denkmalschutz |

## Arbeitsweise

1. Bescheiddaten in eine Tabelle übernehmen.
2. Mandantenangaben danebenstellen.
3. Jede Abweichung als "belegt", "plausibel offen" oder "unbelegt" markieren.
4. Fehler nach Bescheidzuständigkeit sortieren: Finanzamt oder Gemeinde.
5. Bei Schätzungsbescheid sofort prüfen, ob eine vollständige Erklärung nachgereicht werden muss.

## Output

Erstelle:

- Datenabgleichstabelle.
- Belegliste mit Verantwortlichkeit.
- Änderungsantrag oder Einspruchsbaustein.
- Fristenhinweis.
- Folgeempfehlung: `anw-grundsteuerwert-bewertung-bewg-218ff` oder `anw-grundsteuer-einspruch-adv-bfh`.

## Grenzen

Keine "gefühlten" Flächenwerte als feststehend ausgeben. Bei streitiger Wohnfläche immer Belege oder Messung verlangen. Rechtsprechung nur aus geöffneten freien Quellen zitieren.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
