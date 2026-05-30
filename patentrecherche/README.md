# patentrecherche


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **FTO-Recherche Rotorblattheizung — Windsysteme Norderhof AG vs. Vellbruck Energietechnik / EP 3 218 922 B1** (`fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter`) | [Gesamt-PDF lesen](../testakten/fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter/gesamt-pdf/fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fto-recherche-windkraft-rotorblattheizung-windsysteme-norderhof-eppendorfer-stadter.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

> Plugin für **Patentanwältinnen und Patentanwälte**, das Claude Cowork agentisch durch die klassischen Patentdatenbanken führt — Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO. Vorrecherche, **keine amtliche Recherche**.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Patentrecherche (`patentrecherche`, dieses Plugin) | [patentrecherche.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/patentrecherche.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 14 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agentische-datenbank-recherche` | Agentische Patentdatenbank-Recherche: Suchauftrag in natuerlicher Sprache mit Erfindungsmaterial (Anspruchsentwurf, Beschreibung, Skizzen) wird automatisch in Suchstrings für Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Regis... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Patentrecherche-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Be... |
| `erfinderische-taetigkeit-pruefen` | Prüft erfinderische Tätigkeit nach § 4 PatG und Art. 56 EPUe mit dem Problem-Solution-Approach der EPA-Beschwerdekammern. Drei Stufen: (1) Bestimmung des naechstliegenden Stands der Technik (closest prior art) anhand technischer Naehe Zw... |
| `freedom-to-operate-recherche` | Freedom-to-Operate-Recherche (FTO) vor Markteintritt eines konkreten Produkts oder Verfahrens der Mandantin. Sucht **in Kraft befindliche** Patente und Gebrauchsmuster Dritter im Zielmarkt deren Schutzbereich nach § 14 PatG Art. 69 EPUe... |
| `klassifikation-cpc-ipc` | CPC- und IPC-Klassifikation für Patentrecherche bestimmen: Erfindung soll recherchiert werden und Klassen für Datenbanksuche muessen festgelegt werden. Normen: WIPO IPC (International Patent Classification), CPC (Cooperative Patent Class... |
| `neuheit-pruefen` | Prüft Neuheit nach § 3 PatG und Art. 54 EPUe. Methodisches Schema: ein Anspruch wird in seine Merkmale zerlegt und Merkmal-fuer-Merkmal gegen genau eine Entgegenhaltung verglichen. Neuheitsschaedlich ist nur die vollständige Vorwegnahme... |
| `patentfamilien-analyse` | Patentfamilien-Analyse über INPADOC und Espacenet-Family-View. Sammelt zu einem konkreten Treffer alle Familienmitglieder weltweit DE EP US JP CN KR WO und sonstige Aemter mit gleichem Prioritaetstag. Liefert eine Familientabelle pro Fam... |
| `patentrecherche-kaltstart-interview` | Kaltstart-Interview für das Patentrecherche-Plugin. Stellt fest wer recherchiert (Patentanwaeltin Patentanwalt Patentassessor Patentingenieur Recherchekraft) welche Kanzlei und welche Technikgebiete (Mechanik Elektrotechnik Chemie Biotec... |
| `pruefungsbescheid-vorbereiten` | Bereitet Antwort auf Prüfungsbescheid des DPMA nach § 45 PatG oder des EPA nach Art. 94 EPUe systematisch vor. Liest den Bescheid und die zitierten Entgegenhaltungen ein. Strukturiert pro Beanstandung: Beanstandung wortlautgetreu zitiert... |
| `recherchebericht-erstellen` | Formaler Recherchebericht für den Mandanten oder die Akte. Bringt Auftrag Methodik durchsuchte Datenbanken verwendete Suchstrings Klassen Schlagworte Zeitraum Trefferzahlen Treffertabelle und Bewertungen aus Skills neuheit-prüfen erfinde... |
| `rechtsstand-pruefen` | Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR. Liefert Anmeldetag Veröff... |
| `rueckfragen-mandant` | Generiert Rückfragen an den Mandanten wenn das vorgelegte Material für eine sinnvolle Recherche nicht ausreicht oder Abgrenzungsfragen offen sind. Pflichtfragen: Was ist der wesentliche Lösungsbeitrag der Erfindung gegenüber dem Stand de... |
| `stand-der-technik-recherche` | Recherche Stand der Technik vor eigener Patentanmeldung. Identifiziert anhand des Erfindungsmaterials und der ermittelten CPC-IPC-Klassen die wichtigsten Veröffentlichungen die der Anmeldetag-Reife der Mandantenerfindung im Wege stehen k... |
| `ueberwachung-konkurrenten` | Laufende Überwachung neuer Patentanmeldungen von Konkurrenten der Mandantin. Definiert Watch-Profile pro Mandant mit Anmelder-Namen (inklusive Konzern-Toechter und ehemaliger Schreibweisen), CPC-IPC-Klassen, Schlagwoerter, Territorien. L... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
