---
name: zeitnarrative
description: "Für Zeitnarrative und Timesheet: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Zeitnarrative und Timesheet

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Für welche Akte und welchen Bearbeiter soll der Zeiteintrag erfasst werden?
2. Ist die Taetigkeit nach RVG oder nach Stundensatz abrechenbar — oder intern (nicht abrechenbar)?
3. Gibt es eine genaue Zeitangabe oder soll die Dauer aus dem Workflow-Verlauf geschaetzt werden?
4. Soll der Eintrag sofort in die Rechnung oder erst in das interne Timesheet?

## Zentrale Normen
- § 10 RVG — Pflichtangaben auf der Rechnung: Taetigkeitsnachweis als Faelligkeitsvoraussetzung
- § 3a RVG — Honorarvereinbarung: Stundensatz-Abrechnung und Dokumentationspflicht
- § 147 AO — Aufbewahrungspflicht: Zeiterfassungsbelege 10 Jahre
- § 238 HGB — Buchfuehrungspflicht: Zeitnarrative als Teil der betrieblichen Aufzeichnungen

## Standardfrage

> Soll ich für die letzte Stunde einen Zeiteintrag vorbereiten? Ich habe folgende mögliche Tätigkeiten erkannt: ... Welcher Akte soll ich das zuordnen?

## Ablauf

1. Beobachtete oder geschilderte Tätigkeit zusammenfassen.
2. Aktenzuordnung vorschlagen und Unsicherheit markieren.
3. Bearbeiter, Rolle und Verantwortlichen erfassen.
4. Start, Ende, Dauer, Mindesttakt und Rundung erfragen oder vorschlagen.
5. Tätigkeit klassifizieren: Intake, Aktenprüfung, Frist, Recherche, Schriftsatz, Telefonat, Mandantenkontakt, Gegnerkontakt, Gerichtskontakt, beA, Rechnung, intern.
6. Abrechenbarkeit markieren: abrechenbar, nicht abrechenbar, pro bono, intern, Pauschale enthalten, RVG-Nachweis.
7. Honorargrundlage: RVG, Stundenhonorar, Pauschale, Vorschuss, Rechtsschutz, Kulanz.
8. Rechnungsfähigkeit prüfen: mandantenfähig, verständlich, quellenbasiert, ohne unnötige Geheimnisse.
9. Narrative formulieren: knapp, mandatsbezogen, prüfbar.
10. Freigabe abfragen.
11. Übergabe an `kanzlei-allgemein-rechnung` vormerken, wenn abrechnungsreif.

## Narrative-Stil

Gut:

- "Prüfung beA-Eingang und Fristnotierung; Entwurf Rückfrage an Mandant."
- "Analyse Klageerwiderung und Strukturierung der Gegenargumente."
- "Telefonat mit Mandant zur Sachverhaltsergänzung und Abstimmung der nächsten Schritte."
- "Entwurf und Überarbeitung Schriftsatzantwort einschließlich Anlagenabgleich."

Nicht gut:

- interne Gedankengänge,
- überflüssige Geheimnisse,
- unsichere Spekulationen,
- personenbezogene Details ohne Abrechnungsnutzen.

## Granularität

Für Rechnungen lieber mehrere saubere Einträge als einen Sammelblock erzeugen:

- beA-Eingang prüfen.
- Frist und Vorfrist notieren.
- Anlagen sichten.
- Rechtsfrage prüfen.
- Mandantenrückfrage entwerfen.
- Schriftsatz entwerfen.
- Schriftsatz finalisieren.
- Versand vorbereiten.

Nicht künstlich zersplittern, wenn ein zusammenhängender Arbeitsblock fachlich besser passt. Ziel ist prüfbare, verständliche Abrechnung.

## Datenschutzreduktion

Narrative sollen genug Inhalt für Rechnung und Prüfung enthalten, aber keine unnötigen Mandatsgeheimnisse offenlegen. Namen Dritter, Gesundheitsdaten, Bankdaten, Kinder, Strafvorwürfe und interne Prozessstrategie nur aufnehmen, wenn sie für die Abrechnung wirklich erforderlich sind.

## Rechnungsschnittstelle

Jeder freigegebene abrechenbare Eintrag bekommt:

- Rechnungsstatus: offen, gesperrt, abgerechnet, nicht abrechenbar.
- Rechnungsposition oder RVG-Nachweis.
- Leistungszeitraum.
- Bearbeiter.
- Nettofähige Beschreibung.
- Hinweis, ob die Narrative in eine Anlage zur E-Rechnung übernommen werden darf.

## Ausgabe

`assets/templates/zeit-narrative-ledger.md` verwenden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Automationshinweis

Wenn Automationen verfügbar sind, nach Zustimmung stündliche Erinnerung vorschlagen. Keine stille Dauerüberwachung.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
