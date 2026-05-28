---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Aktenauszug Gerichtsverfahren-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Aktenauszug Gerichtsverfahren — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Aktenauszug Gerichtsverfahren**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivortraege Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten.

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
| `aktenauszug-erstellen` | Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze oder PDFs und will strukturierten Aktenauszug erstellen. Sechs Bausteine: Verfahrensidentifikation Einleitungssatz Absatz-Zusammenfassung Sachverhaltschronologie… |
| `aktenauszug-strukturpruefung` | Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Prüfraster Bausteine-Vollständigkeit Fristen-Markierung… |
| `anlagenverzeichnis-extrakt` | Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der Akte und will Anlagenverzeichnis erstellen. Anlagenbezeichnung Kurzbeschreibung Schriftsatz Blattangabe je Partei. Normen §§ 130 131 ZPO Schriftsatz-Anlagen.… |
| `anwaltsschriftsatz-stilrichtlinie` | Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln… |
| `arbeitsgerichtsverfahren-modus` | Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwochenfrist § 4 KSchG Berufung § 64 ArbGG Revision § 72 ArbGG. Normen ArbGG §§ 2 54 64 72 KSchG §§ 1… |
| `beweismittel-gegenueberstellung` | Anwalt will Beweisangebote aller Parteien uebersichtlich gegenüberstellen: Zeugen Urkunden Sachverständige Parteivernehmung Augenschein. Normen §§ 355-455 ZPO Sachverständigenbeweis Zeugenbeweis. Prüfraster… |
| `einleitungssatz-generator` | Aktenauszug braucht praegnanten Einleitungssatz: wer streitet mit wem worueber welche Hauptnorm. Juristisch praezise neutral ohne Wertung ohne Erfolgsprognose. Normen §§ 253 304 ZPO. Prüfraster Praegnanz… |
| `fristen-und-terminkalender` | Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungsfrist Verkündungstermin Vollziehungsfrist. Normen §§ 222 517 520 548 ZPO. Prüfraster… |
| `neutralitaetspruefung` | Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale… |
| `parteivortrag-gegenueberstellung` | Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und Beklagtenseite) für streitige Sachverhaltsangaben Punkt für Punkt. Jeder Streitpunkt wird als eigene Zeile gegenübergestellt. Fundstellen in Schriftsaetzen… |
| `rechtsargumente-gegenueberstellung` | Erstellt eine tabellarische Gegenüberstellung der Rechtsargumente beider Parteien: Anspruchsgrundlage Einwendungen Einreden Verjährungsthema und Pinpoint-Zitate aus Rechtsprechung (BGH OLG EuGH). Keine Wertung welches… |
| `sachverhaltschronologie` | Erstellt eine chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen: Vertragsschluss Vorfaelle vorgerichtliche Korrespondenz Schadensereignisse und Behoerdenakte. Datum fett vorangestellt knappe… |
| `schwerpunktthemen-identifikation` | Anwalt braucht schnellen Überblick über drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten ohne Erfolgsprognose. Normen §§ 139 286 ZPO BGH-Leitsaetze. Prüfraster… |
| `sozialgerichtsverfahren-modus` | Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtsermittlungsgrundsatz Sozialversicherungs-Leistungsarten. Normen SGG §§ 51 77 86b 143. Prüfraster… |
| `strafprozess-modus` | Aktenauszug für StPO-Verfahren erstellen: Anklage Hauptverhandlung Revision §§ 333 ff. StPO Wiederaufnahme. Anklageschrift Eroeffnungsbeschluss Beweisantragsrecht Rechtsmittelfristen. Normen StPO §§ 200 203 333 359… |
| `verfahrenschronologie` | Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen… |
| `verfahrensidentifikation` | Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und… |
| `verfahrenszusammenfassung-absatz` | Anwalt will sich schnell in Akte einarbeiten ohne vollständige Lektuere. Acht bis zehn Saetze Hintergrund Streitstand prozessuale Lage anstehende Verfahrenshandlungen. Normen §§ 253 261 ZPO. Prüfraster Vollständigkeit… |
| `verwaltungsprozess-modus` | Aktenauszug für VwGO-Verfahren erstellen: Anfechtungs- Verpflichtungsklage Berufung § 124 VwGO Revision § 132 VwGO Eilrechtsschutz §§ 80 123 VwGO. Normen VwGO §§ 40 42 80 113 124 132. Prüfraster VwGO-spezifische… |
| `zivilprozess-modus` | Aktenauszug für ZPO-Verfahren erstellen: ordentliche Klage muendliche Verhandlung Berufung §§ 511 ff. ZPO Revision §§ 542 ff. ZPO einstweilige Verfuegung §§ 935 ff. ZPO. Normen ZPO BGH-Leitsaetze. Prüfraster… |

## Worum geht es?

