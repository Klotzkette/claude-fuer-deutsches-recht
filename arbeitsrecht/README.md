# Arbeitsrecht-Plugin

Arbeitsrechtliche Abläufe für Personalabteilungen und Arbeitsrechtler: Einstellungsprüfung, Kündigungsprüfung, Richtlinienerstellung, Personalhandbuch-Updates, Lohn-und-Arbeitszeitfragen sowie Statusfeststellung – auf das deutsche Arbeitsrecht (KSchG, BetrVG, BGB, AGG, ArbZG, MiLoG, MuSchG, BEEG, TzBfG, BUrlG, EFZG, SGB IV) zugeschnitten.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, mit Prüfhinweisen versehen und gegen unbeabsichtigte Weitergabe gesichert. Das Plugin erledigt die Recherchearbeit: Es liest Dokumente, wendet Ihre Prüfschemata an, benennt Risiken und erstellt Entwürfe. Die rechtliche Beurteilung und die Entscheidung liegen beim Rechtsanwalt oder Syndikusrechtsanwalt.** Zitate werden nach ihrer Quelle gekennzeichnet, damit klar ist, welche überprüft werden müssen. Vertraulichkeitsvermerke werden zurückhaltend gesetzt. Folgenreiche Handlungen – Einreichen, Versenden, Vollziehen – erfordern ausdrückliche Freigabe.

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
/arbeitsrecht:kaltstart-interview
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
| `/arbeitsrecht:kaltstart-interview` | Ersteinrichtung – Standortprofil, Eskalationsregeln, Handbuchwissen |
| `/arbeitsrecht:einstellungspruefung` | Arbeitsvertragsprüfung: Befristung (TzBfG), AGG, AÜG, Nachweisgesetz |
| `/arbeitsrecht:kuendigungs-pruefung` | Kündigungsprüfung: KSchG, § 102 BetrVG, §§ 622, 626 BGB, Sozialauswahl |
| `/arbeitsrecht:kuendigungsschutzklage` | Entwurf und Prüfung der KSchG-Klage, § 4 KSchG, 3-Wochen-Frist, Klageschrift ArbG |
| `/arbeitsrecht:abmahnung-arbeitsrecht` | Abmahnungsentwurf und -bewertung nach BAG-Grundsätzen |
| `/arbeitsrecht:aufhebungsvertrag` | Aufhebungsvertrag inkl. Sperrzeitprüfung § 159 SGB III, Abfindungssteuer § 34 EStG |
| `/arbeitsrecht:betriebsrat-anhoerung` | Betriebsratsanhörung § 102 BetrVG – Fristen, Inhalt, Mitteilungspflichten |
| `/arbeitsrecht:lohn-arbeitszeit-fragen` | Lohn-/Arbeitszeitfragen: ArbZG, MiLoG, EFZG – standortbezogen |
| `/arbeitsrecht:arbeitnehmer-status` | Statusfeststellung § 7a SGB IV, Scheinselbständigkeit, AÜG |
| `/arbeitsrecht:lohnsteuer-sozialversicherung` | Statusfeststellung, Scheinselbständigkeit, Clearingverfahren DRV |
| `/arbeitsrecht:urlaub-fehlzeiten` | Urlaubsregister und Fehlzeitentracker: BUrlG, EFZG, MuSchG, BEEG |
| `/arbeitsrecht:fehlzeit-erfassen` | Neue Fehlzeit / neuen Urlaub im Register anlegen |
| `/arbeitsrecht:internationaler-einsatz-kickoff [Land]` | Entsendungs-/Expansionsprojekt eröffnen: AÜG, A1, EU-Entsende-RL, AentG |
| `/arbeitsrecht:internationaler-einsatz-update [Land]` | Offenes Entsendungsprojekt aktualisieren |
| `/arbeitsrecht:untersuchung-eroeffnen` | Interne Untersuchung eröffnen – Intake, Quellenplan, Protokoll anlegen |
| `/arbeitsrecht:untersuchung-hinzufuegen` | Dokumente / Gesprächsnotizen zu offener Untersuchung hinzufügen |
| `/arbeitsrecht:untersuchung-abfragen` | Fragen gegen Untersuchungsprotokoll stellen |
| `/arbeitsrecht:untersuchung-memo` | Privilegiertes Untersuchungs-Memo erstellen oder aktualisieren |
| `/arbeitsrecht:untersuchung-zusammenfassung` | Zielgruppenspezifische Zusammenfassung (HR, Geschäftsführung, Außenanwalt) |
| `/arbeitsrecht:personalrichtlinien` | Personalrichtlinien diff und Betriebsvereinbarungsauswirkungen prüfen |
| `/arbeitsrecht:richtlinienerstellung [Thema]` | BetrVG-konforme Richtlinie entwerfen, BR-Anhörung planen |
| `/arbeitsrecht:mandatsakte` | Mandatsakte verwalten (multi-mandant): neu, auflisten, wechseln, schließen, keine |
| `/arbeitsrecht:anpassen` | Kanzlei-/Unternehmensprofil gezielt anpassen |

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
/arbeitsrecht:internationaler-einsatz-kickoff Frankreich
Mitarbeiter soll für 18 Monate nach Paris entsendet werden. Bitte A1-
Bescheinigung, AEntG-Anforderungen und Entsendevertrag-Checkliste.
```

## Lerneffekt

Ihr Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich durch Nutzung. Skills weisen Sie hin, wenn eine Ausgabe auf einem Standardwert beruht, der angepasst werden sollte. Sie können die Einrichtung erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position zu speichern.

## Hinweise

- **Standortkenntnis ist der Kern.** Das Plugin kennt die Unterschiede zwischen Bundesländern und berücksichtigt betriebliche Besonderheiten (Betriebsgröße, Betriebsrat, Tarifbindung).
- **Kündigungsprüfung ersetzt nicht das Gespräch mit HR und Führungskraft.** Sie ist eine Checkliste, die den vergessenen Punkt findet.
- **Lohn-/Arbeitszeitfragen zitieren die Norm**, kennzeichnen aber Grenzfälle zur menschlichen Prüfung. Einstufungsentscheidungen haben Konsequenzen.
- **Zitierstandard:** BGH-Stil gemäß `../references/zitierweise.md`. Rechtsprechung: BAG, BGH, EuGH im Format `BAG, Urt. v. TT.MM.JJJJ – Az., NZA JJJJ, Seite Rn. N.` Kommentare: ErfK, HWK, KR, APS, MüKoBGB, BeckOK Arbeitsrecht.
