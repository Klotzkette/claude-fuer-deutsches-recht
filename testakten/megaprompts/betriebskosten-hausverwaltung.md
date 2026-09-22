# Vollprüfung: betriebskosten-hausverwaltung

## Zusammensetzung

Diese Vollprüfung enthält alle 10 Skills des Plugins `betriebskosten-hausverwaltung`.

## Inhaltsverzeichnis

1. **abrechnung-vorauszahlungen-und-fristen-abschliessen** — Fuehrt gepruefte Kostenanteile und tatsaechliche Vorauszahlungen zum Mietsaldo zusammen, prueft Zugang und Ausschlussfri…
2. **belege-bis-zur-abrechnung** — Erstellt aus Rechnungen, Zahlungen, Verbrauchsdaten und Mietvertrag eine nachrechenbare Betriebskostenabrechnung fuer Mi…
3. **einwendungen-korrektur-und-belegeinsicht-bearbeiten** — Prueft konkrete Einwendungen gegen Betriebskosten, organisiert elektronische Belegeinsicht einschliesslich Zahlungen und…
4. **grundsteuer-und-energie-sonderkosten-trennen** — Prueft Grundsteuerbescheide fuer die Mietumlage, trennt Allgemeinstrom von PV, Mieterstrom und Wallbox und erstellt eine…
5. **kosten-und-hausmeister-abgrenzen** — Prueft Betriebskosten und gemischte Hausmeisterleistungen anhand von Vertrag, Rechnung und Taetigkeitsnachweisen und zie…
6. **co2-kosten-belegt-aufteilen** — Ermittelt CO2-Kosten aus verbrauchten Brennstoffschichten, prueft Wohngebaeudestufe und Vermieterabzug und erstellt den …
7. **weg-kosten-in-mietabrechnung-ueberleiten** — Ueberfuehrt WEG-Gesamt- und Einzelabrechnung in die Mietabrechnung einer Eigentumswohnung, prueft den Schluessel nach Pa…
8. **belege-und-zahlungen-abgleichen** — Ordnet Rechnungen, Abschlaege, Gutschriften und Zahlungsbelege einer Betriebskostenperiode zu und erstellt ein abgestimm…
9. **oel-heizung-und-warmwasser-abrechnen** — Rekonstruiert Oelbestand und Verbrauchskosten, trennt Heizung und Warmwasser und rechnet Grund- und Verbrauchsanteile na…
10. **flaechen-und-umlageschluessel-pruefen** — Prueft Wohnflaechen, Verbrauchs- und WEG-Schluessel sowie Leerstand und Nutzerwechsel und berechnet die belegten Anteile…

---

## Skill: `abrechnung-vorauszahlungen-und-fristen-abschliessen`

_Fuehrt gepruefte Kostenanteile und tatsaechliche Vorauszahlungen zum Mietsaldo zusammen, prueft Zugang und Ausschlussfristen und entwirft die Abrechnung sowie eine begruendete Anpassung nach Paragraf 560 BGB._

# Abrechnung, Vorauszahlungen und Fristen abschließen

## 1. Zweck und Anwendungsfall

Liefere die fertige Betriebskostenabrechnung, nicht nur eine Liste der erforderlichen Bestandteile. Trenne ihre rechnerische Richtigkeit von Fristwahrung, Fälligkeit und einer möglichen Vorauszahlungsanpassung.

## 2. Eingaben

Lies die geprüften Kosten- und Verteilungstabellen, Heizkostenanlage, Mietvertrag, vollständiges Vorauszahlungsjournal und vorhandene Abrechnungsfassungen samt Zugangsnachweisen. Stelle Abrechnungsjahr, Nutzungszeitraum, Erstellungsdatum und Zugang nicht gleich. Frage nur nach den fehlenden Zahlen oder Zugangsdaten, die Saldo oder Rechtsfolge bestimmen.

## 3. Ablauf / Checkliste

### 3.1. Stelle die Rechnung nachvollziehbar zusammen.

Führe je Kostenart Gesamtkosten, erkennbare Bereinigung, Verteilungsschlüssel mit Bezugswerten und den berechneten Mieteranteil auf. Zeige den Zeitraum und gegebenenfalls Nutzerwechsel. Prüfe Heizkostenanlage und CO2-Ausweis auf Übereinstimmung mit der Hauptrechnung. Addiere die Mieteranteile ohne pauschale Sicherheitszuschläge. Die Kontrollsumme aus Mietern, Leerstand und Eigentümeranteilen muss die verteilte Kostenbasis ergeben.

### 3.2. Stimme Vorauszahlungen und Saldo ab.

Ordne tatsächliche Zahlungseingänge, Rücklastschriften und Gutschriften dem Mietkonto und Zeitraum zu. Trenne Nettomiete, Kaution, Soll-Vorauszahlungen und echte Vorauszahlungen. Rechne Kostenanteil minus geleistete Vorauszahlungen; ein negativer Saldo ist ein Guthaben. Führe noch offene Soll-Vorauszahlungen getrennt und verhindere nach Abrechnungsreife die doppelte Forderung von Rückstand und demselben Jahresfehlbetrag. Raten auf einen bereits abgerechneten Saldo mindern diesen, nicht nochmals die Vorauszahlungssumme. Rechne intern mit ausreichender Genauigkeit und dokumentiere Cent-Rundungen.

### 3.3. Prüfe Zugang und Fristen.

Paragraf 556 Absatz 3 BGB verlangt grundsätzlich Mitteilung bis Ende des zwölften Monats nach Periodenende. Für 01.01. bis 31.12.2025 ist das der 31.12.2026. Das Datum auf dem Brief und sein Versand genügen nicht als Zugangsnachweis. Trenne fehlende formelle Mindestangaben von materiellen Fehlern einzelner Ansätze. Ein Belegmangel macht nicht automatisch die gesamte Abrechnung formell unwirksam.

Nach Fristablauf prüfe den Ausschluss einer Nachforderung und ein konkret belegtes fehlendes Vertretenmüssen; ein Mieterguthaben verschwindet dadurch nicht. Die WEG-Verzögerung ist kein pauschaler Entschuldigungsgrund. Bei einer Korrektur nach Fristablauf prüfe insbesondere eine unzulässige Erhöhung gegenüber der rechtzeitigen Abrechnung. Die Einwendungsfrist des Mieters läuft grundsätzlich zwölf Monate ab Zugang; gesetzliche Ausnahmen und Verjährung sind gesondert zu behandeln. Eine freie Zahlungsfrist im Entwurf wird nicht als gesetzliche Fälligkeitsregel dargestellt.

### 3.4. Passe Vorauszahlungen nur begründet an.

Prüfe nach einer inhaltlich tragfähigen Abrechnung die angemessene künftige Vorauszahlung nach Paragraf 560 Absatz 4 BGB. Erkläre die Änderung in Textform, mit Ausgangsbasis, belegten absehbaren Veränderungen, neuem Monatsbetrag und Wirksamkeitszeitpunkt. Vermeide eine automatische Zehn-Prozent-Reserve. Unterscheide hiervon die Pauschale: Deren Erhöhung setzt eine vertragliche Grundlage und die besonderen Regeln der Absätze 1 und 2 voraus; Ermäßigungen sind nach Absatz 3 weiterzugeben. Eine Pauschale wird nicht nachträglich als Vorauszahlung abgerechnet.

### 3.5. Liefere die Endfassung.

Erstelle die Abrechnung mit eindeutiger Saldoaussage und Belegeinsichtsangebot. Bei entscheidenden Lücken liefere den belegten Stand samt gezielter Anforderung, nicht eine fingierte Endabrechnung. Nach Ergänzung aktualisiere Rechnung und Brief. Versende oder anerkenne nichts ohne Auftrag.

## 4. Quellenpflicht

Nutze die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und das [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md). Prüfe Paragrafen 556 und 560 BGB und die dort verifizierten BGH-Anker zur Abrechnung und WEG-Verzögerung. Übernimm keine gesetzliche Zahlungsfrist oder aktuelle Rechtsprechung aus bloßem Modellwissen.

## 5. Ausgabeformat

Liefere Abrechnung und gegebenenfalls Anpassungserklärung in vollständigen, ausformulierten Sätzen mit prüfbaren Tabellen; Skelette, Halbsätze und reine Aufzählungen sind verboten. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Textausgabe steht ein gesonderter Exporthinweis außerhalb des Briefs. Es werden nur tatsächlich erzeugte Dateien verlinkt.

