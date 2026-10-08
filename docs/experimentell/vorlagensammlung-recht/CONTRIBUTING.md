# Mitwirken an der Vorlagensammlung

Beiträge jeder Art sind willkommen — Korrekturen an bestehenden Vorlagen, völlig neue Muster, Hinweise auf veraltete Normzitate, Aktualisierungen nach neuer Rechtsprechung, redaktionelle Verbesserungen.

## Wie ein Beitrag aussieht

1. **Fork und Branch** — pro Beitrag ein eigener Branch.
2. **Eine Vorlage pro Pull Request** — keine Sammel-PRs über mehrere Themenbereiche.
3. **Pflicht: beide Formate, sprechende Dateinamen** — jede neue Vorlage liegt sowohl als `<vorlagen-slug>.md` als auch als `<vorlagen-slug>.odt` vor. Der Dateistamm ist identisch mit dem Unterordner der Vorlage. Generische Namen wie `vertrag.md`, `text.odt`, `vorlage.md`, `VORLAGE.odt`, `SKILL.md` oder `SkillMD` sind nicht zulässig. Das ODT wird aus der bearbeitbaren Markdown-Fassung über das Generator-Skript erzeugt (siehe unten).
4. **Pflicht: kurzer Vorlagenhinweis, lange Hinweise in die README** — jede Vorlagen-Markdown-Datei enthält im Kopf nur den knappen Kurz-Hinweis auf Unverbindlichkeit, experimentellen Text, keine Rechtsberatung, eigene Gewähr und eigene Gefahr. Normenanker, Rechtsprechungsanker, Einsatzgrenzen, ausführliche Warnungen und Bearbeitungshinweise gehören in die README des jeweiligen Vorlagenordners, nicht in die Vorlagendatei und damit auch nicht in das ODT. Der Kurz-Hinweis muss in **jeder** Vorlage folgende Aussagen enthalten:
   - **unverbindlich**
   - **experimenteller Text**
   - **keine Rechtsberatung**
   - **Verwendung ausschließlich auf eigene Gewähr und auf eigene Gefahr**
5. **Pflicht: Vorlagen-README mit Direktdownloads und Vorschau** — jeder Vorlagen-Unterordner enthält eine `README.md` mit Zweck, Anwendungsbereich, einschlägigen Normen, typischen Fallstricken, einem ODT-Direktdownload und einem Direktdownload der gleichnamigen `.md.zip`. Eine Vorschauzeile verlinkt zusätzlich die lokale `.odt`- und `.md`-Datei. Die Linktexte und Dateinamen sind sprechend und nennen das konkrete Dokument, etwa „AGB Online-Shop B2C – ODT herunterladen“, nicht bloß `vertrag.odt`, `text.md`, `Markdown-Quelle` oder `ODT-Arbeitsfassung`.

6. **Pflicht: Dezimale Gliederung** — in jeder Vorlage gilt die Regel aus `references/gliederung.md`: ausschließlich `1`, `1.1`, `1.1.1` …, niemals römische Ziffern oder Großbuchstaben oder Verlagsstil-Mischungen, Leerzeile zwischen Gliederungsüberschrift und Inhalt, Einrückung sparsam. Prüfung im CI: `scripts/check-gliederung.py`.

7. **Pflicht: Präambel nur als Vertragsziffer** — eine Präambel steht bei Verträgen niemals unnummeriert vor dem Vertragstext. Wenn sie gebraucht wird, ist sie Abschnitt `1. Präambel / Gegenstand`; die Schlussbestimmungen enthalten dann ausdrücklich, dass Abschnitt 1 Bestandteil des Vertrags ist und Regelungsgehalt hat.

8. **Pflicht: Gegenstandsindividualisierung** — jede neue oder geänderte
   Vorlage wird anhand von `references/gegenstandsindividualisierung.md`
   geschärft. Vor der ersten Änderung ist zu klären, was genau geregelt wird,
   wer beteiligt ist, welches Recht gilt und welche Besonderheiten diesen
   Gegenstand von ähnlichen Vorlagen unterscheiden. Sätze, die unverändert in
   einem anderen Dokument stehen könnten, werden konkretisiert oder gestrichen.

9. **Pflicht: eckige Platzhalter** — Ausfüllfelder stehen in Vorlagen
   ausschließlich in eckigen Klammern, etwa `[Name]`, `[Datum]`,
   `[Betrag in EUR]` oder `[Alternative A / Alternative B]`. Spitze oder
   geschweifte Klammern sind für Platzhalter nicht zulässig.

10. **Pflicht: beide Navigationsachsen pflegen** — jede neue Vorlage wird im
    `README.md` ihres Rechtsgebiets genau einmal verlinkt und zusätzlich in
    genau eine der drei Dokumenttyp-Sichten unter `kategorien/` eingetragen.
    Das Rechtsgebietsmenü verwendet den H1-Titel der Vorlagen-README als
    Linktext. `scripts/validate-vorlagen.py` und
    `scripts/check-kategorien-index.py` prüfen diese Abdeckung.

