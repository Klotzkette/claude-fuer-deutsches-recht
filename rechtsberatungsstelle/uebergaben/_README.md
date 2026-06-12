# übergaben/ — Übergabevermerke zum Semesterende

Semesterbezogener Ordner mit je einem Übergabevermerk pro aktivem Fall. Erstellt durch `/rechtsberatungsstelle:semester-uebergabe` am Semesterende. Zu lesen von den übernehmenden Studierenden im Rahmen von `/einarbeitung` für die ihnen zugewiesenen Fälle.

## Verzeichnisstruktur

```
uebergaben/
├── _README.md                             # diese Datei
└── [JJJJ-semester]/                       # z. B. 2026-sommersemester, 2026-wintersemester
    ├── _zusammenfassung.md                # fallübergreifende Übersicht: wer übergibt was an wen
    ├── [fall-id].md                       # ein Vermerk pro aktivem Fall
    └── ...
```

## Slug- und Ordnerkonventionen

Semesterordner: `[Jahr]-[sommersemester|wintersemester]`. Beispiele:
- `2026-sommersemester`
- `2026-wintersemester`

Fallvermerk: Fall-ID verwenden (aus `deadlines.yaml` oder der Aufnahmeakte). Konsistent mit den übrigen fallbezogenen Dateien.

## Inhalt eines Übergabevermerks

- Fallzusammenfassung (Sachverhalt, Rechtsgebiet, aktueller Verfahrensstand)
- Name der/des abgebenden Studierenden und — soweit relevant — aufgebaute Beziehung zum Mandanten
- Ausstehende Fristen (aus `deadlines.yaml`)
- Offene Fragen und noch ausstehende Entscheidungen
- Kommunikationsverlauf (aus `mandantenkommunikation/[fall-id]/log.md`)
- Bislang erstellte oder eingereichte Schriftstücke (Verweise auf Fallordner)
- Was die übernehmende Studierende / der übernehmende Studierende wissen und zuerst tun muss
- Hinweise der Lehrperson für die übernehmende Person (sofern vorhanden)

## Ablauf

1. `/rechtsberatungsstelle:semester-uebergabe` wird von der Lehrperson (oder von den abgebenden Studierenden für ihre eigenen Fälle) etwa 1–2 Wochen vor Semesterende ausgeführt.
2. Es entstehen fallbezogene Vermerke sowie eine Gesamtzusammenfassung.
3. Die übernehmenden Studierenden führen zu Beginn des nächsten Semesters `/rechtsberatungsstelle:einarbeitung` aus; `/einarbeitung` legt die Übergabevermerke für die jeweils zugewiesenen Fälle offen.

## Aufbewahrung

Übergabevermerke verbleiben dauerhaft im Verzeichnis. Historische Übergaben sind für die eigene Dokumentation der Beratungsstelle über Fallübergänge nützlich sowie für Studierende, die die Entwicklung eines Falls über mehrere Semester nachvollziehen wollen.
