---
name: benachrichtigungskonto-monitor
description: "Benachrichtigungskonto Monitor: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Benachrichtigungskonto Monitor

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Benachrichtigungskonto Monitor** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `benachrichtigungskonto-monitor` | Richtet Beobachtung von Registereintraegen, Aktualisierungen und Entwicklungen über das Benachrichtigungskonto ein. Output Watchlist. |
| `bestaetigungsdokument-freigabe` | Bestimmt Unterzeichner, Leitungsperson, vertretungsberechtigte Person und interne Freigabe vor Eintragung oder Geschäftsjahresaktualisierung. Output Signaturmappe. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Benachrichtigungskonto Monitor**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `benachrichtigungskonto-monitor`

**Fokus:** Richtet Beobachtung von Registereintraegen, Aktualisierungen und Entwicklungen über das Benachrichtigungskonto ein. Output Watchlist.

# Benachrichtigungskonto Monitor

## Einsatz

Automatisierte Benachrichtigungen in Compliance- oder Wettbewerbsmonitoring einbauen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Registereintraege oder Themen sollen beobachtet werden?
2. Wer erhaelt Benachrichtigungen?
3. Wie werden Alerts bewertet und dokumentiert?
4. Welche API-Abfrage bildet die gleiche Watchlist maschinenlesbar ab?

## Benachrichtigungskonto und API

Das Benachrichtigungskonto ist die fachliche Watchlist im Lobbyregisterumfeld. Die API ist die technische Kontrollspur. Der Skill soll beide Ebenen trennen:

- Benachrichtigungskonto: Empfaenger, Suchprofil, fachliche Bewertung, Eskalation.
- API-Monitor: Endpunkt, Suchparameter, Cursor, `sourceDate`, Registernummern, Versionswechsel, Diff.
- Revisionsspur: Alert, API-Antwort, interne Bewertung und Portalaktion werden zusammen abgelegt.

Bei eigenen Eintraegen ist ein Alert nur vollstaendig bearbeitet, wenn der oeffentliche API-Datenstand mit der internen Freigabeakte verglichen wurde.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Watchlist mit Suchprofilen, Empfaengern, API-Monitoringplan, Bewertungsschema, Revisionsspur und Eskalation.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Alertdaten und API-Daten werden sauber als getrennte Belege benannt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `bestaetigungsdokument-freigabe`

**Fokus:** Bestimmt Unterzeichner, Leitungsperson, vertretungsberechtigte Person und interne Freigabe vor Eintragung oder Geschäftsjahresaktualisierung. Output Signaturmappe.

# Bestaetigungsdokument und Freigabe

## Einsatz

Die Richtigkeitsbestaetigung wirksam und organisatorisch nachvollziehbar vorbereiten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Rechtsform liegt vor?
2. Wer ist Leitungsperson oder vertretungsberechtigt?
3. Welche interne Pruefung muss vor Unterschrift dokumentiert sein?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Signaturmappe mit Unterzeichner, Rechtsgrund, Pruefvermerk, Anlagen und Freigabezeile.

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