11. **Pflicht: Gesamtindex und Release-Pakete aktualisieren** — nach einer
    Neuanlage, Löschung oder Umbenennung wird
    `python3 scripts/build-download-index.py` ausgeführt. Der erzeugte Index
    führt Hauptvorlagen mit ODT und Markdown-ZIP sowie jede gerichtsleitende
    Sondervorlage mit einzelnem Raw-Download. Vor dem Release erzeugt
    `python3 scripts/build-release-assets.py` die ODT-, Markdown- und
    gerichtsleitenden Komplettpakete sowie `SHA256SUMS.txt`; jedes Paket
    erhält zusätzlich einen filterbaren Offline-Index namens `index.html`
    und ein maschinenlesbares `manifest.json` mit Versionsstand, Dateigröße
    und SHA-256-Prüfsumme jeder Arbeitsdatei. Der Paketbau veröffentlicht das
    vollständige Set erst nach erfolgreichem Staging. `dist/` bleibt
    unversioniert.

## ODT aus Markdown erzeugen

Das Repository enthält ein einfaches Generator-Skript:

```bash
python3 scripts/md-to-odt.py <pfad/zur/<vorlagen-slug>.md>
```

Erzeugt im selben Verzeichnis eine gleichnamige `.odt` aus der Markdown-Fassung und normalisiert das ODT-Basislayout auf A4, 2,5 cm Ränder, Times New Roman 11 pt und rechte Seitenzahl in der Fußzeile. Voraussetzung: Python 3 und `pandoc`.

Jede erzeugte ODT-Fassung erhält ausschließlich auf Seite 1 eine
zweisprachige Fußzeile mit dem verbindlichen Hinweis „Mit KI generiert. Dies
ist ein experimentelles Dokument. Benutzung auf eigene Gefahr und eigenes
Risiko.“ und „Generated with AI. This is an experimental document. Use at
your own risk.“ Der Generator fügt den Hinweis automatisch ein; er darf weder
in den Markdown-Mustertext kopiert noch in der ODT-Fassung verändert oder
entfernt werden. Die Integritätsprüfung kontrolliert Wortlaut, Einmaligkeit
und Position auch bei jeder neuen Vorlage.

## Rubrics und Eval-Harness

Jeder Vorlagenordner enthält eine `rubric.yaml`. Neue Vorlagen bekommen deklarative Pass/Fail-Checks; neue Python-Checks sind nur nötig, wenn der vorhandene Check-Typ nicht ausreicht.

Baseline-Rubrics für neue Ordner:

```bash
python3 scripts/generate-default-rubrics.py
```

Bewertung und Report:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/run-eval.py --report
python3 scripts/run-eval.py --verbose
python3 scripts/run-eval.py --json-out runs/baseline.json --label baseline
```

Der normale Eval-Lauf hält die Konsole bewusst knapp und gibt neben der
Gesamtsumme nur fehlgeschlagene Vorlagen mit ihren konkreten Checks aus.
`--verbose` ergänzt sämtliche erfolgreichen Einzelzeilen, wenn ein vollständiges
Protokoll benötigt wird.

Die Testakten unter `tests/testakten/` decken alle vom Harness dokumentierten
Checktypen ab. Wer einen Checktyp ergänzt oder dessen Semantik ändert, erweitert
zuerst diese Testakte und den zugehörigen Negativtest. Unbekannte Checktypen,
doppelte Check-IDs, unlesbare Rubrics und unbekannte Ziel-Slugs müssen sichtbar
fehlschlagen; ein leerer oder still verkürzter Eval-Lauf gilt nicht als grün.

Modell- oder Versionsvergleich:

```bash
python3 scripts/compare-eval-runs.py runs/baseline.json runs/vergleich.json
```

Subjektive Stiltreue-Kriterien, etwa für Kanonistik, klassisches Latein oder PrALR-Sprache, werden nur per LLM-Judge geprüft, wenn Regex oder Textsuche nicht ausreichen. Ohne API-Key läuft das Skript als Dry Run und gibt den Prompt aus.

## Validierung

Vor jedem Pull Request:

```bash
grep -rE "(ae|oe|ue|ss)" --include="*.md"
python3 scripts/validate-vorlagen.py
python3 scripts/build-download-index.py --check
python3 scripts/run-eval.py --report
```

Prüfungen:

- Zu jeder sprechend benannten Markdown-Datei existiert eine gleichnamige ODT-Datei im selben Ordner.
- Jede Vorlagen-Markdown-Datei enthält den Disclaimer-Block und die Hinweisleiste.
- Jeder Vorlagen-Unterordner enthält eine `README.md`.

## Stil

- Sachlich, kurze Sätze, deutsche Rechtssprache.
- Keine generische Schablonensprache: Jede Klausel benennt den konkreten
  Gegenstand, die konkreten Rollen, Pflichten, Fristen, Schnittstellen,
  Rechtsfolgen und Risiken der jeweiligen Vorlage.
- Norm-, Entscheidungs- und Behördenzitate werden vor Aufnahme live geprüft.
- Keine Werbung, keine Eigennennung, keine Verweise auf konkrete Mandate oder Mandanten.
- **Pflicht: echte Umlaute und scharfes ß** — in allen deutschsprachigen Inhalten (Vorlagen, READMEs, Commit-Messages) werden **ä ö ü Ä Ö Ü ß** verwendet, niemals Umschreibungen wie `ae/oe/ue/ss`. In Dateinamen und Slugs sind Umlaute nicht zulässig — dort werden sie ausgeschrieben.

## Lizenz von Beiträgen

Mit dem Einreichen eines Beitrags stimmt die beitragende Person zu, dass der Beitrag unter den beiden Lizenzen dieses Repositories — **Apache-2.0** und **MIT** — veröffentlicht wird.
