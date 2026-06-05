---
name: iv-idw-iv
description: "IV IDW IV: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV IDW IV

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV IDW IV** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-idw-s6-sanierungsfaehigkeit-gate` | Prüft aus Insolvenzverwalter-, Sachwalter- oder vorläufiger Verwalterperspektive, ob ein Sanierungskonzept auf IDW-S-6-Niveau tragfähig ist. Kernbestandteile: Unternehmenslage, Krisenstadium, Krisenursachen, Leitbild des sanierten Unternehmens, Maßnahmenpaket, integrierte GuV-/Bilanz-/Liquiditätsplanung, Fortbestehensprognose, Dokumentation und Red-Team-Gaps. Output: Sanierungsfähigkeitsvermerk, Lückenliste, Datenanforderung und Go/No-go-Ampel. |
| `iv-kommandocenter` | Einstiegspunkt für neue Insolvenzverwaltungsmandate: Verfahrensart bestimmen Prioritaeten setzen naechste Workstreams planen. §§ 56 80 InsO Verwalterbestellung § 270d Schutzschirm StaRUG. Prüfraster: Verfahrensrolle Sicherungsmassnahmen Betriebsfortführung Masseampel Fristen. Output: Verfahrenskarte Beteiligtenregister Risiko-Priorisierung To-do-Liste. Abgrenzung: Einstieg und Triage; Detailarbeit je Workstream in Spezialist-Skills. |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV IDW IV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-idw-s6-sanierungsfaehigkeit-gate`

**Fokus:** Prüft aus Insolvenzverwalter-, Sachwalter- oder vorläufiger Verwalterperspektive, ob ein Sanierungskonzept auf IDW-S-6-Niveau tragfähig ist. Kernbestandteile: Unternehmenslage, Krisenstadium, Krisenursachen, Leitbild des sanierten Unternehmens, Maßnahmenpaket, integrierte GuV-/Bilanz-/Liquiditätsplanung, Fortbestehensprognose, Dokumentation und Red-Team-Gaps. Output: Sanierungsfähigkeitsvermerk, Lückenliste, Datenanforderung und Go/No-go-Ampel.

# Sanierungsfähigkeit-Gate für Insolvenzverwaltung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsfähigkeit-Gate für Insolvenzverwaltung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill prüft, ob ein vorgelegtes oder erst aufzubauendes Sanierungskonzept für Insolvenzplan, Eigenverwaltung, Schutzschirm oder StaRUG wirklich belastbar ist. Er liefert keine Zertifizierung und ersetzt kein Gutachten, sondern macht die insolvenzverwalterliche Arbeitsfrage greifbar: Reicht das Konzept als Entscheidungs-, Berichts- und Verhandlungsgrundlage, oder ist es nur ein Zahlenpaket mit Hoffnungstext?

## Kaltstart in acht Fragen

Stelle zu Beginn nur diese Fragen, soweit die Akte sie nicht bereits beantwortet:

1. Welche Rolle liegt vor: Insolvenzverwalter, Sachwalter, vorläufige Verwaltung, Schuldnerberatung, Gläubigerprüfung?
2. Geht es um Insolvenzplan, Schutzschirm, Eigenverwaltung, StaRUG, außergerichtliche Sanierung oder nur um Plausibilisierung?
3. Gibt es bereits Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit oder rechnerische Überschuldung?
4. Welche Planungsunterlagen liegen vor: Liquiditätsplan, GuV-Plan, Bilanzplan, Maßnahmenplan, BWA, SuSa, OPOS, Bankauszüge?
5. Welche Krise dominiert: Stakeholder-, Strategie-, Produkt-/Absatz-, Erfolgs-, Liquiditäts- oder Insolvenzkrise?
6. Welche Sanierungsmaßnahmen sind rechtlich oder faktisch schon verbindlich?
7. Wer muss überzeugt werden: Gericht, Gläubigerausschuss, Bankenpool, Arbeitnehmer, Investor, Finanzamt, Sozialversicherung?
8. Welcher Output wird gebraucht: Vermerk, Datenanforderung, Red-Team-Liste, Berichtsbaustein oder Entscheidungsampel?

