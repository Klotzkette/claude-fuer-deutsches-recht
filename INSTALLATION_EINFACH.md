# Installation in einfach — wenn der Marketplace-Weg nicht klappt

> Diese Seite richtet sich an alle, die in Claude Desktop / Cowork **keinen GitHub-Pfad eingeben können** und einfach nur die Plugins ausprobieren wollen. Es ist kein bisschen blöd, dort etwas zu suchen — der GitHub-Pfad gehört in ein anderes Dialogfeld, das je nach Version unterschiedlich heißt oder gar nicht angeboten wird.
>
> Der schnellste Weg ist: **ZIP herunterladen → hochladen → fertig.** Genau dort, wo auch das Plugin „Legal Plugin" landet.

## Kurzfassung

> 📆 **Hinweis Release vs. Entwicklungsstand:** Die ZIPs in der Releases-Seite entsprechen einem **getaggten, validierten Stand** (zur Zeit `v7.0.0`). Der `main`-Branch des Repos kann **neuer** sein — mit weiteren Fixes, kleinen Ergänzungen oder neuen Tests. Für stabile Tagung → ZIPs aus dem Release; für neueste Korrekturen → Marketplace-Sync über den GitHub-Pfad (siehe README.md, Weg 1).

1. Auf [die Releases-Seite](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) gehen.
2. Pro gewünschtem Rechtsgebiet **eine ZIP-Datei** herunterladen, z. B. `liquiditaetsplanung.zip`.
3. In Claude Desktop / Cowork auf **Customize → Skills** klicken und zum Abschnitt **Persönliche Plugins / Personal plugins** scrollen — genau die Stelle, an der auch „Legal Plugin" installiert wird.
4. Auf das **+** neben „Persönliche Plugins" klicken und im Dialog das soeben heruntergeladene ZIP auswählen (alternativ: erst auf **Create**, dann **Upload plugin**).
5. Schritte 2–4 für jedes weitere Rechtsgebiet wiederholen, das gebraucht wird.

Das war's. In der Plugin-Liste erscheint das Plugin direkt, kann aktiviert werden, und der Skill ist beim nächsten Chat verfügbar.

> ⚠️ **Was NICHT hochzuladen ist:**
>
> - `marketplace.json` — das ist das Manifest des Gesamtkatalogs, kein Plugin. Wer es trotzdem als Plugin hochlädt, bekommt eine Fehlermeldung.
> - `testakte-*.zip` — das sind **Beispielakten zum Testen**, keine Plugins. Sie gehören in den Chat (als Mandatsunterlagen), nicht in den Plugin-Upload.
>
> Es ist nichts Schlimmes, wenn das versehentlich passiert. Die ZIP wird einfach abgelehnt; nichts geht kaputt.

## Welches ZIP brauche ich?

Auf der [Releases-Seite](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) liegen **80 Plugin-ZIPs** — eines pro Rechtsgebiet bzw. Werkzeug. Es muss nicht alles installiert werden; nur das, was gerade gebraucht wird.

### Kanzlei-Backoffice und Querschnitt

| ZIP                                       | Was steckt drin                                                                                                            |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `kanzlei-allgemein.zip`                      | Fristenbuch, Timesheet, Rechnung, Mandantenakte, Korrespondenz                                                             |
| `kanzlei-allgemein.zip`                 | Kanzlei-Allgemein-Plugin: edles Kommandocenter, GwG, Klage/Replik, Vertrag, Rechtsprechung, beA, Rechnung, UStVA             |
| `grosskanzlei-corporate-ma.zip`           | Freistehend: Big-Law-Corporate/M&A mit Aktenanlage, Datenraum, DD, internem Tabellenreview, Liquiditätsvorschau, Insolvenzreife, CP-Kalender, E-Rechnung/GoBD, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG, PMI |
| `kanzlei-builder-hub.zip`                 | Werkzeuge zum Bauen eigener kanzleiinterner Skills, Security-Review                                                        |
| `verwaltete-agentenrezepte.zip`           | Kuratierte Workflow-Rezepte zum Wiederverwenden                                                                            |
| `aktenaufbereiter-strafrecht.zip`         | Strukturierung großer Strafakten in den Griff bekommen                                                                     |
| `anlagen-zu-schriftsaetzen.zip`           | Anlagen-Sortierung für gerichtliche Schriftsätze                                                                           |
| `memorandums-ersteller.zip`               | Mandantenunterlagen → juristisches Memorandum (4-Teile-Gliederung)                                                         |
| `tabellenreview-3d.zip`                   | 3D-Tabellenreview-Würfel: Spaltenprompts × Zeilenprompts × Tabellenformeln                                                 |
| `verlagsredaktion.zip`                    | Redaktioneller Assistent für juristische Publikationen                                                                     |
| `nda-abgleich.zip`                        | NDA-Review aus Empfängersicht, Markup mit Begründungen                                                                     |
| `methodenlehre-buergerliches-recht.zip`       | Gutachten- vor Urteilsstil, juristische Methodenlehre                                                                      |
| `zitierweise-deutsches-recht.zip`         | Deutsche Hauszitierweise (Datum + Aktenzeichen, BGHZ-Pinpoint mit Randnummer)                                              |
| `common-law-kompass.zip`                  | Common Law, English Law und US Law für deutsche Wirtschaftsjuristen: False Friends, Vertragsbegriffe, Consideration, UCC, Discovery und bilinguale Reviews |
| `europarecht-kompass.zip`                 | Europarecht ohne deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Beihilfen und Vorlageverfahren |
| `einfache-leichte-sprache-jura.zip`       | Juristische Texte wahlweise in Einfache Sprache oder Leichte Sprache übertragen, mit Rechtsinhalt-Sicherung und Qualitätsgate |

