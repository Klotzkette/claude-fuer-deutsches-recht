# Megaprompt: rechtsberatungsstelle

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 54 Skills des Plugins `rechtsberatungsstelle`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Rechtsberatungsstelle (RDG): ordnet Rolle (Hilfesuchender, Berater, Amtsgericht), marki…
2. **bono-erstpruefung-und-mandatsziel** — Bono: Erstprüfung, Rollenklärung und Mandatsziel im Rechtsberatungsstelle.
3. **anleiter-pruefwarteschlange** — 'Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an…
4. **anpassen** — Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte…
5. **anschluss-router** — Einstieg, Schnelltriage und Fallrouting im Rechtsberatungsstelle-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken…
6. **einfache-sprache-briefe** — Anwalts- und Behördenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einsch…
7. **entwurf-einarbeitung-einfache-sprache** — Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspru…
8. **erzeugung-leitfaden-erstellen-mandanten** — Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag …
9. **fristen-fristenkontrolle-rdg** — Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisiere…
10. **kaltstart-interview** — Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester st…
11. **leitfaden-erstellen** — Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen…
12. **mandant-aufnahme** — Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und mu…
13. **mandanten-kommunikations-log** — Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsg…
14. **mandantenbrief-memo-rbs-beratungshilfe** — Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis de…
15. **memo** — Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) m…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Rechtsberatungsstelle (RDG): ordnet Rolle (Hilfesuchender, Berater, Amtsgericht), markiert Frist (Beratungshilfe-Antrag vor Tätigkeit), wählt Norm (RDG, BeratungshilfeG, Prozesskostenhilfe ZPO §§ 114 ff.) und Zuständigkeit (Amtsgericht), leitet zum passenden Spezi..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Rechtsberatungsstelle** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anlaufstellen-beweislast-anleiter-bono` — Anlaufstellen Beweislast Anleiter Bono
- `anleiter-formular-portal-und-einreichung` — Anleiter Formular Portal und Einreichung
- `anleiter-pruefwarteschlange` — Anleiter Pruefwarteschlange
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `bono-erstpruefung-und-mandatsziel` — Bono Erstpruefung und Mandatsziel
- `briefe-erstberatung-rdg-konform` — Briefe Erstberatung RDG Konform
- `einarbeitung` — Einarbeitung
- `einfache-sprache-briefe` — Einfache Sprache Briefe
- `entwurf-einarbeitung-einfache-sprache` — Entwurf Einarbeitung Einfache Sprache
- `erstberatung-rdg-grenzen-und-triage` — Erstberatung RDG Grenzen und Triage
- `erzeugung-leitfaden-erstellen-mandanten` — Erzeugung Leitfaden Erstellen Mandanten
- `fristen-fristenkontrolle-rdg` — Fristen Fristenkontrolle RDG
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Rechtsberatungsstelle sind RDG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `bono-erstpruefung-und-mandatsziel`

_Bono: Erstprüfung, Rollenklärung und Mandatsziel im Rechtsberatungsstelle._

# Bono: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Bono Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Rechtsberatungsstelle** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Pruefungen und Leistungspunktsystem.
- `§ 16 HRG` — Pruefungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Pruefungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Bono: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** RDG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Bono** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `anleiter-pruefwarteschlange`

_'Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell 'formelle Prüfwarteschlange' gewählt wurde; andernfalls inaktiv. Lädt, wenn der Supervisor sehen möchte, w..._

# Supervisoren-Prüfwarteschlange (Optional)

## Eingaben

- **Keine** bei Standardaufruf (zeigt, was wartet)
- **`--freigeben [id]`** — Eintrag freigeben
- **`--zurück [id] "Hinweis"`** — Eintrag mit Kommentar zurückschicken
- **`--bearbeiten [id]`** — Eintrag inline bearbeiten, dann freigeben

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 6 Abs. 2 RDG** — Aufsichtspflicht des begleitenden Rechtsanwalts/der begleitenden Rechtsanwältin: Die Aufsicht muss inhaltlich effektiv sein. Eine Warteschlange mit dokumentierter Prüfung ist eine institutionelle Umsetzung dieser Pflicht.
- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht: Die Warteschlange enthält vertrauliche Mandantendaten; sie ist ausschließlich supervisor-zugänglich und nicht für Studierende einsehbar (außer für ihren eigenen Eintrag nach Freigabe/Rücksendung).
- **§ 203 Abs. 3 StGB** — Gehilfenstatus der Studierenden: Der Supervisor als aufsichtführender Rechtsanwalt/Rechtsanwältin ist strafrechtlich mitverantwortlich für den sachgerechten Umgang mit Mandantendaten.
- **§ 50 BRAO** — Handakten: Freigegebene Dokumente sind Teil der Handakte und unterliegen der 5-jährigen Aufbewahrungspflicht.
- **DSGVO Art. 5, 32** — Sicherheit der Verarbeitung: Die Prüfwarteschlange verarbeitet personenbezogene Mandantendaten; technische und organisatorische Maßnahmen (Zugangsbeschränkung, Verschlüsselung) sind erforderlich.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Konfigurationsprüfung

Zuerst: Klinik-Konfiguration (CLAUDE.md) → Supervisionsmodell prüfen. Falls NICHT "formelle Prüfwarteschlange":

> "Die Beratungsstelle ist für das Supervisionsmodell [konfigurierbare Flags / leichte Begleitung] eingerichtet — es gibt keine formelle Prüfwarteschlange. [Supervisor] begleitet Entwürfe über [die bestehende Betreuungsstruktur]. Um zur formellen Prüfwarteschlange zu wechseln: CLAUDE.md → Supervisionsmodell auf 'formelle Prüfwarteschlange' setzen."

Falls formelle Prüfwarteschlange AKTIVIERT: Flag-Trigger lesen und fortfahren.

### Die Warteschlange

Liegt in `references/review-queue.yaml`. Jeder Eintrag:

```yaml
- id: P-001
 typ: "entwurf" # aufnahme | entwurf | memo | status | mandantenbrief
 mandant: "[Name oder ID]"
 studierender: "[Name]"
 eingereicht: [Zeitstempel]
 flags:
 - regel: "Gerichtliche Einreichung"
 detail: "Klageschrift AG — immer in Warteschlange"
 inhaltspfad: "[Pfad zum Dokument]"
 status: "ausstehend" # ausstehend | freigegeben | bearbeitet-freigegeben | zurückgeschickt
```

### Was wartet (Standard-Anzeige)

```markdown

## Prüfwarteschlange — [Datum]

**Ausstehend:** [N] | **Ältester Eintrag:** [N] Stunden

### Fristgebunden (sofortige Prüfung)
| ID | Typ | Mandant | Studierender | Warum geflaggt | Wartet seit |
|---|---|---|---|---|---|

### Standard
[gleiche Tabelle]

### Nach Studierendem
[Aufschlüsselung — Muster erkennbar: wer reicht viel ein, wer sollte ein Gespräch bekommen]
```

### Eintrag prüfen

Vollständigen Inhalt anzeigen + Warum geflaggt + Notizen des Studierenden.

### Freigeben / Bearbeiten und Freigeben / Zurückschicken

- **Freigeben:** Status → freigegeben, Studierender informiert, protokolliert.
- **Bearbeiten und Freigeben:** Supervisor bearbeitet inline; die freigegebene Version ist die bearbeitete; Original im Protokoll erhalten, damit der Studierende den Unterschied sieht (Lehrmoment).
- **Zurückschicken:** Mit Hinweis. Studierender überarbeitet und reicht erneut ein.

## Beispiel

**Szenario:** Studierender Müller reicht einen Entwurf der Kündigungsschutzklage für Mandantin Erdem ein (AG Berlin). Da es sich um eine gerichtliche Einreichung handelt, wird der Entwurf automatisch in die Prüfwarteschlange eingestellt.

Supervisor sieht:
```
P-003 | entwurf | Erdem | Müller | Gerichtliche Einreichung — Klageschrift AG | 4 Stunden
```

Supervisor prüft den Inhalt. Ergänzt: "§ 4 KSchG-Frist: Bitte noch einmal prüfen ob der Zugang am 15.04.2026 korrekt dokumentiert ist." → Zurückschicken. Müller überarbeitet, reicht neu ein → P-003b.

## Risiken und typische Fehler

- **Prüfung pro forma:** Eine Prüfwarteschlange ohne inhaltliche Prüfung erfüllt § 6 Abs. 2 RDG nicht. Das Protokoll dokumentiert, dass tatsächlich geprüft wurde; es ersetzt nicht die Prüfung selbst.
- **Warteschlange als Flaschenhals:** Bei hoher Fallzahl und Fristdruck kann eine formelle Warteschlange zum Engpass werden. Supervisor muss Kapazitäten planen; dringende Fristen werden in der Warteschlange priorisiert angezeigt.
- **Datenschutz:** Die Warteschlange enthält sensitive Mandantendaten. Nur Supervisoren-Zugang; keine Ablage in unsicheren Systemen.
- **Zurückgeschickte Einträge nicht verfolgt:** Wenn ein Studierender einen zurückgeschickten Eintrag nicht überarbeitet und neu einreicht, bleibt die Arbeit hängen. Supervisor sollte offene Rücksendungen regelmäßig prüfen.

## Lehrfunktion der Warteschlange

Die Warteschlange ist auch Datenbasis. Muster in Rücksendungen ("Studierender X vergisst regelmäßig die Fristprüfung") ist ein Coaching-Gespräch. Muster in Bearbeitungen durch den Supervisor ("Alle Mahnschreiben sind zu lang") ist ein Update für das nächste Semester-Onboarding (`/einarbeitung`).

Der Vergleich Original/bearbeitet im Protokoll ist ein Lehrmoment: Der Studierende sieht, was der Supervisor geändert hat, und warum — sofern der Supervisor einen kurzen Kommentar hinzufügt.

## Quellenpflicht

Prüfentscheidungen werden im Protokoll mit Datum und Supervisorenname dokumentiert. Begründungen für Rücksendungen sind inhaltlich und konkret (nicht "bitte nochmals prüfen", sondern "§ 4 KSchG-Frist: Zustellungsnachweis fehlt"). Das Protokoll ist Teil der Mandantenakte.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall und keine volljuristische Supervision nach § 6 Abs. 2 RDG.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 6 RDG
- § 203 StGB
- § 4 KSchG
- § 84 SGG
- § 74 AsylG
- § 70 VwG
- § 8 RDG
- Art. 30 DSGVO
- Art. 28 DSGVO
- § 3 RDG
- Art. 13 DSGVO
- § 3 AsylG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `anpassen`

_Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezifische Beratungsordnung. Prüfraster Rechtsgebiete einstellen,..._

# /anpassen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

1. Lade `CLAUDE.md` → aktuelles Profil anzeigen.
2. Frage: Welcher Abschnitt soll geändert werden?
3. Führe die gezielte Änderung durch – kein Full-Redo.
4. Aktualisierte Datei ausgeben.

---

### Beratungsstellenprofil anpassen

## Triage zu Beginn
1. Welcher Abschnitt des Profils soll angepasst werden: Semesterwechsel, Fachbereich, Prüfungsgates, Anleiter-Kontakt oder Gesetzesaenderung?
2. Hat sich die Rechtsgrundlage der Beratungsstelle geaendert (z.B. neues RDG, neue Kooperationsvereinbarung)?
3. Sind neue Studierende aufgenommen worden, die in die CLAUDE.md eingetragen werden muessen?
4. Soll gleichzeitig ein Fachbereichsleitfaden angepasst werden oder nur das Hauptprofil?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Anleitungsstruktur muss aktuell und wirksam sein; Semesterwechsel erfordert Profil-Update
- Art. 30 DSGVO — Verarbeitungsverzeichnis: bei Aenderung des Verarbeitungsumfangs zu aktualisieren
- §§ 43, 43a BRAO — Berufspflichten des Anleiters: kontinuierliche Aktualitaet der Organisationsunterlagen
- § 203 Abs. 4 StGB — Einbeziehung Dritter: bei Wechsel von Studierenden neue Verschwiegenheitsvereinbarungen pruefen

## Häufige Anpassungsszenarien

### 1. Semesterwechsel

> Welche Studierenden sind neu? Welche gehen? Wer übernimmt laufende Mandate?

Änderungen in `CLAUDE.md`:
- `Semester: [WS 2024/25]` → `[SS 2025]`
- Liste der aktiven Studierenden aktualisieren.
- Mandate-Übergabe: Verweis auf `/rechtsberatungsstelle:semester-übergabe`.

### 2. Neuen Fachbereich hinzufügen

Fachbereich in `CLAUDE.md` unter `Fachbereiche` ergänzen. Dann sofort:
> "Soll für den neuen Bereich auch ein Leitfaden erstellt werden? → `/rechtsberatungsstelle:leitfaden-erstellen [fachbereich]`"

### 3. Prüfungsgates ändern

> Welche Gates sollen geändert werden? Verschärfen oder lockern?

Tabelle in `CLAUDE.md` → `Aufsichtsmodell` anpassen. Hinweis: Lockerung nur bei nachgewiesener Erfahrung der Studierenden. § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche Anleitung.

### 4. Gesetzesänderungen einpflegen

Häufige Anlässe:
- Neue Regelbedarfsstufen SGB II ab 1. Januar (jährliche Anpassung per Regelbedarfsermittlungsgesetz).
- Neues BAMF-Merkblatt oder Entscheidungspraxis zu einem Herkunftsland.
- BGH-Urteil zur Schönheitsreparatur / Mieterhöhung.
- Änderungen im AsylG / AufenthG.

Pflegen Sie in `CLAUDE.md` → `Wichtige Normen` die relevante Änderung ein. Datum der Änderung festhalten.

### 5. Örtliche Kontakte aktualisieren

Jobcenter, Ausländerbehörde, BAMF-Außenstelle, Gericht, Dolmetscherdienste – Telefon, Zuständigkeit, Sprechzeiten.

### 6. Pädagogikhaltung ändern

Für ein bestimmtes Semester oder einen bestimmten Studierenden die Default-Haltung anpassen. Z. B.: "Für dieses Semester soll der Skill primär im Modus 'Anleiten' arbeiten, da alle Studierenden im ersten Klinik-Semester sind."

## Ablauf

### Schritt 1: Aktuelles Profil anzeigen

Gesamte `CLAUDE.md` ausgeben als Referenz.

### Schritt 2: Gezielter Abschnitt

Welcher Abschnitt? Optionen:
- `[A]` Beratungsstellentyp und Rechtsgrundlage
- `[B]` Fachbereiche
- `[C]` Aufsichtsmodell / Prüfungsgates
- `[D]` Pädagogikhaltung
- `[E]` Verschwiegenheitsorganisation
- `[F]` Örtliche Besonderheiten / Kontakte
- `[G]` Wichtige Normen (Gesetzesänderung)
- `[H]` Semester / Studierende
- `[L]` Fachbereichsleitfaden `guides/<name>.md`

### Schritt 3: Änderung durchführen

Nur den angegebenen Abschnitt bearbeiten. Alle übrigen Abschnitte unverändert lassen.

### Schritt 4: Änderungshistorie

Am Ende der `CLAUDE.md` einen Änderungseintrag hinzufügen:
```

