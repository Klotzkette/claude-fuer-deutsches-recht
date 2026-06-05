---
name: db-agrar-logistik-cyberincident
description: "Db Datenbankrecht Agrar Sensordaten / Db Datenbankrecht Logistik Tracking / Db Datenbankrecht Cyberincident: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output."
---

# Db Datenbankrecht Agrar Sensordaten / Db Datenbankrecht Logistik Tracking / Db Datenbankrecht Cyberincident

## Arbeitsbereich

Dieser Skill bündelt **Db Datenbankrecht Agrar Sensordaten / Db Datenbankrecht Logistik Tracking / Db Datenbankrecht Cyberincident**. Wähle zuerst das Modul, dessen Tatsachen die Akte tragen; kombiniere weitere Module nur, wenn dieselbe Frist, Zuständigkeit, Beweislast oder derselbe Output dadurch wirklich klarer wird.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `db-060-datenbankrecht-agrar-und-sensordaten` | Datenbankrecht für Agrar- und Sensordaten: §§ 87a-87e UrhG für Präzisionslandwirtschaftsdatenbanken und IoT-Sensornetzwerke, Data Act (VO 2023/2854) Zugangsrechte für Landwirte, Verhältnis zu Geschäftsgeheimnissen (GeschGehG) bei Erntedaten und DSGVO-Anforderungen bei personenbezogenen Agrardaten. Erstellt Datenstrategie für AgTech-Unternehmen. |
| `db-061-datenbankrecht-im-logistik-tracking` | Datenbankrecht für Logistik-Tracking-Datenbanken: §§ 87a-87e UrhG für Sendungsverfolgungssysteme und Transportdatenbanken, Data Act (VO 2023/2854) Zugangsrechte für Kunden, Schutz gegen Tracking-Aggregatoren und DSGVO-Anforderungen bei personenbezogenen Lieferdaten. Erstellt Schutzstrategie und Lizenzkonzept für Logistikdienstleister. |
| `db-062-datenbankrecht-und-cyberincident` | Beratung bei Cyberangriffen und Datenbankexfiltration: Prüfung nach §§ 87a-87e UrhG (Herstellerrecht), § 202a StGB (Datenzugang), DSGVO Art. 33-34 (Meldepflicht), NIS2-RL 2022/2555, KRITIS-Dachgesetz. Mandant erlitt Ransomware-Angriff oder Datenleck aus eigenem Datenbankbestand. Output: Notfall-Checkliste, Meldepflichtprüfung BSI/Aufsichtsbehörde, Beweissicherungsprotokoll, Schadensersatzansprüche gegen Angreifer und Dritte. |

## Arbeitsweg

