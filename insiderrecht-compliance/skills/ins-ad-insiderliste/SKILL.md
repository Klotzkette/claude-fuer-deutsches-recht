---
name: ins-ad-insiderliste
description: "Ins 003 Ad Hoc Art17, Ins 005 Insiderliste Art18: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 003 Ad Hoc Art17, Ins 005 Insiderliste Art18

## Arbeitsbereich

Dieser Skill bündelt **Ins 003 Ad Hoc Art17, Ins 005 Insiderliste Art18** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-003-ad-hoc-art17` | Fuehrt durch die vollstaendige Ad-hoc-Pflicht nach Art. 17 MAR: Zeitpunkt, Inhalt, Verbreitung, Website, Sprachfassung, BaFin-Meldung und Dokumentation. |
| `ins-005-insiderliste-art18` | Erstellt und pflegt Insiderlisten nach Art. 18 MAR inklusive Format, Inhalt, Aktualisierungspflichten und BaFin-Uebermittlung. |

## Arbeitsweg

Für **Ins 003 Ad Hoc Art17, Ins 005 Insiderliste Art18** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-003-ad-hoc-art17`

**Fokus:** Fuehrt durch die vollstaendige Ad-hoc-Pflicht nach Art. 17 MAR: Zeitpunkt, Inhalt, Verbreitung, Website, Sprachfassung, BaFin-Meldung und Dokumentation.

# Ad-hoc-Publizität nach Art. 17 MAR

## Rechtlicher Rahmen

Art. 17 VO (EU) 596/2014 (MAR) verpflichtet Emittenten, Insiderinformationen so bald wie möglich
zu veröffentlichen. Die Pflicht ist ausgelöst, sobald eine Insiderinformation im Sinne von Art. 7
MAR vorliegt. Kein Ermessen beim „Ob" – Ermessen nur im Rahmen des Aufschubs nach Art. 17 Abs. 4
MAR. Inhalt, Verbreitung und Format richten sich nach Art. 2 DVO (EU) 2016/1055 und
§§ 48–50 WpHG.

Rechtsgrundlagen:
- Art. 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/1055 (Verbreitungsstandards): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1055
- §§ 48–50 WpHG: https://www.gesetze-im-internet.de/wphg/__48.html
- BaFin-Emittentenleitfaden Kap. VI: https://www.bafin.de/dok/8252648
- ESMA MAR-Guidelines: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill führt den Emittenten vollständig durch den Ad-hoc-Prozess: von der Entscheidung zur
Veröffentlichung bis zur rechtskonformen Dokumentation. Er deckt die Inhaltserfordernisse,
Verbreitungswege, Sprachversionen, BaFin-Meldung und die anschließende Website-Archivierung ab.

## Arbeitsprogramm

### Schritt 1 – Veröffentlichungspflicht bestätigen

- Wurde eine Insiderinformation nach Art. 7 MAR festgestellt (Skill ins-001)?
- Liegt kein wirksamer Aufschub nach Art. 17 Abs. 4 MAR vor oder ist er beendet?
- Wurde ein Leak oder eine Fehlinformation publiziert, die sofortige Veröffentlichung erfordert?
- Entscheid: Veröffentlichung unverzüglich (= ohne schuldhaftes Zögern, i. d. R. sofort).

### Schritt 2 – Entwurf der Ad-hoc-Mitteilung

Inhaltspflichten nach Art. 17 MAR und BaFin-Emittentenleitfaden:
- Überschrift: „Ad-hoc-Mitteilung gemäß Art. 17 Abs. 1 MAR"
- Datum und Uhrzeit der Entscheidung zur Veröffentlichung
- Vollständiger Emittentenname, LEI-Nummer, ISIN
- Genaue Beschreibung der Insiderinformation (Fakten, keine Werbung, keine Prognosen ohne Basis)
- Kursrelevanz-Einschätzung (falls enthalten: klar als solche kennzeichnen)
- Kein irreführender Inhalt, keine Vorab-Weichzeichnung
- Unterzeichner und Kontaktangaben für Rückfragen

