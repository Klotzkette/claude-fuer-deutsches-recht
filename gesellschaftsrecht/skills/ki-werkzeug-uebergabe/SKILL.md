---
name: ki-werkzeug-uebergabe
description: 'KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer "Luminance", "Kira", "KI-Prüfung", "automatische Extraktion" oder "Massenprüfung" erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die ein einheitliches Klausel-Extraktionsprofil erfordern.'

---

# KI-Tool-Übergabe (Luminance / Kira)

## Triage zu Beginn

Vor der Tool-Ubergabe klaeren:

1. **Volumen:** Wie viele Dokumente sind im Datenraum? (< 50: manuelle Prüfung effizienter; 50-200: bedingt sinnvoll; > 200: KI-Tool empfohlen)
2. **Tool vorhanden?** Ist Luminance, Kira oder ein vergleichbares Tool bereits im Praxisprofil konfiguriert? Welches Vertrauensniveau ist eingestellt?
3. **Kategorien:** Sind die Verträge bereits grob kategorisiert (Lieferanten, Kunden, IP, Miet-, Arbeitsverträge)?
4. **AVV geklaert?** Liegt ein Auftragsverarbeitungsvertrag (Art. 28 DSGVO) mit dem Tool-Anbieter vor? Hat der Mandant der Weitergabe zugestimmt?
5. **Rechtsordnung:** Werden auch Verträge nach auslaendischem Recht gepüft? (gesondertes Profil erforderlich)
6. **QA-Ressourcen:** Wer fuehrt die Stichproben-QA durch? Wie viel Zeit steht zur Verfuegung?

## Zentrale Normen

§ 398 BGB (Forderungsabtretung) — § 399 BGB (Abtretungsverbot) — § 354a HGB (Abtretungsverbot unter Kaufleuten; ggf. unwirksam) — §§ 305 ff. BGB (AGB-Kontrolle) — § 307 BGB (unangemessene Benachteiligung) — § 613a BGB (Betriebsubergang; Vertragsuebergang) — §§ 69b, 43 UrhG (Arbeitnehmererfindung) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Datenweitergabe) — § 130 OWiG (Aufsichtspflichtverletzung bei Compliance-Verstoss)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

In M&A-Mandaten mit Datenräumen von 100+ Verträgen übersteigt manuelle Einzelprüfung das verfügbare Zeitbudget. Dieser Skill strukturiert die Übergabe an ein KI-Prüftool (Luminance, Kira oder vergleichbar), legt das Extraktionsprofil fest, QA-checkt die Ausgabe und steuert die Rückübernahme in den DD-Issue-Extraktion-Ablauf.

## Eingaben

- Praxisprofil: `## M&A → KI-gestützte Prüfung` (Tool-Name, Verwendungszweck, Vertrauensniveau, Übergabe-Ablauf)
- VDR-Inventar oder Ordnerliste mit Kategorien
- Klausel-Extraktionsprofil (Standardprofil unten oder Hausformat aus Praxisprofil)
- Anzahl Dokumente in der Übergabecharge
- Deal-Code und Datenraumstruktur

## Ablauf

### Schritt 1: Kategorie-Triage

Nicht jede Kategorie ist für KI-Massenprüfung geeignet. Einschätzen:

| Kategorie | Eignet sich für KI-Tool | Begründung |
|---|---|---|
| Wesentliche Verträge (>50 gleichartige) | ✓ | Standardklauseln, hohes Volumen |
| Rahmenverträge / MSA | ✓ | Strukturierte Klauseln |
| IP-Lizenzverträge | Bedingt | Komplexe Terminologie; Stichproben-QA |
| Arbeitsverträge | Bedingt | Länderspezifische Normen; § 307 BGB |
| Gesellschaftsverträge / Satzungen | ✗ | Besprechungs- und Kontextbedarf |
| Side Letters / Anpassungsvereinbarungen | ✗ | Zu nuanciert für Bulk-Extraktion |

### Schritt 2: Extraktionsprofil erstellen

