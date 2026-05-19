---
name: einfache-sprache-briefe
description: "Referenz: VERALTET — für Routine-Korrespondenz `/mandantenbrief` verwenden, für inhaltliche Statusupdates `/status mandant`. Im Zuge des Umbaus auf Version 2 in zwei fokussiertere Skills aufgeteilt. Lädt, wenn ein Studierender einen verständlichen Mandantenbrief, ein Statusschreiben in leichter Sprache oder eine einfach formulierte Mandantenmitteilung erstellen möchte."
---

# [VERALTET] Verständliche Mandantenbriefe → siehe `/mandantenbrief` und `/status mandant`

## Zweck

Diese Skill wurde im Rahmen des Umbaus auf Version 2 aufgeteilt, weil der ursprüngliche Geltungsbereich zu heterogen war: einfache Terminbestätigungen haben andere Anforderungen als inhaltlich komplexe Statusmitteilungen.

**Routine-Korrespondenz** (Terminbestätigungen, Unterlagenbitten, kurze Eingangsbestätigungen) → `skills/mandantenbrief/` — Befehl `/mandantenbrief [typ]`

**Inhaltliche Statusmitteilungen an Mandanten** (was ist passiert, was passiert als nächstes, was muss der Mandant tun) → `skills/status/` im Mandanten-Modus — Befehl `/status mandant`

Beide Nachfolge-Skills wenden die Verständlichkeitsstandards der Beratungsstelle an (Lesbarkeit Hauptschulniveau, keine nicht erläuterten Fachbegriffe, konkrete Handlungshinweise), wie sie in der Klinik-Konfiguration (CLAUDE.md) festgelegt sind.

## Eingaben

Diese Skill akzeptiert keine Eingaben. Für alle Mandantenbriefe: `/mandantenbrief [typ]` oder `/status mandant`.

## Rechtlicher Rahmen

### Hintergrund der Aufteilung

Die Verständlichkeit von Mandantenkommunikation ist eine Rechtspflicht, keine Serviceleistung. Unverständliche Korrespondenz verletzt die anwaltliche Aufklärungspflicht (§ 43a BRAO, BGH-Rspr.) und kann zur Haftung führen. Die Aufteilung in zwei fokussierte Skills verstärkt diese Pflicht, indem sie die Standards für jeden Typ explizit macht.

### Relevante Normen für die Nachfolge-Skills

- **§ 43a Abs. 4 BRAO** — Sachlichkeitsgebot: Mandantenbriefe müssen sachlich, klar und nicht irreführend sein; gilt auch für studentische Beratungsstellen unter Aufsicht.
- **§ 11a BRAO** — Zusammenarbeit in studentischen Beratungsstellen: Briefe gehen unter Aufsicht des Supervisors heraus; vor Versand ist die Supervisoren-Freigabe einzuholen.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Mandantenkorrespondenz ist ein nach außen gehendes Leistungsergebnis und unterliegt der inhaltlichen Supervisoren-Kontrolle.
- **Art. 13 DSGVO** — Informationspflichten: Falls ein Brief erstmals über die Verarbeitung personenbezogener Daten informiert, müssen DSGVO-Pflichtangaben enthalten sein.
- **§§ 2, 3 BerHG** — Beratungshilfe: Bei Mandanten mit Beratungshilfe-Schein muss die Korrespondenz den Leistungsrahmen einhalten; keine Erweiterung ohne neuen Schein.

### Leitentscheidungen

- BGH, Urt. v. 14.06.2012 – IX ZR 145/11, NJW 2012, 2571 Rn. 12 — Aufklärungspflicht des Rechtsanwalts: Unverständliche Informationen erfüllen die Aufklärungspflicht nicht; Mandant muss den Kern der Mitteilung tatsächlich verstehen können.
- BGH, Urt. v. 20.01.2005 – IX ZR 403/00, NJW 2005, 1116 Rn. 8 — Pflicht zur rechtzeitigen und vollständigen Information des Mandanten; Verzögerung oder Unklarheit begründet Haftung.
- BVerfG, Beschl. v. 08.10.1974 – 2 BvR 747/73, NJW 1975, 103 — Grundrecht auf effektiven Rechtsschutz; Mandanten aus bildungsfernen Schichten haben ein besonderes Interesse an verständlicher Kommunikation.
- BGH, Urt. v. 25.06.2015 – IX ZR 199/14, NJW 2015, 3305 Rn. 18 — Anwaltliche Haftung für Informationsversäumnisse gegenüber dem Mandanten; gilt sinngemäß für Beratungsstellen.

