# Pluginstruktur: Fachprofile, Überschneidungen und Auswahl

Diese Bestandsprüfung hilft bei der Auswahl und Pflege der Plugins. Sie unterscheidet fachliche Einstiege, eigenständige Arbeitsrollen und tatsächliche Doppelungen. Alle Fachanwaltsprofile und die ausdrücklich getrennt gewünschten Insolvenzwerkzeuge bleiben erhalten.

[Fachanwaltsprofile](../../_FACHANWALTSCHAFTS-PLUGINS/README.md) · [Steuerrecht-Einstieg](../../fachanwalt-steuerrecht/README.md) · [Plugin-Gruppen](../../plugin-gruppen/README.md) · [Vollständiges Inventar](./bestand.json)

## 1. Prüfungsumfang und Ergebnis

Stand: 15. November 2026. Grundlage ist Repository-Commit `4fddf053657c5fad76d8768822b85781cf878b10`.

Die strukturelle Prüfung erfasst sämtliche im Marketplace registrierten Plugins: Verzeichnis, Manifest, Version, README, aktive Skills, Skill-Verzeichnis und eigenständige Prompt-Dateien. Für die unten genannten Familien wurden zusätzlich die Arbeitsaufträge, Rollen und ausgewählte Fachmodule verglichen. Das ist keine vollständige juristische Aktualitätsprüfung aller Inhalte und keine Ausführung sämtlicher Skills in einer KI-Oberfläche.

| Merkmal | Ergebnis |
| --- | --- |
| Installierbare Plugins | 315 |
| Aktive Skills insgesamt | 3.175 |
| Größtes einzelnes Plugin | 20 aktive Skills |
| Plugins mit mehr als 20 aktiven Skills | 0 |
| Fehlende zentrale Skill-Verzeichnisse | 0 |
| Abweichende Namen oder Versionen zwischen Marketplace und Manifest | 0 |
| Nicht registrierte aktive Plugin-Manifeste außerhalb der Prüf- und Archivbestände | 0 |
| Fachanwaltsprofile | 24; davon 23 eigene Fachanwalts-Plugins und ein Zugang zum gemeinsamen Steuerrechts-Plugin |
| Skills in diesen 24 Profilen | 284; jedes Profil hat Werkstatt- und Mini-Prompt |

Gezählt werden auswählbare `SKILL.md`-Dateien. Fachvertiefungen, Vorlagen, Referenzen und Archivdateien sind keine zusätzlichen auswählbaren Skills. Das Inventar enthält für jedes Plugin die Pfade und den SHA-256-Wert seiner README sowie den SHA-256-Wert des Marketplace-Manifests. Damit ist der untersuchte Bestand nachvollziehbar.

Bei den eigenständigen Prompt-Dateien bestehen drei Ausnahmen: `grundstuecksrecherche` und `schriftsatzwerkstatt-bea` haben keine gleichnamige Werkstatt-/Schnellstart-Datei; `bea-versand` hat einen Werkstatt-, aber keinen gleichnamigen Schnellstart-Prompt. Das Inventar kennzeichnet diese Werte mit `null`. Daraus folgt nicht, dass ihre installierbaren Skills fehlen.

Zwei aktive Skill-Texte sind jeweils wortgleich in Amts- und Landgerichtsprofilen: die Rechtsprechungsanker für Strafverfahren und für Zivilverfahren. Einzelne gemeinsam verwendete Texte rechtfertigen keine Zusammenlegung unterschiedlicher Gerichtsrollen.

## 2. Fachanwaltschaft und Steuerberatung

Der Ordner [fachanwalt-steuerrecht](../../fachanwalt-steuerrecht/README.md) ist der dauerhafte Fachanwalts-Einstieg. Er verweist auf das installierbare Plugin [Steuerrecht – Steuerberater und Anwälte](../../steuerrecht-anwalt-und-berater/README.md), dessen 20 Skills, eigenständige Prompts und Testakten. Der Wegweiser erzeugt weder ein zweites Installationspaket noch einen zweiten Fachbestand.

