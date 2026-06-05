---
name: pruefumfang-was-standardkostenmodell-skm
description: "Pruefumfang WAS Standardkostenmodell SKM: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pruefumfang WAS Standardkostenmodell SKM

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Pruefumfang WAS Standardkostenmodell SKM** im Plugin Normenkontrollrat (NKR). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nkr-pruefumfang-was-prueft-der-nkr-nicht` | Negativabgrenzung des NKR-Pruefumfangs. Erklaert was der NKR ausdruecklich nicht prueft (politische Zielwahl Verfassungsmaessigkeit Haushaltsfolgen) und was er sehr wohl prueft (Methodik Erfuellungsaufwand Praktikabilitaet Digitaltauglichkeit). Verhindert Zustaendigkeitsanmassung und liefert Standardbausteine fuer die Stellungnahme zur Kompetenzabgrenzung. |
| `nkr-standardkostenmodell-skm` | Beschreibt das Standardkostenmodell SKM als methodischen Kern der Erfuellungsaufwandsberechnung. Erklaert die Standardformel Aufwand pro Fall × Fallzahl Bandbreiten Komplexitaetsfaktoren Bezug auf DESTATIS-Lohnsaetze und Dokumentationsanforderungen. Mit Rechenbeispiel und Checkliste fuer die NKR-Methodenpruefung. |

## Arbeitsweg

Im Plugin Normenkontrollrat (NKR) gilt für **Pruefumfang WAS Standardkostenmodell SKM**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nkr-pruefumfang-was-prueft-der-nkr-nicht`

**Fokus:** Negativabgrenzung des NKR-Pruefumfangs. Erklaert was der NKR ausdruecklich nicht prueft (politische Zielwahl Verfassungsmaessigkeit Haushaltsfolgen) und was er sehr wohl prueft (Methodik Erfuellungsaufwand Praktikabilitaet Digitaltauglichkeit). Verhindert Zustaendigkeitsanmassung und liefert Standardbausteine fuer die Stellungnahme zur Kompetenzabgrenzung.

# NKR-Pruefumfang — was prueft der NKR nicht

## Worum geht es konkret

Spiegelbild zu `nkr-aufgabe-und-kompetenz-nkrg`. Adressiert die haeufige Verwechslung der Rollen Bundesrechnungshof, BVerfG, Wissenschaftlicher Dienst, BMJ-Rechtsabteilung, NKR.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Sekretariat bekommt Vorhaben, das nach NKR aussieht, aber methodisch nicht in den Pruefkern faellt
- Ressort moechte den NKR "instrumentalisieren" fuer politische Argumente
- Stellungnahme-Entwurf wird zu breit, droht Kompetenzgrenze zu ueberschreiten

## Rechtlicher und methodischer Rahmen

- **§ 1 Abs. 1 NKRG** — Pruefung "auf die Darstellung des Erfuellungsaufwands"
- **§ 4 NKRG** — Pruefungsgegenstand: Erfuellungsaufwand und sein Methodik
- **§ 6 NKRG** — Stellungnahme
- **§ 44 GGO** — Gesetzesfolgenabschaetzung (umfasst mehr als nur Erfuellungsaufwand)
- **Art. 114 GG, BHO, § 88 BHO** — Bundesrechnungshof, Wirtschaftlichkeit
- **Art. 93 GG, BVerfGG** — Verfassungsgerichtsbarkeit

## Pruefraster / Schritt fuer Schritt

### Der NKR prueft

1. **Erfuellungsaufwand** (Buerger, Wirtschaft, Verwaltung) — vollstaendig dargestellt?
2. **Methodik** — Standardkostenmodell (SKM) korrekt angewandt?
3. **Fallzahlen und Zeitwerte** — plausibel? nachvollziehbar?
4. **Einmalig vs. laufend** — korrekt unterschieden?
5. **Alternativen** — geprueft und dokumentiert?
6. **One-in-one-out** — verbucht?
7. **KMU-Test** — durchgefuehrt?
8. **Digitaltauglichkeit** — Digitalcheck durchlaufen?
9. **Praktikabilitaet im Vollzug** — fuer Verwaltung leistbar?
10. **Evaluierungsklausel / Befristung** — vorgesehen?

### Der NKR prueft **nicht**

