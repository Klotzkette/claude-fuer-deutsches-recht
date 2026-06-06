---
name: portfolio-status
description: "Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: nicht Einzelmandat-Briefing im Prozessrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Prozessportfolio-Status

## Arbeitsbereich

Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: nicht Einzelmandat-Briefing. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Übersicht

1. **Filterung:** Nur aktive Mandate, alle Mandate oder nur Mandate mit bevorstehenden Fristen?
2. **Risikofilter:** Sollen nur Hochrisiko-Mandate (über Wesentlichkeitsschwelle) angezeigt werden?
3. **Veraltete Mandate:** Sollen Mandate ohne Aktivität (z.B. länger als 30 Tage keine Aktualisierung) markiert werden?
4. **Ausgabeformat:** Tabellarische Übersicht, Briefing für Vorstandssitzung oder Detailansicht pro Mandat?
5. **CLAUDE.md geladen:** Ist das Praxisprofil (Risikokalibrierung, Wesentlichkeitsschwelle) aktuell?

## Zentrale Normen
- § 43a Abs. 3 BRAO (Sorgfaltspflicht — Fristenkontrolle)
- § 43a Abs. 6 BRAO (Pflicht zur zeitnahen Mandatsbearbeitung)
- § 196 BGB (Verjährung von Ansprüchen auf Übertragung von Rechten)
- § 232 ff. ZPO (Fristen und Wiedereinsetzung)
- § 233 ZPO (Wiedereinsetzung in den vorigen Stand bei Fristversäumnis)

## Rechtsprechung (ergänzt)
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Eine Abfrage, die beantwortet: Was führe ich gerade, was erfordert Aufmerksamkeit, was droht zu versanden? Die Ausgabe ist auf schnelles Überfliegen ausgelegt — geeignet für einen Anwalt, der drei Minuten vor dem nächsten Termin hat. Lädt bei allen Anfragen zu einer Gesamtübersicht aktiver oder aller Prozessmandate.

## Eingaben

- **Mandatsprotokoll `_log.yaml`**: Primärquelle
- **Kanzleikonfiguration `CLAUDE.md`**: Risikokalibrierung (zur korrekten Auslegung der Risiko- und Wesentlichkeitsfelder)
- **Flags** (optional): `--alle`, `--risiko=hoch`, `--veraltet`, `--typ=arbeitsrecht`, `--verantwortlicher=[Name]`

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 1 BRAO i.V.m. § 11 BORA** — Sorgfaltspflicht; lückenlose Fristen- und Sachstandskontrolle als Berufspflicht; Verfahren ohne aktuellen Eintrag können auf Versäumnisse hinweisen.
- **§§ 214–233 ZPO; §§ 516, 520, 548, 569 ZPO** — Fristen im Zivilprozess; versäumte Fristen sind einer der häufigsten Anwaltshaftungsgründe.
- **§ 317 StPO** — Berufungsfrist im Strafverfahren (eine Woche ab Urteilsverkündung); besondere Überwachungspflicht.
- **§ 74 VwGO** — Klagefrist im Verwaltungsgerichtsverfahren (ein Monat); versäumt grundsätzlich nicht wiedereinsetzungsfähig.
- **§ 249 HGB** — Rückstellungspflicht für drohende Verluste aus schwebenden Rechtsstreitigkeiten; relevant für die Wesentlichkeitsklassifizierung.
- **§ 285 Nr. 3a HGB; § 340e Abs. 3 HGB** — Offenlegung wesentlicher Rechtsstreitigkeiten im Jahresabschluss; Berührungspunkt mit der Wesentlichkeitskennzeichnung.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1: Kontext laden

`_log.yaml` einlesen; `CLAUDE.md` → Risikokalibrierung lesen.

### Schritt 2: Filtern

Standard: nur aktive Mandate (`status != geschlossen`).

**Flags:**
- `--alle` → geschlossene Mandate einschließen
- `--risiko=hoch` (oder `kritisch` / `mittel` / `niedrig`) → nach Risikostufe filtern
- `--veraltet` → nur Mandate mit `zuletzt_aktualisiert` > 30 Tage
- `--typ=arbeitsrecht` → nach Mandatstyp filtern
- `--verantwortlicher=[Name]` → nach internem Verantwortlichen filtern

### Schritt 3: Übersicht erstellen

(Vorlage siehe Ausgabeformat)

### Schritt 4: Auffälligkeiten prüfen

Sieben Prüfregeln (Details im Abschnitt Auffälligkeitsregeln).

### Schritt 5: Entscheidungsbaum ausgeben

Abschluss mit Nächste-Schritte-Entscheidungsbaum gemäß Kanzleikonfiguration `## Ausgaben`. Optionen an die Ausgabe anpassen (Entwurf erstellen, eskalieren, weitere Fakten beschaffen, beobachten, anderes). Bei mehr als ca. 10 Mandaten oder auf Anfrage: Dashboard-Angebot (Risikoverteilung, Fristatimeline, sortierbare Mandatsliste mit Status und letztem Bearbeitungsdatum).

## Ausgabeformat

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

# Prozessportfolio-Status — [heute]

**Aktive Mandate:** [N]
**Geschlossen (lfd. Jahr):** [N] *(nur bei --alle)*

