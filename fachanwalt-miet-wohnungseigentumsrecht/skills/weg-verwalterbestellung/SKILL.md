---
name: weg-verwalterbestellung
description: "Weg Verwalterbestellung, Weg Verwalterpflichtverletzung, Weg Verwaltungsbeirat Kommunikation, Weg Waermepumpe Geg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Weg Verwalterbestellung, Weg Verwalterpflichtverletzung, Weg Verwaltungsbeirat Kommunikation, Weg Waermepumpe Geg, Weg Weihnachtsbaum Verkehrssicherung

## Arbeitsbereich

Dieser Skill bündelt **Weg Verwalterbestellung, Weg Verwalterpflichtverletzung, Weg Verwaltungsbeirat Kommunikation, Weg Waermepumpe Geg, Weg Weihnachtsbaum Verkehrssicherung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `spezial-weg-verwalterbestellung` | Verwalterbestellung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Bestellung, Vertrag, zertifizierter Verwalter, Laufzeit, Abberufung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-weg-verwalterpflichtverletzung` | Verwalterpflichtverletzung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Pflicht, Beschlussumsetzung, Schaden, Entlastung, Abberufung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-weg-verwaltungsbeirat-kommunikation` | Beiratskommunikation: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft E-Mail-Verteiler, Datenschutz, Protokoll, Beschlussvorbereitung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-weg-waermepumpe-geg` | WEG Wärmepumpe/GEG: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft GEG-Pflichten, Beschluss, Duldung, Finanzierung und Mieterschnittstellen; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-weg-weihnachtsbaum-verkehrssicherung` | Weihnachtsbaum/Verkehrssicherung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Aufstellung, Brandschutz, Haftung, Beschluss, Versicherung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |

## Arbeitsweg

Für **Weg Verwalterbestellung, Weg Verwalterpflichtverletzung, Weg Verwaltungsbeirat Kommunikation, Weg Waermepumpe Geg, Weg Weihnachtsbaum Verkehrssicherung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `fachanwalt-miet-wohnungseigentumsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `spezial-weg-verwalterbestellung`

**Fokus:** Verwalterbestellung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Bestellung, Vertrag, zertifizierter Verwalter, Laufzeit, Abberufung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Verwalterbestellung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verwalterbestellung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Bestellung, Vertrag, zertifizierter Verwalter, Laufzeit, Abberufung.

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

## 2. `spezial-weg-verwalterpflichtverletzung`

**Fokus:** Verwalterpflichtverletzung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Pflicht, Beschlussumsetzung, Schaden, Entlastung, Abberufung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Verwalterpflichtverletzung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verwalterpflichtverletzung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Pflicht, Beschlussumsetzung, Schaden, Entlastung, Abberufung.

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

## 3. `spezial-weg-verwaltungsbeirat-kommunikation`

**Fokus:** Beiratskommunikation: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft E-Mail-Verteiler, Datenschutz, Protokoll, Beschlussvorbereitung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Beiratskommunikation

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beiratskommunikation` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft E-Mail-Verteiler, Datenschutz, Protokoll, Beschlussvorbereitung.

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

## 4. `spezial-weg-waermepumpe-geg`

**Fokus:** WEG Wärmepumpe/GEG: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft GEG-Pflichten, Beschluss, Duldung, Finanzierung und Mieterschnittstellen; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# WEG Wärmepumpe/GEG

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `WEG Wärmepumpe/GEG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft GEG-Pflichten, Beschluss, Duldung, Finanzierung und Mieterschnittstellen.

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

## 5. `spezial-weg-weihnachtsbaum-verkehrssicherung`

**Fokus:** Weihnachtsbaum/Verkehrssicherung: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Aufstellung, Brandschutz, Haftung, Beschluss, Versicherung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Weihnachtsbaum/Verkehrssicherung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Weihnachtsbaum/Verkehrssicherung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Aufstellung, Brandschutz, Haftung, Beschluss, Versicherung.

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
