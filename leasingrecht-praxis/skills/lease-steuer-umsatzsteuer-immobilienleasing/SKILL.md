---
name: lease-steuer-umsatzsteuer-immobilienleasing
description: "Lease Steuer Umsatzsteuer Immobilienleasing: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Steuer Umsatzsteuer Immobilienleasing

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Steuer Umsatzsteuer Immobilienleasing** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-021-steuer-umsatzsteuer-leasingraten-sonderzahlung` | Umsatzsteuer im Leasingrecht: Lieferung vs. sonstige Leistung, Entstehungszeitpunkt, Vorsteuerabzug, Sonderzahlungen und USt-Pflichtangaben. |
| `lease-024-immobilienleasing-erbbaurecht-und-grundbuch` | Immobilienleasing: Erbbaurecht, Grundbucheintragung, Bilanzierung, steuerliche Zurechnung und Besonderheiten gegenüber Mietkauf. |
| `lease-027-grenzueberschreitendes-leasing-unidroit-und-rechtswahl` | Grenzüberschreitendes Leasing: UNIDROIT-Übereinkommen, Rechtswahl (Rom I-VO), internationales Mobiliar-Leasingrecht, Steuerstrukturierung und Valutafragen. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Steuer Umsatzsteuer Immobilienleasing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-021-steuer-umsatzsteuer-leasingraten-sonderzahlung`

**Fokus:** Umsatzsteuer im Leasingrecht: Lieferung vs. sonstige Leistung, Entstehungszeitpunkt, Vorsteuerabzug, Sonderzahlungen und USt-Pflichtangaben.

# Umsatzsteuer im Leasingrecht

## Zweck

Die umsatzsteuerliche Behandlung von Leasingverträgen hängt davon ab, ob der Vertrag als **Lieferung** (Eigentumsübergang wirtschaftlich beim LN) oder als **sonstige Leistung** (fortlaufende Nutzungsüberlassung) qualifiziert wird. Die Unterscheidung bestimmt den USt-Entstehungszeitpunkt und die Vorsteuerabzugsmöglichkeit.

## Lieferung oder sonstige Leistung? (§§ 3, 3a UStG)

### Sonstige Leistung (Regelfall Finanzierungsleasing)
- Wenn wirtschaftliches Eigentum beim LG (BMF-Erlass): Leasingvertrag = Nutzungsüberlassung
- USt-rechtlich: sonstige Leistung (§ 3 IX UStG)
- USt entsteht mit jeder Leasingrate (§ 13 I Nr. 1 UStG): nach Vereinnahmung (IST-Versteuerung) oder nach Rechnungsstellung (SOLL-Versteuerung)

### Lieferung (wirtschaftliches Eigentum beim LN)
- Wenn Mietkauf oder wirtschaftliches Eigentum beim LN: Lieferung (§ 3 I UStG)
- USt entsteht einmalig bei Verschaffung der Verfügungsmacht (§ 13 I Nr. 1 UStG)
- Voller USt-Betrag auf Gesamtpreis (Kaufpreis-Äquivalent)

### BFH V R 51/09 (Finanzierungsleasing und USt-Befreiung)
BFH: Finanzierungsleasing ist als sonstige Leistung (Nutzungsüberlassung) zu qualifizieren; keine USt-Befreiung für Kreditgewährung (§ 4 Nr. 8a UStG) anwendbar, da Leasing kein Kredit ist.

## Entstehung der Umsatzsteuer

### Laufende Leasingraten
- § 13 I Nr. 1 UStG: USt entsteht mit Ablauf des Voranmeldezeitraums, in dem die Leistung ausgeführt wurde
- Bei Vorausrechnungen: USt mit Ausstellung der Rechnung fällig (§ 13 I Nr. 1a S. 4 UStG)
- Anzahlungsrechnung (Sonderzahlung): USt im Zeitpunkt der Vereinnahmung

### Sonderzahlung / Anzahlung
- Sonderzahlung bei Vertragsbeginn = Anzahlung
- § 13 I Nr. 1a S. 4 UStG: USt entsteht bei Vereinnahmung
- Rechnung erforderlich: Anzahlungsrechnung mit gesondertem USt-Ausweis
- Vorsteuerabzug des LN: Erst mit Anzahlungsrechnung möglich

## Vorsteuerabzug (§ 15 UStG)

