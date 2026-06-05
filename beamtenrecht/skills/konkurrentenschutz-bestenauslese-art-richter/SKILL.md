---
name: konkurrentenschutz-bestenauslese-art-richter
description: "Konkurrentenschutz Bestenauslese ART Richter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Konkurrentenschutz Bestenauslese ART Richter

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Konkurrentenschutz Bestenauslese ART Richter** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `konkurrentenschutz-bestenauslese-art-33-ii-gg` | Pruefschema zum Grundsatz der Bestenauslese aus Art. 33 Abs. 2 GG bei Auswahlentscheidungen im oeffentlichen Dienst. Liefert Bausteine fuer Konkurrentenwiderspruch und Konkurrentenklage. Klaert die drei Auswahlkriterien Eignung Befaehigung fachliche Leistung sowie Beurteilungsspielraum Beurteilungsmaszstab und gerichtliche Kontrolldichte. Beruecksichtigt Stand der BVerfG- und BVerwG-Rechtsprechung zum bewerbungsverfahrensrechtlichen Anspruch. Hilft bei der Pruefung Anforderungsprofil dienstliche Beurteilung Auswahlvermerk Auswahlgespraech. Im Zweifel Verweis auf das spezifische Schwester-Skill konkurrentenklage-einstweiliger-rechtsschutz. |
| `konkurrentenschutz-richter-professoren-fuehrungsaemter` | Konkurrentenschutz bei Richtern, Professoren und Führungsämtern: Bestenauslese, Gremienbeteiligung, Präsidialrat, Berufungskommission und besondere Aktenlage. |
| `konkurrentenschutz-sofortprogramm-einzelgerechtigkeit` | Konkurrentenschutz-Sofortprogramm: Bewerbungsverfahrensanspruch, Konkurrentenmitteilung, Stillhaltefrist, Eilantrag, Akteneinsicht und Einzelgerechtigkeit. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Konkurrentenschutz Bestenauslese ART Richter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `konkurrentenschutz-bestenauslese-art-33-ii-gg`

**Fokus:** Pruefschema zum Grundsatz der Bestenauslese aus Art. 33 Abs. 2 GG bei Auswahlentscheidungen im oeffentlichen Dienst. Liefert Bausteine fuer Konkurrentenwiderspruch und Konkurrentenklage. Klaert die drei Auswahlkriterien Eignung Befaehigung fachliche Leistung sowie Beurteilungsspielraum Beurteilungsmaszstab und gerichtliche Kontrolldichte. Beruecksichtigt Stand der BVerfG- und BVerwG-Rechtsprechung zum bewerbungsverfahrensrechtlichen Anspruch. Hilft bei der Pruefung Anforderungsprofil dienstliche Beurteilung Auswahlvermerk Auswahlgespraech. Im Zweifel Verweis auf das spezifische Schwester-Skill konkurrentenklage-einstweiliger-rechtsschutz.


# Konkurrentenschutz — Bestenauslese nach Art. 33 Abs. 2 GG

## 1. Zweck und Anwendungsfall

Skill fuer Bewerber im oeffentlichen Dienst, die in einem Auswahlverfahren um Einstellung, Beförderung oder Übertragung eines höherwertigen Dienstpostens unterlegen sind oder unterliegen koennten. Liefert das materielle Pruefschema des Art. 33 Abs. 2 GG (Bestenauslese als grundrechtsgleiches Recht / bewerbungsverfahrensrechtlicher Anspruch).

Anwendung typischerweise vor und neben den Skills `konkurrentenklage-einstweiliger-rechtsschutz`, `anlassbeurteilung-vs-regelbeurteilung`, `anforderungsprofil-konstitutiv-deklaratorisch`, `auswahlgespraech-dokumentationspflicht`, `plausibilisierung-gleicher-gesamtnoten`.

## 2. Eingaben

- Stellenausschreibung (Wortlaut, Anforderungsprofil)
- Auswahlvermerk / Beförderungsranking
- Eigene letzte dienstliche Beurteilung des Mandanten
- Beurteilung der ausgewaehlten Konkurrentin oder des Konkurrenten (soweit zugaenglich)
- Mitteilung des Dienstherrn ueber die Auswahlentscheidung mit Frist
- Auskunft, ob bereits Ernennung erfolgt ist (Ämterstabilitaet)

