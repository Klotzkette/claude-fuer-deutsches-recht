# Megaprompt: seerecht-schifffahrtsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 120 Skills (gekuerzt fuer Chat-Fenster) des Plugins `seerecht-schifffahrtsrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — See- und Schifffahrtsrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und ers…
2. **074-offshore-schiff-arrest-vorbereiten** — Offshore-Schiff: Glaeubiger sichert Anspruch an Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender durch dingli…
3. **auslandsflagge-local-insolvenz-reederei** — Reederei betreibt Schiff unter Auslandsflagge (Panama; Marshall Islands; Liberia); Abstimmung mit Local Counsel für Regi…
4. **bergung-und-wrack** — Schiff strandet oder sinkt; Berger verlangen Bergungslohn; Wrackbeseitigung wird angeordnet. HGB §§ 574-583 (Bergung); W…
5. **bermuda-struktur-seeschiff** — Reederei nutzt Bermuda-Holding-Struktur (SPV; Cayman/BVI-Holding): steuerliche und haftungsrechtliche Analyse. Abgrenzun…
6. **binnenschiff-arrest-wrackpflicht** — Binnenschiff: Glaeubiger sichert Anspruch an Binnenmotorgueterschiff; Tanker oder Fahrgastschiff durch dinglichen Arrest…
7. **binnenschiff-closing-planen** — Binnenschiff: Closing eines Binnenmotorgueterschiff; Tanker oder Fahrgastschiff-Kaufs oder einer Finanzierung planen: Ei…
8. **binnenschiff-hypothek-bestellen** — Binnenschiff: Binnenschiffer; Verladungsunternehmen; Kreditinstitut bestellt Schiffshypothek als Sicherheit für Finanzie…

---

## Skill: `kaltstart-triage`

_See- und Schifffahrtsrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe._

# See- und Schifffahrtsrecht - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Seerecht Schifffahrtsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startfragen

1. Wer nutzt das Plugin: Laie, Verband, Kanzlei, Behörde, Unternehmen, Presse, Verwaltung oder Fachabteilung?
2. Welche Entscheidung steht jetzt an und welche Frist läuft?
3. Welche Dokumente liegen vor, welche fehlen und welche Quelle muss live geprüft werden?
4. Welche Behörde, welches Gericht, welches Register oder welcher private Akteur ist betroffen?
5. Soll am Ende ein Antrag, ein Widerspruch, eine Klage-/Eilantragslinie, ein Dashboard, ein Memo oder ein Schreiben entstehen?

## Workflow

1. Sachverhalt in Akte, Normpfad, Zuständigkeit, Frist, Beweis und Ziel zerlegen.
2. Die einschlägige Norm nicht aus dem Gedächtnis final behaupten, sondern als Live-Check gegen amtliche Quelle markieren.
3. Ablehnungs-, Kosten-, Zuständigkeits- und Beweisrisiken offen in einer Ampel führen.
4. Bei Mehr-Ebenen-Recht immer Bund, Land, Kommune, EU/international und Spezialgesetz trennen.
5. Ausgabe mit konkretem nächsten Schritt, offenen Rückfragen und einer kurzen Fassung für Nichtjuristen schließen.

## Typische Ausgaben

- Prüfvermerk mit Normpfad und Live-Check-Liste
- Fristen- und Zuständigkeitsmatrix
- Entwurf für Antrag, Widerspruch, Klagebaustein oder Behördenbrief
- Dashboard-/Tracker-Eintrag mit Status, Risiko und nächster Aktion

## Red Flags

- blindes Zitieren nicht verifizierter Rechtsprechung oder alter Gesetzesstände
- falsche Behörde, falscher Rechtsweg oder unbemerkte Spezialzuständigkeit
- Gebühren-, Frist-, Präklusions-, Geheimschutz-, Datenschutz- oder Drittbetroffenenproblem
- politisch klingende Bewertung ohne saubere Rechtsgrundlage und Beleglogik

## Quellen- und Qualitätsregel

Primär mit amtlichen Gesetzestexten, Behördenhinweisen, Gerichtsentscheidungen mit Datum/Aktenzeichen und frei prüfbaren Quellen arbeiten. Literatur, Datenbanken hinter Paywalls und Fundstellen ohne Nutzerquelle nicht behaupten. Wenn Landesrecht, EU-Recht oder ausländisches Recht berührt ist, den Rechtsstand ausdrücklich live prüfen und die Ausgabe als Arbeitsfassung kennzeichnen.

---

## Skill: `074-offshore-schiff-arrest-vorbereiten`

_Offshore-Schiff: Glaeubiger sichert Anspruch an Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantra..._

# Offshore-Schiff – Arrest vorbereiten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Ein Hypothekengläubiger will ein Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zuständiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhörung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das Offshore-Versorgungsschiff (PSV/AHTS) oder Bohrinsel-Tender im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Vertiefung: Internationale Seearrestpraxis
International koordinieren sich Gläubiger häufig über die 1952 Brüsseler Seearrest-Konvention (ISAC 1952) und über P&I-Club-Korrespondenten. In der EU gilt ergänzend die EuGVVO 2012 (Brüssel Ia-VO) für Vollstreckung und gegenseitige Anerkennung von Arrestbeschlüssen. In Drittstaaten gelten nationaler Seearrest-Regeln; Koordination mit Local Counsel ist unverzichtbar.

## Seeforderungen nach ISAC 1952 Art. 1
Zum Arrest berechtigende Seeforderungen umfassen: Schiffsbau- und -reparaturkosten; Schiffsausrüstung; Schifffahrtsabgaben; Frachtzahlungen; Charterzahlungen; Bergungskosten; Schiffsgläubigerrechte; Konnossementsansprüche; Kollisionshaftung; Hypothekenansprüche. Nicht erfasst sind Ansprüche aus reinem Landtransport ohne Seebezug.

