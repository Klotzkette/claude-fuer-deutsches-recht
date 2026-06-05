---
name: gw-einfuehrung-gw-einstweilige-mandat-triage
description: "GW Einfuehrung GW Einstweilige Mandat Triage: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# GW Einfuehrung GW Einstweilige Mandat Triage

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **GW Einfuehrung GW Einstweilige Mandat Triage** im Plugin Gewerblicher Rechtsschutz. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gw-einfuehrung-rechtsschutzwege` | Einführung in die Rechtsschutzwege des gewerblichen Rechtsschutzes: Überblick über Verfahrensarten, Zuständigkeiten, Handlungsoptionen und Weichen bei Marken-, Patent-, Design-, Urheber- und Lauterkeitsverletzungen. Erstes Orientierungsgespräch und Triage. |
| `gw-einstweilige-verfuegung-spezial` | Einstweilige Verfügung im gewerblichen Rechtsschutz: Strategische Gesamtbetrachtung von Antrag bis Hauptsache. Gerichtsauswahl, Tenorformulierung, Sicherheitsleistung, Vollzug, Widerspruch und Übergang in die Hauptsache als integrierter Workflow. |
| `mandat-triage-gewerblicher-rechtsschutz` | Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs-Triage IP-Recht. Prüfraster: Mandantenrolle (Schutzrechtsinhaber Verletzer Lizenznehmer) Sachgebiet (Marke Patent Design Urheber UWG) Sofort-Fristen (einstweilige Verfuegung Dringlichkeit Verletzungsmeldung) Gerichtsauswahl Hamburg Frankfurt Muenchen Duesseldorf. Output: Routing-Entscheidung mit Folge-Skills. Abgrenzung zu verletzungs-triage (Verletzungseinschaetzung) und streitwert-igr-berechnen. |

## Arbeitsweg

Im Plugin Gewerblicher Rechtsschutz gilt für **GW Einfuehrung GW Einstweilige Mandat Triage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gw-einfuehrung-rechtsschutzwege`

**Fokus:** Einführung in die Rechtsschutzwege des gewerblichen Rechtsschutzes: Überblick über Verfahrensarten, Zuständigkeiten, Handlungsoptionen und Weichen bei Marken-, Patent-, Design-, Urheber- und Lauterkeitsverletzungen. Erstes Orientierungsgespräch und Triage.

# GewR: Einführung – Rechtsschutzwege im Überblick

## Zweck und Mandatsbezug

Dieser Skill bietet eine **strukturierte Einführung in die Rechtsschutzwege des gewerblichen Rechtsschutzes** und dient als erstes Orientierungsgespräch. Er sortiert den Sachverhalt nach Rechtsgebiet, Verfahrensart und strategischer Priorität und zeigt, welche konkreten Handlungsoptionen offenstehen. Er ist der Ausgangspunkt vor dem Einsatz spezialisierter Skills.

Mandatsbezug: Mandant kommt mit einem IP-Problem, weiß aber nicht, ob er klagen, abmahnen, anmelden oder nur prüfen lassen soll. Oder: Anwalt übernimmt neues Mandat und braucht eine erste systematische Einordnung.

## Überblick: Materielle Rechtsgebiete

### 1. Markenrecht (MarkenG, EUTMR)

- **Schutzgegenstand:** Kennzeichen (Wort, Bild, 3D, Ton, Farbe) mit Unterscheidungskraft.
- **Eingetragene Marke:** DPMA (national), EUIPO (EU), WIPO/Madrid (international).
- **Nicht eingetragene Rechte:** Unternehmenskennzeichen (§ 5 MarkenG), geografische Angaben (§ 126 ff. MarkenG).
- **Kernverletzungen:** Verwechslungsgefahr (§ 14 Abs. 2 Nr. 2 MarkenG), Ausnutzung/Beeinträchtigung bekannter Marke (Nr. 3).

### 2. Patentrecht und Gebrauchsmuster (PatG, GebrMG)

- **Schutzgegenstand:** Technische Erfindungen (Patent) oder Gebrauchsmuster (ohne Prüfung).
- **Anmeldewege:** DPMA, EPA, PCT (international).
- **Kernverletzungen:** Benutzung der geschützten Lehre (§ 9 PatG).
- **Arbeitnehmererfindungen:** ArbnErfG – besondere Pflichten des Arbeitgebers.

### 3. Designrecht (DesignG, GGV)

