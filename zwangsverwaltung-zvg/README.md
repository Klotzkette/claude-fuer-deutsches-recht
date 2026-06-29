# ZVG-Zwangsverwaltung - Verwalter-Cockpit

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`zwangsverwaltung-zvg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg-werkstatt.md" download><code>zwangsverwaltung-zvg-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg-schnellstart.md" download><code>zwangsverwaltung-zvg-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-zwangsverwaltung-friedrichshoefe-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-friedrichshoefe-berlin.zip) (Zwangsverwaltung Büro- und Geschäftshaus "Friedrichshöfe"); [`testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip) (Zwangsverwaltung ZVG – Mietshaus Parkstraße 18, Leipzig); [`testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip) (ZVG-Versteigerung Eppendorf-Altbau) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Verwaltungsakt anfechten und vorlaeufigen Rechtsschutz erreichen.
Technischer Plugin-Name: `zwangsverwaltung-zvg`.

Großes freistehendes Plugin für Zwangsverwalter nach ZVG und ZwVwV sowie für die Schnittstelle zur Zwangsversteigerung. Abgebildet sind Bestellung, Beschlagnahme, Besitzerlangung, Objektaufnahme, Miet- und Pachtverwaltung, Mieteinzug, Betriebskosten, Versicherungen, öffentliche Lasten, Treuhandkonto, Berichtswesen, Rechnungslegung, Verteilung, Räumungs- und Besitzkonflikte, ZVG-Portal-Recherche, Bieterangebotsbewertung und Teilnahme an Versteigerungsterminen.

**Freistehend:** Dieses Plugin enthält eigene Skills, Vorlagen, Quellenhinweise, Vorschau und Testakte. Es verweist nicht auf andere Plugins als Voraussetzung.

## Installation

1. ZIP aus dem Release herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `zwangsverwaltung-zvg.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Starte das ZVG-Kommandocenter für dieses Mietshaus.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

#

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

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenanlage-objektcockpit` | Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen... |
| `anschluss-routing` | Anschluss-Routing für Zwangsverwaltung ZVG: wählt den nächsten Spezial-Skill nach Engpass (Beschwerde gegen Anordnung, Anordnungsbeschluss, Verwalterbericht, Mietsachen-Akte), dokumentiert Router-Entscheidung mit Begründung. |
| `berichte-beschlagnahme-mietverwaltung-besitz` | Berichte: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `berichtswesen-besitzuebernahme-bestellung` | Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG... |
| `beschlagnahme-fristen-form-und-zustaendigkeit` | Beschlagnahme: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `beschlagnahme-mietverwaltung-start` | Beschlagnahme, Besitzergreifung und Mietverwaltung zum Verfahrensstart: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Zwangsverwaltung Zvg. |
| `beschlagnahme-oeffentliche-lasten` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Zwangsverwaltung Zvg. |
| `besitz-dokumentenmatrix-und-lueckenliste` | Besitz: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `besitzuebernahme` | Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535... |
| `bestellung-beschlagnahme` | Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Ano... |
| `betriebskosten-hausgeld-bieterangebot` | Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten prüfen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben § 16 WEG Hausgeld B... |
| `bieterangebot-bewertung` | Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherhei... |
| `bieterangebote-mieten-oeffentliche` | Bieterangebote: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dokumente-intake` | Dokumentenintake für Zwangsverwaltung ZVG: sortiert Anordnungsbeschluss, Verwalterbericht, Mietsachen-Akte, prüft Datum, Absender, Frist und Beweiswert (Mieteinnahmen, Reparaturen-Belege); markiert Lücken; berücksichtigt Mandatsgeheimnis... |
| `einstieg-routing` | Einstieg, Triage und Routing für Zwangsverwaltung ZVG: ordnet Rolle (Gläubiger, Schuldner Eigentümer, Zwangsverwalter), markiert Frist (Beschwerde gegen Anordnung), wählt Norm (ZVG §§ 146 ff., BGB §§ 1135 ff. Pflichten) und Zuständigkeit... |
| `gate-fehlerkatalog` | Gate Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand |
| `glaeubiger-schuldner-kommunikation` | Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pfli... |
| `insolvenz-schnittstelle-instandhaltung` | Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klären. Normen § 165 InsO Absonder... |
| `instandhaltung-sicherung` | Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht B... |
| `kommandocenter` | Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen starten. Normen §§ 146-161 ZVG Kernvorschriften. Prüfraster Bestellung Beschlagnah... |
| `konten-kassenfuehrung-miet-pachtverwaltung` | Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. P... |
| `miet-und-pachtverwaltung` | Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§... |
| `mieteinzug-rueckstaende` | Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kündigung § 286 BG... |
| `mieten-risikoampel-und-gegenargumente` | Mieten: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `oeffentliche-lasten` | Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10... |
| `oeffentliche-mandantenkommunikation-entscheidungsvorlage` | Oeffentliche: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Zwangsverwaltung ZVG: stimmt Adressat (Gläubiger, Schuldner Eigentümer, Zwangsverwalter), Frist (Beschwerde gegen Anordnung) und Form auf den Zweck ab — typische Outputs: Anordnungsantrag, Verwalterbericht, Erinnerung geg... |
| `portal-quellenkarte` | Portal Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quality-gate` | Quality Gate für Zwangsverwaltung vor Versand oder Rechnungslegung. Anwendungsfall Bericht Rechnungslegung oder Verteilungsplan soll ans Gericht versandt werden und muss vorher geprüft werden. Normen § 161 ZVG Rechnungslegung § 155 ZVG E... |
| `quality-recherche-rechnungslegung` | Quality: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `quellen-livecheck` | Quellen-Live-Check für Zwangsverwaltung ZVG: prüft Normen (ZVG §§ 146 ff., BGB §§ 1135 ff. Pflichten) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht Vollstreckungsgericht und Quellenhygiene nach refer... |
| `raeumung-kuendigung` | Räumung Kündigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kündigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB fristlose Kündigung § 573... |
| `recherche-quality-gate-raeumung` | Recherche von Zwangsversteigerungsterminen im amtlichen ZVG-Portal für Investoren und Gläubiger. Anwendungsfall Mandant sucht Versteigerungsobjekte oder Gläubiger will Terminuebersicht. Normen §§ 87 ff. ZVG Versteigerungstermin § 74a ZVG... |
| `recherche-zahlen-schwellen-und-berechnung` | Recherche: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `rechnungslegung-internationaler-bezug-und-schnittstellen` | Rechnungslegung: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `rechnungslegung-simulation-training` | Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 1... |
| `simulation-training` | Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoa... |
| `spezial-gate-red-team-und-qualitaetskontrolle` | Gate: Red-Team und Qualitätskontrolle. |
| `spezial-portal-livequellen-und-rechtsprechungscheck` | Portal: Livequellen- und Rechtsprechungscheck. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Zwangsverwaltung ZVG-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Do... |
| `treuhandkonto-versteigerung` | Treuhandkonto: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Zwangsverwaltung ZVG: trennt fehlende Tatsachen von fehlenden Belegen (Anordnungsbeschluss, Verwalterbericht, Mietsachen-Akte), nennt pro Lücke Beweisthema, Beschaffungsweg (Amtsgericht Vollstreckungsger... |
| `verkauf-versteigerung-schnittstelle` | Schnittstelle zwischen laufender Zwangsverwaltung und dem Zwangsversteigerungsverfahren. Anwendungsfall Zwangsverwaltung soll aufgehoben werden weil Zwangsversteigerung angeordnet wird oder laeuft. Normen § 153b ZVG Aufhebung der Verwalt... |
| `versicherungen-gefahren-zvg` | Versicherungsschutz und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Gebaeudeversicherung ist nicht bezahlt oder Schadenfall ist eingetreten. Normen § 154 ZVG Erhaltungspflicht § 823 BGB Verkehrssicherungspflicht VVG Versich... |
| `versteigerung-tatbestand-beweis-und-belege` | Versteigerung: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `versteigerungsteilnahme` | Vorbereitung der Teilnahme am Zwangsversteigerungstermin für Gläubiger oder Bieter. Anwendungsfall Mandant will an Versteigerungstermin teilnehmen und benoetigt vollständige Vorbereitung. Normen §§ 87 ff. ZVG Termin § 74a ZVG geringstes... |
| `versteigerungsteilnahme-mehrparteienkonflikt` | Versteigerungsteilnahme: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `verteilung-zwangsverwaltung-aktenanlage` | Verteilung: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `verteilungsplan-155` | Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen §... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Zwangsverwaltung Zvg. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Zwangsverwaltung Zvg. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zwangsverwaltung-erstpruefung-und-mandatsziel` | Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `zwvw-anordnung-zwangsverwaltung` | Bauleiter Anordnung Zwangsverwaltung ZVG: Gläubigerantrag, Anordnungsbeschluss, Verwalterbestellung. Prüfraster für Gläubiger und Eigentuemer im Zwangsverwaltung Zvg. |
| `zwvw-kostenrechnung-verwalter-spezial` | Spezialfall Kostenrechnung des Zwangsverwalters ZwVwV: Regelverguetung, Mehrverguetung, Auslagen. Prüfraster für Gläubiger und Vollstreckungsgericht im Zwangsverwaltung Zvg. |
| `zwvw-mietverhaeltnis-bestand-leitfaden` | Leitfaden Bestand der Mietverhaeltnisse in Zwangsverwaltung § 152 ZVG: Eintritt des Verwalters, Mietzahlungen, Kuendigung. Prüfraster für Mieter und Verwalter im Zwangsverwaltung Zvg. |
| `zwvw-versteigerung-vs-verwaltung-spezial` | Spezialfall Zusammenspiel Zwangsversteigerung und Zwangsverwaltung: Aufhebung, Vorrang, Auskehrung: Prüfraster für Gläubiger und Schuldner. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
