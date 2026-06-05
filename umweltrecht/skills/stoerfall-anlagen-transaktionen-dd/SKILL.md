---
name: stoerfall-anlagen-transaktionen-dd
description: "Stoerfall Anlagen Transaktionen DD: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Stoerfall Anlagen Transaktionen DD

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Stoerfall Anlagen Transaktionen DD** im Plugin Umweltrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `umweltrecht-stoerfall-anlagen` | Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung Sicherheitsbericht Betreiberpflichten Sicherheitsabstaende Bauleitplanung. Output Sicherheitsbericht-Struktur Anordnungs-Widerspruch. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (allg. Genehmigung) und umweltrecht-bußgeld-sanktionen (Bußgelder). |
| `umweltrecht-transaktionen-dd` | M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags Closing-Conditions Capex-Risiken Wert-Adjustierung. Output Umwelt-DD-Report Kaufvertrags-Klauseln Risikomatrix. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (Einzelgenehmigung) und mittelstand-corporate-ma-due-diligence-legal (allg. DD). |
| `umweltrecht-umweltinformation-uig-ifg` | Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz Drittbeteiligung Widerspruchs-Klage. Output Antrags-Muster Widerspruch Klage VG. Abgrenzung zu umweltrecht-verfahren (allg. Verwaltungsklage) und umweltrecht-kommandocenter (Routing). |

## Arbeitsweg

Im Plugin Umweltrecht gilt für **Stoerfall Anlagen Transaktionen DD**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `umweltrecht-stoerfall-anlagen`

**Fokus:** Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung Sicherheitsbericht Betreiberpflichten Sicherheitsabstaende Bauleitplanung. Output Sicherheitsbericht-Struktur Anordnungs-Widerspruch. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (allg. Genehmigung) und umweltrecht-bußgeld-sanktionen (Bußgelder).

# Stoerfall, Anlagenbetrieb und Betreiberpflichten

## Triage — klaere zuerst

1. Faellt die Anlage unter die 12. BImSchV (Stoerfall-Verordnung) — Grundpflichten (Anhang I Spalte 1) oder erweiterte Pflichten (Anhang I Spalte 2)?
2. Sind gefaehrliche Stoffe (Anhang I 12. BImSchV) in welchen Mengen vorhanden?
3. Liegt ein Stoerfall bereits vor oder geht es um praeventive Compliance?
4. Wurden die zustaendige Behoerde und die Oeffentlichkeit informiert (§§ 19, 20 BImSchV)?
5. Besteht eine Anordnung der Behoerde (§ 17 BImSchG) auf Grundlage Sicherheitsmangel?
6. Ist Bauleitplanung in der Naehe geplant — Sicherheitsabstandsproblem?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 3 Abs. 5a BImSchG** — Stoerfall-Definition (unkontrolliertes Ereignis, erhebliche Gefahr)
- **§ 7 Abs. 1 Nr. 5 BImSchG** — Anforderungen an Anlagen Sicherheitsbericht
- **§ 16 BImSchV (12. BImSchV)** — Sicherheitsbericht Pflichtinhalt (Gefahrenquellen, Schutz-/Notfallkonzept)
- **§ 17 BImSchV** — Bericht nach Stoerfall (Untersuchungspflicht, Massnahmen)
- **§ 19 BImSchV** — Stoerfallanzeige bei Behoerde (unverzueglich)
- **§ 20 BImSchV** — Unterrichtung Oeffentlichkeit (Angaben Anlagen-Website)
- **Art. 13 Seveso-III-Richtlinie (2012/18/EU)** — Sicherheitsabstaende Raumordnung
- **§ 50 BImSchG** — Trennungsgebot Gebiete mit schweren Unfaellen und Wohnnutzung
- **§ 17 BImSchG** — Nachtraegliche Auflagen und Anordnungen
- **§ 62 BImSchG** — Ordnungswidrigkeiten (Bussgeld bis 50.000 EUR)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Praeventive Compliance-Pruefung