## Änderungshistorie
- [Datum] Abschnitt [B] geändert: SGB IX / § 76b hinzugefügt. [Kürzel Anleiter]
- [Datum] Abschnitt [H] geändert: Semesterwechsel SS 2025. [Kürzel Anleiter]
```

## Risiken / typische Fehler

- **Versehentliches Löschen:** Beim Anpassen einzelner Abschnitte nie den Rest des Profils löschen. Immer vollständige Datei ausgeben, nicht nur den geänderten Abschnitt.
- **Gesetzesänderungen nicht eingepflegt:** Veraltertes Profil führt dazu, dass der Skill mit überholten Normen arbeitet (z. B. falsche Regelbedarfsstufen, falsche Fristen).
- **Mandate ohne Übergabe:** Beim Semesterwechsel sicherstellen, dass alle laufenden Mandate über `/rechtsberatungsstelle:semester-übergabe` übergeben werden, bevor das Profil auf das neue Semester umgestellt wird.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 6 RDG
- § 203 StGB
- § 4 KSchG
- § 84 SGG
- § 74 AsylG
- § 70 VwG
- § 8 RDG
- Art. 30 DSGVO
- Art. 28 DSGVO
- § 3 RDG
- Art. 13 DSGVO
- § 3 AsylG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `anschluss-router`

_Einstieg, Schnelltriage und Fallrouting im Rechtsberatungsstelle-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenstän..._

# Rechtsberatungsstelle — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Rechtsberatungsstelle**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe.

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
| `anleiter-pruefwarteschlange` | Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell "formelle… |
| `einarbeitung` | Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte… |
| `einfache-sprache-briefe` | Anwalts- und Behördenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behörde Gericht oder Gegenseite… |
| `entwurf` | Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6… |
| `formular-erzeugung` | Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behörde oder Gericht. BeratungsHiG Beratungsschein,… |
| `fristen` | Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard:… |
| `leitfaden-erstellen` | Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache.… |
| `mandant-aufnahme` | Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen.… |
| `mandanten-kommunikations-log` | Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO… |
| `mandantenbrief` | Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behörde oder Gericht vorbereiten.… |
| `memo` | Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit… |
| `recherche-start` | Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, Quellenprüfung, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Studierende… |
| `rechtsberatungsstelle-anpassen` | Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG,… |
| `rechtsberatungsstelle-kaltstart-interview` | Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet… |
| `semester-uebergabe` | Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des… |
| `status` | Fallstatuszusammenfassung nach Zielgruppe — mandantengerichtet (verständliche Sprache), intern (für den Supervisor) oder gerichts-/behördengerichtet (formale Schriftsatzform per Verfahrensordnung). Gleiche Fakten,… |

## Worum geht es?

Das Plugin unterstuetzt studentische und gemeinnuetzige Rechtsberatungsstellen bei der RDG-konformen Durchfuehrung ihrer Beratungsarbeit. Es bildet den gesamten Lebenszyklus eines Mandats ab: von der Erstaufnahme ueber die rechtliche Analyse und Schriftstueckerstellung bis zur sauberen Semesteruebergabe.

Besonderheit gegenueber Anwaltsplugins: Studierende sind keine zugelassenen Rechtsanwaelte. Die Beratungsleistung muss im Rahmen der nach § 6 RDG erlaubten unentgeltlichen Rechtsdienstleistungen bleiben. Alle wesentlichen Dokumente beduerften einer Anleiter-Freigabe. Das Plugin beruecksichtigt diese Aufsichtsstruktur mit einer optionalen Pruefwarteschlange.

## Wann brauchen Sie diese Skill?

- Ein neuer Studierender startet seine Arbeit in der Rechtsberatungsstelle und benoetigt Einarbeitung in Struktur, RDG-Grundlagen und Tools.
- Ein Mandant meldet sich mit einem konkreten Rechtsproblem und muss mit Sachverhalt, Fristen und Interessenkonfliktpruefung aufgenommen werden.
- Sie benoetigen Schriftsaetze, Antraege oder Mandantenbriefe in verstaendlicher Sprache für Mandanten mit sprachlichen Einschraenkungen.
- Das Semester endet und laufende Mandate sollen sauber an die naechste Studierendenkohorte uebergeben werden.
- Sie wollen das Plugin an Ihre Hochschule und deren Rechtsgebiete anpassen.

## Fachbegriffe (kurz erklaert)

- **RDG** — Rechtsdienstleistungsgesetz; regelt, wer ausserhalb der Anwaltschaft Rechtsdienstleistungen erbringen darf.
- **§ 6 RDG** — Erlaubnisnorm für unentgeltliche Rechtsdienstleistungen; Grundlage für studentische Beratungsstellen.
- **BeratungsHiG** — Beratungshilfegesetz; ermoeglicht einkommensschwachen Personen staatlich gefoerderte Rechtsberatung.
- **Anleiter** — Zugelassener Rechtsanwalt, der die Aufsicht ueber Studierende fuehrt und Arbeitsergebnisse freigibt.
- **Gutachtenmethode** — Juristische Analyse nach dem Schema Obersatz - Norm/Definition - Subsumtion - Ergebnis.
- **Interessenkonflikt** — Situation, in der Berater oder Kanzlei bereits die Gegenpartei vertreten; muss vor Mandatsannahme geprueft werden (§ 43a Abs. 4 BRAO entsprechend).
- **Pruefwarteschlange** — Optionale Aufsichtsstruktur, in der Arbeitsergebnisse auf Anleiter-Freigabe warten, bevor sie den Mandanten oder Gerichten zugehen.

## Rechtsgrundlagen

- § 2 RDG — Rechtsdienstleistungs-Begriff
- § 3 RDG — Erlaubnisvorbehalt
- § 6 RDG — Unentgeltliche Rechtsdienstleistungen
- § 43a BRAO — Allgemeine Berufspflichten (Verschwiegenheit, Interessenkonflikt; entsprechend anwendbar)
- BeratungsHiG — Beratungshilfegesetz
- DSGVO Art. 6 Abs. 1 und Art. 13 — Datenschutz bei der Mandatsbearbeitung
- BDSG § 26 — Datenschutz bei studentischen Arbeitnehmerverhaeltnissen

## Schritt-für-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview durchfuehren und Plugin an Hochschule und Rechtsgebiete anpassen.
2. Neue Studierende einarbeiten (Semester-Start).
3. Mandanten aufnehmen: Sachverhalt, Fristen, Interessenkonflikt und Beratungsberechtigung pruefen.
4. Passenden Skill auswaehlen (Memo, Entwurf, Mandantenbrief, einfache Sprache, Formular).
5. Ergebnis in Pruefwarteschlange stellen; nach Anleiter-Freigabe versenden oder weitergeben.

## Skill-Tour (was gibt es hier?)

- `anleiter-pruefwarteschlange` — Supervisoren-Pruefwarteschlange für studentische Arbeitsergebnisse vor Anleiter-Freigabe.
- `einarbeitung` — Semestereinarbeitung für neue studentische Berater mit RDG-Grundlagen und Toolwalkthrough.
- `einfache-sprache-briefe` — Anwalts- und Behördenbriefe in leichte oder einfache Sprache uebersetzen für Mandanten mit sprachlichen Einschraenkungen.
- `entwurf` — Erstentwurf haeufiger Schriftstuecke (Widerspruch, Mietrechtsbrief, Klageschrift im Beratungshilfe-Kontext).
- `formular-erzeugung` — Formulare und Antragsdokumente für Behörden oder Gerichte erstellen.
- `fristen` — Fristenmanagement für laufende Mandate mit Warnschwellen und Eskalation.
- `leitfaden-erstellen` — Praxisleitfaeden für haeufige Mandatskonstellationen in verstaendlicher Sprache erstellen.
- `mandant-aufnahme` — Strukturierter Mandantenintake mit Sachverhaltserfassung, Dringlichkeit und Interessenkonfliktpruefung.
- `mandanten-kommunikations-log` — Mandantenkommunikation datenschutzkonform dokumentieren und Kommunikations-Log fuehren.
- `mandantenbrief` — Mandantenbrief in verstaendlicher oder foermlicher Sprache verfassen.
- `memo` — Gutachten-Geruest nach Gutachtenmethode mit markierten Luecken für studentische Analyse erstellen.
- `recherche-start` — Recherchefahrplan für eine Rechtsfrage mit Normen, Rechtsprechungsbereichen und Suchbegriffen.
- `rechtsberatungsstelle-anpassen` — Plugin an spezifische Hochschule, Rechtsgebiete und Verfahrensregeln anpassen.
- `rechtsberatungsstelle-kaltstart-interview` — Erst-Konfiguration des Plugins mit Hochschule, Anleiter und Beratungsregeln.
- `semester-uebergabe` — Semesterabschluss-Uebergabe laufender Mandate mit Uebergabenotizen und Gesamtuebersicht.
- `status` — Fallstatuszusammenfassung mandantengerichtet, intern oder gerichts-/behoerdengerichtet erstellen.

## Worauf besonders achten

- **RDG-Grenze einhalten**: Studierende duerfen keine individualrechtliche Beratung ausserhalb des § 6 RDG-Rahmens erbringen; Abgrenzung zu anwaltlicher Taetigkeit ist essentiell.
- **Anleiter-Freigabe vor Versand**: Kein Schriftstuck und kein Mandantenbrief verlasst die Beratungsstelle ohne Anleiter-Freigabe.
- **Fristen besonders beobachten**: Versaeumte Fristen koennen den Mandanten seinen Anspruch kosten; der Fristen-Skill muss regelmaessig abgerufen werden.
- **Mandatsgeheimnis bei Semesteruebergabe**: Uebergabenotizen duerfen nur mit dem Einverstaendnis des Mandanten weitergegeben werden.
- **Dokumentation datenschutzkonform**: Mandantendaten duerften nicht in nicht-genehmigten KI-Systemen verarbeitet werden.

## Typische Fehler

- Interessenkonfliktpruefung vergessen: Zwei Studierende aus derselben Kohorte beraten unwissentlich Parteien desselben Konflikts.
- Memo als fertige Rechtsberatung weitergeben statt als Analyse-Grundlage für den Anleiter.
- Fristenliste nicht aktuell halten; Fristaenderungen durch Gericht werden nicht eingetragen.
- Bei der Semesteruebergabe Mandate ohne Uebergabenotiz an Nachfolgekohorte weitergeben.
- Einfache-Sprache-Uebersetzung nicht auf Richtigkeit pruefen lassen; Vereinfachungen koennen Rechtsinhalte veraendern.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- RDG in der ab 2023 gueltigen Fassung

---

## Skill: `einfache-sprache-briefe`

_Anwalts- und Behördenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behörde Gericht oder Gegenseite verstehen. BeratungsHiG kostenfreie Beratung, BRAO niedrigschwellige Erstberatung, Lei..._

# [VERALTET] Verständliche Mandantenbriefe → siehe `/mandantenbrief` und `/status mandant`

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Mandantenbriefe: `/mandantenbrief [typ]` oder `/status mandant`.

## Rechtlicher Rahmen

### Hintergrund der Aufteilung

Die Verständlichkeit von Mandantenkommunikation ist eine Rechtspflicht, keine Serviceleistung. Unverständliche Korrespondenz verletzt die anwaltliche Aufklärungspflicht (§ 43a BRAO, BGH-Rspr.) und kann zur Haftung führen. Die Aufteilung in zwei fokussierte Skills verstärkt diese Pflicht, indem sie die Standards für jeden Typ explizit macht.

### Relevante Normen für die Nachfolge-Skills

- **§ 43a Abs. 4 BRAO** — Sachlichkeitsgebot: Mandantenbriefe müssen sachlich, klar und nicht irreführend sein; gilt auch für studentische Beratungsstellen unter Aufsicht.
- **§ 11a BRAO** — Zusammenarbeit in studentischen Beratungsstellen: Briefe gehen unter Aufsicht des Supervisors heraus; vor Versand ist die Supervisoren-Freigabe einzuholen.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Mandantenkorrespondenz ist ein nach außen gehendes Leistungsergebnis und unterliegt der inhaltlichen Supervisoren-Kontrolle.
- **Art. 13 DSGVO** — Informationspflichten: Falls ein Brief erstmals über die Verarbeitung personenbezogener Daten informiert, müssen DSGVO-Pflichtangaben enthalten sein.
- **§§ 2, 3 BerHG** — Beratungshilfe: Bei Mandanten mit Beratungshilfe-Schein muss die Korrespondenz den Leistungsrahmen einhalten; keine Erweiterung ohne neuen Schein.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Stattdessen verwenden:**

Für einfache Korrespondenz (Terminbestätigung, Unterlagenbitte, Eingangsbestätigung):
```
/mandantenbrief terminbestätigung
/mandantenbrief unterlagenbitte
/mandantenbrief eingangsbestätigung
```

Für inhaltliche Statusmitteilungen:
```
/status mandant
```

Vollständiger Ablauf in den jeweiligen SKILL.md-Dateien:

1. Zielgruppe festlegen (Bildungshintergrund, Sprache, besondere Umstände des Mandanten)
2. Verständlichkeitsstandards der Klinik anwenden (Klinik-Konfiguration → plain-language-standard)
3. Kein Fachjargon ohne Erläuterung; kurze Sätze; konkrete Handlungsanweisungen
4. Supervisoren-Routing nach § 6 Abs. 2 RDG vor Versand

## Beispiel

Statt `/einfache-sprache-briefe`:

```
/status mandant
```

Dieser Befehl erstellt ein verständliches Statusschreiben (Zielgruppe: Mandant/-in) nach dem Hauptschulniveau-Standard, ohne Fachjargon, mit konkreten nächsten Schritten: "Was ist passiert / Was passiert als nächstes / Was müssen Sie tun / So erreichen Sie uns."

Oder für Routine-Korrespondenz:
```
/mandantenbrief terminbestätigung
```

Ergebnis: Eine klare Terminbestätigung mit Ort, Zeit, Mitnahme-Unterlagen und Kontaktdaten — ohne juristische Formulierungen.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Materialien:** Semesterskripte und Tutorenmaterialien auf die neuen Skills umschreiben.
- **Verständlichkeitsstandards als optional behandeln:** Die Pflicht zur verständlichen Mandantenkommunikation ergibt sich aus § 43a BRAO und BGH-Rspr. Sie gilt auch für Studierende in der Beratungsstelle unter Supervisorenaufsicht.
- **Fachbegriffe ohne Erläuterung:** Begriffe wie "Widerspruchsfrist", "Vollstreckungstitel" oder "Klagefrist" sind für viele Mandanten unverständlich. Immer in Klammern oder mit einfachem Folgesatz erläutern.
- **Versand ohne Supervisoren-Freigabe:** Kein Mandantenbrief verlässt die Beratungsstelle ohne Freigabe, auch keine kurze Terminbestätigung.

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben zu Mandantenbriefen: `skills/status/SKILL.md`, Sektion "Quellenpflicht", und `skills/mandantenbrief/SKILL.md`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

## Skill: `entwurf-einarbeitung-einfache-sprache`

_Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6 RDG-konforme Formulierung, ausdrücklich als Ausgangspunkt mit anschließender Studie..._

# Schriftsatzentwurf: Erstentwurf-Erstellung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Studierende wenden erhebliche Zeit auf Erstentwürfe von Schriftstücken auf, deren Bildungswert in der rechtlichen Analyse und Strategie liegt — nicht im Abtippen eines Rubrum oder im Formulieren von "Sehr geehrte Damen und Herren". Diese Skill erstellt den Erstentwurf aus Fallnotizen und Rechtsgebiet-spezifischen Mustern, damit die studentische Arbeitszeit dem eigentlichen juristischen Denken zugute kommt.

**Jeder Entwurf ist ausdrücklich ein Ausgangspunkt.** Kein fertiges Arbeitsergebnis. Der/die Studierende analysiert und überarbeitet; der Supervisor prüft, bevor das Schriftstück die Beratungsstelle verlässt.

Beachte: Rechtliche Beratungsleistungen an Einzelpersonen durch Studierende erfolgen nach § 6 Abs. 1 RDG als unentgeltliche Rechtsdienstleistung unter Aufsicht eines zur Rechtsanwaltschaft zugelassenen Supervisors (§ 6 Abs. 2 RDG). Alle nach außen gehenden Schriftstücke sind ohne Supervisoren-Freigabe nicht zu versenden.

## Eingaben

- **Schriftstücktyp** — z. B. `widerspruch`, `klageschrift-ag`, `mahnschreiben`, `beratungshilfe-antrag`, `pkh-antrag`, `mietrechtliches-kündigungsschreiben`
- **Sachverhaltsnotizen / Aktennotiz** — Fakten des Falls; fehlende Angaben werden markiert, nie erfunden
- **Rechtsgebiet** — Mietrecht, Arbeitsrecht, Verwaltungsrecht, Verbraucherrecht u. a.
- **Zuständiges Gericht / Behörde** (falls bekannt) — für Rubrum und Formvorschriften
- **Frist** — ob eine Einreichungsfrist läuft und bis wann

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 6 RDG** — Unentgeltliche Rechtsdienstleistung: zulässig durch Rechtsberatungsstellen unter anwaltlicher Aufsicht; die Aufsicht muss durch eine zur Rechtsanwaltschaft zugelassene Person ausgeübt werden.
- **§ 43a Abs. 2 BRAO** — Mandatsgeheimnis/Verschwiegenheitspflicht: gilt sinngemäß für Studierende der Beratungsstelle; keine Informationen aus dem Mandat nach außen.
- **§ 203 Abs. 3 StGB** — Strafbarkeit der Verletzung von Privatgeheimnissen; Studierende sind als "berufsmäßig tätige Gehilfen" i. S. d. § 203 Abs. 3 S. 2 StGB zu behandeln.
- **§§ 114 ff. ZPO** — Prozesskostenhilfe (PKH): Entwürfe für PKH-Anträge müssen wirtschaftliche Verhältnisse vollständig darlegen; Prüfung hinreichender Erfolgsaussichten (§ 114 Abs. 1 S. 1 ZPO).
- **§§ 1, 2 BerHG** — Beratungshilfe: Voraussetzungen, Bewilligung vor Erbringung der Leistung.
- **§§ 17, 18, 23 VwVfG** — Form von Widersprüchen und Verwaltungsverfahrensschreiben.
- **§ 70 VwGO** — Form des Widerspruchs (schriftlich oder zur Niederschrift); Einreichungsfrist nach §§ 70, 58, 74 VwGO.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Schritt 1: Welches Schriftstück?

Den Anforderungstyp dem Musterbestand der Beratungsstelle zuordnen. Typischer Bestand nach Rechtsgebiet:

| Rechtsgebiet | Schriftstücke |
|---|---|
| **Mietrecht** | Widerspruch gegen Kündigung, Mängelrüge mit Fristsetzung, Klage auf Kaution, Antrag auf einstweiligen Rechtsschutz |
| **Arbeitsrecht** | Kündigungsschutzklage (AG), Abmahnungsrüge, Zeugnisverlangen, Lohnrückstandsschreiben |
| **Verwaltungsrecht** | Widerspruchsschreiben, Klage beim Verwaltungsgericht (Entwurf), Antrag auf aufschiebende Wirkung (§ 80 Abs. 4, 5 VwGO) |
| **Verbraucherrecht** | Widerrufserklärung (§ 355 BGB), Mahnschreiben, Antwort auf Inkassoschreiben, Antrag auf Lastschriftrückgabe |
| **Allgemein** | Beratungshilfe-Antrag (BerH 1), PKH-Antrag (ZPO 117), Vollmacht, Empfangsbekenntnis |

Falls das angeforderte Schriftstück nicht im Musterbestand vorhanden ist: "Der Musterbestand der Beratungsstelle enthält kein Muster für [X]. Ich kann einen Entwurf nach allgemeinen Grundsätzen versuchen, aber dieser muss besonders sorgfältig geprüft werden — er wurde nicht auf das Rechtsgebiet und die zuständige Behörde/das Gericht abgestimmt. Besser wäre, den Supervisor zu fragen, ob ein bewährtes Muster vorliegt."

### Schritt 2: Sachverhalt aufnehmen

Fallnotizen und Aktennotiz lesen. Für jeden Aspekt, den das Schriftstück benötigt: Liegt die Information vor?

| Schriftstück braucht | Vorhanden? | Quelle |
|---|---|---|
| [Tatsache] | Ja / Nein | [Aktennotiz / Mandantenunterlage / noch zu beschaffen] |

Fehlende notwendige Tatsachen → nicht erfinden. Markierung: `[TATSACHE FEHLT: Zustellungsdatum der Kündigung — aus Briefumschlag oder Postzustellungsurkunde entnehmen]`.

### Schritt 3: Zuständiges Gericht / Behörde und Formvorschriften

- **Rubrum:** Gericht, Aktenzeichen (falls vorhanden), Parteien, Bevollmächtigte/r (Studierender unter Aufsicht des Supervisors)
- **Formvorschriften:** Schriftform, Unterschrift, Einreichungsweg (post, Fax, beA, elektronisch)
- Sind örtliche Besonderheiten nicht bekannt: `[PRÜFEN: Einreichungsweg beim zuständigen Gericht / der zuständigen Behörde überprüfen]`

### Schritt 4: Entwerfen

Das Rechtsgebiet-Muster verwenden. Füllen, was aus den Fakten befüllt werden kann. Platzhalter explizit lassen — niemals mit plausibel klingendem Inhalt füllen.

**Wo immer der Entwurf eine Rechtsbehauptung aufstellt:** Diese Behauptung ist eine Hypothese, die der/die Studierende überprüft, keine Schlussfolgerung, auf die der Entwurf sich verlässt. Entsprechend markieren.

### Schritt 5: Unsicherheiten kennzeichnen

Drei Arten von Markierungen, direkt im Text:

- `[TATSACHE FEHLT: ...]` — das Schriftstück benötigt eine Tatsache, die die Fallnotizen nicht enthalten
- `[PRÜFEN: ...]` — eine Rechts- oder Tatsachenbehauptung, die vor Einreichung überprüft werden muss
- `[UNSICHER: ...]` — der Skill ist genuinely unsicher und sagt dies, anstatt zu raten

### Schritt 6: Supervisoren-Routing

Ein Schriftstück bei Gericht oder einer Behörde einzureichen ist eine folgenschwere Handlung. Das Gate ist das Supervisionsmodell der Beratungsstelle, verstärkt durch die Grundvoraussetzung, dass ein zugelassener Rechtsanwalt/eine zugelassene Rechtsanwältin die Aufsicht innehat (§ 6 Abs. 2 RDG). Gerichtliche und behördliche Einreichungen gehen immer durch die Supervisoren-Prüfung, unabhängig vom gewählten Supervisionsmodell.

- **Formelle Prüfwarteschlange:** Entwurf geht in die Warteschlange; Studierender sieht "in Warteschlange für [Supervisor]"
- **Konfigurierbare Flags:** Wenn dieser Schriftstücktyp ein Flag auslöst (gerichtliche Einreichungen in der Regel immer), enthält der Output: "VOR DER EINREICHUNG MIT [SUPERVISOR] ABSPRECHEN"
- **Leichtere Begleitung:** Standard-Sicherheitslabel; keine zusätzliche Schranke — aber gerichtliche Einreichungen gehen per Klinikverfahren dennoch an den Supervisor vor Einreichung

## Prüfliste für Studierende

Vor Vorlage an [Supervisor]:

- [ ] Das Schriftstück vollständig lesen. Sagt es das, was ausgedrückt werden soll?
- [ ] Jede Tatsache: stimmt sie mit den tatsächlichen Mandantenunterlagen überein?
- [ ] Jedes [PRÜFEN]-Flag: durch Recherche aufgelöst oder gestrichen
- [ ] Jedes [TATSACHE FEHLT]-Flag: mit verifizierten Informationen gefüllt oder Abschnitt entfernt
- [ ] Rechtsgrundlage: ist dies die richtige Argumentation? Gibt es bessere Ansätze? (Das ist die Analyse des Studierenden, nicht des Entwurfs.)
- [ ] Formvorschriften: Rubrum, Einreichungsweg, Format nach aktuellen Vorschriften korrekt?
- [ ] [Supervisionsschritt per Klinik-Konfiguration]
```

