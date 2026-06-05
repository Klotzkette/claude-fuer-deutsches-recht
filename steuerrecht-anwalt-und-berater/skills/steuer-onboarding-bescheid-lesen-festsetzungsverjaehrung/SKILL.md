---
name: steuer-onboarding-bescheid-lesen-festsetzungsverjaehrung
description: "Steuer Onboarding Bescheid Lesen Festsetzungsverjaehrung: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer Onboarding Bescheid Lesen Festsetzungsverjaehrung

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer Onboarding Bescheid Lesen Festsetzungsverjaehrung** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fa-stu-onboarding-bescheid-lesen` | Anleitung zum schnellen und vollstaendigen Erfassen jedes Steuerbescheids — von der Bekanntgabe bis zur Rechtsbehelfsbelehrung. Anwendungsfall Mandant bringt einen Bescheid Anwalt oder Steuerberater muss in zehn Minuten Einspruchsbedarf Fristen und materielle Angriffspunkte erkennen. Behandelt Bekanntgabe Drei-Tages-Fiktion Bestandskraft Vorlaeufigkeitsvermerk Vorbehalt der Nachpruefung Aenderungs- und Korrekturnormen §§ 129 164 165 172 173 175 AO und Rechtsbehelfsbelehrung. Output Checkliste Bescheid-Erstpruefung und Marker fuer Einspruchs- bzw. Aenderungsantrag. Abgrenzung zu anw-einspruch-finanzamt und fa-stu-finanzgerichtsklage-78-fgo. |
| `fa-stu-onboarding-festsetzungsverjaehrung` | Vollstaendige Bearbeitung der Festsetzungsverjaehrung — regulaere und verlaengerte Fristen Anlaufhemmung Ablaufhemmung und besondere Verjaehrungsregeln bei Aussenpruefung Steuerhinterziehung Erbfaellen und ausstehender Steuererklaerung. Anwendungsfall Berater muss pruefen ob ein Steueranspruch noch festgesetzt werden kann oder ob die Finanzbehoerde verspaetet handelt. Behandelt Beginn der Frist nach Abgabe der Erklaerung Anlaufhemmung drei Jahre Ablaufhemmung durch Pruefungsbeginn § 171 Abs. 4 AO und durch laufendes Strafverfahren § 171 Abs. 5 AO. Output Pruefraster und Verjaehrungsrechner. Abgrenzung zu fa-stu-onboarding-verzinsung. |
| `fa-stu-onboarding-korrekturnormen` | Systematischer Vergleich der Korrekturnormen — wann ist welche Vorschrift einschlaegig wann begruendet sie Aenderung zugunsten oder zu Lasten des Steuerpflichtigen und welche Frist gilt. Anwendungsfall Berater hat einen bestandskraeftigen Bescheid und sucht den richtigen Aenderungstatbestand oder muss sich gegen Aenderung des Finanzamts wehren. Behandelt offenbare Unrichtigkeit Vorbehalt der Nachpruefung Vorlaeufigkeit schlichte Aenderung neue Tatsachen widerstreitende Steuerfestsetzungen Grundlagenbescheide und Verfahrensaufhebung. Output Entscheidungsbaum mit Voraussetzungen je Norm. Abgrenzung zu fa-stu-onboarding-bescheid-lesen. |
| `fa-stu-onboarding-mandantenkommunikation` | Leitfaden zur Mandantenkommunikation in steuerlichen Mandaten — wann muss aufgeklaert werden wie wird dokumentiert und welche Fallstricke schaffen Haftungsrisiko fuer Anwalt und Steuerberater. Anwendungsfall Berater hat eine Empfehlung zu unterbreiten die Mehrsteuer Nachzahlungszinsen oder strafrechtliche Risiken aufwirft und muss dies dokumentieren. Behandelt Hinweispflicht auf Risiken Steuergefahren Vorteilhaftigkeitsvergleich Aufklaerung ueber Vergleichswege und Dokumentation in der Akte. Output Aufklaerungsbogen und Bestaetigungsmuster. Abgrenzung zu fa-stu-onboarding-mandatsannahme und fa-stu-rvg-steuerstreit. |
| `fa-stu-onboarding-mandatsannahme` | Erstgespraech-Leitfaden fuer steuerrechtliche Mandate. Anwendungsfall Mandant kommt mit Bescheid Pruefungsanordnung oder Vorladung; Anwalt oder Steuerberater muss in 30 Minuten Sachverhalt Fristen und Risiko klaeren. Behandelt Mandantenfragebogen Interessenkonflikt § 43a BRAO § 57 StBerG Vollmachtsvarianten Verfahrens- und Strafverteidigungsvollmacht Honorarvereinbarung RVG/StBVV Vergueterungsabrede und Aufklaerungspflichten. Output strukturierter Erstberatungsbogen Vollmachtsmuster und Triage-Checkliste mit Fristampel. Abgrenzung zu fa-stu-rvg-steuerstreit (Honorar im Detail) und anw-fristenbuch-steuerrecht (laufende Fristverwaltung). |
| `fa-stu-onboarding-rechtsbehelfssystematik` | Vollstaendige Uebersicht aller steuerlichen Rechtsbehelfe — auf welcher Stufe welcher Rechtsbehelf zustaendig ist welche Frist gilt und welche Zwischenanordnungen verfuegbar sind. Anwendungsfall Berater muss bei Mandatsannahme strategisch entscheiden welche Verfahrenswege offen sind und welche Erfolgsaussicht sie haben. Behandelt Einspruch Klage Revision Nichtzulassungsbeschwerde Anhoerungsruege Verfassungsbeschwerde Vorlage an EuGH AdV einstweiliger Rechtsschutz. Output Entscheidungsbaum mit Wegweiser. Abgrenzung zu anw-einspruch-finanzamt fa-stu-finanzgerichtsklage-78-fgo und anw-aussetzung-vollziehung. |
| `fa-stu-onboarding-verwaltungsanweisungen` | Methodik zur Nutzung und Abgrenzung von Verwaltungsanweisungen im Steuerrecht — BMF-Schreiben Anwendungserlass zur AO Umsatzsteuer-Anwendungserlass Einkommen- und Koerperschaftsteuer-Richtlinien Erbschaftsteuer-Hinweise. Anwendungsfall Berater muss entscheiden ob ein BMF-Schreiben fuer Mandant guenstig ist und ob er sich dem Finanzamt gegenueber darauf berufen kann. Behandelt Bindungswirkung Selbstbindung der Verwaltung Art. 3 GG Vertrauensschutz und prozessuale Verwertbarkeit. Output Argumentationsraster und Zitierhilfe. Abgrenzung zu fa-stu-onboarding-beratungsstruktur und fa-stu-onboarding-bescheid-lesen. |
| `fa-stu-onboarding-verzinsung` | Systematik aller Steuerzinsen — Nachzahlungs- und Erstattungszinsen § 233a AO Hinterziehungszinsen § 235 AO Stundungs- und Aussetzungszinsen §§ 234 237 AO Saeumniszuschlaege § 240 AO und Zinssatzanpassung nach BVerfG-Vorgaben. Anwendungsfall Berater muss Zinsfolge eines Bescheids quantifizieren und pruefen ob Zinsen angreifbar sind. Behandelt Zinsbeginn Karenzzeit 15 Monate Zinslauf Zinsfestsetzung und Aenderungen nach § 233a Abs. 5 AO sowie Verfassungsmaessigkeit des Zinssatzes. Output Berechnungsschema und Argumentationsraster gegen Zinsbescheide. Abgrenzung zu anw-aussetzung-vollziehung. |
| `fa-stu-quellensteuer-50a-estg` | Praxisbearbeitung des Quellensteuerabzugs nach § 50a EStG — Tatbestaende Bemessungsgrundlage Abzugsverfahren Freistellungs- und Erstattungsverfahren. Anwendungsfall Inlaendischer Vergueterungsschuldner zahlt an einen beschraenkt Steuerpflichtigen (Kuenstler Sportler Aufsichtsrat Lizenzen) und muss Steuer einbehalten. Behandelt Schuldner Glaeubiger Bemessungsgrundlage Bruttoabzug 15 Prozent bzw. 30 Prozent Erstattung nach § 50c EStG und DBA-Bezug. Output Pruefraster und Antragsmuster Freistellungsbescheinigung. Abgrenzung zu fa-stu-doppelbesteuerung-musterabkommen-oecd. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer Onboarding Bescheid Lesen Festsetzungsverjaehrung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fa-stu-onboarding-bescheid-lesen`

