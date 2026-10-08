# Antrag auf Genehmigung eines hochwertigen Erdfernerkundungssystems (§§ 3, 4 SatDSiG)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Antragsbestandteil, nicht einreichen]

Diese Vorlage ersetzt nicht die anwaltliche und sicherheitstechnische Eigenleistung. Sie liefert das Gerüst, nicht die BSI-Prüfung. Der Anwender bringt Sensor, Kommandokette, Datenflüsse, Personen und Schutzverfahren; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Die BSI-Beteiligung ist bereits während der Systemarchitektur einzuleiten.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

### Adressat und Antragsteller

An das Bundesamt für Wirtschaft und Ausfuhrkontrolle

[zuständiger Bereich und Anschrift]

Antragsteller und Betreiber: [Firma, Rechtsform, Sitz, Register und Vertretung]

System: [Missionsname, Satellit und Sensor]

Aktenzeichen der Behörde: [neu / Aktenzeichen]

Betreff: Antrag auf Genehmigung nach § 3 Abs. 1 Satellitendatensicherheitsgesetz (SatDSiG)

[Ort], den [Datum]

### 1. Antrag

1.1 Der Antragsteller beantragt die Genehmigung zum Betrieb des hochwertigen Erdfernerkundungssystems [Bezeichnung] ab [geplante Inbetriebnahme].

1.2 Die Genehmigung soll die in Anlage 1 bezeichnete Systemkonfiguration, Sensorbetriebsmodi, Kommando- und Bodenstandorte sowie Datenpfade erfassen.

1.3 [OPTIONAL — nur bei stufenweiser Inbetriebnahme]

Die Genehmigung soll zunächst die Test- und Kalibrierungsphase [Zeitraum und Betriebsmodi der Testphase] und nach Vorlage der Nachweise [konkrete Nachweise für den Übergang] den Regelbetrieb umfassen.

### 2. Anwendungsbereich und Betreiberrolle

2.1 Der Antragsteller steuert das System in eigener Verantwortung. Die unveränderbaren Befehlsfolgen werden am Standort [Ort in Deutschland] hergestellt und über [Bodenstationen und Netze] abgesetzt.

2.2 Das System fällt nach § 1 Abs. 1 Nr. 1 SatDSiG in den deutschen Anwendungsbereich, weil [deutsche Rechtsform, Verwaltungssitz oder Kommandoherstellung im Bundesgebiet].

2.3 Betreiber, Eigentümer, Hersteller, Bodenstationsdienstleister, Cloud- oder Rechenzentrumsanbieter und Datenanbieter sind in Anlage 2 mit ihren Entscheidungs- und Zugriffsbefugnissen abgegrenzt.

### 3. System und Hochwertigkeit

3.1 Das raumgestützte System verwendet [optischen, multispektralen, hyperspektralen, Radar-, Mikrowellen- oder gravimetrischen] Sensor mit den Parametern [geometrische, spektrale, radiometrische und zeitliche Auflösung sowie weitere Parameter].

3.2 Die Bewertung nach SatDSiV ergibt für die Betriebsmodi [Modi] einen besonders hohen Informationsgehalt. Berechnung, Eingangsdaten und Versionsstand sind in Anlage 3 reproduzierbar dokumentiert.

### 4. Zuverlässigkeit

4.1 Antragsteller, Vertretungsorgane und sicherheitsverantwortliche Leitung verfügen über die erforderliche Zuverlässigkeit. Organigramm, Lebensläufe, Register- und Erklärungsmaterial befinden sich in Anlage 4.

4.2 Tatsachen, die Zuverlässigkeit oder sichere Betriebsführung beeinträchtigen könnten, bestehen [nicht / wie folgt und mit Gegenmaßnahme: Sachverhalt].

### 5. Schutz der Befehlsfolgen

5.1 Befehlsfolgen für Plattform, Sensor, Datenübermittlung und unmittelbare Datenverbreitung werden ausschließlich in [gesicherte Umgebung und Standort] hergestellt.

5.2 Rollen für Erstellung, Prüfung, Freigabe, Signierung, Übertragung und Abbruch sind personell getrennt. Jede Befehlsfolge trägt [Kennung, Version, Freigaben, Zeit und Zielsystem].

