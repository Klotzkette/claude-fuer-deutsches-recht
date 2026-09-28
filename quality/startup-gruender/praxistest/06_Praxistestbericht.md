# Praxistestbericht zum Startup-Gründer-Plugin

## 1 Durchführung und Ergebnis

Der fiktive Mandatsauftrag wurde als ausführender Gründungsskill bearbeitet. Es liegen tatsächliche vollständige Markdown-Arbeitsentwürfe und ein ausformulierter Prüfvermerk vor. Die Originale wurden unverändert gelassen; im Repository wurde nichts geschrieben. Erwartungsdaten unter scripts/data oder quality/evals/rubric wurden nicht gelesen. Vorläufige Renderderivate und Akten-README wurden nicht verwendet.

| Ergebnis | Datei |
|---|---|
| Vollständige individuelle GmbH-Satzung | [01_Satzung_DE.md](01_Satzung_DE.md) |
| Vollständiges SHA Deutsch | [02_Gesellschaftervereinbarung_DE.md](02_Gesellschaftervereinbarung_DE.md) |
| Korrespondierendes SHA Englisch | [03_Shareholders_Agreement_EN.md](03_Shareholders_Agreement_EN.md) |
| Beteiligung, Vollzugsstand, Status, Mehrheiten, Finanzierung und konkrete Lücken | [04_Stand_Pruefung_Entscheidungen.md](04_Stand_Pruefung_Entscheidungen.md) |
| Ausformulierte optionale Vestingregel Deutsch/Englisch | [05_Vesting_Variante_DE_EN.md](05_Vesting_Variante_DE_EN.md) |
| Lese- und gesonderter Exporthinweis | [00_Lesehinweis.md](00_Lesehinweis.md) |

Der Ablauf hat das beauftragte Ergebnis erreicht, ohne wegen fehlender Identitätsdaten, IP-Freigaben oder wirtschaftlicher Entscheidungen vollständig abzubrechen. Nicht geklärte Entscheidungen wurden als Vorschläge oder Platzhalter ausgewiesen. Es wurde weder ein fertiges Notarpaket behauptet noch eine externe Handlung ausgeführt.

## 2 Tatsächlich geprüfte Originale

DOCX-Inhalte wurden aus den nativen Dateien gelesen. EML-Nachrichten wurden einschließlich ihrer vier DOCX-Anlagen dekodiert; die Anlagen zu Produktnotiz, Werkraum, KYC und Seed stimmen beim abschließenden Vergleich bytegenau mit den losen Aktenkopien überein. Alle vier PNG-Boards/Chatbilder wurden visuell geöffnet. Die zwölf Rechnungen und die Gutschrift wurden aus den Original-PDFs gelesen. Die drei XLSX-Dateien wurden einschließlich Blattnamen, Zellbezügen, Formeln und gespeicherten Ergebnissen ausgelesen. Zentrale Summen, Anteilsquoten, Finanzierungsrunden, Abstimmungsfälle und die aktualisierte Liquiditätsrechnung wurden unabhängig gerechnet. Es wurde kein Excel-Rechenlauf oder gerendertes Workbook behauptet.

Die nativen Extrakte liegen zu Prüfzwecken in `/tmp/startup-forward-test/original-extracts`; `native_cells.json` enthält die zuletzt gelesenen Formeln/Werte und `calculate.py` die unabhängige Nachrechnung der Auslagen und Liquidität. Die BGH-/BSG-Originale wurden für die zitierten Passagen von amtlichen Seiten geladen. Mehrere Webabrufe scheiterten mit 403 oder Timeout; direkte amtliche Downloads funktionierten. Dies war ein Werkzeugproblem, kein falscher Linknachweis. Nicht fertig geprüfte Produktklassifikationen wurden offen gelassen.

## 3 Wesentliche Befunde aus dem Durchlauf

Die aktuelle Beteiligung ist 22/21/18/15/10/8/6, bleibt aber ein Verhandlungsstand. Keine Einzahlung, kein Konto, keine Beurkundung, keine Organbestellung und kein bestätigter Notartermin sind belegt. Ottilies 21 % verhindern keine Zustimmung der übrigen 79 %; das Budgetrecht des SHA vermittelt keine umfassende gesellschaftsvertragliche Rechtsmacht. Die Beschäftigungsprognose und das Verfahren nach § 7a SGB IV wurden getrennt von den einzelnen Versicherungszweigen behandelt.

Eine konkrete semantische Abweichung wurde gefunden und bearbeitet: Der Budgetwunsch betrifft ein Gesamtbudget über 50.000 EUR, der ursprüngliche SHA-Text nur eine Erhöhung um mehr als 50.000 EUR. Gleiche Zahl und gleiche deutsche/englische Formulierung verdeckten somit eine Abweichung zur Mandantschaft. Die neuen Entwürfe enthalten einen konkret markierten Lösungsvorschlag.

Die Originalbelege ergeben 3.109,23 EUR brutto nach Gutschrift, davon 2.395,23 EUR privat finanziert und 714 EUR offen. Der erste gelesene Liquiditätsstand ließ die 600-EUR-Kaution aus. Während des Tests wurde die native Akte korrigiert. Der abschließende Originalabruf enthält sie in Annahmen C17 und Liquidität C22; SUM(C13:C22) und die aktualisierten Folgeformeln wurden berücksichtigt. Das verbleibende Ergebnis ist ein Fehlbestand ab November von 175 EUR und bis März 55.170 EUR. Die zuvor gelesenen 54.570 EUR und der erste Fehlmonat Dezember werden ausdrücklich nicht als Endergebnis verwendet. Raumreserve, persönliche Altverträge, fehlende Registeranschrift und Laufzeitende Dezember bleiben separate Tatsachen.