Für jede Vertragsart ein Extraktionsprofil mit den zu extraktierenden Klauseln erstellen:

**Standardprofil M&A – deutsches Recht:**

```yaml
extraktionsprofil:
  change_of_control:
    frage: "Gibt es eine Change-of-Control-Klausel? Ist Zustimmung erforderlich?"
    rechtsgrundlage: "Kein gesetzliches Zustimmungserfordernis; rein vertragliche Regelung"
    relevanz: "Zustimmungserfordernis vor Vollzug"
  kuendigungsrecht_abtretung:
    frage: "Gibt es ein Kündigungsrecht oder Abtretungsverbot bei Eigentümerwechsel?"
    rechtsgrundlage: "§ 398 BGB (Abtretung), § 613a BGB (Betriebsübergang)"
    relevanz: "Hemmt Vollzug oder Vertragsübertragung"
  wettbewerbsverbot:
    frage: "Enthält der Vertrag ein Wettbewerbs- oder Exklusivitätsverbot?"
    rechtsgrundlage: "§ 138 BGB (Sittenwidrigkeit), Bindung nach UWG"
    relevanz: "Schränkt Käufer-Geschäft ein"
  haftungsbegrenzung:
    frage: "Gibt es eine Haftungsobergrenze? In welcher Höhe? AGB oder Individualvereinbarung?"
    rechtsgrundlage: "§§ 305 ff. BGB (AGB-Kontrolle); § 309 Nr. 7 BGB"
    relevanz: "Risikoquantifizierung; AGB-Unwirksamkeit prüfen"
  ip_eigentum:
    frage: "Wer ist Eigentümer der erzeugten IP? Enthält der Vertrag eine Abtretung?"
    rechtsgrundlage: "§§ 69b, 43 UrhG (Arbeitnehmererfindung); § 7 ArbNErfG"
    relevanz: "IP-Kette zum Zielunternehmen"
  kuendigungsfristen:
    frage: "Wie sind ordentliche und außerordentliche Kündigung geregelt?"
    rechtsgrundlage: "§§ 314, 615 BGB; vertraglich oder gesetzlich"
    relevanz: "Risiko vorzeitiger Beendigung nach Vollzug"
  agb_kontrolle:
    frage: "Wurden die AGB einbezogen? Welcher Partei? Gültige Einbeziehung gem. §§ 305 ff. BGB?"
    rechtsgrundlage: "§§ 305, 307, 309 BGB"
    relevanz: "Unwirksame Klauseln trotz Vertragstext"
  compliance:
    frage: "Gibt es Compliance-Zusicherungen (Korruptionsverbote, Sanktionen, Exportkontrolle)?"
    rechtsgrundlage: "§ 130 OWiG; AWG/AWV; GwG"
    relevanz: "Compliance-Risiko des Zielunternehmens"
```

### Schritt 3: Tool-Übergabe-Paket erstellen

Das Übergabe-Paket enthält:

1. **Extraktionsprofil** (YAML oben, ggf. im Tool-nativen Format)
2. **Dokument-Inventar** (Liste aller Dokumente mit VDR-Pfad, Kategorie, Dateiname)
3. **Priorisierung** (Top-N nach Wert oder Relevanz zuerst)
4. **QA-Stichprobenplan** (welche %-QA für diesen Auftrag)

```markdown
## Übergabe-Paket – [Deal-Code] – [Datum]

**Tool:** [Luminance / Kira / anderes]
**Volumen:** [N] Dokumente
**Kategorien:** [Liste]
**Extraktionsprofil:** [Anlage-Link]
**Priorisierung:** [nach Wert >X EUR / Top-50 / vollständig]
**QA-Plan:** Stichprobe 10 % oder [N] Dokumente, gleichmäßig über Kategorien verteilt
**Erwartete Lieferzeit:** [N] Stunden/Tage
**Rückgabeformat:** [XLSX / CSV / Tool-API]
**Übergabe an:** [Tool-Administrator / externes Dienstleister]
```

