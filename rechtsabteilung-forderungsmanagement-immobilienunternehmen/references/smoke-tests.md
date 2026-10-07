# Smoke-Tests — immobilien-forderungsmanagement

Diese Datei beschreibt einfache Szenarien, mit denen man das Fachplugin `forderungsmanagement-immobilien` mit 50 Skills und die fachlich neutrale `schriftsatzwerkstatt-bea` mit neun Skills schnell auf Funktionsfähigkeit prüft.

Ein Smoke-Test bestätigt nicht die juristische Richtigkeit jeder Antwort — er stellt sicher, dass das Plugin die Skills lädt, den richtigen Datenraum liest und ein verwertbares Ausgabeformat mit ausformuliertem Arbeitsergebnis liefert.

Vorgehen pro Test:

1. Plugin `forderungsmanagement-immobilien` laden (`/plugin load forderungsmanagement-immobilien`).
2. Den jeweils unter "Eingang" genannten Testakten-Ordner unter `testakten/` als Arbeitsbereich öffnen.
3. Bei Autostart-Tests keinen Skill nennen; sonst den Kaltstart-Skill des Plugins aufrufen, wie unter "Schritt 1" benannt.
4. Den im Test benannten Folgeskill anstossen und prüfen, ob der "Erwartete Output" sichtbar wird.

Für Test 17 stattdessen ausschließlich `schriftsatzwerkstatt-bea` laden. Dadurch wird geprüft, dass die technische Werkstatt unabhängig vom Fachplugin startet und keine materiell-rechtliche Bearbeitung übernimmt.

Wenn der Output nicht erscheint oder der Skill abbricht: Plugin nicht release-fähig, Bugfix vor neuem Tag.

## 0 Kaltstart und Skill-Auswahl

Dieser Test prüft, ob die Skills bei direkter Nutzung zuverlässig den richtigen Einstieg finden und verkümmerte Spezialskills nicht übergangen werden.

**Eingang A:** Gemischtes Upload-Bundle aus SAP-Status, FBL5N, Mietvertrag, E-Mail, Scan und handschriftlicher Notiz.

**Erwarteter Start:** `33-dokumentenmix-ocr-sichten`, danach `01`, `34` oder `06`.

**Abbruchkriterium:** Sofortige Klage, Kündigung, Vollstreckung oder Mieterhöhung ohne Dokumenteninventar.

**Eingang A0:** Gleiches Bundle, aber nur mit Nutzersatz `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.` und ohne Skill-Nennung.

**Erwarteter Start:** Das Plugin startet mit `33-dokumentenmix-ocr-sichten`. Zuerst erscheint die einheitliche Sofortkarte mit Modus, Akten-ID/Stichtag, Fallart, frühester möglicher Frist samt Quelle und Rechenstatus, Ampel/Grund, Dateistand gelesen/gesamt, höchstens drei Kernlücken und Feld `Jetzt` mit genau einer Arbeitsaktion. Danach folgen ohne Befehl `weiter` Startkarte und Dokumenteninventar; die Skill-ID bleibt intern. Nur Fragen, die sofort Frist, Rolle oder Maßnahme ändern, dürfen den Lauf unterbrechen.

**Abbruchkriterium:** Das Modell fragt zuerst nach einer Skillauswahl oder springt direkt in einen Fachskill.

**Eingang A1:** Großes Upload-Bundle mit mehr als 25 Dateien und einem PDF mit mehr als 60 Seiten, darunter am Ende der Sortierung eine kurzfristige gerichtliche Verfügung, Scans mit schlechter OCR und mehrere Dubletten. Die Bearbeitung wird nach dem ersten Stapel unterbrochen und anschließend mit ihrer letzten Ausgabe fortgesetzt.

**Erwarteter Start:** `33-dokumentenmix-ocr-sichten` scannt zuerst den gesamten sichtbaren Bestand und erkennt die gerichtliche Verfügung trotz ihrer späten Position. Danach liefert er die Sofortkarte und vertieft in der Reihenfolge Gericht/Zustellung, Zahlung/Konto, Kündigung/Vertrag, übrige Belege. Ein Stapel endet spätestens nach 20 Dateien oder 30 PDF-Seiten. Die Fortsetzungsmarke nennt Akten-ID, Stichtag, verarbeitet/offen, letzte Quelle mit Seite oder Hash, früheste Frist, Risiken und nächsten Stapel. Nach Wiederaufnahme setzt der Skill dort fort und wiederholt weder unveränderte Dokumente noch Roh-OCR oder vollständige Tabellen. Sichtbare Tabellen haben höchstens sieben Spalten.

**Abbruchkriterium:** Ein unbeschränkter Lauf über das Lang-PDF, fehlende Fortsetzungsmarke, Neustart bei Datei 1, wiederholter Rohtext, eine überbreite Nutzertabelle oder Abbruch wegen einzelner OCR-Probleme.

**Eingang A2:** Vorhandene Startkarte und Chronologie einer laufenden Zahlungsklage, dazu nur eine Teilzahlung, eine gerichtliche Verfügung und ein neuer SAP-Kontoauszug.

**Erwarteter Start:** Das Plugin arbeitet im Delta-Modus. Es übernimmt Akten-ID und letzten Stichtag, gibt eine Änderungskarte mit Alt-/Neu-Saldo, neuer Frist, geändertem Beweisstatus, überholtem Replikstand und genau einer nächsten Arbeitsaktion in Klartext aus. Intern führt bei laufender Gerichtsfrist `37`; der SAP-/Mietkonto-Abgleich über `01` oder `03` steht danach in der Warteschlange.

**Abbruchkriterium:** Vollständiger Neu-Intake trotz belastbarem Altstand, stilles Überschreiben des alten Saldos oder parallele Empfehlung mehrerer Folgeskills ohne Priorität.

**Eingang B:** Sauberer SAP-Statusauszug mit FBL5N-Mietkonto und Vertragsnummer.

**Erwarteter Start:** `01-sap-akte-importieren`, danach `02` bis `05` und `06`.

**Abbruchkriterium:** Direkter Sprung zu `20`, `24` oder `17` ohne Belegmatrix und Triage.

**Eingang C:** Gerichtliche Klageerwiderung mit Minderungseinwendung, Teilzahlung und Beweisangebot.

**Erwarteter Start:** `37-klageerwiderung-auswerten`, danach `38` und `39`; `42` nur bei eigener Mieterklage oder Widerklage.

**Abbruchkriterium:** Neue Zahlungsklage oder Mieterklage-Verteidigung als Standardpfad.

**Eingang D:** Kostenfestsetzungsantrag, KFB oder positiver Zahlungstitel.

**Erwarteter Start:** `46` bei KFA, `47` bei KFB, `48` erst bei positivem vollstreckbaren Titel.

**Abbruchkriterium:** Vollstreckung ohne Titel, Klausel, Zustellung oder Kostengrund.

## 0.1 Rechtzeitigkeit der Wohnraummietzahlung

**Eingang:** SAP weist den Kontoeingang am fünften Kalendertag aus. Der Mieter belegt einen gedeckten Überweisungsauftrag am dritten Werktag; ein Sonnabend liegt im Berechnungszeitraum.

**Erwarteter Start:** Skills `03`, `09`, `11`, `13`, `14`, `20` und `24` trennen Fälligkeit, Zahlungsauftrag und Kontoeingang. Sonnabend zählt für diese Wohnraummietzahlungsfrist nicht. Der Kontoeingang allein löst weder Verzug, Zinsen, Kündigung noch Klageposition aus; BGH VIII ZR 222/15 sowie VIII ZR 129/09 oder VIII ZR 291/09 werden als geprüfte Anker geführt.

**Abbruchkriterium:** Der SAP-Buchungstag nach dem dritten Werktag wird ohne Prüfung von Zahlungsauftrag, Deckung, Rückgabe oder Storno als verspätete Zahlung behandelt.

## 0.2 Freigabegate für Außenstücke

**Eingang:** Fertige Zahlungsklage mit Anlagen und anschließend eine neue Teilzahlung, die Hauptsumme und Zinsstaffel ändert.

**Erwarteter Start:** Skill `20` liefert eine getrennte Freigabekarte mit Status `ENTWURF - NICHT VERSENDEN/EINREICHEN`. Eine reale Freigabeperson wird benannt; das Modell setzt nicht selbst `FREIGEGEBEN`. Die Teilzahlung hebt eine frühere Freigabe auf. Skill `23` blockiert die Einreichung, bis Antrag, Betrag, Anlagenstand, Dokumentversion und Stichtag erneut freigegeben sind.

**Abbruchkriterium:** Freigabe wird unterstellt, der interne Status erscheint im Gerichtsdokument oder eine geänderte Dokumentversion wird mit alter Freigabe eingereicht.

## 0.3 Gerichtsfertiges Einreichungspaket

**Eingang A:** Fachlich fertige Replik einer beauftragten Kanzlei, bereits eingereichte Anlagen K 1 bis K 6, zwei neue DOCX/XLSX-Belege, ein unlesbarer Scan, bekannte Gerichtsakte und Auftrag `Bitte finalisiere alles als gerichtsfertiges Einreichungspaket.`

