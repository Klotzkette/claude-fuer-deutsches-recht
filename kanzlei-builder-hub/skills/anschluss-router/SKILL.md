---
name: anschluss-router
description: "Einstieg, Schnelltriage und Fallrouting im Kanzlei Builder Hub-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständi..."
---

# Kanzlei-Builder-Hub — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 51 Mindestversicherung sofort, FAO § 4 Fachanwalt-Antrag 3-Jahres-Frist (10 % Mindestumfang), GwG-Risikoanalyse jährlich, beA Pflichtnutzung seit 01.01.2022.
- Tragende Normen verifizieren: BRAO §§ 5, 7, 14, 27, 43 ff., 49b, 51 (Berufshaftpflicht), BORA, FAO, RVG §§ 1 ff., GwG §§ 2, 10, 11, 43 (Kanzlei als Verpflichteter), DSGVO, beA-Bedingungen, Steuerrecht (EStG, UStG, GewStG) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Kanzleigründer, Kammer, BRAK, Versicherer (Berufshaftpflicht), Mandant, Steuerberater, IT-Dienstleister (beA, RA-MICRO/AnNoText).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Kanzleihandbuch, Datenschutz-Konzept, Geldwäsche-Risikoanalyse, Mandatsvertrag, Honorarvereinbarung, Versicherungspolice, Sozietätsvertrag, beA-Konfiguration — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Kanzlei Builder Hub**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung.

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
| `automatischer-aktualisierer` | Plugins und Skills in der KI-Anwaltskanzlei automatisch aktualisieren: neue Norm-Versionen, Rechtsprechungsaenderungen. Normen: technisch/intern. Prüfraster: aeltere Versionen identifizieren, Update-Prioritaet,… |
| `deaktivieren` | Einzelne Skills oder Plugins temporaer deaktivieren ohne Deinstallation. Normen: technisch/intern. Prüfraster: Abhaengigkeiten, Deaktivierungsumfang, Reaktivierungsweg. Output: Deaktivierungsbestätigung. Abgrenzung:… |
| `deinstallieren` | Plugins oder Skills vollständig deinstallieren: Abhaengigkeitsprüfung, Datensicherung. Normen: technisch/intern. Prüfraster: Abhaengigkeitscheck, Datensicherung vor Löschung, Bestätigung. Output:… |
| `fundstellenglattzieher` | Normen- und Rechtsprechungszitate in Schriftsaetzen und Skills vereinheitlichen: einheitliche Zitierweise. Normen: allgemein BRAO. Prüfraster: Normzitat-Format, BGH-Aktenzeichen, Quellenangaben. Output: Text mit… |
| `kanzlei-builder-hub-anpassen` | Kanzlei-Builder-Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows. Normen: technisch/intern. Prüfraster: Anpassungsumfang, Kompatibilitaet, Testbedarf. Output:… |
| `kanzlei-builder-hub-kaltstart-interview` | Kaltstart-Interview für den Kanzlei-Builder-Hub: Kanzleiprofil, Rechtsgebiete, gewuenschte Plugins. Normen: technisch/intern. Prüfraster: Rechtsgebietsabdeckung, Mandantenstruktur, Technikvoraussetzungen. Output:… |
| `playbook-aus-eigenen-daten` | Kanzleieigenes Playbook aus vorhandenen Musterdokumenten und Vorlagen automatisch erstellen. Normen: technisch/intern, BRAO. Prüfraster: Dokumentenqualitaet, Kategorisierung, Normverankerung. Output: Kanzlei-Playbook… |
| `skill-installierer` | Neue Skills in der KI-Anwaltskanzlei installieren: Verfuegbarkeitscheck, Abhaengigkeiten, Konfiguration. Normen: technisch/intern. Prüfraster: Kompatibilitaet, Abhaengigkeitsprüfung, Testlauf. Output:… |
| `skill-verwalter` | Übersicht und Verwaltung aller installierten Skills: Status, Version, Abhaengigkeiten. Normen: technisch/intern. Prüfraster: aktive Skills, deaktivierte Skills, Update-Bedarf. Output: Skills-Verwaltungsuebersicht.… |
| `skills-qualitaetspruefung` | Qualitaet installierter Skills prüfen: Normaktualitaet, Description-Qualitaet, Struktur-Compliance. Normen: technisch/intern, SKILL.md-Schema. Prüfraster: Description-Laenge, Normverankerung,… |
| `verwandte-skills-vorschlag` | Verwandte Skills zu einem Mandat oder Rechtsproblem vorschlagen: Ergaenzungsempfehlungen. Normen: technisch/intern. Prüfraster: Rechtsgebiet, Verfahrensphase, Mandantentyp. Output: Vorschlagsliste verwandter Skills.… |
| `verzeichnis-durchsuchen` | Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen. Normen: technisch/intern. Prüfraster: Suchbegriff, Kategoriefilter, Ergebnispriorisierung. Output: Suchergebnisliste Skills. Abgrenzung: nicht… |