### Wirtschaft, Insolvenz, Sanierung

| ZIP                                       | Was steckt drin                                                                                                            |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `liquiditaetsplanung.zip`                 | 3-Wochen-Vorschau, 13/26/52-Wochen-Planung, BGH-Schema Passiva II                                                          |
| `insolvenzrecht.zip`                      | §§ 17, 19 InsO, Antragspflicht § 15a InsO, BGH-Volltexte als PDF                                                           |
| `insolvenzverwaltung.zip`                | Insolvenzverwaltung aus IV-/Sachwalter-Sicht: Eröffnungsgutachten, Masse, Tabelle, Anfechtung, § 15b, Insolvenzplan-/StaRUG-Planwerkstatt, § 208, Berichte, Schlussrechnung |
| `insolvenzforderungsanmeldungspruefung.zip` | Freistehende Forderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund/Betrag/Rang, Bestreiten, Feststellung, Tabelle, Prüfungstermin und § 189-Nachlauf |
| `insolvenzplan-starug-planwerkstatt.zip` | Freistehende Insolvenzplan- und StaRUG-Planwerkstatt: Sanierungskonzept, integrierte Planung, Vergleichsrechnung, Gruppen/Klassen, Planentwurf, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Vollzug |
| `fortbestehensprognose.zip`               | Fortbestehensprognose § 19 II InsO als Geschäftsführer-Selbstdokumentation                                                 |
| `steuerrecht-anwalt-und-berater.zip`             | BWA-/SuSa-/Bilanzprüfung, Krisenfrüherkennung                                                                              |
| `gesellschaftsrecht.zip`                  | M&A-DD, GmbH/AG-Beschlüsse, HRB-Anmeldung                                                                                  |

### Streitige Mandate

| ZIP                                       | Was steckt drin                                                                                                            |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `prozessrecht.zip`                        | Mahnbescheid, einstweilige Verfügung, Schutzschrift, Zwangsvollstreckung                                                   |
| `zwangsverwaltung-zvg.zip`              | ZVG: Zwangsverwaltung, Versteigerung, ZVG-Portal-Recherche, Bieterangebote, Sicherheitsleistung, geringstes Gebot und Terminvorbereitung |
| `strafbefehl-verteidiger.zip`            | Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Wiedereinsetzung, Einstellung und Hauptverhandlung         |
| `verkehrsowi-verteidiger.zip`             | Verkehrsordnungswidrigkeiten: Bußgeld, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Messakte, Einspruch und Amtsgericht |
| `forderungsmanagement-klagewerkstatt.zip` | Standardklage aus eigenen Mustern, Zuständigkeitsprüfung, Inkasso-Zahlungsklage mit Mahnvorlauf und Anspruchs-Gatekeeper |
| `phishing-vorfall-pruefer.zip` | Online-Banking-Phishing, pushTAN, Call-ID-Spoofing, § 675u/§ 675v BGB, Banklogs, Ombudsmann und Klage |
| `vertragsausfueller.zip` | DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, Clean-Verträge erzeugen und Track Changes nur nach ausdrücklicher Nachfrage |
| `vertragsrecht.zip`                       | NDA, AGB, SaaS, Lieferantenverträge                                                                                        |
| `fluggastrechte.zip`                      | VO 261/2004, EuGH-Rspr., Ticketprüfung, Pauschalklage                                                                      |
| `arbeitsrecht.zip`                        | Kündigung (KSchG, 3-Wochen-Frist), Aufhebungsvertrag inkl. Sperrzeit, Abmahnung, BR-Anhörung                               |
| `mietrecht.zip`                           | Mieterhöhung, Mietspiegel-Quellen, Eigenbedarf, Schönheitsreparaturen                                                      |
| `sozialrecht-kanzlei.zip`                 | Bescheidanalyse, Widerspruch, Klage SGB II/III/V/VI/IX/XII                                                                 |
| `steuerrecht-anwalt-und-berater.zip`                 | Bescheidanalyse, Einspruch, Klage FG/BFH                                                                                   |
| `verfassungsrecht.zip`                    | Verfassungsbeschwerde, GG-Auslegung, BVerfG-Verfahren                                                                      |
| `betreuungsrecht.zip`                     | Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Kontoanalyse und verdächtige Verträge (BtOG, §§ 1814 ff. BGB)                                          |

