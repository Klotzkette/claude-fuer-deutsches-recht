---
name: cyber-incident-response-72h
description: "Sofortmassnahmen bei aktivem Cyber-Vorfall Ransomware Datenexfiltration oder Insider-Threat. Anwendungsfall Cyberangriff ist entdeckt und IT-rechtliche Meldepflichten sowie Beweissicherung muessen binnen Stunden eingeleitet werden. Normen Art. 33 DSGVO 72-Stunden-Meldung Datenpanne Art. 34 DSGVO Betroffeneninformation NIS2UmsuCG § 32 BSIG n.F. §§ 202a 303b StGB. Pruefraster Sofort-Eindaemmung Forensik-Sicherung DSGVO-Meldepflicht NIS-2-Fruehwarnung 24 Stunden Strafanzeige Cybersecurity-Versicherer Beweiskette. Output Sofortmassnahmen-Protokoll mit 72-Stunden-Plan Meldungsformulierung und Chain-of-Custody-Dokumentation. Abgrenzung zu fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen und fachanwalt-it-recht-datenschutz-folgenabschaetzung."
---

# Cyber-Incident-Response 72 Stunden

## Kaltstart-Rückfragen

1. Art des Vorfalls — Ransomware (Bildschirmsperre, Erpressungsmail), Datenleck (Exfiltration nach extern), DDoS (Nichterreichbarkeit), Insider-Threat (Mitarbeiter-Exfiltration)?
2. Wann wurde der Vorfall entdeckt — seit wann läuft er vermutlich (Angriffszeitpunkt vs. Entdeckungszeitpunkt)?
3. Welche Systeme und Datenkategorien sind betroffen — personenbezogene Daten (Kunden, Mitarbeiter, Patienten), Geschäftsgeheimnisse, Infrastruktur?
4. Ist Mandant KRITIS-Betreiber oder fällt unter NIS2UmsuCG (§ 28 BSIG n. F. wichtige oder besonders wichtige Einrichtung)?
5. Besteht eine Cyber-Versicherung — Deckungsumfang, Notfallhotline des Versicherers bekannt?
6. Wurden bereits Maßnahmen ergriffen — Systeme abgeschaltet (Forensik-Problem!), Passwörter geändert, Backups überprüft?
7. Liegt eine Erpressungsforderung vor — Betrag, Zahlungsanweisung, Frist?
8. Ist eine betroffene Begleitperson oder Datenschutzbeauftragter vorhanden?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Datenschutz

- **Art. 33 DSGVO** — Meldepflicht bei Verletzung des Schutzes personenbezogener Daten: binnen 72 Stunden nach Kenntnis an zuständige Aufsichtsbehörde.
- **Art. 34 DSGVO** — Benachrichtigung Betroffener unverzüglich bei voraussichtlich hohem Risiko.
- **Art. 32 DSGVO** — Pflicht zu technischen und organisatorischen Maßnahmen; bei Verstoß Mitursache für Haftung.
- **Art. 82 DSGVO** — Schadensersatz Betroffener; Verantwortlicher haftet für Schäden aus Verletzung.
- **Bußgeldrahmen Art. 83 Abs. 4 DSGVO** — Verstoß gegen Art. 32: bis 10 Mio. EUR oder 2 % Jahresumsatz; Verstoß gegen Art. 33/34: bis 10 Mio. EUR oder 2 % Jahresumsatz.

### NIS2 / BSIG

- **NIS2UmsuCG** (in Kraft seit 06.12.2025) — umsetzt NIS-2-Richtlinie (EU) 2022/2555.
- **§ 32 BSIG n. F.** — Meldepflichten erheblicher Sicherheitsvorfälle für wichtige und besonders wichtige Einrichtungen.
- **§ 65 BSIG n. F.** — Bußgeld bis 10 Mio. EUR oder 2 % weltweiten Jahresumsatzes bei wichtigen Einrichtungen; bis 20 Mio. EUR oder 4 % bei besonders wichtigen.
- Adressat: BSI (Bundesamt für Sicherheit in der Informationstechnik) über IT-Sicherheitsportal.