## 6. Beispiele

Bei 2.400 EUR Jahreskosten und 2.200 EUR tatsächlich gezahlten Vorauszahlungen beträgt der Saldo 200 EUR. Wurden 2.400 EUR geschuldet, werden die darin enthaltenen 200 EUR Vorauszahlungsrückstand nicht zusätzlich zum selben Abrechnungssaldo verlangt. Ohne belegte künftige Änderung ist eine Erhöhung auf 220 EUR monatlich nicht mit einer pauschalen Sicherheitsreserve zu begründen.

---

## Skill: `belege-bis-zur-abrechnung`

_Erstellt aus Rechnungen, Zahlungen, Verbrauchsdaten und Mietvertrag eine nachrechenbare Betriebskostenabrechnung fuer Mietshaus oder vermietete Eigentumswohnung und bei Streit den konkreten Antwortbrief._

# Belege bis zur Abrechnung

## 1. Zweck und Anwendungsfall

Führe vorhandene Belege zur konkreten Mietabrechnung oder zum bestellten Antwortbrief. Rechne selbst; eine Skill-Empfehlung ersetzt das Ergebnis nicht. Unterscheide eigenes Mietshaus und vermietete ETW in einer WEG. Erstelle keine ungefragte Klage.

## 2. Eingaben

Lies zuerst Mietvertrag, Zeitraum, Nutzerliste, Rechnungen, Gutschriften, Zahlungskonto, Flächen, Schlüssel und Heizdaten. Bei Öl lies Anfangs-/Endbestand und Lieferbelege der verbrauchten Vorratsschichten; bei WEG Gesamt-/Einzelabrechnung, geltende Verteilung und Eigentümerbelege. Entnimm Rolle und Produkt dem Auftrag. Frage nur nach entscheidenden, aus den Dateien nicht klärbaren Lücken.

## 3. Ablauf / Checkliste

### 3.1. Baue das Rechenbuch aus Belegen auf.

Erfasse je Belegkennung Quelle/Seite, Kostenart, Leistung, Zeitraum, Bruttorechnung, Gutschrift, Zahlung, Periodenansatz und Umlageentscheidung. Verknüpfe Abschläge mit Schlussrechnungen ohne Doppelansatz. Prüfe Dubletten nach Rechnung und Leistung. Unterscheide unbezahlte Rechnung und fehlenden Zahlungsnachweis. Halte bei kalten Kosten Leistungs- oder zulässiges Abflussprinzip je Kostenart konsistent fest; Heizung folgt dem Verbrauch.

### 3.2. Bereinige die Kostenbasis.

Prüfe Umlagevereinbarung und Paragrafen 1 und 2 BetrKV. Rechne: Periodenkosten minus Gutschriften, Rabatte, Erstattungen und nicht umlagefähige Anteile ergeben den Verteilungstopf. Ziehe Verwaltung, Reparaturen und Rücklagenzuführungen ab. Teile Hausmeisterleistungen nach belegten Tätigkeiten und Zeitanteilen auf, nicht mit erfundenen zehn Prozent. Vermeide doppelte Reinigung, Gartenpflege und Heizstrom. Halte Streitpositionen neben dem gesicherten Stand offen.

### 3.3. Leite Schlüssel und Nutzeranteile her.

Prüfe zwingendes Recht und Mietvertrag. Ohne abweichende Vereinbarung gilt beim Mietshaus Paragraf 556a Absatz 1 BGB, bei vermietetem Wohnungseigentum Absatz 3 mit dem geltenden WEG-Maßstab und der Grenze billigen Ermessens. Die HeizkostenV bleibt vorrangig. Dokumentiere Zähler, Nenner und Einheit. Rechne bei Flächenumlage: Topf mal Wohnungsfläche/Gesamtfläche, gegebenenfalls mal belegtem Nutzungszeitanteil. Leerstand bleibt im Nenner und beim Eigentümer. Verbrauch und Heizungsnutzerwechsel folgen Messdaten und Paragraf 9b HeizkostenV, nicht pauschal Tagen. Verteile WEG-Wohnungsbeträge nicht nochmals mit dem Miteigentumsanteil. Bei abweichendem Mietschlüssel rechne aus dem Gebäudetopf neu.

### 3.4. Berechne Wärme, Warmwasser und CO2.

Rechne Ölverbrauch als Anfangsbestand plus Lieferungen minus Endbestand. Bewerte verbrauchte Schichten mit ihren Anschaffungskosten, begründe die Verbrauchsfolge und führe den Restwert fort. FIFO braucht nachvollziehbare Vorratsfortschreibung. Jahreskäufe sind nicht Jahresverbrauch. Prüfe Heiznebenkosten und trenne verbundene Anlagen nach Paragraf 9 HeizkostenV zuerst in Heizung und Warmwasser; Wasser darf nicht doppelt erscheinen.

Im Regelfall sind nach Paragrafen 7 und 8 HeizkostenV 50 bis 70 Prozent verbrauchsabhängig zu verteilen. Die 70-Prozent-Pflicht für Heizung setzt kumulativ ein Gebäude unter dem Niveau der Wärmeschutzverordnung vom 16.08.1994, Öl- oder Gasheizung und überwiegend gedämmte freiliegende Wärmeverteilungsleitungen voraus. Prüfe Ausnahmen und Paragraf 10, statt allein wegen Altbau 70 Prozent anzusetzen. Rechne je Topf: Verbrauchsanteil mal Nutzerverbrauch/Gesamtverbrauch plus Grundanteil mal passende Nutzerfläche/Gesamtfläche.

Ermittle CO2-Menge und enthaltene CO2-Kosten der verbrauchten Lieferanteile mit deren jeweiligen Lieferdaten, Emissionsfaktoren und Kosten. Übertrage keinen einheitlichen Preis von 2025 auf Vorrat aus 2024. Vor 2023 in Rechnung gestellte Mengen unterliegen der Übergangsregel in Paragraf 11 Absatz 2 CO2KostAufG. Bestimme für Wohngebäude kg CO2 je maßgeblichem Quadratmeter und Jahr, runde gesetzlich auf eine Nachkommastelle und ordne die Stufe zu. Ziehe den Vermieteranteil genau einmal vor der Mieterumlage ab und weise Stufe, Grundlagen und Mieteranteil aus. Für 2025 gilt damaliges Recht, keine spätere Normänderung. Fehlende Verbrauchsdaten lösen die Prüfung der gesetzlichen Ersatzverfahren aus, keine erfundenen Messwerte.

### 3.5. Führe die Abrechnung zusammen.

Bereinige jede WEG-Zeile; Hausgeld, Abrechnungsspitze und Sonderumlage sind keine Mietkostenarten. Füge die belegte Wohnungsgrundsteuer nur einmal hinzu. Für Berlin 2025 prüfe Jahresbescheid und Korrekturen; 470 Prozent und für Wohngrundstücke 0.31 Promille sind Kontrollwerte, kein Ersatzbeleg. Halte PV-Anschaffung, Mieterstrom und Wallbox getrennt von Allgemein- und Heizstrom. Paragraf 35a EStG dient nur dem belegten Arbeitskostenausweis, keiner Steuerberechnung.

Addiere die Kostenanteile je Mieter und ziehe die tatsächlich geleisteten, zugeordneten Vorauszahlungen ab. Halte Soll-Vorauszahlungen und Rückstände getrennt, damit nichts doppelt verlangt wird. Runde erst an ausgewiesenen Endpositionen auf Cent und erkläre einen Rundungsrest. Kontrolliere: Mieteranteile plus Eigentümer-/Leerstandsanteile ergeben den bereinigten Topf. Prüfe Abrechnungszeitraum, Gesamtkosten, Schlüssel, Einzelanteil und Vorauszahlungsabzug auf Verständlichkeit. Für das Kalenderjahr 2025 muss die Abrechnung grundsätzlich bis 31.12.2026 zugehen. Eine ausstehende WEG-Beschlussfassung verlängert die Frist nicht automatisch.

### 3.6. Schließe den Vorgang ab.

