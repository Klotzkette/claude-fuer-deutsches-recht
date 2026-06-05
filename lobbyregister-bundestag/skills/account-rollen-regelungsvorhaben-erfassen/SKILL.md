---
name: account-rollen-regelungsvorhaben-erfassen
description: "Account Rollen Regelungsvorhaben Erfassen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Account Rollen Regelungsvorhaben Erfassen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Account Rollen Regelungsvorhaben Erfassen** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `portal-account-rollen` | Plant Administrationskonto, Rollen, Zugriffsschutz, Zwei-Personen-Freigabe und Passwortmanager für das Lobbyregisterportal. Output Account-Konzept. |
| `regelungsvorhaben-erfassen` | Erfasst konkrete aktuelle, geplante oder angestrebte Regelungsvorhaben, auch ohne vorhandenen Referentenentwurf oder Drucksache. Output Regelungsvorhaben-Karte. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Account Rollen Regelungsvorhaben Erfassen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `portal-account-rollen`

**Fokus:** Plant Administrationskonto, Rollen, Zugriffsschutz, Zwei-Personen-Freigabe und Passwortmanager für das Lobbyregisterportal. Output Account-Konzept.

# Portal-Account und Rollen

## Einsatz

Den Portalzugang organisatorisch robust und revisionsfest aufsetzen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wer administriert den Eintrag?
2. Wer darf Daten erfassen, pruefen, freigeben und bestaetigen?
3. Wie werden Vertretung, Passwortwechsel und Ausscheiden geregelt?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Account-Konzept mit Rollen, Rechtekette, Backup, Freigabeprozess und Sicherheitsnotizen.

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

## 2. `regelungsvorhaben-erfassen`

**Fokus:** Erfasst konkrete aktuelle, geplante oder angestrebte Regelungsvorhaben, auch ohne vorhandenen Referentenentwurf oder Drucksache. Output Regelungsvorhaben-Karte.

# Regelungsvorhaben erfassen

## Einsatz

Regelungsvorhaben so konkret eintragen, dass der Einflussgegenstand transparent wird.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche rechtliche Regelung soll eingefuehrt, geaendert, beibehalten oder verhindert werden?
2. Gibt es Referentenentwurf, Drucksache oder bekannte Initiative?
3. Wann steht die erste Kontaktaufnahme dazu bevor?
4. Wie soll das Vorhaben spaeter im oeffentlichen JSON/API-Export wiedergefunden werden?

## API-Suchfaehigkeit

Formuliere Regelungsvorhaben so, dass sie sowohl im Portal als auch spaeter in API/API-Export nachvollziehbar sind: sprechender Titel, Bezug zu Gesetz, Verordnung oder politischer Initiative, keine zu breiten Sammelbegriffe, konsistente Schreibweisen. Fuer Monitoring Suchbegriffe, Varianten und erwartete JSON-Felder `regulatoryProjects` und `statements` notieren.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Regelungsvorhaben-Karte mit Titel, Ziel, Bezug, Dokumentenlinks, Kontaktstart, Updatepflicht und API-Suchprofil.

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