### Schritt 3 – Verbreitung

- Übermittlung über ein zugelassenes Medienbündel (EQS Newswire / DGAP / äquivalent)
 gleichzeitig an alle Medien, die im EWR einen breiten Anlegerkreis erreichen (Art. 2 DVO 2016/1055)
- BaFin-Meldung gleichzeitig mit oder unmittelbar nach Veröffentlichung (§ 50 WpHG)
- Handelsplatz-Meldung an alle relevanten Börsen (XETRA, Regionalbörsen, ausländische Plätze)

### Schritt 4 – Website und Archivierung

- Veröffentlichung im Investor-Relations-Bereich der Emittenten-Website für mindestens 5 Jahre
- Deutliche Kennzeichnung als Ad-hoc-Mitteilung
- Nachweis von Datum und Uhrzeit der Website-Veröffentlichung dokumentieren

### Schritt 5 – Sprachfassung

- Amtssprache des Herkunftsmitgliedstaats (in Deutschland: Deutsch)
- Bei Dual-Listing: Landessprache des weiteren Handelsplatzes oder Englisch (Art. 20 MAR)
- Übersetzung darf den deutschen Originaltext nicht inhaltlich abweichen

### Schritt 6 – Dokumentation (Compliance-Akte)

- Board-/CFO-Freigabe mit Zeitstempel
- Entwurfshistorie und Freigabe-E-Mails
- Verbreitungsbestätigung (EQS/DGAP-Quittung)
- BaFin-Eingangsbestätigung
- Website-Screenshot mit Zeitstempel
- Handelsaussetzung / -wiederaufnahme dokumentieren, falls erfolgt

## Red-Team-Fragen

- Wurde zwischen dem Vorliegen der Insiderinformation und der Veröffentlichung unnötig gezögert?
- Enthält die Mitteilung alle Pflichtangaben laut BaFin-Emittentenleitfaden?
- Wurde die BaFin gleichzeitig informiert (nicht erst danach)?
- Sind alle relevanten Handelsplätze benachrichtigt?
- Wurde die korrekte Sprachfassung gewählt?
- Ist der Website-Nachweis (5-Jahres-Archiv) gesichert?
- Wurde ein eventueller Aufschub korrekt beendet und dokumentiert?
- Ist die Ad-hoc-Mitteilung sachlich korrekt und frei von Marketingsprache?
- Bei Aufhebung eines Aufschubs wegen Leak: Wurde der Hergang dokumentiert?

## Ausgabeformat

Erzeuge:
1. Ad-hoc-Mitteilungs-Entwurf (vollständiger Text, publikationsreif)
2. Checkliste Verbreitungsschritte mit Zeitstempel-Spalte
3. Compliance-Akte: Tabellarische Dokumentationsliste mit Status
4. Sprachversionen-Matrix bei Dual-Listing

Belege ausschließlich mit Quellen aus: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de,
curia.europa.eu, bgh.de, dejure.org, openjur.de.

## 2. `ins-005-insiderliste-art18`

**Fokus:** Erstellt und pflegt Insiderlisten nach Art. 18 MAR inklusive Format, Inhalt, Aktualisierungspflichten und BaFin-Uebermittlung.

# Insiderliste nach Art. 18 MAR

## Rechtlicher Rahmen

Art. 18 VO (EU) 596/2014 (MAR) verpflichtet Emittenten und alle in ihrem Auftrag oder für ihre
Rechnung handelnden Personen, eine Insiderliste zu führen. Format und Mindestinhalte sind in
DVO (EU) 2016/347 festgelegt. Die Insiderliste ist auf Verlangen unverzüglich der BaFin zu
übermitteln. Verletzung ist nach § 120 WpHG bußgeldbewehrt.

