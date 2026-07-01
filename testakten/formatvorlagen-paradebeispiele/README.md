# Formatvorlagen-Paradebeispiele

Wenn du das hier öffnest, willst du sehen, wie der Formatstandard des Repos (Times New Roman 11 pt, dezimale Gliederung, vollständig ausformulierte Sätze) in fertigen juristischen Vorlagen aussieht.

Dieser Ordner ist **keine Testakte**, sondern eine automatisch erzeugte Vorlagensammlung: je Rechtsgebiet ein Unterordner mit ein bis zwei Paradebeispielen als Markdown- und ODT-Fassung (zum Beispiel Kündigungsschutzklage, Aufhebungsvertrag, Erbscheinantrag, Gläubigerantrag nach Paragraf 14 InsO, Grundstückskaufvertrag).

## Wichtig für Audits und Prüfläufe

Die eckigen Platzhalter (`[Betrag]`, `[Name der Kanzlei]`, `[Datum]`) sind hier **beabsichtigt**: Vorlagen leben von Ausfüllfeldern. Das Platzhalterverbot aus [`../QUALITAETSSTANDARD.md`](../QUALITAETSSTANDARD.md) gilt für Aktenstücke in Testakten, nicht für diese Sammlung. Ebenso gibt es hier bewusst kein Gesamt-PDF.

## Pflege

Die Dateien werden von `scripts/generate-formatvorlagen.py` erzeugt (Regeln: A4, 2.5 cm Rand, Disclaimer kursiv oben, verifizierbare Normzitate, bei bilingualen Vorlagen Maßgeblichkeit der deutschen Fassung). Änderungen daher bevorzugt im Generator vornehmen und neu erzeugen, nicht in den Einzeldateien.
