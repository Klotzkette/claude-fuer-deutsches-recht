---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Produktrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Produktrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Produktrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Produktrechtliche Skills für Launch-Review, Impressumspflicht nach DDG und PAngV sowie UWG-Bewertungen.

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
| `feature-risikobewertung` | Tiefgehende Risikobewertung für ein einzelnes Feature oder einen Produktbereich wenn der Launch-Review etwas gefunden hat das mehr als eine Tabellenzeile braucht. Strukturierte Analyse: was könnte schiefgehen, wie… |
| `impressum-pflicht` | Prüft die Impressumspflicht für Websites, Apps und Social-Media-Profile nach §§ 5 und 6 DDG und § 18 MStV, erstellt konforme Impressumstexte und identifiziert typische Abmahnrisiken nach UWG. Lädt bei Fragen zu… |
| `ist-das-ein-problem` | Schnelle „Ist-das-ein-Problem?\"-Antwort für die schnelle Slack-Frage – muster-erkennt gegen Ihre Kalibrierung. Verwenden wenn der Nutzer sagt „ist das ein Problem\", „kurze Frage\", „können wir X machen\", „brauche… |
| `launch-pruefung` | Produktmanager oder Rechtsabteilung will vor dem Launch prüfen ob das Produkt oder Feature produktrechtlich freigegeben werden kann. Vollständige rechtliche Freigabeprufung gegen konfiguriertes Prüfrahmenwerk und… |
| `preisangaben` | Prüft die Einhaltung der Preisangabenverordnung 2022 (PAngV) bei Gesamtpreisen, Grundpreisen, Streichpreisen und Versandkosten, insbesondere die 30-Tage-Niedrigstpreisregel bei Preisreduzierungen. Lädt bei Fragen zu… |
| `produktrecht-anpassen` | Geführte Anpassung Ihres Produktrecht-Praxisprofils – eine Sache ändern ohne das gesamte Kaltstart-Interview erneut auszuführen. Risikokalibrierung, Eskalationskontakte, Launch-Review-Framework, Werbeaussagen-Haltung… |
| `produktrecht-kaltstart-interview` | Produktrecht-Plugin erstmalig einrichten und Launch-Tracker verbinden sowie Risikokalibrierung der Rechtsabteilung erfassen. Verbindet Launch-Tracker liest vergangene Reviews lernt Risikokalibrierung. Normen ProdSG… |
| `produktrecht-mandat-arbeitsbereich` | Verwaltung von Produktmandats-Workspaces — Anlegen, Auflisten, Wechseln, Schließen oder Deaktivieren (auf Kanzleiebene). Lädt, wenn der Nutzer ein neues Mandat anlegen, zwischen Mandaten wechseln, ein Mandat… |
| `werbeaussagen-pruefung` | Prüfung von Werbeaussagen auf Irreführungs- und Wettbewerbsrechtsrisiken nach deutschem und europäischem Recht. Lädt, wenn der Nutzer „Werbetext prüfen\", „Marketingaussagen freigeben\", „UWG-Prüfung\", „Health… |

## Worum geht es?

Dieses Plugin unterstuetzt Produktmanager, Rechtsabteilungen und externe Anwaelte bei der produktrechtlichen Freigabe von digitalen und physischen Produkten vor dem Launch. Es deckt die zentralen rechtlichen Anforderungen ab: Impressumspflicht nach §§ 5 und 6 DDG und § 18 MStV, Preisangaben nach der Preisangabenverordnung 2022 (PAngV), Werbeaussagen nach UWG und EU-Recht (Omnibus-Richtlinie, Health Claims, ESG-Kommunikation), produktsicherheitsrechtliche Anforderungen (ProdSG, EU-Produktsicherheits-VO 2023/988, CE-Kennzeichnung) sowie UWG-Verstoessrisiken und DSGVO-Schnittstellen.

