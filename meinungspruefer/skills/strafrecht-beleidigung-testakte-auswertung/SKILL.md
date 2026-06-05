---
name: strafrecht-beleidigung-testakte-auswertung
description: "Strafrecht Beleidigung Testakte Auswertung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strafrecht Beleidigung Testakte Auswertung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Strafrecht Beleidigung Testakte Auswertung** im Plugin Meinungsfreiheit/Persönlichkeitsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafrecht-185-beleidigung` | Prüft § 185 StGB bei ehrverletzenden Werturteilen und Schimpfworten mit Art 5 GG. Zwingt Sinnermittlung, Kontext, Sachbezug, Formalbeleidigung, Schmähkritik, Menschenwürde und Normalabwägung. |
| `testakte-auswertung` | Wertet die Testakte meinungspruefer-grenzfaelle-alltag aus. Sortiert X, LinkedIn, Kantine, Schule, Arbeitgeber, Bürgermeister, Lackaffe, Pinocchio und Tatsachenbelege in getrennte Prüfstränge. |

## Arbeitsweg

Im Plugin Meinungsfreiheit/Persönlichkeitsrecht gilt für **Strafrecht Beleidigung Testakte Auswertung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafrecht-185-beleidigung`

**Fokus:** Prüft § 185 StGB bei ehrverletzenden Werturteilen und Schimpfworten mit Art 5 GG. Zwingt Sinnermittlung, Kontext, Sachbezug, Formalbeleidigung, Schmähkritik, Menschenwürde und Normalabwägung.

# § 185 StGB - Beleidigung

## Prüfprogramm

1. **Äußerung und Adressat:** Ist eine individualisierbare Person betroffen?
2. **Kundgabe:** Gegenüber Betroffenem oder Dritten?
3. **Missachtung/Nichtachtung:** Liegt eine herabsetzende Bewertung vor?
4. **Sinnermittlung:** Wortlaut, Kontext, Begleitumstände, Publikum.
5. **Schutzbereich Art. 5 GG:** Auch polemische und verletzende Werturteile sind zunächst geschützt.
6. **Ausnahmen:** Menschenwürdeangriff, Formalbeleidigung, Schmähung.
7. **Normalfall:** grundrechtlich angeleitete Abwägung.
8. **§ 193 StGB:** Wahrnehmung berechtigter Interessen.
9. **Strafantrag:** § 194 StGB prüfen.

## Abwägungsfaktoren

Pro Meinungsfreiheit:

- Sachbezug.
- Beitrag zu öffentlicher oder betrieblicher Debatte.
- Machtkritik gegen Amtsträger oder Institutionen.
- Kampf ums Recht, Beschwerde, Verteidigung eigener Interessen.
- spontane Erregung, begrenzter Empfängerkreis.

Pro Ehrschutz:

- reine Herabsetzung ohne Sachkern.
- Vorbedacht, Wiederholung, Prangerwirkung.
- große Reichweite, Bildnutzung, Tagging.
- Angriff auf berufliche Integrität ohne Beleg.
- verletzliche private Situation.

## Typische Ausgabe

Schreibe nie nur "Beleidigung ja/nein". Gib:

- Tatbestandliche Einordnung.
- Verfassungsrechtliche Korrektur.
- stärkstes Argument pro Zulässigkeit.
- stärkstes Argument pro Strafbarkeit.
- Ergebnis mit Ampel.
- sicherere Alternativformulierung, wenn der Nutzer vor Veröffentlichung fragt.

## Spezialfälle

Für "Lackaffe" nutze `schimpfwort-lackaffe-und-spott`.

Für "Pinocchio" nutze `satire-ironisierung-pinocchio`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `testakte-auswertung`

**Fokus:** Wertet die Testakte meinungspruefer-grenzfaelle-alltag aus. Sortiert X, LinkedIn, Kantine, Schule, Arbeitgeber, Bürgermeister, Lackaffe, Pinocchio und Tatsachenbelege in getrennte Prüfstränge.

# Testakte auswerten

## Ziel

Dieses Fachmodul greift, wenn die Arbeitsakte `meinungspruefer-grenzfaelle-alltag` hochgeladen oder genannt wird. Die Akte enthält mehrere kleine, unordentliche Äußerungsfälle. Sie soll nicht mit einer Erwartungshorizont erschlagen werden, sondern in Arbeitsstränge zerlegt werden.

## Vorgehen

1. Dateien inventarisieren.
2. Jede Äußerung als eigenes Äußerungsblatt erfassen.
3. Stränge bilden:
 - X-Post Bauprojekt.
 - LinkedIn Projektleitung.
 - Kantine/Arbeitgeber.
 - Schule/Elternchat.
 - Bürgermeister und "Lackaffe".
 - Pinocchio-Vergleich.
 - Tatsachenvorwurf mit Beleglücken.
4. Pro Strang passende Skills vorschlagen.
5. Eine Gesamtampel ausgeben.

## Output

- Akteninventar.
- Äußerungsliste.
- Risikocluster.
- Nächste Bearbeitungsschritte.
- Vorschlag für einen vollständigen Prüfvermerk.

## Schneller Arbeitsmodus

- Starte mit Wortlaut, Medium, Adressat, Anlass, Vor- und Nachgeschichte, Reichweite, Betroffenem und vorhandenen Belegen.
- Trenne strikt: Tatsachenbehauptung, Werturteil, gemischte Aeusserung, Satire/Spott, Schmähungs- oder Prangerkontext.
- Gewichte meinungsfreiheitsfreundlich, aber nicht blind: Sachbezug, Machtkritik, Beleglage, Formalbeleidigung, Privatbereich und Eskalationsrisiko getrennt ausweisen.
- Keine erfundene Rechtsprechung. Entscheidungen nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle nennen; sonst Recherchebedarf markieren.

## Ausgabeformat

- Ampel mit einem Satz Begruendung.
- Beste Verteidigungslinie.
- Gefaehrlichster Gegeneinwand.
- Sichere Alternativformulierung.
- Naechste Handlung: nichts tun, belegen, loeschen, klarstellen, antworten, verteidigen oder anwaltlich eskalieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