1. **Stoerfall-Relevanz pruefen**: Mengen gefaehrlicher Stoffe nach Anhang I 12. BImSchV — Spalte 1 oder 2.
2. **Sicherheitskonzept Grundpflichten**: § 8 12. BImSchV — schriftliches Konzept Verhuetung Stoerfaelle.
3. **Sicherheitsbericht Erweiterte Pflichten**: § 16 12. BImSchV — Inhalt: Stoffe, Anlage, Risiken, Notfallplanung; Prueflauf alle 5 Jahre.
4. **Anzeige/Genehmigung**: § 4 BImSchG, § 9 12. BImSchV — Behoerde informieren vor Betriebsbeginn.
5. **Sicherheitsabstand pruefen**: KAS-18-Leitfaden BG Chemie; Abstand zu schutzbeduerftigen Gebieten ermitteln.
6. **Notfallplan**: § 10 12. BImSchV — interner Alarm- und Notfallplan; externe Information an Behoerde.
7. **Unterrichtung Oeffentlichkeit**: § 20 12. BImSchV — Anlage-Website Sicherheitsinformationen.

### B) Reaktion auf Stoerfall

1. **Sofortanzeige**: § 19 12. BImSchV — unverzueglich an Behoerde, Feuerwehr, Umweltamt.
2. **Ursachenuntersuchung**: § 17 12. BImSchV — Bericht innerhalb angemessener Frist.
3. **Massnahmenumsetzung**: Wiederholungsvermeidung; Dokumentation.
4. **Bussgeld-Abwehr**: § 62 BImSchG — schuldlose Pflichtverletzung, technisches Versagen ohne Vorwerfbarkeit?
5. **Kommunikation Behoerde**: Kooperationsbereitschaft zeigen; Massnahmenplan vorlegen.

### Entscheidungsbaum Stoerfallrelevanz

```
Stoff in Anhang I 12. BImSchV?
 JA → Menge erreicht Spalte-1-Schwelle?
 JA → Grundpflichten (§§ 3-9 12. BImSchV)
 Menge erreicht Spalte-2-Schwelle?
 JA → Erweiterte Pflichten incl. Sicherheitsbericht § 16
 NEIN → Nur Grundpflichten
 NEIN → Keine Stoerfall-VO-Pflicht; normale BImSchG-Anforderungen
 NEIN → Keine Stoerfall-Relevanz
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Stellungnahme nach Storfallmeldung erstellen | Stellungnahme nach Schema; Template unten |
| Variante A — Stoeranfall noch laufend keine Stellungnahme moeglich | Krisenkommunikation zuerst; Stellungnahme nach Abschluss |
| Variante B — Stoeranfall ohne Schaden nur formale Meldepflicht | Minimale Meldung; Stellungnahme kurzgefasst |
| Variante C — Behoerde droht Betriebsuntersagung | Dringlichkeit erhoehen; Stellungnahme mit Massnahmenplan |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template: Stellungnahme nach Stoerfallanzeige

**Adressat:** Zustaendige Behoerde — Tonfall: sachlich-kooperativ

```
An die [BEHOERDE]

Stoerfall-Bericht gemaess § 17 der 12. BImSchV

Betreiber: [NAME MANDANT]
Anlage: [NAME], [ORT], BImSchG-Genehmigung Az. [NR.]
Ereignis: [DATUM], [UHRZEIT]

I. Beschreibung des Ereignisses
Am [DATUM] um [UHRZEIT] ereignete sich [kurze Beschreibung].
Freigesetzte Stoffe: [Stoff, Menge, Ausbreitung].
Betroffener Bereich: [Gelaende/Oeffentlichkeit].

II. Sofortmassnahmen
1. Alarmierung Feuerwehr und Werkschutz um [UHRZEIT].
2. Evakuierung Gefahrenbereich ab [UHRZEIT].
3. Auftrag Dekontamination an [FIRMA] erteilt.

III. Ursache (vorlaeufige Einschaetzung)
[Beschreibung technischer Ursache, menschliches Versagen / hoeherer Gewalt].

IV. Massnahmen zur Wiederholung-Vermeidung
1. [Technische Massnahme, Zeitplan].
2. [Schulung Personal, Datum].
3. [Aenderung Betriebsanweisung].

V. Naechste Schritte
Wir legen bis zum [DATUM] einen vollstaendigen Untersuchungsbericht vor.