### Schritt 4: QA-Schicht

Nach Erhalt der Tool-Ausgabe:

1. **Stichproben-QA**: [N] Dokumente manuell gegenlesen
   - Vollständigkeit: Alle extraktierten Klauseln vorhanden?
   - Richtigkeit: Klausel korrekt klassifiziert?
   - Falsch-Negative: Übersehene wesentliche Klauseln?
   - Falsch-Positive: Irrelevante Klauseln einbezogen?

2. **Fehler-Typen dokumentieren**:

```markdown
QA-Bericht – [Deal-Code]
- Geprüfte Dokumente: [N] von [M] ([%])
- Fehlerrate: [N] Fehler in [N] geprüften Dokumenten
- Häufige Fehler: [Beschreibung]
- Anpassung Extraktionsprofil: [ja / nein; wenn ja: was]
- Gesamtbewertung Vertrauensniveau: [hoch / mittel / niedrig]
```

3. **Vertrauensniveau aus Praxisprofil anwenden:**
   - `Ergebnis übernehmen`: Direkt in DD-Issues übernehmen, QA-Ergebnis vermerken
   - `Stichproben`: Mittleres Vertrauensniveau; alle 🔴-Issues manuell nachprüfen
   - `Vollständige Neuprüfung`: Nur Screening verwenden; alle Issues selbst extrahieren

### Schritt 5: Rückübergabe an DD-Issue-Extraktion

Tool-Ergebnisse im Standardformat für den `dd-findings-extraktion`-Skill übergeben:

```yaml
ki_tool_ergebnisse:
  tool: "Luminance"
  version: "2024.3"
  datum: "[DATUM]"
  vertrauensniveau: "mittel"
  qa_stichprobe_prozent: 10
  dokumente_gesamt: 312
  findings:
    - dokument: "VDR/02-Verträge/Acme-MSA-2021.pdf"
      kategorie: "Wesentliche Verträge"
      klausel: "change_of_control"
      extrakt: "§ 12 Abs. 3: Bei Kontrollwechsel hat [Vertragspartner] das Recht, fristlos zu kündigen."
      schweregrad_vorschlag: "🔴"
      ki_konfidenz: 0.92
      qa_geprueft: true
      qa_korrekt: true
```

## Quellen und Zitierweise

Normen-Basis für Extraktionsprofil: §§ 305 ff. BGB (AGB-Kontrolle), § 398 BGB (Abtretung), § 613a BGB (Betriebsübergang), §§ 69b, 43 UrhG, § 7 ArbNErfG, § 130 OWiG.

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

1. **Übergabe-Paket** (Markdown-Tabelle + YAML-Extraktionsprofil)
2. **QA-Bericht** (Markdown, nach Stichproben-QA)
3. **Rückgabe-Datensatz** (YAML/XLSX, für dd-findings-extraktion)

## Output-Template

**Adressat:** Tool-Administrator / DD-Team-intern — Tonfall: strukturiert, technisch-praezise