**Erwarteter Start A:** Skill `39` ordnet Tatsachen und Beweise zu, sperrt K 1 bis K 6, vergibt K 7/K 8 nur für vollständige Belege und erzeugt ein Anlagenmanifest. Skill `23` schließt zuerst das Kanzlei-Rollengate, fragt gebündelt nach Gestaltungsprofil und fehlendem Scan, lässt Originale unverändert, erzeugt Einzel-PDFs, kennzeichnet Anlagen, bildet kurze ASCII-Dateinamen und prüft Paragrafen 130a und 130d ZPO, ERVV sowie Signatur- und Versenderidentität.

**Eingang B:** Derselbe fachlich fertige Schriftsatz, aber die private Konzerngesellschaft handelt im zulässigen Amtsgerichts-Parteiprozess selbst. Beschäftigtenstatus und Vollmacht sind belegt; offen ist, ob ein eBO der richtigen Gesellschaft eingerichtet ist.

**Erwarteter Start B:** Skill `23` behandelt die private GmbH nicht allein wegen ihrer Rechtsform als nach Paragraf 130d ZPO aktiv nutzungspflichtig. Er prüft Paragraf 79 ZPO und entscheidet zwischen einem tatsächlich eingerichteten eBO nach Paragraf 130a Abs. 4 S. 1 Nr. 3 ZPO und Paragraf 10 ERVV oder einer im konkreten Verfahren zulässigen eigenhändig unterzeichneten schriftlichen Einreichung. Bei eBO werden Postfachinhaber, verantwortende natürliche Person, Versandberechtigung, Signaturmodell und automatisierte Eingangsbestätigung dokumentiert.

**Abbruchkriterium:** Nummerierung startet erneut bei K 1, Originale werden überschrieben, Anlagen landen als ZIP in der Gerichtsmitteilung, Dateinamen enthalten Umlaute/über 80 Zeichen, eine unlesbare Anlage wird fingiert, das Modell behauptet eigenen Versand, ein GmbH-Beschäftigter nutzt ein beA, die Kanzlei umgeht Paragraf 130d ZPO oder eBO/Vertretung/Signatur bleiben ungeklärt.

## 1 Zahlungsklage Mietrückstand

**Eingang:** `testakten/mietrueckstand-meier-wilhelmstrasse/`

**Schritt 1 — Kaltstart:** `01-sap-akte-importieren` → liest `sap/sap-statusauszug.md`, `vertrag/mietvertrag.md`, `konto/mietkonto-fbl5n.md` und gibt die normalisierte Fall-JSON zurück.

**Schritt 2 — Mahnung:** `09-mietrueckstand-mahnung-erstellen` → produziert ein ausformuliertes Mahnschreiben mit Fälligkeit, Verzugsbeginn und anhand von Zugang, Zahlungsweg und Aktenstand kalendarisch bestimmter Frist; keine starre gesetzliche 14-Tage-Frist.

**Schritt 3 — Klage:** `20-zahlungsklage-mietrueckstand-erstellen` → produziert Klage mit Anträgen, Streitwert/Gerichtskosten-Prüfung, Sachverhalt, rechtlicher Würdigung, Anlagenverzeichnis.

**Erwarteter Output:** Klageentwurf > 2500 Zeichen, mit Verweis auf Paragraf 535 Abs. 2 BGB, Paragraf 23 Nr. 2a GVG, Paragraf 29a ZPO und Paragraf 79 Abs. 2 ZPO.

**Abbruchkriterium:** Skill ruft RVG-Klauseln auf oder zitiert Anwalts-Vollmacht (es gibt keinen Anwalt im Inhouse-Modell).

## 2 Räumungsklage mit Schonfristzahlung

**Eingang:** `testakten/raeumungsklage-kowalski-friedrichshain/`

**Schritt 1 — Kaltstart:** `01-sap-akte-importieren` → Renofa Sandra Berger als Bearbeiterin erkannt.

**Schritt 2 — Kündigung:** `13-fristlose-kuendigung-zahlungsverzug` mit Hilfsweise-Hinweis aus `14-ordentliche-kuendigung-pflichtverletzung` → fristlos+hilfsweise ordentliche Kündigung in einem Schriftsatz.

**Schritt 3 — Schonfristzahlung:** `27-schonfristzahlung-erkennen` → erkennt Jobcenter-Übernahme vom 27.07.2026; markiert fristlose Kündigung als unwirksam und prüft die ordentliche Kündigung gesondert nach Verschulden, Erheblichkeit, Frist und Sozialklausel-Risiko. In der Testakte bleibt die Räumung zum 31.01.2027 verfolgbar.

**Erwarteter Output:** Schriftsatz "Teilerledigterklärung Zahlung, Aufrechterhaltung Räumung" mit BGH-Anker VIII ZR 287/23, VIII ZR 145/24, VIII ZR 307/21, VIII ZR 91/20 und VIII ZR 6/04.

**Abbruchkriterium:** Skill erklärt ordentliche Kündigung pauschal als geheilt (gefährliche Falschauskunft).

## 3 Mieterhöhung mit Berliner Mietspiegel

**Eingang:** `testakten/mieterhoehung-becker-tempelhof/`

**Schritt 1 — Vorbereitung:** `28-mieterhoehung-bgb-558-vorbereiten` → liest letzten Stand, prüft Sperrfrist und Kappungsgrenze.

**Schritt 2 — Mietspiegel:** `04-belegmatrix-aufbauen` mit Mietspiegel-Datei `testakten/mietspiegel-berlin/berliner-mietspiegel-2026.md` → Tabelle 9.2, Zeile 85, mittlere Wohnlage und Spannenwerte erkannt.

**Schritt 3 — Verlangen + Klage:** `29-mieterhoehungsverlangen-text` produziert Verlangen, `30-zustimmungsklage-mieterhoehung` produziert Zustimmungsklage bei Teilverweigerung.

**Erwarteter Output:** Verlangen mit korrekter Wirksamkeit (Beginn des dritten Kalendermonats nach Zugang) und Kappungsgrenze 15 Prozent; Zustimmungsklage mit Streitwert 12 x monatlicher Differenzbetrag (Paragraf 41 Abs. 5 GKG) sowie gelber Freigabeampel, solange die Merkmalgruppen für eine Miete oberhalb des Mittelwerts nicht belegt sind.

**Abbruchkriterium:** Skill missachtet Berliner Kappungsgrenze oder berechnet Wirksamkeitstermin falsch.

## 4 Klageerwiderung und Replik

**Eingang:** Klageentwurf aus `testakten/mietrueckstand-meier-wilhelmstrasse/` plus simulierte Klageerwiderung mit Teilzahlung, angeblicher Minderung und pauschalem Bestreiten.

**Schritt 1 — Auswertung:** `37-klageerwiderung-auswerten` → erstellt Einwendungsmatrix mit Kategorie, Relevanz, Antwortlinie, Beweis und Risiko.

**Schritt 2 — Replik:** `38-replik-erstellen` → produziert ausformulierten Replikschriftsatz mit Anlagenplan aus `39-beweisangebot-anlagenplan`.

**Erwarteter Output:** Kein freier Theorievortrag, sondern Matrix + Schriftsatz. Minderung wird nicht pauschal abgetan, sondern nach Anzeige, Zeitraum, Ursache und Beweisrisiko strukturiert.

## 4.1 Kostenpfad nach erledigendem Ereignis

**Eingang:** Zahlungsklage wegen Mietrückstand, Zahlung des Mieters nach Klageeinreichung, aber vor Zustellung; hilfsweise zweites Szenario mit Zahlung nach Rechtshängigkeit.

**Schritt 1 — Chronologie/Einreichung:** `05-chronologie-fallakte` und `23-klage-egvp-bea-einreichen` → trennen Klageeinreichung, Zustellung, Zahlungseingang und Rechtshängigkeit.

**Schritt 2 — Kostenpfad:** `11-verzugsschaden-berechnen` und `37-klageerwiderung-auswerten` → erstellen Matrix mit Ereignis, Datum, vor/nach Rechtshängigkeit, vollständig/teilweise, Vorverzug, Forderungsstatus bei Einreichung, Wertstellung/Buchung, damaligem Kenntnisstand, Kausalität und Erforderlichkeit der Kosten, Paragraf 91a ZPO, Paragraf 269 Abs. 3 S. 3 ZPO und möglicher Kostenerstattungsklage.

**Schritt 3 — Schriftsatz:** `38-replik-erstellen` → erzeugt keinen normalen Zahlungs-Repliktext gegen die Aktenlage, sondern einen Entscheidungsvorschlag für Erledigung, Rücknahme, Kostenantrag oder materiell-rechtliche Kostenerstattung; ein Feststellungsantrag setzt eine gesonderte Zulässigkeitsprüfung voraus.

