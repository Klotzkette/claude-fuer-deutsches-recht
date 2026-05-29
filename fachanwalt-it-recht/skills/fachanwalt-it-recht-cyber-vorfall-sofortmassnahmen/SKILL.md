---
name: fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen
description: "Cyber-Vorfall-Sofortmassnahmen Ransomware Datenleck Hack. Meldepflichten 72 Stunden Art. 33 DSGVO BSIG NIS2UmsuCG kritische Infrastruktur. Forensik Beweissicherung Chain-of-Custody Behoerden Cybercrime. Krisenkommunikation Betroffene Aufsicht Versicherer. Workflow Tag 1 Tag 2-7 Folgewochen. Strafanzeige §§ 202a 303b StGB Sanktionsprüfung Lösegeldzahlung."
---

# Cyber-Vorfall-Sofortmaßnahmen

## Kaltstart-Rückfragen

1. Art des Vorfalls — Ransomware (Bildschirmsperre, Erpressungsmail), Datenleck (Exfiltration personenbezogener oder geschäftlicher Daten), DDoS (Nichterreichbarkeit), kompromittierter Mitarbeiter-Account, Insider-Threat?
2. Seit wann läuft der Vorfall — Zeitpunkt des Angriffs vs. Zeitpunkt der Entdeckung; Zeitdifferenz für DSGVO-72h-Frist relevant.
3. Welche Datenkategorien betroffen — personenbezogene Daten (Kunden, Mitarbeiter, Patienten), Gesundheitsdaten Art. 9 DSGVO (erhöhter Schutz), Geschäftsgeheimnisse, KRITIS-Steuerungsdaten?
4. Fällt Mandant unter NIS2UmsuCG — wichtige (§ 28 Abs. 2) oder besonders wichtige Einrichtung (§ 28 Abs. 1 BSIG n. F.)?
5. Cyber-Versicherung vorhanden — Policennummer, Notfallhotline des Versicherers?
6. Liegt eine Erpressungsforderung vor — Betrag, Kryptowährung, Zahlungsfrist, TOR-Kontaktadresse?
7. Wurden bereits eigene Maßnahmen ergriffen (Abschaltung — problematisch für Forensik; Passwortzurücksetzung)?
8. Ist Datenschutzbeauftragter involviert — wurde er bereits informiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### DSGVO

- **Art. 33 DSGVO** — Meldung Aufsichtsbehörde binnen 72 Stunden nach Kenntnis; Inhalt: Art, Betroffene, Datenkategorien, wahrscheinliche Folgen, ergriffene Maßnahmen; vorläufige Meldung zulässig mit Nachreichung.
- **Art. 34 DSGVO** — Benachrichtigung Betroffener unverzüglich bei voraussichtlich hohem Risiko; Inhalt: Beschreibung Vorfall, Empfehlungen Selbstschutz.
- **Art. 32 DSGVO** — TOMs; Verletzung als Mitursache für Haftung Art. 82 DSGVO.
- **Art. 83 Abs. 4 DSGVO** — Bußgeld bei Verletzung Art. 32–34: bis 10 Mio. EUR oder 2 % weltweiten Jahresumsatzes.

### BSIG / NIS2

- **§ 32 BSIG n. F. (NIS2UmsuCG)** — erhebliche Sicherheitsvorfälle: Frühwarnung 24 Stunden, Vorfallsmeldung 72 Stunden, Abschlussbericht 1 Monat.
- **§ 28 BSIG n. F.** — besonders wichtige und wichtige Einrichtungen: 18 Sektoren (Energie, Verkehr, Banken, Finanzmarktinfrastruktur, Gesundheit, Trinkwasser, Abwasser, digitale Infrastruktur, öffentliche Verwaltung u. a.).
- **§ 65 BSIG n. F.** — Bußgeld wichtige Einrichtungen bis 10 Mio. EUR oder 2 %; besonders wichtige bis 20 Mio. EUR oder 4 %.

### Strafrecht

