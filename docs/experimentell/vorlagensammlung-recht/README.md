# Vorlagensammlung Recht

Separate experimentelle Kopie, Stand v4.92.0 vom 9. Oktober 2026. Die Vorlagen sind keine Plugins und werden nicht über einen Marketplace installiert. Diese Fassung korrigiert konkrete Rechts- und Quellenfehler insbesondere im Arbeits-, Bank-, Miet-, Insolvenz- und IT-Vertragsrecht. Der [Prüfbericht mit Quellen und Umfang](references/rechtsstandsabgleich-2026-10-09.md) trennt die gezielte fachliche Überarbeitung von den technischen Prüfungen über den vollständigen Bestand. Nicht alle 1094 Vorlagen wurden in dieser Runde einzeln und abschließend rechtlich geprüft. Herkunft und unveränderter ursprünglicher Importstand stehen in [IMPORT.json](IMPORT.json).

Eine offene Sammlung von Vertrags-, Formular- und Schreibvorlagen zum deutschen Recht — jede Hauptvorlage liegt parallel als OpenDocument (`.odt`) und als Markdown (`.md`) vor. Die ODT-Datei ist die sofort bearbeitbare Arbeitsfassung, die Markdown-Datei ist die robuste, prüfbare Quellenfassung für Versionierung, Qualitätssicherung und weitere Bearbeitung.

## Vorlage finden und herunterladen

