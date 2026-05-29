---
name: fachanwalt-it-recht-saas-vertrag-verhandlung
description: "SaaS-Vertragsverhandlung mit Datenschutz Verfuegbarkeit Vendor-Lock-in und Exit-Klausel. Anwendungsfall SaaS-Vertrag soll verhandelt oder geprüft werden und IT-rechtliche Pflicht-Klauseln muessen geprüft werden. Normen Art. 28 DSGVO AVV § 309 BGB AGB-Kontrolle §§ 327 ff. BGB Digitale Produkte EVB-IT. Prüfraster SLA Verfuegbarkeit Datenschutz-AVV Wartung Sicherheitsupdates Vendor-Lock-in Exit-Klausel Datenmigration Haftung Datenlokation Schrems-II SCC. Output Vertragsmark-up mit kommentierten Klauseln Verhandlungsprioritaeten und Datenschutz-Risikoeinschaetzung. Abgrenzung zu fachanwalt-it-recht-it-vertrag-verhandlung-eu-odr und softwarefehler-mangelhaftung-prüfen."
---

# SaaS-Vertrag — Prüfung und Verhandlung

## Kaltstart-Rückfragen

1. Wer ist Anbieter (Hyperscaler wie AWS/Azure/Google, Nischen-SaaS, deutscher Anbieter) und was ist der Service (CRM, ERP, HR-System, Kommunikationsplattform)?
2. Ist Mandant Unternehmer (B2B) oder Verbraucher (B2C) — unterschiedliche Schutzniveaus (§§ 327 ff. BGB bei B2C)?
3. Welches Vertragsvolumen — jährliches Abonnement oder Multi-Year-Deal? Ab ca. 50.000 EUR/Jahr ist Individualverhandlung realistisch.
4. Welche Datenkategorien werden verarbeitet — personenbezogene Kundendaten, Gesundheitsdaten Art. 9 DSGVO, Bankdaten, Geschäftsgeheimnisse?
5. Server-Standort — EU/EWR, USA, andere Drittstaaten? Begründung: DSGVO-Transferbeschränkungen Art. 46, Schrems-II-Folgen, CLOUD Act.
6. Wie lange Vertragslaufzeit und welche Kündigungsfristen? Automatische Verlängerung?
7. Gibt es Vendor-Lock-in-Risiken — proprietäres Datenformat, keine API-Export-Möglichkeit?
8. Welcher Ansprechpartner beim Anbieter für Vertragsverhandlung — Legal, Sales, Procurement?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Vertragstyp und Mängelregime

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§§ 327–327u BGB** (seit 01.01.2022) — Verträge über digitale Inhalte und Dienstleistungen im B2C: § 327e BGB Sachmangel, § 327f BGB Aktualisierungspflicht, § 327j BGB Verjährung 2 Jahre, § 327k BGB Beweislastumkehr 1 Jahr.
- **§§ 305–310 BGB** — AGB-Kontrolle: § 309 Nr. 7 BGB — keine Freizeichnung bei grober Fahrlässigkeit/Vorsatz; § 309 Nr. 5 BGB — angemessene Pauschalschadensersätze; § 308 Nr. 4 BGB — kein einseitiges Leistungsänderungsrecht ohne sachlichen Grund; § 309 Nr. 9 BGB — Laufzeit B2C max. 2 Jahre + monatliche Kündigung.

### Datenschutz

- **Art. 28 DSGVO** — Auftragsverarbeitungsvertrag (AVV): Pflichtinhalt (Abs. 3 lit. a–h), schriftlich oder elektronisch, Unterauftragsverarbeiter mit Genehmigung.
- **Art. 32 DSGVO** — TOMs: Verschlüsselung, Pseudonymisierung, Zutrittskontrolle, Wiederherstellung nach Notfall.
- **Art. 46 DSGVO** — Drittlandübertragung: Standardvertragsklauseln (SCC 2021), angemessener Schutz, BCR.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **EU-US Data Privacy Framework** (Commission Implementing Decision 2023/1795): gültiger Angemessenheitsbeschluss für zertifizierte US-Anbieter (Stand 2023).
- **US CLOUD Act** — US-Behörden können bei US-Anbietern weltweit gespeicherte Daten anfordern; souveräne Cloud prüfen.

