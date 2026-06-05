---
name: einstellung-153a-hauptverhandlung
description: "Einstellung 153a Hauptverhandlung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Einstellung 153a Hauptverhandlung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Einstellung 153a Hauptverhandlung** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-einstellung-153-153a-170` | Einstellung im Strafbefehlsverfahren: § 153 StPO (Geringfuegigkeit ohne Auflage) § 153a StPO (mit Auflage) § 170 Abs. 2 StPO (Einstellung mangels hinreichenden Tatverdachts). Opportunitaetsprinzip. Zustimmungserfordernisse. BZR-Eintrag bei § 153a. Auflage-Wahl Geldbusse Sozialstunden TOA. |
| `strafbefehl-hauptverhandlung-vorbereitung` | Hauptverhandlung nach § 411 StPO bei Einspruch. Termin Vorbereitungspflichten. Beweisanträge § 244 StPO. Einlassung oder Schweigen. Strafzumessung § 46 StGB. Befangenheitsantrag § 24 StPO. Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO. Schlussvortrag § 258 StPO. |
| `strafbefehl-inhalt-409-pruefung` | Prüft Strafbefehl auf Pflichtinhalt nach § 409 StPO (7 Mindestangaben) und identifiziert Nichtigkeitsgründe. Tatbeschreibung Bestimmtheitsgrundsatz Art. 103 Abs. 2 GG. Fehlerhafte Rechtsfolgen Geldstrafe Tagessatz Fahrverbot. Strafbefehlsinhalt-Checkliste. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Einstellung 153a Hauptverhandlung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-einstellung-153-153a-170`

**Fokus:** Einstellung im Strafbefehlsverfahren: § 153 StPO (Geringfuegigkeit ohne Auflage) § 153a StPO (mit Auflage) § 170 Abs. 2 StPO (Einstellung mangels hinreichenden Tatverdachts). Opportunitaetsprinzip. Zustimmungserfordernisse. BZR-Eintrag bei § 153a. Auflage-Wahl Geldbusse Sozialstunden TOA.

# Einstellung des Strafbefehlsverfahrens

## Triage zu Beginn

1. **Wie schwer ist das Delikt?** — § 153 StPO nur bei geringer Schuld und fehlendem oeffentlichen Interesse; § 153a StPO bei schwereren Faellen mit Auflagen.
2. **Ersttatverdaechtiger oder Vorstrafe?** — § 153 StPO bei fehlendem oeffentlichen Interesse; § 153a bei Vorstrafe nur ausnahmsweise.
3. **Was ist das Ziel?** — Kein BZR-Eintrag (§ 153 optimalst), kein Verfahren (§ 153a mit Geldauflage), oder Freispruch nach vollstaendiger Verteidigung.
4. **Ist Zustimmung der Staatsanwaltschaft realistisch?** — Informelle Sondierung vor foermlichem Antrag.
5. **Liegt hinreichender Tatverdacht vor?** — Falls Beweislage duenn: § 170 Abs. 2 StPO beantragen.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 153 StPO** — Einstellung bei Geringfuegigkeit: geringe Schuld, kein oeffentliches Interesse; ohne Auflage; kein BZR-Eintrag
- **§ 153a StPO** — Einstellung mit Auflage (Geldzahlung, Sozialstunden, Therapie, Wiedergutmachung); vorlaeufige Einstellung bis Auflage erfuellt; endgueltige Einstellung nach Erfuellung
- **§ 153a Abs. 1 Satz 8 StPO** — Sperrwirkung: Tat kann nach vollstaendiger Auflage-Erfuellung nicht mehr verfolgt werden (kein Prozesshindernis aber strafrechtlich erledigend)
- **§ 170 Abs. 2 StPO** — Einstellung mangels hinreichenden Tatverdachts (Einstellungsverfuegung der Staatsanwaltschaft)
- **§ 172 StPO** — Klageerzwingungsverfahren bei Einstellungsverweigerung
- **§ 32 Abs. 2 Nr. 1 BZRG** — Eintrag bei § 153a nur wenn Geldbusse > 90 Tagessaetze; bei Geldbusse <= 90 Tagessaetze kein Eintrag

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BGH (GSSt) 03.02.2025 — GSSt 1/24 (KCanG): Bei Cannabisvorwurf ist die sanktionsfreie Eigenkonsummenge (§ 3 KCanG) tatbestandlich auszuklammern; greift sie, fehlt es am Tatverdacht und es ist § 170 Abs. 2 StPO statt § 153a StPO einschlägig. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- BGH 15.07.2025 — 2 StR 644/24 (KCanG-Strafzumessung): Die gesetzliche Wertung des KCanG ist als bestimmender Strafzumessungsgrund zu beruecksichtigen — relevant fuer die Bemessung von Geldauflagen nach § 153a StPO im Cannabisbereich. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24
- Hinweis: Eine BGH-Leitentscheidung speziell zur Anwendung des § 153a StPO im Strafbefehlsverfahren ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 153a StPO Strafbefehl" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vergleich der Einstellungsmoeglichkeiten

| Norm | Voraussetzung | Auflage | BZR-Eintrag |
|------|--------------|---------|-------------|
| § 153 StPO | Geringe Schuld + kein oeff. Interesse | Keine | Kein Eintrag |
| § 153a StPO | Oeff. Interesse durch Auflage abwendbar | Ja | Nur ab 91 TS |
| § 170 Abs. 2 StPO | Kein hinreichender Tatverdacht | Keine | Kein Eintrag |
| § 46a StGB | Geschaedigter vorhanden, TOA | Keine (Milderung) | Nur bei Verurteilung |

## Schritt-fuer-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Sachverhalt qualifizieren:** Delikt-Schwere, Schadenshoehe, Vorleben — passe Antrag an passende Norm an.
2. **Informelle Sondierung bei Staatsanwaltschaft:** Telefonat oder E-Mail — ist Einstellung grundsaetzlich moeglich?
3. **Foermlichen Antrag stellen** mit Begründung und Anlage (Einkommensnachweise, Spendenbereitschaft, Schadenswiedergutmachungsnachweis).
4. **Zustimmungserfordernisse beachten:** § 153 Abs. 1 StPO: StA und Gericht; § 153a StPO: StA und Gericht und Beschuldigter.
5. **Bei § 153a:** Auflage-Erfuellungsfrist beachten; Zahlungsbeleg und Quittung sichern; Abschlussbestaetigung von Staatsanwaltschaft anfordern.
6. **Bei Ablehnung:** Wiederholung des Antrags in der Hauptverhandlung moeglich.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Einstellung nach § 153a StPO oder Einstellungsantrag | Einstellungsantrag nach Schema; Template unten |
| Variante A — Mandant will Freispruch nicht bloss Einstellung | Vollstaendige Verteidigung; Einstellung nur als Hilfsantrag |
| Variante B — Auflage nach § 153a ZPO zu hoch verhandelbar | Auflagenverhandlung vor Annahme; Reduzierung anstreben |
| Variante C — Einstellung wuerde Vorstrafeneintrag vermeiden | Einstellung § 153 ohne Auflage anstreben; § 153a als Rueckfall |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template § 153a-Antrag

**Adressat:** Staatsanwaltschaft — Tonfall: sachlich-kooperativ

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf vorlaeufige Einstellung nach § 153a StPO

Ich rege an das Verfahren gegen [NAME] gegen [Auflage-Art:
Geldzahlung / Sozialstunden / Wiedergutmachung] einzustellen.

Begründung: [NAME] ist ersttaetig, zeigt ernsthafte Reue und hat
[Wiedergutmachungshandlung] geleistet. Die Tat beschraenkt sich auf
[Tatcharakterisierung, Schadenshoehe].

Mein Mandant erklaert sich mit der Einstellung und der Auflage
ausdruecklich einverstanden.

Vorgeschlagene Auflage: Zahlung von [BETRAG] EUR an [EINRICHTUNG]
bis [DATUM].

Mit freundlichen Gruessen [KANZLEI]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Harte Leitplanken

- Zustimmung des Mandanten zur Auflage zwingend einholen und dokumentieren.
- Auflage-Erfuellungsfrist im Kalender einpflegen.
- BZR-Konsequenzen erklaeren: bei § 153a und Geldbusse bis 90 Tagessaetze kein Eintrag.
- Ablehnung der Einstellung ist kein Endpunkt — Antrag in der HV wiederholen.

## 2. `strafbefehl-hauptverhandlung-vorbereitung`

**Fokus:** Hauptverhandlung nach § 411 StPO bei Einspruch. Termin Vorbereitungspflichten. Beweisanträge § 244 StPO. Einlassung oder Schweigen. Strafzumessung § 46 StGB. Befangenheitsantrag § 24 StPO. Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO. Schlussvortrag § 258 StPO.

# Hauptverhandlung nach Einspruch — § 411 StPO

## Triage zu Beginn — Checkliste vor der HV

1. **Erscheinungspflicht klaeren:** Mandant erscheinungspflichtig (§ 411 Abs. 2 StPO); Antrag auf Entbindung moeglich wenn Sachverhalt unstreitig und nur Rechtsfolgen streitig.
2. **Beweisantraege fertig?** — Jeder Beweisantrag braucht konkretes Beweisthema und bestimmtes Beweismittel (§ 244 Abs. 3 StPO).
3. **Einlassung oder Schweigen?** — Abschluss-Entscheidung mit Mandant mindestens 1 Woche vorher treffen.
4. **Sachverstaendiger notwendig?** — Technische Fragen (Messung), medizinische Fragen (BAK), Glaubwuerdigkeitsgutachten.
5. **Verstaendigungsangebot vorher gemacht?** — § 257c StPO oder § 153a-Antrag vor HV abschliessen.

## Zentrale Normen

- **§ 411 StPO** — HV nach Einspruch; Zustellung des Termins; Beschraenkung auf Teilnahme des Verteidigers bei Entbindung
- **§ 243 StPO** — Gang der Hauptverhandlung: Aufruf, Vernehmung, Beweisaufnahme
- **§ 244 StPO** — Beweisantragsrecht und Ablehnungsgruende
- **§ 258 StPO** — Schlussvortrag; Verteidiger hat das letzte Wort
- **§ 24 StPO** — Ablehnung eines Richters wegen Befangenheit
- **§ 46 StGB** — Strafzumessungserwaeungen; Grundlage des Plaedoyers
- **§ 267 StPO** — Urteilsgruende; Grundlage fuer spaetere Revision

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vorbereiungs-(1 Woche vor HV)

1. **Aktenexzerpt aktualisieren** — alle Beweismittel, alle Zeugen, kritische Aktenstellen markieren.
2. **Einlassung finalisieren** — schriftlich vorbereiten, mit Mandant durchgehen, Reihenfolge festlegen.
3. **Beweisantraege formulieren** — pro Antrag: Beweisthema + Beweismittel + Relevanz.
4. **Plaedoyer vorbereiten** — Strafzumessungsargumente strukturieren: mildernde Umstaende, keine Vorstrafe, Schadenswiedergutmachung.
5. **Befangenheitsantrag vorbereiten** — wenn Anzeichen fuer Voreingenommenheit des Richters.
6. **Mandant ueber Ablauf der HV informieren** — Aufruf, Vernehmung, Beweisaufnahme, Plaedoyer, Letztes Wort.

## Entscheidungsbaum in der HV

```
Eroefffnung der HV:
├─ Verstaendigungs-Angebot moeglich → § 257c-Antrag vor Beginn der Beweisaufnahme
├─ § 153a-Antrag noch nicht entschieden → nochmals stellen
└─ Keine Einigung → regulaere Beweisaufnahme

