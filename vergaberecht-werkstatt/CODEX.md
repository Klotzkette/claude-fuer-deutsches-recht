# CODEX.md – Repository-Hinweise für OpenAI Codex

Dieses Repository ist die Vergaberecht-Werkstatt (drei Plugins: `vergabestelle-behoerden`, `bieter-unternehmen`, `konkurrenten-rechtsschutz`). Vollständige Regeln in [`CLAUDE.md`](./CLAUDE.md) und [`AGENTS.md`](./AGENTS.md) — beide gelten unverändert.

## Kurzleitfaden

- Vergaberecht hat drei Marktrollen mit gegenläufigen Interessen: Vergabestelle, Bieter/Bewerber und Konkurrent/Zuschlagsgegner. Niemals mehrere Rollen gleichzeitig optimieren.
- Rechtsregime trennen nach EU-Schwellenwert. Oberhalb: GWB Teil 4 plus passendes Spezialregime, Nachprüfung VK/OLG. Unterhalb: Haushalts-, UVgO-/VOB/A- und Landesrecht; Rechtsweg und Primärrechtsschutz nicht pauschalisieren.
- Schwellenwerte über EUR-Lex oder die EU-Kommission aktuell prüfen; sie ändern sich alle zwei Jahre per EU-Verordnung.
- Anker-Rechtsprechung: EuGH C-81/98 "Alcatel" (Vorabinformation), EuGH C-19/00 "SIAC" (Transparenz), BGH X ZB 10/16 (ungewöhnlich niedriges Angebot), BGH XIII ZR 19/19 (Schadensersatz bei rechtswidriger Aufhebung), BVerfG 1 BvR 1160/03 (Unterschwellen-Rechtsschutz). Aktueller Prüfanker: Schlussanträge GA Kokott vom 07.05.2026, Rs. C-268/25, ECLI:EU:C:2026:382, zu Bietergemeinschaften und Steuerverstoß eines Mitglieds; ausdrücklich nicht als EuGH-Urteil behandeln.
- Quellenhygiene: keine erfundenen Aktenzeichen, keine Kommentar- oder Aufsatz-Zitate aus Modellwissen. Nur Primärquellen.

## Gliederung

Dezimal: `1`, `1.1`, `1.1.1`. Niemals `I/II/A/B/a/b`. Leerzeile zwischen Punkten.

## Validatoren

Vor jedem Commit mindestens diese Prüfungen grün:

```
python3 -m pip install -r requirements-dev.txt
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
python3 scripts/run-smoke-tests.py --quick
```

## Plugin-Slugs

- `vergabestelle-behoerden`
- `bieter-unternehmen`
- `konkurrenten-rechtsschutz`

Alle Plugin-Slugs sind höchstens 64 Zeichen lang. Skill-Slugs bleiben stabil und müssen kein Nummernpräfix tragen.

## Verbotene Inhalte

- Keine Honorar- oder RVG-Berechnung.
- Keine Beratungs- oder Kanzleiempfehlungen.
- Keine festen Margenangaben in Kalkulationen — bleibt bieterindividuell.

## Author identity

- Name: `Klotzkette`
- E-Mail: `39582916+Klotzkette@users.noreply.github.com`
