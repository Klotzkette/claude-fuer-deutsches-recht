---
name: rechtsabteilung-fa-stu-tatsaechliche
description: "Rechtsabteilung FA STU Tatsaechliche: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsabteilung FA STU Tatsaechliche

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Rechtsabteilung FA STU Tatsaechliche** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fa-stu-finanzgerichtsklage-78-fgo` | Strukturierter Aufbau einer Finanzgerichtsklage von der Klagefrist § 47 FGO ueber den Klageantrag und die Begruendung bis zur Akteneinsicht § 78 FGO. Anwendungsfall Einspruchsentscheidung ist ergangen Mandant will klagen — der Skill liefert Klageschrift Klageziel und Begruendungsstrategie. Behandelt Anfechtungsklage Verpflichtungsklage und Feststellungsklage Streitwert nach § 52 GKG und Streitgegenstand. Output Klageschriftmuster und Pruefraster fuer Begruendung. Abgrenzung zu anw-einspruch-finanzamt (Einspruchsstufe). |
| `fa-stu-tatsaechliche-verstaendigung` | Strategischer Skill zur tatsaechlichen Verstaendigung mit dem Finanzamt — wann ist sie zulaessig wie wird sie verhandelt und wie bindet sie. Anwendungsfall Aussenpruefung oder Veranlagung erreicht eine Sachverhaltsfrage die im Schaetzungswege nicht weiter aufklaerbar ist. Behandelt zulaessige Gegenstaende (Tatsachen nicht Recht) Beteiligte Mitwirkungspflicht und Bindungswirkung. Output Mustererklaerung Tatsaechliche Verstaendigung mit Protokoll. Abgrenzung zu fa-stu-onboarding-bescheid-lesen. |
| `rechtsabteilung-dac7-und-plattformreporting` | Rechtsabteilungs-Fachmodul für DAC7 und Plattformreporting: Plattformbetreiber prüfen Meldepflicht, Verkäuferdaten und Korrekturprozesse. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `rechtsabteilung-organschaft-nach-eugh-bfh-update` | Rechtsabteilungs-Fachmodul für Organschaft nach EuGH/BFH-Update: Organträger, Eingliederung und Haftung werden für Konzernrechtsabteilungen geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `rechtsabteilung-transfer-pricing-bei-ip-und-softwarelizenzen` | Rechtsabteilungs-Fachmodul für Transfer Pricing bei IP- und Softwarelizenzen: Intercompany-Lizenzen werden mit DEMPE, Benchmark und Dokumentation geführt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `rechtsabteilung-vga-bei-geschaeftsfuehrer-und-beiratsverguetung` | Rechtsabteilungs-Fachmodul für vGA bei Geschäftsführer- und Beiratsvergütung: Vergütung, Rückwirkung, Dokumentation und Fremdvergleich werden geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |
| `stb-addison-bwa-konfiguration-tipps` | Addison BWA-Konfiguration. Anwendungsfall Kanzleien mit Wolters Kluwer Addison statt DATEV. Methodik Unterschiede zu DATEV Konten-Konfiguration Branchenanpassung. Output BWA in Addison. |
| `stb-belegtransfer-datev-unternehmen-online` | Belegtransfer DATEV Unternehmen Online. Anwendungsfall systematischer Belegfluss Mandant zu StB Beleg-Scan App Mailpostfach Bank-Anbindung. Methodik Konfiguration Workflow. Output Belegfluss-Standard. |
| `stb-buchhaltungsbutler-mandantencloud` | BuchhaltungsButler und vergleichbare Cloud-Buchhaltung beim Mandanten. Anwendungsfall Mandant arbeitet mit BuchhaltungsButler sevDesk Lexware Office Candis StB-Schnittstelle DATEV-Export Datenqualitaetsprüfung AVV. Methodik Konfiguration BelegGoBD-Risiken Honoraranpassung. Output eingerichtete Cloud-Schnittstelle und Prüfroutine. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Rechtsabteilung FA STU Tatsaechliche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fa-stu-finanzgerichtsklage-78-fgo`

