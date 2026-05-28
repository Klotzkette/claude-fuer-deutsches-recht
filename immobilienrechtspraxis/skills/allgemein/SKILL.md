---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Immobilienrechtspraxis-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Immobilienrechtspraxis — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Immobilienrechtspraxis**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Werkzeuge für immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz; Vertragsprüfung gegen Playbook; Grundbuchanalyse; Sachverhaltsermittlung; Mieteranfragen mit BGH-Verankerung; Case Management; projektbasierte Arbeitsweise mit AVV-Prüfung.

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
| `case-management` | Fallmanagement für Immobilienrechtsmandate: Verfahrensstand, Fristen, Dokumente im Überblick. Normen: WEG, §§ 535 ff. 873 ff. BGB, GrEStG. Prüfraster: Fristenliste, offene Anträge, Dokumentenstruktur. Output:… |
| `grundbuchanalyse` | Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten. Normen: §§ 873 ff. 1105 ff. 1191 ff. BGB, GBO. Prüfraster: Abteilung I bis III, Widersprueche, Rangverhältnisse,… |
| `mieteranfragen-bearbeitung` | Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kündigung. Normen: §§ 535 536 556 573 BGB, WEG. Prüfraster: Anfragetyp, Rechtsgrundlage, Fristen, Handlungspflichten. Output:… |
| `projekt-arbeitsweise` | Projektmethodik für Immobilienrechtsprojekte: Strukturierung komplexer Mandate mit mehreren Beteiligten. Normen: BGB, WEG, GrEStG. Prüfraster: Beteiligte, Zeitplan, Meilensteine, Dokumentenstruktur. Output: Projektplan… |
| `sachverhaltsermittlung` | Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhältnisse, Vertragshistorie, Beweismittel. Normen: §§ 873 ff. BGB, GBO, WEG. Prüfraster: Grundbuch, Kaufvertrag, Mietvertrag, Beweismittelkatalog.… |
| `vertragserstellung-musterbasiert` | Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss. Normen: §§ 433 ff. 535 ff. 873 BGB, WEG, GrEStG. Prüfraster: Musterauswahl, Anpassung an Sachverhalt, Notarerfordernis.… |
| `vertragspruefung-playbook` | Immobilienrechtliche Vertraege nach standardisiertem Playbook prüfen: Kaufvertrag, Grundschuld, WEG. Normen: §§ 433 ff. 873 ff. BGB, WEG, GrEStG, GBO. Prüfraster: Playbook-Checkliste, Risikoklauseln, Notar- und… |

## Worum geht es?

Das Plugin unterstuetzt immobilienrechtliche Rechtsabteilungen bei der taeglich anfallenden Vertragsarbeit, der Grundbuch- und Sachverhaltsanalyse sowie der Verwaltung von Miet- und WEG-Mandaten. Es verbindet musterbasierte Vertragserstellung mit einem strukturierten Pruefungs-Playbook und integriert den gesetzlichen Rahmen aus BGB, WEG, GBO und GrEStG.

Zielgruppe sind Unternehmensjuristen und Rechtsanwaelte, die Immobilienprojekte mit mehreren Beteiligten und langer Laufzeit koordinieren muessen. Das Plugin setzt auf eine projektartige Arbeitsweise, die Fristen, Dokumente und Beteiligte in einer Gesamtschau haelt.

## Wann brauchen Sie diese Skill?

- Sie starten ein neues Immobilienrechtsmandat und muessen Eigentumsverhaeltnisse, Grundbuchbelastungen und Vertragshistorie systematisch erfassen.
- Sie wollen einen Kaufvertrag, Mietvertrag oder WEG-Beschluss auf Musterbasis erstellen oder nach einem Playbook auf Risiken pruefen.
- Ein Mieter oder WEG-Eigentumer stellt eine Anfrage zu Instandsetzung, Betriebskosten oder Kuendigung.
- Sie muessen mehrere Beteiligte, Fristen und Meilensteine in einem komplexen Immobilienprojekt steuern.
- Sie benoetigen einen Sachverhalts-Ermittlungsbericht als Grundlage fuer die rechtliche Bewertung.

## Fachbegriffe (kurz erklaert)

- **Grundbuch** — Oeffentliches Register der Eigentumsverhaeltnisse und dinglichen Belastungen eines Grundstuecks; gefuehrt nach der Grundbuchordnung (GBO).
- **Grundschuld** — Dingliches Sicherungsrecht am Grundstueck nach §§ 1191 ff. BGB; haufig Sicherungsmittel fuer Bankdarlehen.
- **WEG** — Wohnungseigentumsgesetz; regelt die Gemeinschaft der Wohnungseigentuemer, Beschlusse und Verwaltung.
- **Dienstbarkeit** — Beschraenkung des Eigentuemers zugunsten Dritter (z. B. Wegerecht, Niesbrauch) nach §§ 1018 ff. BGB.
- **GrEStG** — Grunderwerbsteuergesetz; regelt Steuertatbestand beim Eigentumsubergang.
- **Notarerfordernis** — Formpflicht: Kaufvertraege ueber Grundstuecke beduerften nach § 311b BGB notarieller Beurkundung.
- **Playbook** — Standardisierter Pruefkatalog der Rechtsabteilung mit Risikoklauseln und Ampelbewertung.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; relevant beim KI-Einsatz in der Mandatsbearbeitung.