Anlagen: Lageplan, Stofffliessschema, Messprotokoll
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Anlagenpflichtenmatrix (Kurzform)

| Pflicht | Spalte 1 | Spalte 2 | Grundlage |
|---|---|---|---|
| Schriftliches Sicherheitskonzept | JA | JA | § 8 12. BImSchV |
| Sicherheitsbericht | NEIN | JA | § 16 12. BImSchV |
| Notfallplan intern | JA | JA | § 10 Abs. 1 |
| Extern. Notfallplan Behoerde | NEIN | JA | § 10 Abs. 2 |
| Dominoeffekt-Pruefung | NEIN | JA | § 14 12. BImSchV |
| Oeffentlichkeits-Information | NEIN | JA | § 20 12. BImSchV |
| Sicherheitsabstand | JA | JA | § 50 BImSchG |

## Anschluss-Skills

- `umweltrecht-immissionsschutz-bimschg` — BImSchG-Genehmigungsrahmen
- `umweltrecht-bussgeld-sanktionen` — Bussgeld nach Stoerfall
- `umweltrecht-verfahren` — Klageverfahren gegen Behoerdenanordnung
- `umweltrecht-transaktionen-dd` — Stoerfall-Risiken in M&A

## 2. `umweltrecht-transaktionen-dd`

**Fokus:** M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags Closing-Conditions Capex-Risiken Wert-Adjustierung. Output Umwelt-DD-Report Kaufvertrags-Klauseln Risikomatrix. Abgrenzung zu umweltrecht-immissionsschutz-bimschg (Einzelgenehmigung) und mittelstand-corporate-ma-due-diligence-legal (allg. DD).

# Umweltrechtliche Transaktions-Due-Diligence

## Triage — klaere vor DD-Beginn

1. Share Deal oder Asset Deal? (Share Deal: Haftung folgt Gesellschaft; Asset Deal: Einzelvermoegensuebertragung, Haftungsrueckstand bleibt bei Verkaeufer in Grenzen).
2. Welche Anlagen/Standorte — BImSchG-Genehmigungen vorhanden?
3. Altlasten bekannt (§§ 4, 9 BBodSchG) — Bodenuntersuchungen vorgelegt?
4. TEHG-Pflicht? Emissionshandel-Status?
5. Produktions-Genehmigungen aktuell oder laeuft Aenderungsverfahren?
6. Bestehen Behoerdenanordnungen oder laufende Verwaltungs-/Gerichtsverfahren?

## Zentrale Normen und Paragrafenkette

- **§§ 4 6 BImSchG** — Betriebsgenehmigung; Rechtsnachfolge bei Share Deal
- **§ 17 BImSchG** — Nachtraegliche Auflagen; uebernimmt Erwerber bei Share Deal
- **§§ 4 9 BBodSchG** — Altlastenverantwortlichkeit (Verursacher, Eigentueemer, Gesamtrechtsnachfolger)
- **§ 5 KrWG** — Ende Abfalleigenschaft; DD-relevante Bewertung Abfallstatus
- **§ 13 WHG** — Wasserrechtliche Gestattungen; Erlaubnisse nicht automatisch uebertragbar
- **§ 9 TEHG** — Kostenlose ETS-Zuteilung; Kapazitaetsaenderung nach Transaktion melden
- **§ 1 UmwHaftG** — Haftung fuer Schaden durch Anlage
- **§ 24 BBodSchG** — Erstattungsanspruch bei Sanierung durch Dritte

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-DD

### Phase 1: Kick-off und Scope-Setting

1. Transaktionsstruktur festlegen: Share/Asset Deal, betroffene Gesellschaften, Standorte.
2. DD-Scope: Welche Umweltbereiche — Genehmigungen, Altlasten, Emissionen, Abfall, Wasser, Naturschutz?
3. Datenraum-Liste anfordern: Genehmigungen, Bescheide, Behoerdenkorrespondenz, Gutachten, Monitoring-Berichte.
4. Wesentlichkeitsschwelle definieren: welche Findings ab welchem EUR-Wert als Red Flag?

### Phase 2: Dokument-Analyse

