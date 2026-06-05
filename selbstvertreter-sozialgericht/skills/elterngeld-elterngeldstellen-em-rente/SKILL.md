---
name: elterngeld-elterngeldstellen-em-rente
description: "Elterngeld Elterngeldstellen EM Rente: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elterngeld Elterngeldstellen EM Rente

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Elterngeld Elterngeldstellen EM Rente** im Plugin Selbstvertretung vor dem Sozialgericht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elterngeld-elterngeldstellen-beeg` | Elterngeld nach dem BEEG. Skill klaert die Voraussetzungen Hoehe (Basiselterngeld ElterngeldPlus Partnerschaftsbonus) Antrag bei der Elterngeldstelle Sondervorschriften fuer Selbststaendige und Mehrkindersituationen. Liefert Pruefraster. |
| `em-rente-medizinische-feststellung` | Erwerbsminderungsrente medizinische Feststellung. Skill klaert die Voraussetzungen volle EM-Rente teilweise EM-Rente versicherungsrechtliche Voraussetzungen 5-Jahres-Wartezeit 3-Jahres-Belegungspflicht. Aktuelle Reform Anhebung des Zugangsfaktors. Liefert Pruefraster. |
| `entschaedigung-sgb-xiv-opferleistungen` | Soziales Entschaedigungsrecht SGB XIV seit 2024. Opfer von Gewalttaten Anerkennung Entschaedigung Reha. Reform OEG/BVG. Praktischer Leitfaden für Betroffene. |
| `erstattung-zu-unrecht-50-sgb-x` | Erstattung zu Unrecht erbrachter Leistungen nach § 50 SGB X. Skill klaert wann der Buerger zurueckzahlen muss Voraussetzungen Hoehe Aufrechnung und Verhaeltnis zu Stundung oder Erlass. Liefert Verteidigungsbausteine. |
| `erwerbsminderungs-rente-streit-sgb-vi` | EM-Rente nach §§ 43 240 SGB VI. Volle teilweise EM Wartezeit Pflichtbeitraege Berufsschutz vor 1961. Strategie für Buerger bei Ablehnung durch DRV. |

## Arbeitsweg

Im Plugin Selbstvertretung vor dem Sozialgericht gilt für **Elterngeld Elterngeldstellen EM Rente**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elterngeld-elterngeldstellen-beeg`

**Fokus:** Elterngeld nach dem BEEG. Skill klaert die Voraussetzungen Hoehe (Basiselterngeld ElterngeldPlus Partnerschaftsbonus) Antrag bei der Elterngeldstelle Sondervorschriften fuer Selbststaendige und Mehrkindersituationen. Liefert Pruefraster.

