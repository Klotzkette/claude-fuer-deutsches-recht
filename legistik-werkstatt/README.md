# Legistik-Werkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`legistik-werkstatt`) | [`legistik-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Elektronisches Pflichtpostfach** (`legistik-pflichtpostfach`) | [Gesamt-PDF lesen](../testakten/legistik-pflichtpostfach/gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) | [`testakte-legistik-pflichtpostfach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Legistik-Werkstatt für Ministerien, Bundestag, Fraktionen/Opposition, Länder, Landtage und Normgeber. Baut Referenten- und Kabinettsentwürfe, Vorlagen aus der Mitte, Änderungs-/Entschließungsanträge, Rechtsverordnungen und Satzungen mit Begründung, Synopse, XML und Prüfpfaden.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`legistik-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/legistik-werkstatt/legistik-werkstatt-werkstatt.md" download><code>legistik-werkstatt-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/legistik-werkstatt/legistik-werkstatt-schnellstart.md" download><code>legistik-werkstatt-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Elektronisches Pflichtpostfach: [Gesamt-PDF](../testakten/legistik-pflichtpostfach/gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf), [`testakte-legistik-pflichtpostfach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip), [`testakte-legistik-pflichtpostfach-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Vollständige Werkstatt für Legistinnen und Legisten in Bundesministerien, Bundestag, Fraktionen, Oppositionsarbeit, Landesministerien, Landtagen sowie kommunalen und kammerlichen Normgebern. Vom politischen Auftrag über Startbahn, Normhierarchie, Kompetenzprüfung, Normenkartierung und Terminologie zu Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Rechtsverordnung und Satzung. Mit Querschnittsprüfungen Verfassungsrecht Europarecht Folgenabschätzung Goldplating Bestimmtheit Zirkelschluss. Erzeugt am Ende ein DOCX und PDF im passenden offiziellen Layout - ministerieller Referentenentwurf-Stil, BT-/Landtagsdrucksachen-Stil oder Arbeitsfassung für Fraktion, Ausschuss und Normgeber.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Was kann das Plugin?

Das Plugin deckt **alle Normebenen** ab:

- Bundesgesetz (Stammgesetz, Mantelgesetz, Änderungsgesetz)
- Landesgesetz
- Rechtsverordnung des Bundes und der Länder (Art. 80 GG, Landesverfassungen)
- Satzungen von Kommunen, Kammern und Hochschulen (Art. 28 Abs. 2 GG, Selbstverwaltung)
- Sekundärrechtsdurchführung und Notifizierung
- parlamentarischer Antrag, Entschließungsantrag, Änderungsantrag und Gesetzentwurf aus der Mitte des Bundestages oder Landtages

Das Plugin arbeitet mit **fünf Startbahnen**:

- Bundesressort / Bundesregierung: Referentenentwurf, Ressortabstimmung, NKR, Kabinett, Bundesrat, Bundestag
- Bundestag / Fraktion / Abgeordnete: Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Entschließungsantrag, Ausschussfassung
- Landesressort / Landesregierung: Landesreferentenentwurf, Landesverordnung, Kabinetts- und Landtagsweg
- Landtag / Landtagsfraktion: landesspezifischer Gesetzentwurf, Änderungsantrag, Antrag, Entschließungsantrag
- sonstiger Normgeber: kommunale Satzung, Kammerrecht, Hochschulsatzung, Beschlussvorlage, Bekanntmachung

Das Plugin prüft **immer**:

- Verfassungsrecht (GG, Landesverfassungen, BVerfG-Rechtsprechung)
- Europarecht (Primärrecht, Sekundärrecht, Notifizierung 2015/1535)
- Folgen (Erfüllungsaufwand, Bürokratiekosten, Nachhaltigkeit, KMU-Test)
- Goldplating und Wesentlichkeit
- Bestimmtheit, Terminologie und Zirkelschluss

Am Ende erzeugt es ein **lieferfertiges DOCX und PDF** im offiziellen Layout:

- **Referentenentwurf** (Arial 11pt, Bearbeitungsstand-Kopf, A-F-Vorblatt)
- **BT-Drucksache** (Times New Roman 11pt, Drucksachennummer + Wahlperiode in der Kopfzeile, Sperrsatz für Hauptüberschriften, Anschreiben des Bundeskanzlers)
- **Formulierungshilfe / parlamentarische Vorlage** (für Koalition, Opposition, Ausschuss oder Ministerialzulieferung)
- **Antrag / Entschließungsantrag** (beschlussreif, mit Begründung und Kurzvermerk)
- **Synopse** (dreispaltig)
- **Lesefassung** (konsolidiert nach Inkrafttreten)
- **Kabinettsmappe** (Deckblatt + Anlagenverzeichnis)

## Skill-Tabelle

