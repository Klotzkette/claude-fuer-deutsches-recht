# Forderungsmanagement — Klagewerkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forderungsmanagement-klagewerkstatt`) | [`forderungsmanagement-klagewerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Inkasso-Zahlungsklage ModeFuchs** (`inkasso-zahlungsklage-modefuchs`) | [Gesamt-PDF lesen](../testakten/inkasso-zahlungsklage-modefuchs/gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf) | [`testakte-inkasso-zahlungsklage-modefuchs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`forderungsmanagement-klagewerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/forderungsmanagement-klagewerkstatt/forderungsmanagement-klagewerkstatt-werkstatt.md" download><code>forderungsmanagement-klagewerkstatt-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/forderungsmanagement-klagewerkstatt/forderungsmanagement-klagewerkstatt-schnellstart.md" download><code>forderungsmanagement-klagewerkstatt-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Akte Inkasso-Zahlungsklage ModeFuchs: [Gesamt-PDF](../testakten/inkasso-zahlungsklage-modefuchs/gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf), [`testakte-inkasso-zahlungsklage-modefuchs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip), [`testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
**Generalisierter Klage-Assistent für Inkasso- und Forderungsmanagement-Klagen mit eigenem Plugin-Generator.** Aus eigenen Mustern eine hauseigene Standardvorlage destillieren, online die Zuständigkeit prüfen, die Klage erzeugen und als sofort installierbares Mini-Plugin verpacken. Der Start ist jetzt aktengetrieben: Ordner, ZIP oder Dokumentenstapel zeigen, kurz auslesen lassen, dann mit Parteienhypothese, Forderungsmatrix, Mahnchronologie, Fristenampel und nur noch echten Rückfragen weiterarbeiten. Neu hinzu kommt ein direkter Inkasso-Zahlungsklage-Ersteller mit Mahnvorlauf, Anspruchs-Gatekeeper und der harten Regel: nur klare, fällige und belegte Ansprüche einklagen.

---

---

## So beginnt man

1. Aktenordner, ZIP oder die wichtigsten Dokumente hochladen.
2. `aktenordner-erstlekture` oder `kaltstart-triage` starten.
3. Das Plugin liest zuerst Vollmacht, Rechnung, Vertrag, Mahnung, Kontoauszug, Mahnbescheid, Widerspruch, Klageentwurf und Registerfunde aus.
4. Danach kommt keine lange Einstiegsabfrage, sondern eine Arbeitshypothese: Parteien, Forderung, Zahlungen, Verzug, Verjährung, Verfahrensstand, Engpass.
5. Rückfragen werden auf echte Lücken beschränkt.

## Was ist drin

Kernfunktionen für den Direktlauf aus der Akte heraus:

| Skill | Zweck |
| --- | --- |
| `aktenordner-erstlekture` | **Akten zuerst**: wertet vorhandene Ordner, ZIPs, PDFs, EMLs, Kontoauszüge, Mahnbescheide und Klageentwürfe aus; rekonstruiert Parteien, Forderungsstand, Zahlungen, Mahnverlauf und Fristen; fragt nur noch Lücken ab. |
| `kaltstart-triage` | **Triage ohne Formularfrust**: nimmt die Aktenhypothese auf, sortiert Mahnung, Mahnbescheid, Klage, Vergleich oder Vollstreckung und stellt hoechstens echte Lueckenfragen. |
| `dokumente-intake` | **Belegordnung**: baut aus ungeordneten Dateien ein Akteninventar mit Vertrag, Leistung, Rechnung, Zahlung, Mahnung, Verfahren und Lueckenliste. |
| `klagefreigabe-belegte-forderung` | **Klage-Gatekeeper**: lässt nur schlüssige, faellige und belegte Positionen in die Klage; bereits bezahlte Hauptforderungen werden blockiert. |
| `mahnbescheid-online` | **Mahnverfahren**: führt durch den Online-Mahnbescheid, wenn die Forderung klar und der Streit noch nicht ausgebrochen ist. |
| `zahlungsklage-erstellen` | **Klageentwurf**: erzeugt Rubrum, Antrag, Tatsachenvortrag, Beweismittel, Anlagenlogik und Einreichungscheck. |
| `workflow-orchestrierung` | **Akte steuern**: haelt Wiedervorlagen, Fristen, naechste Schritte und Stop-Bedingungen zusammen. |

Der Plugin-Generator bleibt zusaetzlich über `scripts/plugin_aus_hausregeln.py` und die Vorlagen in `assets/vorlagen-leer/` erhalten.