**Erwarteter Output:** BGH III ZR 156/12 wird als geprüfter Basisanker genannt. Nicht amtlich verifizierte Nutzerfundstellen werden nicht in den Quellenkanon übernommen. Bei unsicherem Kostenweg wird Skill `08-eskalation-an-anwalt` vorgeschlagen. Bei Verzug erst durch oder nach Klageeinreichung wird materiell-rechtliche Kostenerstattung nicht freigegeben. Eine unmittelbar vor Einreichung eingegangene, objektiv noch nicht erkennbare Zahlung erhält gelbe Ampel mit Buchungs- und Kenntnisprüfung, nicht automatisch grün.

**Abbruchkriterium:** Automatische Klagerücknahme oder Erledigungserklärung ohne Prüfung von Vorverzug, Rechtshängigkeit und tragfähigem prozessualem oder materiell-rechtlichem Kostenweg.

## 5 Kostenfestsetzung und Vollstreckung

**Eingang:** `testakten/vollstreckung-krueger-titel-teilzahlung/` (rechtskräftiges Versäumnisurteil, Kostenfestsetzungsantrag, Kostenfestsetzungsbeschluss, Teilzahlung ohne Tilgungsbestimmung); alternativ ein beliebiger anderer obsiegender Titel mit Gerichtskostenbelegen.

**Schritt 1 — KFA:** `46-kostenfestsetzung-antrag` → trennt Gerichtskosten, Auslagen, Quote und nicht erstattungsfähige interne Kosten.

**Schritt 2 — KFB:** `47-kostenbeschluss-pruefen` → prüft Betrag, Zinsbeginn, Zustellung und Rechtsbehelf.

**Schritt 3 — Vollstreckung:** `48-titulierte-forderung-vollstrecken` und `50-vollstreckungsakte-monitoring` → erstellen Forderungsupdate, Vollstreckungsauftrag und Wiedervorlagen.

**Schritt 4 — Unterliegen:** Bei abweisendem oder teilweise abweisendem AG-Urteil wird keine Vollstreckung gestartet; Skills 46 bis 50 setzen Unterliegenssperre, trennen positiv titulierte Teile ab und Skill 08 bekommt Rechtsmittel-Skizze mit Tenor, Frist, Beschwer, Wert, Zulassung, Kostenrisiko und Bearbeitungsauftrag an die Stammkanzlei.

**Schritt 5 — Eigener externer RA:** `08-eskalation-an-anwalt` → erstellt Auftrag, Budget-/Honorarcheck, Rechnungsvotum und Monierungstabelle für unscharfe Stunden-Narrative.

**Schritt 6 — Kostenrechtsbehelfe:** `21`, `46` und `47` → prüfen Streitwertfestsetzung, Kostenrechnung, KFA/KFB, Frist, Beschwer, Berichtigung und Beschwerde als Entscheidungsvorlage.

**Erwarteter Output:** Kosten- und Vollstreckungsakte mit Titel, Betrag, Zinsen, Zahlungen, Tilgungsjournal, nächster Maßnahme und Datenschutzvermerk. Bei Unterliegen stattdessen rote Ampel, Fristenkontrolle und anwaltliche Fortsetzungsprüfung; bei externer Kanzlei zusätzlich Rechnungsvotum und klare Monierungspunkte.

## 6 Qualitätsloop v1.3.0

Dieser Smoke-Test prüft die zehn Nachschärfungen aus dem v1.3.0-Qualitätsdurchgang.

**Eingang:** beliebige Testakte plus unsauberer DMS-/SAP-Export, simulierte Klageerwiderung und späterer KFB.

**Prüfpunkte:**

1. `06-fallziel-renofa-triage` gibt Fallziel, Rollenbefugnis und Entscheidungsampel aus, keine externe-Mandanten-Sprache.
2. `07-rdg-grenzen-check` behandelt gerichtliches Mahnverfahren nur als optionale Abzweigung.
3. `25-raeumungsfrist-vollstreckung` verlangt Räumungstitel aus Urteil oder Vergleich, keinen Vollstreckungsbescheid.
4. `33-dokumentenmix-ocr-sichten` markiert Dubletten, Versionen, OCR-Qualität und Datenschutzhinweis.
5. `34-sap-excel-pdf-normalisieren` gibt Konfliktzeilen aus, wenn SAP, Excel und PDF voneinander abweichen.
6. `35-sap-belegluecken-klaeren` sperrt Klagefreigabe bei roten Pflichtlücken.
7. `37-klageerwiderung-auswerten` und `38-replik-erstellen` führen Frist, Vorfrist, gerichtliche Hinweise und neue Anlagen.
8. `39-beweisangebot-anlagenplan` verknüpft jede Tatsache mit Beweis, Anlage, Version und offener Beschaffung.
9. `46-kostenfestsetzung-antrag` und `47-kostenbeschluss-pruefen` trennen KFA, KFB, Quote, Zinsbeginn und interne nicht erstattungsfähige Kosten.
10. `48`, `49` und `50` dokumentieren Vollstreckungskosten, zulässige Drittauskünfte, Monitoring und nächste Maßnahme.

**Erwarteter Output:** Alle genannten Skills geben Ampel, Fristen oder Monitoringtabellen aus, ohne das gerichtliche Mahnverfahren als Standardpfad zu erzwingen.

## 7 Qualitätsloop v1.4.0

Dieser Smoke-Test prüft die zweite Serie von zehn Nachschärfungen.

**Eingang:** SAP-Statusauszug, Mietkonto, Mietvertrag, unvollständige DMS-Belege, geplanter Klageentwurf, Zahlungsplan und spätere Kündigungs-/Vollstreckungssituation.

**Prüfpunkte:**

1. `01-sap-akte-importieren` gibt Quelle, Sicherheit, Konflikt und Nacharbeit je Pflichtfeld aus.
2. `02-mietakte-rekonstruieren` markiert Vertragsversionen und rote Lücken bei Widerspruch zu SAP.
3. `03-kontoauszug-mietkonto-auslesen` trennt Buchungsdatum, Wertstellung, Storno, Guthaben und Tilgungsbestimmung.
4. `04-belegmatrix-aufbauen` führt Beweisstatus und nächste Beschaffung.
5. `05-chronologie-fallakte` weist Fristwirkung, Beleg und Sicherheit je Ereignis aus.
6. `07-rdg-grenzen-check` vermeidet pauschales RDG-analog und prüft Aussenwirkung sowie Paragraf 10 RDG.
7. `11-verzugsschaden-berechnen` setzt keine internen Renofa-Kosten als Anwaltskosten an.
8. `21-klage-streitwert-gerichtskosten` übernimmt keine ungeprüften Beispiel-Gerichtskosten.
9. `23-klage-egvp-bea-einreichen` behauptet keinen pauschalen Versandweg, sondern prüft Postfach, Signatur und sicheren Übermittlungsweg.
10. `32-datenschutz-mieterdaten` behandelt Auskunftei-Meldungen nicht als Standard und verlangt Datenschutzfreigabe.

**Erwarteter Output:** Quellenstatus, Fristen, Ampel und Nacharbeit sind sichtbar; keine ungeprüften Kosten-, Versandweg- oder Datenschutzbehauptungen.

## 8 Qualitätsloop v1.5.0

Dieser Smoke-Test prüft die dritte Serie von zehn Nachschärfungen mit Schwerpunkt Räumung, Berliner Modell, Sozialwiderspruch und Mieterhöhung.

**Eingang:** Räumungs- oder Mieterhöhungsakte mit SAP-Auszug, Mietvertrag, Mietkonto, Zustellnachweisen, Mieterwiderspruch und Mietspiegel-Unterlage.

**Prüfpunkte:**

1. `16-widerspruch-mieter-pruefen` gibt Frist, Form, Härtegründe, Belege, Vergleichsoption und RA-Eskalation aus.
2. `22-zustaendigkeit-amtsgericht-pruefen` nennt Norm-Anker, Lageort, aktuelle offizielle Gerichtsquelle und Abrufdatum.
3. `24-raeumungsklage-erstellen` trennt Zahlungs- und Räumungsstreitwert und prüft Schonfrist sowie Sozialwiderspruch.
4. `26-berliner-modell-raeumung` wählt das Berliner Modell nicht automatisch, sondern verlangt Kosten-, Inventar-, Verwahrungs- und Risikocheck.
5. `28-mieterhoehung-bgb-558-vorbereiten` prüft Mietspiegel-Fassung, Anwendungsbereich und Rechenblatt.
6. `29-mieterhoehungsverlangen-text` verlangt keine Zielmiete über der berechneten Vergleichsmiete und führt ein Zugangskonzept.
7. `30-zustimmungsklage-mieterhoehung` nutzt Paragraf 41 Abs. 5 GKG und die Jahresdifferenz aus dem geprüften Rechenblatt.
8. `31-kappungsgrenze-mietpreisbremse` unterscheidet Mietspiegelwert, Cap und Zielmiete ohne widersprüchliche Spannenlogik.
9. `forderungsmanagement-grosser-prompt.md` und `forderungsmanagement-kleiner-prompt.md` spiegeln dieselben Räumungs- und Mieterhöhungsregeln.
10. Gerichtliches Mahnverfahren bleibt optionale Abzweigung nach Rückfrage und wird nicht als Standardpfad erzwungen.

