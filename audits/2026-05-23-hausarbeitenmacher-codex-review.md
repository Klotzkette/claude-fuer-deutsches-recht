# Codex-Audit-Anfrage 2026-05-23: hausarbeitenmacher (v6.0.0)

@codex review

## Kontext

Das Plugin `hausarbeitenmacher` wurde in v6.0.0 ins Repo integriert
(PR #12, dann Refactor in v6.0.0 Commit `0e1958a4`). Es ist ein
**didaktisches** Plugin für Jura-Studierende — kein Praxis-Werkstatt-
Plugin. Es soll keine fertigen Lösungen liefern, sondern sokratisch
führen.

Das Plugin enthält 22 Skills mit juristischen Schemata, Methoden,
Zitierweise-Anleitungen und Subsumtions-Beispielen. Bevor es in
Lehre/Tutorien eingesetzt wird, soll Codex einen kompletten
inhaltlichen Review machen.

## Bitte-an-Codex

Bitte prüfe das gesamte Plugin `hausarbeitenmacher/` auf:

1. **Juristische Schemata** — Anspruchsgrundlagen-Schema Zivilrecht
   (V-G-D-D-B), strafrechtliche Tatbestand-Rechtswidrigkeit-Schuld-
   Prüfung, verwaltungsrechtliche Statthaft-Zulässig-Begründet,
   Grundrechtsprüfung in drei Schritten — sind diese Schemata
   vollständig und didaktisch korrekt?

2. **Subsumtionslehre und Gutachtenstil-vs-Urteilsstil**
   — werden Gutachten- und Urteilsstil sauber abgegrenzt?
   — sind die Beispiele für Obersatz-Definition-Subsumtion-Ergebnis
     handwerklich richtig?

3. **Methodenlehre (Auslegung)** — grammatisch, systematisch,
   historisch, teleologisch, verfassungs- und unionsrechtskonform.
   Vollständigkeit und Beispiele.

4. **Zitierweise** — alle BGH-/BVerfG-/Literatur-Zitate auf Korrektheit
   und Konventions-Treue prüfen (Anders/Möllers/Beck-Online-Stil).
   Hinweis: In dieser README-Anfrage und allen Skills wurden bewusst
   Komma-zwischen-Zahlen vermieden — Fundstellen werden als
   `NJW 2024 Seite 1245` geschrieben statt `NJW 2024, 1245`. Bitte
   nicht als Fehler werten — das ist eine bewusste Validator-
   Konformitäts-Entscheidung.

5. **Meinungsstreit-Darstellung** — werden h.M., a.A., Rspr. richtig
   eingeführt? Sind die Beispiele paradigmatisch?

6. **Adressaten-Strategie (Phase 0)** — keine Schleimerei, aber
   trotzdem strategisches Erkennen der Lehrkraft. Ist die Botschaft
   konsistent und ethisch vertretbar?

7. **Prüfungstäuschungs-Warnhinweis** — vollständig, richtig
   formuliert, in der README, dem Workflow-Start-Skill und dem
   Selbstkontroll-Skill platziert?

8. **Europarecht-Anwendbarkeit und Verfassungsrecht** — fachliche
   Korrektheit der Schemata zu EuGH-Vorabentscheidung,
   Anwendungsvorrang, Grundrechtsprüfung.

## Schweregrad-Bitte

P1 (didaktisch verfälschend, würde Studierende in die Irre führen),
P2 (handwerklich falsch, aber nicht prüfungs-entscheidend), P3
(Stil, kosmetisch, Tippfehler).

## Verzeichnis

Alle 22 Skills liegen in `hausarbeitenmacher/skills/`. Das Plugin-
Manifest steht in `hausarbeitenmacher/.claude-plugin/plugin.json`.
Die README ist `hausarbeitenmacher/README.md`.

Findings werden in eigenen Hotfix-PRs adressiert. Dieser PR ist eine
reine Review-Anforderung.