| Phase | Skill | Zweck |
| --- | --- | --- |
| Auftrag | `legistik-auftragsaufnahme` | Startbahn, Institution, formalen Initiator und Regelungsauftrag übersetzen |
| Normhierarchie | `normhierarchie-routing` | Regierung vs Parlament; Gesetz vs Verordnung vs Satzung vs Antrag; Bund vs Land |
| Kompetenz | `gesetzgebungskompetenz-pruefen` | Art. 70 bis 74 GG, Erforderlichkeit |
| Kompetenz | `verordnungsermaechtigung-art80` | Inhalt Zweck Ausmass nach Art. 80 GG |
| Kompetenz | `satzungskompetenz-pruefen` | Art. 28 Abs. 2 GG, Kammern, Hochschulen |
| Mapping | `normenkartierung` | Verweisnetz und Änderungsstellen |
| Sprache | `terminologie-konsistenz` | Begriffsbrüche aufspüren |
| Sprache | `zirkelschluss-pruefen` | Verweisgraf zykelfrei |
| Entwurf | `referentenentwurf-bauen` | Vollformat des Bundes- oder Landes-Referentenentwurfs |
| Entwurf | `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Antrag oder Entschließungsantrag |
| Entwurf | `gesetzesentwurf-kabinett` | Kabinettsmappe |
| Entwurf | `begruendung-allgemein-und-besonders` | Teil A I-VII und Teil B |
| Entwurf | `synopse-erstellen` | Dreispaltige Synopse |
| Entwurf | `lesefassung-konsolidiert` | Konsolidierte Fassung nach Inkrafttreten |
| Entwurf | `xml-paralleldarstellung` | LegalDocML.de und eNorm |
| Prüfung | `europarechtskonformitaet` | Primärrecht Sekundärrecht Notifizierung |
| Prüfung | `goldplating-vermeiden` | Überschießende Umsetzung von Unionsrecht |
| Prüfung | `verfassungsmaessigkeit-quercheck` | Grundrechte Verhältnismäßigkeit Bestimmtheit |
| Folgen | `folgenabschaetzung-erfuellungsaufwand` | Erfüllungsaufwand quantifizieren |
| Folgen | `folgenabschaetzung-nachhaltigkeit` | SDGs Klima Generationengerechtigkeit |
| Inkrafttreten | `inkrafttreten-uebergangsrecht` | Zeitpunkt Übergang Verkündung |
| Beteiligung | `verbaendeanhoerung-ressortabstimmung` | Anhörung und Abstimmung |
| Beteiligung | `normenkontrollrat-kmu-check` | NKR-Stellungnahme einholen |
| Lieferung | `dokumente-rendern-docx-pdf` | DOCX und PDF im offiziellen Layout |
| Schulung | `schulung-legistik` | Trainerleitfaden für Schulungen |

Insgesamt **26 Skills**.

## Beispielprojekt - Pflichtpostfachgesetz

Das Repository enthält eine vollständige Arbeitsakte unter `testakten/legistik-pflichtpostfach/`. Sie simuliert den Weg von der politischen Vorgabe (Koalitionsvertrag) zum lieferfertigen Referentenentwurf eines neuen Stammgesetzes über das elektronische Pflichtpostfach für HReg-Gesellschaften und sehr große Online-Plattformen.

So erzeugen Sie die fertigen Dokumente:

```bash
cd claude-fuer-deutsches-recht
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output

