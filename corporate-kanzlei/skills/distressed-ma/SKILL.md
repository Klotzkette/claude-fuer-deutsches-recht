---
name: distressed-ma
description: "Prüfungslinie für corporate kanzlei distressed ma im Corporate Kanzlei."
---

# Distressed M&A

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Distressed M&A

- **Corporate-Aufgabe (Distressed M&A):** Corporate Kanzlei Distressed Ma: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.
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

## Prüfraster im Gutachtenstil
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

### Distressed M&A

## Triage — klaere vor Beginn

1. Ist Insolvenzantrag bereits gestellt (insolvency proceedings) oder Vorfeldphase (pre-insolvency)?
2. Verkauf durch: Insolvenzverwalter, vorläufigen Verwalter, oder Gesellschaft selbst (Eigenverwaltung/StaRUG)?
3. Asset Deal oder Share Deal? (Im Insolvenzfall fast immer Asset Deal — Verbindlichkeiten bleiben bei InsoSchuldner)
4. Liquiditaetssituation: Wie viele Tage/Wochen hat der Prozess Zeit?
5. Arbeitnehmer: § 613a BGB; Widerspruchsrecht; Betriebsrat; Sozialplan in der Insolvenz?
6. Sicherheiten: Welche Sicherungseigentuemer, Pfandrechte, Grundschulden sind betroffen?
7. Ausländische Tochtergesellschaften im Konzern: separate Insolvenzen oder Konzernanmeldung?

## Zentrale Normen

- **§§ 159-173 InsO** — Liquidation; Verwertung der Masse; Forderungsanmeldung
- **§§ 80, 148-161 InsO** — Insolvenzeroe ffnung; Verwaltungs- und Verfuegungsbefugnis des Verwalters
- **§§ 129-147 InsO** — Insolvenzanfechtung; §§ 133, 130 InsO Vorsatz- und Deckungsanfechtung
- **§ 179a AktG** — Zustimmung HV bei Uebertragung des gesamten Gesellschaftsvermoegen bei AG
- **§§ 21-34 StaRUG** — Restrukturierungsrahmen; Stabilisierungsanordnung; kein Vollstreckungsschutz ohne Anordnung
- **§ 613a BGB** — Betriebsuebergang; Haftung Erwerber für Altverbindlichkeiten (Ausnahmen in Insolvenz)
- **§§ 125-128 InsO** — Interessenausgleich; Sozialplan; Namensliste; erleichterte Kuendigung
- **§ 35 InsO** — Insolvenzmasse; was faellt dazu?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
4. **Freie Vermögensauswahl** — Erwerber kann einzelne Assets, Verträge, IP herauspicken
5. **Insolvenzanfechtungsrisiko gering** — fairer Marktwert-Prozess schuetzt vor § 133 InsO

## § 613a BGB im Insolvenzfall

In der Insolvenz gilt § 613a BGB grundsätzlich weiter. Allerdings:
- Erwerber haftet nicht für rueckstaendige Ansprueche aus der Insolvenz (§ 613a II BGB)
- Kaeufer kann mit Insolvenzverwalter vor Erwerb bestimmte Arbeitnehmervertraege beenden (§§ 125-128 InsO)
- Sozialplanvolumen ist in der Insolvenz begrenzt (§ 123 InsO; max. 2.5 Monatsentgelte)
- Widerspruchsrecht der Arbeitnehmer (§ 613a VI BGB) beachten — Widerspruch verhindert Uebergang

## Schritt-für-Schritt-Workflow

1. **Erstbewertung** — Informationen von Insolvenzverwalter einholen; Massezustand; Fortfuehrungsprognose
2. **Schnell-DD** — Schwerpunkte: wesentliche Verträge CoC/Kuendigungsrecht, Arbeitnehmer, IP, Hauptkunden
3. **Bewertungsrahmen** — Liquidationswert als Floor; Fortfuehrungswert als Ceiling; marktgerechter Preis
4. **APA-Entwurf** — Assets-Liste exakt definieren; Assumed Contracts; Excluded Liabilities; Personaluebernahme
5. **Arbeitnehmer-Konzept** — Uebernahme-Liste; Widerspruchsrecht-Frist; Betriebsrat konsultieren
6. **Anfechtungsrisiko prüfen** — war Preis marktgerecht? War Kaeufer in Kenntnis der Krise?
7. **Signing/Closing** — meist zeitgleich; Kaufpreis in Insolvenzmasse; Schlüssel-Übergabe
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
- § 613a BGB-Uebergang vergessen → ungewollte Haftung für Arbeitnehmerrueckstaende (§ 613a II)
- Kein fairer Marktpreisprozess → Insolvenzverwalter-Haftung; Gläubiger-Schadensersatz
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
