---
name: blockchain-settlement-buergschaft-erste
description: "Blockchain Settlement Buergschaft Erste: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Blockchain Settlement Buergschaft Erste

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Blockchain Settlement Buergschaft Erste** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `blockchain-settlement-dvp` | Blockchain-Settlement und Delivery-versus-Payment prüfen: Wertpapierseite, Geldseite, Finalität, CSD, Token Cash, Smart Contract, Fehlerkorrektur und Rechtswahl. |
| `buergschaft-auf-erste-anforderung-bank` | Bürgschaft oder Garantie auf erste Anforderung aus Bankensicht prüfen: Textauslegung, Abrufmechanik, offensichtlicher Rechtsmissbrauch, einstweiliger Rechtsschutz, Regress gegen Kunden und Dokumentation der Zahlungsentscheidung. |
| `buergschaft-privatperson-gesellschafter-ehegatte` | Privatpersonen-, Gesellschafter- und Ehegattenbürgschaften aus Bankensicht prüfen: Schriftform, krasse finanzielle Überforderung, Sittenwidrigkeit, Verbraucherschutz, Aufklärung, Sicherheitenwert und Prozessrisiko. |
| `chargeback-card-schemes-bankrecht` | Chargeback und Card-Scheme-Disputes rechtlich begleiten: Mastercard/Visa-Regeln, Zahlungsdienstehaftung, Händlerstreit, Fristen, Belege, Kundenerwartung und Kulanzgrenzen. |
| `correspondent-banking-nostro-vostro` | Korrespondenzbankbeziehungen und Nostro/Vostro-Risiken prüfen: AML, Sanktionen, Länder, Zahlungswege, Vertragsklauseln, Informationsrechte, Kündigung und Aufsichtserwartungen. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **Blockchain Settlement Buergschaft Erste**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `blockchain-settlement-dvp`

**Fokus:** Blockchain-Settlement und Delivery-versus-Payment prüfen: Wertpapierseite, Geldseite, Finalität, CSD, Token Cash, Smart Contract, Fehlerkorrektur und Rechtswahl.

# DLT Settlement DvP

## Fachkern: DLT Settlement DvP
- **Spezialgegenstand:** DLT Settlement DvP. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank will DLT-basierte Abwicklung, tokenisiertes Cash oder Wertpapierlieferung gegen Zahlung nutzen.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Instrument, Settlementmodell, Geldtoken, CSD, Smart Contract, Teilnehmer, Fehlerfall, Rechtswahl.
- **Institut und Rolle:** Bank, Zahlungsinstitut, E-Geld-Institut, Wertpapierinstitut, CRR-Kreditinstitut, FinTech-Tochter, Vermittler, Agent, Registerführer, CASP, Emittent oder Dienstleister.
- **Produkt oder Vorgang:** Zahlungsdienst, E-Geld, Kredit, Wertpapier, Token, Register, Organwechsel, Auslagerung, Betrugsfall, Trade Finance oder Kooperation.
- **Aufsicht und Einreichweg:** BaFin, Bundesbank, EZB/SSM, EBA, FIU, Register, MVP, IMAS, Bundesanzeiger, Handelsregister oder interner Ausschuss.
- **Dokumente:** Produktbeschreibung, Flow-of-Funds, Vertragsentwurf, API-Doku, Token Terms, Organ-CV, Eignungsmatrix, Registerauszug, Kundenkommunikation, Logs oder Vorstandsvorlage.

## Prüfaufbau

### 1. Kurzbild

| Punkt | Klärung |
| --- | --- |
| Ergebnisbedarf | Vermerk, Freigabe, BaFin-Anfrage, Vertrag, Vorstandsvorlage oder Prozessstrategie |
| Rechtsregime | KWG, ZAG, WpHG, WpIG, eWpG, MiCAR, DORA, GwG, BGB, HGB, AktG, SEPA-/EU-Regime oder Entwurf |
| Risiko | Aufsicht, Bußgeld, Zivilhaftung, Organhaftung, Kundenstreit, AML, Datenschutz, IT oder Reputation |
| Frist | Anzeige, Launch, Antwort, Rückgabe, Register, Gremium oder Verjährung |
| Entscheidung | Go, Go mit Auflagen, Stop, BaFin-Vorabklärung oder externe Spezialprüfung |

