---
name: kanzleitag-simulation-kanzlei
description: "Kanzleitag Simulation Kanzlei: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kanzleitag Simulation Kanzlei

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Kanzleitag Simulation Kanzlei** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-kanzleitag-simulation` | Führt im Simulationsmodus durch einen achtstuendigen Kanzleitag für Training und Demo. Anwendungsfall Kanzlei will Arbeitsablaeufe testen neue Mitarbeiter einarbeiten oder Plugin-vorhalten. Abdeckt Mandatsannahme GwG Postlauf beA E-Mail Schreibcanvas Fristen Zeitnarrative Rechnung UStVA Eingangsrechnungen und Tagesabschluss. Output Simulationsprotokoll mit Tagesereignissen Fehlerliste Lernhinweisen und Leistungsbewertung. Abgrenzung zu kanzlei-allgemein-automationen (Echtbetrieb) und kanzlei-allgemein-kaltstart. |
| `kanzlei-allgemein-kommandocenter` | Schnellstart und Command Center für Kanzlei-Allgemein-Plugin. Erkennt aus einem Satz den passenden Kanzlei-Workflow, routet zu Mandatsannahme GwG Klage Replik Vertrag Rechtsprechung beA Fristen Rechnung Buchhaltung HR UStVA oder Simulation, stellt nur die nötigsten Rückfragen und erzeugt eine Freigabeampel. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Kanzleitag Simulation Kanzlei**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-kanzleitag-simulation`

**Fokus:** Führt im Simulationsmodus durch einen achtstuendigen Kanzleitag für Training und Demo. Anwendungsfall Kanzlei will Arbeitsablaeufe testen neue Mitarbeiter einarbeiten oder Plugin-vorhalten. Abdeckt Mandatsannahme GwG Postlauf beA E-Mail Schreibcanvas Fristen Zeitnarrative Rechnung UStVA Eingangsrechnungen und Tagesabschluss. Output Simulationsprotokoll mit Tagesereignissen Fehlerliste Lernhinweisen und Leistungsbewertung. Abgrenzung zu kanzlei-allgemein-automationen (Echtbetrieb) und kanzlei-allgemein-kaltstart.

# Kanzleitag-Simulation


## Triage zu Beginn
1. Soll die Simulation in Echtzeit oder beschleunigt ablaufen?
2. Welche Integrationen sind echt vorhanden (beA, E-Mail, DMS) und welche werden simuliert?
3. Welche Testakten und Mandanten sollen in der Simulation vorkommen?
4. Dient die Simulation Training, Onboarding, Demo oder Qualitaetssicherung?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch im Simulationsmodus; keine echten Mandatsdaten ohne Anonymisierung
- Art. 32 DSGVO — TOM: Sicherheitsstandards gelten auch fuer Trainingsumgebungen
- § 43 BRAO — Fortbildungspflicht des Anwalts: Simulation als anerkanntes Fortbildungsmittel
- § 26 BDSG — Beschaeftigtendatenschutz: gilt auch bei internem Onboarding mit Simulationsdaten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt durch einen realistisch wirkenden Kanzleitag, ohne echte Systeme zu benötigen. Er eignet sich für Training, Demo, Testakte und Onboarding junger Anwältinnen und Anwälte.

## Startfragen

1. Echtzeit oder beschleunigt?
2. Welche Integrationen sind echt angeschlossen?
3. Welche Integrationen sollen simuliert werden?
4. Welche Akten sollen vorkommen?
5. Soll der freundliche Copilot aktiv Hinweise geben?
6. Soll nach jeder Station angehalten oder automatisch weitergeführt werden?

## Acht-Stunden-Ablauf