## Verteidigungsstrategien des Schiffseigentümers
- **Letter of Undertaking (LOU)**: P&I-Club stellt ein formelles Versprechen aus das Schiff zu stellen; Arrest wird aufgehoben; Rechtsstreit geht weiter.
- **Gegenklage nach § 945 ZPO**: bei unberechtigtem Arrest; Schadensersatz für Liegekosten; entgangene Fracht; Reparaturkosten.
- **Sofortige Sicherheitsleistung**: Zahlung unter Vorbehalt; Bankbürgschaft; Schuldschein.

## Checkliste Arrest-Vorbereitung
- [ ] Seeforderung nach ISAC 1952 Art. 1 identifiziert und dokumentiert
- [ ] Schiff im Hafen bestätigt; Liegeplatz ermittelt
- [ ] Zuständiges Gericht bestimmt (LG am Liegeplatz; ZPO § 919)
- [ ] Arrestanspruch und Arrestgrund glaubhaft gemacht (Eidesstattliche Versicherung)
- [ ] Arrestantrag (ZPO § 920) vollständig vorbereitet
- [ ] Vollziehungsstrategie: Registereintragung (SchRegO § 67) plus physische Bewachung
- [ ] Freigabe-Optionen identifiziert: LOU des P&I-Clubs; Bankbürgschaft
- [ ] § 945-Schadensersatzrisiko bewertet

## Relevante Rechtsprechung
- LG Hamburg; OLG Hamburg zu Seearrest; Anforderungen an Arrestanspruch und -grund.
- BGH zur Haftung aus ungerechtfertigtem Arrest nach ZPO § 945.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release; Verhältnismäßigkeit der Sicherheitsleistung.

## Normen im Überblick
- ZPO § 916: dinglicher Arrest; Voraussetzungen; Arrestanspruch; Arrestgrund.
- ZPO §§ 917-919: besondere Arrestgründe; örtliche Zuständigkeit (Liegeplatz).
- ZPO § 920: Arrestantrag; Form; Glaubhaftmachung.
- ZPO § 929: Vollziehungsfrist 1 Monat; Wirkungsverlust bei Nichtvollziehung.
- ZPO § 945: Schadensersatz bei unberechtigtem oder wirkungslos gewordenem Arrest.
- SchRegO § 67: Eintragung von Pfändungs- und Arrestvermerken im Schiffsregister.
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest an Schwesterschiffen; Verfahren.

## Vertiefung Arrest

### Seeforderungen und ISAC 1952
Das ISAC 1952 definiert abschließend, für welche Forderungen ein Schiffsarrest zulässig ist (Art. 1). Deutschland ist Vertragsstaat; die meisten EU-Häfen ebenfalls. Im Nicht-Vertragsstaat gilt nationales Recht; die Anforderungen können abweichen.

### Arrest vs. LOU des P&I-Clubs
In der Praxis wird der Arrest häufig durch eine Letter of Undertaking (LOU) des P&I-Clubs abgewandt. Die LOU ist ein abstraktes Schuldversprechen des Clubs; sie wird nur ausgestellt, wenn die zugrundeliegende Forderung club-covered ist.

## Normen-Synopse Arrest
| Norm | Inhalt |
|------|--------|
| ZPO § 916 | Dinglicher Arrest |
| ZPO § 920 | Arrestantrag |
| ZPO § 929 | Vollziehungsfrist |
| ZPO § 945 | Schadensersatz |
| ISAC 1952 Art. 1 | Seeforderungen |

## Quellen
- ZPO §§ 916-945: https://dejure.org/gesetze/ZPO/916.html
- SchRegO § 67: https://dejure.org/gesetze/SchRegO/67.html
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- openjur LG Hamburg Arrest: https://www.openjur.de

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `auslandsflagge-local-insolvenz-reederei`

_Reederei betreibt Schiff unter Auslandsflagge (Panama; Marshall Islands; Liberia); Abstimmung mit Local Counsel für Registerfragen; Hypotheken; PSC-Verfahren. UNCLOS Art. 91-94 (genuine link; Flaggenstaat); FlaggRG §§ 1-10 (Deutsche Flagge); ISM-Code; Paris MOU Port-State-Control. Output: Local-C..._

# Auslandsflagge und Local Counsel – Flaggenstaat-Compliance

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Eine deutsche Reederei betreibt ihre Flotte unter Panama-Flagge und bekommt Port-State-Control-Mängel; Local Counsel in Panama City soll koordiniert werden. Ein Schiff unter Marshall-Islands-Flagge soll in Deutschland mit einer Hypothek belastet werden. Ein Reeder möchte von der Panama-Flagge zur Deutschen Flagge wechseln; Kosten und Anforderungen sind unklar.

## Erste Schritte
1. Flaggenregime prüfen: welches nationale Recht gilt für Schiffseigentumsrecht; Hypotheken und Seeurteile?
2. UNCLOS Art. 91-94 checken: echte Verbindung (genuine link) zwischen Schiff und Flaggenstaat.
3. ISM-DOC der Flaggenstaatsbehörde: Panama Maritime Authority; RMRS (Marshall Islands) als Ansprechpartner für DOC-Ausstellung.
4. Local-Counsel-Briefing erstellen: Registerfragen; Hypothekenrecht des Flaggenstaats; Port-State-Control-Verfahren.
5. Flaggenwechsel-Ablauf: FlaggRG §§ 3-5 für Umflaggung nach Deutschland; Abmeldung im Auslandsregister.
6. Compliance-Checkliste: SOLAS/ISM; MARPOL-Zertifikate; MLC-Zertifikat; ISPS-Code; alle unter neuer Flagge erneuern.

## Rechtsrahmen
- UNCLOS Art. 91-94: Staatsangehörigkeit von Schiffen; Flaggenstaatspflichten; genuine-link-Grundsatz.
- FlaggRG §§ 1-10: Deutsche Flagge; Berechtigung; Pflichten; Umflaggungsvoraussetzungen.
- SchRegO §§ 3-8: Eintragung im deutschen Seeschiffsregister als Voraussetzung für deutsche Flagge.
- ISM-Code Kapitel 1-13: DOC-Ausstellung durch Flaggenstaat; SMC durch Klassifikationsgesellschaft.
- MLC 2006 Titel 5 Reg. 5.1: Flaggenstaatkontrolle über MLC-Compliance.
- Paris MOU: Port-State-Control in Europa; Banning von Schiffen mit wiederholten Mängeln.

