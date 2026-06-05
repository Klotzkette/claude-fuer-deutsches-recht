---
name: zeitmietvertrag-wasserschaden-trocknung-weg
description: "Zeitmietvertrag Wasserschaden Trocknung WEG: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zeitmietvertrag Wasserschaden Trocknung WEG

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Zeitmietvertrag Wasserschaden Trocknung WEG** im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-zeitmietvertrag` | Zeitmietvertrag: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Befristungsgrund, Mitteilung, Verlängerung, Kündigung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-wasserschaden-trocknung` | Wasserschaden/Trocknung: Fachmodul im Miet- und Wohnungseigentumsrecht; klärt Ursache, Zutritt, Trocknungsgeräte, Stromkosten, Ersatzwohnraum und Versicherung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-weg-beirat-haftung` | Verwaltungsbeirat Haftung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Kontrollpflicht, Belege, Interessenkonflikt, Entlastung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-betriebskosten-materiell` | Materielle Betriebskostenprüfung: Umlagefähigkeit nach Mietvertrag und BetrKV, laufende Kosten, Wirtschaftlichkeitsgebot, Abgrenzung Wartung/Reparatur, Verwaltung/Instandhaltung, Hausmeistersplit, Versicherung, Grundsteuer, Belege und Korrekturberechnung. |
| `spezial-grundsteuer-umlage` | Grundsteuer-Umlage: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Umlagevereinbarung, Veranlagung, Wirtschaftseinheit, Eigentumswechsel; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht gilt für **Zeitmietvertrag Wasserschaden Trocknung WEG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-zeitmietvertrag`

**Fokus:** Zeitmietvertrag: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Befristungsgrund, Mitteilung, Verlängerung, Kündigung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Zeitmietvertrag

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeitmietvertrag` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Befristungsgrund, Mitteilung, Verlängerung, Kündigung.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `spezial-wasserschaden-trocknung`

**Fokus:** Wasserschaden/Trocknung: Fachmodul im Miet- und Wohnungseigentumsrecht; klärt Ursache, Zutritt, Trocknungsgeräte, Stromkosten, Ersatzwohnraum und Versicherung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Wasserschaden/Trocknung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Wasserschaden/Trocknung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: klärt Ursache, Zutritt, Trocknungsgeräte, Stromkosten, Ersatzwohnraum und Versicherung.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 3. `spezial-weg-beirat-haftung`

**Fokus:** Verwaltungsbeirat Haftung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Kontrollpflicht, Belege, Interessenkonflikt, Entlastung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Verwaltungsbeirat Haftung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verwaltungsbeirat Haftung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Kontrollpflicht, Belege, Interessenkonflikt, Entlastung.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 4. `spezial-betriebskosten-materiell`

**Fokus:** Materielle Betriebskostenprüfung: Umlagefähigkeit nach Mietvertrag und BetrKV, laufende Kosten, Wirtschaftlichkeitsgebot, Abgrenzung Wartung/Reparatur, Verwaltung/Instandhaltung, Hausmeistersplit, Versicherung, Grundsteuer, Belege und Korrekturberechnung.

# Betriebskosten materiell

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebskosten materiell` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill ist die Kostenarten-Lupe. Er prüft, ob eine formal verständliche Abrechnung inhaltlich stimmt. Der Fokus liegt auf echten Abzugsbeträgen, nicht auf pauschalem Misstrauen.

## Kernprüfung

1. **Vertragliche Umlagegrundlage**: BetrKV-Verweis, konkrete Kostenliste, "sonstige Betriebskosten" konkret vereinbart?
2. **Betriebskostenbegriff**: laufend entstehende Kosten durch Eigentum, Erbbaurecht oder bestimmungsgemäßen Gebrauch; keine Verwaltungskosten, keine Instandhaltung/Instandsetzung.
3. **Kostenart**: BetrKV-Zuordnung je Position, etwa Grundsteuer, Wasser, Entwässerung, Heizung, Warmwasser, Aufzug, Straßenreinigung, Müll, Gebäudereinigung, Gartenpflege, Beleuchtung, Versicherung, Hauswart, Gemeinschaftsantenne/Breitband, Wäschepflege, sonstige Betriebskosten.
4. **Wirtschaftlichkeit**: auffällige Kostensteigerungen, unnötige Dienstleister, Doppelerfassung, nicht marktgerechte Verträge.
5. **Belege**: Rechnung, Vertrag, Leistungszeitraum, Zahlungsbeleg, Aufmaß/Stundenliste, Umlageberechnung.

## Problempositionen

| Position | Typischer Fehler | Prüfung |
| --- | --- | --- |
| Hausmeister | Reparaturen, Verwaltung, Wohnungsabnahmen eingemischt | Stunden-/Tätigkeitsnachweise splitten |
| Gartenpflege | Neuanlage/Umgestaltung statt laufender Pflege | Rechnungstext und Leistungsbeschreibung prüfen |
| Wartung | Reparaturanteil versteckt | Wartungsvertrag und Einzelrechnung trennen |
| Versicherung | nicht grundstücksbezogene Risiken | Police und Beitragsrechnung lesen |
| Aufzug | Vollwartung mit Reparaturanteil | Wartungs-/Instandsetzungsanteil herausrechnen |
| Bank/Verwalter | Verwaltungskosten | grundsätzlich nicht umlagefähig |
| Gewerbe | Restaurant/Praxis verursacht Mehrkosten | Vorwegabzug prüfen |
| CO2 | gar nicht oder pauschal verteilt | CO2KostAufG-Rechnung erstellen |

## Beweis und Taktik

- Mieterseite: erst Belegeinsicht verlangen, dann konkrete Einwendungen nachschieben; Einwendungsfrist nach § 556 Abs. 3 Satz 5 BGB im Blick behalten.
- Vermieterseite: Kostenpositionen nur verteidigen, wenn Belege, Zahlungsfluss und Vertragsgrundlage zusammenpassen.
- Prozess: Bestreiten muss nach Belegeinsicht konkret werden; ohne Belegeinsicht bleibt Zurückbehaltung gegen Nachforderung taktisch wichtig.

## Ausgabe

- Kostenartenmatrix mit BetrKV-Ziffer, Betrag, Beleg, Einwand und Korrektur.
- Bezifferte Kürzung je Position.
- Kurzes Mandantenbild: "zahlen", "teilweise zahlen", "zurückbehalten", "klagen/abwehren".
- Entwurf für Belegeinsicht, Einwendung, Vergleichsvorschlag oder Schriftsatzbaustein.

## Quellen- und Sicherheitsregel

Normtexte von BetrKV, § 556 BGB, § 556a BGB, HeizkostenV und CO2KostAufG aktuell prüfen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## 5. `spezial-grundsteuer-umlage`

**Fokus:** Grundsteuer-Umlage: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Umlagevereinbarung, Veranlagung, Wirtschaftseinheit, Eigentumswechsel; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Grundsteuer-Umlage

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer-Umlage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Umlagevereinbarung, Veranlagung, Wirtschaftseinheit, Eigentumswechsel.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
