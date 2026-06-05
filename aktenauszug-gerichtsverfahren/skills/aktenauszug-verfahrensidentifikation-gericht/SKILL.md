---
name: aktenauszug-verfahrensidentifikation-gericht
description: "Verfahrensidentifikation Gericht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verfahrensidentifikation Gericht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verfahrensidentifikation Gericht** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verfahrensidentifikation` | Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und Verfahrensart (Klage Eilverfahren Berufung Revision Beschwerde). Normen §§ 253 261 ZPO Klageerhebung. |
| `verfahrenszusammenfassung-absatz` | Anwalt will sich schnell in Akte einarbeiten ohne vollständige Lektuere. Acht bis zehn Saetze Hintergrund Streitstand prozessuale Lage anstehende Verfahrenshandlungen. Normen §§ 253 261 ZPO. Prüfraster Vollständigkeit Neutralitaet Verstaendlichkeit Aktualitaet. Output Zusammenfassungs-Absatz. Abgrenzung zu aktenauszug-erstellen (vollständig) und schwerpunktthemen-identifikation (Streitpunkte). |
| `aktenauszug-erstellen` | Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze oder PDFs und will strukturierten Aktenauszug erstellen. Sechs Bausteine: Verfahrensidentifikation Einleitungssatz Absatz-Zusammenfassung Sachverhaltschronologie Verfahrenschronologie Parteivortrag-Tabelle Beweis- und Rechtsargumente. Normen §§ 128-134 ZPO §§ 355-455 ZPO. Output strukturierter Markdown-Aktenauszug. Abgrenzung zu aktenauszug-strukturprüfung (Qualitaetskontrolle) und verfahrenszusammenfassung-absatz (Kurz-Überblick). |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Verfahrensidentifikation Gericht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verfahrensidentifikation`

**Fokus:** Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und Verfahrensart (Klage Eilverfahren Berufung Revision Beschwerde). Normen §§ 253 261 ZPO Klageerhebung.

# Verfahrensidentifikation

## Zweck

Dieser Skill extrahiert alle Stammdaten eines Gerichtsverfahrens aus der vorgelegten Akte und stellt sie in einem standardisierten Block dar. Der Block dient als Kopfzeile jedes Aktenauszugs.

## Triage — kläre vor Erstellung

1. Liegt die Klageschrift oder der Eröffnungsbeschluss vor? (Aktenzeichen, Parteien)
2. Sind die Prozessbevollmächtigten beider Seiten aus der Akte ersichtlich?
3. Wurde der Streitwert festgesetzt (Streitwertbeschluss) oder nur vorläufig angegeben?
4. Gibt es Streithelfer oder Nebenintervenienten?

## Zentrale Normen

- § 253 Abs. 2 Nr. 1 ZPO — Klageschrift muss Gericht, Parteien und Streitgegenstand bezeichnen
- § 261 Abs. 1 ZPO — Anhängigkeit mit Einreichung der Klage; Rechtshängigkeit mit Zustellung
- §§ 3-9 ZPO — Streitwert (Bewertung Klageantrag, Früchte, Zinsen, Kosten)
- § 63 GKG — Streitwertfestsetzung durch das Gericht; § 68 GKG — Streitwertbeschwerde
- §§ 66-74 ZPO — Streithelfer / Nebenintervention (Voraussetzungen, Rechte)

## Rechtsprechung zur Verfahrensidentifikation

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zu extrahierende Felder

### Gericht und Spruchkörper

- Gericht (vollständige Bezeichnung, z. B. Landgericht Frankfurt am Main)
- Kammer oder Senat (z. B. 3. Zivilkammer, 14. Senat)
- Aktenzeichen (z. B. 3 O 123/23)
- Instanz (Erste Instanz / Berufung / Revision / Beschwerde / Rechtsbeschwerde)

### Verfahrensart

- Ordentliches Klageverfahren (ZPO)
- Eilverfahren (einstweilige Verfügung § 935 ff. ZPO / einstweilige Anordnung)
- Berufungsverfahren (§ 511 ff. ZPO)
- Revisionsverfahren (§ 542 ff. ZPO)
- Strafverfahren (StPO)
- Verwaltungsverfahren (VwGO)
- Arbeitsgerichtsverfahren (ArbGG)
- Sozialgerichtsverfahren (SGG)
- Sonstiges (Beschwerde, PKH, Streitwertbeschwerde)

### Streitwert

- Festgesetzter Streitwert (soweit bekannt)
- Vorläufiger Streitwert (soweit Antrag gestellt)
- Gebührenstreitwert (sofern abweichend)

### Parteien

Für jede Partei:

| Feld | Inhalt |
|---|---|
| Bezeichnung | Kläger / Beklagter / Berufungskläger / Streithelfer etc. |
| Name / Firma | Vollständige Bezeichnung |
| Anschrift | Straße PLZ Ort |
| Gesetzliche Vertretung | (bei juristischen Personen) |
| Prozessbevollmächtigter | Kanzlei und Rechtsanwalt |
| Anschrift Bevollmächtigter | Straße PLZ Ort |

### Streithelfer / Nebenintervenienten

- Benennung der Partei, auf deren Seite der Streithelfer steht
- Eigene Bevollmächtigung wenn vorhanden

## Output-Vorlage

```
## Verfahrensidentifikation

