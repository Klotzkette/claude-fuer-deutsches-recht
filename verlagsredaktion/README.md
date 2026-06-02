# Verlagsredaktion

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verlagsredaktion`) | [`verlagsredaktion.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verlagsredaktion.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verlagsredaktion Morgenlage Fachverlag** (`verlagsredaktion-morgenlage-fachverlag`) | [Gesamt-PDF lesen](../testakten/verlagsredaktion-morgenlage-fachverlag/gesamt-pdf/verlagsredaktion-morgenlage-fachverlag_gesamt.pdf) | [`testakte-verlagsredaktion-morgenlage-fachverlag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsredaktion-morgenlage-fachverlag.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Verlagsredaktion Morgenlage Fachverlag** (`verlagsredaktion-morgenlage-fachverlag`) | [Gesamt-PDF lesen](../testakten/verlagsredaktion-morgenlage-fachverlag/gesamt-pdf/verlagsredaktion-morgenlage-fachverlag_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsredaktion-morgenlage-fachverlag.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Ein Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskriptaufnahme, Redaktion, Rechtecheck, Zitat- und Fundstellenkontrolle, Autor:innenkommunikation, Heftplanung, Buchprojektsteuerung, Satzfahnen, Metadaten, Marketingtexte, Produktionsübergabe und Qualitätstor.

Der erste Bildschirm soll sich für eine Sachbearbeiterin so anfühlen: Alles liegt durcheinander im Postfach, aber das Plugin macht daraus sofort eine Morgenlage, eine Prioritätenliste und den nächsten verwendbaren Arbeitsschritt.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Verlagsredaktion (`verlagsredaktion`) | [verlagsredaktion.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verlagsredaktion.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Verlagsredaktion Morgenlage Fachverlag** ([`testakten/verlagsredaktion-morgenlage-fachverlag/`](../testakten/verlagsredaktion-morgenlage-fachverlag/)).

Direkt-Download als ZIP: [testakte-verlagsredaktion-morgenlage-fachverlag.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsredaktion-morgenlage-fachverlag.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `verlagsredaktion.zip` hochladen.

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `references/` enthalten.

## Was das Plugin gut können soll

- Aus einer unordentlichen Inbox eine Tagesübersicht machen.
- Manuskripte, Diktate, Folien, Screenshots, Tabellen und Autor:innenmails inventarisieren.
- Rohmanuskripte als Anschubhilfe erstellen, ohne fremde Texte zu kopieren.
- Vorhandene Texte strukturieren, kürzen, glätten und auf Widersprüche prüfen.
- Zitate, Fundstellen, Randnummern und Quellenstatus transparent markieren.
- Rechtefragen zu UrhG, Verlagsgesetz, Bildrechten, Tabellen und Fremdmaterialien als Ampel vorbereiten.
- Autor:innen freundlich, knapp und verbindlich anschreiben.
- Heft-, Buch- und Online-First-Workflows in Aufgaben und Fristen übersetzen.
- Klappentexte, Vorschauen, Metadaten und Marketingtexte aus dem Manuskript ableiten.
- Satzfahnen und Korrekturläufe steuern.
- KI-Einsatz, Datenschutz und Vertraulichkeit konservativ dokumentieren.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Cooler Einstieg, stummer Upload, Morgenlage und Skill-Routing. |
| `sachbearbeiterinnen-cockpit` | Persönliches Arbeitscockpit für Sachbearbeitung, Redaktion und Herstellung. |
| `eingangskorb-triage` | Mails, Dateien, Screenshots und Fristen in Prioritäten verwandeln. |
| `projektplan-fristen-heftplanung` | Projektplan für Heft, Online-Beitrag, Buchkapitel oder Kommentarupdate. |
| `manuskriptaufnahme-materialinventar` | Materialinventar mit Herkunft, Nutzbarkeit, Lücken und Rechteampel. |
| `verlagsredaktion` | Klassischer Rohmanuskript-/Editionsassistent. |
| `rohmanuskript-anschubhilfe` | Aus Material ein erstes, klar markiertes Rohmanuskript bauen. |
| `lektorat-struktur-redaktion` | Gliederung, Dramaturgie, Kürzung, Redundanz- und Widerspruchsprüfung. |
| `sprachlektorat-stil-tonalitaet` | Ton, Satzbau, Lesbarkeit, Verlagssprache, Zielgruppe. |
| `quellen-zitate-fundstellencheck` | Zitat- und Quellenhygiene ohne erfundene Literatur. |
| `rechtecheck-urhg-verlg` | Urheberrecht, Verlagsgesetz, Nutzungsrechte, Zitatrecht und Zweitveröffentlichung. |
| `bildrechte-grafiken-tabellen` | Bilder, Screenshots, Tabellen, Grafiken, Diagramme und Credits prüfen. |
| `fremdtext-plagiat-uebernahmecheck` | Fremdtext, KI-Text, Copy-Paste und Paraphrase-Risiken markieren. |
| `autorenkommunikation-email` | Autor:innenmails, Erinnerungen, Freigaben, Nachforderungen. |
| `honorar-vertrag-royalties-triage` | Vertrags-/Honorar-/Royalty-Fragen für redaktionelle Vorprüfung. |
| `metadaten-seo-klappentext` | Titel, Untertitel, Abstract, Schlagworte, VLB-/Web-Metadaten, Klappentext. |
| `zeitschriften-heftplanung` | Hefte, Rubriken, Deadlines, Online-first, Fahnen und Umbruch koordinieren. |
| `buchprojekt-kapitelkoordination` | Kapitel, Autor:innen, Register, Abbildungen, Vorwort und Produktionsstand. |
| `kommentar-aktualisierung-randnummern` | Kommentarupdates, Randnummern, Nachweise, Rechtsstandsvermerk. |
| `entscheidungsmonitor-rechtsstand` | Entscheidungen und Gesetzesänderungen als Aktualisierungsanlass erfassen. |
| `satzfahne-korrekturlauf` | Fahnenprüfung, Korrekturzeichen, Umbruch, Freigabe und letzte Checks. |
| `barrierefreiheit-epub-pdf` | Alt-Texte, Überschriftenlogik, Tabellenzugänglichkeit, EPUB/PDF-Check. |
| `marketing-presse-social` | Vorschau, Newsletter, Social Copy, Presseinfo und Nutzenargumente. |
| `sales-katalog-vlb-buchhandel` | Vertriebskurztext, Katalogdaten, Buchhandelsargumente, Zielgruppen. |
| `knowledge-base-faq-kundenservice` | FAQ und interne Wissensbasis für Vertrieb, Support und Redaktion. |
| `ai-einsatz-transparenz-datenschutz` | KI-Einsatz, Vertraulichkeit, DSGVO, Rechte und Freigabe dokumentieren. |
| `produktionsuebergabe-checkliste` | Übergabe an Herstellung, Satz, Online, Marketing, Vertrieb und Archiv. |
| `qualitaetsgate-verlag` | Schlussprüfung vor Autor:innenversand, Satz, Onlinegang oder Druck. |

## Quellenregel

- Keine Kommentar-, Handbuch-, Aufsatz- oder Datenbankfundstellen aus Modellwissen.
- Literatur nur aus Nutzerquelle, frei zugänglicher Quelle oder lizenziertem Live-Zugriff.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Fremdtexte niemals wörtlich übernehmen, außer der Nutzer verlangt ein zulässiges kurzes Zitat mit sauberer Quellenangabe und Zweck.
- Bei Verlagstexten immer trennen: Autor:innenmaterial, Redaktionstext, Fremdquelle, KI-Vorschlag und offene Lücke.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 104 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ai-einsatz-transparenz-datenschutz` | Dokumentiert KI-Einsatz, Vertraulichkeit, Datenschutz, Autor:innenmaterial, Fremdrechte, Trainingsverbot, Freigaben und interne Verlagspolitik. |
| `allgemein` | Cooler Einstieg fuer das Verlagsredaktion-Plugin: stummer Upload, Morgenlage, Eingangskorb, Fristen, Rechteampel, Manuskriptstatus und Routing zu den Verlagsdesk-Skills. |
| `autorenkommunikation-email` | Schreibt freundliche, klare Autor:innenkommunikation fuer Nachforderungen, Korrekturen, Freigaben, Rechtefragen, Fristen und Eskalationen. |
| `barrierefreiheit-epub-pdf` | Prueft Verlagsoutputs auf Struktur, Alt-Texte, Tabellenlesbarkeit, Ueberschriftenlogik, PDF- und EPUB-Zugaenglichkeit. |
| `bildrechte-grafiken-tabellen` | Prueft Bilder, Screenshots, Grafiken, Tabellen, Diagramme, Credits, Alt-Texte, Bearbeitungen und Nutzungsumfang fuer Verlagspublikationen. |
| `buchprojekt-kapitelkoordination` | Steuert Buchprojekte, Kapitel, Autor:innen, Herausgeber:innen, Register, Abbildungen, Vorwort, Fristen und Produktionsstand. |
| `eingangskorb-triage` | Sortiert einen Verlags-Eingangskorb aus Mails, Manuskripten, Fahnen, Bildern, Tabellen und Notizen nach Frist, Risiko, Projekt und naechster Aktion. |
| `entscheidungsmonitor-rechtsstand` | Erfasst neue Entscheidungen, Gesetze und Materialien als moegliche Aktualisierungsanlaesse fuer Zeitschrift, Kommentar, Newsletter oder Buchauflage. |
| `fremdtext-plagiat-uebernahmecheck` | Markiert Fremdtext-, Copy-Paste-, Plagiats-, KI-Text- und Paraphrase-Risiken und erstellt eine redaktionelle Klaerungsliste. |
| `honorar-vertrag-royalties-triage` | Triage fuer Autor:innenvertrag, Honorar, Tantiemen, Pauschale, Nebenrechte, Abrechnung, Nutzungsarten und Eskalation an Justiziariat. |
| `knowledge-base-faq-kundenservice` | Erstellt FAQ, interne Wissensbasis und Kundenservice-Antworten zu Verlagstiteln, Updates, Downloads, Errata, Lizenzen und Produktfragen. |
| `kommentar-aktualisierung-randnummern` | Unterstuetzt Kommentarupdates mit Randnummernlogik, Rechtsstandsvermerk, Nachweisen, Aenderungsprotokoll und Autor:innenrueckfragen. |
| `lektorat-struktur-redaktion` | Redigiert Struktur, Argumentationsgang, Gliederung, Kuerzung, Redundanzen, Widersprueche und Lesefuehrung von Verlagsmanuskripten. |
| `manuskriptaufnahme-materialinventar` | Nimmt Manuskripte und Begleitmaterial auf, erstellt ein Materialinventar, trennt Autor:innenmaterial, Fremdquelle, Redaktionstext, Luecken und Rechtefragen. |
| `marketing-presse-social` | Erstellt Verlagstexte fuer Vorschau, Newsletter, Presse, Website und Social Media aus Manuskript, Zielgruppe und Produktnutzen. |
| `metadaten-seo-klappentext` | Erstellt Titelvarianten, Untertitel, Abstract, Schlagworte, Klappentext, Webteaser, Kurzbeschreibung und Metadaten aus Manuskriptmaterial. |
| `produktionsuebergabe-checkliste` | Erstellt die Uebergabe an Herstellung, Satz, Online, Marketing, Vertrieb und Archiv mit Dateien, Freigaben, Rechten, Metadaten und offenen Punkten. |
| `projektplan-fristen-heftplanung` | Erstellt Projektplaene fuer Heft, Onlinebeitrag, Buchkapitel, Kommentarupdate oder Sonderband mit Deadlines, Abhaengigkeiten und Verantwortlichen. |
| `qualitaetsgate-verlag` | Schlusspruefung fuer Verlagsoutputs vor Autor:innenversand, Satz, Onlinegang oder Druck mit Rechte-, Quellen-, Stil-, Fristen- und Produktionsampel. |
| `quellen-zitate-fundstellencheck` | Prueft Quellen, Zitate, Randnummern, Fundstellen, Rechtsprechung und Literaturstatus mit strenger Regel gegen erfundene oder paywallige Blindzitate. |
| `rechtecheck-urhg-verlg` | Erstellt eine redaktionelle Rechteampel zu UrhG, Verlagsgesetz, Nutzungsrechten, Zitatrecht, Bearbeitung, Zweitveroeffentlichung und Freigaben. |
| `rohmanuskript-anschubhilfe` | Baut aus Diktaten, Folien, Notizen und E-Mails ein klar markiertes Rohmanuskript als Anschubhilfe, ohne Autor:innenstimme und Redaktion zu vermischen. |
| `sachbearbeiterinnen-cockpit` | Persoenliches Verlagscockpit fuer Sachbearbeitung und Redaktion: Tageslage, Prioritaeten, Fristen, Autor:innen, Rechteampel, Produktionsstand und naechste Aktionen. |
| `sales-katalog-vlb-buchhandel` | Bereitet Vertriebs-, Katalog-, VLB- und Buchhandelsdaten mit Zielgruppen, Verkaufsargumenten, Warengruppe, Schlagworten und Vergleichstiteln vor. |
| `satzfahne-korrekturlauf` | Fuehrt durch Satzfahnen, Korrekturlaeufe, Umbruch, Seitenzahlen, Abbildungen, Fussnoten, Freigaben und letzte Produktionschecks. |
| `spezial-autorenkommunikation-compliance-dokumentation-und-akte` | Autorenkommunikation: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bildrechte-zahlen-schwellen-und-berechnung` | Bildrechte: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-buchprojekte-internationaler-bezug-und-schnittstellen` | Buchprojekte: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-eingangskorb-risikoampel-und-gegenargumente` | Eingangskorb: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fachliche-fristen-form-und-zustaendigkeit` | Fachliche: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-heftplanung-mehrparteien-konflikt-und-interessen` | Heftplanung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-juristische-tatbestand-beweis-und-belege` | Juristische: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-manuskript-behoerden-gericht-und-registerweg` | Manuskript: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-metadaten-red-team-und-qualitaetskontrolle` | Metadaten: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtecheck-verhandlung-vergleich-und-eskalation` | Rechtecheck: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-redaktion-schriftsatz-brief-und-memo-bausteine` | Redaktion: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-satzfahnen-formular-portal-und-einreichung` | Satzfahnen: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verlage-dokumentenmatrix-und-lueckenliste` | Verlage: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verlagsdesk-erstpruefung-und-mandatsziel` | Verlagsdesk: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zitate-livequellen-und-rechtsprechungscheck` | Zitate: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `sprachlektorat-stil-tonalitaet` | Verbessert Sprache, Stil, Tonalitaet, Satzbau, Lesbarkeit, Gender- und Hausstilfragen fuer juristische und fachliche Verlagstexte. |
| `verl-abstimmung-mit-autor-feedback-kanal` | Strukturiert die laufende Kommunikation mit Autorin: Kanal Frequenz Dokumentation Eskalationswege bei Konflikten Lieferverzug und Manuskriptaenderungen. |
| `verl-abstimmung-mit-lektorat-format` | Klaert Lektorats- und Redaktionsstandards: wer ist fuer welchen Pruefschritt zustaendig wie wird uebergeben Track-Changes Stand Versionierung Eskalationsregeln. |
| `verl-abstimmung-mit-produktion-satz-druck` | Klaert die Schnittstelle zur Produktion: Satzdaten Format Bildaufloesung Schriftrechte Fahnenlauf Druckfreigabe Online-Auslieferung und Reklamationswege. |
| `verl-abstimmung-mit-rechtsabteilung-pruefung` | Inhouse-Legal-Check vor Veroeffentlichung: strukturierte Abstimmung mit Justiziariat zu Aeusserungsrecht, Persoenlichkeitsrecht, Urheberrecht, Wettbewerbsrecht und Datenschutz. |
| `verl-abstimmung-mit-vertrieb-marketing` | Briefing fuer Vertrieb und Marketing zu einem Verlagsprodukt: Zielgruppe Kernnutzen Vergleichstitel Preisarchitektur und Material fuer Katalog Webseite Veranstaltungen. |
| `verl-audio-transkript-zu-fachbeitrag` | Destilliert einen Audio-Vortrag oder ein freies Diktat zu einem zitierfaehigen Fachbeitrag fuer juristische Fachzeitschriften und Sammelbaende. |
| `verl-aussagensicherheit-pruefung` | Prueft im Manuskript jede tragende Aussage darauf ob sie so im Druck stehen darf: Belegtiefe Ehrenschutz Datenschutz Berufsrecht und Aussagewahrheit. |
| `verl-buchprojekt-bauleiter` | Bauleiter juristisches Buchprojekt: Konzept, Autorenvertrag, Manuskripteinreichung, Lektorat, Druck. Pruefraster fuer Herausgeber und Verlag. |
| `verl-email-konvolute-zu-fachbeitrag` | Verwertet einen E-Mail-Wechsel als Sachverhaltsquelle und Belegmaterial fuer eine Urteilsanmerkung oder einen Praxisbericht, mit Anonymisierung und Chronologie. |
| `verl-eskalation-bei-deadline-konflikt` | Eskalation bei Deadline-Konflikt: strukturierte Hochstufung von Manuskript-, Druck-, Honorar- oder Auslieferungsterminen mit Mustermails fuer Autor, Programmleitung und Geschaeftsfuehrung. |
| `verl-formatvorlage-check-autor-manuskript` | Prueft strikt die Einhaltung der Verlagsformatvorlage in Autorenmanuskripten und meldet Abweichungen so, dass der Autor sie selbst beheben kann. |
| `verl-fussnoten-quellen-konsolidierung` | Konsolidiert den Fussnotenapparat eines Manuskripts: dedupliziert, vereinheitlicht, prueft Pinpoints und stellt die Reihenfolge nach Verlagsstandard her. |
| `verl-glossar-konsistenz-pruefung` | Prueft Glossar und Begriffskonsistenz quer durch Reihen Loseblattwerke und Online-Kommentare: Lemma-Stamm Definitionen Synonyme Querverweise. |
| `verl-grammatik-konsistenzcheck` | Prueft Grammatik und Stilkonsistenz im Manuskript: Tempus Genus Numerus Kasus Verweisbezug Zeitformwechsel und Hausstilkonsistenz quer durch den Text. |
| `verl-haftungsfreistellung-autor-verlag` | Haftungsfreistellung zwischen Autor und Verlag: Klauselbaustein im Verlagsvertrag, Reichweite, AGB-Schranken, Versicherungsfragen, Praxis bei Abmahnung und Klage. |
| `verl-handschrift-und-altdoc-digitalisieren` | Digitalisiert handschriftliche Originalvorlagen und alte Dokumente fuer die Verlagsredaktion, mit Lesart-Markierung, Erhaltungsdokumentation und Auditfaehigkeit. |
| `verl-honorarrechnung-erstellen-pruefen` | Honorarrechnung erstellen und pruefen: Pflichtangaben, USt-Behandlung, Kleinunternehmer, Reverse Charge, Auslandsautoren, KSK. Mit Musterrechnungen fuer Aufsatz, Beitrag, Werk. |
| `verl-honorarvertrag-templates-und-abweichungen` | Honorarvertragstemplates fuer juristische Werke: Standardvertrag Aufsatz, Buch, Kommentar, Herausgeberwerk. Abweichungspruefung gegen UrhG § 32 angemessene Verguetung. |
| `verl-ideenpool-und-priorisierung` | Verwaltet einen Ideen-Backlog der Verlagsredaktion mit Priorisierungsmatrix, Zustandskategorien und Eskalationsregeln fuer entscheidungsreife Themen. |
| `verl-impressum-pflicht-und-pruefung` | Impressumspflicht und Pruefung im Verlag: DDG § 5, MStV § 18 V. i. S. d. P., Anforderungen Print/Online/Newsletter/Social-Media-Profile, Mustertexte und Pruefcheckliste. |
| `verl-interview-roh-zu-magazinbeitrag` | Macht aus einem Interview-Transkript eine drucktaugliche Interview-Fassung fuer Fachmagazin oder Newsletter, mit Autorisierung und Tonalitaetskontrolle. |
| `verl-jourfix-vorbereiten-protokoll` | Bereitet einen Jourfixe der Verlagsredaktion vor: knappe Agenda Statusliste Beschluesse mit Owner und Frist Protokoll innerhalb 24 Stunden. |
| `verl-konferenzmitschnitt-zu-tagungsbericht` | Macht aus einem Tagungs- oder Konferenzmitschnitt einen Tagungsbericht fuer Fachzeitschrift, mit Vortragsuebersicht, Diskussionsskizze und Quellenpflicht. |
| `verl-loeschpflicht-und-archivierung-fachzs` | Loeschpflicht und Archivierung bei juristischer Fachzeitschrift: DSGVO Art. 17 Recht auf Vergessen, Online-Archiv, Aktenzeichen-Anonymisierung, Pressefreiheitsabwaegung, Versionierung. |
| `verl-loseblattwerk-spezial` | Spezialfall Loseblattwerk: Ergaenzungslieferung, Stichtag, Hinweisapparat, Abonnentenpflege. Pruefraster fuer Verlag und Redaktion. |
| `verl-mahnung-an-autor-zahlung-frist` | Mahnung an Autor bei Rueckforderung von Vorschuss oder ueberzahltem Honorar: Stufenmodell, Nachfrist gemaess BGB § 286 und § 323, Verjaehrungspruefung, Mustertexte und gerichtliche Geltendmachung. |
| `verl-manuskript-merkwuerdige-formate-rettung` | Rettet Manuskripte aus DOCX-/Markdown-/LaTeX-Mix, alten Word97-Dateien und KI-generiertem Wust; legt saubere Konvertierungspfade fuer die Verlagsredaktion. |
| `verl-newsletter-redaktion-jur` | Newsletter-Redaktion juristisch: Konzept, Themenkasten, Empfaengerverwaltung nach DSGVO und UWG § 7, double opt-in, Mustertexte fuer wochen- und monatsweisen Versand. |
| `verl-online-kommentar-update-spezial` | Spezialfall Online-Kommentar und Update-Workflow: Versionierung, Rechtsprechungsmonitoring, Verlinkung. Pruefraster fuer Verlag und Hauptbearbeiter. |
| `verl-podcast-zu-zeitschriftenbeitrag` | Nutzt einen juristischen Podcast als Zitat- und Inhaltsquelle fuer einen Zeitschriftenbeitrag, klaert Verwertungsrechte und liefert ein zitierbares Belegformat. |
| `verl-powerpoint-verwurstung-zu-text` | Macht aus einer schlechten Vortrags-PPT einen Fliesstextbeitrag fuer Fachzeitschrift oder Tagungsband, ohne Bullet-Wuesten und mit Quellenrekonstruktion. |
| `verl-pressetext-rechtsthemen` | Pressetext zu Rechtsthemen: Schreibanleitung fuer Verlagspressemitteilung zu neuem Buch oder neuer Entscheidung. Mustertexte fuer Fachpresse und allgemeine Medien mit Sperrfrist. |
| `verl-rechtschreibung-amtlich-aktuell` | Prueft die amtliche deutsche Rechtschreibung in Verlagsmanuskripten nach dem aktuellen Duden-Stand und dem amtlichen Regelwerk inklusive Eigennamen und Sondereinrichtungen. |
| `verl-redaktionelle-rueckmeldung-formulieren` | Formuliert Autoren-Rueckmeldungen kollegial und praezise: trennt klar Stops von Wuenschen vermeidet Praedigtton und gibt der Autorin handhabbare Aufgaben. |
| `verl-redaktionsmemo-jahresplanung` | Erstellt das Jahresheft-Planungsmemo einer juristischen Fachzeitschrift mit Themenarchitektur, Heftfolge, Autorenstrategie und Risikoreserven. |
| `verl-redaktionssitzung-vorbereiten` | Bereitet eine juristische Redaktionssitzung vor: Agenda, Themenscoring, Beschlussvorlage, Protokollskelett und Anschlussaufgaben. |
| `verl-relationslinien-pruefung-im-aufsatz` | Prueft die logischen Relationslinien eines juristischen Aufsatzes: traegt das Argumentationsgeruest die Hauptthese ohne Sprunglinien und ohne Zirkel? |
| `verl-richtigstellung-online-print` | Richtigstellung im Online- und Printmedium: Berichtigungsanspruch, Gegendarstellung nach MStV § 20, Erratum, Online-Korrekturhinweis. Mustertexte fuer alle drei Eskalationsstufen. |
| `verl-roh-research-zu-essay` | Verdichtet unstrukturierten Recherchewust einer Autorin zu einem zitierfaehigen Essay oder Diskussionsbeitrag fuer juristisches Fachformat. |
| `verl-rueckruf-fehlerbeitrag-spaet-erkannt` | Rueckruf bei spaet erkanntem Fehlerbeitrag: Rechtsfolgenpruefung BGB § 824, UrhG § 14, Aeusserungsrecht. Eskalationsplan, Mustertexte fuer Print- und Online-Rueckruf, Kostenabwaegung. |
| `verl-screenshot-pdf-ocr-redaktion` | Fuehrt einen sauberen OCR-Workflow fuer gescannte PDFs und Screenshots zu redaktionellem Manuskript, mit Fehlerquoten-Stichprobe und Pinpoint-Erhalt. |
| `verl-social-media-rechtsfachzeitschrift` | Social-Media-Beitrag fuer juristische Fachzeitschrift: Konzept fuer LinkedIn, Bluesky, Mastodon. Texttemplates, Bildvorgaben, Disclaimer, Werbekennzeichnung nach UWG und DDG. |
| `verl-statusbericht-an-verlagsleitung` | Statusbericht an die Verlagsleitung: knappe Lagedarstellung zu Projekt, Frist, Kosten, Risiko und Eskalation. Mustertexte fuer monatliches Reporting und Ad-hoc-Alarm. |
| `verl-stilbruch-stilcheck-fachzeitschrift` | Spuert Stilbrueche im Fachzeitschriften-Manuskript auf: gemischte Stilebenen Ironie Umgangssprache Floskeln Marketingsprache und KI-typische Phrasen. |
| `verl-tantieme-abrechnung-jaehrlich` | Jaehrliche Tantieme-Abrechnung fuer Autoren juristischer Werke: Stueck- und Umsatzbeteiligung, Loseblatt-Ergaenzungslieferungen, Online-Nutzung, Verrechnung mit Vorschuss, Pflichten nach UrhG § 32d. |
| `verl-themenscout-rechtsentwicklung` | Identifiziert Trends in BGH-/EuGH-/BVerfG-/BMF-Rechtsprechung und Gesetzgebungsverfahren als Themenkandidaten fuer Aufsaetze und Heftaufmacher. |
| `verl-trend-radar-rechtsgebiete` | Beobachtet rechtsgebietsuebergreifende Trends (Digitalisierung, ESG, KI-Recht, EU-Reformen) als Themen-Frueherkennung fuer mehrere Zeitschriften und Reihen. |
| `verl-vergleichsverhandlung-mit-autor` | Vergleichsverhandlung mit Autor: Aufbau einer Verhandlungslinie bei Honorar-, Tantieme- oder Rueckforderungsstreit, BATNA, Eskalationsstufen, schriftlicher Vergleich und Abgeltungsklausel. |
| `verl-vlb-katalog-pflege-jur` | VLB-Katalog (Verzeichnis lieferbarer Buecher) pflegen: ONIX-Metadaten, Schlagworte, Klappentext, Reihen, Preisbindung, Erscheinungstermin-Pflege. Konsistenz mit Webshop, beck-online und Buchhandel. |
| `verl-vorschuss-pruefung-buecher` | Vorschusspruefung fuer Buchprojekte: Bemessungsgrundlage, Auszahlungsstufen, Verrechnung mit Tantiemen, Rueckforderung bei Nichtablieferung, steuerliche und sozialversicherungsrechtliche Folgen. |
| `verl-webinar-vorbereitung-fachbeitrag` | Webinar-Vorbereitung als Fachbeitrag-Sequel: Vom Aufsatz zur Onlineveranstaltung. Vertrag mit Autor, FAO-Fortbildungspunkte, Technik, Datenschutz, Aufzeichnung und Vermarktung. |
| `verl-zeitschriftenartikel-leitfaden` | Leitfaden Zeitschriftenartikel: Auswahl Zeitschrift, Manuskriptregeln, Peer Review, Open Access. Pruefraster fuer Autorin und Verlag. |
| `verl-zitierweise-pruefung-zeitschrift-jus-njw` | Prueft die Zitierweise in Manuskripten gegen die jeweiligen Hausnormen von NJW NZA JuS JZ und verwandten Fachzeitschriften ohne Halluzination. |
| `verl-zweitverwertungsrechte-pauschal` | Zweitverwertungsrechte und Nebenrechte pauschal vereinbaren: Lizenz an juris/beck-online, Open Access, Sonderdruck, Festschriftsuebernahme, Bearbeitungen. Honorarverteilung und § 38 UrhG. |
| `verlagsredaktion` | Kernskill fuer verlegerische Rohmanuskript- und Editionsarbeit: Material inventarisieren, strukturieren, redigieren, Luecken markieren, Quellen trennen und Autor:innenfreigaben vorbereiten. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin verlagsredaktion: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin verlagsredaktion: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin verlagsredaktion: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin verlagsredaktion: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin verlagsredaktion: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin verlagsredaktion: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin verlagsredaktion: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zeitschriften-heftplanung` | Organisiert Zeitschriftenhefte mit Rubriken, Beitraegen, Autor:innen, Seitenbudget, Online-first, Korrekturlauf, Anzeigen und Schlussredaktion. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
