# Wahlkampfrecht Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`wahlkampfrecht-praxis.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/wahlkampfrecht-praxis.md) (53 KB)
- Im Repo: [`testakten/megaprompts/wahlkampfrecht-praxis.md`](../testakten/megaprompts/wahlkampfrecht-praxis.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`wahlkampfrecht-praxis`) | [`wahlkampfrecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/wahlkampfrecht-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Wahlkampfakte Morgenstadt 2026 - Landesliste, Plakatierung und digitale Lage** (`wahlkampfrecht-landtagswahl-morgenstadt-2026`) | [Gesamt-PDF lesen](../testakten/wahlkampfrecht-landtagswahl-morgenstadt-2026/gesamt-pdf/wahlkampfrecht-landtagswahl-morgenstadt-2026_gesamt.pdf) | [`testakte-wahlkampfrecht-landtagswahl-morgenstadt-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wahlkampfrecht-landtagswahl-morgenstadt-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein großes Arbeitsplugin für demokratische Wahlkampfteams, Parteien, Kandidierende, Wahlkampfmanagerinnen, Kreisverbände, Landesgeschäftsstellen, Bundeswahlkampfstäbe, Kampagnenagenturen und anwaltliche Berater. Es verbindet Recht, Strategie und tägliche Durchführung: Plakatierung, Infostände, Veranstaltungen, Social Media, Daten, Spenden, Kandidatentraining, Krisenkommunikation, Desinformation, Wahltag und Nachbereitung.

Das Plugin soll Kampagnen handlungsfähiger machen, ohne sie zu verrohen. Es hilft bei klarer Message, schneller Lagearbeit und robustem Ground Game. Gleichzeitig zieht es rote Linien: keine Plakat-Sabotage, keine verdeckte Finanzierung, keine rechtswidrige Datennutzung, keine Desinformation, keine fingierten Accounts, keine Irreführung über Wahlverfahren und keine Nutzung staatlicher Ressourcen für Parteizwecke.

## Kaltstart

Starte mit `wahlkampf-allgemeiner-kaltstart` oder `wahlkampf-ebenen-und-wahlart-router`. Das Plugin fragt zuerst:

1. Welche Wahl: Bundestag, Europawahl, Landtag, Kommunalwahl, Bürgermeister-/Landratswahl, innerparteiliche Vorwahl oder Sonderfall?
2. Welche Rolle: Bundesstrategie, Landeswahlkampf, Kreisverband, Kandidatenteam, Agentur, Rechtsabteilung, Schatzmeisterei, Social-Media-Team oder Ehrenamtliche vor Ort?
3. Was ist der Druck: Plakatgenehmigung, Podium, Social-Media-Krise, Spende, Datenschutz, Desinformation, Schulveranstaltung, Wahltag, Behördenbrief oder Strategieplan?
4. Welche Rechtsordnung: Bund, Land, Kommune, Plattform, Datenschutz, Parteienfinanzierung, Strafrecht, Medienrecht, Versammlungsrecht?
5. Welcher Output: Schlachtplan, Freigabecheck, Behördenbrief, Briefing, Risikoampel, Presse-Q&A, Volunteer-Skript, Fristenkalender oder Incident-Log?

## Leitgedanken

- **Demokratisch kampfstark:** klare Strategie, aber keine Manipulation des Wahlverfahrens und keine organisierte Unwahrheit.
- **Recht und Taktik zusammen:** Ein Plakatstandort ist zugleich Sondernutzung, Verkehrssicherheit, Sichtbarkeit, Ehrenamtslogistik und Konfliktrisiko.
- **Resilienz vor Empörung:** Desinformation wird dokumentiert, priorisiert, entkräftet und bei Plattformen/Behörden sauber eskaliert.
- **Authentische Kandidierende:** Nicht alle Menschen sind Medienprofis. Das Plugin trainiert Verhalten unter Kamera, ohne Persönlichkeiten glattzubügeln.
- **Keine falsche Neutralität:** Amtsträger, öffentliche Einrichtungen, Schulen, Verwaltungen und Wahlorgane werden rechtlich sauber getrennt.

## Typische Workflows

| Lage | Einstiegsskills | Ergebnis |
| --- | --- | --- |
| Bundes- oder Landeswahlkampf planen | `wahlkampf-bundesstrategie-architektur`, `wahlkampf-landeswahlkampf-lagekarte`, `wahlkampf-schlachtenplan-ethik-und-taktik` | Strategiepapier, Phasenplan, Risiko-Board |
| Kreisverband muss Plakate hängen | `wahlkampf-plakatierung-genehmigung`, `wahlkampf-plakatstandorte-matrix`, `wahlkampf-fremdplakate-nicht-anruehren` | Standortliste, Teambriefing, Ordnungsamtsmail |
| Social-Media-Krise | `wahlkampf-rapid-response-room`, `wahlkampf-viraler-clip-notfall`, `wahlkampf-faktencheck-gegenrede` | Krisenlog, Q&A, Antwortleiter |
| Politische Online-Werbung | `wahlkampf-eu-2024-900-politische-werbung`, `wahlkampf-targeting-dsgvo`, `wahlkampf-ad-library-transparenz` | Transparenznotiz, Freigabevermerk, Targeting-Ampel |
| Podium mit problematischem Gegner | `wahlkampf-podium-teilnahmeentscheidung`, `wahlkampf-keine-buehne-aber-nicht-fehlen`, `wahlkampf-kandidatenbriefing-kamera` | Teilnahmevermerk, Sprechzettel, Schutzplan |
| Schulen, Jugend, öffentliche Einrichtungen | `wahlkampf-schulen-und-jugendformate`, `wahlkampf-staatliche-neutralitaet`, `wahlkampf-amtstraeger-ressourcen` | Einladungsschreiben, Neutralitätsprüfung, Rollenabgrenzung |
| Wahltag und Wahlraum | `wahlkampf-wahlraum-propagandaverbot`, `wahlkampf-wahlbeobachtung-und-wahltag`, `wahlkampf-briefwahlkommunikation` | Wahltagskarte, Beobachterbriefing, Eskalationspfad |

## Amtliche und frei prüfbare Startquellen

- [Grundgesetz](https://www.gesetze-im-internet.de/gg/) - insbesondere Art. 5, Art. 21 und Wahlrechtsgrundsätze.
- [Bundeswahlgesetz](https://www.gesetze-im-internet.de/bwahlg/) und [Bundeswahlordnung](https://www.gesetze-im-internet.de/bwo_1985/) für Bundestagswahlen.
- [Europawahlgesetz](https://www.gesetze-im-internet.de/euwg/) und [Europawahlordnung](https://www.gesetze-im-internet.de/euwo_1988/) für Europawahlen.
- [Parteiengesetz](https://www.gesetze-im-internet.de/partg/) für Parteienfinanzierung, Spenden, Rechenschaft und Parteiorganisation.
- [Strafgesetzbuch](https://www.gesetze-im-internet.de/stgb/) zu Wahlstraftaten, Nötigung, Beleidigung, Sachbeschädigung und Urkundenthemen.
- [Wahlprüfungsgesetz](https://www.gesetze-im-internet.de/wahlprg/) für Wahlprüfung nach Bundestagswahlen.
- [Bundeswahlleiterin: Wahlwerbung](https://www.bundeswahlleiterin.de/service/glossar/w/wahlwerbung.html), [unzulässige Wahlpropaganda](https://www.bundeswahlleiterin.de/service/glossar/w/wahlpropaganda-unzulaessige.html) und [Fakten gegen Desinformation](https://www.bundeswahlleiterin.de/bundestagswahlen/2025/fakten-desinformation.html).
- [Deutscher Bundestag: Parteienfinanzierung](https://www.bundestag.de/parlament/praesidium/parteienfinanzierung) und [Parteispenden über 35.000 EUR](https://www.bundestag.de/parteispenden).
- [EU-Kommission: Transparency and targeting of political advertising](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/democracy-eu-citizenship-anti-corruption/democracy-and-electoral-rights/transparency-and-targeting-political-advertising_en) zur Verordnung (EU) 2024/900, die seit 10. Oktober 2025 voll gilt.
- [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) und [BDSG](https://www.gesetze-im-internet.de/bdsg_2018/) für Datenverarbeitung im Wahlkampf.
- Lokale Plakatierungs-, Sondernutzungs- und Veranstaltungsregeln der jeweiligen Gemeinde; diese müssen immer aktuell am konkreten Ort geprüft werden.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Bei Landeswahlrecht, Plakatierungsfristen, Sondernutzung, Schulen und Kommunalrecht zwingend die konkrete Gemeinde und das Bundesland live prüfen.

## Datenschutz und Kampagnensicherheit

Keine echten Wählerdaten, Mitgliederdaten, Spenderlisten, Social-Media-Profile, Gesundheitsdaten, politische Meinungsdaten oder internen Kampagnengeheimnisse in ungeprüfte Systeme laden. Das Plugin ist ein Arbeits- und Demonstrationsrahmen; produktiver Einsatz braucht Datenschutz-, Berufsrechts-, Parteienfinanzierungs- und IT-Sicherheitsprüfung.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 118 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `72-stunden-sprint` | Wahlkampfrecht Praxis: die letzten 72 Stunden vor Wahl, Debatte oder Krise planen im Wahlkampfrecht. |
| `ad-library-transparenz` | Wahlkampfrecht Praxis: Anzeigenbibliothek- und Transparenznotizen erstellen im Wahlkampfrecht. |
| `agenturvertrag-compliance` | Wahlkampfrecht Praxis: Agentur-, Media- und Beratungsvertraege im Wahlkampf prüfen im Wahlkampfrecht. |
| `aktenplan-beweisarchiv-amtstraeger` | Wahlkampfrecht Praxis: Kampagnenakte so strukturieren, dass sie später prüfbar bleibt im Wahlkampfrecht. |
| `amtstraeger-ressourcen` | Wahlkampfrecht Praxis: Auftritte von Regierungsmitgliedern, Buergermeistern und Abgeordneten prüfen im Wahlkampfrecht. |
| `angriff-auf-wahlleitung-vermeiden` | Wahlkampfrecht Praxis: Kritik an Wahlorganisation ohne Vertrauenszerstoerung formulieren im Wahlkampfrecht. |
| `arbeitsrecht-kampagnenteam` | Wahlkampfrecht Praxis: Beschäftigung, Minijobs, Freelancer und Ehrenamt im Wahlkampf prüfen im Wahlkampfrecht. |
| `archivierung-screenshots` | Wahlkampfrecht Praxis: digitale Beweise für schnelle Praxis sichern im Wahlkampfrecht. |
| `asymmetrische-demobilisierung` | Wahlkampfrecht Praxis: Demobilisierungsstrategien analysieren im Wahlkampfrecht. |
| `barrierefreie-und-mehrsprachige-information` | Wahlkampfrecht Praxis: mehrsprachige und barrierefreie Kampagneninformationen rechtssicher planen im Wahlkampfrecht. |
| `barrierefreiheit-und-inklusion` | Wahlkampfrecht Praxis: barrierearme Wahlkampfkommunikation und Veranstaltungen planen im Wahlkampfrecht. |
| `bots-und-inauthentisches-verhalten` | Wahlkampfrecht Praxis: koordinierte inauthentische Kommunikation erkennen und vermeiden im Wahlkampfrecht. |
| `briefkasten-flyer` | Wahlkampfrecht Praxis: Flyer- und Briefkastenaktionen prüfen im Wahlkampfrecht. |
| `briefwahlkommunikation` | Wahlkampfrecht Praxis: Kommunikation über Briefwahl ohne Irrefuehrung prüfen im Wahlkampfrecht. |
| `buergerdialog-schwierige-fragen` | Wahlkampfrecht Praxis: Buergerdialoge mit unangenehmen, aber legitimen Fragen vorbereiten im Wahlkampfrecht. |
| `bundesstrategie-architektur` | Wahlkampfrecht Praxis: Bundeswahlkampf als rechtlich sauberes Operating Model bauen im Wahlkampfrecht. |
| `community-management` | Wahlkampfrecht Praxis: Community Manager für Kommentare, Beleidigungen und Fragen briefen im Wahlkampfrecht. |
| `compliance-schulung-vorstand` | Wahlkampfrecht Praxis: kurze Compliance-Schulung für Vorstand und Kampagnenteam erstellen im Wahlkampfrecht. |
| `cybersicherheit-kampagne` | Wahlkampfrecht Praxis: Kampagnen-IT gegen Accountuebernahmen und Leaks sichern im Wahlkampfrecht. |
| `datenschutz-folgenabschaetzung-politische-daten` | Wahlkampfrecht Praxis: prüfen, ob politische Datenverarbeitung eine DSFA braucht im Wahlkampfrecht. |
| `debattenvorbereitung` | Wahlkampfrecht Praxis: Kandidierende auf Debatte, Townhall oder TV-Runde vorbereiten im Wahlkampfrecht. |
| `deepfake-und-ki-kennzeichnung` | Wahlkampfrecht Praxis: KI-generierte Inhalte, Deepfakes und synthetische Stimmen prüfen im Wahlkampfrecht. |
| `desinformation-monitoring` | Wahlkampfrecht Praxis: Desinformation und Manipulationsnarrative monitoren im Wahlkampfrecht. |
| `ebenen-wahlart-ehrenamtliche` | Wahlkampfrecht Praxis: Bundestag, Europa, Landtag, Kommunalwahl, Buergermeisterwahl und Sonderlagen sauber unterscheiden im Wahlkampfrecht. |
| `ehrenamtliche-schulen` | Wahlkampfrecht Praxis: Ehrenamtliche schnell und verstaendlich kampagnentauglich machen im Wahlkampfrecht. |
| `eu-2024-900-politische-werbung` | Wahlkampfrecht Praxis: politische Werbung nach EU-Verordnung 2024/900 prüfen im Wahlkampfrecht. |
| `faktencheck-gegenrede` | Wahlkampfrecht Praxis: sachliche Gegenrede gegen falsche Wahlkampfnarrative erstellen im Wahlkampfrecht. |
| `flooding-gegenrede-statt-muell` | Wahlkampfrecht Praxis: auf Informationsflutung reagieren, ohne selbst Muell zu produzieren im Wahlkampfrecht. |
| `foreign-interference-foto-wahlraum` | Wahlkampfrecht Praxis: Anzeichen ausländischer Einflussnahme bewerten im Wahlkampfrecht. |
| `foto-im-wahlraum-und-stimmzettel` | Wahlkampfrecht Praxis: Selfies, Stimmzettelfotos und Wahlgeheimnisrisiken prüfen im Wahlkampfrecht. |
| `fraktion-partei-trennung` | Wahlkampfrecht Praxis: Fraktions-, Amts- und Parteimittel sauber trennen im Wahlkampfrecht. |
| `freiwillige-und-aufwandsersatz` | Wahlkampfrecht Praxis: Aufwandsersatz, Reisekosten und geldwerte Vorteile für Helfer prüfen im Wahlkampfrecht. |
| `fremdplakate-nicht-anruehren` | Wahlkampfrecht Praxis: Teams briefen, fremde Plakate weder abzuhaengen noch zu ueberkleben im Wahlkampfrecht. |
| `gegnerkritik-meinungsfreiheit` | Wahlkampfrecht Praxis: scharfe Kritik an Gegnern ohne Beleidigungs- oder Falschtatsachenrisiko prüfen im Wahlkampfrecht. |
| `gewerkschaften-verbaende-kirchen` | Wahlkampfrecht Praxis: Zusammenarbeit mit Verbaenden, Gewerkschaften, Kirchen und Initiativen prüfen im Wahlkampfrecht. |
| `giveaways-waehlerbestechung` | Wahlkampfrecht Praxis: Geschenke, Gewinnspiele, Essen, Getraenke und Rabatte im Wahlkampf prüfen im Wahlkampfrecht. |
| `grossspenden-sofortmeldung` | Wahlkampfrecht Praxis: Grossspenden über der aktuellen Sofortmeldeschwelle prüfen im Wahlkampfrecht. |
| `hausrecht-privatraeume` | Wahlkampfrecht Praxis: Wahlkampftermine in privaten Hallen, Vereinen und Betrieben prüfen im Wahlkampfrecht. |
| `haustuerwahlkampf-influencer` | Wahlkampfrecht Praxis: Haustuerwahlkampf rechtlich und praktisch sauber machen im Wahlkampfrecht. |
| `influencer-und-unterstuetzer` | Wahlkampfrecht Praxis: Influencer-, Unterstuetzer- und Testimonialkampagnen prüfen im Wahlkampfrecht. |
| `infostand-sondernutzung` | Wahlkampfrecht Praxis: Infostaende auf öffentlichen Flaechen planen im Wahlkampfrecht. |
| `interne-chatdisziplin` | Wahlkampfrecht Praxis: interne Chats so briefen, dass sie nicht zur Brandquelle werden im Wahlkampfrecht. |
| `kaltstart-routing` | Wahlkampfrecht Praxis: Kaltstart für jede Wahlkampflage mit Routing zu Recht, Strategie, Digital, Plakatierung, Finanzen oder Krise. |
| `kandidaten-altposts-screening` | Wahlkampfrecht Praxis: Altposts und digitale Spuren von Kandidierenden screenen im Wahlkampfrecht. |
| `kandidatenbriefing-kamera` | Wahlkampfrecht Praxis: Kandidierende für Kamera, Smartphone-Clips und spontane Fragen trainieren im Wahlkampfrecht. |
| `kandidatenteam-intake` | Wahlkampfrecht Praxis: Kandidatenteam aufnehmen und biografische, digitale und organisatorische Schwachstellen erkennen im Wahlkampfrecht. |
| `kandidierenden-fuersorge` | Wahlkampfrecht Praxis: Belastung, Angriffe und Burnout in Kandidatenteams ernst nehmen im Wahlkampfrecht. |
| `kassenpruefung-kreisverband` | Wahlkampfrecht Praxis: Kreisverbaenden bei sauberer Kasse waehrend intensiver Kampagnen helfen im Wahlkampfrecht. |
| `keine-buehne-aber-nicht-fehlen` | Wahlkampfrecht Praxis: Alternativen entwickeln, wenn ein Podium nicht besucht werden soll im Wahlkampfrecht. |
| `koalitionssignale-kommunalwahlkampf` | Wahlkampfrecht Praxis: Koalitionssignale im Wahlkampf strategisch und rechtlich sauber formulieren im Wahlkampfrecht. |
| `kommunalwahlkampf-groundgame` | Wahlkampfrecht Praxis: Kommunalwahlkampf in Infostaende, Haustuer, Plakate, lokale Termine und Wahlvorschlaege übersetzen im Wahlkampfrecht. |
| `kostenversprechen-und-finanzierbarkeit` | Wahlkampfrecht Praxis: Kosten- und Finanzierungsversprechen kommunikativ und rechtlich absichern im Wahlkampfrecht. |
| `krisenstatement-fehler-eigener-leute` | Wahlkampfrecht Praxis: auf Fehltritte eigener Kandidierender oder Helfer reagieren im Wahlkampfrecht. |
| `lagebild-medienresonanz` | Wahlkampfrecht Praxis: Medien-, Social- und Vor-Ort-Lage ohne Panikmetriken verdichten im Wahlkampfrecht. |
| `landeslisten-direktkandidaten` | Wahlkampfrecht Praxis: Landeslisten, Kreiswahlvorschlaege und Direktkandidaturen ordnen im Wahlkampfrecht. |
| `landesrecht-plakatierung-livecheck` | Wahlkampfrecht Praxis: Livecheck von Landes- und Kommunalrecht bei Plakatierung erzwingen im Wahlkampfrecht. |
| `landeswahlkampf-lagekarte` | Wahlkampfrecht Praxis: Landtagswahlkampf mit Landesrecht, Kreisverbaenden und lokalen Behörden strukturieren im Wahlkampfrecht. |
| `lautsprecher-fahrzeug` | Wahlkampfrecht Praxis: Lautsprecherwagen und mobile Wahlwerbung prüfen im Wahlkampfrecht. |
| `leak-und-hack-notfall` | Wahlkampfrecht Praxis: auf Leaks, Hacks und veroeffentlichte interne Dokumente reagieren im Wahlkampfrecht. |
| `lokale-buendnisse-marken-fremdlogos` | Wahlkampfrecht Praxis: lokale Buendnisse, Listenverbindungen und Unterstuetzungserklaerungen prüfen im Wahlkampfrecht. |
| `marken-und-fremdlogos` | Wahlkampfrecht Praxis: fremde Marken, Unternehmenslogos und Behördenanmutung prüfen im Wahlkampfrecht. |
| `memes-satire-risiko` | Wahlkampfrecht Praxis: Memes, Satire und Bildmontagen prüfen im Wahlkampfrecht. |
| `message-house-authentizitaet` | Wahlkampfrecht Praxis: Message House entwickeln, das Kandidierende nicht kuenstlich verbiegt im Wahlkampfrecht. |
| `minderjaehrige-und-fotos` | Wahlkampfrecht Praxis: Bilder, Schulformate und Daten Minderjaehriger prüfen im Wahlkampfrecht. |
| `nachwahl-evaluation-negative` | Wahlkampfrecht Praxis: Nachwahl-Evaluation ohne Selbstbetrug erstellen im Wahlkampfrecht. |
| `negative-campaigning-grenzen` | Wahlkampfrecht Praxis: Negative Campaigning auf Wahrheit, Fairness und Wirkung prüfen im Wahlkampfrecht. |
| `newsletter-messenger-sms` | Wahlkampfrecht Praxis: Newsletter, WhatsApp, Telegram, Signal und SMS-Wahlkampf prüfen im Wahlkampfrecht. |
| `oeffentliche-einrichtungen-nutzung` | Wahlkampfrecht Praxis: Nutzung öffentlicher Einrichtungen für Wahlkampf prüfen im Wahlkampfrecht. |
| `opposition-research-compliance` | Wahlkampfrecht Praxis: Opposition Research rechtlich und ethisch begrenzen im Wahlkampfrecht. |
| `ordner-sicherheit-parteieigenschaft` | Wahlkampfrecht Praxis: Ordner, Security und Deeskalation bei Wahlkampfterminen organisieren im Wahlkampfrecht. |
| `parteieigenschaft-bundeswahlausschuss` | Wahlkampfrecht Praxis: Parteieigenschaft und Beteiligungsanzeige vorbereiten im Wahlkampfrecht. |
| `plakat-vandalismus-beweissicherung` | Wahlkampfrecht Praxis: Beweissicherung bei beschaedigten Wahlplakaten organisieren im Wahlkampfrecht. |
| `plakatierung-genehmigung` | Wahlkampfrecht Praxis: kommunale Plakatierung und Sondernutzung rechtlich praktisch begleiten im Wahlkampfrecht. |
| `plakatstandorte-matrix` | Wahlkampfrecht Praxis: Standortmatrix für Plakate mit Sichtbarkeit und Rechtssicherheit erstellen im Wahlkampfrecht. |
| `plattformmeldung-dsa-podium` | Wahlkampfrecht Praxis: Plattformmeldewege und DSA-Mechanismen bei rechtswidrigen Inhalten nutzen im Wahlkampfrecht. |
| `podium-teilnahmeentscheidung` | Wahlkampfrecht Praxis: Teilnahme an Podien mit problematischen Mitbewerbern entscheiden im Wahlkampfrecht. |
| `polizei-und-ordnungsamt-kommunikation` | Wahlkampfrecht Praxis: robuste und freundliche Behördenkommunikation formulieren im Wahlkampfrecht. |
| `presseanfrage-antwortleiter` | Wahlkampfrecht Praxis: Presseanfragen in Sofortantwort, Hintergrund, Kein-Kommentar und Rechtspruefung sortieren im Wahlkampfrecht. |
| `presserecht-richtigstellung` | Wahlkampfrecht Praxis: Richtigstellung, Gegendarstellung und Unterlassung im Wahlkampf einordnen im Wahlkampfrecht. |
| `rapid-response-rechenschaftsbericht` | Wahlkampfrecht Praxis: akute Wahlkampfkrisen in Social Media, Presse und vor Ort in einen handlungsfähigen Rapid-Response-Prozess übersetzen im Wahlkampfrecht. |
| `rechenschaftsbericht-vorbereitung` | Wahlkampfrecht Praxis: Wahlkampfbelege für den Rechenschaftsbericht aufbereiten im Wahlkampfrecht. |
| `rechtsfreigabe-gate` | Wahlkampfrecht Praxis: schnellen Freigabeprozess für Plakate, Posts, Ads, Veranstaltungen und Spenden bauen im Wahlkampfrecht. |
| `risiko-register` | Wahlkampfrecht Praxis: lebendes Risiko-Register für Wahlkampfleitung und Rechtsberatung fuehren im Wahlkampfrecht. |
| `rumor-control-center` | Wahlkampfrecht Praxis: Geruechtekontrolle für Teams und Kandidierende einrichten im Wahlkampfrecht. |
| `satellitenkampagne-durch` | Wahlkampfrecht Praxis: Satellitenkampagne eines Vereins oder Dritten auf Zurechnung und Spendenrecht prüfen im Wahlkampfrecht. |
| `schlachtenplan-ethik-und-taktik` | Wahlkampfrecht Praxis: harten, aber demokratisch sauberen Kampagnenplan entwickeln im Wahlkampfrecht. |
| `schulen-und-jugendformate` | Wahlkampfrecht Praxis: Wahlkampfauftritte an Schulen, Jugendforen und Bildungseinrichtungen prüfen im Wahlkampfrecht. |
| `sicherheitslage-kandidierende` | Wahlkampfrecht Praxis: Schutzkonzept für Kandidierende und Wahlkampfteams erstellen im Wahlkampfrecht. |
| `social-media-redaktionsplan` | Wahlkampfrecht Praxis: rechtssicheren Redaktionsplan für Social Media bauen im Wahlkampfrecht. |
| `spendenannahme-sponsoring` | Wahlkampfrecht Praxis: Parteispenden und Sachleistungen vor Annahme prüfen im Wahlkampfrecht. |
| `sponsoring-parteienrecht` | Wahlkampfrecht Praxis: Sponsoring, Anzeigen, Messestaende und geldwerte Vorteile prüfen im Wahlkampfrecht. |
| `sprachregelung-schnellkarte` | Wahlkampfrecht Praxis: Sprachregelungen für Kandidierende, Presse und Ehrenamt erstellen im Wahlkampfrecht. |
| `staatliche-neutralitaet` | Wahlkampfrecht Praxis: staatliche Neutralität bei Schulen, Rathäusern, Amtsinhabern, Behördenkanälen und öffentlichen Einrichtungen prüfen im Wahlkampfrecht. |
| `taegliches-briefing` | Wahlkampfrecht Praxis: taegliches Lagebriefing für Spitze, Stab und Kreisverbaende erstellen im Wahlkampfrecht. |
| `targeting-dsgvo-tracking-pixel` | Wahlkampfrecht Praxis: Targeting und Zustellung politischer Werbung datenschutzrechtlich prüfen im Wahlkampfrecht. |
| `tracking-pixel-cookies` | Wahlkampfrecht Praxis: Kampagnenwebsite, Pixel, Conversiontracking und Cookies prüfen im Wahlkampfrecht. |
| `ueberkleben-sachbeschaedigung` | Wahlkampfrecht Praxis: Ueberkleben, Beschmieren oder Entfernen fremder Plakate prüfen im Wahlkampfrecht. |
| `umfragen-und-prognosen` | Wahlkampfrecht Praxis: Umfragen, Projektionen und interne Trackings richtig verwenden im Wahlkampfrecht. |
| `umgang-mit-provokateuren` | Wahlkampfrecht Praxis: Umgang mit Provokateuren bei Veranstaltungen und Strassenwahlkampf planen im Wahlkampfrecht. |
| `unterstuetzungsunterschriften` | Wahlkampfrecht Praxis: Sammlung von Unterstuetzungsunterschriften prüfen im Wahlkampfrecht. |
| `urheberrecht-musik-bilder-clips` | Wahlkampfrecht Praxis: Musik, Fotos, Stockbilder, Clips und Logos in Wahlwerbung prüfen im Wahlkampfrecht. |
| `veranstaltungslogistik` | Wahlkampfrecht Praxis: Kundgebung, Saalveranstaltung oder Marktplatztermin planen im Wahlkampfrecht. |
| `vereine-unterstuetzer-dritte` | Wahlkampfrecht Praxis: Unterstuetzung durch Vereine, Initiativen und Drittkampagnen prüfen im Wahlkampfrecht. |
| `versammlungsrecht-schnittstelle` | Wahlkampfrecht Praxis: politische Kundgebungen ins Versammlungsrecht routen im Wahlkampfrecht. |
| `viraler-clip-waehlerdaten-listen` | Wahlkampfrecht Praxis: auf unguenstigen viralen Clip ohne Panik reagieren im Wahlkampfrecht. |
| `waehlerdaten-und-listen` | Wahlkampfrecht Praxis: Waehler-, Mitglieder-, Interessenten- und Volunteerlisten prüfen im Wahlkampfrecht. |
| `wahl-o-mat-und-thesen` | Wahlkampfrecht Praxis: Antworten auf Wahl-O-Mat- oder Kandidatencheck-Thesen koordinieren im Wahlkampfrecht. |
| `wahlbeobachtung-und-wahltag` | Wahlkampfrecht Praxis: Wahlbeobachtung ohne Eingriff in Wahlhandlung briefen im Wahlkampfrecht. |
| `wahlkampf-in-vereinen-und-betrieben` | Wahlkampfrecht Praxis: Wahlkampf in Vereinen, Betrieben und halböffentlichen Räumen prüfen im Wahlkampfrecht. |
| `wahlkampfkosten-budget-wahlprogramm` | Wahlkampfrecht Praxis: Budget, Kostenstellen und Rechenschaftslogik bauen im Wahlkampfrecht. |
| `wahlprogramm-und-faktencheck` | Wahlkampfrecht Praxis: Wahlprogramm und Kurzforderungen auf belegbare Tatsachenbasis prüfen im Wahlkampfrecht. |
| `wahlpruefung-nachwahl` | Wahlkampfrecht Praxis: Wahlpruefung und Einspruch nach Wahlfehlern vorbereiten im Wahlkampfrecht. |
| `wahlraum-propagandaverbot` | Wahlkampfrecht Praxis: Wahlwerbung am Wahltag im und am Wahlgebaeude prüfen im Wahlkampfrecht. |
| `wahlstraftaten-stgb` | Wahlkampfrecht Praxis: Wahlstraftaten und strafrechtliche Nebenrisiken routen im Wahlkampfrecht. |
| `wahltag-war` | Wahlkampfrecht Praxis: Krisenkarte für Wahlsonntag erstellen im Wahlkampfrecht. |
| `wahlverfahren-falschinfo` | Wahlkampfrecht Praxis: Falschinformationen über Wahltermin, Briefwahl, Stimmzettel oder Wahlraeume beantworten im Wahlkampfrecht. |
| `wahlvorschlaege-fristen` | Wahlkampfrecht Praxis: Wahlvorschlaege, Beteiligungsanzeige und Fristen prüfen im Wahlkampfrecht. |
| `war-room-betriebsmodell` | Wahlkampfrecht Praxis: Wahlkampfzentrale mit Entscheidungswegen, Freigaben und Eskalation aufsetzen im Wahlkampfrecht. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
