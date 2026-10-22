---
name: nachtragsverteilung-bearbeiten
description: Bearbeitet nach Abschluss ermittelte Massegegenstände und Rückflüsse. Prüft Massezugehörigkeit, Kosten, Antrag, gerichtliche Anordnung, Schlussverzeichnisbezug, Auszahlung und Rechnungslegung ohne den alten Schlussbericht zu überschreiben.
---

# Nachtragsverteilung bearbeiten

## 1. Zweck und Anwendungsfall

Dieser Skill eröffnet nach Schlusstermin oder Aufhebung einen eigenen Nachtragsvorgang. Er bearbeitet frei werdende Rückbehalte, zurückfließende Massebeträge und nachträglich ermittelte Massegegenstände von der Fundmeldung bis zur gerichtlichen Rechnungslegung.

Der historische Schlussbericht bleibt unverändert. Der Skill verknüpft ihn über Verfahrenskennung und Fassung, prüft aber Massezugehörigkeit, Rolle, Kosten und Anordnung neu. Das bloße Zuflussdatum beweist weder Massezugehörigkeit noch Verteilungsreife.

### 1.1 Produkt und Anschluss

Das Leitprodukt ist `BER-NV`. Die Fachroute übergibt an `akte-und-berichtsanlass-steuern`, `schlussrechnung-konten-abgleichen` und `schlussverteilung-aufhebung-vorbereiten`. Jede Übergabe nennt Produktkennung, Pfad, Hash, Version, Stichtag, maßgebliche Beschlüsse, Belege, Rechenstand, Quellenstatus, offene Frage, Frist, verantwortliche Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt die übernommene Fassung.

### 1.2 Rollen- und Handlungsgrenze

Der Skill darf Unterlagen lesen, ordnen, rechnen und Entwürfe erstellen. Eine natürliche, fachlich zuständige Person entscheidet über rechtliche Endbewertung, Einreichung, Zahlung, Hinterlegung, Anerkenntnis, Vergleich, Verzicht und Löschung. Der Skill behauptet keine Außenhandlung ohne tatsächlichen Nachweis.

## 2. Eingaben

| Eingabebereich | Benötigter Inhalt | Bevorzugter Nachweis |
| --- | --- | --- |
| Fund | Gegenstand, Betrag, Funddatum, Quelle und Verfügungsgewalt | Primärbeleg |
| Historie | Schlussbericht, Schlussrechnung, Schlussverzeichnis und Aufhebung | frühere Abschlussakte |
| Massebezug | Entstehungsgrund, Zeitraum, Rechtsträger und frühere Behandlung | Vertrag, Steuer- oder Anspruchsakte |
| Rolle | früherer Verwalter, Treuhänder, Gericht und Befugnisse | Beschlüsse |
| Kosten | Verwertung, Steuer, Gericht, Vergütung und Auszahlungsaufwand | Kostenschätzung und Belege |
| Anordnung | gerichtlicher Antrag, Beschluss, Umfang und Auflagen | Gerichtsakte |

### 2.1 Eingangsprüfung

Lesen Sie vorhandene Unterlagen zuerst. Prüfen Sie Identität, Zeitraum, Stichtag, Fassung und Vollständigkeit. Fragen Sie nur nach einer Lücke, die das bestellte Produkt materiell verändert oder ein Gate sperrt. Nennen Sie bei jeder Lücke die betroffene Aussage oder Zahl, die Auswirkung, einen realistischen Beschaffungsweg, die verantwortliche Person und eine Frist.

### 2.2 Tatsachenstatus

Verwenden Sie `belegt`, `rechnerisch abgeleitet`, `Angabe Dritter`, `vorläufig bewertet`, `offen` oder `widerlegt`. Formulieren Sie den Empfängertext entsprechend. Ein Dateiname, eine Tabellenüberschrift oder eine alte Berichtsfassung ist kein Beleg für den aktuellen Stand.

### 2.3 Historischer und neuer Stichtag

