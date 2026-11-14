---
name: 24-raeumungsklage-erstellen
description: "Leadskill für Räumungsklage Wohnraum nach Kündigung. Wohnung räumen und herausgeben, Kombiklage mit Zahlung, Kündigungszustellung, Sozialwiderspruch, Räumungsstreitwert, Zahlung vor Zustellung und Schonfrist nach Rechtshängigkeit prüfen. Output Klage."
---

# Räumungsklage Wohnraum

## Zweck und Anwendungsfall

Dieser Skill ist der Leadskill für Räumungsklagen und Kombiklagen aus Zahlung und Räumung. Anwendungsfall ist die wirksame Kündigung mit fortbestehendem Rückstand oder sonstigem Räumungsgrund. Skill 20 liefert bei Bedarf den Zahlungsbaustein, führt aber nicht den Kombiprozess.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Mietvertrag, Mietkonto, Mahnungen und Kündigung mit Zustellnachweis.
- Aktueller Kontoauszug zum Klagezeitpunkt.
- Hinweise auf etwaige Härtegründe oder einen Widerspruch nach Paragraf 574 BGB.
- Bei Pflichtverletzung oder sonstigem Räumungsgrund außerhalb des Zahlungsverzugs: Abmahnung, Untervermietungsdaten, Eigenbedarfsgrund, freie Alternativwohnungen, Untermietzins, Erlaubnislage und Belege.

## Ablauf / Checkliste

1. Räumungsantrag ausformulieren:

```
Der Beklagte wird verurteilt, die Wohnung
Wilhelmstraße 14, 10963 Berlin,
3. Obergeschoss links,
bestehend aus 3 Zimmern, Küche, Bad, WC und Diele,
zu räumen und an die Klägerin herauszugeben.
```

