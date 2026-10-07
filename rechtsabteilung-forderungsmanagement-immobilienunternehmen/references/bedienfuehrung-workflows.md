# Bedienführung und Workflow-Standards

Diese Referenz hält fest, wie Skills im Tagesgeschäft wirken sollen: wie eine gute Arbeitsmaske, nicht wie ein Lehrbuch. Zielgruppe sind starke Fachangestellte in einer Immobilien-Rechtsabteilung. Sie brauchen schnelle Orientierung, klare Rückfragen und verwertbare Zwischenergebnisse. Der ergänzende [100-Punkte-Bediencheck](./100-punkte-bediencheck.md) dient Pilot, Review und Release als konkrete Abnahmespur.

## 0. Ein-Satz-Startvertrag

Für einen neuen Fachfall genügt: `Neuer Fall. Prüfe den gesamten Ordner, sichere zuerst alle Fristen und arbeite ohne Skillauswahl bis zur nächsten freigabefähigen Entscheidung weiter.` Für die rein technische Endfertigung eines inhaltlich abgeschlossenen Schriftsatzes genügt im getrennten beA-Plugin: `Mache diesen Ordner beA-fertig. Verändere den juristischen Inhalt nicht und frage nur nach Angaben, die du nicht sicher aus den Dateien entnehmen kannst.`

Der Startvertrag ist verbindlich:

1. Keine Frage nach Skill, Workflowname oder Fallkategorie vor dem Sofortscan.
2. Fehlende ausdrückliche Fallbezeichnung ist kein Stopp, wenn Dokumente vorliegen.
3. Erste sichtbare Ausgabe ist immer dieselbe Sofortkarte: Modus, Akten-ID/Stichtag, Fallart, früheste Frist mit Quelle und Rechenstatus, Ampel mit Grund, Dateistand, höchstens drei Kernlücken und Feld `Jetzt` mit genau einer Arbeitsaktion.
4. Nach der Sofortkarte automatisch weiterarbeiten. Der Nutzer muss weder `weiter` schreiben noch einen Folgeskill bestimmen.
5. Nur blockierende Fragen stellen, deren Antwort die unmittelbar nächste Frist-, Rollen- oder Maßnahmenentscheidung ändert. Andere Unsicherheiten als gelbe Lücke erfassen und vorläufig weiterarbeiten.
6. Jede weitere Ausgabe zeigt den Fortschritt als `gelesen/gesamt`, den gesicherten Stichtag und die nächste aktive Einheit. Bereits geprüfte Inhalte werden nicht wiederholt.

### 0.1 Ergebnis vor Wiederholung

Nach der einmaligen Sofortkarte führt der konkrete Auftrag die Ausgabe. Bei einem Zahlungsavis entsteht der fortgeschriebene Restbetrag, bei fehlenden Betriebskostenbelegen die adressierte Anfrage, bei gegnerischer Post der Antwortentwurf. Register, Beweisplan und Rechenschritte werden im Arbeitsstand geführt; im Chat erscheinen nur Ergebnis, tragende Quelle, offene Entscheidung und nächste Aktion. Vollständige Tabellen nur zeigen, wenn sie für diese Entscheidung gebraucht oder angefordert werden.

Ein roter Befund sperrt die betroffene Außenmaßnahme. Er beendet nicht das Lesen unabhängiger Unterlagen oder die Sicherung einer Gerichtsfrist. Beispielsweise verhindert eine fehlende Hausmeisterrechnung die ungeprüfte Zahlungsklage, aber nicht die Auswertung des Mietvertrags und die konkrete Beleganforderung. Bei fehlenden Dateifunktionen Arbeitsergebnisse kopierbar ausgeben; keine angeblich erzeugten Dateien verlinken.

Bereits beantwortete Fragen entfallen. Gemeinsame Aktenstücke nur einmal lesen; Quellen gezielt zur tragenden Rechtsfrage öffnen. Vor erneutem OCR-Lauf vorhandenen Text und bereits geprüfte Seiten nutzen. Ein Sofortscan zählt nicht als abgeschlossene Lektüre; gelesen/gesamt muss den tatsächlich geprüften Bestand wiedergeben.

## 0a. Skill-Router vor jeder Aktenbearbeitung

Bei neuem oder unspezifischem Akten-Input nicht nach ähnlich klingenden Fachskills springen. Zuerst die Eingangssignale lesen und genau einen Startskill wählen.

