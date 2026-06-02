# Audit Testakten v52 — Fehlersuche

Stand: 30.05.2026
Bearbeiter: Claude (Codex-Audit-Lauf)
Bearbeitungsmethode: Pattern-Grep über `testakten/`-Verzeichnis, anschliessend punktuelle Webverifikation einzelner Aktenzeichen über `bundesgerichtshof.de`, `dejure.org` und `bundesverfassungsgericht.de`. Nur frei einsehbare Quellen, keine kostenpflichtigen Datenbanken.

Nachlauf 31.05.2026: Die als hoch priorisierten Punkte aus diesem Audit wurden nachgezogen, soweit sie noch im aktuellen Arbeitsstand vorhanden waren. Konkret: BGH VIII ZR 263/22 ist in der Energierecht-Akte auf 27.09.2023 korrigiert; Testakten-Verweise auf das frühere eigenständige Sozialrechts-Plugin sind in den Testakten-Übersichten auf `fachanwalt-sozialrecht` ersetzt; die § 17-TzBfG-Frist in der Vogt-Akte wurde auf 23.03.2026 korrigiert; sichtbare "Testakte"-Marker in einzelnen Aktenstücken und eingebetteten PDFs wurden entfernt. Die übrigen Verifikationshinweise bleiben bewusst als Prüfvermerke stehen, soweit die Akte selbst Recherche- oder Red-Team-Material abbildet.

## A. Halluzinierte Aktenzeichen

Nachfolgend Verdachtsfälle: Aktenzeichen, deren Existenz in den geprüften öffentlichen Quellen nicht eindeutig nachgewiesen werden konnte oder deren Datum von der publizierten Entscheidung abweicht. "Verdacht" bedeutet nicht zwingend Falschzitat, sondern Verifikationsbedarf vor Verwendung.

### A.1 Sicher fragwürdig / Datum stimmt nicht

- `testakten/energierecht-stadtwerke-quartier/04_vertraege/waermeliefervertrag_hafenbogen.md:339` — Zitiert "BGH-Linie VIII ZR 263/22 (Urteil vom 06.03.2024)" zur Wirksamkeit Fernwärme-Preisanpassungsklauseln. Verifiziert (dejure.org, NWB): Das Urteil VIII ZR 263/22 wurde am **27.09.2023** verkündet, nicht am 06.03.2024. Datum korrigieren.

### A.2 Verdacht — Aktenzeichen nicht in freien Quellen auffindbar

- `testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/16_befangenheitsantrag_entwurf.md:79` und Z. 89 — Verweis auf "BGH, Beschluss vom 09.05.2017, VI ZB 51/16" zur Befangenheit eines SV. Aktenzeichen ist in dejure.org, bundesgerichtshof.de und der allgemeinen Treffer-Liste nicht direkt zu verifizieren. Der Schriftsatz markiert die Stelle selbst als "Verifikation … bislang ausstehend" und enthält eine ausdrückliche Anweisung des Senior-Reviewers, das Aktenzeichen vor Einreichung zu prüfen — dieses Audit-Beispiel ist daher absichtlich-fragwürdig (eingebauter Demonstrationszweck). Beibehalten, im Skill aber als Prüfbeispiel kennzeichnen.

- `testakten/insolvenzforderungsanmeldungspruefung-phoenix-solar/09_anmeldung_gesellschafterdarlehen_nachrang.md:84` — "BGH, Urt. v. 13.10.2022 – IX ZR 28/21". Eine BGH-Entscheidung mit dem Datum 13.10.2022 existiert (IX ZR 130/21), das Aktenzeichen IX ZR 28/21 ist in dejure.org-Suche nicht eindeutig getroffen. Vor Verwendung verifizieren.

- `testakten/gesellschaftsgruender-streit-roeschen-tech/06_Anfechtungsklage_Christine.md:115` — "BGH, Beschl. v. 08.11.2022 - II ZR 91/21". Verifiziert. Aber zugleich: "BGH, Urt. v. 25.01.2022 - II ZR 50/20" — verifiziert.

