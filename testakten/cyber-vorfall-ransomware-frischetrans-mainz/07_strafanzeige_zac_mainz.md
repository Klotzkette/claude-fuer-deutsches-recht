# Strafanzeige bei der ZAC Mainz — Ransomware-Angriff

**Aktenstück:** 07  
**Datum:** 07.05.2026  
**Aktenzeichen Strafverfolgung:** 421 UJs 6611/26  
**Erstattet durch:** RA Lukas Drosten für Frischetrans Mittelrhein GmbH  
**Adressat:** Kriminalpolizei Mainz, Zentrale Ansprechstelle Cybercrime (ZAC), Valenciaplatz 1, 55118 Mainz

---

## Strafanzeige

**mit dem Antrag auf Strafverfolgung**

---

Kanzlei Drosten & Pekonkur  
Schillerstraße 14  
55116 Mainz  
Telefon: +49 6131 2240-0  
l.drosten@drosten-pekonkur.de

Mainz, den 07.05.2026

An  
Kriminalpolizei Mainz  
Zentrale Ansprechstelle Cybercrime (ZAC)  
Valenciaplatz 1  
55118 Mainz

---

### Strafanzeige gegen Unbekannt

**wegen:**  
- Ausspähens von Daten (§ 202a StGB)  
- Abfangens von Daten (§ 202b StGB)  
- Datenveränderung (§ 303a StGB)  
- Computersabotage (§ 303b StGB)  
- Erpressung (§ 253 StGB)  
- Computerbetrugs (§ 263a StGB)  
- Bandenmäßiger Erpressung (§ 253 Abs. 4 StGB i.V.m. § 260 StGB)

---

### I. Vollmacht und Vertretung

Ich zeige an, dass ich die Frischetrans Mittelrhein GmbH, Binger Straße 142, 55131 Mainz, vertreten durch Geschäftsführerin Theresia Wallbruck, anwaltlich vertrete. Eine Vollmacht liegt dieser Anzeige bei.

### II. Sachverhalt

In der Nacht vom 05. auf den 06.05.2026 wurde das Unternehmens-IT-System der Frischetrans Mittelrhein GmbH Opfer eines schwerwiegenden Ransomware-Angriffs. Die Tätergruppe agiert unter dem Namen „AkiraNext".

**1. Unbefugter Zugang und Datenabfluss**

Netzwerk-Logs belegen, dass die Angreifer bereits ab dem 04.05.2026, ca. 22:44 Uhr, unbefugt Zugang zu den Systemen der Anzeigeerstatterin erlangt hatten. Während der Verweildauer von ca. 29,5 Stunden führten die Täter eine laterale Bewegung durch das interne Netzwerk durch und exfiltrierten ca. 2,1 TB an Daten.

Der initiale Zugang erfolgte vermutlich über die ungepatchte SAP NetWeaver-Schwachstelle CVE-2026-0712. Eine forensische Untersuchung durch die CyberForensik RheinMain GmbH ist eingeleitet; die vollständigen forensischen Ergebnisse werden nachgereicht.

Die exfiltrierten Daten umfassen:
- Kundenstammdaten von 18 Geschäftskunden (Vertrags-, Konditions-, Kontaktdaten)
- Personalakten von 280 Mitarbeiterinnen und Mitarbeitern (inkl. Bankverbindungen, SV-Nummern)
- Gesundheitsdaten aus BEM-Verfahren von 38 Mitarbeiterinnen und Mitarbeitern (besonders sensible Daten)
- Finanzdaten (Buchungsdaten Q1/2026)
- Vertragsdaten und interne Kommunikation

**2. Ransomware-Angriff und Verschlüsselung**

Am 06.05.2026 um ca. 04:17–04:31 Uhr aktivierten die Angreifer die Ransomware „AkiraNext". Folgende Systeme wurden vollständig verschlüsselt:

- SAP S/4HANA Applikationsserver (2 Systeme: FT-ERP-PROD-01, FT-ERP-PROD-02)
- Datenbankserver (FT-DB-01)
- Fileserver (3 Systeme)
- Telematik-Gateway

Auf allen betroffenen Systemen wurde ein Erpressungsschreiben hinterlassen (als Desktop-Hintergrund und als Datei `!!! AKIRA_NEXT_README.txt`).

**3. Erpressung**

Die Tätergruppe fordert die Zahlung von **1.450.000 USD in Monero** (Kryptowährung) innerhalb von 7 Tagen (bis 13.05.2026, 23:59 Uhr UTC). Bei Nichtzahlung drohen die Täter mit der Veröffentlichung der abgeflossenen Daten auf ihrer Leakseite im Tor-Netzwerk.

Die vollständigen Angaben zu Wallet-Adresse und Onion-URL des Erpressungsschreibens werden als Anlage 3 (Erpressungsschreiben) im Original beigefügt.

**4. Wirtschaftlicher Schaden**

Der Gesamtschaden der Anzeigeerstatterin beläuft sich nach vorläufiger Schätzung auf:

