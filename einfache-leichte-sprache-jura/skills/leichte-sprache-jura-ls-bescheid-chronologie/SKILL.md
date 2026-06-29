---
name: leichte-sprache-jura-ls-bescheid-chronologie
description: "Einstieg, Schnelltriage und Fallrouting im Einfache Leichte Sprache Jura-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill e"
---

# Einfache und Leichte Sprache Jura — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BFSG ab 28.06.2025, BITV § 4 Verständlichkeit, BGG § 11 Pflicht zur einfachen Sprache bei Bescheiden auf Antrag.
- Tragende Normen verifizieren: BGG §§ 11, 12a, BITV 2.0 § 4, BFSG, UN-Behindertenrechtskonvention Art. 9 (Zugänglichkeit), EU-RL 2016/2102, DIN SPEC 33429 (Leichte Sprache), Hurraki-/Inclusion Europe-Regeln — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Behörde, Verwaltungsstelle, Übersetzer Leichte Sprache, Prüfgruppe (Selbstvertreter), Sozialverbände (Lebenshilfe, BAGSO), Behindertenbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Bescheid in Leichter Sprache, Erklärfilm-Skript, Antragsformular mit Erläuterung, Mandanteninfo, Prozessunterlagen in einfacher Sprache — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Einfache Leichte Sprache Jura**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen.

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
| `elsj-einfache-sprache` | Kanzlei oder Behörde will juristischen Text für normale Buerger verstaendlich machen: Einfache Sprache B1-Niveau zielgruppenorientiert klare Gliederung erklärte Rechtsbegriffe gesicherte Fristen. Normen BGG § 11… |
| `elsj-juristische-sicherung` | Beim Vereinfachen juristischer Texte darf kein Rechtsinhalt verloren gehen: Rechte Pflichten Fristen Betraege Rechtsfolgen Ausnahmen. Normen §§ 133 157 BGB Auslegungspflicht. Prüfraster Rechte-Vollständigkeit… |
| `elsj-kommandocenter` | Kanzlei oder Behörde startet Vereinfachungs-Projekt für juristischen Text: Zielgruppe Modus Rechtsinhalt-Erfassung Workflow-Steuerung Ausgabe. Normen BGG BITV 2.0. Prüfraster Zielgruppen-Identifikation Modus-Auswahl… |
| `elsj-leichte-sprache` | Kanzlei oder Behörde will juristischen Text für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen aufbereiten: Leichte Sprache nach Netzwerk Leichte Sprache A2-Niveau kurze Saetze klare Zeilenstruktur… |
| `elsj-qualitaetsgate` | Fertig erstellte Fassung in Einfacher Sprache oder Leichter Sprache vor Veröffentlichung prüfen. Verstaendlichkeit Gliederung Glossar Zielgruppenpassung juristische Vollständigkeit offene Nutzergruppen-Prüfung. Normen… |

## Worum geht es?

Juristische Texte — Bescheide, Verträge, Urteile, Merkblaetter — sind für viele Buergerinnen und Buerger schwer verstaendlich. Dieses Plugin unterstuetzt Kanzleien und Behörden dabei, solche Texte in Einfache Sprache (Zielniveau B1) oder Leichte Sprache (Zielniveau A2 gemäß BITV 2.0) zu uebertragen, ohne dabei Rechtsinhalt, Fristen oder Rechtswirkungen zu verlieren.

Das Plugin unterscheidet strikt zwischen Verstaendlichkeit und inhaltlicher Absicherung: Vereinfachungen müssen stets gegen das Original geprueft werden. Das Qualitaetsgate am Ende des Workflows sichert die Konformitaet vor Veroeffentlichung.

## Wann brauchen Sie diese Skill?

- Eine Behörde will Bescheide oder Widerspruchsbeschluesse für Buerger mit eingeschraenkter Lesekompetenz aufbereiten.
- Eine Kanzlei erklaert Mandanten verstaendlich, welche Rechte und Pflichten ein Vertrag begruendet.
- Ein Unternehmen muss seine Datenschutzerklaerung barrierefrei gestalten (BITV 2.0, WCAG 2.1).
- Ein Pflegeheim oder eine Sozialeinrichtung will Heimvertraege in Leichte Sprache übersetzen.
- Ein Verband prüft, ob sein öffentlich zugaengliches Rechtsmerkblatt verstaendlich genug ist.

## Fachbegriffe (kurz erklaert)

- **Einfache Sprache** — Schriftsprachliche Vereinfachung auf ca. Niveau B1 des Europaeischen Referenzrahmens; kurze Saetze, gebraeuchliche Woerter, aktive Formulierungen.
- **Leichte Sprache** — Stark vereinfachte Sprache auf Niveau A2 nach BITV 2.0 und dem Regelwerk des Netzwerks Leichte Sprache; standardisierte Regeln zu Wortlaenge, Satzstruktur und Bildunterstuetzung.
- **BITV 2.0** — Barrierefreie-Informationstechnik-Verordnung; verpflichtet öffentliche Stellen zur barrierefreien Gestaltung digitaler Angebote einschliesslich Leichter Sprache.
- **Rechtsinhalt-Sicherung** — Prüfung, dass nach der Vereinfachung keine Rechte, Pflichten, Fristen oder Rechtsfolgen verloren gegangen sind.
- **Qualitaetsgate** — Abschlusspruefung vor Veroeffentlichung: Verstaendlichkeit, Gleichgewicht zum Original, Glossar-Konsistenz, Barrierefreiheit.
- **Zielgruppe** — Definierte Personengruppe (z. B. Menschen mit Lernschwierigkeiten, Buerger ohne Rechtskenntnisse), nach der Schwierigkeitsgrad und Modus gewaehlt werden.

