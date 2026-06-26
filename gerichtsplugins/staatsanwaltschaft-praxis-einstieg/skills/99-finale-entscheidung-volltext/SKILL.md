---
name: 99-finale-entscheidung-volltext
description: Erzeugt Anklageschrift, Strafbefehlsantrag, Einstellungs- oder Abschlussverfügung als zeichnungsreifen staatsanwaltschaftlichen Volltext mit Tatvorwurf, Beweisstand, Verfügungssatz und Rechtsbehelfshinweis.
---

# Finale Entscheidung als Volltext (Abschlussverfügung Staatsanwaltschaft)

## Zweck

Dieser Skill erzeugt die staatsanwaltschaftliche Abschlussentscheidung nicht als bloßen Vorschlag, sondern als zeichnungsreifen Volltext. Er baut Anklageschrift, Strafbefehlsantrag, Einstellungsverfügung oder Abschlussverfügung mit Verfahrensdaten, Tatvorwurf, Beweisstand, rechtlicher Würdigung, Verfügungssatz, Nebenverfügungen und Rechtsbehelfshinweis.

Gegenstand: Abschlussverfügung im Ermittlungsverfahren (Anklage, Strafbefehl oder Einstellung).

## Rechtlicher Rahmen

Paragrafen 170, 153, 153a, 154, 154a StPO für Einstellungen; Paragraf 200 StPO für Anklageschrift; Paragraf 407 StPO für Strafbefehlsantrag.

## Eingangsvoraussetzungen

Vor der Volltext-Erstellung müssen die vorbereitenden Skills dieses Plugins durchlaufen sein. Insbesondere müssen vorliegen:

- Aktenzeichen, Beschuldigter, Tatzeit, Tatort und zuständiges Gericht;
- konkretisierter Tatvorwurf mit gesetzlichem Tatbestand;
- Beweismittelübersicht mit belastenden und entlastenden Punkten;
- geprüfte Verwertungs-, Belehrungs-, Zuständigkeits- und Eingriffsfragen;
- Entscheidungsspur: Nachermittlung, Einstellung, Strafbefehl, Anklage oder Sonderverfahren.

Fehlt eines dieser Stücke, weist der Skill darauf hin und unterbricht die Volltext-Erstellung, bevor er Phantasie produziert.

## Aufbau des Volltextes

### 1. Kopf und Verfahrensdaten

Staatsanwaltschaft, Aktenzeichen, Datum, Dezernat, Beschuldigter, Verteidiger, Tatvorwurf, Tatzeit, Tatort, zuständiges Gericht und aktueller Verfahrensstand.

### 2. Verfügungssatz oder Anklageformel

Die Entscheidung wird als staatsanwaltschaftliche Handlung formuliert: Anklageerhebung, Strafbefehlsantrag, Einstellung, Teileinstellung, Nachermittlung, Abgabe oder Vorlage. Beispiel für eine Einstellungsverfügung:

Verfügung: Das Verfahren gegen [Name] wegen [Tatvorwurf] wird gemäß Paragraf 170 Absatz 2 StPO eingestellt, weil ein hinreichender Tatverdacht nicht besteht. Der Beschuldigte ist hiervon zu unterrichten. Der Anzeigeerstatter ist gemäß Paragraf 171 StPO zu bescheiden mit Hinweis auf das Beschwerderecht nach Paragraf 172 StPO.

Der Verfügungssatz enthält zwingend: Entscheidung, Tatvorwurf, Beweismittelbezug, zuständiges Gericht oder Adressat und nächste Verfügung.

### 3. Tatvorwurf und Sachverhalt

Knappe, beweisnahe Darstellung des konkreten Tatgeschehens. Keine Lücken füllen, keine bloßen Wertungen. Zeit, Ort, Handlung, Erfolg, subjektive Seite und Beteiligungsform werden getrennt dargestellt.

### 4. Beweisstand und rechtliche Würdigung

