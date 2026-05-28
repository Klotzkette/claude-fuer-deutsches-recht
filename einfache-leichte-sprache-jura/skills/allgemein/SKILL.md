---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Einfache und Leichte Sprache Jura — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Einfache Leichte Sprache Jura**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen.

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
| `elsj-einfache-sprache` | Kanzlei oder Behoerde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11… |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit… |
| `elsj-kommandocenter` | Kanzlei oder Behoerde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl… |
| `elsj-leichte-sprache` | Kanzlei oder Behoerde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur… |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen… |

## Worum geht es?

Juristische Texte — Bescheide, Vertraege, Urteile, Merkblaetter — sind fuer viele Buergerinnen und Buerger schwer verstaendlich. Dieses Plugin unterstuetzt Kanzleien und Behoerden dabei, solche Texte in Einfache Sprache (Zielniveau B1) oder Leichte Sprache (Zielniveau A2 gemaess BITV 2.0) zu uebertragen, ohne dabei Rechtsinhalt, Fristen oder Rechtswirkungen zu verlieren.

Das Plugin unterscheidet strikt zwischen Verstaendlichkeit und inhaltlicher Absicherung: Vereinfachungen muessen stets gegen das Original geprueft werden. Das Qualitaetsgate am Ende des Workflows sichert die Konformitaet vor Veroeffentlichung.

## Wann brauchen Sie diese Skill?

- Eine Behoerde will Bescheide oder Widerspruchsbeschluesse fuer Buerger mit eingeschraenkter Lesekompetenz aufbereiten.
- Eine Kanzlei erklaert Mandanten verstaendlich, welche Rechte und Pflichten ein Vertrag begruendet.
- Ein Unternehmen muss seine Datenschutzerklaerung barrierefrei gestalten (BITV 2.0, WCAG 2.1).
- Ein Pflegeheim oder eine Sozialeinrichtung will Heimvertraege in Leichte Sprache uebersetzen.
- Ein Verband prueft, ob sein oeffentlich zugaengliches Rechtsmerkblatt verstaendlich genug ist.

## Fachbegriffe (kurz erklaert)

- **Einfache Sprache** — Schriftsprachliche Vereinfachung auf ca. Niveau B1 des Europaeischen Referenzrahmens; kurze Saetze, gebraeuchliche Woerter, aktive Formulierungen.
- **Leichte Sprache** — Stark vereinfachte Sprache auf Niveau A2 nach BITV 2.0 und dem Regelwerk des Netzwerks Leichte Sprache; standardisierte Regeln zu Wortlaenge, Satzstruktur und Bildunterstuetzung.
- **BITV 2.0** — Barrierefreie-Informationstechnik-Verordnung; verpflichtet oeffentliche Stellen zur barrierefreien Gestaltung digitaler Angebote einschliesslich Leichter Sprache.
- **Rechtsinhalt-Sicherung** — Pruefung, dass nach der Vereinfachung keine Rechte, Pflichten, Fristen oder Rechtsfolgen verloren gegangen sind.
- **Qualitaetsgate** — Abschlusspruefung vor Veroeffentlichung: Verstaendlichkeit, Gleichgewicht zum Original, Glossar-Konsistenz, Barrierefreiheit.
- **Zielgruppe** — Definierte Personengruppe (z. B. Menschen mit Lernschwierigkeiten, Buerger ohne Rechtskenntnisse), nach der Schwierigkeitsgrad und Modus gewaehlt werden.

## Rechtsgrundlagen

