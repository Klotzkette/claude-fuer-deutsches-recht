---
name: mandat-arbeitsbereich
description: >
  Mandats-Workspaces verwalten — anlegen, auflisten, wechseln, schließen oder vom
  aktiven Mandat trennen, damit Mehrfachmandatsanwälte den Kontext eines Mandats
  sauber von jedem anderen trennen. Wird von allen inhaltlichen Skills gelesen, die
  wissen müssen, in welchem Mandat sie arbeiten. Lädt bei „neues Mandat", „Mandat
  wechseln", „Mandate auflisten", „Mandat schließen" oder wenn der Nutzer nur auf
  Praxisebene arbeiten möchte.
language: de
triggers:
  - "neues Mandat"
  - "Mandat anlegen"
  - "Mandat wechseln"
  - "Mandate auflisten"
  - "Mandat schließen"
  - "Mandatsworkspace"
  - "Datenraum-Phase"
  - "NDA-Phase"
  - "LOI"
  - "SPA-Verhandlung"
argument-hint: "<neu | liste | wechseln | schließen | keine> [slug]"
---

# Mandats-Workspace

## Zweck

Rechtsanwälte und Syndikusrechtsanwälte arbeiten parallel an mehreren Mandaten und Projekten. Ein Mandats-Workspace hält den Kontext eines Mandanten oder Projekts sauber von jedem anderen getrennt. Dieser Skill verwaltet diese Workspaces.

Im M&A-Kontext unterstützt er die typischen Transaktionsphasen: NDA-Phase und Zugang zum Datenraum, Letter of Intent (LOI), Due-Diligence-Phase, SPA-Verhandlung, Signing und Closing sowie Post-Closing-Integration.

## Eingaben

- Unterbefehl (neu / liste / wechseln / schließen / keine) und ggf. Slug
- Bei `neu`: Angaben zu Mandant, Gegenpartei, Mandatstyp, wesentliche Fakten, mandatsspezifische Abweichungen vom Praxisstandard

## Rechtlicher Rahmen

Das Mandatsgeheimnis (§ 43a Abs. 2 BRAO, § 203 Abs. 1 Nr. 3 StGB) verbietet die unerlaubte Offenbarung mandatsbezogener Informationen. Die strikte Mandatstrennung in diesem Skill ist technische Umsetzung dieser Pflicht.

Bei M&A-Mandaten: § 43a Abs. 2 BRAO (Verschwiegenheitspflicht); § 53 StPO (Zeugnisverweigerungsrecht); §§ 1 ff. GwG (Geldwäscheprävention, Mandantenidentifizierung). Interessenkonflikte sind nach § 43a Abs. 4 BRAO und der BORA zu prüfen — dieser Skill übernimmt keine Konfliktprüfung (s. u.).

BGH, Urt. v. 25.06.2015 – IX ZR 199/14, NJW 2015, 3239 Rn. 18 (Anwaltliche Verschwiegenheitspflicht; Schadensersatz bei Verletzung); BGH, Urt. v. 17.09.2015 – IX ZR 280/14, NJW 2016, 317 Rn. 20 (Interessenkonflikt; Kündigung des Mandats bei Pflichtenkollision).

**Kommentarliteratur:** Roth/Altmeppen, GmbHG, 11. Aufl. 2024, Einl. Rn. 15 ff. (Mandatsverhältnis im Gesellschaftsrecht); Baumbach/Hopt, HGB, 41. Aufl. 2024, Einl. vor § 1 Rn. 10 ff. (Berufsrecht der rechtsberatenden Berufe).

## Ablauf

### Schritt 1: Praxisprofil lesen

CLAUDE.md lesen — Abschnitt `## Mandats-Workspaces` prüfen. Falls `Aktiviert` = `✗` (Standard für In-house-Nutzer):

> Mandats-Workspaces sind deaktiviert — Sie sind als interner Rechtsberater mit einem Mandanten konfiguriert, sodass der Skill automatisch mit Praxiskontextdaten arbeitet. Wenn Sie tatsächlich für mehrere Mandanten tätig sind, führen Sie `/gesellschaftsrecht:kaltstart-interview --redo` aus und wählen ein Kanzleisetting. Andernfalls benötigen Sie `/mandats-workspace` nicht.

Kein Fehler — der deaktivierte Zustand ist der erwartete für In-house-Nutzer.

### Schritt 2: Unterbefehl ausführen