## Beispiel

**Szenario:** Mandantin Erdem erhält eine fristlose Kündigung ihres Arbeitsverhältnisses. Kündigung zugestellt am 15.04.2026. Studierender Müller soll einen Entwurf der Kündigungsschutzklage beim Arbeitsgericht Berlin erstellen.

```
/entwurf kündigungsschutzklage-ag
Fall: Erdem-Arbeitsrecht-2026
Frist: 06.05.2026 (3 Wochen ab 15.04.2026, § 4 KSchG)
Arbeitgeber: Beispiel GmbH, Musterstraße 1, 10115 Berlin
```

Entwurf enthält: Rubrum (AG Berlin), Anträge, Klagebegründung mit `[PRÜFEN: Beschäftigungsdauer und Betriebsgröße für Anwendbarkeit KSchG]`, `[TATSACHE FEHLT: Datum des Arbeitsvertragsabschlusses]`.

## Risiken und typische Fehler

- **Frist nicht beachtet:** Der Entwurf weist auf erkannte Fristen hin, berechnet sie aber nicht selbst. Studierende müssen die Dreiwochenfrist des § 4 KSchG, die Widerspruchsfrist (§ 70 VwGO), Verjährungsfristen (§ 195 BGB) eigenständig prüfen und in `/fristen` eintragen.
- **Rubrum falsch:** Zuständigkeit, Parteibezeichnungen, Aktenzeichen müssen überprüft werden. Fehlerhaftes Rubrum kann zur Unzulässigkeit führen.
- **PKH-Antrag vergessen:** Wenn die Mandantin/der Mandant nicht zahlungsfähig ist, muss gleichzeitig mit der Klage ein PKH-Antrag (§ 117 ZPO) eingereicht werden.
- **Entwurf verlässt Klinik ohne Freigabe:** § 6 Abs. 2 RDG verlangt anwaltliche Aufsicht. Kein Entwurf wird dem Mandanten oder einer Behörde/einem Gericht ohne Supervisoren-Freigabe zugeleitet.
- **Falsche Rechtsgrundlagen:** Rechtsbehauptungen im Entwurf sind Hypothesen. Der/die Studierende verifiziert jede Norm und Rechtsprechung, bevor der Entwurf weitergereicht wird.

## Quellenpflicht

Jede Rechtsbehauptung im Entwurf ist mit der einschlägigen Norm oder Entscheidung zu belegen. Vorgeschlagene Quellen aus dem Modell sind mit `[Modellwissen — verifizieren]` zu kennzeichnen und vor Verwendung gegen aktuelle Datenbanken (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, dejure) zu prüfen. Niemals ohne Quellangabe und Supervisoren-Freigabe einreichen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

## Skill: `erzeugung-leitfaden-erstellen-mandanten`

_Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behörde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozialrecht Mietrecht Arbeitsrecht. Prüfraster Formular-Typ bestim..._

# [VERALTET] Formularerstellung → siehe `/entwurf`

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Formular- und Schriftstückaufgaben: `/entwurf [Schriftstücktyp]`.

## Rechtlicher Rahmen

### Hintergrund der Zusammenführung

Die Trennung zwischen "Formularerstellung" und "Schriftsatzerstellung" war in der Praxis studentischer Rechtsberatungsstellen künstlich: Ein Beratungshilfe-Antrag (BerH 1) ist juristisch kein anderes Arbeitsergebnis als ein Widerspruchsschreiben — beide erfordern Sachverhaltsaufnahme, Normprüfung und Supervisoren-Freigabe nach § 6 Abs. 2 RDG.

### Relevante Normen für die Nachfolge-Skill `/entwurf`

- **§ 1 BerHG** — Voraussetzungen der Beratungshilfe: BerH 1-Antrag ist vor Leistungserbringung beim Amtsgericht einzureichen; Studierende müssen die Voraussetzungen (Bedürftigkeit, keine anderweitige Beratungsmöglichkeit) prüfen.
- **§ 117 ZPO** — PKH-Antrag: Einreichung mit Klage oder gesondertem Schriftsatz; wirtschaftliche Verhältnisse vollständig darlegen (Erklärung über persönliche und wirtschaftliche Verhältnisse, Formular bewilligen PKH-Schein).
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Ausgefüllte Formulare, die Rechtspositionen des Mandanten begründen oder geltend machen, sind keine formale Routineaufgabe — sie erfordern inhaltliche Supervisoren-Prüfung.
- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht: Formulare enthalten sensitive Mandantendaten; strenge Vertraulichkeit.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Stattdessen `/entwurf [Schriftstücktyp]` verwenden.**

```
/entwurf beratungshilfe-antrag
/entwurf pkh-antrag
/entwurf widerspruch-nebenkostenabrechnung
/entwurf mahnschreiben
```

Vollständiger Ablauf in `skills/entwurf/SKILL.md`:

1. Schriftstücktyp identifizieren und dem Musterbestand zuordnen
2. Sachverhalt aufnehmen; fehlende Angaben kennzeichnen (`[TATSACHE FEHLT: ...]`)
3. Formvorschriften und Einreichungsweg prüfen
4. Entwurf erstellen mit `[PRÜFEN]`- und `[UNSICHER]`-Flags
5. Supervisoren-Routing nach § 6 Abs. 2 RDG

