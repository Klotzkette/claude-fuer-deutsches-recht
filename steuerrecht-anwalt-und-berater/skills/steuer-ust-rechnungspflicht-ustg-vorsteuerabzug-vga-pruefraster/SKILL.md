---
name: steuer-ust-rechnungspflicht-ustg-vorsteuerabzug-vga-pruefraster
description: "Steuer UST Rechnungspflicht Ustg Vorsteuerabzug VGA Pruefraster: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer UST Rechnungspflicht Ustg Vorsteuerabzug VGA Pruefraster

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Steuer UST Rechnungspflicht Ustg Vorsteuerabzug VGA Pruefraster** im Plugin Steuerrecht Anwalt Und Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fa-stu-ust-rechnungspflicht-14-ustg` | Vollstaendiger Skill zur umsatzsteuerlichen Rechnungspflicht — Pflichtangaben Sonderfaelle Kleinbetragsrechnung Rechnungsberichtigung Rueckwirkung der Berichtigung und Folge eines unrichtigen oder unberechtigten Steuerausweises § 14c UStG. Anwendungsfall Aussenpruefung beanstandet Rechnungen wegen formeller Maengel oder Mandant hat zu hohe Umsatzsteuer ausgewiesen. Behandelt e-Rechnung Pflicht ab 2025 ZUGFeRD XRechnung und elektronische Uebermittlung. Output Mustertabelle Pflichtangaben und Berichtigungsschreiben. Abgrenzung zu fa-stu-ust-vorsteuerabzug-15-ustg. |
| `fa-stu-ust-vorsteuerabzug-15-ustg` | Vollstaendige Pruefung des Vorsteuerabzugs nach § 15 UStG — Unternehmereigenschaft Leistungsbezug fuer das Unternehmen ordnungsgemaesse Rechnung Ausschlusstatbestaende und EuGH-Rechtsprechung zum formellen Mangel. Anwendungsfall Aussenpruefung versagt Vorsteuerabzug wegen formeller Rechnungsmaengel fehlender Leistungsbeschreibung oder Verdacht auf Karussellgeschaeft. Behandelt § 15 UStG iVm § 14 UStG MwStSystRL und der nationale Ausgleich durch § 14a UStG. Output Pruefraster und Argumentationsmuster. Abgrenzung zu fa-stu-ust-rechnungspflicht-14-ustg. |
| `fa-stu-vga-pruefraster` | Pruefraster zur verdeckten Gewinnausschuettung — Vermoegensminderung oder verhinderte Vermoegensmehrung Veranlassung im Gesellschaftsverhaeltnis Auswirkung auf Einkommen Behandlung beim Gesellschafter. Anwendungsfall Aussenpruefung erkennt Geschaeftsfuehrervergueterung Verrechnungspreise oder Gesellschafterdarlehen als verdeckte Ausschuettung und fordert Hinzurechnung. Behandelt klassische Fallgruppen Geschaeftsfuehrer-Gehaltsexzess Beherrschende-Gesellschafter Klarheits- und Rueckwirkungsverbot sowie Folgen Kapitalertragsteuer Anrechnung. Output Argumentationsraster mit Kompensationspruefung. Abgrenzung zu fa-stu-kst-organschaft-14-kstg. |
| `fa-stu-vorbehaltsaufgaben-stberg` | Pruefung der Vorbehaltsaufgaben nach StBerG — wer darf welche steuerliche Hilfeleistung erbringen und welche Folge hat die unerlaubte Hilfeleistung. Anwendungsfall Unternehmen oder Lohnsteuerhilfeverein berufen sich auf eingeschraenkte Befugnisse oder eine Werkstattgesellschaft will steuerliche Hilfe ohne Berater anbieten. Behandelt Vollberater Lohnsteuerhilfevereine Buchstellen Bilanzbuchhalter und § 5 StBerG Ordnungswidrigkeit. Output Pruefraster und Stellungnahmemuster. Abgrenzung zu fa-stu-stberg-vereinbare-taetigkeit. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer UST Rechnungspflicht Ustg Vorsteuerabzug VGA Pruefraster**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fa-stu-ust-rechnungspflicht-14-ustg`

