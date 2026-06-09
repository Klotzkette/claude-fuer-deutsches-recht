# v290.0.0 — Qualitätsoffensive: Fachkerne statt Boilerplate, Testakten-Veredelung

## Skills

- **roemisches-recht**: 223 Skills, die nur identisches Boilerplate trugen (Zwölftafel-Einheitsblock, generische "Sofortsortierung" mit Importeur/Exporteur-Rollenliste), durch themenspezifische romanistische Fachkerne ersetzt — je Skill: Quellenanker mit Digesten-/Gaius-Inskriptionen, Kernregeln, moderne BGB-Parallele, typische Fehler, romanistische Arbeitsweise. 30+ Themencluster (Status/personae, Besitz/Interdikte, Eigentum/usucapio, Kauf/Gefahrtragung, locatio conductio, Delikte/lex Aquilia, Kondiktionen, Erbrecht, Bürgschaft, Pauliana, Konkurs, Seehandel/lex Rhodia, Prozessepochen, Juristen, Kompilation, Rezeption u. a.).
- **Quellenkarten** (73) und **Fehlerkataloge** (53), die nur Slug-Listen bzw. Tautologien enthielten, mit plugin-spezifischer Substanz gefüllt: tragende Normen, zuständige Spruchkörper, amtliche Datenbanken (BFH/BAG/BSG/DPMA/BAFA je nach Gebiet), konkrete Fehler mit Symptom-Diagnose-Heilung.
- 549 Skills mit identischen Descriptions plugin-/schwerpunktspezifisch differenziert; keine Dup-Gruppen mehr.
- 6 verbliebene Fallback-rom-Skills (actio institoria/tributoria, res-Einteilungen, dominium duplex, griechische Terminologie) mit eigenen Fachkernen.

## Testakten

- **kirchenrecht-cic-sancta-caecilia**: 10 Aktenstücke von Stubs zu vollwertigen Dokumenten ausgebaut — Kirchenaustritt (DBK-Dekret 2012, cc. 96, 849, 11 CIC, Omnium in mentem), Mischehe samt Ligamen-Prüfspur (cc. 1085, 1124 f.), Kommunionzulassung (cc. 912, 915 f.), Orgelspende (cc. 1267, 1300, 1303 ff.), förmliches Ordinariatsschreiben sowie sechs vollwertige mehrsprachige Schreiben (EN/ES/IT/LA/AR/PT) im jeweils passenden Register.
- **kernfusion-transrapid-starnberger-see (Projekt Isarlicht)**: 5 Kernvermerke ausgebaut — Standort (BayLplG-ROV, § 35 BauGB, WHG, § 34/44 BNatSchG), Transrapid-Einordnung (AMbG-Planfeststellung vs. Werksbahn), Strahlenschutz (kein § 7 AtG, aber §§ 12 StrlSchG-Genehmigungen, Tritium, Aktivierung), Netz/Vermarktung (§ 17 EnWG, kein EEG-Vorrang, PPA, HkN-Lücke), Förderung/IP/Beihilfe (ArbnErfG, Dual-Use-VO, AGVO/FuEuI-Unionsrahmen, AWV-Investitionsprüfung).
- **private-equity-nachtfalter**: Management-Roll-over als vollwertiger Verhandlungsvermerk (Vendor-Loan-Wirkung auf die Equity-Bridge, Leaver-Tabelle mit Verhandlungsrahmen, § 21 UmwStG, Dry-Income/§ 19 EStG, Non-Compete-Grenzen).

## Sonstiges

- Validator grün; 212 Plugins, alle auf 290.0.0.

# v253.0.0 — Testakten-Sweep: reale Kanzleien und reale Adresse entfernt

## Schwerpunkt

In den Testakten wurden alle Verweise auf reale, namentlich identifizierbare Rechtsanwaltskanzleien entfernt und durch fiktive, deutlich erfundene Namen ersetzt. Konkret wurde dabei auch die in einer Filesharing-Abmahnung verwendete echte Münchner Adresse und Telefonnummer einer realen ehemaligen Kanzlei durch eine fiktive Neuruppin-Adresse ersetzt. Die Akte heißt jetzt nach der fiktiven Kanzlei „Quetschenpaua & Kollegen" in Neuruppin.

## Was ersetzt wurde

| Reale Nennung | Fiktiver Ersatz |
| --- | --- |
| Waldorf Frommer (Filesharing-Abmahner) | Quetschenpaua & Kollegen, Neuruppin |
| Hogan Lovells LLP | Brösel Holzapfel & Partner LLP |
| Hengeler Mueller | Wammeshübel Zwirnknäuel & Sozien |
| Freshfields Bruckhaus Deringer | Pottwitz Stinkmorchel & Eulenspiegel |
| Linklaters | Federfuchs Knöterich & Partner |

Auch die echte Münchner Anschrift (Beethovenstraße 11, 80336) und Telefonnummer (089 52 05 72-10/-30) der ehemaligen Filesharing-Kanzlei wurden in der Akte durch die fiktive Anschrift Karl-Marx-Straße 41, 16816 Neuruppin und Telefon 03391 47 02-0/-29 ersetzt. Der echte Mail-Account `kanzlei@waldorf-frommer.de` ist durch die fiktive Domain `kanzlei@quetschenpaua-kollegen.de` ersetzt; das Aktenzeichen-Präfix `WF-2026-...` durch `QK-2026-...`.

## Was umbenannt/neugerendert wurde

- `testakten/ki-training-tdm-fotografin-windgassen-hamburg/pdfs/waldorf_frommer_abmahnung_redacted.pdf` → `quetschenpaua_kollegen_abmahnung_redacted.pdf` — frisches Layout (zweiseitig, dezenter Header, Fußzeile mit fiktivem HRB Neuruppin)
- `eml/waldorf_frommer_abmahnung_eingang_2026-01-09.eml` → `eml/quetschenpaua_kollegen_abmahnung_eingang_2026-01-09.eml`
- `05_filesharing_abmahnung_waldorf_frommer.md` → `05_filesharing_abmahnung_quetschenpaua_kollegen.md`
- `17_ofac_response_hogan_lovells.md` (Werkmann-Akte) → `17_ofac_response_broesel_holzapfel.md`
- DOCX-Anlage `NFK_Filesharing_Windgassen_Entwurf.docx` neu gepackt, alle Großkanzlei- und Adressverweise ersetzt
- 203 Gesamt-PDFs der Testakten neu gerendert

## Zahlen

- 127 Textersetzungen in 49 Dateien (Round 1)
- 36 weitere Ersetzungen in 27 Dateien (Round 2 für Großschreibung, Domains, Aktenzeichen-Präfix)
- 4 Ersetzungen in 2 Dateien für die Münchner Adresse und Telefonnummer (Round 3)
- 1 DOCX-Anlage repacked
- 1 Skill (`fachanwalt-urheber-medienrecht/.../erstgespraech-mandatsannahme-fachanwalt/SKILL.md`) inhaltlich neutralisiert (konkrete reale Filesharing-Abmahn-Kanzleien aus der Beispielzeile entfernt)

## Validierung

- `validate-plugin-structure`: OK
- `validate-yaml-frontmatter`: 0 Fehler, 0 Warnungen
- `validate-testakten-gesamt-pdf`: OK (203 Testakten)
- Repo-Sweep nach den entfernten Kanzleien: 0 Treffer in `.md/.eml/.txt/.json`, 0 Treffer im PDF-Volltext der Akte

## Hinweise

Allgemein-übliche deutsche Familiennamen, die zufällig auch politisch oder medial prominent sind (z. B. Lauterbach, Scholz, Merkel, Lindner), wurden in den Akten belassen, da sie dort eindeutig fiktive Mandantinnen, Mandanten oder Beteiligte bezeichnen und ihre Vornamen, Berufe und Orte mit keiner real prominenten Person übereinstimmen.

---

# v252.0.0 — Skill-Kürzung ohne Wissensverlust und Sanity-Bump

## Schwerpunkt

Nach dem extern eingespielten v251-Stand wurden die Skills nochmals auf Qualität, Kürze und Lesbarkeit geprüft. Entfernt wurden vor allem generische Beschreibungsschwänze, alte Konsolidierungs-Übersichtstabellen und interne Referenz-/Routingreste, die für Nutzerinnen und Nutzer in Claude/Cowork keinen Mehrwert hatten. Fachliche Inhalte, Normanker, Rechtsprechungshinweise und Arbeitsprodukte bleiben erhalten.

## Änderungen

- Generische Description-Tails wie standardisierte Output-/Risikoampel-Sätze repo-weit gekürzt.
- Alte `Prüfungslinien`-Tabellen mit früheren Skill-Slugs entfernt, wenn sie nur Konsolidierungsgeschichte wiederholten.
- Detailabschnitte neutralisiert (`Fachliche Module` statt Entstehungsgeschichte).
- Testakten-Gesamt-PDFs, Plugin-Struktur, YAML-Frontmatter und Übersichten erneut validiert.
- Versionsstand in Plugin-Manifesten, Marketplace und zentralen Übersichten auf v252.0.0 gehoben.

## Sanity

- 212 Plugins / 18.551 Skills / 203 Testakten.
- Keine alten Bündel-/Sammelskill-Formeln mehr gefunden.
- Testakten-PDF-Erstseiten weiterhin ohne Demo-/README-/Download-Vorspann.

---

# v251.0.0 — Boilerplate-Sweep: identische Wiederholungs-Sections plugin-weit entfernt

## Schwerpunkt

Repo-weit wurden in 211 Plugins identische Wiederholungs-Sections aus den Skills entfernt, die in vielen Plugins dutzend- bis hundertfach gleichlautend gestanden hatten. Insgesamt 17.855 Skills wurden überarbeitet, 57.645 Boilerplate-Blöcke entfernt. Skill-spezifische Bodies, Norm-Pinpoints und Leitentscheidungen bleiben unangetastet — Sections mit drei oder mehr Norm-Pinpoints (`§`, `BVerfGE`, `BGH`, `EuGH`, `OLG`, `Art. N`) wurden grundsätzlich nicht angefasst.

## Was entfernt wurde

Header-basierte Blacklist auf folgenden Wiederholungs-Sections:

- Arbeitsbereich, Arbeitsweise, Arbeitsauftrag, Arbeitsfragen, Aufgabe
- Output, Output-Standard, Ausgabeformat, Ergebnisformate
- Quellenregel, Quellenhygiene
- Qualitätsregel, Qualitätsregeln, Qualitäts-Hardening
- Red-Team-Fragen
- Einstieg ohne Leerlauf, Einsatz
- Minimal-Intake
- Typische Artefakte, Querverweise
- Zweck, Anwendungsbereich, Vorgehen
- Konversationsstil
- V61 Deal-OS Boost, Agentischer Arbeitsmodus
- Anfänger- und First-Year-Modus, Jurisdiktionsweichen in fünf Schritten
- Spezielle Leitplanken

## Was bewahrt wurde

- Fachkern, Prüfpfad, Normen-Bibliothek, Leitentscheidungen, Quellenanker
- Skill-spezifische BGH-Linien und OLG-Rechtsprechungs-Blöcke
- Akten- und beispielnahe Bodies aus den v243-Kaltstarts
- Alle Norm-Pinpoint-haltigen Substanz-Sections (Schutzschwelle: ≥3 Pinpoints)

## Methodik

Sweep-Skript mit Header-Blacklist + Norm-Pinpoint-Substanzschutz und Sicherheits-Fallback (letzte Section eines Skills wird nie entfernt). Header-Base-Erkennung über `re.split('[:—]|\\s–\\s')`, damit Varianten wie "Fachkern: Abtretung" sauber von "Fachkern" als Boilerplate unterschieden werden.

## Folge-Arbeiten

Mehrere Sammelskills (z. B. `verbraucherinsolvenz-schuldenbereinigung/skills/privatdarlehen-familie`) tragen weiterhin mehrere Sub-Themen in einer SKILL.md. Diese werden in einer Folge-Version in eigenständige Skills aufgespalten.

---

# v250.0.0 — Testakten als echte Akten-Dumps und Release-ZIPs ohne Meta-Vorspann

## Schwerpunkt

Die Testakten-Gesamt-PDFs beginnen jetzt direkt mit dem ersten exportierten Aktenstück. Deckblatt, README-Zusammenfassung und Inhaltsverzeichnis wurden aus dem Gesamt-PDF-Generator entfernt, damit die Akten wie echte Dokumentenstapel funktionieren und nicht bereits am Anfang den Fall erklären.

## Änderungen

- `scripts/build-testakte-gesamt-pdf.py` rendert Gesamt-PDFs ohne Cover und Inhaltsverzeichnis; Dateigrenzen bleiben erhalten.
- Neuer gemeinsamer Testakten-Filter `scripts/testakte_file_filter.py`: README-, Download-, Vorführ- und initiale Meta-Übersichtsdateien werden aus Arbeitsmaterial-Exports herausgehalten.
- Neuer Release-ZIP-Builder `scripts/build-testakten-release-zips.py`: Einzel-Testakten-ZIPs und `alle-testakten.zip` enthalten Aktenmaterial plus Gesamt-PDF, aber keine Repo-README- oder Demo-Hinweise.
- Der GitHub-Release-Workflow nutzt den neuen Testakten-ZIP-Builder.
- Alle 203 Gesamt-PDFs wurden mit der neuen Akten-Dump-Logik neu erzeugt.
- Versionsstand in Plugin-Manifesten, Marketplace und zentralen Übersichten auf v250.0.0 gehoben.

## Sanity

- 203 Gesamt-PDFs erfolgreich neu gebaut.
- Testakten-ZIP-Probelauf: 203 Einzel-ZIPs, keine README- oder `00_aktenuebersicht`-Einträge.
- Skill-Boilerplate-Suche nach alten Bündel-/Sammelskill-Formeln ohne Treffer.

---

# v240.0.0 — Audit-Befunde aus 15-Bug-Sweep umgesetzt

## Schwerpunkt

Reine Pflege- und Konsistenzversion nach dem v239-Release. Alle 15 Befunde aus dem internen Audit wurden abgearbeitet, ohne dass sich Skill-Inhalte oder Plugin-Strukturen aendern. Counts und Stand-Angaben sind durchgaengig auf 212 Plugins / 18.549 Skills / 203 Testakten konsolidiert.

## Aenderungen im Einzelnen

- **YAML-Description-Cleanup** in 14 Verhaeltnismaessigkeitspruefer-Skills: Doppel-Bandzahl entfernt (`BVerfGE 7 Band 7 Seite 198` -> `BVerfGE Band 7 Seite 198`), Umlaute/ss in YAML-descriptions vereinheitlicht zu ASCII (ae/oe/ue/ss). Body-Texte unveraendert.
- **Plugin-README** `verhaeltnismaessigkeitspruefer/README.md` auf alle 44 Skills mit sieben Gruppen ausgebaut (Methodik 8, Vor-Trias plus Schranken 4, absolute Grenzen 3, Kontrolldichte 5, BVerfG-Leitentscheidungen 10, Rechtsvergleich 3, Dogmatiklinien 4, Praxis 7) und Plugin-Titel mit ss-Schreibung auf ss-Schreibung umgestellt.
- **marketplace.json** description fuer `verhaeltnismaessigkeitspruefer` mit der plugin.json-Description synchronisiert (jetzt 44 Skills statt vorher noch 31). plugin.json fuer `status-navigator-step-plan` um "mit 35 Skills" ergaenzt, damit marketplace und plugin uebereinstimmen.
- **TESTBERICHT.md** Arbeitsstand-Beschreibung auf v239 aktualisiert (alter LausitzStorage-Text raus), Skill-Count von 18.536 auf 18.549 korrigiert.
- **README.md** Skill-Count auf 18.549, Plugin-Tabellen-Description fuer `verhaeltnismaessigkeitspruefer` um v239-Themen erweitert.
- **Padlet-Skill** `padlet-vier-stufen-tafel/SKILL.md` description-Style an die uebrigen 43 Skills im Plugin angeglichen (keine Quotes mehr, Doppelpunkt vor Beispielen vermieden, damit YAML-Plain-Scalar-Regel eingehalten wird).
- **BVerfG-Schlagwort-Feintuning** in drei Body-Stellen ohne Klammer-Schlagwort: `untermassverbot-schutzpflicht-dimension` (Lueth-Urteil), `vorpruefung-schranke-finden` (G10-Gesetz), `absolute-grenze-menschenwuerde-art-1-i-gg` (Schubhaft).
- **audiovisuelle-leitentscheidungen-sammlung** mit Permalink-Disziplin: Permalinks zu BVerfG-Pressemitteilungen fuer Klimaschutz-Beschluss und Bundesnotbremse-Beschluss eingefuegt, aeltere Leitentscheidungen ohne audiovisuelles Material explizit als ohne Mediathek-Permalink gekennzeichnet.
- **schutzbereich-eingriff-rechtfertigung/SKILL.md** mit Cross-Reference auf die drei Vor-Trias-Skills (`vorpruefung-schutzbereich-eroeffnet`, `vorpruefung-eingriff-klassisch-modern`, `vorpruefung-schranke-finden`) versehen, damit Detailtiefe und Gesamtschau klar zugeordnet sind.
- **Versions-Bump** 239 -> 240 in 212 plugin.json + marketplace.json + 5 Top-Dokumenten (README, TESTBERICHT, ASSET_INDEX, SKILLS, CHANGELOG) und 212 skills-index-Detailseiten.

## Validatoren

- `validate-yaml-frontmatter`: 0 Fehler, 0 Warnungen
- `validate-plugin-structure`: OK
- `validate-testakten-gesamt-pdf`: OK (203 Testakten)

# v239.0.0 — Verhaeltnismaessigkeitspruefer-Politur: 14 neue Stufen- und Schranken-Skills, Padlet-Skill arbeitet wieder, Clip-Club ersetzt

## Schwerpunkt

Das Plugin `verhaeltnismaessigkeitspruefer` ist von 30 auf **44 Skills** angewachsen. Die vierstufige Schranken-Schranke ist jetzt durchgehend mit Vor-Trias (Schutzbereich, Eingriff, Schranke), absoluten Grenzen (Menschenwuerde, Wesensgehalt, Existenzminimum), Bestimmtheit, Wesentlichkeitstheorie, Untermassverbot, Einschaetzungspraerogative und Zitiergebot abgedeckt. Der Padlet-Skill funktioniert wieder, der unjuristische Arbeitstitel "Clip-Club" ist durch eine kuratierte audiovisuelle Leitentscheidungs-Sammlung ersetzt.

### Neue Stufen- und Schranken-Skills (14)

- `vorpruefung-schutzbereich-eroeffnet`
- `vorpruefung-eingriff-klassisch-modern`
- `vorpruefung-schranke-finden`
- `schranke-vorbehaltlos-verfassungsimmanent`
- `absolute-grenze-menschenwuerde-art-1-i-gg`
- `absolute-grenze-wesensgehalt-art-19-ii-gg`
- `absolute-grenze-existenzminimum`
- `untermassverbot-schutzpflicht-dimension`
- `einschaetzungspraerogative-kontrolldichte`
- `bestimmtheit-normklarheit-eingriffsgesetze`
- `wesentlichkeitstheorie-parlamentsvorbehalt`
- `zitiergebot-art-19-i-2-gg`
- `stufenbaum-ascii-art`
- `audiovisuelle-leitentscheidungen-sammlung` (ersetzt `clip-club-leitentscheidungen`)

### Padlet-Skill arbeitet wieder

`padlet-vier-stufen-tafel` legt jetzt **echte** Padlet-Tafeln an. Drei Pfade:

1. **API**: Padlet Public API v1 mit `api_credentials=["custom-cred:padlet.com"]` (User braucht bezahltes Abo + API-Key aus Padlet-Settings → Developer).
2. **Browser**: `browser_task` mit `use_local_browser.local=true` auf https://padlet.com via Tom's MacBook Air M4.
3. **Manuell**: Karten-Markdown fertig zum Einkopieren. Skill gibt nie selbst-gerendertes Shelf-Board als Padlet-Ersatz aus.

Spaltenstruktur mit Ampelfarben gruen/gelb/rot, ASCII-Vorschau als Begleitung.

### Clip-Club geht in Pension

Der Arbeitstitel "Clip-Club" war eine unjuristische Anlehnung an Klipp-Klapp. Der Skill heisst jetzt `audiovisuelle-leitentscheidungen-sammlung` und arbeitet als kuratiertes Lehrmaterial-Verzeichnis mit Aktenzeichen, BVerfGE-Fundstelle inkl. Schlagwort, Datum, Medium, Quelle/Permalink, Zeitstempel, Stufenverortung und Folgewirkung. Quellen ausschliesslich BVerfG-Mediathek, ARD/ZDF/Phoenix und Open-Access-Hochschulvorlesungen. Urheberrechts-Hinweise zu § 51 UrhG.

### BVerfG-Schlagwort-Konvention

Im Skill-Body steht hinter jeder Leitentscheidung jetzt ein Schlagwort in Klammern, z.B. `BVerfGE 7, 198 (Lueth-Urteil)`, `BVerfGE 65, 1 (Volkszaehlung)`, `BVerfGE 115, 118 (Luftsicherheitsgesetz)`. YAML-descriptions nutzen weiter den Workaround "Band X Seite Y" (Komma-Regel).

## Cross-References aktualisiert

- `verhaeltnismaessigkeit-einstieg/SKILL.md`: neue Visualisierungs-Verweise auf `audiovisuelle-leitentscheidungen-sammlung` und `stufenbaum-ascii-art`.
- `verhaeltnismaessigkeitspruefer/README.md`: Praxis-und-Workflow-Block und Skill-Tabelle aktualisiert.
- `verhaeltnismaessigkeitspruefer/.claude-plugin/plugin.json`: description, keywords (`clip-club` → `audiovisuelle-leitentscheidungen`, plus `wesensgehalt`, `menschenwuerde`, `bestimmtheit`, `wesentlichkeitstheorie`).

## Counts (v239)

212 Plugins, 18.549 Skills, 203 Testakten.

---

# v238.0.0 — LausitzStorage-Testakte um zehn Finanzierungs- und Gesellschafterstreit-Originale erweitert

## Schwerpunkt

Die Testakte `status-navigator-batteriespeicher-jaenschwalde-peitz` ist um zehn weitere Originaldokumente von 33 auf **43 Aktenstuecke** angewachsen. Schwerpunkt: vollstaendige Finanzierungs- und Sicherheitenarchitektur (NordCap 96 Mio Senior + 18 Mio Wandel, ILB Avalrahmen 10 Mio, Linklaters als Security Agent) und ein realer Gesellschafterstreit auf Basis der bereits angelegten Drawstop-Krise.

### Finanzierungs- und Sicherheitendokumente

- `34_sicherheitenpoolvertrag_nordcap_ilb.md` — Pool-Vertrag NordCap ∕ ILB ∕ LausitzStorage mit Linklaters LLP als Security Agent, sechs Sicherheitsarten, Rangfolge der Befriedigung, Pari-passu-Klausel.
- `35_kontoverpfaendungsvertrag_commerzbank.md` — Kontoverpfaendung der drei Commerzbank-Konten (Betriebs-, Projekt-, Liquiditaetsreserve), Anzeige nach § 1280 BGB an Commerzbank am 09.09.2025 nachweisbar zugegangen, Verfuegungsfreiheit bis Sicherungsfall.
- `36_globalzession_pachtforderungen_leag.md` — Stiller Globalzessionsvertrag aller LEAG-Pachtforderungen, Bestimmtheitsgrundsatz § 398 BGB, Anzeige nach § 407 BGB bewusst unterlassen.
- `37_anteilsverpfaendungsurkunde_ur_388_2025.md` — Notarielle Anteilsverpfaendung aller 100 % der Gesellschaftsanteile (Bauernfeind 51, Lindenthal 9, NordCap 30, Stadtwerke 10), Form § 15 Abs. 3 GmbHG, Stimmrechte beim Verpfaender bis Sicherungsfall, Gesellschafterliste § 40 GmbHG am 16.09.2025 beim HR Cottbus eingereicht.

### Gesellschafterstreit (drei Aktenstuecke)

- `38_gesellschafterstreit_antrag_nordcap_abberufung_bauernfeind.md` — Einberufungsverlangen NordCap nach § 50 Abs. 1 GmbHG mit Abberufungsantrag gegen Geschaeftsfuehrer Bauernfeind aus wichtigem Grund (§ 38 Abs. 2 GmbHG); fuenf Vorwuerfe (Documentation Gap, Cap-Table-V2, Verschleppung Wandeldarlehens-Reparatur, Genehmigungsregime-Konflikt LEAG, Berichtspflichten LEAG); Stimmverbot § 47 Abs. 4 Satz 2 GmbHG.
- `39_anwaltsschreiben_lindenthal_notarprotest_cap_table.md` — RAin Schweikart-Boeßer namens Mitgesellschafterin Lindenthal protestiert formell gegen Cap Table V2, fordert Klarstellung bis 20.06.2026, kuendigt Enthaltung beim Abberufungsantrag und Sonderpruefungs-Antrag nach § 46 Nr. 6 GmbHG an.
- `40_einberufung_und_stellungnahme_bauernfeind.md` — Einberufung außerordentliche Versammlung 24.06.2026 (Notarbuero Albers Berlin, UR 423/2026); Gegen-Stellungnahme Bauernfeind zu allen NordCap-Vorwuerfen; eigener CRO-Vorschlag Dr. Schoeneberger als Vergleichsweg.

### Operative Originale

- `41_epc_anzahlungsrechnung_sungrow.md` — EPC-Anzahlungsrechnung Sungrow Deutschland 18 Mio EUR aus Tranche 2 (Bezugsrechnung SDE-2025-09-LSS200-A1) mit Advance Payment Bond Bank of China BOC-FRA-2025-09-187.
- `42_zugangsbestaetigung_anlage_4_stadtwerke_cottbus.md` — Stadtwerke Cottbus uebergeben die fehlende Anlage 4 zum Konsortialvertrag (24-seitiger Investorenrechte-Katalog) mit Haftungsfreistellung 25.000 EUR fuer die Fehlheftung; Drawstop-Punkt (iii) damit geheilt.
- `43_forensik_protokoll_cap_table_v2.md` — IT-Forensik Inkubator-IT Cottbus belegt, dass Cap-Table V2 in 18.247 Mailpostfacher- und 8.412 Dateianhangs-Pruefungen niemals in der Außenkommunikation verwendet wurde — Entlastung Bauernfeind fuer die Abberufungs-Versammlung.

## Inhaltliche Verzahnung

Alle zehn neuen Aktenstuecke sind durch durchgaengige Aktenzeichen, Notar-UR-Nummern (387/2025, 388/2025, 423/2026), Einschreiben-Belegnummern (RM 4274 8842 1 DE, RM 5117 9026 4 DE, RM 4517 8829 3 DE) und Posteingangsdaten mit der bestehenden Akte verzahnt. Die Drawstop-Krise NordCap vom 22.05.2026 wird durch die neue Welle vollstaendig: Drawstop-Punkt (iii) ist mit Akte 42 geheilt, Punkt (ii) durch die Reparaturvereinbarung (Akte 22), Punkte (iv) und (v) sind im Step-Plan (Akte 33) gelb.

## Gesamt-PDF

- LausitzStorage Gesamt-PDF: **188 KB / 43 Quelldateien** (vorher 121 KB / 33).

## Counts (unveraendert ggue. v237)

- **212 Plugins**, **18.549 Skills**, **203 Testakten**. Nur eine Testakte gewachsen (33 → 43 Aktenstuecke).

## Validation

- `node scripts/validate-plugin-structure.mjs`: gruen.
- `python3 scripts/validate-yaml-frontmatter.py`: 0 Fehler, 0 Warnungen.
- `python3 scripts/validate-testakten-gesamt-pdf.py`: gruen (203 Testakten).

---

# v237.0.0 — Testakten LausitzStorage und Polizeiverfuegung-Forst erweitert, Repo-Sweep clean

## Schwerpunkt

- **Testakte `status-navigator-batteriespeicher-jaenschwalde-peitz` erweitert** von 27 auf **33 Aktenstuecke**. Sechs zusaetzliche Anwaltsdokumente aus dem Mandatsverlauf:
  - `27_handelsregisterauszug_lausitzstorage_und_leag_immobilien.md` — HRB 11842 Cottbus (LEAG Immobilien GmbH) und HRB 12217 Cottbus (LausitzStorage GmbH) mit § 177 BGB-Belegen zur schwebenden Unwirksamkeit der Reparaturvereinbarung NordCap-Niederee.
  - `28_mandatsvollmacht_lausitzstorage_pohlmann.md` — Vollmacht der LausitzStorage GmbH auf RAin Dr. Friederike Hesselmann-Sauerbruch, Sozietaet Pohlmann und Pohlmann.
  - `29_aktennotiz_telefonat_nordcap_reparaturverhandlung.md` — Aktennotiz Verhandlung mit NordCap-Geschaeftsfuehrer Niederee zur Reparaturkostenuebernahme der Pufferspeicher-Steuerung.
  - `30_zugangsbeweis_einschreiben_drawstop_post.md` — Einwurf-Einschreiben RM 4118 7325 8 DE als Zugangsnachweis gemaess § 130 BGB.
  - `31_rvg_zwischenrechnung_pohlmann.md` — RVG-Zwischenrechnung bei Streitwert 11,9 Mio EUR, 1,3-Gebuehr plus Auslagen plus USt, Endbetrag 41.488,28 EUR.
  - `32_klarstellungsschreiben_leag_pacht_genehmigungsregime.md` — Klarstellung gegenueber LEAG zum Pacht-Genehmigungsregime mit Frist 23.06.2026.
  - `33_step_plan_v2_aenderungslog_und_ampelfortschritt.md` — Step-Plan v2 Aenderungslog mit rot 10 auf 3 reduziert.
- **Testakte `polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz` erweitert** von 20 auf **26 Aktenstuecke**. Sechs zusaetzliche Verfahrensdokumente nach Eilbeschluss-Stattgabe:
  - `21_anwaltsvollmacht_initiative_pohlmann.md` — Vollmacht Initiative Lausitzer Lebensraum e.V. an die Sozietaet.
  - `22_widerspruch_polizeipraesidium_cottbus.md` — Widerspruch nach § 68 VwGO gegen die sechs verbliebenen Auflagen 1/2/4/5/6/8.
  - `23_kostenfestsetzungsantrag_vg_cottbus.md` — Kostenfestsetzungsantrag mit Quote 5/6 zugunsten des Antragstellers, 3.687,12 EUR.
  - `24_fortsetzungsfeststellungsklage_vorbereitung.md` — Vorbereitung der Fortsetzungsfeststellungsklage nach § 113 Abs. 1 Satz 4 VwGO (Wiederholungsgefahr und Rehabilitation).
  - `25_pressespiegel_lausitzer_rundschau.md` — Pressespiegel Lausitzer Rundschau, MAZ, Tagesspiegel, RBB.
  - `26_verhaeltnismaessigkeitspruefung_klausurspur.md` — Klausurspur der Verhaeltnismaessigkeitspruefung pro Auflage entlang BVerfGE 69, 315 Brokdorf.
- **Gesamt-PDFs neu gebaut**: LausitzStorage 121 KB / 33 Quelldateien; Polizei 106 KB / 26 Quelldateien.
- **READMEs der beiden Testakten** um die Punkte 27-33 bzw. 21-26 erweitert, KB-Werte in den Header-Sektionen synchronisiert.

## Repo-Sweep clean

- Skill-Slugs in beiden neuen Plugins (`status-navigator-step-plan`, `verhaeltnismaessigkeitspruefer`) durchgesehen — alle sprechend, normbezogen, keine generischen Kurzformen.
- Boilerplate-Scan repo-weit: "robuste" 191x, "nahtlos" 32x, "klar und verstaendlich" 12x — alle in juristischem Fachkontext (§ 307 BGB, Nahtlosigkeit GKV/RV, etc.), keine generischen KI-Tells.
- Keine leeren SKILL.md, kein TODO/FIXME ausserhalb legitimer Mustertexte (XXX = ISBN-Platzhalter, Az.-Format-Beispiel, TODO-Workflow-Marker).
- description-Laengen aller 18.549 Skills compliant (<= 1024 Zeichen).

## Counts (unveraendert ggue. v236)

- **212 Plugins**, **18.549 Skills**, **203 Testakten**. Nur Inhalt der zwei erweiterten Testakten gewachsen (27 -> 33 und 20 -> 26 Aktenstuecke).

## Validation

- `node scripts/validate-plugin-structure.mjs`: gruen.
- `python3 scripts/validate-yaml-frontmatter.py`: 0 Fehler, 0 Warnungen.
- `python3 scripts/validate-testakten-gesamt-pdf.py`: gruen (203 Testakten).

---

# v236.0.0 — Uebersichten, Asset-Index und Downloadpakete synchronisiert

## Schwerpunkt

- **Root-README alphabetisch nachgezogen:** `status-navigator-step-plan` und `verhaeltnismaessigkeitspruefer` stehen wieder in der zentralen Plugin-Tabelle; die thematischen Cluster nennen beide ebenfalls.
- **PROMPTLISTE aktualisiert:** 208 kuratierte Praxis-Plugins von 212; die vier bewusst ausgenommenen historischen/exotischen Spezialplugins bleiben nicht in der kuratierten Praxisliste.
- **ASSET_INDEX neu aufgebaut:** 212 Plugin-Assets, 203 Testakten-Assets und alle vier Sammel-Assets (`marketplace.json`, `alle-plugins-megazip.zip`, `alle-testakten.zip`, `alles-komplettpaket.zip`) mit den tatsächlich vom Release-Workflow erzeugten Download-URLs.
- **Sofort-Download-Sektionen nachgezogen:** Die beiden neuen Plugins haben nun eigene Direkt-Download-Blöcke mit zugeordneter Demonstrationsakte; bestehende Plugin- und Testakten-README-Blöcke wurden idempotent geprüft.

## Validation

- `node scripts/validate-plugin-structure.mjs`: grün.
- `python3 scripts/validate-testakten-gesamt-pdf.py`: grün.
- `python3 scripts/validate-yaml-frontmatter.py`: grün.
- Lokale Release-ZIP-Simulation: alle 212 Plugin-ZIPs, alle 203 Testakten, `alle-plugins-megazip.zip`, `alle-testakten.zip` und `alles-komplettpaket.zip` vollständig.

---

# v235.0.0 — Status-Navigator, Verhaeltnismaessigkeitspruefer, Fachanwalt-Norm-Skills, Polizeirechtliche Testakte, Veredelungs-Runde 3

## Schwerpunkt

- **Zwei neue Plugins** mit zusammen 66 Skills:
  - `status-navigator-step-plan` (35 Skills): Status-Navigator und Step-Plan-Macher als reine Dokumentenverarbeitung. Strukturiert disparate Dokumentenlagen in eine mehrseitige Excel-Arbeitsmappe und optional ein Padlet-Shelf mit Reitern Ueberblick, Vorhanden, Fehlend und Workflow. Keine rechtliche Bewertung, keine Normenanker.
  - `verhaeltnismaessigkeitspruefer` (31 Skills): Vierstufige Schranken-Schranke (legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit) mit BVerfG-Leitentscheidungen, PrOVG-Kreuzberg-Linie, rechtsvergleichenden Skills zu Suedafrika Section 36 und Workflow-Werkzeugen Clip-Club/Padlet.
- **230 neue Norm-Skills in 23 Fachanwalt-Plugins** (je 10 Skills mit sprechenden Slugs): zitiert konkret aus dem jeweiligen Plugin-Bestand und loest jeweils ein konkretes Problem. Plugins: agrarrecht, arbeitsrecht, bank-kapitalmarktrecht, bau-architektenrecht, erbrecht, familienrecht, gewerblicher-rechtsschutz, handels-gesellschaftsrecht, insolvenz-sanierungsrecht, internationales-wirtschaftsrecht, it-recht, medizinrecht, miet-wohnungseigentumsrecht, migrationsrecht, sozialrecht, sportrecht, strafrecht, transport-speditionsrecht, urheber-medienrecht, vergaberecht, verkehrsrecht, versicherungsrecht, verwaltungsrecht (steuerrecht ausgenommen wegen Redirect).
- **Neue Testakte**: `polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz` (20 Aktenstuecke) — Initiative Lausitzer Lebensraum e.V. (1. Vorsitzender Dr. Werner-Karl Pohlmann-Brandenburg) gegen Polizeiverfuegung wegen Anti-Kohle-Versammlung mit Performance-Erdaushebung "Vier Stufen der Trauer um den Lausitzer Wald". Eilantrag § 80 Abs. 5 VwGO an VG Cottbus 3 L 188/26, Vors. RiVG Dr. Susanne Marquardt-Heuser. Beschluss-Stattgabe wegen Versammlungsfreiheit Art. 8 GG. Bearbeitung durch RAin Dr. Friederike Hesselmann-Sauerbruch, Pohlmann und Pohlmann, AZ PoPo-2026-VR-0617.
- **Veredelungs-Runde 3**: 1.124 Skills in 197 Plugins mit kuratierten Normen-und-Rechtsprechung-Sektionen versehen. Plugin-Top-30 mit handkuratierten Norm-Bibliotheken (8-15 Normen + 3-6 Leitentscheidungen), uebrige Plugins mit aus den Plugin-Skills extrahierten Top-Normen.

