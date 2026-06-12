# patentrecherche

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`patentrecherche.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/patentrecherche.md) (130 KB)
- Im Repo: [`testakten/megaprompts/patentrecherche.md`](../testakten/megaprompts/patentrecherche.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`patentrecherche`) | [`patentrecherche.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecherche.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **FTO-Recherche Rotorblattheizung — Windsysteme Norderhof AG vs. Vellbruck Energietechnik / EP 3 218 922 B1** (`fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter`) | [Gesamt-PDF lesen](../testakten/fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter/gesamt-pdf/fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter_gesamt.pdf) | [`testakte-fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter.zip) |
| **Patentrecht — Erfindungsakten Ravenstein & Moll** (`patentrecht-erfindungsakten-ravenstein-moll`) | [Gesamt-PDF lesen](../testakten/patentrecht-erfindungsakten-ravenstein-moll/gesamt-pdf/patentrecht-erfindungsakten-ravenstein-moll_gesamt.pdf) | [`testakte-patentrecht-erfindungsakten-ravenstein-moll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-patentrecht-erfindungsakten-ravenstein-moll.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

> Plugin für **Patentanwältinnen und Patentanwälte**, das Claude Cowork agentisch durch die klassischen Patentdatenbanken führt — Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO. Vorrecherche, **keine amtliche Recherche**.

## Hinweis vorab

Dieses Plugin ist **Vorrecherche-Werkzeug** für die Patentanwaltspraxis. Es ersetzt nicht die amtliche Recherche durch DPMA oder EPA und nicht die finale Bewertung durch die Patentanwältin. Treffer können unvollständig sein, falsch klassifiziert sein, in nicht maschinenlesbaren Volltexten verborgen sein oder durch Patentfamilien-Verbindungen verfehlt werden. Die abschließende Recherche muss durch eigene Nachrecherche oder durch Überprüfung der Treffer abgesichert werden.

Das Plugin ist Teil des Repositories [`claude-fuer-deutsches-recht`](../) und wurde mit Hilfe eines KI-Code-Assistenten erstellt; die inhaltliche Verantwortung trägt der Autor (Klotzkette).

## Inhalt

14 Skills, 3 References. Die methodische Grundlage stammt aus den Querschnitts-Plugins [`methodenlehre-buergerliches-recht`](../methodenlehre-buergerliches-recht) und [`zitierweise-deutsches-recht`](../zitierweise-deutsches-recht), die parallel aktiviert sein sollten.

### Skills

| Skill | Funktion |
| --- | --- |
| `patentrecherche-kaltstart-interview` | Setup: Patentanwältin, Mandant, Erfindung, Recherchezweck, Rechtsraum |
| `klassifikation-cpc-ipc` | CPC- und IPC-Klassen für die Recherche bestimmen |
| `agentische-datenbank-recherche` | Master-Skill: agentische Bedienung von Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO |
| `stand-der-technik-recherche` | Vorrecherche für Neuheitsbewertung vor eigener Anmeldung |
| `neuheit-pruefen` | § 3 PatG / Art. 54 EPÜ — Einzeldokument-Vorwegnahme aller Merkmale |
| `erfinderische-taetigkeit-pruefen` | § 4 PatG / Art. 56 EPÜ — Problem-Solution-Approach (EPA-Beschwerdekammern) |
| `freedom-to-operate-recherche` | FTO — Patentverletzungsrisiko aus Drittpatenten vor Markteintritt |
| `patentfamilien-analyse` | INPADOC-Familie — weltweite Patente mit gleichem Prioritätstag |
| `rechtsstand-pruefen` | Anmeldetag, Erteilung, Erlöschen, Einspruch, Nichtigkeit |
| `ueberwachung-konkurrenten` | Monitoring neuer Anmeldungen bestimmter Anmelder oder Klassen |
| `pruefungsbescheid-vorbereiten` | EPA- oder DPMA-Bescheid systematisch entgegnen, Stand-der-Technik-Entgegenhaltungen einordnen |
| `recherchebericht-erstellen` | Formaler Output mit Treffern, Bewertung, Disclaimer |
| `rueckfragen-mandant` | Erfindungsabgrenzung klären — Was ist der wesentliche Lösungsbeitrag |

### References

- `cpc-ipc-klassen-uebersicht.md` — CPC- und IPC-Hauptsektionen, Querverweis-Logik
- `patentdatenbanken-quellen.md` — Datenbanken im Detail (URL, Abdeckung, Stärken, Schwächen, agentische Bedienung)
- `bpatg-und-epa-rspr-leitentscheidungen.md` — Leitentscheidungen Patentanwaltspraxis (BGH X. Senat, BPatG, EPA G-Entscheidungen)

## Setup

Nach Aktivierung des Plugins wird beim ersten Lauf von `patentrecherche-kaltstart-interview` ein Profil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/patentrecherche/CLAUDE.md` angelegt (Kanzlei, Patentanwält:innen, Schwerpunktklassen, typische Mandantenstruktur).

## Pflichtdisclaimer

Jedes Recherche-Ergebnis enthält am Anfang den Disclaimer "**Hinweis zur Recherche** — KI-gestützte Vorrecherche, keine amtliche Recherche, finale Bewertung muss eigenständig abgesichert werden". Skills lassen den Disclaimer nicht weg.

## Verhältnis zum Berufsrecht

Patentanwältinnen sind Berufsgeheimnisträger nach § 203 Abs. 1 Nr. 3 StGB; § 39a PAO regelt die Verschwiegenheit, § 39c PAO regelt die Inanspruchnahme von Dienstleistern. Vor produktivem Einsatz eines KI-Dienstleisters: berufsrechtliche Vorprüfung mit dem Schwester-Plugin [`berufsrecht-ki-vertragspruefung`](../berufsrecht-ki-vertragspruefung) durchführen.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agentisch-fristen-form-und-zustaendigkeit` | Agentisch: Fristen, Form, Zuständigkeit und Rechtsweg im Patentrecherche. |
| `agentische-datenbank-recherche` | Agentische Patentdatenbank-Recherche: Suchauftrag in natuerlicher Sprache mit Erfindungsmaterial (Anspruchsentwurf, Beschreibung, Skizzen) wird automatisch in Suchstrings für Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Regis... |
| `anschluss-routing` | Anschluss-Routing für Patentrecherche (FTO, Validity, Family-Watch): wählt den nächsten Spezial-Skill nach Engpass (Prioritätsjahr 12 Monate, Erfindungsmeldung, Anspruchssatz, Recherche-Report), dokumentiert Router-Entscheidung mit Begrü... |
| `depatisnet-verhandlung-vergleich-und-eskalation` | Depatisnet: Verhandlung, Vergleich und Eskalation im Patentrecherche. |
| `dokumente-intake` | Dokumentenintake für Patentrecherche (FTO, Validity, Family-Watch): sortiert Erfindungsmeldung, Anspruchssatz, Recherche-Report, prüft Datum, Absender, Frist und Beweiswert (Espacenet/DEPATISnet-Treffer, USPTO Patent Family); markiert Lü... |
| `dpmaregister-epue-beweislast-erfinderische` | Dpmaregister: Schriftsatz-, Brief- und Memo-Bausteine im Patentrecherche. |
| `einstieg-routing` | Einstieg, Triage und Routing für Patentrecherche (FTO, Validity, Family-Watch): ordnet Rolle (Anmelder, Erfinder, Patentanwalt), markiert Frist (Prioritätsjahr 12 Monate), wählt Norm (PatG § 3 Neuheit, § 4 Erfinderischer Schritt, EPÜ Art... |
| `epo-opposition-strategie` | EPO-Einspruch (Opposition) Strategie: 9-Monatsfrist nach Erteilung, Einspruchsgruende Art. 100 EPC, schriftliches Verfahren, muendliche Verhandlung, Beschwerde Boards of Appeal. Beispieltaktiken und Erfolgsfaktoren. Mustertexte für Einsp... |
| `epo-quellenkarte` | Epo Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `epue-beweislast-und-darlegungslast` | Epue: Beweislast, Darlegungslast und Substantiierung im Patentrecherche. |
| `erfinderische-sonderfall-und-edge-case` | Erfinderische: Sonderfall und Edge-Case-Prüfung im Patentrecherche. |
| `erfinderische-taetigkeit-freedom-to-ki-patent` | Prüft erfinderische Tätigkeit nach § 4 PatG und Art. 56 EPUe mit dem Problem-Solution-Approach der EPA-Beschwerdekammern. Drei Stufen: (1) Bestimmung des naechstliegenden Stands der Technik (closest prior art) anhand technischer Naehe Zw... |
| `espacenet-google-neuheit-red-team-korrektur` | Espacenet: Dokumentenmatrix, Lückenliste und Nachforderung im Patentrecherche. |
| `freedom-to-operate-recherche` | Freedom-to-Operate-Recherche (FTO) vor Markteintritt eines konkreten Produkts oder Verfahrens der Mandantin. Sucht **in Kraft befindliche** Patente und Gebrauchsmuster Dritter im Zielmarkt deren Schutzbereich nach § 14 PatG Art. 69 EPUe... |
| `google-risikoampel-und-gegenargumente` | Google: Risikoampel, Gegenargumente und Verteidigungslinien im Patentrecherche. |
| `kaltstart-interview` | Kaltstart-Interview für das Patentrecherche-Plugin. Stellt fest wer recherchiert (Patentanwaeltin Patentanwalt Patentassessor Patentingenieur Recherchekraft) welche Kanzlei und welche Technikgebiete (Mechanik Elektrotechnik Chemie Biotec... |
| `ki-und-patent-strategie` | Spezialfall KI-Erfindungen Patent-Strategie: DABUS-Entscheidungen DPMA und EPA und BPatG, Erfinderbenennung nur natuerliche Person, Beitrag der KI in Beschreibung, Daten- und Modellrechte. Strategie für KI-getriebene FuE und Patent-Portf... |
| `klassifikation-cpc-neuheit-patentfamilien` | CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche müssen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC (Cooperative Patent Class... |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Patentrecherche. |
| `neuheit-pruefen` | Prüft Neuheit nach § 3 PatG und Art. 54 EPUe. Methodisches Schema: ein Anspruch wird in seine Merkmale zerlegt und Merkmal-für-Merkmal gegen genau eine Entgegenhaltung verglichen. Neuheitsschaedlich ist nur die vollständige Vorwegnahme a... |
| `neuheit-red-team-und-qualitaetskontrolle` | Neuheit: Red-Team und Qualitätskontrolle im Patentrecherche. |
| `output-waehlen` | Output-Wahl für Patentrecherche (FTO, Validity, Family-Watch): stimmt Adressat (Anmelder, Erfinder, Patentanwalt), Frist (Prioritätsjahr 12 Monate) und Form auf den Zweck ab — typische Outputs: FTO-Bericht, Validity-Analyse, Stand der Te... |
| `patentanwaelte-patentrecherche-patents` | Patentanwaelte: Tatbestandsmerkmale, Beweisfragen und Beleglage im Patentrecherche. |
| `patentfamilien-analyse` | Patentfamilien-Analyse über INPADOC und Espacenet-Family-View. Sammelt zu einem konkreten Treffer alle Familienmitglieder weltweit DE EP US JP CN KR WO und sonstige Aemter mit gleichem Prioritaetstag. Liefert eine Familientabelle pro Fam... |
| `patentrecherche-erstpruefung-und-mandatsziel` | Patentrecherche: Erstprüfung, Rollenklärung und Mandatsziel im Patentrecherche. |
| `patents-behoerden-gericht-und-registerweg` | Patents: Behörden-, Gerichts- oder Registerweg im Patentrecherche. |
| `patg-problem-register` | Patg: Mandantenkommunikation und Entscheidungsvorlage im Patentrecherche. |
| `patr-fto-bericht-patentfamilie-priodatum` | Leitfaden Freedom-to-Operate-Bericht: Recherchescope, Trefferbewertung, juristische Einordnung, Empfehlungen. Prüfraster für Patentanwalt und Mandant im Patentrecherche. |
| `patr-patentfamilie-priodatum-spezial` | Spezialfall Patentfamilie und Prioritaetsdatum: Pariser Verbandsuebereinkunft, PCT-Schiene, EP-Validierung, Doppelpatentierung. Prüfraster für internationale Familien im Patentrecherche. |
| `patr-recherchestrategie-bauleiter` | Bauleiter Patentrecherche-Strategie: Stichwort- und Klassifikationssuche, IPC und CPC, Volltext und Familien. Prüfraster für Neuheits- und Freedom-to-Operate-Recherche im Patentrecherche. |
| `patr-software-pr-einfuehrung` | Spezialfall Software- und KI-Patentierbarkeit EPA: Computer-implementierte Erfindung, technischer Beitrag, KI-spezifische Prüfrichtlinien. Prüfraster für Anmeldung im Patentrecherche. |
| `pr-einfuehrung-recherchearten` | Einfuehrung Recherchearten Patent: Patentierbarkeitsrecherche, Freedom-to-Operate, State-of-the-Art, Familien-, Rechtsstand-, Konkurrenz-Monitoring. Pro Art: Ziel, Datenquellen (Espacenet, DEPATIS, USPTO, JPO, KIPO), Aufwand, Output. Ent... |
| `problem-abschlussprodukt-und-uebergabe` | Problem: Abschlussprodukt und Übergabe im Patentrecherche. |
| `pruefungsbescheid-vorbereiten` | Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45 PatG oder des EPA nach Art. 94 EPUe systematisch vor. Liest den Bescheid und die zitierten Entgegenhaltungen ein. Strukturiert pro Beanstandung: Beanstandung wortlautgetreu zitiert... |
| `quellen-livecheck` | Quellen-Live-Check für Patentrecherche (FTO, Validity, Family-Watch): prüft Normen (PatG § 3 Neuheit, § 4 Erfinderischer Schritt, EPÜ Art. 54/56, PCT) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt DPMA und Quell... |
| `recherche-strategie-tools-marktuebersicht` | Recherche-Strategie Keywords und Klassifikationen: Boolesche Operatoren, Wildcards, Stopp-Woerter, Variantenpruefung, Trunkierung, Synonyme. CPC und IPC mit Co-Klassen, Klassenwanderung Updates. Strukturierte Vorbereitung von Suchprofile... |
| `recherche-tools-marktuebersicht` | Marktuebersicht Recherche-Tools: kostenlose Quellen (Espacenet, DEPATIS, Google Patents, Lens, USPTO PatFT/AppFT, J-PlatPat), kostenpflichtige (Derwent, Orbit, PatBase, Minesoft, IPCheckUp, Patsnap). Pro Tool: Staerken, Schwaechen, Lizen... |
| `recherchebericht-erstellen` | Formaler Recherchebericht für den Mandanten oder die Akte. Bringt Auftrag Methodik durchsuchte Datenbanken verwendete Suchstrings Klassen Schlagworte Zeitraum Trefferzahlen Treffertabelle und Bewertungen aus Skills neuheit-prüfen erfinde... |
| `register-zahlen-schwellen-und-berechnung` | Register: Zahlen, Schwellenwerte und Berechnung im Patentrecherche. |
| `rueckfragen-mandant` | Generiert Rückfragen an den Mandanten wenn das vorgelegte Material für eine sinnvolle Recherche nicht ausreicht oder Abgrenzungsfragen offen sind. Pflichtfragen: Was ist der wesentliche Lösungsbeitrag der Erfindung gegenüber dem Stand de... |
| `rueckfragen-mandant-depatisnet` | Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR. Liefert Anmeldetag Veröff... |
| `stand-der-technik-recherche` | Recherche Stand der Technik vor eigener Patentanmeldung. Identifiziert anhand des Erfindungsmaterials und der ermittelten CPC-IPC-Klassen die wichtigsten Veröffentlichungen die der Anmeldetag-Reife der Mandantenerfindung im Wege stehen k... |
| `stand-technik-uspto-interessen` | Stand: Internationaler Bezug und Schnittstellen im Patentrecherche. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Patentrecherche-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokumen... |
| `taetigkeit-fristennotiz-agentische-datenbank` | Taetigkeit: Fristennotiz und nächster Schritt im Patentrecherche. |
| `technik-formular-portal-und-einreichung` | Technik: Formular, Portal und Einreichungslogik im Patentrecherche. |
| `ueberwachung-konkurrenten` | Laufende Überwachung neuer Patentanmeldungen von Konkurrenten der Mandantin. Definiert Watch-Profile pro Mandant mit Anmelder-Namen (inklusive Konzern-Toechter und ehemaliger Schreibweisen), CPC-IPC-Klassen, Schlagwoerter, Territorien. L... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Patentrecherche (FTO, Validity, Family-Watch): trennt fehlende Tatsachen von fehlenden Belegen (Erfindungsmeldung, Anspruchssatz, Recherche-Report), nennt pro Lücke Beweisthema, Beschaffungsweg (DPMA), F... |
| `upc-unified-patent-court-spezial` | Unified Patent Court UPC seit 2023 Spezial: Zuständigkeit, Opt-out, Klage- und Nichtigkeitsverfahren, Local und Central Division, Pace und Sprache, Schadensersatz, Bifurcation: Unified Patent Court UPC seit 2023 Spezial: Zuständigkeit, O... |
| `uspto-mehrparteien-konflikt-und-interessen` | USPTO: Mehrparteienkonflikt und Interessenmatrix im Patentrecherche. |
| `wipo-stand-technik-ueberwachung-konkurrenten` | Wipo: Compliance-Dokumentation und Aktenvermerk im Patentrecherche. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Patentrecherche. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Patentrecherche. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Patentrecherche. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
