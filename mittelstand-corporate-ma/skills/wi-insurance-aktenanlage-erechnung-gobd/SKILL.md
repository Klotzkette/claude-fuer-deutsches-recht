---
name: wi-insurance-aktenanlage-erechnung-gobd
description: "WI Insurance Aktenanlage Erechnung Gobd: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# WI Insurance Aktenanlage Erechnung Gobd

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **WI Insurance Aktenanlage Erechnung Gobd** im Plugin Mittelstand Corporate Ma. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mittelstand-corporate-ma-wi-insurance` | W&I-Versicherung: W&I-Prozess, Underwriting, DD-Berichte, Deckungsausschluesse, AI-DD-Transparenz, Synthetic Warranties, Materiality Scrape und Disclosure Letter für M&A. |
| `mittelstand-ma-aktenanlage` | Kanzlei eroeffnet neue Deal-Akte für M&A-Mandat: Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel Vertraulichkeitsstufen Closing-Bible-Grundgeruest. Normen BRAO §§ 43 50 Aktenaufbewahrungspflicht DSGVO. Prüfraster Vollständigkeit Akte Vertraulichkeitseinstufung Zugriffskontrolle. Output Aktenstruktur-Template Aktenzeichen-Schema Zugriffsmatrix. Abgrenzung zu matter-file (Workspace) und mittelstand-ma-tabellenreview (Daten). |
| `mittelstand-ma-erechnung-gobd` | Kanzlei braucht GoBD-konforme E-Rechnung für M&A-Mandat: XRechnung-XML ZUGFeRD Workstream-Abrechnung revisionssicheren Buchungsnachweis. Normen GoBD BMF-Schreiben 2019 UStG §§ 14 14a ZUGFeRD EN 16931. Prüfraster Pflichtfelder XRechnung Pflichtangaben Narrative Revisionssicherheit Archivierung. Output XRechnung-XML ZUGFeRD-Paket Buchungsnachweis. Abgrenzung zu billing-narratives (Texterstellung) und mittelstand-ma-tabellenreview (Datenprüfung). |
| `mittelstand-ma-insolvenzreife` | Unternehmen in M&A-Situation oder Krise und Anwalt prüft ob Insolvenzantragspflicht besteht: Zahlungsunfähigkeit drohende Zahlungsunfähigkeit Überschuldung StaRUG-Schwelle. Normen §§ 17-19 InsO § 15a InsO §§ 1-4 StaRUG. Prüfraster Zahlungsunfähigkeitstest Überschuldungsprüfung Fortbestehensprognose Antragspflicht-Timing. Output Insolvenzreife-Ampel Antragspflicht-Gutachten Handlungsempfehlung. Abgrenzung zu restructuring-starug-insolvenzplan (Plangestaltung) und liquiditaetsvorschau (Cash-Modell). |

## Arbeitsweg

Im Plugin Mittelstand Corporate Ma gilt für **WI Insurance Aktenanlage Erechnung Gobd**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mittelstand-corporate-ma-wi-insurance`

**Fokus:** W&I-Versicherung: W&I-Prozess, Underwriting, DD-Berichte, Deckungsausschluesse, AI-DD-Transparenz, Synthetic Warranties, Materiality Scrape und Disclosure Letter für M&A.

# W&I-Versicherung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `W&I-Versicherung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: W&I-Versicherung
- **Spezialgegenstand:** W&I-Versicherung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Zweck
Dieser Skill führt ein Mittelstands-Corporate/M&A-Mandat durch den Arbeitsbereich **SPA/APA, Disclosure, Signing, Closing und Post-Closing-Mechanik**. Er macht aus unvollständigen Unternehmerunterlagen einen belastbaren Deal-Befund, trennt gesicherte Tatsachen von Annahmen und übersetzt juristische Risiken in einen nächsten praktischen Schritt. Adressaten sind Partner, Counsel, Associates, Steuerberater, Inhouse-Verantwortliche und Unternehmer in mittelständischen Transaktionen.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier W&I-Versicherung und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das für einen Unternehmenskauf oder -verkauf aus Sicht von Käufer, Verkäufer oder Zielgesellschaft."
- "Mach daraus eine kurze Mandantenunterlage mit Risiken, offenen Punkten und To-dos."
- "Welche Dokumente, Registerauszüge, Freigaben oder Fristen fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst das Mandat selbst angelegt, die Deal-Phase bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/mittelstand-corporate-ma:mittelstand-corporate-ma-kommandocenter` oder `/mittelstand-corporate-ma:mittelstand-corporate-ma-matter-file`. Wenn der Nutzer nur eine kurze Unternehmer-E-Mail will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/mittelstand-corporate-ma/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Rolle, Deal-Typ, Zielgesellschaft, Käufer/Verkäufer, Steuerberater/Notar, Signing-/Closing-Zeitplan, Budgetrahmen und gewünschtes Output-Format.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Gesellschafter-/Beiratsfreigaben.
- Disclosure Letter, Knowledge-Definition, W&I- oder Verkäufergarantie-Struktur.

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

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Deal-Schritt rechtlich tragfähig, praktisch vollziehbar und für die gewählte Mandatsseite wirtschaftlich sinnvoll steuerbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird. Maßgeblich sind Mandatsvereinbarung, Konfliktprüfung und Vertraulichkeitsrahmen. Ist die Rolle unklar, darf kein parteilicher Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Wirksamkeit und Corporate Authority.** Bei Anteils- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Beirats- oder Gesellschafterentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Closing-Fähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

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
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-spa-apa-entwurf` - wenn der Befund in SPA/APA-Entwurf oder Klausellogik einfließen soll.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-vertragsmarkup-key-issues` - wenn Markup-Abweichungen in Key Issues und Verhandlungslinien übersetzt werden müssen.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/mittelstand-corporate-ma:mittelstand-corporate-ma-closing-bible-archiv` - wenn executed documents, Registerbelege und Closing Bible gesichert werden müssen.

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

# W&I-Versicherung

## Zweck

Bereitet W&I-Prozess (Warranty and Indemnity Insurance), Underwriting, DD-Berichte, Deckungsausschluesse und AI-DD-Transparenz vor. Sichert Versicherungsschutz fuer Garantieverletzungen im SPA.

## Triage

1. Ist W&I-Versicherung vom Kaeufer oder Verkaeufer beabsichtigt — Buy-side oder Sell-side Policy?
2. Liegt ein vollstaendiger Red-Flag-Report und ein ausgefuellter Disclosure Letter vor — Underwriter verlangen vollstaendige DD-Dokumentation?
3. Welche Garantien sollen versichert werden — alle Business Warranties, oder nur Title und Financial Statements?
4. Ist ein Materiality Scrape vorgesehen — entfaellt die Materiality-Schwelle fuer Versicherungsansprueche?
5. Wurden Synthetic Warranties vereinbart (warranties ohne SPA-Basis, nur fuer Versicherungszwecke)?
6. Wurden DD-Tools mit KI-Unterstuetzung eingesetzt — Underwriter verlangen Transparenz ueber KI-basierte DD-Methodik?

## Zentrale Rechtsgrundlagen

- §§ 443, 311 BGB — selbstaendige Garantie als Haftungsgrundlage; W&I-Versicherung tritt als Schuldnerin ein wenn Garantie verletzt
- § 61 VVG — Obliegenheitsverletzung bei arglistiger Taeusching: Versicherung kann leistungsfrei werden; gilt auch fuer bewusste Falschaussagen in Underwriting-Unterlagen
- § 123 BGB — arglistige Taeusching durch Verkaeufer: Disclosure Letter schutzt nicht bei Arglist; Versicherer kann Regress nehmen
- § 254 BGB — Mitverschulden des Kaeuf ers: mangelnde DD koennte Versicherungsanspruch mindern
- Art. 22 DSGVO — Entscheidung durch automatisierte Verarbeitung: bei KI-gestuetzter DD koennte Bewertung Versicherungsanspruch beeinflussen; Transparenzpflicht

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **W&I-Struktur entscheiden:** Buy-side (Kaeufer versichert sich gegen Garantienverletzung des Verkaeuf ers) vs. Sell-side (Verkaeufer versichert seine Haftung); Buy-side in Europa Standard
2. **Underwriting-Unterlagen zusammenstellen:** Vollstaendiger DD-Report, Red-Flag-Report, Disclosure Letter, DD-Fragenliste und Antworten, SPA-Entwurf
3. **AI-DD-Transparenz-Erklaerung:** falls KI-gestuetzte Datenraumanalyse eingesetzt — Methodik, Prueftiefe, Human-in-the-loop-Verfahren an Underwriter kommunizieren
4. **Deckungsausschluesse verhandeln:** bekannte Risiken, Environmental, Cyber, Steuern (oft Teil-Ausschluss), Pension Deficits; Ausschlussliste mit SPA-Risiken abgleichen
5. **Materiality Scrape vereinbaren:** bei Scrape wird die Materiality-Schwelle der SPA-Garantien fuer Versicherungsansprueche ignoriert
6. **Synthetic Warranties:** fuer Garantien, die nicht im SPA stehen, aber Underwriter versichern wollen; separater Synthetic Warranty Schedule
7. **Bindungsbestaetigung einholen:** Underwriter Confirmation als W&I-Closing CP
8. **Notification-Pflichten postClosing:** Garantieverletzung innerhalb der Notification-Frist (haeufig 7 Tage nach Kenntnis) dem Versicherer melden

## Entscheidungsbaum

- Buy-side W&I → Kaeufer zahlt Praemie → Verkaeuf er haftet nur noch bis Basket → ggf. Seller clean exit
- Bekanntes Risiko → Disclosure Letter → Ausschluss aus W&I-Deckung → Freistellung im SPA erwaegen
- KI-gestuetzte DD → Underwriter-Transparenz-Anforderung → Methodik dokumentieren; Human-in-the-loop-Protokoll
- Synthetic Warranties → Warranty nicht im SPA → nur durch spezifischen Schedule versicherbar

## Output-Template: W&I-Underwriting-Checkliste

**Adressat:** Versicherer / Deal-Team — Tonfall sachlich-strukturiert

```
W&I-UNDERWRITING-CHECKLISTE
Deal: [DEALNAME] — Datum: [DATUM]