Beweisaufnahme:
├─ Zeuge kommt → Befragung nach Aussage-Konstanz, Widerspruechen
├─ Sachverstaendiger geladen → Gegenfragen vorbereiten, eigenen SV ankuendigen
└─ Urkundsbeweis → Echtheits- und Verwertbarkeitsfragen stellen

Nach Beweisaufnahme:
├─ § 244 Abs. 6 StPO-Pruefung: noch Beweisantraege?
├─ Schlussvortrag § 258 StPO — strukturiert: Sachverhalt, Recht, Strafe
└─ Letztes Wort des Angeklagten § 258 Abs. 3 StPO — kurz, persoenlich
```

## Checkliste Beweisantrag-Formular

```
Beweisthema: [Was soll bewiesen werden?]
Beweismittel: [Zeuge / Sachverstaendiger / Urkunde — konkret benennen]
Erwartetes Ergebnis: [Was wird die Beweisaufnahme zeigen?]
Relevanz fuer das Verfahren: [Warum ist das entscheidungserheblich?]
Gestuetzt auf: § 244 Abs. 2 StPO (Amtsaufklaerungspflicht) /
 § 244 Abs. 4 StPO (Sachverstaendigen-Antrag)
```

## Output-Template Plaedoyer-Gliederung

```
Sehr geehrtes Gericht,

