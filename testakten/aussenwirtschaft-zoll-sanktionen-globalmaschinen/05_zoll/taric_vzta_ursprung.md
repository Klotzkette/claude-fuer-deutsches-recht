# Tarifierungsmemo und vZTA-Antragsentwurf: CNC-Steuermodul GX-900

**Dokumenttyp:** Zolltarifliches Memo + Antragsentwurf vZTA  
**Aktenzeichen:** GM-ZOLL-2026-008  
**Erstellt:** 16. April 2026  
**Verfasser:** Benedikt Schramm, Zollbeauftragter  
**Adressat:** Geschäftsführung, Exportkontrollabteilung  

---

## 1. Tarifierungsmemo

### 1.1 Anlass

Die Globalmaschinen GmbH hat das CNC-Steuermodul GX-900 intern unter der Warenposition **8537 10** eingereiht. Diese Einreihung wurde bislang nicht durch eine verbindliche Zolltarifauskunft (vZTA) bestätigt. Im Kontext der laufenden Hauptzollamtsprüfung und der geplanten Ausfuhr nach Kasachstan ist eine belastbare Tarifierung notwendig. Das vorliegende Memo dokumentiert den Tarifierungsweg und bereitet den vZTA-Antrag vor.

### 1.2 Warenbezeichnung und technischer Ausgangspunkt

Das GX-900 ist ein numerisches Steuermodul für mehrachsige CNC-Werkzeugmaschinen. Es enthält:
- Zentralen Rechenkern (Quadcore-ARM-SoC)
- Speicherkomponenten (RAM 4 GB, Flash 32 GB)
- Kommunikationsschnittstellen (EtherCAT, Profinet, Ethernet)
- Hardware Security Module (HSM)
- Bedienoberfläche (Display-Anschluss, Touch-Schnittstelle)
- Versorgungsnetzteil 24 V DC (intern)

Das Modul wird als selbstständige Einheit geliefert (kein Gehäuse der Werkzeugmaschine); es stellt kein vollständiges System dar, sondern eine funktionale Baugruppe.

### 1.3 Tarifierungsanalyse nach dem Harmonisierten System (HS) und der Kombinierten Nomenklatur (KN)

#### Kapitel 85 – Elektrische Maschinen, Apparate, Geräte

Das GX-900 ist ein elektrischer Apparat zur Steuerung und Signalverarbeitung. Es kommen in Frage:

**Option A: Position 8537 – Tafeln, Schalter, Steuergeräte (≤ 1000 V)**

> "Tafeln, Pults, Schränke, Pulte, Truhen und andere Schaltanlagen für eine Spannung von höchstens 1 000 V"

8537 10 99: Sonstige Tafeln, Schalter und Steuergeräte, ≤ 1000 V, nicht anderweitig genannt.

Für das GX-900 spricht 8537:
- Ausgangsspannung 24 V DC (≤ 1000 V)
- Funktion: Steuerung elektrischer Antriebe (Servos, Encoder)
- Enthält Schutzvorrichtungen, Verbindungsstücke, Eingabegeräte

**Option B: Position 8471 – Automatische Datenverarbeitungsmaschinen (ADV)**

> "Automatische Datenverarbeitungsmaschinen und ihre Einheiten..."

Dagegen spricht:
- Das GX-900 ist nicht zum Einsatz als allgemeine Datenverarbeitungsmaschine konzipiert.
- Es ist mechanisch und funktional auf CNC-Werkzeugmaschinensteuerung ausgerichtet.
- Anmerkung 5E zu Kapitel 84 schließt Maschinen, die nicht zur allgemeinen Verwendung geeignet sind, explizit aus dem ADV-Bereich aus.

**Option C: Position 8479 – Maschinen und Apparate mit besonderer Funktion**

8479 89 (Maschinen und Apparate mit besonderer Funktion, anderweitig weder genannt noch inbegriffen): Diese Ausweichposition kommt infrage, wenn 8537 nicht passt. Das GX-900 hat aber eine klar definierte Steuerfunktion für elektrische Antriebe – 8537 ist präziser.

**Tarifierungsergebnis:**

| Position | Beschreibung | Anwendbar? |
|---|---|---|
| **8537 10 99** | Steuergeräte ≤ 1000 V, sonstige | **Ja – bevorzugte Einreihung** |
| 8471 80 | ADV-Einheiten | Nein |
| 8479 89 | Sonstige Maschinen | Fallback, wenn 8537 abgelehnt |

