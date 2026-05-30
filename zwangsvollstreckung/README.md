# Zwangsvollstreckung


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Zwangsvollstreckung Mietrueckstand und Raeumung — Eppendorfer Altbau Grewenig — Vollstreckungsmappe Zweite Runde** (`zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde`) | [Gesamt-PDF lesen](../testakten/zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde/gesamt-pdf/zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsvollstreckung-mietruekstand-und-raeumung-eppendorfer-altbau-grewenig-vollstreckungsmappe-zweite-runde.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Freistehendes Cowork-Plugin für die Zwangsvollstreckung nach §§ 704 ff. ZPO aus allen Titelarten. Es ist ein vollständiger Arbeitsraum für Gläubigeranwalt, Inkasso, Hausverwaltung, Kreditbearbeitung und Insolvenzverwaltung: Titel prüfen, Klausel besorgen, Zustellung organisieren, Mahn- oder Vollstreckungsbescheid online beantragen, PfÜB gegen Bank, Arbeitgeber, Mieter oder Finanzamt entwerfen, Kontensuche § 802l ZPO und Vermögensauskunft beim Gerichtsvollzieher steuern, Mobiliar- und Räumungsaufträge erteilen, aus notarieller Urkunde § 800 ZPO oder Tabellenauszug § 201 InsO vollstrecken, ZVG-Antrag stellen und Schuldnerschutz auf Erinnerung, Vollstreckungsschutz und P-Konto-Bescheinigung beantworten.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Vollstreckungsmappe Sparkasse Niederrhein gegen Mueller** ([`testakten/vollstreckungsmappe-mueller-sparkasse-niederrhein/`](../testakten/vollstreckungsmappe-mueller-sparkasse-niederrhein/)).

Direkt-Download als ZIP: [testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Direkt herunterladen

- [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsvollstreckung.zip)
- [Testakte Mueller / Sparkasse Niederrhein](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip)

## Wofür das Plugin gedacht ist

- Vollstreckung aus allen Titelarten nach § 794 ZPO: Urteil, Versäumnisurteil, Anerkenntnisurteil, Vollstreckungsbescheid, Prozessvergleich, notarielle Unterwerfungsurkunde § 794 Abs. 1 Nr. 5 ZPO, Anwaltsvergleich, Kostenfestsetzungsbeschluss und Tabellenauszug § 201 InsO.
- Mahn- und Vollstreckungsbescheid online über das zentrale Mahnportal (Barcode-Datensatz, EGVP, beA, beN).
- Forderungspfändung nach §§ 829, 835 ZPO gegen Bank (Lohn- oder Kontokonto), Arbeitgeber (§ 850 ZPO mit Tabelle 1.7.2025), Mieter (§ 851b ZPO) und Finanzamt (Erstattungsansprüche).
- Kontensuche § 802l ZPO über das Bundeszentralamt für Steuern und Vermögensauskunft beim zuständigen Gerichtsvollzieher nach § 802c ZPO.
- Mobiliarvollstreckung und Räumungsauftrag § 885 ZPO (vollständig oder Berliner Modell) beim Gerichtsvollzieher.
- Grundstücksvollstreckung aus notarieller Grundschuldurkunde § 800 ZPO: Zwangsversteigerungsantrag § 15 ZVG, Beitrittsantrag, Sicherungs- vs. Eigentümergrundschuld, Rangverhältnisse.
- Insolvenz-Folgevollstreckung aus Tabellenauszug § 201 InsO nach Aufhebung des Verfahrens (Restschuldbefreiungsantrag pendent oder versagt).
- Schuldnerschutz: Erinnerung § 766 ZPO, Vollstreckungsschutz § 765a ZPO, P-Konto-Bescheinigung § 850k ZPO, Räumungsvollstreckungsschutz § 765a ZPO, Drittwiderspruchsklage § 771 ZPO.
- Reform-Stand 2026/2027: ZVollstrDigitG (BT-Drs. 21/4815, Bundestag 19.3.2026 beschlossen). Inkrafttreten Hauptteile 1.10.2026 (neue ZVFV-Formulare, § 829 Abs. 5 ZPO n.F. mit XML-Antrag als führender Form), Kreditinstitute-Pflicht zum sicheren Übermittlungsweg ab 1.10.2027 (§ 173 Abs. 2 Nr. 1 ZPO n.F., eBO/§ 130a Abs. 4 ZPO). § 840 ZPO erlaubt zusätzlich die Drittschuldnererklärung per Post.

## Leitprinzip

Das Plugin arbeitet titelorientiert und drittschuldnerorientiert. Es prüft erst, ob der Titel die richtige Maßnahme trägt (vollstreckbare Ausfertigung, Klausel, Zustellung, Wartefrist, Sicherheitsleistung), dann, ob der Drittschuldner der richtige Ansprechpartner ist (Sitz, Zustellungsweg, Erklärungspflicht, Auskunftsrecht). Erst danach erzeugt es Schriftsätze. Vollstreckungsschutz, P-Konto und Drittwiderspruch werden nicht als Hindernis behandelt, sondern als parallel zu führender Strang mit eigener Aktenlage. Reform-Übergänge (ZVollstrDigitG) werden datumsabhängig gesteuert: bis 30.9.2026 alte ZVFV, ab 1.10.2026 neue ZVFV-Formulare, ab 1.10.2027 sicherer Übermittlungsweg für Kreditinstitute Pflicht.

## Typischer Ablauf

1. Kommandocenter öffnen: Titelart, Schuldner, Drittschuldner, Forderungshöhe, Zustand der Klausel und Zustellung erfassen.
2. Titel-Klausel-Zustellung prüfen: vollstreckbare Ausfertigung, Klausel § 724 ZPO, Zustellungsnachweis § 750 ZPO, Wartefrist § 798 ZPO bei notarieller Urkunde, Sicherheitsleistung.
3. Vorfeld-Recherche: Vermögensauskunft beim Gerichtsvollzieher, Kontensuche § 802l ZPO über BZSt, Schuldnerverzeichnis § 882c ZPO.
4. Maßnahme wählen: PfÜB Bank/Arbeitgeber/Mieter/Finanzamt, Mobiliarvollstreckung, Räumung § 885 ZPO, ZVG-Antrag oder Tabellenauszug § 201 InsO.
5. Schriftsatz erzeugen: ZVFV-Formular (alt bis 30.9.2026 / neu ab 1.10.2026), Drittschuldnerzustellung organisieren, § 840-Erklärung anfordern.
6. Schuldnerseite begleiten: Erinnerung, Vollstreckungsschutz, P-Konto-Sockel berechnen, Drittwiderspruch prüfen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| zv-kommandocenter | Startet die Zwangsvollstreckung und entscheidet, welche Maßnahme und welcher Skill passt. |
| zv-titel-klausel-zustellung | Prüft vollstreckbare Ausfertigung, Klausel § 724 ZPO und Zustellungsnachweis § 750 ZPO. |
| zv-mahnbescheid-online | Erstellt den Antrag auf Mahnbescheid über das zentrale Mahnportal mit Barcode-Datensatz und EGVP. |
| zv-vollstreckungsbescheid-folge | Steuert Vollstreckungsbescheid, Klausel, Zustellung und Übergang zur Zwangsvollstreckung. |
| zv-pfueb-bank | Entwirft Pfändungs- und Überweisungsbeschluss gegen Bankguthaben mit P-Konto-Behandlung. |
| zv-pfueb-arbeitsentgelt | Pfändet Arbeitseinkommen § 850 ZPO mit Tabelle 1.7.2025, Unterhalts- und Privilegrang. |
| zv-pfueb-mieter-finanzamt | Pfändet Mietzinsforderungen § 851b ZPO und Erstattungsansprüche gegen das Finanzamt. |
| zv-vermoegensauskunft-gv | Beauftragt den Gerichtsvollzieher mit Vermögensauskunft § 802c ZPO und Schuldnerverzeichnis. |
| zv-kontensuche-drittschuldner | Steuert die Kontensuche § 802l ZPO über das Bundeszentralamt für Steuern. |
| zv-notarielle-urkunde-grundschuld | Vollstreckt aus notarieller Grundschuldurkunde § 800 ZPO inkl. Kündigung § 1193 BGB. |
| zv-zvg-antrag-glaeubiger | Stellt Zwangsversteigerungs- und Beitrittsantrag § 15 ZVG aus Gläubigersicht. |
| zv-tabellenauszug-201-inso | Vollstreckt aus Tabellenauszug § 201 InsO nach Aufhebung des Insolvenzverfahrens. |
| zv-mobiliar-gv-auftrag | Erteilt Mobiliarvollstreckungs- und Sachpfändungsauftrag (auch Krypto-Hardware-Wallets). |
| zv-raeumung-885 | Führt Räumungsvollstreckung § 885 ZPO inkl. Berliner Modell und Vollstreckungsschutz. |
| zv-abwehr-schuldner | Erstellt Erinnerung § 766 ZPO, Vollstreckungsschutz § 765a ZPO und Drittwiderspruch § 771 ZPO. |
| zv-vollstreckungsschutz-haertefall-765a | Vertiefter Härtefall-Schutz § 765a ZPO (Suizidgefahr, Schwangerschaft, Obdachlosigkeit, Trauerfall); Antragsformular mit Glaubhaftmachung. **NEU** |
| zv-eu-kontenpfaendung-655-2014 | Europäische Kontenpfändung VO (EU) 655/2014 — grenzüberschreitende vorläufige Sicherung von Bankkonten in der EU (außer Dänemark). **NEU** |
| zv-pfaendungstabelle-2025 | Hält die Pfändungstabelle 1.7.2025 bis 30.6.2026 nach § 850c ZPO bereit. Auto-Warnung des Rechners ab 1.6.2026. |
| zv-elektronische-zustellung-2027 | Steuert sicheren Übermittlungsweg für Kreditinstitute ab 1.10.2027 (ZVollstrDigitG). |

## Werkzeug

`werkzeuge/pfaendungsrechner.py` berechnet den pfändbaren Betrag nach § 850c ZPO mit der Tabelle 1.7.2025 bis 30.6.2026 (BGBl. 2025 I Nr. 110 vom 11.4.2025). Hartcodierte Eckwerte: Grundfreibetrag 1.555,00 EUR, Erhöhung erste Unterhaltspflicht 585,23 EUR, jede weitere bis zur 5. Person 326,04 EUR, Vollpfändungsgrenze 4.766,99 EUR, P-Konto-Sockel 1.560,00 EUR. Pfändbarkeitsquote nach § 850c Abs. 3 ZPO unterhaltsabhängig (7/10 / 5/10 / 4/10 / 3/10 / 2/10 / 1/10). CLI: `python pfaendungsrechner.py --netto 4200 --unterhalt 3` gibt den pfändbaren Betrag, den verbleibenden P-Konto-Sockel und die Tabellenherleitung aus.

## Reform ZVollstrDigitG 2026/2027

| Datum | Was ändert sich |
| --- | --- |
| bis 30.9.2026 | Alte ZVFV-Formulare bleiben gültig, § 829 ZPO unverändert. |
| ab 1.10.2026 | Neue ZVFV-Formulare verbindlich, § 829 Abs. 5 ZPO n.F.: XML-Datensatz wird führend. |
| ab 1.10.2027 | Kreditinstitute müssen sicheren Übermittlungsweg vorhalten (§ 173 Abs. 2 Nr. 1 ZPO n.F., eBO/§ 130a Abs. 4 ZPO). § 840 ZPO-Erklärung weiterhin per Post zulässig. |

## Grenzen

Das Plugin trifft keine unüberprüfte Vollstreckungsentscheidung und ersetzt keine fachliche Prüfung. Bei streitigen Rechtsfragen (Klauselgegenklage § 768 ZPO, Vollstreckungsabwehrklage § 767 ZPO, Drittwiderspruch § 771 ZPO), bei Räumung mit Härtefall, bei ZVG-Anträgen mit Rangstreit und bei grenzüberschreitender Vollstreckung (EU-Kontenpfändungsverordnung Nr. 655/2014, EU-Zustellungs-VO 2020/1784) verlangt es ausdrücklich menschliche Freigabe. Reform-Übergänge ZVollstrDigitG sind datumsabhängig gesteuert und müssen bei jedem Antrag gegen das tatsächliche Inkrafttretensdatum laut BGBl-Verkündung gegengeprüft werden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 20 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Zwangsvollstreckung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan... |
| `zv-abwehr-schuldner` | Schuldner will sich gegen laufende Zwangsvollstreckung wehren oder hat unrechtmäßigen Pfaendungs-Beschluss erhalten. §§ 766 767 768 771 765a 850k 769 ZPO Schuldnerrechte. Prüfraster: Erinnerung § 766 formale Maengel Vollstreckungsabwehrk... |
| `zv-elektronische-zustellung-2027` | Gläubiger oder Kreditinstitut fragt: Was aendert sich durch die Digitalisierung der Zwangsvollstreckung ab 2026/2027? ZVollstrDigitG BT-Drs. 21/4815. Prüfraster: XML-Antrag § 829 Abs. 5 ZPO n.F. ab 1.10.2026 Pflicht sicherer Übermittlung... |
| `zv-eu-kontenpfaendung-655-2014` | Gläubiger hat Schuldner der im EU-Ausland ein Bankkonto haelt und moechte dieses vorlaeufig sichern. EuKtPVO VO (EU) 655/2014 §§ 946 ff. ZPO. Prüfraster: Antrag deutsches Gericht Glaubhaftmachung Anspruch Sicherungsbedürfnis Sicherheitsl... |
| `zv-kommandocenter` | Gläubiger oder Anwalt hat vollstreckbaren Titel und fragt: Welche Vollstreckungsart ist im konkreten Fall am sinnvollsten und wie wird sie eingeleitet? Startpunkt Zwangsvollstreckung. Prüfraster: Titelart und Vollstreckungsziel Routing z... |
| `zv-kontensuche-drittschuldner` | Gläubiger hat Urteil aber kein bekanntes Konto oder Arbeitgeber des Schuldners. § 802l ZPO Drittauskunfte. Prüfraster: Rentenversicherung Bund Bundeszentralamt für Steuern Kontenabruf Kraftfahrt-Bundesamt Schuldnerverzeichnis § 882b ZPO.... |
| `zv-mahnbescheid-online` | Gläubiger will Forderung ohne Klage per Mahnbescheid titulieren lassen. §§ 688 ff. ZPO Online-Mahnverfahren. Prüfraster: Schlüssigkeitsprüfung Antragstyp Gerichtsstand Hauptforderung Nebenforderungen Zinsen Kostenansatz beA EGVP Verjähru... |
| `zv-mobiliar-gv-auftrag` | Gläubiger beauftragt Gerichtsvollzieher mit Sachpfaendung beweglicher Gegenstaende beim Schuldner. §§ 808 ff. ZPO Mobiliar-Pfaendung. Prüfraster: GV-Auftrag Modulwahl § 802a ZPO Anlaufstellen Wohnung Geschäftsräume Unpfaendbarkeitskatalo... |
| `zv-notarielle-urkunde-grundschuld` | Gläubiger hat notarielle Grundschuld-Urkunde und will vollstrecken. § 794 Abs. 1 Nr. 5 ZPO Zwangsvollstreckung aus notarieller Urkunde. Prüfraster: Unterwerfungsklausel dinglich und persoenlich Klauselumschreibung § 727 ZPO bei Abtretung... |
| `zv-pfaendungstabelle-2025` | Lohnpfaendung oder Rentenpfaendung ist beantragt und der pfaendbare Betrag muss konkret berechnet werden. Pfaendungsfreigrenzenbekanntmachung 1.7.2025 gueltig bis 30.6.2026. Prüfraster: Freibetrag § 850c ZPO Unterhaltsstaffel Pfaendungss... |
| `zv-pfueb-arbeitsentgelt` | Gläubiger will Lohn oder Gehalt des Schuldners pfaenden lassen. §§ 829 835 850 ff. ZPO Lohnpfaendung PfUeB. Prüfraster: PfUeB gegen Arbeitgeber als Drittschuldner pfaendbarer Betrag Pfaendungstabelle 1.7.2025 bis 30.6.2026 Unterhaltsbere... |
| `zv-pfueb-bank` | Gläubiger will Bankkonto des Schuldners pfaenden lassen. §§ 829 835 ZPO PfUeB Bankkonten. Prüfraster: Antrag Drittschuldner-Bank P-Konto-Schutz § 850k ZPO Sockelbetrag Kindergeld Erhöhungen ZVollstrDigitG XML-Antrag ab 1.10.2026 elektron... |
| `zv-pfueb-mieter-finanzamt` | Gläubiger will Mietforderung Steuererstattung oder Forderung gegen sonstigen Drittschuldner pfaenden. §§ 829 835 851 850b ZPO sonstige Drittschuldner. Prüfraster: Mieter Mietzinsforderung Finanzamt Steuererstattung Kranken-kasse Krankeng... |
| `zv-raeumung-885` | Vermieter hat Räumungsurteil und will Wohnung oder Gewerberaum räumen lassen. § 885 ZPO Räumungsvollstreckung. Prüfraster: Räumungstitel Klausel Zustellung Mitbewohner Kinder Untermieter Drittwiderspruch § 771 Vollstreckungsschutz § 765a... |
| `zv-tabellenauszug-201-inso` | Gläubiger hat Insolvenzforderung die im Verfahren festgestellt wurde und will nach Insolvenzende vollstrecken. § 201 Abs. 2 InsO Tabellenauszug als Titel. Prüfraster: Voraussetzungen festgestellt nicht bestritten kein RSB-Versagungsgrund... |
| `zv-titel-klausel-zustellung` | Gläubiger hat Urteil oder sonstigen Titel und prüft vor Vollstreckungsbeginn die drei formalen Voraussetzungen. §§ 704 724 750 ZPO Titel Klausel Zustellung. Prüfraster: vollstreckbarer Titel Vollstreckungsklausel Urkundsbeamter/Notar/Ins... |
| `zv-vermoegensauskunft-gv` | Gläubiger weiss nichts über Vermögen des Schuldners und will Auskunft erzwingen. § 802c ZPO Vermogensauskunft EV. Prüfraster: Antrag beim GV Sperrfrist 2 Jahre § 802d ZPO Eintragung Schuldnerverzeichnis § 882b ZPO Erzwingungshaft § 802g... |
| `zv-vollstreckungsbescheid-folge` | Mahnbescheid wurde erlassen und Gläubiger muss entscheiden wie es weitergeht. § 699 ZPO Vollstreckungsbescheid Online-Mahnportal. Prüfraster: Beantragung VB Reaktion auf Einspruch § 700 ZPO Übergang streitiges Verfahren Wirkung VB als Ti... |
| `zv-vollstreckungsschutz-haertefall-765a` | Schuldner ist schwerkrank suizidgefaehrdet oder sonst besonders schutzbedürftig und will Vollstreckung stoppen. § 765a ZPO Vollstreckungsschutz sittenwidrige Haerte. Prüfraster: Antrag Einstellung oder Beschraenkung Haerteanwendungsfaell... |
| `zv-zvg-antrag-glaeubiger` | Gläubiger hat Grundschuld oder Hypothek und will Immobilie des Schuldners versteigern lassen. ZVG Zwangsversteigerungsgesetz. Prüfraster: Antrag Anordnung §§ 15 ff. ZVG Beitritt § 27 ZVG geringstes Gebot Bargebot Verteilungstermin vorher... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
