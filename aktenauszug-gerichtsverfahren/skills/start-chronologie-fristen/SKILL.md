---
name: start-chronologie-fristen
description: "Für Aktenauszug Gerichtsverfahren — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
---

# Aktenauszug Gerichtsverfahren — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Aktenauszug Gerichtsverfahren**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivortraege Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten.

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
4. **Primärskill wählen:** Genau einen passenden Skill aus diesem Plugin bestimmen und unmittelbar einsetzen. Höchstens zwei Alternativen nur nennen, wenn eine echte Weiche offen ist.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
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

### 5. Fachmodule gezielt und sparsam laden

1. Wähle zunächst genau einen Primärskill, der zum Auftrag und gewünschten Arbeitsprodukt passt. Weitere Skills kommen nur bei einer konkreten Schnittstelle hinzu.
2. Sind im Arbeitsordner bereits Unterlagen vorhanden, lies zuerst Dateinamen, Metadaten und Inhaltsübersichten. Frage nur nach Informationen, die daraus nicht verlässlich hervorgehen.
3. Grenze Suchen in Microsoft 365 nach Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und prägnantem Suchbegriff ein. Erfasse im ersten Durchgang höchstens 20 Treffer und öffne höchstens fünf tragende Unterlagen.
4. Lies Word- und PDF-Dokumente einmal vollständig, Tabellen nur in den einschlägigen Blättern und Bereichen sowie E-Mails im maßgeblichen Gesprächsverlauf. Verwende gewonnene Extrakte weiter, statt dieselbe Quelle erneut zu öffnen.
5. Die [vollständige Fachmodulkarte](references/fachmodule.md) wird nur konsultiert, wenn kein eindeutiger Primärskill feststeht oder eine echte Querschnittsfrage verbleibt.

## Worum geht es?

Das Plugin ermoeglicht Anwaelten und Paralegals die schnelle, strukturierte Einarbeitung in deutsche Gerichtsverfahren aller Verfahrensordnungen. Es teilt die Aktenzusammenfassung in sechs klar definierte Bausteine auf: Verfahrensidentifikation mit Stammdaten, praegnanter Einleitungssatz, Zusammenfassungsabsatz, Sachverhaltschronologie, Verfahrenschronologie und tabellarische Gegenueberstellung von Parteivortraegen sowie Beweismitteln und Rechtsargumenten.

Das Ergebnis ist ein Markdown-Aktenauszug in juristisch neutraler Sprache ohne Erfolgsprogosen, der als Grundlage für Beratungsgespraeche, Schriftsaetze oder die Vorbereitung muendlicher Verhandlungen dient. Spezifische Modi für ZPO-, ArbGG-, SGG-, VwGO- und StPO-Verfahren decken die verfahrensordnungsrelevanten Besonderheiten ab.

## Wann brauchen Sie diese Skill?

- Sie uebernehmen ein laufendes Mandat und müssen sich ohne vollstaendige Aktenlektuere schnell orientieren.
- Eine neue Kollegin tritt die Vertretung an und braucht eine neutrale Zusammenfassung des Verfahrensstands.
- Sie moechten Beweismittel und Rechtsargumente beider Seiten strukturiert gegenueberstellen für die Vorbereitung der muendlichen Verhandlung.
- Fristen aus Schriftsaetzen, Beschluessen oder Urteilen müssen systematisch hervorgehoben werden.
- Sie erstellen ein Anlagenverzeichnis für alle Partei-Anlagen aus einer umfangreichen Akte.

## Fachbegriffe (kurz erklaert)

- **Aktenauszug** — Strukturierte Zusammenfassung eines Gerichtsverfahrens aus den vorliegenden Schriftsaetzen und Gerichtsdokumenten.
- **Verfahrensidentifikation** — Erfassung aller Stammdaten: Gericht, Kammer, Aktenzeichen, Streitwert, Parteien und Prozessbevollmaechtigte.
- **Sachverhaltschronologie** — Chronologische Bullet-Liste ausserprozessualer Tatsachen ohne Wertung.
- **Verfahrenschronologie** — Chronologische Auflistung aller prozessualen Schritte mit hervorgehobenen Fristen.
- **Parteivortrag-Gegenueberstellung** — Zweispaltige Tabelle mit streitigen Sachverhaltsangaben je Partei.
- **Neutralitaetspruefung** — Sicherheitsgate zur Entfernung unzulaessiger Wertungen und Erfolgsprognosen aus dem Auszug.
- **Anlagenverzeichnis** — Vollstaendige Liste aller Anlagen (K-, B-, AST-, AG-Verweise) mit Partei und Fundstelle.
- **Stilrichtlinie** — Verbindliche Sprachregelung für juristisch saubere, neutrale Aktenauszuege.

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

## Schritt-für-Schritt: Einstieg ins Plugin

1. Verfahrensordnung und -art bestimmen (ZPO, ArbGG, SGG, VwGO, StPO) und passenden Modus auswaehlen.
2. Verfahrensidentifikation: alle Stammdaten und Beteiligte erfassen.
3. Einleitungssatz und Zusammenfassungsabsatz generieren.
4. Sachverhalts- und Verfahrenschronologie erstellen; Fristen hervorheben.
5. Parteivortrag, Beweismittel und Rechtsargumente gegenueberstellen; Neutralitaet prüfen.