- `testakten/lumen-studios-insolvenz-strafverfahren/07_Vernehmung_Bergmann_22-10-2024.md:58` — "BGH II ZR 130/05 u.a." zur Ressortverteilung. Die Leit-Entscheidung zur Ressortverteilung von 2018 ist BGH II ZR 11/17. II ZR 130/05 ist nicht ohne weitere Quelle verifizierbar. Vor Verwendung prüfen.

- `testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck/Notiz_Erstgespraech_Haspelbeck.txt:29` — "BGH-Rechtsprechung noch nicht ganz klar dazu (schauen: I ZR 197/22, I ZR 284/20)". Beide Aktenzeichen sind in dejure.org-Suche nicht direkt zu verifizieren. Der Notizencharakter ("schauen") legt allerdings nahe, dass die Mandantin/Anwaltsnotiz dies bereits als To-Do markiert — kein bewusst hallucinierter Beleg, sondern Rechercheauftrag. Vor Verwendung prüfen.

- `testakten/legistik-pflichtpostfach/eingang/begruendung-b.md:179` — "Bundesgerichtshofs (BGH XII ZB 233/22, 25.01.2023)" zur elektronischen Zustellung. dejure.org-Trefferliste für den 25.01.2023 enthält IV ZB 7/22 (technische Störungen ERV), aber nicht XII ZB 233/22. XII ZB 233/21 existiert (9.3.2022). Verdacht auf Aktenzeichen-Verwechslung oder Halluzination. Vor Verwendung prüfen.

- `testakten/energierecht-stadtwerke-quartier/06_transaktion/energie_dd_findings_roh.md:55` und `04_vertraege/mieterstromvertrag_muster.md:350` — "BGH VIII ZR 51/13", "BGH VIII ZR 225/14", "BGH VIII ZR 191/18" zu Preisanpassungsklauseln. Keiner dieser Verweise ist im freien Web sicher zuzuordnen; thematisch existieren z. B. VIII ZR 344/13 (25.06.2014) und VIII ZR 175/19 sowie VIII ZR 155/21. Vor Verwendung in DD-Memo verifizieren.

- `testakten/markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon/README.md:96,114,143,144,169,183` — "BGH-Beschluss I ZB 14/26 (28.04.2026)" zur Soundmarke. Datum liegt knapp einen Monat in der "Zukunft" gemessen am Aktenstand 30.05.2026; in einer anonymisierten Fall-Akte vertretbar, aber als spezifisch genanntes Aktenzeichen prüfbar zu kennzeichnen. Akte gibt sich selbst als anonymisiertes Beispiel zu erkennen — keine Änderung erforderlich, aber Hinweis im Skill-Begleittext sinnvoll.

- `testakten/weg-hausverwaltung-hohenzollernhof/12-anfechtungsrisiko-matrix.md:48` — "BGH V ZR 175/18 v. 18.12.2018 — verifizieren". Selbstmarkiert; nicht in dejure.org geprüfter Treffer für dieses Datum. Vor Mandantenversand verifizieren.

- `testakten/weg-hausverwaltung-hohenzollernhof/12-anfechtungsrisiko-matrix.md:50` und `10-beschlussvorlagen-eigentuemerversammlung.md:30` — "BGH V ZR 16/09 v. 21.11.2008" (Sonderumlage). Selbstmarkiert "Stand prüfen". Verifikation steht aus.

- `testakten/weg-hausverwaltung-hohenzollernhof/10-beschlussvorlagen-eigentuemerversammlung.md:55` — "BGH V ZR 11/19 v. 20.09.2019". Selbstmarkiert. Verifikation steht aus.

- `testakten/weg-hausverwaltung-hohenzollernhof/09-wirtschaftsplan-2026-entwurf.md:63` — "BGH (V ZR 28/99 vom 12.10.2000)" als Quelle der Empfehlung "1,0–1,5 % des Verkehrswerts". Empfehlungsinhalt ist branchenüblich, BGH-Beleg dafür eher unwahrscheinlich. Vor Verwendung prüfen.

### A.3 Bestätigt / kein Befund

Folgende konkret zitierte Entscheidungen wurden bei stichprobenartiger Webverifikation als korrekt bestätigt:

