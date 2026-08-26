---
name: umwandlungssteuerrecht-tabellenreview
description: "Für Umwandlungssteuerrecht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. Fachgebiet: Mittelstands-Corporate/M&A."
---

# Umwandlungssteuerrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO; StaRUG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Umwandlungssteuerrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Umwandlungssteuerrecht
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Umwandlungssteuerrecht und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:mittelstand-corporate-ma-matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- 13-Wochen-Liquiditätsplanung, Insolvenzreife-Check und Fortbestehensprognose.
- Asset-/Share-Deal-Struktur, Verwalter-/Eigenverwaltungsrolle und Zahlungsfluss.
- Anfechtungs-, Haftungs-, Steuer- und Closing-Sicherungsfragen.

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
- InsO §§ 15a, 17, 18, 19, 129 ff., 270 ff. für Insolvenzreife, Antragspflicht und Anfechtung.
- StaRUG §§ 1, 9 ff. und 49 ff. für Früherkennung, Plan und Stabilisierung.
- BGB §§ 134, 138, 280, 311 Abs. 2 und 826 für Haftungs- und Sittenwidrigkeitsfragen.
- UmwStG §§ 20 bis 24 und § 8c KStG nur mit Steuerteam verifizieren.

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-distressed-ma` - wenn Krise, Antragspflicht, Anfechtung oder Liquiditätsplanung entscheidend werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-restructuring-starug-insolvenzplan` - wenn StaRUG, Planoptionen oder Insolvenzplanstruktur geprüft werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

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

### Umwandlungssteuerrecht

## Triage — klaere mit Steuerteam vor Strukturentscheidung

1. Soll die Umwandlung zu Buchwerten erfolgen — §§ 11, 13 UmwStG (Verschmelzung), §§ 15, 20 UmwStG (Spaltung/Einbringung)? Antrag erforderlich?
2. Ist die steuerliche Rueckwirkungsfrist einzuhalten — § 2 Abs. 1 UmwStG: maximal 12 Monate vor Anmeldung beim HR?
3. Gibt es steuerliche Verlustvortraege — § 8c KStG Verlustuntergang bei mehr als 50 % Anteilserwerb in 5 Jahren; Sanierungsklausel § 8c Abs. 1a KStG anwendbar?
4. Ist der Grunderwerbsteuer-Ergaenzungstatbestand ausgeloct — § 1 Abs. 2a, 2b GrEStG: 90 % Anteilsuebergang an grundbesitzender Gesellschaft = GrESt-Pflicht?
5. Welche Sperrfristen sind zu beachten — § 22 UmwStG: 7 Jahre nach Einbringung kein schaedlicher Anteilsverkauf (sonst rueckwirkende Entstrickung)?
6. Gibt es Organschaft (§§ 14-19 KStG) — koennte Umwandlung Organschaft beenden?

## Zentrale Rechtsgrundlagen

- §§ 11-13 UmwStG — Verschmelzung: Ansatz Buchwert/Zwischenwert/gemeiner Wert; Antrag für Buchwert beim Finanzamt; spaetestens mit Einreichung Steuererklarung
- §§ 15, 16 UmwStG — Spaltung: Teilbetriebsvoraussetzung für Buchwertansatz; Ausschlussfrist
- §§ 20-24 UmwStG — Einbringung: Einzeluebertragung oder Ausgliederung gegen Anteile; Buchwert nur wenn qualifizierter Teilbetrieb; Sperrfrist 7 Jahre
- § 22 UmwStG — Sperrfrist-Verletzung: rueckwirkende Entstrickung; Einbringungsgewinn I/II
- § 8c KStG — Verlustuntergang: mehr als 50 % Anteilsuebergang (schaedlicher Beteiligungserwerb) in 5 Jahren fuehrt zum vollstaendigen Verlustuntergang; Ausnahmen: Konzernklausel, stille-Reserven-Klausel, Sanierungsklausel
- §§ 1 Abs. 2a, 2b GrEStG — Grunderwerbsteuer-Ergaenzungstatbestand: 90 % Anteilsuebergang an grundbesitzender Gesellschaft loest GrESt aus; Steuersatz je nach Bundesland 3,5-6,5 %
- § 3a EStG — steuerfreier Sanierungsertrag bei Forderungsverzicht im Sanierungsplan; Voraussetzungen: Sanierungsabsicht, Sanierungseignung, Sanierungsbeitraege aller Gläubiger

## Schritt-für-Schritt-Workflow

