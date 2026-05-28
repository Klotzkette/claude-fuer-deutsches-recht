---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Verfassungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Verfassungsrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verfassungsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde.

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
| `bverfg-rechtsprechung-recherchieren` | BVerfG-Rechtsprechung zu konkreter Verfassungsfrage recherchieren und für Schriftsatz aufbereiten. BVerfGG Art. 93 GG BVerfG-Judikatur. Prüfraster: Leitsaetze Tragsaetze obiter dicta Randnummern-Suche Weiterführung… |
| `formelle-verfassungsmaessigkeit` | Formelle Verfassungsmäßigkeit eines Gesetzes prüfen: Kompetenz Verfahren Form. Art. 70 ff. GG Gesetzgebungskompetenzen Art. 76 ff. GG Gesetzgebungsverfahren. Prüfraster: Gesetzgebungskompetenz Bund/Land Art. 70-74 GG… |
| `gesetzentwurf-gg-konformitaet-pruefen` | Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG… |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz des Bundes oder eines Landes für konkretes Regelungsvorhaben prüfen. Art. 70 71 72 73 74 GG Kompetenzkatalog. Prüfraster: ausschließliche konkurrierende Gesetzgebung Abweichungsgesetzgebung… |
| `grundrechtspruefung` | Grundrechtsprüfung nach dem Drei-Stufen-Schema durchführen wenn staatliche Massnahme Grundrecht beruehrt. Art. 1-19 GG Grundrechte Art. 20 Abs. 3 GG Verhältnismäßigkeit. Prüfraster: Schutzbereich Eingriff… |
| `verfassungsbeschwerde-entwurf` | Verfassungsbeschwerde beim BVerfG nach §§ 90 ff. BVerfGG formulieren wenn Grundrechtsverletzung durch öffentliche Gewalt geltend gemacht wird. §§ 90 93 BVerfGG Art. 93 Abs. 1 Nr. 4a GG. Prüfraster:… |
| `verfassungsrechtliche-pruefung` | Verfassungsrechtliche Prüfung einer Massnahme oder Norm umfassend durchführen. Art. 1-20 GG Grundrechte Staatsorganisationsrecht. Prüfraster: formelle Verfassungsmäßigkeit Grundrechtsprüfung Staatsstrukturprinzipien… |
| `verhaeltnismaessigkeit` | Verhältnismäßigkeitsprüfung für staatliche Massnahmen oder Gesetze durchführen. Art. 20 Abs. 3 GG Rechtsstaatsprinzip BVerfG-Stufenschema. Prüfraster: legitimer Zweck Geeignetheit Erforderlichkeit Angemessenheit… |

## Worum geht es?

Dieses Plugin unterstuetzt Spezialkanzleien, Wissenschaftler und Rechtsanwaelte bei verfassungsrechtlichen Pruefungen nach dem Grundgesetz. Es deckt alle Kernbereiche ab: Gesetzgebungskompetenz (Art. 70-74 GG), formelle Verfassungsmaessigkeit, Grundrechtspruefung im Drei-Schritt, Verhaeltnismaessigkeitspruefung, Gesetzentwurfs-Pruefung auf GG-Konformitaet und Verfassungsbeschwerde-Formulierung nach §§ 90 ff. BVerfGG.

Das Plugin ist rechtsprechungsgetrieben: Es orientiert sich an BVerfG-Leitentscheidungen und empfiehlt bei aktuellen Fragen die Live-Recherche auf bundesverfassungsgericht.de.

## Wann brauchen Sie diese Skill?

- Sie pruefen einen Gesetzentwurf auf Vereinbarkeit mit dem Grundgesetz vor Einleitung des Gesetzgebungsverfahrens.
- Sie formulieren eine Verfassungsbeschwerde nach §§ 90 ff. BVerfGG und benoetigen strukturierte Zulassungs- und Begruendungsanforderungen.
- Sie pruefen die Gesetzgebungskompetenz des Bundes oder eines Landes fuer ein konkretes Regelungsvorhaben.
- Eine staatliche Massnahme beeintraechtigt Grundrechte und Sie benoetigen eine strukturierte Pruefung (Schutzbereich, Eingriff, Rechtfertigung).
- Sie benoetigen BVerfG-Rechtsprechung zu einer verfassungsrechtlichen Frage fuer einen Schriftsatz.

## Fachbegriffe (kurz erklaert)

- **Schutzbereich** — Der sachliche und persoenliche Bereich, den ein Grundrecht schuetzt; muss eroeffnet sein, bevor ein Eingriff geprueft wird.
- **Eingriff** — Staatliche Massnahme, die in den Schutzbereich eines Grundrechts einwirkt; klassisch: unmittelbar, final, rechtsaktmaessig.
- **Verhaeltnismaessigkeit** — Verfassungsrechtlicher Grundsatz: Massnahme muss legitimen Zweck verfolgen, geeignet, erforderlich und angemessen sein.
- **Gesetzgebungskompetenz** — Grundsaetzlich bei den Laendern (Art. 70 GG); ausschliessliche Bundeskompetenzen Art. 73 GG; konkurrierende Bundeskompetenzen Art. 74 GG.
- **Wesensgehalt** — Unantastbarer Kernbestand jedes Grundrechts; auch im Kriegszustand nicht einschraenkbar (Art. 19 Abs. 2 GG).
- **Verfassungsbeschwerde** — Rechtsbehelfsmoeglichkeit fuer jede Person gegen Verletzung eines Grundrechts durch oeffentliche Gewalt (Art. 93 Abs. 1 Nr. 4a GG).
- **Normenkontrolle** — Abstrakte (Art. 93 Abs. 1 Nr. 2 GG) oder konkrete (Art. 100 GG) Pruefung von Gesetzen auf Verfassungskonformitaet.

