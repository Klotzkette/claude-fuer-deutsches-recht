---
name: lease-leasing-abrechnung-inkasso
description: "Lease Leasing Abrechnung Inkasso: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Leasing Abrechnung Inkasso

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Leasing Abrechnung Inkasso** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-038-leasing-abrechnung-nachforderung-und-verjaehrung` | Leasingabrechnung: Schlussrechnung, Nachforderungen, Verrechnung von Verwertungserlösen, Verjährungsfristen und Einwendungen des LN. |
| `lease-039-inkasso-leasingforderung` | Inkasso von Leasingforderungen: Mahnprozess, Mahnbescheid, Zwangsvollstreckung, Pfändung von Lohn und Konto, Restschuldbefreiung. |
| `lease-040-gerichtliche-durchsetzung-leasingraten` | Gerichtliche Durchsetzung von Leasingraten: Klage, Beweisführung, einstweiliger Rechtsschutz, vollstreckungsfähiger Titel und Prozessstrategie. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Leasing Abrechnung Inkasso**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-038-leasing-abrechnung-nachforderung-und-verjaehrung`

**Fokus:** Leasingabrechnung: Schlussrechnung, Nachforderungen, Verrechnung von Verwertungserlösen, Verjährungsfristen und Einwendungen des LN.

# Leasingabrechnung, Nachforderung und Verjährung

## Zweck

Am Vertragsende oder nach Kündigung ist eine detaillierte Leasingabrechnung zu erstellen. LN und LG streiten häufig über Nachforderungen, Verwertungserlöse und die Höhe von Schadensersatz. Dieser Skill analysiert die Abrechnungsstruktur, Verjährungsfristen und Verteidigungsstrategien.

## Schlussabrechnung nach Vertragsende

### Bestandteile der Abrechnung
1. **Offene Leasingraten**: Noch nicht bezahlte Raten bis Vertragsende
2. **Minderwert**: Übermäßige Abnutzung bei Rückgabe (§ 548 BGB-Analogie)
3. **Mehrkilometer**: Bei Kilometervertrag über vereinbarte km hinaus
4. **Restwertdifferenz**: Bei Restwertvertrag (wenn Verwertungserlös < kalkulierter Restwert)
5. **Sonstiges**: Fehlende Schlüssel, Zubehör, Wartungsrückstände

### Verwertungserlös-Anrechnung
- Nach Kündigung: LG verwertet Objekt; Erlös mindert Schaden des LG
- § 254 BGB (Schadensminderungspflicht): LG muss bestmöglich verwerten
- LN kann Rechenschaft über Verwertung verlangen

### Abzinsungspflicht
- Ausstehende Raten (nach Kündigung) werden abgezinst
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06: Nominalwert der ausstehenden Raten minus Abzinsungsbetrag

## Verjährungsfristen

| Anspruch | Frist | Beginn | Norm |
|---|---|---|---|
| Mietrechtliche Ansprüche (Minderwert) | 6 Monate | Rückgabe | § 548 BGB |
| Schadensersatz (allgemein) | 3 Jahre | Kenntnis | § 195 BGB |
| Vertragliche Leasingraten | 3 Jahre | Fälligkeit | § 195 BGB |
| Deliktische Ansprüche | 3 Jahre | Kenntnis | § 199 BGB |
| Arglistig verschwiegene Mängel | 3 Jahre | Kenntnis | § 195 BGB |

### § 548 BGB: 6-Monatsfrist für Minderwert
- LG muss Minderwert innerhalb von **6 Monaten** nach Rückgabe geltend machen
- Frist beginnt mit Rückgabe (Schlüsselübergabe, Protokoll)
- Gutachtenerstellung nach 6 Monaten: Zu spät; Anspruch verjährt
- Unterbrechung: Durch Klage (§ 204 BGB), Mahnbescheid, schriftliches Anerkenntnis

## Einwendungen des LN

### Minderwert
- Kein Minderwert: Schaden liegt innerhalb normaler Abnutzung
- Gutachten fehlerhaft: Eigenes Gegengutachten beauftragen
- Fehlende Kausalität: Schaden nach Rückgabe entstanden

### Restwertdifferenz
- Verwertungserlös zu niedrig: LG hat nicht bestmöglich verwertet (§ 254 BGB)
- Restwert zu hoch kalkuliert: Klausel AGB-widrig (fehlende Mehrerlösklausel)

### Verjährung
- Wenn LG 6-Monats-Frist (§ 548 BGB) versäumt: Einrede der Verjährung (§ 214 BGB)
- LN muss Verjährungseinrede erheben; sie gilt nicht von Amts wegen

## Aufrechnung (§ 387 BGB)

- LN kann mit Gegenforderungen aufrechnen (z.B. überbezahlte Raten, Vorauszahlung)
- Abtretung: Wenn Forderung abgetreten, kann LN nach § 406 BGB mit Gegenforderungen aufrechnen