I. Sachverhalt
[Zusammenfassung der Beweisaufnahme aus Verteidigungsperspektive]

II. Rechtliche Wuerdigung
[Tatbestandspruefung, ggf. Zweifel am Vorsatz / an der Schuld]

III. Strafzumessung
Mildernde Umstaende:
- Ersttat / keine Vorstrafe (§ 46 Abs. 2 StGB)
- Gestaendnis / Reue
- Schadenswiedergutmachung (§ 46a StGB)
- Soziale Verhaeltnisse / besondere Haerteumstaende

IV. Antrag
Ich beantrage [Freispruch / Einstellung / Geldstrafe von [X] Tagessaetzen zu [Y] EUR].
```

## Harte Leitplanken

- Letztes Wort des Mandanten niemals vergessen — absoluter Revisionsgrund bei Verletzung.
- Befangenheitsantrag unverzueglich nach Kenntnis stellen.
- Beweisantraege spaetestens in der Hauptverhandlung vor Schluss der Beweisaufnahme stellen.
- Anwaltliche Endkontrolle bei allen Antraegen und Schriftsaetzen.

## 3. `strafbefehl-inhalt-409-pruefung`

**Fokus:** Prüft Strafbefehl auf Pflichtinhalt nach § 409 StPO (7 Mindestangaben) und identifiziert Nichtigkeitsgründe. Tatbeschreibung Bestimmtheitsgrundsatz Art. 103 Abs. 2 GG. Fehlerhafte Rechtsfolgen Geldstrafe Tagessatz Fahrverbot. Strafbefehlsinhalt-Checkliste.

# Strafbefehlsinhalt pruefen — § 409 StPO

## Triage zu Beginn — vor der Inhaltspruefung

1. **Liegt der Strafbefehl im Original vor?** — Abschrift reicht fuer die Pruefung, Original fuer Fristberechnung.
2. **Welches Delikt ist aufgefuehrt?** — § 409 Abs. 1 Nr. 3 StPO verlangt Angabe der gesetzlichen Merkmale und des angewandten Strafgesetzes.
3. **Sind Tatzeit und Tatort konkret benannt?** — Bestimmtheitsgrundsatz Art. 103 Abs. 2 GG; eine pauschale Datumsangabe ("in 2022 mehrfach") kann die Tat unzureichend individualisieren.
4. **Stimmt die Rechtsfolge mit dem Sanktionskatalog des § 407 Abs. 2 StPO ueberein?** — Nur zulässige Sanktionen: Geldstrafe, Freiheitsstrafe bis 1 Jahr auf Bewaehrung, Fahrverbot, Einziehung, Nebenfolgen.
5. **Ist der Tatrichter der sachlich zustaendige Richter?** — Strafbefehle darf nur der Strafrichter (§ 408 Abs. 1 StPO) oder Jugendrichter ausstellen; nicht Schoeffengericht oder LG.

## Pflichtinhalt nach § 409 Abs. 1 StPO (Nichtigkeit bei Fehlen)

| Nr. | Inhaltsmerkmal | Pruefungsaspekt |
|-----|---------------|-----------------|
| 1 | Name des Beschuldigten | Identifikation — Verwechslung moeglich? |
| 2 | Tat, Zeit und Ort | Ausreichende Individualisierung nach BGH |
| 3 | Gesetzliche Merkmale der Tat | Normen vollstaendig genannt? |
| 4 | Beweismittel | Mindestens schlagwortartig |
| 5 | Strafgesetz (angewandte Norm) | § § explizit genannt |
| 6 | Rechtsfolge konkret benannt | Geldstrafe: Tagessatzanzahl + -hoehe |
| 7 | Belehrung ueber Einspruchsrecht und -frist | § 409 Abs. 1 Nr. 7; Fehlen = anfechtbar |

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- **§ 407 StPO** — Zulaessigkeit des Strafbefehls; Strafbefehl nur bei Vergehen, Sanktionsgrenzen
- **§ 408 StPO** — Richterliche Entscheidung; Richter kann bei Bedenken ablehnen
- **§ 409 StPO** — Pflichtinhalt; Fehlen wesentlicher Elemente = Nichtigkeit oder Anfechtbarkeit
- **§ 410 StPO** — Einspruch 2-Wochen-Frist
- **Art. 103 Abs. 2 GG** — Bestimmtheitsgrundsatz
- **§ 40 StGB** — Tagessatz-System (Anzahl nach Schuld, Hoehe nach Einkommen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pruef-Checkliste Strafbefehlsinhalt

```
□ Name und Personalien des Beschuldigten korrekt (Nr. 1)?
□ Tathandlung individualisierbar beschrieben — Zeit, Ort, Modalitaet (Nr. 2)?
□ Alle gesetzlichen Tatbestandsmerkmale der vorgeworfenen Norm genannt (Nr. 3)?
□ Beweismittel wenigstens schlagwortartig aufgefuehrt (Nr. 4)?
□ Strafgesetz (Paragraf, Absatz, Alternative) explizit zitiert (Nr. 5)?
□ Rechtsfolge vollstaendig:
 - Geldstrafe: Anzahl Tagessaetze + Euro je Tagessatz?
 - Fahrverbot: Dauer, § 25 StVG oder § 44 StGB?
 - Bewaehrungsstrafe: Bewaehrungszeit, Auflagen?
 - Einziehung: Gegenstand, Wert?
