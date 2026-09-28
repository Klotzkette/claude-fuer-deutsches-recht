---
name: liquiditaetsvorschau-3-6-12-monate
description: "Erstellt rollierende Liquiditätspläne über 13 bis 52 Wochen und grenzt die Fortbestehensprognose nach Paragraf 19 InsO von der Prognose nach Paragraf 18 InsO ab."
---

# 1. Rollierende Planung und Fortbestehensprognose erstellen

## 1.1. Zweck und Anwendungsfall

Erstelle die verlangte rollierende Planung aus Zahlungsdaten und verbinde sie bei entsprechendem Auftrag mit Fortbestehensprognose oder Sanierungsplanung. 13, 26 und 52 Wochen sind operative Planungshorizonte. § 17 InsO verlangt eine eigenständige Prüfung aktueller Zahlungsunfähigkeit, § 19 InsO eine kalendergenaue Zwölfmonatsprognose und § 18 InsO in aller Regel 24 Monate. 52 Wochen nicht ungeprüft mit zwölf Kalendermonaten gleichsetzen.

## 1.2. Eingaben

Verarbeite Kontoauszüge, OPOS, BWA, SuSa, Kreditverträge, Auftragsbestand, Personal-/Steuertermine und vorhandene Planungen. Übernimm Firma, Stichtag, Horizont, Format und Datenquelle, soweit bekannt. Erhebe Betrag, Fälligkeit, Zahlungszeitpunkt, Verfügbarkeit, Beleg und Annahmenstatus. Anfangsbestände abstimmen, private/Gesellschafterzahlungen rechtlich richtig einordnen, keine doppelte Umsatzsteuer, keine Doppelzählung von Kreditrahmen und Ziehung. OCR-Werte auf Salden, Vorzeichen und Dezimalstellen prüfen. Frage nur nach entscheidenden Lücken.

## 1.3. Ablauf

### 1.3.1. Wochenplan und Szenarien

Rechne `Endbestand = Anfangsbestand + Einzahlungen − Auszahlungen` und übertrage den Endbestand in die Folgeperiode. Trenne operativen Cashflow und Finanzierung. Zeige den ersten und höchsten ungedeckten Bedarf sowie spätesten Bereitstellungstag. Prüfe bei knapper Deckung unterwöchig. Für die Monatsdarstellung den Übergang vom Wochenraster abstimmen; außerhalb des erfassten Horizonts keine Nullwerte als vollständige Prognose ausgeben.

Szenarien folgen konkreten Unsicherheiten wie verspätetem Großkundeneingang, Lieferstopp, Sicherheitenbedingung oder Linienablauf. Eine schematische 100-/80-/60-Prozent-Rechnung darf als Sensitivität erscheinen, aber nicht als Behauptung eines tatsächlich erwarteten Teilzuflusses. Bei mehreren Risiken Wechselwirkungen und Doppelabzüge kontrollieren. Finanzierungsbereitschaft, rechtliche Zusage und tatsächlichen Zufluss trennen.

Das Werkzeug `werkzeuge/build_liquiditaetsplan.py` unterstützt die Exportrechnung. Seine operativen Warnsignale sind keine automatische Insolvenzreife-Ampel. Einen vollständigen Dreiwochenblock nicht aus verkürzten Restspalten behaupten. Für § 17 einen gesonderten Status mit tatsächlichem Stichtag, fälligen Rückständen und rechtlich geprüften Zukunftsposten aufstellen; nicht kumulierte Wochenlücken durch die Verbindlichkeiten nur einer Woche teilen.

Für bestätigte Rechenhinweise verlangt der Builder `daten_bestaetigt: true` und je Planwoche vollständige `einnahmen`- und `ausgaben`-Objekte. Setze die Bestätigung erst nach dem tatsächlichen Belegabgleich. Fehlende Wochen nicht mit leeren Nullobjekten auffüllen; ein ausdrücklich belegter Nullbetrag ist etwas anderes als eine fehlende Angabe.

### 1.3.2. Insolvenzrechtliche Prognose

Lies die [Prüfregeln](../../references/insolvenzpruefung.md). Nach § 19 InsO Fortführungswillen und ein schlüssiges, realisierbares Unternehmenskonzept mit Ertrags- und Finanzplan prüfen. Die Aufrechterhaltung der Zahlungsfähigkeit muss in den nächsten zwölf Monaten überwiegend wahrscheinlich sein. Bewertungsstichtag und Informationen aus damaliger Sicht dokumentieren; bei Verschlechterung kurzfristig aktualisieren.

BGH, Urteil vom 13.07.2021 – II ZR 84/20, Rn. 68–85, verlangt nicht für jeden prognostizierten Sanierungsbeitrag einen einklagbaren Anspruch. Entscheidend sind konkrete Tatsachen zu Leistungsfähigkeit, Leistungsbereitschaft, Umfang, Zeitpunkt und Gesamtkonzept. Bloße frühere Hilfen oder weiche Patronate reichen bei andauernden Verlusten regelmäßig nicht. Eine weiche Erklärung ist außerdem kein aktivierbarer Anspruch im Überschuldungsstatus. Aktuelle §-19-Frist und damalige Gesetzeslage des Urteils unterscheiden.

