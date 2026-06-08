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

Automatisch generierte Komplett-Liste aller 53 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlicher-formkern-bgb-zpo-check` | Amtlicher Formkern-Check für BGB und ZPO: trennt Schriftform, Textform, elektronische Form, qES, beA/EGVP, § 130e ZPO, Zustellung, Zugang und Beweiskraft elektronischer Dokumente im Schriftform Und Textform Bgb: prüft konkret die einschl... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `anspruchsformulierungen-formverstoss` | Prüfungslinie für anspruchsformulierungen bei formverstoss: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textform Bgb: prüft... |
| `arbeitsrecht-befristung-schriftform-checker` | Arbeitgeber oder Arbeitnehmer fragt, ob Befristung, Kündigung oder Aufhebungsvertrag wegen Formverstoß unwirksam ist. Prüft § 14 Abs. 4 TzBfG, § 623 BGB, § 126 BGB, qES bei Befristung, direkte elektronische Form, § 46h ArbGG, § 174 BGB u... |
| `befristungsabrede-qes-rechtsprechung` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung... |
| `befristungsabrede-qes-rechtsprechung-stand-2026` | Aktuelle Rechtsprechung zur elektronischen Signatur bei Befristungsabreden nach § 14 Abs. 4 TzBfG. Prüft Scan, einfache E-Signatur, echte qES, ArbG-Gera-Linie, § 623 BGB, § 46h ArbGG als Sonderpfad und Mandantenhinweise für Arbeitgeber u... |
| `bgb-mehrparteien-konflikt-und-interessen` | BGB: Mehrparteienkonflikt und Interessenmatrix im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schriftform Und... |
| `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` | Mandant hat Buergschaft oder Darlehensvertrag unterschrieben und fragt ob er noch gebunden ist wenn die Form nicht korrekt eingehalten wurde. §§ 766 492 484 311b BGB strenge Formerfordernisse. Prüfraster: Buergschaft § 766 BGB Schriftfor... |
| `checklisten-schriftsatz-brief-und-memo-bausteine` | Checklisten: Schriftsatz-, Brief- und Memo-Bausteine im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schriftfor... |
| `dokumentations-und-beweisarchitektur` | Anwalt oder Kanzlei muss sicherstellen dass Formerklärungen beweissicher dokumentiert und archiviert werden. Beweissicherung Willenserklärungen Formrecht. Prüfraster: Zugang § 130 BGB nachweisen Originalurkunden aufbewahren qES-Validieru... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `elektronische-paragraph-formerfordernisse` | Prüfungslinie für elektronische form paragraph 126a bgb qes: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textform Bgb: prüft... |
| `empfangsbeduerftiger-international` | Dokumentation: Verhandlung, Vergleich und Eskalation im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schriftfor... |
| `empfangsbeduerftiger-international-schnittstellen` | Empfangsbeduerftiger: Internationaler Bezug und Schnittstellen im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im... |
| `form-checker-fuer-vertrag-oder-willenserklaerung` | Mandant hat Vertrag oder Willenserklärung und fragt: Welche Form ist vorgeschrieben wurde sie eingehalten und was passiert wenn nicht? Form-Checker BGB. Prüfraster: gesetzliche vs. gewillkuerte Form Formhierarchie Nichtigkeitsfolge § 125... |
| `formerfordernisse-erstpruefung-und-mandatsziel` | Formerfordernisse: Erstprüfung, Rollenklärung und Mandatsziel im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im S... |
| `formerfordernisse-im-bgb-ueberblick` | Systematik der Formerfordernisse im BGB: gesetzliche vs. gewillkürte Form, §§ 125-129 BGB, Nichtigkeitsfolge § 125 BGB, Heilungsmöglichkeiten, Formhierarchie von Textform bis notarielle Beurkundung — Einstieg und Überblick für die Kanzle... |
| `formwahl-zugang-live-prozessablauf` | Formwahl, Zugang und Beweisrisiko im BGB und Prozessrecht: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Schriftform Und Textform Bgb: prüft konkret die einschlägigen... |
| `gewerberaummiete-paragraph-550-bgb-langzeitform` | Gewerbemieter oder Vermieter fragt: Ist ein laenger als 1 Jahr laufender Gewerberaummietvertrag wegen Schriftform-Verstoß vorzeitig kündbar? § 550 BGB Langzeitform Gewerberaummietvertrag. Prüfraster: Schriftformerfordernis Mietvertraege... |
| `klauselgenerator-formvorbehalt-maklervertrag` | Prüfungslinie für klauselgenerator formvorbehalt und aenderungsvorbehalt: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textfo... |
| `kuendigung-per-mandantenkorrespondenz-zugang` | Anwalt versendet oder empfängt eine Kündigung per Schriftsatz und fragt nach Formwirksamkeit. Prüft Schriftform, beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, § 173 ZPO, § 186 ZPO, § 298 Abs. 3 ZPO und § 174 BGB. Output: Form- und Zugan... |
| `live-zahlen-schwellen-und-berechnung` | Live: Zahlen, Schwellenwerte und Berechnung im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schriftform Und Tex... |
| `mandantenkorrespondenz-form-und-zugang-templates` | Prüfungslinie für mandantenkorrespondenz form und zugang templates: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textform Bgb... |
| `mandantenwarnung-qes-per-email-whatsapp-und-zugang` | Prüfungslinie für mandantenwarnung qes per email whatsapp und zugang: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textform B... |
| `notarielle-beurkundung-prozessablauf-papier` | Mandant muss einen Vertrag notar-beurkunden lassen (GmbH-Kauf Grundstueckskauf Ehevertrag) und fragt nach Ablauf und Kosten. §§ 128 129 BGB Beurkundungsgesetz. Prüfraster: Beurkundungspflicht § 311b BGB Grundstueck § 15 GmbHG GmbH-Anteil... |
| `output-waehlen` | Output wählen im Plugin Schriftform Und Textform Bgb: Diese Output-Weiche für Schriftform Und Textform Bgb entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `paragraph-fehlerkatalog` | Paragraph Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `prozessablauf-mandantenentscheidung` | Prozessablauf: Mandantenkommunikation und Entscheidungsvorlage im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im... |
| `prozessablauf-papier-vs-elektronisch` | Kanzlei oder Mandant muss zwischen Papier, qES, Textform, beA-Schriftsatz oder Formfiktion wählen. Prüft Originalunterschrift, qES-Direktversand, § 130e ZPO, § 46h ArbGG, Textform per E-Mail, Zustellung und Beweisarchitektur. Output: kon... |
| `prozessordnungen-textform-verifikation` | Prozessordnungen: Behörden-, Gerichts- oder Registerweg im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schrift... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsprechung-livecheck-formfragen` | Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Schriftform Und Textform Bgb: prüft konkret die eins... |
| `rechtsprechung-quellenkarte` | Rechtsprechung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schriftform-fristen-form-und-zustaendigkeit` | Schriftform: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schrift... |
| `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift` | Vertragspartner bestreitet Schriftform wegen fehlender oder unzureichender Unterschrift. § 126 BGB Schriftform eigenhaendige Namenszeichnung. Prüfraster: Namenszeichnung vs. Paraphe Urkundeneinheit bei mehrseitigen Vertraegen Blankounter... |
| `schriftform-textform-bgb-start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Schriftform Und Textform Bgb-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan... |
| `sftf-arbeitsvertraege-nachweisgesetz` | Spezialfall Schriftform im Arbeitsverhaeltnis nach Nachweisgesetzaenderung 2022: schriftliche Aushaendigung, Bussgeld, Befristung. Pruefraster für Arbeitgeber im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsme... |
| `sftf-doppelschriftform-aufhebung-spezial` | Spezialfall Aufhebung der doppelten Schriftform durch Individualabrede: BGH-Rechtsprechung, Auslegung, Beweisrisiko. Pruefraster für langlaufende Vertraege im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsmerkm... |
| `sftf-elektronische-signatur-leitfaden` | Leitfaden qualifizierte elektronische Signatur eIDAS: Vertrauensdienst, eID, Fernsignatur. Pruefraster für Vertraege und behoerdliche Verfahren im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen... |
| `sftf-formvorgaben-bgb-interessen-checklisten` | Bauleiter Formvorgaben BGB § 126 sowie § 126a sowie § 126b: Schriftform, elektronische Form, Textform. Pruefraster Vertraege Wohnraum, Arbeit, Verbraucher im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsmerkma... |
| `textform-dokumentenmatrix-und-lueckenliste` | Textform: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schri... |
| `textform-paragraph-verteidigungsstrategie` | Prüfungslinie für textform paragraph 126b bgb dauerhafter datentraeger: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textform... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verifikation-compliance-dokumentation-und-akte` | Verifikation: Compliance-Dokumentation und Aktenvermerk im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schrift... |
| `verteidigungsstrategie-bei-formangriff` | Mandant wird von Vertragspartner mit Formmangel-Einwand konfrontiert und Anwalt muss Verteidigung aufbauen. Verteidigung Formverstoß §§ 125 242 BGB. Prüfraster: Heilungsmöglichkeiten nach Vollzug (§ 311b BGB) Nachholung der Form § 242 BG... |
| `willenserklaerung-zivilrecht-zugang` | Willenserklaerung: Formular, Portal und Einreichungslogik im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Schri... |
| `wohnraummiete-kuendigung-paragraph-568-bgb` | Prüfungslinie für wohnraummiete kuendigung paragraph 568 bgb: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Schriftform Und Textform Bgb: prüf... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprech... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Schriftform Und Textform Bgb: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechun... |
| `zivilrecht-tatbestand-beweis-und-belege` | Zivilrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Sch... |
| `zugang-empfangsbeduerftiger-formgerechter` | Mandant fragt: Wann gilt Kündigung Mahnung oder sonstige Erklärung als zugegangen und ab wann laeuft die Frist? § 130 BGB Zugang. Prüfraster: Machtbereichslehre Möglichkeit der Kenntnisnahme Zugangsvereitelung Annahmeverweigerung Briefka... |
| `zugang-risikoampel-und-gegenargumente` | Zugang: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin schriftform und textform bgb; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Sch... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