- **Schutzgegenstand:** Äußere Erscheinungsform eines Erzeugnisses (Formgebung).
- **Eingetragen:** DPMA, EUIPO.
- **Nicht eingetragenes Gemeinschaftsgeschmacksmuster:** 3-Jahres-Schutz, entsteht automatisch.
- **Kernverletzungen:** Herstellung identischer/ähnlicher Produkte (§ 38 DesignG).

### 4. Urheberrecht (UrhG)

- **Schutzgegenstand:** Werke der Literatur, Wissenschaft, Kunst; entsteht ohne Anmeldung.
- **Schutzrechte:** Urheberpersönlichkeitsrechte, Verwertungsrechte (§§ 15 ff. UrhG).
- **Kernverletzungen:** Unerlaubte Vervielfältigung (§ 16 UrhG), öffentliche Zugänglichmachung (§ 19a UrhG).
- **Besonderheit:** Lichtbildwerke, Datenbankwerke, Computerprogramme.

### 5. Lauterkeitsrecht (UWG)

- **Schutzgegenstand:** Lauter Wettbewerb; kein Ausschließlichkeitsrecht.
- **Anspruchsberechtigte:** Mitbewerber, Verbände (§ 8 Abs. 3 UWG).
- **Kerntatbestände:** Irreführung (§§ 5, 5a UWG), Nachahmung (§ 4 Nr. 3 UWG), Rechtsbruch (§ 3a UWG).

## Überblick: Verfahrensarten und Rechtsschutzwege

### Außergerichtlich

| Verfahren | Beschreibung | Ziel |
|---|---|---|
| Abmahnung | Aufforderung zur Unterlassung mit Unterlassungserklärung | Schnelle Einigung ohne Gericht |
| Schutzschrift | Präventive Gegendarstellung beim ZSSR | Beschlussverfügung verhindern |
| Unterlassungserklärung | Modifizierte oder vollständige Annahme | Wiederholungsgefahr ausräumen |
| DPMA-Widerspruch | Gegen eingetragene Marke (§ 42 MarkenG) | Marke löschen |
| EUIPO-Widerspruch | Gegen Unionsmarke (Art. 46 EUTMR) | Unionsmarke anfechten |

### Gerichtlicher Eilrechtsschutz

| Verfahren | Norm | Beschreibung |
|---|---|---|
| Einstweilige Verfügung (Beschluss) | §§ 935, 937 Abs. 2 ZPO | Sofortiger Unterlassungstitel ohne mündliche Verhandlung |
| Einstweilige Verfügung (Urteil) | §§ 935, 922 ZPO | EV nach mündlicher Verhandlung |
| Arrest | § 916 ZPO | Sicherung von Geldforderungen |

### Ordentliches Gerichtsverfahren

| Verfahren | Beschreibung |
|---|---|
| Unterlassungsklage | Dauerhafter Unterlassungstitel |
| Schadensersatzklage | Ersatz eingetretener Schäden |
| Auskunftsklage | Informationserzwingung (§ 140b PatG, § 19 MarkenG) |
| Lizenzbereitschaftserklärung (FRAND) | Kartellrechtlicher Sonderweg bei SEP |

### Verwaltungsverfahren (Amtsverfahren)

| Verfahren | Zuständigkeit | Beschreibung |
|---|---|---|
| DPMA-Widerspruch/Löschung | DPMA | Marke anfechten |
| DPMA-Nichtigkeitsverfahren | DPMA | Patent/Design anfechten |
| BPatG-Beschwerde | Bundespatentgericht | Gegen DPMA-Entscheidung |
| EUIPO-Widerspruch/Löschung | EUIPO | Unionsmarke anfechten |
| WIPO-UDRP | WIPO | Domain-Name-Streit |

## Kaltstart-Triage in 5 Schritten

### Schritt 1 – Schutzrecht identifizieren
- Liegt ein eingetragenes Schutzrecht vor (Marke, Patent, Design)?
- Liegt ein nicht eingetragenes Recht vor (Urheberrecht, Unternehmenskennzeichen, GGM)?
- Oder handelt es sich um einen UWG-Anspruch ohne Schutzrecht?

### Schritt 2 – Verfahrensziel klären
- Unterlassung (sofort)? → Abmahnung, EV.
- Schadensersatz? → Auskunft, dann Klage.
- Schutzrecht vernichten? → Widerspruch, Löschungsantrag.
- Eigene Position sichern? → Freedom-to-Operate, Schutzschrift.