## 3. Ablauf / Checkliste

### a) Sachlicher Anwendungsbereich
- Steht eine "Einstellung" oder eine "Beförderung" im statusrechtlichen Sinne in Rede oder bloss eine Umsetzung? Bei reiner Umsetzung greift Art. 33 Abs. 2 GG nicht; dann Skill `umsetzung-kein-va-rechtsschutz` heranziehen.
- Ist der Dienstposten höherwertig als das Statusamt des Mandanten? Falls ja, gilt Bestenauslese auch bei Dienstpostenkonkurrenz nach staendiger Rechtsprechung des BVerwG; Az im Einzelfall verifizieren.

### b) Die drei Auswahlkriterien
- Eignung — koerperliche, geistige, charakterliche Eignung; Verfassungstreue
- Befaehigung — Ausbildung, Erfahrung, Vorbildung, allgemeine Faehigkeiten
- Fachliche Leistung — bisherige dienstliche Leistung, Erfolg, Verwendungsbreite

### c) Beurteilungsgrundlage
- Primaer aktuelle dienstliche Beurteilung (Regel- oder Anlassbeurteilung).
- Bei gleicher Gesamtnote: Binnendifferenzierung durch Einzelmerkmale (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).
- Erst danach hilfsweise Auswahlgespraech, Assessment Center, Beurteilungsbeitraege.

### d) Kontrolldichte
- Gerichtliche Kontrolle des Auswahlvermerks auf Verfahrensfehler, Anwendung falscher Massstaebe, Nichteinbeziehung wesentlicher Gesichtspunkte, Verkennung der Beurteilungsstruktur.
- Kein eigener Beurteilungsmaszstab des Gerichts.

### e) Aemterstabilitaet
- Ist die Ernennung des Konkurrenten bereits erfolgt, ist die Auswahlentscheidung in der Regel nicht mehr ruekgaengig zu machen; Skill `schadensersatz-nichtbefoerderung` heranziehen.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; § 9 BeamtStG; § 22 BBG; §§ 32 ff. BLV.
- BVerfG zur Bestenauslese und zum bewerbungsverfahrensrechtlichen Anspruch — ständige Rechtsprechung, konkret vor Zitat frei prüfen, Az im Einzelfall verifizieren.
- BVerwG zur Auswahlentscheidung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Kurzgutachten in Memoform (Sachverhalt — Frage — Kurzantwort — Bewertung — Risiko — Quellen) oder
- Mandantenbrief mit Empfehlung zu Widerspruch / Eilantrag / Klage.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Mandant ist Polizeihauptkommissar Besoldungsgruppe A11. Dienstposten A12 wird ausgeschrieben. Ranking ergibt 17 Bewerber. Mandant Rang 3 mit Gesamtnote "uebertrifft die Anforderungen". Rang 1 hat dieselbe Gesamtnote. Aufgabe: Pruefe Anforderungsprofil, Binnendifferenzierung, Auswahlvermerk; bereite Antrag auf einstweiligen Rechtsschutz nach § 123 VwGO vor.

## 2. `konkurrentenschutz-richter-professoren-fuehrungsaemter`

**Fokus:** Konkurrentenschutz bei Richtern, Professoren und Führungsämtern: Bestenauslese, Gremienbeteiligung, Präsidialrat, Berufungskommission und besondere Aktenlage.


# konkurrentenschutz-richter-professoren-fuehrungsaemter

## Aufgabe

Überträgt Art. 33 Abs. 2 GG auf sensible Auswahlverfahren ohne Schema-Falle.

## Pflichtfragen

- Bund oder welches Bundesland, welcher Dienstherr und welcher Status: Beamter, Richter, Versorgungsempfänger, Bewerber oder Ruhestandsfall?
- Welcher Bescheid, welche Verfügung, welche Auswahlmitteilung, welche Versorgungsauskunft oder welcher Beihilfebescheid liegt vor?
- Datum, Zugang, Frist, Rechtsbehelf und gewünschtes Ziel?
- Welche Aktenbestandteile fehlen: Personalakte, Auswahlvermerk, Beurteilungen, Berechnungsblatt, amtsärztliches Gutachten, Beihilfeakte, PKV-Schreiben?

