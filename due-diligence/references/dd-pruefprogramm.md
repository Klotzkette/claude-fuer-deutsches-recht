# Prüfprogramm und Übergaben für DD – Due Diligence

## 1. Arbeitsprinzip

Der Mandatslauf verbindet einen klar abgegrenzten Prüfauftrag mit Originalbelegen, nachvollziehbaren Zahlen und einer konkreten Entscheidung. Käufer und Investor sind die übliche Perspektive; Verkäufer können denselben Bestand für eine Vendor Due Diligence prüfen lassen. Der Rollenwechsel verändert Ziel und Empfänger, nicht den Wahrheitsgehalt der Befunde.

Vorhandene Unterlagen werden zuerst gelesen. Erforderliche Fragen werden gebündelt, bereits geklärte Angaben nicht erneut erhoben. Danach läuft die interne Bearbeitung selbständig bis zum beauftragten Ergebnis. Fehlende externe Informationen blockieren nur die davon abhängigen Feststellungen. Versand, Offenlegung zusätzlicher vertraulicher Daten, rechtserhebliche Erklärungen und Vollzugsfreigaben benötigen eine konkret dokumentierte menschliche Freigabe.

## 2. Einheitlicher Mandatslauf

| Phase | Eingang | Produkt | Abschlusskriterium |
|---|---|---|---|
| Auftrag | Mandatsziel und Transaktionsunterlagen | `auftrag` | Seite, Gegenstand, Tiefe, Stichtag und Empfänger bestimmt |
| Datenraum | Export und Anhänge | `belegregister` | Dateien, Fassungen, Lesbarkeit und Lücken erfasst |
| Schnellprüfung | Geprüfter Bestand | `schnellbericht` | Wesentliche erste Befunde mit Prüfgrenzen dargestellt |
| Vertiefung | Fachpakete | `fachbefunde` | Sachverhalt, Gegenargument und Rechtsfolge belegt |
| Rückfragen | Konkrete Beleglücken | `qa-register` | Antworten geprüft oder Lücken sichtbar eskaliert |
| Absicherung | Konsolidierter Bericht | `entscheidung` | Preis-, Vertrags- und Vollzugsfolgen formuliert |
| Vollzug | Vereinbarte Bedingungen | `vollzugsnachweise` | Nachweise geprüft und zuständige Person entscheidet |
| Nachlauf | Verbleibende Aufgaben | `integration` | Verantwortung, Quelle und Wiedervorlage benannt |

Der Statusblock enthält Phase, Mandatsseite, Erwerbsgegenstand, Datenraumstichtag, führende Berichtsfassung, offene kritische Befunde, verantwortliche Person und nächstes Produkt. Ein Produktstatus darf „Entwurf“, „in Prüfung“, „fachlich geprüft“ oder „menschlich freigegeben“ lauten. Diese Zustände sind nicht austauschbar. Eine automatisch erfolgreiche Tabellenprüfung ist keine rechtsgeschäftliche Freigabe.

## 3. Die elf Skills und ihre konkreten Übergaben