# Elterngeld Elterngeldstellen Beeg

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Elterngeld Elterngeldstellen Beeg` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Anspruch

§ 1 BEEG: Anspruch auf Elterngeld bei Geburt eines Kindes.

## Hoehe

### Basiselterngeld
- 67 Prozent des Nettoeinkommens vor Geburt.
- Mindestbetrag 300 Euro/Monat, Hoechstbetrag 1800 Euro/Monat.
- Bezugszeit max. 14 Monate (12 bei einem Elternteil, 12 + 2 Partnermonate).

### ElterngeldPlus
- Halber Monatsbetrag, doppelter Bezugszeit.
- Bei Teilzeit waehrend Bezug attraktiv.

### Partnerschaftsbonus
- 4 zusaetzliche ElterngeldPlus-Monate bei beidseitiger Teilzeit von 24-32 Stunden.

## Antrag

- Bei der Elterngeldstelle (Land/Kommune).
- Innerhalb 3 Monate ab Geburt — sonst Rueckwirkung nur 3 Monate.

## Selbststaendige

- Berechnung aus Gewinn des Kalenderjahrs vor Geburt.

## Mehrkindersituationen

- Geschwisterbonus bei mehreren Kindern unter 3 Jahre (10 Prozent, mindestens 75 Euro).
- Mehrlingszuschlag.

## Pruefraster

1. Antrag rechtzeitig?
2. Hoehenberechnung richtig?
3. Basiselterngeld vs. Plus?
4. Geschwisterbonus / Mehrlingszuschlag?
5. Selbststaendigen-Sondervorschriften?

## 2. `em-rente-medizinische-feststellung`

**Fokus:** Erwerbsminderungsrente medizinische Feststellung. Skill klaert die Voraussetzungen volle EM-Rente teilweise EM-Rente versicherungsrechtliche Voraussetzungen 5-Jahres-Wartezeit 3-Jahres-Belegungspflicht. Aktuelle Reform Anhebung des Zugangsfaktors. Liefert Pruefraster.

# Em Rente Medizinische Feststellung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Em Rente Medizinische Feststellung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Voraussetzungen

§ 43 SGB VI.

### Medizinisch
- Volle EM-Rente: Erwerbsfaehigkeit unter 3 Stunden taeglich.
- Teilweise EM-Rente: Erwerbsfaehigkeit 3-6 Stunden taeglich.

### Versicherungsrechtlich
- Allgemeine Wartezeit von 5 Jahren erfuellt.
- In den letzten 5 Jahren vor Eintritt der EM mindestens 3 Jahre Pflichtbeitraege.

## Verfahren

1. Antrag bei DRV.
2. Aerztliche Unterlagen.
3. Gutachten durch DRV-Aerzte.
4. Bescheid.

## Reha vor Rente

§ 9 SGB VI: DRV pruef zuerst Reha. EM-Rente nur, wenn Reha nicht moeglich oder erfolglos.

## Zugangsfaktor

- Bei Eintritt vor Erreichen Regelaltersgrenze Zugangsfaktor < 1.
- Reform 2014/2018/2024 — Anhebung der Zugangsfaktor-Grenze.

## Befristung

- EM-Rente regelmaessig 3 Jahre befristet.
- Nach 9 Jahren ggf. unbefristet.
- Pruefantraege Behoerden initiative.

## Hinzuverdienst

- Hinzuverdienstgrenze hat sich 2023 erheblich erweitert.
- Aktuelle Werte live verifizieren.

## Pruefraster

1. Medizinische Voraussetzung?
2. Versicherungsrechtliche Voraussetzung?
3. Reha gepruef?
4. Befristung beachtet?
5. Hinzuverdienst?

## 3. `entschaedigung-sgb-xiv-opferleistungen`

**Fokus:** Soziales Entschaedigungsrecht SGB XIV seit 2024. Opfer von Gewalttaten Anerkennung Entschaedigung Reha. Reform OEG/BVG. Praktischer Leitfaden für Betroffene.

# Soziales Entschaedigungsrecht — SGB XIV

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Soziales Entschaedigungsrecht — SGB XIV` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Seit 1.1.2024 gilt das neue SGB XIV (Soziale Entschaedigung). Es ersetzt das alte Opferentschaedigungsgesetz (OEG) und das Bundesversorgungsgesetz (BVG). Wer Opfer einer Gewalttat geworden ist, kann hier Hilfe bekommen.

## In einfacher Sprache

Wenn Sie Opfer einer Gewalttat geworden sind, hilft das SGB XIV. Es gibt Geld und Therapie. Sie muessen das beim Versorgungsamt beantragen. Wir zeigen den Weg.

## Wann brauchen Sie diese Skill?

- Sie sind Opfer einer Gewalttat geworden.
- Sie haben gesundheitliche Folgen.
- Ihr Antrag auf Entschaedigung wurde abgelehnt.

## Fachbegriffe (kurz erklaert)

- **Schaedigung**: Gesundheitlicher Schaden durch Gewalttat.
- **Gesundheitliche Folge**: Erkrankung als Folge.
- **Grad der Schaedigungsfolgen (GdS)**: aehnlich GdB, aber spezifisch fuer SGB XIV.
- **Schnelle Hilfe**: Sofortige Therapieangebote (Trauma-Therapie ohne langwierige Anerkennung).

## Rechtsgrundlagen

- **§ 1 SGB XIV** — Anspruchsberechtigung.
- **§ 14 SGB XIV** — Gesundheitsleistungen.
- **§ 88 SGB XIV** — Schnelle Hilfen.
- **Uebergangsregelungen**: Alte OEG/BVG-Faelle laufen weiter.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Anspruchspruefung

- Opfer einer in Deutschland begangenen Gewalttat (auch psychische Gewalt anerkannt unter Voraussetzungen)
- Oder: Hinterbliebene, Angehoerige
- Schaedigung als Folge (koerperlich oder psychisch)

