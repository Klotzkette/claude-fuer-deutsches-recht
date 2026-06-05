---
name: unionsmarken-anmeldung
description: "Unionsmarken Anmeldung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Unionsmarken Anmeldung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Unionsmarken Anmeldung** im Plugin Markenrecht Fashion/Luxus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `unionsmarken-anmeldung-euipo` | Unionsmarke beim EUIPO anmelden nach UMV (EU) 2017/1001: Modehaus will EU-weiten Markenschutz in einem Verfahren. Normen: Art. 32 ff. UMV (Anmeldeerfordernisse), Art. 7 UMV (absolute Schutzhindernisse), Art. 119 UMV (Vertretungszwang). Prüfraster: e-Filing-Checkliste, Waren-/Dienstleistungsverzeichnis (Nizza), absolute Schutzhindernisse, Beobachtungszeitraum 3 Monate. Output Anmeldungs-Entwurf, Klassen-Verzeichnis, Eintragungsstrategie. Abgrenzung: DPMA-Anmeldung siehe wortmarke-anmeldung-dpma; Madrid siehe madrid-protokoll-und-internationale-registrierung. |
| `unternehmenskennzeichen-werktitel-domain` | Unternehmenskennzeichen, besondere Geschäftsbezeichnungen, Werktitel, Domains und Social-Media-Handles markenrechtlich einordnen: Entstehung ohne Register, Priorität, Reichweite, Verwechslungsgefahr und Durchsetzung. |
| `us-counterfeit-und-customs-cbp` | US-Counterfeit-Enforcement und CBP-Recordation: Luxusmarke will gefaelschte Ware in den USA stoppen. Normen: 18 U.S.C. § 2320 (Trademark Counterfeiting Act), 19 C.F.R. § 133 (CBP Recordation), Lanham Act § 34 (Injunctive Relief), § 35 (Statutory/Treble Damages). Prüfraster: IPR e-Recordation bei CBP, Enforcement-Strategie, Schadensersatz-Berechnung, Attorney Fees (Octane Fitness Standard). Output CBP-Recordation-Unterlagen, Enforcement-Strategie-Memo, Schadensersatz-Berechnungs-Template. Abgrenzung: EU-Zoll siehe produktpiraterie-und-zoll; TTAB siehe ttab-opposition-und-cancellation. |
| `us-selektivvertrieb-und-mfp-tiffany-vs-costco` | US-Vertriebsrecht für Luxusmarken: Resale Price Maintenance und MAP-Policies kartellrechtskonform gestalten. Normen: Sherman Act § 1, Leegin 551 U.S. 877 (Rule of Reason), Colgate Doctrine (unilateral), Tiffany v. Costco (Trademark Dilution durch Discount). Prüfraster: RPM-Legalitaet nach Leegin, MAP-Policy Formulierung, Minimum-Advertised-Price Unterschied zu Resale Price Fixing. Output Vertriebspolitik-Memo, MAP-Policy-Entwurf. Abgrenzung: EU Selektivvertrieb siehe selektiver-vertrieb-coty; EU Preisbindung siehe vertikale-preisbindung-vbe-vo. |

## Arbeitsweg

Im Plugin Markenrecht Fashion/Luxus gilt für **Unionsmarken Anmeldung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `unionsmarken-anmeldung-euipo`

**Fokus:** Unionsmarke beim EUIPO anmelden nach UMV (EU) 2017/1001: Modehaus will EU-weiten Markenschutz in einem Verfahren. Normen: Art. 32 ff. UMV (Anmeldeerfordernisse), Art. 7 UMV (absolute Schutzhindernisse), Art. 119 UMV (Vertretungszwang). Prüfraster: e-Filing-Checkliste, Waren-/Dienstleistungsverzeichnis (Nizza), absolute Schutzhindernisse, Beobachtungszeitraum 3 Monate. Output Anmeldungs-Entwurf, Klassen-Verzeichnis, Eintragungsstrategie. Abgrenzung: DPMA-Anmeldung siehe wortmarke-anmeldung-dpma; Madrid siehe madrid-protokoll-und-internationale-registrierung.

# Unionsmarken-Anmeldung beim EUIPO

## Fachkern: Unionsmarken-Anmeldung beim EUIPO
- **Spezialgegenstand:** Unionsmarken-Anmeldung beim EUIPO; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Die Unionsmarke (EUTM) ist das Herzstück des europäischen IP-Portfolios von klôtzzkètté SA. Mit einer einzigen Anmeldung beim EUIPO in Alicante schützt man das Zeichen in allen 27 EU-Mitgliedstaaten — eine strategische Meisterleistung, solange man die Tücken des Verfahrens kennt.

Ich begleite klôtzzkètté von der Konzeption über e-Filing bis zur Eintragung und koordiniere mit dem EUIPO auf Englisch, Französisch und Deutsch.

## Rechtsrahmen

