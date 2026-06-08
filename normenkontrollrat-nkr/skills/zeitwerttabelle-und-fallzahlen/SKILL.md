---
name: zeitwerttabelle-und-fallzahlen
description: "Praxisleitfaden zu Zeitwerttabellen und Fallzahlenermittlung. Zeigt die Struktur der Leitfaden-Zeitwerttabelle die Komplexitaetsstufen die Standard-Lohnsaetze DESTATIS-Quellen die Datenwege zur Fallzahlenermittlung und die typischen Quellen (Statistisches Bundesamt Bundesregister Ressortdaten Branchenstatistiken). Mit Bezugsformeln und Quellenpfaden."
---

# NKR-Zeitwerttabelle und Fallzahlen

## Worum geht es konkret

Zwei Datenfundamente der SKM-Rechnung sind **Zeitwerte** (wie lange dauert eine Standardtaetigkeit?) und **Fallzahlen** (wie oft kommt die Pflicht zur Anwendung?). Beide haben standardisierte Quellen.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Stellungnahme prueft Datengrundlage
- Ressort gibt Zeitwerte ohne Quelle an
- Fallzahlenermittlung scheint zu hoch oder zu niedrig
- Suchen einer offiziellen Quelle

Rueckfrage nur wenn unklar: *"Geht es um Zeitwert oder Fallzahl oder beides?"*

## Rechtlicher und methodischer Rahmen

- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR), Kapitel Zeitwerttabellen
- **DESTATIS Verdienststrukturerhebung**
- **DESTATIS Personalstandstatistik** für Verwaltungslohnsaetze
- **OECD-SKM-Tool**

## Zeitwerttabelle — Struktur

Standardtaetigkeiten mit Zeitwerten (Beispiel-Strukturierung):

| Standardtaetigkeit | Zeit einfach | Zeit mittel | Zeit komplex |
|---|---|---|---|
| Information beschaffen / lesen | 5-10 min | 15-30 min | 45-90 min |
| Antrag ausfuellen / Bericht erstellen | 10-20 min | 30-60 min | 90-180 min |
| Daten verarbeiten | 10-20 min | 30-60 min | 90-240 min |
| Pruefen / Plausibilisieren | 5-15 min | 20-40 min | 60-120 min |
| Versand / Einreichung | 2-5 min | 5-15 min | 20-40 min |
| Archivierung | 2-5 min | 5-10 min | 10-20 min |

Hinweis: Die konkreten Zeitwerte sind aus der jeweils aktuellen Leitfaden-Tabelle zu uebernehmen.

## Lohnsaetze (Beispiel-Bandbreiten Stand 06/2026)

| Adressat | Lohnsatz Bandbreite |
|---|---|
| Buerger (Zeitkosten) | ca. 28 EUR/h |
| Wirtschaft einfache Taetigkeit | ca. 25-35 EUR/h |
| Wirtschaft mittlere Qualifikation | ca. 40-50 EUR/h |
| Wirtschaft hohe Qualifikation | ca. 60-100 EUR/h |
| Verwaltung mittlerer Dienst | ca. 50-60 EUR/h |
| Verwaltung gehobener Dienst | ca. 65-80 EUR/h |
| Verwaltung hoeherer Dienst | ca. 80-100 EUR/h |

Die konkreten Saetze sind aus der jeweils aktuellen DESTATIS-Tabelle und Leitfaden-Tabelle zu uebernehmen.

## Fallzahlenquellen

| Datenart | Quelle |
|---|---|
| Anzahl Unternehmen | Statistisches Bundesamt — Unternehmensregister |
| Anzahl Gesellschaften nach Rechtsform | Statistisches Bundesamt; Handelsregisterauszuege |
| Anzahl Buerger einer Personengruppe | DESTATIS Bevoelkerungsstatistik; Mikrozensus |
| Anzahl Antraege bei Behörden | Ressort-Statistiken, Geschaeftsstatistik |
| Anzahl Beschaeftigte je Branche | DESTATIS Erwerbstaetigenrechnung |
| Anzahl Verfahren bei Gerichten | Justizstatistik |

## Pruefraster / Schritt für Schritt

1. **Pflicht identifizieren** und Standardtaetigkeit zuordnen
2. **Komplexitaetsstufe** bestimmen (einfach / mittel / komplex)
3. **Zeitwert** aus Tabelle ablesen
4. **Lohnsatz** aus DESTATIS / Leitfaden
5. **Fallzahl** aus Statistik (mit Jahresangabe und Quellenpfad)
6. **Bandbreite** ausweisen bei Unsicherheit
7. **Quelle** dokumentieren (Vermerk in der Stellungnahme oder Anlage)
8. **Aktualitaet** pruefen (Statistikjahr vs. Bezugsjahr)

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Zeitwert ohne Quelle
- Fallzahl ohne Jahresangabe
- Statistik aelter als 5 Jahre ohne Begruendung
- Komplexitaetsstufe ohne Begruendung
- Lohnsatz frei gegriffen

## Trade-off-Matrix

| Datenstand | Behandlung |
|---|---|
| Aktuelle DESTATIS-Tabelle | ohne Vorbehalt |
| Aeltere Statistik (3-5 Jahre) | mit Hinweis auf Stand |
| Schaetzung Ressort ohne Statistik | Bandbreite, Sensitivitaet |
| Internationale Vergleichsdaten | nur ersatzweise |

## Mustertexte / Stellungnahme-Bausteine

- "Die Berechnung legt einen Zeitwert von [X] Minuten zugrunde, der der Leitfaden-Tabelle [Bezeichnung] (Komplexitaetsstufe [einfach / mittel / komplex]) entspricht."
- "Die Fallzahl von [N] beruht auf dem Unternehmensregister des Statistischen Bundesamtes (Stand [Jahr])."
- "Der NKR weist darauf hin, dass die zugrundegelegte Fallzahl auf eine [X] Jahre alte Statistik zurueckgreift und eine Aktualisierung wuenschenswert waere."

### Quellenpfad-Vermerk (Standard)

> Quelle Fallzahl: Statistisches Bundesamt, Unternehmensregister, abrufbar unter [www.destatis.de](https://www.destatis.de), Stand [Datum].

## Typische Fehler in Ressort-Entwuerfen

- Zeitwerte ohne Tabellenverweis
- "Erfahrungswerte" ohne Quellenangabe
- Komplexitaetsstufe pauschal mittel ohne Pruefung
- Lohnsatz "ca. 30 EUR" ohne Differenzierung
- Fallzahlen aus Pressemeldungen statt Statistik

## Querverweise

- `nkr-standardkostenmodell-skm`
- `nkr-fallzahlen-schaetzung-bandbreiten`
- `nkr-erfuellungsaufwand-buerger-wirtschaft-verwaltung`
- `nkr-leitfaden-ermittlung-und-darstellung`
- `legistik-werkstatt/folgenabschaetzung-erfuellungsaufwand`

## Quellen Stand 06/2026

- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR), Zeitwerttabellen
- DESTATIS Verdienststrukturerhebung (jeweils aktuelle Ausgabe)
- DESTATIS Unternehmensregister (jeweils aktuelle Ausgabe)
- DESTATIS Personalstandstatistik (jeweils aktuelle Ausgabe)
- NKR-Jahresbericht (jeweils aktuelle Ausgabe)
- Live verifizieren ueber [www.destatis.de](https://www.destatis.de) und [www.bmi.bund.de](https://www.bmi.bund.de)
