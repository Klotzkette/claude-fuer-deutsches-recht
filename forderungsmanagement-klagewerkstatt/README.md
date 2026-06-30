# Forderungsmanagement — Klagewerkstatt

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`forderungsmanagement-klagewerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forderungsmanagement-klagewerkstatt.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/forderungsmanagement-klagewerkstatt/forderungsmanagement-klagewerkstatt-werkstatt.md" download><code>forderungsmanagement-klagewerkstatt-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/forderungsmanagement-klagewerkstatt/forderungsmanagement-klagewerkstatt-schnellstart.md" download><code>forderungsmanagement-klagewerkstatt-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Akte Inkasso-Zahlungsklage ModeFuchs: [Gesamt-PDF](../testakten/inkasso-zahlungsklage-modefuchs/gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf), [`testakte-inkasso-zahlungsklage-modefuchs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip), [`testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
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

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 84 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenordner-erstlekture` | Aktenordner-Erstlektüre fuer Forderungsakten: liest zuerst vorhandene Dokumente, Dateinamen und sichtbare Aktenlogik, rekonstruiert Parteien, Forderung, Zahlungen, Mahnstand, Fristen und naechsten Prozessschritt und fragt danach nur noch... |
| `anschluss-routing` | Anschluss-Routing für Forderungsmanagement Klagewerkstatt: wählt den nächsten Spezial-Skill nach Engpass (Mahnbescheid-Widerspruch 2 Wochen, Mahnung, Mahnbescheid, Vollstreckungsbescheid), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchsschriftsatz-bausteine` | Bausteinkatalog für eine Anspruchsbegruendung in Klage oder Schriftsatz. Liefert Vorlagen für Rubrum Antrag Tatbestand Anspruchsgrund Faelligkeit Verzug Zinsen Verzugsschaden Nebenforderungen Beweis. Pinpoints ZPO 253 Abs. 2 ZPO 130 Schr... |
| `belegte-compliance-aktenvermerk` | Erstellt Compliance-Aktenvermerke bei Klage-Nichtaufnahme Mandantenfreigabe oder begruendetem Klage-Verzicht. Dokumentiert Sachverhalt Prüfraster Mandantenentscheid und Wiedervorlage. Pinpoints BORA 50 Aktenpflicht BRAO 43a Verschwiegenh... |
| `chronologie-belegmatrix` | Erstellt eine zeitliche Belegmatrix für eine Forderung von Vertragsschluss bis Klageeingang. Verknuepft Datum Ereignis Beleg Anlage und Beweismittel. Pinpoints ZPO 138 substantiierter Vortrag ZPO 373 ff Beweismittel ZPO 416 Privaturkunde... |
| `dokumente-intake` | Dokumentenintake fuer Forderungsakten: liest eine vorhandene Ordner- oder ZIP-Struktur zuerst aus, sortiert Vertrag, Leistung, Rechnung, Mahnung, Zahlung, Mahnbescheid, Widerspruch, Titel und Vollstreckungsunterlagen und erzeugt daraus A... |
| `erstpruefung-rollen-mandatsziel` | Rollen- und Mandatszielpruefung nach Aktenlekture: leitet Mandant, Gegner, Vertreter, Ziel und Honorarbasis zuerst aus Vollmacht, Anschreiben, Rechnung, Mahnung und Verfahrensstand ab und fragt nur bei Widerspruch oder Risiko nach. |
| `faellige-zahlen-schwellen` | Zahlentabellen für Faelligkeit Verzug Zinsen Pauschalen Streitwerte und Gebühren in Forderungsverfahren. Liefert aktuelle Basiszinssatz-Werte Verzugszinssaetze Pauschalen B2B Streitwertgrenzen und Gebührentabellen. Pinpoints BGB 247 Basi... |
| `fehlerkatalog` | Katalog typischer Fehler im Forderungsmanagement und Klageweg. Sortiert nach Phase Antrag Mahnbescheid Klage Urteil Vollstreckung. Pinpoints ZPO 690 falscher Antragstyp ZPO 167 verspaetete Vorschusszahlung BGB 286 fehlende Mahnung ZPO 85... |
| `fmkw-mahnverfahren-bauleiter` | Bauleiter automatisiertes Mahnverfahren Paragrafen 688 ff. ZPO: Mahnbescheid, Widerspruch, Vollstreckungsbescheid. Pruefraster fuer Glaeubiger und Inkassodienstleister. |
| `fmkw-saumselig-streitig-erfahrung-spezial` | Spezialfall saeumiges Verfahren und streitiges Verfahren nach Widerspruch: prozessuale Weichen, Beweislast, Schriftsaetze. Pruefraster fuer Klaegeranwalt. |
| `fmkw-titulierung-streckung-leitfaden` | Leitfaden Titulierung mit Ratenzahlung und Streckung: Anerkenntnis, Schuldanerkenntnis, Ratenvereinbarung mit Vollstreckungsmoeglichkeit. Pruefraster fuer Inkassoanwalt. |
| `fmkw-verbraucherklage-cookies-rdg-spezial` | Spezialfall Verbraucherklageinkasso und RDG-Grenzen: Massenforderungen, Sammelklage als Modell, Anti-Claim-Klausel. Pruefraster fuer Legal-Tech und Anwaelte. |
| `forderung-anwaltshonorar-rvg` | Anwaltshonorar nach RVG einklagen: Vergueetungsvereinbarung Paragraf 3a RVG schriftlich, gesetzliche Gebühren Paragrafen 13 ff. RVG, Vorschuss Paragraf 9 RVG. Faelligkeit Paragraf 8 RVG mit Erledigung Auftrag oder Beendigung Mandat. Bere... |
| `forderung-arzthonorar-goae` | Arzthonorar nach GOAE und GOZ einklagen: Faelligkeit Paragraf 12 GOAE mit Rechnungserteilung mit Mindestinhalten Diagnose GOAE-Ziffer und Steigerungsfaktor Regel-Schwellenwert sowie bei Ueberschreitung mit schriftlicher Begruendung. Verj... |
| `forderung-aus-werkvertrag-bgb-bau` | Forderung aus Werk-/Bauvertrag: Faelligkeit Paragraf 641 BGB, Abnahme/Abnahmewirkungen, Schlussrechnungspruefung, Sicherungseinbehalt, Maengelrechte als Einwendung. Output: Pruefraster und Schriftsatz-Module. |
| `forderung-gegen-gesellschafter-13-gmbhg` | Forderung gegen GmbH-Gesellschafter: Paragraf 19 sowie Paragraf 31 GmbHG (Einlagepflicht, Rueckforderung), Paragraf 13 Abs. 2 GmbHG Trennungsprinzip, Durchgriffshaftung bei existenzvernichtendem Eingriff (BGH II ZR 78/06). Pruefraster. |
| `forderung-gegen-gmbh-gesellschafter` | Forderung gegen GmbH-Gesellschafter persoenlich: Paragraf 13 Abs. 2 GmbHG Trennungsprinzip Haftung nur Gesellschaftsvermoegen. Durchgriff bei Paragraf 19 GmbHG (Einlagepflicht) Paragraf 31 GmbHG (verbotene Auszahlung), existenzvernichten... |
| `forderung-gegen-insolventen-schuldner` | Forderung gegen insolventen Schuldner: Anmeldung zur Insolvenztabelle Paragraf 174 InsO binnen Anmeldefrist mit Grund und Hoehe. Aussonderung Paragraf 47 InsO. Absonderungsrecht Paragrafen 49-52 InsO. Massenforderung Paragraf 55 InsO. Na... |
| `forderung-gegen-verbraucher` | Forderung gegen Verbraucher: Verbraucherschutzregeln nach Paragraf 13 BGB, AGB-Kontrolle Paragrafen 305-309 BGB, Widerrufsrecht bei Fernabsatz Paragrafen 312g und 355 BGB, Belehrungspflicht. Verzugszinsen 5 Prozentpunkte ueber Basiszinss... |
| `forderung-im-ausland-vollstrecken` | Forderung im EU-Ausland vollstrecken: Bruessel Ia VO 1215/2012 (Anerkennung ohne Exequatur), Europaeischer Vollstreckungstitel EuVTVO 805/2004, Europaeischer Zahlungsbefehl EuMVVO 1896/2006, geringfuegige Forderung EuGFVO 861/2007. Dritt... |
| `forderung-internationaler-bezug` | Forderungssache mit Auslandsbezug Schuldner im EU-Ausland oder ausserhalb. Klaert anwendbares Recht internationale Zuständigkeit Vollstreckung. Pinpoints VO 1215/2012 Brüssel Ia VO 1896/2006 EuMVVO VO 805/2004 EuVTVO VO 861/2007 EuGFVO R... |
| `forderung-mietruckstand-zahlungsklage` | Mietrueckstand: Zahlungsklage parallel zur Raeumungsklage mit Wohnraum-Sonderzustaendigkeit nach Paragraf 23 Nummer 2a GVG, Schonfrist nach Paragraf 569 Absatz 3 BGB und Gewerberaum-Weiche nach Paragraf 23 Nummer 1 und Paragraf 71 Absatz... |
| `forderung-mietrueckstand-zahlungsklage` | Mietrueckstand und Klageweg: Zahlungsklage parallel zur Raeumungsklage, Wohnraum-Sonderzustaendigkeit nach Paragraf 23 Nummer 2a GVG, kein Anwaltszwang in erster Instanz, Gewerberaum nach Paragraf 23 Nummer 1 und Paragraf 71 Absatz 1 GVG... |
| `forderung-werkvertrag-bau` | Werklohnforderung Paragraf 631, Paragraf 641 BGB: Faelligkeit nach Abnahme, Schlussrechnung. Bauvertrag Paragrafen 650a ff. BGB (seit 2018), VOB/B als AGB. Abschlagszahlungen Paragraf 632a BGB, Sicherheit Paragraf 650f BGB. Mangelhaftigk... |
| `forderung-zwangsvollstreckung-ueberblick` | Zwangsvollstreckung Ueberblick: Mobiliarvollstreckung Gerichtsvollzieher Paragrafen 808 ff. ZPO, Forderungspfaendung Paragraf 829 ZPO, Lohnpfaendung mit Pfaendungstabelle, Immobiliarvollstreckung Zwangshypothek/Versteigerung. Output: Str... |
| `forderungen-interessen-matrix` | Strukturierte Gegenueberstellung mehrerer Forderungen eines Mandanten gegen einen oder mehrere Schuldner. Erfasst Hauptforderung Nebenforderung Zinsen Kosten Faelligkeit Beleg Verjährung. Pinpoints ZPO 260 Klagenhaeufung ZPO 33 Aufrechnu... |
| `forderungsaufnahme` | Forderung systematisch aufnehmen: Gläubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen Paragraf 288 BGB, vorgerichtliche Anwaltskosten Paragraf 280, Paragraf 286 BGB, Mahngebuehren), Faelligkeit Paragraf 271 BGB, V... |
| `forderungsmanagement-aufnahme` | Forderung systematisch aufnehmen: Glaeubiger, Schuldner, Rechtsgrund, Hauptforderung, Nebenforderungen (Zinsen Paragraf 288 BGB, vorgerichtliche Anwaltskosten, Mahngebuehren), Faelligkeit, Verjaehrungsbeginn. Output: vollstaendige Forder... |
| `fristen-risikoampel` | Ampel zur Bewertung saemtlicher Fristen in einer Forderungssache von Verjährung Klagefrist Einspruchsfrist Beschwerdefrist bis Vollstreckungsfristen. Pinpoints BGB 195 199 ZPO 339 Einspruchsfrist Versaeumnisurteil ZPO 700 Einspruch Volls... |
| `gatekeeper-verhandlung-vergleich` | Prüfraster vor Eintritt in Vergleichsverhandlungen. Erhebt Mandantenziel Untergrenzen Sicherheitsbedarf Vollstreckbarkeit. Pinpoints BGB 779 Vergleich ZPO 794 Abs. 1 Nr. 1 Prozessvergleich ZPO 796a anwaltlicher Vergleich. Liefert Verhand... |
| `inkasso-risikoampel` | Bewertung der Erfolgswahrscheinlichkeit einer Forderungseinziehung anhand Schuldnerprofil Belegstand Verjährungslage und Vermögenslage. Pinpoints ZPO 802c Vermögensauskunft ZPO 882b Schuldnerverzeichnis InsO 14 Gläubigerantrag. Liefert A... |
| `inkasso-zahlungsklage-ersteller` | Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement Paragrafen 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten Paragraf 288 BGB... |
| `kaltstart-triage` | Dokumentengetriebene Ersttriage einer Forderungsakte: wertet zuerst Ordner, ZIP, Rechnungen, Mahnungen, Kontoauszuege, Mahnbescheid, Widerspruch oder Klageentwurf aus, bildet eine Aktenhypothese und fragt danach nur echte Luecken ab. Pin... |
| `klage-aus-eigenem-skill` | Kanzlei hat hauseigenes Klage-Plugin installiert und will daraus Klagen erstellen. Pruefraster: Sachverhalt, Beklagtenadresse, Zustaendigkeit nach Paragrafen 12 und 13 sowie 29 und 29c ZPO sowie Paragraf 23 Nummer 1 und 2a GVG und Paragr... |
| `klage-einreichungslogik` | Praktische Einreichungslogik einer Zahlungsklage. Klaert Zuständigkeit Gerichtskostenvorschuss beA-Pflicht Anzahl Abschriften Anlagenbezeichnung und Zustellung. Pinpoints ZPO 130d beA-Pflicht ZPO 253 Klageinhalt ZPO 167 Rueckwirkung Zust... |
| `klagefreigabe-belegte-forderung` | Prüfraster ob eine Forderung klagefaehig ist. Verlangt Belegnachweis Faelligkeit Verzug Verjährung Zustellfaehigkeit und positive Aussicht. Pinpoints ZPO 253 ZPO 138 BGB 286 BGB 195 BGB 199 ZPO 167. Liefert binaere Klagefreigabe-Entschei... |
| `klagevorlage-aus-eigenen-mustern` | Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage Zuständigkeitsprüfung on... |
| `kostenfeststellungsklage-verzugsschaden-erledigung` | Forderungsklage nach Zahlung oder sonstiger Erledigung retten: prüft Kostenfeststellungsklage als materiellen Verzugsschaden statt reflexhafter Erledigung oder Klagerücknahme. Normen: Paragraf 91a ZPO, Paragraf 269 Abs. 3 S. 3 ZPO, Parag... |
| `mahnbescheid-online` | Mahnbescheid (Paragrafen 688-703d ZPO) online beantragen: zentrales Mahngericht je Bundesland, online-mahnbescheid.de, Widerspruchsfrist 2 Wochen Paragraf 692 ZPO, Vollstreckungsbescheid Paragraf 699 ZPO. Vorteile gegenueber Klage: niedr... |
| `mahnbescheid-online-mb` | Mahnbescheid Online-Mahnbescheid (Online-MB): wann sinnvoll, Voraussetzungen Paragraf 690 ZPO, zustaendiges Mahngericht (zentrales Online-Mahngericht), Online-Antrag, Zustellung an Schuldner, Folge Widerspruch fuehrt in streitiges Verfah... |
| `mahnung-aussergerichtlich-stufenmodell` | Aussergerichtliches Mahnverfahren in Stufen: 1. kostenfreie Erinnerung, 2. erste Mahnung verzugsbegruendend Paragraf 286 BGB, 3. zweite/letzte Mahnung mit Fristsetzung. B2B: 30-Tage-Regel Paragraf 286 Abs. 3 BGB. Verbraucher: Belehrungsp... |
| `mahnverfahren-bauleiter` | Spezielles Mahnverfahren bei Werklohnanspruechen aus Bauvertraegen. Beruecksichtigt Faelligkeit nach Abnahme BGB 641 Maengelrechte BGB 634 Bauhandwerkersicherung BGB 650f. Pinpoints ZPO 688 ZPO 690 BGB 641 BGB 650f. Liefert Prüfliste für... |
| `mahnverfahren-beweislast-darlegungslast` | Beweislast und Darlegungslast in Mahnverfahren und Klage: Kläger traegt Darlegungs- und Beweislast für anspruchsbegruendende Tatsachen. Substantiierungspflicht Paragraf 138 ZPO, Wahrheitspflicht, Bestreiten mit Nichtwissen Paragraf 138 A... |
| `mahnvorlauf-dokumentenmatrix` | Dokumentiert den aussergerichtlichen Mahnvorlauf in einer Matrix von Erstmahnung bis letzter Frist. Verknuepft Datum Mahnstufe Empfaenger Zugang Zahlungseingang. Pinpoints BGB 286 Abs. 1 Verzug durch Mahnung Abs. 2 Nr. 1 kalendarische Be... |
| `mandantenkommunikation` | Strukturierte Mandantenkommunikation waehrend einer Forderungssache. Definiert Anlaesse Inhalte und Form für Mandanteninformation Auftragsbestaetigung Sachstand Vergleich Zustimmung und Abschluss. Pinpoints BORA 11 unverzuegliche Informa... |
| `output-waehlen` | Output-Wahl für Forderungsmanagement Klagewerkstatt: stimmt Adressat (Gläubiger, Schuldner, Gerichtsvollzieher), Frist (Mahnbescheid-Widerspruch 2 Wochen) und Form auf den Zweck ab — typische Outputs: Mahnung, Mahnbescheid online (zentra... |
| `quellenkarte` | Kuratierte Quellenkarte für Forderungsmanagement Klagewerkstatt. Sortiert nach Gesetzen Rechtsprechung Verordnungen EU-Recht und Praxis-Literatur. Pinpoints ZPO BGB GVG GKG RVG InsO und EU-Verordnungen Brüssel Ia EuMVVO EuVTVO EuGFVO. Li... |
| `redteam-qualitygate` | Red-Team-Review eines fertigen Schriftsatzes oder Mahnbescheidsantrags. Sucht aus Sicht der Gegenseite nach Angriffsflaechen Schwaechen Beweisluecken und Form-Fehlern. Pinpoints ZPO 138 substantiiertes Bestreiten ZPO 296 Verspaetungsprae... |
| `saumselig-sonderfall-edge-case` | Spezielle Fallkonstellationen die vom Standard abweichen. Schuldner ist unbekannt verstorben verzogen ins Ausland oder unter Betreuung. Pinpoints ZPO 185 öffentliche Zustellung BGB 1922 Erbfolge BGB 1896 Betreuung ZPO 50 Parteifaehigkeit... |
| `spezial-anspruchs-schriftsatz-brief-und-memo-bausteine` | Anspruchs: Schriftsatz-, Brief- und Memo-Bausteine. |
| `spezial-belegte-compliance-dokumentation-und-akte` | Belegte: Compliance-Dokumentation und Aktenvermerk. |
| `spezial-faellige-zahlen-schwellen-und-berechnung` | Faellige: Zahlen, Schwellenwerte und Berechnung. |
| `spezial-fmkw-mandantenkommunikation-entscheidungsvorlage` | Fmkw: Mandantenkommunikation und Entscheidungsvorlage. |
| `spezial-forderungen-mehrparteien-konflikt-und-interessen` | Forderungen: Mehrparteienkonflikt und Interessenmatrix. |
| `spezial-forderungsmanagement-tatbestand-beweis-und-belege` | Forderungsmanagement: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `spezial-freigegeben-red-team-und-qualitaetskontrolle` | Freigegeben: Red-Team und Qualitätskontrolle. |
| `spezial-gatekeeper-verhandlung-vergleich-und-eskalation` | Gatekeeper: Verhandlung, Vergleich und Eskalation. |
| `spezial-inkasso-risikoampel-und-gegenargumente` | Inkasso: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `spezial-klage-formular-portal-und-einreichung` | Klage: Formular, Portal und Einreichungslogik. |
| `spezial-klagefreigabe-belegte-forderung` | Klagefreigabe nur für fällige, belegte und prozessreife Forderungen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-klagewerkstatt-erstpruefung-und-mandatsziel` | Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `spezial-klare-livequellen-und-rechtsprechungscheck` | Klare: Livequellen- und Rechtsprechungscheck. |
| `spezial-mahnverfahren-beweislast-und-darlegungslast` | Mahnverfahren: Beweislast, Darlegungslast und Substantiierung. |
| `spezial-mahnvorlauf-dokumentenmatrix-und-lueckenliste` | Mahnvorlauf: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `spezial-saumselig-sonderfall-und-edge-case` | Saumselig: Sonderfall und Edge-Case-Prüfung. |
| `spezial-werden-internationaler-bezug-und-schnittstellen` | Werden: Internationaler Bezug und Schnittstellen. |
| `spezial-zahlungsklage-behoerden-gericht-und-registerweg` | Zahlungsklage: Behörden-, Gerichts- oder Registerweg. |
| `spezial-zustaendigkeitspruefung-fristen-form-und-zustaendigkeit` | Zustaendigkeitspruefung: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `tatbestand-beweis-belege` | Schluessige Tatbestandsdarstellung in einer Klage oder einem Schriftsatz mit Verknuepfung zu Beweisen und Belegen. Verlangt zeitliche Reihenfolge konkrete Tatsachen mit Beweismitteln Anlagenverweis. Pinpoints ZPO 138 Wahrheitspflicht ZPO... |
| `titulierung-streckung-leitfaden` | Strategie zur Titulierung einer Forderung und Streckung der Vollstreckung durch Ratenzahlungsvereinbarung notarielle Schuldanerkenntnis oder vollstreckbare Urkunde. Pinpoints ZPO 794 Abs. 1 Nr. 1 Vergleich Nr. 5 notarielle Urkunde BGB 78... |
| `urkundenprozess-pruefen` | Urkundenprozess Paragrafen 592-605 ZPO prüfen: Anspruch auf Zahlung auf Urkunden gestuetzt (Vertrag, Schuldschein, Wechsel, Scheck). Beschraenkung Beweismittel Urkunden + Parteivernehmung Paragraf 595 Abs. 2 ZPO. Vorbehaltsurteil Paragra... |
| `verbraucherklage-rdg-grenzen` | Prüfung was Inkassodienstleister und Rechtsanwaelte gegenueber Verbrauchern duerfen und was nicht. Trennt Inkassoerlaubnis von anwaltlicher Vertretung. Pinpoints RDG 2 RDG 10 RDG 11a Hinweispflicht BGB 312j AGB-Kontrolle 305 ff. Liefert... |
| `verjaehrung-pruefen` | Verjährung prüfen: Regelverjaehrung Paragraf 195 BGB drei Jahre, Beginn Paragraf 199 BGB Schluss des Jahres mit Kenntnis. Hoechstfristen Paragraf 199 Abs. 2-4 BGB (10/30 Jahre). Hemmung Paragraf 203 BGB (Verhandlungen), Paragraf 204 BGB... |
| `vollstreckungsbescheid-folgen` | Vollstreckungsbescheid Paragrafen 699 und 700 ZPO: Voraussetzung kein Widerspruch innerhalb 2 Wochen Paragraf 692 Abs. 1 Nr. 3 ZPO, Antrag binnen 6 Monaten Paragraf 701 ZPO. Vollstreckungstitel Paragraf 794 Abs. 1 Nr. 4 ZPO. Verjährung 3... |
| `vollstreckungsbescheid-und-folgen` | Vollstreckungsbescheid Paragrafen 699 und 700 ZPO: Voraussetzung kein Widerspruch innerhalb 2 Wochen, Vollstreckungstitel fuer 30 Jahre, Einspruch noch moeglich (gleicher Fristrahmen wie Widerspruch nach Zustellung). Strategische Hinweise. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-orchestrierung` | Steuert den Gesamtablauf einer Forderungsakte vom Eingang bis zur Vollstreckung oder Abschreibung. Definiert Workflow-Stufen Eingang Prüfung Mahnung Mahnbescheid Klage Titel Vollstreckung Erloesverwertung. Pinpoints ZPO 91 Kostenfolge ZP... |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zahlungsklage-behoerden-register` | Hilfe bei Klagen gegen Behörden und juristische Personen des öffentlichen Rechts. Klaert Verwaltungsweg oder Zivilweg Klägervertreter Vorverfahren Verfahrensart. Pinpoints VwGO 40 abgrenzbare oeffentlich-rechtliche Streitigkeit ZPO 253 f... |
| `zahlungsklage-erstellen` | Zahlungsklage erstellen nach Paragrafen 253 ff. ZPO: Rubrum, Klageantrag, Streitwertangabe, Tatbestand, Beweismittel, Anlagenverzeichnis, Zuständigkeit nach Paragraf 23 Nummer 1 und Nummer 2a GVG sowie Anwaltszwang nach Paragraf 78 Absat... |
| `zinsberechnung-288-bgb` | Zinsberechnung nach Paragraf 288 BGB: Verbraucherverzug 5 Prozentpunkte ueber Basiszinssatz, B2B-Verzug 9 Prozentpunkte. Verzugspauschale 40 EUR Paragraf 288 Abs. 5 BGB B2B. Basiszinssatz Paragraf 247 BGB halbjaehrlich anpasst durch Deut... |
| `zustaendigkeitspruefung-mahngericht` | Sachliche Zustaendigkeit nach Paragraf 23 Nummer 1 GVG und Paragraf 71 Absatz 1 GVG, Wohnraum-Sonderzustaendigkeit nach Paragraf 23 Nummer 2a GVG, oertliche Gerichtsstaende nach ZPO, internationale Zustaendigkeit und Mahngericht nach Par... |
| `zwangsvollstreckung-ueberblick` | Zwangsvollstreckung Überblick: Mobiliarvollstreckung Gerichtsvollzieher Paragrafen 808 ff. ZPO, Forderungspfaendung Paragrafen 828 ff. ZPO (Konto, Lohn), Immobiliarvollstreckung Paragrafen 866 ff. ZPO und ZVG, Vermögensauskunft Paragraf... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
