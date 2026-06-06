---
name: stand-technik-patr2-anmeldeverfahren
description: "Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin im Patentrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Stand-der-Technik-Recherche — Workflow

## Arbeitsbereich

Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: PatG § 34 Anmeldetag, § 41 Priorität 12 Monate, § 81 Nichtigkeitsklage, EPÜ Art. 99 Einspruch 9 Monate, R. 161/162 EPÜ 6 Monate, UPC Opt-out bis Ablauf Transition.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 41, 59, 81, 139, 140a, 140b, EPÜ Art. 52, 54, 56, 64, 69, 87-89, PCT Art. 3, 8, UPCA, EinheitspatentVO 1257/2012 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Erfinder, Patentanwalt, DPMA, EPA, BPatG, BGH X. Senat, UPC, Wettbewerber (Einsprechende).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Patentanmeldung, Patentschrift, Recherchebericht, Prüfungsbescheid, Einspruchsschrift, Nichtigkeitsklage, FTO-Gutachten, UPC-Klage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Wann nutzen?

- vor eigener Anmeldung.
- zur Prüfung eines Anspruchsentwurfs.
- nach Abmahnung oder Prüfungsbescheid.
- für Einspruch/Nichtigkeitsangriff.
- für Investor-/FTO-Vorrecherche.

## Rechercheauftrag erzeugen

1. Erfindung in Merkmale und technische Wirkung zerlegen.
2. Deutsche und englische Begriffe bilden.
3. Oberbegriffe, Synonyme, Herstellerjargon und Funktionsbegriffe ergänzen.
4. CPC/IPC-Kandidaten bestimmen.
5. Datenbanken und Länder auswählen.
6. Suchstrings dokumentieren.
7. Treffer in Clustern bewerten: hoch, mittel, niedrig, nur Kontext.

## Übergabe an `patentrecherche`

Wenn konkrete Datenbankrecherche nötig ist, schlage vor:

- `patentrecherche/klassifikation-cpc-ipc`
- `patentrecherche/agentische-datenbank-recherche`
- `patentrecherche/stand-der-technik-recherche`
- `patentrecherche/recherchebericht-erstellen`

## Output

- Suchprofil.
- Suchstrings.
- Datenbankplan.
- Trefferbewertungsschema.
- Dokumentationsvorlage für spätere Nachvollziehbarkeit.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