**Fokus:** Strukturierter Aufbau einer Finanzgerichtsklage von der Klagefrist § 47 FGO ueber den Klageantrag und die Begruendung bis zur Akteneinsicht § 78 FGO. Anwendungsfall Einspruchsentscheidung ist ergangen Mandant will klagen — der Skill liefert Klageschrift Klageziel und Begruendungsstrategie. Behandelt Anfechtungsklage Verpflichtungsklage und Feststellungsklage Streitwert nach § 52 GKG und Streitgegenstand. Output Klageschriftmuster und Pruefraster fuer Begruendung. Abgrenzung zu anw-einspruch-finanzamt (Einspruchsstufe).

# Finanzgerichtsklage — Aufbau Frist und Akteneinsicht § 78 FGO

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Finanzgerichtsklage — Aufbau Frist und Akteneinsicht § 78 FGO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Liegt eine Einspruchsentscheidung vor oder ist Sprungklage § 45 FGO moeglich?
2. Ist die Klagefrist von einem Monat § 47 FGO eingehalten?
3. Welcher Klagetyp passt — Anfechtung Verpflichtung Feststellung?
4. Wie ist der Streitgegenstand zu bestimmen und welcher Streitwert ergibt sich nach § 52 GKG?
5. Ist AdV § 69 FGO parallel zu beantragen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 40 FGO** — Klagearten.
- **§ 44 FGO** — Vorverfahren.
- **§ 45 FGO** — Sprungklage.
- **§ 46 FGO** — Untaetigkeitsklage.
- **§ 47 FGO** — Klagefrist.
- **§ 64 FGO** — Klageschrift Form und Inhalt.
- **§ 65 FGO** — Inhalt der Klage.
- **§ 69 FGO** — Aussetzung der Vollziehung.
- **§ 78 FGO** — Akteneinsicht.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§§ 40 ff. FGO · § 47 FGO · § 64 FGO · § 65 FGO · § 69 FGO · § 78 FGO · § 96 FGO (Beweiswuerdigung) · § 52 GKG (Streitwert)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Praxisformulierung / Antragsmuster

```
An das Finanzgericht [BUNDESLAND]
[ADRESSE]

Klage
des [MANDANT], vertreten durch [KANZLEI],
 - Klaeger -
gegen das Land [BUNDESLAND], vertreten durch das Finanzamt [ORT],
 - Beklagter -

wegen [STEUERART] [JAHR] (Einspruchsentscheidung vom [DATUM], Az. [NR])

Streitwert: [WERT]

Klageantrag: Der [STEUERART]-Bescheid vom [DATUM] in Gestalt der Einspruchsentscheidung vom [DATUM] wird aufgehoben. Die Steuer wird auf [BETRAG] herabgesetzt.

Begruendung:
I. Sachverhalt: [...]
II. Anwendbare Normen: [...]
III. Rechtliche Wuerdigung: [...]

Antrag auf Akteneinsicht § 78 FGO wird gestellt.
Antrag auf Aussetzung der Vollziehung § 69 FGO wird gestellt.

[ORT, DATUM] [UNTERSCHRIFT RA]
```

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 2. `fa-stu-tatsaechliche-verstaendigung`

**Fokus:** Strategischer Skill zur tatsaechlichen Verstaendigung mit dem Finanzamt — wann ist sie zulaessig wie wird sie verhandelt und wie bindet sie. Anwendungsfall Aussenpruefung oder Veranlagung erreicht eine Sachverhaltsfrage die im Schaetzungswege nicht weiter aufklaerbar ist. Behandelt zulaessige Gegenstaende (Tatsachen nicht Recht) Beteiligte Mitwirkungspflicht und Bindungswirkung. Output Mustererklaerung Tatsaechliche Verstaendigung mit Protokoll. Abgrenzung zu fa-stu-onboarding-bescheid-lesen.

