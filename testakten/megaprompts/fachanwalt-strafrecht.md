# Megaprompt: fachanwalt-strafrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 226 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-strafrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Strafrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zus…
2. **mandat-triage-strafrecht** — Strukturierte Eingangs-Abfrage für Strafmandate: Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstr…
3. **orientierung-mandat-fachanwaltschaft** — Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafre…
4. **orientierung-fristen-form-und-zustaendigkeit** — Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.
5. **erstgespraech-mandatsannahme** — Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polize…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **output-waehlen** — Output-Wahl für Fachanwalt Strafrecht: stimmt Adressat (Beschuldigter/Angeklagter, Staatsanwaltschaft, Verletzte/Nebenkl…
8. **adhaesionsverfahren** — Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig S…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Strafrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Strafrecht

> Vorladung, Durchsuchung, U-Haft, Anklage, Revision — Verfahrensphase entscheidet alles. Identität des Beschuldigten zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 311 II StPO: 1 Woche** sofortige Beschwerde. § 314 StPO: Berufung 1 Woche ab Verkündung. § 341 StPO: Revision 1 Woche ab Verkündung; § 345 StPO: Begründung 1 Monat ab Zustellung. § 33a StPO (Haftprüfung jederzeit). § 67 OWiG: Einspruch Bußgeld 2 Wochen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Hier kein klassischer Anspruch: Tatvorwurf benennen (Norm + StGB- bzw. Nebenstrafrechts-§). Mitwirkung: Akteneinsicht § 147 StPO, Beweisantrag § 244 StPO, Verteidigerwahl § 137 StPO, Pflichtverteidigung § 140 StPO. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | AG Strafrichter / Schöffengericht (§§ 24 ff. GVG), LG große Strafkammer (§ 74 GVG), OLG (Staatsschutz, § 120 GVG). Bei Jugendlichen: JGG-Spruchkörper. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Sofortige Beschwerde (1 Woche), Revisionsfrist (1 Woche / 1 Monat) tickt ab Verkündung/Zustellung. 🟠 Hauptverhandlung in 30 Tagen — Beweisanträge vorbereiten.
- **Beweislage:** 🟠 Beschuldigtenaussage NIE ohne Akteneinsicht. 🔴 Belastungszeugen: Konfrontationsrecht Art. 6 III d EMRK ausnutzen. 🟢 Selbstanzeige § 371 AO nur nach umfassender Aktenlage.
- **Wirtschaftlich:** 🔴 Berufstauglichkeit gefährdet (Beamte, Heilberufe, Approbation): parallel berufsrechtliche Schiene mitdenken. 🟠 Vermögensabschöpfung §§ 73 ff. StGB im Blick.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Untersuchungshaft / Haftbefehl** | `strafr-haftpruefung-haftbeschwerde-workflow` | Haftbeschwerde § 304 StPO, Haftprüfung § 117 StPO, mündliche Verhandlung erzwingen |
| Akteneinsicht & Strategie | `akteneinsicht-beantragen` | Antrag § 147 StPO, Wahl Verfahrensschiene, ggf. Schweigen / Einlassungsmemo |
| Beweisantrag vorbereiten | `strafr-dysfunk-beweisantrag-fundament` | Substantiierte Tatsachenbehauptung, Beweismittel, Konnexität |
| Revision prüfen | `revisionsbegruendung-paragraf-344-stpo` | Sach- vs. Verfahrensrüge, absolute Revisionsgründe § 338 StPO |
| Wirtschafts-/Vermögensabschöpfung | `strafr-vermoegensabschoepfung-spezial` | Einziehung §§ 73 ff. StGB, vermögenssichernde Maßnahmen § 111b StPO |

## Norm-Radar (live verifizieren)

- **§ 147 StPO** — Akteneinsicht des Verteidigers
- **§ 137 StPO** — Recht auf Verteidiger jederzeit
- **§ 244 StPO** — Beweisantragsrecht
- **§ 117 StPO** — Haftprüfung
- **§ 341 StPO** — Revisions-Einlegungsfrist (1 Woche)
- **§ 73 StGB** — Einziehung von Taterträgen

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Verfahrensphase** läuft (Ermittlung · Anklage · Hauptverhandlung · Rechtsmittel · Vollstreckung), und sitzt der Mandant **in Haft**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verständigung § 257c StPO; Mitteilungspflichten** — BVerfG 2. Senat; BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`
- **Beweisantragsrecht § 244 StPO; Konnexität** — BGH-Strafsenate — *live verifizieren auf* `bundesgerichtshof.de`
- **Faires Verfahren / Konfrontationsrecht Art. 6 III d EMRK** — EGMR — *live verifizieren auf* `hudoc.echr.coe.int`
- **Einziehung §§ 73 ff. StGB; verfassungsrechtliche Grenzen** — BVerfG / BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-strafrecht`

_Strukturierte Eingangs-Abfrage für Strafmandate: Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungsha..._

# Strukturierte Eingangs-Abfrage für Strafmandate


## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Plaedoyer Vorbereitung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Strafrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Akteneinsicht § 147 StPO, Rechtsmittel und U-Haft-Eskalation. Routing zu Akteneinsicht, Haftmanagement und Strafprozess-Cockpit.

### Mandat-Triage Strafrecht

## Ablauf — acht Fragen

### Frage 1 — Wer ruft an und für wen?

- Beschuldigter selbst
- Angehöriger
- Polizei (selten — Notdienst)
- Anderer Anwalt (Vertretung)

### Frage 2 — Akute Eilbedürftigkeit?

- Festnahme erfolgt — Vorführung läuft heute
- Untersuchungshaft seit Stunden / Tagen
- Durchsuchung läuft / steht bevor
- Aussage bei Polizei für heute terminiert
- Hauptverhandlung beginnt morgen

**Eskalation:** Festnahme U-Haft Durchsuchung → Telefon-Sofort an Anwalt; binnen einer Stunde Beistand; Anwesenheit bei Vernehmung Pflicht.

### Frage 3 — Verfahrensstadium?

- Ermittlungsverfahren bei Polizei (kein Aktenzeichen StA noch nicht)
- Ermittlungsverfahren bei Staatsanwaltschaft (Az StA vorhanden)
- Zwischenverfahren (Anklage zugestellt — Eröffnungsbeschluss?)
- Hauptverfahren (Hauptverhandlungstermin)
- Berufung / Revision
- Strafvollstreckung
- Strafvollzug (Vollzugsplan Lockerungen Strafaussetzung)

### Frage 4 — Tatvorwurf?

- Norm (§ ggf. StGB Nebengesetz)
- Strafrahmen — Vergehen unter ein Jahr Vergehen ab ein Jahr Verbrechen ab ein Jahr Mindeststrafe (§ 12 StGB)
- Bei Verbrechen oder Strafrahmen ab ein Jahr — notwendige Verteidigung § 140 StPO

### Frage 5 — Haftsituation?

- In Freiheit
- Vorgeführt — Vorführungsbeschluss / Haftbefehl?
- Untersuchungshaft — Haftgründe (Flucht-, Verdunkelungs-, Wiederholungs-)
- Strafvollzug

### Frage 6 — Mitbeschuldigte?

- Wer ist mitbeschuldigt?
- Ist Mitbeschuldigter bereits anwaltlich vertreten?
- Konflikt-Check § 43a Abs. 4 BRAO § 146 StPO Mehrfachverteidigung verboten

### Frage 7 — Aktenstand?

- Aktenstand nachgefragt?
- Akteneinsicht beantragt § 147 StPO
- Bei U-Haft haftrelevante Informationen nach § 147 Abs. 2 S. 2 StPO sichern; in der Regel Akteneinsicht

### Frage 8 — Wirtschaftliche Verhältnisse / Pflichtverteidigung?

- Pflichtverteidigung § 140 § 141 StPO bei notwendiger Verteidigung
- Vergütung nach RVG plus eventuell Honorarvereinbarung

## Routing-Matrix

| Verfahrensstadium | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| U-Haft | `strafprozess-haft-und-besuchsmanagement` | Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Sechs-Monats-Kontrolle § 121 StPO |
| Vorfeld Durchsuchung | Beschwerde § 304 StPO | ggf. nicht statthaft wenn beendet — Feststellungsantrag |
| Polizei-Vernehmung steht an | Verteidigerbeistand § 168c StPO | Termin verlegen oder begleiten |
| Anklage zugestellt | Stellungnahme zur Eröffnung | Frist nach § 201 StPO |
| Anzeige/Anklage § 188 StGB | `strafrecht-spezial-188-stgb-easy-verteidigung` | Strafantrag/besonderes öffentliches Interesse § 194 StGB, vollständiger Äußerungskontext, Art. 5 GG |
| Strafbefehl § 188 StGB | `strafrecht-spezial-188-stgb-anklage-und-strafbefehl` | Einspruch § 410 StPO binnen zwei Wochen ab Zustellung |
| Hauptverhandlung | `akteneinsicht-strafrecht-auswerten` | Beweisanträge vor Schluss Beweisaufnahme |
| Berufung/Revision | `strafprozess-rechtsmittel-und-notfristencockpit` | Berufung/Revision Einlegung binnen 1 Woche; Revisionsbegründung § 345 StPO gesondert berechnen |

## Konflikt-Check

- Mehrfachverteidigung verboten § 146 StPO
- § 43a Abs. 4 BRAO Interessenkollision
- Frühere Vertretung von Mitbeschuldigtem oder Geschädigtem prüfen

## Sofort-Fristen

- **Haftprüfung** § 117 Abs. 1 StPO — jederzeit
- **Haftbeschwerde** § 304 StPO — keine gesetzliche Wochenfrist wie bei sofortiger Beschwerde, aber praktisch sofort vorbereiten
- **Sechs-Monats-Prüfung** OLG § 121 StPO
- **Einspruch Strafbefehl** § 410 StPO zwei Wochen
- **Berufung** § 314 StPO eine Woche
- **Revision** § 341 StPO eine Woche; Revisionsbegründung § 345 StPO grundsätzlich ein Monat nach Ablauf der Einlegungsfrist, bei späterer Urteilszustellung ab Zustellung

## Eskalationspfad

- **Telefon-Sofort** Vorführung Untersuchungshaft Durchsuchung Vernehmung-Termin heute
- **Binnen einer Stunde** Anfahrt zur Vernehmung — Verteidigerbeistand
- **Heute** Akteneinsichtsantrag § 147 StPO, Haftprüfung § 117 StPO oder Haftbeschwerde § 304 StPO prüfen
- **Diese Woche** Stellungnahme Anklage Berufungseinlegung

## Ausgabe

- `triage-protokoll-strafrecht.md` mit acht Fragen
- Aktenanlage Az-Vorschlag
- Fristenbuch-Eintrag (Hauptfrist Vorfrist)
- Mandatsvereinbarung Vorlage mit Pflichtverteidigerbestellungs-Antrag falls notwendig
- Empfehlung Folge-Skill plus Begründung

## Quellen

- StPO §§ 117 121 137 140 141 146 147 168c 201 304 314 341 410
- StGB § 12 (Verbrechen-Vergehen)
- BRAO § 43a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Triage-Check

- § 112 StPO — Haftbefehl (Flucht-, Verdunkelungs-, Wiederholungsgefahr)
- § 117 StPO — Haftpruefungsantrag (jederzeit)
- § 118a StPO — Haftpruefungstermin mit muendlicher Verhandlung
- § 140 StPO — notwendige Verteidigung (Bestellungsgrunde)
- § 141 StPO — Pflichtverteidiger-Bestellung (Zeitpunkt, Ablauf)
- § 146 StPO — Verbot Mehrfachverteidigung
- §§ 10 ff. GwG — Identifizierungspflichten Sorgfaltspflichten Rechtsanwalt

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden: Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverte..._

# Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden


## Arbeitsbereich

**Orientierung** ordnet den Fall über die tragenden Prüfungslinien: Orientierung im Strafrecht-Mandat und Fallrouting, Untersuchungshaft und Haftprüfung nach §§ 112 ff, Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a. Arbeite zuerst die tragende Rechtsfrage heraus; Nebenaspekte werden nur verarbeitet, soweit sie Frist, Zuständigkeit, Beweislast oder das konkrete Arbeitsprodukt tatsächlich beeinflussen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zur richtigen Prüfungslinie. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme.

### Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin für Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Ueberblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjährungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `orientierung-fristen-form-und-zustaendigkeit`

_Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg._

# Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** StPO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Strafrecht-Orientierung Fristen / Form / Zuständigkeit Bausteine
- **Sachliche Zuständigkeit GVG:**
 - **Strafrichter § 25 GVG:** Privatklagen § 374 StPO; allgemein bis Freiheitsstrafe 2 Jahre, sofern nicht hoeher beantragt.
 - **Schoeffengericht § 28 GVG:** bis Freiheitsstrafe 4 Jahre; alle Strafsachen, die nicht zu hoher Strafkammer oder Strafrichter gehoeren.
 - **Grosse Strafkammer § 76 GVG:** alle Strafsachen ab 4 Jahre erwarteter Freiheitsstrafe; bestimmte Wirtschaftsstrafsachen.
 - **Schwurgericht § 74 II GVG:** Toetungsdelikte §§ 211 ff. StGB, Eingriff in Verkehr mit Todesfolge.
 - **Oberlandesgericht § 120 GVG:** Staatsschutzdelikte (Hochverrat, Landesverrat, Terror).
- **Oertliche Zuständigkeit StPO:**
 - **§ 7 StPO:** Tatort - regelmaessig massgeblich.
 - **§ 8 StPO:** Wohnsitz Beschuldigter.
 - **§ 9 StPO:** Ergreifungsort.
 - **§ 13 StPO:** Verbundene Verfahren.
- **Fristen-Uebersicht (StPO):**
 - **Einspruch Strafbefehl § 410 StPO: 2 Wochen** ab Zustellung.
 - **Berufung § 314 StPO: 1 Woche** ab Verkuendung; Begruendung optional.
 - **Revision § 341 StPO: 1 Woche** Einlegung + § 345 StPO **1 Monat** Begruendung ab Zustellung schriftliche Urteilsausfertigung.
 - **Beschwerde § 311 StPO: 1 Woche** sofortige; § 304 StPO einfache unbefristet.
 - **Wiedereinsetzung § 44 StPO: 1 Woche** ab Wegfall des Hindernisses.
 - **Klageerzwingungsverfahren § 172 II StPO: Antrag 1 Monat** ab Bescheid GenStA.
- **Form-Re-Check:**
 - **Schriftform** zwingend für Rechtsmittel (Berufung, Revision, Beschwerde) und Einspruch.
 - **Unterschrift** Verteidiger / Mandant.
 - **Vollmacht** bei Vertretung.
 - **Begruendungs-Pflicht** Revision (Sach- oder Verfahrensruege; § 344 II StPO Substantiierung Verfahrensruege).
- **Rechtsweg:**
 - AG -> LG (Berufung § 312 StPO) -> OLG (Revision § 333 StPO bei LG-Urteil 1. Instanz oder Berufungsurteil).
 - **Sprungrevision § 335 StPO** moeglich (Sprung Berufung).
 - **Wiederaufnahme § 359 StPO** bei neuen Tatsachen / Beweismitteln.
- **EMRK Art. 6:** angemessene Verfahrensdauer als Korrektiv (Strafmilderung BGH-Linie).

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen: Erstgespraeach und Mandatsannahme im Strafrecht: Anwen..._

# Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen. § 136 StPO Belehrung Schweigerecht, § 137 StPO Verteidigerrecht, § 147 StPO Akteneinsicht. Prüfraster Konflikt-Check, Schweigerecht kommunizieren, Sachverhalt aufnehmen, Akteneinsicht beantragen, Honorarvereinbarung treffen. Output Mandats-Aufnahmeprotokoll mit Sofortmassnahmen-Liste und Belehrungsprotokoll. Abgrenzung zu Wahlverteidiger-Mandat für spezifischen Mandatstyp und zu Mandat-Triage.

### Erstgespraech und Mandatsannahme im Allgemeines und Wirtschaftsstrafrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Allgemeines und Wirtschaftsstrafrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; oft mit Vorladung, Strafbefehl, Durchsuchungsbeschluss, Anklageschrift, U-Haft-Anordnung, Anhörung als Zeuge oder Anklageschrift mit Nebenklage-Option.
- Vor jeder weiteren Bearbeitung: erst Annahme klaeren, Rolle bestimmen (Beschuldigte/r, Verletzte/r oder Nebenklage, Zeuge/in mit Beistand), Konflikt- und GwG-Pruefung, Vollmacht, Gebührenvereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Rollenklarheit und Konstellation (10-15 Min.)

Erste Frage: Wofür braucht Mandantschaft Sie?

- **Beschuldigte oder Angeklagte** - Verteidigung im Strafverfahren.
- **Verletzte oder Anzeigeerstattende** - Beratung, Strafanzeige, Akteneinsicht der Verletzten, ggf. Nebenklage-Anschluss.
- **Zeuginnen oder Zeugen** - Zeugenbeistand gemaess § 68b StPO, Auskunftsverweigerungsrecht gemaess § 55 StPO.
- **Insolvenzverwalter/Geschaeftsfuehrung** mit StA-Berlin-Beruehrung - paralleles Insolvenz-/Strafverfahren.

Standard-Fragenraster:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle und Aktenzeichen StA / Gericht).
- Tatvorwurf in einem Satz (StGB-Paragraf, OWiG, Nebenstrafrecht).
- Konkrete fachliche Stossrichtung: Akteneinsicht, Beschuldigtenvernehmung, U-Haft, Strafbefehl-Einspruch, Hauptverhandlung, Revision, Anklage gegen Beschuldigte/n als Nebenklage.
- Bisherige Korrespondenz (Vorladung, Anhörungsbogen, Durchsuchung, Bescheide).
- **Fristenscreening sofort:** Einspruch gegen Strafbefehl 2 Wochen (§ 410 Abs. 1 StPO), Revisionseinlegung 1 Woche (§ 341 StPO), Revisionsbegruendung 1 Monat (§ 345 StPO), Klageerzwingung 1 Monat (§ 172 Abs. 2 StPO), Antrag auf gerichtliche Entscheidung (§ 23 EGGVG) 1 Monat, Beschwerdefristen § 311 StPO.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Mit-Beschuldigte, Verletzte, frueheres Mandat?
- Bei Mehrfach-Beschuldigten zwingend pro Person eigene Verteidigung (§ 146 StPO).
- GwG-Identifizierung: amtlicher Lichtbildausweis, bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Auslandsbezug, Vermoegensherkunft, Tatvorwurf (insbesondere § 261 StGB Geldwaesche, § 370 AO Steuerhinterziehung).
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG, BRAK-Identifizierungsleitfaden).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Vollmacht und Akteneinsicht

