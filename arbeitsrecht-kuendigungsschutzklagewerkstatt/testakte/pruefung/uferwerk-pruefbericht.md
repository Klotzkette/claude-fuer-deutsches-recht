# 1. Technischer und redaktioneller Prüfstand Uferwerk

Prüfdatum: 1. November 2026. Aktenstand: 30. Oktober 2026. Die Fallfiktion dient der eigenen Prüfung einer Berufung; das klageabweisende Urteil ist bewusst angreifbar.

## 1.1. Bestand und Ausgabe

38 Unterlagen der Vorgeschichte, 34 Dokumente der ersten Instanz und 21 Dokumente nach dem Urteil ergeben 93 Aktenstücke. Mit dem fünfseitigen Aktenverzeichnis umfasst das Paket 94 PDFs und 185 Seiten. Der Arbeitsvertrag hat zehn, das Urteil dreiundzwanzig, die Zeugenvernehmung sieben Seiten. Das ZIP enthält daneben ausschließlich die vorgeschriebene README.txt auf Wurzelebene. Originalformate, Gesamt-PDF, Berufungsbegründung, fertige Erfolgsaussichtenprüfung und Lösungsblatt sind nicht enthalten.

Der Bestandsnachweis `uferwerk-bestand.json` enthält Seitenzahlen und SHA-256-Prüfsummen der drei Aktenquellen, des Builders, des Satzmoduls, des Quellenledgers, jeder PDF und des ZIP. README.txt beginnt wortgetreu mit dem deutschen und englischen Pflichthinweis; die PDFs enthalten diesen Hinweis nicht. Die Archive sind flach, durchsuchbar und technisch geprüft. Fiktive Kontakte verwenden reservierte .example-Domains.

## 1.2. Redaktioneller und rechtlicher Abgleich

Der Tatsachenkern des Flyers ist erhalten: Uferwerk, 140 Arbeitnehmer in einem Betrieb, fünfzehn entfallende Designstellen, Lisa Muster mit achtzehn Jahren Betriebszugehörigkeit und zwei Kindern, Vertriebsbeschäftigung und Massenentlassungsverfahren. Anbahnung, Familien- und Erwerbsverlauf, Qualifikation, Stellenbesetzung, Betriebsrat, Kündigung, Prozess und Nachurteilskorrespondenz sind aus der jeweiligen Dokumentperspektive ausgestaltet.

Der Vertrag umfasst rund 4.300 Wörter in zwanzig Ziffern. Anfangsgehalt von 2.800 EUR, Beginn am 1. März 2008, 40 Wochenstunden, Konstanz und der gleichwertige kaufmännische Einsatzrahmen bleiben erhalten. Spätere Gehaltsanpassungen stehen in den Nachträgen. Die Ausarbeitung des Verlagsalltags enthält keine rückdatierte DSGVO-, MiLoG- oder eAU-Regelung. Die für die Bearbeitung maßgeblichen Freistellungs- und Kündigungsregelungen werden als damaliger Vertragsinhalt erhalten.

Neun Prozessdokumente sind substanziell vertieft: Klage, frühe Ergänzung, Erwiderung, Replik, Duplik, Triplik, weitere Stellungnahme, Kammerprotokoll und Urteil. Tatsachen, Beweisangebote, abgestufte Darlegung, Unternehmerentscheidung und tatsächlicher Arbeitswegfall, Vergleichbarkeit, freie Beschäftigung sowie die unterschiedlichen Weiterbeschäftigungsgrundlagen werden getrennt behandelt. Die Beweisaufnahme enthält konkrete Vorhalte und Antworten beider Zeugen. Unbeabsichtigte Behauptungen einer vorhandenen Dateinamenliste wurden korrigiert; die Akte enthält gerade keinen solchen Beleg zum ersten Anzeigeeingang. Die vorgesehenen unzutreffenden gerichtlichen Anwendungen bleiben als Bearbeitungsstoff erhalten.