Ersten Token von `$ARGUMENTE` auswerten:
- `neu` → Aufnahme-Interview durchführen, `mandate/<slug>/mandat.md` schreiben, `verlauf.md` und `notizen.md` anlegen
- `liste` → `mandate/*/mandat.md` aufzählen, Tabelle ausgeben, aktives Mandat markieren
- `wechseln` → `Aktives Mandat:`-Zeile in CLAUDE.md auf Praxisebene aktualisieren
- `schließen` → `mandate/<slug>/` nach `mandate/_archiv/<slug>/` verschieben, Schließungsdatum in `verlauf.md` erfassen
- `keine` → `Aktives Mandat:` auf `keine — nur Praxiskontextdaten` setzen

Änderungen vor dem Schreiben anzeigen und bestätigen.

### Unterbefehl `neu <slug>`

1. Slug prüfen: nicht bereits in `mandate/<slug>/` oder `mandate/_archiv/<slug>/` vorhanden. Falls wiederverwendet: anderen Slug vorschlagen.
2. Aufnahme-Interview durchführen:
   - **Mandant** (die vertretene Partei oder interne Geschäftseinheit bei In-house)
   - **Gegenpartei** (die andere Seite — kann mehrere sein)
   - **Mandatstyp** (für gesellschaftsrecht: M&A Käuferseite | M&A Verkäuferseite | Finanzierung | Governance-Mandat | Gesellschaftsreorganisation | Integrationsprojekt | Sonstige)
   - **Transaktionsphase** (NDA-Phase | LOI-Phase | Due-Diligence-Phase | SPA-Verhandlung | Signing/Closing | Post-Closing-Integration | Laufende Beratung)
   - **Vertraulichkeitsstufe** (standard | erhöht | Clean-Team — erhöht veranlasst besondere Sorgfalt in mandatsübergreifenden Settings)
   - **Wesentliche Fakten** (2–5 Sätze: worum es geht, wer die Stakeholder sind, was auf dem Spiel steht)
   - **Mandatsspezifische Abweichungen vom Praxisprofil** (z.B. „Mandant verlangt 24-monatige Haftungsdeckelung statt 12 Monaten", „Gegenpartei ist strategischer Partner — beziehungspflegender Ton")
   - **Verbundene Mandate** (Slugs ggf. verbundener Mandate)
3. `mandate/<slug>/mandat.md` anhand der untenstehenden Vorlage schreiben.
4. `mandate/<slug>/verlauf.md` mit Eintrag „Eröffnet" anlegen.
5. Leere `mandate/<slug>/notizen.md` erstellen.
6. **Nicht** automatisch wechseln. Fragen: „Möchten Sie jetzt zu `<slug>` wechseln? (`/gesellschaftsrecht:mandats-workspace wechseln <slug>`)"

### Unterbefehl `liste`

`mandate/*/mandat.md` aufzählen. Jede Datei lesen, Status extrahieren. Tabelle ausgeben:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktuell aktives Mandat mit `*` markieren. `_archiv/*` unter separater Überschrift „Archiv" aufführen, falls vorhanden.

### Unterbefehl `wechseln <slug>`

1. `mandate/<slug>/mandat.md` auf Existenz prüfen. Falls nicht vorhanden: `/gesellschaftsrecht:mandats-workspace neu <slug>` anbieten.
2. `Aktives Mandat:`-Zeile in CLAUDE.md auf Praxisebene auf `Aktives Mandat: <slug>` ändern.
3. Inhalt von `mandat.md` zusammenfassen, damit der Nutzer bestätigen kann, das richtige Mandat gewählt zu haben.

### Unterbefehl `schließen <slug>`

1. `mandate/<slug>/` auf Existenz prüfen.
2. Eintrag „Geschlossen" mit heutigem Datum an `mandate/<slug>/verlauf.md` anhängen.
3. `mandate/<slug>/` → `mandate/_archiv/<slug>/` verschieben.
4. War das geschlossene Mandat das aktive: `Aktives Mandat:` auf `keine — nur Praxiskontextdaten` setzen.

### Unterbefehl `keine`

`Aktives Mandat:` in CLAUDE.md auf `keine — nur Praxiskontextdaten` setzen. Mit Nutzer bestätigen.

## Ausgabeformat

Änderungsbestätigung und Inhaltszusammenfassung der relevanten `mandat.md`. Bei `liste`: Tabelle aller Mandate.

## Mandat.md-Vorlage

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — je nach Nutzerprofil aus CLAUDE.md]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]
**Transaktionsphase:** [NDA | LOI | Due Diligence | SPA-Verhandlung | Signing/Closing | Post-Closing | Laufend]

---

## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Mandatstyp