Das [Fachverzeichnis](../../_FACHANWALTSCHAFTS-PLUGINS/README.md) ordnet die 24 Profile nach Rechtsgebiet. Die übrigen Fachanwalts-Plugins behalten ihre eigenständigen Aufgaben und ihren fachlichen Einstieg. Gemeinsame Rechtsgebiete mit Spezialwerkzeugen sind allein kein Zusammenlegungsgrund.

## 3. Konkrete Kandidaten für eine Zusammenlegung

Die folgenden Zeilen sind **begründete Empfehlungen, keine bereits ausgeführten Zusammenlegungen**. Zielzahlen sind eine Planung auf Grundlage der vorhandenen Arbeitswege; ihre Tragfähigkeit ist erst nach vollständiger Zuordnung aller Inhalte belegt. Die Reihenfolge bevorzugt klare Doppelungen mit überschaubarer Migrationslast.

| Priorität | Bestehende Plugins und aktive Skills | Gemeinsame Aufgabe | Erhaltenswerte Unterschiede und Ziel |
| --- | --- | --- | --- |
| 1 | [Bauträgervertrag-Prüfer](../../bautraegervertrag-pruefer/README.md) (9) + [Bauträgervertragsprüfer](../../bautraegervertragspruefer/README.md) (6) | Bausoll, MaBV-Raten, Sicherheiten, Abnahme, Mängel, Notar und Eigentum; die READMEs beschreiben ausdrücklich dasselbe Mandat. | Ein Prüfer mit Rollenwahl und etwa 9–11 Skills. Erwerber, Bauträger, GdWE und Verwalter sowie Baugruppen-, KfW-, Verzugs-, WEG- und Verjährungsthemen erhalten. |
| 1 | [Arbeitszeugnis-Analyse](../../arbeitszeugnis-analyse/README.md) (8) + [Arbeitszeugnisprüfer](../../arbeitszeugnispruefer/README.md) (6) | Arbeitnehmerseitige Prüfung, Formulierungen, Leistungs-/Verhaltensbewertung, Berichtigung und Anspruchsdurchsetzung. | Etwa 6–8 Skills. Besondere Ausbildungs- und Führungskräftefälle, Tätigkeitsbewertung, Briefkopf und Beendigungsgrund zuordnen. Den arbeitgeberseitigen Zeugnisgenerator vorerst separat halten. |
| 1 | [Sozialversicherungspflicht-Prüfer](../../sozialversicherungspflicht-pruefer/README.md) (10) + [Sozialversicherungsstatus-Prüfer](../../sozialversicherungsstatus-pruefer/README.md) (10) | Beschäftigung oder Selbstständigkeit, Geschäftsführung, Lehrtätigkeit und DRV-Verfahren. | Etwa 11–14 Skills. Statusfeststellung, Versicherungspflicht je Zweig und Beitragsentscheidung unterscheiden; A1/Ausland, Plattformen, Dreiecksverhältnisse und Versorgungswerk erhalten. |
| 1 | [Projekteinkauf Baubranche](../../projekteinkauf-baubranche/README.md) (9) + [Bauunternehmer Einkauf](../../bauunternehmer-einkauf/README.md) (10) | Private Beschaffung, Angebotsvergleich, Lieferanten, Verhandlung und Nachträge. | Etwa 14 Skills. GAEB, Beschaffungsstrategie, Lieferung/Abnahme mit Preisrecherche, LV-Erstellung, Dokumentenauswertung und Anfängerzugang verbinden. Alle drei großen Einkaufsakten erhalten. |
| 2 | [Geldwäschebeauftragter](../../geldwaeschebeauftragter/README.md) (11) + [Geldwäscheprävention AML/KYC](../../geldwaeschepraevention-aml-kyc/README.md) (20) | Risikoanalyse, KYC/UBO, Verdachtsfälle, FIU, Kontrollen und Aufsicht. | Etwa 16–20 Skills mit rollenbezogenen Zugängen. Unabhängige Berichtswege, Informationssperren, Berufsgeheimnis, Konzern-, Krypto-, Immobilien- und EU-Übergangsmodule erhalten. |
| 2 | [Einfache/Leichte Sprache](../../einfache-leichte-sprache-jura/README.md) (8) + [Jura in einfacher Sprache](../../jura-in-einfacher-sprache/README.md) (5) | Verständliche Übertragung und Erklärung juristischer Texte. | Etwa 8–10 Skills mit getrennten Sprachmodi. Keine ungeprüfte Zertifizierung als Leichte Sprache; keine Rekonstruktion fehlender Originalaussagen. Deutsch als Zweitsprache bleibt ein eigenes Lernangebot. |
| 2 | [Staats-/Amtsanwaltschaft](../../gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft/README.md) (10) + [Staatsanwaltschaft Praxiseinstieg](../../gerichtsplugins/staatsanwaltschaft-praxis-einstieg/README.md) (10) | Dieselben zehn Themenwege in derselben staatlichen Verfahrensrolle. | Etwa 11–12 Skills mit zusätzlichem Erklärmodus. OWiG-/Bußgeldspur, Polizei-/Geschäftsstellenübergabe und Geheimnisschutz erhalten. Keine Verbindung mit Verteidigungs- oder Richterrollen. |
| 3 | [Corporate-Kanzlei](../../corporate-kanzlei/README.md) (11) + [Mittelstand Corporate/M&A](../../mittelstand-corporate-ma/README.md) (11) + [Großkanzlei Corporate/M&A](../../grosskanzlei-corporate-ma/README.md) (12) | Zehn gemeinsame auswählbare Routen und dieselbe Transaktionskette. | Etwa 12–14 Skills mit Profilen für Mittelstand, großes Transaktionsteam und laufende Corporate-Beratung. Zuerst Corporate/Mittelstand zuordnen; Großkanzlei erst nach gesondertem Abgleich. |
| 3 | [Vertragserstellung](../../vertragserstellung/README.md) (10) + [Corporate Contract Law](../../corporate-contract-law/README.md) (20) | Vollständiger B2B-Vertrag vom Auftrag bis zur Unterschriftenfassung. | Höchstens 20 Skills. Den kompakten Einzelgeschäftsmodus und seinen eigenständigen Werkstatt-Prompt erhalten; seine Fachwege in bestehende Vertiefungen integrieren. |