### Voraussetzungen
- LN ist Unternehmer (§ 2 UStG)
- Leistung für unternehmerischen Bereich verwendet
- Ordnungsgemäße Rechnung (§ 14 UStG): alle Pflichtangaben

### Pflichtangaben der Leasingrechnung (§ 14 IV UStG)
1. Vollständiger Name und Anschrift LG
2. Vollständiger Name und Anschrift LN
3. Steuernummer oder USt-IdNr. des LG
4. Ausstellungsdatum
5. Rechnungsnummer
6. Menge und Art der sonstigen Leistung
7. Zeitraum der sonstigen Leistung
8. Entgelt nach Steuersätzen aufgegliedert
9. Steuerbetrag
10. Anzuwendender Steuersatz
11. Ggf. Hinweis auf Steuerbefreiung

### Vorsteueraufteilung (§ 15 IV UStG)
Wenn LN Gemischtverwender (unternehmerisch + privat): Vorsteuer aufteilen.

## Umsatzsteuerliche Behandlung besonderer Klauseln

### Restwert-Verwertung
- Verwertungserlös am Vertragsende: Lieferung des LG an Erwerber → USt-pflichtig (wenn LG nicht umsatzsteuerbefreit)
- Verwertung im eigenen Namen des LG: Steuerpflicht des LG

### Reparatur-/Wartungskosten
- Im Leasingvertrag enthaltene Wartungskosten (Full-Service): einheitliche Leistung oder mehrere separate?
- BFH: Einheitliche sonstige Leistung, wenn Wartung akzessorisch zum Leasing

## Kommunalleasing und USt-Befreiung
- Körperschaften des öffentlichen Rechts (§ 2b UStG): Ggf. nicht Unternehmer für bestimmte Leistungen
- Aber: KöR als Leasingnehmer in unternehmerischem Bereich: Vorsteuerabzug möglich

## Prüfprogramm

1. Lieferung oder sonstige Leistung? (§ 39 AO-Zurechnung → USt-Qualifikation)
2. USt-Entstehungszeitpunkt: Monatlich (laufende Rate) oder einmalig (Lieferung)?
3. Sonderzahlung: Anzahlungsrechnung ausgestellt? USt korrekt ausgewiesen?
4. Rechnung LN: Alle Pflichtangaben § 14 IV UStG vorhanden?
5. Vorsteuerabzug: LN Unternehmer? Verwendung unternehmerisch?
6. Full-Service: Einheitliche Leistung oder aufzuteilen?

## Typische Fallen

- Sonderzahlung vereinnahmt ohne Anzahlungsrechnung → USt fällig, aber nicht abgeführt
- Rechnung ohne Pflichtangaben → LN verliert Vorsteuerabzug
- Leasingvertrag als Lieferung (Mietkauf) qualifiziert, aber als sonstige Leistung versteuert → USt-Nachzahlung
- Monatliche Rate ohne Dauerrechnung: Nach § 14 III UStG ist Dauerrechnung zulässig, wenn Zeitraum klar

## Normen und Quellen

- § 3 UStG (Lieferung / sonstige Leistung): https://dejure.org/gesetze/UStG/3.html
- § 13 UStG (Entstehung): https://www.gesetze-im-internet.de/ustg_1980/__13.html
- § 14 UStG (Rechnung): https://www.gesetze-im-internet.de/ustg_1980/__14.html
- § 15 UStG (Vorsteuerabzug): https://www.gesetze-im-internet.de/ustg_1980/__15.html
- BFH V R 51/09 (Finanzierungsleasing USt): https://www.bfh.de
- Art. 135 MwStSystRL (USt-Befreiungen): https://eur-lex.europa.eu
- BMF-Schreiben Leasingerlasse: https://www.bundesfinanzministerium.de

## Output-Formate

- **USt-Qualifikationsmatrix**: Lieferung vs. sonstige Leistung je nach BMF-Erlass-Fallgruppe
- **Pflichtangaben-Checkliste**: § 14 IV UStG für Leasingrechnungen
- **Sonderzahlungs-Buchungsschema**: Anzahlung, USt, Vorsteuer
- **Dauerrechnung-Muster**: Monatliche Leasingrate mit korrekten Angaben

## 2. `lease-024-immobilienleasing-erbbaurecht-und-grundbuch`

**Fokus:** Immobilienleasing: Erbbaurecht, Grundbucheintragung, Bilanzierung, steuerliche Zurechnung und Besonderheiten gegenüber Mietkauf.

