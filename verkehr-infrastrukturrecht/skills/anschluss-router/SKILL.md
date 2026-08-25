---
name: anschluss-router
description: "Wenn es um Verkehrs- und Infrastrukturrecht — Allgemein in Verkehrs- und Infrastrukturrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

# Verkehrs- und Infrastrukturrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: VwVfG § 73 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist, VwGO § 47 Normenkontrolle 1 Jahr, BVerwGO § 50 Abs. 1 Nr. 6 erstinstanzliche Zuständigkeit BVerwG.
- Tragende Normen verifizieren: FStrG, BWaStrG, AEG, BImSchG, UVPG, ROG, BauGB §§ 38, 246, VwVfG §§ 72-78 (Planfeststellung), VwGO §§ 47 ff., BNatSchG §§ 14, 15, 34, 44, WHG §§ 8, 67, EU-FFH-RL, UmwRG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger (Bund, Land, DB Netz, Autobahn GmbH), Planfeststellungsbehörde, Anhörungsbehörde, anerkannte Umweltvereinigungen (BUND, NABU), VG, OVG, BVerwG (1. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Planfeststellungsbeschluss, Erörterungsprotokoll, UVP-Bericht, FFH-Verträglichkeitsstudie, Einwendung, Klage zum BVerwG, Erlaubnis nach § 67 WHG — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verkehr Infrastrukturrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende.

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

Das Plugin begleitet rechtliche Fragestellungen rund um Verkehrsplanung und Infrastrukturprojekte auf kommunaler und ueberregionaler Ebene. Es deckt das gesamte Spektrum vom Planfeststellungsverfahren für Strassenbau und Schienenstrecken über Ladeinfrastruktur für Elektromobilitaet bis hin zu Parkraumbewirtschaftung, Sondernutzung öffentlicher Strassenflaechen und Schulwegsicherheit ab.

Zielgruppe sind Verwaltungsjuristen, Kommunalrechtler, Anwaelte von Verkehrstragern und OEPNV-Betreibern sowie Unternehmen, die Foerdergelder oder Vergabe-Auftraege im Infrastrukturbereich benoetigen. Das Plugin unterstuetzt sowohl die angreifende als auch die verteidigenden Seite bei Planfeststellung und Verwaltungsstreitverfahren.

## Wann brauchen Sie diese Skill?

- Vorhabentraeger oder Behörde leitet ein Planfeststellungsverfahren für Strassenneubau, Schieneninfrastruktur oder OEPNV ein und braucht verfahrensrechtliche Begleitung.
- Betreiber plant Ladepunkte für Elektrofahrzeuge und muss Netzanschluss, Förderungsantrag und Genehmigungsrecht klären.
- Kommune fuehrt Bewohnerparkausweis oder Tempo-30-Zone ein und muss Rechtmaessigkeit und Anfechtungsrisiken beachten.
- Unternehmen beantragt Sondernutzungserlaubnis für Aussengastronomie, Lieferzone oder Baustelle im öffentlichen Strassenraum.
- OEPNV-Betreiber oder Gemeinde will Strassenbahnlinie errichten oder Konzession verteidigen.

## Fachbegriffe (kurz erklaert)

- **Planfeststellung** — Foermliches Verwaltungsverfahren nach §§ 72 ff. VwVfG, das Bau und Betrieb von Infrastrukturanlagen konzentriert genehmigt und private Einwendungen ausschliessen kann.
- **GVFG** — Gemeindeverkehrsfinanzierungsgesetz; Bundesfoerderung für kommunale Strassenbahnprojekte und OEPNV-Infrastruktur.
- **Sondernutzung** — Nutzung öffentlicher Strassen, die über den Gemeingebrauch hinausgeht (z.B. Werbeanlagen, Aussengastronomie, Baustellenflaeche) und einer besonderen Erlaubnis bedarf.
- **Planungshoheit** — Kommunale Selbstverwaltungsrecht bei der Bauleit- und Verkehrsplanung (Art. 28 Abs. 2 GG).
- **Konzession (PBefG)** — Genehmigung zum Betrieb von Strassenbahnlinien nach dem Personenbefoerderungsgesetz.
- **Verkehrswende** — Stadtplanerische und rechtliche Maßnahmen zur Förderung umweltfreundlicher Mobilitaet (Fussgaengerzonen, Radwege, Tempo-30-Zonen).
- **Schulwegsicherung** — Amtspflichten der Gemeinde und des Strassenverkehrsrechts zum Schutz von Schulkindern im Strassenverkehr; relevant für Amtshaftung.

## Rechtsgrundlagen

- §§ 72 ff. VwVfG — Planfeststellungsverfahren
- FStrG, StrWG der Länder — Bundesfernstrassenrecht und Landesstrassenrecht
- PBefG — Personenbefoerderungsgesetz (Strassenbahn, Linienverkehr)
- BNatSchG — Naturschutz bei Infrastrukturvorhaben
- GVFG — Gemeindeverkehrsfinanzierungsgesetz
- § 45 StVO — Verkehrsbeschraenkungen (Tempo-30, Spielstrasse)
- VwGO — Verwaltungsgerichtliche Verfahren, Eilrechtsschutz

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Vorhabentraeger, Behörde, Anlieger oder Verband?
2. Phase des Mandats bestimmen: Planungsphase, Genehmigungsverfahren, Foerderantrag oder Streitverfahren?
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen prüfen: Widerspruchs- und Klagefrist gegen Planfeststellungsbeschluss (§ 74 VwVfG, §§ 70 74 VwGO).
5. Anschluss-Skill bestimmen: Nach Genehmigungsverfahren ggf. Foerderantrag oder Vergabe prüfen.

## Skill-Tour (was gibt es hier?)

- `verkehr-infrastrukturrecht-kommandocenter` — Zentrales Steuerungsmodul für neue Verkehrsinfrastruktur-Mandate mit Routing auf passende Skills.
- `verkehr-infrastrukturrecht-planfeststellung` — Planfeststellungsverfahren für Strassenbau, Schienenstrecken und OEPNV-Infrastruktur begleiten oder anfechten.
- `verkehr-infrastrukturrecht-strassenbahn` — Strassenbahn- und OEPNV-Infrastrukturrecht: Konzession, Planfeststellung, Linienplanung nach PBefG.
- `verkehr-infrastrukturrecht-ladeinfrastruktur` — Ladepunkte für Elektromobilitaet: Netzanschluss, Genehmigung und Foerderrecht.
- `verkehr-infrastrukturrecht-parkraumbewirtschaftung` — Bewohnerparkausweis, Abschleppanordnungen und kommunale Parkraummassnahmen rechtssicher gestalten und anfechten.
- `verkehr-infrastrukturrecht-foerderung-vergabe` — GVFG-Foerderantrag und Vergabeverfahren für Infrastrukturprojekte begleiten.
- `verkehr-infrastrukturrecht-sondernutzung` — Sondernutzungserlaubnis für Aussengastronomie, Werbeanlagen und Baustellenflaechen beantragen und anfechten.
- `verkehr-infrastrukturrecht-schulwegsicherheit` — Schulwegsicherung rechtlich verbessern; Amtshaftungsansprueche prüfen und geltend machen.
- `verkehr-infrastrukturrecht-verkehrsplanung` — Strassenverkehrs- und Radverkehrsplanung rechtlich begleiten; Beteiligungspflichten und Abwaegungsfehler.
- `verkehr-infrastrukturrecht-verkehrswende` — Fussgaengerzonen, Tempo-30-Zonen und Radverkehrsfoerderung rechtssicher gestalten.
- `verkehr-infrastrukturrecht-verfahren` — Anhörung, Widerspruch, Klage und Eilverfahren im Verkehrsinfrastrukturrecht vorbereiten.
- `verkehr-infrastrukturrecht-wirtschaftsverkehr` — Lieferzonen, Wirtschaftsverkehrskonzepte und Logistikrecht im staedtischen Raum.

## Worauf besonders achten

- Planfeststellungsbeschluesse werden bestandskraeftig, wenn keine rechtzeitige Klage erhoben wird; Klagefrist beachten (§ 74 Abs. 1 VwVfG i.V.m. VwGO).
- Einwendungsausschluss (§ 73 Abs. 4 VwVfG): Wer im Anhörungsverfahren keine Einwendungen erhebt, verliert Klagebefugnis für diese Punkte.
- GVFG-Foerderantraege erfordern fruehzeitige Abstimmung mit Behörden; spaetere Änderungen am Vorhaben können Foerderausschluss ausloesen.
- Vergaberechtliche Anforderungen gelten ab definierten Schwellenwerten (EU-Schwellenwerte nach VgV); Unterschwellenverfahren unterliegen den Landesvergabeordnungen.
- Verkehrswende-Maßnahmen (Sperrungen, Geschwindigkeitsbeschraenkungen) müssen auf § 45 StVO gestuetzt sein; fehlerhafte Begruendung macht Anordnung angreifbar.

## Typische Fehler

- Einwendungsfrist im Planfeststellungsverfahren versaeumt: Nach Ablauf ist Einwendungsausschluss bindend.
- Foerderantrag zu spaet gestellt: GVFG-Mittel werden jedes Haushaltsjahr kontingentiert; verspaetest gestellte Antraege gehen leer aus.
- Konzessionspflicht uebersehen: Linienbusverkehr und Strassenbahn beduerften zwingend PBefG-Genehmigung; Betrieb ohne Konzession ist Ordnungswidrigkeit.
- Sondernutzungsgebueher nicht einkalkuliert: Kommunale Sondernutzungssatzungen erheben Gebühren; fehlende Berechnungsgrundlage fuehrt zu Nachforderungen.
- Amtshaftungsansprueche bei Schulwegsicherung versaeumen: Dreijaehrige Verjaeehrungsfrist nach § 195 BGB ab Kenntnis des Schadens.

## Quellen und Aktualitaet

- Stand: 05/2026
- VwVfG, FStrG, PBefG, StVO, GVFG in aktuell geltender Fassung
- EU-Schwellenwerte nach VgV/SektVO gemäß aktueller EU-Kommissions-Verordnung