1. **Politische Zielwahl** ("Soll diese Branche reguliert werden?")
2. **Verfassungsmaessigkeit** — BMJ-Rechtsabteilung, ggf. BVerfG
3. **Europarechtskonformitaet im engeren Sinne** — EU-Rechtsabteilungen
4. **Haushaltsmaessige Auswirkungen auf den Bundeshaushalt** — BMF, Bundesrechnungshof
5. **Wirtschaftlichkeit im Sinne der BHO** — Bundesrechnungshof
6. **Ordnungspolitische Sinnhaftigkeit** — politische Entscheidung
7. **Auslegung einzelner Tatbestandsmerkmale** — Gerichte
8. **Konkrete Vollzugsentscheidungen** — Behoerden
9. **Wissenschaftliche Folgenforschung im engeren Sinne** — Wissenschaftlicher Dienst, Ressortforschung
10. **Datenschutzrechtliche Detailpruefung** — BfDI

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Ressort umgeht NKR durch Verschieben der Befassungspflicht (z.B. ueber parlamentarische Aenderung)
- Ressort liefert "alibimaessig" Zahlen ohne Methodik
- Ressort behauptet "kein Aufwand" ohne Plausibilisierung

## Trade-off-Matrix

| Anliegen | NKR | Zustaendig stattdessen |
|---|---|---|
| Verfassungsmaessigkeit | nein | BMJ, BVerfG |
| Bundeshaushalt | nein | BMF, BRH |
| EU-Konformitaet | nein (nur Hinweis) | BMJ, GS-EU |
| Erfuellungsaufwand | ja | NKR |
| Praktikabilitaet | ja | NKR |
| Digitaltauglichkeit | ja | NKR (Digitalcheck) |
| Politik | nein | Bundesregierung, Bundestag |

## Mustertexte / Stellungnahme-Bausteine

- "Die Pruefung des NKR ist gemaess § 4 NKRG auf die Darstellung des Erfuellungsaufwands beschraenkt. Eine Bewertung der ordnungspolitischen Zielsetzung erfolgt nicht."
- "Hinweise zur Verfassungs- oder Europarechtskonformitaet sind nicht Gegenstand der NKR-Pruefung; insoweit verweist der NKR auf die zustaendige Ressortpruefung."
- "Der NKR begruesst grundsaetzlich die Zielsetzung des Vorhabens, beschraenkt seine Stellungnahme aber auf die methodischen Aspekte des Erfuellungsaufwands."

## Typische Fehler in Ressort-Entwuerfen

- "Der NKR hat das Vorhaben verfassungsrechtlich gepruft und nicht beanstandet" — falsch, NKR prueft das nicht
- "Der NKR hat die Wirtschaftlichkeit bestaetigt" — falsch, das ist BRH
- "NKR-Beteiligung erfolgt nur bei wirtschaftspolitischen Vorhaben" — falsch, generelle Befassungspflicht bei Erfuellungsaufwand

## Querverweise

- `nkr-aufgabe-und-kompetenz-nkrg`
- `nkr-stellungnahme-mahnender-charakter-grenzen`
- `nkr-zusammenarbeit-mit-bundesregierung-und-ressorts`
- `nkr-eu-ebene-und-better-regulation`
- `legistik-werkstatt/verfassungsmaessigkeit-quercheck`

## Quellen Stand 06/2026

- NKRG vom 14.08.2006 (BGBl. I S. 1866) §§ 1, 4, 6
- §§ 44, 45 GGO
- BHO §§ 7, 88, 114
- Art. 93, 114 GG
- Live verifizieren ueber Bundesanzeiger und [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)

## 2. `nkr-standardkostenmodell-skm`

**Fokus:** Beschreibt das Standardkostenmodell SKM als methodischen Kern der Erfuellungsaufwandsberechnung. Erklaert die Standardformel Aufwand pro Fall × Fallzahl Bandbreiten Komplexitaetsfaktoren Bezug auf DESTATIS-Lohnsaetze und Dokumentationsanforderungen. Mit Rechenbeispiel und Checkliste fuer die NKR-Methodenpruefung.

# NKR-Standardkostenmodell (SKM)

## Worum geht es konkret

Das Standardkostenmodell (SKM) ist die in Deutschland (und mehreren EU-Mitgliedstaaten) etablierte Methodik zur Quantifizierung von Erfuellungsaufwand. Der NKR hat das SKM 2006/2007 als methodische Grundlage uebernommen und im Leitfaden BMI/NKR weiterentwickelt.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Stellungnahme prueft Methodenanwendung
- Ressort wendet abweichende Methodik an
- Rechenwege sind nicht nachvollziehbar
- Schulung Methodik

Rueckfrage nur wenn unklar: *"Welche Methodik liegt der Ressortdarstellung zugrunde?"*

## Rechtlicher und methodischer Rahmen

- **Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands** (BMI / NKR), Methodenteil
- **OECD-Standard-Cost-Model-Toolkit**
- **EU Better Regulation Toolbox** Tool 24 Standard Cost Model
- **NKRG** § 4 i.V.m. methodischer Auslegung durch den NKR

## SKM-Grundformel

```
Erfuellungsaufwand (jaehrlich)
 = Σ (Aufwand pro Fall × Fallzahl pro Jahr)

Aufwand pro Fall
 = Zeitaufwand × Lohnsatz + Sachkosten + externe Dienstleistungskosten
```