Alle Klage-Skills führen **bei jedem Lauf** die Online-Zuständigkeitsprüfung über [justizadressen.nrw.de](https://www.justizadressen.nrw.de) und das [bundesweite Justizportal](https://justiz.de) durch.

## Inkasso-Zahlungsklage-Ersteller

Der neue Direktlauf ist für Fälle gedacht, in denen eine Forderungsakte schon einen Mahn- oder Inkassoverlauf enthält. Er prüft vor der Klage:

- Rechnung, Fälligkeit, Lieferung/Leistung und Abtretung.
- Mahnvorlauf mit Zugang, Fristen und Beträgen.
- Zahlungseingänge, Teilzahlungen, Erfüllung und interne Kenntnis.
- Mahnkosten, Verzugszinsen, Inkassokosten und Mahnverfahrenskosten einzeln.
- Gerichtsort mit aktueller ladungsfähiger Anschrift.

Die ModeFuchs-Testakte unter [`inkasso-zahlungsklage-modefuchs/`](../testakten/inkasso-zahlungsklage-modefuchs/) ist der Referenzfall: Hauptforderung 698,00 EUR bezahlt vor Klageeinreichung, Nebenforderungen 99,84 EUR streitig. Erwartung: Hauptforderung rot, Nebenforderungen gelb, keine automatische Klage über 797,84 EUR. Direktdownload siehe Sofort-Download-Sektion oben.

## Plugin-Generator

Aus den extrahierten Hausregeln und der Standardvorlage packt der Skill ein eigenes, in Plugin-Umgebung direkt installierbares ZIP:

```bash
python scripts/plugin_aus_hausregeln.py \
  --kanzlei "Kanzlei Mustermann" \
  --vorlage assets/vorlagen-leer/standardklage.md \
  --regeln  /pfad/hausregeln.json \
  --ziel    /pfad/klagewerkstatt-mustermann.zip
```

Layout des erzeugten Plugins:

```
klagewerkstatt-<slug>/
  .claude-plugin/plugin.json
  skills/klage-erstellen/SKILL.md
  assets/vorlage/standardklage.md
  references/hausregeln.json
  references/belegmuster.md
  references/anlagenliste.md
  references/zustaendigkeit-quellen.md
  README.md
```

Der erzeugte Skill enthält die Hausregeln fest verdrahtet und führt weiterhin die **Online-Zuständigkeitsprüfung** als Pflichtschritt aus.

## Ergebnisformate

- **DOCX** über `office/docx` (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und **Markdown-Spiegel**.
- **Anlage Zuständigkeitsprüfung** mit Online-Quelle und Abrufdatum.
- **HTML-Padlet** (`assets/padlet/klage-padlet.html`) — single-file, autark, Live-Vorschau, speichert in `localStorage`, exportiert/importiert JSON.
- **Memo** im Gutachtenstil — nur auf ausdrückliche Anfrage.

## Online-Zuständigkeit (Pflicht in jedem Lauf)

1. **Sachlich** rechnerisch: bis einschließlich 10.000 EUR Amtsgericht nach Paragraf 23 Nummer 1 GVG in der Fassung seit 1.1.2026; über 10.000 EUR Landgericht nach Paragraf 71 Absatz 1 GVG mit Anwaltszwang nach Paragraf 78 Absatz 1 Satz 1 ZPO. Wohnraummietsachen sind davon zu trennen: Ansprüche aus Wohnraummietverhältnissen gehören nach Paragraf 23 Nummer 2a GVG streitwertunabhängig zum Amtsgericht; das gilt auch für verbundene Räumungs- und Zahlungsklagen.
2. **Örtlich** rechtlich: §§ 12, 13 ZPO Allgemeiner Gerichtsstand, § 29 ZPO Erfüllungsort, § 29c ZPO Verbraucherverträge, § 38 ZPO Gerichtsstandsvereinbarung; grenzüberschreitend Brüssel Ia VO 1215/2012.
3. **Online-Adressrecherche**: `justizadressen.nrw.de` (PLZ/Ort) und bundesweit `justiz.de`; Quelle und Abrufdatum dokumentieren.
4. BeA-SAFE-ID: aus dem beA-Adressbuch zu ergänzen.

## Leitentscheidungen (Auswahl, siehe `references/rechtsprechung/INDEX.md`)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `erstpruefung-rollen-mandatsziel`, `kaltstart-triage`, `spezial-klagewerkstatt-erstpruefung-und-mandatsziel`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `aktenordner-erstlekture`, `belegte-compliance-aktenvermerk`, `chronologie-belegmatrix`, `forderungen-interessen-matrix`, `klagefreigabe-belegte-forderung`, `mahnverfahren-beweislast-darlegungslast`, `mahnvorlauf-dokumentenmatrix`, `quellenkarte`, `spezial-belegte-compliance-dokumentation-und-akte`, `spezial-forderungsmanagement-tatbestand-beweis-und-belege`, `spezial-klage-formular-portal-und-einreichung`, `spezial-klagefreigabe-belegte-forderung`, `spezial-klare-livequellen-und-rechtsprechungscheck`, `spezial-mahnverfahren-beweislast-und-darlegungslast`, `spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste`, `tatbestand-beweis-belege`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `anspruchsschriftsatz-bausteine`, `fristen-risikoampel`, `inkasso-risikoampel`, `spezial-anspruchs-schriftsatz-brief-und-memo-bausteine`, `spezial-inkasso-risikoampel-und-gegenargumente`, `spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit`, `zustaendigkeitspruefung-mahngericht` |
| 4. Gestaltung, Strategie und Verhandlung | `forderung-aus-werkvertrag-bgb-bau`, `forderung-werkvertrag-bau`, `gatekeeper-verhandlung-vergleich`, `spezial-gatekeeper-verhandlung-vergleich-und-eskalation` |
| 5. Verfahren, Behörde und Gericht | `fmkw-mahnverfahren-bauleiter`, `fmkw-verbraucherklage-cookies-rdg-spezial`, `forderung-mietruckstand-zahlungsklage`, `forderung-mietrueckstand-zahlungsklage`, `forderung-zwangsvollstreckung-ueberblick`, `inkasso-zahlungsklage-ersteller`, `klage-aus-eigenem-skill`, `klage-einreichungslogik`, `klagevorlage-aus-eigenen-mustern`, `kostenfeststellungsklage-verzugsschaden-erledigung`, `mahnbescheid-online`, `mahnbescheid-online-mb`, `mahnung-aussergerichtlich-stufenmodell`, `mahnverfahren-bauleiter`, `spezial-zahlungsklage-behoerden-gericht-und-registerweg`, `verbraucherklage-rdg-grenzen`, `vollstreckungsbescheid-folgen`, `vollstreckungsbescheid-und-folgen`, ... plus 3 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | `mandantenkommunikation`, `output-waehlen`, `spezial-fmkw-mandantenkommunikation-entscheidungsvorlage` |
| 7. Kontrolle, Qualität und Gegenprüfung | `fehlerkatalog`, `forderung-gegen-gesellschafter-13-gmbhg`, `forderung-gegen-gmbh-gesellschafter`, `forderung-gegen-insolventen-schuldner`, `forderung-gegen-verbraucher`, `redteam-qualitygate`, `spezial-freigegeben-red-team-und-qualitaetskontrolle` |
| 8. Spezialmodule und Schnittstellen | `faellige-zahlen-schwellen`, `fmkw-saumselig-streitig-erfahrung-spezial`, `fmkw-titulierung-streckung-leitfaden`, `forderung-anwaltshonorar-rvg`, `forderung-arzthonorar-goae`, `forderung-im-ausland-vollstrecken`, `forderung-internationaler-bezug`, `forderungsaufnahme`, `forderungsmanagement-aufnahme`, `saumselig-sonderfall-edge-case`, `spezial-faellige-zahlen-schwellen-und-berechnung`, `spezial-forderungen-mehrparteien-konflikt-und-interessen`, `spezial-saumselig-sonderfall-und-edge-case`, `spezial-werden-internationaler-bezug-und-schnittstellen`, `titulierung-streckung-leitfaden`, `urkundenprozess-pruefen`, `verjaehrung-pruefen`, `workflow-orchestrierung`, ... plus 1 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenordner-erstlekture` | Wenn es um Aktenordner-Erstlektüre in Forderungsmanagement — Klagewerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `anspruchsschriftsatz-bausteine` | Wenn es um Anspruchsschriftsatz Bausteine in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `belegte-compliance-aktenvermerk` | Wenn es um Belegte Compliance Aktenvermerk in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `chronologie-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `dokumente-intake` | Wenn es um Dokumente Intake in Forderungsmanagement — Klagewerkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `erstpruefung-rollen-mandatsziel` | Wenn es um Erstpruefung Rollen und Mandatsziel in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `faellige-zahlen-schwellen` | Wenn es um Faellige Zahlen und Schwellen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fehlerkatalog` | Wenn es um Fehlerkatalog Forderungsmanagement in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagen... |
| `fmkw-mahnverfahren-bauleiter` | Wenn es um FMKW: Mahnverfahren Bauleiter in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fmkw-saumselig-streitig-erfahrung-spezial` | Wenn es um FMKW: Saumselig Streitig in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fmkw-titulierung-streckung-leitfaden` | Wenn es um FMKW: Titulierung Streckung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `fmkw-verbraucherklage-cookies-rdg-spezial` | Wenn es um FMKW: Verbraucherinkasso RDG in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderung-anwaltshonorar-rvg` | Wenn es um Anwaltshonorar nach RVG in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderung-arzthonorar-goae` | Wenn es um Arzthonorar nach GOAE und GOZ in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderung-aus-werkvertrag-bgb-bau` | Wenn es um Werk-/Bauwerklohn-Forderung in Forderungsmanagement — Klagewerkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `forderung-gegen-gesellschafter-13-gmbhg` | Wenn es um Forderung gegen Gesellschafter in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderung-gegen-gmbh-gesellschafter` | Wenn es um Forderung gegen GmbH-Gesellschafter in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| `forderung-gegen-insolventen-schuldner` | Wenn es um Forderung gegen insolventen Schuldner in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderung-gegen-verbraucher` | Wenn es um Forderung gegen Verbraucher in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderung-im-ausland-vollstrecken` | Wenn es um Forderung im Ausland vollstrecken in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| `forderung-internationaler-bezug` | Wenn es um Forderung mit internationalem Bezug in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderung-mietruckstand-zahlungsklage` | Wenn es um Mietrueckstands-Klage in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderung-mietrueckstand-zahlungsklage` | Wenn es um Mietrueckstand – Zahlungsklage Wohnraum in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und An... |
| `forderung-werkvertrag-bau` | Wenn es um Werklohnforderung – BGB und Bau in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderung-zwangsvollstreckung-ueberblick` | Wenn es um Zwangsvollstreckung Ueberblick in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderungen-interessen-matrix` | Wenn es um Forderungen-Interessen-Matrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderungsaufnahme` | Wenn es um Forderungsaufnahme in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `forderungsmanagement-aufnahme` | Wenn es um Forderung aufnehmen in Forderungsmanagement — Klagewerkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `fristen-risikoampel` | Wenn es um Fristen-Risikoampel in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gatekeeper-verhandlung-vergleich` | Wenn es um Gatekeeper Verhandlung und Vergleich in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlag... |
| `inkasso-risikoampel` | Wenn es um Inkasso-Risikoampel in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `inkasso-zahlungsklage-ersteller` | Wenn es um Inkasso-Zahlungsklage-Ersteller in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `kaltstart-triage` | Wenn es um Kaltstart-Triage Forderungssache in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagen... |
| `klage-aus-eigenem-skill` | Wenn es um Klagewerkstatt — Laufzeit aus eigenem Skill in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| `klage-einreichungslogik` | Wenn es um Klage-Einreichungslogik in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `klagefreigabe-belegte-forderung` | Wenn es um Klagefreigabe belegte Forderung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `klagevorlage-aus-eigenen-mustern` | Wenn es um Klagewerkstatt — Lernlauf aus eigenen Mustern in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung... |
| `kostenfeststellungsklage-verzugsschaden-erledigung` | Wenn es um Kostenfeststellungsklage nach Zahlung auf die Forderung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, B... |
| `mahnbescheid-online` | Wenn es um Mahnbescheid online in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mahnbescheid-online-mb` | Wenn es um Mahnbescheid (Online-MB) in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mahnung-aussergerichtlich-stufenmodell` | Wenn es um Mahnung aussergerichtlich – Stufenmodell in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und A... |
| `mahnverfahren-bauleiter` | Wenn es um Mahnverfahren bei Bauforderungen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlo... |
| `mahnverfahren-beweislast-darlegungslast` | Wenn es um Beweislast und Darlegungslast in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `mahnvorlauf-dokumentenmatrix` | Wenn es um Mahnvorlauf Dokumentenmatrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mandantenkommunikation` | Wenn es um Mandantenkommunikation in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `output-waehlen` | Wenn es um Output waehlen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quellenkarte` | Wenn es um Quellenkarte in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `redteam-qualitygate` | Wenn es um Redteam Qualitygate in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `saumselig-sonderfall-edge-case` | Wenn es um Saumselige Sonderfaelle in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `spezial-anspruchs-schriftsatz-brief-und-memo-bausteine` | Wenn es um Anspruchs: Schriftsatz-, Brief- und Memo-Bausteine in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begrün... |
| `spezial-belegte-compliance-dokumentation-und-akte` | Wenn es um Belegte: Compliance-Dokumentation und Aktenvermerk in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begrün... |
| `spezial-faellige-zahlen-schwellen-und-berechnung` | Wenn es um Faellige: Zahlen, Schwellenwerte und Berechnung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründun... |
| `spezial-fmkw-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Fmkw: Mandantenkommunikation und Entscheidungsvorlage in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvo... |
| `spezial-forderungen-mehrparteien-konflikt-und-interessen` | Wenn es um Forderungen: Mehrparteienkonflikt und Interessenmatrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Be... |
| `spezial-forderungsmanagement-tatbestand-beweis-und-belege` | Wenn es um Forderungsmanagement: Tatbestandsmerkmale, Beweisfragen und Beleglage in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf m... |
| `spezial-freigegeben-red-team-und-qualitaetskontrolle` | Wenn es um Freigegeben: Red-Team und Qualitätskontrolle in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-gatekeeper-verhandlung-vergleich-und-eskalation` | Wenn es um Gatekeeper: Verhandlung, Vergleich und Eskalation in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründ... |
| `spezial-inkasso-risikoampel-und-gegenargumente` | Wenn es um Inkasso: Risikoampel, Gegenargumente und Verteidigungslinien in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sof... |
| `spezial-klage-formular-portal-und-einreichung` | Wenn es um Klage: Formular, Portal und Einreichungslogik in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung... |
| `spezial-klagefreigabe-belegte-forderung` | Wenn es um Klagefreigabe nur für fällige, belegte und prozessreife Forderungen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit... |
| `spezial-klagewerkstatt-erstpruefung-und-mandatsziel` | Wenn es um Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sof... |
| `spezial-klare-livequellen-und-rechtsprechungscheck` | Wenn es um Klare: Livequellen- und Rechtsprechungscheck in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung u... |
| `spezial-mahnverfahren-beweislast-und-darlegungslast` | Wenn es um Mahnverfahren: Beweislast, Darlegungslast und Substantiierung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträ... |
| `spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste` | Wenn es um Mahnvorlauf: Dokumentenmatrix, Lückenliste und Nachforderung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträg... |
| `spezial-saumselig-sonderfall-und-edge-case` | Wenn es um Saumselig: Sonderfall und Edge-Case-Prüfung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| `spezial-werden-internationaler-bezug-und-schnittstellen` | Wenn es um Werden: Internationaler Bezug und Schnittstellen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründu... |
| `spezial-zahlungsklage-behoerden-gericht-und-registerweg` | Wenn es um Zahlungsklage: Behörden-, Gerichts- oder Registerweg in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begr... |
| `spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit` | Wenn es um Zustaendigkeitspruefung: Fristen, Form, Zuständigkeit und Rechtsweg in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel... |
| `tatbestand-beweis-belege` | Wenn es um Tatbestand Beweis Belege in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `titulierung-streckung-leitfaden` | Wenn es um Titulierung und Streckung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `urkundenprozess-pruefen` | Wenn es um Urkundenprozess in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `verbraucherklage-rdg-grenzen` | Wenn es um Verbraucherklage RDG-Grenzen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `verjaehrung-pruefen` | Wenn es um Verjährung prüfen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vollstreckungsbescheid-folgen` | Wenn es um Vollstreckungsbescheid und Folgen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| `vollstreckungsbescheid-und-folgen` | Wenn es um Vollstreckungsbescheid in Forderungsmanagement — Klagewerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-orchestrierung` | Wenn es um Workflow-Orchestrierung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `zahlungsklage-behoerden-register` | Wenn es um Zahlungsklage gegen Behörden und juristische Personen öffentlichen Rechts in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwu... |
| `zahlungsklage-erstellen` | Wenn es um Zahlungsklage erstellen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `zinsberechnung-288-bgb` | Wenn es um Zinsberechnung Paragraf 288 BGB in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `zustaendigkeitspruefung-mahngericht` | Wenn es um Zuständigkeitspruefung in Forderungsmanagement — Klagewerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `zwangsvollstreckung-ueberblick` | Wenn es um Zwangsvollstreckung Überblick in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
