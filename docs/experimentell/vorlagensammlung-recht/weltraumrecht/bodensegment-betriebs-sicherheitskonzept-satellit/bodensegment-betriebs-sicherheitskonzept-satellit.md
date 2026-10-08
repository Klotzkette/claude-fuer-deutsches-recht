# Betriebs- und Sicherheitskonzept für ein Satellitenbodensegment

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Konzeptbestandteil, vor Freigabe entfernen]

Diese Vorlage ersetzt nicht die technische, sicherheitsfachliche und rechtliche Eigenleistung. Sie liefert das Betriebsgerüst, nicht das Bedrohungsmodell. Der Anwender bringt Missionsarchitektur, reale Berechtigungen, Schlüssel, Kontaktfenster und Wiederanlaufwerte; die Vorlage bringt Rollen, Freigabegates und die unbedingt zu prüfenden Stellen.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

An die

[freigabeverantwortliche Geschäftsleitung oder Missionsleitung]

### 1. Geltungsbereich und Schutzziele

1.1 Dieses Konzept gilt für das Bodensegment der Mission [Missionsname] in den Phasen [Integration / Inbetriebnahme / Regelbetrieb / Manöverbetrieb / Außerbetriebnahme] ab [Datum].

1.2 Erfasst sind Missionskontrollzentrum, Bodenstationen, Antennen, Netze, Rechen- und Cloud-Dienste, Telemetrie-, Bahn- und Nutzlastdaten, Telecommand-Systeme, Schlüsselverwaltung, Entwicklungs- und Testumgebungen sowie die in Anlage 1 bezeichneten Dienstleister.

1.3 Schutzziele sind die autorisierte Kontrolle des Raumfahrzeugs, Verfügbarkeit der Missionsführung, Integrität und Vertraulichkeit von Befehlen und Daten, Nachvollziehbarkeit jeder kritischen Handlung sowie ein beherrschter Übergang in und aus sicheren Betriebszuständen.

### 2. Systemgrenze und Verantwortungsmodell

2.1 System Owner ist [Name und Funktion]. Mission Operations Manager ist [Name und Funktion]. Security Officer ist [Name und Funktion]. Für Frequenzen, SatDSiG, Datenschutz, Exportkontrolle und Arbeitsschutz sind [Namen und Funktionen] verantwortlich.

2.2 Die Betriebsgrenze beginnt bei [Eingang Bahn- oder Missionsplanung] und endet bei [Ausführung des Befehls, Empfang der Telemetrie, Datenübergabe oder Archiv]. Schnittstellen und Vertrauensgrenzen sind in Anlage 2 dargestellt.

2.3 [Variante A — Eigenbetrieb]

Sämtliche kritischen Betriebsfunktionen werden durch Personal des Betreibers ausgeführt.

2.4 [Variante B — Dienstleisterbetrieb]

[Name des Dienstleisters] erbringt [konkret ausgelagerte Funktionen]. Weisungs-, Prüf-, Audit-, Exit- und Notfallrechte sind im Vertrag [Bezeichnung des Dienstleistungsvertrags] verbindlich gesichert.

### 3. Rollen und Berechtigungen

3.1 Planung, Erstellung, technische Prüfung, missionsfachliche Freigabe, kryptografische Signierung und Absetzen eines kritischen Befehls sind getrennten Rollen zugeordnet. Eine Person darf unvereinbare Rollen nicht zugleich ausüben.

3.2 Kritische Berechtigungen werden namentlich, befristet und nach dem Erforderlichkeitsprinzip vergeben. Anlage 3 enthält Rolle, Person, System, Berechtigungsumfang, Genehmiger, Beginn, Ende und letzte Rezertifizierung.

3.3 Eintritt, Rollenwechsel, längere Abwesenheit und Ausscheiden lösen spätestens innerhalb von [Frist] die Anpassung oder Sperrung sämtlicher physischer und logischer Zugänge aus.

### 4. Missionsplanung und Telecommand

4.1 Jeder Befehlsplan bezeichnet Raumfahrzeug, Softwarestand, Kontaktfenster, Zielzustand, zulässige Parameter, Abbruchkriterien und Rückfallverfahren. Veraltete oder nicht freigegebene Sequenzen sind technisch gegen Ausführung gesperrt.

4.2 [Variante A — Routinekommando]

