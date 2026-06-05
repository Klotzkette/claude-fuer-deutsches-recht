---
name: alkohol-drogen-beweisverwertung
description: "Alkohol Drogen Beweisverwertung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Alkohol Drogen Beweisverwertung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Alkohol Drogen Beweisverwertung** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehrsowi-alkohol-drogen-24a` | Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis THC/Kokain/Amphetamin), § 81a StPO (Blutprobe), § 316 StGB (Trunkenheit im Verkehr Abgrenzung). Prüfraster: Toleranzwerte, analytische Nachweisgrenze vs. Wirkung, Blutprobe-Anforderung ordnungsgemäß, Fahrerlaubnis-Konsequenzen § 69 StGB. Output Einspruchs-Strategie, Beweisverwertungs-Antrag. Abgrenzung: Strafrecht § 316 StGB siehe fachanwalt-strafrecht-Plugin; Fahrerlaubnisentzug VwR siehe fachanwalt-verwaltungsrecht-Plugin. |
| `verkehrsowi-beweisverwertung-standardisiert` | Prüffeld für verkehrsowi beweisverwertung standardisiert: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `verkehrsowi-fahreridentifizierung` | Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG (Aussageverweigerungsrecht). Prüfraster: Lichtbildabgleich AG, Sachverständigen-Antrag Biometrie, kein Zwang zur Fahrernennung, Fahrtenbuchauflage-Risiko. Output Verteidigungsstrategie Fahreridentifikation, Sachverständigen-Antrag. Abgrenzung: Beweisauswertung Messbeamter siehe verkehrsowi-zeugen-polizei-strategie; HV-Vorbereitung siehe verkehrsowi-hauptverhandlung-amtsgericht. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Alkohol Drogen Beweisverwertung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehrsowi-alkohol-drogen-24a`

**Fokus:** Alkohol- und Drogen-OWi verteidigen: Mandant hat Bußgeldbescheid wegen 0.5-Promille oder Drogennachweis erhalten. Normen: § 24a Abs. 1 StVG (0.5-Promille-Grenze), § 24a Abs. 2 StVG (Wirkstoffnachweis THC/Kokain/Amphetamin), § 81a StPO (Blutprobe), § 316 StGB (Trunkenheit im Verkehr Abgrenzung). Prüfraster: Toleranzwerte, analytische Nachweisgrenze vs. Wirkung, Blutprobe-Anforderung ordnungsgemäß, Fahrerlaubnis-Konsequenzen § 69 StGB. Output Einspruchs-Strategie, Beweisverwertungs-Antrag. Abgrenzung: Strafrecht § 316 StGB siehe fachanwalt-strafrecht-Plugin; Fahrerlaubnisentzug VwR siehe fachanwalt-verwaltungsrecht-Plugin.

# Alkohol und Drogen — § 24a StVG

## Triage zu Beginn

1. **Alkohol oder Drogen?** — § 24a Abs. 1 StVG: 0,5 Promille-Grenze (Atemalkohol 0,25 mg/l); § 24a Abs. 2 StVG: Drogen-Wirkstoffnachweis.
2. **BAK-Wert oder Atemalkohol-Wert?** — Atemalkohol-Wert (AAK): 0,25 mg/l = OWi; ab 0,50 mg/l AAK oder BAK 1,1 Promille bei Ausfallerscheinungen = § 316 StGB (Strafrecht!).
3. **Blutprobe entnommen?** — Zeitpunkt der Entnahme nach Fahrtende relevant; Rueckrechnung auf Fahrzeitpunkt.
4. **Bei Drogen:** Welcher Stoff? THC, Kokain, Amphetamin — unterschiedliche analytische Grenzwerte.
5. **Fahrerlaubnis-Konsequenzen?** — § 69 Abs. 2 StGB-Regelfall bei § 316 StGB; im OWi-Bereich Fahrverbot nach § 25 StVG.

## Zentrale Normen (Stand Mai 2026)

- **§ 24a Abs. 1 StVG** — Alkohol-OWi: Atemalkohol 0.25 mg/l oder mehr; oder BAK 0.5 Promille oder mehr
- **§ 24a Abs. 1a StVG** — THC-Grenzwert 3.5 ng/ml im Blutserum (in Kraft seit 22.8.2024, BGBl. I 2024 Nr. 274)
- **§ 24a Abs. 2 StVG** — Drogen-OWi: Fahren unter Einfluss von in Anlage zu § 24a StVG genannten Substanzen (Kokain, Amphetamin, MDMA, Methamphetamin, Morphin u.a.)
- **§ 24a Abs. 3 StVG** — keine OWi wenn Drogeneinnahme nachweislich laenger zurueckliegt und keine Fahruntauglichkeit
- **§ 316 StGB** — Trunkenheitsfahrt: BAK ab 1.1 Promille (absolute Fahruntauglichkeit) oder ab 0.3 Promille mit Ausfallerscheinungen (relative Fahruntauglichkeit)
- **§ 315c StGB** — Gefährdung des Strassenverkehrs unter Alkohol
- **§ 81a StPO** — Blutentnahme durch Arzt; richterlicher Anordnungsvorbehalt
- **§ 69 Abs. 2 StGB** — Regelungeeignetheit bei § 316 StGB
- **§ 25 StVG** — Fahrverbot im OWi-Verfahren
- **KCanG** (Konsumcannabisgesetz vom 27.3.2024, BGBl. I 2024 Nr. 109) — Cannabis ab 1.4.2024 kein BtM mehr; medizinische Verwendung im MedCanG

## Aktuelle Rechtsprechung (Stand Mai 2026; offene Quellen)

- **BVerwG, Beschl. v. 8.1.2025, 3 B 2.24** — Cannabis ist seit KCanG (1.4.2024) kein BtM mehr; § 14 FeV im Lichte der neuen Gesetzeslage anzuwenden. Quelle: bverwg.de
- BGH 4. Strafsenat zu § 24a StVG und § 316 StGB: konkrete Aktenzeichen vor Versand in bundesgerichtshof.de oder dejure.org verifizieren.
- OLG-Linien zu Cannabis-Grenzwert und Trennungsfähigkeit: laufende Rechtsprechung 2025/2026 — vor Versand in openjur.de oder nrwe.de prüfen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Trennlinie OWi vs. Strafrecht

| Situation | Norm | Konsequenz |
|---------|------|-----------|
| AAK 0.25 bis 0.49 mg/l ohne Ausfallerscheinung | § 24a Abs. 1 StVG | OWi: Geldbusse + Fahrverbot 1-3 Monate |
| AAK ab 0.55 mg/l (BAK ab 1.1 Promille) OHNE Ausfall | § 316 StGB absolute Fahruntauglichkeit | Strafrecht: Geldstrafe + Fahrerlaubnis-Entzug |
| BAK ab 0.3 Promille MIT Ausfallerscheinung | § 316 StGB relative Fahruntauglichkeit | Strafrecht |
| BAK ab 1.6 Promille bei Wiederholung / Erstkontakt | § 316 StGB + MPU-Pflicht (§ 13 FeV) | Strafrecht, MPU-Pflicht |
| THC im Blutserum ab 3.5 ng/ml (seit 22.8.2024) | § 24a Abs. 1a StVG | OWi |
| Andere Drogen-Wirkstoffnachweis | § 24a Abs. 2 StVG | OWi |

## Schritt-fuer-Schritt-Workflow

1. **Sachverhalt aufnehmen:** AAK-Wert, BAK-Wert, Zeitpunkt der Atemtest/Blutentnahme, Fahrtende.
2. **Zuordnung OWi oder Strafrecht?** — Trennlinie klar definieren.
3. **Blutentnahme-Rechmaessigkeit pruefen:** Richteranordnung vorhanden? Gefahr im Verzug begruendet?
4. **Rueckrechnungspruefung:** Nachweis BAK/AAK korrekt auf Fahrzeitpunkt zurueckgerechnet?
5. **Bei Drogen:** Wirkstoff und Grenzwert pruefen; § 24a Abs. 3 StVG-Ausnahme pruefen.
6. **Fahrerlaubnis-Strategie:** Fahrverbot § 25 StVG vs. Entziehung § 69 StGB — getrennt bearbeiten.

## Harte Leitplanken

- BAK ab 1,6 Promille immer als Strafrecht behandeln — eigener Skill § 316 StGB.
- Blutentnahme-Rechtmaessigkeit aktiv pruefen — Verwertungsverbot argumentierbar.
- Rueckrechnung selbst kontrollieren; Fehler im Urteil sind Revisionsgruende.
- Anwaltliche Endkontrolle bei Abgrenzung OWi/Strafrecht.

## 2. `verkehrsowi-beweisverwertung-standardisiert`

**Fokus:** Prüffeld für verkehrsowi beweisverwertung standardisiert: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Standardisiertes Messverfahren und Beweisverwertung

## Triage zu Beginn

1. **Standardisiertes Messverfahren oder nicht?** — BGH unterscheidet standardisierte Verfahren (keine detaillierte Urteilsbegruendung notwendig) von nichtstandardisierten (vollstaendige Darlegung erforderlich). Grundsatzentscheidung BGHSt 39, 291 (1993) und Folgeentscheidungen — konkrete BGH-Aktenzeichen vor Versand in bundesgerichtshof.de oder dejure.org verifizieren.
2. **Welche konkreten Angriffspunkte auf die Messung gibt es?** — Pauschales Bestreiten genuegt nicht um das standardisierte Verfahren zu erschuettern.
3. **Rohmessdaten angefordert?** — BVerfG-Linie zum Recht auf Zugang zu vorhandenen Daten (Beschl. v. 12.11.2020, 2 BvR 1616/18; Beschl. v. 20.6.2023, 2 BvR 1167/20 — bundesverfassungsgericht.de).
4. **Sachverstaendigenantrag gestellt?** — § 77 Abs. 2 OWiG: Gericht darf nur ablehnen wenn Antrag missbräuchlich oder Beweisthema nicht entscheidungserheblich.
5. **Fahreridentifikation aus Messfoto eindeutig?** — Lichtbild-Qualitaet prufen; Sachverstaendiger fuer biometrischen Vergleich moeglich.

## Zentrale Normen

- **§ 77 OWiG** — Beweisaufnahme: Gericht darf und muss Beweise erheben wenn entscheidungserheblich
- **§ 77 Abs. 2 OWiG** — Ablehnung von Beweisantraegen nur aus enumerativen Gruenden
- **§ 71 OWiG i.V.m. § 261 StPO** — Freie Beweiswuerdigung
- **Art. 103 Abs. 1 GG** — Rechtliches Gehoer: Betroffener muss Beweise angreifen koennen
- **§ 6 MessEG** — Eichpflicht als Grundbedingung der Verwertbarkeit

## Aktuelle Rechtsprechung (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (Volltext vor Versand aufrufen):

- **BVerfG, Beschl. v. 12.11.2020, 2 BvR 1616/18** — Recht des Betroffenen auf Zugang zu vorhandenen Mess- und Begleitdaten als Ausfluss des fairen Verfahrens. Quelle: bundesverfassungsgericht.de
- **BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20** — Keine Pflicht zur Speicherung von Rohmessdaten beim standardisierten Verfahren (Leivtec XV3); Recht auf erweiterten Zugang besteht aber im Einzelfall. Quelle: bundesverfassungsgericht.de
- BGH-Linie zum standardisierten Messverfahren: BGHSt 39, 291 (1993). Aktualisierende OLG-Rechtsprechung in offenen Quellen (openjur.de, nrwe.de) verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Standardisierte Messverfahren — anerkannt in Deutschland

| Messgeraet | Verfahren |
|-----------|---------|
| ESO ES 3.0 | Lasermessung von hinten |
| TraffiStar S350 | Stationaere Radarueberwachung |
| PoliScan Speed | Laserscan-Verfahren |
| Riegl FG21-P | Handlaser-Messung |
| ProViDa | Nachfahren mit Polizeifahrzeug |
| TRAFFIPAX SpeedoPhot | Stationaere Blitzanlage |

## Angriffspunkte gegen die Verwertbarkeit

```
STANDARDISIERTES VERFAHREN ERSCHUETTERN:
1. Eichmangel: Eichschein abgelaufen oder Geraet nicht geeicht
2. Bedienungsfehler: Aufstellort nicht regelkonform
3. Mehrfachbelegung: Zwei Fahrzeuge im Messfeld
4. Reflexionen: Baeume, Schilder im Schussfeld des Lasers
5. Nachfahrmessung: Mindestabstand eingehalten? Geschwindigkeit konstant?

