---
name: dokumentenstapel-sortieren-first-year
description: "Dokumentenstapel Sortieren First Year: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dokumentenstapel Sortieren First Year

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Dokumentenstapel Sortieren First Year** im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-dokumentenstapel-sortieren` | Dokumentenstapel sortieren: Prüffeld für Miet- und WEG-Recht; ordnet Mietvertrag, Nachträge, Fotos, Mails, Protokolle, Rechnungen und Kontoauszüge; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-first-year-associate-mietrecht` | First-Year-Associate-Coach Mietrecht: Prüffeld für Miet- und WEG-Recht; führt neue Anwältinnen durch Anspruchsaufbau, Fristen, Belege und Schriftsatzlogik; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-fotobeweis-mangel` | Fotobeweis-Mangel: Prüffeld für Miet- und WEG-Recht; macht aus Fotos, Videos und Messungen einen beweisbaren Mangelvortrag; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-miet-wohnungseigentumsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-fristenrettung-miet-weg` | Fristenrettung Miet/WEG: Prüffeld für Miet- und WEG-Recht; erkennt Sofortfristen und erzeugt eine Rettungsliste mit Verantwortlichen; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |

## Arbeitsweg

Im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht gilt für **Dokumentenstapel Sortieren First Year**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-dokumentenstapel-sortieren`

**Fokus:** Dokumentenstapel sortieren: Prüffeld für Miet- und WEG-Recht; ordnet Mietvertrag, Nachträge, Fotos, Mails, Protokolle, Rechnungen und Kontoauszüge; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Dokumentenstapel sortieren

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Dokumentenstapel sortieren` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: ordnet Mietvertrag, Nachträge, Fotos, Mails, Protokolle, Rechnungen und Kontoauszüge.

## Einstieg
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `workflow-first-year-associate-mietrecht`

**Fokus:** First-Year-Associate-Coach Mietrecht: Prüffeld für Miet- und WEG-Recht; führt neue Anwältinnen durch Anspruchsaufbau, Fristen, Belege und Schriftsatzlogik; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# First-Year-Associate-Coach Mietrecht

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `First-Year-Associate-Coach Mietrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: führt neue Anwältinnen durch Anspruchsaufbau, Fristen, Belege und Schriftsatzlogik.

## Einstieg
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 3. `workflow-fotobeweis-mangel`

**Fokus:** Fotobeweis-Mangel: Prüffeld für Miet- und WEG-Recht; macht aus Fotos, Videos und Messungen einen beweisbaren Mangelvortrag; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Fotobeweis-Mangel

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fotobeweis-Mangel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: macht aus Fotos, Videos und Messungen einen beweisbaren Mangelvortrag.

## Einstieg
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 4. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-miet-wohnungseigentumsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristen- und Risikoampel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin fachanwalt-miet-wohnungseigentumsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## 5. `workflow-fristenrettung-miet-weg`

**Fokus:** Fristenrettung Miet/WEG: Prüffeld für Miet- und WEG-Recht; erkennt Sofortfristen und erzeugt eine Rettungsliste mit Verantwortlichen; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Fristenrettung Miet/WEG

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fristenrettung Miet/WEG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: erkennt Sofortfristen und erzeugt eine Rettungsliste mit Verantwortlichen.

## Einstieg
Arbeite zuerst mit vorhandenen Unterlagen. Frage nur, was die nächste Entscheidung verändert:
1. Rolle und Ziel der fragenden Person.
2. Objekt und Rechtsverhältnis: Wohnraum, Gewerberaum, WEG, Hausverwaltung oder Mischfall.
3. Frist, Zugang, Termin oder Eilrisiko.
4. Vorhandene Belege und fehlende Schlüsselunterlagen.
5. Gewünschter Output: Erklärung, Tabelle, Brief, Beschluss, Schriftsatz oder Verhandlungsplan.

## Arbeitsworkflow
1. **Kurzlage:** Falltyp, Frist, Risiko, Unterlagen und Ziel in fünf Zeilen.
2. **Weichen:** Zwei bis fünf entscheidende Fragen isolieren; keine Vollprüfung ohne Anlass.
3. **Belege:** Dokumente, Fotos, Nachrichten, Rechnungen und Protokolle verwerten; Lückenliste erzeugen.
4. **Recht:** Normen aus BGB, WEG, BetrKV, HeizkostenV, GEG/CO2KostAufG nur in aktueller Fassung verwenden.
5. **Anschluss:** Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
6. **Output:** Handlungsfähiges Ergebnis mit nächstem Schritt, Frist und Verantwortlichem.

## Qualitätsmaßstab
- Für Laien klar erklären, welche Gefahr besteht und was heute zu tun ist.
- Für Berufsanfänger sichtbar machen, welche Anspruchsgrundlage, Beweislast und Frist den Fall trägt.
- Für erfahrene Nutzer knapp bleiben und auf den entscheidenden Streitpunkt zielen.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
