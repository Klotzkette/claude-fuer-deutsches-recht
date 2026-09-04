---
name: kg-personengesellschaften
description: "Für KG und Personengesellschaften: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Mittelstands-Corporate/M&A."
---

# KG und Personengesellschaften

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KG und Personengesellschaften` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: KG und Personengesellschaften
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier KG und Personengesellschaften und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- Registerauszüge, Gesellschafterliste, Satzung, Geschäftsordnungen und Vollmachten.
- Organbeschlüsse, Zustimmungskataloge, Vollmachtsketten und Notartermine.
- Cap Table, Beteiligungskette, Umwandlungs- oder Carve-out-Plan.

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
- GmbHG §§ 15, 16, 40 und 46 für Anteilsübertragung, Gesellschafterliste und Beschlüsse.
- AktG §§ 76, 93, 111, 179a und 186 für Leitung, Business Judgment und Strukturmaßnahmen.
- HGB §§ 8 ff., 15 und §§ 161 ff. für Registerpublizität und Personengesellschaften.
- UmwG §§ 2, 123, 190 ff. für Verschmelzung, Spaltung und Formwechsel.

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
- `/mittelstand-corporate-ma:gesellschaftsrecht-register` - wenn Registerstand, Gesellschafterliste, Organstellung oder Vollmachtskette geprüft werden müssen.
- `/mittelstand-corporate-ma:handelsregisterabruf` - wenn der offizielle Registerstand belegt werden muss.
- `/mittelstand-corporate-ma:transaktionsstruktur` - wenn Share Deal, Asset Deal, Carve-out, Umwandlung oder Holdingstruktur verglichen werden.
- `/mittelstand-corporate-ma:umwandlungsrecht` - wenn Verschmelzung, Spaltung, Formwechsel oder Ausgliederung strukturiert werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-board-paper-business-judgment` - wenn Organentscheidung und Business-Judgment-Dokumentation vorbereitet werden.

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

### KG und Personengesellschaften

## Triage — klaere vor Beginn

1. Welche Rechtsform liegt vor — OHG, KG, GmbH & Co. KG, PartG, PartGmbB, Limited Partnership?
2. Soll eine Kommanditistenstellung uebertragen werden — Anteilsuebertragung, Teileintritt, Erhöhung Einlage?
3. Wie hoch ist die Hafteinlage und die tatsaechlich geleistete Einlage — sind Haftungsvoraussetzungen (§§ 171-172 HGB) durch Einlagenrueckgewaehr veraendert worden?
4. Sind Vollmachten und Vertretungsregelungen aktuell — wer ist Komplementaer und wie wird er vertreten?
5. Gilt das Gesellschaftsregister nach MoPeG (GbR-Register) — Eintragungspflicht für GbR?
6. Gibt es Fondsstrukturen (z.B. Investmentkommanditgesellschaft § 124 KAGB)?

## Zentrale Rechtsgrundlagen

- §§ 161-177 HGB — KG: Kommanditistenhaftung bis zur Höhe der Einlage; Haftung erneut auflebt nach Rueckgewaehr (§ 172 Abs. 4 HGB)
- §§ 171-172 HGB — Haftung des Kommanditisten: nur bis zur Einlage; haftet erneut, wenn Einlage herabgesetzt oder zurueckgezahlt wird
- § 706 BGB n.F. (MoPeG) — Gesellschaftsregister für GbR; Eintragungspflicht ab 01.01.2024; Grundstuckserwerb nur als eingetragene GbR (eGbR) möglich
- §§ 705-740 BGB n.F. (MoPeG) — modernisiertes Personengesellschaftsrecht ab 01.01.2024
- § 124 KAGB — Investmentkommanditgesellschaft (InvKG): Sonderform für Fondsvehikel; Aufsicht BaFin
- §§ 1 Abs. 3, 48 ff. HGB — Prokura und Handelsvollmacht: massgeblich für Vertretung in der KG
- § 16 GmbHG analog für Kommanditistenwechsel — Gesellschafterliste-Gedanke: Eintragung im HR als Legitimationsakt

