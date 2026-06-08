---
name: widerspruch
description: "Erstellt einen formellen Widerspruchsbrief gegen die Ablehnung eines Fahrgastrechte-Antrags der Deutschen Bahn oder eines anderen Eisenbahnverkehrsunternehmens. Verwende diesen Skill immer wenn der Nutzer ein Ablehnungsschreiben des DB-Servicecenters Fahrgastrechte (oder gleichwertiger EVU-Stelle) zum Thema Verspaetungsentschaedigung erwaehnt einen Widerspruch gegen die Deutsche Bahn formulieren moechte oder Begriffe wie Fahrgastrechte Verspaetungsentschaedigung Servicecenter Fahrgastrechte Entschaedigungsantrag abgelehnt oder DB Ablehnung verwendet. Strukturierter Schriftsatz mit Pinpoint auf konkreten Ablehnungsgrund und Anlagen-YAML."
---

# Fahrgastrechte-Widerspruch — Skill

## Zweck

Analysiert drei Eingabedokumente (Ablehnungsschreiben der DB, ursprünglicher Antrag, Ticket) und erstellt daraus einen juristisch fundierten Widerspruchsbrief als strukturierten Schriftsatz, den der Nutzer an das Servicecenter Fahrgastrechte der Deutschen Bahn (oder das jeweils ausführende EVU) senden kann. Der Brief wird mit dem Skill `fahrgastrechte-anlagen-bauen` in ein beA-konformes Anlagenkonvolut überführt.

## Eingabedokumente

Der Nutzer lädt typischerweise drei Dokumente hoch:

1. **Ablehnungsschreiben der DB** — der Brief, in dem die DB den Antrag ablehnt (PDF oder Foto).
2. **Ursprünglicher Antrag** — das vom Nutzer ausgefüllte Fahrgastrechte-Formular bzw. die Bestätigung (PDF, Screenshot oder Foto).
3. **Ticket / Fahrkarte** — das Original-Ticket als Nachweis der Buchung (PDF aus der DB-App, Scan oder Foto).

Die Dokumente können als PDF (digital oder gescannt), als Screenshots oder als Fotos vorliegen. Wenn die Qualität nicht ausreicht, um relevante Informationen zu extrahieren, den Nutzer bitten, die fehlenden Daten manuell einzugeben.

## Workflow

### Schritt 1: Dokumente identifizieren und lesen

Sichte die hochgeladenen Dateien. Jedes Dokument identifizieren:

- **Ablehnungsschreiben erkennen an:** Absender "Servicecenter Fahrgastrechte", "DB Dialog" oder vergleichbarer EVU-Stelle; Formulierungen wie "Ihrem Antrag können wir leider nicht entsprechen"; Aktenzeichen / Vorgangsnummer.
- **Antrag erkennen an:** Formulardaten mit Verbindungsdaten, Verspätungsangaben, IBAN.
- **Ticket erkennen an:** Buchungsnummer (PNR / Auftragsnummer), Zugbindung, Tarifart, Reisedatum, Verbindungsdetails.

Bei Bildern / Screenshots: Inhalte direkt aus dem Kontext lesen. Bei gescannten PDFs mit schlechter Textextraktion: Seiten als Bilder rendern und visuell auswerten.

### Schritt 2: Relevante Daten extrahieren

Aus den drei Dokumenten folgende Informationen sammeln:

**Aus dem Ticket:**

- Ticketart: Flexpreis, Sparpreis, Super Sparpreis, BahnCard-Ticket, Deutschlandticket, Zeitkarte
- Buchungsnummer / Auftragsnummer
- Reisedatum
- Gebuchte Verbindung (Abfahrt → Ankunft, Umstiege, Zugnummern)
- Preis
- Zugbindung ja/nein (Flexpreis = keine Zugbindung → alternative Verbindungen erlaubt)
- Klasse (1./2.)
- Reisende:r
- Operating EVU (falls Konkurrenz auf bahn.de gebucht)

**Aus dem Antrag:**

