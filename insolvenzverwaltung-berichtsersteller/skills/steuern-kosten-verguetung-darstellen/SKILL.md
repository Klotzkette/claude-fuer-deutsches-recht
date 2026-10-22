---
name: steuern-kosten-verguetung-darstellen
description: Erstellt das Fachmodul zu Steuerperioden, Bescheiden, Verfahrenskosten, Masseverbindlichkeiten, Vergütungsantrag, Festsetzung und Zahlung. Verhindert die Verwechslung von Erwartung, Antrag, Beschluss und Geldfluss.
---

# Steuern, Kosten und Vergütung darstellen

## 1. Zweck und Anwendungsfall

Dieser Skill hält steuerliche Positionen, Verfahrenskosten, sonstige Masseverbindlichkeiten und Vergütung statusrichtig auseinander. Er wird für Zwischen- und Schlussberichte, Abschlussreife, Schlussrechnung und Verteilungsrechnung eingesetzt.

Der Skill ersetzt keine steuerliche Erklärung oder Vergütungsfestsetzung. Er stellt den Aktenstand, die wirtschaftliche Wirkung und offene Schritte so dar, dass Bericht und Rechenwerk dieselben Positionen verwenden.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-SKV`. Die Fachroute übergibt an `schlussrechnung-konten-abgleichen`, die Berichtsskills und `schlussverteilung-aufhebung-vorbereiten`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Steuern | Steuerart, Zeitraum, Erklärung, Anmeldung, Bescheid, Zahlung und Einspruch | Steuerakte |
| Prüfungen | Betriebsprüfung, Anfragen, Rückstellungen und Korrespondenz | Finanzamt und Beratung |
| Gerichtskosten | Kostenrechnung, Vorschuss, Zahlung und Erstattung | Gerichtsakte |
| Masseverbindlichkeiten | Gläubiger, Grund, Zeitraum, Fälligkeit, Prüfung und Zahlung | Buchhaltung und Vertrag |
| Vergütung | Berechnungsgrundlage, Antrag, Beschluss, Rechtsmittel und Zahlung | Vergütungsakte |
| Rechnung | zugehörige Buchungen und Bankbelege | BER-SR |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Perioden- und Statusdelta

Führen Sie je Steuerart, Kostenposition, Masseverbindlichkeit und Vergütungsvorgang eine Statuskette von der Entstehungs- oder Leistungsperiode bis zur Zahlung. Für Steuern werden mindestens Zeitraum, Erklärung oder Anmeldung, behördliche Festsetzung, Rechtsbehelf, Fälligkeit, Zahlung oder Erstattung und offener Betrag getrennt. Für Vergütung werden Berechnungsgrundlage, Antrag, gerichtliche Festsetzung, Rechtsmittelstand, Rechtskraftstatus und Zahlung getrennt. Für sonstige Kosten werden Leistungsgrund, Rechnung, sachliche Prüfung, Fälligkeit, Buchung und Zahlung geführt.

Der Deltaausweis nennt den Stand der letzten Berichtsfassung, Zugänge, Herabsetzungen, Zahlungen, Erstattungen, Statuswechsel und den Stand zum neuen Stichtag. Eine nach dem Stichtag eingehende Festsetzung kann einen bereits stichtagsbezogenen Sachverhalt belegen, muss aber mit ihrer Nachlaufwirkung offen ausgewiesen werden. Das Datum eines Bescheids oder einer Rechnung entscheidet nicht allein über wirtschaftliche oder insolvenzrechtliche Zuordnung.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Erstellen Sie je Steuerart und Zeitraum eine Statuszeile. Trennen Sie Erklärung, Berechnung, Anmeldung, Bescheid, Fälligkeit, Zahlung, Erstattung und Rechtsbehelf.
2. Prüfen Sie bei erwarteten Erstattungen, ob ein Anspruch, ein Bescheid oder nur eine Prognose vorliegt. Buchen Sie keine Erwartung als verfügbaren Bestand.
3. Trennen Sie Verfahrenskosten nach § 54 InsO von sonstigen Masseverbindlichkeiten. Ordnen Sie Grund, Zeitraum und Rang nicht allein nach Rechnungsdatum zu.
4. Erfassen Sie offene Masseverbindlichkeiten mit Betrag, Fälligkeit, Bestreiten, Rückstellung oder Zahlung und konkretem Beleg.
5. Führen Sie Vergütung und Auslagen mit Status beantragt, fachlich geprüft, festgesetzt, angefochten, rechtskräftig und bezahlt. Überspringen Sie keinen Status.
6. Prüfen Sie die Übereinstimmung zwischen Antrag, Beschluss, Buchhaltung, Bankzahlung und Bericht. Erklären Sie Differenzen.
7. Bewerten Sie die Auswirkung jeder offenen Steuer- oder Kostenposition auf Abschlussreife, Rückbehalt und Verteilung.
8. Übergeben Sie nur belegte Beträge an BER-SR und BER-FQ.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Erstellen Sie je Position eine Betragsbrücke aus Anfangsbestand offener Positionen plus neuen, belegten Zugängen minus Herabsetzungen, Zahlungen und Erstattungen gleich Endbestand offener Positionen. Stimmen Sie Zahlungen und Erstattungen positionsbezogen mit Buchhaltung und Bank ab. Eine Sammelzahlung wird auf ihre Bestandteile aufgelöst; ein in einer Zahlung enthaltener Fremdanteil wird nicht der Masseposition zugeschlagen.

Für die Verteilungsrechnung trennen Sie tatsächlichen Bankabfluss, festgesetzte und noch nicht gezahlte Verpflichtung, konkret begründeten Rückbehalt und bloße Prognose. Dieselbe Position darf nicht zugleich als bereits bezahlte Ausgabe und als nochmals abzuziehender Rückbehalt erscheinen. Die Summe der an `BER-SR` übergebenen Zahlungsbewegungen und die Summe der an `BER-FQ` übergebenen offenen Abzüge werden daher getrennt kontrolliert.

### 3.3 Qualitätsgates

`G2` verlangt einen periodengenauen, belegten Status der wesentlichen Steuer-, Kosten- und Vergütungspositionen samt Zuständigkeit und nächster Frist. `G3` verlangt eine Null-Differenz der tatsächlich gebuchten und bezahlten Beträge zu `BER-SR` sowie eine widerspruchsfreie Behandlung der offenen Positionen in `BER-FQ`. Eine unklare Doppelberücksichtigung, eine nicht zugeordnete Sammelzahlung, eine nicht festgesetzte Vergütung oder eine nur erwartete Erstattung sperrt den endgültigen verfügbaren Betrag. Die Einreichung von Steuererklärungen, Rechtsbehelfen oder Vergütungsanträgen erfordert gesonderte menschliche Freigabe für die konkrete Fassung.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

An `schlussrechnung-konten-abgleichen` geht eine Liste der tatsächlichen Zahlungen und Erstattungen mit Position, Betrag, Valuta, Buchungskonto und Bankbeleg. An `forderungen-sicherheiten-quote-darstellen` gehen nur konkret zu behandelnde offene Verfahrenskosten, Masseverbindlichkeiten oder Rückbehalte mit Betrag und Begründung. An die Berichtsskills geht die ausformulierte Statusdarstellung einschließlich offener Perioden und Abschlusswirkung. Antrag, Festsetzung, Rechtskraft und Zahlung werden bei jeder Übergabe als eigene Felder geführt.

## 4. Quellenpflicht

§§ 53 bis 55 InsO trennen Verfahrenskosten und sonstige Masseverbindlichkeiten. §§ 63 und 64 InsO sowie die InsVV betreffen Vergütung, Auslagen und gerichtliche Festsetzung. BGH, Beschluss vom 11.11.2021 – IX ZB 19/20, Rn. 12 und 14 bis 21, trägt die Prüfung von Tätigkeitsabschluss und Vergütungsfälligkeit, nicht eine beliebige Teilfestsetzung.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** §§ 53 bis 55 InsO tragen die Trennung von Verfahrenskosten und sonstigen Masseverbindlichkeiten. §§ 63 und 64 InsO sowie die InsVV tragen Berechnung, Antrag und gerichtliche Festsetzung der Vergütung in den in der Quellenkarte bezeichneten Grenzen. BGH IX ZB 19/20 trägt die Prüfung des Tätigkeitsabschlusses und der Vergütungsfälligkeit; vor Fälligkeit ist nur die dort abgegrenzte Vorschussroute zu prüfen.

**Trägt nicht:** Die Quellen erlauben nicht, einen Antrag als Festsetzung, eine Festsetzung als Zahlung oder eine erwartete Steuererstattung als verfügbaren Massebestand darzustellen. BGH IX ZB 19/20 erlaubt keine beliebige zeitabschnittsweise Teilfestsetzung. Die Quellen ersetzen weder Bescheid, Beschluss, Rechtskraftnachweis noch Bankbeleg des Einzelfalls.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-SKV`

