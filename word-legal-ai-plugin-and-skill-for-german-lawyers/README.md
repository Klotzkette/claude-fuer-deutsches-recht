# Word Legal AI Plugin and Skill for German Lawyers

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`word-legal-ai-plugin-and-skill-for-german-lawyers`) | [`word-legal-ai-plugin-and-skill-for-german-lawyers.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/word-legal-ai-plugin-and-skill-for-german-lawyers.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Drafting-Werkstatt — Asset-Deal / SPV / Grundstück Volkenrath Energie SE (Share-Deal und Pivot)** (`drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben`) | [Gesamt-PDF lesen](../testakten/drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben/gesamt-pdf/drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben_gesamt.pdf) | [`testakte-drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-drafting-werkstatt-asset-deal-spv-grundstueck-volkenrath-energie-share-deal-und-pivot-anwaltsschreiben.zip) |
| **Falkenried & Partner mbB — Managementakte Q2/2026** (`kanzlei-management-falkenried-partnerkreis-q2-2026`) | [Gesamt-PDF lesen](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) |
| **Akte Auerbach Soundworks / Nordlicht in Beton** (`urheberrecht-musik-ki-songstreit-auerbach`) | [Gesamt-PDF lesen](../testakten/urheberrecht-musik-ki-songstreit-auerbach/gesamt-pdf/urheberrecht-musik-ki-songstreit-auerbach_gesamt.pdf) | [`testakte-urheberrecht-musik-ki-songstreit-auerbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-urheberrecht-musik-ki-songstreit-auerbach.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anspruchsgrundlage-rechtsfolgen-b2b-vs` | Anspruchsgrundlage Und Rechtsfolgen Klauseln, B2b Vs B2c Klausel Strategie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `anwaltsschreiben-aussergerichtlich` | Anwaltsschreiben Aussergerichtlich, Argumentationsarchitektur Schreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `bedingungen-aufschiebend` | Fristen Und Risikoampel, Bedingungen Aufschiebend Aufloesend Fristen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `bilingual-drafting-cowork-cloud` | Bilingual Drafting Deutsch Englisch, Cowork Cloud Kollaboration Drafting: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `bilinguales-writing-englische-vertraege` | Bilinguales Legal Writing, Englische Vertraege Deutsches Recht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `boilerplate-klauseln-definitionen-klauseln` | Boilerplate Klauseln Katalog, Definitionen Klauseln Stringent: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `defensive-drafting-deutscher-kanzleistil` | Defensive Drafting Fallen Erkennen, Deutscher Kanzleistil Kalibrieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `dokumentarchitektur-vertrag-englischer` | Dokumentarchitektur Vertrag Und Schriftsatz, Englischer Vertrag Deutsches Recht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `drafting-prinzipien-finaler-writing` | Drafting Prinzipien Klarheit Bestimmtheit Praezision, Finaler Writing Quality Gate: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `entwurfscheck-aktenabgleich-red-team` | Prueft juristische Entwuerfe gegen Akte, Ziel, Belege, Rechtsstand, Ton und Ausgabezweck. Findet Abweichungen, unbewiesene Behauptungen, fehlende Antraege, schwache Argumente und riskante Formulierungen. |
| `force-majeure-geheimhaltung-nda` | Force Majeure Und Erschwerung 313 Bgb, Geheimhaltung Nda Vertraulichkeit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `german-agb-konforme` | German Fristen Form Und Zustaendigkeit, Agb Konforme Klauseln 305 310 Bgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `gutachten-internes-ip-rechteuebertragung` | Gutachten Memo Internes Drafting, Ip Rechteuebertragung Und Lizenzen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `haftungsausschluss-haftungsbegrenzung` | Haftungsausschluss Und Haftungsbegrenzung, Klageerwiderung Substantiiertes Bestreiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `kaltstart-drafting-kommandocenter` | Kaltstart-Kommandocenter für Word Legal AI. Führt deutsche Anwälte in maximal fünf Fragen vom diffusen Schreibauftrag zum Arbeitsmodus, Stilprofil, Dokumentgerüst, nächster Skill-Kette und erstem verwertbarem Output. Nutzt das Plugin wor... |
| `kaltstart-risikoampel-und-gegenargumente` | Kaltstart: Einstieg und Routing; Risikoampel, Gegenargumente und Verteidigungslinien: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `klage-drafting-mandantenmemo-partner` | Klage Drafting 253 Zpo, Mandantenmemo Und Partner Update: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `klausel-bibliothek-kuendigungsklauseln` | Klausel Bibliothek Katalog, Kuendigungsklauseln Und Vertragsbeendigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `lawyers-legal` | Lawyers Dokumentenmatrix Und Lueckenliste, Legal Tatbestand Beweis Und Belege: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `orientierung-drafting-partner-kommentar` | Orientierung Drafting Triage, Partner Kommentar Umsetzen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `revisions-prozess-ueberarbeiten-richterlesbar` | Revisions Prozess Redlines Comparison, Schriftsatz Ueberarbeiten Richterlesbar: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `term-sheet-vertragsstrafe-bgb` | Term Sheet Zu Vertrag Uebersetzung, Vertragsstrafe 339 Bgb: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `transparenzgebot-bgb-us-uk` | Transparenzgebot 307 Bgb, Us Uk Legal Writing Für Deutsche: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `verweis-querverweis-dokument-finish` | Verweis Und Querverweis Technik, Word Dokument Finish Und Layout: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `word-legal-writing-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `word-legal-writing-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `word-legal-writing-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `word-stil-ton` | Word Erstpruefung Und Mandatsziel, Stil Und Ton Juristische Texte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
