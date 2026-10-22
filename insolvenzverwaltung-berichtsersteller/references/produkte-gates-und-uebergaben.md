# Produkte, Gates und Übergaben

## 1. Produktkennungen

| Kennung | Produkt | Führende Inhalte |
| --- | --- | --- |
| `BER-INT` | Verfahrens- und Berichtskarte | Auftrag, Rolle, Anlass, Zeitraum, Stichtag, Frist, gerichtliche Vorgabe, Belegplan |
| `BER-ZW` | Zwischenbericht | Veränderungen, Stand, Risiken, Entscheidungen, nächste Maßnahmen, Anlagen |
| `BER-SB` | Schlussbericht | Verfahrensverlauf, Masse, Verwertung, Tabelle, Kosten, offene Restpunkte, Schlussvorschlag |
| `BER-SR` | Schlussrechnung und Kontenabgleich | Einnahmen, Ausgaben, Unterrechnungen, Konten, Kasse, Belege, Differenzen |
| `BER-MV` | Masse-, Verwertungs- und Betriebsmodul | Vermögensbestand, Rechte, Erlöse, Betrieb, Verträge, Personal, Restpositionen |
| `BER-FQ` | Forderungs-, Sicherheiten- und Quotenmodul | Tabellenstand, Rang, Bestreiten, Absonderung, Ausfall, Rückbehalt, Quote |
| `BER-SKV` | Steuer-, Kosten- und Vergütungsmodul | Steuerperioden, Bescheide, Verfahrenskosten, Masseverbindlichkeiten, Vergütungsstatus |
| `BER-PAH` | Prozess-, Anfechtungs- und Haftungsmodul | Anspruch, Gegner, Stadium, Streitwert, Kosten, Risiko, Erlösstatus |
| `BER-SVA` | Schlussverteilungs- und Aufhebungspaket | Schlussverzeichnis, Zustimmung, Termin, Zahlung, Hinterlegung, Vollzug, Aufhebungsübergabe |
| `BER-NV` | Nachtragsverteilungspaket | Fund, Massezuordnung, Antrag, Anordnung, Rechnung, Auszahlung, Rechnungslegung |
| `BER-CTRL` | Berichtscockpit | Produktstatus, führende Fassungen, Gates, Fragen, Fristen, nächste Route |

## 2. Gates

| Gate | Freigabegegenstand | Mindestnachweis | Bei Nichterfüllung |
| --- | --- | --- | --- |
| `G1 Auftrag` | Berichtstyp, Rolle, Zeitraum und Stichtag | Verfahrenskarte und gerichtliche Vorgabe | keine Empfängerfassung |
| `G2 Belegbestand` | Vollständigkeit für den Auftrag | Belegmatrix, Lückenliste und führende Datenstände | Lücken offen ausweisen |
| `G3 Rechenwerk` | Konten, Forderungsbasis und Summen | Dreifachabgleich, Kontrollsummen und Vier-Augen-Prüfung | keine Quote und keine Schlussreife |
| `G4 Fachfassung` | juristische und sachliche Endfassung | namentliche fachliche Freigabe der genauen Version | nur Entwurf |
| `G5 Einreichung` | konkrete Übersendung an Gericht oder Ausschuss | namentliche Freigabe, Empfänger, Weg und Anlagenliste | keine Außenhandlung |
| `G6 Verteilung` | gerichtliche und organschaftliche Voraussetzungen | Ausschusszustimmung soweit erforderlich, gerichtliche Zustimmung, Termin- und Einwendungsstand | kein Auszahlungslauf |
| `G7 Zahlung` | konkreter Zahlungslauf oder Hinterlegung | freigegebene Liste, verifizierte Bankdaten, Vier-Augen-Freigabe | keine technische Zahlung |
| `G8 Nachtrag` | Nachtragsverwertung und -verteilung | Massezugehörigkeit, gerichtliche Anordnung, Kostenprüfung und Schlussverzeichnisbezug | keine Nachtragsauszahlung |

## 3. Übergaberegel

Jede Übergabe nennt Produktkennung, Dateipfad, Hash, Version, Stichtag, maßgebliche gerichtliche Beschlüsse, verwendete Belege, Rechenstand, Quellenstatus, offene Frage, Frist, zuständige Person, erreichte Gates und nächste Route. Der empfangende Skill bestätigt, welche Fassung er übernimmt. Er verändert nicht stillschweigend den Stichtag oder die Forderungsbasis.

## 4. Standardroute

`BER-INT` eröffnet den Lauf. `BER-ZW` wird aus den jeweils aktualisierten Fachmodulen `BER-MV`, `BER-FQ`, `BER-SKV` und `BER-PAH` erzeugt. Für den Abschluss prüft `BER-CTRL` die Abschlussreife. Danach werden `BER-SB`, `BER-SR` und `BER-FQ` mit identischem Stichtag synchronisiert. `BER-SVA` übernimmt nur freigegebene Daten. Nach Aufhebung eröffnet ein späterer Gegenstand einen neuen Vorgang `BER-NV`, ohne den historischen Schlussbericht zu überschreiben.

## 5. Sperrwirkungen

Eine ungeklärte Kontendifferenz sperrt `G3`. Eine offene wesentliche Verwertung oder ein laufender Prozess mit nicht behandelter Auswirkung sperrt eine positive Aussage zur Abschlussreife. Eine nicht festgesetzte Vergütung wird nicht als endgültige Ausgabe gebucht. Eine bestrittene Forderung ohne abgeschlossene Behandlung nach §§ 189 bis 192 InsO wird nicht wie eine unstreitige Forderung ausgezahlt. Fehlende gerichtliche Zustimmung oder menschliche Zahlungsfreigabe sperrt jede Außenwirkung.
