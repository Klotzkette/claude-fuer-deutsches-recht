# ZVG-Zwangsverwaltung - Verwalter-Cockpit

Technischer Plugin-Name: `zwangsverwaltung-zvg`.

Großes freistehendes Plugin für Zwangsverwalter nach ZVG und ZwVwV sowie für die Schnittstelle zur Zwangsversteigerung. Abgebildet sind Bestellung, Beschlagnahme, Besitzerlangung, Objektaufnahme, Miet- und Pachtverwaltung, Mieteinzug, Betriebskosten, Versicherungen, öffentliche Lasten, Treuhandkonto, Berichtswesen, Rechnungslegung, Verteilung, Räumungs- und Besitzkonflikte, ZVG-Portal-Recherche, Bieterangebotsbewertung und Teilnahme an Versteigerungsterminen.

**Freistehend:** Dieses Plugin enthält eigene Skills, Vorlagen, Quellenhinweise, Vorschau und Testakte. Es verweist nicht auf andere Plugins als Voraussetzung.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| ZVG-Zwangsverwaltung - Verwalter-Cockpit (`zwangsverwaltung-zvg`) | [zwangsverwaltung-zvg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakten

Zu diesem Plugin existieren 3 vollständige Beispielakten:

| Akte | Quelle | Direkt-Download |
|---|---|---|
| Zwangsverwaltung Büro- und Geschäftshaus "Friedrichshöfe" | [`testakten/zwangsverwaltung-friedrichshoefe-berlin/`](../testakten/zwangsverwaltung-friedrichshoefe-berlin/) | [testakte-zwangsverwaltung-friedrichshoefe-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-friedrichshoefe-berlin.zip) |
| Zwangsverwaltung ZVG – Mietshaus Parkstraße 18, Leipzig | [`testakten/zwangsverwaltung-zvg-mietshaus-parkstrasse/`](../testakten/zwangsverwaltung-zvg-mietshaus-parkstrasse/) | [testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip) |
| ZVG-Versteigerung Eppendorf-Altbau | [`testakten/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau/`](../testakten/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau/) | [testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip) |

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `zwangsverwaltung-zvg.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte das ZVG-Kommandocenter für dieses Mietshaus.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

### Zum Ausprobieren: Testakten (separat)

Fiktive Mandatsakten zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **Friedrichshoefe Berlin (Zwangsverwaltung)** | [testakte-zwangsverwaltung-friedrichshoefe-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-friedrichshoefe-berlin.zip) |
| **Mietshaus Parkstrasse (ZVG)** | [testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip) |
| **Eppendorf Altbau (ZVG-Versteigerung)** | [testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip) |

## Kernmodule

| Modul | Funktion |
| Anordnung und Besitz | Bestellung, Bestallung, Beschlagnahmeumfang, Besitzerlangung und Objektaufnahme. |
| Objektbetrieb | Mieter, Pächter, Betriebskosten, Hausgeld, Instandhaltung, Gefahrensicherung und Versicherungen. |
| Finanzen | Treuhandkonto, Soll-Ist-Abgleich, Mieteinzug, Vorschuss, Belege und Kassenbuch. |
| Berichte | Besitzerlangungsbericht, Monatsbericht, gerichtliche Entscheidungsvorlage und Auskunft. |
| Rechnung und Verteilung | Jahresrechnung, Schlussrechnung, Endabrechnung, § 155 ZVG-Verteilung. |
| Konflikte | Räumung, Kündigung, Zutritt, Schuldnerhausstand, Insolvenzschnittstelle und Versteigerung. |
| Versteigerung | ZVG-Portal-Suche, Bekanntmachung, Gutachten, geringstes Gebot, Sicherheitsleistung, Bietlimit und Terminvorbereitung. |

## Skill-Landkarte

| Skill | Zweck |
| `zvg-kommandocenter` | Startet Zwangsverwaltung mit Objekt, Beteiligten, Beschluss und Sofortmaßnahmen. |
| `zvg-aktenanlage-objektcockpit` | Legt Objektakte, Rent Roll, Lastenregister, Konto und Berichtswesen an. |
| `zvg-bestellung-beschlagnahme` | Prüft Anordnung, Beschlagnahmeumfang, Ausweis, Rang und Gerichtsvorgaben. |
| `zvg-besitzuebernahme` | Organisiert Besitznahme, Protokoll, Schlüssel, Zustand, Mobilien und Sofortgefahren. |
| `zvg-miet-und-pachtverwaltung` | Verwaltet Miet- und Pachtverträge, Zahlstellen, Vorausverfügungen und Kautionen. |
| `zvg-mieteinzug-rueckstaende` | Treibt Mieten ein, matcht Zahlungen, mahnt und bereitet Klagen vor. |
| `zvg-betriebskosten-hausgeld` | Steuert Betriebskosten, Hausgeld, Dienstleister, Abrechnung und Liquidität. |
| `zvg-instandhaltung-sicherung` | Prüft Verkehrssicherung, Notmaßnahmen, Instandhaltung, Zustimmung und Budget. |
| `zvg-versicherungen-gefahren` | Sichert Gebäudeversicherung, Haftpflicht, Beitragsrückstände und Schadensfälle. |
| `zvg-oeffentliche-lasten` | Erfasst Grundsteuer, Gebühren, Lasten, Rang und Zahlungsplan. |
| `zvg-konten-kassenfuehrung` | Führt Treuhandkonto, Soll-Ist, Belege, Vorschüsse und Kassenbuch. |
| `zvg-berichtswesen-gericht` | Erstellt Besitzerlangungsbericht, Sachstandsbericht, Monatsnotiz und Gerichtsvorlage. |
| `zvg-rechnungslegung` | Erstellt Jahresrechnung, Schlussrechnung, Endabrechnung und Belegpaket. |
| `zvg-verteilungsplan-155` | Bereitet Verteilung der Nutzungen, Ausgaben, Gläubigerzahlungen und Gerichtskosten vor. |
| `zvg-glaeubiger-schuldner-kommunikation` | Formuliert klare Schreiben an Schuldner, Gläubiger, Mieter, Behörden und Gericht. |
| `zvg-raeumung-kuendigung` | Prüft Kündigung, Räumung, Schuldnerwohnräume, Mieterrechte und Eskalation. |
| `zvg-insolvenz-schnittstelle` | Koordiniert ZVG mit Insolvenzverfahren, IV, Absonderungsrechten und Massefragen. |
| `zvg-verkauf-versteigerung-schnittstelle` | Hält Schnittstelle zur Zwangsversteigerung, Werterhalt, Besichtigung und Erlöslogik. |
| `zvg-portal-recherche` | Recherchiert Zwangsversteigerungstermine im amtlichen ZVG-Portal und dokumentiert Suchparameter, Treffer und Grenzen. |
| `zvg-bieterangebot-bewertung` | Bewertet Versteigerungsobjekte und Bieterangebote mit Verkehrswert, geringstem Gebot, Lasten, Mietlage, Sanierung und Bietlimit. |
| `zvg-versteigerungsteilnahme` | Bereitet die Teilnahme am Versteigerungstermin mit Sicherheitsleistung, Legitimation, Bietstrategie und Nachbereitung vor. |
| `zvg-simulation-training` | Simuliert einen kompletten Zwangsverwaltungstag mit echten Fallakten-Artefakten. |
| `zvg-quality-gate` | Prüft Beschluss, Konto, Rent Roll, Belege, Berichte, Verteilung und Rollen. |

## Typische Workflows

- Bestellung -> Beschlusscheck -> Besitzerlangung -> Mieterinformation -> Treuhandkonto.
- Rent Roll -> Mieteinzug -> Rückstände -> Mahnung/Klage -> Gerichtssachstand.
- Objektmangel -> Gefahrensicherung -> Versicherung -> Kostenvoranschlag -> Gerichtsvorlage.
- Kontoauszug -> Buchführung -> Jahresrechnung -> Belegpaket -> Auskunft.
- Überschuss -> Rücklagencheck -> § 155 ZVG-Verteilungsplan -> Auszahlung.
- Aufhebung -> Schlussrechnung -> Endabrechnung -> Übergabe.
- ZVG-Portal -> Trefferprotokoll -> Gutachten/Grundbuch/Mietlage -> Bieterangebot -> Bietlimit -> Termincheck.

## Enthaltene Vorlagen

- `assets/templates/zvg-objektkarte.md` - Objektkarte für ZVG-Verfahren
- `assets/templates/bestellungs-und-beschlagnahmecheck.md` - Beschluss- und Beschlagnahmeprüfung
- `assets/templates/besitzuebernahme-protokoll.md` - Besitzübernahme und Objektaufnahme
- `assets/templates/mieterliste-rent-roll.md` - Rent Roll und Vertragsübersicht
- `assets/templates/mieteinzug-rueckstaende.md` - Mieteinzug und Rückstandsmatrix
- `assets/templates/betriebskosten-hausgeld.md` - Betriebskosten und Hausgeld
- `assets/templates/instandhaltung-gefahrensicherung.md` - Instandhaltung und Verkehrssicherung
- `assets/templates/versicherung-und-lasten.md` - Versicherungs- und Lastenregister
- `assets/templates/konto-kassenbuch.md` - Treuhandkonto und Kassenbuch
- `assets/templates/monatsbericht-gericht.md` - Monats- oder Sachstandsbericht ans Gericht
- `assets/templates/rechnungslegung.md` - Jahresrechnung, Schlussrechnung und Endabrechnung
- `assets/templates/verteilungsplan-155.md` - Verteilungsplan nach § 155 ZVG
- `assets/templates/schuldner-glaeubiger-kommunikation.md` - Kommunikationsbausteine
- `assets/templates/raeumung-kuendigung.md` - Räumungs- und Kündigungsprüfung
- `assets/templates/insolvenz-schnittstelle.md` - Schnittstelle ZVG und Insolvenzverfahren
- `assets/templates/zvg-portal-rechercheprotokoll.md` - ZVG-Portal-Suche und Trefferprotokoll
- `assets/templates/bieterangebot-bewertung.md` - Bewertung von Versteigerungsangeboten und Bietlimit
- `assets/templates/versteigerungsteilnahme-checkliste.md` - Terminvorbereitung für Bieter
- `assets/templates/schlussrechnung-aufhebung.md` - Aufhebung, Schlussrechnung und Endabrechnung
- `assets/templates/simulationstag.md` - Simulierter ZVG-Arbeitstag
- `assets/templates/quality-gate.md` - ZVG-Vorversandprüfung

## Sicherheitsleitplanken

- Keine gerichtliche, wirtschaftliche oder steuerliche Entscheidung ohne menschliche Letztprüfung.
- Keine echten Mandatsgeheimnisse, Bankzugänge, Gerichtslogins, beA-Zertifikate, Registerzugänge oder personenbezogene Daten in nicht freigegebene Systeme.
- Alle Fristen, Forderungen, Zahlungsflüsse, Tabellenvermerke, Anfechtungsansprüche und Verteilungsrechnungen müssen belegbar sein.
- Wo amtliche Onlinequellen abgefragt werden, werden Abrufdatum, URL, Treffer und Grenzen der Recherche dokumentiert.
- Simulationen sind deutlich als Simulation zu kennzeichnen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Zwangsverwaltung ZVG-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspla... |
| `zvg-aktenanlage-objektcockpit` | Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen... |
| `zvg-berichtswesen-gericht` | Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG... |
| `zvg-besitzuebernahme` | Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535... |
| `zvg-bestellung-beschlagnahme` | Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Ano... |
| `zvg-betriebskosten-hausgeld` | Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten prüfen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben § 16 WEG Hausgeld B... |
| `zvg-bieterangebot-bewertung` | Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherhei... |
| `zvg-glaeubiger-schuldner-kommunikation` | Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pfli... |
| `zvg-insolvenz-schnittstelle` | Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klaeren. Normen § 165 InsO Absonde... |
| `zvg-instandhaltung-sicherung` | Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht B... |
| `zvg-kommandocenter` | Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen Workflow starten. Normen §§ 146-161 ZVG Kernvorschriften. Prüfraster Bestellung Be... |
| `zvg-konten-kassenfuehrung` | Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. P... |
| `zvg-miet-und-pachtverwaltung` | Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§... |
| `zvg-mieteinzug-rueckstaende` | Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kündigung § 286 BG... |
| `zvg-oeffentliche-lasten` | Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10... |
| `zvg-portal-recherche` | Recherche von Zwangsversteigerungsterminen im amtlichen ZVG-Portal für Investoren und Gläubiger. Anwendungsfall Mandant sucht Versteigerungsobjekte oder Gläubiger will Terminuebersicht. Normen §§ 87 ff. ZVG Versteigerungstermin § 74a ZVG... |
| `zvg-quality-gate` | Quality Gate für Zwangsverwaltung vor Versand oder Rechnungslegung. Anwendungsfall Bericht Rechnungslegung oder Verteilungsplan soll ans Gericht versandt werden und muss vorher geprüft werden. Normen § 161 ZVG Rechnungslegung § 155 ZVG E... |
| `zvg-raeumung-kuendigung` | Räumung Kündigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kündigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB fristlose Kündigung § 573... |
| `zvg-rechnungslegung` | Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 1... |
| `zvg-simulation-training` | Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoa... |
| `zvg-verkauf-versteigerung-schnittstelle` | Schnittstelle zwischen laufender Zwangsverwaltung und dem Zwangsversteigerungsverfahren. Anwendungsfall Zwangsverwaltung soll aufgehoben werden weil Zwangsversteigerung angeordnet wird oder laeuft. Normen § 153b ZVG Aufhebung der Verwalt... |
| `zvg-versicherungen-gefahren` | Versicherungsschutz und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Gebaeudeversicherung ist nicht bezahlt oder Schadenfall ist eingetreten. Normen § 154 ZVG Erhaltungspflicht § 823 BGB Verkehrssicherungspflicht VVG Versich... |
| `zvg-versteigerungsteilnahme` | Vorbereitung der Teilnahme am Zwangsversteigerungstermin für Gläubiger oder Bieter. Anwendungsfall Mandant will an Versteigerungstermin teilnehmen und benoetigt vollständige Vorbereitung. Normen §§ 87 ff. ZVG Termin § 74a ZVG geringstes... |
| `zvg-verteilungsplan-155` | Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen §... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
