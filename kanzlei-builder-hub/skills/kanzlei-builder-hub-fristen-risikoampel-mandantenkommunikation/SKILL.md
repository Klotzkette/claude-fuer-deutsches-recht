---
name: kanzlei-builder-hub-fristen-risikoampel-mandantenkommunikation
description: "Fristen Risikoampel Mandantenkommunikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fristen Risikoampel Mandantenkommunikation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Fristen Risikoampel Mandantenkommunikation** im Plugin Kanzlei-Builder-Hub. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin kanzlei-builder-hub: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin kanzlei-builder-hub: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin kanzlei-builder-hub: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |

## Arbeitsweg

Im Plugin Kanzlei-Builder-Hub gilt für **Fristen Risikoampel Mandantenkommunikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin kanzlei-builder-hub: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieser Prüffeld markiert beim Skill-/Plugin-Bau die typischen Risiken: Validator-Fehler, Versionsdrift, Halluzinations-Pfade, Mandantengeheimnis-Konformität, Update-Frist für Rechtsprechungs- und Norm-Änderungen.

## Risikoampel Builder-Hub
- **Rot:** `validate-yaml-frontmatter.py` oder `validate-plugin-structure.mjs` schlägt fehl -- darf nicht ausgeliefert werden.
- **Rot:** Komma-Zahl in `description` (Frontmatter) -- "1,5" statt "1.5"; Validator schlägt fehl.
- **Rot:** Skill-Description enthält Mandantendaten / Beispiele mit Klarnamen.
- **Rot:** Bezug auf erfundene BGH-/EuGH-Az. im Skill-Inhalt.
- **Gelb:** Skill verweist auf andere Skills, die umbenannt wurden -> broken link.
- **Gelb:** Plugin enthält Skill ohne Querverweise zum Anschluss-Skill.
- **Gelb:** Skill bezieht sich auf Norm-Fassung, ohne Fassungsdatum zu nennen (z. B. "ZPO" ohne Hinweis auf KostRMoG / Beschleunigungsnovelle).
- **Grün:** Validator ohne Fehler, Querverweise konsistent, Halluzinationssperre eingebaut, Sprache Deutsch.

## Update-Fristen
- **Quartalsweise:** Norm-Updates der zentralen Gesetzbücher (BGB, ZPO, StGB, AktG, UStG, EStG, ggf. spezielle Verfahrensordnungen).
- **Monatlich:** Rspr.-Updates für Highlight-Entscheidungen (BGH Pressemitteilungen, BVerfG, EuGH).
- **Ad-hoc:** bei tagesaktuellen Gesetzes-/Verordnungsänderungen (z. B. GPSR, AI Act, eIDAS 2.0).

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin kanzlei-builder-hub: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieser Prüffeld kommuniziert Builder-Ergebnisse an die Auftraggeber-Seite (Kanzleipartner, IT-Verantwortliche, Wissensmanagement, externe Mandanten der Builder-Kanzlei) -- knapp, technisch korrekt, mit Hinweis auf Validator-Status.

## Kommunikations-Struktur
- **Was wurde gebaut:** Plugin-Name, Skill-Name(n), Version (semantisch).
- **Validator-Status:** `validate-yaml-frontmatter.py` und `validate-plugin-structure.mjs` -- OK / Fehler.
- **Was ist NICHT enthalten:** Skill-Grenzen klar benennen (kein Live-Quellencheck, kein Mandantengeheimnis-Hosting, kein KI-Output ohne Verifizierung).
- **Nächste Schritte:** Testlauf vorgesehen, Rollout-Termin, Schulungsbedarf.
- **Risiken / offene Punkte:** Halluzinationsrisiken, Mandantenakte-Konformität, BORA-Pflichten der Kanzlei beim Einsatz.

## Adressatengerecht
- **Kanzleipartner:** Geschäftsnutzen, Risikohinweise, Lizenz/Datenschutz, Schulungsaufwand.
- **IT/Admin:** Installations-/Update-Pfad, Validator-Pipeline, Abhängigkeiten.
- **Wissensmanagement:** Pflege, Zitationsstandard, Update-Zyklus für Rechtsprechungs- und Norm-Änderungen.

## Anti-Muster
- Versprechen "rechtssichere KI" -- KI ist nie ohne Verifizierung rechtssicher (Verschwiegenheit § 43a Abs. 2 BRAO, § 203 StGB, Halluzinationsrisiken).
- "Wir ersetzen den Anwalt" -- Skill ist Werkzeug, kein Mandatsverhältnis.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin kanzlei-builder-hub: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin kanzlei-builder-hub: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Builder-Hub Quality-Gate für neue Skills
- **Validator-Lauf:** `python3 scripts/validate-yaml-frontmatter.py` und `node scripts/validate-plugin-structure.mjs` — beide ohne Fehler/Warnungen.
- **Frontmatter:** Genau `name` und `description`. Keine weiteren Felder (kein `triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **Description-Länge:** max. 1024 Zeichen, KEINE Zahlen-Kommas (statt "1,5" schreibe "1.5" oder "eineinhalb").
- **Skill-Name:** max. 64 ASCII-Zeichen, kein Umlaut, kein Sonderzeichen außer Bindestrich.
- **Innenstruktur:** (1) Zweck/Anwendungsfall, (2) Eingaben, (3) Ablauf/Checkliste, (4) Quellenpflicht, (5) Ausgabeformat, (6) Beispiele.
- **Sprache:** Deutsch. Englische Fachbegriffe nur, wenn etabliert und erklärt.
- **Halluzinationssperre:** Keine erfundenen BGH/EuGH-Az.; "BGH ständige Rspr." statt erfundene Az.; Kommentar-/Aufsatz-Fundstellen nur mit Live-Beleg.
- **Reproduzierbarkeit:** Skill muss auch bei Re-Run mit gleichen Eingaben gleiches Ergebnis liefern (Modell-Streuung minimieren durch klare Checklisten).
- **Plugin-Konsistenz:** Skill verweist auf andere Skills des Plugins; keine Selbstreferenz.
- Falle: Beim Refactoring den Skill-Name ändern, ohne Verweise in anderen Skills nachzuziehen → broken-links nicht prüfbar.