**Gericht:** Landgericht [Stadt]
**Kammer:** [X]. Zivilkammer
**Aktenzeichen:** [AZ]
**Instanz:** Erste Instanz
**Verfahrensart:** Ordentliches Klageverfahren (ZPO)
**Streitwert:** [EUR oder "nicht festgesetzt"]

### Parteien

| Rolle | Partei | Anschrift | Prozessbevollmächtigter |
|---|---|---|---|
| Kläger | [Name] | [Adresse] | [Kanzlei / RA] |
| Beklagter | [Name] | [Adresse] | [Kanzlei / RA] |
```

## Hinweise

- Fehlende Felder werden als "nicht aus Akte ersichtlich" gekennzeichnet, nicht geschätzt.
- Bei mehreren Klägern oder Beklagten wird jede Person separat aufgeführt.
- Streithelfer werden gesondert unter der Hauptparteitabelle gelistet.
- Keine Bewertung der Parteibezeichnung (z. B. ob Kläger wirklich klagebefugt ist).

---

## 2. `verfahrenszusammenfassung-absatz`

**Fokus:** Anwalt will sich schnell in Akte einarbeiten ohne vollständige Lektuere. Acht bis zehn Saetze Hintergrund Streitstand prozessuale Lage anstehende Verfahrenshandlungen. Normen §§ 253 261 ZPO. Prüfraster Vollständigkeit Neutralitaet Verstaendlichkeit Aktualitaet. Output Zusammenfassungs-Absatz. Abgrenzung zu aktenauszug-erstellen (vollständig) und schwerpunktthemen-identifikation (Streitpunkte).

# Verfahrenszusammenfassung — Absatz

## Zweck

Der Zusammenfassungsabsatz bietet dem Leser nach dem Einleitungssatz eine kompakte Gesamtschau des Verfahrens. Er ist kein Sachverhaltsnarrativ und keine Chronologie, sondern ein strukturierter Fließtext, der Hintergrund, Streitpunkte, Stand und Ausblick verbindet.

## Triage — kläre vor Erstellung

1. In welchem Stadium befindet sich das Verfahren? (Schriftsatzaustausch / Beweisaufnahme / Entscheidungsreife)
2. Welcher Sachverhalt ist unstreitig, welcher wird bestritten?
3. Hat das Gericht bereits Hinweise nach § 139 ZPO erteilt?
4. Steht ein Termin unmittelbar bevor?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- § 253 ZPO — Klagebegehren (Grundlage des Zusammenfassungsabsatzes)
- § 261 ZPO — Anhängigkeit und Rechtshängigkeit (Verfahrensstand)
- § 139 ZPO — Richterliche Prozessleitung (Hinweise des Gerichts beeinflussen den Stand)
- § 286 ZPO — Freie Beweiswürdigung (offene Fragen zur Beweiswürdigung)

## Rechtsprechung zur Verfahrensdokumentation und Einarbeitung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aufbau (acht bis zehn Sätze)

| Satz | Inhalt |
|---|---|
| 1 | Hintergrund der Geschäftsbeziehung oder des Sachverhalts |
| 2 | Anlass des Rechtsstreits (Auslösendes Ereignis) |
| 3 | Klagebegehren / Antragstellung |
| 4 | Kerneinwand der Gegenseite |
| 5 | Weiterer streitiger Sachverhaltspunkt |
| 6 | Bisheriger prozessualer Verlauf (Schriftsätze / Termine) |
| 7 | Beweisaufnahme oder Beweisanordnung (soweit erfolgt) |
| 8 | Aktueller Verfahrensstand |
| 9 | Nächste Verfahrenshandlung / anstehender Termin |
| 10 | Wesentliche offene Rechtsfrage (ohne Einschätzung) |

## Stilanforderungen

- Präsens oder Perfekt — kein Futur für Vergangenes
- Keine direkten Zitate aus Schriftsätzen (paraphrasieren)
- Keine Wertung: nicht "zu Recht", "unbegründet", "offensichtlich"
- Keine Erfolgsprognose: nicht "wird Erfolg haben", "dürfte scheitern"
- Rechtsbegriffe korrekt verwenden
- Parteienbezeichnung konsistent (z. B. stets "die Klägerin" oder Kurzname)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zusammenfassung fuer Akte oder Uebergabe | Vorlage unten nach acht bis zehn Saetzen |
| Variante A — Adressat ist Laie (Mandant) | Vereinfachte Sprache; keine Paragrafenverweise |
| Variante B — sehr fruehes Stadium ohne Entscheidung | Vorlaeufige Zusammenfassung mit Offenhalten des Ausgangs |
| Variante C — Verfahren laueft noch | Zwischenbericht-Format statt abschliessender Zusammenfassung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Vorlage

```
Die Parteien stehen seit [Zeitraum] in einer [Geschäftsbeziehung / Vertragsbeziehung].
Im [Monat JJJJ] kam es zu [auslösendem Ereignis].
Die Klägerin macht daraufhin [Klagebegehren] geltend und stützt sich hierfür auf [Hauptnorm].
Die Beklagte bestreitet [Kerneinwand] und beruft sich hilfsweise auf [Einrede/Einwendung].
Streitig ist insbesondere [weiterer Streitpunkt].
Im Verfahren wurden bislang [prozessuale Schritte] vorgenommen.
[Soweit Beweisbeschluss: Das Gericht hat Beweis erhoben durch ...]
Derzeit befindet sich das Verfahren im Stadium [aktueller Stand].
Nächste Verfahrenshandlung ist [Termin / Schriftsatzfrist].
Rechtlich offen ist die Frage [zentrale Rechtsfrage].
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Besonderheiten nach Verfahrensart