1. **BImSchG-Genehmigungen**: Inhalt, Nebenbestimmungen, Aenderungs-Historie; laufen aktuelle Verfahren?
2. **Altlasten**: Bodenuntersuchungen Phase I (historische Nutzung) und Phase II (Analytik); Sanierungsplan?
3. **TEHG**: Zuteilungsbescheid, Monitoring-Plan; Abgabe-Geschichte letzter 5 Jahre.
4. **Wasserrecht**: Einleitgenehmigungen, Entnahmegenehmigungen; ablaufende Genehmigungen?
5. **Abfallrecht**: Entsorgungsvertraege, Nachweise; unerlaubte Ablagerungen?
6. **Verfahren/Anordnungen**: Klagen, Widerspruchsverfahren, Behoerdenanordnungen § 17 BImSchG.

### Phase 3: Red-Flag-Bewertung

| Kategorie | Red Flag | Orange | Gruen |
|---|---|---|---|
| BImSchG-Genehmigung | Fehlt oder wesentlich veraltet | Aenderung laufend | Aktuell und vollstaendig |
| Altlasten | Aktiver Kontaminationsherd | Historische Untersuchung fehlt | Phase II ohne Befund |
| TEHG-Abgabe | Rueckstand > 3 Jahre | Einmalige Verspaetung | Vollstaendig |
| Behoerdenanordnung | Rechtshaft unanfechtbar | Widerspruch laufend | Keine |
| Naturschutz | Stoerfall-Anlage in Schutzgebiet | FFH-VS fehlt | Vollstaendig |

### Phase 4: Kaufvertrags-Klauseln

1. **Garantien (W&I)**: Genauigkeit Genehmigungen, Altlasten-Freiheit, keine unbekannten Anordnungen.
2. **Indemnities**: Verkaeufer-Freistellung fuer bekannte Altlasten (Schedule mit Standorten).
3. **Closing-Conditions**: Vorlage aktueller Umwelt-Gutachten, Behoerden-Auskunft Altlasten, Freigabe DEHSt TEHG-Konto.
4. **Purchase-Price-Anpassung**: Discount fuer quantifizierbare Capex-Risiken (Sanierung, Nachruestung).
5. **W&I-Versicherung**: Typical fuer Mid-Market M&A; Umwelt-Endorsements (Altlasten-Ausschluss / Einschluss gegen Praemie).

## Output-Template: DD-Kurz-Finding (Red Flag)

**Adressat:** Mandant (Kaeufer) / Deal Team — Tonfall: sachlich-analysierend

```
Umwelt-DD-Finding Nr. [X]
Kategorie: Altlasten / BImSchG / TEHG / Wasser
Bewertung: ROT / ORANGE / GRUEN
Standort: [ORT], Grundstueck [FLUR/STRASSE]

Befund:
[Beschreibung des konkreten Problems: fehlende Genehmigung, Altlast-Nachweis, Behoerdenanordnung]

Rechtsgrundlage: § [X] [Gesetz]

Risikobewertung:
- Haftungsrisiko Erwerber: Bis [BETRAG] EUR gemaess § 4 Abs. 3 BBodSchG
- Sanierungskosten: geschaetzt [BETRAG] EUR (Gutachten [DATUM])
- Zeitraum: [ZEITHORIZONT] Monate bis Behebung

Empfehlung:
1. Closing-Condition: Vollstaendige Phase-II-Untersuchung oder Sanierungsplan.
2. Preisabzug: [BETRAG] EUR.
3. Verkaeufer-Indemnity fuer bekannten Altlast-Herd.
4. W&I-Versicherungs-Endorsement pruefen.

Quellen: [Dokument im Datenraum, Seite/Tab]
```

## Vertiefung: BBodSchG Haftungskette

- Verursacher > Rechtsnachfolger > Grundstueckseigentuemer > Inhaber tatsaechlicher Gewalt.
- Bei Share Deal: Erwerber tritt als Gesamtrechtsnachfolger in Haftungsposition des Verkaeufers ein.
- Gesamtschuldner-Ausgleich § 24 BBodSchG: Sanierungskosten koennen intern aufgeteilt werden.
- Haftungs-Cap im Kaufvertrag gilt nur zwischen Vertragsparteien, nicht gegenueber Behoerde.

## Anschluss-Skills

