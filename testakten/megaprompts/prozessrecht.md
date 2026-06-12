# Megaprompt: prozessrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 56 Skills des Plugins `prozessrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): ordnet Rolle (Mandant, Gegner, Gericht), markiert Fri…
2. **anspruchstabelle-beweislast** — Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen…
3. **anwaltsgeheimnis-pruefung** — Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 …
4. **beweissicherung-einstweilige-verfuegung** — Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern…
5. **chronologie** — Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253…
6. **gegenseite-status-mahnbescheid-mahnschreiben** — Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Norme…
7. **mahnbescheid** — Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Nor…
8. **mahnschreiben-aufnahme** — Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204…
9. **mahnschreiben-entwurf-anwaltsgeheimnis** — Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §…
10. **mahnschreiben-erhalten-aktualisierung** — Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 2…
11. **mandat-arbeitsbereich-abschnitt** — Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 2…
12. **mandat-aufnahme** — Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BR…
13. **mandat-briefing-schliessen-portfolio-status** — Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfra…
14. **mandat-schliessen** — Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff.…
15. **schriftsatz-abschnitt** — Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): ordnet Rolle (Mandant, Gegner, Gericht), markiert Frist (Berufung 1 Mon. § 517 ZPO), wählt Norm (ZPO, VwGO, StPO, SGG, FGO, FamFG) und Zuständigkeit (Erste Instanz / Rechtsmittelgerichte), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Prozessrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher ZPO Proz Bauleiter Eilverfahren
- `anspruchstabelle-beweislast` — Anspruchstabelle Beweislast
- `anspruchstabelle-gegenseite-interessen` — Anspruchstabelle Gegenseite Interessen
- `anwaltsgeheimnis-pruefung` — Anwaltsgeheimnis Pruefung
- `argumentationsverbesserung-red-team` — Argumentationsverbesserung RED Team
- `beweissicherung-einstweilige-verfuegung` — Beweissicherung Einstweilige Verfuegung
- `chronologie` — Chronologie
- `eilverfahren-risikoampel-und-gegenargumente` — Eilverfahren Risikoampel und Gegenargumente
- `einstweilige-verfuegung` — Einstweilige Verfuegung
- `gegenseite-mehrparteien-konflikt-und-interessen` — Gegenseite Mehrparteien Konflikt und Interessen
- `gegenseite-status-mahnbescheid-mahnschreiben` — Gegenseite Status Mahnbescheid Mahnschreiben
- `kaltstart-interview` — Kaltstart Interview
- `mahnbescheid` — Mahnbescheid
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Prozessrecht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `anspruchstabelle-beweislast`

_Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: §§ 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output: Anspruchstabelle als Grundlage für Klageschrift oder Erwiderung. Abgrenzung: nicht S..._

# Anspruchstabelle

## Zweck

Systematische Prüfung und Visualisierung aller Tatbestandsmerkmale eines zivilrechtlichen Anspruchs oder einer Einrede (z. B. § 280 Abs. 1, 3, § 281 BGB; § 823 Abs. 1 BGB; § 1 UWG) oder einer patentrechtlichen Verletzungsanalyse (Anspruchsmerkmal für Anspruchsmerkmal). Das Plugin erstellt eine Tabelle mit dem aktuellen Beweisstand, markiert Lücken und gibt Handlungsempfehlungen zur Schließung offener Punkte.

Zwei Modi:
- `--zivil`: Zivilrechtliche Ansprüche und Einreden (BGB, HGB, UWG, MarkenG etc.)
- `--patent`: Patentrechtliche Verletzungs- (§§ 9 ff. PatG) oder Nichtigkeitsanalyse (§ 22 PatG i. V. m. §§ 1–5 PatG)

## Eingaben

- Aktives Mandat (Slug)
- Modus: `--zivil [Anspruchsnorm]` oder `--patent [--verletzung | --nichtigkeit] [Patentanspruch-Nr.]`
- Relevante Dokumente (Vertrag, Korrespondenz, Zeugenliste, Sachverständigengutachten, Patentschrift, angegriffene Ausführungsform)
- Aktueller Beweisstand (was liegt vor, was ist streitig)

## Ablauf

### Modus Zivilrecht (`--zivil`)

1. **Norm zerlegen:** Tatbestandsmerkmale des Anspruchs vollständig aufführen (z. B. § 280 Abs. 1 BGB: Schuldverhältnis, Pflichtverletzung, Vertretenmüssen, Schaden, Kausalität). Einreden und Einwendungen des Gegners separat tabellarisieren.

2. **Beweisstand erfassen:** Für jedes Element: belegt/unbelegt/streitig; vorhandene Beweismittel (Urkunde, Zeugenaussage, Sachverständigengutachten, Geständnisfiktion § 138 Abs. 3 ZPO, Augenschein § 371 ZPO) eintragen.

3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

4. **Lücken markieren:** Fehlende Belege und Beweismittel als **[LÜCKE]** mit Handlungsempfehlung (z. B. "Beauftragung Sachverständiger", "Auskunftsklage § 242 BGB / § 254 ZPO", "§ 142 ZPO Antrag auf Urkundenvorlage").

5. **Gegenargumente eintragen:** Bekannte oder antizipatierte Gegenargumente in Gegenargument-Spalte.

6. **Zusammenfassung:** Gesamtbewertung des Beweisrisikos (stark / mittel / schwach) mit Begründung.

### Modus Patent (`--patent`)

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Lücken und Risiken:** Unklare Merkmale, fehlende Dokumente zur angegriffenen Ausführungsform.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Zivilrecht:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Patent:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mes, PatG, 5. Aufl. 2020, § 9 Rn. 22 ff.
- Schulte/Voß, PatG, 10. Aufl. 2017, § 9 Rn. 48 ff.

## Ausgabeformat

### Zivilrechtliche Anspruchstabelle

**Anspruch:** Schadensersatz wegen Pflichtverletzung (§§ 280 Abs. 1, 3, 281 Abs. 1 BGB)

| Nr. | Tatbestandsmerkmal | Beweislast | Beweismittel (vorhanden) | Status | Lücke / Maßnahme |
|---|---|---|---|---|---|
| 1 | Schuldverhältnis (Vertrag) | Kläger | Anlage K1 (Werkvertrag v. 12.03.2022) | ✅ belegt | – |
| 2 | Pflichtverletzung (Nichtleistung) | Kläger | Mahnung Anlage K3; Zeuge Müller | ⚠️ streitig | Bekl. bestreitet Verzug; Zugang prüfen |
| 3 | Fristsetzung (§ 281 Abs. 1) | Kläger | Anlage K3 | ⚠️ Zugang bestritten | [LÜCKE: Rückschein fehlt → Aufgabe Zustellungsnachweis] |
| 4 | Vertretenmüssen (§ 280 Abs. 1 S. 2 BGB) | Schuldner (Umkehr) | – | ✅ vermutet | Bekl. muss Exkulpation vortragen |
| 5 | Schaden | Kläger | Rechnungen Anlage K5–K7 | ✅ belegt | – |
| 6 | Kausalität | Kläger | Gutachten (§ 286 ZPO) | ⚠️ offen | [LÜCKE: SV-Gutachten erforderlich] |

**Gesamtbewertung:** Mittel – Kernproblem: Nachweis des Zugangs der Fristsetzung und Kausalitätsbeleg durch Sachverständigengutachten.

## Risiken / typische Fehler

- **Beweislastumkehr übersehen:** Bei § 280 Abs. 1 S. 2 BGB liegt Entlastungspflicht beim Schuldner; nicht als Klägeraufgabe eintragen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Patentanspruch zu weit ausgelegt:** Merkmalsanalyse muss wortsinngemäß beginnen; Äquivalenz erst im zweiten Schritt (BGH – "Schneidmesser II").
- **Auskunfts-/Stufenklage nicht berücksichtigt:** Bei fehlender Kenntnis des Schadens kann Stufenklage (§ 254 ZPO) sinnvoll sein; Anspruchstabelle sollte Auskunftsstufe separat ausweisen.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 203 StGB
- § 45 GKG
- § 115 VVG
- § 7 StVG
- § 68 GKG
- § 43 GKG
- § 3a RVG
- § 97a UrhG
- § 23 RVG
- § 4a RVG
- § 74 VwG
- § 17 StVG

### Leitentscheidungen

- BGH VI ZR 184/10
- BGH VI ZR 226/16
- BGH VI ZR 73/20

---

## Skill: `anwaltsgeheimnis-pruefung`

_Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 StGB, § 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Grenzen. Output: Prüfergebnis Anwaltsgeheimnis mit Handlungsempfehlung. Abgrenzung:..._

# Vertraulichkeitsschutz-Erstprüfung (Vorlagepflicht und Verschwiegenheit)

## Arbeitsbereich

Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: § 43a BRAO, § 203 StGB, § 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche Grenzen. Output: Prüfergebnis Anwaltsgeheimnis mit Handlungsempfehlung. Abgrenzung: nicht Datenschutz-Compliance DSGVO. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Ein Dokumentensatz im Prozess hat drei Arten von Einträgen: zweifelsfrei geschützt, zweifelsfrei nicht geschützt und die Fälle, die juristisches Urteilsvermögen erfordern. Dieser Skill sortiert die ersten beiden Kategorien, damit die Anwaltszeit vollständig für die dritte zur Verfügung steht.

**Dies ist eine Erstprüfung. Der Anwalt prüft jeden markierten Eintrag. Keine Ausnahmen.**

Hinweis: Ein direktes Pendant zum US-amerikanischen "privilege log" gibt es im deutschen Recht nicht. Dieser Skill deckt die deutschen Rechtsinstitute ab, die vergleichbare Schutzfunktionen erfüllen: Vorlagepflicht nach § 142 ZPO, Beschlagnahmeschutz nach § 97 StPO, Zeugnisverweigerungsrecht nach § 53 StPO und die anwaltliche Verschwiegenheitspflicht nach § 43a Abs. 2 BRAO, § 203 StGB.

## Eingaben

- **Dokumentenbestand** (erforderlich): Dateipfad oder im Dialog übermittelte Dokumentenliste
- **Mandatsbezeichnung (Slug)**: Zur Zuordnung in die Mandatsakte
- **Verfahrensart**: ZPO-Verfahren, StPO-Verfahren, VwGO, FGO, SGG — maßgeblich für die anwendbaren Normen
- **Kontext**: Wurde eine Urkundenvorlageanordnung nach § 142 ZPO erlassen? Liegt eine Durchsuchungs-/Beschlagnahmemaßnahme vor?

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 142 ZPO** — Anordnung der Urkundenvorlegung durch das Gericht; Voraussetzungen: erheblich und zumutbar; kein Zwang zur Vorlage, wenn Verweigerungsrecht besteht.
- **§ 144 ZPO** — Anordnung der Inaugenscheinnahme; parallele Schranken wie § 142 ZPO.
- **§ 97 StPO** — Beschlagnahmeverbote; insbesondere Abs. 1 Nr. 1: Schriftstücke des Rechtsanwalts, die Zeugnisverweigerungsberechtigten gehören; Abs. 2: Schutz von Dokumenten im Gewahrsam des Verteidigers oder Beistands.
- **§ 53 StPO** — Zeugnisverweigerungsrecht der Rechtsanwälte, Ärzte, Notare und sonstiger Berufsgeheimnisträger; gilt auch im Verfahren auf Vorlage.
- **§ 53a StPO** — Erstreckt das Zeugnisverweigerungsrecht auf berufsmäßig tätige Gehilfen.
- **§ 43a Abs. 2 BRAO** — Absolute Verschwiegenheitspflicht des Rechtsanwalts; schützt alle Informationen, die der Anwalt in Ausübung des Berufs anvertraut bekommt.
- **§ 203 Abs. 1 Nr. 3 StGB** — Strafbare Verletzung von Privatgeheimnissen durch Rechtsanwälte; stärkt § 43a BRAO strafrechtlich ab.
- **§ 160a StPO** — Schutz von Berufsgeheimnisträgern bei verdeckten Ermittlungsmaßnahmen; gilt über den Verweis für den gesamten Bereich der Beweiserhebung.