**Fokus:** Anleitung zum schnellen und vollstaendigen Erfassen jedes Steuerbescheids — von der Bekanntgabe bis zur Rechtsbehelfsbelehrung. Anwendungsfall Mandant bringt einen Bescheid Anwalt oder Steuerberater muss in zehn Minuten Einspruchsbedarf Fristen und materielle Angriffspunkte erkennen. Behandelt Bekanntgabe Drei-Tages-Fiktion Bestandskraft Vorlaeufigkeitsvermerk Vorbehalt der Nachpruefung Aenderungs- und Korrekturnormen §§ 129 164 165 172 173 175 AO und Rechtsbehelfsbelehrung. Output Checkliste Bescheid-Erstpruefung und Marker fuer Einspruchs- bzw. Aenderungsantrag. Abgrenzung zu anw-einspruch-finanzamt und fa-stu-finanzgerichtsklage-78-fgo.

# Steuerbescheid lesen — die ersten 10 Minuten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Steuerbescheid lesen — die ersten 10 Minuten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Ist der Bescheid ein Erstbescheid Aenderungs- oder Berichtigungsbescheid?
2. Steht er unter Vorbehalt der Nachpruefung § 164 AO oder vorlaeufig § 165 AO?
3. Gibt es eine ordnungsgemaesse Rechtsbehelfsbelehrung (sonst Jahresfrist § 356 Abs. 2 AO)?
4. Wann ist Bekanntgabe bewirkt (Stempel, Drei-Tages-Fiktion § 122 Abs. 2 AO, ELSTER-Bereitstellung § 122a AO)?
5. Welche Besteuerungsgrundlagen wurden veraendert; gibt es Erlaeuterungstext am Bescheidende?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 122 AO** — Bekanntgabe von Verwaltungsakten.
- **§ 124 AO** — Wirksamkeit eines Verwaltungsakts.
- **§ 157 AO** — Form und Inhalt von Steuerbescheiden.
- **§ 164 AO** — Vorbehalt der Nachpruefung.
- **§ 165 AO** — Vorlaeufige Steuerfestsetzung.
- **§§ 129 172 173 174 175 AO** — Korrektur- und Aenderungsnormen.
- **§ 356 AO** — Rechtsbehelfsbelehrung; Folge fehlerhafter Belehrung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 122 AO · § 124 AO · § 157 AO · § 164 AO · § 165 AO · § 129 AO · § 172 AO · § 173 AO · § 174 AO · § 175 AO · § 356 AO

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Bescheid-Checkliste

