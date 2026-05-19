# gegenseite-status/ — wöchentliche Statusanfragen an Korrespondenzanwalt/Gegenseite

Ausgabe von `/prozessrecht:gegenseite-status`. Pro Lauf ein datierter Ordner; darin je eine Markdown-Datei pro bearbeitetem Mandat sowie eine `_zusammenfassung.md`.

## Verzeichnisstruktur

```
gegenseite-status/
├── _README.md                       # diese Datei
└── [JJJJ-MM-TT]/
    ├── _zusammenfassung.md          # was wurde ausgeführt, was wurde übersprungen und warum
    ├── [slug-1].md                  # ein E-Mail-Entwurf pro Mandat
    ├── [slug-2].md
    └── ...
```

Wenn der Outlook-Konnektor authentifiziert ist, werden zusätzlich Outlook-Entwürfe im Postfach des Nutzers angelegt. Die Markdown-Dateien sind der dauerhafte Nachweis; die Outlook-Entwürfe sind die Handlungsebene.

## Rhythmus

Wöchentlich (montags, früh) wenn zeitgesteuert. Zeitsteuerung einrichten mit `/prozessrecht:gegenseite-status --zeitsteuerung-einrichten`.

Anlassbezogen jederzeit mit `/prozessrecht:gegenseite-status` (Standardfilter) oder `/prozessrecht:gegenseite-status --slug=[slug]` (ein einzelnes Mandat).

## Pflege

Ältere datierte Ordner häufen sich an. Nach Eingang der Antwort der Gegenseite und Aktualisierung des Mandatsverlaufs werden sie nicht mehr benötigt. Ordner, die älter als 30 Tage sind, können gelöscht werden.
