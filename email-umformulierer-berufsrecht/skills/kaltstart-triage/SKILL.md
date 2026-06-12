---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Email Umformulierer Berufsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill"
---

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Email Umformulierer Berufsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Email Umformulierer Berufsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Formuliert unfreundliche, emotionale oder unsachliche E-Mails in hoefliche, sachliche und berufsrechtskonform formulierte Texte um. Fokus auf BRAO/BORA-Konformität, mit Varianten für Steuerberater, Notare und allgemeine berufliche Korrespondenz.

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
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

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
| `email-berufsrecht-berufliche-korrespondenz` | Allgemeine berufliche E-Mail-Korrespondenz von Anwaelten professionell und berufsrechtskonform umformulieren. § 43a BRAO allgemeine Berufspflichten § 26 BORA Sachlichkeitsgebot. Prüfraster: Sachlichkeit… |
| `anrede-und-grussformeln` | Anrede und Grussformeln in Anwaltskorrespondenz prufen und berufsrechtskonform optimieren. § 43a BRAO § 26 BORA Kollegialitätsgebot. Prüfraster: korrekte Anrede Titel akademischer Grad Kollegialformel Schlussformel… |
| `bora-konformitaetspruefung` | E-Mail auf BORA-Konformität prüfen bevor sie versandt wird. §§ 6 ff. BORA allgemeine Berufspflichten § 26 BORA Werbung § 43 BORA Vertretungsverbot. Prüfraster: Sachlichkeitsgebot Werbeverbot Verschwiegenheit… |
| `brao-konformitaetspruefung` | E-Mail auf BRAO-Konformität prüfen bevor sie versandt wird. §§ 43 43a 43b BRAO Grundpflichten Sachlichkeitsgebot Werbung. Prüfraster: Verschwiegenheitspflicht Interessenkonflikt unabhängige Berufsausübung Werbegrenzen… |
| `email-eingangsanalyse` | Eingehende E-Mail analysieren und Tonalitaet Konfliktpotenzial und Handlungsbedarf bestimmen. § 43a BRAO Berufsrecht. Prüfraster: Tonalitaet emotionale Trigger versteckte Forderungen Fristen Eskalationspotenzial.… |
| `emotionale-trigger-katalog` | Emotionale Trigger-Woerter und -Phrasen in Anwaltskorrespondenz identifizieren und neutralisieren. § 26 BORA Sachlichkeit § 43a BRAO Berufspflichten. Prüfraster: aggressive Formulierungen persönliche Angriffe… |
| `frist-und-mahnung-hoeflich` | Fristsetzungen und Mahnungen in Anwaltskorrespondenz hoeflich und dennoch rechtsverbindlich formulieren. § 286 BGB Schuldnerverzug § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Fristklarheit Verbindlichkeit Ton… |
| `ironie-und-sarkasmus-eliminieren` | Ironische oder sarkastische Formulierungen in Anwaltskorrespondenz erkennen und berufsrechtlich einwandfrei neutralisieren. § 26 BORA Sachlichkeitsgebot § 43a BRAO. Prüfraster: Ironie-Erkennung Sarkasmus versteckte… |
| `klare-bitte-formulieren` | Unklare oder versteckte Bitten und Forderungen in Anwaltskorrespondenz klar und direkt formulieren. § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Klarheit der Bitte Unmissverstaendlichkeit Handlungsaufforderung… |
| `kollegialitaetsgebot-pruefung` | E-Mail auf Einhaltung des Kollegialitätsgebots gegenüber Kollegen und Kolleginnen prüfen. § 43a Abs. 3 BRAO § 26 BORA Kollegialität. Prüfraster: kollegiale Formulierungen fehlende Abwertungen sachliche Kritik… |
| `kompetenz-zweifel-respektvoll` | Zweifel an Kompetenz oder Entscheidung des Gegners oder Kollegen respektvoll und sachlich aeussern. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: sachliche Kritik ohne Abwertung Begründung Quellenangabe… |
| `konfliktdeeskalation-formulierungen` | Eskalierte oder hitzige Korrespondenz deeskalieren und konstruktive Kommunikationsbasis herstellen. § 43a BRAO § 26 BORA Sachlichkeit. Prüfraster: Eskalationsniveau Interessenidentifikation deeskalierende… |
| `kooperativer-abschluss` | E-Mail oder Schreiben mit kooperativem und prozessfoerderlichem Abschluss versehen. § 43a BRAO § 26 BORA. Prüfraster: offen für Gespraeich konstruktiver Ausblick ohne Überversprechung. Output: optimierter Abschlusssatz… |
| `mehrsprachige-umformulierung` | Anwaltskorrespondenz in einer anderen Sprache berufsrechtskonform und sachgerecht umformulieren. § 43a BRAO §§ 26 ff. BORA internat. Anwaltsstandards. Prüfraster: Äquivalenz der Rechtsbegriffe Sachlichkeit… |
| `notare-bnotk-modus` | Korrespondenz von Notaren und Notarinnen auf notarrechtliche Besonderheiten und BNotK-Vorgaben anpassen. §§ 14 17 BNotO § 26 BRAO analog. Prüfraster: neutrale Beurkundsrolle Unparteilichkeit Gebotes zur Unabhängigkeit… |
| `persönlichen-angriff-entschaerfen` | Persoenliche Angriffe und Beleidigungen in Anwaltskorrespondenz erkennen und durch sachliche Formulierungen ersetzen. § 43a BRAO § 26 BORA Sachlichkeitsgebot. Prüfraster: persönliche Angriffe Beleidigungen… |
| `sachlichkeitsgebot-anwendung` | Sachlichkeitsgebot nach § 26 BORA auf konkrete Korrespondenz anwenden und Verbesserungen vornehmen. § 26 BORA Sachlichkeit § 43a BRAO. Prüfraster: unsachliche Formulierungen Emotionalisierung Abwertungen… |
| `sachverhalt-neutral-darstellen` | Sachverhalt in Anwaltskorrespondenz neutral und ohne wertende Parteinahme darstellen. § 43a BRAO Sachlichkeit §§ 86 ff. ZPO Sachverhaltspflicht. Prüfraster: Parteinahme Wertungen Auslassungen Einseitigkeit neutrale… |
| `steuerberater-stberg-modus` | Korrespondenz von Steuerberatern auf StBerG- und Berufsrechts-Konformität anpassen. §§ 57 57a StBerG Berufspflichten DVStB. Prüfraster: Verschwiegenheit Sachlichkeit Werbegrenzen fachliche Kompetenz Unabhängigkeit.… |
| `vorher-nachher-tabelle` | Vorher-Nachher-Vergleich für umformulierte Anwaltskorrespondenz erstellen und Änderungen erklären. § 43a BRAO § 26 BORA. Prüfraster: Vollständigkeit Erklärbarkeit jeder Änderung Berufsrechtsbezug. Output: Tabelle mit… |

