---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Regulatorisches Recht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Regulatorisches Recht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Regulatorisches Recht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest.

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
| `aufsichts-feed-monitor` | Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen für Mandanten identifizieren. KWG WpHG DORA VAG BaFin-Rundschreiben. Prüfraster: Relevanz für Mandant Umsetzungsfrist… |
| `dora-ikt-vertragspruefung` | IKT-Drittanbietervertraege auf DORA-Konformität prüfen wenn Finanzunternehmen digitale Dienstleistungen einkaufen. Art. 28 30 DORA VO (EU) 2022/2554. Prüfraster: Pflichtklauseln Art. 30 DORA Ausstiegsstrategien… |
| `inkasso-rdg` | Inkasso- und Rechtsdienstleistungserlaubnis nach RDG prüfen wenn gewerbliche Forderungseinziehung betrieben wird. §§ 2 10 RDG Rechtsdienstleistungserlaubnis. Prüfraster: Erlaubnispflicht Nebenleistungsprivileg… |
| `luecken` | Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren. KWG WpHG DORA VAG GwG. Prüfraster: Ist-Zustand Soll-Anforderungen Luecken Risikograd Priorisierung. Output: Lueckenliste mit… |
| `luecken-aufzeiger` | Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen. GG Art. 12 80 AEUV Art. 107. Prüfraster: Normtext Regelungsziele Luecken unbeabsichtigte Folgen… |
| `regulatorisches-recht-anpassen` | Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen. KWG WpHG DORA DSGVO GwG aktuelle BaFin-Vorgaben. Prüfraster: Bestandsdokument Neuregelung Delta-Analyse Anpassungsbedarf.… |
| `regulatorisches-recht-kaltstart-interview` | Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen. KWG WpHG DORA VAG GwG. Prüfraster: Branche Regulierungsrahmen Sachverhalt Fristen Pflichten Risiko. Output: Mandatssteckbrief Normenkarte… |
| `regulatorisches-recht-mandat-arbeitsbereich` | Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan… |
| `richtlinien-neufassung` | Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen. KWG WpHG DORA DSGVO GwG MaRisk. Prüfraster: regulatorische Anforderungen Inhaltsstruktur Formulierungsstandard Genehmigungsweg.… |
| `richtlinien-vergleich` | Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen. KWG WpHG DSGVO DORA GwG. Prüfraster: Strukturvergleich inhaltliche Unterschiede Aenderungshistorie Bedeutung der… |
| `stellungnahmen` | Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege… |
| `ustva` | Umsatzsteuervoranmeldung im regulatorischen Kontext prüfen wenn Finanzunternehmen oder regulierte Entitaeten USt-Fragen haben. §§ 14 14a 18 UStG Voranmeldungspflicht. Prüfraster: Voranmeldungspflicht Steuerklasse… |

## Worum geht es?

Dieses Plugin deckt das Aufsichtsrecht fuer regulierte Unternehmen ab — Banken, Zahlungsdienstleister, Wertpapierdienstleister, Energieversorger, Telekommunikationsunternehmen, Inkassodienstleister und weitere Sektoren. Es unterstuetzt bei Mandatsaufnahme, Richtlinienpflege, Regulierungsluecken-Analyse, Compliance-Dokumentation und Stellungnahmen gegenueber Behoerden.

Im Mittelpunkt stehen das Kreditwesengesetz (KWG), das Zahlungsdiensteaufsichtsgesetz (ZAG), das Wertpapierhandelsgesetz (WpHG), das Geldwaeschegesetz (GwG), die DORA-Verordnung, das EnWG und das TKG. Das Plugin eignet sich fuer Rechtsanwaelte, Compliance-Beauftragte und Unternehmensjuristen, die in regulierten Branchen beraten.

## Wann brauchen Sie diese Skill?

- Ein Finanzunternehmen muss pruefen, ob ein neues Geschaeftsmodell einer BaFin-Erlaubnis nach KWG oder ZAG bedarf.
- Eine Kanzlei bereitet eine Stellungnahme zu einem neuen Regulierungsvorhaben vor.
- Ein Unternehmen will interne Compliance-Richtlinien nach DORA, MaRisk oder WpHG aktualisieren.
- Ein Inkassounternehmen fragt, ob seine Taetigkeiten unter das RDG fallen.
- Ein reguliertes Unternehmen beobachtet neue BaFin- oder EBA-Veroeffentlichungen und will relevante Aenderungen schnell identifizieren.

## Fachbegriffe (kurz erklaert)

- **KWG** — Kreditwesengesetz; regelt die Zulassung und Beaufsichtigung von Kreditinstituten und Finanzdienstleistungsinstituten.
- **ZAG** — Zahlungsdiensteaufsichtsgesetz; setzt die PSD2-Richtlinie um und regelt Zahlungsinstitute.
- **WpHG** — Wertpapierhandelsgesetz; regelt Wohlverhaltenspflichten, Maerkte und Produktueberwachung.
- **DORA** — Digital Operational Resilience Act (EU-VO 2022/2554); Anforderungen an digitale Betriebsstabilitaet und IKT-Drittanbietervertraege fuer Finanzunternehmen.
- **MaRisk** — Mindestanforderungen an das Risikomanagement der BaFin; konkretisiert § 25a KWG.
- **RDG** — Rechtsdienstleistungsgesetz; regelt, wer aussergerichtliche Rechtsdienstleistungen erbringen darf, insbesondere Inkasso.
- **GwG** — Geldwaeschegesetz; Pflichten fuer Verpflichtete (Banken, Rechtsanwaelte, Immobilienmakler u. a.) zur Geldwaeschepraeventition.
- **BaFin** — Bundesanstalt fuer Finanzdienstleistungsaufsicht; zustaendige Behoerde fuer KWG, ZAG und WpHG.

