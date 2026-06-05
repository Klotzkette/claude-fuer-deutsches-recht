---
name: insol-sanierungsgewinn-insolvenzreife
description: "Insol Sanierungsgewinn Insolvenzreife: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Insol Sanierungsgewinn Insolvenzreife

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Insol Sanierungsgewinn Insolvenzreife** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `insol-sanierungsgewinn-massehaftungsbefreiung-und-bilanz` | Massehaftungsbefreiung und bilanzielle Verbuchung des Sanierungsertrags. Buchungstechnik bei Verzicht: Verbindlichkeit weg, ausserordentlicher Ertrag. Auswirkung auf Eigenkapital. Schnittstelle Masse versus Insolvenzforderungen. Massehaftungsbefreiung Paragraph 60 InsO bei korrekter Buchung. Stille Reserven, latente Steuern, ggf. Paragraph 5 Absatz 2a EStG-Wirkung. Mustertexte Buchungsbeleg und Pruefvermerk fuer die Bilanz. |
| `spezial-insolvenzreife-antragspflicht-und-haftung` | Insolvenzreife, Antragspflicht und Haftung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` | Paragraph 3a EStG im Insolvenzplan-Kontext (Paragraphen 217 ff. InsO). Vier Voraussetzungen pruefen: Sanierungsbeduerftigkeit, Sanierungsfaehigkeit, Sanierungseignung, Sanierungsabsicht der Glaeubiger. Antragsmechanik mit der Steuererklaerung des Sanierungsjahres. Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG. Mustertext fuer darstellenden Teil des Plans und fuer den Erlassantrag. |
| `insol-sanierungsgewinn-3a-estg-im-starug-plan` | Paragraph 3a EStG bei StaRUG-Restrukturierungsplan (Paragraphen 4 ff. StaRUG). Unterschiede zum Insolvenzplan: kein Insolvenzverfahren, keine Massehaftung, Sanierungsabsicht der Glaeubiger im StaRUG-Kontext belegen. Antragsmechanik fuer den Sanierungsertrag bei vorinsolvenzlicher Restrukturierung. Mustertexte fuer Restrukturierungsplan und Steuererklaerung. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Insol Sanierungsgewinn Insolvenzreife**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `insol-sanierungsgewinn-massehaftungsbefreiung-und-bilanz`

**Fokus:** Massehaftungsbefreiung und bilanzielle Verbuchung des Sanierungsertrags. Buchungstechnik bei Verzicht: Verbindlichkeit weg, ausserordentlicher Ertrag. Auswirkung auf Eigenkapital. Schnittstelle Masse versus Insolvenzforderungen. Massehaftungsbefreiung Paragraph 60 InsO bei korrekter Buchung. Stille Reserven, latente Steuern, ggf. Paragraph 5 Absatz 2a EStG-Wirkung. Mustertexte Buchungsbeleg und Pruefvermerk fuer die Bilanz.

# Sanierungsgewinn — Massehaftungsbefreiung und Bilanzbuchung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Massehaftungsbefreiung und Bilanzbuchung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Wenn der Insolvenzplan Forderungsverzichte vorsieht und der bestaetigte Plan rechtskraeftig wird, ist die Bilanz des Schuldners (Steuerbilanz, Handelsbilanz, ggf. IFRS) entsprechend anzupassen. Der bilanzielle Vorgang entscheidet ueber:

- die Hoehe des Sanierungsertrags,
- die latenten Steuern,
- die Behandlung stiller Reserven,
- die Haftung des Verwalters fuer die korrekte Buchung (Paragraph 60 InsO).

Dieser Skill arbeitet die Buchung Schritt fuer Schritt und liefert Pruefvermerke. Adressat: StB des Schuldners, IV/Sachwalter und ggf. Wirtschaftspruefer.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Plan ist bestaetigt; Bilanz fuer das Sanierungsjahr aufzustellen.
- Wirtschaftspruefer fragt im Vorfeld der Pruefung an, welche Buchungen anstehen.
- IV will sich gegen den Vorwurf einer Massehaftungsverletzung absichern.

Kaltstart-Fragen:

1. Welche Forderungen wurden im Plan verzichtet (Liste, Hoehe, Glaeubiger)?
2. Welche werthaltigen Forderungen wurden umgewandelt (DES)?
3. Wie hoch sind die stillen Reserven der Schuldnerin?
4. Wurde Buchwertfortfuehrung oder Bewertungsanpassung beschlossen?
5. Welcher Rechnungslegungsstandard greift (HGB, IFRS)?

## Rechtlicher Rahmen

- Paragraphen 246, 252, 266, 272 HGB.
- Paragraph 5 EStG, insbesondere Massgeblichkeit Paragraph 5 Absatz 1 EStG.
- Paragraph 5 Absatz 2a EStG — Passivierungsverbot bei qualifiziertem Rangruecktritt.
- Paragraph 3a EStG — Sanierungsertrag steuerlich.
- Paragraph 60 InsO — Haftung IV.
- Paragraph 55 InsO — Masseverbindlichkeiten.

## / Schritt fuer Schritt

1. **Bestandsaufnahme** aller im Plan adressierten Verbindlichkeiten.
2. **Buchungssystematik festlegen** je Verzichtsart (siehe `insol-sanierungsgewinn-verzicht-bilanz-im-plan`).
3. **Stille Reserven**: separat dokumentieren; keine Vermengung mit Sanierungsertrag.
4. **Latente Steuern**: pruefen, ob durch den Verzicht und die Nutzung der Verlustvortraege ein latenter Steuereffekt entsteht.
5. **Belege fuer Massehaftungsbefreiung sammeln.** Plan, Bestaetigungsbeschluss, Werthaltigkeitsgutachten, StB-Schreiben, Glaeubigerausschuss-Beschluss.
6. **Bilanz-Pruefvermerk** mit ausweisbarem Sanierungsertrag.
7. **Steuererklaerung** mit Paragraph 3a EStG-Antrag und Paragraph 7b GewStG-Antrag.

## Trade-off-Matrix Bilanz-Optionen

| Bilanz-Option | Wirkung | Risiko |
|---|---|---|
| Buchwertfortfuehrung Aktiva | stille Reserven verbleiben | spaetere Veraeusserungs-/Auflassungsgewinne hoeher |
| Bewertungsanpassung (Stand Sanierung) | stille Reserven werden aufgedeckt | sofortige Gewinnrealisierung; kein Sanierungsertrag |
| Erfolgswirksamer Sanierungsertrag (Verzicht) | Eigenkapital steigt; Sanierungsertrag entsteht | Paragraph 3a EStG-Pruefung; Restbetrag ggf. steuerbar |
| Kapitalruecklage (Gesellschafter-Verzicht werthaltig) | kein Sanierungsertrag | Werthaltigkeitspruefung pflichtig |
| Auflosung Verbindlichkeit nach Rangruecktritt Paragraph 5 Absatz 2a EStG | spaetere Auflosung kann Ertrag erzeugen | Klausel-Gestaltung kritisch |
| IFRS-Sicht (IFRS 9, IAS 32) | abweichend von HGB moeglich | Konzern-Bilanzierung zu pruefen |

## Praxistipps der alten Hasen

1. **Buchwertfortfuehrung ist Regel im Plan.** Wer aufdeckt, riskiert zusaetzliche Steuern, die nicht von Paragraph 3a EStG getragen werden.
2. **Latente Steuern bei Verlustvortrag-Verbrauch.** Werden Verlustvortraege durch Sanierungsertrag aufgezehrt (Paragraph 3a Absatz 3 EStG), entfallen aktive latente Steuern, die ggf. zuvor bilanziert waren — als Aufwand zu erfassen.
3. **Werthaltigkeitsgutachten pro Gesellschafterforderung** dokumentieren. Pauschale Annahmen halten der FA-Pruefung nicht stand.
4. **Stille Reserven listen.** Eine Tabelle stille Reserven (Aktiva-Position, Buchwert, gemeiner Wert, Differenz) gehoert in jede Sanierungsakte.
5. **Wirtschaftspruefer fruehzeitig einbinden.** Bei pruefungspflichtigen Unternehmen ist eine "Aha"-Reaktion des WP im Pruefungstermin der falsche Zeitpunkt.
6. **HGB versus Steuerbilanz dokumentieren.** Ueberleitungsrechnung Paragraph 5b EStG sauber halten.

## Mustertexte / Berechnungsbeispiele

**Buchungsbeleg (verkuerzt):**

```
BUCHUNGSBELEG SANIERUNGSERTRAG
Datum: [Tag der Rechtskraft Bestaetigungsbeschluss]
Mandant: [Schuldnerin]
Buchungstext: Sanierungsertrag aus Forderungsverzicht laut bestaetigtem
Plan Aktenzeichen [...]