Der Nachtragsvorgang führt den historischen Abschlussstichtag `T0`, das Datum der Aufhebung, das Fund- oder Zuflussdatum `F` und den aktuellen Abrechnungsstichtag `T1` getrennt. Ein später Zufluss wird nicht allein wegen `F` der Masse zugeordnet. Zu prüfen sind Entstehungsgrund, zeitliche Zuordnung, Rechtsträger, Rechte Dritter und die Behandlung in Schlussbericht, Schlussrechnung und Schlussverzeichnis.

Erstellen Sie eine Deltaakte, die den historischen Schlussbestand nicht rückwirkend umschreibt. Sie beginnt mit dem nach Abschluss ermittelten Bruttowert, zeigt gesondert realisierte Zuflüsse, belegte Nachtragskosten, noch offene Kosten, Nettoverteilungsbetrag, Einzelzahlungen und verbleibenden Bestand. Korrekturen historischer Angaben werden als Korrekturvermerk mit ihrer Auswirkung dokumentiert; die alte führende Fassung bleibt unverändert abrufbar.

## 3. Ablauf und Checkliste

### 3.1 Fachworkflow

1. Eröffnen Sie unter der alten Verfahrenskennung eine neue Vorgangskennung. Überschreiben Sie keine historische Abschlussdatei.
2. Erfassen Sie Fund und Beleg. Trennen Sie Besitz oder Zahlungseingang von rechtlicher Massezugehörigkeit.
3. Prüfen Sie Entstehungsgrund, Zeitraum, Rechtsträger, frühere Behandlung und etwaige Rechte Dritter. Bei Steuererstattungen ist eine zeitliche Aufteilung zu prüfen.
4. Prüfen Sie, ob § 203 Absatz 1 InsO einschlägig sein kann und wer den Antrag oder die Anregung stellen darf. Bereiten Sie den Text zur menschlichen Freigabe vor.
5. Berechnen Sie erwarteten Nettoeffekt aus Bruttowert und konkreten Kosten. Stellen Sie dar, wenn Kosten außer Verhältnis zum Wert stehen könnten.
6. Warten Sie die tatsächliche gerichtliche Anordnung ab. Erfassen Sie Gegenstand, Umfang, Rolle und Auflagen genau; behaupten Sie keine Anordnung aus einem Entwurf.
7. Verwenden Sie für die Verteilung das maßgebliche Schlussverzeichnis. Prüfen Sie Identität, Rechtsnachfolge und Zahlungsdaten, ohne die festgestellte Basis still zu verändern.
8. Erstellen Sie Nachtragsrechnung, Zahlungslauf, Bankabgleich und Rechnungslegung nach § 205 InsO. Schließen Sie erst mit tatsächlichen Nachweisen.

### 3.2 Rechen- und Konsistenzkontrolle

Prüfen Sie alle Beträge gegen Primärbeleg, Buchhaltung und Bank, soweit diese Ebenen einschlägig sind. Schätzung, Anspruch, vertraglicher Betrag, Festsetzung, Zahlung und Bestand bleiben getrennt. Text, Tabelle, Anlagenverzeichnis und Fachmodule verwenden dieselbe führende Stichtagsfassung. Eine inhaltliche Änderung erzeugt eine neue Version und setzt betroffene Freigaben zurück.

Die Nachtragsrechnung verwendet die Kontrollbrücke `tatsächlich eingegangener Bruttobetrag - belegte oder konkret freigegebene Nachtragskosten - Fremdanteile = Nettoverteilungsbetrag`. Erwartete Werte werden außerhalb dieser Rechnung als Szenario geführt. Die Summe der Einzelzahlungen, Hinterlegungen, Rückläufer und des verbleibenden Bankbestands muss auf den Nettoverteilungsbetrag überleiten. Stimmen historisches Schlussverzeichnis, Gläubigeridentität oder frühere Abschläge nicht mit der Arbeitsliste überein, wird nicht gerechnet, bis die Abweichung positionsbezogen geklärt ist.

### 3.3 Qualitätsgates