- Strafprozessvollmacht (§§ 137 ff. StPO, BORA, RVG).
- Akteneinsichtsantrag gemaess § 147 StPO (Verteidigung) oder § 406e StPO (Verletzten-/Nebenklagevertretung) oder ohne Sondervorschrift für Zeugenbeistand.
- Bei Pflichtverteidigerbestellung Antrag gemaess § 141 StPO frueh stellen (Belehrung gemaess § 136 Abs. 1 S. 3 StPO).
- Bei Nebenklage: Anschlusserklaerung gemaess § 396 StPO und Pruefung der Nebenklage-Befugnis gemaess § 395 StPO.

### 4. Gebührenvereinbarung im Strafverfahren

Strafrechtsspezifische Gebührentatbestaende statt zivilrechtlicher Streitwert-Logik:

- **RVG-Strafsachen-Tatbestaende** (VV-RVG Teil 4 Abschnitt 1): Grundgebuehr Nr. 4100, Verfahrensgebuehr Ermittlungsverfahren Nr. 4104, Verfahrensgebuehr Gerichtsverfahren erster Instanz Nr. 4106 oder 4112 bzw. 4118 je nach Gericht, Terminsgebuehr Nr. 4108 bzw. Nr. 4114 bzw. Nr. 4120, Hauptverhandlungstag-Zuschlag bei Strafkammer.
- **Bei Bussgeldverfahren:** VV-RVG Teil 5 (Nrn. 5100 ff.).
- **Pflichtverteidigung:** Festgebuehren gemaess RVG-Tabelle Teil 4 Abschnitt 1 mit besonderem Gebührentatbestand für den bestellten Verteidiger.
- **Vereinbarungshonorar / Stundenhonorar:** zulaessig nach § 3a RVG mit Schriftform und ausdruecklichem Hinweis; oberhalb der gesetzlichen Gebuehr ueblich bei Wirtschaftsstrafrecht.
- **Erfolgshonorar:** nur in engen Grenzen gemaess § 4a RVG; im Strafverfahren regelmaessig problematisch (kein Erfolg im klassischen Sinne, Risiko des Wertungs-Widerspruchs).
- **Vorschuss:** Vorschussanforderung nach § 9 RVG, in Strafsachen ueblich pro Instanz oder pro Hauptverhandlungstag.
- **Bei Nebenklage:** Gebühren VV-RVG Teil 4 Abschnitt 2 (Nrn. 4124 ff.). Streitwert-Aequivalent nur für adhaesionsrechtliche Anspruche relevant.
- **Bei Adhaesion (§§ 403 ff. StPO):** Gebühren VV-RVG Teil 4 Abschnitt 6 (Nrn. 4143-4147), berechnet nach Gegenstandswert des geltend gemachten Anspruchs.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Verteidigung durch alle Instanzen) oder begrenzt (nur Akteneinsicht und Gutachten, nur Erstellung Einspruch gegen Strafbefehl, nur Zeugenbeistand für einen Vernehmungstermin).
- **Verweisen:** wenn Spezialgebiet ausserhalb (Wirtschaftsstrafrecht vs. allgemeines Strafrecht), oertlich unzuständig oder Mehrfachbeschuldigtenkonstellation.
- **Ablehnen:** Konflikt mit § 146 StPO, GwG-Hit beim Honorar, fehlende Vertrauensbasis.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Rolle, Konflikt-Check, GwG-Status, Tatvorwurf, Aktenzeichen.
2. **Frist-Liste** (Einspruch, Revisionseinlegung, Revisionsbegruendung, Beschwerdefristen, Anschluss-Frist Nebenklage, U-Haft-Pruefungsfristen § 121 StPO).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Bescheide, Schreiben, Anhörungsbogen).
4. **Naechster-Schritt-Plan:** binnen 24 / 48 / 72 h, Owner, Output (Akteneinsicht stellen, Pflichtverteidigerbeiordnung beantragen, U-Haft-Beschwerde).
5. **Honorarvereinbarung** unterschrieben oder Hinweis auf RVG-Festgebuehr / Pflichtverteidiger-Beiordnung.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO Strafrecht (§ 13 FAO).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- StGB, StPO, BtMG, AO (§§ 369 ff.), OWiG, JGG, Nebenstrafrecht (StVG, WaffG, KCanG, AWG, WiStrG 1954).
- RVG mit VV-RVG Teil 4 (Strafsachen) und Teil 5 (Bussgeldsachen).
- DSGVO und BDSG für den Umgang mit Mandanten- und Verletzten-Daten.

