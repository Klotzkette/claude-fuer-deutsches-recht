# Insolvenz-Testakten mit bearbeitbaren Arbeitsvorlagen

Die Ausgabe enthält die 24 dem Fachanwalt für Insolvenz- und Sanierungsrecht zugeordneten Testakten und die dort verlinkte Bremer Darlehensakte. Beide Originalformat-ZIPs jeder Akte enthalten einen Ordner `Arbeitsvorlagen/`. Er enthält einen ausfüllbaren Unternehmenskaufvertrag und die für den Fall erstellten Word- oder Excel-Vorlagen. Alle Vorlagen sind auch in `insolvenz-arbeitsvorlagen.zip` zusammengestellt.

Die 50 früheren Originalformat-ZIPs stammen aus den Ausgaben `grundakten-sammlung-v1.0.0`, `insolvenz-arbeitsakten-v1.0.0` und `grundakten-fachakten-v1.1.0`. Ihre Aktenstücke, Eingangspost, Quellenhinweise und Archivpfade bleiben bytegetreu erhalten. Die Druckfassungen sind weiterhin unter ihren bisherigen Adressen verfügbar.

## Bestand nachvollziehen

`release-bestand.json` nennt den Quellcommit und führt für jede Akte Name, Größe und SHA-256 der Ausgabe, den Tag und die Prüfsumme der Vorfassung sowie die hinzugefügten Arbeitsvorlagen mit ihren Prüfsummen auf. `checksums-sha256.txt` umfasst alle 51 ZIPs und den Bestandsnachweis.

Aus dem ausgecheckten Quellcommit lässt sich die Veröffentlichung so nachbauen. Das Ausgabeverzeichnis muss leer sein. Nach dem ersten Lauf lässt sich derselbe Cache auch mit `--offline` verwenden.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build-insolvenz-arbeitsvorlagen-release.py --dist /tmp/insolvenz-ausgabe --cache /tmp/insolvenz-quellen --expected-commit "$(git rev-parse HEAD)"
```

Der GitHub-Actions-Workflow „Insolvenz-Testakten mit Arbeitsvorlagen“ läuft zur Veröffentlichung auf `main` mit dem Eingabefeld `expected_commit`. Er baut aus diesem Stand, prüft die Akten und lädt anschließend den vollständigen Release-Entwurf erneut zur Prüfung herunter. Erst nach der öffentlichen Freigabe werden die Downloadlinks in einem eigenen Schritt umgestellt.