| Eingangssignal | Bevorzugter Start | Danach | Nicht laden |
|---|---|---|---|
| Gemischtes Upload-Bundle, Scan, DMS, E-Mail, Foto, Excel oder unklare Dateien | `33-dokumentenmix-ocr-sichten` | `01`, `02`, `05`, dann `06-fallziel-renofa-triage` | keine Klage- oder Kündigungsentwürfe vor Inventar |
| SAP-Statusauszug, FBL5N, Mietkonto, Vertragsnummer oder Saldo | `01-sap-akte-importieren` | `02` bis `05`, dann `06-fallziel-renofa-triage` | nicht direkt `20`, `24` oder `17` |
| Saubere Mietkontofrage ohne Dokumentenmix | `03-kontoauszug-mietkonto-auslesen` | `04`, `05`, ggf. `11` | keine Kündigung ohne Rückstandsschwelle und Triage |
| Mieterhöhung, Mietspiegel, Paragraf 558 BGB oder Zustimmungsfrist | `28-mieterhoehung-bgb-558-vorbereiten` | `29`, `30`, `31` | keine Rückstands- oder Kündigungsskills ohne Saldo |
| Klageerwiderung, gerichtlicher Hinweis oder gegnerischer Schriftsatz in eigener Klage | `37-klageerwiderung-auswerten` | `38`, `39`, bei Widerklage ggf. `42` | keine neue Zahlungsklage als Standard |
| Außergerichtliches Mietervereinsschreiben oder gegnerisches Anwaltsschreiben | `43-mieterverein-anwalt-korrespondenz` | je Einwendung Fachpfad, ggf. `44` | nicht als gerichtliche Klageerwiderung behandeln |
| Fertiger Schriftsatz, beA-ready, eBO, Anlagen K/B, Einreichung oder Versandpaket | `39-beweisangebot-anlagenplan` | `23-klage-egvp-bea-einreichen` | keine Übermittlung ohne Rollengate, Anlagenmanifest, Versionssperre, geklärten Weg und reale Freigabe |
| Mieter verklagt Vermieterin, etwa Minderung, Kaution, Auskunft oder Mietpreisbremse | `42-mieterklage-verteidigen` | `39`, `43`, `45`, ggf. `08` | keine Replik ohne Verteidigungsstrategie |
| Betriebskostenabrechnung, Nachzahlung, Belegeinsicht oder Widerspruch | `44-betriebskosten-rueckstand-streit` | `45`, ggf. `20`, `37`, `38` | keine Zahlungsklage ohne formell/materiell getrennten Check |
| Urteil, Vergleich, KFB, Titel oder Vollstreckungsbescheid | Dokumenttyp wählen: `46`, `47`, `48`, `49`, `50` | Kosten und Vollstreckung | keine neue Anspruchsprüfung als Hauptpfad |
| Insolvenz, Berufung, Landgericht, Strafrecht, großer Sachverständigenstreit oder Teilunterliegen | `08-eskalation-an-anwalt` | Übergabe an eigene Kanzlei | keine Eigenbearbeitung |

Negativtrigger sind verbindlich: keine Vollstreckung ohne positiven vollstreckbaren Titel, keine Räumung ohne Kündigung und Zugang, keine Mieterhöhung aus bloßem Mietrückstand und keine Schnittstellenfreigabe ohne Mapping/Rechte/Testsystem. Erwartbarer Widerspruch macht das Mahnverfahren regelmäßig unzweckmäßig, ist aber kein gesetzliches Verbot; Paragraf-688-Gate und Verjährungszweck bleiben zu prüfen.

## 0b. Korrektur bei falscher Skill-Auswahl

Wenn ein Modell trotz Aktenlage den falschen Fachskill lädt, wird nicht im falschen Skill weitergearbeitet. Die Bearbeitung wird auf eine Startkarte zurückgeführt:

1. Eingangssignal benennen: Welche Datei, welcher Satz oder welches Dokument hat den aktuellen Pfad ausgelöst?
2. Gegen die Router-Tabelle prüfen: passt das Signal wirklich zu diesem Skill?
3. Bei Fehlgriff eine neue Arbeitsaktion in Klartext zeigen und intern genau einen passenden Skill routen.
4. Bisherige Zwischenergebnisse nur als Rohmaterial übernehmen, nicht als fachliche Entscheidung.
5. Bei zwei gleich starken Pfaden den risikoärmeren Start wählen: erst Intake, dann Triage, dann Fachpfad.

Typische Korrekturen:

