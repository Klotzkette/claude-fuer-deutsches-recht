---
name: schlussverteilung-aufhebung-vorbereiten
description: Bereitet Schlussverzeichnis, gerichtliche und organschaftliche Freigaben, Schlusstermin, Zahlungslauf, Hinterlegung, Vollzugsabgleich und Aufhebungsübergabe vor. Stoppt jede Auszahlung bei fehlendem Gate.
---

# Schlussverteilung und Aufhebung vorbereiten

## 1. Zweck und Anwendungsfall

Dieser Skill führt das reguläre Verfahren vom freigegebenen Schlussbericht und Rechenwerk bis zum vorbereiteten und belegten Verteilungsvollzug sowie zur Aufhebungsnachbereitung. Er unterscheidet Entwurf, gerichtliche Zustimmung, Schlusstermin, Zahlungsfreigabe, tatsächliche Zahlung und Aufhebungsbeschluss.

Er wird nicht für den abweichenden Abschluss nach Masseunzulänglichkeit verwendet. In dieser Verfahrenslage ist nach §§ 208 bis 211 InsO gesondert zu routen.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-SVA`. Die Fachroute übergibt an `forderungen-sicherheiten-quote-darstellen`, `schlussrechnung-konten-abgleichen` und `berichtserstellung-steuern`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Abschlussprodukte | BER-SB, BER-SR und BER-FQ mit identischem Stichtag | fachlich freigegebene Fassungen |
| Organe | Gläubigerausschuss und erforderliche Zustimmung | Beschlüsse und Protokolle |
| Gericht | Zustimmung, Niederlegung, Bekanntmachung, Schlusstermin und Entscheidungen | Gerichtsakte |
| Verzeichnis | Gläubiger, Rang, Quote, Rückbehalt und Einzelbetrag | BER-FQ |
| Zahlung | verifizierte Empfänger- und Bankdaten | Zahlungsstammdaten mit Nachweis |
| Vollzug | Bankbelege, Rückläufer, Hinterlegungen und Restbestand | Bank und Buchhaltung |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Verteilungsstichtag und Phasenstände

Führen Sie getrennte Stände für den Rechenstichtag des Schlussverzeichnisses, den gerichtlichen Zustimmungs- und Bekanntmachungsstand, den Stand nach Einwendungen oder Änderungen, den freigegebenen Zahlungslauf und den tatsächlichen Vollzug. Eine Änderung der Forderungsbasis oder des verfügbaren Betrags nach Freigabe erzeugt eine neue Rechenfassung; eine bloße spätere Valuta wird als Vollzugsdelta dokumentiert.

Der Phasenvergleich enthält je Position den Betrag des freigegebenen Verzeichnisses, die tatsächlich angewiesene Zahlung, die Bankvaluta, Rückläufer, Hinterlegung und verbleibenden Rest. Die historische freigegebene Liste wird nicht überschrieben. Dadurch bleibt erkennbar, ob eine Differenz aus neuer Berechnung, technischer Ausführung oder Rücklauf stammt.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Prüfen Sie, ob Abschlussreife, Schlussrechnung und Forderungsbasis dieselbe freigegebene Fassung verwenden. Stoppen Sie bei Abweichung.
2. Ermitteln Sie den verfügbaren Betrag aus tatsächlichem Bestand abzüglich belegter Kosten, Masseverbindlichkeiten, gesetzlich oder konkret begründeter Rückbehalte und Hinterlegungen.
3. Prüfen Sie Ausschusszustimmung soweit erforderlich, gerichtliche Zustimmung zur Schlussverteilung, Niederlegung, Bekanntmachung, Fristen, Nachweise und Einwendungen.
4. Erstellen Sie das Schlussverzeichnis mit Gläubigerkennung, Rang, Basis, Quote, Einzelbetrag, Rückbehalt, früheren Abschlägen und Kontrollsumme.
5. Bereiten Sie Schlusstermin und Reaktion auf Einwendungen vor. Jede Änderung erzeugt neue Fassungen von BER-FQ, BER-SVA und betroffenen Berichtszahlen.
6. Erstellen Sie den Zahlungslauf erst nach `G6`. Prüfen Sie Identität und Bankverbindung aus verlässlicher Quelle; eine E-Mail-Änderung wird gesondert verifiziert.
7. Verlangen Sie für den genauen Lauf die namentliche menschliche Freigabe `G7`. Erst dann darf eine technische Zahlung durch befugte Personen erfolgen.
8. Ordnen Sie ausgeführten Zahlungen Bankbeleg und Valuta zu, klären Sie Rückläufer, dokumentieren Sie Hinterlegungen und führen Sie den Schlussbestandsabgleich.
9. Bereiten Sie die Vollzugsmitteilung und Aufhebungsübergabe vor. Erfassen Sie den Status `aufgehoben und belegt` erst nach Eingang des tatsächlichen Beschlusses.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Die Rechenbrücke lautet `tatsächlicher Bestand - belegte Verfahrenskosten - sonstige zu berücksichtigende Masseverbindlichkeiten - konkret begründete Rückbehalte oder Hinterlegungen = verfügbarer Verteilungsbetrag`. Eine pauschale Reserve wird nicht eingesetzt. Die Summe der positionsbezogenen Auszahlungen, Rückbehalte oder Hinterlegungen und einer ausdrücklich ausgewiesenen Rundungsdifferenz muss den verfügbaren Betrag ergeben. Nach Vollzug lautet die zweite Brücke `Anfangsbestand des Zahlungslaufs - valutierte Zahlungen - Gebühren ± Rückläufer = Schlussbestand`.

Prüfen Sie vor Freigabe jede Gläubigerkennung und Zahlstelle gegen die freigegebene Forderungsliste. Änderungsnachweise werden getrennt von der Forderungsfeststellung geführt. Eine Änderung der Bankverbindung verändert nicht Rang oder Forderungsbetrag, verbraucht aber die Zahlungsfreigabe der betroffenen Position.

### 3.3 Qualitätsgates

`G3` verlangt Null-Differenz der Verteilungs- und Kontrollrechnung. `G4` verlangt namentliche Prüfung von Schlussverzeichnis, Rechenweg und Anlagen. `G5` betrifft die konkrete gerichtliche Einreichung samt Zugangsnachweis. `G6` ist erst erfüllt, wenn alle im Verfahren erforderlichen organschaftlichen und gerichtlichen Verteilungsvoraussetzungen sowie Niederlegung, Bekanntmachung, Termin- und Einwendungsstand belegt sind. `G7` umfasst die exakte unveränderte Zahlungsliste, verifizierte Identität und Bankdaten, Vier-Augen-Freigabe und technische Berechtigung. Kein Gate wird durch eine Maschine freigegeben. Eine Änderung von Betrag, Empfänger oder Bankverbindung verbraucht die frühere Zahlungsfreigabe.

Nach Zahlung wird `G7` nicht allein durch einen technischen Erfolgsstatus geschlossen. Erforderlich sind Bankvaluta, Abgleich sämtlicher Positionen, Behandlung von Rückläufern und ein erklärter Schlussbestand. Die Aufhebungsübergabe bleibt bis zur Vollzugsmitteilung und zum tatsächlichen gerichtlichen Beschluss offen.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

Vor `G6` besteht `BER-SVA` aus Schlussverzeichnis, Verteilungsrechnung, Nachweis der Voraussetzungen und Einwendungsjournal. Nach `G6` wird eine separate Zahlungsliste mit Versionskennung, Hash, Gesamtsumme und Positionszahl an die freigebende Person übergeben. Nach `G7` führt das Vollzugsprodukt je Position Anweisung, Valuta, Bankbeleg, Rücklauf oder Hinterlegung. An `berichtserstellung-steuern` gehen anschließend Vollzugsmitteilung, Schlussbestandsabgleich und Entwurf der Aufhebungsübergabe; der Status `aufgehoben` wird erst mit dem Beschlussbeleg gesetzt.

## 4. Quellenpflicht

§§ 187 bis 200 InsO regeln reguläre Verteilung, Schlusstermin, Hinterlegung, Überschuss und Aufhebung. BGH, Beschluss vom 20.11.2014 – IX ZB 16/14, Rn. 11 bis 21, trägt den Grundsatz, dass nach Berichtigung der Masseverbindlichkeiten grundsätzlich die gesamte verwertete Masse verteilt wird; die dortige besondere Rückstellung ist keine allgemeine Reserveermächtigung. BGH, Beschluss vom 24.03.2022 – IX ZB 35/21, Rn. 7 bis 13, grenzt den Abschluss nach § 211 InsO von der regulären Schlussverteilung ab.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** §§ 187 bis 200 InsO tragen die reguläre Verteilungsroute einschließlich Verzeichnis, Behandlung besonderer Forderungslagen, Schlussverteilung, Schlusstermin, Hinterlegung, Überschuss und Aufhebung. BGH IX ZB 16/14 trägt den Grundsatz, dass nach Berichtigung der Masseverbindlichkeiten grundsätzlich die gesamte verwertete Masse zu verteilen ist. BGH IX ZB 35/21 trägt die Abgrenzung des Abschlusses nach § 211 InsO von der regulären Schlussverteilung.

**Trägt nicht:** BGH IX ZB 16/14 erlaubt keinen pauschalen Sicherheitspuffer oder beliebigen Reserveabzug. BGH IX ZB 35/21 ordnet nicht jede Verpflichtung als Alt- oder Neumasseverbindlichkeit ein. Kein Anker ersetzt die Prüfung der konkreten Zustimmung, Bekanntmachung, Einwendung, Bankverbindung oder Zahlung.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-SVA`

