---
name: rollen-und-modus-wahl
description: "Für Rollen- und Moduswahl vor der Zeugnisprüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Rollen- und Moduswahl vor der Zeugnispruefung

Bevor ein einziger Satz des Zeugnisses bewertet wird, legt der Pruefer die Rolle und den Ausgabemodus fest. Beide Entscheidungen bestimmen, welche Module ausgefuehrt werden und welche Schriftstuecke am Ende entstehen. Eine spaetere Kurskorrektur ist moeglich, wenn sich aus dem Zeugnis selbst Hinweise auf eine andere Rolle ergeben.

Die vier Hauptrollen sind: Arbeitnehmer oder Arbeitnehmerin (Standardfall, Rollenvermutung), Anwaltskanzlei auf Arbeitnehmerseite, Arbeitgeber oder Personalabteilung (HR-Gegenpruefer), und Betriebsrat oder neutrale Schulung. Die Rollenvermutung gilt, wenn keine anderslautende Angabe vorliegt: Der Einsender ist die beurteilte Person. Nur bei eindeutigen Hinweisen auf eine HR-, Kanzlei- oder Betriebsratsrolle wird davon abgewichen.

Im interaktiven Einsatz (Chat-Oberflaeche mit gesicherter Folge-Runde) liefert der Pruefer zuerst Analyse und Mandantenbericht und bietet Aufforderungsschreiben sowie Klagestrategie am Ende als Option an. Im nicht-interaktiven Einsatz (API, Agenten-SDK, Automatisierung, One-Shot-Aufruf) wird die Arbeit sofort rollenrichtig fertiggestellt: Vollanalyse, Mandantenbericht oder HR-Korrekturvermerk sowie bei Arbeitnehmerperspektive und vorhandenen Beanstandungen auch das Aufforderungsschreiben, alles in einer einzigen Antwort.

Ein Aufforderungsschreiben wird nur bei Arbeitnehmerperspektive und mindestens einem roten oder orangefarbenen Befund oder einem sonstigen Berichtigungspunkt erzeugt. Bei durchgehend unbedenklichem Zeugnis oder bei HR- und Arbeitgeberperspektive entfaellt es. Fehlende Platzhalter wie Name, Datum oder Kanzleibriefkopf werden klar gekennzeichnet und sind kein Blocker fuer die Ausgabe.