## Counts

- 210 Plugins -> **212 Plugins** (+2: status-navigator-step-plan, verhaeltnismaessigkeitspruefer).
- 18.240 Skills -> **18.549 Skills** (+296 netto: +35 Status-Navigator + 31 Verhaeltnismaessigkeit + 230 Fachanwalt-Norm-Skills, zuzueglich Politur/Korrekturzaehler aus der Zwischenpflege).
- 201 Testakten -> **203 Testakten** (+2: status-navigator-batteriespeicher-jaenschwalde-peitz aus v230-Vorbereitung + neue Polizei-Akte).

## Validation

- `node scripts/validate-plugin-structure.mjs`: gruen.
- `python3 scripts/validate-yaml-frontmatter.py`: gruen.


# v230.0.0 — Bug-Hunt, Praefix-Sweep, Skill-Veredelung, Grammatik-Fix

## Schwerpunkt

- **Grammatik-Fix nach Codex-Polish v216:** 13.346 SKILL.md-Dateien mit grammatischen Folgefehlern der `Prueffeld -> Pruefungslinie`-Substitution korrigiert. Insgesamt rund 13.300 Sprachstellen geheilt: `dieses Pruefungslinie -> diese Pruefungslinie` (~12.993), `Dieser Pruefungslinie -> Diese Pruefungslinie`, `beim sachtragenden -> bei der sachtragenden`, `konkret Pruefungslinie -> konkrete Pruefungslinie`, `in das tragende -> in die tragende`, `zum richtigen -> zur richtigen`, `Passenden -> Passende`.
- **Truncation-Fix V4:** 80 Skill-Slugs mit abgeschnittenen Endungen rekonstruiert.
  - `-un` (Tail-Drop nach `-und`) entfernt fuer 30+ Skills.
  - `-red` -> `-red-team-korrektur` fuer 14 Skills.
  - `-sta` -> `-staatsanwaeltinnen` (StA-Plugin) bzw. `-staatshaftung` (Weltraumrecht).
  - `-fak` -> `-faktenmatrix`, `-ve` -> `-verhaeltnismaessigkeit`.
  - Hardcoded Fixes fuer Spezialfaelle (gesellschafterstreit, rechnungskorrektur etc.).
- **Aspekt-Suffix-Sweep:** 7 Skills mit doppeldeutigen Aspekt-Suffixen `-re/-or/-ka/-2/-3/-4` auf sprechende Vollform gebracht (z. B. `-rechtsprechungscheck`, `-organisationspflicht`, `-kaltstart`, `-kammerantwort`). Slug-Laengen-Limit 64 Zeichen beachtet, wo noetig Kurzform (z. B. `-orgapflicht`, `-rspr-check`).
- **marktmac/energie-Renames:** 5 Slugs aus bundesnetzagentur-verfahren rekonstruiert (`-marktmacht-...`, `-unbundling-...`, `-messstellenbetrieb-...`).
- **Doppel-Skill-Renames:** `interessenkollision-ehegatten-gesellschafter-*` und `honorarabhaengigkeit-non-audit-services-*` auf sprechende Suffixe gebracht.

## Skill-Veredelung mit konkreten Norm-Zitaten

- **535 Skills** in drei Plugins mit dedizierter `## Normen & Rechtsprechung`-Sektion versehen, die konkrete §§, Verordnungs-Artikel und Leitentscheidungen enthaelt.
  - `staatsanwaltschaft-praxis-einstieg` (142 Skills): StPO/StGB/GVG/RiStBV/JGG/BtMG/KCanG mit BVerfG- und BGH-Leitentscheidungen.
  - `berufsrecht-anwaelte` (197 Skills): BRAO/BORA/RVG/GwG mit § 160a StPO und BVerfGE 113, 29.
  - `berufsrecht-notare` (196 Skills): BNotO/BeurkG/GNotKG/DONot mit DNotZ-Rechtsprechung.

## Bug-Hunt-Ergebnisse

- Slug-Laengen alle <=64 Zeichen (Validator-Regel).
- Keine ungueltigen Zeichen in Slugs (nur `[a-z0-9-]`).
- Frontmatter `name` = Verzeichnis-Slug fuer alle 18240 Skills.
- Keine Stub-Skills mehr (Min ~1300 Bytes).

## Konsistenz

- README.md, TESTBERICHT.md, testakten/README.md auf `v230.0.0` gebumpt.
- PROMPTLISTE.md ergaenzt: `fahrgastrechte` in Transport-/Speditionsrecht (5 statt 4 Plugins) nachgetragen.
- SKILLS.md und alle 210 skills-index-Detailseiten regeneriert.
- ASSET_INDEX.md auf 210 Plugins / 201 Testakten / `v230.0.0` regeneriert.
- Plugin-Versionen aller 210 plugin.json und marketplace.json auf `230.0.0`.

## Validator

- `node scripts/validate-plugin-structure.mjs` -> `validate-plugin-structure OK`.

---

# v220.0.0 — Repo-weiter Qualitaets-Sweep: Praefix-Cleanup, Wortsalat-Slugs entwortsalatet, Truncations gefixt, Codex-Polish uebernommen

## Schwerpunkt

- Repo-weiter Qualitaets-Sweep ueber alle 210 Plugins in zwei Phasen.
  - Phase 1: ~1100 Slug-Renames durch Entfernung generischer Plugin-Praefixe (spezial-, neu-, anwaelte-, notare-, insol-, handelsrecht-int-, notariat-, anw-, fa-, fa-stu-, fa-arb-, fa-fam- u. a.) repo-weit, mit Konflikt-Behandlung (8 Boilerplate-Duplikate geloescht).
  - Phase 2: berufsrecht-wirtschaftspruefer (145), berufsrecht-steuerberater (142), berufsrecht-patentanwaelte (136) entpraefixt; 3 Konflikt-Duplikate geloescht.
  - Insgesamt ~2400 Skills umbenannt, 32 Boilerplate-Skills entfernt.
- Nummern-Dubletten in preussisches-recht und roemisches-recht dedupiert: Boilerplate-Varianten geloescht, ausgearbeitete Fachversionen behalten.
- Mischmasch-Slugs entwortsalatet: 102 Wortsalat-Slugs mit 7+ Tokens auf sprechende H1-Slugs verkuerzt (z. B. venture-capital-recht, festlandchina-recht, beamtenrecht, oeffentliches-baurecht-bauplanung).
- Truncations gefixt: 71 abgeschnittene Slug-Endungen rekonstruiert (-rec -> -rechtsprechungscheck, -kammerantw -> -kammerantwort, -organisationspfli -> -organisationspflicht, -verfa/-verfah -> -verfahren, -praeve -> -praevention, -schreib -> -schreiben, -unterlagenanfor -> -unterlagenanforderung).
- bundesnetzagentur: 5x energie-regulierungsakte-...-rechtsmit -> ...-rechtsmittel.
- startup-hr-personalabteilung-berlin/offboarding-account-checkliste-onboarding aufgeteilt und inhaltlich erweitert: dedizierter Skill offboarding-account-sperre-datenuebergabe mit 13 KB konkretem Inhalt zu Account-Sperre, Datenuebergabe, Rueckgabe-Checkliste, Backup-Aufbewahrungspflichten.
- Codex-Polish v216 uebernommen: Begriff Prueffeld -> Pruefungslinie in 13975 SKILL.md vereinheitlicht; Prueffelder -> Pruefungslinien.

## Erhalten gebliebene semantische Praefixe

- lph- (HOAI-Leistungsphasen), bess-/fusion-/h2- (energierecht-Subdomaenen), plan- (insolvenzverwaltung), dba-/bwa-/susa-/lohn- (Steuerrecht), energie-/telekommunikation-/eisenbahn- (BNetzA), jurisdiktion- (Kartellrecht 130 Laender), beirat- (Gesellschaftsrecht), laienhilfe- (Sozialrecht), bautraeger- (Bau), schoeffe- (Schoeffen), china- (Festlandchina), besold- (beamtenrecht), bwbes- (bundeswehrrecht).

## Qualitaetsbild

- Validator gruen.
- 210 Plugins / 18240 Skills / 204 Testakten.
- SKILLS.md, skills-index/, ASSET_INDEX.md, README.md auf v220.0.0.

# v215.0.0 — Generische Kurz-Praefixe aus Skill-Slugs entfernt; README-Plugin-Liste vervollstaendigt

## Schwerpunkt

- In 52 Plugins wurden generische Kurz-Praefixe aus Skill-Slugs entfernt: hoai-, bho-, rom-, stb-, pralr-, solo-, legw-, kom-, drg-, luft-, see-, dsv-, pe-, space-, vc-, btm-, ifg-, oew-, owi-, str-, stv-, tier-, umv-, vdg-, vbr-, ihl-, chn-, ein-, fran-, infl-, db-, kv-, lease-, tk-, ins-, verl-, inv-, iv-, nkr-, inso-, ips-, vaf-, spez-, elsj-, ifap-, jveg-, liqui-, zvg-, zv-, er-, energie-. Insgesamt rund 3500 Skills umbenannt, zwei Boilerplate-Duplikate in normenkontrollrat-nkr geloescht.
- Plugin energierecht zusaetzlich von er- und energie-Praefixen befreit (46 Renames); die semantischen Sub-Domaenen bess-, fusion- und h2- bleiben als sprechende Praefixe erhalten, ebenso lph- in hoai-leistungsphasen-praxis und plan- in insolvenzverwaltung.
- Haupt-README-Plugin-Tabelle vervollstaendigt: Das Plugin fahrgastrechte (Eisenbahn-Fahrgastrechte VO (EU) 2021/782) war in der alphabetischen Liste vergessen und wurde zwischen factoring-recht und fashion-law-moderecht ergaenzt. Damit listet die Tabelle wieder alle 210 Plugins vollstaendig.
- Skill-Gesamtzahl von 9115 (veraltet aus fruehem Stand) auf den tatsaechlichen Stand 18272 angepasst.

## Qualitaetsbild

- Validator gruen.
- Repo-weiter Praefix-Scan: 0 verbleibende generische Kurz-Praefixe ueber 30 Prozent Plugin-Anteil; nur drei semantische Sub-Domaenen-Praefixe (lph-, bess-, plan-) bestehen bewusst weiter.
- 210 Plugins / 18272 Skills / 201 Testakten.
- SKILLS.md, skills-index/, ASSET_INDEX.md, TESTBERICHT.md, README.md, testakten/README.md auf v215.0.0.

# v213.0.0 — Plugin-Praefix-Wiederholungen aus Skill-Slugs entfernt; forderungsmanagement-klagewerkstatt manuell veredelt

## Schwerpunkt

- Repo-weit alle Skills entpraefixt: 1577 Skills umbenannt + 14 als Duplikat zur Kurzform geloescht, in 192 von 210 Plugins. Pluginname als Slug-Praefix komplett eliminiert (z. B. agb-recht-pruefer-kaltstart-triage -> kaltstart-triage, gesellschaftsrecht-tabellenpruefung-cap-table -> tabellenpruefung-cap-table, bgb-at-anfechtung-vor-auslegung -> anfechtung-vor-auslegung).
- Auch Sub-Praefixe spezial-, freigegeben-, fmkw-, workflow-und- aus den entpraefixten Slugs entfernt. Frontmatter name: synchron aktualisiert. Drei externe Link-Verweise in READMEs und einer YAML auf neue Kurzform-Slugs umgebogen.
- Plugin forderungsmanagement-klagewerkstatt manuell konsolidiert: 84 -> 46 Skills. 38 Boilerplate-Klone und drei Meta-Workflow-Skills entfernt (klage-aus-eigenem-skill, klagevorlage-aus-eigenen-mustern, inkasso-zahlungsklage-ersteller). Alle 46 verbleibenden Skills manuell mit echtem ZPO/BGB-Wissen befuellt: Klageschrift-Pflichtbestandteile § 253 Abs. 2 ZPO, Verzug § 286 BGB, Verzugszinsen § 288 BGB inklusive B2C-5pp / B2B-9pp und 40-Euro-Pauschale § 288 Abs. 5 BGB, Verjaehrung §§ 195 199 203 204 212 BGB, Streitwertgrenzen § 23 Nr. 1 GVG 10.000 EUR ab 01.01.2026, Mahnverfahren §§ 688 ff. ZPO, Mahngerichts-Tabelle nach Bundeslaendern, Vollstreckung §§ 704 ff. ZPO inklusive Pfaendungsgrenzen § 850c ZPO, EU-Verfahren Bruessel Ia VO 1215/2012, EuMVVO VO 1896/2006, EuVTVO VO 805/2004 und EuGFVO VO 861/2007.

## Qualitätsbild

- Validator gruen.
- 0 FULL_PREFIX-Treffer und 0 P2-Praefix-Treffer im repo-weiten Re-Scan.
- 210 Plugins / 18274 Skills / 201 Testakten.
- SKILLS.md, skills-index/, ASSET_INDEX.md, TESTBERICHT.md, README.md, testakten/README.md auf v213.0.0.

---

# v212.0.0 — Rest-Boilerplate aus Skillanfängen entfernt

## Schwerpunkt

- Nach v211 erneut alle 9115 `SKILL.md`-Dateien auf sprachliche Konsolidierungsreste geprüft.
- Restformeln wie `Nutze diesen Skill`, `Nutze diese Quellenkarte`, `Nutze diesen Fehlerkatalog`, `dieser Skill beginnt mit der Sachfrage` und variierende `Dieses Fachmodul greift ...`-Starter entfernt.
- 2906 Skill-Dateien redaktionell nachpoliert: Workflow-Skills bleiben als Workflow erkennbar, Spezialskills starten nun stärker mit ihrem konkreten Abschnitts- oder Fachgegenstand.

## Qualitätsbild

- Kein neuer Wissensschnitt: die Änderung ist eine Sprach- und Auffindbarkeitsbereinigung nach der Verdichtung.
- Artefakt-Scan über alle 9115 Skills: 0 Treffer für die alten Bündelungs-, Kompendiums-, Sammelskill-, Entstehungs- und `Nutze diesen Skill`-Muster.
- First-80-Line-Scan über alle Skillanfänge: 0 Treffer für die definierte Boilerplate-Liste.

## Checks

- `validate-yaml-frontmatter` OK.
- `validate-plugin-structure` OK.
- `git diff --check` OK.

---

# v211.0.0 — Freistehende Skills ohne Bündel-Artefakte

## Schwerpunkt

- Alle `SKILL.md`-Dateien auf Entstehungs-/Bündelartefakte geprüft und die alte Verdichtungssprache entfernt.
- Formulierungen wie `Dieser Skill bündelt`, `Arbeitsmodule`, `Sammelskill`, `Kompendium`, `gehört zum Plugin` und vergleichbare Innenansichten durch freistehende Arbeitsbereich-, Prüffeld- und Output-Sprache ersetzt.
- Kleine Generator-Sprachreste aus der Konsolidierung geglättet, unter anderem `Arbeitsfür`, `Spezial-mit` und unnatürliche Großschreibung in Arbeitsweg-Sätzen.

## Qualitätsbild

- 9115 Skills behalten ihre Inhalte, lesen sich aber nicht mehr wie zusammengeklebte Vorgängerskills.
- Der exemplarisch beanstandete Agrarrecht-Skill ist auf Arbeitsbereich, Prüffelder und Arbeitsweg umgestellt.
- Artefakt-Scan in den Skillanfängen: 0 Treffer für `bündelt`, `Arbeitsmodul`, `Kompendium`, `Sammelskill`, `Entstehungsgeschichte` und `gehört zum Plugin`.

## Checks

- `validate-yaml-frontmatter` OK.
- `validate-plugin-structure` OK.
- `validate-testakten-gesamt-pdf` OK.
- Lokale Release-ZIP-Simulation OK.
- `git diff --check` OK.

---

# v210.0.0 — Skillnamen-Powersprint und Release-Synchronisierung

## Schwerpunkt

- Release-Stand auf v210.0.0 synchronisiert: 210 Plugins, 9115 Skills und 201 Testakten.
- Powersprint gegen Autogen-Muster: alte generische Arbeitsbereich-Formeln entfernt, kurze Skills erweitert und stumpfe Einwort-Slugs durch sprechende, in Claude/Cowork auffindbare Skillnamen ersetzt.
- Kuratierte Skillliste, Skills-Index, Plugin-README-Downloadsektionen, Marketplace und Plugin-Manifeste auf denselben Versionsstand gebracht.

## Qualitätsbild

- Keine Skills unter 120 Wörtern im automatischen Scan.
- Keine `Kompendium`-/`Sammelskill`-Präfixe, keine Einwortnamen und keine alten `Nutze dies`-/Autogen-Beschreibungen.
- Testakten bleiben als reale Arbeitsakten mit Gesamt-PDF-Regel validiert und separat von den Plugin-ZIPs.

## Checks

- `validate-yaml-frontmatter` OK.
- `validate-plugin-structure` OK.
- `validate-testakten-gesamt-pdf` OK.
- `git diff --check` OK.

---

# v69.0.0 — Wahlkampfrecht Praxis

## Neu

- Neues Plugin `wahlkampfrecht-praxis` mit 118 Skills für demokratischen Wahlkampf: Strategie, Plakatierung, Ground Game, Social Media, politische Werbung nach VO (EU) 2024/900, Datenschutz, Parteienfinanzierung, Desinformation, Podien, Schulen, Wahltag und Compliance.
- Neue Arbeitsakte `wahlkampfrecht-landtagswahl-morgenstadt-2026` mit Markdown, EML, DOCX, XLSX, PDF, CSV, JPEG-Screenshots und Gesamt-PDF.

## Synchronisiert

- Repo-Stand auf 167 Plugins, 14160 Skills, 160 Testakten und v69.0.0 synchronisiert.
- Marketplace, Plugin-Manifeste, README, Testakten-Übersicht, Asset-Index, Skills-Index und Downloadsektionen aktualisiert.

---

# v68.0.0 — Solo-Selbstständige und HOAI-Leistungsphasen

## Neu

- Neues Plugin `solo-selbststaendige-praxis` mit 200 Skills für Start, Anmeldung, Steuern, Verträge, Rechnungen, Datenschutz, Statusfeststellung, KSK, Versicherungen, Zahlungsausfall, Krise, Wachstum und Alltagspraxis.
- Neues Plugin `hoai-leistungsphasen-praxis` mit 310 Skills: 40 Querschnitts-Workflows und je 30 Skills für HOAI-Leistungsphasen 1 bis 9 nach Gebäude-/Innenraumplanung.
- Zwei neue Testakten mit Originalformaten und Gesamt-PDF: Solo-Designstudio Falkensee und Kita Mühlenhof Lichtenrade.

## Synchronisiert

- Repo-Stand auf 166 Plugins, 14042 Skills, 159 Testakten und v68.0.0 synchronisiert.
- Marketplace, Plugin-Manifeste, README, SKILLS.md, Skills-Index, Testakten-Übersicht, Asset-Index und Downloadsektionen aktualisiert.

---

# v67.0.0 — Handelsregister, Grundbuchamt und Erbbaurecht

## Neu

- Neues Plugin `handelsregister-praxis` mit 72 Skills für Registergericht, Rechtspfleger/Registerrichter, Beanstandung, FamFG-Beschwerde, Gesellschafterliste, Kapitalmaßnahmen, Löschung, Insolvenzvermerk und registerfeste Nachweise.
- Neues Plugin `grundbuchamt-praxis` mit 64 Skills für Grundbuchauszug, Abteilung I/II/III, § 29 GBO, Zwischenverfügung, Rang, Briefgrundschuld, Aufgebot und grundbuchtaugliche Unterlagen.
- Neues Plugin `erbbaurecht-praxis` mit 50 Skills für Erbbaurechtsvertrag, Erbbauzins, Heimfall, Finanzierung, Zustimmung, Zwangsversteigerung und Erbbaugrundbuch.
- Drei neue Demonstrationsakten mit EML, DOCX, XLSX, PDF, JPEG und Gesamt-PDF.

## Synchronisiert

- Marketplace und Plugin-Manifeste auf v67.0.0 vorbereitet; Übersichten und Downloadsektionen werden regeneriert.

---

# v66.0.0 — Kriegsdienstverweigerung und Wehrdienst

## Neu

- Neues Spezialplugin `kriegsdienstverweigerung-wehrdienst` mit 136 Skills zu Art. 4 Abs. 3 GG, KDVG n. F. 2026, Antrag über BAPersBw, BAFzA-Entscheidung, Gewissensbegründung, Soldaten, Reservisten, Rechtsschutz, § 13 KDVG, § 75 VwGO und klarer Abgrenzung zur Totalverweigerung.
- Neue Testakte `kriegsdienstverweigerung-gewissensantrag-berlin-2026` mit Markdown-Aktenstücken, EML-Mailverkehr, DOCX-Entwürfen, XLSX-Fristenlog, JPG-Notizkarte und Gesamt-PDF.
- Bundeswehrrecht-KDV-Routing auf das neue Spezialplugin verlinkt.

## Synchronisiert

- Repo-Stand auf 161 Plugins, 13346 Skills, 154 Testakten und v66.0.0 synchronisiert.
- README, SKILLS.md, Skills-Index, Testakten-Übersicht, Asset-Index, Marketplace und Plugin-Downloadsektionen aktualisiert.

## Validierung

- Plugin-Struktur, YAML-Frontmatter, Gesamt-PDF-Regel, ZIP-/Diff-Sanity werden im Release-Lauf geprüft.

# v65.0.0 — Versammlungsrecht Praxisplugin

## Schwerpunkt

- Neues Plugin `versammlungsrecht` mit 54 Skills für Anzeige, Landesrecht, Behörde, Fristen, Spontan- und Eilversammlung, Ordner, Kooperationsgespräch, Auflagenprüfung, Verbot, Bannmeile, Tag-der-Versammlung-Plan und Eilrechtsschutz.
- Bestehende Klimacamp-/Art.-8-Arbeitsakte zusätzlich dem neuen Plugin zugeordnet; Plugin-Downloadsektionen und Übersichten werden dadurch automatisch mit Gesamt-PDF und Akten-ZIP versorgt.
- Repo-Stand auf 160 Plugins, 13210 Skills, 153 Testakten und v65.0.0 synchronisiert.

## Checks

- `validate-plugin-structure` OK.
- `validate-yaml-frontmatter` OK.
- `validate-testakten-gesamt-pdf` OK (153 Testakten).
- `git diff --check` OK.
- Inventarcheck: 160 Plugins, 160 Plugin-Manifeste, 13210 Skills, 153 Testakten; kein Plugin unter 30 Skills.

---

# v64.0.0 — Medizinrecht Hightech-Boost und Kanzlei-Mandant-Lifecycle

## Schwerpunkt

- `fachanwalt-medizinrecht` von 54 auf 136 Skills erweitert: ATMP, Gentherapie, CAR-T, CRISPR/Base Editing, Hospital Exemption, PEI/EMA-Verfahren, Pharmakovigilanz, ePA, DiGA, EHDS/Genomdaten, KI-Medizinprodukte, IVDR, Companion Diagnostics, Krankenhausreform, Robotik, Implantat-/Rückruf- und Hightech-Haftung.
- Neue Quellenkarte für modernes Medizinrecht mit amtlichen und frei zugänglichen Startquellen zu ATMP/Gentherapie, Patientenrechten, ePA/DiGA, EHDS, EU-HTA und Produkthaftung.
- Neues Plugin `kanzlei-mandant-lifecycle` mit 115 Skills für die gesamte Kanzlei-/Mandant-/Rechtsabteilungsbeziehung: Mandatsstart, Scope, Outside Counsel Guidelines, Budget, eBilling, Rechnungskontrolle, Dashboards, Gerichtsakten-Fortschritt, Erwartungsmanagement, Eskalationen, Quickwins, Closeout und gemeinsame KI-Arbeitsräume.
- Neue Demonstrationsakte `mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech` mit Markdown-Aktenstücken, EML-Mails, CSV/XLSX-Budgetdaten, DOCX-Entwürfen, PDF-Anlagen, Whiteboard-Bild und Gesamt-PDF.
- README, SKILLS.md, Skills-Index, Testakten-Übersicht, Asset-Index, Plugin-READMEs und Downloadsektionen auf 159 Plugins, 13156 Skills, 153 Testakten und v64.0.0 synchronisiert.

## Checks

- `validate-plugin-structure` OK.
- `validate-yaml-frontmatter` OK.
- `validate-testakten-gesamt-pdf` OK (153 Testakten).
- `git diff --check` OK.
- Inventarcheck: 159 Plugins, 13156 Skills, 153 Testakten; kein Plugin unter 30 Skills.

---

# v63.0.0 — Gesamt-Bibliothek, neue Plugins und Skill-Qualitätsboost

## Schwerpunkt

- Konsolidierter Major-Bump von v62.0.0 auf v63.0.0 nach Zusammenführung der neuen Plugin-, Skill- und Testakten-Erweiterungen.
- Bestand synchronisiert auf 158 Plugins, 12959 Skills und 152 Testakten; kein Plugin liegt mehr unter 30 Skills.
- Alle Plugin-Manifeste und die Marketplace-Definition auf 63.0.0 angeglichen; README, SKILLS.md, Skills-Index, Testakten- und Asset-Übersichten regeneriert.
- Durchnummerierte Platzhalter-Skillreihen in `verbraucher-rechtsstaat-alltag`, `berufsgerichtliche-verfahren-freie-berufe` und `schoeffen-handelsrichter-praxis` durch sprechende, fallnahe Spezialskills ersetzt.
- Neue und ausgebaute Plugin-Familien u. a. für Softwarerecht, Urheberrecht, IT-Sicherheits-/NIS-2-Compliance, Hinweisgeberschutz, Handelsvertreterrecht, Hochschul-/Schul-/Prüfungsrecht, Verbraucheralltag, Staatsanwaltschaftspraxis, Schöffen/Handelsrichter, Berufsverfahren freier Berufe, AG/SE-Hauptversammlung, Aufsichtsrat, NDA, Treuepflicht, HR-Startup-Praxis, Private-Equity- und Bank-/Regulierungsthemen.

## Checks

- `validate-plugin-structure` OK.
- `validate-yaml-frontmatter` OK.
- `validate-testakten-gesamt-pdf` OK (152 Testakten).
- `git diff --check` OK.
- Inventarcheck: Marketplace 158 Plugins, 158 Plugin-Manifeste, 12959 Skills, 152 Testakten; keine alten Platzhalter-Slugs der drei ersetzten Skillserien.

---

# v62.0.0 — Major-Bump: konsolidierter Stand nach v61-Reihe

## Schwerpunkt

- Major-Versionsbump von 61.2.2 auf 62.0.0. Inhaltlich identisch mit v61.2.2; signalisiert den Abschluss der v61-Reihe nach Umlaut-Fix, README-Konsolidierung, Beamtenrecht-Quellenanker-Korrektur, Vergaberecht-Workbench-Boost, Forschungszulage-Akten-Erweiterung und globalem Halluzinations-Cleanup.
- Alle 132 plugin.json + marketplace.json (outer und alle 132 Plugin-Einträge) auf 62.0.0 synchron.
- Doku-Stand-Marker in README.md, SKILLS.md, ASSET_INDEX.md und testakten/README.md auf v62.0.0 angeglichen (vorher leichter Drift zwischen v61.2.0 und v61.2.2).
- Plugins: 132 · Skills: 9517 · Testakten: 142 · Fachanwalts-Profile: 24.

## Checks

- `validate-plugin-structure` OK.
- `validate-testakten-gesamt-pdf` OK (142 Testakten).
- Alle plugin.json + marketplace.json einheitlich auf 62.0.0.

---

# v61.2.2 - Vergaberecht Workbench Boost

## Schwerpunkt

- `fachanwalt-vergaberecht` von 54 auf 83 Skills erweitert.
- Neue Workbench-Skills fuer Vergabe-OS, Schwellenwerte 2026/2027, Vergabeakte, Auftragswert/Losbildung, Verfahrenswahl, Markterkundung, Leistungsbeschreibung, Eignung, Bieterfragen, Angebotsoeffnung, Aufklaerung/Nachforderung, Wertungsmatrix, ungewoehnlich niedrige Angebote, Paragraph 134/135 GWB, Paragraph 132 GWB, Rahmenvereinbarungen, Unterschwellenrechtsschutz, Foerdermittel, Wettbewerbsregister, VK-/OLG-Strategie, Padlet-Canvas, KI-/Cloud-Beschaffung, Nachhaltigkeit und Resilienz ergaenzt.
- Alle Vergaberecht-Skills mit v61.2.2-Workbench-Boost gehaertet: Rollen-/Fristen-/Schwellenwert-Gate, Anfaengererklaerung, Padlet-/Tabellenpflicht bei komplexen Faellen, Auftraggeber-Dokumentationslogik und Bieter-Ruege-/Kausalitaetslogik.
- Fuenf neue Templates fuer Master-Padlet, Schwellenwert-Rechner, Wertungsmatrix, Ruege/VK-Powerdraft und Vergabeakte-Lueckenliste plus Quellen-/Aktualitaetsgate ergaenzt.
- Mit dem v61.2.1-Remote-Nachzug zusammengefuehrt; Gesamtbestand jetzt 132 Plugins, 9517 Skills, 142 Testakten.

## Checks

- Plugin-Struktur, YAML-Frontmatter, Testakten-Gesamt-PDF-Regel und Whitespace-Check im finalen Merge geprueft.

---

# v61.2.1 — Forschungszulage-Akte und Release-Asset-Glattzug

## Schwerpunkt

- Neue große Arbeitsakte `forschungszulage-sensorik-startup-taunus` für das Plugin `forschungszulage-antragstellung`.
- Enthalten sind 62 Dateien: 37 Markdown-Aktenstücke, 5 EML-Mails, XLSX/CSV-Zahlenmodelle, 3 DOCX-Entwürfe, 3 JPEG-Bildanlagen, 7 PDF-Anlagen und ein 60-seitiges Gesamt-PDF.
- Inhaltlicher Schwerpunkt: BSFZ-Rückfrage, FuE-Abgrenzung, Stand der Technik, technische Unsicherheit, Laborjournal mit negativen Ergebnissen, Ticket-/Git-Auszüge, Auftragsforschung Lissabon, Unterauftrag-Risiko, Kumulierung mit ZIM/Horizon/Landesförderung, Finanzamt-Kürzung, Einspruch, Bemessungsgrundlage 2024-2026, KMU-/Verbundfragen und Liquiditätsdarstellung gegenüber Bank/Investoren.
- Plugin-README, Testaktenübersicht, Asset-Index und Downloadmapping auf 142 Testakten synchronisiert.
- Ein älterer fehlender Asset-Index-Eintrag für `gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll` wurde nachgetragen.
- Plugin-Manifeste bleiben unverändert; diese Patch-Version ist ein Testakten-/Release-Asset-Glattzug.

## Checks

- `validate-plugin-structure` OK.
- `validate-testakten-gesamt-pdf` OK (142 Testakten).
- Testaktenlisten-Abgleich: 142 Ordner, 142 README-Einträge, 142 Asset-Index-Einträge, 142 Direktdownload-Links.
- `git diff --check` OK.

---

# v61.2.0 — Testakten-Umlaut-Fix, NeuroChain-Akte, README-Konsolidierung und Beamtenrecht-Quellenanker

## Schwerpunkt

- Umlaut-Sanierung über inzwischen 924 Testakten-Dateien (638 in Phase 1 via Hunspell, weitere 286 in Phase 2 via hash-/ID-geschütztem Skript `scripts/fix-umlaute-protected.py`). `ae`/`oe`/`ue`/`ss` → `ä`/`ö`/`ü`/`ß` in Markdown, EML, TXT und CSV.
- Hash-Schutz in Phase 2: YAML-Frontmatter, fenced + inline Code, Markdown-Links, URLs, Hex-Strings ≥ 4 Zeichen, Slug-Tokens (lowercase-with-dashes, snake_case) und CSV-IDs sind explizit gestasht. Iterative Unstash-Auflösung verhindert geschachtelte Placeholder. Pre-Write-Check bricht ab, falls ein Umlaut direkt neben einer Hex-Sequenz landen würde.
- Neue Testakte **NeuroChain Labs — Gründung eines KI/Krypto-Startups in Berlin** (`gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll`) mit 14 Aktenstücken, 6 E-Mails, 2 Tabellen und Gesamt-PDF.
- Plugin-READMEs konsolidiert: veraltete `plugin-testakten-section` aus 117 READMEs entfernt; einzig verbleibende autogenerierte Liste ist die Sofort-Download-Sektion. Skript `inject-plugin-testakten-section.py` ersatzlos gelöscht; `inject-plugin-sofort-download-section.py` ist die alleinige Quelle.
- Doppelte Testakten-Sektionen in weiteren 107 Plugin-READMEs entfernt (33× verschachtelte `<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->`-Blöcke innerhalb der `plugin-sofort-download`-Marker, plus 74× reine Duplikat-Sektionen `## Download`/`## Direkt-Download`/`## Direkt herunterladen`).
- Manuelle Konsolidierungen in `grosskanzlei-corporate-ma`, `strafbefehl-verteidiger`, `urteilsbauer-relationsmacher`, `insolvenzrecht`, `gesellschaftsrecht` und `forderungsmanagement-klagewerkstatt`.
- Beamtenrecht-Quellenanker korrigiert (5 Skills): § 27 BBG → § 45 BBG (begrenzte Dienstfähigkeit), § 26 → § 44 BBG (Dienstunfähigkeit), § 29 → § 46 BBG (Reaktivierung), § 6 → § 15 BEEG (Elternzeit-Anspruch), § 80 → § 79 BBG (Elternzeit-Versorgung), § 9 BeamtStG → § 9 ArbZV (Altersteilzeit-Blockmodell).
- Gesamtzahl Testakten jetzt 141.

## Checks

- `validate-plugin-structure` OK.
- `validate-testakten-gesamt-pdf` OK (141 Testakten).
- 0 Hash-/ID-Korruption in CSV-Spalten (`q_id`, `arbeits_id`, `sha256_kurz` etc.).
- 0 doppelte Testakte-ZIP-Links in Plugin-READMEs.
- YAML-Frontmatter, Whitespace und Hunspell-Wörterbuch grün.

---

# v61.1.1 — Forschungszulage-Plädoyer erweitert

## Schwerpunkt

- `forschungszulage-antragstellung` um den neuen Skill `fz-plaedoyer-begruendung-und-verteidigung` erweitert.
- Plädoyer-Workflow für BSFZ, Finanzamt, Einspruch, Geschäftsführung/CFO sowie Verlust-, Krisen- und Insolvenzlagen ergänzt.
- Router, allgemeiner Einstieg, Portaltexte-Skill, README, SKILLS.md und Skills-Index auf den neuen Plädoyer-Pfad nachgezogen.

## Checks

- YAML-Frontmatter, Plugin-Struktur und Whitespace-Check grün.

---

# v61.1.0 — Beamten-/Richterrecht Spezialskills konsolidiert

## Schwerpunkt

- 50 hochspezialisierte Skills aus PR #205 in das bestehende `beamtenrecht`-Plugin übernommen, nicht als separates Parallelplugin.
- Cluster für Konkurrentenschutz und Beurteilung, Besoldung, Versorgung, Beihilfe und Heilfürsorge, Urlaub und Elternzeit, Dienstunfall und Krankheit, Disziplinarrecht, Nebenpflichten und Statusrecht sowie Richterrecht ergänzt.
- Quellenhygiene im Beamtenrecht weiter geschärft: verifizierte Anker aus der Beamten-/Richterrecht-Wissenssammlung, keine BeckRS-/juris-Blindzitate, Aktenzeichen nur mit prüfbarem Quellenanker.

## Synchronisierung

- `beamtenrecht` wächst auf 125 Skills.
- Marketplace, Plugin-Manifeste, Haupt-README, SKILLS.md, Skills-Index und Asset-Index auf `v61.1.0` nachgezogen.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Testakten-Gesamt-PDF-Regel und Whitespace-Check grün.

---

# v61.0.0 — Corporate/M&A Deal-OS Boost

Großer Ausbau des freistehenden `grosskanzlei-corporate-ma`-Plugins zu einer noch agentischeren Big-Law-Deal-Workbench.

## Schwerpunkt

