# Forderungsmanagement — Klagewerkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`forderungsmanagement-klagewerkstatt.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/forderungsmanagement-klagewerkstatt.md) (74 KB)
- Im Repo: [`testakten/megaprompts/forderungsmanagement-klagewerkstatt.md`](../testakten/megaprompts/forderungsmanagement-klagewerkstatt.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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

**Generalisierter Klage-Assistent für Inkasso- und Forderungsmanagement-Klagen mit eigenem Plugin-Generator.** Aus eigenen Mustern eine hauseigene Standardvorlage destillieren, online die Zuständigkeit prüfen, die Klage erzeugen und als sofort installierbares Mini-Plugin verpacken. Der Start ist jetzt aktengetrieben: Ordner, ZIP oder Dokumentenstapel zeigen, kurz auslesen lassen, dann mit Parteienhypothese, Forderungsmatrix, Mahnchronologie, Fristenampel und nur noch echten Rückfragen weiterarbeiten. Neu hinzu kommt ein direkter Inkasso-Zahlungsklage-Ersteller mit Mahnvorlauf, Anspruchs-Gatekeeper und der harten Regel: nur klare, fällige und belegte Ansprüche einklagen.

---

---

## So beginnt man

1. Aktenordner, ZIP oder die wichtigsten Dokumente hochladen.
2. `aktenordner-schnellstart` oder `kaltstart-triage` starten.
3. Das Plugin liest zuerst Vollmacht, Rechnung, Vertrag, Mahnung, Kontoauszug, Mahnbescheid, Widerspruch, Klageentwurf und Registerfunde aus.
4. Danach kommt keine lange Einstiegsabfrage, sondern eine Arbeitshypothese: Parteien, Forderung, Zahlungen, Verzug, Verjährung, Verfahrensstand, Engpass.
5. Rückfragen werden auf echte Lücken beschränkt.

## Was ist drin

Kernfunktionen für den Direktlauf aus der Akte heraus:

| Skill | Zweck |
| --- | --- |
| `aktenordner-schnellstart` | **Akten zuerst**: wertet vorhandene Ordner, ZIPs, PDFs, EMLs, Kontoauszüge, Mahnbescheide und Klageentwürfe aus; rekonstruiert Parteien, Forderungsstand, Zahlungen, Mahnverlauf und Fristen; fragt nur noch Lücken ab. |
| `kaltstart-triage` | **Triage ohne Formularfrust**: nimmt die Aktenhypothese auf, sortiert Mahnung, Mahnbescheid, Klage, Vergleich oder Vollstreckung und stellt hoechstens echte Lueckenfragen. |
| `dokumente-intake` | **Belegordnung**: baut aus ungeordneten Dateien ein Akteninventar mit Vertrag, Leistung, Rechnung, Zahlung, Mahnung, Verfahren und Lueckenliste. |
| `klagefreigabe-belegte-forderung` | **Klage-Gatekeeper**: lässt nur schluessige, faellige und belegte Positionen in die Klage; bereits bezahlte Hauptforderungen werden blockiert. |
| `mahnbescheid-online` | **Mahnverfahren**: fuehrt durch den Online-Mahnbescheid, wenn die Forderung klar und der Streit noch nicht ausgebrochen ist. |
| `zahlungsklage-erstellen` | **Klageentwurf**: erzeugt Rubrum, Antrag, Tatsachenvortrag, Beweismittel, Anlagenlogik und Einreichungscheck. |
| `workflow-orchestrierung` | **Akte steuern**: haelt Wiedervorlagen, Fristen, naechste Schritte und Stop-Bedingungen zusammen. |

Der Plugin-Generator bleibt zusaetzlich über `scripts/plugin_aus_hausregeln.py` und die Vorlagen in `assets/vorlagen-leer/` erhalten.

Alle Klage-Skills führen **bei jedem Lauf** die Online-Zuständigkeitsprüfung über [justizadressen.nrw.de](https://www.justizadressen.nrw.de/de/justiz/suche) und das [bundesweite Justizportal](https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php) durch.

## Inkasso-Zahlungsklage-Ersteller

Der neue Direktlauf ist für Fälle gedacht, in denen eine Forderungsakte schon einen Mahn- oder Inkassoverlauf enthält. Er prüft vor der Klage:

- Rechnung, Fälligkeit, Lieferung/Leistung und Abtretung.
- Mahnvorlauf mit Zugang, Fristen und Beträgen.
- Zahlungseingänge, Teilzahlungen, Erfüllung und interne Kenntnis.
- Mahnkosten, Verzugszinsen, Inkassokosten und Mahnverfahrenskosten einzeln.
- Gerichtsort mit aktueller ladungsfähiger Anschrift.

Die ModeFuchs-Testakte unter [`testakten/inkasso-zahlungsklage-modefuchs/`](../testakten/inkasso-zahlungsklage-modefuchs/) ist der Referenzfall: Hauptforderung 698,00 EUR bezahlt vor Klageeinreichung, Nebenforderungen 99,84 EUR streitig. Erwartung: Hauptforderung rot, Nebenforderungen gelb, keine automatische Klage über 797,84 EUR. Direktdownload siehe Sofort-Download-Sektion oben.

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 48 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenordner-schnellstart` | Aktenordner-Schnellstart für Forderungsakten: liest zuerst vorhandene Dokumente, Dateinamen und sichtbare Aktenlogik, rekonstruiert Parteien, Forderung, Zahlungen, Mahnstand, Fristen und naechsten Prozessschritt und fragt danach nur noc... |
| `anschluss-routing` | Anschluss-Routing für Forderungsmanagement Klagewerkstatt: wählt den nächsten Spezial-Skill nach Engpass (Mahnbescheid-Widerspruch 2 Wochen, Mahnung, Mahnbescheid, Vollstreckungsbescheid), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchsschriftsatz-bausteine` | Bausteinkatalog für eine Anspruchsbegruendung in Klage oder Schriftsatz. Liefert Vorlagen für Rubrum Antrag Tatbestand Anspruchsgrund Faelligkeit Verzug Zinsen Verzugsschaden Nebenforderungen Beweis. Pinpoints ZPO 253 Abs. 2 ZPO 130 Schr... |
| `belegte-compliance-aktenvermerk` | Erstellt Compliance-Aktenvermerke bei Klage-Nichtaufnahme Mandantenfreigabe oder begruendetem Klage-Verzicht. Dokumentiert Sachverhalt Prüfraster Mandantenentscheid und Wiedervorlage. Pinpoints BORA 50 Aktenpflicht BRAO 43a Verschwiegen... |
| `chronologie-belegmatrix` | Erstellt eine zeitliche Belegmatrix für eine Forderung von Vertragsschluss bis Klageeingang. Verknuepft Datum Ereignis Beleg Anlage und Beweismittel. Pinpoints ZPO 138 substantiierter Vortrag ZPO 373 ff Beweismittel ZPO 416 Privaturkunde... |
| `dokumente-intake` | Dokumentenintake für Forderungsakten: liest eine vorhandene Ordner- oder ZIP-Struktur zuerst aus, sortiert Vertrag, Leistung, Rechnung, Mahnung, Zahlung, Mahnbescheid, Widerspruch, Titel und Vollstreckungsunterlagen und erzeugt daraus A... |
| `erstpruefung-rollen-mandatsziel` | Rollen- und Mandatszielpruefung nach Aktenlekture: leitet Mandant, Gegner, Vertreter, Ziel und Honorarbasis zuerst aus Vollmacht, Anschreiben, Rechnung, Mahnung und Verfahrensstand ab und fragt nur bei Widerspruch oder Risiko nach. |
| `faellige-zahlen-schwellen` | Zahlentabellen für Faelligkeit Verzug Zinsen Pauschalen Streitwerte und Gebühren in Forderungsverfahren. Liefert aktuelle Basiszinssatz-Werte Verzugszinssaetze Pauschalen B2B Streitwertgrenzen und Gebührentabellen. Pinpoints BGB 247 Basi... |
| `fehlerkatalog` | Katalog typischer Fehler im Forderungsmanagement und Klageweg. Sortiert nach Phase Antrag Mahnbescheid Klage Urteil Vollstreckung. Pinpoints ZPO 690 falscher Antragstyp ZPO 167 verspaetete Vorschusszahlung BGB 286 fehlende Mahnung ZPO 85... |
| `forderung-anwaltshonorar-rvg` | Anwaltshonorar nach RVG einklagen: Vergueetungsvereinbarung § 3a RVG schriftlich, gesetzliche Gebühren §§ 13 ff. RVG, Vorschuss § 9 RVG. Faelligkeit § 8 RVG mit Erledigung Auftrag oder Beendigung Mandat. Berechnungsschritte: Gegenstandsw... |
| `forderung-arzthonorar-goae` | Arzthonorar nach GOAE und GOZ einklagen: Faelligkeit § 12 GOAE mit Rechnungserteilung mit Mindestinhalten Diagnose GOAE-Ziffer und Steigerungsfaktor Regel-Schwellenwert sowie bei Ueberschreitung mit schriftlicher Begruendung. Verjährung... |
| `forderung-gegen-gmbh-gesellschafter` | Forderung gegen GmbH-Gesellschafter persoenlich: § 13 Abs. 2 GmbHG Trennungsprinzip Haftung nur Gesellschaftsvermoegen. Durchgriff bei § 19 GmbHG (Einlagepflicht) § 31 GmbHG (verbotene Auszahlung), existenzvernichtender Eingriff BGH II Z... |
| `forderung-gegen-insolventen-schuldner` | Forderung gegen insolventen Schuldner: Anmeldung zur Insolvenztabelle § 174 InsO binnen Anmeldefrist mit Grund und Höhe. Aussonderung § 47 InsO. Absonderungsrecht §§ 49-52 InsO. Massenforderung § 55 InsO. Nachrangige § 39 InsO. Vollstre... |
| `forderung-gegen-verbraucher` | Forderung gegen Verbraucher: Verbraucherschutzregeln nach § 13 BGB, AGB-Kontrolle §§ 305-309 BGB, Widerrufsrecht bei Fernabsatz §§ 312g, 355 BGB, Belehrungspflicht. Verzugszinsen 5 Prozentpunkte über Basiszinssatz § 288 Abs. 1 BGB. Stre... |
| `forderung-im-ausland-vollstrecken` | Forderung im EU-Ausland vollstrecken: Bruessel Ia VO 1215/2012 (Anerkennung ohne Exequatur), Europaeischer Vollstreckungstitel EuVTVO 805/2004, Europaeischer Zahlungsbefehl EuMVVO 1896/2006, geringfuegige Forderung EuGFVO 861/2007. Dritt... |
| `forderung-internationaler-bezug` | Forderungssache mit Auslandsbezug Schuldner im EU-Ausland oder ausserhalb. Klaert anwendbares Recht internationale Zuständigkeit Vollstreckung. Pinpoints VO 1215/2012 Brüssel Ia VO 1896/2006 EuMVVO VO 805/2004 EuVTVO VO 861/2007 EuGFVO R... |
| `forderung-mietrueckstand-zahlungsklage` | Mietrueckstand: Zahlungsklage parallel zu Raeumungsklage § 543 Abs. 2 Nr. 3 BGB ausserordentliche Kuendigung. Mietzahlung im Voraus zum 3. Werktag § 556b BGB. Schonfristzahlung § 569 Abs. 3 Nr. 2 BGB heilt Kuendigung. Streitwert nach § 4... |
| `forderung-werkvertrag-bau` | Werklohnforderung § 631, § 641 BGB: Faelligkeit nach Abnahme, Schlussrechnung. Bauvertrag §§ 650a ff. BGB (seit 2018), VOB/B als AGB. Abschlagszahlungen § 632a BGB, Sicherheit § 650f BGB. Mangelhaftigkeit § 640 Abs. 2 BGB Abnahmeverweige... |
| `forderungen-interessen-matrix` | Strukturierte Gegenueberstellung mehrerer Forderungen eines Mandanten gegen einen oder mehrere Schuldner. Erfasst Hauptforderung Nebenforderung Zinsen Kosten Faelligkeit Beleg Verjährung. Pinpoints ZPO 260 Klagenhaeufung ZPO 33 Aufrechnu... |
| `forderungsaufnahme` | Forderung systematisch aufnehmen: Gläubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen § 288 BGB, vorgerichtliche Anwaltskosten § 280, § 286 BGB, Mahngebuehren), Faelligkeit § 271 BGB, Verjährungsbeginn § 199 BGB.... |
| `fristen-risikoampel` | Ampel zur Bewertung saemtlicher Fristen in einer Forderungssache von Verjährung Klagefrist Einspruchsfrist Beschwerdefrist bis Vollstreckungsfristen. Pinpoints BGB 195 199 ZPO 339 Einspruchsfrist Versaeumnisurteil ZPO 700 Einspruch Volls... |
| `gatekeeper-verhandlung-vergleich` | Prüfraster vor Eintritt in Vergleichsverhandlungen. Erhebt Mandantenziel Untergrenzen Sicherheitsbedarf Vollstreckbarkeit. Pinpoints BGB 779 Vergleich ZPO 794 Abs. 1 Nr. 1 Prozessvergleich ZPO 796a anwaltlicher Vergleich. Liefert Verhan... |
| `inkasso-risikoampel` | Bewertung der Erfolgswahrscheinlichkeit einer Forderungseinziehung anhand Schuldnerprofil Belegstand Verjährungslage und Vermögenslage. Pinpoints ZPO 802c Vermögensauskunft ZPO 882b Schuldnerverzeichnis InsO 14 Gläubigerantrag. Liefer... |
| `kaltstart-triage` | Dokumentengetriebene Ersttriage einer Forderungsakte: wertet zuerst Ordner, ZIP, Rechnungen, Mahnungen, Kontoauszuege, Mahnbescheid, Widerspruch oder Klageentwurf aus, bildet eine Aktenhypothese und fragt danach nur echte Luecken ab. Pin... |
| `klage-einreichungslogik` | Praktische Einreichungslogik einer Zahlungsklage. Klaert Zuständigkeit Gerichtskostenvorschuss beA-Pflicht Anzahl Abschriften Anlagenbezeichnung und Zustellung. Pinpoints ZPO 130d beA-Pflicht ZPO 253 Klageinhalt ZPO 167 Rueckwirkung Zust... |
| `klagefreigabe-belegte-forderung` | Prüfraster ob eine Forderung klagefaehig ist. Verlangt Belegnachweis Faelligkeit Verzug Verjährung Zustellfaehigkeit und positive Aussicht. Pinpoints ZPO 253 ZPO 138 BGB 286 BGB 195 BGB 199 ZPO 167. Liefert binaere Klagefreigabe-Entsche... |
| `mahnbescheid-online` | Mahnbescheid (§§ 688-703d ZPO) online beantragen: zentrales Mahngericht je Bundesland, online-mahnbescheid.de, Widerspruchsfrist 2 Wochen § 692 ZPO, Vollstreckungsbescheid § 699 ZPO. Vorteile gegenueber Klage: niedrigere Kosten, schnelle... |
| `mahnung-aussergerichtlich-stufenmodell` | Aussergerichtliches Mahnverfahren in Stufen: 1. kostenfreie Erinnerung, 2. erste Mahnung verzugsbegruendend § 286 BGB, 3. zweite/letzte Mahnung mit Fristsetzung. B2B: 30-Tage-Regel § 286 Abs. 3 BGB. Verbraucher: Belehrungspflicht. Output... |
| `mahnverfahren-bauleiter` | Spezielles Mahnverfahren bei Werklohnanspruechen aus Bauvertraegen. Beruecksichtigt Faelligkeit nach Abnahme BGB 641 Maengelrechte BGB 634 Bauhandwerkersicherung BGB 650f. Pinpoints ZPO 688 ZPO 690 BGB 641 BGB 650f. Liefert Prüfliste fü... |
| `mahnverfahren-beweislast-darlegungslast` | Beweislast und Darlegungslast in Mahnverfahren und Klage: Kläger traegt Darlegungs- und Beweislast für anspruchsbegruendende Tatsachen. Substantiierungspflicht § 138 ZPO, Wahrheitspflicht, Bestreiten mit Nichtwissen § 138 Abs. 4 ZPO. Se... |
| `mahnvorlauf-dokumentenmatrix` | Dokumentiert den aussergerichtlichen Mahnvorlauf in einer Matrix von Erstmahnung bis letzter Frist. Verknuepft Datum Mahnstufe Empfaenger Zugang Zahlungseingang. Pinpoints BGB 286 Abs. 1 Verzug durch Mahnung Abs. 2 Nr. 1 kalendarische Be... |
| `mandantenkommunikation` | Strukturierte Mandantenkommunikation waehrend einer Forderungssache. Definiert Anlaesse Inhalte und Form für Mandanteninformation Auftragsbestaetigung Sachstand Vergleich Zustimmung und Abschluss. Pinpoints BORA 11 unverzuegliche Informa... |
| `output-waehlen` | Output-Wahl für Forderungsmanagement Klagewerkstatt: stimmt Adressat (Gläubiger, Schuldner, Gerichtsvollzieher), Frist (Mahnbescheid-Widerspruch 2 Wochen) und Form auf den Zweck ab — typische Outputs: Mahnung, Mahnbescheid online (zentra... |
| `quellenkarte` | Kuratierte Quellenkarte für Forderungsmanagement Klagewerkstatt. Sortiert nach Gesetzen Rechtsprechung Verordnungen EU-Recht und Praxis-Literatur. Pinpoints ZPO BGB GVG GKG RVG InsO und EU-Verordnungen Brüssel Ia EuMVVO EuVTVO EuGFVO. Li... |
| `redteam-qualitygate` | Red-Team-Review eines fertigen Schriftsatzes oder Mahnbescheidsantrags. Sucht aus Sicht der Gegenseite nach Angriffsflaechen Schwaechen Beweisluecken und Form-Fehlern. Pinpoints ZPO 138 substantiiertes Bestreiten ZPO 296 Verspaetungsprae... |
| `saumselig-sonderfall-edge-case` | Spezielle Fallkonstellationen die vom Standard abweichen. Schuldner ist unbekannt verstorben verzogen ins Ausland oder unter Betreuung. Pinpoints ZPO 185 öffentliche Zustellung BGB 1922 Erbfolge BGB 1896 Betreuung ZPO 50 Parteifaehigkeit... |
| `tatbestand-beweis-belege` | Schluessige Tatbestandsdarstellung in einer Klage oder einem Schriftsatz mit Verknuepfung zu Beweisen und Belegen. Verlangt zeitliche Reihenfolge konkrete Tatsachen mit Beweismitteln Anlagenverweis. Pinpoints ZPO 138 Wahrheitspflicht ZPO... |
| `titulierung-streckung-leitfaden` | Strategie zur Titulierung einer Forderung und Streckung der Vollstreckung durch Ratenzahlungsvereinbarung notarielle Schuldanerkenntnis oder vollstreckbare Urkunde. Pinpoints ZPO 794 Abs. 1 Nr. 1 Vergleich Nr. 5 notarielle Urkunde BGB 78... |
| `urkundenprozess-pruefen` | Urkundenprozess §§ 592-605 ZPO prüfen: Anspruch auf Zahlung auf Urkunden gestuetzt (Vertrag, Schuldschein, Wechsel, Scheck). Beschraenkung Beweismittel Urkunden + Parteivernehmung § 595 Abs. 2 ZPO. Vorbehaltsurteil § 599 ZPO mit Nachver... |
| `verbraucherklage-rdg-grenzen` | Prüfung was Inkassodienstleister und Rechtsanwaelte gegenueber Verbrauchern dürfen und was nicht. Trennt Inkassoerlaubnis von anwaltlicher Vertretung. Pinpoints RDG 2 RDG 10 RDG 11a Hinweispflicht BGB 312j AGB-Kontrolle 305 ff. Liefert... |
| `verjaehrung-pruefen` | Verjährung prüfen: Regelverjaehrung § 195 BGB drei Jahre, Beginn § 199 BGB Schluss des Jahres mit Kenntnis. Hoechstfristen § 199 Abs. 2-4 BGB (10/30 Jahre). Hemmung § 203 BGB (Verhandlungen), § 204 BGB (Rechtsverfolgung). Neubeginn § 21... |
| `vollstreckungsbescheid-folgen` | Vollstreckungsbescheid §§ 699 und 700 ZPO: Voraussetzung kein Widerspruch innerhalb 2 Wochen § 692 Abs. 1 Nr. 3 ZPO, Antrag binnen 6 Monaten § 701 ZPO. Vollstreckungstitel § 794 Abs. 1 Nr. 4 ZPO. Verjährung 30 Jahre § 197 Abs. 1 Nr. 4 BG... |
| `workflow-orchestrierung` | Steuert den Gesamtablauf einer Forderungsakte vom Eingang bis zur Vollstreckung oder Abschreibung. Definiert Workflow-Stufen Eingang Prüfung Mahnung Mahnbescheid Klage Titel Vollstreckung Erloesverwertung. Pinpoints ZPO 91 Kostenfolge Z... |
| `zahlungsklage-behoerden-register` | Hilfe bei Klagen gegen Behörden und juristische Personen des öffentlichen Rechts. Klaert Verwaltungsweg oder Zivilweg Klägervertreter Vorverfahren Verfahrensart. Pinpoints VwGO 40 abgrenzbare öffentlich-rechtliche Streitigkeit ZPO 253... |
| `zahlungsklage-erstellen` | Zahlungsklage erstellen nach §§ 253 ff. ZPO: Rubrum, Klageantrag, Streitwertangabe § 3 ZPO, Tatbestand, Beweismittel, Anlagenverzeichnis, Unterschrift. Pflichtbestandteile § 253 Abs. 2 ZPO, Belehrung Anwaltszwang § 78 ZPO. Output: vollst... |
| `zinsberechnung-288-bgb` | Zinsberechnung nach § 288 BGB: Verbraucherverzug 5 Prozentpunkte über Basiszinssatz, B2B-Verzug 9 Prozentpunkte. Verzugspauschale 40 EUR § 288 Abs. 5 BGB B2B. Basiszinssatz § 247 BGB halbjaehrlich anpasst durch Deutsche Bundesbank (Stan... |
| `zustaendigkeitspruefung-mahngericht` | Sachliche § 23 Nr. 1 GVG (AG bis 10.000 EUR ab 01.01.2026) und § 71 GVG (LG ab 10.001 EUR), oertliche Zuständigkeit §§ 12-17 ZPO (allgemeiner Gerichtsstand Wohnsitz Schuldner), besondere Gerichtsstaende §§ 20-32 ZPO. Internationale Zustä... |
| `zwangsvollstreckung-ueberblick` | Zwangsvollstreckung Überblick: Mobiliarvollstreckung Gerichtsvollzieher §§ 808 ff. ZPO, Forderungspfaendung §§ 828 ff. ZPO (Konto, Lohn), Immobiliarvollstreckung §§ 866 ff. ZPO und ZVG, Vermögensauskunft § 802c ZPO. Voraussetzung: Voll... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
