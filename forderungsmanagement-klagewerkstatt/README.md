# Forderungsmanagement — Klagewerkstatt

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/forderungsmanagement-klagewerkstatt.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`forderungsmanagement-klagewerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/forderungsmanagement-klagewerkstatt/forderungsmanagement-klagewerkstatt-werkstatt.md" download><code>forderungsmanagement-klagewerkstatt-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/forderungsmanagement-klagewerkstatt/forderungsmanagement-klagewerkstatt-schnellstart.md" download><code>forderungsmanagement-klagewerkstatt-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Inkasso-Zahlungsklage ModeFuchs](../testakten/inkasso-zahlungsklage-modefuchs/README.md) | [Gesamt-PDF](../testakten/inkasso-zahlungsklage-modefuchs/gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf) | [`testakte-inkasso-zahlungsklage-modefuchs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) | [`testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
| `kaltstart-triage` | **Triage ohne Formularfrust**: nimmt die Aktenhypothese auf, sortiert Mahnung, Mahnbescheid, Klage, Vergleich oder Vollstreckung und stellt höchstens echte Lückenfragen. |
| `dokumente-intake` | **Belegordnung**: baut aus ungeordneten Dateien ein Akteninventar mit Vertrag, Leistung, Rechnung, Zahlung, Mahnung, Verfahren und Lückenliste. |
| `klagefreigabe-belegte-forderung` | **Klage-Gatekeeper**: lässt nur schlüssige, fällige und belegte Positionen in die Klage; bereits bezahlte Hauptforderungen werden blockiert. |
| `mahnbescheid-online` | **Mahnverfahren**: führt durch den Online-Mahnbescheid, wenn die Forderung klar und der Streit noch nicht ausgebrochen ist. |
| `zahlungsklage-erstellen` | **Klageentwurf**: erzeugt Rubrum, Antrag, Tatsachenvortrag, Beweismittel, Anlagenlogik und Einreichungscheck. |
| `workflow-orchestrierung` | **Akte steuern**: hält Wiedervorlagen, Fristen, nächste Schritte und Stop-Bedingungen zusammen. |

Der Plugin-Generator bleibt zusätzlich über `scripts/plugin_aus_hausregeln.py` und die Vorlagen in `assets/vorlagen-leer/` erhalten.

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

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`erstpruefung-rollen-mandatsziel`](skills/erstpruefung-rollen-mandatsziel/SKILL.md), [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md), [`spezial-klagewerkstatt-erstpruefung-und-mandatsziel`](skills/spezial-klagewerkstatt-erstpruefung-und-mandatsziel/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`aktenordner-erstlekture`](skills/aktenordner-erstlekture/SKILL.md), [`belegte-compliance-aktenvermerk`](skills/belegte-compliance-aktenvermerk/SKILL.md), [`chronologie-belegmatrix`](skills/chronologie-belegmatrix/SKILL.md), [`forderungen-interessen-matrix`](skills/forderungen-interessen-matrix/SKILL.md), [`klagefreigabe-belegte-forderung`](skills/klagefreigabe-belegte-forderung/SKILL.md), [`mahnverfahren-beweislast-darlegungslast`](skills/mahnverfahren-beweislast-darlegungslast/SKILL.md), [`mahnvorlauf-dokumentenmatrix`](skills/mahnvorlauf-dokumentenmatrix/SKILL.md), [`quellenkarte`](skills/quellenkarte/SKILL.md), [`spezial-belegte-compliance-dokumentation-und-akte`](skills/spezial-belegte-compliance-dokumentation-und-akte/SKILL.md), [`spezial-forderungsmanagement-tatbestand-beweis-und-belege`](skills/spezial-forderungsmanagement-tatbestand-beweis-und-belege/SKILL.md), [`spezial-klage-formular-portal-und-einreichung`](skills/spezial-klage-formular-portal-und-einreichung/SKILL.md), [`spezial-klagefreigabe-belegte-forderung`](skills/spezial-klagefreigabe-belegte-forderung/SKILL.md), [`spezial-klare-livequellen-und-rechtsprechungscheck`](skills/spezial-klare-livequellen-und-rechtsprechungscheck/SKILL.md), [`spezial-mahnverfahren-beweislast-und-darlegungslast`](skills/spezial-mahnverfahren-beweislast-und-darlegungslast/SKILL.md), [`spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste`](skills/spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste/SKILL.md), [`tatbestand-beweis-belege`](skills/tatbestand-beweis-belege/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`anspruchsschriftsatz-bausteine`](skills/anspruchsschriftsatz-bausteine/SKILL.md), [`fristen-risikoampel`](skills/fristen-risikoampel/SKILL.md), [`inkasso-risikoampel`](skills/inkasso-risikoampel/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`spezial-anspruchs-schriftsatz-brief-und-memo-bausteine`](skills/spezial-anspruchs-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`spezial-inkasso-risikoampel-und-gegenargumente`](skills/spezial-inkasso-risikoampel-und-gegenargumente/SKILL.md), [`spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit`](skills/spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit/SKILL.md), [`zustaendigkeitspruefung-mahngericht`](skills/zustaendigkeitspruefung-mahngericht/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`forderung-aus-werkvertrag-bgb-bau`](skills/forderung-aus-werkvertrag-bgb-bau/SKILL.md), [`forderung-werkvertrag-bau`](skills/forderung-werkvertrag-bau/SKILL.md), [`gatekeeper-verhandlung-vergleich`](skills/gatekeeper-verhandlung-vergleich/SKILL.md), [`spezial-gatekeeper-verhandlung-vergleich-und-eskalation`](skills/spezial-gatekeeper-verhandlung-vergleich-und-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`fmkw-mahnverfahren-bauleiter`](skills/fmkw-mahnverfahren-bauleiter/SKILL.md), [`fmkw-verbraucherklage-cookies-rdg-spezial`](skills/fmkw-verbraucherklage-cookies-rdg-spezial/SKILL.md), [`forderung-mietruckstand-zahlungsklage`](skills/forderung-mietruckstand-zahlungsklage/SKILL.md), [`forderung-mietrueckstand-zahlungsklage`](skills/forderung-mietrueckstand-zahlungsklage/SKILL.md), [`forderung-zwangsvollstreckung-ueberblick`](skills/forderung-zwangsvollstreckung-ueberblick/SKILL.md), [`inkasso-zahlungsklage-ersteller`](skills/inkasso-zahlungsklage-ersteller/SKILL.md), [`klage-aus-eigenem-skill`](skills/klage-aus-eigenem-skill/SKILL.md), [`klage-einreichungslogik`](skills/klage-einreichungslogik/SKILL.md), [`klagevorlage-aus-eigenen-mustern`](skills/klagevorlage-aus-eigenen-mustern/SKILL.md), [`kostenfeststellungsklage-verzugsschaden-erledigung`](skills/kostenfeststellungsklage-verzugsschaden-erledigung/SKILL.md), [`mahnbescheid-online`](skills/mahnbescheid-online/SKILL.md), [`mahnbescheid-online-mb`](skills/mahnbescheid-online-mb/SKILL.md), [`mahnung-aussergerichtlich-stufenmodell`](skills/mahnung-aussergerichtlich-stufenmodell/SKILL.md), [`mahnverfahren-bauleiter`](skills/mahnverfahren-bauleiter/SKILL.md), [`spezial-zahlungsklage-behoerden-gericht-und-registerweg`](skills/spezial-zahlungsklage-behoerden-gericht-und-registerweg/SKILL.md), [`verbraucherklage-rdg-grenzen`](skills/verbraucherklage-rdg-grenzen/SKILL.md), [`vollstreckungsbescheid-folgen`](skills/vollstreckungsbescheid-folgen/SKILL.md), [`vollstreckungsbescheid-und-folgen`](skills/vollstreckungsbescheid-und-folgen/SKILL.md), ... plus 3 weitere |
| 6. Ergebnis, Schreiben und Kommunikation | [`mandantenkommunikation`](skills/mandantenkommunikation/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md), [`spezial-fmkw-mandantenkommunikation-entscheidungsvorlage`](skills/spezial-fmkw-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`zahlungsklage-versandmappe-endfertigen`](skills/zahlungsklage-versandmappe-endfertigen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`fehlerkatalog`](skills/fehlerkatalog/SKILL.md), [`forderung-gegen-gesellschafter-13-gmbhg`](skills/forderung-gegen-gesellschafter-13-gmbhg/SKILL.md), [`forderung-gegen-gmbh-gesellschafter`](skills/forderung-gegen-gmbh-gesellschafter/SKILL.md), [`forderung-gegen-insolventen-schuldner`](skills/forderung-gegen-insolventen-schuldner/SKILL.md), [`forderung-gegen-verbraucher`](skills/forderung-gegen-verbraucher/SKILL.md), [`redteam-qualitygate`](skills/redteam-qualitygate/SKILL.md), [`spezial-freigegeben-red-team-und-qualitaetskontrolle`](skills/spezial-freigegeben-red-team-und-qualitaetskontrolle/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`faellige-zahlen-schwellen`](skills/faellige-zahlen-schwellen/SKILL.md), [`fmkw-saumselig-streitig-erfahrung-spezial`](skills/fmkw-saumselig-streitig-erfahrung-spezial/SKILL.md), [`fmkw-titulierung-streckung-leitfaden`](skills/fmkw-titulierung-streckung-leitfaden/SKILL.md), [`forderung-anwaltshonorar-rvg`](skills/forderung-anwaltshonorar-rvg/SKILL.md), [`forderung-arzthonorar-goae`](skills/forderung-arzthonorar-goae/SKILL.md), [`forderung-im-ausland-vollstrecken`](skills/forderung-im-ausland-vollstrecken/SKILL.md), [`forderung-internationaler-bezug`](skills/forderung-internationaler-bezug/SKILL.md), [`forderungsaufnahme`](skills/forderungsaufnahme/SKILL.md), [`forderungsmanagement-aufnahme`](skills/forderungsmanagement-aufnahme/SKILL.md), [`saumselig-sonderfall-edge-case`](skills/saumselig-sonderfall-edge-case/SKILL.md), [`spezial-faellige-zahlen-schwellen-und-berechnung`](skills/spezial-faellige-zahlen-schwellen-und-berechnung/SKILL.md), [`spezial-forderungen-mehrparteien-konflikt-und-interessen`](skills/spezial-forderungen-mehrparteien-konflikt-und-interessen/SKILL.md), [`spezial-saumselig-sonderfall-und-edge-case`](skills/spezial-saumselig-sonderfall-und-edge-case/SKILL.md), [`spezial-werden-internationaler-bezug-und-schnittstellen`](skills/spezial-werden-internationaler-bezug-und-schnittstellen/SKILL.md), [`titulierung-streckung-leitfaden`](skills/titulierung-streckung-leitfaden/SKILL.md), [`urkundenprozess-pruefen`](skills/urkundenprozess-pruefen/SKILL.md), [`verjaehrung-pruefen`](skills/verjaehrung-pruefen/SKILL.md), [`workflow-orchestrierung`](skills/workflow-orchestrierung/SKILL.md), ... plus 1 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 86 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`aktenordner-erstlekture`](skills/aktenordner-erstlekture/SKILL.md) | Wenn es um Aktenordner-Erstlektüre in Forderungsmanagement — Klagewerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`anspruchsschriftsatz-bausteine`](skills/anspruchsschriftsatz-bausteine/SKILL.md) | Wenn es um Anspruchsschriftsatz Bausteine in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`belegte-compliance-aktenvermerk`](skills/belegte-compliance-aktenvermerk/SKILL.md) | Wenn es um Belegte Compliance Aktenvermerk in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`chronologie-belegmatrix`](skills/chronologie-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumente Intake in Forderungsmanagement — Klagewerkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`erstpruefung-rollen-mandatsziel`](skills/erstpruefung-rollen-mandatsziel/SKILL.md) | Wenn es um Erstpruefung Rollen und Mandatsziel in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`faellige-zahlen-schwellen`](skills/faellige-zahlen-schwellen/SKILL.md) | Wenn es um Faellige Zahlen und Schwellen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`fehlerkatalog`](skills/fehlerkatalog/SKILL.md) | Wenn es um Fehlerkatalog Forderungsmanagement in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagen... |
| [`fmkw-mahnverfahren-bauleiter`](skills/fmkw-mahnverfahren-bauleiter/SKILL.md) | Wenn es um FMKW: Mahnverfahren Bauleiter in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`fmkw-saumselig-streitig-erfahrung-spezial`](skills/fmkw-saumselig-streitig-erfahrung-spezial/SKILL.md) | Wenn es um FMKW: Saumselig Streitig in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`fmkw-titulierung-streckung-leitfaden`](skills/fmkw-titulierung-streckung-leitfaden/SKILL.md) | Wenn es um FMKW: Titulierung Streckung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`fmkw-verbraucherklage-cookies-rdg-spezial`](skills/fmkw-verbraucherklage-cookies-rdg-spezial/SKILL.md) | Wenn es um FMKW: Verbraucherinkasso RDG in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderung-anwaltshonorar-rvg`](skills/forderung-anwaltshonorar-rvg/SKILL.md) | Wenn es um Anwaltshonorar nach RVG in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderung-arzthonorar-goae`](skills/forderung-arzthonorar-goae/SKILL.md) | Wenn es um Arzthonorar nach GOAE und GOZ in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderung-aus-werkvertrag-bgb-bau`](skills/forderung-aus-werkvertrag-bgb-bau/SKILL.md) | Wenn es um Werk-/Bauwerklohn-Forderung in Forderungsmanagement — Klagewerkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`forderung-gegen-gesellschafter-13-gmbhg`](skills/forderung-gegen-gesellschafter-13-gmbhg/SKILL.md) | Wenn es um Forderung gegen Gesellschafter in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderung-gegen-gmbh-gesellschafter`](skills/forderung-gegen-gmbh-gesellschafter/SKILL.md) | Wenn es um Forderung gegen GmbH-Gesellschafter in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| [`forderung-gegen-insolventen-schuldner`](skills/forderung-gegen-insolventen-schuldner/SKILL.md) | Wenn es um Forderung gegen insolventen Schuldner in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`forderung-gegen-verbraucher`](skills/forderung-gegen-verbraucher/SKILL.md) | Wenn es um Forderung gegen Verbraucher in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`forderung-im-ausland-vollstrecken`](skills/forderung-im-ausland-vollstrecken/SKILL.md) | Wenn es um Forderung im Ausland vollstrecken in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| [`forderung-internationaler-bezug`](skills/forderung-internationaler-bezug/SKILL.md) | Wenn es um Forderung mit internationalem Bezug in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`forderung-mietruckstand-zahlungsklage`](skills/forderung-mietruckstand-zahlungsklage/SKILL.md) | Wenn es um Mietrueckstands-Klage in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`forderung-mietrueckstand-zahlungsklage`](skills/forderung-mietrueckstand-zahlungsklage/SKILL.md) | Wenn es um Mietrueckstand – Zahlungsklage Wohnraum in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und An... |
| [`forderung-werkvertrag-bau`](skills/forderung-werkvertrag-bau/SKILL.md) | Wenn es um Werklohnforderung – BGB und Bau in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderung-zwangsvollstreckung-ueberblick`](skills/forderung-zwangsvollstreckung-ueberblick/SKILL.md) | Wenn es um Zwangsvollstreckung Ueberblick in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderungen-interessen-matrix`](skills/forderungen-interessen-matrix/SKILL.md) | Wenn es um Forderungen-Interessen-Matrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderungsaufnahme`](skills/forderungsaufnahme/SKILL.md) | Wenn es um Forderungsaufnahme in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`forderungsmanagement-aufnahme`](skills/forderungsmanagement-aufnahme/SKILL.md) | Wenn es um Forderung aufnehmen in Forderungsmanagement — Klagewerkstatt geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`fristen-risikoampel`](skills/fristen-risikoampel/SKILL.md) | Wenn es um Fristen-Risikoampel in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gatekeeper-verhandlung-vergleich`](skills/gatekeeper-verhandlung-vergleich/SKILL.md) | Wenn es um Gatekeeper Verhandlung und Vergleich in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlag... |
| [`inkasso-risikoampel`](skills/inkasso-risikoampel/SKILL.md) | Wenn es um Inkasso-Risikoampel in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`inkasso-zahlungsklage-ersteller`](skills/inkasso-zahlungsklage-ersteller/SKILL.md) | Wenn es um Inkasso-Zahlungsklage-Ersteller in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Forderungsmanagement Klagewerkstatt ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Kaltstart-Triage Forderungssache in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagen... |
| [`klage-aus-eigenem-skill`](skills/klage-aus-eigenem-skill/SKILL.md) | Wenn es um Klagewerkstatt — Laufzeit aus eigenem Skill in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| [`klage-einreichungslogik`](skills/klage-einreichungslogik/SKILL.md) | Wenn es um Klage-Einreichungslogik in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`klagefreigabe-belegte-forderung`](skills/klagefreigabe-belegte-forderung/SKILL.md) | Wenn es um Klagefreigabe belegte Forderung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`klagevorlage-aus-eigenen-mustern`](skills/klagevorlage-aus-eigenen-mustern/SKILL.md) | Wenn es um Klagewerkstatt — Lernlauf aus eigenen Mustern in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung... |
| [`kostenfeststellungsklage-verzugsschaden-erledigung`](skills/kostenfeststellungsklage-verzugsschaden-erledigung/SKILL.md) | Wenn es um Kostenfeststellungsklage nach Zahlung auf die Forderung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, B... |
| [`mahnbescheid-online`](skills/mahnbescheid-online/SKILL.md) | Wenn es um Mahnbescheid online in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mahnbescheid-online-mb`](skills/mahnbescheid-online-mb/SKILL.md) | Wenn es um Mahnbescheid (Online-MB) in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`mahnung-aussergerichtlich-stufenmodell`](skills/mahnung-aussergerichtlich-stufenmodell/SKILL.md) | Wenn es um Mahnung aussergerichtlich – Stufenmodell in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und A... |
| [`mahnverfahren-bauleiter`](skills/mahnverfahren-bauleiter/SKILL.md) | Wenn es um Mahnverfahren bei Bauforderungen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlo... |
| [`mahnverfahren-beweislast-darlegungslast`](skills/mahnverfahren-beweislast-darlegungslast/SKILL.md) | Wenn es um Beweislast und Darlegungslast in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`mahnvorlauf-dokumentenmatrix`](skills/mahnvorlauf-dokumentenmatrix/SKILL.md) | Wenn es um Mahnvorlauf Dokumentenmatrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenkommunikation`](skills/mandantenkommunikation/SKILL.md) | Wenn es um Mandantenkommunikation in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output waehlen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellenkarte`](skills/quellenkarte/SKILL.md) | Wenn es um Quellenkarte in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`redteam-qualitygate`](skills/redteam-qualitygate/SKILL.md) | Wenn es um Redteam Qualitygate in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`saumselig-sonderfall-edge-case`](skills/saumselig-sonderfall-edge-case/SKILL.md) | Wenn es um Saumselige Sonderfaelle in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`spezial-anspruchs-schriftsatz-brief-und-memo-bausteine`](skills/spezial-anspruchs-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Anspruchs: Schriftsatz-, Brief- und Memo-Bausteine in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begrün... |
| [`spezial-belegte-compliance-dokumentation-und-akte`](skills/spezial-belegte-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Belegte: Compliance-Dokumentation und Aktenvermerk in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begrün... |
| [`spezial-faellige-zahlen-schwellen-und-berechnung`](skills/spezial-faellige-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Faellige: Zahlen, Schwellenwerte und Berechnung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründun... |
| [`spezial-fmkw-mandantenkommunikation-entscheidungsvorlage`](skills/spezial-fmkw-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Fmkw: Mandantenkommunikation und Entscheidungsvorlage in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Mandantennachricht oder Entscheidungsvo... |
| [`spezial-forderungen-mehrparteien-konflikt-und-interessen`](skills/spezial-forderungen-mehrparteien-konflikt-und-interessen/SKILL.md) | Wenn es um Forderungen: Mehrparteienkonflikt und Interessenmatrix in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Be... |
| [`spezial-forderungsmanagement-tatbestand-beweis-und-belege`](skills/spezial-forderungsmanagement-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Forderungsmanagement: Tatbestandsmerkmale, Beweisfragen und Beleglage in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf m... |
| [`spezial-freigegeben-red-team-und-qualitaetskontrolle`](skills/spezial-freigegeben-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Freigegeben: Red-Team und Qualitätskontrolle in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-gatekeeper-verhandlung-vergleich-und-eskalation`](skills/spezial-gatekeeper-verhandlung-vergleich-und-eskalation/SKILL.md) | Wenn es um Gatekeeper: Verhandlung, Vergleich und Eskalation in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründ... |
| [`spezial-inkasso-risikoampel-und-gegenargumente`](skills/spezial-inkasso-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Inkasso: Risikoampel, Gegenargumente und Verteidigungslinien in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sof... |
| [`spezial-klage-formular-portal-und-einreichung`](skills/spezial-klage-formular-portal-und-einreichung/SKILL.md) | Wenn es um Klage: Formular, Portal und Einreichungslogik in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung... |
| [`spezial-klagefreigabe-belegte-forderung`](skills/spezial-klagefreigabe-belegte-forderung/SKILL.md) | Wenn es um Klagefreigabe nur für fällige, belegte und prozessreife Forderungen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit... |
| [`spezial-klagewerkstatt-erstpruefung-und-mandatsziel`](skills/spezial-klagewerkstatt-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sof... |
| [`spezial-klare-livequellen-und-rechtsprechungscheck`](skills/spezial-klare-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Klare: Livequellen- und Rechtsprechungscheck in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung u... |
| [`spezial-mahnverfahren-beweislast-und-darlegungslast`](skills/spezial-mahnverfahren-beweislast-und-darlegungslast/SKILL.md) | Wenn es um Mahnverfahren: Beweislast, Darlegungslast und Substantiierung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträ... |
| [`spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste`](skills/spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Mahnvorlauf: Dokumentenmatrix, Lückenliste und Nachforderung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträg... |
| [`spezial-saumselig-sonderfall-und-edge-case`](skills/spezial-saumselig-sonderfall-und-edge-case/SKILL.md) | Wenn es um Saumselig: Sonderfall und Edge-Case-Prüfung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| [`spezial-werden-internationaler-bezug-und-schnittstellen`](skills/spezial-werden-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Werden: Internationaler Bezug und Schnittstellen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründu... |
| [`spezial-zahlungsklage-behoerden-gericht-und-registerweg`](skills/spezial-zahlungsklage-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Zahlungsklage: Behörden-, Gerichts- oder Registerweg in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begr... |
| [`spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit`](skills/spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um Zustaendigkeitspruefung: Fristen, Form, Zuständigkeit und Rechtsweg in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel... |
| [`tatbestand-beweis-belege`](skills/tatbestand-beweis-belege/SKILL.md) | Wenn es um Tatbestand Beweis Belege in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`titulierung-streckung-leitfaden`](skills/titulierung-streckung-leitfaden/SKILL.md) | Wenn es um Titulierung und Streckung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`urkundenprozess-pruefen`](skills/urkundenprozess-pruefen/SKILL.md) | Wenn es um Urkundenprozess in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`verbraucherklage-rdg-grenzen`](skills/verbraucherklage-rdg-grenzen/SKILL.md) | Wenn es um Verbraucherklage RDG-Grenzen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`verjaehrung-pruefen`](skills/verjaehrung-pruefen/SKILL.md) | Wenn es um Verjährung prüfen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vollstreckungsbescheid-folgen`](skills/vollstreckungsbescheid-folgen/SKILL.md) | Wenn es um Vollstreckungsbescheid und Folgen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenl... |
| [`vollstreckungsbescheid-und-folgen`](skills/vollstreckungsbescheid-und-folgen/SKILL.md) | Wenn es um Vollstreckungsbescheid in Forderungsmanagement — Klagewerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Forderungsmanagement — Klagewerkstatt geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-orchestrierung`](skills/workflow-orchestrierung/SKILL.md) | Wenn es um Workflow-Orchestrierung in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`zahlungsklage-behoerden-register`](skills/zahlungsklage-behoerden-register/SKILL.md) | Wenn es um Zahlungsklage gegen Behörden und juristische Personen öffentlichen Rechts in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwu... |
| [`zahlungsklage-erstellen`](skills/zahlungsklage-erstellen/SKILL.md) | Wenn es um Zahlungsklage erstellen in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`zahlungsklage-versandmappe-endfertigen`](skills/zahlungsklage-versandmappe-endfertigen/SKILL.md) | Endfertigt Zahlungsklage, Mahnübergang, Urkundenprozess und Erwiderung im Forderungsmanagement: prüft Anspruch, Fälligkeit, Verzug, Zuständigkeit, Antrag und Zinslauf, verknüpft Vertrag, Leistung, Rechnung, Mahnung und Zahlungen und lief... |
| [`zinsberechnung-288-bgb`](skills/zinsberechnung-288-bgb/SKILL.md) | Wenn es um Zinsberechnung Paragraf 288 BGB in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`zustaendigkeitspruefung-mahngericht`](skills/zustaendigkeitspruefung-mahngericht/SKILL.md) | Wenn es um Zuständigkeitspruefung in Forderungsmanagement — Klagewerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`zwangsvollstreckung-ueberblick`](skills/zwangsvollstreckung-ueberblick/SKILL.md) | Wenn es um Zwangsvollstreckung Überblick in Forderungsmanagement — Klagewerkstatt geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
