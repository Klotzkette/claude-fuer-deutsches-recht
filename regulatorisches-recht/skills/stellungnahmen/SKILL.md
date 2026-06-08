---
name: stellungnahmen
description: "Stellungnahme zu Regulierungsvorhaben oder Konsultationsverfahren verfassen. GG Art. 12 Art. 80 AEUV DSGVO KWG WpHG. Prüfraster: Konsultationsumfang regulatorische Ziele Kritikpunkte Alternativvorschlaege Verhältnismäßigkeit. Output: strukturierte Stellungnahme mit Einzelanmerkungen Aenderungsvorschlaegen. Abgrenzung: nicht für interne Compliance-Analysen im Regulatorisches Recht."
---

# Konsultationsbeiträge

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
 behoerde: "[BaFin / EBA / ESMA / BNetzA / EU-Kommission]"
 titel: "[Vollständiger Titel des Konsultationsdokuments]"
 referenz: "[z. B. BaFin-RS 2024/xx | EBA/CP/2024/xx]"
 kommentierungsfrist: "[TT.MM.JJJJ]"
 einreichungsform: "[E-Mail / Online-Portal / Postalisch]"
 einreichungsadresse: "[URL oder E-Mail]"
 status: "offen"
 entscheidung: "[teilnehmen / nicht teilnehmen / offen]"
 eigentuemer: "[Name / Team]"
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
einreichungsbestaetigung: "[Aktenzeichen / Eingangsbestätigung]"
```

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 47-51 GGO (Verbands-Anhörung, Stellungnahme-Verfahren) — Art. 41 GRCh (Recht auf gute Verwaltung, Anhörungsrecht) — §§ 28, 29 VwVfG (Anhörungsrecht im Verwaltungsverfahren) — §§ 2, 3 UmwRG (Verbandsklage, Stellungnahme)

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Einschlägige Normen und Verlautbarungen:
- BaFin-Konsultationsverfahren: Bekanntmachung auf BaFin-Newsroom, bafin.de
- § 4 Abs. 2 FinDAG (Aufgaben der BaFin)
- Art. 16 EBA-Verordnung (EU) Nr. 1093/2010 (Leitlinien-Verfahren der EBA)
- Art. 10 ESMA-Verordnung (EU) Nr. 1095/2010 (Technische Standards)
- § 68 EnWG (BNetzA-Konsultationsverfahren)
- BaFin-Rundschreiben: z. B. RS 10/2012 (BA) – MaRisk [Modellwissen – prüfen auf aktuelle Fassung]

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Lerch, ZAG, 2. Aufl. 2020 (Zahlungsdiensteaufsicht).

## Beispiel

**Eingabe:** "BaFin hat einen Konsultationsentwurf zur MaRisk-Novelle veröffentlicht. Frist: 30.06.2025. Bitte analysieren und Stellungnahme vorbereiten."

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

---

<!-- AUDIT 27.05.2026
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