### Kommentarliteratur

- Kleine-Cosack, BRAO, 8. Aufl. 2022, § 43a Rn. 30 ff. — Sachlichkeitsgebot; Verständlichkeitsanforderungen bei Mandantenbriefen.
- Deckenbrock/Henssler, RDG, 5. Aufl. 2021, § 6 Rn. 28 ff. — Außenkommunikation der Beratungsstelle; Anforderungen an Mandantenschreiben unter Aufsicht.
- Greger/Unberath/Steffek, Recht der alternativen Konfliktlösung, 3. Aufl. 2023, § 2 MediationsG Rn. 8 — Verständlichkeitspflicht bei der Mandanteninformation; Maßstab.
- Deckenbrock, in: BeckOK BRAO, 23. Ed. (Stand 01.03.2025), § 43a Rn. 15 — Aufklärungspflicht; Inhalt und Grenzen bei studentischen Beratungsstellen.

## Ablauf

**Stattdessen verwenden:**

Für einfache Korrespondenz (Terminbestätigung, Unterlagenbitte, Eingangsbestätigung):
```
/mandantenbrief terminbestaetigung
/mandantenbrief unterlagenbitte
/mandantenbrief eingangsbestaetigung
```

Für inhaltliche Statusmitteilungen:
```
/status mandant
```

Vollständiger Ablauf in den jeweiligen SKILL.md-Dateien:

1. Zielgruppe festlegen (Bildungshintergrund, Sprache, besondere Umstände des Mandanten)
2. Verständlichkeitsstandards der Klinik anwenden (Klinik-Konfiguration → plain-language-standard)
3. Kein Fachjargon ohne Erläuterung; kurze Sätze; konkrete Handlungsanweisungen
4. Supervisoren-Routing nach § 6 Abs. 2 RDG vor Versand

## Ausgabeformat

Keine Ausgabe — diese Skill ist inaktiv. Weiterleitung auf `/mandantenbrief [typ]` oder `/status mandant`.

## Beispiel

Statt `/einfache-sprache-briefe`:

```
/status mandant
```

Dieser Befehl erstellt ein verständliches Statusschreiben (Zielgruppe: Mandant/-in) nach dem Hauptschulniveau-Standard, ohne Fachjargon, mit konkreten nächsten Schritten: „Was ist passiert / Was passiert als nächstes / Was müssen Sie tun / So erreichen Sie uns."

Oder für Routine-Korrespondenz:
```
/mandantenbrief terminbestaetigung
```

Ergebnis: Eine klare Terminbestätigung mit Ort, Zeit, Mitnahme-Unterlagen und Kontaktdaten — ohne juristische Formulierungen.

## Risiken und typische Fehler

- **Verweis auf diese Skill in älteren Materialien:** Semesterskripte und Tutorenmaterialien auf die neuen Skills umschreiben.
- **Verständlichkeitsstandards als optional behandeln:** Die Pflicht zur verständlichen Mandantenkommunikation ergibt sich aus § 43a BRAO und BGH-Rspr. Sie gilt auch für Studierende in der Beratungsstelle unter Supervisorenaufsicht.
- **Fachbegriffe ohne Erläuterung:** Begriffe wie „Widerspruchsfrist", „Vollstreckungstitel" oder „Klagefrist" sind für viele Mandanten unverständlich. Immer in Klammern oder mit einfachem Folgesatz erläutern.
- **Versand ohne Supervisoren-Freigabe:** Kein Mandantenbrief verlässt die Beratungsstelle ohne Freigabe, auch keine kurze Terminbestätigung.

## Quellenpflicht

Nicht anwendbar (Weiterleitungs-Skill). Für alle Quellenangaben zu Mandantenbriefen: `skills/status/SKILL.md`, Sektion „Quellenpflicht", und `skills/mandantenbrief/SKILL.md`.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