### Sonstiges

- **§ 9 GeschGehG** — Schutz Geschäftsgeheimnisse bei Drittland-Hosting.
- **NIS2UmsuCG** — bei KRITIS-Einrichtungen Anforderungen an Dienstleister.
- **ISO/IEC 27001** — TOMs-Standard; BSI C5 (Cloud Computing Compliance Criteria Catalogue).

### Entscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema

| Nr. | Prüfpunkt | Norm | Kernfrage |
|---|---|---|---|
| 1 | AVV Art. 28 DSGVO | Art. 28 DSGVO | Vorhanden? Vollständiger Inhalt? Unterauftragsverarbeiter? |
| 2 | TOMs Art. 32 DSGVO | Art. 32 DSGVO | Verschlüsselung, Zugangskontrolle, Wiederherstellung? |
| 3 | Datenlokation + Drittlandtransfer | Art. 46 DSGVO | Server EU? US: SCC + TIA? EU-US DPF-Zertifizierung? |
| 4 | SLA-Verfügbarkeit | Parteiwahl | Prozentsatz? Definition Ausfall? Wartungsfenster? |
| 5 | SLA-Sanktionen | Parteiwahl | Service Credits? Kündigung bei dauerhafter Unterschreitung? |
| 6 | Wartung und Sicherheitsupdates | §§ 535, 327f BGB | Frequenz? Notfall-Patches? Vorankündigung? |
| 7 | Dateneigentum | Parteiwahl | Wer ist Eigentümer der Kundendaten? |
| 8 | Exit-Klausel / Datenmigration | Parteiwahl | Export-Format? Frist? Kosten? Interoperabilität? |
| 9 | Haftungsbeschränkung | §§ 309 Nr. 7, 309 Nr. 5 BGB | Deckel bei 12 Monaten? Vorsatz/grobe Fahrlässigkeit ausgenommen? |
| 10 | Laufzeit / Kündigung | §§ 314 BGB, 309 Nr. 9 BGB | Laufzeit, automatische Verlängerung, ordentliche / außerordentliche Kündigung? |
| 11 | Preisanpassungsklauseln | § 308 Nr. 4 BGB | Sachlicher Grund? Widerspruchsrecht? |
| 12 | Backup und Notfallwiederherstellung | Art. 32 DSGVO | RPO/RTO definiert? Backup-Frequenz? |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — SaaS-Vertrag verhandeln | Verhandlungs-Bausteine; Template unten |
| Variante A — Mandant ist Anbieter statt Nutzer | AGB-Pruefung auf Anbieterseite; andere Klausel-Prioritaeten |
| Variante B — Kritische Daten im SaaS | DSGVO-Auftragsverarbeitungsvertrag; BSI C5-Testat pruefen |
| Variante C — Kuendigung laufender SaaS-Vertrag | Exit-Strategie; Datenportabilitaet Art. 20 DSGVO |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### SLA-Klausel (Verhandlungsmuster B2B)

