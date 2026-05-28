---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Forderungsmanagement Klagewerkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Forderungsmanagement-Klagewerkstatt — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Forderungsmanagement Klagewerkstatt**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

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
| `inkasso-zahlungsklage-ersteller` | Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten § 288… |
| `klage-aus-eigenem-skill` | Kanzlei hat hauseigenes Klage-Plugin (klagewerkstatt-kanzlei) installiert und will damit Klagen aus eigenem Sachverhalt erstellen. Laufzeit-Variante Klagewerkstatt. Prüfraster: Sachverhalt Beklagtenadresse… |
| `klagevorlage-aus-eigenen-mustern` | Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage… |

## Worum geht es?

Das Plugin begleitet Glaeubiger und Anwaelte vom Forderungsmanagement bis zur gerichtlichen Titulierung. Im Mittelpunkt steht der sogenannte Gatekeeper: Nur Forderungen, die klar beziffert, faellig und belegt sind, werden zur Zahlungsklage freigegeben. So werden aussichtslose Klagen vermieden, die Kosten verursachen ohne Erfolgsaussicht.

Das Plugin unterstuetzt zudem den Aufbau kanzleieigener Klagemuster und ermoeglicht die Integration mit vorhandenen Kanzlei-Klagewerkstatt-Plugins. Zielgruppe sind Anwaelte, Inkassounternehmen und Unternehmensjuristen im Forderungseinzug.

## Wann brauchen Sie diese Skill?

- Glaeubigerseite hat offene, unbezahlte Forderung und muss entscheiden, ob und wie sie klagen soll.
- Kanzlei will den Mahnvorlauf dokumentieren und pruefen, ob Verzug wirksam eingetreten ist.
- Mandant fragt, ob Amtsgericht oder Landgericht zustaendig ist und ob Mahnbescheid oder Klage sinnvoller ist.
- Kanzlei will hauseigene Klagemuster fuer wiederkehrende Forderungstypen strukturieren und wiederverwenden.
- Forderung liegt im Grenzbereich: Verpflichtungseinrede oder Gegenforderung des Schuldners muss vorab geprueft werden.

## Fachbegriffe (kurz erklaert)

- **Gatekeeper** — Vorabpruefung, ob Forderung klar, faellig und belegt ist, bevor Klageerstellung ausgeloest wird.
- **Verzug (§ 286 BGB)** — Schuldner leistet trotz Faelligkeit und Mahnung nicht; Voraussetzung fuer Verzugszinsen und Schadensersatz.
- **Mahnbescheid (§§ 688 ff. ZPO)** — Vereinfachtes gerichtliches Verfahren zur Titulierung unstreitiger Forderungen ohne muendliche Verhandlung.
- **Vollstreckungstitel** — Dokument, das Zwangsvollstreckung erlaubt (z.B. Urteil, Vollstreckungsbescheid, notarielle Urkunde).
- **Streitwert** — Geldwert der Forderung; entscheidet ueber Zustaendigkeit (AG bis 5.000 EUR nach altem Recht; ab 01.01.2026 AG bis 10.000 EUR, § 23 GVG) und Gerichtskosten.
- **Inkasso-Zahlungsklage** — Auf Geldzahlung gerichtete Klage mit standardisierten Pflichtbestandteilen (§§ 253 253 ZPO).

## Rechtsgrundlagen

- §§ 241 280 286 288 BGB — Leistungspflicht, Schadensersatz, Verzug, Verzugszinsen
- §§ 688 ff. ZPO — Mahnverfahren
- §§ 253 313 ZPO — Klageschrift, Urteilsbestandteile
- § 23 GVG — Sachliche Zustaendigkeit Amtsgericht
- § 71 GVG — Sachliche Zustaendigkeit Landgericht

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Forderung pruefen: Ist sie klar beziffert, faellig und belegt (Vertrag, Rechnung, Mahnung)?
2. Zustaendigkeit bestimmen: AG oder LG nach Streitwert; ggf. besonderer Gerichtsstand.
3. Mahnvorlauf dokumentieren: Liegt wirksame Mahnung vor? Ist Verzug eingetreten?
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Klagemuster pruefen oder anpassen: Eigene Kanzleimuster einbinden oder Standardmuster verwenden.

## Skill-Tour (was gibt es hier?)

- `inkasso-zahlungsklage-ersteller` — Erstellt eine vollstaendige Zahlungsklage fuer belegte und faellige Forderungen; Gatekeeper-Pruefung vor Klageerstellung.
- `klage-aus-eigenem-skill` — Verbindet Plugin mit kanzleiinternem Klagewerkstatt-Plugin (klagewerkstatt-kanzlei) fuer mandatsspezifische Klagen aus eigenem Sachverhalt.
- `klagevorlage-aus-eigenen-mustern` — Destilliert kanzleieigene Klagemuster einmalig in ein wiederverwendbares Plugin-Format.

## Worauf besonders achten

- Verzug muss wirksam begruendet sein: Mahnung nach § 286 BGB oder kalendarische Faelligkeit; fehlende Mahnung macht Verzugszinsen unbegruendet.
- Streitwertgrenzen beachten: Seit 01.01.2026 ist das AG bis 10.000 EUR sachlich zustaendig (§ 23 Nr. 1 GVG, Justizstandort-Staerkungsgesetz).
- Gegenansprueche und Einreden des Schuldners vor Klageerhebung ermitteln; unangemeldete Aufrechnung kann Klage entwerten.
- Im Mahnverfahren (§ 688 ZPO) sind von der Hauptforderung abhaengige Nebenforderungen separat zu beziffern.
- Klagemuster aus Kanzlei-Datenbanken muessen auf den konkreten Sachverhalt angepasst werden; blindes Uebernehmen fuehrt zu unzulaessigen oder unschluessigen Antraegen.

## Typische Fehler

- Klage ohne vorherige Mahnung: Ohne wirksame Mahnung kann keine Zahlungsklage auf Verzugszinsen gestellt werden.
- Streitwert falsch angegeben: Neben- und Zinsforderungen koennen Streitwert in eine andere Gerichtsstandskategorie heben.
- Forderung nicht hinreichend substantiiert: Rechnung oder Vertrag fehlt als Anlage; Klage wird unschluessig.
- Verpflichtungseinrede uebersehen: Schuldner hat eigene Gegenansprueche, die aufgerechnet werden koennen.
- Zu spaet zum Massnahmenpaket: Nach Abschluss Mahnverfahren laufen Widerspruchsfristen; versaeumte Folgeschritte fuehren zu Fristversaeumnissen.

## Querverweise

- Plugin `zwangsvollstreckung` — Sobald Titel vorhanden, Vollstreckungsschritte einleiten.
- Plugin `selbstvertreter-amtsgericht` — Klaeger ohne Anwalt; Prozessbegleitung vor dem AG.
- Plugin `grosskanzlei-corporate-ma` — Bei hohen B2B-Forderungen ggf. Konzernhaftung oder Distressed-Aspekte pruefen.

## Quellen und Aktualitaet

- Stand: 05/2026
- § 23 Nr. 1 GVG in der Fassung des Justizstandort-Staerkungsgesetzes (Wertgrenze 10.000 EUR seit 01.01.2026)
- BGB und ZPO in aktuell geltender Fassung