Soll: Verbindlichkeiten 1700 ff. (Aufstellung Anlage 1) EUR x
Haben: Ausserordentlicher Ertrag 5750 (Sanierungsertrag) EUR x

Davon Gesellschafter-Verzicht werthaltig (Einlage):
Soll: Verbindlichkeiten Gesellschafter EUR y
Haben: Kapitalruecklage 2110 EUR y

Beleg Anlagen: Bestaetigungsbeschluss, Plan, Werthaltigkeits-
gutachten WP [Name].
```

**Pruefvermerk Bilanz (Geruest):**

```
PRUEFVERMERK BILANZ ZUM [Stichtag]
Mandant: [Schuldnerin]
StB: [Name]

1. Sachverhalt
Mit Bestaetigungsbeschluss vom [Datum] wurde der Insolvenzplan
rechtskraeftig. Das Plan-Volumen Forderungsverzicht: EUR [Betrag].

2. Bilanz-Erfassung
2.1 Drittglaeubiger-Verzicht endgueltig:
 EUR x als ausserordentlicher Ertrag (Sanierungsertrag).
2.2 Gesellschafter-Verzicht werthaltig:
 EUR y als Kapitalruecklage.
2.3 Gesellschafter-Verzicht nicht werthaltig:
 EUR z als ausserordentlicher Ertrag (Sanierungsertrag).
2.4 Stille Reserven Aktiva:
 Tabelle in Anlage S1; keine Aufdeckung (Buchwertfortfuehrung).

3. Steuerliche Behandlung
3.1 Paragraph 3a EStG-Antrag laeuft, Restsanierungsertrag EUR [...].
3.2 Paragraph 7b GewStG-Antrag laeuft, Restbetrag EUR [...].
3.3 Latente Steuern: Aufloesung aktiver latenter Steuern EUR [...] als
 Steueraufwand.

