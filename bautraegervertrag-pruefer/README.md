# Bauträgervertrag-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Bauträgervertrag-Prüfer aus Verbrauchersicht: MaBV, §§ 650u/650v BGB, § 650m Abs. 2 BGB, AGB, Baubeschreibung, Abnahme, Schlussrate, WEG, Vormerkung, Lastenfreistellung und Drei-Dokumente-Ausgabe.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`bautraegervertrag-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertrag-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertrag-pruefer-werkstatt.md" download><code>bautraegervertrag-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bautraegervertrag-pruefer-schnellstart.md" download><code>bautraegervertrag-pruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip) (Bauträgervertrag Birkenpfuhl — Verbraucherprüfung Quendel / Übelacker-Strohmeyer) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Werklohn, Mängel und Abnahme am Bauvorhaben durchsetzen oder abwehren.
Eigenes Plugin für die verbraucherseitige Prüfung deutscher Bauträgerverträge über Wohnungen, Häuser, Tiefgaragenstellplätze und Sondernutzungsrechte. Das Plugin arbeitet aus Sicht der Käuferin oder des Käufers: Es soll einen Notarentwurf, eine beurkundete Urkunde oder eine chaotische Mandatsakte so auswerten, dass MaBV-Zahlungen, Sicherheiten, AGB-Klauseln, Baubeschreibung, Abnahme, Teilungserklärung, Eigentumssicherung und Verhandlungsstrategie nicht nebeneinander liegen bleiben, sondern in ein belastbares Mandatsprodukt münden.

Der Kern ist aus dem langen Bauträgervertrag-Prüfer-Skill übernommen und fachlich verdichtet. Der ursprüngliche One-Shot-Gedanke bleibt erhalten: Wenn ein Vertrag oder Aktenordner vorliegt, startet die Prüfung aus dem Dokument heraus, bildet zuerst einen Fall-Fingerabdruck und stellt nur solche Rückfragen, ohne die die Bewertung objektiv falsch würde. Daneben sind die Arbeitsabschnitte als eigene Skills vorhanden, damit Plugin-Umgebung/Cowork gezielt den passenden Teil laden kann.

## Wofür dieses Plugin gedacht ist

- Vorprüfung eines Bauträgervertragsentwurfs vor dem Notartermin aus Verbrauchersicht.
- Prüfung einer bereits beurkundeten Urkunde, wenn Raten, Baufortschritt, Sonderwünsche, Abnahme oder Schlussrate streitig werden.
- Aufbereitung einer Mandantenakte mit Teilungserklärung, Baubeschreibung, Ratenplan, Freistellungserklärung, Baugrund-/Technikunterlagen und E-Mail-Verkehr.
- Erstellung eines Drei-Dokumente-Pakets: kurzes Mandantenanschreiben, ausführliches Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notariat mit konkreten Änderungsfassungen.

## Arbeitsweise

1. **Fall-Fingerabdruck:** Urkunde, Parteien, Einheit, Projekt, Preis, Ratenplan, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, WEG-Organisation und Streitstand werden aus der Akte gezogen.
2. **Pflicht-Prüfblock:** § 650u/§ 650v BGB, § 650m Abs. 2 BGB, §§ 3, 7, 12 MaBV, §§ 305 ff. BGB, Abnahme Gemeinschaftseigentum, Schlussrate und Eigentumssicherung werden immer zuerst geprüft.
3. **Klauselmatrix:** Jede problematische Klausel wird mit Originalwortlaut, Risiko, Normanker, Rechtsprechungsanker, Gegenargument und gewünschter Neufassung erfasst.
4. **Drei-Dokumente-Ausgabe:** Das Ergebnis wird nicht als lose Stichwortliste stehen gelassen, sondern in ausformulierte, verwendbare Texte überführt.

## Quellenhygiene

