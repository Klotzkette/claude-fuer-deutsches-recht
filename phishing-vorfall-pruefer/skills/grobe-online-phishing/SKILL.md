---
name: grobe-online-phishing
description: "Grobe Online Phishing: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Grobe Online Phishing

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Grobe Online Phishing** im Plugin Phishing-Vorfall. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-grobe-formular-portal-und-einreichung` | Grobe: Formular, Portal und Einreichungslogik im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-online-risikoampel-und-gegenargumente` | Online: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-phishing-tatbestand-beweis-und-belege` | Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Phishing-Vorfall gilt für **Grobe Online Phishing**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-grobe-formular-portal-und-einreichung`

**Fokus:** Grobe: Formular, Portal und Einreichungslogik im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Grobe: Formular, Portal und Einreichungslogik

## Spezialwissen: Grobe: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Grobe: Formular, Portal und Einreichungslogik / grobe formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Grobe Fahrlässigkeit Phishing** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Grobe Fahrlässigkeit Kunde § 675v Abs. 3 BGB — Substanziierungslast
- **Definition grobe Fahrlässigkeit:** Verletzung der im Verkehr erforderlichen Sorgfalt in besonders schwerem Maße, naheliegende Überlegungen werden nicht angestellt.
- **Beweislast:** Bank (§ 675w S. 4 BGB), die Behauptung allein genügt nicht.
- **Typische "grobe Fahrlässigkeit"-Argumente der Bank — und Gegenargumente:**
 - "Kunde klickte auf Link in Phishing-Mail" — laut BGH XI ZR 91/14 (26.01.2016) reicht das *nicht*, sofern Mail täuschend echt war.
 - "Kunde gab PIN/TAN über Anruf weiter" — kommt auf Vortäuschungsqualität an; Call-ID-Spoofing kann nicht-grob fahrlässig sein.
 - "Kunde gab mehrere TANs" — könnte grobe Fahrlässigkeit nahelegen, wenn typische Bankhinweise ignoriert wurden.
 - "Kunde hat AGB-Warnhinweise ignoriert" — nur, wenn diese verständlich, prominent und konkret waren.

## Bank-Formularwege Reklamation
- **Bankenformulare**: oft "Reklamation nicht autorisierte Zahlung" oder "Schadensanzeige"; alle Banken haben eigene Formulare/Online-Portale.
- **Schlichtungsantrag:** Webformular der zuständigen Schlichtungsstelle (Bundesbank, Bankenverband-Ombudsmann, DSGV-Schlichter, BVR-Schlichter).
- **BaFin-Beschwerde:** über bafin.de — keine direkten Anspruchsdurchsetzung, aber aufsichtsrechtliche Hebelwirkung.

## Praxis-Tipp
Bei "grobe Fahrlässigkeit"-Streit auf Bankspezifika der Nutzerführung achten: Wurde der Kunde durch täuschend echte App- oder Webseite getäuscht? Hat die Bank-App keine Anti-Phishing-Warnung? War der TAN-Bestätigungsdialog ausreichend deutlich? Beweisanforderungen verschieben sich zunehmend zugunsten des Kunden, wenn die Bank die Erkennung nicht aktiv unterstützt.

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

## 2. `spezial-online-risikoampel-und-gegenargumente`

**Fokus:** Online: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Online: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Online: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Online: Risikoampel, Gegenargumente und Verteidigungslinien / online risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Online-Banking Phishing** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Risikoampel Online-Banking Phishing
- **Rot (Mandantengefahr):**
 - 13-Monats-Frist § 676b Abs. 2 BGB läuft ab.
 - Bank hat Erstattung verweigert ohne Beweis für Autorisierung.
 - Großer Schaden (> 10.000 EUR), keine Beweissicherung erfolgt.
 - Strafanzeige fehlt — spätere Strafverfolgung erschwert.
- **Gelb:**
 - Mitverschulden des Kunden möglich (mehrere TANs freigegeben, AGB-Warnhinweise sichtbar).
 - Beweissicherung lückenhaft (kein E-Mail-Header, keine Screenshots).
 - Schlichtungsweg noch nicht ausgeschöpft.
- **Grün:**
 - Anzeige bei Bank rechtzeitig + Strafanzeige bei Polizei mit Az.
 - Beweise gesichert (Mail-Header, Banking-Logs, Konto-Auszug).
 - Schlichtung läuft mit klarer Sachlage zugunsten Kunde.

## Gegenargumente Bank
1. **"Kunde war grob fahrlässig":** Beweislast Bank (§ 675w S. 4 BGB); BGH XI ZR 91/14 (26.01.2016) verlangt sorgfältige Einzelfallprüfung.
2. **"Wir haben starke Kundenauthentifizierung":** § 1 Abs. 24 ZAG-Konformität konkret nachweisen.
3. **"AGB schließen Haftung aus":** AGB-Inhaltskontrolle §§ 305 ff., § 675e BGB (Abweichungsverbot).
4. **"Frist 13 Monate verstrichen":** wenn Anzeige rechtzeitig erfolgte, greift Ausschluss nicht.

## Verteidigungslinien Kunde
- Konzentration auf Beweislast-Umkehr § 675w BGB.
- SCA-Mangel als Trumpfkarte: bei fehlender starker Authentifizierung greift § 675v Abs. 4 — Haftung Kunde **0 EUR** (außer Vorsatz/grobe Fahrlässigkeit).
- BGH-Rspr. mit Datum und Az. konkret zitieren, nicht pauschal.

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

## 3. `spezial-phishing-tatbestand-beweis-und-belege`

**Fokus:** Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin phishing vorfall pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage / phishing tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Phishing-Vorfall** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Phishing — Tatbestände und Beweisfragen
- **Zivilrechtlich §§ 675u, 675v BGB:** Nicht autorisierter Zahlungsvorgang vs. autorisierter unter Täuschung.
 - **Beweislast Bank:** Authentifizierung, ordnungsgemäße Aufzeichnung, korrekte Buchung (§ 675w BGB).
 - **Beweislast Kunde:** keine — Bank trägt; Kunde muss nur Nichtautorisierung anzeigen.
 - **Grobe Fahrlässigkeit § 675v Abs. 3:** Beweislast Bank.
- **Strafrechtlich:**
 - **§ 263a StGB Computerbetrug:** unbefugte Verwendung von Daten, Vermögensschaden.
 - **§ 269 StGB:** Fälschung beweiserheblicher Daten.
 - **§ 202a/202b/202c StGB:** Ausspähen, Abfangen, Vorbereiten.
- **Belege:** E-Mail-Header (DKIM, SPF, Return-Path, Received-Chain), IP-Logs, Banking-Session-Log, Screenshot des Anmeldeprozesses, ggf. App-Log.

## Beweissicherung Tag 1
- E-Mail-Original mit allen Headern (.eml / .msg).
- Screenshots: Phishing-Seite, Banking-Oberfläche, TAN-Aufforderung, Konfirmation der Überweisung.
- Bank-Login-Protokoll (IP, Device, Browser, Zeit) — bei Bank anfordern.
- Telefonprotokoll bei Call-ID-Spoofing (Voicemail, Anrufliste, Rückrufnummer).
- Strafanzeige-Aktenzeichen für späteren Akteneinsichtantrag § 406e StPO.

## Praxis-Tipp
Bei BGH-Az.-Zitaten Phishing immer mit Vorsicht: BGH XI ZR 91/14 (26.01.2016) ist anerkannt für "Klick allein nicht grob fahrlässig". Spätere Entscheidungen variieren je nach SCA-Verfahren (push-TAN, smsTAN, App-TAN) — kontextuell prüfen.

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
