# Dual-Use-Prüfung: CNC-Steuermodul GX-900 – Vollständige Analyse

**Dokumenttyp:** Exportkontroll-Prüfbericht (Internes Vermerk)  
**Aktenzeichen:** GM-EK-2026-041-DU  
**Erstellt:** 15. April 2026  
**Verfasser:** Dipl.-Ing. Rainer Hofstädter, Exportkontrollbeauftragter  
**Geprüft:** Dr. Sabine Brennecke, Syndikusrechtsanwältin  
**Status:** Abgeschlossen – Genehmigungsbedürftigkeit festgestellt

---

## 1. Prüfungsanlass und Sachverhalt

Die Globalmaschinen GmbH beabsichtigt, das CNC-Steuermodul GX-900 (Artikelnummer 8000-GX900-EU) an die Turan Industrial Trading Ltd., Istanbul/Türkei, zu liefern. Der türkische Händler hat schriftlich erklärt, die Ware an einen Endkunden in Kasachstan weiterzuverkaufen. Die endgültige Endverwendung ist mit "zivile Maschinenwartung" angegeben. Aufgrund der technischen Spezifikationen (9-Achsen-Interpolation, Positioniergenauigkeit ≤ 1 μm), der Drittstaatenweiterleitung sowie laufender BAFA-Anfragen hat die Exportkontrollabteilung eine vollständige Dual-Use-Prüfung initiiert.

Rechtliche Grundlage: **Verordnung (EU) 2021/821** (Neufassung Dual-Use-Verordnung), in Kraft getreten 09.09.2021, sowie das **Außenwirtschaftsgesetz (AWG)** und die **Außenwirtschaftsverordnung (AWV)**.

---

## 2. Güterlistenprüfung nach Anhang I EU 2021/821

### 2.1 Kategorie 2 – Materialbearbeitung

#### Position 2B001 – Werkzeugmaschinen und numerische Steuerungen

**Wortlaut (auszugsweise):**
> "2B001.b Numerische Steuerungen für Werkzeugmaschinen, die zur Steuerung von 2 oder mehr simultanen, interpolierend gesteuerten Achsen ausgelegt sind, die in eine Werkzeugmaschine integriert werden können, mit einer Linearpositioniergenauigkeit von weniger als 6 μm..."

**Merkmalsvergleich:**

| Kriterium | Schwellenwert (2B001) | GX-900 | Erfüllt? |
|---|---|---|---|
| Simultane interpolierende Achsen | ≥ 2 (Basistatbestand) / > 5 (erhöhte Kontrolle) | 9 Achsen | **Ja** |
| Positioniergenauigkeit | < 6 μm | ≤ 1 μm | **Ja** |
| Integration in Werkzeugmaschine | Ja | Ja (bestimmungsgemäß) | **Ja** |
| Ausnahme (Special Industrial Equipment) | Nein | entfällt | — |

**Ergebnis 2B001:** Das GX-900 unterfällt **2B001.b** der EU-Dual-Use-Güterliste. Es handelt sich um ein listenpflichtiges Gut.

#### Position 2D001 – Softwarebezug

Software zur Entwicklung oder Produktion von Waren nach 2B001 – hier nicht einschlägig, da kein Softwareexport geplant, sondern Hardwareexport mit integrierter Betriebssoftware (mitgelieferte Firmware gilt als Bestandteil der Ware).

#### Position 2E001 – Technologiebezug

Technologie für die Entwicklung oder Herstellung von Waren nach 2B001 – nicht einschlägig, kein Technologietransfer geplant.

---

### 2.2 Kategorie 5 Teil 2 – Informationssicherheit (Kryptographie)

Das GX-900 enthält einen Hardware Security Module (HSM) Atmel ATECC608A mit AES-256, ECC-384 und SHA-384.

**Position 5A002.a:** Systeme und Ausrüstungen zur "Sicherung von Informationen" mittels kryptographischer Methoden.

**Cryptography Note (CN, Anmerkung 3 zu Kategorie 5 Teil 2):**

Die CN nimmt Waren aus dem Kontrollbereich heraus, die folgende Bedingungen erfüllen:
1. allgemein verfügbar (im Handel erhältlich, massenmarktfähig)
2. kryptographische Funktionalität kann vom Nutzer nicht einfach verändert werden
3. entwickelt für einen spezifischen, nicht-sicherheitskritischen Anwendungsfall

**Prüfung CN für GX-900-HSM:**

- Der HSM ist im GX-900 fest verdrahtet, nicht nach außen zugänglich und dient ausschließlich der Firmware-Integritätsprüfung und Gerätezertifizierung.
- Eine selektive kryptographische Kontrolle durch den Nutzer ist technisch nicht möglich.
- Die Ware richtet sich an kommerzielle CNC-Anwendungen; eine Dual-Use-Hauptfunktion Kryptographie besteht nicht.