| Falsch geladener Skill | Richtiger Neustart | Grund |
|---|---|---|
| `20` bei Räumungs- oder Herausgabeantrag | `24` | Räumung, Sozialwiderspruch, Schonfrist und Streitwert führen den Prozess |
| `42` bei bloßer Minderungseinwendung in eigener Klage | `37` | Mieterklage liegt erst bei eigener Klage oder Widerklage des Mieters vor |
| `48` bei bloßem KFA-Entwurf | `46` | Ohne Titel/KFB keine Vollstreckung |
| `01` bei gemischtem Upload-Bundle | `33` | Erst Dokumentenbestand, Lesbarkeit und Metadaten sortieren |
| `17` bei erwartbarem Streit | `20` oder `24` | Mahnverfahren ist nur optionale Abzweigung bei einfacher unstreitiger Forderung |

## 0c. Schneller Zwei-Phasen-Start

Bei großen Akten darf der Start nicht an einer Vollauswertung hängen. Das erste Ergebnis ist die Sofortkarte, keine fertige Klageakte.

1. Phase 1 scannt zuerst den gesamten sichtbaren Bestand auf Gerichtspost, Zustellung, Fristdaten, Zahlungen, Kündigungen sowie defekte Dateien. Danach liefert sie sofort eine kurze Sofortkarte; interne Skillnummern werden nicht zur Nutzerentscheidung gemacht.
2. Die Sofortkarte enthält nur Modus, Fallart, früheste mögliche Frist samt Quelle, Ampel mit Grund, Dateistand, höchstens drei Kernlücken und genau eine nächste Arbeitsaktion in Klartext.
3. Phase 2 vertieft ohne erneute Aufforderung: zuerst Gerichts- und Zustelldokumente, dann Zahlung und Konto, danach Kündigung und Vertrag, zuletzt Korrespondenz und übrige Belege. Je Stapel höchstens 20 Dateien oder 30 PDF-Seiten bearbeiten; bei neuem roten Risiko sofort stoppen.
4. Nach jedem Stapel eine Fortsetzungsmarke ausgeben: Akten-ID, Stichtag, verarbeitet/offen, letzte Quelle mit Seite oder Hash, früheste mögliche Frist, offene Risiken und nächster Stapel.
5. Nach Unterbrechung an der Fortsetzungsmarke weiterarbeiten. Unveränderte Dokumente, Roh-OCR und Tabellen weder erneut lesen noch vollständig wiederholen; bei geänderter Version nur das betroffene Dokument neu prüfen.
6. OCR-Probleme, Handschrift und schlechte Scans markieren, aber lesbare Dokumente parallel weiterverarbeiten. Ein einzelner Lesefehler beendet keinen Stapel.
7. Sichtbare Nutzertabellen auf höchstens sieben Spalten begrenzen. Technische Metadaten kommen in ein getrenntes Register oder einen Maschinenexport.
8. Keine Rückfrage nach der Skillauswahl. Rückfragen betreffen nur fehlende Tatsachen, Fristen, Rollen, Zielsysteme oder Freigaben.

## 0d. Laufende Akte als Delta fortschreiben

Wenn bereits eine Startkarte, Chronologie oder Prozesskarte vorliegt und nur neue Zahlung, Gerichtspost, Korrespondenz oder DMS-Unterlagen eingehen, wird die Akte nicht vollständig neu begonnen.

1. Akten-ID und letzten belastbaren Stichtag aus dem bisherigen Arbeitsstand übernehmen.
2. Nur Neuzugang und erkennbare Änderungen inventarisieren; fehlt ein belastbarer bisheriger Aktenstand, führt der Weg zurück zu Skill `33` und zum Vollintake.
3. Altstand und Neuzugang für Saldo, Frist, Prozesslage, Beweisstatus und Freigabe vergleichen.
4. Überholte Annahmen und Entwürfe ausdrücklich als überholt markieren; niemals still überschreiben.
5. Chronologie, Mietkonto, Belegmatrix und Fristenblatt nur an den betroffenen Stellen fortschreiben.
6. Ereignisbezogen routen: Gerichtspost zu `37` oder `42`, Zahlung zu `03`, `05`, `11`, `27` oder `50`, KFA/KFB/Titel zu `46` bis `48`, technische Neudaten zu `33`, `34` oder `45`.
7. Bei mehreren Ereignissen führt die nächste harte Frist. Weitere Delta-Aufgaben kommen in eine geordnete Warteschlange, nicht als gleichrangige Parallelstarts.
8. Änderungskarte ausgeben: Stichtag alt/neu, Neuzugang, geänderte Tatsachen und Beträge, überholte Annahmen, unveränderter Kernstand, Sofortfrist und genau eine nächste Arbeitsaktion; Skill-ID nur intern.