## Worum geht es?

Das Plugin formuliert unfreundliche, emotionale oder berufsrechtlich problematische E-Mails in hoefliche, sachliche und berufsrechtskonforme Texte um. Im Mittelpunkt steht die Einhaltung von § 43a BRAO (Sachlichkeitsgebot) und §§ 26 ff. BORA (Kollegialitaets- und Sachlichkeitsgebot). Das Plugin deckt auch Sondermodalitaeten für Notare (BNotO) und Steuerberater (StBerG) ab sowie mehrsprachige Umformulierungen.

Zielgruppe sind Anwaelte, Kanzleipersonal, Notare und Steuerberater, die ihren Schriftverkehr berufsrechtlich absichern und professionell kommunizieren wollen. Das Plugin bietet sowohl Einzelschritt-Skills (z.B. Ironie eliminieren, persönlichen Angriff entschaerfen) als auch Gesamt-Workflows (Eingangsanalyse bis fertiger Vorher-Nachher-Vergleich).

## Wann brauchen Sie diese Skill?

- Anwalt hat eine hitzige oder beleidigende E-Mail erhalten und will sachlich, aber bestimmt antworten.
- Kollegin hat Entwurf geschrieben, der zu emotional oder zu aggressiv ist und BORA-Konformitaet fehlt.
- Kanzlei versetzt eine Fristsetzung oder Mahnung, die zwar klar sein soll, aber dennoch hoeflich und nicht eskalierend.
- Notar oder Steuerberater braucht standestypische Korrespondenz, die den jeweiligen Berufspflichten genuegt.
- Schriftsatz oder E-Mail in fremder Sprache soll berufsrechtlich einwandfrei und sachlich formuliert werden.