# Tatsaechliche Verstaendigung mit dem Finanzamt — Voraussetzungen und Vertragsmuster

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Tatsaechliche Verstaendigung mit dem Finanzamt — Voraussetzungen und Vertragsmuster` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Geht es um Tatsachen die nicht weiter aufklaerbar sind — sonst keine tatsaechliche Verstaendigung zulaessig?
2. Wer ist auf Behoerdenseite zustaendig (Sachgebietsleiter oder Vorsteher)?
3. Ist die Mandantenposition rechtlich durchsetzbar oder Schaetzungsrisiko hoch?
4. Soll die Verstaendigung mit oder ohne Vorbehalt der Nachpruefung getroffen werden?
5. Welche Folgewirkung auf USt EStG GewSt KSt und auf Folgejahre wird vereinbart?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 88 AO** — Untersuchungsgrundsatz; bei Unaufklaerbarkeit Schaetzung § 162 AO.
- **§ 162 AO** — Schaetzung von Besteuerungsgrundlagen.
- **§ 201 AO** — Schlussbesprechung; haeufig Vehikel der Verstaendigung.
- **§ 204 AO** — verbindliche Zusage; rechtsverbindliche Auspraegung.
- **Bindungswirkung** — entwickelt durch Rechtsprechung; nur ueber gravierende Aenderungen aufhebbar.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 88 AO · § 162 AO · § 201 AO · § 204 AO · § 88a AO (Sammlung von Daten) · Treu und Glauben (allgemeiner Verfahrensgrundsatz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Praxisformulierung / Antragsmuster

```
TATSAECHLICHE VERSTAENDIGUNG
ueber die Besteuerungsgrundlagen [STEUERART] [JAHRE]

Zwischen Finanzamt [ORT] - Sachgebietsleiter [NAME] - und Steuerpflichtigem [NAME], vertreten durch [KANZLEI]:

1. Sachverhalt: [...]
2. Tatsachenproblem: [unaufklaerbares Element].
3. Verstaendigung: Die Beteiligten erkennen folgende Tatsachen einvernehmlich an: [...]
4. Steuerliche Folgen: [USt EStG KSt GewSt - jeweils Betrag/Periode].
5. Bindung: Die Verstaendigung bindet beide Seiten; sie umfasst nicht die rechtliche Wuerdigung.
6. Vorbehalt der Nachpruefung wird [aufgehoben/aufrechterhalten].

Ort, Datum [FA] [Mandant] [Berater]
```

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 3. `rechtsabteilung-dac7-und-plattformreporting`

**Fokus:** Rechtsabteilungs-Fachmodul für DAC7 und Plattformreporting: Plattformbetreiber prüfen Meldepflicht, Verkäuferdaten und Korrekturprozesse. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: DAC7 und Plattformreporting

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsabteilung: DAC7 und Plattformreporting` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialkern: Rechtsabteilung: DAC7 und Plattformreporting

- **Konkretes Problem:** Plattformbetreiber prüfen Meldepflicht, Verkäuferdaten und Korrekturprozesse.
- **Norm-/Quellenanker:** AO, EStG, KStG, GewStG, UStG, GrEStG, AStG, UmwStG, DBA/OECD-MC und BMF/BFH nur verifiziert.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

PStTG, AO, DAC7; Datenschutzschnittstelle

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Plattformbetreiber prüfen Meldepflicht, Verkäuferdaten und Korrekturprozesse.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.

## 4. `rechtsabteilung-organschaft-nach-eugh-bfh-update`

