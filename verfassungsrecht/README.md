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
| **Dr. Ottilie Mondsee und die verschwundene R-Besoldung** (`beamtenrecht-richterlaufbahn-besoldung-mondsee`) | [Gesamt-PDF lesen](../testakten/beamtenrecht-richterlaufbahn-besoldung-mondsee/gesamt-pdf/beamtenrecht-richterlaufbahn-besoldung-mondsee_gesamt.pdf) | [`testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beamtenrecht-richterlaufbahn-besoldung-mondsee.zip) |
| **Verfassungsbeschwerde Klimacamp Initiative Saarbruecken — Art. 8 GG / Versammlungsfreiheit / Bannmeile Landtag** (`verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg`) | [Gesamt-PDF lesen](../testakten/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg/gesamt-pdf/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg_gesamt.pdf) | [`testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Verfassungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. B... |
| `bverfg-rechtsprechung-recherchieren` | BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung durch Folge-Rspr. Outp... |
| `formelle-verfassungsmaessigkeit` | Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG Verfahren Art. 76-78... |
| `gesetzentwurf-gg-konformitaet-pruefen` | Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip... |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung Subsidiaritaet Sperrwirk... |
| `grundrechtspruefung` | Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff Rechtfertigung verfassungsrechtl... |
| `spezial-acht-zahlen-schwellen-und-berechnung` | Acht: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bundesverfassungsgericht-livequellen-check` | Bundesverfassungsgericht: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bverfg-verfahrenssicht-und-annahmerisiko` | BVerfG-Verfahrenssicht, Annahmerisiko und Tenorierungsziel: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-formelle-mehrparteien-konflikt-und-interessen` | Formelle: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gesetzgebungskompetenz-compliance-dokumentation-und-akte` | Gesetzgebungskompetenz: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grundgesetz-fristen-form-und-zustaendigkeit` | Grundgesetz: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grundrechte-red-team-und-qualitaetskontrolle` | Grundrechte: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-grundrechtspruefung-und-verhaeltnismaessigkeit` | Grundrechtsprüfung und Verhältnismäßigkeit: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-live-schriftsatz-brief-und-memo-bausteine` | Live: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-materielle-internationaler-bezug-und-schnittstellen` | Materielle: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-petition-sonderfall-und-edge-case` | Petition: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-recherche-verhandlung-vergleich-und-eskalation` | Recherche: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsprechungsgetrieben-rechtsweg-register` | Rechtsprechungsgetrieben: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sicht-dokumentenmatrix-und-lueckenliste` | Sicht: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-spezialkanzlei-risikoampel-und-gegenargumente` | Spezialkanzlei: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-unter-tatbestand-beweis-und-belege` | Unter: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verfassung-beweislast-und-darlegungslast` | Verfassung: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verfassungsbeschwerde-mandantenentscheidung` | Verfassungsbeschwerde: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verfassungsmaessigkeit-formular-portal-und-einreichung` | Verfassungsmaessigkeit: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verfassungsrecht-erstpruefung-und-mandatsziel` | Verfassungsrecht: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `verfassung-abstrakte-normenkontrolle` | Abstrakte Normenkontrolle Art. 93 Abs. 1 Nr. 2 GG, §§ 76 ff. BVerfGG: Antragsteller (BReg, Landesregierung, ein Viertel BT-Mitglieder), Verfahrensgegenstand Bundes- oder Landesgesetz. Pruefraster. |
| `verfassung-bund-laender-streit` | Bund-Laender-Streit Art. 93 Abs. 1 Nr. 3 GG, §§ 68 ff. BVerfGG: Streitigkeiten Bund/Land oder Land/Land. Pruefraster und Beispiele (Finanzausgleich, Schulrecht, Polizeirecht). |
| `verfassung-grundgesetz-verfahren` | Verfahren der Verfassungsaenderung Art. 79 GG: Zwei-Drittel-Mehrheit BT und BR, Ewigkeitsklausel Art. 79 Abs. 3 GG. Beispiele unzulaessiger Aenderungen. |
| `verfassung-grundrechte-juristische-personen` | Grundrechtsfaehigkeit juristischer Personen Art. 19 Abs. 3 GG: inlaendische jur. Personen, Wesensmaessigkeitsklausel. Beispiele: Wirtschafts-Grundrechte ja, Wuerde nein. Auslaendische jur. Personen jetzt teilweise EuGH-konform anerkannt. |
| `verfassung-grundrechte-uebersicht` | Grundrechte des GG Ueberblick: Art. 1 Wuerde, Art. 2 freie Entfaltung, Art. 3 Gleichheit, Art. 4 Glaubensfreiheit, Art. 5 Meinungsfreiheit, Art. 8 Versammlung, Art. 12 Berufsfreiheit, Art. 14 Eigentum. Schutzbereich, Eingriff, Schranken,... |
| `verfassung-grundrechte-und-eu-recht` | Verhaeltnis GG-Grundrechte und EU-Grundrechtecharta: Solange-II BVerfGE 73 S. 339, Bananenmarkt BVerfGE 102 S. 147, Recht auf Vergessen I sowie II BVerfG 1 BvR 16 aus 13 und 1 BvR 276 aus 17. Pruefraster: Anwendungsbereich Charta vs. GG. |
| `verfassung-konkrete-normenkontrolle` | Konkrete Normenkontrolle Art. 100 Abs. 1 GG, §§ 80 ff. BVerfGG: Vorlage durch Gericht, das Gesetz fuer verfassungswidrig haelt. Vorlagepflicht und Entscheidungserheblichkeit. |
| `verfassung-organstreitverfahren` | Organstreitverfahren Art. 93 Abs. 1 Nr. 1 GG, § 13 Nr. 5, §§ 63 ff. BVerfGG: Antragsteller (Verfassungsorgane, mit eigenen Rechten ausgestattete Teile), Antragsgegenstand Massnahme Verfassungsorgan, Frist 6 Monate. Pruefraster. |
| `verfassung-parteiverbot` | Parteiverbot Art. 21 Abs. 2 GG, § 13 Nr. 2 BVerfGG: Voraussetzungen, NPD-Verfahren BVerfG 2 BvB 1/13. Pruefraster, hohe Schwelle (Potenzialitaet). Ausschluss von staatlicher Finanzierung Art. 21 Abs. 3 GG. |
| `verfassung-petition-und-verfassungsschutz` | Petitionsrecht Art. 17 GG und Verfassungsschutz: Verhaeltnis demokratische Teilhabe und Sicherheitsbehoerden. Beobachtung politischer Parteien und Akteure, Rechtsschutz vor VG. |
| `verfassung-staatsorganisation` | Staatsorganisation des GG: Demokratieprinzip Art. 20, Rechtsstaatsprinzip, Bundesstaatsprinzip, Sozialstaatsprinzip, Republikprinzip. Bundesorgane: BT, BR, BReg, BPraes, BVerfG. Pruefraster Staatsfunktionen. |
| `verfassungsbeschwerde-entwurf` | Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster: Beschwerdeführerbefugnis Beschwerdeobje... |
| `verfassungsrechtliche-pruefung` | Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien Verhältnismäßigkeit E... |
| `verhaeltnismaessigkeit` | Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit Dreistufenprüfung Abwaegu... |
| `vfgr-bundestreue-foederalismus-spezial` | Spezialfall Bundestreue und Foederalismus: ungeschriebener Verfassungsgrundsatz, Pflicht zur Ruecksicht. Pruefraster fuer Bund-Laender-Konflikte und Klagen Karlsruhe. |
| `vfgr-grundrechtspruefung-bauleiter` | Bauleiter Grundrechtspruefung: Schutzbereich, Eingriff, Rechtfertigung, Verhaeltnismaessigkeit. Pruefraster fuer Klausur und Schriftsatz. |
| `vfgr-organstreit-leitfaden` | Leitfaden Organstreit Art. 93 Abs. 1 Nr. 1 GG: Beteiligtenfaehigkeit, Antragsgegenstand, Antragsbefugnis. Pruefraster fuer Bundestagsfraktionen und Abgeordnete. |
| `vfgr-verfassungsbeschwerde-substantiierung-spezial` | Spezialfall Verfassungsbeschwerde Substantiierung § 23, § 92 BVerfGG: Beschwerdebefugnis, Selbst- gegenwaertig- unmittelbar, Rechtswegerschoepfung. Pruefraster fuer Anwalt. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin verfassungsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin verfassungsrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin verfassungsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin verfassungsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin verfassungsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin verfassungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin verfassungsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin verfassungsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin verfassungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin verfassungsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