Die Freigabe erfolgt durch [freigabeberechtigte Rollen] nach automatisierter Plausibilitätsprüfung und Simulation.

4.3 [Variante B — kritisches Kommando]

Das Kommando erfordert unabhängige Prüfung durch [zwei voneinander unabhängige Funktionen], Simulation in [Bezeichnung der Testumgebung], dokumentierte Go-No-Go-Entscheidung und aktive Bestätigung unmittelbar vor Übertragung.

4.3 Telecommands werden eindeutig identifiziert, versioniert, signiert und mit Ersteller, Prüfer, Freigeber, Übertragungszeit, Bodenstation, Ergebnis und Telemetrieantwort protokolliert.

4.4 Befehle außerhalb genehmigter Kontaktfenster, von Ersatzstandorten oder unter Notfallrechten sind nur nach dem Verfahren in Abschnitt 9 zulässig.

### 5. Telemetrie, Bahn- und Nutzlastdaten

5.1 Eingehende Daten werden an Quelle, Zeit, Integrität und erwarteten Wertebereichen geprüft. Abweichungen erzeugen [Alarmklasse, Reaktion und Eskalationsweg].

5.2 Rohdaten, verarbeitete Daten und abgeleitete Produkte bleiben über [Kennung und Metadaten] rückverfolgbar. Änderungen an Algorithmen, Kalibrierung oder Datenformaten werden versioniert und freigegeben.

5.3 [OPTIONAL — bei hochwertiger Erdfernerkundung: Daten werden ausschließlich an die in Anlage 4 bezeichneten, nach § 11 SatDSiG zugelassenen Anbieter übermittelt. Freigaben nach §§ 17 bis 20 SatDSiG bleiben dem Datenanbieter zugeordnet.]

### 6. Kryptografie und Schlüsselverwaltung

6.1 Schlüssel für Telecommand, Telemetrie, Datenübertragung und Administration werden nach Zweck, System und Umgebung getrennt. Erzeugung, Import, Aktivierung, Rotation, Sicherung, Widerruf und Vernichtung folgen Anlage 5.

6.2 Private oder symmetrische Schlüssel verlassen [Hardware-Sicherheitsmodul oder gesicherte Umgebung] nicht im Klartext. Notfallschlüssel unterliegen [Vier-Augen-Verwahrung, Zugriffsvoraussetzungen und Verwendungsprotokoll].

6.3 Bei vermuteter Kompromittierung werden betroffene Schlüssel unverzüglich gesperrt, Ersatzschlüssel aktiviert, Systeme und Gegenstellen geprüft und die in Abschnitt 10 bestimmten Stellen informiert.

### 7. Netze, Standorte und Lieferkette

7.1 Produktions-, Test-, Büro- und Gastnetze sind getrennt. Übergänge sind auf dokumentierte Verbindungen beschränkt und werden durch [Kontrollen] überwacht.

7.2 Zutritt zu Missionskontrolle, Antennensteuerung, Server- und Schlüsselräumen wird rollenbezogen freigegeben und protokolliert. Besucher bleiben begleitet.

7.3 Software, Firmware, Bibliotheken und Konfigurationen werden aus freigegebenen Quellen bezogen, auf Integrität geprüft und in Anlage 6 inventarisiert. Kritische Schwachstellen lösen [Bewertung, Frist, Kompensationsmaßnahme und Betriebsentscheidung] aus.

### 8. Routinebetrieb und Schichtübergabe

8.1 Jede Schicht übernimmt aktuellen Raumfahrzeugzustand, offene Anomalien, geplante Kontakte, aktive Sperren, Wetter- oder Weltraumwetterlage und bevorstehende Manöver anhand des Übergabeprotokolls in Anlage 7.

8.2 Abweichungen von Betriebsverfahren bedürfen einer dokumentierten Ausnahme mit Grund, Risiko, kompensierender Kontrolle, Geltungsdauer und Genehmiger.

### 9. Notbetrieb und Wiederanlauf

9.1 Auslöser für Safe Mode, Kontaktverlust, Ausweichbodenstation, Notfallkommando und Betriebsunterbrechung sind in Anlage 8 mit Schwelle und Entscheidungsbefugnis festgelegt.

9.2 [Variante A — Kontaktverlust]