## Gerichtliche Durchsetzung

- Mahnbescheid: Für Leasingraten geeignet (§§ 688 ff. ZPO)
- Klagefrist: § 548 BGB startet Verjährung ab Rückgabe → sofort tätig werden

## Prüfprogramm

1. Schlussabrechnung vollständig: Raten, Minderwert, km, Restwert, Abzinsung?
2. § 548 BGB: 6-Monate-Frist ab Rückgabe gewahrt?
3. Verwertungserlös: Dokumentiert und marktgerecht?
4. LN-Einwände: Normale Abnutzung, falsches Gutachten, zu niedrige Verwertung?
5. Verjährungseinrede: Hat LN erhoben? Frist abgelaufen?
6. Aufrechnung: Gegenforderungen des LN vorhanden?

## Typische Fallen

- LG erstellt Minderwertgutachten 7 Monate nach Rückgabe: § 548 BGB-Verjährung
- Keine Abzinsung der ausstehenden Raten: BGH-widrig → reduzierter Anspruch
- Verwertungserlös ohne Dokumentation → LN ficht an
- LN erhebt Verjährungseinrede nicht → verliert sie

## Normen und Quellen

- § 548 BGB (Verjährung Mietrecht): https://dejure.org/gesetze/BGB/548.html
- § 195 BGB (Regelverjährung): https://dejure.org/gesetze/BGB/195.html
- § 199 BGB (Verjährungsbeginn): https://dejure.org/gesetze/BGB/199.html
- § 387 BGB (Aufrechnung): https://dejure.org/gesetze/BGB/387.html
- § 254 BGB (Schadensminderungspflicht): https://dejure.org/gesetze/BGB/254.html
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Abzinsung nach Kündigung): https://www.bgh.de
- openjur.de § 548 BGB Leasing: https://openjur.de

## Output-Formate

- **Schlussabrechnungs-Vorlage**: Leasingvertrag – alle Positionen
- **Verjährungs-Fristenplan**: Rückgabe → 6-Monats-Frist § 548 BGB
- **Widerspruch-Vorlage**: LN gegen Minderwert- und Restwertnachforderung
- **Abzinsungs-Tabelle**: Ausstehende Raten nach Kündigung

## 2. `lease-039-inkasso-leasingforderung`

**Fokus:** Inkasso von Leasingforderungen: Mahnprozess, Mahnbescheid, Zwangsvollstreckung, Pfändung von Lohn und Konto, Restschuldbefreiung.

# Inkasso von Leasingforderungen

## Zweck

Dieser Skill führt durch den vollständigen Inkasso-Prozess für ausgefallene Leasingforderungen: vom ersten Mahnschreiben bis zur Zwangsvollstreckung und den Besonderheiten bei privaten Schuldnern (Restschuldbefreiung).

## Außergerichtliches Mahnverfahren

### Mahnstufenfolge
1. **1. Mahnung**: Zahlungserinnerung, keine Kosten (Kulanz)
2. **2. Mahnung**: Setze Frist (z.B. 14 Tage), drohe Inkasso an
3. **3. Mahnung / Letzte Mahnung**: Kündigung und Klage ankündigen
4. **Inkasso-Beauftragung** oder **gerichtliches Mahnverfahren**

### Verzugszinsen
- § 286 BGB: Verzug tritt ein nach Mahnung oder bei kalendarisch bestimmtem Fälligkeitstermin
- § 288 BGB: Verzugszinsen 5 % über Basiszinssatz (B2C); 9 % über Basiszinssatz (B2B)
- § 289 BGB: Zinseszinsverbot

### Inkassokosten
- RDG § 10: Inkassounternehmen darf Kosten nach RVG-Tabelle berechnen
- Inkassokosten als Verzugsschaden geltend machen (§ 280 I, II BGB)

## Gerichtliches Mahnverfahren (§§ 688 ff. ZPO)

### Antrag auf Mahnbescheid
- Formular: Bundesweites Online-Mahnportal (egvp.de)
- Kosten: Gerichtsgebühren nach GKG (günstiger als Klage)
- Zustellung: Zustellung durch Gericht an Schuldner
- Widerspruch: Schuldner kann widersprechen (dann → streitiges Verfahren)

### Vollstreckungsbescheid
- Kein Widerspruch: Vollstreckungsbescheid auf Antrag
- Vollstreckungsbescheid = Vollstreckungstitel (§ 794 I Nr. 4 ZPO)

## Zwangsvollstreckung (§§ 803 ff. ZPO)

### Pfändungsarten

**Kontopfändung (§§ 828 ff. ZPO)**:
- Pfändungs- und Überweisungsbeschluss (PfÜB) an Bank
- Konto P-Konto (§ 850k ZPO): Mindestpfändungsfreigrenze (2024: 1.410 €/Monat)

