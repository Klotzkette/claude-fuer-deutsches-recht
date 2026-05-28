---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im bAV Strategie Konzern-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Betriebliche Altersversorgung Strategie Konzern — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **bAV Strategie Konzern**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Strategische Beratung zur betrieblichen Altersversorgung in Konzernen: Pensionsmodelle alle fuenf Durchführungswege CTA Pension Buyouts Drei-Stufen-Theorie Versorgungssystem-Harmonisierung internationale Benefits Restrukturierung DB-zu-DC im Duesseldorfer Boutique-Stil.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `buyout-im-ma-deal-asset-vs-share` | Betriebliche Altersversorgung im M-und-A-Deal strukturieren: Haftungsuebernahme bei Asset- vs. Share-Deal. Normen: §§ 4 28 BetrAVG, UmwG. Prüfraster: Haftungsuebergang, Versorgungsverpflichtungen, PSV-Haftung,… |
| `country-by-country-benefits-matrix-konzern` | Laenderuebergreifende Benefits-Matrix für internationalen Konzern erstellen: Versorgungsniveaus im Vergleich. Normen: IORP-II, lokale Pensionsgesetze. Prüfraster: Leistungsebenen, gesetzliche Mindeststandards,… |
| `cta-contractual-trust-arrangement-strukturierung` | CTA-Struktur für Auslagerung von Pensionsverpflichtungen aufsetzen: Treuhandmodell, IFRS-Saldierung. Normen: § 6a EStG, IFRS, BetrAVG. Prüfraster: Treuhandvertragsstruktur, Insolvenzsicherung, Bilanzauswirkung. Output:… |
| `drei-stufen-theorie-eingriffsanalyse` | Drei-Stufen-Theorie bei Eingriffen in Versorgungsanwartschaften anwenden: erdiente und noch erdienbare Anwartschaften. Normen: §§ 2 7 BetrAVG, BVerfG-Rechtsprechung. Prüfraster: Stufen-Einordnung,… |
| `expatriate-pensionsplanung-und-totalization` | Pensionsplanung für Expatriates: Totalisierungsabkommen, Doppelversicherungsvermeidung, Pensionsluecken. Normen: EG-VO 883/2004, bilaterale SV-Abkommen. Prüfraster: Entsendelaender, Sozialversicherungsrecht,… |
| `governance-und-anpassungsmechanismen` | Governance-Strukturen und Anpassungsmechanismen für Versorgungsordnung im Konzern entwerfen. Normen: §§ 1 ff. BetrAVG, BetrVG. Prüfraster: Anpassungsbeschlussprozesse, Mitbestimmungsrechte, Informationspflichten.… |
| `harmonisierung-und-migration-rechtssicher` | bAV-Systeme nach Unternehmensrestrukturierung rechtssicher harmonisieren und migrieren. Normen: §§ 4 17 BetrAVG, UmwG. Prüfraster: Bestandsschutz, Unverfallbarkeit, Migrationsschritte. Output: Harmonisierungsplan bAV.… |
| `historisch-gewachsene-altsysteme-due-diligence` | Due Diligence historisch gewachsener bAV-Altsysteme im Konzern: Bestandsanalyse, Haftungsrisiken. Normen: §§ 2 6a EStG, BetrAVG. Prüfraster: Durchführungswege, ungedeckte Verpflichtungen, Altregelungen. Output:… |
| `internationale-buyout-datenflows-und-datenschutz` | Datenfluesse bei internationalem bAV-Buyout datenschutzrechtlich absichern: DSGVO, Drittlandtransfers. Normen: DSGVO Art. 44 ff., BDSG. Prüfraster: Datenkategorie, Transfermechanismen, Einwilligung vs. Vertrag. Output:… |
| `internationale-harmonisierung-konzern-bav` | Internationale bAV-Systeme im Konzern harmonisieren: Governance, Finanzierungsniveaus, lokale Compliance. Normen: IORP-II, lokale Pensionsgesetze, BetrAVG. Prüfraster: Harmonisierungsziele, rechtliche Grenzen,… |
| `japan-bav-und-corporate-pension-iorp` | Japanisches betriebliches Altersversorgungssystem und IORP-Vergleich für europaeische Konzerne. Normen: IORP-II, japanisches Pensionsrecht DB-Pensions-Act. Prüfraster: Leistungsunterschiede, Finanzierungsanforderungen,… |
| `kollektivrechtliche-loesungen-und-sozialplan` | Kollektivrechtliche Lösungen für bAV-Einschnitte: Betriebsvereinbarung, Sozialplan, Einigungsstelle. Normen: §§ 77 112 BetrVG, BetrAVG. Prüfraster: Mitbestimmungsrechte, Sozialplanvolumen, Ausgleichszahlungen. Output:… |
| `mitbestimmung-betriebsrat-einigungsstelle-bav` | Betriebsratsbeteiligung bei bAV-Einführung und -Aenderung sicherstellen: Mitbestimmungsrechte. Normen: §§ 87 Abs. 1 Nr. 8 sowie 77 112 BetrVG. Prüfraster: Mitbestimmungstatbestaende, Informationspflichten,… |
| `pension-buyout-strukturierung-und-de-risking` | Pensionsbuyout und De-Risking strukturieren: Risikoauslagerung an Versicherungsunternehmen oder CTA. Normen: §§ 4 BetrAVG, VAG, IFRS. Prüfraster: Buyout-Voraussetzungen, Versicherungslösungen, Bilanzbereinigung.… |
| `pensionsmodelle-fuenf-durchfuehrungswege` | Fuenf Durchführungswege der betrieblichen Altersversorgung vergleichen und waehlen. Normen: §§ 1 1b BetrAVG. Prüfraster: Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds - Vor- und… |
| `psv-pensionssicherungsverein-und-haftungsketten` | PSV-Pflichtversicherung und Haftungsketten bei Insolvenz des Arbeitgebers analysieren. Normen: §§ 7 ff. BetrAVG, PSVaG-Satzung. Prüfraster: Insolvenzsicherungspflicht, gesicherte Leistungen, Haftungsquoten. Output:… |
| `versorgungsordnung-und-betriebsvereinbarung-drafting` | Versorgungsordnung und Betriebsvereinbarung zur bAV-Einführung entwerfen. Normen: §§ 1 17 BetrAVG, §§ 77 87 BetrVG. Prüfraster: Leistungszusagen, Unverfallbarkeit, Mitbestimmung, Finanzierungsklauseln. Output:… |

