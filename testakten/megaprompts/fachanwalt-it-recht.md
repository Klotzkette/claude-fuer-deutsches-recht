# Megaprompt: fachanwalt-it-recht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 124 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-it-recht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt IT-Recht: ordnet Rolle (Auftraggeber, Software-Hersteller, Cloud-Anbieter), …
2. **mandat-triage-it-recht** — Strukturierte Eingangs-Abfrage für IT-rechtliche Mandate mit Fristen-Sofort-Check: Anwendungsfall neues IT-Rechtsmandat …
3. **orientierung-mandat-fachanwaltschaft** — Orientierung im IT-Recht für Mandate und Fachanwaltschaft nach FAO: Anwendungsfall Kanzlei will IT-Mandat beurteilen ode…
4. **orientierung-sonderfall-edge-case** — Orientierung: Sonderfall und Edge-Case-Prüfung: Orientierung: Sonderfall und Edge-Case-Prüfung.
5. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für IT-, Datenschutz- und Telemedienrecht: Erfassung der Konstellation, Konflikt-…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **itr-einfuehrung-rechtsmaterien** — IT-Recht einfuehrend: IT-Vertragsrecht (Beschaffung, Wartung, SLA), Datenschutz DSGVO/BDSG, IT-Sicherheit BSI-Gesetz und…
8. **itr-ki-systeme-vertragsklausel-leitfaden** — Leitfaden Vertragsklauseln für KI-Systeme: Trainings- und Inferenzphase, Black-Box-Klausel, Halluzination, Outputrechte,…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt IT-Recht: ordnet Rolle (Auftraggeber, Software-Hersteller, Cloud-Anbieter), markiert Frist (Mängelfristen Software), wählt Norm (BGB §§ 631 ff. Software, GeschGehG, UrhG §§ 69a ff. Software) und Zuständigkeit (Zivilgerichte), leitet zum passenden Spezia..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt It Recht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `ai-act-art-6-hochrisiko-ki` — AI ACT ART 6 Hochrisiko KI
- `cloud-act-vs-dsgvo-art-48-dsgvo` — Cloud ACT VS DSGVO ART 48 DSGVO
- `vertragsstrafe-pruefen` — Cloud Vertrag Datenschutz ITR
- `cyber-vorfall-sofortmassnahmen` — Cyber Datenschutz
- `datenschutzrecht-fehlerkatalog` — Datenschutzrecht Fehlerkatalog
- `dma-compliance-dokumentation-und-akte` — DMA DSA DSGVO Fachanwalt Governance
- `dsv-dsfa-update-nach-vorfall` — Dsfa Update Erstgespraech Vorfallmeldung
- `dsgvo-bussgeld-art-83-eugh-c-807-21` — DSGVO Bussgeld ART 83 Eugh C 807 21
- `hacking-haftung-paragraf-823-bgb-it-sicherheit` — Hacking Haftung Paragraf 823 BGB IT Sicherheit
- `informationstechnologierecht-tatbestand-beweis` — Informationstechnologierecht Kanzlei
- `dsv-aufnahme-statusinformation` — IT Recht Aufnahme Statusinformation Benachrichtigung ART
- `dsv-massenbenachrichtigung` — IT Recht Massenbenachrichtigung Meldekette Auftragsverarbeiter
- `dsv-stakeholder-mapping` — IT Recht Stakeholder Mapping Tonfall Krisenkommunikation
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt It Recht sind BDSG, DDG, DSGVO, TKG, TTDSG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-it-recht`

_Strukturierte Eingangs-Abfrage für IT-rechtliche Mandate mit Fristen-Sofort-Check: Anwendungsfall neues IT-Rechtsmandat geht ein und muss schnell triagiert und dem richtigen..._

# Strukturierte Eingangs-Abfrage für IT-rechtliche Mandate mit Fristen-Sofort-Check


## Aktenstart statt Formularstart

Wenn zu **Itr Open Source Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt It Recht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für IT-rechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues IT-Rechtsmandat geht ein und muss schnell triagiert und dem richtigen zugeordnet werden. Normen Art. 33 DSGVO 72-Stunden-Frist NIS-2 24-Stunden-Fruehwarnung §§ 327 ff. BGB Digitale Produkte. Prüfraster Sachgebiet Mandantenrolle Vertragstyp Phase Sofort-Fristen Cyber-Vorfall Eskalation. Output Triage-Ergebnis mit Routing zu Folgeskills und Fristen-Eskalationshinweis bei Cyber-Vorfall. Abgrenzung zu erstgespraech-mandatsannahme und cyber-incident-response-72h.

### Mandat-Triage IT-Recht

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Software-Auftraggeber (typisch Mittelstand)
- Software-Auftragnehmer (Hersteller Entwickler-Studio)
- SaaS-Anbieter / SaaS-Kunde
- Hosting / Cloud-Provider
- Plattform (Marketplaces Social Media)
- Nutzer / Endkunde
- IT-Sicherheits-Verantwortlicher
- Datenschutz-Beauftragter externer

### Frage 2 — Sachgebiet?

- Softwareerstellungs-Vertrag
- Lizenzrecht (kommerziell Open-Source)
- SaaS / Cloud Bezug
- Hosting / Domain
- IT-Sicherheit / Cyber-Vorfall
- DSGVO (an `datenschutzrecht`-Plugin)
- NIS-2 KRITIS
- AI Act (an `ki-governance`-Plugin)
- DSA Plattformhaftung
- E-Commerce-Recht (Impressum AGB Verbraucherschutz)
- Domain-Streit
- Telekommunikationsrecht TKG / TDDDG (vormals TTDSG)
- IT-Strafrecht (§§ 202a 202b 202c 263a 303a 303b StGB)

### Frage 3 — Akute Eilbedürftigkeit?

- **Cyber-Vorfall** Hacker-Angriff aktive Datenpanne
- **DSGVO-Meldung** binnen 72 Stunden Art. 33 DSGVO
- **NIS-2-Meldung** binnen 24 Stunden Frühwarnung
- **Sicherheits-Lücke** wird ausgenutzt
- **Domain-Streit** UDRP Frist
- **Behördliche Untersagung** sofortige Vollziehung
- **Filesharing-Abmahnung** mit kurzer Frist

### Frage 4 — Stand?

- Beratung vor Vertragsschluss
- Vertrag läuft — Projekt in Erstellung
- Abnahme / Live-Gang
- Mangel-Streit nach Abnahme
- Klage erhoben
- Behördliches Verfahren (BSI Datenschutzbehörde BNetzA)
- Strafverfahren bei IT-Vorfall

### Frage 5 — Vertragsbasis?

- Schriftlicher Vertrag mit Anlagen
- Lizenzbedingungen
- SLA
- Pflichtenheft Lastenheft
- Open-Source-Lizenzen im Stack

### Frage 6 — Frist?

- **DSGVO-Meldung Datenpanne** 72 Stunden Art. 33
- **NIS-2** 24 Stunden Frühwarnung 72 Stunden Vorfallsmeldung
- **Verjährung Mangel Kauf** zwei Jahre § 438 / Werk § 634a
- **Verjährung deliktisch** drei Jahre § 195 BGB
- **DSA Anordnung** Behörde

### Frage 7 — Wirtschaftliche Verhältnisse?

- Versicherung Cyber Berufshaftpflicht IT
- Berufshaftpflicht Anwalt für Beratung
- Streitwert sehr variabel
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Softwarefehler Mangelhaftung | `softwarefehler-mangelhaftung-pruefen` |
| Lizenzrechts-Streit | `softwarefehler-mangelhaftung-pruefen` plus Lizenzfokus |
| Cyber-Vorfall | EILMODUS sofort (Skill cyber-incident-response — perspektivisch) |
| DSGVO-Datenpanne | weiter an `datenschutzrecht`-Plugin |
| NIS-2 KRITIS | (Skill nis-2-compliance — perspektivisch) |
| AI Act | weiter an `ki-governance`-Plugin |
| DSA Plattform | weiter an `mandat-triage-urheber-medienrecht` |
| E-Commerce-AGB | weiter an `produktrecht`-Plugin |
| Domain-Streit | (Skill domain-streit-udrp — perspektivisch) |

## Cyber-Incident-Eilmodus

Bei aktivem Hacker-Angriff:

1. Sofortmaßnahmen: Netzwerk-Trennung Forensik-Sicherung
2. DSGVO-Meldung 72 Stunden Art. 33
3. NIS-2 Meldung wenn KRITIS
4. Strafanzeige § 202a § 303a § 303b StGB
5. Versicherer informieren
6. Kommunikationsstrategie (Kunden Mitarbeiter Öffentlichkeit)
7. Rechtssicherung Beweismittel
8. Lessons Learned und Verfahren nachschärfen

## Mandatsannahme

- **Konflikt-Check** — keine doppelte Vertretung Auftraggeber/Auftragnehmer
- **Streitwert** bei IT-Großprojekten oft sehr hoch — sechs- bis siebenstellig
- **Sachverständigen-Bedarf** IT-Forensik
- **Versicherungs-Deckung** Cyber-Versicherung BHV IT

## Eskalation

- **Telefon-Sofort** Cyber-Vorfall Datenpanne 72-Stunden-Lauf
- **Binnen einer Stunde** Untersagungs-Anordnung sofortige Vollziehung
- **Heute** DSGVO-Meldung Domain-Sperre Filesharing-Antwort
- **Diese Woche** Mangel-Klage Vertragsentwurf

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — IT-Recht Mandat triage und routen | Triage-Protokoll; Template unten |
| Variante A — Datenschutz-Schwerpunkt | DSGVO-Skills pruefen; DPA als erstes |
| Variante B — Strafrecht-Beruehrer | § 202a ff. StGB; Strafrecht-Skill einbeziehen |
| Variante C — Eilsituation Datenpanne | 72h-Frist DSGVO Art. 33; Skill cyber-incident-response |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Ausgabe

- `triage-protokoll-it-recht.md`
- Aktenanlage
- Frist im Fristenbuch (kurzfristig DSGVO 72h NIS-2 24h)
- Mandatsvereinbarung mit Honorar
- Bei Cyber-Incident: Sofort-Checkliste als Anhang
- Empfehlung Folge-Skill

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Quellen

- BGB §§ 433 ff. 535 ff. 611 631 ff.
- StGB §§ 202a 202b 202c 263a 303a 303b
- DSGVO Art. 33 34
- NIS-2-RL (in DE umgesetzt durch NIS2UmsuCG in Kraft seit 06.12.2025 — Hauptnorm § 32 BSIG n.F.)
- AI Act
- DSA
- BGH VIII. Zivilsenat
- Marly Softwarerecht
- Schneider IT-Recht

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a BRAO — Anwaltliche Grundpflichten: Interessenkonflikt-Verbot
- § 45 BRAO — Verbotene Taetigkeit (frueherer Mandant / Gegenpartei)
- Art. 33 DSGVO — 72-Stunden-Meldepflicht Datenpanne
- § 32 BSIG n. F. — NIS-2-Meldepflicht 24 Stunden / 72 Stunden
- Art. 19 NIS-2-RL (EU 2022/2555) — Haftung Geschaeftsleitungsorgane

## Triage zu Beginn
1. Besteht ein Interessenkonflikt — wurde dieselbe Partei oder Gegenseite bereits beraten (§ 43a BRAO)?
2. Liegt ein Cyber-Vorfall oder eine Datenpanne vor — laeuft die 72-Stunden-Frist (Art. 33 DSGVO)?
3. Handelt es sich um eine NIS-2-relevante Einrichtung — laeuft die 24-Stunden-Fruhwarnung (§ 32 BSIG n. F.)?
4. Welches Sachgebiet ist einschlaegig (Softwarerecht, Datenschutz, KI-VO, DSA, Plattformrecht)?
5. Wie hoch ist der Streitwert — sechsstellig oder mehr erfordert fruehs Sachverstaendigen-Bedarf klaeren?

## Output-Template — Triage-Protokoll IT-Recht
**Adressat:** Kanzlei intern (Akte) — Tonfall: strukturiert-knapp
```
TRIAGE-PROTOKOLL IT-RECHT
[DATUM] — [AKTENZEICHEN] — [NAME MANDANT]