**Erwarteter Output:** Skill- und Prompt-Antworten enthalten Rechenblatt, Fristen, Quellenstatus, Zugangsnachweis und Eskalationspunkte; keine automatische Berliner-Modell- oder Mahnverfahren-Entscheidung.

## 9 Qualitätsloop v1.6.0

Dieser Smoke-Test prüft die vierte Serie von zehn Nachschärfungen mit Schwerpunkt Kostenfestsetzung, KFB, Vollstreckung, Drittauskunft und Monitoring.

**Eingang:** Urteil oder Vergleich, KFA-Entwurf, KFB, Zustellnachweis, Zahlungen nach Titel, GV-Protokoll, bekannte SEPA-Bankverbindung und möglicher Insolvenz- oder P-Konto-Hinweis.

**Prüfpunkte:**

1. `46-kostenfestsetzung-antrag` verlangt Kostengrundentscheidung, Quote, Belege, Zahlungsabgleich und Zinsantrag nach Paragraf 104 Abs. 1 S. 2 ZPO.
2. `46-kostenfestsetzung-antrag` sortiert interne Personal-, SAP-, DMS- und Konzernverwaltungskosten aus.
3. `47-kostenbeschluss-pruefen` wartet nicht pauschal auf Bestandskraft, sondern prüft Vollstreckbarkeit, Rechtsbehelfsfrist, Zustellung und Paragraf 798 ZPO.
4. `47-kostenbeschluss-pruefen` bildet Abweichungen zwischen KFA und KFB als Entscheidungsvorlage ab.
5. `48-titulierte-forderung-vollstrecken` trennt Titel, Kosten, Zinsen und Zahlungen je Titel und dokumentiert Klausel, Zustellung und Wartefristen.
6. `48-titulierte-forderung-vollstrecken` stoppt bei Insolvenz oder Vollstreckungsverbot und eskaliert.
7. `49-kontoermittlung-und-drittauskunft` nutzt Drittauskünfte nur über gesetzliche Wege und übernimmt keine veraltete 500-EUR-Schwelle ungeprüft.
8. `49-kontoermittlung-und-drittauskunft` ersetzt Schuldnerverzeichnis, Melderegister oder Paragraf 802l ZPO nicht durch freie Internetrecherche.
9. `50-vollstreckungsakte-monitoring` führt Tilgungsjournal, notwendige Vollstreckungskosten, Wiedervorlagen, Titel-/Zinsverjährung und Datenschutzstatus.
10. `forderungsmanagement-grosser-prompt.md` und `forderungsmanagement-kleiner-prompt.md` enthalten dieselben Vollstreckungsstopps und dieselbe offene Tilgungslogik.

**Erwarteter Output:** Nach-Titel-Antworten enthalten Vollstreckbarkeitscheck, Fristen, Tilgungsjournal, Datenschutzstatus und nächste Maßnahme; keine informelle Konto- oder Arbeitgeberrecherche.

## 10 Qualitätsloop v1.7.0

Dieser Smoke-Test prüft die fünfte Serie von zehn Nachschärfungen mit Schwerpunkt Mieterklage, Vertreterkorrespondenz, Betriebskosten und Hausverwaltung.

**Eingang:** Mietervereinsschreiben oder Mieterklage mit Mietminderung, Betriebskostenwiderspruch, Kautionsforderung, unklarem Vertreterstatus, Hausverwaltungsnotizen und DMS-Belegen.

**Prüfpunkte:**

1. `42-mieterklage-verteidigen` erfasst Zustellung, Klageerwiderungsfrist, Vorfrist und Anspruchsziel.
2. `42-mieterklage-verteidigen` trennt Mangelanzeige, Zugang, Zeitraum, Ursache, Abhilfemöglichkeit, Beweislast und Sachverständigenrisiko.
3. `42-mieterklage-verteidigen` prüft Kaution mit Abrechnungsreife, Gegenforderungen, Betriebskostenrisiko und Verrechnungsstand.
4. `43-mieterverein-anwalt-korrespondenz` gibt bei unklarem Vertreterstatus keine personenbezogenen Detaildaten heraus.
5. `43-mieterverein-anwalt-korrespondenz` erfasst Vergleichs- und Teilzahlungsangebote ohne Anerkenntnis und mit Freigabecheck.
6. `44-betriebskosten-rueckstand-streit` berechnet Abrechnungsfrist und Einwendungsfrist nach Paragraf 556 Abs. 3 BGB getrennt.
7. `44-betriebskosten-rueckstand-streit` trennt formelle Wirksamkeit, materielle Fehler, Belegeinsicht, Zahlung und Verjährung.
8. `44-betriebskosten-rueckstand-streit` filtert nicht umlagefähige Verwaltungs-, Instandhaltungs- und Instandsetzungskosten.
9. `45-hausverwaltung-schnittstelle` fragt beweisorientiert ab: Wer hat was wann gesehen, dokumentiert, fotografiert oder versandt?
10. `forderungsmanagement-grosser-prompt.md` und `forderungsmanagement-kleiner-prompt.md` enthalten dieselben Frist-, Beweis-, Daten- und Hausverwaltungsregeln.

**Erwarteter Output:** Matrix, Fristentabelle, Belegeinsichtsstatus, Datenschutzcheck, beweisorientierter Hausverwaltungsauftrag und ausformulierter Antwort- oder Schriftsatzentwurf.

## 11 Release-Asset-Abnahme

Dieser Smoke-Test prüft, ob ein Release für eine große Immobilienabteilung praktisch auslieferbar ist.

**Eingang:** Release-Seite des aktuellen Tags.

**Prüfpunkte:**

1. `forderungsmanagement-immobilien.zip` ist vorhanden und lässt sich als Plugin-Upload verwenden.
2. `schriftsatzwerkstatt-bea.zip` ist vorhanden und lässt sich unabhängig vom Fachplugin verwenden.
3. `marketplace.json` ist vorhanden und enthält dieselbe Version wie beide Plugin-Manifeste.
4. Beide Skill-Markdown-ZIPs sind vorhanden; sie enthalten jeweils das Plugin-README und exakt die Skills ihres Plugins.
5. Pro Testakte gibt es ein Arbeits-ZIP.
6. Kein Arbeits-ZIP enthält Markdown oder andere Formate als DOCX, XLSX und PDF; kein Testakten-ZIP enthält Unterordner.
7. Pro Testakte gibt es ein Einzel-PDF-ZIP mit einzeln benannten PDF-Unterlagen.
8. Pro Testakte gibt es ein direktes `testakte-<slug>-gesamt.pdf`; es ist vollständig lesbar und bytegleich mit der getrackten Quelle, wird aber im Arbeits-ZIP nicht gedoppelt.
9. `alle-testakten.zip` ist als einziges Sammel-Arbeits-ZIP vorhanden.
10. `alle-testakten-einzel-pdfs.zip` ist als einziges Sammel-ZIP für Einzel-PDFs vorhanden.
11. Alte doppelte Sammelpaketnamen sind nicht mehr vorhanden.
12. `testakten-release-index.json` ist vorhanden und nennt Gesamt-PDF, Arbeits-ZIP, Einzel-PDF-ZIP und Sammel-Assets ohne doppelte Dateinamen.
13. `scripts/validate-testakten-release-zips.py` läuft gegen die heruntergeladenen Release-Dateien ohne Fehler.
14. `scripts/validate-release-zips.py` läuft gegen die heruntergeladenen Release-Dateien ohne Fehler.
15. `scripts/validate-testakten-financial-consistency.py` läuft vor dem Release ohne Fehler.
16. `scripts/validate-testakten-stammdaten.py` bestätigt neben Vertrags- und Personendaten auch, dass jede DMS-Trefferzahl zur Dokumenttabelle passt und kein Dokument nach dem angegebenen Exportzeitpunkt liegt.
17. `immobilien-forderungsmanagement-dokumentation.zip` enthält den vollständigen getrackten Repo-Inhalt ohne `.git` oder `dist`; relative Links zwischen Root-README, beiden Plugin-READMEs, allen 59 Skills, Referenzen, Testakten und Smoke-Tests funktionieren nach dem Entpacken.
18. `release-katalog.md` verlinkt jedes veröffentlichte Asset; `checksums-sha256.txt` enthält für jedes übrige Asset genau eine passende SHA-256-Prüfsumme.

**Erwarteter Output:** Release ist ohne Repo-Klon nutzbar: Plugin-ZIP, Marketplace-Datei und Testaktenpakete können direkt an Pilotgruppe oder interne Plugin-Verwaltung übergeben werden.

**Abbruchkriterium:** Eine Testakte hat weniger als drei direkte Downloadformen, ein Gesamt-PDF weicht von der Repo-Quelle ab oder der Asset-Index fehlt.

## 12 Deployment-Readiness in der Fachabteilung

Dieser Smoke-Test prüft, ob eine Pilotgruppe das Plugin ohne Entwicklererklärung starten kann.

