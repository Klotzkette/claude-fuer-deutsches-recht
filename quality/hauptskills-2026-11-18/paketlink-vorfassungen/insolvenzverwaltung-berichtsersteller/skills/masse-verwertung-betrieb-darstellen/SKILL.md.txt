---
name: masse-verwertung-betrieb-darstellen
description: Erstellt das Fachmodul zu Masse, Fremdrechten, Bewertung, Verwertung und Betriebsfortführung. Verknüpft Vermögensgegenstände mit Verträgen, Zahlungen, Kosten, Personal und dem tatsächlichen Masseeffekt.
---

# Masse, Verwertung und Betrieb darstellen

## 1. Zweck und Anwendungsfall

Dieser Skill bildet Vermögensbestand, Rechte Dritter, Verwertung und gegebenenfalls Betriebsfortführung in einer konsistenten Fachfassung ab. Er wird verwendet, wenn ein Zwischen- oder Schlussbericht Vermögenskomplexe, Veräußerungen, Einziehungen, Freigaben, Vertragsabwicklung, Personal oder Stilllegung erklären muss.

Der Skill trennt rechtliche Zugehörigkeit, wirtschaftliche Bewertung, vereinbarte Verwertung, tatsächliche Zahlung und Nettoeffekt. Ein Gegenstand ist nicht verwertet, nur weil ein Vertrag unterzeichnet wurde.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-MV`. Die Fachroute übergibt an `zwischenbericht-erstellen`, `schlussbericht-erstellen` und `schlussrechnung-konten-abgleichen`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Masseverzeichnis | Gegenstände, Forderungen, Rechte, Beteiligungen und Daten | Inventur und Eröffnungsunterlagen |
| Fremdrechte | Aus- und Absonderungsanzeigen, Eigentum, Leasing und Sicherheiten | Verträge und Korrespondenz |
| Bewertung | Gutachten, Angebote, Schätzungen und Buchwerte | bewertende Unterlagen |
| Verwertung | Ausschreibung, Vertrag, Genehmigung, Rechnung, Zahlung und Übergabe | Verwertungsakte |
| Betrieb | Liquidität, Umsatz, Kosten, Personal, Waren, Verträge und Genehmigungen | Betriebsakte |
| Abrechnung | Verwertungskosten, Umsatzsteuer, Kostenbeiträge und Nettoerlös | Buchhaltung |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Objekt- und Stichtagsüberleitung

Für jeden Vermögenskomplex führen Sie eine Objektkarte mit Bestand zu Beginn der Berichtsperiode, Zugängen, Abgängen, Wertkorrekturen, Verwertungsstatus und Bestand am Stichtag. Die Kontrollbeziehung lautet `Anfangsbestand + Zugänge - endgültige Abgänge ± belegte Korrekturen = Endbestand`. Der Wertansatz wird separat geführt; eine Abschreibung oder neue Schätzung ist kein körperlicher Abgang. Ereignisse nach dem Stichtag erscheinen in einer Nachlaufspalte und verändern den stichtagsbezogenen Bestand nur, wenn sie als später eingegangener Beleg eine bereits am Stichtag bestehende Tatsache nachweisen.

Die Statuskette lautet mindestens `ermittelt`, `rechtlich zugeordnet`, `bewertet`, `Verwertung beschlossen`, `Vertrag geschlossen`, `übergeben`, `fakturiert`, `bezahlt`, `Kosten abgerechnet` und `erledigt`. Nicht einschlägige Stufen werden begründet; sie werden nicht still übersprungen. Für Fremdrechte wird zusätzlich festgehalten, ob Anspruch nur angemeldet, geprüft, anerkannt, bestritten oder vollzogen ist.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Erstellen Sie je Vermögenskomplex eine eindeutige Objektkennung und ordnen Sie Eigentum, Besitz, Massezugehörigkeit und Fremdrechte getrennt zu.
2. Vergleichen Sie Eröffnungswert, Gutachtenwert, Angebot, Vertragswert, Rechnung, Zahlung und Nettoerlös. Erläutern Sie erhebliche Abweichungen.
3. Prüfen Sie bei Aussonderung und Absonderung Anspruch, Gegenstand, Individualisierung, Besitz, Sicherheit, Verwertungsbefugnis und Abrechnung.
4. Dokumentieren Sie Verwertungsweg, Auswahl, erforderliche Zustimmung, Käufer, Vertrag, Fälligkeit, Zahlung, Übergabe, Gewährleistung und Restforderung.
5. Ordnen Sie Kosten unmittelbar oder nachvollziehbar zu. Weisen Sie Brutto- und Nettoeffekt aus, ohne Umsatzsteuer oder Kostenbeiträge doppelt zu behandeln.
6. Bei Betriebsfortführung stellen Sie Zeitraum, Entscheidung, Liquidität, Umsatz, Wareneinsatz, Personal, Verträge, Risiken und tatsächlichen Masseeffekt dar.
7. Prüfen Sie nicht verwertete Gegenstände einzeln. Nennen Sie Ermittlungen, Rechtslage, Kosten-Nutzen-Abwägung und Entscheidung; verwenden Sie keine pauschale Leerformel.
8. Übergeben Sie Zahlungsbewegungen an BER-SR und Sicherheitenauswirkungen an BER-FQ.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Der Nettoeffekt jedes Verwertungsvorgangs wird aus tatsächlich zuordenbaren Zahlungseingängen abzüglich belegter unmittelbar zugeordneter Kosten und abgeführter Fremdanteile übergeleitet. Vertragswert, Rechnung und offene Restforderung stehen daneben, dürfen den Zahlungseingang aber nicht ersetzen. Die Summe der Objekt-Nettoeffekte wird gegen die einschlägigen Buchhaltungskonten und Bankbewegungen abgestimmt. Interne Umbuchungen und durchlaufende Fremdgelder werden ohne wirtschaftliche Doppelzählung ausgewiesen.

Für eine Betriebsfortführung wird eine eigene Brücke gerechnet: Anfangsliquidität plus betriebliche Einzahlungen minus betriebliche Auszahlungen ergibt Endliquidität, bereinigt um periodenfremde und finanzierende Bewegungen. Daneben werden offene Forderungen, Verbindlichkeiten und Bestandsveränderungen gezeigt, damit ein positiver Bankdelta nicht fälschlich als positives Betriebsergebnis bezeichnet wird.

### 3.3 Qualitätsgates

`G2` verlangt für jeden wesentlichen Objektkomplex eine nachvollziehbare Kette aus Identität, Massezuordnung, Fremdrechtsprüfung, Bewertung, Entscheidung und aktuellem Status. Fehlt ein tragender Beleg, nennt das Gate genau die gesperrte Aussage. `G3` verlangt, dass Zahlungseingänge und Kosten je Objekt auf Bank und Buchhaltung überleiten und die Gesamtsumme mit `BER-SR` übereinstimmt. Eine Differenz, eine wesentliche offene Restforderung oder ein nur unterzeichneter, aber nicht vollzogener Vertrag sperrt die Kennzeichnung `erledigt`. Eine wesentliche, nicht konkret behandelte Verwertung sperrt die positive Abschlussreife.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

An `zwischenbericht-erstellen` oder `schlussbericht-erstellen` gehen die ausformulierte Objekt- und Betriebsdarstellung, die wesentlichen Deltas und die Restpositionsliste. An `schlussrechnung-konten-abgleichen` gehen eine Zahlungsliste mit Bankbeleg, Buchungskonto, Objektkennung und Kostenabgrenzung. An `forderungen-sicherheiten-quote-darstellen` gehen je Sicherheitenkomplex Forderung, Gegenstand, Verwertungsbefugnis, Bruttoerlös, Kosten, Fremdanteil und verbleibender Ausfallstatus. Die Übergabe darf keinen Vertragswert als Zahlung kennzeichnen.

## 4. Quellenpflicht

§§ 35 und 36 InsO betreffen Masseumfang und Unpfändbarkeit. §§ 47 bis 52 InsO trennen Aussonderung und Absonderung; § 166 InsO betrifft bestimmte Verwertungsbefugnisse. § 80 InsO ist für die Verwaltungs- und Verfügungsbefugnis zentral. Keine dieser Normen ersetzt die Prüfung des konkreten Eigentums, Vertrags und Bestellungsbeschlusses.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** §§ 35 und 36 InsO tragen die Prüfung von Masseumfang und Unpfändbarkeit; §§ 47 bis 52 InsO die Unterscheidung von Aus- und Absonderung; § 80 InsO den Übergang der Verwaltungs- und Verfügungsbefugnis; § 166 InsO die in der Quellenkarte bezeichneten Verwertungsbefugnisse. § 160 InsO trägt die Prüfung einer erforderlichen Zustimmung bei besonders bedeutsamen Rechtshandlungen.

**Trägt nicht:** Die Normen belegen weder Eigentum noch Massezugehörigkeit, Verwertungsbefugnis, Zustimmung, Übergabe oder Zahlung im Einzelfall. Eine Objektbezeichnung wie „Kommission“, „Leasing“ oder „Sicherheit“ ersetzt keine Vertrags- und Belegprüfung; ein Kaufvertrag belegt keinen vollständigen Massezufluss.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-MV`