Liefere Abrechnung mit Saldo und Belegeinsichtsangebot oder den bestellten Antwortbrief mit korrigierter Rechnung. Paragraf 556 Absatz 4 BGB erlaubt elektronische Belege; alte Originalbelegurteile begründen keinen pauschalen Papierzwang. Prüfe Vollständigkeit, Lesbarkeit, Zahlungen und Gutschriften. Bei entscheidenden Lücken liefere Teilstand und gezielte Anforderung, keine fingierte Endforderung. Rechne nach Eingang die betroffenen Zeilen neu und liefere das Endprodukt ohne neue Gesamtaufnahme. Prüfe Vorauszahlungsanpassung gesondert nach Paragraf 560 Absatz 4 BGB. Versende nichts eigenmächtig.

## 4. Quellenpflicht

Nutze [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md). Trenne Normfassung, Übergangsrecht und Abrufdatum. Belege Rechtsaussagen und Rechengrößen; erfinde keine Urteile oder Literaturstellen.

## 5. Ausgabeformat

Liefere vollständige, ausformulierte Sätze und Rechentabellen; Skelette, Halbsätze und reine Aufzählungen sind als Endprodukt verboten. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung, bei Textausgabe mit getrenntem Exporthinweis. Verlinke nur erzeugte und geprüfte Dateien. Trenne interne Kontrolle vom Empfängertext.

## 6. Beispiele

Bei 12.000 EUR belegten kalten Kosten, 1.200 EUR Abzügen und 80 von 800 Quadratmetern beträgt der ganzjährige Anteil 1.080 EUR. Bei 1.200 EUR geleisteten Vorauszahlungen ergibt sich ein Guthaben von 120 EUR, sofern dies alle abzurechnenden Kosten sind. Eine WEG-Abrechnung mit zusätzlicher Verwaltung und Rücklage wird vor dieser Rechnung bereinigt; sie wird nicht unverändert an den Mieter weitergereicht.

---

## Skill: `einwendungen-korrektur-und-belegeinsicht-bearbeiten`

_Prueft konkrete Einwendungen gegen Betriebskosten, organisiert elektronische Belegeinsicht einschliesslich Zahlungen und Gutschriften und liefert korrigierte Rechnung oder ausformulierten Antwortbrief._

# Einwendungen, Korrektur und Belegeinsicht bearbeiten

## 1. Zweck und Anwendungsfall

Führe einen konkreten Abrechnungsstreit zum begründeten Antwortbrief oder zur korrigierten Abrechnung. Arbeite aus der beauftragten Vermieter- oder Mieterperspektive, ohne berechtigte Gegenargumente zu verschweigen oder ungefragt eine Klage vorzubereiten.

## 2. Eingaben

Lies Abrechnung samt Anlagen, Mietvertrag, Einwendungsschreiben, Zugangsnachweise, angebotene Belege und bisherige Korrespondenz. Nutze bekannte Rechnungen und Berechnungen weiter. Frage nur nach einem fehlenden Beleg oder Zugang, der die konkrete Streitfrage entscheidet.

## 3. Ablauf / Checkliste

### 3.1. Ordne Einwendungen und Fristen zu.

Erfasse betroffene Position, behaupteten Fehler, streitigen Betrag, vorhandenen Gegenbeleg und Zugangsdaten. Trenne Rechenfehler, Umlagefähigkeit, Schlüssel, fehlende Mindestangaben und reine Belegfragen. Prüfe die zwölfmonatige Einwendungsfrist nach Paragraf 556 Absatz 3 BGB und gegebenenfalls fehlendes Vertretenmüssen. Ein Einsichtsverlangen allein ersetzt nicht stets eine konkrete Einwendung und verlängert die Frist nicht automatisch. Erkläre bei Verzögerung, welche Punkte fristwahrend konkret benannt werden können.

### 3.2. Prüfe das tatsächliche Einsichtsangebot.

Paragraf 556 Absatz 4 BGB kodifiziert die Einsicht und gestattet dem Vermieter seit 01.01.2025 elektronische Bereitstellung. Prüfe daher vollständige, lesbare und zugängliche elektronische Rechnungen, Anlagen, Gutschriften und vorhandene Zahlungsbelege. Ein Endbetragsexport ohne Belege erfüllt diese Kontrolle nicht. Prüfe auch die für die Verteilung notwendigen Verbrauchs- und Flächendaten unter zweckgerechtem Datenschutz; schwärze nicht die entscheidenden Prüfinformationen.

BGH, Urteil vom 15.12.2021 - VIII ZR 66/20, betrifft die frühere Rechtslage zum Originalbelegrecht. Es ist kein Beleg für einen heute stets durchsetzbaren Anspruch auf Papieroriginale trotz ordnungsgemäßer elektronischer Bereitstellung. Umgekehrt beseitigt die neue Norm weder das Einsichtsrecht noch die Kontrolle von Authentizität, Lesbarkeit und Vollständigkeit. Bei konkreten Manipulationsindizien oder nicht nutzbarem Zugang kläre die betroffene Datei und eine geeignete Einsichtsform rechtlich und tatsächlich; behaupte weder pauschalen Originalzwang noch eine grenzenlose Befugnis zur Belegvernichtung.

### 3.3. Rechne die streitigen Positionen nach.

Prüfe den Ursprungstopf, Abzüge und Gutschriften, Schlüssel, Nutzeranteil und Vorauszahlungen. Erstelle eine Alt-Neu-Rechnung nur für die betroffenen Positionen und aktualisiere den Gesamtsaldo. Nenne, welche Einwendungen anerkannt, teilweise berechtigt oder belegbar zurückzuweisen sind. Prüfe für eine nachträgliche Erhöhung gesondert die Abrechnungsfrist; eine Korrektur zu Gunsten des Mieters wird nicht wegen Fristablaufs pauschal verweigert.

### 3.4. Formuliere eine verhältnismäßige Antwort.

Benenne Betrag, Begründung, konkrete Belege und das tatsächlich mögliche Einsichtsangebot. Bei berechtigt verlangter, noch verweigerter Belegeinsicht prüfe ein zeitweiliges Leistungsverweigerungsrecht hinsichtlich der Nachforderung; empfehle nicht pauschal, sämtliche Miete einzustellen. Prüfe Heizkosten- und CO2-Kürzungen eigenständig, ohne verschiedene Prozentsätze blind zu addieren. Bei entscheidender Lücke liefere das gezielte Anforderungsschreiben und nach Nachreichung den korrigierten Abschluss. Versand, Anerkenntnis, Vergleich, Verzicht oder gerichtliches Vorgehen erfolgen nicht eigenmächtig.

## 4. Quellenpflicht

Beachte die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und das [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md). Prüfe Paragraf 556 Absätze 3 und 4 BGB, BGH, Urteil vom 09.12.2020 - VIII ZR 118/19, Randnummern 12 bis 17, sowie den historischen Anker VIII ZR 66/20 im Licht der Gesetzesänderung. Behaupte keine neue Entscheidung aus 2026 ohne geprüften amtlichen Volltext.

## 5. Ausgabeformat

Liefere den adressatengerechten Brief und erforderlichenfalls eine korrigierte Rechentabelle in vollständigen, ausformulierten Sätzen. Skelette, Halbsätze und reine Aufzählungen sind verboten. Nutze soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Technische Quellenprotokolle und Exporthinweise bei Textausgabe bleiben getrennt. Behaupte keine tatsächlich nicht erzeugten Anhänge.

## 6. Beispiele

Der Mieter verlangt zu 1.200 EUR Hausmeisterkosten die Zahlungsbelege, während bisher nur die Rechnung im Portal liegt. Der Antwortentwurf kündigt nur tatsächlich bereitstellbare Belege an und beantwortet die Kostenfrage anhand der Leistungsanteile. Die elektronische Bereitstellung wird nicht pauschal abgelehnt, die Zahlungseinsicht aber auch nicht mit dem Hinweis auf das Portal verweigert.

---

## Skill: `grundsteuer-und-energie-sonderkosten-trennen`

_Prueft Grundsteuerbescheide fuer die Mietumlage, trennt Allgemeinstrom von PV, Mieterstrom und Wallbox und erstellt einen belegten Arbeitskostenausweis nach Paragraf 35a EStG ohne Steuerberechnung._

# Grundsteuer und Energie-Sonderkosten trennen

