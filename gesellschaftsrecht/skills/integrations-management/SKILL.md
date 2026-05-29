---
name: integrations-management
description: 'Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste. Berücksichtigt § 613a BGB (Betriebsübergang), BetrVG-Mitbestimmung und gesellschaftsrechtliche Post-Closing-Pflichten nach UmwG/GmbHG/AktG. Lädt bei "Post-Merger-Integration", "Post-Closing", "Betriebsübergang", "Vertragsübertragung" oder "was ist noch offen".'

---

# Post-Merger-Integrations-Management

## Triage zu Beginn

Vor dem Start des Integrations-Trackings klären:

1. **Closing-Datum:** Wann war das Closing? (Tag-1/Tag-30/Tag-90-Workstreams hängen davon ab)
2. **SPA-Dokument verfügbar?** Vollständiges SPA oder nur Deal-Zusammenfassung?
3. **Schwerpunkt Rechtliches vs. Operatives:** Ist der Skill für rechtlichen Workstream oder operative Integration?
4. **Betriebsübergang?** Ist § 613a BGB ausgelöst? Wurden Arbeitnehmer bereits informiert?
5. **CoC-Klauseln:** Sind Tier-3-Verträge mit CoC-Klauseln identifiziert?
6. **Gesellschaftsbereinigung:** Soll eine Zielgesellschaft aufgelöst, verschmolzen oder fortgeführt werden?

## Zentrale Normen

§ 613a BGB (Betriebsübergang; Informationspflicht Abs. 5; Widerspruchsrecht Abs. 6 — 1 Monat) — §§ 111 ff. BetrVG (Interessenausgleich und Sozialplan) — § 17 KSchG (Massenentlassung) — § 40 GmbHG (Gesellschafterliste aktualisieren) — §§ 17 ff. UmwG (Verschmelzung) — §§ 65 ff. GmbHG (Liquidation) — §§ 414 f. BGB (Schuldübernahme; Vertragsübernahme) — § 25 HGB (Firmenhaftung bei Betriebsübernahme) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Tool-Übergabe)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ist die Programmmanagement-Ebene für die rechtliche Post-Closing-Integration — nicht operative Geschäftsintegration oder IT-Systeme. Der rechtliche Workstream: Drittpartei-Zustimmungen, Vertragsübertragungen, Gesellschaftsbereinigung, IP-Umschreibungen, SPA-Pflichten, Betriebsübergang nach § 613a BGB, betriebliche Mitbestimmung nach BetrVG.

## Eingaben

- Unternehmenskaufvertrag (SPA/Anteilskaufvertrag) oder Auszüge
- deal-context.md (Mandatscode, Zielgesellschaft, Closing-Datum, Transaktionsleiter)
- Bestehende Abschluss-Checkliste, Vertragsbestand der Zielgesellschaft
- Statusmitteilungen von externem Berater, HR, Corporate Development

## Rechtlicher Rahmen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

Aufruf über Flag: `--init` (Modus 1) | `--verträge` (Modus 2) | `--bericht` (Modus 3) | `--update` (Modus 4) | `--export` (Modus 5).

### Modus 1: Initialisierung (`--init`)

deal-context.md lesen; ggf. anlegen. Abschluss-Checkliste importieren (Post-Closing-Punkte → Tag-1/30-Arbeitsplan).

Transaktionsunterlagen anfordern (Vollständiger SPA > Deal-Zusammenfassung > nichts). Phasenbasierten Arbeitsplan generieren:

**Tag 1 — rechtlich federführend:** Firmenname Handelsregister; Bankkonten-Bevollmächtigte; Gesellschafterliste § 40 GmbHG; D&O-Nachhaftungsdeckung; IP-Abtretungen.

**Tag 1 — rechtlich begleitend:** Mitarbeiterinformation § 613a Abs. 5 BGB (Frist beachten); Betriebsrat informieren; Kundenanschreiben prüfen.

**Tag 30:** Erster Zustimmungsanlauf (alle Gegenparteien); IP-Umschreibung DPMA; CoC-Vertragsanalyse (Tier 3).