## Skill-Tour (was gibt es hier?)

- `aktenauszug-erstellen` — Vollstaendigen Aktenauszug in allen sechs Bausteinen aus Gerichtsakte oder Schriftsaetzen erstellen.
- `aktenauszug-strukturpruefung` — Fertig erstellten Aktenauszug auf Vollstaendigkeit, Fristen-Markierung und Neutralitaet prüfen.
- `anlagenverzeichnis-extrakt` — Alle Anlagen-Verweise (K-, B-, AST-, AG-) aus der Akte extrahieren und Anlagenverzeichnis erstellen.
- `anwaltsschriftsatz-stilrichtlinie` — Verbindliche Stilregeln für neutralen, juristisch sauberen Aktenauszug anwenden.
- `arbeitsgerichtsverfahren-modus` — Aktenauszug für ArbGG-Verfahren mit KSchG-Fristen und ArbGG-Besonderheiten erstellen.
- `beweismittel-gegenueberstellung` — Beweisangebote aller Parteien (Zeugen, Urkunden, Sachverstaendige) tabellarisch gegenueberstellen.
- `einleitungssatz-generator` — Praegnanten Einleitungssatz generieren: wer streitet mit wem worueber nach welcher Hauptnorm.
- `fristen-und-terminkalender` — Prozessuale Fristen und Termine hervorheben und Fristen-Box erstellen.
- `neutralitaetspruefung` — Aktenauszug auf unzulaessige Wertungen und Erfolgsprognosen prüfen und neutralisieren.
- `parteivortrag-gegenueberstellung` — Zweispaltige Tabelle streitiger Sachverhaltsangaben Kläger vs. Beklagte erstellen.
- `rechtsargumente-gegenueberstellung` — Tabellarische Gegenueberstellung der Rechtsargumente beider Parteien mit Normfundstellen.
- `sachverhaltschronologie` — Chronologische Bullet-Liste ausserprozessualer Tatsachen ohne Wertung erstellen.
- `schwerpunktthemen-identifikation` — Drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Fundstellen identifizieren.
- `sozialgerichtsverfahren-modus` — Aktenauszug für SGG-Verfahren mit Vorverfahrens-Prüfung und Leistungsarten erstellen.
- `strafprozess-modus` — Aktenauszug für StPO-Verfahren mit Anklageschrift, Hauptverhandlung und Rechtsmitteln erstellen.
- `verfahrenschronologie` — Chronologische Liste aller prozessualen Schritte mit hervorgehobenen kritischen Fristen.
- `verfahrensidentifikation` — Alle Verfahrensstammdaten strukturiert erfassen: Gericht, Kammer, Aktenzeichen, Parteien.
- `verfahrenszusammenfassung-absatz` — Acht bis zehn Saetze Hintergrund, Streitstand und anstehende Verfahrenshandlungen.
- `verwaltungsprozess-modus` — Aktenauszug für VwGO-Verfahren mit Vorverfahren und Widerspruchsbescheid erstellen.
- `zivilprozess-modus` — Aktenauszug für ZPO-Verfahren mit Berufung, Revision und einstweiliger Verfuegung erstellen.

## Worauf besonders achten

- **Neutralitaet strikt einhalten**: Ein Aktenauszug enthaelt keine Erfolgsprognose und keine Bewertung, welcher Vortrag zutrifft; Verstoss untergraebt die Verwendbarkeit.
- **Fristen immer optisch hervorheben**: Eine uebersehene Berufungsfrist kann das Mandat kosten; der Fristen-und-Terminkalender-Skill ist Pflichtschritt.
- **Modus korrekt auswaehlen**: ArbGG, SGG, VwGO und StPO haben eigene Fristen und Besonderheiten, die der jeweilige Modus-Skill abdeckt.
- **Anlagenverzeichnis vollstaendig fuehren**: Fehlende Anlagen können in der Verhandlung nicht nachgereicht werden ohne Fristrisiko.
- **Stilrichtlinie für alle Bausteine verbindlich**: Unterschiedliche Sprachstile in verschiedenen Bausteinen zerstoeren die Lesbarkeit des Auszugs.

## Typische Fehler

- Zusammenfassungsabsatz statt vollstaendigem Aktenauszug verwenden: Luecken in Sachverhalt und Beweismitteln bleiben unentdeckt.
- Parteivortraege ohne Fundstellen aus Schriftsaetzen eintragen: Prüfbarkeit entfaellt.
- Einleitungssatz mit Erfolgsprognose formulieren; verfaelscht den Charakter des neutralen Auszugs.
- Verfahrensordnung falsch eingestuft; ZPO-Fristen bei ArbGG-Verfahren angewendet.
- Neutralitaetspruefung als letzten Schritt weglassen; Wertungen aus frueheren Entwurfsrunden bleiben stehen.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- § 23 Nr. 1 GVG: Wertgrenze AG 10.000 EUR seit 01.01.2026