**TARIC-Code:** 8537 10 99 10 (DE-Tarifierung, Zusatzcode für Mehrachsensteuerungen, Anmerkung: konkrete Unterpositionierung durch HZA zu bestätigen)

**Drittlandszollsatz:** 2,7 % (EU-Normalsatz für 8537 10 99 per Zolltarif 2026)

### 1.4 Ursprungsbestimmung

#### 1.4.1 Problematik

Für den Nachweis des EU-Ursprungs (nichtpräferenziell und präferenziell) bestehen folgende Lücken:

| Problem | Beschreibung |
|---|---|
| US-Prozessorkern | ARM Cortex-A72, Chip-Design USA – kein EU-Ursprung für diese Komponente |
| Lieferantenerklärung Schweiz | Ausgestellt 2025 für Swiss Parts AG; zugrundeliegende Stückliste wurde seitdem geändert – Erklärung ist ungültig |
| Fehlende REX-Registrierung | Globalmaschinen ist noch nicht im REX-System (Registered Exporter System) registriert |
| CBAM-Relevanz | Stahl/Aluminium-Importe aus Drittstaaten für Fertigung – Ursprungsnachweispflicht prüfen |

#### 1.4.2 Nichtpräferenzieller Ursprung

Der nichtpräferenzielle Ursprung (Art. 59–63 UZK) richtet sich nach der letzten wesentlichen und wirtschaftlich gerechtfertigten Be- oder Verarbeitung, die in einem Unternehmen ausgeführt wurde und zur Herstellung eines neuen Erzeugnisses führte (Tarifpositionswechsel-Regel).

Der US-Prozessorkern (HS 8542 – integrierte Schaltkreise) wird beim Einbau in das GX-900 (HS 8537) einer Tarifpositionsänderung auf Kapitelebene unterzogen (Kapitel 85 verbleibt; aber Positionsebene wechselt von 8542 zu 8537). Nach Art. 32 der Durchführungsverordnung (EU) 2015/2447 reicht ein Positionswechsel auf 4-Stellen-Ebene aus, sofern der Wertschöpfungsanteil in der EU angemessen ist.

**Vorläufiges Ergebnis nichtpräferenziell:** Der überwiegende Wertschöpfungsanteil (Montage, Integration, Software, Qualitätsprüfung) erfolgt in Stuttgart. EU-Ursprung nach Tarifpositionswechsel-Methode ist vertretbar; sollte durch HZA-Binding Ruling bestätigt werden.

#### 1.4.3 Präferenzieller Ursprung (REX / Lieferantenerklärung)

Für Exporte in Länder mit EU-Freihandelsabkommen (z.B. Kasachstan: kein FHA mit EU; Schweiz: FHA 1972/Zollunion) ist der präferenzielle Ursprung relevant. Für den Schweizer Präferenzursprung der Swiss-Parts-AG-Lieferungen (Schrauben, Verbindungselemente) ist:

1. Die alte Lieferantenerklärung (LE 2025) aufgrund der Stücklistenänderung **ungültig**.
2. Eine neue LE muss von Swiss Parts AG für die aktuelle Stückliste ausgestellt werden.
3. Alternativ: Langzeit-Lieferantenerklärung für 2026.

Für die eigenen Ausfuhren der Globalmaschinen GmbH nach Ländern mit FHA-Präferenzen:

- Globalmaschinen ist **nicht im REX-System registriert**. Für Sendungen über 6.000 EUR (außerhalb EU) ohne REX-Registrierung kann kein präferenzieller Ursprungsnachweis in Form einer Ursprungserklärung auf der Rechnung ausgestellt werden.
- **Maßnahme:** REX-Registrierung beim HZA Stuttgart-Neckar beantragen (Formular 0870 e).

---

## 2. Entwurf: Antrag auf Verbindliche Zolltarifauskunft (vZTA)

> **Achtung:** Dies ist ein Antragsentwurf. Der finale Antrag ist über das EU-Portal EBTI-3 (European Binding Tariff Information) einzureichen.

---

**Antrag auf Erteilung einer verbindlichen Zolltarifauskunft**  
gemäß Art. 33 Unionszollkodex (UZK), VO (EU) Nr. 952/2013

