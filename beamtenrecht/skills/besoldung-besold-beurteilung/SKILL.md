---
name: besoldung-besold-beurteilung
description: "Besoldung Besold Beurteilung: bündelt 7 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Besoldung Besold Beurteilung

## Arbeitsbereich

Dieser Skill bündelt 7 sachlich verwandte Arbeitsschritte rund um **Besoldung Besold Beurteilung** im Plugin Beamten- und Richterdienstrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `besold-neu-019-beurteilung-plausibilisierung-und-anlassbeurteilu` | Beamtenrecht: Beurteilung Plausibilisierung und Anlassbeurteilung mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `besold-neu-020-befoerderungskaskade-organisationsmissbrauch-red` | Beamtenrecht: Beförderungskaskade Organisationsmissbrauch Red-Team mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `besoldung-bund-bbesg` | Bundesbesoldung nach BBesG: Grundgehalt, Stufen, Zulagen, Familienzuschlag, Rückforderung und Verlust der Besoldung. |
| `besoldung-bverfg-dreischritt-2025` | Vertiefung amtsangemessene Alimentation nach Art. 33 Abs. 5 GG: BVerfG-Linie 2015/2020/2025, Mindestabstand, Prekaritätsschwelle, Drei-Schritt-Prüfung, Reparaturgesetz und Output für Widerspruch, Vorlageanregung und Mandantenmemo. |
| `besoldung-laender-check` | Länderbesoldung: Landesbesoldungsgesetz, Stufen, Sonderzahlungen, Familienzuschläge und landesspezifische Abweichungen. |
| `besoldung-verfassungswidrig-a-besoldung` | Skill zur Geltendmachung verfassungswidriger A-Besoldung im Land. Pruefschema fuer den Verstoss gegen die amtsangemessene Alimentation in der A-Besoldung unter Beruecksichtigung des Mindestabstandsgebots zum sozialhilferechtlichen Grundsicherungsniveau. Behandelt die Konstellationen Familienzuschlag fuer das dritte und weitere Kinder lange statische Besoldung in Verbindung mit Tariferhoehungen sowie die zeitnahe Geltendmachung des Anspruchs im jeweiligen Haushaltsjahr. Liefert Widerspruch und Vorlageantrag. |
| `besoldung-versorgung-familienzuschlag` | Überträgt Alimentationsfragen vorsichtig auf Versorgungsempfänger, Hinterbliebene, kinderreiche Beamtenfamilien und Familienzuschlag-Rückforderungen, mit ausdrücklicher Unsicherheits- und Landesrechtsprüfung. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Besoldung Besold Beurteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `besold-neu-019-beurteilung-plausibilisierung-und-anlassbeurteilu`

**Fokus:** Beamtenrecht: Beurteilung Plausibilisierung und Anlassbeurteilung mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Besold Beurteilung Plausibilisierung Und Anlassbeurteilu

## Aufgabe

Skill fuer dienstliche Beurteilung — Plausibilisierung und Anlassbeurteilung.

## Norm

- **§ 21 BBG**: Beurteilung.
- BLV (Bundeslaufbahnverordnung).
- Beurteilungsrichtlinien des Dienstherrn.

## Beurteilungsarten

- **Regelbeurteilung** (turnusmaessig, z. B. alle 3 Jahre).
- **Anlassbeurteilung** (vor Beförderung, Versetzung).
- **Endbeurteilung** (bei Pensionierung selten).

## Plausibilisierung

- Beurteilung muss in sich konsistent sein.
- Begruendung der Note nachvollziehbar.
- Einzelmerkmale stimmen mit Gesamtnote ueberein.

## Konkurrentenfall: Vergleichsbeurteilung

- Bei Auswahlverfahren muessen alle Beurteilungen vergleichbar sein.
- Sonst: Auswahl rechtsfehlerhaft.

## Klagewege

- Widerspruch gegen Beurteilung.
- Verpflichtungsklage VG auf Neuabfassung.

## Pruefraster

1. Welche Beurteilung?
2. Plausibel?
3. Konkurrenzlage?
4. Anfechtungsklage?