### Strafrecht

- **§ 202a StGB** — Ausspähen von Daten (Freiheitsstrafe bis 3 Jahre).
- **§ 202b StGB** — Abfangen von Daten.
- **§ 202c StGB** — Vorbereiten des Ausspähens (Hacker-Tools).
- **§ 202d StGB** — Datenhehlerei.
- **§ 263a StGB** — Computerbetrug.
- **§ 303a StGB** — Datenveränderung; Qualifikation § 303b StGB Computersabotage (bis 5 Jahre).
- **§ 269 StGB** — Fälschung beweiserheblicher Daten.
- **§ 261 StGB** — Geldwäsche: Lösegeld kann bei sanktionierten Tätergruppen (Russland/Iran/NK) Sanktionsrecht verletzen.

### Sektorales Recht

- **§ 75c SGB V** — Krankenhäuser mit Pflicht zu IT-Sicherheit nach BSI-Standard.
- **BSI-KritisV** — Kritische Infrastrukturen (Energie, Wasser, Gesundheit, Finanzen, Transport).
- **§ 8a BSIG a. F. / § 30 BSIG n. F.** — Sicherheitsanforderungen KRITIS.

### Entscheidungen

- EuGH, Urt. v. 14.12.2023 — C-340/21 (Natsionalna agentsia): Art. 82 DSGVO — allein die unbefugte Offenlegung begründet Schadensersatzanspruch; kein Nachweis konkreten Schadens für immateriellen Schaden erforderlich.
- EuGH, Urt. v. 14.12.2023 — C-340/21 (Natsionalna agentsia za prihodite), NJW 2024, 1091: Immaterieller DSGVO-Schadensersatz nach Art. 82 Abs. 1 setzt Schaden + Kausalitaet + DSGVO-Verstoss kumulativ voraus; keine Bagatellgrenze; bereits begruendete Sorge vor Datenmissbrauch kann ersatzfaehig sein; Verantwortlicher muss Geeignetheit der TOMs nach Art. 32 DSGVO darlegen.
- OLG Dresden, Urt. v. 30.11.2021 — 4 U 1158/21: Schadensersatzpflicht bei mangelnden TOMs Art. 32 DSGVO.
- LG München I, Urt. v. 09.12.2021 — 31 O 16606/20: Datenpanne + mangelnde Sicherheit = Schadensersatz.

## Prüfschema / Zeitplan

| Zeit | Prüfschritt | Norm | Aktion |
|---|---|---|---|
| Stunde 0 | Vorfallbestätigung | intern | Krisenstab einberufen; Forensik bestellen |
| Stunde 1 | Eindämmung | Art. 32 DSGVO | Netzwerktrennung (kein Abschalten!); RAM-Dump; Log-Sicherung |
| Stunde 2-4 | Forensik-Auftrag | Art. 28 DSGVO | AVV mit Forensik-Dienstleister; Chain-of-Custody beginnt |
| Stunde 4-8 | Personenbezug prüfen | Art. 33 DSGVO | Welche Datenkategorien? Wie viele Betroffene? |
| Stunde 8-12 | DSGVO-Meldepflicht bewerten | Art. 33 DSGVO | Verletzung des Schutzes personenbezogener Daten? Risiko? |
| Stunde 12 | NIS2-Prüfung | § 32 BSIG n. F. | KRITIS / NIS2-Einrichtung? 24-Stunden-Frühwarnung? |
| Stunde 24 | NIS2-Frühwarnung | § 32 BSIG n. F. | Meldung BSI wenn NIS2 anwendbar |
| Stunde 48 | DSGVO-Meldung vorbereiten | Art. 33 DSGVO | Entwurf + Abstimmung |
| Stunde 72 | DSGVO-Meldung einreichen | Art. 33 DSGVO | Aufsichtsbehörde online; NIS2-Vorfallsmeldung BSI |
| Tag 4-7 | Betroffene informieren | Art. 34 DSGVO | Wenn hohes Risiko: unverzüglich |
| Tag 4-7 | Strafanzeige | §§ 202a 303b StGB | LKA Cybercrime; Forensik-Bericht beifügen |
| Tag 4-14 | Versicherer-Antrag | Cyber-Police | Unterlagen; Selbstbehalt; Forensik |
| Monat 1 | NIS2-Abschlussbericht | § 32 BSIG n. F. | Ursachenanalyse; Maßnahmen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Cyber-Incident 72h DSGVO-Meldung | Incident-Response-Protokoll; Template unten |
| Variante A — Kein meldepflichtiger Vorfall | Interne Dokumentation ohne Meldung; Template vereinfacht |
| Variante B — Kritische Infrastruktur betroffen | BSI-Meldepflicht § 8b BSIG zusaetzlich zur DSGVO-Meldung |
| Variante C — Strafanzeige erwaegen | § 202a ff. StGB; parallel zu Aufsichtsbehoerde informieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### DSGVO-Meldung Art. 33 (Vorlage)

