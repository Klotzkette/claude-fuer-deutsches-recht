---
name: schlussrechnung-konten-abgleichen
description: Erstellt die Schlussrechnung und den belegten Dreifachabgleich von Bank, Kasse, Buchhaltung und Berichtsrechnung. Klärt Differenzen, Unterrechnungen, Fremdgeld, Vergütung und Belegketten vor der Verteilung.
---

# Schlussrechnung und Konten abgleichen

## 1. Zweck und Anwendungsfall

Dieser Skill baut die Schlussrechnung aus Einzelbewegungen und Belegen auf. Er verhindert, dass Kontostand, Buchhaltungssaldo und Berichtsrechnung ungeprüft gleichgesetzt werden. Er wird für Zwischenrechnungen, Schlussrechnungen, gerichtliche Rückfragen und die Vorbereitung einer Verteilung verwendet.

Das Produkt ist ein prüffähiges Rechenwerk mit Belegindex und Differenzprotokoll. Es ersetzt nicht die gerichtliche Prüfung, einen Vergütungsbeschluss oder die Freigabe eines Zahlungslaufs.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-SR`. Die Fachroute übergibt an `steuern-kosten-verguetung-darstellen`, `forderungen-sicherheiten-quote-darstellen` und `schlussbericht-erstellen`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Konten | vollständige Auszüge aller Masse-, Anderkonten und relevanten Unterkonten | Bankoriginale |
| Kasse | Kassenbuch, Zählprotokolle und Barbelege | Kassenunterlagen |
| Buchhaltung | Journal, Kontenblätter, Saldenliste und Eröffnungswerte | Finanzbuchhaltung |
| Belege | Rechnungen, Gutschriften, Verträge, Zahlungsbelege und Stornierungen | Belegarchiv |
| Abgrenzungen | Fremdgeld, Sicherheiten, Hinterlegungen, Steuern und Unterrechnungen | Fachakten |
| Kosten | Gerichtskosten, Vergütung, Auslagen und Masseverbindlichkeiten | BER-SKV |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Rechnungsstichtag und Vollständigkeit

Für jedes Konto und jede Kasse werden Anfangsdatum, Anfangsbestand, lückenloser Auszugs- oder Kassenbuchzeitraum, Enddatum und Endbestand festgelegt. Valuta und Buchungsdatum bleiben getrennt. Der Rechnungsstichtag bestimmt den Bestand; später eingegangene Auszüge können ihn belegen, später valutierte Bewegungen gehören in den Nachlauf. Prüfen Sie bei Kontoschließungen die Schlussabrechnung und bei Kontoeröffnungen die Herkunft des Eröffnungsbestands.

Die Vollständigkeitskontrolle umfasst die fortlaufende Auszugsnummer, fehlende Tage oder Seiten, Kontoinhaber, Währung, Storno- und Rücklastschriftketten, doppelt importierte Bewegungen und nicht einbezogene Unterkonten. Ein Saldenblatt ersetzt diese Prüfung nicht. Jede Datenlücke erhält ihren maximal möglichen Betragseffekt oder die Feststellung, dass dieser noch nicht bestimmbar ist.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Bestimmen Sie Rechnungszeitraum, Anfangsbestand und sämtliche einbezogenen Konten. Prüfen Sie Eröffnung, Schließung und Kontoinhaber.
2. Importieren oder erfassen Sie jede Bewegung mit Datum, Valuta, Betrag, Gegenkonto, Buchungstext, Kategorie, Belegkennung und Status. Verhindern Sie doppelte Erfassung von Umbuchungen.
3. Ordnen Sie Einzahlungen und Auszahlungen rechtlich und wirtschaftlich zu. Kennzeichnen Sie Fremdgeld, Sicherheitenerlöse und Hinterlegungen getrennt.
4. Stimmen Sie Bank- und Kassenbestand gegen Finanzbuchhaltung und Berichtsrechnung ab. Dokumentieren Sie den Rechenweg und jede Differenz.
5. Prüfen Sie Unterrechnungen für Verwertung, Betrieb, Personal, Steuern und Prozesse gegen die Hauptrechnung. Summen müssen reproduzierbar sein.
6. Trennen Sie beantragte, festgesetzte und bezahlte Vergütung sowie erwartete, festgesetzte und gezahlte Steuerpositionen.
7. Erstellen Sie ein Differenzprotokoll. Jede Differenz erhält Ursache oder offenen Status, Betrag, betroffene Produkte, Verantwortlichen und Frist.
8. Frieren Sie die führende Rechenfassung für die Text- und Verteilungsprodukte ein. Jede spätere Bewegung erzeugt eine neue Version.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Rechnen Sie je Konto `Anfangsbestand + Einzahlungen - Auszahlungen = Endbestand` und dokumentieren Sie Vorzeichen und Währung. Für die konsolidierte Rechnung werden Umbuchungen zwischen einbezogenen Konten paarweise eliminiert; die Einzelbewegungen bleiben prüfbar. Danach werden drei unabhängig gewonnene Größen verglichen: tatsächlicher Bank- und Kassenbestand, Saldo der Finanzbuchhaltung und aus Anfangsbestand plus klassifizierten Einzelbewegungen errechneter Berichtsbestand. Eine Differenz von null ist Ergebnis des Abgleichs, keine Vorgabe, die durch Sammelbuchung hergestellt werden darf.

Jede Summenposition besitzt eine Belegreichweite und eine Kontrollsumme zur Einzelbewegungsliste. Stichproben genügen nicht für den Summennachweis, wenn ein vollständiger Export vorhanden ist. Prüfen Sie negative Beträge, Stornos, Rücklastschriften, Gutschriften, Gebühren und interne Umbuchungen gesondert, weil sie bei bloßer Vorzeichensummierung leicht doppelt oder spiegelverkehrt erfasst werden.

### 3.3 Qualitätsgates

`G3 Rechenwerk` ist nur erfüllt, wenn alle Konten und Kassen vollständig erfasst sind, Anfangs- und Endbestände belegt sind, Umbuchungen eliminiert wurden, jede Kategorie auf Einzelbewegungen überleitet und Bank/Kasse, Buchhaltung und Berichtsrechnung denselben erklärten Endbestand ergeben. Eine ungeklärte Differenz, eine fehlende Auszugsfolge oder ein ungeklärtes Fremdgeld sperrt Quote und Auszahlung. `G4` erfordert eine namentliche fachliche Prüfung der exakten Arbeitsmappe oder Rechnung samt Formeln und Belegindex; `G7 Zahlung` wird in diesem Skill nicht freigegeben.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

An `schlussbericht-erstellen` gehen Einnahmen- und Ausgabensummen, Endbestand und die fachlich freigegebenen Erläuterungen, jeweils mit Stichtag und Fassungskennung. An `forderungen-sicherheiten-quote-darstellen` geht der verfügbare Ausgangsbestand zusammen mit den ausdrücklich noch abzuziehenden oder gesondert zu behandelnden Positionen; eine freie Quote wird nicht übergeben. An `schlussverteilung-aufhebung-vorbereiten` gehen erst nach `G3` der bestätigte Bestand, die Belegkette und das Null-Differenz-Protokoll. Das Differenzprotokoll nennt für jede offene Position Betrag, Konten, Belege, Ursache oder Prüfweg, Verantwortlichen, Frist und gesperrte Folgeprodukte.

## 4. Quellenpflicht

§ 66 InsO trägt die Rechnungslegung. § 69 InsO weist dem Gläubigerausschuss Prüf- und Überwachungsaufgaben einschließlich Geldverkehr und Bestand zu. §§ 53 bis 55 InsO sowie §§ 63 und 64 InsO strukturieren Kosten, Masseverbindlichkeiten und Vergütung; sie erlauben keine Buchung eines bloßen Antrags als festgesetzte Ausgabe.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** § 66 InsO trägt die Schlussrechnung und Zwischenrechnungslegung. § 69 InsO trägt bei bestehendem Gläubigerausschuss dessen Prüfung von Geldverkehr und Bestand; § 79 InsO trägt die in der Quellenkarte bezeichnete Prüfrolle der Gläubigerversammlung, wenn kein Gläubigerausschuss bestellt ist. §§ 53 bis 55 sowie §§ 63 und 64 InsO tragen die getrennte Einordnung von Kosten, sonstigen Masseverbindlichkeiten und Vergütung.

**Trägt nicht:** Die Normen belegen keine konkrete Buchung, Kontovollständigkeit, Zahlung oder Freigabe. Ein Vergütungsantrag ist weder Festsetzungsbeschluss noch Bankabfluss; ein Buchhaltungssaldo beweist keinen Bankbestand und ein Kontostand keine zutreffende rechtliche Kategorisierung.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-SR`

