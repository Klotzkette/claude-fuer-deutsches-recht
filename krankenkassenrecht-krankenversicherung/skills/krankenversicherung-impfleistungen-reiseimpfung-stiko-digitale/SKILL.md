---
name: krankenversicherung-impfleistungen-reiseimpfung-stiko-digitale
description: "Impfleistungen Reiseimpfung Stiko Digitale: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Impfleistungen Reiseimpfung Stiko Digitale

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Impfleistungen Reiseimpfung Stiko Digitale** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-050-impfleistungen-reiseimpfung-und-stiko` | GKV-Impfleistungen: STIKO-Empfehlungen (§ 20i SGB V), Reiseimpfungen als Satzungsleistung, Off-STIKO-Impfungen und Widerspruch bei Ablehnung. |
| `kv-051-digitale-gesundheitsanwendungen-diga-antrag-und-erprobung` | GKV-Leistungsanspruch auf DiGA (§ 33a SGB V): Verzeichnis, Verordnung, Freischaltung, Erprobungsphase und Nutzenbewertung durch BfArM. |
| `kv-052-telemedizin-epa-erezept-und-datenschutz` | Digitalisierung im Gesundheitswesen: Telemedizin, elektronische Patientenakte (ePA), elektronisches Rezept (eRezept) – GKV-Leistungsrahmen, Datenschutz und Opt-out. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Impfleistungen Reiseimpfung Stiko Digitale**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-050-impfleistungen-reiseimpfung-und-stiko`

**Fokus:** GKV-Impfleistungen: STIKO-Empfehlungen (§ 20i SGB V), Reiseimpfungen als Satzungsleistung, Off-STIKO-Impfungen und Widerspruch bei Ablehnung.

# Impfleistungen: Reiseimpfung und STIKO

## Skill-Zweck

GKV übernimmt Kosten für Schutzimpfungen nach STIKO-Empfehlung. Dieser Skill klärt **welche Impfungen die GKV zahlen muss, welche nur freiwillig angeboten werden und wie Reiseimpfungen abrechnungsfähig sind**.

## Rechtlicher Rahmen

- **§ 20i SGB V** – Schutzimpfungen: GKV zahlt STIKO-Empfehlungen vollständig
- **§ 11 Abs. 6 SGB V** – Satzungsleistungen: Kasse kann Reiseimpfungen freiwillig anbieten
- **§ 92 SGB V i.V.m. Schutzimpfungs-Richtlinie (SI-RL) des G-BA**
- **§ 20 IfSG** – Impfpflicht in bestimmten Einrichtungen (Masern seit 2020)
- **STIKO (Ständige Impfkommission)** – Empfehlungen im Bundesgesundheitsblatt
- BSG B 1 KR 16/23 R (Impfanspruch), BSG B 1 KR 13/18 R

## STIKO-Empfehlungen: GKV-Pflichtleistungen

| Impfung | GKV-Pflichtleistung | STIKO-Empfehlung |
|---------|---------------------|------------------|
| Tetanus, Diphtherie, Polio | Ja | Grundimmunisierung + Auffrischung |
| Masern, Mumps, Röteln (MMR) | Ja | 2 Dosen Kindesalter |
| HPV | Ja (Mädchen + Jungen 9–14) | Seit 2022 auch Jungen |
| FSME | Ja in Risikogebieten | STIKO-Karte beachten |
| Grippeimpfung | Ja für Risikogruppen | Ältere, Chroniker |
| Hepatitis B | Ja (Grundimmunisierung Kind) | Mehrere Dosierungen |

## Prüfprogramm

### Schritt 1 – STIKO-Empfehlung prüfen
- Aktuelle STIKO-Empfehlung (Bundesgesundheitsblatt): Ist die Impfung empfohlen?
- Schutzimpfungs-Richtlinie G-BA: setzt STIKO-Empfehlungen in GKV-Leistungen um
- GKV muss zahlen wenn STIKO-Empfehlung und SI-RL-Auflistung vorhanden

### Schritt 2 – Reiseimpfungen
- Grundsätzlich KEINE GKV-Pflichtleistung (keine STIKO-Empfehlung als Standardimpfung)
- Manche Kassen als Satzungsleistung: Gelbfieber, Typhus, Hepatitis A für Risikogebiete
- Antrag an Kasse: Informationen über Reiseziel, Risikoeinschätzung
- Tropenmedizinische Beratung: häufig GKV-Leistung (§ 27 SGB V, § 20 SGB V)

### Schritt 3 – Ablehnung einer STIKO-Impfung
- Kasse lehnt STIKO-Empfehlung ab: rechtswidrig; Widerspruch sofort
- SI-RL des G-BA ist verbindlich; Kasse hat kein Ermessen bei STIKO-Leistungen
- Auffrischimpfungen: ebenfalls GKV-Leistung wenn STIKO empfiehlt