## Typische Fehler im Erstgespraech

- Rolle der Mandantschaft nicht klar getrennt - Mehrfachvertretung Beschuldigter und Nebenklaegerin im gleichen Verfahren ist berufsrechtswidrig.
- Frist uebersehen, weil Mandantschaft sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen, insbesondere Strafbefehl mit Zustellungsdatum).
- Pflichtverteidiger-Antrag erst spaet gestellt - Vergutungsrisiko für Wahlverteidiger bis Beiordnung.
- Akteneinsicht zu spaet beantragt - Hauptverhandlungsvorbereitung leidet.
- Honorarvereinbarung muendlich oder ohne § 3a-RVG-Form - Honorar nur in Hoehe der gesetzlichen Gebuehr durchsetzbar.
- GwG-Pruefung verfehlt - Risiko § 261 StGB beim Honorar-Bezug aus inkriminierter Quelle.

## Praxis-Checkliste

- [ ] Rolle der Mandantschaft eindeutig festgestellt
- [ ] Personalien und Aktenzeichen aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt (auch Mit-Beschuldigte gemaess § 146 StPO)
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Strafprozessvollmacht unterschrieben
- [ ] Akteneinsicht beantragt (§ 147 oder § 406e StPO)
- [ ] Pflichtverteidigerbestellung beantragt, soweit Voraussetzungen vorliegen (§ 140 StPO)
- [ ] Honorarvereinbarung schriftlich (§ 3a RVG) oder Hinweis auf RVG-Festgebuehr
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Strafbefehl mit Einspruchsfrist