- **VO (EU) 2017/1001 (UMV):** Hauptrechtsquelle für Unionsmarken (ersetzt VO 207/2009)
- **DurchfVO (EU) 2018/626:** Durchführungsverordnung (Formvorschriften, Fristen)
- **DelegVO (EU) 2018/625:** Delegierte Verordnung (Verfahrensdetails)
- **Art. 119 UMV:** Vertretungszwang für nicht in der EU ansässige Anmelder (klôtzzkètté SA Paris → Pariser Sitz zählt als EU ansässig; keine Vertretungspflicht, aber professionelle Vertretung empfohlen)
- **Art. 33 UMV:** Nizza-Klassifikation obligatorisch
- **Art. 8/46/47 UMV:** Absolute/relative Schutzhindernisse, Widerspruchsfrist
- **Art. 35 UMV:** Prioritätsanspruch (6 Monate ab erster Anmeldung)
- **Art. 38/39 UMV:** Formprüfung, Veröffentlichung
- **Art. 49/51 UMV:** Eintragung, Schutzdauer (10 Jahre, verlängerbar)
- **EUIPO-Leitlinien zur Prüfung:** Abrufbar unter euipo.europa.eu, laufend aktualisiert

## Prüfungsschritte

1. **Vorrecherche (obligatorisch vor e-Filing):**
 - EUIPO eSearch plus: Suche nach identischen und ähnlichen älteren Marken
 - EUIPO TMview: internationale Datenbank
 - Attention: EUIPO prüft keine relativen Schutzhindernisse von Amts wegen — Widerspruch ist Sache der Inhaber älterer Marken

2. **e-Filing — Anmeldeformular:**
 - Zugang via: euipo.europa.eu/eSearch/ → Online Filing
 - Markenart wählen: Wortmarke / Bildmarke / 3D-Marke / Hörmarke / Positionsmarke / Bewegungsmarke / Multimediamarke / Hologrammmarke / Farbmarke / Mustermarke
 - Markenwiedergabe hochladen (je nach Markenart: Text / JPG / MP3 / MP4)
 - Nizza-Klassen und Warenverzeichnis (ID-Manual EUIPO nutzen)
 - Inhaberangaben
 - Prioritätsanspruch (falls vorhanden): DPMA-Aktenzeichen, Anmeldedatum
 - Sprache: 1. Sprache (Anmeldesprache); 2. Sprache (muss offizielle EUIPO-Sprache sein: DE/EN/FR/ES/IT)

3. **Gebühren (Stand 2024):**
 - Elektronische Anmeldung: EUR 850 für Klasse 1; EUR 50 für Klasse 2; EUR 150 je weitere Klasse
 - Papier-Anmeldung: EUR 1.000 (Aufschlag — immer e-Filing bevorzugen)

4. **Formprüfung durch EUIPO:**
 - Ca. 1-2 Wochen Prüfung nach Eingang
 - Bei Mängeln: Fristsetzung zur Behebung (1 Monat, verlängerbar)

5. **Inhaltliche Prüfung:**
 - Absolute Schutzhindernisse Art. 7 UMV (entspricht § 8 MarkenG)
 - Kein Prüfen relativer Hindernisse
 - Bei Beanstandung: Office Action mit Erwiderungsfrist 2 Monate (verlängerbar)

6. **Veröffentlichung:**
 - Nach Prüfung: Veröffentlichung im EUIPO-Markenblatt (EUTM Bulletin)
 - Beginn der 3-monatigen Widerspruchsfrist (Art. 46 UMV)

7. **Widerspruchsphase:**
 - 3 Monate ab Veröffentlichung für Widersprüche Dritter
 - Cooldown-Periode: 2 Monate friendly-settlement, dann Schriftsatzphase
 - Vgl. Skill `euipo-widerspruchsverfahren`

8. **Eintragung:**
 - Nach widerspruchsfreiem Ablauf der 3-Monatsfrist oder nach Abschluss der Widerspruchsverfahren
 - Eintragungsbeschluss, Eintragung im EUIPO-Register
 - Eintragungsurkunde (digital, keine physische Urkunde mehr)

## Falltypische Konstellationen

### Konstellation 1: EUTM-Erstanmeldung klôtzzkètté
Parallele Anmeldung zu DPMA-Basismarke mit Prioritätsanspruch (Tag +30 nach DPMA-Anmeldung). Sprache: Englisch (1. Sprache) / Deutsch (2. Sprache). Klassen 3/14/18/25/35. Anmeldungsgebühr: EUR 850 + 50 + 150 + 150 + 150 = EUR 1.350.

### Konstellation 2: Widerspruch durch älteren Rechteinhaber
Nach Veröffentlichung legt Mailänder Modehaus "Klothé SRL" Widerspruch wegen Verwechslungsgefahr ein (EUIPO-Widerspruchsverfahren Art. 46 ff. UMV). → Übergabe an Skill `euipo-widerspruchsverfahren`.

### Konstellation 3: Priorität auf DPMA-Anmeldung vergessen
Frist für Prioritätsanspruch (6 Monate nach DPMA-Anmeldung) um 3 Tage versäumt. Konsequenz: Kein Prioritätsdatum, Anmeldedatum der EUTM ist maßgeblich. In der Zwischenzeit eingegangene Widersprüche werden auf Basis des EUTM-Anmeldedatums beurteilt.

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Templates

