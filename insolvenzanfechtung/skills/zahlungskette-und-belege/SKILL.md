---
name: zahlungskette-und-belege
description: "Rekonstruiert Zahlungen, Vertragswechsel, Empfänger und Krisenwissen aus Bankdaten, Buchhaltung und Schriftverkehr. Liefert eine belegte Vorgangsmatrix mit offenen Zuordnungen für die Insolvenzanfechtung."
---

# Zahlungsketten und Krisenbelege rekonstruieren

## 1. Zweck und Anwendungsfall

Erstellen Sie aus einer unübersichtlichen Schuldnerakte eine belastbare Zahlungskette. Die Buchungszeile ist ein Einstieg, kein Beweis für Forderungsinhaber, Rechtsgrund oder Kenntnis. Unterscheiden Sie Vermögensbewegung, wirtschaftlichen Zweck und rechtliche Zuordnung. Der Skill passt zu Kontoauszügen, Zahlungsdienstleistern, Darlehensplattformen, Vertragsübernahmen und gewöhnlichen Lieferantenkonten. Er liefert die Tatsachengrundlage für beide Prozessseiten; eine verdächtige Zahlung wird noch nicht als anfechtbar bezeichnet.

Beginnen Sie mit der vom Auftrag betroffenen Forderung und den dafür relevanten Unterlagen. Liegt bereits ein Forderungsschreiben vor, erfassen Sie dessen behauptete Zahlungsliste und vergleichen diese mit den Bankbelegen. Ein Auftrag zur Verteidigung wird nicht stillschweigend in eine Verwalterrecherche geändert. Bei Masseprüfung bleibt eine entlastende Gegenleistung ebenso sichtbar wie eine auffällige Weiterleitung.

## 2. Eingaben

Benötigt werden Schuldneridentität, Verfahrensstand, betroffene Konten und das bestellte Produkt. Lesen Sie Kontoauszüge mit Buchungstag, Wertstellung, Gegenkonto und Verwendungszweck, Vertragsfassungen, Rechnungen, offene Posten, Zahlungsfreigaben und die einschlägigen Nachrichten. Übernehmen Sie bekannte Beteiligte; fragen Sie nur nach fehlender Zuordnung. Bei CSV oder Excel sind Trennzeichen, Dezimaldarstellung, Währung, Soll/Haben und Exportzeitraum zu klären. Eine negative Zahl kann je Export eine Belastung oder einen Gegenposten bezeichnen.

Erfassen Sie Absender, Empfangsadressen und Weiterleitungen von E-Mails, jedoch nur soweit sie den Zugang einer Information tragen. Ein allgemeines Funktionspostfach belegt nicht ohne Weiteres, dass eine entscheidungsbefugte Person den gesamten Anhang gelesen hat. Fehlende Anhänge kommen auf die Nachforderungsliste; ihr Inhalt wird nicht aus dem Betreff rekonstruiert.

## 3. Ablauf und Checkliste

### 3.1 Originalbestand sichern

Erstellen Sie ein Dokumentenverzeichnis mit Dokumentkennung, Dateipfad, Datum und überprüfbarer Fundstelle. Bearbeiten Sie Kopien. OCR-Ergebnisse sind Hilfstexte; kontrollieren Sie Beträge, Namen und Datumsangaben am Bild. Dubletten werden verknüpft und nicht als weitere Zahlung gerechnet. Ein erneut übersandter Kontoauszug ändert die Beweiszahl, nicht den Kontoumsatz. Bei geschwärzten Unterlagen benennen Sie genau, welche Prüfung deshalb offenbleibt.

### 3.2 Jede Vermögensbewegung einzeln erfassen

Vergeben Sie stabile Vorgangskennungen wie Z-001. Erfassen Sie Zahler, belastetes Vermögen, tatsächlichen Empfänger, Buchungs- und Wertstellungstag, Betrag, Währung und Beleg. Storno, Rücklastschrift, Teilzahlung, Gebühren und interne Umbuchung erhalten eigene Beziehungen zur Ausgangsbuchung. Die Bruttosumme aller Zeilen ist kein Anfechtungsbetrag. Stimmen Sie Anfangssaldo plus Zugänge minus Abgänge mit dem Endsaldo ab; eine Differenz wird vor jeder rechtlichen Bewertung als Datenproblem ausgewiesen.

### 3.3 Forderungs- und Vertragskette abbilden