## Beispiel

Statt `/formular-erzeugung beratungshilfeantrag`:

```
/entwurf beratungshilfe-antrag
```

Der Befehl `/entwurf` füllt das Formular BerH 1 aus den Fallnotizen, kennzeichnet fehlende Pflichtangaben mit `[TATSACHE FEHLT: ...]` (z. B. Kontonummer für Bedürftigkeitsnachweis), und leitet nach Fertigstellung in die Supervisoren-Prüfung.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Unterlagen:** Bestehende Handreichungen, Semesterskripte oder Tutorenmaterialien, die auf `/formular-erzeugung` verweisen, auf `/entwurf` umschreiben.
- **Formularausfüllung als Routineaufgabe unterschätzen:** Formulare, die Rechtspositionen des Mandanten geltend machen (PKH, Beratungshilfe, Widerspruch), sind rechtliche Arbeitsergebnisse und unterliegen der Supervisoren-Prüfpflicht nach § 6 Abs. 2 RDG.
- **Falsche Angaben im BerH 1-Antrag:** Unvollständige oder unrichtige Angaben zur Bedürftigkeit können zu Ablehnung und ggf. zur Rückforderung bereits gewährter Beratungshilfe führen (§ 9 BerHG).

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben bei konkreten Schriftstücken und Formularen: `skills/entwurf/SKILL.md`, Sektion "Quellenpflicht".

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund: GELOESCHT. Echtes Datum 22.10.2015 (Skill hatte 14.01.2016); echtes Thema Streitwert der Vollstreckungsgegenklage (§§ 3, 4 ZPO) — kein Bezug zu Beratungshilfe oder anwaltlicher Antragspruefungspflicht. Quelle: dejure.org/2015,32471. Ersatz: kein passender Beleg gefunden; Zeile entfernt.
-->

---

## Skill: `fristen-fristenkontrolle-rdg`

_Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überfällige Einträge bleiben markiert bis zur ausdrücklichen Erle..._

# Fristenverwaltung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Fall-ID + Bezeichnung** — um welches Mandat handelt es sich?
- **Rechtsgebiet** — z. B. Mietrecht, Aufenthaltsrecht, Verbraucherrecht
- **Fristtyp** — Einreichungsfrist / Gerichtstermin / Verjährungsfrist / Widerspruchsfrist / Klagefrist / Wiedereinsetzungsfrist / Sonstige
- **Beschreibung** — eine Zeile: was ist fällig?
- **Fälligkeitsdatum** (ggf. Uhrzeit)
- **Quelle** — Grundlage der Frist (z. B. Zustellungsurkunde v. 20.04.2026, § 74 VwGO, § 276 Abs. 1 ZPO, Mietvertrag § 7)
- **Zuständige/-r Studierende/-r**

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 186–193 BGB** — Berechnung von Fristen und Terminen; § 193 BGB: Fristende am nächsten Werktag, wenn Fälligkeit auf Samstag, Sonntag oder gesetzlichen Feiertag fällt.
- **§§ 217–222 ZPO** — Prozessuale Fristberechnung (Beginn, Ende, Verlängerung, Notfristen).
- **§§ 233–238 ZPO** — Wiedereinsetzung in den vorigen Stand: bei unverschuldeter Fristversäumung binnen zwei Wochen nach Wegfall des Hindernisses zu beantragen (§ 234 ZPO); bei Notfristen und Frist zur Begründung der Revision beachte § 233 S. 2 ZPO.
- **§§ 31, 32 VwVfG / §§ 57–60 VwGO** — Fristberechnung im Verwaltungsverfahren und verwaltungsgerichtlichen Verfahren; Wiedereinsetzung nach § 60 VwGO.
- **§ 74 VwGO** — Klagefrist von einem Monat nach Zustellung des Widerspruchsbescheids.
- **§ 80 Abs. 5 VwGO** — Antrag auf Wiederherstellung der aufschiebenden Wirkung (einstweiliger Rechtsschutz).
- **§ 4 KSchG** — Dreiwochenfrist zur Erhebung der Kündigungsschutzklage (Notfrist); § 5 KSchG Wiedereinsetzung (nachträgliche Zulassung).
- **§§ 195 ff. BGB** — Verjährungsfristen: Regelverjährung 3 Jahre (§ 195 BGB), Beginn mit Schluss des Entstehungsjahres (§ 199 Abs. 1 BGB).
- **§§ 12–17 BeratungshilfeG (BerHG)** — Verfahren bei Beratungshilfe; Beratungshilfeschein vor Mandatsbeginn einholen.
- **§§ 114–127a ZPO** — Prozesskostenhilfe (PKH): Antrag vor oder mit Klageerhebung, keine Unterbrechung laufender Fristen durch PKH-Antrag (§ 204 Abs. 1 Nr. 14 BGB beachten).

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Modus `--eintragen` — neue Frist erfassen

1. Fall-ID + Bezeichnung abfragen.
2. Fristtyp und Beschreibung erfassen.
3. Fälligkeitsdatum aufnehmen; Quelle dokumentieren.
4. Zuständige/-n Studierende/-n zuweisen.
5. System generiert automatisch eine ID: `[fall-id]-[kurzbezeichnung]-[JJJJ-MM]`.
6. Duplikatsprüfung: existiert bereits ein Eintrag mit gleicher Fall-ID, gleichem Typ und gleichem Datum? Falls ja, Hinweis vor dem Speichern.
7. **Plausibilitätsprüfung (Pflicht):** Nach Eingabe des Datums wird das Ergebnis gegen typische Fristbänder für den gewählten Typ geprüft (z. B. Klagefrist VwGO: ca. 1 Monat nach Zustellung; Dreiwochenfrist KSchG: 21 Tage ab Zugang Kündigung; Widerspruchsfrist VwGO: 1 Monat). Liegt das eingetragene Datum außerhalb des typischen Bandes, erfolgt folgende Warnung:
 > "Das eingetragene Datum liegt außerhalb des typischen Bereichs für [Fristtyp] im deutschen Recht ([Rechtsgebiet]). Typische Dauer: ca. [Bandbreite] nach [auslösendem Ereignis]. Ihr Eintrag: [Datum], das sind [N] Tage nach [Ereignis]. Prüfen Sie Ihre Berechnung gegen [zitierte Norm aus dem Fristenband] sowie die maßgebliche Fristberechnungsregel (§ 187 f. BGB / § 222 ZPO / § 57 VwGO). Falls Ihre Berechnung korrekt ist (Sonderregelung, Hemmung, Unterbrechung, Wiedereinsetzung), bestätigen Sie; ich trage die Frist unverändert ein."
8. Gibt der/die Studierende `[PRÜFEN]` im Datumsfeld ein, wird der Eintrag mit `fällig: [PRÜFEN]` gespeichert; die Plausibilitätsprüfung läuft erst, wenn ein konkretes Datum eingetragen wird.
9. **Die Skill berechnet keine Fristen.** Die Berechnung obliegt dem/der Studierenden und dem Supervisor; die Skill trägt das Ergebnis ein.

### Modus `--bericht` (Standard) — gesamtübergreifende Übersicht

Liest `deadlines.yaml` und erzeugt folgende Tabelle:

```markdown
### Fristenübersicht — [heute]

**Aktive Fristen:** [N]
**Überfällig:** [N] ⚠
**Fällig diese Woche (nächste 7 Tage):** [N]

---

## Überfällig (sofortige Bearbeitung erforderlich)

| ID | Fall | Typ | Fällig | Zuständig | Tage überfällig |
|---|---|---|---|---|---|

## Fällig heute / in den nächsten 3 Tagen

| ID | Fall | Typ | Fällig | Zuständig |
|---|---|---|---|---|

## Fällig in 4–7 Tagen

| ID | Fall | Typ | Fällig | Zuständig |
|---|---|---|---|---|

## Fällig in 8–14 Tagen

[Liste]

## Über 14 Tage (Anzahl — Details mit `--bericht --horizont=30`)

---

## Nach Zuständigen (Arbeitsbelastung)

| Studierende/-r | Überfällig | Nächste 7 Tage | Nächste 14 Tage | Gesamt aktiv |
|---|---|---|---|---|

## Nach Rechtsgebiet

[gleiche Tabelle, nach Rechtsgebiet gruppiert]

## Nicht zugewiesene Fristen

[Liste — Warnung, wenn aktive Fristen ohne Zuständige vorhanden sind]
```

### Modus `--aktualisieren [id]` — bestehende Frist ändern

Typische Aktualisierungen: Fristdatum geändert (Terminverlegung durch Gericht), Zuständige/-r gewechselt (Neuzuweisung), Notiz hinzugefügt. Jede Änderung wird mit Datum protokolliert; der Verlauf bleibt im Eintrag sichtbar.

### Modus `--erledigt [id]` — als abgeschlossen markieren

- Setzt `status: erledigt`, `erledigungsdatum: [heute]`.
- Bestätigt mit dem/der Studierenden, dass die Handlung tatsächlich vorgenommen und (soweit erforderlich) eingereicht wurde.
- Verschwindet aus aktiven Berichten, bleibt aber in der YAML-Datei erhalten.

### Modus `--schliessen [id]` — ohne Erledigung schließen

Für Fristen, die nicht mehr relevant sind (Fall einvernehmlich beendet, Antrag zurückgenommen, Mandant hat Beratungsstelle abgewählt). Erfordert zwingend einen Eintrag in `notizen:` mit Begründung.

## Beispiel

**Szenario:** Studierende Maria hat eine Kündigung des Mietverhältnisses erhalten. Kündigung wurde am 08.04.2026 zugestellt. Widerspruchsfrist (§ 574 BGB i. V. m. § 542 BGB) läuft am 08.05.2026 ab.

```
/fristen --eintragen
Fall: Mueller-Mietrecht-2026
Typ: Klagefrist
Beschreibung: Widerspruch gegen Kündigung, § 574 BGB
Fällig: 08.05.2026
Quelle: Zustellung der Kündigung 08.04.2026, § 574 BGB
Zuständig: stud. Berater Schmidt
```

Ausgabe: Eintrag `mueller-mietrecht-widerspruch-2026-05` wird gespeichert. Plausibilitätsprüfung: 30 Tage nach Zustellung — im typischen Band für Widerspruchsfristen im Mietrecht. Eintrag übernommen.

## Risiken und typische Fehler

- **Frist falsch berechnet:** Die Skill trägt ein, was der/die Studierende eingibt; sie berechnet nicht selbst. Besonders kritisch bei: § 222 ZPO (Wochenfrist), § 193 BGB (Sonn-/Feiertagsverschiebung), § 57 VwGO, Sonderfälle bei Zustellungsfiktion nach § 41 Abs. 2 VwVfG.
- **Notfrist verwechselt mit verlängerbarer Frist:** ZPO-Notfristen (z. B. Notfrist Berufung, § 548 ZPO; Revisionsfrist, § 548 ZPO) sind nicht verlängerbar. Fristverlängerungsanträge bei Notfristen sind unwirksam. Immer beim Supervisor klären.
- **PKH-Antrag hemmt Frist nicht automatisch:** Die Einreichung eines PKH-Antrags unterbricht keine Klagefrist. Ausnahme: § 204 Abs. 1 Nr. 14 BGB (Verjährungshemmung durch PKH-Antrag bei Verjährungsfristen); nicht bei prozessualen Ausschlussfristen.
- **Keine Zuweisung:** Aktive Fristen ohne Zuständige/-n werden im Bericht besonders hervorgehoben. Unzugewiesene Fristen sind Hochrisikopositionen.
- **Frist nur im Kopf des Studierenden:** Wird nicht in der YAML-Datei eingetragen und nicht an die nächste Kohorte übergeben.

## Quellenpflicht

Jede eingetragene Frist muss eine **Quellnorm** enthalten (Gesetz, Gerichtsurteil, Vertrag, behördlicher Bescheid). Fristen ohne Quellangabe erhalten den Warnstatus `warnung: keine-quelle`. Die Quellnorm ist die Grundlage, gegen die der Supervisor die Berechnung prüft.

Jeder Fristeneintrag, der außerhalb des Plausibilitätsbands liegt und dennoch bestätigt wurde, erhält automatisch den Hinweis: `warnung: außerhalb-plausibilitätsband — vom Supervisor zu prüfen`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall. Alle Fristenberechnungen sind vom begleitenden Supervisor zu prüfen und freizugeben.

---

## Skill: `kaltstart-interview`

_Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet werden. BeratungsHiG § 1 Erlaubnisnorm, BRAO Aufsicht, Beratungsordnung der Hochsch..._

# /kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Rechtsberatungsstelle** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

1. Prüfe: Ist bereits eine `CLAUDE.md` vorhanden? Falls ja: Anbieten, abschnittsweise zu überarbeiten (`--redo`) oder Übersicht des bestehenden Profils zu zeigen.
2. Führe das Interview durch – Schritt für Schritt, nicht alles auf einmal.
3. Schreibe `CLAUDE.md` mit allen erhobenen Daten.
4. Empfehle als nächsten Schritt: `/rechtsberatungsstelle:leitfaden-erstellen` für jeden Fachbereich.

---

### Ersteinrichtung der Beratungsstelle

## Triage zu Beginn
1. Handelt es sich um eine Neugründung oder eine grundlegende Neuausrichtung der bestehenden Beratungsstelle?
2. Welche Rechtsgrundlage gilt für die Beratungsstellenarbeit: § 6 Abs. 2 Nr. 2 RDG, § 8 RDG oder Tätigkeit unter zugelassenem Anwalt?
3. Welche Fachbereiche sollen von Anfang an eingerichtet werden (Mietrecht, Sozialrecht, Aufenthaltsrecht)?
4. Ist bereits eine CLAUDE.md vorhanden, die abschnittsweise ueberarbeitet werden soll?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Voraussetzungen für erlaubnisfreie Rechtsberatung in Beratungsstellen: Anleitungserfordernis und Unentgeltlichkeit
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des Anleiters: muss von Beginn an organisatorisch sichergestellt werden
- § 203 Abs. 4 StGB — Einbeziehung Dritter (Studierende): Verschwiegenheitsvereinbarungen als Pflichtbestandteil der Ersteinrichtung
- Art. 30 DSGVO — Verarbeitungsverzeichnis: muss vor Beginn der Datenverarbeitung erstellt werden

## Berufsrechtlicher Rahmen

- § 6 Abs. 2 Nr. 2 RDG: Die Organisation der Anleitungsstruktur muss sicherstellen, dass der Volljurist tatsächlich in der Lage ist, die Studierenden anzuleiten. "Formelle" Aufsicht ohne tatsächliche Prüfung genügt nicht; vgl. Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 52.
- § 43a Abs. 2 BRAO: Verschwiegenheitsorganisation muss bereits bei Einrichtung der Beratungsstelle mitgedacht werden (kein Mandantendaten-Upload in nicht abgesicherte Systeme).
- § 203 Abs. 4 StGB: Einbeziehung Dritter (Studierende, externe IT) erfordert vertragliche Absicherung.