Der Test hat den laufenden Quellenumbau berücksichtigt: Ein externer Qualitätsimpuls der koordinierenden Bearbeitung wies auf die Vollübernahme beim Vorerwerb und § 203 BGB hin. Diese Punkte wurden in den Testentwürfen umgesetzt und abschließend in den inzwischen korrigierten Originalen 31/32 nachgelesen. Sie werden hier nicht als unabhängig entdeckte Findings ausgegeben. Die Rohtexte des letzten Teilabrufs stehen in `latest_31_review.txt` und `latest_32_review.txt`.

## 4 Konkrete Schwächen und Verbesserungsmöglichkeiten der Skillanleitung

Eine blockierende Fehlfunktion oder ein Zwang zum Abbruch trat nicht auf. Die Anleitung zur vollständigen Dokumentproduktion, zur Trennung der Phasen und zur Quellenprüfung war brauchbar. Die folgenden Lücken wurden bei der tatsächlichen Ausführung sichtbar und erforderten zusätzliche Bearbeiterentscheidungen:

1. Die Pflicht zum Lesen von Tabellen und Anlagen legt keine technische Mindestprüfung fest. Im Fall waren EML-Anlagen, native Excel-Formeln und private PDF-Belege entscheidend. Ein knapper Zusatz zu `gruendungsunterlagen-abgleichen` sollte ausdrücklich Formeln statt nur Anzeige/Caches, Nachrichtenanlagen statt nur Mailtext und Quellenfassungen statt nur Dateinamen verlangen. Ohne diese Eigeninitiative wäre die aktualisierte Kaution leicht verloren gegangen.

2. Die Mehrheiten-/Budgetprüfung nennt Bezugsgrößen, enthält aber keinen ausdrücklichen Prüfauftrag für semantische Schwellen: Gesamtbudget, Erhöhungsbetrag, Einzelgeschäft, Brutto/Netto und zusammengehörende Vorgänge. Der Widerspruch bei 50.000 EUR war materiell wichtiger als die DE/EN-Übereinstimmung allein. Ein konkreter Prüfpunkt würde die Reproduzierbarkeit verbessern.

3. Für den Gesamtauftrag fehlt ein präziser Mindestumfang der Liquiditätsprüfung. Das Plugin leitet gut durch Cap Table und Runden; hier waren zusätzlich der erste negative Monat, einmalige Kaution, Vergütungsbeginn, auslaufende Raumnutzung und vor dem Notartermin fällige private Rechnungen nötig. Eine kurze Rechenanweisung im Hauptskill könnte diese Aspekte absichern, ohne jedes Mandat mit einem neuen Finanzmodell zu belasten.

4. Die wiederverwendbaren Referenzen sind teilweise auf genau diese Akte zugeschnitten. `status-register-produkt.md` nennt ausdrücklich die Schnittflug-Akte und die vorgesehenen Organe; der Hauptskill und die Quellenmemos wiederholen sieben Gründer und 21 %. Das erleichtert diesen Fall, begrenzt aber die Aussagekraft als unabhängigen Generalisierungstest. Konkrete Aktenfakten sollten aus Rechtsreferenzen in Beispiele oder Testmaterial ausgelagert werden; der nächste Verhaltenstest sollte andere Zahlen und Beteiligungsstrukturen verwenden.

Diese Punkte sind Verbesserungen der Anleitung, keine Behauptung, dass die vorliegende Ausführung die betreffenden Prüfungen ausgelassen hätte.

## 5 Offene Annahmen und Grenzen des Entwurfs

Die Vorlage wählt als vorläufige Ausgangslösung die GmbH mit 25.000 EUR voller Bareinzahlung, gemeinschaftlicher Vertretung und doppelter 75-%-Schwelle. Sie schlägt einen ausdrücklichen Bezugsrechtsablauf und ein präzisiertes schuldrechtliches Budgetrecht vor. Diese Entscheidungen sind nicht als Mandantenzustimmung erfunden. Die 2.500-EUR-Gründungskostenobergrenze stammt aus dem vorhandenen Satzungsentwurf und bleibt abzustimmen.

Mangels Einigung bleibt die Grundfassung zunächst ohne mitarbeitsabhängigen Zwangsrückerwerb und ohne Drag-along. Um die Arbeit nicht bei Schlagworten abzubrechen, liegt eine vollständige Vestingalternative mit vorgeschlagenen 25 % Vorleistungsanerkennung, 48 Monaten, zwölfmonatiger Anfangsfrist, Krankheitsschutz und Verkehrswertzahlung vor. Das sind ausdrücklich gewählte Verhandlungsparameter, keine angeblich unvermeidbaren oder marktverbindlichen Regeln. Persönliche Aufgaben-/Vergütungsvereinbarungen, Startdaten, Identitätsdetails und Nachweise wurden nicht erfunden.

Es wurden Markdown-Arbeitsprodukte wie beauftragt erstellt. Word-/PDF-Layout, notarielle Vollzugsfreigabe, eine verbindliche Statusentscheidung und vollständige Produktzulassung waren weder erreichbar noch Gegenstand dieses Verhaltenstests. Die tatsächlichen offenen Beiträge der Mandantschaft sind in Datei 04 konkret mit Zuständigkeit und Wirkung benannt.