Ordnen Sie zur Zahlung die ursprüngliche Forderung, deren Fälligkeit und etwaige Änderungen zu. Trennen Sie Abtretung einer Forderung, Schuldübernahme, Vertragsübernahme, Einzugsermächtigung und bloßen Wechsel des Zahlwegs. Prüfen Sie Unterschriften, Zustimmungserfordernisse und Wirksamkeitsbedingungen anhand des tatsächlich einschlägigen Rechts. Ein neuer Briefkopf oder ein Zahlungsauftrag beweist keinen Gläubigerwechsel. Markieren Sie für jede behauptete Übernahme, welche Partei zu welchem Zeitpunkt zustimmte und welcher Beleg fehlt.

### 3.4 Wissen zeitbezogen erfassen

Bauen Sie neben der Zahlungsliste eine Kenntnischronologie auf. Eine Nachricht nach der Zahlung kann frühere Tatsachen bestätigen, beweist aber nicht automatisch früheres Empfängerwissen. Erfassen Sie jeweils Inhalt, Zugang, Adressat, Vertretungsrolle und erkennbare Reichweite. Eine Bitte um Ratenzahlung hat andere Aussagekraft als die Mitteilung, dass fällige Forderungen mehrerer Gläubiger nicht mehr bedient werden. Stellen Sie entlastende Umstände daneben: bestrittene Forderung, technischer Zahlungsfehler, zugesagte Finanzierung oder nachgeholte Regulierung.

### 3.5 Gezielt nachfordern und fortschreiben

Priorisieren Sie die fehlenden Belege nach ihrem Einfluss auf Empfänger, Zeitpunkt, Gegenleistung und Krisenkenntnis. Formulieren Sie eine konkret beantwortbare Nachfrage: „Bitte übersenden Sie die Zustimmung der bisherigen Darlehensgeberin zum Vertragswechsel und den vollständigen Zahlungsbeleg zur Buchung Z-004.“ Fordern Sie nicht pauschal alle Geschäftsunterlagen an. Nach Eingang der Antwort ergänzen Sie dieselben Vorgangskennungen und protokollieren, welche Schlussfolgerung sich ändert.

### 3.6 Für die juristische Prüfung übergeben

Übergeben Sie die bereinigte Zahlungskette an die zeitliche und tatbestandliche Prüfung. Kennzeichnen Sie bewiesen, bestritten, nur behauptet und derzeit unklar. Ein rechnerisch passender Saldo ersetzt keine Rechtsgrundprüfung. Erstellen Sie auf Wunsch bereits das ausformulierte Sachverhaltskapitel; offene Tatsachen werden darin als streitig oder ungeklärt bezeichnet. Sie dürfen nicht durch eine scheinbar durchgehende Erzählung verdeckt werden.

### 3.7 Selbstkontrolle und Übergabe

Prüfen Sie abschließend, ob Brutto- und Nettobeträge vermischt wurden, ob dieselbe Rechnung durch mehrere Belege mehrfach gezählt wurde und ob die Gegenkontoangabe tatsächlich zum behaupteten Anfechtungsgegner gehört. Unterscheiden Sie eine Empfängerbank von ihrem Kunden. Ein Treuhandkonto kann weitere Zurechnungsfragen auslösen; schreiben Sie die Treuhänderstellung nicht ohne Vertrag fest. Bei mehreren Schuldnergesellschaften muss jede Buchung einer eigenen Masse zugeordnet bleiben. Eine Konzernübersicht ersetzt die Einzelzuordnung nicht.

Die Übergabe enthält Vorgangskennung, konkreten Beleg, festgestellte Tatsachen, bestrittene Punkte und das benötigte nächste Produkt. Nutzen Sie nur die sachlich erforderlichen Nachbarschritte: [Rechtshandlung, Zeitpunkt und Gläubigerbenachteiligung prüfen](../rechtshandlung-zeit-benachteiligung/SKILL.md), [Anfechtungsansprüche durchsetzen, abwehren und vergleichen](../prozess-und-vergleich/SKILL.md). Nach einer Antwort ergänzen Sie den laufenden Stand und kontrollieren die betroffenen Folgeprodukte.

## 4. Quellenpflicht

### 4.1 Fachlicher Entscheidungsanker