**Eilverfahren:** Besondere Dringlichkeit und Verfügungsgrund hervorheben; Vollziehungsfrist nach § 929 Abs. 2 ZPO benennen.

**Strafverfahren:** Anklageschrift-Inhalt und Verfahrensstand (Eröffnungsbeschluss / laufende Hauptverhandlung / Revisionsinstanz) darstellen.

**Verwaltungsverfahren:** Vorverfahren (Widerspruchsbescheid) und aufschiebende Wirkung (§ 80 VwGO) erwähnen.

**Arbeitsgerichtsverfahren:** Gütetermin und Kammertermin unterscheiden; Frist des § 4 KSchG ansprechen.

## Qualitätscheck

- [ ] Acht bis zehn Sätze vorhanden?
- [ ] Hintergrund dargestellt?
- [ ] Klagebegehren und Kerneinwand genannt?
- [ ] Aktueller Stand und nächster Schritt benannt?
- [ ] Keine Wertung, keine Prognose?
- [ ] Richterliche Hinweise nach § 139 ZPO berücksichtigt?

<!-- AUDIT 27.05.2026: BGH VI ZR 146/19 (NOT_FOUND auf dejure.org) entfernt und ersetzt durch BGH VI ZR 84/19, NJW 2021, 2364 (verifiziert auf dejure.org). -->

## 3. `aktenauszug-erstellen`

**Fokus:** Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze oder PDFs und will strukturierten Aktenauszug erstellen. Sechs Bausteine: Verfahrensidentifikation Einleitungssatz Absatz-Zusammenfassung Sachverhaltschronologie Verfahrenschronologie Parteivortrag-Tabelle Beweis- und Rechtsargumente. Normen §§ 128-134 ZPO §§ 355-455 ZPO. Output strukturierter Markdown-Aktenauszug. Abgrenzung zu aktenauszug-strukturprüfung (Qualitaetskontrolle) und verfahrenszusammenfassung-absatz (Kurz-Überblick).

