---
name: mandat-briefing-schliessen-portfolio-status
description: "Mandat Briefing Schliessen Portfolio Status: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandat Briefing Schliessen Portfolio Status

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandat Briefing Schliessen Portfolio Status** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mandat-briefing` | Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Termin. Abgrenzung: nicht Zeugenvorbereitung (eigener Skill). |
| `mandat-schliessen` | Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussbericht Mandat. Abgrenzung: nicht laufende Mandat-Aktualisierung. |
| `portfolio-status` | Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: nicht Einzelmandat-Briefing. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Mandat Briefing Schliessen Portfolio Status**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mandat-briefing`

**Fokus:** Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Termin. Abgrenzung: nicht Zeugenvorbereitung (eigener Skill).

# Mandat-Briefing

## Zweck

Erzeugung eines strukturierten Tiefenbriefings zu einem einzelnen Mandat auf Basis der `mandat.md` und `verlauf.md`. Das Briefing fasst den aktuellen Verfahrensstand zusammen, identifiziert offene Handlungspunkte, prüft die nächste Frist und bewertet das Prozessrisiko neu. Einsatz vor Mandantengesprächen, GC/Justiziarssitzungen, Außenanwalts­telefonate oder vor internen Review-Terminen.

## Eingaben

- Mandat-Slug
- Optional: Fokusthema (`--frist`, `--risiko`, `--naechste-schritte`)
- Optional: Empfänger (`--mandant`, `--justiziar`, `--anwalt`) – steuert Detailgrad und Stil

## Ablauf

1. **Mandatsdaten laden:** `mandate/[slug]/mandat.md` und `mandate/[slug]/verlauf.md` einlesen.

2. **Verfahrensstand zusammenfassen:**
 - Parteien, Gericht, Aktenzeichen
 - Verfahrensstadium (Klagezustellung, Schriftsatzphase, Beweisaufnahme, Urteil, Rechtsmittel, Vollstreckung)
 - Ansprüche / Streitgegenstand (§ 264 ZPO)
 - Bisheriger Verfahrensverlauf (Chronologie der Verfahrenshandlungen)

3. **Entwicklungen seit letztem Update:**
 - Letzte Eintrag in verlauf.md identifizieren
 - Neue Schriftsätze, Gerichtsentscheidungen, Vergleichsgespräche

4. **Fristen-Check:**
 - Nächste Frist (Schriftsatzfrist, Berufungsfrist, Urteilsfrist, Vollstreckungsverjährung)
 - Risiko-Frist (in roter Zone wenn < 14 Tage)

5. **Offene Handlungspunkte:**
 - Was muss der Anwalt noch erledigen?
 - Was ist von der Gegenseite / dem Gericht ausstehend?
 - Welche Beweise fehlen noch?

6. **Risikoneueinschätzung:**
 - Änderung der Risikoeinschätzung seit letztem Intake? (BGH-Rechtsprechung, neue Sachverhalte)
 - Expositionsschätzung (untere / mittlere / obere Schadenswert-Bandbreite)
 - Vergleichspotential (§ 278 Abs. 1 ZPO: Gericht soll in jeder Lage des Verfahrens auf Vergleich hinwirken)

7. **Ausgabe:** Strukturiertes Briefing-Memo im Urteilsstil oder als Executive Summary.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
MANDAT-BRIEFING
──────────────────────────────────────
Mandat: [Slug]
Parteien: [Kläger] ./. [Beklagter]
Gericht / Az.: [Gericht], Az. [JJJJ] [Aktenzeichen]
Verfahrensstufe: [z. B. Berufung – OLG Frankfurt]
Stand: TT.MM.JJJJ
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
1. VERFAHRENSSTAND
──────────────────────────────────────
[Kurzdarstellung: Wo sind wir? Was wurde bisher eingereicht / entschieden?]

──────────────────────────────────────
2. ENTWICKLUNGEN SEIT [DATUM LETZTES UPDATE]
──────────────────────────────────────
[Neue Schriftsätze, Urteile, Korrespondenz]