| Skill | Führendes Produkt | Eingang aus Nachbarskill | Rückgabe / nächste Übergabe |
|---|---|---|---|
| `due-diligence-steuern` | Mandatslauf | Auftrag und Fachprodukte | Nächstes Produkt, offene Entscheidung, Zuständigkeit |
| `auftrag-transaktion-abgrenzen` | `auftrag` | Transaktionsziel | Prüfbestand und Grenzen an Datenraum und Fachskills |
| `datenraum-belege-ordnen` | `belegregister` | Auftrag, Dateien | Fassungen und Belegketten an alle Fachskills |
| `gesellschaft-beteiligungen-pruefen` | `corporate-befunde` | Register- und Urkundenpaket | Titel-, Einlagen- und Zustimmungslage an Bilanz und Entscheidung |
| `personal-arbeitsvertraege-pruefen` | `personalregister` | Verträge, Nachträge, Organisation | Zuordnung und Kostenbrücke an Bilanz und Entscheidung |
| `bilanz-finanzierung-pruefen` | `finanzbruecken` | Konten, Belege, Fachrisiken | Geprüfte Beträge und Annahmen an Entscheidung |
| `vertraege-vermoegen-pruefen` | `vertragsregister` | Vertrags- und Vermögenspaket | Übertragungs- und Fortführungsvoraussetzungen an Entscheidung |
| `verbraucherdarlehen-pruefen` | `darlehensfallkarten` | Kreditakten und Buchungsjournale | Saldo, Einwendungen und Durchsetzbarkeit an Portfolio und Bilanz |
| `kreditportfolio-uebertragen` | `portfolioplan` | Fallkarten, Rollen, Loan Tape | Zivilrechtliche und regulatorische Bedingungen an Entscheidung |
| `befunde-qa-verfolgen` | `qa-register` | Fachbefunde und Antworten | Geprüfte Änderungen zurück an betroffene Fachskills |
| `kaufentscheidung-absichern` | `entscheidung` | Konsolidierte Fachprodukte | Vertrag, Vollzugsplan und Integrationsliste an Hauptskill |

Ein Fachskill kann einen bereits geklärten Punkt wieder öffnen, wenn ein neuer Beleg seine Grundlage verändert. Er dokumentiert Quelle und Grund. Die führende Befundkennung bleibt erhalten; alte Fassungen werden nicht rückwirkend umgeschrieben.

## 4. Gemeinsame Datenmodelle

### 4.1. Belegregister

Ein Beleg erhält stabile Kennung, Originalpfad, Dateityp, Hash, Einlieferungszeitpunkt, Dokumentdatum, betroffenen Rechtsträger oder Einzelfall, führende Fassung, Lesestatus und konkrete Fundstelle. E-Mail-Anhang und Nachricht werden verknüpft. Ein OCR-Auszug ist als Arbeitskopie gekennzeichnet. Unlesbar, nicht vorgelegt und nicht geprüft sind unterschiedliche Zustände.

### 4.2. Befundregister

Ein Befund erhält Kennung, Fachgebiet, Tatsachengrundlage, Beleg- und Gegenbelegkennungen, offene Frage, Rechtsgrundlage, begründete Bewertung, Betrag oder Nichtbezifferbarkeit, mögliche Überschneidungen und Handlungsvorschlag. Die Prüftiefe und Datenabdeckung stehen getrennt von der Risikobedeutung. Eine hohe Unsicherheit ist nicht automatisch ein bewiesener hoher Schaden.

### 4.3. Fragenregister

Eine Frage erhält Kennung, zugehörigen Befund, konkreten Fragetext, benötigten Nachweis, Empfänger, internen Verantwortlichen, Zeitvorgabe samt Herkunft, Antwort mit Datum, geprüfte Anlagen und verbleibende Lücke. Nur eine inhaltlich geprüfte Antwort kann einen Befund klären. Erledigung durch ausdrückliche Risikoübernahme verlangt Person, Datum, Kenntnisstand und Entscheidung.

### 4.4. Zahlenregister

Jeder relevante Betrag wird als extrahiert, berechnet, geschätzt oder vorgegeben gekennzeichnet. Stichtag, Währung, Vorzeichen, Rechenweg, Beleg und Rundung sind nachvollziehbar. Leere Zelle, Nullbetrag, fehlender Beleg und streitiger Betrag werden nicht gleichgesetzt. Derselbe Risikobetrag wird nicht mehrfach in Kaufpreis, Betriebskapital und Freistellung eingerechnet.

## 5. Excel als Arbeitsprodukt

Die Arbeitsmappe beginnt mit einer verständlichen Legende und enthält Rohdaten, geprüfte Einzelpositionen, Überleitungen, Szenarien, offene Fragen und Quellen. Berechnete Felder enthalten nachvollziehbare Formeln. Manuelle Annahmen sind sichtbar markiert. Filter, ausgeblendete Zeilen, externe Verknüpfungen und Summenbereiche werden kontrolliert. Kritische Ergebnisse erhalten eine exemplarische unabhängige Nachrechnung.