**Eingang:** `README.md`, `forderungsmanagement-immobilien/README.md`, aktueller Release und eine Testakte als Einzel-PDF-ZIP.

**Prüfpunkte:**

1. README erklärt, welches Release-Asset für die Plugin-Installation genutzt wird.
2. README erklärt die drei Testakten-Downloadformen.
3. README nennt Pilotgruppe, Rollen, Freigabegrenzen, Datenschutz und Vier-Augen-Prinzip.
4. Plugin-README nennt die benötigten Unterlagen aus SAP, DMS, Mietvertrag, Mietkonto, Korrespondenz und Gericht.
5. Plugin-README beschreibt Tagesmuster für Mietrückstand, Räumung, Mieterhöhung, Prozessreaktion, Kostenfestsetzung und Vollstreckung.
6. Plugin-README erklärt den Autostart ohne Skillauswahl: neuer Fall, Projektordner oder Upload-Bundle führt zu Skill `33`.
7. Die Skill-Übersicht zeigt stabile Skill-IDs und sprechende Arbeitsnamen, ohne Ordner umzubenennen.
8. Kontrollpunkte vor Versand sind konkret genug für Renofas und Rechtsfachwirt:innen.
9. Kein Text vermittelt, dass Dokumente ungeprüft an Gericht, Mieter, Gerichtsvollzieher oder Gegenseite versandt werden dürfen.
10. Live-Daten werden im Training nicht vorausgesetzt.
11. Interne 10.000-EUR-Grenze wird als Organisations- und Freigabekriterium beschrieben.
12. Landgericht, Berufung, Revision, Insolvenz, Strafrecht und Sachverständigenthemen lösen Eskalation aus.
13. Plugin-README enthält kopierbare Nutzersätze für neuen Fall, SAP-Statusauszug, fertige Fallkarte, Gerichtspost, Gerichtspaket und Kosten/Vollstreckung.
14. Jeder kopierbare Nutzersatz nennt den erwarteten Startskill oder Zielpfad.
15. Root-README enthält einen Start-in-30-Sekunden-Abschnitt mit Alltagssätzen und erwarteter erster Ausgabe.
16. Plugin-README und Bedienführungsreferenz beschreiben den schnellen Zwei-Phasen-Start für große Uploads.
17. Plugin-README erklärt die getrennte Freigabekarte, den menschlichen Freigabeschritt und das Erlöschen der Freigabe bei relevanten Änderungen.
18. Root-README führt direkt zu Plugin-Menü, Testakten, Prompt-Quellen, Referenzen, Smoke-Tests, Release-Katalog und Prüfsummen.
19. Im Plugin-README öffnet jede technische Skill-ID direkt die zugehörige `SKILL.md`.
20. Jede Einzelakten-README führt zurück zur Testakten-Übersicht, zum Plugin-Menü, zum Skill-Index und zu den zentralen Downloads.
21. `scripts/validate-readme-navigation.py` läuft ohne Fehler und die Offline-Dokumentation lässt sich ohne GitHub-Verzeichnisnavigation lesen.
22. Root- und Plugin-README verlinken ERV-/eBO-/beA-Referenz und Rechtsprechungsradar; der Gerichtspaket-Startauftrag führt zu Skills `39` und `23` und verlangt dort zuerst das Rollengate.
23. `SKILLS.md` führt pluginübergreifend zu allen 59 Skilldateien; die Detailseiten nennen nur tatsächlich veröffentlichte Assets.
24. `alle-skills-markdown.zip` enthält direkt Plugin-Ordner, README-Indizes und `SKILL.md`-Dateien, aber keine verschachtelten ZIP-Dateien.

**Erwarteter Output:** Ein fachlicher Pilot kann mit Release-Link, README, Plugin-README und Testaktenpaketen starten.

**Abbruchkriterium:** Pilotgruppe braucht Repo-Insiderwissen, um Plugin, Prompt-Skills, Testakten oder den richtigen Startauftrag zu finden.

## 13 Training mit Testakten

Dieser Smoke-Test prüft, ob die Testakten als Schulungsstrecke funktionieren.

**Eingang:** Einzel-PDF-ZIPs und Arbeits-ZIPs aller Testakten.

**Prüfpunkte:**

1. Mietrückstand Meier deckt Intake, Forderungsaufstellung, Belegmatrix und Zahlungsklage ab.
2. Räumung Kowalski deckt Kündigung, Zustellung, Räumung, Schonfristzahlung und Erledigungsreaktion ab.
3. Mieterhöhung Becker deckt Paragraf 558 BGB, Mietspiegel, Kappungsgrenze und Zustimmungsklage ab.
4. Mietrückstand Lange deckt versehentliche Nichtzahlung, Bankwechsel, gelbe Ampel und Kulanz-Ratenplan ab.
5. Mietrückstand Demir deckt absichtliche Nichtzahlung, rote Ampel, Kündigung, Zahlung und Räumung ab.
6. Nebenkosten Braun deckt laufend gezahlte Miete, offene Betriebskosten-Nachzahlung, Einwendung, Belegeinsicht samt Zahlungsbelegen und den roten Einreichungsstopp bis zur ordnungsgemäßen Einsicht ab.
7. Ratenplan Riedel deckt gebrochenen Kulanzplan, Wiedervorlage, Kulanzende und Restforderung ab.
8. Vollstreckung Krüger deckt Kostenfestsetzung, Titelverwaltung, Tilgungsreihenfolge nach Paragraf 367 BGB, Vollstreckungsauftrag mit Vermögensauskunft und Monitoring ab.
9. Mietspiegel Berlin kann als Querschnittsmaterial in Mieterhöhungsfällen verwendet werden.
10. Einzel-PDF-ZIPs bilden den realistischen Upload-Mix flach und ohne Gesamt-PDF-Dublette ab.
11. Gesamt-PDFs ermöglichen schnelle Sichtprüfung.
12. Arbeits-ZIPs erhalten die fachliche Herkunft über Präfixe im Dateinamen, ohne Unterordner anzulegen.
13. Sämtliche ZIP-Dateinamen bestehen aus ASCII-Zeichen und kollidieren auch auf Dateisystemen ohne Unterscheidung der Groß-/Kleinschreibung nicht.
14. Interne Aktennotizen bleiben auch dann DOCX, wenn ihr Dateiname Wörter wie `Jobcenter` oder `E-Mail` enthält.
15. Einzel-PDFs beginnen unmittelbar mit dem Aktenstück und zeigen weder Markdown-Quellpfad noch den technischen Footer `Arbeitsakte: Einzel-PDF`.
16. Die Dateimetadaten erzeugter DOCX/XLSX folgen dem Dokument- oder Unterschriftsdatum und übernehmen kein Geburtsdatum.
17. Symlinks sowie versehentlich übergroße Einzeldateien oder Aktenbestände brechen den Paketbau kontrolliert ab.
18. Schulungsablauf in der README ist zeitlich und fachlich nachvollziehbar.

**Erwarteter Output:** Eine Trainingsleitung kann ohne weitere Datei-Erstellung einen halben Schulungstag für die Forderungsmanagement-Abteilung durchführen.

## 14 Prompt- und Skill-Konsistenz

Dieser Smoke-Test prüft, ob Steuerungsprompts, Skills und README denselben Betriebsmodus beschreiben.

**Eingang:** `forderungsmanagement-grosser-prompt.md`, `forderungsmanagement-kleiner-prompt.md`, Plugin-README und eine beliebige Testakte.

**Prüfpunkte:**

1. Der Große Prompt startet mit Intake, nicht sofort mit Klage.
2. Der Kleine Prompt nennt Lückenliste, Fristenkontrolle, Quellenstatus und nächsten Schritt.
3. Beide Prompts beschreiben Mahnverfahren als optionale Abzweigung.
4. Beide Prompts behandeln Kostenfestsetzung und Vollstreckung nach Titel.
5. Beide Prompts verlangen Stopps bei Insolvenz, Berufung, Sachverständigen-Großrisiko oder ungesicherter Rechtsquelle.
6. Plugin-README beschreibt dieselben Kernpfade wie die Prompts.
7. Skills 01 bis 05 liefern Intake-Grundlagen, Skills 46 bis 50 decken Nach-Titel-Arbeit ab.
8. Dokumententwürfe bleiben fachlich freigabepflichtig.
9. Beide Prompts unterscheiden Vollintake und Delta-Fortschreibung; Neuzugang entwertet überholte Salden, Fristen oder Entwürfe sichtbar.
10. Beide Prompts führen BGH VIII ZR 222/15 zur Rechtzeitigkeit der Wohnraummietzahlung und das Freigabegate mit dem Status `ENTWURF - NICHT VERSENDEN/EINREICHEN`.
11. Beide Prompts erzeugen autark ein Gerichtspaket mit fortlaufenden K-/B-Anlagen, Einzel-PDFs, ASCII-Dateinamen, ERV-/Signaturgate und Eingangsnachlauf; sie verweisen dafür nicht bloß auf Skills.

**Erwarteter Output:** Keine widersprüchliche Steuerung zwischen README, Prompt und Skill-Set.

