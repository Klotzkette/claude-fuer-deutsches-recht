---
name: kfe-restrukturierungsbeauftragter
description: "KFE Restrukturierungsbeauftragter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KFE Restrukturierungsbeauftragter

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **KFE Restrukturierungsbeauftragter** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kfe-restrukturierungsbeauftragter-spezial` | Spezialfall Restrukturierungsbeauftragter §§ 73 ff. StaRUG: Bestellung, Aufgaben, Haftung, Kosten. Pruefraster fuer Geschaeftsleitung und Glaeubigerausschuss. |
| `kfe-stabilisierungsanordnung-spezial` | Spezialfall Stabilisierungsanordnung §§ 49 ff. StaRUG: Verwertungs- und Vollstreckungssperre, Voraussetzungen, Befristung. Pruefraster fuer Antragsteller und betroffene Glaeubiger. |
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW-S-6-Krisenstadien diagnostizieren und Handlungskorridore bestimmen: Berater oder GF will Krisenstadium und passende Massnahmen ermitteln. Normen: IDW S 6 (Sanierungsstandard: Stakeholder-, Strategie-, Produkt-, Ertrags-, Liquiditaetskrise), § 1 StaRUG. Prüfraster: Erkennungsmerkmale je Stadium, Diagnose-Checklisten, Handlungskorridore, Eskalationspflichten. Output Krisenstadium-Diagnose, Massnahmen-Empfehlung je Stadium. Abgrenzung: Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform; Warnpflicht siehe paragraph-102-starug-warnpflicht-bei-rechtsberatern. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **KFE Restrukturierungsbeauftragter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kfe-restrukturierungsbeauftragter-spezial`

**Fokus:** Spezialfall Restrukturierungsbeauftragter §§ 73 ff. StaRUG: Bestellung, Aufgaben, Haftung, Kosten. Pruefraster fuer Geschaeftsleitung und Glaeubigerausschuss.

# KFE: Restrukturierungsbeauftragter

## Spezialwissen: KFE: Restrukturierungsbeauftragter
- **Spezialgegenstand:** KFE: Restrukturierungsbeauftragter / kfe restrukturierungsbeauftragter spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG, KFE, BGH, BVerfG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `kfe-stabilisierungsanordnung-spezial`

**Fokus:** Spezialfall Stabilisierungsanordnung §§ 49 ff. StaRUG: Verwertungs- und Vollstreckungssperre, Voraussetzungen, Befristung. Pruefraster fuer Antragsteller und betroffene Glaeubiger.

# KFE: Stabilisierungsanordnung

## Spezialwissen: KFE: Stabilisierungsanordnung
- **Spezialgegenstand:** KFE: Stabilisierungsanordnung / kfe stabilisierungsanordnung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG, KFE, BGH, BVerfG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet`

**Fokus:** IDW-S-6-Krisenstadien diagnostizieren und Handlungskorridore bestimmen: Berater oder GF will Krisenstadium und passende Massnahmen ermitteln. Normen: IDW S 6 (Sanierungsstandard: Stakeholder-, Strategie-, Produkt-, Ertrags-, Liquiditaetskrise), § 1 StaRUG. Prüfraster: Erkennungsmerkmale je Stadium, Diagnose-Checklisten, Handlungskorridore, Eskalationspflichten. Output Krisenstadium-Diagnose, Massnahmen-Empfehlung je Stadium. Abgrenzung: Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform; Warnpflicht siehe paragraph-102-starug-warnpflicht-bei-rechtsberatern.

# Krisenstadien-Diagnostik — IDW S 6 Stadienlehre

Die Stadienlehre des IDW S 6 ist mehr als ein akademisches Ordnungsraster. Sie ist das Diagnose-Werkzeug, das den Zeitpunkt der Krisenintervention bestimmt — und damit auch den Zeitpunkt, ab dem § 1 StaRUG greift, ab dem Berater warnen müssen und ab dem der Geschäftsführer sein Pflichtenprofil neu kalibrieren muss. Wer das Stadium falsch einschätzt, handelt zu spät — und verliert den Zugang zu den effektiven Sanierungswerkzeugkästen.

---

## Rechtsgrundlagen

- IDW S 6 Tz. 12 ff. (Stadienmodell der Unternehmenskrise)
- § 1 StaRUG (Früherkennungspflicht — schon ab Stakeholderkrise relevant)
- § 18 InsO (drohende Zahlungsunfähigkeit — Liquiditätskrise als Schwelle)
- § 17 InsO (eingetretene Zahlungsunfähigkeit)
- § 19 InsO (Überschuldung)
- § 29 Abs. 2 StaRUG (Zugangsschwelle: drohende ZU muss vorliegen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Pflichten

### 1. Das fünfstufige Stadienmodell

IDW S 6 unterscheidet fünf Krisenstadien, die in der Praxis selten trennscharf sind und sich überlappen können:

```
STADIUM 1: STAKEHOLDERKRISE
 Definition: Vertrauensverlust bei wesentlichen Stakeholdern
 (Gesellschafter, Banken, Schlüsselkunden, Lieferanten, Mitarbeiter)
 Zeitlicher Vorlauf vor Insolvenz: typisch 3-8 Jahre
 StaRUG-Relevanz: § 1 StaRUG grundsätzlich schon auslösbar