──────────────────────────────────────
3. NÄCHSTE FRIST
──────────────────────────────────────
⚠️ [Frist] – [Beschreibung] – [Datum]

──────────────────────────────────────
4. OFFENE HANDLUNGSPUNKTE
──────────────────────────────────────
□ [Punkt 1]
□ [Punkt 2]

──────────────────────────────────────
5. RISIKOEINSCHÄTZUNG
──────────────────────────────────────
Expositionsschätzung: EUR [X] – EUR [Y]
Risikostufe: 🔴 hoch / 🟡 mittel / 🟢 gering
Vergleichspotential: [Einschätzung]
```

## Risiken / typische Fehler

- **Veraltete mandat.md:** Ohne regelmäßige Updates per `/mandat-update` liefert das Briefing einen falschen Stand; nach jeder Entwicklung updaten.
- **Fristversäumnis-Risiko:** Das Briefing ersetzt nicht den Fristenkalender; jede Frist muss separat in das Kanzlei-Fristbuch eingetragen werden.
- **Vertraulichkeit des Briefings:** Das Briefing enthält Mandatsgeheimnisse; Empfängerkreis sorgfältig wählen (§ 43a Abs. 2 BRAO); nicht per unverschlüsselter E-Mail versenden.

<!-- AUDIT 27.05.2026
Halluzinierte Referenz geloescht. Keine Ersatzquelle gefunden.
-->

## 2. `mandat-schliessen`

**Fokus:** Mandat nach Prozessabschluss formal schließen: Kostenfestsetzung, Archivierung, Mandanteninformation. Normen: §§ 103 ff. ZPO, RVG. Prüfraster: Kostenfestsetzungsantrag, Ergebnismitteilung, Handaktenfreigabe. Output: Abschlussbericht Mandat. Abgrenzung: nicht laufende Mandat-Aktualisierung.

# Mandat schließen

## Zweck

Strukturierter Abschluss eines Mandats im Portfolio: Ergebnis dokumentieren, Kosten und Honorar abrechnen, Lehren festhalten, Mandat aus dem aktiven Portfolio in den Archivstatus überführen. Der Datensatz bleibt dauerhaft erhalten (Aufbewahrungspflicht § 50 Abs. 1 BRAO: 6 Jahre nach Mandatsende).

## Eingaben

- Mandat-Slug
- Abschlusstyp: `--urteil`, `--vergleich`, `--klagerücknahme`, `--erledigungserklärung`, `--einstellung`, `--sonstiges`
- Ergebnis (kurz): Wer hat gewonnen, was wurde vereinbart, welcher Betrag?

## Ablauf

1. **Abschlusstype und Ergebnis erfassen:**

 | Typ | Relevante Normen |
 |---|---|
 | Urteil (Endurteil) | §§ 300 ff. ZPO; Rechtskraft § 322 ZPO |
 | Anerkenntnisurteil | § 307 ZPO |
 | Versäumnisurteil | §§ 330 ff. ZPO |
 | Vergleich | §§ 794 Abs. 1 Nr. 1, 278 ZPO; vollstreckbar |
 | Klagerücknahme | §§ 269, 270 ZPO; Kostenfolge § 269 Abs. 3 ZPO |
 | Erledigungserklärung | § 91a ZPO; Kostenbeschluss |
 | Einstellung (Strafrecht) | §§ 153, 153a, 170 Abs. 2, 204 StPO |
 | Verfahrensvergleich (Verwaltungsrecht) | § 106 VwGO |

2. **Endexposition berechnen:**
 - Gezahlter Betrag / auferlegte Leistung
 - Kostenfestsetzung (§§ 103 ff. ZPO): eigene Kosten + erstattete / zu erstattende Kosten
 - Vergleich mit ursprünglicher Risikoschätzung (Intake-Wert)

3. **Honorar und Gebühren:**
 - Letzte Abrechnung nach RVG (§ 8 RVG: Fälligkeit mit Mandatsbeendigung)
 - Offene Vorschüsse (§ 9 RVG) zurückerstatten oder verrechnen
 - Fremdgelder abwickeln (§ 43a Abs. 5 BRAO: unverzügliche Weiterleitung)

4. **Lessons Learned:**
 - Was lief gut / schlecht?
 - Prozessführungsempfehlung für künftige vergleichbare Mandate?
 - BGH- oder OLG-Urteile, die im Mandat relevant waren und für spätere Mandate zu merken sind?

5. **Handakte archivieren (§ 50 BRAO):**
 - Handakte für mind. 6 Jahre nach Mandatsende aufbewahren
 - Elektronische Akte: gleichwertige Sicherung (§ 50 Abs. 2 BRAO)
 - Herausgabepflicht auf Verlangen (§ 50 Abs. 3 BRAO)

6. **Portfolio-Log aktualisieren:** Status in `_log.yaml` auf `archiv` setzen; Abschlussdatum, Ergebnis, Endexposition eintragen.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- BRAO § 50 (Aufbewahrungspflicht Handakten: 6 Jahre); § 43a Abs. 5 BRAO (Fremdgelder).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
MANDAT-ABSCHLUSS
──────────────────────────────────────
Mandat-Slug: [slug]
Schließungsdatum: TT.MM.JJJJ
Typ: [z. B. Vergleich]
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
ERGEBNIS
──────────────────────────────────────
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

──────────────────────────────────────
ENDEXPOSITION
──────────────────────────────────────
Eingeklagter Betrag: EUR XX.XXX
Vergleichszahlung: EUR XX.XXX
Kostenerstattung: EUR X.XXX (§§ 103 ff. ZPO)
Ursprüngliche Schätzung: EUR XX.XXX – EUR XX.XXX

──────────────────────────────────────
LESSONS LEARNED
──────────────────────────────────────
[Freitext]

──────────────────────────────────────
ARCHIVIERUNG
──────────────────────────────────────
Handakte aufzubewahren bis: TT.MM.JJJJ (§ 50 Abs. 1 BRAO: 6 Jahre)
_log.yaml-Status: archiv
```