4. Massehaftungsbefreiung
Buchung erfolgt auf Basis Plan, WP-Gutachten und StB-Pruefung. Aktenstand:
- Plan, Bestaetigungsbeschluss
- Werthaltigkeitsgutachten WP [Name] vom [Datum]
- Glaeubigerausschuss-Beschluss vom [Datum]
- Aktennotiz Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG.
```

## Typische Fehler

1. Buchung als "ausserordentlicher Ertrag" pauschal, ohne Werthaltigkeitspruefung beim Gesellschafterverzicht.
2. Stille Reserven mit Sanierungsertrag vermengt.
3. Latente Steuern aus Verlustvortrag nicht aufgeloest.
4. HGB- und Steuerbilanz nicht abgestimmt — Ueberleitung Paragraph 5b EStG fehlt.
5. IFRS-Bilanz parallel uebersehen.
6. Bei Plan-Cramdown auf Anteilseigner (Paragraph 225a Absatz 3 InsO): Kapitalherabsetzung/-erhoehung bilanziell nicht abgebildet.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-verzicht-bilanz-im-plan` — Verzichtsmechanik.
- `insol-sanierungsgewinn-debt-equity-swap-im-plan` — DES.
- `insol-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg-im-plan` — Rangruecktritt.
- `insol-sanierungsgewinn-iv-haftung-fuer-versaumte-3a-iv-antraege` — Haftung.

In anderen Plugins:

- `steuerrecht-anwalt-und-berater` — Bilanzsteuerrecht.
- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.

## Quellen Stand 06/2026

- Paragraphen 246, 252, 266, 272 HGB.
- Paragraph 5 EStG, Paragraph 5b EStG.
- Paragraph 3a EStG.
- Paragraph 7b GewStG.
- Paragraphen 55, 60, 225a InsO.
- Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 2. `spezial-insolvenzreife-antragspflicht-und-haftung`

**Fokus:** Insolvenzreife, Antragspflicht und Haftung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Insolvenzreife, Antragspflicht und Haftung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzreife, Antragspflicht und Haftung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `insolvenzrecht`. Kontext des Plugins: Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Insolvenzreife, Antragspflicht und Haftung** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `insol-sanierungsgewinn-3a-estg-im-insolvenzplan`

**Fokus:** Paragraph 3a EStG im Insolvenzplan-Kontext (Paragraphen 217 ff. InsO). Vier Voraussetzungen pruefen: Sanierungsbeduerftigkeit, Sanierungsfaehigkeit, Sanierungseignung, Sanierungsabsicht der Glaeubiger. Antragsmechanik mit der Steuererklaerung des Sanierungsjahres. Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG. Mustertext fuer darstellenden Teil des Plans und fuer den Erlassantrag.

# Sanierungsgewinn — Paragraph 3a EStG im Insolvenzplan

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Paragraph 3a EStG im Insolvenzplan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der Insolvenzplan (Paragraphen 217 ff. InsO) ist das in der Praxis wichtigste Instrument fuer Forderungsverzichte und damit zugleich der typische Ausloeser eines Sanierungsertrags. Mit der Wiederaufnahme von Paragraph 3a EStG ist die fruehere Streitfrage, ob der Sanierungserlass per Verwaltungsanweisung oder per Gesetz gelte, erledigt: die Steuerbefreiung steht im Gesetz.

Dieser Skill arbeitet die Pruefung des Sanierungsertrags im Plan-Kontext durch: vier materielle Voraussetzungen, Verrechnungsreihenfolge, Antrag, Plan-Texte. Adressat ist der Plan-Anwalt, der Insolvenzverwalter und der StB.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Insolvenzplan wird ausgearbeitet, Forderungsverzicht der Glaeubiger ist Kerngegenstand.
- Plan ist eingereicht oder steht vor Einreichung — Steuerteil muss geschrieben werden.
- StB soll den Erlassantrag oder die Steuererklaerung des Sanierungsjahres vorbereiten.

Kaltstart-Fragen:

1. Schuldner: GmbH, AG, GmbH und Co. KG, Einzelunternehmer, eingetragener Kaufmann?
2. Hoehe des Forderungsverzichts im Plan?
3. Plan-Quote (was bleibt den Glaeubigern)?
4. Verlustvortraege bekannt (KSt, GewSt, ESt)?
5. Liegt ein Sanierungskonzept nach IDW S 6 oder vergleichbarer Standard vor?

## Rechtlicher Rahmen

- Paragraphen 217 ff. InsO — Insolvenzplan.
- Paragraph 3a EStG — Steuerbefreiung Sanierungsertrag.
- Paragraph 3a Absatz 2 EStG — vier Voraussetzungen.
- Paragraph 3a Absatz 3 EStG — Verrechnungsreihenfolge; verdraengt Mindestbesteuerung.
- Paragraph 7b GewStG — Gewerbesteuer-Parallel.
- Paragraph 251 AO — Steuern im Insolvenzverfahren.
- BFH, Urteil vom 26.02.2003 — II R 19/01: Verbindlichkeiten bleiben zivilrechtlich ueber die Liquidation hinaus bestehen; blosse Vermoegenslosigkeit begruendet keine Ausbuchung — zur Abgrenzung Sanierungsertrag vs. Ausbuchung mangels Schuldner.

