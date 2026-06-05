---
name: intake-mandat-lobbyregister
description: "Intake Mandat Lobbyregister: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Intake Mandat Lobbyregister

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Intake Mandat Lobbyregister** im Plugin Lobbyregister Bundestag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lobbyregister-intake-mandat` | Erfasst Ausgangslage, Organisation, Kontaktplaene, Auftraggeber, Fristen und Portalstatus vor jeder Lobbyregister-Prüfung. Nutzt LobbyRG §§ 1 bis 5 und Bundestags-Handbuch. Output Intake-Protokoll und Dokumentenliste. |
| `lobbyregister-kommandocenter` | Master-Routing für Lobbyregister-Mandate: Pflichtcheck, Registrierung, Aktualisierung, Verhaltenskodex, Meldung, Sanktion, Unterlagen und naechster Skill. Normen LobbyRG §§ 1 bis 7. Output Mandatskarte, Routing und Qualitaetsgate. |

## Arbeitsweg

Im Plugin Lobbyregister Bundestag gilt für **Intake Mandat Lobbyregister**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lobbyregister-intake-mandat`

**Fokus:** Erfasst Ausgangslage, Organisation, Kontaktplaene, Auftraggeber, Fristen und Portalstatus vor jeder Lobbyregister-Prüfung. Nutzt LobbyRG §§ 1 bis 5 und Bundestags-Handbuch. Output Intake-Protokoll und Dokumentenliste.

# Mandats- und Projekt-Intake

## Einsatz

Einen vollstaendigen Intake fuer neue oder bestehende Registerprojekte bauen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche geplanten oder laufenden Kontakte gibt es?
2. Welche Regelungsvorhaben, Stellungnahmen oder Gutachten liegen vor?
3. Welche Registereintraege, Portalrollen und Freigaben bestehen bereits?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Intake-Protokoll mit Faktenstand, Dokumentenanforderung, Risikofragen und Verantwortlichkeiten.

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

## 2. `lobbyregister-kommandocenter`

**Fokus:** Master-Routing für Lobbyregister-Mandate: Pflichtcheck, Registrierung, Aktualisierung, Verhaltenskodex, Meldung, Sanktion, Unterlagen und naechster Skill. Normen LobbyRG §§ 1 bis 7. Output Mandatskarte, Routing und Qualitaetsgate.

# Lobbyregister-Kommandocenter

## Einsatz

Mandat starten, Ziel klaeren und den passendes Fachmodul auswaehlen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wer will handeln: Einzelperson, Unternehmen, Verband, Netzwerk, Agentur oder Auftraggeber?
2. Gegen wen richtet sich die Interessenvertretung: Bundestag, Bundesregierung oder beide?
3. Geht es um Erstregistrierung, Aktualisierung, Regelungsvorhaben, Stellungnahme, Beschwerde oder Bussgeld?

## Routing

| Lage | Naechster Skill |
|---|---|
| Unklar, ob LobbyRG ueberhaupt greift | `interessenvertretung-begriff` |
| Kontaktperson oder Stelle unklar | `adressatenkreis-bundestag-bundesregierung` |
| Registrierungspflicht fraglich | `registrierungspflicht-schwellen` |
| Ausnahme moeglich | `ausnahmen-bundestag` oder `ausnahmen-bundesregierung` |
| Neue Registrierung | `erstregistrierung-ausfuellen` |
| Bestehender Eintrag mit Aenderung | `aktualisierung-unverzueglich` |
| Jahrespruefung | `geschaeftsjahresaktualisierung` |
| Regelungsvorhaben oder Stellungnahme | `regelungsvorhaben-erfassen` oder `stellungnahmen-gutachten-upload` |
| Auftrag fuer Dritte | `auftraggeber-ermitteln` und `unterauftragnehmer-erfassen` |
| Finanzdaten | `finanzaufwendungen-berechnen` bis `jahresabschluss-rechenschaftsbericht` |
| Kontaktverhalten | `verhaltenskodex-integritaet` und `erstkontakt-offenlegung` |
| Verstoß melden oder verteidigen | `verstoesse-melden` oder `bussgeld-und-pruefverfahren` |

## Standard-Mandatskarte

```
LOBBYREGISTER-MANDATSKARTE
Stand: [DATUM]
Organisation/Person: [NAME]
Rolle: [eigene Interessenvertretung / Auftrag fuer Dritte / Unterauftrag]
Adressaten: [Bundestag / Bundesregierung / beides / unklar]
Kontaktstatus: [geplant / laufend / abgeschlossen]
Pflichtampel: [ROT Registrierung noetig / ORANGE pruefen / GRUEN derzeit keine Pflicht]
Naechster Skill: [SKILL]
Sofortfrist: [DATUM ODER KEINE]
Fehlende Unterlagen: [LISTE]
Freigabe durch: [PERSON/FUNKTION]
```

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Mandatskarte mit Ampel, Routing-Tabelle, offenen Nachweisen und naechstem Arbeitsschritt.

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