```
§ [X] Service Level Agreement

1. Verfuegbarkeit
   Der Anbieter sichert eine monatliche Systemverfuegbarkeit
   von mindestens 99,5 % (SaaS Standard) / 99,9 % (Premium)
   zu, gemessen am Netzwerkuebergabepunkt des Anbieters,
   ausschliesslich geplanter Wartungsfenster.

2. Wartungsfenster
   Geplante Wartungsarbeiten werden mindestens 48 Stunden
   im Voraus angekuendigt und in die Zeit Montag bis Freitag
   20:00–06:00 Uhr und Wochenende gelegt. Maximale Dauer:
   6 Stunden/Monat.

3. Definitionen
   "Ausfall" ist die vollstaendige Nichterreichbarkeit oder
   Nicht-Nutzbarkeit wesentlicher Kernfunktionen des Dienstes
   aus Gruenden, die nicht in der Sphaere des Kunden liegen.

4. Service Credits
   Bei Unterschreitung der Verfuegbarkeit erhalt der Kunde:
   - 99,0–99,5 %: 10 % der Monatspauschale
   - 98,0–99,0 %: 20 % der Monatspauschale
   - unter 98 %:  50 % der Monatspauschale als Gutschrift.
   Die Geltendmachung erfolgt mit Antrag binnen 30 Tagen.
   Service Credits schliessen weitergehende gesetzliche
   Ansprueche nicht aus.

5. Ausserordentliche Kuendigung
   Unterschreitet die tatsaechliche Verfuegbarkeit zwei
   aufeinanderfolgende Monate die garantierte Verfueg-
   barkeit um mehr als 2 Prozentpunkte, ist der Kunde
   berechtigt, den Vertrag ohne Frist zu kuendigen.
```

### Exit-Klausel / Datenmigration

```
§ [X] Datenexport und Beendigung

1. Daten des Kunden
   Alle vom Kunden eingegebenen, generierten oder
   hochgeladenen Daten ("Kundendaten") verbleiben im
   Eigentum des Kunden. Der Anbieter erwirbt kein
   Eigentum und kein dauerhaftes Nutzungsrecht.

2. Datenexport
   Waehrend der gesamten Vertragslaufzeit kann der Kunde
   jederzeit und ohne Mehrkosten alle Kundendaten in einem
   gaengigen Standardformat (CSV, JSON, XML oder
   branchenublichem Format) exportieren.

3. Nach Vertragsende
   Innerhalb von [60 / 90] Tagen nach Vertragsbeendigung
   haelt der Anbieter alle Kundendaten zum Abruf bereit.
   Nach Ablauf dieser Frist werden die Daten unwieder-
   bringlich geloescht; Loeschbestaetigung wird erteilt.

4. Migrations-Unterstuetzung
   Auf Wunsch des Kunden erbringt der Anbieter Migrations-
   unterstuetzung zu einem Pauschalpreis von EUR [X]
   (Datenexport in Zielformat + technische Dokumentation
   der Datenstruktur).

5. API-Zugang
   Dem Kunden steht waehrend der Vertragslaufzeit eine
   dokumentierte REST-API zur Datenabfrage und zum
   Datenexport zur Verfuegung.
```

### AVV-Kurzcheck