### e-Filing Checkliste EUIPO
```
[ ] Markenart ausgewählt
[ ] Markenwiedergabe: Format korrekt (JPG max. 2 MB / MP3 max. 2 MB)
[ ] 1. und 2. EUIPO-Verfahrenssprache angegeben
[ ] Nizza-Klassen und Warenverzeichnis: ID-Manual EUIPO geprüft
[ ] Inhaberangaben vollständig (Name, Adresse, Nationalität/Rechtsform)
[ ] Prioritätsanspruch eingetragen (Aktenzeichen + Anmeldedatum DPMA)
[ ] Gebühren per Kreditkarte / EUIPO-Konto bezahlt
[ ] Anmeldebestätigung mit Aktenzeichen gespeichert
```

## Verweise auf andere Skills

- `anmeldung-strategie-portfolio` — Strategischer Rahmen
- `euipo-widerspruchsverfahren` — Nach Veröffentlichung
- `wortmarke-anmeldung-dpma` — Basismarke für Prioritätsanspruch
- `madrid-protokoll-und-internationale-registrierung` — Erweiterung auf Drittstaaten

## Risiken & Stolperfallen

- **Einheitlichkeit der EUTM:** Eine Unionsmarke, die in einem Mitgliedstaat absolut nicht schutzfähig ist, wird insgesamt zurückgewiesen (Art. 7 II UMV) — Territoriumsproblem bei länderspezifisch beschreibenden Begriffen
- **Keine amtliche Prüfung relativer Hindernisse:** Ältere eingetragene Marken werden nicht automatisch gefunden und dem Anmelder mitgeteilt (anders als beim DPMA, das einen Hinweis gibt)
- **Widerspruchskosten:** Bei Widerspruchsverfahren entstehen schnell EUR 5.000–15.000 Anwaltskosten pro Seite
- **2. Sprache:** Falsche Wahl der 2. Sprache (muss eine der 5 offiziellen EUIPO-Sprachen sein) führt zu Beanstandung

## Triage-Fragen vor EUIPO-Anmeldung

Bevor das e-Filing startet, klaere:
1. Wurde eine eSearch-Vorrecherche auf identische und aehnliche aeltere Marken durchgefuehrt?
2. Ist das Warenverzeichnis hinreichend praezise (IP Translator — keine pauschalen Klassenüberschriften)?
3. Soll Prioritaet auf eine DPMA-Anmeldung beansprucht werden — ist die 6-Monats-Frist noch offen?
4. Gibt es bekannte aeltere Inhaber, die widerspruchsberechtigt sein koennen?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `unternehmenskennzeichen-werktitel-domain`

**Fokus:** Unternehmenskennzeichen, besondere Geschäftsbezeichnungen, Werktitel, Domains und Social-Media-Handles markenrechtlich einordnen: Entstehung ohne Register, Priorität, Reichweite, Verwechslungsgefahr und Durchsetzung.

# Unternehmenskennzeichen, Werktitel und Domains

## Fachkern: Unternehmenskennzeichen, Werktitel und Domains
- **Spezialgegenstand:** Unternehmenskennzeichen, Werktitel und Domains; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Aufgabe

Prüfe Kennzeichenrechte außerhalb der eingetragenen Marke und ihre Kollision mit Marken, Domains, App-Namen, Hashtags und Social-Media-Handles.

## Intake

- Bezeichnung, Nutzungsbeginn, Gebiet, Branche, Verkehrskreise.
- Domainregistrierung, Website-Livegang, Social-Media-Handle, App-Store-Eintrag.
- Eingetragene Marken und Unternehmensregister.
- Konflikt: Abmahnung, Löschung, UDRP, DENIC-Dispute, Plattformmeldung?

## Prüfprogramm

1. **Kennzeichenart bestimmen:** Unternehmenskennzeichen, besondere Geschäftsbezeichnung, Werktitel, Domain als Kennzeichen oder rein technische Adresse.
2. **Entstehung prüfen:** Tatsächliche namensmäßige Benutzung im geschäftlichen Verkehr; Reichweite aus Verkehrsgeltung und Tätigkeitsgebiet.
3. **Priorität vergleichen:** Registerpriorität vs. Benutzungsbeginn; Expansion nicht beliebig.
4. **Verwechslungsgefahr:** Zeichen, Branche, Waren/Dienstleistungen, Gebiet, Aufmerksamkeit.
5. **Durchsetzung:** Unterlassung, Domainübertragung meist nicht automatisch, Dispute-Eintrag, Plattformprozesse, Vergleich.

## Output

- Kennzeichenkarte mit Prioritäten.
- Domain-/Handle-Strategie.
- Abmahn- oder Verteidigungsentwurf.

## Quellen

MarkenG live prüfen; Domain- und Plattformregeln konkret nach Registry/Plattform nachziehen.

## 3. `us-counterfeit-und-customs-cbp`

**Fokus:** US-Counterfeit-Enforcement und CBP-Recordation: Luxusmarke will gefaelschte Ware in den USA stoppen. Normen: 18 U.S.C. § 2320 (Trademark Counterfeiting Act), 19 C.F.R. § 133 (CBP Recordation), Lanham Act § 34 (Injunctive Relief), § 35 (Statutory/Treble Damages). Prüfraster: IPR e-Recordation bei CBP, Enforcement-Strategie, Schadensersatz-Berechnung, Attorney Fees (Octane Fitness Standard). Output CBP-Recordation-Unterlagen, Enforcement-Strategie-Memo, Schadensersatz-Berechnungs-Template. Abgrenzung: EU-Zoll siehe produktpiraterie-und-zoll; TTAB siehe ttab-opposition-und-cancellation.

