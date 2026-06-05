---
name: beleglage-tatsachenbehauptung-beweissicherung
description: "Beleglage Tatsachenbehauptung Beweissicherung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beleglage Tatsachenbehauptung Beweissicherung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Beleglage Tatsachenbehauptung Beweissicherung** im Plugin Meinungsfreiheit/Persönlichkeitsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beleglage-tatsachenbehauptung` | Erstellt eine Belegmatrix für Tatsachenbehauptungen, Verdachtsäußerungen und gemischte Äußerungen. Prüft Wahrheit, Beweisbarkeit, Nichterweislichkeit, bewusste Unwahrheit, Quellenqualität und Dokumentationsbedarf. |
| `beweissicherung-screenshots` | Erstellt einen Beweissicherungsplan für Screenshots, URLs, Zeitstempel, Chatverläufe, Zeugen, Metadaten, Löschungen und Exportdateien. Geeignet für Social Media, Messenger, E-Mail und Bewertungsportale. |

## Arbeitsweg

Im Plugin Meinungsfreiheit/Persönlichkeitsrecht gilt für **Beleglage Tatsachenbehauptung Beweissicherung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beleglage-tatsachenbehauptung`

**Fokus:** Erstellt eine Belegmatrix für Tatsachenbehauptungen, Verdachtsäußerungen und gemischte Äußerungen. Prüft Wahrheit, Beweisbarkeit, Nichterweislichkeit, bewusste Unwahrheit, Quellenqualität und Dokumentationsbedarf.

# Beleglage bei Tatsachenbehauptungen

## Aufgabe

Sobald eine Äußerung einen Tatsachenkern hat, muss dieser gesondert geprüft werden. Das Ziel ist nicht, vorschnell jede Tatsache zu verbieten, sondern Belegbarkeit und Risiko sauber zu dokumentieren.

## Belegmatrix

| Tatsachenkern | Quelle | Qualität | Gegenbeleg | Risiko |
|---|---|---|---|---|
| | eigene Wahrnehmung / Dokument / Zeuge / öffentlich / Hörensagen | stark / mittel / schwach | | grün / gelb / rot |

## Prüfpunkte

1. **Wahrheit:** Ist die Behauptung belegbar wahr?
2. **Nichterweislichkeit:** Bei § 186 StGB kann schon fehlender Wahrheitsbeweis problematisch sein.
3. **Bewusste Unwahrheit:** Bei § 187 StGB und im Zivilrecht besonders gefährlich.
4. **Verdachtsäußerung:** Mindestbestand an Belegtatsachen? Betroffener vorher angehört? Verdacht als Verdacht gekennzeichnet?
5. **Wertung auf Tatsachenbasis:** Sind die zugrunde gelegten Tatsachen vollständig genug?
6. **Aktualität:** Ist der Sachverhalt überholt, korrigiert oder erledigt?

## Besonders riskante Tatsachenkerne

- Straftatvorwürfe: Betrug, Korruption, Urkundenfälschung, Diebstahl.
- Berufliche Pflichtverletzungen: "fälscht", "kassiert doppelt", "arbeitet bewusst gegen Kunden".
- Gesundheits-, Schul- oder Arbeitsplatzvorwürfe mit identifizierbaren Personen.
- Unternehmensbezogene Aussagen, die Kredit, Erwerb oder Fortkommen gefährden können.

## Output

Gib aus:

- Liste der Tatsachenkerne.
- Belegstand.
- Welche Formulierungen als Meinung erhalten bleiben können.
- Welche Formulierungen entschärft oder belegt werden müssen.
- Vorschlag für belegbare Alternativformulierungen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `beweissicherung-screenshots`

**Fokus:** Erstellt einen Beweissicherungsplan für Screenshots, URLs, Zeitstempel, Chatverläufe, Zeugen, Metadaten, Löschungen und Exportdateien. Geeignet für Social Media, Messenger, E-Mail und Bewertungsportale.

# Beweissicherung

## Grundsatz

Ohne sauberen Beweis ist Äußerungsrecht oft nur Gefühl. Sichere nicht nur den Satz, sondern auch Kontext, Reichweite und Identifizierbarkeit.

## Checkliste

- vollständiger Screenshot mit Datum, Uhrzeit, URL, Accountname.
- Thread oder Chat davor und danach.
- Profilseite und Impressum, soweit relevant.
- sichtbare Reichweite: Likes, Kommentare, Shares.
- Bild, Tagging, Hashtags, Gruppenname.
- Exportdatei bei Messenger oder E-Mail.
- Zeugenvermerk bei mündlicher Äußerung.
- Löschzeitpunkt und etwaige Korrektur.

## Beweisblatt

| Beweis | Datei/Ort | Was belegt es? | Schwäche |
|---|---|---|---|

## Output

- Was ist bereits gesichert?
- Was fehlt?
- Welche Beweise sind besonders dringend?
- Was sollte nicht verändert werden?

## Warnung

Keine heimlichen Aufnahmen empfehlen. Bei Ton-/Videoaufnahmen immer gesondert Strafbarkeit und Datenschutz prüfen.

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