## 14.1 Lebensnahe Testakten mit DMS-Beifang

Dieser Smoke-Test prüft, ob die seit v5.11.0 ergänzten unaufgeräumten Aktenstücke tatsächlich als Trainingsmaterial wirken und nicht als Fehler im Kernfall behandelt werden.

**Eingang:** Die neun Fach-Testakten mit den zusätzlichen E-Mail-Nachträgen, Rückrufnotizen, DMS-/DocuWeb-Hinweisen, unklaren Verwendungszwecken, angekündigten Anlagen und Vollstreckungsrückläufen.

**Prüfpunkte:**

1. Jede einzelne Akten-README nennt die zusätzlichen Aktenstücke im Abschnitt `Akte`, `Dateien` oder `Inhalt`.
2. Die zusätzlichen Aktenstücke laufen in Arbeits-ZIP, Gesamt-PDF und Einzel-PDF-ZIP mit.
3. `33-dokumentenmix-ocr-sichten` erstellt ein Dokumenteninventar mit DMS-Beifang, Dubletten, Dateiversion, OCR-/Scanqualität und Datenschutzklasse.
4. `04-belegmatrix-aufbauen` trennt beweisfähige Unterlagen von bloßen Behauptungen, angekündigten Anlagen, Dubletten und irrelevanten Beifängen.
5. `05-chronologie-fallakte` übernimmt nur datierbare sichere Ereignisse als harte Chronologiepunkte und markiert Rückrufe oder E-Mail-Behauptungen mit Quellenstatus.
6. `06-fallziel-renofa-triage` eskaliert nicht automatisch, sondern unterscheidet Kulanzfall, klagereife Forderung, rote Kündigungsakte und Nach-Titel-Vollstreckung.
7. Die neuen Unschärfen verändern keine kanonischen Stammdaten, keine Kernsalden und keine bereits validierten Betriebskosten- oder Titelbeträge.

**Erwarteter Output:** Dokumenteninventar, Beifang-Liste, Rückfragen, Quellenstatus und Ampel entstehen vor jedem Entwurf. Kein Skill erzeugt aus einer bloßen Mieterbehauptung oder einem DMS-Duplikat eine neue Forderung.

## 14.1.1 Schimmelklage Schulz verteidigen

**Eingang:** Arbeits-ZIP der Akte `mieterklage-schimmel-schulz-verteidigung`.

**Prüfpunkte:**

1. Zustellung am 14.07.2026, Notfrist zur Verteidigungsanzeige am 28.07.2026 und Klageerwiderungsfrist am 11.08.2026 stehen vor jeder Ursachen- oder Quotenprüfung.
2. Sichtbarer Befall am 18.02.2026 wird nicht pauschal bestritten; Beginn, Dauer, Ausmaß, Gebrauchsbeeinträchtigung, Ursache und Quote werden getrennt geführt.
3. BGH VIII ZR 67/18 und VIII ZR 271/17 werden nur für bauzeitübliche Wärmebrücken, Schimmelgefahr und fallbezogene Lüftungszumutbarkeit verwendet, nicht als automatische Abweisung bei tatsächlichem Befall.
4. BGH VIII ZR 155/11 verhindert eine überspannte Substantiierungsanforderung an technische Ursache oder Minderungsquote.
5. Mieter-Fotovorschau, Originalfotos des technischen Dienstes, Loggerauswertung, Logger-Rohdaten, Messlücke, Fensterunterlagen und Möbelabstand erhalten getrennte Quellenstatus.
6. Die Klageforderung wird rechnerisch als fünf Monate mal 20 Prozent aus 1260,00 EUR, mithin 1260,00 EUR, kontrolliert; die Rechnung beweist weder Quote noch Zeitraum.
7. Der Entwurf bleibt rot, bis Beweis-, Anlagen-, Vertretungs- und Versandfreigabe vollständig vorliegen.

**Erwarteter Output:** Fristenkarte, Anspruchsmatrix für Beseitigung und Rückzahlung, Beweismatrix, konkrete Beschaffungsaufträge, freizugebender Klageerwiderungsentwurf und anschließend ein technisch getrenntes Gerichtspaket.

## 14.2 Juristische Regressionen in Kernpfaden

Dieser Smoke-Test verhindert, dass bereits bereinigte Fehler in den besonders haftungsträchtigen Pfaden zurückkehren.

**Eingang:** Skills 08, 09, 12, 13, 16 bis 18, 22, 25 bis 30, 40, 41, 44 und 46 bis 49 sowie beide autarken Prompts.

**Prüfpunkte:**

1. Mahnung und letzte Frist behaupten keine starre gesetzliche 14-Tage-Frist und keine internen Bearbeitungs- oder Kündigungskosten.
2. Die Kündigungsheilung verlangt die vollständige Befriedigung der fälligen Miete und einer fälligen Nutzungsentschädigung oder eine wirksame Verpflichtung einer öffentlichen Stelle; eine bloße Zahlungsankündigung genügt nicht.
3. Der Sozialwiderspruch nach § 574 BGB wird nicht auf die außerordentliche Kündigung übertragen und bleibt bei einem Grund nach § 543 Abs. 2 Satz 1 Nr. 3 BGB ausgeschlossen.
4. Das Mahnverfahren trennt Ausschlüsse nach § 688 ZPO, Mahngericht nach § 689 ZPO, späteres Streitgericht, Abgabeantrag nach § 696 ZPO und Anspruchsbegründung nach § 697 ZPO.
5. Ein erwartbarer Widerspruch ist nur ein Wirtschaftlichkeitsfaktor, kein gesetzliches Hindernis des Mahnverfahrens.
6. Die Verjährungsprüfung verbindet § 204 Abs. 1 Nr. 3 BGB mit der demnächst erfolgenden Zustellung nach § 167 ZPO.
7. Der ausschließliche Gerichtsstand nach § 29a ZPO wird nur nach Prüfung der Ausnahmen des Absatzes 2 angewandt.
8. Berufung wird nach § 511 Abs. 2 ZPO mit einer Beschwer über 1.000 EUR oder Zulassung geprüft; die Fristen nach §§ 517 und 520 ZPO bleiben getrennt.
9. Die Zustimmungsklage bildet Zugang, Überlegungsfrist, Wirksamkeit, Klagefrist von drei weiteren Monaten und die Heilung nach § 558b Abs. 3 BGB kalendarisch ab.
10. Belegeinsicht bei Betriebskosten umfasst nach BGH VIII ZR 118/19 auch Zahlungsbelege; eine berechtigt verweigerte Einsicht löst nach BGH VIII ZR 189/17 einen vorläufigen Einreichungsstopp aus.
11. Das Berliner Modell trennt Gerichtsvollzieherinventar, Entfernung und Verwahrung durch die Vermieterin, Monatsfrist, Rückgabe, Verwertung/Vernichtung und Haftung nach § 885a ZPO.
12. Räumungsfrist und Vollstreckungsschutz nennen die Zweiwochenfristen und die Höchstgrenze des § 721 Abs. 5 ZPO; die fachliche Prüfung ersetzt keine erfundene Dreiwochenfrist.
13. Der Urkundenprozess bildet §§ 592 bis 600 ZPO einschließlich Vorbehaltsurteil, Nachverfahren und Abstandnahme ab.
14. Prozessvergleich, Kostengrundentscheidung, Kostenfestsetzung und materieller Kostenerstattungsanspruch bleiben begrifflich und rechtlich getrennt.
15. Vollstreckung beginnt erst nach titelbezogener Prüfung von Klausel, Zustellung, besonderen Eintrittsnachweisen und einer Wartefrist nach § 798 ZPO, soweit sie für den konkreten Titel gilt.

**Erwarteter Output:** `scripts/validate-legal-anchors.py` läuft ohne Fehler; Prompts, Skills, Referenzen und Testakten geben in den Kernpfaden dieselbe Rechtslage wieder.

## 14.3 Tatsachenvortrag und Argumentationskontrolle

Dieser Smoke-Test prüft, ob Fachskills aus heterogenen Akten einen belastbaren Schriftsatz statt einer bloßen Dokumentenzusammenfassung erzeugen.

**Eingang:** Arbeits-ZIP der Akte `mietrueckstand-meier-wilhelmstrasse` einschließlich Mietkonto, SAP-Auszug, Teilzahlungs-Buchungsklärung und Einwurfprotokoll.

**Prüfpunkte:**