### 2. Subsumtion und Geschäftsmodell

Arbeite in dieser Reihenfolge:

1. Lebenssachverhalt und Rollen in einfachen Sätzen festhalten.
2. Geld-, Daten-, Wertpapier- oder Tokenfluss als Tabelle beschreiben.
3. Tatbestandsmerkmale einzeln prüfen.
4. Ausnahmen, Privilegierungen, Bestandsschutz, Übergangsregeln oder Entwurfsstand gesondert behandeln.
5. Gegenargumente und Red-Team-Sicht der Aufsicht formulieren.
6. Praktische Auflagen für Launch, Fortführung, Korrektur oder Ablehnung schreiben.

### 3. Beleg- und Unterlagenliste

| Frage | Beleg | Fehlt | Owner | Wirkung |
| --- | --- | --- | --- | --- |
| Wer erbringt welche Leistung? | Vertrag, Produktbild, Prozess | ... | Legal/Produkt | Regimewahl |
| Fließen Kundengelder oder Kryptowerte? | Flow-of-Funds, Wallet-/Kontoauszug | ... | Operations/Risk | Erlaubnis/Haftung |
| Gibt es Aufsichtskontakt? | Schreiben, Ticket, Portalnachweis | ... | Legal/Compliance | Frist/Strategie |
| Sind Kunden betroffen? | AGB, FAQ, Beschwerde, Marketing | ... | Vertrieb/Legal | Transparenz/Haftung |

### 4. Ergebnis

Erzeuge Settlement-Risikomatrix, Finalitätsfragen, Vertragsbausteine und Operations-Kontrollen.

Baue das Ergebnis mit diesen Elementen:

- **Entscheidungssatz:** Ein Satz, der intern zitiert werden kann.
- **Risikoampel:** Rot/Gelb/Grün mit kurzer Begründung.
- **Auflagen:** Welche Bedingungen müssen vor Go-Live oder vor Antwort erfüllt sein?
- **Offene Punkte:** konkrete Rückfragen statt allgemeiner Rechercheaufträge.
- **Anschluss-Skills:** passende Skills aus `bank-rechtsabteilung` nennen, insbesondere `bafin-kommunikation-und-anhoerung`, `bankaufsichtsrecht-kwg-marisk-triage`, `dora-ict-vertraege-vorfall`, `gwg-aml-kyc-verdachtsmeldung`, `vorstandsvorlage-gutachten` oder `produktfreigabe-new-product-process`.

## Spezialhinweise

- **PSD3/PSR:** Als EU-Gesetzgebungsvorschau behandeln, bis finaler Text und nationale Umsetzung/Anpassung greifbar sind. Keine Scheingeltung behaupten.
- **eWpG/MiCAR:** Immer zuerst trennen, ob der Token ein Finanzinstrument, elektronisches Wertpapier, Kryptowert, E-Geld-Token, vermögenswertreferenzierter Token oder etwas anderes ist.
- **ZAG:** Zahlungsfluss und Besitz an Kundengeldern sind zentral. Grafische Flow-of-Funds-Logik in Worte übersetzen.
- **Geschäftsleiter/FAP:** Nicht nur Einzelperson prüfen, sondern Kollektiveignung, Zeitverfügbarkeit, Interessenkonflikte und Einreichkanal.
- **Tokenisierung:** Keine Technikromantik. Rechtsposition, Register, Verwahrung, Übertragung, Verlustfall, Kundenschutz und Aufsicht zuerst.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 2. `buergschaft-auf-erste-anforderung-bank`

**Fokus:** Bürgschaft oder Garantie auf erste Anforderung aus Bankensicht prüfen: Textauslegung, Abrufmechanik, offensichtlicher Rechtsmissbrauch, einstweiliger Rechtsschutz, Regress gegen Kunden und Dokumentation der Zahlungsentscheidung.

# Bürgschaft auf erste Anforderung

