---
name: anspruchslandkarte-bgb-aufforderungsschreiben
description: "Anspruchslandkarte BGB Aufforderungsschreiben: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anspruchslandkarte BGB Aufforderungsschreiben

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anspruchslandkarte BGB Aufforderungsschreiben** im Plugin Nachbarschaftsstreit. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anspruchslandkarte-bgb-nachbarrecht` | Anspruchslandkarte für Nachbarschaftsstreit erstellen: BGB-Eigentumsansprüche, Besitzschutz, Überbau, Überhang, Immissionen, Notweg, Landesnachbarrecht, öffentliches Recht, Beweise, Einwendungen und Rechtsfolge trennen. |
| `aufforderungsschreiben-nachbar` | Aufforderungsschreiben im Nachbarschaftsstreit erstellen: sachlich, beweisstark, fristgebunden, deeskalierend oder druckvoll; für Überbau, Überhang, Einfriedung, Immission, Notweg, Baugrube und Duldung. |
| `beweissicherung-ortstermin-fotos` | Beweissicherung im Nachbarrechtsfall planen: Ortstermin, Fotodokumentation, Messpunkte, Zeugen, Vermessung, Sachverständige, Lärm-/Geruchsprotokoll, Rissmonitoring und selbständiges Beweisverfahren. |

## Arbeitsweg

Im Plugin Nachbarschaftsstreit gilt für **Anspruchslandkarte BGB Aufforderungsschreiben**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anspruchslandkarte-bgb-nachbarrecht`

**Fokus:** Anspruchslandkarte für Nachbarschaftsstreit erstellen: BGB-Eigentumsansprüche, Besitzschutz, Überbau, Überhang, Immissionen, Notweg, Landesnachbarrecht, öffentliches Recht, Beweise, Einwendungen und Rechtsfolge trennen.

# Anspruchslandkarte BGB-Nachbarrecht

## Zweck

Dieser Skill sortiert einen Nachbarschaftsstreit in Anspruchsgrundlagen, Einwendungen, Beweisfragen und Rechtsfolgen. Er ist besonders nützlich, wenn mehrere Themen durcheinanderlaufen.

## Raster

| Streit | Kernnormen | Rechtsfolge |
|---|---|---|
| Eigentumsbeeinträchtigung | § 1004 BGB, § 903 BGB | Beseitigung, Unterlassung |
| Besitzstörung | §§ 862, 858 BGB | Beseitigung, Unterlassung |
| Immissionen | § 906 BGB | Duldung, Unterlassung, Ausgleich |
| Überhang | § 910 BGB | Selbsthilferecht nach Frist, Grenzen |
| Überbau | §§ 912-916 BGB | Duldung oder Beseitigung, Überbaurente, Abkauf |
| Vertiefung | § 909 BGB | Unterlassung, Sicherung, Schaden |
| Gefahranlage/Einsturz | §§ 907, 908 BGB | Sicherung/Beseitigung |
| Notweg | §§ 917, 918 BGB | Duldung gegen Rente |
| Grenze/Grenzanlage | §§ 919-923 BGB | Abmarkung, Nutzung, Unterhaltung |
| Landesnachbarrecht | Landesrecht | Einfriedung, Grenzabstände, Hammerschlag |

## Ausgabe

Gib eine Tabelle:

| Anspruchsteller | Gegner | Tatsache | Anspruch | Einwendung | Beweis | nächster Schritt |

## Prüfhinweise

- § 1004 BGB ist kein Freifahrtschein: Duldungspflichten aus § 906, § 912, Landesrecht, Dienstbarkeit oder Vertrag prüfen.
- Bei Bäumen immer Bundesrecht, Landesrecht, kommunale Satzung und Naturschutz trennen.
- Öffentlich-rechtliche Genehmigung bedeutet nicht automatisch privatrechtliche Zulässigkeit.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `aufforderungsschreiben-nachbar`

**Fokus:** Aufforderungsschreiben im Nachbarschaftsstreit erstellen: sachlich, beweisstark, fristgebunden, deeskalierend oder druckvoll; für Überbau, Überhang, Einfriedung, Immission, Notweg, Baugrube und Duldung.

# Aufforderungsschreiben an den Nachbarn

## Zweck

Dieser Skill schreibt nicht beleidigt, sondern wirksam. Das Schreiben soll später vor Gericht gut aussehen und trotzdem eine Einigung ermöglichen.

## Aufbau

