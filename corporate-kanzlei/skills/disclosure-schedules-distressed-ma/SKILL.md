---
name: disclosure-schedules-distressed-ma
description: "Disclosure Schedules Distressed MA: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Disclosure Schedules Distressed MA

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Disclosure Schedules Distressed MA** im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `corporate-kanzlei-disclosure-schedules` | Disclosure Schedules zum SPA erstellen und prüfen: Verkaeufer offenbart bekannte Risiken um Warranty-Verletzungen nach § 444 BGB (Arglist) zu verhindern; Kaeufer prüft Vollständigkeit. Normen: § 444 BGB, § 311 Abs. 2 BGB (vorvertragliche Pflichten), § 442 BGB (Kenntnis des Kaeufers). Prüfraster: je Warranty-Abschnitt korrespondierender Schedule, Vollständigkeits-Prüfung, W&I-Versicherungs-Schnittstelle. Output Draft Disclosure Schedules, Luecken-Memo, Disclosure-Letter. Abgrenzung: SPA-Entwurf siehe spa-apa-entwurf; W&I-Police siehe wi-insurance. |
| `corporate-kanzlei-distressed-ma` | Prüffeld für corporate kanzlei distressed ma: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

Im Plugin Corporate-Kanzlei (M&A, Gesellschaftsrecht) gilt für **Disclosure Schedules Distressed MA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `corporate-kanzlei-disclosure-schedules`

**Fokus:** Disclosure Schedules zum SPA erstellen und prüfen: Verkaeufer offenbart bekannte Risiken um Warranty-Verletzungen nach § 444 BGB (Arglist) zu verhindern; Kaeufer prüft Vollständigkeit. Normen: § 444 BGB, § 311 Abs. 2 BGB (vorvertragliche Pflichten), § 442 BGB (Kenntnis des Kaeufers). Prüfraster: je Warranty-Abschnitt korrespondierender Schedule, Vollständigkeits-Prüfung, W&I-Versicherungs-Schnittstelle. Output Draft Disclosure Schedules, Luecken-Memo, Disclosure-Letter. Abgrenzung: SPA-Entwurf siehe spa-apa-entwurf; W&I-Police siehe wi-insurance.

# Disclosure Schedules

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Disclosure Schedules` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Disclosure Schedules

- **Corporate-Aufgabe (Disclosure Schedules):** Verkaeufer offenbart bekannte Risiken um Warranty-Verletzungen nach § 444 BGB (Arglist) zu verhindern; Kaeufer prüft Vollständigkeit.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Disclosure Schedules und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- aktueller Vertragsentwurf, Markup, Term Sheet und Annex-/Schedule-Struktur.
- CP-Tracker, Closing Deliverables, Gesellschafter-/Organfreigaben.
- Disclosure Letter, Knowledge-Definition, W&I- oder Garantie-Struktur.

Arbeite mit diesen Variablen: `gesellschaft`, `rolle`, `organ`, `beschlussdatum`, `registerstand`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Corporate-Kontext fixieren.** Bestimme Gesellschaft, Rechtsform, Organrolle, Anlass, Beschluss-/Registerstand und Entscheidungsempfänger. Wenn Rolle oder Rechtsform fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste Dokumente mit Datum, Version, Quelle, Register-/Urkunden-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Organ- und Kompetenzebene trennen.** Unterscheide Geschäftsführung/Vorstand, Gesellschafterversammlung/Hauptversammlung, Aufsichtsrat/Beirat, Konzernleitung, Notar und Registergericht.
4. **Materiality-Schwelle setzen.** Fehlt eine Vorgabe, arbeite mit Ampel: Nichtigkeit/Unwirksamkeit, Anfechtungs-/Haftungsrisiko, Registerhindernis, Zustimmungserfordernis, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Corporate-Schritt: Zuständigkeit, Form, Frist, Mehrheit, Vollmacht, Registerfähigkeit, Haftung und Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn Registerauszug, BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, Rechtsfolge, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder eine Partner-/Organvorlage mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Beschlussentwurf, Board Paper, Registeranmeldung, SPA-Markup, CP-Tracker, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Corporate-Schritt gesellschaftsrechtlich wirksam, registerfähig, organschaftlich vertretbar und für die Mandatsseite praktisch umsetzbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird: Gesellschaft, Organmitglied, Gesellschafter, Investor, Käufer, Verkäufer oder Konzernmutter. Ist die Rolle unklar, darf kein parteilicher Beschluss-, Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Zuständigkeit, Form und Corporate Authority.** Bei Anteils-, Beschluss- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Mehrheit, Form und Registerlage zu prüfen. Relevanter Kern:
- BGB §§ 133, 157, 241 Abs. 2, 280, 311 Abs. 2, 433 und 453 für Kaufvertrag und Auslegung.
- GmbHG §§ 15 und 16 für Anteilsübertragung und Gesellschafterliste.
- AktG §§ 76, 93, 111 und 179a für Leitungs-/Kontrollpflichten und Strukturmaßnahmen.
- BGB § 158 für Closing Conditions und Bedingungseintritt.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Aufsichtsrats- oder Beiratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Beschlussfähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Satzungszustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Registerhindernis? Beschlussmangel? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Haftungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 46 GmbHG Zustimmung erforderlich?` nur bejahen, wenn Satzung, Geschäftsordnung und Maßnahme geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Corporate-Kontext: nicht beschließen, nicht anmelden, nicht signieren, nicht closen oder nicht extern versenden, bevor Partner, Organ oder Spezialist freigegeben hat.