## / Schritt fuer Schritt

1. **Forderungsverzicht erfassen.** Welche Forderungen entfallen im Plan in welcher Hoehe? Trennung Drittglaeubiger vs. Gesellschafter (Gesellschafter-Verzicht kann verdeckte Einlage sein).
2. **Werthaltigkeit der Forderungen pruefen.** Nur werthaltige Forderungen erzeugen einen vollwertigen Sanierungsertrag; nicht werthaltige Forderungen erhoehen den Sanierungsertrag rechnerisch, fuehren aber zugleich zu einer abweichenden bilanziellen Behandlung.
3. **Vier Voraussetzungen Paragraph 3a Absatz 2 EStG abarbeiten** (Sanierungsbeduerftigkeit, Sanierungsfaehigkeit, Sanierungseignung, Sanierungsabsicht der Glaeubiger).
4. **Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG aufstellen.**
5. **Restsanierungsertrag berechnen.**
6. **Antrag stellen.** Mit der Steuererklaerung des Sanierungsjahres; ggf. zusaetzlich Vorabauskunft Paragraph 89 AO.
7. **Plan-Texte schreiben** (darstellender Teil mit Voraussetzungs-Belegen; gestaltender Teil mit Verzichtsklauseln).

## Vier Voraussetzungen Paragraph 3a Absatz 2 EStG

| Voraussetzung | Pruefkriterium | Beleg |
|---|---|---|
| Sanierungsbeduerftigkeit | Unternehmen ohne Verzicht nicht ueberlebensfaehig | Liquiditaetsplan, Fortbestehensprognose, Eroeffnungsantrag |
| Sanierungsfaehigkeit | Unternehmen ist nach Sanierung lebensfaehig | IDW S 6-Gutachten oder gleichwertig |
| Sanierungseignung | Forderungsverzicht ist geeignet, die Sanierung zu erreichen | Plan-Quote + Liquiditaets-Auswirkung |
| Sanierungsabsicht der Glaeubiger | Glaeubiger verzichten, gerade weil die Sanierung sonst nicht funktioniert | Glaeubigerausschuss-Protokoll, Glaeubigerbriefe, Plan-Annahme-Beschluss |

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Unternehmensbezogene Sanierung (Paragraph 3a Absatz 2 EStG) | Steuerbefreiung greift | Vier Voraussetzungen muessen wasserdicht belegt sein |
| Unternehmerbezogene Sanierung | nicht von Paragraph 3a Absatz 1 EStG erfasst | Steuerpflichtig — Erlass nur ueber Paragraph 227 AO |
| Gesellschafter-Verzicht (gesellschaftsrechtlich veranlasst) | keine Steuer (Einlage) | Werthaltigkeitspruefung; ggf. verdeckte Einlage |
| Drittglaeubiger-Verzicht | klar Sanierungsertrag | bei Werthaltigkeit gewinnerhoehend |
| Verzicht mit Besserungsschein | nur teilweise endgueltig | Sanierungsertrag entsteht ggf. nachgelagert; Buchungstechnik beachten |

## Praxistipps der alten Hasen

1. **Vier Voraussetzungen in den darstellenden Teil ausdruecklich aufnehmen.** Wer das im Plan dokumentiert, hat dem Finanzamt eine vorgefertigte Begruendung serviert.
2. **Sanierungsabsicht ist plural.** Wenn nur ein Hauptglaeubiger verzichtet, hilft das nicht — der Verzicht muss von einem ausreichenden Glaeubigerkreis getragen sein, weil die Sanierung sonst nicht plausibel ist.
3. **Besserungsschein steuerlich pruefen.** Forderungsverzicht mit Besserungsabrede entstehen den Sanierungsertrag erst, wenn der Besserungsfall **nicht** eintritt — bis dahin ist der Verzicht aufschiebend.
4. **Stille Reserven nicht durch Buchungstechnik in den Sanierungsertrag mischen.** Aufdeckungen sind regulaer steuerpflichtige Gewinne.
5. **Vorabauskunft Paragraph 89 AO** ist gebuehrenpflichtig, aber bei Volumen ab ca. 1 Mio EUR Sanierungsertrag in der Regel sinnvoll.
6. **Doppelt parallel laufen** — KSt-Antrag und GewSt-Antrag (Paragraph 7b GewStG) gleichzeitig vorbereiten.

## Mustertexte / Berechnungsbeispiele

**Plan-Text fuer den darstellenden Teil (Auszug):**