**Fokus:** Rechtsabteilungs-Fachmodul für Organschaft nach EuGH/BFH-Update: Organträger, Eingliederung und Haftung werden für Konzernrechtsabteilungen geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: Organschaft nach EuGH/BFH-Update

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsabteilung: Organschaft nach EuGH/BFH-Update` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialkern: Rechtsabteilung: Organschaft nach EuGH/BFH-Update

- **Konkretes Problem:** Organträger, Eingliederung und Haftung werden für Konzernrechtsabteilungen geprüft.
- **Norm-/Quellenanker:** AO, EStG, KStG, GewStG, UStG, GrEStG, AStG, UmwStG, DBA/OECD-MC und BMF/BFH nur verifiziert.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

UStG § 2; MwStSystRL; EuGH/BFH-Linie live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Organträger, Eingliederung und Haftung werden für Konzernrechtsabteilungen geprüft.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.

## 5. `rechtsabteilung-transfer-pricing-bei-ip-und-softwarelizenzen`

**Fokus:** Rechtsabteilungs-Fachmodul für Transfer Pricing bei IP- und Softwarelizenzen: Intercompany-Lizenzen werden mit DEMPE, Benchmark und Dokumentation geführt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: Transfer Pricing bei IP- und Softwarelizenzen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsabteilung: Transfer Pricing bei IP- und Softwarelizenzen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialkern: Rechtsabteilung: Transfer Pricing bei IP- und Softwarelizenzen

- **Konkretes Problem:** Intercompany-Lizenzen werden mit DEMPE, Benchmark und Dokumentation geführt.
- **Norm-/Quellenanker:** AO, EStG, KStG, GewStG, UStG, GrEStG, AStG, UmwStG, DBA/OECD-MC und BMF/BFH nur verifiziert.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

AO § 1 AStG; OECD-Verrechnungspreise; Lizenzschranke live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Intercompany-Lizenzen werden mit DEMPE, Benchmark und Dokumentation geführt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.

## 6. `rechtsabteilung-vga-bei-geschaeftsfuehrer-und-beiratsverguetung`

**Fokus:** Rechtsabteilungs-Fachmodul für vGA bei Geschäftsführer- und Beiratsvergütung: Vergütung, Rückwirkung, Dokumentation und Fremdvergleich werden geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: vGA bei Geschäftsführer- und Beiratsvergütung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsabteilung: vGA bei Geschäftsführer- und Beiratsvergütung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialkern: Rechtsabteilung: vGA bei Geschäftsführer- und Beiratsvergütung

- **Konkretes Problem:** Vergütung, Rückwirkung, Dokumentation und Fremdvergleich werden geprüft.
- **Norm-/Quellenanker:** AO, EStG, KStG, GewStG, UStG, GrEStG, AStG, UmwStG, DBA/OECD-MC und BMF/BFH nur verifiziert.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

KStG § 8 Abs. 3; EStG; BFH-Linie live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Vergütung, Rückwirkung, Dokumentation und Fremdvergleich werden geprüft.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.

## 7. `stb-addison-bwa-konfiguration-tipps`

**Fokus:** Addison BWA-Konfiguration. Anwendungsfall Kanzleien mit Wolters Kluwer Addison statt DATEV. Methodik Unterschiede zu DATEV Konten-Konfiguration Branchenanpassung. Output BWA in Addison.

# Addison BWA-Konfiguration

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Addison BWA-Konfiguration` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Addison (Wolters Kluwer) ist die zweitstaerkste StB-Kanzleisoftware in Deutschland. Funktionen vergleichbar mit DATEV: Buchfuehrung, BWA, Lohn, Jahresabschluss. Andere Bedienlogik und andere Standardforms. Steuerberater, die mit Addison arbeiten, brauchen aequivalente Praxis-Tipps.

## Kaltstart-Rueckfragen

1. Welche Addison-Version (jaehrliche Updates)?
2. Welche Module (Finanzbuchhaltung, Lohn, Jahresabschluss)?
3. Welche Standard-Form fuer Mandanten?
4. Welche Branchen-Konfiguration?
5. Welche individuellen Anpassungen?
6. Welche Schnittstellen aktiv (eRechnung, Bank)?
7. Welche Berater-Sicht-Konfiguration?
8. Welche Schulungsstand der Sachbearbeiter?

## Workflow

### Phase 1 — Standardformen

| Addison-Bezeichnung | DATEV-Aequivalent | Verwendung |
|---|---|---|
| Standard-BWA / Kurz-BWA | DATEV BWA 01 | Standard 90 % der Mandate |
| Bewegungs-BWA | DATEV BWA 11 | Detaillierter Vormonatsvergleich |
| Branchen-BWA | DATEV BWA 21 | Mit Branchenkennzahlen |
| Liquiditaets-BWA | DATEV BWA 41 | Cashflow-orientiert |
| Kostenstellen-BWA | DATEV BWA 31 | Bei Kostenstellenrechnung |