## Worum geht es?

Der Kanzlei-Builder-Hub ist die Steuerzentrale für Installation, Verwaltung und Qualitaetssicherung von Skills und Plugins in der KI-gestuetzten Kanzleiumgebung. Er fuehrt vor dem Deployment ein Security-Review-Gate durch, das Community-Skills auf Sicherheit, Normkonformitaet und Qualitaet prüft, bevor sie produktiv genutzt werden.

Der Hub ermoeglicht ausserdem die Erstellung kanzleieigener Playbooks aus vorhandenen Musterdokumenten sowie die gezielte Suche und Verwaltung des Skill-Verzeichnisses. Er richtet sich an Kanzleiinhaber, IT-Verantwortliche und Kanzleimanager, die ihre KI-Kanzleiumgebung strukturiert aufbauen und pflegen wollen.

## Wann brauchen Sie diese Skill?

- Sie wollen erstmals den Hub einrichten und Ihr Kanzleiprofil mit Rechtsgebieten und Technikvoraussetzungen erfassen.
- Sie suchen neue Community-Skills für ein bestimmtes Rechtsgebiet und moechten diese vor dem Einsatz sicherheitsprufen.
- Ein installierter Skill soll aktualisiert, temporaer deaktiviert oder vollstaendig deinstalliert werden.
- Sie wollen aus Ihren eigenen Musterdokumenten ein kanzleispezifisches Playbook generieren.
- Sie benoetigen eine Qualitaetspruefung aller installierten Skills auf Normaktualitaet und Strukturkonformitaet.

## Fachbegriffe (kurz erklaert)

- **Security-Review-Gate** — Strukturiertes Prüfverfahren, das vor der Freigabe eines Community-Skills Sicherheit, Normverankerung und Qualitaet bewertet.
- **Plugin** — Zusammenschluss mehrerer thematisch verwandter Skills zu einem Funktionspaket für ein Rechtsgebiet oder einen Workflow.
- **Skill** — Einzelne spezialisierte Anleitung in einer SKILL.md-Datei, die einen definierten Arbeitsschritt abdeckt.
- **Playbook** — Kanzleispezifischer Prüf- und Arbeitskatalog, der aus eigenen Musterdokumenten automatisch erstellt wird.
- **Kaltstart-Interview** — Strukturiertes Erstgespraech zur Erfassung von Kanzleiprofil, Rechtsgebieten und Konfigurationsparametern.
- **Fundstelle** — Normzitat oder Rechtsprechungsnachweis; der Hub prüft deren einheitliche Zitierweise.

## Rechtsgrundlagen

- § 43a BRAO — Allgemeine Berufspflichten des Rechtsanwalts (Sorgfalt, Verschwiegenheit)
- § 43e BRAO — Dienstleister-Regelung: Berufsrechtliche Anforderungen an IT-Dienstleister der Kanzlei
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag bei externen Dienstleistern
- Art. 32 DSGVO — Technische und organisatorische Maßnahmen

