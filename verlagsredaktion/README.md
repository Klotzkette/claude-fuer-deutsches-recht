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
| **Akte Auerbach Soundworks / Nordlicht in Beton** (`urheberrecht-musik-ki-songstreit-auerbach`) | [Gesamt-PDF lesen](../testakten/urheberrecht-musik-ki-songstreit-auerbach/gesamt-pdf/urheberrecht-musik-ki-songstreit-auerbach_gesamt.pdf) | [`testakte-urheberrecht-musik-ki-songstreit-auerbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-urheberrecht-musik-ki-songstreit-auerbach.zip) |
| **Akte Lilienfeld Verlag: Fachbuch, E-Book-Bundle, Remittenden und Preisbindungsabmahnung** (`verlagsrecht-buchpreisbindung-fachverlag-lilienfeld`) | [Gesamt-PDF lesen](../testakten/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld/gesamt-pdf/verlagsrecht-buchpreisbindung-fachverlag-lilienfeld_gesamt.pdf) | [`testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsrecht-buchpreisbindung-fachverlag-lilienfeld.zip) |
| **Verlagsredaktion Morgenlage Fachverlag** (`verlagsredaktion-morgenlage-fachverlag`) | [Gesamt-PDF lesen](../testakten/verlagsredaktion-morgenlage-fachverlag/gesamt-pdf/verlagsredaktion-morgenlage-fachverlag_gesamt.pdf) | [`testakte-verlagsredaktion-morgenlage-fachverlag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verlagsredaktion-morgenlage-fachverlag.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskriptaufnahme, Redaktion, Rechtecheck, Zitat- und Fundstellenkontrolle, Autor:innenkommunikation, Heftplanung, Buchprojektsteuerung, Satzfahnen, Metadaten, Marketingtexte, Produktionsübergabe und Qualitätstor.

Der erste Bildschirm soll sich für eine Sachbearbeiterin so anfühlen: Alles liegt durcheinander im Postfach, aber das Plugin macht daraus sofort eine Morgenlage, eine Prioritätenliste und den nächsten verwendbaren Arbeitsschritt.

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
| `verlagsredaktion-allgemein` | Cooler Einstieg, stummer Upload, Morgenlage und Skill-Routing. |
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
| `abstimmung` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert... |
| `abstimmung-lektorat-produktion-satz` | Klaert Lektorats- und Redaktionsstandards: wer ist für welchen Pruefschritt zuständig wie wird uebergeben Track-Changes Stand Versionierung Eskalationsregeln im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Frist... |
| `abstimmung-mit-autor-feedback-kanal` | Strukturiert die laufende Kommunikation mit Autorin: Kanal Frequenz Dokumentation Eskalationswege bei Konflikten Lieferverzug und Manuskriptaenderungen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Be... |
| `abstimmung-mit-produktion-satz-druck` | Klaert die Schnittstelle zur Produktion: Satzdaten Format Bildaufloesung Schriftrechte Fahnenlauf Druckfreigabe Online-Auslieferung und Reklamationswege im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, B... |
| `abstimmung-mit-rechtsabteilung-pruefung` | Inhouse-Legal-Check vor Veroeffentlichung: strukturierte Abstimmung mit Justiziariat zu Aeusserungsrecht, Persoenlichkeitsrecht, Urheberrecht, Wettbewerbsrecht und Datenschutz im Verlagsredaktion: prüft konkret die einschlägigen Tatbesta... |
| `abstimmung-mit-vertrieb-marketing` | Briefing für Vertrieb und Marketing zu einem Verlagsprodukt: Zielgruppe Kernnutzen Vergleichstitel Preisarchitektur und Material für Katalog Webseite Veranstaltungen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmal... |
| `ai-einsatz-transparenz-datenschutz` | Dokumentiert KI-Einsatz, Vertraulichkeit, Datenschutz, Autor:innenmaterial, Fremdrechte, Trainingsverbot, Freigaben und interne Verlagspolitik im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und... |
| `audio-transkript-zu-fachbeitrag` | Destilliert einen Audio-Vortrag oder ein freies Diktat zu einem zitierfaehigen Fachbeitrag für juristische Fachzeitschriften und Sammelbaende im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und R... |
| `aussagensicherheit-buchprojekt-bauleiter` | Prueft im Manuskript jede tragende Aussage darauf ob sie so im Druck stehen darf: Belegtiefe Ehrenschutz Datenschutz Berufsrecht und Aussagewahrheit im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Beleg... |
| `autorenkommunikation-compliance-dokumentation-und-akte` | Autorenkommunikation: Compliance-Dokumentation und Aktenvermerk; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die ei... |
| `autorenkommunikation-email` | Schreibt freundliche, klare Autor:innenkommunikation für Nachforderungen, Korrekturen, Freigaben, Rechtefragen, Fristen und Eskalationen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechts... |
| `barrierefreiheit-epub-pdf` | Prueft Verlagsoutputs auf Struktur, Alt-Texte, Tabellenlesbarkeit, Ueberschriftenlogik, PDF- und EPUB-Zugaenglichkeit im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert p... |
| `bildrechte-grafiken-tabellen` | Prueft Bilder, Screenshots, Grafiken, Tabellen, Diagramme, Credits, Alt-Texte, Bearbeitungen und Nutzungsumfang für Verlagspublikationen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechts... |
| `bildrechte-zahlen-schwellen-und-berechnung` | Bildrechte: Zahlen, Schwellenwerte und Berechnung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägigen Ta... |
| `buchprojekt-bauleiter` | Bauleiter juristisches Buchprojekt: Konzept, Autorenvertrag, Manuskripteinreichung, Lektorat, Druck. Pruefraster für Herausgeber und Verlag im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rec... |
| `buchprojekt-kapitelkoordination` | Steuert Buchprojekte, Kapitel, Autor:innen, Herausgeber:innen, Register, Abbildungen, Vorwort, Fristen und Produktionsstand im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `buchprojekte-internationaler-bezug-und-schnittstellen` | Buchprojekte: Internationaler Bezug und Schnittstellen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägig... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `eingangskorb-heftplanung-interessen` | Eingangskorb: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die... |
| `eingangskorb-triage-entscheidungsmonitor` | Sortiert einen Verlags-Eingangskorb aus Mails, Manuskripten, Fahnen, Bildern, Tabellen und Notizen nach Frist, Risiko, Projekt und naechster Aktion im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `email-konvolute-zu-fachbeitrag` | Verwertet einen E-Mail-Wechsel als Sachverhaltsquelle und Belegmaterial für eine Urteilsanmerkung oder einen Praxisbericht, mit Anonymisierung und Chronologie im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fris... |
| `entscheidungsmonitor-rechtsstand` | Erfasst neue Entscheidungen, Gesetze und Materialien als moegliche Aktualisierungsanlaesse für Zeitschrift, Kommentar, Newsletter oder Buchauflage im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `eskalation-bei-deadline-konflikt` | Eskalation bei Deadline-Konflikt: strukturierte Hochstufung von Manuskript-, Druck-, Honorar- oder Auslieferungsterminen mit Mustermails für Autor, Programmleitung und Geschaeftsfuehrung im Verlagsredaktion: prüft konkret die einschlägig... |
| `fachliche-fristen-form-und-zustaendigkeit` | Fachliche: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägige... |
| `formatvorlage-check-autor-manuskript` | Prueft strikt die Einhaltung der Verlagsformatvorlage in Autorenmanuskripten und meldet Abweichungen so, dass der Autor sie selbst beheben kann im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und... |
| `fremdtext-plagiat-uebernahmecheck` | Markiert Fremdtext-, Copy-Paste-, Plagiats-, KI-Text- und Paraphrase-Risiken und erstellt eine redaktionelle Klaerungsliste im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `fussnoten-quellen-glossar-konsistenz` | Konsolidiert den Fussnotenapparat eines Manuskripts: dedupliziert, vereinheitlicht, prueft Pinpoints und stellt die Reihenfolge nach Verlagsstandard her im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, B... |
| `glossar-konsistenz-pruefung` | Prueft Glossar und Begriffskonsistenz quer durch Reihen Loseblattwerke und Online-Kommentare: Lemma-Stamm Definitionen Synonyme Querverweise im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Re... |
| `grammatik-konsistenzcheck` | Prueft Grammatik und Stilkonsistenz im Manuskript: Tempus Genus Numerus Kasus Verweisbezug Zeitformwechsel und Hausstilkonsistenz quer durch den Text im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Bele... |
| `haftungsfreistellung-autor-verlag` | Haftungsfreistellung zwischen Autor und Verlag: Klauselbaustein im Verlagsvertrag, Reichweite, AGB-Schranken, Versicherungsfragen, Praxis bei Abmahnung und Klage im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, F... |
| `handschrift-und-altdoc-digitalisieren` | Digitalisiert handschriftliche Originalvorlagen und alte Dokumente für die Verlagsredaktion, mit Lesart-Markierung, Erhaltungsdokumentation und Auditfaehigkeit im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fri... |
| `heftplanung-mehrparteien-konflikt-und-interessen` | Heftplanung: Mehrparteienkonflikt und Interessenmatrix; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägig... |
| `honorar-vertrag-royalties-triage` | Triage für Autor:innenvertrag, Honorar, Tantiemen, Pauschale, Nebenrechte, Abrechnung, Nutzungsarten und Eskalation an Justiziariat im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprech... |
| `honorarrechnung-erstellen-pruefen` | Honorarrechnung erstellen und pruefen: Pflichtangaben, USt-Behandlung, Kleinunternehmer, Reverse Charge, Auslandsautoren, KSK. Mit Musterrechnungen für Aufsatz, Beitrag, Werk im Verlagsredaktion: prüft konkret die einschlägigen Tatbestan... |
| `honorarvertrag-templates-und-abweichungen` | Honorarvertragstemplates für juristische Werke: Standardvertrag Aufsatz, Buch, Kommentar, Herausgeberwerk. Abweichungspruefung gegen UrhG § 32 angemessene Verguetung im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmal... |
| `ideenpool-priorisierung-impressum` | Verwaltet einen Ideen-Backlog der Verlagsredaktion mit Priorisierungsmatrix, Zustandskategorien und Eskalationsregeln für entscheidungsreife Themen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `impressum-pflicht-und-pruefung` | Impressumspflicht und Pruefung im Verlag: DDG § 5, MStV § 18 V. i. S. d. P., Anforderungen Print/Online/Newsletter/Social-Media-Profile, Mustertexte und Pruefcheckliste im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerk... |
| `interview-roh-zu-magazinbeitrag` | Macht aus einem Interview-Transkript eine drucktaugliche Interview-Fassung für Fachmagazin oder Newsletter, mit Autorisierung und Tonalitaetskontrolle im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Bel... |
| `jourfix-vorbereiten-protokoll` | Bereitet einen Jourfixe der Verlagsredaktion vor: knappe Agenda Statusliste Beschluesse mit Owner und Frist Protokoll innerhalb 24 Stunden im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rech... |
| `juristische-tatbestand-beweis-und-belege` | Juristische: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einsc... |
| `kaltstart-triage` | Cooler Einstieg für das Verlagsredaktion-Plugin: stummer Upload, Morgenlage, Eingangskorb, Fristen, Rechteampel, Manuskriptstatus und Routing zu den Verlagsdesk-Skills. |
| `knowledge-base-faq-kundenservice` | Erstellt FAQ, interne Wissensbasis und Kundenservice-Antworten zu Verlagstiteln, Updates, Downloads, Errata, Lizenzen und Produktfragen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsp... |
| `kommentar-aktualisierung-randnummern` | Unterstuetzt Kommentarupdates mit Randnummernlogik, Rechtsstandsvermerk, Nachweisen, Aenderungsprotokoll und Autor:innenrueckfragen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprech... |
| `konferenzmitschnitt-zu-tagungsbericht` | Macht aus einem Tagungs- oder Konferenzmitschnitt einen Tagungsbericht für Fachzeitschrift, mit Vortragsuebersicht, Diskussionsskizze und Quellenpflicht im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, B... |
| `lektorat-struktur-manuskriptaufnahme` | Redigiert Struktur, Argumentationsgang, Gliederung, Kuerzung, Redundanzen, Widersprueche und Lesefuehrung von Verlagsmanuskripten im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechun... |
| `loeschpflicht-archivierung-loseblattwerk` | Loeschpflicht und Archivierung bei juristischer Fachzeitschrift: DSGVO Art. 17 Recht auf Vergessen, Online-Archiv, Aktenzeichen-Anonymisierung, Pressefreiheitsabwaegung, Versionierung im Verlagsredaktion: prüft konkret die einschlägigen... |
| `loseblattwerk-spezial` | Spezialfall Loseblattwerk: Ergaenzungslieferung, Stichtag, Hinweisapparat, Abonnentenpflege. Pruefraster für Verlag und Redaktion im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechun... |
| `mahnung-an-honorar-vertrag` | Mahnung an Autor bei Rueckforderung von Vorschuss oder ueberzahltem Honorar: Stufenmodell, Nachfrist gemaess BGB § 286 und § 323, Verjährungspruefung, Mustertexte und gerichtliche Geltendmachung im Verlagsredaktion: prüft konkret die ein... |
| `manuskript-behoerden-gericht-und-registerweg` | Manuskript: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägigen Ta... |
| `manuskript-merkwuerdige-formate-rettung` | Rettet Manuskripte aus DOCX-/Markdown-/LaTeX-Mix, alten Word97-Dateien und KI-generiertem Wust; legt saubere Konvertierungspfade für die Verlagsredaktion im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen,... |
| `manuskriptaufnahme-materialinventar` | Nimmt Manuskripte und Begleitmaterial auf, erstellt ein Materialinventar, trennt Autor:innenmaterial, Fremdquelle, Redaktionstext, Luecken und Rechtefragen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen... |
| `marketing-presse-social` | Erstellt Verlagstexte für Vorschau, Newsletter, Presse, Website und Social Media aus Manuskript, Zielgruppe und Produktnutzen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. L... |
| `metadaten-fehlerkatalog` | Metadaten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `metadaten-seo-klappentext` | Erstellt Titelvarianten, Untertitel, Abstract, Schlagworte, Klappentext, Webteaser, Kurzbeschreibung und Metadaten aus Manuskriptmaterial im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `newsletter-redaktion-jur` | Newsletter-Redaktion juristisch: Konzept, Themenkasten, Empfaengerverwaltung nach DSGVO und UWG § 7, double opt-in, Mustertexte für wochen- und monatsweisen Versand im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale... |
| `online-kommentar-update-spezial` | Spezialfall Online-Kommentar und Update-Workflow: Versionierung, Rechtsprechungsmonitoring, Verlinkung. Pruefraster für Verlag und Hauptbearbeiter im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `output-waehlen` | Output wählen im Verlagsredaktion (Recht): Diese Output-Weiche für Verlagsredaktion entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `podcast-zeitschriftenbeitrag-powerpoint` | Nutzt einen juristischen Podcast als Zitat- und Inhaltsquelle für einen Zeitschriftenbeitrag, klaert Verwertungsrechte und liefert ein zitierbares Belegformat im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fris... |
| `powerpoint-verwurstung-zu-text` | Macht aus einer schlechten Vortrags-PPT einen Fliesstextbeitrag für Fachzeitschrift oder Tagungsband, ohne Bullet-Wuesten und mit Quellenrekonstruktion im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Be... |
| `pressetext-rechtsthemen` | Pressetext zu Rechtsthemen: Schreibanleitung für Verlagspressemitteilung zu neuem Buch oder neuer Entscheidung. Mustertexte für Fachpresse und allgemeine Medien mit Sperrfrist im Verlagsredaktion: prüft konkret die einschlägigen Tatbesta... |
| `produktionsuebergabe-checkliste` | Erstellt die Uebergabe an Herstellung, Satz, Online, Marketing, Vertrieb und Archiv mit Dateien, Freigaben, Rechten, Metadaten und offenen Punkten im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `projektplan-fristen-heftplanung` | Erstellt Projektplaene für Heft, Onlinebeitrag, Buchkapitel, Kommentarupdate oder Sonderband mit Deadlines, Abhaengigkeiten und Verantwortlichen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege un... |
| `qualitaetsgate-verlag-quellen-zitate` | Schlusspruefung für Verlagsoutputs vor Autor:innenversand, Satz, Onlinegang oder Druck mit Rechte-, Quellen-, Stil-, Fristen- und Produktionsampel im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quellen-zitate-fundstellencheck` | Prueft Quellen, Zitate, Randnummern, Fundstellen, Rechtsprechung und Literaturstatus mit strenger Regel gegen erfundene oder paywallige Blindzitate im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege... |
| `rechtecheck-urhg-verlg` | Erstellt eine redaktionelle Rechteampel zu UrhG, Verlagsgesetz, Nutzungsrechten, Zitatrecht, Bearbeitung, Zweitveroeffentlichung und Freigaben im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und... |
| `rechtecheck-verhandlung-vergleich-und-eskalation` | Rechtecheck: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägigen T... |
| `rechtschreibung-amtlich-aktuell` | Prueft die amtliche deutsche Rechtschreibung in Verlagsmanuskripten nach dem aktuellen Duden-Stand und dem amtlichen Regelwerk inklusive Eigennamen und Sondereinrichtungen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsm... |
| `redaktion-satzfahnen-verlage-verlagsdesk` | Redaktion: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägigen T... |
| `redaktionelle-rueckmeldung-formulieren` | Formuliert Autoren-Rueckmeldungen kollegial und praezise: trennt klar Stops von Wuenschen vermeidet Praedigtton und gibt der Autorin handhabbare Aufgaben im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen,... |
| `redaktionsmemo-jahresplanung` | Erstellt das Jahresheft-Planungsmemo einer juristischen Fachzeitschrift mit Themenarchitektur, Heftfolge, Autorenstrategie und Risikoreserven im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und R... |
| `redaktionssitzung-vorbereiten` | Bereitet eine juristische Redaktionssitzung vor: Agenda, Themenscoring, Beschlussvorlage, Protokollskelett und Anschlussaufgaben im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung... |
| `relationslinien-pruefung-im-aufsatz` | Prueft die logischen Relationslinien eines juristischen Aufsatzes: traegt das Argumentationsgeruest die Hauptthese ohne Sprunglinien und ohne Zirkel? im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Bele... |
| `richtigstellung-online-print` | Richtigstellung im Online- und Printmedium: Berichtigungsanspruch, Gegendarstellung nach MStV § 20, Erratum, Online-Korrekturhinweis. Mustertexte für alle drei Eskalationsstufen im Verlagsredaktion: prüft konkret die einschlägigen Tatbes... |
| `roh-research-zu-essay` | Verdichtet unstrukturierten Recherchewust einer Autorin zu einem zitierfaehigen Essay oder Diskussionsbeitrag für juristisches Fachformat im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Recht... |
| `rohmanuskript-anschubhilfe` | Baut aus Diktaten, Folien, Notizen und E-Mails ein klar markiertes Rohmanuskript als Anschubhilfe, ohne Autor:innenstimme und Redaktion zu vermischen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Bele... |
| `rueckruf-fehlerbeitrag-screenshot-pdf` | Rueckruf bei spaet erkanntem Fehlerbeitrag: Rechtsfolgenpruefung BGB § 824, UrhG § 14, Aeusserungsrecht. Eskalationsplan, Mustertexte für Print- und Online-Rueckruf, Kostenabwaegung im Verlagsredaktion: prüft konkret die einschlägigen Ta... |
| `sachbearbeiterinnen-cockpit` | Persoenliches Verlagscockpit für Sachbearbeitung und Redaktion: Tageslage, Prioritaeten, Fristen, Autor:innen, Rechteampel, Produktionsstand und naechste Aktionen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale,... |
| `sales-katalog-satzfahne-korrekturlauf` | Bereitet Vertriebs-, Katalog-, VLB- und Buchhandelsdaten mit Zielgruppen, Verkaufsargumenten, Warengruppe, Schlagworten und Vergleichstiteln vor im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege un... |
| `satzfahne-korrekturlauf` | Fuehrt durch Satzfahnen, Korrekturlaeufe, Umbruch, Seitenzahlen, Abbildungen, Fussnoten, Freigaben und letzte Produktionschecks im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `satzfahnen-formular-portal-und-einreichung` | Satzfahnen: Formular, Portal und Einreichungslogik; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägigen T... |
| `screenshot-pdf-ocr-redaktion` | Fuehrt einen sauberen OCR-für gescannte PDFs und Screenshots zu redaktionellem Manuskript, mit Fehlerquoten-Stichprobe und Pinpoint-Erhalt im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rech... |
| `social-media-rechtsfachzeitschrift` | Social-Media-Beitrag für juristische Fachzeitschrift: Konzept für LinkedIn, Bluesky, Mastodon. Texttemplates, Bildvorgaben, Disclaimer, Werbekennzeichnung nach UWG und DDG im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsm... |
| `sprachlektorat-stil-tonalitaet` | Verbessert Sprache, Stil, Tonalitaet, Satzbau, Lesbarkeit, Gender- und Hausstilfragen für juristische und fachliche Verlagstexte im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung... |
| `statusbericht-an-verlagsleitung` | Statusbericht an die Verlagsleitung: knappe Lagedarstellung zu Projekt, Frist, Kosten, Risiko und Eskalation. Mustertexte für monatliches Reporting und Ad-hoc-Alarm im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale... |
| `stilbruch-stilcheck-fachzeitschrift` | Spuert Stilbrueche im Fachzeitschriften-Manuskript auf: gemischte Stilebenen Ironie Umgangssprache Floskeln Marketingsprache und KI-typische Phrasen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Beleg... |
| `tantieme-abrechnung-themenscout` | Jaehrliche Tantieme-Abrechnung für Autoren juristischer Werke: Stueck- und Umsatzbeteiligung, Loseblatt-Ergaenzungslieferungen, Online-Nutzung, Verrechnung mit Vorschuss, Pflichten nach UrhG § 32d im Verlagsredaktion: prüft konkret die e... |
| `themenscout-rechtsentwicklung` | Identifiziert Trends in BGH-/EuGH-/BVerfG-/BMF-Rechtsprechung und Gesetzgebungsverfahren als Themenkandidaten für Aufsaetze und Heftaufmacher im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und R... |
| `trend-radar-rechtsgebiete` | Beobachtet rechtsgebietsuebergreifende Trends (Digitalisierung, ESG, KI-Recht, EU-Reformen) als Themen-Frueherkennung für mehrere Zeitschriften und Reihen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen,... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `vergleichsverhandlung-mit-autor` | Vergleichsverhandlung mit Autor: Aufbau einer Verhandlungslinie bei Honorar-, Tantieme- oder Rueckforderungsstreit, BATNA, Eskalationsstufen, schriftlicher Vergleich und Abgeltungsklausel im Verlagsredaktion: prüft konkret die einschlägi... |
| `verlage-dokumentenmatrix-und-lueckenliste` | Verlage: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschläg... |
| `verlagsdesk-erstpruefung-und-mandatsziel` | Verlagsdesk: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verlagsredaktion: prüft konkret die einschlägi... |
| `verlagsredaktion` | Kernskill für verlegerische Rohmanuskript- und Editionsarbeit: Material inventarisieren, strukturieren, redigieren, Luecken markieren, Quellen trennen und Autor:innenfreigaben vorbereiten im Verlagsredaktion: prüft konkret die einschlägi... |
| `vlb-katalog-pflege-jur` | VLB-Katalog (Verzeichnis lieferbarer Buecher) pflegen: ONIX-Metadaten, Schlagworte, Klappentext, Reihen, Preisbindung, Erscheinungstermin-Pflege. Konsistenz mit Webshop, beck-online und Buchhandel im Verlagsredaktion: prüft konkret die e... |
| `vorschuss-ai-einsatz` | Vorschusspruefung für Buchprojekte: Bemessungsgrundlage, Auszahlungsstufen, Verrechnung mit Tantiemen, Rueckforderung bei Nichtablieferung, steuerliche und sozialversicherungsrechtliche Folgen im Verlagsredaktion: prüft konkret die einsc... |
| `webinar-vorbereitung` | Webinar-Vorbereitung als Fachbeitrag-Sequel: Vom Aufsatz zur Onlineveranstaltung. Vertrag mit Autor, FAO-Fortbildungspunkte, Technik, Datenschutz, Aufzeichnung und Vermarktung im Verlagsredaktion: prüft konkret die einschlägigen Tatbesta... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert p... |
| `zeitschriften-heftplanung` | Zeitschriften Heftplanung im Verlagsredaktion (Recht) im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `zeitschriftenartikel-leitfaden` | Leitfaden Zeitschriftenartikel: Auswahl Zeitschrift, Manuskriptregeln, Peer Review, Open Access. Pruefraster für Autorin und Verlag im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprech... |
| `zitate-quellenkarte` | Zitate Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `zitierweise-pruefung-zeitschrift-jus-njw` | Prueft die Zitierweise in Manuskripten gegen die jeweiligen Hausnormen von NJW NZA JuS JZ und verwandten Fachzeitschriften ohne Halluzination im Verlagsredaktion: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und R... |
| `zweitverwertungsrechte-pauschal` | Zweitverwertungsrechte und Nebenrechte pauschal vereinbaren: Lizenz an juris/beck-online, Open Access, Sonderdruck, Festschriftsuebernahme, Bearbeitungen. Honorarverteilung und § 38 UrhG im Verlagsredaktion: prüft konkret die einschlägig... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
