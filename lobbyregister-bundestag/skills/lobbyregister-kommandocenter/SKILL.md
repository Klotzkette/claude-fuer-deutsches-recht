---
name: lobbyregister-kommandocenter
description: "Master-Routing für Lobbyregister-Mandate: Pflichtcheck, Registrierung, Aktualisierung, Verhaltenskodex, Meldung, Sanktion, Unterlagen und naechster Skill. Normen LobbyRG §§ 1 bis 7. Output Mandatskarte, Routing und Qualitaetsgate."
---

# Lobbyregister-Kommandocenter

## Einsatz

Mandat starten, Ziel klaeren und den richtigen Spezial-Skill auswaehlen.

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