- Tatsächlich gefahrene Verbindung
- Angegebene Endziel-Verspätung
- Datum des Antrags
- Beantragter Erstattungs-/Entschädigungsbetrag
- Ggf. Verpflegungskosten, Taxikosten, Hotelkosten

**Aus dem Ablehnungsschreiben:**

- Aktenzeichen / Vorgangsnummer
- Datum des Schreibens
- Konkreter Ablehnungsgrund (genauen Wortlaut notieren)
- Sachbearbeiter (falls angegeben)
- Antwortadresse

### Schritt 3: Rechtliche Analyse

Lies die References dieses Plugins (`references/vo-2021-782-uebersicht.md`, `references/evo-2023-uebersicht.md`, `references/db-tarif-und-agb.md`) und konsultiere insbesondere `skills/db-ablehnungsgruende-pruefen/SKILL.md` für das vorliegende Ablehnungs-Muster.

Kernpunkte der Analyse:

1. **Verspätungsdauer prüfen:** Ab 60 Min = 25 % des Fahrpreises, ab 120 Min = 50 %.
2. **Ablehnungsgrund identifizieren und widerlegen** — Pinpoint auf den jeweiligen Eintrag in `db-ablehnungsgruende-pruefen`.
3. **Ticketart berücksichtigen:**
   - Flexpreis: keine Zugbindung → Fahrgast durfte jede beliebige Verbindung auf der Strecke nehmen.
   - Sparpreis: Zugbindung, aber bei voraussichtlich > 20 Min Verspätung aufgehoben (Ziffer 9 BB DB) → Reisender darf umsteigen.
   - Deutschlandticket / Zeitkarte: Entschädigung pauschal nach Tarifbestimmungen (siehe `db-tarif-und-agb.md`).
4. **Verpflegungs-, Taxi-, Hotel-Ansprüche:** Art. 18 Abs. 3 (100-Min-Frist Eigenbeförderung), Art. 20 (60-Min-Hilfeleistung), § 11 EVO (SPNV, 20-Min-Schwelle, 120-EUR-Höchstbetrag).
5. **Befreiung Art. 19 Abs. 10 VO:** Streiks DB-Personal, Handlungen Infrastrukturbetreiber sind ausdrücklich KEINE Befreiungsgründe.

### Schritt 4: Widerspruchsbrief erstellen

Der Brief wird als strukturierter Schriftsatz nach folgender Vorlage erstellt:

```
[Name und Adresse der/des Reisenden — aus dem Ticket/Antrag]
[Tel] [E-Mail]
[IBAN]

                                    DB Dialog GmbH
                                    Servicecenter Fahrgastrechte
                                    60647 Frankfurt am Main

[Ort], den [aktuelles Datum]

Betreff: Widerspruch gegen Ablehnung meines Entschädigungsantrags
         Aktenzeichen / Vorgangsnummer: [Nummer aus dem Ablehnungsschreiben]
         Mein Schreiben vom [Datum des Ursprungsantrags]
         Ihr Ablehnungsschreiben vom [Datum]

Sehr geehrte Damen und Herren,

[Absatz 1: Bezugnahme]
mit Schreiben vom [Datum] haben Sie meinen Entschädigungsantrag mit dem
Aktenzeichen [Vorgangsnummer] abgelehnt. Gegen diese Entscheidung lege ich
hiermit Widerspruch ein.

[Absatz 2: Sachverhaltsdarstellung]
Am [Datum] reiste ich mit dem [Zug + Nummer] von [Abfahrtsbahnhof] nach
[Zielbahnhof]. Planmäßige Ankunft war um [HH:MM]. Tatsächlich erreichte
ich das Ziel erst um [HH:MM], was einer Verspätung von [X] Minuten am
Zielort entspricht (gemessen an der Türöffnung am Bahnsteig, Art. 3 Nr. 18
VO (EU) 2021/782).

[Absatz 3 — nur bei Bedarf: Flexpreis-Argument]
Bei meinem Ticket handelt es sich um ein Flexpreis-Ticket ohne Zugbindung.
Ich war daher berechtigt, jeden beliebigen Zug auf meiner gebuchten Strecke
zu nutzen. Die in Ihrem Ablehnungsschreiben angeführte Argumentation, ich
hätte eine andere als die gebuchte Verbindung genutzt, geht ins Leere.
Maßgeblich ist ausschließlich die Verspätung am Zielbahnhof.

[Absatz 3 alternativ — Sparpreis mit Zugbindungsaufhebung]
Zwar handelt es sich um ein Sparpreis-Ticket mit grundsätzlicher Zugbindung.
Da jedoch bereits am Abfahrtsbahnhof eine Verspätung von mehr als 20 Minuten
am Zielort absehbar war, wurde die Zugbindung gemäß Ziffer 9 der
Beförderungsbedingungen der Deutschen Bahn aufgehoben. Ich war berechtigt,
einen alternativen Zug zu nutzen.

[Absatz 4: Rechtliche Begründung]
Gemäß Art. 19 Abs. 1 [lit. a / lit. b] VO (EU) 2021/782 steht mir bei einer
Verspätung von mehr als [60 / 120] Minuten am Zielort eine Entschädigung in
Höhe von [25 / 50] Prozent des Fahrpreises zu. Der von Ihnen angeführte
Ablehnungsgrund "[Grund zitieren]" steht diesem Anspruch nicht entgegen, da
[konkrete Gegenargumentation aus db-ablehnungsgruende-pruefen — mit
Pinpoint auf den entsprechenden Artikel der VO 2021/782 oder § der EVO].

[Absatz 5 — falls Verpflegung / Hotel / Eigenbeförderung]
Darüber hinaus steht mir gemäß [Art. 20 / Art. 18 Abs. 3 Unterabs. 2] VO
(EU) 2021/782 [eine angemessene Verpflegung / eine eigenständige Beförderung]
zu. Da mir [diese von Ihnen nicht bereitgestellt wurde / Sie binnen 100
Minuten keine Alternativverbindung mitgeteilt haben], war ich gezwungen,
[Verpflegung im Wert von / Ersatzbeförderung im Wert von] [Betrag] EUR
selbst zu beschaffen. Ich bitte um Erstattung dieser Kosten.

[Absatz 6: Forderung und Frist]
Ich bitte Sie, meinen Widerspruch innerhalb von vier Wochen ab Zugang dieses
Schreibens zu prüfen und mir die zustehende Entschädigung in Höhe von
[Gesamtbetrag] EUR auf das in meinem ursprünglichen Antrag genannte Konto
zu überweisen.

Sollte meinem Widerspruch nicht entsprochen werden, behalte ich mir vor,
die Schlichtungsstelle Reise & Verkehr e.V. (vormals söp — Schlichtungs-
stelle für den öffentlichen Personenverkehr), Fasanenstraße 81, 10623
Berlin, anzurufen. Das Verfahren ist für mich als Verbraucher kostenfrei
(§§ 4 ff. VSBG). Anschließend werde ich Klage zum zuständigen Amtsgericht
erheben.

Mit freundlichen Grüßen

[Name]

Anlagen:
 K1 Kopie des Originaltickets
 K2 Kopie des ursprünglichen Antrags
 K3 Kopie des Ablehnungsschreibens
 K4 [ggf. Belege Verpflegung / Hotel / Ersatzbeförderung]
```

#### Stilrichtlinien für den Brief