## Ablauf

### Schritt 0: Bestehendes Profil prüfen

Ist eine `CLAUDE.md` vorhanden?
- Ja: "Ihr Profil ist bereits eingerichtet. Möchten Sie (a) das Profil anzeigen, (b) einen Abschnitt überarbeiten, oder (c) komplett neu starten (`--redo`)?"
- Nein: Mit Schritt 1 beginnen.

### Schritt 1: Beratungsstellentyp

> Welche Art von Beratungsstelle richten Sie ein?

Optionen (Mehrfachauswahl möglich):
1. **Universitäre Refugee Law Clinic (RLC)** – Schwerpunkt Asyl/Aufenthaltsrecht; § 6 II Nr. 2 RDG
2. **Studentische Rechtsberatung allgemein** – SGB II, Mietrecht, Verbraucherrecht; § 6 II Nr. 2 RDG
3. **AnwVer / DAV Pro-Bono-Programm** – Zugelassene Anwälte, kein RDG-Problem
4. **Verbraucherzentrale** – § 8 Abs. 1 Nr. 4 RDG (Sondererlaubnis)
5. **Wohlfahrtsverband / Sozialberatung** (AWO, Caritas, Diakonie, DRK, Paritätischer) – § 8 Abs. 1 Nr. 4 RDG
6. **Sonstiges** – Bitte beschreiben.

Erfasse auch: Hochschule / Trägerin, Stadt, seit wann aktiv, Anzahl aktiver Studierender pro Semester.

### Schritt 2: Rechtsgrundlage bestätigen

Je nach Typ aus Schritt 1:

| Typ | Rechtsgrundlage | Pflichten |
|---|---|---|
| RLC / studentische Beratung | § 6 Abs. 2 Nr. 2 RDG | Unentgeltlichkeit, Anleitung durch Volljurist zwingend |
| Verbraucherzentrale | § 8 Abs. 1 Nr. 4 RDG | Trägergebundene Erlaubnis; keine Einzelfallklage |
| Sozialberatung (Verbände) | § 8 Abs. 1 Nr. 4 RDG | Satzungsgemäßer Auftrag erforderlich |
| Pro-Bono (zugelassene Anwälte) | § 1 BRAO (volle Zulassung) | BRAO/BORA voll anwendbar |

> Bestätigen Sie: "Alle Beratungsleistungen erfolgen unentgeltlich. Die Studierenden stehen unter meiner tatsächlichen Anleitung. Ich nehme meine Aufsichtspflicht wahr." (§ 6 II Nr. 2 RDG)

### Schritt 3: Fachbereiche

> Welche Rechtsgebiete deckt Ihre Beratungsstelle ab?

Optionen (Mehrfachauswahl):
- [ ] Asyl- und Flüchtlingsrecht (AsylG, AufenthG)
- [ ] Aufenthaltsrecht allgemein (AufenthG, FreizügG/EU)
- [ ] SGB II / Bürgergeld
- [ ] SGB XII / Grundsicherung im Alter
- [ ] SGB IX / Eingliederungshilfe (inkl. § 76b SGB IX Geflüchtete)
- [ ] Rentenrecht / SGB VI
- [ ] Mietrecht (privat)
- [ ] Mietrecht (Sozialwohnung / WoBindG)
- [ ] Verbraucherrecht / AGB
- [ ] Arbeitsrecht (Kündigung, KSchG)
- [ ] Familienrecht (Unterhalt, Sorgerecht)
- [ ] Strafrecht (nur eingeschränkt – an Fachanwälte verweisen)
- [ ] Sonstiges: [Freitext]

### Schritt 4: Aufsichtsmodell

> Wie möchten Sie das Aufsichtsmodell einrichten?

**Prüfungsgates (Default, anpassbar):**

| Dokument | Default-Gate |
|---|---|
| Widerspruch (Fristen < 2 Wochen) | Sofortige Anleiterkonsultation |
| Widerspruch (Frist > 2 Wochen) | Anleiter prüft vor Versand |
| Klageschrift | Anleiter prüft und gibt frei (zwingend) |
| Mandantenbrief mit Rechtsrat | Anleiter prüft vor Versand |
| Intake-Protokoll | Anleiter nimmt Kenntnis |
| Memo / Rechtsgutachten | Anleiter prüft inhaltlich |
| Semesterübergabe | Anleiter muss bestätigen |

Anleiter kann Gates verschärfen (z. B. alle Dokumente) oder – für erfahrene Studierende – für bestimmte Routinedokumente lockern.

### Schritt 5: Pädagogikhaltung

> Wie lernen Studierende bei Ihnen am besten?

| Haltung | Beschreibung | Geeignet für |
|---|---|---|
| **Ausführen** | Das System erstellt vollständige Entwürfe; Studierende analysieren und übergeben | Erfahrene Studierende (3.–5. Sem.), Routinedokumente |
| **Anleiten** | Das System gibt Struktur und Schlüsselpunkte; Studierende füllen aus | Mittelstufe (2.–3. Sem.) |
| **Lehren** | Das System stellt nur Fragen; Studierende erarbeiten Lösung | Anfangssemester, neue Fachgebiete |

Default für gesamte Beratungsstelle + ggf. Übersteuern je Fachbereich / Dokumenttyp.

### Schritt 6: Verschwiegenheitsorganisation

> Wie ist die IT-Infrastruktur organisiert?

- Werden Mandantendaten in einem Cloud-System verarbeitet? → Auftragsverarbeitungsvertrag (AVV) nach Art. 28 DSGVO erforderlich.
- Wer hat Zugang zu den Mandantenakten?
- Wie werden Akten nach 5 Jahren gelöscht (§ 50 BRAO Aufbewahrungspflicht)?
- Einweisung der Studierenden in Verschwiegenheitspflichten? → Empfehlung: Schriftliche Verpflichtungserklärung zu § 203 StGB.

### Schritt 7: Örtliche Besonderheiten

> Welche örtlichen Kontexte sind wichtig?

- Zuständige BAMF-Außenstelle?
- Zuständige Ausländerbehörde?
- Jobcenter-Bezirke / Träger (kommunal oder BA)?
- Sozialgerichte / Verwaltungsgerichte mit Zuständigkeit?
- Kooperationspartner (Dolmetscherdienste, andere Beratungsstellen, Pro-Bono-Initiativen)?
- Qualifizierter Mietspiegel vorhanden? (Relevant: Berlin, Hamburg, München, Frankfurt, Köln)

### Schritt 8: CLAUDE.md schreiben

Ausgabe: vollständige, aktualisierte `CLAUDE.md` mit allen erhobenen Konfigurationswerten. Struktur wie im CLAUDE.md-Template vorgegeben.

Anschließend empfehlen:
- `/rechtsberatungsstelle:leitfaden-erstellen` für jeden konfigurierten Fachbereich
- `/rechtsberatungsstelle:einarbeitung` – Testlauf aus Studierenden-Perspektive

## Risiken / typische Fehler

- **Anleitungsstruktur nur auf dem Papier:** § 6 Abs. 2 Nr. 2 RDG verlangt tatsächliche, nicht nur formelle Anleitung. Ein Anleiter, der monatlich einmal ins Büro schaut, genügt nicht.
- **Fachbereiche zu weit gefasst:** Eine Beratungsstelle, die alles anbietet, kann nichts gut anbieten. Lieber weniger Bereiche mit klarer Gate-Struktur als viele Bereiche mit Qualitätslücken.
- **IT-Sicherheit nicht mitgedacht:** Cloud-Systeme ohne AVV verletzen DSGVO Art. 28. Besonders kritisch bei Asylsuchenden (Art. 9 DSGVO: besondere Kategorien).
- **Semesterwechsel nicht organisiert:** Ohne klare Übergaberegeln fallen Mandate zwischen den Semestern durch. `/rechtsberatungsstelle:semester-übergabe` muss im Ablaufplan verankert sein.

---

<!-- AUDIT-HINWEIS 27.05.2026: Halluzinierte BGH-Zitate entfernt (NOT_FOUND oder WRONG_TOPIC gemaess dejure.org-Pruefung). Betroffene AZ siehe inline-Kommentare. Frontmatter unveraendert. -->

---

## Skill: `leitfaden-erstellen`

_Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache. BeratungsHiG niedrigschwellige Beratung, Verbraucherrecht Mietrecht Arbeitsrec..._

# /leitfaden-erstellen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

1. Lade `CLAUDE.md` → Rolle (muss Anleitender Volljurist sein), Fachbereiche, Rechtsgrundlage.
2. Nutze den untenstehenden Ablauf.
3. Wenn der Nutzer kein Anleitender Volljurist ist: Stopp und weiterleiten (Studierende → `/rechtsberatungsstelle:einarbeitung`).
4. Durchlaufe: Fachbereich → Intake-Fragen → Pädagogikhaltung → Prüfungsgates → Querprüfungen → örtliche Besonderheiten.
5. Schreibe `guides/<fachbereich>.md`. Erstelle das Verzeichnis `guides/` bei Bedarf.
6. Biete einen Testlauf an: `/rechtsberatungsstelle:entwurf` unter der konfigurierten Haltung ausführen, damit der Anleiter sieht, was Studierende sehen.

---

### Build Guide: Anleitungsgeführter Fachbereichsleitfaden

## Triage zu Beginn
1. Fuer welchen Fachbereich soll der Leitfaden erstellt werden (Mietrecht, Sozialrecht, Aufenthaltsrecht, Strafrecht)?
2. Welche Paedagogikhaltung soll der Leitfaden vorgeben: ausfuehren, anleiten oder lehren?
3. Gibt es einen bestehenden Leitfaden, der ueberarbeitet werden soll, oder wird er neu erstellt?
4. Welche spezifischen Prüfungsgates und RDG-Grenzen sollen für diesen Fachbereich konfiguriert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 6 Abs. 2 Nr. 2 RDG — Erlaubnisfreie Rechtsberatung in Beratungsstellen unter Anleitung eines Volljuristen; Leitfaden konfiguriert den Anleitungsrahmen
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des anleitenden Anwalts: gilt auch für Leitfaden-Inhalte und Mandatsdaten
- § 203 Abs. 4 StGB — Einbeziehung Dritter (Studierende) erfordert vertragliche Absicherung der Verschwiegenheit
- § 43a Abs. 4 BRAO i.V.m. § 3 BORA — Interessenkonflikt-Regeln muessen im Leitfaden für jeden Fachbereich verankert sein

## Berufsrechtlicher Rahmen

Dieser Leitfaden ist ein internes Konfigurationsdokument. Er legt fest, wie die Beratungsstelle nach § 6 Abs. 2 Nr. 2 RDG betrieben wird:

- **§ 6 Abs. 2 Nr. 2 RDG:** Unentgeltlichkeit und Anleiterpflicht sind in jedem Leitfaden zu verankern.
- **§ 43a Abs. 2 BRAO:** Verschwiegenheit des Anleiters erstreckt sich auf alle im Rahmen der Beratungsstelle erlangten Informationen.
- **§ 43a Abs. 4 BRAO / BORA § 3:** Der Leitfaden muss Konfliktprüfungsregeln für den Fachbereich enthalten.
- **Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 44–52:** Anforderungen an die Anleitungsorganisation.

## Schlüsselinhalte des Leitfadens

Biete dies als Checkliste an, die der Anleiter durcharbeiten oder als Inhaltsverzeichnis nutzen kann:

- Was müssen Studierende wissen, bevor sie einen Fall berühren? (Verschwiegenheit nach § 43a BRAO analog / § 203 StGB; RDG-Grenzen; Umfang ihrer Befugnisse)
- Was sind die 3–5 häufigsten Fehler von Studierenden in diesem Fachbereich, und wie soll der Skill sie erkennen?
- Wann muss der Studierende pausieren und Rücksprache halten? (Einreichung, Versand, Strategieentscheidung, Vergleich)
- Welches Sprachniveau ist für Mandantenmitteilungen anzustreben? (Leichte Sprache Niveau B1/B2 als Ziel bei Mandanten ohne juristische Vorbildung; ggf. mehrsprachig bei Geflüchteten)
- Welche örtlichen Sonderregeln, Formulare oder Fristen muss jede Studierende kennen?
- Wann soll der Skill lehren statt tun? (Je Dokumenttyp – Default und Ausnahmen festlegen)

## Ablauf

### Schritt 1: Rollenprüfung

Dies ist ein Anleiter-Skill. Lies `CLAUDE.md` → `Rolle`. Wenn die Rolle nicht "Anleitender Volljurist" ist:

> Dieser Skill ist für Anleiter – er konfiguriert das Verhalten der studierendengerichteten Skills. Wenn Sie der Anleiter sind, stellen Sie sicher, dass Ihre Rolle in `/rechtsberatungsstelle:rechtsberatungsstelle-kaltstart-interview` auf "Anleitender Volljurist" gesetzt ist. Wenn Sie Studierende/r sind, ist dies nicht der richtige Skill für Sie – starten Sie mit `/rechtsberatungsstelle:einarbeitung`.

Stopp, wenn Rolle nicht Anleiter.

### Schritt 2: Fachbereich?

> Für welchen Fachbereich soll dieser Leitfaden gelten? (Asyl/Aufenthaltsrecht | SGB II/Bürgergeld | Mietrecht | Verbraucherrecht | Familienrecht | SGB IX/Eingliederungshilfe | Sonstiges)

Falls "Sonstiges": Kurzname erfragen → wird zum Dateinamen (Kleinbuchstaben, Bindestriche: `asyl.md`, `sgbii.md`, `mietrecht.md`).

Prüfe die in `CLAUDE.md` → `Fachbereiche` eingetragenen Bereiche. Wenn der gewählte Bereich dort nicht aufgeführt ist, hinweisen.

Falls ein Leitfaden für diesen Bereich bereits existiert: "Möchten Sie (a) abschnittsweise überarbeiten, (b) neu aufbauen und überschreiben, oder (c) zunächst den bestehenden Leitfaden sehen?"

### Schritt 3: Intake-Fragen

> Was sollten Studierende eine neue Mandantin/einen neuen Mandanten für diesen Fachbereich fragen? Ich starte mit einem generischen Intake für [Fachbereich] – sagen Sie mir, was hinzugefügt, entfernt oder geändert werden soll. Welche Warnsignale sollten Studierende erkennen? Welche Fälle passen gut zur Beratungsstelle, welche sollten weitervermittelt werden?

Fachbereichs-Defaults (wenn keine Angaben vorhanden):

