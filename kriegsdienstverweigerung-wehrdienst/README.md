# Kriegsdienstverweigerung und Wehrdienst

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`kriegsdienstverweigerung-wehrdienst.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/kriegsdienstverweigerung-wehrdienst.md) (49 KB)
- Im Repo: [`testakten/megaprompts/kriegsdienstverweigerung-wehrdienst.md`](../testakten/megaprompts/kriegsdienstverweigerung-wehrdienst.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kriegsdienstverweigerung-wehrdienst`) | [`kriegsdienstverweigerung-wehrdienst.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kriegsdienstverweigerung-wehrdienst.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **KDV-Verfahren Malte Eberhard Rabenow / Berlin-Köln 2026** (`kriegsdienstverweigerung-gewissensantrag-berlin-2026`) | [Gesamt-PDF lesen](../testakten/kriegsdienstverweigerung-gewissensantrag-berlin-2026/gesamt-pdf/kriegsdienstverweigerung-gewissensantrag-berlin-2026_gesamt.pdf) | [`testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für Kriegsdienstverweigerung aus Gewissensgründen nach Art. 4 Abs. 3 GG und KDVG. Es ist ausdrücklich kein Plugin für Totalverweigerung, Dienstflucht, Befehlsboykott oder politische Leistungsverweigerung. Es behandelt die verfassungsrechtlich loyale Inanspruchnahme eines Grundrechts: Wer nicht gegen sein Gewissen Kriegsdienst mit der Waffe leisten kann, stellt sich nicht außerhalb der Ordnung, sondern beruft sich auf eine ihrer zentralen Gewissensgarantien.

Das Plugin führt von der ersten inneren Klärung über den Antrag beim Bundesamt für das Personalmanagement der Bundeswehr bis zur BAFzA-Entscheidung, Anhörung, Nachreichung, Anerkennung, Ablehnung, Widerspruch, Untätigkeitsklage und Eilrechtsschutz. Es berücksichtigt den Stand 2026 nach dem Wehrdienstmodernisierungsgesetz, insbesondere § 13 KDVG n. F. für ungediente Wehrpflichtige, die vor dem 01.01.2010 geboren wurden.

## Kaltstart

1. **Status klären:** ungedient, wehrpflichtig, vor/nach 01.01.2010 geboren, gemustert, einberufen, Reservist, FWDL, Soldat auf Zeit, Berufssoldat, Soldatin, frühere Soldatin/früherer Soldat?
2. **Ziel klären:** Antrag stellen, Begründung ordnen, Unterlagen vervollständigen, Sachstand erzwingen, Anhörung vorbereiten, Ablehnung angreifen, laufenden Dienstkonflikt entschärfen?
3. **Gewissen klären:** Geht es wirklich um Kriegsdienst mit der Waffe als solcher oder nur um einen bestimmten Krieg, eine politische Lage, Angst, Karriere, Gesundheit oder Totalverweigerung?
4. **Verfahren klären:** Antrag läuft über BAPersBw; BAFzA entscheidet inhaltlich nach Zuleitung. Direkte Übersendung an das BAFzA ist nicht der gesetzliche Standardweg.
5. **Rechtsschutz klären:** Sachstand, Nachreichung, Widerspruch, § 75 VwGO, § 80 VwGO oder § 123 VwGO nur nach Lage und Frist.

## Leitgedanke

Das Plugin soll nicht fertige Gewissensformeln produzieren. Es hilft, eine echte persönliche Entscheidung so zu strukturieren, dass sie rechtlich verständlich wird: Lebensweg, innere Entwicklung, Auslöser, Stabilität, Konsequenzen, Abgrenzung zu bloßer Politik und Plausibilität. Allgemeine Mustersätze sind gefährlich; eine persönliche, wahrhaftige und prüffähige Darstellung ist stärker.

## Typische Outputs

| Situation | Skills | Ergebnis |
| --- | --- | --- |
| Erster Antrag | `kriegsdienstverweigerung-wehrdienst-allgemein`, `status-routing`, `antrag-bapersbw-form`, `gewissensbegruendung-werkstatt` | Antragspaket mit Lebenslauf- und Begründungsplan |
| Antrag liegt, nichts passiert | `eingang-und-pk-nachweis`, `sachstandsanfrage-und-frist`, `untaetigkeitsklage-vwgo-75` | Sachstandsschreiben, Fristenmatrix, Eskalationsplan |
| Soldat oder Soldatin im Dienst | `aktive-soldaten-prioritaet`, `entlassung-berufssoldat-sg-46`, `entlassung-saz-sg-55`, `dienstpflichten-waehrend-verfahren` | Statusstrategie ohne unnötiges Disziplinarrisiko |
| Anhörung oder Zweifel | `schriftliche-anhoerung-kdvg-6`, `muendliche-anhoerung-vorbereitung`, `zweifel-ausraeumen-gesamtvorbringen` | Antwortentwurf, Anhörungsleitfaden, Belegliste |
| Ablehnung | `ablehnungsbescheid-analyse`, `widerspruch-kdvg-9`, `verwaltungsgericht-kdvg-10` | Rechtsbehelfsplan und Klagegerüst |
| 2026-Sonderfall | `wdmodg-2026-uebergang`, `kdvg-13-neun-monate`, `ungedient-vor-2010` | Prüfung der neuen Sonderregeln |

## Keine Totalverweigerung

Dieses Plugin erklärt bei Bedarf die Abgrenzung, unterstützt aber nicht beim bewussten Bruch mit allen Dienst- und Ersatzdienstpflichten. Der Fokus liegt auf der rechtmäßigen, offenen und dokumentierten Berufung auf das Gewissen gegen den Kriegsdienst mit der Waffe.

## Quellenstrategie

- **Amtlich zuerst:** GG, KDVG, WPflG, SG, VwGO, BAFzA-Hinweise, BAPersBw/Bundeswehr-Hinweise.
- **Rechtsprechung verifiziert:** BVerwG und BVerfG nur mit Datum, Aktenzeichen und freiem Link.
- **Aktualität 2026:** Vor Ausgabe immer prüfen, ob Wehrdienstmodernisierung, Bedarfswehrpflicht oder Verwaltungspraxis geändert wurden.
- **Keine Blindzitate:** keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## Datenschutz und Sicherheit

Gewissensbegründungen, Gesundheitsdaten, Personalakten, Musterungsunterlagen und Soldatenakten sind hochsensibel. In produktiven Verfahren nur in einem dafür freigegebenen, datenschutz- und berufsrechtskonformen System arbeiten.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 133 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ablehnungsbescheid-analyse` | Analysiert Tenor, Begründung, Rechtsbehelfsbelehrung und Fehler eines Ablehnungsbescheids im Kriegsdienstverweigerung Wehrdienst. |
| `ablehnungsgruende-kdvg-7` | Zerlegt Ablehnungen wegen Musterungsverweigerung, Unvollständigkeit, ungeeigneter Gründe oder Zweifel im Kriegsdienstverweigerung Wehrdienst. |
| `adressat-und-versandwege` | Prüft Post, Fax, E-Mail, Unterschrift und Zugangsnachweis im Kriegsdienstverweigerung Wehrdienst. |
| `akte-fuer-gericht-aufbauen` | Ordnet Tatsachen, Gewissen, Belege und Verfahrensfehler gerichtsfest im Kriegsdienstverweigerung Wehrdienst. |
| `akteneinsicht-kdv-aktenvernichtung-kdvg` | Routet Akteneinsicht bei BAFzA, BAPersBw und Gericht im Kriegsdienstverweigerung Wehrdienst. |
| `aktive-soldaten-prioritaet` | Nutzt § 4 KDVG für vorrangige Entscheidung bei laufendem Dienst im Kriegsdienstverweigerung Wehrdienst. |
| `aktuelle-lage-2026` | Prüft keine aktive Einberufung, fortbestehendes KDV-Recht und WDModG-Änderungen im Kriegsdienstverweigerung Wehrdienst. |
| `anerkennung-und-dienstfolgen` | Ordnet Folgen der Anerkennung für Wehrpflichtige, Soldaten und Reservisten im Kriegsdienstverweigerung Wehrdienst. |
| `anerkennung-voraussetzungen` | Prüft Vollständigkeit, geeignete Beweggründe und fehlende Wahrheitszweifel im Kriegsdienstverweigerung Wehrdienst. |
| `anerkennungsbescheid-gueltigkeit` | Erklärt Fortgeltung alter Anerkennungsbescheide und Nachweisstrategien im Kriegsdienstverweigerung Wehrdienst. |
| `angst-karriere-gesundheit-abgrenzen` | Unterscheidet Gewissensgründe von Angst, Karriere, Familienlage und Tauglichkeitsfragen im Kriegsdienstverweigerung Wehrdienst. |
| `anhoerungsprotokoll-und-korrektur` | Prüft Protokoll der Anhörung auf Missverständnisse und Ergänzungsbedarf im Kriegsdienstverweigerung Wehrdienst. |
| `anlagenverzeichnis-kdv` | Erstellt ein nachvollziehbares Anlagenverzeichnis für den KDV-Antrag im Kriegsdienstverweigerung Wehrdienst. |
| `anschreiben-kurz-antrag-bapersbw` | Erstellt ein kurzes Anschreiben mit Art.-4-Berufung und Anlagenliste im Kriegsdienstverweigerung Wehrdienst. |
| `antrag-bapersbw-form` | Führt durch Adresse, Form, Unterschrift, Lebenslauf und persönliche Begründung im Kriegsdienstverweigerung Wehrdienst. |
| `antrag-zur-niederschrift` | Erklärt Antragstellung zur Niederschrift beim BAPersBw im Kriegsdienstverweigerung Wehrdienst. |
| `anwaltlicher-brief-bafza` | Formuliert Schreiben im inhaltlichen Anerkennungsverfahren im Kriegsdienstverweigerung Wehrdienst. |
| `anwaltlicher-brief-bapersbw` | Formuliert Schreiben zu Eingang, Weiterleitung, Musterung und §13 im Kriegsdienstverweigerung Wehrdienst. |
| `arbeitgeber-fehlzeit-argumente-nicht` | Kommuniziert Anhörungstermine datensparsam gegenüber Arbeitgebern im Kriegsdienstverweigerung Wehrdienst. |
| `argumente-die-nicht-tragen` | Markiert KDV-schwache Argumente und passende Alternativwege im Kriegsdienstverweigerung Wehrdienst. |
| `aufschiebende-wirkung-kdvg-3` | Erklärt § 3 KDVG, § 11 KDVG und die Sonderwirkung des § 13 Abs. 3 im Kriegsdienstverweigerung Wehrdienst. |
| `ausbildungskosten-rueckforderung` | Prüft mögliche Rückforderungen und Härteargumente nach KDV-bezogenem Ausscheiden im Kriegsdienstverweigerung Wehrdienst. |
| `auslaendischer-wehrdienst-und-asyl` | Trennt deutsche KDV von Asyl-, Auslieferungs- und ausländischem Wehrrecht im Kriegsdienstverweigerung Wehrdienst. |
| `ausland-aufenthalt-bafza-entscheidungspfad` | Prüft Ruhen der Wehrpflicht und Genehmigungspflichten bei Auslandsaufenthalten im Kriegsdienstverweigerung Wehrdienst. |
| `bafza-entscheidungspfad` | Trennt Registrierung/Zuleitung durch BAPersBw von der inhaltlichen Entscheidung des BAFzA im Kriegsdienstverweigerung Wehrdienst. |
| `bedarfswehrpflicht-wpflg-2a` | Hält das Plugin anschlussfähig an aktivierte Bedarfswehrpflicht im Kriegsdienstverweigerung Wehrdienst. |
| `befehl-und-gewissenskonflikt` | Routet akute Befehlsgewissenskonflikte neben dem KDV-Verfahren im Kriegsdienstverweigerung Wehrdienst. |
| `begruendung-ehemalige-anerkannte-reservisten` | Prüft Widerspruch zwischen alter Anerkennung und späterer Bundeswehrnähe im Kriegsdienstverweigerung Wehrdienst. |
| `begruendung-fuer-aktive-soldaten` | Spezialwerkstatt für aktive Soldaten mit früherer Dienstbereitschaft im Kriegsdienstverweigerung Wehrdienst. |
| `begruendung-fuer-reservisten` | Spezialwerkstatt für Reservisten mit früherem Dienst und aktueller Heranziehungsnähe im Kriegsdienstverweigerung Wehrdienst. |
| `begruendung-fuer-ungediente` | Spezialwerkstatt für ungediente Antragsteller ohne Umkehrproblem im Kriegsdienstverweigerung Wehrdienst. |
| `begruendung-redaktion-ohne-schablone` | Überarbeitet persönliche Begründung sprachlich, ohne sie zu standardisieren im Kriegsdienstverweigerung Wehrdienst. |
| `beistand-kirchen-beratung` | Ordnet Beistand, kirchliche Beauftragte und anwaltliche Vertretung im Kriegsdienstverweigerung Wehrdienst. |
| `berufliche-folgen-berufssoldaten-kdv-bescheid` | Prüft Arbeitgeber, Ausbildung, Studium und Nachweise außerhalb der Bundeswehr im Kriegsdienstverweigerung Wehrdienst. |
| `berufssoldaten-kdv` | Prüft KDV-Antrag, Entlassungsfolge und Statusrisiken bei Berufssoldaten im Kriegsdienstverweigerung Wehrdienst. |
| `bescheid-archivieren` | Erstellt Nachweis- und Archivstrategie für Anerkennungsbescheide im Kriegsdienstverweigerung Wehrdienst. |
| `beweislast-und-ueberzeugungsbildung` | Erklärt hohe Wahrscheinlichkeit und gerichtliche Überzeugungsbildung im Kriegsdienstverweigerung Wehrdienst. |
| `bverwg-2005-pfaff-befehl` | Ordnet BVerwG 2 WD 12.04 als konkreten Gewissenskonflikt ein im Kriegsdienstverweigerung Wehrdienst. |
| `bverwg-2018-innere-umkehr` | Wendet BVerwG 03.08.2018 - 6 B 124.18 auf Gediente an im Kriegsdienstverweigerung Wehrdienst. |
| `bverwg-2021-parteivernehmung` | Bereitet persönliche gerichtliche Befragung nach BVerwG 31.03.2021 vor im Kriegsdienstverweigerung Wehrdienst. |
| `bverwg-sanitaetsdienst-innere-umkehr` | Wendet BVerwG 22.02.2012 - 6 C 31.11/6 C 11.11 an im Kriegsdienstverweigerung Wehrdienst. |
| `checkliste-nach-antrag` | Ordnet Eingangsnachweis, Aktenlog, Sachstand und Fristen nach Antragstellung im Kriegsdienstverweigerung Wehrdienst. |
| `checkliste-vor-antrag` | Letztes Qualitätsgate vor Absendung des KDV-Antrags im Kriegsdienstverweigerung Wehrdienst. |
| `datenschutz-gewissensakte-dienststelle` | Schützt Gewissensbegründung, Gesundheitsdaten und Personalakten im Kriegsdienstverweigerung Wehrdienst. |
| `dienstpflichten-waehrend-verfahren` | Minimiert Disziplinarrisiken während laufendem KDV-Antrag im Kriegsdienstverweigerung Wehrdienst. |
| `dienststelle-kommunikation` | Formuliert sachliche Dienststellenkommunikation ohne Provokation im Kriegsdienstverweigerung Wehrdienst. |
| `disziplinarrisiken-soldaten` | Warnt vor Disziplinar- und Strafrisiken bei eigenmächtigem Verhalten im Kriegsdienstverweigerung Wehrdienst. |
| `disziplinarvorgesetzter-stellungnahme` | Erklärt Stellungnahme der Disziplinarvorgesetzten bei Berufs- und Zeitsoldaten im Kriegsdienstverweigerung Wehrdienst. |
| `doppelte-staatsangehoerigkeit` | Routet deutsche KDV und ausländische Wehrpflichten ohne falsche Auslandsversprechen im Kriegsdienstverweigerung Wehrdienst. |
| `eidesstattliche-versicherung-eilrechtsschutz` | Prüft, ob eidesstattliche Versicherungen zulässig oder sinnvoll sind im Kriegsdienstverweigerung Wehrdienst. |
| `eilrechtsschutz-drohende-einberufung` | Prüft § 80 oder § 123 VwGO bei drohendem Dienst an der Waffe im Kriegsdienstverweigerung Wehrdienst. |
| `einberufung-nach-antrag` | Prüft, ob Einberufung trotz KDV-Antrag zulässig sein kann im Kriegsdienstverweigerung Wehrdienst. |
| `eingang-und-pk-nachweis` | Sichert Zugang, Aktenzeichen und Fristbeginn für spätere Rechtsschutzschritte im Kriegsdienstverweigerung Wehrdienst. |
| `einstweilige-anordnung-vwgo-123` | Prüft vorläufige Regelung ohne passenden §80-Fall im Kriegsdienstverweigerung Wehrdienst. |
| `europa-menschenrechte-familie-partnerschaft` | Ergänzt EMRK/EU-Grundrechte bei internationalen Bezügen vorsichtig im Kriegsdienstverweigerung Wehrdienst. |
| `familie-partnerschaft-gesellschaftsdruck` | Trennt externe Erwartungen von der eigenen Gewissensentscheidung im Kriegsdienstverweigerung Wehrdienst. |
| `fehlende-rechtsschutzbelehrung` | Prüft Bescheide auf richtige Rechtsbehelfsbelehrung und Fristfolgen im Kriegsdienstverweigerung Wehrdienst. |
| `formularmythen-social-media` | Entlarvt falsche Tipps zu Adresse, Mustern, Fristen und angeblichen Automatismen im Kriegsdienstverweigerung Wehrdienst. |
| `frist-bei-nachforderung-ein-monat` | Prüft Monatsfrist zur Vervollständigung nach § 7 KDVG im Kriegsdienstverweigerung Wehrdienst. |
| `fristenkalender-kdv` | Erstellt Fristenkalender für Antrag, Nachreichung, Anhörung, Widerspruch, § 75 und § 13 im Kriegsdienstverweigerung Wehrdienst. |
| `fruehere-soldaten-und-erneute-heranziehung` | Prüft Rechtsschutzinteresse früherer Soldaten wegen möglicher erneuter Heranziehung im Kriegsdienstverweigerung Wehrdienst. |
| `frueherer-abgelehnter-fuehrungszeugnis` | Prüft Folgen früherer Ablehnung oder Rücknahme für Schutzwirkung und Glaubhaftigkeit im Kriegsdienstverweigerung Wehrdienst. |
| `fuehrungszeugnis-zweifel` | Erklärt begrenzte Anforderung eines Führungszeugnisses bei Zweifeln im Kriegsdienstverweigerung Wehrdienst. |
| `fwdl-probezeit-und-kdv` | Unterscheidet KDV von einfacher Beendigung des freiwilligen Wehrdienstes im Kriegsdienstverweigerung Wehrdienst. |
| `gesetzliche-vertreter-rechtsbehelfe` | Erklärt Rechte gesetzlicher Vertreter im Widerspruchs- und Gerichtsverfahren im Kriegsdienstverweigerung Wehrdienst. |
| `gewissensbegruendung-werkstatt` | Strukturiert Lebensweg, Auslöser, Wandel und heutige Unbedingtheit ohne fremde Mustersätze im Kriegsdienstverweigerung Wehrdienst. |
| `gewissensentscheidung-massstab-glossar-kdv` | Prüft schwere Gewissensnot, unbedingte Bindung und Entscheidung gegen Töten im Krieg im Kriegsdienstverweigerung Wehrdienst. |
| `glossar-kdv` | Erklärt Wehrpflicht, Musterung, Anerkennung, Ersatzdienst, BAPersBw und BAFzA im Kriegsdienstverweigerung Wehrdienst. |
| `grundrecht-art-4-abs-3` | Rahmt KDV als staatstreue Grundrechtsausübung statt Staatsablehnung im Kriegsdienstverweigerung Wehrdienst. |
| `humanistische-pazifistische-gruende` | Formt säkulare Ethik in eine persönliche KDV-Begründung im Kriegsdienstverweigerung Wehrdienst. |
| `innere-umkehr-gediente` | Erarbeitet bei Gedienten den grundlegenden Wandel seit früherer Dienstbereitschaft im Kriegsdienstverweigerung Wehrdienst. |
| `kaltstart-triage` | Kaltstart für Kriegsdienstverweigerung aus Gewissensgründen: Status, Verfahrenslage, Gewissenskern, Antragspfad, Fristen, Rechtsschutz und passende Fachmodule auswählen. |
| `karrierecenter-bapersbw-kdvg-neun-kein` | Erklärt Behördennamen, Wehrersatzbehörde und frühere Kreiswehrersatzamt-Begriffe im Kriegsdienstverweigerung Wehrdienst. |
| `kdvg-13-neun-monate` | Nutzt § 13 Abs. 2 KDVG als Argument gegen unbegrenztes Liegenlassen im Kriegsdienstverweigerung Wehrdienst. |
| `kein-totalverweigerungs-tool` | Grenzt KDV vom bewussten Bruch mit jeder Dienst- oder Ersatzdienstpflicht ab im Kriegsdienstverweigerung Wehrdienst. |
| `ki-nutzung-gewissensbegruendung` | Setzt Grenzen für KI-Hilfe: strukturieren ja, fremde Begründung nein im Kriegsdienstverweigerung Wehrdienst. |
| `klage-ohne-berufung` | Erklärt § 10 KDVG und warum erstinstanzliche Sorgfalt besonders wichtig ist im Kriegsdienstverweigerung Wehrdienst. |
| `kommunikation-familie-kosten-auslagen` | Erklärt KDV ruhig gegenüber Familie und Umfeld ohne private Überoffenbarung im Kriegsdienstverweigerung Wehrdienst. |
| `kosten-und-auslagen-anhoerung` | Prüft Auslagen, Entgeltfortzahlung und notwendige Aufwendungen bei Anhörung im Kriegsdienstverweigerung Wehrdienst. |
| `lebensfuehrung-und-plausibilitaet` | Prüft, welche Lebensstationen die Gewissensentscheidung stützen oder erklären im Kriegsdienstverweigerung Wehrdienst. |
| `lebenslauf-luecken-und-widersprueche` | Bearbeitet frühere Waffenaffinität, Bundeswehrbewerbung oder Lebenslauflücken ehrlich im Kriegsdienstverweigerung Wehrdienst. |
| `mehrsprachige-orientierung` | Hilft Nicht-Muttersprachlern mit deutschen KDV-Begriffen ohne falsche Übersetzungssicherheit im Kriegsdienstverweigerung Wehrdienst. |
| `minderjaehrige-antragstellung-muendliche` | Prüft Antrag sechs Monate vor 18 oder vor 17 unter Sondervoraussetzungen im Kriegsdienstverweigerung Wehrdienst. |
| `muendliche-anhoerung-vorbereitung` | Bereitet nichtöffentliche mündliche Anhörung ohne auswendig gelernte Musterantworten vor im Kriegsdienstverweigerung Wehrdienst. |
| `musterung-verweigert-ablehnung` | Erklärt Ablehnungsrisiko bei Musterungsverweigerung im Kriegsdienstverweigerung Wehrdienst. |
| `musterungen-und-eignung` | Erklärt, warum KDV-Antrag Musterung grundsätzlich nicht ersetzt und wie § 13 wirkt im Kriegsdienstverweigerung Wehrdienst. |
| `musterungsbescheid-bestandskraft` | Prüft Bedeutung des Musterungsbescheids für Zuleitung und Entscheidung im Kriegsdienstverweigerung Wehrdienst. |
| `nachreichung-fehlender-unterlagen` | Formuliert fristwahrende Nachreichungen nach behördlicher Aufforderung. |
| `notfallplan-dienstantritt-parteivernehmung` | Erstellt 24/48-Stunden-Plan bei kurzfristiger Musterung, Übung oder Dienstantritt im Kriegsdienstverweigerung Wehrdienst. |
| `parteivernehmung-vorbereiten` | Bereitet persönliche gerichtliche Befragung ehrlich und konsistent vor im Kriegsdienstverweigerung Wehrdienst. |
| `personalakte-und-datenschutz-soldaten` | Prüft Personalaktenzuleitung und Datenschutz bei Soldaten-KDV im Kriegsdienstverweigerung Wehrdienst. |
| `personenkennziffer-und-grundakte` | Erklärt Registrierung, PK, Grundakte und Zuleitung im BAPersBw-Verfahren im Kriegsdienstverweigerung Wehrdienst. |
| `politische-motive-abgrenzen` | Trennt allgemeine Gewissensentscheidung von Kritik an einem bestimmten Krieg oder Staat im Kriegsdienstverweigerung Wehrdienst. |
| `presseanfragen-kdv-psychische-belastung` | Hilft bei öffentlicher Kommunikation ohne Verfahrensschaden im Kriegsdienstverweigerung Wehrdienst. |
| `psychische-belastung-und-beratung` | Routet Belastungen durch Gewissenskonflikt zu Hilfe ohne Pathologisierung im Kriegsdienstverweigerung Wehrdienst. |
| `qualitaetsgate-vor-ausgabe` | Erzwingt Normstand, Behördenstand, Statusprüfung, Quellenhygiene und Abgrenzung zur Totalverweigerung im Kriegsdienstverweigerung Wehrdienst. |
| `recht-auf-entscheidung` | Formuliert grundrechtsbewusst, warum eine ernste Gewissensentscheidung nicht beliebig liegen bleiben darf im Kriegsdienstverweigerung Wehrdienst. |
| `rechtsanwaltliche-vollmacht` | Erstellt Vollmacht, Akteneinsicht und Zustellungsbitte im Kriegsdienstverweigerung Wehrdienst. |
| `rechtsprechung-livecheck-dienstpflichten` | Prüft KDV-Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und Link im Kriegsdienstverweigerung Wehrdienst. |
| `rechtsschutzbeduerfnis-religioese` | Prüft Sachbescheidungsinteresse bei ausgesetzter Wehrpflicht und Soldatenstatus im Kriegsdienstverweigerung Wehrdienst. |
| `religioese-weltanschauliche-gruende` | Ordnet religiöse, humanistische und weltanschauliche Gründe ohne Bekenntniszwang im Kriegsdienstverweigerung Wehrdienst. |
| `reservisten-heranziehung` | Prüft KDV bei Beorderung, Heranziehungsbescheid und Übungen im Kriegsdienstverweigerung Wehrdienst. |
| `ruecknahme-oder-verzicht` | Erklärt Rücknahme eines Antrags oder Verzicht auf Anerkennung im Kriegsdienstverweigerung Wehrdienst. |
| `sachstandsanfrage-und-frist` | Formuliert gezielte Sachstandsanfragen vor Eskalation in § 75 VwGO im Kriegsdienstverweigerung Wehrdienst. |
| `sanitaetsdienst-und-waffenloser-dienst` | Setzt BVerwG 2012 zu Sanitätsdienst und waffenlosem Dienst um im Kriegsdienstverweigerung Wehrdienst. |
| `schluesselerlebnis-wandel-schriftliche` | Unterscheidet einzelne Schlüsselerlebnisse und längere innere Wandelungsprozesse im Kriegsdienstverweigerung Wehrdienst. |
| `schriftliche-anhoerung-kdvg-6` | Beantwortet Zweifel des BAFzA konkret, wahrhaftig und belegbar im Kriegsdienstverweigerung Wehrdienst. |
| `sicherheitsueberpruefung-und-extremismus` | Trennt Gewissensentscheidung von Loyalitäts- oder Extremismusvorwürfen im Kriegsdienstverweigerung Wehrdienst. |
| `social-media-und-oeffentlichkeit` | Prüft Posts, öffentliche Kampagnen und Dienstgeheimnisse im KDV-Kontext im Kriegsdienstverweigerung Wehrdienst. |
| `sofortvollzug-und-anordnung` | Prüft Sofortvollzug und aufschiebende Wirkung im KDV-Kontext im Kriegsdienstverweigerung Wehrdienst. |
| `soldat-zeit-soldatinnen-kdv-spannungs` | Prüft KDV, § 55 SG und Nebenfolgen bei Soldaten auf Zeit im Kriegsdienstverweigerung Wehrdienst. |
| `soldatinnen-und-kdv` | Stellt KDV-Rechte von Frauen dar, die dienen oder früher gedient haben im Kriegsdienstverweigerung Wehrdienst. |
| `spannungs-verteidigungsfall` | Prüft Sonderregeln im Spannungs-, Verteidigungs- und Bereitschaftsdienstfall im Kriegsdienstverweigerung Wehrdienst. |
| `sprache-der-loyalitaet` | Formuliert staatstreu und grundgesetznah ohne Unterwürfigkeit im Kriegsdienstverweigerung Wehrdienst. |
| `sprachlich-einfache-erklaerung` | Erklärt KDV in einfacher Sprache für Menschen ohne Juristensprache im Kriegsdienstverweigerung Wehrdienst. |
| `status-stellungnahmen-dritter-ungedient-ab` | Bestimmt, ob jemand ungedient, wehrpflichtig, Soldat, Reservist, frühere Soldatin oder Sonderfall ist im Kriegsdienstverweigerung Wehrdienst. |
| `stellungnahmen-dritter` | Prüft, wann Wahrnehmungen Dritter nach § 2 Abs. 3 KDVG helfen im Kriegsdienstverweigerung Wehrdienst. |
| `ungedient-ab-2010` | Prüft jüngere ungediente Personen, Antragstermin und fehlendes aktuelles Bescheidungsinteresse im Kriegsdienstverweigerung Wehrdienst. |
| `ungedient-vor-2010` | Wendet § 13 KDVG n. F. auf vor 2010 geborene ungediente Wehrpflichtige an im Kriegsdienstverweigerung Wehrdienst. |
| `unterlagenmappe-kdv-verwaltungsakt` | Strukturiert Antrag, Lebenslauf, Begründung, Belege, Nachweise und Bescheide im Kriegsdienstverweigerung Wehrdienst. |
| `verwaltungsakt-oder-informelles-schreiben` | Unterscheidet Bescheid, Aufforderung, Sachstand und informelle E-Mail im Kriegsdienstverweigerung Wehrdienst. |
| `vollstaendiger-lebenslauf` | Erstellt einen vollständigen, datensparsamen Lebenslauf mit gewissensrelevanten Stationen im Kriegsdienstverweigerung Wehrdienst. |
| `vollstaendigkeit-kdvg-2` | Prüft Anschreiben, Art.-4-Berufung, Lebenslauf und persönliche Begründung im Kriegsdienstverweigerung Wehrdienst. |
| `waffenbesitz-jagd-wahrheitspflicht` | Unterscheidet zivilen Waffenbezug von Kriegsdienst mit der Waffe im Kriegsdienstverweigerung Wehrdienst. |
| `wahrheitspflicht-und-authentizitaet` | Entfernt austauschbare KI-/Musterprosa und stärkt eigene Sprache im Kriegsdienstverweigerung Wehrdienst. |
| `wehrpflicht-ruht-ausland` | Prüft Ruhen der Wehrpflicht bei ständiger Lebensgrundlage im Ausland im Kriegsdienstverweigerung Wehrdienst. |
| `widerspruch-kdvg-9` | Erstellt Widerspruch gegen Ablehnung oder verfahrensrelevante Entscheidung im Kriegsdienstverweigerung Wehrdienst. |
| `widerspruch-sonderlagen-ablehnungsbescheid` | Prüft normale und verkürzte Widerspruchsfristen, insbesondere § 11 KDVG im Kriegsdienstverweigerung Wehrdienst. |
| `zeugenauswahl-und-aussage` | Prüft geeignete Zeugen für persönliche Entwicklung und Lebensführung im Kriegsdienstverweigerung Wehrdienst. |
| `zivildienst-altfaelle-ziviler-ersatzdienst` | Prüft Dienstzeit- oder Anerkennungsbescheinigungen aus früherem Zivildienst im Kriegsdienstverweigerung Wehrdienst. |
| `ziviler-ersatzdienst-art-12a` | Erklärt Ersatzdienst nach Art. 12a GG und § 1 Abs. 2 KDVG im Kriegsdienstverweigerung Wehrdienst. |
| `zweifel-ausraeumen-gesamtvorbringen` | Bearbeitet Zweifel aus Gesamtvorbringen und bekannten Tatsachen im Kriegsdienstverweigerung Wehrdienst. |
| `zweitbescheid-bescheinigung` | Formuliert Antrag auf Bestätigung oder Zweitausfertigung einer früheren Anerkennung im Kriegsdienstverweigerung Wehrdienst. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