Wenn Eile besteht, erstelle sofort eine Minimalampel mit Stoppern und fordere danach gezielt Unterlagen nach.

## Kernlogik: zwei Ebenen sauber trennen

### Ebene 1: Fortbestehensprognose

Prüfe zunächst, ob das Unternehmen im relevanten Prognosezeitraum mit überwiegender Wahrscheinlichkeit zahlungsfähig bleibt oder durch rechtzeitig verbindliche Maßnahmen zahlungsfähig gehalten wird. Dafür reicht keine reine Managementabsicht. Es braucht eine nachvollziehbare Liquiditätsplanung, gesicherte Finanzierungsquellen, klare Fälligkeiten und eine Sensitivität gegen plausible Abweichungen.

### Ebene 2: Nachhaltige Sanierungsfähigkeit

Danach prüfen: Ist das Unternehmen nach Umsetzung der Maßnahmen wieder wettbewerbs-, rendite- und finanzierungsfähig? Eine bloße Verlängerung der Liquiditätsreichweite genügt nicht. Die wesentlichen Krisenursachen müssen beseitigt oder beherrschbar sein; das Geschäftsmodell muss nach der Sanierung ohne dauerhafte Sonderstützung tragfähig sein.

## Pflichtbausteine des Sanierungskonzepts

Arbeite jeden Baustein sichtbar ab:

| Baustein | Prüffrage | Typischer Mangel |
|---|---|---|
| Auftrag und Umfang | Was soll das Konzept leisten, für wen und mit welcher Haftungs-/Verwendungsgrenze? | Unklarer Zweck, falsche Adressatenlogik |
| Unternehmensbild | Rechtliche, wirtschaftliche, steuerliche und operative Ausgangslage vollständig? | Nur BWA und Bankliste, keine Geschäftsmodellanalyse |
| Vermögens-, Finanz- und Ertragslage | Ist die Ist-Lage stichtagsbezogen, rechnerisch geschlossen und belegbar? | SuSa passt nicht zu Bank, OPOS oder Steuerständen |
| Krisenstadium | Welche Krise liegt wirklich vor und wie weit ist sie fortgeschritten? | Liquiditätsproblem wird als reines Kostenproblem behandelt |
| Krisenursachen | Sind Ursachen von Symptomen getrennt? | Maßnahmen bekämpfen nur Zahlungsdruck |
| Leitbild | Wie sieht das sanierte Unternehmen konkret aus? | Allgemeiner Zukunftssatz ohne Markt-, Produkt- und Margenlogik |
| Maßnahmen | Welche Maßnahme wirkt wann, kostet was, braucht wen und hängt wovon ab? | Maßnahmenliste ohne Verantwortliche, Timing und Nachweis |
| Integrierte Planung | Sind GuV, Bilanz und Liquidität verzahnt? | Liquiditätsplan widerspricht Planbilanz oder Working Capital |
| Sanierungsfähigkeit | Gibt es positive Fortbestehensprognose und nachhaltige Wettbewerbsfähigkeit? | Nur kurzfristige Finanzierungslücke geschlossen |
| Dokumentation | Können Quellen, Annahmen und Rechenwege von Dritten nachvollzogen werden? | Keine Versionierung, keine Annahmenliste, keine Belegspur |

## Leitbild des sanierten Unternehmens

Formuliere das Leitbild nicht als Marketingtext, sondern als prüfbare Zielarchitektur:

- **Markt:** Zielkunden, Nachfrage, Wettbewerb, Preisfähigkeit, Marktrisiken.
- **Leistung:** Produkte, Dienstleistungen, Qualität, Lieferfähigkeit, Kernkompetenzen.
- **Organisation:** Geschäftsleitung, Schlüsselpersonen, Prozesse, IT, Controlling, Governance.
- **Ertrag:** Zielmargen, Fixkostenbasis, Break-even, Kostentreiber, Preis- und Mengenlogik.
- **Finanzierung:** Kapitalstruktur, Working Capital, Linien, Covenants, Sicherheiten, Eigenbeiträge.
- **Resilienz:** Abhängigkeiten von Kunden, Lieferanten, Energie, Cyber, ESG-/Nachhaltigkeitsrisiken, Regulatorik.

