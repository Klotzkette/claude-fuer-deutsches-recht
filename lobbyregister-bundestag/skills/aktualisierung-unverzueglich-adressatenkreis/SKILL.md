---
name: aktualisierung-unverzueglich-adressatenkreis
description: "Aktualisierung Unverzueglich Adressatenkreis: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aktualisierung Unverzueglich Adressatenkreis

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Aktualisierung Unverzueglich Adressatenkreis** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aktualisierung-unverzueglich` | Steuert unverzuegliche Updates bei Stammdaten, Personen, Tätigkeitsbeschreibung, Vorhabenbereichen, Regelungsvorhaben, Auftraegen und Auftraggebern. Output Update-Ticket. |
| `adressatenkreis-bundestag-bundesregierung` | Kartiert Adressatinnen und Adressaten nach § 1 LobbyRG: Bundestagsorgane, Mitglieder, Fraktionen, Gruppen, Mitarbeitende, Bundesregierung und Leitungsebenen bis Referatsleitung. Output Adressatenkarte. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Aktualisierung Unverzueglich Adressatenkreis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aktualisierung-unverzueglich`

**Fokus:** Steuert unverzuegliche Updates bei Stammdaten, Personen, Tätigkeitsbeschreibung, Vorhabenbereichen, Regelungsvorhaben, Auftraegen und Auftraggebern. Output Update-Ticket.

# Unverzuegliche Aktualisierung

## Einsatz

Aenderungen so schnell erfassen, dass keine verspaetete Aktualisierung entsteht.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Angabe hat sich wann geaendert?
2. Ist die Aenderung registerrelevant?
3. Wer muss Text, Beleg und Freigabe liefern?
4. Welche veroeffentlichten API-Felder muessen nach der Portalaktion kontrolliert werden?

## API-Nachkontrolle

Nach einer Portalaktualisierung soll der Skill eine Wiedervorlage fuer den oeffentlichen API-Abgleich anlegen:

1. Vorherige API-Antwort oder PDF-Version aus der Akte ziehen.
2. Nach Veroeffentlichung `GET /registerentries/{registerNumber}?format=json` abrufen.
3. Wenn die Version geaendert wurde, alte und neue Version gegenueberstellen.
4. `lastUpdateDate`, `validFromDate`, `fiscalYearUpdate.updateMissing`, `refusedAnything`, Regelungsvorhaben, Stellungnahmen, Personen und Finanzdaten pruefen.
5. Abweichungen in `assets/templates/registerexport-diff.md` dokumentieren.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Update-Ticket mit Ausloeser, Pflichtfeld, Deadline, Portaltext, Verantwortlichem, API-Nachkontrolle und Kontrollpunkt.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Nach der Veroeffentlichung wird die API-Antwort als Beleg gesichert oder die fehlende Veroeffentlichung eskaliert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `adressatenkreis-bundestag-bundesregierung`

**Fokus:** Kartiert Adressatinnen und Adressaten nach § 1 LobbyRG: Bundestagsorgane, Mitglieder, Fraktionen, Gruppen, Mitarbeitende, Bundesregierung und Leitungsebenen bis Referatsleitung. Output Adressatenkarte.

# Adressatenkreis Bundestag und Bundesregierung

## Einsatz

Ermitteln, ob der konkrete Kontakt in den Anwendungsbereich faellt.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Person oder Stelle soll kontaktiert werden?
2. Ist es Bundestag, Bundesregierung, Ministerium, nachgeordnete Behoerde oder EU-Ebene?
3. Sind Mitarbeitende, Referatsleitungen oder politische Leitung betroffen?

## Rechtsstand 2026

Reformfassung des LobbyRG durch das Gesetz zur Aenderung des Lobbyregistergesetzes vom 15.01.2024, in Kraft seit 01.03.2024. Wesentliche Neuerung: Kontakte zu Bundesministerien werden bereits ab Referatsleiterebene erfasst (§ 1 Abs. 3 Nr. 2 LobbyRG n.F.). Uebergangsfrist fuer Bestandsregistrierungen lief bis 30.06.2024.

## Quellenanker

- LobbyRG (konsolidierte Fassung 2024): https://www.bundestag.de/resource/blob/991838/Konsolidierte-Fassung-LobbyRG-2024.pdf
- LobbyRG bei gesetze-im-internet: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Bundestag Hinweise zur Rechtslage ab 01.03.2024: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-zur-neuen-rechtslage-ab-dem-1-maerz-2024-955618
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Adressatenkarte mit In-Scope/Out-of-Scope, Belegquelle und Folgepflichten.

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