### Regulierung und Compliance

| ZIP                                       | Was steckt drin                                                                                                            |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `aussenwirtschaft-zoll-sanktionen.zip` | Exportkontrolle, Sanktionen, Embargos, Zoll, TARIC, CBAM, Verbrauchsteuer, Antidumping, AWV, AML/KYC, Prüfungen und Krisenkommunikation |
| `datenschutzrecht.zip`                    | DSGVO/BDSG/TDDDG, PIA/DPIA, AVV-Review, Datenpannenmeldung                                                                 |
| `geldwaeschepraevention-aml-kyc.zip` | Geldwäscheprävention, AML/KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister, Monitoring, Audit und Behördenverfahren |
| `ki-governance.zip`                       | EU-KI-VO + DSGVO: Use-Case-Triage, KI-Inventar, Vendor-Review                                                              |
| `berufsrecht-ki-vertragspruefung.zip`     | Berufsrechtliche Vorprüfung von Verträgen mit Legal-Tech-Anbietern                                                         |
| `regulatorisches-recht.zip`               | KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG                                                                                 |
| `energierecht.zip`                       | Stadtwerke, Energieversorger, Wärme, Netze, Vertrieb, Industriekunden, EEG/KWKG, E-Mobility, Wasserstoff, Transaktionen |
| `umweltrecht.zip`                        | Emissionshandel, BImSchG, Abfall, Wasser, Boden, Naturschutz, UIG/IFG, Bußgeld, Umwelt-DD                              |
| `verkehr-infrastrukturrecht.zip`         | Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum, Wirtschaftsverkehr, Verkehrswende            |
| `produktrecht.zip`                        | Launch-Review, Impressum (§§ 5, 6 DDG), PAngV, Marketing-Claims                                                            |
| `gewerblicher-rechtsschutz.zip`           | DPMA/EUIPO-Markenrecherche, Anmeldung, FTO, UWG-Abmahnung                                                                  |
| `patentrecherche.zip`                     | Espacenet, Google Patents, DPMAregister                                                                                    |
| `immobilienrechtspraxis.zip`              | Vertragserstellung, Bauträger, WEG, Maklerrecht                                                                            |
| `rechtsberatungsstelle.zip`               | Pro-Bono / studentische Beratung (RDG-konform), Intake, Fristen                                                            |
| `jveg-kostenpruefer.zip` | JVEG-Kostenprüfung: Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Fristen, Festsetzung und Beschwerde |
| `jurastudium.zip`                         | Karteikarten, Gutachten-Coaching, Examensvorbereitung                                                                      |

### Fachanwalt-Plugin fuer Fachanwaltschaft (22 Stück)

Kein Vollassistent, sondern Orientierung in Normen, Notfristen, typischen Mandanten und Schriftsatzbausteinen.

`fachanwalt-agrarrecht.zip`, `fachanwalt-bank-kapitalmarktrecht.zip`, `fachanwalt-bau-architektenrecht.zip`, `fachanwalt-erbrecht.zip`, `fachanwalt-familienrecht.zip`, `fachanwalt-internationales-wirtschaftsrecht.zip`, `fachanwalt-it-recht.zip`, `fachanwalt-medizinrecht.zip`, `fachanwalt-migrationsrecht.zip`, `fachanwalt-sportrecht.zip`, `fachanwalt-strafrecht.zip`, `fachanwalt-transport-speditionsrecht.zip`, `fachanwalt-urheber-medienrecht.zip`, `fachanwalt-vergaberecht.zip`, `fachanwalt-verkehrsrecht.zip`, `fachanwalt-versicherungsrecht.zip`, `fachanwalt-verwaltungsrecht.zip`

Wer **nur die Liquiditätsplanung** ausprobieren will, lädt sich nur `liquiditaetsplanung.zip` herunter. Wer sich umsehen möchte, lädt drei oder vier ZIPs.

## Bonus: die Beispielakten