- `umweltrecht-wasser-bodenschutz` — Altlasten-Vertiefung
- `umweltrecht-emissionshandel-tehg` — TEHG bei Transaktion
- `umweltrecht-immissionsschutz-bimschg` — Genehmigungsrechtsnachfolge
- `energierecht-transaktionen-dd` — Energie-Asset-DD

## 3. `umweltrecht-umweltinformation-uig-ifg`

**Fokus:** Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz Drittbeteiligung Widerspruchs-Klage. Output Antrags-Muster Widerspruch Klage VG. Abgrenzung zu umweltrecht-verfahren (allg. Verwaltungsklage) und umweltrecht-kommandocenter (Routing).

# Umweltinformation nach UIG und IFG

## Triage — klaere vor Antragstellung

1. Liegt Umweltinformation (§ 2 Abs. 3 UIG) vor oder allgemeine Behoerdeninformation (IFG)?
2. Welche Behoerde/Stelle — Behoerde des Bundes (IFG/UIG Bund), Behoerde des Landes (LIFG/LUIG)?
3. Besteht Drittbeteiligung (Unternehmen, das Geheimnisschutz beansprucht — § 9 UIG)?
4. Ist Antragsgruende angabe notwendig (IFG: nicht erforderlich; UIG: ebenso nicht)?
5. Besteht Eilbedarf (Oeffentlichkeitsbeteiligung in Genehmigungsverfahren laufend)?
6. Soll Widerspruch oder direkt Klage (VG) erhoben werden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 3 Abs. 1 UIG** — Anspruch auf Umweltinformationen (jedermann, keine Begruendung)
- **§ 4 UIG** — Antragstellung; Frist Behoerde 1 Monat (verlaeaerbar auf 2 Monate bei Umfang)
- **§ 8 UIG** — Ausschlussgrundsaetze oeffentliches Interesse (laufende Verfahren, Landesverteidigung)
- **§ 9 UIG** — Schutz Betriebs- und Geschaeftsgeheimnisse; Drittbeteiligung Verfahren
- **§ 10 UIG** — Aktive Verbreitung durch Behoerde
- **§ 1 IFG** — Anspruch auf Zugang zu amtlichen Informationen (Bundesbehoerden)
- **§ 3 IFG** — Schutz besonderer oeffentlicher Belange (Sicherheit, Beratungsgeheimnis)
- **§ 5 IFG** — Schutz personenbezogener Daten
- **§ 6 IFG** — Schutz des geistigen Eigentums und Betriebs-/Geschaeftsgeheimnisse
- **§ 9 IFG** — Antrag und Frist (1 Monat)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### A) Antragsteller (Buerger, NGO, Unternehmen)

1. **Antrag formulieren**: Konkrete Umweltinformation benennen; Bezug zu § 2 Abs. 3 UIG herstellen; keine Begruendung erforderlich.
2. **Adressat**: Informationspflichtige Stelle (Behoerde, privatrechtliche Stelle mit oeffentlichen Aufgaben — § 2 Abs. 1 UIG).
3. **Frist kontrollieren**: Behoerde muss binnen 1 Monat antworten (§ 4 UIG); bei Umfang 2 Monate unter Mitteilung.
4. **Drittbeteiligung abwarten**: Wenn Dritter (Unternehmen) beteiligt — Stellungnahme-Frist + Entscheidung.
5. **Ablehnung anfechten**: Widerspruch (falls Widerspruchsverfahren vorgesehen) oder Klage VG; Klagerecht § 6 UIG auch ohne Vorverfahren in einigen Laendern.
6. **Eilbedarf**: § 123 VwGO Antrag auf vorlaeufige Herausgabe wenn Informationsbedarf dringend.

### B) Dritter (Unternehmen) — Geheimnisschutz verteidigen

1. **Drittbeteiligung beobachten**: Behoerde muss vor Herausgabe Anhoerun durchfuehren (§ 9 Abs. 1 UIG).
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Behoerdenentscheidung anfechten**: Klage VG gegen Herausgabe-Anordnung; Eilantrag § 80 Abs. 5 VwGO (aufschiebende Wirkung bis VG-Entscheidung).

### Entscheidungsbaum Antrag

