---
name: mandat-arbeitsbereich
description: Mandat-Workspaces verwalten (nur Kanzleibetrieb mit mehreren Mandanten). Laden, um ein neues Mandat anzulegen, zwischen Mandaten zu wechseln, ein Mandat zu schließen oder Workspaces zu deaktivieren.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - mandat-arbeitsbereich
  - neues Mandat
  - Mandat wechseln
  - Mandat schließen
  - Mandats-Workspace
  - matter workspace
---

# Mandat-Workspace-Verwaltung

## Zweck

Dieser Skill verwaltet Mandat-Workspaces für Kanzleien mit mehreren Mandanten. Im regulatorischen Recht ist ein „Mandat" typischerweise:
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
2. Mandat-Bezeichnung / Slug (z. B. bafin-pruefung-2025-mandantA)
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
├── mandat.md          # Mandat-Fakten und Übersteuerungen
├── gap-tracker.yaml   # Mandat-spezifische Gaps
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
| bafin-pruefung-2025-A | Mandant A | Gap-Analyse | BaFin | 31.12.2025 | aktiv |
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
- Nächster empfohlener Schritt (z. B. „Mandat aktiv – starten Sie mit `/regulatorisches-recht:luecken-aufzeiger`")

## Beispiel

**Eingabe:** `/regulatorisches-recht:mandat-arbeitsbereich neu`

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

Nächster Schritt: /regulatorisches-recht:luecken-aufzeiger
```

## Risiken / typische Fehler

- **Cross-Mandat-Kontext versehentlich aktiviert:** Skills dürfen mandantsübergreifend niemals Informationen verbinden, wenn Cross-Mandat-Kontext deaktiviert ist (Standard). Explizite Anfrage erforderlich.
- **Klarnamen in Pfaden:** Mandanten-Klarnamen nicht in Dateinamen oder Logs verwenden. Nur Kürzel.
- **Nicht geschlossene Mandate:** Alte aktive Mandate ohne Leitfrist überprüfen und bei Abschluss schließen; beugt Versehen mit veralteten Kontextinformationen vor.
- **Mandantengeheimnis:** Inhalte aus `mandat.md` und den mandat-spezifischen Trackern sind vertraulich nach § 43a Abs. 2 BRAO. Nie in gemeinsame Kontexte oder Protokolle exportieren.
