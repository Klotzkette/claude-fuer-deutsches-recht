# Praxisnachträge zu zwölf Testakten

Die Fallseiten führen zur vollständigen Originalakte mit Nachtrag. Für kurze Übungen lässt sich dort auch nur der Nachtrag laden. In jeder Vollakte enthält `Praxisnachtrag/Grundakte` die E-Mail des ersten Eingangs mit ihrem CSV-Anhang. Die Tabelle liegt zusätzlich separat bei. `Praxisnachtrag/Nachlieferung` enthält die spätere schriftliche Auskunft und einen zweiten Datenauszug. Die Zeitangaben stehen in der E-Mail und im Vermerk. Wer zunächst nur den ersten Eingang kennt, kann seine vorläufige Antwort festhalten und sie nach der zweiten Lieferung am Beleg überprüfen.

| Fall und Downloads | Auszug beim ersten Eingang | Auszug bei der Nachlieferung |
| --- | --- | --- |
| [Zwei Paletten für Tor 2](../../testakten/compliance-hameln-schokolade-charge-k17/README.md) | Versanddruckjournal Puffer 2 | Kundendienst Filiale 014 · Teilmenge bereits gemeldeter Rücknahmen |
| [Der Feiertag im Tourenjournal](../../testakten/forderungsmanagement-baeckerei-behaeltertausch-hamburg/README.md) | Schlüsselbuch der Backstube · Jahreswechsel | Abfragejournal · Tour H03 / Datensatzherkunft |
| [Die Rückseite von Tageszettel 1578](../../testakten/berufskrankheit-asbest-schlosser-werft-bremen/README.md) | Lesesaal · Bereitstellung 20. Juli | Abschrift Rückseiten · interne Zeitverteilung |
| [Mit dem Schlüssel vor der Hoftür](../../testakten/sozialrecht-elektrorollstuhl-koerner-oldenburg/README.md) | Theaterwall 62 · Reinigungsplan Erdgeschoss | Beobachtungsblatt 16. Juni · Hofseite |
| [Wer hat den Camper reserviert?](../../testakten/steuerrecht-freiburg-oderkonto-schenkungsteuer/README.md) | Verkaufstagebuch · Vorgang RM-518 | Historie RM-518 · Übergabe und Rücklauf |
| [Vier Hauskostenbuchungen für die Wohnung in Rom](../../quality/steuerrecht-freiburg/tomasius-solo/README.md) | Quartalsblatt Interno 7 · Belegversand | Mietmodul · Beispiel einer Zahlungsreferenz |
| [Der verlegte Gitarrentermin](../../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/README.md) | Studioauszug · Freitag 6. März | Portaljournal · Termin- und Abrechnungsfelder |
| [Was ist aus dem Stadtbestand wirklich verwendbar?](../../testakten/bauunternehmer-einkauf-altstadt-bordsteine/README.md) | Lagerplatz Rosenbogen · Ausgabeplan | Messzettel Stichprobe S-A · Längen am Kopf |
| [Die Rückwand hinter E4-075](../../testakten/bauunternehmer-einkauf-brandschutztueren-krimpfort/README.md) | Begehungsliste Ebene E4 · Ausschnitt | Aufmaß 07.12. · Ausschnitt Ebene E4 |
| [Die Pumpenleitung hinter Gerät S03](../../testakten/bauunternehmer-einkauf-lueftungszentralen-krimpfort/README.md) | TGA-Aufmaß · südlicher Technikgang | S03 · Einfache Trasse vorläufiger Stationsort |
| [Das Registerbuch im zweiten Archivkasten](../../testakten/notariat-berlin-mumbai-gesellschafterliste/README.md) | Office records · Mumbai / dispatch register | Vollzugsakte · Nachforderungskontrolle |
| [Zwei Dinge in einem Kurierumschlag](../../testakten/notariat-berlin-vae-vertretungsnachweis/README.md) | Dubai filing desk · counter list | Posteingang · Nebenakte UVZ 527/2026 |

## Ausgaben nachvollziehen

Die Fassungen der ursprünglichen ZIPs sind in den [Quelldaten](../../scripts/data/testakten-praxisnachtraege-2026-11.json) je Fall mit Release-Adresse und SHA-256 festgehalten. Jeder bisher enthaltene Dateipfad und sein Inhalt bleiben in der erweiterten ZIP erhalten. Die vier hinzugekommenen Aktenstücke stehen in den beiden Nachtragsordnern. Die Einzel-PDFs und das vierseitige PDF bilden nur diese vier Aktenstücke ab.

Für den Wiederaufbau die zwölf ZIPs aus `baseline.url` unter ihrem bisherigen Dateinamen in einem gemeinsamen Quellordner ablegen. Mit ReportLab und pypdf aus der Repository-Umgebung anschließend im Repository-Hauptverzeichnis ausführen.

```sh
python3 scripts/build-testakten-praxisnachtraege.py --baselines <Quellordner> --dist <Ausgabeordner>
```

Der Aufbau prüft die SHA-256 jeder Ausgangsdatei, vergleicht nach dem Verpacken jeden bisherigen ZIP-Eintrag byteweise und prüft die vier Seiten des Nachtrags auf Textinhalt. Mit `--annex` lässt sich auch für die kompakten Downloads ein eigener Ausgabeordner festlegen.
