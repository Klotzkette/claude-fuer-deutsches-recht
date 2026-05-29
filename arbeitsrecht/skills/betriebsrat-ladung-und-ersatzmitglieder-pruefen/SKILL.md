---
name: betriebsrat-ladung-und-ersatzmitglieder-pruefen
description: "Workflow-Skill zu betriebsrat ladung und ersatzmitglieder pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Betriebsrat — Ladung und Ersatzmitglieder prüfen

## Rechtsgrundlagen

- **§ 25 Abs. 2 BetrVG** — Reihenfolge der nachrückenden Ersatzmitglieder; gehört zu den wesentlichen und unverzichtbaren Verfahrensvorschriften
- **§ 29 Abs. 2 BetrVG** — Einberufung und Ladung; Tagesordnung; Ladung von Ersatzmitgliedern
- **§ 33 BetrVG** — Beschlussfähigkeit; Mehrheitsbeschluss
- **§ 24 BetrVG** — Erlöschen der Mitgliedschaft
- **§ 25 Abs. 1 BetrVG** — Nachrücken in den Betriebsrat
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Warum diese Prüfung — Anker für die ganze Beschlussfassung

Ein Betriebsratsbeschluss ist nur wirksam, wenn das Gremium ordnungsgemäß zusammengesetzt war. Schwerpunkte:

1. **Wer war ordentliches Mitglied?** (Wahlperiode, etwaige Erlöschen-Tatbestände nach § 24 BetrVG)
2. **Wer war geladen?** (§ 29 Abs. 2 BetrVG — rechtzeitig, mit Tagesordnung)
3. **Wer war verhindert?** (Krankheit, Urlaub, dienstliche Abwesenheit, Interessenkollision)
4. **Wer hätte als Ersatzmitglied nachrücken müssen?** (§ 25 Abs. 2 BetrVG — Nachrückreihenfolge)
5. **Wer hat tatsächlich teilgenommen?**
6. **Stimmen Ladung, Verhinderung und tatsächliche Besetzung überein?**

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Workflow

### Schritt 1: Sitzungsdaten zusammenstellen

```
□ Datum der Betriebsratssitzung
□ Tagesordnung (war auf der Ladung vermerkt?)
□ Vorsitzender bzw. Stellvertreter, der die Sitzung leitete
□ Protokoll der Sitzung — vollständig vorhanden?
□ Liste der ordentlichen Betriebsratsmitglieder zum Sitzungszeitpunkt
□ Liste der Ersatzmitglieder mit Listenherkunft und Nachrückreihenfolge
```

### Schritt 2: Verhinderungen erfassen

Für jedes ordentliche Mitglied:

```
□ War das Mitglied an dem Sitzungstag verhindert?
   → Urlaub (geplant, im Voraus bekannt)
   → Krankheit (kurzfristig, wann genau bekannt geworden?)
   → Dienstliche Abwesenheit
   → Befangenheit / Interessenkollision in einer Tagesordnungs-Sache
   → Erlöschen der Mitgliedschaft (§ 24 BetrVG)
□ Wann wurde die Verhinderung bekannt?
   → Vor dem Sitzungstag: rechtzeitige Nachladung möglich → war erforderlich
   → Am Sitzungstag: Beurteilungsspielraum des Vorsitzenden
     Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
□ Dokumentierte Mitteilung der Verhinderung?
```

### Schritt 3: Nachrückreihenfolge prüfen (§ 25 Abs. 2 BetrVG)

Bei Verhinderung muss das **richtige** Ersatzmitglied geladen werden:

```
□ Wahl mit Listenwahl oder Mehrheitswahl?
   → Listenwahl: Ersatzmitglied stammt aus DERSELBEN Liste wie das
     verhinderte ordentliche Mitglied (Listentreue)
   → Mehrheitswahl: Ersatzmitglieder nach Stimmenzahl
□ Innerhalb der Liste: Reihenfolge nach dem festgestellten Wahlergebnis
□ Geschlechterquote (§ 15 Abs. 2 BetrVG) — Minderheitsgeschlecht
   muss bei der Nachrückreihenfolge beachtet werden
□ Ist das richtige Ersatzmitglied geladen worden?
□ Ist das richtige Ersatzmitglied erschienen?
□ Hat es an der Abstimmung teilgenommen?
```

