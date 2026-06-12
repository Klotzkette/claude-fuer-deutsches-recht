# Megaprompt: patentrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 59 Skills des Plugins `patentrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Patentrecht (Verfahren, Verletzung): ordnet Rolle (Patentinhaber, Verletzer, Lizenznehm…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FT…
3. **dokumente-intake** — Dokumentenintake für Patentrecht (Verfahren, Verletzung): sortiert Patentschrift, Einspruchsschrift, Verletzungsanalyse,…
4. **rechtsabteilung-freedom-to-operate-vor-product-launch** — Rechtsabteilungs-Fachmodul für Freedom-to-Operate vor Product Launch: FTO wird mit Claim Chart, Länderpriorität und Desi…
5. **rechtsabteilung-upc-eilverfahren-und-deutsche-parallelstrategie** — Rechtsabteilungs-Fachmodul für UPC-Eilverfahren und deutsche Parallelstrategie: PI-Antrag, Schutzschrift, Bifurcation un…
6. **rechtsabteilung-employee-invention-frand** — Rechtsabteilungs-Fachmodul für Employee Invention im Konzernprojekt: Meldung, Inanspruchnahme, Vergütung und ausländisch…
7. **rechtsabteilung-proportionalitaet-schweiz** — Rechtsabteilungs-Fachmodul für Proportionalität der Unterlassung § 139 PatG: Injunction-Risiken werden für komplexe Prod…
8. **rechtsabteilung-frand-verteidigung-bei-sep-abmahnung** — Rechtsabteilungs-Fachmodul für FRAND-Verteidigung bei SEP-Abmahnung: Lizenzbereitschaft, Vergleichbarkeit und Hold-out/H…
9. **kaltstart-interview** — Kaltstart-Interview für Patentrechtsmandate. Erstellt ein kurzes Profil zu Mandant, Technik, Ziel, Territorien, Fristen,…
10. **register-patentanmeldung-anspruchsentwurf** — Prüft Patentregister und Fristen: DPMAregister, EPO Register, nationale Validierungen, Einheitspatent, Jahresgebühren, P…
11. **internationaler-patentrechts-und-laendercheck** — Routet grenzüberschreitende Patentmandate nach DE, EP, UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei und Israel; tre…
12. **patentlizenzvertrag-review** — Prüft Patentlizenzverträge: Schutzrechte, Territory, Field of Use, Exklusivität, Unterlizenzen, Royalties, Milestones, I…
13. **abmahnung-patentverletzung-verteidigung** — Verteidigt gegen Patentabmahnungen: Fristen, Unterlassungserklärung, Registerstand, Anspruchsfassung, Nichtverletzung, R…
14. **einspruch-epa-und-nichtigkeit-bpatg** — Bereitet EPA-Einspruch und deutsche Nichtigkeitsklage vor: Fristen, Zuständigkeit, Angriffsmittel, Stand der Technik, un…
15. **erfinderbenennung-arbeitnehmererfindung** — Prüft Erfinderbenennung, Rechtekette und Arbeitnehmererfindungs-Schnittstellen: wer ist Erfinder, wer ist Anmelder, Dien…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Patentrecht (Verfahren, Verletzung): ordnet Rolle (Patentinhaber, Verletzer, Lizenznehmer), markiert Frist (Einspruch EPA 9 Monate), wählt Norm (PatG, IntPatÜG, EPÜ, UPCA, ArbnErfG) und Zuständigkeit (DPMA), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Patentrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abmahnung-patentverletzung-verteidigung` — Abmahnung Patentverletzung Verteidigung
- `anspruchsentwurf-dokumentenmatrix-und-lueckenliste` — Anspruchsentwurf Dokumentenmatrix und Lueckenliste
- `beschreibung-zeichnungen-einspruch-epa-epo` — Beschreibung Zeichnungen Einspruch EPA EPO
- `einspruch-epa-und-nichtigkeit-bpatg` — Einspruch EPA und Nichtigkeit Bpatg
- `epo-epue-einspruch-beschwerde-beschraenkung` — EPO Epue Einspruch Beschwerde Beschraenkung
- `erfinderbenennung-arbeitnehmererfindung` — Erfinderbenennung Arbeitnehmererfindung
- `erfindungsaufnahme-tatbestand-beweis-und-belege` — Erfindungsaufnahme Tatbestand Beweis und Belege
- `erfindungsmeldung-aufnahme-und-rueckfragen` — Erfindungsmeldung Aufnahme und Rueckfragen
- `freedom-to-operate-und-schutzbereich` — Freedom TO Operate und Schutzbereich
- `gebrauchsmuster-patent-patentrechts` — Gebrauchsmuster Patent Patentrechts
- `internationaler-patentrechts-und-laendercheck` — Internationaler Patentrechts und Laendercheck
- `israel-patentrecht-ilpo-opposition-revocation` — Israel Patentrecht Ilpo Opposition Revocation
- `japan-jpo-kanada-cipo-loeschung-widerruf` — Japan JPO Kanada Cipo Loeschung Widerruf
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ R. 161/162 6 Monate Einreichungsfrist EP-Anmeldung.
- Fachpfad wählen: zentrale Anker im Patentrecht sind PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87–89, PCT Art. 3, 8, UPCA. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPO, BPatG, BGH X. Senat, UPC.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch, Nichtigkeit, Register- und Fristenfragen; schlägt passende Fachmodule aus diesem Plugin und bei Bedarf das Schwesterplugin patentrecherche vor._

# Patentrecht — Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Patentrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startprinzip

Beginne nicht mit einer Vorlesung. Lies die Unterlagen, sichere Fristen, ordne die Aktenart ein und wähle den passenden Arbeitsweg. Wenn Material fehlt, stelle genau die eine Rückfrage, ohne die der nächste Schritt falsch wäre.

## Stummer Upload

Wenn der Nutzer nur Dateien hochlädt:

1. **Frist zuerst:** Zustellung, Einspruch, Prüfungsbescheid, Abmahnfrist, Prioritätsjahr, Offenbarung, Messe, Launch, Lizenzdeadline.
2. **Material erkennen:** Erfindungsmeldung, Anspruchsentwurf, Beschreibung, Zeichnungen, Patentvolltext, Prüfungsbescheid, Registerauszug, Abmahnung, Claim Chart, Lizenzvertrag, Prior-Art-Liste, Term Sheet.
3. **Rechtsfrage bestimmen:** Anmeldung, Patentfähigkeit, Recherche, FTO, Verletzung, Verteidigung, Lizenz, Bestand, Register.
4. **Fachmodul routen:** zuerst einen Skill aus `patentrecht`; bei Datenbankrecherche zusätzlich `patentrecherche`.
5. **Erster Output:** Kurzbild, Risiken, fehlende Unterlagen, nächster Arbeitsschritt.

## 60-Sekunden-Intake

| Punkt | Frage |
| --- | --- |
| Ziel | Anmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch/Nichtigkeit, Portfolio? |
| Technik | Produkt, Verfahren, Vorrichtung, Software, Chemie, Biotech, Mechanik, Elektronik? |
| Material | Skizzen, Prototyp, Beschreibung, Anspruchsentwurf, Registerauszug, E-Mail, Produktdaten, Vertrag? |
| Frist | Priorität, Messe, Veröffentlichung, Abmahnung, Prüfungsbescheid, Einspruch, Closing? |
| Territory | DE, EP, Einheitspatent/UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei, Israel, China, nur DACH, weltweit? |
| Rolle | Patentanwalt, Rechtsanwalt, Unternehmen, Gründerteam, Investor, Verletzungsbeklagter? |
| Output | Memo, Claim Draft, Rückfragen, Claim Chart, Rechercheauftrag, Vertrag, Mandantenbrief? |

## Routing

| Lage | Primärskill | Ergänzung |
| --- | --- | --- |
| Rohe Erfindungsidee | `erfindungsmeldung-aufnahme-und-rueckfragen` | `patentanmeldung-anspruchsentwurf` |
| Anspruchsentwurf prüfen | `patentanmeldung-anspruchsentwurf` | `beschreibung-und-zeichnungen-pruefen` |
| Recherchebedarf | `stand-der-technik-recherche-workflow` | `patentrecherche/agentische-datenbank-recherche` |
| Neuheit/Erfindungshöhe | `neuheit-und-erfinderische-taetigkeit` | `patentrecht-redteam-qualitygate` |
| Launch/FTO | `freedom-to-operate-und-schutzbereich` | `rechtsstand-register-und-fristen` |
| Abmahnung | `abmahnung-patentverletzung-verteidigung` | `patentverletzung-claim-chart` |
| behauptete Vorbenutzung | `vorbenutzungsrecht-paragraph-12-patg` | Beweis- und Chronologiematrix |
| Lizenzvertrag | `patentlizenzvertrag-review` | `patentlizenzvertrag-de-en-drafting` |
| Erfinder-/ArbEG-Thema | `erfinderbenennung-und-arbeitnehmererfindung` | Vergütungs- und Rechtekette |
| Einspruch/Nichtigkeit | `einspruch-epa-und-nichtigkeit-bpatg` | `neuheit-und-erfinderische-taetigkeit` |
| UPC/Einheitspatent | `upc-verletzung-und-rechtsbestand` | `upc-widerruf-und-widerklage-revocation` |
| internationale Länderstrategie | `internationaler-patentrechts-und-laendercheck` | `pct-laenderstrategie-und-nationalphasen` |
| USA/UK/Kanada/Japan/Schweiz/Türkei/Israel | jeweiliger Länderskill | Local-Counsel-Fragenkatalog |
| Patentprozess/Eilverfahren | `patentprozess-einstweilige-verfuegung-de-upc` | `patentprozess-schutzschrift-und-caveat` |
| globale Revocation/Nichtigkeit | `loeschung-widerruf-nichtigkeit-global-route` | `patentprozess-kostensicherheit-und-budget` |

## Antwortformat

**Kurzbild**
- Arbeitsziel: [...]
- Frist/Risiko: [...]
- Sicherer Sachverhalt: [...]
- Offene technische Punkte: [...]

**Nächster Arbeitsweg**
1. [...]
2. [...]
3. [...]

**Passende Skills**
| Skill | Warum jetzt? | Ergebnis |
| --- | --- | --- |
| `...` | [...] | [...] |

---

## Skill: `dokumente-intake`

_Dokumentenintake für Patentrecht (Verfahren, Verletzung): sortiert Patentschrift, Einspruchsschrift, Verletzungsanalyse, prüft Datum, Absender, Frist und Beweiswert (Stand-der-Technik-Dokumente, FTO-Analyse); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO._

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Patentrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Patentrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abmahnung-patentverletzung-verteidigung` — Abmahnung Patentverletzung Verteidigung
- `anspruchsentwurf-dokumentenmatrix-und-lueckenliste` — Anspruchsentwurf Dokumentenmatrix und Lueckenliste
- `beschreibung-zeichnungen-einspruch-epa-epo` — Beschreibung Zeichnungen Einspruch EPA EPO
- `einspruch-epa-und-nichtigkeit-bpatg` — Einspruch EPA und Nichtigkeit Bpatg
- `epo-epue-einspruch-beschwerde-beschraenkung` — EPO Epue Einspruch Beschwerde Beschraenkung
- `erfinderbenennung-arbeitnehmererfindung` — Erfinderbenennung Arbeitnehmererfindung
- `erfindungsaufnahme-tatbestand-beweis-und-belege` — Erfindungsaufnahme Tatbestand Beweis und Belege
- `erfindungsmeldung-aufnahme-und-rueckfragen` — Erfindungsmeldung Aufnahme und Rueckfragen
- `freedom-to-operate-und-schutzbereich` — Freedom TO Operate und Schutzbereich
- `gebrauchsmuster-patent-patentrechts` — Gebrauchsmuster Patent Patentrechts
- `internationaler-patentrechts-und-laendercheck` — Internationaler Patentrechts und Laendercheck
- `israel-patentrecht-ilpo-opposition-revocation` — Israel Patentrecht Ilpo Opposition Revocation
- `japan-jpo-kanada-cipo-loeschung-widerruf` — Japan JPO Kanada Cipo Loeschung Widerruf
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Patentrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87–89, PCT Art. 3, 8, UPCA — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Patentanmelder, Erfinder, Patentanwalt, DPMA, EPO, BPatG, BGH X. Senat, UPC prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 12 PatG
- § 3 PatG
- § 4 PatG
- § 14 PatG
- § 139 PatG
- § 34 PatG
- § 6 ArbEG
- § 9 ArbEG
- § 37 PatG
- § 8 PatG
- § 10 PatG
- § 44 PatG