Rechtsprechung wird nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet. Zulässige Startquellen sind insbesondere offizielle Bundes-/Landesgerichtsseiten, `rechtsprechung-im-internet.de`, `rechtsinformationen.bund.de`, `dejure.org` und `openjur.de`. BeckRS-, juris-, Kommentar- und Aufsatzfundstellen werden nicht als Beleg zitiert.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Umgebung oder Cowork → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Bei einer Prüfung zusätzlich die Testakte oder eigene Vertragsunterlagen als PDF/DOCX/Markdown hochladen.

> Hinweis: Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abnahme-gemeinschaftseigentum-schlussrate-und-maengelrechte` | Abnahmeprüfung im Bauträgervertrag: Sondereigentum, Gemeinschaftseigentum, Vertreter-/Sachverständigenabnahme, Erstverwalter, § 640 BGB, § 634a BGB, § 3 Abs. 2 MaBV, Schlussrate, Verjährungsbeginn und Nachzügler. |
| `agb-klauselkontrolle-beweislast-und-tatsachenbestaetigung` | AGB-Klauselkontrolle im Bauträgervertrag: prüft § 307 BGB, § 308 Nr. 4 BGB, § 309 Nr. 1, Nr. 2 lit. a, Nr. 8, Nr. 12 und Nr. 15 BGB, Tatsachenbestätigung, Beweislast, Änderungsrechte und Zahlungssicherheit. |
| `baubeschreibung-bausoll-und-wohnflaeche` | Baubeschreibung und Bausoll im Bauträgervertrag: prüft § 650j, § 650k Abs. 2/3, § 650n BGB, Art. 249 EGBGB, beurkundete Anlagen, Wohnfläche, Prospekt/Showroom, DIN-Verweise und anerkannte Regeln der Technik. |
| `baugruppen-gbr-beurkundung-mopeg-und-mabv-abgrenzung` | Prüft Baugruppen-GbR als Alternative zum Bauträgervertrag: § 311b BGB, §§ 705 ff. BGB nach MoPeG, WEG-Teilung, Beurkundungspflicht, Heilung, Bruchteilseigentum, Haftung, Nachschüsse und fehlende MaBV-Sicherung. |
| `bauzeit-verzug-vertragsstrafe-und-hoehere-gewalt` | Bauzeit- und Verzugsprüfung beim Bauträgervertrag: verbindlicher Termin, Bezugsfertigkeit, vollständige Fertigstellung, bauablaufbezogene Darlegung, Pandemie/Lieferketten/Wetter, § 313 BGB, Vertragsstrafe und Schadensersatz. |
| `beurkundung-verbraucherfrist-notar-und-bezugsurkunden` | Beurkundungs- und Notarprüfung beim Bauträgervertrag: § 311b BGB, § 17 BeurkG, § 13a BeurkG, Zwei-Wochen-Frist, Bezugsurkunden, Baubeschreibung, Pläne, Reservierung, Vorausleistung und notarielle Amtspflichten. |
| `din-anerkannte-regeln-technik-und-standardwechsel` | Prüft technische Standards im Bauträgervertrag: DIN-Normen, anerkannte Regeln der Technik, Stand der Technik, Stand von Wissenschaft und Technik, Stichtag Abnahme, Standardwechsel, Sowieso-Kosten und Bedenkenhinweis. |
| `druckmuster-schluessel-vormerkung-und-zahlung` | Prüft Bauträger-Druckmuster: Schlüssel nur gegen Zahlung, Vormerkungslöschung, Rücktrittsdrohung, Schlussrate trotz Mängeln, Baustellenzugang, § 320 BGB, § 641 Abs. 3 BGB, § 253 StGB und § 309 Nr. 2/12 BGB. |
| `eigentumssicherung-vormerkung-lastenfreistellung-und-insolvenz` | Eigentumssicherung beim Bauträgervertrag: Auflassungsvormerkung, Rang, Lastenfreistellung, Globalgrundschuld, Pfandfreigabe, Finanzierungsvollmacht, § 103/§ 106 InsO, § 7 MaBV und Schutz vor Zahlung ohne Eigentumspfad. |
| `fall-fingerabdruck-und-schnelltriage` | Fall-Fingerabdruck für Bauträgerakten: extrahiert Urkunde, Verkäufer, Verbraucherrolle, Einheit, Kaufpreis, Raten, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, Baufortschritt, Abnahme- und Streitstand vor jeder Ampel. |
| `geschaeftsfuehrer-architekt-und-bautenstandshaftung` | Prüft Drittansprüche bei Bauträgerprojekten: Geschäftsführerhaftung nach § 823 Abs. 2 BGB i.V.m. § 3/§ 7 MaBV, § 263 StGB, unrichtige Bautenstandsbestätigung, Architekt/Bauleiter, Schutzwirkung zugunsten Erwerber. |
| `hoai-technik-baugrund-und-objektueberwachung` | Technischer Realitätscheck im Bauträgerprojekt: HOAI-Leistungsphasen als Prüfraster, Baugrund, Objektüberwachung, anerkannte Regeln der Technik, Schall, Brand, Feuchte, Energie, Tiefgarage, Aufzug und Unterlagen nach § 650n BGB. |
| `kfw-geg-foerderung-und-unterlagenpflicht-650n` | Prüft Förder-, Energie- und Nachweisunterlagen beim Bauträgervertrag: § 650n BGB, Art. 249 EGBGB, GEG, KfW-/BEG-Versprechen, Energieausweis, Fachunternehmererklärungen, Nachweisrisiko und Schaden. |
| `mabv-agb-klauselmatrix-rot-orange-gruen` | Erstellt eine Bauträgervertrags-Klauselmatrix mit Rot/Orange/Grün-Befunden zu MaBV-Raten, § 650m-Sicherheit, Abnahme, Fertigstellung, Vormerkung, Preisanpassung, WEG-Änderung, Bausoll und Druckmustern. |
| `mabv-ratenplan-sicherheiten-und-notaranderkonto` | MaBV-Prüfung aus Erwerbersicht: § 3 Abs. 1/2 MaBV, sieben Raten, § 7 MaBV, § 12 MaBV, § 650v BGB, 5-%-Sicherheit nach § 650m Abs. 2 BGB, Reservierung, Sonderwünsche, Notaranderkonto und Vermischungsverbot. |
| `nachzuegler-altbau-sanierung-und-kaufrecht-werkrecht` | Prüft Sonderfälle des Bauträgervertrags: Nachzügler nach Abnahme, vermietete Einheiten, Altbau- und Sanierungsobjekte, werkvertragliche Mängelrechte, Kaufrecht, § 650u BGB, § 634a BGB und Abnahmesicherung. |
| `notarhaftung-belehrung-und-streitverkuendung` | Prüft notarielle Amtspflichten im Bauträgervertrag: § 17 BeurkG, § 14 BNotO, § 19 BNotO, MaBV-/AGB-Klauselkontrolle, Preisanpassung, § 650m-Sicherheit, Niedrig-Grundstücksanteil, Bezugsurkunden und Streitverkündung. |
| `preisanpassung-315-saldierung-und-loesungsrecht` | Prüft Preisanpassungsklauseln im Bauträgervertrag: AGB-Charakter trotz Notar, § 309 Nr. 1 BGB, § 307 BGB, § 315 BGB, Saldierung, Transparenz, Lösungsrecht, § 313 BGB und Ausschluss von § 648a BGB. |
| `prozessstrategie-zahlung-feststellung-und-vorschuss` | Entwickelt Prozessstrategie im Bauträgerstreit: Feststellung nicht fälliger Raten, Vorschuss nach § 637 BGB, Klage/Widerklage, Zahlung unter Vorbehalt, Beweislast, Sachverständige, Zinsen und Vergleich. |
| `quellenhygiene-rechtsprechungsanker-und-bughunt` | Quellen- und Bug-Hunt-Skill für Bauträgervertragsprüfungen: verifiziert Normenstand, BGH-/OLG-Rechtsprechung, MaBV, AGB, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, Abnahme, Schlussrate und verhindert BeckRS-/juris-Blindzitate. |
| `sicherheit-650m-fuenf-prozent-einbehalt-und-buergschaft` | Prüft die 5-Prozent-Sicherheit des Verbrauchers im Bauträgervertrag: § 650m Abs. 2 BGB, § 309 Nr. 15 BGB, Einbehalt, Bürgschaft, Kostenabwälzung, Transparenz, Verzicht, MaBV-Raten und Verhältnis zu § 7 MaBV. |
| `sonderwuensche-preisanpassung-und-ausstattungswahl` | Sonderwünsche und Bemusterung im Bauträgervertrag: prüft Form, MaBV-Einordnung, Vorauszahlung, Ausstattungswahl, Mehr-/Minderpreise, Lieferbarkeit, Fristversäumnis, Bauzeitfolgen und Änderung des Sondereigentums. |
| `unwirksame-abnahmeklauseln-dreissig-jahre-und-nachholung` | Prüft unwirksame Abnahmeklauseln im Bauträgervertrag: Erstverwalter, Sachverständige, Erwerbervertreter, Nachzügler, § 640 BGB, § 634a BGB, personale Teilunwirksamkeit, 30-Jahres-Grenze und nachträgliche Abnahme. |
| `verbraucherbauvertrag-650i-650u-widerruf-und-unterlagen` | Trennt Verbraucherbauvertrag nach § 650i BGB vom Bauträgervertrag nach § 650u BGB: § 650l-Widerruf, § 650k Abs. 2/3 BGB, § 650n BGB, §§ 312 ff. BGB, Einzelgewerkvergabe und § 650f Abs. 6 BGB. |
| `verhandlung-drei-dokumente-paket` | Drei-Dokumente-Ausgabe für Bauträgervertragsprüfung: Mandantenanschreiben, klauselorientiertes Gutachten und Schreiben an Bauträger/Notar mit MaBV-, AGB-, Abnahme-, Preisanpassungs-, Bausoll- und Sicherheitsforderungen. |
| `verzugsschadenspositionen-berechnung-und-zinsen` | Berechnet Verzugsschäden beim verspäteten Bauträgerprojekt: Ersatzwohnung, Umzug, Lager, Bereitstellungszinsen, doppelte Miete, Hotel, Nutzungsausfall, Vertragsstrafe, § 287 BGB/ZPO, § 291 BGB, § 289 BGB und § 308 ZPO. |
| `vollstaendige-fertigstellung-schlussrate-und-aussenanlagen` | Prüft Schlussrate im Bauträgervertrag: vollständige Fertigstellung, Bezugsfertigkeit, Außenanlagen, Protokollmängel, Restarbeiten, § 3 Abs. 2 MaBV, § 641 Abs. 3 BGB, § 817/§ 818 BGB und BGH VII ZR 88/25. |
| `wohnflaeche-toleranz-methode-und-minderung` | Prüft Wohnflächenangaben im Bauträgervertrag: WoFlV, DIN 277, Prospektfläche, Planfläche, Toleranzklausel, Beschaffenheitsvereinbarung, § 650k BGB, § 633 BGB, Minderung und Beweis durch Aufmaß. |
| `wohnungseigentum-teilungserklaerung-und-erstverwalter` | WEG- und Teilungserklärungsprüfung beim Bauträgerprojekt: Sondereigentum, Gemeinschaftseigentum, Sondernutzungsrechte, Untergemeinschaften, Kostenverteilung, Erstverwalter, Wartungsverträge und Änderungsvollmachten. |
| `workflow-one-shot-verbraucherpruefung` | One-Shot-Workflow für die verbraucherseitige Prüfung eines deutschen Bauträgervertrags: startet aus Vertrag oder Aktenordner, bildet Fall-Fingerabdruck, prüft MaBV, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, AGB, Bausoll, Abnahme, WEG, Insolv... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
