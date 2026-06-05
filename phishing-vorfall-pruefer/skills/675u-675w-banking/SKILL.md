---
name: 675u-675w-banking
description: "675u 675w Banking: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# 675u 675w Banking

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **675u 675w Banking** im Plugin Phishing-Vorfall. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-675u-verhandlung-vergleich-und-eskalation` | 675U: Verhandlung, Vergleich und Eskalation im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-675w-zahlen-schwellen-und-berechnung` | 675W: Zahlen, Schwellenwerte und Berechnung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-banking-behoerden-gericht-und-registerweg` | Banking: Behörden-, Gerichts- oder Registerweg im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Phishing-Vorfall gilt für **675u 675w Banking**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-675u-verhandlung-vergleich-und-eskalation`

**Fokus:** 675U: Verhandlung, Vergleich und Eskalation im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# 675U: Verhandlung, Vergleich und Eskalation

## Spezialwissen: 675U: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** 675U: Verhandlung, Vergleich und Eskalation / 675u verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **§ 675u BGB** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## § 675u BGB im Kern
Bei einer nicht autorisierten Zahlung hat der Zahlungsdienstleister gegenüber dem Zahler keinen Anspruch auf Erstattung der Aufwendungen und ist verpflichtet, dem Zahler den Betrag **unverzüglich, spätestens bis zum Ende des folgenden Geschäftstags** zu erstatten und das Zahlungskonto wieder auf den Stand vor der nicht autorisierten Zahlung zu bringen.

Voraussetzung: Anzeige der Nichtautorisierung durch den Zahler unverzüglich nach Feststellung, spätestens **13 Monate** nach Belastung (§ 676b Abs. 2 BGB).

## Verhandlungsposition gegenüber Bank
- **Anker**: § 675u BGB stellt die Erstattung in den Mittelpunkt; § 675v BGB ist die Ausnahme (Schadensersatz wegen grober Fahrlässigkeit oder Vorsatz).
- **Beweislast nach § 675w BGB**: Die Bank muss nachweisen, dass das Zahlungsinstrument authentifiziert, ordnungsgemäß aufgezeichnet und nicht durch eine Störung beeinträchtigt war. Bloße Nutzung des Sicherungsverfahrens reicht **nicht** als Anscheinsbeweis grober Fahrlässigkeit (BGH XI ZR 91/14, Urteil vom 26.01.2016).
- **Hilfsweise**: § 675v Abs. 3 BGB — Haftungsbegrenzung 50 EUR bei Verlust, Diebstahl oder sonstigem Abhandenkommen, wenn nicht grob fahrlässig.

## Eskalationsstufen
1. **Außergerichtliche Korrespondenz**: Erstattungsforderung mit Fristsetzung 14 Tage; § 286 BGB-Verzug ab Ablauf.
2. **Bankenombudsmann** (BdB, BVR, DSGV, VÖB): kostenlos für Verbraucher, bei Streitwert bis 10.000 EUR bindend für Bank (privater Bankensektor) — siehe jeweilige Schlichtungsordnung.
3. **Schlichtung Deutsche Bundesbank** (§ 14 UKlaG i. V. m. ZAG): wenn keine eigene Schlichtungsstelle.
4. **Klage**: Amtsgericht bis 5.000 EUR, sonst Landgericht; Streitverkündung Strafanzeige unabhängig fortführen.

## Vergleichshebel
- **Sicherungspflicht der Bank** nach Art. 97 PSD2 (umgesetzt in § 55 ZAG): starke Kundenauthentifizierung — bei deren Fehlen Haftung der Bank verschärft.
- **Schwachstelle pushTAN/Phishing**: BGH-Rechtsprechung hat den Anscheinsbeweis grober Fahrlässigkeit erheblich eingeschränkt; Banken setzen häufig auf Quotenvergleiche (50-70 % Erstattung) statt vollständiger Verteidigung.

## Trade-off
Vergleich vor Schlichtung spart Zeit, opfert aber häufig 20-30 % der Erstattung. Bei klarer Beweislage (kein Vorsatz, keine grobe Fahrlässigkeit) ist Schlichtungsverfahren regelmäßig die wirtschaftlichere Option, da kostenfrei und ohne Vertretungspflicht.

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