## 1. Zweck und Anwendungsfall

Kläre die oft außerhalb der Hauptabrechnung liegenden Grundsteuer-, Energie- und Arbeitskostenbelege. Dieses Arbeitsziel umfasst keine umfassende Grundsteuerbewertung, Stromvertragsgestaltung oder Einkommensteuerberechnung.

## 2. Eingaben

Lies Jahresgrundsteuerbescheid samt Änderungen, Erstattungen und Zahlungskonto, die Mietklausel, Stromrechnungen, Zählerplan, PV- und Wallboxbelege, Mieterstromvertrag sowie aufgeschlüsselte Dienstleistungsrechnungen. Nutze die vorhandenen Nachweise zuerst; frage nur nach der entscheidenden Zuordnung oder Kostentrennung.

## 3. Ablauf / Checkliste

### 3.1. Ordne Grundsteuer dem Objekt und Jahr zu.

Unterscheide Grundsteuerwert, Messbetrag, Jahressteuer und Zahlungen. Umlagegegenstand ist die vereinbarte laufende öffentliche Last nach Paragraf 2 Nummer 1 BetrKV, nicht der Grundsteuerwert oder die Summe von Bescheid und Quartalszahlungen. Prüfe Jahresbescheid, wirtschaftliche Einheit, Zeitraum, Erlass und Änderungsbescheide. Säumniszuschläge und Rechtsbehelfskosten werden nicht als Grundsteuer weitergegeben.

Für Berlin 2025 sind 470 Prozent Hebesatz B und für Wohngrundstücke 0.31 Promille amtlich belegt. Ein bereits festgesetzter Messbetrag wird mit 4.70 multipliziert, nicht nochmals mit der Messzahl. Verwende weder den alten Hebesatz von 810 Prozent noch einen errechneten Schätzbetrag anstelle des konkreten Bescheids. Bei einer eigens veranlagten ETW prüfe die wohnungsbezogene Zuordnung und die Mietvereinbarung; verteile den Wohnungsbetrag nicht nochmals als Gebäudesteuer. Einwendungen gegen einen Wertbescheid werden nicht ungefragt zu einem steuerlichen Rechtsbehelf erweitert.

### 3.2. Trenne vier Energieabrechnungen.

Ordne Strom für gemeinschaftliche Beleuchtung, Heizungsbetrieb, Haushaltslieferung und Fahrzeugladen den tatsächlichen Verbrauchen zu. Nicht jeder Strom im gemeinsamen Zähler ist Allgemeinstrom nach Paragraf 2 Nummer 11 BetrKV. Für fehlende Unterzähler sind nachvollziehbare Abgrenzungsgrundlagen notwendig; Kosten werden nicht willkürlich auf alle Wohnungen verteilt.

PV-Anschaffung, Finanzierung und Reparatur sind keine laufenden Betriebskosten allein wegen Energieerzeugung. Eigenstrom wird nicht ohne nachgewiesene Rechts- und Kostenbasis mit einem fiktiven Netzstromtarif bepreist. Mieterstrom nach Paragraf 42a EnWG wird grundsätzlich über einen getrennten Liefervertrag behandelt; prüfe dessen Anwendungsbereich und Ausnahmen, statt Haushaltsstrom in die Betriebskostenabrechnung zu verschieben. Wallbox-Anschaffung und nutzerspezifisches Laden bleiben ebenfalls getrennt. Ein WEG-Beschluss begründet keine beliebige mietvertragliche Kostenübernahme. Prüfe Zuschüsse und Erlöse in ihrem konkreten Kostenbezug, ohne automatisch sämtliche PV-Einnahmen auf Mieter zu verteilen.

### 3.3. Erstelle nur den belegten Arbeitskostenausweis.

Für Paragraf 35a EStG weise getrennt die belegten, dem jeweiligen Empfänger zugeordneten Arbeitskosten haushaltsnaher Dienstleistungen oder Handwerkerleistungen aus. Halte Materialkosten, Zahlungsnachweis, Leistungsort und Zuordnungsschlüssel sichtbar. Bei fehlendem Arbeitskostenanteil fordere eine Aufschlüsselung an, statt ihn zu schätzen. Eine Reparatur kann steuerlich anders einzuordnen sein und bleibt trotzdem aus der Mietumlage ausgeschlossen. Bescheinige dem Mieter keine allein vom Eigentümer getragenen Kosten. Berechne weder eine Steuerersparnis noch persönliche Höchstbeträge oder eine Doppelberücksichtigung neben Werbungskosten.

## 4. Quellenpflicht

Nutze [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md), insbesondere die Berliner amtlichen Informationen zu 2025, Paragrafen 1 und 2 BetrKV, 42a EnWG und 35a Absatz 5 EStG. Rechtsstand und Anwendungsjahr bleiben getrennt. Nicht belegte Liefervergütungen oder Steuerwirkungen werden nicht als feststehend ausgegeben.

## 5. Ausgabeformat

Liefere die abgegrenzten Kostenzeilen, die erforderliche Korrektur und gegebenenfalls den gesonderten Arbeitskostenausweis in vollständigen, ausformulierten Sätzen. Skelette, Halbsätze und reine Aufzählungen sind als Endprodukt verboten. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Textausgabe steht der Exporthinweis getrennt. Behaupte keine nicht erstellte Bescheinigung oder Datei.

## 6. Beispiele

Ein belegter Messbetrag von 86.80 EUR ergibt bei 470 Prozent einen Jahresbetrag von 407.96 EUR. Vier Zahlungen sind damit abzugleichen, nicht hinzuzurechnen. Eine Wallboxrechnung von 2.000 EUR wird nicht deshalb Allgemeinstrom, weil sie über das Hauskonto bezahlt wurde.

---

## Skill: `kosten-und-hausmeister-abgrenzen`

_Prueft Betriebskosten und gemischte Hausmeisterleistungen anhand von Vertrag, Rechnung und Taetigkeitsnachweisen und zieht Verwaltung, Reparaturen, Ruecklagen und Doppelansaetze nachvollziehbar ab._

# Kosten und Hausmeister abgrenzen

## 1. Zweck und Anwendungsfall

Bestimme für jede Kostenposition, ob und in welcher Höhe sie in die Mietabrechnung eingehen darf. Die Beschriftung einer WEG-Liste als umlagefähig ist ein Prüfansatz, keine Rechtsgrundlage.

## 2. Eingaben

Lies Mietvertrag und Betriebskostenanlage, Rechnungspositionen, Dienstleistungsverträge, Tätigkeits- und Zeitnachweise, Gutschriften sowie die vorhandene Kostentabelle. Erfrage keine bereits enthaltenen Angaben. Bei einer gemischten Rechnung benötigst du die fehlende Aufteilung, nicht die gesamte Buchhaltung nochmals.

## 3. Ablauf / Checkliste

### 3.1. Prüfe Vertragsgrund und Kostenart.

Ordne jede Position einer vereinbarten Kostenart und Paragraf 2 BetrKV zu. Prüfe laufenden Anfall nach Paragraf 1 Absatz 1 und die Ausschlüsse nach Absatz 2. Nicht jede jährlich bezahlte Ausgabe ist eine Betriebskostenposition. Sonstige Betriebskosten benötigen eine hinreichend konkrete Umlagevereinbarung; eine unbenannte Restkategorie trägt keine beliebigen neuen Positionen. Prüfe Wirtschaftlichkeit anhand konkreter Auffälligkeiten, nicht nach einer erfundenen starren Preisgrenze.

### 3.2. Zerlege Mischleistungen.

Trenne bei Hausmeister, Aufzug, Heizungswartung und Vollwartungsverträgen laufende Betriebstätigkeiten von Reparatur, Ersatzbeschaffung und Verwaltung. Für den Hauswart verknüpfe den tatsächlichen Zeitaufwand mit Tätigkeitsnachweisen und Vergütung. Besichtigungen für Neuvermietung, Mietinkasso und Reparaturarbeiten werden nicht durch das Etikett Hausmeister umlagefähig. Ein pauschaler Abzug ohne nachvollziehbare Grundlage wird nicht als gesicherte Aufteilung behandelt. Bei bestrittenen Pauschalen braucht die Vermieterseite eine konkrete Aufschlüsselung.

### 3.3. Berechne den bereinigten Ansatz.