STADIUM 2: STRATEGIEKRISE
 Definition: Erosion des strategischen Wettbewerbsvorteils
 (Marktposition, Technologievorsprung, Kundenloyalität)
 Zeitlicher Vorlauf: typisch 2-6 Jahre
 StaRUG-Relevanz: § 1 StaRUG-Pflicht klar ausgelöst, wenn existenzgefährdend

STADIUM 3: PRODUKT-/ABSATZKRISE
 Definition: Nachfragerückgang, Marktanteilsverlust, Preisverfall
 ohne korrigierende strategische Reaktion
 Zeitlicher Vorlauf: typisch 1-4 Jahre
 StaRUG-Relevanz: Erhöhte Eskalationspflicht, § 102 StaRUG für Berater

STADIUM 4: ERTRAGSKRISE
 Definition: Nachhaltig negatives EBIT/EBITDA, Verlustakkumulation,
 Eigenkapitalverzehr
 Zeitlicher Vorlauf: typisch 6-24 Monate
 StaRUG-Relevanz: Drohende ZU oft in Sichtweite, StaRUG-Zugang prüfen

STADIUM 5: LIQUIDITÄTSKRISE
 Definition: Zahlungsunfähigkeit droht oder ist eingetreten;
 Kreditlinien erschöpft, Zulieferer auf Vorkasse
 Zeitlicher Vorlauf: Wochen bis Monate
 StaRUG-Relevanz: Letztes Fenster für StaRUG; danach InsO-Pflicht
```

### 2. Die kritische Schwelle: Wann wird aus Krise ein Insolvenzgrund?

```
ERTRAGSKRISE → Überschuldungsrisiko (§ 19 InsO):
 Wenn Verluste das Eigenkapital aufgezehrt haben und negative
 Fortführungsprognose vorliegt.

LIQUIDITÄTSKRISE → Drohende ZU (§ 18 InsO):
 Wenn die Liquiditätsplanung (24 Monate) zeigt, dass Verbindlichkeiten
 überwiegend wahrscheinlich nicht bedient werden können.

LIQUIDITÄTSKRISE → Eingetretene ZU (§ 17 InsO):
 Wenn fällige Verbindlichkeiten nicht beglichen werden können
 und dies nicht nur vorübergehend ist.
```

---

## Vorgehen

### Schritt 1: Stadien-Schnelldiagnose (Checkliste)

**Stadium 1 — Stakeholderkrise:**
- [ ] Gesellschafter äußern grundsätzliche Kritik am Management?
- [ ] Bank hat Kreditgespräch intensiviert oder Konditionen verschlechtert?
- [ ] Schlüsselkunden haben Aufträge reduziert oder Rahmenverträge nicht verlängert?
- [ ] Schlüsselmitarbeiter haben das Unternehmen verlassen?
- [ ] Lieferanten verlangen verschärfte Zahlungsbedingungen?

**Stadium 2 — Strategiekrise:**
- [ ] Marktanteil sinkt seit mind. zwei Jahren?
- [ ] Wettbewerber haben technologischen Vorsprung aufgeholt oder überholt?
- [ ] Kundenzufriedenheitswerte (NPS, Reklamationsquote) verschlechtern sich?
- [ ] Kernprodukte/Dienstleistungen haben keine klare Differenzierungsstrategie mehr?
- [ ] Das Geschäftsmodell wurde in den letzten fünf Jahren nicht adaptiert?

**Stadium 3 — Absatzkrise:**
- [ ] Umsatzrückgang > 10 % in zwei aufeinanderfolgenden Quartalen?
- [ ] Auftragsbestand sinkt unter Normalreichweite?
- [ ] Preisreduzierungen erforderlich, um Aufträge zu gewinnen?
- [ ] Produktionsauslastung unter 70 %?

**Stadium 4 — Ertragskrise:**
- [ ] EBIT seit mehr als zwei Quartalen negativ?
- [ ] EBITDA-Marge unter Branchendurchschnitt?
- [ ] Eigenkapitalquote unter 15 %?
- [ ] Verlustvorträge übersteigen 25 % des Stammkapitals?
- [ ] Working Capital steigt trotz sinkender Umsätze?

**Stadium 5 — Liquiditätskrise:**
- [ ] Kreditlinien zu mehr als 80 % ausgelastet?
- [ ] Finanzamt oder Sozialversicherungsträger werden verzögert bezahlt?
- [ ] Lieferanten auf Vorkasse oder Avale?
- [ ] Liquiditätsreichweite unter sechs Monate?
- [ ] Covenant-Verletzung eingetreten oder droht?

### Schritt 2: Stadium einordnen und Handlungsprogramm ableiten

| Stadium | Sofortmaßnahmen | Sanierungsträger | StaRUG-Werkzeug |
|---|---|---|---|
| Stakeholderkrise | Kommunikation, Governance | Management, ggf. PE | Nicht nötig |
| Strategiekrise | Strategieüberprüfung, Restrukturierung | Management + Berater | Nicht nötig |
| Absatzkrise | Vertrieb, Pricing, Portfolio | Management + Berater | Präventiv prüfen |
| Ertragskrise | Kostenstruktur, Working Capital | GF + Restrukt.-Berater | § 1 StaRUG aktiv |
| Liquiditätskrise | Cash-Management, Notfallplan, Gläubiger | GF + RA + Insolvenzrechtler | §§ 29 ff. StaRUG oder § 15a InsO |

### Schritt 3: Diagnose dokumentieren

```
STADIUM-DIAGNOSE-PROTOKOLL
Gesellschaft: [Firma]
Datum: [TT.MM.JJJJ]
Erstellt: [GF / Berater]