## Prüfprogramm

1. **Rechtsquelle trennen:** Bundesrecht, Landesrecht, Richterrecht und Satzungs-/Versorgungsrecht sauber auseinanderhalten.
2. **Eilbedürftigkeit prüfen:** Konkurrentenschutz, Widerspruchsfrist, Klagefrist, Beihilfefrist, Dienstunfallmeldung oder Ruhestandsdatum sichern.
3. **Materiellen Kern prüfen:** Art. 33 Abs. 2 oder Abs. 5 GG, BeamtVG, BBhV/landesrechtliche Beihilfe, BBesG/Landesbesoldung, BeamtStG/BBG und VwGO.
4. **Akte auswerten:** Nicht nur Normen, sondern Dokumentation, Ermessen, Beteiligung, Begründung, Plausibilität und Beweiswert bewerten.
5. **Output bauen:** Sofortmaßnahme, Antrag, Widerspruch, Eilantrag, Akteneinsicht, Mandantenbrief oder Berechnungsmatrix.

## Ausgabe

- Kurzbild mit Frist und Ziel.
- Prüfmatrix mit Normgruppe, Tatsachen, Unterlagen und Risiken.
- Konkreter nächster Schritt mit Entwurf oder Anlagenliste.

## Quellen-Hardening

Keine Rechtsprechung aus Modellwissen zitieren. Entscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher/frei prüfbarer Quelle. Landesrecht und Beihilferecht live prüfen.

## 3. `konkurrentenschutz-sofortprogramm-einzelgerechtigkeit`

**Fokus:** Konkurrentenschutz-Sofortprogramm: Bewerbungsverfahrensanspruch, Konkurrentenmitteilung, Stillhaltefrist, Eilantrag, Akteneinsicht und Einzelgerechtigkeit.


# konkurrentenschutz-sofortprogramm-einzelgerechtigkeit

## Aufgabe

Sichert den konkreten Bewerber, bevor die Ernennung vollendete Tatsachen schafft.

## Pflichtfragen

- Bund oder welches Bundesland, welcher Dienstherr und welcher Status: Beamter, Richter, Versorgungsempfänger, Bewerber oder Ruhestandsfall?
- Welcher Bescheid, welche Verfügung, welche Auswahlmitteilung, welche Versorgungsauskunft oder welcher Beihilfebescheid liegt vor?
- Datum, Zugang, Frist, Rechtsbehelf und gewünschtes Ziel?
- Welche Aktenbestandteile fehlen: Personalakte, Auswahlvermerk, Beurteilungen, Berechnungsblatt, amtsärztliches Gutachten, Beihilfeakte, PKV-Schreiben?

## Prüfprogramm

1. **Rechtsquelle trennen:** Bundesrecht, Landesrecht, Richterrecht und Satzungs-/Versorgungsrecht sauber auseinanderhalten.
2. **Eilbedürftigkeit prüfen:** Konkurrentenschutz, Widerspruchsfrist, Klagefrist, Beihilfefrist, Dienstunfallmeldung oder Ruhestandsdatum sichern.
3. **Materiellen Kern prüfen:** Art. 33 Abs. 2 oder Abs. 5 GG, BeamtVG, BBhV/landesrechtliche Beihilfe, BBesG/Landesbesoldung, BeamtStG/BBG und VwGO.
4. **Akte auswerten:** Nicht nur Normen, sondern Dokumentation, Ermessen, Beteiligung, Begründung, Plausibilität und Beweiswert bewerten.
5. **Output bauen:** Sofortmaßnahme, Antrag, Widerspruch, Eilantrag, Akteneinsicht, Mandantenbrief oder Berechnungsmatrix.

## Ausgabe

- Kurzbild mit Frist und Ziel.
- Prüfmatrix mit Normgruppe, Tatsachen, Unterlagen und Risiken.
- Konkreter nächster Schritt mit Entwurf oder Anlagenliste.

## Quellen-Hardening

Keine Rechtsprechung aus Modellwissen zitieren. Entscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher/frei prüfbarer Quelle. Landesrecht und Beihilferecht live prüfen.
