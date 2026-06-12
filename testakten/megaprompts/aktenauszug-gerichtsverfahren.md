# Megaprompt: aktenauszug-gerichtsverfahren

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `aktenauszug-gerichtsverfahren`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Aktenauszüge zivilgerichtlicher Verfahren: ordnet Rolle (Mandant, Gegenpartei, Gericht)…
2. **aktenauszug-erstellen** — Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze oder PDFs und will strukturierten Aktenauszug erstellen. Sechs …
3. **aktenauszug-strukturpruefung-akzg-bauleiter** — Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprach…
4. **aktenauszug-verfahrensidentifikation-gericht** — Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Str…
5. **anlagenverzeichnis-extrakt** — Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung K…
6. **anwaltsschriftsatz-stilrichtlinie** — Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklat…
7. **arbeitsgerichtsverfahren-modus-terminkalender** — Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwo…
8. **beweismittel-gegenueberstellung** — Anwalt will Beweisangebote aller Parteien uebersichtlich gegenüberstellen: Zeugen Urkunden Sachverständige Parteivernehm…
9. **einleitungssatz-generator** — Aktenauszug braucht praegnanten Einleitungssatz: wer streitet mit wem worueber welche Hauptnorm. Juristisch praezise neu…
10. **fristen-und-terminkalender** — Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungs…
11. **neutralitaetspruefung** — Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markier…
12. **rechtsargumente-gegenueberstellung** — Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einre…
13. **sachverhaltschronologie** — Erstellt eine chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen: Vertragsschluss Vorfaelle vorg…
14. **schwerpunktthemen-identifikation-akten** — Anwalt braucht schnellen Überblick über drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten …
15. **sozialgerichtsverfahren-modus** — Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtser…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Aktenauszüge zivilgerichtlicher Verfahren: ordnet Rolle (Mandant, Gegenpartei, Gericht), markiert Frist (Akteneinsicht im laufenden Verfahren jederzeit), wählt Norm (§ 299 ZPO Akteneinsicht, § 130a ZPO eA-Übermittlung, § 169 GVG Öffentlichkeit) und Zuständigkeit (..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Aktenauszug Gerichtsverfahren** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `akten-mandantenkommunikation-entscheidungsvorlage` — Akten Mandantenkommunikation Entscheidungsvorlage
- `aktenauszug-erstellen` — Aktenauszug Erstellen
- `aktenauszug-strukturpruefung-akzg-bauleiter` — Aktenauszug Strukturpruefung Akzg Bauleiter
- `aktenauszug-tatbestand-beweis-und-belege` — Aktenauszug Tatbestand Beweis und Belege
- `aktenauszug-verfahrensidentifikation-gericht` — Aktenauszug Verfahrensidentifikation Gericht
- `akzg-aktenauszug-bauleiter` — Akzg Aktenauszug Bauleiter
- `akzg-multiparteienverfahren-konsolidierung-spezial` — Akzg Multiparteienverfahren Konsolidierung Spezial
- `akzg-vertraulichkeit-redaction-spezial` — Akzg Vertraulichkeit Redaction Spezial
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt` — Akzg Zeitstrahl Anlagenverzeichnis Extrakt
- `anlagenverzeichnis-extrakt` — Anlagenverzeichnis Extrakt
- `anwaltsschriftsatz-beweislast-beweismittel` — Anwaltsschriftsatz Beweislast Beweismittel
- `anwaltsschriftsatz-stilrichtlinie` — Anwaltsschriftsatz Stilrichtlinie
- `arbeitsgerichtsverfahren-modus-terminkalender` — Arbeitsgerichtsverfahren Modus Terminkalender
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Aktenauszug Gerichtsverfahren sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `aktenauszug-erstellen`

_Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze oder PDFs und will strukturierten Aktenauszug erstellen. Sechs Bausteine: Verfahrensidentifikation Einleitungssatz Absatz-Zusammenfassung Sachverhaltschronologie Verfahrenschronologie Parteivortrag-Tabelle Beweis- und Rechtsargumente. Norme..._

# Aktenauszug Erstellen — Hauptworkflow

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Leitidee

Wer ein Gerichtsverfahren schnell erfassen muss — sei es beim Mandatswechsel, bei der Einarbeitung eines neuen Sachbearbeiters oder bei der Vorbereitung auf eine mündliche Verhandlung — benötigt einen strukturierten Überblick. Dieser Skill nimmt die gesamte Akte entgegen und erzeugt einen vollständigen Aktenauszug mit allen sechs Bausteinen.

## Triage zu Beginn — kläre vor Erstellung des Aktenauszugs

1. Welche Verfahrensart liegt vor? (Zivilprozess, Arbeitsgericht, Verwaltungsgericht, Sozialrecht, Strafprozess)
2. In welcher Instanz befindet sich das Verfahren? (Erstinstanz, Berufung, Revision)
3. Liegen alle wesentlichen Schriftsätze vor oder nur Teilakten?
4. Gibt es bereits einen Termin, dessen Vorbereitung im Vordergrund steht?
5. Soll der Aktenauszug intern (anwaltlich) oder zur Übergabe an Mandant dienen?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen (Prozessrecht)

- §§ 128-134 ZPO — Schriftliches und mündliches Verfahren, Schriftsätze
- §§ 253-261 ZPO — Klageerhebung und Verfahrenseinleitung
- §§ 355-455 ZPO — Beweisaufnahme (Sachverstaendige, Zeugen, Augenschein, Urkunden)
- §§ 495a, 522, 540 ZPO — Vereinfachtes Verfahren, Berufungsverwerfung, Berufungsurteil
- §§ 704-945 ZPO — Zwangsvollstreckung (Abschnitt relevant für Vollstreckungstitel in Akte)
- § 91a ZPO — Kosten bei Erledigterklärung
- § 139 ZPO — Materielle Prozessleitung, richterliche Hinweispflicht

## Aktuelle Rechtsprechung zum Aktenauszug und Verfahrensrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Voraussetzungen

- Gerichtliche Akte oder wesentliche Teile davon (PDF, Word, maschinenlesbar)
- Optional: Inhaltsverzeichnis der Akte
- Optional: Hinweis auf die Verfahrensart (Zivil, Straf, Verwaltung, Arbeit, Sozial)

## Sechs Bausteine des Aktenauszugs

### Baustein 1 — Verfahrensidentifikation

Gericht, Kammer/Senat, Aktenzeichen, Streitwert, Parteien mit Anwälten, Instanz, Verfahrensart.

### Baustein 2 — Einleitungssatz

Ein bis zwei Sätze, die den Kern des Rechtsstreits nennen: Wer streitet mit wem worüber, welche Hauptnorm ist einschlägig.

### Baustein 3 — Zusammenfassung (Absatz)

Acht bis zehn Sätze: Hintergrund, Streitstand, prozessuale Lage, anstehende Verfahrenshandlungen.

### Baustein 4 — Sachverhaltschronologie

Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen. Datum fettgedruckt vorangestellt.

### Baustein 5 — Verfahrenschronologie

Chronologische Bullet-Liste der prozessualen Schritte. Fristen und Termine werden hervorgehoben.

### Baustein 6 — Tabellen (Parteivortrag / Beweismittel / Rechtsargumente)

Drei separate Tabellen im Markdown-Format mit Spalten für Klägerseite und Beklagtenseite.

## Schritt-für-Schritt-Workflow

1. **Akte sichten** — Inhaltsverzeichnis oder Seitenstruktur erfassen; fehlende Seiten markieren
2. **Verfahrensart bestimmen** — aktiviere passenden Modus-Skill (Zivil/ArbG/VerwG/Sozial/Straf)
3. **Verfahrensidentifikation extrahieren** (→ Skill `verfahrensidentifikation`)
4. **Einleitungssatz formulieren** (→ Skill `einleitungssatz-generator`)
5. **Zusammenfassungsabsatz schreiben** (→ Skill `verfahrenszusammenfassung-absatz`)
6. **Sachverhalt chronologisch ordnen** (→ Skill `sachverhaltschronologie`)
7. **Verfahrensschritte chronologisch ordnen** (→ Skill `verfahrenschronologie`)
8. **Fristen hervorheben** (→ Skill `fristen-und-terminkalender`) — alle Notfristen mit ⚠️
9. **Parteivortrag gegenüberstellen** (→ Skill `parteivortrag-gegenueberstellung`)
10. **Beweismittel tabellarisch erfassen** (→ Skill `beweismittel-gegenueberstellung`)
11. **Rechtsargumente tabellarisch erfassen** (→ Skill `rechtsargumente-gegenueberstellung`)
12. **Neutralitätsprüfung** (→ Skill `neutralitaetspruefung`)
13. **Strukturprüfung** (→ Skill `aktenauszug-strukturpruefung`)

## Entscheidungsbaum — Verfahrensart

```
Liegt Akte vor?
 → Ja: Verfahrensart prüfen
 → Arbeitsgericht? → Skill arbeitsgerichtsverfahren-modus aktivieren
 → Verwaltungsgericht? → Skill verwaltungsprozess-modus aktivieren
 → Strafgericht? → Skill strafprozess-modus aktivieren
 → Sozialgericht? → Skill sozialgerichtsverfahren-modus aktivieren
 → Zivilgericht (LG/AG/OLG)? → Skill zivilprozess-modus aktivieren
 → Nein: Fehlende Unterlagen beim Mandanten anfordern; Notfrist prüfen
```

## Output-Format

```markdown
### Aktenauszug — [Aktenzeichen]

## Verfahrensidentifikation
...

## Einleitungssatz
...

## Zusammenfassung
...

## Sachverhaltschronologie
- **TT.MM.JJJJ** Beschreibung
- **TT.MM.JJJJ** Beschreibung

## Verfahrenschronologie
- **TT.MM.JJJJ** Beschreibung
- ⚠️ **TT.MM.JJJJ — FRIST:** Beschreibung

## Parteivortrag

| Punkt | Klägerseite | Beklagtenseite |
|---|---|---|

## Beweismittel

| Beweismittel | Klägerseite | Beklagtenseite |
|---|---|---|

## Rechtsargumente

| Aspekt | Klägerseite | Beklagtenseite |
|---|---|---|
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — strukturierter Aktenauszug für Gericht | Vollformat nach den sechs Bausteinen unten |
| Variante A — nur interne Einarbeitung noetig | Kurzform ohne Verfahrenschronologie; Bausteine 1-3 genuegen |
| Variante B — Eilsache; Zeit fehlt für vollstaendigen Auszug | Einleitungssatz + Sachverhaltschronologie priorisieren; Rest nachliefern |
| Variante C — Parteivertreter hat bereits Zusammenfassung geliefert | Kritische Pruefung und Ergaenzung statt Neuerstellung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template Übergabevermerk (intern)

**Adressat:** Sachbearbeiter / aufnehmender Anwalt — Tonfall: sachlich-juristisch

```
ÜBERGABEVERMERK — [AKTENZEICHEN]
Bearbeiter bisher: [NAME]
Stand: [DATUM]

Verfahren: [KURZBEZEICHNUNG]
Nächste Frist: [DATUM + BEZEICHNUNG]
Nächster Termin: [DATUM + ORT]
Offene Aufgaben: [LISTE]

Besonderheiten: [z.B. Beweissicherungsantrag gestellt, SV noch nicht bestellt]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Qualitätsgrundsätze

- Keine Erfolgsprognose
- Neutrale Sprache ohne Wertung
- Alle Fristen und Termine hervorgehoben
- Keine KI-Terminologie im Output

## Hinweis

Der Aktenauszug ersetzt nicht die eigene Aktenlektüre. Er ist ein strukturiertes Arbeits- und Kommunikationsmittel für den anwaltlichen Alltag und bedarf der Prüfung durch den verantwortlichen Rechtsanwalt.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- BGH VII ZB 36/20: ersatzlos entfernt (Entscheidung nicht auffindbar auf dejure.org oder bundesgerichtshof.de; NJW-RR 2022, 1350 konnte keinem BGH VII ZB 36/20 zugeordnet werden)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 KSchG
- § 80 VwG
- § 86b SGG
- § 74 VwG
- § 124 VwG
- § 64 ArbGG
- § 72 ArbGG
- § 132 VwG
- § 123 VwG
- § 103 SGG
- § 151 SGG
- § 66 ArbGG

### Leitentscheidungen

- BGH VII ZB 36/20
- BGH VI ZR 146/19
- BGH VI ZR 84/19
- BGH VI ZR 396/18
- BGH VII ZR 131/13

---

## Skill: `aktenauszug-strukturpruefung-akzg-bauleiter`

_Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Prüfraster Bausteine-Vollständigkeit Fristen-Markierung Neutralitaets-Check Sprach-Qualitaet. Output Prüfergebnis-Bericht Lueckenliste Verbesserung..._

# Aktenauszug — Strukturprüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — Kläre vor der Prüfung

1. Für welche Verfahrensart wurde der Aktenauszug erstellt? (Zivil/Arbeit/Verwaltung/Sozial/Straf)
2. Ist der Aktenauszug als intern-anwaltlicher Vermerk oder als Übergabedokument konzipiert?
3. Steht ein konkreter Termin oder eine Frist bevor, die besonders zu prüfen ist?

## Zentrale Normen

- § 128 ZPO — Muendliche Verhandlung; § 128a ZPO — Ton-/Bildübertragung
- § 139 ZPO — Materielle Prozessleitung (Hinweispflicht des Gerichts)
- § 253 ZPO — Inhalt der Klageschrift (Mindestinhalt als Vergleichsmassstab)
- § 495a ZPO — Vereinfachtes Verfahren unter 600 EUR
- §§ 355-414 ZPO — Beweisaufnahme (Zeugenbeweis, Sachverständigenbeweis, Augenschein)

## Rechtsprechung zu Vollstaendigkeit und Ordnung der Akte

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfcheckliste

### Baustein 1 — Verfahrensidentifikation

- [ ] Gericht und Kammer angegeben
- [ ] Aktenzeichen angegeben
- [ ] Instanz und Verfahrensart angegeben
- [ ] Streitwert angegeben (oder als unbekannt markiert)
- [ ] Alle Parteien mit Prozessbevollmächtigten aufgeführt

### Baustein 2 — Einleitungssatz

- [ ] Ein bis zwei Sätze vorhanden
- [ ] Wer streitet mit wem worüber benannt
- [ ] Hauptnorm genannt
- [ ] Keine Wertung enthalten

### Baustein 3 — Zusammenfassung

- [ ] Acht bis zehn Sätze vorhanden
- [ ] Hintergrund dargestellt
- [ ] Aktueller Verfahrensstand benannt
- [ ] Nächste Verfahrenshandlung benannt
- [ ] Keine Wertung / Prognose enthalten

### Baustein 4 — Sachverhaltschronologie

- [ ] Chronologisch sortiert
- [ ] Datum fettgedruckt vorangestellt
- [ ] Wesentliche außerprozessuale Ereignisse vollständig
- [ ] Fundstellen angegeben
- [ ] Keine prozessualen Schritte enthalten

### Baustein 5 — Verfahrenschronologie

- [ ] Chronologisch sortiert
- [ ] Alle prozessualen Schritte erfasst
- [ ] Fristen hervorgehoben (Präfix ⚠️ FRIST)
- [ ] Fristentabelle vorhanden
- [ ] Keine außerprozessualen Ereignisse enthalten

### Baustein 6 — Tabellen

**Parteivortrag:**
- [ ] Tabelle mit zwei Spalten (Kläger / Beklagter)
- [ ] Alle wesentlichen Streitpunkte als Zeilen
- [ ] Fundstellen angegeben

**Beweismittel:**
- [ ] Alle angebotenen Beweismittel erfasst
- [ ] Beweisthema je Beweismittel angegeben
- [ ] Anlagenbezeichnung angegeben

**Rechtsargumente:**
- [ ] Anspruchsgrundlagen beider Seiten erfasst
- [ ] Einwendungen und Einreden erfasst
- [ ] Verjährungsthema behandelt (falls relevant) — §§ 195-218 BGB
- [ ] Rechtsprechung mit Aktenzeichen angegeben

## Qualitätsgrundsätze

- [ ] Neutralitätsprüfung bestanden (keine Wertungen, keine Prognosen)
- [ ] Keine verbotenen Begriffe (keine KI-Terminologie)
- [ ] Fristen an prominenter Stelle (Fristenbox oder Fristentabelle am Anfang)
- [ ] Klare Markdown-Gliederung mit Überschriften

## Ergebnis-Format

```markdown

## Strukturprüfung — Ergebnis

| Baustein | Status | Anmerkung |
|---|---|---|
| Verfahrensidentifikation | vollstaendig | — |
| Einleitungssatz | vollstaendig | — |
| Zusammenfassung | unvollstaendig | Nächste Verfahrenshandlung fehlt |
| Sachverhaltschronologie | vollstaendig | — |
| Verfahrenschronologie | vollstaendig | — |
| Parteivortrag-Tabelle | vollstaendig | — |
| Beweismittel-Tabelle | unvollstaendig | B-Anlagen nicht erfasst |
| Rechtsargumente-Tabelle | vollstaendig | — |

**Gesamtergebnis:** ÜBERARBEITUNG ERFORDERLICH
**Offene Punkte:** [Anzahl]
```

## Adressat und Tonfall

Adressat: Sachbearbeiter / Kanzleiintern — Tonfall: sachlich-juristisch, präzise Mängelangabe.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 KSchG
- § 80 VwG
- § 86b SGG
- § 74 VwG
- § 124 VwG
- § 64 ArbGG
- § 72 ArbGG
- § 132 VwG
- § 123 VwG
- § 103 SGG
- § 151 SGG
- § 66 ArbGG

### Leitentscheidungen

- BGH VII ZB 36/20
- BGH VI ZR 146/19
- BGH VI ZR 84/19
- BGH VI ZR 396/18
- BGH VII ZR 131/13

---

## Skill: `aktenauszug-verfahrensidentifikation-gericht`

_Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und Verfahrensart (Klage Eilverfahren Berufung Revision Beschwerde). Normen §§ 253 261 ZPO Klag..._

# Verfahrensidentifikation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Liegt die Klageschrift oder der Eröffnungsbeschluss vor? (Aktenzeichen, Parteien)
2. Sind die Prozessbevollmächtigten beider Seiten aus der Akte ersichtlich?
3. Wurde der Streitwert festgesetzt (Streitwertbeschluss) oder nur vorläufig angegeben?
4. Gibt es Streithelfer oder Nebenintervenienten?

## Zentrale Normen

- § 253 Abs. 2 Nr. 1 ZPO — Klageschrift muss Gericht, Parteien und Streitgegenstand bezeichnen
- § 261 Abs. 1 ZPO — Anhängigkeit mit Einreichung der Klage; Rechtshängigkeit mit Zustellung
- §§ 3-9 ZPO — Streitwert (Bewertung Klageantrag, Früchte, Zinsen, Kosten)
- § 63 GKG — Streitwertfestsetzung durch das Gericht; § 68 GKG — Streitwertbeschwerde
- §§ 66-74 ZPO — Streithelfer / Nebenintervention (Voraussetzungen, Rechte)

## Rechtsprechung zur Verfahrensidentifikation

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zu extrahierende Felder

### Gericht und Spruchkörper

- Gericht (vollständige Bezeichnung, z. B. Landgericht Frankfurt am Main)
- Kammer oder Senat (z. B. 3. Zivilkammer, 14. Senat)
- Aktenzeichen (z. B. 3 O 123/23)
- Instanz (Erste Instanz / Berufung / Revision / Beschwerde / Rechtsbeschwerde)

### Verfahrensart

- Ordentliches Klageverfahren (ZPO)
- Eilverfahren (einstweilige Verfügung § 935 ff. ZPO / einstweilige Anordnung)
- Berufungsverfahren (§ 511 ff. ZPO)
- Revisionsverfahren (§ 542 ff. ZPO)
- Strafverfahren (StPO)
- Verwaltungsverfahren (VwGO)
- Arbeitsgerichtsverfahren (ArbGG)
- Sozialgerichtsverfahren (SGG)
- Sonstiges (Beschwerde, PKH, Streitwertbeschwerde)

### Streitwert

- Festgesetzter Streitwert (soweit bekannt)
- Vorläufiger Streitwert (soweit Antrag gestellt)
- Gebührenstreitwert (sofern abweichend)

### Parteien

Für jede Partei:

| Feld | Inhalt |
|---|---|
| Bezeichnung | Kläger / Beklagter / Berufungskläger / Streithelfer etc. |
| Name / Firma | Vollständige Bezeichnung |
| Anschrift | Straße PLZ Ort |
| Gesetzliche Vertretung | (bei juristischen Personen) |
| Prozessbevollmächtigter | Kanzlei und Rechtsanwalt |
| Anschrift Bevollmächtigter | Straße PLZ Ort |

### Streithelfer / Nebenintervenienten

- Benennung der Partei, auf deren Seite der Streithelfer steht
- Eigene Bevollmächtigung wenn vorhanden

## Output-Vorlage

```

## Verfahrensidentifikation

**Gericht:** Landgericht [Stadt]
**Kammer:** [X]. Zivilkammer
**Aktenzeichen:** [AZ]
**Instanz:** Erste Instanz
**Verfahrensart:** Ordentliches Klageverfahren (ZPO)
**Streitwert:** [EUR oder "nicht festgesetzt"]

### Parteien

| Rolle | Partei | Anschrift | Prozessbevollmächtigter |
|---|---|---|---|
| Kläger | [Name] | [Adresse] | [Kanzlei / RA] |
| Beklagter | [Name] | [Adresse] | [Kanzlei / RA] |
```

## Hinweise

- Fehlende Felder werden als "nicht aus Akte ersichtlich" gekennzeichnet, nicht geschätzt.
- Bei mehreren Klägern oder Beklagten wird jede Person separat aufgeführt.
- Streithelfer werden gesondert unter der Hauptparteitabelle gelistet.
- Keine Bewertung der Parteibezeichnung (z. B. ob Kläger wirklich klagebefugt ist).

---

---

## Skill: `anlagenverzeichnis-extrakt`

_Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung Kurzbeschreibung Schriftsatz Blattangabe je Partei. Normen §§ 130 131 ZPO Schriftsatz-Anlagen. Prüfraster Vollständigkeit Fundstellen-Praezision Parteizuordnung. Output vollständ..._

# Anlagenverzeichnis-Extrakt

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Liegt ein vollständiges Inhaltsverzeichnis der Akte vor?
2. Sind alle Schriftsätze in der Akte? Welche fehlen?
3. Besteht Streit über Übergabe oder Vollständigkeit bestimmter Anlagen?
4. Ist ein Anlageregister für Gericht oder für Mandant gedacht?

## Zentrale Normen

- § 130 Nr. 5 ZPO — Inhalt des Schriftsatzes: Anlagen müssen bezeichnet werden
- § 131 ZPO — Bezugnahme auf beigefügte Schriftstücke als Anlagen; Verlesen bei Bedarf
- § 141 ZPO — Persönliches Erscheinen; Vorlage von Unterlagen durch Partei
- § 142 ZPO — Anordnung der Urkundenvorlage durch Gericht (richterliche Vorlageanordnung)
- § 422 ZPO — Vorlegungspflicht für Urkunden (Parteibesitz)
- § 432 ZPO — Anforderung von Urkunden durch das Gericht bei Behörden

## Rechtsprechung zu Anlagen und Schriftsatz-Bezugnahmen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anlagenbezeichnungen

### Klägerseite

- K 1, K 2, K 3 ... (K = Kläger)
- AST 1, AST 2 ... (Antragsteller in Eilverfahren)

### Beklagtenseite

- B 1, B 2, B 3 ... (B = Beklagter)
- AG 1, AG 2 ... (Antragsgegner in Eilverfahren)

### Sonstige

- GA 1, GA 2 ... (Gericht, z. B. Sachverständigengutachten)
- SV 1, SV 2 ... (Sachverständiger)

## Tabellenstruktur

```markdown
| Anlage | Inhalt (kurz) | Datum des Dokuments | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag vom TT.MM.JJJJ | TT.MM.JJJJ | Klageschrift | 12-18 |
| K 2 | Abnahmeprotokoll | TT.MM.JJJJ | Klageschrift | 19-21 |
| K 3 | Mängelrüge (Schreiben) | TT.MM.JJJJ | Klageschrift | 22 |
```

## Schritt-für-Schritt-Workflow

1. **Jeden Schriftsatz** auf Anlagenverweise (K 1, B 1 etc.) durchsuchen
2. **Anlage mit Inhalt und Datum** erfassen; Originalbezeichnung übernehmen
3. **Schriftsatz und Blattangabe** notieren
4. **Alle Anlagen** nach Partei getrennt tabellarisch listen
5. **Lücken prüfen** — fehlende Nummern als [nicht in vorliegender Akte] markieren
6. **Doppelreferenzen** prüfen — gleiche Anlage in mehreren Schriftsätzen vermerken
7. **Vorlageanordnung prüfen** — falls § 142 ZPO-Beschluss in Akte: erfasste Anlagen abgleichen

## Entscheidungsbaum — Anlage fehlt in Akte

```
Anlage ist im Schriftsatz bezeichnet aber fehlt körperlich in Akte?
 → Handelt es sich um beweiserhebliche Urkunde? (§ 422 ZPO)
 → Ja: Schriftsatz an Gericht: Vorlage anfordern; Eintrag: [angefordert TT.MM.JJJJ]
 → Nein: Vermerk: [nicht in vorliegender Akte]
 → War Anlage Gegenstand einer Vorlageanordnung (§ 142 ZPO)?
 → Ja: Nachverfolgung ob Vorlage erfolgt — ggf. Antrag auf Ungehorsamssanktion
```

## Beispiel (vollständig)

### Klägeranlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag | 15.03.2021 | Klageschrift 08.02.2023 | 12-18 |
| K 2 | Abnahmeprotokoll | 02.09.2021 | Klageschrift 08.02.2023 | 19-21 |
| K 3 | Mängelrüge | 14.10.2021 | Klageschrift 08.02.2023 | 22 |
| K 4 | Nachbesserungsprotokoll | 08.11.2021 | Klageschrift 08.02.2023 | 23-24 |
| K 5 | Rücktrittsandrohung | 03.01.2022 | Klageschrift 08.02.2023 | 25 |
| K 6 | Rücktrittserklärung | 15.02.2022 | Klageschrift 08.02.2023 | 26 |

### Beklagtenanlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| B 1 | E-Mail-Korrespondenz | versch. | Klageerwiderung 14.04.2023 | 40-44 |
| B 2 | Wartungsprotokoll | 05.09.2021 | Klageerwiderung 14.04.2023 | 45-47 |

## Qualitätscheck

- [ ] Alle Anlagenbezeichnungen aus allen Schriftsätzen erfasst?
- [ ] Lücken in der Nummerierung als fehlend markiert?
- [ ] Inhalt kurz aber aussagekräftig beschrieben?
- [ ] Fundstelle (Schriftsatz und Blatt) angegeben?
- [ ] Vorlageanordnungen nach § 142 ZPO berücksichtigt?

<!-- AUDIT 27.05.2026 -->
<!-- BGH VI ZR 396/18 (claimed: Fehlende Anlage kann nachgereicht werden, NJW 2020, 404): WRONG_TOPIC. Urteil existiert (dejure.org/2019,38295), behandelt aber Kfz-Unfall Beilackierungskosten/§287 ZPO Schaetzungsermessen, NJW 2020, 236. Kein Bezug zu ZPO-Anlagenrecht. Eintrag geloescht. -->

---

## Skill: `anwaltsschriftsatz-stilrichtlinie`

_Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln für alle Bausteine des Aktenauszugs. Massstab §§ 130 131 ZPO im Aktenauszug Geri..._

# Anwaltsschriftsatz-Stilrichtlinie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normhintergrund — Schriftsatz-Anforderungen

- § 130 ZPO — Pflichtinhalt anwaltlicher Schriftsätze (Bezeichnung der Partei, Antraege, Tatsachen, Beweismittel)
- § 131 ZPO — Beizufügende Schriftstücke und Anlagen
- § 253 Abs. 2 ZPO — Klageschrift: bestimmter Antrag, Sachverhalt, Benennung Gericht
- § 520 Abs. 3 ZPO — Berufungsbegründung: Bezeichnung der Angriffspunkte, neues Vorbringen
- § 551 Abs. 3 ZPO — Revisionsbegründung: Angabe der Revisionsgründe

## Rechtsprechung zum Schriftsatzstil und Schriftsatz-Anforderungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sprache

### Allgemeine Grundsätze

- **Sachlich und präzise:** Jeder Satz transportiert eine Information. Füllphrasen vermeiden.
- **Juristisch korrekt:** Rechtsbegriffe werden in ihrer gesetzlichen oder gefestigten dogmatischen Bedeutung verwendet.
- **Neutral:** Keine Wertungen, keine Erfolgsprognosen (→ Skill `neutralitaetspruefung`).
- **Aktiv bevorzugen:** "Die Klägerin macht geltend" — nicht "Es wird geltend gemacht".

### Verbotene Begriffe

Keine Begriffe aus dem Bereich kommerzieller Textverarbeitungssoftware oder Assistenzsysteme. Keine Formulierungen wie "basierend auf meiner Analyse" oder "nach meiner Einschätzung". Keine Ich-Form.

### Parteibezeichnungen

- Konsistente Verwendung im gesamten Aktenauszug
- Zulässig: vollständiger Name, Kurzname, Parteibezeichnung (die Klägerin)
- Nicht mischen: nicht "Klägerin" in einem Abschnitt und "Frau Müller" im nächsten
- Abkürzungen (Kl., Bekl.) nur in Tabellen, nicht in Fließtext

### Normen und Paragraphen

- Vollständige Angabe bei erster Nennung: § 634 Nr. 4 i.V.m. § 280 Abs. 1 BGB
- Abkürzung bei Wiederholung möglich: § 634a Abs. 1 Nr. 1 BGB (Verjährung)
- Gesetze stets mit Kurzbezeichnung: BGB, ZPO, StPO, VwGO, ArbGG, SGG, KSchG, GKG

## Gliederung

### Überschriften-Hierarchie

```
### Aktenauszug — [Aktenzeichen] (H1 — nur einmal)

## Verfahrensidentifikation (H2 — Bausteine)
### Parteien (H3 — Unterabschnitte)
#### Klägerseite (H4 — bei Bedarf)
```

### Abschnittstrennungen

Jeder Baustein beginnt auf einer neuen Hierarchieebene. Zwischen Bausteinen eine Leerzeile.

## Tabellen

### Formatierung

- Markdown-Tabellen mit Pipes und Trennzeile
- Spaltenbreite nicht fixieren (Markdown passt sich an)
- Spaltenköpfe fett oder als Header-Zeile

### Tabellenstil

| Gut | Nicht gut |
|---|---|
| Klägerin / Beklagte als Spaltenköpfe | Kl. / Bekl. |
| Kurze präzise Zellinhalte | Lange Fließtextabsätze in Zellen |
| Fundstellen in separater Spalte | Fundstellen ohne Quelle |

## Datumsformat

- Vollständig: TT.MM.JJJJ (z. B. 15.03.2021)
- Kein ISO-Format (2021-03-15) im Aktenauszug-Body
- Monats-/Jahresangaben: März 2021 (nicht 03/2021)

## Beträge

- Immer mit EUR-Präfix: EUR 45.000
- Keine Tausenderpunkte in Zahlen: EUR 45000 oder EUR 45.000 (Punkt als Tausendertrenner ist im Deutschen üblich)
- Keine Abkürzung T€ oder TEUR im Aktenauszug (ausgeschrieben)

## Aktenzeichen

Format: [Gericht-Kürzel] [Senats-/Kammernummer] [Verfahrensart] [Laufnummer]/[Jahr]

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Markdown-Besonderheiten

- Fettdruck (`**Text**`) für Daten in Chronologien
- Kursiv (`*Text*`) sparsam — für Gesetzesbegriffe oder Fremdwörter
- Code-Blöcke (` ``` `) für Musterformulierungen und Vorlagen
- Fristenboxen hervorheben (Tabelle oder Blockquote mit ⚠️)