[M&A Käuferseite | M&A Verkäuferseite | Finanzierung | Governance-Mandat | Gesellschaftsreorganisation | Integrationsprojekt | Sonstige — mit Ein-Satz-Begründung]

## Wesentliche Fakten

[2–5 Sätze. Worum geht es. Wer sind die Stakeholder. Was steht auf dem Spiel. Was macht dieses Mandat vom Standardprofil abweichend.]

## Mandatsspezifische Abweichungen

*Jede Abweichung vom Praxisprofil auf Mandatsebene, die nur für dieses Mandat gilt.*

- [z.B. „Haftungsdeckelung: Mandant besteht auf 24 Monaten, nicht Hausstandard 12 Monate."]
- [z.B. „Ton: beziehungspflegend — Gegenpartei ist strategischer Partner."]
- [z.B. „Anwendbares Recht: muss deutsches Recht sein, nicht englisches Recht."]

## Verbundene Mandate

- [slug — ein Satz, warum verbunden]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer die Mandatsunterlagen einsehen darf. Ob mandatsübergreifender Kontext zulässig ist, auch wenn global aktiviert.]
```

## Verlauf.md-Startdatei

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Nur-Anhängen-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Ggf. anfänglicher Kontext — z.B. „Eröffnet auf Eingang eines SPA-Entwurfs von [Gegenpartei]."]
```

## Mandatsübergreifender Kontext

CLAUDE.md auf Praxisebene enthält einen `Mandatsübergreifender Kontext:`-Schalter. Wenn er `aus` ist (Standard): Ein Skill, der in Mandat A arbeitet, liest **niemals** Dateien in `mandate/B/` für ein anderes Mandat B. Dies ist die Vertraulichkeitsgarantie, für die diese Einstellung existiert.

Wenn er `an` ist: Ein Skill darf Dateien mandatsübergreifend nur dann lesen, wenn der Nutzer dies ausdrücklich verlangt (z.B. „Vergleiche unsere Haftungsbegrenzungen in den letzten fünf Vendor-Mandaten"). Auch bei `an` ist der Standard: nur das aktive Mandat laden, außer der Nutzer fragt ausdrücklich nach einem Mandatsvergleich.

## Hinweise

- Slugs sind Kleinbuchstaben mit Bindestrichen. Beispiele: `abc-gmbh-anteilskauf-2026`, `zenith-renewal`, `vendor-xyz-nda`.
- Der Skill führt keine Interessenkonfliktprüfung durch — das ist Aufgabe des Anwalts / der Sozietät.
- Schließen ist kein Löschen — archivierte Mandate bleiben für Archivierungs- und Konfliktzwecke lesbar.
- Bei Wiederverwendung eines Slugs aus dem Archiv: Archiv-Version bleibt unter `_archiv/<slug>/` erhalten.
## Beispiel

**Szenario M&A Käuferseite:** Sozietät begleitet GmbH-Anteilskauf. Neues Mandat angelegt: Slug `alpha-gmbh-anteilskauf-2026`, Mandatstyp M&A Käuferseite, Transaktionsphase Due-Diligence, erhöhte Vertraulichkeit (Clean-Team). Zwei verbundene Mandate (NDA-Phase und LOI-Phase) verknüpft. Nach Closing: Mandat auf Phase Post-Closing-Integration aktualisiert. Nach Abschluss der Integration: `/gesellschaftsrecht:mandats-workspace schließen alpha-gmbh-anteilskauf-2026` archiviert das Mandat dauerhaft.


## Risiken und typische Fehler

- **Mandatsübergreifenden Kontext bei sensiblen Mandaten aktiviert lassen.** Bei erhöhter Vertraulichkeit in `mandat.md` explizit vermerken, dass mandatsübergreifender Kontext für dieses Mandat unzulässig ist.
- **Slugs nicht eindeutig wählen.** Mehrere Mandate mit ähnlichem Namen führen zu Verwechslungen. Mandant + Transaktionsart + Jahr verwenden.
- **In-house-Nutzer aktivieren Workspaces unnötig.** Standardmäßig deaktiviert; nur für Mehrfachmandatsanwälte erforderlich.

## Quellenpflicht

Mandatsgeheimnis und Interessenkonflikte:
- `§ 43a Abs. 2 BRAO` (Verschwiegenheitspflicht)
- `§ 203 Abs. 1 Nr. 3 StGB` (Verletzung von Privatgeheimnissen)
- `BGH, Urt. v. 25.06.2015 – IX ZR 199/14, NJW 2015, 3239 Rn. 18`

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