1. Rechnungsauftrag, Zeitraum und Kontenbestand
2. Anfangsbestände und Eröffnungsüberleitung
3. Einnahmen und Ausgaben nach Kontengruppen
4. Unterrechnungen und Abgrenzungen
5. Bank-Kasse-Buchhaltung-Berichtsrechnung-Abgleich
6. Differenzprotokoll und Sperrwirkungen
7. Endbestand, Kontrollsummen und Belegindex

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Umbuchung doppelt erfasst

Eine Übertragung vom Massekonto auf ein verzinstes Unterkonto erscheint auf beiden Auszügen. Der Skill bildet sie als interne Umbuchung ab, nicht als neue Einnahme und Ausgabe mit wirtschaftlichem Effekt. Beide Bankbewegungen bleiben über Belegkennungen nachvollziehbar.

### 6.2 Dreitausend Euro Differenz

Der Bankbestand liegt 3.000 Euro über dem Buchhaltungssaldo. Es gibt keinen identifizierten Beleg. Der Skill weist die Differenz aus, ordnet Verantwortlichen und Frist zu und sperrt `G3`. Er erzeugt weder eine fiktive sonstige Einnahme noch eine Quote.

### 6.3 Gebühr nach dem Stichtag

Der Kontoauszug zum 31. März weist 50.000 Euro aus. Am 2. April belastet die Bank eine am 31. März valutierte Gebühr von 40 Euro. Der Skill prüft den maßgeblichen Bankbeleg und ordnet die Bewegung nach Valuta dem Stichtag zu, statt nur das Abrufdatum zu verwenden. Schlussrechnung und Endbestand werden auf 49.960 Euro übergeleitet; betroffene Folgeprodukte erhalten neue Fassungen und frühere Freigaben werden zurückgesetzt.
