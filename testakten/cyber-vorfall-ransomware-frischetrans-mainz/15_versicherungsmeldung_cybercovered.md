# Versicherungsmeldung an CyberCovered AG

**Aktenstück:** 15  
**Datum der Meldung:** 07.05.2026  
**Schadensnummer:** CC-SCHADEN-2026-FTM-0914  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Versicherer:** CyberCovered AG, Taunusanlage 17, 60325 Frankfurt am Main

---

## 1. Versicherungsvertrag — Eckdaten

| Parameter | Wert |
|---|---|
| Versicherungsnehmerin | Frischetrans Mittelrhein GmbH |
| Policennummer | CC-2024-FTM-8801 |
| Versicherungsart | Cyber-Versicherung (All-Risk) |
| Deckungssumme | 5.000.000 EUR |
| Jahresprämie | 42.800 EUR (netto) |
| Versicherungsbeginn | 01.01.2024 |
| Versicherungsende | 31.12.2026 (Laufzeit 3 Jahre) |
| Makler | Finanz- und Versicherungsbüro Riedel, Mainz |
| Schadenmeldepflicht (Vertragsklausel) | Unverzüglich, max. 72 h nach Kenntnisnahme |

---

## 2. Deckungsumfang der Police (Zusammenfassung)

Die Cyber-Versicherungspolice CC-2024-FTM-8801 der CyberCovered AG deckt (gemäß § 3 der Allgemeinen Versicherungsbedingungen Cyber, AVB-Cyber 2023):

**Erstparteileistungen:**
- Betriebsunterbrechungsschäden (Ertragsausfall durch Systemausfall, bis 72 Stunden Karenzzeit)
- IT-Wiederherstellungskosten (Forensik, Datenwiedherstellung, Systemwiederaufbau)
- Krisenmanagement und PR-Kosten
- Kosten für Benachrichtigung betroffener Personen (Art. 34 DSGVO)
- Erpressungskosten (Lösegeldzahlungen — mit Zustimmungsvorbehalt des Versicherers)
- Anwaltskosten im Zusammenhang mit dem Vorfall

**Drittparteileistungen:**
- Haftpflichtschäden aus Datenschutzverletzungen (DSGVO-Bußgelder bis zur gesetzlichen Grenze)
- Schadensersatzansprüche Dritter aus Datenpannen
- Abwehr von Schadensersatzansprüchen durch Versicherungsdeckung der Anwaltskosten

**Ausschlüsse (wesentliche):**
- Schäden durch Kriegsakte und staatlich gesteuerte Cyberangriffe (War Exclusion)
- Vorsätzlich herbeigeführte Schäden
- Schäden, die bei bekannten ungepatchten Schwachstellen entstehen, die der VN trotz Kenntnis nicht behoben hat (fragliche Anwendung im vorliegenden Fall — zu prüfen!)

---

## 3. Schadensmeldung vom 07.05.2026

**Übermittelt an:** CyberCovered AG, Schadenabteilung Cyber  
**Kanal:** Verschlüsselte E-Mail an schaden-cyber@cybercovered.de + telefonische Erstmeldung  
**Ansprechpartner Versicherer:** Lena Hamann (Schadenmanagerin Cyber, CyberCovered AG)

---

### Inhalt der Schadensmeldung

**Schadenereignis:**  
Ransomware-Angriff (AkiraNext) am 06.05.2026, Entdeckung 04:17 Uhr. Vollständige Verschlüsselung des SAP ERP-Systems und weiterer IT-Infrastruktur sowie Datenabfluss (2,1 TB).

**Vorläufige Schadenspositionen (zum Zeitpunkt der Meldung):**

| Position | Betrag (vorläufig) |
|---|---|
| IT-Forensik und Wiederherstellung | ca. 200.000–270.000 EUR |
| Betriebsunterbrechungsschaden | ca. 350.000–500.000 EUR |
| Kosten Datenschutzmeldungen / DSGVO | ca. 20.000–40.000 EUR |
| Anwaltskosten | ca. 80.000–120.000 EUR |
| PR / Krisenmanagement | ca. 15.000–30.000 EUR |
| **Gesamt (vorläufig)** | **ca. 665.000–960.000 EUR** |

Lösegeld wurde **nicht** gezahlt und ist auch nicht geplant.

**Angabe zum Angriffsverlauf:**  
Initial Access über CVE-2026-0712 (SAP-Schwachstelle). Patch war durch IT-Dienstleister ProcessSpark Cloud AG verspätet eingespielt worden (55 Tage Verzug). Frischetrans selbst hatte keine unmittelbare Kenntnis von der Patchlücke.

---

## 4. Rechtliche Bewertung — Ausschlussklausel ungepatchte Schwachstellen

**Kritischer Punkt:** Viele Cyber-Policen enthalten Klauseln, die Schäden ausschließen, die aus bekannten, nicht gepatchten Schwachstellen resultieren.

**Analyse im vorliegenden Fall:**

1. Die Frischetrans selbst hatte **keine direkte Kenntnis** von CVE-2026-0712 und dem Patch-Rückstand. Die Mandantin hatte die Patchpflicht an ProcessSpark Cloud AG ausgelagert.

2. Die Ausschlussklausel greift nach gefestigter Auffassung in der Versicherungsrechtsliteratur nicht, wenn der VN die Behebung der Schwachstelle vertraglich an einen Dritten ausgelagert hatte und der Dritte pflichtwidrig nicht gehandelt hat.

3. Arglistige oder grob fahrlässige Kenntnis der Mandantin ist nicht gegeben.

**Empfehlung:** Sollte CyberCovered AG die Leistung unter Berufung auf diese Klausel ablehnen oder kürzen, ist der Einwand zu bestreiten und ggf. gerichtlich anzugreifen. Parallel wird ProcessSpark in Regress genommen (Aktenstück 10).

---

## 5. Weiterer Prozess mit der Versicherung

| Schritt | Datum | Status |
|---|---|---|
| Erstmeldung | 07.05.2026 | Erledigt |
| Benennung externer Forensiker (Vorgabe des Versicherers) | 08.05.2026 | Erledigt (CyberForensik RheinMain bestätigt) |
| Vorlage Forensikzwischenbericht | 15.05.2026 | Offen |
| Vorlage vollständiger Schadensdokumentation | 31.05.2026 | Offen |
| Schadenregulierung (Erstabschlagszahlung) | ca. 01.06.2026 | Offen |
| Abschließende Regulierung | ca. 30.06.2026 | Offen |

---

## 6. Wichtiger Hinweis zu Lösegeldzahlungen

Die Police CC-2024-FTM-8801 sieht vor, dass Lösegeldzahlungen nur mit vorheriger Zustimmung der CyberCovered AG erstattet werden. Da keine Zahlung geleistet wurde, ist dieser Punkt irrelevant. Die Entscheidung, kein Lösegeld zu zahlen, entspricht auch der Empfehlung der CyberCovered AG (Schadenmanagerin Hamann bestätigte telefonisch, dass CyberCovered bei Ransomware grundsätzlich auf Zahlung verzichtet und forensische Wiederherstellung bevorzugt).
