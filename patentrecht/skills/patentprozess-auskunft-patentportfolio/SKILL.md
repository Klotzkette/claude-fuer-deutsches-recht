---
name: patentprozess-auskunft-patentportfolio
description: "Patentprozess Auskunft Patentportfolio: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Patentprozess Auskunft Patentportfolio

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Patentprozess Auskunft Patentportfolio** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patentprozess-auskunft-rechnungslegung-schadensersatz` | Bereitet Folgeansprüche nach Patentverletzung vor: Auskunft, Rechnungslegung, Rückruf, Vernichtung, Schadensberechnung, Lizenzanalogie, Verletzergewinn und Daten-/Geheimnisschutz. |
| `patentportfolio-und-technikstrategie` | Unterstützt Patentportfolio- und Technikstrategie: Schutzzaun, Roadmap, Wettbewerbsmonitoring, defensive Veröffentlichungen, Anmeldepriorisierung, Länderstrategie und Budgetsteuerung. |
| `abmahnung-patentverletzung-verteidigung` | Verteidigt gegen Patentabmahnungen: Fristen, Unterlassungserklärung, Registerstand, Anspruchsfassung, Nichtverletzung, Rechtsbestand, Vorbenutzungsrecht, Schutzschrift, Vergleich und Mandantenkommunikation. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Patentprozess Auskunft Patentportfolio**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `patentprozess-auskunft-rechnungslegung-schadensersatz`

**Fokus:** Bereitet Folgeansprüche nach Patentverletzung vor: Auskunft, Rechnungslegung, Rückruf, Vernichtung, Schadensberechnung, Lizenzanalogie, Verletzergewinn und Daten-/Geheimnisschutz.

# Patentprozess: Auskunft, Rechnungslegung, Schadensersatz

## Aufgabe

Remedies nach Verletzungsfeststellung oder Vergleichsverhandlung.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Anspruchsziel und Zeitraum definieren.**
2. **Produkte, Lieferketten und Umsätze erfassen.**
3. **Schadensmethoden getrennt bewerten.**
4. **Geheimhaltungs- und Datenschutzrisiken bei Zahlenmaterial markieren.**
5. **Vergleichs- und Audit-Klauseln vorbereiten.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Remedies Matrix.
- Accounting Request Draft.
- Damages Data Room List.
- Settlement Numbers Memo.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 2. `patentportfolio-und-technikstrategie`

**Fokus:** Unterstützt Patentportfolio- und Technikstrategie: Schutzzaun, Roadmap, Wettbewerbsmonitoring, defensive Veröffentlichungen, Anmeldepriorisierung, Länderstrategie und Budgetsteuerung.

# Patentportfolio und Technikstrategie

## Analyseachsen

1. Produkte und Roadmap.
2. technische Kernfeatures und Differenzierung.
3. Wettbewerber und Patentlandschaft.
4. Länder und Umsatzmärkte.
5. Fertigung, Lieferkette und Reverse Engineering.
6. Budget, Timing, Investorenerwartung.
7. Geheimhaltung versus Offenlegung.

## Strategieoptionen

- Kernpatent breit absichern.
- Teilanmeldungen und Verbesserungsanmeldungen planen.
- Gebrauchsmuster als schneller taktischer Schutz.
- FTO vor Launch priorisieren.
- Monitoring für kritische Wettbewerber.
- defensive Veröffentlichung bei nicht schutzwürdigen, aber blockaderelevanten Details.
- Lizenzierungs- oder Cross-License-Strategie.

## Output

- Portfolio-Landkarte.
- Anmeldepriorisierung.
- Recherche- und Monitoringplan.
- Budget- und Fristenübersicht.
- Board-/Investor-taugliche Kurzfassung.

## Kosten, Routen und Fristen-Anker

- **DPMA-Anmeldung:** 60 EUR Anmeldegebühr, ab 11. Anspruch je 30 EUR; Prüfungsantrag bis 7 Jahre (§ 44 PatG) für 350 EUR.
- **EPA-Anmeldung:** ca. 280 EUR Anmeldegebühr, 1.520 EUR Recherchegebühr, 1.890 EUR Prüfungsgebühr, ab 16. Anspruch je 270 EUR (Gebühren regelmäßig prüfen).
- **PCT:** Internationale Phase 18 Monate ab Priorität; nationale/regionale Phase je nach Staat 30 oder 31 Monate.
- **Einheitspatent (Unitary Patent):** ab Erteilung Antrag binnen 1 Monat; Jahresgebühr nach UPC-Tarif (geringer als national bei viel-Land-Strategie).
- **UPC-Opt-Out:** während Übergangszeit (sunrise period) möglich; nach Übergangszeit Opt-out nur eingeschränkt.
- **Jahresgebühren DPMA:** ab 3. Patentjahr 70 EUR; Steigerung jährlich; ab 20. Jahr 1.940 EUR.
- **Strategie-Faustregeln:** Kernpatent breit anmelden, Familie auseinanderhalten (DE+EP+US+CN als typisch); Gebrauchsmuster nur für schnellen taktischen Schutz; defensive Veröffentlichung bei Stand-der-Technik-Vorrat.
- **Investorenkommunikation:** Patent-Status mit Reifegrad (Anmeldung pending vs. erteilt) und geographischer Abdeckung; "Patente angemeldet" ist NICHT identisch mit "erteilt".
- Falle: 30-Monats-Frist PCT-Übergang in nationale Phase versäumen — Wiedereinsetzung sehr eng (Art. 122 EPÜ unter Voraussetzungen).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `abmahnung-patentverletzung-verteidigung`

**Fokus:** Verteidigt gegen Patentabmahnungen: Fristen, Unterlassungserklärung, Registerstand, Anspruchsfassung, Nichtverletzung, Rechtsbestand, Vorbenutzungsrecht, Schutzschrift, Vergleich und Mandantenkommunikation.

# Patentabmahnung verteidigen

## Sofortscan

1. Frist und Zustellung.
2. Absender, Vertreter, Schutzrecht, Anspruchsfassung, Territory.
3. Geforderte Erklärung: Unterlassung, Auskunft, Rechnungslegung, Rückruf, Vernichtung, Kostenerstattung.
4. Produktbezug und konkrete Verletzungsbehauptung.
5. Eilrisiko: einstweilige Verfügung, Messe, Launch, Lieferstopp.

## Verteidigungslinien

- Schutzrecht nicht in Kraft oder falsche Anspruchsfassung.
- Produkt verwirklicht ein Merkmal nicht.
- Äquivalenz greift nicht.
- Rechtsbestand zweifelhaft.
- Vorbenutzungsrecht oder Lizenz.
- Erschöpfung oder Lieferketteneinwand.
- Unterlassungserklärung zu weit, Vertragsstrafe zu riskant, Konzern-/Lieferkettenumfang unklar.
- Vergleich, Standstill, Design-around oder negative Feststellung.

## Output

- Fristen- und Sofortmaßnahmenplan.
- Claim Chart Verteidigung.
- Redline-Risiken der Unterlassungserklärung.
- Mandantenmail mit Entscheidungsoptionen.
- Entwurf Antwortschreiben an Gegenseite.

## Regel

Nie empfehlen, eine vorformulierte Unterlassungserklärung ungeprüft zu unterschreiben. Immer Umfang, Vertragsstrafe, Anerkenntniswirkung, Auskunft und Rückruf isoliert prüfen.

## Anker-Normen und Doktrinen
- **§ 9 PatG:** Allein- und Mitbenutzungsrecht; Verletzungstatbestand.
- **§ 14 PatG / Art. 69 EPÜ + Protokoll:** Schutzbereich richtet sich nach den Patentansprüchen; Beschreibung und Zeichnungen sind heranzuziehen.
- **§ 139 PatG:** Unterlassungs- und Schadensersatzanspruch (Schadensersatz dreistufig: konkret, Lizenzanalogie, Gewinnabschöpfung).
- **§ 140a PatG:** Vernichtung; **§ 140b PatG:** Auskunftsanspruch.
- **§ 12 PatG:** Vorbenutzungsrecht -- inländische ernsthafte Benutzung vor Prioritätstag schützt vor Verletzung.
- **Äquivalenzdoktrin** (BGH, Schneidmesser-Linie, vgl. ständige Rspr.): drei Schritte (gleiche Wirkung, Auffindbarkeit, Gleichwertigkeit im Schutzbereich).
- **Erschöpfung:** rechtmäßig in den EWR in Verkehr gebrachte Erzeugnisse.
- **FRAND-Pflichten bei SEP:** EuGH Huawei/ZTE, C-170/13, Urt. v. 16.07.2015.

## Schutzschrift
- Hinterlegung im Zentralen Schutzschriftenregister `schutzschriftenregister.de`; spätestens vor Antragstellung der eV; sechs Monate Gültigkeit.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