- BGH VIII ZR 159/23 vom 27.11.2024 — `schriftform-mietkuendigung-bielefeld-online-pferdedrescher/` (mehrere Stellen). Datum und Aktenzeichen stimmen.
- BGH V ZR 244/22 vom 09.02.2024 — `weg-hausverwaltung-hohenzollernhof/` (mehrere Stellen). Datum und Aktenzeichen stimmen.
- BGH V ZR 236/23 vom 14.02.2025 — `weg-hausverwaltung-hohenzollernhof/` (mehrere Stellen). Bestätigt.
- BGH V ZR 128/23 vom 14.02.2025 — `weg-hausverwaltung-hohenzollernhof/07-teilungserklaerung-auszug.md:76`. Bestätigt.
- BGH II ZR 174/80 vom 25.02.1982 (Holzmüller) — `gesellschaftsrecht-legal-english-frankfurt-startup/14-board-und-consent-matters-mapping-de-en.md:74`. Bestätigt.
- BGH II ZR 50/20 vom 25.01.2022 — `gesellschaftsgruender-streit-roeschen-tech/06_Anfechtungsklage_Christine.md:115`. Bestätigt.
- BGH II ZR 91/21 vom 08.11.2022 — selbe Datei. Bestätigt.
- BGH III ZR 179/20 / III ZR 192/20 vom 29.07.2021 — `dsa-dma-bayrische-baustube-meissner/08_eilantrag_lg_nuernberg_fuerth_entwurf.md:45`. Bestätigt.
- BVerfG 1 BvL 7/14 vom 06.06.2018 — `befristungskontrollklage-vogt-stadtwerke/` (mehrere Stellen). Bestätigt.
- BVerwG/BAG-Aktenzeichen in `kuendigungsschutzklage-weber-techlogix/` (BAG 18.03.2010 – 2 AZR 468/08; BAG 20.05.2008 – 9 AZR 382/07): nicht systematisch nachgeprueft, aber Format plausibel.

## B. Falsche oder zu spezifische BMF-Daten

- `testakten/grunderwerbsteuer-sharedeal-closing-waldkrone/12-bmf-anwendungserlass-bezug.md:9-14` — Die Akte verzichtet bewusst auf konkrete Datierung des "gleichlautenden Ländererlasses zu § 1 GrEStG" und vermerkt explizit: "Konkrete Daten und Aktenzeichen dieser Erlasse müssen vor Versand der Anhörungsantwort amtlich verifiziert werden". Sauber gehandhabt.

- `testakten/legistik-pflichtpostfach/eingang/gesetzestext.md:251` und `eingang/begruendung-b.md` — "BMF-Stellungnahme" und Mitwirkung BMF generisch erwähnt, keine konkreten Daten / Aktenzeichen. OK.

- `testakten/lobbyregister-dublin-bank-frankfurt-branch/19_meeting_notes_bmf_terminvorbereitung.md` und Folgedateien — BMF-Termin sind als Mandats-Akte interner Vermerk, keine BMF-Schreiben mit Datum zitiert.

- `testakten/lobbyregister-public-affairs-agentur-wasserstoff/` — BMF nur als Adressat von Stellungnahmen genannt, keine BMF-Schreiben mit Datum.

Befund: **keine konkreten falschen BMF-Schreiben-Daten** festgestellt. Die Akten halten sich an die Konvention "ohne konkrete Datierung, solange nicht verifiziert".

## C. Datums-Inkonsistenzen

Stichprobenartige Pruefung im Zwischenraum Bescheid/Widerspruch.

### C.1 Geprüft, plausibel

- `testakten/sozialrecht-rollstuhl-tannenberg/01-olaf-rollstuhl/Eilantrag_SG_Kiel_25-08-2026.md:55` — "Am 11.02.2026 wurde von der Antragsgegnerin der Antrag auf einen Aktivrollstuhl gestellt. Mit Bescheid vom 18.04.2026 wurde der Antrag abgelehnt". **Sprachlicher Fehler**: Antragsteller (nicht Antragsgegnerin) stellt den Antrag. Vermutlich Tippfehler "Antragsgegnerin" statt "Antragstellerseite/Mandant". Vor Einreichung korrigieren.