## 1. Erste Antwort

Wenn eine neue Akte eingeht, beginnt die Ausgabe mit einer Sofortkarte. Sie ersetzt nicht die spätere Startkarte, verhindert aber, dass ein großer Upload bis zur Vollauswertung ohne sichtbares Ergebnis bleibt:

| Feld | Inhalt |
|---|---|
| Modus | Vollintake oder Delta-Fortschreibung |
| Fallart | Zahlung, Räumung, Mieterhöhung, Betriebskosten, Verteidigung, Kosten, Vollstreckung |
| Ampel | grün, gelb oder rot |
| Warum | ein Satz |
| Dateistand | sichtbar, lesbar, defekt oder OCR-offen |
| Nächste Arbeitsaktion | genau ein verständlich bezeichneter Arbeitsschritt; Skill-ID nur intern |
| Fehlendes Kernstück | höchstens drei Punkte |
| Frist | frühestes mögliches Datum, Auslöser, Quelle, Rechenstatus, Vorfrist und verantwortliche Rolle |

Nach der Sofortkarte arbeitet das Plugin automatisch bis zur vollständigen Start- oder Änderungskarte weiter, solange kein roter Stopp eine reale Entscheidung oder fehlende Pflichtangabe erfordert.

Bei mehr als 20 Dateien oder 30 PDF-Seiten erscheint nach jedem Stapel eine Fortsetzungsmarke. Sie verhindert, dass ein Kontextwechsel die Akte neu beginnen lässt oder lange Rohtexte erneut ausgegeben werden.

## 2. Rückfragen

Rückfragen sind erlaubt und gewollt, aber sie müssen bedienbar bleiben:

1. Maximal drei Rückfragen auf einmal.
2. Jede Rückfrage muss sagen, warum sie gebraucht wird.
3. Wenn der Fall trotzdem bearbeitbar ist, wird mit gelber Ampel vorläufig weitergearbeitet.
4. Nur rote Lücken stoppen den Workflow: unklarer Gegner, unklare Forderung, abgelaufene Frist, fehlender Titel, ungeprüfter Schreibzugriff in ein Zielsystem.

## 3. Interne Workflow-Karte

Nach Intake oder Triage wählt das Plugin den passenden Pfad automatisch. Nur wenn eine echte Unternehmensentscheidung zwischen mehreren rechtlich tragfähigen Folgen nötig ist, zeigt es höchstens drei konkrete Optionen mit Auswirkung, Risiko und Freigabebedarf. Die folgende Karte dient dem internen Routing:

| Auswahl | Workflow | Start |
|---|---|---|
| A | Zahlung fordern oder klagen | Skills 09 bis 12 oder 20 bis 23 |
| B | Kündigung und Räumung | Skills 13 bis 16 und 24 bis 27 |
| C | Mieterhöhung | Skills 28 bis 31 |
| D | Gerichtliche Prozessreaktion | Skills 37 bis 42 |
| E | Außergerichtliche Gegenseite | Skill 43, fachlich ggf. 44 oder 45 |
| F | Betriebskosten und Hausverwaltung | Skills 44 bis 45 |
| G | Kosten und Vollstreckung | Skills 46 bis 50 |
| H | Schnittstelle, DMS, IT | Skills 01, 33, 34 und 45 |
| I | Eskalation an Anwalt | Skill 08 |

## 3a. Risikobasierte Routing-Karte

