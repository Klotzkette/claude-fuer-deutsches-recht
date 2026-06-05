---
name: zivilrecht-unterlassung-abmahnung
description: "Zivilrecht Unterlassung Abmahnung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zivilrecht Unterlassung Abmahnung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Zivilrecht Unterlassung Abmahnung** im Plugin Meinungsfreiheit/Persönlichkeitsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zivilrecht-unterlassung-widerruf-schadensersatz` | Prüft zivilrechtliche Ansprüche bei Äußerungen: Unterlassung, Beseitigung, Widerruf, Richtigstellung, Geldentschädigung, § 823 BGB, § 824 BGB und § 1004 BGB analog. |
| `abmahnung-strafanzeige-reaktion` | Hilft bei Reaktion auf Abmahnung, Strafanzeige, polizeiliche Anhörung, Plattformmeldung oder Löschungsverlangen wegen einer Äußerung. Erstellt Fristencheck, Beweisplan und Verteidigungsstrategie. |

## Arbeitsweg

Im Plugin Meinungsfreiheit/Persönlichkeitsrecht gilt für **Zivilrecht Unterlassung Abmahnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zivilrecht-unterlassung-widerruf-schadensersatz`

**Fokus:** Prüft zivilrechtliche Ansprüche bei Äußerungen: Unterlassung, Beseitigung, Widerruf, Richtigstellung, Geldentschädigung, § 823 BGB, § 824 BGB und § 1004 BGB analog.

# Zivilrechtliche Äußerungsansprüche

## Anspruchslandkarte

- **Unterlassung:** Wiederholungsgefahr, rechtswidrige Verletzung des allgemeinen Persönlichkeitsrechts oder Unternehmenspersönlichkeitsrechts.
- **Beseitigung/Löschung:** fortwirkende Beeinträchtigung.
- **Widerruf/Richtigstellung:** vor allem bei unwahren Tatsachenbehauptungen.
- **Geldentschädigung:** nur bei schwerwiegenden Persönlichkeitsrechtsverletzungen.
- **§ 824 BGB:** kreditgefährdende unwahre Tatsachen über Unternehmen oder berufliches Fortkommen.
- **§ 823 Abs. 2 BGB:** Schutzgesetze wie §§ 185 ff. StGB.

## Prüfung

1. Äußerungstyp.
2. Rechtsgut.
3. Rechtswidrigkeit durch Abwägung.
4. Wiederholungs- oder Erstbegehungsgefahr.
5. Anspruchsziel.
6. Beweislast und Belege.

## Output

- mögliche Ansprüche:
- Anspruchssteller:
- Anspruchsgegner:
- stärkste Anspruchsgrundlage:
- Verteidigungsargumente:
- Entwurf für Aufforderung oder Erwiderung.

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

## 2. `abmahnung-strafanzeige-reaktion`

**Fokus:** Hilft bei Reaktion auf Abmahnung, Strafanzeige, polizeiliche Anhörung, Plattformmeldung oder Löschungsverlangen wegen einer Äußerung. Erstellt Fristencheck, Beweisplan und Verteidigungsstrategie.

# Reaktion auf Abmahnung oder Strafanzeige

## Sofortregeln

- Fristen notieren.
- Äußerung und Kontext sichern.
- Keine vorschnelle Schuldanerkennung.
- Bei Polizei als Beschuldigter grundsätzlich Schweigerecht beachten.
- Unterlassungserklärung nie ungeprüft unterschreiben.

## Prüfprogramm

1. Was wird konkret beanstandet?
2. Welche Äußerung und welches Medium?
3. Strafrecht, Zivilrecht oder Plattformregel?
4. Sind Wortlaut und Kontext richtig wiedergegeben?
5. Welche Belege gibt es?
6. Gibt es Wiederholungsgefahr?
7. Welche Reaktion passt: Zurückweisung, modifizierte Unterlassung, Klarstellung, Vergleich?

## Output

- Fristencheck.
- Risikoampel.
- Verteidigungslinie.
- Dokumentenliste.
- Entwurf einer ersten anwaltlichen Antwort oder Mandantennotiz.

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
