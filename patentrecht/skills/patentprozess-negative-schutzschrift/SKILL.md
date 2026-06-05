---
name: patentprozess-negative-schutzschrift
description: "Patentprozess Negative Schutzschrift: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Patentprozess Negative Schutzschrift

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Patentprozess Negative Schutzschrift** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patentprozess-negative-feststellungsklage` | Prüft negative Feststellungsklagen, Nichtverletzungserklärungen, Forum-Risiken, Abmahnreaktionen und grenzüberschreitende Koordination bei Patentstreitigkeiten. |
| `patentprozess-schutzschrift-und-caveat` | Erstellt Schutzschrift-/Protective-Letter-Strategien für deutsche Patentgerichte, UPC und ausländische Eilrisiken, inklusive Nichtverletzung, Rechtsbestand, Dringlichkeit und Geheimhaltungsanträgen. |
| `patentsettlement-und-cross-license-litigation` | Unterstützt Patentvergleiche: Cross-License, Covenant not to sue, Territory, Field of Use, Release, Rückruf, Kosten, Kartellrecht, Geheimhaltung und Vollstreckbarkeit. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Patentprozess Negative Schutzschrift**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `patentprozess-negative-feststellungsklage`

**Fokus:** Prüft negative Feststellungsklagen, Nichtverletzungserklärungen, Forum-Risiken, Abmahnreaktionen und grenzüberschreitende Koordination bei Patentstreitigkeiten.

# Patentprozess: Negative Feststellung und Torpedo-Risiken

## Aufgabe

Aktive Verteidigung und Forum-Strategie bei drohender Patentklage.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Rechtschutzbedürfnis und Drohlage erfassen.**
2. **Forum, Zuständigkeit und Territorialität prüfen.**
3. **Nichtverletzungsargumente in claim construction übersetzen.**
4. **Parallel zu Revocation/FTO/Schutzschrift planen.**
5. **Kommunikationsrisiken gegenüber Gegner und Kunden steuern.**


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

- DNI Strategy Memo.
- Forum Risk Map.
- Non-Infringement Chart.
- Client Communication Draft.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 2. `patentprozess-schutzschrift-und-caveat`

**Fokus:** Erstellt Schutzschrift-/Protective-Letter-Strategien für deutsche Patentgerichte, UPC und ausländische Eilrisiken, inklusive Nichtverletzung, Rechtsbestand, Dringlichkeit und Geheimhaltungsanträgen.

# Patentprozess: Schutzschrift und Protective Letter

## Aufgabe

Vorbeugende Verteidigung gegen erwartete Eilanträge.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Antragswahrscheinlichkeit und Foren bestimmen.**
2. **Nichtverletzung und Rechtsbestandsangriffe priorisieren.**
3. **Dringlichkeits- und Verhältnismäßigkeitsargumente sammeln.**
4. **Belege, Anlagen und Geheimhaltungsbedarf strukturieren.**
5. **Einreichungs- und Aktualisierungsplan festlegen.**


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

- Protective Letter Draft Points.
- Forum Filing Map.
- Evidence Bundle Index.
- Update Calendar.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `patentsettlement-und-cross-license-litigation`

**Fokus:** Unterstützt Patentvergleiche: Cross-License, Covenant not to sue, Territory, Field of Use, Release, Rückruf, Kosten, Kartellrecht, Geheimhaltung und Vollstreckbarkeit.

# Patentvergleich und Cross-License im Streit

## Aufgabe

Vergleichs- und Lizenzarchitektur im laufenden Patentstreit.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Litigation-Ziele und rote Linien aufnehmen.**
2. **Schutzrechte, Produkte, Territorien und Konzernparteien mappen.**
3. **Cross-License, Release und future products sauber trennen.**
4. **Kartellrecht, Wettbewerberkontakt und FRAND-Risiken markieren.**
5. **Term Sheet und Vollzugsschritte erstellen.**


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

- Settlement Term Sheet.
- Cross-License Matrix.
- Red Flag List.
- Board Memo.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
