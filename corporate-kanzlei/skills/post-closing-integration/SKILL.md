---
name: post-closing-integration
description: "Post-Closing-Integration (PMI) rechtlich begleiten: Unmittelbar nach Closing muessen Handelsregister, Vertraege, Organ-Strukturen und Steuereinheiten angepasst werden. Normen: GmbHG, AktG, UmwStG, KStG (Organschaft), § 613a BGB (Betriebsuebergang, Arbeitnehmerinfo). Prüfraster: Handelsregisteranm"
---

# Post-Closing-Integration (PMI)

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Post-Closing-Integration (PMI)

- **Corporate-Aufgabe (Post-Closing-Integration (PMI)):** Unmittelbar nach Closing müssen Handelsregister, Verträge, Organ-Strukturen und Steuereinheiten angepasst werden.
- **Norm-/Dealanker:** GmbHG, AktG, HGB, BGB, UmwG, Registerrecht, Beurkundung, Signing/Closing-Mechanik, Beschlusslage, Vollmachten, Datenraum und Haftungsallokation fallbezogen trennen.
- **Entscheidende Weiche:** Gesellschaftsrechtliche Wirksamkeit, Dealprozess, Mandatsführung, Gremienfreigabe, Dokumentenbeweis und Eskalation nicht vermischen.
- **Arbeitsprodukt:** Partnerfähiges Memo, Closing-/Action-Liste, Redline-Hinweis oder PMO-Board mit Verantwortlichen und Blockern.

## Wann wird dieser Skill aufgerufen
Typische Auslöser:
- "Ich habe hier Post-Closing-Integration (PMI) und brauche einen belastbaren nächsten Schritt."
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

## Prüfraster im Gutachtenstil
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
- `/corporate-kanzlei:corporate-kanzlei-disclosure-schedules` - wenn Garantien, Knowledge und Disclosure Letter abgeglichen werden.
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

### Post-Closing-Integration (PMI)

## Triage — klaere nach Closing

1. Welche Handelsregister-Änderungen sind erforderlich (neuer GF, Firmenname, Sitzverlegung)?
2. Organschaft geplant? (Beherrschungs- und Gewinnabfuehrungsvertrag nach §§ 291 ff. AktG, steuerlich §§ 14 ff. KStG)
3. § 613a BGB: Wurden Arbeitnehmer ordnungsgemaess informiert? Widerspruchsfristen beachtet?
4. Change-of-Control-Verträge: Wurden alle Consents fristgemaess eingeholt?
5. Transition Services Agreement (TSA): Welche Dienstleistungen werden weiter bezogen/geliefert?
6. D&O und andere Versicherungen: Runoff-Policy für altes Management; neue Police für neue Eigentuemerstruktur?
7. Brandkarte: Umfirmierung, neues CI, IT-Systeme migrieren — Zeitplan?

## Zentrale Normen

- **§§ 39-45 GmbHG** — Anmeldung von GF-Änderungen; Satzungsaenderung; Sitzverlegung beim Handelsregister
- **§§ 291-310 AktG** — Beherrschungsvertrag; Gewinnabfuehrungsvertrag; Vertragskonzern; Minderheitsschutz
- **§§ 14-19 KStG** — koerperschaftsteuerliche Organschaft; finanzielle Eingliederung; GAV-Voraussetzung
- **§ 613a BGB** — Betriebsuebertragung; Informationspflicht; Widerspruchsrecht 1 Monat
- **§ 106 I BetrVG** — Unterrichtung des Wirtschaftsausschusses bei Betriebsaenderung
- **§ 111 AktG** — Aufsichtsrats-Informationsrechte bei wesentlichen Änderungen post-Closing
- **§§ 14 ff., 20 ff. UmwStG** — Steuerneutrale Integration; Verschmelzung; Sperrfristen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Post-Closing-Aktionsplan: Priorisierte Maßnahmen

### Sofort (bis 2 Wochen post-Closing)
- [ ] Handelsregister-Anmeldung (neuer GF, ggf. Firmenname) → Notar beauftragt; Frist prüfen
- [ ] § 613a-Information an Arbeitnehmer (wenn Betriebsuebergang) → Musterbrief vorbereiten; individuell zustellen; Datum dokumentieren
- [ ] Konten und Unterschriftsberechtigungen ändern → Bank informieren; neue SEPA-Mandate
- [ ] Steuernummern / USt-ID umschreiben oder neu beantragen
- [ ] Versicherungen anpassen: D&O, Betriebshaftpflicht; Runoff-Policy altes Management

### Kurzfristig (bis 1 Monat)
- [ ] Change-of-Control-Consents bestaetigend dokumentieren; Vertragsgegner schriftlich informieren
- [ ] TSA-Management einrichten: Vertrag, Service-Level-Monitoring, Exit-Plan
- [ ] Betriebsrat informieren (§ 106 BetrVG); Interessenausgleich falls Betriebsaenderung

### Mittelfristig (bis 6 Monate)
- [ ] Organschaft-Beschluss (GAV notariell beurkunden, HR anmelden; steuerliche Anerkennung ab 01.01. des Jahres, in dem Eintragung erfolgt)
- [ ] Konzernintegration: IT-Systeme, ERP-Migration, Shared Services
- [ ] Finanzielle Eingliederung nach § 14 KStG sicherstellen (>50% Stimmrechte; unmittelbar oder mittelbar)