**Asyl/Aufenthaltsrecht:**
- Aktueller Status und Einreisezeitpunkt (Datum für Jahresfrist § 74 AsylG wichtig!)
- Laufende Verfahren: BAMF-Bescheid erhalten? Klage eingereicht?
- Besondere Vulnerabilität: Minderjährigkeit, Traumatisierung, Behinderung (§ 76b SGB IX)
- Familienangehörige und deren Status
- Vorstrafen (mit Sensibilität erfragen – § 3 AsylG, § 60 AufenthG prüfen)
- Sprachkenntnisse / Dolmetscherbedarf
- Dringlichkeit: Zustellungsdatum des Bescheids? Klagefrist (§ 74 AsylG: 2 Wochen bei § 36-Bescheid!)?

**SGB II / Bürgergeld:**
- Aktueller Leistungsbezug / zuletzt erhaltener Bescheid
- Anlass: Bewilligungs-, Änderungs- oder Ablehnungsbescheid? Sanktionsbescheid?
- Einkommensverhältnisse, Vermögen (§§ 11–12 SGB II)
- Unterkunftskosten (§ 22 SGB II – Angemessenheit prüfen)
- Widerspruchsfrist: 1 Monat ab Bekanntgabe (§ 84 SGG)
- Vorherige Kontakte mit dem Jobcenter (Widersprüche, Klagen)

**Mietrecht:**
- Art des Mietverhältnisses (privat, sozial, öffentlich-gefördert)
- Anlassfall: Kündigung, Mieterhöhung, Mängel, Kaution, Modernisierung?
- Mietvertrag und Mietdauer
- Dokumentation vorhandener Mängel (Fotos, Schriftverkehr)
- Mietspiegel des Ortes verfügbar? (z. B. Berliner Mietspiegel 2023/2024)
- Dringlichkeit: Räumungsklage? Gerichtstermin?

### Schritt 4: Pädagogikhaltung

Drei Stufen – Anleiter wählt Default und kann je Dokumenttyp übersteuern:

| Haltung | Was der Skill tut | Geeignet für |
|---|---|---|
| **Ausführen** | Entwurf vollständig ausarbeiten; Studierende analysieren und übergeben | Routineschriftsätze im 3. Semester+ |
| **Anleiten** | Gliederung und Schlüsselpunkte ausgeben; Studierende füllen aus | Memos, neue Fachbereiche |
| **Lehren** | Nur Fragen stellen; Studierenden zur Lösung führen | 1. Semester, neue Fachbereiche, komplexe Rechtsfragen |

### Schritt 5: Prüfungsgates

> Welche Arten von Dokumenten oder Entscheidungen müssen zwingend zu Ihnen? Ich schlage vor: Klageerhebung, Widerspruch (bei kurzfristigen Rechtsbehelfsfristen sofort), alle Schriftsätze an Gericht, alle Mitteilungen an Mandanten mit konkretem Rechtsrat.

Anleiter kann die Gate-Liste erweitern, einschränken oder beibehalten.

### Schritt 6: Querprüfungen

Welche anderen Fachbereiche überschneiden sich regelmäßig?

- Asylmandate → fast immer SGB II/XII-Fragen (§ 7 Abs. 1 Satz 2 Nr. 1 SGB II: Leistungsausschluss für bestimmte Ausländer beachten!)
- Mietmandate → ggf. Sozialhilfe (§ 22 SGB II Unterkunftskosten), ggf. Familienrecht
- SGB II → Arbeitsrecht (Eingliederungsvereinbarung, Sanktionen bei Ablehnung von Arbeit)

### Schritt 7: Örtliche Besonderheiten

> Gibt es örtliche Regeln, Sonderformulare oder Fristen, die jede Studierende kennen muss? Welche lokalen Anlaufstellen (Gerichte, Behörden, Dolmetscherdienste, Kooperationspartner) sind wichtig?

**Berlin-Beispiele:**
- Berliner Mietspiegel 2023/2024 (qualifiziert nach § 558d BGB)
- Jobcenter-Bezirke Berlin (11 Bezirke) – Formulare und Zuständigkeiten
- BAMF-Außenstellen Berlin, Eisenhüttenstadt
- Pro Bono Berlin e. V. als Weitervermittlungspartner
- Berliner Beratungszentrum für Migration und Qualifizierung (BBZ)

**Bremen-Beispiele:**
- Jobcenter Bremen (zentral)
- BAMF Bremen
- Refugee Law Clinic Bremen (Uni Bremen) – Kooperationen möglich
- Caritasverband Bremen – Migrationsberatung
- Verbraucherzentrale Bremen

### Schritt 8: Leitfaden schreiben

Ausgabe: `guides/<fachbereich>.md` mit den Sektionen:
1. Fachbereichsüberblick und RDG-Grenzen
2. Intake-Fragen (Standard und Warnsignale)
3. Pädagogikhaltung (Default + Ausnahmen)
4. Prüfungsgates
5. Querprüfungen
6. Örtliche Besonderheiten und Weitervermittlung
7. Wichtige Fristen auf einen Blick
8. Empfohlene Quellen und Datenbanken

## Risiken / typische Fehler

- **Fristenversäumnis:** Der Leitfaden muss für jeden Fachbereich die kritischsten Fristen explizit benennen. Besonders gefährlich: § 36 AsylG (1 Woche), § 74 AsylG (2 Wochen bei beschleunigtem Verfahren), § 4 KSchG (3 Wochen).
- **RDG-Grenzen nicht klar kommuniziert:** Studierende ohne klare Anleitungsstruktur überschreiten versehentlich § 3 RDG.
- **Fehlende Konfliktprüfung:** Ohne explizite Gate-Regel übersehen Studierende, wann sie den Anleiter einschalten müssen.
- **Sprachbarrieren bei Geflüchteten:** Leitfaden sollte Dolmetscherressourcen und Sprach-Level-Anforderungen an Mandantenbriefe festlegen.

---

## Skill: `mandant-aufnahme`

_Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen. BeratungsHiG § 2 Beratungsberechtigung, BRAO § 43a Interessenkonflikte, niedrigschwe..._

# /mandant-aufnahme

1. Lade `CLAUDE.md` → Fachbereiche, Intake-Vorlagen, Aufsichtsmodell, Konfliktprüfungsregeln.
2. Nutze den Ablauf unten.
3. Route zum fachbereichsspezifischen Template; achte auf fachübergreifende Probleme.
4. Konfliktprüfung, RDG-Plausibilitätsprüfung, Triage.
5. Ausgabe: formatierte Fallzusammenfassung mit KI-Label, Verifikationshinweisen, Aufsichtsrouting.

---

### Mandantenintake

## RDG-Besonderheiten beim Intake

- § 6 Abs. 2 Nr. 2 RDG: Das Intake-Gespräch ist eine Rechtsdienstleistung – es darf nur unentgeltlich und unter Anleitungsstruktur stattfinden.
- § 43a Abs. 4 BRAO / BORA § 3: **Vor jedem Intake Interessenkonflikt prüfen.** Hat die Beratungsstelle oder der Anleiter bereits die Gegenseite vertreten?
- § 203 StGB: Alles, was im Intake erfährt wird, ist Mandantengeheimnis – ab dem ersten Wort des Gesprächs.
- DSGVO Art. 13: Der Mandant ist zu Beginn über die Verarbeitung seiner Daten zu informieren (Name, Zweck, Speicherdauer, Rechte).

## Interessenkonflikt-Check (zwingend vor jedem Intake)

Bevor das Gespräch beginnt:
1. Name des Mandanten und aller beteiligten Parteien (Vermieter, Jobcenter-Sachbearbeiter o. Ä.) erfassen.
2. Gegen bestehende Mandate und Mandantenregister abgleichen.
3. Wenn Konflikt erkannt: Intake sofort stoppen; Mandant höflich über Hindernis informieren; keine Rechtsauskünfte mehr erteilen; an alternative Beratungsstelle verweisen.

> Prüffrage: "Hat unsere Beratungsstelle oder unser Anleiter je die Gegenseite dieses Verfahrens beraten?" – wenn ja: Konflikt.

## Datenschutz-Hinweis zu Beginn (Pflicht)

Vor Beginn des Gesprächs vorlesen oder übersetzen (ggf. mit Dolmetscher):

> "Wir sind eine studentische Rechtsberatungsstelle. Ihre Daten werden nur für Ihre Beratung genutzt und nach Abschluss des Mandats mindestens 5 Jahre aufbewahrt (§ 50 BRAO). Sie können jederzeit Auskunft, Berichtigung oder Löschung verlangen (DSGVO Art. 15–17). Ihre Angaben sind vertraulich (§ 203 StGB)."

## Fachbereichsspezifisches Intake

### Asyl / Aufenthaltsrecht
- **Personalien:** Vollständiger Name (mit Schreibweise lt. Reisepass/Ausweis), Geburtsdatum, Staatsangehörigkeit.
- **Status:** Aktueller aufenthaltsrechtlicher Status (Asylantragsteller, GFK-Schutz, subsidiärer Schutz, Duldung, humanitärer Aufenthaltstitel § 25 AufenthG)?
- **Verfahrensstand:** BAMF-Bescheid erhalten? Datum der Zustellung? → **Fristencheck sofort!** Bei § 36-Bescheid: Klage binnen 1 Woche (§ 74 Abs. 1 i. V. m. § 36 AsylG)!
- **Einreise:** Datum und Einreiseweg (relevant für Dublin III, Jahresfrist § 74 AsylG).
- **Vorverfahren:** Frühere Asylanträge, Abschiebungen, EURODAC-Treffer?
- **Vulnerabilität:** Minderjährigkeit (§ 12 AsylG: Bestellung Vormund), Schwangerschaft, Trauma, Behinderung (→ § 76b SGB IX prüfen).
- **Familie:** Familienangehörige, deren Status, Familiennachzug?
- **Strafrecht:** Vorstrafen (§ 3 Abs. 2 AsylG Ausschluss, § 25 Abs. 3 AufenthG Sperrung)?
- **Sprache:** Welche Sprachen spricht der Mandant? Dolmetscher notwendig?
- **Dringlichkeit:** Abschiebung angekündigt? Ankündigungsschreiben der Ausländerbehörde?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### SGB II / Bürgergeld
- **Bescheid:** Art des Bescheids (Bewilligung, Änderung, Ablehnung, Sanktion) und Datum der Bekanntgabe → **Widerspruchsfrist: 1 Monat ab Bekanntgabe (§ 84 SGG)**.
- **Leistungen:** Aktuell bewilligte Bedarfe (Regelbedarf, Unterkunft § 22 SGB II, Mehrbedarfe §§ 20 ff. SGB II)?
- **Anlass:** Sanktion (§ 31 SGB II – Pflichtverletzung, Höhe, Dauer)? Einkommensanrechnung (§§ 11–11b SGB II)? Unterkunftskosten unangemessen (§ 22 SGB II)?
- **Haushaltsgemeinschaft:** Wer lebt im Haushalt?
- **Einkommen und Vermögen:** Erwerbseinkommen, Kindergeld, Unterhalt; Vermögen (Schonvermögen § 12 SGB II beachten).
- **Vorherige Rechtsmittel:** Frühere Widersprüche oder Klagen?
- **Dringlichkeit:** Droht Obdachlosigkeit? Einstweiliger Rechtsschutz (§ 86b SGG) nötig?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Mietrecht
- **Mietverhältnis:** Privat, sozial gefördert (WoBindG), Genossenschaft?
- **Anlassfall:** Kündigung (fristlos § 543 BGB, ordentlich § 573 BGB), Mieterhöhung (§§ 558 ff. BGB), Mängel (§ 536 BGB Minderung), Kaution (§ 551 BGB), Modernisierung (§§ 559 ff. BGB)?
- **Dokumente:** Mietvertrag, Kündigungsschreiben, Mieterhöhungsverlangen, Mietspiegel vorhanden?
- **Fristen:** Datum des Kündigungsschreibens / Mieterhöhungsverlangens? Gerichtstermin?
- **Mietspiegel:** Liegt ein qualifizierter Mietspiegel i. S. v. § 558d BGB vor? (Berlin: Berliner Mietspiegel 2023/2024)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Sozialklausel:** § 574 BGB – Widerspruch des Mieters gegen Kündigung? Härtegründe?
- **Dringlichkeit:** Räumungsklage anhängig? Vollstreckungsankündigung?

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

### Verbraucherrecht
- **Vertragsart:** Fernabsatz (§§ 312 ff. BGB), Energielieferung, Mobilfunk, Versicherung, Finanzierung?
- **Problem:** Widerrufsrecht abgelaufen? AGB-Klausel unwirksam (§§ 305–310 BGB)? Schuldnerberatung (kein RDG – an anerkannte Schuldnerberatung verweisen)?
- **Fristen:** Widerrufsfrist 14 Tage (§ 355 BGB); bei fehlender Belehrung: 12 Monate + 14 Tage.

### Familienrecht / SGB IX
- **Thema:** Unterhalt (§§ 1601 ff. BGB), Sorgerecht (§§ 1626 ff. BGB), Trennungsunterhalt (§ 1361 BGB), Gewalt (Gewaltschutzgesetz §§ 1–2 GewSchG)?
- **Kinder:** Minderjährige Kinder, Umgangsregelung, Kindeswohlgefährdung (§ 8a SGB VIII – Meldepflichten prüfen)?
- **SGB IX:** Eingliederungshilfe nach § 76b SGB IX (bes. für Geflüchtete mit Behinderung)?

## Triage-Klassifikation

| Klasse | Kriterium | Empfehlung |
|---|---|---|
| **Dringend** | Frist in ≤ 14 Tagen; drohende Abschiebung; Räumungsklage | Sofortige Rücksprache mit Anleiter; ggf. einstweiliger Rechtsschutz |
| **Regulär** | Frist > 14 Tage; Beratungsmandat ohne unmittelbaren Handlungsdruck | Normaler Ablauf |
| **Weitervermittlung** | Außerhalb RDG-Erlaubnis; Interessenkonflikt; zu komplex für Beratungsstelle | Verweis auf RAK-Vermittlung, Pro Bono Berlin/Bremen, VB-Zentrale |
| **Schuldnerberatung** | Überschuldung als Hauptthema | An anerkannte Schuldnerberatungsstelle (§ 305 Abs. 1 Nr. 1 InsO) verweisen |

## Fallprotokoll [Datum]

**Mandantenkennung:** [anonymisiert – z. B. M-2024-17]
**Fachbereich:** [Asylrecht | SGB II | Mietrecht | ...]
**Dringlichkeitsklasse:** [Dringend | Regulär | Weitervermittlung]
**Bearbeitende/r:** [Kürzel]

### Sachverhalt
[Knapper Fließtext, sachlich, keine Wertung]

### Rechtliche Fragestellungen (vorläufig)
1. ...
2. ...

### Konfliktprüfung
☑ Keine Interessenkonflikte festgestellt / ☐ Konflikt: [Beschreibung]

