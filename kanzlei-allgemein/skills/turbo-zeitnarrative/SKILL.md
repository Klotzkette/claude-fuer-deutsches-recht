---
name: turbo-zeitnarrative
description: "Kanzlei Allgemein Schriftsatz Turbo, Kanzlei Allgemein Zeitnarrative: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Kanzlei Allgemein Schriftsatz Turbo, Kanzlei Allgemein Zeitnarrative

## Arbeitsbereich

Dieser Skill bündelt **Kanzlei Allgemein Schriftsatz Turbo, Kanzlei Allgemein Zeitnarrative** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `kanzlei-allgemein-schriftsatz-turbo` | Erstellt schnell Klage Replik Antrag Klageerwiderung oder Schriftsatzantwort mit Anlagenlogik. Anwendungsfall Frist laeuft und Schriftsatz muss schnell mit allen Pflichtbestandteilen erstellt werden. Normen § 253 ZPO Klageschrift § 276 ZPO Klageerwiderung § 130a ZPO beA-Einreichung. Prüfraster Antrag Sachverhalt Beweise Recht Fristen Zuständigkeit beA-Versand. Output Fertig strukturierter Schriftsatz mit Antrag Begründung Beweisangeboten Anlagenverzeichnis und Qualitaetsgate-Hinweis. Abgrenzung zu kanzlei-allgemein-schreibcanvas (freies Canvas) und kanzlei-allgemein-qualitaetsgate-hardening. |
| `kanzlei-allgemein-zeitnarrative` | Zeiterfassung mit abrechenbaren Narrativen für Kanzlei-Mandate. Anwendungsfall Anwalt hat Tätigkeit ausgeubt und will Zeit mit praezisem Narrativ erfassen für spaetere Rechnungsstellung. Normen § 10 RVG Pflichtangaben Narrative GoBD-Zeitstempel. Prüfraster Akte Dauer Takt 6-Minuten-Bloecke Bearbeiter Tätigkeit Honorargrundlage Abrechenbarkeit Datenschutzreduktion. Output Zeiterfassungsprotokoll mit Narrativ Abrechenbarkeit und Rechnungsvorbereitungsnotiz. Abgrenzung zu timesheet-aktenzeitung (Gesamtzeittabelle) und kanzlei-allgemein-rechnung. |

## Arbeitsweg

Für **Kanzlei Allgemein Schriftsatz Turbo, Kanzlei Allgemein Zeitnarrative** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `kanzlei-allgemein` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `kanzlei-allgemein-schriftsatz-turbo`

**Fokus:** Erstellt schnell Klage Replik Antrag Klageerwiderung oder Schriftsatzantwort mit Anlagenlogik. Anwendungsfall Frist laeuft und Schriftsatz muss schnell mit allen Pflichtbestandteilen erstellt werden. Normen § 253 ZPO Klageschrift § 276 ZPO Klageerwiderung § 130a ZPO beA-Einreichung. Prüfraster Antrag Sachverhalt Beweise Recht Fristen Zuständigkeit beA-Versand. Output Fertig strukturierter Schriftsatz mit Antrag Begründung Beweisangeboten Anlagenverzeichnis und Qualitaetsgate-Hinweis. Abgrenzung zu kanzlei-allgemein-schreibcanvas (freies Canvas) und kanzlei-allgemein-qualitaetsgate-hardening.

# Schriftsatz-Turbo: Klage, Replik, Antrag


## Triage zu Beginn
1. Welcher Schriftsatztyp wird benoetigt: Klage, Replik, Klageerwiderung, Antrag auf einstweiligen Rechtsschutz?
2. Welches Gericht ist zustaendig (oertlich, sachlich, instanziell) und welche Verfahrensordnung gilt?
3. Welche Frist laeuft und wann ist spaetester Einreichungstermin?
4. Sind alle Beweisangebote und Anlagen vorhanden und vorbereitet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 253 ZPO — Klageschrift: Formerfordernis und Antragspflicht
- § 12 GVG — Sachliche Zustaendigkeit des AG (bis 10.000 EUR ab 01.01.2026 — Grenze angehoben)
- § 13 GVG — Sachliche Zustaendigkeit des LG (ab 10.000 EUR ab 01.01.2026)
- §§ 935-945 ZPO — Einstweiliger Rechtsschutz: Verfuegungsgrund und Verfuegungsanspruch

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bringt aus ungeordneten Informationen schnell einen gerichtsfähigen Entwurf: Klage, Replik, Antrag, Klageerwiderung, Schriftsatzantwort, einstweiliger Antrag oder Mandantenentwurf. Er priorisiert Nutzbarkeit: erst Struktur und Pflichtteile, dann Verfeinerung.