Hinweis: konkrete Form-Nummern und Bezeichnungen variieren mit der Addison-Version; aktuellen Stand in der Programmdokumentation pruefen.

### Phase 2 — Konten-Konfiguration

- Kontenrahmen SKR 03 / SKR 04 wie in DATEV; alternativ branchenspezifische Rahmen (z.B. SKR 14 Landwirtschaft, IKR fuer Industrieunternehmen).
- BWA-Konten-Zuordnung ueber Berater-Stammdaten (typischer Pfad `Stammdaten → BWA-Konfiguration → Konten-Zuordnung`; konkreter Menue-Pfad variiert je Addison-Version — im Zweifelsfall in der Programm-Onlinehilfe unter "BWA-Konfiguration" nachschlagen).
- Bei individuellen Konten manuelle Zuordnung zur BWA-Zeile vor erstem Lauf.

### Phase 3 — Periodenvergleich

- Vorjahresdaten werden bei vorhandener Buchhaltungs-Historie automatisch herangezogen.
- Planwerte ueber das Plan-Erfassungs-Modul (jaehrlich/monatlich) erfassen; Plan-Ist-Vergleich in der BWA aktivieren.
- Mehrjahresvergleich bis 5 Jahre zurueck moeglich.

### Phase 4 — Branchenvergleich

- Wolters Kluwer Branchenberichte als Alternative zu DATEV BBE-Branchenberichten.
- Branchenschluessel (WZ-Code) im Mandantenstamm hinterlegen.
- Aktualitaet der Branchendaten pruefen — typischerweise jaehrliche Aktualisierung.

### Phase 5 — Ausgabe

- PDF-Export mit Mandanten-Briefkopf.
- Excel-Export fuer Detailauswertung (Pivot-tauglich).
- Mandantenportal "Wolters Kluwer Mandanten-Cockpit" als Pendant zu DATEV Unternehmen Online.

### Phase 6 — Updates

- Jaehrliche Programm-Updates zum 1. Januar (Lohnsteuer-, SV-Tabellen, USt-Aenderungen, AfA-Tabellen).
- Bei groesseren Reformen unterjaehrige Updates (z.B. Wachstumschancengesetz, eRechnung).
- Update-Pflicht aus § 146 AO (Programm muss aktuelle Tabellen abbilden).

## Output

- Konfigurierte Addison-BWA.

## Strategie und Praxis-Tipps

- Addison-Schulungen ueber Wolters Kluwer Akademie.
- Wechsel von DATEV zu Addison oder umgekehrt sorgfaeltig planen — Mandantenmigration aufwendig.
- Hybrid-Modelle (z.B. Lohn Addison, Buchhaltung DATEV) sind selten und teuer.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV Pendant.
- `stb-sage-buchhalter-bwa-konfiguration` — Sage.

## Quellen und Updates

Stand: 05/2026.

- Wolters Kluwer Addison Programm- und Bedienungsdokumentation (aktuelle Version pruefen).
- Wolters Kluwer Branchenberichte als Vergleichsdatenbank.
- Verifikations-Hinweis: konkrete Programmpfade und Form-Nummern ggf. abweichend in aktueller Addison-Version.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (Programmpfad-Hinweis ohne Marker neu formuliert) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-belegtransfer-datev-unternehmen-online`

**Fokus:** Belegtransfer DATEV Unternehmen Online. Anwendungsfall systematischer Belegfluss Mandant zu StB Beleg-Scan App Mailpostfach Bank-Anbindung. Methodik Konfiguration Workflow. Output Belegfluss-Standard.

# Belegtransfer ueber DATEV Unternehmen Online

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Belegtransfer ueber DATEV Unternehmen Online` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

DATEV Unternehmen Online (DUO) ist die Standardplattform fuer Belegtransfer zwischen Mandant und StB. Mandant erfasst Belege ueber Smartphone-App, Scanner oder Mailpostfach; StB greift in DATEV Kanzlei-Rechnungswesen direkt zu. Dieser Skill konkretisiert den Belegfluss und die Standard-Workflow-Konfiguration.