UNTERLAGEN FUER UNDERWRITER
[ ] Red-Flag-Report (vollstaendig, datiert)
[ ] Disclosure Letter (mit Anlagen)
[ ] DD-Scope-Beschreibung (Methodik, Tools, Human-in-the-loop)
[ ] SPA-Entwurf, letzter Stand
[ ] Fragen/Antworten DD-Prozess (Q&A-Protokoll)

DECKUNGSAUSSCHLUESSE (BEKANNTE RISIKEN)
[ ] Umwelthaftung: [BESCHREIBUNG]
[ ] Steuerrisiko: [BESCHREIBUNG]
[ ] [WEITERE AUSSCHLUESSE]

MATERIALITY SCRAPE: [ ] Vereinbart [ ] Nicht vereinbart
SYNTHETIC WARRANTIES: [ ] Vorhanden (Schedule: [NAME]) [ ] Nicht vorhanden

PRÄMIE: ca. [X %] der Versicherungssumme
VERSICHERUNGSSUMME: [BETRAG EUR] entspricht [X %] des Kaufpreises
BINDUNGSBESTAETIGUNG FRIST: bis [DATUM]
```

## Rote Schwellen

- Unvollstaendiger DD-Report an Underwriter: Underwriter kann Deckung anfechten
- Bekannte Risiken nicht discloset: Arglist; Versicherung wird leistungsfrei (§ 28 VVG)
- Notification-Frist versaeumt: Deckungsverlust

## Standardausgabe

- W&I-Underwriting-Checkliste
- Deckungsausschluss-Tabelle
- Notification-Protokoll

## Uebergabe an andere Skills

- DD-Findings → `mittelstand-corporate-ma-due-diligence-legal`
- Disclosure → `mittelstand-corporate-ma-disclosure-schedules`
- SPA → `mittelstand-corporate-ma-spa-apa-entwurf`

## Vorlagen

- assets/templates/wi-versicherung-checkliste.md
- assets/templates/wi-underwriting-disclosure.md

## 2. `mittelstand-ma-aktenanlage`

**Fokus:** Kanzlei eroeffnet neue Deal-Akte für M&A-Mandat: Aktenzeichen Parteienregister Ordnerstruktur Datenraumspiegel Vertraulichkeitsstufen Closing-Bible-Grundgeruest. Normen BRAO §§ 43 50 Aktenaufbewahrungspflicht DSGVO. Prüfraster Vollständigkeit Akte Vertraulichkeitseinstufung Zugriffskontrolle. Output Aktenstruktur-Template Aktenzeichen-Schema Zugriffsmatrix. Abgrenzung zu matter-file (Workspace) und mittelstand-ma-tabellenreview (Daten).

# Freistehende M&A-Aktenanlage (Mittelstand)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freistehende M&A-Aktenanlage (Mittelstand)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freistehende M&A-Aktenanlage (Mittelstand)
- **Spezialgegenstand:** Freistehende M&A-Aktenanlage (Mittelstand) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Kernsachverhalt

Im Mittelstands-M&A sind die Transaktionen häufig vom Gesellschafter-Geschäftsführer geprägt: Familienunternehmen, Nachfolgelösungen, Gesellschafterwechsel, Management-Buy-out oder -in (MBO/MBI) und strategische Zukäufe mittelständischer Käufer. Die Aktenanlage muss diese besonderen Strukturmerkmale abbilden — fehlende externe DD-Teams, begrenzte Ressourcen auf Verkäuferseite, häufig keine W&I-Versicherung und oft kürzere Zeitpläne. Dennoch gelten dieselben Dokumentationspflichten des Anwalts (§ 50 BRAO, GwG) und dieselben berufsrechtlichen Sorgfaltspflichten. Der Skill strukturiert die Mittelstands-Transaktion von der ersten Kontaktaufnahme bis zur Closing Bible, angepasst an schlanke Prozesse ohne Großkanzlei-Infrastruktur.

## Kaltstart-Rückfragen

1. Wer ist der Mandant — Verkäufer (Gesellschafter, Gesellschafter-GF), Käufer (strategisch, MBO/MBI), Finanzierungspartner?
2. Handelt es sich um eine Unternehmensnachfolge? Gibt es familiäre oder erbrechtliche Aspekte (Testament, vorweggenommene Erbfolge, Pflichtteil)?
3. Wie lautet der vorläufige Deal-Code? Welche Zielgesellschaft — GmbH, GmbH & Co. KG, Einzelkaufmann (e.K.)?
4. Welche Deadline ist realistisch — häufig 3–6 Monate im Mittelstand statt 12–18 Monate in Large-Cap?
5. Gibt es existierende Gesellschafterverträge, Stimmbindungsverträge, Erbverträge oder Testamente, die die Transaktion beeinflussen?
6. Ist eine externe Finanzierung (Hausbank, KfW, Beteiligungsgesellschaft) vorgesehen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Relevante Normen

| Norm / Regel | Regelungsinhalt |
|---|---|
| § 50 BRAO | Pflicht zur Führung einer geordneten Handaktenführung; Aufbewahrungspflicht 5 Jahre |
| §§ 5, 6 GwG | Sorgfaltspflichten bei Mandatsannahme; KYC; Identifizierung des wirtschaftlich Berechtigten |
| § 40 GmbHG | Gesellschafterliste; aktuelle Version zwingend für Anteilsübertragung |
| § 15 GmbHG | Form der Anteilsübertragung: notarielle Beurkundung erforderlich |
| §§ 2032 ff. BGB | Erbengemeinschaft: gemeinschaftliche Verwaltung; Einzelner kann Anteil nicht allein übertragen |
| § 29 GmbHG | Gesellschafterbeschluss zur Veräußerung von Gesellschaftsanteilen; ggf. Zustimmungspflicht |
| § 43 GmbHG | Geschäftsführerhaftung; Handlungspflichten bei Transaktionen |
| §§ 1 ff. GmbHG, AktG | Gesellschaftsform-spezifische Regelungen |

### Leitentscheidungen

| Gericht | Az. | Datum | Leitsatz (kurz) |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema / Anlage-Checkliste (Mittelstand-angepasst)


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Status |
|---|---|---|---|
| 1 | KYC / Mandatsannahme | GwG-Identifikation; bei Familienunternehmen: wirtschaftlich Berechtigte (>25 %) identifizieren; Erbengemeinschaft prüfen | TODO / OK |
| 2 | Matter Opening Card | Deal-Code, Aktenzeichen, Mandant, Zielgesellschaft, Gegenseite, Vertraulichkeit, Deadline | Angelegt |
| 3 | Gesellschaftsrechtliche Grundstruktur | HRB/HRA, Gesellschafterliste (§ 40 GmbHG), Satzung, Gesellschaftervereinbarungen | Struktur klar |
| 4 | Nachfolgerechtliche Dimension | Testament, Erbvertrag, vorweggenommene Erbfolge, Pflichtteilsrechte; ggf. Steuerberater für Schenkungssteuer | Erbrecht geprüft |
| 5 | Zustimmungspflichten | Gesellschaftsvertrag: Zustimmung der Gesellschafterversammlung erforderlich? Vinkulierung? | Zustimmung gesichert |
| 6 | Ordnerstruktur anlegen | 00_Admin bis 90_Archive; angepasst an Mittelstand: ggf. ohne separate Regulatory/PMI-Folder | Struktur angelegt |
| 7 | Datenraumspiegel (ggf. vereinfacht) | Mittelstand nutzt oft USB-Stick, Dropbox, SharePoint — Dokumentation des Übergabemodus | Spiegel/Nachweis |
| 8 | Finanzierungsstruktur | Hausbank-Finanzierung, KfW-Förderung, Beteiligungsgesellschaft; Letter of Intent Bank vorhanden? | Finanzierung klar |
| 9 | Notar-Termin vormerken | § 15 GmbHG: notarielle Beurkundung; Notar frühzeitig kontaktieren; Wartezeiten einplanen | Notar-Termin |
| 10 | Fristen-Kalender | LOI, DD-Phase, Signing, Closing, Behördenfrist (bei Fusionskontrolle), Long-Stop-Date | Kalender angelegt |
| 11 | Closing-Bible-Index | SPA, Abtretungsurkunde, Gesellschafterliste (neu), Freigaben, Zahlungsnachweis | Index vorbereitet |
| 12 | Vertraulichkeitsregeln | NDA oder konkludente Vertraulichkeit; Datenschutz (DSGVO) für Mitarbeiterdaten | Regeln dokumentiert |
| 13 | Steuerberater einbinden | Unternehmensbewertung, steuerliche Strukturierung (§ 8b KStG, Schenkungsteuer, § 6b EStG) | Berater-Loop |
| 14 | Signing-Vorbereitung | Unterschriftenliste, Vollmachten, notarielle Formvorschriften; Clearing erforderlicher Zustimmungen | Signing-Plan |
| 15 | Archivierung | § 50 BRAO: 5 Jahre; DSGVO-konforme Archivierung; Originalurkunden beim Notar | Archivplan |

## Mittelstand-spezifische Besonderheiten

| Thema | Mittelstand | Großkanzlei |
|---|---|---|
| Datenraum | Oft USB-Stick, SharePoint, Dropbox — Protokoll anlegen | Professionelle VDR-Plattform (Intralinks, Datasite) |
| W&I-Versicherung | Selten; stattdessen höherer Garantiekatalog im SPA | Standard bei > EUR 10 Mio. Transaktionsvolumen |
| DD-Team | Oft nur 1–2 Anwälte + Steuerberater | Multi-Workstream, viele Berater |
| Zeitplan | 3–6 Monate | 6–18 Monate |
| Nachfolgerecht | Häufig relevant (Erbrecht, Testament, Familienstrategie) | Selten relevant |
| Kaufpreisfinanzierung | Hausbank + KfW + Eigenkapital Käufer | Leveraged Finance, PE-Strukturen |
| Fusionskontrolle | Selten (Umsatzschwellen oft unterschritten) | Häufig GWB/EU-FKVO |

## Beweislast / Dokumentationspflichten

| Anforderung | Norm | Konsequenz |
|---|---|---|
| Handaktenführung | § 50 BRAO | Beweislastumkehr im Regressfall |
| GwG-Identifikation | §§ 5, 6 GwG | Bußgeld; Meldepflicht |
| Notarielle Form | § 15 GmbHG | Nichtigkeit der Abtretung bei Formverstoß |
| Zustimmungspflicht | Gesellschaftsvertrag | Schwebende Unwirksamkeit; Anfechtbarkeit |

## Fristen und Aufbewahrung

| Fristtyp | Dauer | Norm |
|---|---|---|
| Handaktenaufbewahrung | 5 Jahre nach Mandatsabschluss | § 50 Abs. 2 BRAO |
| GwG-Aufbewahrung | 5 Jahre | § 8 GwG |
| Notarielle Urkunden | 30 Jahre beim Notar | § 51 BNotO |
| DSGVO-Aufbewahrung | So lange wie nötig; Löschung nach Zweckfortfall | Art. 5 DSGVO |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — M-and-A-Akte fuer Mittelstand anlegen | Aktenanlage nach Checkliste; Dokumentenvorlage unten |
| Variante A — Sehr kleines Unternehmen KMU einfache Akte | Vereinfachte Akte ohne alle Unterordner |
| Variante B — Familienunternehmen besondere Vertraulichkeit | Strikte Zugangskontrolle; separate Vertraulichkeits-Akte |
| Variante C — Mehrere parallele Interessenten parallel-Track | Parallel-Track-Aktenstruktur; Datenraum koordinieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Matter Opening Card (Mittelstand)

```
MATTER OPENING CARD — VERTRAULICH