## Rechtsgrundlagen

- §§ 433 ff. BGB — Kaufvertrag
- §§ 535 ff. BGB — Mietrecht
- §§ 873 ff. BGB — Eigentumsuebertragung und dingliche Rechte
- §§ 1018 ff. BGB — Grunddienstbarkeiten
- §§ 1105 ff. BGB — Reallast
- §§ 1191 ff. BGB — Grundschuld
- WEG — Wohnungseigentumsgesetz
- GBO — Grundbuchordnung
- GrEStG — Grunderwerbsteuergesetz

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren (Kaeufer, Verkaeufer, Vermieter, WEG-Verwalter, Rechtsabteilung).
2. Phase des Mandats bestimmen (Sachverhaltsaufnahme, Vertragserstellung, Vertragspruefung, laufende Verwaltung, Streitfall).
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Fristen pruefen (Kaufvertragsfrist, Kuendigungsfristen, GrESt-Zahlungsfristen).
5. Bei Projekten mit mehreren Beteiligten: Projektplan anlegen und Case Management aktivieren.

## Skill-Tour (was gibt es hier?)

- `case-management` — Fallmanagement fuer Immobilienrechtsmandate: Verfahrensstand, Fristen und Dokumente im Ueberblick.
- `grundbuchanalyse` — Grundbuchauszug analysieren: Eigentuemer, Belastungen, Grundschulden, Dienstbarkeiten und Rangverhaeltnisse.
- `mieteranfragen-bearbeitung` — Mieteranfragen im Miet- und WEG-Recht bearbeiten: Instandsetzung, Betriebskosten, Kuendigung.
- `projekt-arbeitsweise` — Projektmethodik fuer Immobilienrechtsprojekte mit mehreren Beteiligten, Meilensteinen und Dokumentenstruktur.
- `sachverhaltsermittlung` — Sachverhalt in Immobilienrechtsstreitigkeiten ermitteln: Eigentumsverhaeltnisse, Vertragshistorie, Beweismittel.
- `vertragserstellung-musterbasiert` — Immobilienrechtliche Vertraege auf Musterbasis erstellen: Kaufvertrag, Mietvertrag, WEG-Beschluss.
- `vertragspruefung-playbook` — Immobilienrechtliche Vertraege nach standardisiertem Playbook pruefen: Kaufvertrag, Grundschuld, WEG.

## Worauf besonders achten

- **Formzwang**: Kaufvertraege ueber Grundstuecke beduerften notarieller Beurkundung (§ 311b BGB); Formmangel fuehrt zu Nichtigkeit des gesamten Vertrages.
- **Grundbuchstand vor Vertragsschluss pruefen**: Nicht eingetragene Belastungen und Widersprueche koennen Eigentumsuebergang erschweren.
- **WEG-Beschluesse**: Nicht ordnungsgemaesse Einberufung oder fehlende Mehrheiten fuehren zur Anfechtbarkeit; Fristen nach § 45 WEG beachten.
- **GrEStG-Grunderwerbsteuer**: Zahlungsfrist nach § 15 GrEStG; Unbedenklichkeitsbescheinigung Voraussetzung fuer Grundbucheintragung.
- **AVV beim KI-Einsatz**: Mandatsdaten duerfen nur in KI-Systeme eingegeben werden, wenn ein datenschutzkonformer AVV vorliegt.

## Typische Fehler

- Mustervertrag ohne Anpassung an Sachverhalt verwenden: fehlende Sondervereinbarungen zu Moebeln, Inventar oder Baumangeln fuehren spaeter zu Streit.
- Grundbuch-Abt. III (Grundschulden) nicht vollstaendig pruefen: ueberraschende Belastungen koernen Kaufpreis und Finanzierung gefaehrden.
- Kuendigungsfristen nach § 573c BGB verwechseln mit Kuendigungsgruenden nach § 573 BGB.
- WEG-Beschluesse ohne Protokollpruefung uebernehmen: Fehler in der Abstimmung sind nicht immer offensichtlich.
- Sachverhaltsermittlung und rechtliche Bewertung vermischen: Tatsachen erst vollstaendig erfassen, dann bewerten.

## Querverweise

- `kanzlei-allgemein` — Allgemeines Kanzlei-Workflow-Plugin fuer Fristen, Schriftsaetze und Mandatsmanagement.
- `zwangsverwaltung-zvg` — Bei Zwangsverwaltung und Zwangsversteigerung von Immobilien.
- `aktenauszug-gerichtsverfahren` — Fuer schnelle Einarbeitung in laufende Immobilienprozesse.
- `insolvenzverwaltung` — Wenn Immobilien Teil einer Insolvenzmasse sind.
- `selbstvertreter-amtsgericht` — Wenn Mieter ohne Anwalt im Mietprozess vor dem Amtsgericht auftreten.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- BGH-Rechtsprechung zu §§ 535 ff. BGB (Mietrecht) und WEG laufend beachten