- § 11 BGG (Barrierefreiheitsgebot oeffentlicher Stellen)
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung
- § 3 BMAS-Richtlinie zu Leichter Sprache in Behoerden
- Art. 7 Abs. 2 DSGVO (Anforderungen an Einwilligungserklaerungen in verstaendlicher Sprache)
- § 305 Abs. 2 BGB (Einbeziehungsvoraussetzungen fuer AGB — Deutlichkeitsgebot)

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer ist die Zielgruppe des vereinfachten Textes?
2. Modus festlegen: Einfache Sprache (B1) oder Leichte Sprache (A2)?
3. Rechtsinhalt erfassen: Alle relevanten Rechte, Pflichten, Fristen und Rechtsfolgen des Originaltexts sichern (Skill `elsj-juristische-sicherung`).
4. Vereinfachung erstellen: Passenden Skill waehlen (`elsj-einfache-sprache` oder `elsj-leichte-sprache`).
5. Qualitaetsgate durchlaufen: Fertige Fassung vor Veroeffentlichung pruefen (`elsj-qualitaetsgate`).

## Skill-Tour (was gibt es hier?)

- `elsj-kommandocenter` — Navigationszentrum: Zielgruppe und Modus klaeren, Workflow starten, alle Skills koordinieren.
- `elsj-einfache-sprache` — Juristischen Text auf Einfache Sprache Niveau B1 uebertragen fuer Buerger ohne Fachkenntnisse.
- `elsj-leichte-sprache` — Juristischen Text auf Leichte Sprache Niveau A2 uebertragen fuer Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen.
- `elsj-juristische-sicherung` — Sicherstellt, dass kein Rechtsinhalt (Rechte, Pflichten, Fristen, Betraege, Rechtsfolgen) bei der Vereinfachung verloren geht.
- `elsj-qualitaetsgate` — Abschlusspruefung der vereinfachten Fassung vor Veroeffentlichung auf Verstaendlichkeit, Glaeubigkeit und Vollstaendigkeit.

## Worauf besonders achten

- Einfache Sprache und Leichte Sprache sind verschiedene Standards mit unterschiedlichen Regelwerken — Modus am Anfang festlegen, nicht waehrend der Bearbeitung wechseln.
- Kein Rechtsinhalt darf durch Vereinfachung verloren gehen: Fristen, Betraege und Rechtsfolgen muessen exakt erhalten bleiben.
- Leichte Sprache erfordert typischerweise die Einbindung von Prueferinnen und Pruefern mit kognitiven Einschraenkungen — das Plugin kann nur den Text liefern, nicht die Pruefung ersetzen.
- Bei Bescheiden und amtlichen Dokumenten gilt: Vereinfachungen sind Informationshilfen, kein rechtsverbindlicher Ersatz des Originaldokuments.
- AGB-Vereinfachungen koennen auf Einbeziehungsfragen nach § 305 BGB wirken — rechtliche Wechselwirkungen bedenken.

## Typische Fehler

- Zielgruppe nicht definiert: Text wird zu stark oder zu wenig vereinfacht, weil unklar ist, fuer wen er bestimmt ist.
- Rechtsinhalt-Sicherung uebersprungen: Fristen oder Rechtswirkungen gehen in der Vereinfachung unter.
- Einfache und Leichte Sprache verwechselt: Leichte Sprache hat deutlich strengere Regeln (Satzlaenge, Bildunterstuetzung, Glossar).
- Qualitaetsgate nicht durchgefuehrt: Vereinfachter Text wird veroeffentlicht, ohne auf Korrektheit geprueft zu werden.
- Vereinfachung als rechtsverbindlich behandelt: Mandant glaubt, der vereinfachte Text ersetzt das Original.

## Querverweise

- `datenschutzrecht` — DSGVO-Einwilligungen und Datenschutzerklaerungen muessen verstaendlich formuliert sein (Art. 7 Abs. 2 DSGVO).
- `vertragsrecht` — AGB-Einbeziehung nach § 305 BGB erfordert klare, verstaendliche Formulierungen.
- `selbstvertreter-amtsgericht` — Buerger ohne Rechtskenntnisse koennen von vereinfachten Gerichtsdokumenten profitieren.

## Quellen und Aktualitaet

- Stand: 05/2026
- BITV 2.0 in der Fassung vom 21.05.2019
- Gesetzesfassungen zum Stand-Datum
- Regelwerk Leichte Sprache des Netzwerks Leichte Sprache (netzwerk-leichte-sprache.org)
- WCAG 2.1 (Web Content Accessibility Guidelines)
