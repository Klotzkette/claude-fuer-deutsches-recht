---
name: strafbefehl-einlassung-deal-verstaendigung
description: "Einlassung Deal Verstaendigung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Einlassung Deal Verstaendigung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Einlassung Deal Verstaendigung** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-beweis-und-einlassung` | Beweisprüfung und Einlassungsstrategie im Strafbefehlsverfahren. Schweigen nach § 136 StPO darf nicht nachteilig gewertet werden (BGH st. Rspr.). Gestaendnis vs. Bestreiten Strategie. Beweisanträge § 244 StPO. Einlassung schriftlich oder muendlich. Beweisverwertungsverbote § 136a StPO. |
| `strafbefehl-deal-verstaendigung` | Verständigung nach § 257c StPO im Strafbefehlsverfahren. Voraussetzungen Inhalt Bindungswirkung Belehrung nach § 257c Abs. 4 und 5 StPO. Grenzen: kein Freispruch kein Schuldspruchverzicht. Abgrenzung informelle Absprache. Ablaufprotokoll TOA § 46a StGB. |
| `strafbefehl-einspruch-beschraenkung` | Beschraenkter Einspruch nach § 410 Abs. 2 StPO auf Rechtsfolgen. Schuldspruch wird rechtskraeftig. Taktisches Kalkuel. Geldstrafe Tagessatz Fahrverbot Einziehung angreifbar. Vollstreckungsverzug § 456a StPO. Abgrenzung unbeschraenkter Einspruch. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Einlassung Deal Verstaendigung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-beweis-und-einlassung`

**Fokus:** Beweisprüfung und Einlassungsstrategie im Strafbefehlsverfahren. Schweigen nach § 136 StPO darf nicht nachteilig gewertet werden (BGH st. Rspr.). Gestaendnis vs. Bestreiten Strategie. Beweisanträge § 244 StPO. Einlassung schriftlich oder muendlich. Beweisverwertungsverbote § 136a StPO.

# Beweis und Einlassung im Strafbefehlsverfahren

## Triage zu Beginn

1. **Was bestreitet der Mandant?** — Tathandlung, Fahrereigenschaft, Vorsatz, Schuld? Klare Abgrenzung der streitigen Punkte.
2. **Aktenlage:** Welche Beweismittel hat die Staatsanwaltschaft — Zeugen, Messgeraet, Video, Gestaendnis im Anhoerungsbogen?
3. **Hat der Mandant sich bereits gegenueber der Polizei gaeussert?** — Aussagen im Anhoerungsverfahren oder Vernehmung koennen belastend sein.
4. **Anhoerungsbogen ausgefuellt oder unterschrieben?** — Nur schriftliche Bekanntgabe, kein Gestaendnis; Unterschrift kann als Einraeuming der Fahrereigenschaft ausgelegt werden.
5. **Dauer der Hauptverhandlung und Ressourcen des Mandanten** — Einlassung mit Kostenpruefung abstimmen.
6. **Smartphone-, Polizei- oder Versammlungsaufnahme?** — Bei Strafbefehl wegen Filmens/Audioaufnahme sofort `strafbefehl-polizeifilmerei-201-kug` hinzuziehen: § 201 StGB, § 201a StGB und KunstUrhG/KUG dürfen nicht vermischt werden.

## Zentrale Normen

- **§ 136 StPO** — Schweigrecht; Belehrung vor jeder Vernehmung
- **§ 136a StPO** — Verbotene Vernehmungsmethoden; Verstoss = absolutes Beweisverwertungsverbot
- **§ 163a StPO** — Vernehmung des Beschuldigten durch die Polizei; Belehrungspflicht
- **§ 244 StPO** — Beweisantragsrecht; Gericht muss jeden Beweisantrag bescheiden
- **§ 257c StPO** — Verstaendigung (Deal); auch im vereinfachten Verfahren moeglich
- **§ 46 StGB** — Strafzumessung; Gestaendnis als Milderungsgrund
- **§§ 22, 23, 33 KunstUrhG/KUG** — Bildnisveröffentlichung; bloße Anfertigung von Bildern getrennt prüfen
- **§§ 201, 201a StGB** — Tonaufnahmen und höchstpersönliche Bildinhalte; Nichtöffentlichkeit, Schutzbereich und Rechtfertigung sauber trennen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Einlassungsstrategie

```
Mandant bestreitet Tat?
├─ Ja, substantiiert (Alibi, Messversagen, Fahreridentitaet)
│ ├─ Schweigen bis Hauptverhandlung empfehlen
│ ├─ Beweisantraege vorbereiten (§ 244 StPO)
│ └─ Einlassung in HV formulieren
├─ Nein, Tat anerkannt, nur Strafmass angreifbar
│ ├─ Gestaendnis-Strategie: frueh und glaubhaft (§ 46 Abs. 2 StGB)
│ ├─ Wiedergutmachung als Milderungsgrund (§ 46a StGB)
│ └─ § 153a-Antrag bei Staatsanwaltschaft pruefen
└─ Fahrereigenschaft bestreitbar
 ├─ Lichtbildabgleich anfordern
 ├─ Keine Aussagen zur Fahreridentifikation
 └─ Beweisantrag auf Sachverstaendigen fuer Lichtbild-Identifikation