ROHMESSDATEN-PROBLEMATIK:
- Geraet speichert keine Rohmessdaten? → BVerfG 2020 zitieren
- Geraet speichert, aber Herausgabe verweigert? → Verwertungsverbot ruegen

FAHRERIDENTIFIKATION:
- Foto nicht eindeutig → Sachverstaendigen-Antrag Lichtbild-Identifikation
- Fahrerbestreitens → kein Auskunftszwang (§ 55 StPO)

SACHVERSTAENDIGENANTRAG (§ 77 Abs. 2 OWiG):
- Konkrete Angriffspunkte benennen: Eichfehler, Bedienungsfehler, Reflexion
- Antrag konkret: Sachverstaendiger fuer [GERAET], Beweisthema: [THEMA]
```

## Schritt-fuer-Schritt-Workflow

1. **Messgeraet und -verfahren identifizieren.**
2. **Angriffspunkte pruefen** (s. Checkliste).
3. **Rohmessdaten-Status feststellen** — angefordert? Vorhanden?
4. **Sachverstaendigenantrag konkret formulieren** wenn Angriffspunkte bestehen.
5. **In der Hauptverhandlung:** Beweisantrag § 77 OWiG stellen; bei Ablehnung: Gruende in das Protokoll aufnehmen lassen; Rechtsbeschwerde-Grundlage sichern.

## Harte Leitplanken

- Pauschal "Messung war falsch" genuegt nicht — konkrete Angriffspunkte notwendig.
- Sachverstaendigenantrag mit Beweisthema und Sachverstaendigenbezeichnung formulieren.
- Rohmessdaten-Anforderung immer schriftlich dokumentieren.
- Anwaltliche Endkontrolle bei Sachverstaendigenauswahl.

## 3. `verkehrsowi-fahreridentifizierung`

**Fokus:** Fahreridentifizierung im OWi-Verfahren angreifen oder verteidigen: Mandant bestreitet Fahrereigenschaft oder will Fahrer nicht nennen. Normen: § 31a StVG (Halter-Auskunftspflicht und Fahrtenbuchauflage), § 55 OWiG (Aussageverweigerungsrecht). Prüfraster: Lichtbildabgleich AG, Sachverständigen-Antrag Biometrie, kein Zwang zur Fahrernennung, Fahrtenbuchauflage-Risiko. Output Verteidigungsstrategie Fahreridentifikation, Sachverständigen-Antrag. Abgrenzung: Beweisauswertung Messbeamter siehe verkehrsowi-zeugen-polizei-strategie; HV-Vorbereitung siehe verkehrsowi-hauptverhandlung-amtsgericht.

# Fahreridentifizierung im OWi-Verfahren

## Triage zu Beginn

1. **Ist der Betroffene eindeutig auf dem Messfoto identifizierbar?** — Qualitaet des Fotos entscheidend; unklares Foto = Angriffspunkt.
2. **Hat der Betroffene sich bereits als Fahrer identifiziert?** — Anhoerungsbogen, Polizeivermerk, sonstige Aussagen.
3. **Ist die Halter-Auskunft (§ 31a StVG) bereits ergangen?** — Halter muss Auskunft geben; Fahrernennung ist freiwillig.
4. **Ist eine Fahrtenbuchauflage drohendes Thema?** — § 31a StVG: wenn Fahrer nicht ermittelt werden kann, kann Halter Fahrtenbuch fuehren muessen.
5. **Biometrischer Vergleich noetig?** — Sachverstaendiger wenn Foto-Identifikation streitig und fuer das Gericht nicht offenkundig.

## Zentrale Normen

- **§ 55 Abs. 1 OWiG** — Betroffener muss nicht zur Sache aussagen; kein Zwang zur Fahrernennung
- **§ 31a StVG** — Fahrtenbuchauflage: Halter, der Fahrerauskunft verweigert, kann Fahrtenbuchfuehrungs-Pflicht erhalten
- **§ 163b StPO i.V.m. § 46 OWiG** — Identitaetsfeststellung durch Polizei; begrenzt auf Personalien
- **§ 77 OWiG** — Beweisaufnahme: Sachverstaendiger fuer Lichtbild-Identifikation ist Beweisantrag
- **Art. 6 Abs. 1 EMRK** — Recht auf faires Verfahren; keine Pflicht zur Selbstbelastung
- **§ 261 StPO i.V.m. § 71 OWiG** — Freie Beweiswuerdigung; Richter darf Foto-Vergleich selbst vornehmen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Fahreridentifikation

```
Messfoto vorhanden?
├─ Qualitaet hoch, Fahrer eindeutig erkennbar
│ └─ Kein Angriffspunkt auf Identifikation; andere Strategie waehlen
├─ Qualitaet niedrig / Fahrer nicht eindeutig erkennbar
│ ├─ Sachverstaendigenantrag (§ 77 OWiG): "Lichtbild-Identifikation nicht moeglich"
│ └─ Bestreiten der Fahreridentitaet in der Hauptverhandlung
└─ Kein Messfoto (stationaere Anlage defekt / Video)
 └─ Fahreridentifikation durch andere Mittel pruefen (Zeugen, Protokoll)