Deal-Code: [PROJEKT-NACHFOLGE]
Aktenzeichen: [Kanzlei-AZ]
Datum: [TT.MM.JJJJ]

PARTEIEN
Mandant: [Name, Adresse] — Rolle: [Verkäufer / Käufer]
Zielgesellschaft: [Name, Sitz, HRB, Gesellschaftsform]
Gegenseite: [Name] — vertreten durch [Kanzlei / Steuerberater]

GESELLSCHAFTSRECHTLICHE DATEN
Gesellschafterliste: [Datum, Anlage]
Satzung: [Datum, Version]
Gesellschaftervereinbarungen: [Ja / Nein / TODO prüfen]
Vinkulierung: [Ja / Nein]

NACHFOLGE / ERBRECHT
Testament / Erbvertrag vorhanden: [Ja / Nein / TODO]
Vorweggenommene Erbfolge: [Ja / Nein]
Pflichtteilsberechtigte: [Namen / TODO]

FRISTEN
LOI-Unterzeichnung: [Datum]
Notar-Termin: [Datum]
Signing: [Datum]
Closing: [Datum]
Long-Stop-Date: [Datum]

BERATER
Notar: [Name, Ort]
Steuerberater: [Name]
Hausbank: [Name]

NÄCHSTE AKTION: [Beschreibung] — Owner: [Name] — bis: [Datum]
```

### Baustein 2 — Vereinfachtes Datenraum-Übergabeprotokoll

```
DATENRAUM-ÜBERGABEPROTOKOLL — Projekt [Deal-Code]
Stand: [Datum]

