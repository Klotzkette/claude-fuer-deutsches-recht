---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Prozessrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordn..."
---

# Prozessrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Prozessrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Bei tragenden ZPO-Fragen zuerst `amtlicher-zpo-verfahrenscheck` zuschalten, damit Zuständigkeit, Schriftsatzform, Zustellung, Frist, Beweis, Mahnverfahren, Vollstreckung und Eilrechtsschutz gegen die aktuelle ZPO-Fassung laufen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

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

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anspruchstabelle` | Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: Paragrafen 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output:… |
| `anwaltsgeheimnis-pruefung` | Anwaltsgeheimnis und Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen. Normen: Paragraf 43a BRAO, Paragraf 203 StGB, Paragraf 102 ZPO. Prüfraster: Offenbarungsbefugnis, Zeugnisverweigerungsrecht, strafrechtliche… |
| `beweissicherung` | Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten: Sachverständigengutachten vor Klageerhebung sichern. Normen: Paragrafen 485 ff. ZPO. Prüfraster: Beweissicherungsinteresse, Antragstellung, Gutachterauswahl,… |
| `chronologie` | Sachverhaltschronologie für Klageschrift oder Verteidigung aufbauen: Zeitlinie mit Belegen und Normbezug. Normen: Paragrafen 253 138 ZPO. Prüfraster: Ereignisse, Zeitpunkte, Dokumente, Normbezug, streitige vs. unstreitige… |
| `einstweilige-verfuegung` | Antrag auf einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprüche formulieren. Normen: Paragrafen 935 940 ZPO. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Glaubhaftmachung, Zuständigkeit, Arrest-Abgrenzung.… |
| `gegenseite-status` | Prozessualen Status der Gegenseite erfassen: Bevollmaechtigung, Zustelladresse, Insolvenzantrag, Kostensicherheit. Normen: Paragrafen 78 85 ZPO. Prüfraster: Vertreternachweis, Prozessvollmacht, Beklagteninsolvenz,… |
| `mahnbescheid` | Mahnbescheid im gerichtlichen Mahnverfahren beantragen: Voraussetzungen, Formulierung, Übergang zum Streitverfahren. Normen: Paragrafen 688 ff. ZPO. Prüfraster: Zuständigkeit Mahngericht, bestimmte Geldforderung,… |
| `mahnschreiben-aufnahme` | Erhaltenes Mahnschreiben der Gegenseite aufnehmen und einordnen: Anerkennungsgefahr, Verjaebrungshemmung. Normen: Paragrafen 204 212 BGB, Paragraf 93 ZPO. Prüfraster: Fristenlauf, Anerkennungsrisiko, Reaktionsoptionen. Output:… |
| `mahnschreiben-entwurf` | Vorgerichtliches Mahnschreiben entwerfen: Zahlungsaufforderung mit Frist und Klageankündigung. Normen: Paragrafen 286 288 BGB, Paragrafen 204 ff. BGB. Prüfraster: Verjaebrungshemmung, Verzugsbeginn, Schadensersatz, Klageandrohung.… |
| `mahnschreiben-erhalten` | Auf erhaltenes Mahnschreiben der Gegenseite reagieren: Widerspruch, Zahlungsplan oder Verjaebrungsaufschub. Normen: Paragrafen 286 287 BGB, Paragrafen 203 204 BGB. Prüfraster: Forderungsprüfung, Verjaebrungsrisiko,… |
| `mandat-aktualisierung` | Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschlüsse, Fristen eintragen. Normen: Paragrafen 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes… |
| `mandat-aufnahme` | Prozessmandat aufnehmen: Sachverhalt erfassen, Zuständigkeit prüfen, Klagekonzept skizzieren. Normen: Paragrafen 253 261 ZPO, BRAO. Prüfraster: Sachverhaltserfassung, Anspruchsgrundlage, Zuständigkeit, Kosten-Risiko-Analyse.… |
| `mandat-briefing` | Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: Paragrafen 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für… |
| `mandat-schliessen` | Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: Paragrafen 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output:… |
| `portfolio-status` | Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht… |
| `prozessrecht-anpassen` | Prozessrechtliche Strategie im laufenden Verfahren anpassen: Klageaenderung, Widerklage, Rücknahme. Normen: Paragrafen 263 264 269 ZPO. Prüfraster: Klageaenderungsvoraussetzungen, Rücknahmefolgen, Widerklagemöglichkeiten.… |
| `prozessrecht-kaltstart-interview` | Prozessrechtliches Erstinterview strukturiert durchführen: Sachverhalt, Klagebegehren, Fristen, Kosten. Normen: Paragrafen 253 261 ZPO, BRAO. Prüfraster: Anspruchsgrundlage, Zuständigkeit, Verjaebrung, Kostenrisiko. Output:… |
| `prozessrecht-mandat-arbeitsbereich` | Digitaler Arbeitsbereich für Prozessmandate: Dokumentenablage, Aufgabenverteilung, Fristentracking. Normen: ZPO, BRAO. Prüfraster: Dokumentenstruktur, Aufgabenliste, Fristverwaltung. Output:… |
| `schriftsatz-abschnitt` | Einzelne Abschnitte eines Schriftsatzes erstellen: Tatbestand, Begründung, Beweisangebot nach ZPO-Schema. Normen: Paragrafen 253 313 ZPO. Prüfraster: Schluessigskeit, Beweisangebot, Normzitat. Output: Schriftsatz-Abschnitt für… |
| `strafverteidigung-ersttermin` | Ersttermin bei Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, prozessuale Schritte. Normen: Paragrafen 137 147 StPO. Prüfraster: Akteneinsichtsrecht, Mandatsverhältnis, erste Verteidigungsoptionen. Output:… |
| `streitwert` | Streitwert für zivilrechtliche Klagen berechnen: Hauptforderung, Nebenforderungen, Gerichts- und Anwaltsgebühren. Normen: Paragrafen 3 9 ZPO, GKG, RVG. Prüfraster: Streitwertbemessung, Nebenforderungen, Kostenfolge. Output:… |
| `verkehrsunfall` | Verkehrsunfall-Mandat im Zivilprozess vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz. Normen: Paragrafen 7 18 StVG, Paragrafen 823 253 BGB, Paragraf 115 VVG. Prüfraster: Haftungsquote, Schadensposten, Verjaebrung,… |
| `vollstreckung` | Zwangsvollstreckung aus Zivilurteil vorbereiten und einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung. Normen: Paragrafen 704 ff. ZPO. Prüfraster: vollstreckbarer Titel, Klausel, Zustellungsnachweis,… |
| `vorlageanordnung` | Vorlageanordnung nach Paragraf 142 ZPO beantragen: Vorlage von Urkunden durch Gegner oder Dritte. Normen: Paragrafen 142 143 ZPO. Prüfraster: urkundliche Beweise, Pflicht zur Vorlage, Sanktionen bei Weigerung. Output: Antrag auf… |
| `zeuge-vorbereitung` | Zeuge für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsablauf. Normen: Paragrafen 373 ff. 383 ff. ZPO. Prüfraster: Zeugnisverweigerungsrecht, Glaubwürdigkeitsfragen, Vernehmungsthemen. Output:… |

## Worum geht es?

Das Prozessrecht-Plugin unterstuetzt Anwaltskanzleien bei zivilprozessualen Mandaten nach der Zivilprozessordnung (ZPO): von der Mandatsaufnahme über Mahnschreiben, Mahnbescheid und Klageschrift bis zu Beweissicherung, einstweiliger Verfuegung, Vollstreckung und Rechtsmitteln. Zusaetzlich sind grundlegende Strafverteidigungsschritte für den Ersttermin sowie verkehrsunfallrechtliche Grundlagen abgedeckt.

Das Plugin richtet sich an Generalisten-Kanzleien, die Zivilprozesse fuehren, sowie an Anwaelte, die ein strukturiertes Mandats-Tracking und Fristverwaltung benoetigen.

## Wann brauchen Sie diese Skill?

- Ein neues Prozessmandat ist aufzunehmen: Sachverhalt klären, Zuständigkeit prüfen und Kosten-Risiko-Analyse vornehmen.
- Eine Geldforderung soll schnell per Mahnbescheid geltend gemacht oder ein erhaltenes Mahnschreiben beantwortet werden.
- Eine einstweilige Verfuegung zur Sicherung zivilrechtlicher Ansprueche ist zu beantragen.
- Ein Urteil liegt vor und es soll vollstreckt werden (Pfaendung, Sachpfaendung, Forderungspfaendung).
- Ein Portfolio laufender Prozessmandate soll nach Fristen und Verfahrensstand ueberwacht werden.

## Fachbegriffe (kurz erklaert)

- **Streitwert** — der Geldwert des Streitgegenstands; bestimmt Gerichts- und Anwaltsgebuehren sowie die sachliche Zuständigkeit.
- **Mahnbescheid** — gerichtliche Zahlungsaufforderung im schriftlichen Mahnverfahren (Paragrafen 688 ff. ZPO); bei Widerspruch Uebergang zum streitigen Verfahren.
- **Einstweilige Verfuegung** — vorläufige gerichtliche Maßnahme zur Sicherung eines Anspruchs (Paragrafen 935 ff. ZPO); Verfuegungsanspruch und Verfuegungsgrund erforderlich.
- **Beweissicherung** — selbständiges Beweisverfahren nach Paragrafen 485 ff. ZPO; sichert Gutachten oder Tatsachen vor Klageerhebung.
- **Vollstreckbarer Titel** — Grundlage für Zwangsvollstreckung (Paragraf 704 ZPO); benoetigt Vollstreckungsklausel und Zustellungsnachweis.
- **Vorlageanordnung** — gerichtliche Anordnung zur Vorlage von Urkunden durch Gegner oder Dritte (Paragraf 142 ZPO).

## Rechtsgrundlagen

- Paragrafen 253 ff. ZPO — Klageschrift und Klagezulaessigkeit
- Paragrafen 688 ff. ZPO — Mahnverfahren und Mahnbescheid
- Paragrafen 935 ff. ZPO — einstweilige Verfuegung
- Paragrafen 485 ff. ZPO — selbständiges Beweisverfahren
- Paragrafen 704 ff. ZPO — Zwangsvollstreckung
- Paragraf 142 ZPO — Vorlageanordnung
- Paragrafen 3 ff. ZPO — Streitwertbemessung
- Paragraf 78 ZPO — Anwaltszwang (ab Landgericht)
- Paragrafen 137 ff. StPO — Strafverteidigung und Akteneinsicht

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Kläger oder Beklagter? Zivilsache oder Strafsache? Eilbedarf?
2. Phase des Mandats bestimmen: Vorprozessual (Mahnschreiben, Mahnbescheid), Klagephase, Beweissicherung oder Vollstreckung?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen prüfen: Verjaebrung (Paragrafen 195 ff. BGB), Klageanmeldefristen, Widerspruchsfristen beim Mahnbescheid (zwei Wochen).
5. Anschluss-Skill bestimmen: Nach Klageschrift ggf. einstweilige Verfuegung; nach Urteil Vollstreckungsauftrag.

## Skill-Tour (was gibt es hier?)

- `mandat-aufnahme` — Prozessmandat aufnehmen: Sachverhalt, Zuständigkeit, Klagekonzept skizzieren.
- `prozessrecht-kaltstart-interview` — Erstinterview strukturiert durchfuehren: Sachverhalt, Klagebegehren, Fristen, Kostenrisiko.
- `prozessrecht-mandat-arbeitsbereich` — Digitaler Arbeitsbereich: Dokumentenablage, Aufgabenverteilung, Fristentracking.
- `prozessrecht-anpassen` — Strategie anpassen: Klageaenderung, Widerklage, Rücknahme (Paragrafen 263 ff. ZPO).
- `mandat-aktualisierung` — Laufendes Mandat aktualisieren: neue Schriftsaetze, Beschlüsse, Fristen eintragen.
- `portfolio-status` — Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte.
- `mandat-briefing` — Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen.
- `mandat-schliessen` — Mandat formal schliessen: Kostenfestsetzung, Archivierung, Mandanteninformation.
- `anspruchstabelle` — Anspruchstabelle erstellen: alle Ansprueche und Gegenansprueche tabellarisch.
- `streitwert` — Streitwert berechnen: Hauptforderung, Nebenforderungen, Kosten und Gebührentabelle.
- `chronologie` — Sachverhaltschronologie aufbauen: Zeitlinie mit Belegen und Normbezug.
- `gegenseite-status` — Prozessualen Status der Gegenseite erfassen: Vollmacht, Zustelladresse, Insolvenz.
- `mahnschreiben-entwurf` — Vorgerichtliches Mahnschreiben erstellen: Fristsetzung, Verzugsbeginn, Klageandrohung.
- `mahnschreiben-aufnahme` — Erhaltenes Mahnschreiben einordnen: Anerkennungsgefahr, Verjaebrungshemmung.
- `mahnschreiben-erhalten` — Auf erhaltenes Mahnschreiben reagieren: Widerspruch, Zahlungsplan, Verjaebrungsaufschub.
- `mahnbescheid` — Mahnbescheid im gerichtlichen Mahnverfahren beantragen (Paragrafen 688 ff. ZPO).
- `einstweilige-verfuegung` — Antrag auf einstweilige Verfuegung zur Anspruchssicherung formulieren (Paragrafen 935 ff. ZPO).
- `beweissicherung` — Beweissicherungsantrag im selbständigen Beweisverfahren vorbereiten (Paragrafen 485 ff. ZPO).
- `vorlageanordnung` — Urkundenvorlageanordnung nach Paragraf 142 ZPO beantragen.
- `schriftsatz-abschnitt` — Einzelne Abschnitte eines Schriftsatzes erstellen (Tatbestand, Begruendung, Beweisangebot).
- `vollstreckung` — Zwangsvollstreckung einleiten: Pfaendung, Sachpfaendung, Forderungspfaendung (Paragrafen 704 ff. ZPO).
- `zeuge-vorbereitung` — Zeugen für Gerichtstermin vorbereiten: Aussagerecht, Zeugnisverweigerung, Vernehmungsthemen.
- `anwaltsgeheimnis-pruefung` — Verschwiegenheitspflicht bei Weitergabe von Mandatsinformationen prüfen.
- `verkehrsunfall` — Verkehrsunfall-Mandat vorbereiten: Schadensersatz, Schmerzensgeld, Versicherungskorrespondenz.
- `strafverteidigung-ersttermin` — Ersttermin in der Strafverteidigung vorbereiten: Akteneinsicht, Schweigepflicht, Optionen.

## Worauf besonders achten

- **Anwaltszwang ab LG**: Vor dem Landgericht und hoeheren Instanzen gilt Paragraf 78 ZPO; nur vor dem Amtsgericht kann der Mandant ohne Anwalt auftreten.
- **Verjaebrung laeuft gegen Kläger**: Mahnschreiben hemmen Verjaebrung nicht; erst Klageschrift oder Mahnbescheid hemmen nach Paragraf 204 BGB.
- **Widerspruch beim Mahnbescheid in zwei Wochen**: Wer keinen Widerspruch einlegt, erhalt auf Antrag des Glaebigers einen Vollstreckungsbescheid.
- **Glaubhaftmachung bei eV**: Ohne eidesstattliche Versicherung oder sonstige Glaubhaftmachung wird der Antrag auf einstweilige Verfuegung zurueckgewiesen.
- **Kostenfestsetzungsantrag nicht vergessen**: Nach obsiegendem Urteil muss der Kostenfestsetzungsantrag gestellt werden; das Gericht tituliert Kosten nicht von Amts wegen.

## Typische Fehler

- Klageschrift ohne bestimmten Antrag eingereicht: Paragraf 253 Abs. 2 Nr. 2 ZPO verlangt einen konkreten Antrag; ohne ihn ist die Klage unzulaessig.
- Beweismittel nicht benannt: Paragraf 138 ZPO verlangt, dass Beweismittel zumindest bezeichnet werden; spaeteres Nachschieben kann Verspaeterngsfolgen ausloesen.
- Streitwert zu niedrig angesetzt: Unterschaetzung fuehrt zu zu niedrigen Gebühren und verzoegert Verfahren, wenn nachtraeglich korrigiert wird.
- Kein Widerspruch auf Mahnbescheid eingelegt: Rechtskraftfalle — der Vollstreckungsbescheid ist vollstreckbarer Titel.
- Vollstreckung ohne Klausel und Zustellungsnachweis begonnen: Vollstreckungsorgane werden Auftrag zurueckweisen; Paragraf 750 ZPO ist Grundvoraussetzung.

## Quellen und Aktualitaet

- Stand: 05/2026
- ZPO in geltender Fassung
- GKG und RVG in geltender Fassung
- Paragraf 23 Nr. 1 GVG: Streitwertgrenze AG 10.000 EUR seit 01.01.2026
