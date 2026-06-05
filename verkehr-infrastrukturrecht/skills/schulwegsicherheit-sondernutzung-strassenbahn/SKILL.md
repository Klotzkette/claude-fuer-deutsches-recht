---
name: schulwegsicherheit-sondernutzung-strassenbahn
description: "Schulwegsicherheit Sondernutzung Strassenbahn: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schulwegsicherheit Sondernutzung Strassenbahn

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schulwegsicherheit Sondernutzung Strassenbahn** im Plugin Verkehr-/Infrastrukturrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehr-infrastrukturrecht-schulwegsicherheit` | Schulwegsicherheit rechtlich verbessern oder Amtshaftung geltend machen: Schule, Eltern oder Kommune will Schulwegplan umsetzen oder gegen Unfall auf Schulweg vorgehen. Normen: § 45 StVO (Schulweghelfer, Schulstrassen, 30er-Zone), § 839 BGB i.V.m. Art. 34 GG (Amtshaftung). Prüfraster: Schulwegplan kommunale Pflicht, Gefahrenstellen-Meldepflicht, Amtshaftung bei Verkehrsunfall auf Schulweg, Elterntaxi-Regelung. Output Amtshaftungsschreiben, Widerspruch gegen Schulwegplanung. Abgrenzung: Allgemeine Verkehrsplanung siehe verkehr-infrastrukturrecht-verkehrsplanung; Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung. |
| `verkehr-infrastrukturrecht-sondernutzung` | Sondernutzung öffentlicher Strassenflaechen beantragen und anfechten: Unternehmen braucht Erlaubnis für Aussengastronomie, Ladesaeule oder Baustelle. Normen: § 8 FStrG (Bundesstrassenrecht), § 16 StrWG NW (Landesstrassenrecht), BayStrWG (Bayern), VwGO (Widerspruch). Prüfraster: Erlaubnis vs. Gemeingebrauch, Auflagen-Prüfung, Gebühren, Widerruf bei Verkehrsanforderungen, Ladesaeulen/Aussengastro/Warenauslagen/Baustelleneinrichtung. Output Sondernutzungsantrag, Widerspruchsschrift gegen Ablehnung. Abgrenzung: Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung; Planfeststellung siehe verkehr-infrastrukturrecht-planfeststellung. |
| `verkehr-infrastrukturrecht-strassenbahn` | Strassenbahn- und OEPNV-Infrastrukturrecht: Betreiber beantragt Konzession oder Planfeststellung, oder Gemeinde will Linie neu planen. Normen: § 9 PBefG (Konzession), § 28 PBefG (Planfeststellung Strassenbahn), § 39 PBefG (Linienbuendelung), § 8a PBefG (Direktvergabe), § 41 BImSchG (Laermschutz). Prüfraster: Konzessionsvoraussetzungen, Planfeststellungsverfahren, Direktvergabe-Zulassigkeit, Laerm-/Erschuetterungsschutz Anwohner. Output Konzessionsantrag-Prüfung, Planfeststellungs-Einwendung. Abgrenzung: Planfeststellung Schiene siehe verkehr-infrastrukturrecht-planfeststellung; Foerderung siehe verkehr-infrastrukturrecht-foerderung-vergabe. |

## Arbeitsweg

Im Plugin Verkehr-/Infrastrukturrecht gilt für **Schulwegsicherheit Sondernutzung Strassenbahn**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verkehr-infrastrukturrecht-schulwegsicherheit`

**Fokus:** Schulwegsicherheit rechtlich verbessern oder Amtshaftung geltend machen: Schule, Eltern oder Kommune will Schulwegplan umsetzen oder gegen Unfall auf Schulweg vorgehen. Normen: § 45 StVO (Schulweghelfer, Schulstrassen, 30er-Zone), § 839 BGB i.V.m. Art. 34 GG (Amtshaftung). Prüfraster: Schulwegplan kommunale Pflicht, Gefahrenstellen-Meldepflicht, Amtshaftung bei Verkehrsunfall auf Schulweg, Elterntaxi-Regelung. Output Amtshaftungsschreiben, Widerspruch gegen Schulwegplanung. Abgrenzung: Allgemeine Verkehrsplanung siehe verkehr-infrastrukturrecht-verkehrsplanung; Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung.

# Schulwegsicherheit

## Triage zu Beginn

1. **Welches Ziel?** — Einrichtung einer Schulstrasse/30er-Zone, Schadensersatz nach Unfall auf dem Schulweg, Schulwegplan-Erstellung, Gefahrenstelle-Beseitigung?
2. **Wer ist Mandant?** — Gemeinde (Pflichten), Eltern (Schadensersatz), Schule (Organisationspflicht), Kind/Eltern nach Unfall?
3. **Amtshaftung?** — War Gefahrenstelle bekannt? Wurde Pflicht zur Sicherung verletzt?
4. **Zustaendigkeiten?** — Strassenverkehrsbehoerde (§ 45 StVO), Schule (Schulbehorde), Gemeinde (Strassenlasttrager).
5. **Eilt?** — Bei bekannter akuter Gefahrenstelle: Unterlassungsantrag oder Eilantrag moeglich.