Übergabemodus: [USB-Stick / SharePoint / Dropbox / anderes]
Übergabe durch: [Name, Datum]
Empfang bestätigt durch: [Name, Datum]

ENTHALTENE DOKUMENTE (Inventar)
1. Jahresabschlüsse [Jahr1], [Jahr2], [Jahr3] — Vollständig: [Ja / Nein]
2. Gesellschafterliste (§ 40 GmbHG) — Datum: [Datum]
3. Gesellschaftsvertrag — Version: [Datum]
4. Arbeitsverträge Top-Management — Anzahl: [X]
5. Wesentliche Kundenverträge — Anzahl: [X]
6. Grundbuchauszüge — Anzahl: [X]

DATENLÜCKEN (TODO)
- Steuerbescheid [Jahr] fehlt → TODO [Owner] bis [Datum]
- Pensionsgutachten nicht übergeben → TODO [Owner] bis [Datum]

VERTRAULICHKEITSVERMERK: Alle übermittelten Unterlagen unterliegen dem
Vertraulichkeitsvertrag vom [Datum] (Anlage [X]).
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Strategische Empfehlung

| Akteur | Empfehlung |
|---|---|
| Anwalt (Mittelstand) | Gesellschaftsrechtliche Grundstruktur am Tag 1 prüfen; Vinkulierung und Zustimmungspflichten sofort klären; Nachfolgerecht frühzeitig einbeziehen |
| Käufer | Finanzierungsbestätigung vor DD-Phase einholen; KfW-Förderantrag frühzeitig prüfen; Eigenkapitalnachweis vorlegen |
| Verkäufer | Jahresabschlüsse mindestens 3 Jahre vorlegen; Gesellschafterliste aktualisieren (§ 40 GmbHG); Testament / Erbrecht klären |

## Anschluss-Skills

- `mittelstand-ma-tabellenreview` — Review-Matrix aufbauen
- `mittelstand-ma-liquiditaetsvorschau` — Liquiditätsanalyse starten
- `mittelstand-ma-insolvenzreife` — Insolvenzreife prüfen
- `mittelstand-ma-erechnung-gobd` — Abrechnung vorbereiten

## Quellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 50 BRAO; §§ 5, 6, 8 GwG; §§ 15, 40 GmbHG; §§ 2032 ff. BGB; Art. 5 DSGVO

## Ergaenzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `mittelstand-ma-erechnung-gobd`

**Fokus:** Kanzlei braucht GoBD-konforme E-Rechnung für M&A-Mandat: XRechnung-XML ZUGFeRD Workstream-Abrechnung revisionssicheren Buchungsnachweis. Normen GoBD BMF-Schreiben 2019 UStG §§ 14 14a ZUGFeRD EN 16931. Prüfraster Pflichtfelder XRechnung Pflichtangaben Narrative Revisionssicherheit Archivierung. Output XRechnung-XML ZUGFeRD-Paket Buchungsnachweis. Abgrenzung zu billing-narratives (Texterstellung) und mittelstand-ma-tabellenreview (Datenprüfung).

# Freistehender Billing-, GoBD- und E-Rechnungs(Mittelstand)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freistehender Billing-, GoBD- und E-Rechnungs(Mittelstand)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freistehender Billing-, GoBD- und E-Rechnungs(Mittelstand)
- **Spezialgegenstand:** Freistehender Billing-, GoBD- und E-Rechnungs(Mittelstand) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Kernsachverhalt

Mit der Einführung der E-Rechnungspflicht im B2B-Verkehr (§ 14 UStG n.F. ab 01.01.2025 für den Empfang, ab 01.01.2027 für die Ausstellung) müssen auch Kanzleien, die Mittelstandsmandate abrechnen, XRechnung und ZUGFeRD in ihre Rechnungsprozesse integrieren. Gleichzeitig verlangen die GoBD (Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form) unveränderliche, revisionssichere und vollständige Belege. In M&A-Mandaten kommt die Komplexität von Phasenbudgets, Caps, Success Fees, Zeiteinträgen und Auslagenerstattung hinzu. Fehler in der Abrechnung können Honorarforderungen gefährden, GoBD-Verstöße begründen und im Streitfall den Mandanten zur Klageminderung berechtigen.

## Kaltstart-Rückfragen

1. Welche Abrechnungsform gilt — Stundensatz (RVG oder Honorarvereinbarung), Phasenpauschalhonorar, Success Fee, Kombination?
2. Welcher Leistungszeitraum ist abzurechnen — Phase (Signing, Closing, DD), einzelner Workstream, gesamtes Mandat?
3. Wurde ein Budget vereinbart? Gibt es einen Cap? Sind Überschreitungen kommuniziert und genehmigt?
4. Welche Auslagen sind entstanden — Gerichts-/Notarkosten, Reisekosten, externe Berater, Datenbankgebühren?
5. Ist der Mandant ein inländisches Unternehmen (Reverse Charge irrelevant) oder grenzüberschreitend (§ 13b UStG / Art. 196 MwStSystRL)?
6. Welches Rechnungsformat ist erforderlich — Standard-PDF, XRechnung, ZUGFeRD, EDIFACT?
7. Wurden die Zeiteinträge vollständig und mit ausreichendem Narrative dokumentiert (GoBD-Anforderung)?
8. Ist die Rechnungsnummer-Vergabe lückenlos und nicht rückdatiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte

| Norm | Regelungsinhalt (Auszug) |
|---|---|
| § 14 UStG | Pflichtangaben auf Rechnungen; ab 01.01.2025: Empfangspflicht für E-Rechnungen; ab 01.01.2027 (KMU bis 2028): Ausstellungspflicht E-Rechnung im B2B |
| § 14a UStG | Besondere Pflichten bei Bauleistungen, sonstigen Leistungen an Nichtunternehmer, innergemeinschaftliche Leistungen |
| § 13b UStG | Reverse Charge: bei bestimmten Leistungen Steuerschuldner der Leistungsempfänger (z.B. im Ausland ansässiger Leistender) |
| § 15 UStG | Vorsteuerabzug: Rechnungen mit falschen oder fehlenden Pflichtangaben berechtigen nicht zum Vorsteuerabzug |
| §§ 145–147 AO | Buchführungs- und Aufzeichnungspflichten; Aufbewahrungsfristen; Unveränderlichkeit digitaler Belege |
| GoBD (BMF-Schreiben 28.11.2019) | Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form; Unveränderbarkeit, Vollständigkeit, Nachvollziehbarkeit |
| XRechnung (Standard CEN EN 16931) | Europäischer Rechnungsstandard; strukturiertes XML-Format; Pflichtfelder und Validierungsregeln |
| ZUGFeRD (Version 2.3) | Hybridformat: PDF/A-3 mit eingebettetem XML (Factur-X); lesbar für Mensch und Maschine |
| § 4 Abs. 1 BRAO | Anwaltliche Vergütungsvereinbarung: muss schriftlich vereinbart werden; Formvorschriften beachten |
| § 49b BRAO | Verbot der Vereinbarung eines Erfolgshonorars in der Regel; Ausnahme: Inkassomandat; in M&A: Success-Fee-Gestaltung prüfen |