- **§ 202a StGB** — Ausspähen von Daten; bis 3 Jahre Freiheitsstrafe.
- **§ 202b StGB** — Abfangen von Daten.
- **§ 303a StGB** — Datenveränderung; **§ 303b StGB** — Computersabotage (qualifizierter Fall): bis 5 Jahre.
- **§ 261 StGB** — Geldwäsche: Lösegeld bei sanktionierten Tätergruppen (Russland, Iran, Nordkorea) = Sanktionsrecht § 18 AWG.

### Sonstiges

- **§ 87 BetrVG** — Mitbestimmung Betriebsrat bei IT-Überwachungsmaßnahmen.
- **§ 9 GeschGehG** — Sicherung von Geschäftsgeheimnissen bei Exfiltration.
- **§ 43 GwG** — FIU-Meldung bei Geldwäscheverdacht durch Lösegeld.

## Prüfschema / Zeitplan

| Zeit | Prüfschritt | Aktion | Norm |
|---|---|---|---|
| Stunde 0–1 | Erstkontakt + Bestätigung | Krisenstab einberufen; Mandant: Systeme NICHT abschalten | intern |
| Stunde 1–2 | Netzwerktrennung | Switch-Port deaktivieren; RAM-Dump; Log-Sicherung | Art. 32 DSGVO |
| Stunde 2–4 | Forensik beauftragen | AVV Art. 28 DSGVO; Chain-of-Custody beginnen | Art. 28 DSGVO |
| Stunde 4–8 | Betroffenheit personenbezogener Daten? | Datenkategorien + Anzahl Betroffener ermitteln | Art. 33 DSGVO |
| Stunde 8–12 | NIS2-Prüfung | Einrichtungsklassifikation; 24h-Frist läuft | § 32 BSIG n. F. |
| Stunde 12–24 | Frühwarnung BSI (NIS2) | Wenn anwendbar: BSI-Meldung über IT-Sicherheitsportal | § 32 Abs. 1 BSIG n. F. |
| Stunde 24–48 | DSGVO-Meldung vorbereiten | Entwurf Art. 33; Abstimmung DSB; Aufsichtsbehörde | Art. 33 DSGVO |
| Stunde 72 | DSGVO-Meldung einreichen | Online-Portal Aufsichtsbehörde; NIS2-Vorfallsmeldung BSI | Art. 33 DSGVO; § 32 BSIG n. F. |
| Tag 4–7 | Betroffene informieren | Bei hohem Risiko Art. 34 DSGVO; Massenmailing vorbereiten | Art. 34 DSGVO |
| Tag 4–7 | Strafanzeige | LKA Cybercrime; Forensik-Zwischenbericht beifügen | §§ 202a, 303b StGB |
| Tag 4–7 | Versicherer-Antrag | Cyber-Police; Unterlagen vollständig | AVB Cyber |
| Woche 2–4 | Forensik-Endbericht | Ursachenanalyse; Schwachstellen; Maßnahmenplan | intern |
| Monat 1 | NIS2-Abschlussbericht | BSI; vollständige Analyse | § 32 Abs. 3 BSIG n. F. |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Cyber-Vorfall IT-Recht Sofortmassnahmen | Sofortmassnahmen-Checkliste; Template unten |
| Variante A — Ransomware; kein Backup | Loesegeld-Zahlung vs. Strafbarkeitsrisiko abwaegen; BKA informieren |
| Variante B — Insider-Threat | Arbeitsrechtliche Massnahmen parallel; HR einbeziehen |
| Variante C — Supply-Chain-Angriff | Lieferantenvertrag pruefen; Regress gegen Dienstleister |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Notruf-Checkliste (Mandant)

```
Sofortmassnahmen Cyber-Vorfall — erste 2 Stunden

1. Krisenteam informieren:
   - IT-Leitung: [...]
   - Datenschutzbeauftragter: [...]
   - Geschaeftsfuehrung: [...]
   - Anwalt: [...]
   - Forensik-Dienstleister: [...]

2. Systeme NICHT abschalten — nur Netzwerk trennen:
   - Switch-Port deaktivieren (IT)
   - WLAN abschalten
   - VPN-Zugaenge sperren

3. Keine Loesegeld-Zahlung ohne Anwaltsruecksprache.

4. Keine externe Kommunikation ohne Freigabe.

5. Logdateien sichern (Kopie, unveraendert).

6. Erpressungsmail/Erpressungsnachweis sichern (Screenshot + Original).
```