Das Plugin ermoeglicht Anwaelten und Paralegals die schnelle, strukturierte Einarbeitung in deutsche Gerichtsverfahren aller Verfahrensordnungen. Es teilt die Aktenzusammenfassung in sechs klar definierte Bausteine auf: Verfahrensidentifikation mit Stammdaten, praegnanter Einleitungssatz, Zusammenfassungsabsatz, Sachverhaltschronologie, Verfahrenschronologie und tabellarische Gegenueberstellung von Parteivortraegen sowie Beweismitteln und Rechtsargumenten.

Das Ergebnis ist ein Markdown-Aktenauszug in juristisch neutraler Sprache ohne Erfolgsprogosen, der als Grundlage fuer Beratungsgespraeche, Schriftsaetze oder die Vorbereitung muendlicher Verhandlungen dient. Spezifische Modi fuer ZPO-, ArbGG-, SGG-, VwGO- und StPO-Verfahren decken die verfahrensordnungsrelevanten Besonderheiten ab.

## Wann brauchen Sie diese Skill?

- Sie uebernehmen ein laufendes Mandat und muessen sich ohne vollstaendige Aktenlektuere schnell orientieren.
- Eine neue Kollegin tritt die Vertretung an und braucht eine neutrale Zusammenfassung des Verfahrensstands.
- Sie moechten Beweismittel und Rechtsargumente beider Seiten strukturiert gegenueberstellen fuer die Vorbereitung der muendlichen Verhandlung.
- Fristen aus Schriftsaetzen, Beschluessen oder Urteilen muessen systematisch hervorgehoben werden.
- Sie erstellen ein Anlagenverzeichnis fuer alle Partei-Anlagen aus einer umfangreichen Akte.

## Fachbegriffe (kurz erklaert)

- **Aktenauszug** — Strukturierte Zusammenfassung eines Gerichtsverfahrens aus den vorliegenden Schriftsaetzen und Gerichtsdokumenten.
- **Verfahrensidentifikation** — Erfassung aller Stammdaten: Gericht, Kammer, Aktenzeichen, Streitwert, Parteien und Prozessbevollmaechtigte.
- **Sachverhaltschronologie** — Chronologische Bullet-Liste ausserprozessualer Tatsachen ohne Wertung.
- **Verfahrenschronologie** — Chronologische Auflistung aller prozessualen Schritte mit hervorgehobenen Fristen.
- **Parteivortrag-Gegenueberstellung** — Zweispaltige Tabelle mit streitigen Sachverhaltsangaben je Partei.
- **Neutralitaetspruefung** — Sicherheitsgate zur Entfernung unzulaessiger Wertungen und Erfolgsprognosen aus dem Auszug.
- **Anlagenverzeichnis** — Vollstaendige Liste aller Anlagen (K-, B-, AST-, AG-Verweise) mit Partei und Fundstelle.
- **Stilrichtlinie** — Verbindliche Sprachregelung fuer juristisch saubere, neutrale Aktenauszuege.

## Rechtsgrundlagen

- §§ 128-134 ZPO — Muendliche Verhandlung und Schriftsatz
- §§ 130 131 ZPO — Inhalt und Anlagen des Schriftsatzes
- §§ 253 261 ZPO — Klageerhebung und Verfahrensstammdaten
- §§ 222 517 520 ZPO — Fristberechnung, Berufungsfrist, Begruendungsfrist
- ArbGG §§ 2 54 64 72 — Arbeitsgerichtsverfahren und Rechtsmittel
- SGG §§ 51 77 86b 143 — Sozialgerichtsverfahren
- VwGO §§ 40 42 80 113 124 132 — Verwaltungsprozess
- StPO §§ 200 203 333 359 — Strafprozess und Rechtsmittel
- § 4 KSchG — Kuendigungsschutzklage: Dreiwochenfrist

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Verfahrensordnung und -art bestimmen (ZPO, ArbGG, SGG, VwGO, StPO) und passenden Modus auswaehlen.
2. Verfahrensidentifikation: alle Stammdaten und Beteiligte erfassen.
3. Einleitungssatz und Zusammenfassungsabsatz generieren.
4. Sachverhalts- und Verfahrenschronologie erstellen; Fristen hervorheben.
5. Parteivortrag, Beweismittel und Rechtsargumente gegenueberstellen; Neutralitaet pruefen.

## Skill-Tour (was gibt es hier?)

