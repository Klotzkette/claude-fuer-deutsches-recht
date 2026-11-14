---
name: start-chronologie-fristen
description: "Für Zwangsvollstreckung — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
---

# Zwangsvollstreckung — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 704 ff. ZPO; § 802l Kontensuche, Vermögensauskunft, Räumung; § 800 ZPO Notar; § 201 InsO, ZVG, EU-Kontenpfändung VO 655; § 765a Härtefall, Schuldnerschutz — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Zwangsvollstreckung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für die Zwangsvollstreckung nach §§ 704 ff. ZPO aus allen Titelarten: Mahn-/Vollstreckungsbescheid online, PfÜB Bank/Arbeitgeber, Kontensuche § 802l ZPO, Vermögensauskunft, Räumung, notarielle Urkunde § 800 ZPO, Insolvenztabelle § 201 InsO, ZVG-Antrag und Schuldnerschutz.

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

Das Plugin begleitet die Zwangsvollstreckung aus der Perspektive beider Seiten: Gläubiger, die einen vorhandenen Titel vollstrecken wollen, und Schuldner, die sich gegen Vollstreckungsmassnahmen wehren. Es deckt das gesamte Spektrum der §§ 704 ff. ZPO ab: vom Mahnbescheid und Vollstreckungsbescheid über Pfaendungs- und Uebertragungsbeschluesse (PfUeB) bei Bankkonten und Arbeitseinkommen bis zur Raeumungsvollstreckung und zum ZVG-Antrag bei Immobilien.

Einbezogen sind auch EU-grenzueberschreitende Maßnahmen (EuKtPVO) und der Schuldnerschutz nach § 765a ZPO sowie § 802l-Kontensuche. Zielgruppe sind Anwaelte, Inkassobetriebe und Rechtspfleger.

## Wann brauchen Sie diese Skill?

- Gläubiger hat rechtskraeftiges Urteil oder anderen vollstreckbaren Titel und muss entscheiden, welche Vollstreckungsart am sinnvollsten ist.
- Gläubiger kennt weder Konto noch Arbeitgeber des Schuldners und muss Vermögensauskunft oder Drittauskunft beantragen.
- Schuldner hat unrechtmäßigen PfUeB erhalten oder ist besonders schutzbeduerftig (Krankheit, Suizidrisiko) und will Vollstreckungsschutz.
- Vermieter hat rechtskraeftiges Raeumungsurteil und muss Gerichtsvollzieher beauftragen.
- Gläubiger will Immobilie des Schuldners versteigern lassen (ZVG-Antrag).

## Fachbegriffe (kurz erklaert)

- **Vollstreckbarer Titel (§ 704 ZPO)** — Grundlage jeder Zwangsvollstreckung; typisch: Urteil, Vollstreckungsbescheid, notarielle Urkunde.
- **Vollstreckungsklausel (§ 724 ZPO)** — Formale Bescheinigung auf dem Titel, die Vollstreckbarkeit bestaetigt.
- **PfUeB** — Pfaendungs- und Uebertragungsbeschluss; richterlicher Beschluss, der Forderung des Schuldners gegenueber Drittschuldner pfaendet.
- **P-Konto** — Pfaendungsschutzkonto; schuetzt Existenzminimum des Schuldners bei Kontopfaendung (§ 850k ZPO).
- **Pfaendungsfreigrenze (§ 850c ZPO)** — Betrag des Arbeitseinkommens, der pfaendungsfrei bleibt; Pfaendungstabelle wird regelmaessig angepasst.
- **Vermögensauskunft (§ 802c ZPO)** — Pflicht des Schuldners, vollstaendiges Vermögen zu offenbaren; frueherer Name: Eidesstattliche Versicherung.
- **ZVG** — Zwangsversteigerungsgesetz; Grundlage für Immobilienvollstreckung durch Versteigerung.
- **EuKtPVO** — EU-Kontenpfaendungsverordnung (VO 655/2014); ermoeglicht vorläufige Kontenpfaendung in EU-Mitgliedstaaten.

## Rechtsgrundlagen

- §§ 704 ff. ZPO — Allgemeine Voraussetzungen der Zwangsvollstreckung
- §§ 724 726 ZPO — Vollstreckungsklausel und Zustellung
- §§ 688 ff. ZPO — Mahnverfahren, Vollstreckungsbescheid
- §§ 808 ff. ZPO — Sachpfaendung (Mobiliarpfaendung)
- §§ 829 835 850 ff. ZPO — Forderungspfaendung, Lohn- und Kontopfaendung
- § 850k ZPO — Pfaendungsschutzkonto
- § 802c ff. ZPO — Vermögensauskunft, § 802l Drittauskunft
- § 765a ZPO — Vollstreckungsschutz in Haertefall
- § 885 ZPO — Raeumungsvollstreckung
- ZVG — Zwangsversteigerung und Zwangsverwaltung
- VO (EU) 655/2014 (EuKtPVO) — EU-Kontenpfaendung
- § 201 InsO — Vollstreckung aus Tabellenauszug nach Insolvenz

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Gläubiger-Seite (Vollstreckung einleiten) oder Schuldner-Seite (Vollstreckung abwehren)?
2. Titelstatus prüfen: Liegt ein vollstreckbarer Titel mit Klausel und Zustellung vor (§§ 704, 724, 750 ZPO)?
3. Zielobjekt bestimmen: Bankkonto, Arbeitseinkommen, Mobiliarsachen, Immobilie oder sonstige Forderung?
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Eilfristen prüfen: Haertefall-Antrag nach § 765a ZPO sofort bei Vollstreckungstermin; EU-Kontenpfaendung hat eigene Fristen.

## Skill-Tour (was gibt es hier?)