### Schritt 4: Quorum und Mehrheit (§ 33 BetrVG)

```
□ War der Betriebsrat beschlussfähig?
   (mehr als die Hälfte der Mitglieder anwesend, § 33 Abs. 2 BetrVG)
□ Wurde der Beschluss mit Mehrheit der abgegebenen Stimmen gefasst?
□ Stimmenthaltungen korrekt behandelt (zählen nicht als Ja-Stimme)?
```

### Schritt 5: Bewertung und Folge

```
□ Alle vorstehenden Punkte erfüllt?
   → Beschluss wirksam

□ Verstoß gegen Nachrückreihenfolge (§ 25 Abs. 2 BetrVG)?
   Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
   → ABER: Heilung möglich (→ Skill `betriebsrat-beschluss-heilung-nachtraeglich`)

□ Verstoß gegen Ladungsvorschriften (§ 29 Abs. 2 BetrVG)?
   → Grundsätzlich Unwirksamkeit
   → Heilung durch neuen Beschluss möglich (→ Heilungs-Skill)

□ Verhinderung erst am Sitzungstag bekannt und Vorsitzender hat
   keine Nachladung versucht?
   Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
   → Beurteilungsspielraum des Vorsitzenden
   → Beschluss bleibt wirksam, wenn das Quorum auch ohne
     Nachladung erreicht war
```

## Häufige Fehlerquellen

| Fehler | Folge | Heilbar? |
|----|----|----|
| Ersatz Nr. 2 der Liste geladen, obwohl Ersatz Nr. 1 verfügbar | Beschluss unwirksam | Ja (BAG 25.09.2024) |
| Ersatzmitglied aus falscher Liste geladen | Beschluss unwirksam | Ja |
| Geschlechterquote nicht beachtet bei Nachrücken | Beschluss unwirksam | Ja |
| Tagesordnung nicht oder zu spät mitgeteilt | Beschluss unwirksam | Ja |
| Quorum nicht erreicht | Beschluss unwirksam | Nein — neue Sitzung mit Quorum nötig |
| Verhinderung erst am Sitzungstag bekannt, keine Nachladung | Regelmäßig kein Fehler | — (BAG 20.05.2025) |
| Vorsitzender lädt nicht selbst (oder Stellvertreter) | Beschluss unwirksam | Ja |

## Anwendungsbeispiel

**Mandat**: Der Betriebsrat hat in einer Sitzung am 14. März die Beauftragung eines Rechtsanwalts für ein Beschlussverfahren beschlossen. Der Arbeitgeber wendet ein, der Beschluss sei unwirksam, weil das Ersatzmitglied X anstelle des verhinderten Y teilgenommen hat — obwohl auf derselben Liste das Ersatzmitglied Z davor stehe.

**Prüfung mit dem Workflow**:
1. Sitzungsdaten zusammenstellen (Schritt 1) → Y war ordentlich, war krank
2. Verhinderung erfassen (Schritt 2) → bestätigt, Krankschreibung vom Vortag
3. Nachrückreihenfolge prüfen (Schritt 3) → Tatsächlich hätte Z geladen werden müssen, X stand erst danach
4. Quorum (Schritt 4) → war auch ohne X erreicht, aber X hat mitgestimmt
5. Bewertung (Schritt 5) → Beschluss **unwirksam** wegen § 25 Abs. 2 BetrVG

**Folge**: Wechsel zum Skill `betriebsrat-beschluss-heilung-nachtraeglich` — kann der Betriebsrat den Beschluss in einer Folgesitzung nachträglich heilen?

## Querverweise

- → `betriebsrat-beschluss-heilung-nachtraeglich` — Heilungsmöglichkeit bei festgestelltem Fehler
- → `betriebsrat-anhoerung` — formgerechte Anhörung des Betriebsrats vor Kündigung
- → `kuendigungsschutz-grundlagen`