### Schritt 2 — Strafanzeige sinnvoll

Bei Gewalttat: Strafanzeige bei Polizei. Akte hilft im Verfahren.

### Schritt 3 — Antrag stellen

Beim Versorgungsamt (oder Bezirksregierung — Land je nach Bundesland):

- Schriftlicher Antrag mit Schilderung der Tat
- Polizei-Akte / Aktenzeichen
- Aerztliche Atteste zu Folgen
- Therapie-Berichte

### Schritt 4 — Schnelle Hilfen

§ 88 SGB XIV: Auch ohne abgeschlossene Anerkennung gibt es Trauma-Therapie (Soforthilfe). Antragen bei Versorgungsamt.

### Schritt 5 — Bei Ablehnung Widerspruch

```
Versorgungsamt / Bezirksregierung [...] [Ort, Datum]

Az: [...]

Widerspruch gegen den Bescheid vom [Datum]

Sehr geehrte Damen und Herren,

gegen den o.g. Bescheid lege ich Widerspruch ein.

Begruendung:

1. Tatbestand der Gewalttat
 Am [Datum] erfolgte gegen mich Gewalttat in Form von [...]. Polizei-Akte Az [...].

2. Gesundheitliche Folgen
 Diagnosen:
 - PTBS (ICD F43.1) - Diagnose-Datum [...]
 - Depression (F33) - Diagnose-Datum [...]
 - [koerperliche Folgen]
 Belege: Atteste Dr. [Name], Therapeutin Dr. [Name].

3. Ursaechlichkeit
 Die psychischen Folgen sind nach aerztlicher Einschaetzung ursaechlich auf die Gewalttat zurueckzufuehren.

4. GdS Bewertung
 Nach Versorgungsmedizinischen Grundsaetzen ist GdS mindestens [Wert] gegeben.

Mit freundlichen Gruessen
```

### Schritt 6 — Klage am SG

Wie bei anderen Sozialleistungen.

### Schritt 7 — Beweisstrategie

- Polizei-Akte
- Zeugen
- Aerzte / Therapeuten
- Opferberatungs-Stellen (Weisser Ring, Hilfetelefon Gewalt gegen Frauen)

## Worauf Sie besonders achten muessen

- **Reform 2024**: Anwendungsbereich erweitert (auch psychische Gewalt unter Voraussetzungen). Pruefen Sie aktuellen Stand.
- **Schnelle Hilfen** § 88 SGB XIV: nicht vergessen, niedrige Schwelle.
- **Opferentschaedigung kann lange dauern**: parallel Therapie und Krankenkassen-Behandlung.
- **Trauma-Diagnose**: wichtig fuer psychische Folgen.

## Typische Fehler

- Keine Strafanzeige → schwerer Beweis
- Folgen erst spaet beanstandet → Latenz erschwert Kausalitaet
- Therapie-Berichte fehlen → wichtig
- Behoerden-Bezeichnung verwechselt → je Land unterschiedlich

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `widerspruch-vorverfahren-78-sgg` — Widerspruch
- `verpflichtungsklage-54-sgg` — Klage
- `arztberichte-vorlegen-laien-leitfaden` — Atteste
- `medizinische-gutachten-strategie-laien` — Gutachten

## Quellen und Aktualitaet

Stand: 05/2026. SGB XIV in Kraft seit 1.1.2024 (Reform OEG/BVG). Uebergangsregelungen pruefen. BSG-Linien noch im Aufbau. Bei diesem neuen Recht besonders sorgfaeltig pruefen — Verifikation in juris empfohlen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `erstattung-zu-unrecht-50-sgb-x`

**Fokus:** Erstattung zu Unrecht erbrachter Leistungen nach § 50 SGB X. Skill klaert wann der Buerger zurueckzahlen muss Voraussetzungen Hoehe Aufrechnung und Verhaeltnis zu Stundung oder Erlass. Liefert Verteidigungsbausteine.