- `kommandocenter` — Routing: Welche Vollstreckungsart ist im konkreten Fall am sinnvollsten? Überblick und Weiterleitung.
- `mahnbescheid-online-mobiliar-gv` — Mahnbescheid online beantragen und Vollstreckungsbescheid erwaerken nach §§ 688 ff. ZPO.
- `vollstreckungsbescheid-zv` — Nach Mahnbescheid: Vollstreckungsbescheid beantragen oder auf Widerspruch reagieren.
- `titel-klausel-zustellung` — Formale Trias prüfen: vollstreckbarer Titel, Vollstreckungsklausel, Zustellung an Schuldner.
- `pfueb-bank` — PfUeB für Bankkonto beantragen; Drittschuldner-Erklarung, P-Konto-Schutz.
- `pfueb-arbeitsentgelt` — PfUeB für Arbeitseinkommen; Pfaendungsfreigrenze nach § 850c ZPO berechnen.
- `pfueb-802l-arbeit` — PfUeB für Mietforderung, Steuererstattung oder sonstige Drittschuldner-Forderung.
- `pfaendungstabelle-pfueb-arbeitsentgelt` — Pfaendungsfreien Betrag nach aktueller Pfaendungstabelle (Stand 2025) konkret berechnen.
- `kontensuche-drittschuldner` — § 802l-Kontensuche und Drittauskunft wenn Konto oder Arbeitgeber des Schuldners unbekannt sind.
- `vermoegensauskunft-gv` — Vermögensauskunft nach § 802c ZPO durch Gerichtsvollzieher beantragen.
- `mobiliar-gv-auftrag` — Gerichtsvollzieher mit Sachpfaendung beweglicher Gegenstaende beauftragen (§§ 808 ff. ZPO).
- `raeumung-tabellenauszug-inso` — Räumungsvollstreckung nach Paragraf 885 ZPO; Gerichtsvollzieherauftrag und beschränkte Räumung nach Paragraf 885a ZPO.
- `notarielle-urkunde-grundschuld` — Vollstreckung aus notarieller Grundschuld-Urkunde nach § 794 Abs. 1 Nr. 5 ZPO.
- `zvg-antrag-glaeubiger` — ZVG-Antrag auf Zwangsversteigerung oder Zwangsverwaltung bei Immobilien.
- `tabellenauszug-201-inso` — Vollstreckung aus Insolvenz-Tabellenauszug nach § 201 InsO nach Verfahrensende.
- `eu-kontenpfaendung-655-2014` — Vorlaeufige EU-Kontenpfaendung nach EuKtPVO bei EU-Auslandskonto des Schuldners.
- `vollstreckungsschutz-haertefall-765a` — Haertefall-Schutzantrag für besonders schutzbeduerftige Schuldner nach § 765a ZPO.
- `abwehr-schuldner` — Schuldner-Abwehrmassnahmen: sofortige Beschwerde, Vollstreckungserinnerung, Haertefall, P-Konto.
- `elektronische-zustellung-eu` — Digitalisierung der Zwangsvollstreckung ab 2026/2027: neue Pflichten und Verfahren.

## Worauf besonders achten

- Formale Trias ist zwingend: Titel, Klausel und Zustellung müssen vollstaendig vorliegen, bevor Vollstreckung beginnt (§ 750 ZPO).
- P-Konto-Schutz gilt automatisch, wenn Schuldner P-Konto eingerichtet hat; Gläubiger muss Freibetrag-Erhoehung separat anfechten.
- Pfaendungsfreigrenzen werden jaehrlich angepasst (§ 850c ZPO); immer aktuelle Tabelle verwenden.
- EU-Kontenpfaendung nach EuKtPVO setzt Zuständigkeit eines deutschen Gerichts voraus; Antrag hat eigene Formalien.
- Haertefall-Antrag nach § 765a ZPO hemmt Vollstreckung nur bei sofortiger Antragstellung vor dem Vollstreckungstermin.

## Typische Fehler

- Vollstreckung ohne Zustellung an Schuldner begonnen: § 750 ZPO erfordert vorherige oder gleichzeitige Zustellung; fehlende Zustellung macht Vollstreckungsmassnahme anfechtbar.
- Pfaendungsfreigrenze falsch berechnet: Falsche Steuerklasse oder Unterhaltspflichten nicht beruecksichtigt; Schuldner kann Erinnerung einlegen.
- Gerichtsvollzieher-Auftrag zu spaet gestellt: Mobiliarsachen können veraessert oder abhandengekommen sein.
- Verjährung des Titels uebersehen: Vollstreckungsverjaeaehrung nach § 197 BGB betraegt 30 Jahre ab Urteil; Mahnbescheide können kuerzere Fristen haben.
- EU-Kontenpfaendung ohne Zuständigkeitspruefung: Deutsche Gerichte sind nur zuständig wenn Deutschland Vollstreckungsmitgliedstaat ist.

## Quellen und Aktualitaet

- Stand: 05/2026
- ZPO, ZVG, InsO in aktuell geltender Fassung
- Pfändungsfreigrenzenbekanntmachung 2026 vom 19. März 2026 (BGBl. 2026 I Nr. 80), gültig vom 1. Juli 2026 bis 30. Juni 2027. Amtliche Quelle: https://www.gesetze-im-internet.de/pf_ndfreigrbek_2026/
- Justizstandort-Staerkungsgesetz (BGBl. 2025 I Nr. 318 vom 11.12.2025): ab 01.01.2026 Amtsgerichts-Zuständigkeit bis 10.000 EUR (§ 23 GVG n.F.), Berufungssumme 1.000 EUR (§ 511 Abs. 2 ZPO n.F.); Uebergangsvorschrift § 47 EGZPO.
- EuKtPVO (VO 655/2014) unmittelbar anwendbar.