- `testakten/dsa-dma-bayrische-baustube-meissner/08_eilantrag_lg_nuernberg_fuerth_entwurf.md:29,45` — Stichtag "13.03.2026 23:59 UTC" und Sperre "14.03.2026" sind konsistent; UTC-Hinweis fachlich richtig.

- `testakten/meinungspruefer-grenzfaelle-alltag/12_zeitachse_aeusserungen.csv` (gerade ausgebaute Akte) — Datumsangaben stimmen mit den Einzeldateien überein.

### C.2 Auffällig / Prüfbedarf

- `testakten/sozialrecht-rollstuhl-tannenberg/01-olaf-rollstuhl/Notiz_Kanzlei_Erstgespraech.txt:10` — "Bescheid vom 18.04.2026 zugestellt laut Mandant am 21.04.2026". Plausibel.

- `testakten/befristungskontrollklage-vogt-stadtwerke/klageschrift_vogt_arbg_berlin.md:74` — Klagefrist Berechnung: Vertragsende 28.02.2026 → 3 Wochen-Frist (§ 17 S. 1 TzBfG) endet 21.03.2026 (nicht 20.03.2026 wie angegeben, weil Samstag/Sonntag-Verschiebung erst ab Wochenende eintritt). Prüfen: ist 21.03.2026 ein Samstag? Lt. Kalender 2026 ist 21.03.2026 ein Samstag, also Frist regulär 23.03.2026. Die Akte nennt 20.03.2026 — verfährt zu konservativ; in der Sache geht das nicht zu Ungunsten des Mandanten, sollte aber präzisiert werden. **Hinweis: Fristberechnung in der Klageschrift sicherheitshalber neu durchrechnen.**

- Keine vom Aufgabenbeispiel "Bescheid 14.03.2026 vs. 13.03.2026 im Einspruch" beschriebene Inkonsistenz gefunden. Die im DSA-Bayrische-Baustube-Fall genannten beiden Daten (13.03.2026 = Stichzeitpunkt vor Sperre, 14.03.2026 = Sperrdatum) sind durchgehend konsistent in mehreren Aktenstücken belegt.

## D. Plugin-Querverweise

### D.1 Verweis auf nicht (mehr) existierendes Plugin

- `testakten/README.md:69` und `testakten/sozialrecht-rollstuhl-tannenberg/README.md:109` verwiesen auf ein früheres eigenständiges Sozialrechts-Plugin. Dieses Plugin existiert nicht mehr als Top-Level-Plugin. Existierende Plugins: `fachanwalt-sozialrecht` (mit Skill `sozialrecht-fallaufnahme-routing`, der in der Testakte ebenfalls referenziert wird), und `selbstvertreter-sozialgericht`. Stand Nachlauf: in den Übersichten auf `fachanwalt-sozialrecht` korrigiert.

### D.2 Bestätigt vorhanden

Alle anderen in `testakten/` referenzierten Plugins existieren als Top-Level-Verzeichnis:

- `meinungspruefer`, `nachbarschaftsstreit-pruefer`, `selbstvertreter-amtsgericht`, `selbstvertreter-sozialgericht`, `weg-hausverwaltung`, `arbeitsrecht`, `betreuungsrecht`, `forderungsmanagement-klagewerkstatt`, `insolvenzforderungsanmeldungspruefung`, `insolvenzverwaltung`, `legistik-werkstatt`, `lobbyregister-bundestag`, `phishing-vorfall-pruefer`, `ki-richtlinie-kanzleien`, `vertragsrecht`, `jveg-kostenpruefer`, `grosskanzlei-corporate-ma`, `krisenfrueherkennung-starug`, `markenrecht-fashion-luxus`, `bav-strategie-konzern`, `fluggastrechte`, `schriftform-und-textform-bgb`.

- `kanzlei-allgemein` existiert (in der Sachverständigen-Akte als Plugin referenziert via Skill `umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten`); der Skill ist tatsächlich unter `kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten/SKILL.md` vorhanden.