## Rechtsgrundlagen

- Art. 1-19 GG — Grundrechte
- Art. 19 Abs. 2 GG — Wesensgehaltgarantie
- Art. 20 Abs. 3 GG — Rechtsstaatsprinzip und Verhaeltnismaessigkeit
- Art. 70-74 GG — Gesetzgebungskompetenzen Bund und Laender
- Art. 76-82 GG — Gesetzgebungsverfahren
- Art. 93 GG — Zustaendigkeit BVerfG
- Art. 100 GG — Konkrete Normenkontrolle
- §§ 90 ff. BVerfGG — Verfassungsbeschwerde

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Pruefungsanlass (Gesetzentwurf, staatliche Massnahme, Verfassungsbeschwerde), Verfahrensstadium.
2. Phase des Mandats bestimmen: Kompetenzpruefung, formelle Pruefung, Grundrechtspruefung, Verhaeltnismaessigkeit oder Beschwerde-Entwurf.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Verfassungsbeschwerde-Frist ein Monat ab Zustellung (§ 93 Abs. 1 BVerfGG) bzw. ein Jahr bei Gesetzesbeschwerden.
5. Anschluss-Skill bestimmen: nach Grundrechtspruefung folgt Verhaeltnismaessigkeitspruefung; nach Gesamtpruefung ggf. Verfassungsbeschwerde-Entwurf.

## Skill-Tour (was gibt es hier?)

**Umfassende Pruefung**

- `verfassungsrechtliche-pruefung` — Umfassende Verfassungspruefung einer Massnahme oder Norm; Oberbegriff-Skill mit Verweis auf Spezialisten-Skills.
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf auf GG-Konformitaet pruefen vor Einleitung des Gesetzgebungsverfahrens.

**Kompetenz und formelle Pruefung**

- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz des Bundes oder Landes: ausschliesslich, konkurrierend, Abweichungsgesetzgebung.
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit pruefen: Kompetenz, Verfahren (Art. 76-78 GG) und Ausfertigung (Art. 82 GG).

**Grundrechte und Verhaeltnismaessigkeit**

- `grundrechtspruefung` — Grundrechtspruefung im Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung mit Wesensgehalt-Pruefung.
- `verhaeltnismaessigkeit` — Verhaeltnismaessigkeitspruefung: legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit.

**Verfassungsbeschwerde**

- `verfassungsbeschwerde-entwurf` — Verfassungsbeschwerde nach §§ 90 ff. BVerfGG: Zulaessigkeit (Beschwerdefuehrer, Objekt, Rechtswegerschoepfung, Frist) und Begruendung.

**Rechtsprechungsrecherche**

- `bverfg-rechtsprechung-recherchieren` — BVerfG-Rechtsprechung zu konkreter Frage recherchieren und fuer Schriftsatz aufbereiten.

## Worauf besonders achten

- **Rechtswegerschoepfung ist Voraussetzung fuer Verfassungsbeschwerde.** Vor Einlegung der Verfassungsbeschwerde muessen alle ordentlichen und verwaltungsgerichtlichen Rechtsbehelfe ausgeschoepft sein (§ 90 Abs. 2 BVerfGG).
- **Einmonats-Frist laeuft ab Zustellung, nicht ab Kenntnis.** Verfassungsbeschwerde ist nach § 93 Abs. 1 BVerfGG an harte Fristen gebunden; keine Wiedereinsetzung ohne triftigen Grund.
- **Schutzbereich und Eingriff sorgfaeltig trennen.** Haeufiger Fehler ist es, den Eingriff in der Schutzbereichspruefung zu behandeln; die Struktur des Drei-Schritt ist in Schriftsaetzen streng einzuhalten.
- **Konkrete Normenkontrolle nur durch Gerichte.** Buerger und Behoerden koennen keine Normenkontrolle nach Art. 100 GG beantragen; nur Gerichte koennen vorlegen.
- **Aktuelle BVerfG-Rechtsprechung immer live recherchieren.** Das Plugin verweist auf bundesverfassungsgericht.de; jedes Gebiet hat potentiell neuere Entscheidungen als der interne Wissensstand.

## Typische Fehler

- Verhaeltnismaessigkeitspruefung wird ohne Herausarbeitung eines legitimen Zwecks begonnen; Pruefung ist dann unvollstaendig.
- Verfassungsbeschwerde wird eingereicht ohne Rechtswegerschoepfung; BVerfG nimmt sie nicht zur Entscheidung an.
- Grundrechtspruefung vermischt Schutzbereich und Eingriff; strukturelles Problem im Schriftsatz.
- Gesetzgebungskompetenz wird nur fuer den Bund geprueft ohne Sperrwirkung und Abweichungsgesetzgebung zu beachten.
- BVerfG-Judikatur aus den 1990er Jahren wird ohne Ueberpruefung auf Weitergeltung angewendet; Rechtsprechung kann sich geaendert haben.

## Querverweise

- `jurastudium` — Fuer Studierende die Verfassungsrecht fuer das Staatsexamen ueben wollen.
- `subsumtions-pruefer` — Fuer die mechanische Subsumtion einzelner Verfassungsrechtsnormen im Vier-Schritt.
- `gesellschaftsrecht` — Wenn Verfassungsrecht im Kontext von Unternehmensrecht (z.B. Berufsfreiheit Art. 12 GG) relevant wird.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (GG, BVerfGG)
- Leitentscheidungen: bundesverfassungsgericht.de (Lueith, Volkszaehlung, Apotheken-Urteil, Kalkar, Elfes); aktuelle Recherche empfohlen
