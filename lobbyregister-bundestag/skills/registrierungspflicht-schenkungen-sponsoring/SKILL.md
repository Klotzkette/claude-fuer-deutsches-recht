---
name: registrierungspflicht-schenkungen-sponsoring
description: "Registrierungspflicht Schenkungen Sponsoring: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Registrierungspflicht Schenkungen Sponsoring

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Registrierungspflicht Schenkungen Sponsoring** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `registrierungspflicht-schwellen` | Prüft § 2 Abs. 1 LobbyRG: regelmäßig, auf Dauer, geschäftsmäßig für Dritte, mehr als 30 Kontakte in drei Monaten, Gegenleistung oder Auftrag. Output Pflichtampel. |
| `schenkungen-sponsoring` | Prüft Schenkungen und sonstige lebzeitige Zuwendungen Dritter, Gesamtstufe, Einzelangaben, Zustimmung und Altfall-Anonymisierung. Output Sponsoring-Check. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Registrierungspflicht Schenkungen Sponsoring**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `registrierungspflicht-schwellen`

**Fokus:** Prüft § 2 Abs. 1 LobbyRG: regelmäßig, auf Dauer, geschäftsmäßig für Dritte, mehr als 30 Kontakte in drei Monaten, Gegenleistung oder Auftrag. Output Pflichtampel.

# Registrierungspflicht und Schwellen

## Einsatz

Entscheiden, ob eine unverzuegliche Registrierungspflicht ausgeloest ist.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wie oft und seit wann wird Interessenvertretung betrieben?
2. Wird fuer Dritte oder gegen Gegenleistung gehandelt?
3. Wie viele unterschiedliche Kontakte gab es in den letzten drei Monaten?

## Rechtsstand 2026

Reformfassung LobbyRG durch Gesetz zur Aenderung des Lobbyregistergesetzes vom 15.01.2024 (BGBl. I 2024, in Kraft 01.03.2024). Reformiert wurden unter anderem § 2 (Anwendungsbereich, einschliesslich Referatsleiterebene), § 3 (Eintragspflichtige Angaben, jetzt mit konkreten Regelungsvorhaben, betroffenen Bereichen und Upload von Stellungnahmen und Gutachten von grundsaetzlicher Bedeutung) und § 5 (Verhaltenskodex).

## Quellenanker

- LobbyRG (konsolidierte Fassung 2024): https://www.bundestag.de/resource/blob/991838/Konsolidierte-Fassung-LobbyRG-2024.pdf
- LobbyRG bei gesetze-im-internet: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Pflichtampel mit Schwellenrechnung, Triggerdatum und naechstem Portal-Schritt.

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

## 2. `schenkungen-sponsoring`

**Fokus:** Prüft Schenkungen und sonstige lebzeitige Zuwendungen Dritter, Gesamtstufe, Einzelangaben, Zustimmung und Altfall-Anonymisierung. Output Sponsoring-Check.

# Schenkungen und Sponsoring

## Einsatz

Schenkungen transparent und datenschutzsensibel im Register vorbereiten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Drittzuwendungen gab es im letzten Geschaeftsjahr?
2. Welche Geber erreichen Einzel- und Prozent-Schwellen?
3. Liegt Einwilligung oder ein Altfall vor Maerz 2024 vor?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Sponsoring-Check mit Gesamtstufe, Einzelgebern, Einwilligungsstatus und Anonymisierungsnotiz.

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