### Besonderheit: Syndikusrechtsanwalt (§ 46 BRAO)

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Schritt 0: Anwendbares Recht bestimmen

Vor der Dokumentenprüfung: Welches Verfahrensrecht gilt?

- **ZPO-Verfahren**: § 142 ZPO (Urkundenvorlage), § 144 ZPO (Inaugenscheinnahme); Weigerungsrecht nach § 142 Abs. 2 ZPO i.V.m. §§ 383, 384 ZPO.
- **StPO-Verfahren**: § 97 StPO (Beschlagnahmeverbot); § 53 StPO (Zeugnisverweigerungsrecht); § 160a StPO (Schutz bei Ermittlungsmaßnahmen).
- **VwGO/FGO/SGG**: Parallelvorschriften; Vorlagepflicht vergleichbar §§ 86, 99 VwGO; Akteneinsichtsrechte.

Quellenattribuierung: Jeden Regelhinweis und jede Entscheidung in der Ausgabe mit Herkunftsnachweis versehen: `[Primärquelle]`, `[Kommentar – prüfen]`, `[Trainingsdaten – prüfen]`. Quellen mit Prüfvermerk tragen höheres Fehlerrisiko und sollten zuerst verifiziert werden.

### Schritt 1: Formatkontrolle

Hat der Dokumentensatz die erforderlichen Angaben?

| Feld | Vorhanden? |
|---|---|
| Datum | |
| Verfasser/Urheber | |
| Empfänger (An, CC, BCC) | |
| Dokumentenart | |
| Behaupteter Schutztatbestand (Mandatsgeheimnis / Beschlagnahmeverbot / Zeugnisverweigerung) | |
| Beschreibung (ausreichend zur Beurteilung ohne Offenbarung des Geschützten) | |

Fehlende Felder → vor der inhaltlichen Prüfung zur Ergänzung markieren.

### Schritt 2: Eintrag für Eintrag

Für jeden Eintrag:

```
Eintrag [N] ([Aktenzeichen/Belegnummer]): [✅ Geschützt | ✅ Geschützt + ⚠️ Markiert | ❌ Nicht geschützt (Bewertung)]
[Bei ✅ (ohne Markierung): einzeilige Begründung mit Norm]
[Bei ✅ + ⚠️: Schutz behalten; konkrete Frage, die der Anwalt beantworten muss; Argumente pro und contra]
[Bei ❌: einzeilige Begründung — Schutz bleibt im Register, bis der Anwalt ihn entfernt]
```

**Dreistufenregel:** Der Skill entscheidet nie stillschweigend eine subjektive Schwellenwertfrage. Bei jeder unsicheren Entscheidung — Mandatsgeheimnis oder rein kaufmännischer Zweck, Beschlagnahme­schutz grenzwertig, gemischter Inhalt, Beteiligung Dritter — wird die Schutzklassifizierung beibehalten und eine ⚠️-Markierung gesetzt. Zu wenig als geschützt zu kennzeichnen öffnet die Tür zu Beweismittelverlust (einbahnige Tür); zu viel als geschützt zu kennzeichnen ist vom Anwalt korrigierbar (zweiseitige Tür). Den korrigierbaren Fehler bevorzugen.

### Schritt 3: Mustererkennung

Über den gesamten Dokumentensatz:

- Gleiche Frage wiederholt? (Z. B. dieselbe Drittpartei in 50 Einträgen — eine Entscheidung löst 50 Markierungen)
- Überklassifizierungsmuster? (Wenn alles als geschützt gekennzeichnet wird, ohne Differenzierung — dem Anwalt zur Kenntnis bringen; aber die Entscheidung zur Einschränkung liegt beim Anwalt)
- Unzureichende Beschreibungen? (So vage, dass ein Gericht eine In-Camera-Prüfung anordnen könnte)

## Vertraulichkeitsschutz-Erstprüfung: [Mandat] — [Datum]

**Anwendbare Normen:** [§ 142 ZPO / § 97 StPO / § 53 StPO / § 43a BRAO — Pinpoint-Zitate] `[UNSICHER — Aktualität prüfen]`
**Dokumente geprüft:** [N]
**Ergebnis:** [N] ✅ sicher geschützt / [N] ✅+⚠️ Schutz beibehalten & markiert / [N] ❌ Schutzentfernung empfohlen (Anwalt bestätigt)

### ✅ + ⚠️ Markiert — Schutz beibehalten, Anwalt entscheidet

| Eintrag | Belegnummer | Frage | Pro Schutz | Contra Schutz | Zu klärende Entscheidung |
|---|---|---|---|---|---|
| [N] | [Bereich] | [Was subjektiv ist] | [eine Zeile] | [eine Zeile] | [konkrete zu treffende Entscheidung] |

### ❌ Schutzentfernung empfohlen (Anwalt bestätigt vor Streichung)

| Eintrag | Belegnummer | Begründung |
|---|---|---|

*Vermerkt, nicht vollzogen. Der Skill entfernt keine Schutzklassifizierungen aus dem Register — das tut der Anwalt nach Prüfung.*

### ✅ Geschützt (kein Handlungsbedarf)

[Anzahl. Liste auf Anfrage abrufbar.]

### Musterbeobachtungen

[Wiederkehrende Fragen, Überklassifizierung, Beschreibungsprobleme]

### Markierungsdisziplin

- `[PRÜFEN: Sachaussage über Dokument/Verfasser/Datum]`
- `[UNSICHER: Grenzfall Schutztatbestand / Beschlagnahme / Reichweite]`
- `[BELEG FEHLT: Norm, lokale Variante oder Entscheidung als Stütze]`

---

**Anwalt muss alle ⚠️- und ❌-Einträge vor jeder Maßnahme prüfen.**

**Schutzwürdigkeit des Ausgabedokuments:** Diese Prüfung liest per definitionem schutzkandidaten-fähige Unterlagen. Das Ausgabedokument erbt diesen Status — es ist mit dem Mandatsmaterial zu verwahren, entsprechend zu kennzeichnen und nicht außerhalb des Vertrauenskreises zu verbreiten. Eine Weitergabe kann selbst den Schutz aushöhlen.
```

## Beispiel

**Sachverhalt:** Anordnung nach § 142 ZPO; Gericht verlangt Vorlage aller E-Mails zwischen der Partei und ihrem Rechtsanwalt zu einer Schadensersatzforderung.

**Erstprüfungsergebnis:**
- ✅ 12 E-Mails: Mandatsgeheimnis (§ 43a Abs. 2 BRAO); Anwalt bittet um Rechtsrat, Anwalt erteilt Rat; keine Drittpartei im Verteiler.
- ✅+⚠️ 3 E-Mails: Anwalt in CC bei rein kaufmännischer Verhandlung; dominanter Zweck unklar → Anwalt entscheidet.
- ❌ 2 E-Mails: Keine anwaltliche Beteiligung; CC an Anwalt ohne rechtliche Substanz; Bewertung: kein Schutz nach § 43a BRAO.

## Risiken und typische Fehler

- **Syndikusanwalt-Grenzfälle:** Die Schutzwürdigkeit von Korrespondenz des Syndikusrechtsanwalts hängt von seiner konkreten Funktion im Einzelfall ab (§ 46 Abs. 3 BRAO) — nie pauschal als "sicher geschützt" klassifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wirkung der Weitergabe:** Wird ein eigentlich geschütztes Dokument im Verfahren vorgelegt (auch versehentlich), kann der Schutz vollständig entfallen — Rückruf ist möglich, aber keineswegs sicher.
- **Beschreibungstiefe:** Zu vage Beschreibungen können dazu führen, dass das Gericht eine In-Camera-Vorlage zur eigenen Prüfung anordnet.
- **Fehlende Quellenverifizierung:** Alle Normen- und Entscheidungshinweise in der Ausgabe sind KI-generiert; vor einer Einreichung sind sie gegen Primärquellen (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, Wolters Kluwer) zu verifizieren.

## Quellenpflicht

- Gesetzestexte: §§ 142, 144 ZPO; §§ 53, 53a, 97, 160a StPO; §§ 43a, 46 BRAO; § 203 StGB; §§ 86, 99 VwGO
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

## Skill: `beweissicherung-einstweilige-verfuegung`

_Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: §§ 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl, Verfahrensablauf. Output: Antrag auf selbständiges Beweisverfahren. Abgrenzung..._

# Aufbewahrungspflicht und Beweissicherung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktives Mandat (Slug)
- Modus: `--anordnen`, `--aktualisieren`, `--aufheben`, `--status`
- Betroffene Dokumentenkategorien und Custodians (Personen/Abteilungen, die Dokumente halten)
- Aufbewahrungsanlass: laufendes Verfahren / angekündigtes Verfahren / Behördenanfrage

## Ablauf

### 1. Aufbewahrungspflichten prüfen

**Handels- und steuerrechtliche Pflichtfristen:**
| Kategorie | Frist | Rechtsgrundlage |
|---|---|---|
| Handelsbücher, Inventare, Jahresabschlüsse | 10 Jahre | § 257 Abs. 4 HGB |
| Buchungsbelege | 10 Jahre | § 257 Abs. 4 HGB, § 147 Abs. 3 AO |
| Handels- und Geschäftsbriefe | 6 Jahre | § 257 Abs. 4 HGB |
| Sonstige steuerlich relevante Unterlagen | 6 Jahre | § 147 Abs. 1 Nr. 5 AO |
| Lohnunterlagen (SV-relevant) | 10 Jahre | § 28f Abs. 2 SGB IV |

**Prozessuale Aufbewahrungspflicht:**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Konsequenzen der Beweisvereitelung:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 286 ZPO: Freie Beweiswürdigung kann vernichtungsbedingte Nachteile zulasten der vernichtenden Partei ziehen.
- §§ 339 ff. StGB: Strafbarkeit wegen Beweisvereitelung / Urkundenunterdrückung (§ 274 StGB) bei vorsätzlicher Vernichtung.

### 2. Beweissicherungs-Anordnung erstellen (`--anordnen`)

Inhalt der Anordnung:
- Adressaten (Custodians): Namen, Funktion, Abteilung
- Betroffene Dokumentenarten: E-Mails, Verträge, Buchungsbelege, CAD-Dateien, Systemlogs
- Zeitraum der zu sichernden Unterlagen
- Löschverbot: Ausdrückliches Verbot, betreffende Daten zu löschen, zu überschreiben oder zu ändern
- Aufbewahrungsort und -format
- Überprüfungsintervall
- Kontaktperson für Rückfragen
- Geltungsdauer / Aufhebungsvorbehalt

### 3. Selbständiges Beweisverfahren (§§ 485 ff. ZPO)

Wenn Beweismittel außerhalb des Prozesses gesichert werden müssen (z. B. drohende Veränderung von Sachzustand, Mängel, Bauschäden):

- Antrag nach § 485 ZPO: Beantragung der Beweissicherung durch das Prozessgericht (oder nach § 486 ZPO beim Amtsgericht des Ortes)
- Inhalt: Beweisthema, Beweismittel (Sachverständiger, Augenschein), Benennung des Antragsgegners
- Wirkung: Gutachten bindet das spätere Prozessgericht grundsätzlich (§ 493 ZPO)
- Fristen: §§ 486 Abs. 2, 487 ZPO

### 4. Statusbericht (`--status`)

Tabelle aller aktiven Sicherungsanordnungen im Portfolio mit:
- Mandat-Slug
- Datum der Anordnung
- Betroffene Custodians
- Überprüfungsdatum
- Aufhebungsvoraussetzungen

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 257 HGB; § 147 AO (Aufbewahrungsfristen).
- § 274 StGB (Urkundenunterdrückung), § 339 StGB (Rechtsbeugung, nur für Richter und Beamte).

## Ausgabeformat

### Beweissicherungs-Anordnung

```
BEWEISSICHERUNGS-ANORDNUNG
Mandat: [Slug]
Datum: TT.MM.JJJJ
Erstellt von: [Anwalt]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO / § 203 StGB