## Fachkern: Bürgschaft auf erste Anforderung
- **Spezialgegenstand:** Bürgschaft auf erste Anforderung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Prüfe Fälle, in denen die Bank sich verpflichtet hat oder verpflichten soll, bei bloßem formalem Abruf zunächst zu zahlen. Der Skill soll verhindern, dass Legal entweder blind zahlt oder reflexhaft blockiert. Entscheidend ist die genaue Trennung zwischen Akzessorietät, selbständiger Garantie, erstem Anfordern, Missbrauchseinwand und späterem Rückforderungs-/Regressprozess.

## Wann nutzen

- Begünstigter verlangt "Zahlung auf erstes Anfordern".
- Kunde bittet, einen Abruf zu stoppen.
- Bank soll fremden Garantietext für Bau, Liefervertrag, M&A, Leasing, Zoll, Steuer oder öffentliche Ausschreibung freigeben.
- Es gibt Eilrechtsschutz, einstweilige Verfügung oder drohenden Fristablauf.

## Kernfragen

| Frage | Warum sie zählt |
| --- | --- |
| Ist es wirklich Bürgschaft oder selbständige Garantie? | Bürgschaft ist akzessorisch; Garantie kann abstrakter sein. |
| Steht "erstes Anfordern" klar und wirksam im Text? | Die Bank darf keine verschärfte Zahlungspflicht hineinlesen. |
| Welche Dokumente verlangt der Abruf? | Formalisierung entscheidet oft über Zahlung oder Zurückweisung. |
| Gibt es offensichtlichen Missbrauch? | Nur klare, liquide belegte Missbrauchslagen rechtfertigen Blockade. |
| Welche Regressbasis besteht? | Bank muss Rückgriff gegen Kunden, Sicherheiten und Kontobelastung prüfen. |

## Normen- und Quellenanker

- §§ 765 ff. BGB für Bürgschaft, Einreden und Forderungsübergang.
- §§ 780, 781 BGB für abstraktere Zahlungsversprechen, soweit einschlägig.
- §§ 305 ff. BGB bei Formulartexten und überraschenden/unklaren Klauseln.
- §§ 349, 350 HGB bei kaufmännischer Bürgschaft.
- ZPO-Eilrechtsschutz prüfen, wenn Abruf blockiert oder Zahlung verhindert werden soll.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwenden; keine BeckRS-/Juris-Blindfundstellen.

## Prüfworkflow

### 1. Text sezieren

Markiere wörtlich aus dem vorgelegten Text:

- Sicherungsgegenstand.
- Höchstbetrag.
- Zahlungsvoraussetzungen.
- Anforderungstext.
- Dokumente.
- Einwendungs-/Einredenverzicht.
- Laufzeit und Erlöschen.
- Rechtswahl/Gerichtsstand.

### 2. Abruf prüfen

| Prüfungspunkt | Ergebnis |
| --- | --- |
| Abrufberechtigte Person | stimmt / unklar / falsch |
| Form | Original, E-Mail, SWIFT, Portal, Brief |
| Frist | innerhalb Laufzeit? |
| Betrag | innerhalb Höchstbetrag? |
| Dokumente | vollständig? |
| Erklärung | exakt wie vereinbart? |
| Missbrauch | nur wenn evident und belegbar |

### 3. Zahlungsentscheidung

Erstelle eine Ampel:

- **Grün zahlen:** Formal abrufbar, keine liquiden Missbrauchsbelege, Regress gesichert.
- **Gelb halten:** Formmangel, unklare Vertretung, widersprüchliche Dokumente, sofortige Nachforderung möglich.
- **Rot stoppen:** eindeutige Fälschung, falscher Begünstigter, abgelaufene Laufzeit, Betrag überschritten, evidenter Missbrauch.

### 4. Regress und Kommunikation

Formuliere:

- Nachricht an Kunden: Was liegt vor, wann droht Zahlung, welche Belege braucht die Bank sofort?
- Nachricht an Begünstigten: formale Rückfrage oder Zurückweisung ohne unnötige materiellrechtliche Diskussion.
- Internen Freigabevermerk: warum Zahlung/Stop dokumentationsfest ist.
- Sicherheiten- und Kontobelastungsplan.