## Risiken / typische Fehler

- **Aufbewahrungsfrist übersehen:** § 50 Abs. 1 BRAO: mindestens 6 Jahre nach Mandatsende; kürzere Vernichtung ist Berufsrechtsverletzung.
- **Fremdgelder nicht abgewickelt:** § 43a Abs. 5 BRAO – Fremdgelder (Kostenvorschüsse, Schadensersatzbeträge) unverzüglich weiterleiten; Verzögerung kann zur Strafbarkeit führen (§ 266 StGB).
- **Rechtsmittelfrist läuft noch:** Vor dem Schließen prüfen, ob Berufungs- (§ 517 ZPO: 1 Monat) oder Revisionsfrist (§ 548 ZPO: 1 Monat) noch offen ist; Mandat erst nach Eintritt der Rechtskraft schließen oder Mandanten ausdrücklich auf Verzicht hinweisen.
- **Vollstreckungsverjährung:** Vollstreckungstitel verjähren nach § 197 Abs. 1 Nr. 3 BGB in 30 Jahren; Abschluss nicht ohne Dokumentation der Vollstreckungsmaßnahmen.

<!-- AUDIT 27.05.2026
Halluzinierte Referenz geloescht. Keine Ersatzquelle gefunden.
-->

## 3. `portfolio-status`

**Fokus:** Statusuebersicht aller laufenden Prozessmandate: Fristen, Verfahrensstand, naechste Schritte. Normen: ZPO, RVG. Prüfraster: Fristenliste, offene Anträge, Termine, Mahnfristen. Output: Portfolio-Statusbericht Prozessmandate. Abgrenzung: nicht Einzelmandat-Briefing.

# Prozessportfolio-Status

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
