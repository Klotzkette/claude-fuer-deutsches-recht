---
name: integrations-management
description: >
  Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung,
  Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung
  oder Abschluss-Checkliste. Berücksichtigt § 613a BGB (Betriebsübergang), BetrVG-Mitbestimmung
  und gesellschaftsrechtliche Post-Closing-Pflichten nach UmwG/GmbHG/AktG. Lädt bei
  „Post-Merger-Integration", „Post-Closing", „Betriebsübergang", „Vertragsübertragung"
  oder „was ist noch offen".
language: de
triggers:
  - "Post-Merger-Integration"
  - "Post-Closing"
  - "Betriebsübergang"
  - "Vertragsübertragung"
  - "Integrationsstatus"
  - "was ist noch offen"
  - "Zustimmungen ausstehend"
  - "Integrationsplan"
  - "PMI"
argument-hint: "[--init | --vertraege | --bericht | --update | --export] [--mandat [code]]"
---

# Post-Merger-Integrations-Management

## Zweck

Dieser Skill ist die Programmmanagement-Ebene für die rechtliche Post-Closing-Integration — nicht operative Geschäftsintegration oder IT-Systeme. Der rechtliche Workstream: Drittpartei-Zustimmungen, Vertragsübertragungen, Gesellschaftsbereinigung, IP-Umschreibungen, SPA-Pflichten, Betriebsübergang nach § 613a BGB, betriebliche Mitbestimmung nach BetrVG.

## Eingaben

- Unternehmenskaufvertrag (SPA/Anteilskaufvertrag) oder Auszüge
- deal-context.md (Mandatscode, Zielgesellschaft, Closing-Datum, Transaktionsleiter)
- Bestehende Abschluss-Checkliste, Vertragsbestand der Zielgesellschaft
- Statusmitteilungen von externem Berater, HR, Corporate Development

## Rechtlicher Rahmen

**Betriebsübergang:** § 613a BGB (Übergang kraft Gesetzes; Widerspruchsrecht Abs. 6; Informationspflicht Abs. 5 — Frist: rechtzeitig vor Übergang). BAG, Urt. v. 27.11.2008 – 2 AZR 675/07, NZA 2009, 842 Rn. 20 (Widerspruchsfrist § 613a Abs. 6 BGB); BGH, Urt. v. 21.01.2010 – I ZR 172/08, NJW 2010, 2506 Rn. 20 (Vertragsübernahme im Betriebsübergang).

**Betriebliche Mitbestimmung:** §§ 111 ff. BetrVG (Interessenausgleich und Sozialplan bei Betriebsänderung); § 17 KSchG (Massenentlassung, Anzeigepflicht). BAG, Urt. v. 22.01.2004 – 2 AZR 111/02, NZA 2004, 593 Rn. 30 (Betriebsrat-Anhörung § 102 BetrVG im Integrationskontext).

**Change of Control / Vertragskontinuität:** BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18 (CoC-Klausel, Auslegung; mittelbarer Kontrollwechsel); §§ 414 f. BGB (Schuldübernahme); § 25 HGB (Haftung bei Firmenfortführung).

**Gesellschaftsrechtliche Post-Closing-Pflichten:** § 40 GmbHG (Gesellschafterliste aktualisieren); §§ 17 ff. UmwG (Verschmelzung); §§ 65 ff. GmbHG (Liquidation). Roth, in: MüKoBGB, 9. Aufl. 2022, § 414 Rn. 5; Hopt, in: Baumbach/Hopt, HGB, 41. Aufl. 2024, § 25 Rn. 1.

## Ablauf

Aufruf über Flag: `--init` (Modus 1) | `--vertraege` (Modus 2) | `--bericht` (Modus 3) | `--update` (Modus 4) | `--export` (Modus 5).

### Modus 1: Initialisierung (`--init`)

deal-context.md lesen; ggf. anlegen. Abschluss-Checkliste importieren (Post-Closing-Punkte → Tag-1/30-Arbeitsplan).

Transaktionsunterlagen anfordern (Vollständiger SPA > Deal-Zusammenfassung > nichts). Phasenbasierten Arbeitsplan generieren:

**Tag 1 — rechtlich federführend:** Firmenname Handelsregister; Bankkonten-Bevollmächtigte; Gesellschafterliste § 40 GmbHG; D&O-Nachhaftungsdeckung; IP-Abtretungen.

**Tag 1 — rechtlich begleitend:** Mitarbeiterinformation § 613a Abs. 5 BGB (Frist beachten); Betriebsrat informieren; Kundenanschreiben prüfen.