Mandantschaft bringt Strafbefehl am Donnerstag, Einspruchsfrist 2 Wochen ab Zustellung. Handlungs-Sequenz:

1. Zustellungsdatum aus Strafbefehl auslesen (Zustellungsurkunde, EB).
2. Akteneinsicht (§ 147 StPO) sofort schicken.
3. Einspruch fristwahrend einlegen, Begruendung nachreichen.
4. Wiedereinsetzung in den vorigen Stand (§§ 44 ff. StPO) als Reserve dokumentieren.

### Konstellation B: U-Haft

Mandantschaft sitzt seit Wochen in U-Haft. Pflichtverteidiger noch nicht beantragt.

1. Pflichtverteidigerbestellung beantragen (§ 140 Abs. 1 Nr. 4 StPO).
2. Akteneinsicht beantragen, soweit § 147 Abs. 2 StPO nicht entgegensteht.
3. Haftpruefung (§ 117 StPO) oder Haftbeschwerde (§ 304 StPO).
4. Mandantengespraech in der JVA terminieren (Sprecherlaubnis).

### Konstellation C: Verletzte/r mit Nebenklage-Option

Mandantschaft ist Opfer einer Sexualstraftat oder schweren Koerperverletzung.

1. Akteneinsichtsantrag für Verletztenvertretung (§ 406e StPO).
2. Pruefung Nebenklagebefugnis (§ 395 StPO).
3. Antrag auf Beiordnung als Opferanwalt (§ 397a StPO).
4. Adhaesion (§§ 403 ff. StPO) und psychosoziale Prozessbegleitung (§ 406g StPO) erwaegen.
5. Cross-Ref: `fachanwalt-strafrecht-nebenklage-opfervertretung`.