Betroffener will nicht aussagen?
├─ § 55 OWiG: Schweigen ausdruecklich empfehlen
└─ Fahrtenbuchauflage-Risiko (§ 31a StVG) erklaeren
 └─ Halter muss abwaegen: OWi mit Fahrverbot vs. Fahrtenbuch 1-2 Jahre
```

## Fotoqualitatspruefung — Checkliste

```
□ Gesicht vollstaendig und frontal erkennbar?
□ Bildaufloesungnsstufe ausreichend?
□ Keine Ueberstrahlung / Spiegelreflektion im Bild?
□ Brillentraeger / Muetze / Maske als Identifikationshindernis?
□ Vergleichsbild fuer biometrischen Abgleich vorhanden?
□ Mehrere Personen im Fahrzeug — richtige Person identifiziert?
```

## Output-Template Sachverstaendigenantrag Lichtbild

```
In der Bussgeldsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Einholung eines Sachverstaendigen-Gutachtens
gemaess § 77 OWiG

Ich beantrage die Einholung eines Sachverstaendigen-Gutachtens
zur Frage, ob die auf dem Messfoto abgebildete Person identisch
ist mit dem Betroffenen [NAME].

Begruendung: Das vorliegende Messfoto weist [Bildqualitaetsmangel
beschreiben] auf. Eine laienhafte Beurteilung durch das Gericht
ist nicht ausreichend. [NAME] bestreitet, zum Tatzeitpunkt der
Fahrzeugfuehrer gewesen zu sein.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Fahreridentifikations-Zwang gibt es nicht — Schweigen ist legitim.
- Fahrtenbuchauflage dem Mandanten klar erklaeren — Konsequenz des Schweigens.
- Sachverstaendigenantrag bei schlechter Foto-Qualitaet stellen — nicht pauschal.
- Anwaltliche Endkontrolle bei Beweisantrag-Formulierung.