## Schnellstart

Wenn wenig Zeit ist, fragen:

1. Wer ist Gericht oder Gegner?
2. Was soll das Gericht entscheiden?
3. Welche Frist läuft?
4. Welche Tatsachen sind sicher?
5. Welche Beweise oder Anlagen gibt es?
6. Was ist der dringendste Antrag?

Danach sofort ein Gerüst erzeugen, auch wenn Details offen sind.

## Produktionspfade

### Klage in 20 Minuten

1. Rubrum aus Akte, Registerabruf oder Mandatsblatt vorbereiten.
2. Antrag als Arbeitsfassung formulieren.
3. Anspruchsgrundlage wählen und hilfsweise Alternativen markieren.
4. Chronologie aus Quellen bauen.
5. Anlagen automatisch durchnummerieren.
6. Rechtsprechungsbedarf markieren und bei streitigen Rechtsfragen `kanzlei-allgemein-rechtsprechungsrecherche` anstoßen.
7. Fehlende Beweise als TODO im Text markieren.
8. Qualitätsgate `Schnellcheck` ausführen.

### Replik in 20 Minuten

1. Klageerwiderung oder Gegenschreiben in einzelne Behauptungen zerlegen.
2. Jede Behauptung als `zugestanden`, `bestritten`, `unerheblich`, `neu`, `verspätet` oder `klärungsbedürftig` einordnen.
3. Substantiierte Antwort mit Quelle und Beweis bauen.
4. Rechtsprechung zu streitentscheidenden Rechtsfragen gezielt nachziehen und Fundstellen im Register ablegen.
5. Pauschales Bestreiten vermeiden.
6. Am Ende nur die wirklich nötigen Anträge wiederholen oder anpassen.

### Antrag oder Eilsache

1. Eilbedürftigkeit und Frist zuerst klären.
2. Glaubhaftmachungsmittel vorziehen.
3. Sachverhalt knapp, aber datiert darstellen.
4. Risiken der Zuständigkeit und des Rechtsschutzbedürfnisses markieren.

## Schriftsatz-Bausteine

1. Rubrum oder Beteiligte.
2. Aktenzeichen und Betreff.
3. Antrag.
4. Kurzüberblick.
5. Sachverhalt chronologisch mit Quellen.
6. Rechtliche Würdigung.
7. Beweisangebote oder Glaubhaftmachung.
8. Anlagenverzeichnis.
9. Frist- und Zustellhinweise.
10. Kosten- und Streitwertnotiz.
11. Signatur und Versandcheck.

## Replik-Modus

Bei Replik:

- Gegenseitigen Vortrag in Streitpunkte zerlegen.
- Zugestanden, bestritten, unerheblich, neu, verspätet markieren.
- Pro Streitpunkt Tatsachen, Beweis, Recht und Antrag ergänzen.
- Keine pauschalen Bestreitenssätze ohne Substanz stehen lassen.

## Anfängerführung

Wenn der Nutzer nur Stichworte gibt:

- Aus Stichworten eine Chronologie erzeugen.
- Fehlende Pflichtdaten als TODO in eckigen Klammern markieren.
- Nur die wichtigsten Rückfragen stellen: Gericht, Antrag, Frist.
- Einen Rohentwurf liefern, der sichtbar unfertige Stellen enthält, statt zu blockieren.

## Profi-Härtung

Wenn genug Material vorhanden ist:

- Anspruchsgrundlagen in Haupt- und Hilfsvortrag ordnen.
- Vortrag nach Darlegungs- und Beweislast strukturieren.
- Einwendungen der Gegenseite antizipieren.
- Rechtsprechungs- oder Zitierbedarf markieren.
- Amtliche Rechtsprechungsfundstellen über `kanzlei-allgemein-rechtsprechungsrecherche` verifizieren.
- Anlagenreihenfolge so wählen, dass das Gericht die Chronologie ohne Suche nachvollziehen kann.