### Leitentscheidungen

| Gericht | Az. | Datum | Leitsatz (kurz) |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema / Billing-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Status |
|---|---|---|---|
| 1 | Zeiteinträge erfassen | Tätigkeiten, Datum, Dauer (in Stunden), Fee Earner, Phase, Workstream, Deliverable | Zeiterfassung vollständig |
| 2 | Narrative formulieren | Kurz, konkret, mandatsbezogen; kein Geheimnisschutz verletzen; nicht zu allgemein | Narrative OK |
| 3 | Workstream-Zuordnung | Jede Leistung Phase (LOI, DD, Signing, Closing), Workstream (Legal, Tax, Finance), Mandatsebene | Zuordnung vollständig |
| 4 | Honorar-Kalkulation | Stundensatz × Stunden; Phasenpauschale; Cap-Prüfung; Überschreitung kommuniziert? | Honorarbetrag EUR [X] |
| 5 | Success Fee prüfen | Zulässigkeit nach § 49b BRAO; Berechnungsbasis (Kaufpreis, EBITDA-Multiplikator); steuerliche Behandlung | Success-Fee-Status |
| 6 | Auslagen erfassen | Notar, Gericht, Reise, externe Berater, Datenbanklizenzen; Belege vorhanden? | Auslagen EUR [Y] |
| 7 | Umsatzsteuer prüfen | Steuersatz 19 %; Reverse Charge bei ausländischem Mandanten (§ 13b UStG); Leistungsort (§ 3a UStG) | USt-Behandlung klar |
| 8 | Pflichtangaben nach § 14 UStG | Name/Adresse, Steuernummer/USt-ID, Rechnungsdatum, Rechnungsnummer, Leistungsbeschreibung, Steuerbetrag | Pflichtangaben vollständig |
| 9 | Rechnungsnummer | Lückenlos, nicht rückdatiert; keine Doppelvergabe; Nummernkreis dokumentiert | Nummernkreis OK |
| 10 | E-Rechnungsformat | XRechnung (Pflicht für öffentliche Auftraggeber, ab 2027 B2B); ZUGFeRD als Alternative | Format festgelegt |
| 11 | XRechnung-XML erstellen | Strukturierter Datensatz nach CEN EN 16931; Pflichtfelder prüfen; Validierung vor Versand | XML valide |
| 12 | ZUGFeRD-Paket (falls nötig) | PDF/A-3 mit eingebettetem XML (Factur-X Level EXTENDED oder EN 16931); Echtheitsprüfung | ZUGFeRD fertig |
| 13 | GoBD-Protokoll | Änderungslog; Storno und Korrekturrechnung dokumentieren; Unveränderbarkeit durch Zeitstempel | GoBD-konform |
| 14 | DATEV-Export | CSV-kompatible Buchungsvorschläge: Buchungsdatum, Buchungstext, Betrag, Konto, Gegenkonto | Export bereit |
| 15 | Versand und Archivierung | E-Rechnung per Peppol oder direkte XML-Übermittlung; Archivierung 10 Jahre (§ 147 AO) | Archiviert |

## GoBD-Anforderungen im Überblick

| GoBD-Kriterium | Anforderung | Typischer Fehler |
|---|---|---|
| Unveränderbarkeit | Rechnung darf nach Erstellung nicht verändert werden; Korrekturen nur durch Storno + Neurechnung | Manuelles Editieren der PDF nach Versand |
| Vollständigkeit | Alle Rechnungen müssen erfasst werden; kein selektives Archivieren | Fehlende Rechnungen in Buchhaltungslücken |
| Ordnung | Belege müssen jederzeit auffindbar und lesbar sein; Indexierung erforderlich | Unstrukturierte E-Mail-Ablage ohne Belegkette |
| Nachvollziehbarkeit | Buchungsweg vom Erstbeleg bis zum Jahresabschluss muss lückenlos sein | Fehlende Verknüpfung zwischen Zeiterfassung und Buchungsbeleg |
| Zeitgerechtheit | Buchungen zeitnah vornehmen; keine systematischen Rückdatierungen | Rechnungen erst Monate nach Leistung gestellt und rückdatiert |
| Aufbewahrung | 10 Jahre für Rechnungen (§ 147 Abs. 1 Nr. 1 AO) | Löschung digitaler Unterlagen nach 6 Jahren |

## E-Rechnung: XRechnung vs. ZUGFeRD

| Merkmal | XRechnung | ZUGFeRD |
|---|---|---|
| Format | Reines XML (UBL oder CII) | PDF/A-3 mit eingebettetem XML |
| Lesbarkeit für Menschen | Nur maschinell lesbar | PDF-Teil für Menschen; XML für Maschinen |
| Pflicht öffentlicher Auftraggeber | Seit 2020 | Alternativ akzeptiert |
| B2B-Pflicht ab 2027 | Ja (CEN EN 16931) | Ja (als Profil EXTENDED oder EN 16931) |
| Validierungstool | KoSIT Validator | Factur-X-Bibliothek |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — E-Rechnung und GoBD-Anforderungen fuer Mittelstand pruefen | GoBD-Checkliste nach Schema; Template unten |
| Variante A — Kanzlei noch in Umstellungsphase kein Vollbetrieb | Uebergangs-Checkliste; Fristen und Schritte dokumentieren |
| Variante B — Mandant nutzt Cloud-Buchhaltung | Cloud-spezifische GoBD-Anforderungen pruefen |
| Variante C — Steuerpruefung laeuft E-Rechnung als Beweismittel | Beweissicherung der E-Rechnungen pruefen; Zugriff sichern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Billing Narrative Ledger

```
BILLING NARRATIVE LEDGER — VERTRAULICH
Projekt: [Deal-Code]
Abrechnungszeitraum: [TT.MM.JJJJ] bis [TT.MM.JJJJ]
Erstellt: [Datum]

| Datum | Fee Earner | Phase | Workstream | Tätigkeit (Narrative) | Dauer (h) | Rate (EUR/h) | Betrag (EUR) |
|------------|------------|----------|------------|----------------------------------------------------------|-----------|--------------|--------------|
| [Datum] | [Partner] | DD | Legal | Prüfung Gesellschaftsvertrag und Gesellschafterliste; | 2,5 | [X] | [Y] |
| | | | | Identifikation Vinkulierungsklausel; Memo an Mandant | | | |
| [Datum] | [Assoc.] | DD | Finance | Überprüfung Jahresabschlüsse 2021–2023; EBITDA-Berein. | 4,0 | [X] | [Y] |
| [Datum] | [Partner] | Signing | Legal | Vertragsverhandlung SPA mit Gegenseite; Textmarkups | 3,0 | [X] | [Y] |
| [Datum] | [Assoc.] | Admin | Admin | Notar-Koordination; Vollmachten vorbereiten | 1,0 | [X] | [Y] |
| | | | | GESAMT: | [Summe] | | EUR [Total] |

AUSLAGEN:
- Notargebühren Urkunde vom [Datum]: EUR [X] (Beleg: Kostenrechnung Anlage [X])
- Reisekosten Meeting [Ort] vom [Datum]: EUR [X] (Beleg: Anlage [X])
GESAMT AUSLAGEN: EUR [Y]

GESAMTBETRAG (netto): EUR [Z]
UMSATZSTEUER (19 %): EUR [Z × 0,19]
RECHNUNGSBETRAG (brutto): EUR [Z + USt]
```