Das Plugin richtet sich an ein internes Rechts-Ops-Publikum: Entscheider in Rechtsabteilungen, Compliance-Teams und Kanzleien, die schnell und strukturiert produktrechtliche Risiken identifizieren wollen.

## Wann brauchen Sie diese Skill?

- Produkt oder Feature soll gelauncht werden und Rechtsabteilung muss gruene Ampel geben.
- Impressum einer Website, App oder Social-Media-Praesenz soll auf Vollstaendigkeit und Abmahnrisiken geprueft werden.
- Marketing will eine Werbeaussage prufen lassen: Streichpreise, Grundpreise, Health Claims, Klimaneutralitaet.
- Ein Feature des Produkts hat ein Risiko erzeugt, das tiefer analysiert werden muss als eine Checklisten-Zeile.
- Kaltstart: Plugin soll erstmalig konfiguriert und auf das Risikoprofil der Rechtsabteilung kalibriert werden.

## Fachbegriffe (kurz erklaert)

- **DDG** — Digitale-Dienste-Gesetz; nationales Ausfuehrungsgesetz; §§ 5 und 6 DDG regeln Anbieterkennzeichnungspflicht (Impressum).
- **PAngV** — Preisangabenverordnung 2022; regelt Gesamtpreise, Grundpreise, Streichpreise und die 30-Tage-Niedrigstpreisregel bei Preisreduzierungen.
- **UWG** — Gesetz gegen den unlauteren Wettbewerb; Massstab fuer irrefuehrende Werbeaussagen, vergleichende Werbung und aggressive Geschaeftspraktiken.
- **ProdSG** — Produktsicherheitsgesetz; regelt Sicherheitsanforderungen und Marktueberaufsicht.
- **CE-Kennzeichnung** — Konformitaetszeichen fuer Produkte, die EU-Harmonisierungsrecht entsprechen; Pflicht fuer viele Produktkategorien.
- **Health Claims** — Naehrwert- und gesundheitsbezogene Angaben; geregelt in VO (EG) 1924/2006; strenge Zulassungspflicht.
- **30-Tage-Niedrigstpreisregel** — Bei Preisreduzierungen muss als Ausgangspreis der niedrigste Preis der letzten 30 Tage angegeben werden (§ 11 PAngV; Omnibus-Richtlinie 2019/2161).
- **Launch-Review** — Strukturiertes rechtliches Freigabeverfahren vor Produkteinfuehrung mit Ampel-Status und offenem-Punkte-Liste.

## Rechtsgrundlagen

- §§ 5 und 6 DDG — Impressumspflicht.
- § 18 MStV — Impressumspflicht im Rundfunk- und Medienbereich.
- PAngV 2022 — Preisangaben; insb. § 11 PAngV (Streichpreise), § 4 PAngV (Grundpreis).
- UWG §§ 3 bis 7 — Irrefuehrende und aggressive Geschaeftspraktiken.
- ProdSG, EU-Produktsicherheits-VO 2023/988 — Produktsicherheit und CE-Konformitaet.
- VO (EG) 1924/2006 — Health Claims.
- AI Act (EU) 2024/1689 — KI-VO; Risikoklassen fuer KI-Systeme (relevant fuer KI-Features).
- DSGVO — Datenschutz-Schnittstelle fuer Features mit Personenbezug.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Plugin konfigurieren (Erstnutzung): Skill `produktrecht-kaltstart-interview`.
2. Schnelle Plausibilitaetsfrage: Skill `ist-das-ein-problem` fuer Kurzantwort in Minuten.
3. Vollstaendige Launch-Freigabe: Skill `launch-pruefung`.
4. Vertieftes Einzel-Risiko: `feature-risikobewertung`.
5. Spezialthemen: `impressum-pflicht`, `preisangaben` oder `werbeaussagen-pruefung` direkt ansteuern.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Mandatsverwaltung**