### Schritt 4 – Masernimpfpflicht (§ 20 IfSG)
- Masernimpfpflicht für Kinder und Betreuungspersonal seit März 2020
- GKV zahlt Impfung; Nachweispflicht gegenüber Einrichtung
- Bei Verweigerung: Bußgeld und Ausschluss aus Einrichtung

### Schritt 5 – Impfschaden
- Impfschaden-Entschädigung: § 60 IfSG, nicht GKV-Leistung
- Zuständig: Versorgungsamt
- GKV bleibt für Behandlungskosten des Impfschadens zuständig (§ 27 SGB V)

## Typische Fallen

- **STIKO-Empfehlung neu, GKV noch nicht angepasst**: SI-RL kann zeitlicher Nachlauf haben; BSG verpflichtet Kasse trotzdem zu leisten wenn STIKO-Empfehlung vorliegt.
- **Privatarzt rechnet GOÄ ab**: Kassenarzt rechnet Impfung direkt mit Kasse ab; Privatarzt-Impfung muss Versicherter zunächst selbst zahlen und dann Erstattung beantragen.
- **HPV bei Jungen**: Seit 2022 STIKO-Empfehlung auch für Jungen 9–14; GKV muss zahlen.
- **Auffrischung nach Auslandsaufenthalt**: Auch bei Rückkehr aus Endemiegebiet kann Auffrischung STIKO-empfohlen sein.

## Output-Formate

- Impfanspruchs-Checkliste (STIKO vs. Satzung)
- Widerspruch gegen Impfablehnungsbescheid
- Reiseimpfungs-Satzungsleistungs-Antrag
- Masernimpfpflicht-Nachweisprotokoll
- Impfschaden-Anzeige (IfSG)

## Quellen

