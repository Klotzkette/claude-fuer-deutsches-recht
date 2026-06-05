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

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `eingangskorb-heftplanung-interessen` | Eingangskorb Risikoampel Und Gegenargumente, Heftplanung Mehrparteien Konflikt Und Interessen, Juristische Tatbestand Beweis Und Belege, Manuskript Behörden Gericht Und Registerweg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigke... |
| `eingangskorb-triage-entscheidungsmonitor` | Eingangskorb Triage, Entscheidungsmonitor Rechtsstand, Fremdtext Plagiat Uebernahmecheck, Knowledge Base Faq Kundenservice: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten be... |
| `lektorat-struktur-manuskriptaufnahme` | Lektorat Struktur Redaktion, Manuskriptaufnahme Materialinventar, Marketing Presse Social, Metadaten Seo Klappentext: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastba... |
| `metadaten-fehlerkatalog` | Metadaten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `qualitaetsgate-verlag-quellen-zitate` | Qualitaetsgate Verlag, Quellen Zitate Fundstellencheck, Rechtecheck Urhg Verlg, Rohmanuskript Anschubhilfe: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `redaktion-satzfahnen-verlage-verlagsdesk` | Redaktion Schriftsatz Brief Und Memo Bausteine, Satzfahnen Formular Portal Und Einreichung, Verlage Dokumentenmatrix Und Lueckenliste, Verlagsdesk Erstpruefung Und Mandatsziel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, B... |
| `sales-katalog-satzfahne-korrekturlauf` | Sales Katalog Vlb Buchhandel, Satzfahne Korrekturlauf, Autorenkommunikation Compliance Dokumentation Und Akte, Bildrechte Zahlen Schwellen Und Berechnung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `verl-abstimmung` | Chronologie Und Belegmatrix, Fristen Und Risikoampel, Verl Abstimmung Mit Autor Feedback Kanal, Projektplan Fristen Heftplanung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächst... |
| `verl-abstimmung-lektorat-produktion-satz` | Verl Abstimmung Mit Lektorat Format, Verl Abstimmung Mit Produktion Satz Druck, Verl Abstimmung Mit Rechtsabteilung Prüfung, Verl Abstimmung Mit Vertrieb Marketing: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `verl-aussagensicherheit-buchprojekt-bauleiter` | Verl Aussagensicherheit Prüfung, Verl Buchprojekt Bauleiter, Verl Email Konvolute Zu Fachbeitrag, Verl Eskalation Bei Deadline Konflikt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert de... |
| `verl-fussnoten-quellen-glossar-konsistenz` | Verl Fussnoten Quellen Konsolidierung, Verl Glossar Konsistenz Prüfung, Verl Grammatik Konsistenzcheck, Verl Handschrift Und Altdoc Digitalisieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `verl-ideenpool-priorisierung-impressum` | Verl Ideenpool Und Priorisierung, Verl Impressum Pflicht Und Prüfung, Verl Interview Roh Zu Magazinbeitrag, Verl Jourfix Vorbereiten Protokoll: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lie... |
| `verl-loeschpflicht-archivierung-loseblattwerk` | Verl Loeschpflicht Und Archivierung Fachzs, Verl Loseblattwerk Spezial, Verl Manuskript Merkwuerdige Formate Rettung, Verl Newsletter Redaktion Jur: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage un... |
| `verl-mahnung-an-honorar-vertrag` | Verl Mahnung An Autor Zahlung Frist, Honorar Vertrag Royalties Triage, Verl Honorarvertrag Templates Und Abweichungen, Verl Haftungsfreistellung Autor Verlag: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgr... |
| `verl-podcast-zeitschriftenbeitrag-powerpoint` | Verl Podcast Zu Zeitschriftenbeitrag, Verl Powerpoint Verwurstung Zu Text, Verl Pressetext Rechtsthemen, Verl Rechtschreibung Amtlich Aktuell: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `verl-redaktionsmemo-jahresplanung` | Verl Redaktionsmemo Jahresplanung, Verl Redaktionssitzung Vorbereiten, Verl Relationslinien Prüfung Im Aufsatz, Verl Richtigstellung Online Print: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `verl-rueckruf-fehlerbeitrag-screenshot-pdf` | Verl Rueckruf Fehlerbeitrag Spaet Erkannt, Verl Screenshot Pdf Ocr Redaktion, Verl Social Media Rechtsfachzeitschrift, Verl Statusbericht An Verlagsleitung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrun... |
| `verl-tantieme-abrechnung-themenscout` | Verl Tantieme Abrechnung Jaehrlich, Verl Themenscout Rechtsentwicklung, Verl Trend Radar Rechtsgebiete, Verl Vergleichsverhandlung Mit Autor: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefe... |
| `verl-vorschuss-ai-einsatz` | Verl Vorschuss Prüfung Buecher, Ai Einsatz Transparenz Datenschutz, Autorenkommunikation Email, Barrierefreiheit Epub Pdf: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten bel... |
| `verl-webinar-vorbereitung` | Verl Webinar Vorbereitung Fachbeitrag, Verl Zeitschriftenartikel Leitfaden, Verl Zitierweise Prüfung Zeitschrift Jus Njw, Verl Zweitverwertungsrechte Pauschal: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsg... |
| `verlagsredaktion-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verlagsredaktion-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `verlagsredaktion-kaltstart-triage` | Cooler Einstieg fuer das Verlagsredaktion-Plugin: stummer Upload, Morgenlage, Eingangskorb, Fristen, Rechteampel, Manuskriptstatus und Routing zu den Verlagsdesk-Skills. |
| `verlagsredaktion-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `verlagsredaktion-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verlagsredaktion-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `zeitschriften-heftplanung` | Zeitschriften Heftplanung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `zitate-quellenkarte` | Zitate Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