| Gesucht | Direkteinstieg | Ergebnis |
|---|---|---|
| Eine konkrete Vorlage mit direktem ODT- oder Markdown-Download | [Gesamtindex und Direktdownloads](DOWNLOADS.md#schnellzugriff) | Durchsuchbare Liste aller Hauptvorlagen mit Menüseite, Dokumenttyp und beiden Downloadfassungen; gerichtsleitende Dateien sind ebenfalls einzeln erfasst. |
| Vorlage zu einem bestimmten Rechtsgebiet | [Rechtsgebiete und Dokumenttypen](#rechtsgebiete-und-dokumenttypen) | Einstieg über Arbeitsrecht, Erbrecht, Sozialrecht und 38 weitere Praxisfelder. |
| Vertrag, Klage, Antrag, Formular oder Arbeitshilfe | [Drei-Ordner-Sicht](kategorien/) | Vollständiger Index aller 981 Hauptvorlagen, zuerst nach Dokumenttyp und danach nach Rechtsgebiet geordnet. |
| Klage, Erwiderung, Replik oder Eilrechtsschutz als zusammenhängender Verfahrensgang | [Prozesspakete](prozessvorlagen/) | Grundarchitekturen für Zivil-, Arbeits-, Verwaltungs-, Finanz-, Sozial- und Familienverfahren. |
| Gerichtliche, staatsanwaltschaftliche oder amtsanwaltschaftliche Schrift | [Gerichtsleitender Gesamtindex](vorlagen-gerichtsleitend/INDEX.md) | 113 Markdown-Vorlagen für Verfügungen, Beschlüsse, Tenorentwürfe und staatsanwaltschaftliche Arbeit; [Einzeldownloads stehen im Gesamtindex](DOWNLOADS.md#gerichtsleitender-sonderbereich). |
| Bestimmte Datei oder bestimmter Begriff | [Dateisuche auf `main`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/docs/experimentell/vorlagensammlung-recht) | Dateinamen durchsuchen; für Volltextsuche das Repository klonen und `rg` verwenden. |
| Pflege-, Prüf- oder Releaseablauf | [WORKFLOWS.md](WORKFLOWS.md) | Kurzer Arbeitszettel für Nutzung, Änderung, Qualitätsgate und Veröffentlichung. |

Jeder Rechtsgebietsordner führt zu einer Tabelle seiner Vorlagen. Der Link einer Vorlage öffnet deren eigene `README.md`; dort stehen Anwendungsbereich, Einsatzgrenzen, Normenanker und die beiden Direktdownloads. Wer den Namen bereits kennt, springt stattdessen unmittelbar in den [Schnellzugriff des Gesamtindex](DOWNLOADS.md#schnellzugriff). Dadurch bleibt der Weg stets gleich: **Rechtsgebiet, Dokumenttyp oder Gesamtindex wählen → Vorlage öffnen → README prüfen → ODT oder Markdown-ZIP herunterladen.** Der Gesamtindex enthält Rücksprünge nach jedem Rechtsgebiet; `Strg+F` oder `Cmd+F` findet Vorlagennamen und Stichwörter ohne Scrollen.

### Downloads

**Einzelne Datei online:** Im [Gesamtindex](DOWNLOADS.md#schnellzugriff) das Rechtsgebiet wählen. Bei Hauptvorlagen führt der Titel zuerst zur fachlichen README; daneben stehen ODT und Markdown-ZIP als unmittelbare Downloads. Im [Sonderbereich](DOWNLOADS.md#gerichtsleitender-sonderbereich) stehen Vorschau und unveränderter Markdown-Download nebeneinander.

**Gesamten Bestand offline:** Eines der folgenden Komplettpakete herunterladen und entpacken. Jedes Paket enthält im Wurzelverzeichnis eine `index.html`. Sie arbeitet ohne Installation und ohne Netzwerkzugriff, verknüpft mehrere Suchwörter unabhängig von ihrer Reihenfolge und filtert zusätzlich nach Rechtsgebiet und Dokumenttyp. Die Suche erfasst neben Titel und Dateipfad auch verdichtete Fachbegriffe aus Anwendungsbereich, Normen, Risiken und taktischen Hinweisen. Umlaute und ASCII-Umschriften führen zum selben Treffer; `/` setzt den Fokus in die Suche und `Escape` leert aktive Filter. Versionsstand und Dateizahl stehen sichtbar im Kopf. Der Vorlagentitel öffnet die fachlichen Hinweise, „Datei öffnen“ unmittelbar die Arbeitsdatei. Arbeitsabläufe, Beitragsregeln, Rechtsstandsprüfpfad und weitere Referenzdokumente liegen ebenfalls im Paket. Für Kanzleisoftware und eigene Auswertungen enthält jedes Paket außerdem ein UTF-8-kodiertes `manifest.json` mit Version, Titel, Rechtsgebiet, Dokumenttyp, Dateipfad, README-Pfad, Dateigröße und SHA-256-Prüfsumme jeder Arbeitsdatei. Wer einen dauerhaft reproduzierbaren Stand benötigt, verwendet die Assets eines konkreten Tags statt des Verweises auf `latest`.

- **Alle ODT-Arbeitsfassungen:** [ODT-Komplettpaket der neuesten Veröffentlichung herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-odt.zip). Das Paket enthält editierbare Bürofassungen, den filterbaren Offline-Index und das Maschinenmanifest.
- **Alle Markdown-Hauptvorlagen:** [Markdown-Komplettpaket der neuesten Veröffentlichung herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-markdown.zip). Das Paket enthält die prüfbaren Quellen, ihre READMEs, den filterbaren Offline-Index und das Maschinenmanifest.
- **Gerichtsleitender Sonderbereich:** [Alle gerichtlichen und staatsanwaltschaftlichen Markdown-Vorlagen herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagen-gerichtsleitend-markdown.zip). Auch dieses Paket enthält `index.html` und `manifest.json`.
- **Prüfsummen kontrollieren:** [`SHA256SUMS.txt` der neuesten Veröffentlichung herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/SHA256SUMS.txt).
- **Einzelne Vorlage bearbeiten:** In der README der Vorlage auf „ODT herunterladen“ klicken. Die ODT-Datei ist die editierbare Bürofassung.
- **Markdown zuverlässig herunterladen:** Den Link „Markdown (ZIP) herunterladen“ verwenden. GitHub zeigt rohe Markdown-Dateien häufig nur im Browser an; die ZIP-Fassung erzwingt den Download und enthält genau die gleichnamige `.md`-Datei.
- **Vor dem Download ansehen:** Die Links „Vorschau im Repository“ öffnen ODT und Markdown am kanonischen Speicherort.
- **Gesamte Sammlung herunterladen:** [`main` als ZIP-Archiv herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-gesamt.zip). Das Archiv enthält alle versionskontrollierten Vorlagen, ODT-Dateien, Markdown-ZIPs, READMEs und Prüfskripte des aktuellen Hauptstands.
- **Veröffentlichten Stand verwenden:** [Komplettpakete und Prüfsummen öffnen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/docs/experimentell/vorlagensammlung-recht/dist). Diese Kopie ist öffentlich zugänglich; das Quellrepository bleibt unverändert.

### Welche Fassung passt?

| Arbeitsweise | Empfohlener Einstieg |
| --- | --- |
| Einzelne Vorlage in LibreOffice oder Word bearbeiten | ODT-Link in der Vorlagen-README oder im [Gesamtindex](DOWNLOADS.md) |
| Einzelne Vorlage versionieren, vergleichen oder automatisiert prüfen | Markdown-ZIP-Link in der Vorlagen-README oder im [Gesamtindex](DOWNLOADS.md) |
| Gesamten Kanzleibestand offline in Office bereitstellen | [ODT-Komplettpaket](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-odt.zip) |
| Gesamte Quellenfassung offline durchsuchen | [Markdown-Komplettpaket](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-markdown.zip) |
| Bestand in Kanzleisuche, Skript oder Dokumentenmanagement einlesen | `manifest.json` im passenden Komplettpaket |
| Repository entwickeln, Validatoren ausführen oder Historie prüfen | [`main`-Archiv](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-gesamt.zip) oder Git-Klon |

## Worum es bei diesem Repo eigentlich geht

Dieses Repo ist mindestens so sehr ein Experiment und Werkzeugkasten wie eine Vorlagensammlung. Es zeigt, wie sich mit klaren Strukturvorgaben, wiederholten Redaktionsschleifen und harten Validatoren eine große Familie ordentlich strukturierter Dokumente zu vielen Rechtsgebieten aufbauen lässt, ohne immer wieder bei Null anzufangen und ohne dass die Qualität in der Fläche zerläuft.

Wer sich selbst in seinem Metier viele Vorlagen schaffen will, kann dieses Repo klonen und als Gerüst nutzen. Mitgeliefert sind nicht nur die Vorlagen, sondern auch die Mechanismen drumherum, die das Erzeugen, das Pflegen und das mehrstufige Verbessern über viele Dokumente hinweg überhaupt erst tragbar machen:

- Strukturvorgaben je Vorlage (Anwendungsbereich, Pflichtangaben, Mustertext mit Platzhaltern, Hinweise zur Verwendung), durchgängige Dezimalgliederung, einheitliche Tonalität.
- Konventionen für Dateinamen und Slugs (ASCII), Fließtext (echte Umlaute), Anführungszeichen, Paragrafenschreibung sowie die Trennung zwischen Hauptbestand und gerichtsleitendem Sonderbereich.
- Validatoren als CI-Checks, die diese Konventionen automatisch durchsetzen (`validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`).
- Eval-Harness (`run-eval`), das jede Vorlage gegen ein Rubric prüft und einen All-Pass-Score über den gesamten Bestand liefert; ein eigener Testakten-Korpus kontrolliert dabei sämtliche deklarativen Checktypen und wichtige Fehlerfälle des Harness.
- Skripte für Pflege und Massenarbeit: `md-to-odt.py`, `build-md-zips.py`, `build-download-index.py`, `build-release-assets.py`, `check-all.py` und Hygiene-Sweeps.
- Eine automatisch erzeugte, zweisprachige Erstseiten-Fußzeile kennzeichnet jede ODT-Arbeitsfassung als KI-generiertes experimentelles Dokument zur Benutzung auf eigene Gefahr und eigenes Risiko; die Integritätsprüfung verhindert fehlende, doppelte oder auf Folgeseiten wiederholte Hinweise.
- Versionierung und Workflow über Pull Requests, Codex-Review und Admin-Merge.

Mit diesem Gerüst lassen sich eigene Vorlagen mit eigenen Elementen, eigenem Wissen, eigenen Rechtsprechungsankern und eigenen Bausteinen aufsetzen — selbstverständlich datenschutz- und urheberrechtskonform. Es geht hier nicht um eine bloße Vorlagentankstelle, sondern um den Nachweis, dass eine fachlich saubere, formal konsistente Vorlagenfamilie tragfähig bleibt, wenn Strukturvorgaben, Validatoren, Quellenhygiene und redaktionelle Disziplin zusammenspielen.

Dazu noch eine ehrliche Einordnung: Die Vorlagen in diesem Repo sind strukturierte Textdokumente mit eckigen Platzhaltern. Sie sind kein Formularsystem mit Textfeldern, das sich aus einem Datenmodell selbst befüllt, sondern werden bewusst gelesen, geprüft und manuell ausgefüllt. Dafür ist der Einstieg niedrigschwellig und der Ansatz portabel: Markdown, ODT, ZIP, eine Handvoll Validatoren, und läuft überall.

## Bitte zuerst lesen

Diese Sammlung enthält unverbindliche Muster. Es handelt sich nicht um Rechtsberatung, nicht um Empfehlungen für einen konkreten Fall und nicht um geprüftes Vertragswerk. Jede Vorlage ist ein Anregungs- und Diskussionsbeitrag, der vor jedem Einsatz im Einzelfall geprüft, an den konkreten Sachverhalt angepasst und durch eine fachkundige Person freigegeben werden muss.

Eine Haftung des Autors für Inhalte, Aktualität, Vollständigkeit oder Eignung der Vorlagen für einen konkreten Zweck ist ausgeschlossen, soweit gesetzlich zulässig. Volltext: siehe [DISCLAIMER.md](DISCLAIMER.md) und [RECHTLICHE-HINWEISE.md](RECHTLICHE-HINWEISE.md).

Verbesserungsvorschläge, Korrekturen und neue Muster sind ausdrücklich willkommen — siehe [CONTRIBUTING.md](CONTRIBUTING.md).

## Eine Vorlage verwenden

Vor dem Ausfüllen ist die README der konkreten Vorlage zu lesen. Danach wird die ODT-Arbeitsfassung geöffnet oder die Markdown-Quelle für einen versionskontrollierten Arbeitsablauf verwendet. Eckige Platzhalter werden bewusst ersetzt oder gestrichen. Wer eine Vorlage ändert, bearbeitet die Markdown-Fassung, erzeugt bei Hauptvorlagen die ODT-Fassung neu, baut die Markdown-ZIP neu und lässt anschließend den vollständigen lokalen Gate laufen:

```bash
python3 scripts/check-all.py
```

Der Sammellauf führt die neun nur lesenden Prüfungen standardmäßig mit vier parallelen Prozessen aus. Im zehnten Schritt laufen die Testakten des Eval-Harness und die vollständige Rubric-Bewertung parallel. Die Standardausgabe meldet nur Zusammenfassung und Fehler; `python3 scripts/run-eval.py --verbose` zeigt bei Bedarf zusätzlich jede erfolgreiche Vorlage. Für Fehlersuche oder Laufzeitvergleiche erzwingt `python3 scripts/check-all.py --jobs 1` eine serielle Ausführung der ersten neun Prüfungen.

Der kompakte Arbeitszettel für Finden, Benutzen, Ändern, Neuanlage, Sonderbereich und Release steht in [WORKFLOWS.md](WORKFLOWS.md).

Für die tägliche Arbeit gilt eine einfache Reihenfolge:

1. Die `README.md` der konkreten Vorlage klärt zuerst, ob der Dokumenttyp passt.
2. Die ODT-Fassung ist die lesbare Büroarbeitsfassung für Entwurf, Prüfung und Abstimmung.
3. Die Markdown-Fassung bleibt die Quelle für Änderungen, Versionsvergleich und automatisierte Prüfung.
4. Die ZIP-Datei ist nur die portable Markdown-Mitnahme, nicht die führende Bearbeitungsfassung.
5. Rechtsprechungsanker bleiben Rechercheanker, bis sie in einer amtlichen oder anerkannten Quelle für den konkreten Fall geprüft sind.

Für kurze Rechtsstandsprüfungen gibt es zusätzlich den Arbeitszettel
[Rechtsstands-Sanity-Check](references/rechtsstands-sanity-check.md). Er
beschreibt, wie veraltete Normbezüge, Formanforderungen, Übergangsregeln und
Rechtsprechungsanker gezielt geprüft werden, ohne gute Vorlagen durch
mechanische Ersetzungen zu verschlechtern.

Der aus dem Quellbestand übernommene [Rechtsprechungsaudit vom August 2026](references/rechtsprechungsaudit-2026.md) beschreibt den damaligen Bestand von 954 Hauptvorlagen und 113 Sondervorlagen. Er ist ein historischer Bericht und keine Bestätigung des heutigen Gesamtbestands. Der [Abgleich vom 9. Oktober 2026](references/rechtsstandsabgleich-2026-10-09.md) dokumentiert neu gefundene Fehler, konkrete Korrekturen und die Grenzen der erneuten Prüfung.

## Rechtsgebiete und Dokumenttypen

Die Sammlung ist nach 41 Rechtsbereichen geordnet, die sich an klassischen Spezialisierungsfeldern und zusätzlichen Praxisfeldern orientieren — ohne berufsrechtlich geschützte Bezeichnungen zu verwenden.

Zusätzlich gibt es eine Drei-Ordner-Sicht nach Dokumenttyp. Diese
Ordner sind Inhaltsverzeichnisse, keine zweite Ablage der Dateien:

| Sicht | Inhalt | Anzahl |
|---|---|---:|
| [Vertragliche Vorlagen](kategorien/01-vertragliche-vorlagen/) | Verträge, Satzungen, AGB, Vollmachten, Sicherheiten und Vergleiche | 365 |
| [Prozessuale Vorlagen und Formulare](kategorien/02-prozessuale-vorlagen-und-formulare/) | Klagen, Anträge, Rechtsmittel, Widersprüche, Formulare und Verfahrensdokumente | 512 |
| [Sonstige Vorlagen](kategorien/03-sonstige-vorlagen/) | Vermerke, Pläne, Prüfpapiere, Risikomatrizen und weitere Arbeitshilfen | 104 |

Die kanonische Ablage bleibt der jeweilige Rechtsgebietsordner. Dort liegen
README, Markdown, Markdown-ZIP, ODT und Rubric; die Drei-Ordner-Sicht verweist
nur auf diese Originalorte.

Als vierter, technisch getrennter Arbeitsbereich steht
[`vorlagen-gerichtsleitend/`](vorlagen-gerichtsleitend/) bereit. Dieser Ordner
enthält gerichtsleitende sowie staatsanwaltschaftliche und
amtsanwaltschaftliche Schriftvorlagen für Verfügungen, Beschlüsse,
Tenor-Entwürfe, Ladungen, Hinweise, Anklageschriften, Einstellungs- und
Abschlussverfügungen, Strafbefehlsanträge, Beweisanträge, Rechtsmittel,
Plädoyergerüste und Begründungsskelette. Er ist Markdown-only, steht für
sich und wird mit `scripts/check-gerichtsleitend.py` gesondert geprüft.
Stand: 113 Vorlagen in 18 Bereichen einschließlich Familiengericht,
staatsanwaltschaftlicher sowie amtsanwaltschaftlicher Bereiche.

| Bereich | Ordner |
|---|---|
| AGB-Recht | [`agb-recht/`](agb-recht/) |
| Allgemeines und Bereichsübergreifendes | [`allgemeines-und-bereichsuebergreifendes/`](allgemeines-und-bereichsuebergreifendes/) |
| Arbeitsrecht | [`arbeitsrecht/`](arbeitsrecht/) |
| Aufsichtsrecht, BaFin und europäische Aufsichtsbehörden | [`aufsichtsrecht-und-bafin/`](aufsichtsrecht-und-bafin/) |
| Bank- und Kapitalmarktrecht | [`bank-und-kapitalmarktrecht/`](bank-und-kapitalmarktrecht/) |
| Bau- und Architektenrecht | [`bau-und-architektenrecht/`](bau-und-architektenrecht/) |
| Beamten-, Soldaten- und Wehrrecht | [`beamten-und-soldatenrecht/`](beamten-und-soldatenrecht/) |
| Energierecht | [`energierecht/`](energierecht/) |
| Erbrecht | [`erbrecht/`](erbrecht/) |
| Europarecht | [`europarecht/`](europarecht/) |
| Familienrecht | [`familienrecht/`](familienrecht/) |
| Gewerblicher Rechtsschutz | [`gewerblicher-rechtsschutz/`](gewerblicher-rechtsschutz/) |
| Handels- und Gesellschaftsrecht | [`handels-und-gesellschaftsrecht/`](handels-und-gesellschaftsrecht/) |
| Informationstechnologierecht | [`informationstechnologierecht/`](informationstechnologierecht/) |
| Insolvenzrecht | [`insolvenzrecht/`](insolvenzrecht/) |
| Internationales Wirtschaftsrecht | [`internationales-wirtschaftsrecht/`](internationales-wirtschaftsrecht/) |
| Kartell- und Marktrecht | [`kartell-und-marktrecht/`](kartell-und-marktrecht/) |
| KI- und Plattformregulierung | [`ki-und-plattformregulierung/`](ki-und-plattformregulierung/) |
| Medizinrecht | [`medizinrecht/`](medizinrecht/) |
| Mergers and Acquisitions | [`mergers-and-acquisitions/`](mergers-and-acquisitions/) |
| Mietrecht und Wohnungseigentumsrecht | [`mietrecht-und-wohnungseigentumsrecht/`](mietrecht-und-wohnungseigentumsrecht/) |
| Migrationsrecht | [`migrationsrecht/`](migrationsrecht/) |
| Öffentliches Baurecht | [`oeffentliches-baurecht/`](oeffentliches-baurecht/) |
| Prozessvorlagen | [`prozessvorlagen/`](prozessvorlagen/) |
| Restrukturierungsrecht und StaRUG | [`restrukturierungsrecht-starug/`](restrukturierungsrecht-starug/) |
| Sozialrecht | [`sozialrecht/`](sozialrecht/) |
| Sportrecht | [`sportrecht/`](sportrecht/) |
| Steuerrecht | [`steuerrecht/`](steuerrecht/) |
| Strafrecht | [`strafrecht/`](strafrecht/) |
| Strafvollzugsrecht | [`strafvollzugsrecht/`](strafvollzugsrecht/) |
| Transport- und Speditionsrecht | [`transport-und-speditionsrecht/`](transport-und-speditionsrecht/) |
| Umweltrecht und Emissionshandel | [`umweltrecht-und-emissionshandel/`](umweltrecht-und-emissionshandel/) |
| Urheber- und Medienrecht | [`urheber-und-medienrecht/`](urheber-und-medienrecht/) |
| Vergaberecht | [`vergaberecht/`](vergaberecht/) |
| Verkehrsrecht | [`verkehrsrecht/`](verkehrsrecht/) |
| Verwaltungsrecht | [`verwaltungsrecht/`](verwaltungsrecht/) |
| Versicherungsrecht | [`versicherungsrecht/`](versicherungsrecht/) |
| Vertriebs- und Handelsrecht | [`vertriebs-und-handelsrecht/`](vertriebs-und-handelsrecht/) |
| Verfassungsrecht | [`verfassungsrecht/`](verfassungsrecht/) |
| Weltraumrecht | [`weltraumrecht/`](weltraumrecht/) |
| Zoll- und Außenwirtschaftsrecht | [`zoll-und-aussenwirtschaftsrecht/`](zoll-und-aussenwirtschaftsrecht/) |

## Aufbau einer Vorlage

Jede Vorlage liegt in einem eigenen Unterordner ihres Themenbereichs und enthält:

```
<themenbereich>/<vorlagen-slug>/
  <vorlagen-slug>.md     Bearbeitbare Markdown-Fassung
  <vorlagen-slug>.md.zip Direktdownload der Markdown-Fassung
  <vorlagen-slug>.odt    Editierbare ODT-Bürofassung
  README.md               Menüseite mit Downloads, Vorschau und Hinweisen
  rubric.yaml             Prüfkriterien für den Eval-Harness
```

Die Vorlagedateien tragen denselben sprechenden Dateistamm wie ihr Vorlagenordner. Im Ordner `grundschuldbestellung-notariell/` liegen also `grundschuldbestellung-notariell.md` und `grundschuldbestellung-notariell.odt`, nicht `vertrag.md`, `text.odt`, `vorlage.md` oder ein sonstiger generischer Name.

Ausnahme: Der Sonderbereich `vorlagen-gerichtsleitend/` enthält keine
Kanzlei- oder Mandatsvorlagen, sondern gerichtsleitende Markdown-Bausteine.
Dort gibt es keine ODT-, ZIP- oder Rubric-Pflicht; stattdessen gelten die
Sonderregeln des eigenen Validators.

Direktdownload-Links in den Vorlagen-READMEs werden ebenfalls kurz und sprechend nach dem konkreten Dokument beschriftet, etwa „Rahmenliefervertrag B2B – ODT herunterladen“ oder „AGB Online-Shop B2C – Markdown (ZIP) herunterladen“. Linktext und Dateiname dürfen nie nur `vertrag`, `text`, `VORLAGE`, `SkillMD` oder ähnlich generisch sein.

Sowohl die Markdown- als auch die ODT-Version beginnen nur mit einem kurzen Hinweis auf Experiment, Unverbindlichkeit, eigene Prüfung und README. Der ausführliche Vorspruch mit Haftungs-, Berufsrechts-, Strafrechts-, Datenschutz- und Lizenzhinweisen steht in der jeweiligen `README.md` der Vorlage. Anwendungsbereich, Einsatzgrenzen, Normen- und Quellenanker sowie Downloadlinks stehen ebenfalls dort.

Die ODT-Fassungen sind seit v4.60.0 bewusst luftiger gesetzt: mehr Zeilenhöhe, stärkere Absatzabstände, ruhigere Listen und besser lesbare Tabellen. Breite Berechnungs-, Bewertungs- und Anlagenmatrizen wechseln abhängig von Spalten- und Zeilenzahl in A4-Querformat; der Integritätscheck gleicht dieses Seitenprofil mit der Markdown-Quelle ab. Diese Gestaltung soll die Arbeit am Bildschirm und im Ausdruck erleichtern; fachlich führend bleibt dennoch immer die Markdown-Quelle, aus der die ODT-Datei erzeugt wird.

Die Gliederung in jeder Vorlage folgt dauerhaft und ausnahmslos der
dezimalen Form `1`, `1.1`, `1.1.1`, `1.1.1.1` (verbindlich, siehe
[gliederung.md](references/gliederung.md)). Römische Ziffern,
Buchstabenebenen, Buchstaben-Zahlen-Mischungen und Verlagsstil-Gliederungen
sind nicht zulässig. Zwischen Gliederungspunkt und Inhalt steht eine
Leerzeile; Einrückung bleibt maßvoll.

## Beispiel — Paradevorlage

Asset Deal in kleinem Umfang im Insolvenzverfahren, mit ausführlichen Hinweisen in der README:

- [`asset-deal-klein-im-insolvenzverfahren/`](insolvenzrecht/asset-deal-klein-im-insolvenzverfahren/)

## Eval-Harness

Die Vorlagen werden automatisiert auf Vollständigkeit, Layout-Konformität,
Sprach- und Quellenhygiene geprüft. Aktueller Stand: 981 validierte
Hauptvorlagen, 113 gerichtsleitende Sondervorlagen und All-Pass 981/981
im Eval-Harness (siehe [EVAL_RESULTS.md](EVAL_RESULTS.md)). Der
Testakten-Korpus unter [`tests/testakten/`](tests/testakten/) stellt sicher,
dass keine dokumentierte Checkart nur auf dem Papier existiert und kein
Themenordner unbemerkt aus der Evaluation fällt.

Lokal nachvollziehen:

```
python3 scripts/check-all.py
```

Einzelchecks, wenn ein Fehler eingegrenzt werden soll:

```
python3 scripts/validate-vorlagen.py
python3 scripts/check-kategorien-index.py
python3 scripts/check-gerichtsleitend.py
python3 scripts/check-umlauthygiene.py
python3 scripts/check-rechtsprechungshygiene.py
python3 scripts/build-md-zips.py
python3 scripts/check-md-zip-integrity.py
python3 scripts/check-odt-integrity.py
python3 scripts/check-odt-spaltenlayout.py
python3 scripts/check-gliederung.py
python3 scripts/run-eval.py --report
# optional mit sämtlichen PASS-Zeilen:
python3 scripts/run-eval.py --verbose
```

Für Modellvergleiche, LLM-Judges und das Schema der `rubric.yaml` siehe
[CLAUDE](CLAUDE.md), [kautelarstandard.md](references/kautelarstandard.md),
[gegenstandsindividualisierung.md](references/gegenstandsindividualisierung.md),
[zitierweise.md](references/zitierweise.md),
[Prüfquellen.md](references/pruefquellen.md),
[Rechtsprechungsaudit 2026](references/rechtsprechungsaudit-2026.md),
[Rechtsprechungsradar amtliche Prüfanker.md](references/rechtsprechungsradar-amtliche-pruefanker.md)
und [Leitentscheidungen anker.md](references/leitentscheidungen-anker.md).

## Lizenz

Diese Sammlung ist unter zwei freien Lizenzen wahlweise verfügbar. Nutzer können frei wählen, unter welcher der beiden Lizenzen sie eine Vorlage übernehmen, weiterbearbeiten und verbreiten wollen:

- Apache-2.0 — siehe [LICENSE-APACHE](LICENSE-APACHE)
- MIT — siehe [LICENSE-MIT](LICENSE-MIT)

Dieses Dual-License-Setup folgt der Konvention des Rust-Ökosystems: maximale Anschlussfähigkeit, keine Hindernisse für Einbindung in eigene Projekte.

## Warum dieses Repository überhaupt?

Diese Sammlung ist auch ein Experiment — ein Versuch zu zeigen und zu untersuchen, was es bedeutet, wenn sich juristische Vorlagen mit Sprachmodellen in hoher Dichte und vertretbarer Qualität erzeugen lassen.

Die Frage dahinter ist nicht technisch, sondern berufsethisch und berührt das Selbstverständnis der freien Advokatur:

- Kränkung? Ist die Maschine, die in Sekunden einen tragfähigen Vertragsentwurf oder einen ordentlichen Schriftsatzkopf liefert, eine Kränkung des anwaltlichen Schreibens, das traditionell als höchstpersönliche, durch jahrelange Übung geformte Leistung verstanden wird?
- Stärkung? Oder ist es umgekehrt eine Stärkung anwaltlicher Unabhängigkeit — weil das Routinegestell endlich kein Engpass mehr ist und die rechtliche Prüfung, die Tatsachenarbeit und das Mandantengespräch ins Zentrum rücken können, also genau das, wofür Anwälte ausgebildet sind?
- Demokratisierung? Oder ist es eine Form von Egalitarismus: Wer bisher keinen Zugang zu einer gut gepflegten Kanzleibibliothek hatte, bekommt einen Startpunkt, der nicht hinter dem zurückbleibt, was in vielen Kanzleien tatsächlich seit Jahren auf der Festplatte, in Outlook-Entwürfen oder in einer E-Akte herumgereicht wird?

Das Problem der Überarbeitung und der Korrektheit bleibt selbstverständlich — keine Vorlage hier ersetzt anwaltliche Prüfung am konkreten Mandat. Aber ehrlicherweise: Der Vergleichsmaßstab sind nicht abstrakte Idealvorlagen, sondern die tatsächlich verwendeten Bestandstemplates, die in vielen Kanzleien jahrelang ungepflegt mitlaufen, Rechtsprechungsständen von 2017 entsprechen und Klauseln zitieren, die längst durch Reformen ausgehöhlt sind. Gegen diesen Maßstab schneidet sorgfältig generiertes und disziplinierbar gepflegtes Material häufig nicht schlechter, sondern in Aktualität und Vollständigkeit überraschend oft besser ab.

Die Antwort, die das Repository auf diese Spannung gibt, ist nicht theoretisch, sondern praktisch:

1. Vorlagen sind Gerüst, kein Endprodukt. Jeder Kurz-Hinweis sagt es, jede README führt es aus: Verwendung auf eigene Gewähr und auf eigene Gefahr, anwaltliche Endprüfung zwingend.
2. Prüfbarkeit statt Vertrauen. Der Eval-Harness (`scripts/run-eval.py`) macht Qualität messbar: Jede Vorlage trägt die Struktur- und Hygiene-Baseline, vorlagenspezifische Rubrics ergänzen fachliche Pass/Fail-Kriterien; zwei `human_review`-Marker halten Aktenzeichen-Verifikation und Endprüfung durch Berufsträger sichtbar. Testakten prüfen Checktypen, Rubric-Schema und vollständige Themenabdeckung vor jeder Gesamtbewertung.
3. Quellenhygiene statt Scheingenauigkeit. Konkrete Entscheidungen sind nur Rechercheanker, solange sie nicht in den amtlichen oder primären Quellen nach [Prüfquellen.md](references/pruefquellen.md) live geprüft wurden.
4. Endprüfung außerhalb der Vorlage. Vertragsarchitektur, Schriftsatzarchitektur, Form, Vollzug, Beweis, Anlagen, Sprachvorrang und Quellenprüfung werden nicht als generische Checkliste im Vorlagentext verankert, sondern als mandatsbezogene Prüfung in der Akte oder im Skill durchgeführt. Damit bleiben die Vorlagen schlank und auf den konkreten Sachverhalt zuschneidbar.
5. Offen und teilbar. Die Sammlung steht unter Apache-2.0 oder MIT, ohne Vertriebsmodell, ohne Lock-in. Wer sie verbessert, verbessert sie für alle.

Was dieses Repository nicht ist: ein Ersatz für juristische Arbeit, eine Garantie für Mandatssicherheit oder ein Argument gegen die Notwendigkeit anwaltlicher Beratung. Was es sein möchte: ein ehrlicher Versuchsaufbau, mit dem sich diese Diskussion an konkretem Material und nicht an Spekulationen führen lässt.

## Hinweise nach Berufs-, Straf- und Datenschutzrecht

Wer als Berufsträger Mandatsunterlagen in eine Vorlage übernimmt oder eine ausgefüllte Vorlage in einer KI-Umgebung verarbeitet, beachtet insbesondere:

- § 43a Abs. 2 BRAO / § 2 BORA — Verschwiegenheitspflicht: Personenbezogene und mandatsbezogene Inhalte vor Verarbeitung anonymisieren oder verschlüsseln.
- § 203 Abs. 1 Nr. 3 StGB — Strafbarkeit der Offenbarung fremder Geheimnisse: Drittdienste nur einsetzen, wenn die Voraussetzungen des § 203 Abs. 3 und 4 StGB (mitwirkende Personen, Verschwiegenheitsverpflichtung) gewahrt sind.
- DSGVO Art. 5, 6, 28 — Rechtsgrundlage und Auftragsverarbeitung: Bei Einsatz eines KI-Dienstes Auftragsverarbeitungsvertrag prüfen, Datenkategorien und Löschkonzept dokumentieren.

Die jeweiligen Vorlagen verweisen im Kurz-Hinweis auf die ausführlichen README-Hinweise.

## Pausenkarte für lange Redaktionsläufe

Dieser Abschnitt gehört nicht zur juristischen Vorlagensammlung und ist weder Gesundheits- noch Produktempfehlung. Koffeingehalt, Zucker, Zutaten und individuelle Verträglichkeit unterscheiden sich erheblich; maßgeblich sind Produktkennzeichnung, persönliche Situation und gegebenenfalls ärztlicher Rat. Energy-Drinks und andere stark koffeinhaltige Getränke werden nicht mit Alkohol kombiniert und ersetzen weder Schlaf noch Pausen. Sachinformationen zu Koffein, Kennzeichnung und Risikogruppen bietet das [Bundesinstitut für Risikobewertung](https://www.bfr.bund.de/fragen-und-antworten/thema/fragen-und-antworten-zu-koffein-und-koffeinhaltigen-lebensmitteln-einschliesslich-energy-drinks/).

| Getränkefamilie | Beispiele für die Redaktionspause |
| --- | --- |
| Espresso und kurze Kaffees | Ristretto, Espresso, Doppio, Espresso macchiato und Mokka |
| Verlängerte und gefilterte Kaffees | Americano, Filterkaffee, Café Crema, Handfilter, French Press und Cold Brew |
| Kaffee mit Milch oder Pflanzendrink | Cappuccino, Flat White, Caffè Latte, Latte macchiato und Café au lait |
| Tee mit natürlichem Koffein | schwarzer Tee, Earl Grey, grüner Tee, weißer Tee, Oolong, Matcha, Chai und Mate-Tee |
| Mate, Guarana und Cola | Mate-Limonade, Guarana-Getränke, klassische Cola, zuckerfreie Cola und koffeinhaltige Cola-Mischgetränke ohne Alkohol |
| Energy-Drinks und Energy-Shots | Red Bull, Monster, Rockstar, Effect und vergleichbare koffeinhaltige Produkte; Marken sind ausschließlich Beispiele und keine Wertung |
| Warm, aber ohne Koffein | Rooibos, Pfefferminztee, Ingweraufguss, Früchtetee, heiße Zitrone, Kakao und warme Milch- oder Pflanzendrinks |
| Kühl und ohne Koffein | Mineralwasser, Saftschorle, alkoholfreie Kräuterlimonade, Kokoswasser, alkoholfreies Ginger Beer und ungesüßter Eistee ohne Koffein |
| Für längere Termine | Karaffe Wasser, Trinkflasche oder die gute alte Thermoskanne mit Wasser; auf Wunsch mit Zitrone, Gurke, Beeren oder Minze |