### Schritt 3 – Dringlichkeit einschätzen
- Verletzung akut und fortlaufend? → Sofortige EV-Vorbereitung.
- Verletzung entdeckt, nicht mehr akut? → Abmahnung, dann ggf. Klage.
- Droht Verletzung erst? → Schutzschrift, Unterlassungsklage wegen Erstbegehungsgefahr.

### Schritt 4 – Beweislage prüfen
- Schutzrechtsurkunde, Registerauszug vorhanden?
- Verletzungsnachweis (Screenshot, Kaufbeleg, Zeuge) vorhanden?
- Eidesstattliche Versicherung möglich?

### Schritt 5 – Ressourcen und Kosten einschätzen
- Streitwert schätzen → Gerichts- und Anwaltskosten grob ermitteln.
- Kostenrisiko bei Verlust?
- Eigene Kostentragung vs. Kostenerstattung bei Obsiegen?

## Weichenentscheidung: Welcher Skill als nächstes?

| Situation | Empfohlener Skill |
|---|---|
| EV-Antrag vorbereiten | `gewr-einstweilige-verfuegung-eilverfahren-spezial` |
| UWG-Abmahnung | `gewr-uwg-abmahnung-checkliste` |
| Markenanmeldung | `gewr-markenanmeldung-bauleiter` |
| Markenrecherche | `markenrecherche` |
| Patentverletzung prüfen | `fto-triage` |
| Vollzug EV | `evvollzug-neu-001` |
| Erstgespräch strukturieren | `gewerblicher-rechtsschutz-kaltstart-interview` |

## Quellenregel

