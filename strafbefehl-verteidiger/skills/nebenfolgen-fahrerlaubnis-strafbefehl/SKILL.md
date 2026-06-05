---
name: nebenfolgen-fahrerlaubnis-strafbefehl
description: "Nebenfolgen Fahrerlaubnis Strafbefehl: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nebenfolgen Fahrerlaubnis Strafbefehl

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Nebenfolgen Fahrerlaubnis Strafbefehl** im Plugin Strafbefehl-Verteidigung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-nebenfolgen-fahrerlaubnis` | Fahrerlaubnisentzug § 69 StGB und Fahrverbot § 44 StGB im Strafbefehl. Regelentziehung § 69 Abs. 2 StGB bei §§ 315c 316 142 StGB. Sperrfrist § 69a StGB. Vorzeitige Aufhebung § 69a Abs. 7 StGB. Abgrenzung § 25 StVG (OWi-Fahrverbot). MPU-Anforderungen. Haertfall-Argumente. |
| `strafbefehl-pflichtverteidiger` | Pflichtverteidigerbestellung im Strafbefehlsverfahren nach § 140 StPO. Notwendige Verteidigung. Antrag auf Beiordnung § 141 StPO. Bestellung durch Gericht. Auswechslung des Pflichtverteidigers § 143a StPO. Gebühren Nr. 4100 ff. VV-RVG. |
| `strafbefehl-polizeifilmerei-201-kug` | Strafbefehl wegen Filmens oder Fotografierens von Polizeieinsätzen, Versammlungen oder Kontrollen: prüft § 201 StGB, § 201a StGB, KunstUrhG/KUG §§ 22 bis 23 sowie § 33, Beweissicherung, Tonspur, Veröffentlichung, Beschlagnahme des Smartphones, Einspruch, Einlassung und Verteidigungsstrategie. |

## Arbeitsweg

Im Plugin Strafbefehl-Verteidigung gilt für **Nebenfolgen Fahrerlaubnis Strafbefehl**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-nebenfolgen-fahrerlaubnis`

**Fokus:** Fahrerlaubnisentzug § 69 StGB und Fahrverbot § 44 StGB im Strafbefehl. Regelentziehung § 69 Abs. 2 StGB bei §§ 315c 316 142 StGB. Sperrfrist § 69a StGB. Vorzeitige Aufhebung § 69a Abs. 7 StGB. Abgrenzung § 25 StVG (OWi-Fahrverbot). MPU-Anforderungen. Haertfall-Argumente.

# Nebenfolgen Fahrerlaubnis im Strafbefehl

## Triage zu Beginn

1. **Fahrverbot (§ 44 StGB) oder Fahrerlaubnisentzug (§ 69 StGB)?** — Grundlegend verschieden: Fahrverbot ist befristete Sperre (1-6 Monate), Entzug vernichtet die Fahrerlaubnis.
2. **Liegt ein § 69 Abs. 2-Regelfall vor?** — §§ 315a, 315c, 316, 142 StGB (bei schwerem Unfall), 315d StGB — bei diesen Delikten wird Ungeeignetheit vermutet; Widerlegung moeglich aber schwer.
3. **Sperrfrist nach § 69a StGB:** Wie lang? 6 Monate bis 5 Jahre (bei groben Verstaessen bis 10 Jahre oder dauernd).
4. **Ist die Fahrerlaubnis fuer den Beruf notwendig?** — Haertefall-Argument, mildert aber nur im Ausnahmefall (§ 69 StGB ist auf Fahreignung ausgerichtet, nicht auf Konsequenzen).
5. **Vorzeitige Aufhebung der Sperrfrist nach § 69a Abs. 7 StGB?** — Halbe Sperrfrist abgelaufen, neue Erkenntnisse zur Fahreignung.

## Zentrale Normen

- **§ 44 StGB** — Fahrverbot: Nebenstrafe, 1 bis 6 Monate, wirksam bei Einziehung des Fuehrerscheins
- **§ 69 StGB** — Entziehung der Fahrerlaubnis: bei Ungeeignetheit, keine Strafe sondern Massregel
- **§ 69 Abs. 2 StGB** — Regelungeeignetheit bei bestimmten Katalogtaten (§§ 315a, 315c, 316, 142 StGB)
- **§ 69a StGB** — Sperrfrist: Mindest 6 Monate, Regelfall 6 Monate bis 5 Jahre; Ausnahme bis 10 Jahre oder dauernd
- **§ 69a Abs. 7 StGB** — vorzeitige Aufhebung der Sperrfrist nach halbem Ablauf
- **§ 25 StVG** — Fahrverbot im OWi-Verfahren (1-3 Monate); grundsaetzlich anders als § 44 StGB
- **§ 11 FeV** — MPU-Anforderung durch Fahrerlaubnisbehoerde