1. Mandantenrolle: [Auftraggeber / Auftragnehmer / Plattform / Nutzer]
2. Sachgebiet: [Softwareerstellung / SaaS / DSGVO / NIS-2 / AI Act / DSA / ...]
3. Eilbeduerftigkeit:
 - Cyber-Vorfall: [Ja / Nein] — Entdeckungszeitpunkt: [DATUM UHRZEIT]
 - DSGVO-Meldung 72h laeuft ab: [DATUM UHRZEIT] (Art. 33 DSGVO)
 - NIS-2-Fruehwarnung 24h laeuft ab: [DATUM UHRZEIT] (§ 32 BSIG n. F.)
4. Konflikt-Check: [Durchgefuehrt — kein Konflikt / KONFLIKT: BESCHREIBUNG]
5. Streitwert-Schaetzung: EUR [BETRAG]
6. Naechste Schritte:
 - [MASSNAHME 1] bis [DATUM]
 - [MASSNAHME 2] bis [DATUM]
7. Routing: [FOLGE-SKILL]

Bearbeiter: [NAME RA/RAin]
```

<!-- AUDIT 27.05.2026: BGH VII ZR 198/15 (26.01.2017) NOT_FOUND auf dejure.org – Eintrag "Eilbeduerftigkeit im IT-Projektstreit, NJW 2017, 1534" gelöscht. Thema passt nicht zu IT-Recht-Triage (VII ZR ist Baurechtssenat). Kein verifizierter Ersatz recherchiert; bei Zweifel löschen. -->

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im IT-Recht für Mandate und Fachanwaltschaft nach FAO: Anwendungsfall Kanzlei will IT-Mandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung IT-Recht vor. Normen DS..._

# Orientierung im IT-Recht für Mandate und Fachanwaltschaft nach FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im IT-Recht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will IT-Mandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung IT-Recht vor. Normen DSGVO BDSG TDDDG TKG NIS2UmsuCG BSIG DDG DSA DMA KI-VO 2024/1689 EVB-IT. Prüfraster Sachgebiet IT-Vertragsrecht Datenschutzrecht IT-Sicherheitsrecht NIS-2 KI-VO Cyber-Vorfall. Output Rechtsgebietsuebersicht mit Normenhierarchie verifizierbare Quellen und Routing zu Folge-Skills. Abgrenzung zu mandat-triage-it-recht und erstgespraech-mandatsannahme.

### Fachanwalt für Informationstechnologierecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 50 Fälle in den letzten drei Jahren, davon mindestens 25 IT-rechtliche und 15 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| IT-Vertragsrecht | BGB §§ 305 ff. (AGB) §§ 631 ff. (Werkvertrag bei Softwareentwicklung) §§ 535 ff. (Mietrecht analog bei SaaS-Cloud-Modellen) |
| Datenschutz | DSGVO BDSG TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz seit 14.05.2024 vormals TTDSG) |
| Telekommunikation | TKG |
| Digitale Dienste | DDG (Digitale-Dienste-Gesetz seit 14.05.2024 ersetzt TMG für Plattformbetreiber) |
| Cybersicherheit | NIS2UmsuCG (in Kraft seit 06.12.2025) BSIG n.F. § 32 BSIG Meldepflichten |
| Plattformregulierung | DSA (EU 2022/2065) DMA (EU 2022/1925) |
| Kuenstliche Intelligenz | EU-KI-VO (EU 2024/1689) |
| Urheberrecht | UrhG bei Software §§ 69a ff. UrhG |
| Open Source | GPL MIT Apache LGPL etc. |
| Patent | PatG bei computerimplementierten Erfindungen |

## Typische Mandate

- SaaS-Verträge Cloud-Verträge Software-Lizenz
- Datenschutz-Audit Datenschutzfolgenabschätzung (siehe datenschutzrecht)
- Open-Source-Compliance
- IT-Sicherheit NIS2-Umsetzung
- KI-Governance KI-VO (siehe ki-governance)
- Plattformhaftung DSA Notice-and-Action
- Sportradardienste Algorithmen
- Eskalation bei Cyberangriff (Meldepflichten DSGVO Art. 33 / NIS2)

## Fristen

- **Datenpannenmeldung** DSGVO Art. 33 — 72 Stunden.
- **NIS2-Meldepflicht** § 32 BSIG n.F. — 24 Stunden Frühwarnung 72 Stunden Folgemeldung Abschlussbericht binnen eines Monats.
- **Vertragsverjährung** regelmäßig drei Jahre (§ 195 BGB).
- **Open-Source-Lizenzverletzung** Verjährung drei Jahre.

## Hauptgerichte

- Landgericht Zivilkammern für IT-Sachen.
- OLG.
- BGH I. Zivilsenat oder III. Zivilsenat je nach Bezug.
- Bundeskartellamt / Vergabekammer bei öffentlichen IT-Aufträgen.
- BfDI und Landesdatenschutzbehörden.

## Berufsverband

- Davit Deutscher Anwaltverein IT-Recht.

## Schnittstellen

- **datenschutzrecht** für DSGVO-Pflichten.
- **ki-governance** für KI-VO und AIA.
- **gewerblicher-rechtsschutz** bei Markenrecht IT-Branding.
- **vertragsrecht** bei SaaS-/Cloud-AGB-Prüfung.
- **kanzlei-allgemein** Fristen Versand.

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Welches IT-Rechtsgebiet ist primär einschlägig?
2. Liegt ein akuter Handlungsbedarf vor (Cyber-Vorfall, laufende Frist)?
3. Welche anderen Plugins sind einzubeziehen? (datenschutzrecht / ki-governance / fachanwalt-strafrecht)
4. Fachanwalt IT-Recht: FAO-Pflichtfächer (§ 14b FAO) alle abgedeckt?

## Output-Template — Orientierungs-Übersicht

**Adressat:** Mandant / Kanzlei intern — Tonfall: verständlich-erklärend

```
IT-Recht Orientierungs-Übersicht [DATUM]
Sachgebiet: [BEZEICHNUNG]
Primär einschlägig: [RECHTSGEBIET]
Sekundär: [QUERVERWEISE]

