# Europarecht-Kompass für deutsche Juristinnen und Juristen

Großes, freistehendes Plugin für deutsche Juristinnen und Juristen, die Europarecht nicht als deutsches Verwaltungsrecht mit Brüsseler Briefkopf missverstehen wollen. Es erklärt Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Beschlüsse, Soft Law, Charta, Grundfreiheiten, Beihilfen, Wettbewerbsrecht, Vorlageverfahren und Durchsetzung aus der Eigenlogik des Unionsrechts.

Dieses Plugin ist **vollständig freistehend**. Es benötigt keine anderen Plugins, keine externen Agenten und keine Kanzleisoftware. Wenn keine Datenbank, kein DMS, kein Übersetzungstool, keine Rechercheplattform oder kein Behördenzugang angeschlossen ist, arbeitet es mit manuellen Uploads oder einem ausdrücklich markierten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder ZIP aus dem Release installieren.
2. Neue Sache mit `europarecht-kommandocenter` starten.
3. Rechtsordnung, Zieltext, Parteirolle, Verfahrensstand und gewünschtes Arbeitsprodukt nennen.
4. Vertragsauszug, Memo, Bescheid, Normtext, Redline, Übersetzung oder fiktive Simulationsakte hochladen.
5. Am Ende immer das Qualitätstor verlangen: Rechtsquelle, Jurisdiktion, Denkfehler, False Friends, offene Annahmen, Review-Level und nächster Schritt.

## Enthaltene Skills

- `europarecht-kommandocenter` - Europarecht-Kommandocenter
- `europarecht-deutscher-denkfehler-scanner` - Deutscher-Denkfehler-Scanner
- `europarecht-vorrang-unmittelbare-wirkung` - Vorrang und unmittelbare Wirkung
- `europarecht-richtlinie-umsetzung` - Richtlinie und Umsetzung
- `europarecht-verordnung-beschluss-soft-law` - Verordnung, Beschluss und Soft Law
- `europarecht-grundfreiheiten-binnenmarkt` - Grundfreiheiten und Binnenmarkt
- `europarecht-grundrechte-charta` - EU-Grundrechte und Charta
- `europarecht-beihilfen-vergaben` - Beihilfen, Förderungen und Vergabe
- `europarecht-wettbewerb-kartell` - EU-Wettbewerb und Kartellrecht
- `europarecht-vorlageverfahren-art-267` - Vorlageverfahren Art. 267 AEUV
- `europarecht-vertragsverletzung-durchsetzung` - Vertragsverletzung und Durchsetzung
- `europarecht-delegierte-durchfuehrungsakte` - Delegierte und Durchführungsakte
- `europarecht-nationales-verfahren-effektivitaet` - Nationales Verfahren und Effektivität
- `europarecht-gesetzgebung-trilog` - EU-Gesetzgebung und Trilog
- `europarecht-klagearten-eugh` - EuGH-Klagearten und Rechtsschutz
- `europarecht-mandantenmemo` - Mandantenmemo und Executive Briefing
- `europarecht-quality-gate` - Europarecht-Qualitätstor
- `europarecht-simulation-behoerde-gericht` - Simulation Behörde, Gericht und Kommission

## Vorlagen

- `assets/templates/beihilfe-risk-assessment.md`
- `assets/templates/charta-grundrechte-check.md`
- `assets/templates/denkfehler-scan.md`
- `assets/templates/eu-gesetzgebung-monitor.md`
- `assets/templates/europarecht-mandantenmemo.md`
- `assets/templates/europarecht-mandatskarte.md`
- `assets/templates/europarecht-quality-gate.md`
- `assets/templates/grundfreiheiten-pruefung.md`
- `assets/templates/klagearten-eugh-check.md`
- `assets/templates/rechtsquellen-matrix.md`
- `assets/templates/richtlinie-umsetzung-map.md`
- `assets/templates/vertragsverletzung-beschwerde.md`
- `assets/templates/vorlagefrage-art-267.md`
- `assets/templates/vorrang-direktwirkung-check.md`

