---
name: forderungen-sicherheiten-quote-darstellen
description: Erstellt das Forderungs- und Verteilungsmodul. Gleicht gerichtliche Tabelle, Rang, Bestreiten, Bedingungen, Sicherheiten, Verwertungsausfall, Rückbehalte, Abschläge und Quote ohne Doppelbefriedigung ab.
---

# Forderungen, Sicherheiten und Quote darstellen

## 1. Zweck und Anwendungsfall

Dieser Skill bildet die Grundlage der Forderungsdarstellung und Verteilungsrechnung. Er wird für Zwischenberichte, Schlussberichte, Schlussverzeichnis, Abschlags- oder Schlussverteilung und gerichtliche Rückfragen verwendet. Maßgeblich ist der belegte gerichtliche Tabellen- und Prüfungsstand.

Der Skill unterscheidet Anmeldung, Prüfung, Feststellung, Bestreiten, Rang, Bedingung, Sicherung und tatsächliche Teilnahme. Er verhindert eine Doppelbefriedigung gesicherter Gläubiger und eine Quote aus bloßen Schätzwerten.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-FQ`. Die Fachroute übergibt an `schlussrechnung-konten-abgleichen`, `schlussverteilung-aufhebung-vorbereiten` und die Berichtsskills. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Tabelle | gerichtlicher Tabellenstand und Prüfvermerke | Gerichtsakte |
| Anmeldungen | Betrag, Grund, Rang, Belege und Änderungen | Anmeldeakte |
| Bestreiten | Widerspruch, Feststellungsprozess und Nachweise | Gerichts- und Prozessakte |
| Sicherheiten | Recht, Gegenstand, Forderung, Erlös, Kosten und Ausfall | Sicherheitenabrechnung |
| Verteilung | verfügbarer Betrag, Rückbehalte, Abschläge und frühere Zahlungen | BER-SR und Zahlungshistorie |
| Fristen | Niederlegung, Bekanntmachung, Nachweise, Änderungen und Einwendungen | Gerichtsverkehr |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Forderungsstichtag und Delta

Führen Sie mindestens vier getrennte Stände: letzte eingereichte Tabelle, gerichtlicher Tabellenstand zum Berichtsstichtag, nach dem Stichtag eingegangene gerichtliche Änderung und interne Arbeitsliste. Für jede Tabellenposition lautet die Deltaformel `alter berücksichtigungsfähiger Betrag + Feststellungen + nachgewiesene Ausfälle + zulässige Statuszugänge - Herabsetzungen - erledigte oder nicht teilnehmende Beträge = neuer berücksichtigungsfähiger Betrag`. Eine bloße Änderung der Gläubigeranschrift oder Zahlstelle verändert die Forderungsbasis nicht.

Jede Differenz zwischen gerichtlicher Tabelle und Arbeitsliste erhält eine Positionskennung, den alten und neuen Status, Betrag, Beleg, Wirksamkeitszeitpunkt und Auswirkung auf Basis, Rückbehalt und Einzelzahlung. Nachlaufänderungen werden nicht still in eine schon freigegebene Quote eingerechnet. Sie lösen eine neue `BER-FQ`-Fassung und die Prüfung aus, welche Bekanntmachungs-, Einwendungs- oder Verteilungsschritte tatsächlich betroffen sind.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Importieren Sie den gerichtlichen Tabellenstand positionsbezogen. Halten Sie Kanzleiabweichungen getrennt und kennzeichnen Sie die maßgebliche Quelle.
2. Ordnen Sie jeder Forderung Betrag, Rechtsgrund, Rang, Feststellungsstatus, Bestreitenden, Bedingung, Sicherheit und frühere Zahlung zu.
3. Prüfen Sie bestrittene Forderungen nach §§ 189 bis 192 InsO. Erfassen Sie Nachweis, Eingangsdatum, Verfahren und erforderlichen Rückbehalt.
4. Prüfen Sie gesicherte Forderungen nach § 190 InsO. Stellen Sie Forderung, Sicherheitenerlös, Kosten und nachgewiesenen Ausfall getrennt dar.
5. Berechnen Sie die sichere Forderungsbasis und zusätzliche Rückbehaltsbasis. Berücksichtigen Sie frühere Abschlagsverteilungen und Rundungen positionsbezogen.
6. Ermitteln Sie den verfügbaren Verteilungsbetrag ausschließlich aus BER-SR und den konkret begründeten Abzügen. Verwenden Sie keine pauschale Reserve.
7. Berechnen Sie Quote, Einzelbetrag, Rückbehalt und Kontrollsumme. Die Summe der Einzelpositionen muss der Ausschüttungs- und Rückbehaltssumme entsprechen.
8. Versionieren Sie jede Änderung des Tabellen-, Nachweis- oder Verteilungsstands und lösen Sie die betroffenen Freigaben neu aus.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Erstellen Sie vier Kontrollsummen: angemeldeter Gesamtbetrag, tabellarisch festgestellter Betrag, für die konkrete Verteilung berücksichtigte Basis und gesondert behandelte Rückbehaltsbasis. Die Quotenrechnung lautet nachvollziehbar `verfügbarer Verteilungsbetrag / freigegebene Forderungsbasis`; sie wird nur für die einschlägige Ranggruppe angewandt. Je Position werden Quotenbetrag, frühere Abschläge, Rückbehalt und Auszahlungsbetrag getrennt gerechnet. Die Summe aus Auszahlungen, wirksam behandelten Rückbehalten oder Hinterlegungen und verbleibendem Rest muss auf den verfügbaren Betrag überleiten. Rundung wird positionsbezogen ausgewiesen und nicht durch Änderung der Forderungsbasis versteckt.

Bei Absonderung führen Sie volle Anmeldung, Sicherheitenwert oder Verwertungserlös, Verwertungskosten, belegten Ausfall und bereits erhaltene Zahlungen in getrennten Spalten. Der Sicherheitenerlös wird nicht zugleich vom verfügbaren Massebestand und von der Forderungsbasis abgezogen, wenn dies denselben wirtschaftlichen Vorgang doppelt erfassen würde.

### 3.3 Qualitätsgates

`G3` verlangt eine positionsweise reproduzierbare Forderungsbasis, den aus `BER-SR` übernommenen verfügbaren Betrag und eine Null-Differenz der Kontrollsumme. Eine ungeklärte Tabellenabweichung, ein nur geschätzter Absonderungsausfall oder eine nicht aufgelöste Rundungsdifferenz sperrt die Quote. `G6 Verteilung` verlangt Ausschusszustimmung soweit erforderlich, gerichtliche Zustimmung zur Schlussverteilung sowie den belegten Niederlegungs-, Bekanntmachungs-, Termin- und Einwendungsstand. `G7` verlangt die unveränderte freigegebene Zahlungsliste, verifizierte Identität und Bankdaten sowie die Vier-Augen-Freigabe. Ein späterer Adress- oder Bankdatenwechsel öffnet `G7` für die betroffene Position erneut.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

An `schlussbericht-erstellen` wird die zusammengefasste Forderungs- und Sicherheitenlage mit dem maßgeblichen Tabellenstand übergeben. An `schlussverteilung-aufhebung-vorbereiten` gehen dagegen das vollständige positionsbezogene Schlussverzeichnis, die Rechenparameter, frühere Abschläge, Rückbehalte, Rundungslogik und Kontrollsumme. An `schlussrechnung-konten-abgleichen` gehen nur die tatsächlich gezahlten Ausschüttungen und belegten Hinterlegungen. Die Übergabe benennt ausdrücklich, ob eine Zahl Tabellenbetrag, Verteilungsbasis, Rückbehalt oder Zahlung ist.

## 4. Quellenpflicht

§§ 174 bis 178 InsO regeln Anmeldung, Tabelle und Feststellung. §§ 187 bis 195 InsO regeln Verteilungsverzeichnis, Nachweise, Sicherheiten, Bedingungen, Änderungen und Einwendungen. BGH, Urteil vom 09.03.2017 – IX ZR 177/15, Rn. 15 bis 17, trägt die Trennung zwischen voller Anmeldung und Teilnahme an der Verteilung sowie den Ausschluss einer Doppelbefriedigung. Das Erfordernis des nachgewiesenen Ausfalls folgt aus § 190 Absatz 1 InsO. BGH, Beschluss vom 13.09.2012 – IX ZB 143/11, Rn. 6 bis 10, betrifft den Nachweis nach § 189 InsO. BGH, Beschluss vom 22.03.2007 – IX ZB 8/05, Rn. 8 bis 11, betrifft eine erst nach Bekanntmachung und Niederlegung des Schlussverzeichnisses angemeldete Forderung und keinen allgemeinen Ausschluss für alle Zwecke.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** §§ 174 bis 178 und §§ 187 bis 195 InsO tragen die getrennte Behandlung von Anmeldung, Feststellung, Verzeichnis, Nachweis, Sicherheit, Bedingung, Änderung und Einwendung. BGH IX ZR 177/15 trägt die Trennung von Anmeldung und Verteilung sowie den Ausschluss einer Doppelbefriedigung; § 190 Absatz 1 InsO trägt das Erfordernis des nachgewiesenen Ausfalls. BGH IX ZB 143/11 trägt die in der Quellenkarte beschriebene Qualität des Nachweises nach § 189 InsO; BGH IX ZB 8/05 trägt die dort abgegrenzte Folge einer erst nach Bekanntmachung und Niederlegung angemeldeten Forderung.

**Trägt nicht:** Die Anker erlauben weder Doppelbefriedigung noch einen geschätzten Ausfall als feststehende Verteilungsbasis. Sie begründen auch keinen allgemeinen Ausschluss jeder späteren Forderungsanmeldung und ersetzen nicht den konkreten gerichtlichen Tabellen- und Nachweisstand.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-FQ`