```
An: [Zustaendige Datenschutz-Aufsichtsbehoerde]
Betreff: Meldung einer Verletzung des Schutzes personenbezogener
Daten gemaess Art. 33 DSGVO

Verantwortlicher: [Name, Anschrift, Datenschutzbeauftragter]
Datum/Uhrzeit Kenntnis: [...]
Meldenummer (falls Folgemeldung): [...]

A) Art der Verletzung
[Vertraulichkeitsverletzung / Integritaetsverletzung /
Verfuegbarkeitsverletzung] durch [Ransomware-Angriff / externen
Angreifer / Datenleck / Insider]

B) Betroffene Kategorien und Anzahl
Betroffene Personen: ca. [Anzahl] ([Kunden / Mitarbeiter /
Patienten])
Datenkategorien: [Name, Adresse, Kontonummer, Gesundheitsdaten,
besondere Kategorien Art. 9 DSGVO?]

C) Wahrscheinliche Folgen
[Identitaetsdiebstahl / Phishing / Reputationsschaden /
Diskriminierung]

D) Ergriffene Massnahmen
- [Netztrennung am Datum Uhrzeit]
- [Forensik beauftragt am Datum]
- [Passwortzuruecksetzung]
- [Backup-Wiederherstellung im Gange]

E) Kontakt
Datenschutzbeauftragter: [Name, Tel, E-Mail]

Hinweis: Diese Meldung erfolgt nach bestem aktuellem
Kenntnisstand. Wir behalten uns Nachreichung weiterer
Informationen gemaess Art. 33 Abs. 4 DSGVO vor.

[Unterschrift, Datum]
```

### Forensik-Auftrag mit AVV-Klausel (Kurzform)