## Fachbegriffe (kurz erklaert)

- **Sachlichkeitsgebot (§ 43a BRAO / § 26 BORA)** — Anwaelte müssen sachlich formulieren und unwahre Tatsachenbehauptungen oder herabwuerdigende Aeusserungen unterlassen.
- **Kollegialitaetsgebot (§ 43a Abs. 3 BRAO / § 26 BORA)** — Im Verkehr mit anderen Anwaelten ist gegenseitige Achtung und fairer Umgang gefordert.
- **Emotionale Trigger** — Woerter oder Formulierungen, die beim Empfaenger negative Emotionen ausloesen und die Kommunikation eskalieren.
- **Deeskalation** — Kommunikative Maßnahmen, um aus einer eskalierten Korrespondenz konstruktiv herauszufinden.
- **BORA** — Berufsordnung der Rechtsanwaelte; konkretisiert die Berufspflichten aus § 43a BRAO.
- **BNotO** — Bundesnotarordnung; berufsrechtliche Grundlage für Notare, mit eigenen Sachlichkeits- und Unabhaengigkeitspflichten.
- **StBerG** — Steuerberatungsgesetz; regelt Berufspflichten der Steuerberater, u.a. § 57 StBerG Allgemeine Berufspflichten.

## Rechtsgrundlagen

- §§ 43 43a BRAO — Grundpflichten der Rechtsanwaelte, Sachlichkeitsgebot
- § 26 BORA — Sachlichkeitsgebot, Kollegialitaet im Rechtsanwaltsverkehr
- §§ 6 ff. BORA — Allgemeine Berufspflichten
- § 14 BNotO — Allgemeine Amts- und Berufspflichten der Notare
- § 57 StBerG — Allgemeine Berufspflichten der Steuerberater
- § 186 StGB — Beleidigung (grenzwertige Formulierungen können strafrechtlich relevant sein)

## Schritt-für-Schritt: Einstieg ins Plugin

1. E-Mail oder Schreiben einlesen: Original-Text einspielen oder einfuegen.
2. Eingangsanalyse durchfuehren: Tonalitaet, emotionale Trigger und Konfliktpotenzial bestimmen.
3. Berufsrechtlichen Kontext festlegen: BRAO/BORA, BNotO oder StBerG; Sprache der Korrespondenz?
4. Passenden Skill auswaehlen (siehe Skill-Tour) oder Gesamt-starten.
5. Vorher-Nachher-Vergleich prüfen und Änderungen erklaeren.

## Skill-Tour (was gibt es hier?)