| Nutzerfall | Skill-Kette | Trigger |
|---|---|---|
| SAP/DMS-Intake | `01` oder `33` -> `34` -> `35` -> `05` -> `06-fallziel-renofa-triage` | SAP-Status, FBL5N, DMS-Export, OCR/Scan, fehlende Vertragsdaten, Fristdokument |
| Mietkonto | `03` -> `04` -> `05` -> ggf. `11` | Soll/Ist, Saldo, Teilzahlung, Storno, Guthaben, Tilgungsbestimmung, Buchungsdatum |
| Zwei offene Mieten | `03` -> `06-fallziel-renofa-triage`/`36` -> `09`/`10`/`12` oder `13` | Schwelle erreicht, Versehen/Kulanz möglich, laufende Miete stabil, Kündigung prüfen |
| Fünf offene Mieten | `03` -> `13`/`14`/`15` -> `20`/`24` -> `21`/`22`/`23` | erheblicher Rückstand, Zahlungsstopp, Minderungsbehauptung, Räumungsrisiko |
| Gebrochener Ratenplan | `10` -> `05` -> `11` -> `20` oder `41` | Rate ausgefallen, Fälligstellungsklausel, Anerkenntnis, Wiedervorlage |
| Kündigung | `13` und `14` -> `15` -> `16` -> ggf. `27` | Rückstandsschwelle, Zugang, alle Mieter, Sozialwiderspruch, frühere Schonfrist |
| Räumung | `24` -> `21`/`22` -> `25`/`26` -> `27` | Räumungsverweigerung, Zahlungs- und Räumungsantrag, Härtefall, Berliner Modell |
| Schonfristzahlung | `27` -> `37`/`38` -> ggf. `11`/`08` | Jobcenter/Zahlung nach Rechtshängigkeit, fristlose Kündigung geheilt, Kostenpfad |
| Mieterhöhung | `28` -> `29` -> `30` -> `31` | Paragraf 558 BGB, Sperrfrist, Mietspiegel, Kappungsgrenze, Teilzustimmung |
| Betriebskosten | `44` -> `45` -> ggf. `20`/`37`/`38` | Nachzahlung offen, Abrechnungsfrist, Einwendungsfrist, Belegeinsicht |
| Klageerwiderung/Replik | `37` -> `38` -> `39` -> ggf. `40`/`41` | Klageerwiderung, Hinweisbeschluss, Minderung, Zahlung nach Klage, Beweisrisiko |
| Mieterklage | `42` -> `39` -> `43`/`45` -> ggf. `08` | Zustellung, Klageerwiderungsfrist, Mängel, Kaution, Auskunft, Sachverständiger |
| Externe Kanzlei | `06-fallziel-renofa-triage`/`07` -> `08` | Landgericht, statthafte oder zugelassene Berufung, Insolvenz, Strafrecht, Sachverständiger, Kostenstreit |
| KFA/KFB/Vollstreckung | `46` -> `47` -> `48` -> `49` -> `50` -> ggf. `08` | Urteil, Vergleich, KFB, Klausel, Zustellung, Quote, Zahlung, Insolvenz |
| Gerichtsfertiges Einreichungspaket | `39` -> `23` -> ggf. `08` | freigegebener Schriftsatz, K-/B-Anlagen, PDF, Rollengate, beA/eBO/schriftlicher Weg, Signatur, ERVV soweit einschlägig, Eingang |
| DocuWeb/DATEV/RA-MICRO/MCP | `01`/`33`/`34` -> `45` -> `32` | Mapping unbekannt, Rechte/Testsystem fehlen, Importweg offen, MCP nur Planung |

## 4. Ausgabequalität

Jedes Zwischenergebnis enthält:

1. Tabelle oder Matrix.
2. Frist oder Wiedervorlage, falls relevant.
3. Beleg- oder Quellenstatus.
4. Ampel mit Grund.
5. Nächste Arbeitsaktion in Klartext; Skill-ID nur intern.
6. Außenentwurf nur bei ausreichenden Fakten. Sonst entsteht ausschließlich eine interne Arbeitsskizze mit klaren Lückenmarken; offene Platzhalter sperren Freigabe und beA-Übergabe.

## 4a. Freigabekarte vor Außenwirkung

Jedes Schreiben an Mieter, Vertreter oder Hausverwaltung und jeder Schriftsatz, Kostenantrag oder Vollstreckungsauftrag erhält eine getrennte interne Freigabekarte. Die Karte steht vor dem Dokumentpaket, gehört aber nicht in das außenwirksame Dokument.

| Prüffeld | Mindestinhalt |
|---|---|
| Status | zunächst `ENTWURF - NICHT VERSENDEN/EINREICHEN` |
| Aktenstand | Akten-ID, Datenstichtag, letzte berücksichtigte Zahlung und Dokumentversion |
| Adressat | richtige Partei, Anschrift, Gericht, Aktenzeichen und Vertretung |
| Rechtsfolge | Antrag oder Aufforderung stimmt mit Fallziel, Normenprüfung und Tenor überein |
| Betragskontrolle | Hauptforderung plus Zinsen plus Kosten minus Zahlungen ergibt den verlangten Betrag |
| Tatsachen und Beweise | tragende Tatsache hat Quelle; Anlage, Zugang und Zustellnachweis sind zugeordnet |
| Frist und Weg | Fristablauf, interne Vorfrist, Zustell- oder Einreichungsweg und Eingangsnachweis |
| Rollencheck | interne Grenze, Paragraf 79 ZPO, RA-Eskalation und zeichnungsberechtigte Person |
| Freigabe | Name der fachlichen Freigabeperson, Zeitpunkt, Entscheidung und verbleibende Auflage |

