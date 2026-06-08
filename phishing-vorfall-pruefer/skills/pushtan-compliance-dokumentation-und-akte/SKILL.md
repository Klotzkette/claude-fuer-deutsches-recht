---
name: pushtan-compliance-dokumentation-und-akte
description: "Pushtan: Compliance-Dokumentation und Aktenvermerk im Plugin phishing vorfall pruefer im Phishing Vorfall Pruefer."
---

# Pushtan: Compliance-Dokumentation und Aktenvermerk

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: § 675u; § 675v — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Pushtan: Compliance-Dokumentation und Aktenvermerk
- **Normen-/Quellenanker:** BGB §§ 675u, 675v, 675w, 280; ZAG/PSD2, künftig PSD3/PSR beobachten; DSGVO Art. 33, 34; StGB §§ 263, 263a, 202a, 269; Bank-AGB, Authentifizierungsprotokolle und Ombudsmannregeln.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **pushTAN** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## pushTAN-Verfahren technisch
pushTAN ist ein App-basiertes Authentifizierungsverfahren der Sparkassen / Volksbanken / Banken-eigenen Apps:
- Banking-App auf Endgerät A.
- pushTAN-App (oder integriertes Verfahren) auf demselben oder einem zweiten Endgerät.
- Transaktion wird vom Endgerät an die Bank gesendet; Bank pusht Bestätigungsanforderung an die pushTAN-App; Nutzer bestätigt mit PIN/Biometrie.

## Schwachstellen pushTAN
- **Same-Device-Risiko**: pushTAN-App und Banking-App auf demselben Smartphone → bei Malware-Befall beide kompromittierbar.
- **Visualisierung Empfänger/Betrag**: muss in pushTAN-App dargestellt werden — bei kompromittierten Anzeigen Manipulation möglich.
- **Social Engineering (Callcenter-Trick)**: Anrufer gibt sich als Bankmitarbeiter aus, lässt Kunden TAN bestätigen "um den Vorfall abzuwehren".
- **Phishing-Webseite**: leitet Eingaben in die echte Banking-Strecke; Kunde glaubt, eigene Transaktion zu autorisieren, autorisiert in Wahrheit Angreiferüberweisung.

## Dokumentationspflicht in der Akte
- **Tool-Beschreibung**: Welches pushTAN-Verfahren? Welche Version der App? Welche Endgeräte (gleiches/getrenntes)?
- **Beweismittelliste**: Screenshots der Banking-App im fraglichen Zeitraum, pushTAN-Verlauf, Geräte-Logs (soweit verfügbar), Telefon-Verbindungsnachweise, Phishing-Mail / SMS / Webseite.
- **Sachverhaltschronologie**: Minute für Minute der Angriff (Eingang Mail/Anruf, Klick, Eingabe, TAN-Bestätigung, Buchung, Entdeckung).
- **Kundenverhalten dokumentieren**: Wahrnehmung des Visualisierungstextes? Wurde Empfänger/Betrag in der TAN-App geprüft? Anzeichen für Druckaufbau (Eile, Drohung)?

## Pflichten Bank zu pushTAN
- **Starke Kundenauthentifizierung** § 55 ZAG (PSD2-Umsetzung): zwei unabhängige Elemente; bei Same-Device pushTAN ist die Unabhängigkeit fraglich — Anti-Fraud-Mechanismen zwingend.
- **Dynamische Verknüpfung** (Art. 5 Delegierte VO (EU) 2018/389): Authentifizierungs-Code dynamisch verknüpft mit Betrag und Empfänger; bei manipulierter Anzeige Pflichtverletzung.
- **Risikoanalyse** § 27 ZAG: laufende Anomalie-Erkennung.

## Akten-Output für Schlichtung/Klage
- Risikoampel pushTAN-Vorfall (rot/gelb/grün) mit Begründung.
- Pflichtenmatrix Bank (erfüllt/nicht erfüllt).
- Kundenmatrix § 675l BGB (verletzt/nicht verletzt).
- Konkretisierungsempfehlung Klage/Schlichtung.

## Trade-off
pushTAN ist faktisch mehrheitlich Same-Device — Banken werden in Verfahren regelmäßig zur Erstattung verurteilt, wenn Anomalie-Erkennung schwach und Visualisierung manipulierbar war. Live-Recherche aktueller OLG-Linien lohnt sich.