1. Vor dem Entwurf entsteht eine Tatsachenkarte für Vertrag, Miethöhe, Fälligkeit, Zahlung, Tilgung, Rest, Verzug, Einwendung, Prozessstatus, Beweislast und Beweis.
2. Mietkonto, SAP-Saldo und Buchungsklärung werden als getrennte Quellen geführt; ein Systemwert ersetzt weder den Zahlungsvortrag noch den Kontobeleg.
3. Die Teilzahlung wird mit Buchungsdatum, Wertstellung, Verwendungszweck und Tilgungsfolge eingeordnet.
4. Jeder streitige erhebliche Tatsachensatz erhält unmittelbar ein Beweisangebot. Ein Anlagenverweis ohne Tatsachensatz und ein Zeugenname ohne Wahrnehmungsthema werden zurückgewiesen.
5. Der Entwurf folgt der Kette Antrag, Tatbestandsmerkmal, konkrete Tatsache, Prozessstatus, Beweislast, Beweis, Subsumtion, Gegeneinwand und Rechtsfolge.
6. Widersprüchlicher oder geänderter Vortrag wird aufgeklärt und ausdrücklich eingeordnet; er wird nicht allein wegen des Widerspruchs übergangen.
7. Die Schlusskontrolle stimmt Antrag, Rechenblatt, Tatsachenkarte, Anlagenmanifest, Frist und Freigabestatus gegeneinander ab.

**Erwarteter Output:** Vollständig formulierter, quellennaher Klageentwurf mit Tatsachenkarte, Monatsrechnung, Beweisangeboten, Einwendungsbehandlung, Lückenliste und Freigabekarte.

## 14.4 Inhaltstreue der beA-Konvertierung

**Eingang:** Inhaltlich freigegebener DOCX-Schriftsatz mit einem bezifferten Antrag, einem Termin und drei Anlagen; während der Konvertierung wird testweise eine Zahl im PDF verändert.

**Prüfpunkte:**

1. Quellhash, Konvertierungsprofil, Ausgabehash, Seitenzahl und Sichtstatus werden für jede Datei protokolliert.
2. Der Drei-Wege-Abgleich Quelle, PDF und gerendertes Seitenbild erkennt die veränderte Zahl.
3. Die Werkstatt setzt den Vorgang auf Rot, verwirft die Arbeitskopie und fordert eine neue Konvertierung aus der unveränderten Quelle.
4. Weder automatische Reparatur noch manuelle Textkorrektur im PDF ist zulässig.
5. Erst eine inhaltlich identische Neuausgabe darf in den finalen Preflight gelangen.

**Erwarteter Output:** Keine technische Freigabe bei inhaltlicher Abweichung; vollständiger Delta- und Fehlernachweis im Prüfprotokoll.

## 15 Cloud-Co-Work-Standalone-Skills

Dieser Smoke-Test prüft, ob Werkstattprompt und Schnellstartprompt auch ohne komplettes Plugin als einzelne Skills nutzbar sind.

**Eingang:** Release-Assets `forderungsmanagement-immobilien-grosser-prompt-skill.zip`, `forderungsmanagement-immobilien-grosser-prompt-skill.md`, `forderungsmanagement-immobilien-kleiner-prompt-skill.zip` und `forderungsmanagement-immobilien-kleiner-prompt-skill.md`.

**Prüfpunkte:**

1. Beide ZIPs enthalten exakt eine Datei `SKILL.md` an der ZIP-Wurzel.
2. Die jeweilige `SKILL.md` ist inhaltlich identisch mit dem gleichnamigen Markdown-Asset.
3. Die YAML-Frontmatter parst fehlerfrei und enthält nur `name` und `description`.
4. Die `description` ist single-quoted YAML, bleibt unter 1024 Zeichen und enthält keine spitzen Klammern, keine eingebetteten doppelten Anführungszeichen, keine Komma-Zahlen und keine verbotenen Web-Auslese-Anglizismen.
5. Der Schnellstartprompt bleibt unter 7.500 Zeichen.
6. Der vertiefte Werkstattprompt bleibt für große Kontexte handhabbar; seine erzeugte Standalone-`SKILL.md` hat einschließlich Frontmatter höchstens 30.000 Zeichen.
7. Beide Skills beschreiben dieselbe Zielgruppe: starke Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement.
8. Beide Skills liefern Intake, Tabelle, Lückenliste, Fristen, Quellenstatus, Eskalation und nächsten Schritt.
9. Kein Standalone-Skill verweist auf eine Datei, die nur im Repo-Root existiert und im Einzel-Skill-ZIP fehlt.
10. Der volle Produktivpfad bleibt das Plugin-ZIP; Standalone-Skills sind Fallback für Umgebungen ohne Plugin-Installation.
11. Derselbe Ein-Satz-Auftrag wie im Plugin startet beide Standalone-Skills ohne Workflow- oder Skillauswahl.
12. Beide beginnen mit Modus, Akten-ID/Stichtag, Frist/Quelle, Ampel/Grund, gelesen/gesamt, Kernlücken und Feld `Jetzt` und arbeiten danach ohne Befehl `weiter` fort.
13. Der Werkstattprompt führt ohne manuelle Skillwahl durch Eingang, Frist, Rekonstruktion, Rechtsroute, Entscheidung, Produktion, Qualitätskontrolle, Freigabe und Nachlauf.
14. Seine Quellenkarte trennt amtliche Normen und Volltexte, Instanzrechtsprechung, bloße Suchhinweise und unverifizierte Treffer; die 2026-Entscheidungskarten nennen jeweils die konkrete Arbeitsfolge.

**Erwarteter Output:** Schnellstartprompt und Werkstattprompt können in Cloud-Co-Work als einzelner Skill geladen werden, ohne dass ein Repo-Klon oder weitere Dateien benötigt werden.

## 16 E-Akte- und DMS-Anschluss

Dieser Smoke-Test prüft, ob das Plugin Akten aus SAP, DocuWeb/DocuWare, DATEV-Dokumentenablage, RA-MICRO E-Akte, Datenbankexporten, XML/JSON-Dateien, MCP-Kontextplanung oder neutralen DMS-Exporten anschlussfähig strukturiert.

**Eingang:** Gemischter Export mit SAP-Statusauszug, PDF-Dateien, DMS-Metadaten, Fremd-Aktenzeichen, Dokument-IDs, Registern, E-Mail-Anlagen, XML/JSON- oder CSV-Datenbankauszug und einem unklaren Fristdokument.

**Prüfpunkte:**

1. `01-sap-akte-importieren` erkennt Herkunftssystem, Fremd-ID, Exportdatum und technische Herkunftsspur.
2. `33-dokumentenmix-ocr-sichten` inventarisiert Dokumente mit Zielregister, Dokumenttyp, OCR-Qualität, Datenschutzklasse und Fristbezug.
3. `34-sap-excel-pdf-normalisieren` erzeugt ein Schema für `fallakte.json`, `dms-register.csv`, optional `fallakte.xml` und `mcp-context-manifest.json`.
4. DocuWeb/DATEV/RA-MICRO/MCP-Importfähigkeit wird nicht blind behauptet, sondern bis zur Prüfung von Feldmapping, Rechten, Testsystem, Protokollierung und Importweg gelb markiert.
5. `45-hausverwaltung-schnittstelle` erzeugt einen `schnittstellenauftrag.md` mit konkreten Rückfragen an DMS-Administration oder IT.
6. Originaldateien bleiben unverändert; abgeleitete PDF/A- oder OCR-Dateien werden als Arbeitskopie gekennzeichnet.

**Erwarteter Output:** Strukturierte Fallakte, Dokumentregister, XML-/MCP-Planung, Mapping-Lückenliste und klare IT-/DMS-Klärungspunkte für Import oder Rückexport.

## 17 Schriftsatzwerkstatt beA

Dieser Smoke-Test prüft die fachlich neutrale technische Endfertigung eines bereits inhaltlich freigegebenen Schriftsatzes.

**Eingang:** Ein Projektordner mit DOCX-Hauptschriftsatz, XLSX-Tabelle, EML mit zwei Anhängen, JPEG-Scan, Bestands-PDF, früheren K-Anlagen und einer alten Entwurfsfassung.

**Prüfpunkte:**