1. maßgeblicher Tabellen- und Prüfungsstand
2. Forderungen nach Rang und Status
3. bestrittene, bedingte und geänderte Forderungen
4. Sicherheiten, Erlöse und Ausfälle
5. verfügbarer Betrag und Rückbehalte
6. Quote, Einzelbeträge und Kontrollsumme
7. Fristen, Einwendungen und Freigabestatus

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Gesicherte Bankforderung

Die Bank meldet 250.000 Euro an. Aus der Sicherheit wurden 200.000 Euro erlöst; der Ausfall von 50.000 Euro ist belegt. Der Skill führt die volle Anmeldung im Tabellenkontext, berücksichtigt für die Verteilung aber nur den Ausfall. Er zieht den Sicherheitenerlös nicht ein zweites Mal ab.

### 6.2 Bestrittene Forderung

Eine Forderung über 100.000 Euro ist bestritten; ein rechtzeitiger Nachweis nach § 189 InsO liegt vor. Der Skill nimmt sie nicht wie eine unstreitige Auszahlung auf. Er berechnet und kennzeichnet den erforderlichen Rückbehalt und nennt Nachweis sowie offene gerichtliche Behandlung.

### 6.3 Delta nach einem Abschlag

Bei der letzten Abschlagsverteilung betrug die berücksichtigte Basis 1.000.000 Euro; ein Gläubiger erhielt auf 100.000 Euro bereits 5.000 Euro. Vor der Schlussverteilung wird seine Forderung auf 80.000 Euro berichtigt und eine andere Forderung über 20.000 Euro festgestellt. Der Skill ändert beide Positionen mit Beleg und Zeitpunkt, berechnet die Schlussquote auf der neuen Gesamtbasis und zieht den früheren Abschlag nur bei der tatsächlich begünstigten Position ab. Die Kontrollsumme weist Auszahlung, etwaige Rückbehalte und Restbestand getrennt aus.