## Worum geht es?

Das Plugin deckt die strategische und rechtliche Beratung zur betrieblichen Altersversorgung (bAV) in Konzernen ab. Es reicht von der Wahl und dem Vergleich der fuenf Durchfuehrungswege ueber die Strukturierung von CTAs und Pension Buyouts bis hin zur internationalen Harmonisierung von Versorgungssystemen in multinationalen Konzernen.

Zielgruppe sind Anwaelte, Personalleiter und Steuerberater, die mit der rechtssicheren Gestaltung, Anpassung oder Aufloesung von Betriebsrenten beauftragt sind. Besondere Relevanz hat die Drei-Stufen-Theorie des BAG bei Eingriffen in bereits erdiente Anwartschaften sowie die Mitbestimmungsrechte des Betriebsrats. Im M-und-A-Kontext sind Haftungsuebergang und Due Diligence von Altsystemen zentrale Themen.

## Wann brauchen Sie diese Skill?

- Ein Konzern moechte seine bAV-Landschaft nach einer Fusion oder Akquisition harmonisieren und bestehende Altsysteme analysieren.
- Sie beraten zu einem Pension Buyout und muessen Voraussetzungen, Versicherungsloesungen und Bilanzauswirkungen strukturieren.
- Betriebsrat und Arbeitgeber verhandeln eine neue Versorgungsordnung und benoetigen einen rechtssicheren Entwurf.
- Expatriates sind in internationalen Konzernen taetig und Pensionsluecken sowie Totalisierungsabkommen muessen analysiert werden.
- Ein US- oder Japan-Konzern moechte seine europaeischen bAV-Strukturen mit lokalen Anforderungen und IORP-II in Einklang bringen.

