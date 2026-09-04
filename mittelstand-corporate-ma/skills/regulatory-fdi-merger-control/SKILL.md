---
name: regulatory-fdi-merger-control
description: "Für Fusionskontrolle und Investitionskontrolle: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Mittelstands-Corporate/M&A."
---

# Fusionskontrolle und Investitionskontrolle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fusionskontrolle und Investitionskontrolle` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Fusionskontrolle und Investitionskontrolle
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Fusionskontrolle und Investitionskontrolle und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- Transaktionsstruktur, Umsätze, Erwerberkontrolle, Zielbranche und Jurisdiktionen.
- Signing-/Closing-Zeitplan, Vollzugsakte und Long-Stop-Date.
- UBO-Daten, PEP-/Sanktionsscreening, Börsennotierung und Insiderlisten.

Arbeite mit diesen Variablen: `deal_name`, `rolle`, `deal_phase`, `target`, `gegenpartei`, `jurisdiktionen`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Deal-Kontext fixieren.** Bestimme Rolle, Phase, Transaktionsstruktur, Zielgesellschaft und Entscheidungsempfänger. Wenn Rolle oder Phase fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste alle Dokumente mit Datum, Version, Quelle, Datenraum-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, öffentliche Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Mittelstandsrealität abbilden.** Prüfe, ob Gesellschafter, Geschäftsführung, Familie, Hausbank, Steuerberater, Notar oder Beirat faktisch mitentscheiden. Dokumentiere informelle Absprachen als Risiko, nicht als Rechtsgrundlage.
4. **Materiality-Schwelle setzen.** Fehlt eine vertragliche Schwelle, arbeite mit pragmatischer Ampel: Dealbreaker, Kaufpreis-/Freistellungsfolge, Closing-Bedingung, Disclosure-only, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Deal-Schritt: Wirksamkeit, Zustimmung, Vollzugshindernis, Haftung, Offenlegung, Frist, Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn ein Registerauszug, eine BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, wirtschaftliche Auswirkung, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder ein kurzes Partner-/Mandantenmemo mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Datenraum-Q&A, SPA-Markup, CP-Tracker, Mandantenmail, Notarcheckliste oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Prüfraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite wirtschaftlich sinnvoll steuerbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- GWB §§ 35 bis 41 für deutsche Fusionskontrolle und Vollzugsverbot.
- AWV §§ 55 ff. und §§ 60 ff. für Investitionsprüfung.
- GwG §§ 10, 11, 12 und 15 für Sorgfaltspflichten und verstärkte Prüfungen.
- MAR Art. 7, 17 und 18 sowie WpÜG bei börsennotierter Zielgesellschaft.

**3. Organ- und Zuständigkeitsprüfung.** Nur wenn der konkrete Arbeitsschritt eine Organentscheidung vorbereitet, Zuständigkeit, Zustimmungsvorbehalte, Interessenkonflikte, Informationsgrundlage und Dokumentation prüfen. Der fachlich passende Haftungs- oder Board-Paper-Skill liefert die dafür einschlägige Rechtsprechung; ARAG/Garmenbeck ist kein Universalanker.

