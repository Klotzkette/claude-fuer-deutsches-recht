---
name: datenbankrecht-und-cyberincident
description: "Beratung bei Cyberangriffen und Datenbankexfiltration: Prüfung nach §§ 87a-87e UrhG (Herstellerrecht), § 202a StGB (Datenzugang), DSGVO Art. 33-34 (Meldepflicht), NIS2-RL 2022/2555, KRITIS-Dachgesetz. Mandant erlitt Ransomware-Angriff oder Datenleck aus eigenem Datenbankbestand. Output: Notfall-Checkliste, Meldepflichtprüfung BSI/Aufsichtsbehörde, Beweissicherungsprotokoll, Schadensersatzansprüche gegen Angreifer und Dritte im Datenbankrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Datenbankrecht und Cyberincident: Exfiltration, Meldepflicht, Beweissicherung

## Arbeitsbereich

Beratung bei Cyberangriffen und Datenbankexfiltration: Prüfung nach §§ 87a-87e UrhG (Herstellerrecht), § 202a StGB (Datenzugang), DSGVO Art. 33-34 (Meldepflicht), NIS2-RL 2022/2555, KRITIS-Dachgesetz. Mandant erlitt Ransomware-Angriff oder Datenleck aus eigenem Datenbankbestand. Output: Notfall-Checkliste, Meldepflichtprüfung BSI/Aufsichtsbehörde, Beweissicherungsprotokoll, Schadensersatzansprüche gegen Angreifer und Dritte. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
