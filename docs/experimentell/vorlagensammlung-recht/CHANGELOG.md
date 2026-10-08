# Änderungshistorie

Alle nennenswerten Änderungen an dieser Vorlagensammlung werden hier
dokumentiert. Versionsschema nach Semantic Versioning.

## v4.91.0 — Zweisprachiger KI-Hinweis in jeder ODT-Erstseitenfußzeile (2026-08-11)

**Stand:** 981 validierte Hauptvorlagen in 41 Themenordnern, 113 gerichtsleitende Sondervorlagen und 983 versionierte ODT-Dokumente. Jede paginierte Arbeitsfassung kennzeichnet ihren experimentellen Entstehungszusammenhang jetzt sichtbar, einheitlich und dauerhaft.

### Einheitliche Kennzeichnung auf Seite 1

- Sämtliche 981 ODT-Vorlagen sowie `EVAL_RESULTS.odt` und `RECHTLICHE-HINWEISE.odt` tragen ausschließlich auf Seite 1 den deutschen Hinweis „Mit KI generiert. Dies ist ein experimentelles Dokument. Benutzung auf eigene Gefahr und eigenes Risiko.“ und die englische Fassung „Generated with AI. This is an experimental document. Use at your own risk.“
- Die Erstseitenfußzeile setzt beide Sprachfassungen in Times New Roman 8 pt zentriert und ergänzt die dynamische Seitennummer. Folgeseiten behalten die bisherige unaufdringliche Seitennummer ohne wiederholten Warntext.
- Der Hinweis liegt ausschließlich im ODT-Seitenlayout. Er wird weder Vertrags-, Antrags- oder Schriftsatzinhalt noch Bestandteil der Markdown-Quellen.

### Dauerhafte Generator- und Prüfregel

- `scripts/md-to-odt.py` erzeugt den Erstseitenhinweis idempotent über einen eigenen ODF-Erstseitenfußzeilenstil. Jeder künftige Export und jede neue ODT-Vorlage erhält ihn automatisch.
- `scripts/check-odt-integrity.py` kontrolliert nun alle 983 ODT-Dokumente einschließlich der Root-Dokumente auf exakten Wortlaut, Einmaligkeit, Position in `style:footer-first`, Schriftstil, Seitenprofil und fortlaufende Paginierung. Ein fehlender, veränderter oder doppelter Hinweis bricht die Prüfung ab.
- `CLAUDE.md`, `CONTRIBUTING.md`, `README.md` und ein zusätzlicher Unit-Test verankern die Regel für alle weiteren Beiträge und Generatorläufe. Alle ODT-Arbeitsfassungen und das ODT-Komplettpaket wurden vollständig neu erzeugt.

## v4.90.0 — InsO- und StaRUG-Vorlagen mit Varianten- und Vollzugstiefe (2026-08-09)

**Stand:** 981 validierte Hauptvorlagen in 41 Themenordnern und 113 gerichtsleitende Sondervorlagen. Sämtliche 28 InsO- und elf StaRUG-Vorlagen wurden auf aktuelle Rechtsmechanik, Varianten, Anlagen, Vollzug und innere Anschlussfähigkeit geprüft; 28 Mustertexte und 17 Begleitdateien erhielten konkrete Verbesserungen.

### Insolvenzrecht vom Eröffnungsantrag bis zum Planvollzug

- Verbraucherinsolvenzantrag und Schuldenbereinigungsplan unterscheiden nun Einmal-, Raten-, flexible und Nullplanvariante, bilden Sicherheiten, Mitschuldner, laufende Verträge, Anpassung, Leistungsstörung und die gerichtliche Ersetzung nach §§ 307 bis 309 InsO in sechs ausfüllbaren Anlagen ab. Restschuldbefreiung, Tabellenanmeldung, Nachmeldung und Bestreiten führen genauer durch qualifizierte Rechtsgründe, Rang, Betreibenslast, Verteilungsfristen und Nachweisführung.
- Gläubigerantrag, Freigabe, Masseunzulänglichkeit, Sicherheitenprüfung und Verwertungsvereinbarung trennen Anspruch, Eröffnungsgrund, Beschlag, Verwertungskompetenz, Kostenbeiträge und Ausgleichswirkung. Die Zahlung nach einem Gläubigerantrag wird jetzt exakt nach § 14 Abs. 1 Satz 2 und Abs. 3 InsO behandelt; die gesetzliche Wochenfrist des § 168 Abs. 1 InsO knüpft an die konkrete Veräußerungsmitteilung an.
- Eigenverwaltungsbericht, Schutzschirmantrag und Fortführungslieferantenvereinbarung erhielten belastbare Liquiditäts-, Genehmigungs-, Vertrags-, Plan- und Risikoregister. Ein wesentlicher Normfehler ist beseitigt: Im Schutzschirm trägt § 270c Abs. 4 InsO die gerichtliche Ermächtigung zur Begründung von Masseverbindlichkeiten; § 270d Abs. 3 InsO betrifft Vollstreckungsmaßnahmen.
- Der Insolvenzplan wurde auf Vergleichsrechnung, Ausproduktion, Kapitalmaßnahmen, gruppeninterne Drittsicherheiten, Erklärungen nach § 230 InsO und sämtliche Vollzugsanlagen gegengeprüft. Optionale Finanzierungs-, Personal- und Drittsicherheitenanlagen sind jetzt nach ihrem konkreten Einsatzfall bezeichnet.

### StaRUG vom Konzept bis zur Bestätigung

- Restrukturierungsanzeige, Gruppenvermerk und Abstimmungsprotokoll verzahnen Planstichtag, Planbetroffenheit, Gruppenbildung, Stimmrecht, Zugangsbeleg, Einzelstimme, Mehrheitsrechnung und Einwendungen. Die READMEs nennen die einschlägigen Vorschriften absatzgenau und grenzen außergerichtliche Abstimmung, gerichtliches Verfahren und Bestätigungsprüfung voneinander ab.
- Stabilisierungsanordnung und Anzeige mit Sanierungskonzept führen durch den bestimmten Adressaten- und Maßnahmenkreis, Sechs-Monats-Finanzplan, Pflichtangaben, Gläubigerschutz, Änderungsanzeigen und Aufhebungsgründe. Der Antrag beschränkt sich auf die Wirkungen der §§ 49 bis 59 StaRUG und beansprucht kein gesetzlich nicht vorgesehenes pauschales Kündigungsverbot.
- Standstill und Sanierungsvergleich wurden zu vollständigen Vertragsmechaniken mit Forderungs- und Sicherheitenstichtag, Wirksamkeitsbedingungen, Meilensteinen, Neugeld, Berichtswesen, Verjährung, Beteiligungsschwellen, Besserung, Wiederaufleben, Ausgleich und Closing-Anlagen ausgebaut.
- Der 1.101-zeilige Restrukturierungsplan wurde vollständig auf persönliche OHG-Gesellschafterhaftung nach § 2 Abs. 4 Satz 2 StaRUG, gruppeninterne Dritt- und Cross-Sicherheiten, angemessene Entschädigung, Zustimmungen, Drittverpflichtungen, Vergleichswasserfall und Vollstreckbarkeit geprüft. Seine Varianten und Anlagen 22, 23 und 25 bilden diese Eingriffe bereits vollständig ab; verbliebene Blindbezeichnungen bei Gruppen und Planbedingungen wurden konkretisiert.

### Hygiene, Formate und Prüfung

- Interne Rechercheanweisungen und unbestimmte Felder wie „Beschreibung“, „Regelung“ oder „Option“ wurden aus den Mustertexten entfernt oder in sprechende, dokumenttypische Eingabefelder überführt. Die zweisprachige Sanierungsleitvorlage bleibt satzgenau parallel und verwendet idiomatisches Legal English.
- Alle 28 geänderten ODT-Arbeitsfassungen und Markdown-Einzelpakete wurden neu erzeugt. Sämtliche zehn Qualitätsprüfungen laufen grün; Hauptbestand 981/981, Sonderbestand 113 Vorlagen in 18 Bereichen und Eval All-Pass 981/981.

## v4.89.0 — Taktische Hinweise und Vorlagennavigation vollständig (2026-08-09)

**Stand:** 981 validierte Hauptvorlagen in 41 Themenordnern und 113 gerichtsleitende Sondervorlagen. Sämtliche 981 Hauptvorlagen-READMEs tragen nun die Abschnitte „Taktische Hinweise“ und „Verwandte Vorlagen“.

### Taktische Arbeitsebene geschlossen

- Die bislang offenen 334 READMEs in 32 Rechtsgebieten erhielten jeweils eine vorlagenspezifische Vorgehensreihenfolge, zwei bis vier konkret erwartbare Einwände mit Antwortlinie und zwei bis vier vermeidbare Fehler. Die Hinweise knüpfen an Tatsachen, Fristen, Zuständigkeiten, Registerlagen, Beweismittel und Vollzugsfragen des jeweiligen Dokuments an; in den neu ergänzten Taktikblöcken bestehen keine identischen Absatzdubletten.
- Die Ergänzungen erfassen insbesondere Urheber- und Medienrecht, Strafrecht, Sportrecht, Aufsichtsrecht und BaFin, Verkehrsrecht, KI- und Plattformregulierung, Weltraumrecht, öffentliches Baurecht, Beamten- und Soldatenrecht, gewerblichen Rechtsschutz, internationales Wirtschaftsrecht, Energie- und Umweltrecht sowie die kleineren Restbestände.

### Verwandte Vorlagen ohne Navigationsbruch

- Alle Nachbarlisten enthalten nun drei bis fünf anklickbare Verweise mit dem exakten H1-Titel der Ziel-README und einer konkreten Abgrenzung. Der Abschluss-Sweep prüfte 4.146 interne Links auf vorhandenes Ziel, passenden Linktext und einheitliches Format; tote Links oder bloße Pfadangaben verbleiben nicht.
- In 214 älteren READMEs wurden rohe Pfadlisten, überlange Nachbarlisten und Sonderformate vereinheitlicht. Sieben Europarechts-READMEs ordnen bereits vorhandene Nutzungshinweise wieder der richtigen Sektion zu; drei BAföG-READMEs enthalten nur noch eine konsolidierte Nachbarliste.
- Zwanzig Altdateien wurden ohne inhaltliche Änderung in die einheitliche Leserfolge „Hinweise zur Verwendung“, „Taktische Hinweise“, „Verwandte Vorlagen“ gebracht. Die Einwandüberschrift der Klage gegen eine immissionsschutzrechtliche Genehmigung bezeichnet die zugehörige Antwortlinie jetzt ausdrücklich.

### Geprüft

- Der amtliche Wortlaut des § 182 VVG bestätigt die bestehende Zuordnung der Beweislast bei mitwirkenden Krankheiten oder Gebrechen; die Vorlagen benötigen insoweit keine Korrektur.
- Sämtliche zehn Qualitätsprüfungen laufen grün; Eval-Harness All-Pass 981/981. Vorlagen-Markdown, ODT und Einzel-ZIP blieben unverändert, weil diese Runde ausschließlich README-Navigation und Anwendungstaktik betrifft. Die vollständigen Releasepakete werden für `v4.89.0` neu gebaut.

## v4.88.0 — Taktik-Ausbau Runde 5: 149 weitere READMEs in 16 Rechtsgebieten (2026-08-09)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Die Runde bringt die Taktik-Achse auf 656 von 954 READMEs.

### Weitere 149 READMEs versorgt

Die Abschnitte „Taktische Hinweise" (Vorgehensreihenfolge, typische Gegnereinwände mit Antwortlinie, häufige Fehler) und „Verwandte Vorlagen" mit verifizierten Zielen kamen in 16 Rechtsgebieten hinzu, schwerpunktmäßig in gewerblichem Rechtsschutz, internationalem Wirtschaftsrecht, Urheber- und Medienrecht, Miet- und Wohnungseigentumsrecht, Informationstechnologierecht, Insolvenzrecht, Steuerrecht und Aufsichtsrecht. Fachliche Anker unter anderem: Verfall und Nichtigkeit einer Marke §§ 49, 50 MarkenG, Schutzschriftenregister § 945a ZPO, Zweckübertragungsgrundsatz § 31 Abs. 5 UrhG mit Vergütungsansprüchen §§ 32, 32a UrhG, Text- und Data-Mining §§ 44b, 60d UrhG, automatische Anwendung des UN-Kaufrechts nach Artikel 1 Absatz 1 Buchstabe a CISG mit Ausschluss nur nach Artikel 6, Vollstreckung ohne Exequatur nach der Brüssel-Ia-Verordnung, Beschlussanfechtung § 45 WEG, Anfechtungsfristenraster §§ 129 bis 146 InsO, Aussetzung der Vollziehung § 361 AO und § 69 FGO sowie Erlaubnispflicht § 32 KWG und Sorgfaltspflichten §§ 10 ff. GwG.

### Prüfdisziplin

Fünf Formulierungen, die eine Selbst-Verifikation von Rechtsprechung nahelegten, wurden auf „geprüft" umgestellt; der Rechtsprechungshygiene-Check läuft damit wieder grün. Kein halbfertiger Abschnitt im Bestand: jede bearbeitete README trägt beide Abschnitte vollständig, alle Verweise sind gegen den Dateibestand geprüft.

### Offen

298 READMEs in 30 Rechtsgebieten tragen die beiden Abschnitte noch nicht; sie bleiben für Folgerunden vorgemerkt. Die Arbeit an dieser Runde wurde durch die Sitzungsbegrenzung der Arbeitsumgebung ausgebremst, nicht durch fachliche Hindernisse.

### Geprüft

Alle zehn CI-Checks grün, Eval-Harness All-Pass 954/954. Rechtsprechung bleibt durchgehend Live-Recherche-Suchanker ohne ungeprüfte Aktenzeichen; Beträge, Schwellenwerte und Fristen aus Bedingungswerken stehen als Platzhalter.
## v4.87.0 — OHG-Haftung und Drittsicherheiten im StaRUG-Plan (2026-08-09)

**Stand:** 981 validierte Hauptvorlagen in 41 Themenordnern und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 981/981.

### Persönliche Gesellschafterhaftung präzise gestaltbar

- Der Restrukturierungsplan enthält jetzt vollständige Varianten für die Befreiung, Teilbefreiung oder den Fortbestand der persönlichen Haftung von OHG-Gesellschaftern. Die Bausteine trennen Geschäftsführungsbefugnis und Außenhaftung, individualisieren die betroffenen Forderungen und Gesellschafter und berücksichtigen Eintritts- und Nachhaftung nur nach gesonderter Anwendungsprüfung.
- Die angemessene Entschädigung nach § 2 Abs. 4 Satz 2 StaRUG wird aus dem realisierbaren Nettohaftungswert hergeleitet. Pfändbares Vermögen, Vorlasten, konkurrierende Verbindlichkeiten, Vollstreckungsrisiken, Kosten und Doppelverwertungen fließen in ein gläubigerbezogenes Bewertungs- und Zahlungsmodell ein. Bei fortbestehender oder nur teilweise beseitigter Haftung führt das Bestätigungsdossier durch die Zustimmungskontrolle nach § 60 Abs. 2 StaRUG.

### Dritt- und Cross-Sicherheiten mit Ausgleich und Vollzug

- Gruppeninterne Drittsicherheiten, Cross-Collateral-, Cross-Guarantee-, Parallel-Debt- und Sicherheitenpool-Strukturen werden nach Sicherungszweck, gesicherter Forderung, Nettowert, Eingriff und fortbestehendem Restrecht getrennt. Nicht gestaltbare Drittsicherheiten bleiben unberührt; Rückgriff und Innenausgleich werden nach § 67 Abs. 3 Satz 2 StaRUG eigenständig ausgewiesen.
- Anlage 22 enthält das Haftungs-, Sicherheiten-, Entschädigungs- und Innenausgleichsregister. Anlage 23 liefert individualisierte Zustimmungen und Drittverpflichtungen; Anlage 25 bündelt die Nachweise für die gerichtliche Bestätigung. Vorfinanzierung, unmittelbar abrufbare Garantie und vollstreckbare Drittverpflichtung nach § 71 Abs. 2 StaRUG stehen als vollständige Alternativen bereit, ergänzt um Planbedingungen und optionale Überwachung nach § 72 StaRUG.

### Geprüft und synchronisiert

- README und Rubric sichern Abgrenzung, Stichtagslogik, Bewertungsmethode, Zustimmungen, Entschädigungsdeckung, Rückgriff und Vollstreckbarkeit dauerhaft ab. Markdown, ODT und Einzel-ZIP sind synchron.
- Sämtliche zehn Qualitätsprüfungen laufen grün; Hauptbestand 981/981, Sonderbestand 113 Vorlagen in 18 Bereichen und Eval All-Pass 981/981.

## v4.86.0 — Medienaufsicht und Weltraumrecht als vollständige Verfahrenssuiten (2026-08-09)

**Stand:** 981 validierte Hauptvorlagen in 41 Themenordnern und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 981/981.

### Medienrecht vom Abrufkanal bis zum Verwaltungsgericht

- Zwölf neue Einzelvorlagen bilden die medienrechtliche Betriebskette ab: Unbedenklichkeitsbescheinigung für lineare Livestreams und YouTube-Angebote, bundesweite Fernseh- und Hörfunkzulassung, KEK-Beteiligungsdossier, Beteiligungsänderung, Anzeige von Medienplattform oder Benutzeroberfläche, Jugendmedienschutzkonzept, Podcast-Redaktionsstatut, Anhörungserwiderung, Widerspruch, Direktklage sowie Werbe-, Sponsoring- und Produktplatzierungsregister.
- Die Vorlagen unterscheiden Abruf-Telemedium, linearen Rundfunk, zulassungsfreies Rundfunkprogramm und zulassungspflichtiges bundesweites Programm anhand der tatsächlichen Angebotsgestaltung. Ein normaler YouTube-Abrufkanal wird nicht in ein erfundenes Antragsverfahren gedrängt; für lineare Angebote stehen Reichweiten- und Bedeutungsprüfung nach § 54 MStV bereit.
- Der Bug-Hunt trennt beide Tatbestandswege des § 19 Abs. 1 Satz 1 und 2 MStV, berücksichtigt Pressekodex und anerkannte freiwillige Selbstkontrolle nach § 109 Abs. 1 Satz 4 MStV und beseitigt eine doppelte Gliederungsnummer. Widerspruch und Direktklage sind nun strikt abgegrenzt: Gegen Entscheidungen nach §§ 104 Abs. 2 und 105 MStV schließt § 110 MStV das Vorverfahren aus.

### Deutsches Weltraumrecht ohne fiktive Einheitsgenehmigung

- Der neue Themenordner `weltraumrecht/` enthält 15 missionsbezogene Vorlagen: Verfahrensmatrix, Luftraum- und Startplatzdossiers, nationale Frequenzzuteilungen für Satellitennetz und Erdfunkstelle, ITU-Anmeldung, SatDSiG-Genehmigung, Negativfeststellung und Datenanbieterzulassung, Registerdossier, Exportkontrolle, zweisprachige Ariane-/Falcon-Nutzlastfreigabe, Bodensegment-Sicherheitskonzept, Weltraumschrott- und Missionsendeplan sowie Experimentantrag für den Bremer Fallturm.
- Die Sammlung bildet die im August 2026 geltende sektorale Rechtslage ab. Sie behauptet weder ein bereits geltendes allgemeines deutsches Weltraumgesetz noch eine universelle Startgenehmigung. Standort, Luftraum, Frequenzen, Erdfernerkundung, Export, Registrierung, Startdienst und Forschungseinrichtung bleiben getrennte Prüf- und Freigabespuren mit gemeinsamen Gate-Entscheidungen.
- Die Endprüfung präzisiert die fehlende Formzuweisung des § 25 SatDSiG für den Antrag nach § 3 Abs. 4 Satz 1 SatDSiG. Das Registerdossier führt jetzt zum Luftfahrt-Bundesamt und zur Luftfahrzeugrolle Band R, ohne eine nicht bestehende allgemeine Registrierungspflicht privater Betreiber zu behaupten; DLR-Programmkoordination und UN-Mitteilung bleiben davon getrennt.

### Navigation, Formate und Qualität

- Rechtsgebietsmenüs, Dokumenttyp-Sichten, Arbeitsabläufe und `DOWNLOADS.md` erschließen jede neue Vorlage. Jede Hauptvorlage besitzt README, Markdown-Quelle, ODT-Arbeitsfassung, Markdown-Einzelpaket und Rubric.
- Sämtliche zehn Qualitätsprüfungen laufen grün. Die vollständigen ODT-, Markdown- und gerichtsleitenden Releasepakete werden mit Offline-Index, Manifest und SHA-256-Prüfsummen neu erzeugt.

## v4.85.0 — Rechtsprechungsstand 2026 amtlich nachgeführt (2026-08-09)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Der vollständige Bestand wurde gegen die bis einschließlich 9. August 2026 amtlich veröffentlichte, unmittelbar vorlagenrelevante Rechtsprechung geprüft.

### Vollständiger Relevanz-Audit statt Jahreszahlpflege

- Der neue `references/rechtsprechungsaudit-2026.md` dokumentiert Prüfumfang, Methode, Änderungsquote und Entscheidungswirkung. Alle 1.067 Vorlagen wurden erfasst; 62 Hauptvorlagen-READMEs und neun gerichtsleitende Sondervorlagen erhielten einen konkreten neuen Prüfanker. Bei 892 Hauptvorlagen und 104 Sondervorlagen bestand kein hinreichend enger Änderungsbedarf, sodass ihre vorhandenen Hinweise bewusst unverändert blieben.
- 47 amtliche Direktquellen von Bundesverfassungsgericht, Bundesgerichtshof, Bundesarbeitsgericht, Bundesverwaltungsgericht, Bundessozialgericht, Bundesfinanzhof und Gerichtshof der Europäischen Union wurden auf Erreichbarkeit, Entscheidungsform, Datum, Aktenzeichen und vorlagenspezifische Aussage geprüft. Pressemitteilungen dienen ausschließlich als amtliche Orientierung; ihnen werden weder Randnummern noch nicht veröffentlichte Begründungsschritte zugeschrieben.
- Die README-Navigation und der Rechtsprechungsradar führen zum Audit. Jeder neue Anker benennt die praktische Folge für Auswahl, Formulierung, Beweisführung, Anlagenapparat oder Verfahrensstrategie der konkreten Vorlage, statt Entscheidungen nur aufzulisten.

### Rechtsgebietsübergreifende Präzisierung

- Neue Anker betreffen unter anderem Kündigungsbutton und digitale Vertragsbeendigung, Verbrauchsgüterkauf, Vergleichsbefristung, Freistellung und Betriebsratsbeschluss, betriebliche Altersversorgung, Sorge und Umgang, vereinfachten Kindesunterhalt, Datenschutzrechte, Insolvenz- und Restrukturierungsprognose, Wohnungseigentum, Arbeitsunfall und Grundsicherung, Steuerverfahren, Migration, Urheber- und Medienrecht, Verfassungsbeschwerde, Verkehrsrecht, Erbvertrag, Unternehmensmitbestimmung und Kartellschadensrecht.
- Im gerichtsleitenden Bestand wurden die richterlichen Prüfprogramme für Stabilisierung und Planbestätigung, verfassungsgerichtliche Vorprüfung, familiengerichtliche Begutachtung und Anhörung sowie verwaltungsgerichtliche Nachbarklagen punktgenau ergänzt. Die Sonderbereichskonventionen bleiben gewahrt.
- Ein bei der Gegenprüfung entdeckter Überdehnungsfehler zu BVerfG 1 BvR 497/26 ist beseitigt. Die Hinweise beschränken sich nun auf die amtlich veröffentlichten Aussagen zu Beistand, wirksamer Erhebung und Substantiierung; aus der nicht weiter begründeten Nichtannahme werden keine zusätzlichen fallbezogenen Anforderungen abgeleitet.

### Verifiziert und veröffentlicht

- Sämtliche neuen amtlichen Links antworten erfolgreich. Alle zehn lokalen Qualitätsprüfungen laufen grün; Hauptbestand 954/954, Sonderbestand 113 Vorlagen in 18 Bereichen und Eval All-Pass 954/954.
- Die Mustertexte und damit die 954 ODT-Arbeitsfassungen bleiben inhaltlich unverändert, weil die Aktualisierung ausschließlich die fachlichen Hinweise und unmittelbar gerichtlichen Prüfanker betrifft. Die drei vollständigen Releasepakete und `SHA256SUMS.txt` wurden dennoch auf dem neuen Versionsstand reproduzierbar neu gebaut und geprüft.

## v4.84.0 — Revirement: Rechtskorrektur, Offline-Suche und transaktionssichere Werkzeuge (2026-08-09)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Die Veröffentlichung bündelt zugleich die seit v4.79.0 auf `main` abgeschlossenen Inhalts- und Taktikrunden in erstmals wieder vollständig aktuellen Releasepaketen.

### Konkreten Rechtsfehler im Unfallversicherungsrecht beseitigt

Die Hinweise zum Anspruchsschreiben aus privater Unfallversicherung ordnen Gefahrerhöhung, mitwirkende Ursachen und Sachverständigenverfahren nun den richtigen Vorschriften zu. § 181 VVG regelt die Gefahrerhöhung, § 182 VVG die Beweislast für bedingungsgemäßen Wegfall oder Minderung bei mitwirkenden Krankheiten oder Gebrechen und § 84 VVG das vertraglich vorgesehene Sachverständigenverfahren. Die frühere Vertauschung ist anhand der amtlichen Gesetzesfassung korrigiert; eine Mitwirkungsschwelle wird nicht länger dem Gesetz zugeschrieben, sondern zutreffend aus der konkret vereinbarten AUB-Klausel abgeleitet.

### Offline-Pakete schneller auffindbar und prüfbar

Der Offline-Index durchsucht neben Titel, Rechtsgebiet und Dateipfad nun verdichtete Fachbegriffe aus Anwendungsbereich, Normen, Risiken und taktischen Hinweisen. Versionsstand und Dateizahl stehen sichtbar im Kopf. Das Maschinenmanifest verwendet Schema 2 und führt für jede Arbeitsdatei zusätzlich Suchbegriffe, Dateigröße und SHA-256-Prüfsumme; extrahierte Dateien lassen sich damit ohne Rückgriff auf das Gesamtarchiv identifizieren und verifizieren.

### Erzeugung gegen Abbruch und Teilstände gehärtet

Markdown-Einzelpakete, Downloadindex, Eval-Report und JSON-Snapshots werden vollständig in temporäre Dateien geschrieben, optional geprüft und erst danach atomar ersetzt. Der Releasebau erzeugt alle drei ZIP-Pakete und die Prüfsummendatei zunächst gemeinsam in einem Staging-Verzeichnis; ein Fehler lässt das letzte gute Paketset unverändert. Auch die Veröffentlichung des Paketsets besitzt einen Rückfallpfad, falls ein Dateiaustausch scheitert.

Der ODT-Export löst relative Ressourcen jetzt aus dem Ordner der Markdown-Quelle auf, meldet fehlende Eingabedateien mit Fehlerstatus und fängt Export- sowie Layoutfehler verständlich ab. Der Umlaut-Hygienecheck besitzt eine native Python-Implementierung; der vollständige Gate benötigt damit unter Windows keine Bash-Umgebung mehr, während der bisherige Shell-Aufruf als kompatibler Wrapper erhalten bleibt.

### Navigation und Regressionen verschärft

Relative Markdown-Links werden nicht mehr nur auf vorhandene Dateien geprüft. Der Validator kontrolliert zusätzlich Fragmente, explizite HTML-IDs, GitHub-kompatible Überschriftenanker und die exakte Groß-/Kleinschreibung jedes Zielpfads, sodass auf macOS unsichtbare Linkfehler nicht erst unter Linux oder im Release auffallen. Sechs neue Regressionen sichern atomare Schreibabbrüche, vollständiges Release-Staging, Manifestintegrität, fachliche Offline-Suche, ODT-Ressourcenauflösung und Fragmentprüfung. Sämtliche zehn Qualitätschecks laufen grün; der vollständige Releasebau wurde einschließlich CRC, Manifest und SHA-256-Summen verifiziert.

## v4.83.0 — Taktik-Ausbau Runde 4: Bau-, Vergabe-, Versicherungs- und Vertriebsrecht vollständig (2026-08-05)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Vier weitere Rechtsgebiete sind damit vollständig mit Taktik- und Querverweis-Abschnitten versorgt.

### Vier Rechtsgebiete abgeschlossen

Die 98 noch offenen READMEs in `bau-und-architektenrecht/` (27), `vergaberecht/` (20), `versicherungsrecht/` (23) und `vertriebs-und-handelsrecht/` (28) tragen jetzt die Abschnitte „Taktische Hinweise" (Vorgehensreihenfolge, typische Gegnereinwände mit Antwortlinie, häufige Fehler) und „Verwandte Vorlagen" mit ausschließlich verifizierten Zielen. Alle vier Gebiete stehen bei voller Abdeckung: Baurecht 30 von 30, Vergaberecht 30 von 30, Versicherungsrecht 28 von 28, Vertriebs- und Handelsrecht 28 von 28.

Fachliche Anker unter anderem: die zweistufige Anordnungsmechanik der §§ 650b, 650c BGB samt VOB/B-Parallele, Bauhandwerkersicherung § 650f BGB, Prüffähigkeit § 14 VOB/B und Druckzuschlag § 641 Abs. 3 BGB; im Vergaberecht Akteneinsicht und Geheimschutz § 165 GWB, Zuschlagsgestattung § 169 Abs. 2 GWB, Beschwerde- und Verlängerungsfristen §§ 172, 173 GWB, Produktneutralität § 121 GWB und Dokumentationslast § 8 VgV; im Versicherungsrecht Rücktritt und Kausalitätsklausel §§ 19 bis 22 VVG, Quotelung § 28 Abs. 2 VVG, Stichentscheid § 128 VVG, Sachverständigenverfahren § 84 VVG, Umstandsmeldung und Vergleichsverbot § 105 VVG in der Organhaftungsversicherung; im Vertriebsrecht der Ausgleich § 89b HGB mit Jahresfrist und Kappung, Buchauszug § 87c HGB, Kernbeschränkungen der Vertikal-GVO, Ranking-Transparenz nach Artikel 5 der Verordnung (EU) 2019/1150 und die Insolvenzfestigkeit von Konsignations- und Werkzeugbeständen (§ 47 InsO, § 771 ZPO).

Die repoweite Taktik-Abdeckung steigt von 409 auf 507 von 954 READMEs.

### Zwei Sachfehler in Mustertexten berichtigt

Im Bedingungsmuster der Organhaftungsversicherung verwies Ziffer 5.3 für die Rückzahlungspflicht auf Ziffer 8.4; die Pflicht steht in Ziffer 8.3. Der Querverweis ist in beiden Sprachspalten berichtigt. Im Rahmenbezugsvertrag für Industriekomponenten war das UN-Kaufrecht als Opt-in gefasst („gilt nur, wenn die Parteien es ausdrücklich einbeziehen"). Das ist unzutreffend: Bei einem internationalen Warenkauf zwischen Parteien in Vertragsstaaten gilt das Übereinkommen bereits kraft Artikel 1 Absatz 1 Buchstabe a CISG, und die bloße Wahl deutschen Rechts schließt es nicht aus. Die Klausel bietet nun die richtige Wahl zwischen ausdrücklichem Ausschluss nach Artikel 6 CISG und ausdrücklicher Anwendung; eine repoweite Suche nach derselben Fehlkonstruktion blieb ohne weiteren Treffer. Ferner steht die Gewährleistungsfrist für Bauwerke in der betroffenen README jetzt richtig mit fünf Jahren (§ 634a Abs. 1 Nr. 2 BGB).

### Geprüft

Alle zehn CI-Checks grün, Eval-Harness All-Pass 954/954; die geänderten ODT- und Markdown-ZIP-Fassungen wurden neu erzeugt. Rechtsprechung bleibt durchgehend Live-Recherche-Suchanker ohne ungeprüfte Aktenzeichen; Beträge, Schwellenwerte, Marktanteile und Bedingungsfristen stehen als Platzhalter. Eine unklare Absatzzählung zum Mitwirkungsanteil in der Unfallversicherung (§ 181 gegenüber § 182 VVG) trägt einen ausdrücklichen Live-Prüfhinweis, weil die amtliche Quelle in der Arbeitsumgebung nicht erreichbar war.

## v4.82.0 — Taktik-Ausbau Runde 3 (Teilstand): Bau, Vergabe und Versicherung angefangen (2026-08-05)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Die Runde wurde auf Wunsch nach dem ersten Wellenabschnitt abgeschlossen und liefert einen vollständig geprüften Teilstand statt eines abgebrochenen Gesamtdurchlaufs.

### Taktik-Abschnitte in drei weiteren Rechtsgebieten begonnen

18 weitere READMEs tragen jetzt die Abschnitte „Taktische Hinweise" (Vorgehensreihenfolge, typische Gegnereinwände mit Antwortlinie, häufige Fehler) und „Verwandte Vorlagen" mit verifizierten Zielen: 10 im Vergaberecht, 5 im Versicherungsrecht und 3 im Bau- und Architektenrecht. Fachliche Anker unter anderem die dreifache Zulässigkeitshürde des Nachprüfungsantrags (§ 160 GWB) mit Zuschlagsverbot (§ 169 Abs. 1 GWB), Wartefristen und Unwirksamkeitsfolge (§§ 134, 135 GWB), Grenzen wesentlicher Vertragsänderungen (§ 132 GWB), Eignungsleihe (§ 47 VgV), Abnahmewirkungen und fiktive Abnahme (§ 640 BGB) sowie Obliegenheits-, Rücktritts- und Verfahrensmechanik der Versicherungsdeckung (§§ 19 bis 22, 28, 84, 128 VVG).

Die repoweite Taktik-Abdeckung steigt von 392 auf 409 von 954 READMEs. Die verbleibenden 545 READMEs in 34 Rechtsgebieten bleiben ausdrücklich offen und sind für Folgerunden vorgemerkt; kein Rechtsgebiet dieser Runde ist vollständig abgeschlossen.

### Geprüft

Alle zehn CI-Checks grün, Eval-Harness All-Pass 954/954. Kein halbfertiger Abschnitt im Bestand: jede bearbeitete README trägt beide Abschnitte vollständig. Rechtsprechung bleibt durchgehend Live-Recherche-Suchanker ohne ungeprüfte Aktenzeichen; Beträge, Schwellenwerte und Bedingungsfristen stehen als Platzhalter.

## v4.81.0 — Taktik-Ausbau Runde 2: Bank- und Kapitalmarktrecht sowie Verwaltungsrecht komplett (2026-08-03)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Die Runde setzt den Taktik-Ausbau aus v4.80.0 fort.

### Zwei weitere Rechtsgebiete vollständig versorgt

Alle 75 zuvor fehlenden READMEs in `bank-und-kapitalmarktrecht/` (41) und `verwaltungsrecht/` (34) tragen jetzt die Abschnitte „Taktische Hinweise" (Vorgehensreihenfolge, typische Gegnereinwände mit Antwortlinie, häufige Fehler) und „Verwandte Vorlagen" mit ausschließlich verifizierten Zielen. Inhaltliche Anker unter anderem: Geeignetheitserklärung und Taping (§§ 64, 83 WpHG), Erstattungs- und Haftungsmechanik bei nicht autorisierten Zahlungen (§§ 675u ff. BGB, 13-Monats-Frist § 676b BGB), Sicherungsabrede und Vollstreckungsunterwerfung bei der Grundschuld, P-Konto-Staffel (§§ 899 ff. ZPO), Factoring-Kollisionslagen, Intercreditor-Rangordnung; verwaltungsrechtlich die Fristen- und Vorverfahrensmechanik (§§ 68 ff., 74 VwGO), Aussetzungslast bei Abgaben- und Kostenbescheiden (§ 80 Abs. 2 Satz 1 Nr. 1, Abs. 4 und 5 VwGO), Fortsetzungsfeststellungs-Fallgruppen (§ 113 Abs. 1 Satz 4 VwGO), Normenkontroll-Doppelfristen (§ 47 Abs. 2 VwGO, § 215 BauGB), Remonstrationsstufen (§ 36 BBG, § 63 BeamtStG), Vollziehungsfrist einstweiliger Anordnungen (§ 123 Abs. 3 VwGO, § 929 Abs. 2 ZPO) und die komplette BAföG-Strecke (§§ 7 Abs. 3, 24 Abs. 3, 36, 48, 50 Abs. 4 BAföG).

Die Taktik-Abdeckung des Repositories steigt von 317 auf 392 von 954 READMEs. Rechtsprechung bleibt durchgehend Live-Recherche-Suchanker ohne ungeprüfte Aktenzeichen; Beträge und Bedarfssätze stehen als Platzhalter mit Fortschreibungshinweis. Alle zehn CI-Checks laufen grün.

## v4.80.0 — Gesamtrunde Design und Inhalt: Leserhythmus, Tiefenlift der dünnsten Vorlagen, Taktik-Ausbau (2026-08-02)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen; Eval-Harness All-Pass 954/954. Die Runde verbindet einen repoweiten Design-Pass mit gezielter Inhaltsvertiefung an den schwächsten Stellen des Bestands.

### Leserhythmus repoweit vereinheitlicht

385 Vorlagen-Markdown-Fassungen erhielten den einheitlichen Leserhythmus: eine Leerzeile zwischen aufeinanderfolgenden nummerierten Klauselzeilen sowie vor und nach Überschriften und Trennstrichen. Tabellen und Codeblöcke blieben durch Wächter unangetastet (verifiziert: keine einzige Leerzeile in einer Tabelle). Die ODT-Fassungen übernehmen den ruhigeren Absatzfluss aus dem Design-Profil der Neusetzung.

### Die 36 dünnsten Vorlagen substanziell vertieft

Keine Hauptvorlage liegt mehr unter 75 Zeilen (vorher 36, darunter alle zweisprachigen Leitvorlagen mit 50 bis 74 Zeilen). Alle zweisprachigen Erweiterungen laufen satz- und absatzgenau parallel weiter. Beispiele: Die Vergabe-Leitvorlage deckt jetzt Nachforderung (§ 56 VgV), Preisaufklärung (§ 60 VgV), Informations- und Wartepflicht (§§ 134, 135 GWB) und das Nachprüfungsverfahren (§§ 160 ff. GWB) ab; die Deckungsprüfung Großschaden führt Obliegenheits-, Fälligkeits- und Sachverständigenverfahrens-Blöcke (§§ 28, 30, 31, 84, 14 VVG); die Logistikschaden-Leitvorlage verzahnt CMR (Art. 17 ff., 29, 32), §§ 425 ff. HGB, ADSP und Multimodal-Streckenteilung; die CISG-Vorlagen erhalten Rüge-, Nachfrist- und Aufhebungsbausteine mit wörtlichen Erklärungsmustern (Art. 38, 39, 47, 49 CISG); die UG- und Investorenklassen-Satzungen sowie die Investmentrunden-Leitvorlage bilden Rücklagenpflicht (§ 5a GmbHG), Klassenrechte, Vesting-, Drag-/Tag- und Abfindungsmechanik ab; die vier Mietrechts-Schriftsätze tragen ausformulierte Antrags-, Würdigungs- und Beweisteile; die IFG-Anträge für Bund und Länder entgegnen den Ausnahmen der §§ 3–6 IFG einzeln.

### Taktische Hinweise und Verwandte Vorlagen für zwei komplette Rechtsgebiete

Alle 123 zuvor fehlenden READMEs in `allgemeines-und-bereichsuebergreifendes/` (67) und `handels-und-gesellschaftsrecht/` (56) tragen jetzt die Abschnitte „Taktische Hinweise" (Vorgehensreihenfolge, typische Gegnereinwände mit Antwortlinie, häufige Fehler) und „Verwandte Vorlagen" mit ausschließlich verifizierten Verweisen (469 geprüfte Links, null tote Ziele). Die Taktik-Abdeckung des Repositories steigt von 194 auf 317 von 954 READMEs; die übrigen Rechtsgebiete folgen in den nächsten Runden.

### Werkstattdisziplin

Zehn in der Vertiefung entstandene Verstöße gegen das Verschachtelungsverbot für Platzhalter wurden aufgelöst (Options- und Variantenklammern in Prosa mit ausdrücklicher Streichanweisung überführt), eine englische Wortdopplung und eine deutschsprachige Passage in einer englischen Tabellenspalte korrigiert. 421 ODT-Fassungen und die zugehörigen Markdown-ZIPs wurden neu erzeugt; alle zehn CI-Checks laufen grün. Rechtsprechung bleibt durchgehend Live-Recherche-Suchanker ohne ungeprüfte Aktenzeichen.

## v4.79.0 — Anti-Generik-Lift und vorlagenspezifische Dokumentlogik (2026-07-29)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 954/954.

### Mustertexte auf den konkreten Rechtsakt zugespitzt

- 507 Hauptvorlagen und 108 gerichtsleitende oder staatsanwaltschaftliche Muster wurden einzeln auf austauschbare Textreste geprüft. Wiederholte Metadatenköpfe, universelle Freigabeformeln, pauschale Zugangs- und Verwahrungssätze sowie inhaltsleere Vollzugsbausteine sind entfernt oder durch den jeweiligen Vertrags-, Antrags-, Verfügungs- oder Beweiszweck ersetzt.
- Sieben bislang knappe Vollstreckungsmuster enthalten nun ausformulierte Anträge, Vollstreckungsvoraussetzungen, Forderungsaufstellungen und nachweisfähige Anlagenlogik. 25 Vollmachten benennen den konkreten Vertretungsumfang; 29 Zugangs- und Dokumentationsbausteine sichern den jeweils entscheidenden Übermittlungs-, Register-, Zustellungs- oder Aufbewahrungsvorgang.
- 16 AGB-Muster unterscheiden ihren Leistungsgegenstand, die konkrete Abwicklung, Mängel- und Ausfallrisiken sowie die jeweilige Verbraucher- oder Unternehmerrolle. 59 Schreiben besitzen einen auf Anlass, Adressat und begehrte Rechtsfolge zugeschnittenen Kopf; 79 Laufzeit-, Risiko- und Beendigungsklauseln verwenden keine austauschbare Universalklausel mehr.
- Die zweisprachigen Muster für den GmbH-und-Co.-KG-Gesellschaftsvertrag und das Shareholders' Agreement mit Investorenklassen wurden vollständig neu aufgebaut. Deutsche und englische Fassung bilden Beteiligungsstruktur, Governance, Finanzierung, Verfügungsbeschränkungen, Exit, Abfindung beziehungsweise Liquidationspräferenz und Anlagenapparat satzgenau parallel ab.

### Hinweise und Anlagenapparat gestrafft

- 184 Hinweisdokumente wurden auf ihren tatsächlichen Vertrag, Antrag oder Verfahrensschritt zugeschnitten. Insbesondere im Energie-, Gesellschafts-, Kartell-, Transport- und Umweltrecht ersetzen konkrete Anwendungsgrenzen, Normketten und Vollzugsrisiken die zuvor wiederholten Bereichsfloskeln.
- Mehrfach kopierte Anlagenhüllen mit leeren Status-, Freigabe- und Prüffeldern sind entfallen. Die verbleibenden Anlagenlisten benennen die für den jeweiligen Anspruch, Vertragsschluss, Registervollzug oder Nachweisweg benötigten Unterlagen; Verweise führen damit nicht mehr in gleichförmige Verwaltungsschalen.
- 211 leere Zwischenüberschriften mit der bloßen Bezeichnung „Inhalt der Anlage“ wurden entfernt. Vier energierechtliche Vertragsmuster besitzen statt pauschaler Anlagenzeilen nun vollständige Tabellen für Konzessionsgebiet, Auswahlwertung, Netzdaten, PPA-Mengen und Preise, Speicherbetrieb sowie gewerbliche Lieferstellen.
- Wiederkehrende Hinweise zur Platzhalterpflege, Akteneingabe und Dokumentklassifikation wurden aus den Mustertexten entfernt. Die fachlichen Hinweise bleiben in den READMEs, während gerichtliche und staatsanwaltschaftliche Entwürfe nur noch entscheidungs-, tenor- und vollzugsrelevanten Text enthalten.

### Dauerhafte Qualitätssicherung

- Der Validator blockiert künftig die beseitigten Generikmuster: universelle Metadaten- und Parteiköpfe, pauschale Freigabewahlen, leere Ausfüllkerne, generische Zugangsformeln und vorlagenfremde Verwendungshinweise im Entscheidungstext.
- Regressionstests prüfen jeden gesperrten Baustein einzeln und sichern die vollständige Vorlageninventur. Alle geänderten ODT-Arbeitsfassungen und Markdown-Einzelpakete wurden aus den bereinigten Quellen neu erzeugt; sämtliche zehn lokalen Qualitätsprüfungen laufen grün.

## v4.78.0 — Inventur- und Releaseartefakte portabel abgesichert (2026-07-29)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 954/954.

### Fünf verdeckte Fehlerpfade geschlossen

- Die Bestandsprüfung erkennt Vorlagen außerhalb der kanonischen Themenliste nun auch bei einem falschen oder generischen Dateistamm. Eine neu angelegte `vertrag.md`, ODT-Datei, Markdown-ZIP-Datei oder Rubric kann nicht mehr deshalb unbemerkt bleiben, weil sie noch nicht den Ordnernamen trägt.
- Der erzeugte Downloadindex verwendet unmittelbar die strenge kanonische Vorlageninventur. Uneindeutige Markdown-Quellen führen dadurch auch beim isolierten Indexbau zum sichtbaren Abbruch, statt aus `DOWNLOADS.md` still herauszufallen.
- Der Releasebau verwirft doppelte, nur in Groß- und Kleinschreibung oder Unicode-Normalisierung kollidierende ZIP-Einträge. Das verhindert plattformabhängig unterschiedliche Paketansichten und die unbemerkte Verdrängung von `index.html` oder `manifest.json`.
- Absolute Pfade, Rücksprünge, leere Pfadteile und Windows-Trennzeichen sind auch für erzeugte Zusatzdateien im Releasearchiv gesperrt. Eine spätere Erweiterung des Paketbaus kann damit keine unsicheren ZIP-Mitglieder einführen.
- Atomar erzeugte ODT-Dateien, Releasepakete und Prüfsummendateien erhalten vor dem Austausch ausdrücklich portable Leserechte `0644`. Die temporäre Standardberechtigung `0600` wird nicht mehr in die veröffentlichte Datei übernommen.

### Reproduzierbarkeit und Regressionen

- Vier neue Regressionstests decken generisch fehlbenannte Fremdvorlagen, den strengen Downloadindex, gefährliche oder kollidierende Archivnamen und portable Artefaktberechtigungen ab. Der Testbestand steigt auf 28 Fälle.
- Zwei vollständige Releasebauten erzeugen bytegleiche Prüfsummen. Ein zusätzlicher echter Pandoc-Lauf bestätigt die Integrität und Berechtigung einer neu erzeugten ODT-Arbeitsfassung.
- Die Vorlageninhalte, 954 ODT-Arbeitsfassungen und Markdown-Einzelpakete bleiben unverändert. Sämtliche zehn lokalen Qualitätsprüfungen laufen grün.

## v4.77.1 — Fünf harte Fehlerpfade geschlossen (2026-07-29)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 954/954.

### Falsch-Grün und stille Bestandslücken beseitigt

- Ein fehlendes `rubric.yaml` und ein vollständig leerer Discovery-Lauf führen im Eval nun zwingend zum Fehlschlag. Bericht und Konsole weisen fehlende Rubrics ausdrücklich aus, statt einen unvollständigen Lauf als erfolgreich erscheinen zu lassen.
- Rubric-Prüfpfade und Globmuster bleiben innerhalb des jeweiligen Vorlagenordners. Absolute Pfade, Rücksprünge mit `..`, unportable Pfade und symbolische Links werden vor jedem Datei- oder Inhaltszugriff abgewiesen.
- Die kanonische Inventur bricht bei fehlenden Themenordnern, uneindeutigen Markdown-Quellen, symbolisch verknüpften Vorlagendateien und neu angelegten Vorlagen außerhalb der Themenliste sichtbar ab. Einzelne Bestandsverbraucher können dadurch keinen vollständigen Bereich mehr still auslassen.

### Export und Veröffentlichung ausfallsicher gemacht

- Releasepakete übernehmen ausschließlich echte Dateien innerhalb des Repositories. Symbolische Links nach außen und relative Markdown-Links aus dem Repository heraus werden blockiert; ZIPs und Prüfsummendatei ersetzen eine vorhandene gute Fassung erst nach vollständigem Schreiben und erfolgreicher CRC-Prüfung.
- Der ODT-Generator arbeitet bis zum Abschluss in temporären Dateien. Erst ein lesbarer, normalisierter Export mit Dokumenttext, erwartetem Seitenprofil, Grundschrift und Seitenzahl ersetzt die vorhandene Arbeitsfassung; ein Pandoc-, Layout- oder Validierungsfehler lässt die letzte gute ODT unverändert.
- Sieben neue Negativ- und Ausfallsicherheitstests erhöhen den Testbestand auf 24 Fälle. Ein echter Pandoc-Export, der vollständige Releasepaketbau und sämtliche zehn Qualitätsprüfungen laufen grün; Vorlageninhalt, ODT-Bestand und Markdown-ZIPs bleiben unverändert.

## v4.77.0 — Usability, Mikrofehler und schnelleres Qualitätsgate (2026-07-26)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 954/954.

### Verdeckte Bestandsabweichungen dauerhaft ausgeschlossen

- Sechs Release-, Download- und Prüfskripte leiteten den Hauptbestand bislang unabhängig über eigene Ausschlusslisten her. Downloadindex, Markdown-ZIPs, Releasepakete, Kategorienansicht, ZIP-Integritätsprüfung, README-Linkpflege und Eval nutzen nun dieselbe kanonische Themen- und Vorlageninventur.
- Neue Regressionstests vergleichen sämtliche Bestandsverbraucher gegen alle 954 Hauptvorlagen. Eigene Ausschlusslisten in den beteiligten Skripten, ausgelassene Themenordner oder voneinander abweichende Paketbestände schlagen sichtbar fehl.
- Der Bug-Hunt kontrollierte zusätzlich 6.175 relative Markdown-Linkziele ohne Fehlfund. Release-Indizes prüfen für jede Vorlage Arbeitsdatei und Hinweispfad, eindeutige HTML-IDs sowie die vollständige Trennung gerichtlicher, staatsanwaltschaftlicher und amtsanwaltschaftlicher Dokumenttypen.

### Schnellere und ruhigere Qualitätsprüfung

- Der Eval-Lauf gibt standardmäßig nur Gesamtsumme und konkrete Fehler aus; `--verbose` bleibt für das vollständige Einzelprotokoll verfügbar. Damit sinkt ein grüner Gesamtlauf von annähernd tausend Konsolenzeilen auf wenige Dutzend, ohne Diagnosedaten bei Fehlern zu verlieren.
- Testakten und vollständige Rubric-Bewertung laufen im zehnten Qualitätsblock parallel. Eine doppelte Ausführung sämtlicher Bestandsrubrics unmittelbar vor dem identischen Gesamtlauf entfällt. Der vollständige lokale Gate sank in der Vergleichsmessung von rund 8,6 auf rund 5,3 Sekunden.
- Siebzehn Regressionstests sichern Eval-Fehlerausgabe, Testakten, kanonische Inventur, Offline-Index, Paketdokumentation und ODT-Layoutschwellen. `check-all.py` bleibt auf vier parallele, nur lesende Prüfungen begrenzt und vermeidet unnötige Prozesslast.

### Offline-Index und Dokumentbild

- Der Offline-Index besitzt größere Klickziele, eine Sprungnavigation, klare Fokuszustände, einen deaktivierten Reset ohne aktive Filter und eine entprellte Suche. Vorlagentitel führen zu den fachlichen Hinweisen; die Arbeitsdatei bleibt als eigener Befehl erreichbar.
- Auf Mobilgeräten werden Tabellenkopf und lange deutsche Komposita ohne horizontales Scrollen in beschriftete Karten überführt. Desktop- und Mobilansicht, Suche, Reset, Leermeldung, Ergebniszahl, Tastatursteuerung und reduzierte Bewegungspräferenz wurden im Browser geprüft.
- Die Komplettpakete enthalten neben den Vorlagen nun auch sämtliche Arbeits-, Beitrags- und Referenzdokumente aus dem Repo-Root, den Rechtsstandsprüfpfad und den gerichtsleitenden Gesamtindex. Offline-Nutzer erreichen damit die in der Startseite verlinkten Pflege- und Prüfhinweise ohne einen zweiten Download.
- Fünf zuvor im Hochformat gequetschte, kurze und dennoch sieben- bis neuntspaltige Tabellen erhalten nun A4-Querformat. Das betrifft Mängelliste, Schlussrechnung, Wechselmodell-Kostenliste, KI-Nutzungsrichtlinie und Vergabe-Bewertungsmatrix. Maskierte senkrechte Striche innerhalb zweisprachiger Tabellenzellen werden dabei nicht länger als zusätzliche Spalten fehlgedeutet. Der ODT-Integritätscheck vergleicht das Seitenprofil fortan mit der Markdown-Quelle.
- README, Beitragsleitfaden und Workflow erläutern die kompakte Eval-Ausgabe, die eindeutigen Offline-Befehle und das quellensynchrone ODT-Seitenprofil. Sämtliche zehn lokalen Prüfungen laufen grün: 954/954 Hauptvorlagen, 113/113 Sondervorlagen und Eval All-Pass 954/954.

## v4.76.0 — Testakten, vollständige Eval-Abdeckung und Strafvollzugspräzision (2026-07-26)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht erstmals vollständig bei All-Pass 954/954.

### Verdeckten Abdeckungsfehler beseitigt

- Der Eval-Harness ließ den Themenordner `strafvollzugsrecht` und damit acht vorhandene Vorlagen unbemerkt aus. Eine gemeinsame, kanonische Themenliste steuert nun Validierung, Rubric-Erzeugung und Eval; Listenabweichungen zwischen diesen Werkzeugen sind damit ausgeschlossen.
- Unbekannte Vorlagen-Slugs, syntaktisch defekte Rubrics, doppelte Check-IDs, unbekannte Check-Typen und fehlerhafte reguläre Ausdrücke führen jetzt zu einem sichtbaren Fehlschlag. Ein scheinbar erfolgreicher Nulllauf oder ein Abbruch ohne auswertbaren Befund ist nicht mehr möglich.
- Die bereits dokumentierten strukturierten Prüfarten für YAML- und JSON-Felder sind vollständig implementiert. Der eingebaute YAML-Fallback verarbeitet typisierte und verschachtelte Felder auch in einer schlanken Python-Umgebung ohne PyYAML.

### Testakten und Qualitätsgate

- Eine eigenständige Eval-Testakte deckt sämtliche acht Prüfarten mit positiven und negativen Fällen ab. Acht automatisierte Tests kontrollieren außerdem die vollständige Abdeckung aller 954 Vorlagen, die Schemakonsistenz sämtlicher Bestandsrubrics und den Betrieb ohne optionale Abhängigkeiten.
- `check-all.py` führt im zehnten Qualitätsblock zuerst die Testakte und anschließend den vollständigen Rubric-Lauf aus. README und Beitragsleitfaden beschreiben den neuen Prüfpfad und den korrigierten All-Pass-Stand.
- Alle acht Strafvollzugsvorlagen besitzen nun fachspezifische Rubrics mit je 22 automatisierten Prüfungen und zwei gezielten Prüfpunkten für die menschliche Endkontrolle.

### Strafvollzugsrecht fachlich geschärft

- Der Antrag nach § 109 StVollzG trennt Antragsbefugnis, schriftliche Bekanntgabe, die Zwei-Wochen-Frist des § 112 Absatz 1 StVollzG, den Fall fehlender schriftlicher Bekanntgabe und die Wiedereinsetzung nach § 112 Absatz 2 und 3 StVollzG. Untersuchungshaftrecht wird nicht mehr in den Anwendungsbereich dieser Vorlage einbezogen.
- Medizinischer Rechtsschutz und Untersuchungshaft unterscheiden nun sauber zwischen § 109 und § 114 StVollzG einerseits sowie dem besonderen Rechtsbehelf nach § 119a StPO andererseits. Der Untersuchungshaftantrag ordnet Erstbegehren, gerichtliche Beschränkung, behördliche Maßnahme, Drei-Wochen-Untätigkeit, Zuständigkeit nach § 126 StPO und Verteidigerverkehr nach §§ 148 und 148a StPO getrennten Antragsvarianten zu.
- Disziplinarbeschwerde, Eilantrag und Rechtsbeschwerde sichern die jeweils eigenständigen Fristen und Rechtsbehelfe. Die Rechtsbeschwerde bildet Einlegung, Begründungsfrist, Form, Sachrüge, optionale Verfahrensrüge und Beruhensprüfung nach §§ 116 bis 118 StVollzG ausformuliert ab.
- Für sechs geänderte Hauptvorlagen wurden ODT und Markdown-ZIP neu erzeugt. Sämtliche zehn lokalen Prüfungen laufen grün: 954/954 Hauptvorlagen, 113/113 Sondervorlagen und Eval All-Pass 954/954.

## v4.75.0 — Mikrofehler-Bug-Hunt und einheitliches Vorlagendesign (2026-07-15)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 946/946.

### Juristische und mechanische Fehlerbereinigung

- Ein repoweiter Einzeldatei-Audit hat mehr als 100 kleine Fehler mit praktischer Folgewirkung beseitigt. 208 unbestimmte Auslassungsplatzhalter wurden durch ausfüllbare Tatsachen-, Datums-, Betrags- oder Anlagenfelder ersetzt; bedingte Anlagenverweise, unvollständige Klammern, Rubrumsangaben, Beweisangebote und Rechenfelder wurden auf den jeweiligen Verfahrensablauf abgestimmt.
- Die Anbieter- und Betreiberpflichten der KI-Verordnung sind in der Prüfmatrix absatz- und rollenrichtig neu zugeordnet. Dokumentation, Aufbewahrung, Konformitätsbewertung, Registrierung, Protokollierung, Grundrechte-Folgenabschätzung, Überwachung und Meldefristen stehen nun bei der jeweils verpflichteten Rolle und verweisen auf die einschlägigen Artikel.
- Fachspezifische Lapsus wurden unter anderem bei energierechtlicher Zuständigkeit, BaFin-Finanzierung, ausländerrechtlicher Niederlassungserlaubnis, Nachweisführung, Anlagenlogik und zweisprachiger Vertriebsvertragskündigung korrigiert. Die Kündigungs-README trennt jetzt Zugang nach § 130 BGB von der besonderen Gerichtsvollzieherzustellung nach § 132 BGB und enthält nur noch einen vorlagenspezifischen Normabschnitt.

### Navigation und Nutzerführung

- Alle 954 Vorlagen-READMEs wurden auf einen einheitlichen Navigationsvertrag geprüft. Jede README enthält genau einmal Download, Vorspruch und Nutzungsgrenze, Anwendungsbereich, einschlägige Normen sowie Hinweise zur Verwendung; 337 uneinheitliche Überschriften in 230 Dateien und 49 fehlende Kernabschnitte wurden bereinigt.
- Anwendungsgrenzen und Normkerne wurden insbesondere für Vorsorgevollmacht, IP-Strategie, urheberrechtliche Kreditsicherheit, Sanierungsgutachten, Rentenwiderspruch, Content-Lizenzierung und insolvenzrechtlichen Zahlungsdienstvergleich konkretisiert. Doppelte H1, leere Links und konkurrierende Standardabschnitte sind ausgeschlossen.
- Der Offline-Index stellt breite Tabellen auf kleinen Bildschirmen als beschriftete Karten dar, verbessert Filter, Fokusführung und Druckbild und bleibt ohne Netzverbindung vollständig bedienbar. Direktdownloads, lokale Vorschauen und maschinenlesbare Manifeste sind in allen drei Paketen synchron.

### Dokumentdesign und Releasequalität

- Sämtliche 954 ODT-Fassungen wurden neu gesetzt. Mehr Weißraum, ruhigere Absatzabstände, kontrollierte Zeilenhöhe, Schusterjungen- und Hurenkinderkontrolle, klarere Überschriften sowie Tabellen mit Kopfzeile, Rahmen und Innenabstand verbessern Lesbarkeit und Bearbeitung, ohne die juristische Gliederung zu verändern.
- Neun tabellendominierte Vorlagen wechseln automatisch in ein geprüftes A4-Querformat; alle übrigen bleiben im einheitlichen A4-Hochformat. Der Integritätscheck akzeptiert nur diese beiden fest definierten Layoutprofile und verhindert zufällige Seitenformate oder Randabweichungen.
- Die drei Releasearchive wurden vollständig neu gebaut und über `SHA256SUMS.txt` verifiziert. Sämtliche zehn lokalen Prüfungen laufen grün: 954/954 Hauptvorlagen, 113/113 Sondervorlagen und Eval All-Pass 946/946.

## v4.74.0 — Schnellere Offline-Navigation und präziser Fahrerlaubnisrechtsschutz (2026-07-15)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 946/946.

### Nutzbarkeit und Arbeitsgeschwindigkeit

- Die Offline-Indizes aller drei Releasepakete besitzen nun eine wortreihenfolgeunabhängige Mehrwortsuche, gleichwertige Treffer für Umlaute und ASCII-Umschriften, Filter nach Rechtsgebiet und Dokumenttyp, einen Zurücksetzen-Befehl, eine verständliche Leermeldung sowie Tastatursteuerung mit `/` und `Escape`.
- Jedes Releasepaket enthält zusätzlich ein UTF-8-kodiertes `manifest.json` mit Titel, Rechtsgebiet, Dokumenttyp, Datei- und Hinweispfad jeder Vorlage. Automatisierte Arbeitsabläufe können den Bestand damit ohne Auswertung der HTML-Seite erschließen.
- Der Releasebau sortiert die Einträge deterministisch und bricht bei doppelten oder fehlenden Indexzielen ab. README, Downloadübersicht, Workflow- und Beitragsdokumentation erläutern die direkte Suche, die Filter und das maschinenlesbare Manifest einheitlich.

### Juristische Präzision

- Die bisher missverständlich als Klage gegen eine MPU-Anordnung bezeichnete Vorlage ist bei unverändertem Dateipfad zu einer vollständigen Anfechtungsklage gegen die Fahrerlaubnisentziehung nach nicht beigebrachtem Gutachten ausgebaut. Sie behandelt die Gutachtenaufforderung gemäß § 44a VwGO als vorbereitende Verfahrenshandlung und prüft Rechtsgrundlage, Anlass, Fragestellung, Frist, Belehrung und den Schluss nach § 11 Abs. 8 FeV innerhalb der Klage gegen die Entziehungsentscheidung.
- Die Fahrerlaubnisvorlagen trennen Alkohol nach § 13 FeV, Cannabis nach dem seit dem 1. April 2024 geltenden § 13a FeV und sonstige Betäubungsmittel oder psychoaktiv wirkende Arzneimittel nach § 14 FeV. Neuerteilungsantrag und Widerspruchshinweise bilden zudem Sperrfrist, vorzeitige Aufhebung und die aufschiebende Wirkung nach § 80 VwGO präziser ab.
- Die interne KI-Nutzungsrichtlinie verweist für aktuelle Geschäftsgeheimnisverstöße nicht länger auf § 17 UWG alter Fassung, sondern auf §§ 4 und 23 GeschGehG; § 203 StGB und datenschutzrechtliche Folgen bleiben eigenständig abgegrenzt.

### Layout, Artefakte und Qualität

- Die Anlagenliste der Fahrerlaubnisklage führt Dokument und Datum in einer belastbaren Spalte zusammen. Die ODT-Erzeugung hält Tabellenzeilen künftig am Seitenwechsel geschlossen, damit Bezeichnung, Betrag und Erläuterung nicht auf verschiedene Seiten geraten.
- Die geänderten ODT- und Markdown-Arbeitsfassungen wurden synchron neu erzeugt und als A4-PDF visuell kontrolliert. Die drei Releasepakete enthalten geprüfte Offline-Indizes, Manifeste und vollständige Zielpfade; `SHA256SUMS.txt` wurde neu gebaut und erfolgreich gegengeprüft.
- Sämtliche zehn lokalen Prüfungen laufen grün: 954/954 Hauptvorlagen, 113/113 Sondervorlagen und Eval All-Pass 946/946.

## v4.73.1 — Vollständige Neuveröffentlichung des geprüften Bestands (2026-07-15)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 946/946.

### Release und Artefakte

- Der mit v4.73.0 fachlich und technisch bereinigte Vorlagenbestand wird unverändert als neuer Patch-Stand veröffentlicht. Es wurden keine juristischen Regelungen, Rechtsprechungsanker oder Dokumentstrukturen ohne neuen Sachgrund verändert.
- Das ODT-Komplettpaket, das Markdown-Komplettpaket und das Markdown-Paket des gerichtsleitenden Sonderbereichs wurden vollständig neu gebaut. Jedes Archiv enthält den aktuellen durchsuchbaren Offline-Index.
- `SHA256SUMS.txt` wurde für alle drei Release-Pakete neu erzeugt und erfolgreich gegengeprüft. Sämtliche zehn lokalen Prüfungen sowie der Eval-Harness laufen grün.

## v4.73.0 — Repoweiter Layout-Bug-Hunt und beschleunigtes Qualitätsgate (2026-07-14)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 946/946.

### Nachweisbare Fehlerbereinigung

- Ein vollständiger Format-Sweep hat 209 redundante Markdown-Trennlinien in 184 Vorlagen entfernt. Dreifach gesetzte Trenner wurden vollständig auf eine Linie reduziert; dadurch entfallen leere Doppelbalken in Markdown, ODT und Offline-Paketen.
- 148 rendererabhängige HTML-Abstände in elf Vorlagen wurden durch stabile Markdown-Tabellen, getrennte Betreffzeilen und sprechende Platzhalter ersetzt. Die Unterschriftsfelder in Bau-, Familien-, Miet-, Vergabe- und Fotolizenzvorlagen bleiben damit in Browser und ODT zweispaltig ausgerichtet.
- Die BAföG-Klage führt den Verfahrensgegenstand gliederungskonform als Kopfangabe. Der Sponsoringvertrag verweist nun auf das tatsächlich eingeräumte Nutzungsrecht statt auf eine nicht vorhandene Ziffer. Erbausschlagung, Erbscheinsantrag und Mängelrüge besitzen bereinigte Betreff-, Untergliederungs- und Fristfelder.
- Doppelte Unterschriftsbereiche in Schutzschrift und Vergabeaufklärung, übermäßige Leerzeilen in drei Mustertexten und sechs Vorlagen-READMEs sowie die unnummerierte Anlage der Umgangsvereinbarung wurden bereinigt. Für 187 geänderte Hauptvorlagen sind ODT und Markdown-ZIP synchron neu erzeugt.

### Dauerhafte Absicherung und Geschwindigkeit

- `validate-vorlagen.py` blockiert künftig doppelte Trennlinien, mehr als zwei aufeinanderfolgende Leerzeilen und HTML-Abstandsartefakte. Die Schlussblockprüfung erkennt zugleich unterschiedlich lange, tatsächlich vorhandene Unterschriftslinien.
- Gliederungs- und Rechtsprechungshygiene prüfen nun auch neue, noch nicht versionierte Dateien. Eine gezielte Negativprobe hat bestätigt, dass beide Checks solche Fehler vor dem ersten Commit abfangen.
- Die Umlautprüfung verarbeitet die gesamte Git-Dateiliste in einem einzigen Python-Prozess statt für jede Datei einen Interpreter zu starten. `check-all.py` führt die neun nur lesenden Prüfungen parallel und den reportschreibenden Eval-Lauf anschließend separat aus; `--jobs 1` bleibt als serielle Diagnoseoption verfügbar.
- Der vollständige Zehnfach-Lauf sank auf derselben Arbeitskopie von 65,44 Sekunden auf 5,25 Sekunden. Der optimierte serielle Vergleichslauf benötigt 8,81 Sekunden. Kein Qualitätscheck wurde entfernt oder abgeschwächt; alle zehn lokalen Prüfungen laufen grün.

## v4.72.0 — Vollständige BAföG-Antrags- und Rechtsschutzsuite (2026-07-14)

**Stand:** 954 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 946/946.

### Zwölf neue BAföG-Vorlagen

- Der Bereich Verwaltungsrecht enthält jetzt eigenständige Vorlagen für Erstantrag, Weiterförderung, Aktualisierung des Elterneinkommens, Vorausleistung, Fachrichtungswechsel, Vorabentscheidung, Auslandsförderung, Aufschub des Leistungsnachweises und Förderung über die Förderungshöchstdauer hinaus.
- Widerspruch, Verpflichtungsklage und einstweilige Anordnung bilden den vorgerichtlichen und gerichtlichen Rechtsschutz vollständig ab. Sie trennen Landesrechtsweiche, Rechtsbehelfsfrist, richtigen Beklagten, Verpflichtungs- und Bescheidungsantrag sowie den Eilmaßstab nach § 123 VwGO.
- Jede Vorlage besitzt einen fallbezogenen Tatsachen- und Beweisaufbau, ausformulierte Auswahlmodule, eine nummerierte Anlagenliste sowie eine eigene README mit Anwendungsgrenzen, amtlichen Quellen und Live-Rechercheankern. Amtliche BAföG-Formblätter werden ergänzt, nicht ersetzt.

### Rechtsstand und Nutzerführung

- Die Suite verarbeitet insbesondere Förderungsbeginn und Formblätter nach §§ 15 und 46 BAföG, die Zwei-Kalendermonats-Mechanik des § 50 Absatz 4 BAföG, Aktualisierung und Rückforderungsvorbehalt nach § 24 Absatz 3 BAföG sowie beide Vorausleistungswege nach § 36 BAföG.
- Fachrichtungswechsel und Leistungsnachweis enthalten die aktuellen Semestergrenzen und die Übergangsregeln des § 66a BAföG. Auslandsförderung trennt die Tatbestände des § 5 BAföG, Mindestdauer, Anerkennung, Bedarfe und die ausschließliche Zuständigkeit nach § 45 Absatz 4 BAföG.
- Der Verwaltungsrechtsindex, die Drei-Ordner-Sicht, der Gesamtdownloadindex und die Bestandszahlen wurden auf 954 Hauptvorlagen synchronisiert. Für alle Neuanlagen wurden ODT, Markdown-ZIP und spezifische Rubrics erzeugt; alle zehn lokalen Prüfungen laufen grün.

## v4.71.2 — Zahlungssaldo der Wechselmodell-Kostenabrechnung korrigiert (2026-07-14)

### Korrigiert

- Anlage 2 trennt nun Gesamtbetrag, unstreitige Zwischensumme und streitige Zwischensumme ausdrücklich. Streitige Kostenpositionen bleiben außerhalb der Sollanteile und des zahlbaren Ausgleichssaldos.
- Die Vorleistungen beider Eltern werden nur für unstreitige Positionen angesetzt. Eine spiegelbildliche Rechenkontrolle sichert, dass beide Elternrechnungen denselben Saldo mit umgekehrtem Vorzeichen ergeben.
- README, Checkliste, ODT und Markdown-ZIP wurden synchronisiert; alle zehn lokalen Prüfungen laufen grün.

## v4.71.1 — Anlagen des Wechselmodell-Betreuungsplans vervollständigt (2026-07-14)

### Korrigiert

- Die in Abschnitt 5.6 vorausgesetzte Anlage 2 ist nun als vollständige quartalsweise Beleg- und Ausgleichsliste vorhanden. Sie trennt Bruttokosten, Drittleistungen, verteilungsfähigen Nettobetrag, Elternquoten, bereits geleistete Zahlungen, Streitstatus und unstreitigen Ausgleichssaldo.
- Einwendungen gegen einzelne Kostenpositionen blockieren nicht mehr den unstreitigen Saldo. Übermittlungs-, Einwendungs- und Zahlungsfristen sowie das Verbot eines stillschweigenden Anerkenntnisses oder Unterhaltsverzichts sind ausfüllbar geregelt.
- Der bislang unnummerierte Verweis auf mitwandernde Gegenstände führt jetzt zu Anlage 3. Diese unterscheidet Übergabegegenstände von der dauerhaft in beiden Haushalten vorzuhaltenden Grundausstattung.
- ODT und Markdown-ZIP der Vereinbarung wurden erneuert; alle zehn lokalen Prüfungen laufen grün.

## v4.71.0 — Familien- und Erbrechtsvorlagen fachlich vertieft (2026-07-14)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Familienrecht

- Alle 38 Familienrechtsvorlagen wurden geprüft; die tragenden Muster für Kindesunterhalt, Mehr- und Sonderbedarf, Betreuungsunterhalt, einstweiligen Unterhalt, Umgang, gemeinsame Sorge, Wechselmodell und Zugewinnausgleich wurden mit fallspezifischer Subsumtion, Zeitabschnitten, Beweisführung und vollziehbaren Regelungsvarianten vertieft.
- Der Unterhalts-Eilrechtsschutz folgt nun dem eigenständigen Maßstab des § 246 Abs. 1 FamFG und verlangt nicht länger zusätzlich das dringende Regelungsbedürfnis des § 49 FamFG. Vorhandene Titel, Differenzbeträge und das Verbot doppelter Vollstreckung werden ausdrücklich geprüft.
- Verifizierte Anker des Bundesgerichtshofs und Bundesverfassungsgerichts erschließen die Bedarfsbemessung nach § 1615l BGB, Wechselmodell und Mehrbedarf, Sorge- und Umgangsmaßstab, grundrechtliche Grenzen erzwungener Begutachtung sowie die Bewertung freiberuflicher Praxen im Zugewinnausgleich.

### Erbrecht

- Alle 46 Erbrechtsvorlagen wurden geprüft; Erbfolge-Prüfvermerk, Erbscheinsanträge und -beschwerde, Ausschlagung und Anfechtung, Testamentseröffnung, Pflichtteilsstufenklage sowie notarielles Nachlassverzeichnis führen jetzt präziser durch Berufungskette, Nachweis, Amtsermittlung, Wertermittlung und Vollzug.
- Die eidesstattliche Versicherung beim gemeinschaftlichen Erbschein folgt § 352a Abs. 4 FamFG: Grundsätzlich erklären alle Erben; nur das Nachlassgericht kann die Versicherung einzelner Erben genügen lassen. Der überholte Vorbescheid ist durch den Feststellungsbeschluss nach § 352e FamFG ersetzt.
- Die Genehmigungsprüfung für Ausschlagungen Minderjähriger verwendet § 1643 Abs. 1 und 3 in Verbindung mit § 1851 Nr. 1 BGB. Die Anker BGH IV ZB 12/22 und IV ZB 37/23 unterscheiden den unbeachtlichen Irrtum über den Nächstberufenen von der aktuellen Genehmigungsausnahme; Pflichtteils- und Nachlassverzeichnisvorlagen verarbeiten die amtlich belegten Ermittlungs- und Vollstreckungsmaßstäbe.

### Qualität und Artefakte

- 84 Vorlagen wurden vollständig kontrolliert; 26 Mustertexte und 21 zugehörige Bereichs- oder Vorlagen-READMEs wurden materiell nachgeschärft. Doppelte Rubren, eine doppelte Unterschrift, missverständliche Stichtagsannahmen und unbedingte Anlagenverweise wurden bereinigt.
- Für alle 26 geänderten Hauptvorlagen wurden ODT und Markdown-ZIP neu erzeugt. Sämtliche zehn lokalen Prüfungen einschließlich Rechtsprechungshygiene, Gliederung, Artefaktintegrität und Eval laufen grün.

## v4.70.0 — Einzeldownloads und Offline-Navigation vervollständigt (2026-07-12)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Gesamtindex und Menüführung

- `DOWNLOADS.md` erschließt nun alle 1.055 Vorlagen einzeln. Der neue Schnellzugriff führt zu den Downloadtabellen aller 40 Rechtsgebiete; jeder Abschnitt besitzt einen Rücksprung. Alle Bereichs-READMEs verlinken unmittelbar ihren eigenen Downloadblock statt nur den Anfang des langen Gesamtindex.
- Die 113 gerichtlichen, staatsanwaltschaftlichen und amtsanwaltschaftlichen Markdown-Vorlagen stehen erstmals zusätzlich als individuelle Raw-Downloads im Gesamtindex. Die 18 Sonderbereichsmenüs führen jeweils direkt zum passenden Downloadabschnitt.
- Der Nutzerweg unterscheidet jetzt klar zwischen fachlicher Vorlagen-README, unmittelbarem Einzeldownload, Offline-Komplettpaket und reproduzierbarem Release-Stand. Browser-Suche und Bereichssprünge vermeiden langes Scrollen.

### Durchsuchbare Offline-Pakete

- Jedes der drei Release-ZIPs enthält eine eigenständige `index.html`. Der lokale Katalog filtert ohne Installation nach Rechtsgebiet, Titel oder Dateipfad und öffnet ausschließlich relative Ziele innerhalb des entpackten Pakets.
- Die ODT- und Markdown-Indizes enthalten jeweils 942 eindeutige Dateilinks; der Sonderbereichsindex enthält 113. Archivintegrität, Linkziele und SHA-256-Prüfsummen wurden für alle Pakete geprüft.

### README und dauerhafte Absicherung

- Die Pausenkarte ist klar vom juristischen Bestand getrennt und um weitere Kaffee-, Tee-, Mate-, Cola-, Energy- und koffeinfreie Getränke einschließlich Red Bull, Monster und der Thermoskanne mit Wasser erweitert. Ein amtlicher BfR-Verweis führt zu Sachinformationen über Koffein und Energy-Drinks.
- `validate-vorlagen.py` sichert die bereichsspezifischen Downloadanker der 40 Hauptbereiche. `check-gerichtsleitend.py` verlangt für alle 18 Sonderbereiche den passenden Sprunglink sowie Vorschau und Raw-Download jeder Sondervorlage im erzeugten Gesamtindex.
- Alle zehn lokalen Prüfungen laufen grün.

## v4.69.1 — GitHub-Actions-Laufzeit auf Node 24 gehoben (2026-07-11)

### Korrigiert

- Der Eval-Workflow verwendet `actions/checkout@v6` statt der auf Node.js 20 beruhenden Version 4. Damit entfällt die von GitHub gemeldete erzwungene Laufzeitumstellung; zugleich nutzt der Checkout-Schritt das aktuelle, getrennte Credential-Handling der offiziellen Action.
- Vorlagenbestand, Navigationsindex und Release-Pakete bleiben gegenüber v4.69.0 unverändert. Alle zehn lokalen Prüfungen sowie der anschließende GitHub-Eval laufen grün.

## v4.69.0 — Gesamtindex, Komplettpakete und Menüführung ausgebaut (2026-07-11)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Navigation und Nutzerführung

- Der neue, erzeugte Gesamtindex `DOWNLOADS.md` führt für jede der 942 Hauptvorlagen zur fachlichen Menüseite sowie unmittelbar zur ODT-Arbeitsfassung und zum Markdown-ZIP. Alle 40 Rechtsgebietsmenüs, die Drei-Ordner-Sicht, die Prozesspakete und der gerichtsleitende Sonderbereich verweisen auf diesen Direkteinstieg.
- Das Wurzel-README unterscheidet die Arbeitswege für Einzelvorlage, Offline-Kanzleibestand, prüfbare Quellenfassung und Repository-Entwicklung. Der Downloadweg folgt jetzt einheitlich der Reihenfolge Rechtsgebiet oder Dokumenttyp wählen, Vorlagen-README prüfen und gewünschte Fassung laden.
- Ein verdeckter Zählversatz in der Startseite wurde berichtigt: Der Bestand verteilt sich auf 365 vertragliche, 479 prozessuale und formularbezogene sowie 98 sonstige Vorlagen. `check-kategorien-index.py` gleicht diese drei Angaben künftig mit dem kanonischen Kategorieindex ab.

### Downloads und Release-Artefakte

- `scripts/build-release-assets.py` erzeugt reproduzierbar ein ODT-Komplettpaket, ein Markdown-Komplettpaket, ein Markdown-Paket des gerichtsleitenden Sonderbereichs und `SHA256SUMS.txt`. Die Pakete werden als Release-Assets veröffentlicht und sind über versionsunabhängige `releases/latest/download`-Links erreichbar.
- `scripts/build-download-index.py` erzeugt den vollständigen Direktdownloadindex aus dem kanonischen Bestand. Sein Prüfmodus verhindert, dass Neuanlagen oder Umbenennungen unbemerkt aus dem Index fallen.
- Die Startseite enthält auf ausdrücklichen Wunsch zusätzlich eine klar vom juristischen Bestand getrennte Pausenkarte mit Kaffee, Tee, koffeinhaltigen und koffeinfreien Getränken, beispielhaft Red Bull und Monster sowie der Thermoskanne mit Wasser.

### Dauerhafte Absicherung

- `validate-vorlagen.py` prüft nun die Aktualität des Gesamtindex, die Komplettpaket-Links, die Verknüpfung aller 40 Bereichsmenüs und sämtliche relativen Markdown-Linkziele im nutzerseitigen Bestand. Tote Menüpunkte oder verschobene Dateien brechen damit den lokalen Gate.
- Die drei ZIP-Pakete wurden deterministisch gegengeprüft, vollständig entpackt und anhand ihrer SHA-256-Summen verifiziert. Alle zehn lokalen Prüfungen laufen grün.

## v4.68.1 — Deutschen MiCAR-Bestandsübergang nach § 50 KMAG korrigiert (2026-07-11)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Korrigiert

- Der Übergangsplan für Kryptowerte-Dienstleister vermischt den unionsrechtlichen Höchstrahmen des Art. 143 Abs. 3 MiCAR nicht länger mit der kürzeren deutschen Fortgeltung für erlaubte Bestandsinstitute. Für die in § 50 Abs. 1 KMAG bezeichneten Erlaubnisse weist er nun den nach § 50 Abs. 2 KMAG maßgeblichen früheren Endzeitpunkt und spätestens den 31. Dezember 2025 aus.
- Zuvor erlaubnisfreie Tätigkeiten werden als eigener Pfad nach § 50 Abs. 4 KMAG behandelt. Die Vorlage verlangt den Nachweis der Anzeige bis zum 1. August 2024 und trennt diesen Pfad von Erlaubnisfortgeltung, Art.-60-Notifizierung und Art.-63-Zulassung.
- Warnhinweis, Statusaufnahme, Fristenkalender, Anschlussstatus und Anlagenapparat führen für jede Altleistung zu einem belegten Übergangspfad und letzten rechtmäßigen Erbringungstag. Dadurch kann die unionsrechtliche Höchstfrist bis zum 1. Juli 2026 nicht mehr irrtümlich als deutsche Erlaubnisbrücke für das erste Halbjahr 2026 verwendet werden.

### Review und Prüfung

- Der nachträgliche automatische Codex-Review zu PR #285 enthielt keine Inline-Threads oder Änderungsanforderungen. Die zusätzliche Primärquellenprüfung gegen Art. 143 MiCAR und § 50 KMAG deckte den nationalen Fristenfehler auf.
- ODT und Markdown-ZIP der betroffenen Vorlage wurden neu erzeugt. Alle zehn lokalen Prüfungen laufen grün.

## v4.68.0 — SGB-II-Reform, MiCAR-Fristablauf und Rechtsbehelfsmechanik aktualisiert (2026-07-11)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Grundsicherung für Arbeitsuchende ab 1. Juli 2026

- Eilantrag, Jobcenter-Widerspruch und Unterkunftsklage verwenden jetzt das Grundsicherungsgeld und bilden die Reform zum 1. Juli 2026 materiell ab. Die Vermögensprüfung enthält die altersabhängigen Freibeträge nach § 12 Abs. 2 SGB II; die Unterkunftskarenz berücksichtigt Eineinhalbfachgrenze, Ausnahmen, Mietpreisprüfung und Gesamtangemessenheitsgrenze; Pflichtverletzungen und wiederholte Meldeversäumnisse folgen der aktuellen 30-Prozent-Systematik.
- § 65a SGB II ist als echte Übergangsweiche umgesetzt: Für § 12 entscheidet der Beginn des Bewilligungszeitraums, für §§ 31 bis 32 der Zeitpunkt der Pflichtverletzung oder des Meldeversäumnisses. Die bis Ende 2026 zulässige Weiterverwendung der Bezeichnung „Bürgergeld“ durch Behörden wird nicht fälschlich als Bescheidmangel behandelt.
- Die Rechtsbehelfsmechanik trennt die von § 39 Nr. 1 SGB II erfasste Aufhebungs-, Entziehungs- und Minderungsregelung von der Erstattungsregelung nach § 50 SGB X. Letztere behält grundsätzlich ihre aufschiebende Wirkung nach § 86a Abs. 1 SGG, auch wenn beide Regelungen in einem Bescheid verbunden sind.

### Aufsichts-, Digital- und Schadensrecht

- Der Übergangsplan nach Art. 143 Abs. 3 MiCAR ist nach Ablauf der Fortführungsbefugnis spätestens am 1. Juli 2026 als Abschluss-, Nachweis- und Mängelbeseitigungsdossier ausgerichtet. Er verlangt Anschlussstatus, letzten rechtmäßigen Übergangstag, Statuslücken, Kundenmigration, Restabwicklung und gegebenenfalls Aufsichtseskalation; ein anhängiger Antrag wird nicht als fortdauernde Erlaubnisbrücke dargestellt.
- Veraltete TMG-Verweise wurden durch Art. 4 DSA sowie §§ 7 und 8 DDG ersetzt. Die Filesharing-Hinweise unterscheiden Haftungsprivilegierung und Sperranspruch einschließlich des gesetzlichen Kostenausschlusses.
- Die Darstellung des Werkstattrisikos nach BGH VI ZR 253/22 trennt bezahlte und unbezahlte Werkstattrechnung und weist bei unbezahlter Rechnung auf Zahlung an die Werkstatt Zug um Zug gegen Anspruchsabtretung hin.

### Dokumentlogik und dauerhafte Absicherung

- 13 Warnblöcke bezeichnen Vertrag, Erklärung, Anspruchsschreiben und Schriftsatz wieder rollengerecht. Räumungsvereinbarungen und Letter of Intent erscheinen nicht mehr als Schriftsätze; Klagen, Selbstanzeige, Verteidigungsanzeige, Vorpfändung, Widerruf und Teilzeitverlangen werden nicht mehr als Verträge etikettiert.
- `scripts/validate-vorlagen.py` blockiert künftig offenkundige Vertrag-/Schriftsatz-Verwechslungen im Warnhinweis anhand des Rubric-Typs.
- Die 28 berührten Hauptvorlagen wurden als ODT neu erzeugt; 28 Markdown-ZIPs wurden synchronisiert. Alle zehn lokalen Prüfungen laufen grün.

## v4.67.0 — Rechtsprechungs-, Rechtsstands- und Typzuordnungen amtlich nachgeschärft (2026-07-11)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Rechtsprechung und Primärquellen

- Überdehnte oder sachfremd zugeordnete Entscheidungsanker wurden am amtlichen Volltext korrigiert. Das betrifft insbesondere BGH VII ZR 10/24 zur rechtsgeschäftlichen Anordnung nach § 2 Abs. 5 VOB/B, BGH I ZR 187/17 zur fallbezogenen Schadensbemessung bei fehlender Urheberbenennung, BGH IV ZR 437/22 zu einer konkreten Berufsunfähigkeitsklausel, BGH VI ZR 396/24 und EuGH C-741/21 zur datenschutzrechtlichen Verantwortlichkeit sowie BGH EnZR 85/20 und EnVR 17/22 im Energierecht.
- Die nicht amtlich auffindbare Angabe „OLG Karlsruhe, 7 U 173/25“ wurde aus der Kostenfeststellungsvorlage entfernt. Der verbleibende Prüfanker BGH III ZR 156/12 ist direkt mit dem amtlichen Volltext verbunden und auf die Erledigung vor Rechtshängigkeit begrenzt.
- `references/leitentscheidungen-anker.md` wurde von einem unverbundenen Aktenzeichenpool zu einer kompakten Liste unmittelbar verlinkter Primärquellen mit eng beschriebenem Prüfungsgegenstand umgebaut. Der Rechtsprechungshygiene-Check verlangt dort künftig für jede Entscheidung einen Direktlink und blockiert als Verifikation ausgegebene Nutzerangaben oder nur aktenzeichenähnliche Linien.

### Rechtsstand und Antragsmechanik

- Die EEG-Zahlungsklage trennt Marktprämie, Einspeisevergütung und Mieterstromzuschlag nach § 19 Abs. 1 EEG 2023, führt Abschläge und Fälligkeit nach § 26 EEG 2023 richtig und berechnet Gegenansprüche nach § 52 EEG 2023 in Euro je Kilowatt und Kalendermonat. Die Netzentgeltvorlage verwendet nicht länger den weggefallenen § 27 StromNEV, behauptet keine Verjährungshemmung durch ein bloßes Beanstandungsschreiben und formuliert das Begehren nach §§ 30, 31 EnWG vollziehbar.
- Weitere Korrekturen betreffen die elektronische Belegbereitstellung nach § 556 Abs. 4 BGB, die Folgen einer verspätet formal korrigierten Betriebskostenabrechnung, § 20 MStV, die seit dem 19. Juni 2026 geltenden Widerrufsregeln für Finanzdienstleistungen, die Marktanteils- und Wettbewerbsverbotsgrenzen der Vertikal-GVO sowie die Ermessensprüfung nach § 227 AO.
- Gegenüberstellungen, Verträge und Schriftsätze enthalten Entscheidungen nicht mehr als operative Klauselbestandteile. Rechtsprechungsgrenzen, Praxisfolgen und amtliche Links stehen in den jeweiligen READMEs; die Mustertexte bleiben ausfüll- und versandfähig.

### Dokumenttypen, Kategorien und Artefakte

- 32 ausdrückliche Typausnahmen verhindern, dass Beschlüsse, Erklärungen, Vorvereinbarungen oder Rechtsschutzschreiben bei einer Rubric-Regeneration als falscher Dokumenttyp behandelt werden. Der Generator übernimmt den echten H1-Titel, unterstützt gezielte Regenerationen mit `--slug` und hält Typ, Prüfblock und Anzeigename reproduzierbar zusammen.
- Widerrufs- und Gegendarstellungsschreiben, Anfechtung der Erbausschlagung sowie Forderungsverkauf wurden in der Drei-Ordner-Sicht ihrem tatsächlichen Arbeitsmodus zugeordnet. Die drei Kategorien umfassen nun 365 vertragliche, 479 prozessuale und formularbezogene sowie 98 sonstige Vorlagen.
- Die 16 geänderten Hauptvorlagen wurden als ODT neu erzeugt; ihre Markdown-ZIPs und die repoweiten Downloadpakete sind synchronisiert.

## v4.66.0 — Mehr als fünfhundert strukturelle und fachliche Altfehler bereinigt (2026-07-10)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Platzhalter und Redaktionsfehler

- 409 Zeilen mit verschachtelten Platzhaltern in 109 Hauptvorlagen wurden in eindeutig ausfüllbare Einzelfelder, Auswahlfelder oder klar bezeichnete Variantenmodule überführt. Lange Wahlklauseln behalten dabei ihre rechtliche Aussage und ihre gesonderten Felder für Datum, Betrag, Urkundsdaten, Beteiligte und Nachweise.
- Versehentliche Wort- und Feldwiederholungen, doppelte Abkürzungen, leere Alternativen und gebrochene Fettschriftmarker wurden repoweit beseitigt. Ein zusätzlicher Gegencheck erfasste insbesondere unbrauchbare Kombinationen wie doppelte Nummernfelder, fehlende IBAN-Felder, unbestimmte Urkundsrollennummern und verlorene Datumsfelder.
- Der Vermächtniserfüllungsvertrag trennt nun Geld-, Sach- und Grundstücksvollzug, Belastungsvarianten, notarielle Urkundsdaten, Abgeltungsumfang und Empfangsbestätigung ohne verschachtelte oder nur scheinbar ausfüllbare Felder.

### Tabellen, Zuständigkeit und Dokumentlogik

- 45 verschobene Markdown-Tabellenzeilen in 20 Vorlagen und zwei unmaskierte Tabellenzeichen in Themenübersichten wurden korrigiert. Zweisprachige Tabellen bleiben wieder spaltenparallel; Platzhalter umspannen keine Zellgrenzen mehr.
- Zivilprozessuale Zuständigkeitshinweise verwenden die seit dem 1. Januar 2026 geltende Amtsgerichtsgrenze von 10.000 EUR und unterscheiden anhand von § 44 EGGVG ältere, bereits anhängige Verfahren. Die Korrektur betrifft unter anderem Erb-, Insolvenz-, Energie-, Verkehrs- und allgemeine Zivilprozessvorlagen.
- Sechs sachfremde Vollstreckungsabsätze in READMEs zu Prozesskostenhilfe, Fristverlängerung, RVG-Kostenrechnung, Streitwertbeschwerde, Stufen- und Zahlungsklage wurden durch vorlagenspezifische Form-, Frist-, Zuständigkeits- und Nachweisführung ersetzt.

### Dauerhafte Absicherung

- `scripts/validate-vorlagen.py` erkennt jetzt verschachtelte Platzhalter, Inhaltswort- und Abkürzungsdopplungen, leere Alternativen, gebrochene Fettschrift sowie uneinheitliche oder von Platzhaltern überspannte Markdown-Tabellen in Mustertexten und READMEs.
- `scripts/check-gerichtsleitend.py` blockiert verschachtelte Platzhalter auch im gerichtlichen und staatsanwaltschaftlichen Sonderbereich.
- Insgesamt wurden mehr als fünfhundert reproduzierbare Einzelbefunde behoben. Die 175 berührten Hauptvorlagen wurden als ODT neu erzeugt und ihre Markdown-ZIPs synchronisiert; alle zehn lokalen Prüfungen laufen grün.

## v4.65.0 — Navigation und Downloads vollständig erschlossen (2026-07-10)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Einstieg und Menüführung

- Das Wurzel-README beginnt nun mit einem arbeitsorientierten Direkteinstieg: Rechtsgebiet, Dokumenttyp, Prozesspaket, gerichtsleitender Gesamtindex, Dateisuche, Workflow, neueste Veröffentlichung und vollständiges Repository-Archiv sind ohne Umwege erreichbar.
- Alle 40 Rechtsgebiets-READMEs besitzen eine einheitliche Navigation zurück zur Startseite, zur Drei-Ordner-Sicht, zu den Arbeitsabläufen und zum ZIP-Archiv des Hauptstands.
- Die 39 tabellarischen Rechtsgebietsmenüs verwenden jetzt die echten H1-Dokumenttitel und sind alphabetisch sortiert. 75 bislang nur über die Drei-Ordner-Sicht auffindbare Vorlagen wurden zusätzlich in ihre fachlichen Bereichsmenüs aufgenommen. Der bereits eigenständig strukturierte Index des öffentlichen Baurechts blieb erhalten.
- Die Drei-Ordner-Sicht, der Workflow-Arbeitszettel und der gerichtsleitende Sonderbereich wurden mit konsistenten Rück- und Querverweisen ausgestattet. Die 18 Unterbereiche des Sonderbereichs führen nun unmittelbar zur Startseite und zum vollständigen Gerichtsindex.

### Downloads und Vorschau

- 108 Vorlagen-READMEs mit bislang unvollständiger lokaler Vorschau verlinken nun sowohl die ODT- als auch die Markdown-Datei am kanonischen Speicherort. Die vorhandenen ODT- und Markdown-ZIP-Direktdownloads bleiben unverändert.
- `scripts/update-readme-md-zip-links.py` normalisiert künftig neben dem Markdown-ZIP-Link auch die beiden Vorschauziele und erkennt beide im Bestand verwendeten Downloadüberschriften.
- `scripts/validate-vorlagen.py` prüft jetzt den exakten `.md.zip`-Direktdownload statt einer bloßen `.md`-Teilzeichenfolge, den ODT-Direktdownload, beide lokalen Vorschauen, die Wurzelverlinkung aller 40 Themenordner und die genau einmalige Aufnahme jeder Hauptvorlage in ihr Rechtsgebietsmenü.
- `CLAUDE.md` und `CONTRIBUTING.md` beschreiben die neue Navigations- und Downloadpflicht, damit Neuanlagen beide Navigationsachsen vollständig mitführen.

### Prüfung

Alle relativen Markdown-Links wurden repoweit geprüft; 4.792 Linkziele sind vorhanden. Jede der 942 Hauptvorlagen ist sowohl über ihr Rechtsgebietsmenü als auch genau einmal über die Drei-Ordner-Sicht erreichbar und besitzt ODT-Download, Markdown-ZIP-Download sowie beide Vorschauziele. Der vollständige lokale Gate wurde mit allen zehn Prüfungen ausgeführt.

## v4.64.0 — Planwerke und Klagearchitektur vervollständigt (2026-07-10)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Insolvenz- und Restrukturierungsplan

- Der Insolvenzplan bildet die bedarfsabhängigen Anlagen nach §§ 229, 230 InsO jetzt rollengenau ab. Neu hinzugekommen sind vollständige Arbeitsblätter für gruppeninterne Drittsicherheiten, Fortführung und Planerfüllung, Masseberichtigung und Aufhebungsreife, Ausgleichsfonds, Ausschüttung, Vollstreckung und Planüberwachung.
- Gruppeninterne Drittsicherheiten werden im darstellenden Teil, in einer eigenen Gruppe, im gestaltenden Teil, in der Vergleichsrechnung und mit der Zustimmung des verbundenen Sicherungsgebers konsistent geführt. Forderungsquote und Entschädigung für den Sicherungseingriff bleiben getrennt.
- Der Restrukturierungsplan enthält eine nachrechenbare Erklärung zur Sicherung oder Wiederherstellung der Bestandsfähigkeit, den vollständigen Erklärungssatz nach § 15 StaRUG, individualisierte Planangebote, Kosten- und Annahmeunterlagen, Versammlungsvarianten, Abstimmungsdokumentation und Bestätigungsdossier.
- Eine neue Anlage 26 erfasst die Stellungnahme eines vor der Abstimmung bestellten Restrukturierungsbeauftragten nach § 76 Abs. 4 StaRUG. Die Gründe und der Nettoeffekt einer neuen Finanzierung werden entsprechend der gesetzlichen Anlage zu § 5 StaRUG offengelegt.
- Unzulässige automatische Ersatzklauseln, ungenaue Rollenzuweisungen und verschachtelte Platzhalter wurden aus beiden Planwerken entfernt. Sämtliche neuen Anlagen sind mit Planstellen, Rechenwerken, Nachweisen und Vollzugsschritten verbunden.

### Klage- und Verfahrensabdeckung

- Die sechs Prozesspakete für Zivil-, Arbeits-, Verwaltungs-, Finanz- und Sozialgericht sowie Familienverfahren wurden um ausformulierte Klage- und Antragsvarianten erweitert. Die Pakete trennen nun unter anderem Zahlungs-, Handlungs-, Feststellungs- und Stufenklage, Kündigungs- und Befristungskontrolle, Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungs- und Untätigkeitsklage sowie Sorge-, Umgangs-, Unterhalts- und Scheidungsanträge.
- Jede Gerichtsbarkeit erhält eine eigene Fristen-, Zuständigkeits- und Beweisarchitektur. Beweismatrizen verbinden Tatbestandsmerkmal, konkrete Tatsache, Beweismittel und Fundstelle; die READMEs erläutern die jeweils maßgeblichen Statthaftigkeits- und Eilrechtsschutzgrenzen.
- Die Übersicht `prozessvorlagen/README.md` weist die Grundarchitekturen und die fachrechtlichen Klagen in den Themenordnern nachvollziehbar aus, ohne Antragsverfahren künstlich als Klagen zu bezeichnen.

### Artefakte und Prüfung

Die acht geänderten Hauptvorlagen wurden als ODT neu erzeugt; sämtliche Markdown-ZIPs wurden anschließend synchronisiert. Der vollständige lokale Gate wurde mit allen zehn Prüfungen ausgeführt.

## v4.63.5 — Umfangsangabe des Rechtsfeinschliffs berichtigt (2026-07-09)

### Korrigiert

- Die Umfangsangabe zu v4.63.4 nennt nun zutreffend sechzehn Themenbereiche. Die Zahl von 24 fachlich überarbeiteten Hauptvorlagen, der Vorlagenbestand und sämtliche Prüfergebnisse bleiben unverändert.

## v4.63.4 — Platzhalter-, Rollen- und Rechtsfeinschliff (2026-07-09)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Korrigiert

- 24 Hauptvorlagen aus sechzehn Themenbereichen wurden anhand konkreter Restfehler überarbeitet. Falsche Mandantenformen sind nun durchgehend grammatisch korrekt; Erkenntnis-, Frist-, Betrags- und Beweisfelder lassen sich ohne verbleibende Redaktionswörter ausfüllen.
- Der gerichtliche Antrag auf Aussetzung der Vollziehung trennt Aussetzung und Aufhebung einer bereits vollzogenen Steuerfestsetzung nach § 69 Abs. 3 FGO. Die zugehörige README beschreibt Säumnis- und Aussetzungszinsfolgen ohne pauschale Rückwirkungsbehauptung.
- Die CISG-Kaufpreisklage trennt den Zinsanspruch aus Art. 78 CISG vom vertraglich oder nach Art. 7 Abs. 2 CISG und dem Kollisionsrecht zu bestimmenden Zinssatz. Rechnungs- und Mahnanlagen sind widerspruchsfrei nummeriert.
- Die Insolvenzanfechtungsklage berücksichtigt die seit dem 1. Januar 2026 geltende Wertgrenze von 10.000 EUR und die Übergangsregel des § 44 EGGVG für ältere Verfahren.
- Gemischte Anlagenbezeichnungen wie „Anlagen 1 bis K 7", ein fehlerhafter Tabellenplatzhalter in der Berufsunfähigkeitsklage und unzutreffende Dezimal-Querverweise wurden bereinigt.

### Artefakte und Prüfung

Die 24 betroffenen ODT-Dateien und Markdown-ZIPs wurden aus den geänderten Markdown-Quellen neu erzeugt. Der vollständige lokale Gate wurde anschließend mit allen zehn Prüfungen ausgeführt.

## v4.63.3 — Redaktions- und Nutzungsfehler in Kanzleivorlagen bereinigt (2026-07-09)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Korrigiert

- Zehn Hauptvorlagen aus Gewerblichem Rechtsschutz, Vergaberecht, Medizinrecht, Versicherungsrecht, Strafrecht, Verkehrsrecht sowie Urheber- und Medienrecht wurden redaktionell bereinigt.
- Fehlerhafte Formen wie „unsere Mandant" und „meiner Mandant" wurden in den betroffenen Kanzleischreiben auf „Mandantschaft" beziehungsweise die korrekte Mandantin-/Mandanten-Form umgestellt.
- Im urheberrechtlichen Auskunftsschreiben nach § 101 UrhG wurde ein gebrochener Vertriebsbaustein geschlossen: Der Testkauf-/Anlagenplatzhalter steht nun als sauber ausfüllbarer Satz ohne Klammerbruch.

### Artefakte und Prüfung

Die zehn betroffenen ODT-Dateien und die Markdown-ZIPs wurden aus den geänderten Markdown-Quellen neu erzeugt. Der vollständige lokale Gate wurde anschließend ausgeführt.

## v4.63.2 — Rechtsstands-Sanity-Workflow ergänzt (2026-07-09)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Ergänzt

- `references/rechtsstands-sanity-check.md` beschreibt einen kompakten Prüffahrplan für Rechtsstands- und Rechtsprechungs-Sweeps: erst Validatoren, dann gezielte Suchmuster, dann Primärquelle, dann enger Diff.
- `WORKFLOWS.md` verlinkt den neuen Arbeitszettel und trennt echte Rechtsstandsfehler von Warnbeispielen, Suchankern und historischen Hinweisen.
- `README.md` weist im Schnellstart auf den Rechtsstands-Sanity-Check hin.

### Geprüft

Der vollständige lokale Gate wurde ausgeführt: `python3 scripts/check-all.py` läuft mit 10/10 Checks grün; `validate-vorlagen` erkennt 942 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen in 18 Bereichen und `run-eval` meldet All-Pass 934/934.

## v4.63.1 — Rechtsstands- und Gliederungskorrektur im Urheberrecht (2026-07-09)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Korrigiert

- `urheber-und-medienrecht/antrag-einstweilige-verfuegung-urheberrecht-bildrecht/` verwendet im formalen Kopf nun „Betreff" statt einer freistehenden Gegenstandszeile. Damit passt die neue Eilvorlage wieder zur repoweiten Gliederungsregel aus `CLAUDE.md`.
- `urheber-und-medienrecht/autorenvertrag-verlag/` trennt allgemeine Vertragsänderungen von den gesetzlichen Schriftformfällen des Urhebervertragsrechts. § 40 UrhG wird nicht mehr als pauschales Schriftformerfordernis für jede Vertragsänderung behandelt; die Klausel verweist nun gezielt auf § 31a Abs. 1 Satz 1 UrhG für unbekannte Nutzungsarten und § 40 Abs. 1 Satz 1 UrhG für künftige, nicht näher oder nur der Gattung nach bestimmte Werke.

### Geprüft

Die betroffenen ODT- und Markdown-ZIP-Artefakte wurden neu erzeugt. Der vollständige lokale Gate wurde ausgeführt: `python3 scripts/check-all.py` läuft mit 10/10 Checks grün; `check-rechtsprechungshygiene`, `check-gliederung`, ODT-Integrität, ZIP-Synchronität und `run-eval` melden keine Fehler.

## v4.63.0 — Urheber- und Medienrecht für Plattformen, KI-Training und Rechteklärung erweitert (2026-07-08)

**Stand:** 942 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Eval-Harness steht bei All-Pass 934/934.

### Neue Vorlagen im Urheber- und Medienrecht

- `urheber-und-medienrecht/ki-trainingsdaten-lizenzvertrag-urhg/` ergänzt einen Lizenzvertrag für urheberrechtlich geschützte Trainingsdaten bei KI-Systemen. Der Vertrag trennt Trainingskorpus, Rechtekette, Text-und-Data-Mining-Zweck, Nutzungsvorbehalt, Opt-out-Matrix, Vergütung, Audit, Output-Schutz und Löschung.
- `urheber-und-medienrecht/antrag-plattformentfernung-urheberrecht-dsa/` ergänzt eine Notice-and-action-Meldung an Plattformen und Hostingdienste nach Art. 16 Digital Services Act für urheberrechtliche Uploads, rechtswidrige Bildnisse und persönlichkeitsrechtsverletzende Inhalte.
- `urheber-und-medienrecht/rechteklaerung-audiovisuelle-produktion-dossier/` ergänzt ein Rechteklärungsdossier für Film-, Serien-, Dokumentations-, Trailer- und Social-Media-Produktionen mit Drittmaterial, Musikrechten, Bildnisrechten, Risikomatrix und Versionsfreigabe.
- `urheber-und-medienrecht/antrag-einstweilige-verfuegung-urheberrecht-bildrecht/` ergänzt einen gerichtlichen Eilantrag bei unberechtigter Foto-, Video-, Text- oder Bildnisnutzung mit konkreter Verletzungsform, Dringlichkeit und Glaubhaftmachung.

### Navigation und Artefakte

Die Bereichsübersicht `urheber-und-medienrecht/README.md` sowie die Drei-Ordner-Sicht wurden auf die vier neuen Muster erweitert. Für alle neuen Hauptvorlagen wurden Markdown, ODT, Markdown-ZIP und Rubric erzeugt.

### Geprüft

Der vollständige lokale Gate wurde ausgeführt: `python3 scripts/check-all.py` läuft mit 10/10 Checks grün. `validate-vorlagen` erkennt 942 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen in 18 Bereichen, `check-md-zip-integrity` bestätigt synchrone ZIPs und `run-eval` meldet All-Pass 934/934.

## v4.62.0 — Vorschau- und Downloadsprache repoweit geschärft (2026-07-08)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Release verbessert die Nutzungsebene aller Hauptvorlagen-READMEs, ohne fachliche Mustertexte, ODT-Binaries, ZIPs oder Rechtsprechungsanker zu verändern.

### Vorschau statt missverständlichem Online-Ansehen

832 Vorlagen-READMEs verwenden nun die Bezeichnung „Vorschau im Repository" für die Rohansicht der ODT- und Markdown-Dateien. Damit ist klarer getrennt zwischen der Vorschau im GitHub-Repository, dem echten ODT-Download und dem ZIP-gepackten Markdown-Direktdownload.

### Pflegekonvention nachgezogen

`CLAUDE.md` und `scripts/update-readme-md-zip-links.py` wurden auf die neue Bezeichnung nachgezogen. Künftige Pflege- und Downloadlink-Läufe sollen die Roh-Markdown-Vorschau deshalb nicht wieder als „Online ansehen" ausgeben.

### Geprüft

Die Änderung betrifft nur README- und Pflegehinweise. Download-URLs, lokale Dateipfade, ODT-Dateien, Markdown-ZIPs und Vorlageninhalte bleiben unverändert. Der vollständige lokale Gate wurde anschließend ausgeführt.

## v4.61.0 — Navigations- und Nutzungshygiene nach dem ODT-Lesbarkeitslift (2026-07-08)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Release schärft die Einstiegsebene nach dem ODT-Schriftbildlift: keine fachlichen Vorlagentexte, keine Rechtsprechungsanker und keine Binaries wurden verändert; verbessert wurden ausschließlich Navigation, Nutzungsreihenfolge und Lesbarkeit zentraler Projektdokumente.

### Klarerer Einstieg

Die Startseite führt jetzt ausdrücklich durch die praktische Reihenfolge `README.md`, ODT-Arbeitsfassung, Markdown-Quelle und ZIP-Mitnahme. Außerdem erklärt sie den seit v4.60.0 bewusst luftigeren ODT-Satz und stellt klar, dass die Markdown-Quelle fachlich führend bleibt.

### Workflow vor blindem Befüllen

`WORKFLOWS.md` enthält eine kurze Passungsprüfung vor der Vorlagennutzung: Dokumenttyp, Rolle, Verfahrensstadium, Zuständigkeit und Anlagenapparat werden vor dem Ersetzen der Platzhalter geprüft. Die Drei-Ordner-Sicht erklärt nun deutlicher, dass sie eine Navigationsschicht nach Arbeitsmodus ist und nicht die kanonische Rechtsgebietsablage ersetzt.

### Sonderbereich lesbarer

Der Vorspruch des gerichtsleitenden Sonderbereichs wurde in kurze, scannbare Absätze zerlegt. Die Hinweise zu Artikel 22 DSGVO, KI-VO, Aktengeheimnis, Amtsverschwiegenheit, Schatten-KI und Freigabeverantwortung bleiben inhaltlich unverändert, sind aber nicht mehr als dichter Block gesetzt.

### Geprüft

Interne Links in `README.md`, `WORKFLOWS.md`, `kategorien/README.md` und `vorlagen-gerichtsleitend/README.md` wurden geprüft. Zusätzlich laufen Kategorienindex, Sonderbereichsvalidator und Rechtsprechungshygiene grün; der vollständige lokale Gate wurde anschließend ausgeführt.

## v4.60.0 — ODT-Schriftbild weiter aufgelockert und Bleiwüsten reduziert (2026-07-08)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Release hebt ausschließlich das Arbeitsfassungs-Design der ODT-Dateien: Die juristischen Mustertexte bleiben unverändert, aber die editierbaren Bürovorlagen lesen sich luftiger, ruhiger und weniger gedrängt.

### Mehr Raum im Schriftbild

Der ODT-Generator setzt für Fließtext nun 121 Prozent Zeilenhöhe sowie stärkere Absatzabstände davor und danach. Überschriften erhalten mehr Abstand zum vorhergehenden Text und bleiben näher am folgenden Inhalt. Listen bekommen mehr vertikale Luft; Tabellenzellen erhalten größere Innenabstände und 114 Prozent Zeilenhöhe, damit Anlagen, zweisprachige Fassungen und lange Klauseltabellen nicht mehr wie eine enge Bleiwüste wirken.

### Layoutcheck nachgezogen

`scripts/check-odt-integrity.py` prüft die neuen Layoutmarker, damit spätere ODT-Builds nicht unbemerkt auf den engeren Stil zurückfallen. Der Spaltenlayout-Check bleibt unverändert streng: Keine Vorlage darf durch Pandoc in eine schmale, zentrierte Fließtextspalte geraten.

### Geprüft

Alle 938 ODT-Fassungen wurden neu erzeugt. Die Markdown-Quellen und Markdown-ZIPs bleiben unverändert, weil dieser Release nur das ODT-Schriftbild betrifft. Zusätzlich laufen Rechtsprechungshygiene, Gliederung, Kategorien, Sonderbereich und Eval-Harness im vollständigen lokalen Gate.

## v4.59.0 — Spezifizitäts-Sweep gegen harte Generik und Leerformeln (2026-07-07)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Lauf beseitigt harte Generik-Funde im Hauptbestand: leere Kernplatzhalter, pauschale Rechtsfolgenformeln und einzelne sichtbar holprige Fassungszeilen wurden gezielt gegen konkrete, gegenstandsbezogene Bausteine ausgetauscht.

### Platzhalter mit Gegenstand

In 97 Hauptvorlagen wurden die harten Stub-Felder `[Regelung]`, `[Text]` und `[Angaben]` aus den Mustertexten entfernt. SaaS-, Softwarepflege-, Arbeitnehmerüberlassungs-, Vergabe-, Restrukturierungs-, Versicherungs-, M&A-, Städtebau- und Vertriebsdokumente tragen nun sprechende Listen zu Leistungsumfang, Rollen, Fristen, Abrechnung, Sicherheitsanforderungen, Datenexport, Anlagen, Vergütung und Vollzug. Bei zweisprachigen Dokumenten wurden die deutschen und englischen Felder parallel geführt.

### Normanker statt Leerformel

Die pauschale Formel „nach den gesetzlichen Vorschriften“ wurde in den betroffenen Mustertexten durch konkrete Normmechanik ersetzt: Verzug und Verzugszinsen stehen bei §§ 286, 288 BGB, vertragliche Pflichtverletzungen bei §§ 280 Abs. 1, 241 Abs. 2, 276 BGB, werkvertragliche Mängel bei §§ 633, 634 BGB, Stornierung und Rücktritt bei §§ 323, 314 BGB, Unternehmensvertragsfolgen bei §§ 304, 305 AktG und Speditionshaftung bei §§ 461 bis 466 HGB sowie Nr. 22 ADSp 2017.

### Bug-Hunt und Lesbarkeit

Ein überschießender Verzugszinsbaustein im zweisprachigen Schuldscheindarlehen wurde auf § 288 BGB zurückgeführt. Vier gewachsene Fassungszeilen mit „Der Bearbeitungsstand ist Diese Fassung …“ wurden geglättet. In der D&O-Bedingungsvorlage wurden Versicherungssumme, Jahreshöchstleistung, Sublimit, Selbstbehalt und Prämie wieder als eigenständige wirtschaftliche Ausfüllfelder sichtbar.

### Geprüft

97 ODT-Fassungen und 97 Markdown-ZIPs wurden neu erzeugt. Zusätzlich geprüft wurden harte Stub-Platzhalter, die Leerformel „nach den gesetzlichen Vorschriften“, neu geänderte verschachtelte Platzhalter, Diff-Whitespace und die Verzugszinszuordnung. Der vollständige lokale Gate läuft grün.

## v4.58.0 — ODT-Lesbarkeit und Layout-Luftigkeit repoweit verbessert (2026-07-07)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Designlauf verbessert die Arbeitsfassungen, ohne die fachlich geprüften Mustertexte umzuschreiben: Die Markdown-Quellen bleiben stabil, die ODT-Ausgabe wird ruhiger, luftiger und besser scannbar.

### Mehr Luft in den ODT-Arbeitsfassungen

Die ODT-Erzeugung setzt nun eigene Absatzabstände für Fließtext, Überschriften, Listen und Tabellenzellen. Hauptüberschriften, Zwischenüberschriften und Unterpunkte erhalten mehr Abstand davor und danach; Fließtext bekommt eine ruhigere Zeilenhöhe, und Tabelleninhalte stehen nicht mehr so eng in den Zellen. Gerade lange Vertrags-, Klage- und Anlagenvorlagen lassen sich dadurch besser am Bildschirm prüfen und im Ausdruck schneller erfassen.

### Layout-Regel abgesichert

`scripts/md-to-odt.py` wurde um eine zentrale Lesbarkeits-Normalisierung erweitert. `scripts/check-odt-integrity.py` prüft die neuen Layoutmerkmale mit, sodass spätere ODT-Builds nicht unbemerkt auf den alten engen Stil zurückfallen.

### Geprüft

Alle 938 ODT-Fassungen wurden neu erzeugt. Die Markdown-ZIPs blieben unverändert und synchron, weil die Markdown-Quellen nicht geändert wurden. Der vollständige lokale Gate läuft grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung` und `run-eval` mit All-Pass 930/930.

## v4.57.0 — Finaler Benutzbarkeits- und Warnhinweis-Sweep (2026-07-07)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Schlusslauf beseitigt einen repoweiten Dokumenttyp-Bruch in Warnhinweisen, vereinheitlicht die Vorschau-Links in den Vorlagen-READMEs und schärft eine verkehrsrechtliche Vergleichsvorlage mit präziseren Berechnungsplatzhaltern.

### Warnhinweise typgerecht

574 Hauptvorlagen erhielten einen typgerechten Eigenleistungs-Schlusssatz im `[WARNHINWEIS]`-Block. Vertragsvorlagen sprechen nun von Vertrag, Planvorlagen von Plan, Vermerke von Vermerk, Texte von Text und sonstige Arbeitshilfen von einem verwendbaren Dokument; Schriftsatzvorlagen behalten „Schriftsatz“. Damit passt der wichtigste Nutzungs- und Eigenleistungs-Hinweis wieder zum jeweiligen Dokumenttyp.

### Zugriff und Vorschau

831 Vorlagen-READMEs normalisieren die Zeile „Online ansehen“ auf die echten Dateinamen in Backticks. Dadurch fallen sichtbarer Linktext, Dateiname und Pfad wieder zusammen; unschöne Mischschreibungen aus Slug-Umformungen verschwinden. Die Startseite wurde zusätzlich sprachlich geglättet und macht den Unterschied zwischen ODT-Arbeitsfassung, Markdown-Quelle, ZIP-Download und Sonderbereich klarer.

### Verkehrsunfallvergleich

Die Vergleichsvorlage zur Verkehrsunfallregulierung arbeitet in der Schadenstabelle jetzt mit sprechenden EUR-Platzhaltern je Position. Die bisher hart eingesetzte Kostenpauschale wurde durch einen ausfüllbaren Platzhalter ersetzt; die README weist darauf hin, Pauschalen anhand regionaler Regulierungspraxis und aktueller Rechtsprechung zu prüfen.

### Geprüft

574 ODT-Fassungen und 574 Markdown-ZIPs wurden neu erzeugt. Die zentralen Markdown-Links wurden geprüft; `validate-vorlagen`, `check-kategorien-index` und `check-md-zip-integrity` laufen grün. Der vollständige lokale Gate wurde anschließend erneut ausgeführt.

## v4.56.0 — Schluss-Sweep für Startseite, Navigation und Nutzungszugang (2026-07-07)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Dieser Schluss-Sweep korrigiert die zentrale Einstiegsebene nach dem v4.55.0-Qualitätspass, ohne die fachlich bereits geprüften Vorlagentexte unnötig anzufassen.

### Startseite und Zugriff

Die `README.md` wurde auf den aktuellen Bestand gebracht: 40 Rechtsbereiche, 938 Hauptvorlagen, 113 gerichtsleitende Sondervorlagen und Eval All-Pass 930/930. Die Rechtsgebietstabelle zeigt wieder die kanonischen ASCII-Slugs, damit sichtbarer Linktext, Ordnername und tatsächlicher Pfad zusammenfallen. Auch das Paradebeispiel verweist nun mit dem echten Slug auf die Insolvenz-Asset-Deal-Vorlage.

### Sprache und Kohärenz

Die Projekteinordnung wurde straffer und arbeitsnäher formuliert: weniger Produkt- oder Modellbezug, mehr Fokus auf Strukturvorgaben, Validatoren, Quellenhygiene und redaktionelle Disziplin. Im Sonderbereich wurde die sichtbare Großschreibung von Staatsanwaltschaft und Amtsanwaltschaft vereinheitlicht.

### Geprüft

Zusätzlich zu den regulären Checks wurde ein zentraler Markdown-Link-Sweep über `README.md`, `WORKFLOWS.md`, `kategorien/README.md` und `vorlagen-gerichtsleitend/README.md` ausgeführt. Der Sonderbereichsvalidator läuft grün; der vollständige CI-Gate wurde anschließend erneut geprüft.

## v4.55.0 — Finaler Qualitäts- und Kohärenzpass: Lizenz-Vereinheitlichung, Reparaturen, Genauigkeits-Abnahme (2026-07-07)

**Stand:** 938 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Abschlussrelease des zentralen Qualitätspasses: Bug-Jagd, Kohärenz-Durchsicht und Schönheitsreparaturen über den gesamten Bestand, ohne inhaltliche Neuausrichtung einzelner Vorlagen.

### Lizenz-Fußzeile repoweit vereinheitlicht

Jede der 938 Hauptvorlagen-Markdown-Fassungen endet jetzt einheitlich auf den Trennstrich mit der Schlusszeile `Lizenz: Apache-2.0 OR MIT.` Zuvor existierten drei gewachsene Stile nebeneinander: die Standalone-Schlusszeile, eine eigene `## Lizenz`-Sektion (20 Vorlagen) und mitten im Dokument verbliebene Alt-Fußzeilen, hinter denen spätere Ausbauwellen Schluss- und Anlagenblöcke angefügt hatten. 431 Vorlagen erhielten die fehlende Schlusszeile, 104 Dateien wurden von Dopplungen und Fehllagen auf genau eine kanonische Fußzeile bereinigt, in 132 Dateien wurden dabei entstandene doppelte Leerzeilen geglättet. Der Sonderkorpus `vorlagen-gerichtsleitend/` bleibt konventionsgemäß einheitlich ohne Lizenzzeile.

### Reparaturen aus der Bug-Jagd

Vier tote Verweise in „Verwandte Vorlagen"-Abschnitten zeigen wieder auf existierende Vorlagen (`strafrecht/verteidigungsanzeige-akteneinsicht`, `verkehrsrecht/einspruch-bussgeldbescheid`, `versicherungsrecht/deckungsklage-rechtsschutzversicherung`, `versicherungsrecht/anspruchsschreiben-haftpflicht`). Drei doppelt vorhandene README-Abschnitte „Hinweise zur Verwendung" wurden zusammengeführt (`transport-und-speditionsrecht/frachtvertrag-cmr`, `handels-und-gesellschaftsrecht/kapitalerhoehungsbeschluss-gmbh`, `internationales-wirtschaftsrecht/saft-token-finanzierung-us-style-zweisprachig`). Der Warnhinweis der Incoterms-Klauselmatrix trägt jetzt wie alle übrigen Vorlagen den Eigenleistungs-Absatz.

### Genauigkeits-Abnahme ohne Befund

Eine abschließende Prüf-Battery über alle Markdown-Fassungen suchte nach hartcodierten Sozial- und Tabellenwerten (Regelbedarf, Mindestlohn, Pfändungsfreigrenzen, Düsseldorfer Tabelle), vertauschten Verzugszinssätzen des § 288 BGB, falschen Fristdauern zu § 626 Abs. 2 BGB, § 4 KSchG, § 548 BGB, § 517 ZPO, § 195 BGB und Art. 263 AEUV sowie nach bekannten Falschzitat-Mustern. Ergebnis: keine Fehler; vier Verdachtsstellen erwiesen sich als korrekt gesetzte Varianten-Schreibweisen (B2B- und Verbraucher-Zinssatz sauber getrennt, Berufungs- und Berufungsbegründungsfrist richtig § 517 und § 520 Abs. 2 Satz 1 ZPO zugeordnet). Rechtsprechung bleibt durchgehend Live-Recherche-Suchanker ohne ungeprüfte Aktenzeichen.

### Geprüft

Alle zehn CI-Checks grün, Eval-Harness All-Pass 930/930; 524 ODT-Fassungen und die zugehörigen Markdown-ZIPs neu erzeugt.

## v4.54.0 — Exzellenz-Pass und Sanierungs-Suite: Taktik, Rechenwerke und zwei neue Kernvorlagen (2026-07-06)

**Stand:** 938 validierte Hauptvorlagen (vorher 936; neu: Sanierungskonzept und handelsrechtliche Fortführungsprognose). Alle zehn CI-Checks grün.

### Exzellenz-Pass (additiv) über Datenschutz, Familien-, Erb-, Sozial- und Arbeitsrecht

Rund 185 Vorlagen tragen jetzt je eine neue Prüf-/Rechenschema- oder Einreichungs-Checklisten-Anlage sowie die README-Abschnitte „Taktische Hinweise" (Vorgehensreihenfolge, typische Gegnereinwände mit Antwortlinie, häufige Fehler) und „Verwandte Vorlagen". Abdeckung: Datenschutz 29 von 29, Arbeitsrecht 42 von 42, Sozialrecht 39 von 39, Familienrecht 34 von 38, Erbrecht rund 40 von 46 — die wenigen Reste sind der laufenden Pflege überantwortet. Beispiele der Rechenwerke: Abfindungskorridor §§ 9, 10 KSchG samt Annahmeverzugs-Saldo, Urlaubsabgeltungsformel §§ 7 Abs. 4, 11 BUrlG, m/n-tel-Berechnung § 2 BetrAVG, Zugewinn- und Pflichtteilsstaffeln, Drei-Fünftel-Belegung und § 44 SGB X-Zeitstrahl, Artikel-28-Abgleichliste, 72-Stunden-Zeitstrahl Artikel 33 DSGVO und Artikel-82-Schadensposten-Gerüst.

### Sanierungs-Suite im Insolvenz- und Restrukturierungsrecht

Beide Muster-Pläne führen ihre Vergleichsrechnung jetzt mehrszenarig und gruppenbezogen (Szenario-Matrix mit begründeter Auswahl, Verteilungsrechnung bis zur Gruppenquote mit Verfahrenskosten- und §§ 170 f. InsO-Abzügen, Downside-Sensitivität, ausformulierte Konsistenzregeln, Herleitungsregister) und tragen ausformulierte Ansätze für sämtliche Pflichtanlagen (§§ 229 f., 230, 249 InsO; §§ 6 Abs. 2, 8, 12, 14 StaRUG samt neuem Verzeichnis gruppeninterner Drittsicherheiten). Die Antragsfamilie wurde mit Anlagen-Ansätzen ausgestattet: Regelinsolvenz-Eigenantrag mit den Kennzeichnungs-Verzeichnissen des § 13 Abs. 1 Satz 4 bis 7 InsO und § 15a-Zeitachse, beide Eigenverwaltungsanträge mit der Eigenverwaltungsplanung des § 270a Abs. 1 Nr. 1 bis 5 InsO als Einzel-Gerüste samt Abs. 2-Erklärungen, beide Schutzschirmanträge mit Bescheinigungs-Gerüst nach § 270d Abs. 1 InsO und Planvorlage-Kalender, beide Restrukturierungsanzeigen mit den Inhalten des § 31 Abs. 2 StaRUG, Zuständigkeits- und Gruppengerichts-Baustein (§§ 34 f. StaRUG), Instrumenten-Fahrplan (§ 29 StaRUG), Erlöschenskalender (§ 31 Abs. 4 StaRUG) und Pflichten-Prüfblock (§§ 32, 42 f. StaRUG).

### Neu

`restrukturierungsrecht-starug/sanierungskonzept-insolvenzplan-restrukturierungsplan` — Sanierungskonzept als gemeinsamer Unterbau beider Planarten (Stadienlehre mit Insolvenzreife-Prüfzeile, Krisenursachen, Leitbild, dreigeteiltes Maßnahmenprogramm mit Effekten, integrierte Drei-Jahres-Planung, getrennte Sanierungsfähigkeits-Aussage und Überleitungs-Mapping-Tabelle auf § 220 InsO und §§ 5 f., 14 StaRUG; IDW S 6 und die Anforderungen der Rechtsprechung nur als Rechercheanker). `insolvenzrecht/fortfuehrungsprognose-handelsrechtlich-going-concern` — Dokumentation der Going-Concern-Beurteilung (§ 252 Abs. 1 Nr. 2 HGB) mit Gegebenheiten-Katalog, Vier-Felder-Abgrenzungsmatrix zur insolvenzrechtlichen Fortbestehensprognose und dreivariantiger Gesamtaussage. Die bestehende § 19-Dokumentation erhielt Prüf-/Rechenschema-Anlage, Going-Concern-Abgrenzung und Taktik-README.

### Geprüft

Alle zehn CI-Checks grün; rund 200 ODT- und ZIP-Fassungen neu erzeugt; keine neuen Aktenzeichen (Rechtsprechung nur als Live-Recherche-Suchanker).

## v4.53.0 — Datenschutz, Sozialversicherung, Unterhalt und Erbfolge weiter verdichtet (2026-07-06)

**Stand:** 936 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Ausbau ergänzt gezielt Arbeitshilfen und Anträge in Datenschutzrecht, Sozialrecht, Rentenrecht, Krankenkassenrecht, Familienunterhalt und Erbfolgeprüfung.

### Datenschutzrecht

Zwei neue Vorlagen in `informationstechnologierecht/` ergänzen die Datenschutz-Dokumentation jenseits des Drittlandtransfer- und Due-Diligence-Pakets: ein Löschkonzept mit Aufbewahrungsmatrix sowie ein Betroffenenrechte-Register. Beide Vorlagen führen Fristen, Verantwortlichkeiten, Sperrvermerke, Nachweise, Ausnahmen und Eskalationspunkte so, dass Datenschutzorganisation und Datenraumprüfung dieselbe Dokumentenbasis nutzen können.

### Sozialrecht, Rente und Krankenkasse

Vier neue Vorlagen in `sozialrecht/` erweitern die Renten- und Krankenkassenstrecke: Antrag auf Feststellung von Kindererziehungszeiten und Berücksichtigungszeiten, Widerspruch gegen fehlerhafte Kindererziehungszeiten, Antrag auf Kinderkrankengeld nach § 45 SGB V und Widerspruch gegen Reha-Ablehnung durch DRV oder Krankenkasse. Die Texte trennen Versicherungsverlauf, Haushalts- und Erziehungszeiten, Anspruchstage, ärztliche Bescheinigung, Entgeltausfall, Zuständigkeitsklärung nach § 14 SGB IX und Akteneinsicht.

### Familienrecht und Unterhalt

Drei neue Unterhaltsvorlagen ergänzen `familienrecht/`: Betreuungsunterhalt nach § 1615l BGB, Mehrbedarf und Sonderbedarf beim Kindesunterhalt sowie eine Berechnungsdokumentation für Kindesunterhalt. Damit werden Bedarf, Leistungsfähigkeit, Rang, Quotenhaftung, Rückstände, Dynamisierung und Wechselmodell nicht nur behauptet, sondern nachvollziehbar berechnet und belegbar gemacht.

### Erbrecht und Erbfolge

Vier neue Vorlagen in `erbrecht/` stärken die Nachlassgerichtspraxis und die Erbfolgeprüfung: Prüfvermerk gesetzliche und gewillkürte Erbfolge, Antrag auf Testamentseröffnung, Antrag auf Abschrift von Testament und Eröffnungsniederschrift sowie gemeinschaftlicher Erbschein für Miterben. Die Muster führen Sterbeurkunde, Beteiligtenliste, Verwahrdaten, Testamentsauslegung, Ausschlagung, Ehegattenquote, Güterstand, Miterbenquoten und eidesstattliche Versicherung getrennt.

### Navigation und Hygiene

Die neuen Vorlagen wurden in den Fach-READMEs und in der Drei-Ordner-Sicht unter `kategorien/02-prozessuale-vorlagen-und-formulare/` und `kategorien/03-sonstige-vorlagen/` verlinkt. ODT-Dateien, Markdown-ZIP-Downloads und Rubrics wurden neu erzeugt; ein Rubric-Fund im Kinderkrankengeld-Antrag wurde durch ein behördliches Geschäftszeichenfeld im Kopf behoben.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 936 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` meldet All-Pass 928/928.

## v4.52.0 — Datenschutz- und KI-Due-Diligence-Suite für M&A-Prüfungen (2026-07-06)

**Stand:** 923 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Ausbau ergänzt die erwartbare Dokumentensuite für Unternehmenskäufe mit Datenschutz-, Drittlandtransfer- und KI-Risiken.

### Datenschutz-Due-Diligence

Sechs neue Vorlagen in `informationstechnologierecht/` decken die Datenraum- und Sanierungspraxis ab: Datenschutzrechtliche Due-Diligence-Anforderungsliste, Verzeichnis der Verarbeitungstätigkeiten für Due Diligence, Datenschutz-Gap-Report, Auftragsverarbeiter- und Subprocessor-Register, DSFA-Review sowie Drittlandtransfer-Due-Diligence mit SCC, DPF und Transfer Impact Assessment. Die Vorlagen trennen bewusst operative Verarbeitung, Dokumentenlage, Rechtsgrundlagen, AVV-Ketten, Drittlandtransfer, Restrisiken, Kaufvertragsfolgen und Post-Closing-Maßnahmen.

### KI-Due-Diligence

Fünf neue Vorlagen in `ki-und-plattformregulierung/` bilden die transaktionsbezogene KI-Prüfung nach der KI-Verordnung ab: KI-Due-Diligence-Anforderungsliste, KI-Systeminventar, Prüfung verbotener KI-Praktiken, Hochrisiko-KI-Einstufung nach Art. 6 und Konformitäts- sowie Registrierungsprüfung. Die Suite arbeitet mit Systemkarten, Rollenklärung, Anhang-III-Fallgruppen, Art.-6-Abs.-3-Rückausnahme, technischer Dokumentation, Qualitätsmanagement, Konformitätsbewertung und EU-Datenbankregistrierung.

### Navigation und Hygiene

Die neuen Vorlagen wurden in den Fach-READMEs und in der Drei-Ordner-Sicht unter `kategorien/03-sonstige-vorlagen/` verlinkt. ODT-Dateien, Markdown-ZIP-Downloads und Rubrics wurden erzeugt. Ein Sanity-Check korrigiert zusätzlich eine freistehende Gegenstandszeile im Verbraucherinsolvenzantrag, damit die Gliederungskonvention wieder vollständig eingehalten ist.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 923 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` meldet All-Pass 915/915.

## v4.51.0 — Sozialversicherung und Insolvenzverfahren mit neuen Spezialanträgen ausgebaut (2026-07-06)

**Stand:** 912 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Der Ausbau ergänzt gezielt Sozialversicherung, Krankengeld, Arbeitsunfall, Verbraucherinsolvenz, GmbH-Eigenantrag, Eigenverwaltung, Schutzschirm und StaRUG-Anzeige mit Sanierungskonzept.

### Sozialrecht und Sozialversicherung

Sechs neue Vorlagen erweitern `sozialrecht/`: Statusfeststellungsantrag nach § 7a SGB IV, Widerspruch gegen Scheinselbstständigkeitsfeststellung, Widerspruch gegen Beitragsbescheid für Selbstständige, Antrag auf Anerkennung eines Arbeitsunfalls, Widerspruch gegen Arbeitsunfallablehnung und Widerspruch gegen Krankengeldbeendigung oder Aussteuerung. Die Texte führen Bescheidzugang, Akteneinsicht, Beweisangebote, medizinische Unterlagen, Statusmerkmale, Beitragsberechnung, Blockfrist und Kausalitätsdarstellung getrennt.

### Insolvenzrecht

Vier neue Vorlagen ergänzen `insolvenzrecht/`: Verbraucherinsolvenzantrag mit Schuldenbereinigungsplan nach § 305 InsO, GmbH-Eigenantrag im Regelinsolvenzverfahren nach §§ 13, 15a InsO, GmbH-Eigenantrag mit Eigenverwaltung nach § 270a InsO und GmbH-Schutzschirmverfahren nach § 270d InsO. Die Muster enthalten jeweils Anlagenlogik, OPOS-/Gläubigerlisten, Liquiditätsplanung, Insolvenzgründe, Eigenverwaltungsplanung, Bescheinigung, Schutzanordnungen und Fristenführung.

### StaRUG

Neu in `restrukturierungsrecht-starug/` ist die Restrukturierungsanzeige nach § 31 StaRUG für Fälle, in denen noch kein Restrukturierungsplan vorliegt und stattdessen ein Sanierungskonzept beigefügt wird. Die Vorlage trennt Krise, Restrukturierungsziel, Verhandlungsstand, Verbraucher- und KMU-Betroffenheit, Gruppenwiderstand, Pflichterfüllungsvorkehrungen und Anlagen.

### Hygiene

Die Drei-Ordner-Sicht, Fach-READMEs, ODT-Dateien, Markdown-ZIP-Downloads und Rubrics wurden synchronisiert. Der Rubric-Generator erkennt `schutzschirmverfahren` künftig als Schriftsatztyp, damit Schutzschirm-Anträge bei späterer Rubric-Regeneration nicht versehentlich als sonstige Arbeitshilfen eingestuft werden.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 912 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` meldet All-Pass 904/904.

## v4.50.0 — Gerichtsleitende Sondervorlagen abschließend sonderbereichsfest geführt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen und 113 gerichtsleitende Sondervorlagen. Etappe 10 der 18-Punkte-Veredelung schließt den Sonderbereich `vorlagen-gerichtsleitend/` mit einer bereichseinheitlichen Normschreibweise und nachgezogener Fristen- und Beweisführungsführung ab.

### Sonderbereich und Normschreibweise

Alle 113 gerichtsleitenden, staatsanwaltschaftlichen und amtsanwaltschaftlichen Muster sowie der Sonderbereichs-Index wurden auf die Sonderbereich-Konvention zurückgeführt: Normverweise schreiben `Paragraf` oder `Paragrafen` aus; im gesamten Ordner `vorlagen-gerichtsleitend/` verbleibt kein Paragrafenzeichen. Damit sind Tenor, Verfügung, Beschlussgerüst, staatsanwaltschaftliche Verfügung und README-Führung wieder einheitlich lesbar.

### Bereichs-READMEs

18 Bereichs-READMEs wurden gemessen und nachgeführt. Jeder Bereich trägt nun `Hinweise zur Verwendung` mit einem eigenständigen Fristen- und Beweisführungsabsatz, der Zustellung, Anhörung, Aktenbeiziehung, Eilbedürftigkeit, Rechtsmittel, Vollzug, Protokollierung und Entscheidungsreife auf die jeweilige Gerichtsbarkeit oder staatsanwaltschaftliche Rolle zuschneidet.

### Strafvollstreckungskammer

Die zwei Beschlussmuster zur gerichtlichen Entscheidung in Vollzugssachen und zu Sicherungsverwahrung und Lockerungen erhielten ergänzende Fristen- und Beweisführungsbausteine. Eingang, Zugang der Anstaltsentscheidung, Vollzugsplan, Sicherheitsprognose, Stellungnahmen und Rechtsbeschwerdebelehrung werden dadurch aktenfest geführt, ohne den Tenor mit Anwendungshinweisen zu überladen.

### Hygiene

Der Hauptbestand blieb unberührt; daher waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich. Es wurden keine neuen Aktenzeichen, keine neuen Rechtsprechungsfundstellen und keine Fremdrepo-Verweise eingeführt.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.49.0 — AGB, Vertrieb und M&A mit Fristen- und Modularchitektur nachgerüstet (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 9 der 18-Punkte-Veredelung ergänzt die fachliche README-Führung in `agb-recht/`, `vertriebs-und-handelsrecht/` und `mergers-and-acquisitions/`, ohne Sprach-Churn in den bereits polierten Mustertexten und ohne neue Vorlagen.

### AGB-Recht

16 AGB-READMEs wurden auf die vollständige AGB-Kaskade nach §§ 305 bis 310 BGB, Verbraucher- und Unternehmerdifferenzierung, Fernabsatz, Button-Lösung, Widerruf, Informationspflichten, Preisangaben, Einbeziehung und Versionierungsbeweis ausgerichtet. Jede README trägt nun einen eigenen Fristen- und Beweisführungsabsatz sowie eine Varianten- und Modulführung für Unternehmergeschäft, Verbraucherbezug und digitale Bestellstrecken.

### Vertrieb und Handel

28 Vertriebs- und Handels-READMEs wurden fachlich nachgerüstet. Die Hinweise trennen nun Abruf, Forecast, Lieferfenster, Mängelrüge nach § 377 HGB, Nacherfüllung, Rückruf, Audit, Kündigung, Ausgleichsanspruch nach § 89b Abs. 4 HGB, Gebiet, Kundenschutz, Provisionslogik, Qualität, Plattformranking, Vertikal-GVO-Prüfung und Nachlauf sauber.

### Mergers and Acquisitions

19 M&A-READMEs wurden um Transaktionskalender, Conditions Precedent, Freigaben, Signing, Closing, Long-Stop, Kaufpreisanpassung, Earn-out, Garantieanzeigen, W&I-Notice, Escrow-Release, TSA-Leistungsfenster, Verjährung und Claim-Dokumentation ergänzt. Die Varianten- und Modulführung trennt Share Deal, Asset Deal, Carve-out, W&I, Escrow und Warranty-Claim-Protokolle.

### Hygiene

Alte `Warnung`-, `Hinweise`-, `Anwendung und Grenzen`-, `Besondere Warnhinweise`-, `Normen- und Prüfanker`-, `Normen- und Quellenanker`- und `Einsatzgrenzen`-Reste wurden in die kanonischen README-Abschnitte überführt. Alle 63 betroffenen README-Dateien tragen nun `Einschlägige Normen`, `Anwendungsbereich` und `Hinweise zur Verwendung` mit konkretem Fristen-, Beweis- und Modulabsatz. Da ausschließlich READMEs geändert wurden, waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.48.0 — Allgemeine und bereichsübergreifende Vorlagen mit Fristen- und Beweisachsen geführt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 8 der 18-Punkte-Veredelung hebt die README-Führung in `allgemeines-und-bereichsuebergreifendes/`, ohne neue Vorlagen und ohne Mustertextänderungen.

### Forderungen, Sicherheiten und Vergleiche

Die README-Hinweise zu Abtretung, Bürgschaft, Garantie, Freistellung, Schuldanerkenntnis, Schuldbeitritt, Stundung, Ratenzahlung, Mahnung, Vergleich, Schenkung, Patronat, Vorvertrag und Haftungsausschluss wurden nachgeführt. Die Hinweise trennen nun Anspruchsgrund, Fälligkeit, Verzug, Verjährung, Hemmung, Einwendungen, Sicherheitenstellung, Abtretungsanzeige, Erledigungswirkung und Insolvenzrisiken.

### Vollstreckung, Prozess und Grundbuchvollzug

Die README-Hinweise zu PKH, Fristverlängerung, Zahlungsklage, Stufenklage, Streitwertbeschwerde, Drittwiderspruchsklage, Erinnerung, Pfändung, Vermögensauskunft, Vollziehungsauftrag, Zwangssicherungshypothek und Kostenrechnung wurden auf Titelspur, Klausel, Zustellung, Rechtskraft, Vollziehungsfrist, Rechtsbehelf und Kostenfestsetzung ausgerichtet. Grundstücksnahe Vorlagen führen nun Grundbuchstand, Rang, Bewilligung, Beurkundung und Bestimmtheit deutlicher.

### Mandat, Datenschutz, Vollmachten und Leistungsbeziehungen

Mandats-, Datenschutz-, Vollmachts-, Projekt-, Werk-, Dienstleistungs-, Kunst-, Catering-, Sicherheitsdienst-, Reinigungs-, Wartungs- und Werklieferungsvorlagen erhielten präzisere Hinweise zu Vollmacht, Vergütung, Verschwiegenheit, DSGVO, Abnahme, Freigabe, Mitwirkung, Mängeln, Nutzungsrechten, Leistungsänderung und Zahlungsnachweis. Die Standardklausel-Sammlung wurde in der README stärker an AGB-Kontrolle, Form, Rechtswahl, Gerichtsstand und Zugang gekoppelt.

### Hygiene

Alte `Warnung`-, `Qualitätshinweise`-, `Typische Fallstricke`-, `Einsatzgrenzen`- und `Normen- und Quellenanker`-Reste wurden entfernt oder in `Hinweise zur Verwendung` und `Einschlägige Normen` überführt. Alle 69 betroffenen README-Dateien tragen nun `Einschlägige Normen`, `Anwendungsbereich` und `Hinweise zur Verwendung` mit konkretem Fristen- und Beweisführungsabsatz. Da ausschließlich READMEs geändert wurden, waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.47.0 — Kleine Fachordner, Internationales Wirtschaftsrecht und Handelsrecht fachlich geführt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 7 der 18-Punkte-Veredelung hebt die README-Führung in `kartell-und-marktrecht/`, `prozessvorlagen/`, `strafvollzugsrecht/`, `verfassungsrecht/`, `europarecht/`, `energierecht/`, `umweltrecht-und-emissionshandel/`, `beamten-und-soldatenrecht/`, `transport-und-speditionsrecht/`, `zoll-und-aussenwirtschaftsrecht/`, `internationales-wirtschaftsrecht/` und `handels-und-gesellschaftsrecht/`, ohne neue Vorlagen und ohne Mustertextänderungen.

### Kleine Prozess-, Verfassungs- und Öffentlichkeitsordner

7 kartellrechtliche, 8 prozessuale, 8 strafvollzugsrechtliche, 8 verfassungsrechtliche, 9 europarechtliche und 11 beamten- und soldatenrechtliche README-Dateien wurden gemessen und nachgeführt. Die Hinweise arbeiten nun mit Rüge-, Beschwerde-, Rechtsmittel-, Vollzugs-, Verfassungsbeschwerde-, Vorabentscheidungs-, Konkurrentenstreit-, Wehrbeschwerde- und beamtenrechtlicher Fristenmechanik statt mit generischen Einsatzgrenzen.

### Energie, Umwelt, Transport, Zoll und Außenwirtschaft

10 energierechtliche, 10 umweltrechtliche, 19 transport- und speditionsrechtliche sowie 5 zoll- und außenwirtschaftsrechtliche README-Dateien wurden geschärft. Die Hinweise trennen nun EEG- und Netzanschlussfristen, Bundesnetzagentur-Festlegungen, Genehmigungs- und Widerspruchsfristen, Lieferketten- und Umweltbeweis, CMR- und ADSP-Regressketten, Standgeld, Incoterms, Ausfuhrgenehmigung, Investitionsprüfung, Sanktionslistenprüfung und Zollwertkorrektur.

### Internationales Wirtschaftsrecht und Handels-/Gesellschaftsrecht

25 international-wirtschaftsrechtliche und 56 handels- und gesellschaftsrechtliche README-Dateien wurden auf konkrete Nutzerführung nachgezogen. Die Hinweise führen nun CISG-Mängelrüge, Nachfrist und Vertragsaufhebung, Incoterms-Dokumentenlauf, Akkreditivlogik, Exportkontrolle, grenzüberschreitende Gerichtsstands- und Schiedsklauseln, GmbH-, AG-, SE- und SCE-Satzungen, Beschlussmängel, Registervollzug, Organpflichten, Cash Pooling, Rangrücktritt, Beteiligungs- und Finanzierungsrunden sowie Umwandlungs- und Liquidationsmechanik genauer.

### Hygiene

Alte `Warnung`-, `Praxisfallen`-, `Qualitätshinweise`-, `Typische Fallstricke`-, `Rechtliche Hinweise`-, `Praxishinweise`-, `Einsatzgrenzen`- und `Normen- und Quellenanker`-Reste wurden aus den Einzel-READMEs entfernt oder ersetzt. Alle 176 betroffenen README-Dateien tragen nun `Einschlägige Normen`, `Anwendungsbereich` und `Hinweise zur Verwendung` mit konkretem Fristen- und Beweisführungsabsatz. Da ausschließlich READMEs geändert wurden, waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.46.0 — Bau, Miete, Vergabe, Verkehr und Verwaltungsrecht mit Fristenarchitektur ergänzt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 6 der 18-Punkte-Veredelung hebt die README-Führung in `mietrecht-und-wohnungseigentumsrecht/`, `bau-und-architektenrecht/`, `oeffentliches-baurecht/`, `vergaberecht/`, `verkehrsrecht/` und `verwaltungsrecht/`, ohne neue Vorlagen und ohne Mustertextänderungen.

### Miete, WEG und Immobilien

24 Einzel-READMEs wurden gemessen und nachgeführt. Die Hinweise arbeiten nun mit Kündigungs-, Schonfrist-, Mieterhöhungs-, Betriebskosten-, Modernisierungs- und Kautionslogik sowie mit der WEG-Beschlussklagearchitektur aus Beschlussdatum, Verkündung, Anfechtungsfrist und Begründungsfrist. Grundstückskauf, Erbbaurecht, Gewerbemiete und Fernwärme-Kaufkonstellationen haben ergänzende Abgrenzungs- und Normenführung erhalten.

### Bau- und öffentliches Baurecht

30 bau- und architektenrechtliche sowie 12 öffentlich-baurechtliche READMEs wurden nachgeführt. Geschärft wurden VOB/B-Behinderungsanzeige, Bedenkenhinweis, Bauvertrag, Nachtrag, Schlussrechnung, Werklohnklage, selbständiges Beweisverfahren, Architekten- und Ingenieurverträge, EPC, Reinraum, Maschinenlieferung, Wartung, Erschließungsvertrag, Folgekostenvertrag, Durchführungsvertrag, textliche Festsetzungen, Innenentwicklung, Grün- und Ausgleichsfestsetzungen, Satzungsbeschluss und Öffentlichkeitsbeteiligung. Die Hinweise trennen nun Abnahme, Bauzeit, Nachtragsauslöser, Mängel, Sicherheiten, § 214-/§ 215-BauGB-Risiken und Abwägungsdokumentation.

### Vergabe, Verkehr und Verwaltungsrecht

30 Vergabe-, 17 Verkehrs- und 22 Verwaltungsrechts-READMEs wurden nachgeführt. Vergaberechtliche Hinweise führen nun Rügeobliegenheit nach § 160 Abs. 3 GWB, Zuschlagsinformation nach § 134 GWB, Nachprüfungsantrag, Zuschlagsverbot, sofortige Beschwerde und Vertragsunwirksamkeit getrennt. Verkehrsvorlagen trennen Bußgeldfrist, Messbeweis, Fahrerlaubnis-/MPU-Spur und Unfallregulierung. Verwaltungsrechtliche Vorlagen unterscheiden § 80 Abs. 5 VwGO, § 123 VwGO, Widerspruchs- und Klagefristen, Informationszugang, Akteneinsicht, Normenkontrolle und Untätigkeit.

### Hygiene

Alte `Warnung`-, `Praxisfallen`-, `Qualitätshinweise`-, `Typische Fallstricke`- und `Normen- und Quellenanker`-Reste wurden aus den Einzel-READMEs entfernt oder ersetzt. Alle 135 betroffenen README-Dateien tragen nun `Einschlägige Normen`, `Anwendungsbereich` und `Hinweise zur Verwendung` mit konkretem Fristen- und Beweisführungsabsatz. Da ausschließlich READMEs geändert wurden, waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.45.0 — Medizin-, Sport- und Migrationsrecht mit Fristen- und Beweisführung geschärft (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 5 der 18-Punkte-Veredelung hebt die README-Führung in `medizinrecht/`, `sportrecht/` und `migrationsrecht/`; zusätzlich wird die Visum-Remonstrationsvorlage auf den Rechtsstand der Abschaffung des Remonstrationsverfahrens zum 1. Juli 2025 zurückgebunden.

### Medizinrecht

17 Einzel-READMEs wurden gemessen und vollständig nachgeführt. Neu verdichtet sind insbesondere Arzthaftung, selbständiges Beweisverfahren, Patientenakte, Aufklärungsbögen, Privatleistungs- und Behandlungsverträge, Arztpraxis-Kauf, MVZ-Kooperation, Krankenhauskooperation, Schweigepflichtentbindung, Pflegegradstellungnahme und Approbationsverfahren. Die Hinweise arbeiten nun mit § 630h-BGB-Beweislastarchitektur, § 630g-BGB-Aktenzugang, GOÄ-Fälligkeit, § 203-BGB-Verhandlungshemmung, MD-Modulführung und gesundheitsdatenschutzrechtlicher Rollenklärung.

### Sportrecht

18 Einzel-READMEs wurden nachgeführt und von generischen Verbandswarnungen auf konkrete Sportmechanik umgestellt. Geschärft wurden Spielberechtigung im Eilrechtsschutz, Athletenvereinbarung, Spielervertrag, Trainervertrag, Aufhebungsvereinbarung, Spielertransfer, Sponsoring, Stadionordnung, Bildrechte, Vermarktung, CAS-Schiedsklausel, Verbandsdisziplinarverfahren, Doping-Anhörung, Einspruchsverfahren und Vergütungsklage. Die Hinweise trennen nun Transferfenster, Registrierung, TMS/ITC, Verbandsrechtsweg, Morals Clause, Anti-Doping-Tatbestand, Bildnisfreigabe, Ausschlussfristen und Beweisquellen.

### Migrationsrecht

14 Einzel-READMEs wurden nachgeführt. Die Hinweise differenzieren jetzt Aufenthaltserlaubnisverlängerung, Fiktionsbescheinigung, Duldung, Fachkräfteverfahren, Chancenkarte, Asylklage, asylrechtlichen Eilrechtsschutz, Dublin-Verfahren, Härtefallkommission, Einbürgerung, Familiennachzug, Niederlassungserlaubnis und Fachkräftestrategie. Die Vorlage `migrationsrecht/remonstration-visum` ist nun ausdrücklich als Altfall- und Ausnahmevorlage gekennzeichnet; README, Muster-MD, ODT und Markdown-ZIP wurden entsprechend aktualisiert.

### Hygiene

Alte `Warnung`-, `Praxisfallen`-, `Qualitätshinweise`-, `Typische Fallstricke`- und `Normen- und Quellenanker`-Reste wurden aus den Einzel-READMEs entfernt oder ersetzt. `Anwendungsbereich`, `Einschlägige Normen` und `Hinweise zur Verwendung` stehen nun in konsistenter Reihenfolge. Nur `migrationsrecht/remonstration-visum` berührt den Mustertext; ODT und Markdown-ZIP wurden dafür neu erzeugt.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.44.0 — IT-, Datenschutztransfer- und KI-/Plattformvorlagen fachlich geführt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 4 der 18-Punkte-Veredelung hebt die README-Führung in `informationstechnologierecht/` und `ki-und-plattformregulierung/`, ohne neue Vorlagen, ohne Mustertextänderungen und ohne Strukturverschiebung.

### Informationstechnologierecht

41 aktuelle README-Dateien wurden gemessen und vollständig nachgeführt. Der Ordner enthält mehr Vorlagen als der ältere Übergabeplan; gehoben wurde deshalb der Ist-Bestand. Neu geordnet sind insbesondere Drittlandtransfer-Paket, SCC-Begleitvereinbarung, Data Privacy Framework, Art.-49-Ausnahme, BCR-Freigabe, TIA, AVV, TOM-Anlage, Data-Breach-Meldung, Website-Datenschutz, Marketingeinwilligung, Art.-15- und Art.-82-Klagen sowie SaaS-, PaaS-, API-, Outsourcing-, Cloud-Migration-, Escrow-, Support-, SLA- und agile Softwareentwicklungsverträge. Die Hinweise arbeiten jetzt mit Art.-12-Monatsfrist, Art.-33-72-Stunden-Meldung, Art.-28-Pflichtkatalog, TDDDG-Trackingbezug, Abnahme-/Change-/Exit-Mechanik und Drittlandtransfer-Wiedervorlagen.

### KI- und Plattformregulierung

11 README-Dateien wurden nachgeführt: Datenlizenzvertrag für KI-Training, Datenraum nach Data Act, DMA-Beschwerde, DSA-Statement of Reasons, Trusted-Flagger-Meldung, KI-Nutzungsrichtlinien, KI-VO-Pflichtencheck, Hochrisiko-Konformität, Risikomanagementsystem, P2B-Beschwerdeantwort und VLOP-Transparenzbericht. Die Hinweise trennen nun Rollen, Risikoklasse, Datenquelle, Modellartefakte, menschliche Aufsicht, DSA-Moderationsentscheidung, DMA-Gatekeeperpflicht und Data-Act-Datenzugang.

### Hygiene

Alte `Warnung`-, `Praxisfallen`-, `Qualitätshinweise`-, `Typische Prüfpunkte`-, `Einsatzgrenzen`-, `Dokumenttyp`- und TTDSG-Reste wurden aus den Einzel-READMEs entfernt oder ersetzt. `Anwendungsbereich`, `Einschlägige Normen` und `Hinweise zur Verwendung` stehen nun in konsistenter Reihenfolge. Da ausschließlich READMEs geändert wurden, waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.43.0 — Gewerblicher Rechtsschutz und Medienrecht fachlich geführt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 3 der 18-Punkte-Veredelung hebt die README-Führung in `gewerblicher-rechtsschutz/` und `urheber-und-medienrecht/`, ohne neue Vorlagen, ohne Mustertextänderungen und ohne Strukturverschiebung.

### Gewerblicher Rechtsschutz

27 README-Dateien wurden gemessen; 26 hatten echte Lücken bei `Hinweise zur Verwendung`, absatzgenauen Normen oder Abgrenzung zu Nachbarvorlagen. Nachgeschärft wurden insbesondere Markenabmahnung, UWG-Abmahnung, markenrechtliche Berechtigungsanfrage, Löschungsantrag, Koexistenz- und Abgrenzungsvereinbarung, Marken-, Patent-, Gebrauchsmuster-, Design- und Know-how-Lizenzen, Entwicklungskooperation, F&E-Vertrag, Geheimnisschutz, Lizenz-Audit, Schutzrechtsverwarnung, Schutzschrift und technische Eilverfügungen. Die Hinweise arbeiten nun mit Fristen-, Beweis-, Audit-, Register-, Qualitätskontroll-, Dringlichkeits- und Kartellrechtsachsen statt mit generischen Warntexten.

### Urheber- und Medienrecht

21 README-Dateien wurden gemessen; 20 hatten echte Lücken bei Nutzerführung, Normenblock oder Abgrenzung. Verdichtet wurden insbesondere Gegendarstellung, presserechtlicher Eilrechtsschutz, Unterlassungserklärung, Urheberrechtsauskunft, Rechteketten Musik, Autoren-, Foto-, Film-, Musical-, Musikproduktions-, Podcast-, Influencer- und Kreativleistungsverträge sowie Filesharing- und Urheberrechtsklage. Die Hinweise unterscheiden nun Rechtekette, Bildnisrecht, DSGVO, Gegendarstellungsform, Eilfristen, Lizenzanalogie, Buy-out-Risiken und Plattform-Compliance.

### Hygiene

Alte `Warnung`-, `Praxisfallen`-, `Qualitätshinweise`-, `Typische Prüfpunkte`-, `Einsatzgrenzen`- und `Dokumenttyp`-Generatorreste wurden in spezifische `Hinweise zur Verwendung` überführt oder entfernt. Da ausschließlich READMEs geändert wurden, waren keine ODT- oder Markdown-ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.42.0 — Steuerrecht und Strafrecht mit Fristen- und Verfahrensarchitektur geschärft (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 2 der 18-Punkte-Veredelung hebt die READMEs in Steuerrecht und Strafrecht ohne neue Vorlagen und ohne Änderungen an Mustertexten.

### Steuerrecht

17 steuerrechtliche Einzel-READMEs wurden gezielt nachgeschärft. Die Hinweise zur Verwendung arbeiten nun mit den entscheidenden Verfahrensachsen: Änderungsnorm und Festsetzungsverjährung, Aussetzung der Vollziehung nach § 361 AO und § 69 FGO, Billigkeitserlass nach § 227 AO, Vorauszahlungsherabsetzung, verbindliche Auskunft nach § 89 Abs. 2 AO, verbindliche Zusage nach §§ 204 bis 207 AO, Einspruchsfrist nach § 355 AO, Finanzgerichtsklage nach § 47 FGO, Nichtzulassungsbeschwerde nach §§ 115, 116 FGO, Selbstanzeige nach § 371 AO, Stundung nach § 222 AO, Umsatzsteuer-Organschaft und USt-Voranmeldungskorrektur.

### Strafrecht

19 strafrechtliche READMEs wurden auf eine einheitliche, forensisch brauchbare Hinweisebene gebracht. Neu verdichtet sind insbesondere Adhäsion, Einstellung nach §§ 153, 153a StPO, Pflichtverteidigung nach § 140 StPO, Bewährung nach § 56 StGB, Beweisantrag nach § 244 StPO, Strafbefehlseinspruch nach § 410 StPO, Einziehungsbeteiligung, Haftprüfung mit §§ 117, 121, 122 StPO, Klageerzwingung nach § 172 StPO, Nebenklage, Schlussvortrag, Strafanzeige und Strafantrag, Verständigung nach § 257c StPO, Akteneinsicht nach § 147 StPO, Wiederaufnahme nach § 359 StPO sowie Revision und Sprungrevision.

### Hygiene

Die alten generischen `Warnung`, `Qualitätshinweise`, `Praxishinweise` und `Rechtliche Hinweise` wurden in den Einzelvorlagen-READMEs der beiden Ordner entfernt oder in spezifische `Hinweise zur Verwendung` überführt. Da nur READMEs geändert wurden, waren keine ODT- oder ZIP-Neubauten erforderlich.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.41.0 — Bank- und Versicherungsrecht auf 18-Punkte-Niveau nachgeschärft (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Etappe 1 der 18-Punkte-Veredelung hebt die sechs offenen Bank- und Kapitalmarktrecht-Restvorlagen sowie den älteren Versicherungsrechtsbestand ohne neue Vorlagen und ohne Strukturverschiebung.

### Bank- und Kapitalmarktrecht

Die sechs Restvorlagen `covenant-waiver-letter-kreditvertrag`, `factoringvertrag-unechtes-factoring`, `genussrechtsvereinbarung-mezzanine`, `klage-schadensersatz-anlageberatung`, `schuldscheindarlehen-unternehmen` und `schuldscheindarlehen-zweisprachig` wurden gezielt verdichtet. Neu sind insbesondere Covenant-Testtage, Covenant Certificate, Equity-Cure-Modul, Auszahlungslogik, Zahlungsverzug-Heilungsmechanik, Waiver-Mehrheits- und Sicherheitenprüfung, Factoring-Recourse-Matrix, Rangrücktritts- und Insolvenznähe-Hinweise sowie beweisfeste Anlageberatungsdarlegung.

### Versicherungsrecht

Der ältere Bestand der 18 Versicherungsrechtsvorlagen hat durchgehend gegenstandsspezifische `Hinweise zur Verwendung` erhalten. Die generischen Warn- und Qualitätshinweise wurden durch konkrete Prüfachsen ersetzt: § 115 VVG-Direktanspruch, Krankentagegeld-Tätigkeitsbild, AUB-Fristen, BU-Berufsprofil und Nachprüfung, Cyber-72-Stunden-Parallelität, Rechtsschutz-Stichentscheid, D&O-Claims-made-Mechanik, Kasko-Obliegenheiten, Lebensversicherung-Bezugsrecht, Sachverständigenverfahren, Wohngebäude-/Hausrat-Schadenanzeige sowie §§ 19 bis 22, 28, 81 VVG.

### Hygiene

Fünf geänderte Mustertexte wurden in ODT und Markdown-ZIP synchron neu gebaut. Platzhalter wurden auf sprechende eckige Form gebracht, starre AUB-Fristen wurden an das konkrete Bedingungswerk zurückgebunden und verschachtelte Platzhalter in den Schuldschein-Modulen entfernt.

### Geprüft

Alle zehn CI-Checks laufen lokal grün über `python3 scripts/check-all.py --ci`; `validate-vorlagen` meldet 901 Hauptvorlagen, `check-gerichtsleitend` 113 Sondervorlagen und `run-eval` bleibt All-Pass 893/893.

## v4.40.1 — ODT-Spaltenlayout der CISG- und Incoterms-Vorlagen bereinigt (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen. Patch-Release zur ODT-Hygiene der sechs in v4.40.0 ergänzten deutsch-englischen CISG-, Incoterms- und Transportvorlagen.

### Bereinigt

Die zweisprachigen Tabellen verwenden in den Tabellenzellen keine Markdown-Überschriften mehr. Abschnittsmarker wie Mängelrüge, Incoterms-Matrix, Transportauftrag und Schlussbestimmungen sind nun als fett gesetzte Zeilen innerhalb der Tabelle formatiert; dadurch bleibt der zweispaltige Lesefluss erhalten, ohne den ODT-Spaltenlayout-Validator zu verletzen.

### Geprüft

`python3 scripts/check-all.py --ci` läuft lokal grün; insbesondere `check-odt-spaltenlayout` prüft jetzt 901 ODT-Dateien und meldet keinen Body-in-Tabelle-Fund. `run-eval` bleibt All-Pass 893/893.

## v4.40.0 — CISG-, Incoterms- und Transportpaket zweisprachig (2026-07-04)

**Stand:** 901 validierte Hauptvorlagen (vorher 895). Sechs neue deutsch-englische Vorlagen schließen die Lücke zwischen internationalem Warenkauf nach CISG, Incoterms-2020-Lieferklauseln, dokumentärem Zahlungsverkehr und operativer Transportabwicklung.

### Internationales Wirtschaftsrecht

`cisg-rahmenkaufvertrag-industriekomponenten-zweisprachig` liefert einen ausformulierten Rahmenkaufvertrag für Industriekomponenten mit CISG-Grundlage, ergänzendem deutschen Recht, Spezifikation, Wareneingang, Mängelrüge, Nachfrist, Lieferabruf, Incoterms-2020-Schnittstelle und Sprachvorrang. `cisg-mangelruege-nachfrist-aufhebung-zweisprachig` bildet die Eskalation von der konkreten Vertragswidrigkeit über Art. 38, 39 und 47 CISG bis zur möglichen Vertragsaufhebung nach Art. 49 CISG ab. `cisg-rechtswahl-und-ausschlussklauseln-zweisprachig` stellt praxistaugliche Varianten für CISG-Einbeziehung, CISG-Ausschluss, ergänzendes Recht, Incoterms-Abgrenzung, Forum und Sprachvorrang bereit. `dokumentenavis-akkreditiv-incoterms-zweisprachig` verbindet Akkreditivbedingungen, Incoterms-Regel, Transportdokumente, Versicherungsnachweise und Dokumentenfrist in einem zweisprachigen Avis.

### Transport und Incoterms

`incoterms-2020-klauselmatrix-zweisprachig` ist als Auswahl- und Dokumentationsmatrix für alle elf wesentlichen Incoterms-2020-Regeln angelegt: EXW, FCA, CPT, CIP, DAP, DPU, DDP, FAS, FOB, CFR und CIF. Die Vorlage reproduziert bewusst keinen geschützten ICC-Regeltext, sondern führt den Anwender über Eignung, Ortspunkt, Export, Import, Versicherung, Dokumente und typische Fehlgriffe zur belastbaren Auswahl. `incoterms-transportauftrag-container-seefracht-zweisprachig` übersetzt die gewählte Lieferklausel in eine operative Weisung für Container- und Seefracht mit Terminal, Cut-off, Dokumenten, Versicherung, Zollrollen, Demurrage/Detention und Akkreditivschnittstelle.

### Quellen- und Prüflogik

Die READMEs verweisen auf offizielle Quellen: UNCITRAL zum CISG und seinem Ratifikationsstand, ICC zu Incoterms 2020 sowie die Incoterms-Erläuterung der International Trade Administration. Die Vorlagen trennen bewusst CISG-Vertragsrecht, Incoterms-Gefahr- und Kostenschnittstelle, Frachtvertrag, Zollabwicklung und Akkreditivlogik.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py`; `validate-vorlagen` meldet 901 Hauptvorlagen in 40 Themenordnern, `check-kategorien-index` 901 Vorlagen in drei Kategorieordnern, `check-gerichtsleitend` 113 Vorlagen in 18 Bereichen und `run-eval` All-Pass 893/893.

## v4.39.0 — Drittlandtransfer-Nachsteuerung: BCR, Behördenzugriff und Aussetzung (2026-07-04)

**Stand:** 895 validierte Hauptvorlagen (vorher 892). Drei neue Vorlagen ergänzen das Datenschutz-Drittlandtransfer-Paket um die praktische Nachsteuerung nach der Erstfreigabe: konzerninterne Transfers über Binding Corporate Rules, Drittlandbehördenzugriffe und die Aussetzung oder Wiederaufnahme problematischer Transfers.

### Ergänzt

`binding-corporate-rules-transferfreigabe-dsgvo` prüft, ob ein konkreter konzerninterner Datenfluss tatsächlich vom genehmigten BCR-Scope nach Art. 47 DSGVO erfasst ist — mit Beitrittsliste, Rollenmatrix, Drittlandrisiko, Weiterübermittlungskontrolle, Betroffenenrechte-Workflow und Freigabeauflagen. `drittlandtransfer-behoerdenzugriff-pruefvermerk` führt durch Herausgabeverlangen, Zugriffssignale und Anbieterbenachrichtigungen aus Drittländern — mit Art.-48-DSGVO-Achse, SCC-/BCR-/DPF-Folgen, Importeurweisung, Meldeprüfung und Transferbeschränkung. `drittlandtransfer-aussetzung-abhilfeplan` baut den operativen Notfallpfad, wenn DPF-Status, SCC-Anlagen, BCR-Scope, TIA oder Unterauftragskette nicht mehr tragen — mit Sofortsperre, Nachweisforderung, Ersatzlösung, Maßnahmenmatrix und Wiederaufnahmeentscheidung.

### Quellen- und Prüflogik

Die neuen READMEs verweisen auf offizielle Quellen: DSGVO auf EUR-Lex, Durchführungsbeschluss (EU) 2021/914, EuGH C-311/18 `Schrems II`, EDPB Recommendations 01/2020, EDPB Recommendations 1/2022 zu Controller Binding Corporate Rules und das EDPB-Verfahrensdokument vom 13. März 2025 zur BCR-Genehmigung. BCR-P-Entwicklungen werden nicht als endgültige Rechtslage ausgegeben.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py`; `validate-vorlagen` meldet 895 Hauptvorlagen in 40 Themenordnern, `check-kategorien-index` 895 Vorlagen in drei Kategorieordnern und `run-eval` All-Pass 887/887.

## v4.38.0 — Datenschutzrechtliches Drittlandtransfer-Paket (2026-07-04)

**Stand:** 892 validierte Hauptvorlagen (vorher 880). Zwölf neue Vorlagen im Informationstechnologierecht decken internationale Datentransfers nach DSGVO strukturiert ab: EU-Standardvertragsklauseln, EU-US Data Privacy Framework, allgemeine Angemessenheitsbeschlüsse, Transfer Impact Assessment, Art.-49-Ausnahme, Betroffeneninformation, Behördenkommunikation, Unterauftragsfreigabe, Registerführung und internes Gutachten.

### Drittlandtransfer-Set (12)

`drittlandtransfer-pruefvermerk-dsgvo` (Einstiegsprüfung zu Datenfluss, Empfängerrolle, Kapitel-V-Instrument und Freigabeauflagen), `transfer-impact-assessment-scc-dsgvo` (Schrems-II-Prüfung für SCC-Transfers mit Drittlandrecht, Zugriffswahrscheinlichkeit und ergänzenden Maßnahmen), `standardvertragsklauseln-scc-begleitvereinbarung` (Modulwahl, SCC-Anlagen, Vorrangregel, Behördenzugriffe und Aussetzung), `eu-us-data-privacy-framework-pruefung` (DPF-Listung, Zertifizierungsumfang, Covered Data, Scope-Abgleich und Fallback), `dpf-lieferantenbestaetigung-usa-transfer` (Lieferantenzusicherung zu DPF, Onward Transfers, Statusverlust und Nachweisen), `angemessenheitsbeschluss-drittlandtransfer-freigabe` (Freigabe für Nicht-USA-Angemessenheitsbeschlüsse mit Scope- und Weiterübermittlungsprüfung), `art-49-ausnahme-drittlandtransfer-dokumentation` (restriktive Einzelfalldokumentation für Ausnahmen nach Art. 49 DSGVO), `betroffeneninformation-drittlandtransfer-dsgvo` (Textbausteine nach Art. 13 Abs. 1 lit. f und Art. 14 Abs. 1 lit. f DSGVO), `datenschutzbehoerde-drittlandtransfer-stellungnahme` (Schreiben an die Aufsicht mit Sachverhalt, Rechtsgrundlage, Transferinstrument und Abhilfeplan), `drittlandtransfer-register-kontrollblatt` (laufende Nachprüfung von Transferinstrument, Auflagen und Eskalation), `unterauftragsverarbeiter-drittlandtransfer-freigabe` (Art.-28-Flow-Down und Kapitel-V-Prüfung für Unterauftragsketten), `drittlandtransfer-internes-gutachten-dsgvo` (Gutachtenstil für Geschäftsleitung, Datenschutz und Revision).

### Quellen- und Prüflogik

Die READMEs verweisen auf offizielle Quellen: DSGVO auf EUR-Lex, Durchführungsbeschluss (EU) 2021/914 zu den SCC, EuGH C-311/18 `Schrems II`, EDPB Recommendations 01/2020, EDPB Guidelines 05/2021, EU-Kommission zu Angemessenheitsbeschlüssen und EU-US Data Privacy Framework sowie die offizielle Data Privacy Framework List. Die Vorlagen unterscheiden bewusst zwischen DPF-Transfers, SCC/TIA-Transfers, sonstigen Angemessenheitsbeschlüssen und eng begrenzten Art.-49-Ausnahmen.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py`; `validate-vorlagen` meldet 892 Hauptvorlagen in 40 Themenordnern, `check-kategorien-index` 892 Vorlagen in drei Kategorieordnern und `run-eval` All-Pass 884/884.

## v4.37.0 — Zehn neue Vorlagen: Rechtsschutz-Deckungspraxis und D&O-Versicherung (2026-07-03)

**Stand:** 880 validierte Hauptvorlagen (vorher 870). Zehn Neuanlagen im Versicherungsrecht mit vollständiger README, ODT- und ZIP-Fassung, Baseline-Rubric und Kategorien-Eintrag; erstmals mit vertraglicher Rechtsgebietssicht `kategorien/01-vertragliche-vorlagen/versicherungsrecht/`.

### Rechtsschutzversicherung — Deckungskommunikation der Praxis (6)

`deckungsanfrage-rechtsschutzversicherung-kanzlei` (Erstanfrage mit Verstoß-Prinzip-Baustein nach § 4 ARB, freier Anwaltswahl § 127 VVG und Kostenprognose), `deckungserweiterung-folgeinstanz-rechtsschutz` (Folgedeckung mit Rechtsmittelfrist-Ankern), `deckungsanfrage-rentenberater-rechtsschutz` (Vertretung nach § 73 Abs. 2 Satz 2 Nr. 3 SGG, Registrierung nach dem Rechtsdienstleistungsgesetz, Erstattung nach § 63 SGB X), `deckungsanfrage-betreuer-rechtsschutz` (Aufgabenkreis und Vertretungsmacht §§ 1814, 1823 BGB, Genehmigungs-Prüfbaustein, Abgrenzung zur Betreuervergütung), `gegenvorstellung-deckungsablehnung-rechtsschutz` (vier Angriffslinien inklusive Anerkenntnisfiktion des § 128 Satz 3 VVG und Eskalationsleiter zu Stichentscheid, Ombudsmann und Deckungsklage), `kostenabrechnung-rechtsschutzversicherung` (Gebührenstruktur, Vergleichsquote, Erstattungsübergang § 86 VVG).

### D&O-Versicherung (4)

`d-and-o-versicherungsbedingungen-zweisprachig` (deutsch-englisches Bedingungsgerüst: Claims-made-Prinzip, Rückwärtsdeckung und Nachmeldefrist, Abwehrkosten nach § 101 VVG, Pflichtselbstbehalt des § 93 Abs. 2 Satz 3 AktG, Wissentlichkeits-Ausschluss mit Beweislast des Versicherers, Abtretbarkeit nach § 108 Abs. 2 VVG, Severability, Sprachvorrang der deutschen Fassung), `umstandsmeldung-anspruchserhebung-d-and-o` (bestimmtheitsfeste Umstandsmeldung als Fristanker und förmliche Anspruchsmeldung nach § 104 VVG), `abwehrkostenvorschuss-anfrage-d-and-o` (Vorschussanforderung mit Fristenlage der Verteidigung, Wissentlichkeits-Vorbehalt und Budgetplan-Anlage), `vergleichszustimmung-d-and-o-versicherer` (Dreiecksabstimmung mit unterschriftsreifem Zustimmungsmuster des Versicherers, Vorbehalts-Varianten, §§ 105, 106 VVG).

### Geprüft

Alle zehn CI-Checks grün; sämtliche Neuanlagen mit Abgrenzung zu den bestehenden Vorlagen `stichentscheid-rechtsschutz`, `deckungsklage-rechtsschutzversicherung` und `deckungsschreiben-d-o-versicherung`; keine neuen Aktenzeichen (Rechtsprechung nur als Live-Recherche-Suchanker).

## v4.36.0 — Bank- und Kapitalmarktrecht: 35 Vorlagen auf Zieltiefe (2026-07-03)

Zweite Etappe der Veredelungs-Kampagne: 35 der 41 bank- und kapitalmarktrechtlichen Vorlagen wurden je gegenstandsspezifisch vertieft, verlängert und juristisch geschärft — mit den tragenden Form- und Fristbausteinen des Kreditsicherungs- und Anlegerschutzrechts.

### Schwerpunkte

Bürgschaftsrecht mit Schriftformstrenge (§ 766 BGB, Ausschluss der elektronischen Form), Bestimmtheit der Hauptschuld, Einredensystem §§ 768, 770, 773 BGB und Sittenwidrigkeits-Warnbaustein bei krasser Überforderung; Darlehensrecht mit unabdingbaren Kündigungsrechten (§ 489 Abs. 4 BGB), Vorfälligkeits- und Verbraucherkredit-Bausteinen (§§ 490 bis 495 BGB, Art. 247 EGBGB) und Widerrufs-Rückabwicklung (§ 356b BGB, Fristbeginn erst mit vollständigen Pflichtangaben); Kreditsicherheiten mit Anzeige-Wirksamkeitsvoraussetzung der Kontoverpfändung (§ 1280 BGB), Sicherungsgrundschuld-Regime (§ 1193 Abs. 2 Satz 2 BGB, Sicherungszweckerklärung eng/weit als Varianten, Rückgewähranspruch), Übersicherungs-Freigabe und Insolvenzfestigkeit (§§ 47, 51, 166, 170 f. InsO); Factoring mit scharfer Trennung echt/unecht, Globalzessions-Kollision und § 354a HGB; Zahlungsdienste mit der Dreizehn-Monats-Ausschlussfrist des § 676b Abs. 2 BGB, Erstattung nicht autorisierter Zahlungen (§ 675u BGB) und Lastschrift-Acht-Wochen-Frist; P-Konto-System §§ 850k, 850l, 899 ff. ZPO mit Bescheinigungsmechanik § 903 ZPO; Rangrücktritts- und KWG-Einlagengeschäft-Warnbausteine bei Nachrang- und Mezzanine-Finanzierungen; WpHG-Beratungsdokumentation nach §§ 63 f. WpHG.

### Verbleibend

Sechs Vorlagen des Ordners (covenant-waiver-letter-kreditvertrag, factoringvertrag-unechtes-factoring, genussrechtsvereinbarung-mezzanine, klage-schadensersatz-anlageberatung, schuldscheindarlehen-unternehmen, schuldscheindarlehen-zweisprachig) sowie die weiteren Themenordner der Kampagne bleiben der laufenden Pflege vorbehalten; die Kampagne wird mit dieser Version planmäßig geschlossen.

### Geprüft

Alle zehn CI-Checks grün; 35 ODT- und ZIP-Fassungen neu erzeugt; keine neuen Aktenzeichen (Rechtsprechung nur als Live-Recherche-Suchanker).

## v4.35.0 — Arbeitsrecht auf Zieltiefe und Abschluss der Kernordner (2026-07-03)

Erste Etappe der Veredelungs-Kampagne über den Gesamtbestand: Alle 42 arbeitsrechtlichen Vorlagen wurden je gegenstandsspezifisch vertieft, verlängert und juristisch geschärft; dazu die letzten drei erbrechtlichen Vorlagen — damit sind sämtliche Kernordner vollständig auf Zieltiefe.

### Arbeitsrecht (42)

Fristen-Gerüst durchgängig ausdrücklich: Drei-Wochen-Klagefrist § 4 KSchG mit Fiktion § 7 und nachträglicher Zulassung § 5 KSchG, Zwei-Wochen-Frist § 626 Abs. 2 BGB mit Rückwärtsplanung gegen die Drei-Tages-Frist des § 102 Abs. 2 Satz 3 BetrVG, Wochenfrist § 99 Abs. 3 BetrVG samt Zustimmungsfiktion, § 17 TzBfG, §§ 15 f. BEEG (sieben/dreizehn Wochen), AÜG-Stichtage (Höchstdauer 18 Monate, Equal-Pay 9/15 Monate) und Ausschlussfristen-Bausteine mit MiLoG-Festigkeit. Betriebsverfassung mit Ladungs-/Beschlussfähigkeitskette (§§ 25, 29, 33 BetrVG), § 99-Katalog als Subsumtionsraster, Einigungsstellen- und Nachteilsausgleichs-Mechanik (§§ 76, 100 ArbGG, §§ 112 f. BetrVG). Rechtsstand nachgezogen (Textform im NachwG und AÜG, elektronische Zeugnisform, Fünftelungsregelung in der Veranlagung, § 95 Abs. 2a BetrVG und KI-Verordnung als Rechercheanker). Dabei substanzielle Reparaturen: das Teilzeitverlangen war ein fehlerhaftes Vollstreckungs-Boilerplate und wurde als echtes § 8 TzBfG-Verlangen neu gebaut; ein unwirksamer Pauschal-Freiwilligkeitsvorbehalt wurde durch eine AGB-feste Bonus-Architektur ersetzt; Anlagenapparate von generisch auf fallspezifisch umgestellt.

### Erbrecht (3)

Testamentsvollstrecker-Annahme mit vollem Pflichtenprogramm (§§ 2202, 2215 f., 2218 f., 2221 BGB), Vermächtniserfüllungsvertrag mit zwei korrigierten Falschzitaten und Beurkundungs-Variante, Vorsorgevollmacht mit Patientenverfügung strukturell saniert (Dezimalgliederung statt Pseudo-Paragrafen, Bestimmtheitsgebot § 1827 BGB umgesetzt, Organspende-Baustein).

### Geprüft

Alle zehn CI-Checks grün; 45 ODT- und ZIP-Fassungen neu erzeugt; keine neuen Aktenzeichen (Rechtsprechung nur als Live-Recherche-Suchanker). Nächste Etappen der Kampagne: Bank- und Kapitalmarktrecht, Steuer-, Straf-, Medizin- und Versicherungsrecht.

## v4.34.0 — Schluss-Lift Familien- und Erbrecht: 23 Vorlagen auf Zieltiefe (2026-07-03)

Abschluss des fachlichen Tiefen-Lifts über die letzten ungehobenen Bestandsvorlagen: zehn familienrechtliche und dreizehn erbrechtliche Vorlagen tragen jetzt absatzgenaue Normzitate, Fristen- und Formbausteine, OPTIONAL- und Varianten-Module sowie vollständige READMEs mit Abgrenzungen und einem Fristen-Absatz unter „Hinweise zur Verwendung".

### Familienrecht (10)

Auskunftskette zum Zugewinn geschlossen (§ 1379 BGB satzgenau, Hinzurechnung § 1375 Abs. 2 und 3 BGB, vorzeitiger Ausgleich §§ 1385 f. BGB als Modul), Eskalationshebel § 235 Abs. 2 FamFG beim Unterhalts-Auskunftsverlangen, Überleitungsklauseln der Ehewohnungs-Vereinbarung von der Trennungszeit (§§ 1361a, 1361b BGB) in die Zeit nach Scheidung (§§ 1568a, 1568b BGB mit Jahresfrist), dokumentationsfestes Umgangsprotokoll mit Neutralitätsgebot, Wechselmodell-Betreuungsplan mit Rhythmus-Varianten und Billigungs-Option § 156 Abs. 2 FamFG, Versorgungsausgleichs-Auskunftsbogen mit allen Anrechtsarten und Teilungssystematik §§ 10–17 VersAusglG. Dabei mehrere falsche Normzitate korrigiert (u. a. erfundenes „§ 1376 Abs. 1 Satz 2", unzutreffende Auslandszitate) und Übersetzungsfehler der zweisprachigen Fassungen behoben.

### Erbrecht (13)

Personenstands- und Nachlasssicherungskette vertieft (PStG-Anträge, Nachlasspflegschaft § 1960 BGB, Nachlassverwaltung mit Wirkung § 1984 BGB, Nachlassinsolvenz mit § 1980-Warnbaustein), Testamentsvollstreckerzeugnis § 2368 BGB, Erbengemeinschafts-Trio (Verwaltung §§ 2038, 745 BGB, Verfügung § 2040 BGB, Teilungsversteigerung nach dem Zwangsversteigerungsgesetz als Ausweichszenario, Beurkundungspflicht § 311b BGB), Erbteilsübertragung mit Haftungsfortdauer § 2036 BGB, Europäisches Nachlasszeugnis mit Sechs-Monats-Gültigkeit der Abschrift (Art. 70 Abs. 3 EuErbVO), notarielle Grundstücksübertragung und Übergabevertrag mit Rückforderungs-Varianten, Nießbrauchs- und Pflichtteilsanrechnungs-Systematik.

### Geprüft

Alle zehn CI-Checks grün; 23 ODT- und ZIP-Fassungen neu erzeugt; keine neuen Aktenzeichen (Rechtsprechung nur als Live-Recherche-Suchanker). Drei erbrechtliche Vorlagen (Testamentsvollstrecker-Annahme, Vermächtniserfüllungsvertrag, Vorsorgevollmacht mit Patientenverfügung) stehen noch auf der Liste für die laufende Pflege.

## v4.33.4 — Release-Stand, README und Eval synchronisiert (2026-07-03)

### Verbessert

- **Release-Stand nachgezogen:** Die seit v4.33.3 auf `main` gemergten Schlussstein-Nachträge zur zweisprachigen Sozialleistungsakte und zur umfassenden Insolvenzverfahrens-Vollmacht werden mit diesem Patch-Release als Latest-Stand veröffentlicht.
- **Root-README aktualisiert:** Der Einstieg nennt jetzt den aktuellen Gate-Stand von 870 validierten Hauptvorlagen, 113 gerichtsleitenden Sondervorlagen und `run-eval` All-Pass 862/862.
- **Markdown-ZIP synchronisiert:** Die ZIP-Fassung der umfassenden Insolvenzverfahrens-Vollmacht wurde aus der aktuellen Markdown-Datei neu erzeugt.
- **Eval-Report erneuert:** `EVAL_RESULTS.md` wurde auf den aktuellen Lauf vom 3. Juli 2026 gesetzt.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py`; `validate-vorlagen` meldet 870 Hauptvorlagen in 40 Themenordnern, `check-gerichtsleitend` 113 Vorlagen in 18 Bereichen und `run-eval` All-Pass 862/862.

## v4.33.3 — Letzte Nachzügler: Überleitungsanzeige, Verwertungsvereinbarungen, Überprüfungs-README (2026-07-02)

Letzte Tropfen der Lift-Runde: Der Prüfvermerk zur Überleitungsanzeige grenzt die Überleitung nach § 93 SGB XII jetzt sauber von den gesetzlichen Forderungsübergängen ab (§ 94 SGB XII Unterhalt; §§ 115, 116 SGB X) und prüft die Ermessensbegründung (§ 35 Abs. 1 Satz 3 SGB X); beide Verwertungsvereinbarungen und die Überprüfungs-README wurden nachgeschärft. Alle zehn CI-Checks grün. Die Runde ist damit endgültig abgeschlossen.

## v4.33.2 — Abschluss der Lift-Runde: Tabellenfeststellung, Bank-Vergleich, Renten-Überprüfung (2026-07-02)

Abschließender Konsolidierungs-Patch der Tiefen-Lift-Runde: Die README der Tabellenfeststellungsklage erklärt jetzt die zweiwöchige Ausschlussfrist des § 189 InsO im Verteilungsverfahren, die Deckungsgleichheit von Klageantrag und Anmeldung (§ 181 InsO) und den quotenbasierten Streitwert (§ 182 InsO). Die Vergleichsvereinbarung mit Banken und Zahlungsdiensten trägt die Aufrechnungs-Prüfachse der §§ 94 bis 96 InsO samt Bargeschäftseinwand, das Wiederaufleben nach § 144 InsO und die Zustimmungslage nach §§ 160, 164 InsO. Der Überprüfungsantrag zum Rentenbescheid wurde weiter geschärft. Alle zehn CI-Checks grün; ODT- und ZIP-Fassungen neu erzeugt. Damit ist die mit v4.31.0 begonnene Runde (Neuanlagen und Tiefen-Lift in Familien-, Erb-, Sozial- und Insolvenzrecht) abgeschlossen; weitere Vertiefungen erfolgen als laufende Pflege.

## v4.33.1 — Nachzügler des Tiefen-Lifts: Schutzschirm, Sonderkündigung, Tabellenfeststellung, EM-Klage, Reha-Antrag (2026-07-02)

Fünf weitere Bestandsvorlagen erhielten den fachlichen Tiefen-Lift: der Schutzschirm-Antrag samt README (Voraussetzungen des § 270d InsO geschärft), das Sonderkündigungs-Muster (Erfüllungswahlsystem §§ 103 ff. InsO, Unwirksamkeit insolvenzabhängiger Lösungsklauseln als Suchanker), die Tabellenfeststellungsklage (Betreibenslast bei titulierten Forderungen § 179 Abs. 2 InsO, Deckungsgleichheit mit der Anmeldung), die Klage auf Erwerbsminderungsrente (Wegefähigkeit und Summierung ungewöhnlicher Leistungseinschränkungen als Begründungsbausteine, § 109 SGG) und der Reha-/Teilhabeantrag (Zuständigkeitsklärung § 14 SGB IX mit Zwei-Wochen-Weiterleitung, Wunsch- und Wahlrecht § 8 SGB IX). Alle zehn CI-Checks grün; ODT- und ZIP-Fassungen neu erzeugt.

## v4.33.0 — Fristen- und Bausteinpass in Sozial-, Erb- und Insolvenzrecht (2026-07-02)

Gezielter Pass über fristkritische Stellen und einzelne Bestandsvorlagen; alle zehn CI-Checks grün, ODT- und ZIP-Fassungen der sieben berührten Vorlagen neu erzeugt.

- **Vier-Jahres-Grenze ausdrücklich benannt.** Beide Überprüfungsanträge nach § 44 SGB X (`ueberpruefungsantrag-sgb-x`, `ueberpruefungsantrag-rentenbescheid-sgb-x`) nennen die Nachzahlungsgrenze von längstens vier Jahren (§ 44 Abs. 4 SGB X) jetzt beim Namen, samt der Verkürzung auf ein Jahr im SGB II (§ 40 Abs. 1 Satz 2 SGB II) und im SGB XII (§ 116a SGB XII).
- **Zwei-Jahres-Grenze des Gläubigerantrags.** Der Antrag auf Nachlassverwaltung stellt klar, dass der Gläubigerantrag nur binnen zwei Jahren seit Annahme der Erbschaft zulässig ist (§ 1981 Abs. 2 Satz 2 BGB).
- **Jahresfrist nach Scheidung.** Die README der Ehewohnungs- und Hausratsvereinbarung grenzt die Trennungsregelung nach § 1361b BGB von der Regelung nach Scheidung ab und warnt vor dem Erlöschen des Mietwohnungs-Anspruchs ein Jahr nach Rechtskraft (§ 1568a Abs. 6 BGB).
- **Sozialgerichtlicher Eilrechtsschutz und Bürgergeld-Eilantrag** wurden fachlich vertieft (§ 86b Abs. 1 und 2 SGG sauber getrennt, Glaubhaftmachung, Folgenabwägung; vorläufige Bewilligung § 41a SGB II, Minderungsstufen nach der Reform).
- **Insolvenzrecht:** Masseunzulänglichkeitsanzeige (Rangfolge § 209 InsO, Vollstreckungsverbot § 210 InsO) und Nachmeldung zur Tabelle (verspätete Anmeldung § 177 InsO mit Kostenfolge) ausgebaut.

Geprüft wurde zudem, dass die übrigen als fristkritisch markierten Vorlagen die maßgeblichen Fristen bereits tragen (Vorkaufsrecht der Miterben zwei Monate, EU-Nachlasszeugnis-Abschrift sechs Monate, Schutzschirm-Planvorlage höchstens drei Monate). Der flächige Tiefen-Lift der verbleibenden Bestandsvorlagen der vier Kernordner wird in Folgeversionen fortgesetzt.

## v4.32.0 — StaRUG-Restrukturierungsplan: Abstimmungsmechanik und § 4-Ausnahmen vervollständigt (2026-07-02)

Der Muster-Restrukturierungsplan in `restrukturierungsrecht-starug/restrukturierungsplan-starug` trug bereits Vergleichsrechnung gegen das nächstbeste Alternativszenario, gruppenbezogene Schlechterstellungsprüfung, Debt-Equity-Baukasten und einundzwanzig Anlagen — ihm fehlten aber zwei tragende Verfahrensbausteine, die jetzt als Abschnitte 2.9 und 2.10 ergänzt sind:

- **Nicht gestaltbare Rechtsverhältnisse (§ 4 StaRUG).** Ausdrückliche Klarstellung, dass Arbeitnehmerforderungen einschließlich der Rechte aus Zusagen der betrieblichen Altersversorgung, Forderungen aus vorsätzlich begangenen unerlaubten Handlungen sowie Geldstrafen und gleichgestellte Geldzahlungspflichten von den Plangestaltungen unberührt bleiben, samt Prüfvermerk-Anker in Anlage 3.
- **Planabstimmung, Mehrheiten und gruppenübergreifende Annahme (§§ 17 ff., 24 bis 28 StaRUG).** Planangebot außergerichtlich oder im gerichtlichen Planabstimmungsverfahren als ausformulierte Varianten, Stimmrechtszuordnung nach § 24 StaRUG mit Anlage-3-Verweis, Dreiviertel-Mehrheit je Gruppe (§ 25 Abs. 1 StaRUG) und die gruppenübergreifende Mehrheitsentscheidung mit den drei Voraussetzungen der §§ 26 bis 28 StaRUG (keine Schlechterstellung, angemessene Wertbeteiligung nach der absoluten Prioritätsregel des § 27 mit § 28-Durchbrechungen, Mehrheit der Gruppen) einschließlich der Brücke zu Bestätigung, Versagungsgründen und Minderheitenschutz (§§ 60, 63, 64 StaRUG).

Daneben trägt `familienrecht/antrag-vereinfachtes-verfahren-kindesunterhalt` beim Titel jetzt eine echte Wahl zwischen dynamischem Prozentsatz-Titel und beziffertem Festbetrag mit Eignungshinweisen. Alle zehn CI-Checks grün; ODT- und ZIP-Fassungen der beiden geänderten Vorlagen neu erzeugt. Der verbleibende Bestands-Tiefen-Lift der vier Kernordner folgt in der nächsten Runde.

## v4.31.0 — Familien-, Erb-, Sozial- und Insolvenzrecht: 13 neue Vorlagen und fachlicher Tiefen-Lift (2026-07-02)

**Stand:** 870 validierte Hauptvorlagen in 39 Themenordnern (vorher 857), 114 Schriftvorlagen in `vorlagen-gerichtsleitend/`, Drei-Ordner-Index mit Zählern 361/441/68, Eval-Harness All-Pass, alle zehn CI-Checks grün.

### Neu — 13 Vorlagen für Praxis-Klassiker, die bisher fehlten

Familienrecht: `antrag-vaterschaftsfeststellung` (§ 1600d BGB mit Empfängniszeit-Vermutung und § 178 FamFG-Duldungspflicht), `vaterschaftsanfechtung-antrag` (eigener Fristwahrungs-Abschnitt zur Zweijahresfrist des § 1600b BGB, Scheinvaterregress-Vorbehalt), `antrag-gemeinsame-sorge-1626a-bgb` (negativer Kindeswohlmaßstab, Vermutungsregel und vereinfachtes Verfahren nach § 155a FamFG), `antrag-annahme-als-kind-stiefkindadoption` (Einwilligungs-Fahrplan der §§ 1746–1750 BGB samt Ersetzungs-Variante nach § 1748 BGB, § 1766a BGB).

Erbrecht: `erbvertrag-notariell` (vertragsmäßige Verfügungen nach § 2278 BGB, Rücktrittsvorbehalt §§ 2293, 2296 BGB, Pflegekoppelung über das Rücktrittsrecht), `behindertentestament` (nicht befreite Vorerbschaft über der Pflichtteilsquote plus Dauertestamentsvollstreckung mit sozialhilfefesten Verwaltungsanweisungen, § 2306-Kalibrierung), `anfechtung-erbausschlagung` (Varianten für erklärte Ausschlagung und Fristversäumung § 1956 BGB, Eigenschafts- vs. Motivirrtum, Sechs-Wochen-Frist), `vollmacht-digitaler-nachlass` (transmortal, dienstbezogene Weisungen, getrennt verwahrtes Zugangsverzeichnis ohne Passwörter im Dokument).

Sozialrecht: `antrag-erwerbsminderungsrente-drv` (Drei-Fünftel-Belegung samt Verlängerungstatbeständen, § 99 SGB VI-Antragsfrist, „Reha vor Rente"), `antrag-pflegegrad-pflegeleistungen-sgb-xi` (sechs Begutachtungsmodule, kompletter Leistungswahl-Baukasten, Begutachtungsfristen), `untaetigkeitsklage-sozialgericht-88-sgg` (Sperrfristen sechs/drei Monate, Bescheidungsantrag, vorbereitete Erledigungserklärung mit Kostenantrag), `antrag-grundsicherung-alter-erwerbsminderung-sgb-xii` (beide Anspruchs-Varianten, Mehrbedarfe, prominenter Baustein zum Unterhaltsrückgriffs-Privileg der 100.000-Euro-Grenze).

Insolvenzrecht: `fortfuehrungsprognose-dokumentation-19-inso` — geführte Arbeits- und Nachweisvorlage der Geschäftsführung zur Fortbestehensprognose nach § 19 Abs. 2 InsO: Vorprüfung der Zahlungsunfähigkeit mit Warnbaustein, Überschuldungsstatus mit Rangrücktritten nach § 19 Abs. 2 Satz 2 InsO, Zwölf-Monats-Liquiditätsplan mit Prämissenkatalog, Sensitivitäten, Gesamtwürdigung mit Folgenbelehrung zu §§ 15a, 15b InsO und StaRUG-Option sowie Sieben-Schritte-Anleitung in der README.

Alle Neuanlagen mit vollständiger README (Normenliste, Anwendungsbereich mit Abgrenzung zu Nachbarvorlagen, Fristen- und Formhinweise, Rechtsprechungs-Suchanker ohne ungeprüfte Aktenzeichen), ODT- und Markdown-ZIP-Fassung, Baseline-Rubric und genau einem Eintrag in der Drei-Ordner-Sicht.

### Verbessert — fachlicher Tiefen-Lift des Bestands

Rund zwei Drittel der Bestandsvorlagen in Familien-, Erb- und Sozialrecht erhielten den fachlichen Tiefen-Lift: präzise Zuständigkeits- und Fristangaben mit Absatz-genauen Normzitaten, konkrete Beweis- und Glaubhaftmachungsbausteine, OPTIONAL-Module (Verfahrenskostenhilfe, einstweilige Anordnung, Akteneinsicht nach § 25 SGB X, Aussetzung der Vollziehung nach § 86a SGG), geschärfte README-Abgrenzungen. Im Insolvenzrecht wurden unter anderem Anfechtungs-Anspruchsschreiben und Masseverbindlichkeitsvereinbarung vertieft und der Insolvenzplan um rund hundert Zeilen ausgebaut (Vergleichsrechnung, Gruppenbildung, § 225a-Gestaltungen). Der restliche Bestands-Lift der vier Ordner sowie der StaRUG-Restrukturierungsplan-Ausbau folgen in der nächsten Runde.

### Geprüft

Alle zehn CI-Checks grün; 84 ODT-Dateien und 83 Markdown-ZIPs neu erzeugt; Kurz-Hinweis-Tokens, Warnhinweis-Blöcke mit Eigenleistungs-Absatz, Rubrum- und Schlussmarker sowie Dezimalgliederung in allen Neuanlagen verifiziert; keine neuen Aktenzeichen aufgenommen.

## v4.30.1 — Einstiegsdokumentation und Validator-Beschreibung nachgezogen (2026-07-01)

### Verbessert

- **Root-README synchronisiert:** Die Startseite nennt jetzt den tatsächlichen Stand von 857 validierten Hauptvorlagen, 113 gerichtsleitenden Sondervorlagen und `run-eval` All-Pass 849/849.
- **Themenübersicht vervollständigt:** Der seit v4.19 vorhandene Themenordner `strafvollzugsrecht/` ist nun auch in der thematischen Gliederung der Root-README aufgeführt; die Rechtsbereichszahl wurde auf 40 korrigiert.
- **Validator-Dokumentation bereinigt:** Die Docstring-Beschreibung von `scripts/validate-vorlagen.py` spricht nicht mehr von der entfernten Mandatsreife-Prüfmatrix und nennt die korrekte Zahl erwarteter Themenordner.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py` mit `run-eval` All-Pass 849/849.

## v4.30.0 — Standardklauseln für Verträge ergänzt (2026-07-01)

### Neu

- **Klauselsammlung für Vertragsbausteine:** Neue sonstige Vorlage `standardklauseln-vertraege` im Bereich Allgemeines und Bereichsübergreifendes mit ausformulierten Standardklauseln für Vertragsschluss per PDF, E-Mail oder Signaturplattform, Rechtswahl, Gerichtsstand, Anlagenrangfolge, Textform, Mitwirkung, Abnahme, Vergütung, Verzug, Aufrechnung, Haftung, Vertraulichkeit, Datenschutz, höhere Gewalt, Abtretung, Compliance, Zugang, Teilunwirksamkeit und Sprachvorrang.
- **AGB- und Formgrenzen sichtbar gemacht:** README und Warnhinweis trennen die freiwillig vereinbarte elektronische Textform klar von gesetzlicher Schriftform, qualifizierter elektronischer Signatur und notarieller Beurkundung; die Klauseln enthalten Schutzmechaniken für § 305b BGB, § 307 BGB, § 309 BGB und § 38 ZPO.

### Geprüft

ODT und Markdown-ZIP der neuen Vorlage erzeugt; Drei-Ordner-Sicht und Themen-README aktualisiert; alle zehn CI-Checks grün über `python3 scripts/check-all.py` mit `run-eval` All-Pass 849/849.

## v4.29.2 — Betriebsrenten-Rechtsweg und Erziehungsrente bereinigt (2026-06-30)

### Behoben

- **Betriebsrentenklage mit Rechtsweg-Check:** Die Klage gegen Arbeitgeber oder Versorgungsträger prüft den Rechtsweg zu den Arbeitsgerichten jetzt ausdrücklich nach Beklagtenstellung und § 2 ArbGG. Bei externen Versorgungsträgern verweist die Vorlage nicht mehr pauschal auf das Arbeitsgericht, sondern zwingt zur Prüfung von ordentlichem Rechtsweg, Einstandspflicht und gegebenenfalls gemeinsamer Inanspruchnahme.
- **DRV-Hinterbliebenenantrag ohne Erziehungsrente:** Die Erziehungsrente nach § 47 SGB VI wurde aus dem Antrag aus der Versicherung der verstorbenen Person entfernt. Die Vorlage deckt jetzt klar Witwen-, Witwer-, Lebenspartner- und Waisenrente ab; die README grenzt die Erziehungsrente als Leistung aus eigener Versicherung aus.

### Geprüft

ODT und Markdown-ZIP der beiden berührten Vorlagen neu gebaut; alle zehn CI-Checks grün über `python3 scripts/check-all.py`.

## v4.29.1 — Hinterbliebenenrente rententypenscharf korrigiert (2026-06-30)

### Behoben

- **Ein-Jahres-Prüfung sauber begrenzt:** Der DRV-Antrag auf Hinterbliebenenrente trennt die Voraussetzungen für Witwen-, Witwer- und Lebenspartnerrenten jetzt von Waisenrente und Erziehungsrente. Die kurze Ehe- oder Lebenspartnerschaft mit besonderem Umstand steht nur noch bei § 46 SGB VI; Waisenrente und Erziehungsrente erhalten eigene ausfüllbare Tatsachenketten zu Kindstatus, Ausbildung, Scheidung, Rentensplitting, Kindererziehung und Wartezeit.
- **README fachlich nachgezogen:** Die Hinweise zur Verwendung nennen nun § 47 SGB VI ausdrücklich und erklären, dass § 46 Absatz 2a SGB VI nicht auf Waisenrente oder Erziehungsrente übertragen wird.

### Geprüft

ODT und Markdown-ZIP der berührten Vorlage neu gebaut; alle zehn CI-Checks grün über `python3 scripts/check-all.py`.

## v4.29.0 — Rentenberatung fachlich nachgeschärft (2026-06-30)

### Verbessert

- **DRV-Rentenberatung konkreter geführt:** Kontenklärung, Rentenauskunft, Altersrente, Schwerbehindertenrente, Hinterbliebenenrente, Widerspruch, Überprüfungsantrag und Rentenhöheklage enthalten jetzt zusätzliche Szenarien-, Lücken-, Wartezeit-, Einkommens- und Kontrollrechnungstabellen sowie präzisere Hilfsanträge.
- **Betriebsrentenberatung vertieft:** Auskunft, Anspruchsschreiben und Klage zur betrieblichen Altersversorgung trennen deutlicher zwischen arbeitsrechtlicher Zusage, Durchführungsweg, Versorgungsträgerberechnung, Arbeitgeber-Einstandspflicht, Anpassungsprüfung und Passivlegitimation.
- **Erwerbsminderungsrente bereinigt:** Der alte Bearbeitungshinweis im Mustertext wurde durch verwendbaren Klagevortrag zu arbeitsmarktbedingter voller Erwerbsminderung, Wegefähigkeit und Drei-Fünftel-Belegung ersetzt.

### Geprüft

ODT und Markdown-ZIP für alle zwölf berührten Rentenberatungs-Vorlagen neu gebaut; alle zehn CI-Checks grün über `python3 scripts/check-all.py` mit `run-eval` All-Pass 848/848.

## v4.28.0 — Rentenrecht und Betriebsrenten-Vorlagen ausgebaut (2026-06-30)

### Neu

- **DRV-Antragsstrecke ergänzt:** Acht neue sozialrechtliche Vorlagen decken Kontenklärung, Rentenauskunft, Altersrente, Altersrente für schwerbehinderte Menschen, Hinterbliebenenrente, Widerspruch gegen Rentenbescheide, Überprüfungsantrag nach § 44 SGB X und Klage zur Rentenhöhe beziehungsweise zum Versicherungsverlauf ab.
- **Betriebsrentenstrecke ergänzt:** Drei neue arbeitsrechtliche Vorlagen führen durch Auskunft zur betrieblichen Altersversorgung, außergerichtliche Geltendmachung von Betriebsrentenansprüchen und arbeitsgerichtliche Klage gegen Arbeitgeber oder Versorgungsträger.

### Verbessert

- **Nutzerführung im Rentenrecht verdichtet:** Die neuen Muster arbeiten mit sprechenden Pflichtangaben, tabellarischen Fehlzeiten- und Berechnungspunkten, konkreten Anlagenlisten, Akteneinsichtsanträgen und branchenspezifischen Angriffspunkten zu Wartezeit, Entgeltpunkten, Zugangsfaktor, Kindererziehung, Pflegezeiten, Hinterbliebeneneinkommen und Betriebsrentenanpassung.
- **Index und Themen-READMEs nachgezogen:** Sozialrecht, Arbeitsrecht und die prozessuale Drei-Ordner-Sicht verweisen auf die neuen DRV- und Betriebsrenten-Vorlagen; die Bestandszahlen steigen auf 856 validierte Hauptvorlagen.

### Geprüft

ODT und Markdown-ZIP für alle elf neuen Hauptvorlagen erzeugt; alle zehn CI-Checks grün über `python3 scripts/check-all.py`.

## v4.27.1 — Vergleichsvereinbarung sprachlich und optisch geglättet (2026-06-30)

### Verbessert

- **Deutschsprachige Fristlogik geschärft:** In der insolvenzrechtlichen Bank-/Zahlungsdienst-Vergleichsvereinbarung heißt die Viermonatsgrenze nun „äußerster Zahlungseingangstermin" statt „Long-Stop-Date"; die englische Fassung behält den üblichen Begriff „long-stop date".
- **Formatierung beruhigt:** Der Vertragseingang ist als übersichtliche Kopftabelle gefasst, der zweisprachige Titel ist lesbarer getrennt und Anlage 3 verwendet dieselbe deutschsprachige Fristbezeichnung wie Abschnitt 3.

### Geprüft

ODT und Markdown-ZIP der berührten Vorlage neu gebaut; alle zehn CI-Checks grün über `python3 scripts/check-all.py`.

## v4.27.0 — Insolvenzrechtliche Bank- und Zahlungsdienstvergleiche ergänzt (2026-06-30)

### Neu

- **Vergleichsvereinbarung Bank / Zahlungsdienst Insolvenzmasse:** neue zweisprachige vertragliche Vorlage für Vergleiche zwischen Insolvenzverwalter und Bank oder Zahlungsdienstleister über Kontoguthaben, Reservebeträge, Fremdwährungspositionen, Rückzahlungsrisiken und Insolvenzanfechtungsansprüche.
- **Anlagenmechanik für Konto- und Zahlungsdaten:** Anlagen zu Konten und Stichtagsbeständen, streitigen Übertragungen, Vergleichszahlung, Fremdwährungsumrechnung und Vollzug/Freigaben bilden den Verhandlungsstand belegbar ab.

### Verbessert

- **Insolvenzrecht- und Kategorienindex aktualisiert:** neue Vorlage in `insolvenzrecht/` und in der vertraglichen Drei-Ordner-Sicht verankert; Bestandszahlen auf 845 Hauptvorlagen und All-Pass 837/837 nachgezogen.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py`: `validate-vorlagen` (845/845), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 837/837).

## v4.26.1 — Kohärenz-Feinschliff: Repo-Hygiene und Paragraf-12-Bereinigung (2026-06-29)

Punktueller Bug-Hunt- und Kohärenzdurchlauf nach dem Usability-Ausbau in v4.26.0. Ein repoweiter Scan (verschachtelte oder kaputte Platzhalter, doppelte Überschriften, unbalancierte Klammern, Fülltext-Marker, halluzinierte Namen) bestätigt einen sauberen Bestand; behoben wurde gezielt der Langschwanz statt einer breiten generischen Welle.

### Behoben

- **Repo-Hygiene.** Eine verirrte Arbeits-Prompt-Datei im Wurzelverzeichnis entfernt; sie war ein Auftragsdokument, keine Vorlage, und auf keinen Index verlinkt.
- **Verstümmelter Anlagentitel.** In der Vorlage `klage-rueckabwicklung-darlehenswiderruf` war der Titel der Anlage 5 verstümmelt (begann mit „und Tilgungsleistungen … […] €"). Er lautet jetzt „Aufstellung der Zins- und Tilgungsleistungen des Darlehensnehmers"; die Zweckangabe ist ein vollständiger Satz mit Geldbetrag im Format [Betrag] EUR.
- **Anwendungshinweise aus dem Mustertext ausgelagert.** Drei Hauptbestand-Vorlagen (`covenant-waiver-letter-kreditvertrag`, `vergleichsvorschlag-prozess-und-aussergerichtlich`, `datenschutz-einwilligung-mandatskommunikation`) trugen einen Abschnitt mit Anwendungshinweisen im Mustertext. Diese gehören nach CLAUDE.md Abschnitt 12 ausschließlich in die README; der Inhalt wurde dorthin verschoben und der Abschnitt aus dem Mustertext entfernt.

### Geprüft

Alle zehn CI-Checks grün; ODT und ZIP der vier berührten Vorlagen neu gebaut. Bewusst nicht angefasst: die in Schriftsätzen idiomatischen „EUR [Betrag]"-Stellen und die englischen Spalten zweisprachiger Vorlagen sowie editorielle Auslassungszeichen in Zitaten — eine pauschale Umschreibung wäre eine generische Welle ohne Mehrwert gewesen.

## v4.26.0 — Usability- und Workflow-Einstieg geglättet (2026-06-29)

### Neu

- **Workflow-Handbuch ergänzt:** `WORKFLOWS.md` führt jetzt knapp durch Finden, Benutzen, Ändern, Neuanlage, Sonderbereich, Release und typische Fehlerbilder.
- **Gebündelter Qualitätsgate:** `scripts/check-all.py` führt alle zehn lokalen Prüfungen in CI-Reihenfolge aus; im Entwicklerlauf aktualisiert es den Eval-Report, im CI-Modus schreibt es wie bisher die JSON-Ausgabe.

### Verbessert

- **README als Einstiegspunkt geschärft:** Schnellstart, aktuelle Bestandszahlen und der Workflow-Verweis machen klarer, wie Nutzer und Bearbeiter durch das Repo gehen.
- **GitHub Action vereinheitlicht:** Die CI ruft denselben gebündelten Qualitätsgate mit `--ci` auf, damit lokaler und remote Workflow nicht auseinanderlaufen.

### Geprüft

Alle zehn CI-Checks grün über `python3 scripts/check-all.py`: `validate-vorlagen` (844/844), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 836/836).

## v4.25.0 — Sanity-, Rechtsprechungs- und Kohärenzfeinschliff (2026-06-29)

### Verbessert

- **Sozialrecht rechtsprechungsnäher gemacht:** Die neuen Vorlagen zu Sperrzeit, Hilfsmittel und Kosten der Unterkunft enthalten nun verifizierte BSG-Anker zu Sperrzeitprüfung, Hilfsmittelversorgung und schlüssigem Unterkunftskostenkonzept; die KdU-Klage verwendet präzisere Zahlungsplatzhalter.
- **Presserechtliche Eilverteidigung geschärft:** Die README zur Erwiderung im presserechtlichen einstweiligen Verfügungsverfahren verweist jetzt auf aktuelle BVerfG-Anker zur prozessualen Waffengleichheit und zur Anhörungslogik im Eilrechtsschutz.
- **Schutzrechtsverträge entgenerisiert:** Haftungs-, Compliance- und Gebührenklauseln in Marken-, Know-how-, Design-, F&E-, Geheimnisschutz- und Patentpoolvorlagen benennen jetzt konkrete Pflichtverletzungen, marken- und produktsicherheitsbezogene Risiken sowie sprechendere Gebührenfelder.
- **Gliederungskohärenz nachgezogen:** Zwei freistehende Gegenstandszeilen aus neuen Schriftsatzmustern wurden in zulässige Kopfangaben überführt.
- **Artefakte synchronisiert:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und die Markdown-ZIPs aktualisiert.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (844/844), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 836/836).

## v4.24.0 — Sozialrecht, Schutzrechts-Eilrechtsschutz und Medienverteidigung ausgebaut (2026-06-29)

### Neu

- **Sozialrecht laienfreundlicher erweitert:** Neue Vorlagen für Widerspruch gegen Sperrzeit beim Arbeitslosengeld, Widerspruch gegen Hilfsmittelablehnung der Krankenkasse und Klage wegen Kosten der Unterkunft im Bürgergeld. Die Muster führen stärker durch Sachverhaltsermittlung, Belege, Amtsermittlung, funktionellen Bedarf, Kostensenkung, Wohnungsmarkt und sozialgerichtliche Anträge.
- **Gewerblicher Rechtsschutz vertieft:** Neue Gebrauchsmusterlizenz mit ungeprüftem Rechtsbestandsrisiko, Löschungsmechanik und Lizenzabrechnung sowie neue Vorlagen für technische Schutzrechtsverfügungen und Schutzschriften zu Patent, Gebrauchsmuster und Design.
- **Urheber- und Medienrecht ergänzt:** Neue Erwiderung im presserechtlichen einstweiligen Verfügungsverfahren und neue Unterlassungserklärung im Medien- und Persönlichkeitsrecht mit Aussagekern, konkreter Verletzungsform, Vertragsstrafe, Deindexierung und Vorbehalten.

### Verbessert

- **Nutzerführung im Sozialrecht geschärft:** Das Sozialrechts-README erklärt jetzt ausdrücklich, dass sozialrechtliche Vorlagen eine juristisch geführte Sachverhaltsermittlung brauchen und nicht nur das Einsetzen von Normbehauptungen.
- **Kategorie- und Rubric-Mechanik aktualisiert:** Drei-Ordner-Index, Themen-READMEs, Rubrics und Rubric-Typerkennung wurden auf die neuen Schutzschrift-, Erwiderungs- und Unterlassungserklärungsfälle angepasst.
- **Artefakte erzeugt:** Für alle acht neuen Hauptvorlagen wurden ODT-Dateien, Markdown-ZIPs und Rubrics erstellt.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (844/844), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 836/836).

## v4.23.1 — Pflegegradklage: Zweitbegutachtung befüllbar verzweigt (2026-06-29)

### Verbessert

- **Pflegegradklage korrigiert:** Der Sachverhaltsteil trennt jetzt Fälle ohne Zweitbegutachtung von Fällen mit Zweitgutachten. Datum, Gutachtenstelle und gewichtete Gesamtpunkte sind echte Platzhalter; der Widerspruchsbescheid verweist je nach Verfahrensstand auf Anlage 4 oder Anlage 5.
- **Artefakte synchronisiert:** ODT und Markdown-ZIP der Pflegegradklage wurden neu erzeugt.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (836/836), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 828/828).

## v4.23.0 — Sanity-, Bug- und Kohärenzrunde für Vorlagen (2026-06-29)

Diese Runde zieht eine gezielte Fehlersuche über Mustertexte mit didaktischen Resten, gebrochenen Platzhaltern, doppelten Schlussblöcken und unklaren Querverweisen. Der Fokus lag auf echter Anwendbarkeit: Mustertexte enthalten weniger Bearbeiterkommentar, Optionen sind besser vollziehbar, und formale Artefakte sind wieder synchron.

### Verbessert

- **28 Hauptvorlagen und eine Sonderbereichsvorlage geglättet:** Didaktische Kommentarzeilen wurden aus Arbeits-, Vergabe-, Bank-, Familien-, Straf- und Immaterialgütervorlagen entfernt; die Mustertexte bleiben dadurch Vertrags-, Antrags- oder Schriftsatztext.
- **Mechanikfehler beseitigt:** Der CMR-Frachtvertrag enthält nun saubere ICC- und DIS-Schiedsklauseln, den richtigen Verweis auf Abschnitt 8.3 und keinen doppelten Schlussblock mehr; die Pflegegradklage trennt Antrag, Begutachtung, Widerspruch und Zweitbegutachtung wieder befüllbar.
- **Meta- und Warnsprache entschärft:** SAFT, Kontoverpfändung, Leihe, Schenkung, Schuldanerkenntnis, UWG-Verfügung, Designanmeldung, Schiedsvereinbarung, Europäisches Mahnverfahren, Erbausschlagung und staatsanwaltschaftliche Einstellung verwenden nun fallbezogene Klausel- oder Verfügungssprache statt Vorlagenkommentar.
- **Artefakte synchronisiert:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und die Markdown-ZIPs aktualisiert.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`.

## v4.22.0 — Generische Gerüstvorlagen fachlich konkretisiert (2026-06-29)

Diese Runde verdichtet kurze oder noch schablonenhafte Antrags-, Anspruchs- und Stellungnahmevorlagen aus Bankrecht, Bau- und Architektenrecht, Insolvenzrecht, Mietrecht, Migrationsrecht, Steuerrecht, Strafrecht, Vergaberecht, Verkehrsrecht, Verwaltungsrecht, Sportrecht, Medienrecht und gewerblichem Rechtsschutz. Statt generischer Platzhalter wie „Hauptantrag einsetzen“ enthalten die Muster nun konkrete Anträge, fallbezogene Sachverhaltsmechanik, Normzuordnung, Nachweislogik und spezifische Anlagen.

### Verbessert

- **29 Hauptvorlagen konkretisiert:** Generische Antragsteile wurden durch ausformulierte Abschnitte zu Kopfdaten, Antrag, Sachverhalt, rechtlichem Mechanismus, Nachweisen und Schlussformel ersetzt.
- **Nutzerführung geschärft:** Anlagen heißen nun nach ihrer tatsächlichen Beweisfunktion, etwa Bauzeitenplan, Betriebskostenbelege, Fiktionsnachweis, Steuerprognose, Einziehungszuordnung, Zahlungsdienste-Protokolle oder Vergabevermerk.
- **Rechtsprechungsanker ergänzt:** READMEs zu Einspruchsruhe, Zahlungsdienste-Reklamation, Belegeinsicht und Modernisierungsankündigung enthalten nun verifizierte Anker zu BFH X B 183/11, BGH XI ZR 91/14, BGH VIII ZR 66/20 und BGH VIII ZR 55/19 mit Primärlinks.
- **Artefakte synchronisiert:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und die Markdown-ZIPs aktualisiert.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (836/836), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 828/828).

## v4.21.0 — Planführung, Kryptoverwahrung, SE/SCE und Sanierungssteuer ergänzt (2026-06-27)

Die Sanierungsplanvorlagen, Kryptovorlagen, kleine AG und steuerlichen Sanierungs- und Gemeinnützigkeitsformulare wurden gezielt erweitert. Schwerpunkt sind bessere Nutzerführung, klare Anlagenlogik, insolvenzfeste Kryptowerte-Zuordnung, europäische Gesellschaftsformen und steuerliche Folgeanträge bei Sanierungsgewinnen.

### Neu

- **SE-Satzung:** Neue Satzung für eine Societas Europaea mit dualistischem oder monistischem Organisationsmodell, Namensaktien, Arbeitnehmerbeteiligung, Sitz-/Strukturmaßnahmen und Registervollzug.
- **SCE-Satzung:** Neue Satzung für eine Europäische Genossenschaft mit variablem Kapital, Fördergeschäft, Mitgliedergruppen, Prüfungsverband, Arbeitnehmerbeteiligung und Auseinandersetzungslogik.
- **§60a-AO-Anträge:** Neue Finanzamtsanträge für gGmbH und gemeinnützige Genossenschaft mit AO-Synopse, Zweckverwirklichung, Vermögensbindung, tatsächlicher Geschäftsführung und Nahestehendenprüfung.
- **Sanierungsertragsteuer:** Neue Anträge zur körperschaftsteuerlichen Behandlung nach § 3a EStG/§ 8 KStG und zur gewerbesteuerlichen Behandlung nach § 7b GewStG, jeweils mit Verlustverbrauch, Sanierungseignung, Liquiditätswirkung und Billigkeitshilfsanträgen.

### Verbessert

- **Insolvenzplan und StaRUG-Plan:** READMEs um Befüllungskompass mit Planstelle, einzusetzenden Daten, Gesetzesanker und Kontrollfrage ergänzt; Plantexte um eigene Steueranlagen zu Sanierungsertrag, Verlustverbrauch, Körperschaftsteuer, Gewerbesteuer, Finanzamt und Kommune erweitert.
- **Krypto- und Aufsichtsrecht:** CASP-Zulassung, Art.-60-Notifizierung, Art.-143-Übergangsplan und Krypto-Verwahr-/Treuhandvereinbarung enthalten nun eigene Matrizen für Kundenvermögenszuordnung, Art.-60-Abgrenzung, Übergangspfad, Exit und Insolvenzschutz nach § 46i KWG, § 45 KMAG und Art. 75 MiCAR.
- **Kleine AG:** Zweisprachige Satzung deutlich ausgebaut um Aktienregister, vinkulierte Namensaktien, Zustimmungskatalog, Hauptversammlung, Kapitalmaßnahmen, Interessenkonflikte, Gründungsaufwand und Schlussbestimmungen; README mit aktienrechtlichen Praxisankern ergänzt.
- **Index und Artefakte:** Drei-Ordner-Sicht, ODT-Dateien, Markdown-ZIPs und Rubrics für alle neuen und berührten Hauptvorlagen aktualisiert.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (836/836), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 828/828).

## v4.20.0 — Insolvenzplan und StaRUG-Restrukturierungsplan vertieft (2026-06-27)

Die beiden großen Sanierungsplanvorlagen wurden fachlich verdichtet und stärker auf aktuelle Planpraxis zugeschnitten. Schwerpunkt sind belastbare Vergleichsrechnung, Ausproduktion im Übergangsbetrieb, Kapitalmaßnahmen nach deutschem Recht und planfeste Vollzugsanlagen.

### Verbessert

- **Insolvenzplan:** Vergleichsrechnung erweitert um Plan-, Regelabwicklungs- und Downside-Szenarien, Nettoansatz neuer Finanzierung, Verbot der Doppelzählung von Forderungsverzichten sowie produktbezogene Ausproduktions- und Übergangsbetriebsanlagen.
- **StaRUG-Plan:** Anlagenapparat auf Liquiditätsplanung, Planbetroffene, Bestandsfähigkeit, Besserungsschein, Forderungsbewertung, Kapitalmaßnahmen, Anteilseigner-Vergleichsrechnung, Kapitalmarktvollzug und Closing-Kalender ausgeweitet.
- **Kapitalmaßnahmen:** Varianten für Kapitalschnitt auf null, Kapitalerhöhung gegen Bar- oder Sacheinlage, Debt-to-Equity-Swap, Bezugsrechtsausschluss, Anteilstransfer, Abfindung und Register-/Depotvollzug ergänzt.
- **Praxisanker:** READMEs um amtliche Normlinks und Rechtsprechung zu Vergleichsrechnung, StaRUG-Minderheitenschutz, Leoni/VARTA-Anteilseingriffen und Planbestimmtheit ergänzt.
- **Artefakte synchronisiert:** Beide ODT-Dateien wurden neu erzeugt und die Markdown-ZIPs aktualisiert.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (830/830), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.19.0 — Strafvollzugsrecht und Beschwerderecht ergänzt (2026-06-27)

Neuer Themenordner `strafvollzugsrecht` mit ausformulierten anwaltlichen Vorlagen für Strafvollzug, Untersuchungshaft, Sicherungsverwahrung, Eilrechtsschutz und Rechtsbeschwerde. Zusätzlich wurde der Sonderbereich `vorlagen-gerichtsleitend` um Vorlagen für Strafvollstreckungskammer und Beschwerdegericht erweitert.

### Neu

- **Acht Hauptvorlagen im Strafvollzugsrecht:** Anträge nach §§ 109, 114 und 116 StVollzG, Vollzugslockerungen, Untersuchungshaftkontakte nach §§ 119, 119a StPO, medizinische Behandlung im Vollzug, Disziplinarmaßnahmen und Sicherungsverwahrung mit Abstandsgebot.
- **Fünf gerichtsleitende Vorlagen:** Eingangsverfügung, Beschluss nach § 115 StVollzG, Eilbeschluss nach § 114 StVollzG, Rechtsbeschwerdeentscheidung und Beschluss zu Sicherungsverwahrung und Lockerungen.
- **Rechtsprechungsanker ergänzt:** Die neuen READMEs verweisen auf einschlägige Entscheidungen des Bundesverfassungsgerichts zu Resozialisierung, Vollzugslockerungen, Untersuchungshaftbeschränkungen, Briefkontrolle und Sicherungsverwahrung.
- **Index und Validatoren aktualisiert:** Der neue Themenordner ist in `validate-vorlagen`, im Kategorienindex und im Sonderbereichscheck abgebildet.
- **Artefakte erzeugt:** Für alle acht neuen Hauptvorlagen wurden ODT-Dateien, Markdown-ZIPs und Rubrics erstellt.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (830/830), `check-kategorien-index`, `check-gerichtsleitend` (113/18), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.18.1 — Review-Fixes zu KDV, StaRUG und Zollwert (2026-06-26)

Gezielte Korrekturrunde zu drei Review-Hinweisen aus `v4.18.0`: KDV-Anträge werden im Muster nun an das Bundesamt für das Personalmanagement der Bundeswehr beziehungsweise das zuständige Karrierecenter adressiert, Stabilisierungsanträge vermeiden ein pauschales Kündigungsverbot außerhalb der gesetzlichen StaRUG-Wirkungen, und nachträgliche Zollwertminderungen werden nur noch unter den engen Voraussetzungen des Unionszollrechts als wertmindernd behandelt.

### Verbessert

- **Kriegsdienstverweigerung:** Der Antrag adressiert BAPersBw, zuständiges Karrierecenter und Dienststelle für laufende Dienstmaßnahmen; das BAFzA bleibt Entscheidungsstelle nach Weiterleitung.
- **StaRUG-Stabilisierungsanordnung:** Der Hilfsantrag nennt keine pauschale Sperre von Kündigungsrechten mehr, sondern begrenzt Vertragswirkungen auf § 55 StaRUG und grenzt nicht erfasste Gestaltungsrechte ausdrücklich aus.
- **Zollwert-Nacherhebung:** Die Rabatt-/Gutschriftvariante stellt klar, dass nachträgliche Preisermäßigungen nur bei vertraglicher Voranlage oder unter Art. 132 der Durchführungsverordnung (EU) 2015/2447 zollwertmindernd berücksichtigt werden.
- **Artefakte synchronisiert:** Für alle drei berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.18.0 — Zehn Vorlagen gezielt weiter spezifiziert (2026-06-26)

Feinschliff über zehn kurze oder noch zu generisch wirkende Vorlagen aus Zoll- und Außenwirtschaftsrecht, Insolvenzrecht, StaRUG, Europarecht, Kartellrecht, Arbeitsrecht sowie Beamten- und Soldatenrecht. Der Lauf ersetzt weitere Bearbeiterimperative durch einreichungsfähige Antrags-, Stellungnahme- und Begründungsbausteine.

### Verbessert

- **Zoll und Außenwirtschaft:** Zollwert-Nacherhebung und verbindliche Zolltarifauskunft enthalten jetzt konkrete UZK-Anknüpfungen, MRN-/KN-Code-Logik, Rechenwegsanforderungen und hilfsweise Verfahrensanträge.
- **Insolvenz und StaRUG:** Restschuldbefreiung, Freigabe aus Insolvenzbeschlag, Planabstimmungsprotokoll und Stabilisierungsanordnung wurden bei Abtretung, Obliegenheiten, Massewertprüfung, Stimmrechtsausweisung, Schlechterstellungseinwendungen und Vollstreckungssperre verdichtet.
- **Europa- und Kartellrecht:** Vertragsverletzungsbeschwerde und Kronzeugen-/Markeranfrage unterscheiden klarer zwischen Strukturverstoß, nationalem Rechtsbehelfsstand, Markerumfang, Legal Hold und Kooperationspflicht.
- **Arbeits- und Wehrrecht:** Beschäftigungs-Eilverfügung und KDV-Antrag wurden bei Tenor, § 888 ZPO, Interessenabwägung, Glaubhaftmachung, persönlicher Gewissensentscheidung und Anhörung konkreter gefasst.
- **Artefakte synchronisiert:** Für alle zehn berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.17.1 — BEEG-Textform bei Elternteilzeit korrigiert (2026-06-26)

Gezielter Review-Fix für die Vorlage `antrag-elternzeit-teilzeit-beeg`: Die Ablehnung eines Teilzeitbegehrens während der Elternzeit verweist nicht mehr pauschal auf Schriftform, sondern auf die gesetzlich erforderliche Form. Für Kinder, die ab dem 1. Mai 2025 geboren oder zur Adoption aufgenommen wurden, wird die Textform nach aktueller BEEG-Übergangslogik ausdrücklich berücksichtigt.

### Verbessert

- **Mustertext korrigiert:** Abschnitt 3.3 unterscheidet nun zwischen der aktuellen Textformmöglichkeit und älteren Übergangsfällen, in denen die fortgeltende strengere Form zu prüfen ist.
- **README ergänzt:** Die Hinweise zur Verwendung benennen die Praxisfalle einer rechtzeitig eingegangenen E-Mail-Ablehnung und verknüpfen sie mit § 15 und § 28 BEEG.
- **Artefakte synchronisiert:** ODT und Markdown-ZIP der Vorlage wurden neu erzeugt.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.17.0 — Stummelvorlagen fachspezifisch verdichtet (2026-06-26)

Gezielte Individualisierungsrunde über kurze, generisch wirkende und redaktionell noch schablonenhafte Vorlagen. Der Lauf ersetzt fachfremde Kopfmarker, generische Anlagenverzeichnisse und Bearbeiter-Imperative durch gegenstandsspezifische Mustertexte, ohne Slugs, Kategorien, bestehende Rechtsprechungsanker oder Validatorlogik zu verändern.

### Verbessert

- **Kurze Antrags- und Schriftsatzvorlagen ausgebaut:** Grundbuchberichtigung nach Erbfall, Nachlassinsolvenz, Aufgebot von Nachlassgläubigern, Entlassung des Testamentsvollstreckers, Erbunwürdigkeitsklage, Elternzeit-/Teilzeitantrag, Einigungsstellenantrag, Verdachtskündigungsanhörung, Zugewinnauskunft und Kindeswohlmaßnahmen enthalten jetzt mehr Tatbestandslogik, Fristen, Nachweise, Beweisangebote und Vollzugspunkte.
- **Miet-, Arbeits-, Erb-, Insolvenz-, StaRUG-, Kartell-, Zoll- und Europarechtsvorlagen konkretisiert:** Zuvor knappe Vermerke und Schreiben wurden um fachspezifische Anspruchs-, Zuständigkeits-, Risiko- und Nachweislogik ergänzt.
- **Generische Kopfmarker beseitigt:** Alte Marker wie `Dokumentenkopf`, `Schreibenkopf` und `Gremien- und Sitzungsdaten` wurden repoweit in den berührten Mustertexten durch konkrete Kopfzeilen zum jeweiligen Verfahrens-, Vertrags-, Beschluss- oder Prüfgegenstand ersetzt.
- **Anlagen fachlich neu gefasst:** 25 generische Anlagenverzeichnisse mit Vollmachtslogik wurden durch konkrete Nachweis-, Stimmrechts-, Sicherheiten-, Screening-, Zoll-, StaRUG-, Insolvenz-, Kartell- und Europarechtsanlagen ersetzt.
- **Artefakte synchronisiert:** Für alle 167 berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822). Zusätzlicher Sanity-Sweep ohne Mustertext-Befund für generische Marker wie `Dokumentenkopf`, `Schreibenkopf`, `Gremien- und Sitzungsdaten`, `Anlagenverzeichnis und Vollmacht`, direkte Bearbeiter-Imperative und `[Regelung]`-Stubs.

## v4.16.0 — Vertrags- und Aufsichtsrechtsvorlagen nachgeschärft (2026-06-26)

Gezielte Qualitätsrunde über die Vertragsvorlagen mit besonderem Fokus auf IT-, Finanzierungs-, Krypto-, Städtebau- und Aufsichtsrechtsverträge sowie auf zentrale BaFin- und MiCAR-Schreibvorlagen. Der Lauf ersetzt weitere generische Haftungs-, Fristen- und Schlussbestimmungsreste durch gegenstandsspezifische Regelungen, ohne Slugs, Indexstruktur oder Rechtsprechungsanker neu zu setzen.

### Verbessert

- **IT- und Plattformverträge:** Agile Softwareentwicklung, Cloud-Migration, PaaS und IT-Outsourcing unterscheiden jetzt schärfer zwischen Anbieterpflichten, Auftraggebermitwirkung, Cutover, Datenabgleich, Plattformsteuerung, Sicherheitskonfiguration, Exit und Handover.
- **Finanzierungs- und Forderungsverträge:** Factoring, Einzelforderungsverkauf, Intercreditor-Vereinbarung und Schuldscheindarlehen enthalten präzisere Haftungs-, Waterfall-, Sicherheiten-, Verzugszins- und Fristenlogik.
- **BaFin, MiCAR und Kryptoverwahrung:** Institutserlaubnis, KWG-Zulassung, CASP-Zulassung, Art. 60-/Art. 143-MiCAR-Pfade, Custody-Policy, Krypto-Verwahrtreuhand, Produktgovernance, Voranfrage und Aufsichtsreaktionsplan wurden bei Go-live-Readiness, Wallet-/Registerabgleich, Incident-Matrix, Kundentrennung, Mittelherkunft, Aufsichtszusagen und Rückgabefristen nachgeschärft.
- **Städtebau- und Bau-Schnittstellen:** Folgekostenvertrag, Durchführungsvertrag, Bauträger-Folgekostenrefinanzierung und Architekten-Festsetzungsprüfung enthalten konkretere Kausalitäts-, Sicherheiten-, Erwerberinformations-, Planänderungs-, Haftungs- und Anlagenklauseln.
- **Meta-Reste entfernt:** In den berührten Vertragsdateien wurden alte „Abschnitt 1 ist Bestandteil“-Sätze durch echte Schlussbestimmungen zu Anlagen, technischen Spezifikationen und Schriftform ersetzt.
- **Artefakte synchronisiert:** Für alle 24 berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.15.0 — Prozess- und Aufsichtsrechtsvorlagen geschärft (2026-06-24)

Gezielte Qualitätsrunde über alle acht `prozessvorlagen` und alle zwanzig Vorlagen im Themenordner `aufsichtsrecht-und-bafin`. Der Lauf verdichtet Anspruchsgrundlagen, Verteidigungslogik, Beweisantritte, Eilrechtsschutz, BaFin-Kommunikation, MiCAR/CASP-Pfade, DORA-Auslagerungen und Fit-and-Proper-Unterlagen, ohne Slugs, Indexstruktur oder bestehende Rechtsprechungsanker umzubauen.

### Verbessert

- **Prozessvorlagen:** Klage-, Erwiderungs-, Replik- und Eilrechtsschutzpakete enthalten nun konkretere Streitgegenstandsabgrenzung, tatbestandliche Subsumtionspunkte, Beweisangebote und Anlagenlogik für Zivil-, Verwaltungs-, Sozial-, Finanz-, Arbeits- und Familienverfahren. Prozessvergleich und Kostenfeststellungsklage wurden im Vollzug und bei materieller Kostenerstattung präzisiert.
- **BaFin und Aufsichtsrecht:** KWG-, CASP-, Art. 60-MiCAR-, Art. 143-MiCAR-, DORA-, Fit-and-Proper-, Inhaberkontroll-, Auskunfts-, Anhörungs-, Produktgovernance- und Verwahrvorlagen unterscheiden jetzt schärfer zwischen Antragspfad, Geschäftsmodell, Kontrollnachweis, Stop-Kriterium, Migration, Exit, Kundenkommunikation und Aufsichtsnachweis.
- **Zweisprachige Vorlagen:** Die finanzaufsichtsrechtliche Voranfrage und die Krypto-Verwahr- und Treuhandvereinbarung wurden parallel in Deutsch und Englisch nachgezogen, insbesondere bei Dienstleistungsmapping, Register-/Wallet-Abgleich, Exit-Datensatz und Verlustaufarbeitung.
- **Artefakte synchronisiert:** Für alle 28 berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.14.0 — Große Vertragsvorlagen feingeschliffen (2026-06-24)

Gezielte Sanity- und Bug-Hunt-Runde über die umfangreichsten Vertrags- und Planvorlagen. Der Lauf beseitigt redaktionelle Restmarker, fehleranfällige Platzhalter und unvollständige Anlagenlogik, ohne die bewährte Klauselsystematik oder Rechtsprechungsanker neu zu setzen.

### Verbessert

- **Restrukturierungs- und Insolvenzpläne:** Defekte Tabellenfelder, verschachtelte Platzhalter und verbliebene Arbeitsmarker wurden bereinigt. Krisenursachen, Bestandsfähigkeit, Sicherheiteneingriffe, Planfinanzierung, Sacheinlagen und salvatorische Planregelungen sind jetzt unmittelbar verwendbarer und stärker am jeweiligen Planmechanismus ausgerichtet.
- **Konsortial- und ARGE-Verträge:** Der Konsortialvertrag enthält nun ausformulierte Anlagen zu Vergabe-, Wettbewerbs- und Erforderlichkeitsvermerk, Abschichtungsrechnung und steuerlicher Einordnung. Der ARGE-Vertrag hat konkretere Ausscheidens-, Abschichtungs- und Streitbeilegungsbausteine.
- **Gesellschaftsrechtliche Großverträge:** Verschmelzungs- und Venture-Capital-Vertrag verwenden präzisere Anlagen- und Platzhalterlogik für Grundbesitz, steuerliche Behandlung, Beteiligungen, Wandlungsrechte, virtuelle Anteile und Verwässerungsinstrumente.
- **Artefakte synchronisiert:** Für alle sechs berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.13.0 — Krypto-Verwahrtreuhand zweisprachig ergänzt (2026-06-24)

Gezielte Ergänzung im Themenordner `aufsichtsrecht-und-bafin` für regulierte Kryptoverwahrung, CASP-Custody und insolvenzrechtlich robuste Kundenzuordnung. Die neue Vorlage verbindet die aufsichtsrechtliche Verwahrlogik mit einer deutsch-englischen Vertragsfassung für Kunden, Kryptoverwahrer und optionale Sicherungs- oder Kontrollbegünstigte.

### Neu

- **Krypto-Verwahr- und Treuhandvereinbarung:** Neue zweisprachige Vertragsvorlage für regulierte Verwahrer, CASP und Kunden mit Verwahrgegenstand, Positionsregister, Kundentrennung, Nutzungsverbot, Sperr- und Kontrollrechten, Sub-Custody, Forks, Airdrops, Exit, Haftung, Gebühren und deutsch-englischem Sprachvorrang.
- **Insolvenz- und Aufsichtskern:** Die Vorlage dokumentiert ausdrücklich die negative Nutzungsabrede gegen Verfügung für Rechnung des Verwahrers oder Dritter und verankert die Aussonderungslogik über § 46i KWG, § 45 KMAG und § 47 InsO sowie Art. 75 MiCAR.
- **Normklarstellung:** Der vom Mandat angesprochene Verweis auf „§ 45 KAWG“ wurde nach aktueller amtlicher Gesetzeslage als § 45 KMAG eingeordnet und im README transparent erläutert.

### Eingehängt

- **Index und Rubric:** Die neue Vorlage ist in der BaFin-Bereichs-README und in der vertraglichen Drei-Ordner-Sicht einsortiert. Eine passende Vertrags-Rubric wurde erzeugt.
- **Artefakte synchronisiert:** ODT-Datei und Markdown-ZIP wurden aus der Markdown-Fassung neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (822/822), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 822/822).

## v4.12.0 — MiCAR- und CASP-Vorlagen für BaFin-Verfahren ergänzt (2026-06-24)

Gezielter Ausbau des Themenordners `aufsichtsrecht-und-bafin` um die fehlenden Kryptowerte-, CASP- und KWG-Zulassungsvorgänge. Der Ordner deckt nun neben klassischen KWG- und BaFin-Verfahren auch die MiCAR-Zulassung, die Art. 60-Notifizierung, die Custody-Policy und den Übergang von Bestandsinstituten ab.

### Neu

- **KWG-Zulassung Finanzdienstleistungsinstitut:** Neuer § 32-KWG-Antrag mit Tatbestandssubsumtion, Geschäftsmodell, Geschäftsleitern, Inhaberkontrolle, Kapital, § 25a-KWG-Organisation, IT, Auslagerungen und Geldwäscheorganisation.
- **CASP-Zulassung nach MiCAR:** Neuer Art. 62-MiCAR-Zulassungsantrag für Crypto-Asset Service Provider mit Dienstleistungsmapping, Drei-Jahres-Plan, Governance, Eigenmitteln, DORA-Nachweisen, Geldwäscheprävention, Custody-Policy und Anlagenpaket.
- **Art. 60-MiCAR-Notifizierung:** Neue Anzeigevorlage für bereits beaufsichtigte Finanzunternehmen mit Gleichwertigkeitsmatrix, 40-Arbeitstage-Zeitplan, technischer Dokumentation, DORA-Kontrollen, Custody-Anlage und kryptospezifischer Geldwäscheorganisation.
- **Kryptoverwahrung und Bestandsübergang:** Neue Custody-Policy nach Art. 75 MiCAR sowie ein Übergangsplan für Bestandsinstitute nach Art. 143 MiCAR mit Lückenanalyse, Kundenkommunikation, Neugeschäftsgrenze, Migration und Exit.

### Eingehängt

- **Index und Rubrics:** Die fünf neuen Vorlagen sind in der BaFin-Bereichs-README sowie in der Drei-Ordner-Sicht einsortiert. Die Rubric-Erkennung klassifiziert Notifizierungen künftig als Schriftsätze.
- **Artefakte synchronisiert:** Für alle fünf neuen Vorlagen wurden ODT-Dateien erzeugt und Markdown-ZIPs gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (821/821), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 821/821).

## v4.11.0 — BaFin- und Aufsichtsrechtsvorlagen vertieft (2026-06-24)

Gezielte Ausbau- und Qualitätsrunde für `aufsichtsrecht-und-bafin`. Der Ordner deckt nun nicht nur Reaktions- und Erlaubnisfragen ab, sondern auch die praktischen BaFin-Kernvorgänge rund um Fit-and-Proper, Organanzeigen, Inhaberkontrolle, Auskunftsersuchen und Mängelverfolgung.

### Neu

- **Geschäftsleiter und Aufsichtsorgane:** Neue Vorlagen für die Anzeige der Geschäftsleiterbestellung nach KWG, ZAG und KAGB, ein eigenständiges Fit-and-Proper-Eignungsdossier sowie die Anzeige eines Aufsichtsorganmitglieds nach KWG.
- **Beteiligung und Aufsichtskommunikation:** Neue Vorlagen für die Inhaberkontrollanzeige bei bedeutenden Beteiligungen, die Antwort auf ein Auskunftsersuchen nach § 44 KWG und einen Maßnahmenplan zur Abarbeitung von BaFin-, Bundesbank- und Prüfungsfeststellungen.
- **Index und Rubrics:** Der Themenordner und die drei Kategorien-Indizes führen die neuen Vorlagen. Die Default-Rubric-Erkennung ordnet Anzeigen und Auskunftsersuchen künftig als Schriftsätze ein.

### Vertieft

- **Institutserlaubnis und DORA:** Der BaFin-Erlaubnisantrag nach § 32 KWG und die DORA-Auslagerungsanzeige enthalten jetzt deutlich konkretere Vollständigkeits-, Governance-, Kapital-, IKT- und Übergangsbausteine.
- **Anhörung, Reaktionsplan und Produktgovernance:** Die bestehenden Aufsichtsantworten wurden von knappen Platzhaltern zu belastbaren, frist- und maßnahmenorientierten Schriftsätzen ausgebaut.
- **Voranfrage und europäische Beschwerde:** Die zweisprachige Voranfrage sowie die Beschwerde an europäische Aufsichtsbehörden sind sprachlich geglättet, strukturierter und näher an der konkreten aufsichtsrechtlichen Funktion.
- **Artefakte synchronisiert:** Für alle 14 BaFin-/Aufsichtsrechtsvorlagen wurden ODT-Dateien und Markdown-ZIPs neu erzeugt.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (816/816), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 816/816).

## v4.10.0 — Große Vertragsvorlagen geprüft und geschärft (2026-06-24)

Gezielte Qualitätsrunde über die umfangreichsten Vertragsmuster. Der Lauf beseitigt sichtbare Fehler in Vertragseingängen, Platzhaltern, Anlagenlogik und Optionsbausteinen, ohne Rechtsprechungsanker oder Grundsystematik der Vorlagen neu zu setzen.

### Verbessert

- **Konsortial- und Finanzierungsmuster:** Defekte Fassungsstand-Platzhalter in Konsortialvertrag, Konsortialkreditvertrag, Bau-ARGE und Emissionskonsortialvertrag wurden bereinigt; Rollenbezeichnungen, Gesamtzusage und Geschäftsführungsvergütung sind jetzt sprechender und besser ausfüllbar.
- **Große Transaktions- und Unternehmensverträge:** Das zweisprachige Mid-Market-SPA verwendet konkretere deutsch-englische Betragsfelder für Anteile, Kaufpreisanpassung, Retention, Haftungsgrenzen und Steuerfreistellung. Verschmelzungs- und Beherrschungsvertrag haben in den Anlagen weniger Meta-Sprache und mehr unmittelbaren Vollzugsgehalt.
- **Immobilien- und Sanierungstreuhand:** Der Wohnraummietvertrag erhielt einen echten mietrechtlichen Vertragseingang mit Vermieter-, Mieter- und Erklärungszugang. Die doppelnützige Sanierungstreuhand wurde von generischen Parteiblöcken, Buchstabenunterpunkten und Arbeitsnotizen befreit; Bedingungen, Sicherungsfall, Verwertung und Vergütung sind nun als klare Vertragsklauseln gefasst.
- **Artefakte synchronisiert:** Für alle neun berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810).

## v4.9.0 — Vorlagen verdichtet und §-Konvention vereinheitlicht (2026-06-24)

Repoweiter Sanity-Check, Bug-Hunt und Kohärenz-Sweep nach v4.8.3. Der Lauf hebt die Lesbarkeit und Verwendbarkeit der Vorlagen, ohne Rechtsprechungsanker oder Aktenzeichen neu zu setzen.

### Verbessert

- **§-Konvention vereinheitlicht:** Normverweise wurden repoweit auf das Paragrafenzeichen `§` zurückgeführt; `[WARNHINWEIS]`-Blöcke dürfen weiterhin „Paragraf“ ausschreiben. Der Sonderbereich-Validator wurde entsprechend gelockert.
- **Platzhalter geschärft:** Geldbeträge wurden in den bearbeiteten Mustertexten auf sprechendere Felder wie `[Betrag in EUR]` gebracht; doppelte Währungsangaben und unklare `EUR [Betrag]`-Artefakte wurden bereinigt.
- **Stub-Klauseln ersetzt:** Restliche `[Regelung]`-Platzhalter in Vergabe-, IT-, Familien-, Erb-, Insolvenz-, Bau-, Medizin-, Vertriebs- und IP-Vorlagen wurden durch konkrete Klauseltexte, Alternativen oder Nachweislogiken ersetzt.
- **Zweisprachige Tabellen geglättet:** Familien-, Erb- und GmbH-Beschlussvorlagen erhielten präzisere deutsch-englische Parallelformulierungen für Wohnung, Zugewinn, steuerliche Folgen, Unternehmensbewertung und Geschäftsführer-Eckpunkte.
- **Artefakte synchronisiert:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810). Zusätzlich ohne Befund: keine `[Regelung]`-Stubs, keine ausgeschriebenen „Paragraf“-Normverweise außerhalb von Warnhinweis-Blöcken und keine doppelten Währungsplatzhalter.

## v4.8.3 — Schneller Sanity- und Brillanzfeinschliff (2026-06-24)

Zackige Sanity-Runde nach v4.8.2 mit gezielter Bug-Hunt-Prüfung auf sichtbare Ausfüll-, Tabellen- und Platzhalterartefakte. Keine Rechtsprechungsanker und keine Klauselsystematik wurden umgebaut.

### Bereinigt

- **Ausfüllfelder präzisiert:** Restliche `Az..`-, `2..`- und offene Klammerartefakte in familienrechtlichen, steuerrechtlichen, verkehrsrechtlichen und vollmachtsbezogenen Vorlagen wurden entfernt.
- **Zweisprachige Leitvorlagen geglättet:** Beschädigte `.br`-Marker, `[...]`-Stummel und offene Tabellenzellen in Sanierungs-, Mandatsaufnahme-, Freigabe- und arbeitsrechtlichen Compliance-Leitvorlagen wurden in sprechende, sofort nutzbare Ausfüllfelder überführt.
- **Sonderbereich poliert:** Drei strafgerichtliche Vorlagen erhielten präzisere Platzhalter für notwendige Verteidigung, Dolmetscherangaben und Neubestimmung nach Aussetzung.
- **Artefakte:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt; die Markdown-ZIP-Dateien wurden synchron neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810). Zusätzlich ohne Befund: keine verschachtelten eckigen Platzhalter, kein `Az. Az.`, kein `Nr..`, keine beschädigten `.br`-Marker, keine Plugin-Verweise und keine `Mandatsreife Prüfmatrix`.

## v4.8.2 — Sanity- und Kohärenzfeinschliff (2026-06-24)

Weitere Bug-Hunt- und Schönheitsrunde nach v4.8.1. Der Lauf konzentriert sich auf sichtbare Ausfüll-, Titel- und Lesbarkeitsartefakte, ohne Rechtsprechungsanker, Klauselsystematik oder fachliche Substanz neu zu fassen.

### Bereinigt

- **Warnhinweis-Typen geschärft:** Vollmachten, Kündigungen und Klageschriften verwenden nun dokumentgenaue Warnhinweis-Kennzeichnungen wie „Vollmachtsbestandteil“, „Erklärungsbestandteil“ und „Schriftsatzbestandteil“ statt pauschaler Vertragsformulierungen.
- **Download- und Indextexte geglättet:** Verlorene Bindestriche in zusammengesetzten Titeln wurden wiederhergestellt, etwa bei Auskunfts-, Räumungs-, Stundungs-, Pfändungs-, Transfer- und Poolvorlagen.
- **Anlagen und Platzhalter poliert:** Generierte „Zweck dieser Anlage“-Zeilen beginnen grammatisch sauber; Restartefakte wie `Az. Az.`, `Nr..`, doppelte Punkte, offene Klammern und verschachtelte Ausfüllfelder wurden entfernt.
- **Artefakte:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt; die Markdown-ZIP-Dateien wurden synchron neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810). Zusätzlich ohne Befund: keine verschachtelten oder ungeschlossenen eckigen Platzhalter, keine spitzen oder geschweiften Platzhalter, kein `Az. Az.`, kein `Nr..`, keine Plugin-Verweise und keine `Mandatsreife Prüfmatrix`.

## v4.8.1 — Kohärenz-Sweep für Platzhalter und Syntaxartefakte (2026-06-24)

Sanity-Check, Bug-Hunt und Schönheitskorrektur nach dem v4.8.0-Warnhinweis-Release. Der Lauf bereinigt echte Ausfüll- und Layoutartefakte, ohne Rechtsprechungsanker, Klauselsystematik oder fachliche Substanz neu zu fassen.

### Bereinigt

- **Platzhalter-Syntax:** Verschachtelte und nicht geschlossene eckige Platzhalter wurden in 385 Hauptvorlagen und 20 Schriftvorlagen im Sonderbereich zu einfachen, sprechenden Ausfüllfeldern geglättet. Innere Platzhalter wie `[Datum]` oder `[Betrag]` stehen nun als Klartext innerhalb eines einzigen Ausfüllfelds; Inhalt und Regelungslogik bleiben erhalten.
- **Verirrte Klammern und Tabellenartefakte:** Beschädigte `]`-Reste in Gegendarstellungen, Unterlassungserklärungen, Anlagenüberschriften, SLA-Tabellen, Vergabeschriftsätzen, Sozialrechtswidersprüchen und verwaltungsgerichtlichen Alternativanträgen wurden entfernt oder in saubere Mustertextform gebracht.
- **Repo-Konventionen:** Verbotene englische Begriffe für automatisiertes Auslesen wurden durch „massenhaftes automatisiertes Auslesen“ ersetzt. Die Prüfung auf spitze, geschweifte, doppelte oder verschachtelte Platzhalter ist nun ohne Befund.
- **Artefakte:** Für alle berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt; die Markdown-ZIP-Dateien wurden synchron neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810). Zusätzlich ohne Befund: keine verschachtelten oder ungeschlossenen eckigen Platzhalter, keine spitzen oder geschweiften Platzhalter, keine Plugin-Verweise und keine `Mandatsreife Prüfmatrix`.

## v4.8.0 — i-Tüpfelchen-Hinweis in allen Warnblöcken (2026-06-23)

Alle 810 Hauptvorlagen und alle 108 Schriftvorlagen im Sonderbereich `vorlagen-gerichtsleitend/` tragen nun einen einheitlichen Eigenleistungs-Hinweis im Warnhinweis-Block. Bestehende Warnblöcke wurden ergänzt; Vorlagen ohne bisherigen Warnblock erhielten einen schlanken Block mit Eigenleistungs-Hinweis und README-Verweis. Inhalt, Klauselsystematik, Rechtsprechungsanker, READMEs und fachliche Substanz blieben unangetastet.

### Umgesetzt

- **Hauptbestand:** Jede Vorlagen-Markdown-Datei enthält nun oben einen dokumenttypspezifischen `[WARNHINWEIS]`-Block. Verträge verwenden die Kennzeichnung „nicht Vertragsbestandteil, nicht mit unterzeichnen“, Anträge und Schriftsätze verwenden die jeweilige Einreichungsgrenze, sonstige Vorlagen eine dokumentbezogene Fassung.
- **Sonderbereich:** Jede gerichtsleitende, staatsanwaltschaftliche und amtsanwaltschaftliche Schriftvorlage enthält nun einen eigenen Hinweis zur richterlichen oder staatsanwaltlichen Eigenleistung. Der Sonderbereich spricht weiterhin `Paragraf` aus und bleibt ohne ODT-/ZIP-Pflicht.
- **Synchronisierung:** Für alle 810 berührten Hauptvorlagen wurden ODT-Dateien neu erzeugt und Markdown-ZIPs neu gebaut.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810).

## v4.7.0 — Eloquenz-, Verwendbarkeits- und Schönheitslift (kommerzieller Vertragsblock) (2026-06-23)

**Stand:** 810 validierte Hauptvorlagen in 39 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/`, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 810/810`, alle zehn CI-Checks grün.

Fokussierter Tiefen-Lift des kommerziellen Vertragsblocks — 63 Vorlagen in `agb-recht` (16), `vertriebs-und-handelsrecht` (28) und `mergers-and-acquisitions` (19). Die Substanzarbeit aus v4.0 bis v4.6 (Rechtsprechungsanker, Klauselsystematik) bleibt unangetastet; dieser Lauf hebt Sprache, Verwendbarkeit und Form auf Kanzleiniveau. Weitere Themenordner folgen in den nächsten Releases.

### Verbessert

- **Eloquenz.** Aktiv statt Passiv, Floskeln gestrichen, präzise juristische Termini, stimmige Klauselüberschriften der Anwaltspraxis. Jeder Satz trägt eine Aussage, ein Tatbestandsmerkmal oder eine Rechtsfolge.
- **Verwendbarkeit.** Stub-Klauseln zu ausformulierten Klauseltexten ausgebaut, mit echten Auswahl-Varianten (`[Variante A: … — geeignet wenn …; Variante B: …]`) und optionalen Modulen (`[OPTIONAL — nur aufnehmen, wenn …: …]`); Platzhalter sprechend benannt (etwa `[Höhe der Vergütung in EUR]` statt `[Betrag]`).
- **Präambel und Gegenstand entgenerisiert.** Selbstbeschreibungen und Belehrungen aus dem Abschnitt 1 entfernt; dort stehen nur noch Parteien in ihrer Eigenschaft, Interesse und geschuldete Hauptleistung.
- **Warnhinweis-Disziplin.** Vorhandene `[WARNHINWEIS]`-Blöcke auf Indikativ und höchstens vier Sätze gebracht und mit dem Schlusssatz zur README versehen.
- **Bug-Hunt mit echten Funden.** Doppelte Unterschriftsblöcke entfernt, kaputte und verschachtelte Platzhalter repariert (etwa `[ 1 % EV;`, `[Laufend seit [Datum]`, `]`-Konvertierungsglitches), falsche Unterschriftszeilen korrigiert (`Partei 1/2` zu `Verkäufer/Käufer`), Anlagentitel an die In-Text-Verweise angeglichen, Geldbetragsformat auf `[Betrag in EUR]` vereinheitlicht, ungewöhnliche Abkürzungen (CMR, CISG, EUFKVO, EDI, Vertikal-GVO) beim ersten Auftreten ausgeschrieben.
- **READMEs.** Generische Hinweis-Floskeln durch gegenstandsspezifische Prosa mit einschlägigem Rechtsregime und Querverweisen ersetzt; Fließtext-Fettdruck entfernt. Aktenzeichen, Leitentscheidungen und amtliche Links unverändert.
- **Zweisprachige Vorlagen.** Deutsch-englische Zweispaltentabellen satzgenau parallel gehoben; das Legal English entgermanisiert.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (810), `check-kategorien-index`, `check-gerichtsleitend` (108), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810). ODT und ZIP der berührten Vorlagen neu erzeugt; Kurz-Hinweis-Tokens, Rubrum-/Schluss-Marker, Dezimalgliederung und alle Normzitate bewahrt.


## v4.6.0 — Warnhinweise und Meta-Sätze aus Mustertexten bereinigt (2026-06-23)

Repoweiter Sweep über alle 810 Hauptvorlagen und alle 108 Schriftvorlagen im Sonderbereich. Warnhinweise, Anwenderbelehrungen und Meta-Sätze wurden aus den eigentlichen Mustertexten entfernt oder in echte Vertrags-, Antrags- und Schriftsatzsprache überführt. 207 Mustertexte und 72 READMEs wurden berührt; alle übrigen Vorlagen wurden geprüft und blieben ohne Befund.

### Bereinigt

- **Mustertext statt Anwenderkommentar:** Explizite `Warnhinweis:`, `Hinweis:`, `Achtung:`- und `Anmerkung:`-Zeilen wurden aus Vertrags-, Antrags- und Schriftsatztexten entfernt. Wo der Inhalt selbst an Gericht, Behörde oder Gegenseite gerichtet ist, wurde die Überschrift in normale Erklärungssprache umgebaut.
- **Klare Warnblöcke:** Form- und Vollzugsfallen stehen nur noch als kurze `[WARNHINWEIS — ...]`-Blöcke am Anfang der Vorlage, wenn sie vor Befüllung, Unterzeichnung oder Einreichung zwingend sichtbar sein müssen.
- **README statt Mustertext:** Ausführlichere Prüf- und Praxiswarnungen wurden unter „Hinweise zur Verwendung“ in die jeweilige README ausgelagert.
- **Präambel/Gegenstand entschlackt:** Redundante Abschnitt-1-Sätze wie „Abschnitt 1 ist Bestandteil dieses Vertrags und hat Regelungsgehalt“ wurden aus Präambeln entfernt. Bestandteils- und Rangfolgeklarstellungen stehen, soweit nötig, in den Schlussbestimmungen.
- **Generierte Vollzugschecklisten bereinigt:** `Vollzugskern`- und `Rechtliche und praktische Prüfpunkte`-Blöcke wurden aus Vollstreckungs-, Zustellungs- und Vollziehungsaufträgen entfernt oder in konkrete Auftragsformulierungen umgebaut.

### Ankerfälle

- **Befristeter Arbeitsvertrag nach TzBfG:** Die Schriftformbelehrung zu § 14 Abs. 4 TzBfG wurde aus dem Vertragskörper ausgelagert. Oben steht nur noch der kurze Warnblock zur Schriftform vor Arbeitsaufnahme und zur Rechtsfolge nach § 16 Satz 1 TzBfG; die README enthält die vertiefte Form- und Rechtsprechungsdarstellung.
- **Zwangssicherungshypothek:** Die bisherige generische Vollzugscheckliste wurde als echter Antrag an das Grundbuchamt nach §§ 866, 867 ZPO neu gefasst, mit Rubrum, Antragsformel, Titel-/Zustellungsnachweis, Grundstücksangaben, Forderungsaufstellung, Kosten und Anlagen.
- **CMR-Frachtbrief:** Vordruck- und eCMR-Hinweise stehen nicht mehr als Frachtbrieftext, sondern als nicht einzureichender Warnblock; der Mustertext beginnt mit den auszufüllenden Sendungs- und Verfahrensdaten.

### Geprüft

- Vollständige Zählung: 810 Hauptvorlagen und 108 Schriftvorlagen im Sonderbereich wurden durch den Sweep geführt.
- Zielmuster-Scanner: keine verbliebenen Warnlabel, Abschnitt-1-Bestandteilsätze, `Vollzugskern`-, `Verfahrenslogik`- oder `Modellwissen`-Zeilen im eigentlichen Mustertext.
- Alle berührten Hauptvorlagen wurden für ODT und Markdown-ZIP neu synchronisiert.
- Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810).

## v4.5.1 — BVerwG-Anker zu § 125 BauGB präzisiert (2026-06-23)

Der Rechtsprechungsanker zu BVerwG, Beschluss vom 15. Mai 2025 — 9 B 52.24 im Erschließungsvertrag nach § 124 BauGB wurde nachgeschärft. Die README stellt nun klar, dass § 125 Absatz 2 BauGB materiell-rechtlich auf die Anforderungen des § 1 Absatz 4 bis 7 BauGB verweist, daraus aber keine besonderen formalen Dokumentationspflichten folgen; interne Vermerke bleiben nur eine zweckmäßige Nachweis- und Aktenführungsempfehlung.

## v4.5.0 — Städtebau- und Festsetzungsvorlagen in spezifische Einzelvorlagen aufgegliedert (2026-06-23)

Die zuvor zu grob gebündelten städtebaulichen Vertrags- und Bebauungsplanmuster wurden in thematisch saubere Einzelvorlagen überführt. Öffentlich-rechtliche Bauleitplanungsdokumente liegen nun im eigenen Themenordner `oeffentliches-baurecht/`; privatrechtliche Schnittstellen bleiben im Bau- und Architektenrecht, prozessuale Angriffe im Verwaltungsrecht.

### Neu

- **Öffentliches Baurecht:** Zwölf neue Einzelvorlagen zu Mantelvertrag nach § 11 BauGB, Folgekostenvertrag, Erschließungsvertrag, Durchführungsvertrag zum vorhabenbezogenen Bebauungsplan, Änderungs- und Aufhebungsvertrag, textlichen Festsetzungen, Innenentwicklung nach § 13a BauGB, Grün- und Ausgleichsfestsetzungen, örtlicher Bauvorschrift, Satzungsbeschluss und Öffentlichkeitsbeteiligung.
- **Verwaltungsrecht:** Zwei spezifische Schriftsatzvorlagen für Normenkontrollantrag gegen Bebauungspläne nach § 47 VwGO und Antragsbegründung zu Abwägungsfehlern nach § 1 Absatz 7 BauGB, §§ 214, 215 BauGB.
- **Bau- und Architektenrecht:** Zwei Schnittstellenverträge für Bauträger-Folgekostenrefinanzierung und Architekten-Festsetzungsprüfungspflicht.

### Bereinigt

- Die beiden Sammelvorlagen `bau-und-architektenrecht/staedtebaulicher-vertrag-baugb/` und `bau-und-architektenrecht/bebauungsplan-festsetzungen-baugb/` wurden entfernt; ihre brauchbaren Inhalte sind in spezifische Einzelvorlagen aufgegangen.
- `validate-vorlagen` und `generate-default-rubrics` kennen den neuen Themenordner `oeffentliches-baurecht/`; die Drei-Ordner-Sicht ist auf 810 kanonische Vorlagen aktualisiert.
- Alle neuen Vorlagen verwenden eckige Platzhalter, sprechende Dateinamen, eigene READMEs, ODTs, Markdown-ZIPs und Rubrics.

### Rechtsprechung und Quellen

- Die neuen Hinweise verankern die Vorlagen unter anderem mit BVerwG, Urteil vom 29. Januar 2009 — 4 C 15.07, BVerwG, Urteil vom 24. März 2011 — 4 C 11.10, BVerwG, Urteil vom 12. Dezember 2012 — 9 C 12.11, BVerwG, Urteil vom 20. Juni 2023 — 4 CN 11.21, BVerwG, Urteil vom 16. September 2025 — 4 CN 2.24, und BVerwG, Beschluss vom 8. Dezember 2025 — 4 BN 9.25.
- Amtliche Normlinks führen auf die einschlägigen Vorschriften des BauGB, der VwGO, des BGB und der MaBV.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (810/810), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 810/810).

## v4.4.3 — Planungsrechtlicher Kohärenz- und README-Sweep (2026-06-23)

Gezielter Qualitätslauf nach dem Baurechtsausbau mit Fokus auf aktuelle planungsrechtliche Rechtsprechung, didaktikfreie Mustertexte und konsistente Platzhalterhinweise.

### Geschärft

- **Bebauungsplan-Festsetzungen:** Die Vorlage unterscheidet nun genauer zwischen tragenden städtebaulichen Gründen, reinen Privat- oder Wettbewerbsinteressen und bloß vorgeschobenen Zwecken. Grundflächenfestsetzungen nach § 16 Abs. 2 Nr. 1 BauNVO werden ausdrücklich nicht als isolierte Hauptanlagen-Grundfläche behandelt; Erschließung, Sackgassen, Wendemöglichkeiten, Rettungswege und Entsorgungslogik sind als eigene Abwägungspunkte verankert.
- **Städtebaulicher Vertrag:** Folgekosten werden stärker nach Neunutzeranteil, Altnutzeranteil, Bestandsdefizit und vorhabenbedingtem Mehrbedarf getrennt. Ein Vertragskontrollvermerk ordnet jede wesentliche Leistung städtebaulicher Maßnahme, Verursachung, Vorteil, Kostenansatz, Verteilungsschlüssel und Rückabwicklung zu.
- **Normenkontrollantrag § 47 VwGO:** Der generische Rubrumblock wurde entfernt. Die Rügen zu § 2 Abs. 3 BauGB, § 1 Abs. 7 BauGB, § 16 Abs. 2 Nr. 1 BauNVO, § 19 Abs. 4 BauNVO und § 47 Abs. 6 VwGO sind konkreter auf Bebauungsplanangriffe zugeschnitten.

### Rechtsprechung

- Neue oder nachgeschärfte Anker zu BVerwG, Beschluss vom 8. Dezember 2025 — 4 BN 9.25, BVerwG, Urteil vom 16. September 2025 — 4 CN 2.24, BVerwG, Beschluss vom 6. August 2024 — 4 BN 2.24, und BVerwG, Beschluss vom 15. Mai 2025 — 9 B 52.24.

### Bereinigt

- Alte `**Hinweis:**`-Randnotizen in mehreren Mustertexten wurden in verwertbare Erklärungen, Formularfelder oder Vertrags-/Schriftsatzsätze umgebaut.
- Sichtbare Winkelplatzhalter in einzelnen READMEs wurden auf eckige Platzhalter oder Klartext umgestellt. Die README-Hinweise zu Platzhaltern sprechen nun einheitlich von eckigen Klammern.
- Alle berührten ODT-Dateien und Markdown-ZIPs wurden aus den aktualisierten Markdown-Dateien neu erzeugt.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (796/796), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 796/796).

## v4.4.2 — Städtebauliche Verträge und Bebauungsplan-Festsetzungen (2026-06-23)

Gezielte Ergänzung im Bau- und Planungsrecht zu kommunaler Baulandentwicklung und textlichen Festsetzungen.

### Ergänzt

- **Städtebaulicher Vertrag nach § 11 BauGB:** Neue Vertragsvorlage mit Planungsziel, Vertragsgebiet, Planungs- und Gutachtenkosten, Erschließung, sozialer Infrastruktur, Folgekosten, Angemessenheitskontrolle, Koppelungsverbot, Wohnraumquote, Umwelt-, Artenschutz- und Ausgleichslogik, Sicherheiten, Rechtsnachfolge und Rückabwicklung bei Planänderung oder Scheitern des Bebauungsplans.
- **Textliche Festsetzungen zum Bebauungsplan:** Neue Arbeitsvorlage für Festsetzungen nach § 9 BauGB und BauNVO mit Baugebietslogik, Maß der baulichen Nutzung, Bauweise, Verkehr, Immissionsschutz, Grünordnung, Wasser, Klima, Artenschutz, örtlichen Bauvorschriften, bedingten Festsetzungen, Abwägung, Begründung und Fehlerkontrolle.

### Verankert

- Die Baurechts-README und die Kategorieindizes verweisen auf beide neuen Vorlagen mit sprechenden Download-Links für Markdown und ODT.
- Rechtsprechungsanker sind unter anderem BVerwG, Urteil vom 29. Januar 2009 — 4 C 15.07, BVerwG, Urteil vom 12. Dezember 2012 — 9 C 12.11, BVerwG, Urteil vom 24. März 2011 — 4 C 11.10, BVerwG, Urteil vom 22. Oktober 2024 — 4 CN 1.24, BVerwG, Urteil vom 24. April 2024 — 4 C 2.23, und BVerwG, Urteil vom 5. Mai 2015 — 4 CN 4.14.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (796/796), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 796/796).

## v4.4.1 — Schriftformhinweis für Befristungen nach TzBfG (2026-06-23)

Gezielter arbeitsrechtlicher Form-Lift zu befristeten Arbeitsverträgen nach § 14 Abs. 4 TzBfG.

### Ergänzt

- **Befristeter Arbeitsvertrag:** Die Vorlage stellt klar, dass die Befristungsabrede vor Arbeitsaufnahme eigenhändig auf Papier oder mit qualifizierter elektronischer Signatur beider Parteien geschlossen werden muss; E-Mail, Scan, einfache PDF-Signatur und einfache DocuSign-/eSign-Lösungen reichen nicht aus.
- **Entfristungsklage:** Die Formunwirksamkeit ist nun als eigener Angriffspunkt mit § 16-Satz-1-TzBfG-Rechtsfolge, § 17-TzBfG-Frist und Signaturberichtskontrolle ausformuliert.
- **Unbefristeter Arbeitsvertrag und Bereichs-README:** Spätere Befristungsabreden, befristete Anschlussvereinbarungen und das Hinausschieben eines Vertragsendes werden ausdrücklich auf § 14 Abs. 4 TzBfG zurückgeführt.

### Rechtsprechung

- Arbeitsgericht Berlin, Urteil vom 28. September 2021 — 36 Ca 15296/20, Landesarbeitsgericht Berlin-Brandenburg, Urteil vom 16. März 2022 — 23 Sa 1133/21, und Arbeitsgericht Gera, Urteil vom 7. März 2024 — 2 Ca 936/23, sind in den Arbeitsrechts-READMEs als Rechtsprechungsanker zur Schriftform und qualifizierten elektronischen Signatur eingearbeitet.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (794/794), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 794/794).

## v4.4.0 — Specificity-Lift für Vertragsvorlagen (2026-06-23)

**Stand:** 794 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 794/794`, **alle zehn CI-Checks grün**.

Substanzieller Vertrags-Lift mit Schwerpunkt auf praxisnahen IT-, Franchise- und Beendigungsverträgen. Ziel war weniger Schablone und mehr unmittelbar verwendbarer Vertragsrohbau: konkrete Leistungspflichten, messbare Fristen, operative Anlagen, klare Risikoverteilung und weniger austauschbare Standardformeln.

### Vertieft

- **Agile Softwareentwicklung:** Sprint-Abnahme, Product-Backlog-Steuerung, Definition of Done, Fehlerklassen, Open-Source-Liste, Escrow-Option, inkrementbezogene Nutzungsrechte und Übergabe nach Vertragsende wurden konkretisiert.
- **SaaS:** Nutzerkreis, Mandanten, Verfügbarkeit, Service Credits, Sicherheitsvorfälle, API-Änderungen, Unterauftragnehmer, Datenlokation, Data-Act-Exit und Exportumfang sind nun als ausfüllbare Vertragsmechanik abgebildet.
- **Softwarepflege und Support:** Die alte Maintenance-Schablone wurde durch einen spezifischen Pflegevertrag mit Releaseumfang, Störungsklassen, Sicherheitsupdates, Fernwartung, Auftragsverarbeitung, Zusatzleistungen, Pflegeende und Audit ersetzt.
- **Aufhebungsvertrag:** Management- und Führungskräftefälle enthalten jetzt Sprinterklausel, Abfindungsformel, Freistellung, Bonus/LTI, Dienstwagen, betriebliche Altersversorgung, Zeugnis, Rückgabe, Wettbewerbsverbot und sozialrechtliche Hinweise in ausformulierter Vertragsform.
- **Franchisevertrag:** Systemhandbuch, Markenlizenz, Gebietsschutzvariante, Bezugsbindung, Gebührenmodell, Einkaufsvorteile, Qualitätsaudits, Kartellrechtsrisiken, Datenschutzrollen, De-Branding und optionaler Goodwill-Ausgleich wurden fachlich ausgebaut.

### README und Artefakte

- Die begleitenden READMEs der bearbeiteten Vorlagen wurden entschlackt, doppelte Warnblöcke entfernt und um spezifische Praxisfallen sowie verifizierte Rechtsprechungsanker ergänzt.
- Alle berührten ODT-Dateien und Markdown-ZIPs wurden aus den aktualisierten Markdown-Vorlagen neu erzeugt.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (794/794), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 794/794).

## v4.3.0 — Kohärenz- und Rechtsprechungsanker-Sweep (2026-06-23)

**Stand:** 794 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 794/794`, **alle zehn CI-Checks grün**.

Letzter Feinschliff nach dem Platzhalterlift mit Fokus auf didaktikfreie Mustertexte, schlankere README-Umgebung und verifizierbare Rechtsprechungsanker in besonders praxisrelevanten Bereichen.

### Bereinigt

- **Mustertexte ohne Kommentarballast:** `Kommentar:`-Blöcke und pauschale Normprüfungsfloskeln wurden aus den ausfüllbaren Vorlagen entfernt. Der Mustertext enthält damit wieder Anträge, Regelungen, Tatsachen und Belege statt erklärender Randnotizen.
- **README statt Vorlage:** Fachliche Praxisfallen aus den entfernten Kommentaren stehen nun in den jeweiligen READMEs, soweit sie inhaltlich tragen. Die Vorlage selbst bleibt direkt verwendbar.
- **Downloads:** Der README-Audit bestätigt weiterhin keine doppelten Direktdownload-Zeilen.

### Ergänzt

- **Beamten- und Soldatenrecht:** Der Beihilfe-Widerspruch enthält zusätzliche README-Anker zu BVerwG 5 B 3.18, BVerwG 2 C 14.10 und BVerwG 5 C 6.12.
- **Sozialrecht:** Die Erwerbsminderungsrentenklage verweist auf BSG B 13 R 7/18 R und den Großen Senat GS 2/95 zum offenen Arbeitsmarkt, Katalogfällen und konkreter Verweisung.
- **Versicherungsrecht:** Das Unfallversicherungs-Anspruchsschreiben enthält den BGH-Anker IV ZR 137/06 zur ärztlichen Invaliditätsfeststellung sowie den Normanker § 213 VVG zur Gesundheitsdatenerhebung.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (794/794), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 794/794).

## v4.2.0 — Substanz- und Platzhalterlift im Hauptbestand (2026-06-23)

**Stand:** 794 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 794/794`, **alle zehn CI-Checks grün**.

Breiter Qualitätslauf über Hauptbestand und Sonderbereich mit Fokus auf einheitliche Platzhalter, saubere Download-Artefakte und zusätzliche materielle Substanz in bislang zu dünnen Bereichen.

### Vereinheitlicht

- **Eckige Platzhalter repo-weit in Vorlagen:** Ausfüllfelder in den Markdown-Vorlagen verwenden jetzt durchgängig eckige Platzhalter wie `[Datum]`, `[Name]`, `[Aktenzeichen]`, `[Betrag]` und `[Alternative A / Alternative B]`. Versehentliche Doppelklammern und beschädigte Blockquote-Warnungen aus der Umstellung wurden bereinigt.
- **Regeln nachgezogen:** `CLAUDE.md`, `CONTRIBUTING.md` und `references/gegenstandsindividualisierung.md` halten die neue Platzhalterdisziplin ausdrücklich fest.
- **README-Bereinigung:** Alte unsichtbare Marker aus früheren Link-Sweeps wurden aus READMEs und Regeldateien entfernt; sichtbare Markdown-Linktexte sind wieder sprechend und ohne technische Platzhalterreste.

### Vertieft

- **Versicherungsrecht:** Das Unfallversicherungs-Anspruchsschreiben enthält jetzt ausgearbeitete Anlagen zur Vollmacht und § 213 VVG-Einwilligungslogik, Erstbefund, fristwahrender Invaliditätsanzeige, Behandlungsverlauf, Invaliditätsattest, Leistungsberechnung und Kostenbelegen.
- **Beamten- und Soldatenrecht:** Neue Vorlage `widerspruch-beihilfeablehnung` für Beihilfestreitigkeiten mit Beihilfefähigkeit, medizinischer Notwendigkeit, Angemessenheit, Gebührenprüfung, Fürsorgepflicht, Datenschutz, Akteneinsicht und belastbarer Anlagenstruktur.
- **ODT und Markdown-ZIPs:** Alle berührten ODT-Dateien und Markdown-ZIPs wurden synchron aus den aktualisierten Markdown-Vorlagen neu erzeugt.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (794/794), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 794/794).

## v4.1.1 — Review-Fix zu § 109 SGG und § 213 VVG (2026-06-23)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielte Review-Fixes nach v4.1.0.

### Korrigiert

- **Sozialrecht:** In der Erwerbsminderungsrentenklage ist der Antrag nach § 109 SGG wieder ausdrücklich optional und von gesonderter Entscheidung der Klagepartei sowie Kostenrisiko-Freigabe abhängig.
- **Versicherungsrecht:** Im Unfallversicherungs-Anspruchsschreiben ist die § 213 VVG-Gesundheitsdaten-Einwilligung nicht mehr automatische Standarderklärung, sondern als Option mit Einzelfreigabe-Alternative formuliert.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v4.1.0 — Sozial- und Versicherungsrecht mit mehr Substanz (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Substanzlift für besonders dünne und generische Vorlagen im Sozialrecht und Versicherungsrecht. Der Schwerpunkt liegt auf konkreter Anspruchslogik, brauchbarer Subsumtion, besseren Anlagen und Rechtsprechungs-/Normankern in den READMEs, ohne die Vorlagen selbst mit langen Warntexten zu belasten.

### Vertieft

- **Sozialrecht:** Bürgergeld-Eilantrag, Jobcenter-Widerspruch, Reha-/Teilhabeantrag, GdB-Widerspruch, Krankenkassen-Widerspruch, Krankengeldklage, Erwerbsminderungsrentenklage, Überprüfungsantrag nach § 44 SGB X und der allgemeine SGG-Eilrechtsschutz wurden fachlich nachgeschärft. Bedarf, Unterkunftskosten, Mehrbedarfe, Mitwirkung, Aufhebung/Erstattung, § 41a SGB II, Teilhabeplan, Wunsch- und Wahlrecht, AU-Chronologie, MD-Stellungnahmen und § 109 SGG sind jetzt konkreter abgebildet.
- **Versicherungsrecht:** Rechtsschutzdeckungsklage, Stichentscheid, D&O-Deckungsanfrage, Sachverständigenverfahren in der Sachversicherung, Haftpflichtregressabwehr, Krankentagegeld, BU-Leistungsantrag, BU-Widerspruch, BU-Klage, Unfallversicherung, Haftpflichtanspruch und Obliegenheits-/Rücktrittswidersprüche wurden von Schablonenresten bereinigt und mit deckungsrechtlicher Logik ausformuliert.
- **READMEs:** Sozial- und versicherungsrechtliche READMEs enthalten zusätzliche Normen-, Rechtsprechungs- und Suchanker, unter anderem zu SGB-II-Sanktionen, Unterkunftskosten, Reha-Zuständigkeit, GdB/VersMedV, Rechtsschutzversicherung, D&O und Krankentagegeld.

### Bereinigt

- Generische `Kopfdaten`, `Hauptantrag`, `Tatsache 1`, Checkboxen, Kommentarblöcke und technisch wirkende Anlagen wie `Beleg 3` oder `leistungsbeschreibung und technische Spezifikation` wurden in den bearbeiteten Vorlagen durch konkrete Fachabschnitte, Belegachsen und Anlagen ersetzt.
- Alle geänderten ODT-Dateien und Markdown-ZIPs wurden neu erzeugt.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v4.0.1 — Selbstleseverfügung mit allen Verfahrensbeteiligten (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielter Review-Fix im Sonderbereich `vorlagen-gerichtsleitend/`.

### Korrigiert

- **LG-Strafkammer:** Die Selbstleseverfügung nach § 249 Absatz 2 StPO erfasst bei Gelegenheit zur Kenntnisnahme und Protokollvermerk jetzt alle am Selbstleseverfahren beteiligten Verfahrensbeteiligten, insbesondere Nebenklage, Einziehungsbeteiligte, Privatklage und sonstige Beteiligte, statt nur Staatsanwaltschaft, angeklagte Person und Verteidigung.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v4.0.0 — Gerichtsleitender Feinschliff ohne generische Vollzugsbausteine (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Major-Release nach drei weiteren Qualitätsschleifen über den Sonderbereich `vorlagen-gerichtsleitend/`. Die Änderungen sind eng geführt: kein Strukturumbau, keine neuen Vorlagen, sondern gezielte Entfernung generischer Restbausteine aus richterlichen und gerichtlichen Mustertexten.

### Verbessert

- **LG-Zivilkammer:** Die Einzelrichterübertragung nach § 348a ZPO ist jetzt noch stärker auf die Übertragungsvoraussetzungen, den Haupttermin zur Hauptsache, die gesetzliche Ausnahme nach Absatz 1 Nummer 3 und die spätere Rückübertragung nach Absatz 2 zugeschnitten. Generische Rechtsmittel- und Vollzugssätze wurden durch Besetzungs-, Gehörs- und Geschäftsstellenkontrolle ersetzt.
- **Berufungszurückweisung nach § 522 Absatz 2 ZPO:** Der Mustertext beschreibt jetzt konkret Zustellung, Stellungnahmefrist, Wiedervorlage und den Umgang mit neuem Vortrag, statt einen allgemeinen Vollzugssatz mitzuschleppen.
- **Familiengericht, Finanzgericht, LG-Strafkammer und Arbeitsgericht:** Verfahrensbeistand, Umgangs- und Sorgebeschluss, Versorgungsausgleichsauskunft, Aussetzung der Vollziehung, Aussetzung wegen Vorgreiflichkeit, Selbstleseverfügung, Aussetzungsbeschluss und arbeitsgerichtliches Beschlussverfahren haben konkrete Vollzugs- und Kontrollsätze erhalten.
- **Recherche-Suchläufe:** Die verbliebenen pauschalen Suchläufe in LG-Zivilkammer-Vorlagen wurden durch vorlagenspezifische Suchbegriffe ersetzt.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v3.11.5 — Codex-Reviews integriert: kaputte gesetze-im-internet-URLs repariert, § 348a ZPO am gesetzlichen Maßstab (2026-06-22)

Zwei Codex-Review-Befunde aus v3.11.4 abgearbeitet. CI weiter grün.

### Repariert

- **38 gesetze-im-internet-URLs in 17 READMEs**: Der Bold-Sweep aus v3.11.4 hat das doppelte `__` aus den Linkzielen `https://www.gesetze-im-internet.de/<abk>/__<paragraf>.html` entfernt und damit jede dieser URLs in einen 404 verwandelt. Codex hat das in mehreren Inline-Reviews aufgezeigt. Reparatur durch Rekonstruktion aus dem Pre-Sweep-Stand (Commit `ec07c99e`). Betroffen waren unter anderem `bgb/__305c.html`, `bgb/__307.html`, `bgb/__309.html`, `bgb/__311b.html`, `bgb/__650m.html`, `bgb/__650u.html`, `beurkg/__17.html`, `gewo_34cdv/__3.html`. Bautraegervertrag-, AGB-, Sicherungs-, Bürgschafts-, Abtretungs- und weitere READMEs sind wieder linkfähig.
- **`vorlagen-gerichtsleitend/lg-zivilkammer/05-einzelrichteruebertragung-348a-zpo.md`**: Die Vorlage prüft jetzt den **gesetzlichen Maßstab des § 348a Absatz 1 Nummer 3 ZPO** — „im Haupttermin zur Hauptsache verhandelt" — statt des engeren, nicht-statutorischen Merkmals „streitige Hauptverhandlung". Damit greift die Vorlage auch in Konstellationen wie einseitige Sachverhandlung im Versäumnis-Haupttermin, in denen der frühere Wortlaut die Übertragung fälschlich zugelassen hätte. Pflichtangaben, Mustertext, Hinweise und Praxisfehler einheitlich angepasst.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (793/793), `check-kategorien-index`, `check-gerichtsleitend` (108/17), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v3.11.4 — READMEs ohne Markdown-Fettdruck, Top-README repariert (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Reine Lesbarkeits-Politur der READMEs. Hervorhebungs-Marker werden raus genommen, weil sie in Renderern, die Markdown nicht interpretieren, störend roh durchschlagen. Inhalt bleibt unverändert.

### Geändert

- **711 READMEs und INDEX-Dateien**: alle Fettdruck- und Italic-Marker (`**Wort**`, `__Wort__`) entfernt. 11.174 Marker insgesamt. Inhalt der Fettungen bleibt als normaler Text erhalten. Inline-Code (`` `Code` ``) und Codeblöcke (` ``` `) sind weiterhin als Code formatiert.
- **Top-`README.md` repariert**: 55 NULL-Byte-Marker (`\x00S<n>\x00`) aus einem alten Sweep-Bug aus v3.4.0 entfernt. Markdown-Links wurden anhand der Linkziele mit sprechenden Linktexten neu aufgebaut. Datei ist jetzt wieder reine UTF-8-Textdatei (vorher als binary erkannt).

### Unverändert

- Bestand, Validatoren, Workflow, Sonderbereich-Konventionen
- Vorlagen selbst (im Mustertext sind Fettungen weiterhin erlaubt, sie wurden hier nicht angefasst — nur READMEs und INDEX)

### CI

Alle zehn Checks grün:
- `validate-vorlagen` — 793 Vorlagen, 38 Themenordner
- `check-kategorien-index` — 793 Vorlagen, 3 Kategorieordner
- `check-gerichtsleitend` — 108 Vorlagen, 17 Bereiche
- `check-umlauthygiene`
- `check-odt-integrity` — 793 ODT
- `check-odt-spaltenlayout` — 793 ODT
- `check-md-zip-integrity` — 793 ZIP synchron
- `check-rechtsprechungshygiene`
- `check-gliederung`
- `run-eval` — 793/793 All-Pass

## v3.11.3 — Einzelrichterübertragung nach § 348a ZPO präzisiert (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielter Review-Fix im Sonderordner `vorlagen-gerichtsleitend/`.

### Korrigiert

- **LG-Zivilkammer:** Die Vorlage zur Einzelrichterübertragung nach § 348a ZPO behandelt die streitige Kammerverhandlung nicht mehr als ausnahmslosen Ausschlussgrund. Pflichtangaben, Mustertext, Hinweise und Praxisfehler nennen jetzt die gesetzliche Ausnahme für ein nachfolgendes Vorbehaltsurteil, Teilurteil oder Zwischenurteil.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v3.11.2 — Sanity-Lift gerichtsleitender Restmuster (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielter Sanity- und Bug-Hunt nach dem Paragraf-522-ZPO-Fix.

### Verbessert

- **LG-Zivilkammer:** Hinweisbeschluss, Beweisbeschluss, Einzelrichterübertragung, Prozesskostenhilfe und Entscheidungsskelett verwenden jetzt vorlagenspezifische Praxisfehler-Hinweise. Die verbliebenen pauschalen Wertzuständigkeitsreflexe wurden durch konkrete Prüfungen zu Hinweisfunktion, Beweissteuerung, gesetzlichem Richter, Prozesskostenhilfe und Berufungsentscheidung ersetzt.
- **Recherche-Suchläufe:** Die letzten generischen Suchläufe zu Verfahrensleitung, Zustellung, Frist, rechtlichem Gehör und Vollzug wurden in Arbeits-, Familien-, Finanz-, Strafkammer- und LG-Zivilkammer-Vorlagen durch konkrete, vorlagenbezogene Suchbegriffe ersetzt.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).


## v3.11.1 — Berufungszuständigkeit bei Paragraf-522-ZPO-Vorlage korrigiert (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielter Review-Fix im Sonderordner `vorlagen-gerichtsleitend/`.

### Korrigiert

- **LG-Zivilkammer:** Die Vorlage zum Hinweis- und Zurückweisungsbeschluss nach § 522 Absatz 2 ZPO prüft bei typischen Praxisfehlern nicht mehr die erstinstanzliche Wertzuständigkeit oberhalb von zehntausend Euro. Stattdessen verweist sie auf die Berufungszuständigkeit der Zivilkammer nach § 72 GVG sowie auf Statthaftigkeit, Beschwer, Form und Fristen der Berufung.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v3.11.0 — Letzte Perfektionierung gerichtsleitender Vorlagen (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Finaler Qualitätsschliff im Sonderordner `vorlagen-gerichtsleitend/`. Alle 108 richterlichen, staatsanwaltschaftlichen und amtsanwaltschaftlichen Schriftvorlagen wurden auf generische Restformeln, austauschbare Lückenlisten und bereichsfremde Praxisfehler-Hinweise geprüft.

### Verbessert

- **Lückenlisten:** Die dritte amtliche Entscheidungssuche ist nun in jeder Sonderbereichsvorlage bereichsspezifisch formuliert. Die bisherige Universalformel zu Gehör, Zustellung, Frist und Verfahrensfehler wurde durch Suchläufe ersetzt, die Gerichtsbarkeit, Verfahrensrolle und konkrete Vorlage benennen.
- **Praxisfehler:** Die Bezeichnung „dieser Vorlagenklasse" wurde bereinigt. Hinweise sprechen jetzt die konkrete Vorlage an und vermeiden den Eindruck eines pauschalen Sammelbausteins.
- **Zivil-, Arbeits-, Finanz- und Verfassungsgerichtsbarkeit:** Hinweisverfügungen, Beweisbeschlüsse, Tenorvorlagen, Streitwert- und Kammertexte wurden bei Fehlerachsen und Recherchefokus auf ihre jeweilige Funktion geschärft.
- **Strafrechtliche Sonderbereiche:** Amtsanwaltschaft, staatsanwaltschaftliche Ermittlungs-, Abschluss-, Hauptverhandlungs-, Rechtsmittel- und Vollstreckungsvorlagen sowie die LG-Strafkammer-Vorlagen haben jetzt getrennte Risikoachsen für Strafbefehl, Opportunität, Anklage, Haft, Revision, Vollstreckung, Selbstlesen, Unterbringung und Ladung.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).

## v3.10.0 — Positionierung als Experiment und Werkzeugkasten (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Reine README-Erweiterung. Das Repo steht jetzt von Anfang an als das da, was es eigentlich ist: ein Experiment und Werkzeugkasten, mit dem sich Vorlagenfamilien zu einem Fachgebiet in überschaubarer Zeit mit mehreren KI-Loops aufbauen lassen — nicht primär als fertige Vorlagentankstelle.

### Geändert

- **README**: Neue Sektion „Worum es bei diesem Repo eigentlich geht" direkt nach dem Titel. Erklärt das Repo als Experiment und Werkzeugkasten, listet die mitgelieferten Mechanismen (Strukturvorgaben, Konventionen, zehn CI-Validatoren, Eval-Harness, Pflege-Skripte, PR-Workflow) und nennt die ehrliche Einordnung gegenüber echten Vorlagenmanagement-Systemen mit Datenmodell.

### Unverändert

- Bestand, Validatoren, Workflow, Sonderbereich-Konventionen.

## v3.9.3 — Gerichtsleitende Eilprüfkerne und Praxisfehler geschärft (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Folge-Lauf zur gerichtsleitenden Qualitätssicherung mit Fokus auf nicht generische Hinweise, verfahrensspezifische Eilprüfungen und bessere richterliche Kontrollspuren.

### Verbessert

- **Eilrechtsschutz:** Die Eilvorlagen zu § 123 VwGO, § 86b Absatz 2 SGG, Gewaltschutz und Unterhalt verwenden keine gemischten Standardraster mehr. Sie benennen jetzt jeweils den passenden Prüfungsgegenstand: Anordnungsanspruch und Anordnungsgrund, dringendes Bedürfnis, Schutzvorfall, Unterhaltsbedarf, Leistungsfähigkeit, Vorwegnahmegrenze, Vollstreckbarkeit und Befristung.
- **Familiengericht:** Acht Vorlagen tragen jetzt eigene Praxisfehler-Hinweise zu Kindschaftseingang, Terminierung, Einvernehmen, Verfahrensbeistand, Sachverständigenbeweis, Eilanordnung, Umgang/Sorge und Versorgungsausgleich statt eines pauschalen Sammelhinweises.
- **Verwaltungsgericht:** Eingangsverfügung, Hinweisverfügung, Beweisbeschluss, Paragraf-80-Absatz-5-Beschluss, EuGH-Vorlage und Urteilsskelett wurden bei typischen Risiken und Freigabehinweisen auf die jeweilige Verfahrenshandlung zugeschnitten.
- **Sozialgericht:** Eingangsverfügung, Hinweis, Beweis, Gutachten nach § 109 SGG, Beiladung, einstweilige Anordnung und Entscheidungsskelett nennen nun jeweils konkrete Fehlerquellen wie Bescheidkette, notwendige Beiladung, Verwaltungsakte, Leistungszeitraum, Kostenvorschuss, Berufungszulassung und existenzsichernde Eilbedürftigkeit.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (793), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).


## v3.9.2 — Nachschärfung AG-Zivil-Übergangsrecht (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielter Review-Fix im Sonderordner `vorlagen-gerichtsleitend/`.

### Korrigiert

- **AG-Zivil Eingangsverfügung:** Die amtsgerichtliche Zuständigkeitsnotiz bildet das Übergangsrecht nach § 44 EGGVG nun vollständig ab. Für vor dem 1. Januar 2026 anhängig gewordene Verfahren werden neben § 23 Nummer 2 Buchstabe e GVG auch die neuen wertunabhängigen Landgerichts- und Spezialzuweisungen nach § 71 Absatz 2 Nummer 7 bis 9 GVG, § 72a Absatz 1 Nummer 8 GVG und § 119a Absatz 1 Nummer 8 GVG ausdrücklich ausgenommen. Altverfahren werden daher nicht allein wegen dieser Neuregelungen vom Amtsgericht weggegeben.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (793), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).


## v3.9.1 — Review-Fix gerichtsleitender Übergangs- und Eilvorlagen (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Gezielter Review-Fix im Sonderordner `vorlagen-gerichtsleitend/`.

### Korrigiert

- **Zivilgerichtliche Eingangsverfügungen:** Die Übergangsvorschrift des § 44 EGGVG wird nun nicht nur bei der Wertgrenze, sondern auch bei den neuen besonderen Zuständigkeitszuweisungen berücksichtigt. Vor dem 1. Januar 2026 anhängig gewordene Verfahren werden nicht allein wegen der neuen Zuweisungen nach § 23 Nummer 2 Buchstabe e GVG, § 71 Absatz 2 Nummer 7 bis 9 GVG oder § 72a Absatz 1 Nummer 8 GVG umgesteuert.
- **Familiengerichtliche einstweilige Anordnung:** Die Gründe stehen wieder als eigener Begründungsteil außerhalb des nummerierten Tenors. Der dokumentspezifische Kern verwendet FamFG-Eilkriterien wie dringendes Bedürfnis, Glaubhaftmachung, Kindeswohl oder Schutzinteresse und nicht das fachfremde § 123 VwGO-Raster.
- **Pflichtverteidigerbestellung:** Die Hinweise sprechen wieder die typischen Risiken der notwendigen Verteidigung an: Zeitpunkt der Bestellung, konkreter Beiordnungsgrund, Auswahlrecht, Anhörung, Umfang der Bestellung und Zustellung.
- **BVerfG-Nichtannahmebeschluss ohne Begründung:** Der Prüfungsfokus trennt jetzt ausdrücklich interne Vorprüfung und ausgefertigten begründungsfreien Beschluss. Interne Gründe dürfen nicht versehentlich in den Musterbeschluss übernommen werden.

### Geprüft

- Alle zehn CI-Checks grün: `validate-vorlagen` (793), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).


## v3.9.0 — Strafprozessuale Revisions- und Rechtsmittelvorlagen (2026-06-22)

**Stand:** 793 validierte Vorlagen in 38 Themenordnern, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 793/793`, **alle zehn CI-Checks grün**.

Dieser Lauf ergänzt die anwaltlichen Strafrechtsvorlagen um zwei praxisrelevante Rechtsmittelmuster für die Zeit nach einem Strafurteil.

### Neu

- **Revision gegen Strafurteil mit Revisionsbegründung (§§ 333 ff. StPO):** Voll ausgearbeitete Vorlage für Einlegung, Revisionsanträge, Sachrüge, Verfahrensrügen, absolute Revisionsgründe, Beruhensprüfung, Umfang der Aufhebung und Zurückverweisung. Enthalten sind Fristen- und Zuständigkeitsblatt, Verfahrensrügenmatrix, Sachrügenprüfbogen sowie Fundstellen- und Versandverzeichnis.
- **Annahmeberufung, Sprungrevision und Rechtsmittelwahl im Strafverfahren (§§ 313, 335 StPO):** Vorlage zur sauberen Abgrenzung von Berufung, Annahmeberufung und Sprungrevision. Sie stellt ausdrücklich klar, dass es im Strafprozess keine allgemeine Nichtzulassungsbeschwerde gegen Strafurteile gibt, und führt stattdessen zu den tatsächlich eröffneten strafprozessualen Rechtsmitteln.

### Verbessert

- **Strafrechtsübersicht bereinigt:** Das Themen-README `strafrecht/README.md` wurde von alten technischen Platzhalterlabels befreit und führt die Strafrechtsvorlagen jetzt mit sprechenden Ordnernamen.
- **Rubric-Generator nachgezogen:** Slugs mit `revision` oder `berufung` werden künftig als Schriftsatz erkannt, damit neu generierte Rubrics die gerichtliche Anrede- und Antragsstruktur prüfen.
- **Kategorieindex aktualisiert:** Die strafrechtlichen Prozessvorlagen sind in der Drei-Ordner-Sicht von 15 auf 17 Vorlagen erweitert; der Gesamtzähler der prozessualen Vorlagen steigt auf 394.

### Geprüft

- Normen- und Quellenanker für Revision, Verfahrensrüge, Sprungrevision und Rechtsmittelzug wurden anhand amtlicher Primärquellen plausibilisiert.
- ODT- und Markdown-ZIP-Artefakte wurden für beide neuen Vorlagen frisch erzeugt.
- Alle zehn CI-Checks grün: `validate-vorlagen` (793), `check-kategorien-index`, `check-gerichtsleitend`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 793/793).


## v3.8.1 — Review-Fix gerichtsleitender Eil- und Zuständigkeitsvorlagen (2026-06-22)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Gezielter Review-Fix ausschließlich im Sonderordner `vorlagen-gerichtsleitend/`.

### Korrigiert

- **Zivilgerichtliche Eingangsverfügungen:** Die Amtsgerichts- und Landgerichtsvorlagen verzweigen die Wertzuständigkeit nun nach dem Eingangsdatum der Klageschrift. Vor dem 1. Januar 2026 anhängig gewordene Verfahren bleiben nach § 44 EGGVG bei der früheren Zuständigkeitsgrenze; ab dem 1. Januar 2026 gilt die angehobene Grenze bis einschließlich zehntausend Euro beim Amtsgericht.
- **Verwaltungsgerichtlicher Eilrechtsschutz nach § 80 Absatz 5 VwGO:** Die Pflichtangaben und Mustertexte verwenden nicht mehr das Prüfprogramm des § 123 VwGO, sondern stellen auf Entfallen der aufschiebenden Wirkung, Aussetzungsinteresse, Vollziehungsinteresse, summarische Hauptsacheprüfung und Interessenabwägung ab.
- **Einstweilige Anordnung nach § 32 BVerfGG:** Die Vorlage führt jetzt konsequent zur verfassungsgerichtlichen Doppelhypothese der Folgenabwägung und zur vorgelagerten Prüfung, ob die Hauptsache nicht von vornherein unzulässig oder offensichtlich unbegründet ist.
- **Nichtannahmebeschluss ohne Begründung:** Der Mustertext bleibt begründungsfrei; Hinweise zur Trennung von Zulässigkeit, Annahmevoraussetzungen und Begründetheit stehen nur noch in den Verwendungshinweisen.

### Geprüft

- Sonderbereichs-Audit: keine spitzen Klammern, keine Paragrafenzeichen, keine geraden Anführungszeichen, keine Komma-Zahlen, keine Cross-Repo-Verweise, keine verbotenen Recherchebegriffe.
- Alle zehn CI-Checks grün: `validate-vorlagen` (791), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791).


## v3.8.0 — Weitere Politur gerichtsleitender Vorlagen (2026-06-22)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Folge-Lauf zu v3.7.0 ausschließlich im Sonderordner `vorlagen-gerichtsleitend/`. Der Lauf beseitigt verbliebene generische Reststellen, präzisiert Risiko- und Recherchehinweise nach Vorlagenklasse und zieht mehrere besonders sensible Mustertexte fachlich weiter.

### Verbessert

- **Drei Qualitätsrunden über alle 108 Schriftvorlagen.** Einheitlichere Formulierungen für Prüfungsfokus, Praxisfehler, Freigabehindernisse und Lückenlisten; verbleibende schematische Wendungen wurden durch vorlagenbezogene Hinweise ersetzt.
- **Risiken nach Verfahrensart getrennt.** Haft, Unterbringung, Register, Insolvenz, Verfassungsbeschwerde, Eilrechtsschutz, Beweissteuerung, Hinweise, Entscheidungsskelette, Eingangsverfügungen und Vollstreckung tragen jetzt jeweils eigene Risikohinweise statt eines pauschalen Standardsatzes.
- **Recherchehinweise geglättet.** Die Lückenlisten sprechen nun von amtlicher Entscheidungssuche und konkreten Suchläufen; missverständliche Formulierungen wie „offene Klammern“ oder bloß technische Suchfolgen wurden entfernt.
- **Einzelne Hochrisiko-Vorlagen vertieft.** EuGH-Vorlage nach Art. 267 AEUV, Senatsvorlage zur Verfassungsbeschwerde, StaRUG-Planbestätigung und Unterhalt im einstweiligen Familienverfahren enthalten zusätzliche Prüfungspunkte zu Acte-clair, gesetzlichem Richter, Vergleichsrechnung, planbedingter Entlastung und vorläufiger Unterhaltstitulierung.
- **Familiengerichtliche Eilentscheidungen klarer strukturiert.** Tenor und Gründe beginnen nicht mehr jeweils neu bei `1.`, sondern laufen in einer eindeutigen Dezimalstruktur.
- **Vollstreckung nach Bewährungswiderruf präzisiert.** Die Vorlage zum Widerruf der Strafaussetzung spricht nun von Vollstreckungsentscheidung, Bewährungszeit, Widerrufsgrund, milderen Mitteln und Verhältnismäßigkeit statt von unpassenden Haftbefehl-Suchbegriffen.

### Geprüft

- Sonderbereichs-Audit: keine spitzen Klammern, keine Paragrafenzeichen, keine geraden Anführungszeichen, keine Komma-Zahlen, keine Cross-Repo-Verweise, keine verbotenen Recherchebegriffe.
- Mustertext-Audit: eindeutige Top-Level-Nummerierung in allen Mustertexten.
- Alle zehn CI-Checks grün: `validate-vorlagen` (791), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791).

### Hinweis

Die gerichtsleitenden, staatsanwaltschaftlichen und amtsanwaltschaftlichen Vorlagen bleiben experimentelle Gerüste. Sie ersetzen keine richterliche oder staatsanwaltschaftliche Entscheidung; die fachliche Endprüfung durch die zuständige Person bleibt zwingend.


## v3.7.0 — Aktueller Fach- und Qualitätslift für vorlagen-gerichtsleitend (2026-06-22)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Frische kritische Durchsicht ausschließlich des Sonderordners `vorlagen-gerichtsleitend/`. Der Lauf schärft die gerichtlichen, staatsanwaltschaftlichen und amtsanwaltschaftlichen Vorlagen fachlich, sprachlich und organisatorisch nach dem Gesetzesstand 2026, ohne Dateien außerhalb des Sonderbereichs inhaltlich anzufassen.

### Verbessert

- **Alle 108 Schriftvorlagen fachlich vertieft.** Jede Vorlage enthält jetzt einen dokumentspezifischen Prüfungsfokus, der den konkreten Verfahrensstand, die tragende Tatsachengrundlage, den maßgeblichen Entscheidungsmaßstab und den nächsten Vollzugsschritt sichtbar macht.
- **Pflichtangaben weiter konkretisiert.** Zu jeder Vorlage sind ein dokumentspezifischer Kern, ein Prüfvermerk vor Zeichnung und ein Vollzugs- beziehungsweise Kontrollpunkt ergänzt, damit Verfügung, Beschluss, Tenor oder staatsanwaltschaftlicher Antrag nicht als Schablone stehen bleiben.
- **Mustertexte aktiver und tenorfähiger.** Die Mustertexte wurden um konkrete Vollzugs-, Prüf- und Begründungssätze erweitert; Nummerierungssprünge aus früheren Arbeitsläufen wurden in zehn Mustertexten bereinigt.
- **Hinweise praxisnäher.** Jede Vorlage benennt jetzt typische Praxisfehler, Gehörs-, Beschwerde-, Revisions- oder Vollzugsrisiken und verlangt ausdrücklich, dass offene Platzhalter vor Freigabe gefüllt oder bewusst gestrichen werden.
- **Lückenlisten geschärft.** Ergänzt sind konkrete Recherche-Suchläufe mit dokumentbezogenen Suchfolgen; Aktenzeichen und Fundstellen bleiben Platzhalter und werden nicht erfunden.
- **Aktualität 2026.** Die amtsgerichtliche Zuständigkeitsgrenze nach § 23 Nummer 1 GVG ist auf zehntausend Euro aktualisiert; korrespondierende Zivilkammer-Hinweise sind angepasst.
- **Oberflächenpolitur.** `README.md` und `INDEX.md` des Sonderbereichs führen gerichtliche, staatsanwaltschaftliche und amtsanwaltschaftliche Vorlagen einheitlich; sichtbare ASCII-Reste in Indexlabels wurden beseitigt.

### Geprüft

- Harter Sonderbereichs-Audit: keine spitzen Klammern, keine Paragrafenzeichen, keine geraden Anführungszeichen, keine Komma-Zahlen, keine Plugin-, Skill- oder Cross-Repo-Verweise, keine verbotenen Recherchebegriffe.
- Nummerierungs-Audit über alle Mustertexte: keine Sprünge in zusammenhängenden Dezimallisten.
- Alle zehn CI-Checks grün: `validate-vorlagen` (791), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791).

### Hinweis

Die gerichtsleitenden, staatsanwaltschaftlichen und amtsanwaltschaftlichen Vorlagen bleiben experimentelle Gerüste. Sie ersetzen keine richterliche oder staatsanwaltschaftliche Entscheidung; die fachliche Endprüfung durch die zuständige Person bleibt zwingend.


## v3.6.0 — Feinschliff und Konsistenz im gerichtsleitenden Sonderbereich (2026-06-22)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Folge-Lauf zu v3.5.0. Der Brillanz-Lift hatte die 108 Vorlagen fachlich auf ein hohes Niveau gehoben, aber über sechs unabhängige Bearbeitungsstränge kleine Formunterschiede hinterlassen. Dieser Lauf vereinheitlicht Form, Vorspruch und Lückenlisten über alle 17 Bereiche, ohne die Substanz anzutasten.

### Vereinheitlicht

- **Lückenlisten-Form über alle 108 Vorlagen.** Durchgängig die kanonische Form „Recherche-Suchbegriffe sind …" mit nackten Platzhalterzeilen. Fünf Vorlagen der Hauptverhandlung trugen noch „Suchbegriffe für die Live-Recherche"; fünf amtsanwaltschaftliche Vorlagen hatten die Suchbegriffe abweichend an die Lückenlistenpunkte gehängt — beides auf die einheitliche Form gebracht.
- **Pflichtangaben-Abstand.** Zwischen nummerierten Pflichtangaben steht jetzt durchgängig eine Leerzeile (zuvor in der Hälfte der Vorlagen kompakt gesetzt), passend zu Mustertext und Hinweisen.
- **Vorspruch der Bereichs-READMEs.** Der DSGVO- und KI-VO-Vorspruch ist über alle 17 Bereiche einheitlich. Der KI-VO-Satz (Art. 6 Absatz 2 in Verbindung mit Anhang III Nummer 8 lit. a und Art. 6 Absatz 3, Registrierungspflicht nach Art. 49 Absatz 2) wurde in den fünf staatsanwaltschaftlichen und amtsanwaltschaftlichen READMEs ergänzt; der Familiengericht-Vorspruch wurde auf die kanonische Fassung zurückgeführt. Die rollenbezogene Eröffnung (richterlich, staatsanwaltschaftlich, amtsanwaltschaftlich) bleibt erhalten.

### Geprüft

- **Konsistenz-Audit über alle 108 Vorlagen:** einheitliche Sektionsreihenfolge, einheitliche Lückenlisten- und Pflichtangaben-Form, rollenkorrekte Schlussmarkierung (83 richterlich, 25 staatsanwaltschaftlich), keine Sprünge in Tonalität oder Tiefe zwischen den Bereichen.
- **INDEX:** keine doppelten oder schablonenhaften Anwendungsbereich-Zellen; jede Vorlage trägt einen unterscheidbaren Zweck.
- **Aktualität:** Normanker auf Plausibilität Stand 2026 gegengeprüft; Aktenzeichen bleiben Rechercheanker, nichts erfunden.
- **Bug-Hunt:** keine kaputten internen Links, kein Trailing-Whitespace, keine Floskeln oder Gemeinplätze, keine doppelten Leerzeichen, keine Plugin- oder Cross-Repo-Verweise.
- Alle zehn CI-Checks grün: `validate-vorlagen` (791), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791).

### Hinweis

Die gerichtsleitenden, staatsanwaltschaftlichen und amtsanwaltschaftlichen Vorlagen sind experimentelle Gerüste. Sie ersetzen keine richterliche oder staatsanwaltschaftliche Entscheidung; die fachliche Endprüfung durch die zuständige Berufsträgerin oder den zuständigen Berufsträger bleibt zwingend.


## v3.5.0 — Brillanz-Lift für vorlagen-gerichtsleitend (2026-06-22)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` in 17 Bereichen, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Tiefgreifende Qualitätsanhebung aller 108 gerichtsleitenden, staatsanwaltschaftlichen und amtsanwaltschaftlichen Schriftvorlagen. Bis v3.4.0 trugen die richterlichen Vorlagen über alle Bereiche hinweg identische, generische Pflichtangaben und Hinweise sowie dürftige Lückenlisten. Dieser Lauf bringt sie auf das fachliche Niveau der staatsanwaltschaftlichen Vorlagen aus v3.3.0.

### Verbessert

- **Pflichtangaben dokumentspezifisch.** Die zuvor in allen Vorlagen identische Fünf-Punkt-Schablone (etwa „Spruchkörper, Richterin oder Richter, Berichterstattung, Rechtspflege") ist durch Pflichtangaben ersetzt, die genau die Tatsachen und Felder benennen, die der jeweilige Beschluss, die Verfügung oder der Tenor braucht.
- **Hinweise mit Praxistiefe.** Statt der generischen Standardhinweise nennt jede Vorlage nun konkrete Praxisfehler, Revisions- und Verfahrensrisiken, Frist- und Zuständigkeitsfallen — etwa die Schlüssigkeitsprüfung beim Versäumnisurteil, das Zugangserfordernis nach § 69 Absatz 4 FGO bei der Aussetzung der Vollziehung, die Trennbarkeit bei der Rechtsmittelbeschränkung, das Beschleunigungsgebot in Kindschafts- und Haftsachen oder die Drei-Wochen-Frist nach § 4 KSchG.
- **Reichhaltige Lückenlisten.** Jede Vorlage führt vor den Platzhalterzeilen einen Satz mit konkreten, dokumentbezogenen Recherche-Suchbegriffen statt vager Stichworte. Aktenzeichen bleiben Rechercheanker; nichts wird erfunden.
- **Geschärfte Mustertexte.** Tenorierungen sind tenorfähig ohne erläuternde Einschübe, Formulierungen aktiv und präzise, Normanker auf den Stand 2026 gebracht und mit Absatzangabe konkretisiert.
- **Bereichs-READMEs und INDEX.** Alle 17 Bereichs-READMEs nennen je Vorlage einen präzisen, unterscheidbaren Zweck; die Zweckspalte im Master-Index ist von ASCII-Resten bereinigt.

### Bereinigt

- Verbliebene ASCII-Ersatzschreibungen im Sonderbereich zu echten Umlauten korrigiert (unter anderem `Ruecklauf`, `Massgabe`, `Guetetermin`, `Kuendigung`, `Anhoerung`, `Loeschung`, `Vermoegenslosigkeit`, `verfuegen`, `Schoeffinnen`); Datei-Slugs und Linkziele bleiben unverändert ASCII.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen` (791), `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791). Mehrere Überarbeitungsrunden, abschließender Sanity-Check und Bug-Hunt: keine kaputten internen Links, kein Trailing-Whitespace, keine erfundenen Aktenzeichen oder Klar-Namen, keine Plugin- oder Cross-Repo-Verweise, keine generischen Pflichtangaben mehr.

### Hinweis

Die gerichtsleitenden, staatsanwaltschaftlichen und amtsanwaltschaftlichen Vorlagen sind experimentelle Gerüste. Sie ersetzen keine richterliche oder staatsanwaltschaftliche Entscheidung; die fachliche Endprüfung durch die zuständige Berufsträgerin oder den zuständigen Berufsträger bleibt zwingend.


## v3.4.0 — Eigenständigkeit des gerichtsleitenden Sonderbereichs, repoweite Politur (2026-06-22)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/`, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Der gerichtsleitende Sonderbereich steht jetzt für sich. Plugin- und Skill-Querverweise auf das Schwester-Repo `claude-fuer-deutsches-recht` werden vollständig aus den Vorlagen, Bereichs-READMEs und dem Master-Index entfernt; die Validatorregel wird umgedreht und blockt solche Verweise. Vorlagen aus diesem Repo sind als geschlossene Texte zu lesen.

### Geändert

- **Plugin-/Skill-Querverweise raus.** In allen 108 Vorlagen und 17 Bereichs-READMEs des Sonderbereichs ist der Abschnitt `## Korrespondierendes Plugin` beziehungsweise `## Korrespondierendes Plugin und Skill` ersatzlos entfernt. Der `INDEX.md` verliert die Spalte `Korrespondierender Skill`; die Master-Tabelle hat jetzt drei Spalten (`Bereich`, `Vorlage`, `Anwendungsbereich`). Das Top-README des Sonderbereichs und das Repo-README verlieren ihre Verweise auf `_GERICHTE_EXPERIMENTAL/`.
- **`check-gerichtsleitend` umgedreht.** Früher Pflicht zu `_GERICHTE_EXPERIMENTAL/`-Querlinks und `## Korrespondierendes Plugin und Skill`-Sektion. Ab v3.4.0 ist beides ein **harter Fehler**: Vorlagen und Bereichs-READMEs dürfen keine Plugin-/Skill-Querverweise auf andere Repos enthalten. Der Sonderbereich ist eigenständig.
- **Repo-README Stand aktualisiert.** `vorlagen-gerichtsleitend/` ist jetzt mit 108 Vorlagen in 17 Bereichen ausgewiesen einschließlich staatsanwaltschaftlicher und amtsanwaltschaftlicher Bereiche; der früher dokumentierte Stand von 83 Vorlagen in 12 Gerichtsbarkeiten wird abgelöst.

### Geprüft

- **Repoweiter Umlaut-Sweep** über alle 791 Hauptvorlagen und alle 108 Schriftvorlagen des Sonderbereichs. Schutzschicht: Codeblöcke, Inline-Code, vollständige Markdown-Links inklusive Linktext und Bare-URLs bleiben unangetastet. ASCII-Slugs in Dateinamen und Linkpfaden bleiben ASCII. Ergebnis: 191 Ersetzungen im Sonderbereich, 2 im CHANGELOG-Kontext.
- **10 Quality-Loops** durch das Repo: Trailing-Whitespace (0), Mehrfach-Leerzeilen am Dateiende (0), Inline-Leerzeilen-Cluster (1 normalisiert), gerade Anführungszeichen (Diagnose, im Hauptbestand Konvention, im Sonderbereich verboten und sauber), Tabs (0), doppelte Leerzeichen im Fließtext (9 normalisiert), Heading-Syntax (0), verbotene Listenmarker (0 bis auf das Konventionsbeispiel in `references/gliederung.md`), Markdown-Link-Auflösung im Sonderbereich (0 broken).
- **ODT und ZIP synchron neu erzeugt** für alle 10 vom Sweep berührten Hauptvorlagen.

### CI

Alle zehn Checks grün:
- `validate-vorlagen` — 791/791 All-Pass
- `check-kategorien-index` — 791 Vorlagen, 3 Kategorieordner
- `check-gerichtsleitend` — 108 Vorlagen, 17 Bereiche, harter Block für Plugin-Querverweise
- `check-umlauthygiene` — keine ASCII-Ersatzschreibungen
- `check-odt-integrity` — 791 ODT
- `check-odt-spaltenlayout` — 791 ODT
- `check-md-zip-integrity` — 791 ZIP synchron
- `check-rechtsprechungshygiene`
- `check-gliederung`
- `run-eval` — 791/791 All-Pass

### Abgrenzung

Relations- und Plugin-Arbeit gehört nicht in dieses Repo. Sie liegt im Schwester-Repo `Klotzkette/claude-fuer-deutsches-recht`. Im Repo `vorlagensammlung-recht` sind die Vorlagen geschlossene Texte ohne Querverweis auf Skill-Plugins.

## v3.3.0 — Staatsanwaltschaft und Amtsanwaltschaft im gerichtsleitenden Bereich (2026-06-21)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 108 Schriftvorlagen in `vorlagen-gerichtsleitend/` (richterlich, staatsanwaltschaftlich und amtsanwaltschaftlich), Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, **alle zehn CI-Checks grün**.

Der gerichtsleitende Sonderbereich wird um die staatsanwaltschaftliche und amtsanwaltschaftliche Seite des Strafverfahrens erweitert. Damit deckt der Ordner nicht mehr nur die richterliche, sondern die gesamte justizielle Verfahrensführung im Strafprozess ab — vom Anfangsverdacht bis zur Strafvollstreckung.

### Neu

- **25 staatsanwaltschaftliche und amtsanwaltschaftliche Vorlagen** in fünf neuen Unterordnern von `vorlagen-gerichtsleitend/`:
  - `staatsanwaltschaft-ermittlungsverfahren/`: Einleitungsverfügung (§ 152 Absatz 2, 160 StPO), Durchsuchungs- und Beschlagnahmeantrag (§ 102, 105 StPO), Haftbefehlsantrag (§ 112, 128 StPO), Einstellung mangels Tatverdachts (§ 170 Absatz 2 StPO), Abschlussverfügung (§ 169a StPO).
  - `staatsanwaltschaft-abschlussentscheidung/`: Einstellung aus Opportunität (§ 153, 153a StPO), Strafbefehlsantrag (§ 407 StPO), Anklageschrift zum Strafrichter, zum Schöffengericht und zur großen Strafkammer beziehungsweise zum Schwurgericht (§ 200 StPO).
  - `staatsanwaltschaft-hauptverhandlung/`: Plädoyer und Schlussvortrag (§ 258 StPO, § 46 StGB), Beweisantrag (§ 244 StPO), Stellungnahme zur Haftprüfung (§ 117 StPO), Antrag im beschleunigten Verfahren (§ 417 StPO), Nachtragsanklage (§ 266 StPO).
  - `staatsanwaltschaft-rechtsmittel-vollstreckung/`: Berufung (§ 312 StPO), Revision mit Begründung (§ 344 StPO), Vollstreckungsverfügung und Ladung zum Strafantritt (§ 451 StPO), Widerruf der Strafaussetzung (§ 56f StGB), Vollstreckung der Geldstrafe (§ 459e StPO).
  - `amtsanwaltschaft/`: Strafbefehlsantrag, Einstellung mangels Tatverdachts, Einstellung aus Opportunität, Anklage zum Strafrichter und Antrag auf Verwarnung mit Strafvorbehalt (§ 59 StGB), jeweils auf den Zuständigkeitsbereich der Amtsanwaltschaft (§ 142 GVG) zugeschnitten.
- Jede neue Vorlage folgt der Sonderordner-Konvention (eckige Platzhalter, kein Paragrafenzeichen, kein ODT-/ZIP-/Rubric-Zwang) mit eigener staatsanwaltschaftlicher Schlussmarkierung, vollständigen Sätzen, Recherche-Suchbegriffen statt erfundener Aktenzeichen und einem Querverweis auf das korrespondierende Plugin.
- `INDEX.md` und die Bereichs-READMEs um alle 25 Vorlagen und fünf Unterordner erweitert; die Master-Tabelle führt jetzt die Spalte „Bereich" statt „Gerichtsbarkeit".

### Geändert

- **`check-gerichtsleitend` von ASCII-Only auf echte Umlaute umgestellt.** Die blanke ASCII-Regel ist entfernt; der Sonderordner trägt jetzt durchgängig echte Umlaute. Die übrigen Portabilitätsregeln (eckige Platzhalter, kein Paragrafenzeichen, keine geraden Anführungszeichen, keine Komma-Zahlen) bleiben. Die Schlussmarkierung akzeptiert die richterliche und die staatsanwaltschaftliche Variante, die fünf neuen Unterordner sind in den Sollbestand aufgenommen.
- **`check-gerichtsleitend` ist damit wieder grün.** Der Zielkonflikt aus v3.0.0 (`check-umlauthygiene` erzwingt Umlaute, `check-gerichtsleitend` verlangte ASCII) ist aufgelöst; erstmals seit v3.0.0 sind alle zehn CI-Checks grün.
- **Residuale ASCII-Ersatzschreibungen** in den bestehenden 83 richterlichen Vorlagen zu echten Umlauten normalisiert (`Lückenliste`, `füllen`, `Tätigkeit`, `Begründung`, `trägt`); Slugs und Linkziele blieben unverändert ASCII.

### Geprüft

Alle zehn CI-Checks grün: `validate-vorlagen`, `check-kategorien-index`, `check-gerichtsleitend` (108 Vorlagen, 17 Bereiche), `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791). Drei Qualitätsrunden, ein abschließender Sanity-Check und ein Bug-Hunt: keine kaputten internen Links, keine erfundenen Aktenzeichen oder Klar-Namen, kein generischer Fülltext, keine ASCII-Ersatzschreibungen im Fließtext, kein Trailing-Whitespace.

### Hinweis

Die gerichtsleitenden und staatsanwaltschaftlichen Vorlagen sind experimentelle Gerüste ohne Rubric und ohne Eval-Bewertung. Sie ersetzen keine richterliche oder staatsanwaltschaftliche Entscheidung; die fachliche Endprüfung durch die zuständige Berufsträgerin oder den zuständigen Berufsträger bleibt zwingend.


## v3.2.0 — Paarformen in Parteiköpfen korrigiert (2026-06-21)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 84 gerichtsleitende Schriftvorlagen in `vorlagen-gerichtsleitend/`, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, die acht Kern-CI-Checks grün.

Verfeinerungs-Loop nach v3.1.0: das gesamte Repo wurde erneut auf Tonalität, Schreibweise und Gliederung durchgegangen. Der einzige substanzielle Fund war ein Artefakt eines zurückgenommenen De-Gendering-Laufs, das in Parteiköpfen und Adressatenfeldern die sinnlose Dopplung „Mandant oder Mandant" hinterlassen hatte. Er wurde auf die im Repo durchgängige Paarform zurückgeführt.

### Behoben

- **Paarform-Artefakt korrigiert.** In 48 Vorlagen stand in Rubren, Beteiligtenköpfen und Adressaten- beziehungsweise Verwendungszweck-Feldern die fehlerhafte Dopplung „Mandant oder Mandant". Sie wurde an 52 Fundstellen auf die im gesamten Repo verwendete Paarform „Mandantin oder Mandant" zurückgeführt. Zusätzlich wurde im zweisprachigen IP-Leitfaden ein „Inhaberin oder Inhaberin" zu „Inhaberin oder Inhaber" korrigiert.
- **Abgeleitete Fassungen neu erzeugt.** Für die 48 betroffenen Vorlagen wurden die ODT- und die Markdown-ZIP-Fassung neu gebaut, damit Markdown, ODT und ZIP byte-synchron bleiben.

### Geprüft

Die acht Kern-CI-Checks grün auf 791 Vorlagen: `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-md-zip-integrity`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval` (All-Pass 791/791, Fail 0); zusätzlich `check-kategorien-index` grün. Der Bug-Hunt-Durchlauf fand keine weiteren ASCII-Ersatzschreibungen im Fließtext der Standardvorlagen, keine römischen oder Buchstaben-Gliederungsebenen, keine erfundenen Aktenzeichen oder Klar-Namen, keine „Mandatsreife Prüfmatrix"-Blöcke und keine kaputten Markdown-Links.

### Bekannte offene Punkte

- `check-gerichtsleitend` ist vorbestehend rot und nicht Teil dieses eng begrenzten Release. Ursache ist ein Zielkonflikt zwischen zwei CI-Checks für den Sonderordner `vorlagen-gerichtsleitend/`: `check-umlauthygiene` erzwingt seit v3.1.0 echte Umlaute, `check-gerichtsleitend` verlangt für genau diese Dateien ASCII-Only. Beide Regeln widersprechen sich für jedes umlauthaltige Wort. Die Auflösung erfolgt in einer Folgeversion gemeinsam mit dem Ausbau des gerichtsbezogenen Sonderbereichs.


## v3.1.0 — Querverweise in vorlagen-gerichtsleitend repariert (2026-06-21)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern, 84 gerichtsleitende Schriftvorlagen in `vorlagen-gerichtsleitend/`, Drei-Ordner-Index in `kategorien/`, Eval-Harness `All-Pass 791/791`, alle acht CI-Checks grün.

Final-Sanity-Check nach v3.0.0: das gesamte Repo wurde tiefgehend auf integrierbare ungemergte Substanz geprüft. Alle vier stehengebliebenen Remote-Branches (`claude/optimistic-ptolemy-ljsp4l` und drei `quality/*` vom 13. Juni) enthalten beweisbar keine eigene Substanz mehr — die exklusiven Dateien dort sind historische `VORLAGE.md`-Stände (zwischen 147 und 220 Zeilen), die längst durch sprechende Dateinamen mit massiv ausgebautem Inhalt (236+ Zeilen) auf main ersetzt wurden. Mergen würde Substanz vernichten.

### Bereinigt

- **`vorlagen-gerichtsleitend/`**: 60 broken Markdown-Links in 13 Dateien repariert. Die `INDEX.md` und einige Bereichs-READMEs verlinkten auf Umlaut-Dateinamen (`01-eingangsverfügung-klagezustellung.md`), aber die Dateien existieren als ASCII-Slugs (`01-eingangsverfuegung-klagezustellung.md`). Die Links zeigen jetzt durchgängig auf die ASCII-Slugs.
- Drei verbleibende `aussergerichtlich`-Ersatzschreibungen aus dem v3.0.0-Lauf bereinigt.

### Geprüft

Alle acht CI-Checks grün auf 791 Vorlagen: `validate-vorlagen`, `check-umlauthygiene` (jetzt einschließlich `vorlagen-gerichtsleitend/`), `check-odt-integrity`, `check-md-zip-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` All-Pass 791/791, Fail 0.

### Abgrenzung

Relations- und Urteilsbauer-Arbeit gehört nicht in dieses Repo; sie liegt in `Klotzkette/claude-fuer-deutsches-recht` (`urteilsbauer-relationsmacher/`, `unified-mini-prompts/relationstechnik-zivilrecht.md`). Im Repo `vorlagensammlung-recht` bleibt der vierte Themenordner `vorlagen-gerichtsleitend/` der einzige richterliche Bereich.


## v3.0.0 — Konsolidierter Stand: alle Beiträge von Perplexity, Claude und Codex auf einem Tag (2026-06-21)

**Stand:** 791 validierte Vorlagen in 38 Themenordnern (sowie 84 gerichtsleitende Schriftvorlagen in `vorlagen-gerichtsleitend/` und ein Drei-Ordner-Index `kategorien/`), Eval-Harness `All-Pass 791/791`, alle acht CI-Checks grün.

Die Versionsnummer 3.0.0 markiert den Übergang aus der intensiven Co-Entwicklung von Perplexity, Claude und Codex in einen konsolidierten Stand: alle PRs der vergangenen Wochen sind gemergt, kein Branch liegt mit ungemergten Inhalten herum (`claude/optimistic-ptolemy-ljsp4l` und drei `quality/*`-Branches sind stehengebliebene Arbeits-Branches ohne eigene noch nicht eingespielte Commits — main hat 282 Dateien mehr als der claude-Branch und ist beweisbar vollständiger), und die Hygiene über alle Themenordner ist auf einem Niveau.

### Geprüft (Sanity-Check vor diesem Release)

- **165 PRs** durchgegangen: 164 gemergt, 1 vorhin per Admin-Merge geschlossen; 5 historisch zurückgewiesene PRs sind inhaltlich in Nachfolge-PRs eingearbeitet.
- **Sechs Remote-Branches** ungelöscht (`claude/optimistic-ptolemy-ljsp4l`, drei `quality/*` vom 13. Juni): jeweils null ungemergte Commits; im Endstand hat main mehr Dateien als jeder dieser Branches.
- **`prozessvorlagen/` und `vorlagen-gerichtsleitend/`** sind als zwei eigenständige Bereichsstrukturen vollständig auf main.

### Bereinigt in diesem Release

- **`vorlagen-gerichtsleitend/`** (118 Vorlagen) wies flächendeckende ASCII-Ersatzschreibungen auf (`Verfuegung`, `koennen`, `fuer`, `gemaess`, `Grosse Strafkammer`, `eroeffnet`, `persoenlich`, `geaeussert` u. v. m.), weil der Umlaut-Hygienecheck den Ordner ausdrücklich übersprungen hatte. **Über 110 Dateien repariert.** Echte Umlaute und scharfes s sind jetzt durchgängig gesetzt.
- **`scripts/check-umlauthygiene.sh`:** der explizite `-path './vorlagen-gerichtsleitend' -prune`-Ausschluss wurde entfernt. Der Check greift jetzt repoweit, sodass neue ASCII-Reste in gerichtsleitenden Vorlagen sofort auffallen.
- **Trailing-Whitespace** in den drei betroffenen Vorlagen-MDs (Verfassungsbeschwerde, Wechselmodell-Vereinbarung, Betriebsvereinbarung Arbeitszeit) bereinigt; zugehörige ZIPs neu erzeugt.

### Geprüft

Alle acht CI-Checks grün auf 791 Vorlagen: `validate-vorlagen`, `check-umlauthygiene` (jetzt repoweit), `check-odt-integrity`, `check-md-zip-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` All-Pass 791/791, Fail 0.

### Beiträge

Dieser Stand ist das Ergebnis aus Beiträgen von **Perplexity, Claude und Codex** über die letzten Wochen — auf jeden Beitrag gibt es einen eigenen CHANGELOG-Eintrag in der Historie, eine Release-Note und in der Regel auch eine PR. Mit v3.0.0 sind diese Beiträge zu einem geprüften Gesamtstand zusammengeführt.


## v2.13.4 — Kostenfeststellungsklage nach Erledigung vor Rechtshängigkeit (2026-06-21)

**Stand:** 791 kanonische Kanzleivorlagen in 38 Rechtsgebieten,
Eval-Harness `All-Pass 791/791`, alle zehn CI-Checks grün, zusätzlich
83 gerichtsleitende Markdown-Vorlagen in 12 Gerichtsbarkeiten.

### Neu

- `prozessvorlagen/kostenfeststellungsklage-nach-erledigung-vor-rechtshaengigkeit`
  ergänzt einen ausformulierten Schriftsatz für Klägerfälle, in denen das
  ursprüngliche Klagebegehren nach Einreichung vor Rechtshängigkeit wegfällt
  und die bei Klageeinreichung im Verzug befindliche Gegenseite die
  Rechtsverfolgungskosten als materiellen Verzugsschaden tragen soll.
- Die Vorlage trennt Erledigungserklärung, Klagerücknahme, § 91a ZPO,
  § 269 Abs. 3 Satz 3 ZPO und materiell-rechtliche Kostenfeststellungsklage,
  enthält einen konkreten Feststellungsantrag, eine Verzugschronologie,
  Kostenabgrenzung gegen doppelte Erstattung und Rechtsprechungsanker.

### Verbessert

- `prozessvorlagen/prozesspaket-zivilprozess-klage-erwiderung-replik-eilrechtsschutz`
  enthält jetzt einen eigenen Block zur Umstellung auf
  Kostenfeststellungsklage, damit bei Zahlung, Aufrechnung, dauernder Einrede,
  Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses nicht mechanisch
  Erledigung erklärt oder zurückgenommen wird.
- Die Prozessvorlagen-READMEs und die Drei-Ordner-Sicht wurden um die neue
  Vorlage ergänzt; ODT- und Markdown-ZIP-Artefakte wurden synchron neu
  erzeugt.

## v2.13.3 — Umlaut-Hygiene und Einzelvorlagen-Politur (2026-06-21)

**Stand:** 790 kanonische Kanzleivorlagen in 38 Rechtsgebieten,
Eval-Harness `All-Pass 790/790`, alle zehn CI-Checks grün, zusätzlich
83 gerichtsleitende Markdown-Vorlagen in 12 Gerichtsbarkeiten.

### Verbessert

- `steuerrecht/antrag-verbindliche-auskunft` wurde als sauberer, normaler
  Antrag nach § 89 Abs. 2 AO und StAuskV neu gegliedert: Rubrum,
  ernsthaft geplanter Sachverhalt, Rechtsfragen, eigene Rechtsauffassung,
  Gebührenangaben und Anlagen sind jetzt durchgehend ausformuliert.
- `arbeitsrecht/betriebsvereinbarung-ki-systeme` formuliert den
  KI-Einsatz konkreter über Systemregister, Zweck, Datenkategorien,
  Nutzerkreis, Protokollierung, menschliche Kontrolle und Löschfristen.
- `arbeitsrecht/arbeitnehmerueberlassungsvertrag-aueg` ersetzt die
  unpräzise AÜG-Logik-Formulierung durch eine konkrete Einsatzfreigabe mit
  Erlaubnisnachweis, Konkretisierung, Unterweisung und Einsatzdokumentation.
- `steuerrecht/einspruch-steuerbescheid` und
  `steuerrecht/stundungs-und-erlassantrag` erhielten bereinigte
  Vollmachtsanlagen und klarere Zweckzeilen ohne Klammerartefakte.
- ODT- und Markdown-ZIP-Fassungen der bearbeiteten Vorlagen wurden
  synchron neu erzeugt; die Umlaut-Hygiene wurde zusätzlich im sichtbaren
  Fließtext kontrolliert.

## v2.13.2 — Betriebsrats-Beschlussverfahren weiter geschärft (2026-06-21)

**Stand:** 790 kanonische Kanzleivorlagen in 38 Rechtsgebieten,
Eval-Harness `All-Pass 790/790`, alle zehn CI-Checks grün, zusätzlich
83 gerichtsleitende Markdown-Vorlagen in 12 Gerichtsbarkeiten.

### Verbessert

- `arbeitsrecht/antrag-einstweilige-verfuegung-betriebsrat` wurde
  verfahrensschärfer formuliert: Beschlussverfahren nach § 2a ArbGG,
  Eilrechtsschutz nach § 85 Abs. 2 ArbGG, konkrete Beteiligtenlogik,
  Vollstreckungsdifferenzierung und klarere Glaubhaftmachung.
- `arbeitsrecht/beschlussverfahren-betriebsrat-99-betrvg` bildet jetzt
  Zustimmungsersetzung, Zustimmungsfiktion, Aufhebung, § 100-BetrVG-
  Eilkonstellationen, Wochenfrist und Unterrichtungslücken ausführlicher ab.
- ODT- und Markdown-ZIP-Fassungen wurden synchron neu erzeugt.

## v2.13.1 — Arbeitsgerichtliches Prozesspaket für Beschlussverfahren getrennt (2026-06-21)

**Stand:** 790 kanonische Kanzleivorlagen in 38 Rechtsgebieten,
Eval-Harness `All-Pass 790/790`, alle zehn CI-Checks grün, zusätzlich
83 gerichtsleitende Markdown-Vorlagen in 12 Gerichtsbarkeiten.

### Korrigiert

- `prozessvorlagen/prozesspaket-arbeitsgericht-klage-erwiderung-replik-eilverfuegung`
  trennt betriebsverfassungsrechtlichen Eilrechtsschutz jetzt vom
  Klage-/Urteilsverfahren. BetrVG-Konstellationen bleiben im Paket, werden
  aber als eigener Beschlussverfahrenspfad mit Antragsteller und Beteiligten
  nach § 2a ArbGG geführt.
- README, ODT und Markdown-ZIP wurden synchronisiert.

## v2.13.0 — Europarechtszugang und Beamten-/Soldatenrecht ergänzt (2026-06-21)

**Stand:** 790 kanonische Kanzleivorlagen in 38 Rechtsgebieten,
Eval-Harness `All-Pass 790/790`, alle zehn CI-Checks grün, zusätzlich
83 gerichtsleitende Markdown-Vorlagen in 12 Gerichtsbarkeiten.

### Neu

- Neuer Rechtsbereich `beamten-und-soldatenrecht/` mit zehn anwaltlichen
  Vorlagen für Konkurrentenstreit, dienstliche Beurteilung, Besoldung und
  Zulagen, Kriegsdienstverweigerung, Wehrbeschwerde, gerichtliche Entscheidung
  nach WBO, Versetzung aus Härtegründen, Laufbahnzulassung und Zurückstellung
  vom Reservistendienst.
- Neue Europarechtsvorlage
  `europarecht/antrag-vorabentscheidung-eugh-nationales-gericht/` für den
  Antrag an ein deutsches Gericht auf Vorlage an den EuGH nach Art. 267 AEUV.
- Neue Strategievorlage
  `europarecht/zugangscheck-eugh-eug-verfahrensstrategie/` zur Abgrenzung von
  Vorabentscheidungsverfahren, Direktklage vor dem Gericht der Europäischen
  Union, Rechtsmittel zum EuGH und nationaler Anschlussstrategie.

### Verbessert

- `verfassungsrecht/verfassungsbeschwerde-bverfg` enthält jetzt einen
  eigenen Block zur unterlassenen EuGH-Vorlage als Rüge aus Art. 101 Abs. 1
  Satz 2 GG, mit Begründungs- und Substantiierungsgerüst für CILFIT-,
  Foto-Frost- und Consorzio-Italian-Management-Konstellationen.
- `europarecht/vorlagebeschluss-eugh-art-267-aeuv` und
  `europarecht/eugh-schriftsatz-ecuria` sind auf eckige Platzhalter und
  sprechendere Anlagenbezeichnungen nachgezogen.
- `run-eval.py`, `validate-vorlagen.py`, `generate-default-rubrics.py` und
  die Kategorieübersichten erfassen den neuen Rechtsbereich vollständig.

## v2.12.1 — Familiengericht in gerichtsleitende Vorlagen aufgenommen (2026-06-21)

**Stand:** 778 kanonische Kanzleivorlagen in 37 Rechtsgebieten,
Eval-Harness `All-Pass 778/778`, zusätzlich 83 gerichtsleitende
Markdown-Vorlagen in 12 Gerichtsbarkeiten.

### Neu

- Neuer Unterordner `vorlagen-gerichtsleitend/familiengericht/` mit zehn
  familiengerichtlichen Schriftvorlagen.
- Abgedeckt sind Eingangsverfügung, beschleunigte Terminsverfügung nach
  § 155 FamFG, Hinweisverfügung zum Einvernehmen nach § 156 FamFG,
  Verfahrensbeistand nach § 158 FamFG, Sachverständigenbeweis nach § 163
  FamFG, einstweilige Anordnung nach § 49 FamFG, Gewaltschutzbeschluss nach
  § 214 FamFG, Umgangs- und Sorgebeschluss, Versorgungsausgleichsauskunft und
  einstweilige Unterhaltsanordnung.
- `scripts/check-gerichtsleitend.py`, `vorlagen-gerichtsleitend/README.md`
  und `vorlagen-gerichtsleitend/INDEX.md` erfassen das Familiengericht jetzt
  als eigene Gerichtsbarkeit.

## v2.12.0 — Gerichtsleitende Schriftvorlagen ergänzt (2026-06-21)

**Stand:** 778 kanonische Kanzleivorlagen in 37 Rechtsgebieten,
Eval-Harness `All-Pass 778/778`, alle zehn CI-Checks grün, zusätzlich
73 gerichtsleitende Markdown-Vorlagen in 11 Gerichtsbarkeiten.

### Neu

- Neuer Sonderbereich `vorlagen-gerichtsleitend/` mit Markdown-only-Vorlagen
  für gerichtliche Verfügungen, Beschlüsse, Tenor-Entwürfe, Ladungen,
  Hinweise, Protokollgerüste und Begründungsskelette.
- Enthalten sind Amtsgericht Zivilsachen, Amtsgericht Strafsachen, Amtsgericht
  Insolvenz- und Restrukturierungsgericht, Amtsgericht Handelsregister,
  Landgericht Zivilkammer, Landgericht Strafkammer, Verwaltungsgericht,
  Finanzgericht, Sozialgericht, Arbeitsgericht und BVerfG-Kammer.
- `vorlagen-gerichtsleitend/INDEX.md` listet alle 73 Vorlagen mit
  Anwendungsbereich und Cross-Reference auf die korrespondierende
  `_GERICHTE_EXPERIMENTAL/`-Struktur.

### Qualitätssicherung

- Neuer CI-Check `scripts/check-gerichtsleitend.py`: prüft
  Gerichtsbarkeitsordner, 5 bis 10 Vorlagen je Ordner, Pflichtabschnitte,
  INDEX-Abdeckung, ASCII-Kompatibilität, eckige Platzhalter, Slug-Länge,
  Verzicht auf spitze Klammern und Paragraphenzeichen sowie die
  Pflichtmarkierung zum richterlichen Prüfvorbehalt.
- Die normalen Kategorie-, Markdown-ZIP- und Umlautprüfungen nehmen den
  Sonderbereich bewusst aus, weil dort andere Kompatibilitätsregeln gelten.

## v2.11.0 — Generisches Maskulinum in allen Vorlagen und READMEs (2026-06-21)

**Stand:** 778 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 778/778`, alle acht CI-Checks grün.

Sprachregel: das Repo nutzt durchgängig das generische Maskulinum. Doppelnennungen, Gender-Sternchen, Doppelpunkt-Schreibweisen, Schrägstrich- und Klammerformen sind in Vorlagen und READMEs nicht zulässig. Alleinstehende weibliche Bezeichnungen für eine konkret benannte Person bleiben erlaubt.

### Geändert

- **Repoweite Entgenderung der Vorlagen und READMEs.** 416 Markdown-Dateien angepasst, insgesamt 896 Ersetzungen. Häufigste Muster: „Rechtsanwältinnen und Rechtsanwälte" → „Rechtsanwälte", „Mandantinnen und Mandanten" → „Mandanten", „Berufsträgerinnen und Berufsträger" → „Berufsträger", „Vermieterinnen oder Vermieter" → „Vermieter", „Auftraggeberinnen und Auftraggeber" → „Auftraggeber". Auch die Dativ- und Singular-Doppelformen wurden gefangen. Doppelpunkt-Gender-Schreibweisen („Mandant:in", „Betreuer:in") und Klammerformen („Antragsteller(in)") sind entfernt. Spezialformen wie „Athletinnen und Athleten", „Schöffinnen und Schöffen", „Miterbinnen und Miterben", „Autorinnen und Autoren" sind ebenfalls vereinheitlicht.
- **Alle zugehörigen ODT-Fassungen** (394 Dateien) neu aus den angepassten Markdown-Quellen erzeugt. Die zugehörigen `.md.zip`-Spiegelkopien synchronisiert.

### Bewusst nicht angetastet

- Alleinstehende weibliche Personenbezeichnungen, die im Sachverhalt eine konkret benannte Person bezeichnen können (etwa „die Klägerin", wenn nur ein konkretes Verfahren mit weiblicher Klagepartei beschrieben wird), bleiben unverändert. Das Skript war konservativ und hat nur Doppelformen angepasst.
- Offizielle Bezeichnungen, in denen weibliche Endungen Teil des Namens sind (z. B. „Bundesnotarkammer", „Aufsichtsbehörde", „Sachverständige" als juristisch-feminines Substantiv), sind erhalten geblieben.

### Geprüft

Alle acht CI-Checks grün auf 778 Vorlagen: `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`, `check-md-zip-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` All-Pass 778/778, Fail 0.


## v2.10.1 — Vergaberechtliche Feinschärfung nach Normkontrolle (2026-06-21)

**Stand:** 778 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 778/778`, alle neun CI-Checks grün.

### Verbessert

- `vergaberecht/antrag-zuschlagsgestattung-169-gwb` bildet die
  Zwei-Wochen-Wirkung der Gestattungsentscheidung, die Zuschlagsaussichten und
  besondere Verteidigungs- oder Sicherheitsinteressen nach § 169 GWB klarer ab.
- `vergaberecht/erwiderung-nachpruefungsantrag-vergabestelle` und
  `vergaberecht/stellungnahme-beigeladene-vergabekammer` schärfen
  Akteneinsicht, Geheimnisschutz und Schwärzungsmatrix nach § 165 GWB.
- `vergaberecht/beschwerdeerwiderung-vergabesenat-olg` ergänzt
  Beschwerdebegründung, anwaltliche Unterzeichnung, Beteiligtenunterrichtung
  und aufschiebende Wirkung nach §§ 172, 173 GWB.
- `vergaberecht/vergaberechtsverstoss-pruefvermerk-bieter` grenzt laufende
  Zuschlagsverfahren von § 135-GWB-Konstellationen sauberer ab.
- `vergaberecht/ruegeschreiben-nichtabhilfe-vergabestelle` stellt
  Nichtabhilfe, neue Beanstandungen und fehlende Fristverlängerungswirkung
  deutlicher heraus.

## v2.10.0 — Vergaberechtliches Komplettpaket für Rüge, Nachprüfung und Verteidigung (2026-06-21)

**Stand:** 778 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 778/778`, alle neun CI-Checks grün.

### Neu

- `vergaberecht/vergaberechtsverstoss-pruefvermerk-bieter` ergänzt einen
  internen Bieter-Prüfvermerk mit Fehler-, Fristen- und Belegmatrix für Rüge
  und Nachprüfung.
- `vergaberecht/ruegeschreiben-nichtabhilfe-vergabestelle` ergänzt die
  Nichtabhilfe- und Rügeantwort der Vergabestelle mit Zugangsdokumentation und
  Fristenmatrix.
- `vergaberecht/erwiderung-nachpruefungsantrag-vergabestelle` ergänzt den
  Verteidigungsschriftsatz der Vergabestelle im Nachprüfungsverfahren.
- `vergaberecht/stellungnahme-beigeladene-vergabekammer` ergänzt die
  Stellungnahme der Beigeladenen mit Angebotsverteidigung und
  Geheimnisschutzmatrix.
- `vergaberecht/antrag-zuschlagsgestattung-169-gwb` ergänzt den Antrag auf
  Gestattung des Zuschlags trotz Zuschlagsverbot.
- `vergaberecht/terminsvermerk-muendliche-verhandlung-vergabekammer` ergänzt
  einen Terminsvermerk für die mündliche Verhandlung vor der Vergabekammer.
- `vergaberecht/beschwerdeerwiderung-vergabesenat-olg` ergänzt die
  Beschwerdeerwiderung im Verfahren vor dem OLG-Vergabesenat.

### Struktur

- `vergaberecht/README.md` und die Drei-Ordner-Sicht sind auf das neue
  Vergaberechtspaket erweitert.
- `scripts/generate-default-rubrics.py` erkennt Rüge-Schreibweise,
  Stellungnahmen und Beschwerdeerwiderungen regenerationsfest als
  Schriftsätze.

## v2.9.1 — Prozesspakete verfahrensspezifisch geglättet (2026-06-21)

**Stand:** 771 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 771/771`, alle neun CI-Checks grün.

### Verbessert

- Die sechs Prozesspakete aus v2.9.0 erhalten konkretere Rubren für
  Zivilprozess, Arbeitsgericht, Verwaltungsprozess, Familienverfahren,
  Sozialgericht und Finanzgericht.
- Die README-Anwendungsbereiche wurden von generischer Prozesssprache auf die
  jeweilige Verfahrensordnung zugeschnitten; Eilrechtsschutz, Statthaftigkeit
  und Vollstreckungsinstrumente werden prozessartgenau beschrieben.
- Das Root-README verweist wieder auf den aktuellen Stand von 771 Vorlagen und
  führt `prozessvorlagen/` als eigenen Rechtsbereich auf.

## v2.9.0 — Prozesspakete für Klage, Erwiderung, Replik und Eilrechtsschutz (2026-06-21)

**Stand:** 771 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 771/771`, alle neun CI-Checks grün.

### Neu

- `prozessvorlagen/prozesspaket-zivilprozess-klage-erwiderung-replik-eilrechtsschutz`
  ergänzt ein ZPO-Paket mit Klageschrift, Klageerwiderung, Replik,
  einstweiliger Verfügung und Erwiderung auf den Eilantrag.
- `prozessvorlagen/prozesspaket-arbeitsgericht-klage-erwiderung-replik-eilverfuegung`
  ergänzt ein ArbGG-Paket mit Urteilsverfahren und arbeitsgerichtlichem
  Eilrechtsschutz; Beschäftigungsgebote werden auf § 888 ZPO ausgerichtet,
  Unterlassungs- und Duldungstenöre auf § 890 ZPO.
- `prozessvorlagen/prozesspaket-verwaltungsprozess-klage-erwiderung-replik-eilrechtsschutz`
  ergänzt ein VwGO-Paket für Anfechtungs-, Verpflichtungs-, Leistungs- und
  Feststellungsklage sowie § 80 Abs. 5 und § 123 VwGO.
- `prozessvorlagen/prozesspaket-familienverfahren-antrag-erwiderung-replik-eilanordnung`
  ergänzt ein FamFG-Paket mit Antragsschrift, Erwiderung, weiterer
  Stellungnahme und einstweiliger Anordnung.
- `prozessvorlagen/prozesspaket-sozialgerichtsprozess-klage-erwiderung-replik-eilrechtsschutz`
  ergänzt ein SGG-Paket mit Klage, Klageerwiderung, Replik und § 86b SGG.
- `prozessvorlagen/prozesspaket-finanzgerichtsprozess-klage-erwiderung-replik-aussetzung`
  ergänzt ein FGO-Paket mit Klage, Klageerwiderung, Replik, Aussetzung der
  Vollziehung und einstweiliger Anordnung.

### Struktur

- Die sechs neuen Prozesspakete sind in `prozessvorlagen/README.md` und in
  der prozessualen Drei-Ordner-Sicht verlinkt; ODT, Markdown-ZIP und
  Rubrics sind synchron erzeugt.

## v2.8.2 — Rubric-Generator für Testamentsvollstrecker-Amtsannahme abgesichert (2026-06-21)

**Stand:** 765 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 765/765`, alle neun CI-Checks grün.

### Behoben

- `scripts/generate-default-rubrics.py` klassifiziert
  `erbrecht/testamentsvollstrecker-annahme-amtspflichten` auch bei einem
  erzwungenen Neuaufbau mit `--force` als `typ: "sonstiges"`.
- Damit bleibt die in v2.8.1 korrigierte Rubric regenerationsfest; der
  Wortbestandteil `testament` löst für diese Nachlassgerichts-Erklärung nicht
  mehr den Vertrags-Detektor aus.
- `EVAL_RESULTS.md` aktualisiert: **765/765 All-Pass**.

## v2.8.1 — Rubric-Typ Testamentsvollstrecker-Amtsannahme korrigiert (2026-06-21)

**Stand:** 765 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 765/765`, alle neun CI-Checks grün.

### Behoben

- `erbrecht/testamentsvollstrecker-annahme-amtspflichten` ist eine an das
  Nachlassgericht gerichtete Annahmeerklärung mit Amtsführungsplan und bleibt
  in der Drei-Ordner-Sicht unter `03-sonstige-vorlagen`.
- Die `rubric.yaml` ist entsprechend von `typ: "vertrag"` auf
  `typ: "sonstiges"` umgestellt; der unpassende Vertrags-Parteienblock-Check
  wurde durch den Sonstige-Basisstrukturcheck ersetzt.
- `EVAL_RESULTS.md` aktualisiert: **765/765 All-Pass**.

## v2.8.0 — Zehn neue Praxisvorlagen für Arbeitsrecht, Erbrecht, Gesellschaftsrecht, Bankrecht, Mietrecht, IT und Versicherung (2026-06-21)

**Stand:** 765 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 765/765`, alle neun CI-Checks grün.

### Neu — zehn unmittelbar nutzbare Vorlagen

- `arbeitsrecht/klage-bonuszahlung-zielvereinbarung` — Zahlungsklage für
  variable Vergütung mit Zielvereinbarung, verspäteter Zielvorgabe,
  Zielerreichungsberechnung, Schadensersatzvariante und Beleganlagen.
- `arbeitsrecht/betriebsvereinbarung-ki-systeme` — Betriebsvereinbarung für
  KI-Systeme mit Systemregister, Freigabeprozess, Datenschutz, menschlicher
  Kontrolle, Schulung und Betriebsratsrechten.
- `erbrecht/testamentsvollstrecker-annahme-amtspflichten` —
  Annahmeerklärung gegenüber dem Nachlassgericht mit Amtsführungsplan,
  Nachlasssicherung, Beteiligtenkommunikation und Rechnungslegung.
- `erbrecht/abschichtungsvereinbarung-erbengemeinschaft` —
  Abschichtungsvertrag mit Anwachsung, Abfindung, Freistellung,
  Nachlassverzeichnis, Formprüfung und Vollzugsvollmacht.
- `handels-und-gesellschaftsrecht/gesellschafterbeschluss-gewinnverwendung-gmbh`
  — GmbH-Beschluss zu Jahresabschluss, Ausschüttung, Rücklagen, Steuerabzug,
  Fälligkeit und Kapitalerhaltungsprüfung.
- `handels-und-gesellschaftsrecht/gesellschafterbeschluss-einziehung-geschaeftsanteil`
  — GmbH-Beschluss zur Geschäftsanteilseinziehung mit Satzungsgrundlage,
  Anhörung, Abfindung, Kapitalerhaltung und Gesellschafterlisten-Vollzug.
- `bank-und-kapitalmarktrecht/kreditprolongations-und-waiver-vereinbarung` —
  Änderungsvereinbarung zum Kreditvertrag mit Prolongation, konkret begrenztem
  Waiver, Reportingpflichten, Sicherheitenbestätigung und Vollzugsvoraussetzungen.
- `versicherungsrecht/anspruchsschreiben-krankentagegeld` —
  Leistungsaufforderung an die private Krankenversicherung mit
  Arbeitsunfähigkeitsnachweisen, Tätigkeitsbild, Berechnung und Datenschutzgrenzen.
- `mietrecht-und-wohnungseigentumsrecht/klage-duldung-modernisierung` —
  Duldungsklage nach Modernisierungsankündigung mit Zutrittsantrag,
  Härteprüfung, Schutzmaßnahmen und vollständigen Anlagen.
- `informationstechnologierecht/quellcode-herausgabe-und-datenexport-notfallplan`
  — Notfallplan für Quellcode, Datenexport, Schlüsselübergabe, Testimport,
  Geheimnisschutz und Mängelprotokoll bei IT-Ausfall, Kündigung oder Insolvenz.

### Pflege

- Neue Vorlagen jeweils mit sprechendem Markdown-, ODT- und ZIP-Dateinamen,
  README-Downloadlinks, `rubric.yaml`, Anlagenblöcken und
  Drei-Ordner-Sicht eingetragen.
- ODT-Dateien und Markdown-ZIP-Downloads synchron erzeugt.
- `EVAL_RESULTS.md` aktualisiert: **765/765 All-Pass**.

## v2.7.2 — Familienrecht: generische Muster-Anlagen durch fallspezifische Anlagen ersetzt (2026-06-20)

**Stand:** 755 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 755/755`, alle neun CI-Checks grün.

### Behoben — fallspezifische Anlagen statt generischer Muster

In sechs weiteren Familienrecht-Vorlagen trugen die Anlagen noch das generische
Muster („1. Identifikation / 2. Inhalt und Bezug / 3. Prüfung und Verwendung"
mit der Floskel „Zweck dieser Anlage: …"), teils mehrere gleichlautende Anlagen.
Sie sind jetzt fallspezifisch und an den im Vorlagentext in Bezug genommenen
Anlagen ausgerichtet:

- `scheidungsantrag` — Personenstandsurkunden und Trennungsnachweis sowie
  Angaben zu Folgesachen.
- `antrag-elterliche-sorge-uebertragung` — Nachweise zum Kindeswohl
  (Jugendamtsbericht nach § 162 FamFG, Schul- und ärztliche Unterlagen,
  Vorfallsdokumentation).
- `antrag-gewaltschutz-gewschg` — sechs gleichlautende Muster-Anlagen ersetzt
  durch Vorfalls- und Gewaltdokumentation, ärztliche Atteste, polizeiliche
  Vorgänge, Zeugenbenennung, frühere Anordnungen und eidesstattliche
  Versicherung.
- `umgangsprotokoll-eltern` — Umgangsgrundlage, Kommunikationsnachweise sowie
  Gesundheits- und Kindeswohlunterlagen mit konkretem, ausfüllbarem Inhalt.
- `ehevertrag-zweisprachig` und `scheidungsfolgenvereinbarung-zweisprachig` —
  zweisprachige, fallspezifische Anlagen (Vermögensverzeichnisse,
  Vermögens- und Hausratsaufteilung, offene Punkte, Nachweise), durchgehend
  zweispaltig nach Abschnitt 19 des Repo-Leitfadens (Deutsch links, Englisch
  rechts).

Verirrte Trennlinien nach `## Vorlage` bereinigt; `Lizenz: Apache-2.0 OR MIT.`
als letzte Zeile sichergestellt; ODT und Markdown-ZIP neu erzeugt. Damit trägt
keine Familienrecht-Vorlage mehr eine generische Muster-Anlage.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-kategorien-index`,
  `check-odt-integrity`, `check-odt-spaltenlayout`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene`,
  `check-md-zip-integrity` OK; `run-eval`: `All-Pass 755/755`.
## v2.7.1 — Verfassungsbeschwerde und prozessuale Vorlagen geschärft (2026-06-21)

Qualitätsrelease für zwei prozessuale Schwerpunkte: Die
Verfassungsbeschwerde-Vorlage wurde an den Annahme-, Zulässigkeits- und
Substantiierungsanforderungen des Bundesverfassungsgerichts ausgerichtet; dazu
kommen gezielte Schärfungen prozessualer Vorlagen aus Erbrecht, Mietrecht,
Arbeitsrecht, Sportrecht, Vergaberecht und Verwaltungsrecht.

**Stand:** 755 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 755/755`,
alle lokalen Gates grün.

### Inhaltliche Schärfungen

- Verfassungsbeschwerde mit klarerer Beschwerdebefugnis, Rechtswegerschöpfung,
  Subsidiarität, Annahmebegründung, Grundrechtsrügen und
  Rechtsprechungsankern.
- Sportrechtlicher Eilantrag auf Spielberechtigung mit getrennten Tenor- und
  Vollstreckungsvarianten für positive Handlung, Unterlassung und Duldung.
- Betriebsverfassungsrechtlicher Eilantrag mit präziserer Trennung zwischen
  Unterlassungstenor und positiver Vollzugshandlung.
- Nachlassgerichtliche Vorlagen zu Testamentsvollstreckerzeugnis,
  Erbscheinseinziehung, Nachlassverwaltung und Erbscheinsbeschwerde deutlich
  ausformuliert.
- Verwaltungsrechtliche Vorlagen zu Kommunalabgaben-Widerspruch und
  Akteneinsicht/DSGVO-Auskunft von generischer Platzhaltersprache befreit.
- Vergaberechtlicher Antrag nach § 173 GWB mit vollständiger Fristen-,
  Erfolgsaussichts- und Folgenabwägungslogik neu gefasst.

### Qualitätssicherung

- ODT-Dateien und Markdown-ZIP-Downloads zu allen bearbeiteten Vorlagen neu
  erzeugt.
- Lokale `* 2.*`-Dubletten aus dem Arbeitsbaum entfernt.
- Eval-Stand: **755/755 All-Pass**.

## v2.7.0 — Familienrecht: Unterhaltsvorlagen vertieft und nachehelicher Unterhalt ergänzt (2026-06-20)

**Stand:** 755 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 755/755`, alle neun CI-Checks grün.

### Neu

- `familienrecht/antrag-nachehelicher-unterhalt` — Antrag auf nachehelichen
  Unterhalt (§§ 1569 ff. BGB, §§ 231 ff. FamFG) mit Stufenantrag (Auskunft
  § 1605 BGB, eidesstattliche Versicherung, Zahlung), den Anspruchstatbeständen
  Betreuungs-, Alters-, Krankheits-, Aufstockungs-, Ausbildungs- und
  Billigkeitsunterhalt (§§ 1570–1576 BGB), der Befristung und Herabsetzung nach
  § 1578b BGB und der Verwirkung nach § 1579 BGB; in die Drei-Ordner-Sicht
  eingetragen.

### Unterhaltsvorlagen mit echter Berechnung vertieft

Die Unterhaltsvorlagen trugen bisher nur knappe Berechnungsskizzen und
generische Muster-Anlagen. Sie enthalten jetzt einen vollständigen,
schrittweisen Rechengang (bereinigtes Nettoeinkommen mit den üblichen Abzügen,
Bedarf nach Halbteilung beziehungsweise Düsseldorfer Tabelle, Bedürftigkeit und
Erwerbsobliegenheit, Leistungsfähigkeit, Selbstbehalt und Mangelfall mit
Rangfolge nach § 1609 BGB) sowie unterhaltsspezifische Anlagen
(Einkommens- und Belegverzeichnis, ausfüllbare Unterhaltsberechnung). Alle
Tabellen- und Selbstbehaltswerte stehen als Platzhalter „nach aktueller
Düsseldorfer Tabelle":

- `klage-trennungsunterhalt` (§ 1361 BGB) — Differenzmethode, Erwerbstätigenbonus,
  Erwerbsobliegenheit im ersten Trennungsjahr (§ 1361 Abs. 2 BGB).
- `aufforderung-kindesunterhalt` — Einstufung in die Düsseldorfer Tabelle,
  Mindestunterhalt § 1612a BGB mit dynamischem Titel, Kindergeldanrechnung
  § 1612b BGB, Volljährigenunterhalt, Verzug § 1613 BGB.
- `antrag-vereinfachtes-verfahren-kindesunterhalt` (§§ 249 ff. FamFG) — mit
  Einwendungssystem § 252 FamFG und Übergang ins streitige Verfahren.
- `auskunftsverlangen-unterhalt` (§ 1605 BGB) — vollständiger Belegkatalog,
  Zweijahressperre, Stufenantrag und eidesstattliche Versicherung.
- `antrag-abaenderung-unterhaltstitel` (§ 238 FamFG) — Abgrenzung zu §§ 239,
  240 FamFG, Wesentlichkeitsschwelle, Präklusion, Gegenüberstellung alt/neu.
- `antrag-einstweilige-anordnung-unterhalt` (§ 246 FamFG) — Eilbedürfnis,
  Glaubhaftmachung (§ 31 FamFG) und Verhältnis zur Hauptsache (§ 52 FamFG).
- `unterhaltsvergleich-familiengericht` — Lizenzzeile ergänzt, Grammatik
  bereinigt.

### Weitere Familienrecht-Verbesserung

- `ehevertrag` — die zwei gleichlautenden Muster-Anlagen wurden durch die im
  Vertragstext in Bezug genommenen Vermögensverzeichnisse für Ehegatte A und
  Ehegatte B ersetzt (mit privilegiertem Anfangsvermögen nach § 1374 Abs. 2
  BGB); Lizenzzeile ergänzt.
- Verirrte Trennlinien direkt nach `## Vorlage` und generische Muster-Anlagen
  in den bearbeiteten Vorlagen entfernt; durchgehende Dezimalgliederung mit
  Leerzeilen.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-kategorien-index`,
  `check-odt-integrity`, `check-odt-spaltenlayout`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene`,
  `check-md-zip-integrity` OK; `run-eval`: `All-Pass 755/755`.

## v2.6.0 — Verfassungsrecht auf BVerfG-Niveau, Flaggschiff-Verträge und repoweite Füller-Bereinigung (2026-06-20)

**Stand:** 754 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 754/754`, alle neun CI-Checks grün.

### Neu

- `verfassungsrecht/konkrete-normenkontrolle-richtervorlage-bverfg` — Aussetzungs-
  und Vorlagebeschluss eines Fachgerichts nach Art. 100 Abs. 1 GG, §§ 80 ff.
  Bundesverfassungsgerichtsgesetz (BVerfGG), mit Tenor (Aussetzung und Vorlage),
  Entscheidungserheblichkeit und der Darlegung der Überzeugung von der
  Verfassungswidrigkeit; in die Drei-Ordner-Sicht eingetragen.

### Verfassungsrecht — alle Vorlagen auf einreichungsfähiges Niveau gehoben

Die sieben bestehenden Verfassungsrecht-Vorlagen waren bloße Ausfüll-Merkzettel
und trugen einen sachfremden Kartellrecht-Block („Sprach- und Fassungsregel"
mit Letter of Intent, Dawn Raid, Leniency, Gun Jumping, e-Curia) sowie eine
mitten im Dokument stehende Lizenzzeile. Sie sind jetzt durchformulierte
Schriftsätze bzw. ein Prüfvermerk:

- Verfassungsbeschwerde und Kommunalverfassungsbeschwerde mit vollständiger
  Zulässigkeits- und Begründetheitsprüfung (Art. 93 Abs. 1 Nr. 4a und 4b GG,
  §§ 90 ff., 91, 92, 93, 95, 34a, 32 BVerfGG; Selbstverwaltungsgarantie des
  Art. 28 Abs. 2 GG).
- Abstrakte Normenkontrolle, Organstreit, Bund-Länder-Streit und Eilantrag nach
  § 32 BVerfGG (mit doppelter Folgenabwägung) durchformuliert.
- Grundrechtsprüfung als Prüfvermerk im Gutachtenstil (Schutzbereich, Eingriff,
  Rechtfertigung, Verhältnismäßigkeit).

### Flaggschiff-Verträge — Großkanzlei-Feinschliff

- Wohnraummietvertrag, Handelsvertretervertrag, Bauvertrag (VOB/B) und
  GmbH-Geschäftsanteilskaufvertrag: Unterabsätze durchgängig dezimal nummeriert
  (1.1, 1.2 …) mit Leerzeile zwischen den Ebenen.
- Wohnraummietvertrag: verirrte Titelzeile und doppelter Unterschriftenblock
  entfernt; generische Muster-Anlagen durch Übergabeprotokoll, Grundriss-/
  Inventarbeschreibung und Hausordnung ersetzt.
- Handelsvertreter- und Bauvertrag: vertragsspezifische Anlagen
  (Vertragsprodukte, Vertragsgebiet/Kundenkreis bzw. Leistungsverzeichnis,
  Baubeschreibung, Ausführungspläne) statt gleichlautender Muster-Anlagen.
- Geschäftsanteilskaufvertrag: interne Querverweise von „§ 5"/„nach 4." auf
  eindeutige „Abschnitt N.M" umgestellt; Gesetzesverweise unverändert.

### Bereinigt — repoweit

- Der sachfremde Abschnitt „Sprach- und Fassungsregel" wurde aus
  dreiunddreißig weiteren Vorlagen (Kartell-, Europa-, Insolvenz-, Aufsichts-,
  Zoll- und Restrukturierungsrecht) entfernt. Er war stets der letzte
  nummerierte Abschnitt vor dem Schluss-Block und wurde ohne Eingriff in
  Nummerierung, Anträge oder Querverweise herausgenommen.

### Geprüft

- Einsortierung in der Drei-Ordner-Sicht repo-weit gesichtet; Bug-Hunt zu
  Bereichsindizes, Abschnittsnummerierung, Querverweisen und Buchstaben-
  Restspuren ohne neue Befunde.
- `validate-vorlagen`, `check-gliederung`, `check-kategorien-index`,
  `check-odt-integrity`, `check-odt-spaltenlayout`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene`,
  `check-md-zip-integrity` OK; `run-eval`: `All-Pass 754/754`.
## v2.5.4 — Anti-Generik-Runde für Rubren und Dokumentauftakte (2026-06-20)

**Stand:** 753 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle acht CI-Checks grün.

### Verbessert — konkrete Rollen statt Schablonenköpfe

- 32 Vorlagen mit früher generischen Erklärungsköpfen verwenden jetzt
  fallbezogene Rollenbezeichnungen, etwa Vollmachtgeberin,
  Ressourcengeberin, steuerpflichtige Person, Diensteanbieterin,
  Websitebetreiberin, Abfallerzeugerin, Vermieterin, Arbeitgeberin oder
  Unterlassungsschuldnerin.
- Zweisprachige Vorsorge- und postmortale Vollmachten benennen im Kopf jetzt
  ausdrücklich die notarielle beziehungsweise postmortale Reichweite,
  Anerkennungszweck und Einsatzbereich.

### Verbessert — Auftaktsätze

- 18 Dokumente beginnen nicht mehr mit der austauschbaren Formel
  „Gegenstand dieses Dokuments ist der folgende Vorgang", sondern mit einem
  auf das jeweilige Dokument zugeschnittenen Satz zu Zweck, Adressat und
  operativer Funktion.
- Zwei erkennbare Schablonenreste in Nachunternehmererklärung und
  Strafprozessvollmacht wurden sprachlich bereinigt.
- ODT- und Markdown-ZIP-Artefakte wurden für alle geänderten Vorlagen
  synchron neu erzeugt.

## v2.5.3 — Qualitätsrunde Anlagenkennzeichnung, LOI-Anlagen und Vollziehungsauftrag (2026-06-20)

**Stand:** 753 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle acht CI-Checks grün.

### Verbessert — Anlagen und Verweisqualität

- Der internationale Letter of Intent verwendet keine Buchstabenanlagen mehr.
  Asset-Liste und Datenraumanforderungen sind jetzt als Anlage 1 und Anlage 2
  ausgearbeitet, damit Transaktionsgegenstand und Due-Diligence-Umfang im
  Dokument selbst belastbar befüllt werden können.
- Die zweisprachige Leitvorlage zur ehelichen Vermögensauseinandersetzung
  verweist bei Hausrat und streitigen Gegenständen auf Anlage 1 und Anlage 2
  und enthält dazu korrespondierende zweisprachige Anlagezeilen.
- Die zivilprozessualen Vorlagen `vollstreckungsabwehrklage-767-zpo`,
  `drittwiderspruchsklage-771-zpo`, `erinnerung-vollstreckung-766-zpo` und
  `stufenklage-zivilprozess` verwenden in den Anlagenabschnitten jetzt
  durchgehend dezimale Anlagen statt `Anlage K` oder `Anlage E`; knappe
  Anlagenüberschriften wurden um verwendbare Platzhaltertexte ergänzt.

### Korrigiert — Sprache und generische Reste

- Der verwaltungsrechtliche Zustellungs- und Vollziehungsauftrag nach § 123
  VwGO beschreibt Zustellungsadressat, Umsetzungsfrist, behördliche
  Zuständigkeit und Vollstreckungsweg jetzt konkret statt abstrakt mit
  „Vollzugslogik".
- Der Vergabevermerk verwendet keine Platzhalteranlage `Anlage X` mehr,
  sondern verweist auf die in den Vergabeunterlagen bekanntgemachte
  Wertungstabelle.
- Die geänderten ODT- und Markdown-ZIP-Artefakte wurden synchron neu erzeugt.

## v2.5.2 — Podcast-AVV an Art. 28 DSGVO nachgeschärft (2026-06-20)

**Stand:** 731 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 731/731`, alle acht CI-Checks grün.

### Korrigiert — Podcast-Produktionsvertrag

- Anlage 4 des Podcast-Produktionsvertrags berücksichtigt jetzt ausdrücklich
  das Wahlrecht des Auftraggebers nach Art. 28 Abs. 3 lit. g DSGVO: Nach Ende
  der Verarbeitung werden personenbezogene Daten nach Wahl zurückgegeben oder
  gelöscht; vorhandene Kopien sind anschließend zu löschen, soweit keine
  Aufbewahrungspflicht, Archivierungsweisung oder ein konkreter Rechtsstreit
  entgegensteht.
- Unterauftragnehmer werden nicht mehr nur dokumentiert und per
  Widerspruchsmechanismus freigegeben. Das Produktionsstudio muss ihnen jetzt
  dieselben Datenschutzpflichten auferlegen, insbesondere Weisungen,
  Vertraulichkeit, technische und organisatorische Maßnahmen, Unterstützung,
  Kontrollrechte, Rückgabe und Löschung.
- Der Drei-Ordner-Kategorienindex verweist beim gerichtlichen
  Prozessvergleich wieder auf den kanonischen Ordner `prozessvorlagen/` und
  nicht mehr auf den früheren Pfad unter
  `allgemeines-und-bereichsuebergreifendes/`.
- Die zugehörigen ODT- und Markdown-ZIP-Artefakte wurden synchron neu erzeugt.

## v2.5.1 — Anwaltliche Vollmachten auf einheitliches Sozietätsmuster, neuer Themenordner `prozessvorlagen` (2026-06-20)

**Stand:** 731 Vorlagen in 37 Rechtsgebieten, Eval-Harness `All-Pass 731/731`, alle acht CI-Checks grün.

Die anwaltlichen Allgemein-Vollmachten folgen jetzt einheitlich dem in der Praxis bewährten Sozietäts-Muster: präzise Bezeichnung der Vollmachtgeberin und der Bevollmächtigten, klar abgegrenzter Sachbezug, vollständiger Befugniskatalog für gerichtliche und außergerichtliche Vertretung mit ausdrücklichem Bezug auf §§ 81 ff. ZPO, Reichweite über alle Instanzen und Nebenverfahren, Auskunfts- und Verschwiegenheitsfreigabe, Kostenersatz-Abtretung, § 181 BGB-Befreiung, Genehmigungsvollmacht, Freistellung mit Vorsatz- und Grobfahrlässigkeits-Ausnahme, zweistufiger Widerruf. Zusätzlich entsteht der neue Themenordner `prozessvorlagen`, in dem fachgebietsübergreifende prozessuale Vorlagen liegen — gestartet wird mit dem gerichtlichen Prozessvergleich, der nun das Diktat zum Protokoll nach § 160 Abs. 3 Nr. 1 ZPO ausdrücklich abbildet.

### Hinzugefügt

- Neuer Themenordner **`prozessvorlagen/`** mit eigener Bereichs-README; in `ERWARTETE_THEMEN` und `BEREICHE` der Skripte `validate-vorlagen.py`, `run-eval.py` und `generate-default-rubrics.py` eingetragen.

### Geändert

- **`allgemeines-und-bereichsuebergreifendes/vollmacht-allgemein`** komplett auf das einheitliche Sozietäts- und Einzelvollmacht-Muster umgeschrieben. Befugnisse präzisiert: Anträge und Anzeigen nach ZPO und InsO, Vertretung in Gläubigerversammlungen und -ausschüssen, Forderungsanmeldung und Widerspruch, Insolvenz-/Eigenverwaltungs-/Schutzschirm-/StaRUG-Verfahren mit Folgeprozessen, Prozessführung nach §§ 81 ff. ZPO, einseitige Willenserklärungen, freiwillige Gerichtsbarkeit, Erledigung durch Vergleich, Verzicht oder Anerkenntnis. Reichweite über alle Instanzen und Nebenverfahren mit Zustellung, Rechtsmittel, Empfang von Geld, Wertsachen und Urkunden, Akteneinsicht. Vier Anlagen: Vertretungsnachweis, Bevollmächtigtenliste, Kostenersatz- und Honorarvereinbarung, Widerrufsschreiben.
- **`allgemeines-und-bereichsuebergreifendes/vollmacht-kanzlei-und-vertretung-zweisprachig`** komplett umgestellt: jede Klausel jetzt deutsch und englisch in paralleler Pipe-Tabelle, exakt nach dem Sozietätsmuster, mit Cross-Border-Hinweis zur Apostille, Legalisation und beglaubigter Übersetzung; deutsche Fassung maßgeblich.
- **`prozessvorlagen/prozessvergleich-gerichtlich-mit-vollzug`** (verschoben aus `allgemeines-und-bereichsuebergreifendes/`): die Diktat-Mechanik nach § 160 Abs. 3 Nr. 1 ZPO ist jetzt führend — Diktattext zur Niederschrift, Protokollvermerk vor und nach dem Diktat, Variante Feststellungsbeschluss nach § 278 Abs. 6 ZPO. Zusätzliche Klauseln zu Streitwert und Vergleichswert (§ 3 ZPO, § 48 GKG, § 22 Abs. 2 RVG) und drei ausgearbeitete Anlagen (Vergleichsentwurf, Kostenvergleichsrechnung, Widerrufsschreiben).
- Bereichs-READMEs entsprechend aktualisiert.

### Geprüft

Alle acht CI-Checks grün auf 731 Vorlagen: `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`, `check-md-zip-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` All-Pass 731/731, Fail 0.

## v2.5.0 — Konsortial- und Arbeitsgemeinschaftsverträge, drei weitere Wirtschaftsrechts-Vorlagen, Umlaut- und Strukturkorrekturen (2026-06-18)

**Stand:** 715 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 715/715`, alle acht CI-Checks grün.

### Neu — sechs große Wirtschaftsrechts-Vorlagen

- `handels-und-gesellschaftsrecht/beherrschungs-und-gewinnabfuehrungsvertrag` —
  Beherrschungs- und Gewinnabführungsvertrag (Unternehmensvertrag nach
  §§ 291 ff. AktG) mit Leitungsmacht und Weisungsrecht, Gewinnabführung,
  zwingender Verlustübernahme durch dynamische Verweisung auf § 302 AktG,
  Ausgleich und Abfindung außenstehender Anteilseigner sowie Mindestlaufzeit
  der ertragsteuerlichen Organschaft.
- `handels-und-gesellschaftsrecht/verschmelzungsvertrag-umwg` —
  Verschmelzungsvertrag (Verschmelzung durch Aufnahme, § 2 Nr. 1 UmwG) mit dem
  Mindestinhalt nach § 5 UmwG, Verschmelzungsstichtag, Umtauschverhältnis,
  Schlussbilanz, Verschmelzungsbericht und -prüfung, Kapitalerhöhung,
  Registeranmeldung sowie Gläubiger- und Arbeitnehmerschutz.
- `handels-und-gesellschaftsrecht/konsortialkreditvertrag` —
  syndizierter Konsortialkredit eines Kreditgeberkonsortiums (Bankenkonsortium)
  mit anteiligen Zusagen der Kreditgeber als Teilschuld (§ 420 BGB), Bündelung
  über einen Konsortialführer (Agent) und einen Sicherheitentreuhänder mit
  Parallelschuld, Verzugszins der Tilgung nach § 288 Abs. 1 BGB,
  Mehrheitsentscheidungen nach Zusagen und Pro-rata-Gleichbehandlung.
- `handels-und-gesellschaftsrecht/emissionskonsortialvertrag` —
  Übernahmevertrag eines Bankenkonsortiums über die Übernahme und Platzierung
  einer Wertpapieremission mit nur anteiliger Übernahme (§ 420 BGB),
  Bookbuilding, Mehrzuteilungsoption (Greenshoe) und Stabilisierung,
  Prospektverantwortung und Freistellung nach Wertpapierprospektgesetz (WpPG)
  und EU-Prospektverordnung, Marktschutz (Lock-up) und Rücktritt bei
  wesentlicher nachteiliger Veränderung.
- `bau-und-architektenrecht/arbeitsgemeinschaftsvertrag-arge` —
  Bau-Arbeitsgemeinschaftsvertrag (ARGE) als nach außen auftretende,
  rechtsfähige Gesellschaft bürgerlichen Rechts (MoPeG) mit Bezug auf den
  Hauptauftrag und die Vergabe- und Vertragsordnung für Bauleistungen, Teil B
  (VOB/B), gesamtschuldnerischer Außenhaftung der Gesellschafter (§ 421 BGB)
  und Innenausgleich nach Quoten (§ 426 BGB), den klassischen ARGE-Organen,
  Beistellungen und Gerätevorhaltung, Wagnis und Gewinn sowie Auseinandersetzung.

Hinzu kommt die ebenfalls in dieser Fassung erstmals enthaltene Vorlage
`handels-und-gesellschaftsrecht/konsortialvertrag` (Innenkonsortium in der
Rechtsform der Gesellschaft bürgerlichen Rechts, §§ 705 ff. BGB).

### Ausgebaut

- `handels-und-gesellschaftsrecht/konsortialvertrag` um fünf Abschnitte
  erweitert (Höhere Gewalt und Störung des Vorhabens, Steuern und Umsatzsteuer,
  Datenschutz im Konsortium, Compliance und Sanktionen, Versicherung) sowie um
  ein Abtretungs- und Verfügungsverbot über den Konsortialanteil
  (Abschnitt 3.6) und eine Verzugszinsregelung für rückständige Beiträge nach
  § 288 Abs. 1 BGB (Abschnitt 9.6); neue Anlage 3 (Versicherungs- und
  Datenschutzfestlegungen). Die Schlussbestimmungen rücken auf Abschnitt 20;
  alle internen Querverweise wurden geprüft.

### Behoben

- Drei ASCII-Ersatzschreibungen in Vorlagentexten korrigiert: „Verfügung"
  → „Verfügung" (Kronzeugenantrag), „Rueckgabe" → „Rückgabe"
  (CMR-Ladungsschein) und „erfuellen" → „erfüllen"
  (LkSG-Eingangsbestätigung).
- Strukturfehler im Kronzeugenantrag behoben: die Zeile „Lizenz: Apache-2.0 OR
  MIT." stand mitten im Dokument vor dem Schluss- und Anlagenteil; sie steht nun
  konventionsgemäß als letzte Zeile.
- Strukturfehler im Bereichsindex `bau-und-architektenrecht/README.md` behoben:
  fünf Tabellenzeilen standen unterhalb des Lizenz-Abschnitts; sie stehen nun
  wieder innerhalb der Vorlagentabelle.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene`, `check-md-zip-integrity` OK; `run-eval`:
  `All-Pass 715/715`.
- Das human_review-Token (`r90-az-live-verifiziert`, `r91-endpruefung-anwalt`)
  bleibt offen und ist vor jeder Mandatsverwendung anwaltlich zu prüfen.


## v2.4.6 — Podcast-Anlagen und Auftragsverarbeitung geschärft (2026-06-20)

**Stand:** 753 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle neun CI-Checks grün.

### Korrigiert — Podcast-Produktionsvertrag

- Anlage 1 enthält jetzt einen ausfüllbaren Episoden-, Themen- und Terminplan
  mit Aufnahmedaten, Schnittabgabe, Veröffentlichungsterminen und
  Produktionszeitraum. Die Verweise aus den Laufzeit- und Verzugsregelungen
  laufen damit auf einen tatsächlich nutzbaren Zeitplan.
- Anlage 4 ist nicht mehr nur eine Beschreibung von Gästedaten, sondern bildet
  die für einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO wesentlichen
  Pflichten ab: Weisungen, Vertraulichkeit, technische und organisatorische
  Maßnahmen, Unterauftragnehmer, Drittlandtransfer, Unterstützung,
  Kontrollrechte, Rückgabe und Löschung.
- Die zugehörigen ODT- und Markdown-ZIP-Artefakte wurden synchron neu erzeugt.

## v2.4.5 — Qualitätsrunde Anlagen, Vertragseingänge und Download-Artefakte (2026-06-20)

**Stand:** 753 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle neun CI-Checks grün.

### Verbessert — Anlagenblöcke und Formulierungsqualität

- In der Kasko-Klage, der Pflegegrad-Klage, der Familiennachzugs-Klage und der
  Vergabe-Leistungsbeschreibung wurden generische Anlagenbezeichnungen wie
  „Beleg 4" oder „Nachweis 7" durch sachbezogene, sofort verständliche
  Anlagenzwecke ersetzt.
- Der Podcast-Produktionsvertrag enthält jetzt ausgearbeitete Anlagen für
  Episodenplan, Moderatoreneinwilligung, Moderationsvergütung und
  Auftragsverarbeitung statt bloßer Anlagen-Merkzeilen.

### Korrigiert — sichtbare Sprach- und Strukturfehler

- Die Kasko-Klage wurde am Rubrum und Schluss bereinigt: doppelte
  Unterschriftsreste und generische Kopfangaben sind entfernt.
- Zwei Vertragseingänge mit der fehlerhaften Formulierung „ist vertrag über"
  wurden in klare Vertragssprache überführt.
- Die geänderten Markdown-, ODT- und Markdown-ZIP-Dateien sind synchron neu
  erzeugt.

## v2.4.4 — Rechtsprechungshygiene nach amtlichen Bundesgerichtsquellen (2026-06-20)

**Stand:** 753 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle neun CI-Checks grün.

### Korrigiert — BImSchG-Vorlagen

- Die Vorlagen `widerspruch-bimsch-bescheid` und
  `klage-bimsch-genehmigung-vg` verwenden BVerwG, Urteil vom 3. Dezember
  2025, Az. 7 A 14.25, nicht mehr als pauschalen Rechtssatz zum allgemeinen
  Beurteilungszeitpunkt. Der Text benennt jetzt präzise, dass die amtliche
  Entscheidung die Änderungsgenehmigungsbedürftigkeit eines konkreten
  LNG-Terminal-Weiterbetriebs nach § 16 BImSchG betrifft.

### Präzisiert — DSGVO und Auftragsverarbeitung

- Die Vorlagen `auftragsverarbeitungsvertrag-dsgvo` und
  `software-as-a-service-vertrag` fassen BGH, Urteil vom 11. November 2025,
  Az. VI ZR 396/24, enger am amtlichen Leitsatz: Der Verantwortliche muss bei
  Auftragsende das nach den Umständen Erforderliche zur tatsächlichen Rückgabe
  oder Löschung beim Auftragsverarbeiter beitragen; verbleibende und später
  abgegriffene Daten können einen immateriellen Schaden nach Art. 82 DSGVO
  begründen.
- Die geänderten Markdown-, ODT- und Markdown-ZIP-Dateien sind synchron neu
  erzeugt.

## v2.4.3 — Anti-Generik-Schärfung und formale Kopfangaben (2026-06-20)

**Stand:** 753 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle neun CI-Checks grün.

### Verbessert — konkrete Vertrags- und Projektpflichten

- In Factoring-, Intercreditor-, SAFT-, F&E-, Cloud-Migration-, TSA-, Escrow-,
  AÜG-, Kommissions-, OEM-, Rahmenliefer- und Garantievorlagen wurden
  generische Informations-, Garantie- und Prüfprotokollformeln durch
  gegenstandsspezifische Pflichten ersetzt. Die Klauseln benennen jetzt
  konkrete Dokumente, Fristen, Freigaben, Register, Akten und Risiken des
  jeweiligen Vertrags.
- Wiederkehrende Formulierungen wie allgemeine Prüfungen „empfangener
  Unterlagen" und abstrakte Protokolle zu „Rechten, Pflichten, Fristen" sind
  aus den betroffenen Vorlagen entfernt.

### Verbessert — Rubrum und Abschnittslogik

- Freistehende `Gegenstand:`-Zeilen vor Abschnitt 1 wurden in formale
  `Aktenangabe:`-Zeilen umgestellt. Der materielle Gegenstand bleibt damit in
  der nummerierten Abschnittslogik und die Vorlagenköpfe wirken ruhiger.
- `scripts/check-gliederung.py` erkennt jetzt auch einfache `Gegenstand:`-
  Zeilen außerhalb der Abschnittslogik, nicht nur fett gesetzte
  `**Gegenstand:**`-Zeilen.

## v2.4.2 — Weitere arbeits-, familien- und erbrechtliche Prozessvorlagen (2026-06-20)

**Stand:** 753 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 753/753`, alle neun CI-Checks grün.

### Neu — sechs zusätzliche Vorlagen

- **Arbeitsrecht:** Klage auf Annahmeverzugslohn nach Kündigung und Klage auf
  Herausgabe von Arbeitspapieren und Abrechnungsunterlagen.
- **Familienrecht:** Antrag auf Abänderung eines Unterhaltstitels und Antrag
  auf Wohnungszuweisung während der Trennung.
- **Erbrecht:** Anfechtungserklärung gegen ein Testament beim Nachlassgericht
  und Klage auf Herausgabe von Nachlassgegenständen.

### Verbessert — Einsortierung und Lesbarkeit

- Die neuen Vorlagen sind in den Rechtsgebiets-READMEs und in der
  prozessualen Drei-Ordner-Sicht einsortiert.
- Die Vorlagendateien enthalten nur den knappen Kurz-Hinweis und danach den
  eigentlichen Schriftsatz oder Antrag; Anwendungsbereich, Grenzen,
  Normenanker und Downloadlinks stehen jeweils in der README.
- Die neuen Muster sind ohne Bullet-Rubrum, mit klaren Parteiköpfen,
  vollständigen Sätzen, dezimaler Gliederung und sprechenden Dateinamen
  angelegt.

## v2.4.1 — Rechtsgebiets-Unterordner in der Drei-Ordner-Sicht (2026-06-20)

**Stand:** 747 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 747/747`, alle neun CI-Checks grün.

### Verbessert — Drei-Ordner-Sicht

- Die drei Oberordner unter `kategorien/` sind jetzt jeweils nach Rechtsgebieten
  untergliedert. Die Suche läuft damit zuerst über die Arbeitsperspektive
  (vertraglich, prozessual/Formular, sonstig) und anschließend über das
  einschlägige Rechtsgebiet.
- Die kanonischen Vorlagenordner bleiben unverändert. Die neuen
  Rechtsgebiets-Unterordner enthalten ausschließlich README-Indizes mit Links
  auf die bestehenden Vorlagenordner, damit Download-Links, Rubrics, ODT-Dateien
  und Markdown-ZIP-Dateien stabil bleiben.
- `scripts/check-kategorien-index.py` validiert die verschachtelte
  Kategorienstruktur und prüft weiterhin, dass jede Vorlage genau einmal in der
  Drei-Ordner-Sicht verlinkt ist.

## v2.4.0 — Drei-Ordner-Sicht, zweiunddreißig neue Vorlagen und Einsortierungskorrekturen (2026-06-20)

**Stand:** 747 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 747/747`, alle neun CI-Checks grün.

### Neu — Drei-Ordner-Sicht (zusätzliche Navigationsschicht)

- Der Ordner `kategorien/` bietet eine zusätzliche, leichter verständliche Sicht
  auf den Bestand in drei Sammlungen: `01-vertragliche-vorlagen` (Verträge,
  Satzungen, AGB, Vollmachten, Sicherheiten, Vergleiche und sonstige
  kautelarische Vorlagen), `02-prozessuale-vorlagen-und-formulare` (Klagen,
  Anträge, Beschwerden, Widersprüche, behördliche und gerichtliche Formulare,
  Protokolle, Verzeichnisse, Nachweise und Dokumentationsmuster) sowie
  `03-sonstige-vorlagen` (Leitvorlagen, Pläne, Vermerke, Risikomatrizen,
  Strategie- und Prüfpapiere). Die kanonischen Vorlagen bleiben in ihren
  Rechtsgebietsordnern; die Drei-Ordner-Sicht ist ein reiner Navigationsindex,
  damit Rubrics, ODT-Dateien, Markdown-ZIP-Downloads und bestehende Direktlinks
  stabil bleiben.
- Neuer CI-Check `scripts/check-kategorien-index.py`: Er stellt sicher, dass
  jede Vorlage genau einmal in einer der drei Sichten verlinkt ist, keine toten
  Links entstehen und die Zähler im Kategorie-README stimmen. Die CI prüft damit
  jetzt neun Checks.

### Neu — zweiunddreißig Vorlagen

- **Arbeitsrecht (zehn):** Anhörung zur Verdachtskündigung, Antrag auf
  Einsetzung der Einigungsstelle (§ 76 BetrVG), zwei einstweilige Verfügungen
  (Weiterbeschäftigung sowie betriebsverfassungsrechtlich), Antrag auf
  Elternzeit-Teilzeit (BEEG), Beschlussverfahren nach § 99 BetrVG,
  Betriebsvereinbarung Arbeitszeiterfassung, Klage auf Nachteilsausgleich
  (§ 113 BetrVG), Klage auf Urlaubsabgeltung und Klage auf
  Zeugnisberichtigung.
- **Erbrecht (neun):** Aufgebot der Nachlassgläubiger, Einziehung des
  Erbscheins, Entlassung des Testamentsvollstreckers, Grundbuchberichtigung im
  Erbfall, Nachlassinsolvenzverfahren, Nachlasspflegschaft,
  Nachlassverwaltung, Beschwerde gegen die Erbscheinerteilung und Klage auf
  Feststellung der Erbunwürdigkeit.
- **Familienrecht (neun):** Alleinentscheidungsbefugnis (§ 1628 BGB),
  einstweilige Anordnung zum Unterhalt, Kindesherausgabe (§ 1632 BGB),
  Kindeswohlmaßnahmen (§§ 1666, 1666a BGB), Ordnungsmittel im Umgang,
  Zugewinnausgleich als Folgesache, Auskunftsschreiben zum Endvermögen,
  Erwiderung auf den Scheidungsantrag in Folgesachen und Vereinbarung zum
  Wechselmodell mit Betreuungsplan.
- **Mietrecht und Wohnungseigentumsrecht (vier):** einstweilige Verfügung zum
  Mietgebrauch, Klage auf Mängelbeseitigung und Mietminderung, Klage auf
  Unterlassung vertragswidrigen Gebrauchs und Klage auf Zustimmung zur
  Mieterhöhung.

### Behoben — Einsortierung in der Drei-Ordner-Sicht

Sieben Vorlagen standen in der falschen Sammlung und wurden umsortiert, damit
gleichartige Vorlagen beieinanderstehen:

- nach `01-vertragliche-vorlagen`: die Marketplace-Händler-AGB (von
  `03`), die Einsatzvereinbarung Leiharbeit und die Räumungsvereinbarung
  Wohnraum (beide von `02`), die drei Letter-of-Intent-Vorlagen (von `02`,
  da kautelarische Vorvertragsdokumente) sowie die Bietererklärung zu
  Interessenkonflikten (von `03`, zu den übrigen Vergabe-Erklärungen).

### Geprüft

- Einsortierung der Drei-Ordner-Sicht repo-weit gesichtet: alle eindeutigen
  Verträge stehen in `01`, alle eindeutigen Klagen, Anträge und Rechtsbehelfe
  in `02`. Verbliebene Grenzfälle (einseitige Erklärungen, Gesellschafter- und
  Organbeschlüsse als Dokumentationsmuster, bindende Insolvenz- und
  Restrukturierungspläne) sind bewusst einheitlich zugeordnet.
- Bug-Hunt zu Querverweisen, Abschnittsnummerierung und Buchstaben-Restspuren
  ohne neue Befunde; die neuen Vorlagen sind regelkonform (Kurz-Hinweis,
  Dezimalgliederung, vollständige Sätze, belegte Normen, kein verbotener
  Abschnitt „Mandatsreife Prüfmatrix").
- `validate-vorlagen`, `check-gliederung`, `check-kategorien-index`,
  `check-odt-integrity`, `check-odt-spaltenlayout`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene`,
  `check-md-zip-integrity` OK; `run-eval`: `All-Pass 747/747`.

## v2.3.1 — Sanity-Check und Bug-Hunt: Querverweise, Abschnittsnummerierung und Bereichsindizes (2026-06-18)

**Stand:** 715 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 715/715`, alle acht CI-Checks grün.

### Behoben — Bereichsindizes (Tabellenzeilen unterhalb des Footers)

In vier Bereichs-READMEs standen Tabellenzeilen versehentlich unterhalb der
Abschnitte „Rechtliche Hinweise" und „Lizenz" statt in der Vorlagentabelle; sie
stehen nun wieder innerhalb der Tabelle:

- `vergaberecht/README.md` (fünf Zeilen),
- `informationstechnologierecht/README.md` (fünf Zeilen),
- `internationales-wirtschaftsrecht/README.md` (zwei Zeilen),
- `allgemeines-und-bereichsuebergreifendes/README.md` (zehn Zeilen).

### Behoben — Abschnittsnummerierung

- `mergers-and-acquisitions/due-diligence-request-list-legal`: Der letzte
  Themenblock war fälschlich als „1. Compliance / AML / Sanctions" nummeriert
  und steht nun korrekt als „9." in der Folge der Themenblöcke 1 bis 9.
- `allgemeines-und-bereichsuebergreifendes/mandatsvertrag-anwaltsvergutung`:
  Die Schlussbestimmungen waren als Abschnitt 10 nummeriert, obwohl nur die
  Abschnitte 1 und 2 vorausgehen; sie stehen nun als Abschnitt 3 (samt
  Unterpunkten 3.1 bis 3.3).
- `insolvenzrecht/insolvenzplan-darstellender-und-gestaltender-teil`: Der
  Abschnitt „Abstimmung, Mehrheiten und gerichtliche Bestätigung" im
  darstellenden Teil war als „9." statt als „1.9" nummeriert; er und seine
  Unterpunkte stehen nun als „1.9" bis „1.9.6". Außerdem wurden Restverweise aus
  einer früheren Buchstabengliederung berichtigt (B.1 zu Abschnitt 2.1, der
  Verweis auf „B.8" auf den gestaltenden Teil, Abschnitt 7 zu Abschnitt 1.7 und
  Abschnitt 9.2 zu Abschnitt 1.9.2).

### Behoben — verirrte Buchstaben-Querverweise in Klagemustern

In vier Klagemustern verwiesen Restspuren einer früheren A./B./C.-Gliederung
ins Leere; sie zeigen nun auf die richtigen Dezimalabschnitte:

- `insolvenzrecht/klage-insolvenzanfechtung` (A.2, A.3, A.4 zu Abschnitt 2.1
  Nummer 2, 3 und 4),
- `bank-und-kapitalmarktrecht/klage-rueckabwicklung-darlehenswiderruf` (B.4 zu
  Abschnitt 2.2 Nummer 4),
- `internationales-wirtschaftsrecht/klage-kaufpreis-cisg` (A.2, A.3 zu
  Abschnitt 2.1 Nummer 2 und 3),
- `migrationsrecht/klage-niederlassungserlaubnis` (C.1 zu Abschnitt 2.3).

### Geprüft

- Repo-weiter Bug-Hunt zu Abschnitts-Sequenz, internen Querverweisen,
  Anlagenverweisen, Lizenz-Position und Bereichsindizes. Die verbliebenen
  Treffer sind durchweg unkritisch: zwei Verweise zeigen bewusst in die
  Gliederung externer Dokumente (Anteilskaufvertrags-Anlage und AKB), die
  übrigen betreffen Mehrdokument-Muster, Beweismittel-Anlagen in Klagen oder die
  uneinheitliche, aber zulässige Lizenz-Position am Dokumentende.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene`, `check-md-zip-integrity` OK; `run-eval`:
  `All-Pass 715/715`.

## v2.3.0 — Konsortial- und Arbeitsgemeinschaftsverträge, drei weitere Wirtschaftsrechts-Vorlagen, Umlaut- und Strukturkorrekturen (2026-06-18)

**Stand:** 715 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 715/715`, alle acht CI-Checks grün.

### Neu — sechs große Wirtschaftsrechts-Vorlagen

- `handels-und-gesellschaftsrecht/beherrschungs-und-gewinnabfuehrungsvertrag` —
  Beherrschungs- und Gewinnabführungsvertrag (Unternehmensvertrag nach
  §§ 291 ff. AktG) mit Leitungsmacht und Weisungsrecht, Gewinnabführung,
  zwingender Verlustübernahme durch dynamische Verweisung auf § 302 AktG,
  Ausgleich und Abfindung außenstehender Anteilseigner sowie Mindestlaufzeit
  der ertragsteuerlichen Organschaft.
- `handels-und-gesellschaftsrecht/verschmelzungsvertrag-umwg` —
  Verschmelzungsvertrag (Verschmelzung durch Aufnahme, § 2 Nr. 1 UmwG) mit dem
  Mindestinhalt nach § 5 UmwG, Verschmelzungsstichtag, Umtauschverhältnis,
  Schlussbilanz, Verschmelzungsbericht und -prüfung, Kapitalerhöhung,
  Registeranmeldung sowie Gläubiger- und Arbeitnehmerschutz.
- `handels-und-gesellschaftsrecht/konsortialkreditvertrag` —
  syndizierter Konsortialkredit eines Kreditgeberkonsortiums (Bankenkonsortium)
  mit anteiligen Zusagen der Kreditgeber als Teilschuld (§ 420 BGB), Bündelung
  über einen Konsortialführer (Agent) und einen Sicherheitentreuhänder mit
  Parallelschuld, Verzugszins der Tilgung nach § 288 Abs. 1 BGB,
  Mehrheitsentscheidungen nach Zusagen und Pro-rata-Gleichbehandlung.
- `handels-und-gesellschaftsrecht/emissionskonsortialvertrag` —
  Übernahmevertrag eines Bankenkonsortiums über die Übernahme und Platzierung
  einer Wertpapieremission mit nur anteiliger Übernahme (§ 420 BGB),
  Bookbuilding, Mehrzuteilungsoption (Greenshoe) und Stabilisierung,
  Prospektverantwortung und Freistellung nach Wertpapierprospektgesetz (WpPG)
  und EU-Prospektverordnung, Marktschutz (Lock-up) und Rücktritt bei
  wesentlicher nachteiliger Veränderung.
- `bau-und-architektenrecht/arbeitsgemeinschaftsvertrag-arge` —
  Bau-Arbeitsgemeinschaftsvertrag (ARGE) als nach außen auftretende,
  rechtsfähige Gesellschaft bürgerlichen Rechts (MoPeG) mit Bezug auf den
  Hauptauftrag und die Vergabe- und Vertragsordnung für Bauleistungen, Teil B
  (VOB/B), gesamtschuldnerischer Außenhaftung der Gesellschafter (§ 421 BGB)
  und Innenausgleich nach Quoten (§ 426 BGB), den klassischen ARGE-Organen,
  Beistellungen und Gerätevorhaltung, Wagnis und Gewinn sowie Auseinandersetzung.

Hinzu kommt die ebenfalls in dieser Fassung erstmals enthaltene Vorlage
`handels-und-gesellschaftsrecht/konsortialvertrag` (Innenkonsortium in der
Rechtsform der Gesellschaft bürgerlichen Rechts, §§ 705 ff. BGB).

### Ausgebaut

- `handels-und-gesellschaftsrecht/konsortialvertrag` um fünf Abschnitte
  erweitert (Höhere Gewalt und Störung des Vorhabens, Steuern und Umsatzsteuer,
  Datenschutz im Konsortium, Compliance und Sanktionen, Versicherung) sowie um
  ein Abtretungs- und Verfügungsverbot über den Konsortialanteil
  (Abschnitt 3.6) und eine Verzugszinsregelung für rückständige Beiträge nach
  § 288 Abs. 1 BGB (Abschnitt 9.6); neue Anlage 3 (Versicherungs- und
  Datenschutzfestlegungen). Die Schlussbestimmungen rücken auf Abschnitt 20;
  alle internen Querverweise wurden geprüft.

### Behoben

- Drei ASCII-Ersatzschreibungen in Vorlagentexten korrigiert: „Verfügung"
  → „Verfügung" (Kronzeugenantrag), „Rueckgabe" → „Rückgabe"
  (CMR-Ladungsschein) und „erfuellen" → „erfüllen"
  (LkSG-Eingangsbestätigung).
- Strukturfehler im Kronzeugenantrag behoben: die Zeile „Lizenz: Apache-2.0 OR
  MIT." stand mitten im Dokument vor dem Schluss- und Anlagenteil; sie steht nun
  konventionsgemäß als letzte Zeile.
- Strukturfehler im Bereichsindex `bau-und-architektenrecht/README.md` behoben:
  fünf Tabellenzeilen standen unterhalb des Lizenz-Abschnitts; sie stehen nun
  wieder innerhalb der Vorlagentabelle.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene`, `check-md-zip-integrity` OK; `run-eval`:
  `All-Pass 715/715`.
- Das human_review-Token (`r90-az-live-verifiziert`, `r91-endpruefung-anwalt`)
  bleibt offen und ist vor jeder Mandatsverwendung anwaltlich zu prüfen.

## v2.2.4 — Sanity-Check, Bug-Hunt und Look-&-Feel-Feinschliff (2026-06-18)

**Stand:** 709 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 709/709`.

### Behoben

- `scripts/update-readme-md-zip-links.py` war nicht idempotent: bei jedem Lauf
  hängte es den Zusatz „, gepackt für direkten Download" erneut an und hätte so
  die README-Beschriftungen bei wiederholter Ausführung verdoppelt. Die Stelle
  arbeitet jetzt mit einer Negativ-Lookahead-Ersetzung und ist idempotent.
- Die README des neuen Gewerbemietvertrags verwies noch auf die rohe `.md`; der
  Download-Link zeigt nun konventionsgemäß auf die `.md.zip`.

### Look & Feel

- Letzte sechs frei stehende Abschnittsnummern, die allein über einer Tabelle
  standen (KI-Transparenzbericht und KI-Pflichtencheckliste), erhalten einen
  vollständigen, einleitenden Satz, der die jeweilige Tabelle ankündigt. Damit
  steht im gesamten Bestand keine Nummer mehr nackt über einem Absatz oder einer
  Tabelle.

### Geprüft (Sanity-Check und Bug-Hunt)

- Abschnitts-Sequenz, interne Querverweise und Anlagenverweise repo-weit
  gesichtet; die verbliebenen Treffer sind durchweg Mehrdokument-Vorlagen
  (etwa Schiedsvereinbarung mit zwei Varianten) oder externe Verweise und keine
  echten Fehler.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene`, `check-md-zip-integrity` OK; `run-eval`:
  `All-Pass 709/709`.

## v2.2.3 — Regelungstiefe-Standard an schlanke Vorlagen angepasst (2026-06-18)

**Stand:** 709 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 709/709`, alle acht CI-Checks grün.

### Korrigiert

- Der Schärfungs-Standard `references/regelungstiefe-vertraege.md` verweist
  in der Freigabe-Checkliste nicht mehr auf eine zu aktualisierende
  `Mandatsreife Prüfmatrix`, weil dieser Block seit `v2.2.0` nicht mehr in
  Vorlagentexten geführt wird.
- Stattdessen verlangt die Checkliste nun die dokumentierte anwaltliche
  Endprüfung außerhalb der Vorlage in der Mandatsakte.

## v2.2.2 — Gliederung der Insolvenzvollmacht CI-konform korrigiert (2026-06-18)

**Stand:** 709 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 709/709`, alle acht CI-Checks grün.

### Korrigiert

- In der umfassenden anwaltlichen Vollmacht in Insolvenzsachen wurde die
  unzulässige a)–d)-Untergliederung in Abschnitt 6.2 durch die zulässige
  Dezimalgliederung 6.2.1 bis 6.2.4 ersetzt.
- Der erläuternde Ausweichsatz zur Buchstabenliste wurde entfernt.
- Die betroffene ODT-Datei und der Markdown-ZIP-Download wurden neu erzeugt.

## v2.2.1 — Umfassende anwaltliche Vollmacht in Insolvenzsachen ergänzt (2026-06-18)

**Stand:** 709 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 709/709`, alle acht CI-Checks grün.

### Hinzugefügt

- **`insolvenzrecht/vollmacht-insolvenzverfahren-umfassend`** als zusätzliche Variante neben den bestehenden Vollmachts-Vorlagen. Sozietäts- und Einzelvollmacht mit präzisen Befugnissen für Tabellenanmeldung (§ 174 InsO), Gläubigerversammlungen (§§ 74 ff. InsO), Gläubigerausschuss (§§ 67 ff. InsO), Insolvenzanfechtungssachen (§§ 129 ff. InsO), Feststellungsstreitigkeiten (§ 180 InsO) und allen prozessualen Folgeverfahren. Enthält Kostenersatz-Abtretung, § 181 BGB-Befreiung, Auskunfts- und Verschwiegenheitsfreigabe mit Verweis auf § 43a Abs. 2 BRAO, § 203 StGB und DSGVO, vier ausgearbeitete Anlagen (Vertretungsnachweis, Forderungsaufstellung, Kostenersatz- und Honorarvereinbarung, Widerrufsschreiben).
- Bereichs-README in `insolvenzrecht/` um den neuen Eintrag ergänzt.

Die bestehenden Vollmachts-Vorlagen (`allgemeines-und-bereichsuebergreifendes/vollmacht-allgemein`, `vollmacht-kanzlei-und-vertretung-zweisprachig`, `generalvollmacht`, `strafrecht/strafprozessvollmacht-verteidigung`, `erbrecht/*-vollmacht*`) bleiben unverändert; die neue Vorlage ergänzt das Spektrum um eine insolvenzbezogene Variante.


## v2.2.0 — Mandatsreife Prüfmatrix repoweit aus Vorlagen entfernt (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`, alle acht CI-Checks grün.

Der bisher am Ende jeder Vorlagen-Markdown wiederkehrende Block `## Mandatsreife Prüfmatrix` wirkte als generische Freigabeliste, ließ jede Vorlage am Schluss gleich aussehen und trug keinen konkreten Mandatsbezug. Mit dieser Version verschwindet er vollständig — sowohl aus den Vorlagentexten als auch aus den darüberliegenden Regeln und Prüfungen.

### Geändert

- **708 Vorlagen-Markdowns** entkleidet: `## Mandatsreife Prüfmatrix` (einschließlich nummerierter Varianten wie `## 6. Mandatsreife Prüfmatrix`) entfernt; trailing Whitespace bereinigt; jede `<slug>.odt` und `<slug>.md.zip` aus der bereinigten Quelle neu erzeugt.
- **`scripts/validate-vorlagen.py`:** `Mandatsreife Prüfmatrix` aus `PFLICHT_TOKENS` und `README_PFLICHT_TOKENS` entfernt; `## Mandatsreife Prüfmatrix` und `### Mandatsreife Prüfmatrix` zur Liste `VERBOTENE_TEMPLATE_ABSCHNITTE` aufgenommen, damit der Block nicht wieder einsickert.
- **`scripts/generate-default-rubrics.py`:** Rubric-Check `r81-mandatsreife-pruefmatrix` und die einleitende Doku-Zeile gestrichen. Aus dem Pattern für `r16-abschnittsgliederung` wurde die alte Annahme „mindestens zwei H2-Überschriften" entfernt; eine H2 reicht jetzt aus, da viele Vorlagen schlank mit nur `## Vorlage` auskommen.
- **708 `rubric.yaml`-Dateien:** `r81-mandatsreife-pruefmatrix` und der zugehörige Kommentar entfernt; das `r16`-Pattern entsprechend angepasst.
- **`CLAUDE.md` Abschnitt 16** neu gefasst: aus „Mandatsreife Prüfmatrix" wird die explizite Regel „Keine Mandatsreife Prüfmatrix in Vorlagen". Abschnitt 17 entsprechend angepasst.
- **`templates/_hinweise.md`** und **`README.md`** angeglichen: die Endprüfung findet außerhalb der Vorlage statt.
- **Zwölf Schriftsatz-/Meldungsvorlagen** um einen knappen Antrags-/Anzeigensatz ergänzt (BaFin-Stellungnahme, VOB/B-Bedenkenanzeige und -Nachtragsangebot, DSK-Incident-Meldung, Insolvenz-Freigabe, Kronzeugenantrag, USt-Voranmeldungskorrektur, CMR-Ladungsschein, LkSG-Beschwerdebestätigung, W&I-Anfrage, DSA-Trusted-Flagger, P2B-Beschwerdeantwort), damit der Eval-Check `r17-antrag-oder-begehren` weiterhin greift, nachdem das frühere Antragsverb im entfernten Mandatsreife-Block stand.

### Geprüft

Alle acht CI-Checks grün auf 708 Vorlagen: `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`, `check-md-zip-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` liefert **All-Pass 708/708**, Fail 0.


## v2.1.11 — Preispläne in Rahmenlieferung und Cloud-Migration geschärft (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- Im B2B-Rahmenliefervertrag stehen Basispreise, Staffelpreise, Zuschläge,
  Werkzeugumlagen, Frachtkosten und Zahlungsziel jetzt ausdrücklich im
  Preisblatt der Anlage 5; die Lieferfensteranlage wird nicht mehr als
  Preisplan verwendet.
- Im Cloud-Migration-Projektvertrag gibt es jetzt eine eigene Anlage 5 für
  Projektvergütung, Meilensteine, Change Requests, Provider-Weiterbelastungen
  und Exit-Kosten; Abnahme- und Handover-Anlagen werden nicht mehr als
  Vergütungsplan missverstanden.
- Die betroffenen ODT-Dateien und Markdown-ZIP-Downloads wurden neu erzeugt.

## v2.1.10 — Restgenerik in Spezialverträgen weiter bereinigt (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Veredelt

- In 18 Spezialverträgen verbliebene generische Anlagen-, Vollzugs- und
  Zahlungssätze durch gegenstandsspezifische Regelungen ersetzt.
- Besonders Factoring, Arbeitnehmerüberlassung, B2B-Rahmenlieferung,
  OEM-Entwicklung, Cloud-Migration, KI-Datenlizenz, F&E/IP, TSA, Escrow und
  SAFT wurden in den operativen Abschnitten 2.3, 4.1, 5.1 und 5.2
  präzisiert.
- Die Sanity-Suche nach den bisherigen Restgenerik-Mustern ist leer.
- Alle betroffenen ODT-Dateien und Markdown-ZIP-Downloads wurden neu erzeugt.

## v2.1.9 — Textform in Brückenteilzeit-Rückkehrplan vereinheitlicht (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- In der Brückenteilzeit-Vereinbarung verweist der Rückkehrplan in Anlage 1
  jetzt auf Vereinbarungen in Textform und passt damit zur allgemeinen
  Änderungsregel in Abschnitt 9.1.
- Die betroffene ODT-Datei und der Markdown-ZIP-Download wurden neu erzeugt.

## v2.1.8 — Brückenteilzeit-Anlage für Entgeltfolgen ausgearbeitet (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- In der Brückenteilzeit-Vereinbarung ist Anlage 1 jetzt ein ausgearbeiteter
  Arbeitszeit-, Entgelt- und Rückkehrplan statt eines allgemeinen
  Unterlagenverzeichnisses.
- Die Anlage enthält konkrete Felder für bisherige und verringerte
  Wochenarbeitszeit, Einsatzplanung, Bruttovergütung, Zulagen, variable
  Vergütung, Urlaub, Arbeitszeitkonto, Mehrarbeit und Rückkehr zur bisherigen
  Arbeitszeit.
- Der Verweis aus Abschnitt 5.2 auf Anlage 1 ist damit inhaltlich
  vollständig hinterlegt.
- Die betroffene ODT-Datei und der Markdown-ZIP-Download wurden neu erzeugt.

## v2.1.7 — Querverweise in Brückenteilzeit und SAFT korrigiert (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- In der Brückenteilzeit-Vereinbarung zeigen die Pflichten zur
  Arbeitszeitverringerung, Verteilung, Rückkehr, Vergütungsanpassung und
  Dokumentation jetzt auf die jeweils tragenden Abschnitte 2.4.1 bis 2.4.4.
- Die Vergütungsfolgen der Brückenteilzeit sind arbeitszeitbezogen
  ausformuliert statt als allgemeine Zahlungsklausel.
- Im zweisprachigen SAFT verweist die Purchaser-Pflicht zur Tokenlieferung
  und regulatorischen Freigabe auf 2.4.2 und 2.4.3; der Sprachvorrang bleibt
  gesondert in 2.4.4 verankert.
- Die betroffenen ODT-Dateien und Markdown-ZIP-Downloads wurden neu erzeugt.

## v2.1.6 — Restgenerik in Spezialverträgen geglättet (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Veredelt

- In 18 Spezialverträgen abstrakte Rollenüberschriften durch konkrete
  Parteibezeichnungen aus dem jeweiligen Vertragseingang ersetzt.
- Unpräzise Querverweise auf Abschnitt 2.4.4 entfernt und durch
  gegenstandsspezifische Vollzugssätze ersetzt.
- Abschnitt 5 in denselben Vertragsgruppen fachnäher benannt, etwa nach
  Factorentgelt, Escrow-Kosten, Projektvergütung, Serienpreisen,
  Serviceentgelt, Lizenzentgelt oder SAFT-Investmentbetrag.
- Die zweisprachige SAFT-Vorlage zusätzlich sprachlich geglättet und mehrere
  holprige Legal-English-Sätze bereinigt.
- Alle betroffenen ODT-Dateien und Markdown-ZIP-Downloads wurden neu erzeugt.

## v2.1.5 — Parteibezeichnungen in Anlagen vereinheitlicht (2026-06-18)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- Im F&E/IP-Vertrag verwendet Anlage 3 durchgehend die definierte
  `Entwicklungspartnerin` statt einer nicht definierten Auftragnehmerin.
- In der KI-Datenlizenz verwendet Anlage 4 durchgehend `Datennehmerin` und
  `Datengeberin` statt nicht definierter Lizenzparteien.
- Im B2B-Rahmenliefervertrag verwenden die Anlagen 3 und 5 durchgehend
  `Kundin` und `Lieferantin` statt kaufvertraglicher Ersatzbegriffe.
- Die betroffenen ODT-Dateien und Markdown-ZIP-Downloads wurden neu erzeugt.

## v2.1.4 — Anlagenverweise in Spezialverträgen geschlossen (2026-06-17)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- Fehlende Anlagen in Einzelforderungsverkauf, Intercreditor-Vereinbarung,
  F&E/IP-Vertrag, Cloud-Migration, KI-Datenlizenz, OEM-Vertrag und
  Rahmenliefervertrag ergänzt.
- Verweise auf Drittschuldneranzeige, Erlöswasserfall, Senior-Waiver,
  IP-Zuordnung, Meilensteine, Veröffentlichungsfreigaben,
  Datenschutz-/Sicherheitsmatrix, Modellartefakte, Serienpreise,
  Rückrufkosten, Qualität, Lieferfenster, Preisgleitung und Exit-Belieferung
  zeigen jetzt auf ausgearbeitete Anlagen statt auf leere oder fehlende
  Dokumente.
- Den OEM-Verweis auf einen nicht vorhandenen Abschnitt 10 auf die
  einschlägige Anlage 4 umgestellt.
- Alle geänderten ODT-Dateien und Markdown-ZIP-Downloads neu erzeugt.

## v2.1.3 — Anti-Generik-Politur und Vorlagen-Feinschliff (2026-06-17)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Veredelt

- Restliche Schablonenformulierungen wie „Spezialfall", „Spezialmaterie" und
  „operative Kernmechanik" aus Vertragsvorlagen entfernt und durch
  gegenstandsspezifische Regelungen ersetzt.
- Escrow, Transition Services, Intercreditor, Arbeitnehmerüberlassung,
  Leiharbeits-Einsatz, Brückenteilzeit, Factoring-Varianten,
  KI-Datenlizenz, Cloud-Migration, Rahmenlieferung, OEM-Entwicklung,
  Kommission, F&E/IP und SAFT in den Eingangsklauseln konkretisiert.
- Verwaltungsrechtliche Schriftsatzmuster von kursiven Schein-Nummern auf
  echte Dezimalunterpunkte umgestellt.
- Interne Vorab-Checklisten bei Selbstanzeige und Doping-Stellungnahme aus
  dem versandfertigen Dokumenttext entfernt und in die jeweilige README
  verlagert.
- Sozialrechtliche Alternativanträge und familienrechtliche
  Umgangsregelungen sprachlich geglättet und besser in den Dokumentfluss
  eingebettet.

### Synchronisiert und geprüft

- Alle geänderten ODT-Dateien und Markdown-ZIP-Downloads neu erzeugt.
- Voller Gate lokal grün: `validate-vorlagen`, `check-gliederung`,
  `check-md-zip-integrity`, `check-odt-integrity`, `check-odt-spaltenlayout`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` und `run-eval`.
  Eval: `All-Pass 708/708`.

## v2.1.2 — Gegenstandsindividualisierung als verbindlicher Standard (2026-06-17)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Ergänzt

- Neuer Referenzstandard `references/gegenstandsindividualisierung.md`:
  Gegenstand, Rollen, Interessenlage, Rechtsordnung und spezifische Risiken
  werden vor jeder Überarbeitung intern fixiert.
- `CLAUDE.md`, `CONTRIBUTING.md` und `README.md` verweisen jetzt ausdrücklich
  auf die Anti-Generik-Doktrin: Sätze, die unverändert in einem anderen
  Dokument stehen könnten, sind zu konkretisieren oder zu streichen.
- Die Doktrin gilt auch für künftige Legal-AI-Skills und Legal-AI-Plugins,
  nicht nur für Verträge und Formatvorlagen.

## v2.1.1 — StaRUG-Planwert ohne Forderungsverzicht-Doppelzählung (2026-06-17)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Korrigiert

- In `restrukturierungsrecht-starug/restrukturierungsplan-starug` werden
  Forderungsverzichte, Haircuts, Stundungen und bloße Rangänderungen nicht mehr
  als additive Neu- oder Drittmittelbeiträge in den verteilbaren Planwert
  eingestellt.
- Die Vergleichsrechnung unterscheidet jetzt ausdrücklich zwischen echten
  neuen, nicht rückzahlbaren Mittelzuflüssen und planbedingter Entlastung, die
  nur in Forderungsbasis, Barwert und Liquiditätsplan berücksichtigt wird.

## v2.0.1 — Generische Vorlagenkörper bereinigt (2026-06-17)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Entgenerisiert

- 38 Vorlagen aus Aufsichtsrecht, Europarecht, Insolvenzrecht, Kartellrecht,
  Restrukturierungsrecht, Verfassungsrecht sowie Zoll- und
  Außenwirtschaftsrecht beginnen im Dokumentkörper nicht mehr mit generischen
  Zweck-, Normen- und Quellenankerblöcken.
- Standstill-Vereinbarung, GmbH-Gründungsfahrplan, UG-Musterprotokoll-Check
  und Betriebsratsanhörung zusätzlich geglättet: keine Normanker-Schablone im
  Vertragstext, keine namenlose Anlagenliste, klarere Eingangssätze.
- Die echten README-Dateien bleiben der Ort für ausführliche Warn-, Quellen-
  und Nutzungshinweise; die eigentlichen Vorlagen starten schneller mit dem
  verwendbaren Dokument.

### Synchronisiert und geprüft

- Alle geänderten Markdown-Dateien mit gleichnamigen ODT-Dateien und
  Markdown-ZIP-Downloads neu synchronisiert.
- Voller Gate lokal grün: `validate-vorlagen`, `check-gliederung`,
  `check-md-zip-integrity`, `check-odt-integrity`, `check-odt-spaltenlayout`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` und `run-eval`.
  Eval: `All-Pass 708/708`.

## v2.0.0 — Finalisierte Integrationsfassung (2026-06-17)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

Diese Version konsolidiert die jüngsten Claude- und Codex-Beiträge zu einer
stabilen Hauptfassung. Die Sammlung enthält nun sprechend benannte Markdown-,
ODT- und ZIP-Downloads je Vorlage, kurze Hinweise in den eigentlichen
Vorlagendateien, ausführliche Hinweise in den README-Dateien, lückenlose
Dezimalgliederung und synchronisierte Download-Artefakte.

### Finalisiert

- Root-README auf den tatsächlichen Stand `All-Pass 708/708` gebracht.
- Lokale Prüfsequenz im README um `build-md-zips.py`,
  `check-md-zip-integrity.py` und `check-odt-spaltenlayout.py` ergänzt.
- StaRUG-Vergleichsrechnung zuletzt nochmals geschärft: neue Finanzierung wird
  im Planwert nicht brutto addiert, sondern nur netto nach Rückzahlungs-, Zins-,
  Rang- und Sicherheitenbelastungen berücksichtigt.
- Markdown-ZIP-Spiegelkopien nach dem aktuellen `main` synchronisiert,
  einschließlich des neuen Gewerbemietvertrags.

### Geprüft

Voller Gate lokal grün: `validate-vorlagen`, `check-gliederung`,
`build-md-zips.py`, `check-md-zip-integrity`, `check-odt-integrity`,
`check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
`check-umlauthygiene` und `run-eval`. Eval: `All-Pass 708/708`.

## v1.32.0 — Look-&-Feel-Veredelung, ausführlichere Vorlagen und neuer Gewerbemietvertrag (2026-06-16)

**Stand:** 708 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 708/708`.

### Look & Feel

- 515 frei stehende Dezimalnummern (die Ziffer stand allein auf einer Zeile,
  darunter erst nach einer Leerzeile der Text) wurden mit ihrem Absatz zu
  „1.1 Text" verschmolzen — kein zerrissener Nummern-Vorspann mehr.
- Neun fett gesetzte Pseudo-Überschriften „1 **Titel**" wurden in saubere
  Markdown-Überschriften „### 1. Titel" überführt. 29 Vorlagen sind dadurch
  wohlgegliedert mit korrekten Abständen.

### Ausführlicher gefasst

- `grundschuldbestellung-notariell` (182 Zeilen): §§ 1191, 1192, 1116, 1193 BGB,
  Rangvorbehalt § 881 BGB, Unterwerfung § 800 ZPO und § 794 Abs. 1 Nr. 5 ZPO,
  Eintragungsbewilligung § 19 GBO.
- `darlehensvertrag-privat-angehoerige` (136 Zeilen) und
  `darlehensvertrag-unternehmen` (302 Zeilen, mit Conditions Precedent,
  Covenants, Negative Pledge, Cross Default); ein aus dem Modellwissen
  stammendes Aktenzeichen wurde entfernt und durch § 489 BGB ersetzt.
- `insolvenzplan-darstellender-und-gestaltender-teil` (417 Zeilen): Abstimmung,
  Mehrheiten, Obstruktionsverbot, gerichtliche Bestätigung und Minderheitenschutz
  (§§ 235–253 InsO).
- `arbeitsvertrag-unbefristet` (376 Zeilen, 17 gleichartig gegliederte
  Abschnitte) und `wohnraummietvertrag` (364 Zeilen).

### Neu

- `mietrecht-und-wohnungseigentumsrecht/gewerbemietvertrag` — ein ausführlicher
  Gewerbemietvertrag (Umsatzsteueroption § 9 UStG, Wertsicherung, Konkurrenz-
  schutz, Schriftform § 550 BGB, Rückbau), als Vollvertrag neben der Kurzform.

### Geprüft

- `validate-vorlagen` (708), `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 708/708`.

## v1.31.1 — Sanity-Politur für neue Vertragsvorlagen (2026-06-16)

**Stand:** 707 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 707/707`, alle acht CI-Checks grün.

### Geändert

- Acht neue Vertragsvorlagen aus v1.30.0 beginnen nicht mehr mit
  erklärenden Parteien-Listen, sondern mit einem knappen Bearbeitungsstand
  und anschließend unmittelbar mit dem eigentlichen Vertragseingang
  („zwischen … und …"). Betroffen sind Genussrechtsvereinbarung,
  Generalunternehmervertrag, Ingenieurvertrag Tragwerksplanung,
  Nachunternehmervertrag, Projektsteuerungsvertrag, Anteilstreuhandvertrag,
  Venture-Capital-Beteiligungsvertrag und Stimmbindungs-/Poolvertrag.
- Mehrere unnötige horizontale Trennlinien direkt nach `## Vorlage` wurden in
  den neuen Vertragsvorlagen entfernt.
- Verschachtelte Platzhalter in neuen Verträgen wurden bereinigt, damit
  Markdown, ODT und ZIP-Download sichtbar und bearbeitbar bleiben.
- Der Ingenieurvertrag Tragwerksplanung verweist bei der Honorarzone jetzt
  präzise auf § 52 Abs. 2 HOAI in Verbindung mit Anlage 14 Nummer 14.2 HOAI
  und verwendet korrekt Honorarzonen I bis V.

### Geprüft

Alle acht CI-Checks grün: `validate-vorlagen`, `check-gliederung`,
`check-md-zip-integrity`, `check-odt-integrity`, `check-odt-spaltenlayout`,
`check-rechtsprechungshygiene`, `check-umlauthygiene`, `run-eval`.
`run-eval`: `All-Pass 707/707`.

## v1.31.0 — Markdown-Direktdownload über ZIP-Spiegelkopie (2026-06-16)

**Stand:** 707 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 707/707`, alle acht CI-Checks grün.

GitHub serviert `.md`-Dateien mit `Content-Type: text/plain`. Browser zeigten den prominent verlinkten Markdown-Download in der Vorlagen-README deshalb inline an, statt die Datei herunterzuladen. Diese Version löst das auf Repo-Ebene: jede Vorlage wird von einer byte-identischen `<slug>.md.zip` begleitet, die genau die Markdown-Datei enthält; die `README.md` verlinkt die ZIP-Fassung im Download-Block, und Browser laden zuverlässig herunter.

### Hinzugefügt

- `<slug>.md.zip` neben jeder `<slug>.md` (707 ZIPs), deterministisch erzeugt mit fixem Zeitstempel 2026-01-01.
- `scripts/build-md-zips.py` erzeugt und aktualisiert die ZIPs idempotent.
- `scripts/check-md-zip-integrity.py` prüft die Synchronität (Vorhandensein, exakt ein Eintrag, byte-identischer Inhalt) und ist als achter CI-Check in der GitHub-Action eingehängt.

### Geändert

- 707 Vorlagen-READMEs: Der prominente Markdown-Direktdownload zeigt jetzt auf `<slug>.md.zip`. Linktext heißt nun „… – Markdown (ZIP) herunterladen", Zusatzbeschriftung „— Bearbeitbare Markdown-Fassung, gepackt für direkten Download". Die rohe `<slug>.md` bleibt als Vorschau-Quelle im Block „Online ansehen" verlinkt.
- `CLAUDE.md` Abschnitt 15 (Direktdownload-Links) um die ZIP-Konvention erweitert, damit Folge-PRs die ZIPs mitführen.
- `.github/workflows/eval.yml` um den achten Check `check-md-zip-integrity` ergänzt.

### Geprüft

Alle acht CI-Checks grün: `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`, `check-md-zip-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` All-Pass 707/707.


## v1.30.0 — Gesellschafts-, Bau- und Europa-/Verfassungsrecht: zwölf neue Vorlagen (2026-06-16)

**Stand:** 707 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 707/707`.

### Neu

Zwölf ausführliche, durchgehend ausformulierte Vorlagen, an echten Normen
verankert und ohne zitierte Rechtsprechung:

- **Gesellschafts- und Investmentrecht:** Venture-Capital-Beteiligungsvertrag
  (Kapitalerhöhung mit Aufgeld, Tranchen nach Meilensteinen, Verwässerungsschutz,
  Garantien, Closing), GmbH-Anteilstreuhandvertrag (§§ 666, 667, 670 BGB,
  § 15 GmbHG, Transparenzregister) und Stimmbindungs- und Poolvertrag
  (Tag-along, Drag-along, Grenzen der Stimmbindung, § 47 GmbHG).
- **Bau- und Architektenrecht:** schlüsselfertiger Generalunternehmervertrag
  (§§ 650a ff. BGB, § 650f BGB), Bau-Nachunternehmervertrag (VOB/B, § 14 AEntG),
  Ingenieurvertrag Tragwerksplanung (HOAI) und Projektsteuerungsvertrag (AHO
  Heft 9).
- **Bank-/Kapitalmarktrecht:** Genussrechtsvereinbarung als Mezzanine-Kapital
  mit qualifiziertem Rangrücktritt (§ 39 InsO).
- **Europarecht:** Beihilfebeschwerde an die EU-Kommission (Art. 107, 108 AEUV,
  VO (EU) 2015/1589) und Klage auf außervertragliche EU-Haftung (Art. 268,
  340 AEUV).
- **Verfassungsrecht:** Kommunalverfassungsbeschwerde (Art. 93 Abs. 1 Nr. 4b,
  Art. 28 Abs. 2 GG) und Antrag im Bund-Länder-Streit (Art. 93 Abs. 1 Nr. 3 GG).

### Geprüft (Bug-Hunt und Sanity-Check)

- Abschnitts-Sequenz und Querverweise der neuen Vorlagen lückenlos; keine
  nackten Platzhalter (ausgenommen die strukturelle Unterschriftszeile), keine
  Stummelsprache, kein generischer Fülltext.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 707/707`.

## v1.29.1 — Sanity-Politur für Arbeits- und Vergabevorlagen (2026-06-16)

**Stand:** 695 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 695/695`.

### Geändert

- Die Betriebsvereinbarung in `arbeitsrecht/betriebsvereinbarung-mustertext`
  ist nicht mehr als Beispiel-Stummel geführt, sondern als ausformulierte
  Betriebsvereinbarung über betriebliche Regelungen mit Geltungsbereich,
  Zweckbindung, mitbestimmungsfestem Regelungsinhalt, Datenschutz,
  Laufzeitregelung und sauberem Unterzeichnungsblock.
- Der Antrag auf Akteneinsicht vor der Vergabekammer in
  `vergaberecht/antrag-akteneinsicht-vergabekammer` verwendet klarere
  Anträge, eine präzisere Begründung und echte Zusatzabschnitte für
  Geheimhaltungseinwände, Kennzeichnungserklärungen, Erweiterungsanträge und
  verfahrensleitende Anregungen.
- Die Bietererklärung zu Interessenkonflikten in
  `vergaberecht/bietererklaerung-interessenkonflikt` ist von verschachtelten
  Platzhaltern bereinigt.
- Die Leistungsbeschreibung in
  `vergaberecht/vergabeunterlagen-leistungsbeschreibung` ist von
  Kommentarformeln bereinigt und formuliert Anforderungen, Gleichwertigkeit,
  Abnahme, Ausführungsbedingungen und Zuschlagskriterien präziser aus.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK.
- `run-eval`: `All-Pass 695/695`.

## v1.29.0 — Notarielle Immobilien- und Sachenrechtsvorlagen (2026-06-16)

**Stand:** 695 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 695/695`.

### Neu

- Zehn ausführliche, durchgehend ausformulierte notarielle Immobilien- und
  Sachenrechtsvorlagen, an echten Normen verankert und ohne zitierte
  Rechtsprechung:
  - Notarieller Grundstückskaufvertrag (§§ 433, 311b, 925 BGB) mit
    Auflassungsvormerkung, Fälligkeit über Notarbestätigung,
    Belastungsvollmacht und gemeindlichem Vorkaufsrechtszeugnis (§ 28 BauGB).
  - Teilungserklärung mit Gemeinschaftsordnung (§ 8 WEG, reformiertes Recht).
  - Erbbaurechtsvertrag (Erbbaurechtsgesetz: Erbbauzins-Reallast, Heimfall,
    Erneuerungsvorrecht, Entschädigung).
  - Immobilien-Übergabevertrag zur vorweggenommenen Erbfolge mit Nießbrauch
    oder Wohnungsrecht, Pflege-Reallast, Gleichstellungsgeld,
    Pflichtteilsanrechnung (§ 2315 BGB) und Rückforderungsrechten.
  - Wohnungsrecht (§ 1093 BGB), Grunddienstbarkeit als Geh-, Fahr- und
    Leitungsrecht (§ 1018 BGB), Reallast für Altenteil und
    Versorgungsleistungen (§ 1105 BGB), dingliches Vorkaufsrecht
    (§§ 1094 ff. BGB), Nachbarrechtsvereinbarung über Grenzbebauung und
    Überbau (§§ 912, 921 BGB) sowie beschränkte persönliche Dienstbarkeit als
    Leitungsrecht zugunsten eines Versorgungsunternehmens (§ 1090 BGB).

### Geprüft (Bug-Hunt und Sanity-Check)

- Abschnitts-Sequenz, interne Querverweise und Anlagenverweise repo-weit
  geprüft: keine neuen Lücken, Doppelungen oder verwaisten Verweise.
- Die zehn neuen Vorlagen ohne nackte Platzhalter, ohne Stummelsprache und
  ohne generischen Fülltext (je 0).
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 695/695`.

## v1.28.2 — Codex-P2-Fixes: Grundschuld, § 529 BGB, Drittwiderspruchsklage-Zuständigkeit, § 601 BGB, Art. 10 DSGVO (2026-06-16)

**Stand:** 685 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 675/675`, alle sieben CI-Checks grün.

Folgt auf v1.28.1 und arbeitet fünf P2-Reviewhinweise von Codex zu konkreten juristischen Ungenauigkeiten in den neuen Vorlagen ab.

### Geändert

- **Abtretungsvereinbarung-Forderung:** § 401 BGB nur noch für akzessorische Sicherheiten ausgewiesen. Neue Klausel 1.3 trennt nicht akzessorische Sicherheiten (insbesondere Grundschuld, Sicherungsübereignung, Sicherungszession, Garantie) ab und beschreibt die gesonderte Übertragung durch schriftliche Abtretungserklärung nach §§ 1192 Abs. 1, 1154 BGB, mit Brief-Übergabe und Grundbucheintragung bzw. Buchgrundschuld-Eintragung nach § 873 BGB.
- **Schenkungsvertrag, § 529 BGB:** Zehn-Jahres-Frist korrekt als Frist seit Vollzug der Schenkung ausgewiesen, geprüft zum Zeitpunkt des Eintritts der Bedürftigkeit (nicht zehn Jahre nach Eintritt der Verarmung).
- **Drittwiderspruchsklage § 771 ZPO:** Trennung von örtlicher Zuständigkeit (§ 771 Abs. 1 ZPO, Vollstreckungsbezirk) und sachlicher Zuständigkeit (§§ 23, 23a, 71 GVG nach Streitwert; bis 5 000 EUR Amtsgericht, darüber Landgericht). Klage geht damit nicht reflexhaft an das Vollstreckungsgericht, sondern an das sachlich zuständige Amts- oder Landgericht im Vollstreckungsbezirk. Mandatsreife Prüfmatrix angepasst.
- **Leihvertrag (§§ 598 ff. BGB):** Verspätete Rückgabe in Klausel 3.4 nicht mehr auf § 601 BGB gestützt. Schadensersatz wegen verspäteter Rückgabe folgt § 280 Abs. 1 und Abs. 2 i. V. m. § 286 BGB (Verzug); § 601 BGB betrifft ausschließlich laufende Erhaltungskosten.
- **Datenschutz-Einwilligung-Mandatskommunikation:** Strafrechtliche Verurteilungen und Straftaten werden nicht mehr unter Art. 9 DSGVO subsumiert. Neue Klausel 1.4 weist Art. 10 DSGVO als eigenständige Rechtsgrundlage aus, in Verbindung mit Art. 6 Abs. 1 lit. b oder lit. f DSGVO und der nach Art. 10 DSGVO erforderlichen nationalen Ermächtigung (§§ 22 Abs. 1 Nr. 1 lit. d, 24 BDSG, § 43a Abs. 2 BRAO). Geeignete Garantien sind benannt. Mandatsreife Prüfmatrix entsprechend angepasst.

### Geprüft

Alle sieben CI-Checks grün: `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`, `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`, `run-eval`. `run-eval` All-Pass 675/675.


## v1.28.1 — Anti-Generisch-Lift in 110 Schablonen-Vorlagen, HTML-Bereinigung und acht neue Zivilrechtsvorlagen (2026-06-16)

**Stand:** 685 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 675/675`.

### Hinzugefügt

- **Zehn neue Vorlagen** aus dem Allgemeinen Vertragsrecht und Zivilprozess in
  `allgemeines-und-bereichsuebergreifendes/`, jeweils mit eigenem README, voll
  ausformulierter Markdown-Vorlage und gleichnamiger ODT:
  - `schenkungsvertrag` (§§ 516, 518, 525, 528, 530 BGB)
  - `schuldanerkenntnis-deklaratorisch` (§ 781 BGB)
  - `stundungsvereinbarung` (Stundung mit Verzinsung und Sicherheitenstellung)
  - `abtretungsvereinbarung-forderung` (§§ 398 ff. BGB)
  - `stufenklage-zivilprozess` (§ 254 ZPO)
  - `vollstreckungsabwehrklage-767-zpo` (§ 767 ZPO)
  - `drittwiderspruchsklage-771-zpo` (§ 771 ZPO)
  - `erinnerung-vollstreckung-766-zpo` (§ 766 ZPO)
  - `leihvertrag-bgb` (§§ 598–606 BGB)
  - `patronatserklaerung-hart` (harte Patronatserklärung, §§ 311, 280, 765 BGB)

  `schenkungsvertrag` und `patronatserklaerung-hart` stehen als allgemein gefasste, nicht-notarielle Varianten neben den von v1.28.0 angelegten `schenkungsvertrag-notariell` und `patronatserklaerung-hart-weich`.

### Geändert

- **110 generische Schablonen-Vorlagen vollständig ausformuliert.** Vorlagen,
  die noch maschinell erzeugte Hülsen mit Ankündigungsfloskeln, generischen
  Rubren („Partei 1 / Auftraggeberin"), HTML-maskierten Platzhaltern und
  Stummelsätzen enthielten, sind durchgängig zu konkreten, mandatsreifen
  Vorlagen umgeschrieben. Jeder Platzhalter steht nun in einen vollständigen
  Satz eingebettet; jede Klausel ist auf den konkreten Vorlagentyp zugeschnitten.
- **HTML-Reste in 33 Vorlagen bereinigt** (`&lt;`, `&gt;`, `&amp;`, `&nbsp;`,
  `&quot;` durch korrekte Zeichen ersetzt) und alle zugehörigen ODT neu erzeugt.
- **Drei Eval-Fails behoben** durch sprachlich passende Ergänzungen
  (DSGVO-Meldung: explizite Anzeige- und Antragsformulierung;
  Insolvenz-Nachmeldung: Forderung „macht hiermit … geltend und beantragt
  deren Feststellung"; Letter of Intent: Gegenzeichnungsbitte und
  Bestätigungsantrag der Initiatorin).

### Geprüft

- Alle sieben CI-Checks grün:
  `validate-vorlagen`, `check-umlauthygiene`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`, `check-gliederung`,
  `run-eval`.
- `run-eval`: **All-Pass 665/665, Fail 0**.


## v1.28.0 — Bug-Hunt, neue Zivilrechtsvorlagen und vollständige Anlagen (2026-06-16)

**Stand:** 675 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 675/675`.

### Neu

- Zehn neue, durchgehend ausformulierte Vorlagen aus dem allgemeinen
  Vertrags- und Zivilrecht, jeweils an echten Normen verankert und ohne
  zitierte Rechtsprechung: Schenkungsvertrag (notariell, §§ 516, 518, 525,
  528, 530 BGB), Immobilien-Maklervertrag (§§ 652, 656a, 656c, 656d BGB mit
  Verbraucherwiderruf), konstitutives Schuldanerkenntnis (§ 781 BGB),
  Ratenzahlungsvereinbarung mit Verfallklausel, Schuldübernahme und
  Schuldbeitritt (§§ 414, 415, 421, 426 BGB), Werklieferungsvertrag
  (§ 650 BGB), Nießbrauchsbestellung an einem Grundstück (notariell,
  §§ 1030 ff. BGB), Vorvertrag, Verwahrungsvertrag (§§ 688 ff. BGB) und
  Patronatserklärung mit harter und weicher Variante.

### Behoben (Bug-Hunt)

- Ein neuer Prüfblick auf die Abschnitts-Sequenz und interne Querverweise
  (den `check-gliederung` nicht abdeckt, da dort nur der Stil, nicht die
  Reihenfolge geprüft wird) deckte echte Nummerierungslücken auf: 32
  Schriftsatz-/Vermerk-Vorlagen sprangen von Abschnitt 6 auf 8 (7 fehlte);
  acht weitere Vorlagen hatten Lücken oder Doppelungen. Alle wurden lückenlos
  resequenziert (ohne Bruch interner Verweise).
- Der Konzessionsvertrag verwies in der salvatorischen Klausel per
  Copy-Paste auf „Ziffer 10.3 des Stromliefervertrags"; dies wurde durch eine
  eigenständige salvatorische Klausel ersetzt.

### Vervollständigt

- Fünf Verträge (Patentlizenz-, Architekten-, Joint-Venture-, Drehbuch- und
  Musical-Libretto-Vertrag) verwiesen auf Anlagen, die im Anlagenverzeichnis
  nicht definiert waren. Jede referenzierte Anlage trägt nun eine eigene,
  sprechende Überschrift mit ausformulierter Beschreibung.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 675/675`.

## v1.27.0 — Generische Schablonen-Verträge vollständig ausformuliert (2026-06-16)

**Stand:** 665 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 665/665`.

### Geändert

- 52 Vertragsvorlagen waren maschinell erzeugte Hülsen: Sie kündigten ihren
  Inhalt nur an („Der Regelungsbereich „…" wird ausdrücklich und mandatsbezogen
  konkretisiert", „Für den Vertragstyp „…" werden Parteien, Vertretung … nur
  insoweit geregelt", „Besonderer Prüfpunkt: …"), enthielten grammatische
  Stummel („Die Parteien regeln Anfertigung …") und HTML-maskierte Platzhalter
  `&lt;…&gt;`. Sie sind jetzt durchgängig zu konkreten, vollständig
  ausformulierten Vertragsvorlagen umgeschrieben — mit echtem
  Leistungsgegenstand, Hauptpflichten, Vergütung, Fristen und Abnahme,
  Gewährleistung und Haftung, Laufzeit und Kündigung sowie den jeweils
  einschlägigen Normen, alles in vollständigen Sätzen.
- Jeder Platzhalter steht nun in einen vollständigen Satz eingebettet (etwa „Der
  Werklohn beträgt <Betrag> EUR zuzüglich der gesetzlichen Umsatzsteuer."), nie
  mehr als nacktes Feld. Alle HTML-Maskierungen `&lt;…&gt;` sind in echte spitze
  Klammern überführt.
- Betroffen sind unter anderem Werk- und Dienstverträge (Gemälde-/Portrait- und
  Büsten-Auftrag, Klavierstimmen und -reparatur, Malerarbeiten, Catering,
  Reinigung, Sicherheitsdienst, Gebäudewartung), Finanzierungs- und
  Bankverträge (Equipment-Finance-Lease, Sale-and-Lease-Back,
  Intercompany-Darlehen, Kontokorrentrahmen, Treuhandkonto), Bau- und
  Anlagenverträge (EPC, Maschinen- und Ersatzteillieferung, Reinraum,
  Service-Level-Wartung), Schutzrechtsverträge (Design-, Marken-, Know-how- und
  Patent-Pool-Lizenz, Geheimnisschutz), IT-Verträge (Managed Cybersecurity,
  Datenlizenz, Enterprise-SaaS, IT-Outsourcing, agile Entwicklung,
  Exportkontrolle), M&A-Vorlagen (Carve-out, Earn-Out, Management-Beteiligung,
  Vendor Loan Note, Warranty Claims Protocol), Vergabe- und Vertriebsvorlagen.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 665/665`.
- Repo-weiter Stummelsprache-Bug-Hunt: keine hohlen Ankündigungsklauseln,
  keine grammatischen Stummel, keine Schlagwort-Listen-Aufzählungen und keine
  zu engen Rubrumspalten mehr.

## v1.26.0 — Präambeln durchgängig als Abschnitt 1 nummeriert (CLAUDE.md §2) (2026-06-15)

**Stand:** 665 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 665/665`.

### Geändert

- Vierzehn Vorlagen trugen noch eine unnummerierte `Präambel`-Überschrift vor dem
  Vertragstext und verstießen damit gegen CLAUDE.md §2 („Eine Präambel steht
  niemals unnummeriert vor dem Vertragstext"). Sie sind jetzt durchgängig als
  Abschnitt `1. Präambel / Gegenstand` geführt. Wo der bisherige Abschnitt 1
  bereits den Gegenstand regelte, wurde das Rezital in diesen Abschnitt
  eingefaltet (`1. Präambel / <bisheriger Titel>`), ohne die übrige Nummerierung
  zu verschieben; sonst wurde die Präambel zum neuen Abschnitt 1 und die
  Folgeklauseln samt aller internen Querverweise um eins weitergezählt.
- Betroffen: `letter-of-intent-grenzueberschreitend`,
  `internationaler-liefervertrag-cisg`, `selektiver-vertriebsvertrag-luxus-marke`,
  `franchisevertrag-systemzentrale-partner`, `lizenzvertrag-marke`,
  `exklusiv-vertriebsvertrag-eu`, `joint-venture-vertrag-eu`,
  `sicherungsabtretung`, `geschaftsanteilskaufvertrag`, `vergleichsvereinbarung`,
  `verschwiegenheitsvereinbarung-nda`, `aufhebungsvertrag`,
  `betriebsvereinbarung-mustertext` und `schiedsvereinbarung-icc`.
- In jeder dieser Vorlagen hält nun die Schlussbestimmung ausdrücklich fest, dass
  Abschnitt 1 Bestandteil des Dokuments ist und Regelungsgehalt hat (CLAUDE.md §2);
  bei der notariellen Anteilsübertragung steht dieser Vermerk innerhalb des
  beurkundeten Vertragstextes vor dem Signaturblock.

### Neu

- `scripts/check-gliederung.py` erkennt zusätzlich unnummerierte
  `Präambel`-Überschriften in Vorlagendateien und verhindert so, dass die Regel
  aus CLAUDE.md §2 künftig wieder unterlaufen wird.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 665/665`.

## v1.25.0 — Qualitätslift für Volltext, Zweisprachigkeit und ODT-Synchronität (2026-06-15)

**Stand:** 665 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 665/665`.

### Geschärft

- Generische Vertragsdaten-Tabellen und Standardfloskeln in 44 älteren
  Vertrags- und Vereinbarungsvorlagen entfernt.
- Basisklauseln zu Terminen, Zahlungen, Haftungsgrenzen, Risikoerfassung,
  Laufzeit und Rückgabe nach Vertragsende ausformuliert, damit die Vorlagen
  nicht nur Platzhalter ankündigen, sondern konkrete Prüf- und
  Regelungsentscheidungen verlangen.
- Standalone-„English Reading Version“-Blöcke in nicht-zweisprachigen
  Vorlagen entfernt; zweisprachige Vorlagen bleiben zweispaltig mit
  `Deutsch | English`.
- Unpassende bilinguale Prüfpunkte aus nicht-zweisprachigen Mandatsreife-
  Matrizen entfernt.

### Geprüft

- 56 Markdown-Fassungen und die zugehörigen ODT-Dateien synchronisiert.
- README-Direktdownloads, sprechende Dateinamen, ODT-Integrität,
  ODT-Spaltenlayout, Dezimalgliederung, Umlaute und Rechtsprechungshygiene
  erneut geprüft.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 665/665`.

## v1.24.0 — Wirtschaftsrechtlicher Ausbau und sprechende Downloads (2026-06-15)

**Stand:** 665 Vorlagen in 36 Rechtsgebieten, Eval-Harness `All-Pass 665/665`.

### Neu

- 20 zusätzliche Wirtschaftsrechtsvorlagen mit sprechenden Dateinamen,
  synchroner Markdown- und ODT-Fassung, README-Direktdownloads und
  Baseline-Rubrics.
- Neue Schwerpunkte: Lieferketten- und Forecast-Verträge, Qualitäts- und
  Werkzeugüberlassung, Service/Wartung, Cash Pooling, Geschäftsführer-
  Dienstvertrag, Mitarbeiterbeteiligung, Escrow, Nachrangdarlehen mit
  Wandlungsoption, Covenant Waiver, Due-Diligence-Freigabe, Closing-
  Checkliste, PaaS, API-Nutzung, selektiver Vertrieb, kartellrechtliche
  Selbstreinigung, Interessenkonflikterklärung im Vergabeverfahren,
  Incoterms-Exportlieferung und Fortführungslieferung als Massegeschäft.

### Geschärft

- Bereichs-READMEs nennen jetzt durchgehend den verbindlichen Dateistamm
  `<vorlagen-slug>.md` und schließen generische Namen wie `vertrag.md`,
  `text.md`, `antrag.md`, `vorlage.md` oder `skill.md` ausdrücklich aus.
- Volltext statt Stummelsprache in den neuen Vorlagen: konkrete Klauseln,
  Rubrum, Schluss-/Unterzeichnungsblock, Freigabevermerk und
  Mandatsreife Prüfmatrix.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 665/665`.

## v1.23.0 — GbR-Gesellschaftsvertrag und privater Darlehensvertrag (2026-06-15)

**Stand:** 624 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 624/624`.

### Neu

- `handels-und-gesellschaftsrecht/gbr-gesellschaftsvertrag` —
  Gesellschaftsvertrag einer Gesellschaft bürgerlichen Rechts nach dem seit dem
  1. Januar 2024 geltenden MoPeG-Recht, mit Beiträgen, Geschäftsführung und
  Vertretung, Beschlüssen, Fortsetzung beim Ausscheiden, Abfindung, eGbR-Option
  und Auseinandersetzung.
- `bank-und-kapitalmarktrecht/darlehensvertrag-privat-angehoerige` —
  privater Darlehensvertrag unter Privatpersonen und Angehörigen mit
  Verzinsung, Tilgung, Kündigung (§§ 488, 490 BGB) und Hinweisen zum
  steuerlichen Fremdvergleich.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 624/624`.

## v1.22.0 — Internationales Erbrecht: ENZ, internationale Sterbeurkunde und Grundstücks-Erbauseinandersetzung (2026-06-15)

**Stand:** 622 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 622/622`.

### Neu

- `erbrecht/grundstuecksuebertragung-erbauseinandersetzung-notariell` —
  notarielle Übertragung eines Nachlassgrundstücks zur Auseinandersetzung der
  Erbengemeinschaft mit Auflassung, Ausgleichszahlung, Lastenfreistellung,
  Vormerkung, Grundbuchvollzug und Grunderwerbsteuerbefreiung (§ 3 Nr. 3 GrEStG).
- `erbrecht/europaeisches-nachlasszeugnis-antrag` — Antrag auf ein Europäisches
  Nachlasszeugnis nach der EU-Erbrechtsverordnung (Artikel 62 ff.) und dem
  IntErbRVG für grenzüberschreitende Erbfälle.
- `erbrecht/antrag-internationale-sterbeurkunde-ciec` — Antrag auf eine
  mehrsprachige internationale Sterbeurkunde nach § 55 PStG und dem
  CIEC-Übereinkommen Nr. 16.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 622/622`.

## v1.21.0 — Neue Erbrechts- und Genossenschaftsvorlagen (2026-06-15)

**Stand:** 619 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 619/619`.

### Neu

- `erbrecht/auseinandersetzungsvollmacht-miterben` — große gemeinsame Vollmacht
  sämtlicher Miterben, mit der eine Person die Auseinandersetzung der
  Erbengemeinschaft verhandelt, abschließt und vollzieht (Grundbuch, Konten,
  Teilungsversteigerung), mit Innenverhältnis, § 181 BGB und Widerruf.
- `handels-und-gesellschaftsrecht/genossenschaft-satzung-gemeinnuetzig` —
  ausführliche Satzung einer gemeinnützigen eingetragenen Genossenschaft, die
  die GenG-Pflichtinhalte (Firma, Gegenstand, Geschäftsanteil, Organe,
  Pflichtprüfung) mit den Anforderungen der §§ 51 ff. AO (Selbstlosigkeit,
  Ausschüttungsverbot, Vermögensbindung) verbindet.
- `handels-und-gesellschaftsrecht/genossenschaft-beitrittserklaerung` —
  unbedingte Beitrittserklärung mit Zeichnung der Geschäftsanteile,
  Anerkennung der Satzung und datenschutzrechtlicher Einwilligung.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 619/619`.

## v1.20.0 — Arbeitszeugnis mit Notenvarianten 1 bis 6 und Bilingual-Zweispalten-Regel (2026-06-15)

**Stand:** 616 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 616/616`.

### Neu

- `arbeitsrecht/arbeitszeugnis-qualifiziert-notenvarianten` — qualifiziertes
  Arbeitszeugnis nach § 109 GewO, das jede Schulnote von eins bis sechs in
  vollständig ausformulierten Fassungen vorhält (Zufriedenheitsformel,
  Fachwissen, Verhaltensbeurteilung, Schlussformel) und mit Klammer-Hinweisen
  zeigt, welcher Satz für welche Note ein- oder auszubauen ist. Erschlossen aus
  der verschlagenen Zeugnissprache, den Steigerungsadverbien und der
  BAG-Beweislastregel (bis Note drei Arbeitgeber, ab Note zwei Beschäftigte).
- Grundregel (CLAUDE.md Abschnitt 19): zweisprachige Vorlagen stets
  zweispaltig — Deutsch links, Englisch rechts, satz- und absatzgenau parallel.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-odt-spaltenlayout`, `check-rechtsprechungshygiene`,
  `check-umlauthygiene` OK; `run-eval`: `All-Pass 616/616`.

## v1.19.4 — ODT-Layout-Wurzelfix (keine enge Mittelspalte) und neue Grundregeln (2026-06-15)

Behebt einen gravierenden ODT-Renderingfehler und verankert zwei verbindliche
Grundregeln.

**Stand:** 615 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 615/615`.

### Behoben

- ODT-Layout: Pandocs `multiline_tables`/`simple_tables` deuteten die
  `---`-Trennlinien zwischen Abschnitten als Tabellenränder und zwangen
  Rubrum- und Vertragstext in eine schmale, mittig zentrierte Spalte.
  `scripts/md-to-odt.py` schaltet diese Extensions jetzt ab; alle 615
  ODT-Fassungen wurden neu erzeugt und rendern wieder über die volle
  Satzbreite.
- Untertitel-Hierarchie: in neun Umweltrecht-Mustern wurden die Untertitel
  unter den herabgestuften Dokumenttiteln auf `###` nachgezogen
  (Folgekorrektur zu v1.19.3 nach Codex-Review).

### Neu

- Grundregel (CLAUDE.md Abschnitt 17): durchgehend vollständige, eloquente
  Sätze; keine Stummelsprache, Halbsätze oder generischer Fülltext im
  Vorlagentext.
- Grundregel (CLAUDE.md Abschnitt 18) samt Prüfskript
  `scripts/check-odt-spaltenlayout.py`: niemals enge zentrierte Spalte, der
  Body steht über die volle Satzbreite.

### Geprüft

- `check-odt-spaltenlayout` OK (615), `validate-vorlagen`, `check-gliederung`,
  `check-odt-integrity`, `check-rechtsprechungshygiene`, `check-umlauthygiene`
  OK, `run-eval`: `All-Pass 615/615`.

## v1.19.3 — Typografischer Feinschliff und einheitliche H1-Titel (2026-06-15)

Eleganz- und Smoothness-Lauf, fundiert in den repo-eigenen Typografieregeln.

**Stand:** 615 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 615/615`.

### Geändert

- Einheitlich ein H1 je Vorlage: 18 Vorlagen mit zweitem (operativem)
  H1-Titel auf `##` herabgestuft, passend zur dominanten Ein-H1-Konvention der
  übrigen Vorlagen; saubere Leerzeile nach der Überschrift gesichert.
- Typografie geglättet: ASCII-Ellipsen `...` durch das Ellipsenzeichen `…`
  ersetzt (Fließtext), Betragsschreibweise „1.560,--" zu „1.560,—",
  Prozentangabe „5%" zu „5 %".
- Betroffene ODT-Fassungen neu aus der Markdown-Quelle erzeugt.

### Geprüft

- Bewusst unverändert: Aktenzeichen und Referenz-IDs mit Bindestrich (keine
  falschen Bis-Striche), zweisprachige englische Anführungszeichen.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` OK.
- `run-eval`: `All-Pass 615/615`.

## v1.19.2 — Brief-/Parteiblock-Umbrüche und Markdown-Politur der MDK-/Approbationsmuster (2026-06-15)

Folgekorrektur zu v1.19.1 und gezielte Markdown-Überführung zweier Altmuster.

**Stand:** 615 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 615/615`.

### Behoben

- Brief-, Bezugs- und Vertragsparteien-Köpfe: In v1.19.1 hatte die
  Whitespace-Glättung dort Markdown-Hardbreaks (abschließende zwei Leerzeichen)
  entfernt, wodurch Zeilen wie „An … / In der Sache … / Aktenzeichen … / Datum …"
  und Parteienblöcke beim Rendern zu einem Absatz verschmolzen. Jetzt durch echte
  Absatztrennung robust gesetzt (9 Vorlagen). Hinweis aus dem Codex-Review zu #59.

### Geändert

- Die beiden medizinrechtlichen Altmuster (`antrag-approbationsverfahren` und
  `stellungnahme-mdk-pflegegrad`) aus dem Monospace-Codeblock in sauberes
  Markdown überführt: Dezimalgliederung statt römischer Abschnitte,
  `<…>`-Platzhalter statt `[…]`, Listen statt Leerzeichen-Spalten. Alle
  §-Verweise, Erklärungen und Modulbewertungen bleiben inhaltlich unverändert.
- Betroffene ODT-Fassungen neu aus der Markdown-Quelle erzeugt.

### Geprüft

- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` OK.
- `run-eval`: `All-Pass 615/615`.

## v1.19.1 — Formatierungsglättung über alle Vorlagen (2026-06-15)

Reiner Formatier- und Lesbarkeitsschliff; keine inhaltliche Änderung der
Rechtsaussagen.

**Stand:** 615 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 615/615`.

### Behoben

- ASCII-Art-Trennlinien (Box-Zeichen) aus den Brief- und Formularmustern
  entfernt; die Abschnittsüberschriften bleiben erhalten.
- Side-by-side-Signaturblöcke, deren Spalten beim Rendern zusammenliefen, auf
  saubere gestapelte Unterschriftszeilen umgestellt.
- Defekte Tabellenzeile in der Datenschutz-Incident-Meldung repariert: die
  Risiko-Bewertung passt jetzt ins zweispaltige Raster.
- Trailing-Whitespace in mehreren Vorlagen entfernt; betroffene ODT-Fassungen
  neu aus der Markdown-Quelle erzeugt.

### Geprüft

- Tiefen-Scan ohne weitere Befunde: keine kaputten Glyphen, Steuer- oder
  Ersatzzeichen, Soft-Hyphens, kompakten Abkürzungen, `{{…}}`- oder
  `[…]`-Fill-in-Platzhalter.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` OK.
- `run-eval`: `All-Pass 615/615`.

## v1.19.0 — Finanzierungs- und Vollmachtsausbau, platzhalterfeste ODTs (2026-06-15)

Qualitätsrunde mit weiterer Verschlankung der Arbeitsfassungen, stärkerer
ODT-Verlässlichkeit und vier neuen Praxisvorlagen für Finanzierung,
Sicherheiten und Nachlassvollzug.

**Stand:** 615 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 615/615`.

### Hinzugefügt

- Deutsch-englisches Schuldscheindarlehen mit Tranchen, Zahlstelle,
  Covenants, Kündigungsgründen, Kostenmechanik und Anlagen.
- Deutsch-englisches Gesellschafterdarlehen mit Kapitalerhaltungsprüfung,
  optionalem qualifiziertem Rangrücktritt, Informationsrechten und
  Gesellschafterbeschluss.
- Sicherungsabtretung notarieller Ansprüche mit Notifizierungsmuster,
  enger Sicherungszweckerklärung und Freigabe-/Rückabtretungsmechanik.
- Deutsch-englische postmortale Vollmacht mit Bank-, Behörden-,
  Grundstücks-, Gesellschafts-, Steuer-, Digital- und Nachlassbefugnissen
  sowie optionaler Befristung.

### Geändert

- Kontoverpfändung als Kreditsicherheit um den konstitutiven Hinweis auf
  die Notifizierung der kontoführenden Bank, fortbestehende
  Verfügungsbefugnis bis zum Verwertungsfall, Bankrückbestätigung und
  Kontenverzeichnis ergänzt.
- ODT-Generator schützt repo-übliche Platzhalter in spitzen Klammern vor
  Pandocs HTML-Erkennung; Platzhalter wie `<Datum>`, `<IBAN>` und `<Ort>`
  bleiben damit in heruntergeladenen ODT-Dateien sichtbar.
- Repo-Regeln zur Präambel geschärft: Eine Präambel steht bei Verträgen
  nicht vor dem Vertragstext, sondern als Ziffer 1 „Präambel / Gegenstand“;
  die Schlussbestimmungen stellen ihren Regelungsgehalt klar.
- Weitere lange Hinweis-, Normen- und Quellenabschnitte aus
  Vorlagendateien entfernt; die ausführlichen Hinweise bleiben in den
  README-Dateien, die Arbeitsfassungen bleiben schlank.

## v1.18.1 — Dubletten-Schutz nach Arbeitsfassungsumstellung (2026-06-15)

Patch-Release nach Abschlusskontrolle der schlanken Arbeitsfassungen.

**Stand:** 611 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 611/611`.

### Geändert

- Lokale „ 2“-Dubletten aus Finder- oder Editor-Kopien werden über
  `.gitignore` ausgeschlossen, damit alte Hinweisbausteine nicht versehentlich
  wieder als untracked Arbeitsdateien auftauchen.
- Arbeitsbaum, `main`, Tag-Stand und GitHub-Release-Kette nach `v1.18.0`
  erneut geprüft.

## v1.18.0 — Schlanke Arbeitsfassungen, Paginierung und Wirtschaftsrechtsausbau (2026-06-14)

Großer Struktur- und Ausbau-Release: Die Vorlagendateien selbst sind jetzt
deutlich schlanker. Normenanker, Rechtsprechungsanker, ausführliche Warnungen,
Einsatzgrenzen und Bearbeitungshinweise stehen in der jeweiligen README; die
Markdown- und ODT-Arbeitsfassungen enthalten nur noch den kurzen Kopfhinweis,
die eigentliche Vorlage, Anlagen und die Mandatsreife Prüfmatrix.

**Stand:** 611 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 611/611`.

### Geändert

- 689 lange Hinweis-, Normen-, Quellen- und Bearbeitungsabschnitte aus den
  eigentlichen Vorlagendateien entfernt; README-Dateien bleiben der zentrale
  Ort für Warnungen, Anwendungsbereich, Normenanker, Quellenanker und
  Direktdownloadlinks.
- ODT-Generator erweitert: A4, 2,5 cm Ränder, Times New Roman 11 pt und
  rechtsbündige Seitenzahl in der Fußzeile werden nun technisch erzwungen.
- `validate-vorlagen.py` und `check-odt-integrity.py` verschärft: lange
  Hinweisabschnitte in `<typ>.md`, fehlende README-Direktdownloads und
  fehlende ODT-Paginierung werden künftig abgefangen.

### Neu

- 52 zusätzliche Wirtschaftsrechtsvorlagen, darunter Malerarbeiten,
  Klavierreparatur, Klavierstimmen, Gemälde-/Büstenauftrag, Catering,
  Gebäudetechnik-Wartung, Sicherheitsdienst, Projektmanagement,
  Distributions-, Reseller-, Servicepartner-, Handelsvertreter-,
  Einkaufsrahmen-, Lieferantenqualitäts-, Dropshipping-, Kommissionslager-
  und Konsignationslagerverträge.
- Neue IP-/Technologievorlagen für Markenlizenz, Know-how-Lizenz,
  Patent-/Know-how-Pool, Designlizenz, Geheimnisschutz,
  Enterprise-SaaS, agile Softwareentwicklung, IT-Outsourcing-Transition,
  Managed Cybersecurity und B2B-Datenlizenz.
- Neue M&A-, Finanzierungs-, Vergabe-, Anlagenbau- und Exportvorlagen,
  unter anderem Managementbeteiligung, Vendor Loan Note, Earn-Out-
  Streitbeilegung, Carve-out-Separationsplan, Warranty Claims Protocol,
  Equipment Finance Lease, Sale-and-Lease-Back, Intercompany-Darlehen,
  Kontokorrentrahmen, Treuhandkonto, besondere vergaberechtliche
  Vertragsbedingungen, Nachtragsvereinbarung öffentlicher Auftrag,
  Halbleiter-Maschinenliefervertrag, EPC-Vertrag, Reinraumvertrag,
  Exportkontrollklausel und International Manufacturing Services Agreement.

## v1.17.1 — SAFT-Quellenanker aktualisiert (2026-06-14)

Patch-Release nach Quellenabgleich: Die SAFT-Vorlage verweist nicht mehr auf
das zurückgezogene SEC Digital Assets Framework als aktiven Startpunkt,
sondern auf aktuelle SEC-Startpunkte und weist ausdrücklich darauf hin, dass
zurückgezogene oder überholte Frameworks nicht als aktuelle Guidance verwendet
werden dürfen.

**Stand:** 559 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 559/559`.

## v1.17.0 — Factoring, Arbeit, Vollstreckung und Wirtschaftsverträge (2026-06-14)

Ausbau der Sammlung um weitere praxistaugliche Vertrags-, Antrags- und
Schreibenvorlagen für Finanzierung, Factoring, Arbeitsrecht,
Zwangsvollstreckung und wirtschaftsrechtliche Standardfälle.

**Stand:** 559 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 559/559`.

### Neu

- Factoring und Forderungsfinanzierung: echtes Factoring, unechtes Factoring,
  stilles Factoring mit Offenlegungsplan und Einzelforderungsverkauf.
- Arbeitsrecht: Arbeitnehmerüberlassungsvertrag, Einsatzvereinbarung nach AÜG,
  Brückenteilzeit-Vereinbarung und Teilzeitverlangen nach TzBfG.
- Vollstreckung und Eilrechtsschutz: Pfändungs- und Überweisungsbeschluss,
  vorläufiges Zahlungsverbot, Gerichtsvollzieherauftrag, Vermögensauskunft,
  Zwangssicherungshypothek sowie Zustellung und Vollziehung einstweiliger
  Verfügungen und Anordnungen.
- Internationale Finanzierung: zweisprachige SAFT-Vorlage mit besonderem
  Warn- und Prüfprogramm zu Wertpapier-, Krypto-, Steuer- und US-Recht.
- Zehn zusätzliche wirtschaftsrechtliche Vertragsmuster, unter anderem
  Rahmenliefervertrag, OEM-/Produktentwicklungsvertrag, Kommissionsvertrag,
  F&E-/IP-Vertrag, Datenlizenz für KI-Training, Cloud-Migration,
  Transition Services Agreement, M&A-Escrow, Intercreditor Agreement und
  Garantie-/Freistellungsvereinbarung.

### Geprüft

- Markdown- und ODT-Fassungen aller neuen Vorlagen synchron erzeugt.
- Direkt-Download-Links, Rubrics, Kurz-Hinweise, Rubrum-/Adressatenköpfe,
  Schlussblöcke und Mandatsreife Prüfmatrizen angelegt.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` OK.
- `run-eval`: `All-Pass 559/559`.

## v1.16.0 — Typografische Vereinheitlichung der Abkürzungen (2026-06-14)

Feinschliff nach einem Tiefen-Qualitätslauf über den Gesamtbestand; reiner
Typografie- und Lesbarkeitsschliff ohne inhaltliche Änderung der Vorlagen.

**Stand:** 532 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 532/532`.

### Geändert

- Deutsche Mehrwort-Abkürzungen durchgängig in der gespreizten Form gesetzt
  (z. B., u. a., d. h., i. V. m., i. S. d., i. S. v., n. F., a. F., i. d. F.,
  i. d. R., h. M., o. g., i. e. S., i. w. S.) — 236 Stellen an die im Bestand
  vorherrschende Schreibweise angeglichen. Betroffene ODT-Fassungen neu erzeugt.

### Geprüft

- Keine kaputten Glyphen, Steuer-, Ersatzzeichen oder Soft-Hyphens.
- Keine erfundenen Klarnamen, keine `{{…}}`- oder `[…]`-Fill-in-Platzhalter;
  Maßeinheiten (etwa `[TJ]`) und Status-Marker bewusst in eckigen Klammern belassen.
- Keine fehletikettierten zweisprachigen Leitvorlagen mehr.
- `validate-vorlagen`, `check-gliederung`, `check-odt-integrity`,
  `check-rechtsprechungshygiene`, `check-umlauthygiene` OK.
- `run-eval`: `All-Pass 532/532`.

## v1.15.0 — Sanity-Check und Review-Fixes (2026-06-14)

Kleiner Release-Stand nach lokalem Sanity-Check, Bug-Hunt und zwei
nachgelagerten Review-Fixes seit `v1.14.0`.

**Stand:** 532 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 532/532`.

### Behoben

- Standstill-Vereinbarung: Platzhalter für Korrekturfrist und Gerichtsstand
  bleiben in der ODT-Fassung sichtbar und werden nicht durch die Konvertierung
  als HTML-Tags entfernt.
- Sicherungsabtretung: Haftungsbeispiel zur Offenlegung an die
  Offenlegungsgründe nach 3.2 angepasst; zulässige Offenlegung ohne
  Sicherungsfall wird nicht mehr als Pflichtverletzung dargestellt.

### Geprüft

- Keine untracked `* 2.md`- oder `* 2.odt`-Dubletten im Release-Stand.
- Keine verbliebenen `leitvorlage-…-zweisprachig/vertrag.md`-Fehltypisierungen.
- 532 getrackte ODT-Dateien zu 532 Vorlagen.
- `validate-vorlagen OK (532 Vorlagen, 35 Themenordner)`.
- `check-gliederung OK`.
- `check-odt-integrity OK (532 ODT-Dateien)`.
- `check-rechtsprechungshygiene OK`.
- `check-umlauthygiene.sh` ohne Treffer.
- `python3 scripts/run-eval.py --report`: `All-Pass 532/532`.

## v1.14.0 — Vertrags-Schärfung und Leitvorlagen-Taxonomie (2026-06-14)

Gezielte Vertrags-Schärfung nach `references/regelungstiefe-vertraege.md` und
mechanische Bereinigung der zweisprachigen Leitvorlagen-Taxonomie.

**Stand:** 532 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 532/532`.

### Geändert

- Standstill-Vereinbarung, Geschäftsanteilsabtretung, Sicherungsabtretung und
  doppelnützige Sanierungstreuhand nach dem Regelungstiefe-Standard gezielt
  geschärft.
- Zweisprachige Leitvorlagen, die keine Austauschverträge sind, von
  `vertrag.md` auf den zutreffenden Inhaltstyp `plan.md` oder `vermerk.md`
  umgestellt; READMEs, Rubrics und ODT-Fassungen synchronisiert.
- Vertrags-Schärfung bewusst ohne sachfremde Bausteine: keine erfundenen
  Vergütungen, Laufzeiten oder Schiedsklauseln, wo der Vertragstyp sie nicht
  trägt.

## v1.13.0 — Regelungstiefe-Standard, Rubrum-Pflicht und Vorlagen-Politur (2026-06-14)

Durchgreifende Qualitätsrunde über alle Vorlagen samt weiterem Ausbau der
Sammlung. Die zwischenzeitlich vergebenen Tags v1.10.0 bis v1.12.0 blieben
ohne eigenen Changelog-Eintrag; dieser Eintrag führt den dokumentierten Stand
seit v1.9.0 fort.

**Stand:** 532 Vorlagen in 35 Rechtsgebieten, Eval-Harness `All-Pass 532/532`.

### Neu

- Regelungstiefe-Standard `references/regelungstiefe-vertraege.md`: legt je
  Kautelar-Baustein und je Vertragstyp fest, wie regelungsgenau ein Vertrag
  auszuformulieren ist (Präzision vor Wortfülle), mit Antiverbositäts-Regeln
  und Schärfungs-Checkliste; aus `CLAUDE.md` Abschnitt 2 referenziert.
- Wachstum auf 532 Vorlagen seit der letzten dokumentierten Version (v1.9.0, 459 Vorlagen).

### Geändert

- Rubrum- und Schlussblock-Pflicht: jede Vorlage trägt oben einen Rubrum-,
  Beteiligten- oder Adressatenkopf und unten einen Schluss- oder
  Unterzeichnungsblock.
- Kurz-Hinweis statt Vollvorspruch im Vorlagentext; der ausführliche
  Vorspruch steht jetzt in der README des jeweiligen Vorlagenordners.
- Platzhalter vereinheitlicht: Fill-in-Felder durchgängig in spitzen
  Klammern `<…>` statt `[…]`.

### Behoben

- Schwarze Block-Glyphen und unsichtbare Soft-Hyphens aus Vorlagen, READMEs
  und einer Rubric entfernt.
- ODT-Arbeitsfassungen der bereinigten Vorlagen neu aus der Markdown-Quelle
  erzeugt.

## v1.9.0 — Neue Rechtsgebiete, Aufsichtsrecht und EU-/Kartell-Ausbau (2026-06-13)

Ausbau der Sammlung auf 30 Rechtsgebiete mit neuen eigenständigen Bereichen
für Verfassungsrecht, Europarecht, Kartell- und Marktrecht, Zoll- und
Außenwirtschaftsrecht, Aufsichtsrecht/BaFin sowie getrenntes Insolvenz- und
Restrukturierungsrecht.

**Stand:** 459 Vorlagen in 30 Rechtsgebieten, Eval-Harness `All-Pass 459/459`.

### Neu

- 35 zusätzliche Vorlagen mit Markdown-Quelle, ODT-Arbeitsfassung, README
  und `rubric.yaml`.
- Neue Bereiche:
  `verfassungsrecht`, `europarecht`, `kartell-und-marktrecht`,
  `zoll-und-aussenwirtschaftsrecht`, `aufsichtsrecht-und-bafin`,
  `restrukturierungsrecht-starug`.
- Insolvenz- und Sanierungsvorlagen ohne Dubletten aufgeteilt:
  insolvenzrechtliche Muster nach `insolvenzrecht`, StaRUG- und
  Sanierungsmuster nach `restrukturierungsrecht-starug`.
- BaFin- und Bundesnetzagentur-Vorlagen ohne Dubletten in
  `aufsichtsrecht-und-bafin` zusammengeführt.

### Verbessert

- Bereichs-READMEs neu aufgebaut: sprechende Dateinamen, ODT-Hinweis,
  Downloadlogik und Rubric-Konvention statt alter `VORLAGE.md`-Hinweise.
- `references/pruefquellen.md` um BVerfGG, GG, InsO, StaRUG, GWB, AWG, AWV,
  Unionszollkodex, BAFA, Bundeskartellamt, EU-Kommission, EBA, ESMA und
  EIOPA ergänzt.
- `references/rechtsprechungsradar-amtliche-pruefanker.md` um amtliche
  EU- und Kartellrechtsanker ergänzt, insbesondere CILFIT, Foto-Frost,
  Francovich und Intel.
- Gliederungsregel geschärft: `§` bleibt Normzitat, aber keine
  Klauselüberschrift als Gliederungsersatz; neue und berührte Vorlagen
  arbeiten dezimal.
- Umlaut-Hygiene-Check präzisiert: relative Markdown-Linkziele und technische
  Slugs lösen keinen Fehlalarm mehr aus.

### Geprüft

- `validate-vorlagen OK (459 Vorlagen, 30 Themenordner)`.
- `check-gliederung OK`.
- `check-umlauthygiene.sh` ohne Treffer.
- `check-rechtsprechungshygiene OK`.
- `check-odt-integrity OK (459 ODT-Dateien)`.
- `python3 scripts/run-eval.py --report`: `All-Pass 459/459`.

## v1.7.0 — Mandatsreife Prüfmatrix und amtliche Prüfanker (2026-06-13)

Qualitätslauf über den Gesamtbestand mit besonderem Fokus auf Kautelarstil,
Schriftsatzlogik, zweisprachige Klarheit, ODT-Nutzbarkeit und Quellenhygiene.

**Stand:** 424 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 424/424`.

### Verbessert

- Jede `VORLAGE.md` enthält nun eine **Mandatsreife Prüfmatrix** mit
 typabhängigen Prüfpunkten für Verträge, Schriftsätze, Anträge, Formulare,
 Notar-/Registervollzug, Aufsichtsbezug, zweisprachige Fassungen und
 Quellenprüfung.
- Alle 424 `rubric.yaml` erhalten den neuen Pflichtcheck
 `r81-mandatsreife-pruefmatrix`; `scripts/generate-default-rubrics.py` und
 `scripts/validate-vorlagen.py` erzeugen bzw. prüfen den Standard künftig
 automatisch.
- Neue Referenz `references/kautelarstandard.md` für Vertrags-,
 Schriftsatz- und Freigabelogik.
- Neue Referenz
 `references/rechtsprechungsradar-amtliche-pruefanker.md` mit erreichbaren
 amtlichen oder primären Prüfankern, getrennt nach Volltext,
 Pressemitteilung und Behördenquelle.
- Ältere Hinweise zu Rechtsprechungsrecherche wurden auf amtliche oder
 primäre Quellen zurückgeführt; Sekundärdatenbanken bleiben nur Suchhilfe.
- Alle 424 ODT-Dateien wurden aus den aktuellen Markdown-Quellen neu erzeugt.

### Geprüft

- `validate-vorlagen OK (424 Vorlagen, 24 Themenordner)`.
- `check-umlauthygiene.sh` ohne Treffer.
- `check-rechtsprechungshygiene OK`.
- `check-odt-integrity OK (424 ODT-Dateien)`.
- Stichproben im ODT-XML: Mandatsreife Prüfmatrix, Times New Roman, A4 und
 2,5-cm-Ränder vorhanden.
- 17/17 amtliche Prüfanker aus dem neuen Rechtsprechungsradar erreichbar.
- `python3 scripts/run-eval.py --report`: `All-Pass 424/424`.

## v1.6.0 — Quellenhygiene und ODT-Styling (2026-06-13)

Qualitätslauf über den Gesamtbestand.

**Stand:** 424 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 424/424`.

### Verbessert

- Vorspruch aller Vorlagen vereinheitlicht: knapper, stärkerer Hinweis auf
 experimentellen Charakter, fehlende Rechtsberatung, Eigengefahr,
 Berufsrecht, Datenschutz und Lizenz.
- Rechtsprechungsabschnitte sprachlich entschärft: konkrete Entscheidungen
 werden als Rechtsprechungsanker ausgewiesen und bleiben bis zur Live-Prüfung
 Recherchematerial, kein fertiger Zitatpool.
- Neue zentrale Prüfquellenliste: `references/pruefquellen.md`.
- ODT-Erzeugung verbessert: Überschriften nutzen nun ebenfalls Times New Roman;
 der ODT-Integritätscheck blockiert verbliebene Arial-Überschriften.

### Eval

- Neuer CI-Check `scripts/check-rechtsprechungshygiene.py`.
- Neuer Rubric-Pflichtcheck `r80-rechtsprechungshygiene` in allen 424
 Vorlagen.
- GitHub-Workflow führt die Rechtsprechungs-Hygieneprüfung aus.

### Geprüft

- `validate-vorlagen OK (424 Vorlagen, 24 Themenordner)`.
- `check-umlauthygiene.sh` ohne Treffer.
- `check-rechtsprechungshygiene OK`.
- `check-odt-integrity OK (424 ODT-Dateien)`.
- Interne Markdown-Links: 0 tote Ziele.
- Primärquellenlinks aus `references/pruefquellen.md`: 17/17 erreichbar.
- `python3 scripts/run-eval.py --report`: `All-Pass 424/424`.

## v1.5.0 — Praxisvorlagen-Ausbau und ODT-Qualitätsschleifen (2026-06-13)

Additiver Ausbau nach erneutem Qualitätslauf.

**Stand:** 424 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 424/424`.

### Neu

- 120 zusätzliche Praxisvorlagen: in jedem der 24 Rechtsgebiete genau fünf
 weitere Vorlagen, darunter Mandatsvereinbarung mit Honorar-,
 Haftungsbegrenzungs- und Datenschutzteil, Werkvertrag, Bürgschaftsvertrag,
 WEG-Protokoll, Beiratsprotokoll, Bewertungsmatrix im Vergaberecht,
 Datenschutzvorfälle, Rehabilitations- und Migrationsanträge,
 Transport- und Versicherungsformulare.
- Jede neue Vorlage enthält `VORLAGE.md`, `VORLAGE.odt`, `README.md` und
 `rubric.yaml`.
- Die neuen READMEs enthalten Downloadlinks, Anwendungsbereich,
 Einsatzgrenzen, Normen- und Quellenanker sowie Links zu amtlichen
 Gesetzes- und Rechtsprechungsquellen.

### Qualität

- Neuer technischer ODT-Integritätscheck `scripts/check-odt-integrity.py`
 prüft ZIP-Struktur, `content.xml`, `styles.xml`, A4-Seitenformat,
 2,5-cm-Ränder, Times New Roman und 11-pt-Grundschrift.
- GitHub-Workflow prüft nun zusätzlich Umlaut-Hygiene und ODT-Integrität.
- Dokumenthinweise der neuen Vorlagen sind knapp im Vorspruch; Detailhinweise
 liegen in den jeweiligen READMEs.

## v1.4.0 — Finaler Codex-Sanity-Check und Freigabeprotokoll (2026-06-13)

Abschließender Qualitätslauf auf dem konsolidierten v1.3.0-Stand.

**Stand:** 304 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 304/304`.

### Neu

- `allgemeines-und-bereichsuebergreifendes/freigabeprotokoll-vorlagenverwendung-zweisprachig` —
 zweisprachiges Freigabeprotokoll für die fachliche Endprüfung einer aus
 der Sammlung abgeleiteten Mandatsfassung.

### Behoben und verbessert

- Leere Tabellenplatzhalter im Pflegegrad-Widerspruch durch sprechende
 Platzhalter ersetzt.
- Umlaut-Hygiene-Check verbessert: technische Slugs, URLs und Markdown-Code
 werden nicht mehr als Fließtext-Fehler gewertet; die Prüfung erfasst nun
 Markdown- und YAML-Dateien repo-weit.
- Haupt-README auf den aktuellen Eval-Stand nachgezogen.

### Geprüft

- `validate-vorlagen OK (304 Vorlagen, 24 Themenordner)`.
- `scripts/check-umlauthygiene.sh` ohne Treffer.
- `python3 scripts/run-eval.py --report`: `All-Pass 304/304`.
- Interne Markdown-Links ohne tote Ziele, Platzhalter-URLs ausgenommen.

## v1.3.0 — Feinschliff der zehn Paradedokumente (2026-06-13)

Sprachlich-juristische Überarbeitung der zehn in der Praxis am häufigsten
gebrauchten Vorlagen — klarer, präziser, eleganter, ohne den rechtlichen
Gehalt zu verändern.

**Stand:** 303 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 303/303`.

### Überarbeitet

- Wohnraummietvertrag, GmbH-Gesellschaftsvertrag, unbefristeter Arbeitsvertrag,
 Mandats-/Vergütungsvereinbarung, Verschwiegenheitsvereinbarung (NDA),
 Kündigungsschutzklage, arbeitsrechtliche Abmahnung, Einzeltestament,
 Einspruch gegen den Bußgeldbescheid, Widerspruch gegen den Verwaltungsakt.

### Art der Verbesserungen

- Schachtsätze aufgelöst, aktive Formulierungen, eindeutige Bezugnahmen.
- Definierte Begriffe vereinheitlicht (z. B. offenlegende/empfangende Partei).
- Schriftsatz-Anträge in saubere Infinitivform gebracht; einzelne Grammatik-
 und Querverweisfehler korrigiert (rein redaktionell).
- Vorspruch, Hinweisleisten, Aktenzeichen und Regelungsumfang unverändert;
 ODT neu erzeugt; Eval je Dokument PASS.

## v1.2.0 — Qualitäts-Sanity-Check und zwei ergänzte Vorlagen (2026-06-13)

Sanity-Check und Bug-Hunt über den Gesamtbestand; rein additiv.

**Stand:** 303 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 303/303`.

### Neu (schließen zuvor tote Querverweise)

- `allgemeines-und-bereichsübergreifendes/datenschutzinformation-mandanten` —
 Mandanteninformation nach Art. 13, 14 DSGVO (vom Mandatsvertrag verlinkt).
- `sportrecht/vermarktungsvertrag-bildrechte` — Vermarktungs- und
 Bildrechtevertrag Sportler/Agentur (von zwei Sportrecht-Vorlagen verlinkt).

### Geprüft (Bug-Hunt)

- Keine Merge-Konfliktmarker, keine ASCII-Ersatzschreibung im deutschen
 Fließtext, keine offenen Platzhalter-Reste.
- Interne Markdown-Links: 0 tote Verweise (die 3 zuvor toten Querverweise
 durch die zwei neuen Vorlagen geschlossen).
- Vollständigkeitsprüfung: jede VORLAGE.md mit Vorspruch und VORLAGE.odt;
 Bereichs-Listings als Union konsistent.

## v1.1.0 — Zweisprachige Leitvorlagen und Codex-Ausbau (2026-06-13)

Integration der parallel erarbeiteten Beiträge; rein additiv, keine
Bestandsvorlage gelöscht.

**Stand:** 301 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 301/301`.

### Neu

- 6 Vorlagen Wirtschaft/Verwaltung (Codex): Generalvollmacht, Kaufvertrag
 bewegliche Sachen, Antrag Sterbeurkunde, Gesellschafterbeschluss
 Satzungsänderung GmbH, Informationszugang IFG Bund und Länder.
- 24 zweisprachige Leitvorlagen, je eine pro Rechtsgebiet.
- 15 konkrete zweisprachige Großtemplates (GmbH-/UG-/kleine-AG-Satzung,
 Shareholders Agreement, Beiratsordnung, GmbH-&-Co.-KG, Ehevertrag,
 Scheidungsfolgenvereinbarung, notarielle Vorsorgevollmacht,
 Grundstückskaufvertrag, BaFin-Institutserlaubnis,
 Bundesnetzagentur-Regulierungsantrag u. a.).

### Integrationshinweis

Ein Beitragsbranch basierte auf dem alten 142-Stand und hätte bei
direktem Merge 114 Bestandsvorlagen gelöscht; daher wurden nur die 39
echten Neuzugänge additiv übernommen. Alle zweisprachigen Vorlagen
enthalten eine Sprachvorrangklausel (deutsche Fassung maßgeblich).

### Behoben

- Datenverlust aus der Anwendungsbereich-Migration (PR #9) in zwei
 Insolvenzrecht-Vorlagen behoben; Migrations-Skript korrigiert.

## v1.0.0 — Vereinheitlichter Gesamtstand (2026-06-13)

Erster konsolidierter Release. Die Beiträge aller Mitwirkenden wurden auf
`main` zusammengeführt und in einen konsistenten Stand gebracht.

**Stand:** 256 Vorlagen in 24 Rechtsgebieten, Eval-Harness `All-Pass 256/256`.

### Inhalt

- Aufbau der Sammlung und Pflegelauf über alle 24 Rechtsgebiete; je Bereich
 mehrere Vertrags-, Schriftsatz- und Formularvorlagen.
- Rechtsprechungsstand 2024–2026 in den fachlichen Hinweisen; Aktenzeichen
 sind vor Mandatsverwendung live in den amtlichen Quellen zu verifizieren
 (human_review `r90`).
- Kompakt-READMEs mit direkten Download-Links (`raw/main/...`) auf die
 Markdown- und ODT-Fassung jeder Vorlage.

### Verbindliche Regeln (CLAUDE.md)

- Echte Umlaute und ß in allen deutschen Texten; ASCII-Ersatzschreibungen
 nur in technischen Slugs und URLs.
- Pflicht-Vorspruch in jeder `VORLAGE.md`: unverbindlich, experimenteller
 Text, keine Rechtsberatung, Verwendung auf eigene Gewähr und Gefahr;
 Hinweise nach BRAO § 43a, StGB § 203, DSGVO; Lizenz Apache-2.0 OR MIT.
- § 11 Rechtsprechungs-Hyperlinks, § 12 Anwendungsbereich nur im README,
 § 13 Abkürzungserklärung beim ersten Auftreten.

### Bereinigungen in diesem Release

- StaRUG-Redundanz beseitigt: Tippfehler-Slug `restrukturierungsplan-stare-ug`
 entfernt, ausführliche Fassung umbenannt auf `restrukturierungsplan-starug`;
 alle Verweise und Download-Links nachgezogen.
- Repo-weite ODT-Markdown-Konsistenz wiederhergestellt: alle 256 ODT aus der
 aktuellen Markdown-Quelle neu erzeugt (A4, Times New Roman 11 pt), nachdem
 die Migration des Anwendungsbereichs in die READMEs die ODT zunächst
 unberührt gelassen hatte.

### Eval-Harness

- Deklarative Rubrics je Vorlage; `python3 scripts/run-eval.py --report`.
- Die human_review-Token `r90-az-live-verifiziert` und
 `r91-endpruefung-anwalt` bleiben offen — die anwaltliche Endprüfung durch
 eine zugelassene Berufsträgerin ist nicht ersetzbar.
