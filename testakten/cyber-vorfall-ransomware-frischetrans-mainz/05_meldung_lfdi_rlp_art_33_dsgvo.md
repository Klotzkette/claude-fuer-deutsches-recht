# Meldung an den LfDI Rheinland-Pfalz gemäß Art. 33 DSGVO

**Aktenstück:** 05  
**Datum der Übermittlung:** 08.05.2026, 22:45 Uhr  
**Übermittlungsweg:** Online-Meldeportal LfDI RLP (https://www.datenschutz.rlp.de/meldung)  
**Referenznummer LfDI:** LfDI-RLP-2026-0508-4419  
**Bearbeiter:** RA Lukas Drosten für Frischetrans Mittelrhein GmbH

---

## Meldeformular — Art. 33 DSGVO

**An:**  
Der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Rheinland-Pfalz (LfDI RLP)  
Hintere Bleiche 34  
55116 Mainz

**Meldung einer Verletzung des Schutzes personenbezogener Daten**  
gemäß Art. 33 Abs. 3 DSGVO

---

### Abschnitt 1: Angaben zum Verantwortlichen

**Name des Verantwortlichen:**  
Frischetrans Mittelrhein GmbH

**Vertreten durch:**  
Theresia Wallbruck (Geschäftsführerin)

**Anschrift:**  
Binger Straße 142, 55131 Mainz

**Handelsregister:**  
HRB 44821, Amtsgericht Mainz

**Kontakt für Rückfragen:**  
RA Lukas Drosten, Kanzlei Drosten & Pekonkur  
Schillerstraße 14, 55116 Mainz  
Telefon: +49 6131 2240-0  
E-Mail: l.drosten@drosten-pekonkur.de

**Datenschutzbeauftragter (extern):**  
Markus Feilke, Dipl.-Inform. (Datenschutzkanzlei Rhein-Main)  
E-Mail: m.feilke@datenschutz-rhein-main.de  
Telefon: +49 6131 9944-11

---

### Abschnitt 2: Art der Verletzung des Schutzes personenbezogener Daten

**Art der Verletzung (§ Art. 4 Nr. 12 DSGVO):**  
☑ Verlust der Verfügbarkeit  
☑ Verlust der Vertraulichkeit  
☑ Verlust der Integrität  

**Beschreibung des Vorfalls:**  
In der Nacht vom 05. auf den 06.05.2026 wurde das IT-System der Frischetrans Mittelrhein GmbH Opfer eines Ransomware-Angriffs durch die kriminelle Gruppe „AkiraNext". Das ERP-System (SAP S/4HANA, on-premises, Serverstandort Mainz) sowie weitere interne IT-Systeme wurden vollständig verschlüsselt.

Forensische Analyse ergab, dass die Angreifer bereits ab dem 04.05.2026 (ca. 22:44 Uhr) Zugang zu den Systemen hatten und vor der Aktivierung der Ransomware ca. 2,1 TB an Unternehmensdaten aus dem internen Netzwerk exfiltriert haben. Der initiale Zugang erfolgte über die ungepatchte SAP-Schwachstelle CVE-2026-0712.

**Zeitpunkt der Entdeckung:**  
06.05.2026, 04:17 Uhr (Detektion durch SOC-System der InsoTec Systems GmbH, Frankfurt)

**Zeitpunkt der Kenntnisnahme durch den Verantwortlichen:**  
06.05.2026, 04:52 Uhr (Benachrichtigung von Theresia Wallbruck, GF)

---

### Abschnitt 3: Betroffene Personen und Kategorien

**Kategorien betroffener Personen:**

1. **Kunden (Unternehmen):**  
   18 Geschäftskunden der Frischetrans Mittelrhein GmbH. Abgeflossene Daten umfassen Kundenstammdaten (Firmendaten, Ansprechpartner, Vertrags- und Lieferdetails, Bankverbindungen für die Abrechnung).

2. **Mitarbeiterinnen und Mitarbeiter:**  
   280 aktive Beschäftigte, davon 38 Mitarbeiter mit besonders sensiblen Gesundheitsdaten aus laufenden oder abgeschlossenen Betrieblichen Eingliederungsmanagement-Verfahren (BEM). Bei diesen 38 Personen sind Diagnosen, Therapieverläufe und ärztliche Bescheinigungen in den Personalakten enthalten.

   Darüber hinaus: Personalstammdaten (Name, Adresse, Geburtsdatum, Sozialversicherungsnummer, Bankverbindung, Lohnabrechnung) aller 280 Mitarbeiter.

**Ungefähre Zahl betroffener Personen:**  
298 natürliche Personen (280 Mitarbeiter + ca. 18 Kontaktpersonen bei Firmenkunden; die Kunden selbst sind juristische Personen und fallen nicht unmittelbar unter Art. 33 DSGVO).

**Besondere Kategorien (Art. 9 DSGVO):**  
☑ Gesundheitsdaten (BEM-Verfahren, 38 Mitarbeiter)  

---

### Abschnitt 4: Voraussichtliche Folgen der Verletzung

Die Verletzung des Schutzes personenbezogener Daten hat voraussichtlich folgende Folgen:

1. **Identitätsdiebstahl und Betrug:** Durch den Abfluss von Personalstammdaten inkl. Bankverbindungen besteht für die betroffenen Mitarbeiter ein erhöhtes Risiko von Kontomissbrauch und Identitätsdiebstahl.

2. **Bloßstellung und Diskriminierung:** Die abgeflossenen BEM-Gesundheitsdaten (Diagnosen, Therapieverläufe) können im Falle einer Veröffentlichung durch die Tätergruppe zu erheblichen Nachteilen für die betroffenen 38 Mitarbeiter führen (soziale Stigmatisierung, potenzielle Auswirkungen auf Versicherbarkeit oder Kreditwürdigkeit).

3. **Geschäftliche Nachteile für Kunden:** Vertrauliche Vertrags- und Konditionsinformationen können von Wettbewerbern genutzt werden.

4. **Reputationsschaden:** Veröffentlichung der Daten auf Leakseiten der Tätergruppe droht.

---

### Abschnitt 5: Getroffene und geplante Maßnahmen

**Bereits getroffene Maßnahmen:**

- Sofortige Abschottung aller betroffenen Systeme (Network Kill, 06.05.2026, 05:35 Uhr)
- Beauftragung forensischer Spezialisten (CyberForensik RheinMain GmbH)
- Strafanzeige bei ZAC Mainz erstattet (07.05.2026, AZ: 421 UJs 6611/26)
- Meldung an BSI Außenstelle Frankfurt (07.05.2026)
- Einleitung der Wiederherstellung aus Backup-Systemen
- Mandatierung von RA Lukas Drosten (Kanzlei Drosten & Pekonkur)
- Meldung an Cyber-Versicherer CyberCovered AG (07.05.2026)

**Geplante Maßnahmen:**

- Benachrichtigung der betroffenen Mitarbeiter gemäß Art. 34 DSGVO (geplant: 11.05.2026)
- Einleitung einer Datenschutz-Folgenabschätzung (DSFA) für die Verarbeitung von BEM-Gesundheitsdaten (Art. 35 DSGVO)
- Vollständige forensische Aufarbeitung des Angriffsverlaufs
- Implementierung eines überarbeiteten Patch-Management-Prozesses
- Überprüfung und Erneuerung der Firewall-Konfiguration
- Ggf. Schadensersatzforderungen gegen IT-Dienstleister

---

### Abschnitt 6: Angaben zum Datenschutzbeauftragten

Externer Datenschutzbeauftragter ist vorhanden (siehe Abschnitt 1).

---

### Abschnitt 7: Sonstige Hinweise

Diese Meldung erfolgt auf Basis der zum Zeitpunkt der Übermittlung (08.05.2026, 22:45 Uhr) vorliegenden Erkenntnisse. Die forensische Untersuchung ist noch nicht abgeschlossen. Eine Ergänzungsmeldung mit vollständigen Befunden des forensischen Abschlussberichts wird innerhalb von 14 Tagen (bis 22.05.2026) eingereicht.

Das Unternehmen hat sich bei der Vorbereitung dieser Meldung anwaltlicher Beratung bedient (RA Lukas Drosten, Fachanwalt für IT-Recht).

---

### Rechtsgrundlagen

- Art. 33 Abs. 1 DSGVO: Meldepflicht des Verantwortlichen an Aufsichtsbehörde binnen 72 Stunden  
- Art. 33 Abs. 3 DSGVO: Inhaltliche Anforderungen der Meldung  
- Art. 33 Abs. 4 DSGVO: Gestuftes Meldesystem bei unvollständigen Informationen  
- Erwägungsgrund 87 DSGVO: Unverzüglichkeit der Meldung  
- § 42 BDSG: Strafvorschriften BDSG (ergänzend)

Zur Rechtslage bei gestuften Meldungen im Ransomware-Kontext vgl. auch Orientierungshilfe der Datenschutzkonferenz (DSK) „Ransomware: Meldung und Benachrichtigung" (Stand 2023/2024).

---

**Mainz, den 08.05.2026**

RA Lukas Drosten  
Kanzlei Drosten & Pekonkur  
(handelnd für und im Auftrag der Frischetrans Mittelrhein GmbH)

*[Elektronisch signiert und über das LfDI-Meldeportal übermittelt — Empfangsbestätigung Ref. LfDI-RLP-2026-0508-4419 liegt vor]*
