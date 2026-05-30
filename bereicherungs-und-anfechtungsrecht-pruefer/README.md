# bereicherungs-und-anfechtungsrecht-prüfer

Generisches Mechanik-Prüfungs-Plugin zum interaktiven Durchprüfen aller Tatbestandsmerkmale von:

- **Bereicherungsrecht** §§ 812 ff. BGB (Herausgabe ohne Rechtsgrund Erlangtes)
- **Anfechtungsgesetz** (AnfG) — Rückgewähr trotz Rechtsgrund durch benachteiligten Vollstreckungsgläubiger
- **Insolvenzanfechtung** §§ 129–147 InsO — Rückgewähr zur Insolvenzmasse

Kein Rechtsberatungs-Tool. Mechanische Tatbestandsprüfung mit ständigen Warnhinweisen.

---

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| bereicherungs-und-anfechtungsrecht-prüfer | [bereicherungs-und-anfechtungsrecht-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bereicherungs-und-anfechtungsrecht-pruefer.zip) |

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `bereicherungs-und-anfechtungsrecht-pruefer.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe eine Insolvenzanfechtung gegen einen Lieferanten.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install bereicherungs-und-anfechtungsrecht-pruefer@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Kern-Workflow

1. **Triage**: Was ist passiert? Vermögensverschiebung mit oder ohne Rechtsgrund? Insolvenzverfahren eröffnet? Vollstreckungstitel vorhanden?
2. **Weichenstellung**:
   - Kein Rechtsgrund → Bereicherungsrecht (Leistungs- oder Nichtleistungskondiktion)
   - Rechtsgrund + außerhalb Insolvenz + Vollstreckungsgläubiger benachteiligt → AnfG
   - Rechtsgrund + Insolvenzverfahren → InsO-Anfechtung
   - Kombinationen und Konkurrenzen werden gesondert geprüft
3. **Bereicherungsrechtliche Feinsortierung**: Vermögensvorteil, Leistungszweck, Rechtsgrund, Behaltensgrund, Mehrpersonenverhältnis, Saldo, § 818 BGB
4. **Tatbestandsmerkmale pro Pfad**: Definitionen, Belegbedarf, Subsumtion im Vier-Schritt-Schema (Obersatz, Definition, Untersatz, Ergebnis)
5. **Rechtsfolgen, Konkurrenzen, Verjährung, Einreden**
6. **Output**: Klageschrift Bereicherungsklage, Anfechtungsklage (AnfG), Anfechtungsanzeige des Insolvenzverwalters

---

## Skills (98)

### A. Triage / Weichenstellung (6)

| Skill | Inhalt |
|---|---|
| `allgemein` | Einstieg, Routing und Überblick über Bereicherung, AnfG, InsO-Anfechtung und KI-Screening |
| `triage-vermoegensverschiebung-erfassen` | Strukturierte Erfassung: Wer hat was an wen geleistet, Belege, Zeitpunkt |
| `weichenstellung-bereicherung-oder-anfechtung` | Entscheidungsknoten: Rechtsgrund, Insolvenz, Vollstreckungstitel |
| `falsche-wiese-warnung-bereicherung-anfechtung` | Typische Falschverortungen und Systemfehler |
| `parallel-und-konkurrenz-pruefung` | Bereicherungsrecht und Anfechtung nebeneinander |
| `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` | Komplexitätsindikatoren, Fachanwaltsempfehlung |

### B. Bereicherungsrecht — Dogmatik und Feinsortierung (4)

| Skill | Inhalt |
|---|---|
| `rechtsgrund-und-behaltensgrund-pruefen` | Vermögensvorteil, Zweck, Rechtsgrund und Behaltensgrund sauber trennen |
| `zweckverfehlung-und-kondiktionszweck` | Zweckabrede, Zweckverfehlung, Risikozuweisung, Ausschlussgründe |
| `saldotheorie-rueckabwicklung-nichtiger-vertraege` | Rückabwicklung gegenseitiger Verträge mit Saldo, Schutzkorrekturen, Zug um Zug |
| `nutzungen-verwendungen-gefahrtragung-818` | Nutzungen, Surrogate, Verwendungen, Ersparnisse und Gefahrtragung bei § 818 BGB |

### C. Bereicherungsrecht — 50 zusätzliche Vertiefungs-Skills (50)

| Skill | Inhalt |
|---|---|
| `anspruchsziel-und-rueckabwicklungsarchitektur` | Anspruchsziel und Rückabwicklungsarchitektur: das praktische Rückabwicklungsziel in eine belastbare Anspruchsarchitektur übersetzt werden muss |
| `kondiktionskarte-vollstaendiger-fallaufbau` | Kondiktionskarte: vollständiger Fallaufbau: ein komplexer Fall zuerst als Personen-, Leistungs- und Vermögenskarte erfasst werden muss |
| `vermoegensvergleich-und-nettobetrachtung` | Vermögensvergleich und Nettobetrachtung: der bereicherungsrechtliche Netto-Vorteil statt nur der äußere Zufluss gesucht wird |
| `rechtsgrundmangel-anfang-und-wegfall` | Rechtsgrundmangel: Anfang und Wegfall: Anfangsmangel, späterer Wegfall, Teilmangel und Zweckausfall zeitlich getrennt werden müssen |
| `beweise-und-darlegungslast-bereicherungsrecht` | Beweise und Darlegungslast im Bereicherungsrecht: Darlegung, Beweislast und Belegbedarf anspruchsbezogen geplant werden müssen |
| `condictio-ob-causam-finitam-wegfall-des-rechtsgrundes` | Condictio ob causam finitam: Wegfall des Rechtsgrundes: ein zunächst bestehender Rechtsgrund später entfallen sein kann |
| `condictio-ob-rem-zweckabrede` | Condictio ob rem: Zweckabrede: eine Leistung für einen erkennbar bezweckten Erfolg erbracht wurde |
| `condictio-causa-data-causa-non-secuta` | Causa data causa non secuta: der erwartete Leistungserfolg endgültig nicht eingetreten ist |
| `leistungszweck-bei-vorleistung-und-anzahlung` | Leistungszweck bei Vorleistung und Anzahlung: Anzahlungen, Vorschüsse oder Reservierungsentgelte rückabgewickelt werden sollen |
| `schenkung-leihe-und-unbenannte-zuwendung` | Schenkung, Leihe und unbenannte Zuwendung: unentgeltliche Zuwendung, Nutzungsüberlassung und Zweckbindung auseinanderfallen können |
| `anweisungsfall-deckungs-und-valutaverhaeltnis` | Anweisungsfall: Deckungs- und Valutaverhältnis: ein Zahlungs- oder Leistungsdreieck mit Deckungs- und Valutaverhältnis vorliegt |
| `bankueberweisung-fehlbuchung-und-empfaengerhorizont` | Banküberweisung, Fehlbuchung und Empfängerhorizont: eine Banküberweisung, Fehlbuchung oder Fehlleitung bereicherungsrechtlich zugeordnet werden muss |
| `drittleistung-267-bgb-und-rueckgriff` | Drittleistung nach § 267 BGB und Rückgriff: ein Dritter bewusst auf eine fremde Schuld gezahlt haben könnte |
| `abgetretene-forderung-und-zession` | Abgetretene Forderung und Zession: Abtretung, Zahlung und Forderungsbestand auseinandergehalten werden müssen |
| `zahlung-auf-fremde-schuld-und-putativschuldner` | Zahlung auf fremde Schuld und Putativschuldner: jemand irrtümlich als vermeintlicher Schuldner oder auf fremde Schuld zahlt |
| `zahlstelle-bote-vertreter-und-treuhand` | Zahlstelle, Bote, Vertreter und Treuhand: eine Zwischenperson im Zahlungsweg rechtlich richtig eingeordnet werden muss |
| `insolvenzrisiko-im-dreipersonenverhaeltnis` | Insolvenzrisiko im Dreipersonenverhältnis: ein Direktanspruch im Dreieck faktisch ein Insolvenzrisiko verlagern würde |
| `bereicherungsausgleich-bei-kettenvertraegen` | Bereicherungsausgleich bei Kettenverträgen: Vertrags- oder Lieferketten ohne falschen Durchgriff rückabgewickelt werden müssen |
| `wertersatz-bei-dienstleistung-und-gebrauchsvorteil` | Wertersatz bei Dienstleistung und Gebrauchsvorteil: eine nicht rückgabefähige Dienstleistung oder Nutzung bewertet werden muss |
| `ersparte-aufwendungen-und-lebenshaltung` | Ersparte Aufwendungen und Lebenshaltung: Verbrauch des Erlangten mit ersparten eigenen Ausgaben kollidiert |
| `surrogat-erloes-versicherung-ersatzforderung` | Surrogat, Erlös, Versicherung und Ersatzforderung: an die Stelle des Erlangten ein Ersatzwert getreten sein kann |
| `boesglaeubigkeit-kenntnis-und-819-timing` | Bösgläubigkeit, Kenntnis und § 819 Timing: der Zeitpunkt der Kenntnis über den Umfang der Haftung entscheidet |
| `entreicherung-beweislast-und-substantiierung` | Entreicherung: Beweislast und Substantiierung: § 818 Abs. 3 BGB konkret behauptet oder angegriffen werden muss |
| `verwendungen-auf-das-erlangte` | Verwendungen auf das Erlangte: Aufwendungen auf den erhaltenen Gegenstand als Abzug oder Gegenrecht auftauchen |
| `nutzungen-zinsen-fruechte-gebrauchsvorteile` | Nutzungen, Zinsen, Früchte und Gebrauchsvorteile: Nutzungen und Zinsen ohne Doppelzählung erfasst werden müssen |
| `wertveraenderung-und-stichtag` | Wertveränderung und Bewertungsstichtag: Wertsteigerung, Wertverlust und Bewertungszeitpunkt streitig sind |
| `ebv-und-bereicherungsrecht` | EBV und Bereicherungsrecht: Eigentum, Besitz, Nutzungen und Verwendungen mit §§ 812 ff. BGB konkurrieren |
| `ruecktritt-widerruf-und-bereicherung` | Rücktritt, Widerruf und Bereicherung: Rücktritts- oder Widerrufsfolgen neben Bereicherungsrecht stehen |
| `anfechtung-142-und-rueckabwicklung` | Anfechtung nach § 142 BGB und Rückabwicklung: eine wirksame Anfechtung den Rechtsgrund rückwirkend beseitigt |
| `nichtiger-vertrag-134-138-und-rueckforderung` | Nichtiger Vertrag nach §§ 134 und 138 BGB: Verbots- oder Sittenwidrigkeit die Rückforderung prägt |
| `minderjaehrige-und-schutzwertung` | Minderjährige und Schutzwertung: Minderjährigenschutz durch Wertersatz oder Saldo nicht entwertet werden darf |
| `gesetzesverstoss-und-817-satz-2-vertiefung` | Gesetzesverstoß und § 817 Satz 2 vertieft: § 817 S. 2 BGB nach Normzweck und Schutzrichtung geprüft werden muss |
| `kondiktion-bei-schwarzarbeit-und-illegalitaet` | Kondiktion bei Schwarzarbeit und Illegalität: illegale Austauschverhältnisse bereicherungsrechtlich nicht normalisiert werden dürfen |
| `familien-und-partnerzuwendungen` | Familien- und Partnerzuwendungen: private Zuwendungen zwischen Näheverhältnis, Zweckbindung und Spezialrecht stehen |
| `gesellschaftsrechtliche-zuwendungen` | Gesellschaftsrechtliche Zuwendungen: Gesellschafterleistungen nicht ohne Gesellschaftsrecht rückabgewickelt werden dürfen |
| `arbeitsrechtliche-ueberzahlung` | Arbeitsrechtliche Überzahlung: Arbeitsentgelt überzahlt wurde und Ausschlussfristen oder Entreicherung drohen |
| `miet-und-pachtrechtliche-rueckabwicklung` | Miet- und pachtrechtliche Rückabwicklung: Miete, Pacht, Kaution oder Nutzung ohne Vertrag zurückabgewickelt werden |
| `kredit-darlehen-und-zinsenrueckforderung` | Kredit, Darlehen und Zinsenrückforderung: Darlehenszahlungen, Zinsen oder Entgelte positionengenau geprüft werden müssen |
| `versicherung-und-praemienrueckforderung` | Versicherung und Prämienrückforderung: Prämien und Leistungen im Versicherungsverhältnis zurückgefordert werden |
| `oeffentlich-rechtliche-rueckforderung-abgrenzung` | Öffentlich-rechtliche Rückforderung abgrenzen: Zivilrecht und öffentlich-rechtliche Erstattung auseinanderzuhalten sind |
| `eingriff-in-namen-bild-und-persoenlichkeitswert` | Eingriff in Name, Bild und Persönlichkeitswert: kommerzieller Persönlichkeitswert ohne Zustimmung genutzt wurde |
| `eigentumsnutzung-und-sachenrechtliche-zuweisung` | Eigentumsnutzung und sachenrechtliche Zuweisung: fremdes Eigentum wirtschaftlich genutzt wurde |
| `ip-lizenzanalogie-und-bereicherung` | IP-Lizenzanalogie und Bereicherung: ersparte Lizenz und Schutzrechtsnutzung bereicherungsrechtlich bewertet werden |
| `verfuegung-nichtberechtigter-816-vertiefung` | § 816 BGB vertieft: Verfügung Nichtberechtigter: ein Nichtberechtigter wirksam über fremde Rechte verfügt hat |
| `weitergabe-und-822-verteidigung` | Weitergabe und § 822 BGB Verteidigung: ein erlangter Vorteil unentgeltlich an Dritte weitergegeben wurde |
| `klageantrag-zahlung-herausgabe-zug-um-zug` | Klageantrag: Zahlung, Herausgabe, Zug um Zug: aus der Prüfung ein vollstreckbarer Antrag gebaut werden muss |
| `vergleichsberechnung-und-verhandlungsangebot` | Vergleichsberechnung und Verhandlungsangebot: bereicherungsrechtliche Risiken in einen Vergleichskorridor übersetzt werden |
| `verteidigung-gegen-bereicherungsklage` | Verteidigung gegen Bereicherungsklage: eine Bereicherungsklage systematisch abgewehrt werden soll |
| `mandanteninterview-bereicherungsrecht` | Mandanteninterview Bereicherungsrecht: die Tatsachen für einen Bereicherungsfall erst strukturiert erhoben werden müssen |
| `qualitaetskontrolle-halluzinationsschutz-bereicherungsrecht` | Qualitätskontrolle und Halluzinationsschutz: ein bereicherungsrechtlicher Output auf Scheinsicherheit und Quellenrisiken geprüft wird |

### D. Bereicherungsrecht — Leistungskondiktion §§ 812 ff. BGB (8)

| Skill | Inhalt |
|---|---|
| `leistungskondiktion-grundtatbestand-812-i-1-alt-1` | Grundtatbestand: etwas erlangt, durch Leistung, ohne Rechtsgrund |
| `leistungsbegriff-bewusste-zweckgerichtete-mehrung` | Definition Leistung, Mehrpersonenverhältnisse |
| `condictio-indebiti-813-bgb` | Einredebehaftete Verbindlichkeiten |
| `ausschluss-814-bgb-kenntnis-der-nichtschuld` | Ausschluss bei positiver Kenntnis der Nichtschuld |
| `ausschluss-817-bgb-gesetzes-und-sittenverstoss` | Sperrwirkung bei eigenem Verstoß, Rückausnahmen |
| `umfang-der-herausgabe-818-bgb-und-entreicherung` | Surrogate, Nutzungen, Wertersatz, Entreicherungseinrede |
| `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` | Bösgläubigkeit, Rechtshängigkeit, Haftungsfolgen |
| `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` | Anweisungsfälle, Doppelmangel, Drittleistung |

### E. Bereicherungsrecht — Nichtleistungskondiktion §§ 812 ff. BGB (4)

| Skill | Inhalt |
|---|---|
| `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` | Grundtatbestand: in sonstiger Weise erlangt |
| `eingriffskondiktion-zuweisungsgehalt` | Eingriff in Rechtszuweisungsgehalt, IP, Persönlichkeitsrecht |
| `verfuegung-eines-nichtberechtigten-816-bgb` | Entgeltliche und unentgeltliche Verfügung |
| `bereicherung-eines-dritten-822-bgb` | Unentgeltliche Weitergabe an Dritten |

### F. Anfechtungsgesetz — außerhalb Insolvenz (8)

| Skill | Inhalt |
|---|---|
| `anfg-grundtatbestand-und-anfechtungsberechtigte` | § 2 AnfG: Titel, fällige Forderung, Fruchtlosigkeit |
| `anfg-vorsatzanfechtung-3-i` | Benachteiligungsvorsatz und Kenntnis, zehn Jahre |
| `anfg-unentgeltliche-leistung-4` | Unentgeltlichkeit, vier Jahre |
| `anfg-mittelbare-benachteiligung-und-kongruenz` | Kongruente und inkongruente Deckung im AnfG |
| `anfg-fristen-und-anfechtungszeitraum` | Fristen §§ 3 und 4 AnfG, Verjährung |
| `anfg-rechtsfolge-rueckgewaehr-11` | Duldungspflicht, Rückgewähr, Wertersatz |
| `anfg-anfechtungsklage-prozessuales` | Zuständigkeit, Klageantrag, Streitwert, Vollstreckung |
| `anfg-einreden-und-verteidigung-anfechtungsgegner` | Gegenwehr des Anfechtungsgegners |

### G. Insolvenzanfechtung §§ 129–147 InsO (11)

| Skill | Inhalt |
|---|---|
| `inso-grundtatbestand-129-glaeubigerbenachteiligung` | Grundtatbestand: Rechtshandlung, objektive Benachteiligung |
| `inso-kongruente-deckung-130` | Drei Monate, Zahlungsunfähigkeit, Kenntnis |
| `inso-inkongruente-deckung-131` | Nicht beanspruchbare Leistung, Fristen |
| `inso-unmittelbar-nachteilige-rechtshandlungen-132` | § 132 InsO, drei Monate, unmittelbare Nachteiligkeit |
| `inso-vorsatzanfechtung-133` | Benachteiligungsvorsatz, Reform 2017, zehn Jahre, vier Jahre bei Deckung, zwei Jahre § 133 Abs. 4 |
| `inso-unentgeltliche-leistung-134` | Vier Jahre, keine Verschuldenserfordernis |
| `inso-gesellschafterdarlehen-135` | Gesellschafterdarlehen, Drittdarlehen mit Gesellschaftersicherheit, § 135 InsO |
| `inso-bargeschaeft-142` | Bargeschäft, unmittelbarer gleichwertiger Austausch, § 133-Unlauterkeit |
| `inso-rechtsfolge-rueckgewaehr-143-bis-147` | Rückgewähr zur Masse, Wertersatz, Gegenleistung, Verjährung |
| `inso-ki-anfechtungsansprueche-schuldnerakten` | KI-Screening von Schuldnerakten auf Anfechtungskandidaten mit Human-Review-Grenzen |
| `inso-verteidigung-anfechtungsgegner` | Verteidigung gegen Insolvenzanfechtung aus Sicht des Anfechtungsgegners |

### H. Konkurrenzen und Verjährung (3)

| Skill | Inhalt |
|---|---|
| `konkurrenz-bereicherung-vertraglich-deliktisch` | §§ 812 ff. neben Vertrag, Delikt, EBV |
| `konkurrenz-bereicherung-anfechtung-und-vindikation` | § 812 BGB neben AnfG, InsO und § 985 BGB |
| `verjaehrung-bereicherung-anfechtung-fristen` | § 195 BGB, § 15 AnfG, § 146 InsO, absolute Grenzen |

### Output-Skills (4)

| Skill | Inhalt |
|---|---|
| `output-klageschrift-bereicherungsklage` | Muster Klageschrift § 812 BGB |
| `output-anfechtungsklage-anfg` | Muster Anfechtungsklage nach AnfG |
| `output-anfechtungsanzeige-insolvenzverwalter` | Muster Anschreiben Insolvenzverwalter |
| `output-warnhinweis-und-pruefungsdokument` | Pflicht-Header und Warnblock |

---

## Inhaltliche Regeln

- **Keine Rechtsberatung** — jeder Skill endet mit Disclaimer-Block.
- Paragrafen-Format: `§ 812 Abs. 1 S. 1 Alt. 1 BGB`, `§ 133 InsO`, `§ 3 AnfG`.
- Beträge ohne Tausender-Komma.
- Umlaute in Texten ja, in Skill-Slugs nicht.
- Verbotene Einzel-Begriffe: bestimmte Modell- und Produktnamen (siehe CONTRIBUTING.md des Repos).

---

## Lizenz

Apache-2.0 OR MIT

## Autor

Klotzkette


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 98 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abgetretene-forderung-und-zession` | Nutze diesen Skill, wenn Abtretung, Zahlung und Forderungsbestand auseinandergehalten werden müssen. Normen: §§ 398-413 BGB sowie §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Bereicherungs- und Anfechtungsrecht-Prüfer. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen kl... |
| `anfechtung-142-und-rueckabwicklung` | Nutze diesen Skill, wenn eine wirksame Anfechtung den Rechtsgrund rückwirkend beseitigt. Normen: §§ 119 bis 124 BGB sowie §§ 142 und 812 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertu... |
| `anfg-anfechtungsklage-prozessuales` | Mandant hat vollstreckbaren Titel und will angefochtene Vermögensverschiebung gerichtlich angreifen: Anfechtungsklage nach AnfG erheben. Normen: §§ 2 11 13 AnfG, §§ 195 199 BGB. Prüfraster: Titel und Fristprüfung, Duldungs- vs. Wertersat... |
| `anfg-einreden-und-verteidigung-anfechtungsgegner` | Mandant ist Anfechtungsgegner und will sich gegen AnfG-Anfechtungsklage verteidigen. Normen: §§ 3 4 11 AnfG, §§ 195 199 BGB, § 142 InsO analog. Prüfraster: Entreicherungseinwand, fehlende Kenntnis des Benachteiligungsvorsatzes, Bargeschä... |
| `anfg-fristen-und-anfechtungszeitraum` | Anfechtungsfristen im außerinsolvenzlichen Anfechtungsrecht bestimmen: zehn Jahre Vorsatzanfechtung, vier Jahre unentgeltliche Leistung. Normen: §§ 3 4 AnfG, §§ 195 199 BGB. Prüfraster: Fristbeginn, Fristberechnung, Verjährungsverhältnis... |
| `anfg-grundtatbestand-und-anfechtungsberechtigte` | Grundvoraussetzungen der außerinsolvenzlichen Gläubigeranfechtung klären: vollstreckbarer Titel, fällige Forderung, Gläubigerbenachteiligung. Normen: §§ 1 2 AnfG, §§ 195 199 BGB. Prüfraster: Anfechtungsberechtigung, Rechtshandlungsbegrif... |
| `anfg-mittelbare-benachteiligung-und-kongruenz` | Kongruente und inkongruente Deckung sowie mittelbare Gläubigerbenachteiligung im AnfG-Kontext analysieren. Normen: §§ 1 3 4 AnfG. Prüfraster: unmittelbar vs. mittelbar begünstigende Rechtshandlung, Kongruenz, abstrakte Benachteiligungsmö... |
| `anfg-rechtsfolge-rueckgewaehr-11` | Rechtsfolge bei erfolgreicher AnfG-Anfechtung bestimmen: Duldungspflicht des Anfechtungsgegners und Wertersatz nach § 11 AnfG. Normen: § 11 AnfG, §§ 819 ff. BGB analog. Prüfraster: Duldung vs. Wertersatz, Bösgläubigkeit, Umfang der Rückg... |
| `anfg-unentgeltliche-leistung-4` | Anfechtung unentgeltlicher Leistungen außerhalb der Insolvenz prüfen: Schenkungsanfechtung in den letzten vier Jahren nach § 4 AnfG. Normen: § 4 AnfG. Prüfraster: Unentgeltlichkeitsbegriff, gemischte Schenkungen, Ausnahmen für Anstandssc... |
| `anfg-vorsatzanfechtung-3-i` | Vorsatzanfechtung außerhalb der Insolvenz geltend machen: Benachteiligungsvorsatz und Kenntnis des Anfechtungsgegners nach § 3 Abs. 1 AnfG. Normen: § 3 Abs. 1 AnfG. Prüfraster: Benachteiligungsvorsatz-Indizien, Kenntnis des Gegners, Zehn... |
| `anspruchsziel-und-rueckabwicklungsarchitektur` | Nutze diesen Skill, wenn das praktische Rückabwicklungsziel in eine belastbare Anspruchsarchitektur übersetzt werden muss. Normen: §§ 812 und 818 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne i... |
| `anweisungsfall-deckungs-und-valutaverhaeltnis` | Nutze diesen Skill, wenn ein Zahlungs- oder Leistungsdreieck mit Deckungs- und Valutaverhältnis vorliegt. Normen: § 670 BGB und §§ 812 ff. BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfä... |
| `arbeitsrechtliche-ueberzahlung` | Nutze diesen Skill, wenn Arbeitsentgelt überzahlt wurde und Ausschlussfristen oder Entreicherung drohen. Normen: § 611a BGB; §§ 812 und 818 BGB; § 199 BGB; tarifliche Ausschlussfristen. Prüfraster: Prüfe das Spezialrecht vor dem allgemei... |
| `ausschluss-814-bgb-kenntnis-der-nichtschuld` | Bereicherungsanspruch scheitert an § 814 BGB wegen positiver Kenntnis des Leistenden von der Nichtschuld. Normen: § 814 BGB. Prüfraster: positive Kenntnis vs. bloss Zweifel, Zeitpunkt der Kenntnis, Abgrenzung zu condictio indebiti. Outpu... |
| `ausschluss-817-bgb-gesetzes-und-sittenverstoss` | Bereicherungsanspruch gesperrt durch § 817 S. 2 BGB wegen eigenen Gesetzes- oder Sittenverstosses des Leistenden. Normen: §§ 817 134 138 BGB. Prüfraster: beiderseitiger Verstoß, Sperrwirkung, enge Rückausnahmen nach h.M. Output: Prüferge... |
| `bankueberweisung-fehlbuchung-und-empfaengerhorizont` | Nutze diesen Skill, wenn eine Banküberweisung, Fehlbuchung oder Fehlleitung bereicherungsrechtlich zugeordnet werden muss. Normen: §§ 675 ff. BGB; § 675u BGB; §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor de... |
| `bereicherung-eines-dritten-822-bgb` | Bereicherungsanspruch gegen Dritten bei unentgeltlicher Weitergabe des Erlangten nach § 822 BGB prüfen. Normen: § 822 BGB. Prüfraster: Unentgeltlichkeit der Weitergabe, Entreicherung des Erstempfängers, Subsidiarität des Drittanspruchs.... |
| `bereicherungsausgleich-bei-kettenvertraegen` | Nutze diesen Skill, wenn Vertrags- oder Lieferketten ohne falschen Durchgriff rückabgewickelt werden müssen. Normen: §§ 812 und 818 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhor... |
| `beweise-und-darlegungslast-bereicherungsrecht` | Nutze diesen Skill, wenn Darlegung, Beweislast und Belegbedarf anspruchsbezogen geplant werden müssen. Normen: §§ 812 ff. BGB; §§ 138 und 286 ZPO. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne inner... |
| `boesglaeubigkeit-kenntnis-und-819-timing` | Nutze diesen Skill, wenn der Zeitpunkt der Kenntnis über den Umfang der Haftung entscheidet. Normen: §§ 819 und 820 BGB; § 818 Abs. 4 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate... |
| `condictio-causa-data-causa-non-secuta` | Nutze diesen Skill, wenn der erwartete Leistungserfolg endgültig nicht eingetreten ist. Normen: § 812 Abs. 1 S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von erke... |
| `condictio-indebiti-813-bgb` | Rückforderung trotz Erfüllung einer einredebehafteten Verbindlichkeit nach § 813 BGB prüfen. Normen: § 813 BGB. Prüfraster: dauernde vs. temporäre Einreden, Verjährungseinrede, Tatbestandsmerkmale. Output: Prüfergebnis condictio indebiti... |
| `condictio-ob-causam-finitam-wegfall-des-rechtsgrundes` | Nutze diesen Skill, wenn ein zunächst bestehender Rechtsgrund später entfallen sein kann. Normen: § 812 Abs. 1 S. 2 Alt. 1 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von er... |
| `condictio-ob-rem-zweckabrede` | Nutze diesen Skill, wenn eine Leistung für einen erkennbar bezweckten Erfolg erbracht wurde. Normen: § 812 Abs. 1 S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere Motivation von... |
| `drittleistung-267-bgb-und-rueckgriff` | Nutze diesen Skill, wenn ein Dritter bewusst auf eine fremde Schuld gezahlt haben könnte. Normen: §§ 267 und 268 BGB; § 812 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont de... |
| `ebv-und-bereicherungsrecht` | Nutze diesen Skill, wenn Eigentum, Besitz, Nutzungen und Verwendungen mit §§ 812 ff. BGB konkurrieren. Normen: §§ 987 bis 1003 BGB; §§ 812 und 818 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm S... |
| `eigentumsnutzung-und-sachenrechtliche-zuweisung` | Nutze diesen Skill, wenn fremdes Eigentum wirtschaftlich genutzt wurde. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB; § 818 BGB. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der verletzte... |
| `eingriff-in-namen-bild-und-persoenlichkeitswert` | Nutze diesen Skill, wenn kommerzieller Persönlichkeitswert ohne Zustimmung genutzt wurde. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB; §§ 22 und 23 KUG; Art. 2 Abs. 1 GG. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt;... |
| `eingriffskondiktion-zuweisungsgehalt` | Nichtleistungskondiktion wegen Eingriffs in fremde Rechtsposition klären: Immaterialgüterrechte, Persönlichkeitsrechte. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB. Prüfraster: Zuweisungsgehalt der Rechtsposition, Eingriff ohne Leistung, Fallgr... |
| `entreicherung-beweislast-und-substantiierung` | Nutze diesen Skill, wenn § 818 Abs. 3 BGB konkret behauptet oder angegriffen werden muss. Normen: § 818 Abs. 3 BGB; §§ 138 und 286 ZPO. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate un... |
| `ersparte-aufwendungen-und-lebenshaltung` | Nutze diesen Skill, wenn Verbrauch des Erlangten mit ersparten eigenen Ausgaben kollidiert. Normen: § 818 Abs. 2 und Abs. 3 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und erspa... |
| `falsche-wiese-warnung-bereicherung-anfechtung` | Typische Falschverortungen erkennen: Vertrag statt Bereicherung, Bereicherung statt Anfechtung, AnfG statt InsO. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Abgrenzungsmatrix, häufige systematische Fehler, Weiterleitung. O... |
| `familien-und-partnerzuwendungen` | Nutze diesen Skill, wenn private Zuwendungen zwischen Näheverhältnis, Zweckbindung und Spezialrecht stehen. Normen: §§ 313 und 516 BGB; § 812 BGB; §§ 1372 ff. und § 1568a BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereic... |
| `gesellschaftsrechtliche-zuwendungen` | Nutze diesen Skill, wenn Gesellschafterleistungen nicht ohne Gesellschaftsrecht rückabgewickelt werden dürfen. Normen: §§ 30 und 31 GmbHG; §§ 57 und 62 AktG; § 812 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungs... |
| `gesetzesverstoss-und-817-satz-2-vertiefung` | Nutze diesen Skill, wenn § 817 S. 2 BGB nach Normzweck und Schutzrichtung geprüft werden muss. Normen: §§ 134 und 138 BGB; § 817 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in... |
| `inso-bargeschaeft-142` | Bargeschäft nach § 142 InsO prüfen: unmittelbarer gleichwertiger Leistungsaustausch, Geschäftsverkehrsübung, Arbeitsentgelt-Drei-Monats-Regel, Verhältnis zu §§ 130-132 und Vorsatzanfechtung § 133 mit erkannter Unlauterkeit. Output: Verte... |
| `inso-gesellschafterdarlehen-135` | Gesellschafterdarlehen und gleichgestellte Forderungen nach § 135 InsO prüfen: Sicherheiten zehn Jahre, Befriedigung ein Jahr, Drittdarlehen mit Gesellschaftersicherheit, Gebrauchsüberlassung, Sanierungsprivileg und Kleinbeteiligtenausna... |
| `inso-grundtatbestand-129-glaeubigerbenachteiligung` | Grundvoraussetzungen der Insolvenzanfechtung nach § 129 InsO klären: Rechtshandlung, objektive Gläubigerbenachteiligung, Kausalität. Normen: § 129 InsO. Prüfraster: Rechtshandlungsbegriff, unmittelbare vs. mittelbare Benachteiligung, Kau... |
| `inso-inkongruente-deckung-131` | Inkongruente Deckungsanfechtung nach § 131 InsO prüfen: Sicherung oder Befriedigung, die der Gläubiger nicht, nicht in der Art oder nicht zu der Zeit beanspruchen konnte. Fristen letzter Monat, zweiter oder dritter Monat; Zahlungsunfähig... |
| `inso-ki-anfechtungsansprueche-schuldnerakten` | KI-gestütztes Screening von Schuldnerakten auf mögliche Insolvenzanfechtungsansprüche nach §§ 129-147 InsO. Prüft Zahlungsdaten, Kontoauszüge, OPOS, Verträge, Sicherheiten, Gesellschafterdarlehen und Kommunikation; erzeugt Kandidatenmatr... |
| `inso-kongruente-deckung-130` | Kongruente Deckungsanfechtung nach § 130 InsO prüfen: geschuldete Sicherung oder Befriedigung, Drei-Monats-Zeitraum vor Insolvenzantrag oder Handlung nach Antrag, Zahlungsunfähigkeit, Kenntnis oder zwingende Kenntnisumstände, Margensiche... |
| `inso-rechtsfolge-rueckgewaehr-143-bis-147` | Rechtsfolgen der Insolvenzanfechtung nach §§ 143-147 InsO bestimmen: Rückgewähr zur Masse, Geldschuld und Zinsen, Entreicherung bei unentgeltlicher Leistung, Gegenleistung § 144, Rechtsnachfolger § 145, Verjährung § 146 und Rechtshandlun... |
| `inso-unentgeltliche-leistung-134` | Anfechtung unentgeltlicher Leistungen in der Insolvenz nach § 134 InsO prüfen: vier Jahre vor Insolvenzantrag. Normen: § 134 InsO. Prüfraster: Unentgeltlichkeitsbegriff, Ausnahmen Anstandsschenkungen, nahestehende Personen, Fristberechnu... |
| `inso-unmittelbar-nachteilige-rechtshandlungen-132` | Anfechtung unmittelbar nachteiliger Rechtshandlungen nach § 132 InsO prüfen: Benachteiligung in den letzten drei Monaten. Normen: §§ 132 129 InsO. Prüfraster: unmittelbare Nachteiligkeit, Kausalität, Drei-Monats-Frist, Abgrenzung § 129 I... |
| `inso-verteidigung-anfechtungsgegner` | Verteidigung des Anfechtungsgegners gegen Insolvenzanfechtung nach §§ 129-147 InsO strukturieren. Prüft fehlende Rechtshandlung oder Gläubigerbenachteiligung, Fristen, Kenntnis, § 133-Vermutungen, Bargeschäft § 142, Gegenleistung § 144,... |
| `inso-vorsatzanfechtung-133` | Vorsatzanfechtung nach § 133 InsO prüfen: Benachteiligungsvorsatz, Kenntnis, Vermutungsregel, Deckungshandlungen mit Vier-Jahres-Frist, kongruente Deckung mit Zahlungsunfähigkeit, Zahlungserleichterungs-Vermutung, nahestehende Personen u... |
| `insolvenzrisiko-im-dreipersonenverhaeltnis` | Nutze diesen Skill, wenn ein Direktanspruch im Dreieck faktisch ein Insolvenzrisiko verlagern würde. Normen: §§ 812 und 818 BGB; §§ 129 ff. InsO. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Emp... |
| `ip-lizenzanalogie-und-bereicherung` | Nutze diesen Skill, wenn ersparte Lizenz und Schutzrechtsnutzung bereicherungsrechtlich bewertet werden. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB; § 97 UrhG; § 14 MarkenG; § 139 PatG. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbezi... |
| `klageantrag-zahlung-herausgabe-zug-um-zug` | Nutze diesen Skill, wenn aus der Prüfung ein vollstreckbarer Antrag gebaut werden muss. Normen: §§ 812 und 818 BGB; §§ 253 und 322 BGB; § 348 BGB; § 274 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich o... |
| `kondiktion-bei-schwarzarbeit-und-illegalitaet` | Nutze diesen Skill, wenn illegale Austauschverhältnisse bereicherungsrechtlich nicht normalisiert werden dürfen. Normen: §§ 134 und 817 BGB; SchwarzArbG. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm... |
| `kondiktionskarte-vollstaendiger-fallaufbau` | Nutze diesen Skill, wenn ein komplexer Fall zuerst als Personen-, Leistungs- und Vermögenskarte erfasst werden muss. Normen: §§ 812 bis 822 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor; Trenne innere... |
| `konkurrenz-bereicherung-anfechtung-und-vindikation` | Anspruchskonkurrenzen zwischen Bereicherungsrecht §§ 812 ff. BGB, AnfG/InsO-Anfechtung und Vindikation § 985 BGB klären. Normen: §§ 812 985 BGB, §§ 129 ff. InsO, AnfG. Prüfraster: Verdrängungsregeln, Subsidiarität, Parallelität der Anspr... |
| `konkurrenz-bereicherung-vertraglich-deliktisch` | Verhältnis von Bereicherungsrecht zu vertraglichen Ansprüchen und Deliktsrecht §§ 823 ff. BGB klären. Normen: §§ 812 823 987 ff. BGB. Prüfraster: Vorrang-/Spezialitätsfragen, bereicherungsrechtliche Lückenfüllung. Output: Anspruchspriori... |
| `kredit-darlehen-und-zinsenrueckforderung` | Nutze diesen Skill, wenn Darlehenszahlungen, Zinsen oder Entgelte positionengenau geprüft werden müssen. Normen: § 488 BGB; §§ 812 und 818 BGB; §§ 491 bis 505d BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrech... |
| `leistungsbegriff-bewusste-zweckgerichtete-mehrung` | Leistungsbegriff im Bereicherungsrecht bestimmen: bewusste zweckgerichtete Mehrung, Empfängerhorizont, Vermögenszuordnung und Mehrpersonenfälle. Output: Leistungskarte mit Abgrenzung zur Nichtleistungskondiktion. |
| `leistungskondiktion-grundtatbestand-812-i-1-alt-1` | Leistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 1 BGB im Vier-Schritt-Schema prüfen: Erlangtes, Leistung, Rechtsgrund, Behaltensgrund, Ausschlussgründe und Umfang. Output: Bereicherungsanspruchs-Gutachten mit Abgrenzung zur Nichtleistung... |
| `leistungszweck-bei-vorleistung-und-anzahlung` | Nutze diesen Skill, wenn Anzahlungen, Vorschüsse oder Reservierungsentgelte rückabgewickelt werden sollen. Normen: § 812 Abs. 1 S. 1 Alt. 1 und S. 2 Alt. 2 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene vor... |
| `mandanteninterview-bereicherungsrecht` | Nutze diesen Skill, wenn die Tatsachen für einen Bereicherungsfall erst strukturiert erhoben werden müssen. Normen: §§ 812 ff. BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; Halte Bewei... |
| `mandatsabbruch-empfehlung-an-fachanwalt-insolvenz` | Komplexitätsindikatoren erkennen: Wann uebersteigt der Sachverhalt dieses Prüfungstool und erfordert Fachanwalt für Insolvenzrecht. Normen: §§ 129 ff. InsO, AnfG. Prüfraster: Komplexitätssignale, Mandatsgrenzen, Hinweispflicht. Output: W... |
| `mehrpersonenverhaeltnisse-direkt-und-durchgriffskondiktion` | Bereicherungsausgleich in Mehrpersonenverhältnissen prüfen: Leistungskarte, Anweisung, Deckungs- und Valutaverhältnis, Doppelmangel, Drittleistung, Insolvenzrisiko und Direktkondiktion. Output: Anspruchspriorisierungsmatrix. |
| `miet-und-pachtrechtliche-rueckabwicklung` | Nutze diesen Skill, wenn Miete, Pacht, Kaution oder Nutzung ohne Vertrag zurückabgewickelt werden. Normen: §§ 535 bis 580a BGB; §§ 812 und 818 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schut... |
| `minderjaehrige-und-schutzwertung` | Nutze diesen Skill, wenn Minderjährigenschutz durch Wertersatz oder Saldo nicht entwertet werden darf. Normen: §§ 107 bis 113 BGB; § 818 Abs. 3 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schu... |
| `nichtiger-vertrag-134-138-und-rueckforderung` | Nutze diesen Skill, wenn Verbots- oder Sittenwidrigkeit die Rückforderung prägt. Normen: §§ 134 und 138 BGB; §§ 812 und 817 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzwertungen in Saldo... |
| `nichtleistungskondiktion-grundtatbestand-812-i-1-alt-2` | Nichtleistungskondiktion nach § 812 Abs. 1 S. 1 Alt. 2 BGB prüfen: in sonstiger Weise ohne Rechtsgrund erlangt. Normen: § 812 Abs. 1 S. 1 Alt. 2 BGB. Prüfraster: kein Leistungsverhältnis, Abgrenzung zur Leistungskondiktion, Zuweisungsgeh... |
| `nutzungen-verwendungen-gefahrtragung-818` | Nutzungen, Verwendungen, Surrogate, ersparte Aufwendungen und Gefahrtragung bei § 818 BGB strukturiert prüfen. Output: Wert- und Risiko-Tabelle. |
| `nutzungen-zinsen-fruechte-gebrauchsvorteile` | Nutze diesen Skill, wenn Nutzungen und Zinsen ohne Doppelzählung erfasst werden müssen. Normen: § 818 Abs. 1 BGB; § 100 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und ersparte... |
| `oeffentlich-rechtliche-rueckforderung-abgrenzung` | Nutze diesen Skill, wenn Zivilrecht und öffentlich-rechtliche Erstattung auseinanderzuhalten sind. Normen: §§ 48 und 49a VwVfG; § 37 AO; § 812 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schut... |
| `output-anfechtungsanzeige-insolvenzverwalter` | Anschreiben des Insolvenzverwalters an den Anfechtungsgegner erstellen: Rückgewähr nach §§ 129 ff. und § 143 InsO, Tatbestand transaktionsscharf benennen, § 142- und § 144-Hinweise, Zinsen nur bei Verzug oder § 291 BGB, Verjährung § 146... |
| `output-anfechtungsklage-anfg` | Klageschrift für AnfG-Anfechtungsklage des Vollstreckungsgläubigers aufbauen: Rubrum, Duldungsantrag, Begründungsstruktur. Normen: §§ 2 11 13 AnfG. Prüfraster: Antragsformulierung, Begründungsaufbau Anfechtungstatbestand, Streitwertangab... |
| `output-klageschrift-bereicherungsklage` | Klageschrift aus Bereicherungsrecht §§ 812 ff. BGB aufbauen: Klageantrag auf Zahlung oder Herausgabe, ODUE-Schema. Normen: §§ 812 818 BGB, §§ 253 313 ZPO. Prüfraster: Obersatz, Definition, Untersatz, Ergebnis, Streitwert, Beweisangebot.... |
| `output-warnhinweis-und-pruefungsdokument` | Pflicht-Header und Warnblock für alle Prüfungsdokumente generieren: kein Rechtsrat, nur mechanische Prüfung. Normen: BRAO § 3. Prüfraster: Warnhinweis, Haftungsausschluss, Hinweis auf unvollständige Sachverhalte. Output: Standardisierter... |
| `parallel-und-konkurrenz-pruefung` | Bereicherungsrecht und Anfechtungsrecht gleichzeitig prüfen: Anspruchskonkurrenzen und gegenseitige Beeinflussung aller drei Regelungskreise. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Parallelität, Subsidiarität, wechsel... |
| `qualitaetskontrolle-halluzinationsschutz-bereicherungsrecht` | Nutze diesen Skill, wenn ein bereicherungsrechtlicher Output auf Scheinsicherheit und Quellenrisiken geprüft wird. Normen: §§ 812 ff. BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; Halt... |
| `rechtsgrund-und-behaltensgrund-pruefen` | Bereicherungsrechtliche Kernfrage prüfen: nicht nur Zufluss, sondern Rechtsgrund und Behaltensgrund. Normen: §§ 812 ff. BGB. Output: Behaltensgrund-Matrix mit Darlegungslast und Verteidigungsrisiken. |
| `rechtsgrundmangel-anfang-und-wegfall` | Nutze diesen Skill, wenn Anfangsmangel, späterer Wegfall, Teilmangel und Zweckausfall zeitlich getrennt werden müssen. Normen: § 812 Abs. 1 S. 1 Alt. 1 und S. 2 Alt. 1 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgr... |
| `ruecktritt-widerruf-und-bereicherung` | Nutze diesen Skill, wenn Rücktritts- oder Widerrufsfolgen neben Bereicherungsrecht stehen. Normen: §§ 346 bis 359 BGB; § 812 BGB; §§ 355 bis 361 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Sch... |
| `saldotheorie-rueckabwicklung-nichtiger-vertraege` | Rückabwicklung nichtiger gegenseitiger Verträge mit Saldierung, Schutzkorrekturen und § 818 Abs. 3 BGB prüfen. Output: Saldo- und Risikoanalyse. |
| `schenkung-leihe-und-unbenannte-zuwendung` | Nutze diesen Skill, wenn unentgeltliche Zuwendung, Nutzungsüberlassung und Zweckbindung auseinanderfallen können. Normen: §§ 516 und 528 BGB; § 530 BGB; § 812 BGB. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und Rechtsgrundebene... |
| `surrogat-erloes-versicherung-ersatzforderung` | Nutze diesen Skill, wenn an die Stelle des Erlangten ein Ersatzwert getreten sein kann. Normen: § 818 Abs. 1 BGB; § 285 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und ersparte... |
| `triage-vermoegensverschiebung-erfassen` | Erster Schritt: Vermögenverschiebung strukturiert erfassen für Bereicherungs- und Anfechtungsrecht. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Wer hat was an wen geleistet, Zeitpunkt, Belegsicherung, Weichenstellung Regel... |
| `umfang-der-herausgabe-818-bgb-und-entreicherung` | Umfang der Bereicherungshaftung nach § 818 BGB bestimmen: Erlangtes, Nutzungen, Surrogate, Wertersatz, Entreicherung, ersparte Aufwendungen und Zurechnung des Wegfalls. Output: Werttabelle mit Einredeprüfung. |
| `verfuegung-eines-nichtberechtigten-816-bgb` | Bereicherungsanspruch des Berechtigten nach § 816 BGB gegen verfügenden Nichtberechtigten prüfen. Normen: § 816 BGB. Prüfraster: wirksame Verfügung durch Gutglaubenserwerb oder Genehmigung, entgeltlich vs. unentgeltlich, Anspruch auf Erl... |
| `verfuegung-nichtberechtigter-816-vertiefung` | Nutze diesen Skill, wenn ein Nichtberechtigter wirksam über fremde Rechte verfügt hat. Normen: § 816 BGB; § 932 BGB. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der verletzten Po... |
| `vergleichsberechnung-und-verhandlungsangebot` | Nutze diesen Skill, wenn bereicherungsrechtliche Risiken in einen Vergleichskorridor übersetzt werden. Normen: §§ 812 und 818 BGB; § 779 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder Interview; H... |
| `verjaehrung-bereicherung-anfechtung-fristen` | Verjährung und Anfechtungsfristen trennen: § 195 und § 199 BGB für Bereicherung, § 15 AnfG, § 146 InsO mit Verweis auf regelmäßige BGB-Verjährung. Prüft Fristbeginn, Kenntnis, grob fahrlässige Unkenntnis, Hemmung, Anfechtungszeiträume §§... |
| `vermoegensvergleich-und-nettobetrachtung` | Nutze diesen Skill, wenn der bereicherungsrechtliche Netto-Vorteil statt nur der äußere Zufluss gesucht wird. Normen: §§ 812 und 818 BGB; Saldotheorie und Zweikondiktionentheorie. Prüfraster: Arbeite vom Vermögensvorteil zur Zweck- und R... |
| `verschaerfte-haftung-819-bgb-bei-bosglaeubigkeit` | Verschärfte Bereicherungshaftung nach § 819 BGB bei Bösgläubigkeit oder Rechtshängigkeit prüfen. Normen: §§ 819 818 Abs. 4 BGB. Prüfraster: Kenntnis des Mangels, Zeitpunkt, Umfang verschärfte Haftung, Rechtshängigkeitswirkung. Output: Pr... |
| `versicherung-und-praemienrueckforderung` | Nutze diesen Skill, wenn Prämien und Leistungen im Versicherungsverhältnis zurückgefordert werden. Normen: §§ 1 und 39 VVG; § 152 VVG; § 812 BGB. Prüfraster: Prüfe das Spezialrecht vor dem allgemeinen Bereicherungsrecht; Übernimm Schutzw... |
| `verteidigung-gegen-bereicherungsklage` | Nutze diesen Skill, wenn eine Bereicherungsklage systematisch abgewehrt werden soll. Normen: §§ 814 und 815 BGB; § 817 BGB; § 818 Abs. 3 BGB; § 819 BGB. Prüfraster: Übersetze die Anspruchsprüfung in Antrag, Verteidigung, Vergleich oder I... |
| `verwendungen-auf-das-erlangte` | Nutze diesen Skill, wenn Aufwendungen auf den erhaltenen Gegenstand als Abzug oder Gegenrecht auftauchen. Normen: §§ 994 bis 1003 BGB; § 818 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Su... |
| `weichenstellung-bereicherung-oder-anfechtung` | Triage-Entscheidung: welcher Regelungskreis ist einschlägig - Bereicherungsrecht, außerinsolvenzliche Anfechtung oder Insolvenzanfechtung. Normen: §§ 812 ff. BGB, AnfG, §§ 129 ff. InsO. Prüfraster: Rechtsgrundmangel, Insolvenzeröffnung,... |
| `weitergabe-und-822-verteidigung` | Nutze diesen Skill, wenn ein erlangter Vorteil unentgeltlich an Dritte weitergegeben wurde. Normen: § 822 BGB; § 818 Abs. 3 BGB. Prüfraster: Prüfe zuerst, ob wirklich keine Leistungsbeziehung vorliegt; Bestimme den Zuweisungsgehalt der v... |
| `wertersatz-bei-dienstleistung-und-gebrauchsvorteil` | Nutze diesen Skill, wenn eine nicht rückgabefähige Dienstleistung oder Nutzung bewertet werden muss. Normen: § 818 Abs. 2 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und erspart... |
| `wertveraenderung-und-stichtag` | Nutze diesen Skill, wenn Wertsteigerung, Wertverlust und Bewertungszeitpunkt streitig sind. Normen: § 818 Abs. 1 und Abs. 2 BGB. Prüfraster: Erstelle eine Vermögensbilanz statt einer Gegenstandsliste; Prüfe Nutzungen, Surrogate und erspa... |
| `zahlstelle-bote-vertreter-und-treuhand` | Nutze diesen Skill, wenn eine Zwischenperson im Zahlungsweg rechtlich richtig eingeordnet werden muss. Normen: §§ 164 ff. BGB; § 812 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerho... |
| `zahlung-auf-fremde-schuld-und-putativschuldner` | Nutze diesen Skill, wenn jemand irrtümlich als vermeintlicher Schuldner oder auf fremde Schuld zahlt. Normen: §§ 267 und 812 BGB. Prüfraster: Zeichne Deckung, Valuta und Zahlungsweg vor der Anspruchswahl; Bestimme den Empfängerhorizont d... |
| `zweckverfehlung-und-kondiktionszweck` | Zweckverfehlung, Wegfall des Leistungszwecks und kondiktionsrechtliche Zweckabreden prüfen. Normen: § 812 Abs. 1 S. 2 BGB. Output: Zweckkondiktions-Prüfbogen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