# Erstattung Zu Unrecht 50 Sgb X

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstattung Zu Unrecht 50 Sgb X` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Tatbestand § 50 SGB X

- Verwaltungsakt wurde aufgehoben (zumeist nach § 45 oder § 48 SGB X).
- Bisher gezahlte Leistungen sind dann zurueckzuerstatten.

## Hoehe

- Der zu Unrecht erbrachte Betrag.
- Zinsen ab Bekanntgabe der Erstattungsforderung (§ 50 Abs. 3 SGB X).

## Verteidigung

1. **Aufhebungsbescheid angreifen**: Wenn die Aufhebung selbst rechtswidrig ist, faellt auch die Erstattung weg.
2. **Vertrauensschutz**: § 45 SGB X — Vertrauensschutz schliesst Aufhebung aus, dann auch keine Erstattung.
3. **Verjaehrung**: § 50 Abs. 4 SGB X — 4 Jahre nach Ablauf des Kalenderjahrs der Bekanntgabe.
4. **Aufrechnung**: § 51 SGB I — Behoerde rechnet die Forderung mit kuenftigen Leistungen auf. Pruefen ob Pfaendungsfreigrenze gewahrt.

## Stundung und Erlass

- Stundung: § 76 Abs. 2 Nr. 1 SGB IV.
- Erlass: § 76 Abs. 2 Nr. 3 SGB IV (Haerteklausel).
- Antrag schriftlich bei der Behoerde — Beleg der wirtschaftlichen Lage.

## Pruefraster

1. Aufhebungsbescheid bestandskraeftig?
2. Hoehe nachvollziehbar berechnet?
3. Vertrauensschutz vorgebracht?
4. Verjaehrung pruefen?
5. Aufrechnung — Pfaendungsfreigrenze?
6. Erlass moeglich?

## 5. `erwerbsminderungs-rente-streit-sgb-vi`

**Fokus:** EM-Rente nach §§ 43 240 SGB VI. Volle teilweise EM Wartezeit Pflichtbeitraege Berufsschutz vor 1961. Strategie für Buerger bei Ablehnung durch DRV.

# Erwerbsminderungs-Rente — Streit mit der Rentenversicherung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erwerbsminderungs-Rente — Streit mit der Rentenversicherung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Sie koennen wegen Krankheit nicht mehr richtig arbeiten. Sie haben EM-Rente beantragt — und die DRV hat abgelehnt. Diese Skill zeigt, wie Sie Widerspruch und Klage fuehren.

## In einfacher Sprache

Sie koennen nicht mehr arbeiten. Sie wollten Rente wegen Krankheit. Die Rentenversicherung hat Nein gesagt. Wir zeigen Ihnen den Weg.

## Wann brauchen Sie diese Skill?

- DRV hat EM-Rente abgelehnt.
- Sie sind unsicher, ob Sie die Voraussetzungen erfuellen.
- Sie wollen Klage einreichen.

## Fachbegriffe (kurz erklaert)

- **EM-Rente**: Rente wegen Erwerbsminderung.
- **Volle EM**: Leistungsvermoegen unter 3 Stunden taeglich.
- **Teilweise EM**: 3 bis unter 6 Stunden taeglich.
- **Berufsschutz § 240 SGB VI**: Schutz im bisherigen Beruf (nur Jahrgaenge vor 02.01.1961).
- **Wartezeit**: 5 Jahre Versicherungspflicht.
- **Verschlossener Teilzeitarbeitsmarkt**: BSG-Konstruktion, dass 3-6h-Personen oft volle EM bekommen.

## Rechtsgrundlagen

- **§ 43 SGB VI** — EM-Rente (volle und teilweise).
- **§ 240 SGB VI** — Berufsschutz fuer Altjahrgaenge.
- **§ 50 SGB VI** — Allgemeine Wartezeit.
- **§ 99 SGB VI** — Rentenbeginn.
- **§ 109 SGG** — eigenes Gutachten.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Voraussetzungen pruefen

**Versicherungsrechtliche Voraussetzungen** (§ 43 Abs. 1 Nr. 2-3 SGB VI):

- 5 Jahre allgemeine Wartezeit (§ 50 SGB VI)
- 3 Jahre Pflichtbeitraege in den letzten 5 Jahren vor Eintritt der Erwerbsminderung

Wenn nicht erfuellt: keine EM-Rente — ausser Sonderregeln (z.B. § 53 SGB VI Sondertatbestaende bei Wehrdienst etc.).

**Medizinische Voraussetzungen** (§ 43 Abs. 2 SGB VI):

- Volle EM: weniger als 3 Stunden taeglich Erwerbstaetigkeit auf dem allgemeinen Arbeitsmarkt
- Teilweise EM: 3 bis unter 6 Stunden

### Schritt 2 — Versicherungsverlauf anfordern

Bei der DRV per Anfrage. Pruefen Sie:

- Liegen 5 Jahre Wartezeit vor?
- Liegen 3 Jahre Pflichtbeitraege in den letzten 5 Jahren vor?
- Falls Luecken: Anrechnungszeiten? Kindererziehungszeiten?

### Schritt 3 — Medizinische Belege sammeln

- Hausarzt
- Facharzt (mehrere)
- Reha-Berichte
- Krankenhaus-Berichte
- AU-Zeiten

Verlauf darstellen: Wann begann die Verschlechterung? Welche Therapien wurden versucht?

### Schritt 4 — Widerspruch

```
Deutsche Rentenversicherung [Traeger] [Ort, Datum]

