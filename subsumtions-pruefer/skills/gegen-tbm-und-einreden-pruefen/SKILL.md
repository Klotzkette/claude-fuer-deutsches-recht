---
name: gegen-tbm-und-einreden-pruefen
description: "Prüft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden: Nichtigkeitsgründe, Anfechtung, Erfuellung, Aufrechnung, Verjährung, Zurückbehaltungsrecht, Verwirkung, Verzicht. Strukturierte Gegenprüfung nach Anspruchsaufbau."
---

# Gegen-TBM und Einreden prüfen

## Triage zu Beginn — kläre vor der Gegenprüfung

1. Ist der Anspruch dem Grunde nach bereits positiv subsumiert?
2. Welche Einwendungen hat der Anspruchsgegner erhoben oder könnte er erheben?
3. Besteht eine Aufrechnungslage (§§ 387 ff. BGB)? — fällig, gleichartig, gegenseitig?
4. Ist Verjährung eingreifend? → Skill `verjaehrung-fristen-pruefen` parallel nutzen
5. Hat der Gläubiger durch sein Verhalten einen Vertrauenstatbestand gesetzt? → Verwirkung prüfen

## Zweck

Nach der positiven Subsumtion (Anspruch entstanden dem Grunde nach) prüft dieser Skill, ob Einwendungen oder Einreden des Anspruchsgegners den Anspruch ausschließen, vernichten oder hemmen. Dieser Schritt ist zwingend, bevor ein Ergebnis ausgegeben wird.

## Zentrale Paragrafenkette

- §§ 104-113 BGB — Geschäftsfähigkeit (rechtshindernde Einwendung bei Mangel)
- § 125 BGB — Nichtigkeit wegen Formmangels
- §§ 119, 120, 123 i.V.m. § 142 Abs. 1 BGB — Anfechtung (ex tunc-Nichtigkeit)
- §§ 305-310 BGB — AGB-Recht, Einbeziehung und Inhaltskontrolle
- § 362 BGB — Erfüllung als rechtsvernichtende Einwendung
- §§ 387-396 BGB — Aufrechnung (Aufrechnungslage, Aufrechnungserklärung)
- § 397 BGB — Erlass (vertraglicher Forderungsverzicht)
- §§ 194-217 BGB — Verjährung (Einrede, nicht Einwendung — § 214 BGB)
- § 273 BGB, § 320 BGB — Zurückbehaltungsrecht, Einrede des nicht erfüllten Vertrags
- § 242 BGB — Verwirkung (Treu und Glauben)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Systematik der Gegenrechte

### 1. Rechtshindernde Einwendungen (Anspruch entsteht gar nicht)

Rechtshindernde Einwendungen verhindern die Entstehung des Anspruchs:
- **Geschäftsunfähigkeit** (§ 104 BGB): Rechtsgeschäft nichtig; Anspruch nie entstanden
- **Formmangel** (§ 125 BGB): Nichtigkeit bei Nichteinhaltung der gesetzlichen Form
- **Sittenwidrigkeit / Gesetzesverstoß** (§§ 134/138 BGB): Nichtigkeit
- **Anfechtung** (§§ 119/120/123 BGB i.V.m. § 142 Abs. 1 BGB): Nichtigkeit ex tunc (rückwirkend)
- **AGB-Unwirksamkeit** (§§ 305 ff. BGB): Klausel nicht wirksam einbezogen oder inhaltlich unwirksam
- **Unmöglichkeit bei Vertragsschluss** (§ 311a BGB): Primärleistungspflicht entfällt

### 2. Rechtsvernichtende Einwendungen (Anspruch ist erloschen)

- **Erfüllung** (§ 362 BGB): Leistung bewirkt; Anspruch erloschen
- **Aufrechnung** (§§ 387 ff. BGB): Gegenforderung des Schuldners; Fälligkeit, Gleichartigkeit, Aufrechnungslage
- **Erlass** (§ 397 BGB): Vertraglicher Verzicht auf Forderung
- **Rücktritt** (§§ 346 ff. BGB): Rückabwicklung; Rücktrittsrecht muss vorliegen
- **Widerruf** (§§ 355 ff. BGB): Verbraucherverträge; Widerrufsfrist 14 Tage; beginnt mit ordnungsgemäßer Belehrung

### 3. Rechtshemmende Einreden (Anspruch besteht, ist aber nicht durchsetzbar)

- **Verjährung** (§§ 194 ff. BGB): Einrede, nicht Einwendung; muss erhoben werden (§ 214 BGB). Regelfall: 3 Jahre, Kenntnis ab Jahresende. Details in Skill `verjaehrung-fristen-pruefen`.
- **Zurückbehaltungsrecht** (§ 273 BGB / § 320 BGB): Leistung Zug-um-Zug; Fälligkeit der Gegenforderung
- **Einrede des nicht erfüllten Vertrags** (§ 320 BGB): Vorleistungspflicht beachten
- **Stundung**: Fälligkeit noch nicht eingetreten

### 4. Verwirkung (§ 242 BGB)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Mitverschulden (§ 254 BGB)

Kein vollständiger Ausschluss, aber Kürzung des Anspruchs. Das System fragt: Hat der Anspruchsteller selbst zum Schaden beigetragen? Welcher Anteil?

## Entscheidungsbaum Gegenprüfung

```
Ist ein Nichtigkeitsgrund vorhanden?
├─ Ja → rechtshindernde Einwendung → Anspruch nicht entstanden
└─ Nein → Ist ein Erlöschensgrund vorhanden?
          ├─ Ja → rechtsvernichtende Einwendung → Anspruch erloschen
          └─ Nein → Liegt eine Einrede vor (Verjährung, ZBR, § 320)?
                    ├─ Ja (und erhoben) → Anspruch nicht durchsetzbar
                    └─ Nein → Mitverschulden § 254 BGB prüfen → Quote
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Tabelle aller geprüften Gegenrechte mit Ergebnis (eingreifend / nicht eingreifend / fraglich). Gesamtergebnis: Anspruch besteht vollständig / gemindert / nicht durchsetzbar / nicht entstanden.

**Adressat:** Richter/Anwalt — Tonfall sachlich-juristisch

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

<!-- AUDIT 27.05.2026
-->