### DSGVO-Meldung Art. 33 (Muster)

```
An: [Landesdatenschutzbehoerde]
Betreff: Meldung Verletzung Schutz personenbezogener Daten
         gemaess Art. 33 DSGVO

Verantwortlicher: [Unternehmen, Anschrift, DSB, Kontakt]
Datum/Uhrzeit Kenntnis: [TT.MM.JJJJ HH:MM]
Vorlaeufige Meldung: [ja / nein]

A) Art der Verletzung
Ransomware-Angriff / Datenleck / Unbefugter Zugriff durch Dritten.
Art der Verletzung: Vertraulichkeit [X] Integrität [X] Verfügbarkeit [X]

B) Betroffene Kategorien und Anzahl
Personenkategorien: Kunden / Mitarbeiter / Patienten
Datenkategorien: Name, Adresse, [ggf. Art. 9 DSGVO-Daten]
Anzahl Betroffene: ca. [Zahl] (Schaetzung; wird praezisiert)

C) Wahrscheinliche Folgen
Identitaetsdiebstahl / Phishing / Beruflicher Schaden / keine
schwerwiegenden Folgen erkennbar [Begruendung]

D) Ergriffene und geplante Massnahmen
- Netztrennung am [TT.MM. HH:MM]
- Forensik beauftragt am [Datum]
- Passwortzuruecksetzung [Datum]
- Benachrichtigung Betroffene geplant ab [Datum]

E) Kontakt fuer Rueckfragen
DSB: [Name, Tel, E-Mail]

[Ort, Datum, Unterschrift]
```

### Strafanzeige (Skeleton)