### 3.1 Belege und Grenzen der Bewertung

- **Bauträger:** Beide READMEs erklären im Abschnitt zu Schwesterplugins, dass sie dasselbe Mandat abdecken und eines von beiden genügt. Die [ausführliche Werkstatt](../../bautraegervertragspruefer/bautraegervertragspruefer-werkstatt.md) enthält weitere Rollen; ein rein käuferbezogener Zusammenschnitt würde Inhalte verlieren.
- **Arbeitszeugnisse:** Die beiden Arbeitswege [Zeugnisauftrag/Form/Tätigkeit – Analyse](../../arbeitszeugnis-analyse/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) und [Zeugnisauftrag/Form/Tätigkeit – Prüfer](../../arbeitszeugnispruefer/skills/zeugnisauftrag-form-taetigkeit-bearbeiten/SKILL.md) sowie vier weitere Fachwege erfüllen weitgehend dieselben Prüfaufträge.
- **Statusprüfung:** Der konkrete [Status- und Betriebsprüfungsweg](../../sozialversicherungspflicht-pruefer/skills/statusverfahren-und-betriebspruefung/SKILL.md) und die [internationalen/Nebenberufsfragen](../../sozialversicherungsstatus-pruefer/skills/international-nebenberuf-versicherung-bearbeiten/SKILL.md) lassen sich ergänzen. Eine einheitliche Antwort ohne Trennung der Rechtsfragen wäre dagegen ein fachlicher Rückschritt.
- **Einkauf:** Beide Angebotsvergleichs-Skills verlangen einen belegten positionsbezogenen Preisspiegel: [Projekteinkauf](../../projekteinkauf-baubranche/skills/angebote-vergleichen/SKILL.md), [Bauunternehmer](../../bauunternehmer-einkauf/skills/angebote-vergleichen/SKILL.md). Krimpfort/Brandschutztüren einschließlich LV-Entstehung und GAEB, Lüftungszentralen und Altstadt-Bordsteine müssen vollständig erreichbar bleiben.
- **Geldwäsche:** [Verdachtsfälle/Meldungen](../../geldwaeschebeauftragter/skills/verdachtsfaelle-meldungen-steuern/SKILL.md) und [FIU-Leitfaden](../../geldwaeschepraevention-aml-kyc/skills/aml-verdachtsmeldung-fiu-leitfaden/SKILL.md) zeigen den gemeinsamen Kern; berufs- und rollenabhängige Offenlegungsgrenzen dürfen beim Bündeln nicht verschwinden.
- **Sprache:** [Textübertragung mit Sprachmodi](../../einfache-leichte-sprache-jura/skills/text-uebertragen-bearbeiten/SKILL.md) und [juristischen Text übertragen](../../jura-in-einfacher-sprache/skills/juristischen-text-uebertragen/SKILL.md) überschneiden sich. Das Lernangebot [Deutsch als Zweitsprache](../../juristische-sprache-deutsch-als-zweitsprache/README.md) verfolgt ein anderes Ziel.
- **Staatsanwaltschaft:** Die Wege [Ermittlungsverfahren/Eingriffe](../../gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft/skills/ermittlungsverfahren-und-eingriffe-bearbeiten/SKILL.md) und [Praxiseinstieg Ermittlungsverfahren/Eingriffe](../../gerichtsplugins/staatsanwaltschaft-praxis-einstieg/skills/ermittlungsverfahren-und-eingriffe-bearbeiten/SKILL.md) bearbeiten dieselbe staatliche Aufgabe. Ein Anfängerzugang kann als Modus erhalten bleiben.
- **Corporate:** Trotz gemeinsamer Menüs sind die Bestände mit 86/99/226 Fachmodulen und 73/86/92 Vorlagendateien unterschiedlich. Der [Mittelstands-Intake](../../mittelstand-corporate-ma/skills/deal-intake/FACHINHALT.md) bezieht etwa Familie, Hausbank, Steuerberater und informelle Entscheidungen ein. Gleiche Skill-Namen beweisen keine identischen Fachinhalte.
- **Verträge:** Der [kompakte Hauptskill](../../vertragserstellung/skills/vertrag-vom-auftrag-bis-zur-endfassung-erstellen/SKILL.md) bezeichnet sich ausdrücklich als Ergänzung für ein mittelständisches Einzelgeschäft. Dieser überschaubare Arbeitsmodus muss bei einer Bündelung benutzbar bleiben.

