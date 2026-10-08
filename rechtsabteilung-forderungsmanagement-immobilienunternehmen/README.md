# Rechtsabteilung Forderungsmanagement Immobilienunternehmen

Für Fachangestellte und Fachkräfte der internen Immobilien-Rechtsabteilung: vom SAP-/DMS-Ordner bis zum begründeten Entwurf, zur Kostenakte und zur Vollstreckung. **50 Fachskills**, beide autarken Prompts und der gesamte Quellstand aus Version 5.27.1 sind erhalten. Der Name ist unternehmensneutral; Vermieterin, Vertretung und Befugnisse werden für jeden Fall aus den Unterlagen ermittelt.

## In einer Minute beginnen

1. [Fachplugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/rechtsabteilung-immobilien-v445.33.1/rechtsabteilung-forderungsmanagement-immobilienunternehmen.zip) und im vorgesehenen Plugin-Import installieren.
2. Fallordner oder bisherigen Arbeitsstand samt neuer Post bereitstellen.
3. Auftrag: `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.`

Keine Skillnummer nötig. Bereits beantwortete Fragen werden übernommen. Bei einer konkreten Aufgabe entsteht direkt Restrechnung, Mieterantwort, Beleganforderung oder Prozessentwurf. Eine ungeklärte Außenmaßnahme sperrt nicht die übrige Aktenarbeit. Dateien und Register werden nur dann als erzeugt bezeichnet, wenn die Umgebung sie tatsächlich erstellen kann.

## Einstieg und Downloads