- `grosskanzlei-corporate-ma` von 75 auf 125 Skills erweitert: Deal-OS-Orchestrator, Padlet-Canvas, Matrix Factory, Junior-Mentor, Weakness Coach, Battlecards, Term-Sheet-to-SPA, VDD/Legal Fact Book, Authority Matrix, Cap Table/UBO, Locked Box/Completion Accounts, Earn-out, Warranty/Indemnity, MAC/Ordinary Course, Clean Team/Gun-Jumping, FSR, Sector Regulatory, Financing/Security, Signing/Closing Room und Register-Implementation.
- Alle 125 Corporate/M&A-Skills mit V61 Deal-OS Boost gehärtet: Anfängerführung, Deal-Phasen-Erkennung, Padlet-/Tabellen-Ausgabe, Schwachstellenreparatur, Quellen-/Aktualitätsgate und Human-in-the-loop-Quality-Gate.
- Sechs neue Templates für Master-Padlet, Junior-Feedback, Matrix Factory, Negotiation Battlecards, Risk Heatmap und Official Source Check ergänzt.

## Synchronisierung

- Marketplace und alle Plugin-Manifeste auf `v61.0.0` gesetzt.
- `README.md`, `SKILLS.md`, Skills-Index und Asset-Index auf 132 Plugins, 9437 Skills und 140 Testakten nachgezogen.

## Checks

- Plugin-Struktur, YAML-Frontmatter, Testakten-Gesamt-PDF-Regel und Whitespace-Check laufen im Release-Check.

---

# v60.0.1 - Beamtenrecht/Richterrecht Wissenssammlung

- Beamtenrecht-Plugin um vertiefte Skills zur BVerfG-Alimentationsrechtsprechung, zeitnahen Geltendmachung, Föderalismusreform, BDG-2024, Suspendierung, Verfassungstreue, Richterdienstaufsicht, Richterdienstgerichten und EU-Justizunabhängigkeit erweitert.
- Recherchematerial aus dem Branch `recherche/beamtenrecht-richterrecht-wissenssammlung` als gesonderte Arbeitsablage übernommen.
- Quellenhygiene im Beamtenrecht verschärft: keine privaten Datenbankzitate, keine Literatur-Blindzitate, keine ungeprüften richterdienstgerichtlichen Fundstellen.

# v60.0.0 — Beamtenrecht, US-Copyright-Registrierung und Release-Sync

Release-Sprung auf v60.0.0 mit zwei neuen Plugins und einer neuen Beamtenrecht-Demonstrationsakte.

## Neu

- `beamtenrecht`: großes Plugin für Bundes- und Landesbeamtenrecht, Richterdienstrecht, Laufbahn, Besoldung, Versorgung, Konkurrentenstreit, Disziplinarrecht, Dienstunfähigkeit, Beihilfe, Richterbeurteilung und verständliche Mandatsführung mit 59 Skills.
- `testakten/beamtenrecht-richterlaufbahn-besoldung-mondsee`: neue Beamtenrecht-/Richterlaufbahn-Akte mit 15 Einzeldateien, EML, CSV, Chatnotizen und Gesamt-PDF.
- `us-copyright-registrierung-verlag`: kleines Praxis-Plugin für deutsche Verlage zur US-Copyright-Registrierung über eCO mit 13 Skills zu Account, Standard Application, Gebühren, Deposit, Shipping Slip, Versand und Monitoring.

## Synchronisierung

- Marketplace und alle Plugin-Manifeste auf `v60.0.0` gesetzt.
- `README.md`, `SKILLS.md`, Skills-Index, Testaktenübersicht und Asset-Index auf 132 Plugins, 9371 Skills und 140 Testakten nachgezogen.
- Gesamt-PDF für die neue Beamtenrecht-Akte erzeugt und in Plugin-/Testakten-READMEs verlinkt.

# v59.0.0 — Skill-Boost, Legistik-Ressort-Mapping und Release-Synchronisierung

Nachgezogener Hauptstand nach v58.0.0: Claude/Perplexity-Ergänzungen wurden übernommen, alle Plugin-/Marketplace-Versionen stehen einheitlich auf v59.0.0, und die Übersichten sind wieder mit der tatsächlichen Skillzahl synchron.

## Schwerpunkt

- `legistik-werkstatt` stark erweitert: Ressort-Router, Ressortaufgaben, Ressort-spezifische Fachpfade, RuleMapping, Norm-zu-Entscheidungsbaum, Vollzugstauglichkeit, Verweisungslogik und Anschluss an die allgemeine Legistik-Werkstatt.
- `fachanwalt-strafrecht` um Pro-Verteidiger-Skills zu dysfunktionaler/konfliktiver Verteidigung ergänzt: Beweisantragsstrategie, Befangenheit, § 257 StPO, § 143a StPO, § 138a StPO, Sitzungspolizei, Verschleppungsabgrenzung, KI-Schriftsatz-Fallen und strategische Mandantenführung.
- 158 magere Skills in 10 Plugins veredelt, insbesondere in Apothekenrecht, Bürokratieversteher, Bundesnetzagentur-Verfahren, Bundeswehrrecht, E-Commerce, Factoring, Krankenhausrecht, Private Equity und Robotik-Recht.
- `normenkontrollrat-nkr` präzisiert: NKRG-Aufgaben, Unabhängigkeit, Vorsitz, BMJ-Anbindung, Digitalcheck und DDG-Mere-Conduit-Bezug korrigiert.
- Tote Legistik-RuleMapping-Verweise in Ressort-Skills und Router auf `legw-rmap-grundlagen` umgebogen.
- Marketplace, alle 130 Plugin-Manifeste, Haupt-README, Testaktenübersicht, Skill-Gesamtübersicht und Skills-Index auf 130 Plugins, 9299 Skills und 139 Testakten synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel und Whitespace-Check grün.

---

# v58.0.0 — Private Equity, Batteriespeicher, NKR und Loan-Transfer

Großer Fachausbau für Private Equity, Private Credit, Batteriespeicherrecht, NKR-Gesetzesprüfung und distressed Finanzierungen.

## Schwerpunkt

- Neues Plugin `private-equity-praxis` mit 103 Skills: Anfänger- und Profi-Workflow, Fund Formation, KAGB/AIF/ELTIF, Fundraising, Subscription, Side Letter, Deal Execution, Legal DD, SPA/APA, Management Participation, W&I, Private Credit, Schuldschein, LMA, NPL, Portfolio, Exit, Distressed M&A und Qualitygate.
- `energierecht` um 30 Batteriespeicher-Skills plus Fusions-/Großprojekt-Skills erweitert: Bauleitplanung, BImSchG-Screening, Brandschutz, Netzanschluss, Netzentgelte, Marktrollen, Co-Location, Grundlast-/Kapazitätsmechanismen, Diesel-Notstrom, Power Quality, Wasser/Boden, KRITIS/NIS2, Cyber, physische Sicherheit, Finanzierung, EPC/O&M, Versicherung und Rechtsmittel.
- Corporate- und Insolvenz-Plugins um Schuldscheindarlehen, Übertragung von Schuldscheindarlehen, LMA-Facility-Transfer, NPL-Kreditkauf, Kreditzweitmarktgesetz, Distressed Debt und Loan-to-own-Schnittstellen ergänzt.
- Neues Plugin `normenkontrollrat-nkr` aus dem aktuellen Hauptstand integriert und auf v58 synchronisiert: 37 Skills plus Testakte zur elektronischen Erreichbarkeit im Handelsregister, NKR-Stellungnahme, Erfüllungsaufwand, SKM, Digitalcheck, Alternativen, One-in-one-out und Ressortkommunikation.
- Neue Testakten mit Gesamt-PDF und ZIP-Eintrag: `batteriespeicher-brandenburg-berlin-resilienz`, `kernfusion-transrapid-starnberger-see` und `private-equity-buyout-schuldschein-npl-heidelberg`.
- Marketplace, Haupt-README, Testaktenübersicht, Skill-Gesamtübersicht und Skills-Index auf 130 Plugins, 9156 Skills und 139 Testakten synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur und Gesamt-PDF-Regel grün.

---

# v57.0.0 — Skill-Qualitätssweep, Quellenhygiene und schlanke Gesamt-PDFs

Großer Repo-weiter Qualitäts- und Release-Sweep nach den v56-Erweiterungen.

## Schwerpunkt

- Alle 8698 Skills geprüft und mit einem einheitlichen Qualitäts-Hardening gegen generische Antworten, Scheinpräzision, ungeprüfte Rechtsprechung und Literatur-Blindzitate versehen.
- Zentrale Zitierregel auf v4.1 geschärft: keine BeckRS-/juris-/Kommentar-/Aufsatz-Blindzitate, keine aktuellen Palandt-/Pahlen-Zitate, Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle.
- Kurze und hakelige Skills in `gesellschaftsgruender` und `anlagen-zu-schriftsaetzen` weiter vertieft.
- Strafrechts-Findings korrigiert: § 223 StGB/§ 230 StGB bei einfacher Körperverletzung, § 238 StGB nach geltendem Recht mit `wiederholt`, Abs. 2/Abs. 3 sauber getrennt.
- Alle 132 Gesamt-PDF-Testakten neu gebaut: Die erste Seite startet jetzt aktennah mit Aktenname und Inhaltsübersicht, ohne README-, ZIP-, Download-, Release- oder Testakten-Meta-Hinweise.
- Marketplace, Plugin-Manifeste, Haupt-README, Skill-Gesamtübersicht, Skills-Index und Asset-Index auf 128 Plugins, 8698 Skills und 132 Testakten synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, First-Page-Meta-Scan, Diff-Whitespace-Check und Release-Versionssynchronisierung grün.

---

# v56.0.0 — Factoring, Gesundheitsregulierung, BNetzA, E-Commerce und Wehrrecht

Großer Fachplugin-Ausbau mit sieben neuen Rechtsgebieten und vertieften bestehenden Plugins.

## Schwerpunkt

- Neue Plugins: `factoring-recht`, `krankenhausrecht`, `goae-gebuehrenordnung-aerzte`, `apothekenrecht`, `ecommerce-recht`, `bundeswehrrecht-wehrrecht` und `bundesnetzagentur-verfahren`.
- `bundesnetzagentur-verfahren` mit 220 Skills für Energie, Telekommunikation, Post, Eisenbahn, Digital Services Act/DDG und allgemeine BNetzA-Verfahren.
- `kartellrecht-marktabgrenzung-pruefung` über die reine Marktabgrenzung hinaus ausgebaut: Art. 101/102 AEUV, GWB, Vertikal-/Horizontal-GVO, Fusionskontrolle, Private Enforcement, Dawn Raid und Compliance.
- `kindeswohlgefaehrdung-eilantrag` stark um Versorgungsausgleich erweitert: interne/externe Teilung, Anrechte, Versorgungsträger, Vereinbarungen, Anpassung, Abänderung, Beschwerde und Mandantenkommunikation.
- Marketplace, Plugin-READMEs, Skill-Gesamtübersicht, Haupt-README und Asset-Index auf 128 Plugins, 8696 Skills und 132 Testakten synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Skill-Index, Downloadsektionen, ZIP-Bau und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v55.0.0 — Gesellschaftsgründer, BGB BT, HGB und Methodenlehre

Großer Ausbau der zivil- und wirtschaftsrechtlichen Grundwerkzeuge mit zwei neuen Plugins, stärkerem Gesellschaftsgründer und vertiefter Methodenlehre.

## Schwerpunkt

- Neues Plugin `bgb-bt-pruefer` mit 54 Skills: Kauf, Miete, Werk, Reise, Dienst, Auftrag, Geschäftsbesorgung, Bürgschaft, GoA, Bereicherung, Delikt, Schadensrecht, Regress, Verjährung und BGB-BT-Kaltstart.
- Neues Plugin `handelsrecht-hgb` mit 51 Skills: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, OHG, KG, stille Gesellschaft, Handelsgeschäfte, kaufmännisches Bestätigungsschreiben, § 377 HGB, Fracht, Spedition, Lager und HGB-Verfahrensfragen.
- `gesellschaftsgruender` auf 100 Skills ausgebaut: Anfänger-Kaltstart, einfache Sprache, Rechtsformnavigation, Gründerrollen, Notarbriefing, Bank/KYC, Transparenzregister, IP/Open Source, Daten/KI, regulierte Geschäftsmodelle, Founder Vesting, ESOP/VSOP, Seed-Runde, Registerbeanstandung und erste 100 Tage.
- `methodenlehre-buergerliches-recht` auf 66 Skills erweitert: positivistische Rückbindung an Text und Gesetz, freiheitliche und konservative Methodenkritik, institutionelle Folgen, Empirie- und Quellenkritik, Red-Team gegen postfaktische Argumente und methodenehrliche Schriftsatzarbeit.
- Neue Testakte `bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt` mit E-Mails, Kosten-/Fristen-CSV und Gesamt-PDF.
- Neue Testakte `handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona` zu eGbR/OHG-Statuswechsel, KG-Investor, Prokura, Handelskauf und § 377 HGB.
- Gesellschaftsgründer- und Methodenlehre-Akten erweitert; Gesamt-PDFs neu gebaut.
- Marketplace, Haupt-README, Testaktenübersicht, Asset-Index und Skill-Index auf 121 Plugins, 7771 Skills und 131 Testakten synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, Diff-Whitespace-Check und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v54.1.0 — Anlagen zu Schriftsätzen: K1-Sortierung und Anlagenpaket-Qualitygate

Gezielter Ausbau des Plugins `anlagen-zu-schriftsaetzen` für große gerichtliche Anlagenpakete, K1-Konvolute und beA-/ERV-taugliche Einreichungen.

## Schwerpunkt

- README neu erklärt: aus chaotischem Mandantenordner, Schriftsatz und halb sortierten Dateien wird eine gerichtstaugliche Anlagenstruktur mit K/B/AST/AG-Nummern, Belegmatrix, Konvolutdeckblättern, Hashlog, Lückenliste und Versandcheck.
- Skillset von 54 auf 79 Skills erweitert: K1-Sortierwerkstatt, Schriftsatz-Anlagen-Mapping, Duplikat-/Versionen-/Hashlog, beA-Paketierung, OCR/Scanqualität, E-Mails/Chats/Screenshots, Excel-Zahlenbeweis, Fremdsprachen, Nachreichung, Berufung, Schiedsverfahren, Massenanlagen und finaler Qualitygate-Check.
- Acht generische Auto-Skills konkretisiert, damit sie nicht mehr bloß generische Spezialworkflow-Hüllen sind, sondern brauchbare Anlagen-, Beweis- und Versandwerkzeuge.
- Werkmann-Testakte erweitert: neue K1-Sortierakte mit Sortierprotokoll, Deckblatt, Belegmatrix, beA-Paketierungsplan, Duplikat-/Hashlog, Redaktionsprotokoll, Nachreichungsplan, Finalcheck, Mandantennachforderung, EMLs, CSV, DOCX und XLSX.
- Gesamt-PDF der Werkmann-Akte neu gebaut: 52 Quelldateien, 85 Seiten.
- Zentrale Quellenanker für ZPO § 130a/§ 130d, BRAO § 31a und ERVV ergänzt; falscher § 43e-BRAO-Rest entfernt.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel und Diff-Whitespace-Check grün.

---

# v54.0.0 — German Legal AI Plugins and Skills

Major-Release zur Stabilisierung des Gesamtwerks: 119 Plugins, 7579 Skills, 129 Testakten. Codex-Findings Runde 5 eingearbeitet, READMEs poliert, Validator und Smoke-Tests grün.

## Schwerpunkt

- **Codex-Findings v5 behoben (P2):** `aktenaufbereiter-strafrecht` Bandendiebstahl-Zitate korrigiert (§ 244 I Nr. 2 / § 244a / § 263 V statt fälschlich § 244 IV, Strafrahmen Wohnungseinbruchsdiebstahl § 244 Abs. 4 klargestellt). `verkehrsowi-verteidiger` und `fachanwalt-verkehrsrecht`: § 25 OWiG (Einziehung) statt Fahrlässigkeit, § 10 OWiG ergänzt, FeV-Punktekatalog von „Anlage 12“ auf **„Anlage 13 zu § 40 FeV (Punktekatalog FAER)“** korrigiert, § 248b StGB als „unbefugter Gebrauch eines Fahrzeugs“ statt „Kraftfahrzeugdiebstahl“.
- READMEs (Haupt-README, SKILLS.md, Testakten-README) auf `v54.0.0` synchronisiert.
- Validator und Plugin-Struktur-Check grün; Drift in Testaktenübersicht entfernt.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, ZIP-Bau und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v53.6.0 — Robotik-Recht-Plugin mit großer Demonstrationsakte

Neues Plugin `robotik-recht` für physische Robotik in Deutschland und der EU: Maschinenverordnung, KI-VO, Produkthaftung, Produktsicherheit, Datenschutz, Cyber Resilience Act, Data Act, Medizinrobotik, Arbeitsschutz, Marktüberwachung, Rückruf, Verträge und Streitfall.

## Schwerpunkt

- `robotik-recht` neu mit 143 Skills: Kaltstart, Rollenmatrix, CE-/Produktakte, Maschinenverordnung, KI-VO Art. 3/5/6/Anhang III, Hochrisiko-KI, CRA/SBOM, Data Act, DSGVO/DSFA, Produkthaftung, Rückruf, Marktüberwachung, Robot-as-a-Service, Medizin-/Pflege-/Service-/Cobot-/AMR-Robotik und Litigation.
- Neue Akte `robotikrecht-roboterflotte-vellbruck-muenchen` mit 69 Quelldateien und 184-seitigem Gesamt-PDF: Cobot-Werkbank, AMR-Flotte, Pflegepilot, Unfall, Betreiberänderung, Patch-Dilemma, Datenschutzbeschwerde, Behördenkontakt, Versicherer- und Lieferkettenstreit.
- Quellenanker auf amtliche/frei zugängliche Quellen: EUR-Lex, Gesetze im Internet, BAuA, EU-Kommission, BGH und Safety Gate.
- Marketplace, Plugin-READMEs, Testaktenübersicht, Skill-Gesamtübersicht, Asset-Index und Haupt-README auf `v53.6.0` synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, ZIP-Bau und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v53.5.0 — Miet/WEG und Migrationsrecht auf Großformat

Ausbau der beiden Fachanwalts-Plugins `fachanwalt-miet-wohnungseigentumsrecht` und `fachanwalt-migrationsrecht` auf große, workflowstarke Skillsets.

## Schwerpunkt

- `fachanwalt-miet-wohnungseigentumsrecht` auf 225 Skills erweitert: Laienmodus, First-Year-Coach, Wohnraum, Gewerberaum, Betriebskosten, Heizkosten, CO2-Kosten, Kündigung/Räumung, Modernisierung, Mietpreisbremse, WEG-Beschlüsse, Hausverwaltung, bauliche Veränderungen, GEG/Wärmepumpe, E-Ladung, Photovoltaik, Beweis- und Fristenworkflows.
- `fachanwalt-migrationsrecht` auf 376 Skills erweitert: stärkere Kaltstartführung, einfache Sprache, Spanisch-Modus, Blaue Karte EU, Fachkräfte, Chancenkarte, Visum, Familiennachzug, Asyl, Dublin/GEAS, Einbürgerung, Duldung, Abschiebungsabwehr, Staatenlosigkeit und Staaten-/Gebietschecks für nahezu alle relevanten Herkunfts-, Transit- und Zielstaaten einschließlich Palästina, Nordzypern und Westsahara.
- Quellenanker für amtliche Normtexte, BGH/BAMF/BMI/Auswärtiges Amt, EUR-Lex, EUAA, UNHCR, HUDOC und Council of Europe ergänzt.
- Marketplace, Plugin-READMEs, Skill-Gesamtübersicht, Asset-Index und Haupt-README auf `v53.5.0` synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, ZIP-Bau und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v53.4.0 — AGB-Recht-Prüfer mit 200 Skills

Neues Plugin `agb-recht-pruefer` als großes Werkzeug für deutsches AGB-Recht: Prüfen, Entwerfen, Redlinen, Verhandeln, Rollout und Streitverteidigung.

## Schwerpunkt

- 200 neue Skills für AGB-Kaltstart, AGB-Entwurf, Live-Check auf Gesetze im Internet, Klauselinventar, B2C/B2B/B2B2C, Einbeziehung, § 305 bis § 310 BGB, UKlaG, Preisanpassung, Haftung, Laufzeit, Kündigung, Gewährleistung, digitale Bestellstrecken, SaaS, Cloud, Banking, Payment, Miete, Arbeit, Bau, Franchise, Marketplace, KI-Services und zahlreiche weitere Klausel-/Branchenfamilien.
- Starker `allgemein`-Skill mit Weichenstellung `prüfen` oder `entwerfen`, stummem Upload, Quellenhygiene, Skill-Routing und Ausgabeformaten.
- Quellenanker für BGB §§ 305 bis 310 und UKlaG auf Gesetze im Internet ergänzt.
- Marketplace, Plugin-README, Skill-Gesamtübersicht, Asset-Index und Haupt-README auf `v53.4.0` synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, ZIP-Bau und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v53.3.0 — Bank-Rechtsabteilung Spezial-Boost ZAG, PSD, eWpG und Tokenisierung

Zweiter Ausbau des Plugins `bank-rechtsabteilung` von 50 auf 100 Skills. Schwerpunkt sind Spezialmaterien, die in einer Bank-Rechtsabteilung schnell schief werden können, wenn man sie nur als normales Bankrecht behandelt.

## Schwerpunkt

- 50 neue Spezial-Skills für Geschäftsleiterbestellung, Fit-and-Proper, Organwechsel, Schlüsselfunktionen, ZAG-Erlaubnis, Finanztransfergeschäft, ZAG-Negativauskunft, E-Geld, AIS/PIS, Agenten, ZAG-Ausnahmen, PSD2-SCA, Open-Banking-API, Fraud/Refund, PSD3/PSR-Vorschau, Instant Payments, IBAN-Name-Check, eWpG-Emission, Kryptowertpapierregister, Registerfehler, Tokenisierung, MiCAR-CASP, ART/EMT, Whitepaper, DLT Pilot Regime, Krypto-Custody, Stablecoins, DLT-Settlement, Travel Rule, Krypto-AML, APP-Fraud, SEPA/Card Disputes, Correspondent Banking, Trade Finance, Pfandbrief, Syndicated Loans, SLL, Bank-as-a-Service und Embedded Finance.
- `allgemein`-Skill auf 99 Anschluss-Skills erweitert, damit Kaltstart und stummer Upload weiterhin sauber routen.
- Quellenanker ergänzt: BaFin PSD2/ZAG, Personenanzeigen, Geschäftsleiter-Merkblatt, Kryptowertpapierregisterführung, eWpG, MiCAR, EU PSD3/PSR-Materialien.
- Marketplace, Plugin-README, Skill-Gesamtübersicht, Asset-Index und Haupt-README synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, ZIP-Bau und Release-ZIP-Validierung werden vor Tagging ausgeführt.

---

# v53.2.0 — Bank-Rechtsabteilung-Plugin

Neues Inhouse-Plugin `bank-rechtsabteilung` für die Rechtsabteilung einer mittelgroßen deutschen Bank.

## Schwerpunkt

- 50 neue Skills für Chefjustiziar-/Syndikus-Workflows: Aufsicht, KWG/MaRisk, DORA, GwG, Sanktionen, ZAG, WpHG/MiFID, AGB, Darlehen, Kreditentscheidung, Stundung, Sanierungsgutachten, Restrukturierung, Sicherheiten, Insolvenzanfechtung, Handelsvertreter, Provisionsmodelle, externe Anwälte, Rechnungsreview, Vorstand, Aufsichtsrat, HV, Fit-and-Proper, Datenschutz, Auskunftsersuchen, IT/Cloud, Produktfreigabe, ESG, Policy-Drafting, Litigation und Krise.
- Starker `allgemein`-Skill mit Kaltstart, stummem Upload, Fristencheck, Risikoampel und Anschluss-Skill-Routing.
- Amtliche Quellenanker in `bank-rechtsabteilung/references/QUELLEN.md` für KWG, ZAG, WpHG, GwG, HGB, BGB, AktG, BaFin, Bundesbank, EZB/SSM, EBA und EUR-Lex.
- Marketplace, Plugin-Übersicht, Skill-Gesamtübersicht, Plugin-READMEs und Asset-Index auf 117 Plugins und 6693 Skills synchronisiert.

## Checks

- YAML-Frontmatter, Plugin-Struktur, Gesamt-PDF-Regel, ZIP-Bau und Release-ZIP-Validierung werden vor dem Tagging erneut ausgeführt.

---

# v53.1.0 — Anthropic-Tiefe-Boost Batch A01 M&A-Kern

Erster produktiver Skill-Tiefe-Boost aus dem Branch `anthropic-patterns-experimente`, sauber auf den aktuellen `main`-Stand integriert. Der alte Experiment-Branch wurde nicht stumpf gemerged, damit der v53.0.0-Release-Stand erhalten bleibt.

## Schwerpunkt

- `grosskanzlei-corporate-ma`: 46 kurze/mittlere Skills auf mandatsbegleitende Tiefe gebracht.
- `mittelstand-corporate-ma`: 47 kurze/mittlere Skills auf Mittelstands-M&A-Tiefe gebracht.
- `corporate-kanzlei`: 38 kurze/mittlere Skills auf Corporate-/Inhouse-Governance-Tiefe gebracht.
- `anthropic-lessons/` mit Analyse, Selektionslogik und Boost-Instruktion in `main` übernommen.
- Matter-Workspace-Hinweise, Quellen-Tags, Hand-Offs, Negativ-Abgrenzungen und berufsrechtliche Hinweise in den geboosteten Skills ergänzt.

## Checks

- YAML-Frontmatter: 0 Fehler, 0 Warnungen.
- Plugin-Struktur: OK.
- Gesamt-PDF-Regel der Testakten: OK (128 Testakten).
- Release-ZIP-Validierung lokal: OK (116 Plugin-ZIPs).

---

# v53.0.0 — Neue Grundplugins, Commercial Courts, Patentrecht und Skill-Mindeststandard

Großer Integrationsrelease nach den parallelen Ergänzungen: neue Plugins für Bürokratieverstehen, Vereinsrecht und Parteienorganisation; Integration des Commercial-Courts-Plugins; Patentrecht international/prozessual erweitert; Perplexity-Skillpakete integriert; anschließend alle Plugins auf mindestens 50 Skills gebracht.

## Schwerpunkt

- 116 Plugins im Marketplace.
- 6643 Skills insgesamt; kein Plugin mehr unter 50 Skills.
- 1.713 ältere generische Spezial-Skills in konkrete Fachbausteine mit Kaltstart, Prüfmatrix, Risikoampel, Anschluss-Skills und Quellenregel umgebaut.
- Neue Sammel-/Einzeldownload-Übersichten, Skill-Index und Plugin-READMEs synchronisiert.
- 128 Testakten bleiben als ZIP und Gesamt-PDF verlinkt.
- Release-Workflow robuster gemacht: ZIP-Anhänge werden bei großen Releases gedrosselt hochgeladen, damit GitHubs Secondary Rate Limit nicht die Veröffentlichung abbricht.

## Checks

- YAML-Frontmatter: 0 Fehler, 0 Warnungen.
- Plugin-Struktur: OK.
- Gesamt-PDF-Regel der Testakten: OK (128 Testakten).
- Release-ZIP-Validierung lokal: OK (116 Plugin-ZIPs).

---

# v52.5.0 — Batch 1: 12 Plugins auf 20 Skills aufgestockt

189 neue, plugin-spezifische Skills in 12 Plugins, die bisher 10 oder weniger Skills hatten. Je Plugin etwa zur Haelfte einfuehrend/erweiternd, etwa zur Haelfte spezielle Fallskills.

## Aufgestockte Plugins (jeweils auf 20)
- aktenaufbereiter-strafrecht: 2 -> 20 (+18)
- anlagen-zu-schriftsaetzen: 2 -> 20 (+18)
- memorandums-ersteller: 2 -> 20 (+18)
- nda-abgleich: 2 -> 20 (+18)
- phishing-vorfall-pruefer: 2 -> 20 (+18)
- zitierweise-deutsches-recht: 2 -> 20 (+18)
- forderungsmanagement-klagewerkstatt: 4 -> 21 (+17)
- liquiditaetsplanung: 5 -> 20 (+15)
- einfache-leichte-sprache-jura: 6 -> 20 (+14)
- betreuungsrecht: 8 -> 20 (+12)
- immobilienrechtspraxis: 8 -> 20 (+12)
- verfassungsrecht: 9 -> 20 (+11)

## Zahlen
- 112 Plugins (unveraendert)
- 3092 Skills (+189)
- alle plugin.json + marketplace.json auf 52.5.0

## Validatoren
- validate-yaml-frontmatter: 0 Fehler, 0 Warnungen
- validate-plugin-structure: OK

---

# v52.4.0 — Vergaberecht-Vertiefung + IDW-S-6-Korrektur

Vertiefende Erweiterung des `fachanwalt-vergaberecht`-Plugins um 12 neue Spezial-Skills sowie inhaltliche Korrektur einer fehlerhaften Zuschreibung der IDW-S-6-Krisenstadien.

## fachanwalt-vergaberecht: 12 neue Skills (16 -> 28)

- `fachanwalt-vergaberecht-zuschlagskriterien-wertungsschema` — Wertungsmatrix nach § 127 GWB / § 58 VgV, Auftragsbezug, Lebenszykluskosten, Wertungsrüge.
- `fachanwalt-vergaberecht-olg-sofortige-beschwerde` — §§ 171-184 GWB, 2-Wochen-Frist, aufschiebende Wirkung § 173 GWB.
- `fachanwalt-vergaberecht-schadensersatz-181-gwb` — § 181 GWB + BGB-Vorvertragsrecht, Echte-Chance-Doktrin BGH X ZR 100/04.
- `fachanwalt-vergaberecht-sektorenvergabe-sektvo` — §§ 100-104 GWB + SektVO, Wasser/Energie/Verkehr/Post.
- `fachanwalt-vergaberecht-konzessionsvergabe-konzvgv` — Konzessionsbegriff Betriebsrisiko, KonzVgV-Verfahren.
- `fachanwalt-vergaberecht-inhouse-interkommunal` — § 108 GWB, Teckal-Doktrin, Hamburg-Stadtreinigung.
- `fachanwalt-vergaberecht-verhandlungsverfahren-dialog` — §§ 17-19 VgV, BAFO, Gleichbehandlung in Verhandlung.
- `fachanwalt-vergaberecht-freiberufliche-leistungen-hoai` — § 50 VgV, HOAI nach EuGH C-377/17, Planungswettbewerb RPW 2013.
- `fachanwalt-vergaberecht-losbildung-mittelstandsfoerderung` — § 97 Abs. 4 GWB, Fach- und Teillose, Eignungsleihe § 47 VgV.
- `fachanwalt-vergaberecht-vergabesperre-korruption-selbstreinigung` — §§ 123-126 GWB, § 125 Selbstreinigung, Wettbewerbsregister § 8 WRegG.
- `fachanwalt-vergaberecht-uvgo-unterschwellenvergabe` — UVgO Bund/Land, Primärrechtsschutz VG, Sekundärschutz LG.
- `fachanwalt-vergaberecht-vob-a-bauvergabe` — VOB-A Abschnitte 1+2, Leistungsbeschreibung § 7, Nebenangebote § 8.

## Inhaltliche Korrekturen

- **IDW S 6 Stadienlehre**: Die fünf/sechs Krisenstadien (Stakeholder-, Strategie-, Produkt-/Absatz-, Erfolgs-, Liquiditätskrise, Insolvenzreife) korrekt als IDW-S-6-eigene Stadienlehre (in Anlehnung an Müller 1986) zugeordnet, nicht mehr als "Hauschka-Krisenmodell" bezeichnet.
  - `steuerrecht-anwalt-und-berater/skills/stb-liquiditaetsvorschau-3-6-12-monate/references/idw-s6-kernelemente.md`
  - `testakten/beispielakte-edelholz-berlin/liquiditaetsplan_edelholz.md`

## Zahlen

- 112 Plugins (unverändert)
- 2903 Skills (vorher 2891)
- alle plugin.json + marketplace.json auf 52.4.0

---

# v52.3.0 — Außenwirtschaft, Sozialrecht-Laienhilfe und bessere Einstiege

Sammelrelease mit neuen und vertieften Skills fuer Aussenwirtschaft, Sozialrecht, juristische Sprachhilfe und juristische Arbeitsmethodik.

## Neue und erweiterte Skills

- `aussenwirtschaft-zoll-sanktionen` auf 100 Skills erweitert: Exportkontrolle, Embargos, Sanktionen, BAFA, Zoll/TARIC, CBAM, AWV, Screening, Audit-Trail und Ermittlungs-/Selbstkorrekturworkflows.
- `fachanwalt-sozialrecht` um 50 laienverstaendliche Skills erweitert: Bescheide, Widerspruch, Eilantrag, Pflegegrad, GdB, Krankenkasse, Buergergeld, EM-Rente, Gutachten, Fristen und Fehlervermeidung.
- Neues Plugin `juristische-sprache-deutsch-als-zweitsprache` mit 50 Skills fuer Juristendeutsch, Bescheide, Fristen, Formulare, Gerichtstermine, eigene Formulierungen und respektvolle Sprachhilfe.
- Bessere Einstiege in `arbeitsrecht` und `arbeitszeugnis-analyse`: neue Problem-sortieren-Skills fuer unsortierte Anfragen und Dokument-Uploads.
- Querschnittliche Arbeitsmethodik ergaenzt: KI-Arbeitsauftrag-Briefing, Entwurfscheck/Aktenabgleich/Red Team, prozessuale Argumentationsverbesserung und WEG-TOP-Generator.

## Release-Stand

- Marketplace und Plugin-Manifeste auf `v52.3.0` synchronisiert.
- `SKILLS.md`, `skills-index/`, Plugin-READMEs, Download-Bloecke und zentrale Uebersichten regeneriert.
- Stand: 112 Plugins, 2891 Skills, 128 Testakten.

## Checks

- YAML-Frontmatter validiert.
- Plugin-Struktur validiert.
- Gesamt-PDF-Regel der Testakten validiert.
- Whitespace-Diffcheck sauber.

# v52.2.2 — Skillset-Sanity und Kurzskill-Boost

Breiter Funktionscheck über alle 2.682 Skills mit Schwerpunkt Nutzbarkeit, Kaltstart, Geschwindigkeit und klare Ausgabe.

## Skill-Audit

- Alle 2.682 `SKILL.md` strukturell gescannt: Frontmatter, Mindestlänge, Output-Signale, Platzhalter-/Müllmarker und Extremwerte.
- Harte Validatoren erneut grün: YAML-Frontmatter und Plugin-Struktur.
- Sehr kurze Skills gezielt nachgeschärft statt pauschal aufgebläht.

## Boost

- 92 kurze Skills in `verlagsredaktion`, `gesellschaftsrecht-legal-english`, `meinungspruefer`, `nachbarschaftsstreit-pruefer`, `barrierefreiheit-web-checker`, `subsumtions-pruefer` und `weg-hausverwaltung` mit knappem Arbeitsmodus, Mindestinput, Qualitätsgate und Ausgabeformat ergänzt.
- Ergebnis: kein Skill mehr unter 1.200 Zeichen; Minimum jetzt ca. 1.210 Zeichen, Median unverändert schlank bei ca. 5.438 Zeichen.
- Fokus bleibt schnell: keine langen neuen Referenzblöcke, sondern kurze operative Leitplanken.

# v52.2.1 — Testakten-Download-Audit und README-Sync

Nachlauf auf den vollständigen Testaktenbestand mit Schwerpunkt Downloadfähigkeit in jedem Plugin-README.

## Download- und Aktenstandard

- Alle 127 Testakten erneut geprüft: jedes Akten-README enthält Gesamt-PDF und Akten-ZIP-Link.
- Alle Plugin-READMEs mit zugeordneten Akten zeigen jetzt im Sofort-Download-Block sowohl Plugin-ZIP als auch Gesamt-PDF und Akten-ZIP je Akte.
- Alias-Zuordnungen für ältere Sachgebietsbezeichnungen (`dsgvo`, `cisg-handelskauf`, `internationales-privatrecht`, `bauplanungsrecht`) in die README-Generatoren übernommen.
- DSA/DMA-Akte Bayrische Baustube Meißner mit eigenem README versehen und Gesamt-PDF synchronisiert.

## Qualitätskorrekturen

- Offene TBD-/TODO-artige Marker aus mehreren Aktenstücken entfernt und durch akteninterne Vermerke ersetzt.
- Sichtbare "Testakte"/"Beispielakte"-Präfixe aus individuellen Akten-README-H1 entfernt, damit Gesamt-PDF-Cover mandatsnäher wirken.
- Gesamt-PDFs der geänderten Akten neu gebaut.

## Checks

- 127 Gesamt-PDFs validiert.
- 511 PDFs / 11.327 Seiten lesbar, 173 XLSX, 320 DOCX und 210 Bilddateien technisch geprüft.
- 110 Plugin-ZIPs lokal gebaut und mit `validate-release-zips.py` validiert.

# v52.2.0 — Testakten-Nachlauf und Release-Glattzug

Nachlauf auf den von Perplexity/Claude eingebrachten Testakten-Vollbestand.

## Testakten