2. Kombiklage führen: Zahlungs- und Räumungsklage zusammen, hilfsweise ordentliche Kündigung mitgeltend machen; Anträge und Streitwerte für Zahlung und Räumung getrennt ausweisen.
3. Streitwert ansetzen: Räumung Wohnraum nach Paragraf 41 Abs. 2 GKG mit einer Jahresnettomiete.
4. Sachvortrag aufbauen: Mietverhältnis (Vertrag K1); Pflichtverletzung Verzug (Konto K2); Mahnungen (K3, K4); Kündigung mit Zustellnachweis (K5); aktueller Kontoauszug zum Klagezeitpunkt mit Hinweis auf die spätere Schonfristprüfung. Bei Untervermietung Erlaubnislage, Abmahnung, Drittgebrauch, Untermietzins, wohnungsbezogene Aufwendungen und einen erst darüber hinausgehenden Gewinnanteil darstellen; BGH VIII ZR 228/23 schützt das Kostensenkungsinteresse, nicht den Gewinnüberschuss. Bei Eigenbedarf Bedarfsperson, Nutzungswunsch, Ernsthaftigkeit, Wohnbedarf, Zeitplan und jede freie Alternativwohnung des Vermieters erfassen. Nach BGH VIII ZR 289/23 kann eine ohne wesentliche Abstriche geeignete freie Wohnung für die Rechtsmissbrauchsprüfung erheblich sein; das ist von einer bloßen Anbietpflicht zu trennen.
5. Sozialklausel-Risiko prüfen: Im Sachvortrag und in der Risikoanlage prüfen, ob der Mieter Widerspruch nach Paragraf 574 BGB erhoben hat oder Härtegründe erkennbar sind; wenn ja, Skill `16-widerspruch-mieter-pruefen` einbeziehen. Bei Suizidgefahr, schwerer Krankheit, hohem Alter oder Ersatzwohnungsangebot BGH VIII ZR 390/21, VIII ZR 270/22, VIII ZR 262/24, VIII ZR 17/25 und VIII ZR 277/25 als Warnanker nutzen. Bei substantiierten schweren Umzugsfolgen Vortrag, Behandlerunterlagen, Bestreiten und Sachverständigenfragen trennen; nach VIII ZR 277/25 beim Bestreiten auch eine Gutachteneinholung von Amts wegen nach Paragraf 144 ZPO einplanen. Nicht ohne RA-Freigabe in eine Standardräumung gehen.
6. Wenn nach Einreichung Zahlung, Aufrechnung oder ein sonstiges erledigendes Ereignis eintritt, Zeitpunkt trennen: vor Zustellung die Chronologie in Skill `05-chronologie-fallakte` fortschreiben und den Kostenpfad über Skills `11` und `37` prüfen; bei nötiger Antragsumstellung führt Skill `38`. Nach Zustellung/Rechtshängigkeit bei vollständiger Befriedigung zusätzlich Skill `27-schonfristzahlung-erkennen`. Skill `23` wird erst wieder für das fachlich geklärte geänderte Einreichungspaket genutzt und entscheidet dabei zwischen Kanzlei/beA und Eigenvertretung/eBO oder zulässiger schriftlicher Einreichung.
7. Nutzungsentschädigung nach Ende des Mietverhältnisses nicht automatisch aus bloßem Besitz ableiten: Nach BGH VIII ZR 291/23 Vorenthalten, Rückgabeunterlassen, entgegenstehenden Rückerlangungswillen und tatsächliche Nutzung getrennt prüfen.
8. Bei der Rückstands- und Verzugsdarstellung Wohnraummietzahlungen nicht allein nach SAP-Kontoeingang als verspätet behandeln. Sonnabend zählt für die Zahlungsfrist nicht; bei gedecktem Konto kann der rechtzeitige Überweisungsauftrag genügen. BGH VIII ZR 129/09, VIII ZR 291/09 und VIII ZR 222/15 prüfen.
9. Vor Einreichung Haftungsgate nach BGH VIII ZR 4/23: formelle Wirksamkeit, materieller Kündigungsgrund, Verschulden, Vertretungsmacht und Beweise getrennt prüfen. Eine schuldhaft materiell unberechtigte Kündigung kann bei kausalem Mieterschaden Ersatzansprüche auslösen; die bloße Prozessführung wird dagegen grundsätzlich über das Prozesskostenrecht abgewickelt.
10. Getrennte Freigabekarte erstellen: Gericht, Parteien, Wohnung, Räumungs- und Zahlungsantrag, Kündigungen, materieller Grund, Form, Zugang, aktueller Saldo, Zahlungsauftrag/Banklauf, Streitwerte, Härterisiken, Anlagen, Vorschuss, Einreichungsweg und Freigabeperson. Status bis zur dokumentierten Freigabe `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

## Argumentationsstandard

Die Klage führt fünf Tatsachenketten getrennt: Mietverhältnis und Wohnung, Pflichtverletzung, jede Kündigung mit eigenem Grund, Zugang bei allen Mietern sowie fortbestehender Besitz ohne Rückgabe. Zahlungs- und Räumungsantrag erhalten getrennte Anspruchs- und Beweisblöcke. Bei fristloser und ordentlicher Kündigung werden Tatbestand, Verschulden, Schonfristfolge und Sozialwiderspruch nicht in einer Sammelwürdigung vermengt. Für Substantiierung, Bestreiten und Beweisangebot gilt `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Jede juristische Aussage wird nach `references/zitierweise.md` belegt (Rechtsprechung vor Literatur, neueste zuerst). Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert; keine erfundenen Aktenzeichen. Für Untervermietung, Nutzungsentschädigung, Eigenbedarf, Schonfrist und Sozialklausel `references/gepruefte-bgh-anker-mietrecht.md` prüfen.

## Ausgabeformat

Getrennte interne Freigabekarte und Klageschrift Räumung mit allen Anlagen, getrenntem Zahlungs- und Räumungsstreitwert, aktuellem Mietkonto, Zustellnachweisen, Sozialwiderspruchsprüfung und Gerichtskostenvorschuss-Daten. Die Klageschrift wird in vollständigen, ausformulierten Sätzen im Urteilsstil geliefert; Stichwort-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht).

## Beispiele

- Fristlose und hilfsweise ordentliche Kündigung wegen Rückstands: Kombiklage auf Zahlung und Räumung mit getrennten Streitwerten.
- Erkennbare Härtegründe der Mieterin: Aufnahme der Sozialklausel-Prüfung in die Risikoanlage und Verweis auf Skill 16.
- Schonfristzahlung nach Klageeinreichung: Räumung, Zahlung und Kosten nicht vermischen.
