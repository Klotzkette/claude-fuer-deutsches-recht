---
name: ueberbau-ueberhang-aeste-mediation
description: "Ueberbau Ueberhang Aeste Mediation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ueberbau Ueberhang Aeste Mediation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ueberbau Ueberhang Aeste Mediation** im Plugin Nachbarschaftsstreit. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ueberbau-pruefung` | Überbau nach §§ 912-916 BGB prüfen: Gebäude oder Gebäudeteil über Grenze, Vorsatz/grobe Fahrlässigkeit, Widerspruch, Duldungspflicht, Beseitigung, Überbaurente, Abkauf, Beweise und Schreiben. |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, eindringende Wurzeln, Laub, Früchte und Verschattung prüfen: § 910 BGB, Beeinträchtigung, Fristsetzung, Selbsthilfe, Beseitigungsanspruch, Baumschutzsatzung, Naturschutz und Landesnachbarrecht. |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich und Befriedung im Nachbarschaftsstreit entwerfen: Rückschnittplan, Bau-/Grenzregelung, Kostenquote, Betretensrechte, Lärmzeiten, Pflegepflichten, Vertragsstrafe, Dokumentation und Vollzug. |

## Arbeitsweg

Im Plugin Nachbarschaftsstreit gilt für **Ueberbau Ueberhang Aeste Mediation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ueberbau-pruefung`

**Fokus:** Überbau nach §§ 912-916 BGB prüfen: Gebäude oder Gebäudeteil über Grenze, Vorsatz/grobe Fahrlässigkeit, Widerspruch, Duldungspflicht, Beseitigung, Überbaurente, Abkauf, Beweise und Schreiben.

# Überbau-Prüfung

## Zweck

Dieser Skill prüft, ob ein Baukörper über die Grenze ragt und welche Rechtsfolgen daraus entstehen. Nicht jeder Grenzverstoß ist ein Überbau im Sinne von § 912 BGB; Überhang von Pflanzen gehört in `ueberhang-aeste-wurzeln`.

## Intake

- Was ragt über: Gebäude, Garage, Carport, Dämmung, Dachüberstand, Fundament, Mauer?
- Wann errichtet?
- War die Grenze bekannt, vermessen, markiert?
- Wurde vor oder sofort nach Grenzüberschreitung widersprochen?
- Liegt Vorsatz oder grobe Fahrlässigkeit nahe?
- Gibt es Baugenehmigung, Lageplan, Vermesser, Bauunternehmer?
- Welche Fläche und welcher Wert sind betroffen?

## Prüfschema

1. **Gebäude/bauliche Anlage:** § 912 BGB betrifft den Überbau bei Errichtung eines Gebäudes. Andere Anlagen können über § 1004 BGB laufen.
2. **Grenzüberschreitung:** tatsächliche Überschreitung beweisen; Vermessung erwägen.
3. **Kein Vorsatz/grobe Fahrlässigkeit:** Duldungspflicht nur, wenn dem Bauenden dies nicht zur Last fällt.
4. **Widerspruch:** Wurde vor oder sofort nach Grenzüberschreitung widersprochen?
5. **Rechtsfolge:** Duldung gegen Geldrente oder Beseitigung/Unterlassung.
6. **Rente/Abkauf:** §§ 912 Abs. 2, 913-915 BGB prüfen.

## Output

- Überbau-Vermerk.
- Beweis- und Vermessungsliste.
- Entwurf Widerspruch/Beseitigungsverlangen.
- Alternativ: Duldungs- und Rentenverhandlung.

## Fehler vermeiden

- Baugenehmigung ersetzt nicht privatrechtliche Berechtigung.
- "Schon lange so" heißt nicht automatisch rechtmäßig; Verjährung/Duldung getrennt prüfen.
- Grenzüberragende Äste sind kein Überbau.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `ueberhang-aeste-wurzeln`

**Fokus:** Überhängende Äste, eindringende Wurzeln, Laub, Früchte und Verschattung prüfen: § 910 BGB, Beeinträchtigung, Fristsetzung, Selbsthilfe, Beseitigungsanspruch, Baumschutzsatzung, Naturschutz und Landesnachbarrecht.

# Überhang, Äste und Wurzeln

## Zweck

Dieser Skill führt durch die Prüfung von herüberragenden Zweigen und eindringenden Wurzeln. Er schützt vor zwei klassischen Fehlern: zu früh selbst schneiden und zu spät Rechte sichern.

## Prüfschema § 910 BGB

1. Wurzeln oder Zweige stammen vom Nachbargrundstück.
2. Sie ragen ein oder dringen ein.
3. Sie beeinträchtigen die Grundstücksbenutzung.
4. Bei Zweigen: angemessene Frist zur Beseitigung gesetzt.
5. Frist erfolglos abgelaufen.
6. Keine Sperre durch Naturschutz, Baumschutzsatzung, Gefahr, Eigentum Dritter oder Verhältnismäßigkeit.

## Beeinträchtigung

Dokumentiere konkret:

- Dachrinne verstopft, Dach beschädigt, Fassade feucht.
- Gartenfläche nicht nutzbar, Weg unpassierbar.
- Wurzeln heben Pflaster, beschädigen Leitungen, Mauern oder Drainage.
- Erhebliche Verschattung nur mit Tatsachen und Landesrecht prüfen.

## Fristsetzung

Ein Schreiben soll enthalten:

- konkrete Pflanze,
- betroffene Grenze,
- genaue Beeinträchtigung,
- Aufforderung zum Rückschnitt/Beseitigung,
- angemessene Frist,
- Ankündigung von Selbsthilfe oder gerichtlichen Schritten,
- Hinweis auf Baumschutz/Naturschutzprüfung.

## Output

- Rückschnittvermerk.
- Fristsetzungsschreiben.
- Selbsthilfe-Risikoampel.
- Fotoplan und Beweisliste.

## Warnung

Selbsthilfe ist kein Freibrief. Unzulässiger Rückschnitt kann Schadensersatz, Besitzschutz, Naturschutz- oder Baumschutzprobleme auslösen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `vergleich-mediation-nachbarschaftsfrieden`

**Fokus:** Vergleich und Befriedung im Nachbarschaftsstreit entwerfen: Rückschnittplan, Bau-/Grenzregelung, Kostenquote, Betretensrechte, Lärmzeiten, Pflegepflichten, Vertragsstrafe, Dokumentation und Vollzug.

# Vergleich, Mediation und Nachbarschaftsfrieden

## Zweck

Dieser Skill baut Lösungen, die nicht nur juristisch, sondern alltagstauglich sind. Nachbarn bleiben meistens Nachbarn.

## Vergleichsbausteine

- genaue Grundstücke und Grenze,
- Rückschnitt/Beseitigung/Sicherung,
- Kostenquote,
- Termine,
- Zutrittsregelung,
- Schutzmaßnahmen,
- künftige Kommunikation,
- Dokumentation,
- Vertragsstrafe nur maßvoll,
- Erledigung und keine Präjudizwirkung, wenn gewünscht.

## Output

- Vergleichsentwurf.
- Gesprächsleitfaden.
- rote Linien.
- Vollzugsplan mit Datum, Verantwortlichen und Nachweisen.

## Deeskalationsregel

Frieden heißt nicht Nachgeben ohne Akte. Erst Rechte kennen, dann verhandeln.

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