## E. Umlauthygiene

Insgesamt **25 Markdown-Dateien** weisen gemischte Umlautbehandlung auf (ASCII-Ersatz "ä/ö/ü/ss" und gleichzeitig echte Umlaute "ä/ö/ü/ß").

### E.1 Akten mit konsequenter ASCII-Linie und sporadischen Umlaut-Einschüssen

- `testakten/lobbyregister-dublin-bank-frankfurt-branch/00_aktenuebersicht.md:6` — Akte sonst durchgehend ASCII; einmalige Stelle "unselbstständiger" (mit ß) verstoesst gegen die Linie. Vorschlag: "unselbstständiger".

- `testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/` (gerade ausgebaute Akte) — Bestandteile in ASCII, vereinzelt "Brüchen", "vollständig", "regulär" enthalten. Inkonsequenz zwischen Originaldateien (ASCII) und Booster-Dateien 14-18 (echte Umlaute). Vorschlag: vereinheitlichen oder als bewusste Akte mit gemischter Quelle akzeptieren (Originaldokumente unterscheiden sich oft im Schreibstil).

- `testakten/lobbyregister-buergerinitiative-waldmoor/00_aktenuebersicht.md` — überwiegend ASCII; vereinzelte Umlaute. Prüfen.

- `testakten/common-law-kompass-crossborder-contract/03_term_sheet_delaware_english_law.md` — Mischung englisch/deutsch; ASCII + Umlauten gemeinsam. Akzeptabel im internationalen Kontext.

### E.2 Akten mit konsequenter Umlaut-Linie und sporadischen ASCII-Inseln

- `testakten/sozialrecht-rollstuhl-tannenberg/04-bodo-em-rente/Widerspruchsentwurf_Bodo_EM-Rente.md` — Hauptsächlich Umlaut, einzelne ASCII-Ersatzformen. Prüfen.

- `testakten/gesellschaftsgruender-streit-roeschen-tech/06_Anfechtungsklage_Christine.md` — Mischung. Prüfen.

### E.3 Bewertung

Die Umlauthygiene-Inkonsistenz ist meist redaktioneller Natur und nicht juristisch relevant. Empfehlung: pro Akte eine Linie wählen und dann durchziehen. Akten mit Sachverstaendigengutachten / Verfahrensakte können plausibel zwischen Originaldokumenten (Umlaut) und Anwaltsschriftsätzen (Umlaut) und alten Vorlagen (ASCII) unterscheiden — solche Inkonsistenzen sind realitätsnah und nicht zwingend zu beheben.

Anzahl Dateien mit Mischfall: 25. Komplette Liste unter `find testakten -name "*.md" -exec ...` (siehe Bearbeitungsmethode oben).

## F. Sonstige Beobachtungen

1. **Eingebaute "Verifizieren-vor-Verwendung"-Marker.** Mehrere Akten (insbes. `weg-hausverwaltung-hohenzollernhof/`, `gesellschaftsrecht-legal-english-frankfurt-startup/`) markieren Aktenzeichen ausdrücklich als "verifizieren" oder "vor Verwendung prüfen". Das ist ein didaktisch wertvoller Stil und entspricht der CLAUDE.md-Vorgabe ("Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren … Bei Unsicherheit: kennzeichnen und Verifizierung in amtliche oder frei zugängliche Quellen"). Beibehalten.

2. **Streitwerthöhen in Meinungspruefer-Akte (gerade veredelt).** Die in `08_abmahnung_und_aufforderung.md` und `15_anwaltsmahnung_novawerk_rupprecht.md` jeweils auf einen Gegenstandswert von 25.000 EUR gesetzte 1,3-Geschäftsgebühr von 1.295,43 EUR brutto ist ein Standard-RVG-Wert (vor 19. Erhöhung) — für eine 2026er Akte ggf. mit 1.295,43 vs. aktuelle KostRAEG-Werte abgleichen. Keine zwingende Korrektur, aber im Skill `meinungspruefer/output-memo-pruefvermerk` als Beispiel prüfen.