1. Vermögens- und Rechteübersicht
2. Bewertung und Veränderungen
3. Fremdrechte und Verwertungsbefugnis
4. Verwertung nach Komplexen
5. Betrieb, Verträge und Personal
6. Kosten, Zahlungen und Nettoeffekt
7. Restpositionen, Risiken und Übergaben

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Kaufpreis nur teilweise bezahlt

Eine Maschine wurde für 170.000 Euro verkauft; 150.000 Euro sind eingegangen. BER-MV zeigt Vertrag, Übergabe und offene Restforderung getrennt. BER-SR übernimmt nur den Zahlungseingang. Der Schlussbericht darf nicht von einem vollständig realisierten Erlös sprechen.

### 6.2 Fremde Kommissionsware

Waren sind als „Kommission“ etikettiert. Der Skill prüft Vereinbarung, eigenen oder fremden Namen, Rechnung, Eigentum, Absatzrisiko und Erlösabrechnung. Die Bezeichnung allein wird nicht als Aussonderungsnachweis behandelt.

### 6.3 Fortführung mit irreführendem Liquiditätsplus

Während der Fortführung steigen die Bankbestände um 90.000 Euro. Darin enthalten sind jedoch 120.000 Euro aus dem Verkauf einer Altanlage; zugleich sind Löhne von 35.000 Euro und Lieferantenrechnungen von 20.000 Euro noch unbezahlt. Der Skill trennt den periodenfremden Verwertungserlös, die offenen Verpflichtungen und die tatsächlichen betrieblichen Zahlungsströme. Er berichtet weder ein positives Betriebsergebnis noch einen freien Massezuwachs, bevor die Brücke und die offenen Positionen geprüft sind.