## 4. Getrennte Einstiege mit fachlichem Grund

| Familie | Grund für getrennte Plugins oder Zugänge |
| --- | --- |
| Alle 24 Fachanwaltsprofile | Fachlicher Einstieg und Mandatsführung bleiben auffindbar; Spezialwerkzeuge ergänzen sie. Steuerrecht verweist auf den gemeinsamen Fachbestand. |
| Alle 16 Werkzeuge der [Insolvenzgruppe](../../insolvenzrecht-plugins/README.md) | Ausdrückliche Vorgabe: gemeinsamer Oberordner, alle Plugins behalten. Forderungsanmeldung, Insolvenzreifeprüfung und Planwerkstatt bleiben eigenständig; ebenso die übrigen Werkzeuge. Das Insolvenzgericht bleibt zusätzlich als eigene Gerichtsrolle bestehen. |
| Öffentliche Bauvergabe und privater Projekteinkauf | Auftraggeber, Bieter und Rechtsschutz haben andere Verfahren, Bindungen und Handlungsmöglichkeiten als private Einkäufer. |
| Bank-Rechtsabteilung, Private Equity und Venture Capital | Kredit/Auszahlung/Sicherheiten, Fondsfinanzierung und Beteiligungsrunde/Verwässerung sind unterschiedliche Aufträge und Arbeitsprodukte. |
| Gericht, Staatsanwaltschaft und Verteidigung | Unterschiedliche Verfahrensrollen, Neutralität, Informationszugänge und Interessen. Gemeinsame Quellenpflege ist möglich. |
| Compliance, Meldestelle und interne Untersuchung | Unterschiedliche Empfänger, Vertraulichkeitskreise und Untersuchungsaufträge; gemeinsame Sachverhalte rechtfertigen keine pauschale Zusammenlegung. |
| Kanzleialltag, Kanzleimanagement und KI-Arbeitsplatz | Mandatsabwicklung, Wirtschaftlichkeit und konkrete Computerbedienung mit Freigaben sind unterschiedliche Aufgaben. |
| KI-Governance und spezialisierte KI-Rechtswerkzeuge | Governance, Verbote, Hochrisiko, Konformität, Transparenz und Meldungen benötigen klare Abgrenzung. Ein gemeinsamer Einstieg ist sinnvoller als ein überladenes Gesamtplugin. |
| Allgemeiner Datenschutz und Datenschutzverteidigung | Laufende Beratung und Abwehr eines konkreten Vorwurfs unterscheiden sich in Rolle und Ziel. |