## Zentrale Normen

- **§ 45 Abs. 1 StVO** — Allgemeine Verkehrsregelungsbefugnis; 30er-Zonen, Tempo-30 vor Schulen
- **§ 45 Abs. 9 StVO** — Restriktive Voraussetzungen fuer Geschwindigkeitsbeschraenkungen
- **§ 40 StVO** — Schulwarnzeichen (Zeichen 136)
- **§ 839 BGB i.V.m. Art. 34 GG** — Amtshaftung bei Verletzung der Verkehrssicherungspflicht
- **§ 823 Abs. 1 BGB** — Deliktische Haftung fuer Verkehrsgefahren
- **KMK-Empfehlungen** — Schulwegplan-Empfehlungen der Kultusministerkonferenz

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Situation vor Ort analysieren:** Gefahrenstellen, Sichtbehinderungen, fehlende Querungshilfen.
2. **Zustaendige Behoerde identifizieren:** Strassenverkehrsbehoerde, Strassenbaulasttraeger, Schulbehörde.
3. **Antrag auf Sicherungsmasssnahmen stellen** mit Begruendung; Fotos, Unfallstatistiken.
4. **Bei Ablehnung:** Widerspruch, dann Verpflichtungsklage VG.
5. **Bei Schadensfall:** Amtshaftungsklage (§ 839 BGB i.V.m. Art. 34 GG) oder Deliktsklage (§ 823 BGB).

## Harte Leitplanken

- Gefahrenstelle bekannt aber nicht gesichert = Amtshaftungsrisiko fuer Gemeinde.
- 30er-Zone-Antrag erfordert Nachweis besonderer Gefaehrdung (§ 45 Abs. 9 StVO).
- Schadensfall sofort dokumentieren: Fotos, Zeugen, Polizeiprotokoll.
- Anwaltliche Endkontrolle bei Amtshaftungsklagen.

## 2. `verkehr-infrastrukturrecht-sondernutzung`

**Fokus:** Sondernutzung öffentlicher Strassenflaechen beantragen und anfechten: Unternehmen braucht Erlaubnis für Aussengastronomie, Ladesaeule oder Baustelle. Normen: § 8 FStrG (Bundesstrassenrecht), § 16 StrWG NW (Landesstrassenrecht), BayStrWG (Bayern), VwGO (Widerspruch). Prüfraster: Erlaubnis vs. Gemeingebrauch, Auflagen-Prüfung, Gebühren, Widerruf bei Verkehrsanforderungen, Ladesaeulen/Aussengastro/Warenauslagen/Baustelleneinrichtung. Output Sondernutzungsantrag, Widerspruchsschrift gegen Ablehnung. Abgrenzung: Parkraum siehe verkehr-infrastrukturrecht-parkraumbewirtschaftung; Planfeststellung siehe verkehr-infrastrukturrecht-planfeststellung.

# Sondernutzung oeffentlicher Strassenflaechen

## Triage zu Beginn

1. **Bundesstrasse oder Gemeindestrasse?** — Bundesstrasse: § 8 FStrG; Gemeindestrasse: § 16 StrWG (je nach Bundesland); unterschiedliche Zustaendigkeiten.
2. **Art der Sondernutzung?** — Ladesaeule, Aussengastro, Warenauslage, Baustelleneinrichtung, Werbetafel, Kiosk.
3. **Liegt schon eine Genehmigung vor?** — Widerrufsvorbehalt pruefen; Gebuehren; Auflagen.
4. **Wurde abgelehnt?** — Zustaendige Behoerde, Versagungsgruende, Ermessen?
5. **Zeitliche Dringlichkeit?** — Einstweiliger Rechtsschutz (§ 80a VwGO) bei drohender Vollzugshandlung.

## Zentrale Normen

- **§ 8 FStrG** — Sondernutzung an Bundesfernstrassen; Erlaubnis erforderlich; widerruflich
- **§ 16 StrWG NRW (als Muster)** — Sondernutzung an Gemeindestrassen; Gebuehren; Auflagenpraxis
- **§ 18 StrWG NRW** — Sondernutzungsgebuehren; Gebuehrenrahmen
- **§ 7 FStrG** — Gemeingebrauch; Abgrenzung zur Sondernutzung
- **§ 40 VwVfG** — Ermessen der Behoerde bei der Erlaubniserteilung; kein Anspruch, aber willkuerfreie Entscheidung
- **§ 49 VwVfG** — Widerruf einer rechtmaessigen Erlaubnis

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **Sondernutzungsart und Strassenkategorie bestimmen** → zustaendige Behoerde.
2. **Antrag stellen:** Nutzungsart, Dauer, Flaeche, Zweck; Lageskizze.
3. **Auflagen beim Erhalt der Erlaubnis pruefen:** Verkehrssicherungspflicht, Haftung, Gebuehren.
4. **Widerrufsvorbehalt dokumentieren:** Bei laengerfristiger Investition (Ladesaeule) Bestandsschutz-Frage klaeren.
5. **Bei Ablehnung:** Widerspruch (1 Monat, § 70 VwGO) → Verpflichtungsklage VG.