## Output-Module
- **Corporate-Vermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Beschluss-/Board-Paper-Modul:** Zuständigkeit, Beschlussvorschlag, Informationsgrundlage, BJR-Dokumentation, Anlagenliste.
- **Issue List:** Finding, Quelle, Risiko, Rechtsfolge, Register-/Vertragsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Organ, Notar, Registerteam, Steuerberater oder Gegenseite.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/corporate-kanzlei:corporate-kanzlei-spa-apa-entwurf` - wenn der Befund in SPA/APA-Entwurf oder Klausellogik einfließen soll.
- `/corporate-kanzlei:corporate-kanzlei-vertragsmarkup-key-issues` - wenn Markup-Abweichungen in Key Issues und Verhandlungslinien übersetzt werden müssen.
- `/corporate-kanzlei:corporate-kanzlei-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.
- `/corporate-kanzlei:corporate-kanzlei-closing-bible-archiv` - wenn executed documents, Registerbelege und Closing Bible gesichert werden müssen.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partner-, Organ- oder Mandantenentscheidung über Beschluss, Signing, Registeranmeldung oder Closing.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Registergericht, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht Corporate-Befund, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

# Disclosure Schedules

## Triage — klaere vor Beginn

1. Welche Warranties im SPA erfordern Disclosure Schedules (Specific vs. General Disclosures)?
2. Ist ein General Disclosure Letter (GDL) vorgesehen oder nur Specific Disclosures?
3. Was ist die Kenntnis-Definition (Seller's Knowledge: Best Knowledge, Actual Knowledge, Constructive Knowledge)?
4. Gibt es eine Materiality-Schwelle fuer Disclosure-Eintrage (z.B. > 50 TEUR)?
5. Anti-Sandbagging-Regelung: haftet Verkaefer auch bei Kaeufer-Kenntnis?
6. Disclosure Letter als Schedule zum SPA oder separates Dokument?
7. Zeitpunkt der Disclosure: nur bei Signing, oder auch Bring-Down-Disclosure bei Closing?

## Zentrale Normen

- **§ 444 BGB** — bei arglistigem Verschweigen keine Haftungsfreizeichnung moeglich; Disclosure heilt nur bei vollstaendiger Offenbarung
- **§ 311 II BGB** — vorvertragliche Aufklaerungspflicht; c.i.c.-Haftung bei wesentlichen verhohlenen Umstaenden
- **§ 442 BGB** — Kaeufer-Kenntnis schliesst Mangel-Haftung aus; Anti-Sandbagging schraenkt das ein
- **§ 453 BGB** — Anteilskauf; Gewaehrleistungsregime beim Anteilskauf

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Disclosure-Struktur: Specific und General Disclosures

### Specific Disclosures
Direkt an einzelne Warranties geknuepft: jede Warranty hat eine korrespondierende Schedule-Nummer.

Beispiele:
- Schedule 4.1 (Corporate Title): Gesellschafterliste, vinkulierte Anteile, Optionen
- Schedule 5.2 (Financial Statements): Jahresabschluss-Abweichungen, Rueckstellungsluecken
- Schedule 5.5 (Material Contracts): vollstaendige Liste; CoC-Klauseln hervorgehoben
- Schedule 5.7 (Litigation): laufende und drohende Verfahren mit Streitwertangabe
- Schedule 5.9 (Employment): Schluesselarbeitnehmer; Change-of-Control-Klauseln; Pensionen
- Schedule 5.11 (Tax): offene Betriebspruefungen; Einsprueche; Selbstanzeigen

### General Disclosure
Allgemeine Offenlegung aller Datenraum-Dokumente als Disclosure — nur wirksam wenn klar spezifiziert welches Dokument welche Warranty einschraenkt (OLG Frankfurt-Rspr.).

## Pruefungsmatrix: Vollstaendigkeit des Disclosure Letter

| Kategorie | Pruefungspunkt | Risiko bei Luecke |
|---|---|---|
| Litigation | Alle Verfahren >50 TEUR offenbart | Warranty-Verletzung; Indemnity-Anspruch |
| Material Contracts | Alle CoC-Klauseln und Kuendigungsrechte | Fehlende Consents post-Closing |
| Tax | Betriebspruefungen, Einsprueche, Selbstanzeigen | Tax-Warranty-Breach; voller Schaden |
| HR | Pensionszusagen, Gehaltserhohungen, Schluesselpersonen CoC | Unvorhergesehene Kosten post-Closing |
| Compliance | Laufende Ermittlungen, GwG/AML-Vorwuerfe, Sanktionen | Regulatory-Risiko; Closing-Blockade |
| Real Estate | Altlasten, Baulasten, Sondernutzungsrechte | Umwelthaftung; Wertverlust |

## Schritt-fuer-Schritt-Workflow

1. **Warranty-Katalog analysieren** — jede Warranty des SPA einer Disclosure-Kategorie zuordnen
2. **Disclosure-Koordinator benennen** — Ansprechpartner auf Verkaefer-Seite fuer jede Kategorie
3. **Faktensammlung** — Datenraum-Dokumente systematisch auf disclosure-relevante Informationen pruefen
4. **Interne Anhörung** — Management, Finance, Legal, HR, Compliance abfragen
5. **Entwurf Disclosure Letter** — konkrete Beschreibungen; keine allgemeinen Verweise auf Datenraum
6. **Pruefung § 444 BGB** — bekannte Arglist-Risiken vollstaendig erfassen; kein Weglassen
7. **Verhandlung mit Kaeufer** — manche Disclosures fuehren zu Nachverhandlung des SPA; Preisminderung oder Indemnity
8. **Bring-Down bei Closing** — wenn neues Ereignis zwischen Signing und Closing aufgetreten: Closing Disclosure anpassen
9. **Archivierung** — Disclosure Letter als Signatur-Anlage zum SPA; versioniert archivieren

## Entscheidungsbaum: Wie umgehen mit neuem Finding nach Signing?

```
Neues Material-Finding nach Signing entdeckt?
 → Warranty-Verletzung?
 → Ja, wesentlich (MAC-Level)?
 → Kaeufer kann Ruecktrittsrecht geltend machen (MAC-Klausel pruefen)
 → Ja, nicht wesentlich?
 → Closing-Disclosure: Kaeufer informieren; Preisanpassung oder Waiver verhandeln
 → Kein Warranty-Thema, aber CoC-Risiko?
 → Consent sofort einholen; Closing-Condition-Status pruefen
 → Arglist-Risiko (§ 444 BGB)?
 → Vollstaendige Offenbarung im Closing Disclosure Letter; ggf. Rechtsrat einholen
```

## Output-Template Disclosure Letter (Auszug)

**Adressat:** Kaeufer — Tonfall sachlich, vollstaendig

```
DISCLOSURE LETTER
Bezugnehmend auf den Share Purchase Agreement ("SPA") vom [DATUM]
zwischen [VERKAEFER] und [KAEUFER] betreffend [ZIELGESELLSCHAFT]

ALLGEMEINE OFFENBARUNG
Der Verkaefer legt hiermit alle im Datenraum (Platform: [NAME]; Index: [VERSION], Stand: [DATUM])
enthaltenen Dokumente und Informationen offen.

SPEZIFISCHE OFFENBARUNGEN

ZU SCHEDULE 5.7 (LITIGATION):
1. Laufendes Klageverfahren LG Frankfurt, Az. [Nr.], Streitwert [EUR]; Klaeger: [Name]; Gegenstand: [Beschreibung]
2. Drohendes Verfahren gemass Anwaltsschreiben vom [Datum]; Gegenstand: [Beschreibung]

ZU SCHEDULE 5.9 (EMPLOYMENT):
1. Schluesselperson [Name], Position [X], CoC-Recht zur ausserordentlichen Kuendigung bei > 50 % Anteilswechsel; Vertragsanlage [Nr.]
2. Betriebliche Altersversorgung: Rueckdeckungsversicherung [Versicherungsgesellschaft]; Volumen [EUR]

ZU SCHEDULE 5.11 (TAX):
1. Offene Betriebspruefung fuer Zeitraum [Jahr-Jahr]; Finanzamt [Name]; Sachstand: [Beschreibung]

[Weiterer Abschnitt je Warranty-Kategorie]

KENNTNIS-DEFINITION (KNOWLEDGE QUALIFIER)
"Best Knowledge des Verkaefers" bedeutet: tatsaechliche Kenntnis folgender Personen: [LISTE NAMES/FUNCTIONS]
nach vernaenftiger Nachforschung.
```

## Rote Schwellen

- Bekannte Arglist-Risiken nicht offenbart → § 444 BGB; keine Haftungsfreizeichnung
- Allgemeiner Verweis auf Datenraum statt konkreter Disclosure → OLG Frankfurt: keine wirksame Disclosure
- Bring-Down-Disclosure bei Closing vergessen → Warranty-Verletzung fuer Ereignisse zwischen Signing und Closing
- Materiality-Schwelle zu hoch gesetzt → kleinere Risiken nicht offenbart; spaeter Streit
- Anti-Sandbagging falsch ausgelegt → Kaeufer-Kenntnis schliesst Ansprueche nicht aus wenn vertraglich so vereinbart

## Quellen

- § 444, 311 II, 442, 453 BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Holzapfel/Poellath, Unternehmenskauf (16. Aufl. 2022) Kap. 10

## 2. `corporate-kanzlei-distressed-ma`

**Fokus:** Prüffeld für corporate kanzlei distressed ma: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Distressed M&A

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Distressed M&A` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Distressed M&A

- **Corporate-Aufgabe (Distressed M&A):** Prüffeld für corporate kanzlei distressed ma: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Distressed M&A und brauche einen belastbaren nächsten Schritt."
- "Bitte prüfe das aus Sicht der Gesellschaft, Geschäftsführung, Gesellschafter oder Inhouse-Rechtsabteilung."
- "Mach daraus eine Beschlussvorlage, Partnernotiz, Mandantenmail oder Organunterlage."
- "Welche Register-, Beschluss-, Compliance- oder Fristpunkte fehlen noch?"

Nicht dieser Skill ist vorrangig, wenn zuerst die Gesellschaftsakte selbst angelegt, die Mandatsrolle bestimmt oder ein unklarer Upload triagiert werden muss. Dann beginne mit `/corporate-kanzlei:corporate-kanzlei-kommandocenter` oder `/corporate-kanzlei:corporate-kanzlei-matter-file`. Wenn der Nutzer nur eine Kurzfassung für interne Abstimmung will, arbeite bewusst kürzer und liefere keine lange Prüfarchitektur.

## Voraussetzungen und Kontext laden
Lies zuerst, falls vorhanden, den Matter-Workspace unter `~/.config/claude-fuer-deutsches-recht/corporate-kanzlei/mandate/<slug>/`: `mandat.md`, `history.md`, `chronologie.md`, `fristen.yaml` und den aktuellen Dokumentenlog. Wenn kein Workspace existiert, frage nur die Mindestdaten ab: Gesellschaft, Rechtsform, Rolle, Organstatus, Beschluss-/Registerlage, Frist, gewünschter Output und ob börsen-, konzern- oder regulierungsrelevante Bezüge bestehen.

Benötigte Unterlagen:
- 13-Wochen-Liquiditätsplanung, Insolvenzreife-Check und Fortbestehensprognose.
- Asset-/Share-Deal-Struktur, Verwalter-/Eigenverwaltungsrolle und Zahlungsfluss.
- Anfechtungs-, Haftungs-, Steuer- und Closing-Sicherungsfragen.

Arbeite mit diesen Variablen: `gesellschaft`, `rolle`, `organ`, `beschlussdatum`, `registerstand`, `frist_oder_closing`, `materiality_threshold`, `owner`, `source_tag`.

## Workflow
1. **Corporate-Kontext fixieren.** Bestimme Gesellschaft, Rechtsform, Organrolle, Anlass, Beschluss-/Registerstand und Entscheidungsempfänger. Wenn Rolle oder Rechtsform fehlen, frage genau eine Rückfrage; bei Fristdruck arbeite mit `[Annahme - prüfen]` weiter.
2. **Quellen inventarisieren.** Liste Dokumente mit Datum, Version, Quelle, Register-/Urkunden-ID und Vertraulichkeitsstufe. Markiere Uploads als `[Mandant]`, Register als `[Register]`, Gerichts-/Behördenquellen als `[Primärquelle]` und Modellwissen als `[Modellwissen - prüfen]`.
3. **Organ- und Kompetenzebene trennen.** Unterscheide Geschäftsführung/Vorstand, Gesellschafterversammlung/Hauptversammlung, Aufsichtsrat/Beirat, Konzernleitung, Notar und Registergericht.
4. **Materiality-Schwelle setzen.** Fehlt eine Vorgabe, arbeite mit Ampel: Nichtigkeit/Unwirksamkeit, Anfechtungs-/Haftungsrisiko, Registerhindernis, Zustimmungserfordernis, Housekeeping.
5. **Normenprüfung durchführen.** Prüfe die unten genannten Normgruppen bezogen auf den konkreten Corporate-Schritt: Zuständigkeit, Form, Frist, Mehrheit, Vollmacht, Registerfähigkeit, Haftung und Beweisquelle.
6. **Belegkette bauen.** Jede wesentliche Aussage braucht Quelle, Dokument, Fundstelle und Unsicherheitsmarker. Keine Fundstelle erfinden. Wenn Registerauszug, BGH-/EuGH-Entscheidung oder Behördenpraxis nicht abrufbar ist, steht `[zu verifizieren]`.
7. **Risikomatrix erstellen.** Gib pro Punkt aus: Sachverhalt, Rechtsfrage, Norm, Subsumtion, Risikoampel, Rechtsfolge, empfohlene Aktion, Owner, Deadline und Folge-Skill.
8. **Draft oder Review-Gate wählen.** Wenn die Tatsachen reichen, liefere den gewünschten Output. Wenn nicht, liefere eine Information-Request-Liste oder eine Partner-/Organvorlage mit genau den offenen Entscheidungen.
9. **Hand-off vorbereiten.** Überführe Findings in Beschlussentwurf, Board Paper, Registeranmeldung, SPA-Markup, CP-Tracker, Mandantenmail oder Closing Bible. Verweise auf den konkreten Anschluss-Skill unten.
10. **Abschlusskontrolle.** Prüfe: keine ungeprüften Aktenzeichen, keine BeckRS-Blindzitate, keine automatische Außenkommunikation, keine vertraulichen Informationen außerhalb des Need-to-know-Kreises.

## Pruefraster im Gutachtenstil
**Obersatz:** Zu prüfen ist, ob der im Skill bearbeitete Corporate-Schritt gesellschaftsrechtlich wirksam, registerfähig, organschaftlich vertretbar und für die Mandatsseite praktisch umsetzbar ist.

**1. Mandats- und Rollenrahmen.** Zunächst muss feststehen, wer vertreten wird: Gesellschaft, Organmitglied, Gesellschafter, Investor, Käufer, Verkäufer oder Konzernmutter. Ist die Rolle unklar, darf kein parteilicher Beschluss-, Vertrags- oder Verhandlungsoutput als final erscheinen; zulässig ist nur eine neutrale Struktur- oder Fragenliste.

**2. Zuständigkeit, Form und Corporate Authority.** Bei Anteils-, Beschluss- und Strukturmaßnahmen sind Vertretungsmacht, Zustimmungserfordernisse, Mehrheit, Form und Registerlage zu prüfen. Relevanter Kern:
- InsO §§ 15a, 17, 18, 19, 129 ff., 270 ff. für Insolvenzreife, Antragspflicht und Anfechtung.
- StaRUG §§ 1, 9 ff. und 49 ff. für Früherkennung, Plan und Stabilisierung.
- BGB §§ 134, 138, 280, 311 Abs. 2 und 826 für Haftungs- und Sittenwidrigkeitsfragen.
- UmwStG §§ 20 bis 24 und § 8c KStG nur mit Steuerteam verifizieren.

**3. Organpflichten und Business Judgment.** Bei Geschäftsleitungs-, Aufsichtsrats- oder Beiratsentscheidungen ist zu fragen, ob die Entscheidung auf angemessener Informationsgrundlage, ohne sachfremde Interessen und zum Wohl der Gesellschaft vorbereitet ist. Für Organverantwortung: BGH, 21.04.1997 - II ZR 175/95, ARAG/Garmenbeck, https://dejure.org/1997,161 `[dejure.org]`.

**4. Register- und Gesellschafterlistenlogik.** Bei GmbH-Anteilen, Einziehung, Vollmachtskette oder Beschlussfähigkeit ist § 16 GmbHG gesondert zu prüfen. Zur Legitimationswirkung der Gesellschafterliste: BGH, 20.11.2018 - II ZR 12/17, https://dejure.org/2018,47817 `[BGH-Datenbank/dejure.org]`.

**5. Vollzugshindernisse.** Wenn Fusionskontrolle, AWV/FDI, MAR, GwG, Sanktionen, Bankzustimmung, Satzungszustimmung oder branchenspezifische Genehmigungen berührt sind, muss das Ergebnis lauten: Anmeldung erforderlich? Vollzugsverbot? Registerhindernis? Beschlussmangel? Long-Stop-Date gefährdet? Bußgeld-, Nichtigkeits- oder Haftungsfolge?

**6. Subsumtion.** Subsumtion erfolgt dokumentennah. Beispiel: `§ 15 GmbHG notarielle Form erfüllt?` nur bejahen, wenn Entwurf/Urkunde/Notarbestätigung vorliegt. `§ 46 GmbHG Zustimmung erforderlich?` nur bejahen, wenn Satzung, Geschäftsordnung und Maßnahme geprüft sind.

**Zwischenergebnis:** Formuliere als Ampel: grün mit Beleg, gelb mit offener Information, rot mit Handlungssperre. Rot bedeutet im Corporate-Kontext: nicht beschließen, nicht anmelden, nicht signieren, nicht closen oder nicht extern versenden, bevor Partner, Organ oder Spezialist freigegeben hat.

## Output-Module
- **Corporate-Vermerk:** Kurzbild, Sachverhalt, Normen, Subsumtion, Risikoampel, Empfehlung.
- **Beschluss-/Board-Paper-Modul:** Zuständigkeit, Beschlussvorschlag, Informationsgrundlage, BJR-Dokumentation, Anlagenliste.
- **Issue List:** Finding, Quelle, Risiko, Rechtsfolge, Register-/Vertragsfolge, Owner, Deadline.
- **Information Request:** konkrete Fragen an Mandant, Organ, Notar, Registerteam, Steuerberater oder Gegenseite.
- **Matter-Update:** kurzer Eintrag für `history.md` und ggf. Frist-/Owner-Eintrag für `fristen.yaml`.

## Quellen und Zitierregel
Nutze nur frei prüfbare Quellen oder vom Nutzer bereitgestellte/lizenzierte Quellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und Link auf `dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu` oder `eur-lex.europa.eu`. Keine BeckRS-Alleinzitate, keine anwalt24-Belege, keine erfundenen Randnummern. Quellen-Tags: `[Mandant]`, `[Register]`, `[BGH-Datenbank]`, `[dejure.org]`, `[EUR-Lex]`, `[Web-Recherche - prüfen]`, `[Modellwissen - prüfen]`.

## Hand-Off zu anderen Skills
Nach diesem Skill weiter mit:
- `/corporate-kanzlei:corporate-kanzlei-restructuring-starug-insolvenzplan` - wenn StaRUG, Planoptionen oder Insolvenzplanstruktur geprüft werden.
- `/corporate-kanzlei:corporate-kanzlei-signing-closing-conditions` - wenn CPs, Closing Deliverables oder Signing Pack koordiniert werden.

## Was dieser Arbeitsgang nicht macht
- Er ersetzt keine Partner-, Organ- oder Mandantenentscheidung über Beschluss, Signing, Registeranmeldung oder Closing.
- Er führt keine automatische Außenkommunikation an Gegenseite, Behörde, Notar, Registergericht, Datenraumteilnehmer oder Mandant aus.
- Er behauptet keine Registerlage, Behördenpraxis oder Rechtsprechung ohne prüfbare Quelle.
- Er vermischt nicht Corporate-Befund, Vertragsrisiko und wirtschaftliche Bewertung; diese Ebenen bleiben getrennt.
- Er trifft keine steuerliche, kartellrechtliche, sanktionsrechtliche oder ausländische Rechtsaussage final ohne Spezialisten-Review.
- Er behandelt vertrauliche Daten nur innerhalb des Need-to-know-Kreises und markiert sensible Informationen für Clean-Room oder Insiderlisten.

## Berufsrechtliche Hinweise
Vor Mandatsarbeit sind Interessenkonflikte nach § 43a BRAO und § 3 BORA, Verschwiegenheit nach § 43a Abs. 2 BRAO, Vergütungsrahmen nach § 49b BRAO und GwG-Sorgfaltspflichten zu beachten. Bei personenbezogenen Daten gelten DSGVO Art. 5, 6, 25 und 32. Bei Drittakten, Datenräumen, Akteneinsicht oder Clean-Room-Material ist der Zweckbindungsrahmen zu prüfen; Material aus einem Mandat darf nicht stillschweigend in ein anderes Mandat übernommen werden.

## Bisheriger Skill-Kern, integriert und weiterzuverwenden

# Distressed M&A

## Triage — klaere vor Beginn

1. Ist Insolvenzantrag bereits gestellt (insolvency proceedings) oder Vorfeldphase (pre-insolvency)?
2. Verkauf durch: Insolvenzverwalter, vorlaeufigen Verwalter, oder Gesellschaft selbst (Eigenverwaltung/StaRUG)?
3. Asset Deal oder Share Deal? (Im Insolvenzfall fast immer Asset Deal — Verbindlichkeiten bleiben bei InsoSchuldner)
4. Liquiditaetssituation: Wie viele Tage/Wochen hat der Prozess Zeit?
5. Arbeitnehmer: § 613a BGB; Widerspruchsrecht; Betriebsrat; Sozialplan in der Insolvenz?
6. Sicherheiten: Welche Sicherungseigentuemer, Pfandrechte, Grundschulden sind betroffen?
7. Auslaendische Tochtergesellschaften im Konzern: separate Insolvenzen oder Konzernanmeldung?

## Zentrale Normen

- **§§ 159-173 InsO** — Liquidation; Verwertung der Masse; Forderungsanmeldung
- **§§ 80, 148-161 InsO** — Insolvenzeroe ffnung; Verwaltungs- und Verfuegungsbefugnis des Verwalters
- **§§ 129-147 InsO** — Insolvenzanfechtung; §§ 133, 130 InsO Vorsatz- und Deckungsanfechtung
- **§ 179a AktG** — Zustimmung HV bei Uebertragung des gesamten Gesellschaftsvermoegen bei AG
- **§§ 21-34 StaRUG** — Restrukturierungsrahmen; Stabilisierungsanordnung; kein Vollstreckungsschutz ohne Anordnung
- **§ 613a BGB** — Betriebsuebergang; Haftung Erwerber fuer Altverbindlichkeiten (Ausnahmen in Insolvenz)
- **§§ 125-128 InsO** — Interessenausgleich; Sozialplan; Namensliste; erleichterte Kuendigung
- **§ 35 InsO** — Insolvenzmasse; was faellt dazu?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Distressed M&A: Prozessstruktur

| Phase | Dauer | Inhalt | Besonderheit |
|---|---|---|---|
| Screening/Erstkontakt | 1-2 Wochen | Insolvenzverwalter kontaktieren; NDA; Process Letter | Zeitdruck; keine Exklusivitaet |
| Erste Analyse | 1-2 Wochen | Reduzierter Datenraum; Kurz-DD; Arbeitnehmer-Check | Informationen lueckenhaft |
| Indikatives Angebot | 1-3 Tage | IOI/Non-Binding Offer; Kaufpreisrahmen | Verwalter hat Massemaximierungspflicht |
| Detaillierte Verhandlung | 1-2 Wochen | APA/Asset Purchase Agreement; Schedules | Haftungsausschluss maximal |
| Signing & Closing | 1 Woche | Closing meist = Signing; kein Vollzug-Vorbehalt | Schnell; Masseverwertung |

## Distressed M&A: Asset Deal Besonderheiten

Im Gegensatz zum normalen M&A ist im Distressed-Fall der Asset Deal Standard:

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Arbeitnehmer-Selektionsmoeglickeit** — kein automatischer Uebergang aller Arbeitnehmer, aber § 613a BGB beachten
3. **Steuerliche Vergangenheit bleibt** bei Insolvenzschuldner — kein Steuerrisiko aus Vergangenheit
4. **Freie Vermoegensauswahl** — Erwerber kann einzelne Assets, Vertraege, IP herauspicken
5. **Insolvenzanfechtungsrisiko gering** — fairer Marktwert-Prozess schuetzt vor § 133 InsO

## § 613a BGB im Insolvenzfall

In der Insolvenz gilt § 613a BGB grundsaetzlich weiter. Allerdings:
- Erwerber haftet nicht fuer rueckstaendige Ansprueche aus der Insolvenz (§ 613a II BGB)
- Kaeufer kann mit Insolvenzverwalter vor Erwerb bestimmte Arbeitnehmervertraege beenden (§§ 125-128 InsO)
- Sozialplanvolumen ist in der Insolvenz begrenzt (§ 123 InsO; max. 2.5 Monatsentgelte)
- Widerspruchsrecht der Arbeitnehmer (§ 613a VI BGB) beachten — Widerspruch verhindert Uebergang

## Schritt-fuer-Schritt-Workflow

1. **Erstbewertung** — Informationen von Insolvenzverwalter einholen; Massezustand; Fortfuehrungsprognose
2. **Schnell-DD** — Schwerpunkte: wesentliche Vertraege CoC/Kuendigungsrecht, Arbeitnehmer, IP, Hauptkunden
3. **Bewertungsrahmen** — Liquidationswert als Floor; Fortfuehrungswert als Ceiling; marktgerechter Preis
4. **APA-Entwurf** — Assets-Liste exakt definieren; Assumed Contracts; Excluded Liabilities; Personaluebernahme
5. **Arbeitnehmer-Konzept** — Uebernahme-Liste; Widerspruchsrecht-Frist; Betriebsrat konsultieren
6. **Anfechtungsrisiko pruefen** — war Preis marktgerecht? War Kaeufer in Kenntnis der Krise?
7. **Signing/Closing** — meist zeitgleich; Kaufpreis in Insolvenzmasse; Schluessel-Uebergabe
8. **Post-Closing Integration** — schnell; Kundeninfo; Lieferantenkuendigungen behandeln

## Output-Template APA Outline — Distressed

**Adressat:** Insolvenzverwalter / Kaeufer — Tonfall sachlich, rechtssicher

```
ASSET PURCHASE AGREEMENT (DISTRESSED M&A)
Parteien: [INSOLVENZVERWALTER als Verkaefer] / [KAEUFER]
Datum: [DATUM]

1. KAUFGEGENSTAND (INCLUDED ASSETS)
 - Anlagevermogen: [Liste Maschinen, Fahrzeuge, Inventar]
 - IP: [Marken, Patente, Know-how, Kundendaten]
 - Assumed Contracts: [Vertragsliste — nur genannte Vertraege gehen ueber]
 - Lagerbestand: [zum Stichtag]

2. AUSGESCHLOSSENE VERBINDLICHKEITEN (EXCLUDED LIABILITIES)
 Kaeufer uebernimmt KEINE Verbindlichkeiten des Schuldners ausser den Assumed Liabilities.

3. KAUFPREIS
 [EUR]; Zahlung: [sofort bei Closing / Ratenzahlung]

4. ARBEITNEHMER
 Uebernahme von [X] Arbeitnehmern gem. Anlage X.
 § 613a BGB Hinweis an Arbeitnehmer bis [DATUM].

5. REPRESENTATIONS (MINIMAL SCOPE)
 Nur: Titel/Verfuegungsbefugnis des Verwalters; keine Business Reps

6. HAFTUNGSAUSSCHLUSS
 Vollstaendiger Ausschluss aller Gewaehrleistungen; § 444 BGB nicht anwendbar (keine Arglist)

7. CLOSING
 Datum: [DATUM]; Simultaneous Signing & Closing
```

## Rote Schwellen

- § 133 InsO Anfechtungsrisiko: Kaeufer wusste von Zahlungsunfaehigkeit → Transaktion anfechtbar
- § 613a BGB-Uebergang vergessen → ungewollte Haftung fuer Arbeitnehmerrueckstaende (§ 613a II)
- Kein fairer Marktpreisprozess → Insolvenzverwalter-Haftung; Glaeubiger-Schadensersatz
- Assumed Contracts unvollstaendig — wichtige Kundenvertraege nicht uebertragen
- Zeitdruck: Signing ohne abgeschlossene DD — Haftungsausschluss im APA muss maximal sein

## Quellen

- InsO: https://www.gesetze-im-internet.de/inso/
- § 80 InsO (Verwaltungs- und Verfuegungsrecht des Insolvenzverwalters): https://www.gesetze-im-internet.de/inso/__80.html
- §§ 129-147 InsO (Insolvenzanfechtung; verschaerfte Vorsatzanfechtung § 133 InsO i.d.F. SanInsFoG seit 01.01.2021 — 4-Jahres-Frist statt 10 Jahre): https://www.gesetze-im-internet.de/inso/__129.html
- §§ 159-173 InsO (Verwertung der Masse): https://www.gesetze-im-internet.de/inso/__159.html
- § 613a BGB (Betriebsuebergang): https://www.gesetze-im-internet.de/bgb/__613a.html
- § 179a AktG: https://www.gesetze-im-internet.de/aktg/__179a.html
- StaRUG (Unternehmensstabilisierungs- und -restrukturierungsgesetz; in Kraft seit 01.01.2021 durch SanInsFoG, BGBl. I 2020, 3256): https://www.gesetze-im-internet.de/starug/
- § 15a InsO (Insolvenzantragspflicht: 3 Wochen ZU / 6 Wochen UE): https://www.gesetze-im-internet.de/inso/__15a.html
- § 15b InsO (Zahlungsverbot bei Insolvenzreife seit 01.01.2021; rechtsformneutral): https://www.gesetze-im-internet.de/inso/__15b.html
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