BGH, Urteil vom 18. April 2024 – IX ZR 129/22, ECLI:DE:BGH:2024:180424UIXZR129.22.0, Rn. 20 bis 27. Gelesen: Rn. 8 bis 27.

[Amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_129-22.pdf?__blob=publicationFile&v=1).

Trägt: Ein außenstehender Empfänger muss aus einer nicht durch Einzelbelege erläuterten, nur zusammengefassten Liquiditätstabelle keine nicht vorhandenen internen Kenntnisse gewinnen. Umfang des erforderlichen Bestreitens hängt von Substantiierung des Verwaltervortrags und eigener Kenntnis ab. Forderung, Fälligkeit, liquide Mittel und Belege sind so aufzubereiten, dass konkrete Einwendungen möglich sind.

Trägt nicht: Pauschales Nichtwissen ist bei eigenen Handlungen immer zulässig; jede Liquiditätsrechnung benötigt ausnahmslos jeden Buchhaltungsbeleg als Anlage; der außenstehende Empfänger ist materiell von Anfechtung befreit.

### 4.2 Prüfung vor Verwendung

Prüfen Sie die anwendbare Normfassung und jede tragende gerichtliche Aussage anhand der [Rechtsquellen](../../references/rechtsquellen.md) und der [Zitierweise](../../references/zitierweise.md). Eine Suchtrefferüberschrift, ein früherer KI-Text oder ein Datenbankzitat ohne gelesenen Volltext ist kein Beleg. Gericht, Entscheidungsform, Datum, Aktenzeichen und gelesene Randnummer müssen zur konkreten Aussage passen. Dokumentieren Sie, was der Anker trägt und was er nicht trägt. Übernehmen Sie keine allgemeine Bindung aus einem Präzedenzfall.

Ist der amtliche Text nicht zugänglich, bleibt die Aussage ausdrücklich unverifiziert; verlangen Sie den Originaltext oder formulieren Sie den offenen Prüfpunkt. Erfinden Sie keine Randnummer, Frist oder Fundstelle. Die [Arbeitsweise](../../references/arbeitsweise.md) verlangt eine getrennte Tatsachen-, Rechts- und Rechenkontrolle. Im Schriftsatz stehen tragende Nachweise an der passenden Stelle; technische Abrufprotokolle bleiben in der internen Notiz.

## 5. Ausgabeformat

Das Arbeitsergebnis besteht aus Zahlungsliste, Vertragskette, Kenntnischronologie und einer priorisierten Nachforderung. Für Excel verwenden Sie getrennte Blätter „Vorgänge“, „Belege“, „Verträge“, „Wissen“ und „Abgleich“. Die Übersicht darf höchstens vier sichtbare Spalten haben; zusätzliche Detailfelder gehören in Einzelblätter oder Vorgangsblöcke. Jede berechnete Summe nennt ihre Ausgangszeilen. Ein Schreiben enthält nur die für den Empfänger erforderlichen Fragen und keine internen Verdachtsbewertungen.

Alle Endprodukte werden vollständig ausformuliert in grammatikalisch vollständigen Sätzen geliefert. Skelette, leere Klauselrümpfe und bloße Stichwortsammlungen sind kein fertiges Dokument. Fehlende Einzelangaben erhalten eindeutige Platzhalter, ohne den umgebenden Sinnsatz wegzulassen. Formatierte Dokumente verwenden soweit technisch möglich Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei reiner Textausgabe steht der Formatwunsch in einem getrennten Exporthinweis. Versand, Einreichung, Anerkenntnis, Verzicht und Vergleichsannahme werden nicht ohne konkrete menschliche Freigabe ausgeführt.

## 6. Beispiele

Eine Bremer Darlehensplattform bezeichnet sich nach einem Vertragswechsel als neue Gläubigerin. Die Kontoauszüge zeigen Zahlungen an ein anderes Unternehmen. Ergebnis ist keine pauschale Rückforderung, sondern eine Kette aus bisherigem Vertrag, Übernahmevereinbarung, Zustimmung, Einzug und Weiterleitung. Bleibt die Zustimmung offen, werden zwei rechtliche Varianten mit identischen Zahlungsbelegen weitergegeben.

Eine Lieferantin sendet drei Mahnungen und zwei erneut exportierte Bankzeilen. Sie werden nicht als fünf Zahlungen behandelt. Eine spätere Rückerstattung wird der tatsächlich betroffenen Zahlung zugeordnet und nur einmal berücksichtigt.
