# 1. Bauwirtschaft: gezielte Nachprüfung der Visualisierung

Prüftag: 14. November 2026. Die aktive Auswahl enthält zehn Skills; alle 29 bisherigen Fachtexte und neun separaten HOAI-Werkstätten bleiben vorhanden. Diese Nachprüfung ändert keine Fachtexte.

## 1.1. Anlass und nachgewiesener Umfang

Bereits vor der Skillmigration passten zwei Skill- und neun Phasenwerkstatt-Bindungen nicht zu ihren Dateien. Für jede der elf Dateien reproduziert das Entfernen ausschließlich des markierten Visualisierungszusatzes bytegenau den historischen SHA-256. Die Abweichung enthält damit keine weitere Änderung des damals gebundenen Textes. Die vollständigen bisherigen Review-Objekte, alten Hashes, aktuellen Hashes und individuellen Prüfpunkte stehen in [der Prüfevidenz](bauwirtschaft-visualisierung-nachpruefung.json).

Die beiden Einstiegsskills wurden vollständig einschließlich ihrer Prüffälle gelesen. Für die neun Phasenwerkstätten wurde der untereinander identische Zusatz vollständig gelesen und jeweils mit phasenspezifischem Einstieg, Abschluss und individuellem Ergebnisfall samt Fortsetzung abgeglichen. Der Hash der ganzen Datei ist eine Fassungskennung; er behauptet keine erneute fachliche Vollprüfung ihres gesamten Hauptteils.

## 1.2. Konkrete Gegenprüfung

### 1.2.1. bauwirtschaft/skills/bauprojekt-starten-und-arbeitsstand-fortfuehren/SKILL.md

- Den gesamten Projektstartskill samt Visualisierungszusatz und Prüffall projektstart-planrevision-fortsetzen gelesen.
- Die neue Ansicht verlangt Planversion, Beleg, Kosten, Termin und Zuständigkeit; damit bleiben Plan C (freigegeben), Plan D (Prüfung) und T-17 trennbar.
- Die Aufforderung zur Fortschreibung desselben Arbeitsprodukts ist konsistent mit P-014; eine zusätzliche Ansicht ersetzt weder CSV noch ausformulierte Entscheidungsvorlage.
- Fehlende Werte werden nicht als null behandelt; eine Skizze darf keine Freigabe vortäuschen. Keine Ermächtigung für Auftrag, Zahlung oder externe Erklärung.
- 938000 EUR bleibt die im vorhandenen Kriterium erwartete unfreigegebene Änderungsvariante; dies ist eine redaktionelle Konsistenzprüfung, kein beobachtetes Modellergebnis.

### 1.2.2. bauwirtschaft/skills/projektziele-und-entscheidungsrahmen-festlegen/SKILL.md

- Den gesamten Projektzielskill samt Visualisierungszusatz und Prüffall projektziele-option-flachenerweiterung gelesen.
- Die Projektabschnittsansicht ergänzt die bestehende Zieltabelle und bewahrt die belegte Trennung von 600 m² Bedarf und 80 m² Option.
- Eine wählbare Termin- oder Planvariante darf die fehlende technische Zulässigkeit nicht ersetzen; der Zusatz verbietet gerade eine fingierte vermessene oder freigegebene Planung.
- Fortschreibung, Preisbasis und Belegführung bleiben mit Bruttobudget einschließlich Reserve und der nur geschätzten Erweiterungsvariante vereinbar.
- 1960000 EUR ist weiterhin die vorhandene Variantenrechnung; die neue Darstellung hebt den Vorrang des bestätigten 1800000-EUR-Budgets nicht auf. Kein Live-Modelllauf.