**Ergebnis 5A002:** CN greift. Keine Listenpflicht nach Kategorie 5 Teil 2.

---

### 2.3 Sonstige Kategorien (Schnellprüfung)

| Kategorie | Grund für Prüfung | Ergebnis |
|---|---|---|
| 3A001 (Elektronik) | Prozessorkern US-Ursprung | Kein Treffer: Cortex-A72 unter 3A991 (EAR) / kein EU-Listeneintrag |
| 6 (Sensoren/Laser) | Encoder-Schnittstelle | Kein Treffer: Standardauflösung, keine ITAR-Optik |
| 7 (Luft-/Raumfahrt) | Achssteuerung | Kein Treffer: kein Inertialnavigationsbezug |

---

## 3. ECCN-Vergleich nach US-EAR (15 CFR Part 774, CCL)

Da der Prozessorkern (ARM Cortex-A72, IP-Herkunft USA) US-Exportkontrolle berührt, ist eine parallele ECCN-Einordnung erforderlich.

### 3.1 Warenklassifizierung unter CCL

| ECCN | Beschreibung | Anwendung auf GX-900 | Ergebnis |
|---|---|---|---|
| **2B001** (CCL) | NC-Steuerungen für Werkzeugmaschinen | Übereinstimmende Tatbestandsmerkmale mit EU-Liste | **Treffer wahrscheinlich** |
| **3A991.a.2** | Prozessoren (nicht unter 3A001), US-Ursprung | ARM Cortex-A72 als Commodity | Treffer für Komponente |
| **5A992** | Kryptographiefähige Ausrüstungen (Massenmarkt) | HSM nach CN-Prüfung (EAR: License Exception ENC) | Freigestellt / ENC gilt |
| **EAR99** | Nicht auf CCL | Ausschluss für Gesamtgerät: nicht möglich wegen 2B001-Treffer | Nein |

### 3.2 De-minimis-Berechnung (§ 734.4 EAR)

Für Produkte nicht-amerikanischer Hersteller (Foreign-Made Items) gilt die EAR nicht, wenn der US-Wertanteil (controlled US-origin content) unter **25 %** des Gesamtwarenwerts liegt (Nicht-E:1-Länder, Nicht-Gruppen-D:1-Länder). Für Kasachstan (kein E:1-Land, nicht Gruppe D:5) gilt die 25-%-Schwelle.

**Schätzung US-Wertanteil:**

| Komponente | Schätzwert | US-kontrolliert? |
|---|---|---|
| ARM Cortex-A72 SoC | ca. 85 EUR | Ja (3A991) |
| HSM ATECC608A | ca. 4 EUR | Ja (5A992/ENC) |
| Sonstige Elektronik (EU/Asien) | ca. 620 EUR | Nein |
| Gehäuse, Mechanik (DE) | ca. 180 EUR | Nein |
| **Gesamt** | **ca. 889 EUR** | |
| US-Anteil | ca. 89 EUR | **ca. 10 %** |

**Ergebnis De-minimis:** US-Anteil vorläufig unter 25 % – De-minimis-Ausnahme könnte greifen. Endgültige Kalkulation mit Einkaufspreisen ist durchzuführen und zu dokumentieren.

### 3.3 Foreign Direct Product Rule (FDPR, § 736.2(b)(3) EAR)

Die FDPR kann auch bei geringem US-Wertanteil gelten, wenn die Ware durch bestimmte US-Technologie/Software hergestellt wurde. Die erweiterte FDPR-Regel (seit 2022) erfasst insbesondere Exporte nach Russland und Belarus. Für Kasachstan als Endbestimmungsland gilt die Standard-FDPR; da der Chip nicht nach 3A001 listenpflichtig ist, greift die FDPR nicht eigenständig.

---

## 4. Catch-All-Prüfung (Art. 4 EU 2021/821)

Unabhängig von der Listenpflicht ist zu prüfen, ob die Ware für eine militärische Endverwendung, WMD-Entwicklung oder für verbotene Endverwender bestimmt ist.

### 4.1 Bekannte Risikoindikatoren (Red Flags)

| Indikator | Befund | Bewertung |
|---|---|---|
| Routing über Drittland (TR → KZ) | Dokumentiert (E-Mail Mandant) | **Erhöhtes Risiko** |
| Zahlung über VAE-Entität (Al Noor FZE) | Dokumentiert (AWV-Liste) | **Erhöhtes Risiko** |
| Endkunde in Kasachstan unklar | Keine EUC | **Erhöhtes Risiko** |
| Interne Nachricht "dann halt über Kasachstan" | Dokumentiert (Chat-Protokoll) | **Sehr hohes Risiko** |
| Lizenzwert 125.000 EUR (Vorauszahlung KZ) | Kein vergleichbarer Zivil-Auftrag bekannt | Auffällig |

### 4.2 Rechtliche Konsequenz

