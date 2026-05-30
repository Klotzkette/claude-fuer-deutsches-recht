# Verlagsredaktion

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

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

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
| `sprachlektorat-stil-tonalitaet` | Verbessert Sprache, Stil, Tonalitaet, Satzbau, Lesbarkeit, Gender- und Hausstilfragen fuer juristische und fachliche Verlagstexte. |
| `verlagsredaktion` | Kernskill fuer verlegerische Rohmanuskript- und Editionsarbeit: Material inventarisieren, strukturieren, redigieren, Luecken markieren, Quellen trennen und Autor:innenfreigaben vorbereiten. |
| `zeitschriften-heftplanung` | Organisiert Zeitschriftenhefte mit Rubriken, Beitraegen, Autor:innen, Seitenbudget, Online-first, Korrekturlauf, Anzeigen und Schlussredaktion. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