### Leitentscheidungen

- BGH X ZR 168/00

---

## Skill: `rechtsabteilung-freedom-to-operate-vor-product-launch`

_Rechtsabteilungs-Fachmodul für Freedom-to-Operate vor Product Launch: FTO wird mit Claim Chart, Länderpriorität und Design-Around-Entscheidung ausgegeben. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Patentrecht._

# Rechtsabteilung: Freedom-to-Operate vor Product Launch

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Freedom-to-Operate vor Product Launch

- **Konkretes Problem:** FTO wird mit Claim Chart, Länderpriorität und Design-Around-Entscheidung ausgegeben.
- **Norm-/Quellenanker:** PatG, EPÜ, UPCA/UPC-Verfahrensordnung, ArbNErfG, ZPO/Eilrechtsschutz, Lizenzvertragsrecht und FRAND/SEP-Linien.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

PatG, EPÜ, UPC, Design/Know-how-Schnittstellen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

FTO wird mit Claim Chart, Länderpriorität und Design-Around-Entscheidung ausgegeben.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-upc-eilverfahren-und-deutsche-parallelstrategie`

_Rechtsabteilungs-Fachmodul für UPC-Eilverfahren und deutsche Parallelstrategie: PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Patentrecht._

# Rechtsabteilung: UPC-Eilverfahren und deutsche Parallelstrategie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: UPC-Eilverfahren und deutsche Parallelstrategie

- **Konkretes Problem:** PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen.
- **Norm-/Quellenanker:** PatG, EPÜ, UPCA/UPC-Verfahrensordnung, ArbNErfG, ZPO/Eilrechtsschutz, Lizenzvertragsrecht und FRAND/SEP-Linien.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

EPÜ, EPGÜ, UPC Rules; nationale PatG-Verfahren

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-employee-invention-frand`