| Pruefpunkt | Wo im Bescheid | Folge |
| --- | --- | --- |
| Adressat korrekt | Kopf | sonst Bekanntgabemangel |
| Steuerart und Zeitraum | Kopf | sonst Inhaltsmangel |
| Festgesetzter Betrag | Tenor | Basis fuer AdV-Antrag |
| Vorbehalt der Nachpruefung | Tenor / Erlaeuterungen | jederzeit Aenderung § 164 Abs. 2 AO |
| Vorlaeufigkeitsvermerk | Erlaeuterungen | Reichweite genau pruefen |
| Rechtsbehelfsbelehrung | Ende | fehlt oder fehlerhaft → Jahresfrist § 356 Abs. 2 AO |
| Erlaeuterungstext | letzte Seite | Indikator fuer Streitpunkt |


## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 2. `fa-stu-onboarding-festsetzungsverjaehrung`

**Fokus:** Vollstaendige Bearbeitung der Festsetzungsverjaehrung — regulaere und verlaengerte Fristen Anlaufhemmung Ablaufhemmung und besondere Verjaehrungsregeln bei Aussenpruefung Steuerhinterziehung Erbfaellen und ausstehender Steuererklaerung. Anwendungsfall Berater muss pruefen ob ein Steueranspruch noch festgesetzt werden kann oder ob die Finanzbehoerde verspaetet handelt. Behandelt Beginn der Frist nach Abgabe der Erklaerung Anlaufhemmung drei Jahre Ablaufhemmung durch Pruefungsbeginn § 171 Abs. 4 AO und durch laufendes Strafverfahren § 171 Abs. 5 AO. Output Pruefraster und Verjaehrungsrechner. Abgrenzung zu fa-stu-onboarding-verzinsung.