Rechne ausgehend vom periodenbezogenen Bruttobetrag die belegten Gutschriften und nicht umlagefähigen Teilbeträge heraus. Ziehe Verwaltungskosten, Instandhaltung und Instandsetzung sowie Rücklagenzuführungen ab. Prüfe bei Rücklagenentnahmen die tatsächlich bezahlte Leistung gesondert, ohne sie wegen ihrer Finanzierung zur Betriebskostenposition zu erklären. Für Eigenleistungen prüfe Paragraf 1 Absatz 1 Satz 2 BetrKV; setze keine fiktive Umsatzsteuer eines Dritten an.

### 3.4. Schließe doppelte Leistungen aus.

Vergleiche die Hauswartstätigkeiten mit Reinigung, Gartenpflege, Winterdienst und weiteren Dienstleisterpositionen. Paragraf 2 Nummer 14 BetrKV verhindert den doppelten Ansatz der dort bezeichneten Arbeitsleistungen. Prüfe auch doppelt erfassten Schornsteinfeger und Heizstrom. Schreibe eine ungeklärte Aufteilung als offene Position fort und fordere den konkreten Leistungsnachweis an. Nach Eingang liefere die bereinigte Endsumme mit Begründung oder den bestellten Korrekturbrief.

## 4. Quellenpflicht

Nutze die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und das [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md). Tragend sind Paragrafen 1 und 2 BetrKV, Paragraf 556 BGB sowie BGH, Versäumnisurteil vom 20.02.2008 - VIII ZR 27/07, Randnummern 27 bis 32. Prüfe den Normstand der Abrechnungsperiode und belege Aufteilungsquoten aus der Akte.

## 5. Ausgabeformat

Liefere die Gegenüberstellung von Rechnung, Abzug und umlagefähigem Rest mit ausformulierter Begründung. Briefe und Vermerke bestehen aus vollständigen Sätzen; Skelette, Halbsätze und reine Aufzählungen sind als Endprodukt verboten. Nutze soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Trenne bei Textausgabe den Exporthinweis vom Empfängertext und behaupte keine nicht erzeugten Exporte.

## 6. Beispiele

Von 12.000 EUR Hauswartskosten entfallen nach geprüften Leistungsnachweisen 2.400 EUR auf Reparaturen und 1.200 EUR auf Verwaltung. Der Ausgangsansatz beträgt 8.400 EUR; zusätzlich ist zu prüfen, ob eine gesonderte Reinigungsrechnung dieselben Arbeitsleistungen enthält. Eine pauschale Behauptung, zehn Prozent seien immer ausreichend, wird nicht übernommen.

---

## Skill: `co2-kosten-belegt-aufteilen`

_Ermittelt CO2-Kosten aus verbrauchten Brennstoffschichten, prueft Wohngebaeudestufe und Vermieterabzug und erstellt den transparenten Ausweis oder eine bezifferte Erstattungsanforderung._

# CO2-Kosten belegt aufteilen

## 1. Zweck und Anwendungsfall

Rechne die CO2-Kostenaufteilung für Zentralversorgung oder Selbstversorgung des Mieters. Eine Energierechnung mit CO2-Zeile ist noch keine fertige gesetzliche Verteilung. Eine WEG darf den Vermieteranteil nicht als gewöhnliche Mietkosten weiterreichen.

## 2. Eingaben

Lies Abrechnungs- und Lieferzeiträume, Emissionen, Energiegehalt, Emissionsfaktor und enthaltene CO2-Kosten der Lieferbelege. Bei Öl lies die bewertete Bestandsfortschreibung samt Rechnungen der Altvorräte. Ermittle Wohngebäudeeigenschaft, versorgte Einheit, maßgebliche Wohnfläche, Heizkostenschlüssel und etwaige belegte öffentlich-rechtliche Hindernisse. Frage nur nach fehlenden Werten, die Einstufung oder Betrag ändern.

## 3. Ablauf / Checkliste

### 3.1. Fixiere Rechtszeit und Bezugsobjekt.

Für die Rechnung 2025 gilt das damalige CO2KostAufG; spätere Änderungen der aktuellen Normseite gelten nicht rückwirkend. Prüfe Anwendungsbereich, Zentral- oder Selbstversorgung und die Bezugsfläche nach Paragraf 5. Teile Gebäudeemissionen nicht durch die Fläche nur einer Wohnung. Für Nichtwohngebäude gilt 2025 nicht automatisch die Wohngebäudetabelle; eine gesetzliche Ankündigung eines künftigen Stufenmodells ist noch keine fertige Tabelle.

### 3.2. Berechne verbrauchsbezogene Emissionen und Kosten.

Ermittle je Liefer- oder Vorratsschicht die im Zeitraum verbrauchte Menge und deren anteilige Emissionen sowie CO2-Kosten. Bei homogener Lieferung ergibt sich der Kostenanteil aus Verbrauchsmenge/Liefermenge mal ausgewiesenen CO2-Kosten, die Emission entsprechend. Halte Lieferjahr, Rechnung, Faktor, Umsatzsteuerbehandlung und Restmenge sichtbar. Verwende keinen Preis des Verbrauchsjahrs für anders bepreisten Altvorrat. Die Übergangsregel des Paragrafen 11 Absatz 2 lässt CO2-Kosten vor 01.01.2023 in Rechnung gestellter Brennstoffmengen unberücksichtigt; bilde diese Schicht getrennt ab. Kläre bei solchen Altbeständen auch die für die Einstufung maßgebliche Emissionsabgrenzung anhand der einschlägigen Fassung, statt still alle Liter gleichzubehandeln.

### 3.3. Bestimme Stufe und Vermieteranteil.

Teile die maßgeblichen Jahreskilogramm durch die gesetzlich maßgebliche Wohnfläche und runde den spezifischen Ausstoß auf eine Nachkommastelle. Bei verkürztem Zeitraum passe die Tabellenschwellen anteilig an; annualisiere nicht zusätzlich nochmals. Die Vermieteranteile der Anlage betragen bei den Grenzen unter 12, 17, 22, 27, 32, 37, 42, 47 und 52 kg sowie ab 52 kg der Reihe nach 0, 10, 20, 30, 40, 50, 60, 70, 80 und 95 Prozent. Prüfe die Tabelle am Normtext, insbesondere genau auf einer Grenze.

Öffentlich-rechtliche Beschränkungen können nach Paragraf 9 den Vermieteranteil halbieren oder bei Hindernissen in beiden gesetzlichen Bereichen entfallen lassen. Die bloße Bezeichnung Denkmalschutz oder Milieuschutz genügt nicht; der Vermieter muss die konkreten einschlägigen Hindernisse nachweisen. Halbiere bei einem belegten einschlägigen Hindernis den Vermieteranteil, nicht die Gesamtkosten.

### 3.4. Führe die Kosten in die Abrechnung zurück.

Ziehe den Vermieteranteil vor der Mieterumlage genau einmal aus den bereits CO2-haltigen Brennstoffkosten ab. Verteile den verbleibenden Mieteranteil nach dem maßgeblichen Heiz- und Warmwasserschlüssel, nicht nochmals allein nach Wohnfläche. Weise Stufe, Berechnungsgrundlagen, Gesamt-CO2-Kosten und Mieteranteil aus. Prüfe bei fehlender Aufteilung oder fehlenden Angaben Paragraf 7 Absatz 4 und dessen Drei-Prozent-Kürzung, ohne sie mit anderen Kürzungen ungeprüft zu addieren.

Bei Selbstversorgung des Mieters berechne die Erstattung und prüfe die zwölfmonatige Geltendmachungsfrist ab Lieferantenabrechnung sowie Textform nach Paragraf 6 Absatz 2. Halte Anzeige, Verrechnung und späteste Erstattung getrennt. Nach einem ergänzten Lieferbeleg korrigiere die Schichtrechnung und den bestellten Brief unmittelbar.

## 4. Quellenpflicht

Nutze die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und die historischen und aktuellen CO2-Quellen im [Register](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md). Die amtliche Ursprungsfassung vom 05.12.2022 belegt den für 2025 relevanten Rechenkern der Paragrafen 3 bis 9, 11 und der Anlage. Verifiziere Anwendungszeitpunkt und etwaiges Änderungsrecht vor jeder späteren Abrechnung; erfinde keine Gerichtsentscheidung zur Stufung.

