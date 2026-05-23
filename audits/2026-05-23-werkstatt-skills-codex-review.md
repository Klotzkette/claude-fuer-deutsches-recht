# Codex-Audit-Anfrage 2026-05-23: Werkstatt-Skills aus PR #13

@codex review

## Kontext

PR #13 (Commit `54bd016d`) hat drei Stub-Skills im Plugin
`urteilsbauer-relationsmacher` substantiell ausgebaut. Codex hatte
bei der ursprünglichen Review zwei juristische Bugs gefunden, die
in PR #15 und PR #16 bereits adressiert wurden.

Jetzt: vollständiger juristischer Zweit-Review der drei Skills.

## Bitte-an-Codex

Bitte prüfe die folgenden drei Skill-Dateien gezielt auf:

1. **Juristische Korrektheit der BGH-/BVerfG-Zitate**
   — existieren die zitierten Aktenzeichen?
   — passen Aktenzeichen, Jahrgang, Fundstelle und Randnummer zusammen?
   — sind die Aussagen, die ihnen zugeschrieben werden, im Beleg-Urteil
     tatsächlich enthalten?

2. **Paragrafen-Verweise**
   — sind alle ZPO-, BGB-, GVG-Paragrafen tatbestandsmäßig richtig
     verortet?
   — gibt es Verweise auf Paragrafen, die so nicht (mehr) existieren?
   — sind Absatz-Verweise korrekt?

3. **Tenor-Bausteine und Begründungsmuster**
   — sind die vorgeschlagenen Tenor-Formulierungen juristisch korrekt?
   — passen Entscheidungsform (Urteil/Versäumnisurteil/Beschluss) und
     Rechtsgrundlage zusammen (vgl. PR #16 zum einseitige-Erledigung-Bug)?
   — sind die typischen Fehler-Listen vollständig oder fehlen wichtige
     Klassiker?

4. **Workflow-Handoffs zu anderen Skills**
   — referenzieren die Skills nur Skill-IDs, die im Repo tatsächlich
     existieren? (vgl. PR #15)

## Zu prüfende Dateien

- `urteilsbauer-relationsmacher/skills/beschluss-bauen-zpo/SKILL.md`
- `urteilsbauer-relationsmacher/skills/aktenintake-zivil/SKILL.md`
- `urteilsbauer-relationsmacher/skills/revisionsfest-pruefen/SKILL.md`

## Schweregrad-Bitte

Bitte als P1 (juristischer Fehler, der zu falscher Entscheidung führen
würde), P2 (handwerklicher Mangel, formal falsch aber nicht ergebnis-
verfälschend) oder P3 (Stil, kosmetisch) klassifizieren.

Findings werden nicht in diesem PR adressiert — dieser PR ist eine
reine Review-Anforderung. Etwaige Fixes folgen in eigenen Hotfix-PRs.