**Lohnpfändung (§§ 850 ff. ZPO)**:
- Pfändung des Arbeitseinkommens; Pfändungsfreigrenze beachten
- Tabelle nach § 850c ZPO: Abhängig von Nettoeinkommen und Unterhaltsverpflichtungen

**Sachpfändung (§§ 808 ff. ZPO)**:
- Gerichtsvollzieher pfändet bewegliche Sachen beim Schuldner
- Unpfändbare Sachen: §§ 811 f. ZPO (Gegenstände für Grundbedarf)

### Vermögensauskunft (§ 802a ZPO)
- Schuldner muss vollständige Vermögensauskunft erteilen
- Eintragung ins Schuldnerverzeichnis bei Falschaussage oder Nichtzahlung

## Verbraucher: Restschuldbefreiung

- §§ 286 ff. InsO: Privatinsolvenz mit Wohlverhaltensperiode (3 Jahre seit 2021)
- Restschuldbefreiung: Leasingforderung nach Wohlverhaltensperiode erlischt
- Ausnahme: Vorsätzliche unerlaubte Handlung (§ 302 Nr. 1 InsO)

## Prüfprogramm

1. Vollständige Forderungsaufstellung: Raten, Zinsen, Kosten?
2. Außergerichtlich erfolglos? Mahnbescheid-Antrag stellen?
3. Vollstreckungstitel vorhanden? Vollstreckungsbescheid oder Urteil?
4. Vermögensauskunft: Was hat Schuldner?
5. Pfändungsart: Konto, Lohn oder Sachpfändung?
6. Privatinsolvenz: Restschuldbefreiung zu erwarten?

## Typische Fallen

- Verjährung vergessen (§ 195 BGB: 3 Jahre ab Fälligkeit) → Forderung verjährt
- P-Konto nicht beachtet → Pfändung scheitert an Freibetrag
- Restschuldbefreiung nicht geprüft → kostspielige Vollstreckung ohne Ergebnis
- Vollstreckungsbescheid nicht rechtszeitig vollstreckt → 30-jährige Verjährung läuft ab 2024 nicht mehr automatisch

## Normen und Quellen

- §§ 286–290 BGB (Verzug, Zinsen): https://dejure.org/gesetze/BGB/286.html
- §§ 688 ff. ZPO (Mahnverfahren): https://www.gesetze-im-internet.de/zpo/__688.html
- §§ 803 ff. ZPO (Zwangsvollstreckung): https://www.gesetze-im-internet.de/zpo/__803.html
- § 850c ZPO (Pfändungsfreigrenze): https://www.gesetze-im-internet.de/zpo/__850c.html
- §§ 286 ff. InsO (Restschuldbefreiung): https://www.gesetze-im-internet.de/inso/__286.html
- RDG § 10 (Inkassorecht): https://www.gesetze-im-internet.de/rdg/__10.html

## Output-Formate

- **Mahnschreiben-Reihe**: Stufen 1–3 mit Fristen und Ankündigungen
- **Mahnbescheids-Antrag**: Formularanleitung für egvp.de
- **Pfändungs-Checkliste**: Konto, Lohn, Sachen – Voraussetzungen und Fristen
- **Vollstreckungsübersicht**: Schuldner-Vermögen – geeignete Maßnahme

## 3. `lease-040-gerichtliche-durchsetzung-leasingraten`

**Fokus:** Gerichtliche Durchsetzung von Leasingraten: Klage, Beweisführung, einstweiliger Rechtsschutz, vollstreckungsfähiger Titel und Prozessstrategie.

# Gerichtliche Durchsetzung von Leasingraten

## Zweck

Wenn außergerichtliches Mahnverfahren scheitert, muss der LG klagen. Dieser Skill führt durch die Prozesstaktik, Beweisführung, einstweiligen Rechtsschutz und die Besonderheiten der Leasingrate-Klage.

## Vorbereitende Maßnahmen

### Aktenaufbau
- Leasingvertrag (Original oder beglaubigte Kopie)
- Abnahmeprotokoll (Beweismittel für Übergabe und Zustand)
- Rechnungen (fällige Raten, lückenlos)
- Mahnkorrespondenz (Nachweis Verzug und Abmahnung)
- Bonitätsnachweis Schuldner (für Vollstreckbarkeit)

### Gerichtsstand
- Allgemeiner Gerichtsstand: Wohnort oder Sitz des Beklagten (§ 12 ZPO)
- Besonderer Gerichtsstand: Erfüllungsort (§ 29 ZPO) → typischerweise Sitz des LG
- Gerichtsstandsklausel im Leasingvertrag: Im B2B zulässig; im B2C nur eingeschränkt (§ 38 ZPO)
- Streitwert bestimmt Zuständigkeit: Bis 5.000 € → Amtsgericht; darüber → Landgericht

