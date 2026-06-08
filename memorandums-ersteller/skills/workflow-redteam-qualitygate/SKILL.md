---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Memorandums Ersteller."
---

# Red-Team Qualitygate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Verjährung Anwaltshaftung § 195 BGB 3 Jahre, ggf. § 199 (Kenntnis), Mandatsannahme/Ablehnung unverzüglich, BRAO § 44 Annahme/Ablehnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 43b, 49b (Verschwiegenheit/Haftung), BORA §§ 2, 5, 11, BGB §§ 280, 675 (Anwaltshaftung), HOAI-/RVG-Aspekte, ZPO § 138 (Wahrheitspflicht) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Rechtsanwalt, Auftraggeber (intern: Rechtsabteilung), Gegner, ggf. Gericht (bei Vorlage), externer Spezialist.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Memo (Sachverhalt, Frage, Kurzergebnis, Begründung, Risiko, Empfehlung), Akteneinsichtsantrag, Vollmacht, Honorarvereinbarung, Tatsachenpaket — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Red-Team-Punkte Memo
- **Halluzinations-Scan:** Jede zitierte Entscheidung mit echtem Az.? "Ständige Rspr." mit konkretem Az. belegt? Kommentar-/Aufsatzfundstellen mit Quelle?
- **Anspruchsgrundlagen vollständig?** Reihenfolge Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung (vgl. CLAUDE.md / `references/methodik-buergerliches-recht.md`).
- **Subsumtion sauber?** Obersatz - Definition - Tatsachen - Schluss; keine Sprung-Subsumtion; keine Zirkelschlüsse.
- **Gegenargumente / Mindermeinung gewürdigt?** Wenn entscheidungserheblich.
- **Sondernormen geprüft?** AGB-Recht (§§ 305 ff. BGB), Verbraucherschutz (§§ 13, 14, 312 ff. BGB), DSGVO, Sektorengesetze (KWG, ZAG, GWG, etc.).
- **Auslegung erklärt?** Vier Auslegungsmethoden zzgl. verfassungs-/unionsrechtskonform.
- **Empfehlung klar?** Eine Linie, mit Begründung; Alternativen mit Trade-off.
- **Risikoanalyse?** Restrisiken benannt; "Cone of uncertainty".
- **Form:** Kurzantwort am Anfang, Quellenverzeichnis am Ende, Privileged & confidential.
- **Sprache:** Gutachtenstil bei Memo-Hauptteil; Cover-Letter mandantengerecht.
- Falle: Memo nur aus Mandantenperspektive -- bedenke immer auch die Sicht der Gegenseite / der Behörde / des Gerichts.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