# US Counterfeit Enforcement und CBP Recordation

## Fachkern: US Counterfeit Enforcement und CBP Recordation
- **Spezialgegenstand:** US Counterfeit Enforcement und CBP Recordation; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Produktfälschungen auf dem US-Markt sind eine existenzielle Bedrohung für klôtzzkètté Inc. in New York. J. Halston Whitman III, Esq. und Eleanor M. Quintero, Esq. (Whitman Brennan Forsythe LLP) handhaben alle US-Enforcement-Maßnahmen; wir koordinieren die europäischen Schutzrechts-Dokumentation und internationale Parallelmaßnahmen (vgl. Skill `produktpiraterie-und-zoll` für EU-Parallelen).

Das US-System kombiniert zivile und strafrechtliche Instrumente zu einem der schärfsten Anti-Counterfeiting-Arsenale der Welt.

## Rechtsrahmen

- **18 U.S.C. § 2320 (Trademark Counterfeiting Act 1984):** Strafrecht — Verwendung einer Fälschungsmarke auf Waren/Dienstleistungen; bis zu 10 Jahre Haft + USD 2 Mio. Geldstrafe pro Person; bis zu 20 Jahre bei Wiederholungstäter
- **15 U.S.C. § 1114 (Lanham Act § 32):** Zivilrechtlicher Infringement Claim (gegen Verwendung eingetragener Marke)
- **15 U.S.C. § 1116 (Lanham Act § 34):** Injunctive Relief — federal courts dürfen Unterlassungsverfügungen erlassen; ex parte Seizure möglich bei Counterfeiting
- **15 U.S.C. § 1117 (Lanham Act § 35):** Damages:
 - Defendant's Profits (Herausgabe des Verletzergewinns)
 - Actual Damages (nachgewiesener Schaden klôtzzkètté)
 - Treble Damages: bis 3x bei willful infringement
 - Statutory Damages bei Counterfeiting: USD 1.000-200.000 je Mark/Goods-Kombination; USD 2.000.000 bei willful counterfeiting
 - Attorney Fees in "exceptional cases" (§ 1117(a))
- **Octane Fitness, LLC v. ICON Health & Fitness, Inc., 572 U.S. 545 (2014):** Standard für "exceptional case" (ursprünglich Patentrecht, übertragen auf Markenrecht durch 4th Cir.) — niedrigerer Standard als früher; subjective bad faith oder objectively weak position genügt
- **19 C.F.R. § 133 (CBP Recordation):** US Customs and Border Protection-Anmeldung; ermöglicht Grenzbeschlagnahme an US-Grenzübergängen
- **19 U.S.C. § 1526:** CBP-Importverbote für Fälschungsware

## Prüfungsschritte

### Schritt 1: CBP Recordation (Präventiv)

1. **IPR e-Recordation:**
 - Online-Portal: iprecordation.cbp.dhs.gov
 - Voraussetzung: Eingetragene US-Marke (Principal Register) oder US-Copyright
 - Eingabe: Markenregistrierungs-Nummer, Inhaberdaten, Produktbeschreibung mit Originalmerkmalen
 - Upload: Fotos Original vs. bekannte Fälschungen
 - Gebühr: USD 190 je Record (Marke oder Copyright)
 - Laufzeit: Solange Marke eingetragen; jährliche Aktualisierung empfohlen

2. **Fälschungsmerkmals-Dokumentation für CBP:**
 - Echtheitszertifikate, Hologramme, QR-Codes
 - Unterschiede Original vs. Fälschung (Foto-Checkliste)
 - Warenbezeichnung, HS-Codes (Harmonized Tariff Code) für Klasse 25-Produkte
 - Bekannte Hersteller/Exporteure von Fälschungen (Guangzhou-Adressen)

3. **CBP IPR Center:**
 - Kooperation mit IPR Center (Washington DC): spezialisierte Zollbehörde für IP-Enforcement
 - Beziehungsaufbau: Whitman Brennan Forsythe LLP unterhält direkte Kontakte zu CBP IPR-Agents

### Schritt 2: Ex parte Seizure (§ 34 Lanham Act)

4. **Antrag auf ex parte Seizure Order:**
 - Bei akuter Bedrohung (Fälschungsware im Umlauf, Vernichtungsgefahr)
 - Application beim Federal District Court: SDNY (bevorzugt für Fashion Cases)
 - Requiremenets: (1) TRO wäre unzureichend; (2) Plaintiff has valid mark; (3) Counterfeit evidence; (4) Harm without seizure; (5) Public interest not harmed
 - Richter kann ohne Anhörung des Beklagten anordnen
 - U.S. Marshal vollstreckt; Sicherheitsleistung erforderlich

5. **Aftermath:**
 - Sequestered goods werden gelagert
 - Notifikation des Beklagten nach Seizure
 - Hearing within 15 days
 - Übergang zu regulärem Injunction-Verfahren

### Schritt 3: Zivilklage — Damages

