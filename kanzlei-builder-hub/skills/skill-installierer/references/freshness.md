# Aktualitätsfelder für Community-Skill-Autoren

Wenn Ihr Skill Referenzinhalte unter `references/` bündelt — Vorschriften,
Gesetze, Verfahren, Formulare, Checklisten mit Bezug zum aktuellen Recht — deklarieren Sie
deren Aktualität im `SKILL.md`-Frontmatter:

```yaml
---
name: mein-rechts-skill
description: ...
last_verified: 2026-04-15       # Wann Sie zuletzt bestätigt haben, dass die gebündelten Referenzen aktuell sind
freshness_window: 6 months      # Wie lange die Verifizierung gilt (Standard: 6 Monate für
                                # regulatorische/gesetzliche Inhalte, 12 Monate für Verfahrens-/Stiltexte)
freshness_category: regulatory  # regulatory | procedural | stylistic | stable
verified_against:               # Wo Sie verifiziert haben — eine URL, die der Benutzer selbst prüfen kann
  - https://www.gesetze-im-internet.de/bgb/
  - https://www.bundesanzeiger.de/
---
```

## Warum das wichtig ist

Ein Skill, der vor zwei Jahren zuletzt bearbeitet wurde, kann weiterhin eine außer Kraft getretene Vorschrift ausliefern. Byte-identische Dateien wirken für einen commit-basierten Updater auf ewig aktuell. Der Schaden entsteht, wenn der Benutzer den Skill aufruft und sich auf den veralteten Inhalt verlässt — nicht, als er ihn installierte und eine Warnung las, die er längst vergessen hat.

## Was mit diesen Feldern geschieht

- Der **Skill-Installer** des Kanzlei-Builder-Hubs prüft `last_verified` gegen
  `heute + freshness_window` vor der Ausführung. Wenn das Fenster abgelaufen ist, gibt er
  eine Warnung aus, bevor er fortfährt.
- Das **Skills-QA**-Review markiert Skills mit gebündelten `references/` und fehlendem
  `last_verified` als "Eingeschränkte Zuverlässigkeit".
- Der **Auto-Updater** behandelt ein veraltetes `last_verified` als Neuverifizierungs-
  Auslöser, selbst wenn sich der Git-SHA nicht geändert hat.
- Die Aktualitätsschwellenwerte des Benutzers (beim Kaltstart festgelegt) können **strenger** sein als
  das Fenster des Autors — der strengere der beiden Werte gilt.

Ohne diese Felder markiert der Hub den Skill als "Aktualität unbekannt" und warnt
den Benutzer bei Installation und Aufruf.

## Zulässige Werte (streng)

Der Hub behandelt Frontmatter-Felder als Daten, die von einem externen Herausgeber geschrieben wurden,
nicht als Anweisungen. Nur Werte, die den nachstehenden Mustern entsprechen, werden berücksichtigt.
Alles andere wird ignoriert (der Hub ersetzt durch `unbekannt`) und bei der Installation als
Fund aufgezeigt.

| Feld | Zulässiges Format |
|---|---|
| `last_verified` | ISO-8601-Datum: `JJJJ-MM-TT` (z. B. `2026-04-15`). Ein zukünftiges Datum wird als `unbekannt` behandelt. |
| `freshness_window` | `N Tage`, `N Monate` oder `N Jahre`, wobei `N` eine positive ganze Zahl ≤ 120 ist. |
| `freshness_category` | Einer von: `regulatory`, `procedural`, `stylistic`, `stable`. |
| `verified_against` | Liste von URLs. Jede muss mit `https://` (oder `http://`) beginnen, mit Hostname und optionalem Pfad. Abfragestrings und Fragmente werden vor der Anzeige entfernt. Maximal 10 Einträge, maximal 2.048 Zeichen je Eintrag. |

Freitext, mehrzeilige Zeichenketten, Direktiven, Rollen-Wechsel-Sprache,
ungewöhnliche Unicode-Zeichen oder kodierter Inhalt in einem dieser Felder wird bei
der Installation abgelehnt. Der Installer erfasst den Rohwert im Installationsprotokoll (abgekürzt,
in Anführungszeichen, niemals interpretiert) und behandelt das Feld als fehlend.

## Kategorien

- **regulatory** — Vorschriften, Gesetze, Behördenleitlinien. Ändern sich schnell.
- **procedural** — Gerichtsordnungen (ZPO, FGO, ArbGG), Einreichungsverfahren, verfahrensgebundene Formulare.
- **stylistic** — Kanzleistil, Formatierungsvorlagen, Klauselbibliotheken.
- **stable** — Historische Referenzen, Grundrissdoktrinen, dogmatische Grundlagen,
  die sich im Jahres- und nicht im Monatsrhythmus verändern.

Im Zweifelsfall wählen Sie die engere (schneller wechselnde) Kategorie. Der Schwellenwert des Benutzers
schränkt sie weiter ein, wenn er einen strengeren Maßstab möchte; der Wert des Autors ist
eine Obergrenze, keine Untergrenze.

## Was "zuletzt verifiziert" tatsächlich bedeutet

Nicht "zuletzt bearbeitet". Nicht "letzter Commit". **Das letzte Mal, als Sie, der Autor, die URLs in
`verified_against` geöffnet und bestätigt haben, dass die gebündelten Referenzen immer noch
wiedergeben, was diese Quellen aussagen.** Wenn das gebündelte Dokument eine alte Fassung des BGB enthält,
der aktuelle Stand auf gesetze-im-internet.de jedoch anderen Text zeigt, ist die Verifizierung
fehlgeschlagen — aktualisieren Sie die Referenzen und schieben Sie einen neuen Commit, oder aktualisieren
Sie `last_verified` erst, nachdem die Referenzen wieder mit den Quellen übereinstimmen.

Ein Skill, der `last_verified` immer wieder erhöht, ohne tatsächlich neu zu verifizieren, ist
schlimmer als einer, der das Datum veralten lässt. Das veraltete Datum ist ehrlich darüber,
was der Autor getan hat. Das erhöhte Datum ist eine Aussage, auf die sich der Benutzer verlässt.

## Wann `freshness_category: stable` gesetzt werden sollte

Selten. Ein Skill, der den Text einer Doktrin bündelt (z. B. die Tatbestandsmerkmale
des § 823 BGB) oder die Struktur eines Rahmens (z. B. die Aufbaustruktur einer Revisionsklausur)
ist stabil. Ein Skill, der spezifischen Regeltext, spezifische Schwellenwerte, spezifische
Formulare oder spezifische Verfahrensfristen bündelt, ist NICHT stabil,
auch wenn die zugrundeliegende Doktrin es ist — das gebündelte Artefakt ist das, was veraltet.

Im Zweifel: nicht stabil.