## Prüfraster
- Besteht genuine link zwischen Reeder und Flaggenstaat (UNCLOS Art. 91)?
- Hat die Flaggenstaatsbehörde alle Pflicht-Zertifikate (DOC; SMC; ISSC; DMLC) ausgestellt?
- Sind Port-State-Control-Mängel (Paris MOU / Tokyo MOU) bekannt?
- Welches Recht gilt für Schiffshypotheken im Flaggenstaat?
- Gibt es Verbote für Flaggenwechsel während laufender Zwangsvollstreckung?

## Typische Fallstricke
- Registrierung unter Auslandsflagge hebt nicht alle deutschen Schutzrechte auf; Lex registri gilt für Hypotheken.
- Hypotheken unter deutschem Recht sind im Auslandsregister nicht automatisch anerkannt.
- DOC muss auf das operativ verantwortliche Unternehmen ausgestellt sein.
- Paris-MOU-Banning kann alle europäischen Häfen sperren.

## Checkliste Local-Counsel-Beauftragung
- [ ] Local Counsel ausgewählt (Empfehlung P&I-Club-Korrespondent)
- [ ] Erfahrung des LoC mit Seerecht im Hafenstaat bestätigt
- [ ] Vollmacht ausgestellt und übermittelt
- [ ] Briefing-Dokument erstellt: Schiffsdaten; Sachverhalt; deutsches Recht
- [ ] Budgetrahmen genehmigt (P&I-Club-Approval)
- [ ] Berichtspflichten und Eskalationsweg definiert
- [ ] Prüfung ob LOU des P&I-Clubs den Arrest entbehrlich macht
- [ ] ISAC-1952-Status des Hafenstaats geprüft

## Relevante Rechtsprechung
- ITLOS Arctic Sunrise Case No. 22 (Netherlands v. Russia 2013): einstweilige Maßnahmen nach UNCLOS Art. 290; Freilassung des Schiffes.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release nach Art. 292; angemessene Sicherheitsleistung.
- EuGH zur EuGVVO 2012; gegenseitige Anerkennung von Vollstreckungstiteln in der EU.

## Normen im Überblick
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest; Verfahren; Vertragsstaat-Liste.
- EuGVVO 2012 Recast Art. 35-57: Vollstreckung ausländischer Titel in der EU.
- UNCLOS Art. 292: Prompt Release; Schiff und Crew freizulassen gegen angemessene Sicherheit.
- ZPO §§ 722-723: Vollstreckbarerklärung ausländischer Urteile in Deutschland.
- Anerkennungs- und Vollstreckungsausführungsgesetz (AVAG): nationale Umsetzung EuGVVO.

## Erweiterte Normengrundlage

### Flaggenrecht
- UNCLOS Art. 91-94: Staatszugehörigkeit; genuine link; Flaggenstaat-Pflichten.
- FlaggRG §§ 1-23: deutsche Flagge; Berechtigung; Pflichten; Entziehung.
- MAR-Register / Zweitregister: Flaggenrecht für Wirtschaftlichkeit ohne deutsche Arbeitnehmer-Quotes.

### Local Counsel
- ISAC 1952 Art. 1-8: Seeforderungen; Zuständigkeit; Verfahren im Ausland.
- EuGVVO 2012 Recast Art. 35-57: EU-weite Vollstreckung; Zuständigkeit.
- NYÜ 1958: Anerkennung ausländischer Schiedssprüche.

## Checkliste Auslandsflagge / Local Counsel
- [ ] Flaggenstaat identifiziert; Registerbehörde bekannt
- [ ] Genuine-Link-Anforderungen geprüft; erfüllt?
- [ ] Local Counsel im Flaggenstaat oder Hafenstaat beauftragt
- [ ] Vollmacht übermittelt; Briefing-Memo erstellt
- [ ] P&I-Club-Approval für Local-Counsel-Budget eingeholt
- [ ] ISAC-1952-Status des Hafenstaats geprüft

## Relevante Rechtsprechung
- ITLOS M/V Saiga No. 2 (Saint Vincent v. Guinea 1999): genuine link; Flaggenstaat-Verantwortung.
- ITLOS Arctic Sunrise No. 22 (Netherlands v. Russia 2013): einstweilige Maßnahmen nach UNCLOS Art. 290.
- EuGH zur EuGVVO 2012; gegenseitige Anerkennung von Vollstreckungstiteln in der EU.

## Quellen
- UNCLOS Art. 91-94: https://www.un.org/Depts/los/convention_agreements/texts/unclos/unclos_e.pdf
- FlaggRG: https://www.gesetze-im-internet.de/flaggrg/
- BSH ISM: https://www.bsh.de/DE/THEMEN/Schifffahrt/ISM_Code/ism_code_node.html
- Paris MOU: https://www.parismou.org
- ITLOS M/V Saiga: https://www.itlos.org/en/main/cases/list-of-cases/

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `bergung-und-wrack`

_Schiff strandet oder sinkt; Berger verlangen Bergungslohn; Wrackbeseitigung wird angeordnet. HGB §§ 574-583 (Bergung); WSG §§ 1-12 (Wrackbeseitigungsgesetz); WRC 2007 Nairobi-Uebereinkommen; LOF 2020; SCOPIC-Klausel. Output: Bergungslohn-Kalkulation; WRC-Pflichtenanalyse und Kostenrisiko-Matrix i..._

# Bergung und Wrack – Bergungslohn und Beseitigungspflicht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Ein Bergungsschlepper rettet einen havarierten Frachter in der Nordsee; der Reeder verhandelt über den Bergungslohn; der Berger droht mit Lloyd's Schiedsverfahren. Ein Schiff sinkt in der deutschen AWZ; das WSA ordnet Wrackbeseitigung an; der Eigentümer fragt nach Kostentragung. Ein P&I-Club prüft ob SCOPIC höher ist als der konventionelle Bergungslohn.

