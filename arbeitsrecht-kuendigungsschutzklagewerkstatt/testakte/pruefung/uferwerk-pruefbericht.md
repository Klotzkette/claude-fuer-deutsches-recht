# 1. Technischer und redaktioneller Prüfstand Uferwerk

Prüfdatum: 1. November 2026. Aktenstand: 30. Oktober 2026. Die Fallfiktion dient der eigenen Prüfung einer Berufung und ist kein Muster für eine fehlerfreie erstinstanzliche Entscheidung.

## 1.1. Bestand und Ausgabe

38 Unterlagen der Vorgeschichte, 34 Dokumente der ersten Instanz und 21 Dokumente nach dem Urteil ergeben 93 Aktenstücke. Mit dem fünfseitigen Aktenverzeichnis umfasst das Paket 94 PDFs und 155 Seiten. Der Arbeitsvertrag hat sieben, das Urteil zehn Seiten. Das ZIP enthält daneben ausschließlich die vorgeschriebene README.txt auf Wurzelebene. Keine Originalformatdateien, keine Gesamt-PDF, keine Berufungsbegründung, keine fertige Erfolgsaussichtenprüfung und kein Lösungsblatt sind enthalten.

Der Bestandsnachweis `uferwerk-bestand.json` enthält die SHA-256-Prüfsummen der drei Satzquellen, jeder PDF und des ZIP sowie die Seitenzahlen. Das Archiv ist durchsuchbar und technisch fehlerfrei. README.txt beginnt wortgetreu mit dem deutschen und englischen Pflichthinweis; in den PDFs steht dieser Hinweis nicht. Alle Kontakte verwenden reservierte .example-Domains.

## 1.2. Redaktioneller Abgleich

Der Tatsachenkern des Flyers ist erhalten: Uferwerk, 140 Arbeitnehmer in einem Betrieb, fünfzehn aufgehobene Designerstellen, Lisa Muster mit achtzehn Jahren Betriebszugehörigkeit und zwei Kindern, Vertriebsbeschäftigung und Massenentlassungsverfahren. Vertragsanbahnung, Familie, Arbeit und Prozess sind vollständig aus der jeweiligen Dokumentperspektive ausgestaltet. Die Gegenprüfung erfasst den Arbeitgeber, Personen- und Gehaltsdaten, Tätigkeiten, Anlagenkennzeichen, Vertrags- und Kündigungsdaten, Zeugen, Urteil und Zustellung sowie die Herkunft später beschaffter Belege. Unbeabsichtigte Abweichungen wurden korrigiert; die für die eigene Rechtsmittelprüfung vorgesehenen Widersprüche zwischen Beweisergebnis und Urteil bleiben erhalten.

Die Fristnotiz berücksichtigt die Zustellung des vollständigen Urteils am 14. Oktober 2026, die Einlegungsfrist bis Montag, 16. November 2026, und die Begründungsfrist bis 14. Dezember 2026. Die reine Berufungseinlegung am 30. Oktober enthält keine Begründungsbausteine. Die Ausgangskontrolle innerhalb der Fallfiktion lässt die Begründungsfrist ausdrücklich offen. Neue Tatsachen, später beschaffte Beweise und bereits früher vorhandene Unterlagen sind anhand ihrer tatsächlichen Verfügbarkeit unterscheidbar.

Die amtliche Gerichtszuordnung und die einschlägige Bezeichnung der 7. Kammer wurden geprüft; das Fallaktenzeichen ist frei erfunden. Die Rechtsprechungsprüfung und die Grenzen der sechs Flyerentscheidungen sind in den Quellenkarten und im getrennten Referentenmaterial dokumentiert. Es wird kein amtlicher Volltext mit Randnummern behauptet, wenn nur eine amtliche Kurzveröffentlichung verifiziert ist.

## 1.3. Satz- und Sichtprüfung

Times New Roman 11 pt ist die Grundschrift. Tabellen verwenden ein lesbares gesondertes Layout, die Kanzleimarken eine farbige Wortmarke. Alle 155 Seiten wurden gerendert und auf dreizehn Kontaktbögen visuell geprüft; zusätzliche Einzelansichten betreffen insbesondere Urteil, Zeugenaussagen, Berufungsschrift, Vertrag und die Personalvergleichstabelle. Isolierte Signaturseiten, verwaiste Schlussüberschriften und getrennte Jahreszahlen wurden im Satz behoben. Der abschließende Koordinatenscan meldet keine Texte außerhalb des Satzspiegels. Die letzte Anpassung betrifft allein die Worttrennung in V30; alle anderen PDFs sind bytegleich mit dem vollständig visuell geprüften Stand, und die drei geänderten V30-Seiten wurden erneut gerendert.

## 1.4. Automatisierte Prüfung und Reichweite

`scripts/test-uferwerk-berufungsakte.py` prüft den genauen Archivbestand, Quellen- und PDF-Prüfsummen, Seitenzahlen, lesbare Texte, Grundschrift, Fristenübergaben, Nachweisverfügbarkeit und das Fehlen eines Begründungsschriftsatzes. `scripts/test-kuendigungsschutzklagewerkstatt.py` bindet die Prüfung in den bisherigen Elf-Skill-/Prompt-/Aktenbestand ein. Der Release umfasst 37 Dateien; das PDF-ZIP ist mit dem geprüften Bestand identisch, Begleitprompts und Fallakten bleiben außerhalb des installierbaren Plugin-ZIP.

Die Prüfung belegt redaktionellen Abgleich, technische Konsistenz und visuelle Qualität. Sie ist kein tatsächlicher Modelllauf mit einer verfassten Berufungsbegründung und keine Aussage, dass das bewusst angreifbare Urteil materiell richtig wäre.