Belastende und entlastende Beweismittel werden getrennt gewürdigt. Danach folgen Tatbestandsprüfung, Konkurrenzen, Verwertungsfragen, Zuständigkeit und Abschlussreife. Bei Strafbefehl oder Anklage muss der hinreichende Tatverdacht tragfähig begründet sein.

### 5. Nebenverfügungen

Wiedervorlage, Ladungen, Zustellungen, Mitteilungen an Verletzte, Einziehungs- oder Arrestfragen, Asservate, Registermitteilungen, Bewährungs- oder Vollstreckungshinweise und statistische Erledigung werden gesondert verfügt.

### 6. Rechtsbehelf, Beschwerde und Belehrung

Bei Einstellungs- und Beschwerdeentscheidungen werden Rechtsbehelf, Frist, Form und Adressat vollständig benannt. Bei Anklage und Strafbefehl wird die gerichtliche Anschlusslogik genannt.

### 7. Zeichnung

Ort, Datum, Dezernent, Amtsbezeichnung und gegebenenfalls Sichtvermerk oder Vorlagevermerk an Abteilungsleitung.

## Prozessuale Glanzkontrolle

Vor der finalen Verfügung wird zwingend geprüft:

1. Anfangsverdacht, hinreichender Tatverdacht oder Opportunitätsentscheidung sind sauber getrennt.
2. Eingriffe wie Durchsuchung, Beschlagnahme, Telekommunikationsdaten, U-Haft oder Vermögensarrest haben Norm, Tatsachenbasis, Verhältnismäßigkeit und Richtervorbehalt.
3. Entlastende Umstände sind sichtbar verarbeitet; die Verfügung denkt nicht nur belastend.
4. Beweisverwertungsfragen, Belehrungen, Rechtshilfe, digitale Spuren und Zufallsfunde sind als eigene Zeile geprüft.
5. Abschlussentscheidung passt zum Beweisstand: Nachermittlung, Einstellung, Strafbefehl, Anklage, Beschleunigtes Verfahren oder Rechtsmittel.
6. Rechtsprechungsanker: BVerfG, 20.02.2001 - 2 BvR 1444/00 für Durchsuchung und Gefahr im Verzug; BVerfG, 19.03.2013 - 2 BvR 2628/10 für Verständigung und Dokumentation; EuGH, 30.04.2024 - C-670/22 für importierte Kommunikationsdaten.

## Format und Stil

- Echte Umlaute in der Prosa; Umschrift nur in Slugs und technischen Dateinamen.
- Sachlich, knapp, in deutscher Gerichtssprache.
- Generisches Maskulinum.
- Paragrafenzeichen ausgeschrieben als „Paragraf".
- Aktenzeichen Punkt- oder Schrägstrich-Stil, niemals Komma.
- Keine Doppelsterne für Fettschrift im Fließtext.

## Ergebnis

Ein vollständiger, zeichnungsreifer staatsanwaltschaftlicher Volltext, der von Verfahrensdaten bis Zeichnung alles enthält. Der Dezernent kann ihn verwenden oder vor Zeichnung redaktionell prüfen. Offene Lücken werden nicht überspielt, sondern in eckigen Klammern markiert und am Ende in einer Lückenliste zusammengefasst.

## Eigenkontrolle

Bevor der Volltext freigegeben wird, durchläuft der Skill eine Eigenkontrolle:

1. Passt die Abschlussentscheidung zum Beweisstand?
2. Sind belastende und entlastende Umstände sichtbar verarbeitet?
3. Sind Zuständigkeit, Verwertbarkeit, Belehrung und Eingriffsgrundlagen geprüft?
4. Sind Tatzeit, Tatort, Tatvorwurf, Normen und Beweismittel widerspruchsfrei?
5. Sind Rechtsbehelf, Anschlussverfügung und Wiedervorlage vollständig?
6. Sind alle Lückenpunkte explizit markiert?

Erst nach bestandener Eigenkontrolle wird der Volltext als zeichnungsreif ausgegeben.
