---
name: anhoerung-verkehrsowi-einspruch-messverfahren
description: "Anhoerung Verkehrsowi Einspruch Messverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anhoerung Verkehrsowi Einspruch Messverfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anhoerung Verkehrsowi Einspruch Messverfahren** im Plugin Verkehrs-OWi-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-anhoerung-fristen-form-und-zustaendigkeit` | Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `verkehrsowi-fristen-einspruch` | Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), § 74 OWiG (Verwerfung bei Versaeumnis). Prüfraster: Zustellungsdatum und -art, Fristberechnung, Beschraenkter Einspruch § 67 Abs. 2 OWiG (nur Fahrverbot). Output Fristenblatt, Einspruchs-Template, ggf. Wiedereinsetzungsantrag. Abgrenzung: Inhalt des Einspruchs siehe verkehrsowi-beweisverwertung-standardisiert; Rechtsbeschwerde siehe verkehrsowi-rechtsbeschwerde. |
| `verkehrsowi-messverfahren-geschwindigkeit` | Prüffeld für verkehrsowi messverfahren geschwindigkeit: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Verkehrs-OWi-Verteidigung gilt für **Anhoerung Verkehrsowi Einspruch Messverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-anhoerung-fristen-form-und-zustaendigkeit`

**Fokus:** Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg / anhoerung fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** OWiG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Anhoerung** prüfen.
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

## Qualitätsanker: Messdaten, Messakte und faires Verfahren

- **Verifizierter Leitanker:** BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Verfahren zugänglich sein, wenn sie konkret und rechtzeitig verlangt werden.
- **Praktische Übersetzung:** Niemals nur pauschal „Messung bestreiten“. Immer präzise anfordern: Falldatei/Rohmessdaten, Messreihe soweit vorhanden und relevant, Token/Passwort, Eichschein, Gebrauchsanweisung, Schulungsnachweise, Wartungs-/Reparaturhinweise, Standort-/Beschilderungsunterlagen, Statistik und Auswerteprotokoll.
- **Angriffslinie:** Standardisiertes Messverfahren ist eine Beweiserleichterung, kein Denkverbot. Der Skill muss aus Unterlagen konkrete Einwendungen machen: falsches Gerät, fehlende Eichung, fehlerhafte Bedienung, unklare Fahreridentität, unplausible Messreihe, fehlende Einsicht, Frist-/Gehörsproblem.
- **Output-Pflicht:** Immer ein kurzes Anforderungsschreiben oder einen gerichtsfesten Begründungsbaustein anbieten, wenn Akteneinsicht, Messunterlagen oder Fristwahrung Thema sind.

## 2. `verkehrsowi-fristen-einspruch`

**Fokus:** Einspruchsfrist im OWi-Verfahren berechnen und wahren: Drohende Rechtsbestandskraft des Bußgeldbescheids. Normen: § 67 OWiG (Einspruch 2 Wochen ab Zustellung), §§ 33 OWiG, 177-182 ZPO (Zustellungsfiktion), § 52 OWiG (Wiedereinsetzung), § 74 OWiG (Verwerfung bei Versaeumnis). Prüfraster: Zustellungsdatum und -art, Fristberechnung, Beschraenkter Einspruch § 67 Abs. 2 OWiG (nur Fahrverbot). Output Fristenblatt, Einspruchs-Template, ggf. Wiedereinsetzungsantrag. Abgrenzung: Inhalt des Einspruchs siehe verkehrsowi-beweisverwertung-standardisiert; Rechtsbeschwerde siehe verkehrsowi-rechtsbeschwerde.

# Einspruchsfrist und Einspruch — § 67 OWiG

## Triage zu Beginn

1. **Wann wurde der Bussgeldbescheid zugestellt?** — Ausgangspunkt der 2-Wochen-Frist § 67 Abs. 1 OWiG.
2. **Zustellungsform?** — Persoenliche Uebergabe, Einwurf-Einschreiben (§§ 33 OWiG, 180 ZPO), PZU.
3. **Mandant kennt Zugangsdatum?** — Falls unsicher: Zustellungsfiktion pruefen; fuer Mandanten spaetestes bekanntes Datum nehmen.
4. **Frist bereits abgelaufen?** — Wiedereinsetzungsantrag nach § 52 OWiG pruefen.
5. **Beschraenkt oder unbeschraenkt einlegen?** — § 67 Abs. 2 OWiG: Beschraenkung auf Rechtsfolgen moeglich.

## Zentrale Normen

- **§ 67 Abs. 1 OWiG** — Einspruch: 2 Wochen ab Zustellung des Bussgeldbescheids
- **§ 67 Abs. 2 OWiG** — Beschraenkter Einspruch auf Rechtsfolgen (Geldbusse, Fahrverbot)
- **§ 33 OWiG** — Zustellungsvorschriften: entsprechende Anwendung ZPO
- **§ 52 OWiG** — Wiedereinsetzung in den vorigen Stand nach § 44 StPO entsprechend
- **§ 74 OWiG** — Verwerfung des Einspruchs bei unentschuldigtem Ausbleiben
- **§ 28 OWiG** — Bekanntmachung des Bussgeldbescheids; Fristbeginn

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Fristen-Berechnungsschema

```
Zustellungsdatum: [DATUM]
+ 14 Tage: [DATUM + 14 Tage]
= Fristende: [DATUM]