```
III. Steuerliche Folgen des Forderungsverzichts

Der gestaltende Teil dieses Plans sieht einen Forderungsverzicht der
Insolvenzglaeubiger in Hoehe von EUR [Betrag] vor. Dieser Verzicht loest
nach den Grundsaetzen der Bilanzierung einen Sanierungsertrag aus.

Die Voraussetzungen der Steuerbefreiung nach Paragraph 3a Absatz 2 EStG
liegen vor:

1. Sanierungsbeduerftigkeit
Die Schuldnerin ist ohne den Verzicht nicht ueberlebensfaehig. Dies ist
durch den Eroeffnungsantrag, den vorlaeufigen Bericht des Verwalters vom
[Datum] und die diesem Plan als Anlage beigefuegte Liquiditaetsplanung
belegt.

2. Sanierungsfaehigkeit
Das diesem Plan als Anlage beigefuegte Sanierungsgutachten nach IDW S 6
[oder vergleichbar] belegt die Sanierungsfaehigkeit der Schuldnerin nach
Vollzug des Plans.

3. Sanierungseignung
Die im Plan vorgesehenen Massnahmen — insbesondere der Forderungsverzicht
in Verbindung mit [weiteren Massnahmen] — fuehren rechnerisch zur
Wiederherstellung positiver Eigenkapitalquote ab [Stichtag] gemaess
Anlage [...].

4. Sanierungsabsicht der Glaeubiger
Die Insolvenzglaeubiger verzichten in dem im gestaltenden Teil
vorgesehenen Umfang, weil eine Sanierung der Schuldnerin ohne den Verzicht
nicht moeglich waere. Dies ist im Glaeubigerausschuss-Beschluss vom
[Datum] und im Schreiben des Hauptglaeubigers vom [Datum] dokumentiert.

5. Verrechnungsreihenfolge nach Paragraph 3a Absatz 3 EStG
[Tabelle siehe Anlage S-3]
```

**Erlassantrag-Geruest:**

```
An das Finanzamt [Ort]
Steuernummer [...]

Antrag auf Behandlung des Sanierungsertrags nach Paragraph 3a EStG fuer
das Sanierungsjahr [Jahr]

1. Sachverhalt
[Kurze Darstellung mit Verweis auf bestaetigten Insolvenzplan]

2. Sanierungsertrag
[Betrag, Berechnung mit Verweis auf Plan-Anlage]

3. Vier Voraussetzungen Paragraph 3a Absatz 2 EStG
[Verweis auf darstellenden Teil des Plans Abschnitt III]

4. Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG
[Tabelle mit Restsanierungsertrag]

5. Antrag
Wir beantragen die Anwendung der Steuerbefreiung nach Paragraph 3a Absatz
1 EStG auf den ermittelten Restsanierungsertrag in Hoehe von EUR [Betrag].
Hilfsweise: Erlass nach Paragraph 227 AO. Hilfsweise: Stundung nach
Paragraph 222 AO.

6. Anlagen
[1. Bestaetigter Insolvenzplan, 2. IDW S 6, 3. Fortbestehensprognose,
4. Glaeubigerausschuss-Beschluss, 5. Verrechnungsreihenfolge-Tabelle]
```

## Typische Fehler