```
Auftrag zur digitalen Forensik und AVV gemaess Art. 28 DSGVO

Verantwortlicher: [Unternehmen]
Auftragsverarbeiter: [Forensik-Dienstleister]

1. Gegenstand: Sicherung und Analyse digitaler Beweismittel
   im Zusammenhang mit Sicherheitsvorfall vom [Datum].

2. Weisungsgebundenheit: Dienstleister handelt ausschliesslich
   nach Weisung des Verantwortlichen.

3. Vertraulichkeit: Alle im Rahmen des Auftrags erlangten
   Informationen sind streng vertraulich zu behandeln.

4. Technische und organisatorische Massnahmen: Dienstleister
   wendet mindestons die in Anlage 1 beschriebenen TOMs an.

5. Sub-Verarbeiter: Nur mit vorheriger schriftlicher Zustimmung.

6. Rueckgabe/Loeschung: Nach Abschluss des Auftrags werden
   alle personenbezogenen Daten unverzueglich zurueckgegeben
   oder geloescht, soweit keine gesetzliche Aufbewahrungspflicht
   entgegensteht.

7. Chain of Custody: Alle Beweismittel werden mit Hash-Werten
   gesichert und lueckenlos protokolliert.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast und Darlegungslast

| Frage | Last | Norm |
|---|---|---|
| Verletzung der Meldepflicht Art. 33 | Behörde; Entlastung durch Dokumentation des Verantwortlichen | Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht) |
| Kausalität Schaden — Datenpanne | Betroffener für tatsächliche Schäden; immateriell schon bei festgestelltem Verstoß (EuGH C-340/21) | Art. 82 Abs. 1 DSGVO |
| Entlastung Verantwortlicher | Verantwortlicher: Nachweis angemessener TOMs | Art. 82 Abs. 3 DSGVO |
| Straftat § 202a StGB | Staatsanwaltschaft | StPO |
| Versicherungsschutz | Versicherungsnehmer | AVB Cyber-Police |

## Fristen und Verjährung

| Pflicht | Frist | Norm |
|---|---|---|
| DSGVO-Meldung Aufsichtsbehörde | 72 Stunden ab Kenntnis | Art. 33 Abs. 1 DSGVO |
| Betroffenen-Benachrichtigung | Unverzüglich (kein Zahlenwert) | Art. 34 Abs. 1 DSGVO |
| NIS2-Frühwarnung (Verdacht) | 24 Stunden ab Kenntnis | § 32 Abs. 1 BSIG n. F. |
| NIS2-Vorfallsmeldung | 72 Stunden ab Kenntnis | § 32 Abs. 2 BSIG n. F. |
| NIS2-Abschlussbericht | 1 Monat ab Vorfallsmeldung | § 32 Abs. 3 BSIG n. F. |
| Versicherer-Anzeige | Vertraglich 24–48 Stunden | AVB Cyber |
| DSGVO-Schadensersatz Verjährung | 3 Jahre § 195 BGB ab Kenntnis | §§ 195, 199 BGB |
| Strafanzeige § 202a StGB | Keine Frist; Strafverfolgungsverjährung 5 Jahre | § 78 StGB |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Keine Datenpanne — nur Systemausfall | Verfügbarkeitsverletzung ist Datenpanne wenn personenbezogene Daten betroffen; Art. 4 Nr. 12 DSGVO prüfen |
| 72-Stunden-Frist nicht bekannt | Unkenntnis schützt nicht; Bußgeldtatbestand Art. 83 Abs. 4 DSGVO; sofortige Nachmeldung reduziert Bußgeld |
| Lösegeld zahlen — alternativlos | Sanktionsprüfung (Russland-Gruppen auf OFAC-Liste); BSI rät ab; Versicherer-Konditionen prüfen; keine Garantie der Entschlüsselung |
| Forensik-Beauftragung zu teuer | Ohne Forensik keine Beweissicherung für Strafanzeige, Versicherung, Haftungsabwehr |
| KRITIS-Pflichten unbekannt | § 28 BSIG n. F. — Selbsteinstufung Pflicht; Nichtmeldung = Bußgeld bis 20 Mio. EUR |

## Streitwert und Kosten

- DSGVO-Bußgeld Aufsichtsbehörde: bis 10 Mio. EUR oder 2 % weltweiter Jahresumsatz (Art. 83 Abs. 4 DSGVO); schwere Verstöße Art. 83 Abs. 5: bis 20 Mio. EUR / 4 %.
- NIS2-Bußgeld besonders wichtige Einrichtungen: bis 20 Mio. EUR oder 4 % Jahresumsatz (§ 65 BSIG n. F.).
- Schadensersatz Betroffener Art. 82 DSGVO: immateriell 500–5.000 EUR pro Person (Tendenz steigend); bei Datenmassen Sammelklagen.
- Forensik-Kosten: 10.000–150.000 EUR je nach Umfang.
- Cyber-Versicherungsprämie: 0,3–1,5 % der versicherten Summe jährlich.
- Anwaltshonorar Krisen-Mandant: Zeithonorar 250–500 EUR/h; Streitwert-RVG für behördliche Verfahren nach GKG.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Ransomware — Systeme noch aktiv | Netzwerktrennung sofort; kein Abschalten; Forensik-Dienstleister binnen 2 Stunden |
| Personenbezogene Daten betroffen | 72-Stunden-Meldung einplanen; bei Zweifel melden (Bußgeld für Nicht-Meldung höher) |
| KRITIS / NIS2-Einrichtung | 24-Stunden-Frühwarnung BSI; paralleler DSGVO-Countdown |
| Lösegeld-Forderung | Sanktionsprüfung; Versicherer einbinden; BSI und LKA Cybercrime informieren |
| Betroffene Massenkommunikation | Datenschutzbeauftragter + Kommunikationsabteilung + Anwalt; Pressemitteilung koordiniert |

## Anschluss-Skills

- `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` — ergänzende Sofortmaßnahmen
- `fachanwalt-it-recht-saas-vertrag-verhandlung` — AVV-Prüfung bei Cloud-Diensten
- `fachanwalt-strafrecht-zeugenbeistand` — bei Mitarbeiterbefragungen im Unternehmen
- `datenschutzrecht-datenpanne-meldung` — für behördliches Verfahren

## Quellen

- DSGVO Art. 28, 32–34, 82, 83
- NIS2UmsuCG in Kraft seit 06.12.2025; §§ 32, 65 BSIG n. F.
- StGB §§ 202a–202d, 261, 263a, 269, 303a, 303b
- EuGH C-340/21 (Natsionalna agentsia)

- BSI IT-Grundschutz-Kompendium
- BSI-Lageberichte Cybersicherheit

## Aktuelle Rechtsprechung (v14.2)
- BGH, Urt. v. 26.01.2023 — III ZR 9/22, NJW 2023, 1085 Rn. 28: Ransomware-Schaden und Betreiberhaftung — Unternehmen haftet Betroffenen nach Art. 82 DSGVO wenn fehlende TOMs Art. 32 DSGVO kausal fuer Datenverlust; Entlastungsnachweis liegt beim Verantwortlichen.

## Output-Template — DSGVO-Meldung Art. 33
**Adressat:** Zustaendige Datenschutz-Aufsichtsbehoerde — Tonfall: sachlich-berichtend
```
AN: [DATENSCHUTZBEHOERDE ZUSTAENDIG — z.B. LDA Bayern / BfDI]
VON: [NAME VERANTWORTLICHER], Datenschutzbeauftragter: [NAME DSB]
BETREFF: Meldung Datenpanne Art. 33 DSGVO — [AKTENZEICHEN INTERN]
DATUM/UHRZEIT DER MELDUNG: [DATUM UHRZEIT]

