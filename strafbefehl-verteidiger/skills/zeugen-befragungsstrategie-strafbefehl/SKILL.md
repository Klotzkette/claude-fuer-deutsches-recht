---
name: zeugen-befragungsstrategie-strafbefehl
description: "Zeugen Befragungsstrategie Strafbefehl: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zeugen Befragungsstrategie Strafbefehl

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Zeugen Befragungsstrategie Strafbefehl** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-zeugen-befragungsstrategie` | Hauptverhandlung nach Strafbefehl-Einspruch — Zeugen erschuettern oder Entlastungszeugen foerdern. Prüfraster Glaubwürdigkeitsanalyse Aussage-Konstanz Vorhalt fruehere Aussage Fragerecht § 240 StPO. Normen § 68 StPO Zeugenpflichten § 52 StPO Zeugnisverweigerungsrecht § 244 StPO Beweisanträge. Output Befragungsstrategie-Memo Fragenkatalog für Belastungs- und Entlastungszeugen. Abgrenzung: strafbefehl-hauptverhandlung-vorbereitung für allgemeine HV-Vorbereitung. |
| `strafbefehl-zulaessigkeit-407` | Zulässigkeit des Strafbefehls nach § 407 StPO. Nur Vergehen. Sanktionskatalog § 407 Abs. 2 StPO. Sachliche Zuständigkeit Amtsgericht. Keine U-Haft. Keine Beweisprobleme die Hauptverhandlung erfordern. Ablehnung durch Richter § 408 Abs. 3 StPO. Nichtigkeit bei Zulässigkeitsmaengeln. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Zeugen Befragungsstrategie Strafbefehl**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-zeugen-befragungsstrategie`

**Fokus:** Hauptverhandlung nach Strafbefehl-Einspruch — Zeugen erschuettern oder Entlastungszeugen foerdern. Prüfraster Glaubwürdigkeitsanalyse Aussage-Konstanz Vorhalt fruehere Aussage Fragerecht § 240 StPO. Normen § 68 StPO Zeugenpflichten § 52 StPO Zeugnisverweigerungsrecht § 244 StPO Beweisanträge. Output Befragungsstrategie-Memo Fragenkatalog für Belastungs- und Entlastungszeugen. Abgrenzung: strafbefehl-hauptverhandlung-vorbereitung für allgemeine HV-Vorbereitung.

# Zeugen-Befragungsstrategie in der Hauptverhandlung

## Triage zu Beginn

1. **Wer sind die Belastungszeugen?** — Polizeibeamte, Geschaedigte, Passanten, Sachverstaendige — unterschiedliche Erschuetterungsstrategien.
2. **Haben die Zeugen fruehere Aussagen gemacht?** — Polizeivernehmung, Anhoerung im OWi-Verfahren, andere Verfahren — Inkonsistenzen nutzen.
3. **Zeugnisverweigerungsrecht vorhanden?** — § 52 StPO: Angehoerige; § 53 StPO: Berufsgeheimnisstraeger. Zeuge ueber Recht belehrt?
4. **Aussage-Konstanz pruefen:** Sind Angaben in der Polizeiaussage identisch mit der HV-Aussage? Abweichungen sind Angriffspunkt.
5. **Schriftsatzzeugen:** Dokumentarische Beweise (Messprotokolle, Bericht der Polizei) als Ergaenzung zu Zeugenbefragung.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 52 StPO** — Zeugnisverweigerungsrecht fuer Angehoerige; ohne Belehrung = absolutes Beweisverwertungsverbot
- **§ 53 StPO** — Zeugnisverweigerungsrecht fuer Berufsgeheimnisstraeger (Aerzte, Anwaelte, etc.)
- **§ 55 StPO** — Auskunftsverweigerungsrecht bei Selbstbelastung (nemo tenetur)
- **§ 68 StPO** — Zeugenpflichten: erscheinen, Zeugnis ablegen (mit Ausnahmen)
- **§ 68a StPO** — Fragen nach Vorstrafen des Zeugen zulaessig zur Glaubwuerdigkeitspruefung
- **§ 240 StPO** — Fragerecht; alle Beteiligten koennen Fragen stellen
- **§ 249 StPO** — Urkundenbeweis; Vorlesen von Dokumenten
- **§ 254 StPO** — Verlesung von Protokollen richterlicher Vernehmung (Vorhalt)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vorbereitung Zeugenbefragung — Checkliste

