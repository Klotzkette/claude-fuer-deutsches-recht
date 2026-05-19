# mandantenkommunikation/ — fallbezogene Kommunikationsprotokolle

Ein Ordner pro Fall. Darin ein fortlaufendes `log.md`, das jeden Mandantenkontakt dokumentiert — eingehend und ausgehend, per Telefon, E-Mail, Textnachricht, Brief und persönlichem Gespräch. Erstellt und fortgeschrieben durch `/rechtsberatungsstelle:mandantenkommunikation-protokoll`.

## Verzeichnisstruktur

```
mandantenkommunikation/
├── _README.md                     # diese Datei
└── [fall-id]/
    └── log.md                     # fortlaufendes Protokoll (nur Ergänzungen)
```

## Slug

Entspricht der Fall-ID, die auch in der Aufnahmeakte und in `deadlines.yaml` unter `case_id` verwendet wird. Ein Fall = ein Ordner.

## Zweck dieses Verzeichnisses

- **Haftungsschutz** — „Wir haben X am Datum Y mitgeteilt" erfordert einen schriftlichen Beleg.
- **Kontinuität bei Übergaben** — die übernehmenden Studierenden können das Protokoll lesen und kennen den Sachverhalt des Mandanten, ohne ihn erneut befragen zu müssen.
- **Muster erkennen** — fünf nicht zurückgerufene Nachrichten in sechs Wochen ist ein Hinweiszeichen, das der Aufsicht gemeldet werden sollte.
- **Mandantenakten-Aufbewahrung** — Rechtsberatungsstellen haben Aufbewahrungspflichten für Akten; dieses Protokoll ist Teil der vollständigen Akte.

## Aufbau der Protokolleinträge

```markdown
## [JJJJ-MM-TT HH:MM] — [eingehend / ausgehend] — [Kontaktweg]

**Wer (Studierende/r):** [Name]
**Wer (Mandantenseite):** [Name des Mandanten, oder Dritter, z. B. bei Anruf durch Gegenanwalt]
**Dauer / Umfang:** [10-minütiges Telefonat | 3-absätzige E-Mail | 2-seitiger Brief]

**Zusammenfassung:**
[Was ist vorgefallen, 2–4 Sätze. Inhalt und — soweit relevant — Ton des Gesprächs.]

**Aufgaben:**
- [Aufgabe, die die/der Studierende dem Mandanten schuldet, mit Frist]
- [Aufgabe, die der Mandant der/dem Studierenden schuldet, mit erwartetem Zeitpunkt]

**Wiedervorlage:** [Datum, sofern zutreffend]

**Hinweise:**
[Was relevant ist, aber oben keinen Platz findet — verwendete Sprache, beobachtete Familiendynamik, erkennbare Belastung des Mandanten]
```

## Was dieses Verzeichnis NICHT enthält

- Inhaltliche Fallanalysen (diese gehören in die Aufnahmeakte, das Rechtsgutachten oder die Statusdateien)
- Entwürfe von Schriftstücken (diese liegen in gesonderten Fallordnern)
- Nur intern zugängliche Anwaltsnotizen (diese verbleiben im internen Fallnotiz-System der Beratungsstelle)

Das Kommunikationsprotokoll ist eine sachliche Kontaktdokumentation, kein anwaltliches Arbeitsergebnis. Inhaltliches gehört ins Protokoll; Strategie und Rechtsanalyse verbleiben andernorts.

## Aufbewahrung

Nur Ergänzungen, keine nachträglichen Änderungen. Wenn ein Eintrag falsch war oder einer Erläuterung bedarf, ist ein neuer Eintrag mit Bezug auf den alten hinzuzufügen. Der Nachweis, was wann gesagt wurde, ist Bestandteil der Mandantenakte; eine nachträgliche Bearbeitung widerspricht dem Sinn der Dokumentation.
