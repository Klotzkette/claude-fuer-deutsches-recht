# NDA-Abgleich

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`nda-abgleich`) | [`nda-abgleich.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nda-abgleich.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Waldkrone HealthTech GmbH - NDA, Meldekanal und Lieferantenhinweis** (`hinweisgeberschutz-nda-meldekanal-waldkrone`) | [Gesamt-PDF lesen](../testakten/hinweisgeberschutz-nda-meldekanal-waldkrone/gesamt-pdf/hinweisgeberschutz-nda-meldekanal-waldkrone_gesamt.pdf) | [`testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip) |
| **NDA-Vertragsabgleich Windsysteme Norderhof AG / Eickmann Wirtschaftspartner Pte. Ltd. — Joint Venture, GeschGehG, Exportkontrolle** (`nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft`) | [Gesamt-PDF lesen](../testakten/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft/gesamt-pdf/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft_gesamt.pdf) | [`testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

NDA-Verhandlungshilfe für die empfangende Seite. Akzeptiert den Entwurf der Gegenseite und setzt den eigenen Standard chirurgisch durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Word-Tracked-Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `nda-abgleich` | NDA-Verhandlungshilfe für die empfangende Seite. Zwei Modi: (A) Standard-Destillation aus 1 bis n eigenen NDAs und frei beschreibbarer Erfahrung in einen konsolidierten Haltelinien-Standard mit Ampelmatrix ROT/GELB/G… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 85 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aenderungsmodus-compliance-dokumentation` | Aenderungsmodus: Compliance-Dokumentation und Aktenvermerk im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwel... |
| `aenderungsmodus-compliance-dokumentation-und-akte` | Aenderungsmodus: Compliance-Dokumentation und Aktenvermerk im Plugin nda abgleich im NDA-Abgleich. |
| `ampelmatrix-internationaler-bezug-schnittstellen` | Ampelmatrix: Internationaler Bezug und Schnittstellen im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Z... |
| `ampelmatrix-internationaler-bezug-und-schnittstellen` | Ampelmatrix: Internationaler Bezug und Schnittstellen im Plugin nda abgleich im NDA-Abgleich. |
| `anschluss-routing` | Anschluss-Routing für NDA-Abgleich: wählt den nächsten Spezial-Skill nach Engpass (Geltungsdauer NDA (5-10 Jahre), NDA-Entwurf, Mustervorlage, Vorvertrags-Korrespondenz), dokumentiert Router-Entscheidung mit Begründung. |
| `arbeitnehmer-kuendigung` | Empfangende Seite soll NDA der Gegenseite prüfen und verhandeln oder Kanzlei will aus mehreren NDAs einen eigenen Standard destillieren. NDA-Verhandlungshilfe. Modus A Destillation: 1 bis n eigene NDAs in konsolidierten Haltelinien-Stand... |
| `ausgabe-changes-docx-beweislast` | Ausgabe: Mandantenkommunikation und Entscheidungsvorlage im Plugin nda abgleich im NDA-Abgleich. |
| `ausgabe-mandantenkommunikation-entscheidungsvorlage` | Ausgabe: Mandantenkommunikation und Entscheidungsvorlage im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `changes-abschlussprodukt-uebergabe` | Changes: Abschlussprodukt und Übergabe im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktio... |
| `changes-abschlussprodukt-und-uebergabe` | Changes: Abschlussprodukt und Übergabe im Plugin nda abgleich im NDA-Abgleich. |
| `chirurgisch-quellenkarte` | Chirurgisch Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im NDA-Abgleich: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits... |
| `docx-beweislast-darlegungslast` | Docx: Beweislast, Darlegungslast und Substantiierung im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Za... |
| `docx-beweislast-und-darlegungslast` | Docx: Beweislast, Darlegungslast und Substantiierung im Plugin nda abgleich im NDA-Abgleich. |
| `dokumente-intake` | Dokumentenintake für NDA-Abgleich: sortiert NDA-Entwurf, Mustervorlage, Vorvertrags-Korrespondenz, prüft Datum, Absender, Frist und Beweiswert (Versionsverlauf, Mailverkehr); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `durch-interessen` | Durch: Mehrparteienkonflikt und Interessenmatrix im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlun... |
| `durch-interessen-echten-sonderfall-eigenen` | Durch: Mehrparteienkonflikt und Interessenmatrix im Plugin nda abgleich im NDA-Abgleich. |
| `echten-sonderfall-edge-case` | Echten: Sonderfall und Edge-Case-Prüfung im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sankt... |
| `echten-sonderfall-und-edge-case` | Echten: Sonderfall und Edge-Case-Prüfung im Plugin nda abgleich im NDA-Abgleich. |
| `eigenen-risikoampel-gegenargumente` | Eigenen: Risikoampel, Gegenargumente und Verteidigungslinien im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schw... |
| `eigenen-risikoampel-und-gegenargumente` | Eigenen: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin nda abgleich im NDA-Abgleich. |
| `einstieg-routing` | Einstieg, Triage und Routing für NDA-Abgleich: ordnet Rolle (Vertragspartner, Berater, Aufsichtsorgan), markiert Frist (Geltungsdauer NDA (5-10 Jahre)), wählt Norm (BGB §§ 145 ff., 280/339, GeschGehG, DSGVO Art. 28) und Zuständigkeit (zu... |
| `entwurf-tatbestand-beweis-und-belege` | Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin nda abgleich im NDA-Abgleich. |
| `entwurf-tatbestandsmerkmale-beweisfragen-beleglage` | Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im NDA-Abgleich: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `gegen-dokumentenmatrix-und-lueckenliste` | Gegen: Dokumentenmatrix, Lückenliste und Nachforderung: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `gegen-gelb-gleicht` | Gegen: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin nda abgleich im NDA-Abgleich. |
| `gegenseite-fristen-form-zustaendigkeit-rechtsweg` | Gegenseite: Fristen, Form, Zuständigkeit und Rechtsweg im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle,... |
| `gegenseite-tracked-fristennotiz-nda` | Gegenseite: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin nda abgleich im NDA-Abgleich. |
| `gelb-formular-portal-einreichungslogik` | Gelb: Formular, Portal und Einreichungslogik im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, S... |
| `gelb-formular-portal-und-einreichung` | Gelb: Formular, Portal und Einreichungslogik im Plugin nda abgleich im NDA-Abgleich. |
| `geschaeftsgeheimnis-geschgehg` | NDA als angemessene Geheimhaltungsmassnahme i. S. § 2 Nr. 1 b GeschGehG: NDA allein reicht nicht, technisch-organisatorische Massnahmen erforderlich (Zugangsschutz, Klassifizierung, Logging). Pruefraster im NDA-Abgleich. |
| `gleicht-erstpruefung-rollenklaerung-mandatsziel` | Gleicht: Erstprüfung, Rollenklärung und Mandatsziel im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zah... |
| `gleicht-erstpruefung-und-mandatsziel` | Gleicht: Erstprüfung, Rollenklärung und Mandatsziel im Plugin nda abgleich im NDA-Abgleich. |
| `gruen-fehlerkatalog` | Gruen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `haltelinien-setzt-standard` | Haltelinien: Verhandlung, Vergleich und Eskalation im Plugin nda abgleich im NDA-Abgleich. |
| `haltelinien-verhandlung-vergleich-eskalation` | Haltelinien: Verhandlung, Vergleich und Eskalation im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahl... |
| `it-saas-laufzeit-survival-m-a` | NDA für SaaS-/IT-Vendor-Pitches: Cloud-Hosting, Datentrennung, Subprozessoren, Audit-Rechte, Penetration-Testing-Erlaubnis. Empfehlung: nicht-exklusive Lizenz für Test-Daten, klare Loeschpflicht nach Pitch im NDA-Abgleich. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im NDA Abgleich-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-U... |
| `m-a-aenderungsmodus-ampelmatrix` | NDA vor M&A-Data-Room: enge Zweckbindung (Pruefung Transaktion), Standstill-Klausel, Non-Solicit, Verbot Reverse-Engineering. Empfehlung: separater Clean Team Agreement für Kartell-/Wettbewerbsdaten im NDA-Abgleich. |
| `mandantenkommunikation` | Mandantenkommunikation im NDA-Abgleich: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen bereits vor? |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im NDA-Abgleich. |
| `mitarbeiter-need-non-solicit-permitted` | Mitarbeiter und Need-to-Know: NDA verpflichtet Mitarbeiter ueber Arbeitsvertrag, externe Berater nur ueber separate NDA oder Backup-Klausel. Empfehlung: Liste freigegebener Personen, Bestaetigung Mitarbeiter-NDA, kein Datenraum-Zugriff o... |
| `nda-abgleich` | Empfangende Seite soll NDA der Gegenseite prüfen und verhandeln oder Kanzlei will aus mehreren NDAs einen eigenen Standard destillieren. NDA-Verhandlungshilfe. Modus A Destillation: 1 bis n eigene NDAs in konsolidierten Haltelinien-Stand... |
| `nda-anwendbares-recht-gerichtsstand` | Anwendbares Recht und Gerichtsstand bei NDA: Empfehlung deutsches Recht + LG Sitz des Discloser; Schiedsklausel (DIS Regeln) ab hoeherer Bedeutung. Pruefraster: internationale NDAs vs. nationale, Verbraucherbeteiligung. |
| `nda-bei-arbeitnehmer-kuendigung` | Post-Termination-NDA bei Arbeitnehmer-Kuendigung: Wirksamkeit, Karenzentschaedigung § 74 HGB analog, Reichweite (keine generelle Wettbewerbssperre). Schnittstelle Arbeitsrecht. Empfehlung: nur ergaenzend zu nachvertraglichem Wettbewerbsv... |
| `nda-bei-bewerbungen-pitches` | NDA bei Bewerbungen/Pitches/Investorengespraechen: Investor-NDAs sind ungewoehnlich; ueblich nur enge Mutual-NDAs für fortgeschrittene Stage. Empfehlung: nicht beleidigt sein, wenn VC unterschreibt nicht; Verhandlungsstrategie. |
| `nda-bei-r-d-kooperation` | NDA bei F&E-Kooperation: Background-IP / Foreground-IP-Trennung, IP-Zuordnung bei gemeinsamer Erfindung, Foerderrechtshinweise (BMBF/EU). Empfehlung: NDA + Pre-LoI mit IP-Grundsaetzen. |
| `nda-definitionsklausel-abgleichen` | Definitionsklausel 'Vertrauliche Information' abgleichen: weiter Begriff (alle Informationen) vs. eng definiert (nur als vertraulich markiert). Empfehlung je nach Rolle: Discloser will weit, Recipient will eng. Wortlautempfehlungen. |
| `nda-grundstruktur-pruefen` | NDA-Grundstruktur pruefen: Parteien, Zweck der Offenlegung, Definition Vertrauliche Information, Pflichten, Laufzeit, Aufbewahrung/Rueckgabe, Vertragsstrafe, Geheimhaltungsdauer nach Vertragsende, Jurisdiction. Pruefraster gegen marktueb... |
| `nda-international-arbitration-spezial` | Spezialfall internationale NDAs und Schiedsklauseln: Rechtswahl, Schiedsort, einstweiliger Rechtsschutz, Common-Law-Begriffe Equity. Pruefraster für Cross-Border-Mandat. |
| `nda-it-saas-vendor` | NDA für SaaS-/IT-Vendor-Pitches: Cloud-Hosting, Datentrennung, Subprozessoren, Audit-Rechte, Penetration-Testing-Erlaubnis. Empfehlung: nicht-exklusive Lizenz für Test-Daten, klare Loeschpflicht nach Pitch. |
| `nda-laufzeit-und-survival` | Laufzeit und Survival der Geheimhaltungspflicht: Festlaufzeit, automatische Verlaengerung, Survival 2/3/5 Jahre nach Vertragsende. Bei Geschäftsgeheimnissen i. S. GeschGehG ist Survival 'so lange die Information Geschaeftsgeheimnis ist'... |
| `nda-m-und-a-clean-team-spezial` | Spezialfall NDA für M-and-A und Clean-Team-Arrangements: Datenraum, Sondervertraulichkeit Wettbewerbsdaten, Kartellrecht. Pruefraster für Antitrust-Counsel. |
| `nda-mit-geschaeftsgeheimnis-geschgehg` | NDA als angemessene Geheimhaltungsmassnahme i. S. § 2 Nr. 1 b GeschGehG: NDA allein reicht nicht, technisch-organisatorische Massnahmen erforderlich (Zugangsschutz, Klassifizierung, Logging). Pruefraster. |
| `nda-mit-kartellsensitiven-daten` | NDA mit kartellsensitiven Daten (Preise, Mengen, Kunden): Clean Team Agreement, Aggregation, externe Berater zwischen den Parteien. Empfehlung: Vorabklaerung ob Daten ueberhaupt ausgetauscht werden duerfen. |
| `nda-mit-personenbezogenen-daten` | NDA mit personenbezogenen Daten: ggf. AV-Vertrag § 28 BDSG / Art. 28 DSGVO erforderlich, gemeinsame Verantwortlichkeit Art. 26 DSGVO pruefen. NDA ersetzt AV nicht. Empfehlung: separater AVV anlagengeb. |
| `nda-mitarbeiter-need-to-know` | Mitarbeiter und Need-to-Know: NDA verpflichtet Mitarbeiter ueber Arbeitsvertrag, externe Berater nur ueber separate NDA oder Backup-Klausel. Empfehlung: Liste freigegebener Personen, Bestaetigung Mitarbeiter-NDA, kein Datenraum-Zugriff o... |
| `nda-non-solicit-kartellrechtlich` | Non-Solicit in NDA kartellrechtlich pruefen: zeitlich begrenzt (12-24 Monate), sachlich begrenzt (nur für NDA-Zweck involvierte Mitarbeiter), keine generelle Bewerbungs-Sperre. Andernfalls Risiko § 1 GWB / Art. 101 AEUV. |
| `nda-permitted-disclosure` | Permitted Disclosure: Konzern, Beraterklausel, gesetzliche Offenlegungspflichten (Aufsicht, Strafverfolgung, Gericht). Standard-Wortlaut und typische Fallstricke (z. B. Konzernbegriff zu eng). |
| `nda-rueckgabe-vernichtung` | Rueckgabe und Vernichtung Vertraulicher Information: Pflicht, Bestaetigung, Backup-Ausnahme (technisch unmoeglich zu loeschende Backups). Bei Daten in Cloud: Loeschbestaetigung Vendor erforderlich. Wortlautempfehlungen. |
| `nda-standardklauseln-bauleiter` | Bauleiter NDA-Standardklauseln: Vertraulichkeitsumfang, Empfaengerkreis, Laufzeit, Rechtsfolgen, Schriftform. Pruefraster für mutual und one-way NDA. |
| `nda-typen-vergleich` | NDA-Typen vergleichen: einseitig (unilateral), gegenseitig (mutual), mehrparteiig. Empfehlung pro Situation: Verkaeufer in M&A unilateral; gemeinsame Entwicklung mutual; Konsortium mehrparteiig. Praxisanker für Templates. |
| `nda-vergleichsmatrix-leitfaden` | Leitfaden NDA-Vergleichsmatrix: relevante Klauseln vergleichen, Markup, Risikoampel, Wechselwirkungen mit Geschaeftsgeheimnisgesetz. Pruefraster für Reviewteam. |
| `nda-vertragsstrafe-pruefen` | Vertragsstrafe pruefen: Hoehe, AGB-Kontrolle §§ 305 ff. BGB, Bestimmtheitsgrundsatz, Schadensersatzkumulation oder Anrechnung. Bei Verbraucher-NDA strengere Grenzen. Bei B2B-Standard: ueblich 5000-25000 EUR pro Vorfall, Kumulation moeglich. |
| `nda-vor-m-a-data-room` | NDA vor M&A-Data-Room: enge Zweckbindung (Pruefung Transaktion), Standstill-Klausel, Non-Solicit, Verbot Reverse-Engineering. Empfehlung: separater Clean Team Agreement für Kartell-/Wettbewerbsdaten. |
| `output-waehlen` | Output-Wahl für NDA-Abgleich: stimmt Adressat (Vertragspartner, Berater, Aufsichtsorgan), Frist (Geltungsdauer NDA (5-10 Jahre)) und Form auf den Zweck ab — typische Outputs: Markup mit Kommentaren, Issue List, Mandantenmemo Risiken. |
| `quellen-livecheck` | Quellen-Live-Check für NDA-Abgleich: prüft Normen (BGB §§ 145 ff., 280/339, GeschGehG, DSGVO Art. 28) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt zuständige Stelle und Quellenhygiene nach references/quellenhyg... |
| `r-d-nda-grundstruktur-international` | NDA bei F&E-Kooperation: Background-IP / Foreground-IP-Trennung, IP-Zuordnung bei gemeinsamer Erfindung, Foerderrechtshinweise (BMBF/EU). Empfehlung: NDA + Pre-LoI mit IP-Grundsaetzen im NDA-Abgleich. |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `rueckgabe-vernichtung-nda-typen` | Rueckgabe und Vernichtung Vertraulicher Information: Pflicht, Bestaetigung, Backup-Ausnahme (technisch unmoeglich zu loeschende Backups). Bei Daten in Cloud: Loeschbestaetigung Vendor erforderlich. Wortlautempfehlungen im NDA-Abgleich. |
| `setzt-schriftsatz-brief-memo-bausteine` | Setzt: Schriftsatz-, Brief- und Memo-Bausteine im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung,... |
| `setzt-schriftsatz-brief-und-memo-bausteine` | Setzt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin nda abgleich im NDA-Abgleich. |
| `standard` | Standard: Behörden-, Gerichts- oder Registerweg im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung... |
| `standard-behoerden-gericht-und-registerweg` | Standard: Behörden-, Gerichts- oder Registerweg im Plugin nda abgleich im NDA-Abgleich. |
| `standardklauseln-bauleiter-nda-vertragsstrafe` | Bauleiter NDA-Standardklauseln: Vertraulichkeitsumfang, Empfaengerkreis, Laufzeit, Rechtsfolgen, Schriftform. Pruefraster für mutual und one-way NDA im NDA-Abgleich. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im NDA Abgleich-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-U... |
| `tracked-fristennotiz-naechster-schritt` | Tracked: Fristennotiz und nächster Schritt im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, San... |
| `tracked-fristennotiz-und-naechster-schritt` | Tracked: Fristennotiz und nächster Schritt im Plugin nda abgleich im NDA-Abgleich. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für NDA-Abgleich: trennt fehlende Tatsachen von fehlenden Belegen (NDA-Entwurf, Mustervorlage, Vorvertrags-Korrespondenz), nennt pro Lücke Beweisthema, Beschaffungsweg (zuständige Stelle), Frist und Ersatzna... |
| `word` | Word im NDA-Abgleich im NDA-Abgleich. |
| `word-zahlen-schwellenwerte-berechnung` | Word: Zahlen, Schwellenwerte und Berechnung im NDA-Abgleich: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sa... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im NDA-Abgleich. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im NDA-Abgleich. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im NDA-Abgleich. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