Besonderheiten:
- Fristende Samstag/Sonntag/Feiertag → naechster Werktag (§ 43 StPO)
- Zustellungsfiktion § 180 ZPO: Einwurf-Einschreiben = 3 Tage nach Aufgabe
- Mandant im Urlaub/Krankenhaus → Wiedereinsetzungsgruende pruefen
```

## Entscheidungsbaum

```
Frist noch offen?
├─ Ja → Einspruch sofort formulieren und einlegen
│ ├─ Beschraenkt (nur Rechtsfolgen)? → § 67 Abs. 2 OWiG
│ └─ Unbeschraenkt → Standardvorgehen
└─ Nein (Frist abgelaufen)
 ├─ Kein Verschulden? → Wiedereinsetzung § 52 OWiG
 │ ├─ Krankheit, Urlaub, Fehler der Behoerde
 │ └─ Eidesstattliche Versicherung + gleichzeitiger Einspruch
 └─ Verschulden → Bussgeldbescheid rechtskraeftig; Vollstreckung abwenden
```

## Output-Template Einspruchsschreiben

```
An die [Bussgeldstelle] / Amtsgericht [ORT]
Az.: [AKTENZEICHEN]

Einspruch nach § 67 OWiG

Namens des Betroffenen [NAME] lege ich gegen den Bussgeldbescheid
vom [DATUM DES BESCHEIDS], zugegangen am [ZUSTELLUNGSDATUM],
form- und fristgerecht

Einspruch

ein.

[Falls beschraenkt: Der Einspruch wird auf die festgesetzten
Rechtsfolgen beschraenkt. § 67 Abs. 2 OWiG.]

Ich bitte um Uebersendung der vollstaendigen Verfahrensakte
einschliesslich Messakte.

Anlage: Vollmacht [NAME]

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Frist unmittelbar nach Mandatsuebernahme berechnen und im Kalender eintragen.
- 3-Tage-Vorlauffrist-Erinnerung setzen.
- Beschraenkter Einspruch nur nach Mandantenruecksprache.
- Anwaltliche Endkontrolle vor dem Versand.

## 3. `verkehrsowi-messverfahren-geschwindigkeit`

**Fokus:** Prüffeld für verkehrsowi messverfahren geschwindigkeit: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Geschwindigkeitsmessung OWi-Verfahren

## Triage zu Beginn — Sofortklaerung

1. **Messgeraet identifizieren:** Welches Geraet wurde eingesetzt? (ESO ES 3.0 / ProViDa / TraffiStar S350 / Riegl FG21-P / PoliScan Speed / Traffipax Traffistar S330) — beeinflusst Angriffsstrategie entscheidend.
2. **Toleranzabzug korrekt?** — PTB-Tabelle: Geschw. bis 100 km/h: 3 km/h Abzug; ab 100 km/h: 3% Abzug. Im Bescheid korrekt angewendet?
3. **Eichschein vorhanden und gueltig?** — Eichschein aus der Messakte anfordern; Eichgueltigkeit pruefen (Ablaufdatum); § 6 MessEG.
4. **Messprotokoll und Schulungsnachweis?** — Bedienungsanleitung beachtet? Beamter fuer dieses Geraet geschult?
5. **Rohmessdaten vorhanden und herausgegeben?** — Nach BVerfG hat Betroffener Recht auf Zugang zu Rohmessdaten; Verweigerung verletzt rechtliches Gehoer.

## Zentrale Normen

- **§ 24 StVG** — Ordnungswidrigkeitentatbestand Geschwindigkeitsueberschreitung
- **§ 49 StVO i.V.m. § 3 StVO** — Geschwindigkeitsvorschriften
- **§ 6 MessEG** — Eichpflicht fuer Messgeraete im Verkehr
- **§ 244 Abs. 2 StPO i.V.m. § 77 OWiG** — Amtsaufklaerungspflicht
- **§ 46 OWiG i.V.m. § 244 StPO** — Beweisantragsrecht im OWi-Verfahren
- **Art. 103 Abs. 1 GG** — Rechtliches Gehoer (Rohmessdaten-Recht)

## Aktuelle Rechtsprechung (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand Volltext aufrufen):