---

## Nach Risiko

| Risiko | Anzahl | Mandate |
|---|---|---|
| Kritisch | [N] | [Bezeichnungen] |
| Hoch | [N] | [Bezeichnungen] |
| Mittel | [N] | [nur Anzahl — mit `--risiko=mittel` ausklappen] |
| Niedrig | [N] | [nur Anzahl] |

## Bevorstehende Fristen

| Zeitraum | Mandate |
|---|---|
| 14 Tage | [Bezeichnung — Frist — Kurzbeschreibung] |
| 15–30 Tage | [...] |
| 31–60 Tage | [...] |

*Überfällige Fristen werden gesondert im Auffälligkeitsabschnitt markiert.*

## Wesentlichkeit

| Kategorie | Anzahl | Gesamt-Exposure (Mittelwert) |
|---|---|---|
| Rückgestellt | [N] | [EUR X] |
| Offengelegt | [N] | [EUR X] |
| Beobachtet | [N] | — |
| Keine | [N] | — |

## Nach Verfahrensstadium

[Tabelle: Klageerhebung / Beweisaufnahme / mündliche Verhandlung / Rechtsmittel / Vergleich / vollständige Erledigung]

---

## Auffälligkeiten

- **Überfällige Fristen:** [Mandate mit vergangener `nächste_frist`]
- **Veraltet (>30 Tage kein Update):** [Liste]
- **Interessenkonfliktprüfung offen:** [Mandate mit `konfliktstatus: ausstehend` oder `nicht-durchgeführt`]
- **Interessenkonflikt überbrückt (Override aktiv):** [Mandate mit aktivem Override — dauerhaft markiert bis manuell gelöscht]
- **Hohes/kritisches Risiko ohne externe Bevollmächtigte:** [Liste]
- **Rückstellung ohne Update seit >60 Tagen:** [Liste — Neubewertung der Rückstellung wahrscheinlich überfällig]
- **Keine Beweissicherungsanordnung bei laufendem Prozess:** [Liste]
- **Fehlende Pflichtfelder:** [Bezeichnung → Feld]

---

## Handlungsempfehlung

[Ein bis zwei Sätze — was zuerst anschauen, falls etwas wirklich heraussticht. Kein Boilerplate — nur wenn etwas tatsächlich auffällig ist.]
```

## Beispiel

**Sachverhalt:** Portfolio mit 8 aktiven Prozessmandaten. Zwei Mandate haben Fristen in den nächsten 14 Tagen. Ein Mandat wurde seit 45 Tagen nicht aktualisiert. Ein Mandat ist mit kritischem Risiko ohne externe Bevollmächtigte.

**Auffälligkeiten-Ausgabe:**

```
- Überfällige Fristen: keine
- Veraltet (>30 Tage): bauer-ag-revision-2024 (45 Tage)
- Kritisches Risiko ohne externe Bevollmächtigte: mueller-gmbh-strafverfolgung-2025
 → Empfehlung: unverzüglich externe Strafverteidigung mandatieren
```

## Auffälligkeitsregeln

1. **Überfällige Frist:** `nächste_frist < heute` und `status != geschlossen`
2. **Veraltet:** `zuletzt_aktualisiert < heute - 30 Tage` und `status != geschlossen`
3. **Interessenkonflikt offen:** `konfliktstatus in [ausstehend, nicht-durchgeführt]` und `status != geschlossen`
4. **Override aktiv:** `konflikt_override.durch != null` (löscht sich nicht automatisch)
5. **Hohes Risiko ohne Bevollmächtigte:** `risiko in [hoch, kritisch]` und `externe_bevollmaechtigte.sozietaet == null`
6. **Veraltete Rückstellung:** `wesentlichkeit == rückgestellt` und `zuletzt_aktualisiert < heute - 60 Tage`
7. **Fehlende Beweissicherung:** `status in [angedroht, aktiv, beweisaufnahme, verhandlung, rechtsmittel]` und `beweissicherung.angeordnet == false` — Sicherungspflicht setzt bei vernünftiger Erwartung eines Verfahrens ein, also auch bei angedrohten Klagen (Risikovorsatz)
8. **Fehlende Pflichtfelder:** beliebiges Pflichtfeld `null` — `risiko`, `wesentlichkeit`, `status`, `eroeffnet`, `konfliktstatus`

## Risiken und typische Fehler

- **Scheingenaue Exposure-Summen:** Exposure-Mittelwerte sind grob und sollten als solche gekennzeichnet sein.
- **Kein Ersatz für ein Aktenverwaltungssystem (MACS/Kanzleisoftware):** Dies ist eine Arbeitsspeicher-Übersicht, kein Aktensystem.
- **Stille Entscheidungen:** Der Skill stellt Fragen, trifft keine Prioritätsentscheidungen für den Nutzer.
- **Risikoklassifizierung:** Die Risikostufen werden aus dem Protokoll gelesen — eine schlechte Datenpflege führt zu einer schlechten Übersicht.

## Quellenpflicht

- Gesetzestexte: §§ 43a BRAO; § 11 BORA; §§ 214 ff., 516, 520, 548, 569 ZPO; § 317 StPO; § 74 VwGO; §§ 249, 285 HGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
