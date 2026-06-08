# VerkehrsOWi-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verkehrsowi-verteidiger`) | [`verkehrsowi-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Norderhof-Tannenmoor — Abstandsverstoß Section Control BAB 7 Bispingen, Bußgeld und Fahrverbot** (`verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof/gesamt-pdf/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof_gesamt.pdf) | [`testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip) |
| **VerkehrsOWi – Qualifizierter Rotlichtverstoß, Tempoüberschreitung und Fahrverbot** (`verkehrsowi-rotlicht-tempo`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-rotlicht-tempo/gesamt-pdf/verkehrsowi-rotlicht-tempo_gesamt.pdf) | [`testakte-verkehrsowi-rotlicht-tempo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-rotlicht-tempo.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Verteidigungsassistent für Verkehrsordnungswidrigkeiten: vom Anhörungsbogen über Einspruch, Akteneinsicht, Messakte und Punkte bis zur Amtsgerichtsverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `verkehrsowi-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `verkehrsowi-kommandocenter` - VerkehrsOWi-Kommandocenter
- `verkehrsowi-aktenanlage` - Aktenanlage und Dokumentenregister
- `verkehrsowi-anhoerung-bussgeldbescheid` - Anhörung und Bußgeldbescheid prüfen
- `verkehrsowi-fristen-einspruch` - Fristen und Einspruch
- `verkehrsowi-verjaehrung-zustellung` - Verjährung und Zustellung
- `verkehrsowi-akteneinsicht-messakte` - Akteneinsicht und Messakte
- `verkehrsowi-messverfahren-geschwindigkeit` - Geschwindigkeitsmessung
- `verkehrsowi-rotlicht-abstand-handy` - Rotlicht, Abstand und Handy
- `verkehrsowi-alkohol-drogen-24a` - Alkohol und Drogen nach § 24a StVG
- `verkehrsowi-fahreridentifizierung` - Fahreridentifizierung
- `verkehrsowi-punkte-fahrverbot-flensburg` - Punkte, Fahrverbot und Flensburg
- `verkehrsowi-haertefall-fahrverbot` - Härtefall beim Fahrverbot
- `verkehrsowi-beweisverwertung-standardisiert` - Beweisverwertung und Standardisierung
- `verkehrsowi-zeugen-polizei-strategie` - Zeugen- und Polizeibefragung
- `verkehrsowi-hauptverhandlung-amtsgericht` - Hauptverhandlung vor dem Amtsgericht
- `verkehrsowi-rechtsbeschwerde` - Rechtsbeschwerde
- `verkehrsowi-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `verkehrsowi-mandantenkommunikation` - Mandantenkommunikation
- `verkehrsowi-simulation-training` - Simulation und Training
- `verkehrsowi-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/verkehrsowi-mandatskarte.md` - VerkehrsOWi-Mandatskarte
- `assets/templates/frist-und-verjaehrung.md` - Fristen- und Verjährungsblatt
- `assets/templates/anhoerungsbogen-check.md` - Anhörungsbogen-Check
- `assets/templates/bussgeldbescheid-pruefung.md` - Bußgeldbescheid-Prüfung
- `assets/templates/einspruch-owig-67.md` - Einspruch nach § 67 OWiG
- `assets/templates/akteneinsicht-messakte.md` - Akteneinsicht und Messakte
- `assets/templates/messverfahren-checkliste.md` - Messverfahren-Checkliste
- `assets/templates/fahreridentifizierung.md` - Fahreridentifizierung
- `assets/templates/punkte-fahrverbot-matrix.md` - Punkte- und Fahrverbotsmatrix
- `assets/templates/haertefall-fahrverbot.md` - Härtefallpaket Fahrverbot
- `assets/templates/zeugen-polizei-fragenkatalog.md` - Zeugen- und Polizeifragen
- `assets/templates/hauptverhandlung-amtsgericht.md` - Hauptverhandlung Amtsgericht
- `assets/templates/rechtsbeschwerde-check.md` - Rechtsbeschwerde-Check
- `assets/templates/rechtsprechungsrecherche.md` - Rechtsprechungsrecherche
- `assets/templates/mandantenanschreiben.md` - Mandantenanschreiben
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Arbeitsakte

Zum Arbeiten liegt die Akte unter `testakten/verkehrsowi-rotlicht-tempo`. Sie wird im Release als `testakte-verkehrsowi-rotlicht-tempo.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abstand-quellenkarte` | Abstand Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `akteneinsicht-internationaler-bezug-und-schnittstellen` | Akteneinsicht: Internationaler Bezug und Schnittstellen im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi... |
| `alkohol-compliance-dokumentation-und-akte` | Alkohol: Compliance-Dokumentation und Aktenvermerk im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Verte... |
| `alkohol-drogen-beweisverwertung` | Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis THC/Kokain/Amphetamin), § 81a StPO (B... |
| `amtsgericht-drogen-interessen-einspruch` | Amtsgericht: Mandantenkommunikation und Entscheidungsvorlage im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehr... |
| `anhoerung-verkehrsowi-einspruch-messverfahren` | Anhörung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Ver... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `bussgeldbescheid-tatbestand-beweis-und-belege` | Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Ve... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `drogen-mehrparteien-konflikt-und-interessen` | Drogen: Mehrparteienkonflikt und Interessenmatrix im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Vertei... |
| `einspruch-dokumentenmatrix-und-lueckenliste` | Einspruch: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrso... |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fahrverbot-geschwindigkeit-handy` | Fahrverbot: Behörden-, Gerichts- oder Registerweg im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Vertei... |
| `geschwindigkeit-verhandlung-vergleich-und-eskalation` | Geschwindigkeit: Verhandlung, Vergleich und Eskalation im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi V... |
| `handy-zahlen-schwellen-und-berechnung` | Handy: Zahlen, Schwellenwerte und Berechnung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Verteidiger... |
| `hauptverhandlung-sonderfall-messakte-messung` | Hauptverhandlung: Sonderfall und Edge-Case-Prüfung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Verte... |
| `mandantenkommunikation` | Mandantenkommunikation im OWi-Mandat: Mandant versteht Verfahren nicht und benoetigt verstaendliche Erklärung. Normen: BRAO § 43a (Beratungspflicht), § 67 OWiG, § 25 StVG. Prüfraster: Erstgespraeche-Leitfaden, Anhörungsbogen-Empfehlung,... |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtspr... |
| `messakte-formular-portal-und-einreichung` | Messakte: Formular, Portal und Einreichungslogik im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Verteid... |
| `messung-fahrverbot-punkte` | Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Verkehrsowi Verteidiger: prüft konkret die einschlägi... |
| `output-waehlen` | Output wählen im Plugin Verkehrsowi Verteidiger: Diese Output-Weiche für Verkehrsowi Verteidiger entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `punkte-rotlicht-verkehrsowi` | Punkte: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrs... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rotlicht-schriftsatz-brief-und-memo-bausteine` | Rotlicht: Schriftsatz-, Brief- und Memo-Bausteine im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi Vertei... |
| `simulation-training-verjaehrung-zustellung` | Simulationstraining für OWi-Mandate. Uebungsszenarien Messverfahren Rotlicht Handy Alkohol Fahreridentifizierung. Rollenspiel Mandantengespraeche Hauptverhandlung. Fallvarianten mit Erwartungshorizont. Training ohne echte Mandatsdaten im... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Verkehrsowi Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verkehrsowi-aktenanlage` | Akte im Verkehrs-OWi-Mandat anlegen und strukturieren: Neues Mandat Bußgeldbescheid oder Fahrverbot-Drohung. Normen: § 46 OWiG i.V.m. StPO, § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch). Prüfraster: Bußgeldbescheid, Me... |
| `verkehrsowi-akteneinsicht-messakte` | Prüfungslinie für verkehrsowi akteneinsicht messakte: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Verkehrsowi Verteidiger: prüft konkret die... |
| `verkehrsowi-anhoerung-bussgeldbescheid` | Anhörung vor Bußgeldbescheid und Reaktion auf Bußgeldbescheid: Mandant hat Anhörungsbogen oder Bußgeldbescheid erhalten. Normen: § 55 OWiG (Anhörung, Schweigerecht), § 66 OWiG (Pflichtinhalt Bußgeldbescheid), § 67 OWiG (Einspruch 2-Woche... |
| `verkehrsowi-beweisverwertung-standardisiert` | Prüfungslinie für verkehrsowi beweisverwertung standardisiert: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Verkehrsowi Verteidiger: prüft ko... |
| `verkehrsowi-erstpruefung-und-mandatsziel` | Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrsowi... |
| `verkehrsowi-fahreridentifizierung` | Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG (Aussageverweigerungsre... |
| `verkehrsowi-fristen-einspruch` | Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), §... |
| `verkehrsowi-haertefall-fahrverbot` | Haertefall-Argumentation gegen Fahrverbot nach § 25 StVG: Mandant ist beruflich auf Führerschein angewiesen. Normen: § 25 StVG (Fahrverbot), § 25 Abs. 2a StVG (Wirkungszeitpunkt verschiebbar), § 17 Abs. 3 OWiG (Geldbusse erhoehen als Alt... |
| `verkehrsowi-hauptverhandlung-amtsgericht` | Hauptverhandlung in OWi-Sache am Amtsgericht vorbereiten und führen: Termin nach Einspruch gegen Bußgeldbescheid. Normen: § 71 OWiG (HV nach StPO), § 77 OWiG (Beweisanträge), § 55 OWiG (Schweigerecht), § 17 OWiG (Strafmass). Prüfraster:... |
| `verkehrsowi-kommandocenter` | Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-R... |
| `verkehrsowi-messverfahren-geschwindigkeit` | Prüfungslinie für verkehrsowi messverfahren geschwindigkeit: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Verkehrsowi Verteidiger: prüft konk... |
| `verkehrsowi-punkte-fahrverbot` | Punkte im Fahreignungsregister (FAER) Flensburg und Fahrverbot § 25 StVG: Mandant hat Punktewarnung erhalten oder Führerscheinentzug droht. Normen: § 4 StVG (Punktesystem: Warnung 4 Pkt, Verwarnung 6 Pkt, Entzug 8 Pkt), § 65 StVG (Tilgun... |
| `verkehrsowi-quality-gate` | Quality-Gate-Checkliste OWi-Mandat: Vor Einspruch, nach Akteneingang und vor HV prüft Kanzlei Vollständigkeit. Normen: § 67 OWiG (Einspruch), § 77 OWiG (HV-Beweisanträge), BVerfG Rohmessdaten. Prüfraster: Messakte vollständig, Rohmessdat... |
| `verkehrsowi-rechtsbeschwerde` | Rechtsbeschwerde im OWi-Verfahren nach § 79 OWiG einlegen: AG hat OWi-Urteil gesprochen und Mandant will Rechtsbeschwerde. Normen: § 79 OWiG (Zulassigkeit: Geldbusse über 250 EUR oder Fahrverbot), § 80 OWiG (Zulassungsbeschwerde), § 344... |
| `verkehrsowi-rechtsprechungsrecherche` | Rechtsprechungsrecherche für OWi-Verkehrsmandate: Anwalt sucht OLG-Entscheidungen zu Messverfahren, Rohmessdaten und Fahrverbot. Normen: §§ 24 StVG, 25 StVG, 4 StVG; OWiG §§ 67 und 79 und 80. Prüfraster: OLG-Datenbanken (amtliche oder fr... |
| `verkehrsowi-rotlicht-abstand-handy` | Rotlicht-OWi, Abstand-OWi und Handy-OWi verteidigen: Mandant hat Bußgeldbescheid wegen Rotlicht, zu geringem Abstand oder Handynutzung erhalten. Normen: § 37 StVO (Rotlicht: einfach vs. qualifiziert 1 Sekunde), § 4 StVO (Abstand-Berechnu... |
| `verkehrsowi-verjaehrung-zustellung` | Verfolgungsverjährung im OWi-Verfahren prüfen: Anwalt will Verjährungseinwand erheben. Normen: § 26 StVG i.V.m. § 31 OWiG (Verjährungsfrist 3 Monate nach Tatende), § 33 OWiG (Unterbrechungshandlungen), absolute Verjährung 6 Monate. Prüfr... |
| `verkehrsowi-zeugen-polizei-strategie` | Zeugen-Strategie gegenüber Polizeibeamten im OWi-Verfahren: Polizeibeamter als einziger Zeuge in der HV. Normen: § 240 StPO i.V.m. § 71 OWiG (Fragerecht), §§ 373 ff. StPO (Zeugenvernehmung). Prüfraster: Aussage-Konstanz (Protokoll vs. HV... |
| `verteidiger-beweislast-verkehrsowi` | Verteidiger: Beweislast, Darlegungslast und Substantiierung im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Verkehrs... |
| `vowi-akteneinsicht` | Vowi Akteneinsicht im Plugin Verkehrsowi Verteidiger im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nä... |
| `vowi-bussgeldbescheid-verkehrsowi-quality` | Bauleiter Pruefung Bussgeldbescheid OWiG: Tatvorwurf, Beweismittel, Hoehe, Rechtsfolgen Punkte und Fahrverbot. Pruefraster für Verteidiger im Erstgespraech im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale,... |
| `vowi-handyverstoss-akteneinsicht-alkohol` | Spezialfall Handy- und Geraeteverstoss § 23 Abs. 1a StVO: erfasste Geraete, Halten, Nutzen, Abgrenzung Sprachsteuerung. Pruefraster für Verteidiger im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen,... |
| `vowi-tempomessverfahren-bussgeldbescheid` | Spezialfall Tempomessverfahren und Fehlerquellen: Poliscan, ES 3.0, ES 8.0, Riegl, Eichschein, Verkehrsfehlergrenzen. Pruefraster für Verteidiger und Sachverstaendiger im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestan... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung.... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lie... |
| `zeugenstrategie-fehlerkatalog` | Zeugenstrategie Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