1. Voraussetzungen und führende Abschlussfassungen
2. verfügbarer Betrag und zulässige Abzüge
3. Schlussverzeichnis und Kontrollsumme
4. Zustimmungen, Bekanntmachung, Termin und Einwendungen
5. freizugebender Zahlungslauf
6. Zahlungen, Rückläufer und Hinterlegungen
7. Vollzugsabgleich und Aufhebungsübergabe

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Fehlende gerichtliche Zustimmung

Schlussbericht und Rechenwerk sind fertig; die gerichtliche Zustimmung nach § 196 Absatz 2 InsO fehlt. Der Skill kann Schlussverzeichnis und Zahlungsvorlage als Entwurf erzeugen. `G6` bleibt geschlossen; kein Auszahlungslauf erhält den Status freigegeben.

### 6.2 Geänderte Bankverbindung

Kurz vor Auszahlung teilt ein Gläubiger per E-Mail eine neue Bankverbindung mit. Der Skill markiert den Datensatz als ungeklärt, verlangt eine verlässliche Verifikation und setzt die frühere Freigabe für diese Position aus. Andere Positionen werden nur verarbeitet, wenn der genehmigte Lauf dies ausdrücklich zulässt.

### 6.3 Unbegründeter Sicherheitspuffer

Der tatsächliche Bestand beträgt 300.000 Euro; belegte Kosten und Masseverbindlichkeiten betragen 60.000 Euro. Die Arbeitsliste enthält zusätzlich einen pauschalen Puffer von 20.000 Euro ohne benannten Grund. Der Skill setzt den verfügbaren Betrag nicht auf 220.000 Euro, sondern sperrt die Rechnung und verlangt für jeden Abzug Rechtsgrund, Betrag und Beleg. Ohne konkrete Grundlage lautet die Rechenbasis 240.000 Euro; eine Auszahlung erfolgt trotzdem erst nach den weiteren belegten Voraussetzungen und menschlichen Freigaben.
