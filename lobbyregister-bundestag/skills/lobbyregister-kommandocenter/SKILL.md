---
name: lobbyregister-kommandocenter
description: "Für Lobbyregister-Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck."
---

# Lobbyregister-Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 3 LobbyRG Eintragung vor erster Interessenvertretung, § 5 LobbyRG jährliche Aktualisierung, Berichtspflicht ggf. innerhalb 3 Monaten nach Ende des Geschäftsjahres.
- Tragende Normen verifizieren: LobbyRG §§ 1, 2, 3, 5, 6, 7, 8 (i.d.F. Reform 2024), Verhaltenskodex Lobbyregister, GOBT, BGleiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Interessenvertreter, Bundestagsverwaltung (Lobbyregisterstelle), Geschäftsstelle, registrierte Verbände, Bundesregierung (zweiter Registerteil).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lobbyregistereintrag, Verhaltenskodex-Bestätigung, Tätigkeitsbericht, Hausausweisantrag, Finanzangaben, Verbandsmitgliederliste — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
| Ausnahme möglich | `ausnahmen-bundestag` oder `ausnahmen-bundesregierung` |
| Neue Registrierung | `erstregistrierung-ausfuellen` |
| Bestehender Eintrag mit Aenderung | `aktualisierung-unverzueglich` |
| Jahrespruefung | `geschaeftsjahresaktualisierung` |
| Regelungsvorhaben oder Stellungnahme | `regelungsvorhaben-erfassen` oder `stellungnahmen-gutachten-upload` |
| Auftrag für Dritte | `auftraggeber-ermitteln` und `unterauftragnehmer-erfassen` |
| Finanzdaten | `finanzaufwendungen-berechnen` bis `jahresabschluss-rechenschaftsbericht` |
| Kontaktverhalten | `verhaltenskodex-integritaet` und `erstkontakt-offenlegung` |
| Verstoß melden oder verteidigen | `verstoesse-melden` oder `bussgeld-und-pruefverfahren` |

## Standard-Mandatskarte

```
LOBBYREGISTER-MANDATSKARTE
Stand: [DATUM]
Organisation/Person: [NAME]
Rolle: [eigene Interessenvertretung / Auftrag für Dritte / Unterauftrag]
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
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-für-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Lobbyregisterrecht:** Wer kontrolliert wen, wer schuldet wem etwas und welche Zustimmung fehlt?

**Erste Ansicht:** Zeige Beteiligte und Beziehungen als beschriftetes Schaubild. Trenne Kapital, Stimmrechte, Organstellung, Vollmacht, Forderung und wirtschaftliche Zuordnung; erläutere jede verwendete Kante.

**Sinnvolle Interaktion:** Eine Auswahl kann eine Partei oder Transaktion mit ihren Belegen zeigen. Ein veränderter Anteil oder eine alternative Struktur erzeugt eine gesonderte Variante; Kontrolle, Zuständigkeit oder Rechtsfolge werden nicht allein aus einer Prozentzahl abgeleitet.

**Datengrundlage:** Rechtsträger, Rolle, Anteil oder Anspruch, maßgeblicher Zeitpunkt, Beziehungstyp und Urkundenbeleg. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** begründete Strukturentscheidung und die beauftragten Beschluss-, Vertrags- oder Meldetexte. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