### Konstellation D: Zeuge mit Auskunftsverweigerungsrecht

Mandantschaft hat Vorladung als Zeuge in einem Verfahren erhalten, ist aber selber Mit-Beschuldigte/r in anderer Sache.

1. Pruefung § 55 StPO (Selbstbelastungsgefahr) und § 52 StPO (Angehoerigenstellung).
2. Zeugenbeistand gemaess § 68b StPO; Beiordnung gemaess § 68b Abs. 2 StPO bei Bedrohung.
3. Vorbereitung der Aussage und Auskunftsverweigerung in der Vernehmung.
4. Cross-Ref: `fachanwalt-strafrecht-zeugenbeistand`.

### Konstellation E: Wirtschaftsstrafverfahren mit Insolvenzantrag der StA

Mandantschaft ist Geschaeftsfuehrer/in einer GmbH; StA hat Insolvenzantrag gemaess § 14 InsO gestellt, parallel laeuft Strafverfahren wegen Insolvenzverschleppung (§ 15a InsO) oder Untreue (§ 266 StGB).

1. Doppelgleisige Strategie: Strafverteidigung + Insolvenzverteidigung.
2. Pruefung Anhörungsantraege im InsO-Verfahren.
3. Vermoegensabschoepfung gemaess §§ 73 ff. StGB und Beschlagnahme gemaess § 111b StPO im Auge behalten.
4. Cross-Ref: `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft`.

## Mandanten-Erwartungsmanagement

- Realistische Strafmass- und Bewaehrungs-Prognose (nicht: "Wir bekommen sicher Freispruch").
- Verfahrensdauer: Ermittlungsverfahren Wochen bis Monate, Hauptverhandlung Termine pro Instanz, Revision mehrere Monate.
- Verstaendigungschance gemaess § 257c StPO und Einstellung gemaess § 153a StPO als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Mandatsbogen-Muster (Mindestinhalt für Strafsachen)