**Fokus:** Vollstaendiger Skill zur umsatzsteuerlichen Rechnungspflicht — Pflichtangaben Sonderfaelle Kleinbetragsrechnung Rechnungsberichtigung Rueckwirkung der Berichtigung und Folge eines unrichtigen oder unberechtigten Steuerausweises § 14c UStG. Anwendungsfall Aussenpruefung beanstandet Rechnungen wegen formeller Maengel oder Mandant hat zu hohe Umsatzsteuer ausgewiesen. Behandelt e-Rechnung Pflicht ab 2025 ZUGFeRD XRechnung und elektronische Uebermittlung. Output Mustertabelle Pflichtangaben und Berichtigungsschreiben. Abgrenzung zu fa-stu-ust-vorsteuerabzug-15-ustg.


# Rechnungspflicht und Rechnungsberichtigung — § 14 § 14a § 14c UStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechnungspflicht und Rechnungsberichtigung — § 14 § 14a § 14c UStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Sind alle Pflichtangaben § 14 Abs. 4 UStG vorhanden?
2. Greifen Erleichterungen § 33 UStDV Kleinbetragsrechnung bis 250 Euro?
3. Liegt Reverse-Charge vor und wurde Hinweis nach § 14a Abs. 5 UStG aufgenommen?
4. Ist der Steuerausweis unberechtigt oder unrichtig § 14c UStG — Berichtigungsweg pruefen?
5. Wurde elektronische Rechnung iSd § 14 Abs. 1 UStG ab 2025 verwendet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 14 UStG** — Rechnungspflicht; e-Rechnungs-Pflicht ab 1. Januar 2025.
- **§ 14a UStG** — Zusatzangaben.
- **§ 14c UStG** — unrichtiger oder unberechtigter Steuerausweis.
- **§ 33 UStDV** — Kleinbetragsrechnungen.
- **§ 14b UStG** — Aufbewahrung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 14 UStG · § 14a UStG · § 14b UStG · § 14c UStG · § 33 UStDV · § 31 UStDV · § 18 UStG (Voranmeldung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 2. `fa-stu-ust-vorsteuerabzug-15-ustg`

**Fokus:** Vollstaendige Pruefung des Vorsteuerabzugs nach § 15 UStG — Unternehmereigenschaft Leistungsbezug fuer das Unternehmen ordnungsgemaesse Rechnung Ausschlusstatbestaende und EuGH-Rechtsprechung zum formellen Mangel. Anwendungsfall Aussenpruefung versagt Vorsteuerabzug wegen formeller Rechnungsmaengel fehlender Leistungsbeschreibung oder Verdacht auf Karussellgeschaeft. Behandelt § 15 UStG iVm § 14 UStG MwStSystRL und der nationale Ausgleich durch § 14a UStG. Output Pruefraster und Argumentationsmuster. Abgrenzung zu fa-stu-ust-rechnungspflicht-14-ustg.


# Vorsteuerabzug — § 15 UStG materielle und formelle Voraussetzungen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorsteuerabzug — § 15 UStG materielle und formelle Voraussetzungen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Hat der Mandant Unternehmereigenschaft iSd § 2 UStG mit nachhaltiger Taetigkeit?
2. Wurde die Leistung fuer das Unternehmen bezogen (Mindestnutzung 10 Prozent § 15 Abs. 1 S. 2 UStG)?
3. Liegt eine ordnungsgemaesse Rechnung mit Pflichtangaben § 14 § 14a UStG vor?
4. Gibt es einen Ausschluss § 15 Abs. 1a UStG (Repraesentationsaufwendungen)?
5. Sind die Rechnungen rueckwirkend berichtigungsfaehig (EuGH Senatex)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 15 UStG** — Vorsteuerabzug.
- **§ 14 UStG** — Pflichtangaben in der Rechnung.
- **§ 14a UStG** — zusaetzliche Angaben in besonderen Faellen.
- **§ 14c UStG** — unrichtiger oder unberechtigter Steuerausweis.
- **MwStSystRL Art. 167 ff.** — gemeinschaftsrechtliche Grundlage.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 15 UStG · § 14 UStG · § 14a UStG · § 14c UStG · § 2 UStG · MwStSystRL Art. 167 ff. · § 25b UStG (innergem. Dreiecksgeschaeft)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 3. `fa-stu-vga-pruefraster`

**Fokus:** Pruefraster zur verdeckten Gewinnausschuettung — Vermoegensminderung oder verhinderte Vermoegensmehrung Veranlassung im Gesellschaftsverhaeltnis Auswirkung auf Einkommen Behandlung beim Gesellschafter. Anwendungsfall Aussenpruefung erkennt Geschaeftsfuehrervergueterung Verrechnungspreise oder Gesellschafterdarlehen als verdeckte Ausschuettung und fordert Hinzurechnung. Behandelt klassische Fallgruppen Geschaeftsfuehrer-Gehaltsexzess Beherrschende-Gesellschafter Klarheits- und Rueckwirkungsverbot sowie Folgen Kapitalertragsteuer Anrechnung. Output Argumentationsraster mit Kompensationspruefung. Abgrenzung zu fa-stu-kst-organschaft-14-kstg.


# Verdeckte Gewinnausschuettung — § 8 Abs. 3 S. 2 KStG Pruefraster

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verdeckte Gewinnausschuettung — § 8 Abs. 3 S. 2 KStG Pruefraster` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Liegt eine Vermoegensminderung oder verhinderte Vermoegensmehrung bei der Kapitalgesellschaft vor?
2. Ist die Veranlassung im Gesellschaftsverhaeltnis zu suchen (Fremdvergleich)?
3. Bei beherrschenden Gesellschaftern: war die Vereinbarung im Voraus klar und tatsaechlich durchgefuehrt?
4. Auswirkungen auf das Einkommen — Hinzurechnung und auf Ebene des Gesellschafters § 20 Abs. 1 Nr. 1 S. 2 EStG?
5. Kapitalertragsteuer 25 Prozent und Erstattungsanspruch bei Anteilseigner im Ausland (DBA)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 8 Abs. 3 S. 2 KStG** — Definition vGA und Folge auf Ebene der KapGes.
- **§ 20 Abs. 1 Nr. 1 S. 2 EStG** — Behandlung beim Gesellschafter.
- **§ 43 ff. EStG** — Kapitalertragsteuerabzug.
- **§ 4 Abs. 1 S. 1 EStG** — Vermoegensvergleich; Massstab.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 8 Abs. 3 S. 2 KStG · § 8b KStG (Befreiungssystem) · § 20 Abs. 1 Nr. 1 S. 2 EStG · §§ 43 ff. EStG · § 32a KStG (Korrespondenzregel)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 4. `fa-stu-vorbehaltsaufgaben-stberg`

**Fokus:** Pruefung der Vorbehaltsaufgaben nach StBerG — wer darf welche steuerliche Hilfeleistung erbringen und welche Folge hat die unerlaubte Hilfeleistung. Anwendungsfall Unternehmen oder Lohnsteuerhilfeverein berufen sich auf eingeschraenkte Befugnisse oder eine Werkstattgesellschaft will steuerliche Hilfe ohne Berater anbieten. Behandelt Vollberater Lohnsteuerhilfevereine Buchstellen Bilanzbuchhalter und § 5 StBerG Ordnungswidrigkeit. Output Pruefraster und Stellungnahmemuster. Abgrenzung zu fa-stu-stberg-vereinbare-taetigkeit.


# Vorbehaltsaufgaben Steuerberater — § 3 § 4 StBerG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorbehaltsaufgaben Steuerberater — § 3 § 4 StBerG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Welche Taetigkeit konkret ausgeuebt — Erstellung Erklaerung Buchfuehrung Beratung?
2. Wer fuehrt sie aus — Steuerberater Buchhalter Lohnsteuerhilfeverein Unternehmer?
3. Greift § 4 StBerG Befugnis zur eingeschraenkten Hilfeleistung?
4. Liegt unerlaubte Hilfeleistung § 5 StBerG vor — Ordnungswidrigkeit § 160 StBerG?
5. Welche zivilrechtliche Folge — § 134 BGB Nichtigkeit?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 3 StBerG** — befugte Personen.
- **§ 4 StBerG** — eingeschraenkte Befugnis Lohnsteuerhilfevereine Buchstellen.
- **§ 5 StBerG** — Verbot unerlaubter Hilfeleistung.
- **§ 160 StBerG** — Bussgeld.
- **§ 134 BGB** — Nichtigkeit gesetzwidriger Rechtsgeschaefte.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 3 StBerG · § 4 StBerG · § 5 StBerG · § 160 StBerG · § 134 BGB · § 6 StBerG (ausgenommene Taetigkeiten)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.
