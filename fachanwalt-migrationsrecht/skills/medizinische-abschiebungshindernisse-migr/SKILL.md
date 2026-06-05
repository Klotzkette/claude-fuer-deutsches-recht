---
name: medizinische-abschiebungshindernisse-migr
description: "Medizinische Abschiebungshindernisse Migr: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Medizinische Abschiebungshindernisse Migr

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Medizinische Abschiebungshindernisse Migr** im Plugin Fachanwalt Migrationsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-medizinische-abschiebungshindernisse` | Medizinische Abschiebungshindernisse: Fachmodul im Migrationsrecht; prüft qualifiziertes Attest, Behandlung, Reisefähigkeit, Zielstaat; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck. |
| `spezial-migr-sonderfall-und-edge-case` | Migr: Sonderfall und Edge-Case-Prüfung im Plugin fachanwalt migrationsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Fachanwalt Migrationsrecht gilt für **Medizinische Abschiebungshindernisse Migr**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-medizinische-abschiebungshindernisse`

**Fokus:** Medizinische Abschiebungshindernisse: Fachmodul im Migrationsrecht; prüft qualifiziertes Attest, Behandlung, Reisefähigkeit, Zielstaat; mit deutschem Recht, EU/EMRK/GFK, Belegen, Fristen und Quellencheck.

# Medizinische Abschiebungshindernisse

## Aufgabe
Fachmodul im Plugin `fachanwalt-migrationsrecht`. Er bearbeitet: prüft qualifiziertes Attest, Behandlung, Reisefähigkeit, Zielstaat.

## Einstieg
1. Wer ist betroffen, wer fragt, und welches konkrete Ziel besteht?
2. Welche Staatsangehörigkeit/Gebietszuordnung, welcher Aufenthaltsort und welcher aktuelle Status liegen vor?
3. Welche Frist oder welches Eilrisiko entscheidet den Fall?
4. Welche Unterlagen beweisen Identität, Status, Familie, Arbeit, Ausbildung, Schutzgrund oder Gesundheit?
5. Soll das Ergebnis auf Deutsch, in einfacher Sprache oder zusätzlich auf Spanisch ausgegeben werden?

## Prüfraster
1. **Status und Ziel:** Ist der passende Titel/Schutz-/Rechtsbehelfspfad richtig gewählt?
2. **Tatbestand:** Normmerkmale, Ausnahmen, Ermessen, Versagungsgründe und Gegenargumente.
3. **EU/EMRK/GFK:** Unionsrechtliche oder menschenrechtliche Ebene prüfen, wenn sie den Fall tragen kann.
4. **Staatenbezug:** Herkunfts-, Transit- und Zielstaat nur mit aktuellen Quellen bewerten; keine statischen Sicherheitsannahmen.
5. **Beweis:** Dokumente, Urkunden, Übersetzungen, Atteste, Länderquellen und digitale Belege sauber trennen.
6. **Taktik:** Antrag, Nachreichung, Fristverlängerung, Eilantrag, Klage, Vergleich, Behördenkommunikation.

## Output
- Kurzlage und Risikoampel.
- Prüfmatrix: Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- Direkt nutzbarer Textbaustein für Behörde, Gericht, Arbeitgeber oder Mandant.
- Anschluss-Skills innerhalb dieses Plugins.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `spezial-migr-sonderfall-und-edge-case`

**Fokus:** Migr: Sonderfall und Edge-Case-Prüfung im Plugin fachanwalt migrationsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Migr: Sonderfall und Edge-Case-Prüfung

## Spezialwissen: Migr: Sonderfall und Edge-Case-Prüfung
- **Spezialgegenstand:** Migr: Sonderfall und Edge-Case-Prüfung / migr sonderfall und edge case. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AufenthG, AsylG, GFK, VO, RL, StAG, EU, GEAS.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Migr** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Qualitätsanker: Identität, Schutzstatus und aktuelle Lageprüfung

- **Verifizierte Rechtsprechungsanker:** BVerwG, Urteil vom 13.12.2023 - 1 C 34.22 und BVerwG, Urteil vom 18.12.2025 - 1 C 27.24 zur Identitätsklärung/Stufenmodell im Einbürgerungsrecht; BVerwG, Urteil vom 16.04.2025 - 1 C 18.24 zur Tatsachenrevision und Art. 4 GRCh/Art. 3 EMRK bei anerkannten Schutzberechtigten in Griechenland.
- **Prüfdisziplin:** Aufenthaltsrecht, Asylrecht, Staatsangehörigkeitsrecht, Freizügigkeit/EU, Dublin/GEAS, Abschiebungsschutz, Familiennachzug und Arbeit/Beschäftigung strikt trennen. Keine Auskunft „nach Gefühl“ über Länderpraxis oder Behördenlaufzeiten.
- **Aktualitätsfilter:** Herkunftsland, Schutzstatus, Dokumentenlage, Identität, Passbeschaffung, Zumutbarkeit, Vulnerabilität und aktuelle Lageberichte/live verfügbare Gerichtsquellen sind tragend; bei Lagefragen immer Datum und Erkenntnisbasis nennen.
- **Output-Pflicht:** Entscheidungsbaum mit Sofortfrist, zuständiger Behörde/Gericht, benötigten Unterlagen, Beweisnot-/Zumutbarkeitsargumenten und nächstem rechtssicheren Schritt.
