# Handelsregister Praxis

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Praxisplugin für den Umgang mit dem Handelsregister: Anmeldung, Registergericht, Rechtspfleger, Registerrichter, Beanstandung, Zwischenverfügung, Beschwerde, Gesellschafterliste, Kapitalmaßnahmen, Firma, Vertretung, Prokura, Löschung, Insolvenzvermerk und registerfeste Nachweise.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`handelsregister-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/handelsregister-praxis/handelsregister-praxis-werkstatt.md" download><code>handelsregister-praxis-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/handelsregister-praxis/handelsregister-praxis-schnellstart.md" download><code>handelsregister-praxis-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Rabenhof Sensorik GmbH - Registergericht Charlottenburg, HRB 246810 B: [Gesamt-PDF](../testakten/handelsregister-registergericht-rabenhof-gmbh-2026/gesamt-pdf/handelsregister-registergericht-rabenhof-gmbh-2026_gesamt.pdf), [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip), [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine gesellschaftsrechtliche Maßnahme rechtssicher beschliessen und dokumentieren.
Ein Registergerichts-Cockpit für Gesellschaftsrechtler, Notariate, Kanzleien und Rechtsabteilungen. Es ordnet, was eingetragen werden soll, welche Urkunden nötig sind, wer beim Registergericht entscheidet, wie man Beanstandungen beantwortet und wann Beschwerde oder Eilrechtsschutz Sinn ergeben.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `handelsregister-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- HGB §§ 8 ff., § 15
- FamFG Registersachen und Beschwerde
- GmbHG Anmeldung, Gesellschafterliste, Kapitalmaßnahmen
- [Registerportal der Länder](https://www.handelsregister.de)
- [Unternehmensregister](https://www.unternehmensregister.de)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 77 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtsloeschung-familienloeschung-registerblatt` | Prüft Löschungsandrohung, Anhörung, Unrichtigkeit, Vermögenslosigkeit, Gegenwehr und Dokumentationsstrategie im Handelsregister Praxis. |
| `auslandsurkunden-apostille-legalisation-uebersetzung` | Prüft Apostille, Legalisation, beglaubigte Übersetzung, Existenznachweis und Vertretungsnachweis im Handelsregister Praxis. |
| `beanstandung-zwischenverfuegung` | Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, formuliert Nachreichung, Bitte um Fristverlängerung oder Beschwerdevorbereitung im Handelsregister Praxis. |
| `bekanntmachungen-monitoring` | Erstellt Monitoringplan für Bekanntmachungen, Friststart, Einspruchsfenster und Mandantenalerts im Handelsregister Praxis. |
| `chronologischer-registerauszug` | Rekonstruiert Registergeschichte, kritische Umschlagpunkte und mögliche Inkonsistenzen im Handelsregister Praxis. |
| `closing-handelregister-einstweiliger` | Prüft CP/CS, Eintragungsabhängigkeiten, Vollzugsreihenfolge, Escrow, Notarbestätigung und Bring-down im Handelsregister Praxis. |
| `einstweiliger-rechtsschutz-registerstreit` | Plant Schutz gegen drohende Eintragung, Verzögerung, Registersperre, Gesellschafterlistenstreit und Vollzugsschäden im Handelsregister Praxis. |
| `eintragung-prozessvergleich-registerfolge` | Übersetzt gerichtliche Vergleiche in Beschluss, Anmeldung, Liste, Löschung oder Berichtigung im Handelsregister Praxis. |
| `erlaubnispflichtige-taetigkeit-famfg` | Prüft KWG, ZAG, GewO, Handwerk, Arbeitnehmerüberlassung und ob das Registergericht Nachweise verlangen kann im Handelsregister Praxis. |
| `famfg-beschwerde-registersache` | Prüft Statthaftigkeit, Beschwer, Frist, Form, Abhilfe, Nichtabhilfe und Beschwerdebegründung gegen Registerentscheidungen im Handelsregister Praxis. |
| `fehlerhafte-eintragung-berichtigung` | Prüft Schreibfehler, materiell falsche Eintragung, Amtskorrektur, Löschung, neue Anmeldung und Haftungsnotiz im Handelsregister Praxis. |
| `firma-firmenbildung-formwechsel-registercheck` | Prüft Firmenkern, Unterscheidbarkeit, Irreführung, Rechtsformzusatz, IHK-Stellungnahme und Abgrenzung zu Marke/Domain im Handelsregister Praxis. |
| `formwechsel-registercheck` | Prüft Formwechselbericht, Beschlüsse, Satzung, neue Firma, Registerwechsel und Identitätskontinuität im Handelsregister Praxis. |
| `frist-und-vollzugslog-register` | Baut ein Log für Beanstandungsfristen, Eintragungsdatum, Bekanntmachung, Closing-Abhängigkeit und Mandantenbericht im Handelsregister Praxis. |
| `genossenschaft-registerschnittstelle` | Prüft Vorstand, Aufsichtsrat, Prüfung, Satzung und Eintragungslogik bei eG im Handelsregister Praxis. |
| `gesellschafterlistenstreit-eilstrategie-gmbh` | Ordnet Anspruch, einstweilige Verfügung, Registersperre, materiellen Streit und Kommunikation mit Registergericht/Notar im Handelsregister Praxis. |
| `gmbh-co-kg-registerdoppelvollzug` | Koordiniert KG-Register, Komplementär-GmbH, Vertretung, Gesellschafterlisten und Firmenidentität im Handelsregister Praxis. |
| `gmbh-geschaeftsfuehrerbestellung-abberufung` | Prüft Beschluss, Anmeldung, Versicherung, Vertretungsregel, Amtsannahme, Abberufung und Handelsregistervollzug im Handelsregister Praxis. |
| `gmbh-gesellschafterliste-paragraph-gruendung` | Prüft Liste, Prozentangaben, Veränderungsspalte, Notarzuständigkeit, Legitimationswirkung und Streit über Unrichtigkeit im Handelsregister Praxis. |
| `gmbh-gruendung-erstanmeldung` | Checkt Stammkapital, Einzahlung, Geschäftsführer, Versicherung, Musterprotokoll, Gesellschaftsvertrag und Registereintragung im Handelsregister Praxis. |
| `gmbh-kapitalerhoehung-bareinlage` | Prüft Satzungsänderung, Übernahme, Einzahlung, Anmeldung, Versicherung, Liste und Registervollzug im Handelsregister Praxis. |
| `gmbh-kapitalerhoehung-sacheinlage` | Prüft Sacheinlagebericht, Werthaltigkeit, verdeckte Sacheinlage, Anmeldung und Beanstandungsrisiko im Handelsregister Praxis. |
| `gmbh-kapitalherabsetzung-und-schutzjahr` | Prüft Gläubigerschutz, Sperrjahr, Bekanntmachungen, Versicherung und registerfeste Unterlagen im Handelsregister Praxis. |
| `gmbh-liquidation-und-loeschung` | Führt durch Auflösung, Liquidatoren, Sperrjahr, Schlussbilanz, Löschung, Nachtragsliquidation und Registerkommunikation im Handelsregister Praxis. |
| `gmbh-satzungsaenderung-handelsvollmacht-nicht` | Prüft Beschlussmehrheit, notarielle Beurkundung, vollständige Neufassung, Gegenstand, Firma, Sitz, Kapital und Anmeldung im Handelsregister Praxis. |
| `handelsvollmacht-nicht-eintragungsfaehig` | Erklärt, was nicht ins Register gehört und wie interne Vollmachten dennoch sicher dokumentiert werden im Handelsregister Praxis. |
| `hgb-publizitaet-paragraph-15` | Prüft negative und positive Publizität, Bekanntmachung, Gutgläubigkeit, Dritte und Risiko falscher Registerlage. |
| `insolvenzvermerk-registereintrag` | Prüft Eintragung von Eröffnung, Eigenverwaltung, Aufhebung, Insolvenzplan, Freigabe und Wirkungen für Vertretung im Handelsregister Praxis. |
| `internationaler-registervergleich` | Vergleicht Companies House, irische/österreichische/schweizer Register und deutsche Nachweisanforderungen im Handelsregister Praxis. |
| `kaltstart-routing` | Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau. |
| `kg-kommanditist-eintritt-austritt-haftsumme` | Prüft Einlage/Haftsumme, Sonderrechtsnachfolge, Austritt, Nachhaftung und Registerpublizität im Handelsregister Praxis. |
| `ki-registerakte-nachlass` | Zwingt zu Belegpfad, Registerauszug, Aktenzeichen, Normenanker und klarer Kennzeichnung nicht verifizierter Annahmen im Handelsregister Praxis. |
| `nachlass-und-testamentsvollstrecker-register` | Prüft Erbschein, Europäisches Nachlasszeugnis, Testamentsvollstreckerzeugnis und Vertretungsmacht im Handelsregister Praxis. |
| `notar-registergericht-kommunikation` | Erstellt klare Nachreichungslisten, Telefonnotizen, E-Mail-Entwürfe und Mandantenupdates ohne Schuldzuweisungschaos im Handelsregister Praxis. |
| `ohg-kg-online-abruf-partg-partgmbb` | Prüft kaufmännischen Betrieb, Statuswechsel, Anmeldung, Gesellschafter, Vertretung und MoPeG-Schnittstellen im Handelsregister Praxis. |
| `online-abruf-registerportal-unternehmensregister` | Führt durch Handelsregister, Unternehmensregister, Bekanntmachungen, Chronologie, Ausdrucke, Screenshots und Beleglog im Handelsregister Praxis. |
| `partg-partgmbb-register` | Prüft Partnerschaftsregister, Berufszulassung, Namensführung, Haftungsbeschränkung und Berufshaftpflichtnachweis im Handelsregister Praxis. |
| `prokura-eintragung-rechtsabteilung` | Prüft Einzel-/Gesamtprokura, Filialprokura, Gesamtvertretung, Widerruf, Publizität und Unterschriftenmuster im Handelsregister Praxis. |
| `rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug` | Rechtsabteilungs-Fachmodul für Geschäftsführerbestellung mit Auslandsbezug: Identität, Versicherung, Unterschrift und Übersetzung werden sauber vorbereitet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im H... |
| `rechtsabteilung-gesellschafterliste-nach-streit-und-ev` | Rechtsabteilungs-Fachmodul für Gesellschafterliste nach Streit und EV: Rechtsabteilungen bauen registertaugliche Listenpakete und Widerspruchsstrategien. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Hand... |
| `rechtsabteilung-insolvenzvermerk` | Rechtsabteilungs-Fachmodul für Insolvenzvermerk und ausländischer Trustee: Vertretungsmacht ausländischer Insolvenzorgane wird registertauglich nachgewiesen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im... |
| `rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung` | Rechtsabteilungs-Fachmodul für Kapitalerhöhung und Zwischenverfügung: Zwischenverfügungen werden in heilbare Punkte, Streitpunkte und Beschwerde sortiert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Han... |
| `rechtsabteilung-mopeg-gesellschaftsregister-und-ohg-sprung` | Rechtsabteilungs-Fachmodul für MoPeG-Gesellschaftsregister und OHG-Sprung: GbR, eGbR, OHG und Grundstücksfähigkeit werden registerlogisch abgegrenzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsr... |
| `rechtsprechung-register-frist-vollzugslog` | Legt fest, wie Entscheidungen in Registersachen nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink ausgegeben werden im Handelsregister Praxis. |
| `rechtsschein-innenstreit-register` | Trennt materielles Gesellschaftsrecht, Registerlage, Vertretungsmacht und Gutglaubensschutz im Handelsregister Praxis. |
| `register-mandantenbrief` | Erstellt klare Mandantenupdates: Stand, Risiko, To-dos, Fristen, nächste Entscheidung im Handelsregister Praxis. |
| `register-qualitaetsgate-vor-einreichung` | Checkliste vor dem Absenden: Urkunden, Beschlüsse, Listen, Unterschriften, Kapital, Namen, Daten, Registerblatt im Handelsregister Praxis. |
| `registerakte-schnellscan-registerauszug-lesen` | Erstellt eine Vollzugskarte aus Satzung, Beschluss, Anmeldung, Liste, Notarvermerk, Gerichtsschreiben und Fristenlog im Handelsregister Praxis. |
| `registerauszug-lesen` | Erklärt Abteilungen/Spalten, Historie, Vertretung, Kapital, Firma, Prokura, Insolvenz und Bekanntmachungen im Handelsregister Praxis. |
| `registerbeweis-im-prozess` | Bereitet Registerauszüge, Bekanntmachungen und Nachweise prozesstauglich auf im Handelsregister Praxis. |
| `registergericht-rollen-datenschutz` | Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache richterlich, rechtspflegerisch oder rein vollzugstechnisch hängt im Handelsregister Praxis. |
| `registergericht-und-datenschutz` | Klärt öffentliche Registerdaten, sensible Anlagen, Schwärzungen, Anschriften und Löschungswünsche im Handelsregister Praxis. |
| `registerkosten-und-notarkosten` | Ordnet Register- und Notarkosten grob, vermeidet Doppelvollzug und erklärt Mandanten die Kostenlogik im Handelsregister Praxis. |
| `registerrecht-aktiengesellschaft-vorstand` | Prüft Bestellung, Vertretung, Satzungsänderungen, Kapitalmaßnahmen und Eintragung bei der AG im Handelsregister Praxis. |
| `registerrecht-beschlussmaengel-und-registervollzug` | Prüft, ob das Registergericht bei Kapitalmaßnahme, Geschäftsführerbestellung oder Satzungsänderung Beschlussmängel beachten muss, wie weit die formelle Prüfung reicht und wann der materielle Streit auf Zivilprozess/Eilrechtsschutz verlag... |
| `registerrecht-digitalgruendung` | Prüft Online-Beurkundung/Beglaubigung, Identifizierung, digitale Einreichung und Medienbruch im Handelsregister Praxis. |
| `registerrecht-fehlende-einzahlung-fehlerhafte` | Prüft Geschäftsführerversicherung, Kontoauszug, Hin- und Herzahlen, verdeckte Sacheinlage und Haftungsnotiz im Handelsregister Praxis. |
| `registerrecht-fehlerhafte-geschaeftsfuehreradresse` | Prüft Anschriften, Geburtsdaten, Schutzinteressen, Schwärzungsmöglichkeiten und Auszugstypen im Handelsregister Praxis. |
| `registerrecht-kapitalgesellschaft-co-kg-komplementaerwechsel` | Koordiniert Ausscheiden/Eintritt der Komplementär-GmbH, Haftung, Vertretung und Registerreihenfolge im Handelsregister Praxis. |
| `registerrecht-mandatsannahme-notarferne` | Klärt Rolle der anwaltlichen Beratung neben Notar, Verantwortungsgrenzen und Mandantensteuerung im Handelsregister Praxis. |
| `registerrecht-niederlassung-registergericht` | Prüft eintragungsfähige Zweigniederlassung, unselbständige Betriebsstätte und Adress-/Vertretungsangaben im Handelsregister Praxis. |
| `registerrecht-registergericht-telefonat-protokoll` | Erstellt kurze Telefonnotiz mit Name, Aktenzeichen, Beanstandung, Frist, Zusage und Folgeschritt im Handelsregister Praxis. |
| `registerrecht-registerzeichen-und-aktenzeichen` | Erklärt HRB, HRA, PR, GnR, VR, Registernummer, Gericht und Aktenzeichenlogik im Handelsregister Praxis. |
| `registerrecht-scheinloeschung` | Prüft Restvermögen, Prozessfähigkeit, Bestellung Nachtragsliquidator und Registereintragung im Handelsregister Praxis. |
| `registerrecht-se-und-europaeische-gesellschaft` | Prüft SE-Firma, Sitz, monistisches/dualistisches System, Leitung, Verwaltungsrat und grenzüberschreitende Bezüge im Handelsregister Praxis. |
| `registerrecht-umbenennung-rebranding` | Prüft Firmenänderung, Satzung, IHK, Marken-/Domainkonflikte, Bekanntmachung und Mandantenkommunikation im Handelsregister Praxis. |
| `registersperre-closing-sitz-inlandsanschrift` | Bewertet Sperrwirkung, einstweilige Verfügung, Gesellschafterlistenkonflikt und Alternativvollzug im Handelsregister Praxis. |
| `sitz-inlandsanschrift-und-geschaeftsanschrift` | Prüft Satzungssitz, inländische Geschäftsanschrift, Empfangsbevollmächtigte, Briefkastenrisiken und Registereintragung im Handelsregister Praxis. |
| `todesfall-gesellschafter-register` | Prüft Erbnachweis, Sonderrechtsnachfolge, Testamentsvollstrecker, Liste und Registerkommunikation im Handelsregister Praxis. |
| `transparenzregister-schnittstelle-umwandlung` | Verbindet Handelsregisterdaten mit wirtschaftlich Berechtigten, GwG-Risiken und Meldepflichten im Handelsregister Praxis. |
| `umwandlung-registervollzug` | Prüft Verschmelzung, Spaltung, Formwechsel, Registerreihenfolge, Schlussbilanz und Bekanntmachung im Handelsregister Praxis. |
| `umzug-registerbezirk-amtsloeschung` | Prüft innerörtlich/anderer Bezirk, Satzungsänderung, Registerabgabe, Bekanntmachung und Adresslogik im Handelsregister Praxis. |
| `unternehmensgegenstand-beanstandung` | Formuliert eintragungsfähige Gegenstände ohne Erlaubnis-/Aufsichtsrechtsfalle und ohne zu enge Zukunftsfessel im Handelsregister Praxis. |
| `verein-registerschnittstelle-verschmelzung` | Klärt, wann Vereinsregisterlogik statt Handelsregisterlogik greift und welche Beschlüsse/Protokolle gebraucht werden im Handelsregister Praxis. |
| `verschmelzung-gmbh-registercheck` | Checkt Verschmelzungsvertrag, Zustimmungsbeschlüsse, Registeranmeldungen, Gläubigerschutz und Wirksamkeitszeitpunkt im Handelsregister Praxis. |
| `vollmacht-und-anmeldung-oeffentliche-beglaubigung` | Prüft notarielle Beglaubigung, Vertreteranmeldung, Untervollmacht, Signatur und elektronische Einreichung im Handelsregister Praxis. |
| `zweigniederlassung-auslaendische-gesellschaft` | Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsanschrift: Prüft Registerfähigkeit, Nachweise aus dem Herkunftsstaat, Übersetzung, Vertretungsmacht und deutsche Geschäftsansc... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