`G8 Nachtrag` wird in vier prüfbare Phasen unterteilt. Die Fundprüfung ist erfüllt, wenn Gegenstand, Verfahrensbezug und Primärbeleg feststehen. Die Antragsprüfung ist erfüllt, wenn Massezugehörigkeit, zuständige Rolle, frühere Behandlung und Kostenwirkung fachlich freigegeben sind. Die Vollzugsprüfung beginnt erst mit dem tatsächlichen gerichtlichen Beschluss und übernimmt dessen Gegenstand, Umfang und Auflagen wortgetreu in die Arbeitsakte. Die Abschlussprüfung verlangt Nachtragsrechnung, Bankabgleich und Einreichungsnachweis der Rechnungslegung. Für einen Zahlungslauf gelten zusätzlich `G3`, `G4` und `G7`; eine Freigabe der Anregung ist keine Zahlungsfreigabe.

### 3.4 Übergabe

Die Übergabe enthält das fachlich bearbeitete Produkt, eine Quellen- und Belegnotiz, ein Differenz- oder Lückenprotokoll, den Gate-Status und das konkret nächste Produkt. Offene Punkte werden nicht in einer pauschalen Resteliste versteckt, sondern der betroffenen Passage oder Zahl zugeordnet.

Vor der gerichtlichen Anordnung besteht das Übergabeprodukt aus Fundmeldung, Massezuordnungsprüfung, Rollenprüfung, Kostenrechnung und freizugebendem Antrags- oder Anregungsentwurf. Nach der Anordnung werden Beschlussdatei, Anordnungsumfang, historisches Schlussverzeichnis und eine neue `BER-NV`-Rechenfassung an `schlussrechnung-konten-abgleichen` und `schlussverteilung-aufhebung-vorbereiten` übergeben. Nach Vollzug enthält die Rückgabe Bankbelege, Rückläufer, Hinterlegungen, Restbestand und Entwurf der gerichtlichen Rechnungslegung. Jede Phase besitzt eine eigene Versionskennung und darf nicht durch den Status einer späteren Phase vorweggenommen werden.

## 4. Quellenpflicht

§§ 203 bis 205 InsO regeln Anordnung und Vollzug. BGH, Beschluss vom 26.09.2024 – IX ZB 5/24, Rn. 6 bis 15, trägt die eigenständige Prüfung einer Steuererstattung und dass Restschuldbefreiung die Nachtragsverteilung eines Massegegenstands nicht hindert. BGH, Beschluss vom 25.09.2025 – IX ZB 13/25, Rn. 7 bis 16 und 20 bis 22, trägt die mögliche Nachtragsverteilung auch bei einem früher bekannten, tatsächlich nicht verwerteten Massegegenstand; Massezugehörigkeit bleibt erforderlich. BGH, Beschluss vom 21.05.2026 – IX ZB 45/25, Rn. 7 bis 17, 19 bis 29 und 33 bis 36, trägt die Antragsbefugnis des früheren Insolvenzverwalters nach Aufhebung, nicht die Massezugehörigkeit jedes Anspruchs.

Prüfen Sie die aktuelle amtliche Fassung der einschlägigen Normen und den zeitlichen Anwendungsbereich. Verwenden Sie die [amtliche Quellenkarte](../../references/rechtsquellen.md), die [Arbeitsweise](../../references/arbeitsweise.md) sowie die [Produkt- und Gatematrix](../../references/produkte-gates-und-uebergaben.md). Für die Form der Nachweise gilt ergänzend die [Zitierweise des Repositorys](../../../references/zitierweise.md).

Zitieren Sie eine Entscheidung nur für die in der Quellenkarte verifizierte Aussage und nennen Sie die Aussagegrenze. Prüfen Sie Gericht, Entscheidungsform, Datum, Aktenzeichen, Randnummer und amtlichen Volltext vor produktiver Verwendung erneut. Erfinden Sie keine Fundstelle und ergänzen Sie keine Literatur aus Modellwissen. Ist eine tragende Quelle nicht zugänglich, kennzeichnen Sie die Rechtsfrage als offen; Tatsachenabgleich, Rechnung und unabhängige Berichtsteile werden weiterbearbeitet.

Gerichtliche Einzelverfügungen, lokale Formulare und Kanzleimuster gelten nur für das konkrete Verfahren. Ein Muster liefert Aufbau und Kontrollfragen, keine Tatsachen. Ein Bericht beweist weder seine Einreichung noch gerichtliche Zustimmung, Festsetzung, Zahlung oder Aufhebung.