## Anschluss-Skills

- `avalrahmenlinie-kautionsaval-praxis` für Avalrahmen und Kautionsaval.
- `garantieabruf-missbrauch-und-zahlungsstopp` für Eilfall.
- `kreditsicherheiten-bestellung-verwertung` für Regress und Sicherheiten.
- `litigation-schlichtung-prozess` für gerichtlichen Streit.

## 3. `buergschaft-privatperson-gesellschafter-ehegatte`

**Fokus:** Privatpersonen-, Gesellschafter- und Ehegattenbürgschaften aus Bankensicht prüfen: Schriftform, krasse finanzielle Überforderung, Sittenwidrigkeit, Verbraucherschutz, Aufklärung, Sicherheitenwert und Prozessrisiko.

# Buergschaft Privatperson Gesellschafter Ehegatte

## Aufgabe

Skill fuer Buergschaft Privatperson / Gesellschafter / Ehegatte — Wirksamkeit und Sittenwidrigkeit.

## Norm

- **§§ 765-778 BGB**: Buergschaft.
- **§ 766 BGB**: Schriftformerfordernis.
- **§ 138 BGB**: Sittenwidrigkeit.

## Drei Konstellationen

### Gesellschafter-Buergschaft
- Gesellschafter buergt fuer Kredit der eigenen GmbH/AG.
- Wirksam, weil unmittelbares Eigeninteresse.

### Ehegatten-Buergschaft
- Ehegatte buergt fuer Kredit des anderen Ehegatten oder seines Unternehmens.
- **BGH XI ZR 56/93** (19.01.1999) zur Sittenwidrigkeit bei "krasser Vermoegensueberforderung".
- Voraussetzungen:
 - Buergin/Buerge hat kein nennenswertes Einkommen / Vermoegen.
 - Buergschaft uebersteigt Pfaendungsmoeglichkeit drastisch.
 - Buergin emotional verbunden mit Hauptschuldner.

### Drittbuergschaft (z. B. Eltern fuer Kinder)
- Aehnliche Pruefung wie Ehegatte.

## Sittenwidrigkeit § 138 BGB

- BGH-Linie: ca. 1 Prozent monatliche Tilgungsfaehigkeit als Schwelle.
- Bei Unterschreitung: vermutung Sittenwidrigkeit.

## Pruefraster

1. Verhaeltnis Buerge - Hauptschuldner?
2. Eigeninteresse?
3. Tilgungsfaehigkeit?
4. Sittenwidrigkeit?

## Output

- Wirksamkeitspruefung.
- Klage bei Inanspruchnahme.

## 4. `chargeback-card-schemes-bankrecht`

**Fokus:** Chargeback und Card-Scheme-Disputes rechtlich begleiten: Mastercard/Visa-Regeln, Zahlungsdienstehaftung, Händlerstreit, Fristen, Belege, Kundenerwartung und Kulanzgrenzen.

# Chargeback und Kartenstreit

## Fachkern: Chargeback und Kartenstreit
- **Spezialgegenstand:** Chargeback und Kartenstreit. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Kunde verlangt Kartenrückbuchung oder Händler/Acquirer streitet über Chargeback, Fraud oder Ware nicht erhalten.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Kartentransaktion, Scheme, Reason Code, Belege, Fristen, Händlerantwort, Kundenkommunikation.
- **Institut und Rolle:** Bank, Zahlungsinstitut, E-Geld-Institut, Wertpapierinstitut, CRR-Kreditinstitut, FinTech-Tochter, Vermittler, Agent, Registerführer, CASP, Emittent oder Dienstleister.
- **Produkt oder Vorgang:** Zahlungsdienst, E-Geld, Kredit, Wertpapier, Token, Register, Organwechsel, Auslagerung, Betrugsfall, Trade Finance oder Kooperation.
- **Aufsicht und Einreichweg:** BaFin, Bundesbank, EZB/SSM, EBA, FIU, Register, MVP, IMAS, Bundesanzeiger, Handelsregister oder interner Ausschuss.
- **Dokumente:** Produktbeschreibung, Flow-of-Funds, Vertragsentwurf, API-Doku, Token Terms, Organ-CV, Eignungsmatrix, Registerauszug, Kundenkommunikation, Logs oder Vorstandsvorlage.