### Relevante Fristen
| Frist | Datum | Norm |
|---|---|---|
| ... | TT.MM.JJJJ | § ... |

### Empfohlene nächste Schritte (Entwurf)
1. ...

### Anleiterhinweis
[Punkte, die zwingend mit dem Anleiter besprochen werden müssen]
```

## Risiken / typische Fehler

- **Fristvergessenheit:** Datum der Zustellung sofort prüfen – nicht erst beim nächsten Termin. Bei § 36-Bescheid AsylG 1 Woche, bei § 74 AsylG sonst 2 Wochen oder 1 Monat – immer konkret berechnen.
- **Fehlende Konfliktprüfung:** Ohne Check kann § 43a Abs. 4 BRAO verletzt sein. Dann keine weiteren Informationen mehr entgegennehmen.
- **Sprachbarriere nicht dokumentiert:** Wenn der Mandant die Erläuterungen nicht verstanden hat, ist die Aufklärungspflicht nicht erfüllt.
- **Falsche Rechtsbereichszuordnung:** Asylmandat schlägt fast immer auf SGB II durch (§ 7 Abs. 1 Satz 2 SGB II: Leistungsausschluss für bestimmte Ausländer – prüfen!).
- **Entgeltlichkeit:** Kein Entgelt entgegennehmen – auch kein "freiwilliges Geschenk". Verletzt § 6 Abs. 2 Nr. 2 RDG (Unentgeltlichkeitspflicht) und ist bußgeldbewehrt (§ 20 RDG).

---

## Skill: `mandanten-kommunikations-log`

_Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO Datenschutz studentische Rechtsberatung, § 43a BRAO Vertraulichkeit, BDSG. Prüfrast..._

# /mandanten-kommunikations-log

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

1. Lade `CLAUDE.md` → Fachbereich, Aufsichtsmodell, Verschwiegenheitspflichten.
2. Prüfe: Handelt es sich um eine neue Kommunikation (→ Eintrag hinzufügen) oder um Abruf/Export (→ strukturierte Übersicht ausgeben)?
3. Erfasse alle relevanten Metadaten (Datum, Art, Beteiligte, Inhalt, Ergebnis, nächste Schritte).
4. Gib den neuen Logeintrag formatiert aus.
5. Weise auf offene Fristen und ausstehende Antworten hin.

---

### Mandantenkommunikations-Logbuch

## Zweck

Lückenlose Dokumentation aller Kontakte in einem Mandat ist aus mehreren Gründen unverzichtbar:

1. **Semesterübergabe:** Nachfolgende Studierende müssen den Stand des Mandats vollständig nachvollziehen können (`/rechtsberatungsstelle:semester-übergabe`).
2. **Haftungssicherung:** Im Streitfall muss nachgewiesen werden können, wann welche Mitteilung erging (§ 127 BGB analog für Fristwahrung).
3. **Qualitätssicherung:** Der anleitende Volljurist prüft, ob der Mandant korrekt informiert und keine unzulässige Rechtsberatung erteilt wurde.
4. **Verschwiegenheit:** Das Logbuch enthält personenbezogene Daten und fällt unter § 43a Abs. 2 BRAO (Anleiter), § 203 StGB (alle Beteiligten), DSGVO Art. 5, 9. Kein Zugang für Dritte ohne Freigabe.

## Berufsrechtlicher Rahmen

- § 43a Abs. 2 BRAO: Verschwiegenheitspflicht des anleitenden Anwalts.
- § 203 Abs. 1 Nr. 3 StGB: Unbefugte Offenbarung von Mandantengeheimnissen.
- § 50 BRAO: Aufbewahrungspflicht Mandantenakte mindestens 5 Jahre.
- DSGVO Art. 5 Abs. 1 lit. e: Speicherbegrenzung – keine unnötig langen Aufbewahrungszeiten.
- DSGVO Art. 9: Besondere Kategorien (Asylstatus, Gesundheitsdaten) – erhöhte Sorgfalt.

**Intern bleiben:** Logeinträge werden nicht an den Mandanten weitergegeben. Sie sind interne Arbeitsdokumentation.

## Eingaben

- Aktenzeichen oder anonyme Mandantenkennung (z. B. "M-2024-17")
- Datum und Uhrzeit des Kontakts
- Art des Kontakts: persönlich | telefonisch | schriftlich (Brief/E-Mail/Fax) | durch Dritte (Dolmetscher)
- Beteiligte: Studierender, Anleiter, Mandant, Behörde/Gericht, Dolmetscher
- Inhalt: Was wurde mitgeteilt / besprochen / vereinbart?
- Ergebnis: Was ist entschieden, was bleibt offen?
- Nächste Schritte und Fristen

## Logstruktur (Standardformat)

```
### Eintrag [Nummer] – [Datum] [Uhrzeit]

**Art:** [persönlich | telefonisch | schriftlich]
**Beteiligte:** [Studierender: Name/Kürzel] | [Anleiter: ✓ anwesend / – nicht anwesend] | [Mandant: ✓] | [Dolmetscher: Name/Sprache oder –]
**Gegenüber:** [Jobcenter Mitte Berlin | BAMF Bremen | VG Berlin | Mandant direkt | Sonstiges: ]
**Thema:** [Kurzbeschreibung, 1–2 Sätze]

**Inhalt:**
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

**Ergebnis / Stand:**
[Was ist beschlossen? Was wurde mitgeteilt? Was bleibt offen?]

**Offene Fristen:**
| Frist | Datum | Status |
|---|---|---|
| [z. B. Widerspruch SGB II] | [TT.MM.JJJJ] | [offen] |

**Nächste Schritte:**
1. [Aktion – verantwortlich: Studierender / Anleiter – bis: TT.MM.JJJJ]
2. …

**Verschwiegenheitshinweis:** Dieser Eintrag enthält vertrauliche Mandantendaten (§ 203 StGB, § 43a BRAO). Kein Zugang für Externe.
```

## Typische Kontaktarten und besondere Hinweise

### Erstgespräch / Intake
- Immer das Datum festhalten → Ausgangspunkt für Fristen (z. B. Jahresfrist AsylG § 74: Klagefrist läuft ab Bescheidzustellung, nicht ab Erstgespräch).
- Dokumentieren, ob Dolmetscher anwesend war und ob dieser selbst Verständlichkeit bestätigt hat.
- Datenschutz-Einwilligung des Mandanten nach Art. 13 DSGVO eingeholt?

### Behördenkontakt (Jobcenter, BAMF, Ausländerbehörde)
- Aktenzeichen der Behörde notieren.
- Bei telefonischen Auskünften: Name des Sachbearbeiters, Uhrzeit, Inhalt – wegen späterer Beweisbarkeit.
- Schriftliche Bestätigung mündlicher Auskünfte anfordern (Schreiben / E-Mail als Nachbeweis).

### Gerichtskontakt
- Geschäftsnummer des Gerichts notieren.
- Fristen aus dem Beschluss/Urteil sofort in `/rechtsberatungsstelle:fristen` eintragen.
- Termin für nächste Sitzung festhalten.

### Mandantenbrief / Schriftsatz
- Versanddatum und -weg (Brief mit Einschreiben / Fax mit Sendebericht / E-Mail mit Lesebestätigung) notieren.
- Anlagen auflisten.
- Freigabe durch Anleiter vor Versand? → Status "Freigabe erteilt von [Name/Kürzel] am [Datum]".

## Ablauf

### Schritt 1: Neuer Eintrag oder Abruf?

- Neue Kommunikation dokumentieren → Eingaben abfragen (Datum, Art, Beteiligte, Inhalt, Fristen).
- Bestehendes Log abrufen → Alle Einträge chronologisch ausgeben; Summary der offenen Fristen und nächsten Schritte.
- Log für Semesterübergabe exportieren → `/rechtsberatungsstelle:semester-übergabe` aufrufen.

### Schritt 2: Fristen prüfen

Nach jedem Eintrag automatisch prüfen:
- Gibt es neue Fristen aus diesem Kontakt?
- Sind bestehende Fristen durch diesen Kontakt beeinflusst (Hemmung, Verlängerung, Verkürzung)?
- Liegt eine kritische Frist innerhalb der nächsten 14 Tage?

Wenn ja: sofortige Benachrichtigung des Anleiters empfehlen.

### Schritt 3: Ausgabe

Strukturierter Logeintrag nach obigem Format. Immer mit Verschwiegenheitshinweis. Immer mit offenem Fristenstatus.

## Beispiel

### Eintrag 3 – 14.01.2025 14:30

**Art:** telefonisch
**Beteiligte:** Studierende: AS | Anleiter: – | Mandant: ✓ | Dolmetscher: Hamid Y. (Dari)
**Gegenüber:** Mandant direkt
**Thema:** Besprechung Widerspruchsergebnis Jobcenter – Bescheid vom 10.01.2025 erhalten

**Inhalt:**
- Mandant hat Bescheid vom Jobcenter Mitte Berlin (Az. 012345/24) am 12.01.2025 erhalten.
- Leistungen für Februar 2025 um 30 % abgesenkt (Sanktionsbescheid § 31a SGB II).
- Mandant versteht Bescheid nicht; Dolmetscher erklärt Inhalt auf Dari.
- Widerspruch soll eingelegt werden.

**Ergebnis / Stand:**
Mandant wünscht Widerspruch. Kopie des Bescheids wird per Post zugesandt. Frist läuft bis 12.02.2025 (1 Monat ab Bekanntgabe, § 84 SGG).

**Offene Fristen:**
| Frist | Datum | Status |
|---|---|---|
| Widerspruch SGB II § 84 SGG | 12.02.2025 | offen – dringend |

**Nächste Schritte:**
1. Entwurf Widerspruchsschreiben – verantwortlich: AS – bis: 20.01.2025
2. Freigabe durch Anleiter – bis: 28.01.2025
3. Versand per Einschreiben – bis: 10.02.2025 (Puffer)

**Verschwiegenheitshinweis:** Dieser Eintrag enthält vertrauliche Mandantendaten (§ 203 StGB, § 43a BRAO). Kein Zugang für Externe.

## Risiken / typische Fehler

- **Kein Versanddatum notiert:** Im Nachhinein nicht mehr beweisbar, ob eine Frist gewahrt wurde. Immer Einschreibebeleg aufbewahren und im Log festhalten.
- **Dolmetscher nicht dokumentiert:** Bei Sprachbarrieren ist der Nachweis, dass der Mandant den Inhalt verstanden hat, entscheidend (Aufklärungspflicht).
- **Offene Fristen nicht weitergegeben:** Beim Semesterwechsel sind nicht übergebene Fristen das größte Haftungsrisiko. Das Log ist die Grundlage für `/rechtsberatungsstelle:semester-übergabe`.
- **Personenbezogene Daten unverschlüsselt gespeichert:** DSGVO Art. 9 verlangt erhöhten Schutz für Asylstatus, Gesundheitsdaten. Kein Upload in unkonfigurierte Cloud-Systeme ohne Auftragsverarbeitungsvertrag (Art. 28 DSGVO).

---

## Skill: `mandantenbrief-memo-rbs-beratungshilfe`

_Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behörde oder Gericht vorbereiten. BeratungsHiG niedrigschwellige Beratung, Mandantenkommunikation in verstaendlicher Sprache...._

# /mandantenbrief

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

1. Lade `CLAUDE.md` → Fachbereich, Sprachniveau-Einstellungen, Anleiterpflicht.
2. Ermittle: Was soll der Brief mitteilen? Welchen nächsten Schritt soll der Mandant tun?
3. Schreibe den Brief in einfacher Sprache (Ziel: B1/B2; bei besonderen Bedarfen: leichte Sprache A2).
4. Kein Juristenjargon. Kurze Sätze. Aktive Formulierungen.
5. Ausgabe: Entwurf mit KI-Label. Versand erst nach Anleiterpfreigabe.

---

### Mandantenbrief in einfacher Sprache

## Triage zu Beginn
1. Was soll der Brief mitteilen: Ergebnis einer Pruefung, Verfahrensstand, konkreter naechster Schritt oder Ablehnung?
2. Auf welchem Sprachniveau soll der Brief verfasst werden: B1/B2 Standard oder Leichte Sprache A2 bei besonderem Bedarf?
3. Enthaelt der Brief Angaben ueber Dritte oder interne Bewertungen, die im Mandantenbrief nicht erscheinen duerfen?
4. Hat der anleitende Volljurist den Briefentwurf bereits freigegeben oder ist das Gate noch ausstehend?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- BORA § 11 — Mitteilungspflicht: Mandant ist ueber wesentliche Verfahrensschritte zu informieren
- § 43a Abs. 2 BRAO — Verschwiegenheit: Mandantenbrief darf keine Drittinformationen offenbaren
- § 6 Abs. 2 Nr. 2 RDG — Anleitungspflicht: Mandantenbrief von Studierenden erfordert Anleiterpruefung und -freigabe
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur für Mandanten bestimmte Informationen im Brief

## BORA-Pflichten bei Mandantenmitteilungen

- BORA § 11 (Handakten / Mitteilungspflichten): Der Anwalt (hier: der Anleiter) hat den Mandanten über wesentliche Verfahrensschritte zu informieren.
- BORA § 14: Rücksendung von Unterlagen und Abrechnung (hier: da unentgeltlich, primär Aktenführung).
- § 43a Abs. 2 BRAO: Keine Informationen über Dritte im Brief an den Mandanten preisgeben.
- Datenschutz: Im Brief nur Informationen, die für den Mandanten bestimmt sind. Keine internen Bewertungen, keine Drittdaten.

## Sprach- und Verständlichkeitsprinzipien

### Grundregeln (Ziel B1/B2)

| Regel | Schlecht | Besser |
|---|---|---|
| Kurze Sätze (max. 15 Wörter) | "Die Frist zur Einlegung des Widerspruchs beträgt nach § 84 SGG einen Monat ab Bekanntgabe des Bescheids." | "Sie haben einen Monat Zeit, um Widerspruch einzulegen. Die Frist beginnt mit dem Datum auf dem Bescheid." |
| Aktiv statt Passiv | "Der Widerspruch wird eingelegt." | "Wir legen Widerspruch ein." |
| Bekannte Wörter | "Klagefrist", "Begründetheit", "Subsumtion" | "Frist", "Grund für den Widerspruch" |
| Keine Abkürzungen ohne Erklärung | "SGB II § 22" | "Bürgergeld-Gesetz (Abschnitt über Wohnen)" |
| Handlungsorientierung | Nur Information | "Was Sie jetzt tun müssen: ..." |
| Freundlicher Ton | Amtsdeutsch | Persönliche, respektvolle Ansprache |

### Bei Geflüchteten / mehrsprachigem Kontext
- Brief auf Deutsch schreiben; wenn möglich parallel auf Arabisch / Dari / Tigrinya (mit Hinweis, dass dies kein Rechtsrat in der Zielsprache ist, sondern eine Orientierungshilfe).
- Keine Terminologie verwenden, die kulturell unterschiedlich verstanden wird (z. B. "Widerspruch" → erklären, was das ist).
- Ansprechperson und Erreichbarkeit der Beratungsstelle immer angeben.

## Briefstruktur (Standard)

```
[Briefkopf Beratungsstelle]
[Ort, Datum]