**Trägt:** §§ 203 bis 205 InsO tragen Anordnung, Vollzug und Rechnungslegung der Nachtragsverteilung. BGH IX ZB 5/24 trägt die gesonderte zeitliche Prüfung einer Steuererstattung und die in der Quellenkarte beschriebene Wirkung der Restschuldbefreiung. BGH IX ZB 13/25 trägt die mögliche Einbeziehung eines schon bekannten, tatsächlich nicht verwerteten Massegegenstands. BGH IX ZB 45/25 trägt die dort abgegrenzte Antragsbefugnis des früheren Insolvenzverwalters nach Aufhebung.

**Trägt nicht:** Weder ein später Zahlungseingang noch eine frühere Erwähnung im Schlussbericht beweist Massezugehörigkeit. Die Entscheidungen begründen keine allgemeine Antragsbefugnis eines Treuhänders, keine Zuordnung jedes Anspruchs zur Masse und keine Auszahlung ohne gerichtliche Anordnung und freigegebenes Rechenwerk.

## 5. Ausgabeformat

### 5.1 Aufbau des Leitprodukts `BER-NV`

1. Fundmeldung und historischer Verfahrensbezug
2. Massezugehörigkeit und Rechte Dritter
3. Rolle, Antragsbefugnis und Kostenbetrachtung
4. Antrag oder Anregung an das Gericht
5. gerichtliche Anordnung und Vollzugsplan
6. Nachtragsrechnung, Verteilung und Bankabgleich
7. Rechnungslegung und Abschlussstatus

### 5.2 Ausformulierung und Format

Das beauftragte Dokument steht zuerst. Es wird vollständig ausformuliert und in grammatikalisch sauberen, prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen und Zuordnungen zeigen, ersetzen aber weder Begründung noch konkrete Handlung. Ein Ergebnis mit Skelettcharakter ist zu verwerfen und vollständig neu zu schreiben.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Fehlende Angaben erhalten eindeutige Platzhalter; der umgebende Satz bleibt vollständig. Interne Prüffelder, Promptanweisungen und Quellenprotokolle gehören nicht in eine gerichtliche Empfängerfassung.

Jede Ausgabe endet mit einer getrennten internen Statusnotiz: Produktkennung und führende Fassung, Stichtag, letzte berücksichtigte Unterlage, erreichte Gates, offene Frage mit Auswirkung und Verantwortlichem, erforderliche menschliche Freigabe, nächste Route und nächstes Produkt. Zulässige Statuswerte sind `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` und `ausgeführt und belegt`.

## 6. Beispiele

### 6.1 Späte Steuererstattung

Nach Aufhebung gehen 18.000 Euro für mehrere Veranlagungszeiträume ein. Der Skill trennt Auszahlungsdatum, steuerlichen Entstehungsgrund und Zeitanteile. Er bereitet eine Massezuordnung und gerichtliche Anregung vor, überweist aber nichts ohne Anordnung und Freigabe.

### 6.2 Früher bekannter Anspruch

Ein Anspruch war im Schlussbericht erwähnt, wurde aber tatsächlich nicht verwertet. Der Skill prüft weiterhin Massezugehörigkeit, frühere Behandlung und Kosten. Die damalige Erwähnung verhindert die Nachtragsroute nicht automatisch und ersetzt keine gerichtliche Anordnung.

### 6.3 Freigewordener Rückbehalt mit Rückläufer

Ein Rückbehalt von 12.000 Euro wird nach Aufhebung frei. Der gerichtliche Beschluss ordnet die Nachtragsverteilung dieses Betrags an. Die freigegebene Liste weist 11.940 Euro Zahlungen und 60 Euro belegte Bankkosten aus; eine Zahlung über 900 Euro läuft zurück. Der Skill ändert den historischen Schlussbericht nicht, ordnet dem Rückläufer einen offenen Status zu und weist in der Rechnungslegung 11.040 Euro vollzogene Zahlungen, 900 Euro Restbestand und 60 Euro Kosten aus. Der Vorgang bleibt bis zur Behandlung des Rückläufers offen.