## Prüfaufbau

### 1. Kurzbild

| Punkt | Klärung |
| --- | --- |
| Ergebnisbedarf | Vermerk, Freigabe, BaFin-Anfrage, Vertrag, Vorstandsvorlage oder Prozessstrategie |
| Rechtsregime | KWG, ZAG, WpHG, WpIG, eWpG, MiCAR, DORA, GwG, BGB, HGB, AktG, SEPA-/EU-Regime oder Entwurf |
| Risiko | Aufsicht, Bußgeld, Zivilhaftung, Organhaftung, Kundenstreit, AML, Datenschutz, IT oder Reputation |
| Frist | Anzeige, Launch, Antwort, Rückgabe, Register, Gremium oder Verjährung |
| Entscheidung | Go, Go mit Auflagen, Stop, BaFin-Vorabklärung oder externe Spezialprüfung |

### 2. Subsumtion und Geschäftsmodell

Arbeite in dieser Reihenfolge:

1. Lebenssachverhalt und Rollen in einfachen Sätzen festhalten.
2. Geld-, Daten-, Wertpapier- oder Tokenfluss als Tabelle beschreiben.
3. Tatbestandsmerkmale einzeln prüfen.
4. Ausnahmen, Privilegierungen, Bestandsschutz, Übergangsregeln oder Entwurfsstand gesondert behandeln.
5. Gegenargumente und Red-Team-Sicht der Aufsicht formulieren.
6. Praktische Auflagen für Launch, Fortführung, Korrektur oder Ablehnung schreiben.

### 3. Beleg- und Unterlagenliste

| Frage | Beleg | Fehlt | Owner | Wirkung |
| --- | --- | --- | --- | --- |
| Wer erbringt welche Leistung? | Vertrag, Produktbild, Prozess | ... | Legal/Produkt | Regimewahl |
| Fließen Kundengelder oder Kryptowerte? | Flow-of-Funds, Wallet-/Kontoauszug | ... | Operations/Risk | Erlaubnis/Haftung |
| Gibt es Aufsichtskontakt? | Schreiben, Ticket, Portalnachweis | ... | Legal/Compliance | Frist/Strategie |
| Sind Kunden betroffen? | AGB, FAQ, Beschwerde, Marketing | ... | Vertrieb/Legal | Transparenz/Haftung |

### 4. Ergebnis

Liefer Fristen- und Belegmatrix, Scheme-Fragen, Kundenbrief, Eskalationsoption und Prozessrisiko.

Baue das Ergebnis mit diesen Elementen:

- **Entscheidungssatz:** Ein Satz, der intern zitiert werden kann.
- **Risikoampel:** Rot/Gelb/Grün mit kurzer Begründung.
- **Auflagen:** Welche Bedingungen müssen vor Go-Live oder vor Antwort erfüllt sein?
- **Offene Punkte:** konkrete Rückfragen statt allgemeiner Rechercheaufträge.
- **Anschluss-Skills:** passende Skills aus `bank-rechtsabteilung` nennen, insbesondere `bafin-kommunikation-und-anhoerung`, `bankaufsichtsrecht-kwg-marisk-triage`, `dora-ict-vertraege-vorfall`, `gwg-aml-kyc-verdachtsmeldung`, `vorstandsvorlage-gutachten` oder `produktfreigabe-new-product-process`.

## Spezialhinweise

- **PSD3/PSR:** Als EU-Gesetzgebungsvorschau behandeln, bis finaler Text und nationale Umsetzung/Anpassung greifbar sind. Keine Scheingeltung behaupten.
- **eWpG/MiCAR:** Immer zuerst trennen, ob der Token ein Finanzinstrument, elektronisches Wertpapier, Kryptowert, E-Geld-Token, vermögenswertreferenzierter Token oder etwas anderes ist.
- **ZAG:** Zahlungsfluss und Besitz an Kundengeldern sind zentral. Grafische Flow-of-Funds-Logik in Worte übersetzen.
- **Geschäftsleiter/FAP:** Nicht nur Einzelperson prüfen, sondern Kollektiveignung, Zeitverfügbarkeit, Interessenkonflikte und Einreichkanal.
- **Tokenisierung:** Keine Technikromantik. Rechtsposition, Register, Verwahrung, Übertragung, Verlustfall, Kundenschutz und Aufsicht zuerst.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 5. `correspondent-banking-nostro-vostro`