6. **Claim-Kalkulation:**
 - Statutory Damages Strategie: Bei klarer Counterfeiting (keine langwierige Damages-Berechnung nötig)
 - USD 1.000 (Minimum) bis USD 200.000 je Mark per type of goods
 - Willful: bis USD 2.000.000 — zu beweisen durch Knowledge of klôtzzkètté-Marke + deliberate copying
 - Mehrere Marks × mehrere Goods-Kategorien = substanzieller Gesamtbetrag
 - Beispiel: 3 Marks × 3 Goods = 9 Kombinationen × USD 50.000 = USD 450.000

7. **Attorney Fees:**
 - Octane Fitness-Standard: Exceptional case = subjectively bad faith or objectively baseless defense
 - Counterfeit cases: Meist als exceptional eingestuft wenn Defendant continued infringement after notice

### Schritt 4: Strafverfolgung (18 U.S.C. § 2320)

8. **Zusammenarbeit mit DOJ/FBI:**
 - Anzeige bei FBI Field Office (NYC) oder ICE-HSI (Homeland Security Investigations)
 - IPR Center für koordinierte Ermittlungen
 - Whitman Brennan Forsythe LLP koordiniert Ermittlungsunterstützung (ohne anwaltliche Einschränkungen durch Strafrecht)

## Falltypische Konstellationen

### Konstellation 1: Container-Beschlagnahme durch CBP am JFK
CBP JFK Alert: Container aus Guangzhou mit 3.500 klôtzzkètté-Fälschungen. CBP-Recordation löst Alert aus. Whitman Brennan Forsythe LLP reagiert innerhalb 24h: Bestätigung Counterfeit, Zustimmung zur Beschlagnahme. Forfeiture und Vernichtung. Parallel: Ermittlung des US-Importeurs für Zivilklage.

### Konstellation 2: Donauzon US Marketplace Enforcement
Donauzon US-Marketplace (us.donauzon.com) verkauft Fälschungen über Drittanbieter. Ex parte Seizure-Antrag SDNY gegen 12 identifizierte Sellers. Statutory Damages bei willful Counterfeiting: USD 2.000.000 je Mark je Goods-Typ.

### Konstellation 3: Criminal Referral
Organisierter Fälschungsring (multiple shipments, estimated USD 5M in counterfeit goods). Kooperation mit FBI/HSI. Whitman Brennan Forsythe LLP als Victim's Counsel; Steinacker Lichtenberg koordiniert EU-Parallelvorgehen (VO EU 608/2013).

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Templates

### CBP Recordation Checkliste
```
[ ] US Trademark Registration Number (Principal Register)
[ ] Trademark owner contact information
[ ] Product description with HTS codes
[ ] Photos: Genuine product (multiple angles)
[ ] Photos: Known counterfeit (if available, with differences marked)
[ ] Authentication features described (hologram, QR, serial number)
[ ] Known counterfeit manufacturers (addresses if known)
[ ] Authorized U.S. importers (list for CBP)
[ ] Fee: USD 190 per record
[ ] Annual review calendar set
```

### Ex parte Seizure Application — Required Showings
```
1. A temporary restraining order would be inadequate:
 [Risk of destruction/concealment of evidence]

2. Applicant will suffer irreparable harm without seizure:
 [Ongoing sales/damage to goodwill of klôtzzkètté]

3. The harm to applicant outweighs harm to defendant:
 [Counterfeiting has no legitimate business interest]

4. Applicant is likely to succeed on the merits:
 [Registration + clear counterfeiting evidence]

5. Public interest will not be harmed:
 [Consumers protected from counterfeit luxury goods]
```

## Verweise auf andere Skills

- `produktpiraterie-und-zoll` — EU-Parallelvorgehen (VO EU 608/2013)
- `messe-verletzung-und-gv-einsatz` — Deutsche Messe-Enforcement Parallele
- `us-trade-dress-und-secondary-meaning` — Trade Dress Infringement parallel
- `nyc-korrespondenz-und-conflict-check` — Koordination Whitman Brennan Forsythe LLP

## Risiken & Stolperfallen

- **Sicherheitsleistung ex parte Seizure:** Gericht verlangt Bond; bei falscher Seizure haftet klôtzzkètté für Schäden des Beklagten
- **Statutory Damages Strategie vs. Actual Damages:** Bei hohem tatsächlichen Schaden kann Actual Damages + Treble vorteilhafter sein; frühzeitig kalkulieren
- **CBP-Recordation-Aktualisierung:** Neue Designs/Marken müssen nachgemeldet werden; CBP nimmt nur eingetragene US-Marken
- **Criminal vs. Civil Coordination:** Parallelverfahren können sich gegenseitig beeinflussen; enge Abstimmung mit DOJ/FBI-Kooperationsregeln

## Triage-Fragen bei US-Produktpiraterie

Bevor CBP-Massnahmen oder die ex-parte-Seizure beantragt wird, klaere:
1. Ist die US-Marke bei CBP recordiert (aktuelles Recordation mit korrektem E.P. Code und gueltigem Registrierungsdatum)?
2. Liegen Beweise fuer eine unmittelbar bevorstehende Piraterie-Sendung vor (Zoll-Tip, Labortest, Lieferschein)?
3. Handelt es sich um strafrechtlich relevante Counterfeit Goods (18 U.S.C. § 2320 — Federal Crime) oder nur zivilrechtliche Verletzung?
4. Ist die ex-parte-Seizure gerechtfertigt (droht Beweisvernichtung) oder genuegt eine TRO/PI?