- **BVerfG, Beschl. v. 12.11.2020, 2 BvR 1616/18** — Recht des Betroffenen auf Zugang zu den nicht-zum-Aktenbestand gehörenden Messunterlagen (Rohmessdaten, Lebensakte etc.) als Ausfluss des fairen Verfahrens. Quelle: bundesverfassungsgericht.de
- **BVerfG, Beschl. v. 20.6.2023, 2 BvR 1167/20** — Keine Pflicht zur Speicherung von Rohmessdaten bei standardisiertem Messverfahren (Leivtec XV3); Recht auf erweiterten Zugang besteht aber im Einzelfall. Quelle: bundesverfassungsgericht.de
- BGH-Linie zum standardisierten Messverfahren: konkrete Aktenzeichen (Beschluesse BGH 4. Strafsenat) vor Versand in bundesgerichtshof.de oder dejure.org verifizieren.

Hinweis: Standardisiertes Messverfahren bringt Beweis-Erleichterung; konkrete Angriffspunkte (Eichung, Aufstellung, Mehrfachreflexion, Bedienfehler) müssen substantiiert vorgetragen werden.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Messverfahren-Angriffspunkte — Checkliste

```
EICHUNG:
□ Eichschein vorhanden (aus Messakte)?
□ Eichgueltigkeit zum Messzeitpunkt?
□ Geraet in Deutschland geeicht (PTB-Zulassung)?

AUFSTELLUNG / BEDIENUNG:
□ Standort wie in Bedienungsanleitung vorgeschrieben?
□ Mindestabstand zu Schildern / Kurven eingehalten?
□ Keine gegenueberliegenden Reflexionsflaechen?
□ Mehrfachbelegerung (zwei Fahrzeuge gleichzeitig im Messfeld)?

MESSFOTO / ZUORDNUNG:
□ Fahrzeug eindeutig identifizierbar?
□ Kennzeichen lesbar?
□ Nur ein Fahrzeug im relevanten Messbereich?
□ Fahrtrichtung korrekt?

SCHULUNG:
□ Messbeamter fuer dieses Geraet geschult?
□ Schulungsnachweis in der Akte?

ROHMESSDATEN:
□ Rohmessdaten angefordert?
□ Herausgegeben oder Weigerung begruendet?
□ Bei Weigerung: BVerfG 2020 zitieren, Verwertungsverbot ruegen
```

## Toleranzabzuege nach PTB-Richtlinie

| Gemessene Geschwindigkeit | Toleranzabzug |
|--------------------------|---------------|
| Bis 100 km/h | 3 km/h |
| Ueber 100 km/h | 3% der Messung |

**Beispiel:** Gemessen 84 km/h → abzuziehen 3 km/h → vorwerfbar 81 km/h.
**Beispiel:** Gemessen 130 km/h → abzuziehen 3% = 3,9 km/h ≈ 4 km/h → vorwerfbar 126 km/h.

## Schritt-fuer-Schritt-Workflow

1. **Messakte vollstaendig anfordern** (§ 147 StPO i.V.m. § 49 OWiG): Eichschein, Messprotokoll, Schulungsnachweis, Rohmessdaten, Messfoto hochauflöesend.
2. **Toleranzabzug nachrechnen** — ist der Abzug im Bescheid korrekt?
3. **Eichgueltigkeit pruefen** — Eichablaufdatum vor Messzeitpunkt?
4. **Messfoto analysieren** — eindeutige Fahrzeugzuordnung?
5. **Sachverstaendigen-Antrag stellen** (§ 244 Abs. 4 StPO i.V.m. § 77 OWiG) wenn konkrete Angriffspunkte bestehen.
6. **Verwertungsverbot ruegen** bei fehlenden Rohmessdaten (BVerfG 2020 zitieren).

## Output-Template Messakte-Anforderung

```
An das Amtsgericht [ORT] / die Zentrale Bussgeldbehörde [ORT]
Az.: [AKTENZEICHEN]

Antrag auf vollstaendige Akteneinsicht und Herausgabe der Messunterlagen

Ich fordere die vollstaendige Messakte einschliesslich:
- Messprotokoll (Aufstellungsort, Zeit, Geraet)
- Eichschein (original oder beglaubigte Kopie)
- Bedienungsanleitung fuer [GERAET]
- Schulungsnachweis des Messbeamten
- Rohmessdaten des Falldatensatzes und gesamter Messreihe (BVerfG, Beschl. v. 12.11.2020, 2 BvR 1616/18; Beschl. v. 20.6.2023, 2 BvR 1167/20 — Volltext und Randnummern aus bundesverfassungsgericht.de)
- Messfoto hochaufloesend

Ohne vollstaendige Herausgabe wird Verwertungsverbot gerueget.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Rohmessdaten-Anforderung ist Standard — niemals darauf verzichten.
- Sachverstaendigen-Antrag nur bei konkreten Angriffspunkten stellen (pauschal genuegt nicht).
- Toleranzabzug immer selbst nachrechnen.
- Anwaltliche Endkontrolle bei Sachverstaendigen-Auswahl und Beweisantraegen.