## Anlagenlogik

Jede Anlage braucht:

- Anlagenkürzel.
- Dateiname.
- Quelle.
- Beweisthema.
- Fundstelle im Schriftsatz.
- Datenschutzcheck.
- beA-PDF-Check.

Bei Anlagen immer prüfen:

- Ist die Anlage im Text wirklich verwendet?
- Ist das Beweisthema konkret genug?
- Sind personenbezogene Daten Dritter geschwärzt?
- Ist die Datei lesbar, nicht beschädigt und passend benannt?
- Gibt es Screenshots oder Videos, die in ein gerichtstaugliches Protokoll übersetzt werden müssen?

## Qualitätsgate

Vor Ausgabe immer `kanzlei-allgemein-qualitaetsgate-hardening` ausführen. Vor Versand zusätzlich `kanzlei-allgemein-output-versand`.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Schriftsatz schnell erstellen Turbo-| Schriftsatz nach Turbo-Schema; Template unten |
| Variante A — Schriftsatz sehr komplex mehrere Rechtsgebiete | Fachanwalt-Skill separat einsetzen; Turbo nur als Strukturhilfe |
| Variante B — Mandant will nur Entwurf keine Fertigstellung | Entwurfs-Version ohne finale Formulierung |
| Variante C — Frist droht in 2 Stunden | Kernantraege sofort; Begruendung nachreichen wenn Frist es erlaubt |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Ausgabe

- `assets/templates/schriftsatz-turbo-geruest.md`.
- `assets/templates/rechtsprechungsfundstellen-register.md`, wenn Rechtsprechung gesucht wurde.
- `assets/templates/klage-replik-pruefmatrix.md`.
- `assets/templates/anlagenverzeichnis-schriftsatz.md`.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 2. `kanzlei-allgemein-zeitnarrative`

**Fokus:** Zeiterfassung mit abrechenbaren Narrativen für Kanzlei-Mandate. Anwendungsfall Anwalt hat Tätigkeit ausgeubt und will Zeit mit praezisem Narrativ erfassen für spaetere Rechnungsstellung. Normen § 10 RVG Pflichtangaben Narrative GoBD-Zeitstempel. Prüfraster Akte Dauer Takt 6-Minuten-Bloecke Bearbeiter Tätigkeit Honorargrundlage Abrechenbarkeit Datenschutzreduktion. Output Zeiterfassungsprotokoll mit Narrativ Abrechenbarkeit und Rechnungsvorbereitungsnotiz. Abgrenzung zu timesheet-aktenzeitung (Gesamtzeittabelle) und kanzlei-allgemein-rechnung.

# Zeitnarrative und Timesheet


## Triage zu Beginn
1. Fuer welche Akte und welchen Bearbeiter soll der Zeiteintrag erfasst werden?
2. Ist die Taetigkeit nach RVG oder nach Stundensatz abrechenbar — oder intern (nicht abrechenbar)?
3. Gibt es eine genaue Zeitangabe oder soll die Dauer aus dem Workflow-Verlauf geschaetzt werden?
4. Soll der Eintrag sofort in die Rechnung oder erst in das interne Timesheet?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 10 RVG — Pflichtangaben auf der Rechnung: Taetigkeitsnachweis als Faelligkeitsvoraussetzung
- § 3a RVG — Honorarvereinbarung: Stundensatz-Abrechnung und Dokumentationspflicht
- § 147 AO — Aufbewahrungspflicht: Zeiterfassungsbelege 10 Jahre
- § 238 HGB — Buchfuehrungspflicht: Zeitnarrative als Teil der betrieblichen Aufzeichnungen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill macht aus Arbeitsschritten abrechenbare oder interne Zeitnarrative. Er fragt nach, welcher Akte die Tätigkeit zugeordnet werden soll, und erzeugt klare Zeiteinträge, die später in Rechnung, E-Rechnung, Prüfprotokoll oder interne Controlling-Auswertung übernommen werden können.

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

## Automationshinweis

Wenn Automationen verfügbar sind, nach Zustimmung stündliche Erinnerung vorschlagen. Keine stille Dauerüberwachung.