## Aktuelle Rechtsprechung (Stand Mai 2026)

- KCanG-Folgeproblem fuer Fahrerlaubnis nach BGH (GSSt) 03.02.2025 — GSSt 1/24 und § 24a Abs. 1a StVG (THC-Grenzwert 3,5 ng/ml im Blutserum, in Kraft seit 22.08.2024): Bei sanktionsfreier Eigenkonsumlage bleibt die straßenverkehrsrechtliche Eignungsfrage (FeV) eigenständig zu prüfen; die strafrechtliche Bewertung determiniert nicht das FeV-Verfahren. Offene Fundstelle zum GSSt-Beschluss: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 zur Eignungsfrage nach § 11 FeV bei einmaligem Cannabiskonsum nach KCanG-Inkrafttreten ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de / bverwg.de unter "Cannabis Fahreignung FeV" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Fahrerlaubnis-Strategie

```
Im Strafbefehl: Fahrverbot § 44 StGB?
├─ JA → Dauer verhältnismaessig? Berufsbedingte Notwendigkeit?
│ ├─ Ja: Einspruch mit Haertefallargument (Ausnahmen eng!)
│ └─ Nein: akzeptieren, ggf. Timing-Optionen nutzen
└─ Im Strafbefehl: Entziehung § 69 StGB?
 ├─ Regeldelikt § 69 Abs. 2 StGB?
 │ ├─ Ja: Widerlegungs-Argument vorbereiten (besondere Einzelfallumstaende)
 │ └─ Nein: Individualpruefung — konkrete Ungeeignetheit bestreiten
 ├─ Sperrfrist verhandelbar? (§ 69a StGB)
 │ └─ Nach halbem Ablauf: § 69a Abs. 7-Antrag vorbereiten
 └─ MPU vorgesehen oder droht sie?
 └─ MPU-Vorbereitung parallel starten (§ 11 FeV)
```

## Argumente fuer Widerlegung § 69 Abs. 2 StGB

**Moeglicherweise widerlegende Umstaende:**
- Einmalige Ausnahmesituation (nachgewiesen)
- Bislang 20+ Jahre unfallfreies Fahren
- Medizinisch dokumentierter Ausnahmezustand
- Erheblich eingeschraenkte Vorwerfbarkeit (§ 21 StGB)
- Geringe Alkoholmenge, BAK klar unter Grenzwert fuer harte Vermutung

**Nicht ausreichend:**
- Berufliche Notwendigkeit der Fahrerlaubnis
- Wirtschaftliche Haerte
- Langer Zeitablauf allein

## Harte Leitplanken

- § 69 StGB ist Massregel, keine Strafe — Verhältnismaessigkeit wird anders bewertet.
- MPU-Anforderung durch Behoerde ist eigenstaendiger Verwaltungsrechtsweg.
- Haertefall-Argument bei § 69 StGB selten erfolgreich — Mandant realistisch informieren.
- Sperrfrist-Antrag nach § 69a Abs. 7 StGB erst nach halber Mindestlaufzeit.

## 2. `strafbefehl-pflichtverteidiger`

**Fokus:** Pflichtverteidigerbestellung im Strafbefehlsverfahren nach § 140 StPO. Notwendige Verteidigung. Antrag auf Beiordnung § 141 StPO. Bestellung durch Gericht. Auswechslung des Pflichtverteidigers § 143a StPO. Gebühren Nr. 4100 ff. VV-RVG.

# Pflichtverteidiger im Strafbefehlsverfahren

## Triage zu Beginn

1. **Liegt ein Fall notwendiger Verteidigung vor?** — § 140 Abs. 1 StPO: Hauptverhandlung vor LG oder Schwurgericht; Freiheitsstrafe > 1 Jahr droht; § 140 Abs. 2 StPO: erhebliche Schwierigkeit der Sach- oder Rechtslage; Unfaehigkeit zur Selbstverteidigung.
2. **Ist der Mandant mittellos?** — Beiordnung ist unabhaengig von Mittellosigkeit (§ 140 StPO), aber bei Eigenantrag nach § 140 Abs. 2 StPO sollte Beduerfftigkeit ergaenzend dargelegt werden.
3. **Hat der Mandant einen Wunschverteidiger?** — Mandant hat Recht auf Wahlverteidiger; wenn dieser nicht erschwinglich, Beiordnung des Wunschverteidigers als Pflichtverteidiger nach § 142 Abs. 5 StPO moeglich.
4. **Ist die Beiordnung bereits beantragt?** — Antrag kann von Staatsanwalt, Gericht oder Beschuldigtem gestellt werden (§ 141 Abs. 1 StPO).
5. **Bestellung im laufenden Strafbefehlsverfahren?** — Nach Einspruch gilt ab Hauptverhandlung die Pflichtverteidiger-Pflicht wenn Freiheitsstrafe mit Bewaehrung im Raum steht.