## Kaltstart-Rueckfragen

1. Welche Mandanten arbeiten bereits mit DUO?
2. Welche Belegart wird transferiert?
3. Welche Erfassungs-Kanaele (App, Mail, Scanner)?
4. Welche OCR-Qualitaet erforderlich?
5. Welche Bank-Anbindung?
6. Welche eRechnung-Empfaenger?
7. Welche Mandantenfreigabe-Workflow?
8. Welche Archivierung GoBD-konform?

## Workflow

### Phase 1 — Belegerfassung

| Kanal | Anwendung |
|---|---|
| DATEV Upload Online (Mobile App) | Belege per Smartphone scannen |
| Mailpostfach | E-Mail-Rechnungen direkt an DUO-Postfach |
| Scanner | Buero-Scanner mit Standard-PDF |
| eRechnung | XRechnung/ZUGFeRD direkt empfangen |
| Bank-Online | PSD2-Anbindung; Bankbewegungen automatisch |

### Phase 2 — OCR und Beleg-Klassifizierung

- OCR-Erkennung des Beleg-Inhalts (Lieferant, Betrag, Datum, USt).
- Automatische Klassifizierung in DATEV-Konten-Vorschlag.
- Mandantenfreigabe oder direkte Verbuchung.

### Phase 3 — Buchungs-Vorschlag

- DATEV "Belege Online" / Belegcockpit zeigt Beleg-Bild und Buchungsvorschlag (Konto, USt-Schluessel, Buchungstext) nebeneinander an.
- Sachbearbeiter prueft den Vorschlag, korrigiert ggf. die Kontierung und gibt frei.
- Bei manueller Klaerung wird die Mandantenanfrage ueber das DUO-Postfach gestellt (revisionssichere Dokumentation).
- Konkrete Menue-Pfade in der aktuellen DATEV-Programmversion ggf. abweichend.

### Phase 4 — Bank-Anbindung

- Bank-Online ueber PSD2.
- Bankbewegungen automatisch.
- Zuordnung zu Belegen ueber Verwendungszweck.

### Phase 5 — eRechnungs-Empfang

- DUO mit eRechnungs-Postfach.
- XRechnung/ZUGFeRD-Auswertung.
- Automatische Verbuchung moeglich.

### Phase 6 — Archivierung

- GoBD-konform im Originalformat.
- 10 Jahre Aufbewahrung.
- Belege im Mandanten-Online-Postfach.

## Output

- Konfigurierter Belegfluss DUO.
- Buchungen mit Belegverknuepfung.
- GoBD-konforme Archivierung.

## Strategie und Praxis-Tipps

- DUO + DATEV Upload Online = Killer-Kombination fuer effizienten Belegfluss.
- OCR-Qualitaet variabel — Kontrolle durch Sachbearbeiter bleibt Pflicht.
- Bei vielen kleinen Belegen: Mandant taeglich scannen, Sachbearbeiter woechentlich pruefen.
- Bei eRechnungs-Empfang: Automatisierung Hebel.
- DATEV-Tipp: DATEV Upload Online mit GoBD-konformer Mandanten-Schulung.

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-erechnung-pflicht-b2b-2025-2026` — eRechnung.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 146, 147.
- BMF v. 28.11.2019 zu GoBD.
- DATEV Unternehmen Online und "Belege Online" Dokumentation (aktuelle Version pruefen).
- Verifikations-Hinweis: konkrete Programmpfade und Modul-Bezeichnungen ggf. abweichend in aktueller DATEV-Version.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-buchhaltungsbutler-mandantencloud`

**Fokus:** BuchhaltungsButler und vergleichbare Cloud-Buchhaltung beim Mandanten. Anwendungsfall Mandant arbeitet mit BuchhaltungsButler sevDesk Lexware Office Candis StB-Schnittstelle DATEV-Export Datenqualitaetsprüfung AVV. Methodik Konfiguration BelegGoBD-Risiken Honoraranpassung. Output eingerichtete Cloud-Schnittstelle und Prüfroutine.