──────────────────────────────────────────────
ANORDNUNG ZUR AUFBEWAHRUNG VON UNTERLAGEN
──────────────────────────────────────────────

An: [Name, Funktion, Abteilung]

Betreff: Aufbewahrungspflicht im Zusammenhang mit [Sachverhaltskurzbezeichnung]

Aufgrund eines bevorstehenden / laufenden Rechtsstreits [Aktenzeichen oder Sachverhalt]
ordnen wir an, folgende Unterlagen bis auf Weiteres aufzubewahren:

Betroffene Dokumente:
1. Alle E-Mails und sonstigen Korrespondenzen betreffend [Thema] ab [Datum]
2. Verträge und Anlagen zu [Projekt]
3. [weitere Kategorien]

LÖSCHVERBOT: Es ist untersagt, die oben bezeichneten Unterlagen zu löschen, zu
vernichten, zu überschreiben oder anderweitig unzugänglich zu machen.

Nächste Überprüfung: TT.MM.JJJJ
Kontakt: [Anwalt, Kanzlei, Telefon]
```

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Zu enger Anwendungsbereich:** Custodians und Dokumentenkategorien zu eng gewählt; alle betroffenen Abteilungen und IT-Systeme (E-Mail-Archiv, Cloud-Speicher) einschließen.
- **Datenschutzkollision:** Aufbewahrungspflicht und DSGVO-Löschpflicht können kollidieren; bei Widerspruch gilt prozessuale Sicherungspflicht im Zweifel (vgl. Art. 17 Abs. 3 lit. e DSGVO: Aufbewahrung für Rechtsstreitigkeiten).
- **Selbständiges Beweisverfahren zu spät:** Nach Sachzustandsveränderung ist keine Beweissicherung mehr möglich; § 485 ZPO-Antrag frühzeitig stellen.

<!-- AUDIT 27.05.2026 bundle_040
-->

---

## Skill: `chronologie`

_Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: §§ 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige Tatsachen. Output: Tabellarische Sachverhaltschronologie. Abgrenzung: nicht vollstä..._

# Sachverhalts-Chronologie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Erstellung

1. **Modus:** Arbeitschronologie (intern, vollständig), Schriftsatz-Chronologie (aufbereitet) oder Zeugenchronologie (gefültert)?
2. **Dokumentenbasis:** Liegen die Quellen vor (Verträge, E-Mails, Schriftsätze, Anlagen)?
3. **Zeitraum:** Welcher Zeitraum ist mandatsrelevant — gibt es einen frühesten relevanten Stichtag?
4. **Lücken:** Gibt es bekannte Zeiträume, für die keine Dokumente vorliegen?
5. **Prozessuale Funktion:** Für Sachverhaltsdarstellung (§ 253 ZPO), Zeugenvernehmung (§§ 373 ff. ZPO) oder Berufungsbegründung (§ 520 Abs. 3 ZPO)?

## Zentrale Normen
- § 253 Abs. 2 Nr. 1 ZPO (Anforderungen an die Klageschrift — vollständiger Sachvortrag)
- § 138 ZPO (Erklärungspflicht der Parteien — Vollständigkeit und Wahrheitspflicht)
- § 373 ff. ZPO (Zeugenbeweis — Grundlage der Zeugenchronologie)
- § 520 Abs. 3 ZPO (Berufungsbegründung — tatsächliche Angaben)
- § 286 ZPO (Freie Beweiswuerdigung — Chronologie als Hilfsmittel)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Aufbau einer mandatsbezogenen Sachverhalts-Chronologie aus vorliegenden Dokumenten, Schriftsätzen, Verträgen, E-Mails und Anlagen. Die Chronologie dient als Grundlage für Sachverhaltsdarstellungen im Schriftsatz (§ 253 Abs. 2 Nr. 1 ZPO), Zeugenvernehmungsvorbereitung (§§ 373 ff. ZPO), Berufungsbegründung (§ 520 Abs. 3 ZPO) und interne Mandatsbriefings.

Drei Modi:
- **Arbeitschronologie** – intern, vollständig, mit Lückenmarkierungen
- **Sachverhaltsdarstellungs-Chronologie** – aufbereitet für den Schriftsatz, urteilsstilgerecht
- **Zeugenchronologie** – gefiltert auf einen bestimmten Zeugen für Vernehmungsvorbereitung

## Eingaben

- Aktives Mandat (Slug)
- Hochgeladene Dokumente: Verträge, Korrespondenz, E-Mails, Protokolle, Rechnungen, Sachverständigengutachten, Gerichtsentscheidungen
- Wahl des Modus: `--arbeits` | `--sachverhalt` | `--zeuge=[Name]`
- Optional: bekannte Schlüsseldaten (z. B. Vertragsschluss, Fälligkeitsdatum, Kündigungserklärung)

## Ablauf

1. **Dokumente parsen:** Alle hochgeladenen Dateien auf datierte Ereignisse scannen. Datum, Uhrzeit (soweit angegeben), Ereignisbeschreibung, Quelle (Dokumentenbezeichnung, Anlage-Nr.) und beteiligte Personen extrahieren.

2. **Deduplizierung:** Gleiche Ereignisse aus verschiedenen Quellen zusammenführen; Widersprüche markieren als `[WIDERSPRUCH: Quelle A gibt X an, Quelle B gibt Y an]`.

3. **Mandatstheorien-Tagging:** Jedes Ereignis nach Relevanz für die Mandatstheorie markieren:
 - 🔑 Kernereig­nis (unmittelbar anspruchsbegründend oder -ausschließend)
 - ⚠️ Risikopunkt (könnte gegen Mandantin sprechen)
 - 📎 Hintergrundinformation
 - ❓ Ungeklärt / Beleg fehlt

4. **Lücken identifizieren:** Zeiträume ohne belegte Ereignisse und inhaltliche Lücken (z. B. fehlende Zugangsbestätigung, unklare Übergabe) als `[LÜCKE: Zeitraum MM/JJJJ bis MM/JJJJ – kein Beleg]` markieren.

5. **Modus anwenden:**
 - *Arbeitschronologie:* Vollständige Liste mit Quellenangaben und Anmerkungen.
 - *Sachverhaltsdarstellung:* Fließtext im Urteilsstil, Ereignisse in der dritten Person, Beweisquellen als Fußnoten.
 - *Zeugenchronologie:* Nur Ereignisse mit Beteiligung des Zeugen; Ergänzung um mögliche Wissenslücken des Zeugen.

6. **Versionierung:** Neue Chronologien als `chronology-v[N].md` im Mandatsordner speichern.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken / typische Fehler

- **Unklarer Zugangszeitpunkt:** Zugangsnachweis für Mahnungen und Fristsetzungen ist entscheidend für Verzugsbeginn (§ 286 Abs. 1 BGB); fehlende Belege zwingend als Lücke markieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Veraltete Chronologie:** Nach jedem Mandat-Update (`/mandat-update`) die Chronologie ergänzen; veraltete Versionen archivieren.
- **Zeugenchronologie zu weit gefasst:** Nur mandatsrelevante Ereignisse einbeziehen; nicht alle Ereignisse, an denen der Zeuge beteiligt war.
- **Datenschutz:** Personenbezogene Daten Dritter nur soweit erforderlich; DSGVO-Minimierungsgrundsatz (Art. 5 Abs. 1 lit. c DSGVO) beachten.

---

## Skill: `gegenseite-status-mahnbescheid-mahnschreiben`

_Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: §§ 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz, Sicherheitsleistung. Output: Statusbericht Gegenseite. Abgrenzung: nicht Streitwert oder An..._

# Statusabfrage Externe Bevollmächtigte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Mandatsprotokoll `_log.yaml`**: Filterquelle und Feldquelle
- **`akte.md` und `verlauf.md`** je Mandat: Mandatskontext und aktuelle Entwicklungen
- **Kanzleikonfiguration `CLAUDE.md`**: Direktive für externe Bevollmächtigte (Tonvorgabe), Unterzeichner, Budgethaltung
- **Flags** (optional): `--alle`, `--slug=[bezeichnung]`, `--kein-outlook`

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 4 BRAO** — Anwaltliche Fortbildungs- und Berichterstattungspflicht gegenüber dem Mandanten; regelmäßige Rückmeldung der externen Bevollmächtigten ist Teil der ordnungsgemäßen Mandatsführung.
- **§ 667 BGB** — Auskunftspflicht des Beauftragten; der externe Bevollmächtigte hat dem Auftraggeber auf Verlangen Auskunft zu erteilen; die wöchentliche Statusanfrage ist Ausfluss dieses Anspruchs.
- **§ 43a Abs. 2 BRAO** — Vertraulichkeit; die Statuskorrespondenz mit externen Bevollmächtigten ist durch die gemeinsame Verschwiegenheitspflicht geschützt.
- **§ 49b BRAO; §§ 2 ff. RVG** — Vergütung; Budgetanfragen und Kostenkontrollen im Statusschreiben orientieren sich am vereinbarten Honorar und etwaigen Vergütungsrahmen.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Schritt 1: Mandate filtern

**Standardfilter:**

- `status != geschlossen`
- `externe_bevollmaechtigte.sozietaet != null` UND `externe_bevollmaechtigte.partner != null`
- Entweder: letzte Aktualisierung vor mehr als 10 Tagen ODER `nächste_frist` innerhalb von 21 Tagen

Übersprungen werden: Mandate mit Update in den letzten 10 Tagen (kein erneutes Anschreiben erforderlich) sowie Mandate ohne hinterlegte E-Mail-Adresse des externen Bevollmächtigten (Markdown-Entwurf wird trotzdem erstellt; Outlook-Entwurf nicht).

**Flags:**
- `--alle` → Entwurf für alle aktiven Mandate, unabhängig von der Aktualität
- `--slug=[bezeichnung]` → Entwurf nur für ein Mandat (Ad-hoc-Anfrage)
- `--kein-outlook` → kein Outlook-Entwurf, auch wenn MCP verfügbar

### Schritt 2: Je Mandat — E-Mail-Entwurf erstellen

Jede E-Mail folgt demselben Grundgerüst; Inhalt ist mandatsspezifisch.

**Betreff:** gemäß Kanzleidirektive (Fallback: `[Mandat: [Bezeichnung]] — Wöchentlicher Sachstand`)

**Rumpf-Gerüst:**

```
[Vorname des Partneranwalts],