Vierzehn Entscheidungen und fünf tatsächlich gelesene Literaturtexte sind im gesonderten Vertiefungsledger mit Fundstelle, Zugangsstatus, Verfügbarkeit und Aussagegrenze dokumentiert. Die rechtlichen Nachweise und die zeitliche Verfügbarkeit wurden unabhängig gegengeprüft. Es gibt keine fingierten ErfK-, KR- oder Schaub-Fundstellen. Knapp paraphrasierte Literatur wird sparsam verwendet; auch bei vorsichtiger Zurechnung vollständiger belegter Absätze bleibt jeder der fünf Texte unter zweihundert Wörtern. Es wurden keine eigenständigen wörtlichen Literaturübernahmen festgestellt. Volltextrandnummern der Entscheidungen 2026 erscheinen erst nach ihrer amtlichen Bereitstellung.

Die Gerichtszuordnung und die Bezeichnung der 7. Kammer passen zum Verfahrensort; das Aktenzeichen ist erfunden. Das Urteil wurde vollständig am 14. Oktober 2026 zugestellt. Die Fristnotiz nennt die Einlegungsfrist bis Montag, 16. November, und die Begründungsfrist bis 14. Dezember 2026. Die Berufungsschrift vom 30. Oktober wahrt nur die Einlegungsfrist. Herkunft, frühere Beschaffungsversuche und tatsächliche Verfügbarkeit weiterer Unterlagen bleiben nachvollziehbar.

## 1.3. Satz- und Sichtprüfung

Times New Roman 11 pt ist die Grundschrift. Tabellen verwenden ein gesondertes lesbares Layout. Beide Kanzleien besitzen eigene Wortmarken; Urteil, Niederschriften, gerichtliche Post, interne Verfügung, Vertrag, Unternehmensunterlagen, Mailausdrucke und elektronische Empfangsvermerke haben passende Satzformen. Das Urteilsrubrum steht außerhalb der dezimalen Sachgliederung. Archivkennzeichen V/P/N werden nicht zu angeblichen historischen gerichtlichen Anlagen umetikettiert. Echte Unterschriften, Dienstsiegel und technische Transportzertifikate werden nicht imitiert.

Alle 185 Seiten wurden gerendert und auf sechzehn Kontaktbögen visuell geprüft. Einzelansichten betreffen insbesondere Urteilsanfang und -schluss, Zeugenvernehmung, Vertragsschluss, Anträge, Mailfolgen und Personal-/Einarbeitungstabellen. Erkannte Satzfehler wurden behoben: getrennte Datumsbestandteile, unpassende BR-Absenderfüße, ein vom Nachrichtentext abgetrennter Mailkopf, Inline-Mailtext im Datumsfeld, unsaubere Mailadressentrennung und doppelte Namensabschlüsse. Im Schlussdurchgang wurden alle neun geänderten PDFs erneut gerendert; die übrigen fünfundachtzig PDFs sind bytegleich mit dem bereits vollständig gesichteten Stand. Der Koordinatenabgleich prüft zusätzlich Text außerhalb der Seitenränder.

## 1.4. Automatisierte Prüfung und Reichweite

`scripts/test-uferwerk-berufungsakte.py` prüft Archivbestand und Formatwahl, Quellen-/Produktions-/PDF-Prüfsummen, Seitenzahlen, lesbare Texte, Grundschrift, vollständigen Absatzinhalt nach dem Satz, Quellenledger, zeitgerechte Volltextzitate, Urteilsaufbau und Rubrumsidentitäten, Fristübergaben und das Fehlen eines Begründungsschriftsatzes. Strukturierte Mailfelder werden nach ihrer Aufteilung auf Kopf und Nachrichtentext abgeglichen. Seitenköpfe und Fußzeilen werden bei diesem Absatzvergleich ausgeblendet.

`scripts/test-kuendigungsschutzklagewerkstatt.py` bindet die Akte in den vorhandenen Elf-Skill-/Prompt-/Aktenbestand ein. Der Komponentenrelease umfasst 37 Dateien; das PDF-ZIP entspricht dem geprüften Bestand. Begleitprompts und Fallakten bleiben außerhalb des installierbaren Plugin-ZIP. Die fünf früheren Fallfassungen behalten ihre Dateien und Formate.

Die Prüfung belegt redaktionellen Abgleich, technische Konsistenz und visuelle Qualität. Sie ist kein tatsächlicher Modelllauf mit einer verfassten Berufungsbegründung und kein Testat materieller Richtigkeit des bewusst angreifbaren Urteils.