1. Vier Voraussetzungen nicht ausdruecklich im darstellenden Teil belegt.
2. Werthaltigkeitspruefung beim Gesellschafterverzicht vergessen.
3. Besserungsschein als unmittelbarer Sanierungsertrag verbucht.
4. GewSt-Parallel-Antrag (Paragraph 7b GewStG) nicht gestellt.
5. Stille Reserven mit Sanierungsertrag vermengt.
6. Annahme, die Plan-Bestaetigung loese die Steuerfreiheit automatisch aus — sie ist Voraussetzung, aber der Antrag ist gesondert zu stellen.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-fruehe-vorbereitung-vor-plan` — Zeitachse.
- `insol-sanierungsgewinn-verlustvortrag-und-3a-iii-vorab` — Verrechnungs-Modell.
- `insol-sanierungsgewinn-verzicht-bilanz-im-plan` — Bilanzteil.
- `insol-sanierungsgewinn-7b-gewstg-im-insolvenzplan-paralleltrack` — GewSt-Spiegel.
- `insol-sanierungsgewinn-debt-equity-swap-im-plan` — DES-Variante.
- `inso-eroeffnungsantrag-checkliste` — Verfahrenseroeffnung.

In anderen Plugins:

- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt insgesamt.
- `steuerrecht-anwalt-und-berater` — generelle Steuer-Skills.
- `grosskanzlei-corporate-ma` — Investor-Sicht.

## Quellen Stand 06/2026

### Normen

- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraph 5 Absatz 2a EStG.
- Paragraph 7b GewStG, `gesetze-im-internet.de/gewstg/__7b.html`.
- Paragraphen 217 ff. InsO, `gesetze-im-internet.de/inso/`.
- Paragraph 251 AO, `gesetze-im-internet.de/ao_1977/__251.html`.
- Paragraph 11 KStG (Liquidationsbesteuerung — fuer Plan-B-Pfade).

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 26.02.2003 — II R 19/01** — Verbindlichkeiten bleiben zivilrechtlich auch in Liquidation bestehen.
- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Passivierung nur bei wirtschaftlicher Belastung.
- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — Paragraph 5 Absatz 2a EStG bei Rangruecktritt.
- **FG Koeln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** — Os. 7: Bei Liquidation rangruecktrittsbehaftete Verbindlichkeit passiviert bis Loeschung; rechtstheoretisch entstehender Gewinn mangels Steuersubjekt nicht steuerpflichtig (vorgehend zu BFH I R 34/12).
- **BFH, Beschl. v. 05.02.2014 — I R 34/12, BFH/NV 2014, 1014** — bestaetigt FG-Koeln-Linie als „nicht evident rechtsfehlerhaft".
- **FG Koeln, Urt. v. 04.11.2025 — 12 K 1413/25** — Antragsfristen Paragraph 3a Abs. 4 EStG.

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfuegung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782**.
- **OFD Frankfurt a. M., Rundverfuegung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560**.
- **OFD Nordrhein-Westfalen, Kurzinformation ESt Nr. 46/2014, akt. 22.09.2017, DB 2017, 2580**.

### Mindestbesteuerung / Definitiveffekt

- **FG Duesseldorf, Urt. v. 18.09.2018 — 6 K 454/15 K, DStRE 2019** — Definitiveffekt der Mindestbesteuerung in Liquidation. Revision anhaengig BFH I R 36/18 (ausgesetzt wegen BVerfG 2 BvL 19/14, Vorlage BFH I R 59/12).
- **OFD Frankfurt v. 27.12.2018, BeckVerw 447487** — Einsprueche zur Mindestbesteuerung ruhend zu stellen.

### Plan-B-Pfad Liquidation

- Siehe Fachmodul `stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` (Drei-Phasen-Analyse) im Plugin `steuerrecht-anwalt-und-berater`.

Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.

## 4. `insol-sanierungsgewinn-3a-estg-im-starug-plan`

**Fokus:** Paragraph 3a EStG bei StaRUG-Restrukturierungsplan (Paragraphen 4 ff. StaRUG). Unterschiede zum Insolvenzplan: kein Insolvenzverfahren, keine Massehaftung, Sanierungsabsicht der Glaeubiger im StaRUG-Kontext belegen. Antragsmechanik fuer den Sanierungsertrag bei vorinsolvenzlicher Restrukturierung. Mustertexte fuer Restrukturierungsplan und Steuererklaerung.

# Sanierungsgewinn — Paragraph 3a EStG bei StaRUG-Restrukturierungsplan

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Paragraph 3a EStG bei StaRUG-Restrukturierungsplan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Das Unternehmensstabilisierungs- und -restrukturierungsgesetz (StaRUG) ermoeglicht seit 2021 die vorinsolvenzliche Restrukturierung mit Mehrheitszwang. Auch im StaRUG-Plan kommt es regelmaessig zu Forderungsverzichten — und damit zu Sanierungsertraegen. Paragraph 3a EStG ist hier ebenso anwendbar wie im Insolvenzplan, weil das Gesetz nicht von einem Insolvenzverfahren abhaengt, sondern von der **unternehmensbezogenen Sanierung**.

Dieser Skill arbeitet die Besonderheiten der StaRUG-Variante heraus: keine Masseverwaltung, kein gerichtlich bestellter Verwalter, statt dessen Restrukturierungsbeauftragter und ggf. Sanierungsmoderator; engere zeitliche Fenster; schwierigere Dokumentation der Sanierungsabsicht der Glaeubiger.

## Wann dieses Modul hilft / Kaltstart-Fragen

- StaRUG-Verfahren ist angezeigt oder Restrukturierungsplan ist in Vorbereitung.
- Sie sind Restrukturierungsbeauftragter, Sanierungsmoderator, Plan-Anwalt oder StB des Schuldners.
- Plan sieht Forderungsverzichte gegenueber bestimmten Planbetroffenen vor.

Kaltstart-Fragen:

1. StaRUG-Variante (mit gerichtlicher Bestaetigung, mit Stabilisierungsanordnung, ohne)?
2. Hoehe des Forderungsverzichts?
3. Planbetroffene Glaeubiger — wer wird wie verzichten?
4. Welcher Insolvenzgrund liegt zugrunde (drohende Zahlungsunfaehigkeit als Voraussetzung Paragraph 29 StaRUG)?
5. Verlustvortraege bekannt?

## Rechtlicher Rahmen

- Paragraphen 4 ff. StaRUG — Restrukturierungsverfahren.
- Paragraph 29 StaRUG — drohende Zahlungsunfaehigkeit als Voraussetzung.
- Paragraphen 7 ff. StaRUG — Restrukturierungsbeauftragter.
- Paragraphen 94 ff. StaRUG — gerichtliche Bestaetigung des Plans.
- Paragraph 3a EStG — Sanierungsertrag.
- Paragraph 7b GewStG — Gewerbesteuer-Parallel.
- Paragraph 89 AO — verbindliche Auskunft.

## / Schritt fuer Schritt

1. **StaRUG-Variante einordnen.** Die Steuerwirkung haengt nicht von der Variante ab, aber die Dokumentation der Sanierungsabsicht ist unterschiedlich schwer.
2. **Planbetroffene erfassen.** Nur die im StaRUG-Plan benannten Glaeubiger sind betroffen; andere bleiben unverzichtbar.
3. **Vier Voraussetzungen Paragraph 3a Absatz 2 EStG pruefen.**
4. **Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG aufstellen.**
5. **Restsanierungsertrag berechnen.**
6. **Antrag in der Steuererklaerung des Sanierungsjahres stellen.** Bei StaRUG ist die Vorabauskunft Paragraph 89 AO besonders empfehlenswert, weil dem Finanzamt der Plan-Hintergrund seltener vertraut ist als bei Insolvenzplaenen.
7. **Parallel-Antrag Paragraph 7b GewStG.**

## Besonderheiten im Vergleich zum Insolvenzplan

| Punkt | Insolvenzplan | StaRUG-Plan |
|---|---|---|
| Verfahrenseroeffnung | erforderlich | nicht erforderlich; nur Anzeige der Restrukturierungssache |
| Schuldner-Vertretung | meist IV oder Sachwalter | Geschaeftsleitung bleibt im Amt; Restrukturierungsbeauftragter ggf. zur Seite |
| Insolvenzgrund | Paragraphen 17, 19 InsO | drohende Zahlungsunfaehigkeit Paragraph 29 StaRUG |
| Wirkung auf alle Glaeubiger | ja | nur auf Planbetroffene |
| Dokumentation Sanierungsabsicht | aus Glaeubigerausschuss-Protokoll | aus Planbetroffenen-Voten + Verhandlungsdokumentation |
| Reichweite des Plans | umfassend | enger; nicht alle Forderungsklassen erfasst |
| Sanierungsbeduerftigkeit | meist evident | muss aktiv begruendet werden |
| Steuerlich Paragraph 3a EStG anwendbar | ja | ja, unter denselben Voraussetzungen |

## Trade-off-Matrix

| Entscheidung | wann StaRUG | wann Insolvenzplan |
|---|---|---|
| Forderungsverzicht erfasst alle Glaeubiger | nicht moeglich (Bindung nur Planbetroffene) | ja, im bestaetigten Plan |
| Geschaeftsleitung bleibt im Amt | typisch | nur in Eigenverwaltung |
| Plan-Quote hoch | typisch | typisch wenn Sanierungschance |
| Plan-Quote sehr niedrig | meist nicht durchsetzbar | ggf. ueber Cramdown |
| Sanierungserleichterung Paragraph 3a EStG | ja, falls Voraussetzungen | ja |
| Mehrheits-Cramdown | Paragraphen 26 ff. StaRUG | Paragraph 245 InsO |
| Steuerliche Verzichtsdokumentation | aufwendiger | leichter, weil Verfahrensdokumentation breit |

## Praxistipps der alten Hasen

1. **Sanierungsabsicht aus Plan-Voten ableiten.** Im StaRUG existiert keine "Glaeubigerversammlung" wie in der InsO; die Mehrheitsentscheidungen erfolgen in Klassen. Das Klassen-Voting ist der wichtigste Beleg fuer die Sanierungsabsicht.
2. **Drohende Zahlungsunfaehigkeit ist nicht Sanierungsbeduerftigkeit.** Paragraph 29 StaRUG verlangt drohende Zahlungsunfaehigkeit, Paragraph 3a Absatz 2 EStG verlangt Sanierungsbeduerftigkeit — die Belege ueberlappen sich, sind aber nicht identisch. Beide getrennt dokumentieren.
3. **Restrukturierungsbeauftragter ist nicht IV.** Er hat keine Massehaftung, aber Beratungspflichten. Wenn er den Sanierungsertrag uebersieht, kann die Schuldnerin trotzdem in der Steuerklemme landen.
4. **Vorabauskunft Paragraph 89 AO** ist im StaRUG oft besonders wertvoll, weil dem Finanzamt der vorinsolvenzliche Plan-Hintergrund seltener vertraut ist.
5. **Stabilisierungsanordnung Paragraph 49 StaRUG** verhindert Zwangsmassnahmen — auch durch das Finanzamt fuer Steuerforderungen. Trotzdem laeuft die Steueraufzeichnungspflicht weiter.

## Mustertexte / Berechnungsbeispiele

**Plan-Text fuer den darstellenden Teil eines StaRUG-Plans (Auszug):**

```
III. Steuerliche Folgen des Forderungsverzichts