**Fokus:** Korrespondenzbankbeziehungen und Nostro/Vostro-Risiken prüfen: AML, Sanktionen, Länder, Zahlungswege, Vertragsklauseln, Informationsrechte, Kündigung und Aufsichtserwartungen.

# Correspondent Banking

## Fachkern: Correspondent Banking
- **Spezialgegenstand:** Correspondent Banking. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank führt oder nutzt Korrespondenzbankkonten oder muss Relationship Review, Exit oder Questionnaire beantworten.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Korrespondenzbank, Länder, Produkte, Zahlungsvolumen, AML-Fragebogen, Sanktionen, Audit-Rechte.
- **Institut und Rolle:** Bank, Zahlungsinstitut, E-Geld-Institut, Wertpapierinstitut, CRR-Kreditinstitut, FinTech-Tochter, Vermittler, Agent, Registerführer, CASP, Emittent oder Dienstleister.
- **Produkt oder Vorgang:** Zahlungsdienst, E-Geld, Kredit, Wertpapier, Token, Register, Organwechsel, Auslagerung, Betrugsfall, Trade Finance oder Kooperation.
- **Aufsicht und Einreichweg:** BaFin, Bundesbank, EZB/SSM, EBA, FIU, Register, MVP, IMAS, Bundesanzeiger, Handelsregister oder interner Ausschuss.
- **Dokumente:** Produktbeschreibung, Flow-of-Funds, Vertragsentwurf, API-Doku, Token Terms, Organ-CV, Eignungsmatrix, Registerauszug, Kundenkommunikation, Logs oder Vorstandsvorlage.

## Prüfaufbau

### 1. Kurzbild

| Punkt | Klärung |
| --- | --- |
| Ergebnisbedarf | Vermerk, Freigabe, BaFin-Anfrage, Vertrag, Vorstandsvorlage oder Prozessstrategie |
| Rechtsregime | KWG, ZAG, WpHG, WpIG, eWpG, MiCAR, DORA, GwG, BGB, HGB, AktG, SEPA-/EU-Regime oder Entwurf |
| Risiko | Aufsicht, Bußgeld, Zivilhaftung, Organhaftung, Kundenstreit, AML, Datenschutz, IT oder Reputation |
| Frist | Anzeige, Launch, Antwort, Rückgabe, Register, Gremium oder Verjährung |
| Entscheidung | Go, Go mit Auflagen, Stop, BaFin-Vorabklärung oder externe Spezialprüfung |

### 2. Subsumtion und Geschäftsmodell

Arbeite in dieser Reihenfolge:

1. Lebenssachverhalt und Rollen in einfachen Sätzen festhalten.
2. Geld-, Daten-, Wertpapier- oder Tokenfluss als Tabelle beschreiben.
3. Tatbestandsmerkmale einzeln prüfen.
4. Ausnahmen, Privilegierungen, Bestandsschutz, Übergangsregeln oder Entwurfsstand gesondert behandeln.
5. Gegenargumente und Red-Team-Sicht der Aufsicht formulieren.
6. Praktische Auflagen für Launch, Fortführung, Korrektur oder Ablehnung schreiben.

### 3. Beleg- und Unterlagenliste

| Frage | Beleg | Fehlt | Owner | Wirkung |
| --- | --- | --- | --- | --- |
| Wer erbringt welche Leistung? | Vertrag, Produktbild, Prozess | ... | Legal/Produkt | Regimewahl |
| Fließen Kundengelder oder Kryptowerte? | Flow-of-Funds, Wallet-/Kontoauszug | ... | Operations/Risk | Erlaubnis/Haftung |
| Gibt es Aufsichtskontakt? | Schreiben, Ticket, Portalnachweis | ... | Legal/Compliance | Frist/Strategie |
| Sind Kunden betroffen? | AGB, FAQ, Beschwerde, Marketing | ... | Vertrieb/Legal | Transparenz/Haftung |