**Tag 30:** Erster Zustimmungsanlauf (alle Gegenparteien); IP-Umschreibung DPMA; CoC-Vertragsanalyse (Tier 3).

**Tag 90:** Pflicht-Zustimmungen-Frist (SPA); Gesellschaftsbereinigungsentscheidung; HR-Harmonisierung (BetrVG).

**Tag 180:** Verschmelzungsanmeldung §§ 17 ff. UmwG oder Liquidationsanmeldung §§ 65 ff. GmbHG; Garantiefrist-Tracking.

### Modus 2: Vertragsübertragung (`--vertraege`)

Vertragsbestand aus Datenraum, hochgeladener Liste oder SPA-Disclosure-Schedule importieren. Übertragungsmechanismus für jeden Vertrag klassifizieren:

| Mechanismus | Tier |
|---|---|
| Zustimmungserforderlich (ausdrückliche Klausel) | 1 (SPA-Pflicht) oder 2 |
| Change-of-Control-Klausel (ausgelöst durch Closing) | 3 — sofort handeln ⚠️ |
| Automatisch übertragbar (keine Beschränkung) | 4 |
| Keine Regelung (§§ 398 ff. BGB prüfen; § 354a HGB bei Kaufleuten) | 2 |

Tier-3-Verträge prominent ausweisen: CoC-Recht kann bereits mit Closing-Datum ausgelöst sein.

### Modus 3: Statusbericht (`--bericht`)

```
INTEGRATIONSSTATUS — [Mandatscode] / [Zielgesellschaft]
[Datum] — Tag [N] nach Closing

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO. Weitergabe nur nach Freigabe.

PFLICHT-ZUSTIMMUNGEN  [Frist: DATUM — N Tage]
  Erhalten: [N] von [gesamt]  ████░░  [%]
  Verweigert: [N] ⚠️

VERTRAGSÜBERTRAGUNG
  Tier 1–3: Status je Kategorie
  CoC offen: [N] ⚠️

ARBEITSPLAN — ÜBERFÄLLIG / DIESE WOCHE / ABGESCHLOSSEN

BLOCKIERER & ENTSCHEIDUNGSBEDARF
```

### Modus 4: Aktualisierung (`--update`)

Freitext oder hochgeladenes Statusdokument einlesen. Tracker-Einträge aktualisieren und Zusammenfassung der Änderungen zeigen.

### Modus 5: Export (`--export`)

Flaches CSV (Spalten: id, phase, beschreibung, prioritaet, frist, status, blockierer) oder Markdown-Tabelle. Formel-Injektionsschutz: Zellen aus Fremdquellen mit vorangestelltem Apostroph.

## Ausgabeformat

YAML-Tracker-Datei + strukturierter Statusbericht mit Arbeitsergebnis-Kopfzeile. Export als CSV.

## Beispiel

GmbH-Anteilskauf, Closing 01.03.2025, 15 Pflicht-Zustimmungen aus SPA-Anhang, 3 CoC-Verträge. Tag-30-Bericht: 8 von 15 Zustimmungen erhalten, 2 verweigert (SPA-Pflicht gefährdet), 3 CoC-Verträge zur sofortigen Kontaktaufnahme.

## Risiken und typische Fehler

- **§ 613a Abs. 5 BGB-Informationspflicht vergessen.** Widerspruchsfrist 1 Monat läuft ab ordnungsgemäßer Information.
- **CoC-Klauseln zu spät identifizieren.** Tier-3-Verträge prominent anzeigen — Recht kann ab Closing laufen.
- **Garantiefristen nicht differenzieren.** Allgemeine, fundamentale und Steuergarantien haben unterschiedliche Überlebensfristen — aus SPA einzeln extrahieren.
- **Earn-out nicht abgrenzen.** Nur Referenzdaten führen, Eigentümer = Finance.

## Quellenpflicht

- `§ 613a Abs. 5 BGB` (Information), `§ 613a Abs. 6 BGB` (Widerspruchsfrist)
- `§§ 17 ff. UmwG` (Verschmelzung), `§§ 65 ff. GmbHG` (Liquidation), `§ 40 GmbHG` (Gesellschafterliste)
- BGH: `BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18`
- BAG: `BAG, Urt. v. 27.11.2008 – 2 AZR 675/07, NZA 2009, 842 Rn. 20`
- Kommentare: `Roth, in: MüKoBGB, 9. Aufl. 2022, § 414 Rn. 5`

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