Grün bedeutet nur fachlich freigabefähig. Erst die dokumentierte Entscheidung einer realen Freigabeperson ändert den Status auf `FREIGEGEBEN`; ein Modell darf dies nicht selbst setzen. Gelb bleibt bearbeitbarer Entwurf ohne Versand. Rot stoppt Versand oder Einreichung.

Eine frühere Freigabe erlischt, sobald sich Betrag, Antrag, Partei, Frist, Beweis, Anlage, Zustellweg oder Datenstichtag ändert. Dann wird die Änderungskarte gegen die letzte Freigabekarte geprüft und das Gate erneut durchlaufen.

## 5. Übergaben

Übergaben zwischen Skills sind knapp und maschinenlesbar:

| Übergabe | Mindestinhalt |
|---|---|
| Intake an Klage | Stammdaten, Forderung, Belege, Fristen, Konflikte |
| Klage an Replik | gegnerische Einwendungen, Antwortlinie, Beweise, Frist |
| Urteil an Kosten | Tenor, Quote, Vollstreckbarkeit, Fristen, KFA-Bedarf |
| Kosten an Vollstreckung | Titel, Forderung, Zinsen, Kosten, Zahlungen, Schuldnerdaten |
| Akte an IT | Zielsystem, Mapping, Rechte, Pflichtfelder, Testimport |
| Laufende Akte an Folgeschritt | Akten-ID, Stichtag alt/neu, Delta, überholte Annahmen, neue Frist, aktualisierter Saldo, nächste Arbeitsaktion und interner Folgeskill |
| Anlagenplan an Einreichung | Parteirolle, Schriftsatzversion, höchste vergebene K-/B-Nummer, Beweistatsache, Originalquelle, Seiten, Hash, Zielname, Beschaffungs- und Datenschutzstatus |

Jede Übergabe hält den bereits geprüften Stand fest. Ein Folgeskill wiederholt den Vollintake nur, wenn Akten-ID, Stichtag oder tragender Aktenstand fehlen; sonst arbeitet er auf der Änderungskarte weiter.

## 5a. Gerichtsfertiges Dokumentenpaket

Wenn der Nutzer „fertig zur Einreichung“, „beA-ready“, „eBO-fertig“ oder „Schriftsatz mit Anlagen finalisieren“ sagt, folgt kein allgemeiner Klageworkflow mehr. Skill `39` schließt zuerst Beweistatsachen, Beweislast, bereits vergebene K-/B-Nummern, Originalquellen und fehlende Anlagen. Skill `23` entscheidet danach zwingend zwischen Eigenvertretung und Kanzlei, erzeugt Hauptschriftsatz und jede Anlage als eigene geprüfte PDF-Arbeitskopie, sichtbare Anlagenkennzeichnung, logische ASCII-Dateinamen, Anlagenverzeichnis, Hashmanifest, Form-/Signaturcheck, Versandauftrag und Eingangsnachlauf nach `references/erv-dokumentenproduktion.md`.

Eine Übermittlung wird nie simuliert. Im Kanzleifall muss bei einfacher Signatur die verantwortende anwaltliche Person selbst aus ihrem beA versenden. In zulässiger Eigenvertretung wird ein tatsächlich eingerichtetes eBO nach Paragraf 130a Abs. 4 S. 1 Nr. 3 ZPO und Paragraf 10 ERVV oder eine im konkreten Verfahren zulässige schriftliche Einreichung geprüft. Eine private GmbH ist nicht allein wegen ihrer Rechtsform nach Paragraf 130d ZPO aktiv nutzungspflichtig. Ohne reale Freigabe, eindeutige Schriftsatzversion, vollständiges Anlagenmanifest, belegte Vertretung oder geklärten Übermittlungsweg bleibt die Ampel rot.

## 6. Sprache

1. Kurze Hauptsätze.
2. Normen nur mit Arbeitsfolge.
3. Keine Professorenprosa.
4. Keine bloßen Schlagworte als Endprodukt.
5. Bei Unsicherheit: offen sagen, gelb markieren, Rückfrage stellen.