Versicherungs-Nr: [...]

Widerspruch gegen den Bescheid vom [Datum]

Sehr geehrte Damen und Herren,

gegen den o.g. Bescheid lege ich

 Widerspruch

ein.

Vorlaeufige Begruendung:

1. Versicherungsrechtliche Voraussetzungen erfuellt
 - Wartezeit 5 Jahre erfuellt seit [Datum]
 - 3 Jahre Pflichtbeitraege in den letzten 5 Jahren vor [Datum der Erwerbsminderung]

2. Medizinische Voraussetzungen
 - Diagnosen: [Liste mit ICD-Codes]
 - Aktuelles Leistungsvermoegen: weniger als 3 Stunden taeglich
 - Belege: Atteste meines Hausarztes Dr. [Name] vom [Datum] und Facharztes Dr. [Name] vom [Datum]

3. Verschlossener Teilzeitarbeitsmarkt (hilfsweise)
 Sollte ein Leistungsvermoegen von 3 bis unter 6 Stunden angenommen werden, ist der Teilzeitarbeitsmarkt fuer mich verschlossen.

4. Berufsschutz § 240 SGB VI (falls Jahrgang vor 02.01.1961)
 Berufsschutz ist gegeben.

Beigefuegt:
- Aerztliche Befundberichte
- Reha-Entlassungsbericht
- Schweigepflichtsentbindung

Mit freundlichen Gruessen
```

### Schritt 5 — Klage einreichen

Wenn Widerspruch erfolglos: kombinierte Anfechtungs- und Verpflichtungsklage (siehe `verpflichtungsklage-54-sgg`).

### Schritt 6 — Im SG-Verfahren

- Gericht holt Befundberichte ein.
- Gericht beauftragt Gutachter (meist Orthopaedie, Innere, Psychiatrie).
- Untersuchungs-Termin.
- Bei negativem Gutachten: § 109-Gutachten erwaegen.

### Schritt 7 — Beim Berufsschutz argumentieren

Nur bei Jahrgang vor 02.01.1961. Sonst irrelevant. Pruefen Sie genau die Definition Ihres "bisherigen Berufs" — qualifizierte Berufstaetigkeit.

## Worauf Sie besonders achten muessen

- **Versicherungsverlauf zwingend pruefen** — wenn die Voraussetzungen nicht erfuellt sind, ist EM-Rente nicht moeglich.
- **Befristete EM-Rente** § 102 SGB VI: meist 3 Jahre, Verlaengerung moeglich.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Krankengeld-Ende** als Trigger: oft erfolgt EM-Antrag erst nach Aussteuerung.

## Typische Fehler

- "Ich kann nicht mehr arbeiten" ohne konkrete Stundenangabe → konkret
- Versicherungsverlauf nicht geprueft → Grundvoraussetzung
- Berufsschutz fuer falschen Jahrgang behauptet → nur vor 02.01.1961
- Reha-Bericht ignoriert → wichtigster Beleg

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `verpflichtungsklage-54-sgg` — Klageform
- `arztberichte-vorlegen-laien-leitfaden` — Atteste
- `medizinische-gutachten-strategie-laien` — Gutachten
- `sachverstaendigen-wahlrecht-109-sgg` — eigenes Gutachten
- `widerspruch-gegen-gutachten-laien` — Reaktion auf Gutachten

## Quellen und Aktualitaet

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