# BuchhaltungsButler — Mandanten-Cloud-Loesung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `BuchhaltungsButler — Mandanten-Cloud-Loesung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

BuchhaltungsButler (auch sevDesk, Lexware-Office, Billbee, Candis) sind Cloud-Buchhaltungsloesungen fuer Mandanten, die ihre Buchfuehrung weitgehend selbst betreiben. Sie bieten Beleg-Scan, Bank-Abruf, automatische Buchungs-Vorschlaege. Der Steuerberater erhaelt Daten ueber DATEV-Export oder andere Schnittstellen. Vorteil: Mandant traegt einen Teil der Arbeit; Nachteil: Daten-Qualitaet variabel.

## Kaltstart-Rueckfragen

1. Welche Cloud-Loesung verwendet der Mandant?
2. Welche Schnittstellen zu DATEV existieren?
3. Wer bucht — Mandant, StB, automatisch?
4. Welche Datenqualitaet wird geliefert?
5. Welche Pflichten des Mandanten (Buchungs-Kontrolle, GoBD-Konformitaet)?
6. Welche AVV mit Cloud-Anbieter?
7. Welche Sicherheits-Vorkehrungen?
8. Welche Mandanten-Schulungsstand?

## Workflow

### Phase 1 — System-Wahl

| Tool | Geeignet fuer |
|---|---|
| BuchhaltungsButler | KMU mit hohem Belegaufkommen |
| sevDesk | Solo-Selbstaendige, Kleinunternehmer |
| Lexware-Office | Kleinmandanten, Klein-GmbH |
| Candis | Mittelstand mit Beleg-|
| Datev DUO | StB-Mandanten (Standard) |

### Phase 2 — Schnittstelle zu DATEV

- DATEV-Buchungsstapel-Export aus der Cloud im DATEV-CSV-Format (sog. "ASCII-Format" bzw. neuer "Belege Online"-Schnittstelle).
- Import in DATEV Kanzlei-Rechnungswesen ueber `Datei → Datenuebernahme → Buchungsstapel` (konkrete Programmpfade in der aktuellen DATEV-Programmversion ggf. abweichend).
- Plausibilitaetspruefung der Buchungen (Konten-Mapping, USt-Schluessel, Belegverknuepfung).

### Phase 3 — Mandanten-Setup

- Mandant erhaelt Cloud-Konto.
- StB-Lese-Zugang.
- Belegfestlegen.

### Phase 4 — Buchungsfreigabe

- Mandant bucht (oder Cloud schlaegt vor).
- StB prueft und freigibt.
- Bei Fehlern Korrektur.

### Phase 5 — Auswertung

- BWA aus DATEV oder direkt aus Cloud.
- Bei Cloud-BWA: in der Regel nicht GoBD-Standard.
- StB-BWA aus DATEV bleibt verbindlich.

### Phase 6 — DSGVO

- AVV mit Cloud-Anbieter zwingend.
- Daten-Hosting in EU.
- Backup-Strategie.

## Output

- Cloud-Konto eingerichtet.
- Schnittstelle zu DATEV.
- Mandant geschult.

## Strategie und Praxis-Tipps

- Cloud-Tools sind Effizienzhebel, wenn Mandant disziplinarisch arbeitet.
- Datenqualitaet schwankend — StB-Pruefung bleibt Pflicht.
- DSGVO-Compliance staendig pruefen.
- Honorar oft niedriger bei Cloud-betreibenden Mandanten (Buchungs-Anteil reduziert).
- StBVV: Honorarmodell anpassen (Pauschal niedriger, Pruefung Stunden).

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-datentransfer-mandant-cloud-dsgvo` — DSGVO im Datenverkehr.

## Quellen und Updates

Stand: 05/2026.

- BuchhaltungsButler, sevDesk, Lexware Dokumentation.
- DSGVO Art. 28.
- BMF v. 28.11.2019 zu GoBD.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