- 127 Testakten strukturell geprüft: Gesamt-PDF-Regel, EML-Header, PDF-Signaturen, leere Dateien und ZIP-Release-Erwartung.
- Sichtbare "Testakte"/"Demonstrationsakte"-Marker aus mehreren Aktenstücken entfernt und durch akteninterne Arbeitsvermerke ersetzt.
- Eingebettete Einzel-PDFs in der Bereicherungsakte und Strafsammelakte bereinigt; die jeweiligen Gesamt-PDFs wurden neu gebaut.
- Vogt-Befristungskontrollakte korrigiert: § 17-TzBfG-Frist wegen Samstag/§ 193 BGB bis 23.03.2026, nicht 20.03.2026.
- Rechtsberatungsstellen-, Eigenbedarfs-, Bereicherungs-, Strafsammel- und WEG/Hausverwaltungs-Akte redaktionell geglättet und Gesamt-PDFs synchronisiert.

## Übersichten und Plugin-Verweise

- `fachanwalt-medizinrecht` verweist nicht mehr auf das alte, nicht mehr existente Plugin `sozialrecht-kanzlei`, sondern auf `fachanwalt-sozialrecht`.
- Marketplace und 110 Plugin-Manifeste auf `52.2.0` synchronisiert.
- ASSET_INDEX, SKILLS.md und Skills-Index für 110 Plugins / 127 Testakten / 241 Release-Assets aktualisiert.

## Checks

- PDF-/EML-/Leerdaten-Schnellcheck: grün.
- Release-ZIP-Validierung: grün.
- Standard-Validatoren siehe Commit/Release-Protokoll.

# v52.1.0 — Sanity-Pass, Bug-Hunt und Versions-Glattzug

Vollstaendiger Repository-Sweep nach v52.0.0 — Validatoren, tote Links, Versions-Drift, CSV-Strukturdaten.

## Bug-Hunt-Ergebnisse