## Aktuelle Rechtsprechung (US)

> **Tiffany (NJ) Inc. v. eBay Inc., 600 F.3d 93 (2d Cir. 2010):** Online-Marktplaetze sind nicht schlechthin fuer Counterfeit-Listings ihrer Seller haftbar; Haftung setzt voraus, dass der Marktplatz spezifische Kenntnis von bestimmten verletzenden Angeboten hatte und trotzdem nicht gehandelt hat (specific knowledge rule).

> **Louis Vuitton Malletier S.A. v. Akanoc Solutions Inc., 658 F.3d 936 (9th Cir. 2011):** Hosting-Provider koennen als Contributory Infringer haften, wenn sie direkte Kontrolle ueber und direkten Nutzen aus verletzenden Inhalten ziehen und trotz Kenntnis der Verletzung nichts unternehmen.

> **Gucci America, Inc. v. Guess?, Inc., 868 F. Supp. 2d 207 (S.D.N.Y. 2012):** Bei Verletzung bekannter Luxusmarken durch Counterfeit-Produkte koennen Statutory Damages bis USD 2.000.000 pro Verletzungshandlung zugesprochen werden; fuer willful infringement erhoehen sich die Maxima auf das Dreifache nach § 35(b) Lanham Act.

## Output-Template: CBP Recordation Update

