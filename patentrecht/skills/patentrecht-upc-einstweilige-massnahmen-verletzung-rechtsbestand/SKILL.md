---
name: patentrecht-upc-einstweilige-massnahmen-verletzung-rechtsbestand
description: "UPC Einstweilige Massnahmen Verletzung Rechtsbestand: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# UPC Einstweilige Massnahmen Verletzung Rechtsbestand

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **UPC Einstweilige Massnahmen Verletzung Rechtsbestand** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `upc-einstweilige-massnahmen` | Bereitet einstweilige Maßnahmen vor dem UPC vor: Dringlichkeit, Schutzbereich, Rechtsbestand, Beweislast, Schutzschrift, Geheimnisschutz, Vollziehung und Vergleichsfenster. |
| `upc-verletzung-und-rechtsbestand` | Prüft Einheitliches Patentgericht UPC: Verletzungsklage, Zentral-/Lokal-/Regionalkammer, Widerklage auf Nichtigerklärung, Opt-out, Einheitspatent und klassische europäische Patente. |
| `upc-widerruf-und-widerklage-revocation` | Plant isolierte Widerrufsklage und Widerklage auf Nichtigerklärung vor dem UPC, inklusive zentraler Kammer, Verletzungsverfahren, Hilfsanträgen und Koordination mit EPA-Einspruch. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **UPC Einstweilige Massnahmen Verletzung Rechtsbestand**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `upc-einstweilige-massnahmen`

**Fokus:** Bereitet einstweilige Maßnahmen vor dem UPC vor: Dringlichkeit, Schutzbereich, Rechtsbestand, Beweislast, Schutzschrift, Geheimnisschutz, Vollziehung und Vergleichsfenster.

# UPC: Einstweilige Maßnahmen

## Aufgabe

Preliminary injunctions und provisional measures vor dem UPC aus Antragsteller- oder Antragsgegnerperspektive.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Dringlichkeit und Kenntniszeitpunkt rekonstruieren.**
2. **Verletzungsnachweise und Rechtsbestandsangriff parallel prüfen.**
3. **Schutzschrift-/Protective-Letter-Strategie abwägen.**
4. **Geheimhaltungsanträge, Besichtigung und Sicherheitsleistung prüfen.**
5. **Antragsentwurf oder Verteidigungsfahrplan erstellen.**


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

- PI-Readiness-Check.
- Protective-Letter-Outline.
- Evidence Bundle.
- Hearing Script.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 2. `upc-verletzung-und-rechtsbestand`

**Fokus:** Prüft Einheitliches Patentgericht UPC: Verletzungsklage, Zentral-/Lokal-/Regionalkammer, Widerklage auf Nichtigerklärung, Opt-out, Einheitspatent und klassische europäische Patente.

# UPC: Verletzung, Rechtsbestand und Zuständigkeit

## Aufgabe

UPC-Route für europäische Patentstreitigkeiten mit Zuständigkeit, Opt-out-Status, Verletzungs- und Rechtsbestandsangriffen.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Patentart klären: Einheitspatent oder EP-Bündelpatent.**
2. **Opt-out und Übergangsregime live im UPC/EPO-Kontext prüfen.**
3. **Kammerwahl nach Sitz, Verletzungsort, Beklagtem und Patentklassifikation vorbereiten.**
4. **Verletzungsangriff, Revocation-Counterclaim und Bifurcation-Risiko abbilden.**
5. **Verfahrenssprache, CMS-Anforderungen und Beweismittelpaket planen.**


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

- UPC-Routenmemo.
- Claim/Invalidity Matrix.
- CMS-Aktionsliste.
- Mandantenampel.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `upc-widerruf-und-widerklage-revocation`

**Fokus:** Plant isolierte Widerrufsklage und Widerklage auf Nichtigerklärung vor dem UPC, inklusive zentraler Kammer, Verletzungsverfahren, Hilfsanträgen und Koordination mit EPA-Einspruch.

# UPC: Widerruf und Revocation Counterclaim

## Aufgabe

Rechtsbestandsangriffe vor dem UPC mit Parallelität zu EPO-Opposition und nationalen Verfahren.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Angriffsgründe: Neuheit, erfinderische Tätigkeit, Ausführbarkeit, unzulässige Erweiterung, Schutzbereichserweiterung.**
2. **Stand der Technik mit Merkmalstabelle zuordnen.**
3. **Parallelverfahren EPA/national prüfen.**
4. **Hilfsantragslogik und Stay-/Bifurcation-Argumente erfassen.**
5. **Settlement- und Cross-License-Fenster markieren.**


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

- Revocation Strategy Memo.
- Invalidity Chart.
- Parallel Proceedings Map.
- Local Counsel Brief.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