### 1.2.3. bauwirtschaft/bauwirtschaft-hoai-1-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Bedarfssicht muss 120 bestätigte Sitzplätze, die Option mit 160 Stehplätzen und die ungeklärte Dachraumnutzung getrennt zeigen.
- Die zwei Untersuchungen ergeben 4510 EUR netto und 5366,90 EUR brutto; eine rechnerische Reserve von 6633,10 EUR ersetzt weder Auftrag noch Tragfähigkeitsnachweis.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.4. bauwirtschaft/bauwirtschaft-hoai-2-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Variantenansicht muss gleiche Leistungsabgrenzung verwenden: A 2100000 EUR und B einschließlich fehlender Außenanlagen und Ausstattung 2190000 EUR netto.
- Die verworfene fünfte Gruppe bleibt außerhalb des Vergleichs; eine telefonische Vorverhandlung wird durch die Ansicht nicht zum Bauvorbescheid.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.5. bauwirtschaft/bauwirtschaft-hoai-3-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Kostenberechnung 3860000 EUR minus Kostenschätzung 3600000 EUR ergibt 260000 EUR; die enthaltenen 170000 EUR dürfen nicht nochmals zugeschlagen werden.
- Die Planansicht muss S-03/B, T-12/C und deren offene Kollision unterscheiden; funktionaler Bedarf bewilligt weder Budget noch Tragwerksverträglichkeit.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.6. bauwirtschaft/bauwirtschaft-hoai-4-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Nachreichungsansicht trennt A-04/C mit tatsächlichem Eingang am 24.09.2026 vom weiter fehlenden Brandschutznachweis und zeigt die vorgegebene Frist 02.10.2026.
- Eine angekündigte Lieferung, ein Ortstermin oder die Auswahl eines Planstands ersetzt weder behördlichen Eingang noch Nachbarzustimmung, Genehmigung oder Einreichungsbefugnis.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.7. bauwirtschaft/bauwirtschaft-hoai-5-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Detailansicht muss D-21/B, D-21/C und M-08 mit Status und Empfängerkreis führen; die bestätigte Bodenänderung erledigt weder Brandschutzanschluss noch Kabeltrasse.
- Interne Weiterleitung ist keine Baustellenzustellung, schematische Darstellung keine freigegebene Ausführungsplanung. Das bestellte Klärungsschreiben bleibt erforderlich.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.8. bauwirtschaft/bauwirtschaft-hoai-6-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Mengensicht muss bestätigte 12 Innentüren und 4 Außentüren von verworfenen 2 Zusatztüren trennen; 38400 EUR Türpaket plus 9500 EUR Schließanlage ergibt 47900 EUR netto.
- Planerpreis, fehlender Unternehmerpreis und Nullpreis werden getrennt; Visualisierung ersetzt keine Brandschutzklassifikation, Vergaberechtsprüfung oder Rechtsdienstleistungsbefugnis.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.9. bauwirtschaft/bauwirtschaft-hoai-7-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Vergleichsansicht führt die unveränderten Angebotssummen 125000, 121000 und 127000 EUR netto sowie die bei B fehlende Pflichtwartung; eine frei geschätzte Preisreparatur bleibt unzulässig.
- Aufklärung, Wertbarkeit und Zuschlagsentscheidung bleiben getrennt. Auswahl erzeugt keinen Zuschlag und erweitert nicht die ausdrücklich im Einstieg begrenzte Befugnis zur individuellen Skontoklausel.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.10. bauwirtschaft/bauwirtschaft-hoai-8-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Mengenfortschreibung führt nach Ergänzungsaufmaß 116 bestätigte und 4 offene Quadratmeter; bestätigte 9280 EUR netto minus tatsächlich bezahlte 4000 EUR netto ergibt 5280 EUR netto bzw. 6283,20 EUR brutto.
- Detail C, Tagesbericht B und unzureichendes Foto bleiben getrennte Belege. Eine Belegansicht behauptet weder eigene Ortskontrolle noch Verdeckungsfreigabe oder Zahlungsentscheidung.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

### 1.2.11. bauwirtschaft/bauwirtschaft-hoai-9-werkstatt.md

- Visualisierungszusatz vollständig gelesen; phasenspezifischen Einstieg und Abschluss sowie vorhandenen Ergebnisfall einschließlich Fortsetzung redaktionell gegengeprüft.
- Die Mängelansicht trennt den offenen Türmangel aus der Abnahme 15.10.2021 vom späteren Dachbefund; Nutzungsbeginn, Phasenzeitraum und konkrete Anspruchsfrist bleiben verschieden.
- Foto von unten, Kulanzbesichtigung und Auswahl eines Vorgangs begründen weder geklärte Ursache noch Anerkenntnis, Fristhemmung oder Freigabe der Sicherheit von 18000 EUR.
- Die Ansicht ergänzt das bestellte vollständige Dokument, verwendet nur belegte oder ausdrücklich bezeichnete Szenariowerte und bleibt bei fehlender Werkzeugfunktion als Text/Tabelle nutzbar. Keine tatsächliche Modell- oder Appletausführung.

## 1.3. Grenzen und technische Integration

Keine neuen Primärquellen wurden für diese Visualisierungsnachprüfung abgerufen. Historische Quellenstände wurden nicht verjüngt. Die Prüffälle wurden redaktionell gegengelesen; es gab keinen Live-Modelllauf, keinen ausgeführten Applet-Sichttest und keine beobachtete Modellantwort. Alle Laufstatus bleiben `not_run`.

Die Spezialtests unterscheiden nun aktive Auswahl, 29 erhaltene Fachtexte, 29 individuelle Ergebnisfälle und neun eigenständige Phasenwerkstätten. Sie prüfen weiter die einzelnen Inhaltsbindungen, Umfang und Form der Fachtexte, Verfügbarkeit der lokalen Verweise sowie die 15 Testakten und ihre nativen Dateien. Abschließende tatsächliche Prüfung am 14.11.2026 nach Regeneration der README: `python3 scripts/test-bauwirtschaft.py` besteht mit zehn von zehn Tests. Der zuvor abweichende README-Abgleich prüft jetzt die tatsächlich vorhandenen zehn aktiven Skills. Python-Kompilation und `git diff --check` der bearbeiteten Dateien bestanden. Diese technischen Tests ersetzen weder Primärquellenprüfung noch einen Live-Modelllauf.