- **Sachlich und bestimmt**, nicht aggressiv — aber klar in der Forderung.
- **Konkrete Rechtsnormen** zitieren (VO (EU) 2021/782 mit Artikel, EVO mit Paragraph, DB-Tarifbestimmungen mit Ziffer).
- **Spezifisch auf den Ablehnungsgrund eingehen** — nicht pauschal argumentieren. Auf den entsprechenden Punkt in `db-ablehnungsgruende-pruefen` Bezug nehmen.
- **Fristen setzen:** Antwort in angemessener Frist erbitten. Praxis: vier Wochen oder ein Monat — die Bearbeitungsfrist nach Art. 19 Abs. 7 VO ist auf einen Monat angelegt; vier Wochen sind kürzer (28 Tage) und können bei Streit über den Verzugseintritt nachteilig sein.
- **Schlichtungsstelle erwähnen:** Hinweis auf Schlichtungsstelle Reise & Verkehr e.V. (vormals söp) als nächsten Schritt.
- **Förmlich aber nicht übertrieben juristisch** — der Brief soll von einer Privatperson kommen können, nicht zwingend von einem Anwalt.

### Schritt 5: Ausgabe und Anlagen-Übergabe

1. Den fertigen Brief als `widerspruch-<datum>.md` und PDF in der Fallakte ablegen.
2. Direkt im Anschluss den Skill `fahrgastrechte-anlagen-bauen` aufrufen.

**Anlagen-Übergabe-Schema:**

```yaml
schriftsatz: widerspruch-<datum>.md
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # Sammel-PDF Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold        # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

3. Dem Nutzer eine kurze Zusammenfassung geben:
   - Welcher Ablehnungsgrund identifiziert wurde
   - Welche Gegenargumente verwendet wurden (mit Norm-Pinpoint)
   - Welcher Entschädigungsbetrag gefordert wird
   - Empfehlung für nächste Schritte (Schlichtungsstelle Reise & Verkehr falls erneut abgelehnt — Skill `schlichtung-reise-verkehr-anrufen`)

## Fehlende Informationen

Falls wichtige Informationen nicht aus den Dokumenten extrahiert werden können, den Nutzer gezielt fragen — zum Beispiel:

- "Wie viel Verspätung hattest du am Zielbahnhof genau (Türöffnung am Bahnsteig)?"
- "Hast du eine alternative Verbindung genommen? Wenn ja, welche?"
- "Hattest du Ausgaben für Verpflegung, Taxi oder Hotel? Wenn ja, wie viel?"
- "Wie lautet deine Adresse für den Briefkopf?"
- "War der Zug im Fernverkehr (ICE / IC / FlixTrain) oder Nahverkehr (RE / RB)?"

Nicht alle Informationen auf einmal abfragen, sondern nur das, was wirklich fehlt.

## Wichtige Hinweise

- **Kein "Keine-Rechtsberatung"-Disclaimer im Brief selbst** — der Brief soll wie ein normaler Widerspruch einer Privatperson aussehen.
- **Aber dem Nutzer im Chat sagen:** "Das ist keine Rechtsberatung. Im Zweifel einen Anwalt oder eine Verbraucherzentrale konsultieren."
- **Datum:** Immer das aktuelle Datum verwenden, nicht das Datum des Ablehnungsschreibens.
- **Beschwerdefrist Art. 27 VO:** Die 3-Monats-Frist ist eine Verfahrensfrist — keine Ausschlussfrist für den materiellen Anspruch. § 195 BGB (3 Jahre) bleibt maßgeblich.
- **Bei Anwaltsmandat** zusätzlich den Standardsatz aus CLAUDE.md am Briefende mit aufnehmen: Berufsbezeichnung, Mandatsverhältnis, Kostenhinweis (RVG / Honorarvereinbarung).

## Anschluss-Skills

- Wenn DB auch auf Widerspruch ablehnt oder schweigt: `schlichtung-reise-verkehr-anrufen`.
- Wenn Klage nötig: `klage-amtsgericht-fahrgast`.
- Für die Ablehnungsgrund-Analyse: `db-ablehnungsgruende-pruefen`.

## Quellen

- VO (EU) 2021/782 — eur-lex.europa.eu (CELEX 32021R0782)
- EVO 2023 — gesetze-im-internet.de/evo_2023
- DB-Beförderungsbedingungen — bahn.de/agb
- Schlichtungsstelle Reise & Verkehr e.V. — schlichtungsstelle-reise-verkehr.de

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
