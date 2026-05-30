# verfassungsrecht



<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verfassungsrecht`) | [`verfassungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verfassungsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte: Verfassungsbeschwerde Klimacamp Initiative Saarbruecken — Art. 8 GG / Versammlungsfreiheit / Bannmeile Landtag** (`verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg`) | [Gesamt-PDF lesen](../testakten/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg/gesamt-pdf/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg_gesamt.pdf) | [`testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Verfassungsbeschwerde Klimacamp Initiative Saarbruecken — Art. 8 GG / Versammlungsfreiheit / Bannmeile Landtag** (`verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg`) | [Gesamt-PDF lesen](../testakten/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg/gesamt-pdf/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Deutsches Verfassungsrecht unter dem Grundgesetz aus der Sicht einer verfassungsrechtlichen Spezialkanzlei. **Rechtsprechungsgetrieben** mit verpflichtender Live-Recherche auf [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) und einem internen Kanon der ca. 50 wichtigsten Leitentscheidungen mit Aktenzeichen, Randnummer und URL.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Verfassungsrecht (`verfassungsrecht`, dieses Plugin) | [verfassungsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verfassungsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Wofür

- Prüfung, ob ein Gesetz vom **zuständigen Gesetzgeber** erlassen wurde (Art. 70–74 GG).
- Prüfung der **formellen Verfassungsmäßigkeit** (Verfahren Art. 76–82 GG, Zitiergebot Art. 19 I 2 GG, Bestimmtheitsgebot, Wesentlichkeitstheorie/Parlamentsvorbehalt).
- Prüfung der **materiellen Verfassungsmäßigkeit** der Grundrechte (Schutzbereich, Eingriff, verfassungsrechtliche Rechtfertigung mit Verhältnismäßigkeit).
- Begleitung im konkreten Mandat: Verfassungsbeschwerde nach § 90 BVerfGG, Stellungnahmen, Gutachten.
- Begleitung des Gesetzgebers: GG-Konformitätscheck eines Entwurfs vor Einbringung.

## Disclaimer

Verfassungsrecht ist ein hochspezialisiertes Rechtsgebiet mit existentiellen Folgen für Mandanten und Allgemeinheit. Die Ausgaben dieses Plugins sind **kein Ersatz** für die anwaltliche Mandatsbearbeitung durch eine verfassungsrechtliche Spezialkanzlei. Insbesondere Verfassungsbeschwerden unterliegen strengen Zulässigkeits­anforderungen und Fristen (§§ 90 ff. BVerfGG, § 93 BVerfGG).

## Skills

- **`bverfg-rechtsprechung-recherchieren`** — Live-Recherche auf bundesverfassungsgericht.de plus Kanon-Referenz (Az., Rn., URL). Verbindlicher Einstiegspunkt vor jeder verfassungsrechtlichen Aussage.
- **`verfassungsrechtliche-pruefung`** — Master-Workflow: Gesamtschema formelle + materielle Verfassungsmäßigkeit.
- **`gesetzgebungskompetenz-pruefen`** — Art. 70–74 GG, ausschließliche/konkurrierende/Rahmen, Erforderlichkeitsklausel Art. 72 II GG.
- **`formelle-verfassungsmaessigkeit`** — Verfahren Art. 76–82 GG (drei Lesungen, Bundesrat, Ausfertigung), Zitiergebot Art. 19 I 2 GG, Bestimmtheitsgebot, Wesentlichkeitstheorie/Parlamentsvorbehalt.
- **`grundrechtspruefung`** — Schutzbereich-Eingriff-Rechtfertigung mit Drei-Stufen-Theorie (Apothekenurteil), Schranken-Schranken, Wechselwirkungslehre (Lüth).
- **`verhaeltnismaessigkeit`** — Vier-Stufen-Prüfung: legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit, jeweils mit BVerfG-Pinpoint.
- **`verfassungsbeschwerde-entwurf`** — § 90 BVerfGG: Beschwerdebefugnis, Rechtswegerschöpfung, Subsidiarität, Begründungsanforderungen, Frist.
- **`gesetzentwurf-gg-konformitaet-pruefen`** — Gesetzgeber-/Ministeriumssicht: GG-Check vor Einbringung des Entwurfs.

## Referenzen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenstrategie

1. **Primär:** Live-Suche auf [www.bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) (offizielle Entscheidungssammlung). Zitat immer mit Aktenzeichen, Randnummer und URL.
2. **Sekundär:** Eigene Kanon-Referenz unter `references/bverfg-leitentscheidungen.md` als Schnellzugriff.
3. **Ersatzweise:** [servat.unibe.ch/dfr/](https://www.servat.unibe.ch/dfr/) (DFR-Volltextsammlung BVerfGE), [opinioiuris.de](https://opinioiuris.de), [dejure.org](https://dejure.org) — nur wenn auf bundesverfassungsgericht.de nicht greifbar.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Jede verfassungsrechtliche Aussage benötigt eine BVerfG-Pinpoint-Quelle (Az. + Rn.). Modellwissen ohne Quelle wird als `[zu verifizieren auf bundesverfassungsgericht.de]` markiert.

## Hinweis zum berufsrechtlichen Rahmen (Stand Mai 2026)

Anwältinnen und Anwälte sind nach **§ 203 StGB** (Verletzung von Privatgeheimnissen) und **§ 43a BRAO** (anwaltliche Verschwiegenheitspflicht) zur Verschwiegenheit verpflichtet. Eine unmittelbare Weitergabe mandatsbezogener Daten an außereuropäische KI-Anbieter ohne datenschutzkonformes Setup ist berufsrechtlich riskant und kann strafrechtliche Folgen haben. Deshalb empfiehlt sich der Betrieb über einen **deutschen Zwischenanbieter** (z. B. § 203-konformes Cowork-Setup; siehe [README im Repo-Root](../README.md#einrichtungsleitfaden-fuer--203-konformes-cowork-ueber-deutschen-zwischenanbieter)), der als Auftragsverarbeiter nach Art. 28 DSGVO eingebunden ist und die Weiterleitung an den KI-Anbieter pseudonymisiert/anonymisiert handhabt.

**Disclaimer:** technische, **keine juristische** Auskunft; die Tool-Landschaft entwickelt sich seit Frühjahr 2026 sehr dynamisch. Die berufsrechtlichen Pflichten nach § 203 StGB und § 43a BRAO bleiben in jedem Fall in der Verantwortung der jeweiligen Anwältin / des jeweiligen Anwalts.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Verfassungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. B... |
| `bverfg-rechtsprechung-recherchieren` | BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Outp... |
| `formelle-verfassungsmaessigkeit` | Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG Verfahren Art. 76-78... |
| `gesetzentwurf-gg-konformitaet-pruefen` | Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip... |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung Subsidiaritaet Sperrwirk... |
| `grundrechtspruefung` | Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff Rechtfertigung verfassungsrechtl... |
| `verfassungsbeschwerde-entwurf` | Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster: Beschwerdeführerbefugnis Beschwerdeobje... |
| `verfassungsrechtliche-pruefung` | Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien Verhältnismäßigkeit E... |
| `verhaeltnismaessigkeit` | Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit Dreistufenprüfung Abwaegu... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