Fehlt eine positive Fortbestehensprognose, Vermögen und Verbindlichkeiten im eigenständigen Überschuldungsstatus bewerten. Negatives Handelsbilanz-Eigenkapital nicht mit Insolvenzreife gleichsetzen. Verwertungswerte, stille Lasten und tatsächlich verwertbare stille Reserven belegen; selbstgeschaffene immaterielle Werte nicht pauschal aktivieren. Einen Rangrücktritt am konkreten Wortlaut, der Rangtiefe und der vorinsolvenzlichen Durchsetzungssperre prüfen. Die Forderung erlischt nicht, Liquidität fließt dadurch nicht zu; BGH IX ZR 133/14.

Für § 18 InsO grundsätzlich auf 24 Monate erweitern und die voraussichtliche Zahlungsfähigkeit bei den tatsächlichen Fälligkeiten beurteilen. Ein hypothetischer Worst Case allein begründet kein abschließendes §-18-Ergebnis. Eine negative §-19-Prognose allein ist noch nicht der vollständige Überschuldungstatbestand. Aktuelle Zahlungsunfähigkeit und § 15a InsO unabhängig von langfristiger Prognose prüfen; Höchstfristen erlauben kein allgemeines Abwarten.

### 1.3.3. Sanierungsplanung und fortlaufende Bearbeitung

Für einen Sanierungsauftrag Liquidität, GuV, Planbilanz, Krisenursachen, Leitbild, Maßnahmen, Kosten, Zeitbedarf und Sensitivitäten zusammenführen. Positive Fortbestehensprognose und nachhaltige Sanierungsfähigkeit sind unterschiedliche Ergebnisse. IDW-S-6-/S-11-Konformität nur bei tatsächlich entsprechender Prüfung und zugänglicher aktueller Standardfassung behaupten. `idw-s6-integrierte-sanierungsplanung` kann vertiefen; der hier beauftragte Plan ist trotzdem fertigzustellen.

Nach neuen Belegen Ist-Werte übernehmen, betroffene Perioden und Szenarien neu rechnen, den Horizont fortschreiben und Abweichungen erläutern. Eine offene Bankbedingung bleibt offen, bis ihr Eintritt belegt ist. Auf Antworten mit einer aktualisierten Rechnung und dem bestellten ausformulierten Schreiben reagieren; keine starre Zahl von Rückfragerunden.

## 1.4. Quellenpflicht

Aktuelle §§ 17, 18, 19, 15a und 15b InsO sowie gegebenenfalls § 1 StaRUG prüfen. Die [Entscheidungskarte](../../references/rechtsprechung/INDEX.md) enthält Volltexte und genaue Reichweiten, insbesondere IX ZR 123/04, II ZR 88/16, II ZR 112/21, IX ZR 133/14 und II ZR 84/20. Tragende Aussagen am Original belegen, keine Kommentar-/IDW-Fundstellen aus Modellwissen ergänzen.

## 1.5. Ausgabeformat

Liefere die vereinbarte Excel-Planung mit erhaltenen Formeln und Quellen-/Annahmenfeldern; optional ein HTML-Padlet oder Markdown. Ohne Dateiexport nachrechenbare Tabellen liefern. Statusfelder unabhängig von Wochen-Cashflows führen. Negative Bestände sind Finanzierungsbedarf; Tabellenfarben keine gerichtlichen Feststellungen.

Ein beauftragter Finanzierungsvermerk, Bankbrief oder Prognosebericht wird vollständig ausformuliert. Formatierte Texte in Times New Roman 11 pt, dezimale Gliederung; keine Skelette. Interne Quellen-/Techniknotizen getrennt halten. Keinen ungefragten Insolvenzantrag oder Vertragsentwurf und keinen Versand ohne Auftrag.

## 1.6. Beispiel

Eine Gesellschaft hat eine operative 52-Wochen-Planung und negatives handelsbilanzielles Eigenkapital. Für § 19 ergänze gegebenenfalls die fehlenden Tage bis zum Ende der nächsten zwölf Monate, prüfe Finanzierung und Unternehmenskonzept und bei fehlender positiver Prognose den Überschuldungsstatus. Für § 18 fehlen grundsätzlich weitere zwölf Monate. Ein als „qualifiziert“ bezeichnetes Darlehen darf erst nach Klauselprüfung anders behandelt werden; es wird nicht zum Kontoguthaben.

Ein Investor hat noch keine einklagbare Zahlungspflicht übernommen, aber eine konkrete Finanzierungsprüfung abgeschlossen und nachweislich Mittel für einen bestimmten Betrag und Termin reserviert. Würdige diese Unterlagen positiv und prüfe verbleibende Bedingungen, Leistungsbereitschaft und Deckung im Gesamtplan. Weder allein wegen des fehlenden Anspruchs negativ bescheinigen noch die Reservierung ohne Prüfung als unbedingte Zahlung behandeln.