```
□ Aktenexzerpt aller Zeugenaussagen aus Ermittlungsakte erstellt?
□ Fruehere Aussagen mit HV-Aussage (soweit vorhersehbar) abgeglichen?
□ Bekannte Inkonsistenzen notiert (mit Blatt-/Bandangabe)?
□ Zeugnisverweigerungsrecht geprueft? Belehrung dokumentiert in Akte?
□ Angehoerigen-Verhaeltnis geprueft (§ 52 StPO)?
□ Fragerechts-Strategie festgelegt (offene oder geschlossene Fragen)?
```

## Befragungs-Strategie nach Zeugentyp

**Polizeibeamter:**
- Dienstprotokoll: Wann, Wo, Was genau aufgeschrieben?
- Erinnerung oder Protokoll-Wiedergabe? ("Erinnern Sie sich persoenlich oder lesen Sie aus Protokoll?")
- Sicherheitsabstand, Sichtweitverhaeltnisse, Beschilderung — Messbedingungen
- Schulung fuer das eingesetzte Messgeraet?

**Geschaedigter/Opfer-Zeuge:**
- Emotionale Beteiligung → Glaubwuerdigkeitsanalyse
- Widersprueche zu frueheren Angaben vorhalt
- Schadensbild genau beschreiben lassen

**Sachverstaendiger:**
- Methodik und Annahmen hinterfragen
- Fehlerspannen und Unsicherheiten thematisieren
- Eigener Gegensachverstaendiger ankuendigen

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zeugen-Befragungsstrategie fuer Strafbefehl-Verfahren erstellen | Frageliste nach Schema; Template unten |
| Variante A — Zeuge ist Belastungszeuge offensichtlich feindlich | Kurze konfrontative Befragung; kein ausfuehrliches Kreuzverhoer |
| Variante B — Zeuge kennt Mandanten gut Entlastung moeglich | Entlastungszeuge foerdern; ausfuehrliche Befragung zu Gunsten |
| Variante C — Zeuge verweigert Aussage zu erwarten | Befragungsstrategie fuer Aussageverweigerung vorbereiten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Frageliste Zeuge