Anhoerungsbogen ausgefuellt?
├─ Nein → gut; Schweigen weiter empfehlen bis Akteneinsicht
├─ Ja, Tat zugegeben → Gestaendnis-Wert pruefen fuer § 153a oder Strafmassreduzierung
└─ Ja, Einwaende gemacht → auf diese aufbauen, widerspruchsfrei vertiefen
```

## Schritt-fuer-Schritt-Workflow

1. **Akteneinsicht anfordern** (§ 147 StPO) — Basis fuer jede Einlassungsstrategie.
2. **Beweislage analysieren:** Welche Beweismittel hat die Anklage? Sind sie verwertbar (Belehrungsfehler, § 136a-Verstoss)?
3. **Mandantengespraech: Sachverhaltsschilderung vollstaendig aufnehmen** — ohne Bewertung, nur erfassen.
4. **Strategie festlegen** (s. Entscheidungsbaum) — schriftlich dokumentieren, Mandant ueber Risiken aufklaeren.
5. **Einlassung formulieren oder Schweigen anordnen** — bei Schweigen Mandanten anweisen, keine Angaben gegenueber Polizei/Staatsanwaltschaft zu machen.
6. **Beweisantraege formulieren** (§ 244 StPO) — konkret: Beweisthema und Beweismittel benennen.
7. **Wenn Gestaendnis:** Timing und Umfang mit Mandant absprechen; Gestaendnis in HV fruehzeitig abgeben fuer optimalen Strafzumessungseffekt.

## Output-Template Einlassungsschreiben

**Adressat:** Gericht — Tonfall: sachlich-juristisch

```
In der Strafsache gegen [NAME MANDANT]
Az.: [AKTENZEICHEN]

Einlassung zur Sache

Namens und im Auftrag des Angeklagten erklaere ich wie folgt:

[Variante A — Bestreiten:]
Der Angeklagte bestreitet die ihm zur Last gelegte Tat.
[Sachverhaltsschilderung aus Mandantenperspektive]

[Variante B — Gestaendnis:]
Der Angeklagte gibt zu, [Sachverhalt] getan zu haben.
Er bedauert dies aufrichtig und hat [Wiedergutmachungshandlung]
vorgenommen.