_Rechtsabteilungs-Fachmodul für Employee Invention im Konzernprojekt: Meldung, Inanspruchnahme, Vergütung und ausländische R&D-Beiträge werden aufgesetzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Patentrecht._

# Rechtsabteilung: Employee Invention im Konzernprojekt

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Employee Invention im Konzernprojekt

- **Konkretes Problem:** Meldung, Inanspruchnahme, Vergütung und ausländische R&D-Beiträge werden aufgesetzt.
- **Norm-/Quellenanker:** PatG, EPÜ, UPCA/UPC-Verfahrensordnung, ArbNErfG, ZPO/Eilrechtsschutz, Lizenzvertragsrecht und FRAND/SEP-Linien.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

ArbEG; PatG; internationale Miterfinder

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Meldung, Inanspruchnahme, Vergütung und ausländische R&D-Beiträge werden aufgesetzt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-proportionalitaet-schweiz`

_Rechtsabteilungs-Fachmodul für Proportionalität der Unterlassung § 139 PatG: Injunction-Risiken werden für komplexe Produkte und Supply Chain bewertet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Patentrecht._

# Rechtsabteilung: Proportionalität der Unterlassung § 139 PatG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: Proportionalität der Unterlassung § 139 PatG

- **Konkretes Problem:** Injunction-Risiken werden für komplexe Produkte und Supply Chain bewertet.
- **Norm-/Quellenanker:** PatG, EPÜ, UPCA/UPC-Verfahrensordnung, ArbNErfG, ZPO/Eilrechtsschutz, Lizenzvertragsrecht und FRAND/SEP-Linien.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

PatG § 139; Verhältnismäßigkeitsrechtsprechung live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Injunction-Risiken werden für komplexe Produkte und Supply Chain bewertet.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `rechtsabteilung-frand-verteidigung-bei-sep-abmahnung`

_Rechtsabteilungs-Fachmodul für FRAND-Verteidigung bei SEP-Abmahnung: Lizenzbereitschaft, Vergleichbarkeit und Hold-out/Hold-up werden dokumentiert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Patentrecht._

# Rechtsabteilung: FRAND-Verteidigung bei SEP-Abmahnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialkern: Rechtsabteilung: FRAND-Verteidigung bei SEP-Abmahnung

- **Konkretes Problem:** Lizenzbereitschaft, Vergleichbarkeit und Hold-out/Hold-up werden dokumentiert.
- **Norm-/Quellenanker:** PatG, EPÜ, UPCA/UPC-Verfahrensordnung, ArbNErfG, ZPO/Eilrechtsschutz, Lizenzvertragsrecht und FRAND/SEP-Linien.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

Art. 102 AEUV; EuGH Huawei/ZTE; BGH Sisvel-Haier-Linie

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Lizenzbereitschaft, Vergleichbarkeit und Hold-out/Hold-up werden dokumentiert.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

---

## Skill: `kaltstart-interview`

_Kaltstart-Interview für Patentrechtsmandate. Erstellt ein kurzes Profil zu Mandant, Technik, Ziel, Territorien, Fristen, Dokumentenlage, Risiko und gewünschtem Output; speichert keine Geheimnisse, sondern strukturiert die nächsten Skills._

# Patentrecht — Kaltstart-Interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Patentrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Ziel

In maximal sieben Fragen klären, welche patentrechtliche Arbeit zu leisten ist. Danach nicht weiter interviewen, sondern einen Arbeitsplan und den ersten konkreten Output liefern.

## Fragen

1. **Was ist das Ziel?** Anmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch/Nichtigkeit, Portfolio, Prüfungsbescheid?
2. **Welche Technik?** Vorrichtung, Verfahren, Software/Computerimplementierung, Chemie, Biotech, Medizintechnik, Mechanik, Elektronik?
3. **Welche Unterlagen liegen vor?** Skizzen, Fotos, Prototyp, Anspruchsentwurf, Beschreibung, Patentnummer, Registerauszug, Vertrag, Abmahnung, Tabelle?
4. **Gibt es Fristen oder Veröffentlichungen?** Messe, Pitchdeck, Website, Verkauf, Prioritätsjahr, Abmahnfrist, Einspruchsfrist, Bescheidfrist?
5. **Welche Länder?** Deutschland, EP, Einheitspatent/UPC, PCT, USA, China, UK, andere?
6. **Was ist das wirtschaftliche Ziel?** Schutz aufbauen, Launch absichern, Verletzung abwehren, Lizenz monetarisieren, Investor beruhigen?
7. **Welcher Output wird gebraucht?** Mandantenmail, Gutachten, Anspruchsentwurf, Rechercheauftrag, Claim Chart, Vertragsredline, Fristenplan?

## Ergebnisformat

- **Mandatsprofil:** Beteiligte, Technik, Ziel, Territory.
- **Fristenprofil:** harte Fristen, weiche Business Deadlines, Offenbarungsrisiken.
- **Dokumentenprofil:** vorhandene und fehlende Aktenstücke.
- **Skillpfad:** 2 bis 5 passende Skills in Reihenfolge.
- **Erster Arbeitsschritt:** sofort verwertbarer Entwurf oder konkrete Rückfrage.

## Patentrechtlicher Pflichtkern

- **Schutzvoraussetzungen § 1 PatG:** Erfindung auf technischem Gebiet, neu (§ 3 PatG), erfinderische Tätigkeit (§ 4 PatG), gewerblich anwendbar (§ 5 PatG). Software als solche nicht patentfähig (§ 1 Abs. 3 Nr. 3 PatG), aber computer-implementierte Erfindungen unter Voraussetzungen.
- **Neuheitsschädliche Offenbarung:** Jede Verkaufs-/Messe-/Web-Offenbarung vor Anmeldung vernichtet Neuheit (§ 3 PatG). Bei Prio-Beanspruchung 12 Monate (Art. 4 PVÜ, § 41 PatG).
- **Schutzwirkung § 9 PatG:** unmittelbare und mittelbare Verletzung (§ 10 PatG); Schutzbereich nach § 14 PatG / Art. 69 EPÜ und Auslegungsprotokoll (Wortsinn und Äquivalenz).
- **Wichtige Fristen:** Einspruch beim DPMA 9 Monate ab Patenterteilung (§ 59 PatG); UPC-Opt-out bis Ende Übergangszeit; Jahresgebühren beim DPMA / EPA ab 3. Patentjahr.
- Falle: Anmeldetag-Strategie missachten — Veröffentlichung auf Pitchdeck oder Crowdfunding gilt als neuheitsschädlich, auch im Inland.

---

## Skill: `register-patentanmeldung-anspruchsentwurf`

_Prüft Patentregister und Fristen: DPMAregister, EPO Register, nationale Validierungen, Einheitspatent, Jahresgebühren, Priorität, Veröffentlichung, Erteilung, Einspruch, Beschränkung, Nichtigkeit und Verlängerungen im Patentrecht._

# Rechtsstand, Register und Fristen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Registerquellen

- DPMAregister für deutsche Schutzrechte.
- EPO Register für EP-Anmeldungen und EP-Patente.
- nationale Register für validierte EP-Teile.
- UPC/EPA/DPMA-Informationen, soweit Verfahrensstand betroffen ist.

## Fristenliste

| Frist | Startpunkt | Was prüfen? |
| --- | --- | --- |
| Prioritätsjahr | erste Anmeldung | Nachanmeldung/EP/PCT möglich? |
| Prüfungsbescheid | Zustellung/Amtsmitteilung | Antwortfrist, Verlängerung, Gebühren |
| Jahresgebühren | Anmeldetag/Jahr | gezahlt, Nachfrist, Erlöschen |
| Einspruch EP | Bekanntmachung der Erteilung | Fristende, Gebühr, Einspruchsgründe |
| Nichtigkeit | prozessuale Lage | Zulässigkeit, Parallelverfahren |
| Abmahnung | Zugang | Unterlassung/EV-Risiko |

## Regel

Nie allein aus einer Patentnummer schließen, dass ein Patent in Kraft ist. Immer Rechtsstand, Territory und geltende Anspruchsfassung prüfen.

## Konkrete Fristen

- **Prioritätsjahr Art. 87 EPÜ / § 41 PatG:** 12 Monate ab erster Hinterlegung; PCT-Frist ebenfalls 12 Monate.
- **PCT-Nationalisierung:** regelmäßig 30 oder 31 Monate ab Prioritätstag (Land-spezifisch; DE und EP: 31 Monate).
- **Recherchengebühr EPA:** mit Anmeldung; Prüfungsantrag binnen 6 Monaten nach Veröffentlichung des Recherchenberichts (Art. 94 (1) EPÜ).
- **Antwort auf Prüfungsbescheid EPA:** regelmäßig 4 Monate, verlängerbar.
- **DPMA-Prüfungsantrag (§ 44 PatG):** binnen 7 Jahren nach Anmeldetag.
- **Einspruch EPA:** **9 Monate** ab Veröffentlichung des Erteilungshinweises (Art. 99 EPÜ).
- **Beschränkungs-/Widerrufsantrag (Art. 105a EPÜ):** jederzeit.
- **Jahresgebühren EPA:** ab dem 3. Anmeldejahr; ab Erteilung an nationale Ämter.
- **Jahresgebühren DPMA (§ 17 PatG):** ab dem 3. Anmeldejahr; bei Nichtzahlung Erlöschen (§ 20 PatG); Wiedereinsetzungsfrist § 123 PatG.
- **Nichtigkeitsklage BPatG (§ 81 PatG):** keine starre Frist, aber nur gegen erteiltes Patent.
- **UPC Opt-out (Übergangszeit):** prüfen Sie aktuell unifiedpatentcourt.org -- Übergangszeitraum 7 Jahre ab Inkrafttreten UPCA (mit Verlängerungsoption auf 14 Jahre).

## Quellen live
- `register.dpma.de`, `register.epo.org`, `worldwide.espacenet.com`, `unifiedpatentcourt.org`, `wipo.int/portal/en/index.html` (PatentScope für PCT).

---

## Skill: `internationaler-patentrechts-und-laendercheck`

_Routet grenzüberschreitende Patentmandate nach DE, EP, UPC, PCT, USA, Kanada, Japan, Schweiz, UK, Türkei und Israel; trennt Recherche, Anmeldung, Rechtsstand, Verletzung, Rechtsbestand und lokale Counsel-Fragen im Patentrecht._

# Internationaler Patent- und Ländercheck

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Territorien und wirtschaftliche Märkte priorisieren.**
2. **Patentfamilie, Prioritäten, Anmelder- und Inhaberkette erfassen.**
3. **Pro Land trennen: Schutzfähigkeit, Rechtsstand, Verletzung, Rechtsbestand, Durchsetzung, Kosten.**
4. **Live-Register definieren: DPMA, EPO Register, Espacenet, WIPO PATENTSCOPE, USPTO, CIPO, J-PlatPat, Swissreg, UKIPO, TURKPATENT, ILPO.**
5. **Lokale Counsel-Fragen und Übersetzungsbedarf ausgeben.**

## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

---

## Skill: `patentlizenzvertrag-review`

_Prüft Patentlizenzverträge: Schutzrechte, Territory, Field of Use, Exklusivität, Unterlizenzen, Royalties, Milestones, Improvements, Inhaberschaft, Gewährleistung, Durchsetzung, Kündigung und Insolvenzrisiken im Patentrecht._

# Patentlizenzvertrag prüfen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Red-Flag-Check

| Thema | Frage |
| --- | --- |
| Schutzrechte | Welche Patente/Anmeldungen genau, welcher Rechtsstand, welche Länder? |
| Lizenzart | einfach, exklusiv, allein, konzernweit, nicht übertragbar? |
| Field of Use | Produktfeld technisch und wirtschaftlich klar? |
| Unterlizenz | erlaubt, zustimmungspflichtig, Konzern-/OEM-/Distributor-Abdeckung? |
| Gegenleistung | upfront, milestone, running royalty, Mindestumsatz, auditierbare Basis? |
| Verbesserungen | wem gehören Improvements, wer darf sie nutzen, wer muss anmelden? |
| Durchsetzung | wer klagt, wer trägt Kosten, wer kontrolliert Vergleich? |
| Gewährleistung | Bestand, Nichtverletzung, Inhaberschaft, technische Eignung sauber begrenzt? |
| Ende | Kündigung, Sell-off, Know-how-Rückgabe, Daten, Lagerbestand, Insolvenz? |

## Typische Fehler

- Territory und validierte Länder widersprechen sich.
- Exklusivität kollidiert mit eigener Nutzung oder bestehenden Lizenzen.
- "Patent" meint Anmeldung, aber Vertrag behandelt es wie erteiltes Schutzrecht.
- Erfinderpersönlichkeitsrechte werden wie übertragbare Vermögensrechte formuliert.
- Royalty Base passt nicht zu Produktbündeln, Ersatzteilen oder Dienstleistungen.

## Pflicht-Normen und Doktrinen
- **§ 15 PatG:** Übertragung und Lizenz; Lizenz ist sukzessionsfest, wenn dinglich bestellt.
- **VertikalGVO (EU) 2022/720 + Leitlinien:** Marktanteils-Sicherheitshafen 30 %; Kernbeschränkungen (RPM, Gebiete) bleiben verboten.
- **TT-GVO (EU) 316/2014:** Gruppenfreistellung für Technologietransfer; Marktanteilsschwellen (20 % bei Wettbewerbern, 30 % bei Nichtwettbewerbern); Kernbeschränkungen Art. 4.
- **FRAND / SEP:** EuGH Huawei/ZTE, C-170/13, Urt. v. 16.07.2015 -- pflichtgemäßes Verhandlungsritual.
- **Insolvenz des Lizenzgebers:** § 103 InsO Wahlrecht des Insolvenzverwalters; einfache Lizenz erlischt nicht zwingend, aber Risiko der Anfechtung. Schutz durch ausschließliche Lizenz mit Eintragung im DPMA-Register (§ 30 PatG); ggf. Treuhand.
- **AGB-Recht / B2B:** §§ 305 ff. BGB greifen im B2B-Geschäft begrenzt, aber Inhaltskontrolle nach § 307 BGB bleibt; bei Massenverträgen Klauselrisiko.
- **Compliance:** Exportkontrolle (Dual-Use-VO (EU) 2021/821), Sanktionsrecht, Embargos.

## Praxis-Tipp
- Konkrete Beispiele für Royalty-Bemessung im Vertrag (Stücklohn vs. Umsatz), Audit-Right mit 12-Monats-Vorlauf, Vertraulichkeit auf 5-10 Jahre.

---

## Skill: `abmahnung-patentverletzung-verteidigung`

_Verteidigt gegen Patentabmahnungen: Fristen, Unterlassungserklärung, Registerstand, Anspruchsfassung, Nichtverletzung, Rechtsbestand, Vorbenutzungsrecht, Schutzschrift, Vergleich und Mandantenkommunikation im Patentrecht._

# Patentabmahnung verteidigen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofortscan

1. Frist und Zustellung.
2. Absender, Vertreter, Schutzrecht, Anspruchsfassung, Territory.
3. Geforderte Erklärung: Unterlassung, Auskunft, Rechnungslegung, Rückruf, Vernichtung, Kostenerstattung.
4. Produktbezug und konkrete Verletzungsbehauptung.
5. Eilrisiko: einstweilige Verfügung, Messe, Launch, Lieferstopp.

## Verteidigungslinien

- Schutzrecht nicht in Kraft oder falsche Anspruchsfassung.
- Produkt verwirklicht ein Merkmal nicht.
- Äquivalenz greift nicht.
- Rechtsbestand zweifelhaft.
- Vorbenutzungsrecht oder Lizenz.
- Erschöpfung oder Lieferketteneinwand.
- Unterlassungserklärung zu weit, Vertragsstrafe zu riskant, Konzern-/Lieferkettenumfang unklar.
- Vergleich, Standstill, Design-around oder negative Feststellung.

## Regel

Nie empfehlen, eine vorformulierte Unterlassungserklärung ungeprüft zu unterschreiben. Immer Umfang, Vertragsstrafe, Anerkenntniswirkung, Auskunft und Rückruf isoliert prüfen.

## Anker-Normen und Doktrinen
- **§ 9 PatG:** Allein- und Mitbenutzungsrecht; Verletzungstatbestand.
- **§ 14 PatG / Art. 69 EPÜ + Protokoll:** Schutzbereich richtet sich nach den Patentansprüchen; Beschreibung und Zeichnungen sind heranzuziehen.
- **§ 139 PatG:** Unterlassungs- und Schadensersatzanspruch (Schadensersatz dreistufig: konkret, Lizenzanalogie, Gewinnabschöpfung).
- **§ 140a PatG:** Vernichtung; **§ 140b PatG:** Auskunftsanspruch.
- **§ 12 PatG:** Vorbenutzungsrecht -- inländische ernsthafte Benutzung vor Prioritätstag schützt vor Verletzung.
- **Äquivalenzdoktrin** (BGH, Schneidmesser-Linie, vgl. ständige Rspr.): drei Schritte (gleiche Wirkung, Auffindbarkeit, Gleichwertigkeit im Schutzbereich).
- **Erschöpfung:** rechtmäßig in den EWR in Verkehr gebrachte Erzeugnisse.
- **FRAND-Pflichten bei SEP:** EuGH Huawei/ZTE, C-170/13, Urt. v. 16.07.2015.

## Schutzschrift
- Hinterlegung im Zentralen Schutzschriftenregister `schutzschriftenregister.de`; spätestens vor Antragstellung der eV; sechs Monate Gültigkeit.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 12 PatG
- § 3 PatG
- § 4 PatG
- § 14 PatG
- § 139 PatG
- § 34 PatG
- § 6 ArbEG
- § 9 ArbEG
- § 37 PatG
- § 8 PatG
- § 10 PatG
- § 44 PatG

### Leitentscheidungen

- BGH X ZR 168/00

---

## Skill: `einspruch-epa-und-nichtigkeit-bpatg`

_Bereitet EPA-Einspruch und deutsche Nichtigkeitsklage vor: Fristen, Zuständigkeit, Angriffsmittel, Stand der Technik, unzulässige Erweiterung, Ausführbarkeit, Priorität, Hilfsanträge und Prozessstrategie im Patentrecht._

# Einspruch und Nichtigkeit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Weichenstellung

- **EPA-Einspruch:** nach Erteilung innerhalb der EPÜ-Frist; zentraler Angriff gegen europäisches Patent.
- **Nichtigkeitsklage:** deutscher Angriff gegen nationalen Teil, wenn zulässig und strategisch sinnvoll.
- **Parallelität:** Verletzungsverfahren, UPC, BPatG, EPA und Vergleichsverhandlungen koordinieren.

## Angriffsmittel

1. fehlende Neuheit.
2. fehlende erfinderische Tätigkeit.
3. nicht patentfähiger Gegenstand.
4. mangelnde Ausführbarkeit.
5. unzulässige Erweiterung.
6. unzulässige Erweiterung des Schutzbereichs nach Erteilung.
7. Prioritätsproblem.

## Beweispaket

| Angriff | Dokument/Beweis | Relevanz | Beweisqualität | Lücke |
| --- | --- | --- | --- | --- |

---

## Skill: `erfinderbenennung-arbeitnehmererfindung`

_Prüft Erfinderbenennung, Rechtekette und Arbeitnehmererfindungs-Schnittstellen: wer ist Erfinder, wer ist Anmelder, Diensterfindung, freie Erfindung, Inanspruchnahme, Vergütung und Dokumentationsrisiken im Patentrecht._

# Erfinderbenennung und Arbeitnehmererfindung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Erfinderstatus

Erfinder ist, wer einen schöpferischen Beitrag zur technischen Lehre geleistet hat. Nicht ausreichend sind bloße Aufgabenstellung, Finanzierung, Management, Routineversuche oder mechanische Umsetzung ohne eigenen Beitrag.

## Prüffragen

1. Wer hatte welche konkrete technische Idee?
2. Welche Beiträge betreffen den erfinderischen Kern?
3. Arbeitnehmer, Geschäftsführer, Freelancer, Universität, Kunde, Lieferant?
4. Gibt es Arbeitsvertrag, Entwicklungsvertrag, NDA, IP Assignment, Hochschul-/Forschungsbedingungen?
5. Wurde eine Diensterfindung gemeldet und in Anspruch genommen?
6. Sind Vergütungs- und Nachweisdokumente vorhanden?
7. Muss die Anmeldung korrigiert oder eine Rechtekette geschlossen werden?

## Red Flags

- Anmelder ist Konzernmutter, erfunden wurde aber bei Tochter/Freelancer.
- Erfinder sollen aus politischen Gründen aufgenommen oder gestrichen werden.
- "Alle Rechte übertragen" steht im Vertrag, aber Erfinderbenennung/ArbEG-Logik ist ungeklärt.
- Lizenzvertrag setzt Inhaberschaft voraus, Register und Aktenlage tragen das nicht.

## ArbEG — Pflichtnormen

- **§ 5 ArbEG Meldepflicht:** Arbeitnehmer muss Diensterfindung unverzüglich schriftlich melden; Arbeitgeber bestätigt schriftlich. Frist für Bestätigung: unverzüglich.
- **§ 6 ArbEG Inanspruchnahme:** Arbeitgeber kann binnen 4 Monaten nach ordnungsgemäßer Meldung ablehnen; sonst gilt sie als unbeschränkt in Anspruch genommen (§ 6 Abs. 2 ArbEG seit 01.10.2009).
- **§ 9 ArbEG Vergütung:** angemessene Vergütung nach Lizenzanalogie; Vergütungsrichtlinien (RL Nr. 1 bis 39 vom 20.07.1959 / Anpassungen). Üblich: Erfindungswert x Anteilsfaktor (a, b, c) x Persönlicher Anteil. Vergütung verfällt nicht mit Beendigung des Arbeitsverhältnisses.
- **§ 16 ArbEG Schutzrechtsanmeldung:** Arbeitgeber muss Patent anmelden, sonst Rückübertragungsanspruch (§ 16 ArbEG).
- **§ 37 PatG Erfinderbenennung:** Erfinder muss in Anmeldung benannt werden; Anmeldung ohne richtige Erfinderbenennung ist anfechtbar (§ 8 PatG Vindikation).
- **Spezialfälle:** Hochschulerfindungen § 42 ArbEG (Hochschullehrer); Universitäten haben 30 % Vergütungsanteil; Veröffentlichungsfreiheit zu wahren.
- **Vergütung Routinearbeit:** § 9 ArbEG-Logik nicht auf "freie" Erfindungen anwendbar — Trennung sauber ziehen.
- Falle: Bei Konzernlizenzen IP-Inhaberschaft live im DPMA-Register prüfen; "wirtschaftliche" Zuordnung reicht nicht; Diensterfinderbenennung darf nicht zur Familienangelegenheit werden — § 8 PatG Vindikationsanspruch droht.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