- **9 CSV-Dateien** mit unquotierten Kommas/Semikolons gefixt — alle 87 testakten-CSVs parsen jetzt konsistent (separater Hotfix-PR #166 vor diesem Release).
- **Tote interne Markdown-Links**: 0 — alle 130+ Aktenordner und 110 Plugin-READMEs sauber.
- **Verbotene Frontmatter-Keys** (triggers/when_to_use/language/...): 0.
- **Komma+Zahl-Pattern** in Plugin- und SKILL.md-Descriptions: 0.
- **Kaputte JSON**: 0.

## Versions-Glattzug

Vor diesem Release hatten die plugin.json-Dateien aller Plugins veraltete Versionsstaende (105 Plugins noch auf 50.0.0, 5 auf gemischten alten Staenden, marketplace.json auf 51.4.0). Jetzt:

- marketplace.json: 51.4.0 → **52.1.0**
- 110/110 plugin.json: **52.1.0** (alle vereinheitlicht)
- ASSET_INDEX.md, testakten/README.md, SKILLS.md, 110 skills-index/*.md: Stand v52.1.0
- README.md Release-Zeile auf v52.1.0

## Sofort-Download-Section

Alle 110 Plugin-READMEs haben weiterhin den `Sofort-Downloads`-Block direkt nach dem H1-Titel. Die Links zeigen auf `/releases/latest/download/` und werden mit dem v52.1.0-Release automatisch auf die neuen Assets aktualisiert.

## Validatoren (alle gruen)

- `validate-plugin-structure` OK
- `validate-yaml-frontmatter` 0 Fehler, 0 Warnungen
- `validate-testakten-gesamt-pdf` OK (127 Testakten)

## Counts unveraendert

- **110 Plugins** im Marketplace
- **127 Testakten** in `testakten/`
- **2682 Skills** in SKILLS.md

---

# v52.0.0 — Testakten-Veredelung, Praktiker-Tipps und Audit-Fixes

User-Wunsch: Zehn dünne Testakten zu echten Arbeitsakten ausbauen, in DFG- / Forschungszulage- / DBA-Skills die Tipps und Tricks der alten Hasen ergänzen und Codex-Findings reparieren.

## Testakten — massiv ausgebaut (10 Akten)

Aus 16-35 KB Gesamt-PDF wurden 76-383 KB. Jede Akte enthält jetzt zusätzlich 3-5 neue realistische Dokumente (Mandatsnotizen, Eilanträge, EML-Dateien mit Headern, CSV-/JSON-Anlagen, Aktenvermerke, Befangenheitsanträge, Compliance-Memos). Bestehende Stub-Dokumente wurden auf 60-130 Zeilen vertieft.

- `verlagsredaktion-morgenlage-fachverlag` (16 → 85 KB)
- `grunderwerbsteuer-sharedeal-closing-waldkrone` (19 → 107 KB, Closing Memo, Tax Indemnity Letter, Step Plan, BMF-Anwendungserlass)
- `grundsteuer-rosenwinkel-bescheidkette` (20 → 105 KB, Grundsteuer-A vs. -B Verwechslung, Einsprüche, Eigentümerbrief)
- `lobbyregister-buergerinitiative-waldmoor` (26 → 98 KB, Vorstandssitzung, Bundestags-Korrespondenz, Pressetext)
- `bgb-at-altfraenkische-werkstatt` (26 → 105 KB, Anfechtungserklärung, Werkstattmeister-Notizen, Eltern-Mail-Konflikt)
- `meinungspruefer-grenzfaelle-alltag` (28 → 87 KB, Anwalts-Mahnung, Polizei-Anzeige, Whistleblower-Statement)
- `lobbyregister-public-affairs-agentur-wasserstoff` (29 → 129 KB, BMWi-Briefing, Honorarrechnung mit Aufwandsstunden, Compliance-Memo)
- `sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger` (30 → 76 KB, Befangenheitsantrag, Gegen-Gutachten, Mandanten-Mail)
- `einfache-leichte-sprache-jura-mandantenbrief` (31 → 96 KB, zwei zusätzliche Mandantenbriefe mit Vergleichsdokumenten schwer→einfach→leicht, BITV-Hinweis)
- `ki-vo-konformitaetsbescheinigung-bewerberpilot` (35 → 83 KB, EU-Konformitätserklärung, DSFA, Bias-Audit-Bericht, Bewerber-Beschwerde)

Plus Gesamt-PDF-Regeneration für die geboosteten Akten und für `energierecht-stadtwerke-quartier` und `sozialrecht-rollstuhl-tannenberg`, in denen Audit-Fixes eingeflossen sind.

## Audit-Fixes

`testakten/AUDIT_v52.md` neu — Repository-weite Fehlersuche durch Background-Agent (Pattern-Grep plus Webverifikation).

- **A.1 (sicher falsch):** `energierecht-stadtwerke-quartier/04_vertraege/waermeliefervertrag_hafenbogen.md` zitierte BGH VIII ZR 263/22 mit Datum 06.03.2024. Korrekt verkündet am 27.09.2023 (verifiziert über dejure.org). Datum gefixt.
- **D (Plugin-Querverweis):** Vier Stellen verwiesen auf das nicht existierende Plugin `sozialrecht-kanzlei` — durch `fachanwalt-sozialrecht` ersetzt (in `testakten/README.md`, `sozialrecht-rollstuhl-tannenberg/README.md`, `Bildbeschreibung_Rollator_kaputt.md`, `Wohnungsskizze_Mandant_Beschreibung.md`).
- **C (Sprachfehler):** `sozialrecht-rollstuhl-tannenberg/01-olaf-rollstuhl/Eilantrag_SG_Kiel_25-08-2026.md` hatte "Antragsgegnerin stellt den Antrag" — auf "Antragsteller hat bei der Antragsgegnerin den Antrag gestellt" korrigiert.
- Verdachtsfälle mit "verifizieren"-Markern wurden belassen — die Akten weisen sich selbst als prüfungsbedürftig aus (z. B. WEG-Hohenzollernhof Anfechtungsrisiko-Matrix).

## DFG / Forschungszulage / DBA — Praktiker-Tipps und Trade-offs

Aus PR #160 in der vorigen Session (auf v51 zurückgemerged; hier in Kontext gehalten):

- DFG-Plugin: 10 Skills von 378 auf 1753 Zeilen geboostet — Karrierestand-Matching, Reviewer-Killersatz-Tabelle, Drei-Brillen-Red-Team, Stellungnahme bei Wiedereinreichung.
- Forschungszulage-Plugin: 11 Skills auf 131-167 Zeilen — BSFZ-Trigger, Q1-Antragsstrategie, Stundenaufzeichnungs-Struktur, AGVO-Kumulierung, Mehrjahresantrag.
- DBA-Skills im Steuer-Plugin: 56 Skills mit länderspezifischen BZSt-/Cerfa-/Modelo-/Form-Hinweisen, Trade-off-Tabellen, Berechnungsbeispielen, Pillar Two, Estonian Tax Model, USA-LoB, Russland-Suspendierung (PR #161 differenzierte 30.12.2023 → ab 01.01.2024 in voller Reichweite, Übergangszeitraum 08.08.2023–31.12.2023 separat).

## Versionen und Übersichten

- SKILLS.md Stand `v52.0.0`.
- README.md "Letzter Release" `v52.0.0`.
- Validator (`scripts/validate-plugin-structure.mjs`, `scripts/validate-testakten-gesamt-pdf.py`) durchgehend grün.
- Plugin-Versionen unverändert — diese Release-Linie ist eine Testakten-Veredelung, keine Skill-Reform.

# v51.4.0 — Sofort-Download-Box in jedem Plugin-README

User-Beschwerde: "beim Word-Plugin ist im README nicht direkt der Link zum Download des Plugins. Es soll bei jedem Plugin-README sofort das Plugin als ZIP-File und dann auch immer die Testakte als ZIP und als PDF herunterladbar sein." Bisher gab es zwar in jedem Plugin-README einen Plugin-ZIP-Link, beim Word-Plugin aber erst weit unten in der Installation-Sektion. Das ist jetzt fuer alle 110 Plugins einheitlich oben.

## Aenderungen

- Neues Skript `scripts/inject-plugin-sofort-download-section.py`: fuegt in jede `<plugin>/README.md` direkt nach dem H1 (ganz oben) eine `## ⬇️ Sofort-Downloads`-Sektion ein mit (a) Plugin-ZIP-Direktdownload, (b) je zugeordneter Testakte ein Gesamt-PDF-Link und ein Akten-ZIP-Link. Idempotent ueber HTML-Marker `plugin-sofort-download-section`. Akten-Zuordnung wird wie schon bei `inject-plugin-testakten-section.py` aus den Backtick-Referenzen in `testakten/<slug>/README.md` abgeleitet.
- Skript ausgefuehrt: 110 von 110 Plugin-READMEs aktualisiert. Plugin-ZIP-Link steht jetzt in **jedem** Plugin-README sofort sichtbar unter dem Titel, vor allem anderen Inhalt.
- `marketplace.json` Version `51.3.0` -> `51.4.0`.
- `SKILLS.md` und `skills-index/` regeneriert (Versionsstring v51.4.0; Skill-Zahl 2682/110 unveraendert).
- `README.md`: Release-Zeile auf `v51.4.0`.
- Validatoren gruen (Plugin-Struktur, YAML-Frontmatter, Gesamt-PDFs mit 127 Testakten).

# v51.3.0 — Repo-Glattzug nach v51.2.0

Konsistenz-Pass nach dem v51.2.0-Merge: zwei neue Plugins aus v51.0.0/v51.1.0 (`dfg-foerderantrag`, `forschungszulage-antragstellung`) waren noch nicht im Marketplace-Manifest und in der Skill-Gesamtuebersicht eingetragen. Veraltete Zaehlerstaende in `README.md`, `SKILLS.md` und `ASSET_INDEX.md` korrigiert.

## Aenderungen

- `.claude-plugin/marketplace.json`: `dfg-foerderantrag` und `forschungszulage-antragstellung` ergaenzt; alphabetisch sortiert; `version` `51.2.0` -> `51.3.0`. Marketplace listet jetzt **110 Plugins** (vorher 108).
- `SKILLS.md` regeneriert: **2682 Skills in 110 Plugins** (vorher 2661 in 108); veralteten Satz mit `63 Testakten` auf `127 Testakten` korrigiert.
- `skills-index/`: 110 Plugin-Detailseiten plus Index regeneriert.
- `README.md`: Kennzahlen-Tabelle aktualisiert (Testakten `63` -> `127`, Release `v51.1.0` -> `v51.3.0`).
- `ASSET_INDEX.md`: Stand-Zeile auf `v51.3.0` aktualisiert.
- Sanity-Check: kein `\d,\d` in `description` (plugin.json, marketplace.json, SKILL.md); alle Descriptions <=300 Zeichen in Plugin-Manifesten, <=1024 in SKILL.md.
- Validatoren gruen: `validate-plugin-structure.mjs`, `validate-yaml-frontmatter.py`, `validate-testakten-gesamt-pdf.py` (127 Testakten).

# v51.2.0 — Plugin-Testakten-Vollbestand (64 neue Testakten)

User-Wunsch: Wirklich alle Luecken im Testakten-Bestand schliessen. Pro bisher untestrierter Plugin-Familie eine vollstaendige, individualisierte Demoakte auf dem Qualitaetsniveau der `Rosengarten`-Vorbildakte (ca. 15-25 Aktenstuecke, Beteiligte mit Namen, Aktenzeichen, Konfliktstraenge, deutsche Normen). Pro Akte ein Commit, alles auf einem Branch.

## Aenderungen

- **64 neue Testakten** in 11 Wellen angelegt, je 38 Aktenstuecke (22 nummerierte MD plus 3 DOCX plus 2 XLSX plus 4 EML plus 2 PDF plus 3 JPG plus Gesamt-PDF) plus README. Quellen ausschliesslich aus dejure.org, openjur.de, bundesgerichtshof.de, bundesverfassungsgericht.de und amtlichen Behoerden-URLs; keine BeckRS-Modellzitate, kein anwalt24.de.
- **Testakten-Bestand 63 -> 127** (siehe `testakten/README.md`).
- **ASSET_INDEX.md** aktualisiert: 108 Plugin-ZIPs plus 127 Fallakten-ZIPs plus 4 Standalone-Assets = **239 Release-Assets** fuer `v51.2.0` und `latest`.
- Welle-Themen: Welle 1-7 (Arbeitsrecht, Familie, Erbe, Insolvenz, Bau, IT-Recht, Strafrecht); Welle 8 (KI-Governance, KI-VO, Mandantenanfragen, MundA, Methodenlehre, Mietrecht); Welle 9 (Share-Deal, NDA, Normenkontrolle, FTO-Recherche, Produkthaftung, Zivilprozess BGH-Revision); Welle 10 (Rechtsberatungsstelle, BaFin-Regulatorik, Steuerrecht/Selbstanzeige, Strafzumessung, Subsumtions-Pruefer, Tabellenreview); Welle 11 (Richter-Urteilsbau, Verfassungsrecht, VerkehrsOWi, Drafting-Werkstatt, Zitierweise, Zwangsvollstreckung).
- **Validatoren gruen:** `validate-plugin-structure.mjs`, `validate-yaml-frontmatter.py`, `validate-testakten-gesamt-pdf.py` (127 Testakten).
- **Plugin-READMEs:** `inject-plugin-testakten-section.py` automatisiert die Demonstrationsakten-Tabelle in jedem Plugin-README; 75 Plugins haben jetzt eine eigene Demonstrationsakte.
- **Gesamt-PDFs:** Pro Akte ein automatisch gebautes Gesamt-PDF (Skript `build-testakte-gesamt-pdf.py`, breite Tabellen >12 Spalten fallen sequentiell zurueck), oben im Akten-README verlinkt.
- Pattern fuer Testakten festgehalten: kein YAML-Frontmatter; 38 Dateien plus README; Plot mit 5-8 individualisierten Konfliktstraengen; konsistente Beteiligten- und Aktenzeichen-Liste; ASCII in Commit-Messages und in `description` (Dezimalkommas nur im Body, nicht in der Description).
- Marketplace-Version `51.1.0` -> `51.2.0`; Generator regeneriert SKILLS.md und skills-index/; Plugins/Skills unveraendert (110/2682).

# v51.1.0 — DFG/Forschungszulage Workflow-Boost

Nachlauf zu den neuen Förderplugins: Claude-Code-Ausbau übernommen und mit einem weiteren Codex-Audit veredelt.

## DFG-Förderantrag

- `allgemein` arbeitet jetzt adaptiv: geführter Modus für Erstantragsteller, Normalmodus, Profi-Red-Team und Rettungsmodus nach Ablehnung.
- DFG-Kaltstart erzeugt auch aus losen Ideen eine Mini-Roadmap mit Minimalprojekt, Idealprojekt, Lückenliste und 10-Arbeitstage-Plan.
- Koselleck-Logik korrigiert: mehrere abgeschlossene DFG-Projekte sind starkes Praxisindiz, aber kein behauptetes starres formales Muss.
- Strategie-Skill ergänzt einen Entscheidungsmotor: minimal förderfähig, optimal wissenschaftlich, Prestige/Vision.

## Forschungszulage

- `allgemein` unterscheidet jetzt Einsteiger, Technikteam, CFO/Steuerberatung, Krisenmodus und Ablehnung/Nachforderung.
- BSFZ-Projektbeschreibung auf Portalrealität umgestellt: interne Langfassung plus Portaltexte mit Zeichenbudgets nach BSFZ-Leitfaden 2026.
- Fördercheck behandelt kleine Vorhaben nicht mehr pauschal als unwirtschaftlich; er baut bei Bedarf schlanke Anträge.
- Bemessungsgrundlagen-Skill präzisiert § 2 Abs. 5 FZulG bei Auftragsforschung und ergänzt eine Datenqualitäts-Ampel.

# v51.0.0 — DFG, Forschungszulage und weltweite DBA-Matrix

User-Wunsch: Zwei neue Förderplugins für DFG-Anträge und Forschungszulage sowie ein deutlich tieferer Ausbau der DBA-Skills im Steuerrechtsplugin.

## Neue Plugins

- `dfg-foerderantrag`: DFG-Sachbeihilfe, elan-Formalia, kleine schnelle Anträge bis zur 200.000-Euro-Begutachtungsmarke, Koselleck-Route ab 500.000 Euro, Finanzplan, Reviewer-Red-Team, KI/Ethik/Forschungsdaten und Wiedereinreichung.
- `forschungszulage-antragstellung`: BSFZ-Bescheinigung, FuE-Abgrenzung, Bemessungsgrundlage 2026, Finanzamt-Festsetzung, Auszahlung, Verlust-/Insolvenzlagen, Dokumentationspaket, Kumulierung und Einspruch/Nachbesserung.

## Steuerrecht / DBA

- Neue `references/dba-laendermatrix-2026.md` nach BMF-Stand 01.01.2026 als weltweite Routing-Matrix.
- Neue DBA-Skills: Ländermatrix, Nicht-EU-Regionenrouter, Edge-Case-Playbook, MAP/EU-Streitbeilegung, Quellensteuer-Atlas und All-Country-Memo-Generator.
- `rechtsstand-mai-2026-faktenbank` ergänzt um den DBA-Stand 2026 und neue DBA-Folgeskills.

## Versionen und Übersichten

- Marketplace-Version `50.10.0` → `51.0.0`.
- Plugins: 108 → 110.
- Skills: 2655 → 2682.
- Release-Assets erwartet: 177 = 110 Plugin-ZIPs, 63 Testakten-ZIPs, `marketplace.json` und 3 Sammelarchive.
- `SKILLS.md`, `skills-index/`, Plugin-READMEs, `README.md` und `ASSET_INDEX.md` synchronisiert.

# v50.10.0 — Akten-ZIP-Download in jedem Testakten-README

User-Wunsch: In jedem Testakten-README muss ganz oben sowohl ein Link zum Gesamt-PDF als auch ein Link zur Akten-ZIP mit allen Einzeldateien stehen. Bisher gab es nur das Gesamt-PDF.

## Änderungen

- `scripts/inject-gesamt-pdf-section.py`: Die autogen-Sektion ganz oben in jeder Testakten-README heißt jetzt "Akte komplett herunterladen" und enthält **zwei** Zeilen: Gesamt-PDF (lokaler Repo-Link auf `gesamt-pdf/<slug>_gesamt.pdf`) und Akten-ZIP (stabile URL auf `releases/latest/download/testakte-<slug>.zip`). Idempotent über bestehende HTML-Marker.
- Alle 63 Testakten-READMEs neu generiert; jede hat jetzt beide Download-Links prominent oben.
- CI-Workflow `.github/workflows/release-plugin-zips.yml` baut die `testakte-<slug>.zip` schon seit dem ersten Release. Diese ZIP-URLs werden ab v50.10.0 nun auch in den READMEs angezeigt.
- Marketplace 50.9.1 → 50.10.0; Generator läuft, SKILLS.md und `skills-index/` zeigen `Stand v50.10.0`.

# v50.9.1 — Download-Link im Word-Plugin-README

User-Hinweis: Das Plugin-README von `word-legal-ai-plugin-and-skill-for-german-lawyers` hatte als einziges der 108 Plugins keinen ZIP-Direkt-Download-Link auf die Release-Asset-URL. Beim Rename in v50.7.0 ist die Installation-Section verloren gegangen.

## Änderungen

- `word-legal-ai-plugin-and-skill-for-german-lawyers/README.md`: Neue Section "Installation" mit Direkt-Download-Tabelle und Drei-Schritt-Anleitung ergänzt — analog zu allen anderen 107 Plugin-READMEs. Link: `releases/latest/download/word-legal-ai-plugin-and-skill-for-german-lawyers.zip`.
- Prüfung quer durchs Repo: Alle 108 Plugin-READMEs zeigen jetzt korrekt auf ihre eigene Release-ZIP (`releases/latest/download/<plugin>.zip`).
- Marketplace 50.9.0 → 50.9.1; Generator läuft, SKILLS.md und `skills-index/` zeigen `Stand v50.9.1`.

# v50.9.0 — Sanity-Check, ASSET_INDEX-Sortierung und Plugin-Übersicht im README

Nachlauf zu v50.8.0/8.1: User-Sanity-Check des Codex-Ausbaus und zwei Übersichts-Fixes.

## Änderungen

- Sanity-Check der zwölf neuen/umbenannten Skills von v50.8.0/8.1: alle Frontmatter konform zu den Hausregeln (keine verbotenen Felder, ASCII-Namen ≤ 64, Description ≤ 1024, kein `\d,\d`-Muster). Validatoren `validate-plugin-structure.mjs`, `validate-yaml-frontmatter.py` und `welle5_komma_check.py` alle grün.
- ASSET_INDEX.md: `word-legal-ai-plugin-and-skill-for-german-lawyers` aus der falschen Position zwischen `jurastudium` und `jveg-kostenpruefer` verschoben. Steht jetzt korrekt unter W, zwischen `wandeldarlehen-lebenszyklus` und `zitierweise-deutsches-recht`.
- README.md: Plugin-Tabelle im Abschnitt "Was ist drin?" um `word-legal-ai-plugin-and-skill-for-german-lawyers` ergänzt (bisher 107 von 108 Plugins in der Tabelle, jetzt vollständig). Neue Cluster-Zeile "Drafting & Word" im Abschnitt "Querschnittliche Werkzeuge".
- Marketplace 50.8.1 → 50.9.0; Generator läuft sauber durch, SKILLS.md und `skills-index/` zeigen `Stand v50.9.0`. Plugin- und Skill-Zahlen unverändert (108 / 2655).

# v50.8.1 — Word Legal AI ohne Makro-/VBA-Ballast

User-Wunsch: Im Word-Writing-Plugin sollen Skills raus, die nach Makros, Office-Automatisierung oder unnötigem Word-Technikkram aussehen.

## Änderung

- Skill `word-formatvorlagen-querverweise-track-changes` entfernt.
- Skill `dokumentstruktur-makroebene-vertrag-und-schriftsatz` in `dokumentarchitektur-vertrag-und-schriftsatz` umbenannt, damit "Makroebene" nicht wie Word-Makros/VBA missverstanden wird.
- Word-Plugin jetzt 38 statt 39 Skills; Gesamtbestand 2655 statt 2656 Skills.
- README und Skill-Routing klargestellt: kein Makro-, VBA- oder Word-Automatisierungs-Skill.
- `verweis-und-querverweis-technik` bleibt als juristischer Verweislogik-Skill erhalten, aber ohne Verweis auf den gelöschten Word-Technik-Skill.
- `word-dokument-finish-und-layout` bleibt als schlanke Versand- und Finish-Kontrolle erhalten.

# v50.8.0 — Word Legal AI: Kaltstart, Kanzleistil, Word-Finish und US/UK-Drafting

Nachlauf zum umbenannten Word-Plugin: Der neue Slug `word-legal-ai-plugin-and-skill-for-german-lawyers` bleibt bestehen, das Plugin wurde aber vom reinen Drafting-Baukasten zu einem geführten Schreibworkflow für deutsche Anwältinnen und Anwälte ausgebaut.

## Workflow

- Neuer Kaltstart mit `kaltstart-drafting-kommandocenter`: maximal fünf Fragen, Mandatsmatrix, Stilprofil und konkrete Skill-Kette statt leerem Start.
- `orientierung-drafting-triage` erweitert: routet jetzt ausdrücklich nach Dokumenttyp, Stadium, Adressat, Kanzleistil, Sprachraum und Risiko.
- Neuer Kanzleistil-Check mit `deutscher-kanzleistil-kalibrieren`: Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht/Behörde und US/UK-Korrespondenz.

## Neue Skills

- `word-dokument-finish-und-layout` für Formatvorlagen, Nummerierung, Querverweise, Track Changes, Metadaten, PDF/beA und Versandfassung.
- `partner-kommentar-umsetzen` für knappe Partnernotizen und Randkommentare.
- `mandantenmemo-und-partner-update` für Executive Summary, Empfehlung, Risikoampel und nächste Schritte.
- `argumentationsarchitektur-schreiben` für These, Norm, Tatsache, Beleg, Gegenargument und Rechtsfolge.
- `schriftsatz-ueberarbeiten-richterlesbar` für Anträge, Ergebnisüberschriften, Beweisangebote, Anlagenverweise und Ton.
- `us-uk-legal-writing-fuer-deutsche` für englische/amerikanische Legal-Texte aus deutscher Anwaltsperspektive.
- `englischer-vertrag-deutsches-recht` für englischsprachige Verträge mit deutschem Recht ohne versehentlichen Common-Law-Import.
- `finaler-writing-quality-gate` als letzte Freigabeampel vor Versand.

## Übersichten und Versionen

- Plugin-Version `50.7.0` → `50.8.0`.
- Marketplace-Version `50.7.0` → `50.8.0`.
- Word-Plugin: 29 → 39 Skills.
- Gesamtbestand: 2646 → 2656 Skills.
- `SKILLS.md`, `skills-index/`, Plugin-README, `README.md`, `ASSET_INDEX.md` und Testakten-README synchronisiert.

# v50.7.0 — Plugin-Rename: `juristisches-drafting` → `word-legal-ai-plugin-and-skill-for-german-lawyers`

User-Wunsch: Der Plugin-Name soll explizit klarmachen, dass es um Word, Legal AI und deutsche Juristen geht — auch in der Betreffzeile und im Link. Der Anzeigename lautet jetzt "Word Legal AI Plugin and Skill for German Lawyers".

## Rename

- Plugin-Ordner umbenannt: `juristisches-drafting/` → `word-legal-ai-plugin-and-skill-for-german-lawyers/`.
- `plugin.json` name-Feld umgestellt; description führt jetzt mit "Word Legal AI Plugin and Skill for German Lawyers".
- `marketplace.json`: Plugin-name, source-Pfad und Beschreibung aktualisiert.
- Plugin-`README.md`: Titel `Word Legal AI Plugin and Skill for German Lawyers`; Hinweis auf den früheren Slug bleibt erhalten.
- `orientierung-drafting-triage`: Selbstreferenz auf den neuen Slug umgestellt.
- `ASSET_INDEX.md`: Stand und Tabellenzeile aktualisiert.
- Neue Keywords: `word-legal-ai`, `legal-ai-word`, `word-plugin-jura`, `german-lawyers`. Der alte Slug `juristisches-drafting` bleibt als Keyword erhalten für Aufwärtskompatibilität der Suche.

## Achtung

Die permanente Regel "Plugin-Renames verboten" wurde für diesen Fall ausdrücklich vom User überschrieben. Künftige Renames brauchen weiterhin eine explizite Freigabe.

Auswirkungen für Nutzer:

- Wer das Plugin aus dem Marketplace neu zieht, erhält den neuen Slug; keine Aktion nötig.
- Wer das Plugin lokal entpackt hat: Ordner wird mit dem neuen Namen geliefert (`word-legal-ai-plugin-and-skill-for-german-lawyers.zip` im Release).
- Skill-Namen sind unverändert (z. B. `definitionen-klauseln-stringent`, `klausel-bibliothek-katalog`).

## Versionen

- Marketplace-Version `50.6.1` → `50.7.0`.
- Plugin-Version `50.6.0` → `50.7.0`.
- Skills-Zahl bleibt 2646.

# v50.6.1 — Schmalfeld-Betreuungsakte vertieft

Nachlauf zum Testakten-Qualitätssprung: Die Schmalfeld-Akte zur Vermögenssorge/Kontodaten-/Vertragsverdachtsprüfung wurde deutlich lebensnäher ausgebaut und auf den bereits veröffentlichten `v50.6.0`-Stand mit dem erweiterten `juristisches-drafting`-Plugin rebased.

## Änderungen

- `testakten/betreuung-schmalfeld-kontodaten-vertraege/` erweitert:
  - neue Aktenstücke zu Bankrückfrage, Saldenabgleich, Onlinebanking/pushTAN, Telefonakquise, Haustürkontakten, Gedächtnisprotokollen und nachgereichter Vertragsmappe,
  - neue EML-Korrespondenz von Bank, Umfeld und Angehörigen,
  - neue JPEG-Fragmente zu TAN-Umschlag und Seniorenveranstaltung,
  - neue PDF-Vertragsmappe und Excel-Prüfmatrix für Fristen, Beleglücken, Vertragstypen und Maßnahmen.
- Schmalfeld-README und Aktenübersicht ent-demoisiert: stärker Arbeitsakte statt Lehrfall, keine pauschale Betrugslogik, bessere Trennung zwischen echter Lebensführung, belegbedürftiger Hilfe, technischen Risiken und wirtschaftlich auffälligen Verträgen.
- Gesamt-PDF der Schmalfeld-Akte neu erzeugt: 177 Seiten, 19 Quelldateien, inklusive neuer EML-/XLSX-/PDF-/JPEG-Anlagen.
- Übersichten synchronisiert:
  - Marketplace top-level `50.6.0` → `50.6.1`,
  - `SKILLS.md` und `skills-index/` neu generiert,
  - `juristisches-drafting/README.md` Skill-Überblick auf den neuen 29-Skill-Bestand aktualisiert.

Validatoren: `validate-plugin-structure`, `validate-testakten-gesamt-pdf`, `validate-yaml-frontmatter`, Release-ZIP-Trockenlauf, ZIP-Probe und `git diff --check`.

---

# v50.6.0 — `juristisches-drafting` genialer: Defensive Drafting, Term Sheet, Bilingual, Klauselbibliothek

User-Wunsch: Das Plugin `juristisches-drafting` ist solide, aber spartanisch. Es soll genialer werden für Juristinnen und Juristen, die in Word schreiben. Vier zentrale Lücken wurden geschlossen: fehlende fertige Klauselbausteine, keine defensive Verteidigungs-Heuristik bei Gegenseitenentwürfen, kein Term-Sheet-zu-Vertrag-Workflow und keine bilinguale Drafting-Anleitung.

## Vier neue Skills im Plugin `juristisches-drafting`

- **`defensive-drafting-fallen-erkennen`** — Zwölf typische Fallen in Gegenseitenentwürfen mit Roten-Flaggen-Wortlisten und Verteidigungsformulierungen (von einseitigen Haftungsbegrenzungen über kaschierte Vertragsstrafen bis zu versteckten Optionsrechten).
- **`term-sheet-zu-vertrag-uebersetzung`** — Mapping-Tabelle Term-Sheet-Position → Vertragsklausel, zwölf typische Term-Sheet-Lücken (Steuern, IP, Indemnities, Closing Conditions, MAC-Klauseln), Mandantenmemo-Vorlage mit offenen Punkten.
- **`bilingual-drafting-deutsch-englisch`** — Drei Use Cases (zwei Sprachfassungen, Glossar-Anhang, parallele Spalten), False-Friends-Tabelle DE-EN mit 25 Einträgen (z. B. `Schuldner ≠ schuldner`, `Erfüllungsort ≠ place of performance`, `Schadensersatz ≠ damages`), Maßgeblichkeits-Klausel.
- **`klausel-bibliothek-katalog`** — Bedienungsanleitung für die Klauselbibliothek mit über 60 Bausteinen. Jeder Baustein hat B2B/B2C-Ampel, AGB-Risiko (grün/gelb/rot), mild/scharf-Variante und englische Fassung.

## Asset

- **`juristisches-drafting/references/klausel-bibliothek.md`** — Klauselbibliothek mit über 60 Bausteinen in 25 Bereichen (Präambel, Definitionen, Leistung, Vergütung, Verzug, Aufrechnung, Gewährleistung, Haftung, Vertragsstrafe, Kündigung, Force Majeure, Geheimhaltung, Datenschutz, IP, Änderungsrechte, Sprache, Schriftform, Salvatorisch, Gerichtsstand, Schiedsklausel, Whole Agreement, Abtretung, Compliance, Subunternehmer, Audit-Recht).

## Weitere Änderungen

- `orientierung-drafting-triage`: Triage-Tabelle um vier neue Zeilen erweitert (Gegenseitenentwurf, Term Sheet, bilinguale Verträge, Klauselbedarf).
- `juristisches-drafting/README.md`: Blockstruktur erweitert um **Block G – Verhandlung und Klauselbibliothek**; Asset-Datei dokumentiert.
- `juristisches-drafting/.claude-plugin/plugin.json`: Description und Keywords um Defensive Drafting, Term Sheet, Bilingual und Klauselbibliothek ergänzt.
- Marketplace-Version `50.5.2` → `50.6.0`.
- Plugin-Version `juristisches-drafting` `50.0.0` → `50.6.0`.
- Automatische Regeneration von `SKILLS.md` und `skills-index/juristisches-drafting.md` über `scripts/generate-skills-md.py`.
- Enthält die zuvor unveröffentlichten Änderungen aus v50.5.2 (Regeneration der Übersichten für das initial in v50.5.x hinzugefügte Plugin).

# v50.5.2 — Skill-Übersichten für `juristisches-drafting` regeneriert

Bugfix für ein Codex-P2-Finding zu v50.5.x: Das neue Plugin `juristisches-drafting` war zwar in der `marketplace.json` eingetragen, tauchte aber weder in `SKILLS.md` noch in `ASSET_INDEX.md` noch in `README.md` auf. Im ZIP-Download des Komplettpakets fehlten dadurch alle 25 neuen Skills aus der Übersicht.

## Änderungen

- `scripts/generate-skills-md.py` neu gelaufen: `SKILLS.md` zählt jetzt 2642 Skills in 108 Plugins (vorher 2617/107) und enthält eine eigene Detailseite `skills-index/juristisches-drafting.md`.
- `ASSET_INDEX.md`: Plugin-Tabelle um `juristisches-drafting` ergänzt; Plugin-Zähler 107 → 108, Gesamtsumme 174 → 175.
- `README.md`: Stats-Tabelle aktualisiert (Plugins 107 → 108, Skills 2617 → 2642, letzter Release `v50.5.2`).
- Marketplace-Version `50.5.1` → `50.5.2`.

# v50.5.1 — Komplettpaket-ZIP enthält jetzt `skills-index/`

Bugfix für ein Codex-P2-Finding zu v50.4.0: Die `alles-komplettpaket.zip` aus dem Release-Workflow enthielt zwar die schlanke `SKILLS.md`, aber nicht den Ordner `skills-index/` mit den Detailseiten. Dadurch zeigten alle Plugin-Links der Übersichtstabelle im Offline-ZIP ins Leere.

## Änderungen

- `.github/workflows/release-plugin-zips.yml`: Beim Bauen von `alles-komplettpaket.zip` wird `skills-index/` mit nach `uebersichten/skills-index/` kopiert, damit die relativen Links der `SKILLS.md` im ZIP auflösen.
- Marketplace-Version `50.5.0` → `50.5.1`.

# v50.5.0 — Testakten-Qualitätssprung und Gesamt-PDF-Regel

User-Wunsch: Die Testakten sollen sich wie echte, disparat gewachsene Mandatsakten anfühlen und zugleich jeweils als ein sauberes Gesamt-PDF bereitstehen. Besonders die Rosengarten-Nachbarschaftsakte sollte nach Perplexitys Ausbau nochmals dichter, realistischer und technisch sauberer werden.

## Änderungen

- Rosengarten-Akte `testakten/nachbarschaftsstreit-horrorfall-rosengarten/` weiter ausgebaut:
  - neue Aktenstücke `15_starkregen_dachrinne_kellerfeuchte.md`, `16_notweg_hammerschlag_handwerkertermin.md`, `17_kamera_licht_drohne_datenschutz.md`, `18_ortstermin_konfliktmatrix.md`,
  - zwei neue `.eml`-Mails zu Starkregen/Kellerfeuchte und Kamera/Licht/Drohne,
  - vier neue JPEG-Anlagen (Dachrinne/Starkregen, Risslineal, Kamera/Lichtstrahler, Chat-Screenshot),
  - neue PDF-Anlagen zur Versicherung und zur Fotoanlage,
  - neue Excel-Konfliktmatrix mit Beweisproblemen, Fristsachen und Risikoeinschätzung.
- Doppelte Rosengarten-Gesamt-PDF entfernt; maßgeblich ist jetzt nur `gesamt-pdf/nachbarschaftsstreit-horrorfall-rosengarten_gesamt.pdf`.
- `scripts/build-testakte-gesamt-pdf.py` verbessert:
  - Gesamt-PDFs heißen im Dokument jetzt "Arbeitsakte" statt "Testakte",
  - Metadaten/Footer vermeiden Demo-Sprache,
  - JPEG/PNG-Bildanlagen werden in Gesamt-PDFs eingebunden,
  - alle 63 Gesamt-PDFs neu erzeugt.
- `scripts/inject-gesamt-pdf-section.py` glättet den Auto-Block in allen Akten-READMEs: "Arbeitsakte", Umlaute, Größe, keine doppelte Demo-Sprache.
- Neues `scripts/validate-testakten-gesamt-pdf.py`: prüft je Akte auf vorhandenes `gesamt-pdf/<slug>_gesamt.pdf`, PDF-Signatur, EOF-Marker, Seitenobjekte, README-/00-Aktenübersicht-Link und doppelte Gesamt-PDFs.
- Release-Workflow validiert Gesamt-PDFs vor dem ZIP-Build.
- Neuer Standard `testakten/QUALITAETSSTANDARD.md`: jede Akte hat künftig zwei parallele Zugänge, nämlich Originalformate als gewachsener Datenraum plus ein sauberes Gesamt-PDF.
- Mehrere Akten-READMEs und Aktenübersichten von Test-/Demo-Formulierungen bereinigt, damit die Unterlagen stärker aus ihrer eigenen Aktenlogik sprechen.
- Integriert auf den bereits veröffentlichten v50.4.0-Stand mit aufgeteilter `SKILLS.md` und `skills-index/`.

## Versionen

- Marketplace top-level 50.4.0 -> 50.5.0
- Plugin-Versionen unverändert (nur Testakten, Generatoren, Validatoren und Übersichten)

Validatoren grün: validate-plugin-structure OK, validate-testakten-gesamt-pdf 63/63 OK, validate-yaml-frontmatter 0/0, Release-ZIP-Probe OK, git diff --check OK.

---

# v50.4.0 — SKILLS.md aufgeteilt + Mega-ZIP-Download prominent oben

User-Meldung: Die SKILLS.md liess sich auf github.com kaum oeffnen, weil sie 2 MB gross war und 2617 Tabellenzeilen enthielt -- GitHubs Markdown-Renderer hat die Seite endlos neu geladen oder gar nicht angezeigt. GitHubs offizielles Renderer-Limit liegt bei ca. 512 KB.

## Aenderungen

- **SKILLS.md aufgeteilt:** Die Hauptseite ist jetzt nur noch ca. 27 KB gross und enthaelt lediglich den Hinweisblock, die Download-Buttons und die Plugin-Schnellzugriffstabelle. Pro Plugin gibt es eine eigene Detailseite unter `skills-index/<plugin>.md` mit der vollstaendigen Skill-Tabelle und allen Download-Links. Auch die groesste Detailseite (`steuerrecht-anwalt-und-berater.md`, 161 KB) bleibt deutlich unter GitHubs Renderer-Limit.
- **Mega-ZIP-Download prominent oben:** Direkt unter dem Titel von SKILLS.md gibt es jetzt einen Block `## ⬇️ Alle Skills auf einmal herunterladen` mit zwei Optionen:
  - `alle-plugins-megazip.zip` (~11 MB): nur die {n} Plugin-Skills
  - `alles-komplettpaket.zip` (~80 MB): Plugins + Testakten + Uebersichten
  Beide ZIPs existieren bereits als Release-Assets (gebaut von `.github/workflows/release-plugin-zips.yml`).
- **Index-Seite:** `skills-index/README.md` listet alle 107 Detailseiten als Sitemap.
- **Generator-Skript erweitert:** `scripts/generate-skills-md.py` schreibt jetzt SKILLS.md + 107 Detailseiten + Index in einem Lauf. Loescht veraltete Detailseiten beim Lauf (idempotent).

## Versionen

- Marketplace top-level 50.3.0 -> 50.4.0
- Plugin-Versionen unveraendert.

Validatoren gruen.

---

# v50.3.0 — SKILLS.md vollautomatisch generieren mit Download-Links

User-Wunsch: Die Skill-Gesamtuebersicht (`SKILLS.md`) soll oben prominent erklaeren, dass die Skills nichts weiter als grosse Markdown-Prompts sind und in jedem Chatbot per Copy-Paste funktionieren. Pro Skill ein Direkt-Download (Markdown + Raw), pro Plugin ein ZIP-Download-Button. Garantie: jeder neue Skill landet automatisch in der Uebersicht.

## Aenderungen

- Neues Skript `scripts/generate-skills-md.py`: liest Plugin-Reihenfolge aus `marketplace.json`, scannt alle `<plugin>/skills/<skill>/SKILL.md`, liest die `description` aus dem YAML-Frontmatter und schreibt `SKILLS.md` neu. **Idempotent und vollstaendig** -- jeder neu angelegte Skill taucht beim naechsten Lauf automatisch auf.
- `SKILLS.md` hat jetzt oben einen Hinweisblock **"Worum es hier geht: alles nur grosse Prompts"** mit Schritt-fuer-Schritt-Anleitung fuer Nutzerinnen von ChatGPT, Mistral, Gemini, DeepSeek, Le Chat usw.
- Pro Plugin: Link auf die Plugin-README und ein **ZIP-Download-Link** auf das Release-Asset (`releases/latest/download/<plugin>.zip`, vorhandenes Artefakt aus `release-plugin-zips.yml`).
- Pro Skill: Spalte **Download** mit `[Markdown]`-Link (github.com/blob/main) und `[Raw .md]`-Link (raw.githubusercontent.com), beide direkt klickbar im Browser.
- Stand: 2617 Skills in 107 Plugins, jetzt vollstaendig in SKILLS.md verlinkt.

## Versionen

- Marketplace top-level 50.2.0 -> 50.3.0
- Plugin-Versionen unveraendert.

Validatoren gruen.

---

# v50.2.0 — Gesamt-PDF fuer jede Testakte (doppelt gemoppelt)

User-Wunsch: Jede Testakte soll im ZIP-Release zusaetzlich ein einziges, durchsuchbares Gesamt-PDF mit allen Aktenstuecken enthalten. So liegt jede Akte sowohl in Einzelformaten (MD, DOCX, XLSX, EML, PDF) als auch in einer 'doppelt gemoppelten' Druckfassung vor.

## Aenderungen

- Neues Skript `scripts/build-testakte-gesamt-pdf.py` buendelt MD, TXT, EML, CSV, XLSX, DOCX und PDF einer Testakte zu einem PDF mit:
  - Cover (H1-Titel, Slug, Auszug aus Sachverhalt/Kurzbild/Worum/Zweck/Szenario/Idee/Mandant/Verfahrenseckdaten/...),
  - Inhaltsverzeichnis,
  - Seitenzahlen,
  - Trennblaettern fuer Original-PDF-Anhaenge (Layout per pypdf erhalten).
  Sehr lange Tabellenzellen (>1.200 Zeichen, z.B. bilingualer Wandeldarlehensvertrag) werden in eine sequentielle Absatzdarstellung umgewandelt, damit ReportLab nicht ueberlauft.
- Neues Skript `scripts/inject-gesamt-pdf-section.py` ergaenzt jede Testakte-README idempotent (HTML-Marker) um einen Block `## 📕 Gesamt-PDF (alles in einer Datei)` direkt unter dem H1 (also noch vor dem Direkt-Download).
- 63 von 63 Testakten haben jetzt `testakten/<name>/gesamt-pdf/<name>_gesamt.pdf`. Die Datei landet automatisch im Release-ZIP `testakte-<name>.zip` (siehe `.github/workflows/release-plugin-zips.yml`).
- Stichproben-Sichtung des Repos: keine TODO/FIXME-Marker, keine Lorem-Ipsum-Reste, keine leeren Quelldateien. Inhalte sind durchweg konsistent.

## Versionen

- Marketplace top-level 50.1.1 -> 50.2.0
- Plugin-Versionen unveraendert (nur Testakten-Inhalte und Hilfsskripte aendern sich; keine Plugin-Manifeste)

Validatoren gruen: validate-plugin-structure OK, validate-yaml-frontmatter 0/0, welle5-komma-check 0 Treffer.

---

# v50.1.1 — Testakten-Sektion bei dekorierten Direkt-Download-Headings korrekt positionieren

Codex-Review zu PR #148 hat bemerkt: Der Regex in `scripts/inject-testakten-section.py` matchte nur Headings, die exakt mit `## Direkt-Download` beginnen. Dekorierte Varianten wie `## ⬇️ Direkt-Download (einzelnes ZIP)` oder `## Arbeitsakte (Direkt-Download)` fielen durch, und der Auto-Block wurde stattdessen *vor* dem ersten H2 eingefuegt -- also oberhalb des Direkt-Download-Blocks, entgegen der Skript-Intention.

## Aenderungen

- Regex in `find_insert_position()` aufgeweitet auf `^##[^\n]*Direkt-Download[^\n]*`. Dekorationen wie Emoji, Klammerzusaetze und Praefixe werden jetzt mitgematcht.
- Skript erneut ausgefuehrt; 10 READMEs mit dekorierten Headings sind dadurch korrekt umsortiert worden: `arbeitsrecht`, `arbeitszeugnis-analyse`, `betreuungsrecht`, `datenschutzrecht`, `fachanwalt-verwaltungsrecht`, `fluggastrechte`, `forderungsmanagement-klagewerkstatt`, `legistik-werkstatt`, `steuerrecht-anwalt-und-berater`, `vertragsrecht`.

In den betroffenen Plugin-READMEs steht der Testakten-Block jetzt direkt unter dem Direkt-Download statt davor. Keine fachlichen Inhalte geaendert; nur Reihenfolge.

## Versionen

- Marketplace top-level 50.1.0 -> 50.1.1
- Plugin-Versionen unveraendert (nur READMEs umsortiert, kein SKILL.md, keine plugin.json) -- analog v49.2.0 und v50.1.0.

Validatoren gruen: validate-plugin-structure OK, validate-yaml-frontmatter 0/0, welle5-komma-check 0 Treffer.

---

# v50.1.0 — Testakten-Uebersichten in Plugin-READMEs und Rosengarten-Testakte ausgebaut

User-Feedback: Testakten waren in Plugin-READMEs zu tief unten erwaehnt und es fehlten Downloadlinks. Die Rosengarten-Testakte sollte um alle gaengigen Datenformate erweitert werden.

## Plugin-READMEs (50 betroffene Plugins)

- Neues Skript `scripts/inject-testakten-section.py` legt einen idempotenten Auto-Block `## Testakte(n)` direkt unter den Direkt-Download in jeder betroffenen Plugin-README. HTML-Kommentar-Marker grenzen den Block ab; alte manuell platzierte Testakten-Sektionen werden ausserhalb des Auto-Blocks entfernt.
- Mapping Plugin -> Testakten ist hardcoded; alle 47 Plugin-Eintraege haben zugeordnete Testakten (Mehrfachzuordnungen z.B. bei steuerrecht-anwalt-und-berater, lobbyregister-bundestag, zwangsverwaltung-zvg, betreuungsrecht, insolvenzverwaltung, schriftform-und-textform-bgb, urteilsbauer-relationsmacher, arbeitsrecht).
- Cross-Check: 0 doppelte Testakten-Sektionen im Repo.

## Rosengarten-Testakte

Die Testakte `testakten/nachbarschaftsstreit-horrorfall-rosengarten/` ist um alle gaengigen Datenformate erweitert worden:

- `emails/`: sechs `.eml`-Dateien (Thujahecke, Carport, Bauamt-Anfrage und -Antwort)
- `whatsapp/`: Standard-WhatsApp-Chat-Export
- `xlsx/`: Kosten/Angebote und Riss-Log Stuetzmauer (zwei Tabellenblaetter)
- `docx/`: Anwaltsschreiben Kessler, Aufforderungsschreiben-Entwurf Albers, Vergleichsentwurf
- `pdfs/`: Baumgutachten, Bauamt-Zustaendigkeitsbescheid, Vermessungsskizze
- `scan-whatsapp/`: visuell gerenderter Handy-Screenshot-Scan als PDF
- `gesamt-pdf/`: alles in einem Gesamtdokument mit Cover, Inhaltsverzeichnis, Seitenzahlen und Trennblaettern fuer die externen PDF-Anhaenge
- neue MD-Stuecke `13_zeugenliste_und_anwohner.md` und `14_telefonprotokolle_kanzlei.md` mit Anwohnern, Handwerkern, Behoerdenkontakten und sechs Telefonprotokollen aus dem Kanzleisystem
- README der Testakte komplett neu strukturiert: Gesamt-PDF prominent oben, Format-Sektionen mit allen Dateilinks, Beteiligten-Block, Vorfuehrpfad

## Versionen

- `nachbarschaftsstreit-pruefer` 50.0.0 -> 50.1.0 (Minor, neuer Inhalt in der Testakte)
- Marketplace top-level 50.0.0 -> 50.1.0
- Die 50 nur in der Testakten-Sektion geaenderten Plugin-READMEs bekommen keinen Versions-Bump (nur READMEs, kein SKILL.md, keine plugin.json) -- analog Vorgehen v49.2.0.

Validatoren gruen: validate-plugin-structure OK, validate-yaml-frontmatter 0/0, welle5-komma-check 0 Treffer.

---

# v50.0.0 — Sanity-Check und Versionsbump

- Sanity-Check nach `v49.2.0`: Plugin-Struktur, YAML-Frontmatter, Download-Abdeckung und Release-ZIP-Probelauf geprüft.
- Alle Plugin-Manifeste, Marketplace-Top-Level und Marketplace-Einträge einheitlich auf `50.0.0` gesetzt.
- README, SKILLS.md, Testakten-README und ASSET_INDEX auf 107 Plugins, 2617 Skills, 63 Testakten und 174 Release-Assets nachgezogen.
- Keine fachlichen Inhalte geändert; der Release markiert den konsolidierten v49.2-Stand als nächste Hauptversion.

# v49.2.0 — Skill-Uebersicht in allen 107 Plugin-READMEs vollstaendig

Sanity-Check ergab: in 96 von 107 Plugin-READMEs fehlten Skills in der jeweiligen Uebersicht. In den meisten Faellen war es nur der `allgemein`-Triage-Skill; bei steuerrecht-anwalt-und-berater, selbstvertreter-amtsgericht, arbeitsrecht und 18 fachanwalt-Plugins fehlten erhebliche Bloecke.

## Aenderungen

- Neues Skript `scripts/generate-skills-overview.py` baut in jeder Plugin-README einen automatisch gepflegten Abschnitt `## Alle Skills im Ueberblick` ans Ende. Der Block ist mit HTML-Kommentar-Markern eingegrenzt und kann jederzeit regeneriert werden, ohne manuelle README-Inhalte zu zerstoeren.
- 107 Plugin-READMEs einmalig generiert. Jede README listet jetzt alle Skills des Plugins mit Description aus der jeweiligen SKILL.md.
- Cross-Check: 0 Plugins mit Skill-Drift in der README (vorher: 96).

## Versionen

Plugin-Versionen bleiben unveraendert (49.0.0 bzw. 49.1.0 fuer methodenlehre/mietrecht). Es haben sich nur READMEs geaendert, kein SKILL.md, keine plugin.json, keine references oder assets. Der Repo-Tag `v49.2.0` markiert den Sweep auf Repo-Ebene.

Validatoren gruen: validate-plugin-structure OK, validate-yaml-frontmatter 0/0, welle5-komma-check 0 Treffer.

---

# v49.1.0 — Skill-Uebersichten in methodenlehre und mietrecht vollstaendig

Codex hatte in v48.0.0 achtzehn neue Methodenlehre-Skills hinzugefuegt; die README und der `allgemein`-Skill listeten aber nur zwei davon auf. Im Mietrecht-Plugin fehlten vier Skills in der README-Tabelle.

## methodenlehre-buergerliches-recht

- README Skill-Tabelle vollstaendig: alle 20 Skills in fuenf Bloecken (Praxis-Einstieg, klassische Auslegungskanones, Verfassungs- und Unionsrechtskonforme Auslegung, Rechtsfortbildung und Argumentationsfiguren, methodische Stroemungen).
- `skills/allgemein/SKILL.md` Abschnitt 5 (Spezial-Skills): Routing-Tabelle mit allen 20 Skills, ebenfalls in fuenf Bloecken; Routing-Faustregel um Norm-Auslegung, Rechtsfortbildung, unionsrechtlichen Ursprung und akademische Reflexion erweitert.
- Tippfehler `Geriust` -> `Gerüst` korrigiert (in der Beschreibung des Savigny-Skills).

## mietrecht

- README Skill-Tabelle: vier fehlende Skills ergaenzt (`allgemein`, `mandat-triage-mietrecht`, `mietkaution-rueckforderung`, `weg-beschluss-anfechten`).

## Versionen

- `methodenlehre-buergerliches-recht`: 49.0.0 -> 49.1.0
- `mietrecht`: 49.0.0 -> 49.1.0
- Marketplace.json: entsprechend bewegt

Validatoren gruen: validate-plugin-structure OK, validate-yaml-frontmatter 0/0, welle5-komma-check 0 Treffer.

---

# v49.0.0 — WEG-Großakte, Barrierefreiheit und Komplettpaket

- `weg-hausverwaltung` ausgebaut: sieben zusätzliche Skills für Großakten-Routing, Protokollmarathon, Ist-/Plan-/Mieterschnittstelle, Heizungs-/Versicherungsschäden, E-Mobilität/PV/Kellerstrom, Restaurant-/Hofkonflikte sowie Hausordnungsthemen.
- Testakte `weg-hausverwaltung-hohenzollernhof` erweitert: 24 Aktenstücke, EML-Mailbox, CSV/XLSX-Ist-Plan-Tabelle, Bildablage und konsolidierte 112-Seiten-Gesamt-PDF.
- Neues Plugin `barrierefreiheit-web-checker` mit 12 Skills für BFSG/BFSGV/BITV/WAD/EN 301 549/WCAG, Audit, Tastatur, Screenreader, Formulare, PDFs, Erklärung, Roadmap und Agenturabnahme.
- Release-Workflow baut zusätzlich `alles-komplettpaket.zip` mit allen Plugin-ZIPs, allen Testakten-ZIPs, Marketplace und Übersichten.
- Marketplace, README, Testakten-README, Asset-Index, Rechtsgebietsübersicht und Skill-Gesamtübersicht auf 107 Plugins, 2617 Skills und 63 Testakten aktualisiert.

# v47.2.0 — Plugin methodenlehre-buergerliches-recht: README und Skills geschaerft

Das Plugin `methodenlehre-buergerliches-recht` wurde an drei Stellen verbessert; die alte Breaking-Change-Sektion in der README ist entfernt, weil sie seit dem Plugin-Rename in v3.0 ihren Zweck erfuellt hat und nun nur noch Laerm war.

## README

- Sektion `Breaking Change in v3.0` entfernt.
- Neue Sektion `Was dieses Plugin konkret macht`: praezise Beschreibung der Plugin-Leistung mit allen Komponenten (Anspruchsgrundlagen-Reihenfolge, vier Kanones plus zwei Querschnittskanones, Lueckenfuellung, Generalklauseln, Querschnittsthemen, Verbotsliste, Memo-Standardstruktur, Selbstpruefungs-Checkliste).
- Skill-Tabelle um den `allgemein`-Skill erweitert (war bisher untertabelliert).
- Neuer Abschnitt `Verknuepfung mit anderen Plugins`.

## Skill `methodenlehre-anwenden`

- Neue Begruendung der Anspruchsgrundlagen-Reihenfolge (Speziellere vor Allgemeineren, rechtsgeschaeftliche Bindung vor gesetzlichen Schuldverhaeltnissen, etc.).
- Drei konkrete Praxisbeispiele zur Gewichtung der Auslegungskanones (§ 199 Abs. 1 BGB, § 138 Abs. 2 BGB, §§ 651a ff. BGB Pauschalreise).
- Erweiterter Abschnitt zu Rechtsfortbildung mit vier klassischen BGH-Argumentationsmustern (Vertrag mit Schutzwirkung, Drittschadensliquidation, c.i.c. vor 2002, Verwirkung/Treuwidrigkeit ueber § 242 BGB).
- Neuer Hinweis zu typischen Fehlanwendungen von Generalklauseln als Erstargument.
- Verbotsliste um Punkt "keine ergebnisorientierte Rueckwaerts-Subsumtion" erweitert.
- Selbstpruefungs-Checkliste um Rechtsfortbildungs-Frage erweitert.
- Verlinkung zu `bgb-at-pruefer` ergaenzt.

## Skill `allgemein`

- Sektion `Spezial-Skills in diesem Plugin`: aussagekraeftige Beschreibung statt Trunkierung; neue Spalte `Erwarteter Output`.
- Neuer Block `Routing-Faustregel` mit vier konkreten Weiterleitungen (BGB-AT-Detailpruefung zu `bgb-at-pruefer`, Zitierfragen zu `zitierweise-deutsches-recht`, Fachgebiete zu Fachplugins).

## Plugin-Version

- `methodenlehre-buergerliches-recht/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json` auf `42.1.0`. Description und Slug unveraendert.

# v47.1.1 — Plugin gesellschaftsrecht-legal-english: Codex-Feedback zu bgb-at-schuldrecht-at-im-ma

Reaktion auf zwei P2-Badges aus dem Codex-Review zu PR #142:

- **§ 343 BGB qualifiziert auf Kaufleute (§ 348 HGB):** Die fruehere Aussage "Im B2B kein § 343 BGB-Schutz" war zu pauschal. Der Ausschluss der richterlichen Herabsetzung greift nach § 348 HGB nur, wenn ein Kaufmann die Vertragsstrafe im Betrieb seines Handelsgewerbes verspricht. Fuer Freiberufler, nicht-gewerbliche GbRs und Unternehmer ohne Kaufmannseigenschaft bleibt § 343 BGB anwendbar. Wurde sauber qualifiziert.
- **Falsche BGH-Zitate ersetzt:** BGH I ZR 17/05 (Pralinenform II) ist Markenrecht und keine Best-Efforts-/§ 242-Entscheidung. BGH VIII ZR 244/97 betrifft Leasing-AGB und nicht die Einheitstheorie. Beide entfernt. Neu: BGH II ZR 155/85 (14.04.1986) und BGH VIII ZR 329/99 (27.06.2001, NJW 2002, 142) zur Reichweite des Beurkundungserfordernisses nach § 15 Abs. 4 GmbHG. Die Best-Efforts-Auslegung wird nun dogmatisch ueber § 242 BGB hergeleitet, ohne unpassende Einzelfallzitate. AGB-B2B-Quelle ersetzt durch BGH VII ZR 58/14 (22.10.2015).

## Plugin-Version

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json` auf `47.1.1` gebumpt. Description und Slug unveraendert. Skill-Anzahl unveraendert (32).

# v47.1.0 — Plugin gesellschaftsrecht-legal-english: zwei neue Grundlagen-Skills

Reaktion auf den Hinweis aus der Praxis (LinkedIn-Diskussion vom 29.05.2026), dass M&A-Anwaelte regelmaessig Basics aus BGB AT, Schuldrecht AT und Kapitalaufbringungsrecht uebersehen, weil sie M&A fuer reines Vertragsrecht halten. Gerade in Zeiten breiter KI-Nutzung bleibt das Grundlagenwissen entscheidend, damit Ergebnisse richtig interpretiert werden.

Zwei neue Skills im Plugin `gesellschaftsrecht-legal-english`:

- **`verdeckte-sacheinlage`**: erkennt und prueft verdeckte Sacheinlage und Hin-und-Her-Zahlung nach § 19 Abs. 4 und Abs. 5 GmbHG. Anrechnungsloesung seit MoMiG, Vorbelastungshaftung, Pruefraster mit sieben Schritten, typische M&A-Fallen (Cash-In-Series-A plus Akquisition, Wandeldarlehen, Verrechnungsabreden, Sale-and-lease-back, Beraterhonorar an Investor), klare Heilungswege.
- **`bgb-at-schuldrecht-at-im-ma`**: macht sichtbar, wo BGB AT und Schuldrecht AT in englischsprachigen M&A-, Finanzierungs- und SHA-Vertraegen unter deutschem Recht stillschweigend mitlaufen. Zehnstufiges Pruefraster: Form und Einheitstheorie § 15 Abs. 4 GmbHG, Stellvertretung §§ 164 ff. und § 181 BGB, Bedingungseintritt und -vereitelung § 162 BGB, AGB-Kontrolle §§ 305 ff. und § 307 BGB auch im B2B, Treu und Glauben § 242 BGB fuer reasonable-/best-efforts, Anfechtung §§ 119, 123 BGB und Sperre des § 444 BGB. Konkrete Falleinordnungen mit Heilungswegen.

Beide Skills sind in der Fuehrungsmatrix des `allgemein`-Routing-Skills erfasst, damit Nutzer mit Aussagen wie "Wir machen Vertragsrecht, BGB AT ist egal" oder "Bareinlage und gleichzeitig Erwerb vom Gesellschafter" direkt auf die richtige Stelle geroutet werden.

## Plugin-Version

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json` auf `47.1.0` gebumpt (Skill-Anzahl von 30 auf 32). Description und Slug unveraendert.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v47.0.0 — Schlussrunde Testakten, Übersichten und quellenfeste Schriftformakte

Große Abschlussrunde über den Akten- und Release-Bestand:

- Alle Testakten-READMEs von sichtbaren Test-/Lehr-/Fiktionsmarkern bereinigt und auf Aktenlogik, Direkt-Downloads und menschliche Umlaute geglättet.
- Schmalfeld-Betreuungsakte um `09_vertragsauszuege_pruefmappe.md` erweitert: Alltagsverträge, Fernwartungs-/Sicherheitssoftware, Hochrisikoanlagen, Spanien-Reservierung, Haustürvertrieb, Beleglücken und priorisierte Maßnahmen.
- Schriftform-Maklerakte Haspelbeck von einem nicht verifizierten BGH-Scheinzitat bereinigt: fake BGH-PDF entfernt, PDFs neu ohne Erzeugungsfußzeilen gebaut, Excel/Markdown-Vorschau auf offene Rechtsprechungsprüfung umgestellt.
- VerkehrsOWi-Akte von konstruierten OLG-Fundstellen bereinigt und in eine quellenfeste Rechtsprechungsrecherche mit Arbeitsmatrix umgebaut.
- Sichtbare Unterrichts-/Muster-Slugs in mehreren Akten entschärft: LUMEN Studios, Strafbefehl, VerkehrsOWi, Solis Vision X, Sozialrecht Tannenberg und Roeschen Tech laufen nun als Arbeits-, Prüf- oder Fallkonferenzakten.
- `SKILLS.md` neu aus dem tatsächlichen Bestand generiert: 2.553 Skill-Links in 105 Plugins, inklusive der bisher fehlenden Agio-/Kapitalrücklage-Skills.
- Plugin-/Testakten-Übersichten aktualisiert; `gesellschaftsrecht` und `grosskanzlei-corporate-ma` verlinken nun auch die Corporate-Legal-English-Frankfurt-Akte.
- README, Testaktenübersicht und Asset-Index auf `v47.0.0` nachgezogen; Sammel-Downloads `alle-plugins-megazip.zip` und `alle-testakten.zip` bleiben sichtbar.

---

# v46.0.0 — Corporate-Legal-English-Akte: Gesamt-PDF und Cap-Table-Abgleich

Nachlauf für `gesellschaftsrecht-legal-english` und die Frankfurt-Startup-Akte:

- `18-cap-table-und-waterfall.xlsx` auf den Aktenstand aus Datei 02 gebracht: Kunigunde/Meinhard/Walburga, 900 VSOP, 5.000 Pool, 6.700 Convertible, 16.679 Northbridge- und 1.390 Krämer-Angel-Anteile.
- `18-cap-table-und-waterfall.pdf` als PDF-Ausdruck des Excel-Arbeitsmodells ergänzt.
- `26-gesamtakte-kometenfalter-series-a.pdf` als 64-seitige zusammengeführte Lesefassung der Aktenbestandteile ergänzt, inklusive Excel-Ausdruck, Bildfragmenten und E-Mail-Anhang.
- WhatsApp-PDF im Chatlook neu erzeugt; die Bildfragmente 20 bis 22 von Rookie-/Lernhinweisen bereinigt.
- README-Dateien, Marketplace und Plugin-Manifest für `gesellschaftsrecht-legal-english` aktualisiert; Plugin-Version jetzt `46.0.0`.

---

# v45.0.0 — Sammel-ZIPs für Plugins und Testakten

Release-Infrastruktur und Übersichten nachgezogen:

- `.github/workflows/release-plugin-zips.yml` baut zusätzlich `alle-plugins-megazip.zip` mit allen installierbaren Plugin-ZIPs plus `marketplace.json`.
- Der Workflow baut zusätzlich `alle-testakten.zip` mit allen Testaktenordnern in Originalstruktur.
- `README.md`, `testakten/README.md` und `ASSET_INDEX.md` zeigen die Sammel-Downloads sichtbar an.
- Erwarteter Release-Umfang: 105 Plugin-ZIPs, 63 Testakten-ZIPs, `marketplace.json` und 2 Sammelarchive, also 171 Assets.

---

# v44.0.1 — Akte: Excel entlehrmaterialisiert, gemischte PDFs nach Kanaltyp getrennt

Folgefix nach v44.0.0. Drei Dinge:

## Excel

- `18-cap-table-waterfall-training.xlsx` → ersetzt durch `18-cap-table-und-waterfall.xlsx`.
- Workbook-Titel: "Cap Table und Waterfall — Series A Project Comet Moth" (statt "Corporate Legal English Training Workbook").
- Sheets neu: Übersicht, Cap Table, Pool-Szenarien, Wandeldarlehen, Waterfall. Sheet "Rookie Quiz" geloescht, Sheet "README" als "Übersicht" mit Mandantin / Aktenzeichen / Sachbearbeitung / Stand neu aufgesetzt.
- Alle "Lernziel", "Didaktischer Hinweis", "fiktive Testakte", "Training Workbook", "didaktisch", "Rookie"-Markierungen entfernt.

## PDF-Trennung nach Kanaltyp

- `01-partnerauftrag-email.md` enthielt zwei E-Mails plus einen Slack-Thread im selben PDF. Aufgeteilt: `01-partnerauftrag-emails.md` (nur die zwei E-Mails) plus `chats/01-slack-comet-moth-cap-table.md` (Slack) jeweils als eigenes DOCX und PDF.
- `11-investor-counsel-markup-roundtrip.md` enthielt drei E-Mails plus eine Randnotiz Westarp. Aufgeteilt: `11-investor-counsel-markup-emails.md` (nur die drei E-Mails) plus `11n-westarp-randnotiz-zum-entwurf.md` (Randnotiz) jeweils als eigenes DOCX und PDF.
- `chats/16-whatsapp-partner-associate-thread.md` jetzt auch als eigenes DOCX und PDF (zusaetzlich zum bereits separat existierenden Datei-16-PDF im Wurzelverzeichnis).

## Restliche Textentlehrungen

- `00-deal-personen-und-zeitleiste.md`: Abschnitt "Was die Akte testet" umbenannt in "Aktenschwerpunkte fuer die kommende Verhandlung", inhaltlich auf das Mandat statt auf den Lernzweck formuliert.
- `06-associate-arbeitsstand.md`: Lead-Absatz von "dem Nachwuchs zeigen, wie eine Partnerin Anfaengertexte umarbeitet — sachlich, hart, lehrreich" auf "Adelheid von Westarp hat am 21.05.2026 vormittags Anmerkungen am Rand vermerkt" geaendert.
- `14-board-und-consent-matters-mapping-de-en.md`: Abschnitt "Lernziel" in "Ausgangspunkt" umbenannt.
- `chats/01-slack-comet-moth-cap-table.md`: Kopfblock "Auszug aus dem internen Slack-Channel" durch realistische Channel-/Teilnehmer-/Zeitstempel-Angaben ersetzt.

## Konsequenzen fuer README und Plugin-README

- Testakten-`README.md`: Aktenbestand-Tabelle aktualisiert (neue Dateinamen `01-partnerauftrag-emails`, `11-investor-counsel-markup-emails`, `11n-westarp-randnotiz-zum-entwurf`, `18-cap-table-und-waterfall.xlsx`). Hinweise auf chats/DOCX/PDF ergaenzt.
- Plugin-`README.md`: Excel-Dateiname aktualisiert; Demo-Material-Sektion um chats/ ergaenzt.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Volltextsuche `lehr|fiktiv|didakt|training|quiz|rookie|lernziel|simul|cheatsheet|musterloesung` ueber alle PDFs/DOCX/XLSX — 0 echte Treffer (nur juristischer Fachbegriff "Zweckuebertragungslehre" verbleibt).

---

# v44.0.0 — Testakte Frankfurt-Startup entlehrmaterialisiert: echte Akte statt Lehrkompendium

Die Frankfurt-Startup-Testakte wird zu einer realistischen Mandatsakte umgebaut. Alle didaktischen Marker ("fiktive Lehrakte", "Aehnlichkeiten zu realen Transaktionen sind nicht beabsichtigt", "Lehrmaterial") sowie alle formalen Lehrhilfen (Cheat-Sheets, Glossare, Fehlerkataloge, Index-Beipackzettel) sind entfernt. Was bleibt, ist das bluehende Leben einer Series-A-Mandatsakte der Kanzlei Hagemann & Westarp fuer die Kometenfalter Systems GmbH.

## Entlehrmaterialisierung

- Fuenf formale Lehrdateien geloescht (jeweils `.md` + `.docx` + `.pdf`): `07-erwarteter-output`, `08-glossar-english-deutsch`, `09-anfaengerfehler-katalog`, `17-anschauungsmaterial-index`, `23-rookie-cheatsheet`.
- In den verbleibenden 15 Markdown-Dateien alle Disclaimer-Zeilen entfernt ("Fiktive Lehrakte", "Aehnlichkeit zu realen Transaktionen", "Lehrmaterial", "Didaktischer Hinweis", "Simuliert wird").
- ASCII-Umlaute systematisch gefixt: `Aehnlichkeiten` → `Ähnlichkeiten`, `Uebersetzung` → `Übersetzung`, `fuer` → `für` (kontextabhaengig), `dass` korrekt, `ß` durchgaengig.
- E-Mail-Adressen entfiktivisiert: `[mailto fiktiv ...]` → echte Kanzlei-Domains (`@hagemann-westarp.de`, `@brackenmuir-quint.de`); "Fiktive Adresse:" → echte Anschrift.
- `README.md` der Testakte komplett neu als Akten-Deckblatt der Kanzlei (Mandantin, Az., Sachbearbeitung, Aktenbestand).

## Re-Rendering

- Alle verbleibenden 16 Markdown-Dateien (15 Sachdateien + `README.md`) sowie das Notar-Memo 19 neu als `.docx` und `.pdf` gerendert (17 DOCX + 17 PDF).
- Footer: `Vertraulich · Akteninterne Bearbeitungsfassung` (statt v43-Footer `Lehrmaterial Didaktisches Gesellschaftsrecht`).
- Nummerierte Listen werden jetzt korrekt als `1.`/`2.`/`3.` gerendert (war v43-Bug — alle Eintraege erschienen als `1.`).
- Notar-Memo 19 (`19-notar-scan-beurkundungssprache`) neu als realistisches Memorandum aus dem Notariat Veitschegger mit Briefkopf, Az. UR-Nr. 1182/2026, ohne didaktische Rahmung.
- EML-Dateien (`emails/11a`, `emails/11b`) korrigiert: echte Domains, korrekte Anschriften.

## Plugin-Version

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json` auf `44.0.0` gebumpt. `description` und Slug unveraendert.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Volltextsuche `lehr|fiktiv|didakt|simuliert|aehnlich` in allen 17 PDFs, 17 DOCX, 5 EML, 2 Chat-MDs — 0 Treffer.
- PDF 19 (Notar-Memo) und PDF 11 (Investor-Counsel) visuell mit `pdftoppm` geprueft: Briefkopf korrekt, Nummerierung korrekt, kein Ueberlauf.

---

# v43.0.0 — Frankfurt-Startup-Testakte Big-Law-Rebuild + Plugin-Spotlight "Didaktisches Gesellschaftsrecht — English Business Terms"

Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` komplett neu gerendert und didaktisch erweitert; Plugin `gesellschaftsrecht-legal-english` (Slug unveraendert) tritt jetzt unter dem Titel "Didaktisches Gesellschaftsrecht — English Business Terms" auf.

## Testakte-Rebuild

- Alle 20 Textdateien + 2 didaktische Cheatsheets (19, 23) zusaetzlich als Big-Law-Memo gerendert: 22x `.docx` und 22x `.pdf` im Stil Times New Roman 11pt, Blocksatz, Seitenkopf (Mandantenname links / Dateilabel rechts), Seitenfuss (Vertraulichkeitshinweis links / "Seite X von Y" rechts), H1 zentriert, H2 nummeriert (13pt bold), H3 als (a)/(b) (11pt bold), Tabellen mit grauer Headerzeile und sauberem Umbruch.
- PDF 19 (Notar-Scan Beurkundungssprache § 16 BeurkG) und PDF 23 (Rookie Cheatsheet Corporate Legal English ↔ Deutsches Werkzeug) komplett neu aufgesetzt: kein Textueberlauf am rechten Rand mehr, keine Label-Kollision "Deutsches WerkzeugSatzung" mehr, Spaltenbreiten 22/38/40 % mit sauberem Zeilenumbruch.
- Fiktive E-Mails (2 aus Datei 01, 3 aus Datei 11) zusaetzlich als echte `.eml`-Dateien in `emails/` mit RFC-5322-Headern (Outlook-kompatibel).
- Slack-Thread `#project-comet-moth` (Mittwoch 22:14-22:58) als eigenstaendige Markdown in `chats/01-slack-comet-moth-cap-table.md` extrahiert.
- WhatsApp-Verlauf Partner/Associate (Donnerstag 06:58-08:21) vollstaendig in `chats/16-whatsapp-partner-associate-thread.md` gespiegelt (zusammenhaengender Thread, daher in Gaenze).

## Plugin-Spotlight

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json`: `description` auf "Didaktisches Gesellschaftsrecht — English Business Terms: Corporate Legal English fuer Big-Law-Anfaenger…" umgestellt, `version` auf `43.0.0` gebumpt. Slug `gesellschaftsrecht-legal-english` BLEIBT (kein Rename).
- `gesellschaftsrecht-legal-english/README.md`: Titel auf "Didaktisches Gesellschaftsrecht — English Business Terms". Testakten-Beschreibung um DOCX/PDF/EML/Chats erweitert.
- `.claude-plugin/marketplace.json`: Eintrag fuer `gesellschaftsrecht-legal-english` an die neue description angepasst und auf `43.0.0` synchronisiert.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- PDF 19/23 + Stichprobe PDF 11 visuell mit `pdftoppm` geprueft: kein Ueberlauf, Header/Footer/Seitenzaehler korrekt.

---

# v42.0.0 — README-Spotlight komplett entfernt

- "Ganz oben: Corporate Legal English"-Spotlight-Block aus README entfernt.
- README startet jetzt direkt mit "Über dieses Repository" nach der Titelzeile und dem Lead-Absatz.
- Keine Plugin-Aenderungen.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v41.0.0 — README-Spotlight: Corporate Legal English statt Meinungspruefer (Tag-Bump nach v40)

Reiner Tag-Bump: Der v40.0.0-Tag wurde bereits zuvor auf den Sanity-Release-Commit `51ade7ae` gesetzt. Da der README-Schnitt (Meinungspruefer-Hero raus, Corporate Legal English oben) danach folgte und Tags nicht ueberschrieben werden, wird der aktuelle `main` als `v41.0.0` markiert.

Inhaltlich identisch zum unten gepflegten v40-Eintrag (Sanity-Release + README-Spotlight). Keine Plugin-Aenderungen.

---

# v40.0.0 — Sanity-Check-Release nach v39 + README-Spotlight Corporate Legal English

Sammelrelease: Der aktuelle `main`-Stand nach `v38.0.0` (Steuerrechts-Sanity-Fix) und `v39.0.0` (CO2KostAufG-Präzisierung) wurde gegen die Repo-Validatoren und den Release-ZIP-Bau geprüft und als nächster stabiler Download-Stand markiert. Zusätzlich wurde das README-Spotlight redaktionell geändert.

## README-Spotlight

- Meinungspruefer-Block ganz oben aus README entfernt.
- Spotlight-Abschnitt umbenannt zu "Ganz oben: Corporate Legal English" und auf `gesellschaftsrecht-legal-english` mit Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` fokussiert (Kaltstart, Dealroom-Lernpfad, Cap Table, Gesellschafterliste, Term Sheet, SHA, Liquidation Preference, Anti-Dilution, Vesting, Drag/Tag, SPA/DD-Begriffe, englische Vertragssprache unter deutschem Recht).
- Keine Plugin-Aenderungen; rein redaktioneller README-Schnitt zusätzlich zum Sanity-Release.

## Qualitätssicherung

- `git diff --check` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-release-zips.py /tmp/codex-release-sanity .claude-plugin/marketplace.json` — OK
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Release-Asset-Sanity: 105 Plugin-ZIPs, 63 Testakten-ZIPs, 1 `marketplace.json`, insgesamt 169 Assets

## Dokumentation

- `README.md` und `ASSET_INDEX.md` auf `v40.0.0` aktualisiert.

---

# v39.0.0 — Codex-Round-5: CO2KostAufG-Praezisierung (§ 3-Pflichtangaben + § 8 Nichtwohngebaeude 2025)

Zwei Codex-Findings zur Testakte `testakten/weg-hausverwaltung-hohenzollernhof/11-co2kostaufg-aufteilungspruefung.md`:

## Findings

- **§ 3 vs. § 5/§ 7 — Primaerdaten von Berechnungsfeldern trennen.** Das Beanstandungsschreiben fuehrte `gebaeudespezifischer Wert in kg CO2/m2/a` und `Einstufung in die Anlage zu § 5` als angeblich vom Gaslieferanten nach § 3 CO2KostAufG zu uebermittelnde Angaben auf. Tatsaechlich kennt der Lieferant weder die relevante Wohnflaeche noch die resultierende § 5-Stufe; § 3 Abs. 1 Nr. 1-5 schuldet nur (1) Brennstoffemissionen in kg CO2, (2) CO2-Preisbestandteil in EUR, (3) heizwertbezogener Emissionsfaktor in kg CO2/kWh, (4) Energiegehalt in kWh, (5) Hinweis auf Erstattungsansprueche §§ 6 Abs. 2, 8 Abs. 2. `gebaeudespezifischer Wert` und `Einstufung` sind § 5/§ 7-Berechnungen des Vermieters. Klarstellung im Datenpflichten-Abschnitt, im Beanstandungsschreiben und im Hinweis fuer die Verwalterin eingebaut.
- **§ 8 CO2KostAufG — Stufenmodell fuer Nichtwohngebaeude 2025 noch nicht operativ.** Der frueher Abschnitt schrieb `ab 01.01.2025 auch Nichtwohngebaeude im Stufenmodell`. § 8 Abs. 4 sieht aber nur vor, dass die haelftige Aufteilung im Jahr 2025 abgeloest werden soll; ein operatives Stufenmodell fuer Nichtwohngebaeude ist im Gesetzestext noch nicht enthalten. Bis zur Einfuehrung der Tabelle gilt nach § 8 Abs. 1 weiterhin **50/50** (Vereinbarungen ueber mehr als 50 % Mieteranteil unwirksam). Korrigiert in der Anwendungsbereichs-Beschreibung und im Berechnungsabschnitt.

Quelle (verifiziert): https://www.gesetze-im-internet.de/co2kostaufg/__3.html, https://www.gesetze-im-internet.de/co2kostaufg/__8.html

## Plugin-Versionsbumps

- `weg-hausverwaltung` 37.0.0 → 38.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v38.0.0 — Sanity-Check Tax + Bug-Fix § 1 Abs. 3 GrEStG statt AO

Sanity-Check des Tax-Commits `4ab560c2` (16 neue GrESt- und Grundsteuer-Skills, zwei neue Testakten). Validatoren alle grün, Rechtsstand-Anker verifiziert (§ 6a GrEStG noch 95 %, BFH II B 13/25, II B 23/25, II B 47/25, BFH II R 25/24 zum Bundesmodell, BVerfG 1 BvL 11/14). Ein Bug gefunden und behoben.

## Bug-Fix

- **`anw-grunderwerbsteuer-share-deal-90-prozent` description**: Die YAML-`description` hatte den falschen Normverweis `§ 1 Abs. 3 AO` (Abgabenordnung) statt `§ 1 Abs. 3 GrEStG`. Im Body war die Norm korrekt zitiert; nur das Suchmetadatum-Feld war vertauscht. Korrigiert.

## Plugin-Versionsbumps

- `steuerrecht-anwalt-und-berater` 36.1.0 → 37.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Forbidden-Frontmatter-Check — leer

---

# v37.0.0 — Codex-Round-4-Fixes: CO2KostAufG-Datenpflichten richtig zuordnen

Drei Codex-Findings zur Testakte `11-co2kostaufg-aufteilungspruefung.md` aus dem v36-PR behoben:

- **Datenpflichten-Basis korrigiert**: `§ 2 Abs. 2 CO2KostAufG` war falsche Anspruchsgrundlage — § 2 regelt nur den Anwendungsbereich. Datenpflichten differenziert nach § 3 (Lieferanteninformation an den Bezieher = WEG/Verwalter), § 5 (Stufentabelle/Anlage), § 6 (Begrenzung Umlagefähigkeit/Erstattungsanspruch Mieter), § 7 Abs. 3 und 4 (Vermieter-Abrechnungspflicht gegenüber Mieter), § 8 (Nichtwohngebäude). Praxis-Klarstellung: die WEG-Jahresabrechnung muss die CO2-Datenfelder selbst **nicht** ausweisen; die Verwalterin muss die § 3-Lieferantendaten an die vermietenden Eigentümer **weiterreichen**, damit diese ihrer § 7-Pflicht nachkommen können.
- **Stufe-5-Anteile entreversed**: Das Beanstandungsschreiben hatte "60 % Vermieter / 40 % Mieter" — die Stufentabelle weist Stufe 5 (27–32 kg CO2/m2/a) korrekt mit **60 % Mieter / 40 % Vermieter** aus. Korrigiert.
- **Endempfehlung konsistent**: Der Schlussabschnitt "Hinweis fuer Verwalterin" empfahl noch die Anwendung des Stufenmodells in der WEG-Heizkostenabrechnung — widersprach der neuen WEG-Analyse. Korrigiert: WEG-interne Verteilung nach HeizkostenV (70/30) bleibt unverändert; Stufenmodell **nicht** in der WEG-Abrechnung; stattdessen separate Anlage "CO2-Lieferantendaten nach § 3 CO2KostAufG" zur Jahresabrechnung. Anfechtungs-Praxisempfehlung entsprechend nachgezogen.

## Plugin-Versionsbumps

- `weg-hausverwaltung` 36.0.0 → 37.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v36.1.0 - Steuerrecht Grundsteuer und Grunderwerbsteuer

- **16 neue Steuerrechts-Skills.** Acht Grundsteuer-Skills decken Kaltstart/Bescheidkette, Verfassungscheck, Ermittlungsbasis, BewG-Bewertung, Einspruch/AdV, Landesmodell-Routing, Hebesatz/Zahlung und gemeinen Wert/Gutachten ab. Acht GrESt-Skills decken Asset Deal, Share Deal, Signing/Closing-Doppelfestsetzung, § 19-Anzeige, SPA-Tax-Clause, § 6a-Konzernklausel und Bescheid/Einspruch/AdV/§ 16 GrEStG ab.
- **Faktenbank erweitert.** `rechtsstand-mai-2026-faktenbank` enthält jetzt die Grundsteuer-Anker BVerfG 10.04.2018, BFH-AdV 27.05.2024, BFH-Bundesmodell 12.11.2025, BFH-Baden-Württemberg-Stand Mai 2026, die gleich lautenden Ländererlasse vom 20.02.2026 zu Share Deals sowie die BFH-Signing/Closing-Beschlüsse II B 13/25, II B 23/25 und II B 47/25.
- **Zwei neue Testakten.** `grundsteuer-rosenwinkel-bescheidkette` führt durch Grundsteuerwert-, Mess- und Gemeindebescheid mit Flächenfehlern, Denkmalschutz, Leerstand und niedrigerem gemeinen Wert. `grunderwerbsteuer-sharedeal-closing-waldkrone` bildet eine Share-Deal-Closing-Akte mit drei Bundesländern, § 19-Anzeige, SPA-Steuerklausel, Escrow und Doppelbescheid-AdV ab.
- **Dokumentation und Metadaten.** Steuerrechts-README, Testakten-README, SKILLS-Übersicht, Asset-Index, Marketplace und Plugin-Manifest aktualisiert; `steuerrecht-anwalt-und-berater` auf `36.1.0` gesetzt.

## Qualitätssicherung

- `git diff --check`
- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- JSON-Manifest-Parse aller Plugin-Manifeste

---

# v36.0.0 — Codex-Round-3-Fixes: HeizkostenV-Bandbreite, § 18 vs. § 28 WEG, CO2KostAufG WEG-Grenzen, Gewährleistungs-Werkart, § 55a GmbHG, negatives Agio

Sechs Codex-Review-Findings aus dem v35-PR systematisch behoben:

- **HeizkostenV-Bandbreite korrekt formuliert** (`weg-hausverwaltung/skills/betriebskosten-nebenkostenabrechnung/SKILL.md`). Die irreführende Formulierung `mindestens 50/30/70 Prozent nach Verbrauch` wurde durch die richtige Regel ersetzt: verbrauchsabhängiger Anteil mindestens 50 Prozent und höchstens 70 Prozent, restlicher Anteil (30 bis 50 Prozent) nach Wohnfläche oder umbautem Raum (§§ 7, 8 HeizkostenV). Der häufige Schlüssel 70/30 ist ausdrücklich als eine zulässige Ausgestaltung innerhalb der Bandbreite gekennzeichnet.
- **§ 55a GmbHG ergänzt** (`corporate-kanzlei/skills/corporate-kanzlei-agio-und-kapitalerhoehungsstruktur/SKILL.md`). Die Authorized-Capital-Zeile in der US-Term-Sheet-Übersetzungstabelle behauptete fälschlich, die GmbH kenne kein genehmigtes Kapital. Korrigiert auf: bei der AG § 202 AktG, bei der GmbH seit MoMiG ausdrücklich § 55a GmbHG (mit Verweis auf den bestehenden Skill `gesellschaftsgruender-genehmigtes-kapital`).
- **Negatives Agio als rechtlich ausgeschlossen klargestellt** (`corporate-kanzlei/skills/corporate-kanzlei-agio-und-kapitalerhoehungsstruktur/SKILL.md`). Die Down-Round-Passage hatte die wirtschaftliche Verwässerung mit einem "negativen Agio" beschrieben. Das ist juristisch falsch: Ausgabe unter pari verstößt gegen § 9 Abs. 1 GmbHG / § 5 Abs. 2 GmbHG (Verbot der Unter-pari-Emission, nichtige Kapitalerhöhung). Korrigiert auf die drei zulässigen Down-Round-Instrumente: Null-Agio, größere Stückzahl zum reduzierten Preis pro Anteil, flankierende Wandeldarlehen oder Anti-Dilution-Anpassungen.
- **CO2KostAufG nicht auf WEG-Innenverhältnis anwenden** (`testakten/weg-hausverwaltung-hohenzollernhof/11-co2kostaufg-aufteilungspruefung.md`). Die Testakte hatte den Eindruck vermittelt, das CO2KostAufG-Stufenmodell sei auf die WEG-Jahresabrechnung anzuwenden. Korrigiert: das CO2KostAufG regelt nur das Vermieter-Mieter-Verhältnis (§§ 1, 2 CO2KostAufG); die WEG-interne Hausgeldumlage bleibt bei § 16 Abs. 2 WEG und HeizkostenV. Praxisrelevanz für die WEG: vermietende Eigentümer brauchen aus der Jahresabrechnung Datengrundlagen (Brennstoffmenge, CO2-Emission, Energieträger, gebäudespezifischer CO2-Wert) gemäß § 2 Abs. 2 CO2KostAufG. Beanstandung und Anfechtungsrisiko entsprechend umformuliert.
- **Gewährleistungsfrist nach Werkart differenziert** (`weg-hausverwaltung/skills/handwerker-beauftragung-vergabe/SKILL.md`). Die pauschale Auswahl `5 / 4 Jahre` ist nur für Bauwerk-Arbeiten korrekt. Ergänzt um die richtige Trias: BGB Bauwerk 5 Jahre (§ 634a Abs. 1 BGB), VOB/B Bauwerk 4 Jahre bei wirksamer Einbeziehung (§ 13 Abs. 4 VOB/B), sonstige Werkleistungen und Wartung 2 Jahre. Im Auftragsbestaetigungs-Muster und in der Vergleichstabelle.
- **Belegeinsicht § 18 Abs. 4 WEG statt § 28 Abs. 4 WEG** (`weg-hausverwaltung/skills/datenschutz-dokumentenfreigabe/SKILL.md`). Die Belegeinsicht in Verwaltungsunterlagen folgt § 18 Abs. 4 WEG; § 28 Abs. 4 WEG regelt nur den Vermögensbericht. Description und Body entsprechend getrennt; beide Rechtsgrundlagen verlinkt.

## Plugin-Versionsbumps

- `corporate-kanzlei` 30.0.0 → 31.0.0
- `weg-hausverwaltung` 35.0.0 → 36.0.0
- `gesellschaftsrecht-legal-english` 35.0.0 → 36.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v35.0.0 — Agio-Dogmatik in drei Plugins, Codex-Round-2-Fixes, Umlaut-Hygiene Testakte

- **Codex-Round-2-Fixes in `testakten/gesellschaftsrecht-legal-english-frankfurt-startup/`.** Der `§ 14 GmbHG`-Anker für Sonderrechte/Vorzugsanteile wurde in den Dateien `06-associate-arbeitsstand.md` und `07-erwarteter-output-ohne-musterloesung.md` durch den korrekten Anker `Satzungsautonomie + § 35 BGB analog` ersetzt; gestützt auf ständige Rechtsprechung (BGHZ 123, 15; BGH II ZR 89/79 = LM BGB § 35 Nr. 4; OLG Nürnberg 12 U 813/99). § 14 GmbHG (Einlagepflicht/Nennbetrag) wird explizit als Nicht-Anker markiert. In `02-cap-table-und-gesellschafterliste.md` wurde der irreführende Verweis auf eine angebliche Subscription-Liste in Datei 03 Ziff. 2 berichtigt — die 4,8/0,4-Aufteilung steht in Datei 02 selbst (CFO-Slack-Thread vom 28.05.2026); Datei 03 Ziff. 2 verlangt nur eine Lead-Mindestquote von 75 Prozent.
- **Umlaut-Hygiene Testakte.** Sämtliche deutschen Wörter in der Testakte wurden auf korrekte Umlaute (ä/ö/ü/ß) umgestellt. Wortgrenzen-basiertes Ersetzungsskript mit expliziter Wörterliste; englische Termini (gross proceeds, business, issued, less, loss, passu, Voss, Stein, Goetheplatz, ...) bleiben unangetastet. 17 Dateien geändert.
- **Agio-Dogmatik in drei Plugins.** Echtes/korporatives vs. unechtes/schuldrechtliches Agio bei der GmbH; § 3 Abs. 2 GmbHG mit Dauerwirkung auch bei Kapitalerhöhung; Differenzierung nach Fälligkeit (Fall 1 keine Satzungsaufnahme erforderlich, Fall 2 Eintragungshindernis bei Nichtaufnahme); Sachagio im Rahmen des qualifizierten Anteilstauschs § 21 UmwStG; § 272 Abs. 2 Nr. 1 vs. Nr. 4 HGB; § 27 KStG steuerliches Einlagekonto. Rechtsprechung verifiziert: BGH II ZR 216/06; BGH BGHZ 80, 129; BGH BGHZ 71, 40 (Kali+Salz); BFH I R 53/08; BFH IX R 12/22.
  - **Neuer Skill `gesellschaftsrecht/skills/agio-und-kapitalruecklage`** mit voller Dogmatik, Praxismuster-Formulierungen, US-Term-Sheet-Übersetzung und Anfängerfehler-Katalog.
  - **Neuer Skill `corporate-kanzlei/skills/corporate-kanzlei-agio-und-kapitalerhoehungsstruktur`** mit Schnittstellen-Management (Notar, Steuerberater, Investor Counsel, CFO), Strukturierungsentscheidungen und Streitpunkten in der Praxis.
  - **Neue Testakten-Datei `24-agio-und-kapitalruecklage-streitfrage.md`** in der Frankfurt-Testakte mit Mandatsbezug (Kometenfalter Series A), Notiz Adelheid von Westarp an Hildemar K., US-Term-Sheet-Bezug (Original Purchase Price, Par Value, APIC, Liquidation Preference) und Aufgabenkatalog für den Associate.
- **Plugin-Versionsbump.** `gesellschaftsrecht` 29.0.0 → 30.0.0; `corporate-kanzlei` 29.0.0 → 30.0.0; `gesellschaftsrecht-legal-english` 34.0.0 → 35.0.0 in den jeweiligen `<plugin>/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Forbidden-Frontmatter-Check: keine Treffer
- description-Längen ≤ 1024 Zeichen, Skill-Namen ≤ 64 ASCII
- Verifikation aller Rechtsprechungs-Zitate über dejure.org und bundesfinanzhof.de

---

# v34.0.0 - Corporate Legal English didaktisiert, Multi-Format-Testakte

- **`gesellschaftsrecht-legal-english` didaktisch nachgeschärft.** Der `allgemein`-Skill startet jetzt mit einem echten 90-Sekunden-Kaltstart: Sofortdiagnose, Erfahrungslevel, drei Rückfragen, Skill-Routing und Mini-Arbeitsprodukt. Der `rookie-modus` wurde vom bloßen Prüfraster zum Lerncoach mit 30-Minuten-Plan, Begriffskarten, Mini-Übungen und klaren Senior-Review-Gates.
- **Zwei neue Skills.** `lernpfad-dealroom-simulator` führt Anfänger durch mehrteilige Transaktionsakten mit Materialinventar, Dealkarte, Lernpfad, Übungen und Arbeitsprodukt. `anschauungsmaterial-multiformat-auswertung` wertet Excel, PDF, Scan, Screenshot, JPEG, Chat, Email und Dealroom-Fragmente quellenkritisch aus.
- **Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` weiter ausgebaut.** Neu: WhatsApp-Thread als Markdown, Multi-Format-Index, echtes Excel-Trainingsmodell (`18-cap-table-waterfall-training.xlsx`), PDF-Scan zur Beurkundungssprache, Whiteboard-Foto, Investor-Email-Screenshot, WhatsApp-Screenshot und Rookie-Cheatsheet als PDF.
- **Dokumentations- und Versionspflege.** Plugin-README, Testakten-README, Root-README, SKILLS-Übersicht, Marketplace und Plugin-Manifest aktualisiert; `gesellschaftsrecht-legal-english` auf `34.0.0` gesetzt.

## Qualitätssicherung

- `git diff --check`
- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- JSON-Manifest-Parse aller Plugin-Manifeste
- Multi-Format-Sanity: XLSX mit `openpyxl`, PDFs mit `pypdf`, JPEGs mit `PIL` geöffnet

---

# v33.0.0 — Corporate Legal English Testakten-Ausbau, Codex-Klarstellungen

- **Corporate Legal English Testakte massiv ausgebaut.** `testakten/gesellschaftsrecht-legal-english-frankfurt-startup/` von 7 auf 16 Dateien erweitert. Neue Dateien: `00-deal-personen-und-zeitleiste.md` (Cast, Zeitleiste, fiktive Eckdaten), `08-glossar-deutsch-englisch-fallstricke.md` (zwoelf Begriffspaare mit typischen Missverstaendnissen), `09-anfaengerfehler-katalog-mit-partner-rotstift.md` (fuenf Fehlerklassen mit Vorher/Nachher), `10-wandeldarlehen-tante-ermelind.md` (vollstaendiger Convertible Loan mit Discount 20 Prozent, Cap 10 Mio. EUR, 8 Prozent PIK), `11-investor-counsel-markup-roundtrip.md` (Markup-Email Brackenmuir & Quint LLP, interne Sortierung, 02:14-Uhr-Antwort), `12-notar-checkliste-und-handelsregisterlogik.md` (Notariat Schwartz, § 5 BeurkG, Einheitsdoktrin, § 40 GmbHG), `13-side-letter-und-information-rights.md` (Stahlauge Seed Side Letter, Northbridge Series A Side Letter), `14-board-und-consent-matters-mapping-de-en.md` (zehn Reserved Matters mit DE-Umsetzung), `15-closing-checkliste-cp.md` (30 CPs, Gap-Analyse, Post-Closing). Bestandsdateien 01 bis 07 substantiell ausgebaut (Term Sheet jetzt mit vollstaendigem Definitions-Set, SHA-Synopse Seed/Series A, DD-Index mit Datenraumstruktur, Associate-Notiz mit Partner-Rotstift, Pruefraster 100 Punkte).
- **README der Testakte neu strukturiert** mit Lernpfaden A (Begriffsdisziplin, 2 Stunden), B (Mandatsanalyse, 4 Stunden), C (Vertiefung, 4 bis 6 Stunden) und D (Mandantenkommunikation, 1 bis 2 Stunden).
- **Plugin-Versionsbump.** `gesellschaftsrecht-legal-english` von 24.1.0 auf 25.0.0 in `<plugin>/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json`.
- **Codex-PR-Klarstellung Direktwirkung EU-Lohntransparenzrichtlinie** in `fachanwalt-arbeitsrecht/skills/fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich/SKILL.md`. Praxishinweis: vertikale Direktwirkung gegenueber oeffentlichen Arbeitgebern (Van Duyn 41/74, Becker 8/81, Marshall 152/84) ab 07.06.2026, horizontale Direktwirkung gegenueber privaten Arbeitgebern grundsaetzlich ausgeschlossen (Marshall 152/84, Dansk Industri C-441/14); richtlinienkonforme Auslegung (Marleasing C-106/89) und Francovich-Staatshaftung (C-6/90, C-9/90) bleiben.
- **Codex-PR-Klarstellung BVerfG 1 BvR 183/25** in `mietrecht/skills/mietspiegel-quellen/SKILL.md`. Der Nichtannahmebeschluss vom 08.01.2026 betrifft die 2020er Verlaengerung der Mietpreisbremse (§ 556d BGB in der Fassung vom 19.03.2020) und die Berliner Mietenbegrenzungsverordnung vom 19.05.2020, nicht das Verlaengerungsgesetz vom 17.07.2025 (BGBl. 2025 I Nr. 163, Geltung bis 31.12.2029). Verfassungsgerichtliche Pruefung der 2025er Verlaengerung steht noch aus.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Grep auf verbotene Frontmatter-Felder — 0 Treffer

---

# v29.0.1 — EU-Richtlinien-Nachzug, GVG-Streitwert ab 01.01.2026, Mietpreisbremse-Verlaengerung

- **EU-Lohntransparenzrichtlinie 2023/970 nachgetragen** in `arbeitsrecht/skills/bag-equal-pay-paarvergleich-8azr30024/SKILL.md` und `fachanwalt-arbeitsrecht/skills/fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich/SKILL.md`. Neue Bloecke fassen Art. 5 (vorvertragliche Transparenz, Verbot Gehaltshistorie), Art. 7 (Auskunft binnen zwei Monaten), Art. 9 (Berichtspflichten ab 250 / 150 / 100 Beschaeftigten), Art. 10 (gemeinsame Bewertung ab fuenf Prozent Gefaelle), Art. 16 (Schadensersatz ohne Obergrenze), Art. 18 (Beweislastumkehr bei Pflichtverletzung) und Art. 21 (Verjaehrung mindestens drei Jahre) zusammen. Umsetzungsfrist 07.06.2026; nationale Umsetzung steht zum Stand Mai 2026 noch aus. Quelle: https://eur-lex.europa.eu/eli/dir/2023/970/oj
- **EU-Plattformarbeitsrichtlinie 2024/2831 ausgearbeitet** in `arbeitsrecht/skills/arbeitnehmer-status/SKILL.md`. Einzeiler aus v29 ersetzt durch ausgearbeiteten Block mit Vermutungsregel zugunsten des Beschaeftigungsverhaeltnisses, Beweislastumkehr und Umsetzungsfrist 02.12.2026. Quelle: https://eur-lex.europa.eu/eli/dir/2024/2831/oj
- **Mindestlohn ab 01.01.2026 / 01.01.2027 verifiziert** mit Fundstelle Fuenfte MindestlohnAnpassungsverordnung vom 05.11.2025, BGBl. 2025 I Nr. 268 — in `arbeitsrecht/skills/allgemein/SKILL.md` und `arbeitsrecht/skills/mindestlohn-arbeitszeit-erfassung/SKILL.md`. 13,90 EUR ab 01.01.2026; 14,60 EUR ab 01.01.2027.
- **GVG-Streitwertgrenze korrigiert** in `mietrecht/skills/klageentwurf-amtsgericht/SKILL.md`. Frontmatter und Body benennen jetzt das Gesetz zur Staerkung der Amtsgerichte in Zivilsachen (Bundesrat-Billigung 21.11.2025, Inkrafttreten 01.01.2026) statt der falschen "Justizmodernisierung 2024". Anwaltszwang ebenfalls ab zehntausend Euro; Berufungsbeschwer in § 511 Abs. 2 Nr. 1 ZPO von 600 auf 1.000 Euro angehoben. Uebergangsregelung: vor 01.01.2026 anhaengige Verfahren bleiben bei fünftausend Euro. Quelle: BRAK-Nachrichten 24/2025 vom 26.11.2025.
- **BGH-Rechtsprechung zur Zahlungsverzugskuendigung ergaenzt** in `mietrecht/skills/mahnung-zahlungsverzug-mieter/SKILL.md`: BGH, Urt. v. 01.07.2020 – VIII ZR 323/18 (Schonfristzahlung beseitigt nur die fristlose Kuendigung, hilfsweise ordentliche bleibt wirksam; § 574 Abs. 1 Satz 2 BGB ausgeschlossen) und BGH, Beschl. v. 08.12.2021 – VIII ZR 32/20 (Erheblichkeit nach § 573 Abs. 2 Nr. 1 BGB anhand der Gesamthoehe des Rueckstands). VIII ZR 287/23 vom 09.07.2025 aus v29 unveraendert erhalten.
- **Mietpreisbremse-Verlaengerung dokumentiert** in `mietrecht/skills/mietspiegel-quellen/SKILL.md`. Neuer Block zum Verlaengerungsgesetz vom 17.07.2025 (BGBl. 2025 I Nr. 163, § 556d Abs. 2 Satz 4 BGB bis 31.12.2029) sowie BVerfG-Nichtannahmebeschluss vom 08.01.2026 – 1 BvR 183/25 (Verfassungsbeschwerde gegen die Verlaengerung erfolglos; Bestaetigung der Linie aus 1 BvL 1/18).
- **Versionsbump.** `arbeitsrecht`, `fachanwalt-arbeitsrecht` und `mietrecht` auf `29.0.1` in `<plugin>/.claude-plugin/plugin.json` und in `.claude-plugin/marketplace.json`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v24.2.0 — References-Einzelfix und UNVERIFIABLE-Online-Check

- **Welle 5 — References-Einzelfix.** Die 16 in v24.1.0 noch offenen toten `references/`-Verweise einzeln durchgegangen. 14 waren falsch-positiv (Aufloesungspfade, ASCII-Tree-Beispiele, generierte Skills). 1 echter Bug gefixt: `produktrecht/skills/produktrecht-kaltstart-interview` verwies auf `references/launch-pruefung-framework-de.md`, korrigiert auf den realen Pfad `produktrecht/skills/launch-pruefung/references/seven-category-framework.md`. 2 Laufzeit-Cache-Verweise (`kanzlei-builder-hub`: `registry-cache.json`, `surfaced.json`) durch leere `references/`-Verzeichnisse mit `README.md`-Hinweis dokumentiert.
- **Welle 6 — UNVERIFIABLE-Online-Check.** Die 893 in Welle 2 als UNVERIFIABLE markierten Aktenzeichen wurden online gegen dejure.org, BGH-/BAG-/BFH-/BSG-Datenbanken, Curia, openJur und Landesjustizportale geprueft (20 parallele Batches a ~45 AZ). Ergebnis: 148 rehabilitiert, 621 in Schnellrunde nicht auffindbar, 30 widerspruechlich, 94 uebersprungen. Konservative Strip-Strategie (Welle-1-NOT_FOUND + Original-Audit-Negativ-Marker, ohne positive Hinweise) lieferte 7 sichere Loeschkandidaten – alle bereits durch v24.1.0 entfernt. Welle 6 entfernt netto keine weiteren Zeilen, liefert aber die konsolidierte Klassifikation in `audit/welle2_unverifiable_audit_2026-05-29.json` und die 20 Roh-Batches in `audit/unverifiable_batches/` als Grundlage fuer kuenftige Reparaturwellen.
- **Audit-Bericht erweitert.** `audit/README.md` enthaelt jetzt sechs Wellen mit Methodik und Befunden.
- **Versionsbump.** Alle 103 Plugins (inkl. neuer `meinungspruefer`), Marketplace-Top-Level und alle Marketplace-Plugin-Eintraege einheitlich auf `24.2.0`.
- **Neues Plugin `meinungspruefer`** mit 36 Skills zur Pruefung von Aeusserungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung/Tatsache, Beleidigung, ueble Nachrede, Verleumdung, § 188 StGB, § 193 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR-/EuGH-Rechtsprechung, OLG-/KG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Arbeitsplatz, Schule und kommunale Machtkritik. Rechtsprechungsbank mit frei pruefbaren Quellen und ohne BeckRS-/Kommentar-/Aufsatz-Blindzitate.
- Neue Testakte **`meinungspruefer-grenzfaelle-alltag`** mit X-Post zum kommunalen Bauprojekt, LinkedIn-Pinocchio, Kantinenaeusserung ueber Zahlen, Elternchat, Buergermeister-"Lackaffe", Abmahnung, polizeilicher Anhoerung, Belegmappe und USA-Vergleichsnotiz.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v24.1.0 — AZ-Strip, Konversationsstil und LG Aachen 10 O 306/25

- **Welle 3 — Halluzinations-AZ entfernt.** Die im Vollaudit (`audit/audit_problems_2026-05-27.json`) als WRONG_TOPIC oder NOT_FOUND klassifizierten 969 Aktenzeichen wurden aus den betroffenen SKILL.md gestrichen. Ergebnis: 175 Dateien geaendert, 392 Zeilen entfernt; YAML-Frontmatter blieb unangetastet. Dokumentiert in `audit/README.md` und `audit/references_audit_2026-05-29.json`.
- **Welle 4 — References-Konsistenz.** 17 tote Markdown-Verweise auf `references/`-Dateien identifiziert; einer (`rechtsberatungsstelle/.../pruef-warteschlange.yaml` → `review-queue.yaml`) gefixt. Die restlichen 16 sind in `audit/references_audit_2026-05-29.json` dokumentiert.
- **Konversationsstil-Update.** `CLAUDE.md` und alle 102 `<plugin>/skills/allgemein/SKILL.md` erhalten einen verbindlichen Block: erste Antwort konzis, hoechstens eine unverzichtbare Rueckfrage, dann schnell zur Dokumentenproduktion. Ausfuehrlich nur bei echter Subsumtion, Tabellen, Risikoanalysen oder Schriftsatz-/Memo-Text. Allgemein-Skills sind Einstieg, nicht Vorlesung.
- **Frontmatter-Konvention geschaerft.** `CLAUDE.md` listet jetzt die verbotenen Frontmatter-Felder explizit (`triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **LG Aachen 10 O 306/25 (Urteil vom 27.05.2026) als Leitentscheidung aufgenommen** in: `bgb-at-pruefer/.../kauf-im-internet-und-auktionen`, `bgb-at-pruefer/.../gesetzesverbot-sittenwidrigkeit-paragraphen-134-138`, `vertragsrecht/.../vertragspruefung`, `produktrecht/.../feature-risikobewertung`. Inhalt: Button-Beschriftung "Wette abgeben" beim Online-Gluecksspiel genuegt nicht § 312j Abs. 3 BGB; endgueltige Unwirksamkeit nach Abs. 4; Rueckabwicklung nach § 812 BGB unabhaengig von Lizenz. Quellenhinweis: offizieller Volltext zum Aufnahmezeitpunkt noch nicht oeffentlich; Aufnahme erfolgte auf Basis Pressehinweis Gamesright GmbH / rightmart, 28.05.2026.
- **Audit-JSON-Fix bewahrt.** Zwei unescapte Quotes (Z. 425, 7661) aus dem Vollaudit-JSON sind gefixt (bereits in v24.0.0 als Commit `5b0676ef` gepusht).

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Alle 102 Plugins, Marketplace-Top-Level und alle Marketplace-Plugin-Eintraege einheitlich auf `24.1.0`

---

# v24.0.0 — Einheitliche Versionsbasis und vollständige Codex-Integration

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` einheitlich auf Version `24.0.0` gezogen. Damit sind erstmals seit mehreren Releases sämtliche Manifeste, der Marketplace-Top-Level und alle Marketplace-Plugin-Einträge auf identischer Versionsnummer.
- Sämtliche Codex-Pull-Requests (Selbstvertreter Amtsgericht und Sozialgericht, Lobbyregister Bundestag, Wertgrenzen 2026 nach Justizstandort-Stärkungsgesetz, 150 Steuerberater-Skills BWA/Lohn/DBA) sind in `main` integriert und im Release enthalten.
- YAML-Frontmatter-Hygiene aus v23.0.1 vollständig übernommen: 47 SKILL.md-Frontmatter und ein verbliebener Plugin-Root-CLAUDE.md-Bug aus dem ASCII-Quote-Sweep sind bereinigt; alle Skills passieren den offiziellen `claude plugin validate --strict`.
- Validatoren erweitert: `scripts/validate-yaml-frontmatter.py` (echter pyyaml-Parse-Check inklusive Komma-Zahl-Sequenzen) und `scripts/validate-with-claude-cli.sh` (Wrapper für offizielles `claude plugin validate --strict`).

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- `./scripts/validate-with-claude-cli.sh` (offizielle Anthropic CLI v2.1.153)
- `git diff --check`

---

# v23.0.1 — Download-Abdeckung und Quellenhygiene

- Alle 102 Plugin-READMEs geprüft: jedes Plugin nennt sein Plugin-ZIP aus dem `latest`-Release.
- Alle 57 Testakten sind im Testakten-Index mit ZIP-Download eingetragen; jede Testakte ist aus mindestens einem passenden Plugin-README verlinkt.
- Die zentrale README-Übersicht nennt alle 102 Plugins, inklusive `liquiditaetsplanung` und der beiden Selbstvertreter-Plugins.
- Zitierweise v4.0 repo-weit nachgezogen: keine BeckRS-, Kommentar-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei/amtlich oder per lizenziertem Live-Zugriff verifizierter Quelle.
- Unsichere oder nicht frei belegte Rechtsprechungs- und Literaturzeilen in Skills, README-Texten, Generatorvorlagen und Beispiel-Hausregeln durch Live-Verifikationshinweise ersetzt.
- Alle Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `23.0.1` gezogen; der `v23.0.0`-Stand bleibt enthalten.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Zusatzcheck: 102/102 Plugin-READMEs mit Plugin-ZIP, 57/57 Testakten-ZIPs im Index und aus Plugin-READMEs erreichbar, 0 unsichere Zitations-Treffer im engeren Audit.
- lokaler Build und Validierung aller Plugin- und Testakten-ZIPs mit `scripts/validate-release-zips.py`

---

# v23.0.0 — Selbstvertreter-Ausbau und ASCII-Anführungszeichen

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `23.0.0` gezogen.
- Beide Selbstvertreter-Testakten (`selbstvertreter-amtsgericht-kuechentisch-kaufpreis` und `selbstvertreter-sozialgericht-heizkosten-eilantrag`) deutlich ausgebaut: je drei neue Dokumente, alle bestehenden Dateien stark erweitert, mittlerer bis höherer Schwierigkeitsgrad. Neu in der Amtsgericht-Akte: AGB-Klauseln zur Prüfung, privat eingeholte Voreinschätzung eines Tischlermeisters, Foto-Inventar mit EXIF-Metadaten, zehn widersprüchliche Internet-Treffer. Neu in der Sozialgericht-Akte: vollständiger Bürgergeld-Bescheid mit Berechnungsblatt, Attest mit Mindesttemperaturangabe wegen kindlichem Asthma, vier Telefonnotizen, KdU-Konzept der Stadt Leipzig.
- Beide Selbstvertreter-Plugins `selbstvertreter-amtsgericht` und `selbstvertreter-sozialgericht` in der Plugin-Übersichtstabelle im Root-README ergänzt (waren bislang versehentlich nicht in der Tabelle).
- Steuerrecht-Plugin: Plugin-README-H1 von "Steuerrecht für Anwaltschaft und Steuerberatung" auf "Steuerrecht - Steuerberater und Anwälte" geändert (Slug `steuerrecht-anwalt-und-berater` bleibt — keine Breaking Changes).
- Repo-weiter Sweep: alle typografischen Anführungszeichen (`"` `"` `'` `'` `"` `"`) durch ASCII `"`/`'` ersetzt in 909 Dateien. Verhindert HTML-Entity-Darstellung (`&#x201E;` etc.) in Plugin-Outputs bei Clients, die Markdown durch HTML-Escaping schicken.
- Stand jetzt 102 Plugins, 2410 Skills und 55 Testakten.

---

# v22.0.0 — Nachbarschaftsstreit, US-Transfer-TIA, KI-VO-Evidence-Pack

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `22.0.0` gezogen.
- Neues Plugin **`nachbarschaftsstreit-pruefer`** mit 19 Skills zum Nachbarrecht: Überbau (§§ 912-916 BGB), Überhang (§ 910 BGB), Grenzbaum/Grenzanlage (§§ 921-923 BGB), Einfriedung, Immissionen (§ 906 BGB), Notweg (§§ 917-918 BGB), Vertiefung/Baugrube (§ 909 BGB), Hammerschlagsrecht, Landesnachbarrecht-Router, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung und Vergleich. Mit zwölfteiliger Testakte `nachbarschaftsstreit-horrorfall-rosengarten`.
- Drei neue Datenschutz-Skills im Plugin `datenschutzrecht`: `us-transfer-tia-dokumentation`, `standardvertragsklauseln-scc-paket`, `drittlandtransfer-behoerdenpaket-output`. Mit Testakte `datenschutz-us-transfer-cloudsuite-rheinmain` (CloudSuite Assist, DPF-Lücke, SCC Modul 2, hbDI-Antwortentwurf).
- Neuer KI-VO-Skill `output-konformitaetsbescheinigung-evidence-pack` mit Statusleiter Final/Entwurf/Readiness/Drittstelle, EU-Konformitätserklärung nach Art. 47 / Anhang V, Evidence Index und Lückenliste. Mit Testakte `ki-vo-konformitaetsbescheinigung-bewerberpilot`.
- Bereicherungs- und Arbeitsrecht-Cleanup: URL-Konsistenz `claude-fuer-deutsches-recht` und ASCII-Slugs in den Direkt-Download-Tabellen, Skill-Slugs in Plugin-README-Tabellen ohne Umlaute.
- Direkt-Download-Blöcke in den beiden neuen Testakten-READMEs analog zu den 53 anderen.
- Stand jetzt 102 Plugins, 2410 Skills und 55 Testakten.

---

# v21.0.0 — Direkt-Downloads und Bereicherungsrecht-Cleanup

- Alle 101 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `21.0.0` gezogen.
- 52 Testakten-Unterordner-READMEs mit sichtbarem Direkt-Download-Button für die jeweilige ZIP-Datei aus dem `latest`-Release.
- 13 Plugin-READMEs mit eigenem **Zum Ausprobieren: Testakte**-Block und Direkt-Download-Link: `arbeitszeugnis-analyse`, `bgb-at-pruefer`, `fachanwalt-arbeitsrecht`, `fachanwalt-sozialrecht`, `fachanwalt-verwaltungsrecht`, `gesellschaftsrecht`, `grosskanzlei-corporate-ma`, `insolvenzrecht`, `jveg-kostenpruefer`, `kanzlei-allgemein`, `liquiditaetsplanung`, `lobbyregister-bundestag`, `steuerrecht-anwalt-und-berater`.
- Bereicherungsrecht-Cleanup: 77 Skills mit Umlaut- und Typo-Reparatur, 50 Skills mit vollständig ausgebauten Aktivierungs-Descriptions im Muster Trigger + Normen + Prüfraster + Output + Abgrenzung.
- Stand bleibt 101 Plugins, 2386 Skills und 52 Testakten.

---

# v20.0.0 — Release 20 Gesamtstand

- Alle 101 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `20.0.0` gezogen.
- `README.md` und `testakten/README.md` auf Release `v20.0.0` aktualisiert; Stand bleibt 101 Plugins, 2332 Skills und 52 Testakten.
- Inhaltlicher Stand aus `v19.1.0` bleibt enthalten: BGB-AT-Prüfer mit qES-/beA-/Formfiktion-Workflow, Arbeitszeugnis-Testakte, Legistik-Ausbau und die bisherigen Qualitätsbereinigungen.

---

# v19.1.0 — BGB AT, Arbeitszeugnis-Testakte und Legistik-Ausbau

- Neues Plugin `bgb-at-pruefer` mit 53 Skills zum BGB Allgemeiner Teil: Fallaufnahme, Anspruchsaufbau, Willenserklärung, Zugang, Vertragsschluss, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung.
- `bgb-at-pruefer` um einen eigenen qES-/beA-/Formfiktion-Skill erweitert: §§ 126, 126a, 130 BGB, § 130e ZPO, § 46h ArbGG, § 173 ZPO und BGH VIII ZR 155/23 / VIII ZR 159/23 werden jetzt als gemeinsamer BGB-AT-/Prozessrechts-Workflow geprüft.
- Neue synthetische Testakte `bgb-at-altfraenkische-werkstatt` mit Online-Auktion, Annahmefrist, Minderjährigenkauf, Vollmacht, Anfechtung, Bedingung, Form-/Sittenwidrigkeitsprüffeldern und beA-/qES-/Formfiktion-Nachtrag.
- Neue Testakte `arbeitszeugnis-analyse-bluehendes-leben` mit zehn vollständigen Arbeitszeugnissen aus zehn Branchen (PTA Apotheke, angestellter Anwalt, MTRA Radiologie, Lagermeister, ZFA, Filialleiterin Sparkasse, Speditionsdisponent, Hotel-Empfangsleiter, Wohnbereichsleitung Pflege, Industriemechanik); tatsächliche Noten verdeckt über gesamte Skala eins bis fünf, ohne Musterlösung.
- `methodenlehre-buergerliches-recht` und `subsumtions-pruefer` verweisen nun auf `bgb-at-pruefer`, wenn die abstrakte Methodik in konkrete BGB-AT-Mechanik überführt werden soll.

- Legistik-Werkstatt auf fünf Startbahnen erweitert: Bundesressort/Bundesregierung, Bundestag/Fraktion/Opposition, Landesressort/Landesregierung, Landtag/Landtagsfraktion und sonstige Normgeber.
- Legistik-Allgemein-Skill fragt jetzt Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Verfahrensstand, Drucksache, Geschäftsordnung und Outputformat ab und routet sauber in Spezial-Skills.
- `formulierungshilfe-bauen` kann jetzt nicht nur ministerielle Koalitions-Zulieferungen, sondern auch Gesetzentwürfe aus der Mitte, Änderungsanträge, Anträge und Entschließungsanträge für Bundestag und Landtage einschließlich Oppositionsarbeit.
- `legistik-auftragsaufnahme`, `normhierarchie-routing` und `referentenentwurf-bauen` trennen fachlichen Verfasser, formalen Initiator und politischen Auftraggeber und führen Landesverfassung, Landes-Geschäftsordnung, Landtags-GO und Verkündungsrecht als Pflichtprüfpunkte mit.
- Perplexitys stummer Upload-Block in allen 100 Allgemein-Skills geglättet: Fristenscan zuerst, Materialklassifikation, Kontextanker, Skill-Routing, nur eine konkrete Rückfrage und ein weniger begrenzender Co-Pilot-Ton.
- Testakten mit `.placeholder`-Dateinamen in Chatbeschreibungen, Bildbeschreibungen, Fehlblätter, Inhaltsvermerke und Validierungsnotizen umbenannt; README-Verweise entsprechend aktualisiert.
- Produktrecht-Skills von offenen Verify-/Pinpoint-Markern, einer nicht tragfähigen Produkthaftungsfundstelle und schematischen Influencer-/Green-Claims-Aussagen bereinigt.
- KI-Governance-Beispiele auf Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO für Bewerbungs-/Beschäftigungssysteme korrigiert und die allgemeine Chatbot/GPAI-Abgrenzung geschärft.
- BVerfG-Leitentscheidung "Soldaten sind Mörder" mit den konkreten Aktenzeichen ersetzt; Quellenhinweis auf geprüfte Primärquellen und Pinpoint-Nachtrag umgestellt.

---

# v19.0.0 — KI-VO-Härtung, BVG-Abschleppakte und Release-Stand

- `ki-vo-ai-act-pruefer` vertieft Art. 3 Nr. 1 KI-VO mit einem dokumentierbaren KI-System-Vermerk zu Automation, Autonomie, Adaptivität, Inferenz, Output und Umgebungseinfluss.
- Art. 6 Abs. 2 i.V.m. Anhang III ist neu aufgebaut: alle acht Bereiche mit Untertatbeständen, Zweckbestimmung, allgemeiner Chatbot/GPAI-Abgrenzung und Mitarbeitenden-Fehlgebrauch.
- Allgemeine Chatbots/GPAI werden ausdrücklich nicht automatisch als Hochrisiko behandelt; maßgeblich sind Anbieter-Zweckbestimmung, Betreiberzweck und tatsächliche Integration in Anhang-III-Prozesse.
- Art. 6 Abs. 3 wurde mit Profiling-Sperre, vier Fallgruppen, Grundrechtsrisiko und Art.-6-Abs.-4-Dokumentation geschärft.
- Normen-/Standards-Skill trennt harmonisierte Normen, gemeinsame Spezifikationen, GPAI Code of Practice und ISO/IEC-Standards ohne falsche Vermutungswirkung.
- Output-Dokumentation enthält jetzt Art.-3-Vermerk, Anhang-III-Matrix, Off-label-Governance, Re-Evaluation-Trigger und Standards-Hinweis.
- Perplexitys BVG-/ÖPNV-Abschleppmaterial ist in `main` integriert: neuer Verwaltungsrechts-Skill `fa-vwgo-widerspruchsbescheid-abschleppen-oepnv` und neue Testakte `bvg-widerspruchsstelle-abschleppen-mobg`.
- Die BVG-Testakte verwendet nun Lichtbildbeschreibungen statt Platzhalterdateien; die VG-Berlin-Fundstelle ist auf Urteil vom 30.05.2022, VG 11 K 298/21, mit Pressemitteilung vom 04.07.2022 korrigiert.
- `README.md`, `SKILLS.md`, `testakten/README.md` und der Allgemein-Skill des Verwaltungsrechts-Plugins spiegeln nun 2279 Skills, 50 Testakten und das neue Routing zum BVG-Widerspruchsbescheid wider.
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `19.0.0`.
- `README.md` und `testakten/README.md` auf Stand 101 Plugins, 2331 Skills, 52 Testakten und Release `v19.1.0` aktualisiert.

---

# v18.0.0 — Allgemein-Skills als schöne Plugin-Einstiege

Version 18.0.0 ist ein repo-weiter Workflow-Release: Jedes Plugin hat nun einen eigenen `allgemein`-Einstiegsskill als schnellen Intake-, Workflow- und Routingpunkt.

- 34 fehlende `skills/allgemein/SKILL.md` neu angelegt.
- 66 vorhandene Allgemein-Skills mit einheitlichem Schnellstart-Workflow, Intake in 60 Sekunden, Sofort-Triage, Antwortformat und Routing-Regeln ergänzt.
- Jeder Allgemein-Skill enthält eine automatisch aus dem jeweiligen Plugin gezogene Liste der verfügbaren Spezial-Skills und soll bei Bedarf zwei bis fünf passende Folge-Skills mit Grund und erwartetem Output vorschlagen.
- `SKILLS.md` und README-Zählungen auf 2278 Skills aktualisiert.
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `18.0.0`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Zusatzcheck: 100 Plugins, 2278 Skills, 100 Allgemein-Skills mit Schnellstart-Workflow
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v17.5.1 — Insolvenzanfechtung-Audit, KI-Screening und Verteidigung

Version 17.5.1 ist ein gezielter Nachlauf nur für Insolvenzanfechtungsrecht. Der Schwerpunkt liegt auf den fehleranfälligen Normgruppen §§ 129, 130/131, 133, 134, 135, 142 und §§ 143-147 InsO, dem Reformstand nach der Anfechtungsreform 2017, den Fristen, dem Bargeschäft, Gesellschafterdarlehen und der Verteidigung des Anfechtungsgegners.

## Korrigiert und gehärtet

- **§§ 130/131 InsO:** kongruente und inkongruente Deckung wurden sauber getrennt; § 130 verlangt Kenntnis, während § 131 die objektive Monats-/Antragsnähe und die subjektiven Alternativen für den zweiten und dritten Monat abbildet.
- **§ 133 InsO:** Vorsatzanfechtung arbeitet nun mit Zehnjahresgrundtatbestand, Vierjahresfenster für Deckungshandlungen, Zahlungsvereinbarungsregel und der Zweijahresvariante für entgeltliche Verträge mit nahestehenden Personen.
- **§ 142 InsO:** Bargeschäft ist nicht mehr als starre 30-Tage-Regel beschrieben; die Skills prüfen unmittelbaren Leistungsaustausch nach Verkehrsauffassung, das Drei-Monats-Fenster für Arbeitsentgelt und die Sondergrenze bei § 133 InsO.
- **§ 135 InsO:** neuer eigener Skill für Gesellschafterdarlehen, Gesellschaftersicherheiten, Rückzahlungen, Besicherungen, Kleinbeteiligungs-/Sanierungsprivileg und Drittfinanzierungsvarianten.
- **§§ 143-147 InsO:** Rechtsfolgen, § 144 InsO, Rechtsnachfolge, Verjährung und Handlungen nach Verfahrenseröffnung wurden neu geordnet; Zinsen werden an § 143 Abs. 1 Satz 3 InsO, Verzug und § 291 BGB angebunden.
- **Verteidigung des Anfechtungsgegners:** neuer eigener Skill mit defensiver Matrix zu Normauswahl, Gläubigerbenachteiligung, Kenntnis, Bargeschäft, Entreicherung, § 144 InsO, Verjährung und Vergleich.

## KI-Anfechtungsworkflow

- Neuer Skill `inso-ki-anfechtungsansprueche-schuldnerakten` für die Auswertung von Schuldnerakten mit Quellenankern, Zahlungschronologie, Anfechtungskandidaten-Matrix, Human-Review-Markierungen und Evidenzlücken.
- Das System darf Anfechtungskandidaten identifizieren und strukturiert vorprüfen, ersetzt aber keine anwaltliche Wertung bei § 133 InsO, Gläubigerbenachteiligungsvorsatz, Kenntnisindizien, Sanierungsversuchen, Bargeschäftsverteidigung und komplexen Dreiecksverhältnissen.
- Insolvenzverwaltung und Fachanwalt-Insolvenz/Sanierung wurden mit demselben Prüfungsmaßstab synchronisiert, damit Verwalterseite, Klagevorbereitung und Verteidigung nicht auseinanderlaufen.

## Release-Stand

- 100 Plugins
- 2244 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `17.5.1`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- gezielte Suche nach alten Fehlmustern zu SanInsFoG/Reform 2017, § 130/§ 131, § 133, § 142, § 146 und § 135 InsO
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v17.5.0 — Text-/Quellenaudit, README-Gateway-Anleitung und Lobbyregister-API-Härtung

Version 17.5 finalisiert den nachgezogenen Hauptstand nach v17 und zieht die Repository-Dokumentation, Plugin-Versionen und Release-Artefakte auf einen einheitlichen Zwischenrelease. Schwerpunkt ist ein konservativer Qualitätsschnitt: weniger erfundene Fundstellen, bessere deutsche Beschreibungstexte, klarere README-Anleitung für alternative Claude-kompatible API-Endpunkte und ein belastbareres Lobbyregister-Plugin.

## Korrigiert und gehärtet

- **Rechtsprechungs- und Literaturhinweise:** mehrere falsch oder unsicher zugeordnete BGH-/Kapitalmarkt-/Corporate-Nachweise wurden entfernt oder durch passendere, überprüfbare Leitentscheidungen ersetzt; methodische Skills sollen nicht mehr mit frei erfundenen Aktenzeichen arbeiten.
- **Lobbyregister Bundestag:** die API-Hinweise wurden als lesende Kontroll- und Monitoring-Schicht geschärft. Mock-Artefakte verweisen auf den stabilen `current`-Schema-Pfad und dokumentieren den Stand `R2.21`, statt eine spekulative neue API-Version zu behaupten.
- **README:** die Anleitung zum Einhängen einer eigenen oder zwischengeschalteten Claude-/Anthropic-kompatiblen API wurde providerneutral neu gefasst, mit klarer Trennung zwischen Claude Code im Terminal und Desktop-/Cowork-Oberflächen.
- **Deutsche Beschreibungstexte:** Frontmatter-Descriptions und Marketplace-Texte wurden breit auf Umlaute, ß und lesbare deutsche Formulierungen bereinigt, ohne Pfade, Links oder technische IDs umzubenennen.
- **Testakten:** Lobbyregister-Testakten bleiben bewusst realistisch-fragmentarisch, enthalten aber keine spekulativen API-Abgabeversprechen. Die API wird für Suche, Exportvergleich, Monitoring und Plausibilisierung genutzt.

## Release-Stand

- 100 Plugins
- 2241 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `17.5.0`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- JSON-Parsing der geänderten Lobbyregister-API-Mockdateien
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v16.0.0 — Halluzinationsbereinigung, Audit-Hardening und v15-Finalstand

Version 16 baut direkt auf `v15.0.0` auf und nimmt den dortigen Stand mit Lobbyregister-Plugin, Selbstvertreter-Plugins und Steuerberater-Werkzeugen vollständig mit. Der Schwerpunkt dieses Releases ist eine weitere Qualitätsschicht gegen erfundene oder falsch zugeordnete Rechtsprechungsnachweise.

## Korrigiert und gehärtet

- **KI-Governance / KI-VO:** falsche Altzuordnungen zu `EuGH C-203/22` wurden aus KI-VO-/Governance-Kontexten entfernt und auf den tatsächlich passenden DSGVO-Art.-15-Kontext umgestellt.
- **Insolvenzplan / StaRUG / Insolvenzverwaltung:** unsichere oder nicht verifizierbare BGH-Nachweise wie `VI ZR 184/17`, `IX ZR 238/17`, `IX ZB 32/21` und `IX ZR 18/19` wurden aus produktiven Skills entfernt, soweit keine belastbare Ersatzfundstelle vorlag.
- **Insolvenzrecht / D&O:** falsche `II ZR 234/18`- und `II ZR 199/19`-Zuordnungen wurden durch passende, überprüfte Leitentscheidungen ersetzt.
- **Squeeze-out:** der Handels-/Gesellschaftsrecht-Skill verweist nun auf DAT/Altana und Stollwerck statt auf eine falsche Insolvenz-/Haftungszuordnung.
- **Audit-Dokumentation:** `audit/HALLUZINATIONS_AUDIT_2026-05-27.md` dokumentiert die zusätzliche lokale Reparaturwelle und den Übergang auf `v16.0.0`.

## Release-Stand

- 100 Plugins
- 2175 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `16.0.0`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Rest-Suche nach den bekannten problematischen Aktenzeichen-/Fundstellenmustern außerhalb der Audit-Historie

---

# v15.0.0 — Lobbyregister, Selbstvertreter, Steuerberater-Werkzeuge und Release-Finalisierung

Version 15 buendelt die nachgelieferten Perplexity-/Klar-Ausbauten mit dem neuen `lobbyregister-bundestag` Plugin und setzt den gesamten Marketplace auf einen einheitlichen Major-Stand.

## Neue und stark ausgebaute Inhalte

- **`lobbyregister-bundestag` neu:** 50 gefuehrte Skills fuer Registrierungspflicht, Ausnahmen, Portal-Eingabeplan, Finanzdaten, Regelungsvorhaben, Stellungnahmen/Gutachten, Verhaltenskodex, Aktualisierung, Bussgeldrisiken, RfS-Kommunikation und Revisionsspur.
- **Open Data/API V2 im Lobbyregister:** eigene Referenz, API-Abfrageplan, JSON-Mapping, Registerexport-Diff und Monitoringplan. Die API wird bewusst als lesende Kontrollschicht gefuehrt; Registrierung und Aktualisierung bleiben Portalhandlungen.
- **Drei Lobbyregister-Testakten:** Dublin-Bank mit Frankfurter Zweigniederlassung und Doppelregistrierungsproblem, Public-Affairs-Agentur Wasserstoff, Bürgerinitiative Waldmoor. Alle drei enthalten API-/Export-Diff-Artefakte.
- **Selbstvertreter-Plugins:** Amtsgericht und Sozialgericht sind auf `main` integriert und in die Marketplace-/Release-Struktur aufgenommen.
- **Steuerberater-Werkzeuge:** `steuerrecht-anwalt-und-berater` enthaelt die neuen StB-Skills fuer BWA, SuSa, Lohn, Jahresabschluss, DBA, Mandantenkommunikation und Software-/Portalroutinen.
- **Audit-Fixes:** Halluzinations- und Aktenzeichen-Reparaturwellen aus den v14.2.x Hotfixes sind mitenthalten.

## Release-Stand

- 100 Plugins
- 2175 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `15.0.0`

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- JSON-Parsing der neuen Lobbyregister-Testakten
- Release-ZIP-Validierung ueber `scripts/validate-release-zips.py` im Build/Workflow

---

# v14.2.0 — Vollumfaenglicher Wissensboost ueber alle 1800+ Skills

Inhaltlicher Tiefenboost ueber alle 97 Plugins und ueber 1800 Skills. Jeder bearbeitete Skill bekommt eine konkrete Triage zum Mandatseinstieg, eine vollstaendige Paragrafenkette mit Wortlaut der zentralen Tatbestandsmerkmale, zwei bis vier aktuelle Leitsatz-Zitate aus BVerfG BGH BAG BFH BSG BVerwG EuGH oder OLG mit Aktenzeichen und Fundstelle, Hinweise auf die zentrale Kommentarliteratur des Rechtsgebiets, einen Schritt-fuer-Schritt-Workflow und ein passendes Output-Template fuer Schriftsatz Bescheid Beschluss oder Mandantenbrief. Strukturelle Bereinigung Plugin sozialrecht-kanzlei vollstaendig nach fachanwalt-sozialrecht uebernommen und alte Light-Touch-Selbstbezeichnung entfernt.

## Was sich pro geboostetem Skill geaendert hat

- **Triage zum Einstieg** — fuenf bis sieben konkrete Vorabfragen mit Begruendung warum sie zu klaeren sind
- **Zentrale Normen mit Wortlaut** — Paragrafenkette mit kursivem Tatbestandsmerkmal nicht nur Paragrafennummer
- **Aktuelle Rechtsprechung** — zwei bis vier Leitsaetze BVerfG BGH BAG BFH BSG BVerwG EuGH OLG mit Aktenzeichen Fundstelle Randnummer Paraphrase
- **Kommentarliteratur** — die ein bis drei einschlaegigen Standardkommentare fuer das Rechtsgebiet
- **Workflow in Schritten** — von Aktenanlage ueber Substantiierung bis Versand
- **Output-Template mit Platzhaltern** — Schriftsatz Bescheid Beschluss Klage Mandantenbrief
- **Rote Schwellen und Eskalationskriterien** — wann Fall an Fachanwalt oder Notar abgegeben gehoert
- **Verzicht auf Boilerplate** — keine generischen Phrasen mehr keine Wiederholungen

## Welleneinteilung

Der Boost erfolgte in 12 Wellen mit jeweils 90 bis 250 Skills.

| Welle | Cluster | Skills |
| --- | --- | --- |
| 1 | Arbeitsrecht inkl. Arbeitszeugnis | 201 |
| 2 | Steuerrecht Familienrecht Erbrecht Sozialrecht | 108 |
| 3 | Strafrecht Verkehrsrecht | 117 |
| 4 | Miet- Bau- und Immobilienrecht | 92 |
| 5 | Medizinrecht Versicherungsrecht Sport- und Transportrecht | 89 |
| 6 | Gewerblicher Rechtsschutz Urheber- und Medienrecht | 90 |
| 7 | IT-Recht Datenschutz KI-Verordnung DSA NIS-2 | 137 |
| 8 | Insolvenz- und Sanierungsrecht | 154 |
| 9 | Corporate M und A Gesellschaftsrecht Gruendung | 208 |
| 10 | Bank- und Kapitalmarktrecht Vergabe International Migration | 114 |
| 11 | Verwaltungs- Verfassungs- Energie- Umwelt- Kartell- Verbraucherrecht | 135 |
| 12 | Prozessrecht Vertragsrecht Forderungsmanagement Compliance Kanzlei-Methodik Jurastudium | 308 |

## Quellenhygiene-Hinweis

Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht aus Modellwissen erzeugt. Literatur darf nur mit vom Nutzer bereitgestellter Quelle oder lizenziertem Live-Zugriff verwendet werden.

## Strukturelle Bereinigung

- **Plugin sozialrecht-kanzlei** wurde vollstaendig in **fachanwalt-sozialrecht** ueberfuehrt. 20 Skills wurden verschoben vier doppelt vorhandene Themen wurden gemergt. Das Fachanwalt-Plugin enthaelt jetzt sowohl die Fachanwalt-Rechtsprechungstiefe als auch die volle Kanzleioperative — Bescheidanalyse Akteneinsicht Anlagen Eilantrag Hilfsmittel Pflegegrad Fristenbuch und PKH.
- **Light-Touch-Selbstbezeichnung entfernt** in 51 Files. Plugins fuer Fachanwaltschaft sind nicht laenger Light-Touch sondern vollumfaenglich.
- **SKILLS.md** mit funktionierenden GitHub-Anker-Links und Zwei-Spalten-Tabelle pro Plugin direkt verlinkt zur SKILL.md.

## Qualitaetssicherung

- Validator `node scripts/validate-plugin-structure.mjs` final OK
- Komma-Sweep in plugin.json und SKILL.md Frontmatter `description:` ueberall ohne Komma zwischen Ziffern
- Cyrillic-Confusables-Sweep ueber alle bearbeiteten Files clean
- Keine verbotenen Frontmatter-Felder (triggers when_to_use language rechtsgebiet license argument-hint user-invocable allowed_tools tools model adapted_from)
- Keine XML-Brackets in description-Feldern
- YAML-Quoting bei descriptions mit Doppelpunkt-Konstrukten korrekt

## Versionsstand nach v14.2.0

- 97 Plugins
- Ueber 1800 boostfaehige Skills bearbeitet (44 Skills waren bereits auf v14.1-Niveau und wurden ohne weitere Aenderung uebernommen)
- alle plugin.json und marketplace.json auf version `14.2.0`

# v14.1.0 — Grosser Inhalts-Boost (145 Top-Skills auf dreifache Tiefe)

Inhaltliche Verdreifachung der 145 fachlich wichtigsten Skills in allen 24 Fachanwalt-Plugins sowie in `steuerrecht-anwalt-und-berater` und den fuenf Corporate-Plugins (`corporate-kanzlei`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `gesellschaftsrecht`, `gesellschaftsgruender`). Generische Boilerplate-Skills (Erstgespraech, Vergleichsverhandlung, Mandantenkommunikation) sind aus dem Boost ausgenommen — der Fokus liegt auf der fachlichen Substanz.

## Was sich pro geboostetem Skill geaendert hat

Jeder der 145 ausgewaehlten Skills wurde von einer Knappformulierung in eine voll ausgearbeitete Arbeitsanleitung umgeschrieben. Erweitert wurden, wo passend:

- **Kaltstart-Mandantenfragen** — sechs bis zehn konkrete Fragen mit Begruendung
- **Rechtsgrundlagen** — Wortlaut der zentralen Tatbestandsmerkmale, nicht nur Paragrafnummer
- **Pruefschemata in Tabellenform** — acht bis fuenfzehn Schritte
- **Schriftsatzbausteine und Klauselvorlagen** — vollstaendige Formulierungen
- **Beweislast und Darlegungslast** — klar zugeordnet
- **Fristen und Verjaehrung** — konkret kalendermaessig
- **Typische Gegenargumente und Reaktion** — Tabellenform
- **Streitwert und RVG-Hinweise** — beziffert
- **Strategische Empfehlung** — aussergerichtlich, Klage, Vergleich
- **Anschluss-Skills** — Querverweise zu anderen Skills im Plugin
- **Aktuelle Aktenzeichen** — BGH, BAG, BFH, BVerwG, BVerfG, OLG, FG

## Cluster-Aufteilung

| Cluster | Plugins | Geboostete Skills |
| --- | --- | --- |
| Cluster A — 24 Fachanwalt-Plugins | siehe Plugin-Liste unten | 120 |
| Cluster B — Steuerrecht | `steuerrecht-anwalt-und-berater` | 5 |
| Cluster C — Corporate | `corporate-kanzlei`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `gesellschaftsrecht`, `gesellschaftsgruender` | 25 (5 pro Plugin) |

## Fachanwalt-Plugins im Boost (alle 24)

`agrarrecht`, `arbeitsrecht`, `bank-kapitalmarktrecht`, `bau-architektenrecht`, `erbrecht`, `familienrecht`, `gewerblicher-rechtsschutz`, `handels-gesellschaftsrecht`, `insolvenz-sanierungsrecht`, `internationales-wirtschaftsrecht`, `it-recht`, `medizinrecht`, `miet-wohnungseigentumsrecht`, `migrationsrecht`, `sozialrecht`, `sportrecht`, `strafrecht`, `transport-speditionsrecht`, `urheber-medienrecht`, `vergaberecht`, `verkehrsrecht`, `versicherungsrecht`, `verwaltungsrecht`.

## Nebenbei behoben

Zwei alte Validator-Fehler in nicht-geboosteten Skills (Komma-in-Zahlen-Pattern in `description`):

- `fachanwalt-gewerblicher-rechtsschutz/.../SKILL.md`: `§§ 5, 32 HinSchG` zu `§§ 5 und 32 HinSchG`
- `fachanwalt-insolvenz-sanierungsrecht/.../SKILL.md`: `§ 9, 3/4-Mehrheit` zu `§ 9 mit 3/4-Mehrheit`

## Globaler Versionsbump

- Alle 98 `plugin.json` auf 14.1.0.
- `marketplace.json` (Top-Level und alle Plugin-Eintraege) auf 14.1.0.
- Validator OK.

---

# v14.0.0 — Frischer Major-Release

Frischer Sammelrelease ueber alle 98 Plugins. Der Versionssprung von 12.x auf 14.0 markiert das Ende des 12er-Inkrement-Zyklus und buendelt den aktuellen Stand der Skill-Familie als einheitliches Major-Release.

## Bug-Hunt Immobilienrechtspraxis

Der Immobilien-Plugin-Schwerpunkt dieses Releases ist eine systematische Bug-Pruefung. Geprueft wurden Frontmatter-Felder, Description-Laengen, verbotene Pattern (Komma in Zahlen), verbotene Frontmatter-Keys, Cross-References, kaputte Markdown-Links und Mischformen aus Umlauten und ASCII-Aequivalenten.

- Inkonsistente Schreibweise `Buerogeb\u00e4ude` (ASCII-Mix mit Umlaut) zu `B\u00fcrogeb\u00e4ude` korrigiert (`projekt-arbeitsweise`).
- Cross-Reference auf `memorandums-ersteller` validiert (Plugin existiert im Marketplace, Verweis bleibt).
- Frontmatter aller sieben Skills geprueft: keine verbotenen Felder, keine zu langen Descriptions, keine Komma-Patterns.
- Plugin-Description und Keywords sauber, keine Aenderung erforderlich.

## Globaler Versionsbump

- Alle 98 `plugin.json` auf 14.0.0.
- `marketplace.json` auf 14.0.0 (Top-Level und alle Plugin-Eintraege).
- Validator OK.

---

# v12.6.0 — Aktuelle BAG-Rechtsprechung 2025/2026 (Arbeitsrecht + Fachanwalt)

Drei kuerzlich entschiedene BAG-Urteile, die die Arbeitnehmerseite spuerbar staerken, werden in den Plugins `arbeitsrecht` und `fachanwalt-arbeitsrecht` jeweils als eigenstaendiger Pruefungsskill verankert. Die Skills enthalten Kaltstartfragen, Pruefschema, Schriftsatzbausteine und konkrete Verteidigungslinien.

## Neue Skills im Plugin `arbeitsrecht` (drei)

- `bag-equal-pay-paarvergleich-8azr30024` — BAG 23.10.2025 (8 AZR 300/24): Equal Pay durch Paarvergleich. Eine Arbeitnehmerin muss keine statistische Vergleichsgruppe auswerten. Ein einziger besser bezahlter maennlicher Kollege bei gleichwertiger Arbeit begruendet die Vermutung des Paragraf 22 AGG. Pauschale Hinweise auf Median oder Verhandlungsgeschick reichen nicht mehr.
- `bag-mindesturlaub-kein-verzicht-9azr10424` — BAG 03.06.2025 (9 AZR 104/24): Kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhaeltnis, auch nicht durch gerichtlichen Vergleich. Klausel-Verbote, empfohlene Vergleichsformulierung mit Trennung Mindesturlaub und Mehrurlaub.
- `bag-freistellungsklausel-unwirksam-5azr10825` — BAG 25.03.2026 (5 AZR 108/25): Pauschale formularmaessige Freistellungsklausel nach Kuendigung unwirksam wegen unangemessener Benachteiligung Paragraf 307 BGB. Beschaeftigungsanspruch BAG GS 1/84 bleibt bestehen.

## Neue Skills im Plugin `fachanwalt-arbeitsrecht` (drei)

- `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich` — Anwaltsperspektive auf 8 AZR 300/24: Kaltstart-Rueckfragen, Klagebaustein Equal Pay, typische Arbeitgeber-Verteidigung und Reaktion.
- `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht` — Anwaltsperspektive auf 9 AZR 104/24: empfohlene Vergleichsformulierung, Klausel-Verbote, Nachforderungsmoeglichkeit bei bereits geschlossenem Pauschalvergleich.
- `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` — Anwaltsperspektive auf 5 AZR 108/25: Strategie fuer Beschaeftigungsanspruch oder Verhandlungsmasse, Schriftsatzbaustein, Annahmeverzugsfolgen.

## Plugin-Metadaten

- Plugin-Beschreibung beider Plugins um Hinweis auf aktuelle BAG-Rechtsprechung 2025/2026 ergaenzt.
- README beider Plugins um Abschnitt zu den neuen Skills erweitert.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.6.0.

---

# v12.5.0 — Arbeitszeugnis-Analyse: Vollstaendiger Mandatsablauf

Schliesst den Mandatsworkflow im `arbeitszeugnis-analyse` Plugin: vom Erstkontakt mit dem Mandanten ueber den Ergebnisbericht bis zum Aufforderungsschreiben an den Arbeitgeber. Das Plugin deckt damit nicht nur die Analyse des Zeugnistextes ab, sondern den gesamten Anwaltsworkflow von der Mandatsannahme bis zum Berichtigungsverlangen.

## Neue Skills (drei)

- `erstgespraech-und-mandatsannahme` — Eingangsbestaetigung mit Dank fuer das uebersandte Zeugnis, strukturierte Anforderungsliste fuer fehlende Unterlagen (Arbeitsvertrag, Aenderungsvereinbarungen, Vorzeugnisse, Kuendigungsschreiben, Abmahnungen, Fehlzeitenuebersicht, Lohnabrechnungen), Erstgespraech-Leitfaden in fuenf Bloecken (Sachverhalt, Ziel, Vergleichsbereitschaft, rechtliche Erstinformation, Vereinbarung), Pruefliste vor Mandatsannahme.
- `mandantenbericht-zeugnisanalyse` — Schriftlicher Ergebnisbericht an den Arbeitnehmer in sieben Abschnitten: Gesamtnote, Befund pro Themenbereich, kritische Einzelstellen mit Wortlaut, rechtliche Einordnung, Erfolgsaussichten in drei Stufen, drei Handlungsoptionen (Akzeptanz, Berichtigungsverlangen, Klage) mit Kosten-Nutzen-Abwaegung, klare Empfehlung. Verstaendliche Sprache fuer den juristischen Laien.
- `aufforderungsschreiben-arbeitgeber` — Aussergerichtliches Berichtigungsverlangen mit acht Bausteinen: Mandatsanzeige, Bezugnahme auf das Zeugnis, Rechtsgrundlage Paragraf 109 GewO, Beanstandungen pro Streitstelle (Wortlaut alt, Wortlaut neu, Begruendung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Schlussformel-Pruefung, kalendermaessige Fristsetzung, Klageandrohung, Kostenfolge. Hoeflich-bestimmter Ton ohne Drohgebaerden. Vollstaendiger Mustertext mit Beispielen.

## Plugin-Metadaten

- 31 Skills (vorher 28), 20-Schritte-Workflow im README.
- Plugin-Beschreibung neu gefasst, hebt den vollstaendigen Mandatsablauf hervor.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.5.0.

---

# v12.4.0 — Arbeitszeugnis-Analyse: Sprachhebel, Codeworte, Klagestrategie

Vertiefung des `arbeitszeugnis-analyse` Plugins um drei spezialisierte Sprach- und Recht-Skills: feingranularer Steigerungsadverbien-Katalog, vollstaendiger Katalog negativer Codeworte fuer sensible Themen sowie eine durchgaengige Klagestrategie zur Zeugnisberichtigung von der ausserprozessualen Rueckforderung bis zum vollstreckbaren Tenor.

## Neue Skills (drei)

- `steigerungsadverbien-katalog` — Vier-Klassen-Matrix der Adverbien mit Notenwirkung: echte Steigerer (stets, jederzeit, immer), Schein-Steigerer mit Risiko (sehr, ausserordentlich nur in Kombination), Abschwaecher (im Allgemeinen, weitgehend, meist) und negative Verstaerker (nie, kaum, kein einziges Mal). Notenkalibrierung jeder Klasse, sodass die satzweise Bewertung das richtige Gewicht erhaelt.
- `negative-codeworte-katalog` — Tabuthemen-Katalog mit den verdeckten Anspielungen auf Alkohol, Krankheit, Diebstahl/Untreue, Konflikt mit Vorgesetzten, mangelnde Loyalitaet, Betriebsratstaetigkeit, sexuelle Verfehlungen, Mitlaeufertum sowie systematischen Auslassungssignalen. Jede Kategorie mit den typischen Formulierungen und dem rechtlich gebotenen Tenor.
- `klage-strategie-zeugnisberichtigung` — Vollstaendige prozessuale Linie: aussergerichtliches Berichtigungsverlangen, Klageantrag mit Tenor (vollstreckbar gemaess Paragraf 888 ZPO), Beweislastverteilung (Note ab Drei: Arbeitnehmer; oberhalb der Drei: Arbeitgeber), Streitwertberechnung, Verjaehrung/Verwirkung und prozesstaktische Empfehlungen.

## Geaenderte Skills

- `verbesserungsvorschlaege-formulieren` — drei neue Drift-Rewrite-Beispiele zu Lernbereitschaft, Innovationsverhalten und Sozialverhalten; ergaenzte Regeln-Tabelle.
- `rechtliche-bewertung-bag-rechtsprechung` — drei neue Absaetze zu verfestigter BAG-Rechtsprechung, Schlussformel-Codeworten und Verjaehrung/Verwirkung; sieben neue Regeln-Tabellenzeilen und drei zusaetzliche Bewertungsbeispiele.

## Plugin-Metadaten

- 28 Skills (vorher 25), erweiterter 16-Schritte-Workflow im README.
- Plugin-Beschreibung neu gefasst und auf die drei neuen Schwerpunkte abgestimmt.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.4.0.

---

# v12.3.0 — Arbeitszeugnis-Analyse: Schaufenster-Drift-Detektor

Spezialisierter Ausbau des `arbeitszeugnis-analyse` Plugins um die Erkennung des Schaufenster-Patterns: einzelne Saetze auf Note-1-Niveau, daneben Saetze auf Note-3-Niveau zum selben Themenbereich. Wer nur die Spitzensaetze liest, sieht Note 1; wer die Drift erkennt, sieht die korrekte hochgezogene Zwei bis solide Drei.

## Neue Skills (drei)

- **`bereichs-drift-detektor`** — Erkennt Drift innerhalb derselben acht Themenbereiche (Fachkenntnisse, Lernbereitschaft, strategisches Denken, Arbeitsweise, Engagement, Innovation, Arbeitsergebnis, Sozialverhalten). Spreizung zwei Stufen = Rot, eine Stufe = Orange. Drift in weichen Bereichen (Lernen, Innovation, Sozialverhalten) wird gesondert geflaggt.
- **`satzweise-notenmatrix`** — Bewertet jeden notenrelevanten Satz mit Schulnote von eins bis fuenf. Festes Raster: Steigerungsadverb plus Superlativ = 1, eins davon = 2, Grundaussage = 3, Einschraenkung oder "bemueht" = 4, Distanzformel = 5. Tabellarisches Ausgabeformat mit Themenbereich pro Satz — Datenbasis fuer Drift-Detektor und Gesamtnoten-Aggregation.
- **`muster-arbeitszeugnis-gemischte-noten`** — Vollstaendiges anonymisiertes Schulungszeugnis mit Schaufenster-Pattern. Zeigt 1er- und 3er-Saetze gemischt, vollstaendige Satz-fuer-Satz-Notenmatrix, Bereichs-Drift-Analyse und gewichtete Gesamtnote mit Drift-Penalty.

## Updates

- **`gesamtnoten-aggregation`**: neue Drift-Penalty-Regel (minus halbe Stufe bei Spreizung zwei Stufen, minus halbe Stufe bei konstanter Note 3 in weichen Bereichen). Neues Beispiel: Schaufenster-Zeugnis.
- **`widerspruechliche-bewertungen`**: vierter Widerspruchstyp (Schaufenster-Pattern im selben Themenbereich) mit Verweis auf den neuen Drift-Detektor.
- **`README.md`**: erweiterter Empfehlungs-Workflow um Satzmatrix, Drift-Detektor und Widerspruchsanalyse; Plugin enthaelt jetzt 25 Skills.

## Globaler Versionsbump

Alle 98 Plugins und `marketplace.json` auf v12.3.0.

---

# v12.2.0 — Testakten in Plugin-READMEs sichtbar gemacht

## README-Sweep
13 Plugin-READMEs ergaenzt: Testakte als sichtbarer Direkt-Download (Tabelle) direkt unter der Plugin-Download-Sektion.

- arbeitsrecht (Vogt, Weber)
- aussenwirtschaft-zoll-sanktionen (GlobalMaschinen)
- datenschutzrecht (Solis Vision X)
- dsa-dma-digitalregulierung (Bayerische Baustube)
- geldwaeschepraevention-aml-kyc (Musterholding)
- grosskanzlei-corporate-ma (Datenraum)
- insolvenzrecht (LUMEN Studios — Edelholz war bereits drin)
- insolvenzverwaltung (Moebelwerk Havelberg, Nordlicht Handels)
- kanzlei-allgemein (Kanzlei-Alltag)
- steuerrecht-anwalt-und-berater (Edelholz)
- strafbefehl-verteidiger (LUMEN Studios)
- vertragsrecht (Sieglinger SV-Gutachten)
- zwangsverwaltung-zvg (Friedrichshoefe, Mietshaus Parkstrasse, Eppendorf)

## Fix
- testakten/inkasso-zahlungsklage-modefuchs/README.md: toter Link auf `Akte_ModeFuchs_GmbH.zip` entfernt; nur der `originale/` Ordner mit 28 PDFs bleibt.
- Mapping-Korrektur Testakten zu Plugins: `bauplanungsrecht` -> `normenkontrolle-bauleitplanung`.

## Bump
- Alle 98 Plugins, marketplace.json und CHANGELOG auf v12.2.0.

# v12.1.0 — Validatorhaertung Plugin-Generator + Versionsbump

## Fix (gegenueber v12.0.0)
- `forderungsmanagement-klagewerkstatt/scripts/plugin_aus_hausregeln.py`: erzeugte hauseigene Mini-Plugins sind jetzt validatorkonform und sofort in Claude Code installierbar.
  - plugin.json description gekuerzt von 514 auf 218 Zeichen (Marketplace-Limit 300).
  - Zahl-Komma-Zahl-Sequenzen `12, 13, 29, 29c` und `23, 71` ersetzt durch `12/13/29/29c` und `23 und 71` (Cowork-Validator-Regel).
  - Frontmatter-Felder `language`, `license`, `when_to_use` aus erzeugter SKILL.md entfernt; Trigger-Phrasen wurden in die description integriert.

## Bump
- Alle 98 Plugins, marketplace.json und CHANGELOG auf v12.1.0.

# v12.0.1 — Hotfix forderungsmanagement-klagewerkstatt Plugin-Generator

## Fix
- `scripts/plugin_aus_hausregeln.py` erzeugt jetzt validatorkonforme Mini-Plugins (`klagewerkstatt-<slug>`):
  - plugin.json description gekuerzt auf 218 Zeichen (vorher 514, Marketplace-Limit 300)
  - Zahl-Komma-Zahl-Sequenz `12, 13, 29, 29c` und `23, 71` ersetzt durch `12/13/29/29c` und `23 und 71` in plugin.json + SKILL.md description
  - Frontmatter-Felder `language`, `license`, `when_to_use` aus erzeugter SKILL.md entfernt (Trigger-Phrasen in description integriert)
- Erzeugte hauseigene Plugins lassen sich jetzt sofort in Claude Code installieren.

## v12.0.0 — 2026-05-26 — Strafrecht-Ausbau: Nebenklage, Zeugenbeistand, Adhaesion, Insolvenzantrag der StA + Codex-Fixes + Bug-Hunt

### Major-Feature: 4 neue Skills im Plugin `fachanwalt-strafrecht`

- `fachanwalt-strafrecht-nebenklage-opfervertretung` — Nebenklagebefugnis § 395 StPO, Anschluss § 396 StPO, Opferanwaltsbeiordnung § 397a StPO, Akteneinsicht § 406e StPO, psychosoziale Prozessbegleitung § 406g StPO, RVG VV Nr. 4124 ff.
- `fachanwalt-strafrecht-zeugenbeistand` — Beistand gemaess § 68b StPO, Pruefung § 55 StPO Selbstbelastung, §§ 52-53 StPO Zeugnisverweigerung, Adressanonymisierung § 68 Abs. 2/3 StPO, Whistleblower-Konstellation.
- `fachanwalt-strafrecht-adhaesionsverfahren` — zivilrechtliche Anspruche im Strafverfahren §§ 403-406c StPO, Antrag § 404 StPO, Vergleich § 405 StPO als Vollstreckungstitel, Grundurteil § 406 StPO, RVG VV Nr. 4143-4147.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` — Insolvenzantrag StA / Finanzamt gegen Angeklagte, Doppelspur Strafverfahren-Insolvenzverfahren, Vermoegensabschoepfung §§ 73 ff. StGB und Beschlagnahme §§ 111b ff. StPO, § 111i StPO, Schweigerecht vs. § 97 InsO.

### Codex-Feedback adressiert (PR fachanwalt-strafrecht)

Drei Skills im Plugin `fachanwalt-strafrecht` enthielten zivilrechtliche Reste aus einem Allgemein-Template (Leistungs-/Feststellungs-/Gestaltungsantrag, Streitwert aus Hauptforderung, Klage-einreichen-Walk-Away). Komplett strafrechts-spezifisch neu geschrieben:

- `schriftsatzkern-substantiierung` — Einspruch gegen Strafbefehl, Revisionsbegruendung, Klageerzwingung, Beweisantraege § 244 StPO, Verfahrenshindernisse, Sach- und Verfahrensruegen.
- `vergleichsverhandlung-strategie` — Verstaendigung § 257c StPO, Einstellung § 153a StPO, Adhaesionsvergleich § 405 StPO, TOA § 46a StGB; statt zivilrechtlicher Skripte.
- `erstgespraech-mandatsannahme` — RVG-Gebuehrentatbestaende VV-RVG Teil 4 und Teil 5 statt Streitwert-Kalkulation, fuenf strafrechtsspezifische Praxis-Konstellationen.

### Bug-Hunt v12.0.0

- Alle Backtick-Cross-Refs auf das fusionierte Plugin `kanzlei-cowork` (52 Dateien in 24 Plugins + CHANGELOG, INSTALLATION, ASSET_INDEX, TESTBERICHT) auf `kanzlei-allgemein` umgestellt.
- Config-Pfade in `kanzlei-allgemein/skills/{sekretariats-tagesbrief, mandantenakte-anlegen, fristenbuch-fuehren, kanzlei-cowork-kaltstart-interview}` von `~/.claude/plugins/config/.../kanzlei-cowork/` auf `kanzlei-allgemein/` korrigiert.
- Slash-Command-Verweise in `tests/smoke-tests.md` und `kanzlei-cowork-kaltstart-interview` von `/kanzlei-cowork:` auf `/kanzlei-allgemein:` umgestellt.
- `tests/smoke-tests.md`: Abschnitt-Header von `## kanzlei-cowork (rechnungserstellung-rvg)` auf `## kanzlei-allgemein (rechnungserstellung-rvg)` umgestellt.
- `kanzlei-allgemein/.claude-plugin/plugin.json`: Keyword `kanzlei-cowork` aus Liste entfernt (Migrations-Hinweis in README/CHANGELOG bleibt).
- Workflow-Validator-Fixes aus v11.0.0-Schluss: `README.md` ohne toten Link `./kanzlei-cowork`; `testakten/README.md` mit allen 46 Akten (vorher 44), inkl. zwei neuer Tabellen-Zeilen und ZIP-Eintraege fuer `dsa-dma-bayrische-baustube-meissner` und `sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`.

### Repo-Stand v12.0.0

- 98 Plugins, alle plugin.json einheitlich auf 12.0.0
- marketplace.json mit 98 Eintraegen, alle 12.0.0
- 46 Testakten
- QA: kein `\d,\d` in plugin.json/description und SKILL.md/description; Skill-Namen alle ≤ 64 Zeichen; Plugin-Descriptions alle ≤ 300; Skill-Descriptions alle ≤ 1024; Steuer-Plugin-Konvent eingehalten (Frontmatter ASCII); Validator-Script `validate-plugin-structure.mjs` clean.

## v11.0.0 — 2026-05-26 — DSA/DMA-Plugin, BetrVG-Heilung, qES-Befristung, KI-Sachverstaendige, Kanzlei-Cowork-Fusion

### Major-Feature: Plugin "dsa-dma-digitalregulierung"

Neues Plugin Nr. 99: **DSA und DMA und Digitalregulierung EU**. 9 Skills:

- `digitalregulierung-pyramide-check` — Einstiegsskill, ordnet Sachverhalte den passenden Rechtsakten zu (DSA DMA Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO § 19a GWB)
- `dsa-vlop-vlose-einordnung-und-pflichten` — Schwellenwert 45 Mio. EU-Nutzer, Designation, Pflichtenkatalog Art. 34-43
- `dma-gatekeeper-schwellen-und-kernplattformdienste` — drei kumulative Voraussetzungen, quantitative Vermutungen, KPD-Katalog, Pflichten Art. 5-7
- `dsa-art-34-systemische-risikobewertung` — vier Risikoarten, Methodik, Audit Art. 37
- `dsa-art-40-forschungsdatenzugang-algorithmen` — drei Zugangsregime, vetted researchers, Delegierte VO 2024/2987
- `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` — Stufenmodell Art. 17 / 20 / 21, BGH III ZR 179/20 und III ZR 192/20, Eilrechtsschutz
- `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` — Mehr-Anker-Strategie
- `zustellung-und-vertreter-art-13-dsa-art-37-dma` — Praxis Zustellung gegen Auslands-Plattformen
- `klage-gegen-vlop-einordnung-art-263-aeuv` — Nichtigkeitsklage zum EuG, Frist 2 Monate

### Testakte (neu)

- **`testakten/dsa-dma-bayrische-baustube-meissner/`** — fragmentarische Akte mit 17 Dokumenten verschiedener Formate (.md, .csv, .eml). Mandantin Baustube Meissnerlein GmbH, Hoechstadt an der Aisch. Konstellation: Account-Sperre auf US-Plattform "Glitzerwald", parallel VLOP-Designations-Streit, Mitbewerber Lindheim & Soehne KG Schwabach mit Verdacht auf Self-Preferencing, Art.-40-DSA-Forschungsantrag Dr. Vogelbroich (FAU Erlangen), Zustellungsproblem Art. 13 DSA EU-Vertreter Dublin.
- **`testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/`** — fragmentarische Akte mit 15 Dokumenten zum KI-Vorwurf bei Sachverstaendigengutachten (PV-Anlage Werkmangel, Sachverstaendiger Pfaffenberger). Anbindung an LG-Darmstadt-Linie (§ 407a Abs. 1 ZPO; § 8a Abs. 2 S. 1 Nr. 1 und Nr. 2 JVEG).

### BetrVG-Heilung und Ersatzmitglieder

Neue Skills in `arbeitsrecht` und `fachanwalt-arbeitsrecht`:

- `betriebsrat-ladung-und-ersatzmitglieder-pruefen` (arbeitsrecht)
- `betriebsrat-beschluss-heilung-nachtraeglich` (arbeitsrecht)
- `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung` (fachanwalt-arbeitsrecht)

Eingearbeitet: BAG 25.09.2024 — 7 ABR 37/23 (Heilung Betriebsratsbeschluss; Vorinstanz LAG Nuernberg 27.09.2023 — 2 TaBV 8/23), BAG 20.05.2025 — 1 AZR 35/24 (Nachladung Ersatzmitglied).

### Schriftform und qES — Befristung

Neuer Skill in `schriftform-und-textform-bgb`:

- `befristungsabrede-qes-rechtsprechung-stand-2026` — LAG Berlin-Brandenburg 16.03.2022 — 23 Sa 1133/21 (gescannte Unterschrift wahrt § 14 IV TzBfG nicht), ArbG Berlin (einfache elektronische Signatur unwirksam), ArbG Gera 07.03.2024 — 2 Ca 936/23 (qES per DocuSign wahrt Schriftform).

### Maklerskill BGH I ZR 202/25 — voll ueberarbeitet

`maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` komplett neu geschrieben mit 4 verifizierten Leitsaetzen: E-Mail-Austausch erfuellt Textform auch auf getrennten Datentraegern; konkludenter Abschluss moeglich; Erklaerungsende muss erkennbar sein; Bereicherungsanspruch des Maklers gesperrt bei Textformverstoss. Falsche Lehrsaetze der Vorversion ersetzt.

### KI-Vorwurf bei Sachverstaendigengutachten

Drei neue Skills mit verschiedener Perspektive auf die LG-Darmstadt-Linie:

- `kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` (Anwalts-Generalist)
- `grosskanzlei-corporate-ma/skills/ki-einsatz-bei-gutachten-mandatsseite` (Beratungsseite)
- `jveg-kostenpruefer/skills/pruefung-sachverstaendigengutachten-ki-deklaration` (Kostenpruefer, festsetzungs-orientiert)

### Plugin-Fusion: kanzlei-allgemein in kanzlei-allgemein

Das Plugin `kanzlei-allgemein` wurde vollstaendig in `kanzlei-allgemein` fusioniert. Alle 14 Cowork-Skills sind erhalten und werden ab v11.0.0 unter `kanzlei-allgemein/skills/` ausgeliefert: `aktenbestand-pflege`, `bea-versand-pruefen`, `fristenbuch-fuehren`, `geburtstage-feiertage`, `kanzlei-allgemein-kaltstart-interview`, `mahnwesen-honorar`, `mandantenakte-anlegen`, `mandantenbrief-vorlagen`, `posteingang-ausgang`, `rechnungserstellung-rvg` (inkl. Werkzeug `rvg_gebuehrenrechner.py`), `sekretariats-tagesbrief`, `timesheet-aktenzeitung`, `versand-vor-check`, `weihnachtskarten`. Das Stand-Alone-Plugin `kanzlei-allgemein` ist entfallen.

### Repo-Stand v11.0.0

- 98 Plugins (99 minus Cowork-Fusion plus DSA/DMA)
- marketplace.json mit 98 Eintraegen, alle auf 11.0.0
- 98 plugin.json-Dateien einheitlich auf 11.0.0
- 45 Testakten (vorher 43 plus 2 neu)
- QA: kein `\d,\d` in plugin.json/description und SKILL.md/description; Skill-Namen alle ≤ 64 Zeichen; Plugin-Descriptions alle ≤ 300; Skill-Descriptions alle ≤ 1024; Steuer-Plugin-Konvent eingehalten (Frontmatter ASCII)

### QA-Vorlauf (Commit `69f627c0`)

- Aktenzeichen-Korrekturen in 14 Dateien: II ZR 88/13 → II ZR 88/99; IX ZR 92/04 → IX ZR 228/03; 3 AZR 18/12 → 3 AZR 303/18

# Changelog

Alle wesentlichen Änderungen an diesem Repository werden hier dokumentiert. Format orientiert an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/), Versionierung nach [SemVer](https://semver.org/lang/de/).

## v8.0.0 — 2026-05-25 — Steuer-Plugin Härtung + Codex-Audit-Welle

### Major-Update
- Versionsfelder repo-weit auf 8.0.0 angehoben: 97 `plugin.json`-Dateien plus die zentrale `.claude-plugin/marketplace.json` mit 97 Plugin-Einträgen. Summe: 195 Versions-Stellen in 98 Dateien.
- `release-plugin-zips.yml` erzeugt nach dem Tag-Push 97 Plugin-ZIPs + 43 Testakten-ZIPs + `marketplace.json` = 141 Release-Assets.

### Steuer-Plugin Erweiterung (PR #70, #71)
- Neuer Skill **`anw-insolvenzreife-pruefung-17-19-inso`** (210 Zeilen): §§ 17, 19 InsO aus Steueranwalts-Sicht mit § 222 AO Stundung, § 361 AO AdV, § 69 AO GF-Haftung Lohnsteuer, § 266a StGB, BGH IX ZB 50/03, IDW S 11, SanInsKG 24-Monats-Prognose.
- **`stb-warnschreiben-krisensignale`** um Abschnitt "Warum gerade der Steuerberater" und "§ 102 StaRUG als Auslöser der StB-Hinweispflicht" erweitert — Steuerberater als externer Bestandteil des Krisenfrüherkennungssystems.
- **Generalueberholung mit sechs neuen Skills**: `anw-stundung-erlass-vollstreckungsaufschub`, `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern`, `anw-organschaft-konzern-grundlagen`, `anw-grunderwerbsteuer-share-deal-90-prozent`, `anw-dac7-dac8-plattformen-krypto`, `anw-minbestg-pillar2-konzernbesteuerung`, `stb-drv-sozialversicherungspruefung`.

### Juristische Korrekturen (Codex-Audit-Welle PR #72–#76)
- **§ 361 AO AdV ist keine Stundung** (PR #72, #74): AdV hemmt nur die Vollziehung, lässt die Fälligkeit unberührt. AdV-Beträge bleiben Passiva I bei der § 17 InsO-Prüfung. Nur die echte Stundung nach § 222 AO verschiebt die Fälligkeit. Korrektur in `anw-insolvenzreife-pruefung-17-19-inso` und 5 weiteren Liquiditätsprüfer-Skills (`insolvenzrecht/zahlungsunfaehigkeit-pruefung-17-inso`, `insolvenzrecht/liquiditaetsvorschau-insolvenzrechtlich`, `liquiditaetsplanung/liquiditaetsvorschau-3wochen`, `liquiditaetsplanung/liquiditaetsvorschau-insolvenzrechtlich`, `steuerrecht-anwalt-und-berater/stb-liquiditaetsvorschau-3wochen`).
- **§ 393 Abs. 2 AO Verwendungsverbot nur für steuerfremde Straftaten** (PR #73): Korrigiert in `anw-steuerstrafverteidigung-verstaendigung`. Für die Steuerstraftat selbst sind Steuerakten verwertbar (BGH 5 StR 191/04; Joecks/Jaeger/Randt, Steuerstrafrecht, 8. Aufl. 2015, § 393 Rn. 81 ff.). § 30 AO schafft kein Verwendungsverbot. § 136a StPO als realer Verteidigungsansatz ergänzt.
- **§ 393 Abs. 1 S. 2 AO nur Zwangsmittelverbot** (PR #75): Präzisiert in `anw-steuerstrafverteidigung-verstaendigung`. Setzt die steuerlichen Mitwirkungspflichten **nicht** generell außer Kraft, sondern verbietet nur den Einsatz von Zwangsmitteln (§ 328 AO) soweit Selbstbelastungsgefahr. §§ 90, 93, 200 AO bestehen fort; Schätzung § 162 AO und Steuererklärungspflicht bleiben.
- **GrESt-Konzernklausel ist § 6a GrEStG** (PR #76): Korrigiert in `anw-grunderwerbsteuer-share-deal-90-prozent` zweifach. § 6a GrEStG begünstigt Umwandlung/Einbringung im Konzern (95 % Beteiligung, 5 Jahre Vor- und Nachbehaltensfrist). § 7 GrEStG regelt dagegen den Übergang von Gesamthand zu Bruchteilseigentum.
- **GIR-Erstabgabe 18 Monate** (PR #76): Korrigiert in `anw-minbestg-pillar2-konzernbesteuerung`. Übergangsregelung nach § 95 Abs. 1 MinStG i.V.m. Art. 44 Abs. 7 EU-RL 2022/2523. Kalenderjahrgleicher Konzern GJ 2024 → Frist 30.6.2026. Folgejahre weiter 15 Monate.

### Tooling und Cleanup (PR #77, #78)
- ASSET_INDEX.md auf Stand v8.0.0 angehoben, Plugin-Counts repo-weit konsistent: 97 Plugins / 43 Fallakten / 1 Manifest = 141 Release-Assets.
- Repo-Sanity-Sweep durchgeführt: Validator, Marketplace, Skill-Struktur (1.643 Skills), Symlinks, README-Referenzen — alle Prüfungen OK.

## v7.1.0 — 2026-05-24 — Steuer-Plugin-Konsolidierung + ELSTER-Klarstellung

### Major-Feature
- Drei Steuer-Plugins (`steuerrecht-kanzlei`, `fachanwalt-steuerrecht`, `steuerberater-werkzeuge`) zu einem konsolidierten Plugin **`steuerrecht-anwalt-und-berater`** zusammengeführt. 18 Skills mit Präfix-Schema `anw-`/`fa-`/`stb-`: 13× Steueranwalt (Kaltstart-Interview, Mandat-Triage, Steuerbescheid-Analyse, Einspruch ans Finanzamt, AdV, Klage Finanzgericht, Akteneinsicht, Außenprüfung, Selbstanzeige § 371 AO, verbindliche Auskunft § 89 II AO, Fristenbuch, Betriebsausgaben/Werbungskosten-Prüfraster, USt-Vorsteuerabzug), 1× FA-Orientierung, 4× Steuerberater (Kaltstart-Interview, BWA/SuSa/Bilanz, 3-Wochen-Liquiditätsvorschau, 3-/6-/12-Monats-Vorschau). Vier inhaltliche Dubletten (Einspruch, Außenprüfung, Selbstanzeige, verbindliche Auskunft) zu jeweils einem Master-Skill gemergt. Repo-Plugin-Anzahl: 99 → 97.

### Juristische Korrekturen
- **ELSTER/ERiC statt beA an Finanzämter** (§ 87a Abs. 1 S. 2 AO n.F., JStG 2024, seit 6.12.2024): Versandwege in Einspruch, AdV-Antrag, Akteneinsicht, Selbstanzeige und verbindlicher Auskunft umgestellt. beA an Finanzbehörden ist unzulässig — ein per beA eingelegter Einspruch wäre formunwirksam und wahrt die Frist nicht (Nds. FG 12.2.2026 – 2 K 152/25). beA bleibt Pflicht gegenüber Finanzgerichten (§ 52d FGO).
- **Triage-Routing-Slugs** im konsolidierten Plugin auf die neuen Skill-Slugs umgestellt; **ASSET_INDEX**-Dubletten bereinigt; **`stb-`-Sister-Skill-Verweise** auf die konsolidierten Pfade aktualisiert.

### Tooling
- Versionsfelder repo-weit auf 7.1.0 angehoben: 97 `plugin.json`-Dateien plus die zentrale `.claude-plugin/marketplace.json` mit 97 Plugin-Einträgen. Summe: 195 Versions-Stellen in 98 Dateien.
- `release-plugin-zips.yml` erzeugt nach dem Tag-Push 97 Plugin-ZIPs + 43 Testakten-ZIPs + `marketplace.json` = 141 Release-Assets.

## v7.0.0 — 2026-05-24 — Reform-Stand 2026

### Major-Update
- Versionsfelder repo-weit auf 7.0.0 vereinheitlicht: 99 `plugin.json`-Dateien (je ein `version`-Feld) plus eine zentrale `.claude-plugin/marketplace.json`, die ihrerseits 99 Plugin-Einträge mit `version`-Feld enthält. Summe: 99 + 1 Manifest-Datei mit 99 internen Versions-Einträgen = 198 angefasste Versions-Stellen in 100 Dateien.

### Inhaltliche Aktualisierungen
- **Wandeldarlehen-Plugin** auf Reform-Stand 05/2026 angehoben (DiRUG 2022/2023, SanInsFoG 1.1.2021, PostModG 1.1.2025, GesLV, Transparenzregister).
- **Steuerrecht** aktualisiert: WtcG-Gebühren, eRechnung-Pflicht ab 1.1.2025 (§ 14 UStG), § 153 AO; Selbstanzeige-Dublette entfernt; § 398a AO Zuschlagsstaffel ergänzt.
- **liquiditaetsplanung**: openpyxl-Dependency komplett entfernt; Kanzleien starten `build_liquiditaetsplan.py` ohne `pip install` (Stdlib-XLSX-Writer mit Live-Formeln, Styles, DXF-Solid-Fills, Conditional Formatting, Freeze Panes).

### Juristische Korrekturen
- **ELSTER/ERiC statt beA gegenueber Finanzbehoerden** (§ 87a Abs. 1 S. 2 AO n.F., JStG 2024, seit 6.12.2024): Im neuen konsolidierten Steuer-Plugin alle Stellen umgestellt, an denen Einspruch, AdV-Antrag, Akteneinsicht, Selbstanzeige oder verbindliche Auskunft per beA an das Finanzamt empfohlen wurden. beA an Finanzbehoerden ist unzulaessig; ein per beA eingelegter Einspruch ist formunwirksam und wahrt die Frist nicht (Nds. FG 12.2.2026 – 2 K 152/25). beA bleibt Pflicht gegenueber Finanzgerichten (§ 52d FGO).
- **§ 44 DSGVO → § 44 BDSG i.V.m. Art. 79 DSGVO**: Vier Arbeitsrechts-Skills zitierten eine nicht existierende DSGVO-Norm. Die DSGVO hat nur Artikel; § 44 BDSG ist die deutsche Norm für die Gerichtszuständigkeit. Vier weitere DSGVO-Verweise (Art. 8, 13, 34, 37 DSGVO) von `§` auf `Art.` umgestellt.
- **kongruent (lat. *congruens*)**: Phase-2-Umlauten-Patch hatte den etablierten Fachbegriff "kongruente / inkongruente Deckung" (§ 130/131 InsO) fälschlich umlautiert. 17 Dateien, 67 Korrekturen.
- **§ 57 II GmbHG statt § 19 GmbHG**: Codex-Befund — falscher Normverweis in `sacheinlagebericht-werthaltigkeit` (Wandeldarlehen-Plugin) korrigiert; § 57 II GmbHG i.V.m. § 8 II GmbHG ist die korrekte Anker-Norm für die GF-Versicherung in der HR-Anmeldung der Kapitalerhöhung.
- **§ 153 AO ist Berichtigungspflicht — KEINE Strafbefreiung**: Codex-P1-Review von PR #60. In `anw-selbstanzeige-371` stand fälschlich, § 153 AO wirke strafbefreiend. Korrekt: § 153 AO ist eine rein steuerliche Berichtigungspflicht ohne strafrechtliche Sperrwirkung; Strafbefreiung folgt allein aus § 371 AO (Vorsatz) bzw. § 378 III AO (Leichtfertigkeit). Drei-Stufen-Bewertung der Ursprungserklärung ergänzt; Praxisempfehlung: bei Zweifeln zusätzlich Selbstanzeige-Weg erfüllen.
- **Stale Skill-Slug-Verweise** behoben: `datenpannenmeldung → datenpanne-meldung`, `auskunftsersuchen-art-15-dsgvo → dsgvo-auskunft`.

### Repo-Polish
- Umlauten-Polish in SKILL.md-Bodies und references/ (531 Dateien, 5017 Korrekturen); YAML-Frontmatter, Eigennamen, Slugs, URLs, Code-Blocks geschützt.
- Skill-Slugs (Verzeichnisnamen) bleiben ASCII; nur Fließtext umlautiert.
- README-Intro klargestellt: Plugin- und Skill-Sammlung; Beck-Verweise entfernt.
- Testakten-Hinweis im Überblick prominent platziert.

### Tooling
- `release-plugin-zips.yml` triggert automatisch auf Tag-Push; pro Release werden 99 Plugin-ZIPs (aus `.claude-plugin/marketplace.json`) plus 43 Testakten-ZIPs (mit `testakte-`-Prefix, separat aus `testakten/*/` verpackt) plus `marketplace.json` als Manifest erzeugt — zusammen 143 Release-Assets.
- Validator (`scripts/validate-plugin-structure.mjs`) bleibt grün.