```
Informationsbegehren
 → UIG oder IFG? (Umweltbezug → UIG; allgemeine Behoerde → IFG)
 → Behoerde bundesrechtlich? (Bund: UIG-Bund/IFG; Land: UIG-Land/LIFG)
 → Antrag stellen, 1-Monats-Frist abwarten
 → Keine Antwort? → Untaetigkeit-Klage VG
 → Ablehnung? → Widerspruch (falls vorgesehen) → Klage VG
 → Drittbeteiligung? → Stellungnahme Geheimhaltung → Behoerde entscheidet → Klage des Dritten moeglich
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Informationsantrag nach UIG stellen | Antrag nach Schema; Template unten |
| Variante A — Antrag wurde bereits abgelehnt Widerspruch noetig | Widerspruchstemplate verwenden statt Erstantrag |
| Variante B — IFG statt UIG anzuwenden Verwaltungsinformation | IFG-Variante; Abgrenzung UIG-IFG klaeren |
| Variante C — Information eilig Behoerde soll priorisieren | Dringlichkeitsvermerk in Antrag aufnehmen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template: Informationsantrag UIG

**Adressat:** Zustaendige Behoerde — Tonfall: sachlich, klar

```
An die [BEHOERDE]

Antrag auf Zugang zu Umweltinformationen gemaess § 3 Abs. 1 UIG

Antragsteller: [NAME], [ADRESSE]

Ich beantrage Zugang zu folgenden Umweltinformationen:

1. [Konkrete Beschreibung der gesuchten Information]
 Bezug: [Anlage, Ort, Verfahren, Datum]

2. [Zweite Information, falls mehrere]

Diese Informationen betreffen Umweltfaktoren i.S.d. § 2 Abs. 3 UIG:
[Luft, Wasser, Boden, Emissionen, Massnahmen, Zustand der Umwelt].

Ich bitte um Zugang in folgender Form:
[ ] digitale Kopie (PDF per E-Mail)
[ ] Akteneinsicht vor Ort
[ ] schriftliche Auskunft

Gemaess § 4 Abs. 1 UIG bitte ich um Bescheidung binnen eines Monats.

[NAME], [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Output-Template: Widerspruch nach Ablehnung

**Adressat:** Widerspruchsbehoerde — Tonfall: sachlich-juristisch

```
An die [BEHOERDE]

Widerspruch gegen Ablehnungsbescheid

Antragsteller: [NAME]
Ihr Bescheid vom [DATUM], Az. [AZ.]

I. Hiermit legen wir Widerspruch ein.

II. Begruendung
Die Ablehnung ist rechtswidrig:
a) § 9 UIG Geheimnisschutz: Die Behoerde hat keine eigene Abwaegung vorgenommen.
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
b) § 8 UIG laufende Verfahren: Das Verfahren ist abgeschlossen; Ausschlussgrund
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
c) Emissionsdaten sind nach § 9 Abs. 1 Satz 2 UIG grundsaetzlich offenzulegen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

III. Antrag
Wir beantragen, den Ablehnungsbescheid aufzuheben und die Informationen herauszugeben.
```

## Vertiefung: Aktive Informationspflicht § 10 UIG

- Behoerden sollen Umweltinformationen von allgemeinem Interesse aktiv ins Netz stellen.
- Emissionsdaten, Genehmigungen, UVP-Berichte grundsaetzlich oeffentlich.
- Verstoss gegen aktive Veroeffentlichungspflicht: Ruege durch UIG-Antrag + Klage.

## Fristen-Ueberblick

| Schritt | Frist | Grundlage |
|---|---|---|
| Behoerdenentscheidung | 1 Monat (max. 2 Monate) | § 4 Abs. 1 UIG |
| Widerspruch | 1 Monat ab Ablehnung | § 70 VwGO |
| Klage VG | 1 Monat nach Widerspruchsbescheid | § 74 VwGO |
| Untaetigkeit-Klage | 3 Monate | § 75 VwGO |

## Anschluss-Skills

- `umweltrecht-verfahren` — VG-Klage auf Informationszugang
- `klimaklagen-verbandsklage-umwrg` — NGO-Strategie Umweltinformation
- `fachanwalt-verwaltungsrecht-anfechtungsklage` — Klage gegen Ablehnung