## Harte Leitplanken

- Sondernutzungserlaubnis ist widerruflich — Investitionen sorgfaeltig planen.
- Gebuehren muessen verhaeltnismaessig sein — bei exzessiven Gebuehren Widerspruch.
- Gleichbehandlung pruefen: Erlaubt die Gemeinde anderen Nutzern dasselbe?
- Anwaltliche Endkontrolle bei Antraegen und Widerspruechen.

## 3. `verkehr-infrastrukturrecht-strassenbahn`

**Fokus:** Strassenbahn- und OEPNV-Infrastrukturrecht: Betreiber beantragt Konzession oder Planfeststellung, oder Gemeinde will Linie neu planen. Normen: § 9 PBefG (Konzession), § 28 PBefG (Planfeststellung Strassenbahn), § 39 PBefG (Linienbuendelung), § 8a PBefG (Direktvergabe), § 41 BImSchG (Laermschutz). Prüfraster: Konzessionsvoraussetzungen, Planfeststellungsverfahren, Direktvergabe-Zulassigkeit, Laerm-/Erschuetterungsschutz Anwohner. Output Konzessionsantrag-Prüfung, Planfeststellungs-Einwendung. Abgrenzung: Planfeststellung Schiene siehe verkehr-infrastrukturrecht-planfeststellung; Foerderung siehe verkehr-infrastrukturrecht-foerderung-vergabe.

# Strassenbahn und OEPNV — Infrastrukturrecht

## Triage zu Beginn

1. **Konzession (Betrieb) oder Bau?** — Konzession nach § 9 PBefG (Personenbefoerderung), Planfeststellung nach § 28 PBefG (Infrastrukturbau) sind separate Verfahren.
2. **Mandantentyp?** — Verkehrsunternehmen (Konzessionsbewerber), Anlieger (Laerm, Erschuetterungen), Gemeinde (Delegationsrecht, Ausschreibung).
3. **Direktvergabe oder EU-Ausschreibung?** — § 8a PBefG i.V.m. VO (EG) 1370/2007: wann ist Direktvergabe zulaessig?
4. **Planfeststellungseinwendung?** — Laermschutz, Erschuetterungsschutz, Eigentumseingriff, Alternative Trassenauswahl.
5. **Konzessionsablauf?** — Befristung der Konzession; Neuausschreibung oder Verlaengerung.

## Zentrale Normen

- **§ 9 PBefG** — Genehmigung fuer Strassenbahn und Obus; Mindestanforderungen
- **§ 28 PBefG** — Planfeststellung und Plangenehmigung fuer Strassenbahnlinien
- **§ 39 PBefG** — Linienbuendelung; Koordinierung von OEPNV-Linien
- **§ 8a PBefG** — Direktvergabe; Ausnahme von der Ausschreibungspflicht
- **VO (EG) 1370/2007** — Oeffentliche Personenverkehrsdienste; Direktvergabe-Voraussetzungen
- **§ 41 BImSchG i.V.m. 16. BImSchV** — Laermschutz bei Infrastrukturausbau
- **§ 74 VwVfG i.V.m. § 28 PBefG** — Planfeststellungsbeschluss; Schutzauflagen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Planfeststellung Strassenbahn

1. **Trassenauswahl prufen:** Wurden Alternativen ernsthaft geprueft?
2. **Einwendung formulieren:** Laerm, Erschuetterungen, Eigentumseingriff, Sichtbeziehungen.
3. **Laermschutzberechnungen anfordern** (§ 41 BImSchG, 16. BImSchV).
4. **Eroerrterungstermin teilnehmen** (§ 73 Abs. 6 VwVfG).
5. **Planfeststellungsbeschluss pruefen:** Auflagen zu Laerm- und Erschuetterungsschutz korrekt?
6. **Klage:** OVG/BVerwG je nach Bundesland und Vorhabentyp.

## Harte Leitplanken

- Einwendungsfrist 6 Wochen nach § 73 Abs. 4 VwVfG — Praeklusion!
- Direktvergabe EU-rechtskonform pruefen — VO (EG) 1370/2007 beachten.
- Laermschutzberechnungen fachlich begleiten lassen (Sachverstaendiger).
- Anwaltliche Endkontrolle bei Einwendungen und Klagen.