```text
09:00 Tagesstart, offene Fristen, Kalender, Integrationen
10:00 Intake aus E-Mail, Messenger, Fax oder Screenshot
11:00 Postlauf mit beA-Journal, EB-Prüfung, ZIP-Archiv
12:00 Schreib-Canvas für Schriftsatz oder Mandantenbrief
13:00 Zeitnarrative und kurze Pause
14:00 Neue Mandatsanfrage: Konfliktcheck, GwG, KYC, PEP, Kontoblatt, Vorschuss
15:00 Eingangsrechnungen, Betriebsausgaben, UStVA-Vorbereitung, ELSTER-Fallback
16:00 HR, Urlaub, Krankheit, Kanzleikalender und Payroll-Vorbereitung
17:00 Rechnung, E-Rechnung oder Mandatsvereinbarung vorbereiten
17:30 Versandcheck, beA/Fax/E-Mail simulieren oder echt vorbereiten
18:00 Tagesabschluss, Fristen, offene Fragen, Zeit, Rechnung und Personal
```

## Tempo

Im beschleunigten Modus kann eine Stunde als fünf bis zehn Minuten simuliert werden. Vor risikoreichen Handlungen immer anhalten:

- Fristübernahme.
- EB-Abgabe.
- beA-Versand.
- Rechnung finalisieren.
- Mandat annehmen.
- Ausweisdokumente auslesen oder ablegen.
- Verdachtsmeldung oder Unstimmigkeitsmeldung vorbereiten.
- E-Rechnung validieren.
- UStVA übermitteln.
- Lohnabrechnung, SV-Meldung oder Lohnsteuer-Anmeldung übermitteln.
- Krankheitsdaten oder Personalakte ausgeben.

Wenn ELSTER oder Buchhaltung nicht angeschlossen ist, an `kanzlei-allgemein-ustva-simulation` übergeben und zwischen ELSTER-Online-Simulation, manuellem Eingabebogen, XML-Upload-Prüfung und Steuerberater-Paket wählen lassen.

Wenn Kalender, HR- oder Lohnsoftware nicht angeschlossen ist, an `kanzlei-allgemein-kanzleikalender`, `kanzlei-allgemein-hr-personal`, `kanzlei-allgemein-abwesenheiten-urlaub` und `kanzlei-allgemein-lohn-sv` übergeben und ausdrücklich als Simulation markieren.

Wenn Mandatsannahme oder GwG nicht echt angebunden ist, an `kanzlei-allgemein-mandatsannahme-gwg` übergeben und Ausweis-, Register-, PEP-, Mittelherkunfts- und Kontoblattprüfungen als Simulation markieren.

## Ausgabe

`assets/templates/kanzleitag-simulation.md` verwenden.

## 2. `kanzlei-allgemein-kommandocenter`

**Fokus:** Schnellstart und Command Center für Kanzlei-Allgemein-Plugin. Erkennt aus einem Satz den passenden Kanzlei-Workflow, routet zu Mandatsannahme GwG Klage Replik Vertrag Rechtsprechung beA Fristen Rechnung Buchhaltung HR UStVA oder Simulation, stellt nur die nötigsten Rückfragen und erzeugt eine Freigabeampel.

# Kommandocenter

## Zweck

Dieser Skill ist die schnelle Oberfläche des Plugins. Er verhindert, dass Nutzer erst wissen müssen, welcher Fachmodul passt. Aus einem Satz, einer Datei oder einem chaotischen Eingang entsteht eine klare Arbeitskarte mit nächstem Schritt, passenden Skills und Freigabeampel.

## Grundregel

Erst Tempo, dann Tiefe:

1. Ziel erkennen.
2. Risiko erkennen.
3. maximal drei Rückfragen stellen.
4. sofort eine Arbeitskarte erzeugen.
5. `kanzlei-allgemein-look-and-feel` anwenden, wenn eine sichtbare Dashboard-, Status- oder Startausgabe entsteht.
6. an den passenden Fachmodul übergeben.

Nicht alle Checklisten auf einmal öffnen. Nur die Checkliste verwenden, die den nächsten Arbeitsschritt wirklich freischaltet.

## Schnellbefehle