| Schadensposition | Betrag (geschätzt) |
|---|---|
| Wiederherstellungskosten IT | ca. 180.000–220.000 EUR |
| Betriebsausfall Logistik (7 Tage) | ca. 320.000–450.000 EUR |
| Forensikkosten | ca. 45.000–65.000 EUR |
| Rechts- und Beratungskosten | ca. 80.000–120.000 EUR |
| DSGVO-Bußgeldrisiko | bis 500.000 EUR (zu prüfen) |
| Reputationsschaden | nicht bezifferbar |
| **Gesamt (vorläufig)** | **ca. 625.000–1.355.000 EUR** |

### III. Straftaten

**§ 202a StGB (Ausspähen von Daten):**  
Die Täter erlangten unter Überwindung von Zugangssicherungen (Firewalls, Authentifizierungssysteme) unbefugt Zugang zu den gesicherten Daten der Anzeigeerstatterin. Der Tatbestand des § 202a Abs. 1 StGB ist erfüllt.

**§ 202b StGB (Abfangen von Daten):**  
Durch laterale Bewegungen im Netzwerk wurden Datenpakete aus internen Übertragungen abgefangen und exfiltriert. Tatbestand § 202b StGB ist erfüllt.

**§ 303a StGB (Datenveränderung):**  
Durch die Verschlüsselung wurden die Daten rechtswidrig unbrauchbar gemacht (§ 303a Abs. 1 StGB). Es liegt ein schwerer Fall vor (§ 303a Abs. 2 i.V.m. § 303b Abs. 3 StGB), da der wirtschaftliche Schaden erheblich ist.

**§ 303b StGB (Computersabotage):**  
Der Angriff auf das ERP-System und die Telematik-Infrastruktur eines Unternehmens der Lebensmittelversorgungskette stellt eine Computersabotage i.S.d. § 303b Abs. 1 Nr. 2 StGB dar. Es handelt sich möglicherweise um einen Angriff auf eine Einrichtung von erheblicher Bedeutung (§ 303b Abs. 4 StGB).

**§ 253 StGB (Erpressung):**  
Die Täter nötigten die Anzeigeerstatterin durch die Androhung der Veröffentlichung gestohlener Daten und durch die Verweigerung der Entschlüsselung zur Zahlung eines erheblichen Geldbetrages. Die Drohung ist ernstgemeint und geeignet, eine Entschlussfassung zu beeinflussen.

**§ 263a StGB (Computerbetrug):**  
Durch unbefugtes Einwirken auf Datenverarbeitungsabläufe beabsichtigten die Täter, sich rechtswidrige Vermögensvorteile zu verschaffen.

### IV. Beweismittel

Als Anlage werden beigefügt:

1. Vollmacht der Frischetrans Mittelrhein GmbH
2. Netzwerk-Logs mit Nachweis des Datenabflusses (Forensikbericht-Auszug, vorläufig)
3. Erpressungsschreiben (Original inkl. Wallet-Adresse und Onion-URL — vertraulich)
4. Screenshot-Dokumentation der verschlüsselten Systeme
5. Hash-Werte der Ransomware-Datei (ermittelt durch InsoTec Systems GmbH)
6. Vorläufiger forensischer Erstbericht (CyberForensik RheinMain GmbH)

Ergänzende Beweismittel (vollständiger forensischer Abschlussbericht, Server-Logs) werden nachgereicht.

### V. Anträge

1. Es wird beantragt, wegen der vorgenannten Straftaten gegen unbekannte Täter zu ermitteln.
2. Es wird beantragt, die vorliegenden Beweismittel zu sichern und ggf. eine internationale Rechtshilfeanfrage an die zuständigen Behörden (Europol EC3, FBI Cyber Division) zu richten.
3. Es wird beantragt, die Daten der Erpresser-Infrastruktur (Tor-Adressen, Monero-Wallet) mit internationalen Datenbanken abzugleichen.
4. Es wird beantragt, die Anzeigeerstatterin über den Fortgang der Ermittlungen zu informieren (§ 406e StPO analog für Körperschaften).

### VI. Hinweis

Eine Lösegeldzahlung erfolgt nicht und ist auch nicht geplant. Kryptowährungstransaktionen wurden seitens der Anzeigeerstatterin nicht vorgenommen.

Die BSI Außenstelle Frankfurt sowie der LfDI Rheinland-Pfalz wurden ebenfalls über den Vorfall informiert. Eine Abstimmung mit den Ermittlungsbehörden bezüglich der laufenden forensischen Untersuchung ist ausdrücklich erwünscht.

---

**Mainz, den 07.05.2026**

RA Lukas Drosten  
Kanzlei Drosten & Pekonkur

*Für die Anzeigeerstatterin:*  
Frischetrans Mittelrhein GmbH  
gez. Theresia Wallbruck (Geschäftsführerin)

---

*Aktenzeichen vergeben durch ZAC Mainz: 421 UJs 6611/26*  
*Sachbearbeiterin: KHK'in Sabine Erhart, ZAC Mainz*