## Organschaft: Voraussetzungen und Einrichtung (§§ 291 AktG, 14 KStG)

### Steuerliche Organschaft (§§ 14-19 KStG)
- Finanziell eingegliedert: >50 % Stimmrechtsanteil der Muttergesellschaft an Organgesellschaft
- GAV (Gewinnabfuehrungsvertrag) muss notariell beurkundet sein und in HR eingetragen werden
- Mindestlaufzeit: 5 Jahre; vorzeitige Aufhebung = rueckwirkende Steuerpflicht
- Verluste der Organgesellschaft werden beim Organtraeger beruecksichtigt
- Steuerliche Wirkung ab dem Wirtschaftsjahr, in dem die Eintragung im HR erfolgt

### Unternehmensvertrag (§§ 291-310 AktG)
- Für AG/KGaA: Beherrschungsvertrag (Weisungsrecht der Mutter); Gewinnabfuehrungsvertrag (Gewinnabfuehrung an Mutter)
- HV-Beschluss mit 3/4-Mehrheit beider Gesellschaften; Minderheitsschutz: Ausgleich und Abfindung (§§ 304-305 AktG)
- Für GmbH: kein gesetzliches Erfordernis für HV-Beschluss, aber Notarpflicht und Eintragung empfohlen

## Schritt-für-Schritt-Workflow

1. **Post-Closing Checklist abarbeiten** — tagesgenau; Owner für jede Maßnahme
2. **HR-Anmeldungen** — Notar beauftragen; Begleitunterlagen vorbereiten (Gesellschafterbeschluesse)
3. **§ 613a-Information** — Unterrichtungsschreiben ausfertigen; individuell an jeden Arbeitnehmer; Datum beweissicher dokumentieren
4. **CoC-Consents bestaetigend dokumentieren** — Schriftbestaetigung der Vertragspartner einholen
5. **TSA-Management** — Leistungsverzeichnis; Abnahme-Protokoll; Exit-Meilensteine
6. **Organschaft einrichten** — GAV-Entwurf; notariell beurkunden; HR-Anmeldung; steuerliche Beantragung
7. **IT-Migration** — Datenbestands-Uebertragung; DSGVO-Datenschutz; AVV-Anpassung
8. **Abschluss-PMI-Bericht** — Status aller Maßnahmen; Abweichungen dokumentieren; Closing-Bible erganzen

## Output-Template § 613a Informationsschreiben

**Adressat:** Arbeitnehmer — Tonfall klar, vollstaendig (§ 613a V BGB Pflichtinhalte)

```
Sehr geehrte/r Frau/Herr [NAME],

hiermit informieren wir Sie gemass § 613a Abs. 5 BGB ueber den Uebergang Ihres Arbeitsverhaeltnisses.

1. ZEITPUNKT DES UEBERGANGS: [DATUM]

2. GRUND DES UEBERGANGS: Erwerb der [FIRMA] durch [KAEUFER] gemaess Share Purchase Agreement vom [DATUM].

3. RECHTLICHE, WIRTSCHAFTLICHE UND SOZIALE FOLGEN:
 - Ihr Arbeitsverhaeltnis geht mit allen Rechten und Pflichten auf [KAEUFER/NEUE GESELLSCHAFT] ueber.
 - Ihr Gehalt, Ihre Taetigkeit und Ihre Arbeitsbedingungen bleiben unveraendert.
 - Bestehende Betriebsvereinbarungen gelten für ein Jahr fort (§ 613a I 2 BGB), sofern keine abweichende Regelung getroffen wird.

4. GEPLANTE MASSNAHMEN: [Kurzbeschreibung der Integrationsplane, soweit bekannt]

5. WIDERSPRUCHSRECHT: Sie koennen dem Uebergang Ihres Arbeitsverhaeltnisses widersprechen.
 - Frist: 1 Monat ab Zugang dieses Schreibens.
 - Adressat: [Alte Gesellschaft] und/oder [Neue Gesellschaft]
 - Folge des Widerspruchs: Ihr Arbeitsverhaeltnis verbleibt bei [Alte Gesellschaft];
 jedoch koennte eine betriebsbedingte Kuendigung folgen.

Mit freundlichen Gruessen
[FIRMA]
[UNTERSCHRIFT, Datum]
```

## Rote Schwellen

- § 613a-Information vergessen oder unvollstaendig → Widerspruchsfrist laeuft nie ab; spaetere Widersprueche möglich
- Organschaft-GAV unter 5 Jahre → rueckwirkende Steuerpflicht; erhebliche Nachzahlungen
- CoC-Consents nicht dokumentiert → Vertragskuendigungen post-Closing unbemerkt
- TSA ohne Exit-Plan → dauerhafte Abhaengigkeit von altem Konzern
- Runoff-Policy altes Management vergessen → D&O-Luecke für Althandlungen

## Quellen

- §§ 39-45 GmbHG; §§ 291-310, 304-305 AktG; §§ 14-19 KStG; § 613a BGB; § 106 BetrVG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
