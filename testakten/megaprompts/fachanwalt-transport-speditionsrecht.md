# Megaprompt: fachanwalt-transport-speditionsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 64 Skills des Plugins `fachanwalt-transport-speditionsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Transport- und Speditionsrecht: ordnet Rolle (Absender, Frachtführer, Empfän…
2. **mandat-triage-transport-speditionsrecht** — Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs: international. Normen: §§ 407 …
3. **orientierung-mandat-fachanwaltschaft** — Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen: Normen: §§ 407 ff. HG…
4. **erstgespraech-mandatsannahme** — Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenst…
5. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
6. **quellen-livecheck** — Quellen-Live-Check für Fachanwalt Transport- und Speditionsrecht: prüft Normen (HGB §§ 407 ff. Frachtrecht, CMR (Straße)…
7. **dokumente-intake** — Dokumentenintake für Fachanwalt Transport- und Speditionsrecht: sortiert Frachtbrief, CMR-Frachtbrief, Schadensanzeige, …
8. **unterlagen-luecken** — Lücken- und Beschaffungsliste für Fachanwalt Transport- und Speditionsrecht: trennt fehlende Tatsachen von fehlenden Bel…
9. **trans-kabotage-marktzugang-spezial** — Spezialfall Kabotage und Marktzugang EU VO 1072 / 2009 und Mobility Package: zulaessige Kabotagebefoerderungen, Mindestl…
10. **trans-multimodaler-transport-spezial** — Spezialfall multimodaler Transport § 452 HGB und Konnossement: Haftung bei unbekanntem Schadensort, Network-Liability, T…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Transport- und Speditionsrecht: ordnet Rolle (Absender, Frachtführer, Empfänger), markiert Frist (CMR Klage 1 Jahr / 3 Jahre Vorsatz), wählt Norm (HGB §§ 407 ff. Frachtrecht, CMR (Straße), Montrealer Übk. (Luft)) und Zuständigkeit (Handelsgericht), leit..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Transport Speditionsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `transport-autonome-lkw-konvois-haftung-1d-stvg` — Autonome LKW CMR Schadensregulierung
- `cmr-haftung-art-17-cmr` — CMR Haftung ART 17 CMR
- `cmr-haftung` — CMR Haftung Ladungsschaden
- `cotif-schriftsatz-brief-und-memo-bausteine` — Cotif Fachanwalt Haager
- `workflow-mandantenkommunikation` — FA Transport Spedition Mandant Redteam
- `einstieg-schnelltriage-fallrouting` — FA Transport Spedition Start Chronologie Fristen
- `frachtfuehrerhaftung-paragraf-425-hgb` — Frachtfuehrerhaftung Paragraf 425 HGB
- `gefahrgut-adr-paragraf-9-gefstoffvo` — Gefahrgut ADR Paragraf 9 Gefstoffvo
- `hgb-dokumentenmatrix-und-lueckenliste` — HGB Kabotage Beweislast Kanzlei RED Team Korrektur
- `ladungsschaden-art-23-cmr` — Ladungsschaden ART 23 CMR
- `lieferverzug` — Lieferverzug Orientierung Mandat Triage
- `luftfracht-monteral-uebereinkommen` — Luftfracht Monteral Uebereinkommen
- `marktzugang-sonderfall-edge-case` — Marktzugang Sonderfall Montrealer
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Transport Speditionsrecht sind HGB, §§ 407 ff, §§ 453 ff. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-transport-speditionsrecht`

_Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs: international. Normen: §§ 407 454 HGB, CMR. Prüfraster: Vertragstyp, Schadens..._

# Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs


## Aktenstart statt Formularstart

Wenn zu **Lieferverzug Orientierung Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Transport Speditionsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs. international. Normen: §§ 407 454 HGB, CMR. Prüfraster: Vertragstyp, Schadenstyp, Dringlichkeit, Fristen. Output: Mandat-Triage-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Erstgespraeches-Aufnahme.

### Mandat-Triage Transport- und Speditionsrecht

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Versender / Verlader
- Empfänger
- Frachtführer
- Spediteur
- Lager-Betreiber
- Versicherer (Cargo Verkehrshaftung)
- Subunternehmer / Nachunternehmer

### Frage 2 — Verkehrsträger?

- Straße — Lkw
- Schiene — Eisenbahn
- Wasser — Binnen / See
- Luft
- Multimodal — kombiniert
- Lager / Umschlag

### Frage 3 — Geografie?

- Inland
- Grenzüberschreitend EU
- Grenzüberschreitend Drittstaat
- Transit

### Frage 4 — Akute Eilbedürftigkeit?

- **Reklamationsfrist** läuft (sofort / sieben / einundzwanzig Tage)
- **Verjährungsfrist** ein Jahr läuft ab
- **Gefahrgut-Zwischenfall** ADR-Meldung
- **Embargo / Sanktionen** plötzlich greifend
- **Beschlagnahme Zoll** Akut
- **Frachtgut nicht ausgehändigt** wegen Frachtstreit
- **Versicherungs-Stichtag** läuft

### Frage 5 — Sachgebiet?

- Verlust Sendung
- Beschädigung Sendung
- Lieferfrist-Überschreitung
- Frachtforderung Frachtführer
- Speditionsvergütung
- Multimodal-Vertrag
- Gefahrgut-Recht
- Zollrecht
- Lagerlogistik
- Transport-Versicherungs-Streit
- Frachtbrief-Fälschung

### Frage 6 — Frist?

- **Reklamation Verlust erkennbar Beschädigung** sofort schriftlich
- **Reklamation verdeckter Schaden** sieben Tage CMR Art. 30 / § 438 HGB
- **Reklamation Verzug** einundzwanzig Tage
- **Verjährung CMR** ein Jahr / drei Jahre bei Vorsatz
- **Verjährung HGB** ein Jahr / drei Jahre
- **Versicherungs-Anspruch** drei Jahre § 195 BGB
- **CMR-Klage** ein Jahr nach Ablieferung

### Frage 7 — Wirtschaftliche Verhältnisse?

- Versicherung Cargo Verkehrshaftung
- Schadenshöhe vs. SDR-Begrenzung
- Streitwert für Klage
- Bei Spedition: ADSp-Geltung

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Schadensersatz Frachtführer | `frachtfuehrerhaftung-pruefen` |
| Speditionsverhalten | `frachtfuehrerhaftung-pruefen` plus ADSp Spezifika |
| Frachtforderung-Klage | (Skill frachtforderung — perspektivisch) |
| Multimodal-Vertrag | (Skill multimodal — perspektivisch) |
| Gefahrgut ADR | (Skill gefahrgut-adr — perspektivisch) |
| Zollrecht | weiter an `mandat-triage-verwaltungsrecht` plus |
| Versicherungs-Streit | weiter an `mandat-triage-versicherungsrecht` |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Versender/Frachtführer
- **Streitwert** Sendung-Wert oder Frachtforderung
- **Sachverständigen-Bedarf** Transport- und Verpackungs-SV
- **Versicherungs-Deckung** Verkehrshaftungs-Versicherung Mandant prüfen

## Eskalation

- **Telefon-Sofort** Reklamationsfrist heute / morgen Gefahrgut-Vorfall
- **Binnen einer Stunde** Schriftliche Reklamation Frachtbrief-Bemerkung
- **Heute** Auskunfts-Aufforderung an Frachtführer
- **Diese Woche** Klage vor Verjährungs-Ablauf

## Ausgabe

- `triage-protokoll-transport-spedition.md`
- Aktenanlage mit Verkehrsträger und Anwendung CMR/HGB
- Frist im Fristenbuch (Reklamation Verjährung)
- Reklamations-Schreiben sofort
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

## Quellen

- CMR 1956
- HGB §§ 407 ff. 453 ff.
- MÜ CIM CMNI
- ADSp
- BGH I. Zivilsenat
- Koller Transport-/Speditionsrecht

## Aktuelle Rechtsprechung Triage Transport

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen: Normen: §§ 407 ff. HGB, CMR, ADSP. Prüfraster: Vertragsart..._

# Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen


## Aktenstart statt Formularstart

Wenn zu **Lieferverzug Orientierung Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Transport Speditionsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen. Normen: §§ 407 ff. HGB, CMR, ADSP. Prüfraster: Vertragsart Fracht vs. Spedition, national vs. international, Schadenstyp. Output: Skillauswahl-Empfehlung Transport-Speditionsrecht. Abgrenzung: kein inhaltlicher Prüf-Skill.

### Fachanwalt für Transport- und Speditionsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 40 Fälle in den letzten drei Jahren, davon mindestens 25 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Frachtvertrag | HGB §§ 407 ff. |
| Haftung Frachtführer | HGB §§ 425 ff. (Obhutshaftung Haftungshöchstbetrag § 431) |
| Speditionsvertrag | HGB §§ 453 ff. |
| Lagervertrag | HGB §§ 467 ff. |
| Straßenverkehr international | CMR (Convention relative au contrat de transport international de marchandises par Route) |
| Eisenbahn international | COTIF / CIM (Convention concernant les transports internationaux ferroviaires) |
| Luftverkehr | Montrealer Übereinkommen 1999 |
| Seehandel | Haager Visby Regeln BGB-HGB §§ 476 ff. Hamburg-Regeln (nicht in Deutschland in Kraft) |
| Multimodaler Transport | CMR / CIM in Anwendung |
| AGB Spedition | ADSp 2017 |
| EU-Recht | RL 2009/103 Kfz-Versicherung VO 261/2004 Fluggastrechte |

## Typische Mandate

- Frachtschadens-Klage (Verlust Beschädigung Verspätung)
- Spediteurshaftung
- Haftungshöchstgrenzen § 431 HGB CMR Art. 23 Montrealer Übereinkommen Art. 22
- Reklamations- und Klagefristen
- ADSp-Anwendung (Spediteursklauseln)
- Container-Streitigkeiten in Seehandel
- Pflichtversicherung Kraftverkehr Spediteur Frachtführer
- Internationale Vollstreckung

## Fristen

- **Reklamationsfrist** HGB / CMR / Montrealer:
 - HGB § 438 — sieben Tage bei äußerlich erkennbarem Schaden binnen drei Tagen.
 - CMR Art. 30 — sofort bei Annahme Verluste / Beschädigung; sieben Tage bei nicht erkennbaren.
 - Montrealer Art. 31 — 14 Tage Beschädigung 21 Tage Verspätung.
- **Verjährung Frachtschaden** § 439 HGB — ein Jahr (drei Jahre bei Vorsatz / grob fahrlaessig).
- **CMR Art. 32** — ein Jahr (drei Jahre bei Vorsatz).
- **Klagefrist Fluggast** keine Frist im Montrealer; Verjährung zwei Jahre Art. 35 MontU.

## Hauptgerichte

- Amtsgericht / Landgericht Zivilkammer.
- OLG.
- BGH I. Zivilsenat Transportrecht (Sondersenat).
- Ausländische Gerichte bei Auslandsbezug.

## Berufsverband

- ARGE Transportrecht DAV.

## Schnittstellen

- **gesellschaftsrecht** bei Spediteur-Gesellschaft.
- **fachanwalt-internationales-wirtschaftsrecht** bei grenzüberschreitenden Transporten.
- **fachanwalt-versicherungsrecht** bei Transportversicherung.
- **kanzlei-allgemein** Fristen Versand.

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp: Normen: §..._

# Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp. Normen: §§ 407 ff. HGB, CMR, BRAO. Prüfraster: Sachverhaltserfassung, Frachtvertrag vs. Speditionsauftrag, Interessenlage, Fristen. Output: Erstgespraeches-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Klageschrift.

### Erstgespraech und Mandatsannahme im Transport-, Speditions- und Logistikrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Transport-, Speditions- und Logistikrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Transport-, Speditions- und Logistikrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Frachtvertrag, CMR, Spediteur, Versicherung, Multimodal, Zoll
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Frachtklage, Klage CMR-Schaden, Klage HGB-Spediteur-Haftung). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Transport-, Speditions- und Logistikrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Transport-, Speditions- und Logistikrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 407 ff. HGB, CMR, MC, ADSp, RVS-Konvention (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Transport-, Speditions- und Logistikrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Transport-, Speditions- und Logistikrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Hoehe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege moeglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Pruefroutinen.

## Aktuelle Rechtsprechung Erstgespraech Transport

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Erstgespraech Transport

- §§ 407-413 HGB — Frachtvertrag (Grundlagen, Pflichten, Haftung)
- § 439 HGB — Verjährung (1 Jahr ab Ablieferung; 3 Jahre bei Vorsatz)
- Art. 32 CMR — Verjährung im CMR-Verkehr
- Art. 5 CMR — Frachtbrief als Beweisurkunde
- §§ 10 ff. GwG — Identifizierungspflichten auch im Transportrechtsmandat

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** HGB, CMR, COTIF.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `quellen-livecheck`

_Quellen-Live-Check für Fachanwalt Transport- und Speditionsrecht: prüft Normen (HGB §§ 407 ff. Frachtrecht, CMR (Straße), Montrealer Übk. (Luft)) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Handelsgericht und Quellenhygiene nach references/quellenhygiene.md._

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Transport Speditionsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `transport-autonome-lkw-konvois-haftung-1d-stvg` — Autonome LKW CMR Schadensregulierung
- `cmr-haftung-art-17-cmr` — CMR Haftung ART 17 CMR
- `cmr-haftung` — CMR Haftung Ladungsschaden
- `cotif-schriftsatz-brief-und-memo-bausteine` — Cotif Fachanwalt Haager
- `workflow-mandantenkommunikation` — FA Transport Spedition Mandant Redteam
- `einstieg-schnelltriage-fallrouting` — FA Transport Spedition Start Chronologie Fristen
- `frachtfuehrerhaftung-paragraf-425-hgb` — Frachtfuehrerhaftung Paragraf 425 HGB
- `gefahrgut-adr-paragraf-9-gefstoffvo` — Gefahrgut ADR Paragraf 9 Gefstoffvo
- `hgb-dokumentenmatrix-und-lueckenliste` — HGB Kabotage Beweislast Kanzlei RED Team Korrektur
- `ladungsschaden-art-23-cmr` — Ladungsschaden ART 23 CMR
- `lieferverzug` — Lieferverzug Orientierung Mandat Triage
- `luftfracht-monteral-uebereinkommen` — Luftfracht Monteral Uebereinkommen
- `marktzugang-sonderfall-edge-case` — Marktzugang Sonderfall Montrealer
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (HGB, §§ 407 ff, §§ 453 ff) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Transport Speditionsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `dokumente-intake`

_Dokumentenintake für Fachanwalt Transport- und Speditionsrecht: sortiert Frachtbrief, CMR-Frachtbrief, Schadensanzeige, prüft Datum, Absender, Frist und Beweiswert (Lichtbilder Schaden, Übergabeprotokoll); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO._

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Transport Speditionsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Transport Speditionsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `transport-autonome-lkw-konvois-haftung-1d-stvg` — Autonome LKW CMR Schadensregulierung
- `cmr-haftung-art-17-cmr` — CMR Haftung ART 17 CMR
- `cmr-haftung` — CMR Haftung Ladungsschaden
- `cotif-schriftsatz-brief-und-memo-bausteine` — Cotif Fachanwalt Haager
- `workflow-mandantenkommunikation` — FA Transport Spedition Mandant Redteam
- `einstieg-schnelltriage-fallrouting` — FA Transport Spedition Start Chronologie Fristen
- `frachtfuehrerhaftung-paragraf-425-hgb` — Frachtfuehrerhaftung Paragraf 425 HGB
- `gefahrgut-adr-paragraf-9-gefstoffvo` — Gefahrgut ADR Paragraf 9 Gefstoffvo
- `hgb-dokumentenmatrix-und-lueckenliste` — HGB Kabotage Beweislast Kanzlei RED Team Korrektur
- `ladungsschaden-art-23-cmr` — Ladungsschaden ART 23 CMR
- `lieferverzug` — Lieferverzug Orientierung Mandat Triage
- `luftfracht-monteral-uebereinkommen` — Luftfracht Monteral Uebereinkommen
- `marktzugang-sonderfall-edge-case` — Marktzugang Sonderfall Montrealer
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Transport Speditionsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: HGB, §§ 407 ff, §§ 453 ff — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `unterlagen-luecken`

_Lücken- und Beschaffungsliste für Fachanwalt Transport- und Speditionsrecht: trennt fehlende Tatsachen von fehlenden Belegen (Frachtbrief, CMR-Frachtbrief, Schadensanzeige), nennt pro Lücke Beweisthema, Beschaffungsweg (Handelsgericht), Frist und Ersatznachweis._

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Fachanwalt Transport Speditionsrecht** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `transport-autonome-lkw-konvois-haftung-1d-stvg` — Autonome LKW CMR Schadensregulierung
- `cmr-haftung-art-17-cmr` — CMR Haftung ART 17 CMR
- `cmr-haftung` — CMR Haftung Ladungsschaden
- `cotif-schriftsatz-brief-und-memo-bausteine` — Cotif Fachanwalt Haager
- `workflow-mandantenkommunikation` — FA Transport Spedition Mandant Redteam
- `einstieg-schnelltriage-fallrouting` — FA Transport Spedition Start Chronologie Fristen
- `frachtfuehrerhaftung-paragraf-425-hgb` — Frachtfuehrerhaftung Paragraf 425 HGB
- `gefahrgut-adr-paragraf-9-gefstoffvo` — Gefahrgut ADR Paragraf 9 Gefstoffvo
- `hgb-dokumentenmatrix-und-lueckenliste` — HGB Kabotage Beweislast Kanzlei RED Team Korrektur
- `ladungsschaden-art-23-cmr` — Ladungsschaden ART 23 CMR
- `lieferverzug` — Lieferverzug Orientierung Mandat Triage
- `luftfracht-monteral-uebereinkommen` — Luftfracht Monteral Uebereinkommen
- `marktzugang-sonderfall-edge-case` — Marktzugang Sonderfall Montrealer
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Fachanwalt Transport Speditionsrecht-Frage zwingend (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), beweisrelevant, formerheblich.
- Rückfrageschreiben an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `trans-kabotage-marktzugang-spezial`

_Spezialfall Kabotage und Marktzugang EU VO 1072 / 2009 und Mobility Package: zulaessige Kabotagebefoerderungen, Mindestlohn, Entsenderecht: Spezialfall Kabotage und Marktzugang EU VO 1072 / 2009 und Mobility Package: zulaessige Kabotagebefoerderungen, Minde..._

# Spezialfall Kabotage und Marktzugang EU VO 1072 / 2009 und Mobility Package: zulaessige Kabotagebefoerderungen, Mindestlohn, Entsenderecht


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Spezialfall Kabotage und Marktzugang EU VO 1072 / 2009 und Mobility Package: zulaessige Kabotagebefoerderungen, Mindestlohn, Entsenderecht. Pruefraster Frachtfuehrer aus Drittstaat.

### Trans: Kabotage Mobility Package

## Spezialwissen: Trans: Kabotage Mobility Package
- **Normen-/Quellenanker:** EU, VO.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Skill: `trans-multimodaler-transport-spezial`

_Spezialfall multimodaler Transport § 452 HGB und Konnossement: Haftung bei unbekanntem Schadensort, Network-Liability, Through-Bill of Lading: Spezialfall multimodaler Transport § 452 HGB und Konnossement: Haftung bei unbekanntem Schadensort, Network-Liabil..._

# Spezialfall multimodaler Transport § 452 HGB und Konnossement: Haftung bei unbekanntem Schadensort, Network-Liability, Through-Bill of Lading


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Spezialfall multimodaler Transport § 452 HGB und Konnossement: Haftung bei unbekanntem Schadensort, Network-Liability, Through-Bill of Lading. Pruefraster Schadensregulierung.

### Trans: multimodaler Transport

## Spezialwissen: Trans: multimodaler Transport
- **Normen-/Quellenanker:** HGB.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

