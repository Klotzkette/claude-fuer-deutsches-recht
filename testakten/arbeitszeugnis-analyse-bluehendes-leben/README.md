# Testakte: Arbeitszeugnis-Analyse — aus dem blühenden Leben

## ⬇️ Direkt-Download

| Testakte | Direkt-Download |
| --- | --- |
| `testakte-arbeitszeugnis-analyse-bluehendes-leben` (diese Akte) | [testakte-arbeitszeugnis-analyse-bluehendes-leben.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-arbeitszeugnis-analyse-bluehendes-leben.zip) |

Die Testakte ist **kein Teil des Plugins** und wird separat als ZIP-Datei aus dem GitHub-Release geladen. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.


Diese Testakte enthält **zehn Arbeitszeugnisse aus zehn verschiedenen Branchen und Berufen**, jeweils ein bis zwei Seiten lang, alle formal freundlich und im üblichen Wohlwollens-Stil verfasst. Die Akte ist als realistisches Trainingsmaterial für das Plugin [`arbeitszeugnis-analyse`](../../arbeitszeugnis-analyse) gedacht.

## Zweck der Akte

Die Zeugnisse sehen oberflächlich höflich, vollständig und unkritisch aus. Tatsächlich verteilen sich die Bewertungen über die gesamte Notenskala. Die Aufgabe für jeden Skill dieses Plugins ist es, aus Briefkopf, Aufbau, Wortwahl, Steigerungsadverbien, Zufriedenheitsformeln, Beendigungsgrund, Schlussformel und Unterzeichnerstruktur die wahre Bewertung herauszulesen.

Es liegt **keine Musterlösung bei**. Welche Note sich hinter dem jeweiligen Zeugnis verbirgt, soll der Skill selbst aus dem Material herleiten.

## Aktenübersicht

| Nr. | Name | Beruf | Branche | Zeugnistyp | Beendigungsgrund |
|-----|------|-------|---------|------------|------------------|
| 01 | Gunhilde Brachvogel-Riemenschneider | Pharmazeutisch-technische Assistentin | Apotheke (Würzburg) | Endzeugnis | Eigener Wunsch, Wechsel zu Filialleiterstelle |
| 02 | Volkmar Eitel-Hartung | Angestellter Rechtsanwalt | Anwaltspartnerschaft (Düsseldorf) | Endzeugnis | Eigene Kanzleigründung |
| 03 | Edelgard Schwerdtfeger | Medizinisch-technische Radiologieassistentin | Radiologische Gemeinschaftspraxis (Hof) | Endzeugnis | Eigener Wunsch |
| 04 | Friedhelm Pöttering | Lagermeister | Eisenwarenhandel (Gütersloh) | Endzeugnis | Betriebsbedingte Kündigung im Rahmen Umstrukturierung |
| 05 | Walpurga Dietrichsen-Hofstätter | Zahnmedizinische Fachangestellte | Zahnarztpraxis (Ravensburg) | Endzeugnis | Beendigung ohne weitere Angabe |
| 06 | Reinhilde Eisenträger | Filialleiterin | Sparkasse (Selb/Marktredwitz) | Zwischenzeugnis | Antritt Elternzeit |
| 07 | Dietram Auerwald-Bornhöft | Sachbearbeiter Speditionsdisposition | Logistikunternehmen (Bremen) | Endzeugnis | Aufhebung im gegenseitigen Einvernehmen |
| 08 | Hartmut Greifenklau | Empfangsleiter | Vier-Sterne-Hotel (Bautzen) | Endzeugnis | Beendigung ohne weitere Angabe |
| 09 | Ortrud Falckenstein | Examinierte Altenpflegerin, Wohnbereichsleitung | Seniorenresidenz (Einbeck) | Endzeugnis | Eintritt in den Ruhestand |
| 10 | Burchard Holzapfel | Industriemechaniker, Schichtführer | Maschinenbau (Oelsnitz/Erzgebirge) | Endzeugnis | Beendigung ohne weitere Angabe |

## Struktur der einzelnen Akten

Jedes Zeugnis liegt als eigenes PDF in einem eigenen Unterordner. Der Dateiname folgt dem Schema `Arbeitszeugnis_<nr>-<vorname>-<nachname>-<beruf>.pdf`.

Alle Zeugnisse enthalten:

- vollständigen Briefkopf mit Firmenname, Anschrift, Telefon, Fax, E-Mail sowie ggf. USt-IdNr. oder Registernummer
- schlichte Briefkopfmarke mit Kanzlei-, Praxis-, Hotel-, Bank- oder Unternehmensbezug
- Ort und Datum der Ausstellung
- Personalstammdaten (Name, Geburtsdatum, Eintritt, Austritt, Position)
- Aufgabenbeschreibung als Fließtext und Bulletliste
- Bewertungsteile zu Fachkenntnissen, Arbeitsweise, Belastbarkeit, Engagement, Arbeitserfolg und Verhalten
- Beendigungspassage und Schlussformel
- Unterschriftsblock mit ein oder zwei Unterzeichnern und Stempel-Hinweis

## Mögliche Arbeitsaufträge an die Skills

- Note pro Zeugnis ermitteln, einzeln und im Gesamtbild
- Codeworte, Negationen, Auslassungen und Steigerungsadverbien markieren
- Schaufenster-Pattern und Bereichs-Drift erkennen
- Schlussformel auf Vollständigkeit prüfen
- Aus den Befunden eine Mandantenkommunikation, ein Berichtigungsverlangen oder eine Klagestrategie entwickeln

## Technisches

- Format der Zeugnisse: PDF, A4, deutsche Typographie mit Anführungszeichen "...", Halbgeviertstrich und korrekt gesetzten Umlauten
- Keine Blindtexte, keine leeren Lücken und keine Musterlösung im Aktenbestand
- Personen, Firmen, Adressen und Personalnummern sind frei erfunden; Übereinstimmungen mit realen Personen oder Unternehmen sind nicht beabsichtigt
- Die Zeugnisse sind als Trainings- und Testmaterial gedacht und ersetzen keine rechtliche Beratung