1. `schriftsatzwerkstatt-bea` enthält genau neun und niemals mehr als zehn Skills.
2. Der Satz `Mache diesen Ordner beA-fertig. Verändere den juristischen Inhalt nicht und frage nur nach Angaben, die du nicht sicher aus den Dateien entnehmen kannst.` startet `01-bea-ordner-annahme`; eine manuelle Skillauswahl wird nicht verlangt.
3. Alle Quellen bleiben unverändert. Neue Dateien entstehen ausschließlich unter `_bea_ausgabe`.
4. Alte und neue Hauptfassung werden nicht nach Änderungsdatum verwechselt; Kommentare, Änderungsverfolgung und Platzhalter führen zum Stopp.
5. Die höchste vorhandene K-/B-Nummer wird fortgesetzt. Sichtbare Kennzeichnung, Schriftsatzzitat, Dateiname und Manifest stimmen überein.
6. E-Mail-Körper und relevante Anhänge werden getrennt behandelt. XLSX wird lesbar und nicht als unlesbare Ein-Seiten-Miniatur gerendert.
7. Jede relevante PDF-Seite wird gerendert und visuell geprüft; OCR allein gilt nicht als Sichtkontrolle.
8. Der Upload-Ordner enthält nur einzelne PDFs, keine ZIP-, Office-, Manifest- oder Protokolldatei.
9. Dateinamen sind logisch nummeriert, höchstens 80 Zeichen einschließlich `.pdf`, ASCII, ohne Leerzeichen und mit Unterstrichen. Umlaute und `ß` werden als `ae`, `oe`, `ue`, `ss` geschrieben.
10. `versandmanifest.csv` enthält Quelle, Ziel, Seiten, Bytes, SHA-256, OCR-, Kennzeichnungs- und Prüfstatus für jede Upload-Datei.
11. Die amtliche Grenze von 90 Zeichen wird als äußerer ERVB-Rahmen dokumentiert; die Werkstatt bleibt bewusst beim strengeren internen 80-Zeichen-Standard.
12. Bei einfacher Signatur werden verantwortliche Person und tatsächlicher persönlicher Versender getrennt erhoben und müssen übereinstimmen.
13. Bei qeS werden Signaturbezug und finale PDF-Fassung abgeglichen; Anlagen brauchen keine eigene Signatur.
14. Über 900 Dateien oder 180 MB wird gewarnt; über 1.000 Dateien oder 200 MB wird gestoppt.
15. Das Plugin meldet sich nicht selbst im beA an, behauptet keine Freigabe und behauptet bei bloßem Status `gesendet` keinen Gerichtseingang.
16. Die automatisierte Eingangsbestätigung wird mit Empfänger, Aktenzeichen, Zeitstempel, Dateiliste und Versandmanifest abgeglichen und anschließend mit dem Versandstand archiviert.
17. Kein Skill enthält Rechtsprechungsanker oder ändert Antrag, Vortrag, Beweiswürdigung, Frist oder sonstigen fachlichen Inhalt.
18. `uv run --with pypdf python3 schriftsatzwerkstatt-bea/scripts/validate_bea_package.py --selftest` läuft ohne Fehler.
19. Der Delta-Plan unterscheidet `unverändert`, `geändert`, `neu`, `fehlt` und `unklar`; eine Arbeitskopie wird nur bei identischem Quellhash, Profil, Werkzeugstand, Ausgabehash und früherem grünen Sichtstatus wiederverwendet.
20. Das Paketprotokoll weist alle einschlägigen Punkte des 100-Punkte-Fehlerkatalogs aus; rot sperrt, gelb braucht eine reale dokumentierte Entscheidung.
21. Der Validator verwirft abweichende CSV-Köpfe, Pfadaufstieg, Tabellenformeln, Symlinks, aktive PDF-Inhalte, mehrere Hauptschriftsätze und widersprüchliche Anlagenlabels.
22. Begrenzte Parallelisierung verändert weder Anlagenreihenfolge noch Manifest und ersetzt niemals den vollständigen finalen Paketcheck.
23. Der Preflight nennt Datum, tatsächlich aktiven beA-/eBO-/Kanzleisoftwarestand und XJustiz-Profil, übernimmt keine erfundenen Strukturdaten und hält jede clientseitige Datei-, Anhangs-, Signatur- oder Strukturwarnung bis zur realen Klärung offen.

**Erwarteter Output:** Ein reproduzierbares Upload-Verzeichnis, internes Manifest, Konvertierungs- und Prüfprotokoll, Signatur-/Versandwegentscheidung, Freigabekarte und Versandauftrag. Nach dem realen Versand kommt ein gesonderter Eingangsvermerk hinzu.

**Abbruchkriterium:** Quelle wurde verändert, falsche Endfassung gewählt, Anlage überdeckt, PDF nicht visuell geprüft, Dateiname unzulässig, Signatur-/Versenderidentität ungeklärt oder erfolgreicher Eingang ohne automatisierte Bestätigung behauptet.

## 18 Rechtsstand 2026: Online-Verfahren und Zwangsvollstreckung

Dieser Smoke-Test prüft die Stichtags- und Rollenlogik der 2026 neu eingeführten oder bereits verkündeten Verfahrensregeln.

**Eingang:** Reine Mietzahlungsklage über 4.800 EUR im Bezirk des Amtsgerichts Schöneberg durch eine private Konzerngesellschaft, Lohnpfändung im August 2026, je ein elektronischer Gerichtsvollzieher- und PfÜB-Auftrag mit Datum 20.09.2026 und 02.10.2026 sowie eine Schonfristzahlung mit Verweis auf BT-Drs. 21/6807.

**Prüfpunkte:**

1. Die Zuständigkeit wird vor der Teilnahme am Online-Verfahren nach GVG und ZPO bestimmt; das Amtsgericht Schöneberg wird nicht als berlinweites Pilotgericht behandelt.
2. Online-Verfahren nur bei reiner Zahlung bis 10.000 EUR, teilnehmendem zuständigem Amtsgericht, unterstütztem Anspruch, tatsächlicher Rolle und Nutzung des amtlichen Eingabesystems.
3. Die Eigenvertretung einer privaten GmbH durch Beschäftigte wird ohne positive aktuelle Dienstprüfung nicht in das Online-Verfahren geleitet; reguläre Klage nach Paragraf 253 ZPO bleibt verfügbar.
4. KV Nr. 1216 GKG wird nur für ein wirksam eröffnetes Online-Verfahren verwendet. Eine regulär per eBO eingereichte PDF-Klage bleibt bei KV Nr. 1210.
5. Die Lohnpfändung im August 2026 verwendet die amtliche Pfändungstabelle ab 01.07.2026 und behandelt 1.587,40 EUR nicht als fertigen Pfändungsbetrag.
6. Der Auftrag vom 20.09.2026 verwendet nicht vorzeitig die neuen Paragrafen 754a und 829a ZPO.
7. Der Auftrag vom 02.10.2026 verlangt Norm- und Formularprüfung, Übereinstimmungs- und Forderungsbestandsversicherung sowie Änderungsnachlauf.
8. Paragrafen 752a und 753a ZPO werden nicht auf Beschäftigte nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO ausgedehnt.
9. Eine private GmbH wird nicht allein durch Paragraf 753 Abs. 4 ZPO elektronisch nutzungspflichtig behandelt.
10. PDF/XML nach Paragraf 829 Abs. 5 ZPO bleibt bis 01.01.2027 gesperrt; der XML-Vorrang wird vorher nicht ausgegeben.
11. Skill 50 legt eine Umstellungs-Wiedervorlage zum 01.10.2026 und eine gesonderte Zukunftsnotiz zum 01.01.2027 an.
12. Werkstatt- und Schnellstartprompt enthalten dieselben Gates autark; die erzeugten Skills bleiben unter 30.000 beziehungsweise 7.500 Zeichen.
13. BT-Drs. 21/6807 wird als am 09.07.2026 nur an die Ausschüsse überwiesener Entwurf erkannt. Vorgeschlagene Regeln zu Kurzzeitmiete, Möblierung, Indexmiete, Modernisierung, ordentlicher Kündigung und Geschäftsraum-Belegeinsicht verändern keine aktuelle Berechnung oder Rechtsfolge.

**Erwarteter Output:** Zahlungsklagen- und Vollstreckungsakte mit dokumentiertem Normstichtag, richtiger Rolle, zutreffendem regulärem oder Online-Weg, aktueller Pfändungstabelle und ohne vorweggenommene Gesetzesstufe.

**Abbruchkriterium:** Falsches Pilotgericht, nicht unterstützte GmbH-Rolle, falsche GKG-Gebühr, alte Pfändungstabelle, Anwendung von Paragraf 754a oder 829a vor 01.10.2026, XML-Vorrang vor 01.01.2027 oder Behandlung einer BGB-E-Regel aus BT-Drs. 21/6807 als geltendes Recht.

## Validatoren

Vor jedem Tag und PR müssen die Pflichtvalidatoren ohne Fehler laufen:

```
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
python3 scripts/validate-legal-anchors.py
python3 scripts/validate-umlaut-prose.py
python3 scripts/validate-markdown-links.py --selftest
python3 scripts/validate-markdown-links.py
python3 scripts/validate-readme-navigation.py
python3 scripts/generate-skills-md.py --check
python3 scripts/validate-skill-frontmatter-parsers.py
uv run --with pypdf python3 schriftsatzwerkstatt-bea/scripts/validate_bea_package.py --selftest
python3 scripts/validate-testakten-gesamt-pdf.py
python3 scripts/validate-testakten-financial-consistency.py
python3 scripts/validate-testakten-stammdaten.py
uv run --with-requirements requirements-release.txt python3 scripts/validate-testakten-release-zips.py dist
uv run --with-requirements requirements-release.txt python3 scripts/validate-release-zips.py dist .claude-plugin/marketplace.json
uv run --with-requirements requirements-release.txt python3 scripts/validate-release-guardrails.py dist .claude-plugin/marketplace.json
```

Nach einem Tag-Release muss zusätzlich der GitHub-Workflow erfolgreich sein. Die Stufe `Release-Assets remote validieren` prüft die veröffentlichten Assets per `scripts/validate-release-assets.py`. Für eine manuelle Nachkontrolle nach Workflow-Ende die Assets mit `gh release download [tag] --dir [ziel]` herunterladen und dann `validate-testakten-release-zips.py` sowie `validate-release-zips.py` gegen dieses Download-Verzeichnis ausführen.