## Zentrale Normen

- **§ 140 Abs. 1 StPO** — Faelle notwendiger Verteidigung: u.a. Hauptverhandlung vor LG/OLG, Verbrechensanklage, U-Haft, Unterbringung
- **§ 140 Abs. 2 StPO** — Faelle notwendiger Verteidigung: erhebliche Schwierigkeit, Unfaehigkeit zur Selbstverteidigung, Schwere des Vorwurfs
- **§ 141 StPO** — Zeitpunkt der Bestellung; auch auf Antrag des Beschuldigten
- **§ 142 StPO** — Verfahren der Bestellung; Wunschverteidiger zu beruecksichtigen
- **§ 143a StPO** — Ruecknahme der Bestellung; Auswechslung nur in Ausnahmefaellen
- **Nr. 4100 ff. VV-RVG** — Gebuehren in Strafsachen; Verguerverguetungsanspruch des beigeordneten Anwalts gegen die Staatskasse

## Aktuelle Rechtsprechung (Stand Mai 2026)

- Geltungsgrundlagen: § 140 StPO i. d. F. nach RL (EU) 2016/1919 (PKH-Richtlinie Strafverfahren), umgesetzt seit Dezember 2019, weiterhin maßgeblich; Aktualisierungen vor Ausgabe in dejure.org / openjur.de pruefen.
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 speziell zur notwendigen Verteidigung im Strafbefehlsverfahren ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 140 StPO Strafbefehl" durchführen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Entscheidungsbaum Pflichtverteidiger-Bestellung

```
Pflichtverteidiger notwendig?
├─ § 140 Abs. 1 StPO (kraft Gesetzes):
│ ├─ Hauptverhandlung vor LG/OLG? → automatisch
│ ├─ Verbrechensanklage? → automatisch
│ ├─ U-Haft oder Unterbringung? → automatisch
│ └─ Freiheitsstrafe > 1 Jahr zu erwarten? → automatisch
└─ § 140 Abs. 2 StPO (auf Antrag bei Ermessen):
 ├─ Schwierige Sach- oder Rechtslage? → Antrag stellen
 ├─ Mandant nicht in der Lage sich selbst zu verteidigen? → Antrag stellen
 └─ Schwere des zu erwartenden Urteils? → Antrag mit Begruendung

Wunschverteidiger moeglich?
├─ Ja → § 142 Abs. 5 StPO-Antrag
└─ Nein → Gerichtsliste; Recht auf qualifizierten Anwalt
```

## Antrag auf Pflichtverteidiger-Bestellung — Template

**Adressat:** Amtsgericht / Staatsanwaltschaft — Tonfall: sachlich-foermlich

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Beiordnung als Pflichtverteidiger nach § 141 StPO

Ich beantrage meine Beiordnung als Pflichtverteidiger fuer [NAME].

