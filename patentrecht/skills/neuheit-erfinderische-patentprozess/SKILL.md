---
name: neuheit-erfinderische-patentprozess
description: "Neuheit Erfinderische Patentprozess: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Neuheit Erfinderische Patentprozess

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Neuheit Erfinderische Patentprozess** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `neuheit-und-erfinderische-taetigkeit` | Prüft Patentfähigkeit mit Merkmalsgliederung, Neuheit nach § 3 PatG/Art. 54 EPÜ und erfinderischer Tätigkeit nach § 4 PatG/Art. 56 EPÜ; nutzt Einzeldokumentprüfung und Aufgaben-Lösungs-Ansatz. |
| `patentprozess-besichtigung-beweissicherung` | Strukturiert Besichtigung, Beweissicherung und technische Dokumentation in Patentstreitigkeiten: Produktzugang, Geheimnisschutz, Sachverständige, Testkäufe, Reverse Engineering und chain of custody. |
| `patentprozess-claim-construction-de-en` | Übersetzt Patentansprüche prozessfest zwischen Deutsch und Englisch: Merkmalsgliederung, claim construction, Äquivalenz, Prosecution History, technische Begriffe und gerichtstaugliche Argumentation. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Neuheit Erfinderische Patentprozess**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `neuheit-und-erfinderische-taetigkeit`

**Fokus:** Prüft Patentfähigkeit mit Merkmalsgliederung, Neuheit nach § 3 PatG/Art. 54 EPÜ und erfinderischer Tätigkeit nach § 4 PatG/Art. 56 EPÜ; nutzt Einzeldokumentprüfung und Aufgaben-Lösungs-Ansatz.

# Neuheit und erfinderische Tätigkeit

## Neuheit

1. Anspruch in Merkmale gliedern.
2. Eine konkrete Entgegenhaltung auswählen.
3. Prüfen, ob genau diese Entgegenhaltung alle Merkmale unmittelbar und eindeutig offenbart.
4. Keine Mosaikbildung bei der Neuheit.
5. Ergebnis pro Merkmal belegen: Dokument, Stelle, Figur, Absatz, Anspruch.

## Erfinderische Tätigkeit

1. Nächstliegenden Stand der Technik bestimmen.
2. Unterschiede zum Anspruch festhalten.
3. Technische Wirkung der Unterschiede bestimmen.
4. Objektive technische Aufgabe formulieren.
5. Prüfen, ob der Fachmann die Lösung ausgehend vom Stand der Technik nahegelegt bekommen hätte.
6. Gegenargumente sauber notieren: rückschauende Betrachtung, fehlender Anlass, technische Vorurteile, überraschende Wirkung, willkürliche Auswahl.

## Output

| Merkmal | Anspruch | Entgegenhaltung | Offenbart? | Fundstelle | Kommentar |
| --- | --- | --- | --- | --- | --- |

Danach:

- **Neuheit:** ja/nein/unklar mit Begründung.
- **Erfinderische Tätigkeit:** tragende Argumente pro/contra.
- **Claim-Drafting-Folge:** welche Merkmale müssen in Anspruch 1, welche in Unteransprüche?
- **Recherche-Folge:** welche Suchlücken bleiben?

## Vorsicht

Wenn die Entgegenhaltung nur aus Zusammenfassung, Maschinenübersetzung oder Bild ohne Volltext vorliegt, Ergebnis als vorläufig kennzeichnen und Volltext/Originalsprache prüfen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `patentprozess-besichtigung-beweissicherung`

**Fokus:** Strukturiert Besichtigung, Beweissicherung und technische Dokumentation in Patentstreitigkeiten: Produktzugang, Geheimnisschutz, Sachverständige, Testkäufe, Reverse Engineering und chain of custody.

# Patentprozess: Besichtigung und Beweissicherung

## Aufgabe

Beweissicherung bei komplexen technischen Produkten und Verfahren.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Beweisfrage präzise formulieren.**
2. **Zugang zu Produkt, Anlage, Quellcode oder Verfahren rechtlich und praktisch planen.**
3. **Geheimnisschutz und Neutralität der Untersuchung sichern.**
4. **Sachverständigen- und Testprotokoll entwerfen.**
5. **Beweisqualität in Claim Chart überführen.**


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

- Evidence Preservation Plan.
- Inspection Request Outline.
- Chain-of-Custody Sheet.
- Technical Test Protocol.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `patentprozess-claim-construction-de-en`

**Fokus:** Übersetzt Patentansprüche prozessfest zwischen Deutsch und Englisch: Merkmalsgliederung, claim construction, Äquivalenz, Prosecution History, technische Begriffe und gerichtstaugliche Argumentation.

# Patentprozess: Claim Construction DE/EN

## Aufgabe

Bilinguale Anspruchsauslegung für deutsche, UPC- und Common-Law-nahe Verfahren.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Anspruch in technische Merkmale zerlegen.**
2. **Begriffspaare DE/EN mit Definition und Fundstelle erfassen.**
3. **Beschreibung, Figuren und Prosecution History zuordnen.**
4. **Wortsinngemäß/Äquivalenz/Nichtverletzung getrennt argumentieren.**
5. **Gerichts- und Mandantenfassung erstellen.**


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

- Bilingual Claim Construction Table.
- Merkmalsgliederung.
- Hearing Vocabulary Sheet.
- Argument Skeleton.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
