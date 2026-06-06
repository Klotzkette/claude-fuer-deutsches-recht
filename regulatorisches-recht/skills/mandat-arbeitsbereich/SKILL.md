---
name: mandat-arbeitsbereich
description: "Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Abgrenzung: nicht für inhaltliche Regulierungsprüfung im Regulatorisches Recht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Mandat-Workspace-Verwaltung

## Arbeitsbereich

Regulatorisches Mandat strukturieren und Arbeitsbereich abgrenzen. KWG WpHG DORA VAG GwG BaFin. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe beteiligte Behoerden. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Abgrenzung: nicht für inhaltliche Regulierungsprüfung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieser Skill verwaltet Mandat-Workspaces für Kanzleien mit mehreren Mandanten. Im regulatorischen Recht ist ein "Mandat" typischerweise:
- Ein bestimmter Regulierungsakt, zu dem ein Mandant beraten wird (z. B. MaRisk-Novelle-Implementierung)
- Ein offenes Konsultationsverfahren, für das eine Stellungnahme erstellt wird
- Eine BaFin-Prüfung oder eine DORA-GAP-Analyse für einen bestimmten Mandanten
- Ein Anfrageverfahren oder eine Abgrenzungsanfrage an eine Behörde

**Inhouse-Nutzer:** Dieser Skill ist nicht relevant. Das Praxisprofil gilt für das gesamte Unternehmen.

## Eingaben

- Aktives Praxisprofil mit aktivierten Mandat-Workspaces
- Mandat-Subkommando: `neu | auflisten | wechseln | schließen | keiner`
- Optional: Mandat-Name, Mandant, Rechtsgebiet, Frist

## Ablauf

### Subkommando: `neu`

Abfragen:
```
1. Mandant (intern: nur Kürzel, kein vollständiger Name in Logs)
2. Mandat-Bezeichnung / Slug (z. B. bafin-prüfung-2025-mandantA)
3. Art des Mandats:
 a) Gap-Analyse gegen Regulierungsakt
 b) Konsultationsbeitrag
 c) Richtlinienneufassung
 d) Behördenanfrage
 e) Sonstiges
4. Zuständige Behörde(n)
5. Leitfrist (falls bekannt)
```

Mandatsordner anlegen:
```
~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/mandate/<mandat-slug>/
├── mandat.md # Mandat-Fakten und Übersteuerungen
├── gap-tracker.yaml # Mandat-spezifische Gaps
├── comment-tracker.yaml
└── verification-log.md
```

`mandat.md` Vorlage:
```markdown
# Mandat: [Bezeichnung]
Erstellt: [TT.MM.JJJJ]
Mandant: [Kürzel]
Art: [Typ]
Behörde(n): [Liste]
Leitfrist: [TT.MM.JJJJ]
Status: aktiv

## Mandat-spezifische Fakten
[Abweichungen vom Praxisprofil; Mandant-spezifische Materialitätsschwelle usw.]

## Datenschutz-Hinweis
§ 43a Abs. 2 BRAO, § 203 StGB. Dieser Ordner enthält mandantenbezogene Daten.
Cross-Mandat-Kontext: deaktiviert (Standard).
```

### Subkommando: `auflisten`

Alle Mandate auflisten:
```
Aktive Mandate:
| Slug | Mandant | Art | Behörde | Leitfrist | Status |
|---|---|---|---|---|---|
| bafin-prüfung-2025-A | Mandant A | Gap-Analyse | BaFin | 31.12.2025 | aktiv |
```

### Subkommando: `wechseln`

```
Zu welchem Mandat wechseln?
[Liste der aktiven Mandate anzeigen]
```
Nach Auswahl: Aktives Mandat im Profil setzen. Skills lesen jetzt `mandat.md` dieses Mandats.

### Subkommando: `schließen`

```
Mandat [Slug] schließen?
Hinweis: Dateien bleiben erhalten. Status wird auf 'geschlossen' gesetzt.
Lernerkenntnisse ins Praxisprofil übertragen? (ja/nein)
```

### Subkommando: `keiner`

Aktives Mandat deaktivieren → Skills laufen wieder auf Praxisebene.

## Quellen und Zitierweise

Zitierweise: `../../../references/zitierweise.md`

Relevante Berufsrechtsnormen:
- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht)
- § 203 StGB (Verletzung von Privatgeheimnissen)
- § 50 BRAO (Aktenführung)
- BORA § 2 (Unabhängigkeit), § 6 (Handakten)

## Ausgabeformat

- Bestätigung der Aktion (angelegt / gewechselt / geschlossen)
- Aktueller Workspace-Status
- Nächster empfohlener Schritt (z. B. "Mandat aktiv – starten Sie mit `/regulatorisches-recht:lücken-aufzeiger`")

## Beispiel

**Eingabe:** `/regulatorisches-recht:regulatorisches-recht-mandat-arbeitsbereich neu`

**Ausgabe:**
```
Neues Mandat anlegen.

Mandant-Kürzel (nur intern sichtbar): MandantA
Mandat-Bezeichnung: MaRisk-GAP-2025-MandantA
Art: Gap-Analyse
Zuständige Behörde: BaFin
Leitfrist: 31.12.2025

Mandat angelegt unter:
~/.../mandate/mairisk-gap-2025-mandanta/

Aktives Mandat: MaRisk-GAP-2025-MandantA

Nächster Schritt: /regulatorisches-recht:lücken-aufzeiger
```

## Risiken / typische Fehler

- **Cross-Mandat-Kontext versehentlich aktiviert:** Skills dürfen mandantsübergreifend niemals Informationen verbinden, wenn Cross-Mandat-Kontext deaktiviert ist (Standard). Explizite Anfrage erforderlich.
- **Klarnamen in Pfaden:** Mandanten-Klarnamen nicht in Dateinamen oder Logs verwenden. Nur Kürzel.
- **Nicht geschlossene Mandate:** Alte aktive Mandate ohne Leitfrist überprüfen und bei Abschluss schließen; beugt Versehen mit veralteten Kontextinformationen vor.
- **Mandantengeheimnis:** Inhalte aus `mandat.md` und den mandat-spezifischen Trackern sind vertraulich nach § 43a Abs. 2 BRAO. Nie in gemeinsame Kontexte oder Protokolle exportieren.
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kernnormen:** §§ 611-630 BGB (Dienstvertrag, Mandatsrecht) — §§ 48-49 VwVfG — §§ 3-7 BORA (Berufsrecht Rechtsanwaelte)

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