- Mandantschaft (Name, Geburtsdatum, Anschrift, Telefon, E-Mail).
- Rolle (Beschuldigte, Nebenklaegerin, Zeugin, Insolvenzschuldnerin/GF).
- Aktenzeichen StA / Gericht / Polizei.
- Tatvorwurf (Paragraf, Tatzeit, Tatort).
- Kurzbeschreibung Sachverhalt (5-10 Saetze).
- Ziel des Mandats (eine Zeile).
- Strittige Fragen (bullet).
- Geprueft: Konflikt - GwG - Vollmacht.
- Gebührentatbestaende (Nrn. 4100 ff. VV-RVG / Vereinbarung).
- Frist-Liste.
- Aktenanlage Datum.
- Naechster-Schritt.

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für Verstaendigung gemaess § 257c StPO, Einstellung gemaess § 153a StPO und Adhaesion.
- `schriftsatzkern-substantiierung` (im selben Plugin) für Verteidigungsschriftsaetze (Einspruch, Revision, Klageerzwingung).
- `fachanwalt-strafrecht-nebenklage-opfervertretung` (im selben Plugin) für Verletzten- und Nebenklagevertretung.
- `fachanwalt-strafrecht-zeugenbeistand` (im selben Plugin) für Zeugenbeistand gemaess § 68b StPO.
- `fachanwalt-strafrecht-adhaesionsverfahren` (im selben Plugin) für Adhaesion.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` (im selben Plugin) für parallelen Insolvenzantrag der StA.
- `kanzlei-allgemein` für Konflikt-, GwG- und Aktenanlage-Routinen.

## Aktuelle Rechtsprechung Erstgespraech / Mandatsannahme

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Erstgespraech Normen-Check

- § 136 Abs. 1 StPO — Beschuldigtenbelehrung: Schweigerecht, Verteidigerwahl
- § 137 StPO — freie Wahl des Verteidigers
- § 140 StPO — notwendige Verteidigung: Katalog der Pflichtfaelle
- § 146 StPO — Verbot Mehrfachvertretung
- §§ 10-17 GwG — Identifizierung, Risikoeinschaetzung, Dokumentation
- § 261 StGB — Geldwaesche: Strafbarkeit auch des Verteidigers bei Vorsatz/Leichtfertigkeit
- § 3a RVG — schriftliche Honorarvereinbarung; Mindestangaben

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** StPO.

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

## Strafrecht-Fachanwalt Erstpruefung Bausteine
- **Mandantenrolle praezisieren:**
 - **Beschuldigter / Angeklagter:** Verteidigerbestellung § 137 StPO; ggf. notwendige Verteidigung §§ 140-141 StPO.
 - **Geschaedigter / Nebenklage § 395 StPO:** Antrag Anschluss; Antragsdelikte (§§ 174-184k StGB, § 230 StGB, § 263a StGB); Zeugnis-Beistand § 68b StPO.
 - **Adhaesionsverfahren §§ 403-406c StPO:** zivilrechtliche Anspruchsverfolgung im Strafverfahren.
 - **Zeuge:** §§ 52 StPO Angehoerigenzeugnis; § 55 StPO Auskunftsverweigerung; Zeugnisbeistand.
 - **Klageerzwingung § 172 StPO:** Verletzter beantragt Erhebung der öffentlichen Klage.
- **Verfahrensstand-Triage:**
 - **Ermittlungsverfahren:** Akteneinsicht § 147 StPO; Stellungnahme StA; Schweigerecht § 136 StPO.
 - **Zwischenverfahren §§ 199-211 StPO:** Eroeffnungsbeschluss-Pruefung; Einwaende § 201 StPO; Hilfsbeweisantraege.
 - **Hauptverhandlung:** Beweisantraege § 244 StPO; Verstaendigung § 257c StPO; Schlussvortrag.
 - **Rechtsmittel:** Berufung § 314 StPO (1 Woche); Revision §§ 341, 345 StPO (1 Woche / 1 Monat); Beschwerde § 304 StPO.
 - **Vollstreckungsverfahren:** Strafrest § 57 StGB; Bewaehrungswiderruf § 56f StGB.
- **Tatvorwurfsklasse:**
 - **Vergehen § 12 II StGB** (Mindeststrafe unter 1 Jahr): Strafbefehl § 407 StPO moeglich.
 - **Verbrechen § 12 I StGB** (Mindeststrafe 1 Jahr): notwendige Verteidigung § 140 I Nr. 2 StPO; Schwurgericht / grosse Strafkammer.
- **Mandantenziel-Hierarchie:**
 - Schuldspruch vermeiden (Freispruch).
 - Einstellung §§ 153, 153a StPO.
 - Strafmilderung.
 - Bewaehrung sichern (§ 56 StGB).
 - Reputation schuetzen (BZRG, FZR, Berufsrecht).
- **Honoraranfrage / Verguetungsvereinbarung § 3a RVG schriftlich** wenn Wahlanwaltsmandat; bei Pflichtverteidigung Festbetragstarif RVG VV 4100 ff.

---

## Skill: `output-waehlen`

_Output-Wahl für Fachanwalt Strafrecht: stimmt Adressat (Beschuldigter/Angeklagter, Staatsanwaltschaft, Verletzte/Nebenkläger), Frist (Revision 1 Woche/1 Mon. § 341 StPO) und Form auf den Zweck ab — typische Outputs: Akteneinsicht-Antrag, Beweisantrag, Plädoyer._

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Fachanwalt Strafrecht** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `workflow-redteam-qualitygate` — Adhaesionsverfahren Ermittlungsverfahren
- `strafrecht-spezial-aussagepsychologie-staatsanwaltschaft-replik` — Aussagepsychologie Staatsanwaltschaft
- `chatcontrol-csam-anwaltsgeheimnis-53-stpo` — Chatcontrol Csam Einlassung Vorbereiten
- `ergaenzt-mandantenkommunikation-entscheidungsvorlage` — Ergaenzt Fachanwalt Insolvenzantrag RED Team Korrektur
- `fa-strafrecht-quellen-frist-next` — FA Strafrecht Quellen Frist Next
- `freiheitsstrafe-paragraf-57-stgb` — Freiheitsstrafe Paragraf 57 STGB
- `hauptverhandlung-quellenkarte` — Hauptverhandlung Quellenkarte
- `strafrecht-spezial-koerperverletzung-223-stgb-grund` — Koerperverletzung STGB Todesfolge
- `mandat-triage-strafrecht` — Mandat Triage Plaedoyer Vorbereitung
- `nebenklage-compliance-dokumentation-und-akte` — Nebenklage Nebenstrafrecht Opfervertretung
- `notwehr-paragraf-32-stgb` — Notwehr Paragraf 32 STGB
- `orientierung-mandat-fachanwaltschaft` — Orientierung
- `strafrecht-spezial-raub-249-stgb` — Raub Rechtsbeugung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Beschuldigter, Strafverteidiger, Staatsanwaltschaft, Ermittlungsrichter, Vorsitzender, Schöffen, Zeuge, Nebenkläger, JVA, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Strafrecht und Strafprozessrecht (StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 53, 53a, 100a, 100b, 102, 105, 112, 116, 136, 137, 140, 141, 147, 152, 153, 153a, 160, 163a, 168c, 169, 170, 200, 201, 203, 244, 257c, 261, 264, 265, 267, 268, 304, 341, 344, 349) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `adhaesionsverfahren`

_Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess: Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereite..._

# Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess. §§ 403-406c StPO Adhaesionsverfahren, § 823 BGB Schadensersatz, § 253 BGB Schmerzensgeld. Prüfraster Zulässigkeit im Strafverfahren, Antragsschrift-Anforderungen, Beweisangebot, taktische Abwaegung Adhaesion vs. separater Zivilprozess. Output Adhaesionsantrag mit Schadensaufstellung und taktischer Einordnung. Abgrenzung zu Taeter-Opfer-Ausgleich § 46a StGB und zu Verständigung § 257c StPO.

### Adhäsionsverfahren im Strafverfahren

## Kernsachverhalt & Mandantenfragen

Das Adhäsionsverfahren verbindet Strafprozess und Zivilrecht. Es spart der verletzten Person eine eigenständige Zivilklage. Gleichzeitig ist es für die Verteidigung ein Instrument zur Schadensminimierung: Ein Adhäsionsvergleich kann das Strafmaß erheblich beeinflussen (§ 46a StGB).

**8 Kaltstart-Rückfragen:**

1. Was ist die konkrete Straftat und wann wurde sie begangen? Liegt ein Aktenzeichen vor?
2. Welche zivilrechtlichen Schäden sind entstanden: Körperverletzung (Schmerzensgeld), Vermögensschaden (Betrug, Diebstahl), Sachschäden, Verdienstausfall?
3. Liegen ärztliche Atteste, Behandlungsberichte oder Gutachten zur Schadenshöhe vor?
4. Hat die Versicherung (z.B. Krankenversicherung, Unfallversicherung) bereits Leistungen erbracht? Forderungsübergang nach § 116 SGB X prüfen.
5. Ist der/die Angeklagte zahlungsfähig? Pfändbare Vermögenswerte vorhanden oder Insolvenz droht?
6. Besteht parallele Nebenklage oder soll der Adhäsionsantrag ohne Nebenklage gestellt werden?
7. Ist ein außergerichtlicher Vergleich mit dem/der Angeklagten bereits diskutiert oder gescheitert?
8. Welcher Betrag soll konkret geltend gemacht werden, oder soll das Schmerzensgeld dem Ermessen des Gerichts überlassen bleiben?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 403 StPO | Adhäsionsrecht: Verletzte kann vermögensrechtliche Ansprüche aus der Tat im Strafverfahren geltend machen |
| § 404 StPO | Form und Inhalt des Adhäsionsantrags; schriftlich oder zu Protokoll; bis Schluss der Beweisaufnahme |
| § 405 StPO | Adhäsionsvergleich als Vollstreckungstitel; Protokollierung in der Hauptverhandlung |
| § 406 StPO | Entscheidung durch Strafgericht; Grundurteil; Absehen von Entscheidung bei Verfahrensverzögerung |
| § 406a StPO | Rechtsmittel gegen Adhäsionsentscheidung; eingeschränkte Berufungsmöglichkeit |
| § 406b StPO | Vorläufige Vollstreckbarkeit des Adhäsionsurteils |
| § 406c StPO | Vollstreckbarerklärung des Vergleichs |
| § 472a StPO | Kosten des Adhäsionsverfahrens für Verletzte: grundsätzlich kostenfrei |
| § 46a StGB | Täter-Opfer-Ausgleich und Schadenswiedergutmachung als Strafmilderungsgrund |
| § 46 Abs. 2 StGB | Strafzumessung: Schadenswiedergutmachung berücksichtigungsfähig |
| § 253 Abs. 2 BGB | Schmerzensgeld bei Körper-, Gesundheits-, Freiheitsverletzung oder sexueller Selbstbestimmung |
| §§ 249–252 BGB | Art und Umfang des Schadensersatzes; Naturalrestitution, Wertersatz |
| §§ 823–826 BGB | Deliktsrecht: Grundlagen der Schadensersatzpflicht |
| § 830 BGB | Mittäter und Beteiligte haften als Gesamtschuldner |
| § 116 SGB X | Forderungsübergang bei Sozialleistungsträgern (Krankenkasse, Rentenversicherung) |

---

## Leitentscheidungen (Stand Mai 2026)

| Aktenzeichen | Gericht / Datum | Tragende Aussage | Offene Fundstelle |
|---|---|---|---|
| 3 StR 340/24 | BGH (3. Strafsenat), Beschluss 09.01.2025 | Adhäsionsentscheidung im Strafverfahren — Begründungsanforderungen an Schmerzensgeldzumessung; Strafgericht muss die maßgeblichen Zumessungsgesichtspunkte (Verletzungsbild, Dauer, Folgen) erkennbar machen | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.01.2025&Aktenzeichen=3+StR+340/24 |
| 4 StR 232/25 | BGH (4. Strafsenat), Beschluss 20.11.2025 | Zusammenspiel TOA / Schadenswiedergutmachung (§ 46a StGB) und Adhäsionsforderung — Strafmilderung setzt kommunikativen Aussöhnungsprozess voraus, nicht nur Zahlung | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25 |

Weitere Entscheidungen vor Verwendung live in dejure.org/openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Prüfschema Adhäsionsverfahren

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Anspruchsgrundlage prüfen: § 823 BGB (Körperverletzung, Sachschaden), § 826 BGB (sittenwidrige Schädigung bei Betrug), § 249/253 BGB (Schaden und Schmerzensgeld) | §§ 249, 253, 823 BGB |
| 2 | Verletzteneigenschaft prüfen: Nur unmittelbar Verletzte (§ 403 StPO); mittelbar Betroffene ausgeschlossen | § 403 StPO |
| 3 | Forderungsübergang prüfen: § 116 SGB X bei Krankenkassenleistungen; Eigenanteil ermitteln | § 116 SGB X |
| 4 | Schadenshöhe ermitteln: Schmerzensgeld nach Tabellen (Hacks/Slizyk); materieller Schaden beziffern; Feststellungsantrag für Zukunftsschäden | § 253 Abs. 2 BGB |
| 5 | Vollstreckungsperspektive prüfen: Zahlungsfähigkeit des/der Angeklagten; Insolvenzsituation; pfändbares Vermögen | §§ 704, 794 ZPO |
| 6 | Adhäsionsantrag formulieren: bestimmter Antrag (Zahlung, Feststellung, Herausgabe); Sachverhalt; Beweismittel | § 404 StPO |
| 7 | Fristwahrung: Antrag bis Beginn der Schlussvorträge (spätestens); frühzeitig einreichen | § 404 Abs. 1 StPO |
| 8 | Vergleichsstrategie aus Verteidigung: § 46a StGB als Strafmilderungsargument; Ratenvereinbarung vorbereiten | § 46a StGB |
| 9 | Vergleich nach § 405 StPO: In Hauptverhandlung protokollieren lassen; wird Vollstreckungstitel | § 405 StPO |
| 10 | Grundurteil und Folgeentscheidung: Bei Bezifferungsproblemen Grundurteil nach § 406 Abs. 1 S. 2 StPO; Quantifizierung im Zivilverfahren | § 406 Abs. 1 S. 2 StPO |
| 11 | Absehen-Antrag der Verteidigung: § 406 Abs. 1 S. 3–6 StPO – wenn Adhäsion Verfahren wesentlich verzögert | § 406 StPO |
| 12 | Vollstreckung: Titel nach § 794 ZPO; Gerichtsvollzieher, Forderungspfändung; bei Insolvenz: Tabellenanmeldung | § 794 ZPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Adhaesionsverfahren fuehren | Adhaesionsantrag; Template unten |
| Variante A — Mandant will Strafverfahren trennen | Zivilklage separat; Adhaesion entfaellt |
| Variante B — Strafgericht verweist Adhaesion | Nachfolge-Zivilklage; Bindungswirkung des Strafurteils |
| Variante C — Schadenshoehe unklar | Feststellungsklage zuerst; Leistungsklage nach Konkretisierung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Adhäsionsantrag auf Schmerzensgeld

```
An das [Gericht]
Aktenzeichen: [...]