3. **Sachverständigen-Akte: Strategieskizze in Befangenheitsantrag-Entwurf.** Der Befangenheitsantrag-Entwurf (`16_befangenheitsantrag_entwurf.md`) enthält im Prüfhinweis explizit den Hinweis "BGH VI ZB 51/16 verifizieren". Dies ist methodisch das Verhalten, das CLAUDE.md für das Plugin verlangt. Nicht entfernen.

4. **DSA-Bayrische-Baustube-Akte (`testakten/dsa-dma-bayrische-baustube-meissner/`).** Datums- und Aktenketten sind in sich konsistent. Lediglich der Eilantrag bezieht sich auf das US-Recht der Antragsgegnerin (Glitzerwald Inc., Delaware) und nutzt deutsche AGB-/DSA-Argumentation. Sauber.

5. **Vergleichsdatenbasis im Sachverständigen-JSON (gerade aktualisiert).** In `09_vergleich_andere_gutachten_pfaffenberger.json` sind die Aktenzeichen LG Passau 2 O 412/24, LG Landshut 5 O 88/23, AG Cham 5 C 217/22, LG Regensburg 4 O 1742/22 als nicht verifiziert gekennzeichnet. Die Datei selbst weist explizit darauf hin: "kollegial bestätigt durch RA Krall", "nur Vermerk eines Kollegen". Methodisch sauber.

6. **Beträge in den geboosteten Akten.** Frachtkostendifferenz HanseLicht (`07_belegmappe_tatsachenkern.md`): 226.900 - 184.200 = 42.700 EUR. Sammelposition zentral 42.100 EUR. Differenz 600 EUR ist nicht erklärt, aber als realistische "Buchungsungenauigkeit" akzeptabel und genau der Streitpunkt zwischen Mandantin und Kallweit. Nicht zu korrigieren.

7. **Whistleblower-Statement (gerade angelegte Datei 17_whistleblower_statement_okb_insider.md).** Verweis auf "HinSchG" und § 7 HinSchG: korrekt nach geltendem Hinweisgeberschutzgesetz von 2023. Skill-Hinweis: vor Versand prüfen, ob konkrete Meldestellen-Pflichten zu nennen sind.

8. **Mandantenmail Sieglinger (gerade angelegte Datei 18_mandanten_email_sieglinger_nach_anhoerung.md).** Verweis auf "RVG § 4a" (Erfolgshonorar) — Vorsicht: Erfolgshonorare sind nur unter sehr engen Voraussetzungen zulässig (wirtschaftlich notwendig). Im Skill-Kontext als "zu prüfen" zu markieren.

## G. Empfohlene Massnahmen (Priorisierung)

1. **Hoch:** Datumskorrektur BGH VIII ZR 263/22 (energierecht-Akte) auf 27.09.2023.
2. **Hoch:** Korrektur des früheren Sozialrechts-Plugin-Querverweises auf `fachanwalt-sozialrecht` an zwei Stellen.
3. **Mittel:** Sprachliche Korrektur "Antragsgegnerin" → "Antragsteller" in Eilantrag Sozialrecht.
4. **Mittel:** Sammelprüfung der mit "verifizieren" markierten BGH-Aktenzeichen in der WEG-Akte; sukzessives Auflösen.
5. **Niedrig:** Umlauthygiene auf Aktenebene vereinheitlichen (25 Mischdateien).
6. **Niedrig:** Klagefristberechnung in `befristungskontrollklage-vogt-stadtwerke/klageschrift_vogt_arbg_berlin.md` neu durchrechnen.

## Anhang — Datenbasis Audit

- Gesamte Pfade durchsucht: `testakten/**/*.{md,txt,eml,csv,json}`.
- Pruefdauer: ca. 35 Minuten manuelle Auswertung plus 5 Webrecherchen.
- Nicht erfasst: PDFs in `gesamt-pdf/`-Unterordnern (Inhalt nicht durchsucht; nur Pfade gepruelt).
- Webquellen: bundesgerichtshof.de, dejure.org, bundesverfassungsgericht.de, NWB Urteile, jeweils über Such-Snippets verifiziert.