### 4. Ergebnis

Erzeuge Relationship-Risk-Review, Vertragscheck, Nachforderungsliste und Management Summary.

Baue das Ergebnis mit diesen Elementen:

- **Entscheidungssatz:** Ein Satz, der intern zitiert werden kann.
- **Risikoampel:** Rot/Gelb/Grün mit kurzer Begründung.
- **Auflagen:** Welche Bedingungen müssen vor Go-Live oder vor Antwort erfüllt sein?
- **Offene Punkte:** konkrete Rückfragen statt allgemeiner Rechercheaufträge.
- **Anschluss-Skills:** passende Skills aus `bank-rechtsabteilung` nennen, insbesondere `bafin-kommunikation-und-anhoerung`, `bankaufsichtsrecht-kwg-marisk-triage`, `dora-ict-vertraege-vorfall`, `gwg-aml-kyc-verdachtsmeldung`, `vorstandsvorlage-gutachten` oder `produktfreigabe-new-product-process`.

## Spezialhinweise

- **PSD3/PSR:** Als EU-Gesetzgebungsvorschau behandeln, bis finaler Text und nationale Umsetzung/Anpassung greifbar sind. Keine Scheingeltung behaupten.
- **eWpG/MiCAR:** Immer zuerst trennen, ob der Token ein Finanzinstrument, elektronisches Wertpapier, Kryptowert, E-Geld-Token, vermögenswertreferenzierter Token oder etwas anderes ist.
- **ZAG:** Zahlungsfluss und Besitz an Kundengeldern sind zentral. Grafische Flow-of-Funds-Logik in Worte übersetzen.
- **Geschäftsleiter/FAP:** Nicht nur Einzelperson prüfen, sondern Kollektiveignung, Zeitverfügbarkeit, Interessenkonflikte und Einreichkanal.
- **Tokenisierung:** Keine Technikromantik. Rechtsposition, Register, Verwahrung, Übertragung, Verlustfall, Kundenschutz und Aufsicht zuerst.

## Correspondent-Banking-Spezifika
- Rechtsrahmen AML: § 15 GwG (verstärkte Sorgfaltspflichten Korrespondenzbeziehungen mit Banken aus Drittstaaten), § 25 GwG (Verbot Beziehungen mit Shell Banks/Briefkastenbanken), BaFin-Auslegungshinweise zu Korrespondenzbankbeziehungen, Wolfsberg Principles (Industry-Standard), FATF Recommendations 13.
- KYCC (Know Your Customer's Customer): Bank muss Vertragspartner verstehen — Branche, Geschäftsmodell, Kundenstruktur, AML-Programm, Aufsichtsregime; jährliche Reviews; bei US-Cleaningbank zusätzlich USA-PATRIOT-Act-Compliance (Section 312, OFAC).
- Sanktionsexposure: Korrespondenzbank kann unfreiwillig SDN-/EU-Sanktionstreffer durchschleusen; STP-Filter, BIC-Blacklist, MT103-Format ggf. nachrichtenbezogen filtern; bei Schein-Wege Pflicht zur Risikobewertung.
- Operationelles Risiko: Nostro/Vostro-Salden überwachen (Liquiditätsrisiko), Cut-off-Times, Settlement-Risiko (CLS für FX); DORA-Resilience-Pflichten für SWIFT-Anbindung als kritische ICT (Art. 28 DORA-VO).
- Praktiker-Tipp: Onboarding-Pack mit Wolfsberg-CBDDQ, jährliches Refresh, CSR-Reports auswerten; bei Risikoindikatoren Down-Scope oder Termination, dokumentierte Entscheidung; bei Sanktions-Trigger sofort Hold + BaFin/Bundesbank-Meldung; § 11 GwG: Identifizierung CIO/MLRO der Korrespondenzbank ist Pflicht, nicht nur Vorstand.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?