## Rechtsgrundlagen

- § 11 BGG (Barrierefreiheitsgebot öffentlicher Stellen)
- BITV 2.0 — Barrierefreie-Informationstechnik-Verordnung
- § 3 BMAS-Richtlinie zu Leichter Sprache in Behörden
- Art. 7 Abs. 2 DSGVO (Anforderungen an Einwilligungserklaerungen in verstaendlicher Sprache)
- § 305 Abs. 2 BGB (Einbeziehungsvoraussetzungen für AGB — Deutlichkeitsgebot)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Wer ist die Zielgruppe des vereinfachten Textes?
2. Modus festlegen: Einfache Sprache (B1) oder Leichte Sprache (A2)?
3. Rechtsinhalt erfassen: Alle relevanten Rechte, Pflichten, Fristen und Rechtsfolgen des Originaltexts sichern (Skill `elsj-juristische-sicherung`).
4. Vereinfachung erstellen: Passenden Skill waehlen (`elsj-einfache-sprache` oder `elsj-leichte-sprache`).
5. Qualitaetsgate durchlaufen: Fertige Fassung vor Veroeffentlichung prüfen (`elsj-qualitaetsgate`).

## Skill-Tour (was gibt es hier?)

- `elsj-kommandocenter` — Navigationszentrum: Zielgruppe und Modus klären, starten, alle Skills koordinieren.
- `elsj-einfache-sprache` — Juristischen Text auf Einfache Sprache Niveau B1 uebertragen für Buerger ohne Fachkenntnisse.
- `elsj-leichte-sprache` — Juristischen Text auf Leichte Sprache Niveau A2 uebertragen für Menschen mit Lernschwierigkeiten oder kognitiven Einschraenkungen.
- `elsj-juristische-sicherung` — Sicherstellt, dass kein Rechtsinhalt (Rechte, Pflichten, Fristen, Betraege, Rechtsfolgen) bei der Vereinfachung verloren geht.
- `elsj-qualitaetsgate` — Abschlusspruefung der vereinfachten Fassung vor Veroeffentlichung auf Verstaendlichkeit, Gläubigkeit und Vollstaendigkeit.

## Worauf besonders achten

- Einfache Sprache und Leichte Sprache sind verschiedene Standards mit unterschiedlichen Regelwerken — Modus am Anfang festlegen, nicht waehrend der Bearbeitung wechseln.
- Kein Rechtsinhalt darf durch Vereinfachung verloren gehen: Fristen, Betraege und Rechtsfolgen müssen exakt erhalten bleiben.
- Leichte Sprache erfordert typischerweise die Einbindung von Prüferinnen und Prüfern mit kognitiven Einschraenkungen — das Plugin kann nur den Text liefern, nicht die Prüfung ersetzen.
- Bei Bescheiden und amtlichen Dokumenten gilt: Vereinfachungen sind Informationshilfen, kein rechtsverbindlicher Ersatz des Originaldokuments.
- AGB-Vereinfachungen können auf Einbeziehungsfragen nach § 305 BGB wirken — rechtliche Wechselwirkungen bedenken.

## Typische Fehler

- Zielgruppe nicht definiert: Text wird zu stark oder zu wenig vereinfacht, weil unklar ist, für wen er bestimmt ist.
- Rechtsinhalt-Sicherung uebersprungen: Fristen oder Rechtswirkungen gehen in der Vereinfachung unter.
- Einfache und Leichte Sprache verwechselt: Leichte Sprache hat deutlich strengere Regeln (Satzlaenge, Bildunterstuetzung, Glossar).
- Qualitaetsgate nicht durchgefuehrt: Vereinfachter Text wird veroeffentlicht, ohne auf Korrektheit geprueft zu werden.
- Vereinfachung als rechtsverbindlich behandelt: Mandant glaubt, der vereinfachte Text ersetzt das Original.

## Querverweise

- `datenschutzrecht` — DSGVO-Einwilligungen und Datenschutzerklaerungen müssen verstaendlich formuliert sein (Art. 7 Abs. 2 DSGVO).
- `vertragsrecht` — AGB-Einbeziehung nach § 305 BGB erfordert klare, verstaendliche Formulierungen.
- `selbstvertreter-amtsgericht` — Buerger ohne Rechtskenntnisse können von vereinfachten Gerichtsdokumenten profitieren.

## Quellen und Aktualitaet

- Stand: 05/2026
- BITV 2.0 in der Fassung vom 21.05.2019
- Gesetzesfassungen zum Stand-Datum
- Regelwerk Leichte Sprache des Netzwerks Leichte Sprache (netzwerk-leichte-sprache.org)
- WCAG 2.1 (Web Content Accessibility Guidelines)