### Baustein 2 — XRechnung-Datensatz (Skizze)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ubl:Invoice xmlns:ubl="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
 xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
 xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">
 <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.3</cbc:CustomizationID>
 <cbc:ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</cbc:ProfileID>
 <cbc:ID>[RECHNUNGSNUMMER]</cbc:ID>
 <cbc:IssueDate>[JJJJ-MM-TT]</cbc:IssueDate>
 <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
 <cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>
 <cbc:BuyerReference>[LEITWEG-ID-MANDANT oder Bestellnummer]</cbc:BuyerReference>
 <!-- Lieferant -->
 <cac:AccountingSupplierParty>
 <cac:Party>
 <cbc:RegistrationName>[KANZLEINAME]</cbc:RegistrationName>
 <cac:PostalAddress><cbc:StreetName>[STRASSE]</cbc:StreetName></cac:PostalAddress>
 <cac:PartyTaxScheme><cbc:CompanyID>DE[USTID]</cbc:CompanyID></cac:PartyTaxScheme>
 </cac:Party>
 </cac:AccountingSupplierParty>
 <!-- Rechnungsposition -->
 <cac:InvoiceLine>
 <cbc:ID>1</cbc:ID>
 <cbc:InvoicedQuantity unitCode="HUR">[STUNDEN]</cbc:InvoicedQuantity>
 <cbc:LineExtensionAmount currencyID="EUR">[NETTOBETRAG]</cbc:LineExtensionAmount>
 <cac:Item><cbc:Description>[LEISTUNGSBESCHREIBUNG KURZ]</cbc:Description></cac:Item>
 <cac:Price><cbc:PriceAmount currencyID="EUR">[STUNDENSATZ]</cbc:PriceAmount></cac:Price>
 </cac:InvoiceLine>
</ubl:Invoice>
```

### Baustein 3 — GoBD-Korrekturrechnung (Storno)

```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

STORNORECHNUNG / KORREKTURRECHNUNG
Rechnungsnummer: [STORNO-NR]
Datum: [TT.MM.JJJJ]

Diese Rechnung storniert die Rechnung Nr. [URSPRUNGS-NR] vom [Datum].

Stornierungsgrund: [z.B. Fehler in der Leistungsbeschreibung / falscher Stundensatz /
Doppelabrechnung einer Position]

Die ursprüngliche Rechnung Nr. [URSPRUNGS-NR] wird hiermit vollständig storniert.
Der gesamte Betrag EUR [X] brutto wird gutgeschrieben.

Anschließend wurde Korrekturrechnung Nr. [KORREKTUR-NR] vom [Datum] erteilt.

