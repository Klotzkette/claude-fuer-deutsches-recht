---
name: simulation-training-verjaehrung-zustellung
description: "Simulation Training Verjaehrung Zustellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Simulation Training Verjaehrung Zustellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Simulation Training Verjaehrung Zustellung** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehrsowi-simulation-training` | Simulationstraining für OWi-Mandate. Uebungsszenarien Messverfahren Rotlicht Handy Alkohol Fahreridentifizierung. Rollenspiel Mandantengespraeche Hauptverhandlung. Fallvarianten mit Erwartungshorizont. Training ohne echte Mandatsdaten. |
| `verkehrsowi-verjaehrung-zustellung` | Verfolgungsverjährung im OWi-Verfahren prüfen: Anwalt will Verjährungseinwand erheben. Normen: § 26 StVG i.V.m. § 31 OWiG (Verjährungsfrist 3 Monate nach Tatende), § 33 OWiG (Unterbrechungshandlungen), absolute Verjährung 6 Monate. Prüfraster: Tatdatum, Unterbrechungshandlungen, Zustellungsmaengel als Verjährungseinwand, Absolute-Verjährungs-Frist. Output Verjährungs-Berechnungs-Memo, Einwand-Schrift. Abgrenzung: Einspruchsfrist siehe verkehrsowi-fristen-einspruch; Zustellungsfehler siehe verkehrsowi-anhoerung-bußgeldbescheid. |
| `verkehrsowi-zeugen-polizei-strategie` | Zeugen-Strategie gegenüber Polizeibeamten im OWi-Verfahren: Polizeibeamter als einziger Zeuge in der HV. Normen: § 240 StPO i.V.m. § 71 OWiG (Fragerecht), §§ 373 ff. StPO (Zeugenvernehmung). Prüfraster: Aussage-Konstanz (Protokoll vs. HV), Erinnerungsfähigkeit Routine-OWi, Vorhalt frueherer Aussage, Sachverständiger Aussage-Glaubwürdigkeit. Output Fragenkatalog für Polizeizeugen-Vernehmung, Strategie-Memo. Abgrenzung: Fahreridentifizierung siehe verkehrsowi-fahreridentifizierung; HV-Gesamt siehe verkehrsowi-hauptverhandlung-amtsgericht. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Simulation Training Verjaehrung Zustellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehrsowi-simulation-training`

**Fokus:** Simulationstraining für OWi-Mandate. Uebungsszenarien Messverfahren Rotlicht Handy Alkohol Fahreridentifizierung. Rollenspiel Mandantengespraeche Hauptverhandlung. Fallvarianten mit Erwartungshorizont. Training ohne echte Mandatsdaten.

# Simulationstraining OWi-Mandate

## Zweck

Dieser Skill ermoeglicht das Training von OWi-Mandatsbearbeitung ohne echte Mandantendaten. Alle genannten Personen, Aktenzeichen und Umstaende sind frei erfunden und dienen nur dem Lernzweck.

## Uebungsszenario 1: Geschwindigkeitsverstos

**Sachverhalt (simuliert):**
Max Mustermann, wohnhaft in Musterstadt, erhielt am 15.03.2024 einen Bussgeldbescheid ueber 120 EUR und 1 Punkt. Er soll am 01.02.2024 auf der B27 in Musterstadt mit 64 km/h bei erlaubten 50 km/h gefahren sein. Messgeraet: ESO ES 3.0. Zustellung: 15.03.2024 per Einwurf-Einschreiben.

**Aufgaben:**
1. Einspruchsfrist berechnen: Zustellung 15.03.2024 + 14 Tage = 29.03.2024
2. Toleranzabzug pruefen: Gemessen 64 km/h; Abzug 3 km/h → vorwerfbar 61 km/h; Ueberschreitung 11 km/h → 120 EUR und 1 Punkt korrekt nach BKatV?
3. Messakte-Inhalt anfordern: Eichschein, Protokoll, Schulung, Rohmessdaten
4. Einspruchsschreiben formulieren

**Erwartungshorizont:**
- Fristende 29.03.2024 (§ 67 Abs. 1 OWiG + § 33 OWiG, § 180 ZPO)
- Vorwerfbare Geschwindigkeit 61 km/h = 11 km/h Ueberschreitung → BKatV Nr. 11.3.3 = 80 EUR, 1 Punkt — Bescheid koennte zu hoch sein!
- Messakte-Anforderung: Standardformulierung
- Einspruch: unbeschraenkt, Akteneinsicht gleichzeitig

## Uebungsszenario 2: Rotlicht qualifiziert

**Sachverhalt (simuliert):**
Lena Beispiel erhielt einen Bussgeldbescheid: qualifiziertes Rotlicht (> 1 Sekunde), 200 EUR + Fahrverbot 1 Monat + 2 Punkte. Zeugen: zwei Polizeibeamte, kein Videobeweis.

**Aufgaben:**
1. Beweislage analysieren: Wie wurde die Rotphasendauer von > 1 Sekunde festgestellt?
2. Angriffspunkt: Polizeibeamten koennen Sekunden nicht exakt schaetzen
3. Sachverstaendigenantrag formulieren fuer Rotphasendauer-Messung
4. Haertefall-Argumentation prufen (Lena ist Krankenpflegerin, benoetigt Auto)

**Erwartungshorizont:**
- Zeugenaussage zur Rotphasendauer angreifbar wenn keine technische Messung
- Sachverstaendigenantrag: "Zeuge kann Rotphasendauer von > 1 Sekunde nicht exakt einschaetzen; Messung der Ampelphasendauer durch technischen Sachverstaendigen beantragt"
- Haertefall: Krankenhaus-Arbeitgeberbescheinigung + Schichtplan ohne OEPNV-Option

## Uebungsszenario 3: Handy am Steuer

**Sachverhalt (simuliert):**
Karl Probefall, Bussgeld 100 EUR, 1 Punkt. Polizeibeamter sah ihn an einer roten Ampel (Fahrzeug stand) mit Handy in der Hand.

**Rechtsfrage:** Verstos nach § 23 Abs. 1a StVO wenn Fahrzeug steht?

**Erwartungshorizont:**
- BGH 2019: § 23 Abs. 1a StVO gilt auch an der roten Ampel wenn Motor laeuft; nur bei ausgeschaltetem Motor kein Verstos
- Wenn Motor lief: Verstos begruendet
- Wenn Motor aus: kein Verstos; Polizeibeamten befragen ob Motor lief

## Rollenspiel-Szenarien

**Mandantengespraeach (Simulation):**
"Herr Anwalt, ich hatte das Handy nur kurz in der Hand um zu schauen ob ich eine Nachricht habe. Das ist doch kein Problem?"
→ Antwort: Erklaerung § 23 Abs. 1a StVO, BGH-Urteil, Empfehlung Einspruch.

**Hauptverhandlung (Simulation):**
Polizeibeamter sagt aus: "Ich sah das Fahrzeug mit 80 km/h und sicher mehr als eine Sekunde bei Rot."
→ Frage: "Koennen Sie mir erklaeren wie Sie exakt eine Sekunde messen konnten?"

## Harte Leitplanken

- Simulationsdaten niemals als echte Praezedenzfaelle ausgeben.
- Ergebnisse aus Simulation immer mit tatsaechlicher Rechtslage abgleichen.
- Anwaltliche Endkontrolle vor Uebertragung auf echte Mandate.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `verkehrsowi-verjaehrung-zustellung`

**Fokus:** Verfolgungsverjährung im OWi-Verfahren prüfen: Anwalt will Verjährungseinwand erheben. Normen: § 26 StVG i.V.m. § 31 OWiG (Verjährungsfrist 3 Monate nach Tatende), § 33 OWiG (Unterbrechungshandlungen), absolute Verjährung 6 Monate. Prüfraster: Tatdatum, Unterbrechungshandlungen, Zustellungsmaengel als Verjährungseinwand, Absolute-Verjährungs-Frist. Output Verjährungs-Berechnungs-Memo, Einwand-Schrift. Abgrenzung: Einspruchsfrist siehe verkehrsowi-fristen-einspruch; Zustellungsfehler siehe verkehrsowi-anhoerung-bußgeldbescheid.

# Verfolgungsverjaehrung und Zustellungsmaengel — § 31 OWiG

## Triage zu Beginn

1. **Wann war das angebliche Tatdatum?** — Verjaerunsfrist laeuft ab Tatende.
2. **Frist bei § 24 StVG / § 26a StVG?** — § 26 Abs. 3 StVG: 3 Monate Verjaerunsfrist fuer einfache Verkehrs-OWi.
3. **Unterbrechungshandlungen geprueft?** — § 33 OWiG: Anhoerung des Betroffenen, Bussgeldbescheid, Eingang Einspruch — unterbrechen Verjaehrung.
4. **Absolute Verjaehrung?** — § 33 Abs. 3 OWiG: absolute Verjaehrung = doppelte ordentliche Frist (bei 3-Monats-Frist: 6 Monate).
5. **Zustellungsfehler moeglich?** — Fehlerhafte Zustellung unterbricht die Verjaehrung nicht; Bescheid gilt als nicht zugestellt.

## Zentrale Normen

- **§ 31 OWiG** — Verfolgungsverjaehrung im OWi-Verfahren (allgemein); Grundfrist 3 Jahre fuer alle OWi
- **§ 26 Abs. 3 StVG** — Verkehrs-OWi: 3 Monate Verjaerunsfrist ab Tatende (abgekuerzt gegenueber § 31 OWiG)
- **§ 33 OWiG** — Unterbrechungshandlungen: Anhoerung, Bussgeldbescheid, Einspruch, Hauptverhandlungstermin
- **§ 33 Abs. 3 OWiG** — Absolute Verjaehrung: Doppelte ordentliche Frist; faengt nach jeder Unterbrechung neu an, aber nie nach absoluter Frist
- **§ 28 OWiG** — Bekanntgabe des Bussgeldbescheids; fehlerhafte Bekanntgabe = keine Unterbrechung
- **§ 33 OWiG i.V.m. §§ 177-182 ZPO** — Zustellungsvorschriften

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verjaerungs-Pruefschema

```
1. Tatdatum: [DATUM]
2. Verjaehrungsfrist:
 - Verkehrs-OWi § 26 Abs. 3 StVG: 3 Monate
 - Andere OWi § 31 OWiG: 3 Jahre