Für **Db Datenbankrecht Agrar Sensordaten / Db Datenbankrecht Logistik Tracking / Db Datenbankrecht Cyberincident** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `datenbankrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `db-060-datenbankrecht-agrar-und-sensordaten`

**Fokus:** Datenbankrecht für Agrar- und Sensordaten: §§ 87a-87e UrhG für Präzisionslandwirtschaftsdatenbanken und IoT-Sensornetzwerke, Data Act (VO 2023/2854) Zugangsrechte für Landwirte, Verhältnis zu Geschäftsgeheimnissen (GeschGehG) bei Erntedaten und DSGVO-Anforderungen bei personenbezogenen Agrardaten. Erstellt Datenstrategie für AgTech-Unternehmen.

# Datenbankrecht für Agrar- und Sensordaten — Präzisionslandwirtschaft und IoT

## Mandantenfall

- AgTech-Unternehmen hat eine Bodenanalysedatenbank aus Sensordaten von 500 Betrieben aufgebaut und fragt, ob es Datenbankherstellerrecht hat und wie es die Daten lizenzieren kann.
- Landwirt möchte alle Sensordaten seines Smart-Farm-Equipments von einem AgTech-Anbieter zurückbekommen — Data-Act-Zugangsrecht prüfen.
- Saatgutunternehmen kauft von mehreren AgTech-Anbietern Ertragsdaten für KI-Modell-Training und fragt nach Datenbankrecht und TDM-Schranken.

## Erste Schritte

1. Datenbankherstellerrecht für Agrardatenbank: Wesentliche Investition in Sensorinfrastruktur, Datenqualitätsprüfung und Darstellung (§ 87a UrhG)?
2. BHB-Doktrin für Sensordaten: Sind die Sensordaten selbst erzeugte Daten (Messung der eigenen Felder) oder beschaffte Daten — Investitionstyp bestimmen.
3. Data Act für Landwirte: VO 2023/2854 Art. 4 — Landwirt als Nutzer des Smart-Farm-Equipments hat Zugangsrecht zu von seinem Gerät generierten Daten.
4. Geschäftsgeheimnisse bei Erntedaten: Agrardaten können Betriebsgeheimnisse sein — GeschGehG und Geheimhaltungsmaßnahmen.
5. TDM-Schranke für Saatgutunternehmen: § 44b UrhG — ist die Nutzung für KI-Modell-Training TDM-berechtigt, oder wurde Opt-out erklärt?
6. DSGVO bei personenbezogenen Agrardaten: Können Agrardaten (GPS-Positionsdaten von Landmaschinen) personenbezogen sein?

## Rechtsrahmen

- § 87a UrhG: AgTech-Datenbankherstellerrecht — Investition in Sensordaten-Beschaffung (Betriebsführung der Sensoren), Qualitätsprüfung und Darstellung.
- Data Act VO 2023/2854 Art. 4: Zugangsrecht des Landwirts zu Daten seines Smart-Farm-Equipments.
- GeschGehG § 2 Nr. 1: Ernte- und Ertragsdaten als Betriebsgeheimnisse — wenn angemessene Geheimhaltungsmaßnahmen.
- § 44b UrhG: TDM-Schranke für Saatgutunternehmen — kommerzielle Nutzung, Opt-out relevant.
- DSGVO Art. 4 Nr. 1: GPS-Standortdaten von Landmaschinen können personenbezogene Daten sein, wenn Betriebsinhaber identifizierbar.
- EuGH C-203/02 (BHB/William Hill): Sensorisches Messen von eigenen Feldern ist Datenerzeugung, nicht Datenbeschaffung — BHB-Einwand möglich.

## Prüfraster

- Beruht das AgTech-Herstellerrecht auf Investition in Sensordaten-Beschaffung von Dritten oder auf eigener Messung (BHB-Einwand)?
- Hat der Landwirt nach Data Act Art. 4 ein Zugangsrecht zu seinen Gerätedaten beim AgTech-Anbieter?
- Sind Erntedaten als Betriebsgeheimnisse schützenswert — wurden angemessene Geheimhaltungsmaßnahmen ergriffen?
- Hat der AgTech-Anbieter einen TDM-Opt-out nach § 44b Abs. 3 UrhG erklärt?
- Können GPS-Positionsdaten der Landmaschinen personenbezogene Daten nach DSGVO sein?
- Erlauben Lizenzbedingungen die Nutzung aggregierter Agrardaten für Saatgut-KI-Modell-Training?
- Schützt das Data Act Art. 4 Zugangsrecht den Landwirt auch gegen Einwände aus dem Geschäftsgeheimnisrecht des Anbieters?

## Typische Fallstricke

- AgTech-Anbieter, die Daten von den eigenen Sensoren auf Kundenfeldern sammeln, investieren in Datenerzeugung — BHB-Einwand greift.
- Data Act gibt dem Landwirt Zugangsrecht, hebt aber AgTech-Datenbankherstellerrecht an der Gesamtdatenbank nicht auf.
- Agrardaten aggregierter Betriebe können trotz Einzelanonymisierung in der Kombination re-identifizierbar sein.
- Geschäftsgeheimnisschutz für Erntedaten setzt angemessene Maßnahmen voraus — fehlende NDA oder offene API schwächt den Schutz.
- TDM-Schranke schützt den Saatgut-KI-Anbieter nur, wenn kein wirksamer Opt-out erklärt wurde.

## Output

- AgTech-Datenbankherstellerrecht-Check (BHB-Prüfung + Data Act)
- Data Act Art. 4 Zugangsrecht-Implementierungsguide für AgTech
- Geschäftsgeheimnisschutz-Konzept für Agrardaten
- TDM-Opt-out-Guide für AgTech-Unternehmen
- DSGVO-Agrardaten-Compliance-Check (GPS, Betriebsdaten)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)
- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [DSGVO Art. 4 — dejure.org](https://dejure.org/gesetze/DSGVO/4.html)

## 2. `db-061-datenbankrecht-im-logistik-tracking`

**Fokus:** Datenbankrecht für Logistik-Tracking-Datenbanken: §§ 87a-87e UrhG für Sendungsverfolgungssysteme und Transportdatenbanken, Data Act (VO 2023/2854) Zugangsrechte für Kunden, Schutz gegen Tracking-Aggregatoren und DSGVO-Anforderungen bei personenbezogenen Lieferdaten. Erstellt Schutzstrategie und Lizenzkonzept für Logistikdienstleister.

# Datenbankrecht im Logistik-Tracking — Sendungsverfolgung und Transportdaten

## Mandantenfall

- Logistikdienstleister stellt fest, dass ein Tracking-Aggregator seine Sendungsverfolgungsdaten für ein eigenes Tracking-Portal nutzt, ohne Lizenz.
- E-Commerce-Händler verlangt von seinem Paketdienstleister nach Data Act Art. 4 Zugang zu allen Tracking-Daten seiner Sendungen.
- Frachtbörse fragt, ob ihre Frachtraten-Datenbank gegen systematische Übernahme durch Wettbewerber datenbankherstellerrechtlich geschützt ist.

## Erste Schritte

1. Herstellerrecht für Tracking-Datenbank: Wesentliche Investition in Aufbau, Pflege und Darstellung des Sendungsverfolgungssystems (Infrastruktur, Datenbeschaffung von Subdienstleistern)?
2. BHB-Doktrin für Trackingdaten: Werden die Tracking-Events selbst erzeugt (eigene Scanner, GPS) oder beschafft (Subdienstleister-Daten)? Wenn selbst erzeugt — eingeschränkter Schutz.
3. Data Act Zugangsrecht für Händler: Art. 4 VO 2023/2854 — Händler als Auftraggeber des Transports hat Zugangsrecht zu Sendungsdaten seiner Pakete.
4. Aggregator-Verletzung prüfen: Wesentliche Entnahme von Tracking-Datenbankteilen durch Aggregatoren — § 87b UrhG, Innoweb-Test.
5. Lizenzmodell für Tracking-API: Händler-API, Aggregator-Lizenz, White-Label-Lösung — welche Nutzungen sind lizenzpflichtig?
6. DSGVO bei Lieferdaten: Empfänger-Adressdaten, GPS-Standorte, Zustellnachweise — personenbezogene Daten, Rechtsgrundlage, Löschfristen.

## Rechtsrahmen

- § 87a UrhG: Sendungsverfolgungsdatenbank als Herstellerrecht — Investition in Beschaffung von Tracking-Events, Qualitätsprüfung und Darstellung.
- EuGH C-203/02 (BHB/William Hill): Selbst erzeugte Scanner-Events schützt kein Herstellerrecht — separate Investition in Datenbeschaffung/-überprüfung erforderlich.
- Data Act VO 2023/2854 Art. 4: Zugangsrecht des Auftraggebers zu Sendungsdaten — Logistikdienstleister als Geräteanbieter im Sinne des Data Act.
- § 87b UrhG: Wesentliche Entnahme von Tracking-Daten aus der Datenbank des Logistikdienstleisters.
- EuGH C-202/12 (Innoweb/Wegener): Echtzeit-Aggregatoren, die Fremddatenbanken durchsuchen, verwenden wesentliche Teile weiter.
- DSGVO Art. 6 Abs. 1 lit. b: Vertragserfüllung als Rechtsgrundlage für Verarbeitung von Empfänger-Adressdaten.

## Prüfraster

- Hat der Logistikdienstleister eine wesentliche Investition in die Tracking-Datenbank (Infrastruktur, Subdienstleister-Datenbeschaffung) getätigt?
- Sind die Tracking-Events selbst erzeugte Daten (eigene Scanner) oder beschaffte Daten von Netzwerkpartnern?
- Hat der Händler nach Data Act Art. 4 ein Zugangsrecht zu seinen Sendungsdaten?
- Entnimmt der Aggregator wesentliche Teile der Tracking-Datenbank in Echtzeit (Innoweb-Test)?
- Enthalten Lieferdaten personenbezogene Daten der Empfänger — welche DSGVO-Löschfristen gelten?
- Erlauben API-Nutzungsbedingungen die Nutzung für eigene Tracking-Portale Dritter?
- Schützt der Logistikdienstleister seine Tracking-API durch robots.txt und AGB gegen Aggregatoren?

## Typische Fallstricke

- GPS-Tracking-Events von eigenen Fahrzeugen sind selbst erzeugte Daten — kein Herstellerrecht nach BHB-Doktrin.
- Data Act gibt Händlern Zugangsrecht, schränkt aber das Datenbankherstellerrecht des Logistikers an der Gesamtdatenbank nicht vollständig ein.
- Empfänger-Adressdaten müssen nach DSGVO gelöscht werden, sobald der Lieferzweck erfüllt ist — Archivierung für Analytik erfordert separate Rechtsgrundlage.
- Tracking-Aggregatoren können Innoweb-Test erfüllen, wenn sie Echtzeit-Abfragen an Tracking-APIs richten.
- AGB-Tracking-API-Verbote müssen klar formuliert sein — pauschale Verbote für alle automatisierten Abfragen sind nach § 307 BGB riskant.

## Output

- Tracking-Datenbank-Herstellerrecht-Gutachten (BHB-Prüfung)
- Data Act Art. 4 Zugangsrecht-Implementierungsguide für Logistikdienstleister
- Aggregator-Verletzungsanalyse (§ 87b UrhG + Innoweb-Test)
- DSGVO-Löschfristen-Konzept für Empfänger-Lieferdaten
- Tracking-API-Lizenz-AGB-Vorlage (Händler / Aggregator / White-Label)

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [EuGH C-202/12 Innoweb/Wegener — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [DSGVO Art. 6 — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)

## 3. `db-062-datenbankrecht-und-cyberincident`

**Fokus:** Beratung bei Cyberangriffen und Datenbankexfiltration: Prüfung nach §§ 87a-87e UrhG (Herstellerrecht), § 202a StGB (Datenzugang), DSGVO Art. 33-34 (Meldepflicht), NIS2-RL 2022/2555, KRITIS-Dachgesetz. Mandant erlitt Ransomware-Angriff oder Datenleck aus eigenem Datenbankbestand. Output: Notfall-Checkliste, Meldepflichtprüfung BSI/Aufsichtsbehörde, Beweissicherungsprotokoll, Schadensersatzansprüche gegen Angreifer und Dritte.

# Datenbankrecht und Cyberincident: Exfiltration, Meldepflicht, Beweissicherung

## Mandantenfall

- Ransomware-Angriff verschlüsselt Datenbankserver; Angreifer drohen mit Veröffentlichung des exfiltrierten Datenbankbestands.
- Unbekannte haben über eine SQL-Injection auf die Produktdatenbank zugegriffen und strukturierte Datensätze (Kundenstamm, Preislisten) abgezogen.
- Ein ehemaliger Dienstleister hat nach Vertragsende mit einer Datenbankdumpdatei Wettbewerber beliefert; der Mandant bemerkt identische Datensätze beim Konkurrenten.

## Erste Schritte

1. **Incident abgrenzen**: Feststellen, welche Datenbank(en) betroffen sind, Zeitfenster des Zugriffs und Umfang der exfiltrierten Datensätze schätzen (qualitativ und quantitativ im Sinne von § 87b Abs. 1 UrhG).
2. **Beweissicherung forensisch**: Logfiles, Access-Logs, Datenbankaudit-Trails vor Überschreibung sichern; kryptografischen Hash der Rohdaten erstellen (SHA-256); Notarprotokoll oder IT-Gutachter beauftragen.
3. **DSGVO-Meldepflicht prüfen**: Bei personenbezogenen Daten 72-Stunden-Frist nach Art. 33 DSGVO an die zuständige Datenschutzaufsichtsbehörde; Benachrichtigungspflicht Betroffener nach Art. 34 DSGVO bewerten.
4. **NIS2/KRITIS-Meldepflicht prüfen**: Fällt der Mandant unter NIS2-RL oder das KRITIS-Dachgesetz, sind Meldungen an das BSI innerhalb von 24 Stunden (erheblicher Vorfall) bzw. 72 Stunden (Erstmeldung) erforderlich.
5. **Datenbankrecht-Ansprüche formulieren**: Ansprüche auf Unterlassung, Auskunft, Vernichtung, Schadensersatz nach §§ 87b, 97, 97a UrhG gegen identifizierbare Angreifer oder Hehler prüfen.
6. **Strafanzeige erwägen**: § 202a StGB (Ausspähen von Daten), § 303a StGB (Datenveränderung), § 303b StGB (Computersabotage) bei Ransomware; Strafanzeige bei Staatsanwaltschaft oder LKA.

## Rechtsrahmen

- **§ 87b Abs. 1 UrhG** — Entnahme oder Weiterverwendung wesentlicher Teile der Datenbank ohne Zustimmung des Herstellers ist unzulässig; gilt auch bei rechtswidrigem Systemzugang.
- **§ 97 UrhG** — Anspruch auf Unterlassung und Schadensersatz bei Verletzung des Datenbankherstellerrechts; dreifache Schadensberechnung möglich.
- **Art. 33, 34 DSGVO** — Meldepflicht an Aufsichtsbehörde (72 h) und Benachrichtigung Betroffener bei voraussichtlich hohem Risiko; Dokumentationspflicht Art. 33 Abs. 5 DSGVO.
- **NIS2-RL 2022/2555, Art. 23** — Erhebliche Sicherheitsvorfälle sind unverzüglich (24 h Frühwarnung, 72 h Meldung) dem nationalen CSIRT bzw. BSI zu melden.
- **§ 202a StGB** — Strafbarkeit des unbefugten Zugangs zu gesicherten Daten; korrespondiert mit zivilrechtlichen Ansprüchen aus UrhG.
- **§ 823 Abs. 1 BGB i.V.m. § 87a UrhG** — Deliktsrechtlicher Schadensersatz bei Verletzung des Datenbankherstellerrechts als sonstiges Recht.

## Prüfraster

- Liegt eine schutzfähige Datenbank im Sinne von § 87a UrhG vor (wesentliche Investition in Beschaffung, Überprüfung oder Darstellung)?
- Wurden wesentliche Teile qualitativ oder quantitativ entnommen oder wurden unwesentliche Teile systematisch und wiederholt verwendet (§ 87b Abs. 1 S. 2 UrhG)?
- Sind Logfiles und Audit-Trails vollständig gesichert und integer (Hash-Wert dokumentiert)?
- Greift DSGVO Art. 33: Sind personenbezogene Daten betroffen, und wann begann die 72-Stunden-Frist zu laufen?
- Fällt der Mandant unter NIS2-RL oder KRITIS-Regelungen (Sektor, Schwellenwert, wesentliche oder wichtige Einrichtung)?
- Ist ein identifizierbarer Angreifer oder Empfänger der Daten vorhanden, gegen den Unterlassung und Auskunft durchgesetzt werden können?
- Hat der Mandant vertragliche Sicherheitspflichten (SLA, ISO 27001, TISAX) verletzt und haftet gegenüber Dritten?
- Besteht eine Cyber-Versicherung, die Meldepflichten und Fristen im Policentext vorschreibt?

## Typische Fallstricke

- **Fristversäumnis DSGVO**: 72-Stunden-Frist läuft ab Kenntnisnahme, nicht ab Bestätigung des Vorfalls; interne Eskalation muss sofort erfolgen.
- **Beweise überschreiben**: Automatische Log-Rotation oder Neustart des Systems zerstört Forensikdaten; sofortiger Snapshot und Netzwerktrennung sind Vorrang.
- **Doppelrolle Mandant**: Wer eigene Sicherheitslücken verschweigt, riskiert Mitverschulden (§ 254 BGB) und aufsichtsrechtliche Sanktionen.
- **Fehlende Aktivlegitimation**: Nur der Datenbankhersteller (§ 87a UrhG) kann Ansprüche geltend machen; bei Outsourcing prüfen, wer tatsächlich investiert hat.
- **Ransomware-Zahlung und Sanktionsrecht**: Zahlung an Angreifer kann EU-Sanktionsrecht (VO 269/2014 etc.) oder US-OFAC-Regelungen verletzen; immer vor Zahlung prüfen.

## Output

- Notfall-Checkliste mit Sofortmaßnahmen (Beweissicherung, Systemisolierung, Benachrichtigungskette)
- Meldepflichtmemo: DSGVO Art. 33/34-Analyse, NIS2-Meldestatus, BSI-Formular-Hinweise
- Forensik-Beauftragungsschreiben und Beweissicherungsprotokoll (Hash-Log)
- Unterlassungs- und Auskunftsschreiben nach § 87b, § 97 UrhG gegen Angreifer/Hehler
- Strafanzeigeentwurf (§§ 202a, 303a, 303b StGB)
- Schadensberechnung (Lizenzanalogie, entgangener Gewinn, Wiederherstellungskosten)

## Quellen

- [§ 87a UrhG — Datenbankherstellerrecht (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__87a.html)
- [§ 202a StGB — Ausspähen von Daten (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/stgb/__202a.html)
- [Art. 33 DSGVO — Meldung von Verletzungen (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/dsgvo/art_33_dsgvo.html)
- [NIS2-Richtlinie 2022/2555 (eur-lex.europa.eu)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022L2555)
- [§ 97 UrhG — Anspruch auf Unterlassung und Schadensersatz (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__97.html)