python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format bt-drucksache \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```

Voraussetzung: `pip install python-docx pyyaml`. Für die PDF-Konvertierung zusätzlich LibreOffice (`soffice`).

## Disclaimer

Dieses Plugin ist ein Werkzeug zur Beschleunigung legistischer Arbeit. Es ersetzt nicht die juristische Prüfung durch verantwortliche Fachreferentinnen und Fachreferenten und nicht die Prüfung durch die Ressortleitung und das Bundesministerium der Justiz im Rahmen der Rechtsförmlichkeitsprüfung.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `kaltstart-triage`, `legistik-erstpruefung-und-mandatsziel`, `normhierarchie-routing`, `ressort-router`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `aenderungs-formular-portal-einreichungslogik`, `aenderungs-formular-portal-und-einreichung`, `baut-quellenkarte`, `bmds-datenrecht-und-data-act`, `bmvg-wehrrecht-und-soldatenstatus`, `chronologie-und-belegmatrix`, `dokumente-rendern-docx-pdf`, `fraktionen-dokumentenmatrix-lueckenliste`, `fraktionen-dokumentenmatrix-und-lueckenliste`, `kabinettsentwuerfe-compliance-dokumentation-und-akte`, `ministerien-tatbestand-beweis-und-belege`, `ministerien-tatbestandsmerkmale-beweisfragen`, `quellen-livecheck`, `spezial-aenderungs-formular-portal-und-einreichung`, `spezial-baut-livequellen-und-rechtsprechungscheck`, `unterlagen-luecken`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `bmf-steuerrecht-und-fiskalnormen`, `bmwe-aussenwirtschaft-und-investitionspruefung`, `bmwsb-bauproduktenrecht-und-technische-normen`, `erstpruefung-rollenklaerung`, `fristen-und-risikoampel`, `legistik-normenkartierung-aenderungsbefehle`, `legw-bmwe-aussenwirtschaft-und-investitionspruefung`, `normenkartierung-normenkontrollrat-kmu`, `normenkontrollrat-kmu-check`, `normgeber-verhandlung-vergleich-eskalation`, `normgeber-verhandlung-vergleich-und-eskalation`, `normtext-begruendung-synopse`, `normtext-begruendung-und-synopse`, `opposition-risikoampel-gegenargumente`, `opposition-risikoampel-und-gegenargumente`, `rmap-norm-zu-rulemap`, `rmap-tatbestand-und-rechtsfolge`, `verfassungsmaessigkeit-quercheck` |
| 4. Gestaltung, Strategie und Verhandlung | `aa-voelkerrecht-und-vertragsgesetzgebung`, `bmds-ki-verordnung-und-aufsichtsstruktur`, `bmg-krankenhaus-und-versorgungsstrukturrecht`, `bmg-krankenhaus-versorgungsstrukturrecht`, `bmwsb-bau-und-planungsrecht-baugb-baunvo`, `bmwsb-energetische-sanierung-und-geg` |
| 5. Verfahren, Behörde und Gericht | `aa-eu-bmi-verwaltungsverfahren`, `aa-eu-grundlagen-und-ratsverfahren`, `bmds-verwaltungsdigitalisierung-und-registermodernisierung`, `bmi-verwaltungsverfahren`, `bmi-verwaltungsverfahren-und-bundesverwaltung`, `bmjv-gerichtsverfassungs-prozessrecht`, `bmjv-gerichtsverfassungs-und-prozessrecht`, `bundestag-fristen-form-und-zustaendigkeit`, `bundestag-fristen-form-zustaendigkeit`, `gesetzgebungsverfahren-bauleiter`, `laender-behoerden-gerichts-registerweg`, `landtage-schriftsatz-brief-memo-bausteine`, `landtage-schriftsatz-brief-und-memo-bausteine`, `spezial-laender-behoerden-gericht-und-registerweg` |
| 6. Ergebnis, Schreiben und Kommunikation | `gesetzesentwurf-kabinett`, `gesetzesentwurf-kabinett-aa-voelkerrecht`, `legistik-kabinettsentwurf-ressortabstimmung`, `output-waehlen`, `referentenentwurf-bauen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `aa-ausfuhrkontrolle`, `aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension`, `entschliessungsantraege-fehlerkatalog`, `rmap-entscheidungsbaum-validierung`, `spezial-entschliessungsantraege-red-team-und-qualitaetskontrolle` |
| 8. Spezialmodule und Schnittstellen | `aa-konsular-bmas-arbeitsrecht`, `aa-konsular-und-passrecht`, `aa-sanktionsumsetzung-internationale`, `aa-sanktionsumsetzung-und-internationale-abkommen`, `begruendung-allgemein-und-besonders`, `bmas-arbeitsrecht-und-arbeitsschutz`, `bmas-arbeitsschutz-und-arbeitssicherheit`, `bmas-rente-und-altersvorsorgerecht`, `bmas-sozialversicherungsrecht-sgb`, `bmas-teilhabe-bmbfsfj-familien`, `bmas-teilhabe-schwerbehindertenrecht-sgb`, `bmbfsfj-familien-und-elterngeldrecht`, `bmbfsfj-gleichstellungs`, `bmbfsfj-gleichstellungs-und-antidiskriminierungsrecht`, `bmbfsfj-kinder-jugendhilferecht-sgb-viii`, `bmbfsfj-kinder-und-jugendhilferecht-sgb-viii`, `bmbfsfj-schul-und-berufsbildungsrecht`, `bmbfsfj-senioren-pflegevorbeugungsrecht`, ... plus 163 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 254 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aa-ausfuhrkontrolle` | Wenn es um Ausfuhrkontrolle und Aussenwirtschaftsdimension (AA) in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort... |
| `aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension` | Wenn es um Ausfuhrkontrolle und Aussenwirtschaftsdimension (AA) in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort... |
| `aa-eu-bmi-verwaltungsverfahren` | Wenn es um EU-Grundlagen und Ratsverfahren (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: A... |
| `aa-eu-grundlagen-und-ratsverfahren` | Wenn es um EU-Grundlagen und Ratsverfahren (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: A... |
| `aa-konsular-bmas-arbeitsrecht` | Wenn es um Konsularrecht und Passrecht (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Aa Ko... |
| `aa-konsular-und-passrecht` | Wenn es um Konsularrecht und Passrecht (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Aa Ko... |
| `aa-sanktionsumsetzung-internationale` | Wenn es um Sanktionsumsetzung und internationale Abkommen (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Ausw... |
| `aa-sanktionsumsetzung-und-internationale-abkommen` | Wenn es um Sanktionsumsetzung und internationale Abkommen (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Ausw... |
| `aa-voelkerrecht-und-vertragsgesetzgebung` | Wenn es um Voelkerrecht und Vertragsgesetzgebung (AA) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `aenderungs-formular-portal-einreichungslogik` | Wenn es um Änderungs: Formular, Portal und Einreichungslogik in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Aender... |
| `aenderungs-formular-portal-und-einreichung` | Wenn es um Änderungs: Formular, Portal und Einreichungslogik in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Aender... |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `baut-quellenkarte` | Wenn es um Baut Quellenkarte in Legistik-Werkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `begruendung-allgemein-und-besonders` | Wenn es um Begründung allgemein und besonders in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bmas-arbeitsrecht-und-arbeitsschutz` | Wenn es um Arbeitsrecht und Arbeitsschutz (BMAS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmas-arbeitsschutz-und-arbeitssicherheit` | Wenn es um Arbeitsschutz und Arbeitssicherheit (BMAS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmas-rente-und-altersvorsorgerecht` | Wenn es um Rente und Altersvorsorgerecht (BMAS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmas-sozialversicherungsrecht-sgb` | Wenn es um Sozialversicherungsrecht (SGB) (BMAS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmas-teilhabe-bmbfsfj-familien` | Wenn es um Teilhaberecht (SGB IX) (BMAS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Bmas Tei... |
| `bmas-teilhabe-schwerbehindertenrecht-sgb` | Wenn es um Teilhaberecht (SGB IX) (BMAS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Bmas Tei... |
| `bmbfsfj-familien-und-elterngeldrecht` | Wenn es um Familien- und Elterngeldrecht (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmbfsfj-gleichstellungs` | Wenn es um Gleichstellungs- und Antidiskriminierungsrecht (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen.... |
| `bmbfsfj-gleichstellungs-und-antidiskriminierungsrecht` | Wenn es um Gleichstellungs- und Antidiskriminierungsrecht (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen.... |
| `bmbfsfj-kinder-jugendhilferecht-sgb-viii` | Wenn es um Kinder- und Jugendhilferecht (SGB VIII) (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. Auswahlstichwort: Bmbfsfj Kin... |
| `bmbfsfj-kinder-und-jugendhilferecht-sgb-viii` | Wenn es um Kinder- und Jugendhilferecht (SGB VIII) (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. Auswahlstichwort: Bmbfsfj Kin... |
| `bmbfsfj-schul-und-berufsbildungsrecht` | Wenn es um Schul- und Berufsbildungsrecht (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmbfsfj-senioren-pflegevorbeugungsrecht` | Wenn es um Seniorenrecht und Pflegevorbeugung (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmbfsfj-senioren-und-pflegevorbeugungsrecht` | Wenn es um Seniorenrecht und Pflegevorbeugung (BMBFSFJ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmds-datenrecht-und-data-act` | Wenn es um Datenrecht und Data Act (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmds-digitale-verwaltung-ozg-und-egovg` | Wenn es um Digitale Verwaltung (OZG; EGovG) (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmds-it-ki-verordnung` | Wenn es um IT-Sicherheit (BSIG) (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Bmds It Ki... |
| `bmds-it-sicherheit-und-bsig` | Wenn es um IT-Sicherheit (BSIG) (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Bmds It Si... |
| `bmds-ki-verordnung-und-aufsichtsstruktur` | Wenn es um digitale Werkzeuge-Verordnung und Aufsichtsstruktur (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmds-verwaltungsdigitalisierung` | Wenn es um Verwaltungsdigitalisierung und Registermodernisierung (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. Auswahlstich... |
| `bmds-verwaltungsdigitalisierung-und-registermodernisierung` | Wenn es um Verwaltungsdigitalisierung und Registermodernisierung (BMDS) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. Auswahlstich... |
| `bmf-finanzmarktaufsicht-bafin-kwg-wpig` | Wenn es um Finanzmarktaufsicht (BaFin; KWG; WpIG) (BMF) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmf-geldwaesche-und-sanktionsrecht` | Wenn es um Geldwaescherecht und Sanktionsrecht (BMF) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmf-haushalts-und-zuwendungsrecht` | Wenn es um Haushaltsrecht und Zuwendungen (BMF) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmf-steuerrecht-und-fiskalnormen` | Wenn es um Steuerrecht und Fiskalnormen (BMF) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmf-zoll-und-aussenwirtschaftsrecht` | Wenn es um Zollrecht und Aussenwirtschaftsrecht (BMF) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmftr-biotechnologie-und-laborsicherheit` | Wenn es um Biotechnologie und Laborsicherheit (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmftr-forschungsfoerderung` | Wenn es um Forschungsfoerderung und Ressortforschung (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswah... |
| `bmftr-forschungsfoerderung-und-ressortforschung` | Wenn es um Forschungsfoerderung und Ressortforschung (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswah... |
| `bmftr-hochschul-und-wissenschaftsrecht` | Wenn es um Hochschulrecht und Wissenschaftsrecht (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmftr-kuenstliche-intelligenz` | Wenn es um Kuenstliche Intelligenz und Technikregulierung (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. A... |
| `bmftr-kuenstliche-raumfahrt` | Wenn es um Kuenstliche Intelligenz und Technikregulierung (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. A... |
| `bmftr-raumfahrt-und-weltraumrecht-wrgg` | Wenn es um Raumfahrt- und Weltraumrecht (BMFTR) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmg-arzneimittel-medizinprodukterecht` | Wenn es um Arzneimittel- und Medizinprodukterecht (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmg-arzneimittel-und-medizinprodukterecht` | Wenn es um Arzneimittel- und Medizinprodukterecht (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmg-berufsrecht-heilberufe-approbation` | Wenn es um Berufsrecht der Heilberufe und Approbation (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahl... |
| `bmg-berufsrecht-heilberufe-und-approbation` | Wenn es um Berufsrecht der Heilberufe und Approbation (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahl... |
| `bmg-infektionsschutz-und-pandemierecht` | Wenn es um Infektionsschutz und Pandemierecht (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmg-krankenhaus-und-versorgungsstrukturrecht` | Wenn es um Krankenhaus- und Versorgungsstrukturrecht (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmg-krankenhaus-versorgungsstrukturrecht` | Wenn es um Krankenhaus- und Versorgungsstrukturrecht (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmg-krankenversicherungs-leistungsrecht` | Wenn es um Krankenversicherungs- und Leistungsrecht (SGB V) (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. A... |
| `bmg-krankenversicherungs-und-leistungsrecht-sgb-v` | Wenn es um Krankenversicherungs- und Leistungsrecht (SGB V) (BMG) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. A... |
| `bmi-auslaender` | Wenn es um Ausländer- und Staatsangehoerigkeitsrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmi-auslaender-und-staatsangehoerigkeitsrecht` | Wenn es um Ausländer- und Staatsangehoerigkeitsrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmi-bevoelkerungsschutz` | Wenn es um Bevoelkerungsschutz und Katastrophenrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmi-bevoelkerungsschutz-oeffentlicher` | Wenn es um Bevoelkerungsschutz und Katastrophenrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmi-oeffentlicher-dienst-beamtenrecht` | Wenn es um Oeffentlicher Dienst und Beamtenrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmi-oeffentlicher-dienst-und-beamtenrecht` | Wenn es um Oeffentlicher Dienst und Beamtenrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmi-sicherheits-und-polizeirecht` | Wenn es um Sicherheits- und Polizeirecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmi-verwaltungsverfahren` | Wenn es um Verwaltungsverfahren und Bundesverwaltung (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmi-verwaltungsverfahren-und-bundesverwaltung` | Wenn es um Verwaltungsverfahren und Bundesverwaltung (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmjv-gerichtsverfassungs-prozessrecht` | Wenn es um Gerichtsverfassungs- und Prozessrecht (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswahlstichwort: Bmjv Gerichtsverfassungs P... |
| `bmjv-gerichtsverfassungs-und-prozessrecht` | Wenn es um Gerichtsverfassungs- und Prozessrecht (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. Auswahlstichwort: Bmjv Gerichtsverfassungs U... |
| `bmjv-rechtsstaatlichkeit-grundrechte` | Wenn es um Rechtsstaatlichkeit und Grundrechte-Querschnitt (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. A... |
| `bmjv-rechtsstaatlichkeit-und-grundrechte-querschnitt` | Wenn es um Rechtsstaatlichkeit und Grundrechte-Querschnitt (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. A... |
| `bmjv-straf-und-strafprozessrecht-pflege` | Wenn es um Straf- und Strafprozessrecht-Pflege (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmjv-verbraucherschutz-und-unlauterer-wettbewerb` | Wenn es um Verbraucherschutz und Wettbewerbsrecht (UWG) (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Ausw... |
| `bmjv-verbraucherschutz-unlauterer` | Wenn es um Verbraucherschutz und Wettbewerbsrecht (UWG) (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Ausw... |
| `bmjv-zivilrecht-buergerliches-gesetzbuch` | Wenn es um Zivilrecht und BGB-Pflege (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Bmjv... |
| `bmjv-zivilrecht-und-buergerliches-gesetzbuch-pflege` | Wenn es um Zivilrecht und BGB-Pflege (BMJV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstichwort: Bmjv... |
| `bmleh` | Wenn es um Legistik-Werkstatt — Allgemein in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bmleh-agrar-forst-jagdrecht` | Wenn es um Agrar- und Förderungsrecht (GAK; GAP) (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlsti... |
| `bmleh-agrar-und-foerderungsrecht-gak-gap` | Wenn es um Agrar- und Förderungsrecht (GAK; GAP) (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlsti... |
| `bmleh-forst-und-jagdrecht` | Wenn es um Forst- und Jagdrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmleh-lebensmittelrecht` | Wenn es um Lebensmittel- und Futtermittelrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmleh-lebensmittelrecht-und-futtermittelrecht` | Wenn es um Lebensmittel- und Futtermittelrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmleh-oekolandbau-pflanzenschutzrecht` | Wenn es um Oekolandbau und Pflanzenschutzrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmleh-oekolandbau-und-pflanzenschutzrecht` | Wenn es um Oekolandbau und Pflanzenschutzrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmleh-tierschutz-tiergesundheitsrecht` | Wenn es um Tierschutz- und Tiergesundheitsrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmleh-tierschutz-und-tiergesundheitsrecht` | Wenn es um Tierschutz- und Tiergesundheitsrecht (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmukn-abfall-kreislaufwirtschaftsrecht` | Wenn es um Abfall- und Kreislaufwirtschaftsrecht (BMUKN) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. Auswahlstichwort: Bmukn Abf... |
| `bmukn-abfall-und-kreislaufwirtschaftsrecht` | Wenn es um Abfall- und Kreislaufwirtschaftsrecht (BMUKN) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. Auswahlstichwort: Bmukn Abf... |
| `bmukn-atom-und-strahlenschutzrecht` | Wenn es um Atom- und Strahlenschutzrecht (BMUKN) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmukn-immissionsschutz-und-bimschg` | Wenn es um Immissionsschutz (BImSchG) (BMUKN) in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bmukn-naturschutz-und-artenschutzrecht` | Wenn es um Naturschutz- und Artenschutzrecht (BMUKN) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmukn-wasser-bmv-luft-mobilitaets` | Wenn es um Wasser- und Bodenschutzrecht (BMUKN) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. Auswahlstichwort: Bmukn Wasser Bmv Luft Mo... |
| `bmukn-wasser-und-bodenschutzrecht` | Wenn es um Wasser- und Bodenschutzrecht (BMUKN) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. Auswahlstichwort: Bmukn Wasser Und Bodensc... |
| `bmv-luft-und-luftverkehrsrecht` | Wenn es um Luft- und Luftverkehrsrecht (BMV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmv-mobilitaets-und-fuehrerscheinrecht` | Wenn es um Mobilitaets- und Fuehrerscheinrecht (BMV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmv-schienen-und-bahnregulierung-aeg` | Wenn es um Schienen- und Bahnregulierung (AEG) (BMV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmv-schifffahrts-und-seeverkehrsrecht` | Wenn es um Schifffahrts- und Seeverkehrsrecht (BMV) in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bmv-strassenverkehrsrecht-und-stvg-stvo` | Wenn es um Strassenverkehrsrecht (StVG; StVO) (BMV) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmvg-militaerische-beschaffung` | Wenn es um Militaerische Beschaffung und Vergaberecht (BMVg) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswah... |
| `bmvg-militaerische-beschaffung-und-vergaberecht` | Wenn es um Militaerische Beschaffung und Vergaberecht (BMVg) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswah... |
| `bmvg-nato-und-stationierungsrecht` | Wenn es um NATO-Recht und Stationierungsrecht (BMVg) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmvg-reservisten` | Wenn es um Reservistenrecht und Zivilschutzrecht (BMVg) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmvg-reservisten-und-zivilschutzrecht` | Wenn es um Reservistenrecht und Zivilschutzrecht (BMVg) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstic... |
| `bmvg-verteidigungstechnologie-export` | Wenn es um Verteidigungstechnologie und Exportkontrolle (BMVg) in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bmvg-wehrrecht-und-soldatenstatus` | Wenn es um Wehrrecht und Soldatenstatus (BMVg) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmwe-aussenwirtschaft` | Wenn es um Außenwirtschaft und Investitionspruefung (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. Auswahlstichwort:... |
| `bmwe-aussenwirtschaft-und-investitionspruefung` | Wenn es um Außenwirtschaft und Investitionspruefung (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. Auswahlstichwort:... |
| `bmwe-energie-und-netzregulierung-enwg` | Wenn es um Energierecht und Netzregulierung (EnWG) (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmwe-erneuerbare-energien-eeg-windbg` | Wenn es um Erneuerbare Energien (EEG; WindBG) (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmwe-industriepolitik-foerderrecht` | Wenn es um Industriepolitik; Foerderrecht; EU-Beihilfen (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Ausw... |
| `bmwe-industriepolitik-foerderrecht-und-beihilfen` | Wenn es um Industriepolitik; Foerderrecht; EU-Beihilfen (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Ausw... |
| `bmwe-wettbewerb-und-kartellrecht-gwb` | Wenn es um Wettbewerbsrecht und Kartellrecht (GWB) (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmwsb-bau-bauproduktenrecht-technische` | Wenn es um Bau- und Planungsrecht (BauGB; BauNVO) (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlst... |
| `bmwsb-bau-und-planungsrecht-baugb-baunvo` | Wenn es um Bau- und Planungsrecht (BauGB; BauNVO) (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlst... |
| `bmwsb-bauproduktenrecht-technische` | Wenn es um Bauproduktenrecht und technische Normen (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmwsb-bauproduktenrecht-und-technische-normen` | Wenn es um Bauproduktenrecht und technische Normen (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahls... |
| `bmwsb-energetische-sanierung-und-geg` | Wenn es um Energetische Sanierung (GEG) (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmwsb-mietrecht-und-wohnungspolitik` | Wenn es um Mietrecht und Wohnungspolitik (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmwsb-stadtentwicklung-foerderprogramme` | Wenn es um Stadtentwicklung und Foerderprogramme (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlsti... |
| `bmwsb-stadtentwicklung-und-foerderprogramme` | Wenn es um Stadtentwicklung und Foerderprogramme (BMWSB) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlsti... |
| `bmz-entwicklungszusammenarbeit` | Wenn es um Entwicklungszusammenarbeit und bilaterale Abkommen (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen.... |
| `bmz-entwicklungszusammenarbeit-und-bilaterale-abkommen` | Wenn es um Entwicklungszusammenarbeit und bilaterale Abkommen (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen.... |
| `bmz-humanitaere-hilfe-krisenpraevention` | Wenn es um Humanitaere Hilfe und Krisenpraevention (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlsti... |
| `bmz-humanitaere-hilfe-und-krisenpraevention` | Wenn es um Humanitaere Hilfe und Krisenpraevention (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlsti... |
| `bmz-internationale-klimafinanzierung` | Wenn es um Internationale Klimafinanzierung (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bmz-menschenrechte-in-lieferketten-lksg` | Wenn es um Menschenrechte in Lieferketten (LkSG) (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmz-menschenrechte-multilaterale` | Wenn es um Menschenrechte in Lieferketten (LkSG) (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. Auswahlstich... |
| `bmz-multilaterale-zusammenarbeit-und-eu` | Wenn es um Multilaterale Zusammenarbeit und EU (BMZ) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `bundestag-fristen-form-und-zustaendigkeit` | Wenn es um Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Bu... |
| `bundestag-fristen-form-zustaendigkeit` | Wenn es um Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Bu... |
| `chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-rendern-docx-pdf` | Wenn es um Dokumente rendern - DOCX und PDF im offiziellen HdR-Layout in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `entschliessungsantraege-fehlerkatalog` | Wenn es um Entschliessungsantraege Fehlerkatalog in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `erstpruefung-rollenklaerung` | Wenn es um Legistik: Erstprüfung, Rollenklärung und Mandatsziel in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstic... |
| `eu-richtlinienumsetzung-spezial` | Wenn es um LegW: EU-Richtlinienumsetzung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `europarechtskonformitaet` | Wenn es um Europarechtskonformität in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Europarechtskonformitaet; Arbeit... |
| `folgenabschaetzung-erfuellungsaufwand` | Wenn es um Folgenabschätzung - Erfüllungsaufwand in Legistik-Werkstatt geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `folgenabschaetzung-nachhaltigkeit` | Wenn es um Folgenabschätzung - Nachhaltigkeit in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `formulierungshilfe-bauen` | Wenn es um Formulierungshilfe und parlamentarische Vorlage bauen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fraktionen-dokumentenmatrix-lueckenliste` | Wenn es um Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fraktionen-dokumentenmatrix-und-lueckenliste` | Wenn es um Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `gesetzesentwurf-kabinett` | Wenn es um Gesetzesentwurf Kabinett in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Gesetzesentwurf Kabinett; Arbei... |
| `gesetzesentwurf-kabinett-aa-voelkerrecht` | Wenn es um Gesetzesentwurf Kabinett in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Gesetzesentwurf Kabinett Aa Voe... |
| `gesetzgebungskompetenz-pruefen` | Wenn es um Gesetzgebungskompetenz prüfen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gesetzgebungsverfahren-bauleiter` | Wenn es um LegW: Gesetzgebungsverfahren in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `goldplating-vermeiden` | Wenn es um Goldplating vermeiden in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Goldplating Vermeiden; Arbeitsfeld... |
| `goldplating-vermeiden-inkrafttreten` | Wenn es um Goldplating vermeiden in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Goldplating Vermeiden Inkrafttrete... |
| `inkrafttreten-uebergangsrecht` | Wenn es um Inkrafttreten und Übergangsrecht in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kabinettsentwuerfe-compliance-dokumentation-und-akte` | Wenn es um Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `kaltstart-triage` | Wenn es um Kaltstart Triage in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `laender-behoerden-gerichts-registerweg` | Wenn es um Länder: Behörden-, Gerichts- oder Registerweg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Laender Be... |
| `laender-landtage-legistik-ministerien` | Wenn es um Länder: Behörden-, Gerichts- oder Registerweg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Laender La... |
| `landtage-schriftsatz-brief-memo-bausteine` | Wenn es um Landtage: Schriftsatz-, Brief- und Memo-Bausteine in Legistik-Werkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `landtage-schriftsatz-brief-und-memo-bausteine` | Wenn es um Landtage: Schriftsatz-, Brief- und Memo-Bausteine in Legistik-Werkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `legistik-auftragsaufnahme` | Wenn es um Legistik-Auftragsaufnahme in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `legistik-erstpruefung-und-mandatsziel` | Wenn es um Legistik: Erstprüfung, Rollenklärung und Mandatsziel in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstic... |
| `legistik-europarechtskonformitaet-notifizierung` | Wenn es um Europarechtskonformität in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Legistik Europarechtskonformitae... |
| `legistik-kabinettsentwurf-ressortabstimmung` | Wenn es um Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `legistik-normenkartierung-aenderungsbefehle` | Wenn es um Normenkartierung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Legistik Normenkartierung Aenderungsbef... |
| `legw-bmi-auslaender-und-staatsangehoerigkeitsrecht` | Wenn es um Auslaender- und Staatsangehoerigkeitsrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `legw-bmleh-agrar-und-foerderungsrecht-gak-gap` | Wenn es um Agrar- und Foerderungsrecht (GAK; GAP) (BMLEH) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `legw-bmwe-aussenwirtschaft-und-investitionspruefung` | Wenn es um Aussenwirtschaft und Investitionspruefung (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `legw-rmap-evaluierung-und-aenderung` | Wenn es um Evaluierung und Aenderung von Rulemap-Normen in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `lesefassung-konsolidiert` | Wenn es um Lesefassung konsolidiert in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ministerien-tatbestand-beweis-und-belege` | Wenn es um Ministerien: Tatbestandsmerkmale, Beweisfragen und Beleglage in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `ministerien-tatbestandsmerkmale-beweisfragen` | Wenn es um Ministerien: Tatbestandsmerkmale, Beweisfragen und Beleglage in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mitte-internationaler-bezug-schnittstellen` | Wenn es um Mitte: Internationaler Bezug und Schnittstellen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Mitte In... |
| `mitte-internationaler-bezug-und-schnittstellen` | Wenn es um Mitte: Internationaler Bezug und Schnittstellen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Mitte In... |
| `normenkartierung-normenkontrollrat-kmu` | Wenn es um Normenkartierung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Normenkartierung Normenkontrollrat Kmu;... |
| `normenkontrollrat-kmu-check` | Wenn es um Normenkontrollrat / KMU-Check in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `normgeber-verhandlung-vergleich-eskalation` | Wenn es um Normgeber: Verhandlung, Vergleich und Eskalation in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `normgeber-verhandlung-vergleich-und-eskalation` | Wenn es um Normgeber: Verhandlung, Vergleich und Eskalation in Legistik-Werkstatt geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `normhierarchie-routing` | Wenn es um Normhierarchie-Routing in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `normtext-begruendung-synopse` | Wenn es um Normtext, Begründung und Synopse als Gesetzgebungswerkstatt in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfrag... |
| `normtext-begruendung-und-synopse` | Wenn es um Normtext, Begründung und Synopse als Gesetzgebungswerkstatt in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfrag... |
| `opposition-risikoampel-gegenargumente` | Wenn es um Opposition: Risikoampel, Gegenargumente und Verteidigungslinien in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswa... |
| `opposition-risikoampel-und-gegenargumente` | Wenn es um Opposition: Risikoampel, Gegenargumente und Verteidigungslinien in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswa... |
| `output-waehlen` | Wenn es um Output wählen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Legistik-Werkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rechtsbereinigung-spezial` | Wenn es um LegW: Rechtsbereinigung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rechtsfolgenabschaetzung-leitfaden` | Wenn es um LegW: Gesetzesfolgenabschaetzung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `referenten-vorlagen-interessen-synopse` | Wenn es um Referenten: Zahlen, Schwellenwerte und Berechnung in Legistik-Werkstatt geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `referenten-zahlen-schwellenwerte-berechnung` | Wenn es um Referenten: Zahlen, Schwellenwerte und Berechnung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `referentenentwurf-bauen` | Wenn es um Referentenentwurf bauen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-aa` | Wenn es um Ressort-Heranfuehrung AA in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmas` | Wenn es um Ressort-Heranfuehrung BMAS in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmbfsfj` | Wenn es um Ressort-Heranfuehrung BMBFSFJ in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmds` | Wenn es um Ressort-Heranfuehrung BMDS in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressort Bmds; Arbeitsfeld: Le... |
| `ressort-bmf` | Wenn es um Ressort-Heranfuehrung BMF in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressort Bmf; Arbeitsfeld: Legi... |
| `ressort-bmftr` | Wenn es um Ressort-Heranfuehrung BMFTR in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmg` | Wenn es um Ressort-Heranfuehrung BMG in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmi` | Wenn es um Ressort-Heranfuehrung BMI in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmjv` | Wenn es um Ressort-Heranfuehrung BMJV in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmleh` | Wenn es um Ressort-Heranfuehrung BMLEH in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmukn` | Wenn es um Ressort-Heranfuehrung BMUKN in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmv` | Wenn es um Ressort-Heranfuehrung BMV in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmvg` | Wenn es um Ressort-Heranfuehrung BMVg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressort Bmvg; Arbeitsfeld: Le... |
| `ressort-bmvg-bmwe-bmwsb-bmz` | Wenn es um Ressort-Heranfuehrung BMVg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressort Bmvg Bmwe Bmwsb Bmz;... |
| `ressort-bmwe` | Wenn es um Ressort-Heranfuehrung BMWE in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmwsb` | Wenn es um Ressort-Heranfuehrung BMWSB in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-bmz` | Wenn es um Ressort-Heranfuehrung BMZ in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-heranfuehrung-bmds` | Wenn es um Ressort-Heranfuehrung BMDS in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressort Heranfuehrung Bmds; A... |
| `ressort-router` | Wenn es um Legistik-Werkstatt - Ressort-Router in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressort-verbaendeanhoerung` | Wenn es um Ressort-Heranfuehrung BMF in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressort Verbaendeanhoerung; Ar... |
| `ressortaufgaben-aa` | Wenn es um Ressortaufgaben AA in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmas` | Wenn es um Ressortaufgaben BMAS in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmbfsfj` | Wenn es um Ressortaufgaben BMBFSFJ in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmds` | Wenn es um Ressortaufgaben BMDS in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressortaufgaben Bmds; Arbeitsfeld:... |
| `ressortaufgaben-bmds-bmf-bmftr-bmg-bmi` | Wenn es um Ressortaufgaben BMDS in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressortaufgaben Bmds Bmf Bmftr Bmg... |
| `ressortaufgaben-bmf` | Wenn es um Ressortaufgaben BMF in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmftr` | Wenn es um Ressortaufgaben BMFTR in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmg` | Wenn es um Ressortaufgaben BMG in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmi` | Wenn es um Ressortaufgaben BMI in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmjv` | Wenn es um Ressortaufgaben BMJV in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmleh` | Wenn es um Ressortaufgaben BMLEH in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmukn` | Wenn es um Ressortaufgaben BMUKN in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmv` | Wenn es um Ressortaufgaben BMV in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressortaufgaben Bmv; Arbeitsfeld: Le... |
| `ressortaufgaben-bmv-bmvg-bmwe-bmwsb-bmz` | Wenn es um Ressortaufgaben BMV in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Ressortaufgaben Bmv Bmvg Bmwe Bmwsb... |
| `ressortaufgaben-bmvg` | Wenn es um Ressortaufgaben BMVg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmwe` | Wenn es um Ressortaufgaben BMWE in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmwsb` | Wenn es um Ressortaufgaben BMWSB in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ressortaufgaben-bmz` | Wenn es um Ressortaufgaben BMZ in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rmap-anschluss-an` | Wenn es um Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: R... |
| `rmap-anschluss-an-legw` | Wenn es um Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: R... |
| `rmap-bestimmtheit-und-justitiabilitaet` | Wenn es um Bestimmtheit und Justitiabilitaet bei Rulemap-Normen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rmap-entscheidungsbaum-validierung` | Wenn es um Entscheidungsbaum-Simulation und Verifikation in Legistik-Werkstatt geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `rmap-evaluierung-export` | Wenn es um Evaluierung und Änderung von Rulemap-Normen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Rmap Evaluie... |
| `rmap-evaluierung-und-aenderung` | Wenn es um Evaluierung und Änderung von Rulemap-Normen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Rmap Evaluie... |
| `rmap-export-und-systemintegration` | Wenn es um Export und Integration in Vollzugs-IT in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `rmap-grundlagen` | Wenn es um Rulemapping - Grundlagen und Begriffe in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `rmap-norm-zu-rulemap` | Wenn es um Von der Norm zur Rulemap - Vorgehensmodell in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rmap-tatbestand-und-rechtsfolge` | Wenn es um Tatbestand und Rechtsfolge als Knoten modellieren in Legistik-Werkstatt geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `rmap-verweisungen-und-ausnahmen` | Wenn es um Verweisungen und Ausnahmen in der Rulemap in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `rmap-vollzugstauglichkeit` | Wenn es um Vollzugstauglichkeit der Rulemap im Verwaltungsverfahren in Legistik-Werkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anla... |
| `satzungskompetenz-pruefen` | Wenn es um Satzungskompetenz prüfen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schulung-legistik` | Wenn es um Trainerleitfaden Schulung Legistik in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Schulung Legistik; Ar... |
| `schulung-legistik-aenderungs-fraktionen` | Wenn es um Trainerleitfaden Schulung Legistik in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Schulung Legistik Aen... |
| `spezial-aenderungs-formular-portal-und-einreichung` | Wenn es um Aenderungs: Formular, Portal und Einreichungslogik in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-baut-livequellen-und-rechtsprechungscheck` | Wenn es um Baut: Livequellen- und Rechtsprechungscheck in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-entschliessungsantraege-red-team-und-qualitaetskontrolle` | Wenn es um Entschliessungsantraege: Red-Team und Qualitätskontrolle in Legistik-Werkstatt geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-laender-behoerden-gericht-und-registerweg` | Wenn es um Laender: Behörden-, Gerichts- oder Registerweg in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `synopse-erstellen` | Wenn es um Synopse erstellen in Legistik-Werkstatt geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `terminologie-konsistenz` | Wenn es um Terminologie-Konsistenz in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verbaendeanhoerung-ressortabstimmung` | Wenn es um Verbändeanhörung und Ressortabstimmung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verfassungsmaessigkeit-quercheck` | Wenn es um Verfassungsmaessigkeit-Quercheck in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verordnungsermaechtigung-art80` | Wenn es um Verordnungsermaechtigung Art. 80 GG in Legistik-Werkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `vorlagen-interessen` | Wenn es um Vorlagen: Mehrparteienkonflikt und Interessenmatrix in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Vorl... |
| `vorlagen-mehrparteien-konflikt-und-interessen` | Wenn es um Vorlagen: Mehrparteienkonflikt und Interessenmatrix in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Vorl... |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Legistik-Werkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `xml-paralleldarstellung` | Wenn es um XML-Paralleldarstellung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zirkelschluss-pruefen` | Wenn es um Zirkelschluss prüfen in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
