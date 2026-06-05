---
name: lease-mobile-work-verwertung
description: "Lease Mobile Work Verwertung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Mobile Work Verwertung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Mobile Work Verwertung** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-056-mobile-work-equipment` | Leasing mobiler Arbeitsgeräte: Laptops, Tablets, Smartphones; MDM, Datenschutz, BYOD vs. COPE, Rückgabe und Nutzungsrichtlinien. |
| `lease-057-verwertung-nach-kuendigung` | Verwertung des Leasingobjekts nach Kündigung: Verfahren, Schadensminderungspflicht, Erlösoptimierung, Dokumentation und Schadensersatzberechnung. |
| `lease-058-verbraucherbeweglich` | Verbraucherleasing beweglicher Sachen: Pflichtangaben, Widerruf, fehlerhafte Belehrung, Rückabwicklung, typische Fallen und Musterfälle. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Mobile Work Verwertung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-056-mobile-work-equipment`

**Fokus:** Leasing mobiler Arbeitsgeräte: Laptops, Tablets, Smartphones; MDM, Datenschutz, BYOD vs. COPE, Rückgabe und Nutzungsrichtlinien.

# Leasing mobiler Arbeitsgeräte: Laptops, Tablets, Smartphones

## Zweck

Mobile Endgeräte sind das am weitesten verbreitete IT-Leasingsegment. Unternehmen leeasen Laptops, Tablets und Smartphones für ihre Mitarbeiter. Dieser Skill klärt MDM-Anforderungen, Datenschutz, Nutzungsrichtlinien und Rückgabeprozesse.

## BYOD vs. COPE vs. COBO

### BYOD (Bring Your Own Device)
- Mitarbeiter nutzt eigenes Gerät für dienstliche Zwecke
- Kein Leasinggerät; kein LG-Eigentum
- Datenschutz: Unternehmensdaten auf privatem Gerät → MDM erforderlich

### COPE (Corporate Owned, Personally Enabled)
- Unternehmen least Gerät (LN = Unternehmen); Mitarbeiter darf privat nutzen
- Leasingvertrag zwischen LG und Unternehmen
- MDM: Unternehmensdaten getrennt von privaten Daten

### COBO (Corporate Owned, Business Only)
- Gerät nur für geschäftliche Nutzung; keine private Nutzung
- Einfacher für Datenschutz und MDM
- Mitarbeiterzufriedenheit oft geringer

## MDM (Mobile Device Management)

### Funktionen
- Remote Wipe: Gerät aus der Ferne löschen (bei Verlust, Rückgabe)
- Datenverschlüsselung: Unternehmensdaten verschlüsselt
- App-Management: Nur genehmigte Apps erlaubt
- Geofencing: Alarm bei ungewöhnlichem Standort

### MDM und DSGVO
- MDM kann personenbezogene Daten des Mitarbeiters erfassen (Standort, Apps)
- Rechtsgrundlage: § 26 BDSG (Beschäftigtendatenschutz)
- Betriebsrat: Mitbestimmungsrecht (§ 87 I Nr. 6 BetrVG)
- Betriebsvereinbarung MDM empfohlen

## Datenschutz bei COPE

### Getrennte Container
- Android Enterprise / iOS DEP: Arbeits-Container und privater Bereich getrennt
- Remote Wipe nur für Arbeitsbereich (nicht private Fotos des Mitarbeiters)
- Transparenzpflicht: Was erfasst MDM vom Mitarbeiter?

### Art. 13 DSGVO
- Information des Mitarbeiters: Welche Daten werden durch MDM verarbeitet?
- Aufbewahrungsfristen für MDM-Logs

## Rückgabe von Mobilen Endgeräten

### Prozess
1. Mitarbeiter gibt Gerät an IT-Abteilung zurück
2. IT: Remote Wipe (MDM) oder Factory Reset
3. Physischer Zustand prüfen: Displayrisse, Tastendefekte, Akku
4. Datenlöschungs-Zertifikat erstellen
5. Gerät an LG zurückgeben (ggf. über Leasingpartner)

### Minderwert bei mobilen Geräten
- Normale Abnutzung: Leichte Kratzer am Gehäuse; kein Minderwert
- Übermäßiger Verschleiß: Displaybruch, fehlende Tasten, wasserbeschädigte Komponenten

## Nutzungsrichtlinie (Acceptable Use Policy)

### Inhalte
- Erlaubte und verbotene Nutzung (private Nutzung: ja/nein/begrenzt)
- Sicherheitsanforderungen: Bildschirmsperre, PIN, VPN bei Remote Access
- App-Installation: Nur aus genehmigtem App-Store
- Sorgfaltspflicht: Keine Weitergabe an Dritte, Diebstahlschutz

### Rechtliche Basis
- Arbeitsvertrag: Weisungsrecht Arbeitgeber (§ 106 GewO)
- Betriebsvereinbarung: Wenn Überwachungsmaßnahmen enthalten

## Prüfprogramm

1. BYOD, COPE oder COBO? Leasingvertrag angepasst?
2. MDM vorhanden und DSGVO-konform? Betriebsvereinbarung?
3. Art. 13 DSGVO: Mitarbeiter über MDM-Datenverarbeitung informiert?
4. Remote Wipe bei COPE: Nur Arbeitsbereich, nicht privater Bereich?
5. Rückgabeprotokoll: Remote Wipe, physischer Zustand, Datenlöschungs-Zertifikat?
6. Nutzungsrichtlinie: Verabschiedet und jedem Mitarbeiter ausgehändigt?

## Typische Fallen

- Remote Wipe auf COPE-Gerät löscht private Fotos → Datenschutzverletzung und Schadensersatz
- Keine Betriebsvereinbarung MDM → Betriebsrat kann Nutzung untersagen
- Kein Remote Wipe nach Mitarbeiteraustritt → Unternehmensdaten bei Ex-Mitarbeiter
- Displaybruch: „Normale Abnutzung" oder Minderwert? Im Vertrag definiert?

## Normen und Quellen

- DSGVO Art. 6, 13: https://eur-lex.europa.eu
- § 26 BDSG: https://www.gesetze-im-internet.de/bdsg_2018/__26.html
- § 87 I Nr. 6 BetrVG: https://www.gesetze-im-internet.de/betrvg/__87.html
- § 106 GewO (Direktionsrecht): https://www.gesetze-im-internet.de/gewo/__106.html
- BGH VIII ZR 172/05 (normale Abnutzung): https://www.bgh.de
- Apple DEP / Android Enterprise Dokumentation: https://www.apple.com / https://androidenterprise.dev

## Output-Formate

- **Nutzungsrichtlinie Mobile Geräte**: Muster mit Sicherheitsanforderungen
- **Betriebsvereinbarung MDM**: Muster mit DSGVO-konformen Datenschutzvorgaben
- **Rückgabe-Protokoll Mobiles Gerät**: Zustand, Remote Wipe, Datenlöschungs-Zertifikat
- **MDM-Datenschutzinformation**: Art. 13 DSGVO für Mitarbeiter

## 2. `lease-057-verwertung-nach-kuendigung`

**Fokus:** Verwertung des Leasingobjekts nach Kündigung: Verfahren, Schadensminderungspflicht, Erlösoptimierung, Dokumentation und Schadensersatzberechnung.

# Verwertung nach Kündigung: Prozess und Schadensminderung

## Zweck

Nach der Kündigung des Leasingvertrags muss der Leasinggeber das zurückgeholte Objekt bestmöglich verwerten. Dieser Skill beschreibt den Verwertungsprozess, die rechtliche Schadensminderungspflicht und die Schadensersatzberechnung.

## Schadensminderungspflicht (§ 254 BGB)

### Grundsatz
§ 254 BGB: Der Geschädigte (LG) muss zumutbare Maßnahmen ergreifen, um den Schaden zu begrenzen. Bei der Verwertung eines Leasingobjekts bedeutet dies: **Bestmögliche Verwertung zum erziel­baren Marktpreis**.

**BGH, Urteil vom 14.03.2007 - VIII ZR 68/06**: LG muss sich ersparte Aufwendungen und Verwertungserlös anrechnen lassen; fehlt die Anrechnung in der AGB-Klausel, ist diese unwirksam.

### Folgen bei mangelhafter Verwertung
- LN kann niedrigen Erlös anfechten: „LG hat nicht bestmöglich verwertet"
- Korrekturbetrag: LN zahlt nur den Schaden, der auch bei bestmöglicher Verwertung entstanden wäre
- Beweislast: LG muss nachweisen, dass Verwertung marktgerecht war

## Verwertungsverfahren

### 1. Direktverkauf
- Verkauf an Interessenten im eigenen Netzwerk
- Vorteil: Schnell, günstig
- Dokumentation: Kaufvertrag mit Preis und Käufer; Marktpreisnachweis (Vergleichsangebote)

### 2. Auktion
- Online-Auktion: Bidfood, Auto Trader, Surplex (Maschinenleasing)
- Kraftfahrzeuge: DAT-Händlerauktionen, ADESA, Autorola
- Vorteil: Nachweislich marktgerechter Preis (Auktionsergebnis)
- Nachteil: Auktionsgebühren (3–10 %)

### 3. Inzahlungnahme
- Händler nimmt Objekt in Zahlung beim Kauf eines neuen Objekts
- Preis oft unter Marktwert: LN kann anfechten

### 4. Scrap / Verschrottung
- Letzte Option bei wertlosem Objekt
- Nachweis: Kein Verwertungserlös erzielbar

## Objektspezifische Verwertungskanäle

| Objektklasse | Kanal |
|---|---|
| Kfz | Händlerauktion, Leasing-Rückläufer-Portal, DAT |
| Maschinen | Surplex, Troostwijk, Mascus |
| IT | Certideal, Back Market, eigene Abverkauf-Liste |
| Medizintechnik | ProSciento, Medicalia |
| Flugzeug | AVAC, ILS, Cash 4 Planes |

## Dokumentation der Verwertung

### Nachweispflicht
- Vermarkungsmaßnahmen: E-Mails, Angebote, Inserate
- Angebote: Mindestens 3 Vergleichsangebote dokumentieren
- Auktionsergebnis: Auktionsprotokoll mit Bieterhistorie
- Kaufvertrag: Preis, Käufer, Datum

### Abrechnung gegenüber LN
```
Verwertungserlös (netto)
- Verwertungskosten (Auktionsgebühren, Transport, Aufbereitung)
= Netto-Verwertungserlös
```

## Schadensersatzberechnung

```
Gesamtforderung LG:
+ Ausstehende Raten (abgezinst)
+ Vertragskosten (ggf.)
- Netto-Verwertungserlös
- Ersparte Aufwendungen
= Schadensersatz LN
```

## Prüfprogramm

1. Verwertungsverfahren gewählt: Direktverkauf, Auktion oder Sonstige?
2. Mindestens 3 Vergleichsangebote eingeholt?
3. Auktionsgebühren abgezogen vom Erlös?
4. Schadensminderungspflicht nachweislich erfüllt?
5. Abrechnung: Abzinsung, ersparte Aufwendungen korrekt berücksichtigt?
6. Verjährung: Schadensersatzforderung innerhalb § 195 BGB-Frist geltend gemacht?

## Typische Fallen

- Inzahlungnahme unter Marktwert ohne Dokumentation → LN fechtet Erlös an
- Keine Vergleichsangebote → LG kann Marktgerechtheit nicht beweisen
- Verwertungskosten zu hoch (übertriebene Aufbereitung) → LN mindert Differenzzahlung
- Schadensersatz ohne Abzinsungspflicht → BGH-widrig

## Normen und Quellen

- § 254 BGB (Schadensminderungspflicht): https://dejure.org/gesetze/BGB/254.html
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz nach Kündigung): https://www.bgh.de
- § 309 Nr. 5 BGB (Pauschale): https://dejure.org/gesetze/BGB/309.html
- § 195 BGB (Verjährung): https://dejure.org/gesetze/BGB/195.html
- openjur.de Leasingverwertung: https://openjur.de

## Output-Formate

- **Verwertungs-Dokumentation**: Angebotseinholung, Auktionsprotokoll
- **Schadensersatz-Berechnung**: Vorlage mit Abzinsung und Verwertungserlös
- **Verwertungskanal-Matrix**: Objekt – Kanal – Vor-/Nachteile
- **Abrechnung an LN**: Muster-Schlussabrechnung nach Kündigung

## 3. `lease-058-verbraucherbeweglich`

**Fokus:** Verbraucherleasing beweglicher Sachen: Pflichtangaben, Widerruf, fehlerhafte Belehrung, Rückabwicklung, typische Fallen und Musterfälle.

# Verbraucherleasing beweglicher Sachen: Pflichten und Widerruf

## Zweck

Wenn Verbraucher bewegliche Sachen (Kfz, Haushaltsgeräte, IT, Möbel) leasen, gelten §§ 506–509 BGB mit strikten Pflichtangaben. Fehler bei der Belehrung öffnen ein verlängertes Widerrufsrecht. Dieser Skill systematisiert die Anforderungen für das tägliche Geschäft.

## Anwendungsbereich

### § 506 BGB: Entgeltliche Finanzierungshilfe
- Verbraucher (§ 13 BGB): Natürliche Person außerhalb gewerblicher/beruflicher Tätigkeit
- Entgeltlich: Gegen Zahlung von Leasingraten
- Bewegliche Sachen: Kfz, Haushaltsgeräte, IT-Equipment, Möbel, Sportgeräte

### Nicht erfasst
- Kurzfristige Mietverträge ohne Amortisationsstruktur (z.B. Mietauto für 3 Tage)
- B2B-Verträge: § 506 BGB nicht anwendbar
- Immobilien: Spezialnormen gelten

## Pflichtangaben § 506 III BGB: Vollständige Liste

1. **Art des Leasingvertrags** (Finanzierungsleasing / Operating-Lease klar bezeichnen)
2. **Name und Anschrift des Leasinggebers**
3. **Anschaffungspreis** des Leasingobjekts
4. **Gesamtbetrag aller Zahlungen** des Verbrauchers (Raten + Sonderzahlung + Restwert wenn geschuldet)
5. **Laufzeit** des Vertrags
6. **Betrag, Anzahl und Fälligkeit** der einzelnen Raten
7. **Effektiver Jahreszins** (§ 6 PAngV, Annuitätenmethode)
8. **Gesamtkosten** (Gesamtbetrag abzgl. Anschaffungspreis = Finanzierungskosten)
9. **Widerrufsrecht**: Hinweis auf Widerrufsfrist und Widerrufsfolgen
10. **Restwert/Restwertgarantie** (falls vereinbart)
11. **Sonstige Kosten**: Versicherung, Wartung wenn im Vertrag enthalten

## Fehlerfolgen bei fehlenden Pflichtangaben (§ 494 BGB)

| Fehlende Angabe | Rechtsfolge |
|---|---|
| Kein Effektivzins | Vertrag gilt mit gesetzlichem Zinssatz |
| Kein Gesamtbetrag | Vertrag gilt, aber Gesamtbetrag = Anschaffungspreis |
| Keine Laufzeit | Vertrag auf 12 Monate beschränkt |
| Kein Widerrufshinweis | Widerrufsfrist läuft nicht ab (max. 1 Jahr 14 Tage) |
| Keine Raten-Angabe | Vertrag schwebend unwirksam bis Heilung |

## Widerrufsrecht: Details

### Frist und Auslöser
- Standard: 14 Tage ab Vertragsschluss (§ 355 I BGB)
- Verlängerung: Wenn Widerrufsinformation nicht korrekt (Anlage 7 EGBGB-Format) → Widerruf weiter möglich
- Maximum: 12 Monate + 14 Tage (§ 356b III BGB)

### Ordnungsgemäße Widerrufsinformation
- Format: Anlage 7 zu Art. 247 § 6 EGBGB (Muster-Widerrufsinformation)
- Abweichungen vom Muster → Belehrung gilt nicht als ordnungsgemäß
- Aktuelles Muster verwenden: Änderungen durch Gesetzgeber beachten

### Widerrufsfolgen
- Rückgabe des Leasingobjekts durch Verbraucher
- LG erstattet alle Zahlungen (Raten, Anzahlung)
- Wertersatz: Verbraucher schuldet Wertersatz für tatsächliche Nutzung (§ 357 VII BGB)
- Kein Restwert: Restwertgarantie entfällt

## Musterfälle

### Fall 1: Fehlendes Widerrufshinweis
LN least Kfz; Vertrag enthält keinen Widerrufshinweis. 2 Jahre nach Vertragsschluss widerruft LN.
→ Widerruf wirksam (Frist nie angelaufen); Rückabwicklung; LN muss Wertersatz für 2 Jahre Nutzung zahlen; keine Restwertpflicht.

### Fall 2: Falscher Effektivzins
Effektivzins im Vertrag falsch angegeben (1,9 % statt korrekt 3,2 %).
→ § 494 II BGB: Vertrag gilt mit gesetzlichem Zinssatz (aktuell § 246 BGB: 4 % oder Basiszinssatz + 5 PP); LN schuldet niedrigere Rate.

### Fall 3: Widerruf nach Insolvenz LG
LG insolvent; LN will widerrufen.
→ Widerruf gegen InsO-Verwalter; Rückabwicklung aus Insolvenzmasse; Quotensituation für LN oft schlecht.

## Fernabsatz-Leasing

- Vertragsschluss per Telefon, Internet: §§ 312a ff. BGB zusätzlich
- Widerrufsrecht für Fernabsatz: 14 Tage ab Vertragsschluss (§ 356 BGB)
- Informationspflichten: Identität des LG, Gesamtpreis, Widerruf

## Prüfprogramm

1. Verbraucher (§ 13 BGB)? Bewegliche Sache?
2. Alle 11 Pflichtangaben § 506 III BGB vorhanden?
3. Widerrufsinformation nach Anlage 7 EGBGB aktuell und korrekt?
4. Widerrufsfrist: Noch laufend? Belehrung fehlerhaft?
5. Fehlerfolge § 494 BGB: Welche Angabe fehlt? Rechtsfolge?
6. Fernabsatz: Zusätzliche §§ 312 ff. BGB-Anforderungen?

## Typische Fallen

- Veraltetes Widerrufsformular → Widerruf 3 Jahre nach Vertragsschluss noch möglich
- Effektivzins fehlt → LN schuldet nur gesetzlichen Zins; erhebliche Einnahmeverluste
- Restwertgarantie ohne gesonderte Pflichtangabe → Klausel nichtig; kein Restwert
- Fernabsatz: Widerruf auch wenn LN das Fahrzeug bereits nutzt → Nutzungswert als Wertersatz

## Normen und Quellen

- §§ 506–509 BGB: https://dejure.org/gesetze/BGB/506.html
- § 494 BGB (Fehlerfolge): https://dejure.org/gesetze/BGB/494.html
- §§ 355–361 BGB (Widerruf): https://dejure.org/gesetze/BGB/355.html
- Art. 247 EGBGB (Informationspflichten): https://www.gesetze-im-internet.de/egbgb/art_247.html
- §§ 312 ff. BGB (Fernabsatz): https://dejure.org/gesetze/BGB/312.html
- BGH XI ZR 59/17 (Widerruf Leasingvertrag): https://www.bgh.de
- § 6 PAngV: https://www.gesetze-im-internet.de/pangv/__6.html

## Output-Formate

- **Pflichtangaben-Prüf-Checkliste**: Alle 11 Punkte § 506 III BGB
- **Widerrufsinformation-Muster**: Aktuelle Anlage 7 EGBGB
- **Fehlerfolgen-Tabelle**: Fehlende Angabe → Rechtsfolge § 494 BGB
- **Widerrufserklärung**: Muster für Verbraucher (Textform)
