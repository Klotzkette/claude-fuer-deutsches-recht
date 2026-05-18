---
name: policy-redraft
description: Richtlinien-Neufassung – erstellt einen markierten Entwurf einer internen Richtlinie, der eine identifizierte Compliance-Lücke schließt. Laden, wenn eine Richtlinie nach einem Diff oder einer Gap-Analyse überarbeitet werden soll.
language: de
triggers:
  - "policy-redraft"
  - "Richtlinien-Neufassung"
  - "Richtlinie überarbeiten"
  - "Richtlinie anpassen"
  - "Neufassung"
  - "Redline"
  - "Gap schließen"
---

# Richtlinien-Neufassung

## Zweck

Dieser Skill erstellt einen Erst-Entwurf einer überarbeiteten internen Richtlinie auf Basis einer identifizierten Compliance-Lücke (aus `gap-surfacer` oder `policy-diff`). Er erzeugt keinen finalen Text – das Ergebnis ist ein Redline-Entwurf zur internen Prüfung und Freigabe, nicht die direkte Bearbeitung des Quelldokuments.

Typische Einsatzfelder:
- Anpassung von MaRisk-Richtlinien nach BaFin-Novelle
- Überarbeitung der IT-Sicherheitsrichtlinie nach neuem BAIT-Rundschreiben
- ESG-Risikorichtlinie neu erstellen nach aufsichtsrechtlicher Pflicht
- Compliance-Handbuch für Zahlungsinstitute nach ZAG-Änderung

## Eingaben

- **Gap oder Diff:** Ergebnis aus `gap-surfacer` oder `policy-diff` (oder manuelle Beschreibung der Lücke)
- **Bestandsrichtlinie:** Vollständiger Text (hochgeladen oder eingefügt)
- **Aufsichtsverlautbarung:** BaFin-Rundschreiben / Leitlinie (für Normzitate)
- Optional: Richtlinienformat-Vorlage des Unternehmens
- Optional: Übergangsfrist

## Ablauf

### 1. Ausgangslage erfassen

Aus dem Gap/Diff die zu schließende(n) Lücke(n) identifizieren:
- Welche Abschnitte der Bestandsrichtlinie müssen geändert werden?
- Welche Abschnitte sind neu hinzuzufügen?
- Gibt es Abschnitte, die gestrichen oder eingeschränkt werden müssen?

### 2. Normgrundlagen ermitteln

Für jede Änderung die maßgebliche Aufsichtsnorm zitieren:

```
Änderungsgrund: MaRisk AT 4.3.2 Novelle 2023 – Datenhaltungsfrist 10 Jahre
Maßgebliche Norm: BaFin-Rundschreiben 09/2017 (BA) i.d.F. 2023, AT 4.3.2
Verbindlichkeit: verbindliche Mindestanforderung [Modellwissen – prüfen]
Übergangsfrist: 31.12.2025
```

### 3. Redline-Entwurf erstellen

Format: Änderungen nach Redline-Konvention kennzeichnen:
- **~~Durchgestrichen~~** = zu streichender Text
- **`Fett/kursiv`** oder `[NEU:]` = neuer Text
- `[Normverweis]` = Quelle der Änderung

Beispiel:
```
§ 4 Aufbewahrungspflichten

(2) Daten des Risikomanagements sind für einen Zeitraum von 
~~mindestens sieben (7) Jahren~~ **[NEU: mindestens zehn (10) Jahren]** 
aufzubewahren. [MaRisk AT 4.3.2 Novelle 2023 – prüfen]

[NEU: (3) Für die Datenklassifizierung ist eine schriftliche 
Dokumentation zu erstellen und jährlich zu aktualisieren. 
[MaRisk AT 4.3.2 Novelle 2023 – prüfen]]
```

### 4. Neue Abschnitte vollständig entwerfen

Für neu hinzuzufügende Abschnitte vollständigen Text erstellen. Orientierung an:
- Wortlaut der Aufsichtsnorm (ggf. direktes Zitat mit Anpassung)
- Formulierungsstil der Bestandsrichtlinie
- Proportionalitätsgrundsatz (§ 25a Abs. 1 S. 3 KWG)

### 5. Metadaten der Richtlinie aktualisieren

```
Version: [alte Versionsnummer] → [neue Versionsnummer]
Stand: [TT.MM.JJJJ]
Änderungsgrund: Anpassung an [Verlautbarung]
Geprüft durch: [Freigabe durch Rechtsabteilung / Compliance / Vorstand erforderlich]
Nächste Überprüfung: [TT.MM.JJJJ – empfohlen: 12 Monate]
```

### 6. Freigabe-Checkliste

Am Ende des Entwurfs ausgeben:

```
Freigabe-Checkliste vor Inkraftsetzung:
☐ Rechtliche Prüfung abgeschlossen [prüfen]
☐ Compliance-Review durchgeführt
☐ Betroffene Fachabteilung informiert
☐ Vorstand / Geschäftsleitung hat zugestimmt (§ 25a Abs. 1 S. 2 KWG)
☐ Mitarbeiter geschult (falls neue Pflichten)
☐ Versionskontrolle aktualisiert
☐ Datum des Inkrafttretens festgelegt
```

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Jede Änderung im Redline wird mit der maßgeblichen Norm in Kurzform zitiert:
- `[MaRisk AT 4.3.2 Novelle 2023]` – mit Modellwissens-Hinweis, wenn nicht aus Primärquelle
- `[§ 25a Abs. 1 S. 3 KWG – Proportionalität]`
- `[EBA/GL/2021/04 Rz. 45]` – für EBA-Leitlinien

Kommentarliteratur für Entwurfsbegründung:
- Boos/Fischer/Schulte-Mattler, KWG, 5. Aufl. 2016, § 25a Rn. 44 ff.
- Lerch, ZAG, 2. Aufl. 2020, § 27 Rn. 20 ff.
- BaFin-Rundschreiben 09/2017 (BA) – MaRisk [Primärquelle; abrufbar: bafin.de]

## Ausgabeformat

- **Redline-Entwurf:** Vollständige Richtlinie mit markierten Änderungen
- **Änderungsübersicht:** Tabelle aller Änderungen mit Normverweis
- **Freigabe-Checkliste:** Am Ende des Entwurfs
- **Prüfernotiz:** Quellen, Vollständigkeit, offene Fragen
- Reviewer-Header wie in CLAUDE.md definiert

## Beispiel

**Eingabe:** „Bitte die IKS-Richtlinie für GAP-2025-001 (MaRisk AT 4.3.2 – Datenhaltung) neu fassen. Richtlinie hochgeladen."

**Ausgabe (Auszug):**

> **⚠️ Prüfernotiz**
> - **Quellen:** MaRisk RS 09/2017 Novelle 2023 [Modellwissen – prüfen gegen bafin.de], IKS-Richtlinie [Nutzer-Input]
> - **Gelesen:** § 4 IKS-Richtlinie, AT 4.3.2 MaRisk
> - **Zu Ihrer Einschätzung:** 1 Position `[prüfen]` – Aufbewahrungsfrist; Formulierung zur Datenklassifizierung ist Erstentwurf
> - **Vor Verwendung:** Rechts- und Compliance-Freigabe erforderlich; Inkrafttreten bis 31.12.2025

---

**VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS – ERSTENTWURF ZUR INTERNEN PRÜFUNG**

**IKS-Richtlinie – Redline-Entwurf**
*Version 2.0 (Entwurf) | Stand: 01.06.2025 | Änderungsgrund: MaRisk-Novelle 2023*

---

**§ 4 Aufbewahrungspflichten**

(2) Daten des Risikomanagements sowie sämtliche für die Beurteilung der wirtschaftlichen Verhältnisse des Instituts erforderliche Unterlagen sind für einen Zeitraum von ~~mindestens sieben (7) Jahren~~ **[NEU: mindestens zehn (10) Jahren]** aufzubewahren und jederzeit innerhalb angemessener Frist abrufbar zu halten. [MaRisk AT 4.3.2 Novelle 2023 – Modellwissen, prüfen]

**[NEU: (3) Eine schriftliche Dokumentation der Datenklassifizierung ist zu erstellen. Diese ist mindestens jährlich auf Aktualität zu prüfen und bei wesentlichen Änderungen unverzüglich zu aktualisieren. [MaRisk AT 4.3.2 Novelle 2023 – Modellwissen, prüfen]]**

---

**Änderungsübersicht:**
| § | Änderungstyp | Normgrundlage | Status |
|---|---|---|---|
| § 4 Abs. 2 | Friständerung 7 → 10 Jahre | MaRisk AT 4.3.2 | `[prüfen]` |
| § 4 Abs. 3 (neu) | Neuer Absatz Datenklassifizierung | MaRisk AT 4.3.2 | `[prüfen]` |

## Risiken / typische Fehler

- **Direktes Inkraftsetzen ohne Freigabe:** Der Redline-Entwurf ist ein Arbeitsdokument. Niemals ohne rechts- und compliance-seitige Freigabe sowie (bei KWG-Instituten) Geschäftsleiterzustimmung inkraftsetzen.
- **Wörtliche Übernahme von Normtext:** Aufsichtstext ist oft Mindeststandard, nicht optimaler Richtlinientext. Formulierungen ggf. konkretisieren.
- **Fehlende Schulungsmaßnahmen:** Neue Pflichten in internen Richtlinien wirken nicht ohne Mitarbeiterschulungen. Hinweis in Checkliste.
- **Versionskontrolle:** Jede Richtlinienänderung erfordert eine neue Versionsnummer und ein Änderungsprotokoll. Ohne Versionskontrolle ist die Richtlinie in BaFin-Prüfungen nur schwer nachzuweisen.
- **Proportionalitätsgrundsatz vergessen:** Für kleine und mittelgroße Institute gelten teils erleichterte Anforderungen (§ 25a Abs. 1 S. 3 KWG); Redline ggf. anpassen.
