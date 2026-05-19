---
name: stellungnahmen
description: Konsultationsbeiträge für BaFin-, BNetzA-, EBA-, ESMA- und EU-Konsultationen verwalten und verfassen. Laden bei Konsultationszeiträumen, Stellungnahmen und Kommentierungsfristen.
language: de
triggers:
  - "Konsultation"
  - "Stellungnahme"
  - "Kommentierungsfrist"
  - "BaFin-Konsultation"
  - "EBA-Konsultation"
  - "ESMA-Konsultation"
  - "comment period"
  - "Konsultationsbeitrag"
---

# Konsultationsbeiträge

## Zweck

Dieser Skill unterstützt bei der Bearbeitung offener Konsultationszeiträume von Aufsichtsbehörden. Er hilft, Konsultationsentwürfe zu analysieren, die eigene Betroffenheit zu beurteilen, eine Entscheidung zur Teilnahme zu treffen und einen begründeten Stellungnahmebeitrag zu verfassen. Einsatzfelder: BaFin-Konsultationen (Rundschreiben, Merkblätter), BNetzA-Konsultationen (EnWG, TKG), EBA- und ESMA-Konsultationen (CRR, MiFID II, DORA), EU-Kommissions-Konsultationen.

## Eingaben

- Konsultationsdokument (hochgeladen oder per Link)
- Aktives Praxisprofil (Behörden, Segment, Materialitätsschwelle)
- Optional: Eigene interne Richtlinien, die vom Entwurf berührt werden
- Optional: Vorherige Stellungnahmen derselben Behörde zur Konsistenzprüfung

## Ablauf

### 1. Konsultation erfassen

Falls noch nicht im Kommentar-Tracker eingetragen:

```yaml
konsultation:
  behörde: "[BaFin / EBA / ESMA / BNetzA / EU-Kommission]"
  titel: "[Vollständiger Titel des Konsultationsdokuments]"
  referenz: "[z. B. BaFin-RS 2024/xx | EBA/CP/2024/xx]"
  kommentierungsfrist: "[TT.MM.JJJJ]"
  einreichungsform: "[E-Mail / Online-Portal / Postalisch]"
  einreichungsadresse: "[URL oder E-Mail]"
  status: "offen"
  entscheidung: "[teilnehmen / nicht teilnehmen / offen]"
  eigentümer: "[Name / Team]"
```

Datei schreiben: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/comment-tracker.yaml`

### 2. Relevanzprüfung

Fragen:
1. Berührt der Entwurf das eigene Aufsichtssegment (z. B. KWG-Institut, ZAG-Institut, Wertpapierfirma WpIG)?
2. Enthält er neue Pflichten mit Übergangsfrist?
3. Weicht er von der bisherigen Praxis ab (MaRisk-Novelle, neue EBA-Leitlinie)?
4. Besteht Anlass zur inhaltlichen Einwirkung (z. B. unverhältnismäßige Anforderungen, Auslegungsunklarheiten)?

Ergebnis: **Teilnahmeempfehlung** (begründet) oder **Verzicht** (mit Begründung vermerkt).

### 3. Inhaltsanalyse des Entwurfs

Strukturierte Analyse:

| Nr. | Entwurfsabschnitt | Regelungsinhalt | Eigene Betroffenheit | Handlungsbedarf |
|---|---|---|---|---|
| 1 | [Abschnitt] | [Inhalt] | [hoch / mittel / gering] | [Kommentar / Umsetzung / keiner] |

Für jeden Abschnitt mit hoher Betroffenheit:
- Aktuelle Anforderung (aus Bestandsrichtlinien)
- Neue Anforderung laut Entwurf
- Delta / Lücke
- Formulierungsvorschlag für die Stellungnahme

### 4. Stellungnahmenentwurf

Format gemäß Behördenstandard:

**BaFin-Konsultationen:**
```
An: [E-Mail der BaFin-Fachabteilung]
Betreff: Stellungnahme zum Konsultationsentwurf [Titel], Ref. [RS-Nr.]

[Institution / Kanzlei]
[Datum]

Sehr geehrte Damen und Herren,

wir bedanken uns für die Möglichkeit zur Stellungnahme zum Konsultationsentwurf
[Titel] vom [Datum].

Allgemeine Anmerkungen:
[...]

Zu den einzelnen Abschnitten:

Zu Abschnitt [X]:
[Konkrete Anmerkung mit Normverweis]

Wir bitten um Berücksichtigung unserer Anmerkungen.