## 5. Ausgabeformat

Liefere eine Liefer- und Verbrauchstabelle mit begründeter Stufe und bezifferter Überleitung oder den ausformulierten Erstattungsbrief. Endprodukte stehen in vollständigen Sätzen; Skelette, Halbsätze und reine Aufzählungen sind verboten. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Ein Exporthinweis gehört bei Textausgabe nicht in den Brief. Behaupte keine nicht erstellte Datei.

## 6. Beispiele

Bei 24.000 kg CO2 auf 800 Quadratmetern im ganzen Jahr ergeben sich 30.0 kg je Quadratmeter. Bei 1.600 EUR enthaltenen CO2-Kosten und ohne einschlägige Beschränkung entfallen 640 EUR auf den Vermieter und 960 EUR auf die Mietergruppe. Die 960 EUR sind schon Bestandteil des bereinigten Heizkostentopfs und werden nicht nochmals als Zusatzkosten aufgeschlagen.

---

## Skill: `weg-kosten-in-mietabrechnung-ueberleiten`

_Ueberfuehrt WEG-Gesamt- und Einzelabrechnung in die Mietabrechnung einer Eigentumswohnung, prueft den Schluessel nach Paragraf 556a Absatz 3 BGB und entfernt reine Eigentuemerpositionen._

# WEG-Kosten in die Mietabrechnung überleiten

## 1. Zweck und Anwendungsfall

Erstelle für die vermietete Eigentumswohnung eine eigene Betriebskostenabrechnung. Die WEG-Abrechnung ist ein Eingangsbeleg; sie wird weder als Ganzes noch mit ihrem Hausgeldsaldo zur Forderung gegen den Mieter.

## 2. Eingaben

Lies Gesamt- und Einzelabrechnung, Kontennachweise, Heizkostenanlage, Verteilungsbeschlüsse, Mietvertrag, Zahlungsjournal des Mieters und separat getragene Wohnungskosten. Lies Rücklagenbewegungen und Sonderumlagen nur zur Einordnung, nicht als Ersatz für Leistungsbelege. Frage gezielt nach einem fehlenden Gebäudegesamtbetrag oder Schlüssel, wenn die Einzelabrechnung keine Neuberechnung erlaubt.

## 3. Ablauf / Checkliste

### 3.1. Trenne die Rechtsverhältnisse.

Unterscheide Beschlüsse über Vorschüsse oder Nachschüsse nach Paragraf 28 WEG von der mietvertraglichen Kostentragung. Prüfe den Inhalt der einzelnen Kostenzeile nach Paragrafen 1 und 2 BetrKV. Verwaltung, Instandhaltung, Instandsetzung, Rücklagenzuführung, Finanzierung und bloße Abrechnungsspitze werden nicht an den Mieter weitergegeben. Eine Sonderumlage ist eine Finanzierungsform; nur die dahinterstehende konkret belegte Leistung kann gegebenenfalls eine Betriebskostenart sein.

### 3.2. Erstelle die Überleitungsrechnung.

Erfasse je Zeile den WEG-Gesamttopf, den Eigentümeranteil, dessen Schlüssel, nicht umlagefähige Bestandteile, Gutschriften und den Mietansatz. Rechne reparaturhaltige Vollwartung oder Hausmeisterkosten nach den Einzelbelegen auseinander. Prüfe den bereits vorgenommenen CO2-Vermieterabzug und ziehe ihn nicht ein zweites Mal ab. Rücklagenentnahme und damit finanzierte Rechnung werden nicht als zwei Kosten erfasst.

### 3.3. Prüfe den richtigen Mietmaßstab.

Eine wirksame abweichende Mietvereinbarung geht der Auffangregel vor. Ohne eine solche Vereinbarung gilt Paragraf 556a Absatz 3 BGB: Ausgangspunkt ist der jeweils geltende Verteilungsmaßstab der Wohnungseigentümer; bei Widerspruch zu billigem Ermessen gilt Absatz 1. Beachte daneben die zwingende HeizkostenV. Die WEG-Auffangregel legitimiert weder Reparaturkosten noch Rücklagen. Ist die Einzelzeile bereits mit dem richtigen Maßstab wohnungsbezogen gerechnet, verteile sie nicht nochmals. Bei abweichendem Mietmaßstab berechne aus dem bereinigten Gebäudetopf neu; ohne ihn bleibt die betroffene Zeile offen.

### 3.4. Füge Eigentümerbelege und Mietzahlungen hinzu.

Ergänze etwa die Grundsteuer der vermieteten Wohnung, sofern sie nicht schon enthalten ist. Prüfe Bescheididentität und Umlagegrund. Verwende für den Mieter nur dessen tatsächlich geleistete Betriebskostenvorauszahlungen, nicht Hausgeldvorschüsse des Eigentümers. Teile bei Nutzerwechsel die Kosten sachgerecht auf und weise Eigentümer-/Leerstandsanteile aus. Stimme die Überleitung bis zum Mietsaldo ab.

### 3.5. Sichere den Abschluss trotz WEG-Verzögerung.

Ein fehlender WEG-Beschluss ist keine automatische Voraussetzung oder Fristverlängerung für die Mietabrechnung. Prüfe eigene Beschaffungsbemühungen und fehlendes Vertretenmüssen konkret. Fordere benannte Belege rechtzeitig an und arbeite mit vorhandenen gesicherten Zahlen weiter. Eine erfundene vorläufige Nachforderung wahrt keine Frist verlässlich. Nach Ergänzung erstelle die Mietabrechnung oder beantworte die Einwendung; leite keine Klage ohne Auftrag ein.

## 4. Quellenpflicht