## Rechtsgrundlagen

- § 1 KWG (Begriffsbestimmungen Bankgeschaefte und Finanzdienstleistungen)
- §§ 1 ff. ZAG (Zahlungsdienste, Erlaubnispflicht)
- §§ 63 ff. WpHG (Wohlverhaltenspflichten)
- §§ 1 ff. GwG (Verpflichtete, Sorgfaltspflichten)
- Art. 1 ff. DORA-VO EU 2022/2554 (IKT-Risikomanagement)
- §§ 2 ff. RDG (Zulaessige Rechtsdienstleistungen)
- § 25a KWG i. V. m. MaRisk (Risikomanagement)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Branche, Regulierungsrahmen und konkretes Rechtsproblem bestimmen.
2. Mandat strukturieren und Arbeitsbereich abgrenzen (Skill `regulatorisches-recht-kaltstart-interview` oder `regulatorisches-recht-mandat-arbeitsbereich`).
3. Passenden Fachskill auswaehlen (z. B. DORA, Inkasso, Richtlinien, Lueckenanalyse).
4. Eilfristen und Meldepflichten pruefen (Aufsichtsfristen koennen kurz sein).
5. Anschluss-Skill bestimmen (z. B. Richtlinie anpassen oder Stellungnahme verfassen).

## Skill-Tour (was gibt es hier?)

- `aufsichts-feed-monitor` — Aufsichtsbehoerden-Mitteilungen und regulatorische Feeds monitoren und relevante Aenderungen fuer Mandanten identifizieren.
- `dora-ikt-vertragspruefung` — IKT-Drittanbietervertraege auf DORA-Konformitaet pruefen fuer Finanzunternehmen, die digitale Dienstleistungen einkaufen.
- `inkasso-rdg` — Inkasso- und Rechtsdienstleistungserlaubnis nach RDG pruefen, wenn gewerbliche Forderungseinziehung betrieben wird.
- `luecken` — Regulatorische Luecken in bestehenden Compliance-Strukturen identifizieren (KWG, WpHG, DORA, VAG, GwG).
- `luecken-aufzeiger` — Regulatorische Luecken und Inkonsistenzen in Gesetzentwuerfen oder Regulierungsvorhaben aus Mandantensicht aufzeigen.
- `regulatorisches-recht-anpassen` — Bestehende Richtlinien oder Compliance-Dokumente an neue regulatorische Anforderungen anpassen.
- `regulatorisches-recht-kaltstart-interview` — Neues regulatorisches Mandat durch strukturiertes Erstgespraech aufnehmen.
- `regulatorisches-recht-mandat-arbeitsbereich` — Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen.
- `richtlinien-neufassung` — Interne Richtlinien und Unternehmensanweisungen auf regulatorischer Basis neu verfassen.
- `richtlinien-vergleich` — Zwei oder mehr Versionen regulatorischer Richtlinien vergleichen und Unterschiede darstellen.
- `stellungnahmen` — Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen.
- `ustva` — Umsatzsteuervoranmeldung im regulatorischen Kontext pruefen fuer Finanzunternehmen oder regulierte Entitaeten mit USt-Fragen.

## Worauf besonders achten

- Regulatorische Pflichten aendern sich haeufig: EBA-Guidelines, BaFin-Rundschreiben und neue EU-Verordnungen koennen Bestandsregelungen kurzfristig ueberlagern.
- KWG und ZAG-Erlaubnisse sind vorgelagert — kein Geschaeft ohne Erlaubnis starten.
- DORA gilt ab 17.01.2025 fuer alle in Art. 2 DORA genannten Finanzentitaeten; IKT-Drittanbietervertraege muessen nachgeruestet werden.
- Inkasso-Taetigkeiten ohne RDG-Registrierung sind strafbewehrt (§ 20 RDG).
- Sektorspezifische Normen (EnWG, TKG) haben eigene Aufsichtsstrukturen (BNetzA) neben BaFin — Zustaeindigkeit immer klaeren.

## Typische Fehler

- Erlaubnispflicht nach KWG oder ZAG uebersehen: Neue Geschaeftsmodelle (z. B. Krypto, Buy-now-pay-later) werden ohne Vorab-Pruefung gestartet.
- DORA nur als IT-Thema behandelt: Vertragliche Anforderungen an IKT-Drittanbieter werden von der Rechtsabteilung nicht koordiniert.
- Luecken in Compliance-Richtlinien nach Gesetzesaenderungen nicht nachgepflegt: Alte MaRisk-Version oder veraltete GwG-Interna bleiben im Einsatz.
- Fristen fuer Stellungnahmen zu Konsultationsverfahren verpasst: Europ. Behoerden (EBA, ESMA) setzen kurze Fristen.
- Inkasso und Rechtsberatung nicht sauber getrennt: RDG-Grenze wird ueberschritten.

## Querverweise

- `geldwaeschepraevention-aml-kyc` — GwG-Pflichten werden im spezialisierten AML/KYC-Plugin vertieft.
- `datenschutzrecht` — DSGVO-Anforderungen begleiten fast alle regulierten Sektoren.
- `energierecht` — EnWG-spezifische Regulierung bei Versorgern und Netzunternehmen.
- `vertragsrecht` — Vertragliche Grundlagen fuer IKT-Vertraege und Dienstleisterverhaeltnisse.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- DORA-VO EU 2022/2554 anwendbar ab 17.01.2025
- MaRisk-Novelle 2023 der BaFin