# Immobilienleasing: Erbbaurecht und Grundbuch

## Zweck

Beim Immobilienleasing werden Gewerbeimmobilien, Bürogebäude oder Produktionshallen geleast. Das Eigentumsrecht an Grundstücken ist deutlich komplexer als bei Mobilien: § 94 BGB (wesentliche Bestandteile), Grundbucheintragung und Erbbaurecht spielen eine zentrale Rolle.

## Rechtlicher Rahmen

- §§ 535 ff. BGB: Leasingvertrag als atypischer Mietvertrag
- § 94 BGB: Gebäude als wesentlicher Bestandteil des Grundstücks
- §§ 873, 925 BGB: Eigentumsübergang Grundstücke (Auflassung + Grundbucheintragung)
- ErbbauRG: Erbbaurecht als Alternative zu vollem Eigentum
- § 108 InsO: Leasingvertrag über unbewegliche Sachen läuft in Insolvenz fort
- BMF-Leasingerlasse (1971/1972): Gelten für Immobilienleasing mit Anpassungen
- IFRS 16: Aktivierungspflicht auch für Immobilien

## Eigentumsstruktur

### Voller Eigentumsübergang (LG kauft Grundstück)
- LG erwirbt Grundstück von Lieferant/Verkäufer
- Eigentumsübergang: Auflassung (§ 925 BGB) + Grundbucheintragung (§ 873 BGB)
- LG ist im Grundbuch als Eigentümer eingetragen
- LN erhält schuldrechtliches Nutzungsrecht (Leasingvertrag)

### Erbbaurecht
- Alternative: LG erwirbt Erbbaurecht (§§ 1 ff. ErbbauRG)
- Erbbaurecht im Grundbuch eingetragen (Erbbaugrundbuch)
- LG wird Inhaber des Erbbaurechts; Grundeigentümer (Gemeinde, Kirche etc.) behält Grundstück
- Vorteil: Geringere Investitionskosten für LG

### LN-Nutzungsrecht
- Schuldrechtliches Nutzungsrecht aus Leasingvertrag; nicht im Grundbuch
- § 108 InsO: Bei Insolvenz LN läuft Vertrag fort; bei Insolvenz LG auch

## Grundbuch und Absicherung des LN

### Vormerkung (§ 883 BGB)
- LN kann sich eine Auflassungsvormerkung ins Grundbuch eintragen lassen, wenn im Vertrag eine Kaufoption vereinbart ist
- Schutz vor Veräußerung an Dritte

### Dienstbarkeit
- Beschränkte persönliche Dienstbarkeit (§ 1090 BGB) oder Grunddienstbarkeit (§ 1018 BGB) zugunsten des LN möglich
- Dingliches Nutzungsrecht: stärker als schuldrechtlicher Vertrag; überdauert Eigentümerwechsel

## Bilanzierung: Immobilienleasing

### HGB (BMF-Erlass, § 39 AO)
- Wie bei Mobilienleasing: wirtschaftliches Eigentum bestimmt Bilanzierung
- BMF-Sondererlasse für Immobilien: Eigenheiten bei Grundstück (kein AfA auf Grund und Boden) vs. Gebäude

### IFRS 16
- Immobilien-Leasingverträge: Vollständige Aktivierung als RoU-Asset und Verbindlichkeit
- Keine Ausnahme für Immobilien (auch keine geringwertige Ausnahme)
- Besonders relevant für Einzelhandel (viele Filialmietverträge), Bürogebäude, Lager

## Steuerliche Besonderheiten

- AfA auf Gebäude: § 7 IV EStG: 3 % (Gebäude nach 31.12.2022), 2,5 % (davor); auf Anschaffungskosten
- Grund und Boden: Keine AfA (§ 11c EStDV)
- Wirtschaftliches Eigentum beim LN: LN nimmt Gebäude-AfA vor
- Vermietung eines Gebäudes durch LG: Grundsätzlich steuerpflichtig; Option zur USt nach § 9 UStG

## Insolvenz: § 108 InsO Immobilien

§ 108 I InsO: Mietverhältnisse über unbewegliche Sachen laufen mit Wirkung für die Masse fort, wenn Insolvenzeröffnung nach Übergabe. **Wichtige Schutzwirkung für LN**: Auch wenn LG insolvent ist, läuft Leasingvertrag über das Gebäude fort → LN kann das Gebäude weiter nutzen.