## Schritt-für-Schritt-Workflow

1. **Rechtsform und Gesellschaftsvertrag prüfen:** aktueller HR-Auszug HRA, Gesellschaftsvertrag, Kommanditistenliste
2. **Haftungslage klaren:** Hafteinlage vs. tatsaechlich geleistete Einlage; Einlagenrueckgewaehr-Prüfung (§ 172 Abs. 4 HGB) für alle relevanten Zahlungen der letzten 5 Jahre
3. **Vertretungsmacht feststellen:** Komplementaer (in GmbH & Co. KG: GmbH-Geschaftsfuehrer); Prokura; Gesamtvertretung?
4. **Kommanditistenwechsel (falls vorgesehen):** Abtretungsvertrag, HR-Anmeldung, Gesellschaftsvertrag-Zustimmungspflicht prüfen
5. **MoPeG-Compliance:** GbR-Register geprueft? Bei Grundstucksbesitz: Eintragung als eGbR erforderlich (§ 706 BGB n.F.)
6. **Fondsvehikel (§ 124 KAGB):** BaFin-Genehmigung, Anlagebedingungen, KAGB-Compliance
7. **Stimmrechts- und Abstimmungsregeln:** Mehrheitserfordernisse im Gesellschaftsvertrag; Stimmrechtsausschluss bei Interessenkonflikten; Protokoll

## Entscheidungsbaum

- Einlage unter Hafteinlage → § 172 Abs. 4 HGB → Aussenhaftung wieder aufgelebt → Red Flag
- Kommanditanteilsuebertragung → Gesellschaftsvertrag Zustimmungsklausel? → Ja: Zustimmung aller Gesellschafter
- GbR mit Grundstueck → MoPeG § 706 BGB n.F. → Eintragung als eGbR erforderlich vor Eigentumsuebergang
- InvKG § 124 KAGB → BaFin zuständig → besondere Anforderungen an Verwaltung und Anleger

## Output-Template: KG-Checkliste

**Adressat:** Deal-Team intern — Tonfall sachlich-strukturiert

```
KG-CHECKLISTE
Gesellschaft: [NAME] — HR-Nr.: [HRA XXXX]

EINLAGEN
 Hafteinlage Kommanditist [NAME]: [BETRAG] EUR
 Geleistete Einlage: [BETRAG] EUR
 Einlagenrueckgewaehr geprueft: [ ] JA [ ] NEIN → § 172 IV HGB

VERTRETUNG
 Komplementaer: [NAME] — Einzelvertretungsbefugnis: [ ] JA [ ] NEIN
 Prokura: [NAME]

ANTEILSUEBERTRAGUNG
 Zustimmung GV erforderlich: [ ] JA [ ] NEIN
 Abtretungsvertrag formfrei: [ ] JA — Notarpflicht: [ ] NEIN

REGISTER
 HR-Eintrag Kommanditistenwechsel: [ ] OK [ ] offen
 MoPeG eGbR: [ ] nicht relevant [ ] Eintragung erforderlich bis [DATUM]
```

## Rote Schwellen

- Einlagenrueckgewaehr ohne Prüfung: Aussenhaftung des Kommanditisten unerkannt
- Vertretungsmacht unklar: Signing-Vollmacht angreifbar
- MoPeG-Eintragungspflicht versaeumt: Grundstueckserwerb scheitert

## Standardausgabe

- KG-Checkliste mit Haftungs- und Vertretungsanalyse
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe

## Übergabe an andere Skills

- Gesellschaftsrecht/Register → `mittelstand-corporate-ma-gesellschaftsrecht-register`
- Transaktionsstruktur → `mittelstand-corporate-ma-transaktionsstruktur`
- Handelsregisterabruf → `mittelstand-corporate-ma-handelsregisterabruf`

## Vorlagen

- assets/templates/kg-checkliste-einlage-vertretung.md
- assets/templates/kommanditisten-abtretungsvertrag.md

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
