# Word Legal AI Plugin and Skill for German Lawyers


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Drafting-Werkstatt — Asset-Deal / SPV / Grundstück Volkenrath Energie SE (Share-Deal und Pivot)** (`drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben`) | [Gesamt-PDF lesen](../testakten/drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben/gesamt-pdf/drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

(Technischer Plugin-Slug: `word-legal-ai-plugin-and-skill-for-german-lawyers`. Früherer Name bis v50.6.x: `juristisches-drafting`.)

Generisches Drafting-Plugin für deutsche Anwältinnen, Anwälte und Wirtschaftsjuristen. Es trainiert die Erstellung juristischer Texte – Verträge, Klauseln, Schriftsätze, Anwaltsschreiben, Memos – mit Fokus auf **Struktur, Funktion und sprachliche Präzision**. Optimiert für die Arbeit in Microsoft Word und in Claude Cowork (Cloud).

## Zweck

Juristisches Drafting ist Handwerk. Es lebt von wiederkehrenden Mustern, sauberer Definition, präziser Rechtsfolgenanordnung, robusten Boilerplate-Klauseln und einer Schreibhygiene, die jedem Adressaten – Mandant, Gegenseite, Gericht, Behörde – sofort die Struktur erkennbar macht. Dieses Plugin liefert das Skillset, mit dem Sie:

- **Verträge** vom ersten Term Sheet bis zur unterschriftsreifen Endfassung bauen,
- **Klauseln** dogmatisch sauber, klar und sprachlich ökonomisch formulieren,
- **Schriftsätze** und **Anwaltsschreiben** strukturieren, statt sie auszuschütten,
- **AGB-Risiken** vor der Klausel-Übernahme prüfen,
- **Word-Finish** pragmatisch prüfen, ohne Makro-, VBA- oder Automatisierungsballast,
- **Redlines und Revisions-Workflows** in der Cloud sauber führen,
- **Kanzleistil** bewusst kalibrieren: Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht, Behörde,
- **englische und amerikanische Legal-Texte** schreiben, wenn deutsche Anwältinnen und Anwälte international arbeiten müssen, ohne deutsches Recht in Common-Law-Sprache zu verformen.

Das Plugin enthält bewusst **keinen** Makro-, VBA- oder Word-Automatisierungs-Skill. Es soll beim Schreiben, Prüfen und Finalisieren helfen, nicht zur Office-Programmierung abbiegen.

Das Plugin verzichtet bewusst auf eine fertige Testakte. Es ist ein Werkzeug zum **Üben, Strukturieren und Generieren** – nicht zum Abarbeiten eines vorgegebenen Mandats.

## Adressat

- Rechtsanwältinnen und Rechtsanwälte in Kanzleien (Solo bis Großkanzlei)
- Wirtschaftsjuristinnen und Wirtschaftsjuristen in Rechtsabteilungen
- Notarassessoren, Referendare im Wahlstationsbereich, juristische Berater
- Erfahrene Drafter, die einen Sparringspartner für Struktur und Sprache suchen

Voraussetzung: deutsche juristische Grundausbildung; das Plugin erklärt **Drafting-Technik**, nicht das materielle Recht.

## Aufbau

Das Plugin gliedert sich in acht Skill-Blöcke:

### Block A – Grundlagen des Drafting

- `kaltstart-drafting-kommandocenter` – Schöner Kaltstart vom diffusen Schreibauftrag zur Skill-Kette und zum ersten Output.
- `orientierung-drafting-triage` – Welcher Skill für welches Dokument? Triage am Anfang jedes Mandats.
- `drafting-prinzipien-klarheit-bestimmtheit-praezision` – Die drei Leitwerte und ihre Umsetzung.
- `dokumentarchitektur-vertrag-und-schriftsatz` – Architektur statt Bauchgefühl.
- `stil-und-ton-juristische-texte` – Schreibhygiene, Adressatengerechtigkeit, Register.
- `deutscher-kanzleistil-kalibrieren` – Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht, Behörde oder US/UK-Korrespondenz.

### Block B – Klausel-Technik

- `definitionen-klauseln-stringent` – Defined Terms, Hierarchie, Konsistenz.
- `boilerplate-klauseln-katalog` – Salvatorische, Schriftform, Gerichtsstand, Rechtswahl.
- `anspruchsgrundlage-und-rechtsfolgen-klauseln` – Tatbestand und Rechtsfolge sauber trennen.
- `haftungsausschluss-und-haftungsbegrenzung` – Drafting nach §§ 276 III, 309 Nr. 7, 444 BGB.
- `bedingungen-aufschiebend-aufloesend-fristen` – Konditionalstruktur ohne Schleifen.
- `verweis-und-querverweis-technik` – Interne Verweise, Anlagen, Querverweisarchitektur.

### Block C – Spezielle Klauseln

- `vertragsstrafe-339-bgb` – Wirksamkeit, Höhe, Verhältnis zum Schadensersatz.
- `kuendigungsklauseln-und-vertragsbeendigung` – Ordentlich, außerordentlich, Schriftform.
- `geheimhaltung-nda-vertraulichkeit` – Stand-alone NDA und Klauselbaustein.
- `force-majeure-und-erschwerung-313-bgb` – Höhere Gewalt vs. Geschäftsgrundlage.
- `ip-rechteuebertragung-und-lizenzen` – Übertragung, Einräumung, Sub-Lizenz, Rückrufrechte.

### Block D – AGB-Recht

- `agb-konforme-klauseln-305-310-bgb` – Einbeziehung, Inhaltskontrolle, Klauselverbote.
- `transparenzgebot-307-bgb` – Verständlichkeit als Wirksamkeitsvoraussetzung.
- `b2b-vs-b2c-klausel-strategie` – Zwei Vertragswelten, ein Klauselwerk.

### Block E – Schriftsatz-Drafting

- `klage-drafting-253-zpo` – Antrag, Sachverhalt, Rechtliches, Beweisangebote.
- `klageerwiderung-substantiiertes-bestreiten` – Bestreitenshöhe, Gegenangriff, Hilfsanträge.
- `anwaltsschreiben-aussergerichtlich` – Erste Brief, Mahnung, Vergleichsangebot.
- `gutachten-memo-internes-drafting` – Sachverhalt – Frage – Kurzantwort – Bewertung – Ergebnis.

### Block F – Cowork, Revision und Versand

- `cowork-cloud-kollaboration-drafting` – Mandantengeheimnis-konformes Arbeiten in der Cloud.
- `revisions-prozess-redlines-comparison` – Compare-Doc, Markup, Versionierung.
- `word-dokument-finish-und-layout` – Versandfähige Endkontrolle in Word/PDF/beA ohne Makro- oder VBA-Workflow.

### Block G – Verhandlung und Klauselbibliothek (neu in v50.6.0)

- `defensive-drafting-fallen-erkennen` – Zwölf typische Fallen in Gegenseitenentwürfen mit Roten-Flaggen-Wortlisten und Verteidigungsformulierungen.
- `term-sheet-zu-vertrag-uebersetzung` – Mapping-Tabelle Term-Sheet-Position → Vertragsklausel, zwölf typische Term-Sheet-Lücken, Mandantenmemo-Vorlage.
- `bilingual-drafting-deutsch-englisch` – Drei Use Cases (zwei Sprachfassungen, Glossar, parallele Spalten), False-Friends-Tabelle DE-EN, Maßgeblichkeits-Klausel.
- `klausel-bibliothek-katalog` – Über 60 fertige Bausteine mit B2B/B2C-Ampel, AGB-Risiko und bilingualer Variante. Quelle: `references/klausel-bibliothek.md`.

### Block H – Kanzlei-Schreibworkflow und internationale Texte (neu in v50.8.0)

- `partner-kommentar-umsetzen` – Partnerkommentare und Randnotizen in konkrete Drafting-Schritte und neue Passagen übersetzen.
- `mandantenmemo-und-partner-update` – Mandantenmemo, Partner-Update und Management Note mit Executive Summary, Empfehlung und Risikoampel.
- `argumentationsarchitektur-schreiben` – These, Norm, Tatsache, Beleg, Gegenargument und Rechtsfolge tragfähig ordnen.
- `schriftsatz-ueberarbeiten-richterlesbar` – Schriftsätze richterlesbar machen: Anträge, Ergebnisüberschriften, Beweise, Anlagen, Ton.
- `us-uk-legal-writing-fuer-deutsche` – Englische und amerikanische Legal-Texte aus deutscher Anwaltsperspektive schreiben.
- `englischer-vertrag-deutsches-recht` – Englischsprachige Verträge mit deutschem Recht, ohne versehentlichen Common-Law-Import.
- `finaler-writing-quality-gate` – Letzte Freigabeampel vor Versand: Recht, Stil, Namen, Fristen, Anlagen, Word, Metadaten.

## Asset-Datei

- `references/klausel-bibliothek.md` – Klauselbibliothek mit über 60 Bausteinen, gegliedert in 25 Bereiche (Präambel bis Audit-Recht), je mit Verwendungshinweis, AGB-Ampel, mild/scharf-Variante und englischer Fassung.

## Methodischer Rahmen

- **Standardstil:** Urteilsstil für operative Klauseln und Schriftsätze; Gutachtenstil ausschließlich in internen Memos und Gutachten.
- **Sprache:** Deutsch, Sie-Form. Englische Begriffe nur, wenn etabliert (Letter of Intent, Term Sheet, Due Diligence, Discovery) und kurz erklärt.
- **Quellen:** Belegpflicht nach `references/zitierweise.md`. Keine Präjudizienbindungs-Argumentation. Rechtsprechung mit Gericht, Datum, Aktenzeichen, Fundstelle.
- **Mandantengeheimnis:** § 43a II BRAO, § 203 StGB. Keine Mandantendaten in Tools ohne Auftragsverarbeitungsvertrag.

## Installation

| Plugin | Direkt-Download |
| --- | --- |
| Word Legal AI Plugin and Skill for German Lawyers (`word-legal-ai-plugin-and-skill-for-german-lawyers`, dieses Plugin) | [word-legal-ai-plugin-and-skill-for-german-lawyers.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/word-legal-ai-plugin-and-skill-for-german-lawyers.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

## Verwendung

Aktivieren Sie das Plugin `word-legal-ai-plugin-and-skill-for-german-lawyers` in Claude Code oder Cowork. Die Skills sind über ihre Namen direkt ansprechbar (zum Beispiel `definitionen-klauseln-stringent`). Beginnen Sie bei diffusen Schreibaufträgen mit `kaltstart-drafting-kommandocenter`; bei bereits erkennbarem Dokumenttyp mit `orientierung-drafting-triage`. Beide Skills leiten in die passenden Spezial-Skills weiter.

## Lizenz

Apache-2.0 OR MIT. Siehe `LICENSE-APACHE` und `LICENSE-MIT` im Repository-Wurzelverzeichnis.

## Hinweis zur Versionierung

Dieses Plugin folgt der einheitlichen Versionierung des Repositories `claude-fuer-deutsches-recht`. Die aktuelle Version steht in `.claude-plugin/plugin.json`.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 38 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agb-konforme-klauseln-305-310-bgb` | Drafting und Prüfung von Allgemeinen Geschäftsbedingungen nach §§ 305-310 BGB. Klärt den AGB-Begriff (vorformuliert, mehrfach verwendet, gestellt), Einbeziehung im Verbraucher- und Unternehmergeschäft sowie Inhaltskontrolle nach § 307 BG... |
| `anspruchsgrundlage-und-rechtsfolgen-klauseln` | Vertragliche Klauseln nach der Wenn-Dann-Architektur bauen. Klare Trennung von Tatbestand (Wenn-Teil mit Voraussetzungen) und Rechtsfolge (Dann-Teil mit Pflichten und Fristen). Anwendungsbeispiele: Maengelhaftung Verzugsklausel Kuendigun... |
| `anwaltsschreiben-aussergerichtlich` | Außergerichtliches Anwaltsschreiben in drei Spielarten: erster anwaltlicher Brief, Mahnschreiben nach § 286 BGB mit Verzugsbegründung und Vergleichsangebot. Aufbau: Mandantenbezug; Vollmachtnachweis; knapper Sachverhalt; Anspruch oder Fo... |
| `argumentationsarchitektur-schreiben` | Baut die Argumentationsarchitektur für Schriftsatz, Memo oder Verhandlungsposition. Ordnet These, Norm, Tatsache, Beleg, Gegenargument, Antwort und Ergebnis. Erkennt Sprünge, verdeckte Prämissen, fehlende Beweisangebote und unklare Recht... |
| `b2b-vs-b2c-klausel-strategie` | Strategisches Drafting in zwei Vertragswelten. B2C unter strengem Verbraucherschutz (§§ 13 und 14 BGB sowie § 305 II BGB und §§ 308 und 309 BGB direkt anwendbar). B2B im Geschäftsverkehr nach § 310 I BGB erleichtert, aber mit Ausstrahlun... |
| `bedingungen-aufschiebend-aufloesend-fristen` | Konditionalstruktur in Vertraegen sauber bauen. § 158 BGB: aufschiebende Bedingung (Eintritt bei Eintritt) vs aufloesende Bedingung (Wegfall bei Eintritt). Potestativbedingung. Closing Conditions in M&A mit Signing/Closing-Logik. Long St... |
| `bilingual-drafting-deutsch-englisch` | Drafting deutsch-englischer Vertraege in Side-by-Side- oder Stacked-Layout. Bestimmt den Anwendungsfall (true bilingual, sovereign language, courtesy translation), waehlt das Layout (Tabelle zweispaltig oder gestapelte Saetze), klaert di... |
| `boilerplate-klauseln-katalog` | Katalog typischer Boilerplate-Klauseln im deutschen Wirtschaftsvertrag mit Wirksamkeitsanalyse und Mustertexten. Behandelt salvatorische Klausel (BGH-kritisch nach § 139 BGB), Schriftformklausel inklusive doppelter Schriftformklausel, Ge... |
| `cowork-cloud-kollaboration-drafting` | Mandantengeheimnis-konformes Drafting in der Cloud (Claude Cowork; Office 365; Google Workspace). Rechtlicher Rahmen § 43a Abs. 2 BRAO; § 203 StGB; § 26 BORA und Art. 28 DSGVO. Auftragsverarbeitungsvertrag ist Voraussetzung. Sensible Dat... |
| `defensive-drafting-fallen-erkennen` | Defensives Drafting beim Review fremder Entwuerfe. Erkennt die zwoelf haeufigsten Fallen: kaschierte Haftungsfreistellung, verschobene Beweislast, einseitiger Gerichtsstand, unfaire Aenderungsvorbehalte, kurze Verjaehrungsverkuerzung, Na... |
| `definitionen-klauseln-stringent` | Defined Terms in Vertraegen sauber bauen. Hierarchie und Konsistenz: einmal definieren, im gesamten Dokument einheitlich verwenden, mit Grossschreibung sichtbar machen. Trennung zwischen zentralem Definitionen-Abschnitt (alphabetisch) un... |
| `deutscher-kanzleistil-kalibrieren` | Kalibriert juristische Texte auf den passenden deutschen Kanzleistil: Frankfurter Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht oder Behörde. Erstellt ein Stilprofil mit Ton, Satzlänge, Gliederung, Anrede, Risikoniveau, Schärfegr... |
| `dokumentarchitektur-vertrag-und-schriftsatz` | Dokumentarchitektur juristischer Texte sauber bauen. Vertrag mit Rubrum/Parteien, Praeambel, Definitionen, Hauptleistungspflichten, Nebenpflichten, Bedingungen, Beendigung, Boilerplate, Anlagen. Schriftsatz nach § 253 Abs. 2 ZPO mit Rubr... |
| `drafting-prinzipien-klarheit-bestimmtheit-praezision` | Die drei Leitwerte juristischen Drafting sauber operationalisieren. Klarheit (Adressat versteht), Bestimmtheit (Subsumtion moeglich; § 253 Abs. 2 Nr. 2 ZPO; AGB-Transparenzgebot § 307 Abs. 1 Satz 2 BGB) und Praezision (kein ueberfluessig... |
| `englischer-vertrag-deutsches-recht` | Draftet oder prüft englischsprachige Verträge mit deutschem Recht als anwendbarem Recht. Verhindert ungewollten Import von Common-Law-Konzepten, klärt governing language, German-law concepts, Gewährleistung, Garantie, Haftung, Indemnity,... |
| `finaler-writing-quality-gate` | Finales Quality Gate für juristische Texte vor Versand. Prüft Rechtsfrage, Antrag oder Klauselzweck, Adressat, Stil, Zitate, Normen, Anlagen, Beweise, Fristen, Platzhalter, Zahlen, Namen, Datenschutz, Metadaten, Word-Hygiene und Versandf... |
| `force-majeure-und-erschwerung-313-bgb` | Drafting und Abgrenzung von Force-Majeure-Klauseln und § 313 BGB (Wegfall der Geschäftsgrundlage). Strukturiert Definition höherer Gewalt, Anzeigepflicht, Suspendierung der Leistungspflicht und Kaskade bis zur Long-Stop-Kündigung. Klärt... |
| `geheimhaltung-nda-vertraulichkeit` | Drafting eines stand-alone NDA und einer Geheimhaltungsklausel als Vertragsbaustein. Strukturiert Definition der vertraulichen Information, Standardausnahmen (öffentlich bekannt, eigenständig entwickelt, von Dritten rechtmäßig erhalten,... |
| `gutachten-memo-internes-drafting` | Internes Memo und Gutachten im Gutachtenstil. Standardstruktur: Sachverhalt knapp; Frage(n); Kurzantwort in einem Satz; rechtliche Bewertung im Gutachtenstil; Gesamtergebnis; Risiken und offene Punkte; Quellenverzeichnis. Anspruchsgrundl... |
| `haftungsausschluss-und-haftungsbegrenzung` | Haftungsklauseln im deutschen Recht sauber bauen. Pflichtgrenzen § 276 Abs. 3 BGB (Vorsatz nie ausschliessbar), § 309 Nr. 7 BGB (AGB-Klauselverbote fuer Vorsatz grobe Fahrlaessigkeit Kardinalpflichten Koerperschaden), § 444 BGB (arglisti... |
| `ip-rechteuebertragung-und-lizenzen` | Drafting von IP-Klauseln. Urheberrecht (UrhG) kennt keine vollständige Übertragung des Stammrechts (§ 29 UrhG); zulässig ist nur die Einräumung von Nutzungsrechten als einfache oder ausschließliche Lizenz mit räumlicher, zeitlicher und i... |
| `kaltstart-drafting-kommandocenter` | Kaltstart-Kommandocenter für Word Legal AI. Führt deutsche Anwälte in maximal fünf Fragen vom diffusen Schreibauftrag zum Arbeitsmodus, Stilprofil, Dokumentgerüst, nächster Skill-Kette und erstem verwertbarem Output. Nutzt das Plugin wor... |
| `klage-drafting-253-zpo` | Drafting einer Klageschrift nach § 253 Abs. 2 ZPO. Bestimmter Antrag plus Sachverhaltsdarstellung mit Rechtsschutzbegehren und Streitgegenstand. Aufbau: Rubrum (Parteien, Vertretung, Anschriften, Gericht), Anträge (Zahlung, Feststellung,... |
| `klageerwiderung-substantiiertes-bestreiten` | Drafting einer Klageerwiderung mit korrekter Bestreitenshöhe nach § 138 ZPO. Wahrheits- und Substantiierungslast als Drafting-Treiber. Unterscheidung zwischen einfachem Bestreiten und substantiiertem Bestreiten mit Behauptung des Gegente... |
| `klausel-bibliothek-katalog` | Klauselbibliothek mit ueber 60 fertigen Bausteinen fuer deutsche Wirtschaftsvertraege. Sortiert nach Bereichen: Praeambel Definitionen Leistung Verguetung Verzug Gewaehrleistung Haftung Kuendigung Vertragsstrafe Force Majeure Geheimhaltu... |
| `kuendigungsklauseln-und-vertragsbeendigung` | Drafting und Prüfung von Kündigungsklauseln. Ordentliche Kündigung mit Frist und Form, außerordentliche Kündigung aus wichtigem Grund nach § 314 BGB mit Abmahnung und Frist nach Kenntnis, Zugang nach § 130 BGB sowie Form nach §§ 126 (Sch... |
| `mandantenmemo-und-partner-update` | Erstellt Mandantenmemos, Partner-Updates und Management Notes aus juristischer Prüfung. Liefert Executive Summary, klare Empfehlung, Risikoampel, Entscheidungsoptionen, offene Punkte, Fristen und nächste Schritte. Vermeidet Lehrbuch-Guta... |
| `orientierung-drafting-triage` | Einstiegs- und Triage-Skill für juristisches Drafting. Klärt Dokumenttyp, Stadium, Adressat, Stilprofil, Sprachraum und Risiko, erstellt eine Mandatsmatrix und verweist auf die einschlägigen Spezial-Skills im Plugin word-legal-ai-plugin-... |
| `partner-kommentar-umsetzen` | Setzt knappe Partnerkommentare und Randnotizen in echte Drafting-Schritte um. Übersetzt Hinweise wie bitte schärfen, zu lang, commercial, mehr Druck, weniger Gutachten, US counsel fragt, in eine Änderungsliste, priorisiert die Arbeit und... |
| `revisions-prozess-redlines-comparison` | Markup-Workflow zwischen Parteien. Compare-Doc-Funktion erzeugt aus zwei Versionen ein Redline-Dokument. Konventionen: Einfügungen in Rot und unterstrichen; Streichungen in Rot und durchgestrichen; Kommentare am Rand. Versionierung v0 ei... |
| `schriftsatz-ueberarbeiten-richterlesbar` | Überarbeitet Schriftsätze so, dass Richterinnen und Richter sie schnell erfassen können. Prüft Antrag, Streitgegenstand, Ergebnisüberschriften, Sachverhaltschronologie, Beweisangebote, Substantiierung, Anlagenverweise, Ton und Länge. Lie... |
| `stil-und-ton-juristische-texte` | Adressatengerechte Schreibhygiene fuer juristische Texte. Bestimmt Register und Ton je nach Adressat: Mandantenbrief klar und mit Empfehlung, Gegenseitenbrief kuehl und mit Frist, Schriftsatz urteilsstil und beweisbar, Memo gutachtenstil... |
| `term-sheet-zu-vertrag-uebersetzung` | Uebersetzung eines Term Sheets oder Letter of Intent in einen ausgearbeiteten Vertrag. Identifiziert die typischen Term-Sheet-Punkte (Parteien Praeambel Leistung Verguetung Laufzeit Kuendigung Gewaehrleistung Haftung Geheimhaltung Recht... |
| `transparenzgebot-307-bgb` | Drafting nach dem Transparenzgebot des § 307 I S. 2 BGB. Eine inhaltlich zulässige Klausel ist gleichwohl unwirksam, wenn sie nicht klar und verständlich ist. Maßstab ist der durchschnittliche Vertragspartner ohne Spezialwissen. Indizien... |
| `us-uk-legal-writing-fuer-deutsche` | Hilft deutschen Anwälten, englische oder amerikanische Legal-Texte zu schreiben, ohne deutsch zu übersetzen. Klärt US/UK-Adressat, Common-Law-Erwartung, deutsches Recht als Inhalt, Local-Counsel-Rolle, Ton, Struktur, Risk Note, Clause No... |
| `vertragsstrafe-339-bgb` | Drafting und Prüfung von Vertragsstrafeklauseln nach §§ 339-345 BGB. Klärt Bestimmtheit der zu sichernden Hauptverbindlichkeit, Verschuldenserfordernis, Höhe und Verhältnismäßigkeit, Verhältnis zum Schadensersatz (§ 340 BGB Erfüllung sta... |
| `verweis-und-querverweis-technik` | Verweis- und Querverweistechnik in juristischen Dokumenten. Interne Verweise auf Klauseln und Anlagen, externe Verweise auf Gesetze und Urteile. Anlagenverwaltung: jede Anlage einmal benannt, einmal definiert, einmal eingeführt. Vorstehe... |
| `word-dokument-finish-und-layout` | Finalisiert juristische Word-Dokumente vor Versand. Prüft Formatvorlagen, Nummerierung, Inhaltsverzeichnis, Querverweise, Anlagen, Track Changes, Kommentare, Metadaten, PDF/beA-Tauglichkeit, Unterschriftenblock, Tabellen, Seitenumbrüche... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
