# Anlagen zu Schriftsätzen

<!-- BEGIN plugin-sofort-download-section (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`anlagen-zu-schriftsaetzen`) | [`anlagen-zu-schriftsaetzen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/anlagen-zu-schriftsaetzen.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Werkmann ./. K+B — Werklohnklage Lackieranlage Eschweiler — Anlagenkonvolut-Verfahren** (`anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler`) | [Gesamt-PDF lesen](../testakten/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler/gesamt-pdf/anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler_gesamt.pdf) | [`testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-anlagen-zu-schriftsaetzen-konzernumstellung-baudaten-werkmann-baesweiler.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist die Anlagenkanzlei im Kleinen: Es nimmt einen Schriftsatz, einen chaotischen Mandantenordner oder ein schon halb nummeriertes Anlagenpaket und macht daraus eine nachvollziehbare, gerichtstaugliche Anlagenstruktur.

Es hilft besonders dann, wenn nicht einfach „Anlage K1 bis K12“ vorliegt, sondern wenn eine echte Akte lebt: E-Mails mit Anhängen, Scans ohne OCR, Excel-Tabellen, Fotos, Chat-Screenshots, mehrere Vertragsfassungen, fremdsprachige Unterlagen, doppelte Dateien, geschwärzte Drittunterlagen, beA-Grenzen, Verfahrenswechsel und Richterhinweise. Das Plugin führt dann nicht nur eine Nummerierung aus, sondern baut eine Arbeitslogik: Welche Tatsache soll durch welche Anlage belegt werden? Welche Datei gehört wirklich zu K1? Welche Unterlagen sind nur Konvolutbestandteil? Welche Anlage ist zu groß, unleserlich, falsch benannt, doppelt oder im Schriftsatz nicht eingeführt?

## Wofür es gedacht ist

| Situation | Was das Plugin macht | Ergebnis |
| --- | --- | --- |
| Klage/Replik liegt vor, Anlagen sind noch ungeordnet | Schriftsatz lesen, Beweisanker erkennen, K-Nummern vorschlagen, Dateien zuordnen | K1/K2/K3-Reihenfolge, Anlagenverzeichnis, Lückenliste |
| Anlagen sind schon nummeriert, aber niemand traut dem Paket | Prüfmodus: Nummern, Zitate, Dateien, Stempel, Namen, Lesbarkeit und beA-Fähigkeit prüfen | Fehlerprotokoll mit Korrekturplan |
| Mandant liefert Datenraum/ZIP/USB-Stick | Duplikate, Fassungen, Hashes, Dateitypen, Zeitfolge und Relevanz sortieren | Belegmatrix und Nachforderungsliste |
| Eine Anlage ist ein Konvolut | Deckblatt, Untergliederung, interne Seiten-/Dokumentlogik, kurze Erläuterung für Gericht | `Anlage K1` mit `K1.1`, `K1.2`, `K1.3` |
| Elektronische Einreichung steht bevor | Dateinamen, PDF/OCR, Paketgrößen, Anlagenverzeichnis, Prüfvermerk | beA-/ERV-taugliches Versandpaket |

## Der K1-Gedanke

Die erste Anlage ist fast nie nur eine Datei. In großen Verfahren ist `K1` häufig der Orientierungspunkt für das Gericht: Vertrag, Auftrag, Rahmenvereinbarung, Nachtrag, Bestätigungsmail, Protokoll oder Dokumentenfamilie. Das Plugin behandelt `K1` deshalb als Sortierproblem:

1. **Was soll K1 beweisen?** Nicht „alles zum Vertrag“, sondern eine konkrete Tatsache.
2. **Ist K1 Einzelanlage oder Konvolut?** Bei Konvolut: Deckblatt, Reihenfolge, interne Kurzbezeichnungen.
3. **Welche Fassungen gibt es?** Entwurf, unterschriebene Fassung, Scan, OCR-PDF, E-Mail-Anhang, spätere Ergänzung.
4. **Welche Datei ist die gerichtliche Fassung?** Die anderen Fassungen wandern in den internen Hash-/Versionenlog.
5. **Wie wird K1 im Schriftsatz eingeführt?** Der Schriftsatz muss den Tatsachenkern selbst tragen; die Anlage belegt ihn nur.

## Drei Arbeitsmodi

**Auto-Benennung:** Der Schriftsatz enthält noch keine Nummern. Das Plugin liest die Beweisstellen und schlägt die Reihenfolge vor.

**Schriftsatz folgt:** Der Schriftsatz enthält bereits `Anlage K...`-Verweise. Das Plugin sucht die passenden Dateien, erkennt Lücken und meldet Überschüsse.

**Prüfmodus:** Ein fertiges Anlagenpaket wird gegengeprüft: `K7` fehlt, `K12` ist doppelt, `K18` wird im Schriftsatz nie erwähnt, `K23` hat keinen OCR-Text, `K31` enthält ungeschwärzte Drittinformationen.

## Typische Outputs

- Anlagenverzeichnis für Gericht und Kanzleiakte.
- K/B/AST/AG-Nummerierung mit eindeutiger Dateinamenkonvention.
- Konvolutdeckblätter für Sammelanlagen.
- Belegmatrix: Tatsachenbehauptung ↔ Schriftsatzstelle ↔ Anlage ↔ Datei ↔ Status.
- Hash-/Duplikat-/Fassungslog für interne Kontrolle.
- beA-Versandliste mit Paketgrößen, Dateinamen und letzten Prüfpunkten.
- Nachforderungsliste an Mandant oder Sachbearbeitung.
- Berichtigungs- oder Nachreichungsplan nach gerichtlichem Hinweis.

## Wichtig

Anlagen ersetzen keinen Tatsachenvortrag. Wenn eine Behauptung entscheidungserheblich ist, muss sie im Schriftsatz stehen. Die Anlage belegt, erläutert oder vertieft; sie darf nicht der Ort sein, an dem der eigentliche Vortrag versteckt wird.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Besonders wichtige Skills

| Skill | Zweck |
| --- | --- |
| `anlagen-zu-schriftsaetzen-allgemein` | Kaltstart, Triage, Nummernkreis, Ziel-Schriftsatz, K1-Frage und Routing in die passenden Spezial-Skills. |
| `anlagen-zu-schriftsaetzen` | Hauptworkflow für Auto-Benennung, Schriftsatz-folgt-Modus, Prüfmodus und Reparatur nach Hinweis. |
| `k1-sortierwerkstatt` | Baut aus Vertrag, Nachtrag, Mail, Scan und OCR-Fassung eine klare Leit-Anlage `K1` oder ein K1-Konvolut. |
| `schriftsatz-anlagen-mapping` | Verknüpft Tatsachenvortrag, Schriftsatzstelle, Beweisangebot, Anlage und Datei in einer Belegmatrix. |
| `anlagen-duplikate-versionen-hashlog` | Erkennt Dubletten, Versionen, OCR-Kopien und die maßgebliche gerichtliche Fassung. |
| `bea-paketierung-groessen-und-versandplan` | Plant Dateinamen, Paketgrößen, Teilpakete, Begleitvermerk und Eingangskontrolle. |
| `anlagen-qualitygate-finalcheck` | Letzter strenger Check vor Versand: Nummern, Zitate, Dateien, OCR, Schwärzung, Stempel, Paket. |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 115 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlage-fehlerkatalog` | Anlage Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `anlage-red-anlagen-anlagenkonvolut-sonderfall` | Anlage: Red-Team und Qualitätskontrolle. |
| `anlagen-an-assistenz-uebersetzungspflicht` | Erzeugt klare Arbeitsanweisungen für Kanzleiteam, Assistenz, Legal Tech oder externen Dienstleister: was umbenennen, scannen, stempeln, schwärzen, prüfen im Anlagen zu Schriftsätzen. |
| `anlagen-aus-datenraum-und-sharepoint` | Überführt Datenraum-/SharePoint-/DMS-Exporte in Anlagenlogik: Pfade, Versionen, Berechtigungen, Exportzeitpunkt, Index und gerichtliche Fassung. |
| `anlagen-aus-edv-systemen` | Anlagen aus IT-Systemen (ERP-Auszuege, Datenbankexporte, Logdateien): Beweiskraft, Manipulationsschutz, Hashverfahren, Begleitvermerk Erstellung. Empfehlung: Export mit Zeitstempel, Hashprotokoll, ggf. Sachverstaendigenanhoerung Authenti... |
| `anlagen-aus-mandantenmaterial` | Mandantenmaterial in Anlagen umwandeln: Posteingang, E-Mails, PDFs, Verträge, Rechnungen, Korrespondenz. Markiert geschwaerzte Stellen, prüft Vollstaendigkeit, schlaegt sinnvolle Kuerzungen vor. Erkennt vertrauliche Inhalte, die für da... |
| `anlagen-bei-berufung-revision` | Anlagen in Berufung und Revision: bisheriges Anlagenverzeichnis uebernehmen oder neu nummerieren? Empfehlung: Berufungsklaegeranlagen als BK1, BK2 ..., Berufungsbeklagter BB1, BB2 ... Revisionsanlagen sind ueblich nur ergaenzend; Schwerp... |
| `anlagen-bei-eilantrag-eu-arrest` | Anlagen für einstweilige Verfuegung und Arrest: Glaubhaftmachung § 294 ZPO durch Anlagen, eidesstattliche Versicherung als Anlage, parate Beweismittel. Hohe Anforderungen Vollstaendigkeit. Output Standard-Anlagensatz für wettbewerbsrecht... |
| `anlagen-berufung-revision-eilantrag-eu-bilder` | Anlagen in Berufung und Revision: bisheriges Anlagenverzeichnis uebernehmen oder neu nummerieren? Empfehlung: Berufungsklaegeranlagen als BK1, BK2 ..., Berufungsbeklagter BB1, BB2 ... Revisionsanlagen sind ueblich nur ergaenzend; Schwerp... |
| `anlagen-bilder-screenshots` | Bilder und Screenshots als Anlagen: Beweiskraft, Manipulationsanfaelligkeit, EXIF-Daten, Metadaten. Empfehlung: Original und Vergroesserung beifuegen, EXIF-Export anhaengen, Standortdaten transparent machen. Bei Screenshots: voller Brows... |
| `anlagen-check-zustellung-redaktion-dsgvo` | Quality-Check für Anlagenpaket vor Zustellung: Vollstaendigkeit (alle Bezuege im Schriftsatz haben passende Anlage), Lesbarkeit (OCR, kein Schwarzbalken), Schwaerzung (DSGVO und Mandantengeheimnisse), Format (PDF/A wo gefordert). Prüfli... |
| `anlagen-duplikate-versionen-hashlog` | Erkennt doppelte Dateien, verschiedene Fassungen desselben Dokuments, OCR-Kopien, E-Mail-Anhänge und manipulativ wirkende Metadatenbrüche; erzeugt ein Hash- und Versionenprotokoll. |
| `anlagen-elektronische-dokumente-format` | Spezialfall elektronische Dokumente als Anlage: ERVV-Vorgaben, qualifizierte elektronische Signatur, Datei-Format-Whitelist nach ERVV, maximale Groesse, beA-Vorgaben, Container-PDF. Prüfraster und Mustertexte für Eingang bei Gericht im... |
| `anlagen-elektronische-dokumente-spezial` | Spezialfall elektronische Dokumente als Anlage: ERVV-Vorgaben, qualifizierte elektronische Signatur, Datei-Format-Whitelist nach ERVV, maximale Groesse, beA-Vorgaben, Container-PDF. Prüfraster und Mustertexte für Eingang bei Gericht. |
| `anlagen-format-und-dateinamen` | Format und Dateinamen für Anlagen: K-01_2024-03-12_Mietvertrag.pdf. Maschinenlesbar, sortierbar, beA-kompatibel. Maximal 3 Ebenen Unterordner, keine Sonderzeichen, keine Umlaute in Dateinamen, durchgehend kleingeschrieben. |
| `anlagen-fuer-bea-versand` | Anlagen für beA-Versand vorbereiten: PDF/A-konform, max. zulaessige Dateigroesse beachten, OCR über Scans laufen lassen, korrekt strukturiertes XJustiz-Begleitformular. Liste der Anlagen pro Schriftsatz mit Prüfsumme. Verhindert wieder... |
| `anlagen-fuer-glaubhaftmachung` | Spezialfür Eilverfahren: Anlagen, eidesstattliche Versicherung, Screenshots, E-Mails, Fotos und Glaubhaftmachungsdichte nach § 294 ZPO ordnen. |
| `anlagen-haftpflicht-versicherer` | Anlagen-Pflicht gegenueber Haftpflichtversicherer (Berufshaftpflicht, Hausratversicherung, KFZ): welche Anlagen müssen mit Schadenanzeige eingereicht werden, was der Versicherer im Regulierungsverfahren erwartet. Prüfraster aus § 31 VV... |
| `anlagen-konvention-k-b-erlaeutert` | Konvention erklaert und korrekt eingesetzt: K-Anlagen Kläger, B-Anlagen Beklagter, ZN-Anlagen Zeugen, GA-Anlagen Gutachten, AS-Anlagen Anlagenband. Wann Klein-/Grosschreibung, wann Bindestrich. Wechselt sauber, wenn der Mandant im Vorpr... |
| `anlagen-konvention-mandantenfreundlich` | Anlagen-Konvention mandantenfreundlich: durchlaufende Nummerierung K1 / K2 / K3 ff. für Klägerseite, B1 / B2 / B3 ff. für Beklagtenseite, Anlagenbaender, Inhaltsverzeichnis, beA-konforme PDF-Bezeichnung. Mustertext für Anlagenverzeichnis. |
| `anlagen-konvertierung-zahlen-technische-schwellen` | Prüft PDF-Konvertierung, Dateigrößen, Seitenzahlen, OCR und technische Schwellen vor Versand. |
| `anlagen-portal-bea-einreichungslogik` | Prüft, wie Anlagen technisch eingereicht werden: beA, ERV, Portal, Datenträger, mehrere Teilpakete, Begleitvermerk und Eingangsprüfung. |
| `anlagen-prozessual-pruefung-spezial` | Spezialfall prozessuale Anlagenpruefung: keine Substantiierung durch blossen Anlagenverweis (BGH-Linie), eigener Vortrag noch im Schriftsatz erforderlich, Tatsachenkern aus Anlage in den Text uebernehmen. Prüfraster und Korrektur-Bauste... |
| `anlagen-quality-check-vor-zustellung` | Quality-Check für Anlagenpaket vor Zustellung: Vollstaendigkeit (alle Bezuege im Schriftsatz haben passende Anlage), Lesbarkeit (OCR, kein Schwarzbalken), Schwaerzung (DSGVO und Mandantengeheimnisse), Format (PDF/A wo gefordert). Prüfli... |
| `anlagen-qualitygate-finalcheck` | Finaler Red-Team-Check vor Einreichung: Nummern, Schriftsatzverweise, Dateien, Stempel, OCR, Schwärzung, Dateinamen, beA-Paket, Lücken und Begleitvermerk. |
| `anlagen-redaktion-dsgvo-geschgehg` | Prüft Anlagen vor Einreichung auf personenbezogene Daten, Geschäftsgeheimnisse, Drittmandate, Schwärzungsbedarf und Redaktionsprotokoll. |
| `anlagen-schriftsaetze-k1-sortierung` | Baut aus Schriftsatz und Dateiliste eine Matrix mit Tatsachen, Belegen, fehlenden Anlagen und Nachforderungen. |
| `anlagen-schriftsaetze-start-belegmatrix-fristen` | Einstieg, Schnelltriage und Fallrouting im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. B... |
| `anlagen-schwaerzen-anonymisieren` | Anlagen schwaerzen und anonymisieren: personenbezogene Daten unbeteiligter Dritter (Mitarbeiter, Kunden, Patienten) entfernen, Kontonummern bis auf letzte 3 Ziffern schwaerzen, Geburtsdaten redigieren, soweit nicht streitrelevant. Mat2-... |
| `anlagen-stempel-und-deckblattlogik` | Legt fest, wie Anlagenstempel, Konvolutdeckblätter, Unteranlagen und Seiten-/Dokumentbezeichnungen aussehen müssen, damit Gericht und Gegner nicht suchen müssen. |
| `anlagen-stempelbild-entscheidungsvorlage` | Entscheidet Stempelbild, Deckblatt, Anlagenverzeichnis und Mandantenfreigabe so, dass die Anlage optisch und logisch eindeutig ist. |
| `anlagen-tatbestand-beweis-und-belege` | Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `anlagen-uebergabe-an-assistenz-und-legal-tech` | Erzeugt klare Arbeitsanweisungen für Kanzleiteam, Assistenz, Legal Tech oder externen Dienstleister: was umbenennen, scannen, stempeln, schwärzen, prüfen. |
| `anlagen-uebersetzungspflicht` | Fremdsprachige Anlagen: Übersetzungspflicht § 184 GVG. Beglaubigte oder einfache Übersetzung? Gericht kann Übersetzung verlangen oder Ablehnung der Beruecksichtigung androhen. Empfehlung: bei zentralen Urkunden beglaubigte Übersetzun... |
| `anlagen-vorlagepflicht-141-zpo` | Anordnung der Urkundenvorlage nach § 142 ZPO und § 421 ZPO: wann kann das Gericht die Vorlage einer Urkunde anordnen, wann hat ein Beweisfuehrer Anspruch auf Vorlage durch den Gegner. Prüfraster, Antragsformulierung und Folgen Nichtvorl... |
| `anlagen-zur-substantiierung-pflicht` | Anlagen ersetzen keine Substantiierung im Schriftsatz: 'wegen der weiteren Einzelheiten wird auf Anlage K5 verwiesen' ist nicht ausreichend (BGH X ZR 39/16). Prüfraster: Welche Behauptung wird substanziiert, welche durch Anlage nur bele... |
| `anlagenband-strukturieren` | Anlagenband strukturieren: Trennblaetter, Inhaltsverzeichnis, Reihenfolge nach Schriftsatzbezug, durchgehende Foliierung. Anweisung für Kanzleimitarbeiter zur physischen oder elektronischen Erstellung. Für beA-Versand zusaetzlich ein du... |
| `anlagenband-strukturieren-anlagenbezug` | Anlagenband strukturieren: Trennblaetter, Inhaltsverzeichnis, Reihenfolge nach Schriftsatzbezug, durchgehende Foliierung. Anweisung für Kanzleimitarbeiter zur physischen oder elektronischen Erstellung. Für beA-Versand zusaetzlich ein du... |
| `anlagenbezug-im-schriftsatz` | Wie Anlagen im Schriftsatz richtig eingefuehrt werden: 'Beweis: Vorlage der Anlage K1' oder 'wie sich aus Anlage K3 ergibt'. Erste Erwaehnung mit Kurztitel und Datum, danach nur K1, K2 ... Vermeidet sprachliche Fehler bei mehrfachem Bezug. |
| `anlagenkonvolut-konsolidieren` | Anlagenkonvolut aus Mandanten-ZIP konsolidieren: Duplikate über Hashvergleich erkennen, gleiche Verträge in unterschiedlichen Fassungen identifizieren, sortieren nach Datum und Thema, Lueckenanalyse (welcher Vertrag wird im Schriftsatz... |
| `anlagenkonvolut-sonderfall-edge-case` | Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion ode... |
| `anlagenkonvolut-sonderfall-und-edge-case` | Anlagenkonvolut: Sonderfall und Edge-Case-Prüfung. |
| `anlagenmatrix-csv-xlsx-aufbau` | Entwirft eine robuste Anlagenmatrix für große Verfahren mit Dok-ID, Nummernkreisen, Schriftsatzstelle, Beweiszweck, Quelle, Hash, Status, Datenschutz und Nachreichung. |
| `anlagenverzeichnis-gericht-kanzlei-und-intern` | Erstellt getrennte Anlagenverzeichnisse: schlank für Gericht, ausführlicher für Kanzlei und technisch mit Dateipfad, Hash, Quelle und Bearbeitungsstatus. |
| `anlagenverzeichnis-grundaufbau` | Anlagenverzeichnis nach deutscher Anwaltsuebung aufbauen: K1, K2, K3 ... für Klägerseite, B1, B2 ... für Beklagtenseite. Kurztitel, Datum, Funktion (Beweismittel zu welcher Behauptung), Fundstelle im Schriftsatz. Loest Doppel-Nummerieru... |
| `anlagenverzeichnis-kanzlei-grundaufbau-bea` | Erstellt getrennte Anlagenverzeichnisse: schlank für Gericht, ausführlicher für Kanzlei und technisch mit Dateipfad, Hash, Quelle und Bearbeitungsstatus im Anlagen zu Schriftsätzen. |
| `anschluss-routing` | Anschluss-Routing für Anlagen zu Schriftsätzen: wählt den nächsten Spezial-Skill nach Engpass (Klageerwiderungsfrist, Verträge, Korrespondenz, Rechnungen), dokumentiert Router-Entscheidung mit Begründung. |
| `arial-mandantenkommunikation-entscheidungsvorlage` | Entscheidet Stempelbild, Deckblatt, Anlagenverzeichnis und Mandantenfreigabe so, dass die Anlage optisch und logisch eindeutig ist im Anlagen zu Schriftsätzen. |
| `baut-beweislast-benennt-bereits-excel` | Prüft, ob die Anlage eine konkrete Darlegung trägt oder nur einen pauschalen Anlagenverweis kaschiert; trennt Tatsachenvortrag, Beweisangebot und bloße Hintergrundunterlage im Anlagen zu Schriftsätzen. |
| `baut-beweislast-darlegungslast` | Prüft, ob die Anlage eine konkrete Darlegung trägt oder nur einen pauschalen Anlagenverweis kaschiert; trennt Tatsachenvortrag, Beweisangebot und bloße Hintergrundunterlage. |
| `bea-paketierung-groessen-und-versandplan` | Plant elektronische Anlagenpakete für beA/ERV: Dateinamen, Reihenfolge, Paketgrößen, PDF/OCR, Nachsendungen, Begleitvermerk und finaler Versandcheck. |
| `benennt-compliance-dokumentation-aktenvermerk` | Benennt: Compliance-Dokumentation und Aktenvermerk: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion od... |
| `benennt-compliance-dokumentation-und-akte` | Benennt: Compliance-Dokumentation und Aktenvermerk. |
| `bereits-abschlussprodukt-uebergabe` | Bereits: Abschlussprodukt und Übergabe: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahren... |
| `bereits-abschlussprodukt-und-uebergabe` | Bereits: Abschlussprodukt und Übergabe. |
| `berufung-beschwerde-und-neue-anlagen` | Prüft Anlagen in Rechtsmittelverfahren: Übernahme alter Nummern, neue Anlagen, § 531 ZPO-Risiken, Verweis auf Vorinstanz und Synchronisation. |
| `beweisangebot-anlage-emails-chats-excel` | Zeugenbeweis korrekt über Anlagen unterstuetzen: schriftliche Zeugenaussagen sind keine Anlagen-Beweismittel im Strengbeweis, können aber als praeprozessuale Information dienen. Anlagen, die die Glaubhaftigkeit stuetzen (Chatverlauf, E... |
| `beweisangebot-anlage-zeugen` | Zeugenbeweis korrekt über Anlagen unterstuetzen: schriftliche Zeugenaussagen sind keine Anlagen-Beweismittel im Strengbeweis, können aber als praeprozessuale Information dienen. Anlagen, die die Glaubhaftigkeit stuetzen (Chatverlauf, E... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `dokumente-intake` | Dokumentenintake für Anlagen zu Schriftsätzen: sortiert Verträge, Korrespondenz, Rechnungen, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Lichtbilder); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einstieg-routing` | Einstieg, Triage und Routing für Anlagen zu Schriftsätzen: ordnet Rolle (Mandant, Gegenpartei, Gericht), markiert Frist (Klageerwiderungsfrist), wählt Norm (§§ 131/253 ZPO Anlagen, § 416 ZPO Privaturkunde, § 437 ZPO öffentliche Urkunde)... |
| `emails-chats-screenshots-als-anlagen` | Macht aus EML/MSG, Chatverläufen und Screenshots gerichtstaugliche Anlagen mit Headern, Kontext, Exportlogik, Vollständigkeitswarnung und Beweiszweck. |
| `excel` | Macht Tabellenanlagen im Schriftsatz verständlich: Zahlenkern, Rechenweg, PDF-Ausdruck, Anlagenzitat und kurze Erläuterung. |
| `excel-schriftsatz-brief-und-memo-bausteine` | Macht Tabellenanlagen im Schriftsatz verständlich: Zahlenkern, Rechenweg, PDF-Ausdruck, Anlagenzitat und kurze Erläuterung im Anlagen zu Schriftsätzen. |
| `excel-tabellen-und-zahlenbeweis` | Bereitet XLSX/CSV als Anlage auf: Ausdruck, Summenlogik, Formelrisiko, Quelldaten, Rechenweg, PDF-Fassung und Anlagenbezug im Schriftsatz. |
| `fremdsprachige-anlagen-uebersetzung` | Prüft fremdsprachige Anlagen: Relevanz, Übersetzungsbedarf, beglaubigte oder Arbeitsübersetzung, Auszug statt Vollübersetzung, Kosten und Schriftsatzanker. |
| `frist-eilversand-schiedsverfahren-anlagenband` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Anlagen zu Schriftsätzen. |
| `frist-und-eilversand-anlagenpaket` | Minimalpfad bei drohender Frist: welche Anlagen müssen jetzt mit, welche können nachgereicht, welche Risiken müssen im Schriftsatz offen gehalten werden. |
| `fristen-und-risikoampel` | Fristen- und Risikoampel: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `gerichtlichen-fristen-form-und-zustaendigkeit` | Gerichtlichen: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `gerichtlichen-fristen-form-zustaendigkeit-rechtsweg` | Gerichtlichen: Fristen, Form, Zuständigkeit und Rechtsweg: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sank... |
| `haftpflicht-versicherer-konvention-k` | Anlagen-Pflicht gegenueber Haftpflichtversicherer (Berufshaftpflicht, Hausratversicherung, KFZ): welche Anlagen müssen mit Schadenanzeige eingereicht werden, was der Versicherer im Regulierungsverfahren erwartet. Prüfraster aus § 31 VV... |
| `k1-anlagenpaket-aus-chaosordner` | Aus einem Mandantenordner mit beliebigen Dateinamen die erste Anlagenstaffel K1 bis K20 bilden: priorisieren, umbenennen, Lücken markieren, Rückfragen ausgeben. |
| `k1-anlagenpaket-k1-sortierwerkstatt` | Aus einem Mandantenordner mit beliebigen Dateinamen die erste Anlagenstaffel K1 bis K20 bilden: priorisieren, umbenennen, Lücken markieren, Rückfragen ausgeben im Anlagen zu Schriftsätzen. |
| `k1-sortierwerkstatt` | K1-Leitanlage sortieren: Vertrag, Auftrag, Nachtrag, E-Mail-Anhang, Scan, OCR-Fassung und spätere Ergänzungen zu einer gerichtstauglichen Anlage K1 oder einem K1-Konvolut ordnen. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. B... |
| `konform-interessen` | Konform: Mehrparteienkonflikt und Interessenmatrix: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion od... |
| `konform-interessen-konvertiert-oben` | Konform: Mehrparteienkonflikt und Interessenmatrix. |
| `konvertiert-zahlen-schwellen-und-berechnung` | Prüft PDF-Konvertierung, Dateigrößen, Seitenzahlen, OCR und technische Schwellen vor Versand im Anlagen zu Schriftsätzen. |
| `logik-quellenkarte` | Logik Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mandantenkommunikation` | Mandantenkommunikation: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `massenanlagen-sampling-repraesentativitaet` | Hilft bei Tausenden gleichartiger Dokumente: Auswahl, repräsentative Beispiele, Nachreichungsvorbehalt, Anlagenband und Substantiierungsgrenze. |
| `massenanlagen-sampling-und-repraesentativitaet` | Hilft bei Tausenden gleichartiger Dokumente: Auswahl, repräsentative Beispiele, Nachreichungsvorbehalt, Anlagenband und Substantiierungsgrenze im Anlagen zu Schriftsätzen. |
| `mehrparteien-rollen-und-praefixe` | Entwirft Nummernkreise bei Streitgenossen, Nebenintervention, Widerklage, Drittwiderklage, selbständigem Beweisverfahren und parallelen Verfahren. |
| `nachreichung-berichtigung-ocr-scan-original` | Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung im Anlagen zu Schriftsätzen. |
| `nachreichung-berichtigung-und-gerichtshinweis` | Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung. |
| `oben-formular-portal-und-einreichung` | Prüft, wie Anlagen technisch eingereicht werden: beA, ERV, Portal, Datenträger, mehrere Teilpakete, Begleitvermerk und Eingangsprüfung im Anlagen zu Schriftsätzen. |
| `ocr-scan-lesbarkeit-und-beweiswert` | Prüft gescannte Anlagen auf Lesbarkeit, OCR-Durchsuchbarkeit, Seitenreihenfolge, abgeschnittene Ränder, schiefe Scans und Beweiswertprobleme. |
| `original-abschrift-kopie-elektronische` | Klären, wann Original, beglaubigte Abschrift, einfache Kopie, Scan, elektronisches Dokument oder Ausdruck als Anlage sinnvoll oder erforderlich ist. |
| `original-abschrift-kopie-und-elektronische-fassung` | Klären, wann Original, beglaubigte Abschrift, einfache Kopie, Scan, elektronisches Dokument oder Ausdruck als Anlage sinnvoll oder erforderlich ist im Anlagen zu Schriftsätzen. |
| `output-waehlen` | Output-Wahl für Anlagen zu Schriftsätzen: stimmt Adressat (Mandant, Gegenpartei, Gericht), Frist (Klageerwiderungsfrist) und Form auf den Zweck ab — typische Outputs: Anlagenverzeichnis K/B-Nummerierung, Anlagenkonvolut, Schwärzungsanlei... |
| `pruefmodus-fristennotiz-datenraum-sharepoint` | Validiert ein vorhandenes Anlagenpaket und gibt eine kurze Fristennotiz plus nächste Handlung aus im Anlagen zu Schriftsätzen. |
| `pruefmodus-fristennotiz-naechster-schritt` | Validiert ein vorhandenes Anlagenpaket und gibt eine kurze Fristennotiz plus nächste Handlung aus. |
| `quellen-livecheck` | Quellen-Live-Check für Anlagen zu Schriftsätzen: prüft Normen (§§ 131/253 ZPO Anlagen, § 416 ZPO Privaturkunde, § 437 ZPO öffentliche Urkunde) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Zivilgerichte und Quel... |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand |
| `schiedsverfahren-anlagenband-und-datentraeger` | Plant Anlagenbände im Schiedsverfahren: mehrere Originale, USB-Sticks, PDF-Bundles, Index, Hashliste, Verfahrensanordnung und parallele elektronische Struktur. |
| `schriftsaetzen` | Anwalt hat Schriftsatz fertig und muss Anlagen korrekt benennen nummerieren und als PDF-Konvolut aufbereiten. Anlagemanagement gerichtliche Schriftsaetze. Prüfraster: Schriftsatz lesen Beweisstuecke erkennen sortieren beA-konforme Benenn... |
| `schriftsaetzen-dokumentenmatrix-und-lueckenliste` | Baut aus Schriftsatz und Dateiliste eine Matrix mit Tatsachen, Belegen, fehlenden Anlagen und Nachforderungen im Anlagen zu Schriftsätzen. |
| `schriftsatz-anlagen-mapping` | Schriftsatzstellen, Tatsachenbehauptungen, Beweisangebote und Anlagen in eine Matrix bringen; erkennt fehlende, doppelte und nur scheinbar belegte Anlagen. |
| `schriftsatz-verhandlung-vergleich` | Schriftsatz: Verhandlung, Vergleich und Eskalation: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion od... |
| `sortiert-risikoampel-gegenargumente` | Sortiert: Risikoampel, Gegenargumente und Verteidigungslinien: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung,... |
| `sortiert-risikoampel-und-gegenargumente` | Sortiert: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `sortiert-stempelt-word` | Schriftsatz: Verhandlung, Vergleich und Eskalation. |
| `stempelt-internationaler-bezug-schnittstellen` | Stempelt: Internationaler Bezug und Schnittstellen: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion od... |
| `stempelt-internationaler-bezug-und-schnittstellen` | Stempelt: Internationaler Bezug und Schnittstellen. |
| `tatbestandsmerkmale-beweisfragen-beleglage` | Anlagen: Tatbestandsmerkmale, Beweisfragen und Beleglage: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sankt... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Anlagen zu Schriftsätzen: trennt fehlende Tatsachen von fehlenden Belegen (Verträge, Korrespondenz, Rechnungen), nennt pro Lücke Beweisthema, Beschaffungsweg (Zivilgerichte), Frist und Ersatznachweis. |
| `word` | Bereitet Word-, PDF- und Scan-Anlagen für Gerichts- oder Behördenwege vor: Konvertierung, Lesezeichen, PDF/A, Dateiname, Deckblatt. |
| `word-behoerden-gericht-und-registerweg` | Bereitet Word-, PDF- und Scan-Anlagen für Gerichts- oder Behördenwege vor: Konvertierung, Lesezeichen, PDF/A, Dateiname, Deckblatt im Anlagen zu Schriftsätzen. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Anlagen zu Schriftsätzen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Anlagen zu Schriftsätzen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Anlagen zu Schriftsätzen. |
| `zeitleiste-und-belegkette` | Baut aus Anlagen eine Chronologie und zeigt zu jedem Ereignis, welcher Beleg trägt, welcher nur plausibilisiert und welcher fehlt. |
| `zuordnung-erstpruefung-rollenklaerung-mandatsziel` | Zuordnung: Erstprüfung, Rollenklärung und Mandatsziel: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion... |
| `zuordnung-zeitleiste-belegkette` | Zuordnung: Erstprüfung, Rollenklärung und Mandatsziel. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`anlagen-zu-schriftsaetzen.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/anlagen-zu-schriftsaetzen.md) (41 KB)
- Im Repo: [`testakten/megaprompts/anlagen-zu-schriftsaetzen.md`](../testakten/megaprompts/anlagen-zu-schriftsaetzen.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->