1. Betreff mit Grundstück und Streitgegenstand.
2. Kurze Tatsachenchronologie.
3. Konkrete Beeinträchtigung.
4. Rechtsgrundlage mit knapper Einordnung.
5. Aufforderung.
6. Frist.
7. Beweissicherung und Zutritts-/Terminangebot.
8. Rechtsfolgen bei Fristablauf.
9. Vergleichsfenster.

## Tonmodi

- **Nachbarschaftsfrieden:** klar, freundlich, lösungsorientiert.
- **Letzte außergerichtliche Frist:** knapp, bestimmt, beweissicher.
- **Akute Gefahr:** sofortige Sicherung, kurze Frist, Behörden-/Eilrechtsschutzvorbehalt.

## Qualitätsregel

Keine Drohkulisse ohne Tatsachen. Keine strafrechtlichen Vorwürfe ohne belastbare Grundlage. Keine Frist setzen, die praktisch unmöglich ist, außer bei akuter Gefahr.

## Schneller Arbeitsmodus

- Frage zuerst nach Bundesland, Grundstuecksgrenze, Lageplan/Vermessung, Fotos, Datum, Beteiligten und bisheriger Eskalation.
- Sortiere den Konflikt in getrennte Stränge: Grenze/Überbau, Pflanzen/Überhang, Immissionen, Bau/Vertiefung, Zugang/Notweg, Gefahr, Vergleich.
- Behandle Chatnachrichten und Fotos als Beweisansatz, nicht als feststehende Tatsache. Markiere, was gemessen, besichtigt oder sachverstaendig geklaert werden muss.
- Priorisiere befriedende Loesungen, aber sichere Fristen, Besitzschutz und Eilrechtsschutz sichtbar ab.

## Ausgabeformat

- Streitstrang mit Anspruchsrichtung.
- Benötigte Beweise.
- Risiko fuer Mandant und Gegenseite.
- Deeskalierender naechster Schritt.
- Gerichtlicher naechster Schritt, falls Vergleich scheitert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `beweissicherung-ortstermin-fotos`

**Fokus:** Beweissicherung im Nachbarrechtsfall planen: Ortstermin, Fotodokumentation, Messpunkte, Zeugen, Vermessung, Sachverständige, Lärm-/Geruchsprotokoll, Rissmonitoring und selbständiges Beweisverfahren.

# Beweissicherung, Ortstermin und Fotos

## Zweck

Dieser Skill macht Beweise gerichtstauglicher. Nachbarrechtsfälle verlieren oft nicht am Recht, sondern am schlechten Foto aus schrägem Winkel ohne Datum.

## Fotoplan

- Übersichtsfoto je Grundstück.
- Grenzverlauf mit erkennbaren Bezugspunkten.
- Detailfoto der Beeinträchtigung.
- Messfoto mit Maßstab.
- Blickrichtung notieren.
- Datum, Uhrzeit, Standort, Fotograf.
- Keine heimlichen Aufnahmen in höchstpersönlichen Bereichen.

## Spezialbeweise

| Thema | Beweis |
|---|---|
| Überbau | Vermessung, Lageplan, Bauakte, Fotos |
| Überhang | Fotos, Beeinträchtigung, Fristsetzung |
| Wurzeln | Pflasterhebung, Leitungsbefund, Gutachten |
| Immission | Protokoll, Zeugen, Messung |
| Baugrube | Rissmonitoring, Sachverständige, Bauamt |
| Notweg | Karten, Zufahrt, Nutzungshistorie |

## Output

- Beweisverzeichnis.
- Ortstermin-Checkliste.
- Fototabelle.
- Vorschlag selbständiges Beweisverfahren, wenn Zustand verloren gehen kann.

## Schneller Arbeitsmodus

- Frage zuerst nach Bundesland, Grundstuecksgrenze, Lageplan/Vermessung, Fotos, Datum, Beteiligten und bisheriger Eskalation.
- Sortiere den Konflikt in getrennte Stränge: Grenze/Überbau, Pflanzen/Überhang, Immissionen, Bau/Vertiefung, Zugang/Notweg, Gefahr, Vergleich.
- Behandle Chatnachrichten und Fotos als Beweisansatz, nicht als feststehende Tatsache. Markiere, was gemessen, besichtigt oder sachverstaendig geklaert werden muss.
- Priorisiere befriedende Loesungen, aber sichere Fristen, Besitzschutz und Eilrechtsschutz sichtbar ab.

## Ausgabeformat

- Streitstrang mit Anspruchsrichtung.
- Benötigte Beweise.
- Risiko fuer Mandant und Gegenseite.
- Deeskalierender naechster Schritt.
- Gerichtlicher naechster Schritt, falls Vergleich scheitert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