Strafmildernd ist zu beruecksichtigen:
- Ersttatveraechtigter / kein Vorregister
- [Weitere Umstaende]
```

## Harte Leitplanken

- Keine Einlassung vor vollstaendiger Akteneinsicht.
- Schweigrecht nach § 136 StPO ausueben bis Aktenlage klar ist.
- Gestaendnis nur nach Mandantenruecksprache und Aufklaerung ueber Tragweite.
- Beweisverwertungsverbote aktiv pruefen — Fehler der Ermittlungsbehoerden nicht verschenken.
- Anwaltliche Endkontrolle bei jedem Schritt.

## 2. `strafbefehl-deal-verstaendigung`

**Fokus:** Verständigung nach § 257c StPO im Strafbefehlsverfahren. Voraussetzungen Inhalt Bindungswirkung Belehrung nach § 257c Abs. 4 und 5 StPO. Grenzen: kein Freispruch kein Schuldspruchverzicht. Abgrenzung informelle Absprache. Ablaufprotokoll TOA § 46a StGB.

# Verstaendigung im Strafbefehlsverfahren — § 257c StPO

## Triage zu Beginn

1. **Ist eine Verstaendigung im Strafbefehlsverfahren sinnvoll?** — Strafbefehlsverfahren ist ungeeignet fuer komplexe Deals; einfacher: § 153a-Antrag oder direkter Strafmass-Einspruch mit Gestaendnis.
2. **Liegt Gestaendnisbereitschaft des Mandanten vor?** — Verstaendigung setzt nach BGH ein Gestaendnis voraus (§ 257c Abs. 2 StPO).
3. **Was ist das Ziel?** — Geldstrafe statt Bewaehrungsstrafe? Fahrverbot-Vermeidung? Einstellung nach § 153a? Klares Ziel formulieren.
4. **Ist die Staatsanwaltschaft kontaktierbar?** — Fruehzeitige informelle Sondierung vor foermlicher Verstaendigungsanfrage ist zulaessig.
5. **Sind Mitbeschuldigte betroffen?** — Verstaendigung darf nur das eigene Verfahren betreffen.

## Zentrale Normen

- **§ 257c StPO** — Verstaendigung: Voraussetzungen, Inhalt, Bindung, Belehrung
- **§ 257c Abs. 1 StPO** — Verstaendigung nur mit Zustimmung aller Verfahrensbeteiligter (Gericht, StA, Verteidiger/Angeklagter)
- **§ 257c Abs. 2 StPO** — Gegenstand: Rechtsfolgen, prozessuale Handlungen; NICHT: Schuldspruch
- **§ 257c Abs. 4 StPO** — Bindungswirkung entfaellt bei veraenderter Sachlage
- **§ 257c Abs. 5 StPO** — Belehrungspflicht vor Verstaendigung
- **§ 153 StPO** — Einstellung bei Geringfuegigkeit (ohne Auflage)
- **§ 153a StPO** — Einstellung gegen Auflage (Praxis-Alternative zur Verstaendigung)
- **§ 46a StGB** — Taeter-Opfer-Ausgleich als Strafmilderungsgrund

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BGH 20.11.2025 — 4 StR 232/25 (4. Strafsenat): TOA § 46a Nr. 1 StGB setzt einen friedensstiftenden kommunikativen Prozess voraus; bloße Zahlung an das Opfer reicht für Strafmilderung nicht aus. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- BVerfG-Rahmen (Stand-by) zu § 257c StPO: Maßstab weiterhin BVerfG 19.03.2013 — 2 BvR 2628/10, 2 BvR 2155/11, 2 BvR 2883/10 (Verstaendigungs-Urteil); Aktualisierungen vor Ausgabe in dejure.org / bverfg.de pruefen. Offene Fundstelle Verstaendigungs-Urteil: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+BvR+2628/10
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 speziell zur Anwendung des § 257c StPO im Strafbefehlsverfahren ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 257c StPO Strafbefehl" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Abgrenzung: Wann welches Instrument?

| Instrument | Geeignet wenn | Vorteil |
|-----------|--------------|---------|
| § 153 StPO | Bagatelldelikt, keine Vorstrafe, geringer Schaden | Keine Auflage, kein Eintrag |
| § 153a StPO | Mittelgraes Delikt, Zahlungsbereitschaft | Kein Strafregister (Tilgung), flexibel |
| § 257c StPO | Schweres Delikt, Hauptverhandlung notwendig | Strafmass-Sicherheit, Verfahrensabkuerzung |
| § 46a StGB + Gestaendnis | Geschaedigter vorhanden, Wiedergutmachung moeglich | Erhebliche Strafmilderung, kann Bewaehrung ermoeglichen |

## Schritt-fuer-Schritt-Workflow

1. **Zieldefinition mit Mandant:** Was soll das Ergebnis sein? (Strafmass, Fahrverbot, Eintrag)
2. **Informelle Sondierung:** Staatsanwalt telefonisch kontaktieren — Einstellungsbereitschaft testen.
3. **§ 153a-Antrag formulieren** wenn Einstellungsbereitschaft vorhanden — einfacher als foermliche Verstaendigung.
4. **Wenn § 257c notwendig:** Schriftlichen Verstaendigungsvorschlag formulieren mit exakten Rechtsfolgen-Grenzen.
5. **Hauptverhandlung:** Gericht macht Verstaendigungsvorschlag; alle Beteiligten stimmen zu; Belehrung nach § 257c Abs. 5 StPO protokollieren lassen.
6. **Gestaendnis:** Konkret, glaubhaft, auf Beweislage abgestimmt.
7. **Protokollkontrolle:** Verstaendigungsinhalt korrekt protokolliert? Belehrung dokumentiert?

## Output-Template § 153a-Antrag

**Adressat:** Staatsanwaltschaft — Tonfall: sachlich-kooperativ

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Einstellung nach § 153a StPO

Sehr geehrte Damen und Herren,

ich rege an, das Verfahren gegen [NAME] gegen Zahlung einer
Geldbusse von [BETRAG] EUR an [EINRICHTUNG] nach § 153a Abs. 1
StPO einzustellen.

Mein Mandant ist ersttaetig, zeigt Reue und hat [Wiedergutmachung]
geleistet. Der Tatvorwurf betrifft [kurze Tat-Charakterisierung].
Publik-Interesse an Strafverfolgung steht in keinem Verhaeltnis
zum Aufwand.

[NAME] erklaert seine Zustimmung zur Einstellung.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Verstaendigung NIEMALS ohne Belehrung nach § 257c Abs. 5 StPO — Revisionsrisiko.
- Informelle Zusagen nicht vertrauen — nur foermliche Verstaendigung im Protokoll ist bindend.
- Bindungswirkung entfaellt bei neuen Erkenntnissen (§ 257c Abs. 4 StPO) — Mandant darauf hinweisen.
- Anwaltliche Endkontrolle bei Gestaendnisformulierung und Protokoll.

## 3. `strafbefehl-einspruch-beschraenkung`

**Fokus:** Beschraenkter Einspruch nach § 410 Abs. 2 StPO auf Rechtsfolgen. Schuldspruch wird rechtskraeftig. Taktisches Kalkuel. Geldstrafe Tagessatz Fahrverbot Einziehung angreifbar. Vollstreckungsverzug § 456a StPO. Abgrenzung unbeschraenkter Einspruch.

# Beschraenkter Einspruch gegen den Strafbefehl — § 410 Abs. 2 StPO

## Triage zu Beginn

1. **Ist der Schuldspruch unstreitig?** — Beschraenkung nur sinnvoll wenn der Mandant die Tat einraeumt und nur die Rechtsfolgen angreift.
2. **Welche Rechtsfolge soll angehoben werden?** — Tagessatzhoehe zu hoch (Einkommen falsch berechnet)? Tagessatzanzahl unverhältnismaessig? Fahrverbot unverhältnismaessig? Einziehung anfechtbar?
3. **Risiko der Verstaerkungs-Verurteilung?** — Im beschraenkten Einspruchsverfahren kann das Gericht auch hoeher bestrafen als im Strafbefehl angesetzt (kein Verboeschungsverbot bei Rechtsfolgen-Einspruch!).
4. **Verjaehrung/Tilgung:** Schuldspruch-Rechtskraft beschleunigt Eintrag ins Bundeszentralregister.
5. **Kostenrisiko:** Beschraenkt-Einspruch verringert Verfahrensaufwand, Kostenlast bleibt bei Verurteilung.

## Zentrale Normen

- **§ 410 Abs. 2 StPO** — beschraenkter Einspruch auf Rechtsfolgen moeglich
- **§ 40 StGB** — Tagessatzsystem; Anzahl nach Schuld, Hoehe nach Nettoeinkommen / 30
- **§ 25 StVG** — Fahrverbot im Busgeldverfahren (1 bis 3 Monate)
- **§ 44 StGB** — Fahrverbot als strafrechtliche Nebenfolge (1 bis 6 Monate)
- **§ 73 StGB** — Einziehung von Tatertraegen
- **§ 331 StPO** — kein Verboeschungsverbot bei Berufung auf Rechtsfolgen; im Einspruchsverfahren analoge Diskussion
- **§ 46 StGB** — Strafzumessungserwägungen (Grundlage fuer Tagessatzanzahl)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum: Beschraenkt oder unbeschraenkt?

```
Mandant erkennt Tat an?
├─ Ja
│ ├─ Nur Tagessatzhoehe angreifbar (Einkommen falsch)?
│ │ └─ Beschraenkt auf Rechtsfolgen → geringeres Risiko
│ ├─ Fahrverbot unverhältnismaessig?
│ │ └─ Beschraenkt auf Fahrverbot
│ └─ Strafmass insgesamt zu hoch?
│ └─ Unbeschraenkt mit Gestaendnis-Strategie
└─ Nein
 └─ Unbeschraenkt — kein beschraenkter Einspruch!