Jede Maßnahme muss zu diesem Leitbild passen. Maßnahmen ohne Bezug zum Leitbild sind zu streichen oder als Sonderfall zu begründen.

## Integrierte Planung

Verlange eine Planung, die mindestens GuV, Bilanz und Liquidität verknüpft. Für die ersten Monate muss die Liquidität engmaschig nachvollziehbar sein; für das laufende und folgende Planjahr ist regelmäßig eine monatliche Darstellung zweckmäßig. Spätere Jahre können gröber verdichtet werden, sofern die Übergänge rechnerisch geschlossen bleiben.

Prüfe insbesondere:

- Ertragswirkung jeder Maßnahme: Umsatz, Rohertrag, Personal, sonstige Kosten, Zinsen, Steuern.
- Liquiditätswirkung jeder Maßnahme: Einmalzahlung, laufender Effekt, Vorfinanzierungsbedarf, Fälligkeit.
- Bilanzwirkung jeder Maßnahme: Forderungen, Vorräte, Verbindlichkeiten, Eigenkapital, Rückstellungen.
- Working-Capital-Logik: Zahlungsziele, Vorratsreichweite, Debitorenrisiko, Lieferantenkredite.
- Finanzierungslogik: Linien, Covenants, Tilgungen, Sicherheiten, Rangrücktritte, Patronate, Kapitalzufuhr.
- Sensitivitäten: Umsatzverzug, Margendruck, Forderungsausfall, Kostenanstieg, Maßnahmenverzug.
- Steuer- und Sozialversicherungseffekte, wenn sie für Liquidität oder Planergebnis wesentlich sind.

## Proportionalität bei kleineren Unternehmen

Bei kleinen oder weniger komplexen Unternehmen darf der Umfang schlanker sein. Der Prüfmaßstab wird aber nicht leer: Auch dort braucht es klare Ausgangslage, Krisenursachen, Leitbild, Maßnahmen, integrierte Planung und Ergebnis. Geringere Komplexität erlaubt weniger Berichtsumfang, nicht weniger Wahrheit.

Praktische Vereinfachungen:

- Management- und Organisationsanalyse knapper, wenn wenige Schlüsselpersonen den Betrieb tragen.
- Marktanalyse fokussiert auf Hauptkunden, Auftragsbestand und lokale Wettbewerber.
- Planung mit weniger Kontenzeilen, aber vollständiger Verknüpfung von Ergebnis, Bilanz und Liquidität.
- Dokumentation mit sauberer Belegliste statt großem Gutachtenband.

## Dokumentationsregister

Erstelle ein Register mit:

- Quellenliste: Jahresabschlüsse, BWA, SuSa, OPOS, Bank, Verträge, Steuerstände, Lohn/SV, Aufträge, Gesellschafterbeschlüsse.
- Annahmenlog: jede wesentliche Annahme mit Quelle, Verantwortlichem, Plausibilisierung und Sensitivität.
- Maßnahmenlog: Maßnahme, Eigentümer, Voraussetzung, Kosten, Wirkung, Frist, Status, Nachweis.
- Planversionen: Dateiname, Stand, Ersteller, Änderung gegenüber Vorversion.
- Offene Punkte: fehlender Beleg, Auswirkung, Verantwortlicher, Frist.
- Entscheidungsvermerk: warum trotz Unsicherheiten ein Go, Conditional Go oder No-go vertretbar ist.

## Ausgabeformat

Liefer standardmäßig:

1. **Sanierungsfähigkeitsvermerk** mit Kurzfazit, Stichtag, Rolle und Verwendungszweck.
2. **Ampel:** Grün, Gelb, Rot mit Begründung und Stoppern.
3. **Lückenliste:** fehlende Daten, Widersprüche, nicht belegte Annahmen, nicht gesicherte Maßnahmen.
4. **Datenanforderung:** priorisiert nach "entscheidend", "wichtig", "nice to have".
5. **Red-Team-Fragen:** die zehn stärksten Angriffspunkte aus Sicht von Gericht, Gläubigerausschuss, Bank und opponierendem Gläubiger.

## Red Flags