```
CBP RECORDATION — ANNUAL UPDATE
klotzkette SA — Trademark Portfolio

1. REGISTERED US TRADEMARKS (current):
 Reg. No. [xxxx] — KLOTZKETTE wordmark — Cl. 25 — Rec. date [xx/xx/xxxx]
 Reg. No. [xxxx] — Doppel-K device — Cl. 14/18 — Rec. date [xx/xx/xxxx]

2. KNOWN COUNTERFEIT FEATURES (attach images):
 - Stitching quality differences
 - Hologram location/color deviations
 - QR code format variations
 - Packaging typography errors

3. POINTS OF ORIGIN: CN (Guangzhou), TR, IN
4. CONTACT: Eleanor M. Quintero, Esq., Whitman Brennan Forsythe LLP
 Tel: +1 212 xxx xxxx / equintero@wbf.law
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `us-selektivvertrieb-und-mfp-tiffany-vs-costco`

**Fokus:** US-Vertriebsrecht für Luxusmarken: Resale Price Maintenance und MAP-Policies kartellrechtskonform gestalten. Normen: Sherman Act § 1, Leegin 551 U.S. 877 (Rule of Reason), Colgate Doctrine (unilateral), Tiffany v. Costco (Trademark Dilution durch Discount). Prüfraster: RPM-Legalitaet nach Leegin, MAP-Policy Formulierung, Minimum-Advertised-Price Unterschied zu Resale Price Fixing. Output Vertriebspolitik-Memo, MAP-Policy-Entwurf. Abgrenzung: EU Selektivvertrieb siehe selektiver-vertrieb-coty; EU Preisbindung siehe vertikale-preisbindung-vbe-vo.

# US-Selektivvertrieb, Resale Price Maintenance und MAP-Policies

## Fachkern: US-Selektivvertrieb, Resale Price Maintenance und MAP-Policies
- **Spezialgegenstand:** US-Selektivvertrieb, Resale Price Maintenance und MAP-Policies; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** MarkenG, UMV, DesignG/GGV, UWG, UrhG, GeschGehG, Zoll-/Grenzbeschlagnahme, DSA/Marketplace, Erschöpfung, Rufausbeutung und Schadensersatz.
- **Entscheidende Weiche:** Kennzeichen/Design, Priorität, Benutzung, Verwechslungsgefahr, Bekanntheit, Erschöpfung, Plattformbeweis, Auskunft und Vollstreckung getrennt prüfen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


Das US-Antitrust-Recht behandelt vertikale Preisbindung fundamental anders als das EU-Kartellrecht. Seit Leegin (2007) ist Resale Price Maintenance (RPM) nicht mehr per se illegal, sondern unterliegt der Rule of Reason — ein Paradigmenwechsel für Luxusmarken wie klôtzzkètté Inc.

Eleanor M. Quintero, Esq. (Whitman Brennan Forsythe LLP) berät klôtzzkètté Inc. zu allen US-Antitrust-Fragen; Steinacker Lichtenberg München koordiniert die EU-Parallelrechts-Analyse (vgl. Skills `vertikale-preisbindung-vbe-vo` und `selektiver-vertrieb-coty`).

## Rechtsrahmen

- **Leegin Creative Leather Prods., Inc. v. PSKS, Inc., 551 U.S. 877 (2007):** Overrules Dr. Miles Medical Co. (1911); RPM ist jetzt Rule of Reason, nicht per se illegal. Faktoren: Marktmacht, Wettbewerbseffekte, Effizienzgewinne, Schäden für Verbraucher
- **Dr. Miles Medical Co. v. John D. Park & Sons, 220 U.S. 373 (1911):** Historisch — per se illegal (nicht mehr geltendes Recht)
- **United States v. Colgate & Co., 250 U.S. 300 (1919) (Colgate Doctrine):** Hersteller kann einseitig (ohne Vereinbarung) ankündigen, an nicht-kooperative Händler nicht zu liefern; kein Sherman Act § 1-Verstoß weil keine "agreement"
- **Sherman Act § 1, 15 U.S.C. § 1:** Kartellverbot (alle Vereinbarungen in Restraint of Trade)
- **Robinson-Patman Act, 15 U.S.C. § 13:** Price Discrimination zwischen Händlern — bei identischen Waren müssen identische Einkaufspreise gelten (komplex; oft ignoriert in Praxis)
- **Tiffany (NJ) Inc. v. Costco Wholesale Corp., 971 F.3d 74 (2d Cir. 2020):** Costco verwendete Tiffany-Name für generische Diamantringe (nicht von Tiffany) im Regal. Tiffany: Trademark Infringement + Dilution. Result: Settlement nach Geschworenenprozess; Costco zahlte USD 21 Mio.
- **State Antitrust Laws:** Maryland, California, New York haben eigene RPM-Gesetze (strenger als Bundesrecht) — klôtzzkètté Inc. in NY muss NY Donnelly Act beachten

## Prüfungsschritte

### Schritt 1: RPM-Strategie nach Leegin

**Verbotene RPM (immer):**
- Horizontale Preisabsprachen zwischen Wettbewerbern (per se illegal)
- Minimum-Preis-Vereinbarung mit erheblicher Marktmacht + nachgewiesenem Wettbewerbsschaden

**Zulässige RPM nach Leegin:**
- Minimum Resale Price + kein erheblicher Marktmachtmissbrauch + nachweisbare Effizienzgewinne
- Rule of Reason: Gesamtbewertung (Pro-Competitive Benefits vs. Anti-Competitive Effects)

**Colgate Doctrine (Sicherste Methode):**
- klôtzzkètté Inc. kündigt einseitig an: "Wir liefern nicht an Händler, die unter USD 1.200 verkaufen"
- Kein Vertrag, keine "agreement" = kein Sherman Act § 1-Problem
- Grenze: Keine Verhandlung mit Händlern über Einhaltung; echte Unilateralität erforderlich

### Schritt 2: MAP-Policy (Minimum Advertised Price)

**Definition MAP:**
- MAP = Mindestpreis in der Werbung (Katalog, Anzeige, Website-Listing)
- ≠ Mindest-Verkaufspreis (der kann darunter liegen, aber nicht in Werbung kommuniziert)

**Zulässigkeit MAP unter Leegin:**
- MAP-Policy ist grundsätzlich zulässig (Rule of Reason; bei fehlender Marktmacht meist unproblematisch)
- Vorteil: Schützt Brand-Prestige in Werbematerialien ohne direkten Einfluss auf Verkaufspreis
- Grenze: MAP darf nicht faktisch als Floor Price für tatsächliche Verkäufe wirken

**MAP-Policy Implementierung für klôtzzkètté Inc.:**
- Schriftliche MAP-Policy: "Händler dürfen klôtzzkètté-Produkte in Werbematerialien nicht unter USD 1.200 bewerben"
- Keine Sanktionierung von Preissenkungen per se (nur von Werbeverstößen)
- Konsequente Anwendung auf alle Händler (kein Favorites-System)

### Schritt 3: Tiffany v. Costco — Lehren für Luxusmarken

**Sachverhalt Tiffany/Costco:**
- Costco verwendete Pappaufsteller mit Aufschrift "Tiffany" für generische 0.40-ct-Diamantringe
- Tiffany-Marke nicht auf den Ringen selbst; nur Point-of-Sale-Bezeichnung
- Held (nach Jury): Trademark Infringement + False Designation of Origin + Dilution

**Learnings für klôtzzkètté:**
- Discounter-Werbung mit Markenname ohne Zustimmung = Infringement + Dilution
- Dilution by Tarnishment: Assoziation mit Discount = Rufschädigung der Luxusmarke
- Preemptive Enforcement: Klare C&D-Briefe an jede nicht-autorisierte Nutzung des Markennamens in Werbung

### Schritt 4: Robinson-Patman Act Check

**Wesentliche Pflicht:**
- Wenn klôtzzkètté Inc. verschiedenen Händlern unterschiedliche Einkaufspreise berechnet (z.B. Saks Fifth Avenue günstiger als regionaler Boutique-Händler): Robinson-Patman-Risiko
- Ausnahmen: Mengenrabatte (cost-justified), unterschiedliche Märkte/Wettbewerb
- Praxis: Standardisierte Preisliste + dokumentierte Rabattbegründungen

## Falltypische Konstellationen

### Konstellation 1: Colgate-Doctrine-Umsetzung für klôtzzkètté Inc.
klôtzzkètté Inc. sendet an alle US-Händler einseitigen Brief: "Policy: We will not sell to retailers who advertise or sell our products below MSRP USD 1.200 for handbags." Kein Meeting, keine Verhandlung. Pure Colgate. Eleanor Quintero Review: Colgate-konform. Implementierung nach Final Approval Whitman Brennan Forsythe LLP.

### Konstellation 2: MAP-Verstoß durch Brezelmann US (Bad Mergentheim → NYC Import)
Brezelmann US LLC bewirbt klôtzzkètté-Handtaschen auf Website für USD 699. MAP-Policy-Verstoß: Schriftliche Abmahnung, Lieferstopp-Ankündigung. Gleichzeitig: Prüfung ob Ware Gray Market (Erschöpfung?) oder Fälschung (→ Skill `us-counterfeit-und-customs-cbp`).

### Konstellation 3: Costco-ähnlich — Discount-Kette nutzt "klôtzzkètté-Style"
Discount-Kette bewirbt Handtaschen als "klôtzzkètté-inspired luxury" ohne Markenverwendung. Kein Trademark-Verstoß per se (kein Markenname); aber: UWG-Analogie fehlt im US-Recht. Lanham Act § 43(a): False Designation of Origin? Nur wenn Verbraucher echte klôtzzkètté-Verbindung annehmen.

## Quellen-Hardening

- Keine Kommentar-, Handbuch-, Aufsatz-, BeckRS- oder juris-Blindzitate aus Modellwissen.
- Registerdaten, Amtsformulare, Fristen, Gebühren und Behördenpraxis live bei DPMA, EUIPO, WIPO, USPTO oder den jeweils zuständigen Stellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle ausgeben.

## Templates

### MAP-Policy Brief (an US-Händler)
```
klôtzzkètté Inc.
712 Fifth Avenue, New York, NY 10019