| Gewünschtes Ergebnis | Richtiger Einstieg |
|---|---|
| Juristischen Fall bearbeiten | [Plugin mit 50 Skills](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/rechtsabteilung-immobilien-v445.33.1/rechtsabteilung-forderungsmanagement-immobilienunternehmen.zip) |
| Vollworkflow ohne Plugin nutzen | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/rechtsabteilung-forderungsmanagement-immobilienunternehmen-werkstatt.md) |
| Kompakte Einzelprompt-Variante | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/rechtsabteilung-forderungsmanagement-immobilienunternehmen-schnellstart.md) |
| Fertige Schriftsätze nur technisch vorbereiten | [Getrennte beA-Werkstatt](../schriftsatzwerkstatt-bea/README.md) |
| Vollkopie, Herkunft und Akten auswählen | [Projektübersicht](../projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md) |
| Einzelnen Fachschritt nachschlagen | [50 Skills](#alle-skills-im-überblick) |
| Installation im großen Repository | [Installationshilfe](../INSTALLATION_EINFACH.md) |

Für denselben Fall **Plugin oder Werkstatt oder Schnellstart** wählen. Die Prompts werden nicht als zusätzliche Skills geladen. Die technische beA-Werkstatt beginnt erst nach der fachlichen Bearbeitung; andere Versandplugins nicht gleichzeitig für dasselbe Paket verwenden. Die vorhandene allgemeine Forderungsmanagement-Klagewerkstatt bleibt unverändert und ist kein obligatorischer Zwischenschritt.

## Rollout und Grenzen

Zunächst mit fiktiven Akten testen, fachliche Verantwortliche benennen und Ausgabe, Fristen sowie Quellen gegenlesen. Technische Paketprüfungen sind keine juristische Freigabe und kein Nachweis gleichbleibender Modellqualität. Unternehmensdaten nur in dafür freigegebenen Umgebungen verwenden. Quellen behalten ihren dokumentierten Prüfstand; die Übernahme am 07.10.2026 ist keine pauschale Rechtsstandsaktualisierung.

Die interne Bearbeitungsgrenze von 10.000 EUR ersetzt weder Zuständigkeits- noch Vertretungsprüfung. Eigene Gesellschaft, Konzernverbund, Beschäftigtenstatus, Vollmacht und Freigabe werden getrennt behandelt. Die [Arbeitsregeln](./AGENTS.md) und [Bedienführung](./references/bedienfuehrung-workflows.md) führen zum passenden Fachpfad.

## Welche Unterlagen die Bearbeitung braucht

Ein guter Upload-Satz besteht aus:

- SAP-Statusauszug mit Objekt, Mieter, Vermieterin, Vertragsnummer, Saldo und Bearbeitungsstand.
- FBL5N- oder vergleichbarer Mietkontoauszug mit Sollstellung, Ist-Zahlung, Buchungstexten und Saldo.
- DocuWeb-, DATEV-, RA-MICRO-, DocuWare- oder sonstiger E-Akte-/DMS-Export mit Dokumenten, Registern und Metadaten.
- Mietvertrag, Nachträge, Mieterhöhungsverlangen, Betriebskostenunterlagen und sonstige Vertragsdokumente.
- Korrespondenz: Mahnung, Zahlungsvereinbarung, Kündigung, Schreiben des Mieters, Mieterverein, Rechtsanwalt, Jobcenter, Sozialamt.
- Gerichtsunterlagen: Klage, Klageerwiderung, Verfügungen, Hinweise, Vergleich, Urteil, Kostenfestsetzungsbeschluss, Vollstreckungsunterlagen.

Unvollständige Unterlagen sind kein Abbruchgrund. Die Intake-Skills erzeugen dann eine Beleglückenliste und stellen Rückfragen an die Hausverwaltung, Buchhaltung oder Prozesskoordination.

## E-Akte- und DMS-Anschluss

Für DocuWeb/DocuWare-artige DMS, DATEV-Dokumentenablage, RA-MICRO E-Akte, SAP DMS, Datenbankexporte, XML-Importe, Middleware und MCP-/Kontext-Gateways gilt derselbe Anschlussmodus:

1. Skills 01 und 33 sichern Herkunftssystem, Fremd-Aktenzeichen, Dokument-ID, Register, Exportdatum, Dateipfad und Fristbezug.
2. Skill 34 erzeugt neutrale Übergabeformate: `fallakte.json`, `dms-register.csv`, bei Legacy-Bedarf `fallakte.xml`, bei MCP-Planung `mcp-context-manifest.json` und bei offenen Fragen `schnittstellenauftrag.md`.
3. Originaldateien bleiben unverändert; PDF/A oder OCR-PDF wird nur als Arbeitskopie ausgewiesen.
4. Importfähigkeit wird erst grün markiert, wenn Feldmapping, Rechte, Pflichtfelder, Importweg, Testsystem, Dublettenlogik und Rückexport bekannt sind.
5. Schreibende Aktionen in Zielsystemen bleiben gesperrt, bis Freigabe, Protokollierung und Rollback geklärt sind.

## Workflow-Phasen

| Phase | Skills | Inhalt |
|---|---|---|
| A | 01-05 | SAP-Akten-Intake (Statusauszug, Mietvertrag, Mietkonto, Belegmatrix, Chronologie) |
| B | 06-08 | Triage und Rollen-Check (RDG, Eskalation, externe RA-Steuerung) |
| C | 09-12 | Außergerichtliche Forderungssteuerung |
| D | 13-16 | Kündigung (fristlos, ordentlich, Zustellung, Widerspruch) |
| E | 17-19 | Optionales gerichtliches Mahnverfahren nur nach Rückfrage |
| F | 20-23 und 39 | Zahlungsklage, Beweis-/Anlagenmanifest und gerichtsfertiges Einreichungspaket |
| G | 24-27 | Räumungsklage |
| H | 28-31 | Mieterhöhung |
| I | 32 | Datenschutz |
| J | 33-36 | Dokumentenmix, SAP-Normalisierung, Beleglücken, Fallstrategie bis 10.000 EUR |
| K | 37-45 | Klageerwiderung, Replik, Beweisplan, Urkundsprozess, Vergleich, Mieterklage, Betriebskosten, Hausverwaltung |
| L | 46-50 | Kostenfestsetzung, Kostenbeschluss, Vollstreckung, Kontoermittlung, Monitoring |

## Schnellstart

Autostart-Regel: Die Bearbeiter sollen keinen Skill auswählen müssen. Der universelle Auftrag lautet: `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.` Auch kürzere Formulierungen wie "neuer Fall", "hier ist der Ordner", "mach die Akte fertig" oder "prüf das Projekt" und mehrere hochgeladene Dateien starten `33-dokumentenmix-ocr-sichten`. Dieser Skill liefert zuerst die einheitliche fristzentrierte Sofortkarte und arbeitet danach automatisch bis zur Start- oder Änderungskarte weiter. Dem Nutzer wird genau eine nächste Arbeitsaktion in Klartext gezeigt; die Skill-ID bleibt interne Routinginformation.

Discovery-Regel: Bei einem neuen Akten-Upload sind nur drei Startpunkte favorisiert. `33-dokumentenmix-ocr-sichten` ist der Default für gemischte oder unklare Dateien und Projektordner. `01-sap-akte-importieren` wird nur bei sauberem SAP-/Mietkonto-Input geladen. `06-fallziel-renofa-triage` folgt nach abgeschlossenem Intake oder wenn der Nutzer schon eine klare Fallkarte liefert. Fachskills `09` bis `50` werden erst nach Startkarte und Routing geladen.

Vertrag für die erste Antwort: Vor jeder langen Analyse erscheint genau eine Sofortkarte mit `Modus`, `Akten-ID/Stichtag`, `Fallart`, `Frist/Quelle`, `Ampel/Grund`, `Dateistand`, `Kernlücken` und `Jetzt`. `Jetzt` enthält genau eine verständliche Arbeitsaktion. Nicht blockierende Unsicherheiten werden als gelbe Lücke notiert; nur Fragen, deren Antwort die sofortige Frist-, Rollen- oder Maßnahmenentscheidung ändert, werden gebündelt gestellt. Danach läuft die Bearbeitung ohne den Befehl "weiter" fort.

### Direkt nutzbare Startaufträge

Diese Sätze sind für Schulung und Tagesgeschäft gedacht. Sie lösen den richtigen Startskill aus, ohne dass Bearbeiter eine Skill-Liste kennen müssen.

| Situation | Nutzersatz | Erwarteter Start |
|---|---|---|
| Neuer Aktenordner oder Upload-Bundle | `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.` | sofort einheitliche Sofortkarte, danach automatisch Dokumenteninventar, Startkarte und Fachpfad |
| SAP-Statusauszug plus Mietkonto | `Bitte lies den SAP-Auszug und das Mietkonto ein und prüfe den Rückstand.` | `01-sap-akte-importieren`, danach Konto, Belegmatrix und Triage |
| Neue Zahlung oder Unterlage zur laufenden Akte | `Hier ist der bisherige Stand mit einer neuen Zahlung und neuer Post. Bitte nur fortschreiben.` | Änderungskarte über `33`, bei sauberem SAP-/Mietkonto-Delta über `01` oder `03`; danach ereignisbezogener Fachskill |
| Schon sortierte Fallkarte | `Hier ist die Fallkarte. Bitte entscheide den nächsten Forderungsmanagement-Schritt.` | `06-fallziel-renofa-triage` |
| Gerichtspost oder Klageerwiderung | `Bitte werte die neue Gerichtspost aus und zeige Frist, Einwendungen, Beweise und nächsten Schriftsatz.` | Fristen- und Dokumentencheck, danach Prozesskarte und Reaktionsentwurf |
| Fertiger Schriftsatz mit Anlagen | `Bitte finalisiere den Schriftsatz als gerichtsfertiges Einreichungspaket.` | Beweis-/Anlagenmanifest, danach Rollengate und technischer Einreichungspfad |
| Nach Urteil, Vergleich oder KFB | `Bitte prüfe Kosten, Fristen, Zahlung und den nächsten Vollstreckungsschritt.` | `46-kostenfestsetzung-antrag`, `47-kostenbeschluss-pruefen` oder `48-titulierte-forderung-vollstrecken` |

### Schneller Zwei-Phasen-Start

Bei großen Uploads nicht warten, bis jedes Dokument vollständig ausgewertet ist. Erst kommt die Sofortkarte, dann die tiefe Aktenarbeit.

1. Phase 1: gesamten sichtbaren Bestand auf Gerichtspost, Zustellung, Frist, Zahlung, Kündigung und defekte Dateien scannen; dann eine kurze Sofortkarte liefern.
2. Phase 2: ohne erneute Aufforderung zuerst Gerichts- und Zustelldokumente, dann Zahlung/Konto, Kündigung/Vertrag und übrige Belege vertiefen.
3. Je Stapel höchstens 20 Dateien oder 30 PDF-Seiten vertiefen; bei einem neuen roten Risiko sofort stoppen.
4. Nach jedem Stapel eine Fortsetzungsmarke mit Akten-ID, Stichtag, verarbeitet/offen, letzter Quelle/Seite, frühester Frist und nächstem Stapel sichern. Nach Unterbrechung dort fortsetzen und unveränderte Unterlagen nicht erneut ausgeben.
5. Wenn OCR oder Scanqualität bremst: Lesbarkeitsproblem markieren, aber die übrigen lesbaren Unterlagen weiter auswerten.
6. Sichtbare Tabellen auf höchstens sieben Spalten begrenzen; technische Metadaten getrennt ausgeben.
7. Niemals zuerst fragen, welchen Skill die Bearbeiter nutzen wollen. Das Plugin wählt den Startpfad und begründet ihn kurz.

### Laufende Akte ohne Neustart

Wenn Akten-ID, Startkarte, Chronologie oder Prozesskarte vorliegen, verarbeitet das Plugin neue Zahlung, Gerichtspost, Korrespondenz, KFB oder DMS-Datei als Delta. Es hält den letzten Stichtag fest, vergleicht Alt und Neu für Saldo, Frist, Beweisstatus und Prozesslage, markiert überholte Entwürfe und schreibt nur die betroffenen Tabellen fort. Fehlt ein belastbarer Altstand, fällt der Vorgang kontrolliert auf den Vollintake zurück.

Die erste Ausgabe ist eine kompakte Sofortkarte. Danach folgt die Änderungskarte mit Stichtag alt/neu, Neuzugang, geänderten Tatsachen und Beträgen, unverändertem Kernstand, überholter Annahme, Sofortfrist und genau einer nächsten Arbeitsaktion in Klartext. Dadurch bleibt die Akte schnell, prüfbar und ohne stillen Zustandsverlust bearbeitbar.

### Vollintake in acht Schritten

1. Projektordner oder Upload-Bundle mit `33-dokumentenmix-ocr-sichten` inventarisieren.
2. Saubere SAP-/Mietkonto-Teile per `01-sap-akte-importieren` strukturieren.
3. Mietakte mit `02-mietakte-rekonstruieren` zusammenfügen.
4. Konto auslesen `03-kontoauszug-mietkonto-auslesen`.
5. Belegmatrix `04-belegmatrix-aufbauen`.
6. Chronologie `05-chronologie-fallakte`.
7. Triage `06-fallziel-renofa-triage` — Fallziel, Rollenbefugnis und RA-Eskalation.
8. Bei eigener Bearbeitung: passenden Pfad C bis L wählen.

Jeder Schritt soll ein bedienbares Ergebnis liefern: Sofortkarte, Ampel, Tabelle, Lückenliste, Kontrollpunkte vor Versand und klare Eskalation, wenn anwaltliche Freigabe nötig ist. Die Referenz `references/bedienfuehrung-workflows.md` gibt dafür Rückfragegrenzen, automatische Pfadwahl, Klartext-Aktionen und Übergabestandards vor.

## Bedienmuster im Tagesgeschäft

### Mietrückstand und Zahlungsklage

1. Skills 01 bis 05 für Stammdaten, Mietkonto, Belege und Chronologie.
2. Skill 06 für Fallziel und interne Freigabegrenze.
3. Skill 20 für Zahlungsklage, Skill 21 für Streitwert/Gerichtskosten und Skill 22 für Amtsgericht.
4. Skill 39 schließt Beweise und fortlaufende K-/B-Nummern; Skill 23 baut Einzel-PDFs, Anlagenverzeichnis, Manifest, ERV-/Signaturcheck und Eingangsnachlauf.
5. Ergebnis prüfen: Forderungsposten, Zeitraum, Zahlungseingänge, Anlagen, Zinsen, Zustellung.

Rechtzeitigkeitsregel: Bei Wohnraummiete zählt Sonnabend für die Zahlungsfrist des Paragrafen 556b BGB nicht. Bei gedecktem Konto genügt der bis zum dritten Werktag erteilte Überweisungsauftrag; ein späterer SAP-Kontoeingang beweist allein keine Verspätung. Kontrollanker sind BGH VIII ZR 129/09, VIII ZR 291/09 und VIII ZR 222/15.

### Räumung wegen Zahlungsverzug

1. Skills 13 bis 16 für Kündigung, Zustellung und Widerspruch.
2. Skill 24 für Räumungsklage, Skill 25 für Räumungsfrist und Vollstreckung, Skill 26 für Berliner Modell, Skill 27 für Schonfristzahlung.
3. Ergebnis prüfen: Kündigungszugang, Rückstandshöhe, Schonfristzahlung, Erledigungserklärung, Kostenfolge.

### Mieterhöhung

1. Skill 28 für Vorbereitung nach Paragraf 558 BGB.
2. Skill 29 für Mieterhöhungsverlangen.
3. Skill 30 für Zustimmungsklage.
4. Skill 31 für Kappungsgrenze, Mietpreisbremse und Berliner Besonderheiten.
5. Ergebnis prüfen: Ausgangsmiete, Vergleichsmiete, Sperrfrist, Kappungsgrenze, Begründung durch Mietspiegel.

### Prozessreaktion und Verteidigung

1. Skill 37 wertet gerichtliche Klageerwiderungen, gerichtliche Hinweise und gegnerische Schriftsätze in der eigenen Klage aus. Außergerichtliche Schreiben von Mieterverein oder gegnerischem Anwalt führt Skill 43; Mieterklage oder Widerklage führt Skill 42.
2. Skill 38 erstellt die Replik.
3. Skill 39 ordnet Beweise und Anlagen.
4. Skills 40 bis 45 decken Urkundsprozess, Vergleich, Mieterklage, Mieterverein, Betriebskosten und Hausverwaltung ab.
5. Ergebnis prüfen: Bestreiten, Beweislast, Fristen, Beleglücken, Vergleichsrisiko.

### Gerichtsfertiges Dokumentenpaket

Wenn die Rechtsarbeit noch Teil des Auftrags ist, bleibt dieser Fachpfad maßgeblich. Sind Inhalt, Anträge, Vortrag, Beweisentscheidung und Fristen dagegen bereits vollständig freigegeben, kann unmittelbar die [eigenständige beA-Schriftsatzwerkstatt](../schriftsatzwerkstatt-bea/README.md) verwendet werden; sie nimmt keine fachlichen Änderungen vor.

1. Ein finaler Auftrag beginnt mit `Bitte finalisiere den Schriftsatz mit allen Anlagen als gerichtsfertiges Einreichungspaket.`
2. Skill 39 ordnet jede erhebliche Tatsache einem Beweis zu, sperrt bereits eingereichte K-/B-Nummern und erzeugt ein Manifest mit Originalquelle, Version, Hash, Seiten und Beschaffungsstatus.
3. Skill 23 fragt Gericht/Aktenzeichen, Frist, Erscheinungsbild und vor allem die Einreichungsrolle ab: Eigenvertretung der privaten Konzerngesellschaft oder beauftragte Kanzlei.
4. Hauptschriftsatz und jede Anlage entstehen als eigene PDF-Arbeitskopie. Auf der ersten Anlagenseite steht rechts oben `Anlage K 1` oder `Anlage B 1`, ohne Originalinhalt zu verdecken; Originale bleiben unverändert.
5. Dateinamen bleiben unter 80 Zeichen, nutzen ASCII und Unterstriche, etwa `02_Anlage_K01_Mietvertrag_2022-05-01.pdf`.
6. Kanzleiweg: beA und Paragraf 130d ZPO; bei einfacher Signatur muss dieselbe verantwortende anwaltliche Person selbst versenden. Eigenvertretung: Beschäftigtenstatus/Vollmacht nach Paragraf 79 ZPO und ein tatsächlich eingerichtetes eBO nach Paragraf 130a Abs. 4 S. 1 Nr. 3 ZPO/Paragraf 10 ERVV oder ein im konkreten Verfahren zulässiger schriftlicher Weg. Eine private GmbH unterliegt Paragraf 130d nicht allein wegen ihrer Rechtsform.
7. Das Paket enthält Anlagenverzeichnis, Hashmanifest, PDF-/Form-/Signaturcheck, getrennte Freigabekarte und Versandauftrag. Das Plugin sendet nicht selbst. Nach Versand werden automatisierte Eingangsbestätigung oder sonstiger Zugangsnachweis, tatsächlich gesendete Dateiliste, Prüfprotokoll, Zustellung und Wiedervorlage gesichert. Maßgeblich ist [ERV-, eBO- und beA-Dokumentenproduktion](references/erv-dokumentenproduktion.md).

### Kostenpfad nach Klageeinreichung

1. Bei Zahlung, Aufrechnung, dauernder Einrede, Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses nach Klageeinreichung nicht automatisch erledigen oder zurücknehmen.
2. Skill 05 trennt Klageeinreichung, Zustellung und Rechtshängigkeit. Skill 11 prüft Verzugsschaden. Skill 37 erstellt die Kostenpfad-Matrix. Skill 38 formuliert die passende Antragsumstellung.
3. Die Matrix enthält mindestens Ereignis, Datum, vor/nach Rechtshängigkeit, vollständig/teilweise, Vorverzug, Forderungs- und Kenntnisstand bei Einreichung, Kausalität und Erforderlichkeit der Kosten, Paragraf 91a ZPO, Paragraf 269 Abs. 3 S. 3 ZPO, materiell-rechtliche Kostenerstattung und RA-Eskalation.
4. Materiell-rechtliche Kostenerstattung als Verzugsschaden nur bei Vorverzug und kausalen, aus damaliger Sicht erforderlichen Klagekosten prüfen. Grün ist der bei Einreichung noch offene Anspruch. Eine unmittelbar zuvor eingegangene, objektiv noch nicht erkennbare Zahlung bleibt gelb und geht mit Zahlungsweg, Buchungszeitpunkt und Kenntnisstand zur RA-Prüfung.
5. Ampel setzen: grün bei belegtem Vorverzug, offener Forderung bei Einreichung und klarer Kausalität, gelb bei Beleg-, Erkennbarkeits- oder Zeitachsenlücke, rot bei fehlendem Vorverzug oder vermeidbaren Kosten.
6. Bei unsicherem Kostenweg, streitiger Kausalität oder drohendem Kostenverlust Skill 08 einschalten, bevor eine Erklärung an das Gericht abgegeben wird.

### Kosten und Vollstreckung

1. Skill 46 für Kostenfestsetzungsantrag.
2. Skill 47 für Prüfung des Kostenfestsetzungsbeschlusses.
3. Skill 48 für Vollstreckung aus Urteil, Vergleich, Vollstreckungsbescheid oder Kostenfestsetzungsbeschluss.
4. Skill 49 für Konto- und Drittauskünfte nach Titel.
5. Skill 50 für Monitoring von Zahlungen, Raten, Verjährung und nächsten Maßnahmen.
6. Bei abweisendem oder teilweise abweisendem Amtsgerichtsurteil keine Vollstreckung starten, sondern Tenor, Frist, Beschwer, Wert, Zulassung und Kostenrisiko als Rechtsmittel-Skizze an Skill 08 und die Stammkanzlei übergeben.
7. Bei externer eigener Kanzlei Auftrag, Budget, Honorargrundlage, Reporting, Rechnung und Stunden-Narrative mit Skill 08 prüfen und monieren.
8. KFA, gegnerischen KFA, KFB, Streitwertfestsetzung, Kostenrechnung, Berichtigung und Beschwerde immer als Fristen- und Entscheidungsvorlage führen.

## Erwartete Outputs

Das Plugin soll nicht nur Text entwerfen, sondern die Akte beherrschbar machen. Typische Zwischenergebnisse sind:

- Stammdatenblatt mit Objekt, Mietpartei, Vermieterin, Vertrag und Bearbeitungsrolle.
- Forderungsaufstellung mit Soll, Ist, Saldo, Zeitraum und Beleganker.
- Chronologie mit Datum, Ereignis, Quelle, Frist und nächstem Schritt.
- Beleg- und Anlagenmatrix für Schriftsätze.
- Entscheidungsvermerk zu Eskalation, Mahnverfahren-Abzweigung, Klagepfad oder Vergleich.
- Kostenpfad-Matrix nach Klageeinreichung mit Rechtshängigkeit, Verzug, Kostenweg und Eskalation.
- Vollständig ausformulierter Entwurf für Schreiben, Klage, Replik, Antrag oder Vollstreckungsauftrag.
- Gerichtsfertiges Paket aus Hauptschriftsatz, einzelnen K-/B-Anlagen-PDFs, Anlagenverzeichnis, Hashmanifest, ERV-/Signaturcheck, Freigabekarte, Versandauftrag und Eingangsnachlauf.
- Rechtsmittel- und Eskalationsspur bei abweisendem oder teilweise abweisendem Urteil, getrennt von Vollstreckung.
- Kanzlei-Auftrag, Rechnungsvotum und Monierungstabelle für externe eigene Anwälte.
- Kostenrechtsvermerk zu KFA, KFB, Streitwert, Berichtigung, Beschwerde und Frist.
- Kontrollliste für fachliche Freigabe vor Versand.
- Getrennte Freigabekarte mit Status, Aktenstichtag, Adressat, Rechtsfolge, Betragskontrolle, Beweisen/Anlagen, Frist/Weg, Rollencheck und realer Freigabeperson.
- Sofort- und Startkarte mit Fallart, Ampel, kurzer Begründung, Frist, fehlenden Kernstücken und genau einer nächsten Arbeitsaktion.

## Kontrollpunkte vor Versand

Jeder außenwirksame Entwurf beginnt im Arbeitspaket mit einer internen Freigabekarte; sie ist nicht Teil des Mieter- oder Gerichtsdokuments. Standardstatus ist `ENTWURF - NICHT VERSENDEN/EINREICHEN`. Grün bedeutet nur freigabefähig. Erst eine benannte reale Person setzt `FREIGEGEBEN`; das Plugin erteilt keine eigene Freigabe.

- Stimmen Namen, Anschriften, Objekt, Vertragsnummer und Gericht?
- Sind Forderungszeiträume, Zahlungen, Teilzahlungen und Verrechnung nachvollziehbar?
- Gibt es Belege für jede erhebliche Tatsachenbehauptung?
- Sind Kündigung, Zugang, Fristen und Schonfristzahlung sauber dokumentiert?
- Ist die interne 10.000-EUR-Grenze eingehalten oder freigegeben?
- Muss wegen Landgericht, Berufung, Insolvenz, Strafrecht oder Sachverständigenfrage eskaliert werden?
- Sind Datenschutz, Datenminimierung und interne Freigabe dokumentiert?
- Stimmen Datenstichtag und letzte berücksichtigte Zahlung mit Forderung und Antrag überein?
- Wurde eine frühere Freigabe nach Änderung von Betrag, Antrag, Partei, Frist, Beweis, Anlage oder Zustellweg aufgehoben und neu geprüft?

## Abnahme im Pilotbetrieb

Vor Produktivfreigabe sollte die Pilotgruppe mindestens eine Testakte je Hauptpfad bearbeiten:

1. Mietrückstand bis Zahlungsklage.
2. Räumung bis Reaktion auf Schonfristzahlung.
3. Zahlung nach Klageeinreichung bis Kostenpfad-Entscheidung.
4. Mieterhöhung bis Zustimmungsklage.
5. Klageerwiderung bis Replikplan.
6. Kostenfestsetzung bis Vollstreckungsmonitoring.

Die fachliche Leitung prüft dabei nicht nur den Textentwurf, sondern auch Chronologie, Belegmatrix, Fristen, Eskalationsentscheidung und Kontrollliste vor Versand. Die [Smoke-Tests](./references/smoke-tests.md) liefern dafür eine kompakte Abnahmeliste.

## Testakten

Die [zehn Fälle mit jeweils drei Downloadformen](../projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/TESTAKTEN.md) gehören vollständig zum Projekt. Beginne mit Lange (Bankwechsel, Kulanz und Belegdublette), danach Braun (Betriebskosten und Beleglücken). Lade je Fall nur eine Darreichungsform, damit dasselbe Aktenstück nicht mehrfach im Eingang landet.

## Quellen und Konsistenz

Dieses Repo übernimmt die Qualitätsstandards aus [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht):

| Mitgelieferte Referenz | Einsatz im Workflow |
|---|---|
| [Bedienführung und Workflows](references/bedienfuehrung-workflows.md) | Sofortkarte, automatische Pfadwahl, Fortsetzungsmarke, Rückfragen, Übergabe und Freigabekarte |
| [100-Punkte-Bediencheck](references/100-punkte-bediencheck.md) | Abnahme für Einstieg, Fristen, Stapel, Lesbarkeit, Quellen, DMS, Prompts, Testakten und Downloads |
| [Schnittstellenprofile](references/schnittstellenprofile.md) | SAP-, DMS-, DATEV-, RA-MICRO-, XML- und MCP-Anschluss |
| [Geprüfte BGH-Anker Mietrecht](references/gepruefte-bgh-anker-mietrecht.md) | verifizierte Primärquellen und Kontrollbefunde |
| [Rechtsprechungsradar 2021 bis 2026](references/rechtsprechungsradar-mietrecht-2021-2026.md) | BGH-/BVerfG-/EuGH-, KG-, OLG- und LG-Suchspur mit Quellenstatus |
| [Rechtsstand 2026: Verfahren, Vollstreckung und Mietrechtsnovelle](references/rechtsstand-2026-verfahren-vollstreckung.md) | Online-Verfahren, Pfändungsfreigrenzen, elektronische Zwangsvollstreckung und Entwurfs-Gate für BT-Drs. 21/6807 |
| [Schriftsatz- und Argumentationsstandard](references/schriftsatz-und-argumentationsstandard.md) | Tatsachenkarte, Substantiierung, Bestreiten, Beweisangebot, Subsumtion und Endkontrolle |
| [ERV-, eBO- und beA-Dokumentenproduktion](references/erv-dokumentenproduktion.md) | PDF-Paket, Anlagenkennzeichnung, Dateinamen, Rollengate, Signatur und Eingang |
| [Leitentscheidungen-Anker](references/leitentscheidungen-anker.md) | Sucheinstieg nach Falltyp und Norm |
| [Methodik Bürgerliches Recht](references/methodik-buergerliches-recht.md) | Anspruchsaufbau, Beweislast und Rechtsfolge |
| [Quellenhygiene](references/quellenhygiene.md) | Quellenstatus und Live-Verifikation |
| [Zitierweise](references/zitierweise.md) | einheitliche Fundstellen in Vermerk und Schriftsatz |

- Keine BeckRS- oder Aufsatz-Blindzitate
- Rechtsprechung nur verifiziert
- Quellenhygiene wie im Mutter-Repo
- Quellenleitplanken im Plugin-ZIP unter `references/`
- Geprüfte mietrechtliche Kontrollspur mit BGH-Feed-Abgleich vom 09.08.2026 zu Härtefall, Vormiete, Auskunft und Mietpreisbremsen-Streitwert
- Datierte 2026-Kontrollspur für Online-Klagen, Pfändungsfreigrenzen und die erst ab 01.10.2026 anwendbare Vollstreckungsreform
- Harte Sperre gegen die vorzeitige Anwendung der am 09.07.2026 nur an die Ausschüsse überwiesenen Mietrechtsnovelle BT-Drs. 21/6807
- Angepasste Build- und Validierungsskripte für Plugin, Prompts, Testakten und Release-Assets
- Markdown-Skills mit YAML-Frontmatter `name` und `description`

## Lizenz

Apache-2.0 oder MIT (siehe [LICENSE-APACHE](./LICENSE-APACHE) und [LICENSE-MIT](./LICENSE-MIT) im Plugin).


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 50 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`01-sap-akte-importieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/01-sap-akte-importieren/SKILL.md) | SAP-Start bei sauberem SAP-Statusauszug, FBL5N, Mietkonto, Vertragsnummer, Saldo oder neuem SAP-Stand zu laufender Akte. Stammdaten, Delta, Herkunftssystem und Rückexportbedarf erfassen. Bei neuem Ordner oder gemischtem Upload zuerst Ski... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/01-sap-akte-importieren/SKILL.md) |
| [`02-mietakte-rekonstruieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/02-mietakte-rekonstruieren/SKILL.md) | Mietvertrag mit Nachträgen rekonstruieren. Wohnraum und Gewerberaum, Form, Indexklausel, Staffelmiete, Schönheitsreparaturen und Betriebskostenkatalog prüfen. Fehlende Anlagen aus SAP DMS erkennen. Output Anlagenverzeichnis für spätere K... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/02-mietakte-rekonstruieren/SKILL.md) |
| [`03-kontoauszug-mietkonto-auslesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/03-kontoauszug-mietkonto-auslesen/SKILL.md) | Mietkonto, OP-Liste, Buchungsjournal oder neuen Zahlungseingang auslesen und fortschreiben. Saldo, Teilzahlung, Storno, Guthaben, Tilgungsbestimmung und Paragraf 366 BGB prüfen. Bei laufender Akte Alt-Neu-Delta ausgeben, bei Betriebskost... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/03-kontoauszug-mietkonto-auslesen/SKILL.md) |
| [`04-belegmatrix-aufbauen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/04-belegmatrix-aufbauen/SKILL.md) | Belegmatrix nach Mietkonto und Aktenrekonstruktion aufbauen, wenn Forderungsposten, Tatsachen, SAP- oder DMS-Fundstellen und spätere K-/B-Anlagen verknüpft werden müssen. Nicht für Rohdatenintake oder PDF-Finalisierung. Output Beweis- un... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/04-belegmatrix-aufbauen/SKILL.md) |
| [`05-chronologie-fallakte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/05-chronologie-fallakte/SKILL.md) | Chronologie, Ereignisachse und Fristenhistorie aufbauen oder mit neuer Zahlung, Gerichtspost und Korrespondenz fortschreiben. Klageeinreichung, Zustellung, Rechtshängigkeit, Delta, überholte Annahmen und Kostenpfad zeitlich ordnen. Outpu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/05-chronologie-fallakte/SKILL.md) |
| [`06-fallziel-renofa-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/06-fallziel-renofa-triage/SKILL.md) | Verbindlicher interner Router nach Intake, Fallkarte oder Änderungskarte. Prüft Fallziel, Rolle, RDG, Paragraf 79 ZPO, interne 10000-EUR-Freigabe und Eskalation. Wählt automatisch Zahlung, Kündigung, Räumung, Mieterhöhung, Verteidigung,... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/06-fallziel-renofa-triage/SKILL.md) |
| [`07-rdg-grenzen-check`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/07-rdg-grenzen-check/SKILL.md) | RDG-Prüfung der Renofa-Tätigkeit. Eigene Angelegenheit nach Paragraf 2 Abs. 1 RDG, Konzernverbund nach Paragraf 2 Abs. 3 Nr. 6 RDG und Prozessvertretung nach Paragraf 79 ZPO trennen. Drittinkasso erfordert Erlaubnis. Output Befugnisvermerk. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/07-rdg-grenzen-check/SKILL.md) |
| [`08-eskalation-an-anwalt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/08-eskalation-an-anwalt/SKILL.md) | Eskalation und Steuerung eigener externer Rechtsanwaltskanzlei. Trigger Insolvenz, Berufung, abweisendes oder teilabweisendes AG Urteil, Landgericht, Sachverständiger, Strafrecht, Kostenstreit, RA-Honorar und Stunden-Narrativ. Output Übe... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/08-eskalation-an-anwalt/SKILL.md) |
| [`09-mietrueckstand-mahnung-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/09-mietrueckstand-mahnung-erstellen/SKILL.md) | Mahnung wegen Mietrückstand. Erste Mahnung freundlich. Zweite Mahnung mit Klageandrohung. Verzugszinsen Paragraf 288 BGB. Konkrete Forderungsaufstellung Monat für Monat. Output Mahnschreiben als Brief mit Zugangsnachweis-Protokoll. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/09-mietrueckstand-mahnung-erstellen/SKILL.md) |
| [`10-zahlungsplan-stundungsvereinbarung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/10-zahlungsplan-stundungsvereinbarung/SKILL.md) | Zahlungsplan, Ratenplan, Teilzahlungsvereinbarung, Stundung, Schuldanerkenntnis und Verfallklausel aufsetzen oder gebrochenen Ratenplan auswerten. Restbetrag, laufende Miete und Wiedervorlage steuern. Output Vereinbarung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/10-zahlungsplan-stundungsvereinbarung/SKILL.md) |
| [`11-verzugsschaden-berechnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/11-verzugsschaden-berechnen/SKILL.md) | Verzugsschaden nach Paragraf 280 und 286 BGB. Zinsen, Inkasso- und Anwaltskosten, Bonitätsauskunft und Prozesskosten nach erledigendem Ereignis prüfen. Mahnpauschale nicht bei Verbrauchern. Output Schadenstabelle. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/11-verzugsschaden-berechnen/SKILL.md) |
| [`12-vorgerichtliche-letzte-frist`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/12-vorgerichtliche-letzte-frist/SKILL.md) | Letzte kalendarische Frist mit Klageandrohung aus einer geprüften Mietforderung erstellen. Zugang, angemessene Fristlänge, Kündigungsschwelle, gesetzliche Folgekosten und Sozialleistungshinweise trennen. Keine Mahnung als Kündigungsvorau... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/12-vorgerichtliche-letzte-frist/SKILL.md) |
| [`13-fristlose-kuendigung-zahlungsverzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/13-fristlose-kuendigung-zahlungsverzug/SKILL.md) | Fristlose Kündigung wegen Mietzahlungsverzug nach Paragraf 543 und 569 BGB erstellen. Rückstandsschwelle, zwei Termine, längerer Zeitraum, hilfsweise ordentliche Kündigung und Pflicht-Handoff zu Zustellung Skill 15. Output Kündigung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/13-fristlose-kuendigung-zahlungsverzug/SKILL.md) |
| [`14-ordentliche-kuendigung-pflichtverletzung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/14-ordentliche-kuendigung-pflichtverletzung/SKILL.md) | Ordentliche Kündigung wegen schuldhafter Pflichtverletzung nach Paragraf 573 BGB erstellen. Frist Paragraf 573c, Sozialklausel-Hinweis, Pflichtverletzung, Untervermietung, Schonfrist-Abgrenzung und Pflicht-Handoff zu Zustellung Skill 15.... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/14-ordentliche-kuendigung-pflichtverletzung/SKILL.md) |
| [`15-kuendigung-zustellung-nachweis`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/15-kuendigung-zustellung-nachweis/SKILL.md) | Pflichtskill nach freigegebenem Kündigungsentwurf. Freigabekarte, Zugang, Botenvermerk, Einwurf, Zeuge, Briefkasten, Rückscheinrisiko, Einwurf-Einschreiben und Zustellnachweis für alle Mieter sichern. Keine Email oder SMS. Output Zustell... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/15-kuendigung-zustellung-nachweis/SKILL.md) |
| [`16-widerspruch-mieter-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/16-widerspruch-mieter-pruefen/SKILL.md) | Sozialwiderspruch des Mieters gegen Kündigung nach Paragraf 574 BGB prüfen. Härtefall, Ersatzwohnraum, Krankheit, Alter, Suizidgefahr, Räumungsaufschub und fristlose Kündigung abgrenzen. Nicht Mahnbescheid-Widerspruch. Output Empfehlung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/16-widerspruch-mieter-pruefen/SKILL.md) |
| [`17-mahnbescheid-online-antrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/17-mahnbescheid-online-antrag/SKILL.md) | Optionale Mahnverfahren-Abzweigung für bestimmte Euro-Geldforderung prüfen. Ausschlüsse nach Paragraf 688 ZPO, Mahngericht, späteres Streitgericht, erwarteten Widerspruch, Zustellung und Verjährungshemmung trennen. Output Entscheidungsvo... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/17-mahnbescheid-online-antrag/SKILL.md) |
| [`18-widerspruch-vollstreckungsbescheid`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/18-widerspruch-vollstreckungsbescheid/SKILL.md) | Mahnbescheid-Widerspruch oder Einspruch gegen Vollstreckungsbescheid auswerten. Abgabe an Streitgericht, Anspruchsbegründung, Fristsetzung, Einwendungen, Anlagenplan und Rücksprung zur Zahlungsklage vorbereiten. Output Anspruchsbegründung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/18-widerspruch-vollstreckungsbescheid/SKILL.md) |
| [`19-vollstreckungsbescheid-antrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/19-vollstreckungsbescheid-antrag/SKILL.md) | Vollstreckungsbescheid nur als optionale Folge eines zuvor gewählten Mahnverfahrens prüfen. Fristen, Einspruchsrisiko und Titelqualität bewerten. Output Entscheidungsvorlage und Vollstreckungs-Übergabe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/19-vollstreckungsbescheid-antrag/SKILL.md) |
| [`20-zahlungsklage-mietrueckstand-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/20-zahlungsklage-mietrueckstand-erstellen/SKILL.md) | Reine Zahlungsklage wegen Mietrückstand ohne Räumungsantrag erstellen. Mietkonto, Belegmatrix, Rubrum, Zahlungsantrag, Zinsen, Aufrechnung und Kostenpfad verarbeiten. Bei Räumung, Herausgabe, Kündigung oder Kombiklage führt Skill 24. Out... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/20-zahlungsklage-mietrueckstand-erstellen/SKILL.md) |
| [`21-klage-streitwert-gerichtskosten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/21-klage-streitwert-gerichtskosten/SKILL.md) | Streitwert und Gerichtskosten für Zahlungsklage, Räumung, Mieterhöhung und Mietpreisbremse prüfen. Geldforderung als Hauptforderung, mietrechtliche GKG-Spezialwerte, Stichtag und Vorschuss nach Paragraf 12 GKG kontrollieren. Output Berec... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/21-klage-streitwert-gerichtskosten/SKILL.md) |
| [`22-zustaendigkeit-amtsgericht-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/22-zustaendigkeit-amtsgericht-pruefen/SKILL.md) | Sachliche und örtliche Zuständigkeit prüfen plus Anwaltszwang nach Paragraf 78 ZPO. Wohnraummietsachen stets AG Paragraf 23 Nr. 2a GVG ohne Anwaltszwang. Gewerberaum streitwertabhängig. Output Zuständigkeitsvermerk mit Norm-Anker. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/22-zustaendigkeit-amtsgericht-pruefen/SKILL.md) |
| [`23-klage-egvp-bea-einreichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/23-klage-egvp-bea-einreichen/SKILL.md) | Gerichtsfertige Dokumentenproduktion für Klage, Replik, Antrag und sonstigen Schriftsatz. Nutze ihn bei fertig zur Einreichung, beA-ready, eBO, Schriftsatz finalisieren oder Anlagenpaket. Prüft Eigenvertretung oder Kanzlei, Einreichungsw... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/23-klage-egvp-bea-einreichen/SKILL.md) |
| [`24-raeumungsklage-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/24-raeumungsklage-erstellen/SKILL.md) | Leadskill für Räumungsklage Wohnraum nach Kündigung. Wohnung räumen und herausgeben, Kombiklage mit Zahlung, Kündigungszustellung, Sozialwiderspruch, Räumungsstreitwert, Zahlung vor Zustellung und Schonfrist nach Rechtshängigkeit prüfen.... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/24-raeumungsklage-erstellen/SKILL.md) |
| [`25-raeumungsfrist-vollstreckung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/25-raeumungsfrist-vollstreckung/SKILL.md) | Räumungstitel, Räumungsfrist Paragraf 721 ZPO, Räumungstermin, Gerichtsvollzieherauftrag, GV-Auftrag, Vollstreckungsschutz Paragraf 765a ZPO, Attest, Suizidgefahr, Sozialdienst und Fristverlängerung prüfen. Output Antrag. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/25-raeumungsfrist-vollstreckung/SKILL.md) |
| [`26-berliner-modell-raeumung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/26-berliner-modell-raeumung/SKILL.md) | Berliner Räumung als beschränkten Vollstreckungsauftrag nach Paragraf 885a ZPO prüfen. Besitzübergabe ohne Abtransport durch den Gerichtsvollzieher, Dokumentation, Verwahrung, Herausgabe, Monatsfrist, Verwertung, Vernichtung, Haftung und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/26-berliner-modell-raeumung/SKILL.md) |
| [`27-schonfristzahlung-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/27-schonfristzahlung-erkennen/SKILL.md) | Schonfristzahlung erst nach Rechtshängigkeit der Räumungsklage prüfen. Jobcenter-Zahlung, vollständige Befriedigung, fristlose und ordentliche Kündigung, Kostenpfad und Klageumstellung trennen. Zahlung vor Zustellung als eigenes Kostener... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/27-schonfristzahlung-erkennen/SKILL.md) |
| [`28-mieterhoehung-bgb-558-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/28-mieterhoehung-bgb-558-vorbereiten/SKILL.md) | Verwenden vor dem ersten Mieterhöhungsverlangen, wenn Ausgangsmiete, Sperrfrist, Kappungsgrenze, Mietspiegelfeld, Wohnlage oder Merkmalgruppen noch geprüft werden müssen. Berechnet die Obergrenzen nach Paragraf 558 BGB und erzeugt eine V... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/28-mieterhoehung-bgb-558-vorbereiten/SKILL.md) |
| [`29-mieterhoehungsverlangen-text`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/29-mieterhoehungsverlangen-text/SKILL.md) | Verwenden, wenn die Prüfung aus Skill 28 abgeschlossen ist und das Mieterhöhungsverlangen nach Paragrafen 558 und 558a BGB versandfertig entworfen werden soll. Übernimmt nur belegte Wohnungsmerkmale, berechnet Zustimmungs-, Wirkungs- und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/29-mieterhoehungsverlangen-text/SKILL.md) |
| [`30-zustimmungsklage-mieterhoehung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/30-zustimmungsklage-mieterhoehung/SKILL.md) | Verwenden erst nach wirksamem Mieterhöhungsverlangen und abgelaufener Zustimmungsfrist, wenn Zustimmung fehlt oder nur teilweise vorliegt. Prüft Zugang, materielle Zielmiete, Klagefrist nach Paragraf 558b Abs. 2 BGB, Teilzustimmung, Nach... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/30-zustimmungsklage-mieterhoehung/SKILL.md) |
| [`31-kappungsgrenze-mietpreisbremse`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/31-kappungsgrenze-mietpreisbremse/SKILL.md) | Kappungsgrenze bei Bestandsmieterhöhung und Mietpreisbremse bei Neuvermietung getrennt prüfen. 15 Prozent oder 20 Prozent Cap, 10 Prozent Grenze, Landesverordnung, Berlin, Vormiete, Neubau und Modernisierung berechnen. Output Normcheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/31-kappungsgrenze-mietpreisbremse/SKILL.md) |
| [`32-datenschutz-mieterdaten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/32-datenschutz-mieterdaten/SKILL.md) | Datenschutz für Miet-, Prozess- und Vollstreckungsakten nach DSGVO und BDSG prüfen. Rechtsgrundlage, Zweckbindung, Datenminimierung, Auskunft, Aufbewahrung, Löschung, Auskunftei-Meldung und Schadenersatzrisiko mit EuGH-Ankern steuern. Nu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/32-datenschutz-mieterdaten/SKILL.md) |
| [`33-dokumentenmix-ocr-sichten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/33-dokumentenmix-ocr-sichten/SKILL.md) | Verbindlicher Default-Start für neuen Fall, Projektordner, Aktenordner, Upload-Bundle und gemischten Neuzugang. Aktiviert bei kurzen Aufträgen wie neuer Fall, Ordner prüfen oder Akte fertig machen. Fragt nie nach einer Skillauswahl, sich... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/33-dokumentenmix-ocr-sichten/SKILL.md) |
| [`34-sap-excel-pdf-normalisieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/34-sap-excel-pdf-normalisieren/SKILL.md) | Technischer Anschluss-Skill nach Autostart oder SAP-Intake. Normalisiert SAP, Excel, PDF, DocuWeb, DATEV, RA-MICRO, XML, JSON, Datenbankexport, DMS-Register und MCP-Planung. Kein Fachpfad. Output fallakte.json, dms-register.csv, fallakte... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/34-sap-excel-pdf-normalisieren/SKILL.md) |
| [`35-sap-belegluecken-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/35-sap-belegluecken-klaeren/SKILL.md) | Beleglücke, fehlende Anlage, fehlende SAP-Belegnummer, Kontoauszugslücke, DMS-Treffer fehlt oder Buchhaltungsbeleg unklar. Forderung, Vertrag, Zustellung und Zahlung absichern. Rückfragen formulieren. Output priorisierte Liste. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/35-sap-belegluecken-klaeren/SKILL.md) |
| [`36-fallstrategie-bis-10000`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/36-fallstrategie-bis-10000/SKILL.md) | Strategieentscheidung erst nach Triage für Forderungs- und Vertragsstreitigkeiten an der internen 10000-EUR-Grenze. Nutzen, Risiko, Kulanz, Direktklage, Kündigung, Vergleich oder Eskalation abwägen. Kein Intake- oder Standard-Router. Out... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/36-fallstrategie-bis-10000/SKILL.md) |
| [`37-klageerwiderung-auswerten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/37-klageerwiderung-auswerten/SKILL.md) | Neue Klageerwiderung, Gerichtspost oder gegnerischen Schriftsatz im laufenden Prozess als Delta auswerten. Frist, Einwendungen, Zahlung nach Klage, Aufrechnung, Kostenpfad, Beweisrisiken und überholte Prozesspositionen extrahieren. Outpu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/37-klageerwiderung-auswerten/SKILL.md) |
| [`38-replik-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/38-replik-erstellen/SKILL.md) | Replik auf Klageerwiderung oder gerichtlichen Hinweis erstellen. Gegenvortrag, Beweise, Anlagen, Anträge und Kostenpfad bei erledigender Zahlung aktualisieren. Output Schriftsatz. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/38-replik-erstellen/SKILL.md) |
| [`39-beweisangebot-anlagenplan`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/39-beweisangebot-anlagenplan/SKILL.md) | Beweisangebote und fortlaufenden Anlagenplan für Klage, Replik und Verteidigung erzeugen. Ordnet jede erhebliche Tatsache einem zulässigen Beweismittel, Beweislast, Original, K- oder B-Nummer, Dateiversion und Beschaffungsstatus zu. Nutz... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/39-beweisangebot-anlagenplan/SKILL.md) |
| [`40-urkundsprozess-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/40-urkundsprozess-pruefen/SKILL.md) | Urkundenprozess nach Paragrafen 592 bis 600 ZPO für Mietforderungen prüfen. Bestimmte Geldforderung, vollständiger Urkundenbeweis, Klagekennzeichnung, Beweismittelgrenzen, Unstatthaftigkeitsrisiko, Vorbehaltsurteil und Nachverfahren abar... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/40-urkundsprozess-pruefen/SKILL.md) |
| [`41-vergleich-raten-prozess`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/41-vergleich-raten-prozess/SKILL.md) | Außergerichtlichen oder gerichtlichen Vergleich mit Raten, Zahlung, Räumung und Kosten strukturieren. Vollstreckbarer Inhalt nach Paragrafen 278 Abs. 6 und 794 ZPO, optionale Verfallklausel, Abschlussbefugnis, Kostenquote, Monitoring und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/41-vergleich-raten-prozess/SKILL.md) |
| [`42-mieterklage-verteidigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/42-mieterklage-verteidigen/SKILL.md) | Nur bei umgekehrter Prozesslage: Mieter verklagt Vermieterin oder erhebt Widerklage. Verteidigung gegen Mietminderung, Rückzahlung, Kaution, Mängel, Mietpreisbremse, Eigenbedarfsschaden, Vorkaufsrecht oder Unterlassung. Nicht bloße Einwe... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/42-mieterklage-verteidigen/SKILL.md) |
| [`43-mieterverein-anwalt-korrespondenz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/43-mieterverein-anwalt-korrespondenz/SKILL.md) | Außergerichtliche Schreiben von Mieter, Mieterverein oder Anwalt beantworten. Vollmacht, Datenschutz, Beleganforderung, Mietminderung, Vergleichsangebot, Zahlungsbereitschaft und Fristen prüfen. Nicht gerichtliche Klageerwiderung. Output... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/43-mieterverein-anwalt-korrespondenz/SKILL.md) |
| [`44-betriebskosten-rueckstand-streit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/44-betriebskosten-rueckstand-streit/SKILL.md) | Prüft Betriebskosten-Nachforderungen, Vorauszahlungen und Einwendungen. Rechnet Kostenanteile nach, klärt digitale Belegeinsicht und trennt Abrechnungsfehler von vorläufigen Zahlungshindernissen. Liefert eine konkrete Beleganforderung, M... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/44-betriebskosten-rueckstand-streit/SKILL.md) |
| [`45-hausverwaltung-schnittstelle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/45-hausverwaltung-schnittstelle/SKILL.md) | Leadskill für operative Rückfragen an Hausverwaltung, Objektbetreuung, Buchhaltung, DMS-Administration, IT und Forderungsmanagement. Nutze bei Beleglücke, Zustellung, Mängelstatus, Zahlungsklärung oder Schnittstellenmapping. Output inter... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/45-hausverwaltung-schnittstelle/SKILL.md) |
| [`46-kostenfestsetzung-antrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/46-kostenfestsetzung-antrag/SKILL.md) | KFA nach prozessualer Kostengrundentscheidung in Urteil, Beschluss oder Vergleich vorbereiten. Tenor, Quote, Gerichtskosten, tatsächlich entstandene externe Anwaltskosten, Auslagen, Zahlungen, Zinsantrag und gegnerischen KFA nach Paragra... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/46-kostenfestsetzung-antrag/SKILL.md) |
| [`47-kostenbeschluss-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/47-kostenbeschluss-pruefen/SKILL.md) | KFB und Kostenfestsetzungsbeschluss prüfen. Abweichung vom KFA, Tenor, Betrag, Zinsen, Quote, Zustellung, Rechtsbehelfsfrist, Erinnerung, sofortige Beschwerde, vollstreckbare Ausfertigung und Zahlung prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/47-kostenbeschluss-pruefen/SKILL.md) |
| [`48-titulierte-forderung-vollstrecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/48-titulierte-forderung-vollstrecken/SKILL.md) | Verwenden nach vorhandenem Urteil, Vergleich, Vollstreckungsbescheid oder KFB, wenn eine konkrete Vollstreckungsmaßnahme vorbereitet werden soll. Prüft Titel, Klausel, Zustellung, Restforderung, Zinsen und Kosten und strukturiert Gericht... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/48-titulierte-forderung-vollstrecken/SKILL.md) |
| [`49-kontoermittlung-und-drittauskunft`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/49-kontoermittlung-und-drittauskunft/SKILL.md) | Verwenden nur nach Titel, wenn Bank, Arbeitgeber oder andere pfändbare Spur unbekannt ist und eine konkrete Vollstreckung deshalb stockt. Prüft Voraussetzungen und zulässigen Weg für Drittauskunft nach Paragraf 802l ZPO, Schuldnerverzeic... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/49-kontoermittlung-und-drittauskunft/SKILL.md) |
| [`50-vollstreckungsakte-monitoring`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/50-vollstreckungsakte-monitoring/SKILL.md) | Vollstreckungsakte nach Titelgewinn führen und bei neuer Zahlung, Rate, GV-Rücklauf, Pfändung oder Insolvenzmeldung als Delta fortschreiben. Fristen, Tilgung, Kosten und Verjährung überwachen. Output Änderungskarte, Monitoring und nächst... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=rechtsabteilung-forderungsmanagement-immobilienunternehmen/skills/50-vollstreckungsakte-monitoring/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->


## Verzeichnisse der Rechtssammlung

[Startseite](../README.md) · [Alle Skills](../SKILLS.md) · [Skills dieses Plugins](../skills-index/rechtsabteilung-forderungsmanagement-immobilienunternehmen.md) · [Downloads](../ASSET_INDEX.md) · [Weitere Testakten](../testakten/README.md) · [Plugin-Dateien](.)