```
Zeuge: [NAME]
Beweisthema: [Was soll durch Befragung erreicht werden?]

Fragen:
1. [Einstiegsfrage, offen und neutral]
2. [Vertiefungsfrage zur frueheren Aussage]
3. [Vorhalt-Frage: "In Ihrer Aussage vom [DATUM] haben Sie [X] gesagt..."]
4. [Praezisionsfrage zur Wahrnehmungsgrundlage]
5. [Abschlussfrage fuer entlastenden Aspekt]

Erwartetes Ergebnis: [Entlastung / Erschuetterung / Vorhalt]
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

- Keine Fragen stellen, deren Antwort unbekannt ist und schaden koennte.
- Vorhalt nur mit konkreter Fundstelle in der Akte — nie pauschal.
- Zeugnisverweigerungsrecht-Verletzung sofort in der HV ruegen.
- Anwaltliche Endkontrolle bei Frageliste vor HV.

## 2. `strafbefehl-zulaessigkeit-407`

**Fokus:** Zulässigkeit des Strafbefehls nach § 407 StPO. Nur Vergehen. Sanktionskatalog § 407 Abs. 2 StPO. Sachliche Zuständigkeit Amtsgericht. Keine U-Haft. Keine Beweisprobleme die Hauptverhandlung erfordern. Ablehnung durch Richter § 408 Abs. 3 StPO. Nichtigkeit bei Zulässigkeitsmaengeln.

# Zulaessigkeit des Strafbefehls — § 407 StPO

## Triage zu Beginn

1. **Ist das vorgeworfene Delikt ein Vergehen?** — Strafbefehl ist nur bei Vergehen zulaessig (§ 407 Abs. 1 Satz 1 StPO); Verbrechen (§ 12 Abs. 1 StGB, Mindeststrafe 1 Jahr) schliessen Strafbefehl aus.
2. **Ueberschreitet die vorgeschlagene Sanktion den Rahmen des § 407 Abs. 2 StPO?** — Nur bestimmte Sanktionen zulaessig; Freiheitsstrafe nur mit Bewaehrung und nur bis 1 Jahr.
3. **Ist der Richter sachlich zustaendig?** — Strafbefehl kann nur Strafrichter des Amtsgerichts erlassen (§ 407 Abs. 1 Satz 1 StPO); Schoeffengericht und LG sind unzustaendig.
4. **Liegt keine Untersuchungshaft vor?** — Bestehende U-Haft schliesst Strafbefehlsverfahren aus; § 407 gilt nur wenn der Beschuldigte auf freiem Fuss ist.
5. **Keine Hauptverhandlungs-Notwendigkeit?** — Komplexe Beweisfragen, viele Zeugen, Sachverstaendige — wenn HV unabdingbar ist, soll Richter ablehnen (§ 408 Abs. 3 StPO).

## Zulaessiger Sanktionskatalog nach § 407 Abs. 2 StPO

| Sanktion | Grenze |
|---------|--------|
| Geldstrafe | Keine Obergrenze (aber § 40 StGB: max 360 TS) |
| Freiheitsstrafe mit Bewaehrung | Bis 1 Jahr (§ 407 Abs. 2 Nr. 1) |
| Verwarnung mit Strafvorbehalt | § 59 StGB |
| Fahrverbot | §§ 44 StGB, 25 StVG |
| Einziehung | §§ 73, 74 StGB |
| Verfall | § 73 StGB |
| Entziehung Fahrerlaubnis | § 69 StGB inkl. Sperrfrist |
| Berufsverbot | § 70 StGB |
| Absehen von Strafe | § 60 StGB |

**NICHT zulaessig im Strafbefehl:** Sicherungsverwahrung, Unterbringung in Entziehungsanstalt, Freiheitsstrafe ohne Bewaehrung.

## Zentrale Normen

- **§ 407 Abs. 1 StPO** — Zulaessigkeit: Vergehen, auf Antrag der Staatsanwaltschaft, Strafrichter zustaendig
- **§ 407 Abs. 2 StPO** — Sanktionskatalog; abschliessende Aufzaehlung
- **§ 408 Abs. 1 StPO** — Richterliche Entscheidung: Zustimmung oder Ablehnung
- **§ 408 Abs. 2 StPO** — Ablehnung bei Bedenken gegen Sanktionsangemessenheit
- **§ 408 Abs. 3 StPO** — Ablehnung wenn Hauptverhandlung notwendig erscheint
- **§ 12 StGB** — Abgrenzung Verbrechen / Vergehen
- **§ 407 Abs. 1 Satz 4 StPO** — Beschuldigter muss gehoert werden koennen; keine U-Haft

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BGH (GSSt) 03.02.2025 — GSSt 1/24 (KCanG): Bei Cannabisvorwurf ist die sanktionsfreie Eigenkonsummenge tatbestandlich auszuklammern — Strafbefehl in der Variante "Verbrechen oder Vergehen" nach KCanG nur bei Ueberschreiten der sanktionsfreien Grenzen zulaessig; im Uebrigen § 170 Abs. 2 StPO. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- Verfassungsrechtliche Maßstaebe an die Bestimmtheit der Anklage nach Art. 103 Abs. 2 GG gelten auch fuer den Strafbefehl (§ 409 StPO); vgl. BVerfG-Linie 2 BvR. Aktualisierungen vor Ausgabe in dejure.org / bverfg.de pruefen.
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 speziell zur Zulaessigkeit nach § 407 StPO ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 407 StPO Zulaessigkeit" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pruef-Checkliste Zulaessigkeit

```
□ Delikt ist Vergehen (§ 12 Abs. 2 StGB), nicht Verbrechen?
□ Sachliche Zustaendigkeit: Strafrichter des Amtsgerichts?
□ Sanktion liegt im Katalog des § 407 Abs. 2 StPO?
□ Freiheitsstrafe nur mit Bewaehrung und nur bis 1 Jahr?
□ Kein Haftbefehl gegen Beschuldigten?
□ Beschuldigter anhoerbar (nicht auf der Flucht, greifbar)?
□ Kein zwingendes Hauptverhandlungserfordernis (viele Zeugen, komplexe Sachverstaendigenfragen)?
```

## Schritt-fuer-Schritt-Workflow

1. **Strafbefehl erhalten → Zulaessigkeitspruefung sofort** (parallel zur Fristenberechnung).
2. **Delikt qualifizieren:** Vergehen oder Verbrechen? Bei Zweifeln Fischer StGB § 12 konsultieren.
3. **Sanktionspruefung:** Liegt die Rechtsfolge im Katalog des § 407 Abs. 2 StPO?
4. **Bei Unzulaessigkeit:** Antrag auf Nichtigkeitsfeststellung oder Einspruch mit entsprechender Ruege.
5. **In der HV:** Unzustaendigkeitsruege oder Nichtigkeitsruege vortragen.

## Harte Leitplanken

- Nichtigkeit eines unzulaessigen Strafbefehls tritt von Amts wegen ein — trotzdem Einspruch einlegen um Rechtskraft zu verhindern.
- Zulaessigkeitsrueage in der Hauptverhandlung vortragen, nicht erst in der Revision.
- Anwaltliche Endkontrolle bei Qualifizierung Vergehen/Verbrechen.
