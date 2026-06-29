# Staatsanwaltschaft Praxis-Einstieg

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Praxisplugin für neue Staatsanwaelte: Aktenstart, Anfangsverdacht, Ermittlungsauftrag, Eingriffe, Anklage, Strafbefehl, Einstellung, Sitzungsdienst, Rechtsmittel und OWiG.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`staatsanwaltschaft-praxis-einstieg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-praxis-einstieg.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-praxis-einstieg-werkstatt.md" download><code>staatsanwaltschaft-praxis-einstieg-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-praxis-einstieg-schnellstart.md" download><code>staatsanwaltschaft-praxis-einstieg-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`staatsanwaltschaft-praxis-einstieg-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-praxis-einstieg-testakte.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Tatvorwurf entlang von Beweiswuerdigung und Strafzumessung durchdringen und einen verwertbaren Schriftsatz bauen.
> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Strafverfolgung und Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 6 (Strafverfolgung) und Nr. 8 Buchstabe a (Justiz) der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die staatsanwaltschaftliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".
Praxisplugin für neue Staatsanwälte und Sitzungsdienst: Ermittlungsverfahren, Polizei, RiStBV, Vermerke, Beschlagnahme, digitale Beweise, Anklage, Strafbefehl, Hauptverhandlung, Plädoyer, Rechtsmittel und gerichtliche Bußgeldverfahren nach OWiG.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## OWiG- und Bußgeldspur

Für Ordnungswidrigkeiten arbeitet das Plugin bewusst mit anderer Sprache: kein Anklagesatz, kein Strafbefehl, sondern Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage über die Staatsanwaltschaft, gerichtliches Bußgeldverfahren, Beschlussverfahren, Hauptverhandlung und Rechtsbeschwerde. Die neuen `owi-*`-Skills helfen insbesondere bei Datenschutzbußgeldern, Verkehrs-OWi, Unternehmensgeldbußen, Aufsichtspflichtverletzungen, Umwelt-/Arbeitsschutz-/Produktsicherheits-OWi und der Frage, wann die Staatsanwaltschaft am Termin nach Paragraf 75 OWiG teilnehmen sollte.

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI in der Strafverfolgung. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 6 KI-VO**: KI-Systeme, die im Bereich der **Strafverfolgung** zur Bewertung von Beweismitteln, zur Risikoeinschätzung oder zur Aufklärung von Straftaten eingesetzt werden, sind grundsätzlich **Hochrisiko-KI**.
- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehörde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsätzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Verfügungen, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschläge produziert, die Subsumtion vornimmt oder die staatsanwaltschaftliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschließlich automatisierter Entscheidung

Die staatsanwaltschaftliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine erhebt Anklage, stellt ein oder beantragt Untersuchungshaft.** Diese Skills sind ausschließlich **Unterstützung** der staatsanwaltschaftlichen Arbeit, niemals deren Ersatz. Der Staatsanwalt prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschläge.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und das Amtsverschwiegenheitsgebot sind strikt zu wahren.
- Akteninhalte dürfen nicht ungeprüft an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewährleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behördlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Sämtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Staatsanwalt vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde.
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die staatsanwaltschaftliche Bearbeitung wird dokumentiert.
- Aufbewahrungsfristen nach Aktenordnung und KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Staatsanwaltschaften werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Installation

