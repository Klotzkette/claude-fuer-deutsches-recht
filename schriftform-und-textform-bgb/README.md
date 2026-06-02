# Schriftform und Textform im BGB

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`schriftform-und-textform-bgb`) | [`schriftform-und-textform-bgb.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftform-und-textform-bgb.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Schriftform-Maklervertrag – Eheleute Haspelbeck-Türkenfeld** (`schriftform-maklervertrag-muenchen-eheleute-haspelbeck`) | [Gesamt-PDF lesen](../testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck/gesamt-pdf/schriftform-maklervertrag-muenchen-eheleute-haspelbeck_gesamt.pdf) | [`testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip) |
| **Schriftform der Wohnraumkündigung — Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen** (`schriftform-mietkuendigung-bielefeld-online-pferdedrescher`) | [Gesamt-PDF lesen](../testakten/schriftform-mietkuendigung-bielefeld-online-pferdedrescher/gesamt-pdf/schriftform-mietkuendigung-bielefeld-online-pferdedrescher_gesamt.pdf) | [`testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Plugin-Slug:** `schriftform-und-textform-bgb`
**Version:** 3.2.1
**Autor:** Klotzkette

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Schriftform und Textform im BGB (`schriftform-und-textform-bgb`) | [schriftform-und-textform-bgb.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftform-und-textform-bgb.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakten

Zu diesem Plugin existieren 2 vollständige Beispielakten:

| Akte | Quelle | Direkt-Download |
|---|---|---|
| Schriftform-Maklervertrag – Eheleute Haspelbeck-Türkenfeld | [`testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck/`](../testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck/) | [testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip) |
| Schriftform der Wohnraumkündigung — Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen | [`testakten/schriftform-mietkuendigung-bielefeld-online-pferdedrescher/`](../testakten/schriftform-mietkuendigung-bielefeld-online-pferdedrescher/) | [testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip) |

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `schriftform-und-textform-bgb.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe ob unser Maklervertrag der Textform § 126b BGB genügt.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Überblick

Umfassender Workflow-Organisator für Schriftform- und Textform-Erfordernisse im deutschen Zivilrecht. Das Plugin trennt Papierform, qES, Textform, beA/ERV, gerichtliche Zustellung und prozessuale Formfiktion und bietet kanzleitaugliche Orientierung für alle wesentlichen Formerfordernisse des BGB.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 130e ZPO und § 46h ArbGG seit 17.07.2024** — Formfiktion für klar erkennbare Willenserklärungen in elektronischen vorbereitenden Schriftsätzen, auch wenn elektronische Form materiell eigentlich ausgeschlossen ist.

## Skill-Verzeichnis

### Block A — Formvorschriften-Grundlagen

| Skill | Inhalt |
|-------|--------|
| `formerfordernisse-im-bgb-ueberblick` | Systematik §§ 125-129 BGB, Nichtigkeit § 125 BGB, Heilung |
| `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift` | Originalunterschrift, Namenszeichnung, Faksimile, BGH-Linie |
| `elektronische-form-paragraph-126a-bgb-qes` | qES, eIDAS, Zertifikatskette, Zugang, beA-Abgrenzung, § 130e ZPO und § 46h ArbGG |
| `textform-paragraph-126b-bgb-dauerhafter-datentraeger` | E-Mail, WhatsApp, SMS, PDF als dauerhafter Datenträger |
| `notarielle-beurkundung-und-oeffentliche-beglaubigung` | § 128, § 129 BGB, BeurkG, GmbH, Grundstück, Erbvertrag |

### Block B — Zugang der formgerechten Erklärung

| Skill | Inhalt |
|-------|--------|
| `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb` | Zugangslehre, Machtbereich, Annahmeverweigerung |
| `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` | qES-Zugang, Transfervermerk § 298 Abs. 3 ZPO, Lehrsatz |
| `kuendigung-per-schriftsatz-zustellung-formfragen` | beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, Zustellung, Vollmacht und § 174 BGB |
| `mandantenwarnung-qes-per-email-whatsapp-und-zugang` | Mandantenmemo: Mail-Anhänge prüfen, IT-Hinweise |

### Block C — Spezielle Formerfordernisse

| Skill | Inhalt |
|-------|--------|
| `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` | § 656a BGB: E-Mail, Signaturhinweis, Textform und Verifizierungspflicht |
| `wohnraummiete-kuendigung-paragraph-568-bgb` | § 568, qES-Zugang, Begründungspflicht, Praxisempfehlung |
| `gewerberaummiete-paragraph-550-bgb-langzeitform` | Langzeitform, Heilung, ordentliche Kündigung bei Verstoß |
| `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` | § 766, § 492, § 311b BGB, strenge Formen |
| `arbeitsrecht-befristung-und-aufhebung-paragraph-14-tzbfg-623-bgb` | § 14 Abs. 4 TzBfG, § 623 BGB, Aufhebungsvertrag |

### Block D — Workflow-Organisator

| Skill | Inhalt |
|-------|--------|
| `form-checker-fuer-vertrag-oder-willenserklaerung` | Entscheidungsbaum, Konsequenzen, Klausel-Vorschlag |
| `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt` | Schriftformklausel, doppelte Schriftformklausel, AGB-Falle |
| `prozessablauf-papier-vs-elektronisch` | Workflow-Schritte: Papier, qES-Direktversand, beA-Schriftsatz mit Formfiktion und Textform |
| `dokumentations-und-beweisarchitektur` | Zugangsnachweis, qES-Validierung, TR-RESISCAN |

### Block E — Anspruchsgrundlagen-Modul

| Skill | Inhalt |
|-------|--------|
| `anspruchsformulierungen-bei-formverstoss` | § 812 BGB, Räumungsklage, Feststellungsklage, c.i.c. |
| `verteidigungsstrategie-bei-formangriff` | Heilung, § 242 BGB, Beweislast, Treuwidrigkeit |
| `mandantenkorrespondenz-form-und-zugang-templates` | Mandantenbriefe, Checklisten, Warnmemos |

## Hinweis

Alle Skills sind kanzleitauglich formuliert und enthalten vollständige Klauseltexte, Mandantenmemos und Querverweise auf aktuelle BGH-Rechtsprechung. Das Plugin ersetzt keine individuelle Rechtsberatung.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Schriftform Und Textform Bgb-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Ar... |
| `anspruchsformulierungen-bei-formverstoss` | Workflow-Skill zu anspruchsformulierungen bei formverstoss. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `arbeitsrecht-befristung-und-aufhebung-paragraph-14-tzbfg-623-bgb` | Arbeitgeber oder Arbeitnehmer fragt, ob Befristung, Kündigung oder Aufhebungsvertrag wegen Formverstoß unwirksam ist. Prüft § 14 Abs. 4 TzBfG, § 623 BGB, § 126 BGB, qES bei Befristung, direkte elektronische Form, § 46h ArbGG, § 174 BGB u... |
| `befristungsabrede-qes-rechtsprechung-stand-2026` | Aktuelle Rechtsprechung zur elektronischen Signatur bei Befristungsabreden nach § 14 Abs. 4 TzBfG. Prüft Scan, einfache E-Signatur, echte qES, ArbG-Gera-Linie, § 623 BGB, § 46h ArbGG als Sonderpfad und Mandantenhinweise für Arbeitgeber u... |
| `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` | Mandant hat Buergschaft oder Darlehensvertrag unterschrieben und fragt ob er noch gebunden ist wenn die Form nicht korrekt eingehalten wurde. §§ 766 492 484 311b BGB strenge Formerfordernisse. Prüfraster: Buergschaft § 766 BGB Schriftfor... |
| `dokumentations-und-beweisarchitektur` | Anwalt oder Kanzlei muss sicherstellen dass Formerklärungen beweissicher dokumentiert und archiviert werden. Beweissicherung Willenserklärungen Formrecht. Prüfraster: Zugang § 130 BGB nachweisen Originalurkunden aufbewahren qES-Validieru... |
| `elektronische-form-paragraph-126a-bgb-qes` | Workflow-Skill zu elektronische form paragraph 126a bgb qes. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `form-checker-fuer-vertrag-oder-willenserklaerung` | Mandant hat Vertrag oder Willenserklärung und fragt: Welche Form ist vorgeschrieben wurde sie eingehalten und was passiert wenn nicht? Form-Checker BGB. Prüfraster: gesetzliche vs. gewillkuerte Form Formhierarchie Nichtigkeitsfolge § 125... |
| `formerfordernisse-im-bgb-ueberblick` | Systematik der Formerfordernisse im BGB: gesetzliche vs. gewillkürte Form, §§ 125-129 BGB, Nichtigkeitsfolge § 125 BGB, Heilungsmöglichkeiten, Formhierarchie von Textform bis notarielle Beurkundung — Einstieg und Überblick für die Kanzle... |
| `gewerberaummiete-paragraph-550-bgb-langzeitform` | Gewerbemieter oder Vermieter fragt: Ist ein laenger als 1 Jahr laufender Gewerberaummietvertrag wegen Schriftform-Verstoß vorzeitig kündbar? § 550 BGB Langzeitform Gewerberaummietvertrag. Prüfraster: Schriftformerfordernis Mietvertraege... |
| `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt` | Workflow-Skill zu klauselgenerator formvorbehalt und aenderungsvorbehalt. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `kuendigung-per-schriftsatz-zustellung-formfragen` | Anwalt versendet oder empfängt eine Kündigung per Schriftsatz und fragt nach Formwirksamkeit. Prüft Schriftform, beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, § 173 ZPO, § 186 ZPO, § 298 Abs. 3 ZPO und § 174 BGB. Output: Form- und Zugan... |
| `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` | Workflow-Skill zu Maklervertrag, § 656a BGB und Textform. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; behauptete Rechtsprechung zu I ZR 202/25 nie ohne Live-Pruefung zitieren. |
| `mandantenkorrespondenz-form-und-zugang-templates` | Workflow-Skill zu mandantenkorrespondenz form und zugang templates. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `mandantenwarnung-qes-per-email-whatsapp-und-zugang` | Workflow-Skill zu mandantenwarnung qes per email whatsapp und zugang. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `notarielle-beurkundung-und-oeffentliche-beglaubigung` | Mandant muss einen Vertrag notar-beurkunden lassen (GmbH-Kauf Grundstueckskauf Ehevertrag) und fragt nach Ablauf und Kosten. §§ 128 129 BGB Beurkundungsgesetz. Prüfraster: Beurkundungspflicht § 311b BGB Grundstueck § 15 GmbHG GmbH-Anteil... |
| `prozessablauf-papier-vs-elektronisch` | Kanzlei oder Mandant muss zwischen Papier, qES, Textform, beA-Schriftsatz oder Formfiktion wählen. Prüft Originalunterschrift, qES-Direktversand, § 130e ZPO, § 46h ArbGG, Textform per E-Mail, Zustellung und Beweisarchitektur. Output: kon... |
| `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift` | Vertragspartner bestreitet Schriftform wegen fehlender oder unzureichender Unterschrift. § 126 BGB Schriftform eigenhaendige Namenszeichnung. Prüfraster: Namenszeichnung vs. Paraphe Urkundeneinheit bei mehrseitigen Vertraegen Blankounter... |
| `sftf-arbeitsvertraege-nachweisgesetz-spezial` | Spezialfall Schriftform im Arbeitsverhaeltnis nach Nachweisgesetzaenderung 2022: schriftliche Aushaendigung, Bussgeld, Befristung. Pruefraster fuer Arbeitgeber. |
| `sftf-doppelschriftform-aufhebung-spezial` | Spezialfall Aufhebung der doppelten Schriftform durch Individualabrede: BGH-Rechtsprechung, Auslegung, Beweisrisiko. Pruefraster fuer langlaufende Vertraege. |
| `sftf-elektronische-signatur-leitfaden` | Leitfaden qualifizierte elektronische Signatur eIDAS: Vertrauensdienst, eID, Fernsignatur. Pruefraster fuer Vertraege und behoerdliche Verfahren. |
| `sftf-formvorgaben-bauleiter` | Bauleiter Formvorgaben BGB § 126 sowie § 126a sowie § 126b: Schriftform, elektronische Form, Textform. Pruefraster Vertraege Wohnraum, Arbeit, Verbraucher. |
| `spezial-bgb-mehrparteien-konflikt-und-interessen` | BGB: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-checklisten-schriftsatz-brief-und-memo-bausteine` | Checklisten: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-dokumentation-verhandlung-vergleich-und-eskalation` | Dokumentation: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-empfangsbeduerftiger-international-schnittstellen` | Empfangsbeduerftiger: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-formerfordernisse-erstpruefung-und-mandatsziel` | Formerfordernisse: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-formwahl-zugang-und-beweis` | Formwahl, Zugang und Beweisrisiko im BGB und Prozessrecht: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-live-zahlen-schwellen-und-berechnung` | Live: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-paragraph-red-team-und-qualitaetskontrolle` | Paragraph: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-prozessablauf-mandantenentscheidung` | Prozessablauf: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-prozessordnungen-behoerden-gericht-und-registerweg` | Prozessordnungen: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsprechung-livecheck-formfragen` | Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-rechtsprechung-livequellen-und-rechtsprechungscheck` | Rechtsprechung: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schriftform-fristen-form-und-zustaendigkeit` | Schriftform: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-textform-dokumentenmatrix-und-lueckenliste` | Textform: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verifikation-compliance-dokumentation-und-akte` | Verifikation: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-willenserklaerung-formular-portal-und-einreichung` | Willenserklaerung: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zivilrecht-tatbestand-beweis-und-belege` | Zivilrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zugang-risikoampel-und-gegenargumente` | Zugang: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `textform-paragraph-126b-bgb-dauerhafter-datentraeger` | Workflow-Skill zu textform paragraph 126b bgb dauerhafter datentraeger. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `verteidigungsstrategie-bei-formangriff` | Mandant wird von Vertragspartner mit Formmangel-Einwand konfrontiert und Anwalt muss Verteidigung aufbauen. Verteidigung Formverstoß §§ 125 242 BGB. Prüfraster: Heilungsmöglichkeiten nach Vollzug (§ 311b BGB) Nachholung der Form § 242 BG... |
| `wohnraummiete-kuendigung-paragraph-568-bgb` | Workflow-Skill zu wohnraummiete kuendigung paragraph 568 bgb. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin schriftform-und-textform-bgb: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin schriftform-und-textform-bgb: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin schriftform-und-textform-bgb: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin schriftform-und-textform-bgb: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin schriftform-und-textform-bgb: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin schriftform-und-textform-bgb: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin schriftform-und-textform-bgb: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin schriftform-und-textform-bgb: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin schriftform-und-textform-bgb: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb` | Mandant fragt: Wann gilt Kündigung Mahnung oder sonstige Erklärung als zugegangen und ab wann laeuft die Frist? § 130 BGB Zugang. Prüfraster: Machtbereichslehre Möglichkeit der Kenntnisnahme Zugangsvereitelung Annahmeverweigerung Briefka... |
| `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` | Workflow-Skill zu zugang formgerechter erklaerung bgh viii zr 159 23. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