## 2. `spezial-675w-zahlen-schwellen-und-berechnung`

**Fokus:** 675W: Zahlen, Schwellenwerte und Berechnung im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# 675W: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: 675W: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** 675W: Zahlen, Schwellenwerte und Berechnung / 675w zahlen schwellen und berechnung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **§ 675w BGB** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Zahlen, Schwellen und Berechnung Phishing-Vorfall
- **§ 675u BGB:** Erstattungsanspruch — unverzüglich, spätestens am nächsten Geschäftstag nach Anzeige.
- **§ 675v Abs. 3 BGB:** bei grober Fahrlässigkeit Kunde haftet voll (vorher Begrenzung auf 50 EUR nach altem Recht abgeschafft seit 2018).
- **§ 675v Abs. 4 BGB:** Haftung Kunde **0 EUR**, wenn starke Kundenauthentifizierung nach § 1 Abs. 24 ZAG nicht durchgesetzt wurde (Ausnahme: arglistig oder grob fahrlässig).
- **§ 675w BGB Beweislast:** **Bank** muss Authentifizierung, ordnungsgemäße Aufzeichnung, korrekte Buchung beweisen.
- **§ 676b Abs. 2 BGB:** Anzeigefrist **13 Monate** nach Belastung (Ausschlussfrist).
- **Schlichtungswert Verbraucherschlichtungsstelle Bank**: bis 10.000 EUR (Bankenschlichter), höher zivilrechtlich.
- **Verjährung Schadensersatz**: Regelfrist 3 Jahre § 195 BGB.

## Praxis-Tipp
Der häufigste Fehler bei Beratung: die Bank pauschal des "groben Verschuldens" zu bezichtigen. Die Beweislast für **starke Kundenauthentifizierung** (§ 1 Abs. 24 ZAG: Wissen + Besitz + Inhärenz) trägt die Bank — wenn diese den Authentifizierungsnachweis nicht klar führen kann, gewinnt der Kunde § 675u BGB.

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

## 3. `spezial-banking-behoerden-gericht-und-registerweg`

**Fokus:** Banking: Behörden-, Gerichts- oder Registerweg im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Banking: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Banking: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Banking: Behörden-, Gerichts- oder Registerweg / banking behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Banking-Phishing** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Banking-Behördenwege bei Phishing
- **Bank selbst:** Rückerstattungsantrag § 675u BGB → Beschwerdeabteilung der Bank.
- **Schlichtungsstellen Bank-Sparkassen:**
 - **Schlichtungsstelle bei der Deutschen Bundesbank** (für nicht in privaten Schlichtungsstellen erfasste Banken): bundesbank.de/schlichtungsstelle.
 - **Ombudsmann der privaten Banken** (Bankenverband): bankenombudsmann.de.
 - **Ombudsmann der öffentlichen Banken** (VöB).
 - **Schlichter der Sparkassen** (DSGV) und **Schlichter der Genossenschaftsbanken** (BVR).
- **BaFin:** bafin.de — Beschwerde bei groben Bankpflichtverletzungen; keine Rückerstattung, aber aufsichtsrechtliche Wirkung.
- **Polizei / Staatsanwaltschaft:** Strafanzeige wegen §§ 263a, 269 StGB; Aktenzeichen für spätere Akteneinsicht § 406e StPO.
- **DSB / Aufsichtsbehörde:** bei Datenlecks (Art. 33 DSGVO).
- **Zivilgericht:** AG bei Streitwert <= 5.000 EUR, LG > 5.000 EUR; ggf. § 29c ZPO Wohnsitz Verbraucher.

## Praxis-Tipp
Schlichtungsverfahren laufen oft schnell (3-6 Monate), sind regelmäßig kostenfrei für Verbraucher und werden von Banken ernst genommen — auch ohne Vergleichsdruck steigt die Erstattungsquote. Bei klarer Sachlage (nicht autorisiert, SCA-Mangel) ist Schlichtung der pragmatische Erstweg vor Klage.

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