```
Pflicht-Inhalte AVV Art. 28 Abs. 3 DSGVO — Checkliste

[X] Gegenstand, Dauer, Art und Zweck der Verarbeitung?
[X] Art der personenbezogenen Daten; Kategorien Betroffener?
[X] Verarbeitung nur auf dokumentierte Weisung des Verantwortlichen?
[X] Vertraulichkeit der zur Verarbeitung befugten Personen?
[X] TOMs Art. 32 DSGVO implementiert?
[X] Unterauftragsverarbeiter-Regelung (Genehmigung, Weitergabe Art. 28 Pflichten)?
[X] Drittlandtransfer: SCC oder Angemessenheitsbeschluss vorhanden?
[X] Betroffenenrechte-Unterstuetzung (Auskunft, Loeschung, Berichtigung)?
[X] Sicherheitsvorfallmeldung an Verantwortlichen unverzueglich?
[X] Nachweispflicht TOMs (Audits, Zertifikate)?
[X] Loeschung / Rueckgabe bei Vertragsende?
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast und Darlegungslast

| Frage | Last | Norm |
|---|---|---|
| SLA-Unterschreitung | Kunde — Dokumentation Ausfallzeiten | Parteiwahl; § 536 BGB |
| AGB-Unwirksamkeit | Gericht von Amts wegen; Anregung durch Kunden | § 306 BGB |
| DSGVO-Verletzung AVV | Verantwortlicher — Rechenschaftspflicht | Art. 5 Abs. 2 DSGVO |
| TIA-Bewertung Drittlandtransfer | Verantwortlicher | Schrems II; Guidance DSK |
| Vertragsverletzung Anbieter | Kunde | allg. Beweislastregeln |

## Fristen und Verjährung

| Frist | Dauer | Norm |
|---|---|---|
| Mietminderung (SaaS) | Ohne Fristerfordernis; sofortige Minderung § 536 BGB | § 536 BGB |
| Verjährung Schadensersatz | 3 Jahre §§ 195, 199 BGB | §§ 195, 199 BGB |
| Verjährung Mietmängel B2C | 2 Jahre § 327j BGB | § 327j BGB |
| Widerruf B2C-Vertrag | 14 Tage ab Vertragsschluss § 355 BGB | §§ 355, 312g BGB |
| Kündigung bei SLA-Dauerverletzung | Unverzüglich nach Eintritt Kündigungsgrund | § 543 BGB i. V. m. § 314 BGB |
| Rüge Service-Credit-Antrag | Vertraglich typisch 30 Tage | Parteiwahl |

## Typische Vertragsrisiken und Reaktion

| Risiko | Reaktion |
|---|---|
| AVV fehlt vollständig | Eigenständige Datenschutzverletzung; DSGVO-Meldepflicht prüfen; AVV sofort nachfordern |
| Server außerhalb EU ohne SCC | SCC 2021 (Moduldaten) + TIA beifügen; alternativ EU-Cloud-Anbieter |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Preisanpassungsrecht einseitig | § 308 Nr. 4 BGB — unwirksam ohne sachlichen Grund und Widerspruchsrecht |
| Datenmigration nach Kündigung nur gegen Aufpreis | Verhandeln: kostenloses 90-Tage-Exportfenster als Standard |
| US-Anbieter ohne DPF-Zertifizierung | Selbst TIA-Bewertung + SCC; alternativ: Anbieter ohne US-Nexus |

## Streitwert und Kosten

- Vertragsvolumen als Streitwert bei Rücktritt oder Schadensersatz (§ 3 ZPO).
- Schadensersatz SaaS-Ausfall: entgangener Gewinn + Mehraufwand; nachzuweisen.
- DSGVO-Bußgeld fehlender AVV: bis 10 Mio. EUR oder 2 % Jahresumsatz.
- Anwaltshonorar Vertragsverhandlung: Zeithonorar 200–400 EUR/h; 3–8 Stunden pro Vertrag typisch.
- RVG: bei Klage auf SLA-Credits Streitwert = Jahresmietentgelt; Gebühren nach GKG.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Erstprüfung Standard-AGB | AVV, SLA, Exit-Klausel, Haftung als Prioritätspunkte; AGB-Mängelprotokoll erstellen |
| Vertragsvolumen < 20.000 EUR/Jahr | Standardkonditionen mit minimalen Anpassungen; AVV immer eigenständig |
| Vertragsvolumen > 100.000 EUR/Jahr | Vollständige Individualverhandlung; eigene Vertragsmuster einbringen |
| Kündigung wegen SLA-Unterschreitung | § 543 BGB bei erheblichem Mangel; Dokumentation aller Ausfälle + Rügeschreiben |
| KRITIS-Einrichtung | BSI C5-Zertifizierung des Anbieters verlangen; NIS2-Anforderungen in AVV |

## Anschluss-Skills

- `cyber-incident-response-72h` — bei Datenpanne beim SaaS-Anbieter
- `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` — Incident Response
- `softwarefehler-mangelhaftung-pruefen` — bei technischen Mängeln

## Quellen

- BGB §§ 305–310, 327–327u, 535–548
- DSGVO Art. 28, 32, 46, 83
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Commission Implementing Decision 2023/1795 (EU-US DPF)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BSI C5 Anforderungskatalog Cloud Computing
- ISO/IEC 27001

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