Prüfe anhand der [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und des [Quellenregisters](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md) Paragrafen 556, 556a Absatz 3 BGB, 28 WEG und die BetrKV. BGH, Urteil vom 25.01.2017 - VIII ZR 249/15, Randnummern 17, 35 und 46 bis 47, belegt Frist und Kostentrennung. Seine damalige Schlüsseldiskussion ersetzt nicht den später eingeführten Absatz 3 des Paragrafen 556a BGB.

## 5. Ausgabeformat

Liefere die nachvollziehbare WEG-zu-Miet-Überleitung und die bestellte Abrechnung in vollständigen, ausformulierten Sätzen mit Rechentabelle. Skelette, Halbsätze und reine Aufzählungen sind verboten. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Halte technische Exporthinweise bei Textausgabe außerhalb des Empfängertexts; verlinke keine nicht erzeugten Exporte.

## 6. Beispiele

Eine wohnungsbezogene WEG-Kostenaufstellung von 4.800 EUR enthält 600 EUR Verwaltung, 900 EUR Reparaturen und 1.200 EUR Rücklagenzuführung. Nach diesen Abzügen verbleiben 2.100 EUR, deren Mietschlüssel noch zu bestätigen ist. Kommen belegte 300 EUR Grundsteuer einmalig hinzu und wurden 2.600 EUR Mietvorauszahlungen geleistet, ergibt sich bei vollständiger Kostenbasis ein Guthaben von 200 EUR, nicht eine Hausgeldnachforderung.

---

## Skill: `belege-und-zahlungen-abgleichen`

_Ordnet Rechnungen, Abschlaege, Gutschriften und Zahlungsbelege einer Betriebskostenperiode zu und erstellt ein abgestimmtes Belegregister oder eine konkrete Unterlagenanforderung._

# Belege und Zahlungen abgleichen

## 1. Zweck und Anwendungsfall

Erzeuge aus dem vorhandenen Ordner eine prüfbare Kostenbasis für Mietshaus oder vermietete ETW. Unterscheide Entstehung, Zahlung, Abrechnung und Verteilung; ein Kontoauszug allein beweist die Umlagefähigkeit nicht.

## 2. Eingaben

Lies Rechnungen mit Anlagen, Liefer- und Leistungsbelege, Kontobuchungen, Gutschriften, Verträge und Vorjahresabgrenzungen zuerst. Nutze bei WEG sowohl die Gesamtabrechnung als auch wohnungsbezogene Zeilen. Frage nur nach fehlenden Unterlagen, die eine konkrete Zuordnung oder Endsumme verändern.

## 3. Ablauf / Checkliste

### 3.1. Sichere Herkunft und Identität.

Vergib pro Geschäftsvorfall eine Belegkennung mit Datei, Seite oder Tabellenzelle. Erfasse Aussteller, Rechnung, Objekt, Kostenart, Leistungszeit, Rechnungsdatum, Bruttobetrag und Zahlungsdatum. Kennzeichne OCR-unsichere Zahlen zur Sichtprüfung. Eine Datei mit mehreren Rechnungen erhält mehrere Datensätze; eine zweite Kopie erzeugt keine zweite Ausgabe. Verändere keine Originaldateien.

### 3.2. Stimme Rechnung, Minderung und Zahlung ab.

Verknüpfe Teilzahlungen, Skonto, Storno, Erstattung und Gutschrift mit der Ursprungsrechnung. Eine Rechnung von 1.190 EUR mit Gutschrift von 190 EUR und Zahlungen von zweimal 500 EUR ergibt 1.000 EUR Kosten, nicht 2.000 EUR und keinen offenen Rest. Eine Schlussrechnung mit verrechneten Abschlägen wird nicht nochmals um dieselben Abschläge erhöht. Prüfe Kostenminderungen auch bei abweichendem Buchungsjahr.

### 3.3. Bestimme die Periodenzuordnung.

Dokumentiere je kalter Kostenart das angewandte Leistungs- oder zulässige Abflussprinzip und die Vermeidung von Doppelansatz an Jahresgrenzen. Eine noch unbezahlte, periodenbezogene Leistung fällt beim Leistungsprinzip nicht allein wegen fehlender Zahlung aus der Kostenbasis. Beim Abflussprinzip ist der Zahlungszeitpunkt entscheidend. Wechselnde Nutzer und Methodenwechsel erfordern einen gesonderten Zuordnungsabgleich. Bei Heizung darf die Zahlung den Verbrauch nicht ersetzen.

### 3.4. Schließe die Beleglücke konkret.

Summiere je Kostenart den belegten Ansatz, offene Differenzen und Zahlungen. Fordere etwa die bezeichnete Gutschrift, die zweite Rechnungsseite oder den Zahlungsbeleg zur benannten Buchung an, nicht pauschal alle Unterlagen erneut. Belegeinsicht umfasst auch vorhandene Zahlungsbelege, unabhängig von der Abrechnungsmethode. Elektronische Bereitstellung ist nach Paragraf 556 Absatz 4 BGB zulässig; ein Tabellenexport mit Endbeträgen ersetzt nicht die zugrunde liegenden Belege. Nach Eingang aktualisiere die betroffenen Zeilen und übergib die abgestimmte Summe zur Abrechnung.

## 4. Quellenpflicht

Wende die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) an. Prüfe Paragrafen 556 und 259 BGB sowie im [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md) BGH, Urteil vom 09.12.2020 - VIII ZR 118/19, Randnummern 12 bis 17. Dieser Anker belegt Zahlungsbelege, nicht den unbesehenen Ansatz sämtlicher Kontobelastungen.

## 5. Ausgabeformat

Liefere das Belegregister mit Kontrollsummen und die entscheidenden Abweichungen in vollständigen, ausformulierten Sätzen. Ein beauftragtes Anforderungsschreiben ist auszuformulieren; Skelette, Halbsätze und reine Aufzählungen sind kein Endprodukt. Formatierte Dokumente nutzen soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Textausgabe nenne das nur im getrennten Exporthinweis. Verlinke nur tatsächlich erzeugte Dateien.

## 6. Beispiele

Die Hausverwaltung legt zwei Scans derselben Wasserrechnung vor. Erfasse sie einmal und verknüpfe beide Fundstellen. Fehlt zu einer bereits verrechneten Gutschrift der Originalbeleg, benenne diese Lücke; setze die Gutschrift nicht wieder auf null und behaupte keine endgültige Freigabe.

---

## Skill: `oel-heizung-und-warmwasser-abrechnen`

_Rekonstruiert Oelbestand und Verbrauchskosten, trennt Heizung und Warmwasser und rechnet Grund- und Verbrauchsanteile nach der HeizkostenV samt Pflichtquote und Messluecken nach._

# Öl, Heizung und Warmwasser abrechnen

## 1. Zweck und Anwendungsfall

Erstelle eine prüfbare Heizkostenrechnung statt einer bloßen Addition von Brennstoffzahlungen. Der Ablauf gilt auch für die Kontrolle einer WEG-Heizkostenanlage; fossile Kosten und CO2-Vermieteranteil werden getrennt ermittelt und anschließend abgestimmt.

## 2. Eingaben

Lies Tankpeilungen mit Datum, Anfangsbestand und Anschaffungswert, Lieferrechnungen, Gutschriften, Endbestand, Messdienstabrechnung, Zählerliste, Warmwasser-Wärmemessung, Nutzerflächen und Heiznebenkosten. Prüfe den energetischen Gebäudestandard und die Dämmung freiliegender Verteilungsleitungen anhand vorhandener Unterlagen, nicht allein anhand des Baujahrs.

## 3. Ablauf / Checkliste

### 3.1. Ermittle den Bestandsverbrauch.

Rechne Literverbrauch als Anfangsbestand plus Lieferungen minus Endbestand. Prüfe Tankkapazität, Zeitfolge, Lieferscheine und die Übereinstimmung mit dem Vorjahresendbestand. Rechne den Verbrauchswert aus den Anschaffungskosten der verbrauchten Mengen. Lege die nachvollziehbare Verbrauchsfolge und Bewertung offen; für eine belegte FIFO-Fortschreibung werden die ältesten Schichten zuerst verbraucht. Verwende weder den letzten Einkaufspreis für den ganzen Verbrauch noch einen unbegründeten Durchschnitt. Endbestand in Litern und EUR bleibt Vorrat für das Folgejahr. Fehlende Bestandswerte werden nicht durch den Zahlbetrag der Jahreskäufe ersetzt.

### 3.2. Bereinige den Heizkostentopf.

Ordne nur die Kosten nach Paragraf 7 Absatz 2 HeizkostenV zu. Ziehe Reparaturanteile aus Wartung heraus; ordne Heizungsbetriebsstrom nicht zugleich dem Allgemeinstrom zu. Eine Schätzung ohne Zwischenzähler braucht belastbare Leistungs-, Laufzeit- und Tarifdaten oder eine sonst nachvollziehbare Grundlage, keinen frei gewählten Prozentsatz. Stimme den CO2-Vermieterabzug mit der eigenen CO2-Rechnung ab und verhindere dessen doppelten Abzug in einer bereits bereinigten Messdienstabrechnung.

### 3.3. Trenne Wärme und Warmwasser.

Bei verbundener Anlage teile gemeinsame Kosten nach Paragraf 9 HeizkostenV auf und ordne ausschließlich verursachte Zusatzkosten dem richtigen Teil zu. Für Warmwasser gilt grundsätzlich die Wärmemessung. Die Ersatzformel Q = 2,5 mal V mal (tw minus 10) setzt unzumutbar hohen Messaufwand voraus; V steht für Kubikmeter, tw für die belegte mittlere Temperatur. Die weitere Flächenersatzformel ist kein freies Wahlrecht. Bei Öl ergibt Q in kWh geteilt durch Hi in kWh/L die Warmwasser-Brennstoffmenge B in Litern. Erst B geteilt durch den gesamten Periodenverbrauch in Litern ergibt den Kostenanteil. Verwende den Lieferantenheizwert, nur hilfsweise den normativen Wert. Bei zulässiger Aufteilung nach Wärmeverbrauch müssen Warmwasser- und Gesamtwärmezähler dieselbe Systemgrenze und Periode abbilden; ihr Verhältnis in kWh/kWh ist dimensionslos. Vermische nicht abgegebene Nutzwärme und Brennstoffenergie ohne begründete Umrechnung. Prüfe, ob Kaltwasser für Warmwasser schon in den Wasserkosten enthalten ist.

### 3.4. Prüfe Quote und rechne Nutzeranteile.

