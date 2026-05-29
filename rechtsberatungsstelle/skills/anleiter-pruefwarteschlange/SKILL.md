---
name: anleiter-pruefwarteschlange
description: 'Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell "formelle Prüfwarteschlange" gewählt wurde; andernfalls inaktiv. Lädt, wenn der Supervisor sehen möchte, was auf Prüfung wartet, einen Eintrag freigibt, bearbeitet und freigibt oder mit einem Hinweis zurückschickt.'

---

# Supervisoren-Prüfwarteschlange (Optional)

## Zweck

Manche Beratungsstellen wollen ein formelles Gate: Studierendenentw[urf], Supervisoren-Prüfung, dann Freigabe. Andere finden das zu starr — sie begleiten über Fallgespräche und Einzelgespräche, nicht über eine Warteschlange.

**Diese Skill ist nur aktiv, wenn die Klinik-Konfiguration (CLAUDE.md) unter "Supervisionsmodell" die Option "formelle Prüfwarteschlange" gewählt hat.** Andernfalls ist sie inaktiv — beim Kalt-Start-Interview entscheidet der Supervisor, welches Modell er/sie möchte; dies ist eine von drei Optionen.

Ob eine formelle Prüf-Ablauf sinnvoll ist, hängt vom Erfahrungsstand der Studierenden, der Fallzahl und der bestehenden Betreuungsstruktur ab. Der Supervisor entscheidet beim Kalt-Start und kann die Einstellung jederzeit ändern.

**Rechtlicher Hintergrund:** Die Prüfwarteschlange dokumentiert, dass ein zugelassener Rechtsanwalt/eine zugelassene Rechtsanwältin studentische Arbeitsergebnisse geprüft hat, bevor sie Mandanten, Gerichte oder Behörden erreichten. Dies ist die institutionelle Umsetzung der Aufsichtspflicht nach § 6 Abs. 2 RDG.

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
  typ: "entwurf"  # aufnahme | entwurf | memo | status | mandantenbrief
  mandant: "[Name oder ID]"
  studierender: "[Name]"
  eingereicht: [Zeitstempel]
  flags:
    - regel: "Gerichtliche Einreichung"
      detail: "Klageschrift AG — immer in Warteschlange"
  inhaltspfad: "[Pfad zum Dokument]"
  status: "ausstehend"  # ausstehend | freigegeben | bearbeitet-freigegeben | zurückgeschickt
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

## Ausgabeformat

Markdown-Tabellen nach dem Warteschlangen-Anzeigeschema oben. Einzelne Einträge werden mit vollständigem Inhalt, Flag-Begründung und Studierenden-Notizen angezeigt.

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
