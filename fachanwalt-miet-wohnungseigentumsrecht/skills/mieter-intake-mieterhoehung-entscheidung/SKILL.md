---
name: mieter-intake-mieterhoehung-entscheidung
description: "Mieter Intake Mieterhoehung Entscheidung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mieter Intake Mieterhoehung Entscheidung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Mieter Intake Mieterhoehung Entscheidung** im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mieter-intake` | Mieter-Intake: Prüffeld für Miet- und WEG-Recht; sortiert Mängel, Geld, Kündigung, Räumung, Sozialschutz und Belege; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-mieterhoehung-entscheidung` | Mieterhöhung-Entscheidung: Prüffeld für Miet- und WEG-Recht; berechnet Zustimmungspflicht, Kappung, Sperrfrist und Einwendungen; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-mietkonto-kontoauszug` | Mietkonto und Kontoauszug: Prüffeld für Miet- und WEG-Recht; rekonstruiert Soll/Ist, Rückstände, Tilgungsbestimmung und Schonfristzahlung; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-mietpreisbremse-start` | Mietpreisbremse-Start: Prüffeld für Miet- und WEG-Recht; klärt Gebiet, Vormiete, Neubau/Modernisierung, Rüge und Rückforderung; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |
| `workflow-modernisierung-entscheidung` | Modernisierung-Entscheidung: Prüffeld für Miet- und WEG-Recht; klärt Duldung, Härte, Ankündigung, Kosten und spätere Umlage; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output. |

## Arbeitsweg

Im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht gilt für **Mieter Intake Mieterhoehung Entscheidung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mieter-intake`

**Fokus:** Mieter-Intake: Prüffeld für Miet- und WEG-Recht; sortiert Mängel, Geld, Kündigung, Räumung, Sozialschutz und Belege; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Mieter-Intake

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieter-Intake` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: sortiert Mängel, Geld, Kündigung, Räumung, Sozialschutz und Belege.

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

## 2. `workflow-mieterhoehung-entscheidung`

**Fokus:** Mieterhöhung-Entscheidung: Prüffeld für Miet- und WEG-Recht; berechnet Zustimmungspflicht, Kappung, Sperrfrist und Einwendungen; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Mieterhöhung-Entscheidung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieterhöhung-Entscheidung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: berechnet Zustimmungspflicht, Kappung, Sperrfrist und Einwendungen.

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

## 3. `workflow-mietkonto-kontoauszug`

**Fokus:** Mietkonto und Kontoauszug: Prüffeld für Miet- und WEG-Recht; rekonstruiert Soll/Ist, Rückstände, Tilgungsbestimmung und Schonfristzahlung; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Mietkonto und Kontoauszug

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietkonto und Kontoauszug` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: rekonstruiert Soll/Ist, Rückstände, Tilgungsbestimmung und Schonfristzahlung.

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

## 4. `workflow-mietpreisbremse-start`

**Fokus:** Mietpreisbremse-Start: Prüffeld für Miet- und WEG-Recht; klärt Gebiet, Vormiete, Neubau/Modernisierung, Rüge und Rückforderung; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Mietpreisbremse-Start

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietpreisbremse-Start` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: klärt Gebiet, Vormiete, Neubau/Modernisierung, Rüge und Rückforderung.

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

## 5. `workflow-modernisierung-entscheidung`

**Fokus:** Modernisierung-Entscheidung: Prüffeld für Miet- und WEG-Recht; klärt Duldung, Härte, Ankündigung, Kosten und spätere Umlage; mit Kaltstart, Fristencheck, Belegmatrix, Anschluss-Skills und nutzbarem Output.

# Modernisierung-Entscheidung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Modernisierung-Entscheidung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Dieser Prüffeld macht den Einstieg in `fachanwalt-miet-wohnungseigentumsrecht` leichter. Schwerpunkt: klärt Duldung, Härte, Ankündigung, Kosten und spätere Umlage.

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