Der gestaltende Teil dieses Plans sieht Forderungsverzichte der
planbetroffenen Glaeubiger der Klassen [A, B] in Hoehe von insgesamt
EUR [Betrag] vor. Dieser Verzicht loest einen Sanierungsertrag aus.

Die Voraussetzungen der Steuerbefreiung nach Paragraph 3a Absatz 2 EStG
liegen vor:

1. Sanierungsbeduerftigkeit
Die Schuldnerin steht vor drohender Zahlungsunfaehigkeit im Sinne von
Paragraph 29 StaRUG und ist ohne den Verzicht nicht ueberlebensfaehig
(Liquiditaetsplan vom [Datum] — Anlage F-2; Fortbestehensprognose vom
[Datum] — Anlage F-3).

2. Sanierungsfaehigkeit
Das Sanierungsgutachten nach IDW S 6 vom [Datum] — Anlage F-4 — belegt
die Sanierungsfaehigkeit nach Vollzug des Plans.

3. Sanierungseignung
Die Massnahmen des gestaltenden Teils — insbesondere der
Forderungsverzicht in Verbindung mit der Aufnahme einer neuen
Finanzierungslinie ueber EUR [Betrag] gemaess Anlage F-5 — fuehren zur
nachhaltigen Wiederherstellung der Zahlungsfaehigkeit.

4. Sanierungsabsicht der Glaeubiger
Die Planbetroffenen der Klassen [A, B] haben mit Mehrheiten gemaess
Paragraphen 25, 26 StaRUG zugestimmt, weil eine Sanierung ohne den Verzicht
nicht moeglich ist. Das ist in den Klassen-Voten vom [Datum] und den
Schreiben des Hauptglaeubigers [Name] vom [Datum] dokumentiert.

5. Verrechnungsreihenfolge nach Paragraph 3a Absatz 3 EStG
Siehe Anlage F-6.
```

**Verbindliche Auskunft Paragraph 89 AO — Anschreiben-Geruest:**

```
An das Finanzamt [Ort]
Antrag auf verbindliche Auskunft nach Paragraph 89 Absatz 2 AO