□ Belehrung ueber Einspruch und 2-Wochen-Frist vorhanden (Nr. 7)?
□ Richter des Amtsgerichts unterschrieben (kein Rechtspfleger)?
□ Ausstellungsdatum aufgefuehrt?
```

## Entscheidungsbaum bei Maengeln

```
Fehler im Strafbefehl gefunden?
├─ Belehrungsfehler (Nr. 7)
│ └─ Frist laeuft nicht an → unbeschraenkte Zeit fuer Einspruch
│ + Wiedereinsetzungsantrag bei spaeterer Kenntnis (§ 44 StPO)
├─ Tatbeschreibung zu unbestimmt (Nr. 2)
│ └─ Einspruch einlegen + In HV Antrag auf Einstellung wegen
│ Verletzung Art. 103 Abs. 2 GG stellen
├─ Rechtsfolge fehlerhaft / unvollstaendig (Nr. 6)
│ └─ Einspruch (Frist sichern!) + in HV Aufhebung beantragen
└─ Sachlich unzustaendiges Gericht (z.B. Schoeffengericht)
 └─ Einspruch + Unzustaendigkeitsruege in der Hauptverhandlung
```

## Schritt-fuer-Schritt-Workflow

1. **Strafbefehl-Kopie anlegen** — Original sicher verwahren, Kopie fuer Pruefung.
2. **Checkliste § 409 StPO Punkt fuer Punkt abarbeiten** — jeden Mangel notieren.
3. **Tagessatz-Plausibilitaet pruefen:** Anzahl Tagessaetze angemessen? Tagessatzhoehe korrekt berechnet nach § 40 Abs. 2 StGB (Nettoeinkommen / 30)?
4. **Wenn Fehler: Rechtsstrategie waehlen** (s. Entscheidungsbaum).
5. **Einspruch formulieren und fristgerecht einlegen** (§ 410 Abs. 1 StPO — 2-Wochen-Frist!).
6. **In Aktenanforderung auf spezifische Maengel hinweisen** — Staatsanwaltschaft ggf. auf Fehler aufmerksam machen fuer § 153a-Gespraeche.

## Adressat und Tonfall

Schriftsatz an Gericht: sachlich-juristisch, praesize Normzitate.
Mandantenhinweis: verstaendlich-erklaerend, Fachbegriffe erklaeren.

## Harte Leitplanken

- Nichtigkeit des Strafbefehls fuehrt nicht automatisch zum Freispruch — Anklageerhebung moeglich.
- Einspruch immer fristgerecht einlegen, unabhaengig von Fehlerruegen.
- Anwaltliche Endkontrolle vor Versand.
