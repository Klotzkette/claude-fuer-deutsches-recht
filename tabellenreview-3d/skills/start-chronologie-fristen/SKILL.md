---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Tabellenreview 3d-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: — Arbeitskontext: Tabellenreview (Excel/CSV), Schwerpunkt start chronologie fristen."
---

# Tabellenreview 3D — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Tabellenreview 3d**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** 3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `arbeitsblatt-perspektiven-definieren` | Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster,… |
| `audit-trail-protokoll` | Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output:… |
| `belegkette-rueckverfolgung` | Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output:… |
| `caching-und-teil-rerun` | Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten… |
| `dokumentstapel-aufnehmen` | Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output:… |
| `excel-multi-sheet-export` | 3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei… |
| `kreuzblatt-konsistenzpruefung` | Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege.… |
| `pdf-bericht-erzeugen` | 3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Prüfraster: Vollständigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview.… |
| `prompt-versionierung` | Prompt-Versionen für den 3D-Review verwalten: Versionierung der Spaltenprompts und Zeilenprompts. Normen: technisch/governance. Prüfraster: Versionsnummer, Aenderungsprotokoll, aktive Version. Output:… |
| `pruefer-uebergabe-paket` | Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für… |
| `review-durchfuehren` | 3D-Tabellenreview konkret durchführen: jede Zeile in allen drei Perspektiven prüfen und bewerten. Normen: §§ 174 ff. 176 InsO. Prüfraster: Forderungshoehe, Prüfergebnis je Spalte, Risikoampel, Ausnahmekennzeichnung.… |
| `risikoampel-aggregation` | Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht.… |
| `spaltenprompts-definieren` | Spaltenprompts für die drei Prüfperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument.… |
| `tabellenreview-3d-kaltstart-interview` | Kaltstart-Interview für den 3D-Tabellenreview: Fallkategorie, Tabellengrösse, Prüfzweck erfassen. Normen: §§ 174 ff. InsO, HGB. Prüfraster: Zweck, Datenlage, Perspektivenwahl, Exportformat. Output:… |
| `vorlage-arbeitsvertrag-portfolio` | Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format: Forderung/Prüfung/Stellung. Normen: BGB, KSchG, ArbZG. Prüfraster: Vertragsbedingungen, Klauselgueltigkeit, HR-Compliance. Output:… |
| `vorlage-immobilien-portfolio` | Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format. Normen: §§ 535 ff. BGB, WEG, GrEStG. Prüfraster: Miete, Grundbuch, steuerliche Belastung, Instandhaltung. Output: Immobilien-Portfolio-Tabelle.… |
| `vorlage-ma-due-diligence` | Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output:… |
| `vorlage-vendor-onboarding-3d` | Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output:… |
| `wuerfel-aufbauen` | 3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output:… |
| `zeilenprompts-definieren` | Zeilenprompts für einzelne Prüfpositionen im 3D-Tabellenreview definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Zeilentyp, Normverankerung, Eindeutigkeit. Output: Zeilenprompts-Dokument.… |

## Worum geht es?

Das Plugin strukturiert die Massenpruefung von Vertragsstapeln und Due-Diligence-Unterlagen als dreidimensionalen Wuerfel: Die erste Dimension sind Spaltenprompts, die je einen Pruefpunkt (z. B. Kuendigungsklausel, Laufzeit) abfragen. Die zweite Dimension sind Zeilenprompts, die jedes einzelne Dokument des Stapels repraesentieren. Die dritte Dimension sind Arbeitsblatt-Perspektiven, die denselben Datensatz aus unterschiedlichen fachlichen Blickwinkeln betrachten (Recht, Steuer, Wirtschaft).

Das Ergebnis wird als Excel-Datei mit mehreren Arbeitsblaettern exportiert, enthaelt eine Kreuzblatt-Konsistenzpruefung auf Widersprueche zwischen den Dimensionen, einen lueckenlosen Audit-Trail und eine Belegketten-Dokumentation. Typische Einsaetzgebiete sind M-und-A-Due-Diligence, Immobilien-Portfoliopruefung, Vendor-Onboarding und Arbeitsvertrags-Portfolio-Review.

## Wann brauchen Sie diese Skill?

- Sie muessen 20 oder mehr Vertraege auf dieselben Pruefpunkte hin systematisch analysieren und das Ergebnis auswertbar dokumentieren.
- Eine M-und-A-Due-Diligence erfordert die gleichzeitige Betrachtung von Vertraegen aus rechtlicher, steuerlicher und wirtschaftlicher Perspektive.
- Ein Lieferant soll ongeboardet werden und Vertrag, Compliance-Status und Leistungsindikatoren muessen dokumentiert werden.
- Der Pruefer wechselt und das bisher bearbeitete Paket soll mit vollem Kontext und offenem Status uebergeben werden.
- Zwischenergebnisse sollen gecacht und einzelne Teile ohne Vollneustart erneut ausgefuehrt werden.

## Fachbegriffe (kurz erklaert)

- **Wuerfel** — Metapher für die dreidimensionale Pruefstruktur: Zeilen (Dokumente) x Spalten (Pruefpunkte) x Perspektiven (Blickwinkel).
- **Spaltenprompt** — Einzelne Frage oder Pruefanweisung, die für jedes Dokument in einer bestimmten Spalte beantwortet wird.
- **Zeilenprompt** — Dokumentspezifische Pruefanweisung, die das einzelne Dokument als Pruefgegenstand definiert.
- **Arbeitsblatt-Perspektive** — Fachlicher Blickwinkel (Recht, Steuer, Wirtschaft), der denselben Wuerfel in einem eigenen Excel-Sheet abbildet.
- **Kreuzblatt-Konsistenzpruefung** — Abgleich der drei Dimensionen auf Widersprueche und fehlende Eintraege.
- **Audit-Trail** — Lueckenlose Protokollierung aller Pruefschritte mit Zeitstempel, Pruefer-ID und Aenderungshistorie.
- **Risikoampel** — Rot-Gelb-Gruen-Bewertung je Pruefposition zur schnellen Risikouebersicht.
- **Belegkette** — Nachverfolgung der Originalbelege hinter jeder Buchung oder Forderung.