TO: All Authorized U.S. Retailers
RE: Minimum Advertised Price (MAP) Policy

Effective [Date], klôtzzkètté Inc. establishes the following
Minimum Advertised Price (MAP) Policy:

Authorized retailers may not advertise klôtzzkètté products
in any medium (print, digital, broadcast, email) at prices
below the following MAP levels:
- Handbags: USD 1,200
- Scarves: USD 450
- Fragrances: USD 280

This policy is a unilateral business decision of klôtzzkètté Inc.
Actual retail selling prices remain at each retailer's discretion.

Retailers who advertise below MAP will not receive cooperative
advertising support and may lose authorized retailer status.

J. Halston Whitman III, Esq. (legal review confirmed)
```

## Verweise auf andere Skills

- `selektiver-vertrieb-coty` — EU-Pendant: Coty-Selektivvertrieb
- `vertikale-preisbindung-vbe-vo` — EU-Pendant: Vertikal-GVO
- `us-counterfeit-und-customs-cbp` — Counterfeit-Enforcement parallel
- `nyc-korrespondenz-und-conflict-check` — Koordination NYC-Kanzlei

## Risiken & Stolperfallen

- **Leegin ≠ Safe Harbor:** Rule of Reason bedeutet Klagerisiko bleibt; marktmächtige Unternehmen haben höheres Risiko
- **State Law:** New York Donnelly Act und California Cartwright Act können strenger sein als Sherman Act; separate State-Analysis vor US-Launch
- **Colgate-Purity:** Jede Kommunikation über RPM-Erwartungen mit Händlern gefährdet die Colgate-Doktrin; internen E-Mail-Verkehr sorgfältig überwachen
- **Robinson-Patman Documentation:** Alle Rabatt-Begründungen schriftlich dokumentieren; unstrukturierte Preislisten sind Klageeinladungen

## Triage-Fragen zum US-Selektivvertrieb

Bevor das MAP/RPM-System in den USA eingerichtet wird, klaere:
1. Handelt es sich um eine unilaterale MAP-Policy (Colgate-Doktrin — zulaessig) oder eine bilateral vereinbarte Preisbindung (§ 1 Sherman Act-Risiko)?
2. Werden retailer-spezifische Preisabsprachen in E-Mails oder Meetings dokumentiert (Colgate-Gefahr)?
3. Sind staatliche Antitrust-Gesetze (New York Donnelly Act, California Cartwright Act) gesondert geprueft?
4. Ist die Marktmacht von klotzkette Inc. im relevanten US-Markt so gross, dass Rule-of-Reason-Pruefung zum Nachteil ausgeht?

## Aktuelle Rechtsprechung (US)

> **Leegin Creative Leather Products v. PSKS, 551 U.S. 877 (2007):** Der U.S. Supreme Court hat die per-se-Illegalitaet von Resale Price Maintenance aufgegeben und durch den Rule-of-Reason-Standard ersetzt; RPM kann durch procompetitive Effekte gerechtfertigt sein, insbesondere wenn es die Servicequalitaet des Haendlers sichert.

> **Tiffany (NJ) Inc. v. Costco Wholesale Corp., 971 F.3d 74 (2d Cir. 2020):** Der Verkauf von Diamantringen mit dem Schildchen "Tiffany" ohne Genehmigung von Tiffany begründet Likelihood of Confusion und False Designation of Origin nach § 43(a) Lanham Act; unberechtigte Nutzung einer Luxusmarke durch Discounter begründet Marken- und Trade-Dress-Ansprueche.

> **United States v. Colgate & Co., 250 U.S. 300 (1919) (Colgate-Doktrin):** Ein Hersteller hat das Recht, einseitig zu entscheiden, an wen er seine Produkte verkauft und zu welchen Bedingungen; eine unilaterale MAP-Policy ohne Absprache mit Haendlern ist nach der Colgate-Doktrin zulaessig.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