Adhäsionsantrag gemäß §§ 403 ff. StPO

In der Strafsache gegen [Name Angeklagte/r]
wegen [Tatvorwurf]

beantragt die Verletzte [Name] durch ihre anwaltliche Vertretung:

1. Die/den Angeklagte/n wird verurteilt, an die Verletzte
 ein angemessenes Schmerzensgeld zu zahlen, dessen Höhe
 in das Ermessen des Gerichts gestellt wird, jedoch den
 Betrag von [z.B. 15.000 Euro] nicht unterschreiten sollte,
 nebst Zinsen in Höhe von fünf Prozentpunkten über dem
 Basiszinssatz seit Rechtshängigkeit dieses Antrags.

2. Es wird festgestellt, dass die/der Angeklagte verpflichtet
 ist, der Verletzten alle weiteren materiellen und immateriellen
 Schäden zu ersetzen, die aus der Tat vom [Datum] künftig noch
 entstehen, soweit Ansprüche nicht auf Dritte oder Sozial-
 versicherungsträger übergegangen sind.

Begründung:
Die Verletzte erlitt durch die Tat vom [Datum] folgende
Verletzungen: [konkret aufzählen]. Sie wurde [X Tage]
stationär behandelt und befand sich [X Wochen] in ambulanter
Therapie. Behandlungsunterlagen werden als Anlage 1 bis 3
beigefügt.

Das Schmerzensgeld ist nach den Grundsätzen der Ausgleichs-
und Genugtuungsfunktion (§ 253 Abs. 2 BGB) zu bemessen.
Vergleichbare Verletzungen werden in der Rechtsprechung mit
[Betragsbereich] bewertet (Slizyk, Beck'sche Schmerzensgeld-
tabelle, [aktuelle Auflage], Nr. [XX]).

[Ort, Datum]
[Unterschrift]
```

### Baustein 2 – Adhäsionsvergleich (Protokollvorlage)

```
In der Hauptverhandlung am [Datum]
Aktenzeichen: [...]

schließen die Parteien folgenden Vergleich gemäß § 405 StPO:

1. Die/der Angeklagte zahlt an die Verletzte [Name]
 zur Abgeltung sämtlicher Schmerzensgeld- und Schadens-
 ersatzansprüche aus der Tat vom [Datum] einen Betrag
 von [X Euro].

2. Zahlung erfolgt in monatlichen Raten von [X Euro]
 erstmals zum [Datum]; Gesamtfälligkeit bei Zahlungs-
 verzug mit einer Rate.

