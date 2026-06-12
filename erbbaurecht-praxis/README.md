# Erbbaurecht Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`erbbaurecht-praxis`) | [`erbbaurecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/erbbaurecht-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Lindenwerder Erbbaurecht - Erbbauzins, Heimfall und Kita-Finanzierung** (`erbbaurecht-erbbauzins-heimfall-lindenwerder-2026`) | [Gesamt-PDF lesen](../testakten/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026/gesamt-pdf/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026_gesamt.pdf) | [`testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Spezialplugin für das Recht des Erbbaurechts: vom ersten Vertragsentwurf über Erbbauzins und Heimfall bis zu Finanzierung, Zustimmung, Versteigerung und Erbbaugrundbuch. Es erklärt die Sache auch für Menschen, die sonst nur Eigentum oder Miete kennen.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `erbbaurecht-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [ErbbauRG](https://www.gesetze-im-internet.de/erbbauv/)
- [GBO](https://www.gesetze-im-internet.de/gbo/)
- [GBV](https://www.gesetze-im-internet.de/gbvfg/)
- [BGB Sachenrecht](https://www.gesetze-im-internet.de/bgb/)
- [FamFG](https://www.gesetze-im-internet.de/famfg/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ablauf-laufzeitende-erbbaurecht-aktenstruktur` | Prüft die letzten zehn Jahre eines Erbbaurechts: Verlängerung, Neubestellung, Entschädigung, Rückbau, Finanzierungsauslauf, Mieter-/Betreiberkommunikation und Verhandlungsstrategie im Erbbaurecht Praxis. |
| `altlasten-rueckbau-erbbaurecht` | Ordnet Baugrund, Kontamination, Rückbaupflicht, Kostenverteilung und Beweissicherung im Erbbaurecht Praxis. |
| `change-control-dingliche-vorkaufsrechte` | Prüft, ob Anteilsübertragung, Verschmelzung, Formwechsel oder Kontrollwechsel beim Erbbauberechtigten Zustimmungspflichten oder Heimfallrechte auslösen im Erbbaurecht Praxis. |
| `entschaedigung-bei-heimfall-und-ablauf` | Prüft Entschädigung bei Heimfall, Zeitablauf, Wohnzweck, Marktwert, Bewertungsunterlagen und Sicherheiten im Erbbaurecht Praxis. |
| `erbbau-beschwerde-erbbaugrundbuch-lesen` | Prüft Zwischenverfügung, Rangproblem, Zustimmung, Nachweise und Beschwerde im Erbbaurecht Praxis. |
| `erbbaugrundbuch-lesen` | Führt durch Erbbaugrundbuch, Grundstücksgrundbuch, Rangvermerke, Belastungen und korrespondierende Eintragungen im Erbbaurecht Praxis. |
| `erbbaurecht-aktenstruktur` | Sortiert Vertrag, Grundbuch, Zins, Zustimmung, Bau, Bank, Kommunikation und Streit chronologisch im Erbbaurecht Praxis. |
| `erbbaurecht-betreiberwechsel` | Prüft Zustimmung, Bonität, Nutzungsänderung, Gewährleistung und Weitergabeklauseln im Erbbaurecht Praxis. |
| `erbbaurecht-dingliche-vorkaufsrechte` | Prüft vertragliche und dingliche Vorkaufsrechte, Ausübungsfall, Rang und Löschung im Erbbaurecht Praxis. |
| `erbbaurecht-fristen-und-reminder` | Baut Kalender für Zinsanpassung, Laufzeitende, Baupflicht, Versicherungen, Zustimmung und Berichtspflichten im Erbbaurecht Praxis. |
| `erbbaurecht-gewerbepark` | Prüft Nutzung, Baupflicht, Betriebspflicht, Umwelt, Altlasten, Heimfall und Investorenexit im Erbbaurecht Praxis. |
| `erbbaurecht-indexklausel-inflation` | Prüft Wertsicherung, Anpassungszeitpunkte, Transparenz, Streitprotokoll und Alternativformel im Erbbaurecht Praxis. |
| `erbbaurecht-investoren-q-and-a` | Bereitet Antworten zu Laufzeit, Zins, Heimfall, Finanzierung, Exit und Grundbuch auf im Erbbaurecht Praxis. |
| `erbbaurecht-kita-sozialimmobilie` | Prüft kommunale Zwecke, Betreiberwechsel, Fördermittel, Zustimmung, Rückbau und Ausfallrisiko im Erbbaurecht Praxis. |
| `erbbaurecht-mandantenbrief` | Erklärt Lage, Risiken und nächste Schritte ohne Fachchinesisch und mit Entscheidungsoptionen im Erbbaurecht Praxis. |
| `erbbaurecht-notar-und-grundbuchkosten` | Ordnet Kosten bei Bestellung, Änderung, Verlängerung, Übertragung, Belastung, Löschung, Heimfall und Zwangsversteigerung und erklärt sie mandantenverständlich im Erbbaurecht Praxis. |
| `erbbaurecht-photovoltaik-untererbbaurecht` | Prüft Nutzungszweck, bauliche Veränderung, Dienstbarkeit, Einspeisung, Finanzierung und Zustimmung im Erbbaurecht Praxis. |
| `erbbaurecht-qualitygate-vertrag` | Checkt, ob ein Entwurf investierbar, vollziehbar, finanzierbar und konfliktfest ist. |
| `erbbaurecht-rangruecktritt-bank` | Prüft Eigentümerzustimmung, Erbbauzinsrang, Finanzierungssicherheit und Heimfallkompensation im Erbbaurecht Praxis. |
| `erbbaurecht-schieds-und-gerichtsstand` | Prüft Schiedsklausel, Gerichtsstand, Beweisverfahren, Gutachterklausel und Vergleichsmechanik im Erbbaurecht Praxis. |
| `erbbaurecht-teilerbbaurecht-und-aufteilung` | Prüft Aufteilung, Wohnungserbbaurecht, Teilungserklärung, Sondernutzungsrechte, Zustimmung, Grundbuchblätter und Finanzierungsfolgen im Erbbaurecht Praxis. |
| `erbbaurecht-untererbbaurecht-und-weitergabe` | Prüft, ob und wie ein Untererbbaurecht, eine Betreiberüberlassung oder langfristige Untervermietung zulässig ist und welche Zustimmung, Rang- und Heimfallfolgen entstehen im Erbbaurecht Praxis. |
| `erbbaurecht-vorlage-zustimmungsantrag` | Entwirft Antrag an Grundstückseigentümer für Veräußerung, Belastung oder bauliche Änderung im Erbbaurecht Praxis. |
| `erbbaurechtsvertrag-pflichtinhalt` | Prüft Grundstück, Bauwerk, Laufzeit, Nutzung, Erbbauzins, Heimfall, Zustimmung, Versicherung, Instandhaltung und Entschädigung im Erbbaurecht Praxis. |
| `erbbauzins-rueckstand-mahnung` | Erstellt Mahnung, Zahlungsplan, Sicherheitencheck, Heimfallvorprüfung und Vergleichsvorschlag im Erbbaurecht Praxis. |
| `erbbauzins-struktur-erbbauzinsanpassung` | Prüft dingliche Sicherung, Fälligkeit, Wertsicherung, Anpassung, Rückstände und Rang im Erbbaurecht Praxis. |
| `erbbauzinsanpassung-paragraph-9a` | Prüft Anpassungsmechanik, Billigkeit, Verbraucher-/Wohnzwecknähe, Index, Streitwert und Dokumentationslogik im Erbbaurecht Praxis. |
| `erbbauzinsrang-finanzierungsbank-erbbaurecht` | Prüft, wann der Rang der Erbbauzinsreallast die Finanzierung entwertet, wie Rangrücktritt oder Stillhalteabrede aussehen können und welche Risiken Eigentümer, Bank und Erbbauberechtigter jeweils tragen im Erbbaurecht Praxis. |
| `finanzierung-bankfaehigkeit-gemeinde-kirche` | Prüft Beleihbarkeit, Rang, Laufzeitrest, Heimfallrisiko, Erbbauzinsrückstände und Bankauflagen im Erbbaurecht Praxis. |
| `gemeinde-kirche-stiftung-als-eigentuemer` | Prüft Beschluss, Genehmigung, Gemeinwohlbindung, Vergabe-/Beihilfefragen und Zustimmungspraxis im Erbbaurecht Praxis. |
| `heimfall-gruende-indexklausel-inflation` | Prüft Vertragsgrund, Verzug, Pflichtverletzung, Fristen, Verhältnismäßigkeit, Entschädigung und Grundbuchvollzug im Erbbaurecht Praxis. |
| `heimfall-verteidigung-insolvenz` | Entwickelt Einwendungen, Nachholung, Verhältnismäßigkeit, Vergleich, Finanzierungslösung und Eilstrategie im Erbbaurecht Praxis. |
| `insolvenz-erbbauberechtigter` | Ordnet Erbbauzins, Heimfall, Verwertung, Masse, Finanzierung und Grundbuchvollzug im Erbbaurecht Praxis. |
| `instandhaltung-versicherung-investoren-q` | Prüft Gebäudeunterhaltung, Verkehrssicherung, Versicherung, Nachweispflichten, Brandschutz, Betreiberpflichten und Sanktionen bei Pflichtverstößen im Erbbaurecht Praxis. |
| `kaltstart-routing` | Führt durch Grundstück, Erbbauberechtigte, Eigentümer, Laufzeit, Bauwerk, Erbbauzins, Heimfall, Finanzierung, Zustimmung und Grundbuchvollzug. |
| `kauf-due-kita-sozialimmobilie` | Baut DD-Liste: Vertrag, Grundbuch, Laufzeit, Zins, Zustimmung, Heimfall, Bank, Bauzustand und Exit im Erbbaurecht Praxis. |
| `kommunale-beschlussvorlage-erbbaurecht` | Erstellt Gemeinderatsvorlage für Bestellung, Änderung, Verlängerung oder Heimfallentscheidung im Erbbaurecht Praxis. |
| `laufzeit-verlaengerung-wohnungs-weg` | Prüft Verlängerung, Neubestellung, Rang, Zustimmung der Gläubiger und kommunale Beschlusslage im Erbbaurecht Praxis. |
| `nachhaltigkeit-baupflicht-notar` | Prüft Bauverpflichtung, energetische Standards, Fördermittel, Verzögerung und Sanktionen im Erbbaurecht Praxis. |
| `nutzungszweckwechsel-wohnen-rangruecktritt` | Prüft Nutzungszweck, baurechtliche und vertragliche Grenzen, Zustimmungserfordernisse, Erbbauzinsanpassung und Heimfallrisiko bei einem Zweckwechsel im Erbbaurecht Praxis. |
| `rechtsprechung-live-erbbaurecht-reminder` | Sichert, dass Entscheidungen nur mit Gericht, Datum, Aktenzeichen und freiem Link genutzt werden im Erbbaurecht Praxis. |
| `rueckbau-am-schieds-gerichtsstand` | Ordnet Rückbaupflicht, Entschädigung, Zustandserfassung, Sicherheiten und Konfliktstrategie im Erbbaurecht Praxis. |
| `sicherheiten-buergschaft-teilerbbaurecht` | Prüft Bürgschaft, Kaution, Rückbausicherheit, Lastschrift, Patronat, Step-in-Recht und Berichtspflichten als mildere Mittel zum Heimfall im Erbbaurecht Praxis. |
| `steuern-grunderwerbsteuer-entschaedigung` | Markiert GrESt-, Ertragsteuer-, USt- und Bewertungsfragen als Schnittstellen mit steuerlicher Prüfungspflicht im Erbbaurecht Praxis. |
| `verjaehrung-verwirkung-vorlage` | Prüft, ob lange geduldete Nutzungen, verspätete Zinsforderungen oder alte Pflichtverletzungen noch durchsetzbar sind und welche Beweislage gebraucht wird im Erbbaurecht Praxis. |
| `verkauf-spa-erbbaurechtsvertrag-pflichtinhalt` | Entwirft SPA-Klauseln zu Zustimmung, Zinsrückstand, Heimfallrisiko, Belastungen, Garantien und Closing im Erbbaurecht Praxis. |
| `vs-eigentum-erbbauzins-rueckstand` | Erklärt den dogmatischen Unterschied zu Eigentum, Miete, Nießbrauch, Dienstbarkeit und WEG im Erbbaurecht Praxis. |
| `wohnungs-erbbaurecht-und-weg` | Prüft WEG-Struktur, Teilungserklärung, Erbbaugrundbuch, Sondernutzungsrechte und Verwalterzustimmung im Erbbaurecht Praxis. |
| `zustimmung-veraeusserung-zwangsversteigerung` | Prüft Zustimmungserfordernis, Versagungsgründe, Frist, Ersatz durch Gericht und Bankfähigkeit im Erbbaurecht Praxis. |
| `zwangsversteigerung-erbbaurecht` | Prüft Versteigerung des Erbbaurechts, Rang, Erbbauzins, Heimfall, Eigentümerrechte und Erwerberrisiko im Erbbaurecht Praxis. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`erbbaurecht-praxis.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/erbbaurecht-praxis.md) (56 KB)
- Im Repo: [`testakten/megaprompts/erbbaurecht-praxis.md`](../testakten/megaprompts/erbbaurecht-praxis.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->