**Tag 90:** Pflicht-Zustimmungen-Frist (SPA); Gesellschaftsbereinigungsentscheidung; HR-Harmonisierung (BetrVG).

**Tag 180:** Verschmelzungsanmeldung §§ 17 ff. UmwG oder Liquidationsanmeldung §§ 65 ff. GmbHG; Garantiefrist-Tracking.

### Modus 2: Vertragsübertragung (`--verträge`)

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

## Output-Template

**Adressat:** Internes Transaktionsteam / Mandant — Tonfall: sachlich-strukturiert, handlungsorientiert

```
PMI-STATUSBERICHT
Mandat: [MANDATSCODE]
Zielgesellschaft: [ZIELGESELLSCHAFT GmbH]
Closing-Datum: [TT.MM.JJJJ]
Bericht-Datum: [TT.MM.JJJJ] — Tag [N] nach Closing
Erstellt von: [NAME], [KANZLEI]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Weitergabe nur nach ausdrücklicher Freigabe durch Transaktionsleiter.

--- PFLICHT-ZUSTIMMUNGEN (SPA-Anhang [X]) ---
Frist gemäß SPA: [TT.MM.JJJJ] ([N] Tage verbleibend)
Erhalten: [N] von [GESAMT]  ████░░░░  [%]
Offen: [N] (Gegenpartei: [NAME]; kontaktiert: [DATUM])
Verweigert: [N] ⚠️  → SPA-Klausel [§/Ziff.] gefährdet

--- VERTRAGSÜBERTRAGUNGEN ---
Tier 1 (SPA-Pflicht): [N] offen / [N] abgeschlossen
Tier 2 (kein Sperrvermerk): [N] offen / [N] abgeschlossen
Tier 3 (CoC-Klausel ausgelöst): [N] ⚠️ — sofortiger Handlungsbedarf
Tier 4 (automatisch übertragen): [N] erledigt

--- GESELLSCHAFTSRECHTLICHE POST-CLOSING-PFLICHTEN ---
☐ Gesellschafterliste § 40 GmbHG beim Notar eingereicht [DATUM / OFFEN]
☐ Handelsregisteranmeldung [HRA/HRB-Nr.] aktualisiert [DATUM / OFFEN]
☐ IP-Umschreibung DPMA [DATUM / OFFEN]
☐ D&O-Nachhaftung bestätigt [DATUM / OFFEN]
☐ Bankkonten-Bevollmächtigte geändert [DATUM / OFFEN]

--- § 613a BGB / BETRIEBSÜBERGANG ---
☐ Arbeitnehmerinformation § 613a Abs. 5 BGB versandt [DATUM / OFFEN]
☐ Widerspruchsfrist (1 Monat ab Information) läuft bis: [TT.MM.JJJJ]
☐ Betriebsrat informiert (§§ 111 ff. BetrVG) [DATUM / OFFEN]
☐ Massenentlassung § 17 KSchG: [RELEVANT / NICHT RELEVANT]

--- NÄCHSTE SCHRITTE (7-Tage-Fenster) ---
1. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
2. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
3. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]

--- BLOCKIERER & ENTSCHEIDUNGSBEDARF ---
⚠️ [BESCHREIBUNG BLOCKIERER] — benötigt Entscheidung von: [PERSON/GREMIUM]

--- RISIKOAMPEL ---
Gesamt: [GRÜN / GELB / ROT]
Begründung: [KURZBESCHREIBUNG]
```

## Rote Schwellen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Tier-3-CoC-Klausel ausgelöst, aber kein Kontakt** → Recht kann mit Closing-Datum zu laufen begonnen haben; Gegenseite sofort anschreiben.
- **SPA-Pflicht-Zustimmungen: Frist < 14 Tage, < 100 %** → Transaktionsleiter eskalieren; MAC-Klausel prüfen.
- **Gesellschafterliste § 40 GmbHG > 3 Wochen nach Closing nicht beim Notar** → Haftungsrisiko; sofort beauftragen.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