# Aktenauszug Erstellen — Hauptworkflow

## Leitidee

Wer ein Gerichtsverfahren schnell erfassen muss — sei es beim Mandatswechsel, bei der Einarbeitung eines neuen Sachbearbeiters oder bei der Vorbereitung auf eine mündliche Verhandlung — benötigt einen strukturierten Überblick. Dieser Skill nimmt die gesamte Akte entgegen und erzeugt einen vollständigen Aktenauszug mit allen sechs Bausteinen.

## Triage zu Beginn — kläre vor Erstellung des Aktenauszugs

1. Welche Verfahrensart liegt vor? (Zivilprozess, Arbeitsgericht, Verwaltungsgericht, Sozialrecht, Strafprozess)
2. In welcher Instanz befindet sich das Verfahren? (Erstinstanz, Berufung, Revision)
3. Liegen alle wesentlichen Schriftsätze vor oder nur Teilakten?
4. Gibt es bereits einen Termin, dessen Vorbereitung im Vordergrund steht?
5. Soll der Aktenauszug intern (anwaltlich) oder zur Übergabe an Mandant dienen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen (Prozessrecht)

- §§ 128-134 ZPO — Schriftliches und mündliches Verfahren, Schriftsätze
- §§ 253-261 ZPO — Klageerhebung und Verfahrenseinleitung
- §§ 355-455 ZPO — Beweisaufnahme (Sachverstaendige, Zeugen, Augenschein, Urkunden)
- §§ 495a, 522, 540 ZPO — Vereinfachtes Verfahren, Berufungsverwerfung, Berufungsurteil
- §§ 704-945 ZPO — Zwangsvollstreckung (Abschnitt relevant fuer Vollstreckungstitel in Akte)
- § 91a ZPO — Kosten bei Erledigterklärung
- § 139 ZPO — Materielle Prozessleitung, richterliche Hinweispflicht

## Aktuelle Rechtsprechung zum Aktenauszug und Verfahrensrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Voraussetzungen

- Gerichtliche Akte oder wesentliche Teile davon (PDF, Word, maschinenlesbar)
- Optional: Inhaltsverzeichnis der Akte
- Optional: Hinweis auf die Verfahrensart (Zivil, Straf, Verwaltung, Arbeit, Sozial)

## Sechs Bausteine des Aktenauszugs

### Baustein 1 — Verfahrensidentifikation

Gericht, Kammer/Senat, Aktenzeichen, Streitwert, Parteien mit Anwälten, Instanz, Verfahrensart.

### Baustein 2 — Einleitungssatz

Ein bis zwei Sätze, die den Kern des Rechtsstreits nennen: Wer streitet mit wem worüber, welche Hauptnorm ist einschlägig.

### Baustein 3 — Zusammenfassung (Absatz)

Acht bis zehn Sätze: Hintergrund, Streitstand, prozessuale Lage, anstehende Verfahrenshandlungen.

### Baustein 4 — Sachverhaltschronologie

Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen. Datum fettgedruckt vorangestellt.

### Baustein 5 — Verfahrenschronologie

Chronologische Bullet-Liste der prozessualen Schritte. Fristen und Termine werden hervorgehoben.

### Baustein 6 — Tabellen (Parteivortrag / Beweismittel / Rechtsargumente)

Drei separate Tabellen im Markdown-Format mit Spalten für Klägerseite und Beklagtenseite.

## Schritt-für-Schritt-Workflow