Risikopruefung vor Beschraenkung:
- Kann Gericht in HV hoeher bestrafen? → JA, kein Verboeschungsverbot!
- Mandant ueber Risiko aufgeklaert? → Schriftliche Bestaetigung
```

## Nachweis Nettoeinkommen fuer Tagessatz-Reduktion

**Dokumente die angefordert werden sollten:**
- Lohnabrechnung letzter 3 Monate
- Steuerbescheid letztes Jahr
- Bei Selbststaendigen: Betriebswirtschaftliche Auswertung (BWA)
- Unterhalts-/Kreditverpflichtungen (mindern verfuegbares Einkommen)
- Miet-/Pachtkosten
- Krankheitskosten / Pflegepflichten

**Berechnung Tagessatz:**
Nettoeinkommen / 30 = Tagessatz; Mindest 1 EUR (§ 40 Abs. 2 Satz 2 StGB).

## Output-Template beschraenkter Einspruch

**Adressat:** Amtsgericht — Tonfall: sachlich-foermlich

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Beschraenkter Einspruch nach § 410 Abs. 2 StPO

Sehr geehrte Damen und Herren,

namens meines Mandanten lege ich Einspruch gegen den Strafbefehl
vom [DATUM] ein und beschraenke diesen auf die festgesetzten
Rechtsfolgen, naemlich:

[Variante A]: die Tagessatzhoehe von [BETRAG] EUR je Tagessatz.
Das tatsaechliche Nettoeinkommen meines Mandanten betraegt
[BETRAG] EUR monatlich (Nachweise in der Anlage). Der korrekte
Tagessatz betraegt daher [BETRAG / 30] EUR.

[Variante B]: das Fahrverbot von [DAUER] Monaten. Mein Mandant
ist auf sein Fahrzeug zur Berufsausuebung angewiesen [Begründung].

Ich beantrage Termin zur Hauptverhandlung und uebersende
anliegend die einkommensrelevanten Unterlagen.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Beschraenkt-Einspruch nur nach ausdruecklicher Mandantenanweisung.
- Schriftliche Aufklaerung ueber Rechtskraft des Schuldspruchs und Verboescherungs-Risiko.
- Einkommensnachweise vor der Hauptverhandlung vollstaendig einreichen.
- Frist § 410 Abs. 1 StPO (2 Wochen) beachten — gilt auch fuer beschraenkten Einspruch.