**4. Register- und Gesellschafterlistenlogik.** Nur bei GmbH-Anteilen, Einziehung, Vollmachtskette oder streitiger Legitimation Paragraf 16 und 40 GmbHG sowie Registerstand und materielle Berechtigung getrennt prüfen. Ohne solche Title- oder Legitimationsfrage diesen Prüfstrang auslassen.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Vermieterzustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Closing Condition? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Kündigungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 41 GWB Vollzug gesperrt?` nur bejahen, wenn Zusammenschluss, Schwellen und fehlende Freigabe geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Mittelstand regelmäßig: nicht unterschreiben, nicht closen, nicht offenlegen oder nicht extern versenden, bevor Partner, Steuerteam oder Spezialist freigegeben hat.

## Output-Module
- **Mandantenvermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Issue List:** Finding, Quelle, Risiko, Vertragsfolge, Kaufpreis-/Freistellungsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Gegenseite, Steuerberater, Notar oder Datenraum-Team.
- **Drafting-Anschluss:** Klauselvorschlag, Markup-Kommentar, Disclosure-Punkt, CP-Formulierung oder Mandantenmail.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/mittelstand-corporate-ma:conflict-gwg-sanctions` - wenn Mandatsannahme, GwG, Sanktionen oder Interessenkonflikte ungeklärt sind.
- `/mittelstand-corporate-ma:public-ma-kapitalmarkt-mar` - wenn MAR, WpÜG oder kapitalmarktrechtliche Veröffentlichungspflichten betroffen sind.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-rechtsprechungsrecherche` - als fachlicher Anschluss-Skill.
- `/mittelstand-corporate-ma:steps-plan-pmo` - wenn Termine, CPs, Freigaben und Owner in einen belastbaren Transaktionsplan müssen.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partnerentscheidung über Deal-Taktik, Signing-Freigabe oder Closing-Freigabe.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht DD-Finding, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

### Fusionskontrolle und Investitionskontrolle

## Triage — klaere vor Signing

1. Werden Kartellrechtsschwellen erreicht — weltweite Umsaetze der Beteiligten (§ 35 GWB: 500 Mio. EUR weltweit; 25 Mio. EUR in Deutschland); EU-Schwellen (Art. 1 FKVO: 5 Mrd. EUR / 250 Mio. EUR EU)?
2. Gilt das Vollzugsverbot — § 41 GWB / Art. 7 FKVO: Transaktion darf bis zur Freigabe nicht vollzogen werden (Gun Jumping-Verbot)?
3. Ist der Zielmarkt in einem sensiblen Sektor — Verteidigung, kritische Infrastruktur, Energie, Telekommunikation, Medien, Technologie?
4. Kommt ein FDI-Screening nach § 55 ff. AWV in Betracht — ist der Erwerber eine nichteuropaeische Gesellschaft oder hat nichteuropaeische Eigentuermer?
5. Sind Filings in mehreren Jurisdiktionen erforderlich — USA (HSR Act), UK (CMA), China (SAMR), weitere?
6. Liegen Konzentrationseffekte vor, die eine fusionskontrollrechtliche Prüfung in Phase II erfordern können?

## Zentrale Rechtsgrundlagen

- §§ 35-44 GWB — Zusammenschlusskontrolle: Aufgreifschwellen, Anmeldepflicht, Phase I (1 Monat), Phase II (4 Monate), Vollzugsverbot
- §§ 54-56 GWB — Ministererlaubnis; Nebenbestimmungen; sog. "second chance" nach Untersagung durch BKartA
- Art. 1-4 FKVO (EU-Fusionskontrollverordnung 139/2004) — EU-Fusionskontrolle: Schwellen, Vollzugsverbot Art. 7
- §§ 55-62 AWV — Investitionspruefung: sektorspezifische Prüfung (§ 55 AWV: kritische Infrastruktur u.a.); sektoruebergreifende Prüfung (§ 60 AWV: ab 25 % aus Drittstaaten); Meldepflicht; Genehmigungsvorbehalt
- § 4 Abs. 2 AWG — Untersagungsmacht des BMWK bei Bedrohung der öffentlichen Ordnung oder Sicherheit
- Art. 3 EU-FDI-Screening-VO 2019/452 — Koordinierungsrahmen für nationale FDI-Screenings innerhalb der EU

## Aktuelle Rechtsprechung

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt-für-Schritt-Workflow

1. **Umsatz-Screening:** weltweit und in Deutschland (GWB), in der EU (FKVO), in USA, UK, China — Schwellenwerte der Parteien zusammenstellen
2. **Freigabe-Landkarte erstellen:** je Jurisdiktion: Schwelle erreicht? Filing erforderlich? Zeitplan (Phase I / II)?
3. **Gun Jumping-Protokoll:** Clean Team einrichten, Information Barriers, erlaubter Informationsaustausch vor Freigabe dokumentieren
4. **FDI-Prüfung:** § 55 AWV sektorbezogen vs. § 60 AWV sektorubergreifend prüfen; Erwerber-Herkunft feststellen; Meldepflicht-Fristen
5. **Filing-Vorbereitung:** Zusammenschlusserklaerung für BKartA/Kommission; Kontakte zu Behörden aufnehmen; Remedies-Szenarien vordenken
6. **Zeitplan in CP-Tracker einbauen:** Filing-Datum, Phase-I-Ablauf, Phase-II-Risiko; Longstop-Date anpassen
7. **Vollzugsverbot einhalten:** bis Freigabe kein wirtschaftlicher Einfluss des Erwerbers; Information Barriers; Gun Jumping-Protokoll

## Entscheidungsbaum

- Schwelle GWB § 35 erreicht → Filing BKartA → Phase I 1 Monat → Phase II Risiko? → ggf. 4 Monate
- EU-Schwelle FKVO Art. 1 erreicht → Kommission zuständig (one-stop-shop) → keine nationalen Filings
- Erwerber ausserhalb EU mit >25 % Anteil → § 60 AWV FDI-Prüfung → ggf. Genehmigungsvorbehalt; BMWK
- Sektor Verteidigung/kritische Infra → § 55 AWV → strenges sektorbezogenes Screening

## Output-Template: Freigabe-Landkarte

**Adressat:** Deal-Team, Compliance — Tonfall sachlich-analytisch

```
FREIGABE-LANDKARTE
Deal: [DEALNAME] — Datum: [DATUM]