Gemäß Art. 4 Abs. 1 EU 2021/821 darf ein Ausführer keine dual-use-fähigen Waren (auch nicht-gelistete) ausführen, wenn er weiß oder Grund zu der Annahme hat, dass die Ware für militärische Endverwendung bestimmt ist. Gemäß Art. 4 Abs. 2 darf er bei Hinweisen auf Umgehung sanktionierter Länder (hier: RU/BY) nicht ohne Genehmigung ausführen.

**Schlussfolgerung:** Die vorliegenden Red Flags begründen eine Catch-All-Pflicht, auch wenn die Endbestimmung formal Kasachstan ist. Die Genehmigungspflicht besteht **kumulativ**:
- Listenpflicht nach 2B001 (Ware)
- Catch-All nach Art. 4 Abs. 2 (Umgehungsverdacht)

---

## 5. Genehmigungserfordernisse und zuständige Behörde

| Rechtsgrundlage | Genehmigungsart | Zuständigkeit |
|---|---|---|
| § 8 AWG i.V.m. Teil I Abschnitt C AWV | Ausfuhrgenehmigung für Dual-Use-Güter | BAFA, Eschborn |
| Art. 3 EU 2021/821 | EU-Ausfuhrgenehmigung | BAFA als nationale Bewilligungsbehörde |
| Art. 12g VO (EU) 833/2014 | No-Re-Export-Klausel RU/BY | Vertragspflicht (keine Behördengenehmigung) |

### 5.1 BAFA-Antrag

Für den Export nach Kasachstan (Drittland, keine EU-Allgemeingenehmigung anwendbar) ist eine **Einzelgenehmigung** zu beantragen. Zuständig: Bundesamt für Wirtschaft und Ausfuhrkontrolle (BAFA), Referat 411 (Industriegüter), Frankfurter Str. 29–35, 65760 Eschborn.

**Antragsunterlagen:**
1. Antrag auf Erteilung einer Ausfuhrgenehmigung (BAFA-Online-Portal ELAN-K2)
2. Technisches Datenblatt (vorl. Produkt-Datenblatt GX-900, Version 3.2)
3. Endverwendungserklärung (End-User Certificate – EUC) des kasachischen Endkunden
4. Handelsrechnung / Kaufvertrag Globalmaschinen–Turan Industrial Trading
5. Ggf. Erklärung zum US-Komponenten-Anteil (De-minimis)

**Bearbeitungszeit:** Erfahrungsgemäß 4–12 Wochen für Industriegüter mit mittlerem Risikoprofil; aufgrund des vorliegenden Red-Flag-Musters ist mit intensivierter Prüfung und ggf. Rückfragen zu rechnen.

---

## 6. Empfehlungen und Handlungsplan

| Priorität | Maßnahme | Termin | Verantwortlich |
|---|---|---|---|
| 1 (sofort) | Lieferstopp bis Genehmigungserteilung | Sofort | Vertrieb / Exportkontrolle |
| 1 (sofort) | Legal Hold für alle relevanten Kommunikation | Sofort | Syndikusrechtsanwältin |
| 2 | EUC vom kasachischen Endkunden einholen | 30.04.2026 | Vertrieb |
| 2 | BAFA-Antrag stellen (ELAN-K2) | 07.05.2026 | Exportkontrollabteilung |
| 3 | US-Lieferant: ECCN-Bestätigungsschreiben anfordern | 07.05.2026 | Einkauf |
| 3 | De-minimis-Kalkulation (Endversion) | 05.05.2026 | Controlling |
| 4 | Vertragsklausel Art. 12g VO 833/2014 in Händlervertrag aufnehmen | 15.05.2026 | Rechtsabteilung |

---

## 7. Ergebnis

Das CNC-Steuermodul GX-900 ist nach der EU-Dual-Use-Verordnung (EU) 2021/821 unter **Position 2B001.b** listenpflichtig. Ein Export nach Kasachstan bedarf einer Einzelgenehmigung des BAFA. Zusätzlich löst die dokumentierte Red-Flag-Konstellation (Drittstaatenrouting, unklarer Endkunde, interner Chat) eine Catch-All-Genehmigungspflicht nach Art. 4 EU 2021/821 aus. Ein Export ohne Genehmigung erfüllt den Tatbestand des § 17 AWG (Strafvorschrift) und kann zu Freiheitsstrafe bis zu 15 Jahren führen.

**Das Technikteam hat die Dual-Use-Relevanz ursprünglich falsch eingeschätzt; die interne Güterklassifizierungsdokumentation ist unverzüglich nachzuholen.**

---

*Erstellt: 15.04.2026 | Rainer Hofstädter, Exportkontrollbeauftragter | GM-EK-2026-041-DU*  
*Geprüft: 15.04.2026 | Dr. Sabine Brennecke, Syndikusrechtsanwältin*
