# Aktenstück 09 — Cyber-Lösegeld und Sanktionsrecht (OFAC)

**Bezug:** D&O-Deckungsklage LG Köln 26 O 144/26; Ablehnungsgrund "OFAC-Sanktions-Klausel"  
**Ereignis:** Ransomware-Angriff auf Vogelweide+Co Demenz-WG GmbH, November 2022

---

## I. Sachverhaltsdarstellung Ransomware-Angriff

Am **14. November 2022** wurde das IT-System der Vogelweide+Co Demenz-WG GmbH Opfer eines Ransomware-Angriffs. Die Angreifer verschlüsselten sämtliche digitalen Patientenakten (12 Bewohnerpersonalakten, Pflegeplanungsdaten, Medikamentenpläne) mittels der Schadsoftware "LockBit 3.0". Im Erpresserschreiben (in englischer Sprache) forderten die Angreifer die Zahlung von 0,82 BTC (Marktwert ca. 18.000 EUR zum Tatzeitpunkt) an eine Bitcoin-Adresse bc1q...z2vf (nachfolgend "Empfänger-Wallet") binnen 72 Stunden, andernfalls drohte die Veröffentlichung der Patientendaten im Darknet.

### Entscheidungssituation

Frau Vogelweide stand vor folgender Abwägungssituation:

- **Keine Datensicherung** vorhanden (IT-Einrichtung lag bei einem lokalen Dienstleister, der keine regelmäßigen Backups konfiguriert hatte).
- **Sofortige Patientengefährdung**: Ohne Zugriff auf Medikamentenpläne und Pflegeplanungen war der Betrieb der Wohngemeinschaft unmittelbar gefährdet; 12 Demenzkranke waren betroffen.
- **Datenschutzrechtliche Pflicht**: Eine Veröffentlichung der Patientendaten hätte schwere Verstöße gegen Art. 9 DSGVO (besondere Kategorien, Gesundheitsdaten) und § 203 StGB dargestellt.
- **Keine Erreichbarkeit des Gesellschafters**: Die Muttergesellschaft (St.-Antonius-Heim GmbH) war an diesem Sonntagabend nicht erreichbar.

Frau Vogelweide entschied sich zur Lösegeldszahlung als ultima ratio zum Schutz der Bewohner und zur Abwendung der Datenschutzverletzung.

---

## II. OFAC-SDN-Listen-Listung der Empfänger-Wallet

Die OFAC (Office of Foreign Assets Control, US-Finanzministerium) führt die SDN-Liste (Specially Designated Nationals and Blocked Persons). Im März 2023 — also **4 Monate nach** der Lösegeldszahlung — listete die OFAC die Bitcoin-Adresse bc1q...z2vf als mit der Gruppe "LockBit Cybercrime Organization" assoziiert. Der Eintrag erfolgte rückwirkend im Sinne der Transaktionsdatenbankauswertung.

**Wichtig**: Zum Zeitpunkt der Zahlung (November 2022) war die Wallet-Adresse **nicht auf der SDN-Liste**. Die nachträgliche Listung kann keine ex-ante-Sanktionspflichten begründen.

---

## III. Rechtliche Analyse: OFAC-Sanktionsklausel in deutschen Versicherungsverträgen

### a) Anwendbarkeit US-amerikanischen Sanktionsrechts

US-Sanktionsregeln der OFAC haben extraterritoriale Wirkung primär für US-Personen und Transaktionen in USD. Frau Vogelweide ist eine deutsche Staatsangehörige, die Demenz-WG ist eine deutsche GmbH, die Transaktion erfolgte in Kryptowährung ohne USD-Clearing. Eine direkte OFAC-Bindung besteht daher nicht.

Die EU verfügt über eigene Sanktionslisten (Consolidated Sanctions List der EU), auf der "LockBit" zum Zeitpunkt November 2022 **nicht gelistet** war.

### b) Auslegung der AVB-Sanktionsklausel

Die Sanktionsklausel in § 12 Abs. 5 DMO-AVB 2018 der ManagerSchutz AG lautet (auszugsweise): *"Kein Versicherungsschutz besteht, soweit die Erbringung der Versicherungsleistung gegen Sanktionen, Embargos oder sonstige wirtschaftliche Beschränkungen nach deutschem, europäischem oder UN-Recht verstößt."*

Entscheidend ist der Bezugspunkt: Die Klausel richtet sich gegen die **Versicherungsleistung** selbst — also die Zahlung der Deckungssumme durch den Versicherer. Nicht erfasst ist die zugrundeliegende Schadensentstehung. Die D&O-Versicherung erstattet hier die Verteidigungs- und Haftungskosten von Frau Vogelweide gegenüber der Muttergesellschaft. Diese Deckungsleistung berührt keine sanktionierten Parteien.

### c) Zeitpunkt und Kenntnis

Selbst wenn die Sanktionsklausel grundsätzlich anwendbar wäre: Eine Sanktionspflicht kann nur für Transaktionen gelten, bei denen die SDN-Listung zum Zeitpunkt der Transaktion bekannt war oder sein musste (Sorgfaltspflicht-Maßstab). Im November 2022 war die Wallet nicht gelistet; eine Kenntnis oder fahrlässige Unkenntnis von Frau Vogelweide ist ausgeschlossen.

---

## IV. Strafrechtliche Aspekte

### § 89c StGB (Terrorismusfinanzierung)

Eine Strafbarkeit nach § 89c StGB setzt voraus, dass die Zahlung einer Organisation zugute kommt, die terroristische Zwecke verfolgt. Cyberkriminelle Ransomware-Gruppen fallen nicht per se unter den strafrechtlichen Terrorismusbegriff (§ 129a StGB). Die Lösegeldszahlung zur Abwendung einer Notlage ist nach § 34 StGB (rechtfertigender Notstand) gerechtfertigt.

### Geldwäsche (§ 261 StGB)

Da die Lösegeldtransaktion als erzwungene Zahlung zur Notlagenabwendung erfolgte, fehlt es am Vorsatzelement einer Geldwäschehandlung.

---

## V. Ergebnis

Die OFAC-Sanktionsklausel greift im vorliegenden Fall nicht. Der Deckungsanspruch von Frau Vogelweide gegenüber der ManagerSchutz AG bleibt bestehen. Vgl. Klageschrift D&O (Aktenstück, docx/02).

