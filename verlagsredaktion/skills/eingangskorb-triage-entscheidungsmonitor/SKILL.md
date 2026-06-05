---
name: eingangskorb-triage-entscheidungsmonitor
description: "Eingangskorb Triage Entscheidungsmonitor: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Eingangskorb Triage Entscheidungsmonitor

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Eingangskorb Triage Entscheidungsmonitor** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `eingangskorb-triage` | Sortiert einen Verlags-Eingangskorb aus Mails, Manuskripten, Fahnen, Bildern, Tabellen und Notizen nach Frist, Risiko, Projekt und naechster Aktion. |
| `entscheidungsmonitor-rechtsstand` | Erfasst neue Entscheidungen, Gesetze und Materialien als moegliche Aktualisierungsanlaesse fuer Zeitschrift, Kommentar, Newsletter oder Buchauflage. |
| `fremdtext-plagiat-uebernahmecheck` | Markiert Fremdtext-, Copy-Paste-, Plagiats-, KI-Text- und Paraphrase-Risiken und erstellt eine redaktionelle Klaerungsliste. |
| `knowledge-base-faq-kundenservice` | Erstellt FAQ, interne Wissensbasis und Kundenservice-Antworten zu Verlagstiteln, Updates, Downloads, Errata, Lizenzen und Produktfragen. |
| `kommentar-aktualisierung-randnummern` | Unterstuetzt Kommentarupdates mit Randnummernlogik, Rechtsstandsvermerk, Nachweisen, Aenderungsprotokoll und Autor:innenrueckfragen. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Eingangskorb Triage Entscheidungsmonitor**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `eingangskorb-triage`

**Fokus:** Sortiert einen Verlags-Eingangskorb aus Mails, Manuskripten, Fahnen, Bildern, Tabellen und Notizen nach Frist, Risiko, Projekt und naechster Aktion.

# Eingangskorb-Triage

## Arbeitsweise

1. Alles Material listen.
2. Projekt oder Produkt zuordnen.
3. Frist und Abhängigkeit erkennen.
4. Rechte-/Datenschutzrisiko markieren.
5. Nächste Aktion formulieren.

## Kategorien

- Sofort: Druck, Onlinegang, Freigabe, Rechteproblem.
- Heute: Autor:innenantwort, fehlende Anlage, Korrektur.
- Diese Woche: Lektorat, Metadaten, Marketing, Vertrieb.
- Parken: Hintergrund, Ideen, spätere Auflage.

## Output

- Eingangskorb-Tabelle.
- Tagesprioritäten.
- E-Mail-Entwürfe für Nachforderungen.
- Übergabe an passende Fachmodule.

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

## 2. `entscheidungsmonitor-rechtsstand`

**Fokus:** Erfasst neue Entscheidungen, Gesetze und Materialien als moegliche Aktualisierungsanlaesse fuer Zeitschrift, Kommentar, Newsletter oder Buchauflage.

# Entscheidungsmonitor und Rechtsstand

## Ziel

Aus neuen Quellen wird keine Halluzinationsmaschine, sondern eine saubere Aktualisierungsliste.

## Prüfung

- Quelle.
- Datum.
- Aktenzeichen oder Gesetzesfundstelle.
- betroffene Produkte.
- Aktualisierungsbedarf.
- Dringlichkeit.
- Autor:in oder Herausgeber:in.

## Output

- Monitoring-Tabelle.
- Update-Prioritäten.
- Autor:innenbriefing.
- Newsletter-Idee.
- Quellenstatus.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?

## Startfragen

Wenn Material oder Ziel unklar sind, stelle hoechstens drei Fragen: Was soll veroeffentlicht oder uebergeben werden? Fuer wen ist es bestimmt? Bis wann muss es freigegeben sein? Danach mit einer belastbaren Arbeitsfassung beginnen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `fremdtext-plagiat-uebernahmecheck`

**Fokus:** Markiert Fremdtext-, Copy-Paste-, Plagiats-, KI-Text- und Paraphrase-Risiken und erstellt eine redaktionelle Klaerungsliste.

# Fremdtext- und Übernahmecheck

## Ziel

Nicht kriminalisieren, sondern sauber klären: Was ist Autor:innenleistung, was ist Zitat, was ist Paraphrase, was muss neu formuliert oder belegt werden?

## Prüfung

- auffällig wechselnder Stil.
- lange unmarkierte Passagen.
- fehlende Quellen.
- KI-typische Glättung ohne Belege.
- Tabellen oder Übersichten ohne Herkunft.
- Screenshots aus Drittquellen.

## Output

- Risikoliste.
- Textstellen mit Markierung.
- Nachforderungsmail.
- Vorschlag: zitieren, paraphrasieren, streichen, Rechte klären.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?