Mit freundlichen Grüßen
[Unterzeichner]
```

**EBA/ESMA-Konsultationen:**
Format nach dem offiziellen Antwortbogen der Behörde (Excel/Word-Template); Fragen der Behörde einzeln beantworten. Die Antworten sollen prägnant, normbezogen und mit Quellen belegt sein.

### 5. Fristenüberwachung

Alle offenen Konsultationen im Tracker prüfen:
- Frist < 14 Tage: 🔴 sofortiger Handlungsbedarf
- Frist 14–30 Tage: 🟠 Entwurf erstellen
- Frist > 30 Tage: 🟡 Beobachten

Tracker aktualisieren nach Einreichung:
```yaml
status: "eingereicht"
einreichungsdatum: "[TT.MM.JJJJ]"
einreichungsbestätigung: "[Aktenzeichen / Eingangsbestätigung]"
```

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen und Verlautbarungen:
- BaFin-Konsultationsverfahren: Bekanntmachung auf BaFin-Newsroom, bafin.de
- § 4 Abs. 2 FinDAG (Aufgaben der BaFin)
- Art. 16 EBA-Verordnung (EU) Nr. 1093/2010 (Leitlinien-Verfahren der EBA)
- Art. 10 ESMA-Verordnung (EU) Nr. 1095/2010 (Technische Standards)
- § 68 EnWG (BNetzA-Konsultationsverfahren)
- BaFin-Rundschreiben: z. B. RS 10/2012 (BA) – MaRisk [Modellwissen – prüfen auf aktuelle Fassung]

Kommentarliteratur:
- Boos/Fischer/Schulte-Mattler, KWG, 5. Aufl. 2016 (Kommentar zur BaFin-Zuständigkeit).
- Lerch, ZAG, 2. Aufl. 2020 (Zahlungsdiensteaufsicht).

## Ausgabeformat

- **Tracking-Tabelle:** Offene Konsultationen mit Frist, Status, Eigentümer
- **Relevanzmatrix:** Tabelle der betroffenen Abschnitte
- **Stellungnahmenentwurf:** Behördenkonformes Format (Brief oder Antwortbogen)
- Reviewer-Header und Prüfernotiz wie in CLAUDE.md definiert

## Beispiel

**Eingabe:** „BaFin hat einen Konsultationsentwurf zur MaRisk-Novelle veröffentlicht. Frist: 30.06.2025. Bitte analysieren und Stellungnahme vorbereiten."

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** BaFin-Newsroom [Websuche – prüfen], Konsultationsentwurf [Nutzer-Input]
> - **Gelesen:** Vollständiger Entwurf (40 Seiten)
> - **Zu Ihrer Einschätzung:** 3 Abschnitte mit hoher Betroffenheit markiert `[prüfen]`
> - **Vor Verwendung:** Fristen und Einreichungsmodalitäten gegen bafin.de verifizieren

---

**Konsultation erfasst:** BaFin-RS 2025/xx – MaRisk-Novelle, Frist: 30.06.2025

**Relevanzmatrix:**

| Nr. | Abschnitt | Regelungsinhalt | Betroffenheit |
|---|---|---|---|
| 1 | AT 4.3.2 | Neue Anforderungen an Datenhaltung | hoch `[prüfen]` |
| 2 | BT 3.1 | Erweiterung Stresstesting | mittel |
| 3 | BTR 2.3 | Liquiditätsrisikomanagement | gering |

**Stellungnahmenentwurf (Auszug):**

> Zu AT 4.3.2 (Datenhaltung):
> Wir regen an, die vorgeschlagene Aufbewahrungsfrist von 10 Jahren auf 7 Jahre zu begrenzen, da § 257 HGB und § 147 AO für Handelsbücher eine Frist von 10 Jahren vorsehen, für die hier relevanten operativen Daten jedoch keine vergleichbare Pflichtgrundlage besteht. [Modellwissen – prüfen]

## Risiken / typische Fehler

- **Fristversäumnis:** BaFin- und EBA-Fristen sind nicht verlängerbar; nach Fristablauf keine Einreichung mehr möglich. Frist im Kalender setzen und 14 Tage vorab mit 🔴 markieren.
- **Falsches Einreichungsformat:** BaFin: E-Mail an die zuständige Fachabteilung; EBA/ESMA: Offizielles Antwortformular zwingend. Formfehler führen zur Nichtberücksichtigung.
- **Übermäßige Länge:** Aufsichtsbehörden lesen kurze, präzise Stellungnahmen mit klaren Normverweisen bevorzugt. Maximallänge je nach Behörde beachten.
- **Mandantengeheimnis:** Stellungnahmen für externe Kunden müssen gemäß § 43a Abs. 2 BRAO als vertraulich behandelt werden; öffentliche Stellungnahmen bedürfen der Freigabe.
- **Verfasser-Angabe:** Viele Behörden veröffentlichen Stellungnahmen. Klären, ob anonym oder im Namen des Mandanten eingereicht werden soll.