Wichtige Normen:
- [NORM] — [KURZBESCHREIBUNG]

Fristen im Blick:
- [FRIST] bis [DATUM] — [BEZEICHNUNG]

Anschlusskills: [LISTE WEITERFÜHRENDER SKILLS]
```

---

## Skill: `orientierung-sonderfall-edge-case`

_Orientierung: Sonderfall und Edge-Case-Prüfung: Orientierung: Sonderfall und Edge-Case-Prüfung._

# Orientierung: Sonderfall und Edge-Case-Prüfung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Sonderfall und Edge-Case-Prüfung.

## Spezialwissen: Orientierung: Sonderfall und Edge-Case-Prüfung
- **Normen-/Quellenanker:** DSGVO, BDSG, TTDSG, TKG, DDG, DSA, DMA, EU, KI, VO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für IT-, Datenschutz- und Telemedienrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespraechsleit..._

# Strukturierter Erstgespraechsleitfaden für IT-, Datenschutz- und Telemedienrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für IT-, Datenschutz- und Telemedienrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im IT-, Datenschutz- und Telemedienrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich IT-, Datenschutz- und Telemedienrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für IT-, Datenschutz- und Telemedienrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: DSGVO, IT-Vertrag, Cloud, KI-VO, NIS-2, TDDDG, Datenpanne
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Unterlassungsklage Datenschutz, Klage IT-Vertrag, DSGVO-Bussgeldwiderspruch). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich IT-, Datenschutz- und Telemedienrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft IT-, Datenschutz- und Telemedienrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- DSGVO, BDSG, TDDDG, KI-VO, NIS-2-RL, BGB-Werk-/Mietvertrag (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich IT-, Datenschutz- und Telemedienrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich IT-, Datenschutz- und Telemedienrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Hoehe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege moeglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Pruefroutinen.

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Liegt ein Cyber-Vorfall vor? (sofortige Eskalation → Skill cyber-incident-response-72h)
2. Interessenkollision nach § 43a Abs. 4 BRAO prüfen (bereits Gegenseite vertreten?)
3. Welche Fristen laufen? (72h Art. 33 DSGVO / 24h NIS-2 BSI / Schadensersatzverjährung §§ 195/199 BGB)
4. GwG-Check: Politisch exponierte Person / Hochrisiko-Land / anonyme Zahlung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Erstgespraech IT-Recht | Mandatsbogen-Protokoll; Template unten |
| Variante A — Mandant will nur Beratung ohne Mandat | Beratungsvertrag; kein Mandatsbogen erforderlich |
| Variante B — Eilsituation (Abmahnung / Datenpanne) | Sofortberatung; Fristen sichern bevor Vollmandat |
| Variante C — Unternehmens-Compliance-Check | Retainer-Modell statt Einzelmandat erwaegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Erstgespräch-Protokoll

**Adressat:** Kanzlei intern — Tonfall: sachlich-strukturiert

```
Erstgespräch-Protokoll IT-Mandat [DATUM, UHRZEIT]
Mandant: [NAME, ANSCHRIFT, ERREICHBARKEIT]
Berater: [ANWALT]
Aktenzeichen: [AZ]