[Ein einleitender Satz — natürlich, entspricht dem Kanzleiston.]

Kurze Rückmeldung zu [Mandatsbezeichnung] erbeten. Einige Punkte:

1. **Sachstand seit [Datum der letzten Aktualisierung aus verlauf.md]** — Was hat sich bewegt, was ist noch offen? Gab es Schriftsätze, Termine, Korrespondenz oder Telefonate seit unserem letzten Austausch?

2. **Bevorstehende Fristen** — Ich vermerke [nächste_frist aus Protokoll + etwaige Fristen aus akte.md]. Bitte Abdeckungsplan bestätigen und ggf. weitere Termine mitteilen.

3. **Ausstehende Entscheidungen** — [offene Fragen aus akte.md, die externen Input erfordern; entfällt, falls keine vorhanden — umnummerieren]

4. **Budget** — [monatlich / quartalsweise / auf Anfrage gemäß Kanzleikonfiguration]. Wo stehen wir gegenüber [Budgetrahmen aus akte.md]? Gibt es Abweichungen?

[Falls wesentlich und relevant: 5. Konkrete Bitte — z. B. "Bitte Entwurf des Schriftsatzes vor [Datum] übersenden" — aus offenen Punkten in akte.md.]

[Grußformel — Name, Funktion, Kontakt. Aus Kanzleikonfiguration.]
```

Ton wird der Kanzleidirektive angepasst — einige Kanzleien schreiben förmlich, andere per Vorname und Stichpunkte. Die Direktive hat Vorrang.

### Schritt 3: Ausgabe erstellen

### Schritt 4: Abschicken-Schranke

Jedem Entwurf wird folgender Hinweis angefügt (vor dem Versenden entfernen):

> Dies ist ein Entwurf zur anwaltlichen Prüfung vor dem Versand an externe Bevollmächtigte. Prüfen Sie auf privilegierte Inhalte, die nicht aus dem Mandatsverhältnis herausgegeben werden sollten, sachliche Richtigkeit, Ton und Budgethaltung. Auch routinemäßige Wochenanfragen können Strategie, Positionierungen oder unbeabsichtigte Zugeständnisse enthalten.

## Entwurf erstellt für

| Mandat | Externer Partner | Zuletzt aktualisiert | Grund der Aufnahme |
|---|---|---|---|
| [slug] | [Partner] | [Datum] | [veraltet / bevorstehende Frist / --alle / --slug] |

## Übersprungen

| Mandat | Grund |
|---|---|
| [slug] | aktuelles Update (zuletzt bearbeitet [Datum]) |
| [slug] | keine E-Mail des externen Bevollmächtigten im Protokoll — nachtragen mit `/mandat-update [slug]` |

## Auffälligkeiten

- Mandate ohne externe Bevollmächtigte: [Liste — bei hohem/kritischem Risiko gesondert markiert]
- Mandate mit externen Bevollmächtigten, aber ohne E-Mail-Adresse: [Liste]
```

## Beispiel

**Sachverhalt:** Mandat `bauer-ag-berufung-2025`, OLG Hamburg. Letztes Update vor 14 Tagen. Nächste Frist: Berufungserwiderung in 18 Tagen. Externer Partner: RA Dr. Schneider, Schneider & Partner.

**Ergebnis:** Entwurf mit Statusanfrage zu eingereichten Schriftsätzen seit letztem Austausch, Bestätigung der Berufungserwiderungsfrist, Budget-Abfrage gemäß Quartals-Direktive. Gespeichert unter `gegenseite-status/2025-05-12/bauer-ag-berufung-2025.md`.

## Risiken und typische Fehler

- **Vertraulichkeit:** Die Statuskorrespondenz mit externen Bevollmächtigten ist durch § 43a Abs. 2 BRAO geschützt; Entwürfe nicht an Personen außerhalb des Mandatskreises weitergeben.
- **Nicht geprüfte Entwürfe versenden:** Auch kurze Statusanfragen können strategische Hinweise, Budgetkonzessionen oder unbeabsichtigte Zugaben enthalten.
- **Veraltete Kontaktdaten:** Falls die E-Mail des externen Partners nicht im Protokoll hinterlegt ist, wird kein Outlook-Entwurf angelegt; der Nutzer erhält einen Hinweis, die Daten nachzupflegen.
- **Mandatsübergreifende Abfrage:** Nur bei aktivem `Mandatsübergreifender Kontext: an` in der Kanzleikonfiguration darf das System mandatsübergreifend lesen.

## Quellenpflicht

- Gesetzestexte: §§ 43a, 49b BRAO; §§ 2 ff. RVG; § 667 BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

## Skill: `mahnbescheid`

_Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: §§ 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung, Widerspruchsrecht des Schuldners. Output: Mahnbescheidsantrag-Entwurf. Abgrenzung: nicht Kla..._

# Mahnverfahren – §§ 688 ff. ZPO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Verweis auf das freistehende Plugin `zwangsvollstreckung`

Für den operativen Mahnantrag (Barcode-Datensatz, zentrales Mahnportal, EGVP/beA-Übermittlung) und
den Übergang zum Vollstreckungsbescheid samt Klausel und Zustellung lädt das freistehende Plugin
`zwangsvollstreckung` die Skills `zv-mahnbescheid-online` und `zv-vollstreckungsbescheid-folge`.
Liefert die dogmatische Grundlage und Strategie; das Plugin liefert das fertige
Formularpaket.

## Eingaben

Das Modell benötigt:

1. **Forderungsdetails**: Hauptforderung (Betrag, Entstehungsgrund), Zinsen (Verzugszinsen
 § 288 BGB; bei Verbraucher 5 % über Basiszinssatz, bei Unternehmer 9 % über Basiszinssatz),
 Mahnkosten, Auslagen
2. **Parteien**: Name, Anschrift, Rechtsform von Antragsteller und Antragsgegner
3. **Zuständigkeit**: Wohnsitz/Sitz des Antragsgegners → zuständiges Mahngericht (§ 689 ZPO)
4. **Aktuelle Situation**: Liegt bereits ein Mahnbescheid vor? Wurde Widerspruch eingelegt?
 Ist Vollstreckungsbescheid beantragt?
5. **Verjährungsstand**: Wann ist die Forderung fällig geworden? Verjährung droht?

## Rechtlicher Rahmen

### Normen

- **§ 688 ZPO** – Zulässigkeit des Mahnverfahrens (nur Geldforderungen; keine bedingten
 Forderungen; nicht gegen unbekannte Erben)
- **§ 689 ZPO** – Zuständigkeit (zentrale Mahngerichte der Länder; in Bayern: AG Coburg)
- **§ 690 ZPO** – Inhalt des Mahnantrags (Pflichtangaben: Parteien, Forderung, Zinsen,
 Entstehungsgrund kurz bezeichnet)
- **§ 692 ZPO** – Erlass des Mahnbescheids ohne Sachprüfung
- **§ 694 ZPO** – Widerspruch gegen den Mahnbescheid (binnen 2 Wochen ab Zustellung)
- **§ 696 ZPO** – Abgabe an das Streitgericht nach Widerspruch
- **§ 699 ZPO** – Antrag auf Vollstreckungsbescheid (nach Ablauf der Widerspruchsfrist oder
 nach Nicht-Einlegung des Widerspruchs; max. 6 Monate nach Zustellung des Mahnbescheids)
- **§ 700 ZPO** – Einspruch gegen den Vollstreckungsbescheid (2 Wochen ab Zustellung;
 § 700 Abs. 1 ZPO: VB steht einem Versäumnisurteil gleich)
- **§ 701 ZPO** – Weiteres Verfahren nach Einspruch
- **§ 204 Abs. 1 Nr. 3 BGB** – Verjährungshemmung durch Mahnantrag (ab Eingang beim Gericht)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 durch Mahnbescheid; § 204 Abs. 1 Nr. 3 BGB setzt voraus, dass die Forderung im Mahnantrag
 ausreichend individualisiert ist; pauschale Sammelbezeichnungen genügen nicht und hemmen
 die Verjährung nicht.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 anforderung im Mahnverfahren; der Entstehungsgrund muss so bezeichnet sein, dass der
 Antragsgegner die Forderung zuordnen kann; Verweis auf "Lieferscheine" ohne Nummer
 unzureichend.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

1. **Zulässigkeitsprüfung** (§ 688 ZPO): Ist die Forderung eine bezifferte Geldforderung?
 Keine aufschiebende Bedingung? Kein Auslandsaufenthalt des Antragsgegners (§ 688 Abs. 2 ZPO)?
2. **Verjährungsprüfung** (§§ 195, 199 BGB): Verjährungsfrist bereits abgelaufen oder kurz
 vor Ablauf? → Sofortiger Mahnantrag zur Hemmung (§ 204 Abs. 1 Nr. 3 BGB).
3. **Mahnantrag** (§ 690 ZPO) über www.online-mahnantrag.de:
 - Pflichtangaben: Antragsteller/Gegner (vollständig), Forderungsbetrag, Entstehungsgrund
 (Vertragstyp + Datum), Zinsen (Fälligkeitsdatum + Zinssatz), Gerichtsgebühr (§ 12 GKG)
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Erlass und Zustellung** (§§ 692, 693 ZPO): Gericht erlässt MB ohne Sachprüfung; Zustellung
 an Antragsgegner; 2-Wochen-Frist für Widerspruch beginnt.
5. **Widerspruch** (§ 694 ZPO): Binnen 2 Wochen → Abgabe an Streitgericht (§ 696 ZPO);
 Antragsteller muss innerhalb 1 Monat Kostenvorschuss einzahlen, sonst Rücknahmefiktion.
6. **Kein Widerspruch** → Antrag auf Vollstreckungsbescheid (§ 699 ZPO) innerhalb 6 Monaten;
 VB wird zugestellt; Einspruchsfrist 2 Wochen (§ 700 ZPO).
7. **Einspruch gegen VB** (§ 700 ZPO): Verfahren wie nach Widerspruch; VB gilt als
 Versäumnisurteil (§ 700 Abs. 1 ZPO).
8. **Vollstreckung**: VB ohne Einspruch → Vollstreckungsklausel beantragen (§§ 724 ff. ZPO);
 Pfändung oder Forderungspfändung einleiten (→ Skill vollstreckung).

## Beispiel

**Sachverhalt**: Handwerksbetrieb H hat Malerarbeiten für Vermieter V erbracht und eine Rechnung
über EUR 4.850,00 (fällig 01.12.2024) gestellt. V zahlt nicht; ein außergerichtliches Mahnschreiben
blieb erfolglos.

**Prüfung (Urteilsstil)**:

Das Mahnverfahren ist statthaft (§ 688 Abs. 1 ZPO): Die Forderung ist auf Zahlung einer
bestimmten Geldsumme gerichtet; keine aufschiebende Bedingung; V hat Wohnsitz in Deutschland.

*Individualisierung (§ 690 Abs. 1 Nr. 3 ZPO)*: Als Entstehungsgrund ist einzutragen: "Werklohn
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(§ 288 Abs. 2 BGB, da V Unternehmer).

*Verjährung*: Die Forderung entstand 2024; Regelverjährung 3 Jahre (§ 195 BGB), Beginn
01.01.2025. Kein Handlungsbedarf, aber Mahnantrag hemmt Verjährung ab Eingang (§ 204 Abs. 1
Nr. 3 BGB), was vorsorglich zu nutzen ist.

## Risiken und typische Fehler

- **Unzureichende Individualisierung**: Verjährungshemmung tritt nicht ein; Vollstreckungsbescheid
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Versäumte 6-Monatsfrist** für VB-Antrag: Mahnbescheid verliert Wirkung; neues Verfahren
 erforderlich; Verjährungshemmung endet (§ 204 Abs. 2 BGB).
- **Falsche Zinsen**: § 288 Abs. 1 vs. Abs. 2 BGB (Verbraucher vs. Unternehmer);
 zu hoch angesetzte Zinsen führen zu Teilvollstreckungsschutz.
- **Auslands-Antragsgegner**: § 688 Abs. 2 Nr. 2 ZPO – Mahnverfahren unzulässig →
 Klage erforderlich.
- **Berufsrecht**: Mandantendaten (Forderungsunterlagen) nur in verschlüsselter Form
 übermitteln (§ 43a Abs. 2 BRAO, § 203 StGB).

## Quellenpflicht

Jede Aussage zu Zulässigkeit, Inhalt des Mahnantrags und Verjährungswirkung ist nach
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rn.). Kommentare mit Bearbeiter, Werk, Aufl., §, Rn. Keine allgemeinen Pauschalverweise.

---

<!-- AUDIT-HINWEIS 27.05.2026: Halluzinierte BGH-Zitate entfernt (NOT_FOUND oder WRONG_TOPIC gemaess dejure.org-Pruefung). Betroffene AZ siehe inline-Kommentare. Frontmatter unveraendert. -->

---

## Skill: `mahnschreiben-aufnahme`

_Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: §§ 204 212 BGB, § 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output: Einordnungsnotiz und Empfehlung Reaktion. Abgrenzung: nicht eigenes Mahnschreiben ers..._

# Mahnschreiben-Intake

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor dem Intake

1. **Forderungsart:** Kaufpreis, Werkverguetung, Schadensersatz, Darlehensrueckzahlung oder sonstiger Anspruch?
2. **Faelligkeit:** Ist die Forderung bereits fällig und durchsetzbar (§ 271 BGB)?
3. **Verjährung:** Ist die dreijährige Regelverjährung (§ 195 BGB) gewährt oder droht sie?
4. **BATNA:** Was ist die beste Alternative zum Mahnschreiben (gerichtliches Mahnverfahren, Klage, Verhandlung)?
5. **Vertraulichkeitsfilter:** Dürfen mandatsbezogene Daten in das eingesetzte KI-System eingespielt werden?