- MarkenG: [gesetze-im-internet.de/markeng](https://www.gesetze-im-internet.de/markeng/)
- PatG: [gesetze-im-internet.de/patg](https://www.gesetze-im-internet.de/patg/)
- UWG: [gesetze-im-internet.de/uwg_2004](https://www.gesetze-im-internet.de/uwg_2004/)
- ZPO Arrestvorschriften: [dejure.org/gesetze/ZPO/916.html](https://dejure.org/gesetze/ZPO/916.html)
- Keine BeckRS-Blindzitate; aktuelle Normfassungen über gesetze-im-internet.de prüfen.

## Anschluss-Skills

- `mandat-triage-gewerblicher-rechtsschutz` – Vertiefte Mandatstriage
- `verletzungs-triage` – IP-Verletzung Erstentscheidung
- `workflow-kaltstart-und-routing` – Kaltstart-Router
- `allgemein` – Plugin-Übersicht

## 2. `gw-einstweilige-verfuegung-spezial`

**Fokus:** Einstweilige Verfügung im gewerblichen Rechtsschutz: Strategische Gesamtbetrachtung von Antrag bis Hauptsache. Gerichtsauswahl, Tenorformulierung, Sicherheitsleistung, Vollzug, Widerspruch und Übergang in die Hauptsache als integrierter Workflow.

# GewR: Einstweilige Verfügung – Strategische Gesamtbetrachtung

## Zweck und Mandatsbezug

Dieser Skill bietet eine **strategische Gesamtbetrachtung des einstweiligen Verfügungsverfahrens** im gewerblichen Rechtsschutz – von der ersten Lageeinschätzung bis zum Übergang in die Hauptsache. Er ergänzt die spezialisierten Einzelskills der `evvollzug-neu`-Gruppe durch eine übergreifende Strategie- und Koordinationsperspektive.

Mandatsbezug: Anwalt muss innerhalb von 48 Stunden entscheiden, ob er eine EV beantragt, bei welchem Gericht, mit welchem Tenor und wie er danach vorgeht. Oder: Anwalt vertritt Antragsgegner und muss innerhalb einer Woche reagieren.

## Strategische Ausgangsfragen

Vor jeder EV-Entscheidung:
1. Ist das Rechtsschutzziel wirklich ein Unterlassungsanspruch, oder geht es um Auskunft, Herausgabe oder Schadensersatz?
2. Ist der EV-Weg materiell und prozessual aussichtsreich (Verfügungsanspruch + Verfügungsgrund)?
3. Ist die Abmahnung bereits der schnellere und billigere Weg?
4. Welches Gericht bietet die beste Praxis für diesen Fall?
5. Was passiert nach dem Vollzug – Abschlussvereinbarung oder Hauptsache?

## Rechtlicher Gesamtrahmen

### Normen

- **§§ 935–945a ZPO** – Einstweiliger Rechtsschutz; Arrest und einstweilige Verfügung.
- **§ 929 Abs. 2 ZPO** – Vollziehungsfrist.
- **§ 890 ZPO** – Ordnungsmittel nach Vollzug.
- **§ 945 ZPO** – Schadensersatz bei ungerechtfertigter EV; Haftung des Antragstellers.
- **§ 926 ZPO** – Hauptsacheklage auf Anforderung des Schuldners.
- **§ 93 ZPO** – Sofortiges Anerkenntnis und Kostenfolge.

### Typische IP-Ansprüche für EV

| Rechtsgebiet | Unterlassungsanspruch | Norm |
|---|---|---|
| Markenrecht | Markenverletzung | § 14 Abs. 5 MarkenG |
| Patentrecht | Patentverletzung | § 139 Abs. 1 PatG |
| Designrecht | Designverletzung | § 42 Abs. 1 DesignG |
| Urheberrecht | Urheberrechtsverletzung | § 97 Abs. 1 UrhG |
| UWG | Unlauterer Wettbewerb | § 8 Abs. 1 UWG |
| GeschGehG | Geschäftsgeheimnisverletzung | § 6 GeschGehG |

## Strategiephase: Antragsteller

### Phase 1 – Vorprüfung (Tag 0–1)

- **Materieller Anspruch:** Besteht ein Unterlassungsanspruch? Welche Norm?
- **Verfügungsgrund:** Wann erstmals Kenntnis? Keine Selbstwiderlegung?
- **Beweislage:** Screenshot, Kaufbeleg, Schutzrechtsurkunde vorhanden?
- **Abmahnung vorher?** Ja: Reaktionsfrist abgelaufen? Nein: Direkte EV oder Abmahnung zuerst?
- **Kostenrisiko:** § 945 ZPO – Schadensersatz bei ungerechtfertigter EV; Bonität des Schuldners.

### Phase 2 – Gerichtsauswahl (Tag 1–2)

**Kriterien:**
- **Örtliche Zuständigkeit:** Sitz des Beklagten (§ 12 ZPO), Tatort (§ 32 ZPO), besonderer Gerichtsstand MarkenG/UWG.
- **Gerichtspraxis:** Einige LG erlassen EV schneller oder großzügiger als andere.
- **Spezialkammern:** Hamburg, München I, Frankfurt, Düsseldorf haben spezialisierte IP-Kammern.
- **Forum shopping:** Innerhalb der Zuständigkeitsregeln; kein missbräuchliches Forum-Shopping.

### Phase 3 – Antragsgestaltung (Tag 2–3)

- **Tenor:** Präzise Beschreibung der verbotenen Handlung; nicht zu weit, nicht zu eng.
- **Ordnungsmittelandrohung:** Immer in Tenor aufnehmen (§ 890 Abs. 2 ZPO).
- **Streitwertangabe:** Realistisch; zu hoher Streitwert erhöht Kostenrisiko.
- **Glaubhaftmachungspaket:** Eidesstattliche Versicherung + Belege.
- **Sicherheitsleistung:** Antrag auf Absehen stellen; bei unsicherer Beweislage Gegenangebot.

### Phase 4 – Vollzug (nach Erlass)

- **Fristbeginn:** § 929 Abs. 2 ZPO – Monatsfrist ab Zustellung an Antragsteller.
- **Zustellungsweg:** GV (sicher) oder beA (riskant, s. evvollzug-neu-003/004).
- **Vollstreckbare Ausfertigung:** Sofort beantragen.
- **Zustellurkunde:** In Akte, Datum im Fristenbuch.

### Phase 5 – Nach Vollzug

- **Widerspruch des Schuldners?** → Mündliche Verhandlung vorbereiten.
- **Kein Widerspruch?** → Abschlussschreiben senden (s. evvollzug-neu-007).
- **Verstoß gegen EV?** → Ordnungsmittelantrag (s. evvollzug-neu-005).
- **§ 926-Antrag des Schuldners?** → Hauptsacheklage fristgerecht erheben.

## Strategiephase: Antragsgegner

### Phase 1 – Sofortmaßnahmen nach Zustellung (Tag 0–3)

- **Zustellung prüfen:** Wirksam? Fristbeginn korrekt?
- **Tenor lesen:** Was genau ist verboten? Ist Handlung des Mandanten tatsächlich untersagt?
- **Verletzungshandlung beurteilen:** Tatsächlicher Verstoß? Oder Tenorüberschreitung?
- **Wiederholungsgefahr beseitigen?** Verletzung sofort einstellen; Wiederholungsgefahr prüfen.

### Phase 2 – Entscheidung Widerspruch oder Abschluss

| Option | Wann | Folge |
|---|---|---|
| Widerspruch (§ 924 ZPO) | Starke materielle Einwendungen | Mündliche Verhandlung, Kostenrisiko |
| Modifizierte UE | Verletzung tatsächlich gegeben, Tenor zu weit | Prozessbeendigung mit Einschränkungen |
| Vollständige UE | Klare Verletzung, Risiko gering halten | Schnelle Beendigung |
| Abschlussvereinbarung | Verhandlungsbereitschaft beider Seiten | Kompromisspakete möglich |

### Phase 3 – Widerspruchsstrategie

- **Dringlichkeitsselbstwiderlegung rügen:** Hat Antragsteller zu lange gewartet?
- **Verfügungsanspruch angreifen:** Schutzrecht ungültig, kein Verstoß, Erschöpfung, Verwirkung.
- **Verhältnismäßigkeit:** Tenor zu weit; Schaden durch EV größer als Nutzen.
- **§ 945 ZPO-Drohung:** Auf Schadensersatzanspruch bei ungerechtfertigter EV hinweisen.

## Kosten-Nutzen-Überblick EV

| Szenario | Kosten (ca.) | Erfolgschance | Anmerkung |
|---|---|---|---|
| EV mit klarer Beweislage | Gering (Anwaltskosten) | Hoch | Schnelle Durchsetzung |
| EV mit schwacher Beweislage | Hoch (§ 945 ZPO-Risiko) | Mittel | Sorgfältige Abwägung |
| Widerspruchsverfahren | Beidseitig hoch | Hälfte/Hälfte | Vergleich oft sinnvoll |
| Hauptsacheverfahren | Hoch, langwierig | Je nach Fall | Nur bei hohem Streitwert |

## Quellenregel

- [§ 935 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/935.html)
- [§ 945 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/945.html)
- [§ 926 ZPO – dejure.org](https://dejure.org/gesetze/ZPO/926.html)
- BGH-Rechtsprechung zur Dringlichkeit: [bgh.de](https://www.bundesgerichtshof.de); keine BeckRS-Blindzitate.
- Aktuelle OLG-Praxis zu Gerichtsständen: openjur.de.

## Anschluss-Skills

- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag im Detail
- `evvollzug-neu-001` bis `evvollzug-neu-008` – Vollzugsschritte
- `evvollzug-neu-008` – Schutzschrift (Gegenseite)
- `spezial-operate-verhandlung-vergleich-und-eskalation` – Vergleichsstrategie

## 3. `mandat-triage-gewerblicher-rechtsschutz`

**Fokus:** Neues Mandat im gewerblichen Rechtsschutz: Anwalt klaert welches Sachgebiet und welche Skills benoetigt werden. Eingangs-Triage IP-Recht. Prüfraster: Mandantenrolle (Schutzrechtsinhaber Verletzer Lizenznehmer) Sachgebiet (Marke Patent Design Urheber UWG) Sofort-Fristen (einstweilige Verfuegung Dringlichkeit Verletzungsmeldung) Gerichtsauswahl Hamburg Frankfurt Muenchen Duesseldorf. Output: Routing-Entscheidung mit Folge-Skills. Abgrenzung zu verletzungs-triage (Verletzungseinschaetzung) und streitwert-igr-berechnen.

# Mandat-Triage Gewerblicher Rechtsschutz

## Zweck

Gewerblicher Rechtsschutz ist hochspezialisiert nach Schutzrecht (Marke Patent Design Urheber UWG). Triage stellt das richtige Schutzrecht und die richtige Senat-Strategie sicher.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Schutzrechts-Inhaber (offensiv)
- Verletzer (defensiv)
- Mitbewerber (UWG)
- Lizenznehmer / Lizenzgeber
- Designer / Erfinder / Künstler
- Plattform-Betreiber

### Frage 2 — Schutzrechts-Art?

- Marke (Wortmarke Bildmarke Wort-Bild-Kombination 3D Hörmarke)
- Patent / Gebrauchsmuster
- Design / Geschmacksmuster
- Urheberrecht
- Verwertungs-Schutz / GEMA / VG Wort / VG Bild-Kunst
- Wettbewerbsrecht (UWG)
- Lauterkeitsrecht
- Geschäftsgeheimnisse (GeschGehG)
- Domain-Recht

### Frage 3 — Vorgang?

- Schutzrechts-Anmeldung
- Verletzungs-Verfahren (offensiv defensiv)
- Lizenz-Verhandlung
- Lizenz-Streit
- Löschungsverfahren (DPMA EUIPO)
- Einspruch
- Nichtigkeits-Klage Patent
- Open-Source-Compliance
- FTO (Freedom-to-Operate)
- Abmahnung erhalten / vorzubereiten
- Zoll-Beschlagnahme (TRIPS)

### Frage 4 — Akute Eilbedürftigkeit?

- **Einstweilige Verfügung** zugestellt / erlassen
- **Abmahnung** mit kurzer Frist
- **Messe / Produkt-Launch** binnen Tagen
- **Anhörung beim Patentamt**
- **Dringlichkeit** für eigenes EV-Verfahren — typisch ein Monat ab Kenntnis (München) bzw. zwei Monate (Hamburg)
- **Zollbeschlagnahme** läuft

### Frage 5 — Schutzrechts-Status?

- Angemeldet / registriert (mit Aktenzeichen Datum)
- Schutzrechts-Inhaber identifiziert
- Lizenzkette geklärt
- Aktiv-/Passivlegitimation

### Frage 6 — Frist?

- **EV-Dringlichkeit** Senat-Spezifisch (München ein Monat Hamburg / Berlin zwei Monate Frankfurt ein bis zwei Monate Düsseldorf länger)
- **Klage-Frist nach EV-Erlass** § 926 ZPO Aufforderung
- **Markenanmeldung-Prioritätsfrist** sechs Monate § 34 MarkenG
- **Patent-Prioritätsfrist** zwölf Monate Art. 4 PVÜ
- **Widerspruch Marken** drei Monate § 42 MarkenG
- **Patent-Einspruch** neun Monate § 59 PatG
- **Nichtigkeitsklage Marken** vier Monate nach Eintragung; danach jederzeit aber Verwirkung
- **Verjährung Verletzungs-Schadensersatz** sechs Jahre § 21 MarkenG bzw. drei Jahre § 195 BGB Standard

### Frage 7 — Wirtschaftliche Verhältnisse?

- Schutzrecht-Wert
- Versicherungs-Deckung (selten — Spezial-Versicherung gewerblicher Rechtsschutz)
- Streitwert hoch
- Sicherheitsleistung erforderlich bei EV
- Honorarvereinbarung statt RVG fast immer

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Markenrecherche | `markenrecherche` |
| Markenanmeldung DPMA | `markenanmeldung-dpma` |
| Schutzrechts-Portfolio | `schutzrechts-portfolio` |
| Erfindungsmeldung Aufnahme | `erfindungsmeldung-aufnahme` |
| FTO Freedom to Operate | `fto-triage` |
| IP-Klausel Vertrag | `ip-klausel-pruefung` |
| Open Source Prüfung | `open-source-pruefung` |
| Verletzungs-Triage | `verletzungs-triage` |
| Abmahnung Urheber | `abmahnung-urheberrecht` |
| Takedown-Anweisung | `takedown-anweisung` |
| Unterlassungsverlangen | `unterlassungsverlangen` |
| Streitwert-Bestimmung | `streitwert-igr-berechnen` |
| UWG-Wettbewerbsrecht | (Skill uwg-verstoss-pruefen — perspektivisch) |
| Patent-Nichtigkeit | (Skill patent-nichtigkeit — perspektivisch) |
| Geschäftsgeheimnis GeschGehG | (Skill geschäftsgeheimnis — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** sehr strikt — bei Mitbewerbern in selber Branche schwierig
- **Streitwert** typisch sechs- bis siebenstellig
- **Honorarvereinbarung** RVG häufig nicht ausreichend
- **Sachverständigen-Bedarf** technisch bei Patent / Design

## Eskalation

- **Telefon-Sofort** einstweilige Verfügung erlassen Zollbeschlagnahme
- **Binnen einer Stunde** Schutzschrift erforderlich Dringlichkeit verstreicht
- **Heute** Abmahnung vorbereiten Markenrecherche
- **Diese Woche** Anmeldung DPMA Schutzschrift gemäß § 945a ZPO

## Ausgabe

- `triage-protokoll-igr.md`
- Aktenanlage
- Frist im Fristenbuch (EV-Dringlichkeit hoch priorisiert)
- Streitwert-Vorabschätzung
- Senat-Empfehlung bei Konkurrenzzuständigkeit
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- MarkenG PatG GebrMG DesignG UrhG GeschGehG UWG
- ZPO §§ 921 945a 926 940
- GKG §§ 39 47 51
- BGH I. Zivilsenat X. Zivilsenat
- Ingerl/Rohnke MarkenG
- Benkard PatG
- Koehler/Feddersen UWG