Einschränkung: Wenn Refinanzierer Grundschuld oder Hypothek hat (§§ 1113 ff. BGB) und LN kein dingliches Nutzungsrecht → Refinanzierer kann nach Zwangsversteigerung Räumung verlangen.

## Prüfprogramm

1. Grundbucheintragung: Wer ist Eigentümer? Erbbaurecht vorhanden?
2. Nutzungsrecht LN: Schuldrechtlich oder dinglich (Dienstbarkeit, Vormerkung)?
3. Bilanzierung: BMF-Erlass (wirtschaftliches Eigentum) oder IFRS 16?
4. § 108 InsO: Schutz des LN bei Insolvenz LG?
5. AfA: Gebäude vs. Grund/Boden; wer nimmt AfA?
6. Grundpfandrecht: Rangverhältnis zu Refinanzierer-Grundschuld?

## Typische Fallen

- Keine Absicherung des LN im Grundbuch → Kauf durch Dritte gefährdet Nutzungsrecht
- § 108 InsO: Verwalter kündigt Leasingvertrag über Immobilie ohne Beachtung der InsO-Schutzregel
- AfA auf Grund und Boden irrtümlich mitgenommen → steuerliche Korrektur
- Erbbaurecht: Erbbauzins-Erhöhungsklausel übersehen → Kostensteigerung

## Normen und Quellen

- § 94 BGB: https://dejure.org/gesetze/BGB/94.html
- §§ 873, 925 BGB (Eigentumsübergang Grundstück): https://dejure.org/gesetze/BGB/873.html
- ErbbauRG: https://www.gesetze-im-internet.de/erbbaureg/
- § 883 BGB (Vormerkung): https://dejure.org/gesetze/BGB/883.html
- § 108 InsO: https://www.gesetze-im-internet.de/inso/__108.html
- § 7 EStG (AfA Gebäude): https://www.gesetze-im-internet.de/estg/__7.html
- IFRS 16: https://eur-lex.europa.eu

## Output-Formate

- **Eigentumsstruktur-Diagramm**: LG, LN, Grundbuch, Erbbaurecht
- **Grundbuch-Check**: Eigentümer, Lasten, Vormerkung, Grundpfandrechte
- **IFRS-16-Immobilien**: Erstansatz, RoU, Leasingverbindlichkeit
- **AfA-Berechnung**: Gebäude vs. Grund/Boden, Aufteilung

## 3. `lease-027-grenzueberschreitendes-leasing-unidroit-und-rechtswahl`

**Fokus:** Grenzüberschreitendes Leasing: UNIDROIT-Übereinkommen, Rechtswahl (Rom I-VO), internationales Mobiliar-Leasingrecht, Steuerstrukturierung und Valutafragen.

# Grenzüberschreitendes Leasing: UNIDROIT und Rechtswahl

## Zweck

Wenn Leasinggeber und Leasingnehmer in verschiedenen Ländern ansässig sind, oder das Leasingobjekt grenzüberschreitend bewegt wird, stellen sich Kollisionsrechts- und Vertragsfragen. Dieser Skill analysiert das UNIDROIT-Übereinkommen, die Rechtswahl nach Rom I-VO und steuerliche Gestaltungsoptionen.

## UNIDROIT-Übereinkommen über internationales Finanzierungsleasing (Ottawa, 1988)

### Anwendungsbereich
- UNIDROIT-Übereinkommen: Gilt für Finanzierungsleasing, wenn LG und LN in verschiedenen Vertragsstaaten ansässig sind
- Deutschland ist kein Vertragsstaat → gilt nur, wenn Parteien Recht eines Vertragsstaats gewählt haben (z.B. England bis Brexit, Frankreich, USA/einzelne Staaten)
- Regelt: Rechte und Pflichten aus Leasingdreieck (Lieferant, LG, LN)

### Kernregeln UNIDROIT
- Art. 8: LN kann Ansprüche gegen Lieferant direkt geltend machen (wie §398 BGB)
- Art. 10: LN trägt Gefahrübergang wie Käufer
- Art. 13: Kündigung bei Nichterfüllung; Schadensersatz

## Rechtswahl nach Rom I-VO (EG 593/2008)