## Output

- Beurteilungsanfechtung.
- Klageentwurf.

## 2. `besold-neu-020-befoerderungskaskade-organisationsmissbrauch-red`

**Fokus:** Beamtenrecht: Beförderungskaskade Organisationsmissbrauch Red-Team mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Besold Befoerderungskaskade Organisationsmissbrauch Red

## Aufgabe

Skill fuer Beförderungskaskade — Organisationsmissbrauch (Red Flag).

## Was ist Befoerderungskaskade?

- Mehrere Beamte werden hintereinander befoerdert.
- Oft fuer eine geplante Spitzenposition mit zwischengeschalteten Steigerungen.

## Missbrauchsindizien

- Beförderung in voneinander unabhaengigen Statusaemtern hintereinander zur Position X.
- Vorgaben an Beurteilungen zur Steuerung der Auswahl.
- "Stellenparkplatz" fuer Bewerber X.
- BVerwG-Linie zur Manipulation.

## Konkurrentenschutz

- Bei Verdacht: Konkurrentenklage.
- Akteneinsicht in Beurteilungen.
- Antrag auf Vorlage der Beförderungsentscheidungen.

## Red-Team-Pruefung

1. Wer wurde wann befoerdert?
2. Wer hat profitiert?
3. Konsistente Beurteilungen?
4. Manipulation indiziert?

## BVerwG-Linie

- BVerwG zur Missbrauchskontrolle bei Beförderungsketten.
- Az im Mandat live verifizieren.

## Pruefraster

1. Beförderungssequenz auffaellig?
2. Beurteilungen konsistent?
3. Klage moeglich?

## Output

- Red-Team-Memo.
- Konkurrentenklage.

## 3. `besoldung-bund-bbesg`

**Fokus:** Bundesbesoldung nach BBesG: Grundgehalt, Stufen, Zulagen, Familienzuschlag, Rückforderung und Verlust der Besoldung.

# Besoldung Bund Bbesg

## Aufgabe

Bundesbesoldung nach BBesG: Grundgehalt, Stufen, Zulagen, Familienzuschlag, Rückforderung und Verlust der Besoldung.

## Arbeitsweise

Prüfe Besoldungsgruppe, Stufe, Erfahrungszeiten, Teilzeit, Zulagen, Rückforderung und Verjährung. Nutze BBesG live.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.

## 4. `besoldung-bverfg-dreischritt-2025`

**Fokus:** Vertiefung amtsangemessene Alimentation nach Art. 33 Abs. 5 GG: BVerfG-Linie 2015/2020/2025, Mindestabstand, Prekaritätsschwelle, Drei-Schritt-Prüfung, Reparaturgesetz und Output für Widerspruch, Vorlageanregung und Mandantenmemo.

# Besoldung - BVerfG-Dreischritt, Mindestabstand und Reformstand

## Startfrage

Dieser Skill wird genutzt, wenn Besoldung, Familienzuschlag, Nachzahlung, Richter-/Staatsanwaltsbesoldung oder Versorgung verfassungsrechtlich geprüft werden soll. Er beginnt nicht mit einer fertigen Meinung, sondern mit einer kleinen Matrix:

| Frage | Warum sie zählt |
| --- | --- |
| Bund oder welches Land? | Seit der Föderalismusreform laufen Besoldung und Versorgung der Länder landesrechtlich. |
| Besoldungsordnung / Amt / Erfahrungsstufe? | A, B, R, W und C haben unterschiedliche Vergleichsgruppen. |
| Zeitraum? | Verfassungswidrigkeit wird jahresbezogen geprüft; spätere Reparaturgesetze ändern nicht automatisch alte Jahre. |
| Familie / Kinder / Alleinverdiener / Teilzeit? | Mindestabstand und Familienalimentation hängen am konkreten Lebenszuschnitt. |
| Schon zeitnah geltend gemacht? | Rückwirkende Nachzahlung scheitert praktisch oft an der haushaltsnahen Geltendmachung. |

## Leitplanken