Nach [Dauer und Anzahl fehlgeschlagener Kontaktversuche] wird das Wiedergewinnungsverfahren [Bezeichnung des Wiedergewinnungsverfahrens] ausgelöst.

9.3 [Variante B — Kontrollverlust oder unautorisierter Befehl]

Telecommand wird gesperrt, Schlüssel werden gewechselt, Beweise werden gesichert und die Krisenorganisation übernimmt.

9.4 Wiederanlaufziele betragen für [Funktion] höchstens [Zeit bis Wiederherstellung] bei einem höchstens tolerierten Datenverlust von [Zeitraum]. Die Werte werden durch [Testart und Intervall] nachgewiesen.

### 10. Anomalien, Sicherheitsvorfälle und Meldungen

10.1 Ereignisse werden nach [Kategorien und Schweregraden] klassifiziert. Das Lageprotokoll erfasst Zeitpunkt, Erkennung, Systeme, Auswirkungen, Maßnahmen, Beweise, Entscheidungen und Abschluss.

10.2 Der Security Officer prüft unverzüglich Meldepflichten nach SatDSiG, Datenschutzrecht, Telekommunikationsrecht, vertraglichen Vorgaben und sonstigem anwendbarem Recht. Fristbeginn und Entscheidung werden dokumentiert.

10.3 Technische Beweise werden unverändert gesichert. Bereinigung beginnt erst, wenn Sicherheitsinteresse und Beweissicherung miteinander abgestimmt sind.

### 11. Aufzeichnungen, Tests und Änderungskontrolle

11.1 Aufbewahrungsfristen ergeben sich aus Anlage 9. Soweit § 5 SatDSiG anwendbar ist, werden die dort erfassten Befehlsangaben mindestens fünf Jahre nach Befehlsausführung aufbewahrt.

11.2 Notbetrieb, Wiederherstellung, Schlüsselwechsel, Ersatzbodenstation und Kontaktverlust werden mindestens [Intervall] getestet. Feststellungen erhalten Verantwortlichen und Erledigungstermin.

11.3 Änderungen an Raumsegment, Bodensegment, Dienstleister, Standort, Frequenz, Sicherheit oder Datenfluss durchlaufen vor Produktivsetzung Folgenanalyse, Test, rechtliche Prüfung und Freigabe.

### 12. Inkraftsetzung

12.1 Dieses Konzept tritt am [Datum] in Kraft. Eigentümer ist [Funktion]. Die nächste Regelprüfung erfolgt spätestens am [Datum] sowie anlassbezogen nach wesentlichen Änderungen oder Vorfällen.

[Ort], den [Datum]

[Name und Funktion Freigabeverantwortlicher]

[Unterschrift oder dokumentierte elektronische Freigabe]

## Anlagen

### Anlage 1 — Komponenten und Dienstleister

1.1 [Komponente, Betreiber, Standort, Vertrag, Verfügbarkeit und Exit].

### Anlage 2 — Architektur und Datenflüsse

2.1 [Systemgrenzen, Vertrauenszonen, Netze, Schnittstellen und Datenwege].

### Anlage 3 — Rollen- und Berechtigungsmatrix

3.1 [Person, Rolle, System, Recht, Genehmiger, Laufzeit und Rezertifizierung].

### Anlage 4 — Datenempfänger

4.1 [Empfänger, Rechtsgrund, Zulassung, Datenart und Übermittlungsweg].

### Anlage 5 — Schlüsselplan

5.1 [Schlüssel, Zweck, Eigentümer, Speicherort, Rotation, Ersatz und Widerruf].

### Anlage 6 — Software- und Konfigurationsinventar

6.1 [Komponente, Version, Herkunft, Prüfsumme, Freigabe und Schwachstellenstatus].

### Anlage 7 — Schicht- und Kontaktprotokoll

7.1 [Schicht, Kontakte, Zustand, offene Punkte, Sperren und Übergabe].

### Anlage 8 — Notfallkarten

8.1 [Ereignis, Schwelle, Sofortmaßnahme, Entscheidung, Kommunikation und Rückkehr].

### Anlage 9 — Aufbewahrungs- und Testplan

9.1 [Aufzeichnung oder Kontrolle, Rechtsgrund, Frist, System, Verantwortlicher und Prüftermin].

---

Lizenz: Apache-2.0 OR MIT.