- `aktenauszug-erstellen` — Vollstaendigen Aktenauszug in allen sechs Bausteinen aus Gerichtsakte oder Schriftsaetzen erstellen.
- `aktenauszug-strukturpruefung` — Fertig erstellten Aktenauszug auf Vollstaendigkeit, Fristen-Markierung und Neutralitaet pruefen.
- `anlagenverzeichnis-extrakt` — Alle Anlagen-Verweise (K-, B-, AST-, AG-) aus der Akte extrahieren und Anlagenverzeichnis erstellen.
- `anwaltsschriftsatz-stilrichtlinie` — Verbindliche Stilregeln fuer neutralen, juristisch sauberen Aktenauszug anwenden.
- `arbeitsgerichtsverfahren-modus` — Aktenauszug fuer ArbGG-Verfahren mit KSchG-Fristen und ArbGG-Besonderheiten erstellen.
- `beweismittel-gegenueberstellung` — Beweisangebote aller Parteien (Zeugen, Urkunden, Sachverstaendige) tabellarisch gegenueberstellen.
- `einleitungssatz-generator` — Praegnanten Einleitungssatz generieren: wer streitet mit wem worueber nach welcher Hauptnorm.
- `fristen-und-terminkalender` — Prozessuale Fristen und Termine hervorheben und Fristen-Box erstellen.
- `neutralitaetspruefung` — Aktenauszug auf unzulaessige Wertungen und Erfolgsprognosen pruefen und neutralisieren.
- `parteivortrag-gegenueberstellung` — Zweispaltige Tabelle streitiger Sachverhaltsangaben Klaeger vs. Beklagte erstellen.
- `rechtsargumente-gegenueberstellung` — Tabellarische Gegenueberstellung der Rechtsargumente beider Parteien mit Normfundstellen.
- `sachverhaltschronologie` — Chronologische Bullet-Liste ausserprozessualer Tatsachen ohne Wertung erstellen.
- `schwerpunktthemen-identifikation` — Drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Fundstellen identifizieren.
- `sozialgerichtsverfahren-modus` — Aktenauszug fuer SGG-Verfahren mit Vorverfahrens-Pruefung und Leistungsarten erstellen.
- `strafprozess-modus` — Aktenauszug fuer StPO-Verfahren mit Anklageschrift, Hauptverhandlung und Rechtsmitteln erstellen.
- `verfahrenschronologie` — Chronologische Liste aller prozessualen Schritte mit hervorgehobenen kritischen Fristen.
- `verfahrensidentifikation` — Alle Verfahrensstammdaten strukturiert erfassen: Gericht, Kammer, Aktenzeichen, Parteien.
- `verfahrenszusammenfassung-absatz` — Acht bis zehn Saetze Hintergrund, Streitstand und anstehende Verfahrenshandlungen.
- `verwaltungsprozess-modus` — Aktenauszug fuer VwGO-Verfahren mit Vorverfahren und Widerspruchsbescheid erstellen.
- `zivilprozess-modus` — Aktenauszug fuer ZPO-Verfahren mit Berufung, Revision und einstweiliger Verfuegung erstellen.

## Worauf besonders achten

- **Neutralitaet strikt einhalten**: Ein Aktenauszug enthaelt keine Erfolgsprognose und keine Bewertung, welcher Vortrag zutrifft; Verstoss untergraebt die Verwendbarkeit.
- **Fristen immer optisch hervorheben**: Eine uebersehene Berufungsfrist kann das Mandat kosten; der Fristen-und-Terminkalender-Skill ist Pflichtschritt.
- **Modus korrekt auswaehlen**: ArbGG, SGG, VwGO und StPO haben eigene Fristen und Besonderheiten, die der jeweilige Modus-Skill abdeckt.
- **Anlagenverzeichnis vollstaendig fuehren**: Fehlende Anlagen koennen in der Verhandlung nicht nachgereicht werden ohne Fristrisiko.
- **Stilrichtlinie fuer alle Bausteine verbindlich**: Unterschiedliche Sprachstile in verschiedenen Bausteinen zerstoeren die Lesbarkeit des Auszugs.

## Typische Fehler

- Zusammenfassungsabsatz statt vollstaendigem Aktenauszug verwenden: Luecken in Sachverhalt und Beweismitteln bleiben unentdeckt.
- Parteivortraege ohne Fundstellen aus Schriftsaetzen eintragen: Pruefbarkeit entfaellt.
- Einleitungssatz mit Erfolgsprognose formulieren; verfaelscht den Charakter des neutralen Auszugs.
- Verfahrensordnung falsch eingestuft; ZPO-Fristen bei ArbGG-Verfahren angewendet.
- Neutralitaetspruefung als letzten Schritt weglassen; Wertungen aus frueheren Entwurfsrunden bleiben stehen.

## Querverweise

- `kanzlei-allgemein` — Fuer Fristen, Postlauf und Schriftsatzerstellung nach dem Aktenauszug.
- `selbstvertreter-amtsgericht` — Wenn Buerger ohne Anwalt den Aktenauszug als Orientierungshilfe nutzen.
- `tabellenreview-3d` — Wenn mehrere Verfahrensakten gleichzeitig geprueft werden sollen.
- `insolvenzverwaltung` — Bei Insolvenzverfahren mit umfangreicher Verfahrensakte.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- § 23 Nr. 1 GVG: Wertgrenze AG 10.000 EUR seit 01.01.2026