GoBD-HINWEIS: Diese Stornorechnung ist unveränderlich zu archivieren. Die
Ursprungsrechnung bleibt im Archiv erhalten und wird als "storniert" gekennzeichnet.
Eine rückwirkende Änderung oder Löschung der Ursprungsrechnung ist unzulässig.
```

## Streitwert und Kosten

| Risiko / Schadensfall | Ansatz | Norm |
|---|---|---|
| GoBD-Verstoß: Rechnungsänderung ohne Storno | Bußgeld bei Betriebsprüfung; Verweigerung Vorsteuerabzug Mandant | GoBD; § 15 UStG |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rückdatierung von Rechnungen | Steuerstrafrecht; § 370 AO | § 370 AO; GoBD |
| Nicht valide XRechnung | Ablehnung durch Empfangssystem; Verzug | KoSIT-Validierungsregeln |

## Strategische Empfehlung

| Akteur | Empfehlung |
|---|---|
| Kanzlei (Billing-Team) | XRechnung-Validierung vor jedem Versand; GoBD-konformes DMS einsetzen; Rechnungsnummernkreis lückenlos führen |
| Mandant (Mittelstand) | E-Rechnungsempfang ab 01.01.2025 sicherstellen; DATEV oder Buchhaltungssystem auf XRechnung/ZUGFeRD umstellen |
| M&A-Partner | Budget-Kommunikation am Ende jeder Phase; Cap-Überschreitung schriftlich genehmigen lassen; Auslagen-Belege zeitnah sammeln |

## Anschluss-Skills

- `mittelstand-ma-aktenanlage` — Rechnungen in Akte einpflegen; Belegkette sichern
- `mittelstand-ma-tabellenreview` — Workstream-Abrechnung reviewen
- `mittelstand-ma-liquiditaetsvorschau` — Honorarplanung in Cashflow einbauen

## Quellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 14, § 14a, § 13b, § 15 UStG; §§ 145–147 AO; GoBD-Erlass BMF 28.11.2019; §§ 4, 49b BRAO; XRechnung CEN EN 16931; ZUGFeRD 2.3 (Factur-X)

## Ergaenzende Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 4. `mittelstand-ma-insolvenzreife`

**Fokus:** Unternehmen in M&A-Situation oder Krise und Anwalt prüft ob Insolvenzantragspflicht besteht: Zahlungsunfähigkeit drohende Zahlungsunfähigkeit Überschuldung StaRUG-Schwelle. Normen §§ 17-19 InsO § 15a InsO §§ 1-4 StaRUG. Prüfraster Zahlungsunfähigkeitstest Überschuldungsprüfung Fortbestehensprognose Antragspflicht-Timing. Output Insolvenzreife-Ampel Antragspflicht-Gutachten Handlungsempfehlung. Abgrenzung zu restructuring-starug-insolvenzplan (Plangestaltung) und liquiditaetsvorschau (Cash-Modell).

# Freistehender Insolvenzreife- und StaRUG-Schwellencheck (Mittelstand)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Freistehender Insolvenzreife- und StaRUG-Schwellencheck (Mittelstand)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Freistehender Insolvenzreife- und StaRUG-Schwellencheck (Mittelstand)
- **Spezialgegenstand:** Freistehender Insolvenzreife- und StaRUG-Schwellencheck (Mittelstand) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, HGB, BGB, UmwG, WpÜG/GWB/AWG je nach Transaktion, Satzung, Geschäftsordnung, Gesellschafterbeschluss und Beiratsordnung.
- **Entscheidende Weiche:** Trenne Dealstruktur, Organbeschluss, Zustimmungsvorbehalt, Informationsrecht, Haftung, Interessenkonflikt und Vollzugsdokument.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Kernsachverhalt

Im Mittelstand ist die Insolvenzreife-Prüfung besonders heikel, weil der Gesellschafter-Geschäftsführer häufig selbst der einzige Entscheidungsträger ist und keine unabhängige Kontrolle stattfindet. Die Antragspflicht (§ 15a InsO) trifft ihn persönlich und ist strafrechtlich bewehrt (§ 15a Abs. 4 InsO). Gleichzeitig liegen die Warnsignale — BWA mit Verlusten, überzogener Kontokorrentkredit, Steuerrückstände, Lieferantensperren — oft offen auf dem Tisch, werden aber als vorübergehend bagatellisiert. In M&A-Prozessen gefährdet die Insolvenzreife des Zielunternehmens nicht nur das Closing, sondern führt auch dazu, dass der Käufer Schadensersatz verlangen kann oder vom Vertrag zurücktreten darf. Für den Berater ist die Dokumentation des Zeitpunkts der Kenntniserlangung von entscheidender Bedeutung.

## Kaltstart-Rückfragen

1. Welches ist der konkrete Anlass — DD-Krisencheck, GF-Beratung, StaRUG-Frühwarnung, laufender M&A-Prozess mit Liquiditätszweifel?
2. Liegen vor: Bankkontoauszüge (aktuell), OPOS Kreditoren, BWA mit SuSa, letzter Jahresabschluss, Steuerrückstandsauskunft?
3. Besteht ein überzogener Kontokorrentkredit? Hat die Hausbank Bedenken geäußert oder Kreditkündigungen angedroht?
4. Sind Steuerrückstände (Finanzamt, Krankenkassen) vorhanden? Gibt es Vollstreckungsankündigungen oder -beschlüsse?
5. Existieren Lieferantensperren oder Vorkasseforderungen als Krisenindikator?
6. Hat der Steuerberater auf Fortführungszweifel hingewiesen (§ 321a HGB analog, Going-Concern)?
7. Welche M&A-Auswirkungen sind zu prüfen — MAC-Trigger, Closing Condition, Kaufpreisminderung?
8. Kennt der GF seine persönliche Haftungsexposition aus § 15b InsO?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte

| Norm | Regelungsinhalt (Auszug) |
|---|---|
| § 17 InsO | Zahlungsunfähigkeit: > 10 % Deckungslücke über 3 Wochen; maßgeblich für Antragspflicht |
| § 18 InsO | Drohende Zahlungsunfähigkeit: Prognosezeitraum 24 Monate; StaRUG-Öffner |
| § 19 InsO | Überschuldung: Passiva > Aktiva (Überschuldungsstatus); positiver Prognose als Korrektiv |
| § 15a InsO | Antragspflicht: GmbH-GF, Vorstand, Liquidator; 3 Wochen (ZU), 6 Wochen (ÜS) |
| § 15a Abs. 4 InsO | Strafbarkeit der Insolvenzverschleppung: bis zu 3 Jahre Freiheitsstrafe oder Geldstrafe |
| § 15b InsO | Zahlungsverbote nach Insolvenzreife; GF haftet persönlich für masseschmälernde Zahlungen |
| § 43 GmbHG | Sorgfaltspflicht des GF: Pflicht zur Liquiditätsüberwachung und frühzeitigen Krisenreaktion |
| § 64 S. 1 GmbHG a.F. | (heute § 15b InsO): GF-Haftung für Zahlungen nach Insolvenzreife; durch Gesetzesreform 2021 in § 15b InsO überführt |
| §§ 1–93 StaRUG | Vorinsolvenzlicher Restrukturierungsrahmen: Zugang nur bei § 18 InsO, nicht bei § 17 oder § 19 InsO ohne Prognose |

### Leitentscheidungen

| Gericht | Az. | Datum | Leitsatz (kurz) |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema (Mittelstand)


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Datenqualität sicherstellen | Bankkontoauszüge, OPOS, BWA, JA, Steuerrückstandsauskunft; Lücken als TODO | Datenlücken-Liste |
| 2 | Krisenindikator-Screening | Überzogener Kontokorrentkredit, Rücklastschriften, Lieferantensperren, Steuerrückstände, GF-Ratlosigkeit | Indikatoren dokumentiert |
| 3 | Liquiditätsstatus erstellen | Aktuelle Banksalden; OPOS fällig < 3 Wochen; Deckungslücke berechnen | Deckungslücke EUR [X] |
| 4 | § 17 InsO-Prüfung | Deckungslücke > 10 %? Dauer > 3 Wochen? Ausreichende Einzahlungen plausibel? | § 17 InsO: [Ja / Nein / unklar] |
| 5 | Kontokorrentkredit-Status | KK ausgeschöpft? Bank hat Limit reduziert? Kreditkündigung droht? | KK-Status |
| 6 | Steuer- und SV-Rückstände | Finanzamt, Krankenkassen, Berufsgenossenschaft; Vollstreckungsbescheide prüfen | Steuer/SV-Schulden |
| 7 | Überschuldungsstatus (§ 19 InsO) | Bilanz-Passiva > Aktiva? Stille Lasten aufdecken: Pensionen, Prozessrisiken, Bürgschaften | Überschuldung: [Ja / Nein] |
| 8 | Fortbestehensprognose | 12 Monate: konkrete Finanzierungszusage, Auftragsbestand, Saisonalität; nicht nur Hoffnung | Prognose: [positiv / negativ] |
| 9 | § 18 InsO / StaRUG-Eignung | Drohende Zahlungsunfähigkeit 24 Monate; COMI in Deutschland; keine laufende Insolvenz | StaRUG: [geeignet / nicht geeignet] |
| 10 | Antragspflicht-Frist | § 15a InsO: Fristbeginn dokumentieren; GF über Strafrechtrisiko informieren | Frist: [Datum] |
| 11 | § 15b InsO-Exposition | Welche Zahlungen seit Insolvenzreife? GF über Rückforderungsrisiko aufklären | Zahlungs-Protokoll |
| 12 | StaRUG-Frühwarnsystem | Restrukturierungsbeauftragter empfehlen? StaRUG-Anzeige? Gläubigergespräch? | StaRUG-Fahrplan |
| 13 | Deal-Impact (M&A) | MAC-Klausel, Closing Condition, W&I-Ausschluss, Kaufpreisminderung durch Net Debt-Erhöhung | Deal Impact Memo |
| 14 | Steuerberater und GF informieren | Schriftlicher Hinweis auf Insolvenzreife und persönliche Haftung; Dokumentation | Hinweis-Schreiben |
| 15 | Senior-Review und Eskalation | Insolvenzrechtsspezialist einbinden; Human-in-the-loop; Mandats-Dokumentation | Eskalation dokumentiert |

## Mittelstand-Krisenindikator-Checkliste

| Indikator | Schwellenwert / Kriterium | Handlungsbedarf |
|---|---|---|
| Kontokorrentkredit | Über 80 % ausgenutzt; Limit-Reduktion durch Bank | Bankgespräch; StaRUG prüfen |
| Rücklastschriften | Mehr als 2 in einem Monat | Sofortige Liquiditätsvorschau |
| Steuerrückstände | Umsatzsteuer > 2 Monate offen | Ratenzahlungsantrag; Insolvenzreife prüfen |
| Lieferantensperren | Vorkasseforderungen > 3 Lieferanten | Verhandlungen; Liquiditätsstatus erstellen |
| Lohnzahlung verzögert | Löhne > 5 Tage nach Fälligkeit | § 17 InsO-Prüfung sofort |
| BWA-Verlust | Kumulierter Verlust > 50 % des Eigenkapitals | § 19 InsO-Prüfung |
| Jahresabschluss-Testat | Prüfer verweigert Testat oder erteilt eingeschränktes Testat | Sofortige Beratung |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Zahlungsunfähigkeit bei Antragspflicht | Insolvenzverwalter | Bankkontoauszüge, OPOS, Rücklastschriften |
| Fortbestehensprognose | GF | Finanzierungszusage (schriftlich), Auftragsbestand |
| Zeitpunkt der Kenntniserlangung | GF / Insolvenzverwalter | BWA, E-Mails, Beraterkorrespondenz, Protokolle |
| Masseschmälernde Zahlungen § 15b | Insolvenzverwalter | Kontoauszüge, Buchungsbelege, Stichtagsdokumentation |

## Fristen und Verjährung

| Fristtyp | Dauer | Norm | Hinweis |
|---|---|---|---|
| Antragspflicht — ZU | 3 Wochen | § 15a Abs. 1 InsO | Strafrechtliche Sanktion § 15a Abs. 4 InsO |
| Antragspflicht — Überschuldung | 6 Wochen | § 15a Abs. 1 InsO | Keine Verlängerung |
| § 15b-Haftung — Verjährung | 3 Jahre ab Kenntnis | §§ 195, 199 BGB | Direkthaftung GF |
| StaRUG-Rahmen | Max. 24 Monate | §§ 31, 33 StaRUG | Bei § 17 InsO kein StaRUG-Zugang |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Insolvenzreife fuer Mittelstand pruefen | Insolvenzreife-Pruefung nach Schema; Schriftsatz unten |
| Variante A — Mittelstand hat noch Gesellschafter-Darlehen | Nachrangigkeit pruefen; Eigen- vs Fremdkapital abgrenzen |
| Variante B — Sanierungs-LOI mit Investor vorhanden | Fortbestehensprognose mit LOI als Grundlage |
| Variante C — Betrieb soll kurzfristig eingestellt werden | Kontrolllierte Liquidation statt Insolvenzantrag pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Hinweisschreiben an GF (Insolvenzreife-Verdacht)

```
ANWALTLICH VERTRAULICH

