# Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn Landesgesetze

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Denkmalschutzrecht in Deutschland: Art. 14 GG und Art. 73 GG als bundesstaatlicher Rahmen plus alle sechzehn Landesgesetze. Skills für Eintragung Erlaubnis Bußgeld steuerliche Förderung nach Paragraf 7i EStG und Welterbestätten — länderübergreifende Grundlagen und Landesrecht klar getrennt.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`denkmalschutzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/denkmalschutzrecht/denkmalschutzrecht-werkstatt.md" download><code>denkmalschutzrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/denkmalschutzrecht/denkmalschutzrecht-schnellstart.md" download><code>denkmalschutzrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Plugin für die anwaltliche Bearbeitung von Mandaten im deutschen Denkmalschutzrecht. Strukturiert in drei Schichten:

1. **Allgemeiner Teil** — bundesstaatlicher Rahmen (Art. 73 GG, Art. 14 GG, Verwaltungsverfahrensrecht, Welterbe).
2. **Querschnittsskills** — Denkmaleigenschaft, Eintragung, Erlaubnis, Förderung, Enteignung und Entschädigung; sie greifen unabhängig vom Bundesland.
3. **Sechzehn Bundesländer-Skills** — je ein eigener Skill pro Landesgesetz, mit Gesetzesbezeichnung, zuständigen Behörden und den landestypischen Verfahrensbesonderheiten.

## Aufbau und Anwendung

Die Allgemein-Skills helfen, einen Fall zu sortieren und ihn vom GG- und EU-Rahmen aus zu erden. Sobald klar ist, in welchem Bundesland das Objekt belegen ist, wird der landesspezifische Skill (`denkmalschutz-<bundesland>-<gesetzkuerzel>`) zugeschaltet — er enthält die konkreten Norm-Anker des jeweiligen Landesgesetzes und die zuständige Behördenkette.

## Quellenhygiene

Konkrete Paragrafenzitate, Aktenzeichen und Fundstellen werden ausnahmslos in den amtlichen Landesgesetzes-Datenbanken (typischerweise unter `landesrecht.<land>.de` oder `gesetze-im-internet.de` für Bundesrecht) live verifiziert; das Plugin nennt die Gesetzesabkürzungen und das verbindliche Suchregime, nicht aber halluzinierte Randnummern oder Fundstellen aus Modellwissen.

## Sicherheitsabstand

Denkmalschutzrecht ist Landesrecht. Bei jedem Mandat ist als allererstes das anwendbare Landesgesetz zu identifizieren — danach erst die einschlägigen Paragrafen prüfen. Skills, die einen Sachverhalt ohne Belegenheit beurteilen, sind unzulässig.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `art-14-gg-eigentum-und-denkmalschutz` | Art. 14 GG im Denkmalschutz: die Eintragung in die Denkmalliste und die daraus folgenden Erhaltungs-, Duldungs- und Veränderungsverbote sind Inhalts- und Schrankenbestimmung des Eigentums. Skill erklärt Sozialbindung, Zumutbarkeitsgrenze... |
| `art-73-gg-laenderzustaendigkeit` | Bundesstaatlicher Rahmen des Denkmalschutzes: Denkmalschutz ist keine konkurrierende Bundesmaterie nach Art. 73 oder 74 GG, sondern nach Art. 70 GG ausschließlich Sache der Länder. Skill ordnet, welche Aspekte trotzdem bundesrechtlich üb... |
| `baden-wuerttemberg-spezial-sachgesamtheiten-gesamtanlagen` | Baden-Wuerttembergische Besonderheit: Sachgesamtheiten und Gesamtanlagen nach DSchG-BW. Skill erlaeutert, wie Doerfer, Stadtquartiere und industrielle Bauensembles als zusammenhaengender Schutzgegenstand behandelt werden, welche Beteilig... |
| `bauordnungsrechtliche-schnittstelle` | Verhaeltnis von Denkmalrecht und Bauordnungsrecht in allen sechzehn Laendern: Baugenehmigung und Erlaubnisverfahren laufen regelmaessig parallel. Skill ordnet die Konzentrationswirkung der Baugenehmigung, das Beteiligungsrecht der Denkma... |
| `bayern-spezial-bodendenkmaeler-grabungsgenehmigung` | Bayerische Besonderheit: Bodendenkmaeler nach Art. 1 Abs. 4 BayDSchG mit Grabungsgenehmigung nach Art. 7 BayDSchG. Skill ordnet den Anwendungsbereich (jede Erdbewegung in Verdachtsflaechen genehmigungspflichtig), die Beteiligung des Baye... |
| `brandenburg-spezial-schloesser-gutsanlagen-restitution` | Brandenburgische Besonderheit: Hoher Bestand an Schloessern und Gutsanlagen, oft mit komplexer Eigentumsgeschichte nach Bodenreform 1945-1949 und Mauerfall 1990. Skill ordnet die typische Mandatslage zwischen Restitutionsfragen nach Verm... |
| `bussgeld-ordnungswidrigkeitsverfahren` | Sanktionsregime im Denkmalrecht: Bussgeldtatbestaende der Landesgesetze gegen unerlaubte Veraenderung, Beseitigung oder Verbringung; Schnittstelle zum Ordnungswidrigkeitenrecht nach OWiG; Strafrechtsschnittstelle nach Paragraf 304 StGB (... |
| `denkmaleigenschaft-feststellen` | Materielle Prüfung der Denkmaleigenschaft im Sinne der Landesgesetze: Sache von künstlerischem, geschichtlichem, wissenschaftlichem, städtebaulichem, volkskundlichem oder technischem Wert, an deren Erhaltung ein öffentliches Interesse be... |
| `denkmalschutz-baden-wuerttemberg-dschg-bw` | Denkmalschutzrecht Baden-Württemberg nach dem Gesetz zum Schutz der Kulturdenkmale (DSchG-BW). Skill bündelt zuständige Behörden (Landesamt für Denkmalpflege im Regierungspräsidium Stuttgart), Verfahrensbesonderheiten und Erlaubnistatbes... |
| `denkmalschutz-bayern-baydschg` | Denkmalschutzrecht Bayern nach dem Bayerischen Denkmalschutzgesetz (BayDSchG). Skill bündelt zuständige Behörden (Bayerisches Landesamt für Denkmalpflege in München, Außenstellen, untere Denkmalschutzbehörden bei den Kreisverwaltungsbehö... |
| `denkmalschutz-berlin-dschg-bln` | Denkmalschutzrecht Berlin nach dem Gesetz zum Schutz von Denkmalen in Berlin (DSchG-Bln). Skill bündelt zuständige Behörden (Senatsverwaltung für Kultur und Gesellschaftlichen Zusammenhalt; Landesdenkmalamt Berlin; Untere Denkmalschutzbe... |
| `denkmalschutz-berlin-spezial-stadtmauer-und-mauerweg` | Berliner Besonderheit: Der ehemalige Grenzverlauf der Berliner Mauer und Reste der Stadtmauer als denkmalwerter Erinnerungsort. Skill erlaeutert die landesrechtliche Einordnung, die Pflege der Mauerresten und Gedenksaeulen, das Verhaeltn... |
| `denkmalschutz-brandenburg-bbgdschg` | Denkmalschutzrecht Brandenburg nach dem Brandenburgischen Denkmalschutzgesetz (BbgDSchG). Skill bündelt zuständige Behörden (Ministerium für Wissenschaft, Forschung und Kultur; Brandenburgisches Landesamt für Denkmalpflege in Zossen-Wüns... |
| `denkmalschutz-bremen-dschgbrem` | Denkmalschutzrecht Freie Hansestadt Bremen nach dem Bremischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Landesamt für Denkmalpflege Bremen, Stadtamt Bremerhaven als untere Denkmalschutzbehörde im Stadtgebiet Bremerhaven) u... |
| `denkmalschutz-bremen-spezial-rathaus-und-roland-welterbe` | Bremer Besonderheit: Bremer Rathaus und Roland am Marktplatz sind seit 2004 UNESCO-Welterbe. Skill erlaeutert die Pufferzone, die ICOMOS-Begutachtung, das Verhaeltnis zur Bremischen Bauordnung und die Verfahrenspraxis bei Bauvorhaben in... |
| `denkmalschutz-hamburg-dschgha` | Denkmalschutzrecht Freie und Hansestadt Hamburg nach dem Hamburgischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Behörde für Kultur und Medien; Denkmalschutzamt; Bezirksämter als untere Denkmalschutzbehörden) und die Reform... |
| `denkmalschutz-hessen-hdschg` | Denkmalschutzrecht Hessen nach dem Hessischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Hessisches Ministerium für Wissenschaft und Kunst; Landesamt für Denkmalpflege Hessen in Wiesbaden; Untere Denkmalschutzbehörden bei de... |
| `denkmalschutz-mecklenburg-vorpommern-dschg-m-v` | Denkmalschutzrecht Mecklenburg-Vorpommern nach dem Denkmalschutzgesetz Mecklenburg-Vorpommern. Skill bündelt zuständige Behörden (Ministerium für Wissenschaft, Kultur, Bundes- und Europaangelegenheiten; Landesamt für Kultur und Denkmalpf... |
| `denkmalschutz-niedersachsen-ndschg` | Denkmalschutzrecht Niedersachsen nach dem Niedersächsischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Ministerium für Wissenschaft und Kultur; Niedersächsisches Landesamt für Denkmalpflege in Hannover; Untere Denkmalschutzb... |
| `denkmalschutz-nordrhein-westfalen-dschg-nrw` | Denkmalschutzrecht Nordrhein-Westfalen nach dem Denkmalschutzgesetz Nordrhein-Westfalen. Skill bündelt zuständige Behörden (Ministerium für Heimat, Kommunales, Bau und Digitalisierung; LVR-Amt für Denkmalpflege im Rheinland und LWL-Denkm... |
| `denkmalschutz-rheinland-pfalz-dschpflg` | Denkmalschutzrecht Rheinland-Pfalz nach dem Denkmalschutz- und -pflegegesetz Rheinland-Pfalz. Skill bündelt zuständige Behörden (Ministerium des Innern und für Sport; Generaldirektion Kulturelles Erbe Rheinland-Pfalz; Untere Denkmalbehör... |
| `denkmalschutz-saarland-sdschg` | Denkmalschutzrecht Saarland nach dem Saarländischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Ministerium für Bildung und Kultur; Landesdenkmalamt Saarland; Untere Denkmalschutzbehörden bei den Landkreisen) und die spezifis... |
| `denkmalschutz-saarland-spezial-voelklinger-huette-welterbe` | Saarlaendische Besonderheit: Voelklinger Huette seit 1994 UNESCO-Welterbe als bedeutendstes Industrie-Welterbe der Eisen- und Stahlproduktion. Skill ordnet die Schutzkonzeption (vollumfaengliche Erhaltung der industriellen Anlagen), die... |
| `denkmalschutz-sachsen-anhalt-dschg-lsa` | Denkmalschutzrecht Sachsen-Anhalt nach dem Denkmalschutzgesetz des Landes Sachsen-Anhalt. Skill bündelt zuständige Behörden (Ministerium für Wissenschaft, Energie, Klimaschutz und Umwelt; Landesamt für Denkmalpflege und Archäologie Sachs... |
| `denkmalschutz-sachsen-sachsdschg` | Denkmalschutzrecht Sachsen nach dem Sächsischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Sächsisches Staatsministerium für Regionalentwicklung; Landesamt für Denkmalpflege Sachsen in Dresden; Untere Denkmalschutzbehörden b... |
| `denkmalschutz-schleswig-holstein-dschg-sh` | Denkmalschutzrecht Schleswig-Holstein nach dem Denkmalschutzgesetz Schleswig-Holstein. Skill bündelt zuständige Behörden (Ministerium für Allgemeine und Berufliche Bildung, Wissenschaft, Forschung und Kultur; Landesamt für Denkmalpflege... |
| `denkmalschutz-thueringen-thuerdschg` | Denkmalschutzrecht Thüringen nach dem Thüringer Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Thüringer Staatskanzlei; Thüringisches Landesamt für Denkmalpflege und Archäologie in Erfurt; Untere Denkmalschutzbehörden bei den La... |
| `einstieg-routing` | Einstiegsskill für das Denkmalschutzrecht-Plugin. Sortiert das Mandat, klärt Belegenheit des Objekts und damit das anwendbare Landesgesetz, ermittelt Rolle (Eigentümer, Erwerber, Behörde, Nachbar, Förderantragsteller), Fristen und gewüns... |
| `eintragungsverfahren-allgemein` | Verfahren zur Eintragung eines Objekts in die Denkmalliste. Skill ordnet die typischen Verfahrensschritte (Anhörung, sachverständige Stellungnahme, Eintragungsverfügung, Bekanntgabe), erläutert konstitutive und nachrichtliche Eintragung... |
| `enteignung-uebernahme-und-entschaedigung` | Eigentumseingriff im Denkmalrecht: Enteignung nach Art. 14 Abs. 3 GG mit Entschädigung, Übernahmeanspruch der Eigentümerin bei wirtschaftlicher Unzumutbarkeit, Ausgleichszahlungen bei ausgleichspflichtiger Inhaltsbestimmung. Skill ordnet... |
| `erlaubnis-pflichtige-massnahmen` | Erlaubnisvorbehalt für Maßnahmen an Denkmalen: Veränderung, Beseitigung, Verbringung, Umsetzung, Wiederherstellung. Skill erläutert das Antrags- und Erteilungsverfahren, das Verhältnis zur Baugenehmigung (oft kombinierte Erlaubnis), Vers... |
| `erstgespraech-mandatsannahme` | Strukturiert das erste Mandantengespräch im Denkmalschutzrecht. Erhebt die Mandatsgrundlage (Vollmacht, Konfliktcheck, Honorarvereinbarung), das Objekt mit Belegenheit und Schutzstatus, die anstehende Maßnahme und das Mandatsziel. Liefer... |
| `foerderung-und-steuerliche-abschreibung` | Förderung von Denkmalsanierung: direkte Zuschüsse der Länder und Kommunen, Bundesförderung über die Beauftragte der Bundesregierung für Kultur und Medien (BKM) und die Deutsche Stiftung Denkmalschutz, vor allem aber die steuerliche Förde... |
| `grundbegriffe-und-rechtsquellen` | Grundbegriffe des deutschen Denkmalschutzrechts: Baudenkmal, Bodendenkmal, bewegliches Denkmal, Ensemble, Welterbe, Schutzbereich, Erhaltungssatzung. Rechtsquellen: Landesgesetze als primäres Recht, Art. 73 und Art. 14 GG als bundesstaat... |
| `hamburg-spezial-speicherstadt-kontorhausviertel` | Hamburger Besonderheit: Speicherstadt und Kontorhausviertel mit Chilehaus seit 2015 UNESCO-Welterbe. Skill erlaeutert die Schutzkategorien (Welterbe-Kernzone, Pufferzone, Erhaltungssatzung HafenCity), das Beteiligungsrecht des Denkmalsch... |
| `hessen-spezial-limes-bergpark-wilhelmshoehe` | Hessische Besonderheit: Obergermanisch-Raetischer Limes (Welterbe seit 2005, gemeinsam mit Bayern und Rheinland-Pfalz und Baden-Wuerttemberg), Bergpark Wilhelmshoehe in Kassel (Welterbe seit 2013) und Grube Messel (Welterbe seit 1995). S... |
| `kaltstart-triage` | Schnelltriage für ein neues denkmalschutzrechtliches Mandat. Erhebt in einer Sitzung Objektdaten, Schutzstatus, Mandantenrolle, konkrete Maßnahme, drohende Fristen und Eilrisiken. Liefert eine erste Risikoampel und benennt die unverzicht... |
| `mecklenburg-vorpommern-spezial-backsteingotik-stralsund-wismar` | Mecklenburg-vorpommersche Besonderheit: Altstaedte Stralsund und Wismar seit 2002 UNESCO-Welterbe der norddeutschen Backsteingotik. Skill erlaeutert die Verfahrenspraxis bei Sanierungs- und Umnutzungsvorhaben, das Verhaeltnis zur Hansest... |
| `niedersachsen-spezial-wattenmeer-fagus-werk` | Niedersaechsische Besonderheit: Wattenmeer (Welterbe seit 2009, gemeinsam mit Niederlanden und Hamburg und Schleswig-Holstein), Fagus-Werk Alfeld (Welterbe seit 2011), Goslar mit Bergwerk Rammelsberg und Oberharzer Wasserwirtschaft (Welt... |
| `nordrhein-westfalen-spezial-zollverein-industriekultur` | NRW-Besonderheit: Zeche und Kokerei Zollverein in Essen (Welterbe seit 2001), Aachener Dom (Welterbe seit 1978), Schloss und Park Augustusburg / Falkenlust Bruehl (Welterbe seit 1984), Niedergermanischer Limes (Welterbe seit 2021). Skill... |
| `quellen-livecheck` | Quellenhygiene-Skill für das Denkmalschutzrecht-Plugin. Liefert die kuratierte Suchadressen-Liste für die sechzehn Landesgesetzes-Datenbanken, das Bundesrecht (gesetze-im-internet.de), die Verwaltungsgerichtsbarkeit (BVerwG, OVG-Pakete)... |
| `rechtsprechungsanker-denkmalrecht` | Kuratierte Sammlung der zentralen Leitentscheidungen im deutschen Denkmalschutzrecht: Bundesverfassungsgericht zum Verhaeltnis von Art. 14 GG und Erhaltungspflichten, Bundesverwaltungsgericht zur konstitutiven Eintragung und zum Erlaubni... |
| `rheinland-pfalz-spezial-mittelrheintal-schum-staetten` | Rheinland-Pfalz-Besonderheit: Oberes Mittelrheintal (Welterbe seit 2002), Dom zu Speyer (Welterbe seit 1981), roemische Baudenkmaeler und Liebfrauenkirche in Trier (Welterbe seit 1986), SchUM-Staetten in Speyer, Worms und Mainz (Welterbe... |
| `sachsen-anhalt-spezial-bauhaus-quedlinburg-luther` | Sachsen-Anhaltsche Besonderheit: Bauhausstaetten Dessau (Welterbe seit 1996, Erweiterung 2017), Quedlinburg (Welterbe seit 1994), Luthergedenkstaetten Eisleben und Wittenberg (Welterbe seit 1996), Naumburger Dom (Welterbe seit 2018), Des... |
| `sachsen-spezial-montanregion-erzgebirge-muskauer-park` | Saechsische Besonderheit: Montanregion Erzgebirge / Krusnohori (Welterbe seit 2019, gemeinsam mit Tschechien) und Muskauer Park / Park Muzakowski (Welterbe seit 2004, gemeinsam mit Polen). Skill ordnet die grenzueberschreitende Verfahren... |
| `schleswig-holstein-spezial-luebeck-haithabu-wattenmeer` | Schleswig-holsteinische Besonderheit: Hansestadt Luebeck (Welterbe seit 1987), archaeologisches Grenzlandschaft Haithabu / Danewerk (Welterbe seit 2018) und Wattenmeer (Welterbe seit 2009). Skill ordnet die Verfahrenspraxis je Welterbest... |
| `thueringen-spezial-wartburg-klassisches-weimar-juedisches-erfurt` | Thueringer Besonderheit: Wartburg (Welterbe seit 1999), Klassisches Weimar (Welterbe seit 1998), Bauhausstaetten Weimar (Welterbe seit 1996 / Erweiterung 2017), juedisch-mittelalterliches Erbe Erfurt (Welterbe seit 2023). Skill ordnet di... |
| `unesco-welterbe-und-icomos` | Welterbestätten in Deutschland: völkerrechtlicher Rahmen der UNESCO-Welterbekonvention von 1972, ICOMOS-Begutachtung, Pufferzonen, Managementpläne und die mittelbare Wirkung auf das deutsche Landesrecht. Skill ordnet, was die Welterbe-Ei... |
| `verfahrensgrundsaetze-vwvfg` | Verwaltungsverfahrensrecht im Denkmalschutz: Anhörung nach Paragraf 28 VwVfG, schriftlicher Verwaltungsakt mit Begründung und Rechtsbehelfsbelehrung nach Paragrafen 35 37 und 39 VwVfG, Bekanntgabe nach Paragraf 41 VwVfG, Rücknahme rechts... |
| `widerspruch-und-klagewege` | Rechtsschutz im Denkmalschutzrecht: Widerspruchsverfahren nach Paragrafen 68 ff. VwGO (soweit landesrechtlich vorgesehen), Anfechtungsklage nach Paragraf 42 VwGO gegen Eintragung, Erlaubnisversagung, Untersagung und Beseitigungsanordnung... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