```
KI-TOOL-ÜBERGABE-PAKET
Mandat: [MANDATSCODE]
Deal-Code: [DEAL-CODE]
Datum: [TT.MM.JJJJ]
Tool: [LUMINANCE / KIRA / ANDERES]
Erstellt von: [NAME], [KANZLEI]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Weitergabe an Tool-Anbieter nur nach AVV gem. Art. 28 DSGVO und Mandantenzustimmung.

--- CHARGE-BESCHREIBUNG ---
Dokumente gesamt: [N]
Kategorien:
  - [KATEGORIE 1]: [N] Dokumente — Eignung: [HOCH / BEDINGT / NIEDRIG]
  - [KATEGORIE 2]: [N] Dokumente — Eignung: [HOCH / BEDINGT / NIEDRIG]
Ausgeschlossen (manuell zu prüfen): [N] Dokumente (Gesellschaftsvertraege, Side Letters)

--- EXTRAKTIONSPROFIL ---
Version: [v1.0]
Rechtsordnung: [Deutsches Recht / Englisches Recht / Gemischt]
Klauseln im Profil:
  1. change_of_control — [§ Vertrag; CoC-Recht]
  2. abtretungsverbot — [§ 399 BGB; § 354a HGB]
  3. haftungsbegrenzung — [§§ 305 ff. BGB]
  4. wettbewerbsverbot — [§ 138 BGB]
  5. kuendigungsfristen — [§§ 314, 615 BGB]
  [weitere nach Profil]

--- PRIORISIERUNG ---
Top-[N] nach [Vertragswert / Relevanz]: [LISTE]
Vollstaendige Prufung: [JA / NEIN]

--- QA-PLAN ---
Stichprobe: [N] % = [N] Dokumente
Vertrauensniveau Praxisprofil: [ERGEBNIS UEBERNEHMEN / 10-PROZENT-STICHPROBE / VOLLPRÜFUNG]
QA-Verantwortlich: [NAME]
QA-Frist: [TT.MM.JJJJ]

--- ERWARTETER ABLAUF ---
Uebergabe an Tool: [TT.MM.JJJJ]
Erwartete Lieferung: [TT.MM.JJJJ]
Rueckgabeformat: [XLSX / CSV / YAML]

--- QA-BERICHT (nach Lieferung auszufuellen) ---
Geprüfte Dokumente: [N] von [M] ([%])
Fehlerrate: [N] Fehler
Haeufige Fehlertypen: [BESCHREIBUNG]
Gesamtbewertung Vertrauensniveau: [HOCH / MITTEL / NIEDRIG]
Empfehlung: [ERGEBNIS DIREKT UEBERNEHMEN / NACHPRUEFUNG ERFORDERLICH FUER ROT-FINDINGS]
```

## Rote Schwellen

- **Kein AVV (Art. 28 DSGVO) vor Datenweitergabe** — Bussgeldhaftung; Weitergabe sofort stoppen bis AVV vorliegt.
- **KI-Vertrauensniveau "vollstaendige Neuprüfung" und kein QA-Budget** — KI-Tool liefert nur Screening; alle Findings sind manuell zu verifizieren bevor Garantien abgegeben werden.
- **Gesellschaftsvertraege / Side Letters in Batch** — ungeeignet fuer Bulk-Extraktion; sofort aus Charge herausnehmen und manuell prüfen.
- **Abtretungsverbote nicht klassifiziert** — Haftungsrisiko bei Garantien; § 354a HGB-Prüfung fuer Kaufleute-Vertraege immer separat durchfuehren.

## Beispiel

**Eingabe:** Datenraum enthält 280 Lieferantenverträge; Luminance konfiguriert.

**Ausgabe:** Übergabe-Paket mit Extraktionsprofil (8 Klauseln), Priorisierung Top-50 nach Vertragswert >100 TEUR, QA-Stichprobenplan 10 %. Nach QA: 15 🔴-Findings (davon 3 Change-of-Control mit Zustimmungserfordernis) → direkt an Vollzugscheckliste übergeben.

## Risiken / typische Fehler

- **Falsch-Negative bei AGB-Kontrolle:** KI-Tools übersehen oft die AGB-Einbeziehungs-Frage (§ 305 BGB). Immer manuell nachprüfen, ob AGB wirksam einbezogen wurden.
- **Change-of-Control ohne Zustimmungs-Prüfung:** Klausel extrahiert, aber nicht geprüft, ob bloßes Informationsrecht oder echtes Zustimmungserfordernis. Manuelle Klassifizierung erforderlich.
- **Jurisdiktion nicht erkannt:** Bei internationalen Verträgen (z. B. englisches Recht) falsche Klauselklassifizierung. Rechtsordnung im Profil explizit angeben.
- **Vertrauen ohne QA:** Kein Tool ist 100 % korrekt. QA-Stichproben sind nicht optional.
- **Mandantengeheimnis:** Dokumente an Drittanbieter weitergeben erfordert Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO und Zustimmung des Mandanten.