Die Personalarbeitsmappe trennt fünfzig Arbeitsverträge von zwei Geschäftsführeranstellungen. Der Kreditbestand trennt die vollständige Grundgesamtheit vom verfügbaren zwanzigteiligen Aktenauszug. Eine problemorientierte Auswahl wird nicht ohne statistische Grundlage als repräsentativ oder als Beweis einer Portfolioausfallquote ausgegeben. Der Finanzbericht trennt Buchwert, Forderungsbestand, Fälligkeit, Durchsetzbarkeit und erwartbaren Rückfluss.

## 6. Drei Testakten und geeignete Arbeitsaufträge

### 6.1. Innovation Systems Berlin

Aktenordner: `testakten/dd-arbeitsvertraege-innovation-berlin`. Die zugrunde liegende Akte mit fünfzig Arbeitsverträgen wird gespiegelt; die ursprüngliche Testakte bleibt bestehen. Geeigneter Auftrag: „Prüfen Sie aus Erwerbersicht, welche Personen und Verpflichtungen im vorgesehenen Erwerb betroffen sind, erstellen Sie eine vollständige Personalübersicht in Excel und nennen Sie die wichtigsten belegten Rückfragen.“ Die Vertragsfamilienbildung darf keine individuellen Nachträge verschwinden lassen. Insolvenzbezug und Organanstellungen werden gesondert geprüft.

### 6.2. Corporate-DD Silberfalke

Aktenordner: `testakten/dd-corporate-silberfalke`. Die ursprüngliche umfangreiche Datenraumakte bleibt erhalten. Für eine eigenständige Übung können bereits enthaltene DD-Berichte und Bewertungen zunächst außerhalb des Prüfinputs gehalten werden. Geeigneter Auftrag: „Prüfen Sie die Transaktion aus Käufersicht, zeigen Sie Beteiligungs-, Vertrags- und Finanzrisiken und entwickeln Sie konkrete Kaufvertragsänderungen.“ Später werden eigene Ergebnisse mit vorhandenen Fremdbewertungen verglichen; Übereinstimmung ist kein automatischer Wahrheitsnachweis.

### 6.3. Englische Bankfiliale Erfurt

Aktenordner: `testakten/dd-bankfiliale-verbraucherdarlehen-erfurt`. Geeigneter Auftrag: „Prüfen Sie die zwanzig vorgelegten Darlehensakten als Ausschnitt des bezeichneten Tausenderbestands. Trennen Sie Forderungsbestand, rechtliche Durchsetzbarkeit und wirtschaftlichen Rückfluss. Prüfen Sie anschließend den Übertragungs- und Dienstleisterpfad der deutschen Filiale.“ Performing-Kredite, Verzugsfälle, Kündigungen, Titel und Verbraucherinsolvenz erhalten eigene Fallkarten. Der englische Sitz der Mutterbank löst keine pauschale KrZwMG-Ausnahme aus.

## 7. Abschlusskontrolle

Vor Abgabe wird geprüft, ob jeder kaufentscheidende Satz eine Fundstelle oder erkennbar markierte Annahme hat, Rechtsgrundlagen in der passenden Fassung gelesen sind, Zahlen aus derselben Stichtagsbasis stammen und die Ergebnisse in Vertrags- und Vollzugsprodukte überführt wurden. Empfängerdokumente sind vollständig ausformuliert. Interne technische Protokolle und Freigabevermerke stehen getrennt. Formatstandard ist Times New Roman, 11 pt, soweit technisch möglich, mit ausschließlich dezimaler Gliederung.

Ein Abschlussbericht darf offenlassen, was mangels Beleg nicht feststellbar ist. Er darf nicht behaupten, vollständige Daten, aktuelle Erlaubnisse oder menschliche Freigaben lägen vor, wenn nur ein Entwurf oder eine Verkäuferbehauptung existiert. Das Ende der Prüfung ist der belastbare beauftragte Stand mit nachvollziehbaren nächsten Schritten.