| Jurisdiktion | Schwelle | Filing erforderlich | Behörde | Phase I | Phase II | Status |
|-------------|---------|---------------------|---------|---------|---------|--------|
| Deutschland | § 35 GWB | ja / nein | Bundeskartellamt | 1 Monat | 4 Monate | offen: Umsatzschwellen belegen |
| EU | Art. 1 FKVO | ja / nein | Europäische Kommission | 25 Arbeitstage | 90 Arbeitstage | offen: EU-Dimension prüfen |
| AWV/FDI | §§ 55, 60 AWV | ja / nein | BMWK | 2 Monate | 4 Monate | offen: sektorbezogenen Bezug prüfen |
| USA | HSR Act | ja / nein | FTC/DOJ | 30 Tage | variabel | offen: US-Nexus prüfen |

VOLLZUGSVERBOT: [ ] Aktiv — kein wirtschaftlicher Vollzug bis [DATUM]
CLEAN TEAM: [ ] eingerichtet — Information Barriers aktiv
```

## Rote Schwellen

- Filing unterlassen trotz Pflicht: Bussgeldhaftung (§ 81 GWB: bis 1 Mio. EUR; Art. 14 FKVO: bis 10 % Konzernumsatz)
- Gun Jumping (Vollzug vor Freigabe): zivilrechtliche Nichtigkeit; Bussgeld; Rueckabwicklung
- FDI-Screening nicht erkannt: Untersagung nach Closing möglich; Behördenzwang zur Entflechtung

## Standardausgabe

- Freigabe-Landkarte (Multi-Jurisdiction)
- CP-Tracker mit Behorderden-Fristen
- Gun Jumping-Protokoll

## Übergabe an andere Skills

- CPs → `mittelstand-corporate-ma-signing-closing-conditions`
- Fristen → `grosskanzlei-ma-fristen-cp-kalender`
- Konflikt/Sanktionen → `mittelstand-corporate-ma-conflict-gwg-sanctions`

## Vorlagen

- assets/templates/freigabe-landkarte-multijurisdiction.md
- assets/templates/gun-jumping-protokoll.md

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