## Rechtsgrundlagen

- §§ 174 ff. InsO — Forderungsanmeldung und -pruefung (Stammreferenz der 3D-Review-Skills)
- §§ 238 257 HGB — Buchfuehrungs- und Aufbewahrungspflichten
- GmbHG AktG HGB InsO — Relevante Normen je nach Vorlagen-Typ
- BGB §§ 305 ff. — AGB-Kontrolle bei Vertragsstapeln
- BetrAVG — Bei Arbeitsvertrag-Portfolio-Reviews
- DSGVO Art. 5 — Datensparsamkeit bei Verarbeitung von Vertragsdaten

## Schritt-für-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview: Fallkategorie, Tabellengroesse, Pruefzweck und Exportformat erfassen.
2. Wuerfelstruktur aufbauen: Spaltenprompts und Zeilenprompts definieren, Perspektiven festlegen.
3. Dokumentstapel einlesen und Inventar erstellen.
4. Review durchfuehren: jede Zeile in allen drei Perspektiven pruefen und Risikoampel setzen.
5. Kreuzblatt-Konsistenzpruefung und Audit-Trail abschliessen; Excel-Export oder PDF-Bericht erzeugen.

## Skill-Tour (was gibt es hier?)

- `arbeitsblatt-perspektiven-definieren` — Die drei Pruefperspektiven (Recht, Steuer, Wirtschaft) für den 3D-Wuerfel definieren.
- `audit-trail-protokoll` — Alle Review-Schritte mit Zeitstempel und Pruefer-ID protokollieren.
- `belegkette-rueckverfolgung` — Belegkette für Forderungen und Zahlungen zurueckverfolgen.
- `caching-und-teil-rerun` — Zwischenergebnisse cachen und Teilbereiche ohne Vollneustart erneut ausfuehren.
- `dokumentstapel-aufnehmen` — Dokumentenstapel (PDFs, Excel, Word) einlesen und Inventar erstellen.
- `excel-multi-sheet-export` — 3D-Review-Ergebnis als Excel-Datei mit Arbeitsblaettern je Perspektive exportieren.
- `kreuzblatt-konsistenzpruefung` — Abgleich der drei Dimensionen auf Widersprueche und fehlende Eintraege.
- `pdf-bericht-erzeugen` — 3D-Review-Ergebnis als PDF-Bericht mit Zusammenfassung, Tabellen und Risikoampeln erzeugen.
- `prompt-versionierung` — Prompt-Versionen für den 3D-Review verwalten und aendern.
- `pruefer-uebergabe-paket` — Uebergabepaket für Prueferwechsel mit aktuellem Stand und offenen Positionen.
- `review-durchfuehren` — 3D-Tabellenreview konkret durchfuehren: jede Zeile in allen drei Perspektiven pruefen.
- `risikoampel-aggregation` — Risikoampeln für alle geprueften Positionen aggregieren und Gesamtrisiko einschaetzen.
- `spaltenprompts-definieren` — Spaltenprompts für die drei Pruefperspektiven definieren.
- `tabellenreview-3d-kaltstart-interview` — Kaltstart-Interview: Fallkategorie, Tabellengroesse, Pruefzweck und Exportformat erfassen.
- `vorlage-arbeitsvertrag-portfolio` — Vorlagetabelle für Portfolio-Review von Arbeitsvertraegen im 3D-Format.
- `vorlage-immobilien-portfolio` — Vorlagetabelle für Portfolio-Review von Immobilienvertraegen im 3D-Format.
- `vorlage-ma-due-diligence` — Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format.
- `vorlage-vendor-onboarding-3d` — Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format.
- `wuerfel-aufbauen` — 3D-Wuerfelstruktur aufbauen: Zeilen, Spalten und Perspektiven verknuepfen.
- `zeilenprompts-definieren` — Zeilenprompts für einzelne Pruefpositionen im 3D-Review definieren.

## Worauf besonders achten

- **Kreuzblatt-Konsistenz vor Export pruefen**: Widersprueche zwischen den Dimensionen koennen die Aussagekraft des Berichts untergraben.
- **Prompt-Versionierung dokumentieren**: Unterschiedliche Prompt-Versionen im selben Review produzieren nicht vergleichbare Ergebnisse.
- **Audit-Trail von Beginn an fuehren**: Nachtraegliches Erganzen des Protokolls ist fehleranfaellig und im Zweifel nicht beweissicher.
- **Caching konservativ einsetzen**: Gecachte Ergebnisse werden nicht neu berechnet; Aenderungen im Dokument werden nicht erfasst.
- **Vorlagen nicht ohne Anpassung verwenden**: Vorlage-Spaltenprompts sind Ausgangspunkte, keine abschliessenden Pruefkataloge.

## Typische Fehler

- Wuerfelstruktur ohne Kaltstart-Interview aufbauen; Pruefzweck und Exportformat werden spaeter nicht erfuellt.
- Alle drei Perspektiven mit identischen Prompts besetzen; der Wuerfel verliert seine Informationstiefe.
- Risikoampel-Schwellenwerte nicht explizit definieren; Ampelbewertungen werden inkonsistent.
- Prueferwechsel ohne Uebergabepaket; Nachfolger muss von vorne beginnen.
- Excel-Export ohne Kreuzblatt-Pruefung; Inkonsistenzen werden erst beim Mandanten entdeckt.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