Wer einen konkreten Fall durchspielen will, lädt sich zusätzlich eine **Testakte** herunter. Diese werden im Release-Build mit dem Prefix `testakte-` ausgezeichnet, damit sie im Plugin-Upload nicht versehentlich landen.

| Testakte                                                   | Passt zu Plugin                                              |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| `testakte-beispielakte-edelholz-berlin.zip`                | `liquiditaetsplanung` + `insolvenzrecht` + `steuerrecht-anwalt-und-berater` |
| `testakte-fluggastrechte-familie-braeutigam.zip`           | `fluggastrechte`                                             |
| `testakte-betreuung-hildegard-sauer.zip`                   | `betreuungsrecht`                                            |
| `testakte-betreuung-schmalfeld-kontodaten-vertraege.zip`   | `betreuungsrecht`                                            |
| `testakte-einfache-leichte-sprache-jura-mandantenbrief.zip` | `einfache-leichte-sprache-jura`                              |
| `testakte-sozialrecht-rollstuhl-tannenberg.zip`            | `sozialrecht-kanzlei`                                        |
| `testakte-fortbestehensprognose-paragrafix-gmbh.zip`       | `fortbestehensprognose`                                      |
| `testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip` | `insolvenzforderungsanmeldungspruefung` |
| `testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip` | `insolvenzplan-starug-planwerkstatt` |
| `testakte-jveg-zeugin-berger-lg-tuebingen.zip` | `jveg-kostenpruefer` |
| `testakte-inkasso-zahlungsklage-modefuchs.zip` | `forderungsmanagement-klagewerkstatt` |
| `testakte-phishing-vorfall-mayer-sparkasse-berlin.zip` | `phishing-vorfall-pruefer` |
| `testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip` | `vertragsausfueller` |
| `testakte-geldwaesche-aml-kyc-musterholding.zip` | `geldwaeschepraevention-aml-kyc` |
| `testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip` | `aussenwirtschaft-zoll-sanktionen` |
| `testakte-common-law-kompass-crossborder-contract.zip` | `common-law-kompass` |
| `testakte-europarecht-kompass-beihilfe-richtlinie.zip` | `europarecht-kompass` |
| `testakte-strafbefehl-ladendiebstahl-fahrerflucht-musterakte.zip` | `strafbefehl-verteidiger` |
| `testakte-verkehrsowi-rotlicht-tempo-musterakte.zip` | `verkehrsowi-verteidiger` |
| `testakte-energierecht-stadtwerke-quartier.zip`          | `energierecht`                                              |
| `testakte-umweltrecht-industrieanlage-genehmigung.zip`   | `umweltrecht`                                               |
| `testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip` | `verkehr-infrastrukturrecht`                         |
| `testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip` | `zwangsverwaltung-zvg`                              |

Eine Testakte wird **nicht über den Plugin-Upload** geladen, sondern direkt im Chat als Mandatsunterlage abgelegt (per Drag-and-drop oder als Anhang).

## Hilfe, kein „+" da

Je nach Claude-Desktop- / Cowork-Version sieht der Plugin-Dialog leicht anders aus. Die typischen Stellen, an denen der Upload-Knopf sitzt:

- **Customize → Skills → Persönliche Plugins → +** (häufigste Variante)
- **Customize → Skills → Personal plugins → + → Upload from .zip**
- **Customize → Plugins → Add → Install from file** (ältere Versionen)

Wichtig ist nur: gesucht wird der Punkt, an dem **eine einzelne ZIP-Datei** vom Rechner ausgewählt werden kann. Wenn dort stattdessen nach einem GitHub-Pfad gefragt wird, ist das das **andere** Dialogfeld — auf **Cancel** und einen Schritt zurück.

## Wenn nichts davon klappt

In aktuelleren Claude-Code- / Cowork-Versionen geht auch direkt der Marketplace-Befehl (im Terminal):

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install liquiditaetsplanung
```

Falls das ebenfalls kein Dialogfeld findet, ist die Cowork-Version zu alt für Marketplaces — dann ist der ZIP-Upload oben der einzige Weg, und das ist völlig in Ordnung. Er funktioniert in jeder Version, die Plugin-Upload überhaupt kennt.

## Sanity-Check

Nach der Installation in eine neue Konversation gehen und schreiben:

> „Bitte mache eine 3-Wochen-Liquiditätsvorschau für eine kleine GmbH."

Wenn Claude jetzt nach Sachverhalt, Bankstand, offenen Forderungen und Daueraufträgen fragt und am Ende eine Excel-Tabelle vorschlägt, ist die Installation gelungen.

## Probleme?

[Issue auf GitHub aufmachen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/new) — Screenshot vom Dialog mit dabei hilft enorm. Es ist kein bisschen nervig; jede Rückmeldung macht die Anleitung besser.
