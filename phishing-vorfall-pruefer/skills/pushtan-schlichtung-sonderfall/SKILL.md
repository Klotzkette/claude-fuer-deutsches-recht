---
name: pushtan-schlichtung-sonderfall
description: "Pushtan Schlichtung Sonderfall: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pushtan Schlichtung Sonderfall

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pushtan Schlichtung Sonderfall** im Plugin Phishing-Vorfall. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-pruefer-dokumentenmatrix-und-lueckenliste` | Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-pushtan-compliance-dokumentation-und-akte` | Pushtan: Compliance-Dokumentation und Aktenvermerk im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-schlichtung-sonderfall-und-edge-case` | Schlichtung: Sonderfall und Edge-Case-Prüfung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Phishing-Vorfall gilt für **Pushtan Schlichtung Sonderfall**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-pruefer-dokumentenmatrix-und-lueckenliste`

**Fokus:** Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung / pruefer dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB §§ 675u, 675v, 675w, 280; ZAG/PSD2, künftig PSD3/PSR beobachten; DSGVO Art. 33, 34; StGB §§ 263, 263a, 202a, 269; Bank-AGB, Authentifizierungsprotokolle und Ombudsmannregeln.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Pruefer** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-pushtan-compliance-dokumentation-und-akte`

**Fokus:** Pushtan: Compliance-Dokumentation und Aktenvermerk im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Pushtan: Compliance-Dokumentation und Aktenvermerk

## Spezialwissen: Pushtan: Compliance-Dokumentation und Aktenvermerk
- **Spezialgegenstand:** Pushtan: Compliance-Dokumentation und Aktenvermerk / pushtan compliance dokumentation und akte. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB §§ 675u, 675v, 675w, 280; ZAG/PSD2, künftig PSD3/PSR beobachten; DSGVO Art. 33, 34; StGB §§ 263, 263a, 202a, 269; Bank-AGB, Authentifizierungsprotokolle und Ombudsmannregeln.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-schlichtung-sonderfall-und-edge-case`

**Fokus:** Schlichtung: Sonderfall und Edge-Case-Prüfung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Schlichtung: Sonderfall und Edge-Case-Prüfung

## Spezialwissen: Schlichtung: Sonderfall und Edge-Case-Prüfung
- **Spezialgegenstand:** Schlichtung: Sonderfall und Edge-Case-Prüfung / schlichtung sonderfall und edge case. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB §§ 675u, 675v, 675w, 280; ZAG/PSD2, künftig PSD3/PSR beobachten; DSGVO Art. 33, 34; StGB §§ 263, 263a, 202a, 269; Bank-AGB, Authentifizierungsprotokolle und Ombudsmannregeln.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Schlichtung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