## Urheber- und zitatrechtliche Anker
- **Zitatrecht (§ 51 UrhG):** zulaessig fuer den Zweck des Zitats, mit Quellenangabe (§ 63 UrhG); Beispiele: Grosszitat im wissenschaftlichen Werk; Kleinzitat im laufenden Text.
- **Kein Schutz reiner Tatsachen:** Aussage "Der BGH hat am ... entschieden, dass ..." ist urheberrechtlich frei; konkrete Formulierung der Leitsaetze ist es regelmaessig auch, aber Sicherheits-Praxis: zitieren.
- **Amtliche Werke (§ 5 UrhG):** Gesetze, Verordnungen, Urteile sind nicht urheberrechtlich geschuetzt -- Wiedergabe frei, aber bei Bearbeitungen (etwa Kommentar-Auszuege) Rechte des Bearbeiters beachten.
- **KI-Text-Risiko:** Erzeugnisse generativer KI haben keinen klaren Urheberschutz, koennen aber unlautere Wettbewerbsbedingungen ausloesen (§ 4 UWG Nachahmung) und ggf. Trainingsdatenfragen offenlegen.
- **Bildrechte:** Verwendung von Personenabbildungen nach §§ 22, 23 KUG; gestockfotografische Inhalte mit Lizenzkette nachweisen.
- **Plagiats-Folgen wissenschaftlich:** wissenschaftliche Reputationsschaeden; verlagsseitige Vertragsstrafen; Schadensersatz Verlag.

## Praktische Checkliste
- Stilbruchanalyse je Absatz; semantische Konsistenz; Quellenverzeichnis komplett?
- Bilder mit Lizenznachweis; URL+Stand fuer Webquellen; Bibliographie nach `references/zitierweise.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `knowledge-base-faq-kundenservice`

**Fokus:** Erstellt FAQ, interne Wissensbasis und Kundenservice-Antworten zu Verlagstiteln, Updates, Downloads, Errata, Lizenzen und Produktfragen.

# Knowledge Base und Kundenservice

## Einsatz

Für wiederkehrende Fragen aus Vertrieb, Support, Autor:innenbetreuung oder Redaktion.

## Output

- FAQ.
- interne Antwortbausteine.
- Eskalationsregeln.
- Produktstatus.
- Errata-Hinweise.
- Download-/Lizenzhinweise.

## Regel

Keine rechtlichen oder vertraglichen Zusagen erfinden. Unklare Punkte an Verlag/Justiziariat routen.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?

## Startfragen

Wenn Material oder Ziel unklar sind, stelle hoechstens drei Fragen: Was soll veroeffentlicht oder uebergeben werden? Fuer wen ist es bestimmt? Bis wann muss es freigegeben sein? Danach mit einer belastbaren Arbeitsfassung beginnen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `kommentar-aktualisierung-randnummern`

**Fokus:** Unterstuetzt Kommentarupdates mit Randnummernlogik, Rechtsstandsvermerk, Nachweisen, Aenderungsprotokoll und Autor:innenrueckfragen.

# Kommentar-Aktualisierung und Randnummern

## Aufgaben

1. Norm oder Abschnitt bestimmen.
2. alten Stand erfassen.
3. neue Gesetzgebung oder Rechtsprechung als Anlass markieren.
4. Randnummernänderungen vorschlagen.
5. Nachweise prüfen.
6. Autor:innenfragen sammeln.

## Output

- Änderungsprotokoll.
- Randnummernplan.
- Rechtsstandsvermerk.
- Nachweisampel.
- offene Autor:innenfragen.

## Schneller Arbeitsmodus

- Erst klaeren: Produktart, Adressat, Verwendungsort, Frist und Freigabeperson. Wenn Angaben fehlen, mit einer kurzen Arbeitsannahme starten und offene Punkte sichtbar markieren.
- Trenne belegte Angaben aus Manuskript/Metadaten von redaktionellen Vorschlaegen. Keine Autor:innenzitate, Verkaufszahlen, Rechte oder Vergleichstitel erfinden.
- Liefere zuerst eine nutzbare Arbeitsfassung, danach eine kurze Pruefliste fuer Herstellung, Marketing, Vertrieb, Justiziariat oder Autor:innen.

## Qualitaetsgate

- Ist der Text fuer den konkreten Kanal verwendbar?
- Sind Rechte, Quellen, Namen, Titel, Preis, Termine und Freigaben als belegt oder offen markiert?
- Gibt es genau die naechsten Schritte mit Owner, Frist und Eskalation?

## Startfragen

Wenn Material oder Ziel unklar sind, stelle hoechstens drei Fragen: Was soll veroeffentlicht oder uebergeben werden? Fuer wen ist es bestimmt? Bis wann muss es freigegeben sein? Danach mit einer belastbaren Arbeitsfassung beginnen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