Sachverhalt: [KURZBESCHREIBUNG]
Rechtsgebiet: IT-Vertragsrecht / DSGVO / NIS-2 / AI Act / DSA / DMA / [SONSTIGES]
Mandantenrolle: Auftraggeber / Auftragnehmer / Plattform / Nutzer / Betreiber

Fristenprognose:
- Kritische Frist: [DATUM] ([BEZEICHNUNG])
- Wiedervorlage: [DATUM]

Interessenkonflikt: nein (geprüft) / ja (Mandat abzulehnen)
GwG-Check: unauffällig / Prüfung erforderlich

Vollmacht erteilt: ja / ausstehend
Honorarvereinbarung: RVG / Stundensatz [BETRAG EUR/h] / Pauschal [BETRAG EUR]

Nächste Schritte: [LISTE]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** DSGVO, BDSG, TTDSG, TKG, DDG, DSA, DMA, EU, KI, VO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **IT-Recht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## IT-Recht-Erstprüfung: 6-Schritte-Diagnose
1. **Vertragstyp bestimmen:** Werkvertrag (§§ 631 ff. — individuell erstellte Software), Dienstvertrag (§§ 611 ff. — laufende Beratung), Kauf (§§ 433 ff. — Standardsoftware), Miete (§§ 535 ff. — SaaS/Cloud), Lizenz (UrhG, einfaches/ausschließliches Recht).
2. **Rolle:** Anbieter (Hersteller, Lizenzgeber, Cloud-Provider) vs. Kunde (Lizenznehmer, SaaS-Nutzer); B2B vs. B2C; je nach Rolle unterschiedliche AGB-Inhaltskontrolle (§§ 305 ff., 308, 309 BGB).
3. **Daten:** Personenbezogen → DSGVO; nicht-personenbezogen → Geschäftsgeheimnis (GeschGehG); öffentlich → Data Act / DGA.
4. **NIS2 / KritisV?** Wesentliche Einrichtung (Anhang I NIS2-RL) oder wichtige Einrichtung (Anhang II)? KRITIS-Schwellen § 8b BSIG, BSI-KritisV.
5. **Streitstand:** Vorklagephase (Mängelrüge, Nachfristsetzung), Mahnverfahren, Klage, Vergleichsverhandlung, ADR?
6. **Mandatsziel:** Vertrag verhandeln/redlinen? Mangel durchsetzen? Sich verteidigen? Vergleich vermitteln?