## Fachbegriffe (kurz erklaert)

- **Durchfuehrungsweg** — Eine der fuenf gesetzlich anerkannten Formen der bAV: Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds (§§ 1 1b BetrAVG).
- **CTA** — Contractual Trust Arrangement; Treuhandkonstruktion zur Auslagerung von Pensionsverpflichtungen mit IFRS-Saldierungswirkung.
- **Drei-Stufen-Theorie** — BAG-Rechtsprechung zum Schutz erdienter Anwartschaften: Je groesser der Eingriff, desto hoeher die Anforderungen an die Rechtfertigung.
- **PSV** — Pensionssicherungsverein; gesetzlicher Insolvenzschutzmechanismus fuer bestimmte bAV-Durchfuehrungswege.
- **Pension Buyout** — Uebertragung von Pensionsverpflichtungen auf einen Versicherer oder ein CTA zur Bilanzbereinigung (De-Risking).
- **IORP-II** — EU-Richtlinie ueber Taetigkeiten und Beaufsichtigung von Einrichtungen der betrieblichen Altersversorgung.
- **Unverfallbarkeit** — Gesetzlicher Schutz erdienter Anwartschaften: Nach Ablauf der Unverfallbarkeitsfrist bleiben Ansprueche auch bei Arbeitgeberwechsel erhalten (§ 1b BetrAVG).
- **§ 6a EStG** — Steuerliche Regelung zur Passivierung von Pensionsrueckstellungen bei Direktzusagen.

## Rechtsgrundlagen

- §§ 1 1b BetrAVG — Grundsatz und Unverfallbarkeit
- §§ 2 7 BetrAVG — Erdiente Anwartschaften und PSV-Schutz
- §§ 4 17 28 BetrAVG — Uebertragung und M-und-A-Haftung
- §§ 77 87 Abs. 1 Nr. 8 112 BetrVG — Mitbestimmung bei bAV
- § 6a EStG — Pensionsrueckstellungen
- IFRS IAS 19 — Bilanzierung von Versorgungsverpflichtungen
- IORP-II — EU-Pensionsfondsrichtlinie
- DSGVO Art. 44 ff. — Drittlandtransfer bei internationalen bAV-Daten
- EG-VO 883/2004 — Koordinierung der Sozialversicherungssysteme in der EU

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Konzernstruktur und bAV-Ist-Stand erfassen (Durchfuehrungswege, Laender, Beschaeftigtenzahl).
2. Handlungsanlass bestimmen (Neueinfuehrung, Harmonisierung nach M-und-A, Eingriff in Anwartschaften, Buyout).
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Mitbestimmungsrechtliche Anforderungen pruefen (Betriebsrat, Einigungsstelle).
5. Steuerliche und bilanzielle Auswirkungen abstimmen (§ 6a EStG, IFRS IAS 19).

## Skill-Tour (was gibt es hier?)