1. **Akte sichten** — Inhaltsverzeichnis oder Seitenstruktur erfassen; fehlende Seiten markieren
2. **Verfahrensart bestimmen** — aktiviere passenden Modus-Skill (Zivil/ArbG/VerwG/Sozial/Straf)
3. **Verfahrensidentifikation extrahieren** (→ Skill `verfahrensidentifikation`)
4. **Einleitungssatz formulieren** (→ Skill `einleitungssatz-generator`)
5. **Zusammenfassungsabsatz schreiben** (→ Skill `verfahrenszusammenfassung-absatz`)
6. **Sachverhalt chronologisch ordnen** (→ Skill `sachverhaltschronologie`)
7. **Verfahrensschritte chronologisch ordnen** (→ Skill `verfahrenschronologie`)
8. **Fristen hervorheben** (→ Skill `fristen-und-terminkalender`) — alle Notfristen mit ⚠️
9. **Parteivortrag gegenüberstellen** (→ Skill `parteivortrag-gegenueberstellung`)
10. **Beweismittel tabellarisch erfassen** (→ Skill `beweismittel-gegenueberstellung`)
11. **Rechtsargumente tabellarisch erfassen** (→ Skill `rechtsargumente-gegenueberstellung`)
12. **Neutralitätsprüfung** (→ Skill `neutralitaetspruefung`)
13. **Strukturprüfung** (→ Skill `aktenauszug-strukturpruefung`)

## Entscheidungsbaum — Verfahrensart

```
Liegt Akte vor?
 → Ja: Verfahrensart prüfen
 → Arbeitsgericht? → Skill arbeitsgerichtsverfahren-modus aktivieren
 → Verwaltungsgericht? → Skill verwaltungsprozess-modus aktivieren
 → Strafgericht? → Skill strafprozess-modus aktivieren
 → Sozialgericht? → Skill sozialgerichtsverfahren-modus aktivieren
 → Zivilgericht (LG/AG/OLG)? → Skill zivilprozess-modus aktivieren
 → Nein: Fehlende Unterlagen beim Mandanten anfordern; Notfrist prüfen
```

## Output-Format

```markdown
# Aktenauszug — [Aktenzeichen]

## Verfahrensidentifikation
...

## Einleitungssatz
...

## Zusammenfassung
...

## Sachverhaltschronologie
- **TT.MM.JJJJ** Beschreibung
- **TT.MM.JJJJ** Beschreibung

## Verfahrenschronologie
- **TT.MM.JJJJ** Beschreibung
- ⚠️ **TT.MM.JJJJ — FRIST:** Beschreibung

## Parteivortrag

| Punkt | Klägerseite | Beklagtenseite |
|---|---|---|

## Beweismittel

| Beweismittel | Klägerseite | Beklagtenseite |
|---|---|---|

## Rechtsargumente

| Aspekt | Klägerseite | Beklagtenseite |
|---|---|---|
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — strukturierter Aktenauszug fuer Gericht | Vollformat nach den sechs Bausteinen unten |
| Variante A — nur interne Einarbeitung noetig | Kurzform ohne Verfahrenschronologie; Bausteine 1-3 genuegen |
| Variante B — Eilsache; Zeit fehlt fuer vollstaendigen Auszug | Einleitungssatz + Sachverhaltschronologie priorisieren; Rest nachliefern |
| Variante C — Parteivertreter hat bereits Zusammenfassung geliefert | Kritische Pruefung und Ergaenzung statt Neuerstellung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Übergabevermerk (intern)

**Adressat:** Sachbearbeiter / aufnehmender Anwalt — Tonfall: sachlich-juristisch

```
ÜBERGABEVERMERK — [AKTENZEICHEN]
Bearbeiter bisher: [NAME]
Stand: [DATUM]

Verfahren: [KURZBEZEICHNUNG]
Nächste Frist: [DATUM + BEZEICHNUNG]
Nächster Termin: [DATUM + ORT]
Offene Aufgaben: [LISTE]

Besonderheiten: [z.B. Beweissicherungsantrag gestellt, SV noch nicht bestellt]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Qualitätsgrundsätze

- Keine Erfolgsprognose
- Neutrale Sprache ohne Wertung
- Alle Fristen und Termine hervorgehoben
- Keine KI-Terminologie im Output

## Hinweis

Der Aktenauszug ersetzt nicht die eigene Aktenlektüre. Er ist ein strukturiertes Arbeits- und Kommunikationsmittel für den anwaltlichen Alltag und bedarf der Prüfung durch den verantwortlichen Rechtsanwalt.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- BGH VII ZB 36/20: ersatzlos entfernt (Entscheidung nicht auffindbar auf dejure.org oder bundesgerichtshof.de; NJW-RR 2022, 1350 konnte keinem BGH VII ZB 36/20 zugeordnet werden)
