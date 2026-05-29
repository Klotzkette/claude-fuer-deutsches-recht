# Testakte: Nachbarschaftsstreit Rosengartenstraße

**Fiktive Testakte.** Alle Personen, Adressen, Aktenzeichen, Flurstücke, Firmen und Behördenkontakte sind erfunden. Die Akte dient zum Testen des Plugins `nachbarschaftsstreit-pruefer`.

## Kurzbild

Marianne und Dr. Henning Albers besitzen ein Reihenendhaus in der Rosengartenstraße 17 in Köln-Rodenkirchen. Das Nachbargrundstück Rosengartenstraße 19 gehört Stefan und Lara Kessler. Was als Streit über eine zu hohe Thujahecke begann, ist binnen zwei Jahren zu einem vollen Nachbarrechts-Horrorfall geworden:

- Ein neu errichteter Carport der Kesslers ragt nach Albers' Messung über die Grenze.
- Die Dachrinne des Carports entwässert Richtung Albers-Grundstück.
- Eine alte Platane wirft Äste über Garage und Wintergarten; Wurzeln heben Pflaster und drücken gegen eine Grenzmauer.
- Eine Baugrube für einen Pool hat Risse in der Stützmauer ausgelöst.
- Ein Sichtschutzzaun wurde ohne Absprache direkt an die Grenze gesetzt.
- Grillrauch, Lichtstrahler und eine Kamera sorgen für weitere Eskalation.
- Kesslers behaupten plötzlich ein Notwegerecht für Handwerker durch den Garten der Albers.
- Bauamt, Ordnungsamt, Gartenbauunternehmen, Vermesser und zwei Anwälte haben jeweils nur Teile der Akte gesehen.

Die Akte enthält keine Musterlösung. Sie ist absichtlich fragmentarisch, widersprüchlich und voll mit Dingen, die in echten Nachbarschaftsmandaten das Denken verstopfen.

## Dateien

| Datei | Inhalt |
|---|---|
| `01_erstgespraech_mandantennotiz.md` | Kanzleinotiz mit Sachverhaltsaufnahme |
| `02_lage_grundstuecke_grenze.md` | Flurstücke, Grenzpunkte, Liegenschaftskarte, Vermessungszweifel |
| `03_bautagebuch_carport_ueberbau.md` | Bauverlauf, Widerspruch, Carport, Dachrinne |
| `04_fotodokumentation_und_messliste.md` | Foto- und Messplan als Textakte |
| `05_baumgutachten_platane_wurzeln_aeste.md` | Baumsachverständigen-Notiz |
| `06_chat_email_eskalation.md` | E-Mails und Messenger-Auszüge |
| `07_bauamt_ordnungsamt_vorgaenge.md` | Behördenkontakte und Zuständigkeitswirrwarr |
| `08_kosten_schaeden_angebote.csv` | Kosten und Angebote |
| `09_anwaltsschreiben_kessler.md` | Gegnerisches Schreiben |
| `10_aufforderungsschreiben_albers_entwurf.md` | Entwurf eines Anspruchsschreibens |
| `11_eilrechtsschutz_und_beweissicherung.md` | Eil- und Beweissicherungsvermerk |
| `12_vergleichsentwurf_rosengartenfrieden.md` | Vergleichsentwurf mit Vollzugsplan |

## Vorführpfad

1. `horrorfall-aktenauswertung` zum Sortieren der gesamten Akte.
2. `ueberbau-pruefung` für Carport und Dachüberstand.
3. `ueberhang-aeste-wurzeln` für Platane und Wurzeln.
4. `vertiefung-baugrube-stuetzverlust` und `drohender-einsturz-gefahranlage` für Risse.
5. `einfriedung-zaun-mauer-hecke` und `landesnachbarrecht-router` für Sichtschutz/Hecke.
6. `aufforderungsschreiben-nachbar`, danach je nach Lage `einstweilige-verfuegung-und-klage` oder `vergleich-mediation-nachbarschaftsfrieden`.
