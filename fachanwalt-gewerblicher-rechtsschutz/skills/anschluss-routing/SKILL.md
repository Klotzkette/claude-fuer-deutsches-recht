---
name: anschluss-routing
description: "Wählt nach einer ersten Prüfung im gewerblichen Rechtsschutz den sachlich passenden Folgeskill. Trennt Schutzrecht, Rechtsbestand, Verletzung, Eilverfahren und Amtsweg und liefert eine begründete nächste Arbeitsstation statt einer unverbundenen Liste von Normen oder Entscheidungen."
---

# 1. Anschluss-Routing im gewerblichen Rechtsschutz

## 1.1 Startregel

Übernimm zuerst das bisherige Ergebnis samt bereits gebildeten Fundstellen. Erfasse bei neuen Unterlagen zunächst nur Dateiname, Datum, Absender, Schutzrecht und Verfahrensbezug; öffne höchstens die fünf Stücke, die Frist, Rechtsbestand, Verletzung oder Eilbedarf ändern können. Route nicht neu, wenn bereits ein verwertbares Arbeitsprodukt begonnen wurde, und öffne keine schon ausgewertete Datei erneut.

## 1.2 Pflichtweichen

1. Welches Schutzrecht trägt den Vorgang: Marke, Design, Patent, Gebrauchsmuster, Geschäftsgeheimnis, Urheberrecht oder Lauterkeitsrecht?
2. Geht es um Entstehung, Register, Rechtsbestand, Verletzung, Lizenz, Eilverfahren oder Vollstreckung?
3. Welche Frist läuft tatsächlich und aus welchem Dokument folgt sie?
4. Welche territoriale Ebene gilt: Deutschland, EU, EPÜ, internationale Registrierung oder Drittstaat?
5. Welches Arbeitsprodukt wird als Nächstes gebraucht?

## 1.3 Fachrouten

| Fallkern | Folgeskill | Warum |
| --- | --- | --- |
| Designanmeldung, DPMA, EUIPO oder Nichtigkeit | `designg-behoerden-gericht-und-registerweg` | trennt Amts- und Gerichtsweg sowie alten und neuen EU-Rechtsstand |
| Neuheit, Offenbarung oder Formenschatz | `design-neuheit-offenbarung-pruefen` | baut einen belegbaren Offenbarungskalender |
| Designverletzung | `designverletzung` | vergleicht Ansichten, Gesamteindruck und Einreden |
| Markenanmeldung oder Kollision | `markenanmeldung-dpma-und-euipo` oder der konkret passende Markenskill | verbindet Registerstand, Warenverzeichnis, Benutzung und Verwechslungsgefahr |
| Domainkonflikt | `domainrecht-loeschung-bgh-i-zr-138-19` | trennt Kennzeichenrecht, Namensrecht und Domainstatus |
| Abmahnung und einstweiliger Rechtsschutz | `abmahnung-formular-portal-und-einreichung` | sichert Anspruch, Dringlichkeit, Antrag und Zustellung |
| Unklare Akte | `einstieg-schnelltriage-fallrouting` | erzeugt Schutzrechts-, Fristen- und Belegmatrix |
| Qualitätskontrolle | `workflow-redteam-qualitygate` | prüft Gegenargument, Antrag, Beweis und Vollzug |

Wenn ein genannter Slug nicht vorhanden ist, wähle aus der aktuellen Skillübersicht den fachlich nächsten vorhandenen Skill und dokumentiere die Abweichung.

## 1.4 Verfahrenssicherung

1. Sichere amtlichen Registerauszug und angegriffene Entscheidung.
2. Berechne Fristen aus Zustellung und einschlägiger Verfahrensnorm; übernimm keine Frist aus einem anderen Schutzrecht.
3. Trenne Amt, Beschwerdekammer, Bundespatentgericht, Gericht der Europäischen Union und Verletzungsgericht.
4. Weise Entscheidungen nur der Aussage zu, die sie tatsächlich tragen. Eine bloße Aktenzeichenliste ist kein Routingkriterium.
5. Gib als Ergebnis genau einen Hauptskill und höchstens zwei notwendige Nebenspuren aus.

## 1.5 Ausgabe

Erstelle eine kurze Routingkarte mit Fallkern, Hauptskill, Frist, benötigten Unterlagen, erwartetem Arbeitsprodukt und einem Satz zur Auswahlentscheidung.