- [§ 20i SGB V – Schutzimpfungen](https://www.gesetze-im-internet.de/sgb_5/__20i.html)
- [Schutzimpfungs-Richtlinie G-BA](https://www.g-ba.de/richtlinien/60/)
- [STIKO – Robert Koch-Institut](https://www.rki.de/DE/Content/Infekt/Impfen/STIKO/stiko_node.html)
- [§ 60 IfSG – Impfschaden](https://www.gesetze-im-internet.de/ifsg/__60.html)
- [BSG Impfrechtsprechung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 20i SGB V](https://dejure.org/gesetze/SGB_V/20i.html)

## 2. `kv-051-digitale-gesundheitsanwendungen-diga-antrag-und-erprobung`

**Fokus:** GKV-Leistungsanspruch auf DiGA (§ 33a SGB V): Verzeichnis, Verordnung, Freischaltung, Erprobungsphase und Nutzenbewertung durch BfArM.

# Digitale Gesundheitsanwendungen (DiGA): Antrag und Erprobung

## Skill-Zweck

Digitale Gesundheitsanwendungen (DiGA) sind Apps auf Rezept. Dieser Skill klärt **Anspruchsvoraussetzungen, Verordnungsverfahren, Freischaltung durch die Kasse und den Erprobungsprozess**.

## Rechtlicher Rahmen

- **§ 33a SGB V** – DiGA: Anspruch auf digitale Gesundheitsanwendungen
- **§ 139e SGB V** – DiGA-Verzeichnis des BfArM
- **DiGAV** (Digitale-Gesundheitsanwendungen-Verordnung) – Anforderungen und Zulassung
- **§ 92 SGB V** – G-BA: keine eigene DiGA-Richtlinie (Verzeichnis des BfArM maßgeblich)
- BfArM (Bundesinstitut für Arzneimittel und Medizinprodukte): führt DiGA-Verzeichnis
- BSG B 1 KR 3/24 R (DiGA, erster ausstehender BSG-Entscheid)

## DiGA-Systematik

| Phase | Inhalt | Verzeichnisstatus |
|-------|--------|------------------|
| Vorläufige Aufnahme (Erprobung) | 12 Monate; Hersteller muss Nutzenbeweis erbringen | Verzeichnis „vorläufig" |
| Dauerhafte Aufnahme | Positiver Nutzennachweis; oder weiterhin Erprobung | Verzeichnis „dauerhaft" |
| Streichung | Kein Nutzennachweis; Listung endet | Aus Verzeichnis entfernt |

## Prüfprogramm

### Schritt 1 – DiGA im Verzeichnis?
- BfArM-DiGA-Verzeichnis online: aktuelle Liste aller zugelassenen DiGA
- Vorläufig oder dauerhaft? → Beide GKV-erstattungsfähig
- Diagnose: für welche Indikation ist die DiGA zugelassen?

### Schritt 2 – Verordnung
- Verordnungsrecht: Arzt oder Psychotherapeut (Kassenzulassung)
- Formular: Spezialverordnungs-Formular oder auf Standardrezept mit ICD-10
- Einlösecode auf Rezept: für App-Freischaltung erforderlich

### Schritt 3 – Genehmigung durch Kasse
- § 33a Abs. 2: Kasse muss DiGA genehmigen wenn im Verzeichnis und Verordnung vorliegt
- 14-Tage-Frist für Kasse; danach Genehmigungsfiktion (§ 13 Abs. 3a SGB V analog)
- Kasse stellt Freischaltcode aus; Versicherter gibt Code in App ein

### Schritt 4 – Zuzahlung
- 10 % je DiGA, mind. 5 €, max. 10 € (wie andere GKV-Leistungen)
- Befreiungsgrenze: Belastungsgrenze 2 % des Bruttoeinkommens (§ 62 SGB V)

### Schritt 5 – DiGA-Erprobungsphase
- Hersteller muss in 12-monatiger Erprobungsphase Nutzendaten liefern
- Kasse zahlt in Erprobungsphase; auch wenn Nutzenbeweis noch aussteht
- Keine Erstattung nach Streichung aus Verzeichnis

## Typische Fallen

- **Veraltetes Verzeichnis**: BfArM aktualisiert laufend; vor Verordnung aktuellen Stand prüfen.
- **Off-Label DiGA**: DiGA für andere als zugelassene Indikation verordnet → Kasse kann ablehnen.
- **Datenschutz in DiGA**: Gesundheitsdaten verarbeitet; DSGVO; BfArM prüft bei Zulassung; Versicherter muss Einwilligung geben.
- **Interoperabilität ePA**: DiGA kann Daten in ePA übertragen; opt-in durch Versicherten.

## Output-Formate

- DiGA-Verordnungsanleitung (für Arzt)
- Genehmigungsantrag Kasse
- Widerspruch gegen DiGA-Ablehnung
- Genehmigungsfiktion-Schreiben
- DiGA-Datenschutzcheckliste

## Quellen

- [§ 33a SGB V – DiGA](https://www.gesetze-im-internet.de/sgb_5/__33a.html)
- [§ 139e SGB V – DiGA-Verzeichnis](https://www.gesetze-im-internet.de/sgb_5/__139e.html)
- [BfArM DiGA-Verzeichnis](https://diga.bfarm.de/de/verzeichnis)
- [DiGAV – Zulassungsverordnung](https://www.gesetze-im-internet.de/digav/)
- [dejure.org § 33a SGB V](https://dejure.org/gesetze/SGB_V/33a.html)
- [GKV-Spitzenverband DiGA](https://www.gkv-spitzenverband.de)
## Schritt 5 – Widerspruch bei Ablehnung einer DiGA

- Krankenkasse muss innerhalb von 3 Wochen über DiGA-Antrag entscheiden (§ 33a Abs. 4 SGB V)
- Ablehnungsgründe: DiGA nicht im BfArM-Verzeichnis, kein ärztliches/psychotherapeutisches Votum, Indikation nicht erfüllt
- Widerspruch: Ärztliche Verordnung + Diagnosebeleg beifügen
- Bei Erprobungs-DiGA: Zusatznutzen noch nicht belegt, aber Anspruch trotzdem bei Vorliegen der Voraussetzungen

## Weiterführende Quellen

- [§ 33a SGB V – Digitale Gesundheitsanwendungen](https://www.gesetze-im-internet.de/sgb_5/__33a.html)
- [BfArM – DiGA-Verzeichnis](https://diga.bfarm.de/de/verzeichnis)
- [G-BA – DiGA-Richtlinie](https://www.g-ba.de/richtlinien/107/)
- [GKV-Spitzenverband – DiGA-Informationen](https://www.gkv-spitzenverband.de)

## 3. `kv-052-telemedizin-epa-erezept-und-datenschutz`

**Fokus:** Digitalisierung im Gesundheitswesen: Telemedizin, elektronische Patientenakte (ePA), elektronisches Rezept (eRezept) – GKV-Leistungsrahmen, Datenschutz und Opt-out.

# Telemedizin, ePA, eRezept und Datenschutz

## Skill-Zweck

Die Digitalisierung verändert das Krankenversicherungsrecht. Dieser Skill klärt **Telemedizin-Leistungsrahmen, ePA-Regelungen und eRezept-Prozesse** mit besonderem Fokus auf Datenschutz und Opt-out-Rechte.

## Rechtlicher Rahmen

- **§ 291a SGB V** – Telematik-Infrastruktur (TI): Grundlage für ePA, eRezept
- **§ 341 SGB V** – Elektronische Patientenakte (ePA): opt-out ab 2025
- **§ 360 SGB V** – eRezept: Pflicht für GKV-Arzneiverordnungen
- **§ 27 SGB V** – Telemedizin als Krankenbehandlungsform
- **§ 87 SGB V i.V.m. EBM** – Vergütung von Videosprechstunden
- DSGVO Art. 9, BDSG, TSVG (Terminservice- und Versorgungsgesetz 2019)
- BfDI Stellungnahmen zur ePA

## Digitale Versorgungsstruktur

| Element | Rechtsgrundlage | Opt-out möglich |
|---------|-----------------|-----------------|
| ePA (Elektronische Patientenakte) | § 341 SGB V (ab 2025 opt-out) | Ja, Widerspruch jederzeit |
| eRezept | § 360 SGB V | Nein (Pflicht für Arzt) |
| Videosprechstunde | § 87 SGB V, EBM | Ja (Versicherter wählt) |
| eArztbrief | § 291a SGB V | Ja |
| DiGA | § 33a SGB V | Ja (separate Einwilligung) |

## Prüfprogramm

### Schritt 1 – Elektronische Patientenakte (ePA)
- Ab 2025: alle GKV-Versicherten erhalten automatisch ePA (opt-out-Modell)
- Widerspruch: schriftlich an Krankenkasse; kein Grund erforderlich
- Inhalt: Befunde, Diagnosen, Medikationspläne, DiGA-Daten, Mutterpass etc.
- Zugriff: Patient kontrolliert Zugriffsrechte (App der Kasse oder Kiosk-System)

### Schritt 2 – eRezept
- Pflicht für alle GKV-Arzneiverordnungen seit 2024
- Einlösung: Apotheke scannt QR-Code (Papierausdruck oder App)
- Datenschutz: Rezeptdaten zentral gespeichert; Zugriff für Abrechnung und ggf. Auswertung
- Verweigerungsrecht: Versicherter kann analoge Alternative anfordern (wenn technisch nicht möglich)

### Schritt 3 – Videosprechstunde
- GKV-Leistung: Arzt-Patienten-Videokontakt (EBM-Ziffer 01439)
- Plattformzulassung: nur von KBV zertifizierte Anbieter
- Ausnahmen: nicht für erstmaligen Arzt-Patienten-Kontakt (§ 7 Abs. 4 MBOÄ)
- Datenschutz: Ende-zu-Ende-Verschlüsselung erforderlich; DSGVO-Konformität der Plattform

### Schritt 4 – Datenschutz und Opt-out
- Widerspruch ePA: schriftlich, begründungslos, jederzeit widerrufbar
- Datenzugang Dritte (Forschung): pseudonymisiert; Versicherter muss nicht aktiv zustimmen aber kann widersprechen
- Kassenaufsicht (BAS): Aufsicht über Datenschutz bei Kassen (Sozialdaten)
- BfDI: zuständig für föderalen Datenschutz

### Schritt 5 – Telemedizin im Leistungsrecht
- Telemedizinische Behandlung: voller GKV-Leistungsanspruch (§ 27 SGB V)
- Einschränkung: nicht alle Diagnosen telemedizinisch behandelbar; Arzt entscheidet
- Telemonitoring: chronisch kranke Patienten (Herzinsuffizienz: § 137f SGB V)

## Typische Fallen

- **ePA und Arbeitgeber**: Arbeitgeber hat keinen Zugang zur ePA; strikte Trennung.
- **eRezept und Notfall**: Bei Systemausfall Papierrezept als Ersatz; Apotheke kann auf Bedenken reagieren.
- **Videosprechstunde-Plattform nicht zertifiziert**: Arzt haftet bei Nutzung nicht zugelassener Plattform; für Versicherten kein Problem.
- **DiGA-Daten in ePA**: Nur mit expliziter Einwilligung; separates Opt-in erforderlich.

## Output-Formate

- ePA-Widerspruchsschreiben
- Datenschutzerklärung-Checkliste (Telemedizin)
- Videosprechstunden-Einverständnis-Muster
- eRezept-Erklärung (Laienerklärung)
- Kassenaufsichts-Beschwerde (Datenschutz)

## Quellen

- [§ 341 SGB V – ePA](https://www.gesetze-im-internet.de/sgb_5/__341.html)
- [§ 360 SGB V – eRezept](https://www.gesetze-im-internet.de/sgb_5/__360.html)
- [Gematik – ePA und eRezept](https://www.gematik.de)
- [BfDI – Datenschutz Gesundheit](https://www.bfdi.bund.de)
- [dejure.org § 291a SGB V](https://dejure.org/gesetze/SGB_V/291a.html)
- [DSGVO Art. 9](https://dsgvo-gesetz.de/art-9-dsgvo/)