- `email-eingangsanalyse` — Eingehende E-Mail analysieren: Tonalitaet, Konfliktpotenzial und Handlungsbedarf bestimmen.
- `brao-konformitaetspruefung` — E-Mail auf BRAO-Konformitaet (§§ 43 43a 43b) prüfen vor Versand.
- `bora-konformitaetspruefung` — E-Mail auf BORA-Konformitaet (§§ 6 ff. 26 BORA) prüfen vor Versand.
- `sachlichkeitsgebot-anwendung` — Sachlichkeitsgebot nach § 26 BORA auf konkrete Korrespondenz anwenden.
- `kollegialitaetsgebot-pruefung` — Kollegialitaetsgebot im Anwaltsverkehr prüfen und Formulierungen anpassen.
- `emotionale-trigger-katalog` — Trigger-Woerter und -Phrasen identifizieren und neutralisieren.
- `ironie-und-sarkasmus-eliminieren` — Ironie oder Sarkasmus erkennen und berufsrechtlich einwandfrei ersetzen.
- `persönlichen-angriff-entschaerfen` — Persoenliche Angriffe oder Beleidigungen durch sachliche Formulierungen ersetzen.
- `sachverhalt-neutral-darstellen` — Sachverhalt ohne wertende Parteinahme neutral darstellen.
- `kompetenz-zweifel-respektvoll` — Zweifel an Kompetenz oder Entscheidung respektvoll und sachlich aeussern.
- `konfliktdeeskalation-formulierungen` — Eskalierte Korrespondenz deeskalieren; konstruktive Kommunikationsbasis herstellen.
- `frist-und-mahnung-hoeflich` — Fristsetzungen und Mahnungen hoeflich und dennoch rechtswirksam formulieren.
- `klare-bitte-formulieren` — Unklare oder versteckte Forderungen klar und direkt ausformulieren.
- `kooperativer-abschluss` — Schreiben mit kooperativem und prozessfoerderndem Abschluss versehen.
- `anrede-und-grussformeln` — Anrede und Grussformeln auf berufsrechtliche und stilistische Anforderungen prüfen.
- `email-berufsrecht-berufliche-korrespondenz` — Allgemeine berufliche E-Mail-Korrespondenz professionell und berufsrechtskonform umformulieren.
- `notare-bnotk-modus` — Notar-Korrespondenz auf BNotO- und BNotK-Vorgaben anpassen.
- `steuerberater-stberg-modus` — Steuerberater-Korrespondenz auf StBerG-Konformitaet anpassen.
- `mehrsprachige-umformulierung` — Anwaltskorrespondenz in anderer Sprache berufsrechtskonform und sachgerecht umformulieren.
- `vorher-nachher-tabelle` — Vorher-Nachher-Vergleich mit Erklaerungen der Änderungen erstellen.

## Worauf besonders achten

- Das Sachlichkeitsgebot verbietet auch verdeckt herabwuerdigende Formulierungen; nicht nur explizite Beleidigungen sind problematisch.
- Ironie und Sarkasmus sind in Anwalts-Schreiben immer berufsrechtlich riskant, da sie leicht als Beleidigung ausgelegt werden können.
- Bei Fristsetzungen muss die Frist klar und bestimmt sein (§ 286 BGB); Weichspueler-Formulierungen können Rechtswirkung vereiteln.
- Im Notar-Modus gelten besondere Unabhaengigkeitspflichten: Notar darf nicht Partei ergreifen; Sprache muss dies widerspiegeln.
- Mehrsprachige Umformulierungen müssen nicht nur sprachlich, sondern auch standesrechtlich der Zielsprache entsprechen (z.B. englisches Solicitor-Standesrecht).

## Typische Fehler

- Entschaerfung macht Schreiben rechtlich unwirksam: Frist oder Forderung wird so weich formuliert, dass keine Rechtsfolge mehr erkennbar ist.
- Nur oberflaeechliche Änderungen: Emotionaler Kern bleibt im Text, nur Schlüsselwoerter werden ausgetauscht.
- Sachverhalt wird beim Umformulieren verfaelscht: Neutrale Darstellung darf inhaltliche Aussage nicht ändern.
- BORA-Prüfung ohne Kontext: Kollegialitaetsgebot gilt nur im Anwaltsverkehr; in Mandanten-Kommunikation gelten andere Masssstaebe.
- Eigentor durch uebertriebene Hoeflichkeit: Zu konziliante Formulierung im Mahnschreiben kann als Zustimmung zur Verzoegerung ausgelegt werden.

## Quellen und Aktualitaet

- Stand: 05/2026
- BRAO und BORA in aktuell geltender Fassung
- BNotO und BNotK-Richtlinien; StBerG in aktuell geltender Fassung