3. Mit Zahlung des Gesamtbetrags sind alle Ansprüche der
 Verletzten aus der Tat vom [Datum] abgegolten.

4. Die Gerichtskosten des Adhäsionsverfahrens trägt
 [je nach Vereinbarung].

Dieser Vergleich wird als Prozessvergleich nach § 794 Abs. 1
Nr. 1 ZPO protokolliert.

[Unterschriften beider Seiten und Gericht]
```

### Baustein 3 – Verteidigung: Antrag auf Absehen von Entscheidung § 406 Abs. 1 S. 3 StPO

```
An das [Gericht]
Aktenzeichen: [...]

Antrag auf Absehen von der Entscheidung im Adhäsionsverfahren
gemäß § 406 Abs. 1 S. 3 StPO

In der Strafsache gegen [Name Angeklagte/r]

beantragt die Verteidigung,

von einer Entscheidung über den Adhäsionsantrag der Verletzten
abzusehen, da die Entscheidung eine dem Strafverfahren nicht
angemessene Beweisaufnahme erfordern würde und das Strafver-
fahren wesentlich verzögern würde (§ 406 Abs. 1 S. 5 StPO).

Begründung:
Zur Klärung der Schadenshöhe wäre ein medizinisches Sach-
verständigengutachten einzuholen. Der Adhäsionsantrag bezieht
sich auf Schäden in Höhe von [Betrag EUR]. Die Klärung der
Kausalität zwischen Tat und behaupteten Folgeschäden bedarf
einer umfangreichen medizinischen Beurteilung, die den Rahmen
des Strafprozesses sprengt.

[Ort, Datum]
[Unterschrift Verteidigung]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Anspruchsgrundlage (§ 823 BGB) | Verletzte trägt Tatbegehung, Verletzung, Kausalität; im Adhäsionsverfahren erleichtert durch Bindungswirkung des Strafurteils zur Tat |
| Schadenshöhe (Schmerzensgeld) | Verletzte muss Mindestbetrag darlegen; Gericht schätzt nach § 287 ZPO (analog) |
| Forderungsübergang § 116 SGB X | Sozialleistungsträger zeigt Übergang an; Verletzte muss nur Eigenanteil nachweisen |
| Adhäsionsvergleich | Einigung trägt sich selbst; Vollstreckungstitel durch Protokollierung |
| Absehen wegen Verfahrensverzögerung | Gericht entscheidet von Amts wegen; Verteidigung kann Sachverhalt darlegen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Bis Schluss der Beweisaufnahme | Adhäsionsantrag muss vor Schlussvorträgen gestellt sein | § 404 StPO |
| Ab Urteilszustellung: 1 Woche | Berufung/Revision gegen Adhäsionsausspruch | § 406a StPO |
| Ab Urteilsrechtskraft | Vollstreckung aus Adhäsionsurteil beginnt | § 704, § 794 ZPO |
| 3 Jahre | Verjährung deliktsrechtlicher Ansprüche (§ 195 BGB) ab Kenntnis | § 199 BGB |
| 30 Jahre | Verjährung des titulierten Anspruchs nach § 197 BGB | § 197 BGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Adhäsionsantrag verzögert das Strafverfahren" | § 406 Abs. 1 S. 6 StPO — Absehen nur bei wesentlicher Verzögerung; Schmerzensgeld-Antrag wird durch S. 6 a. F. besonders geschützt; aktuelle Begründungsanforderungen siehe BGH 09.01.2025 — 3 StR 340/24 |
| "Forderungsübergang nach § 116 SGB X schließt Adhäsion aus" | Nur soweit Anspruch übergegangen ist; Eigenbeteiligung (Schmerzensgeld soweit nicht gedeckt) verbleibt bei der Verletzten |
| "Angeklagte/r ist insolvent; Adhäsion sinnlos" | § 302 InsO schließt Restschuldbefreiung bei vorsätzlichen unerlaubten Handlungen aus; Titel hat langfristigen Wert |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Adhäsionsantrag kostenfrei für Verletzte | § 472a StPO: keine Gerichtskosten für Verletzte im Adhäsionsverfahren |
| Anwaltsgebühren (Verletztenvertretung) | VV-RVG Nr. 4143 (Verfahrensgebühr), Nr. 4145 (Terminsgebühr), Nr. 4146 (Vergleichsgebühr); Streitwert = Adhäsionsforderung |
| Bei Beiordnung § 397a StPO | Adhäsionsgebühren zusätzlich zur Nebenklagegebühr aus Staatskasse |
| Angeklagter zahlt Kosten bei Adhäsionsverurteilung | Kosten des Adhäsionsverfahrens als Nebenfolge im Strafurteil |
| Angeklagter bei Vergleich § 405 StPO | Kostenregelung im Vergleich frei vereinbar |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Schneller Vollstreckungstitel gewünscht | Adhäsionsantrag frühzeitig stellen; Vergleich nach § 405 StPO anstreben |
| Angeklagter will Strafmilderung | Schadenswiedergutmachung proaktiv anbieten; § 46a StGB nutzen; Vergleich vor Urteil |
| Hohe Schadensummen in Betrugsfall | Adhäsion kombinieren mit Verbleib im Strafverfahren für Bindungswirkung zur Tatbegehung |
| Angeklagter ist insolvent | Adhäsion trotzdem beantragen; § 302 InsO schließt Restschuldbefreiung aus; Titel 30 Jahre vollstreckbar |
| Gericht neigt zu § 406-Absehen | Beweise vorab vollständig vorlegen; Komplexität minimieren; Schmerzensgeld pauschal schätzen lassen |
| Schmerzensgeldzumessung im Strafurteil | Begründungsanforderungen nach BGH 09.01.2025 — 3 StR 340/24 beachten; Verletzungsbild, Dauer, Folgen erkennbar machen |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-nebenklage-opfervertretung` – Nebenklage und Adhäsion kombiniert führen
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – Adhäsionsforderung in der Insolvenz des Angeklagten
- `plaedoyer-vorbereitung-strafverteidigung` – Schadenswiedergutmachung als Strafmilderungsargument
- `fachanwalt-strafrecht-zeugenbeistand` – Begleitung der Verletzten als Zeugin

---

## Quellen (Stand Mai 2026)

- BGH 09.01.2025 — 3 StR 340/24 (Adhäsion / Schmerzensgeldbegründung): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.01.2025&Aktenzeichen=3+StR+340/24
- BGH 20.11.2025 — 4 StR 232/25 (TOA § 46a StGB, kommunikativer Prozess): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- §§ 403–406c StPO, § 472a StPO: https://dejure.org/gesetze/StPO/403.html
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; weitere Rechtsprechung vor Ausgabe in dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen und Aussage verifizieren.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