### Grundsatz: Freie Rechtswahl (Art. 3 Rom I-VO)
- Parteien können das anwendbare Recht frei wählen
- Empfehlung für internationale Leasingverträge: Wahl des Rechts eines Landes mit gut entwickeltem Leasingrecht (England/New York für Finanzierungs-Leasing; Deutschland für EU-Vertragspartner)

### Einschränkungen
- Verbraucher: Art. 6 Rom I-VO: Schutzrecht des Verbrauchers aus seinem Heimatland kann nicht abbedungen werden
- Zwingende Bestimmungen: Bestimmte Schutznormen (Verbraucherrecht, Arbeitsrecht) bleiben trotz Rechtswahl anwendbar (Art. 9 Rom I-VO)

### Anwendbares Recht ohne Rechtswahl (Art. 4 Rom I-VO)
- Leasingvertrag = Dienstleistungsvertrag → Recht des charakteristischen Leistungserbringers (LG) gilt
- LG in Deutschland → deutsches Recht anwendbar

## Internationaler Zahlungsverkehr

### Währungsrisiko
- Leasingrate in Fremdwährung (z.B. USD): LN trägt Währungsrisiko
- Absicherung: Devisentermingeschäfte, Währungsklausel im Vertrag

### Steuerstrukturierung: Cross-Border-Leasing

#### Typische Struktur
- LG in Niedrigsteuerland (z.B. Irland für Flugzeuge, Luxemburg für Finanzinstrumente)
- LN in Hochsteuerland: Leasingraten als Betriebsausgabe
- LG nutzt günstige Steuerregime; Steuervorteil geteilt

#### Risiken
- Doppelbesteuerungsabkommen (DBA): Quellensteuer auf Leasingraten?
- BEPS (Base Erosion and Profit Shifting, OECD): Anti-Gestaltungs-Regeln; Country-by-Country-Reporting
- § 8b KStG, §§ 1 ff. AStG: Verrechnungspreise bei Konzernleasing

### Zollrecht
- Grenzüberschreitende Verbringung von Leasingobjekten: Zollanmeldung erforderlich
- ATA-Carnet: Temporäre Einfuhr ohne Zoll (für Ausstellungen, vorübergehende Nutzung)
- Bei Finanzierungsleasing: Zoll auf Einfuhrwert bei Gestellung im Geltungsgebiet

## Insolvenz: Grenzüberschreitend

- EuInsVO (EG 2015/848): Hauptinsolvenzverfahren am Ort des COMI (Centre of Main Interests)
- Anerkennungspflicht in EU-Staaten
- Drittstaaten-Insolvenz: Anerkennung nach § 343 InsO

## Prüfprogramm

1. Wo sind LG und LN ansässig? UNIDROIT anwendbar?
2. Rechtswahlklausel: Welches Recht, warum?
3. Verbraucherleasing: Art. 6 Rom I-VO – Heimatrecht des Verbrauchers beachtet?
4. Währungsrisiko: Absicherung vereinbart?
5. Steuerstruktur: DBA-Quellensteuer? BEPS-Risiken?
6. Zollrecht: Einfuhr, temporäre Verbringung, ATA-Carnet?

## Typische Fallen

- Keine Rechtswahlklausel → Recht des LG-Landes gilt (möglicherweise unbekanntes Recht)
- Verbraucher im Ausland: Heimatrecht schützt ihn stärker → AGB des LG unwirksam
- Quellensteuer auf Leasingraten nicht eingeplant → Renditeminderung
- ATA-Carnet abgelaufen: Leasingobjekt im Ausland → Zollrisiko

## Normen und Quellen

- UNIDROIT Ottawa Convention 1988: https://www.unidroit.org
- Rom I-VO (EG 593/2008): https://eur-lex.europa.eu
- EuInsVO (EG 2015/848): https://eur-lex.europa.eu
- BEPS-Aktionsplan (OECD): https://www.oecd.org
- § 343 InsO (Ausländisches Insolvenzverfahren): https://www.gesetze-im-internet.de/inso/__343.html
- ATA-Carnet: https://www.ihk.de

## Output-Formate

- **Rechtswahl-Klausel-Muster**: Für internationale Leasingverträge
- **DBA-Quellensteuer-Matrix**: Ländervergleich für typische Leasingstruktur
- **Zoll-Checkliste**: Grenzüberschreitende Verbringung von Leasingobjekten
- **BEPS-Risikobewertung**: Konzernleasing und Verrechnungspreise
