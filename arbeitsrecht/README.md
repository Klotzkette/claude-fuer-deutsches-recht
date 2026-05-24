# Arbeitsrecht-Plugin

Arbeitsrechtliche Abläufe für Personalabteilungen und Arbeitsrechtler: Einstellungsprüfung, Kündigungsprüfung, Richtlinienerstellung, Personalhandbuch-Updates, Lohn-und-Arbeitszeitfragen sowie Statusfeststellung – auf das deutsche Arbeitsrecht (KSchG, BetrVG, BGB, AGG, ArbZG, MiLoG, MuSchG, BEEG, TzBfG, BUrlG, EFZG, SGB IV) zugeschnitten.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, mit Prüfhinweisen versehen und gegen unbeabsichtigte Weitergabe gesichert. Das Plugin erledigt die Recherchearbeit: Es liest Dokumente, wendet Ihre Prüfschemata an, benennt Risiken und erstellt Entwürfe. Die rechtliche Beurteilung und die Entscheidung liegen beim Rechtsanwalt oder Syndikusrechtsanwalt.** Zitate werden nach ihrer Quelle gekennzeichnet, damit klar ist, welche überprüft werden müssen. Vertraulichkeitsvermerke werden zurückhaltend gesetzt. Folgenreiche Handlungen – Einreichen, Versenden, Vollziehen – erfordern ausdrückliche Freigabe.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Arbeitsrecht (`arbeitsrecht`, dieses Plugin) | [arbeitsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus „Code → Download ZIP“ verwenden.


## Für wen ist das Plugin

| Rolle | Primäre Abläufe |
|---|---|
| **Arbeitsrechtlicher Berater / Fachanwalt Arbeitsrecht** | Kündigungsprüfung, Statusfeststellung, Interne Untersuchung, KSchG-Klage, Aufhebungsvertrag |
| **Syndikusrechtsanwalt (in-house)** | Einstellungsprüfung, Personalrichtlinien, Betriebsratsanhörung, Lohn-und-Arbeitszeitfragen |
| **HR Business Partner / Personalleiter** | Einstellungsprüfung, Handbuch-Updates, Urlaub-/Fehlzeiten-Tracker, Abmahnungsentwürfe |
| **GC / Leiter Rechtsabteilung** | Eskalationsempfänger bei hochriskanten Kündigungen, Massenentlassungen, Einigungsstellenverfahren |

## Ersteinrichtung: Kaltstart

Fragt ab, in welchen Bundesländern und Ländern Mitarbeiter beschäftigt sind, liest Ihr Personalhandbuch und drei aktuelle Kündigungsunterlagen, erstellt eine standortbezogene Eskalationstabelle und speichert die Kanzlei- oder Unternehmenskonfiguration.

```
/arbeitsrecht:arbeitsrecht-kaltstart-interview
```

Die Konfiguration wird unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` gespeichert und übersteht Plugin-Updates.

## Voraussetzungen

- **Persistenter Datenpfad.** Der Urlaubsregister, die Untersuchungsprotokolle und die Entsendungs-Tracker werden unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/` gespeichert. Diese Dateien enthalten privilegierte und personenbezogene Daten – vergewissern Sie sich, dass das Verzeichnis gesichert und zugriffsgeschützt ist (§ 26 BDSG, Art. 5 Abs. 1 lit. f DSGVO).
- **Rechtsdatenbank-Zugang.** Die Skills speichern keine konkreten Rechtsnorminhalte (Schwellenwerte, Fristenberechnungen, länderspezifische Regelungen). Alle jurisdiktionsspezifischen Regeln werden zum Zeitpunkt der Prüfung recherchiert und zitiert. Stellen Sie sicher, dass die Sitzung Zugang zu den genutzten Recherchewerkzeugen hat.
- **Außenanwalt bei Fachfragen.** Für neue Jurisdiktionen, komplexe Statusfeststellungen oder hochriskante Maßnahmen wird externer Sachverstand empfohlen.
- **Mandatsgeheimnis.** § 43a Abs. 2 BRAO, § 203 StGB und § 53 StPO gelten für alle Ausgaben dieses Plugins. Keine Weitergabe vertraulicher Mandantendaten ohne ausdrückliche Freigabe.

## Skills

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:arbeitsrecht-kaltstart-interview` | Ersteinrichtung – Standortprofil, Eskalationsregeln, Handbuchwissen |
| `/arbeitsrecht:einstellungspruefung` | Arbeitsvertragsprüfung: Befristung (TzBfG), AGG, AÜG, Nachweisgesetz |
| `/arbeitsrecht:kuendigungs-pruefung` | Kündigungsprüfung: KSchG, § 102 BetrVG, §§ 622, 626 BGB, Sozialauswahl |
| `/arbeitsrecht:kuendigungsschutzklage` | Entwurf und Prüfung der KSchG-Klage, § 4 KSchG, 3-Wochen-Frist, Klageschrift ArbG |
| `/arbeitsrecht:abmahnung-arbeitsrecht` | Abmahnungsentwurf und -bewertung nach BAG-Grundsätzen |
| `/arbeitsrecht:aufhebungsvertrag` | Aufhebungsvertrag inkl. Sperrzeitprüfung § 159 SGB III, Abfindungssteuer § 34 EStG |
| `/arbeitsrecht:betriebsrat-anhoerung` | Betriebsratsanhörung § 102 BetrVG – Fristen, Inhalt, Mitteilungspflichten |
| `/arbeitsrecht:lohn-arbeitszeit-fragen` | Lohn-/Arbeitszeitfragen: ArbZG, MiLoG, EFZG – standortbezogen |
| `/arbeitsrecht:arbeitnehmer-status` | Statusfeststellung § 7a SGB IV, Scheinselbständigkeit, AÜG |
| `/arbeitsrecht:lohnsteuer-sozialversicherung` | Statusfeststellung, Scheinselbständigkeit, Clearingverfahren DRV |
| `/arbeitsrecht:fehlzeiten-register` | Urlaubsregister und Fehlzeitentracker: BUrlG, EFZG, MuSchG, BEEG |
| `/arbeitsrecht:fehlzeit-erfassen` | Neue Fehlzeit / neuen Urlaub im Register anlegen |
| `/arbeitsrecht:expansion-auftakt [Land]` | Entsendungs-/Expansionsprojekt eröffnen: AÜG, A1, EU-Entsende-RL, AentG |
| `/arbeitsrecht:expansion-aktualisierung [Land]` | Offenes Entsendungsprojekt aktualisieren |
| `/arbeitsrecht:untersuchung-eroeffnen` | Interne Untersuchung eröffnen – Intake, Quellenplan, Protokoll anlegen |
| `/arbeitsrecht:untersuchung-ergaenzen` | Dokumente / Gesprächsnotizen zu offener Untersuchung hinzufügen |
| `/arbeitsrecht:untersuchung-abfrage` | Fragen gegen Untersuchungsprotokoll stellen |
| `/arbeitsrecht:untersuchungs-memo` | Privilegiertes Untersuchungs-Memo erstellen oder aktualisieren |
| `/arbeitsrecht:untersuchungs-zusammenfassung` | Zielgruppenspezifische Zusammenfassung (HR, Geschäftsführung, Außenanwalt) |
| `/arbeitsrecht:handbuch-aktualisierung` | Personalrichtlinien diff und Betriebsvereinbarungsauswirkungen prüfen |
| `/arbeitsrecht:richtlinien-entwurf [Thema]` | BetrVG-konforme Richtlinie entwerfen, BR-Anhörung planen |
| `/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich` | Mandatsakte verwalten (multi-mandant): neu, auflisten, wechseln, schließen, keine |
| `/arbeitsrecht:arbeitsrecht-anpassen` | Kanzlei-/Unternehmensprofil gezielt anpassen |

## Interaktive Skills vs. geplante Agenten

Die obigen Skills werden auf Abruf ausgeführt. Der folgende Agent läuft nach Zeitplan:

| Agent | Überwacht | Standard-Rhythmus |
|---|---|---|
| **urlaub-fehlzeiten** | Offene Abwesenheiten mit gesetzlichen Fristen – BUrlG, EFZG, MuSchG, BEEG; Fristen- und Entscheidungshinweise vor Ablauf | Wöchentlich (montags) |

## Anwendungsbeispiele für die deutsche Kanzlei

**Szenario 1 – Ordentliche Kündigung mit Sozialauswahl:**
```
/arbeitsrecht:kuendigungs-pruefung
Mandant plant betriebsbedingte Kündigung von 3 von 12 Arbeitnehmern.
Betrieb hat 15 AN, kein BR. Bitte Sozialauswahl prüfen und § 1 KSchG
Interessenabwägung durchführen.
```

**Szenario 2 – Befristeter Arbeitsvertrag:**
```
/arbeitsrecht:einstellungspruefung
Neuer Mitarbeiter, Befristung ohne Sachgrund auf 2 Jahre nach § 14 Abs. 2
TzBfG. Vorherige Beschäftigung beim selben Arbeitgeber vor 5 Jahren.
Bitte Vorbeschäftigungsverbot prüfen.
```

**Szenario 3 – Abmahnung wegen unentschuldigten Fehlens:**
```
/arbeitsrecht:abmahnung-arbeitsrecht
Mitarbeiter war an 3 Tagen ohne Krankmeldung nicht erschienen. Erste
Abmahnung. Bitte BAG-konforme Abmahnung entwerfen.
```

**Szenario 4 – Interne Untersuchung / Compliance:**
```
/arbeitsrecht:untersuchung-eroeffnen
Verdacht auf Unterschlagung durch Teamleiter in der Buchhaltung. Hinweis
durch anonyme Meldestelle. Bitte Untersuchungsprotokoll anlegen und
Quellenplan § 26 BDSG-konform erstellen.
```

**Szenario 5 – Entsendung nach Frankreich:**
```
/arbeitsrecht:expansion-auftakt Frankreich
Mitarbeiter soll für 18 Monate nach Paris entsendet werden. Bitte A1-
Bescheinigung, AEntG-Anforderungen und Entsendevertrag-Checkliste.
```

## Neue Workflows v3.3.1

### Bündel 1: Kündigungsschutzklage Selbsthilfe-Workflow (KüSchK)

Vollständiger Workflow für Verbraucher und Anwälte zur eigenständigen Einreichung und Verteidigung einer Kündigungsschutzklage — von der Triage über die Klageschrift bis zur Vergleichsverhandlung.

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:kueschk-triage-laie-oder-anwalt` | KERNEINSTIEG: Anwalt oder Laie; Weichenstellung für den gesamten Workflow |
| `/arbeitsrecht:kueschk-grundwarnung-falsche-wiese-und-haftung` | Pflichtkopf für alle Laien-Schriftsätze: Haftungsausschluss, Dreiwochenfrist |
| `/arbeitsrecht:kueschk-anwendbarkeit-kschg-pruefen` | § 1 Abs. 1 KSchG Wartezeit; § 23 KSchG Betriebsgröße; Teilzeit-Berechnung |
| `/arbeitsrecht:kueschk-kuendigungsgrund-personen-verhalten-betrieb` | Drei Kündigungsgründe § 1 Abs. 2 KSchG; Sonderkündigungsschutz-Querverweis |
| `/arbeitsrecht:kueschk-sonderkuendigungsschutz-checkliste` | Schwangerschaft, Elternzeit, Schwerbehinderung, BR-Mitglied, Datenschutzbeauftragter |
| `/arbeitsrecht:kueschk-formfehler-pruefen` | § 623 BGB, § 174 BGB Vollmachtsrüge, § 102 BetrVG, §§ 17/18 KSchG |
| `/arbeitsrecht:kueschk-frist-und-zugang-pruefen` | § 4 KSchG Dreiwochenfrist; § 5 KSchG nachträgliche Zulassung; Zugangsbeweis |
| `/arbeitsrecht:kueschk-klageschrift-laie-baustein` | Ausfüllbare Klageschrift Schritt für Schritt für Laien |
| `/arbeitsrecht:kueschk-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift mit Hilfsanträgen und Anlagen-Checkliste |
| `/arbeitsrecht:kueschk-allgemeiner-und-besonderer-feststellungsantrag` | Punktueller Antrag § 4 KSchG vs. Schleppnetz § 256 ZPO |
| `/arbeitsrecht:kueschk-weiterbeschaeftigungsantrag-grosser-senat` | BAG GS 1985; Voraussetzungen; Vor- und Nachteile |
| `/arbeitsrecht:kueschk-annahmeverzug-loehne-anrechnung-zwischenverdienst` | § 615 BGB; § 11 KSchG Anrechnung; böswilliges Unterlassen |
| `/arbeitsrecht:kueschk-erwiderung-arbeitgeber-strategien-typisch` | Typische Arbeitgeberstrategien; Stricken-Anwälte; Hinhaltetaktik |
| `/arbeitsrecht:kueschk-replik-arbeitnehmer-baustein` | Replik auf Klageerwiderung; Substantiierungstiefe; Beweismittel |
| `/arbeitsrecht:kueschk-guetetermin-strategie-und-sprechzettel` | § 54 ArbGG Gütetermin; Sprechzettel; was sagen / nicht sagen |
| `/arbeitsrecht:kueschk-kammertermin-sprechzettel` | Kammertermin Hauptverhandlung; Antragsstellung; Reaktionsmuster |
| `/arbeitsrecht:kueschk-muendliche-verhandlung-praxistipps-laie` | Auftreten, Kleidung, Anrede, Sitzungsverlauf für Laien |
| `/arbeitsrecht:kueschk-vergleichsverhandlung-checkliste` | Alle Vergleichsbausteine: Abfindung, Zeugnis, Freistellung, Erledigung |
| `/arbeitsrecht:kueschk-abfindung-faustformel-und-spannweite` | Faustformel; Spannweite; § 34 EStG Fünftel-Regelung |
| `/arbeitsrecht:kueschk-stricken-anwalt-risiko-und-vergleichsdruck` | KERNWARNUNG: Stricken-Strategie; Rückkehrpflicht; § 12 KSchG; § 9 KSchG |
| `/arbeitsrecht:kueschk-aufloesungsantrag-arbeitnehmer-9-kschg` | Auflösungsantrag § 9 KSchG bei Unzumutbarkeit; Abfindung § 10 KSchG |
| `/arbeitsrecht:kueschk-paragraph-12-kschg-neuer-job-einseitig` | § 12 KSchG einseitige Lösung; Wochenfrist; Abgrenzung § 9 KSchG |
| `/arbeitsrecht:kueschk-zeugnisanspruch-und-vergleich` | § 109 GewO; BAG-Mindeststandard; geheime Negativsignale; Vergleichsformulierungen |
| `/arbeitsrecht:kueschk-streitwert-kostenfolge-prozesskostenhilfe` | § 42 GKG; § 12a ArbGG keine Kostenerstattung erste Instanz; PKH |
| `/arbeitsrecht:kueschk-berufung-und-revision-lag-bag` | Berufung LAG; Revision BAG; Zulassungsgründe; Fristen |
| `/arbeitsrecht:kueschk-output-warnschriftsatz-laie` | Vollständige Klageschrift mit Pflicht-Disclaimer für Laien |

### Bündel 2: Entfristungsklage / Befristungskontrollklage (TzBfG)

Vollständiger Workflow für die Klage auf Feststellung, dass ein angeblich befristeter Vertrag unbefristet ist — insbesondere bei Schriftformverstößen nach § 14 Abs. 4 TzBfG und digitaler Vertragsunterzeichnung.

| Skill | Funktion |
|---|---|
| `/arbeitsrecht:entfristung-triage-was-will-user` | Einstieg; Erkennung Entfristungsklage; Abgrenzung zu KüSchK |
| `/arbeitsrecht:entfristung-laie-oder-anwalt-frage` | Statusabfrage; Laien-Warnungen; Empfehlung anwaltlicher Beratung |
| `/arbeitsrecht:entfristung-grundwarnung-drei-wochen-frist` | § 17 TzBfG Dreiwochenfrist ab vereinbartem Ende; Fiktionswirkung § 7 KSchG |
| `/arbeitsrecht:entfristung-sachgrund-pruefen-14-abs-1` | Acht Sachgründe § 14 Abs. 1 TzBfG; Prüfungsstruktur; Beweislast |
| `/arbeitsrecht:entfristung-sachgrundlos-14-abs-2-vorbeschaeftigung` | § 14 Abs. 2 TzBfG; Vorbeschäftigungsverbot; BVerfG 2018; Karenzzeit |
| `/arbeitsrecht:entfristung-sachgrundlos-14-abs-2a-neugruendung` | Neugründungsprivileg vier Jahre § 14 Abs. 2a TzBfG |
| `/arbeitsrecht:entfristung-sachgrundlos-14-abs-3-aelter-52` | § 14 Abs. 3 TzBfG; Befristung ab 52; Vorarbeitslosigkeit |
| `/arbeitsrecht:entfristung-schriftform-14-abs-4-erkennen` | KERNSKILL: Schriftform § 14 Abs. 4 TzBfG; eigenhändige Unterschrift; KEINE elektronische Form |
| `/arbeitsrecht:entfristung-elektronische-signatur-vorsicht` | DocuSign, Adobe Sign als Erkennungsmerkmale; Signaturtypen; Rechtslage |
| `/arbeitsrecht:entfristung-rechtsfolge-16-tzbfg-unbefristet` | § 16 Satz 1 TzBfG Vertrag gilt als unbefristet; früheste Kündigung § 16 Satz 2 |
| `/arbeitsrecht:entfristung-klageschrift-laie-baustein` | Schritt-für-Schritt Klageschrift Entfristungsklage für Laien |
| `/arbeitsrecht:entfristung-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift mit Hilfsanträgen und Weiterbeschäftigungsantrag |
| `/arbeitsrecht:entfristung-guetetermin-und-kammertermin-sprechzettel` | Sprechzettel mündliche Verhandlung; Kernargumente Schriftformmangel |
| `/arbeitsrecht:entfristung-vergleichsverhandlung-checkliste` | Vergleichsbausteine Entfristungsklage; Beendigungsdatum; Abfindung; Zeugnis |
| `/arbeitsrecht:entfristung-output-warnschriftsatz-laie` | Vollständige Klageschrift mit Pflicht-Disclaimer für Laien |


## Testakten

Für beide Arbeitsrecht-Skill-Bündel gibt es fertige fiktive Mandatsakten zum sofortigen Ausprobieren im Ordner [`testakten/`](../testakten/):

| Testakte | Inhalt | Passt zu |
|---|---|---|
| [`testakten/kuendigungsschutzklage-weber-techlogix/`](../testakten/kuendigungsschutzklage-weber-techlogix/) | Markus Weber ./. TechLogix GmbH Berlin: betriebsbedingte Kündigung 30.04.2026, lückenhafte BR-Anhörung, fragwürdige Sozialauswahl (Weber 8 J. BZ + 2 Kinder vs. Grunewald 2 J. BZ), § 4 KSchG-Frist 20.05.2026. | `kueschk-*` |
| [`testakten/befristungskontrollklage-vogt-stadtwerke/`](../testakten/befristungskontrollklage-vogt-stadtwerke/) | Lena Vogt ./. Stadtwerke Neukölln GmbH: Befristungskontrollklage, Schriftformverstoß § 14 Abs. 4 TzBfG (AV nur per E-Mail + Scan), Vorbeschäftigung 2021 als Graubereich, § 17 TzBfG-Frist 20.03.2026. | `entfristung-*` |

Download als ZIP:
[testakte-kuendigungsschutzklage-weber-techlogix.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kuendigungsschutzklage-weber-techlogix.zip) · [testakte-befristungskontrollklage-vogt-stadtwerke.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-befristungskontrollklage-vogt-stadtwerke.zip)

### Kündigungsschutzklage Weber ./. TechLogix — Einzeldateien

| Datei | Inhalt |
|---|---|
| [README.md](../testakten/kuendigungsschutzklage-weber-techlogix/README.md) | Überblick, Fristen, Streitpunkte |
| [kündigungsschreiben_techlogix_30-04-2026.txt](../testakten/kuendigungsschutzklage-weber-techlogix/kuendigungsschreiben_techlogix_30-04-2026.txt) | Kündigungsschreiben vom 30.04.2026 |
| [arbeitsvertrag_weber_2018_auszug.txt](../testakten/kuendigungsschutzklage-weber-techlogix/arbeitsvertrag_weber_2018_auszug.txt) | Arbeitsvertrag Auszug 2018 |
| [betriebsrat_anhörung_entwurf_roh.txt](../testakten/kuendigungsschutzklage-weber-techlogix/betriebsrat_anhoerung_entwurf_roh.txt) | Roh-Entwurf der BR-Anhörung mit Lücken |
| [sozialauswahl_vergleichstabelle_roh.md](../testakten/kuendigungsschutzklage-weber-techlogix/sozialauswahl_vergleichstabelle_roh.md) | Sozialauswahl-Vergleichstabelle Weber vs. Grunewald |
| [mandantennotiz_erstgespräch_06-05-2026.txt](../testakten/kuendigungsschutzklage-weber-techlogix/mandantennotiz_erstgespraech_06-05-2026.txt) | Mandantennotiz Erstgespräch |
| [notiz_weber_gespräch_märz_2026.txt](../testakten/kuendigungsschutzklage-weber-techlogix/notiz_weber_gespraech_maerz_2026.txt) | Notiz Vorgespräch März 2026 |
| [vollmacht_weber.txt](../testakten/kuendigungsschutzklage-weber-techlogix/vollmacht_weber.txt) | Vollmacht des Mandanten |

### Befristungskontrollklage Vogt ./. Stadtwerke Neukölln — Einzeldateien

| Datei | Inhalt |
|---|---|
| [README.md](../testakten/befristungskontrollklage-vogt-stadtwerke/README.md) | Überblick, Fristen, Streitpunkte |
| [arbeitsvertrag_vogt_2024_per_email.txt](../testakten/befristungskontrollklage-vogt-stadtwerke/arbeitsvertrag_vogt_2024_per_email.txt) | Befristeter Arbeitsvertrag (per E-Mail übermittelt, Schriftformproblem § 14 Abs. 4 TzBfG) |
| [email_übermittlung_vertrag_feb_2024.txt](../testakten/befristungskontrollklage-vogt-stadtwerke/email_uebermittlung_vertrag_feb_2024.txt) | E-Mail mit Vertrag (Februar 2024) |
| [arbeitsvertrag_ferienaushilfe_2021_auszug.txt](../testakten/befristungskontrollklage-vogt-stadtwerke/arbeitsvertrag_ferienaushilfe_2021_auszug.txt) | Vorbeschäftigung 2021 als Ferienaushilfe |
| [email_schoenfeld_kein_folgevertrag_jan_2026.txt](../testakten/befristungskontrollklage-vogt-stadtwerke/email_schoenfeld_kein_folgevertrag_jan_2026.txt) | E-Mail Schönfeld: kein Folgevertrag (Januar 2026) |
| [mandantennotiz_erstgespräch_09-03-2026.txt](../testakten/befristungskontrollklage-vogt-stadtwerke/mandantennotiz_erstgespraech_09-03-2026.txt) | Mandantennotiz Erstgespräch |
| [vollmacht_vogt.txt](../testakten/befristungskontrollklage-vogt-stadtwerke/vollmacht_vogt.txt) | Vollmacht der Mandantin |

## Lerneffekt

Ihr Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich durch Nutzung. Skills weisen Sie hin, wenn eine Ausgabe auf einem Standardwert beruht, der angepasst werden sollte. Sie können die Einrichtung erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position zu speichern.

## Hinweise

- **Standortkenntnis ist der Kern.** Das Plugin kennt die Unterschiede zwischen Bundesländern und berücksichtigt betriebliche Besonderheiten (Betriebsgröße, Betriebsrat, Tarifbindung).
- **Kündigungsprüfung ersetzt nicht das Gespräch mit HR und Führungskraft.** Sie ist eine Checkliste, die den vergessenen Punkt findet.
- **Lohn-/Arbeitszeitfragen zitieren die Norm**, kennzeichnen aber Grenzfälle zur menschlichen Prüfung. Einstufungsentscheidungen haben Konsequenzen.
- **Zitierstandard:** BGH-Stil gemäß `../references/zitierweise.md`. Rechtsprechung: BAG, BGH, EuGH im Format `BAG, Urt. v. TT.MM.JJJJ – Az., NZA JJJJ, Seite Rn. N.` Kommentare: ErfK, HWK, KR, APS, MüKoBGB, BeckOK Arbeitsrecht.
