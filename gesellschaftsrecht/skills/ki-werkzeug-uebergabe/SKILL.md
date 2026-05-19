---
name: ki-werkzeug-uebergabe
description: >
  KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn
  der Nutzer „Luminance", „Kira", „KI-Prüfung", „automatische Extraktion" oder
  „Massenprüfung" erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die
  ein einheitliches Klausel-Extraktionsprofil erfordern.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Luminance
  - Kira
  - KI-Prüfung
  - automatische Extraktion
  - Massenvertragsprüfung
  - Bulk-Review
---

# KI-Tool-Übergabe (Luminance / Kira)

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
    - dokument: "VDR/02-Vertraege/Acme-MSA-2021.pdf"
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

Kommentarliteratur:
- Altmeppen, in: Roth/Altmeppen, GmbHG, 11. Aufl. 2023, Einl. Rn. 1 (Doppelautoren-Kommentar).
- Wurmnest, in: MüKoBGB, 9. Aufl. 2022, § 307 Rn. 45 (AGB-Kontrolle).
- BGH, Urt. v. 25.03.2015 – VIII ZR 38/14, NJW 2015, 1871 Rn. 16 (zur AGB-Kontrolle von Change-of-Control-Klauseln im B2B-Bereich).

## Ausgabeformat

1. **Übergabe-Paket** (Markdown-Tabelle + YAML-Extraktionsprofil)
2. **QA-Bericht** (Markdown, nach Stichproben-QA)
3. **Rückgabe-Datensatz** (YAML/XLSX, für dd-findings-extraktion)

## Beispiel

**Eingabe:** Datenraum enthält 280 Lieferantenverträge; Luminance konfiguriert.

**Ausgabe:** Übergabe-Paket mit Extraktionsprofil (8 Klauseln), Priorisierung Top-50 nach Vertragswert >100 TEUR, QA-Stichprobenplan 10 %. Nach QA: 15 🔴-Findings (davon 3 Change-of-Control mit Zustimmungserfordernis) → direkt an Vollzugscheckliste übergeben.

## Risiken / typische Fehler

- **Falsch-Negative bei AGB-Kontrolle:** KI-Tools übersehen oft die AGB-Einbeziehungs-Frage (§ 305 BGB). Immer manuell nachprüfen, ob AGB wirksam einbezogen wurden.
- **Change-of-Control ohne Zustimmungs-Prüfung:** Klausel extrahiert, aber nicht geprüft, ob bloßes Informationsrecht oder echtes Zustimmungserfordernis. Manuelle Klassifizierung erforderlich.
- **Jurisdiktion nicht erkannt:** Bei internationalen Verträgen (z. B. englisches Recht) falsche Klauselklassifizierung. Rechtsordnung im Profil explizit angeben.
- **Vertrauen ohne QA:** Kein Tool ist 100 % korrekt. QA-Stichproben sind nicht optional.
- **Mandantengeheimnis:** Dokumente an Drittanbieter weitergeben erfordert Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO und Zustimmung des Mandanten.