ZIP aus dem aktuellen Release laden und über die Plugin-Verwaltung installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 145 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `99-finale-entscheidung-volltext` | Erzeugt Anklageschrift, Strafbefehlsantrag, Einstellungs- oder Abschlussverfügung als zeichnungsreifen staatsanwaltschaftlichen Volltext mit Tatvorwurf, Beweisstand, Verfügungssatz und Rechtsbehelfshinweis. |
| `abschlussverfuegung-anfaengerfehler` | Abschlussverfügung: Anfängerfehler vermeiden: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `aktengeheimnis-und-ki-nutzung-staatsanwaelte` | Aktengeheimnis und KI-Nutzung in der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `anfangsverdacht-und-verfahrenseinleitung` | Anfangsverdacht und Verfahrenseinleitung: Praxis-Skill für neue Staatsanwälte zu Anfangsverdacht, Anzeige, Strafantrag, Offizialdelikt und erste Verfügung trennen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfüg... |
| `anklageschrift-aufbau` | Anklageschrift aufbauen: Praxis-Skill für neue Staatsanwälte zu Anklagesatz, Konkretisierung, Beweismittel, rechtliche Würdigung und wesentliche Ermittlungsergebnisse schreiben; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quelle... |
| `anklageschrift-grosse-wirtschaftsstrafkammer` | Anklageschrift zur großen Wirtschaftsstrafkammer: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `arbeitsstrafrecht-266a-aufsichtsbeschwerde` | Arbeitsstrafrecht: Paragraf 266a StGB, MiLoG und Scheinselbständigkeit: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `arbeitsstrafrecht-266a-und-mindestlohn` | Arbeitsstrafrecht: Paragraf 266a StGB, MiLoG und Scheinselbständigkeit: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `aufsichtsbeschwerde-und-dienstweg` | Aufsichtsbeschwerde, Dienstweg und sachliche Antwort: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `befangenheit-richter-antrag-staatsanwaelte` | Befangenheitsantrag gegen Richter: StA-Perspektive: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `befangenheit-richter-schoeffen` | Befangenheit von Richtern und Schöffen: Praxis-Skill für neue Staatsanwälte zu Ablehnung, Dienstaufsichtsfalle, Schöffenfragen und Verfahrensfairness aus StA-Sicht prüfen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck... |
| `bekaempfung-organisierte-kriminalitaet` | OK-Verfahren: Strukturermittlung ohne Tunnelblick: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `berufung-sta-beweisantraege-stpo` | Berufung der Staatsanwaltschaft einlegen und begrenzen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `berufung-sta-einlegen-und-begrenzen` | Berufung der Staatsanwaltschaft einlegen und begrenzen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `beschleunigtes-verfahren-418-stpo` | Beschleunigtes Verfahren nach Paragraf 418 StPO: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `beschuldigtenvernehmung-anhoerung` | Beschuldigtenvernehmung und Anhörung: Praxis-Skill für neue Staatsanwälte zu Belehrung, Schweigerecht, Verteidigerkontakt und Vernehmungsplanung rechtssicher steuern; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Ver... |
| `betrug-onlinehandel-beweis-und-schaden` | Betrug im Onlinehandel: Beweis, Schaden, Einstellungs- oder Anklagereife: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `beweisantraege-244-stpo-reagieren` | Beweisanträge nach Paragraf 244 StPO: Reaktion der StA: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `beweisverwertungsverbote-staatsanwaelte` | Beweisverwertungsverbote aus Sicht der StA: Praxis-Skill für neue Staatsanwälte zu mögliche Fehler früh erkennen, heilen, offenlegen oder verfahrensstrategisch berücksichtigen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellen... |
| `btmg-kcang-mischfaelle` | BtMG/KCanG-Mischfälle: Besitz, Handel, Grenzwerte: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `btmg-kcang-sitzungsdienst` | BtMG/KCanG im Sitzungsdienst: Praxis-Skill für neue Staatsanwälte zu Substanz, Menge, Wirkstoff, Eigenverbrauch, Handeltreiben und Strafzumessung in typischen Akten prüfen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellenchec... |
| `cybercrime-logfiles-daten-plattformen-deal` | Cybercrime: Logfiles und Chain of Custody: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `cybercrime-logfiles-und-chain-of-custody` | Cybercrime: Logfiles und Chain of Custody: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `daten-von-plattformen-bestandsdaten` | Bestands- und Nutzungsdaten von Plattformen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `deal-verstaendigung-257c-stpo-staatsanwaelte` | Verständigung nach Paragraf 257c StPO: StA sauber positionieren: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `digitale-durchsuchung-daten-sicherung` | Digitale Durchsuchung und Datensicherung: Praxis-Skill für neue Staatsanwälte zu Smartphones, Cloud, Messenger, Server, Hashwerte, Sichtung und Datenminimierung in den Griff bekommen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-... |
| `digitale-spuren-mobiltelefon-cloud` | Digitale Spuren: Mobiltelefon, Cloud, Chat und Standortdaten: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `dokumentenintake-und-aktenlog` | Dokumentenintake und Aktenlog: Praxis-Skill für neue Staatsanwälte zu ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und näc... |
| `durchsuchung-beschlagnahme-antrag` | Durchsuchung und Beschlagnahme: Praxis-Skill für neue Staatsanwälte zu richterlichen Beschluss, Gefahr im Verzug, Verhältnismäßigkeit und Dokumentation sauber vorbereiten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck... |
| `durchsuchung-beschlagnahme-kanzlei-arzt` | Staatsanwaltschaftlicher Skill zu Durchsuchung und Beschlagnahme: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `durchsuchung-kanzlei-arzt-redaktion` | Durchsuchung bei Berufsgeheimnisträgern: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `einstellung-153-153a-auflagen` | Einstellung nach Paragrafen 153/153a StPO: Auflagen sauber begründen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `einstellung-153-153a-stpo` | Einstellung nach Paragrafen 153 und 153a StPO: Praxis-Skill für neue Staatsanwälte zu Opportunität, Auflagen, Zustimmungserfordernisse, Opferinteressen und Dokumentation handhaben; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Que... |
| `einziehung-drittbetroffene-anhoerung` | Einziehung mit Drittbetroffenen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `encrochat-anom-sky` | EncroChat, ANOM, Sky ECC und Kryptodienste: Praxis-Skill für neue Staatsanwälte zu Krypto-Messenger-Beweise, Herkunft, Authentizität, Rechtshilfe, Verwertbarkeit und Verteidigungseinwände prüfen; mit Datenschutz-/Aktengeheimniswarnung, R... |
| `encrochat-anom-sky-ecc-krypto` | EncroChat, ANOM, Sky ECC und Kryptodienste: Praxis-Skill für neue Staatsanwälte zu Krypto-Messenger-Beweise, Herkunft, Authentizität, Rechtshilfe, Verwertbarkeit und Verteidigungseinwände prüfen; mit Datenschutz-/Aktengeheimniswarnung, R... |
| `encrochat-sky-ecc-anom-beweiswert` | EncroChat, Sky ECC und ANOM: Beweiswert und Verwertungsangriff: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `entscheidungsvorlage` | Entscheidungsvorlage: Praxis-Skill für neue Staatsanwälte zu macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächste... |
| `ermittlungsvermerk-schreiben` | Ermittlungsvermerk schreiben: Praxis-Skill für neue Staatsanwälte zu Sachstand, Tatverdacht, Beweislage, offene Ermittlungen und Entscheidungsvorschlag in einem brauchbaren Vermerk bündeln; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-... |
| `erste-woche-staatsanwaltschaft` | Erster Tag und erste Woche als Staatsanwältin oder Staatsanwalt: Onboarding-Leitfaden für den Berufseinstieg mit Rollenklärung Dezernent/Sitzungsdienst/Bereitschaft, Dezernatsübernahme, Fristen- und Haftsachenkontrolle, erste Eingangsver... |
| `europaeischer-haftbefehl-sta-praxis` | Europäischer Haftbefehl aus StA-Sicht: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `frist-und-zustaendigkeit-cockpit` | Fristen- und Zuständigkeitscockpit: Praxis-Skill für neue Staatsanwälte zu macht Fristen, Zuständigkeiten, Rechtsbehelfe und Vorfristen sofort sichtbar; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschl... |
| `fristenkalender-staatsanwaltschaft` | Fristenkalender im Dezernat: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `geldwaesche-krypto-haeusliche-gewalt` | Geldwäsche mit Krypto- oder Kontospuren: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `geldwaesche-krypto-und-kontoarrest` | Geldwäsche mit Krypto- oder Kontospuren: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `haeusliche-gewalt-opferschutz-und-beweis` | Häusliche Gewalt: Opferschutz, Aussage und Beweis: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `haftbefehl-und-u-haft-antrag` | Haftbefehl und Untersuchungshaft: Praxis-Skill für neue Staatsanwälte zu dringenden Tatverdacht, Haftgründe, Verhältnismäßigkeit und Beschleunigungsgebot für Haftanträge strukturieren; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO... |
| `hasskriminalitaet-online-und-plattformdaten` | Hasskriminalität online: Plattformdaten und Kontext: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `hauptverhandlung-sta-vorbereitung` | Hauptverhandlung vorbereiten: Praxis-Skill für neue Staatsanwälte zu Beweisthemen, Zeugen, Urkunden, Verständigung, Nebenklage und Reaktionsplan aus StA-Sicht ordnen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Ver... |
| `insolvenzverschleppung-bankrott-beweisimport` | Insolvenzverschleppung und Bankrott: Tatzeitraum sauber schneiden: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `insolvenzverschleppung-und-bankrott` | Insolvenzverschleppung und Bankrott: Tatzeitraum sauber schneiden: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `internationaler-beweisimport-verwertung` | Internationaler Beweisimport und Verwertung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `jugendstrafrecht-erziehungsziel` | Jugendstrafrecht aus StA-Sicht: Erziehungsziel und Beschleunigung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `jugendstrafrecht-staatsanwaelte` | Jugendstrafrecht für Staatsanwälte: Praxis-Skill für neue Staatsanwälte zu Erziehungsgedanke, Jugendgerichtshilfe, Diversion, Anklage und Sitzungsdienst abstimmen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfüg... |
| `kaltstart-routing` | Führt neue Staatsanwälte vom ersten Aktenblick in den richtigen Arbeitsmodus: Anfangsverdacht, Zuständigkeit, Beweisziel, Eingriff, Abschlussoption, Verfügung und Wiedervorlage. |
| `ki-und-deepfake-beweise-strafverfahren` | KI- und Deepfake-Beweise im Strafverfahren: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `koerperverletzung-strafantrag-230` | Körperverletzung und Strafantrag nach Paragraf 230 StGB: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `konfliktverteidigung-sitzung-ordnung` | Anstrengende Verteidigung in der Sitzung: souverän bleiben: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `konfliktverteidigung-sitzung-souveraen` | Anstrengende Verteidigung in der Sitzung: souverän bleiben: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `konfliktverteidigung-souveraen` | Staatsanwaltschaftlicher Skill zu Umgang mit harter Verteidigung: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `korruptionsdelikte-amtstraeger-und-healthcare` | Korruption: Amtsträger, Healthcare und Unternehmen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `mandanten-oder-beteiligtenkommunikation` | Beteiligtenkommunikation: Praxis-Skill für neue Staatsanwälte zu übersetzt das Ergebnis in klare, taktisch sichere Kommunikation; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |
| `mehrfachverfahren-verbindung-trennung` | Mehrfachverfahren: Verbindung, Trennung und Übersicht: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `opfer-und-nebenklage-kommunikation` | Opfer, Nebenklage und Adhäsion: Praxis-Skill für neue Staatsanwälte zu Verletztenrechte, Informationsrechte, Schutzmaßnahmen und Nebenklage ohne Rollenvermischung berücksichtigen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quel... |
| `opferrechte-nebenklage-adhaesion` | Opferrechte, Nebenklage und Adhäsion: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `owi-abwesenheit-betroffener-73-74` | Abwesenheit des Betroffenen: Entbindung, Verwerfung des Einspruchs und faire Sitzungsreaktion: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quel... |
| `owi-beschlussverfahren-72-und-widerspruch` | Beschlussverfahren nach Paragraf 72 OWiG: Widerspruchsfrist, Zustimmungslage und taktische Entscheidung prüfen: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzun... |
| `owi-beweisaufnahme-77-und-beweisantraege` | Beweisaufnahme im OWi-Verfahren: Aufklärungspflicht, vereinfachte Beweisaufnahme und Beweisanträge: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und... |
| `owi-bussgeldbescheid-inhalt-und-fehler` | Bußgeldbescheid prüfen: Tatbezeichnung, Rechtsgrundlage, Beweismittel, Nebenfolgen, Rechtsbehelf und typische Fehler erkennen: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Ve... |
| `owi-bussgeldbescheid-umwelt` | Bußgeldbescheid prüfen: Tatbezeichnung, Rechtsgrundlage, Beweismittel, Nebenfolgen, Rechtsbehelf und typische Fehler erkennen: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Ve... |
| `owi-datenschutz-bussgeld-lg-zustaendigkeit` | Datenschutz-Bußgeld nach DSGVO/BDSG: Aufsichtsbehörde, OWiG-Verweisung, Landgerichtsschwelle und Unternehmensgeldbuße: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren,... |
| `owi-einspruch-und-zwischenverfahren-69` | Staatsanwaltschaftlicher Skill zu Einspruch gegen Bußgeldbescheid und Zwischenverfahren: Frist, Beschränkung, Nachermittlung, Rücknahme oder Vorlage sauber steuern: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vor... |
| `owi-hauptverhandlung-sitzungsdienst-staatsanwaelte` | OWi-Hauptverhandlung im Sitzungsdienst: Teilnahme, Anträge, Beweisaufnahme, Einstellung und Urteilserwartung: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungs... |
| `owi-kaltstart-bussgeldverfahren-sta-rolle` | Staatsanwaltschaftlicher Skill zu OWiG-Kaltstart: Strafsache oder Ordnungswidrigkeit, Verwaltungsbehörde, Staatsanwaltschaft, Gericht und richtige Verfahrenssprache trennen: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Fris... |
| `owi-ki-deepfake-mehrfachverfahren-verbindung` | KI- und Deepfake-Beweise im Strafverfahren: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `owi-kommunikation-mit-verwaltungsbehoerde` | Kommunikation mit Verwaltungsbehörde und Gericht: sachkundig, knapp und rollenrein: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-kosten-vollstreckung-opportunitaet` | Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhyg... |
| `owi-kosten-vollstreckung-und-ruecknahme` | Kosten, Rücknahme, Rechtskraft und Vollstreckung im Bußgeldverfahren sauber abschließen: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhyg... |
| `owi-opferrechte-nebenklage-abwesenheit` | Opferrechte, Nebenklage und Adhäsion: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `owi-opportunitaet-einstellung-47` | Opportunität im OWi-Verfahren: Paragraf 47 OWiG als andere Logik als Legalitätsprinzip im Strafverfahren: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdien... |
| `owi-rechtsbeschwerde-79-80` | Rechtsbeschwerde im OWi-Verfahren: Zulässigkeit, Zulassung, Frist und StA-Entscheidung: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygi... |
| `owi-uebergang-revision-staatsanwaelte` | Staatsanwaltschaftlicher Skill zu Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `owi-uebergang-strafverfahren-81-82` | Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Qu... |
| `owi-umwelt-arbeitsschutz-produkt-bussgeld` | Umwelt-, Arbeitsschutz- und Produkt-OWi: technische Behördenakten in gerichtsfeste Bußgeldlogik bringen: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdiens... |
| `owi-verbandsgeldbusse-30-130` | Unternehmens- und Aufsichtspflicht-Ordnungswidrigkeiten: Paragrafen 30 und 130 OWiG in der Praxis: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und... |
| `owi-verjaehrung-verfolgungsverjaehrung` | Verjährung im OWi-Verfahren: Verfolgungsverjährung, Unterbrechung und Aktenkalender: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-verkehrsowi-fahrverbot-punkte` | Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Q... |
| `owi-verkehrsowi-vorlage-an` | Staatsanwaltschaftlicher Skill zu Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `owi-vorlage-an-amtsgericht-sta-check` | Vorlage der OWi-Akte an das Amtsgericht: Staatsanwaltschaft als Filter, nicht als Anklageschreiberin: OWiG-Praxis-Skill für junge Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst u... |
| `pflichtverteidigung-aus-sta-sicht` | Pflichtverteidigung aus Sicht der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `plaedoyer-beweiswuerdigung-strafmass` | Plädoyer: Beweiswürdigung und Strafmaß sauber bauen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `plaedoyer-staatsanwaltschaft` | Plädoyer der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwälte zu Schuldfrage, Beweiswürdigung, Strafzumessung, Nebenfolgen und Antrag klar und fair darstellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Ver... |
| `polizei-ermittlungsauftrag-nachsteuerung` | Ermittlungsauftrag an die Polizei: Nachsteuerung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `polizei-zusammenarbeit-ermittlungsauftrag` | Zusammenarbeit mit der Polizei: Praxis-Skill für neue Staatsanwälte zu Ermittlungsaufträge so schreiben, dass die Polizei weiß, was beweiserheblich ist und was nicht; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Ver... |
| `polizei-zusammenarbeit-presse-oeffentlichkeit` | Staatsanwaltschaftlicher Skill zu Zusammenarbeit mit der Polizei: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `presse-und-oeffentlichkeit` | Presse und Öffentlichkeit: Praxis-Skill für neue Staatsanwälte zu Presserecht, Persönlichkeitsrechte, Unschuldsvermutung und Behördenkommunikation vorsichtig handhaben; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, V... |
| `presseauskunft-und-oeffentlichkeit` | Presseauskunft und Öffentlichkeit in Strafsachen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `protokoll-und-nachbereitung` | Protokoll und Nachbereitung: Praxis-Skill für neue Staatsanwälte zu sichert Verlauf, Zusagen, Beschlüsse, Auflagen und nächste Wiedervorlagen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und näc... |
| `prozessuale-kniffe-und-rechtsprechungsanker` | Stellt staatsanwaltschaftliche Verfahrenskniffe, Rechtsprechungsanker, Eingriffsgrenzen, Abschlussoptionen und Sitzungsdienst-Strategie in eine sofort nutzbare Matrix. |
| `quellen-rechtsprechungscheck-anfangsverdacht` | Quellen- und Rechtsprechungscheck: Praxis-Skill für neue Staatsanwälte zu verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag un... |
| `quellen-und-rechtsprechungscheck` | Quellen- und Rechtsprechungscheck: Praxis-Skill für neue Staatsanwälte zu verhindert Blindzitate und zwingt zu amtlich oder frei prüfbaren Quellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag un... |
| `rechtshilfe-europaeische-ermittlungsanordnung` | Europäische Ermittlungsanordnung und Rechtshilfe: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `rechtshilfe-international` | Internationale Rechtshilfe: Praxis-Skill für neue Staatsanwälte zu Ersuchen, Europäische Ermittlungsanordnung, MLAT, Auslieferung und Datenübermittlung in der Akte markieren; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellench... |
| `rechtshilfe-international-ristbv-finden` | Staatsanwaltschaftlicher Skill zu Internationale Rechtshilfe: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `rechtsmittel-sta-berufung-revision` | Rechtsmittel der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwälte zu Berufung, Revision, Beschwerde, Frist, Begründung und Zustimmung bei Rücknahme sauber steuern; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck,... |
| `red-team-qualitygate` | Red-Team-Qualitygate: Praxis-Skill für neue Staatsanwälte zu prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und näch... |
| `revision-sta-verfahrensruegen-vorpruefung` | Revision der Staatsanwaltschaft: Vorprüfung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `ristbv-finden-anwenden` | Staatsanwaltschaftlicher Skill zu RiStBV finden und anwenden: ordnet Tatverdacht, Zuständigkeit, Beweisstand, Verfügung, Frist und Vorlagegrenze. |
| `ristbv-verfuegungstechnik-standard` | RiStBV-Verfügungstechnik und Dezernatsstandard: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `sachverstaendige-beauftragen-und-befragen` | Sachverständige beauftragen und in der HV befragen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `schoeffen-befangenheit-und-mitwirkung` | Schöffen: Befangenheit, Ausfall und Mitwirkung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `schriftsatz-vermerk-und-mustertext` | Schriftsatz, Vermerk und Mustertext: Praxis-Skill für neue Staatsanwälte zu liefert einen belastbaren ersten Entwurf mit offenen Punkten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem... |
| `sexualdelikte-aussage-gegen` | Sexualdelikte: Aussage-gegen-Aussage ohne Abkürzung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `sexualdelikte-aussage-gegen-aussage` | Sexualdelikte: Aussage-gegen-Aussage ohne Abkürzung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `sicherungsverfahren-413-stpo` | Sicherungsverfahren und Maßregelantrag: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `sitzungs-und-terminvorbereitung` | Sitzungs- und Terminvorbereitung: Praxis-Skill für neue Staatsanwälte zu bereitet Gerichtstermin, Behördenkontakt, Kammertermin oder Verhandlungstag vor; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorsch... |
| `sitzungsdienst-amtsgericht` | Sitzungsdienst am Amtsgericht: Praxis-Skill für neue Staatsanwälte zu Aktenvorbereitung, Beweisaufnahme, Anträge, Plädoyer und Rechtsmittelnotiz für den ersten Sitzungsdienst; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellenc... |
| `sitzungsdienst-referendar-notfallkarte` | Sitzungsdienst für Referendare: Notfallkarte: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `staatsanwalt-rolle-legalitaet-objektivitaet` | Rolle der Staatsanwaltschaft: Legalität und Objektivität: Praxis-Skill für neue Staatsanwälte zu Rolle als objektive Verfahrensleiterin im Ermittlungsverfahren, Legalitätsprinzip und Belastungs-/Entlastungsermittlung; mit Datenschutz-/Ak... |
| `staatsanwalt-rolle-staatsanwaltschaft` | Rolle der Staatsanwaltschaft: Legalität und Objektivität: Praxis-Skill für neue Staatsanwälte zu Rolle als objektive Verfahrensleiterin im Ermittlungsverfahren, Legalitätsprinzip und Belastungs-/Entlastungsermittlung; mit Datenschutz-/Ak... |
| `staatsanwaltschaft-entscheidungsvorlage-verfuegung` | Entscheidungsvorlage: Praxis-Skill für neue Staatsanwälte zu macht aus der Prüfung eine Entscheidung mit Optionen, Risiken und Empfehlung; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächste... |
| `staatsanwaltschaft-uebergabe-zwischen-dezernaten` | Dezernatsuebergabe in der Staatsanwaltschaft: prüft Aktenstand, Fristen, Haft, offene Ermittlungsauftraege, Beweisrisiken und Abschlussreife mit Übergabevermerk und naechstem Schritt im Staatsanwaltschafts-Praxis. |
| `staatsanwaltschaft-zwischen-dezernaten` | Dezernatsuebergabe in der Staatsanwaltschaft: prüft Aktenstand, Fristen, Haft, offene Ermittlungsauftraege, Beweisrisiken und Abschlussreife mit Übergabevermerk und naechstem Schritt. |
| `stalking-238-stgb-gewschg-schnittstelle` | Stalking Paragraf 238 StGB und GewSchG-Schnittstelle: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `steuerstrafrecht-kooperation` | Steuerstrafrecht: Zusammenarbeit mit Steuerfahndung und Finanzamt: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `steuerstrafrecht-kooperation-finanzamt` | Steuerstrafrecht: Zusammenarbeit mit Steuerfahndung und Finanzamt: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `strafbefehl-beantragen` | Strafbefehl beantragen: Praxis-Skill für neue Staatsanwälte zu Eignung, Rechtsfolgen, Tagessätze, Fahrverbot, Bewährung und Verteidigungsrechte prüfen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschla... |
| `strafbefehl-tagessaetze-und-nebenfolgen` | Strafbefehl: Tagessätze, Nebenfolgen und Einspruchsrisiko: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `u-haft-fluchtgefahr-verhaeltnismaessigkeit` | U-Haft: Fluchtgefahr, Verdunkelung und Verhältnismäßigkeit: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `u-haft-umweltstrafrecht-behoerdenakten` | U-Haft: Fluchtgefahr, Verdunkelung und Verhältnismäßigkeit: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt im Staatsanwaltschafts-Praxis. |
| `umweltstrafrecht-behoerdenakten` | Umweltstrafrecht: Behördenakten und technische Beweise: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `untreue-geschaeftsfuehrer-kontoanalyse` | Untreue des Geschäftsführers: Kontoanalyse und Pflichtwidrigkeit: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `urheber-und-markenstrafrecht-praxis` | Urheber- und Markenstrafrecht: Akten schnell sortieren: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `verkehrsstrafrecht-blutprobe-fahrerlaubnis` | Verkehrsstrafrecht: Blutprobe, Fahrerlaubnis und Strafbefehl: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `verkehrsstrafrecht-strafbefehl` | Verkehrsstrafrecht und Strafbefehl: Praxis-Skill für neue Staatsanwälte zu Paragrafen 142/315c/316 StGB, Entziehung, Sperre, Fahrverbot und Strafbefehl routiniert bearbeiten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellench... |
| `vermerk-mustertext-sexualdelikte-aussage` | Schriftsatz, Vermerk und Mustertext: Praxis-Skill für neue Staatsanwälte zu liefert einen belastbaren ersten Entwurf mit offenen Punkten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem... |
| `vermoegensarrest-einziehung` | Vermögensarrest und Einziehung: Praxis-Skill für neue Staatsanwälte zu Einziehung, Arrest, Verletztenrechte und Vermögensabschöpfung früh und verhältnismäßig planen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verf... |
| `vermoegensarrest-einziehung-schnellcheck` | Vermögensarrest und Einziehung: schneller Sicherungscheck: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `vollstreckung-und-gnadenschnittstelle` | Vollstreckung und Gnadenschnittstelle: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `waffenrecht-und-sprengstoff-nebenstrafrecht` | Waffen- und Sprengstoffsachen: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `wirtschaftsstrafsachen-sachleitung` | Wirtschaftsstrafsachen sachleiten: Praxis-Skill für neue Staatsanwälte zu komplexe Tatkomplexe, Gutachten, Finanzdaten, Durchsuchung, Arrest und Verständigung koordinieren; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellenchec... |
| `wirtschaftsstrafverfahren-datenraum-aktenplan` | Wirtschaftsstrafverfahren: Aktenplan und Datenraum: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `wohnungsdurchsuchung-gefahr-im-verzug` | Wohnungsdurchsuchung und Gefahr im Verzug: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `zeugenmanagement-und-ladungsrisiken` | Zeugenmanagement für die Hauptverhandlung: Praxis-Skill für neue Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `zeugenvernehmung-zeugenrechte` | Zeugenvernehmung und Zeugenrechte: Praxis-Skill für neue Staatsanwälte zu Ladung, Belehrung, Aussageverweigerung, Auskunftsverweigerung und Schutzbedarf beachten; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügu... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