- `buyout-im-ma-deal-asset-vs-share` — bAV-Haftungsuebergang im M-und-A-Deal bei Asset-Deal vs. Share-Deal strukturieren.
- `country-by-country-benefits-matrix-konzern` — Laenderuebergreifende Benefits-Matrix fuer internationalen Konzern: Versorgungsniveaus im Vergleich.
- `cta-contractual-trust-arrangement-strukturierung` — CTA-Struktur fuer Auslagerung von Pensionsverpflichtungen aufsetzen: Treuhandmodell und IFRS-Saldierung.
- `drei-stufen-theorie-eingriffsanalyse` — Drei-Stufen-Theorie bei Eingriffen in Versorgungsanwartschaften anwenden und Eingriff rechtfertigen.
- `expatriate-pensionsplanung-und-totalization` — Pensionsplanung fuer Expatriates: Totalisierungsabkommen und Pensionslueckenanalyse.
- `governance-und-anpassungsmechanismen` — Governance-Strukturen und Anpassungsmechanismen fuer die Versorgungsordnung im Konzern entwerfen.
- `harmonisierung-und-migration-rechtssicher` — bAV-Systeme nach Unternehmensrestrukturierung rechtssicher harmonisieren und migrieren.
- `historisch-gewachsene-altsysteme-due-diligence` — Due Diligence historisch gewachsener bAV-Altsysteme: Bestandsanalyse und Haftungsrisiken.
- `internationale-buyout-datenflows-und-datenschutz` — Datenfluesse bei internationalem bAV-Buyout nach DSGVO und Drittlandtransfer absichern.
- `internationale-harmonisierung-konzern-bav` — Internationale bAV-Systeme im Konzern harmonisieren: Governance, Finanzierungsniveaus, lokale Compliance.
- `japan-bav-und-corporate-pension-iorp` — Japanisches Pensionssystem und IORP-Vergleich fuer europaeische Konzerne analysieren.
- `kollektivrechtliche-loesungen-und-sozialplan` — Kollektivrechtliche Loesungen fuer bAV-Einschnitte: Betriebsvereinbarung, Sozialplan, Einigungsstelle.
- `mitbestimmung-betriebsrat-einigungsstelle-bav` — Betriebsratsbeteiligung bei bAV-Einfuehrung und -Aenderung rechtssicher sicherstellen.
- `pension-buyout-strukturierung-und-de-risking` — Pensionsbuyout und De-Risking strukturieren: Risikoauslagerung und Bilanzbereinigung.
- `pensionsmodelle-fuenf-durchfuehrungswege` — Alle fuenf Durchfuehrungswege vergleichen und den passenden Weg empfehlen.
- `psv-pensionssicherungsverein-und-haftungsketten` — PSV-Pflichtversicherung und Haftungsketten bei Insolvenz des Arbeitgebers analysieren.
- `versorgungsordnung-und-betriebsvereinbarung-drafting` — Versorgungsordnung und Betriebsvereinbarung zur bAV-Einfuehrung rechtssicher entwerfen.

## Worauf besonders achten

- **Drei-Stufen-Theorie strikt anwenden**: Eingriffe in bereits erdiente Anwartschaften scheitern regelmaessig an der BAG-Rechtsprechung, wenn keine sachlichen Gruende vorliegen.
- **Mitbestimmung nicht vergessen**: Die Einfuehrung und wesentliche Aenderung von bAV-Systemen ist mitbestimmungspflichtig nach § 87 Abs. 1 Nr. 8 BetrVG.
- **IFRS und steuerliche Bilanzierung abstimmen**: IFRS IAS 19 und § 6a EStG folgen unterschiedlichen Bewertungslogiken; Discrepanzen koennen zu Ueberraschungen fuehren.
- **Drittlandrisiko bei internationalen Datenflows**: bAV-Daten von Expatriates oder auslaendischen Konzerngesellschaften fallen unter DSGVO Art. 44 ff.
- **PSV-Pflicht nicht uebersehen**: Nicht alle Durchfuehrungswege sind PSV-pflichtig; Fehler bei der Einordnung fuehren zu Haftungsluecken.

## Typische Fehler

- Betriebsvereinbarung ohne Mitbestimmungsverfahren aendern; fuehrt zu Unwirksamkeit und Einigungsstellenverfahren.
- CTA-Struktur aufbauen ohne IFRS-Saldierungsguachten; IFRS-Bilanzerleichterung tritt nicht ein.
- Beim M-und-A-Deal bAV-Haftung im Asset-Deal uebersehen; Erwerber tritt automatisch in bestehende Versorgungspflichten ein.
- Expatriate-Pensionsplanung ohne Pruefung der Totalisierungsabkommen; doppelte Sozialversicherungspflicht entstehen.
- Historische Altsysteme ohne Due Diligence fortfuehren; ungedeckte Verpflichtungen koennen Bilanzen signifikant belasten.

## Querverweise

- `insolvenzverwaltung` — Bei Insolvenz des Arbeitgebers greift PSV-Schutz; Schnittstelle zur Masseverbindlichkeit.
- `kanzlei-allgemein` — Allgemeines Kanzlei-Workflow-Plugin fuer Fristen und Schriftsaetze in bAV-Mandaten.
- `tabellenreview-3d` — Massenpruefung von bAV-Vertragsstapeln im 3D-Review.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
