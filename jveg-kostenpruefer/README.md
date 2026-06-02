# JVEG-Kostenprüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`jveg-kostenpruefer`) | [`jveg-kostenpruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jveg-kostenpruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte JVEG Zeugenentschädigung – Dr. Sophia Berger / LG Tübingen** (`jveg-zeugin-berger-lg-tuebingen`) | [Gesamt-PDF lesen](../testakten/jveg-zeugin-berger-lg-tuebingen/gesamt-pdf/jveg-zeugin-berger-lg-tuebingen_gesamt.pdf) | [`testakte-jveg-zeugin-berger-lg-tuebingen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-jveg-zeugin-berger-lg-tuebingen.zip) |
| **Akte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH** (`sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`) | [Gesamt-PDF lesen](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin zur Prüfung von Kosten, Vorschüssen, Entschädigungen und Vergütungen nach dem Justizvergütungs- und -entschädigungsgesetz. Es ist auf echte Aktenarbeit zugeschnitten: Unterlagen strippen, Anspruchsart erkennen, JVEG-Positionen rechnen, Belege prüfen, Gerichtsschreiben angreifen oder bestätigen und am Ende ein belastbares Schreiben samt Rechenprotokoll erzeugen.

Die Beispielakte enthält den Fall der Zeugin Sophia Berger vor dem Landgericht Tübingen, Az. 7 O 118/23, mit Vorschussantrag, Gerichtsschreiben, anwaltlichem Schriftsatz und Word-Abschrift.

## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **sachverstaendigengutachten ki vorwurf lg regensburg sieglinger** | [testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## Direkt herunterladen

- [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jveg-kostenpruefer.zip)
- [JVEG-Beispielakte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-jveg-zeugin-berger-lg-tuebingen.zip)
- [Vorschau lokal öffnen](./assets/vorschau/index.html)

## Was das Plugin prüft

- Vorschuss nach § 3 JVEG
- Geltendmachung, Erlöschen, Wiedereinsetzung und Verjährung
- Fahrtkosten nach § 5 JVEG
- Tagegeld und Übernachtung nach § 6 JVEG
- sonstige notwendige Aufwendungen nach § 7 JVEG
- Zeugenentschädigung nach §§ 19 bis 22 JVEG
- Sachverständigen-, Dolmetscher- und Übersetzervergütung
- Kürzungs- und Wegfallrisiken nach § 8a JVEG
- Festsetzungs-, Beschwerde- und Ergänzungsschreiben

## Grundworkflow

1. Akte hochladen: Ladung, Antrag, Gerichtsschreiben, Belege, Rechnung oder Schriftsatz.
2. Rolle bestimmen: Zeuge, Sachverständiger, Dolmetscher, Übersetzer, Dritter oder ehrenamtlicher Richter.
3. Frist und Belehrung prüfen.
4. Jede Kostenposition mit Norm, Beleg und Rechenweg erfassen.
5. Kappungen und Doppelposten prüfen.
6. Beleglücken freundlich als Rückfragen ausgeben.
7. Rechenblatt, Prüfbericht und passendes Gerichtsschreiben erzeugen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| jveg-kommandocenter | Startet die JVEG-Kostenprüfung, trennt Rolle, Anspruchsart, Frist, Belege, Rechenweg und gewünschten Output. |
| jveg-aktenstripper | Liest Gerichtsschreiben, Anträge, Rechnungen, Belege und Kostenfestsetzungsunterlagen in eine prüfbare JVEG-Datenmatrix aus. |
| jveg-anspruchsberechtigung | Kläert, ob Zeuge, Dritter, Sachverständiger, Dolmetscher, Übersetzer, Protokollperson oder ehrenamtlicher Richter betroffen ist. |
| jveg-fristen-erloeschen | Prüft Geltendmachung, Drei-Monats-Frist, Belehrung, Wiedereinsetzung, Verjährung und sichere Fristennotizen. |
| jveg-vorschuss | Prüft Vorschussanträge nach § 3 JVEG mit Schwerpunkt erhebliche Fahrtkosten, Übernachtung und Teilleistungen. |
| jveg-zeugenentschaedigung | Rechnet und plausibilisiert Zeugenentschädigung nach §§ 19 bis 22 JVEG. |
| jveg-fahrtkosten | Prüft Bahn, Flug, eigenes Kfz, Kilometerpauschale, Parkkosten, Auslandsanreise und Wirtschaftlichkeit. |
| jveg-uebernachtung-aufwand | Prüft Tagegeld, notwendige Übernachtung, BRKG-Anknüpfung, Belege und gerichtliche Obergrenzen. |
| jveg-verdienstausfall-haushalt-zeit | Trennt Verdienstausfall, Haushaltsführungsnachteile und Zeitversäumnis, damit keine Doppelberechnung entsteht. |
| jveg-sonstige-aufwendungen-belege | Prüft sonstige notwendige bare Auslagen, Begleitpersonen, Vertretung, Kopien, Dateien und Belegfähigkeit. |
| jveg-sachverstaendigenrechnung | Prüft Sachverständigenvergütung: Honorargruppe, erforderliche Zeit, Reisezeit, Nebenkosten, § 8a-Risiken und Vorschussüberlauf. |
| jveg-dolmetscher-uebersetzer | Prüft Dolmetscher- und Übersetzervergütung, Stundensatz, Zeilen-/Textumfang, Reisezeiten und Sprach-/Terminlogik. |
| jveg-kuerzung-wegfall-8a | Findet Kürzungs- und Wegfallrisiken: Verwertbarkeit, Hinweisobliegenheit, Befangenheit, Vorschussüberschreitung und Mängel. |
| jveg-gerichtsschreiben-pruefung | Prüft Gerichtsschreiben und Kostenbeamtenargumente auf Tatbestandsfehler, Ermessensfehler, Beleganforderungen und Antwortbedarf. |
| jveg-rechenblatt | Erstellt ein prüfbares Rechenblatt mit Norm, Eingabewert, Kappung, Beleg, Rechenschritt und Ergebnis. |
| jveg-antragsgenerator | Erzeugt Vorschuss-, Nachzahlungs-, Festsetzungs- und Ergänzungsschreiben mit Anlagen- und Belegliste. |
| jveg-festsetzung-beschwerde | Führt durch gerichtliche Festsetzung, Erinnerung/Beschwerdeprüfung, Beschwer, Frist und knappe Angriffsmittel. |
| jveg-quality-gate | Letzte Prüfung vor Versand: Normstand, Mathematik, Belege, keine Doppelposten, Fristen, Ton und eindeutiger Antrag. |

## Beispiel Berger

Die Beispielakte bildet einen realistisch aussehenden Vorschussstreit ab: Barcelona nach Tübingen, 2.500 km Hin- und Rückfahrt, zwei Übernachtungen, geltend gemachter Verdienstausfall und gerichtliche Ablehnung des Vorschusses wegen angeblich fehlender Bedürftigkeit. Das Plugin markiert insbesondere, dass § 3 JVEG bei erheblichen Fahrtkosten und sonstigen Aufwendungen ansetzt und die Kostenpositionen getrennt nach Erstattungsfähigkeit, Vorschussfähigkeit und Belegstatus geprüft werden müssen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im JVEG Kostenpruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `jveg-aktenstripper` | JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz für Kostenprüfung... |
| `jveg-anspruchsberechtigung` | Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis Anspruchsberechtigung JVEG. Abgrenz... |
| `jveg-antragsgenerator` | Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nic... |
| `jveg-dolmetscher-uebersetzer` | Verguetung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output: Verguetungsberechnung D... |
| `jveg-dolmetscher-uebersetzer-spezial` | Spezialfall Dolmetscher- und Uebersetzerverguetung JVEG: Stundenhonorar, Zeilenhonorar, schwierige Texte, Eilauftraege. Pruefraster Auftragsannahme. |
| `jveg-fahrtkosten` | Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Übernacht... |
| `jveg-festsetzung-beschwerde` | Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output: Beschwerdeschrift JVEG. Abgrenzung:... |
| `jveg-fristen-erloeschen` | Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung. Abgrenzung: nicht... |
| `jveg-gerichtsschreiben-pruefung` | Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben gegen JVEG-Kuerzung.... |
| `jveg-kommandocenter` | Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis... |
| `jveg-kuerzung-wegfall-8a` | Kuerzung oder Wegfall der JVEG-Verguetung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit Begründung. Abgrenz... |
| `jveg-quality-gate` | Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht JVEG. Abgrenzung:... |
| `jveg-rechenblatt` | JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgr... |
| `jveg-sachverstaendigenrechnung` | Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte Sachverständigenrechnung. A... |
| `jveg-sachverstaendigenrechnung-bauleiter` | Bauleiter Sachverstaendigenrechnung JVEG: Honorargruppen, Zeitaufwand, Auslagen, Mehrwertsteuer. Pruefraster Sachverstaendiger und Kostenfestsetzung. |
| `jveg-sonstige-aufwendungen-belege` | Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Hoehe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG. Abgrenzung: nicht Fahr... |
| `jveg-uebernachtung-aufwand` | Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output: Übernachtungskosten-Nachweis JVEG. Abgrenzung... |
| `jveg-verdienstausfall-haushalt-zeit` | Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output: Verdienstausfall-Berechnung... |
| `jveg-vorschuss` | Vorschuss auf JVEG-Verguetung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung: nicht Kostenfestsetzu... |
| `jveg-vorschuss-kostenrisiko-spezial` | Spezialfall Vorschuss und Kostenrisiko § 17 JVEG: Vorschussverlangen Sachverstaendiger, Verzicht des Gerichts, Folgen bei Nichteinzahlung. Pruefraster fuer Verfahrensbeteiligte. |
| `jveg-zeugenentschaedigung` | Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Prüfraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung. Abgrenzung: nicht Sach... |
| `jveg-zeugenentschaedigung-checkliste` | Checkliste Zeugenentschaedigung JVEG: Verdienstausfall, Fahrtkosten, Aufwandsentschaedigung, Kinderbetreuung. Pruefraster fuer Zeuge und Geschaeftsstelle. |
| `pruefung-sachverstaendigengutachten-ki-deklaration` | KI-Deklaration in Sachverständigengutachten prüfen: Hat der Sachverständige KI-Nutzung offengelegt? Normen: §§ 404 ff. ZPO, JVEG. Prüfraster: Deklarationspflicht, Methodentransparenz, Beeinflussung des Gutachtenwertes. Output: Prüfergebn... |
| `spezial-belegfeste-formular-portal-und-einreichung` | Belegfeste: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-beschwerde-internationaler-bezug-und-schnittstellen` | Beschwerde: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-dolmetscher-sonderfall-und-edge-case` | Dolmetscher: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-dolmetscherkosten-zahlen-schwellen-und-berechnung` | Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fahrtkosten-behoerden-gericht-und-registerweg` | Fahrtkosten: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-festsetzung-mehrparteien-konflikt-und-interessen` | Festsetzung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-freistehender-erstpruefung-und-mandatsziel` | Freistehender: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fristen-compliance-dokumentation-und-akte` | Fristen: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gate-beweislast-und-darlegungslast` | Gate: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-jveg-tatbestand-beweis-und-belege` | JVEG: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kostenfestsetzung-belege-und-fristen` | Kostenfestsetzung mit Belegen, Fristen und Erinnerung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-kostenpruefer-fristen-form-und-zustaendigkeit` | Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-quality-mandantenkommunikation-entscheidungsvorlage` | Quality: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechenprotokolle-red-team-und-qualitaetskontrolle` | Rechenprotokolle: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sachverstaendigen-livequellen-und-rechtsprechungscheck` | Sachverstaendigen: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-uebernachtung-schriftsatz-brief-und-memo-bausteine` | Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-uebersetzer-fristennotiz-und-naechster-schritt` | Uebersetzer: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verdienstausfall-verhandlung-vergleich-und-eskalation` | Verdienstausfall: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vorschuss-risikoampel-und-gegenargumente` | Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zeugenentschaedigung-dokumentenmatrix-und-lueckenliste` | Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin jveg-kostenpruefer: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin jveg-kostenpruefer: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin jveg-kostenpruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin jveg-kostenpruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin jveg-kostenpruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin jveg-kostenpruefer: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin jveg-kostenpruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin jveg-kostenpruefer: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin jveg-kostenpruefer: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin jveg-kostenpruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