Nach Paragrafen 7 und 8 werden regulär 50 bis 70 Prozent nach Verbrauch verteilt; der Rest folgt dem jeweils zulässigen Flächen- oder Raummaßstab. Die Pflicht zu 70 Prozent nach Paragraf 7 Absatz 1 Satz 2 betrifft Heizung und verlangt kumulativ, dass das Anforderungsniveau der Wärmeschutzverordnung vom 16.08.1994 nicht erfüllt ist, eine Öl- oder Gasheizung versorgt und die freiliegenden Wärmeverteilungsleitungen überwiegend gedämmt sind. Ungedämmte Leitungen erfüllen gerade nicht die dritte Voraussetzung. Prüfe Sonderregeln für Rohrwärme, Paragrafen 2, 10 und 11, bevor du eine Quote freigibst. Die Heizungs-Pflichtquote geht nicht automatisch auf Warmwasser über.

Rechne je getrenntem Topf K den Anteil als K mal Verbrauchsquote mal Nutzerverbrauch/Gesamtverbrauch plus K mal Grundkostenquote mal Nutzergrundfläche/Gesamtgrundfläche. Prüfe Einheiten und Zählerzuordnung. Bei Geräteausfall prüfe die Vergleichsverfahren nach Paragraf 9a Absatz 1 und bei mehr als 25 Prozent betroffener maßgeblicher Fläche dessen Absatz 2. Eine fehlende Angabe ist kein Nullverbrauch. Bei Nutzerwechsel gilt Paragraf 9b. Prüfe Kürzungsrechte nach Paragraf 12 gesondert; 15 Prozent heilen keine falsche Abrechnung nach Jahreszahlungen. Beachte zeitliche Übergangsregeln insbesondere bei Fernablesbarkeit und Wärmepumpen.

## 4. Quellenpflicht

Lies die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und die Heizkostenquellen im [Register](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md). Tragend sind Paragrafen 7 bis 12 HeizkostenV sowie BGH, Urteil vom 01.02.2012 - VIII ZR 156/11, Randnummern 10 bis 14, und zum Heizstrom BGH, Versäumnisurteil vom 20.02.2008 - VIII ZR 27/07, Randnummer 32. Prüfe den für 2025 geltenden Text, nicht lediglich die heutige Konsolidierung.

## 5. Ausgabeformat

Liefere Bestandsrechnung, bewertete Verbrauchsschichten, getrennte Kostenpoole und Nutzerrechnung mit ausformuliertem Ergebnis. Vollständige Sätze sind Pflicht; Skelette, Halbsätze und reine Aufzählungen genügen nicht. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Textausgabe steht der Formatwunsch getrennt als Exporthinweis. Gib keine nicht erzeugte Tabellen- oder PDF-Datei vor.

## 6. Beispiele

Ein belegter Anfangsbestand von 2.000 Litern zu 1.10 EUR und ein Zugang von 3.000 Litern zu 1.00 EUR ergeben bei 1.000 Litern Endbestand 4.000 Liter Verbrauch. Mit nachvollziehbarer FIFO-Fortschreibung beträgt der Verbrauchswert 4.200 EUR, der Restwert 1.000 EUR. Die Rechnung von 3.000 EUR für den Zugang allein wäre keine korrekte Jahresverbrauchsrechnung.

---

## Skill: `flaechen-und-umlageschluessel-pruefen`

_Prueft Wohnflaechen, Verbrauchs- und WEG-Schluessel sowie Leerstand und Nutzerwechsel und berechnet die belegten Anteile je Kostenart ohne doppelte Verteilung._

# Flächen und Umlageschlüssel prüfen

## 1. Zweck und Anwendungsfall

Erstelle eine belastbare Verteilungsmatrix für ein Mietshaus oder eine vermietete Eigentumswohnung. Verwechsle die Entscheidung für einen Maßstab nicht mit dem Nachweis der dazu gehörenden Quadratmeter oder Zählerstände.

## 2. Eingaben

Lies die konkrete Mietklausel, Flächenberechnung, Objekt- und Nutzerliste, Zählerzuordnung und Übergabeprotokolle. Bei ETW lies Teilungserklärung und einschlägige Verteilungsbeschlüsse. Frage nur nach dem Nachweis, der einen widersprüchlichen Nenner, Maßstab oder Zeitraum entscheidet.

## 3. Ablauf / Checkliste

### 3.1. Bestimme je Kostenart die Rechtsgrundlage.

Prüfe zwingende Sonderregeln, insbesondere die HeizkostenV, und anschließend die wirksame Mietvereinbarung. Fehlt eine abweichende Vereinbarung, greift beim eigenen Mietshaus Paragraf 556a Absatz 1 BGB. Bei vermietetem Wohnungseigentum gilt dagegen Absatz 3: Der jeweils für die Eigentümer geltende Maßstab ist Ausgangspunkt; bei Widerspruch zu billigem Ermessen ist Absatz 1 anzuwenden. Eine ausdrückliche Mietklausel wird nicht durch einen späteren WEG-Beschluss beliebig ersetzt. Ein Wechsel zum erfassten Verbrauch nach Absatz 2 verlangt seine eigenen Voraussetzungen und eine vorherige Erklärung in Textform.

### 3.2. Kläre die Verteilungseinheit.

Ordne Gebäude, Wirtschaftseinheit, Wohnungsnummer, Gewerbe, Stellplätze und Nutzer den jeweiligen Kosten zu. Prüfe einen Vorwegabzug bei tatsächlich erheblicher Mehrbelastung durch abweichende Nutzung, statt Gewerbe ohne Beleg stets auszunehmen. Dokumentiere für jeden Topf Zähler, Nenner, Maßeinheit und Quelle. Miteigentumsanteile sind keine Quadratmeter. Wenn nach Wohnfläche verteilt wird, sind grundsätzlich die tatsächlichen Flächen maßgeblich; eine alte Zehn-Prozent-Toleranz wird nicht verwendet.

### 3.3. Rechne Nutzeranteile und Leerstand.

Rechne flächenbezogene Jahreskosten als Topf mal Wohnungsfläche/Gesamtfläche. Leerstehende und selbst genutzte Einheiten bleiben mit ihren Anteilen im passenden Nenner. Eine leere Wohnung wird nicht auf die übrigen Mieter umverteilt. Für zeitbezogene Aufteilung verwende belegte Nutzungszeiträume und eine dokumentierte Tages- oder Monatsmethode. Verbrauchskosten folgen den erfassten Mengen; Heizungsnutzerwechsel prüfst du nach Paragraf 9b HeizkostenV mit Zwischenablesung und passendem Grundkostenanteil, nicht mit einem pauschalen Halbjahresfaktor.

### 3.4. Führe Gegenproben aus.

Addiere alle Nutzer- und Eigentümeranteile zum Topf zurück. Prüfe, ob eine WEG-Einzelzeile bereits die Wohnung betrifft und deshalb kein zweiter Miteigentumsfaktor folgen darf. Weicht der Mietschlüssel ab, rekonstruiere den Gesamtbetrag und verteile neu. Bei ungeklärter Fläche zeige nur die entscheidenden belegbaren Varianten samt Differenz; fordere den konkreten Flächenbeleg an und ersetze die Variante nach dessen Eingang durch den Endwert.

## 4. Quellenpflicht

Beachte die [Zitierweise](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/zitierweise.md) und das [Quellenregister](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/betriebskosten-hausverwaltung/references/betriebskosten-quellen.md), insbesondere Paragraf 556a Absätze 1 bis 3 BGB, Paragrafen 7 bis 9b HeizkostenV und BGH, Urteil vom 30.05.2018 - VIII ZR 220/17, Randnummern 19 bis 23. Die Entscheidung zur Fläche hebt die spätere WEG-Auffangregel nicht auf.

## 5. Ausgabeformat

Liefere Schlüssel, Herkunft, Formel, Einzelanteile und Kontrollsumme mit vollständigen, ausformulierten Erläuterungen. Ein Ergebnis nur aus Halbsätzen, Skeletten oder reinen Aufzählungen ist unzulässig. Verwende soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung. Bei Textausgabe trenne den Exporthinweis ab; verlinke nur wirklich erzeugte Dateien.

## 6. Beispiele

Bei 10.000 EUR Jahreskosten und 80 von 800 Quadratmetern ergeben sich ganzjährig 1.000 EUR. Sind davon 100 Quadratmeter leer, bleibt der Nenner 800. Für eine vermietete ETW ohne abweichende Mietklausel ist dagegen zunächst der geltende WEG-Schlüssel zu prüfen; 80/800 darf nicht automatisch verwendet werden.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
