# Forschungszulage-Antragstellung

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`forschungszulage-antragstellung.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/forschungszulage-antragstellung.md) (57 KB)
- Im Repo: [`testakten/megaprompts/forschungszulage-antragstellung.md`](../testakten/megaprompts/forschungszulage-antragstellung.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forschungszulage-antragstellung`) | [`forschungszulage-antragstellung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Forschungszulage Riedblick Sensorik GmbH** (`forschungszulage-sensorik-startup-taunus`) | [Gesamt-PDF lesen](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die steuerliche Forschungsförderung nach dem Forschungszulagengesetz: Fördercheck, BSFZ-Bescheinigung, Projektbeschreibung, FuE-Abgrenzung, Bemessungsgrundlage, Finanzamt-Antrag, Auszahlung, Verlust-/Krisenlage, Dokumentation für Außenprüfung, Kumulierung und Nachbesserung.

Das Plugin ist für Unternehmen, Start-ups, Mittelstand, Steuerberaterinnen, Rechtsanwälte, CFOs und Produkt-/Entwicklungsteams gebaut. Es übersetzt technische Entwicklung in die Sprache, die BSFZ und Finanzamt brauchen: Neuheit, Risiko, systematisches Vorgehen, förderfähige Aufwendungen und saubere Belege. Es kann bewusst zwei Geschwindigkeiten: geführter Modus für Einsteiger und harter Ampel-/Cashflow-Modus für Profis.

## Quellen-Gate

Vor jeder belastbaren Ausgabe live prüfen:

- Forschungszulagengesetz auf `gesetze-im-internet.de`, insbesondere §§ 1 bis 7 und § 10 FZulG.
- BSFZ-Antragsverfahren: zweistufig, erst FuE-Bescheinigung bei der BSFZ, dann Antrag beim Finanzamt.
- BMF-Forschungszulage und BMF-Schreiben vom 07.02.2023, soweit noch nicht durch ein neues finales Schreiben ersetzt.
- Änderungen ab 2026: Bemessungsgrundlagenhöchstbetrag 12 Mio. Euro, 20-%-Pauschale für Gemein- und Betriebskosten bei nach dem 31.12.2025 begonnenen Vorhaben, Eigenleistung 100 Euro pro Stunde bis max. 40 Stunden/Woche.

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `forschungszulage-antragstellung-allgemein` | Einstieg, Triage, Förderroute und Projektaufnahme |
| `fz-foerdercheck-kaltstart` | Anspruchsberechtigung, Projektart, Jahre, Risiken, Sofortpotenzial |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag, Vorhabenbeschreibung, technische Neuheit, Risiko |
| `fz-plaedoyer-begruendung-und-verteidigung` | Plädoyer, Begründung und Verteidigung gegenüber BSFZ, Finanzamt, Geschäftsführung, Insolvenzverwaltung oder Einspruchsstelle |
| `fz-fue-definition-frascati-abgrenzung` | Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung |
| `fz-bemessungsgrundlage-2026` | Personal, Eigenleistung, Auftragsforschung, Wirtschaftsgüter, 12-Mio.-Grenze |
| `fz-finanzamt-festsetzung-auszahlung` | Antrag beim Finanzamt, Anrechnung, Auszahlung, Vorauszahlungssenkung |
| `fz-insolvenz-verlust-liquiditaet` | Krise, Verlustjahr, Insolvenz, Forderungs-/Masseblick, Liquidität |
| `fz-dokumentationspaket-betriebspruefung` | Stundenzettel, Projektakte, Kostenbelege, Prüferpaket |
| `fz-kumulierung-beihilfen-agvo` | Doppelförderung, AGVO, andere Zuschüsse, EU/EWR-Auftragsforschung |
| `fz-ablehnung-nachbesserung-einspruch` | BSFZ-Nachforderung, Ablehnung, Finanzamt-Einspruch, Reparatur |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie, rückwirkende Jahre, Jahreswechsel, Portfolio |

## Typische Startpunkte

| Situation | Start |
| --- | --- |
| "Wir wissen nicht, ob unser Vorhaben FuE ist" | `forschungszulage-antragstellung-allgemein` → `fz-foerdercheck-kaltstart` |
| "Wir müssen den BSFZ-Antrag schreiben" | `fz-fue-definition-frascati-abgrenzung` → `fz-bsfz-bescheinigung-projektbeschreibung` |
| "Wir brauchen ein überzeugendes Plädoyer / eine Begründung" | `fz-plaedoyer-begruendung-und-verteidigung` |
| "Wir wollen wissen, wie viel Geld kommt" | `fz-bemessungsgrundlage-2026` → `fz-finanzamt-festsetzung-auszahlung` |
| "Wir sind im Verlust / in der Krise" | `fz-insolvenz-verlust-liquiditaet` |
| "BSFZ fragt nach oder lehnt ab" | `fz-ablehnung-nachbesserung-einspruch` |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 85 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abgrenzung-adaptiver-antrag` | Abgrenzung: Compliance-Dokumentation und Aktenvermerk. |
| `abgrenzung-compliance` | Abgrenzung: Compliance-Dokumentation und Aktenvermerk im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zust... |
| `ablehnung-nachbesserung-einspruch` | Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-Widerspruch, Finanzamt-Kürzung, Einspruch nach AO, neue Tatsachen, Beleg- und Textreparatur, Klage Finanzgericht als... |
| `adaptiver-dokumentenmatrix` | Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `adaptiver-dokumentenmatrix-und-lueckenliste` | Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `anschluss-routing` | Anschluss-Routing für Forschungszulage FZulG: wählt den nächsten Spezial-Skill nach Engpass (Antrag jederzeit, Projektbeschreibung, BSFZ-Bescheinigung, Stundennachweise), dokumentiert Router-Entscheidung mit Begründung. |
| `antrag-zahlen-schwellen-und-berechnung` | Antrag: Zahlen, Schwellenwerte und Berechnung. |
| `antrag-zahlen-schwellenwerte` | Antrag: Zahlen, Schwellenwerte und Berechnung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `antragstellung-auszahlung-beihilfen` | Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `auftragsforschung-vertragsgestaltung` | Auftragsforschung im Sinne § 3 Abs. 4 FZulG: Auftraggeber-Auftragnehmer-Konstellation, Pflichten des Auftraggebers (Risikotragung, Verwertung), förderfähige Quote 60 oder 70 Prozent der vereinbarten Vergueng. Prüfraster Vertragsgestaltu... |
| `auszahlung-internationaler-bezug` | Auszahlung: Internationaler Bezug und Schnittstellen im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `auszahlung-internationaler-bezug-und-schnittstellen` | Auszahlung: Internationaler Bezug und Schnittstellen. |
| `beihilfen-beweislast-darlegungslast` | Beihilfen: Beweislast, Darlegungslast und Substantiierung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `beihilfen-beweislast-und-darlegungslast` | Beihilfen: Beweislast, Darlegungslast und Substantiierung. |
| `bemessungsgrundlage-2026` | Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, K... |
| `bemessungsgrundlage-interessen` | Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fr... |
| `bemessungsgrundlage-interessen-bsfz` | Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix. |
| `bescheidung-rechtsmittel` | Bescheidung Forschungszulage: Bescheinigungsbescheid BSFZ und Festsetzungsbescheid Finanzamt sind zwei getrennte Verwaltungsakte. Rechtsmittelketten: BSFZ-Widerspruch dann Verpflichtungsklage; Finanzamt-Einspruch dann Klage Finanzgericht... |
| `bescheidung-rechtsmittel-bsfz` | Bescheidung Forschungszulage: Bescheinigungsbescheid BSFZ und Festsetzungsbescheid Finanzamt sind zwei getrennte Verwaltungsakte. Rechtsmittelketten: BSFZ-Widerspruch dann Verpflichtungsklage; Finanzamt-Einspruch dann Klage Finanzgericht... |
| `betriebspruefung-strategie` | Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn keine Steuerstraftat), Argumentationspakete, Schlussbesprechung. Prüfraster: Stundennachweise, Auftragsforschungsvertrae... |
| `bsfz-behoerden-gericht-und-registerweg` | Bsfz: Behörden-, Gerichts- oder Registerweg. |
| `bsfz-behoerden-gerichts` | Bsfz: Behörden-, Gerichts- oder Registerweg im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sc... |
| `bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag und FuE-Projektbeschreibung praxistauglich erstellen: Portaltexte mit Zeichenbudgets, Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete, Prüferlogik, Anti-Floskel-Regeln u... |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Forschungszulage-Antragstellung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Bel... |
| `definition-abschlussprodukt` | Definition: Abschlussprodukt und Übergabe im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schw... |
| `definition-abschlussprodukt-und-uebergabe` | Definition: Abschlussprodukt und Übergabe. |
| `dokumentationspaket-betriebspruefung` | Dokumentationspaket Forschungszulage prüfungsfest aufbauen: Projektakte mit BSFZ-Antrag und Bescheid, Stundenaufzeichnung je Mitarbeiter Tag Vorhaben, Personalkostenbeleg aus Lohnabrechnung, Auftragsforschungsbeleg mit Vertrag und Rechnu... |
| `dokumente-intake` | Dokumentenintake für Forschungszulage FZulG: sortiert Projektbeschreibung, BSFZ-Bescheinigung, Stundennachweise, prüft Datum, Absender, Frist und Beweiswert (F&E-Stundenaufzeichnungen, Projektdokumentation); markiert Lücken; berücksichti... |
| `einspruch-sonderfall-edge-case` | Einspruch: Sonderfall und Edge-Case-Prüfung im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sc... |
| `einspruch-sonderfall-und-edge-case` | Einspruch: Sonderfall und Edge-Case-Prüfung. |
| `einstieg-routing` | Einstieg, Triage und Routing für Forschungszulage FZulG: ordnet Rolle (Unternehmen F&E, BSFZ, Finanzamt), markiert Frist (Antrag jederzeit), wählt Norm (FZulG, EStG § 3 Nr. 26b) und Zuständigkeit (Bescheinigungsstelle Forschungszulage (B... |
| `finanzamt-festsetzung-auszahlung` | Forschungszulage beim Finanzamt beantragen, festsetzen und auszahlen lassen: ELSTER-Antrag, Vorlage der BSFZ-Bescheinigung, Forschungszulagenbescheid, Anrechnung auf Einkommen- oder Körperschaftsteuer, Auszahlung eines Überschusses, Vora... |
| `finanzamt-quellenkarte` | Finanzamt Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `foerdercheck-kaltstart` | Schneller Fördercheck Forschungszulage in zehn Minuten: Anspruchsberechtigung, FuE-Kategorie nach Frascati, KMU-Status, Personalkosten-Schwelle, Projektjahre, Kostenarten, BSFZ-/Finanzamt-Status, Kumulierung, Ausschlussrisiken und realis... |
| `foerdercheck-risikoampel` | Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche... |
| `foerdercheck-risikoampel-und-gegenargumente` | Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `forsch-bsfz-pruefung-spezial` | Spezialfall BSFZ-Prüfung und Nachfragen: typische Rueckfragen Bescheinigungsstelle, Stellungnahmefrist, Widerspruch. Prüfraster für Antragsteller und Steuerberater. |
| `forsch-konzernverbund-forschung-spezial` | Spezialfall Konzernverbundforschung und verbundene Unternehmen: § 3 Abs. 1 FZulG, Auftragsforschung, KMU-Status, Beihilfen-Kumulation. Prüfraster für Konzerntochter und Forschungs-GmbH. |
| `forsch-projektbeschreibung-bauleiter` | Bauleiter Projektbeschreibung FZulG: FuE-Definition Frascati, Neuheit, technologisches Risiko, systematische Vorgehensweise. Prüfraster für schluessige Darstellung gegenueber BSFZ. |
| `forsch-stundenaufzeichnung-fz-ablehnung` | Leitfaden Stundenaufzeichnung FZulG: zuwendungsfaehige Personalkosten, eigene Beschäftigte, Auftragsforschung, Dokumentationspflichten. Prüfraster für Personalcontrolling im Forschungszulage. |
| `forsch-stundenaufzeichnung-leitfaden` | Leitfaden Stundenaufzeichnung FZulG: zuwendungsfaehige Personalkosten, eigene Beschäftigte, Auftragsforschung, Dokumentationspflichten. Prüfraster für Personalcontrolling. |
| `forschungszulage-insolvenzlage-red-team-korrektur` | Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel. |
| `forschungszulage-mandantenentscheidung-antragspfad` | Dokumentation: Mandantenkommunikation und Entscheidungsvorlage im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fr... |
| `forschungszulage-projektbeschreibung-bescheinigung` | Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Fris... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Forschungszulage-Antragstellung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege... |
| `fue-abgrenzung-definition` | FuE-Definition Grenzfaelle nach Frascati-Manual und FZulG: Neuheit und Unsicherheit, Routinearbeiten gegen Versuch und Irrtum. Beispielszenarien Software-Entwicklung, klinische Studien, Produktoptimierung, Reverse Engineering. Prüfraste... |
| `fue-abgrenzung-grenzfaelle` | FuE-Definition Grenzfaelle nach Frascati-Manual und FZulG: Neuheit und Unsicherheit, Routinearbeiten gegen Versuch und Irrtum. Beispielszenarien Software-Entwicklung, klinische Studien, Produktoptimierung, Reverse Engineering. Prüfraste... |
| `fue-definition-frascati-abgrenzung` | FuE-Definition für die Forschungszulage praxisnah prüfen: Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung, Frascati-Kriterien (Neuheit, Schöpferisch, Ungewissheit, Systematik, Reproduzierbarkeit), AGVO-Definitione... |
| `fzulg-fristen-form` | FZulG: Fristen, Form, Zuständigkeit und Rechtsweg im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellu... |
| `fzulg-fristen-form-und-zustaendigkeit` | FZulG: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `historie-und-rechtsgrundlagen` | Historie und Rechtsgrundlagen der steuerlichen Forschungszulage einfuehrend: FZulG seit 2020, Wachstumschancengesetz 2024 mit Erhoehung auf 10 Mio. Euro Bemessungsgrundlage, KMU-Bonus 5 Mio. Euro. Verhältnis zu Projektfoerderung (Bund,... |
| `insolvenz-forsch-konzernverbund` | Forschungszulage in Verlust-, Krisen- und Insolvenzlagen als Liquiditätshebel nutzen: Auszahlung statt bloßer Steuerersparnis, Vorauszahlungssenkung, Massezugehörigkeit, Antragsbefugnis Geschäftsleitung oder Insolvenzverwaltung, Aufrechn... |
| `insolvenz-verlust-liquiditaet` | Forschungszulage in Verlust-, Krisen- und Insolvenzlagen als Liquiditätshebel nutzen: Auszahlung statt bloßer Steuerersparnis, Vorauszahlungssenkung, Massezugehörigkeit, Antragsbefugnis Geschäftsleitung oder Insolvenzverwaltung, Aufrechn... |
| `insolvenzlage-fehlerkatalog` | Insolvenzlage Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `insolvenzlage-red-team-und-qualitaetskontrolle` | Insolvenzlage: Red-Team und Qualitätskontrolle. |
| `kaltstart-triage` | Adaptiver Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Führt Einsteiger, Technikteams, CFOs und Steuerberater unterschiedlich, klärt Unternehmen, FuE-Vorhaben, Wirtschaftsjahre, BSFZ-Status, Finanzamt-Antrag, Liquidit... |
| `konzern-und-organschaft-spezial` | Spezialfall Konzern und Organschaft: Zurechnung von FuE-Aktivitaeten zwischen Mutter und Tochter, Auftragsforschung im Konzernverbund, Verrechnungspreise mit Fremdvergleich, KMU-Status bei Konzernzugehoerigkeit nach KMU-Empfehlung 2003 3... |
| `koordinierung-zwei` | Koordinierung Forschungszulage mit anderen Foerderwegen: keine Doppelfoerderung derselben Kosten, aber Kombination über Modulgrenze hinweg (ZIM, IGF, Horizon Europe, Landesfoerderung). Prüfraster für Kostentrennung, Buchhaltung, Besche... |
| `koordinierung-zwei-foerderwege` | Koordinierung Forschungszulage mit anderen Foerderwegen: keine Doppelfoerderung derselben Kosten, aber Kombination über Modulgrenze hinweg (ZIM, IGF, Horizon Europe, Landesfoerderung). Prüfraster für Kostentrennung, Buchhaltung, Besche... |
| `kumulierung-beihilfen-agvo` | Kumulierung Forschungszulage mit anderen Förderungen und Beihilfen sauber prüfen: AGVO Art. 25, EU/EWR-Auftragsforschung, ZIM, BMBF-Programme, Landesprogramme, De-minimis-Nähe, Horizon, Doppelförderung, Nachweis- und Abzugslogik. Mit Kum... |
| `mandantenentscheidung-einspruch-sonderfall` | Dokumentation: Mandantenkommunikation und Entscheidungsvorlage. |
| `mandantenkommunikation` | Mandantenkommunikation im Forschungszulage-Antragstellung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege l... |
| `mehrjahresroadmap-fristennotiz-fz` | Mehrjahresroadmap: Fristennotiz und nächster Schritt. |
| `mehrjahresroadmap-fristennotiz-naechster` | Mehrjahresroadmap: Fristennotiz und nächster Schritt im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `output-waehlen` | Output-Wahl für Forschungszulage FZulG: stimmt Adressat (Unternehmen F&E, BSFZ, Finanzamt), Frist (Antrag jederzeit) und Form auf den Zweck ab — typische Outputs: BSFZ-Antrag, Festsetzungsantrag FA, Einspruch. |
| `personalkosten-und-stundennachweis` | Foerderfaehige Personalkosten der Forschungszulage: Bruttoarbeitslohn plus Arbeitgeberanteile, Stundenpauschale 70 Euro Eigenunternehmer, Auftragsforschung 60 Prozent (KMU 70 Prozent). Stundennachweissystem: tagesgenau, Aufgabenbezug, Pl... |
| `plaedoyer-begruendung-roadmap` | Plädoyer, Begründung und Verteidigung der Forschungszulage: macht aus Technik, Belegen, Kosten und Behördenkritik einen überzeugenden Vortrag für BSFZ, Finanzamt, Einspruch, Mandantenmemo oder Geschäftsführungsentscheidung. Mit Argumenta... |
| `plaedoyer-begruendung-und-verteidigung` | Plädoyer, Begründung und Verteidigung der Forschungszulage: macht aus Technik, Belegen, Kosten und Behördenkritik einen überzeugenden Vortrag für BSFZ, Finanzamt, Einspruch, Mandantenmemo oder Geschäftsführungsentscheidung. Mit Argumenta... |
| `portaltexte-schriftsatz-brief` | Portaltexte: Schriftsatz-, Brief-, Memo- und Plädoyer-Bausteine im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche F... |
| `portaltexte-schriftsatz-brief-und-memo-bausteine` | Portaltexte: Schriftsatz-, Brief- und Memo-Bausteine. |
| `quellen-livecheck` | Quellen-Live-Check für Forschungszulage FZulG: prüft Normen (FZulG, EStG § 3 Nr. 26b) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Bescheinigungsstelle Forschungszulage (BSFZ) und Quellenhygiene nach references... |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand |
| `roadmap-mehrjahresantrag` | Mehrjahresstrategie Forschungszulage: BSFZ-Bescheinigung für mehrjährige Vorhaben, jährliche Aktualisierung der Stundenaufzeichnung und Projektakte, Folgeanträge knapp halten, Roadmap-Pflege, Liquiditätsplanung über Wirtschaftsjahre, rüc... |
| `start-chronologie-fristen` | Adaptiver Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Führt Einsteiger, Technikteams, CFOs und Steuerberater unterschiedlich, klärt Unternehmen, FuE-Vorhaben, Wirtschaftsjahre, BSFZ-Status, Finanzamt-Antrag, Liquidit... |
| `start-up-und-personengesellschaft` | Start-up- und Personengesellschafts-Konstellation Forschungszulage: GmbH und Co KG, atypisch stille Beteiligung, Mitunternehmerschaft, Verluste in Anfangsjahren mit Zulage als Liquiditaetshebel. Beispielrechnungen, typische Prüfpunkte.... |
| `tatbestand-beweis-belege-antragstellung` | Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche F... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Forschungszulage FZulG: trennt fehlende Tatsachen von fehlenden Belegen (Projektbeschreibung, BSFZ-Bescheinigung, Stundennachweise), nennt pro Lücke Beweisthema, Beschaffungsweg (Bescheinigungsstelle For... |
| `verlust-formular-portal` | Verlust: Formular, Portal und Einreichungslogik im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung... |
| `verlust-zeichenbudgets` | Verlust: Formular, Portal und Einreichungslogik. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Forschungszulage. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Forschungszulage. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Forschungszulage. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Forschungszulage. |
| `zeichenbudgets-verhandlung` | Zeichenbudgets: Verhandlung, Vergleich und Eskalation im Forschungszulage-Antragstellung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zust... |
| `zeichenbudgets-verhandlung-vergleich-und-eskalation` | Zeichenbudgets: Verhandlung, Vergleich und Eskalation. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