Art. 33 Abs. 5 GG schützt das Alimentationsprinzip. Der Dienstherr muss Beamte, Richter und Versorgungsempfänger so alimentieren, dass Amt, Verantwortung, Lebensstellung und Familienlasten realistisch getragen werden können. Nach der verfassungsgerichtlichen Linie seit 2015 darf der Besoldungsgesetzgeber zwar typisieren, er muss aber nachvollziehbar rechnen und darf die Mindestbesoldung nicht unter eine verfassungsrechtliche Untergrenze drücken.

Der Skill nutzt drei Ebenen:

1. **Mindestbesoldung / Prekaritätsabstand:** Der Abstand zur sozialrechtlich geprägten Mindestsicherung darf nicht nur symbolisch sein. Die Prüfung fragt nach Regelbedarf, Unterkunft, Heizkosten, Kranken-/Pflegeversicherung und familientypischen Mehrbedarfen.
2. **Relative Parameter:** Entwicklung von Tariflöhnen im öffentlichen Dienst, Nominallohnindex, Verbraucherpreisindex, Abstände innerhalb der Besoldungsordnung und Vergleich mit anderen Dienstherren.
3. **Gesamtwürdigung:** Die Parameter sind Indizien. Am Ende muss die Gesamtalimentation das Amt tragen; der Gesetzgeber muss begründen, warum sein Besoldungssystem plausibel ist.

## Arbeitsprogramm

- Zeitraum nach Kalenderjahren trennen.
- Dienstherr, Besoldungsgruppe, Erfahrungsstufe, Familienstand und Kinderzahl erfassen.
- Bruttobesoldung, Nettoeffekt und Zuschläge getrennt darstellen.
- Für Länderfälle das jeweilige Landesbesoldungsgesetz und Reparaturgesetz aktuell prüfen.
- Für Richter/Staatsanwälte R-Besoldung nicht einfach mit A-Besoldung gleichsetzen, aber Parametervergleich zulassen.
- Prüfen, ob Besoldung nur formal erhöht wurde oder ob reale Mindestalimentation erreicht wird.
- Bei Familienzuschlägen gesondert prüfen, ob das System die Mehrbelastung kindbezogen realistisch auffängt.

## Warnsignale

- Der Dienstherr verweist pauschal auf Haushaltsnot ohne belastbare Rechenbasis.
- Reparaturgesetze arbeiten nur mit Einmalzahlungen, ohne Systembruch zu erklären.
- Familienzuschläge steigen stark, Grundgehalt bleibt strukturell niedrig.
- Kläger ist Versorgungsempfänger: Übertragbarkeit der Beamten-/Richterlinien genau begründen, nicht behaupten.
- Akte enthält nur Pressemitteilungen: Entscheidung, Datum, Aktenzeichen und amtliche Quelle nachziehen.

## Output

Der Skill erzeugt wahlweise:

- Kurznotiz „besteht verfassungsrechtliches Besoldungsrisiko?";
- Widerspruchs- oder Antragstext zur zeitnahen Geltendmachung;
- Schriftsatzbaustein zur Vorlage nach Art. 100 GG;
- tabellarische Jahresprüfung;
- Mandantenbrief in einfacher Sprache.

## Zitierhygiene

Keine BeckRS-, juris- oder Kommentarzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle. Bekannte Anker: BVerfG 05.05.2015 - 2 BvL 17/09 u.a.; BVerfG 04.05.2020 - 2 BvL 4/18; BVerfG 04.05.2020 - 2 BvL 6/17 u.a.; BVerfG 17.09.2025 - 2 BvL 20/17 u.a. Vor Ausgabe wird die konkrete Quelle live geprüft.

## 5. `besoldung-laender-check`

**Fokus:** Länderbesoldung: Landesbesoldungsgesetz, Stufen, Sonderzahlungen, Familienzuschläge und landesspezifische Abweichungen.

# Besoldung Laender Check

## Aufgabe

Länderbesoldung: Landesbesoldungsgesetz, Stufen, Sonderzahlungen, Familienzuschläge und landesspezifische Abweichungen.

## Arbeitsweise