[NAME MANDANT] ./. [AKTENZEICHEN]

A) Art der Verletzung
[Vertraulichkeits- / Integritaets- / Verfuegbarkeitsverletzung]
durch [Ransomware / Datenleck / unberechtigten Zugriff]
am [DATUM ANGRIFF] — entdeckt am [DATUM ENTDECKUNG UHRZEIT].

B) Betroffene Kategorien und Umfang
Personen: ca. [ANZAHL] ([KATEGORIE: Kunden / Mitarbeiter / Patienten])
Datenkategorien: [NAME, ADRESSE, GESUNDHEITSDATEN, BANKDATEN, ...]
Besondere Kategorien Art. 9 DSGVO: [Ja/Nein]

C) Wahrscheinliche Folgen
[IDENTITAETSDIEBSTAHL / PHISHING / DISKRIMINIERUNG / ...]

D) Ergriffene Massnahmen
1. Netztrennung: [DATUM UHRZEIT]
2. Forensik beauftragt: [DIENSTLEISTER, DATUM]
3. Passwortzuruecksetzung: [DATUM]
4. BSI-Meldung NIS-2 (falls relevant): [DATUM]

E) Kontakt
[NAME DSB], Tel: [TEL], E-Mail: [EMAIL]

Hinweis gemaess Art. 33 Abs. 4 DSGVO: Nachmeldung vorbehalten.

[KANZLEI / UNTERNEHMEN], [DATUM]
```
