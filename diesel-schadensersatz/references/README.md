# Fachquellen und Referenzen

[Plugin-README](../README.md) | [Repository-Start](../../README.md) | [Download-Index](../../ASSET_INDEX.md) | [Werkzeuge](../tools/README.md) | [Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/diesel-schadensersatz.zip)

Diese Dateien bilden die fachliche Wissens- und Quellenebene des Dieselgate-Plugins und werden unmittelbar mit dem installierbaren Plugin ausgeliefert.

Der kuratierte Bestand kontrolliert amtliche Primärquellen, den Normstand 2026, risikoreiche Skill-Zuordnungen und bekannte Fehlformeln zu `C-100/21`, Software-Update/Eigenschaden, § 852 BGB, § 291 ZPO, Nutzungsschätzung, Hilfsantrag, Tatbestandsberichtigung, Restwertvergleich, elektronischer Form, Musterfeststellung, Minderwert und Zuständigkeit. Das lokale [Rechtsstands-Cockpit](../tools/rechtsstand-monitor.py) ergänzt die zwingende Volltextprüfung; es ersetzt sie nicht.

## Rechtsprechung

| Datei | Zweck |
|---|---|
| [gepruefte-anker-dieselgate.md](./gepruefte-anker-dieselgate.md) | kuratierte EuGH-, BGH- und OLG/KG-Kernanker mit Arbeitsregeln |
| [diesel-rechtsprechung-2021-2026.md](./diesel-rechtsprechung-2021-2026.md) | lesbarer Fünfjahreskorpus mit BGH, EuGH, OLG/KG, LG, Verwaltungsbezug, Gegenlinien und Quellenrängen |
| [diesel-rechtsprechung-2021-2026.json](./diesel-rechtsprechung-2021-2026.json) | 135 strukturierte Entscheidungen/Statusakten mit Verifikationsstatus und Verwendungsgrenze |
| [diesel-rechtsprechung-fuenfjahre-ergaenzungen.json](./diesel-rechtsprechung-fuenfjahre-ergaenzungen.json) | redaktionell verifizierte Ergänzungsschicht für den reproduzierbaren Korpus-Build |
| [diesel-rechtsprechung-obergerichte.md](./diesel-rechtsprechung-obergerichte.md) | lesbare Leitlinien-, Status- und Gerichtsübersicht |
| [diesel-rechtsprechung-obergerichte.json](./diesel-rechtsprechung-obergerichte.json) | strukturierte Obergerichtsmatrix für Filter und Validatoren |
| [leitentscheidungen-anker.md](./leitentscheidungen-anker.md) | kompakter Ankerkatalog für Diesel-, Prozess- und Behördenfragen |

## EA288

| Datei | Zweck |
|---|---|
| [ea288-rechtsprechung-instanzen.md](./ea288-rechtsprechung-instanzen.md) | lesbare anonymisierte Instanzsammlung aus Nutzermaterial |
| [ea288-rechtsprechung-instanzen.json](./ea288-rechtsprechung-instanzen.json) | maschinenlesbarer EA288-Korpus |
| [ea288-argumentationslinien.md](./ea288-argumentationslinien.md) | Darlegungslast, Parallelvortrag, Technikbezug, Quote und Rügefragen |

## Behörden und Quellenkontrolle

| Datei | Zweck |
|---|---|
| [behoerden-und-praxisquellen-diesel.md](./behoerden-und-praxisquellen-diesel.md) | KBA-, GovData- und Kanzleipublikationen mit Verwendungsgrenzen |
| [bea-versandfertig.md](./bea-versandfertig.md) | ERVV/ERVB, Signatur, Eingangskontrolle, NRW-Empfehlungen, Dateinamen und Anlagenintegrität |
| [rechtsstand-2026-gesetzgebung.md](./rechtsstand-2026-gesetzgebung.md) | Zuständigkeits- und Rechtsmittelgrenzen, Übergangsrecht, eCoC, Typgenehmigungsrahmen und Euro 7 mit amtlichen Quellen |
| [zitierweise.md](./zitierweise.md) | Mindeststandard für Normen, Entscheidungen und frei zugängliche Quellen |
| [quellenhygiene.md](./quellenhygiene.md) | kurze Stoppliste gegen Fehlzitate und Scheinpräzision |

## Bedienung, Methodik und Schnittstellen

| Datei | Zweck |
|---|---|
| [bedienfuehrung-workflows.md](./bedienfuehrung-workflows.md) | Skill-Router, Startkarte, Menü, Ampel und Übergabestandard |
| [promptketten-schnelllauf.md](./promptketten-schnelllauf.md) | modellneutraler Schnelllauf, minimaler Kontext, verlustfreie Arbeitsstände und einheitliches Freigabegate für Opus 5 und Fable 5 |
| [juristische-schreib-und-argumentationsarchitektur.md](./juristische-schreib-und-argumentationsarchitektur.md) | verbindliche Tatsachen-, Beweis-, Subsumtions-, Gegenargument- und Freigabestruktur für alle 21 Skills |
| [methodik-buergerliches-recht.md](./methodik-buergerliches-recht.md) | Anspruchsaufbau, Auslegung, Beweislast, Verjährung und Selbstprüfung |
| [schnittstellenprofile.md](./schnittstellenprofile.md) | Eingangsprofile, Fallakte, DMS-Register und MCP-/Gateway-Planung |

## Abfragewerkzeuge

Die drei Korpusabfragen und das Rechtsstands-Cockpit im Quellenpaket und Plugin arbeiten ohne Drittanbieterpakete. Im vollständigen Zielrepository werden sie aus dessen Wurzel mit der in [`tools/README.md`](../tools/README.md#reproduzierbare-laufzeitumgebung) beschriebenen `.venv` ausgeführt:

```bash
.venv/bin/python diesel-schadensersatz/tools/diesel-rechtsprechung-query.py --stats
.venv/bin/python diesel-schadensersatz/tools/diesel-fuenfjahre-query.py --arbeitsset --query EA288
.venv/bin/python diesel-schadensersatz/tools/ea288-corpus-query.py --limit 0 --format json
.venv/bin/python diesel-schadensersatz/tools/rechtsstand-monitor.py --strict --format markdown
```

Im entpackten Plugin- oder Quellenpaket werden die Befehle aus dessen Wurzel ausgeführt:

```bash
python3 tools/diesel-rechtsprechung-query.py --stats
python3 tools/diesel-fuenfjahre-query.py --arbeitsset --query EA288
python3 tools/ea288-corpus-query.py --limit 0 --format json
python3 tools/rechtsstand-monitor.py --strict --format markdown
```

Im vollständigen Zielrepository kann zusätzlich die allgemeine Plugin-Struktur geprüft werden:

```bash
node scripts/validate-plugin-structure.mjs
```

Die Filterausgabe ersetzt keine Volltextkontrolle. Status, Folgeentwicklung, technische Vergleichbarkeit und Quellenart bleiben vor jeder Verwendung zu prüfen.
