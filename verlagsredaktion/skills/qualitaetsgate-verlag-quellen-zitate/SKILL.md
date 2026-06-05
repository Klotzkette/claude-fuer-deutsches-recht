---
name: qualitaetsgate-verlag-quellen-zitate
description: "Qualitaetsgate Verlag Quellen Zitate: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Qualitaetsgate Verlag Quellen Zitate

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Qualitaetsgate Verlag Quellen Zitate** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `qualitaetsgate-verlag` | Schlusspruefung fuer Verlagsoutputs vor Autor:innenversand, Satz, Onlinegang oder Druck mit Rechte-, Quellen-, Stil-, Fristen- und Produktionsampel. |
| `quellen-zitate-fundstellencheck` | Prueft Quellen, Zitate, Randnummern, Fundstellen, Rechtsprechung und Literaturstatus mit strenger Regel gegen erfundene oder paywallige Blindzitate. |
| `rechtecheck-urhg-verlg` | Erstellt eine redaktionelle Rechteampel zu UrhG, Verlagsgesetz, Nutzungsrechten, Zitatrecht, Bearbeitung, Zweitveroeffentlichung und Freigaben. |
| `rohmanuskript-anschubhilfe` | Baut aus Diktaten, Folien, Notizen und E-Mails ein klar markiertes Rohmanuskript als Anschubhilfe, ohne Autor:innenstimme und Redaktion zu vermischen. |
| `sachbearbeiterinnen-cockpit` | Persoenliches Verlagscockpit fuer Sachbearbeitung und Redaktion: Tageslage, Prioritaeten, Fristen, Autor:innen, Rechteampel, Produktionsstand und naechste Aktionen. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Qualitaetsgate Verlag Quellen Zitate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `qualitaetsgate-verlag`

**Fokus:** Schlusspruefung fuer Verlagsoutputs vor Autor:innenversand, Satz, Onlinegang oder Druck mit Rechte-, Quellen-, Stil-, Fristen- und Produktionsampel.

# Qualitätstor Verlag

## Pflichtcheck

| Feld | Frage |
| --- | --- |
| Auftrag | Ist klar, was erstellt werden sollte? |
| Material | Ist die Herkunft markiert? |
| Rechte | Gibt es rote oder gelbe Punkte? |
| Quellen | Sind Fundstellen prüfbar? |
| Stil | Passt der Ton zur Zielgruppe? |
| Frist | Ist der nächste Termin sichtbar? |
| Freigabe | Wer muss noch zustimmen? |
| Produktion | Sind Dateien und Metadaten vollständig? |

## Output

- Go/No-Go.
- Stopper.
- offene Rückfragen.
- finale To-do-Liste.
- Versand-/Produktionsfreigabeentwurf.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `quellen-zitate-fundstellencheck`

**Fokus:** Prueft Quellen, Zitate, Randnummern, Fundstellen, Rechtsprechung und Literaturstatus mit strenger Regel gegen erfundene oder paywallige Blindzitate.

# Quellen-, Zitate- und Fundstellencheck

## Quellenregel

Keine Kommentar-, Handbuch-, Aufsatz- oder Datenbankfundstellen aus Modellwissen. Literatur nur aus Nutzerquelle, frei zugänglicher Quelle oder lizenziertem Live-Zugriff. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.

## Prüfung

1. Jede Fundstelle extrahieren.
2. Quelle klassifizieren.
3. Existenzstatus markieren.
4. Pinpoint prüfen.
5. Hausstil anwenden.
6. Unsichere Stellen nicht verbessern, sondern markieren.

## Output

- Fundstellenliste.
- Ampel.
- Korrekturvorschläge.
- `[Quelle zu prüfen]`-Liste.
- Rechtsprechungs-Rechercheaufträge.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?

## 3. `rechtecheck-urhg-verlg`

**Fokus:** Erstellt eine redaktionelle Rechteampel zu UrhG, Verlagsgesetz, Nutzungsrechten, Zitatrecht, Bearbeitung, Zweitveroeffentlichung und Freigaben.

# Rechtecheck UrhG und Verlagsgesetz

## Kein Rechtsgutachten

Dieser Skill bereitet Rechtefragen für Redaktion, Justiziariat oder externe Prüfung vor.

## Prüfpunkte

- Wer ist Urheber:in?
- Welche Nutzungsrechte liegen vor?
- Exklusiv oder einfach?
- Print, E-Book, Online, Datenbank, Newsletter, Social?
- Bearbeitung erlaubt?
- Fremdmaterial enthalten?
- Zitatrecht plausibel?
- Zweitveröffentlichungsrecht oder vorherige Veröffentlichung?

## Rechtsanker

UrhG §§ 31 ff., § 38, § 39, § 51, § 63; Verlagsgesetz; vertragliche Vereinbarungen.

## Output

- Rechteampel.
- Freigabeliste.
- Fragen an Autor:in.
- Stopp-Hinweise.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `rohmanuskript-anschubhilfe`

**Fokus:** Baut aus Diktaten, Folien, Notizen und E-Mails ein klar markiertes Rohmanuskript als Anschubhilfe, ohne Autor:innenstimme und Redaktion zu vermischen.

# Rohmanuskript-Anschubhilfe

## Grundsatz

Das Ergebnis ist ein Arbeitsentwurf, kein stillschweigend fertiger Autor:innentext.

## Ablauf

1. Materialinventar übernehmen.
2. Themencluster bilden.
3. Gliederung vorschlagen.
4. Material je Abschnitt zuordnen.
5. Rohtext schreiben.
6. Lücken und Rechtefragen sichtbar markieren.
7. Autor:innenfreigabe vorbereiten.

## Markierungen

- `[A]` aus Autor:innenmaterial.
- `[R]` redaktionelle Überleitung.
- `[LUECKE]` fehlt.
- `[QUELLE]` prüfen.
- `[RECHTE]` nicht freigegeben.

## Output

- Rohmanuskript.
- Gliederung.
- Fragen an Autor:in.
- Nächster Redaktionsschritt.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `sachbearbeiterinnen-cockpit`

**Fokus:** Persoenliches Verlagscockpit fuer Sachbearbeitung und Redaktion: Tageslage, Prioritaeten, Fristen, Autor:innen, Rechteampel, Produktionsstand und naechste Aktionen.

# Sachbearbeiterinnen-Cockpit

## Ziel

Die Nutzerin soll nach zwei Minuten wissen: Was brennt, was wartet, wer muss angeschrieben werden, was darf noch nicht in Satz oder online.

## Eingang

Verarbeite Mails, Dateiordner, Tabellen, Notizen oder Chatverläufe zu einer Tageskarte.

## Ausgabe

| Block | Inhalt |
| --- | --- |
| Heute kritisch | Fristen, Drucktermine, fehlende Freigaben |
| Autor:innen | Rückstände, Rückfragen, offene Rechte |
| Manuskripte | Status je Beitrag oder Kapitel |
| Rechteampel | Fremdtext, Bilder, Tabellen, KI-Herkunft |
| Nächste Aktionen | Aufgabe, Zuständige, Frist, Vorlage |

## Regeln

- Keine langen Erklärungen.
- Alles in Aufgaben übersetzen.
- Wenn etwas unklar ist, als offene Entscheidung markieren.
- Bei Rot-Status immer konkreten Stopp nennen.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