- `produktrecht-kaltstart-interview` — Plugin erstmalig einrichten; Risikokalibrierung, Launch-Framework, Eskalationsmatrix.
- `produktrecht-anpassen` — Einzelne Elemente des Praxisprofils aendern ohne Kaltstart-Interview.
- `produktrecht-mandat-arbeitsbereich` — Produktmandate anlegen, wechseln, abschliessen.

**Triage und Launch**

- `ist-das-ein-problem` — Schnelle Kurzantwort fuer PM-Fragen; fuenf Minuten, mit Quellenangabe.
- `launch-pruefung` — Vollstaendige rechtliche Launch-Freigabepruefung mit Ampel-Status.
- `feature-risikobewertung` — Tiefgehende Risikobewertung fuer ein einzelnes Feature oder einen Produktbereich.

**Spezialthemen**

- `impressum-pflicht` — Impressumspflicht nach §§ 5 und 6 DDG und § 18 MStV; konformer Impressumstext; Abmahnrisiken.
- `preisangaben` — PAngV 2022: Gesamtpreise, Grundpreise, Streichpreise, 30-Tage-Niedrigstpreisregel.
- `werbeaussagen-pruefung` — Werbebehauptungen auf UWG-, Health-Claims- und ESG-Risiken pruefen.

## Worauf besonders achten

- **Impressumspflicht gilt auch fuer Social-Media-Profile** — Gewerblich genutzte Profile bei Instagram, LinkedIn oder X muessen vollstaendiges Impressum enthalten oder klar darauf verlinken.
- **30-Tage-Regel ist keine Empfehlung, sondern Pflicht** — Streichpreise muessen auf dem Niedrigstpreis der letzten 30 Tage vor Reduzierung basieren; Verstaesse sind abmahnbar.
- **KI-Features benoetigen KI-VO-Check** — Der AI Act gilt fuer KI-Systeme ab August 2026 in vollem Umfang; Hochrisiko-Systeme und verbotene Praktiken muessen vorab identifiziert werden.
- **Health Claims erfordern Zulassung** — Nicht zugelassene Gesundheitsversprechen sind ohne Ausnahme unzulaessig; Positivliste VO 1924/2006 ist abschliessend.
- **Risikokalibrierung ist Ausgangspunkt** — Ohne konfiguriertes Praxisprofil liefert das Plugin nur generische Ergebnisse; `produktrecht-kaltstart-interview` zuerst ausfuehren.

## Typische Fehler

- Impressum fehlt oder ist unvollstaendig (keine Rechtsform, kein Vertretungsberechtigter, keine USt-IdNr. bei Pflicht); erhoehtes Abmahnrisiko.
- Streichpreis-Aktion wird ohne Pruefung des Niedrigstpreises der letzten 30 Tage gestartet; PAngV-Verstoss.
- Feature mit KI-Komponente wird gelauncht ohne Pruefung, ob es als Hochrisiko-KI-System nach AI Act gilt.
- Werbeaussage zu Klimaneutralitaet oder Nachhaltigkeit wird nicht mit belastbaren Nachweisen unterlegt; Greenwashing-Abmahnrisiko.
- Launch-Pruefung wird als Checkliste abgehakt, ohne Risikokalibrierung und Eskalationsschwellen der eigenen Rechtsabteilung.

## Querverweise

- `dsa-dma-digitalregulierung` — Fuer DSA-Pflichten bei Online-Plattformen und VLOP-Einordnung.
- `europarecht-kompass` — Fuer EU-Rechtsquellen-Einordnung (Verordnung, Richtlinie) bei EU-Produktregulierung.
- `vertragsausfueller` — Fuer Lizenz- und Vertriebsvertraege im Produktkontext.

## Quellen und Aktualitaet

- Stand: 05/2026
- DDG §§ 5 und 6 in der geltenden Fassung
- PAngV 2022 in der geltenden Fassung
- UWG in der geltenden Fassung
- EU-Produktsicherheits-VO 2023/988 in der geltenden Fassung
- AI Act (EU) 2024/1689 in der geltenden Fassung