```
An: Zentralstelle Cybercrime [Generalstaatsanwaltschaft Ort]
   
Strafanzeige gemaess § 158 StPO

Anzeigeerstatter: [Unternehmen, vertreten durch Anwalt]
Beschuldigter: Unbekannte Person(en)

Tatzeit: [Datum oder Zeitraum]
Tatort: Computersystem des Anzeigers, Server-Standort [Ort]

Sachverhalt:
Am [Datum] stellte der Anzeigeerstatter fest, dass seine IT-
Infrastruktur durch eine Ransomware-Schadsoftware kompromittiert
wurde. [Detailbeschreibung]

Straftatbestaende:
- § 202a StGB: Unbefugtes Ausspaehn der Daten
- § 303b StGB: Computersabotage durch Ransomware-Einsatz
- § 253 StGB: Erpressung durch Loesegeldforderung

Beweis- und Begleitunterlagen:
1. Forensik-Zwischenbericht [Anlage 1]
2. Erpressungsmail [Anlage 2]
3. Log-Auszuege (Hash: [Hash-Wert]) [Anlage 3]

Wir bitten um Bestaetigung des Eingangs und um Mitteilung des
Aktenzeichens.

[Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast und Darlegungslast

| Frage | Last | Norm |
|---|---|---|
| Verletzung DSGVO-Meldepflicht | Behörde im Bußgeldverfahren; Rechenschaft Verantwortlicher | Art. 5 Abs. 2 DSGVO |
| Angemessenheit TOMs | Verantwortlicher — Nachweis | Art. 82 Abs. 3 DSGVO |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| NIS2-Meldepflicht | Behörde (BSI); Einrichtung muss Eigeneinstufung dokumentieren | § 32 BSIG n. F. |
| Straftat § 202a StGB | Staatsanwaltschaft (StPO) | StPO |
| Versicherungsdeckung | Versicherungsnehmer — vertragsgemäße Anzeige und Schadensnachweise | AVB Cyber |

## Fristen und Verjährung

| Pflicht | Frist | Norm |
|---|---|---|
| DSGVO-Meldung Aufsichtsbehörde | 72 Stunden ab Kenntnis | Art. 33 Abs. 1 DSGVO |
| Betroffenen-Benachrichtigung | Unverzüglich | Art. 34 Abs. 1 DSGVO |
| NIS2-Frühwarnung (Verdacht) | 24 Stunden | § 32 Abs. 1 BSIG n. F. |
| NIS2-Vorfallsmeldung | 72 Stunden | § 32 Abs. 2 BSIG n. F. |
| NIS2-Abschlussbericht | 1 Monat | § 32 Abs. 3 BSIG n. F. |
| Versicherer-Anzeige | Vertraglich 24–48 Stunden | AVB Cyber-Police |
| DSGVO-Schadensersatz Verjährung | 3 Jahre §§ 195, 199 BGB | BGB |
| Strafverfolgungsverjährung § 202a StGB | 5 Jahre | § 78 StGB |

## Typische Fehler und Reaktion

| Fehler | Reaktion |
|---|---|
| System abgeschaltet statt Netzwerk getrennt | RAM-Forensik verlorenl; Restinfos aus Backup-Systemen; Täter-Spuren nur noch aus Netzwerkprotokollen |
| 72-Stunden-Frist verpasst | Sofortige Nachmeldung mit Entschuldigungsschreiben; Bußgeldminderung durch Kooperation |
| Lösegeld ohne Sanktionsprüfung gezahlt | AWG § 18 Strafbarkeit; sofortige Kooperation mit BAFA |
| Versicherer nicht binnen 24–48 h angezeigt | Deckungsverlust; AVB-Klausel prüfen; Obliegenheitsverletzung §§ 28 VVG |
| Betriebsrat nicht einbezogen bei Mitarbeiter-Forensik | § 87 BetrVG; einstweilige Verfügung Betriebsrat möglich |

## Streitwert und Kosten

- DSGVO-Bußgeld bei unterlassener Meldung: bis 10 Mio. EUR oder 2 % Jahresumsatz.
- NIS2-Bußgeld besonders wichtige Einrichtungen: bis 20 Mio. EUR oder 4 %.
- Schadensersatz Art. 82 DSGVO: 500–5.000 EUR/Person; bei Massenvorfall Sammelklagen.
- Forensik-Kosten: 10.000–150.000 EUR (je Umfang).
- Krisenmanagement-Kosten: 5.000–50.000 EUR (Kommunikation, Call-Center, Monitoring).
- Cyber-Versicherung typische Deckungs-Sublimits: Lösegeld 10–50 % der Gesamtversicherungssumme.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Ransomware aktiv | Netzwerktrennung sofort; Forensik-Dienstleister binnen 2 Stunden; Backups prüfen |
| Personendaten betroffen | 72h-Meldung einplanen; DSB einbeziehen; bei Zweifel melden |
| KRITIS / NIS2-Einrichtung | 24h-BSI-Frühwarnung; parallel DSGVO-Countdown |
| Lösegeld-Anforderung | Sanktionsprüfung (OFAC/EU); Versicherer; kein Alleingehen |
| Insider-Verdacht | Betriebsrat einbeziehen vor Forensik-Maßnahmen; Arbeitsrecht parallel |

## Anschluss-Skills

- `cyber-incident-response-72h` — komplementäre Detailstufe
- `fachanwalt-it-recht-saas-vertrag-verhandlung` — AVV-Prüfung Cloud-Dienste
- `fachanwalt-strafrecht-zeugenbeistand` — bei Mitarbeiterbefragungen
- `datenschutzrecht-datenpanne-meldung` — formelles Meldeverfahren

## Quellen

- DSGVO Art. 28, 32–34, 82, 83
- NIS2UmsuCG; §§ 28, 32, 65 BSIG n. F.
- StGB §§ 202a–202d, 261, 303a, 303b
- GeschGehG § 9
- BetrVG § 87
- GwG § 43
- AWG § 18
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BSI IT-Grundschutz; BSI Lageberichte Cybersicherheit

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