| Nutzer sagt | Route |
| --- | --- |
| `Neue Sache` | Intake, Akte, Mandatsannahme/GwG, Aktenzeichen, Kontoblatt |
| `Mach Klage` | Schriftsatz-Turbo, Anlagen, Rechtsprechung, Qualitätsgate, Versand |
| `Mach Replik` | Replikmatrix, Anlagen, Rechtsprechung, Qualitätsgate, Versand |
| `Mach Vertrag` | Vertragsentwurf, Handelsregister, Datenschutz, Qualitätsgate |
| `Post machen` | Postlauf, beA-Journal, Fristen, EB, Aktenablage |
| `Rechnung machen` | Zeitnarrative, Rechnung, E-Rechnung, GoBD, offene Posten |
| `GwG prüfen` | Mandatsannahme/GwG, KYC, PEP, wirtschaftlich Berechtigte, Verdachtslogik |
| `Recherche machen` | Rechtsprechungsrecherche, Fundstellenregister, Verwertungsnotiz |
| `Kanzleitag simulieren` | Integrationen, Simulation, Kalender, Postlauf, Mandatsannahme, Output |
| `Was ist offen?` | Fristen, Action-Items, Rechnungen, GwG-Reminder, Post, HR, UStVA |

## Freigabeampel

Immer eine Ampel ausgeben:

- `GRÜN`: Weiterarbeiten möglich. Keine bekannte Stoppschwelle.
- `GELB`: Nutzbarer Entwurf, aber offene Punkte.
- `ROT`: Nicht versenden, nicht annehmen, nicht buchen oder nicht melden, bevor ein Mensch freigibt.

Typische rote Schwellen:

- Frist unklar.
- beA-Versand oder EB ohne Einzelbestätigung.
- Mandatsannahme ohne Konfliktcheck oder GwG-Status.
- Verdachtsfall, PEP-/Hochrisiko- oder Mittelherkunftsproblem ungeklärt.
- Rechnung ohne Freigabe oder E-Rechnungsvalidierung.
- Rechtsprechung nicht verifiziert.
- Handelsregister, Partei oder Vertretung ungeprüft.

## Arbeitskarte

Immer mit dieser Struktur starten:

```markdown
# Kanzlei-Allgemein-Plugin

## Kommandocenter

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
| | | | |

## Jetzt

1.
2.
3.
```

## Anfängerfreundlichkeit

- Fachworte kurz übersetzen.
- Nicht mit 20 Fragen beginnen.
- Fehlendes als `TODO` markieren.
- Unsichere Nutzer mit einem konkreten Vorschlag führen.
- Bei Profis knapper werden und direkt an die Fachmodule übergeben.

## Übergabe

- Neue Sache oder Dokumenteneingang: `kanzlei-allgemein-intake`, danach `kanzlei-allgemein-akte` und bei Bedarf `kanzlei-allgemein-mandatsannahme-gwg`.
- Klage/Replik/Antrag: `kanzlei-allgemein-schriftsatz-turbo`, `kanzlei-allgemein-rechtsprechungsrecherche`, `kanzlei-allgemein-qualitaetsgate-hardening`.
- Vertrag: `kanzlei-allgemein-vertragsentwurf`, `kanzlei-allgemein-handelsregisterabruf`, `kanzlei-allgemein-qualitaetsgate-hardening`.
- beA/Post: `kanzlei-allgemein-postlauf`, `kanzlei-allgemein-bea-journal`, `kanzlei-allgemein-fristen-monitor`.
- Rechnung/Buchhaltung: `kanzlei-allgemein-zeitnarrative`, `kanzlei-allgemein-rechnung`, `kanzlei-allgemein-erechnung`, `kanzlei-allgemein-buchhaltung-konten`.
- Kanzleibetrieb: `kanzlei-allgemein-kanzleikalender`, `kanzlei-allgemein-automationen`, HR-/Payroll-Skills.

## Ausgabe

- `assets/templates/workflow-kommandocenter.md`
- `assets/templates/workflow-schnellstartkarte.md`
- `assets/templates/workflow-freigabeampel.md`
- optional `assets/templates/workflow-naechste-beste-aktion.md`
- für hochwertige Cowork-Ausgaben zusätzlich `assets/templates/cowork-dashboard.md`, `assets/templates/cowork-statuskarte.md` und `assets/templates/cowork-freigabekarte.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