## Erste Schritte
1. Bergevertrag prüfen: LOF 2020 (Lloyd's Open Form) oder freier Bergevertrag; LOF enthält SCOPIC-Klausel.
2. Bergungslohn-Voraussetzungen: HGB § 574 – Bergungserfolg als Grundvoraussetzung.
3. Bergungslohn nach HGB §§ 577-580 berechnen: Schiffswert; Bergungsrisiko; Umweltschutz-Erfolg; Zeitaufwand.
4. WSG-Anwendbarkeit prüfen: Wrack in deutschen Gewässern; WRC 2007 ab Schiff über 300 BRZ.
5. Meldepflichten: unverzügliche Anzeige beim WSA (WRC Art. 5); Versicherungsnachweis (WRC Art. 12).
6. Schutzmaßnahmen sichern: Bunkeröl und gefährliche Stoffe sofort sichern; MARPOL-Pflichten parallel.

## Rechtsrahmen
- HGB §§ 574-583: Bergung auf See; Bergungslohn-Berechnung; Sondervergütung; Ausschlüsse.
- HGB § 577: Kriterien für Bergungslohn (Schiffswert; Gefahr; Umweltschutz-Erfolg; Zeitaufwand).
- WSG §§ 1-12: Wrackbeseitigungsgesetz; Pflichten des Eigentümers; Behörde auf Kosten des Eigentümers.
- WRC 2007 Nairobi-Übereinkommen: internationales Wrackbeseitigungsübereinkommen.
- LOF 2020: Lloyd's Open Form Bergungsvertrag; Schiedsort London/Lloyd's.
- SCOPIC 2020: Special Compensation P&I Clubs; Alternativvergütung zum HGB-Bergungslohn.

## Prüfraster
- Ist ein Bergevertrag (LOF oder freier Vertrag) geschlossen?
- Wurde die Bergung erfolgreich abgeschlossen (Erfolgserfordernis HGB § 574)?
- Übersteigen die Bergungskosten den Schiffswert; dann nur SCOPIC?
- Greift WRC 2007 (Schiff über 14 Meter; in Gewässern eines Vertragsstaats)?
- Ist P&I-Deckung für Wrackbeseitigungskosten bestätigt?

## Typische Fallstricke
- LOF-Schiedsklausel verpflichtet zu London Arbitration; deutsches Gericht ist nicht zuständig.
- SCOPIC-Aktivierung durch P&I-Club kann Bergungslohnanspruch nach HGB verdrängen.
- WRC gilt auch für Freizeitjachten ab 14 Meter Länge.
- Versicherungspflicht für Wrackbeseitigungskosten (WRC Art. 12) greift ab 300 BRZ.

## Erweiterte Normengrundlage

### Bergungsrecht
- HGB §§ 574-587: Bergung; Bergungslohn; Berechnungskriterien; Verteilungsregeln.
- LOF 2011 (Lloyd's Open Form): Standard-Bergungsvertrag; SCOPIC-Klausel.
- HGB § 576: Berücksichtigung des Umweltschutzes bei der Berechnungsmethode.

### Wrackbeseitigung
- WSG §§ 1-12: Wrackbeseitigungsgesetz; Pflichten des Eigentümers.
- WRC 2007 Nairobi: internationales Wrackbeseitigungsübereinkommen; AWZ-Anwendung.
- MARPOL Annex I Reg. 26: Bunkerölsicherheit; Gefahrenabwehr.

## Checkliste Bergungsfall
- [ ] Gefahr für Schiff und Ladung objektiv bewertet
- [ ] Freiwilligkeit der Bergungsleistung (kein Pre-existing Duty) bestätigt
- [ ] LOF oder anderen Bergungsvertrag unterzeichnet oder mündlich vereinbart
- [ ] Schiffslagen; Schiffstyp; Ladungsart für SCOPIC-Berechnung dokumentiert
- [ ] Umweltgefährdung (Bunkeröl; gefährliche Ladung) für special award bewertet
- [ ] P&I-Club zur Kostenteilung zwischen Schiff und Ladung eingebunden

## Relevante Rechtsprechung
- BGH zum Bergungslohn nach HGB § 578; Berücksichtigung des Erfolgs.
- OLG Hamburg zu SCOPIC-Klauseln; Schutz für Bergungsunternehmen bei erfolgloser Bergung.
- BGH zur Pfandhaftung des Bergungsunternehmers an Schiff und Ladung für den Bergungslohn.

## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB §§ 574-583: https://dejure.org/gesetze/HGB/574.html
- WSG: https://www.gesetze-im-internet.de/wsg/
- WRC 2007 IMO: https://www.imo.org/en/About/Conventions/Pages/Nairobi-International-Convention-on-the-Removal-of-Wrecks.aspx
- BSH: https://www.bsh.de
- LOF 2020: https://www.lloyds.com

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `bermuda-struktur-seeschiff`

_Reederei nutzt Bermuda-Holding-Struktur (SPV; Cayman/BVI-Holding): steuerliche und haftungsrechtliche Analyse. Abgrenzung Reeder vs. Ausruester (HGB §§ 476/477); Durchgriffshaftung; BEPS-Konformitaet (AStG §§ 7-14); BFH-Rechtsprechung; ISM-Code-Verantwortung. Output: Strukturanalyse-Vermerk und H..._

# Bermuda-Struktur prüfen – Holding-Struktur und Haftungsrisiken

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Ein Schiffsfonds hält seine Schiffe über Cayman-SPVs; nach einem Totalverlust fragt der Insolvenzverwalter wer wirklich Reeder und haftbar ist. Eine Bank finanziert ein Schiff das einer BVI-Gesellschaft gehört; der Reeder operiert aus Deutschland. Die Steuerbehörde prüft ob die Bermuda-Struktur BEPS-konform ist.

## Erste Schritte
1. Gesellschafts-Kaskade aufzeichnen: Eigentümer (BVI/Cayman-SPV); Reeder (HGB § 476); Ausrüster (HGB § 477).
2. Substanzprüfung der Offshore-Einheiten: Sitz; Mitarbeiter; Geschäftsführung; BEPS Action 6/13 Anforderungen.
3. ISM-Code-Verantwortung klären: ISM § 1.1.2 – Unternehmen = wer betriebliche Kontrolle hat; nicht zwingend Registereigentümer.
4. Steuerliche Analyse: AStG §§ 7-14 Hinzurechnungsbesteuerung; § 49 EStG; § 8b KStG.
5. Durchgriffshaftungsrisiko bewerten: Konzernhaftung nur in Ausnahmefällen; UNCLOS Art. 94 kann wirtschaftlichen Eigentümer identifizieren.
6. Restrukturierungsoptionen aufzeigen: BEPS-konforme Substanzschaffung.

## Rechtsrahmen
- HGB § 476: Reeder = Betreiber auf eigene Rechnung; auch Offshore-Eigentümer kann Reeder sein.
- HGB § 477: Ausrüster = wer fremdes Schiff auf eigene Rechnung betreibt; haftet wie Reeder.
- AStG §§ 7-14: Hinzurechnungsbesteuerung für passive Offshore-Einkünfte.
- KStG § 8 Abs. 2: Ort der Geschäftsleitung als Anknüpfungspunkt.
- UNCLOS Art. 94: Flaggenstaat verpflichtet zur Kontrolle; darf nicht an formale Eigentumsstruktur anknüpfen.
- ISM-Code Kap. 1.1.2: Unternehmensdefinition; betriebliche Kontrolle entscheidend.

## Prüfraster
- Hat jede Gesellschaft in der Kaskade echte wirtschaftliche Substanz?
- Ist klar wer ISM-Code-Unternehmen ist?
- Greift die Hinzurechnungsbesteuerung (AStG § 7) für Schifffahrtseinkünfte?
- Gibt es Haftungsdurchgriff auf die Holding-Ebene?
- Sind alle Gesellschaften im UBO-Register offengelegt?

## Typische Fallstricke
- Irrige Annahme der Offshore-SPV isoliere vollständig von Haftungsrisiken.
- Fehlende Substanz der Bermuda-Gesellschaft; BFH bejaht Hinzurechnung.
- ISM-DOC ausgestellt auf Managementfirma aber wirtschaftlicher Betreiber ist anders.
- KYC/AML-Anforderungen verlangen zunehmend UBO-Transparenz.

## Erweiterte Normengrundlage

### Gesellschaftsrecht
- BGB §§ 705-740: Gesellschaft bürgerlichen Rechts; Grundstruktur von SPV-Strukturen.
- GmbHG §§ 1-88: GmbH als Einschiffgesellschaft; Haftungsbegrenzung.
- Companies Act 1981 (Bermuda): Bermuda-Gesellschaftsrecht; Exempted Companies.

### Steuerrecht
- AO §§ 12-13: Betriebsstätte; Beschränkte Steuerpflicht.
- UmwStG: Einbringung in Kapitalgesellschaft; Entstrickungsbesteuerung.
- DBA Deutschland-Bermuda: kein vollständiges DBA; Anwendung nationalen Steuerrechts.

## Checkliste Bermuda-Struktur
- [ ] Gesellschaftsstruktur vollständig aufgenommen (Organogramm)
- [ ] Beneficial Owner identifiziert; UBO-Transparenz geprüft (GwG)
- [ ] Steuerliche Ansässigkeit jeder Gesellschaft bestimmt
- [ ] Substanz-Anforderungen der Bermuda-Gesellschaft geprüft
- [ ] Bankkonten und Cash-Flow-Struktur aufgenommen
- [ ] Compliance mit FATF/FATCA/CRS dokumentiert

## Relevante Rechtsprechung
- BGH zur Durchgriffshaftung bei Einschiff-SPV-Strukturen; Unterkapitalisierung.
- BFH zur Besteuerung von Bermuda-Schiffen; beschränkte Steuerpflicht inländischer Einkünfte.
- BVerwG zum Geldwäschegesetz; Transparenzregister-Pflicht für Schiffs-SPV.

## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB §§ 476/477: https://dejure.org/gesetze/HGB/476.html
- AStG §§ 7-14: https://www.gesetze-im-internet.de/astg/__7.html
- UNCLOS Art. 94: https://www.un.org/Depts/los/convention_agreements/texts/unclos/unclos_e.pdf
- ISM-Code: https://www.bsh.de/DE/THEMEN/Schifffahrt/ISM_Code/ism_code_node.html
- BFH: https://www.bfh.de

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `binnenschiff-arrest-wrackpflicht`

_Binnenschiff: Glaeubiger sichert Anspruch an Binnenmotorgueterschiff; Tanker oder Fahrgastschiff durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein..._

# Binnenschiff – Arrest vorbereiten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Ein Hypothekengläubiger will ein Binnenmotorgueterschiff; Tanker oder Fahrgastschiff arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das Binnenmotorgueterschiff; Tanker oder Fahrgastschiff im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des Binnenmotorgueterschiff; Tanker oder Fahrgastschiff konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zuständiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhörung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das Binnenmotorgueterschiff; Tanker oder Fahrgastschiff im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Vertiefung: Internationale Seearrestpraxis
International koordinieren sich Gläubiger häufig über die 1952 Brüsseler Seearrest-Konvention (ISAC 1952) und über P&I-Club-Korrespondenten. In der EU gilt ergänzend die EuGVVO 2012 (Brüssel Ia-VO) für Vollstreckung und gegenseitige Anerkennung von Arrestbeschlüssen. In Drittstaaten gelten nationaler Seearrest-Regeln; Koordination mit Local Counsel ist unverzichtbar.

## Seeforderungen nach ISAC 1952 Art. 1
Zum Arrest berechtigende Seeforderungen umfassen: Schiffsbau- und -reparaturkosten; Schiffsausrüstung; Schifffahrtsabgaben; Frachtzahlungen; Charterzahlungen; Bergungskosten; Schiffsgläubigerrechte; Konnossementsansprüche; Kollisionshaftung; Hypothekenansprüche. Nicht erfasst sind Ansprüche aus reinem Landtransport ohne Seebezug.

## Verteidigungsstrategien des Schiffseigentümers
- **Letter of Undertaking (LOU)**: P&I-Club stellt ein formelles Versprechen aus das Schiff zu stellen; Arrest wird aufgehoben; Rechtsstreit geht weiter.
- **Gegenklage nach § 945 ZPO**: bei unberechtigtem Arrest; Schadensersatz für Liegekosten; entgangene Fracht; Reparaturkosten.
- **Sofortige Sicherheitsleistung**: Zahlung unter Vorbehalt; Bankbürgschaft; Schuldschein.

## Checkliste Arrest-Vorbereitung
- [ ] Seeforderung nach ISAC 1952 Art. 1 identifiziert und dokumentiert
- [ ] Schiff im Hafen bestätigt; Liegeplatz ermittelt
- [ ] Zuständiges Gericht bestimmt (LG am Liegeplatz; ZPO § 919)
- [ ] Arrestanspruch und Arrestgrund glaubhaft gemacht (Eidesstattliche Versicherung)
- [ ] Arrestantrag (ZPO § 920) vollständig vorbereitet
- [ ] Vollziehungsstrategie: Registereintragung (SchRegO § 67) plus physische Bewachung
- [ ] Freigabe-Optionen identifiziert: LOU des P&I-Clubs; Bankbürgschaft
- [ ] § 945-Schadensersatzrisiko bewertet

## Relevante Rechtsprechung
- LG Hamburg; OLG Hamburg zu Seearrest; Anforderungen an Arrestanspruch und -grund.
- BGH zur Haftung aus ungerechtfertigtem Arrest nach ZPO § 945.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release; Verhältnismäßigkeit der Sicherheitsleistung.

## Normen im Überblick
- ZPO § 916: dinglicher Arrest; Voraussetzungen; Arrestanspruch; Arrestgrund.
- ZPO §§ 917-919: besondere Arrestgründe; örtliche Zuständigkeit (Liegeplatz).
- ZPO § 920: Arrestantrag; Form; Glaubhaftmachung.
- ZPO § 929: Vollziehungsfrist 1 Monat; Wirkungsverlust bei Nichtvollziehung.
- ZPO § 945: Schadensersatz bei unberechtigtem oder wirkungslos gewordenem Arrest.
- SchRegO § 67: Eintragung von Pfändungs- und Arrestvermerken im Schiffsregister.
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest an Schwesterschiffen; Verfahren.

## Vertiefung Arrest

### Seeforderungen und ISAC 1952
Das ISAC 1952 definiert abschließend, für welche Forderungen ein Schiffsarrest zulässig ist (Art. 1). Deutschland ist Vertragsstaat; die meisten EU-Häfen ebenfalls. Im Nicht-Vertragsstaat gilt nationales Recht; die Anforderungen können abweichen.

### Arrest vs. LOU des P&I-Clubs
In der Praxis wird der Arrest häufig durch eine Letter of Undertaking (LOU) des P&I-Clubs abgewandt. Die LOU ist ein abstraktes Schuldversprechen des Clubs; sie wird nur ausgestellt, wenn die zugrundeliegende Forderung club-covered ist.

## Normen-Synopse Arrest
| Norm | Inhalt |
|------|--------|
| ZPO § 916 | Dinglicher Arrest |
| ZPO § 920 | Arrestantrag |
| ZPO § 929 | Vollziehungsfrist |
| ZPO § 945 | Schadensersatz |
| ISAC 1952 Art. 1 | Seeforderungen |

## Quellen
- ZPO §§ 916-945: https://dejure.org/gesetze/ZPO/916.html
- SchRegO § 67: https://dejure.org/gesetze/SchRegO/67.html
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- openjur LG Hamburg Arrest: https://www.openjur.de

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `binnenschiff-closing-planen`

_Binnenschiff: Closing eines Binnenmotorgueterschiff; Tanker oder Fahrgastschiff-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan im Seerecht Schiff..._

# Binnenschiff – Closing planen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Der Kauf eines Binnenmotorgueterschiff; Tanker oder Fahrgastschiff soll abgeschlossen werden; Hypotheken sind abzulösen. Ein Käufer besteht auf lastenfreier Lieferung mit gültiger Klasse und MLC-Zertifikat. Eine Bank koordiniert das Closing bei syndizierten Finanzierungen.

## Erste Schritte
1. Ablosebetraege aller Hypothekenglaeubiger anfordern; Stichtag abstimmen.
2. Loeschungsbewilligungen (SchRG § 19) beschaffen; zeitlich koordinieren.
3. Escrow-Konto einrichten: Kaufpreis gegen Loeschungsbestaetigung.
4. Eigentumsuebergang (SchRG § 2) und Hypothekenloesung gleichzeitig für Binnenmotorgueterschiff; Tanker oder Fahrgastschiff.
5. Zertifikate (Klasse; ISM; MLC; ISPS) auf neuen Eigentuemer ummelden.
6. Registerauszug nach Closing beschaffen; Closing-Memo erstellen.

## Rechtsrahmen
- SchRG §§ 2/19; SchRegO §§ 13-19; FlaggRG §§ 3-5; ISM-Code Kap. 3 SMC-Neuzertifizierung.

## Prüfraster
- Sind alle Loeschungsbewilligungen zeitlich koordiniert?
- Ist der Escrow-Mechanismus wasserdicht gegen Insolvenz des Verkaeufers?
- Sind alle Zertifikate für Binnenmotorgueterschiff; Tanker oder Fahrgastschiff auf neuen Eigentuemer vorbereitet?
- Ist der Flaggenwechsel (wenn vorgesehen) vorbereitet?
- Ist die Vollmacht für den Registerantrag aktuell?

## Typische Fallstricke
- Zahlung ohne simultane Loeschung: Hypothek bleibt trotz Zahlung eingetragen.
- ISM-/MLC-Luecke nach Eigentumsuebergang; Port-State-Detention droht.
- Nachranghypotheken blockieren Closing wenn Erstrangglaeubigerbank nicht kooperiert.

## Vertiefung: Closing-Mechanismus im Schiffskauf
Das Closing eines Schiffskaufs ist der Moment wo Eigentum und Risiko auf den Käufer übergehen. Technisch besteht das Closing aus: (1) Zahlung des Kaufpreises (oder freigabe aus Escrow); (2) Übergabe der Delivery Documents; (3) Eintragung des Eigentumsübergangs im Schiffsregister (SchRG § 2). Alle drei Schritte sollen simultan erfolgen; in der Praxis nutzt man Softclose-Mechanismen.

## Delivery Documents Checkliste
Folgende Originalunterlagen müssen beim Closing übergeben werden: Klasse-Zertifikat; Delivery and Acceptance Certificate; Protokoll zur Übergabe von Bunker und Schmieröl; alle Schiffszertifikate (IOPP; IAPP; MLC; ISSC; BSH-Fahrterlaubnis); Logbücher; technische Handbücher. Kopien werden bei der abgebenden Reederei archiviert.

## Nachsorge nach dem Closing
Nach dem Closing: Neuanmeldung beim Flaggenregister; Beantragung neuer DOC beim ISM-Code-Unternehmen; MLC-Erneuerung; P&I-Club-Eintritt des Käufers; Benachrichtigung aller Charterer und Hafenbehörden über den Eigentümerwechsel. Closing-Memo erstellen mit Datum; Kaufpreis; alle übergebenen Dokumente; Beteiligten.

## Checkliste Closing-Vorbereitung
- [ ] Ablösebeträge aller Hypothekengläubiger angefordert; Stichtag fixiert
- [ ] Löschungsbewilligungen (SchRG § 19) von allen Gläubigern vorliegend
- [ ] Escrow-Konto eingerichtet; Escrow-Agent benannt
- [ ] Eigentumsübergang (SchRG § 2) und Hypothekenlöschung zeitlich koordiniert
- [ ] Alle Zertifikate (Klasse; ISM/DOC/SMC; MLC/DMLC; ISSC; BSH) auf neuen Eigentümer vorbereitet
- [ ] P&I-Club-Eintritt des Käufers bestätigt
- [ ] Delivery and Acceptance Certificate vorbereitet
- [ ] Registerauszug nach Closing beauftragt
- [ ] Closing-Memo-Vorlage bereitgestellt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit des Eigentumsübergangs an Schiffen; Einigung und Eintragung als konstitutive Voraussetzungen.
- OLG Hamburg zur Auslegung von Closing-Conditions in MOA-Verträgen; Delivery-Condition-Klauseln.
- BGH zur Haftung des Verkäufers für nach Closing entstehende Schiffsgläubigerrechte; Freistellungspflicht.

## Normen im Überblick
- SchRG § 2: Eigentumsübergang durch Einigung und Eintragung; nicht durch Besitzübergabe.
- SchRG § 19: Löschung der Hypothek; Form; Zeitpunkt; Wirkung.
- SchRegO §§ 13-19: Eintragungsverfahren; Antragsteller; Fristen.
- FlaggRG §§ 3-5: Berechtigung zur Flagge; Pflichten bei Eigentumsübergang.
- ISM-Code Kap. 3: SMC-Gültigkeit und Neuausstellung nach Eigentümerwechsel.
- MLC 2006 Reg. 5.1.3: Neuausstellung MLC-Zertifikat nach Eigentumsübergang und Flaggenwechsel.

## Vertiefung Closing

### Simultaneous Closing
Das "simultaneous closing" (Zug-um-Zug-Abwicklung) ist bei Schiffsverkäufen mit Kreditfinanzierung Standard. Ablöse der Altfinanzierung; Neuhypothek für den Käufer; Eigentumsumschreibung; Kaufpreiszahlung — alles erfolgt zeitgleich über ein Escrow-Konto.

### Zertifikatsübergang
Klasse- und ISM-Zertifikate bleiben nicht automatisch mit dem Schiff verbunden; sie sind personengebunden (SMC an den Reeder; DOC an den Betreiber). Der Käufer muss rechtzeitig seine eigene ISM-Zulassung (DOC) und das SMC für das Schiff beantragen.

## Normen-Synopse Closing
| Norm | Inhalt |
|------|--------|
| SchRG § 2 | Eigentumsübergang |
| SchRG § 19 | Hypothekenlöschung |
| FlaggRG § 3 | Flagge bei Eigentümerwechsel |
| MLC Reg. 5.1.3 | MLC-Zertifikat |

## Quellen
- SchRG §§ 2/19: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- FlaggRG: https://www.gesetze-im-internet.de/flaggrg/
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- SchRegO: https://dejure.org/gesetze/SchRegO

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `binnenschiff-hypothek-bestellen`

_Binnenschiff: Binnenschiffer; Verladungsunternehmen; Kreditinstitut bestellt Schiffshypothek als Sicherheit für Finanzierung eines Binnenmotorgueterschiff; Tanker oder Fahrgastschiff. BinSchG §§ 1-133; SchRG §§ 1-75 für eingetragene Binnenschiffe; BinSchRegO. Notarielle Bestellungsurkunde, Rangst..._

# Binnenschiff – Schiffshypothek bestellen

## Arbeitsbereich

Binnenschiff: Binnenschiffer; Verladungsunternehmen; Kreditinstitut bestellt Schiffshypothek als Sicherheit für Finanzierung eines Binnenmotorgueterschiff; Tanker oder Fahrgastschiff. BinSchG §§ 1-133; SchRG §§ 1-75 für eingetragene Binnenschiffe; BinSchRegO. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall
Eine Bank bestellt eine Hypothek auf ein Binnenmotorgueterschiff; Tanker oder Fahrgastschiff als Sicherheit für einen Schiffskredit. Ein Reeder sucht Zwischenfinanzierung und bietet sein Binnenmotorgueterschiff; Tanker oder Fahrgastschiff als Sicherheit an. Eine Bestandshypothek soll auf eine neue Kredittranche erstreckt werden.

## Erste Schritte
1. Eintragungsfaehigkeit des Binnenmotorgueterschiff; Tanker oder Fahrgastschiffs pruefen; Eintragung im Binnenschiffsregister (AG Duisburg-Ruhrort) bestaetigen.
2. Sicherungsabrede aufsetzen: gesicherte Forderungen, Kuendigungsrechte, Cross-Default.
3. Notarielle Hypothekenbestellungsurkunde nach SchRG §§ 8-18 erstellen.
4. Vertretungsbefugnis des Eigentuemers pruefen; ggf. Handelsregisterauszug.
5. Eintragungsantrag beim {reg_type}-Gericht stellen; Rangstelle fruehzeitig reservieren.
6. Eintragungsbestaetigung und ggf. Hypothekenbrief sichern; Sicherungsvertrag archivieren.

## Rechtsrahmen
- BinSchG §§ 1-133; SchRG §§ 1-75 für eingetragene Binnenschiffe; BinSchRegO; SchRG § 31 Zubehoer-Mithaftung; SchRG § 75 Hoechstbetragshypothek; SchRegO §§ 13-19. ADN-Gefahrgut Binnenwasserstrassen; RheinSchPersV; CESNI-Standards.

## Prüfraster
- Ist das Binnenmotorgueterschiff; Tanker oder Fahrgastschiff im Binnenschiffsregister (AG Duisburg-Ruhrort) eingetragen und eintragungsfaehig?
- Ist die Sicherungsabrede vollstaendig und rechtswirksam?
- Ist Zubehoer-Mithaftung (SchRG § 31) vertraglich gesichert?
- Ist die notarielle Form eingehalten (SchRG § 17)?
- Ist der Rangstellen-Antrag fruehzeitig gestellt?

## Typische Fallstricke
- Fehlende notarielle Form fuehrt zur Nichtigkeit der Hypothek (SchRG § 17).
- Rang entsteht mit Antragstellung; fruehzeitig beim Binnenschiffsregister (AG Duisburg-Ruhrort)-Gericht stellen.
- Briefhypothek verliert Vollstreckungswert bei Verlust des Hypothekenbriefs.

## Vertiefung: Hypothekenarten im deutschen Schiffsrecht
Das SchRG kennt die Verkehrshypothek (§§ 8-30) und die Höchstbetragshypothek (§ 75). Die Verkehrshypothek ist an eine bestimmte Forderung gebunden; die Höchstbetragshypothek sichert variable Forderungen bis zu einem eingetragenen Maximalbetrag und eignet sich für revolvierende Kreditlinien. In der Praxis der Schiffsfinanzierung dominiert die Hypothekenbestellung als erstrangige Höchstbetragshypothek zugunsten der Konsortialführerbank.

## Verfahrensablauf Hypothekenbestellung
1. **Vor der Bestellung**: Eintragungsfähigkeit prüfen; Rangstelle reservieren (SchRegO § 13); Sicherungsabrede verhandeln.
2. **Bestellung**: Notarielle Bestellungsurkunde; Unterschriften des Eigentümers; Vollmachten (ggf. notariell beglaubigt).
3. **Eintragung**: Antrag beim Registergericht; Vorlage der Bestellungsurkunde; Eintragungsgebühr.
4. **Nach der Eintragung**: Registerauszug beschaffen; Sicherungsvertrag und Registerauszug archivieren; Mortgagee's Interest Insurance prüfen.

## Praktische Hinweise
In Konsortialkrediten hält eine Sicherheitentreuhänderin (Security Trustee) die Hypothek für alle Konsortialmitglieder. Die Hypothek kann jederzeit abgetreten werden (SchRG §§ 35-58); für die Abtretung ist Briefübergabe oder Eintragung erforderlich je nach Hypothekenart.

## Checkliste Hypothekenbestellung
- [ ] Eintragungsfähigkeit des Schiffes bestätigt (SchRG § 1)
- [ ] Eigentümer mit Vollmacht zur Hypothekenbestellung legitimiert
- [ ] Sicherungsabrede (Security Agreement / Credit Agreement) unterzeichnet
- [ ] Notarielle Hypothekenbestellungsurkunde erstellt und unterzeichnet
- [ ] Eintragungsantrag beim Registergericht gestellt; Rangstelle reserviert
- [ ] Mithaftung des Zubehörs (SchRG § 31) vertraglich vereinbart
- [ ] Eintragungsbestätigung und ggf. Hypothekenbrief gesichert
- [ ] Mortgagee's Interest Insurance (MII) beantragt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit der notariellen Hypothekenbestellungsurkunde; Formerfordernisse SchRG § 17.
- BGH zur Mithaftung des Zubehörs nach SchRG § 31; Abgrenzung Schiffszubehör von persönlichem Eigentum des Kapitäns.
- OLG Hamburg zur Rangfolge bei gleichzeitig beantragten Hypotheken; Zeitpunkt der Antragstellung maßgeblich.

## Normen im Überblick
- SchRG § 8: Begründung der Schiffshypothek durch Einigung und Eintragung.
- SchRG §§ 9-14: Inhalt der Eintragungsurkunde; Form; Unterschriften.
- SchRG §§ 15-18: Eintragungsvoraussetzungen; notarielle Form.
- SchRG §§ 35-58: Übertragung der Hypothek; Abtretung; Pfändung.
- SchRG § 59: Rangfolge; ältere Hypothek geht jüngerer vor.
- SchRG § 75: Höchstbetragshypothek für revolvierende Kredite.
- InsO § 49: Absonderungsrecht des Hypothekengläubigers in der Insolvenz des Reeders.

## Quellen
- SchRG §§ 8-18: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- SchRegO §§ 13-19: https://dejure.org/gesetze/SchRegO
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- dejure SchRG § 75: https://dejure.org/gesetze/SchRG/75.html

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 WSG
- § 267 StGB
- § 49 EStG
- § 8b KStG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