Rechtsgrundlagen:
- Art. 18 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/347 (Format): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0347
- § 120 WpHG: https://www.gesetze-im-internet.de/wphg/__120.html
- BaFin-Emittentenleitfaden Kap. IV: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill stellt sicher, dass Insiderlisten rechtskonform angelegt, laufend aktualisiert und
im Anforderungsfall vollständig übermittelt werden können. Er deckt die Listenstruktur, die
Belehrungspflicht, die Aktualisierungsauslöser und die Aufbewahrungspflicht ab.

## Arbeitsprogramm

### Schritt 1 – Listenstruktur und Format (DVO 2016/347)

Pflichtfelder je Eintrag:
- Vor- und Nachname
- Geburtsdatum und -ort
- Privatanschrift
- Funktion und Grund für Aufnahme in Liste
- Datum und Uhrzeit des Erhalts der Insiderinformation
- Datum und Uhrzeit der Aufnahme in die Liste
- Datum des Austritts aus der Insiderposition
Trenne: Projektliste (ereignisspezifisch) und permanente Insiderliste (Personen mit dauerhaftem
Zugang zu Insiderinformationen, z. B. Vorstand, Compliance-Officer).

### Schritt 2 – Aufnahme und Belehrungspflicht

- Aufnahme unmittelbar bei Erkenntnis der Insiderinformation, nicht erst bei bestätigtem Abschluss
- Jede aufgenommene Person muss schriftlich über:
 a) das Bestehen einer Insiderinformation informiert werden
 b) die rechtlichen Konsequenzen (Handelsverbote, Offenlegungsverbote) belehrt werden
 c) die Belehrung unterschrieben zurücksenden
- Belehrungsnachweis ist Teil der Compliance-Akte

### Schritt 3 – Aktualisierungspflicht

Aktualisierungspflicht bei:
- Neuaufnahme weiterer Wissensträger (interner oder externer)
- Austritt einer Person aus der Insiderposition (Datum eintragen)
- Änderung der Personendaten
- Übergang von Projektliste zu permanenter Liste oder umgekehrt
Alle Änderungen sind mit Zeitstempel zu versehen.

### Schritt 4 – Externe Dienstleister und Berater

- Banken, Kanzleien, WP-Gesellschaften, die Zugang zur Insiderinformation haben, müssen
 eigene Listen führen (Art. 18 Abs. 2 MAR)
- Emittent muss sicherstellen, dass externe Parteien die Verpflichtung kennen und einhalten
- Vertragliche Klausel in NDA / Beratervertrag empfehlen

### Schritt 5 – Aufbewahrung und BaFin-Übermittlung

- Aufbewahrung mindestens 5 Jahre (Art. 18 Abs. 5 MAR)
- Bei BaFin-Anfrage: Übermittlung unverzüglich (i.d.R. innerhalb von 24 Stunden)
- Format: DVO-konformes Tabellenformat (Excel oder IT-System)
- Zugriff nur für Compliance und Vorstand, nicht für Handelsabteilungen

## Red-Team-Fragen

- Sind alle Wissensträger (intern und extern) erfasst?
- Wurde jede Person schriftlich belehrt und hat die Belehrung bestätigt?
- Sind Aufnahme- und Austrittsdaten mit Uhrzeit korrekt eingetragen?
- Wurden Berater und Banken zur Führung eigener Listen verpflichtet?
- Ist die Liste im DVO-konformen Format erstellt?
- Liegt eine klare Trennung zwischen Projekt- und permanenter Insiderliste vor?
- Ist die Aufbewahrungspflicht von 5 Jahren sichergestellt?
- Kann die Liste im Anforderungsfall binnen 24 Stunden an die BaFin übermittelt werden?

## Ausgabeformat

Erzeuge:
1. Insiderlisten-Vorlage (DVO-konformes Format)
2. Belehrungsschreiben (Vorlag für Einzel- oder Serienmitteilung)
3. Aktualisierungs-Checkliste (Trigger und Zuständigkeiten)
4. BaFin-Übermittlungsprotokoll

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.