### Prozesskostenhilfe / Kostenrisiko
- Obsiegende Partei erhält Kostenerstattung (§ 91 ZPO)
- Unterliegender zahlt: Anwaltsgebühren + Gerichtsgebühren
- Bei Insolvenz des Schuldners: Kosten faktisch verloren

## Klage auf Leasingraten

### Klageart: Leistungsklage
- Zahlungsklage auf fällige Leasingraten
- Streitwert: Summe der eingeklagten Raten + Zinsen + Kosten

### Beweisführung
- Vertragsschluss: Schriftlicher Leasingvertrag mit beider Unterschrift
- Übergabe des Leasingobjekts: Abnahmeprotokoll
- Ratenfälligkeit: Zahlungsplan aus Vertrag
- Verzug: Mahnung oder kalendarisch bestimmte Fälligkeit (§ 286 II BGB)
- Kündigung (wenn nach Kündigung geltend gemacht): Kündigungsschreiben

### Liquidität der Forderung
- Klare Berechnung: Rate × Monate + Zinsen
- Unklare Nebenforderungen (Minderwert) separat geltend machen

## Einstweiliger Rechtsschutz

### Einstweilige Verfügung auf Herausgabe des Leasingobjekts (§ 935 ZPO)
- Nach Kündigung: Herausgabeantrag als einstweilige Verfügung
- Voraussetzungen: Verfügungsanspruch (Eigentum + Kündigung) + Verfügungsgrund (Veräußerungsgefahr)
- Vollzug: Gerichtsvollzieher holt Objekt unmittelbar

### Arrest auf Vermögen (§§ 916 ff. ZPO)
- Sicherungsarrest: Wenn konkrete Gefährdung der Vollstreckung droht (z.B. Schuldner flüchtet, versteckt Vermögen)
- Arrest legt das Vermögen des Schuldners vorläufig fest

## Prozessführung gegen Verbraucher

### Pflichtberatungshinweis
- Gericht weist Verbraucher auf Beratungsmöglichkeiten hin
- Verbraucher kann Einwendungen nachschieben

### Schutzschrift des Schuldners
- Bei erwarteten einstweiligen Verfügungen: Schuldner kann Schutzschrift hinterlegen (§ 945a ZPO)
- Gericht muss Schutzschrift berücksichtigen

## Vollstreckung des Titels

Nach rechtskräftigem Urteil oder Vollstreckungsbescheid:
- Zwangsvollstreckung nach §§ 803 ff. ZPO
- Vollstreckungsklausel: § 724 ZPO
- Zustellung des Titels an Schuldner: Voraussetzung (§ 750 ZPO)

## Prüfprogramm

1. Akten vollständig: Vertrag, Protokoll, Rechnungen, Mahnung?
2. Gerichtsstand: Allgemein oder vertraglich? Zuständig?
3. Klageart und Streitwert: Fällige Raten + Zinsen + ggf. Schadensersatz?
4. Einstweilige Verfügung: Objekt gefährdet? Verfügungsgrund beweisbar?
5. Gegenforderungen LN: Mängelansprüche, Aufrechnung vorhergesehen?
6. Vollstreckung: Schuldner hat pfändbares Vermögen?

## Typische Fallen

- Gerichtsstand-Klausel gegenüber Verbraucher unwirksam → Klage am falschen Gericht
- Kündigung nicht nachgewiesen → Klage auf künftige Raten zu früh
- Einstweilige Verfügung ohne Verfügungsgrund → Gericht lehnt ab
- Titel vollstreckt, Schuldner mittellos → Kostenverschwendung

## Normen und Quellen

- §§ 12, 29 ZPO (Gerichtsstand): https://www.gesetze-im-internet.de/zpo/__12.html
- §§ 935–945a ZPO (einstweilige Verfügung): https://www.gesetze-im-internet.de/zpo/__935.html
- §§ 916 ff. ZPO (Arrest): https://www.gesetze-im-internet.de/zpo/__916.html
- § 91 ZPO (Kostenerstattung): https://www.gesetze-im-internet.de/zpo/__91.html
- §§ 803 ff. ZPO (Vollstreckung): https://www.gesetze-im-internet.de/zpo/__803.html
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz nach Kündigung): https://www.bgh.de

## Output-Formate

- **Klageschrift-Vorlage**: Leasingrate-Klage mit Streitwert und Beweisliste
- **eV-Antrag-Vorlage**: Herausgabe Leasingobjekt nach Kündigung
- **Prozess-Checkliste**: Akten, Beweise, Gerichtsstand, Kostenrisiko
- **Vollstreckungsablauf**: Titel → Klausel → Zustellung → Pfändung
