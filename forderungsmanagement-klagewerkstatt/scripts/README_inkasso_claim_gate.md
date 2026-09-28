# Inkasso Claim Gate

`inkasso_claim_gate.py` ist ein kleiner formaler Prüfer für Forderungsakten. Er liest eine JSON-Datei mit einzelnen Forderungspositionen und gibt je Position eine Ampel aus:

- `GRÜN`: kann in den Klageantrag, wenn Gerichtsort und Belege bestätigt sind.
- `GELB`: nur nach anwaltlicher Freigabe, Rückfrage oder Vergleichsvorschlag.
- `ROT`: nicht einklagen.

Beispiel aus dem Repository-Wurzelverzeichnis:

```bash
python forderungsmanagement-klagewerkstatt/scripts/inkasso_claim_gate.py \
  --input quality/fixtures/modefuchs/08_claim_gate_input.json
```

Ohne `--output` erscheint das Ergebnis auf der Standardausgabe. Die Eingabe und die getrennte Referenzausgabe `quality/fixtures/modefuchs/09_claim_gate_output.json` sind technische Prüfdaten, keine Arbeitsunterlagen der Downloadakte. Eine gespeicherte Lauf-Ausgabe gehört außerhalb von `testakten/` und darf die Referenzausgabe nicht überschreiben.

Das Werkzeug ersetzt keine materiell-rechtliche Prüfung. Es verhindert nur, dass erfüllte oder nicht belegte Positionen ungeprüft in eine Klage übernommen werden.