## Schritt-für-Schritt: Einstieg ins Plugin

1. Kanzleiprofil und Rechtsgebiete im Kaltstart-Interview erfassen.
2. Gewuenschte Skills oder Plugins im Verzeichnis suchen.
3. Security-Review-Gate vor Installation durchlaufen lassen.
4. Skill installieren und Abhaengigkeiten prüfen.
5. Qualitaetspruefung nach Installation; bei Bedarf anpassen oder deaktivieren.

## Skill-Tour (was gibt es hier?)

- `automatischer-aktualisierer` — Plugins und Skills automatisch auf neue Norm-Versionen und Rechtsprechungsaenderungen aktualisieren.
- `deaktivieren` — Einzelne Skills oder Plugins temporaer deaktivieren ohne vollstaendige Deinstallation.
- `deinstallieren` — Plugins oder Skills vollstaendig deinstallieren mit Abhaengigkeitspruefung und Datensicherung.
- `fundstellenglattzieher` — Normen- und Rechtsprechungszitate in Schriftsaetzen und Skills auf einheitliche Zitierweise bringen.
- `kanzlei-builder-hub-anpassen` — Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows.
- `kanzlei-builder-hub-kaltstart-interview` — Kaltstart-Interview: Kanzleiprofil, Rechtsgebiete und gewuenschte Plugins erfassen.
- `playbook-aus-eigenen-daten` — Kanzleieigenes Playbook aus vorhandenen Musterdokumenten automatisch generieren.
- `skill-installierer` — Neue Skills installieren mit Verfuegbarkeitscheck, Abhaengigkeitspruefung und Konfiguration.
- `skill-verwalter` — Übersicht und Verwaltung aller installierten Skills nach Status, Version und Abhaengigkeiten.
- `skills-qualitaetspruefung` — Installierte Skills auf Normaktualitaet, Description-Qualitaet und Strukturkonformitaet prüfen.
- `verwandte-skills-vorschlag` — Verwandte Skills zu einem Mandat oder Rechtsproblem als Ergaenzungsempfehlung vorschlagen.
- `verzeichnis-durchsuchen` — Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen.

## Worauf besonders achten

- **Security-Review-Gate zwingend**: Community-Skills ohne Prüfung können falsche Normen, erfundene Aktenzeichen oder datenschutzrechtliche Schwachstellen enthalten.
- **Abhaengigkeitspruefung vor Deinstallation**: Andere Skills oder Workflows können auf dem zu entfernenden Skill aufbauen.
- **Normaktualitaet regelmaessig prüfen**: Gesetze und Rechtsprechung ändern sich; veraltete Skills sind ein Haftungsrisiko.
- **Datensicherung vor Deinstallation**: Kanzleieigene Anpassungen gehen bei Deinstallation ohne Sicherung unwiederbringlich verloren.
- **Kaltstart nicht ueberspringen**: Ohne vollstaendiges Kanzleiprofil sind Rechtsgebiet-Filter und Kompatibilitaetspruefungen unzuverlaessig.

## Typische Fehler

- Community-Skills ohne Security-Review direkt in die Produktion uebernehmen.
- Bei der Deinstallation nicht auf abhaengige Workflows prüfen, was zu Folgefehlern fuehrt.
- Kanzleiprofil nach Rechtsgebietswechsel nicht aktualisieren, sodass Skill-Vorschlaege nicht mehr passen.
- Fundstellen verschiedener Zitierweisen im selben Schriftsatz mischen (z. B. BGH-Aktenzeichen ohne einheitliches Format).
- Qualitaetspruefung nur bei Neuinstallation, nicht nach Gesetzesaenderungen durchfuehren.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 32 DSGVO
- § 203 StGB
- Art. 28 DSGVO
- Art. 30 DSGVO
- Art. 35 DSGVO
- § 4 KSchG
- Art. 25 DSGVO
- Art. 17 DSGVO
- § 5 KSchG
- § 29 VwVfG
- § 102 BetrVG
- § 17 MuSchG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