## Qualitätscheck Stil

- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteibezeichnungen konsistent?
- [ ] Normen vollständig angegeben?
- [ ] Datumsformat einheitlich TT.MM.JJJJ?
- [ ] Beträge mit EUR-Präfix?
- [ ] Überschriften-Hierarchie korrekt?
- [ ] Schriftsatz erfüllt Mindestanforderungen §§ 130-131 ZPO?

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- VII ZR 248/12 (BGH): ersatzlos entfernt (NOT_FOUND auf dejure.org; kein Urteil vom 06.11.2013 nachweisbar)
- VII ZR 126/02 (BGH): ersatzlos entfernt (WRONG_TOPIC: tatsaechliches Thema ist Werkvertragsrecht/Verputzungsfehler/§ 421 BGB, nicht Prozessrecht; Quelle: https://dejure.org/2003,299)
- Aktenzeichen-Formatbeispiele sind frei erfunden und duerfen nicht als Rechtsprechungszitate verwendet werden.

---

## Skill: `arbeitsgerichtsverfahren-modus-terminkalender`

_Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwochenfrist § 4 KSchG Berufung § 64 ArbGG Revision § 72 ArbGG. Normen ArbGG §§ 2 54 64 72 KSchG §§ 1 4 9. Prüfraster Fristen-Spezifika arbeitsgerichtliche Besonderheiten BAG-Leits..._

# Arbeitsgerichtsverfahren-Modus (ArbGG)

## Arbeitsbereich

Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwochenfrist § 4 KSchG Berufung § 64 ArbGG Revision § 72 ArbGG. Normen ArbGG §§ 2 54 64 72 KSchG §§ 1 4 9. Prüfraster Fristen-Spezifika arbeitsgerichtliche Besonderheiten BAG-Leitsaetze. Output ArbGG-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und sozialgerichtsverfahren-modus (SGG). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Aktivierung des Modus

1. Urteilsverfahren (§§ 46 ff. ArbGG) oder Beschlussverfahren (§§ 80 ff. ArbGG)?
2. Kündigungsschutzklage? → Klagefrist 3 Wochen ab Zugang (§ 4 KSchG) — sofort prüfen!
3. Instanz: Arbeitsgericht / LAG / BAG?
4. Liegt ein Güteterminprotokoll in der Akte?
5. Massenentlassung i.S.v. § 17 KSchG? (Anzeige bei Agentur für Arbeit?)

## Zentrale Normen (ArbGG / KSchG)

- § 4 KSchG — Klagefrist 3 Wochen; § 7 KSchG — Heilungsfiktion bei Fristversäumnis
- § 5 KSchG — Nachträgliche Klagezulassung (enge Voraussetzungen)
- § 1 KSchG — Soziale Rechtfertigung der Kündigung (Anwendbarkeit: § 23 KSchG)
- § 102 BetrVG — Betriebsratsanhörung vor Kündigung (Formerfordernis)
- §§ 46-49 ArbGG — Urteilsverfahren; § 54 ArbGG — Güteversuch
- §§ 64-74 ArbGG — Berufung und Revision beim LAG/BAG
- § 80-90 ArbGG — Beschlussverfahren; § 83 ArbGG — Untersuchungsgrundsatz
- § 12a ArbGG — Kein Anwaltskostenersatz in 1. Instanz

## Rechtsprechung (BAG — aktuelle Leitsätze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Verfahrensarten

### Urteilsverfahren (§§ 46 ff. ArbGG)

Für bürgerliche Rechtsstreitigkeiten zwischen Arbeitnehmern und Arbeitgebern.

**Typischer Ablauf:**

1. Klageeingang
2. Gütetermin (§ 54 ArbGG) — obligatorisch, schnell angesetzt
3. Bei Scheitern: Kammertermin (Hauptverhandlung)
4. Urteil
5. Berufung zum Landesarbeitsgericht (§ 64 ArbGG)
6. Revision zum Bundesarbeitsgericht (§ 72 ArbGG)

### Beschlussverfahren (§§ 80 ff. ArbGG)

Für kollektivrechtliche Streitigkeiten (Betriebsverfassung, Mitbestimmung).

Beteiligte: Arbeitgeber / Betriebsrat / Gewerkschaft. Keine Parteien im zivilprozessualen Sinne — im Aktenauszug "Antragsteller" und "Antragsgegner" verwenden.

## Kritische Fristen (ArbGG / KSchG)

| Frist | Norm | Dauer | Besonderheit |
|---|---|---|---|
| Kündigungsschutzklage | § 4 KSchG | 3 Wochen | ab Zugang Kündigung — NOTFRIST |
| Berufungsfrist | § 66 Abs. 1 ArbGG | 1 Monat | ab Zustellung Urteil |
| Berufungsbegründungsfrist | § 66 Abs. 1 ArbGG | 2 Monate | ab Zustellung Urteil |
| Revisionsfrist | § 74 Abs. 1 ArbGG | 1 Monat | ab Zustellung Urteil |

**Besondere Hervorhebung:** Die Dreiwochenfrist des § 4 KSchG ist absolut — bei Versäumnis gilt die Kündigung als wirksam (§ 7 KSchG), selbst wenn sie materiell unwirksam wäre. Nachträgliche Zulassung nur unter engen Voraussetzungen (§ 5 KSchG).

## Besonderheiten Gütetermin

- Gütetermin findet regelmäßig wenige Wochen nach Klageeingang statt
- Richter versucht aktiv Vergleich herbeizuführen
- Bei Einigung im Gütetermin: Prozessvergleich (§ 794 Abs. 1 Nr. 1 ZPO)
- Im Aktenauszug: Güteterminsdatum und Ergebnis (Einigung / Scheitern) hervorheben
- Abfindungserwartung Faustformel: 0,5 Bruttomonatsgehaelter pro Beschaeftigungsjahr

## Besonderheiten Beschlussverfahren

- Untersuchungsgrundsatz (§ 83 ArbGG) — Gericht ermittelt von Amts wegen
- Beteiligte können unbeschränkt Anträge stellen
- Rechtskraft des Beschlusses nur für Beteiligte

## Kostenrecht (§ 12a ArbGG)

Keine Kostenerstattung für Anwaltskosten in erster Instanz — im Aktenauszug auf Besonderheit hinweisen.

## Besonderheiten im Aktenauszug

- Stets KSchG-Klagefrist und Zugang der Kündigung prominent darstellen
- Gütetermin als eigenen Verfahrensschritt in der Verfahrenschronologie
- Bei Betriebsratsanhörung (§ 102 BetrVG): Datum und Ordnungsgemäßheit in der Sachverhaltschronologie
- Massenentlassung (§ 17 KSchG): Anzeige bei Agentur für Arbeit als eigenes Ereignis

## Output-Template Kammertermin-Vorbereitung

**Adressat:** Sachbearbeiter — Tonfall: sachlich-juristisch

```
TERMINSVORSCHAU — [AKTENZEICHEN]
Termin: [DATUM] [UHRZEIT] — ArbG [ORT] Saal [X]
Verfahren: [KURZBEZEICHNUNG]
Klagefrist gewahrt: Ja / Nein (§ 4 KSchG — Zugang [DATUM] + 21 Tage = [FRISTENDE])
BR-Anhörung: Ja / Nein / unklar
Guetetermin: [DATUM] — [ERGEBNIS]
Aktuelle Antraege: 1. Feststellungsklage § 4 KSchG; 2. [...]
Streitige Punkte: [LISTE]
Vergleichsspielraum: [BETRAG] / offenes Zeugnis / beides
```

---
<!-- AUDIT 27.05.2026: Bundle 010 Halluzinations-Reparatur -->

---

## Skill: `beweismittel-gegenueberstellung`

_Anwalt will Beweisangebote aller Parteien uebersichtlich gegenüberstellen: Zeugen Urkunden Sachverständige Parteivernehmung Augenschein. Normen §§ 355-455 ZPO Sachverständigenbeweis Zeugenbeweis. Prüfraster Vollständigkeit Parteizuordnung Streitpunkt-Zuordnung Fundstellen. Output tabellarische Be..._

# Beweismittel — Gegenüberstellung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Welche Beweismittel sind bereits erhoben (Gutachten vorgelegt, Zeugen vernommen)?
2. Welche Beweismittel sind angeboten aber noch nicht erhoben?
3. Hat das Gericht bereits über die Beweiserhebung entschieden? (Beweisbeschluss § 359 ZPO)
4. Wurden Beweismittel vom Gericht als präkludiert zurückgewiesen (§§ 296, 531 ZPO)?

## Zulässige Beweismittel und Normen (§ 355 ff. ZPO)

- § 371 ff. ZPO — Augenscheinsbeweis (Besichtigung, Fotos, Videoaufnahmen)
- § 373 ff. ZPO — Zeugenbeweis (Ladung, Vernehmung, Eid, Aussageverbot)
- § 402 ff. ZPO — Sachverständigenbeweis (Bestellung, Gutachtenerstattung, Ablehnung)
- § 415 ff. ZPO — Urkundenbeweis (öffentlich/privat, Echtheit, Beweiskraft)
- § 445 ff. ZPO — Parteivernehmung (nur bei Unvollständigkeit anderer Beweismittel)

## Rechtsprechung zum Beweisrecht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Tabellenstruktur

```markdown
| Beweisthema | Beweismittel | Partei | Bezeichnung / Name | Fundstelle |
|---|---|---|---|---|
| [Streitpunkt] | [Art] | Kläger / Beklagter | [Name / Anlage] | [Schriftsatz Bl.] |
```

## Beispiel

| Beweisthema | Beweismittel | Partei | Bezeichnung / Name | Fundstelle |
|---|---|---|---|---|
| Vertragsinhalt Einweisung | Urkunde | Kläger | Werkvertrag K 1 | Klageschrift Bl. 12 |
| Mangel Dach | Zeuge | Kläger | Heiko Mustermann (Bauleiter) | Klageschrift Bl. 28 |
| Mangel Dach | Sachverständiger | Kläger | Einholung eines Baugutachtens | Klageschrift Bl. 29 |
| Ursache Undichtigkeit | Zeuge | Beklagter | Maria Musterfrau (Mitarbeiterin) | Klageerwiderung Bl. 52 |
| Schadenshöhe | Urkunde | Kläger | Sanierungskostenrechnung K 8 | Replik Bl. 70 |
| Schadenshöhe | Sachverständiger | Beklagter | Gegengutachten (beantragt) | Klageerwiderung Bl. 66 |

## Besondere Hinweise

### Urkundenbeweis

Jede Urkunde wird mit ihrer Anlagenbezeichnung (K 1, B 1 etc.) und einem kurzen Inhaltsvermerk aufgeführt.

### Zeugen

Vollständiger Name (sofern bekannt), Eigenschaft (z. B. "Augenzeuge", "Vertragspartner", "Mitarbeiter"), benennende Partei.

### Sachverständige

Wird ein Gutachten beantragt (nicht bereits vorhanden), so ist das Beweisthema zu nennen. Liegt ein Gutachten bereits vor, wird das Gutachten als Urkunde und der Gutachter als gesondert aufgeführt.

### Parteivernehmung

Selten — nur wenn angeboten oder angeordnet. Partei und Vernehmungsthema benennen.

### Präkludierte Beweismittel

Soweit Beweismittel vom Gericht als verspätet zurückgewiesen wurden, werden sie mit dem Vermerk "[zurückgewiesen]" aufgeführt.

## Qualitätscheck

- [ ] Alle angebotenen Beweismittel erfasst?
- [ ] Beweisthema klar bezeichnet?
- [ ] Anlagenbezeichnung und Fundstelle angegeben?
- [ ] Keine Bewertung der Beweiskraft?
- [ ] Präkludierte Beweismittel gekennzeichnet?
- [ ] Beweisbeschluss des Gerichts (§ 359 ZPO) berücksichtigt?

---

## Skill: `einleitungssatz-generator`

_Aktenauszug braucht praegnanten Einleitungssatz: wer streitet mit wem worueber welche Hauptnorm. Juristisch praezise neutral ohne Wertung ohne Erfolgsprognose. Normen §§ 253 304 ZPO. Prüfraster Praegnanz Vollständigkeit Neutralitaet Haupt-Norm-Nennung. Output Ein-Zwei-Satz-Kern Rechtstreit. Abgre..._

# Einleitungssatz-Generator

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Formulierung

1. Zivilverfahren, Arbeitsgericht, Strafverfahren, Verwaltungsgericht oder Sozialgericht?
2. Erstinstanz, Berufung oder Revision?
3. Was ist die Hauptnorm des Anspruchs oder der Anklage?
4. Wie lautet der exakte Klagebetrag oder das Klagebegehren?

## Zentrale Normen (Streitgegenstand / Klagebegehren)

- § 253 Abs. 2 Nr. 2 ZPO — Klageschrift: bestimmter Antrag und Sachverhalt als Grundlage des Einleitungssatzes
- § 264 ZPO — Klageaenderung (im Einleitungssatz ggf. letzten Stand des Antrags aufführen)
- § 308 ZPO — Bindung des Gerichts an Antrag (ne ultra petita)
- § 42 VwGO — Anfechtungs- und Verpflichtungsklage
- § 4 KSchG — Kündigungsschutzklage (Frist und Antrag)

## Rechtsprechung zum Streitgegenstand und Klagebegehren

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Struktur des Einleitungssatzes

**Muster:**

> [Kläger] nimmt [Beklagten] aus [Hauptnorm] auf [Klagebegehren] in Anspruch.

Ergänzend kann ein zweiter Satz den prozessualen Stand knapp abbilden:

> Die Klage ist seit [Datum] beim [Gericht] anhängig; [mündliche Verhandlung steht aus / Urteil erging am ...].

## Varianten nach Verfahrensart

### Zivilverfahren (ZPO)

> [Kläger] begehrt von [Beklagtem] Zahlung von [Betrag] nebst Zinsen aus § [Norm] BGB wegen [Sachverhaltskern]; das Verfahren ist beim Landgericht [Stadt] als [AZ] anhängig.

### Eilverfahren (§ 935 ff. ZPO)

> [Antragstellerin] begehrt im Wege der einstweiligen Verfügung gemäß §§ 935 938 ZPO die Unterlassung von [Handlung] gegenüber [Antragsgegner]; das Verfahren ist beim [Gericht] als [AZ] anhängig.

### Berufungsverfahren

> [Berufungsklägerin] wendet sich mit ihrer Berufung vom [Datum] gegen das Urteil des Landgerichts [Stadt] vom [Datum] (Az. [AZ]) und begehrt weiterhin [Klagebegehren].

### Strafverfahren (StPO)

> Der Angeklagte [Name] ist durch Anklage der Staatsanwaltschaft [Ort] vom [Datum] wegen [Vorwurf] (§§ [Normen] StGB) angeklagt; die Hauptverhandlung findet vor der [Kammer] des [Gerichts] unter dem Az. [AZ] statt.

### Verwaltungsverfahren (VwGO)

> Die Klägerin wendet sich mit einer Anfechtungsklage (§ 42 Abs. 1 Alt. 1 VwGO) gegen den Bescheid der Behörde [Name] vom [Datum] und begehrt dessen Aufhebung.

### Arbeitsgerichtsverfahren (ArbGG)

> Die Klägerin begehrt die Feststellung der Unwirksamkeit der ordentlichen Kündigung vom [Datum] gemäß § 4 KSchG; das Verfahren ist beim Arbeitsgericht [Stadt] als [AZ] anhängig.

### Sozialgerichtsverfahren (SGG)

> Die Klägerin begehrt die Gewährung von [Leistung] durch den Beklagten [Träger] und hat nach Erfolglosigkeit des Widerspruchsverfahrens Klage beim Sozialgericht [Stadt] erhoben (Az. [AZ]).

## Regeln

- Maximal zwei Sätze
- Keine Wertung (nicht: "zu Unrecht"; "unbegründet")
- Keine Erfolgsprognose
- Parteinamen vollständig benennen (kein "Kl." oder "Bekl." im Einleitungssatz)
- Normen mit vollständiger Bezeichnung (nicht nur Paragraphennummer)

## Qualitätscheck

Nach Erstellung prüfen:
- [ ] Wer streitet mit wem? ja/nein
- [ ] Worüber wird gestritten? ja/nein
- [ ] Hauptnorm genannt? ja/nein
- [ ] Keine Wertung? ja/nein
- [ ] Maximal zwei Sätze? ja/nein
- [ ] Streitgegenstand i.S.v. § 253 Abs. 2 Nr. 2 ZPO hinreichend bestimmt? ja/nein

---

## Skill: `fristen-und-terminkalender`

_Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungsfrist Verkündungstermin Vollziehungsfrist. Normen §§ 222 517 520 548 ZPO. Prüfraster Vollständigkeit Frist-Berechnung Hervorhebung Fehler-Scan. Output Fristen-Box Fristen-Tabell..._

# Fristen und Terminkalender

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Fristermittlung

1. Wurde das Urteil (erstinstanzlich) bereits zugestellt? (Berufungsfrist läuft!)
2. Liegt ein Hinweisbeschluss des Gerichts mit Frist vor?
3. Wurden Sachverständigenvorschüsse angefordert mit Zahlungsfrist?
4. Handelt es sich um ein Eilverfahren? (Vollziehungsfrist § 929 Abs. 2 ZPO)
5. KSchG-Verfahren? (3-Wochen-Frist § 4 KSchG — absolute Notfrist)

## Zentrale Normen

- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung (Wochenende, Feiertag)
- § 233-238 ZPO — Wiedereinsetzung in den vorigen Stand bei unverschuldetem Fristversäumnis
- § 517 ZPO — Berufungsfrist 1 Monat; § 520 Abs. 2 ZPO — Begründungsfrist 2 Monate
- § 548 ZPO — Revisionsfrist 1 Monat; § 551 ZPO — Revisionsbegründungsfrist 2 Monate
- § 929 Abs. 2 ZPO — Vollziehungsfrist einstweilige Verfügung 1 Monat
- § 4 KSchG — Klagefrist 3 Wochen (Notfrist); § 74 VwGO — Klagefrist 1 Monat

## Rechtsprechung zu Fristen und Fristversäumnis

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Fristenarten

### Absolute Fristen (gesetzlich, nicht verlängerbar)

| Frist | Norm | Fristdauer | Berechnung |
|---|---|---|---|
| Berufungsfrist | § 517 ZPO | 1 Monat | ab Zustellung Urteil |
| Berufungsbegründungsfrist | § 520 Abs. 2 ZPO | 2 Monate | ab Zustellung Urteil |
| Revisionsfrist | § 548 ZPO | 1 Monat | ab Zustellung Urteil |
| Revisionsbegründungsfrist | § 551 ZPO | 2 Monate | ab Zustellung Urteil |
| Klagefrist KSchG | § 4 KSchG | 3 Wochen | ab Zugang Kündigung |
| Klagefrist VwGO | § 74 VwGO | 1 Monat | ab Zustellung Widerspruchsbescheid |
| Vollziehungsfrist eV | § 929 Abs. 2 ZPO | 1 Monat | ab Zustellung Beschluss |
| Berufungsfrist ArbGG | § 66 ArbGG | 1 Monat | ab Zustellung Urteil |
| Berufungsfrist SGG | § 151 SGG | 1 Monat | ab Zustellung Urteil |

### Richterliche Fristen (verlängerbar)

- Schriftsatzfristen des Gerichts (Klageerwiderung, Replik, Duplik)
- Frist zur Stellungnahme zu Hinweisbeschlüssen
- Frist zur Einzahlung von Auslagen (Sachverständigenvorschuss)

### Notfristen

Fristen, die nicht verlängerbar sind und bei denen Wiedereinsetzung nur unter engen Voraussetzungen möglich ist (z. B. Berufungsfrist).

## Output-Format (Fristenbox am Anfang)

```
FRISTEN UND TERMINE — SOFORT PRUEFEN
Berufungsfrist: TT.MM.JJJJ (§ 517 ZPO)
Begründungsfrist: TT.MM.JJJJ (§ 520 ZPO)
Nächste Verhandlung: TT.MM.JJJJ HH:UU Uhr
Schriftsatzfrist: TT.MM.JJJJ (richterliche Anordnung)
```

Alternativ als Markdown-Tabelle:

```markdown

## Fristen und Termine — Sofort prüfen

| Frist / Termin | Datum | Norm | Status |
|---|---|---|---|
| Berufungsfrist | TT.MM.JJJJ | § 517 ZPO | laeuft |
| Begründungsfrist | TT.MM.JJJJ | § 520 ZPO | laeuft |
| Mündliche Verhandlung | TT.MM.JJJJ | Terminsverfügung | angesetzt |
```

## Berechnungshinweise

- Fristbeginn immer anhand des tatsächlichen Zustellungsdatums aus der Akte ermitteln
- Wenn Zustellungsdatum nicht bekannt: ausdrücklich als "Zustellungsdatum unbekannt — Frist nicht berechenbar" kennzeichnen
- Wochenenden und gesetzliche Feiertage nach § 222 ZPO i.V.m. §§ 187-188 BGB berücksichtigen
- Bei Monatsfristen: Fristende = gleicher Tag des Folgemonats (§ 188 Abs. 2 BGB)

## Qualitätscheck

- [ ] Alle gesetzlichen Fristen aus der Akte erfasst?
- [ ] Fristenbox am Anfang des Aktenauszugs?
- [ ] Berechnungsgrundlage (Zustellungsdatum) angegeben?
- [ ] Fehlende Zustellungsdaten als "unbekannt" markiert?
- [ ] Fristen in der Verfahrenschronologie markiert?
- [ ] Wochenende/Feiertag bei Fristende berücksichtigt (§ 222 ZPO)?

---

---

## Skill: `neutralitaetspruefung`

_Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherheitsgate vor Weitergabe des Auszugs. Massstab § 286 ZPO freie..._

# Neutralitätsprüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Prüfung

1. Für wen ist der Aktenauszug bestimmt? (internes Arbeitsdokument / Übergabe an Mandant / Gericht)
2. Hat der Ersteller den Auftrag, die eigene Mandantsseite besonders darzustellen? (dann kein Aktenauszug, sondern Schriftsatz!)
3. Gibt es Stellen, die bewusst als subjektive Einschätzung des Anwalts markiert sind? (Diese sind zu entfernen oder zu kennzeichnen.)

## Normhintergrund

- § 286 Abs. 1 ZPO — Freie Beweiswürdigung des Gerichts; Aktenauszug darf keine Beweiswürdigungsprognosen enthalten
- § 138 ZPO — Wahrheitspflicht; auch interne Vermerke müssen den Sachverhalt korrekt abbilden
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot; gilt auch für interne Aktendokumentation

## Rechtsprechung zum Sachlichkeitsgebot und Neutralität

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Verbotene Formulierungstypen

### Erfolgsprognosen (absolut verboten)

| Verboten | Erlaubt |
|---|---|
| "Die Klage wird Erfolg haben" | "Die Klage ist anhängig" |
| "Der Anspruch dürfte begründet sein" | "Die Klägerin macht [Anspruch] geltend" |
| "Die Verjährungseinrede greift durch" | "Die Beklagte erhebt die Verjährungseinrede" |
| "Das Gericht wird … erkennen" | "Das Gericht hat … nicht geäußert" |
| "offensichtlich unbegründet" | "nach Vortrag der Beklagten unbegründet" |

### Wertende Adjektive (zu vermeiden)

- substanzlos, unhaltbar, abwegig, überzeugend, zutreffend, unzutreffend
- zu Recht, zu Unrecht
- offensichtlich, eindeutig (ohne Quellenangabe)

### Parteiische Darstellung

- Ausführliche Wiedergabe des Vortrags einer Seite ohne entsprechende Gegenüberstellung der anderen Seite
- Formulierungen, die implizit eine Seite stärken ("Trotz des klaren Wortlauts des Vertrags …")

## Prüfmethodik

### Schritt 1 — Scan auf verbotene Muster

Folgende Muster systematisch suchen:

- `dürfte`, `wird`, `sollte`, `kann davon ausgegangen werden`
- `zu Recht`, `zu Unrecht`, `offensichtlich`, `eindeutig`
- `überzeugt`, `überzeugend`, `substanzlos`, `unhaltbar`
- `Erfolgsaussichten`, `Erfolg haben`, `scheitern`

### Schritt 2 — Parteibalance prüfen

Jeder Abschnitt des Parteivortrag und der Rechtsargumente muss beide Seiten gleichgewichtig darstellen.

### Schritt 3 — Korrekturen vorschlagen

Für jede beanstandete Formulierung wird eine neutrale Ersatzformulierung vorgeschlagen.

## Ergebnis-Format

```markdown

## Neutralitätsprüfung — Ergebnis

### Beanstandungen

| Stelle | Ursprüngliche Formulierung | Ersatzformulierung |
|---|---|---|
| Zusammenfassung Satz 3 | Anspruch dürfte begründet sein | Klägerin macht den Anspruch geltend |
| Rechtsargument Zeile 4 | offensichtlich verjährt | nach Vortrag der Beklagten verjährt |

### Ergebnis

[BESTANDEN / ÜBERARBEITUNG ERFORDERLICH]

Anzahl Beanstandungen: [Zahl]
```

## Qualitätscheck — Checkliste

- [ ] Keine Erfolgsprognose enthalten?
- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteivortrag beider Seiten gleichgewichtig dargestellt?
- [ ] Fristen neutral als Tatsache, nicht als Gefahr formuliert?
- [ ] Keine implizit parteiische Darstellung?

## Hinweis

Die Neutralitätsprüfung ist kein Korrektorat des Aktenauszugs. Sie prüft ausschließlich auf Wertungen und Prognosen. Sachliche Fehler sind durch Abgleich mit der Akte zu beheben.

---

---

## Skill: `rechtsargumente-gegenueberstellung`

_Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einreden Verjährungsthema und Pinpoint-Zitate aus Rechtsprechung (BGH OLG EuGH). Keine Wertung welches Argument ueberzeugt. Normen §§ 195-218 BGB Verjährung §§ 280 ff. BGB Schadenser..._

# Rechtsargumente — Gegenüberstellung

## Arbeitsbereich

Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einreden Verjährungsthema und Pinpoint-Zitate aus Rechtsprechung (BGH OLG EuGH). Keine Wertung welches Argument ueberzeugt. Normen §§ 195-218 BGB Verjährung §§ 280 ff. BGB Schadensersatz. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Welche Anspruchsgrundlagen benennt die Klägerseite explizit?
2. Welche Einwendungen und Einreden erhebt die Beklagtenseite?
3. Ist Verjährung im Raum? (§§ 195-218 BGB — regelmässig 3 Jahre ab Jahresende Entstehung/Kenntnis)
4. Zitieren die Parteien konkrete BGH- oder OLG-Entscheidungen?

## Zentrale Normen (Ansprüche und Einreden)

- §§ 280-285 BGB — Schadensersatz (Pflichtverletzung, Schuldverhältnis, Verschulden)
- §§ 195-218 BGB — Verjährung (regelmässig 3 Jahre §195 BGB; Hemmung §§ 203-211; Neubeginn § 212)
- § 254 BGB — Mitverschulden
- §§ 387-396 BGB — Aufrechnung
- §§ 273-274 BGB — Zurückbehaltungsrecht
- §§ 633-634a BGB — Mängelhaftung Werkvertrag; §§ 434-442 BGB — Kaufrechtliche Mängel
- §§ 305-310 BGB — AGB-Kontrolle (Einbeziehung, unangemessene Benachteiligung)

## Rechtsprechung zu Anspruchsgrundlagen und Einreden

## Tabellenstruktur

```markdown
| Rechtspunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| [Rechtsfrage] | [Position / Norm / Zitat Kläger] | [Position / Norm / Zitat Beklagter] |
```

## Kategorien

### Anspruchsgrundlagen

Welche Norm stützt das Klagebegehren? Welche Gegennorm beruft die Beklagte?

### Einwendungen (rechtshindernde / rechtsvernichtende)

Mängel der Anspruchsvoraussetzungen, Rücktritt, Aufrechnung, Unmöglichkeit.

### Einreden (rechtshemmende)

Verjährung, Zurückbehaltungsrecht, Stundung.

### Schadensrecht

Kausalität, Mitverschulden (§ 254 BGB), Schadenshöhe.

### Rechtsprechung

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiel

| Rechtspunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| Anspruchsgrundlage | § 634 Nr. 4 i.V.m. § 280 Abs. 1 BGB (Schadensersatz wegen Mangel) | Kein Mangel i.S.d. § 633 BGB; Abnahme erfolgte vorbehaltlos |
| Wirksamkeit Abnahme | Abnahme unter Vorbehalt gem. § 640 Abs. 1 S. 2 BGB | Abnahmeprotokoll ohne Vorbehalt unterzeichnet |
| Verjährung | Frist läuft noch; Fristbeginn erst mit Kenntnis des Mangels | Verjährungsfrist von zwei Jahren ab Abnahme (§ 634a Abs. 1 Nr. 1 BGB) bereits abgelaufen |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Schadenshöhe | Volle Kosten der Mängelbeseitigung nach § 635 BGB (EUR 45.000) | § 254 BGB: Mitverschulden wegen unterlassener Wartung mindert Anspruch |

## Umgang mit Rechtsprechung

- Nur in Schriftsätzen zitierte Entscheidungen aufnehmen
- Aktenzeichen und Entscheidungsdatum angeben
- Tenor oder tragende Aussage kurz paraphrasieren
- Keine eigene Rechtsprechungsrecherche im Aktenauszug — nur Wiedergabe des Parteivortrags

## Qualitätscheck

- [ ] Alle Anspruchsgrundlagen der Klägerseite erfasst?
- [ ] Alle Einwendungen und Einreden der Beklagtenseite erfasst?
- [ ] Verjährungsthema behandelt (falls relevant) — §§ 195-218 BGB?
- [ ] Rechtsprechungszitate mit Aktenzeichen und Datum?
- [ ] Keine eigene Rechtsbewertung enthalten?
- [ ] Mitverschulden § 254 BGB erwogen?

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- VI ZR 62/22: ersatzlos entfernt — kein Eintrag auf dejure.org (NOT_FOUND)
- VI ZR 136/20: ersatzlos entfernt — WRONG_TOPIC; reale Entscheidung 05.10.2021 betrifft Feststellungsklage VW-Abgasskandal (NJW-RR 2022, 23), nicht Verjährungsbeginn § 199 BGB; beanspruchte NJW 2022, 53 existiert nicht in dejure
- VI ZR 282/17: ersatzlos entfernt — kein Eintrag auf dejure.org (NOT_FOUND)
- VI ZR 259/17: ersatzlos entfernt — kein Eintrag auf dejure.org (NOT_FOUND)

---

## Skill: `sachverhaltschronologie`

_Erstellt eine chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen: Vertragsschluss Vorfaelle vorgerichtliche Korrespondenz Schadensereignisse und Behördenakte. Datum fett vorangestellt knappe Beschreibung ohne Wertung. Fundstellen in der Akte werden angegeben. Normen §§ 145..._

# Sachverhaltschronologie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Erstellung

1. Liegt der Vertragsschluss klar dokumentiert vor? (Angebot § 145 BGB + Annahme § 147 BGB)
2. Gibt es widersprüchliche Datumsangaben in den Schriftsätzen der Parteien?
3. Existieren Behördenbescheide oder Protokolle, die in die Chronologie einzupflegen sind?
4. Welcher Zeitraum ist rechtserheblich? (Verjährungsfrist nach §§ 195-218 BGB beachten)

## Zentrale Normen (materiell-rechtlicher Hintergrund)

- §§ 145-157 BGB — Vertragsschluss (Angebot, Annahme, Vertragsinhalt)
- §§ 280-285 BGB — Schadensersatz wegen Pflichtverletzung
- §§ 631-651 BGB — Werkvertrag (Errichtung, Abnahme, Mängelhaftung)
- §§ 433-442 BGB — Kaufvertrag (Übergabe, Mängelrechte)
- §§ 195-199 BGB — Verjährung und Verjährungsbeginn (Kenntnis von Anspruch und Person)
- § 307 BGB — Unwirksame AGB-Klauseln die Rechte des Vertragspartners beschneiden

## Rechtsprechung zur Sachverhalts-Dokumentation und Vertragsschluss

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Was gehört hinein

- Vertragsschlüsse, Angebote, Annahmen
- Leistungserbringung oder Nichtleistung
- Mängelrügen, Mahnungen, Zahlungen
- Schadensereignisse (Unfälle, Lieferausfälle, Datenverluste)
- Vorgerichtliche Korrespondenz (Schreiben, E-Mails, Protokolle)
- Behördliche Bescheide, Genehmigungen, Prüfprotokolle
- Verhandlungen und Einigungsversuche
- Kündigung oder Rücktritt
- Alle sonstigen tatsächlichen Handlungen, die für den Rechtsstreit erheblich sind

## Was nicht hinein gehört

- Schriftsätze, Klageschrift, Erwiderungen (→ Verfahrenschronologie)
- Gerichtstermine, Beschlüsse, Urteile (→ Verfahrenschronologie)
- Rechtliche Bewertungen

## Formatvorgabe

```
- **TT.MM.JJJJ** [Kurzbeschreibung des Ereignisses] (Fundstelle: [Anlage / Blatt])
```

## Beispiele

```
- **15.03.2021** Abschluss des Werkvertrags über Errichtung einer Lagerhalle für EUR 850.000 (K 1 Bl. 12-18)
- **02.09.2021** Übergabe der Lagerhalle durch Auftragnehmer; Abnahmeprotokoll unterzeichnet (K 3 Bl. 22-24)
- **14.10.2021** Schriftliche Mängelrüge des Auftraggebers wegen Undichtigkeit des Dachs (K 4 Bl. 26)
- **08.11.2021** Nachbesserungsversuch des Auftragnehmers; Mangel nach Vortrag des Auftraggebers nicht beseitigt (B 2 Bl. 45)
- **03.01.2022** Androhung des Rücktritts per anwaltlichem Schreiben (K 5 Bl. 30)
- **15.02.2022** Erklärung des Rücktritts vom Werkvertrag (K 6 Bl. 33)
```

## Arbeitsschritte

1. Alle Urkunden und Schriftsätze auf tatsächliche Ereignisse durchsehen
2. Jedes Ereignis mit Datum und Kurzbeschreibung erfassen
3. Chronologisch sortieren (ältestes Ereignis zuerst)
4. Fundstelle in der Akte hinzufügen (Anlagebezeichnung und Blattangabe)
5. Doppelte Nennungen zusammenführen
6. Wertende Formulierungen streichen
7. Verjährungsrelevante Ereignisse markieren (Beginn Frist §§ 195-199 BGB)

## Umgang mit unklaren Daten

- Ungenaues Datum: "ca. [Monat JJJJ]" oder "zwischen [Datum] und [Datum]"
- Datum nicht bekannt: "[Zeitraum unbekannt, nach Aktenlage ca. ...]"
- Widersprüchliche Daten in den Schriftsätzen: beide Versionen nennen und Partei angeben

## Qualitätscheck

- [ ] Alle wesentlichen außerprozessualen Ereignisse erfasst?
- [ ] Chronologisch sortiert?
- [ ] Datum fettgedruckt?
- [ ] Fundstelle angegeben?
- [ ] Keine prozessualen Schritte enthalten?
- [ ] Keine Wertung?
- [ ] Verjährungsrelevante Ereignisse besonders markiert?

---

---

## Skill: `schwerpunktthemen-identifikation-akten`

_Anwalt braucht schnellen Überblick über drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten ohne Erfolgsprognose. Normen §§ 139 286 ZPO BGH-Leitsaetze. Prüfraster Streitpunkt-Relevanzbewertung Rechtsprechungs-Verankerung Fundstellen-Praezision. Output Streitpunkt-Liste..._

# Schwerpunktthemen-Identifikation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Identifikation

1. Hat das Gericht bereits Hinweise nach § 139 ZPO erteilt, auf welche Punkte es ankommt?
2. Liegt ein Beweisbeschluss vor (§ 359 ZPO)? Beweisthemen sind automatisch Schwerpunkte.
3. Sind in der Akte BGH- oder OLG-Urteile von den Parteien zitiert? (Hinweis auf rechtlich umstrittene Punkte)
4. Welche Punkte sind in mehreren Schriftsätzen (Klageerwiderung, Replik, Duplik) ausführlich diskutiert?

## Zentrale Normen

- § 139 ZPO — Richterliche Hinweispflicht; Hinweise des Gerichts benennen die Schwerpunkte
- § 286 ZPO — Freie Beweiswürdigung; entscheidungserhebliche Tatsachen sind Schwerpunkte
- § 359 ZPO — Beweisbeschluss; benennt beweisbedürftige Tatsachen
- § 522 Abs. 2 ZPO — Berufungsverwerfung; Schwerpunkt in der Berufung ist Erfolgsaussicht

## Rechtsprechung zu Schwerpunktthemen im Zivilprozess

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kriterien für ein Schwerpunktthema

Ein Thema ist Schwerpunkt, wenn:

- Es in mehreren Schriftsätzen kontrovers diskutiert wird
- Das Gericht einen ausdrücklichen Hinweis dazu erteilt hat
- Ein Beweisbeschluss zu diesem Punkt ergangen ist
- Rechtsprechung der Parteien zu diesem Punkt zitiert wird
- Die Entscheidung im Verfahren von diesem Punkt maßgeblich abhängt

## Anzahl

Drei bis fünf Schwerpunktthemen. Bei einfachen Verfahren können es weniger sein; bei komplexen Verfahren werden trotzdem nicht mehr als fünf ausgewiesen — die übrigen Fragen werden in den Tabellen erfasst.

## Outputformat

```markdown

## Schwerpunktthemen

### 1. [Bezeichnung des Schwerpunktthemas]

**Beschreibung:** [Kurze Darstellung der Rechtsfrage]

**Parteiposition Kläger:** [Position ohne Wertung]

**Parteiposition Beklagter:** [Position ohne Wertung]

**Einschlägige Rechtsprechung (aus Akte):** [Zitat mit Aktenzeichen und Datum soweit in Schriftsätzen genannt]

**Fundstellen:** [Schriftsatz Bl. ...]

---
```

## Beispiel

### 1. Verjährung des Mangelbeseitigungsanspruchs

**Beschreibung:** Streitig ist, ob der Schadensersatzanspruch der Klägerin nach § 634a Abs. 1 Nr. 1 BGB (zwei Jahre ab Abnahme) bereits verjährt ist.

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Fundstellen:** Klageschrift Bl. 30-32; Klageerwiderung Bl. 55-58.

---

### 2. Wirksamkeit der Abnahme unter Vorbehalt

**Beschreibung:** Streitig ist, ob das unterzeichnete Abnahmeprotokoll einen Vorbehalt enthält oder vorbehaltlos ist.

**Parteiposition Klägerin:** Abnahme erfolgte unter Vorbehalt nach § 640 Abs. 1 S. 2 BGB (Bl. 20-21 Anlage K 2).

**Parteiposition Beklagte:** Protokoll enthält keinen Vorbehalt; vorbehaltlose Abnahme liegt vor.

**Fundstellen:** Klageschrift Bl. 20-22; Klageerwiderung Bl. 48-50.

## Hinweis

Schwerpunktthemen werden neutral dargestellt. Die Identifikation eines Themas als Schwerpunkt bedeutet keine Einschätzung, welche Seite in dieser Frage Recht hat.

## Audit-Hinweis

<!-- AUDIT 27.05.2026 -->
**Halluzinations-Reparatur durchgeführt am 27.05.2026.**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Quellen: dejure.org (https://dejure.org/2016,13484 ; https://dejure.org/2019,4759)

---

## Skill: `sozialgerichtsverfahren-modus`

_Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtsermittlungsgrundsatz Sozialversicherungs-Leistungsarten. Normen SGG §§ 51 77 86b 143. Prüfraster SGG-spezifische Fristen Vorverfahrens-Prüfung Leistungsarten. Output SGG-spezifisc..._

# Sozialgerichtsverfahren-Modus (SGG)

## Arbeitsbereich

Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtsermittlungsgrundsatz Sozialversicherungs-Leistungsarten. Normen SGG §§ 51 77 86b 143. Prüfraster SGG-spezifische Fristen Vorverfahrens-Prüfung Leistungsarten. Output SGG-spezifischer Aktenauszug. Abgrenzung zu verwaltungsprozess-modus (VwGO) und arbeitsgerichtsverfahren-modus (ArbGG). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor Aktivierung des Modus

1. Widerspruch eingelegt? Liegt Widerspruchsbescheid vor? (Klagefrist läuft ab Zustellung!)
2. Eilrechtsschutz erforderlich? (§ 86b SGG — einstweilige Anordnung oder aufschiebende Wirkung)
3. Welches SGB-Kapitel ist betroffen? (SGB II, V, VI, VII, IX, XI, XII)
4. Eigene Beweiserhebung des Gerichts (§ 103 SGG) — wurden Sachverständige oder Aktenbeiziehung angeordnet?

## Zentrale Normen (SGG / SGB)

- § 84 SGG — Widerspruchsfrist 1 Monat ab Bekanntgabe
- § 87 SGG — Klagefrist 1 Monat ab Zustellung Widerspruchsbescheid
- § 86b SGG — Eilrechtsschutz (Abs. 1: aufschiebende Wirkung; Abs. 2: einstweilige Anordnung)
- § 103 SGG — Amtsermittlungsgrundsatz (Untersuchungsgrundsatz)
- § 151 SGG — Berufungsfrist 1 Monat; § 164 SGG — Revisionsfrist 1 Monat
- § 183 SGG — Keine Gerichtskosten für Versicherte (Kostenprivileg)
- § 66 Abs. 2 SGG — Jahresfrist bei fehlerhafter Rechtsbehelfsbelehrung

## Rechtsprechung (BSG / BVerfG — Leitsätze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sachgebiete der Sozialgerichtsbarkeit

- Krankenversicherung (SGB V)
- Rentenversicherung (SGB VI)
- Unfallversicherung (SGB VII)
- Arbeitsförderung (SGB III)
- Grundsicherung für Arbeitsuchende (SGB II)
- Sozialhilfe (SGB XII)
- Pflegeversicherung (SGB XI)
- Kinder- und Jugendhilfe (SGB VIII)
- Behinderung und Teilhabe (SGB IX)
- Vertragsarztrecht (SGB V, 4. Kapitel)

## Typischer Verfahrensablauf

1. Verwaltungsverfahren beim Leistungsträger
2. Erlass des Ausgangsbescheids
3. Widerspruch (§§ 83 ff. SGG)
4. Widerspruchsbescheid
5. Klage beim Sozialgericht (§ 90 SGG)
6. Berufung beim Landessozialgericht (§§ 143 ff. SGG)
7. Revision beim Bundessozialgericht (§§ 160 ff. SGG)

## Kritische Fristen (SGG)

| Frist | Norm | Dauer | Besonderheit |
|---|---|---|---|
| Widerspruchsfrist | § 84 SGG | 1 Monat | ab Bekanntgabe |
| Klagefrist | § 87 SGG | 1 Monat | ab Zustellung Widerspruchsbescheid |
| Berufungsfrist | § 151 SGG | 1 Monat | ab Zustellung Urteil |
| Revisionsfrist | § 164 SGG | 1 Monat | ab Zustellung Urteil |

**Besonderheit:** Bei fehlender oder fehlerhafter Rechtsbehelfsbelehrung gilt eine Jahresfrist (§ 66 Abs. 2 SGG).

## Eilrechtsschutz (§ 86b SGG)

| Antrag | Ziel | Norm |
|---|---|---|
| Anordnung der aufschiebenden Wirkung | VA hat keine aufschiebende Wirkung | § 86b Abs. 1 SGG |
| Einstweilige Anordnung | Vorläufige Regelung eines Rechtsverhältnisses | § 86b Abs. 2 SGG |

Eilanträge in sozialgerichtlichen Verfahren (z. B. Grundsicherungsleistungen) sind häufig zeitkritisch — im Aktenauszug besonders hervorheben.

## Amtsermittlungsgrundsatz (§ 103 SGG)

Das Sozialgericht ermittelt den Sachverhalt von Amts wegen. Beweisangebote der Parteien sind möglich, aber das Gericht ist nicht daran gebunden. Im Aktenauszug daher:

- Eigene Beweiserhebungen des Gerichts (ärztliche Gutachten, Aktenbeiziehungen) gesondert erfassen
- Beigezogene Behördenakten nennen

## Besonderheiten im Aktenauszug

- Parteibezeichnungen: "Kläger/in" und "Beklagter" (Leistungsträger / Behörde)
- Streitgegenstand ist häufig ein Bescheid über Leistungsgewährung oder -versagung
- Leistungsart und Leistungszeitraum im Verfahrensidentifikationsblock aufführen
- Gutachten (ärztliche / berufskundliche) als eigene Kategorie in Beweismittel-Tabelle
- Kostenrecht: keine Gerichtskosten für Versicherte (§ 183 SGG)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

