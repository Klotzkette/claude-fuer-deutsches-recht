# JVEG-Kostenprüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`jveg-kostenpruefer.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/jveg-kostenpruefer.md) (94 KB)
- Im Repo: [`testakten/megaprompts/jveg-kostenpruefer.md`](../testakten/megaprompts/jveg-kostenpruefer.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 53 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenstripper` | JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz für Kostenprüfung... |
| `anschluss-routing` | Anschluss-Routing für JVEG-Kostenprüfer: wählt den nächsten Spezial-Skill nach Engpass (Entschädigungsantrag binnen 3 Monaten, SV-Rechnung, Reisekostenabrechnung, Stundennachweise), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchsberechtigung-antragsgenerator` | Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis Anspruchsberechtigung JVEG. Abgrenz... |
| `antragsgenerator` | Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nic... |
| `belegfeste-formular-portal-und-einreichung` | Belegfeste: Formular, Portal und Einreichungslogik. |
| `beschwerde-dolmetscher-sonderfall` | Beschwerde: Internationaler Bezug und Schnittstellen. |
| `dokumente-intake` | Dokumentenintake für JVEG-Kostenprüfer: sortiert SV-Rechnung, Reisekostenabrechnung, Stundennachweise, prüft Datum, Absender, Frist und Beweiswert (Aktennotizen, Reiseplanung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `dolmetscher-sonderfall-und-edge-case` | Dolmetscher: Sonderfall und Edge-Case-Prüfung. |
| `dolmetscher-uebersetzer` | Vergütung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output: Verguetungsberechnung D... |
| `dolmetscher-uebersetzer-fahrtkosten` | Spezialfall Dolmetscher- und Übersetzerverguetung JVEG: Stundenhonorar, Zeilenhonorar, schwierige Texte, Eilauftraege. Prüfraster Auftragsannahme im Jveg Kostenpruefer. |
| `dolmetscherkosten-zahlen-schwellen-und-berechnung` | Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung. |
| `einstieg-routing` | Einstieg, Triage und Routing für JVEG-Kostenprüfer: ordnet Rolle (Sachverständiger, Gericht, Bezirksrevisor), markiert Frist (Entschädigungsantrag binnen 3 Monaten), wählt Norm (JVEG, ZPO §§ 91 ff.) und Zuständigkeit (Gericht), leitet zu... |
| `fahrtkosten` | Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Übernacht... |
| `fahrtkosten-festsetzung-interessen` | Fahrtkosten: Behörden-, Gerichts- oder Registerweg. |
| `festsetzung-beschwerde` | Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output: Beschwerdeschrift JVEG. Abgrenzung:... |
| `festsetzung-mehrparteien-konflikt-und-interessen` | Festsetzung: Mehrparteienkonflikt und Interessenmatrix. |
| `freistehender-erstpruefung-und-mandatsziel` | Freistehender: Erstprüfung, Rollenklärung und Mandatsziel. |
| `fristen-erloeschen` | Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung. Abgrenzung: nicht... |
| `gate-beweislast-jveg-quality` | Gate: Beweislast, Darlegungslast und Substantiierung. |
| `gate-rechenblatt` | Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht JVEG. Abgrenzung:... |
| `gerichtsschreiben-kuerzung-wegfall` | Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben gegen JVEG-Kuerzung.... |
| `jveg-tatbestand-beweis-und-belege` | JVEG: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `kommandocenter` | Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis... |
| `kostenfestsetzung-belege-und-fristen` | Kostenfestsetzung mit Belegen, Fristen und Erinnerung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Jveg Kostenpruefer. |
| `kostenfestsetzung-kostenpruefer` | Fristen: Compliance-Dokumentation und Aktenvermerk. |
| `kostenpruefer-fristen-form-und-zustaendigkeit` | Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `kuerzung-wegfall-8a` | Kuerzung oder Wegfall der JVEG-Vergütung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit Begründung. Abgrenz... |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Jveg Kostenpruefer. |
| `output-waehlen` | Output-Wahl für JVEG-Kostenprüfer: stimmt Adressat (Sachverständiger, Gericht, Bezirksrevisor), Frist (Entschädigungsantrag binnen 3 Monaten) und Form auf den Zweck ab — typische Outputs: JVEG-Prüfung, Erinnerung gegen Festsetzung, Besch... |
| `pruefung-sachverstaendigengutachten-ki-deklaration` | KI-Deklaration in Sachverständigengutachten prüfen: Hat der Sachverständige KI-Nutzung offengelegt? Normen: §§ 404 ff. ZPO, JVEG. Prüfraster: Deklarationspflicht, Methodentransparenz, Beeinflussung des Gutachtenwertes. Output: Prüfergebn... |
| `quality-mandantenkommunikation-entscheidungsvorlage` | Quality: Mandantenkommunikation und Entscheidungsvorlage. |
| `quellen-livecheck` | Quellen-Live-Check für JVEG-Kostenprüfer: prüft Normen (JVEG, ZPO §§ 91 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Gericht und Quellenhygiene nach references/quellenhygiene.md. |
| `rechenblatt` | JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgr... |
| `rechenprotokolle-fehlerkatalog` | Rechenprotokolle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `sachverstaendigen-quellenkarte` | Sachverstaendigen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `sachverstaendigenrechnung` | Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte Sachverständigenrechnung. A... |
| `sachverstaendigenrechnung-bauleiter` | Bauleiter Sachverstaendigenrechnung JVEG: Honorargruppen, Zeitaufwand, Auslagen, Mehrwertsteuer. Prüfraster Sachverstaendiger und Kostenfestsetzung im Jveg Kostenpruefer. |
| `sonstige-aufwendungen-uebernachtung` | Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Höhe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG. Abgrenzung: nicht Fahr... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im JVEG Kostenpruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Doku... |
| `uebernachtung-aufwand` | Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output: Übernachtungskosten-Nachweis JVEG. Abgrenzung... |
| `uebernachtung-verdienstausfall-vorschuss` | Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine. |
| `uebersetzer-fristennotiz-jveg` | Übersetzer: Fristennotiz und nächster Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für JVEG-Kostenprüfer: trennt fehlende Tatsachen von fehlenden Belegen (SV-Rechnung, Reisekostenabrechnung, Stundennachweise), nennt pro Lücke Beweisthema, Beschaffungsweg (Gericht), Frist und Ersatznachweis. |
| `verdienstausfall-haushalt-zeit` | Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output: Verdienstausfall-Berechnung... |
| `verdienstausfall-verhandlung-vergleich-und-eskalation` | Verdienstausfall: Verhandlung, Vergleich und Eskalation. |
| `vorschuss-kostenrisiko` | Vorschuss auf JVEG-Vergütung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung: nicht Kostenfestsetzu... |
| `vorschuss-kostenrisiko-spezial` | Spezialfall Vorschuss und Kostenrisiko § 17 JVEG: Vorschussverlangen Sachverstaendiger, Verzicht des Gerichts, Folgen bei Nichteinzahlung. Prüfraster für Verfahrensbeteiligte im Jveg Kostenpruefer. |
| `vorschuss-risikoampel-und-gegenargumente` | Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Jveg Kostenpruefer. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Jveg Kostenpruefer. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Jveg Kostenpruefer. |
| `zeugenentschaedigung` | Checkliste Zeugenentschaedigung JVEG: Verdienstausfall, Fahrtkosten, Aufwandsentschaedigung, Kinderbetreuung. Prüfraster für Zeuge und Geschäftsstelle im Jveg Kostenpruefer. |
| `zeugenentschaedigung-dokumentenmatrix-und-lueckenliste` | Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung: Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
