---
name: fruehere-interessenvertretung
description: "Fruehere Interessenvertretung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fruehere Interessenvertretung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Fruehere Interessenvertretung** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fruehere-interessenvertretung-exit` | Führt durch Anzeige, dass keine registrierungspflichtige Interessenvertretung mehr betrieben wird, sowie Archivierung und Monitoring der Liste frueherer Eintraege. Output Exit-Akte. |
| `geschaeftsjahresaktualisierung` | Führt durch die mindestens jaehrliche vollständige Überprüfung und Bestätigung des Registereintrags nach § 3 und § 4 LobbyRG. Output Jahresupdate-Mappe. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Fruehere Interessenvertretung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fruehere-interessenvertretung-exit`

**Fokus:** Führt durch Anzeige, dass keine registrierungspflichtige Interessenvertretung mehr betrieben wird, sowie Archivierung und Monitoring der Liste frueherer Eintraege. Output Exit-Akte.

# Exit und fruehere Interessenvertretung

## Einsatz

Registereintraege geordnet beenden, statt sie verwahrlosen zu lassen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wurde die Interessenvertretung dauerhaft eingestellt?
2. Welche Auftraege, Vorhaben und Kontakte laufen noch aus?
3. Welche Dokumente muessen archiviert werden?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Exit-Akte mit Beendigungsentscheidung, Portalaktion, Archivplan und Wiedervorlage.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `geschaeftsjahresaktualisierung`

**Fokus:** Führt durch die mindestens jaehrliche vollständige Überprüfung und Bestätigung des Registereintrags nach § 3 und § 4 LobbyRG. Output Jahresupdate-Mappe.

# Geschaeftsjahresaktualisierung

## Einsatz

Den jaehrlichen Registercheck planbar und belegbar machen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wann endet das Geschaeftsjahr?
2. Welche Finanzdaten, Mitgliederzahlen und Abschluesse sind neu?
3. Wer bestaetigt Richtigkeit und Vollstaendigkeit?

## Aktualisierungsmechanik § 4 LobbyRG

- **Unverzüglich (§ 4 Abs. 1 LobbyRG):** Stammdatenänderungen — neue Auftraggeber, geänderte Schwerpunkte, Personalwechsel in der Interessenvertretung; Praxisrichtwert: binnen 4 Wochen.
- **Jährlich (§ 4 Abs. 3 LobbyRG):** Vollständige Bestätigung des Eintrags zum Stichtag des Geschäftsjahresendes; ohne Bestätigung wird Eintrag als "nicht bestätigt" markiert.
- **Finanzangaben (§ 3 Abs. 1 Nr. 5–7 LobbyRG):** Innerhalb von 6 Monaten nach Geschäftsjahresende — Jahresabschluss, Spenden- und Zuwendungen, Honorareinnahmen mit Schwellenbeträgen (10.000-Euro-Schritte).
- **Tätigkeitsbericht:** Schwerpunkte der Interessenvertretung im abgelaufenen Geschäftsjahr; konkrete Anliegen oder Themen.
- **Verantwortlichkeit:** Vertretungsberechtigte Person nach Handelsregister/Vereinsregister; in Kanzleien Partner; bei juristischen Personen Geschäftsführung — Unterschrift bzw. qualifiziertes Login.
- **Sanktion:** Bußgeld bis 50.000 Euro (§ 7 LobbyRG) bei vorsätzlich/leichtfertig falschen oder unterlassenen Angaben; Vermerk im Register; Reputationsschaden.
- **Praxis-Tipp:** Compliance-Kalender mit zwei festen Daten — Stichtag GJ-Ende und +6 Monate für Finanzangaben; Vorab-Review durch Compliance/Externe vor Portal-Submission.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Jahresupdate-Mappe mit Zeitplan, Datenanforderung, Review-Tabelle, Signatur und Portalnotiz.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
