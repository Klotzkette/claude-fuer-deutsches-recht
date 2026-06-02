# Forderungsmanagement — Klagewerkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forderungsmanagement-klagewerkstatt`) | [`forderungsmanagement-klagewerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Inkasso-Zahlungsklage ModeFuchs** (`inkasso-zahlungsklage-modefuchs`) | [Gesamt-PDF lesen](../testakten/inkasso-zahlungsklage-modefuchs/gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf) | [`testakte-inkasso-zahlungsklage-modefuchs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Generalisierter Klage-Assistent für Inkasso- und Forderungsmanagement-Klagen mit eigenem Plugin-Generator.** Aus eigenen Mustern eine hauseigene Standardvorlage destillieren, online die Zuständigkeit prüfen, die Klage erzeugen und als sofort installierbares Mini-Plugin verpacken. Neu hinzu kommt ein direkter Inkasso-Zahlungsklage-Ersteller mit Mahnvorlauf, Anspruchs-Gatekeeper und der harten Regel: nur klare, fällige und belegte Ansprüche einklagen.

---

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin / Testakte | Direkt-Download |
| --- | --- |
| **forderungsmanagement-klagewerkstatt** (dieses Plugin) | [forderungsmanagement-klagewerkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| **Testakte ModeFuchs** (Referenzfall Inkasso-Zahlungsklage) | [testakte-inkasso-zahlungsklage-modefuchs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |
| prozessrecht (sinnvolle Ergänzung) | [prozessrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |
| Liquiditätsplanung (`liquiditaetsplanung`, Folgeprüfung) | [liquiditaetsplanung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |

Die URLs sind **stabil** und zeigen immer auf die neueste Version. Alle weiteren Plugins (Vertragsrecht, Arbeitsrecht, Datenschutz, …) liegen unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest).

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

---

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Inkasso-Zahlungsklage ModeFuchs** ([`testakten/inkasso-zahlungsklage-modefuchs/`](../testakten/inkasso-zahlungsklage-modefuchs/)).

Direkt-Download als ZIP: [testakte-inkasso-zahlungsklage-modefuchs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Was ist drin

Drei Skills, gedacht als Lernlauf-+-Laufzeit-Paar plus direkter Inkasso-Klageassistent:

| Skill | Zweck |
| --- | --- |
| `klagevorlage-aus-eigenen-mustern` | **Lernlauf**: frisst eigene Klagemuster, Urteile, Kommentare, Aufsätze, Formatvorlagen; destilliert die hauseigene Standardklage-Vorlage; sammelt den Sachverhalt; **prüft online die Zuständigkeit** (justizadressen.nrw.de, justiz.de); liefert die Klage und erzeugt zusätzlich ein eigenes installierbares **Mini-Plugin als ZIP**. |
| `klage-aus-eigenem-skill` | **Laufzeit**: setzt voraus, dass das im Lernlauf erzeugte Mini-Plugin installiert ist. Nimmt nur noch Sachverhalt und Beklagtenadresse, prüft erneut online die Zuständigkeit, befüllt die Hausvorlage. Keine erneute Extraktion. |
| `inkasso-zahlungsklage-ersteller` | **Direktlauf**: liest Forderungsakte, Mahnungen, Abtretung, Inkassoschreiben, Teilzahlungen, Mahnbescheid/Widerspruch und vorhandene Klagen; erstellt Mahnchronologie, Anspruchsmatrix und Gerichtsortprüfung; nimmt nur grüne Positionen in den Klageentwurf. Bezahlte Hauptforderungen werden rot geblockt. |

Alle Klage-Skills führen **bei jedem Lauf** die Online-Zuständigkeitsprüfung über [justizadressen.nrw.de](https://www.justizadressen.nrw.de/de/justiz/suche) und das [bundesweite Justizportal](https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php) durch.

## Inkasso-Zahlungsklage-Ersteller

Der neue Direktlauf ist für Fälle gedacht, in denen eine Forderungsakte schon einen Mahn- oder Inkassoverlauf enthält. Er prüft vor der Klage:

- Rechnung, Fälligkeit, Lieferung/Leistung und Abtretung.
- Mahnvorlauf mit Zugang, Fristen und Beträgen.
- Zahlungseingänge, Teilzahlungen, Erfüllung und interne Kenntnis.
- Mahnkosten, Verzugszinsen, Inkassokosten und Mahnverfahrenskosten einzeln.
- Gerichtsort mit aktueller ladungsfähiger Anschrift.

Die ModeFuchs-Testakte unter [`testakten/inkasso-zahlungsklage-modefuchs/`](../testakten/inkasso-zahlungsklage-modefuchs/) ist der Referenzfall: Hauptforderung 698,00 EUR bezahlt vor Klageeinreichung, Nebenforderungen 99,84 EUR streitig. Erwartung: Hauptforderung rot, Nebenforderungen gelb, keine automatische Klage über 797,84 EUR.

[testakte-inkasso-zahlungsklage-modefuchs.zip herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip)

## Plugin-Generator

Aus den extrahierten Hausregeln und der Standardvorlage packt der Skill ein eigenes, in Claude Code direkt installierbares ZIP:

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

1. **Sachlich** rechnerisch: ≤ 10.000 EUR → AG (§ 23 Nr. 1 GVG i. d. F. seit 1.1.2026); > 10.000 EUR → LG (§ 71 GVG); Sondertatbestände beachten (insbes. Wohnraummietsachen AG ohne Streitwertgrenze, § 23 Nr. 2a GVG).
2. **Örtlich** rechtlich: §§ 12, 13 ZPO Allgemeiner Gerichtsstand, § 29 ZPO Erfüllungsort, § 29c ZPO Verbraucherverträge, § 38 ZPO Gerichtsstandsvereinbarung; grenzüberschreitend Brüssel Ia VO 1215/2012.
3. **Online-Adressrecherche**: `justizadressen.nrw.de` (PLZ/Ort) und bundesweit `justiz.de`; Quelle und Abrufdatum dokumentieren.
4. BeA-SAFE-ID: aus dem beA-Adressbuch zu ergänzen.

## Leitentscheidungen (Auswahl, siehe `references/rechtsprechung/INDEX.md`)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Forderungsmanagement Klagewerkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen kl... |
| `fmkw-mahnverfahren-bauleiter` | Bauleiter automatisiertes Mahnverfahren §§ 688 ff. ZPO: Mahnbescheid, Widerspruch, Vollstreckungsbescheid. Pruefraster fuer Glaeubiger und Inkassodienstleister. |
| `fmkw-saumselig-streitig-erfahrung-spezial` | Spezialfall saeumiges Verfahren und streitiges Verfahren nach Widerspruch: prozessuale Weichen, Beweislast, Schriftsaetze. Pruefraster fuer Klaegeranwalt. |
| `fmkw-titulierung-streckung-leitfaden` | Leitfaden Titulierung mit Ratenzahlung und Streckung: Anerkenntnis, Schuldanerkenntnis, Ratenvereinbarung mit Vollstreckungsmoeglichkeit. Pruefraster fuer Inkassoanwalt. |
| `fmkw-verbraucherklage-cookies-rdg-spezial` | Spezialfall Verbraucherklageinkasso und RDG-Grenzen: Massenforderungen, Sammelklage als Modell, Anti-Claim-Klausel. Pruefraster fuer Legal-Tech und Anwaelte. |
| `forderung-anwaltshonorar-rvg` | Anwaltshonorar nach RVG einklagen: Vereinbarung § 3a RVG, Vergleich, Streitwertfestsetzung, Honorartoleranz. Pruefraster: Wirksame Vergueltungsvereinbarung? Mandantenbeschwerde Rechtsanwaltskammer? Output: Klageschrift und Vorpruefung. |
| `forderung-arzthonorar-goae` | Arzthonorar nach GOAE/GOZ: Faelligkeit § 12 GOAE Rechnungserteilung mit Beschreibung der Leistungen, Wirksamkeit § 4 GOAE, Steigerungsfaktor. Streitige Punkte: angemessene Honorarsteigerung. Output: Klageschrift. |
| `forderung-aus-werkvertrag-bgb-bau` | Forderung aus Werk-/Bauvertrag: Faelligkeit § 641 BGB, Abnahme/Abnahmewirkungen, Schlussrechnungspruefung, Sicherungseinbehalt, Maengelrechte als Einwendung. Output: Pruefraster und Schriftsatz-Module. |
| `forderung-gegen-gesellschafter-13-gmbhg` | Forderung gegen GmbH-Gesellschafter: § 19 sowie § 31 GmbHG (Einlagepflicht, Rueckforderung), § 13 Abs. 2 GmbHG Trennungsprinzip, Durchgriffshaftung bei existenzvernichtendem Eingriff (BGH II ZR 78/06). Pruefraster. |
| `forderung-gegen-insolventen-schuldner` | Forderung gegen insolventen Schuldner: Anmeldung zur Tabelle § 174 InsO, Frist Pruefungstermin, abgesonderte Befriedigung pruefen, Aussonderungsrechte § 47 InsO. Strategische Bewertung Aussichten. |
| `forderung-im-ausland-vollstrecken` | Forderung im EU-Ausland vollstrecken: Brueessel Ia VO (EU 1215/2012), Europaeischer Vollstreckungstitel (EuVTVO), Europ. Mahnverfahren (EuMVVO), Europ. Bagatellverfahren (EuGFVO). Output: Verfahrenswahl-Memo. |
| `forderung-mietruckstand-zahlungsklage` | Mietrueckstand: Zahlungsklage parallel zu Raumungsklage § 543 BGB. Pflicht Mahnung? In der Regel nicht erforderlich (kalendermaessig bestimmt). Schonfristregelung § 569 Abs. 3 BGB. Output: Klageschrift Zahlungsklage + Raumungsklage. |
| `forderung-verbraucher-erleichterungen` | Forderung gegen Verbraucher: Verbraucherschutzregeln, AGB-Kontrolle §§ 305 ff. BGB, Belehrungspflichten Verzugskosten § 288 Abs. 4 BGB, Kostenausschluss § 91 ZPO bei Bagatellsachen. Pruefraster. |
| `forderung-zwangsvollstreckung-ueberblick` | Zwangsvollstreckung Ueberblick: Mobiliarvollstreckung Gerichtsvollzieher §§ 808 ff. ZPO, Forderungspfaendung § 829 ZPO, Lohnpfaendung mit Pfaendungstabelle, Immobiliarvollstreckung Zwangshypothek/Versteigerung. Output: Strategiememo Voll... |
| `forderungsmanagement-aufnahme` | Forderung systematisch aufnehmen: Glaeubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen § 288 BGB, vorgerichtliche Anwaltskosten, Mahngebuehren), Faelligkeit, Verjaehrungsbeginn. Output: vollstaendige Forderungsbes... |
| `inkasso-zahlungsklage-ersteller` | Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten § 288 BGB Gerichtsortfin... |
| `klage-aus-eigenem-skill` | Kanzlei hat hauseigenes Klage-Plugin (klagewerkstatt-kanzlei) installiert und will damit Klagen aus eigenem Sachverhalt erstellen. Laufzeit-Variante Klagewerkstatt. Prüfraster: Sachverhalt Beklagtenadresse Zuständigkeit §§ 12 13 29 29c Z... |
| `klagevorlage-aus-eigenen-mustern` | Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage Zuständigkeitsprüfung on... |
| `mahnbescheid-online-mb` | Mahnbescheid Online-Mahnbescheid (Online-MB): wann sinnvoll, Voraussetzungen § 690 ZPO, zustaendiges Mahngericht (zentrales Online-Mahngericht), Online-Antrag, Zustellung an Schuldner, Folge Widerspruch fuehrt in streitiges Verfahren. Pr... |
| `mahnung-aussergerichtlich-stufenmodell` | Aussergerichtliches Mahnverfahren in Stufen: 1. Mahnung kostenfrei, 2. Mahnung mit Frist, 3. Mahnung mit Anwaltsandrohung. Beleg fuer Verzugseintritt § 286 BGB, Schwelle § 288 Abs. 2 BGB. Output: Mahnschreiben-Templates. |
| `spezial-anspruchs-schriftsatz-brief-und-memo-bausteine` | Anspruchs: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-belegte-compliance-dokumentation-und-akte` | Belegte: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-faellige-zahlen-schwellen-und-berechnung` | Faellige: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fmkw-mandantenkommunikation-entscheidungsvorlage` | Fmkw: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-forderungen-mehrparteien-konflikt-und-interessen` | Forderungen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-forderungsmanagement-tatbestand-beweis-und-belege` | Forderungsmanagement: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-freigegeben-red-team-und-qualitaetskontrolle` | Freigegeben: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gatekeeper-verhandlung-vergleich-und-eskalation` | Gatekeeper: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-inkasso-risikoampel-und-gegenargumente` | Inkasso: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klage-formular-portal-und-einreichung` | Klage: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klagefreigabe-belegte-forderung` | Klagefreigabe nur für fällige, belegte und prozessreife Forderungen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-klagewerkstatt-erstpruefung-und-mandatsziel` | Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-klare-livequellen-und-rechtsprechungscheck` | Klare: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mahnverfahren-beweislast-und-darlegungslast` | Mahnverfahren: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste` | Mahnvorlauf: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-saumselig-sonderfall-und-edge-case` | Saumselig: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-werden-internationaler-bezug-und-schnittstellen` | Werden: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zahlungsklage-behoerden-gericht-und-registerweg` | Zahlungsklage: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit` | Zustaendigkeitspruefung: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `urkundenprozess-pruefen` | Urkundenprozess §§ 592-605 ZPO pruefen: Anspruch auf Zahlung auf Urkunden gestuetzt (Vertrag, Wechsel, Scheck). Vorteil: schnelles Vorbehaltsurteil. Pruefraster: passt der Fall? Output: Klageschrift im Urkundenprozess. |
| `verjaehrung-pruefen` | Verjaehrung pruefen: Regelverjaehrung § 195 BGB drei Jahre ab Schluss des Jahres, in dem Forderung entstanden ist. Sonderverjaehrungen (Werklohn 3 J., Kaufpreis 3 J., Schadensersatz §§ 199 ff. BGB). Hemmung § 203 BGB, Neubeginn § 212 BGB. |
| `vollstreckungsbescheid-und-folgen` | Vollstreckungsbescheid §§ 699 und 700 ZPO: Voraussetzung kein Widerspruch innerhalb 2 Wochen, Vollstreckungstitel fuer 30 Jahre, Einspruch noch moeglich (gleicher Fristrahmen wie Widerspruch nach Zustellung). Strategische Hinweise. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin forderungsmanagement-klagewerkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin forderungsmanagement-klagewerkstatt: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin forderungsmanagement-klagewerkstatt: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin forderungsmanagement-klagewerkstatt: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin forderungsmanagement-klagewerkstatt: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin forderungsmanagement-klagewerkstatt: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin forderungsmanagement-klagewerkstatt: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin forderungsmanagement-klagewerkstatt: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin forderungsmanagement-klagewerkstatt: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin forderungsmanagement-klagewerkstatt: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zahlungsklage-erstellen` | Zahlungsklage erstellen: Klageschrift §§ 253 ff. ZPO, Klageantrag, Tatbestand, Beweismittel, Anlagenverzeichnis. Streitwertangabe, Belehrung Rechtsanwaltszwang, Anschrift Schuldner. Output: Klageschrift-Geruest fuer das LG/AG. |
| `zinsberechnung-288-bgb` | Zinsberechnung § 288 BGB: Verbraucherzinsen 5 Prozentpunkte ueber Basiszins, B2B 9 Prozentpunkte. Verzugseintritt § 286 BGB. Pauschale 40 EUR § 288 Abs. 5 BGB im B2B-Geschaeft. Output: Zinsberechnungs-Tabelle. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