## Pruefraster / Schritt fuer Schritt

1. **Pflicht-Inhalt zerlegen** in Einzeltaetigkeiten ("Activity Mapping")
2. **Standardtaetigkeit** zuordnen (Lese-, Schreib-, Pruef-, Antwort-, Berechnungstaetigkeit)
3. **Zeitwert pro Taetigkeit** ansetzen (Leitfaden-Tabelle, ggf. mit Komplexitaetsfaktor)
4. **Lohnsatz** zuordnen nach Qualifikationsniveau
5. **Sachkosten** ergaenzen (Material, Geraete, IT-Lizenz)
6. **Externe Kosten** ergaenzen (Beraterhonorare, Pruefkosten)
7. **Fallzahl** ermitteln (Statistik, ggf. Schaetzung mit Bandbreite)
8. **Multiplikation** und Aggregation
9. **Plausibilisierung** durch Vergleich mit Referenzfaellen
10. **Dokumentation** vollstaendig: jede Annahme nachvollziehbar

## NKR-Sicht — was triggert eine kritische Stellungnahme

- Methodik nicht offen gelegt (keine Aufschluesselung pro Pflicht)
- Pauschalannahmen ohne Beleg
- Komplexitaetsfaktoren unplausibel (zu hoch oder zu niedrig)
- Fallzahlen nicht aus Statistik, sondern aus dem "Bauch"
- Sachkosten oder externe Dienstleistungen ausgeklammert
- Methodik abweichend ohne Begruendung

## Trade-off-Matrix

| Methodische Frage | NKR-Position |
|---|---|
| Standardisierung vs. Einzelfallrechnung | Standardisierung bevorzugt fuer Vergleichbarkeit |
| Punktwert vs. Bandbreite | Bandbreite bei Unsicherheit ausweisen |
| Pessimistische vs. optimistische Annahme | Mittlere Annahme, Sensitivitaet pruefen |
| Komplexitaetsfaktor | konservativ ansetzen |
| Dunkelziffer / faktische Nutzung | dokumentieren, ggf. nicht einrechnen |

## Mustertexte / Stellungnahme-Bausteine

- "Die Berechnung folgt dem Standardkostenmodell (SKM) gemaess Leitfaden BMI/NKR. Aufwand pro Fall wurde aus den Zeitwerten der Tabelle [Bezeichnung] zuzueglich Sachkosten ermittelt."
- "Der NKR weist darauf hin, dass die Berechnung von der Standardmethodik abweicht; eine Begruendung fehlt. Der NKR bittet das Ressort um Darstellung nach SKM."
- "Die Sensitivitaetsanalyse zeigt: bei Variation der Fallzahl um ± 20% bewegt sich der Erfuellungsaufwand zwischen [X] und [Y] Mio EUR jaehrlich."

### Rechenbeispiel (illustrativ)

Pflicht: jaehrlicher Bericht im Umfang von ca. 4 Stunden.

- Zeitaufwand pro Fall: 240 Minuten
- Lohnsatz Wirtschaft mittlere Qualifikation: ca. 45 EUR/h
- Aufwand pro Fall (Zeit): 240/60 × 45 = 180 EUR
- Sachkosten pro Fall: 10 EUR (Druck, Versand)
- Aufwand pro Fall gesamt: 190 EUR
- Fallzahl jaehrlich: 1,8 Mio Gesellschaften
- Jaehrlicher Erfuellungsaufwand: 1.800.000 × 190 = ca. 342 Mio EUR

(Werte sind illustrativ; verbindlich ist die jeweils aktuelle Leitfaden-Tabelle.)

## Typische Fehler in Ressort-Entwuerfen

- Pflichtinhalt nicht in Einzeltaetigkeiten zerlegt
- Lohnsatz "ca. 30 EUR" ohne Quelle
- Sachkosten "vernachlaessigbar" ohne Begruendung
- Fallzahl aus 10 Jahre alter Statistik
- Komplexitaetsfaktor "1,0" durchgaengig

## Querverweise

- `nkr-erfuellungsaufwand-grundbegriff`
- `nkr-zeitwerttabelle-und-fallzahlen`
- `nkr-leitfaden-ermittlung-und-darstellung`
- `nkr-fallzahlen-schaetzung-bandbreiten`
- `legistik-werkstatt/folgenabschaetzung-erfuellungsaufwand`

## Quellen Stand 06/2026

- Leitfaden zur Ermittlung und Darstellung des Erfuellungsaufwands (BMI / NKR)
- OECD Standard Cost Model Manual
- EU Better Regulation Toolbox Tool 24
- NKRG vom 14.08.2006 (BGBl. I S. 1866) § 4
- Live verifizieren ueber [www.bmi.bund.de](https://www.bmi.bund.de) und [www.normenkontrollrat.bund.de](https://www.normenkontrollrat.bund.de)