# Festsetzungsverjaehrung — §§ 169 bis 171 AO in der Praxis

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Festsetzungsverjaehrung — §§ 169 bis 171 AO in der Praxis` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Welche Steuerart und welcher Veranlagungszeitraum sind betroffen?
2. Wurde Steuererklaerung abgegeben — sonst Anlaufhemmung bis spaetestens drei Jahre § 170 Abs. 2 AO?
3. Gilt die regulaere vier Jahres Frist § 169 Abs. 2 Nr. 2 AO oder verlaengerte zehn Jahre bei Hinterziehung § 169 Abs. 2 S. 2 AO?
4. Liegt Ablaufhemmung wegen Aussenpruefung § 171 Abs. 4 AO oder Steuerstrafverfahren § 171 Abs. 5 AO vor?
5. Bei Schenkungen und Erbfaellen besondere Anlaufhemmung § 170 Abs. 5 AO beachten.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 169 AO** — Festsetzungsverjaehrung; Regelfrist vier Jahre.
- **§ 169 Abs. 2 S. 2 AO** — Verlaengerung auf zehn Jahre bei Hinterziehung; fuenf Jahre bei leichtfertiger Verkuerzung.
- **§ 170 AO** — Beginn der Festsetzungsfrist; Anlaufhemmung.
- **§ 171 AO** — Ablaufhemmung; verbreitetste Vorschrift Abs. 4 (Aussenpruefung) Abs. 5 (Strafverfahren) Abs. 14 (Grundlagenbescheid).
- **§ 47 AO** — Erloeschen durch Festsetzungsverjaehrung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 169 AO · § 170 AO · § 171 AO · § 47 AO · § 181 AO (gesonderte Feststellung) · § 191 Abs. 3 AO (Haftungsbescheid)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 3. `fa-stu-onboarding-korrekturnormen`

**Fokus:** Systematischer Vergleich der Korrekturnormen — wann ist welche Vorschrift einschlaegig wann begruendet sie Aenderung zugunsten oder zu Lasten des Steuerpflichtigen und welche Frist gilt. Anwendungsfall Berater hat einen bestandskraeftigen Bescheid und sucht den richtigen Aenderungstatbestand oder muss sich gegen Aenderung des Finanzamts wehren. Behandelt offenbare Unrichtigkeit Vorbehalt der Nachpruefung Vorlaeufigkeit schlichte Aenderung neue Tatsachen widerstreitende Steuerfestsetzungen Grundlagenbescheide und Verfahrensaufhebung. Output Entscheidungsbaum mit Voraussetzungen je Norm. Abgrenzung zu fa-stu-onboarding-bescheid-lesen.

# Korrektur von Steuerbescheiden — §§ 129 164 165 172 173 174 175 AO im Ueberblick

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Korrektur von Steuerbescheiden — §§ 129 164 165 172 173 174 175 AO im Ueberblick` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Liegt eine offenbare Unrichtigkeit vor — Schreib- oder Rechenfehler § 129 AO?
2. Steht der Bescheid unter Vorbehalt § 164 AO oder ist er vorlaeufig § 165 AO?
3. Soll eine schlichte Aenderung § 172 Abs. 1 Nr. 2a AO innerhalb der Einspruchsfrist gestellt werden?
4. Sind neue Tatsachen oder Beweismittel iSd § 173 AO entstanden — und wessen Verschulden steht der Aenderung entgegen?
5. Liegt eine widerstreitende Festsetzung § 174 AO oder ein Grundlagenbescheid § 175 AO vor?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 129 AO** — offenbare Unrichtigkeit.
- **§ 164 AO** — Vorbehalt der Nachpruefung.
- **§ 165 AO** — vorlaeufige Festsetzung.
- **§ 172 AO** — Aenderung von Steuerbescheiden allgemein.
- **§ 173 AO** — neue Tatsachen und Beweismittel.
- **§ 173a AO** — Schreib- und Rechenfehler bei Erklaerung.
- **§ 174 AO** — widerstreitende Steuerfestsetzungen.
- **§ 175 AO** — Aenderung wegen Grundlagenbescheid oder rueckwirkendem Ereignis.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 129 AO · § 164 AO · § 165 AO · § 172 AO · § 173 AO · § 173a AO · § 174 AO · § 175 AO · § 175a AO · § 176 AO (Vertrauensschutz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 4. `fa-stu-onboarding-mandantenkommunikation`

**Fokus:** Leitfaden zur Mandantenkommunikation in steuerlichen Mandaten — wann muss aufgeklaert werden wie wird dokumentiert und welche Fallstricke schaffen Haftungsrisiko fuer Anwalt und Steuerberater. Anwendungsfall Berater hat eine Empfehlung zu unterbreiten die Mehrsteuer Nachzahlungszinsen oder strafrechtliche Risiken aufwirft und muss dies dokumentieren. Behandelt Hinweispflicht auf Risiken Steuergefahren Vorteilhaftigkeitsvergleich Aufklaerung ueber Vergleichswege und Dokumentation in der Akte. Output Aufklaerungsbogen und Bestaetigungsmuster. Abgrenzung zu fa-stu-onboarding-mandatsannahme und fa-stu-rvg-steuerstreit.

# Mandantenkommunikation und Aufklaerungspflicht im Steuerrecht

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenkommunikation und Aufklaerungspflicht im Steuerrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Welche Handlungsalternativen bestehen und welche Mehr- oder Minder-Steuer ist mit jeder verbunden?
2. Welches Steuerstrafrisiko ist erkennbar — muss zwingend auf § 371 AO und § 153 AO hingewiesen werden?
3. Welche Fristen laufen — hat der Mandant verstanden dass Untaetigkeit zur Bestandskraft fuehrt?
4. Wurde der Mandant ueber Honorarrahmen und Kostenrisiken aufgeklaert?
5. Wurde die Empfehlung schriftlich oder mit Aktenvermerk dokumentiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 280 BGB** — Schadensersatz wegen Pflichtverletzung; Anwalts- und Steuerberaterhaftung.
- **§ 675 BGB** — entgeltliche Geschaeftsbesorgung.
- **§ 33 StBerG** — Berufsbild Steuerberater; eigenverantwortliche Vertretung.
- **§ 43a Abs. 3 BRAO** — Sachlichkeitsgebot; Beratung sachlich und vollstaendig.
- **§ 153 AO** — Berichtigungspflicht bei nachtraeglich erkannter Unrichtigkeit.
- **§ 371 AO** — Selbstanzeige.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 280 BGB · § 675 BGB · § 33 StBerG · § 43a BRAO · § 153 AO · § 371 AO · § 89 AO (verbindliche Auskunft) · § 204 AO (verbindliche Zusage)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Praxisformulierung / Antragsmuster

```
AUFKLAERUNGS- UND ENTSCHEIDUNGSBESTAETIGUNG

Mandant: [NAME], [ADRESSE]
Berater: [NAME], [KANZLEI]
Sache: [STEUERART, JAHR, AKTENZEICHEN]

Heute am [DATUM] habe ich folgende Handlungsoptionen erlaeutert:
1. [OPTION A] — voraussichtliche Mehrsteuer: [BETRAG]; Risiken: [...]
2. [OPTION B] — voraussichtliche Mehrsteuer: [BETRAG]; Risiken: [...]
3. Untaetigkeit — Folge: Bestandskraft des Bescheids.

Ausdruecklich hingewiesen wurde auf:
- Berichtigungspflicht nach § 153 AO bei nachtraeglichem Erkennen einer Unrichtigkeit
- Moeglichkeit der Selbstanzeige nach § 371 AO und ihre Sperrgruende
- Nachzahlungszinsen § 233a AO und Hinterziehungszinsen § 235 AO
- Frist und Kosten

Der Mandant entscheidet sich fuer Option [...].

[ORT, DATUM] [UNTERSCHRIFT MANDANT] [UNTERSCHRIFT BERATER]
```

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 5. `fa-stu-onboarding-mandatsannahme`

**Fokus:** Erstgespraech-Leitfaden fuer steuerrechtliche Mandate. Anwendungsfall Mandant kommt mit Bescheid Pruefungsanordnung oder Vorladung; Anwalt oder Steuerberater muss in 30 Minuten Sachverhalt Fristen und Risiko klaeren. Behandelt Mandantenfragebogen Interessenkonflikt § 43a BRAO § 57 StBerG Vollmachtsvarianten Verfahrens- und Strafverteidigungsvollmacht Honorarvereinbarung RVG/StBVV Vergueterungsabrede und Aufklaerungspflichten. Output strukturierter Erstberatungsbogen Vollmachtsmuster und Triage-Checkliste mit Fristampel. Abgrenzung zu fa-stu-rvg-steuerstreit (Honorar im Detail) und anw-fristenbuch-steuerrecht (laufende Fristverwaltung).

# Mandatsannahme im Steuerrecht — Erstgespraech und Risiko-Triage

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandatsannahme im Steuerrecht — Erstgespraech und Risiko-Triage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Verfahrensstadium klaeren: Veranlagung, Einspruch, Klage, Aussenpruefung, Steuerstrafverfahren, Vollstreckung?
2. Welcher Bescheid oder welche Verfuegung liegt vor (Datum, Zustellungsdatum, Aktenzeichen, Steuerart)?
3. Frist sofort errechnen: Einspruch § 355 AO ein Monat, Klage § 47 FGO ein Monat, AdV § 361 AO formlos.
4. Interessenkonflikt § 43a Abs. 4 BRAO bzw. § 57 Abs. 1 StBerG pruefen (gegenlaeufige Mandate, Konzern, Ehegatten).
5. Steuerstrafrechtlicher Anfangsverdacht? Dann Belehrung nach § 393 AO und ggf. Schweigen empfehlen.
6. Wer ist Mandant: natuerliche Person, Personengesellschaft, Kapitalgesellschaft, Insolvenzverwalter, Erbe?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 43a BRAO** — anwaltliche Grundpflichten; Verschwiegenheit, Interessenkollision.
- **§ 57 StBerG** — Grundpflichten des Steuerberaters; unabhaengige eigenverantwortliche Berufsausuebung.
- **§§ 80 ff. AO** — Vollmachtswirkung im Besteuerungsverfahren.
- **§ 62 FGO** — Prozessvollmacht vor dem Finanzgericht.
- **§ 49b BRAO / § 64 StBerG / RVG / StBVV** — Honorarvereinbarungen, gesetzliche Gebuehren.
- **§ 393 AO** — Verhaeltnis Besteuerungs- zu Strafverfahren; nemo tenetur.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 43a BRAO · § 57 StBerG · §§ 80 ff. AO · § 62 FGO · § 393 AO · § 355 AO (Einspruchsfrist) · § 47 FGO (Klagefrist) · § 49b BRAO · § 64 StBerG · RVG · StBVV

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Praxisformulierung / Antragsmuster

```
VOLLMACHT (steuerrechtliches Mandat)

Ich/Wir, [MANDANT], Steuernummer [NR], bevollmaechtige(n)
Herrn/Frau Rechtsanwalt/Steuerberater [NAME], Kanzlei [KANZLEI],
in der Steuerangelegenheit betreffend [STEUERART] [VERANLAGUNGSZEITRAUM]
gegenueber dem Finanzamt [ORT] sowie der Finanzgerichtsbarkeit
umfassend zur Vertretung, insbesondere zur:
- Akteneinsicht (§ 364 AO, § 78 FGO)
- Einlegung von Rechtsbehelfen (Einspruch, Klage, Revision, Beschwerde)
- Antraegen auf Aussetzung der Vollziehung (§ 361 AO, § 69 FGO)
- Entgegennahme von Bescheiden und Schriftstuecken (§ 122 Abs. 1 S. 4 AO)
- Verhandlungsfuehrung mit dem Finanzamt und Vereinbarungen tatsaechlicher Verstaendigung

[ORT, DATUM] [UNTERSCHRIFT]
```

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 6. `fa-stu-onboarding-rechtsbehelfssystematik`

**Fokus:** Vollstaendige Uebersicht aller steuerlichen Rechtsbehelfe — auf welcher Stufe welcher Rechtsbehelf zustaendig ist welche Frist gilt und welche Zwischenanordnungen verfuegbar sind. Anwendungsfall Berater muss bei Mandatsannahme strategisch entscheiden welche Verfahrenswege offen sind und welche Erfolgsaussicht sie haben. Behandelt Einspruch Klage Revision Nichtzulassungsbeschwerde Anhoerungsruege Verfassungsbeschwerde Vorlage an EuGH AdV einstweiliger Rechtsschutz. Output Entscheidungsbaum mit Wegweiser. Abgrenzung zu anw-einspruch-finanzamt fa-stu-finanzgerichtsklage-78-fgo und anw-aussetzung-vollziehung.

# Rechtsbehelfe im Steuerrecht — Systematik vom Einspruch bis zur Verfassungsbeschwerde

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsbehelfe im Steuerrecht — Systematik vom Einspruch bis zur Verfassungsbeschwerde` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Liegt ein Verwaltungsakt vor — sonst kein Einspruch sondern Untaetigkeitseinspruch § 347 Abs. 1 S. 2 AO?
2. Ist die Einspruchsfrist abgelaufen — pruefen ob Wiedereinsetzung oder schlichte Aenderung § 172 AO?
3. Gibt es eine Einspruchsentscheidung — dann nur noch Klage § 47 FGO offen?
4. Ist die Sache von grundsaetzlicher Bedeutung — Sprungklage § 45 FGO oder Musterverfahren § 363 Abs. 2 AO ueberlegen?
5. Steht eine Verfassungsfrage im Raum — Vorlage § 100 GG oder Verfassungsbeschwerde nach Erschoepfung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§§ 347 ff. AO** — Einspruchsverfahren.
- **§ 45 FGO** — Sprungklage ohne Vorverfahren bei Zustimmung des FA.
- **§ 46 FGO** — Untaetigkeitsklage nach sechs Monaten.
- **§ 47 FGO** — Klagefrist ein Monat.
- **§§ 115 116 FGO** — Revision Nichtzulassungsbeschwerde.
- **§ 133a FGO** — Anhoerungsruege.
- **§§ 100 GG** — Konkrete Normenkontrolle.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§§ 347 ff. AO · § 363 AO · § 45 FGO · § 46 FGO · § 47 FGO · § 69 FGO · § 115 FGO · § 116 FGO · § 120 FGO · § 133a FGO · § 90 BVerfGG · Art. 100 GG · Art. 267 AEUV

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 7. `fa-stu-onboarding-verwaltungsanweisungen`

**Fokus:** Methodik zur Nutzung und Abgrenzung von Verwaltungsanweisungen im Steuerrecht — BMF-Schreiben Anwendungserlass zur AO Umsatzsteuer-Anwendungserlass Einkommen- und Koerperschaftsteuer-Richtlinien Erbschaftsteuer-Hinweise. Anwendungsfall Berater muss entscheiden ob ein BMF-Schreiben fuer Mandant guenstig ist und ob er sich dem Finanzamt gegenueber darauf berufen kann. Behandelt Bindungswirkung Selbstbindung der Verwaltung Art. 3 GG Vertrauensschutz und prozessuale Verwertbarkeit. Output Argumentationsraster und Zitierhilfe. Abgrenzung zu fa-stu-onboarding-beratungsstruktur und fa-stu-onboarding-bescheid-lesen.

# BMF-Schreiben AEAO UStAE EStR — Verwaltungsanweisungen richtig nutzen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `BMF-Schreiben AEAO UStAE EStR — Verwaltungsanweisungen richtig nutzen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Was ist die Quelle: Gesetz Richtlinie Erlass oder bloss Verfuegung einer OFD?
2. Bindet die Anweisung nur die Verwaltung oder hat sie aussenwirksame Selbstbindung?
3. Hat das BMF-Schreiben einen Anwendungszeitraum und Uebergangsregelung?
4. Wuerde die Berufung auf das Schreiben dem Mandanten nuetzen oder schaden?
5. Hat die Rechtsprechung bereits inhaltlich abweichend entschieden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **Art. 20 Abs. 3 GG** — Bindung der Verwaltung an Gesetz und Recht.
- **Art. 3 Abs. 1 GG** — Selbstbindung der Verwaltung; Vertrauensschutz bei stetiger Praxis.
- **§ 4 AO** — Begriff Gesetz; Richtlinien sind nicht Gesetz.
- **§ 89 AO** — Beratungs- und Auskunftspflicht der Finanzbehoerde; verbindliche Auskunft.
- **§ 204 ff. AO** — Verbindliche Zusage nach Aussenpruefung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

Art. 20 Abs. 3 GG · Art. 3 Abs. 1 GG · § 4 AO · § 89 AO · §§ 204 ff. AO · AEAO (Anwendungserlass zur AO) · UStAE · EStR · KStR · ErbStH

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 8. `fa-stu-onboarding-verzinsung`

**Fokus:** Systematik aller Steuerzinsen — Nachzahlungs- und Erstattungszinsen § 233a AO Hinterziehungszinsen § 235 AO Stundungs- und Aussetzungszinsen §§ 234 237 AO Saeumniszuschlaege § 240 AO und Zinssatzanpassung nach BVerfG-Vorgaben. Anwendungsfall Berater muss Zinsfolge eines Bescheids quantifizieren und pruefen ob Zinsen angreifbar sind. Behandelt Zinsbeginn Karenzzeit 15 Monate Zinslauf Zinsfestsetzung und Aenderungen nach § 233a Abs. 5 AO sowie Verfassungsmaessigkeit des Zinssatzes. Output Berechnungsschema und Argumentationsraster gegen Zinsbescheide. Abgrenzung zu anw-aussetzung-vollziehung.

# Steuerliche Verzinsung — § 233a AO Nachzahlungs- und Erstattungszinsen sowie Hinterziehungs- und Aussetzungszinsen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Steuerliche Verzinsung — § 233a AO Nachzahlungs- und Erstattungszinsen sowie Hinterziehungs- und Aussetzungszinsen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Welcher Zinstatbestand greift (§ 233a § 234 § 235 § 237 AO oder § 240 AO)?
2. Wann beginnt der Zinslauf — Karenzzeit 15 Monate nach Ablauf des Veranlagungszeitraums?
3. Ist der Zinssatz fuer den gesamten Zinslauf bereits an die BVerfG-Rechtsprechung angepasst (Zinslauf ab 1. Januar 2019: 1,8 Prozent jaehrlich)?
4. Liegen besondere Erlassgruende vor (§ 227 AO sachliche oder persoenliche Billigkeit)?
5. Sind die Zinsen Folge einer Hinterziehung — dann zwingend § 235 AO unabhaengig von der Aussetzung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 233a AO** — Verzinsung von Steuernachforderungen und Erstattungen.
- **§ 234 AO** — Stundungszinsen.
- **§ 235 AO** — Hinterziehungszinsen.
- **§ 237 AO** — Aussetzungszinsen.
- **§ 238 AO** — Hoehe und Berechnung der Zinsen.
- **§ 239 AO** — Festsetzung der Zinsen.
- **§ 240 AO** — Saeumniszuschlaege.
- **§ 227 AO** — Erlass aus Billigkeitsgruenden.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 233a AO · § 234 AO · § 235 AO · § 237 AO · § 238 AO · § 239 AO · § 240 AO · § 227 AO · Art. 3 GG (Zinssatz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 9. `fa-stu-quellensteuer-50a-estg`

**Fokus:** Praxisbearbeitung des Quellensteuerabzugs nach § 50a EStG — Tatbestaende Bemessungsgrundlage Abzugsverfahren Freistellungs- und Erstattungsverfahren. Anwendungsfall Inlaendischer Vergueterungsschuldner zahlt an einen beschraenkt Steuerpflichtigen (Kuenstler Sportler Aufsichtsrat Lizenzen) und muss Steuer einbehalten. Behandelt Schuldner Glaeubiger Bemessungsgrundlage Bruttoabzug 15 Prozent bzw. 30 Prozent Erstattung nach § 50c EStG und DBA-Bezug. Output Pruefraster und Antragsmuster Freistellungsbescheinigung. Abgrenzung zu fa-stu-doppelbesteuerung-musterabkommen-oecd.

# Quellensteuer bei beschraenkter Steuerpflicht — § 50a EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Quellensteuer bei beschraenkter Steuerpflicht — § 50a EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Ist der Glaeubiger der Verguetung beschraenkt steuerpflichtig nach § 49 EStG?
2. Faellt die Verguetung unter § 50a Abs. 1 EStG (Darbietungen Verwertung Lizenz Aufsichtsrat)?
3. Ist Bruttoabzug einschlaegig oder kann Nettoabzug 30 Prozent gewaehlt werden?
4. Liegt eine Freistellungsbescheinigung BZSt vor — wenn nicht kann sie nachtraeglich beantragt werden?
5. Greift ein DBA mit Erstattungsanspruch nach § 50c EStG?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 50a EStG** — Steuerabzug bei beschraenkt Steuerpflichtigen.
- **§ 49 EStG** — inlaendische Einkuenfte.
- **§ 50c EStG** — Erstattungsverfahren beim BZSt.
- **§ 73c EStDV** — Verfahrensvorschriften.
- **OECD-MA Art. 12** — Lizenzgebuehren.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 50a EStG · § 49 EStG · § 50c EStG · § 50d EStG · § 73c EStDV · OECD-MA Art. 12

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.