Frage Bundesland ab. Erzeuge Prüfliste statt pauschaler Aussage. Jede Zahl und Stufe nur aus amtlicher Quelle.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.

## 6. `besoldung-verfassungswidrig-a-besoldung`

**Fokus:** Skill zur Geltendmachung verfassungswidriger A-Besoldung im Land. Pruefschema fuer den Verstoss gegen die amtsangemessene Alimentation in der A-Besoldung unter Beruecksichtigung des Mindestabstandsgebots zum sozialhilferechtlichen Grundsicherungsniveau. Behandelt die Konstellationen Familienzuschlag fuer das dritte und weitere Kinder lange statische Besoldung in Verbindung mit Tariferhoehungen sowie die zeitnahe Geltendmachung des Anspruchs im jeweiligen Haushaltsjahr. Liefert Widerspruch und Vorlageantrag.

# Verfassungswidrige A-Besoldung — Mindestabstandsgebot und Geltendmachung

## 1. Zweck und Anwendungsfall

Skill fuer Beamte und Richter, die geltend machen wollen, dass ihre Besoldung in der A-Skala (insb. niedrigere Besoldungsgruppen A4 bis A9 mit unterhaltsberechtigten Kindern) das verfassungsrechtliche Mindestabstandsgebot zur Grundsicherung nicht einhaelt. Anwendung neben `amtsangemessene-alimentation-bverfg` und `familienzuschlag-drittes-kind-bverfg`.

## 2. Eingaben

- Besoldungsgruppe und Stufe
- Anzahl der unterhaltsberechtigten Kinder
- Bundesland
- Datum der letzten Anpassung
- Vergleichsberechnung Grundsicherung (Regelbedarf, Wohnen, Heizung) im Haushalt

## 3. Ablauf / Checkliste

### a) Mindestabstand zur Grundsicherung
- Das BVerfG verlangt einen wirksamen Abstand zwischen der Besoldung der untersten Besoldungsgruppen und dem sozialhilferechtlichen Grundsicherungsniveau (gemessen am SGB II / SGB XII unter Beruecksichtigung von Regelbedarfen, Unterkunfts- und Heizkosten und Kinderbedarfen).
- Faustregel: ca. 15 Prozent oberhalb des Grundsicherungsniveaus. Im Einzelfall pruefen.

### b) Familienzuschlag fuer Mehrkinderfamilien
- Familienzuschlag fuer das dritte und jedes weitere Kind hat eine zentrale Rolle. Bei zu niedrigem Zuschlag verstoesst die Besoldung gegen Art. 33 Abs. 5 GG — siehe Schwester-Skill `familienzuschlag-drittes-kind-bverfg`.

### c) Geltendmachung zeitnah
- Wichtige BVerfG-Bedingung: Der Beamte muss seinen Anspruch zeitnah im laufenden Haushaltsjahr geltend machen (Widerspruch). Ohne zeitnahe Geltendmachung kein Nachzahlungsanspruch fuer vergangene Jahre.

### d) Verfahrenslage
- Widerspruch gegen die monatliche Bezuegemitteilung.
- Klage zum VG, ggf. Aussetzung und Vorlage nach Art. 100 Abs. 1 GG.
- Anschluss an Pilotverfahren ratsam.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 5, Art. 100 Abs. 1 GG; BBesG; Landesbesoldungsgesetze; SGB II / SGB XII (zur Grundsicherungsberechnung).
- Rspr.: BVerfG zur A-Besoldung — Quellenanker unten; konkrete Entscheidung in amtlicher oder freier Quelle prüfen.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruchsschrift mit Berechnungsanlage.
- Pruefraster Mindestabstandsgebot.

## 6. Verifizierte Quellenanker

