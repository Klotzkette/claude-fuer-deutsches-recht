---
name: tdm-opt-out-maschinenlesbar-pruefen
description: "Für TDM-Opt-out — Maschinenlesbarkeit prüfen und implementieren: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# TDM-Opt-out — Maschinenlesbarkeit prüfen und implementieren

## Arbeitsbereich

Technische und rechtliche Prüfung des TDM-Opt-outs nach § 44b Abs. 3 UrhG und DSM-RL Art. 4 Abs. 3: Maschinenlesbarkeitsanforderungen für robots.txt, HTTP-Header (X-Robots-Tag), meta-Tags und strukturierte Metadaten. Bewertet Wirksamkeit von Opt-out-Erklärungen, deren Zeitpunkt und Reichweite sowie technische Implementierungsstandards. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber will sicherstellen, dass sein TDM-Opt-out gegenüber kommerziellen KI-Anbietern wirksam ist und fragt, welche technischen Maßnahmen erforderlich sind.
- KI-Unternehmen muss prüfen, ob die von ihm gescrapten Websites einen wirksamen Opt-out erklärt haben, bevor es mit dem Training beginnt.
- Rechtsabteilung fragt, ob ein allgemeines AGB-Verbot für automatisierten Abruf als maschinenlesbarer Opt-out gilt oder ob separate technische Erklärungen erforderlich sind.

## Erste Schritte

1. Opt-out-Anforderungen nach § 44b Abs. 3 UrhG klären: Der Vorbehalt muss maschinenlesbar erklärt werden — AGB-Text allein genügt nicht.
2. robots.txt prüfen: Gibt es einen robots.txt-Eintrag, der TDM-Abrufwerkzeuge explizit ausschließt (z. B. `Disallow: /` für alle Bots oder spezifische TDM-Abrufwerkzeuge)?
3. HTTP-Header analysieren: X-Robots-Tag: noindex, noarchive, noimageindex — welche Header sind gesetzt und welche Abrufwerkzeuge respektieren sie?
4. Structured-Data-Metadaten prüfen: Gibt es maschinenlesbare Metadaten (schema.org, ODRL) mit explizitem TDM-Vorbehalt?
5. Zeitpunkt des Opt-outs: War der Opt-out vor dem Auslesevorgang aktiv? Rückwirkung ist ausgeschlossen.
6. Reichweite des Opt-outs: Gilt er für alle Inhalte oder nur bestimmte Teile der Datenbank?

## Rechtsrahmen

- § 44b Abs. 3 UrhG: TDM-Vorbehalt muss in maschinenlesbarer Form erklärt werden — zeitlich vor dem TDM-Abruf.
- DSM-RL Art. 4 Abs. 3: Rechteinhaber können TDM für kommerzielle Zwecke durch maschinenlesbaren Vorbehalt ausschließen.
- Erwägungsgrund 18 DSM-RL: Maschinenlesbar meint technisch standardisierte Formate, die automatisch erkannt werden können.
- § 44b Abs. 1 UrhG: Ohne wirksamen Opt-out ist TDM-Vervielfältigung für kommerzielle Zwecke erlaubt.
- § 60d UrhG: Wissenschaftliches TDM — kein Opt-out möglich, daher Opt-out-Prüfung irrelevant für § 60d.
- § 97 UrhG: Unterlassung und Schadensersatz bei Verletzung — setzt wirksamen und rechtzeitigen Opt-out voraus.

## Prüfraster

- Ist ein robots.txt-Eintrag vorhanden, der TDM-relevante Abrufwerkzeuge ausschließt?
- Werden HTTP-Header (X-Robots-Tag) eingesetzt, die maschinenlesbar TDM verbieten?
- Gibt es strukturierte Metadaten (ODRL-Policys, schema.org) mit explizitem TDM-Ausschluss?
- War der Opt-out zeitlich vor dem streitgegenständlichen Auslesevorgang aktiv gesetzt?
- Ist der Opt-out auf alle Inhalte der Datenbank anwendbar oder nur auf Teile?
- Respektieren die eingesetzten TDM-Abrufwerkzeuge überhaupt die Opt-out-Signale — werden technische Sperren benötigt?
- Reicht ein allgemeines AGB-Verbot als maschinenlesbarer Opt-out — oder muss zwingend eine technische Erklärung vorhanden sein?

## Typische Fallstricke

- AGB-Verbot für automatisierten Abruf gilt nicht als maschinenlesbar im Sinne des § 44b Abs. 3 UrhG — kein wirksamer Opt-out.
- robots.txt-Einträge ohne expliziten Bezug auf TDM-Verbot schließen nicht alle kommerziellen TDM-Abrufwerkzeuge aus.
- Opt-out nach dem Abrufereignis erklärt — zu spät für diese konkrete Verletzung, gilt nur für die Zukunft.
- Viele KI-Trainings-Abrufwerkzeuge ignorieren robots.txt technisch oder identifizieren sich nicht korrekt — Opt-out technisch erzwingen.
- Fehlender Opt-out für einen Datenbankabschnitt kann TDM für diesen Teil erlaubt sein, obwohl der Rest geschützt ist.

## Quellen

- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [§ 60d UrhG — dejure.org](https://dejure.org/gesetze/UrhG/60d.html)
- [DSM-Richtlinie 2019/790 Art. 4 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