Erkanntes Krisenstadium: [Stadium 1-5]
Grundlage der Einschätzung:
 [ ] Analyse BWA / Liquiditätsplan
 [ ] Kundengespräche
 [ ] Bankgespräch
 [ ] Berater-Einschätzung (IDW S 6)
 [ ] Sonstiges: [___]

Überlappende Stadien: [ja / nein] — Details: [___]

Handlungsmaßnahmen:
 1. [Maßnahme, verantwortlich, Frist]
 2. [Maßnahme, verantwortlich, Frist]

Eskalation:
 Gesellschafter informiert: [ja / nein / geplant bis]
 Berater einbezogen: [ja / nein / geplant]
 StaRUG-Prüfung initiiert: [ja / nein / geplant]

Unterschrift GF: ___________________ Datum: ___________
```

---

## Fallstricke

1. **Stadium zu spät erkannt** — die häufigste und teuerste Fehlleistung. Stakeholder- und Strategiekrise werden als "normales Marktgeschehen" abgetan, bis die Liquiditätskrise plötzlich da ist.

2. **Stadiensprünge unterschätzen** — in wirtschaftlich turbulenten Phasen kann ein Unternehmen mehrere Stadien in wenigen Monaten überspringen (z.B. externe Schocks wie Lieferkettenkrisen).

3. **Keine Aktualisierung der Diagnose** — das Stadium ist dynamisch. Was heute Ertragskrise ist, kann in drei Monaten Liquiditätskrise sein. Monatliche Re-Diagnose ist Pflicht.

4. **Beschönigung gegenüber Gesellschaftern** — wer das Stadium herunterstuft, um schlechte Nachrichten zu vermeiden, verletzt § 1 StaRUG (Unterrichtungspflicht) und riskiert die persönliche Haftung.

5. **Verwechslung mit Insolvenzeröffnungsgrund** — das Stadium der Krise ist nicht dasselbe wie ein Insolvenzeröffnungsgrund. Auch in Stadium 4 kann noch keine Insolvenzantragspflicht bestehen, wenn die Fortführungsprognose positiv ist.

---

## Querverweise

- → `paragraph-1-starug-pflichten-und-24-monats-horizont` — Früherkennungspflicht nach § 1 StaRUG
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Abgrenzung zur drohenden ZU
- → `fortbestehensprognose-zweistufig` — Fortführungsprognose in der Ertragskrise
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-basierte Stadienbestimmung
- → `restrukturierungsplan-architektur-paragraph-7ff-starug` — StaRUG-Werkzeuge ab Liquiditätskrise


## Weitere Leitentscheidungen — Krisenstadien und Stakeholder

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — Krisenstadien-Einordnung

1. **Krisenstadium?** Stakeholderkrise (Vertrauen) → Erfolgskrise (EBIT) → Liquiditaetskrise (Cashflow) → Insolvenzgefahr.
2. **Fruehzeitige Stakeholder-Einbindung?** Bank, Hauptlieferanten, FA, PSV frueizeitig kontaktieren.
3. **Vertraulichkeit?** Stakeholder-Informationen ohne NDA riskant (Weitergabe, Bonitaetsschaden).
4. **Eskalationskette?** GF → Aufsichtsrat → Anwalt → Bank → FA je nach Stadium.