**Antragsteller:**

> Globalmaschinen GmbH  
> Rotebühlplatz 18  
> 70178 Stuttgart  
> EORI-Nummer: DE 1234567890001  
> Umsatzsteuer-ID: DE 987654321  
> Ansprechpartner: Benedikt Schramm, Tel. +49 711 123456-78

**Zuständige Zollbehörde:**

> Generalzolldirektion  
> Referat Verbindliche Zolltarifauskünfte  
> Carusufer 3–5  
> 01099 Dresden

**Betreff:** Antrag auf vZTA für CNC-Steuermodul GX-900

---

### 2.1 Angaben zur Ware

| Merkmal | Angabe |
|---|---|
| Handelsbezeichnung | CNC-Steuermodul GX-900 |
| Interne Artikelnummer | 8000-GX900-EU |
| Vorgeschlagene Einreihung | 8537 10 99 |
| Beschreibung | Numerisches Steuermodul für CNC-Werkzeugmaschinen, 9 interpolierende Achsen, 24 V DC, mit EtherCAT-Schnittstelle und integriertem HSM |
| Bestimmungsland | Kasachstan (als Beispiel-Exportziel) |
| Warenwert (Richtwert) | ca. 890 EUR/Stück |

### 2.2 Begründung der vorgeschlagenen Tarifierung

Das CNC-Steuermodul GX-900 ist ein elektrischer Steuerapparat im Sinne der Tarifposition 8537. Es ist auf die Steuerung elektrischer Antriebe (Servoantriebe) in CNC-Werkzeugmaschinen ausgelegt und enthält alle wesentlichen Funktionseinheiten einer Steueranlage (Prozessor, Kommunikationsinterfaces, Signalverarbeitung, Schutzvorrichtungen). Es handelt sich nicht um eine allgemeine Datenverarbeitungsmaschine (8471), da die Ware ausschließlich für den spezifischen Einsatz als Werkzeugmaschinensteuerung konstruiert ist (vgl. Anmerkung 5 zu Kapitel 84 HS).

Die Unterposition 8537 10 gilt für Betriebsspannungen ≤ 1.000 V (hier: 24 V DC). Die Unterposition 8537 10 99 erfasst sonstige Geräte dieser Art. Ein spezifischerer Zusatzcode (10-stellige TARIC-Ebene) ist durch die Zollbehörde zu bestimmen.

### 2.3 Anlagen zum Antrag

1. Technisches Datenblatt GX-900 (Version 3.2, 01/2026) – wird beigefügt
2. Schaltplan (vereinfacht, ohne sicherheitskritische Details) – wird beigefügt
3. Foto der Ware (Frontansicht, Rückansicht, Platine) – wird beigefügt
4. Muster (Warenprobe oder verfügbar auf Anfrage)
5. Stückliste (BoM, Stand 03/2026) – wird beigefügt
6. Vergleichbare vZTA aus anderen EU-Mitgliedstaaten (keine bekannt)

### 2.4 Erklärung

Der Antragsteller bestätigt die Vollständigkeit und Richtigkeit der gemachten Angaben. Es sind keine laufenden Rechtsstreitigkeiten oder anderweitigen vZTA-Anträge für diese Ware bekannt.

---

*Stuttgart, 16.04.2026*  
*Benedikt Schramm, Zollbeauftragter*  
*Globalmaschinen GmbH*

---

## 3. Zusammenfassung und Empfehlungen

| Thema | Status | Maßnahme |
|---|---|---|
| Tarifierung 8537 10 99 | Intern bestätigt, nicht verbindlich | vZTA beantragen (EBTI-3) |
| Lieferantenerklärung Swiss Parts AG | Ungültig (Stücklistenänderung) | Neue LE anfordern bis 30.04.2026 |
| REX-Registrierung | Fehlend | Antrag HZA Stuttgart bis 30.04.2026 |
| Nichtpräferenzieller EU-Ursprung | Vertretbar nach Tarifpositionswechsel | HZA-Binding Ruling empfohlen |
| TARIC-Zusatzcode | Unklar | Klärung mit HZA Stuttgart |

---

*GM-ZOLL-2026-008 | Benedikt Schramm, Zollbeauftragter | 16.04.2026*