- Plan zeigt Liquidität, aber keine Planbilanz.
- GuV verbessert sich, obwohl keine Maßnahme mit Timing und Eigentümer hinterlegt ist.
- Gesellschafterbeitrag ist als sicher geplant, aber nicht beschlossen oder finanziert.
- Lieferantenstundung wird unterstellt, obwohl keine Vereinbarungen vorliegen.
- Einmalige Liquiditätshilfe wird als dauerhafte Sanierung verkauft.
- Krisenursache bleibt bestehen, wird aber im Leitbild nicht adressiert.
- Steuer-, Sozialversicherungs- oder Zinslasten fehlen.
- Sensitivität kippt sofort in Zahlungsunfähigkeit.
- Datenstand ist unklar oder Planungsversionen widersprechen sich.

## Anschluss-Skills

- `iv-plan-sanierungskonzept` für Aufbau und Text des Sanierungskonzepts.
- `iv-plan-integrierte-planung` für GuV-/Bilanz-/Liquiditätsmodell.
- `iv-plan-vergleichsrechnung` für Planfall gegen Liquidation.
- `iv-plan-redteam-qualitygate` für die harte Endprüfung.
- `iv-schutzschirm-270d` bei Schutzschirm- oder Eigenverwaltungsroute.

## Quellenregel

Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben. Berufsständische Standards nur als methodischen Arbeitsmaßstab verwenden, nicht als Ersatz für die rechtliche Subsumtion.

## 2. `iv-kommandocenter`

**Fokus:** Einstiegspunkt für neue Insolvenzverwaltungsmandate: Verfahrensart bestimmen Prioritaeten setzen naechste Workstreams planen. §§ 56 80 InsO Verwalterbestellung § 270d Schutzschirm StaRUG. Prüfraster: Verfahrensrolle Sicherungsmassnahmen Betriebsfortführung Masseampel Fristen. Output: Verfahrenskarte Beteiligtenregister Risiko-Priorisierung To-do-Liste. Abgrenzung: Einstieg und Triage; Detailarbeit je Workstream in Spezialist-Skills.

# Insolvenzverwaltungs-Kommandocenter

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzverwaltungs-Kommandocenter` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Führt als erste Schaltstelle durch ein Insolvenzverwaltungsmandat aus Sicht des Insolvenzverwalters, vorläufigen Insolvenzverwalters oder Sachwalters.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- neue Bestellung, Gutachtenauftrag oder laufende Verfahrensakte eingeht
- unklar ist, ob Regelverfahren, Eigenverwaltung oder Schutzschirm betroffen ist
- eine schnelle Tagespriorisierung gebraucht wird

## Eingaben

- Beschluss oder Gutachtenauftrag
- Schuldnerdaten, Gericht, Aktenzeichen, Stichtage
- erste OPOS-, Bank-, Lohn- und Vermögenslisten

## Workflow

1. **Einordnen** - Verfahrensart, Rolle, Sicherungsmaßnahmen und rote Fristen erfassen.
2. **Akte bauen** - Verfahrenskarte, Beteiligtenregister, Masseampel und nächste Workstreams anlegen.
3. **Risiko priorisieren** - Betriebsfortführung, Massearmut, Lohn, Steuern, Anfechtung, § 15b InsO und Berichtspflichten gewichten.
4. **Arbeitsauftrag ausgeben** - Nächste drei Aktionen mit Beleganforderungen und Rückfragen formulieren.

## Ausgabe

- Verfahrenskarte mit Ampel
- Priorisierte To-do-Liste
- Rückfragen an Schuldner, Gericht, Banken und Dritte

## Qualitätsgates

- Aktenzeichen und Bestellungsumfang sind geprüft
- Rolle und Befugnisse sind nicht vermischt
- jede Empfehlung nennt Beleg oder fehlenden Beleg

## Rote Schwellen

- unklare Kassenlage
- drohende Masseunzulänglichkeit
- fortlaufende Zahlungen ohne Zustimmung oder Prüfung

## Interne Vorlagen

- assets/templates/iv-mandatskarte.md
- assets/templates/quality-gate.md

## Amtliche Erstquellen

- InsO §§ 21 ff., 56, 80 ff., 270 ff.
- § 208 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