An: [Name Geschäftsführer]
Von: [Kanzlei]
Datum: [TT.MM.JJJJ]

Betreff: Erste Einschätzung zur Liquiditätslage [Firma GmbH]

Sehr geehrte/r Herr/Frau [Name],

auf Grundlage der uns vorliegenden Unterlagen (Bankkontoauszug [Datum], BWA [Monat],
OPOS Kreditoren [Datum]) teilen wir Ihnen folgende erste Einschätzung mit:

LIQUIDITÄTSSTATUS: Die fälligen Verbindlichkeiten übersteigen die verfügbare Liquidität
um EUR [X] (ca. [Y] %). Dies überschreitet die BGH-Schwelle für Zahlungsunfähigkeit
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

PERSÖNLICHE HAFTUNG: Bei Eintritt der Zahlungsunfähigkeit sind Sie als Geschäftsführer
verpflichtet, innerhalb von 3 Wochen Insolvenzantrag zu stellen (§ 15a InsO). Zahlungen,
die Sie nach Eintritt der Insolvenzreife leisten, können von einem späteren
Insolvenzverwalter von Ihnen persönlich zurückgefordert werden (§ 15b InsO).

EMPFOHLENE MASSNAHMEN:
1. Sofortige Liquiditätsvorschau (nächste 3 Wochen) aufstellen.
2. Steuerberater bis [Datum] konsultieren (aktualisierte BWA und Steuerstatus).
3. Prüfen, ob StaRUG-Frühwarnung eingeleitet werden kann.
4. Insolvenzantrag-Fristbeginn dokumentieren.

Diese Einschätzung ersetzt keine vollständige insolvenzrechtliche Stellungnahme.
Wir empfehlen die sofortige Einschaltung eines Restrukturierungsspezialisten.

[Kanzlei, Unterschrift]
```

### Baustein 2 — Deal-Impact-Memo für den Käufer

```
VERTRAULICH — Deal Impact Memo
Projekt: [Deal-Code]
Datum: [TT.MM.JJJJ]

Liquiditätsstatus Zielgesellschaft: AMPEL ROT (Stand [Datum])

DEAL-AUSWIRKUNGEN:

1. MAC-Klausel (SPA Ziffer [X]): Die festgestellte Liquiditätslücke von EUR [X]
 (> 10 % der fälligen Verbindlichkeiten) könnte als Material Adverse Change
 im Sinne der SPA-Definition zu qualifizieren sein.
 EMPFEHLUNG: Vollzug suspendieren bis zur Klärung.

2. Closing Condition: Garantie der Zahlungsfähigkeit (SPA Ziffer [X]) ist bei
 Zahlungsunfähigkeit nicht erfüllt. Käufer kann Vollzug verweigern.

3. Net Debt Erhöhung: Steuerrückstände EUR [X] und KK-Überziehung EUR [Y] erhöhen
 Net Debt um EUR [Z] → Kaufpreisminderung von EUR [Z] (per SPA-Mechanik).

4. W&I-Versicherung: Police Ziffer [X] schließt Schäden aus, die auf Insolvenzreife
 beruhen. W&I-Broker informieren.

NÄCHSTE SCHRITTE:
TODO [Käufer-Anwalt]: MAC-Analyse abschließen bis [Datum]
TODO [Käufer-GF]: Finanzierungsbereitschaft bei MAC neu bewerten
TODO [W&I-Broker]: Police-Ausschlüsse klären bis [Datum]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Streitwert und Kosten

| Schadensfall | Ansatz | Norm |
|---|---|---|
| § 15b InsO-Haftung GF | Summe masseschmälernder Zahlungen | § 15b InsO |
| StaRUG-Beratungskosten | EUR 30.000–300.000 je nach Komplexität | Budgetplanung GF |
| Kaufpreisminderung (Net Debt) | Betrag der Schulden-Mehrung | SPA Completion Accounts |
| Insolvenzverschleppungsschaden | Gläubigerschaden durch verzögerten Antrag | §§ 823 Abs. 2, 826 BGB |

## Strategische Empfehlung

| Akteur | Empfehlung |
|---|---|
| GmbH-GF | Wöchentlichen Liquiditätscheck durchführen; Steuerberater als Frühwarnsystem nutzen; bei Deckungslücke sofort Anwalt — keine Hoffnung auf Besserung ohne Plan |
| Steuerberater | BWA proaktiv auswerten; Mandant bei Warnsignalen schriftlich hinweisen; Haftungsrisiko aus Schweigen kennen |
| Käufer (Mittelstand-DD) | Insolvenzreife als Closing Condition absichern; MAC-Klausel mit konkretem Liquiditätsschwellenwert; Net-Debt-Stichtag wählen |

## Anschluss-Skills

- `mittelstand-ma-liquiditaetsvorschau` — Detaillierte Liquiditätsplanung
- `corporate-kanzlei-restructuring-starug-insolvenzplan` — StaRUG-Planung
- `mittelstand-ma-aktenanlage` — Dokumentation und Aktenführung
- `anw-insolvenzreife-pruefung-17-19-inso` — Technische Insolvenzprüfung

## Quellen

- § 15a InsO (Insolvenzantragspflicht; Hoechstfrist 3 Wochen bei ZU / 6 Wochen bei UE seit SanInsFoG): https://www.gesetze-im-internet.de/inso/__15a.html
- § 15b InsO (Zahlungsverbot bei Insolvenzreife; rechtsformneutral seit 01.01.2021): https://www.gesetze-im-internet.de/inso/__15b.html
- §§ 17, 18, 19 InsO (Zahlungsunfaehigkeit, drohende ZU, Ueberschuldung): https://www.gesetze-im-internet.de/inso/__17.html
- StaRUG (Unternehmensstabilisierungs- und -restrukturierungsgesetz; in Kraft seit 01.01.2021 durch SanInsFoG, BGBl. I 2020, 3256): https://www.gesetze-im-internet.de/starug/
- §§ 1-93 StaRUG (insbesondere § 29 StaRUG-Plan, § 49 StaRUG-Vollstreckungssperre): https://www.gesetze-im-internet.de/starug/__1.html
- § 43 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__43.html
- §§ 823, 826 BGB (Insolvenzverschleppungs-Haftung gegenueber Glaeubigern als Schutzgesetz iVm § 15a InsO): https://www.gesetze-im-internet.de/bgb/__823.html
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
