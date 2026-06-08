---
name: sanity-check-selbstvertretung-amtsgericht
description: "Letzter Sanity-Check vor Klage, Klageerwiderung, Replik, Termin, Vergleich oder Rechtsmittel beim Amtsgericht. Prüft Fristen, Zuständigkeit, Anwaltszwang, Streitwert, Antrag, Tatsachenvortrag, Beweise, Anlagen, Kosten, Zustellung und rote Warnsignale."
---

# Sanity-Check Selbstvertretung Amtsgericht

## Zweck

Dieser Skill ist die letzte Kontrolle, bevor ein Bürger ohne Anwalt etwas beim Amtsgericht einreicht oder im Termin verwendet. Er soll verhindern, dass gute Fälle an Form, Frist, Beweis oder unklarem Antrag scheitern.

## Wann aktivieren?

- Vor Klageeinreichung.
- Vor Klageerwiderung, Replik oder Duplik.
- Vor einem Termin.
- Vor Annahme oder Ablehnung eines Vergleichs.
- Nach Urteil, wenn Rechtsmittel geprüft werden.
- Immer, wenn der Nutzer sagt: "Kann ich das so abschicken?"

## Prüfmatrix

| Prüfungslinie | Kernfrage | Ampel |
|---|---|---|
| Frist | Gibt es eine Notfrist, gerichtliche Frist, Verjährung oder Zustellungsfrage? | Rot/Gelb/Grün |
| Gericht | Ist das Amtsgericht sachlich und örtlich zuständig? | Rot/Gelb/Grün |
| Anwalt | Besteht wirklich kein Anwaltszwang? | Rot/Gelb/Grün |
| Antrag | Ist der Antrag bestimmt, vollstreckbar und zum Ziel passend? | Rot/Gelb/Grün |
| Tatsachen | Ist der Sachverhalt chronologisch und konkret genug? | Rot/Gelb/Grün |
| Beweis | Gibt es zu jeder bestrittenen wichtigen Tatsache ein Beweismittel? | Rot/Gelb/Grün |
| Anlagen | Sind Anlagen nummeriert, lesbar und im Text bezeichnet? | Rot/Gelb/Grün |
| Kosten | Sind Gerichtskosten, Gegenseite und Sachverständige bedacht? | Rot/Gelb/Grün |
| Versand | Ist der Einreichungsweg fristsicher dokumentiert? | Rot/Gelb/Grün |
| Eskalation | Gibt es rote Flaggen für Anwalt, Rechtsantragsstelle oder PKH? | Rot/Gelb/Grün |

## Rote Flaggen

Empfehlen Sie deutlich anwaltliche Hilfe oder Rechtsantragsstelle, wenn:

- Streitwert über 10.000 EUR oder Landgericht möglich;
- Berufung, Revision oder Beschwerde beim Landgericht/Oberlandesgericht;
- Familiensache mit § 114 FamFG;
- unklare Zustellung bei laufender Notfrist;
- drohende Verjährung in weniger als 14 Tagen;
- Sachverständigenbeweis wahrscheinlich und Kostenrisiko hoch;
- Widerklage, Aufrechnung, mehrere Parteien oder Auslandssachverhalt;
- Vergleich mit Raten, Verzicht, Abgeltung oder Vollstreckungsklausel;
- Nutzer versteht den eigenen Antrag nicht.

## Ablauf

### 1. Dokument bestimmen

Benennen Sie genau, was geprüft wird:

- Klage;
- Klageerwiderung;
- Replik/Duplik;
- Fristverlängerungsantrag;
- Terminnotizen;
- Vergleichsvorschlag;
- Berufungsschrift;
- PKH-Antrag.

### 2. Fehlende Informationen markieren

Nicht raten. Fehlt etwas, schreiben Sie:

| Fehlt | Warum wichtig? | Wie nachholen? |
|---|---|---|
| Zustellungsdatum | Fristbeginn | Umschlag/gelber Brief/Fax-/MJP-Quittung prüfen |

### 3. Konkrete Reparatur vorschlagen

Jede gelbe oder rote Ampel bekommt einen Reparaturschritt:

- "Antrag enger formulieren";
- "Anlage K3 im Text nennen";
- "Zeugen mit vollständiger Anschrift benennen";
- "Fristende mit `fristen-berechnen-187-188-bgb` prüfen";
- "Vor Einreichung `zulassungsgrenzen-check-amtsgericht` ausführen".

## Ausgabeformat

**Sanity-Check**
| Feld | Ampel | Befund | Reparatur |
|---|---|---|---|
| Frist | Rot/Gelb/Grün | | |

**Nicht abschicken, bevor**
1. [kritischer Punkt]

**Kann so raus, wenn**
1. [Bedingung]

**Passende nächste Skills**
| Skill | Zweck |
|---|---|
| `zulassungsgrenzen-check-amtsgericht` | Zuständigkeit, Wertgrenze, Rechtsmittel |

## Qualitätsregeln

- Keine Schriftsatzfreigabe behaupten. Formulieren Sie: "Nach Aktenstand wirkt es einreichungsfähig, wenn die offenen Punkte erledigt sind."
- Fristen immer mit Datum, Ausgangspunkt und Unsicherheit nennen.
- Bei Gerichts- oder Rechtsmittelpost nie nur "sieht gut aus" sagen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