- BVerfG, 05.05.2015 - 2 BvL 17/09 u.a.: R-Besoldung Sachsen-Anhalt; Parameterprüfung zur amtsangemessenen Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 4/18: R-Besoldung Berlin; Mindestabstand und Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 6/17 u.a.: kinderreiche Richterfamilien und Familienzuschlag.
- BVerfG, 17.09.2025 - 2 BvL 20/17 u.a.: Berliner A-Besoldung; Prekaritätsschwelle und Dreischritt.
- Seit der Föderalismusreform 2006 ist Landesbesoldung landesrechtlich zu prüfen; BBesG nur für Bund/Soldaten und fortgeltende Sonderlagen.
- Für Stufen, Auslandsdienstbezüge, Erschwerniszulagen und Mehrarbeit zusätzlich aktuelle Spezialnormen live prüfen; die BVerfG-Linie ersetzt keine Fachnormprüfung.

## 7. Beispiel (Kurzfassung)

Polizeimeister A7 Stufe 4, Ehepartner ohne Erwerbseinkommen, vier Kinder. Skill liefert Berechnung Grundsicherungsniveau im Vergleich zu Brutto- und Nettobesoldung, Widerspruchsentwurf mit zeitnaher Geltendmachung.

## 7. `besoldung-versorgung-familienzuschlag`

**Fokus:** Überträgt Alimentationsfragen vorsichtig auf Versorgungsempfänger, Hinterbliebene, kinderreiche Beamtenfamilien und Familienzuschlag-Rückforderungen, mit ausdrücklicher Unsicherheits- und Landesrechtsprüfung.

# Versorgung, Familienzuschlag und offene Übertragungsfragen

## Wann nutzen?

Dieser Skill greift, wenn nicht der aktive Beamte allein betroffen ist, sondern Versorgungsempfänger, Witwen-/Witwergeld, Waisengeld, Familienzuschläge, kinderreiche Familien, Teilzeit oder Rückforderung von Überzahlungen.

## Kernthese

Die Alimentationsrechtsprechung ist stark an aktiven Beamten und Richtern entwickelt. Für Versorgungsempfänger und Hinterbliebene können die Grundgedanken Bedeutung haben, aber die Übertragung ist nicht automatisch. Der Skill arbeitet deshalb mit einer vorsichtigen „Ja, aber"-Struktur.

## Prüfroute

1. Status: aktiv, Ruhestand, Hinterbliebene, begrenzte Dienstfähigkeit, Teilzeit.
2. Rechtsquelle: Bundesversorgung oder Landesversorgung.
3. Anspruchstyp: laufende Versorgung, Nachzahlung, Familienzuschlag, Rückforderung.
4. Zeitraum und Bescheidlage.
5. Besteht eine eigene verfassungsrechtliche Unteralimentation oder nur eine mittelbare Folgewirkung?

## Familienzuschlag

- Kindbezogene Komponenten separat erfassen.
- Konkurrenzfälle abfragen: anderer Elternteil im öffentlichen Dienst, Teilzeit, Trennung, Wechselmodell, Kindergeldberechtigung.
- Nachweispflichten prüfen, aber keine Rückforderung ohne Anhörung, Vertrauensschutz und Entreicherung prüfen.
- Bei kinderreichen Familien die besondere Belastung nicht im Grundgehalt verstecken.

## Versorgung

Der Skill trennt:

- ruhegehaltfähige Dienstzeit;
- Ruhegehaltssatz;
- Mindestversorgung;
- Versorgungsabschläge;
- Witwen-/Witwer- und Waisengeld;
- Ruhen, Anrechnung und Erwerbseinkommen;
- Unfallfürsorge.

## Output

- Risikomemo zur Übertragbarkeit der Besoldungsrechtsprechung.
- Antrag/Widerspruch mit vorsichtiger verfassungsrechtlicher Begründung.
- Rückforderungsabwehr mit Vertrauensschutz- und Billigkeitsargumenten.
- Familienzuschlag-Checkliste für Nachweise.

## Sperre gegen Überbehauptung

Der Skill darf nicht schreiben „Versorgungsempfänger haben sicher denselben Nachzahlungsanspruch wie aktive Beamte". Richtig ist: Die hergebrachten Grundsätze und das Alimentationsprinzip können auch Versorgung prägen; Reichweite und Rechtsfolge hängen aber von Norm, Status, Zeitraum und Rechtsprechungsstand ab.