## Offizielle Startquellen

- [EUR-Lex: primacy of EU law](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=LEGISSUM:primacy_of_eu_law)
- [Consolidated TEU and TFEU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016ME/TXT)
- [Charter of Fundamental Rights](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012P/TXT)
- [EU law: regulations, directives and other acts](https://european-union.europa.eu/institutions-law-budget/law/types-legislation_en)
- [Court of Justice of the European Union](https://curia.europa.eu/)
- [EUR-Lex: direct effect](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=LEGISSUM:l14547)
- [European Commission: State aid](https://competition-policy.ec.europa.eu/state-aid_en)
- [European Commission: infringement procedure](https://commission.europa.eu/law/application-eu-law/implementing-eu-law/infringement-procedure_en)
- [European Parliament: ordinary legislative procedure](https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview)
- [EUR-Lex](https://eur-lex.europa.eu/)

## Download

- Plugin-ZIP: [europarecht-kompass.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/europarecht-kompass.zip)
- Akte: [testakte-europarecht-kompass-beihilfe-richtlinie.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-europarecht-kompass-beihilfe-richtlinie.zip)


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 19 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Europarecht Kompass-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan... |
| `europarecht-beihilfen-vergaben` | Beihilfenrecht und Vergaberecht prüfen wenn staatliche Foerderung oder öffentlicher Auftrag in Frage steht. Art. 107 108 AEUV Beihilfeverbote §§ 97 ff. GWB Vergaberecht. Prüfraster: Beihilfebegriff Ausnahmen Notifizierung De-minimis-Vero... |
| `europarecht-delegierte-durchfuehrungsakte` | Delegierte Rechtsakte und Durchführungsrechtsakte der EU einordnen und deren Verbindlichkeit prüfen. Art. 290 291 AEUV Delegierung. Prüfraster: Kategorie Widerruf Einwand Verbindlichkeit nationaler Umsetzungsbedarf Direktwirkung. Output:... |
| `europarecht-deutscher-denkfehler-scanner` | Typische deutsche Denkfehler im Umgang mit EU-Recht erkennen und korrigieren. Art. 267 AEUV Vorrangprinzip EuGH-Judikatur. Prüfraster: fehlende Europarechtskonformität verkannte Direktwirkung uebergangene Vorlagepflicht falsche Richtlini... |
| `europarecht-gesetzgebung-trilog` | Europaeisches Gesetzgebungsverfahren und Trilog-Verhandlungen einordnen wenn EU-Regelung in Entstehung ist. Art. 289 294 AEUV ordentliches Gesetzgebungsverfahren. Prüfraster: Verfahrensstand Kompromisstext Ratspositionen EP-Positionen Ze... |
| `europarecht-grundfreiheiten-binnenmarkt` | Grundfreiheiten des Binnenmarkts prüfen wenn grenzüberschreitende Wirtschaftstätigkeit oder nationale Beschraenkung in Frage steht. Art. 34 45 49 56 63 AEUV Warenverkehr Personenfreizuegigkeit Niederlassungsfreiheit. Prüfraster: Anwendun... |
| `europarecht-grundrechte-charta` | EU-Grundrechtecharta anwenden wenn EU-Recht vollzogen wird oder Mitgliedstaat im Anwendungsbereich des EU-Rechts handelt. Art. 51 GRC Anwendungsbereich Art. 6 EUV. Prüfraster: Anwendungsbereich Art. 51 GRC beruertes Recht Einschraenkung... |
| `europarecht-klagearten-eugh` | Klagemoglichkeiten vor dem EuGH und EuG einordnen und Zulassigkeitsvoraussetzungen prüfen. Art. 263 265 268 340 AEUV Nichtigkeitsklage Untätigkeitsklage Schadensersatz. Prüfraster: Klageart Klagebefugnis Fristen Zuständigkeit Zulässigkei... |
| `europarecht-kommandocenter` | Einstiegspunkt für Europarechtsmandate: Rechtsgebiet bestimmen relevante Normen identifizieren Bearbeitungsroute festlegen. AEUV EUV GRC EU-Sekundaerrecht. Prüfraster: Sachverhalt EU-Rechtsbezug Rechtsgebiet Route Zeitdruck Mandantenspra... |
| `europarecht-mandantenmemo` | Mandantenmemo zu EU-Rechtsfragen verstaendlich und praxisorientiert verfassen. AEUV EUV EU-Sekundaerrecht Grundfreiheiten. Prüfraster: Sachverhaltszusammenfassung Rechtslage Handlungsoptionen Risiken Empfehlung Mandantensprache. Output:... |
| `europarecht-nationales-verfahren-effektivitaet` | EU-Rechtsvorgaben zum effektiven nationalen Rechtsschutz prüfen wenn nationales Verfahren EU-Rechte beeintraechtigt. Art. 47 GRC Art. 19 EUV Effektivitaetsprinzip. Prüfraster: Effektivitaetsgrundsatz Aequivalenzgrundsatz effektiver Recht... |
| `europarecht-quality-gate` | EU-Rechtsgutachten oder -Schriftsatz auf typische Fehler und Luecken prüfen vor Versand. Art. 267 AEUV EuGH-Judikatur Vorrangprinzip. Prüfraster: Vorlagepflicht uebersehen Direktwirkung verkannt Normhierarchie fehlerhaft Richtlinienkonfo... |
| `europarecht-richtlinie-umsetzung` | EU-Richtlinie in nationales Recht umsetzen oder Umsetzungsdefizit prüfen. Art. 288 AEUV Richtlinienwirkung Art. 267 AEUV Vorabentscheidung. Prüfraster: Umsetzungsfrist Umsetzungsdefizit Direktwirkung richtlinienkonforme Auslegung Staatsh... |
| `europarecht-simulation-behoerde-gericht` | Verhandlung vor EU-Behoerde oder nationalem Gericht mit EU-Rechtsbezug simulieren und Argumentation testen. Art. 267 AEUV Art. 263 AEUV EuGH-Verfahren. Prüfraster: Argumente Gegenargumente Vorlageentscheidung Richterperspektive Schwachst... |
| `europarecht-verordnung-beschluss-soft-law` | EU-Verordnungen Beschluesse und Soft-Law-Instrumente einordnen und deren Verbindlichkeit prüfen. Art. 288 AEUV EU-Rechtsquellen. Prüfraster: Rechtsquellentyp Verbindlichkeit Direktwirkung nationaler Anpassungsbedarf zeitlicher Geltungsbe... |
| `europarecht-vertragsverletzung-durchsetzung` | Vertragsverletzungsverfahren der EU-Kommission gegen Mitgliedstaaten einordnen oder Reaktion eines Mitgliedstaats vorbereiten. Art. 258 260 AEUV Vertragsverletzung. Prüfraster: Verletzungshandlung Mahnschreiben Klage Urteil Sanktion Abhi... |
| `europarecht-vorlageverfahren-art-267` | Vorabentscheidungsersuchen nach Art. 267 AEUV vorbereiten oder Vorlagepflicht eines nationalen Gerichts prüfen. Art. 267 AEUV Vorabentscheidungsverfahren. Prüfraster: Vorlagepflicht acte-clair-Doktrin Vorlagefrage Formulierung Aussetzung... |
| `europarecht-vorrang-unmittelbare-wirkung` | Vorrang des EU-Rechts und unmittelbare Wirkung von EU-Normen prüfen wenn nationales Recht entgegensteht. Art. 288 AEUV Costa v. ENEL Van Gend en Loos EuGH-Judikatur. Prüfraster: Vorrangprinzip Kollision nationales EU-Recht unmittelbare W... |
| `europarecht-wettbewerb-kartell` | Kartell- und Wettbewerbsrecht nach Art. 101 102 AEUV prüfen wenn Absprachen Marktmissbrauch oder Zusammenschluesse in Frage stehen. Art. 101 102 AEUV § 1 GWB VO 1/2003. Prüfraster: Kartellverbot Marktabgrenzung marktbeherrschende Stellun... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