1. Antragsteller
[Schuldnerin, vertreten durch Geschaeftsleitung]

2. Sachverhalt
Die Antragstellerin betreibt ein Restrukturierungsverfahren nach StaRUG.
Der vorlaeufige Plan sieht einen Forderungsverzicht in Hoehe von EUR
[Betrag] vor. Der Antragsteller beabsichtigt, fuer den hieraus
resultierenden Sanierungsertrag die Anwendung von Paragraph 3a EStG.

3. Konkrete Rechtsfrage
Wir bitten um verbindliche Auskunft, ob die Finanzbehoerde
a) die Voraussetzungen Paragraph 3a Absatz 2 EStG bei dem im Entwurf
 beigefuegten StaRUG-Plan als erfuellt ansieht und
b) die Verrechnungsreihenfolge Paragraph 3a Absatz 3 EStG gemaess der
 beigefuegten Tabelle anerkennt.

4. Eigene Rechtsauffassung
[...]

5. Anlagen
[Plan-Entwurf, IDW S 6, Verlustvortrag-Bescheide, Verrechnungstabelle]
```

## Typische Fehler

1. Annahme, Paragraph 3a EStG gelte nur fuer Insolvenzplaene — er greift auch fuer StaRUG.
2. Sanierungsbeduerftigkeit mit drohender Zahlungsunfaehigkeit gleichgesetzt — beide getrennt belegen.
3. Sanierungsabsicht aus dem Klassen-Voting nicht aufbereitet — Plan-Texte muessen das ausweisen.
4. Vergessen, dass Paragraph 3a EStG keinen "StaRUG-Bonus" einbaut, sondern die normalen vier Voraussetzungen verlangt.
5. Stabilisierungsanordnung Paragraph 49 StaRUG nicht beim Finanzamt eingelegt — Aufrechnungs- und Vollstreckungsverhalten des FA bleibt sonst aktiv.

## Querverweise

Im Plugin `insolvenzrecht`:

- `insol-sanierungsgewinn-fruehe-vorbereitung-vor-plan` — Zeitachse.
- `insol-sanierungsgewinn-3a-estg-im-insolvenzplan` — Vergleichsfall.
- `insol-sanierungsgewinn-eigenverwaltung-und-cra` — Eigenverwaltungs-Schiene.
- `insol-sanierungsgewinn-7b-gewstg-im-insolvenzplan-paralleltrack` — GewSt-Parallel.
- `krisenfrueherkennung-starug` — StaRUG-Frueherkennung.

In anderen Plugins:

- `insolvenzplan-starug-planwerkstatt` — Plan-Werkstatt.
- `steuerrecht-anwalt-und-berater` — generelle Steuer-Skills.
- `grosskanzlei-corporate-ma` — Investor-Sicht.

## Quellen Stand 06/2026

### Normen

- Paragraph 3a EStG, `gesetze-im-internet.de/estg/__3a.html`.
- Paragraph 5 Absatz 2a EStG.
- Paragraph 7b GewStG, `gesetze-im-internet.de/gewstg/__7b.html`.
- Paragraph 11 KStG (Liquidationsbesteuerung, fuer Plan-B-Pfade).
- Paragraphen 4 ff. StaRUG, `gesetze-im-internet.de/starug/`.
- Paragraph 29 StaRUG, `gesetze-im-internet.de/starug/__29.html`.
- Paragraph 49 StaRUG, `gesetze-im-internet.de/starug/__49.html`.
- Paragraphen 89, 222, 227, 251 AO, `gesetze-im-internet.de/ao_1977/`.

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — § 5 Abs. 2a EStG bei Rangruecktritt (Kernentscheidung fuer DES und Rangruecktritte im StaRUG-Plan).
- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Voraussetzungen Passivierung (wirtschaftliche Belastung).
- **FG Koeln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** (vorgehend zu BFH I R 34/12) — Liquidations-Kernentscheidung; relevant fuer Plan-B-Pfade.
- **BFH, Beschl. v. 05.02.2014 — I R 34/12, BFH/NV 2014, 1014** — Ls. 3: Streitstand nicht evident rechtsfehlerhaft.
- **FG Koeln, Urt. v. 04.11.2025 — 12 K 1413/25** — Antragstellung Paragraph 3a Abs. 4 EStG.
- **FG Duesseldorf, Urt. v. 18.09.2018 — 6 K 454/15 K, DStRE 2019** — Mindestbesteuerung Definitiveffekt; Rev. anh. BFH I R 36/18.

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfuegung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782**.
- **OFD Frankfurt a. M., Rundverfuegung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560**.
- **OFD Frankfurt v. 27.12.2018, BeckVerw 447487** — Einsprueche Mindestbesteuerung ruhend.
- **OFD Nordrhein-Westfalen, Kurzinformation ESt Nr. 46/2014, akt. 22.09.2017, DB 2017, 2580**.

### Querverweis Liquidations-Pfad

- `steuerrecht-anwalt-und-berater/stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` — Drei-Phasen-Analyse fuer stehen gelassene Verbindlichkeiten in der Liquidation (Plan-B-Pfad bei Scheitern des StaRUG-Plans).

Zitierweise und Quellenpruefung siehe `references/zitierweise.md`.