Begruendung: [Einer der § 140-Gruende, z.B.: "Die Sach- und
Rechtslage ist komplex, da [Beschreibung]. Der Angeklagte ist
nicht in der Lage, sich selbst zu verteidigen."]

Ich bin bereit, das Mandat zu den Pflichtverteidiger-Gebuehren
nach Nr. 4100 ff. VV-RVG zu uebernehmen.

Mit freundlichen Gruessen [KANZLEI]
```

## Harte Leitplanken

- Pflichtverteidiger-Beiordnung nie verzoegern — bei notwendiger Verteidigung ohne Beiordnung = absoluter Revisionsgrund.
- Wunschverteidiger des Mandanten beachten und § 142 Abs. 5 StPO beantragen.
- Auswechslung nach § 143a StPO nur bei ernsthaftem Zerruettnis.
- Gebuehrenanspruch gegen Staatskasse entsteht mit Beiordnung.

## 3. `strafbefehl-polizeifilmerei-201-kug`

**Fokus:** Strafbefehl wegen Filmens oder Fotografierens von Polizeieinsätzen, Versammlungen oder Kontrollen: prüft § 201 StGB, § 201a StGB, KunstUrhG/KUG §§ 22 bis 23 sowie § 33, Beweissicherung, Tonspur, Veröffentlichung, Beschlagnahme des Smartphones, Einspruch, Einlassung und Verteidigungsstrategie.

# Strafbefehl Nach Polizeifilmerei

## Worum Es Geht

Dieser Skill greift, wenn ein Strafbefehl, eine polizeiliche Anhörung oder ein Ermittlungsverfahren daraus entsteht, dass jemand einen Polizeieinsatz, eine Versammlung, eine Kontrolle oder eine konflikthafte Amtshandlung mit dem Smartphone dokumentiert hat.

Die Arbeit beginnt nicht mit Empörung, sondern mit einer kühlen Sortierung: **Was wurde aufgenommen? Wer sprach? Wo? Wie laut? Wurde veröffentlicht? Wurde das Handy sichergestellt? Gibt es eine Frist gegen den Strafbefehl?**

## Sofort-Triage

1. **Frist:** Zustellung des Strafbefehls notieren; Einspruchsfrist § 410 StPO läuft zwei Wochen.
2. **Vorwurf:** § 201 StGB, § 201a StGB, KunstUrhG/KUG, Widerstand, tätlicher Angriff, Nötigung oder Datenschutz-Nebenargument?
3. **Material:** Originalvideo sichern, Metadaten nicht verändern, Kopie für Verteidigung erstellen.
4. **Ort:** öffentliche Versammlung, Straße, Bahnhof, Kontrollstelle, Polizeiwache, Wohnung, Krankenhaus oder Schule?
5. **Ton:** allgemeine Einsatzkommunikation, laut gesprochene Anweisung, Gespräch mit einzelnen Betroffenen, Personalienabfrage, vertrauliche Lagebesprechung?
6. **Bild:** nur Polizei, auch Dritte, verletzte/hilflose Personen, Kinder, private Wohnungen, intime/gesundheitliche Lage?
7. **Veröffentlichung:** nur gespeichert, an Verteidigung/Presse geschickt, in Chatgruppe geteilt, auf X/Instagram/TikTok/YouTube gepostet?
8. **Polizeimaßnahme:** Filmverbot, Platzverweis, Identitätsfeststellung, Sicherstellung/Beschlagnahme, Löschungsverlangen, Gewaltanwendung?

## Verteidigungslinie Nach Tatbestand

### § 201 StGB

Der zentrale Angriffspunkt ist das Merkmal **nichtöffentlich gesprochenes Wort**. Ein Polizeibefehl, eine laut vernehmbare Einsatzansage oder eine Kommunikation inmitten einer öffentlichen Versammlung ist nicht automatisch vertraulich. Zu prüfen sind:

- faktische Öffentlichkeit: Wer konnte mithören?
- Rollenbezug: Amtshandlung, Dienstkommunikation, Einsatzbefehl oder privates Gespräch?
- Erwartungsschutz: durfte die sprechende Person im konkreten Umfeld auf Vertraulichkeit vertrauen?
- Beweissicherung: diente die Aufnahme der Dokumentation einer belastenden oder potentiell rechtswidrigen Maßnahme?
- Tonspur-Notwendigkeit: War gerade der Wortlaut wichtig, etwa bei Belehrung, Drohung, Auflage oder Anordnung?

Risiko bleibt bei leisen Einzelgesprächen, Personalienabfragen, Gesprächen mit Verletzten, Minderjährigen oder privaten Nebenbemerkungen. Dann ist zu prüfen, ob eine Trennung, Verpixelung, Stummschaltung oder Nichtverwertung nötig ist.

### § 201a StGB

Der Skill prüft, ob überhaupt ein höchstpersönlicher Lebensbereich, Hilflosigkeit, Verletztheit, Wohnung, geschützter Raum oder sonstiger besonders sensibler Bildinhalt betroffen ist. Eine öffentliche Amtshandlung im Straßenraum ist davon nicht ohne Weiteres erfasst. Bei Verletzten, Kindern, Wohnungen, Krankenhäusern oder intimen Situationen wird die Verteidigung defensiver und technisch sauberer: Schwärzung, Ausschnitt, Stummschaltung, keine Veröffentlichung.

### KunstUrhG/KUG

Für das KUG wird streng zwischen **Anfertigung** und **Verbreitung/öffentlicher Zur-Schau-Stellung** getrennt. §§ 22, 23, 33 KunstUrhG tragen nicht schon deshalb eine Strafbarkeit, weil ein Bild gemacht wurde. Entscheidend ist, ob ein erkennbares Bildnis verbreitet oder öffentlich gezeigt wurde und ob Rechtfertigungen wie Zeitgeschehen, Versammlung oder berechtigtes Informationsinteresse greifen.

## Einspruchsstrategie

```
Strafbefehl erhalten?
├─ Frist offen → Einspruch sofort vorbereiten, Akteneinsicht beantragen
├─ Frist abgelaufen → Wiedereinsetzung prüfen
└─ unklarer Zugang → Zustellungsakte / PZU anfordern

Vorwurf nur § 201 StGB?
├─ öffentliche Einsatzkommunikation → Nichtöffentlichkeit bestreiten
├─ Tonspur unklar → Akteneinsicht, Videoauswertung, Zeugen zur Hörbarkeit
└─ vertrauliche Passage möglich → Beschränkung, Stummschaltung, Verwertungsstrategie

Vorwurf auch KUG/§ 201a?
├─ keine Veröffentlichung → KUG-Tathandlung angreifen
├─ Veröffentlichung mit Polizeibeamten → Zeitgeschehen/Versammlung/Abwägung
└─ Dritte oder Verletzte sichtbar → Schutzmaßnahmen und Teillöschung prüfen
```

## Beweisanträge Und Belegmatrix

- Originalvideo mit vollständiger Tonspur, Zeitstempel, Standort und Geräte-Metadaten.
- Zeugen, die bestätigen können, dass die Worte allgemein hörbar waren.
- Funk-/Bodycam-/Einsatzberichte der Polizei, soweit aktenkundig oder anzufordern.
- Versammlungsanzeige, Auflagenbescheid, Polizeiverfügungen, Platzverweis, Sicherstellungsprotokoll.
- Screenshot nur als Hilfsbeleg; Originaldatei bleibt entscheidend.
- Gutachten/technische Auswertung nur, wenn die Hörbarkeit, Schnitte oder Authentizität streitig werden.

## Schriftsatz-Baustein

```text
Namens und im Auftrag des Mandanten wird dem strafrechtlichen Vorwurf entgegengetreten.
Die Aufnahme dokumentierte eine öffentliche Amtshandlung im Zusammenhang mit [Versammlung/Kontrolle/Einsatz].
Soweit Polizeibeamte zu hören sind, handelt es sich nach Aktenlage nicht um ein vertrauliches
oder nichtöffentlich gesprochenes Wort, sondern um nach außen gerichtete Einsatzkommunikation
in einem öffentlich wahrnehmbaren Vorgang. Die bloße Anfertigung von Bildaufnahmen erfüllt
zudem nicht die Tathandlung der §§ 22, 23, 33 KunstUrhG. Eine Veröffentlichung wird bestritten
bzw. ist gesondert nach Anlass, Erkennbarkeit, Zeitgeschehen und entgegenstehenden berechtigten
Interessen zu prüfen.

Beantragt wird Akteneinsicht einschließlich aller Video-, Audio-, Bodycam-, Funk-, Sicherstellungs-
und Einsatzdokumentationen sowie der Beiziehung des sichergestellten Geräts nur in einer
forensisch nachvollziehbaren Weise.
```

## Was Das Plugin Nicht Tun Darf

- Nicht pauschal behaupten: „Polizei darf man immer filmen.“
- Nicht pauschal behaupten: „Ton ist immer § 201 StGB.“
- Nicht KUG und DSGVO mit dem bloßen Herstellen von Bildern verwechseln.
- Nicht zur spontanen Veröffentlichung raten, solange Dritte, Verletzte, Kinder, private Daten oder laufende Verfahren betroffen sind.
- Nicht zu Aussagen gegenüber der Polizei raten, bevor Verteidigung, Akteneinsicht und Fristen geklärt sind.

## Anschluss-Skills

- `strafbefehl-fristen-einspruch` für Frist und Einspruch.
- `strafbefehl-akteneinsicht-147` für Akten- und Datenträgerzugang.
- `strafbefehl-beweis-und-einlassung` für Einlassungsstrategie.
- `fachanwalt-strafrecht/strafrecht-polizeifilmerei-201-stgb-kug-verteidigung` für die breitere Strafverteidigung.
- `versammlungsrecht/polizeifilmerei-beweissicherung-kug-201-stgb` für Versammlungstag, Ordner, Presse und Verwaltungsrecht.

## Qualitätsgate

Am Ende muss der Output klar sagen:

1. ob der Strafbefehl fristgerecht angegriffen werden kann,
2. welche Normen wirklich einschlägig sind,
3. welche Tatbestandsmerkmale fehlen oder zweifelhaft sind,
4. welche Passagen des Videos riskant bleiben,
5. ob eine Veröffentlichung getrennt zu prüfen ist,
6. welche Beweise sofort gesichert werden müssen,
7. welcher nächste Schriftsatz oder Antrag sinnvoll ist.