Betreff: [Ihr Verfahren – kurze, klare Beschreibung]

Guten Tag [Vorname Mandant],

wir beraten Sie in Ihrer Sache: [kurze Stichwortbeschreibung, 1 Satz].

**Was ist passiert?**
[1–3 Sätze: Was haben wir geprüft / Was ist zuletzt vorgefallen]

**Was bedeutet das für Sie?**
[1–3 Sätze: Ergebnis der Prüfung in verständlicher Sprache]

**Was passiert jetzt?**
[Konkrete nächste Schritte – nummeriert]
1. ...
2. ...

**Was müssen SIE tun?**
[Wenn der Mandant etwas tun muss – klar hervorgehoben, Frist nennen]
→ Bitte schicken Sie uns bis [TT.MM.JJJJ]: [Dokument / Information]
→ Bitte kommen Sie zu unserem nächsten Termin am: [Datum, Uhrzeit, Ort]

**Was darf ich nicht?**
[Ggf. Hinweis, was der Mandant nicht ohne uns tun sollte – z. B. "Bitte unterschreiben Sie keine neuen Dokumente des Jobcenters, ohne uns zu fragen."]

**Bei Fragen:**
Wenden Sie sich an: [Name des Studierenden / der Beratungsstelle]
Telefon: [...] | E-Mail: [...] | Sprechzeiten: [...]

Mit freundlichen Grüßen

[Name des Studierenden / Kürzel]
[Beratungsstelle]
[Rechtlicher Hinweis: Dieser Brief ist ein Entwurf, geprüft von [Anleiter].]
```

## Häufige Briefanlässe und Formulierungshilfen

### Widerspruch eingelegt (SGB II / SGB XII)
> "Wir haben für Sie am [Datum] Widerspruch gegen den Bescheid vom [Datum] eingelegt. Der Widerspruch heißt, dass wir dem Jobcenter schreiben: Der Bescheid ist nicht korrekt. Das Jobcenter muss jetzt prüfen, ob es recht hat. Das kann einige Wochen dauern. Wir informieren Sie, sobald eine Antwort kommt."

### Klage erhoben (Verwaltungsgericht / Sozialgericht)
> "Wir haben für Sie am [Datum] Klage beim [Gericht, Ort] eingereicht. Das Aktenzeichen ist: [AZ]. Sie erhalten möglicherweise einen Brief vom Gericht – bitte leiten Sie diesen sofort an uns weiter."

### Mietmangel-Schreiben an Vermieter
> "Wir haben Ihrem Vermieter am [Datum] geschrieben, dass die Wohnung [Mangel] hat. Wir haben ihn aufgefordert, das bis zum [Datum] zu reparieren. Wenn er das nicht tut, können Sie die Miete mindern. Das bedeutet: Sie zahlen weniger Miete, weil die Wohnung nicht in Ordnung ist. Wie viel weniger – das besprechen wir mit Ihnen."

### BAMF-Klage eingereicht
> "Wir haben fristgerecht Klage gegen den Bescheid des BAMF vom [Datum] eingereicht. Das Verwaltungsgericht [Ort] prüft jetzt Ihren Fall. Das Aktenzeichen der Klage ist: [AZ]. Der Aufenthalt ist während des Klageverfahrens sichergestellt (§ 81 Abs. 3 AufenthG). Bitte informieren Sie uns sofort, wenn Sie Post vom Gericht oder der Ausländerbehörde bekommen."

### Termin-Erinnerung
> "Ihr nächster Termin bei uns ist: [Datum], [Uhrzeit], [Adresse, Raum]. Bitte bringen Sie mit: [Aufzählung der Unterlagen]. Wenn Sie nicht kommen können: Bitte rufen Sie uns vorher an unter [Nummer]."

## Risiken / typische Fehler

- **Juristischer Rat im Mandantenbrief ohne Freigabe:** Kein Brief darf Aussagen enthalten wie "Sie werden gewinnen" oder "Die Klage hat gute Chancen" – das ist unzulässige Prognose ohne Anleiterbilligung.
- **Falsches Fristenverständnis beim Mandanten:** Der Brief muss Fristen, die der Mandant wahren muss (z. B. Vorlage von Dokumenten), klar und mit genauen Daten benennen. Keine vagen Formulierungen wie "möglichst bald".
- **Keine Rückfrage-Möglichkeit:** Mandantenbrief ohne Kontaktangabe ist wertlos. Immer Erreichbarkeit der Beratungsstelle angeben.
- **Vertraulichkeit verletzt:** Keine Drittdaten (z. B. Informationen über den Vermieter, den Arbeitgeber) im Brief an den Mandanten – es sei denn, der Mandant hat alle relevanten Informationen ohnehin selbst geliefert.

---

## Skill: `memo`

_Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit RECHERCHE ERFORDERLICH markiert, die Subsumtion mit STUDENTISCHE ANALYSE, das Erg..._

# Internes Rechtsgutachten: Gutachten-Gerüst

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Sachverhaltsnotizen / Aktennotiz** — Fakten des Falls; fehlende Angaben werden markiert
- **Rechtsgebiet** — z. B. Mietrecht, Arbeitsrecht, Verwaltungsrecht, Verbraucherrecht
- **Spezifische Rechtsfrage** (optional) — falls der Fokus auf einer bestimmten Frage liegen soll
- **Forschungsstand** (optional) — bereits recherchierte Normen oder Urteile, die eingeflossen sind

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 6 RDG** — Rechtsdienstleistungen durch studentische Beratungsstellen: zulässig als unentgeltliche Rechtsdienstleistung unter anwaltlicher Aufsicht. Das Gutachten ist ein internes Arbeitsmittel und kein Rechtsgutachten im Sinne eines anwaltlichen Leistungsprodukts.
- **§ 43a Abs. 2 BRAO / § 203 StGB** — Mandatsgeheimnis: Das Gutachten enthält vertrauliche Mandanteninformationen und darf die Beratungsstelle nicht ohne Supervisoren-Freigabe verlassen.
- Materialrecht des jeweiligen Rechtsgebiets (wird im Gutachten konkretisiert).

### Leitentscheidungen (exemplarisch für häufige Rechtsgebiete)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

### Schritt 1: Rechtsfragen formulieren

Aus den Fallnotizen: Welche rechtlichen Fragen stellt dieser Fall?

Jede Frage als Obersatz formulieren. Nicht "Mietrecht" — sondern: "Kann die Mandantin die Miete mindern, weil die Heizung seit November defekt ist, und wenn ja, in welcher Höhe?"

Wenn mehrere Fragen vorliegen, bekommt jede ihren eigenen Prüfungsblock.

### Schritt 2: Gutachten-Gerüst aufbauen

Für jede Frage:

**Obersatz:** Als Fragesatz formuliert (aus Schritt 1).

**Norm/Definition:** Dies ist eine Recherche-Lücke, keine Schlussfolgerung. Was der/die Studierende finden muss:

> `[RECHERCHE ERFORDERLICH: § 536 BGB — Mietminderung wegen Sachmangel;
> Voraussetzungen: erheblicher Mangel, Anzeige durch Mieter (§ 536c BGB),
> keine Kenntnis bei Vertragsschluss (§ 536b BGB). Starten Sie mit:
> § 536 BGB, dann Rspr. zu Heizungsausfall als erheblicher Mangel.
> Vgl. /recherche-start für einen Recherchefahrplan.]`

Falls der Skill einen allgemeinen Normrahmen mit hoher Sicherheit kennt, kann dieser als Ausgangspunkt benannt werden — aber ausdrücklich als ungeprüft markiert:

> *Normrahmen (ungeprüft — für [Bundesland/Gericht] verifizieren):* § 536 Abs. 1 BGB
> gibt dem Mieter einen Anspruch auf verhältnismäßige Herabsetzung der Miete,
> wenn die Mietsache zu Mietbeginn oder während der Mietzeit mit einem Mangel
> behaftet ist, der ihre Tauglichkeit zum vertragsmäßigen Gebrauch aufhebt oder
> mindert. Die Minderung tritt kraft Gesetzes ein; einer Erklärung bedarf es nicht.
> `[PRÜFEN: aktuelle Fassung und einschlägige Rspr. für diesen Sachverhalt]`

**Subsumtion:** Hier steht die Analyse des Studierenden. Gerüst strukturieren, nicht ausfüllen:

> `[STUDENTISCHE ANALYSE: Norm auf Sachverhalt anwenden. Relevante Tatsachen:
> - Heizung seit November defekt — seit wann ist dies ein "erheblicher" Mangel?
> - Wann und wie hat die Mandantin den Vermieter informiert (§ 536c BGB)?
> - Ist ein Minderungsausschluss nach § 536b BGB möglich?
> - Wie hoch ist der Minderungsprozentsatz (Rspr. zu Heizungsausfall prüfen)?]`

**Ergebnis:** Bewusst offen lassen:

> `[STUDENTISCHES ERGEBNIS: Welche Schlussfolgerung ergibt sich aus Norm und
> Subsumtion? Wie stark ist der Anspruch? Welche Gegenargumente sind zu erwarten?]`

### Schritt 3: Stärken, Schwächen, offene Fragen

Separater Abschnitt nach den Prüfungsblöcken:

**Stärken (aus dem Sachverhalt — Studierende/-r soll diese testen):**
- [Hilfreiche Tatsache und warum]

**Schwächen (aus dem Sachverhalt — Studierende/-r soll Gewicht abschätzen):**
- [Problematische Tatsache und warum]
- `[UNSICHER: ob [X] tatsächlich eine Schwäche ist — hängt von [Norm/Rspr.] zu [Y] ab]`

**Offene Fragen (aus dem Gutachten nicht beantwortbar):**
- Sachverhaltlich: [Was wissen wir nicht über den Mandanten/die Mandantin?]
- Rechtlich: [Was erfordert Recherche?]
- Strategisch: [Ermessensentscheidungen für Studierenden/Supervisor]

## Kurzergebnis

[Mandat annehmen / Ablehnen, weil X / Weitere Informationen zu Y erforderlich —
nächster Schritt: Z]

---

## Geprüfte Fragen

1. [Frage als Obersatz]
2. [Frage als Obersatz]

---

## Frage 1: [Obersatz]

### Norm / Definition

[Normrahmen als Ausgangspunkt mit PRÜFEN-Flags und RECHERCHE ERFORDERLICH-Blöcken]

### Subsumtion

[STUDENTISCHE ANALYSE — Gerüst mit den relevanten Tatsachen]

### Ergebnis

[STUDENTISCHES ERGEBNIS — bewusst offen]

---

[Wiederholung für jede weitere Frage]

---

## Stärken

[Liste mit Vorbehalten]

## Schwächen

[Liste mit UNSICHER-Flags, wo zutreffend]

## Offene Fragen

**Sachverhaltlich:** [Liste]
**Rechtlich:** [Liste — diese fließen in /recherche-start ein]
**Strategisch:** [Liste — dies ist die Agenda für das Supervisorengespräch]

---

## Recherchelücken-Zusammenfassung

[Alle RECHERCHE ERFORDERLICH-Blöcke in einer Liste, damit der/die Studierende
sie systematisch abarbeiten kann — und /recherche-start für jede starten kann]

═══════════════════════════════════════════════════════════════════════
```

## Beispiel

**Szenario:** Mandant Koch, Mieter einer 3-Zimmer-Wohnung. Heizung defekt seit 01.11.2025. Vermieter nach mündlicher Anzeige vom 05.11.2025 untätig. Mandant zahlt weiter volle Miete 1.200 €/Monat.

Obersatz: "Hat Herr Koch einen Anspruch auf Mietminderung nach § 536 Abs. 1 BGB und wenn ja, in welcher Höhe?"

Normblock enthält: `[RECHERCHE ERFORDERLICH: § 536 BGB, § 536c BGB (Anzeigepflicht), Rspr. zu Heizungsausfall als erheblicher Mangel — AG/LG München, AG Hamburg; Höhe des Minderungsprozentsatzes]`. Subsumtionsblock enthält: `[STUDENTISCHE ANALYSE: Anzeigepflicht am 05.11.2025 erfüllt? Schriftform? Wie viele Monate betroffen?]`. Ergebnisblock offen.

## Risiken und typische Fehler

- **Analyse ohne Recherche ausfüllen:** Die RECHERCHE ERFORDERLICH-Blöcke sind keine Formalität. Ein Gutachten mit ungefüllten oder voreilig abgehakten Normblöcken ist noch kein Gutachten.
- **Unsicherheiten stillschweigend übergehen:** Wenn ein UNSICHER-Flag gesetzt ist, ist das ein Hinweis zur Recherche oder zum Supervisorengespräch, kein Tippfehler.
- **Kurzergebnis ohne Analyse:** Das Kurzergebnis am Anfang des Gutachtens ist eine Orientierung; es muss durch die Prüfungsblöcke belegt sein.
- **Gutachten verlässt Klinik ohne Freigabe:** Das interne Gutachten enthält vertrauliche Mandanteninformationen (§ 203 StGB, § 43a Abs. 2 BRAO). Kein Versand ohne Supervisoren-Freigabe.
- **Falsches Prüfungsschema:** Das Gerüst folgt der üblichen deutschen Gutachtenreihenfolge. Abweichende Prüfungsreihenfolgen (z. B. Prozessvoraussetzungen zuerst im Verwaltungsrecht) müssen vom Studierenden eigenständig berücksichtigt werden.

## Quellenpflicht

Jeder im Gerüst vorgeschlagene Normrahmen oder Entscheidungshinweis ist mit der Herkunft zu kennzeichnen: `[juris]`, `[beck-online]`, `[dejure]` für datenbankgestützte Belege; `[Modellwissen — verifizieren]` für aus dem Modell stammende Hinweise. Hinweise mit "verifizieren" tragen ein höheres Fehlerrisiko und sind zuerst zu prüfen. Tags nicht entfernen — sie sind das schnellste Signal für den Supervisor, welche Stellen besonderer Aufmerksamkeit bedürfen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Befund: KORRIGIERT. Skill hatte falschen Thementext: "Verbraucherrecht: Widerruf nach § 355 BGB". Echtes Thema: Eigenbedarfskündigung; Suizidgefahr des Mieters als Haertegrund (§ 574 BGB); Fortsetzung des Mietverhaeltnisses auf unbestimmte Zeit. Fundstelle korrigiert: NZM 2023 35 Rn. 24 (statt NJW 2023 142 Rn. 20). Quelle: dejure.org/2022,33020.
-->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