## Zentrale Normen
- § 271 BGB (Fälligkeit)
- § 286 BGB (Verzug — Mahnungserfordernis)
- § 288 BGB (Verzugszinsen)
- § 291 BGB (Prozesszinsen)
- § 195 BGB (Regelverjährung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Neuer Slug oder vorhandenes Mandat (Slug)
- Optional: `--full` für vollständigen erweiterten Intake (inkl. BATNA, Prozesskostenrisiko, Streitwertschätzung)

## Ablauf

1. **Mandantenidentifikation:**
 - Vollständiger Name / Firma, Anschrift, Kontaktperson
 - Mandantentyp: Verbraucher (§ 13 BGB) oder Unternehmer (§ 14 BGB) – für Verzugszinsberechnung relevant (§ 288 Abs. 1 vs. 2 BGB)

2. **Schuldneridentifikation:**
 - Vollständiger Name / Firma, Anschrift, HRB-Nummer (bei Gesellschaften)
 - Zustellungsfähige Anschrift vorhanden? (für spätere Klagezustellung, § 253 Abs. 2 Nr. 1 ZPO)
 - Ist die Passivlegitimation des Schuldners geklärt? (z. B. bei Gesamtschuld § 421 BGB, Rechtsnachfolge, Konzernmutter)

3. **Sachverhaltserfassung:**
 - Wie kam das Schuldverhältnis zustande? (Vertragsurkunde vorhanden?)
 - Was wurde nicht geleistet oder schlecht geleistet?
 - Wann war Leistung fällig?
 - Hat der Mandant bereits gemahnt? (schriftlich / mündlich / konkludent – relevant für § 286 Abs. 1 BGB)
 - Gab es Reaktionen des Schuldners (Einwände, Aufrechnungen, Minderung)?

4. **Forderungserfassung:**
 - Hauptforderung (Betrag, Art, Rechtsgrundlage)
 - Nebenforderungen: Verzugszinsen (§ 288 BGB), vorgerichtliche Anwaltskosten (§ 13 RVG i. V. m. VV 2300), Schadensersatz (§§ 280, 281 BGB)
 - Fälligkeitsdatum und bisherige Mahnungen (mit Datum)
 - Offene Restforderung (nach Teilzahlungen)

5. **Hebel und Risiko (BATNA):**
 - Was ist die beste Alternative des Mandanten ohne Mahnschreiben?
 - Welche Risiken bestehen (Aufrechnung, Gegenansprüche, Insolvenzrisiko)?
 - Ist ein Güteantrag (§ 15a EGZPO) im zuständigen Bundesland Pflicht?
 - Empfiehlt sich ein Mahnbescheid (§§ 688 ff. ZPO) statt Mahnschreiben?

6. **Vertraulichkeitsfilter:**
 - Enthält der Sachverhalt vertrauliche Informationen Dritter, die nicht in das Schreiben dürfen?
 - Besteht Zeugnisverweigerungsrecht des Mandanten für bestimmte Tatsachen?

7. **Intake-Datei schreiben:** `demand-letters/[slug]/intake.md` mit allen Feldern befüllen. Fehlende Pflichtfelder markieren.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken / typische Fehler

- **Fehlende Passivlegitimation:** Bei GmbH-Schuldner Handelsregisterauszug abrufen; Insolvenzantrag prüfen (InsO § 17 ff.) – Mahnung an insolventen Schuldner ist sinnlos.
- **Gesamtschuldner übersehen:** Bei mehreren Schuldnern (§ 421 BGB) alle mahnen, um Verjährungshemmung (§ 213 BGB) zu bewirken.
- **Verjährung prüfen:** Intake prüft automatisch die Regelverjährung (§§ 195, 199 BGB: 3 Jahre zum 31.12.); kürzere Sonderfristen (§ 438 BGB: 2 Jahre für Mängelansprüche; § 548 BGB: 6 Monate für Vermieter; § 195 ff. BGB) gesondert markieren.
- **Unterlassungsaufforderung ohne Vertragsstrafe:** Abmahnungen nach UWG, UrhG, MarkenG müssen eine Unterlassungs- und Verpflichtungserklärung mit Vertragsstrafeversprechen enthalten; fehlt dies, kann der Abgemahnte eine nicht der Kostenfolge des § 97a UrhG entsprechende Erklärung abgeben.

---

## Skill: `mahnschreiben-entwurf-anwaltsgeheimnis`

_Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: §§ 286 288 BGB, §§ 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung. Output: Mahnschreiben-Entwurf mit Fristsetzung. Abgrenzung: nicht Mahnbescheid (ge..._

# Mahnschreiben / Vorgerichtliche Aufforderung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Entwurf eines anwaltlichen Mahnschreibens (§ 286 Abs. 1 BGB) oder einer qualifizierten vorgerichtlichen Aufforderung mit Fristsetzung. Einsetzbar für Zahlungsverzug, Pflichtverletzungen, Mängelrügen (§ 281 Abs. 1 BGB) und Unterlassungsaufforderungen (§ 8 Abs. 1 UWG, § 97 Abs. 1 UrhG, § 14 Abs. 5 MarkenG). Das Schreiben ist anwaltlich unterzeichnet und nach § 13 RVG abrechenbar.

## Eingaben

- Abgeschlossenes `mahnschreiben-aufnahme.md` im Mandatsordner (Slug)
- Gewünschter Schriftsatztyp: `--zahlungsverzug`, `--mängelrüge`, `--unterlassung`, `--schadensersatz`
- Optional: `--version=N` für Versionierung bei Überarbeitungen
- Optional: `--skip-gate` – Pflicht-Checkliste überspringen (nur mit expliziter Bestätigung)

## Ablauf

1. **Intake laden:** `demand-letters/[slug]/intake.md` einlesen. Fehlende Pflichtfelder als Fehler ausgeben; kein Entwurf ohne vollständigen Intake.

2. **Pflicht-Checkliste (Gate) – vor dem Entwurf:**
 - [ ] Ist die Forderung dem Grunde nach schlüssig dargetan (§ 286 Abs. 1 BGB)?
 - [ ] Ist der Schuldner eindeutig identifiziert (Name, Anschrift, ggf. Handelsregisternummer)?
 - [ ] Ist der Betrag oder die geschuldete Handlung konkret bezeichnet?
 - [ ] Ist die Frist angemessen (i. d. R. 2 Wochen; bei Baurecht oder komplexen Leistungen ggf. länger)?
 - [ ] Sind Verzugsschäden (§ 288 BGB: 5 % über Basiszinssatz bei Verbrauchern; 9 % bei Unternehmen) korrekt beziffert?
 - [ ] Droht ein Güteantrag (§ 15a EGZPO) in bestimmten Bundesländern vor Klageerhebung?
 - [ ] Mandatsgeheimnis: Enthält das Schreiben keine vertraulichen Informationen Dritter?
 - [ ] FRE-408-Äquivalent (DE): § 278 Abs. 6 ZPO; Vergleichsangebote im Schreiben als solche kennzeichnen.

3. **Schreiben entwerfen:**
 - Briefkopf: Kanzlei, Datum, Aktenzeichen
 - Betreff: Mandant ./. Schuldner – [Kurzbezeichnung des Anspruchs]
 - Einleitung: Mandat und Vertretung
 - Sachverhalt: Knapp, tatsächlich, ohne rechtliche Wertungen
 - Forderung: Betrag / Handlung / Unterlassung, Rechtsgrundlage
 - Fristsetzung: Konkretes Datum (nicht "binnen 14 Tagen", sondern "bis zum [TT.MM.JJJJ]")
 - Konsequenzen: Klageandrohung, Kostenfolge (§§ 91 ZPO, 93 ZPO bei Anerkenntnisklage beachten)
 - Grußformel, Unterschrift

4. **Post-Send-Checkliste:**
 - Zugangsdokumentation (Einschreiben / Fax / gerichtliche Zustellung) planen
 - Frist in Kanzleifristbuch eintragen
 - Mandats-History-Update (`/mandat-update [slug] Mahnschreiben versandt`)

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung zu Verzug und Mahnung vor Ausgabe ueber https://dejure.org und https://openjur.de verifizieren.
- Zum Verzugszins: § 247 BGB (Basiszinssatz); § 288 Abs. 1, 2 BGB. Basiszinssatz zum 01.01.2026: 1,27 Prozent (unveraendert ggue. 01.07.2025). Daraus B2C-Verzugszins 6,27 Prozent, B2B-Verzugszins 10,27 Prozent; halbjaehrliche Anpassung am 01.01. und 01.07. erforderlich. Quelle: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- Verzugspauschale § 288 Abs. 5 BGB (B2B): 40 EUR pro Vorgang.

## Ausgabeformat

```
[KANZLEI-BRIEFKOPF]

An: [Name und Anschrift Schuldner]
Datum: TT.MM.JJJJ
Aktenzeichen: [Kanzleiaktenzeichen]
Mandatsgeheimnis – § 43a Abs. 2 BRAO / § 203 StGB

Betreff: [Mandant] ./. [Schuldner] – Zahlungsaufforderung / Aufforderung zur Mängelbeseitigung

Sehr geehrte Damen und Herren,

wir vertreten [Mandant] und nehmen wie folgt Stellung:

I. Sachverhalt
...

II. Forderung
Wir fordern Sie auf, den Betrag von EUR [X.XXX,XX] bis spätestens zum [TT.MM.JJJJ] auf unser Anderkonto zu überweisen.

III. Hinweis auf Klage
Sollte die Zahlung nicht fristgerecht eingehen, sind wir angewiesen, unverzüglich Klage zu erheben und die uns entstehenden Kosten nach §§ 91, 788 ZPO gegen Sie geltend zu machen.

Mit freundlichen Grüßen
[Anwalt, Kanzlei]
```

Ausgabe als Markdown-Datei `demand-letters/[slug]/v[N].md`.

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 93 ZPO (sofortiges Anerkenntnis):** Wird der Schuldner sofort klaglos, trägt der Kläger die Kosten; Mahnschreiben vorher immer prüfen, ob es bereits eine wirksame Mahnung gab.
- **Unterlassung ohne Abmahnung:** Im UWG/UrhG/MarkenG ist die Abmahnung (mit Unterlassungsaufforderung und Vertragsstrafe) zwingende Voraussetzung; ohne Abmahnung keine Kostenerstattung (§ 97a Abs. 1 UrhG).
- **Güteantrag-Pflicht (§ 15a EGZPO):** In Bayern, Brandenburg, NRW und weiteren Ländern ist bei bestimmten Streitwerten ein Güteantrag vor Klageerhebung vorgeschrieben.
- **Fristberechnung:** Fristende nicht auf Sonn- oder Feiertag setzen (§ 193 BGB).

---

## Skill: `mahnschreiben-erhalten-aktualisierung`

_Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: §§ 286 287 BGB, §§ 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko, Verteidigungsoptionen. Output: Antwortschreiben auf Mahnschreiben. Abgrenzung: nicht Klageverteidi..._

# Eingehendes Mahnschreiben / Abmahnung – Triage

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Auswertung

1. **Schreibentyp:** Einfache Mahnung, Abmahnung (Wettbewerb/Urheberrecht), Forderungsschreiben eines Inkassos oder Klageankündigung?
2. **Frist:** Enthalt das Schreiben eine Zahlungsfrist oder Reaktionsfrist — wann läuft sie ab?
3. **Berechtigung:** Ist die behauptete Forderung dem Grunde und der Höhe nach berechtigt?
4. **Portfolio-Abgleich:** Liegt bereits ein Mandat oder ein Konflikt zu diesem Sachverhalt vor?
5. **Handlungspriorität:** Sofortige Reaktion (Unterlassung, Zahlung, Ablehnung) oder abwarten?

## Zentrale Normen
- § 286 BGB (Verzug durch Mahnung)
- § 203 BGB (Verjährungshemmung durch Verhandlungen)
- § 8 Abs. 1 UWG (Abmahnung im Wettbewerbsrecht)
- § 97a UrhG (Abmahnung im Urheberrecht)
- § 43a Abs. 1 BRAO (Interessenkonflikt bei eingehenden Forderungen)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Hochgeladenes oder einzufügendes Schreiben (Text, Scan, PDF)
- Optional: `--slug=custom-slug` für eigenes Aktenzeichen

## Ablauf

1. **Feldextraktion:**
 - Absender (Name, Kanzlei, Anschrift)
 - Empfänger (Mandant / Gesellschaft)
 - Datum des Schreibens
 - Aktenzeichen / Referenz des Absenders
 - Art des Schreibens (Mahnung, Abmahnung, Klagedrohung, Aufforderung zur Unterlassung, C&D-Äquivalent)
 - Geldforderung (Betrag, Währung, Fälligkeitsdatum)
 - Anspruchsgrundlage (soweit angegeben)
 - Gesetzte Frist (Datum extrahieren; wenn "2 Wochen ab Zugang" oder ähnlich: Frist anhand des Schreibdatums + Postlaufzeit schätzen)

2. **Portfolio-Abgleich:** Prüfen, ob zu Absender / Sachverhalt bereits ein Mandat in `mandate/_log.yaml` existiert. Wenn ja: Verknüpfung herstellen und History-Update vorschlagen.

3. **Berechtigungsprüfung (Kurzanalyse):**
 - Besteht das behauptete Schuldverhältnis dem Grunde nach?
 - Ist die Forderung bezifferbar und plausibel?
 - Sind Verjährungseinwände (§§ 195, 199 BGB) offensichtlich möglich?
 - Stehen Gegenansprüche (Aufrechnung § 387 BGB, Zurückbehaltungsrecht § 273 BGB) im Raum?
 - Besteht Verdacht auf unberechtigte Abmahnung (§ 8c UWG, § 97a Abs. 4 UrhG)?
 - Ist die Abmahnung formell vollständig (Unterlassungserklärung, Vertragsstrafe, Vollmacht)?

4. **Risikoeinschätzung:** Ampelschema:
 - 🔴 Hohe Berechtigung / akute Frist – sofortiger Handlungsbedarf
 - 🟡 Mittlere Berechtigung / prüfungsbedürftig
 - 🟢 Geringe Berechtigung / defensiv haltbar

5. **Handlungsoptionen mit Empfehlung:**
 - (a) Zahlung / Erfüllung (mit Vorbehalten)
 - (b) Modifizierte Unterlassungserklärung (bei Abmahnung)
 - (c) Abwehr / Zurückweisung mit Begründung
 - (d) Verhandlung / Vergleichsgespräch
 - (e) Schutzschrift hinterlegen (§ 945a ZPO) bei Gefahr einstweiliger Verfügung
 - (f) Mandat-Intake → neues Mandat anlegen

6. **Fristen-Alarm:**
 - Antwortfrist aus Schreiben extrahieren und als absolute Frist eintragen
 - Verjährungshemmung durch Verhandlung (§ 203 BGB) oder Mahnbescheid (§ 204 Abs. 1 Nr. 3 BGB) als Optionen nennen

7. **Datei speichern:** `inbound/[JJJJ-MM-TT]-[slug].md`

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 43. Aufl. 2025, § 8c Rn. 5 ff. (missbräuchliche Abmahnung).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
EINGEHENDES SCHREIBEN – TRIAGE-BERICHT
Slug: [automatisch generiert]
Datum Eingang: TT.MM.JJJJ
Absender: [Kanzlei / Gläubiger]
Art: [Mahnung | Abmahnung | Klagedrohung]

──────────────────────────────────────
KERNFELDER
──────────────────────────────────────
Forderungsbetrag: EUR X.XXX,XX
Anspruchsgrundlage: § 280 Abs. 1, 3, § 281 BGB
Frist gesetzt bis: TT.MM.JJJJ
Konsequenz: Klageandrohung

──────────────────────────────────────
RISIKOEINSCHÄTZUNG: 🟡 MITTEL
──────────────────────────────────────
Begründung: Forderung dem Grunde nach plausibel;
Zugang der Fristsetzung unklar; Verjährung prüfen.

──────────────────────────────────────
HANDLUNGSOPTIONEN
──────────────────────────────────────
Empfehlung: (c) Abwehr – fehlender Verjährungsverzicht
Alternativen: (d) Verhandlung, (e) Schutzschrift

──────────────────────────────────────
FRISTEN
──────────────────────────────────────
⚠️ Antwortfrist: TT.MM.JJJJ
📅 Verjährungsende: 31.12.JJJJ (§§ 195, 199 BGB)
```

## Risiken / typische Fehler

- **Fristüberschreitung:** Bei Abmahnungen im UWG/UrhG ist die Frist oft sehr kurz (3–10 Tage); plug-in markiert Schreiben mit kurzem Frist-Alert.
- **Schutzschrift vergessen:** Bei drohender einstweiliger Verfügung (z. B. Wettbewerbsrecht, Markenrecht) sofortige Schutzschrift-Hinterlegung im Zentralen Schutzschriftenregister (ZSSR, § 945a ZPO) erwägen.
- **Kostenfalle § 93 ZPO:** Wenn Berechtigung klar, Zahlung / Unterlassungserklärung vor Klagezustellung prüfen; sonst trägt Beklagter Kosten trotz sofortigem Anerkenntnis.
- **Unvollständige Vollmacht:** Abmahnung ohne beigefügte Vollmacht ist zurückweisbar (§ 174 BGB); Zurückweisung unverzüglich erklären.

---

## Skill: `mandat-arbeitsbereich-abschnitt`

_Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: §§ 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten. Output: Strategieanpassungs-Vermerk. Abgrenzung: nicht Berufungs-Skill im Prozessre..._

# Praxisprofil anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Anpassung

1. **Welches Feld?** Welches Profilfeld soll geändert werden (Rolle, Schwerpunkt, Risikostrategie, Integration)?
2. **Einzeln oder vollständig?** Sollen nur bestimmte Felder geändert oder das gesamte Profil neu aufgesetzt werden (dann Kaltstart-Interview)?
3. **Berufsrechtliche Relevanz:** Hat die geänderte Einstellung berufsrechtliche Folgen (Rollenwechsel, Vergütungsart)?
4. **Integrationscheck:** Muss nach der Änderung `--check-integrations` ausgeführt werden?
5. **Vorher-Nachher-Bestätigung:** Soll der Vergleich der geänderten Felder vor dem Speichern bestätigt werden?

## Zentrale Normen
- § 43a BRAO (Grundpflichten des Rechtsanwalts — Verschwiegenheit, sachlich unabhängige Beratung)
- § 46a BRAO (Syndikusrechtsanwalt — besondere Rollenpflichten)
- § 46c BRAO (Vertretungsverbote des Syndikusrechtsanwalts)
- § 3a RVG (Vergütungsvereinbarung — Textformerfordernis)
- § 4a RVG (Erfolgshonorar — Voraussetzungen)
- BORA §§ 2, 3 (Sachlichkeit und Grundpflichten)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Eines oder mehrere zu ändernde Felder (z. B. "Schwerpunkt auf Strafrecht hinzufügen", "Outlook MCP aktivieren")
- Optional: `--alle` – zeigt alle aktuellen Einstellungen zur Auswahl

## Ablauf

1. **Aktuelle CLAUDE.md einlesen:** Alle bestehenden Profilwerte anzeigen.
2. **Änderungswunsch präzisieren:** Falls unklar, welches Feld geändert werden soll, Auswahl anbieten.
3. **Neuen Wert erfassen:** Validierung gegen zulässige Werte (z. B. Praxisschwerpunkte-Liste).
4. **CLAUDE.md aktualisieren:** Nur das geänderte Feld überschreiben.
5. **Bestätigung:** Vorher-Nachher-Vergleich der geänderten Felder ausgeben.
6. **Integrations-Check (optional):** Bei Aktivierung einer neuen Integration automatisch `--check-integrations` ausführen.

## Quellen und Zitierweise

Keine gesonderten Normen. Allgemein: §§ 43a BRAO, 3a RVG bei rollenbezogenen Änderungen.

## Risiken / typische Fehler

- **Rollenwechsel mit Rechtsfolgen:** Wechsel von Rechtsanwalt zu Syndikusrechtsanwalt (§ 46a BRAO) hat berufsrechtliche Konsequenzen; das Plugin dokumentiert den Wechsel, ersetzt aber keine standesrechtliche Beratung.
- **Überschreiben statt Ergänzen:** Bei Praxisschwerpunkten immer prüfen, ob bestehende Einträge erhalten bleiben sollen; Default ist Ergänzung, nicht Überschreiben.

---

## Skill: `mandat-aufnahme`

_Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse. Output: Mandatsaufnahme-Protokoll. Abgrenzung: nicht inhaltliche Klageschrift im..._

# Mandat-Intake

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Aufnahme

1. **Mandatstyp:** Klägerseite, Beklagtenseite, Beratungsmandat oder gemischtes Mandat?
2. **Interessenkonflikt:** Besteht ein Interessenkonflikt mit laufenden oder abgeschlossenen Mandaten (§ 43a Abs. 4 BRAO, § 3 BORA)?
3. **Verfahrensart:** Zivilverfahren, arbeitsgerichtliches Verfahren, Verwaltungsverfahren, Strafverfahren?
4. **Schlüsselfristen:** Gibt es laufende Fristen (Verjährung, Rechtsmittelfrist, Klagefrist) die sofort gesichert werden müssen?
5. **Außenmandat:** Wird ein Korrespondenzanwalt oder Fachanwalt benötigt?

## Zentrale Normen
- § 43a Abs. 4 BRAO (Interessenkonflikt — Vertretungsverbot)
- § 3 BORA (Interessenkonflikt — weitere Fallgruppen)
- § 49b BRAO (Vergütungsvereinbarung)
- § 204 BGB (Verjährungshemmung durch Klage)
- § 232 ff. ZPO (Fristen und Fristenberechnung)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Optional: Name oder Kurzbezeichnung des Mandats
- Hochgeladene Dokumente (z. B. Klageschrift, Abmahnung, Bescheid, Vertrag)

## Ablauf

### 1. Identifikation und Aktenzeichen

- Kanzlei-Aktenzeichen und interner Slug (URL-freundlich, z. B. `mueller-gmbh-werkvertrag-2024`)
- Mandantenname (juristische oder natürliche Person), Kontaktperson
- Mandantentyp: Unternehmer (§ 14 BGB) / Verbraucher (§ 13 BGB)
- Gegenseite: Vollständiger Name, Anschrift, Verfahrensbevollmächtigter (wenn bekannt)
- Mandats-Art: Klage / Verteidigung / Beratung / Rechtsmittel / Vollstreckung

### 2. Interessenkonflikt-Check (§ 43a Abs. 4 BRAO, § 3 BORA)

- Vertritt die Kanzlei bereits die Gegenseite in irgendeinem Mandat?
- Ist ein Anwalt der Kanzlei früher für die Gegenseite tätig gewesen?
- Bestehen sonstige Interessenkonflikte (persönliche Beziehungen, Eigeninteresse)?
- **Bei positivem Befund:** Mandat ablehnen oder um Einverständnis einholen; Plugin erstellt Interessenkonflikt-Vermerk.

### 3. Sachverhaltserfassung

- Kurzbeschreibung des Sachverhalts (wer, was, wann, wie viel?)
- Anspruchsgrundlage (vorläufig, z. B. § 280 BGB, § 823 BGB, § 1 UWG)
- Rechtliches Kernproblem (streitige Tat- oder Rechtsfrage)
- Vorhandene Dokumente: Liste und Anlage-Nummern

### 4. Verfahrensart und Zuständigkeit

- Verfahrensordnung: ZPO / ArbGG / VwGO / FGO / SGG / FamFG / StPO
- Sachlich zuständiges Gericht: AG (§§ 23 ff. GVG), LG (§§ 71 ff. GVG), Spezialgerichte (ArbG, VG, FG, SG)
- Örtliche Zuständigkeit: allgemeiner Gerichtsstand (§§ 12, 13 ZPO), besonderer Gerichtsstand (§ 29 ZPO: Erfüllungsort), ausschließlicher Gerichtsstand (§ 29a ZPO: Miete)
- Streitwert (vorläufig, nach GKG/RVG)

### 5. Risikotriage

- Erfolgsaussichten: stark / mittel / schwach (mit Kurzbereg)
- Worst-Case-Szenario (maximale Exposition inkl. Kosten § 91 ZPO)
- Wichtig: Prozesskostenrisiko nach § 91 ZPO; ggf. Rechtsschutzversicherung vorhanden?
- Verjährungsrisiko prüfen: Restlaufzeit (§§ 195, 199 BGB)

### 6. Außenanwalt / Korrespondenzanwalt

- Wird die Sache vollständig intern geführt oder von externer Kanzlei?
- Externer Anwalt: Name, Kanzlei, Kontakt
- Reporting-Intervall an Mandanten

### 7. Beweissicherung

- Ist sofortige Beweissicherung erforderlich? (z. B. Baumangel, drohende Sachzustandsveränderung)
- Aufbewahrungsanordnung erstellen? → Weiterleitung an Skill `beweissicherung`

### 8. Schlüsselfristen

- Klagefrist / Antwortfrist
- Verjährungsablauf
- Nächste Prozesshandlung

### 9. mandat.md und verlauf.md schreiben

```yaml
### mandat.md
slug: ""
kanzlei_az: ""
mandant:
 name: ""
 typ: "Unternehmer / Verbraucher"
gegenseite:
 name: ""
 anwalt: ""
verfahren:
 art: ""
 gericht: ""
 az_gericht: ""
 verfahrensordnung: ""
streitwert: 0
anspruchsgrundlage: ""
risiko: "hoch / mittel / gering"
exposition_max: 0
verjaehrung: ""
aussenanwalt: ""
status: "aktiv"
beweissicherung: false
angelegt: "TT.MM.JJJJ"
naechste_frist: "TT.MM.JJJJ"
```

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- BRAO § 43a Abs. 4 (Interessenkonflikt: Verbot der Vertretung widerstreitender Interessen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Risiken / typische Fehler

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Verjährung nicht geprüft:** Vor Intake stets Verjährungsablauf ermitteln; läuft die Verjährung in < 3 Monaten, sofort Hemmungsmaßnahmen (§ 204 BGB: Klageerhebung, Mahnbescheid) einleiten.
- **Zuständigkeit falsch:** Fehlerhafte sachliche Zuständigkeit führt zur Verweisung (§ 281 ZPO) und Zeitverlust; Streitwertgrenzen (AG: bis EUR 10.000; LG: über EUR 10.000, § 23 Nr. 1 GVG i. d. F. seit 1.1.2026) prüfen.
- **Mandant ist Verbraucher – besondere Pflichten:** Informationspflichten nach § 43d BRAO (Kostenmitteilung), § 13 RVG (Vergütungsvereinbarung).

---

## Skill: `mandat-briefing-schliessen-portfolio-status`

_Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Termin. Abgrenzung: nicht Zeugenvorbereitung (eigener Skill) im Prozessr..._

# Mandat-Briefing

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Mandat-Slug
- Optional: Fokusthema (`--frist`, `--risiko`, `--naechste-schritte`)
- Optional: Empfänger (`--mandant`, `--justiziar`, `--anwalt`) – steuert Detailgrad und Stil

## Ablauf

1. **Mandatsdaten laden:** `mandate/[slug]/mandat.md` und `mandate/[slug]/verlauf.md` einlesen.

2. **Verfahrensstand zusammenfassen:**
 - Parteien, Gericht, Aktenzeichen
 - Verfahrensstadium (Klagezustellung, Schriftsatzphase, Beweisaufnahme, Urteil, Rechtsmittel, Vollstreckung)
 - Ansprüche / Streitgegenstand (§ 264 ZPO)
 - Bisheriger Verfahrensverlauf (Chronologie der Verfahrenshandlungen)

3. **Entwicklungen seit letztem Update:**
 - Letzte Eintrag in verlauf.md identifizieren
 - Neue Schriftsätze, Gerichtsentscheidungen, Vergleichsgespräche

4. **Fristen-Check:**
 - Nächste Frist (Schriftsatzfrist, Berufungsfrist, Urteilsfrist, Vollstreckungsverjährung)
 - Risiko-Frist (in roter Zone wenn < 14 Tage)

5. **Offene Handlungspunkte:**
 - Was muss der Anwalt noch erledigen?
 - Was ist von der Gegenseite / dem Gericht ausstehend?
 - Welche Beweise fehlen noch?

6. **Risikoneueinschätzung:**
 - Änderung der Risikoeinschätzung seit letztem Intake? (BGH-Rechtsprechung, neue Sachverhalte)
 - Expositionsschätzung (untere / mittlere / obere Schadenswert-Bandbreite)
 - Vergleichspotential (§ 278 Abs. 1 ZPO: Gericht soll in jeder Lage des Verfahrens auf Vergleich hinwirken)

7. **Ausgabe:** Strukturiertes Briefing-Memo im Urteilsstil oder als Executive Summary.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
MANDAT-BRIEFING
──────────────────────────────────────
Mandat: [Slug]
Parteien: [Kläger] ./. [Beklagter]
Gericht / Az.: [Gericht], Az. [JJJJ] [Aktenzeichen]
Verfahrensstufe: [z. B. Berufung – OLG Frankfurt]
Stand: TT.MM.JJJJ
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
1. VERFAHRENSSTAND
──────────────────────────────────────
[Kurzdarstellung: Wo sind wir? Was wurde bisher eingereicht / entschieden?]

──────────────────────────────────────
2. ENTWICKLUNGEN SEIT [DATUM LETZTES UPDATE]
──────────────────────────────────────
[Neue Schriftsätze, Urteile, Korrespondenz]

──────────────────────────────────────
3. NÄCHSTE FRIST
──────────────────────────────────────
⚠️ [Frist] – [Beschreibung] – [Datum]

──────────────────────────────────────
4. OFFENE HANDLUNGSPUNKTE
──────────────────────────────────────
□ [Punkt 1]
□ [Punkt 2]

──────────────────────────────────────
5. RISIKOEINSCHÄTZUNG
──────────────────────────────────────
Expositionsschätzung: EUR [X] – EUR [Y]
Risikostufe: 🔴 hoch / 🟡 mittel / 🟢 gering
Vergleichspotential: [Einschätzung]
```

## Risiken / typische Fehler

- **Veraltete mandat.md:** Ohne regelmäßige Updates per `/mandat-update` liefert das Briefing einen falschen Stand; nach jeder Entwicklung updaten.
- **Fristversäumnis-Risiko:** Das Briefing ersetzt nicht den Fristenkalender; jede Frist muss separat in das Kanzlei-Fristbuch eingetragen werden.
- **Vertraulichkeit des Briefings:** Das Briefing enthält Mandatsgeheimnisse; Empfängerkreis sorgfältig wählen (§ 43a Abs. 2 BRAO); nicht per unverschlüsselter E-Mail versenden.

<!-- AUDIT 27.05.2026
Halluzinierte Referenz geloescht. Keine Ersatzquelle gefunden.
-->

---

## Skill: `mandat-schliessen`

_Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussbericht Mandat. Abgrenzung: nicht laufende Mandat-Aktualisierung im Proz..._

# Mandat schließen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Mandat-Slug
- Abschlusstyp: `--urteil`, `--vergleich`, `--klagerücknahme`, `--erledigungserklärung`, `--einstellung`, `--sonstiges`
- Ergebnis (kurz): Wer hat gewonnen, was wurde vereinbart, welcher Betrag?

## Ablauf

1. **Abschlusstype und Ergebnis erfassen:**

 | Typ | Relevante Normen |
 |---|---|
 | Urteil (Endurteil) | §§ 300 ff. ZPO; Rechtskraft § 322 ZPO |
 | Anerkenntnisurteil | § 307 ZPO |
 | Versäumnisurteil | §§ 330 ff. ZPO |
 | Vergleich | §§ 794 Abs. 1 Nr. 1, 278 ZPO; vollstreckbar |
 | Klagerücknahme | §§ 269, 270 ZPO; Kostenfolge § 269 Abs. 3 ZPO |
 | Erledigungserklärung | § 91a ZPO; Kostenbeschluss |
 | Einstellung (Strafrecht) | §§ 153, 153a, 170 Abs. 2, 204 StPO |
 | Verfahrensvergleich (Verwaltungsrecht) | § 106 VwGO |

2. **Endexposition berechnen:**
 - Gezahlter Betrag / auferlegte Leistung
 - Kostenfestsetzung (§§ 103 ff. ZPO): eigene Kosten + erstattete / zu erstattende Kosten
 - Vergleich mit ursprünglicher Risikoschätzung (Intake-Wert)

3. **Honorar und Gebühren:**
 - Letzte Abrechnung nach RVG (§ 8 RVG: Fälligkeit mit Mandatsbeendigung)
 - Offene Vorschüsse (§ 9 RVG) zurückerstatten oder verrechnen
 - Fremdgelder abwickeln (§ 43a Abs. 5 BRAO: unverzügliche Weiterleitung)

4. **Lessons Learned:**
 - Was lief gut / schlecht?
 - Prozessführungsempfehlung für künftige vergleichbare Mandate?
 - BGH- oder OLG-Urteile, die im Mandat relevant waren und für spätere Mandate zu merken sind?

5. **Handakte archivieren (§ 50 BRAO):**
 - Handakte für mind. 6 Jahre nach Mandatsende aufbewahren
 - Elektronische Akte: gleichwertige Sicherung (§ 50 Abs. 2 BRAO)
 - Herausgabepflicht auf Verlangen (§ 50 Abs. 3 BRAO)

6. **Portfolio-Log aktualisieren:** Status in `_log.yaml` auf `archiv` setzen; Abschlussdatum, Ergebnis, Endexposition eintragen.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- BRAO § 50 (Aufbewahrungspflicht Handakten: 6 Jahre); § 43a Abs. 5 BRAO (Fremdgelder).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
MANDAT-ABSCHLUSS
──────────────────────────────────────
Mandat-Slug: [slug]
Schließungsdatum: TT.MM.JJJJ
Typ: [z. B. Vergleich]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
ERGEBNIS
──────────────────────────────────────
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

──────────────────────────────────────
ENDEXPOSITION
──────────────────────────────────────
Eingeklagter Betrag: EUR XX.XXX
Vergleichszahlung: EUR XX.XXX
Kostenerstattung: EUR X.XXX (§§ 103 ff. ZPO)
Ursprüngliche Schätzung: EUR XX.XXX – EUR XX.XXX

──────────────────────────────────────
LESSONS LEARNED
──────────────────────────────────────
[Freitext]

──────────────────────────────────────
ARCHIVIERUNG
──────────────────────────────────────
Handakte aufzubewahren bis: TT.MM.JJJJ (§ 50 Abs. 1 BRAO: 6 Jahre)
_log.yaml-Status: archiv
```

## Risiken / typische Fehler

- **Aufbewahrungsfrist übersehen:** § 50 Abs. 1 BRAO: mindestens 6 Jahre nach Mandatsende; kürzere Vernichtung ist Berufsrechtsverletzung.
- **Fremdgelder nicht abgewickelt:** § 43a Abs. 5 BRAO – Fremdgelder (Kostenvorschüsse, Schadensersatzbeträge) unverzüglich weiterleiten; Verzögerung kann zur Strafbarkeit führen (§ 266 StGB).
- **Rechtsmittelfrist läuft noch:** Vor dem Schließen prüfen, ob Berufungs- (§ 517 ZPO: 1 Monat) oder Revisionsfrist (§ 548 ZPO: 1 Monat) noch offen ist; Mandat erst nach Eintritt der Rechtskraft schließen oder Mandanten ausdrücklich auf Verzicht hinweisen.
- **Vollstreckungsverjährung:** Vollstreckungstitel verjähren nach § 197 Abs. 1 Nr. 3 BGB in 30 Jahren; Abschluss nicht ohne Dokumentation der Vollstreckungsmaßnahmen.

<!-- AUDIT 27.05.2026
Halluzinierte Referenz geloescht. Keine Ersatzquelle gefunden.
-->

---

## Skill: `schriftsatz-abschnitt`

_Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: §§ 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für Einbau in Klageschrift oder Erwiderung. Abgrenzung: nicht vollständige Klagesc..._

# Schriftsatzabschnitt-Entwurf

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktives Mandat (Slug) mit mandat.md und verlauf.md
- Bezeichnung des gewünschten Abschnitts (z. B. "Sachverhaltsdarstellung", "Rechtliche Ausführungen zu Klageantrag 1", "Berufungsangriff I: Übergangener Beweisantrag")
- Anspruchstabelle (falls vorhanden, aus `/anspruchstabelle`)
- Chronologie (falls vorhanden, aus `/chronologie`)
- Beizufügende Dokumente / Anlagen (Vertrag, Schriftverkehr, Sachverständigengutachten)
- Gewünschte Schriftsatzart und verfahrensrechtliche Situation

## Ablauf

1. **Mandatsdaten laden:** mandat.md, verlauf.md, ggf. Chronologie und Anspruchstabelle einlesen. Mandatstheorie und Kanzleistil aus CLAUDE.md laden.

2. **Abschnittstyp bestimmen:**
 - **Klageschrift** (§§ 253, 261 ZPO): Rubrum, Anträge, Sachverhaltsdarstellung, Rechtliche Ausführungen, Beweisangebote.
 - **Klageerwiderung** (§ 277 ZPO): Bestreiten (erheblich/unerheblich), Gegendarstellung, Rechtsausführungen, eigene Anträge, Hilfsaufrechnung/Widerklage.
 - **Berufungsbegründung** (§ 520 Abs. 3 ZPO): Darlegung der Berufungsangriffe, Bezifferung von Rechtsverletzungen (§ 546 ZPO), neue Tatsachen und Beweise (§ 531 Abs. 2 ZPO), Berufungsanträge.
 - **Revisionsbegründung** (§ 551 Abs. 3 ZPO): Revisionsgründe (§ 545 ZPO), absolute Revisionsgründe (§ 547 ZPO), Rüge der Nichtzulassung (§ 544 ZPO), Grundsatzrevision (§ 543 Abs. 2 ZPO).
 - **Beschwerde** (§§ 567 ff., 574 ff. ZPO): Statthaftigkeit, Frist, Begründung.

3. **Urteilsstil anwenden:** Tatsachenvortrag in indirekter Rede oder Behauptungsform, normative Subsumtion knapp, Beweisangebote vollständig.

4. **Normen und Rechtsprechung einarbeiten:** Jede Behauptung rechtlicher Art mit Norm und – soweit verfügbar – BGH-Rechtsprechung nach Zitierweise (../references/zitierweise.md) belegen.

5. **Beweisangebote formulieren:** Für jeden bestrittenen Tatsachenbehauptung ein konkretes Beweisangebot (Zeugnis, Sachverständiger, Urkunde, Augenschein, Parteivernehmung § 447 ZPO, Geständnisfiktion § 138 Abs. 3 ZPO).

6. **Lückenprüfung:** Fehlende Tatsachenbehauptungen, unklare Beweisangebote, ungeklärte Passivlegitimation, fehlende Kausalität und Schaden als **[LÜCKE: …]** markieren.

7. **Entwurf ausgeben:** Urteilsstil, kanzleispezifisches Format, Fristen am Ende der Ausgabe.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Einschlägige Kommentare und Rechtsprechung:

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispiel

> **III. Zur Berufungsbegründung – Verletzung des § 286 ZPO**
>
> Das Landgericht hat das Beweisangebot der Klägerin auf Vernehmung des Zeugen Müller (Schriftsatz v. 14.03.2023, S. 7) übergangen, ohne dies in den Entscheidungsgründen zu begründen. Dies verletzt Art. 103 Abs. 1 GG und § 286 Abs. 1 ZPO.
>
> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
>
> *Beweis: Zeugnis des Herrn Max Müller, [Anschrift] – Beweis-Nr. 5.*

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Berufungsbegründungsfrist:** § 520 Abs. 2 ZPO: 2 Monate ab Urteilszustellung; verlängerbar auf Antrag, aber nur mit gegnerischer Zustimmung oder wichtigem Grund.
- **Neue Tatsachen in der Berufung:** § 531 Abs. 2 ZPO begrenzt neues Vorbringen; stets prüfen, ob Nachlässigkeit im ersten Rechtszug vorlag.
- **Revisionsanforderungen:** § 543 Abs. 2 ZPO – Grundsatzbedeutung oder Sicherung einheitlicher Rechtsprechung; ohne NZB-Begründung keine Revision (§ 544 ZPO).
- **Verstoß gegen § 138 ZPO:** Wahrheitspflicht; keine Behauptung ins Blaue hinein; Darlegungs- und Beweislast nicht verwechseln.
- **Berufsrechtliche Hinweispflicht:** Bei überraschenden Rechtswendungen ist der Mandant nach § 43 BRAO zu informieren; kein Schriftsatz ohne Rücksprache versenden.

---

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 73/20, NJW 2021, 1886 Rn. 15 (" neue Angriffsmittel § 531 ZPO ") – Zitatfehler (WRONG_TOPIC). Das Urteil behandelt Verletzung des allgemeinen Persönlichkeitsrechts / Bestimmtheit Klageantrags bei Erstbegehungsgefahr (NJW 2021, 1756), nicht neue Angriffsmittel nach § 531 ZPO (dejure.org/2021,4358). Eintrag ersatzlos gelöscht; kein verifizierbarer Ersatz mit identischem NJW-Fundstelle ermittelt.
Quelle : https://dejure.org/2021,4358
Aktion : Zeile entfernt
-->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