5.3 Das Verfahren gegen Veränderung durch Dritte ist [Bezeichnung und BSI-Prüfstatus]. Schlüssel werden nach [Schlüsselhierarchie, Hardware-Sicherheitsmodul, Rotation, Sperre und Notfallwiederherstellung] verwaltet.

### 6. Schutz der Datenübermittlung

6.1 Datenwege vom Orbitalsystem zum Bodensegment, zwischen Bodenstandorten und zum zugelassenen Datenanbieter sind in Anlage 5 vollständig kartiert.

6.2 Das Verfahren gegen unbefugte Kenntnisnahme ist [Bezeichnung und BSI-Prüfstatus]. Klartext entsteht ausschließlich in [Standorte und Systeme]; Export, Cache, Sicherung und Löschung sind technisch kontrolliert.

### 7. Zutritt, Zugriff und Sicherheitsüberprüfung

7.1 Anlagen für Kommando, Empfang, Verarbeitung und Speicherung liegen in [Betriebsräume]. Physischer Zutritt erfordert [Identität, Berechtigung, Protokollierung und Begleitung].

7.2 Logische Zugriffe folgen [Rollenmodell, Mehrfaktor-Authentisierung, privilegierte Konten, Vier-Augen-Freigabe und Protokollüberwachung].

7.3 Die nach § 4 Abs. 2 SatDSiG sicherheitszuüberprüfenden Personen sind in Anlage 6 mit Rolle, Zugriff und Verfahrensstand aufgeführt. Zugriff wird erst nach erforderlicher Freigabe erteilt.

### 8. Dokumentation und Anzeigen

8.1 Befehlsfolgen, Sensorsteuerung, Übermittlungssteuerung, Verschlüsselung, Schlüssel, Zeitpunkt und Übertragungsweg werden mindestens fünf Jahre nach Ausführung der jeweiligen Befehlsfolge aufbewahrt.

8.2 Änderungen registerrelevanter Tatsachen, Gesellschafter oder Beteiligungen, Verdachtsmomente fremder Kommandierung und Änderungen der Schutzmaßnahmen werden unverzüglich schriftlich oder elektronisch angezeigt.

8.3 Daten werden nur an die in Anlage 7 bezeichneten und nach § 11 SatDSiG zugelassenen Personen übermittelt; Änderungen werden unverzüglich angezeigt.

### 9. BSI-Beteiligung und Inbetriebnahme

9.1 Das Bundesamt für Sicherheit in der Informationstechnik (BSI) wurde am [Datum] beteiligt. Prüfgegenstand, offene Nachweise und Zieltermine ergeben sich aus Anlage 8.

9.2 Der Regelbetrieb beginnt erst nach Genehmigung, erforderlicher BSI-Eignungserklärung, Sicherheitsüberprüfung und technischer Abnahme.

Mit freundlichen Grüßen

[Name, Funktion und Unterschrift]

## Anlagen

### Anlage 1 — Genehmigungskonfiguration

1.1 [Satellit, Sensor, Betriebsmodi, Standorte, Datenpfade und Versionsstände].

### Anlage 2 — Rollen und Verträge

2.1 [Betreiber, Eigentümer, Hersteller, Dienstleister und Datenanbieter].

### Anlage 3 — Hochwertigkeitsbewertung

3.1 [SatDSiV-Parameter, Berechnung und Betriebsmodi].

### Anlage 4 — Zuverlässigkeit

4.1 [Register, Organigramm, Verantwortliche, Lebensläufe und Erklärungen].

### Anlage 5 — Sicherheitsarchitektur

5.1 [Kommando, Datenübermittlung, Kryptografie, Schlüssel und Netzplan].

### Anlage 6 — Personal

6.1 [Zugriffsrollen und Sicherheitsüberprüfungsstatus].

### Anlage 7 — Datenempfänger

7.1 [Zugelassene Datenanbieter, Zulassungsnachweis und Übermittlungsweg].

### Anlage 8 — BSI-Prüfung und Inbetriebnahme

8.1 [Prüfplan, Nachweise, Abnahme, offene Punkte und Startfreigabe].

---

Lizenz: Apache-2.0 OR MIT.