1. **Zielstruktur mit Corporate-Team abstimmen:** welche Umwandlungsform (Verschmelzung, Ausgliederung, Formwechsel) ist beabsichtigt?
2. **Verlustvortraege kartieren:** § 8c KStG-Prüfung — bisherige Anteilsuebertragungen der letzten 5 Jahre; Schwellenwerte berechnen; Sanierungsklausel prüfen
3. **Buchwert-Antrag planen:** Antrag beim zuständigen Finanzamt; Frist (§§ 11 Abs. 1, 20 Abs. 2 UmwStG); ohne Antrag: gemeiner Wert = stille Reserven werden aufgedeckt
4. **Rueckwirkungsfristen einhalten:** steuerlicher Abschlussstichtag bestimmen; maximal 12 Monate rueckwirkend (§ 2 Abs. 1 UmwStG); HR-Anmeldung als Fristbeginn
5. **Grunderwerbsteuer prüfen:** grundbesitzende Gesellschaft? § 1 Abs. 2a, 2b GrEStG Schwelle 90 %? Steuersatz; Steuerbefreiung Konzernklausel § 6a GrEStG?
6. **Sperrfrist-Management:** nach Einbringung nach § 20 UmwStG keine schaedliche Veraeusserung für 7 Jahre; § 22 UmwStG Monitoring einrichten
7. **Organschaft-Auswirkungen:** Umwandlung koennte Organschaft beenden; Verlustausgleich und Ergebnisabfuehrungsvertrag prüfen
8. **Steuer-Rueckstellung und Haftungsrisiken im SPA adressieren:** Tax Warranties, Tax Indemnity, Steuer-Freistellungsklausel

## Entscheidungsbaum

- Verlustvortraege vorhanden + mehr als 50 % Anteilserwerb → § 8c KStG → Verlustuntergang → Sanierungsklausel prufen?
- Einbringung ohne Teilbetrieb → § 20 UmwStG Buchwert nicht möglich → stille Reserven aufzudecken → Steuerbelastung
- GrEStG § 1 Abs. 2a/2b → 90 % Schwelle → GrESt-Pflicht → Konzernklausel § 6a GrEStG greifen?
- Sperrfrist-Verletzung → Einbringungsgewinn I oder II → rueckwirkende Steuer bis zu 7 Jahre

## Output-Template: Steuerliche Strukturmatrix

**Adressat:** Steuerteam und Corporate-Team — Tonfall sachlich-analytisch

```
STEUERLICHE STRUKTURMATRIX
Deal: [DEALNAME] — Datum: [DATUM]

| Aspekt | Analyse | Risiko | Massnahme |
|--------|---------|--------|-----------|
| § 8c KStG Verlustuntergang | [Anteil X % in Y Jahren] | [Hoch/Mittel/Gering] | [Antrag/Gestaltung] |
| Buchwertansatz UmwStG | [Antrag moeglich/nicht moeglich] | [Entstrickung] | [Antragstellung bis DATUM] |
| GrESt-Ergaenzungstatbestand | [90 % Schwelle erreicht/nicht] | [GrESt X EUR] | [Konzernklausel] |
| Sperrfrist § 22 UmwStG | [7-Jahres-Frist bis DATUM] | [Einbringungsgewinn] | [Monitoring] |
| Organschaft | [Besteht/Endet durch Umwandlung] | [EAV-Kündigung] | [...] |

Offene Fragen an Steuerteam: [konkrete Frage] — Verantwortlich: [Name] — Frist: [Datum]
```

## Rote Schwellen

- Steuerliche Annahme ungeprüft: sofortiger Abstimmungsbedarf mit Steuerteam vor Signing
- Buchwertantrag vergessen: stille Reserven werden aufgedeckt; Steuerlast kann Transaktion gefaehrden
- § 8c KStG Verlustuntergang nicht erkannt: erhebliche steuerliche Belastung des Kaeufers
- Sperrfrist-Verletzung: Einbringungsgewinn I/II; rueckwirkende Entstrickungssteuer

## Standardausgabe

- Steuerliche Strukturmatrix mit Risikobewertung
- Offene Punkte mit verantwortlicher Person, Frist und Eskalationsstufe
- Belegkette: Normen, BFH-Urteile, Finanzamts-Korrespondenz

## Übergabe an andere Skills

- Umwandlungsrecht → `mittelstand-corporate-ma-umwandlungsrecht`
- Transaktionsstruktur → `mittelstand-corporate-ma-transaktionsstruktur`
- Insolvenzreife → `grosskanzlei-ma-insolvenzreife`

## Vorlagen

- assets/templates/steuerliche-strukturmatrix.md
- assets/templates/umwandlungssteuer-checkliste.md

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