1. Steuerstatus nach Art und Zeitraum
2. Erklärungen, Bescheide, Zahlungen und Rechtsbehelfe
3. Verfahrenskosten
4. sonstige Masseverbindlichkeiten
5. Vergütung und Auslagen nach Status
6. Auswirkung auf Abschlussreife und Verteilung
7. Abgleich mit Buchhaltung und Bank

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Erwartete Erstattung

Die Steuerberatung erwartet 25.000 Euro; ein Bescheid und Zahlungseingang fehlen. Der Skill zeigt die Prognose und ihren Grund, übernimmt aber null Euro in den verfügbaren Bestand. Ein Nachforderungs- oder Wiedervorlagepunkt wird angelegt.

### 6.2 Vergütung nur beantragt

Der Vergütungsantrag nennt 80.000 Euro; das Gericht hat noch nicht entschieden. Der Bericht bezeichnet den Betrag als beantragt. Die Verteilungsrechnung behandelt nur eine konkret begründete, transparent ausgewiesene Position und behauptet keine Festsetzung oder Zahlung.

### 6.3 Festsetzung weicht vom Antrag ab

Beantragt wurden 80.000 Euro; das Gericht setzt 72.000 Euro fest, bezahlt ist zum Stichtag noch nichts. Der Skill führt 80.000 Euro als historischen Antragsbetrag, 72.000 Euro als festgesetzten Betrag und null Euro als Zahlung. Er korrigiert eine zuvor auf dem Antrag beruhende offene Rechenposition auf den belegten Festsetzungsstand, gibt aber keinen Bankabfluss an `BER-SR` weiter. Die betroffenen Abschluss- und Verteilungsfassungen werden neu versioniert.