## Trade-off
Frühe gerichtliche Eskalation (Klage, einstweilige Verfügung) bringt schnelle Lösung, aber zerstört Geschäftsbeziehung — bei laufenden SaaS-Verhältnissen oft kontraproduktiv. Stufenweises Vorgehen Mängelrüge → Nachfrist → Kündigung/Schadensersatz erhält Beziehung und stärkt spätere Klage.

---

## Skill: `itr-einfuehrung-rechtsmaterien`

_IT-Recht einfuehrend: IT-Vertragsrecht (Beschaffung, Wartung, SLA), Datenschutz DSGVO/BDSG, IT-Sicherheit BSI-Gesetz und NIS2, Urheberrecht Software, AGB-Recht B2B/B2C, eCommerce: IT-Recht einfuehrend: IT-Vertragsrecht (Beschaffung, Wartung, SLA), Datenschu..._

# IT-Recht einfuehrend: IT-Vertragsrecht (Beschaffung, Wartung, SLA), Datenschutz DSGVO/BDSG, IT-Sicherheit BSI-Gesetz und NIS2, Urheberrecht Software, AGB-Recht B2B/B2C, eCommerce


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** IT-Recht einfuehrend: IT-Vertragsrecht (Beschaffung, Wartung, SLA), Datenschutz DSGVO/BDSG, IT-Sicherheit BSI-Gesetz und NIS2, Urheberrecht Software, AGB-Recht B2B/B2C, eCommerce. Entscheidungstabelle und Verweis auf Detail-Skills.

### IT-Recht: Materien

## Spezialwissen: IT-Recht: Materien
- **Normen-/Quellenanker:** IT, SLA, DSGVO, BDSG, BSI, AGB.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `itr-ki-systeme-vertragsklausel-leitfaden`

_Leitfaden Vertragsklauseln für KI-Systeme: Trainings- und Inferenzphase, Black-Box-Klausel, Halluzination, Outputrechte, Daten-Lizenz: Leitfaden Vertragsklauseln für KI-Systeme: Trainings- und Inferenzphase, Black-Box-Klausel, Halluzination, Outputrechte, D..._

# Leitfaden Vertragsklauseln für KI-Systeme: Trainings- und Inferenzphase, Black-Box-Klausel, Halluzination, Outputrechte, Daten-Lizenz


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Leitfaden Vertragsklauseln für KI-Systeme: Trainings- und Inferenzphase, Black-Box-Klausel, Halluzination, Outputrechte, Daten-Lizenz. Pruefraster für Customer und Vendor.

### IT: KI-Systeme Vertragsklausel

## Spezialwissen: IT: KI-Systeme Vertragsklausel
- **Normen-/Quellenanker:** KI, IT.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