### 4.1 beA-Werkzeuge zuerst nach Ausgabeprofil unterscheiden

`bea-versand`, `schriftsatz-versandwerkstatt` und `schriftsatzwerkstatt-bea` überschneiden sich. Sie verwenden aber unterschiedliche Vorgaben zur Anlagenkennzeichnung und Benennung; etwa Kennzeichnung auf der ersten oder auf jeder Anlagenseite. Die [lokalen Regeln der Schriftsatzwerkstatt](../../schriftsatzwerkstatt-bea/AGENTS.md) sehen zudem eine bewusste Begleitfunktion vor.

Vor einer Zusammenlegung müssen benannte Ausgabeprofile und Prüfbeispiele zeigen, dass die jeweiligen Ergebnisse erhalten bleiben. `anlagen-zu-schriftsaetzen` hat daneben die eigenständige Aufgabe der inhaltlichen Beweiszuordnung. Diese vier Werkzeuge werden deshalb nicht als sofortige Zusammenlegung empfohlen.

## 5. Anforderungen an eine tatsächliche Zusammenlegung

1. **Vollständige Zuordnung:** Für jeden bisherigen Skill, jede Fachvertiefung, Vorlage, Testakte und jeden eigenständigen Prompt ein konkretes Ziel dokumentieren. Ähnliche Dateinamen allein reichen nicht zum Entfernen von Inhalten.
2. **Rollen erhalten:** Anfänger-/Expertenmodus, Mandatsseite, behördliche Rolle, Vertraulichkeit und Freigaben ausdrücklich abbilden. Der gemeinsame Hauptskill fragt nur die für den Arbeitsauftrag entscheidenden Unterschiede ab.
3. **Menü begrenzen:** Höchstens 20 aktive Skills; Vertiefungen dürfen ausführlich bleiben. Keine bloße Addition der alten Menüs.
4. **Alte Zugänge erhalten:** Bisherige Einstiegspfade als Wegweiser weiterführen. Marketplace, Manifeste, Download-Zuordnung, Skill-Verzeichnisse und Prompt-Verweise konsistent ändern. Bereits veröffentlichte Releases, Tags und Downloads erhalten.
5. **Arbeitsprodukte prüfen:** Repräsentative vorhandene Akten aus beiden Beständen mit ihren jeweiligen Rollen und Ergebnisformaten prüfen. Bei Einkaufsakten GAEB, Leistungsverzeichnis und Originaldateien ausdrücklich einbeziehen.
6. **Veröffentlichung nachweisen:** Paket bauen, Pflichtprüfungen durchführen und heruntergeladene veröffentlichte Assets gegen den geprüften Bestand abgleichen. Erst danach ist eine Zusammenlegung abgeschlossen.

## 6. Umgesetzter Umfang dieser Prüfung

Umgesetzt sind der eindeutige Steuerrechts-Wegweiser, die nach Rechtsgebieten geordnete Fachanwaltsübersicht und der Verweis von der Repository-Startseite. Die Wolkenfels-Downloadhinweise unterscheiden jetzt zutreffend das Originalformat-ZIP mit `Grundakte/` vom flachen Einzel-PDF-ZIP.

Die installierbaren Pakete, ihre Versionsstände und ihre Fachbestände bleiben in diesem Änderungssatz unverändert. Die Empfehlungen aus Abschnitt 3 sind als gesonderte Umsetzungsaufgaben dokumentiert.