3. Erste Verjaerungs-Deadline: Tatdatum + [Frist]
4. Unterbrechungshandlungen nach § 33 OWiG:
 - Anhoerungsschreiben: Datum + Zustellungsnachweis?
 - Bussgeldbescheid: Datum + Zustellungsnachweis?
5. Neue Verjaerungs-Deadline nach letzter Unterbrechung
6. Absolute Verjaehrung: Doppelte Grundfrist ab Tatende
 - Bei 3 Monaten: 6 Monate ab Tatende
7. Ist absolute Verjaehrung abgelaufen? → Einstellung zwingend!
```

## Zustellungsmaengel als Verteidigung

```
Zustellungsform pruefen:
□ PZU (Postzustellungsurkunde): ordnungsgemaesse Haushaltszustellung?
□ Einwurf-Einschreiben: Beweis des Einwurfs durch Einschreib-Beleg?
□ Persoenliche Uebergabe: quittiert?
□ Zustellung an falschen Empfaenger?

Wenn Zustellungsmangel vorliegt:
→ Unterbrechung nach § 33 OWiG ist NICHT eingetreten
→ Verjaehrungsfrist lief ununterbrochen weiter
→ Moegliche Verjaehrung pruefen und Einstellung beantragen
```

## Harte Leitplanken

- Verjaehrungseinwand ist Prozesshindernis — von Amts wegen zu beachten, muss aber in der Regel gerueagt werden.
- Absolute Verjaehrung (§ 33 Abs. 3 OWiG) kann nicht durch neue Unterbrechungen ueberschritten werden.
- Zustellungsmangel-Prufung ist Standardbestandteil jedes OWi-Mandats.
- Anwaltliche Endkontrolle bei Verjaerungs-Berechnung.

## 3. `verkehrsowi-zeugen-polizei-strategie`

**Fokus:** Zeugen-Strategie gegenüber Polizeibeamten im OWi-Verfahren: Polizeibeamter als einziger Zeuge in der HV. Normen: § 240 StPO i.V.m. § 71 OWiG (Fragerecht), §§ 373 ff. StPO (Zeugenvernehmung). Prüfraster: Aussage-Konstanz (Protokoll vs. HV), Erinnerungsfähigkeit Routine-OWi, Vorhalt frueherer Aussage, Sachverständiger Aussage-Glaubwürdigkeit. Output Fragenkatalog für Polizeizeugen-Vernehmung, Strategie-Memo. Abgrenzung: Fahreridentifizierung siehe verkehrsowi-fahreridentifizierung; HV-Gesamt siehe verkehrsowi-hauptverhandlung-amtsgericht.

# Polizeibeamten als Zeugen im OWi-Verfahren

## Triage zu Beginn

1. **Welche Beamten sind als Zeugen geladen?** — Messbeamter, Beobachtungsbeamter (bei Rotlicht/Handy), Anhaltebeamter.
2. **Haben die Beamten ein Protokoll gefuehrt?** — Datum, Uhrzeit, Messort, Geraet, Bemerkungen.
3. **Gibt es Inkonsistenzen zwischen Protokoll und zu erwartender HV-Aussage?** — Vermeintliche Erinnerung vs. Protokoll-Wiedergabe.
4. **Sind mehrere Beamte taetig geworden?** — Arbeitsteilung: Messbeamter vs. Anhaltebeamter vs. Schreiber.
5. **Lag Routine-Masse an OWi-Faellen vor?** — Massenhaftes Aufschreiben von OWi-Verfahren senkt individuelle Erinnerungsqualitaet.

## Zentrale Normen

- **§ 48 StPO i.V.m. § 46 OWiG** — Zeugenpflicht: Beamte sind auch als Zeugen verpflichtet
- **§ 68a StPO i.V.m. § 71 OWiG** — Vorleben des Zeugen (Vorstrafen) darf erfragt werden
- **§ 240 StPO i.V.m. § 71 OWiG** — Fragerecht aller Beteiligter
- **§ 249 StPO i.V.m. § 71 OWiG** — Urkundsbeweis; Protokolle und Berichte verlesen
- **§ 254 StPO i.V.m. § 71 OWiG** — Vorhalt: frueherer Wortlaut darf vorgehalten werden

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Fragestrategie Polizeibeamter-Zeuge

### Einstiegsfragen (neutral)
- "Wann und wo haben Sie den Messvorgang durchgefuehrt?"
- "Koennen Sie sich an diesen konkreten Fall erinnern, oder lesen Sie aus dem Protokoll?"
- "Wie viele Messungen haben Sie an diesem Tag durchgefuehrt?"

### Vertiefungsfragen (Erinnerung pruefen)
- "Beschreiben Sie bitte das Fahrzeug des Betroffenen ohne in Ihre Unterlagen zu schauen."
- "Koennen Sie die Kleidung oder das Aussehen des Fahrers beschreiben?"
- "War das Messfoto klar genug um den Fahrer eindeutig zu identifizieren?"

### Technik-Fragen (Messverfahren)
- "Haben Sie eine Einweisung in das Messgeraet [Modell] erhalten?"
- "Koennen Sie mir den genauen Standort der Messanlage auf einer Karte zeigen?"
- "Wurden vor und nach der Messung Kontrollmessungen durchgefuehrt?"

### Vorhalt-Fragen (Inkonsistenz)
- "In Ihrem Protokoll vom [DATUM] haben Sie [X] notiert. Jetzt sagen Sie [Y]. Wie erklaeren Sie das?"

## Schritt-fuer-Schritt-Vorbereitung

1. **Protokolle der Polizeibeamten vollstaendig aus der Akte entnehmen.**
2. **Inkonsistenzen zwischen Protokoll und Stellungnahmen markieren.**
3. **Frageliste erstellen** — offene Fragen zuerst, dann konkrete Vorhalt-Fragen.
4. **In der HV:** Sachlich und respektvoll bleiben; Ziel ist Glaubwuerdigkeitserschuetterung, nicht Konfrontation.
5. **Protokollnotiz:** Wichtige Antworten sofort in der HV notieren.

## Harte Leitplanken

- Keine Fragen stellen, deren Antwort unbekannt und schaedlich sein koennte.
- Vorhalt nur mit konkreter Fundstelle in der Akte.
- Polizeibeamten haben grundsaetzlich nicht mehr Glaubwuerdigkeit als andere Zeugen — aber das ist in der HV oft zu betonen.
- Anwaltliche Endkontrolle bei Frageliste vor HV.
