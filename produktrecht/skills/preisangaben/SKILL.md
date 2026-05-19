---
name: preisangaben
description: Prüft die Einhaltung der Preisangabenverordnung 2022 (PAngV) bei Gesamtpreisen, Grundpreisen, Streichpreisen und Versandkosten, insbesondere die 30-Tage-Niedrigstpreisregel bei Preisreduzierungen. Lädt bei Fragen zu Preisauszeichnung, Rabattaktionen, Sale-Kennzeichnung und Grundpreisangabe.
language: de
triggers:
  - "Preisangaben"
  - "PAngV"
  - "Grundpreis"
  - "Streichpreis"
  - "30-Tage-Niedrigstpreis"
  - "Preisauszeichnung"
  - "Versandkosten"
  - "Gesamtpreis"
  - "Sale Kennzeichnung"
  - "Preisreduzierung"
---

# Preisangaben (PAngV 2022)

## Zweck

Dieser Skill begleitet die rechtskonforme Preisauszeichnung gegenüber Verbrauchern nach der Preisangabenverordnung 2022 (PAngV, in Kraft getreten 28.05.2022 zur Umsetzung der EU-Omnibus-Richtlinie). Er deckt Gesamtpreis, Grundpreis, Streichpreise (insb. 30-Tage-Niedrigstpreis nach § 11 PAngV), Versandkosten und die UWG-Rechtsfolgen ab. Anwendungsfälle: Online-Shop-Preisauszeichnung, Black-Friday-Sale, Streichpreiswerbeaktion, Grundpreispflicht für Lebensmittel/Kosmetik, B2C-Preiskommunikation.

## Eingaben

Das Modell benötigt:

- **Art des Angebots**: Online-Shop, stationärer Handel, Werbeanzeige (Online/Print/Social Media)?
- **Produkt**: Lebensmittel, Kosmetik, Drogerieartikel, Elektronik, Textilien?
- **Preisstruktur**: Endpreis inkl. MwSt., Grundpreis (Menge/Gewicht), Versandkosten?
- **Preisreduktion**: Liegt eine Preissenkung vor? Wie wird sie kommuniziert (Streichpreis, Prozentangabe „-30 %", „Sale")?
- **Referenzpreis**: Was ist der Referenzpreis für die Streichpreisangabe? Seit wann galt er?
- **30-Tage-Preishistorie**: Was war der niedrigste Preis in den letzten 30 Tagen vor der Preisreduzierung?
- **Zielgruppe**: Ausschließlich Verbraucher (B2C) oder auch Unternehmer (B2B)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 3 PAngV (Gesamtpreis)**: Gegenüber Verbrauchern ist stets der Gesamtpreis (einschließlich aller Steuern und Abgaben) anzugeben; eindeutig, leicht erkennbar, gut lesbar oder hörbar.
- **§ 4 PAngV (Grundpreis)**: Bei Erzeugnissen nach Gewicht, Volumen, Länge oder Fläche ist neben dem Gesamtpreis der Grundpreis pro Mengeneinheit anzugeben; gilt für Lebensmittel, Kosmetika, Waschmittel, Tierfutter u.a. Ausnahmen: § 9 PAngV (Kleinunternehmen, Einzelhandel).
- **§ 6 PAngV (Versandkosten)**: Versandkosten sind klar anzugeben oder darauf hinzuweisen, dass weitere Kosten anfallen, bevor der Verbraucher seine Bestellung abgibt; kein verstecktes Aufschlagen nach Checkout-Einstieg.
- **§ 11 PAngV (Streichpreis/Preisreduzierung)**: Bei Ankündigung einer Preisermäßigung muss als Referenzpreis der niedrigste Gesamtpreis verwendet werden, den der Händler in den letzten 30 Tagen vor der Preisreduzierung gegenüber Verbrauchern gefordert hat (Umsetzung Art. 6a Preisangaben-RL, eingefügt durch Omnibus-RL 2019/2161).
- **§ 5a Abs. 2, 4 UWG**: Vorenthalten wesentlicher Preisangaben als unlautere Handlung; Grundlage für Unterlassungsansprüche, Abmahnungen, einstweiligen Rechtsschutz.
- **§ 19 PAngV (Bußgeld)**: Verstöße gegen PAngV sind Ordnungswidrigkeiten; Bußgeld bis 25.000 EUR.

### Leitentscheidungen

1. EuGH, Urt. v. 26.09.2024 – C-330/23 (Aldi Süd/Verbraucherzentrale), NJW 2024, 3561 Rn. 42–68: Der Begriff „niedrigster Preis" in Art. 6a Preisangaben-RL (§ 11 PAngV) umfasst ausnahmslos den tatsächlich geforderten Gesamtpreis der letzten 30 Tage; es kommt nicht auf einen „regulären" oder „üblichen" Preis an. Sonderaktionspreise innerhalb des 30-Tage-Zeitraums (z.B. Einführungspreise) müssen als Referenz verwendet werden, wenn sie den Niedrigstpreis darstellen.

2. BGH, Urt. v. 10.11.2022 – I ZR 16/22, GRUR 2023, 162 Rn. 22–35 – „Streichpreis Online": Vor Umsetzung der Omnibus-RL war die Verwendung eines Streichpreises, der nicht dem tatsächlich geforderten Preis entspricht, als irreführende Werbung nach §§ 5, 5a UWG abmahnfähig. Diese Wertung gilt fort; § 11 PAngV konkretisiert nunmehr den zulässigen Referenzpreis verbindlich.

### Kommentarliteratur

1. Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 42. Aufl. 2024, PAngV § 11 Rn. 5–30: Zu den Anforderungen an die 30-Tage-Niedrigstpreisregel im Einzelnen; Fallgruppen (Staffelrabatte, Loyalitätsprogramme, Einführungspreise); Verhältnis zu § 5 UWG bei irreführenden Streichpreisen außerhalb des PAngV-Anwendungsbereichs.

2. Sosnitza, in: Ohly/Sosnitza, UWG, 8. Aufl. 2023, PAngV Vorbem. Rn. 10–40: Zur Systematik der PAngV 2022 als Marktverhaltensregel i.S.d. § 3a UWG; Rechtsfolgen bei PAngV-Verstößen (Unterlassung, Schadensersatz, Gewinnabschöpfung); Abmahnberechtigung nach § 8 Abs. 3 UWG.

## Ablauf

**Schritt 1 – Pflicht zur Gesamtpreisangabe prüfen (§ 3 PAngV)**
- Richtet sich das Angebot an Verbraucher (§ 13 BGB)?
- Gesamtpreis inkl. MwSt. und sämtlicher Pflichtabgaben angeben.
- Keine „ab"-Preise, wenn kein Produkt tatsächlich zu diesem Preis verfügbar ist.

**Schritt 2 – Grundpreispflicht prüfen (§ 4 PAngV)**
- Produkt nach Gewicht/Volumen/Länge/Fläche? → Grundpreis pro kg/l/m/m² angeben.
- Ausnahmen: § 9 PAngV (Kleinunternehmen im stationären Handel), Fertigpackungen < 10 g/ml.
- Grundpreis darf nicht kleiner als Gesamtpreis dargestellt werden; gleich auffällige Platzierung.

**Schritt 3 – Versandkosten (§ 6 PAngV)**
- Versandkosten separat ausweisen oder auf Versandkostenfreiheit hinweisen.
- Bei variablen Kosten (nach Lieferort/Gewicht): spätestens vor Kaufabschluss vollständig ausweisen.
- Keine Aufdeckung zusätzlicher Kosten erst im Checkout-Prozess (irreführend nach § 5a UWG).

**Schritt 4 – Streichpreisangabe und 30-Tage-Regel (§ 11 PAngV)**
- Liegt eine Preisermäßigung vor (Streichpreis, „-30 %", „Sale", „Angebot")?
- Ermittlung des Niedrigstpreises der letzten 30 Tage: niedrigster Gesamtpreis (inkl. aller vorherigen Aktionspreise) im 30-Tage-Fenster vor Beginn der aktuellen Preisreduzierung.
- Dieser Niedrigstpreis = einzig zulässiger Referenzpreis für die Streichpreisdarstellung.
- Bei rollierenden Aktionen (Preis sinkt schrittweise): Niedrigstpreis entsprechend aktualisieren.
- Bei neuen Produkten (< 30 Tage am Markt): § 11 PAngV gilt ab ersten Preissenkung; Referenzpreis ist der Einführungspreis.

**Schritt 5 – UWG-Risikobewertung**
- PAngV ist Marktverhaltensregel i.S.d. § 3a UWG; jeder Verstoß ist per se abmahnfähig.
- Abmahner: Mitbewerber (§ 8 Abs. 3 Nr. 1 UWG), Verbände (§ 8 Abs. 3 Nr. 2 UWG), Verbraucherzentralen.
- Streitwerte bei Streichpreisfehlern: regelmäßig 10.000–30.000 EUR.
- Wiederholungsgefahr nach Abmahnung: strafbewehrte Unterlassungserklärung oder gerichtliche Unterlassung.

**Schritt 6 – Dokumentation**
- 30-Tage-Preishistorie für alle Produkte mit Aktionen intern dokumentieren und archivieren (Beweislast im UWG-Prozess beim Händler).

## Ausgabeformat

- **Preisauszeichnungs-Checkliste** (Tabelle): § 3 / § 4 / § 6 / § 11 PAngV × Anforderung × Status × Handlungsbedarf.
- **Streichpreis-Prüfmemo**: Referenzpreisermittlung mit 30-Tage-Analyse, rechtliche Bewertung.
- **Muster-Preisauszeichnung**: Formatbeispiel für Online-Shop (Gesamtpreis + Grundpreis + Versandkostenhinweis + Streichpreis korrekt).

## Beispiel

**Sachverhalt**: Online-Händler H bewirbt Olivenöl (1 l) mit „UVP 12,99 € jetzt 8,99 €". Der niedrigste Preis der letzten 30 Tage vor der Aktion war 9,49 € (kurze Aktionswoche). H gibt als Streichpreis 12,99 € an.

**Gutachtenstil**:

*Gesamtpreis (§ 3 PAngV)*: 8,99 € inkl. MwSt. korrekt angegeben; Gesamtpreispflicht erfüllt.

*Grundpreis (§ 4 PAngV)*: Olivenöl ist ein Lebensmittel nach Volumen; Grundpreis pro Liter = 8,99 €/l muss neben dem Gesamtpreis angegeben werden. Fehlt im Sachverhalt; Verstoß gegen § 4 PAngV.

*Streichpreis (§ 11 PAngV)*: Der Referenzpreis muss der niedrigste Gesamtpreis der letzten 30 Tage vor der Preisreduzierung sein. Der niedrigste Preis war 9,49 € (nicht 12,99 € UVP). Die Angabe „12,99 €" als Streichpreis ist unzulässig; zulässig wäre nur „zuvor 9,49 €" (EuGH, Urt. v. 26.09.2024 – C-330/23 Rn. 55). Die UVP des Herstellers darf daneben genannt werden, ersetzt aber nicht die Pflichtangabe nach § 11 PAngV.

*Rechtsfolge*: Verstoß gegen § 11 PAngV begründet Abmahnrisiko nach § 3a UWG (Sosnitza, in: Ohly/Sosnitza, UWG, 8. Aufl. 2023, PAngV Vorbem. Rn. 18); Bußgeld nach § 19 PAngV bis 25.000 EUR.

## Risiken und typische Fehler

- **UVP als Streichpreis**: UVP des Herstellers ist kein zulässiger Alleinreferenzpreis nach § 11 PAngV; nur zulässig als zusätzliche Information, wenn der 30-Tage-Niedrigstpreis daneben angegeben wird.
- **Rollierend sinkende Preise**: Bei schrittweise absinkenden Preisen (Black-Friday-Countdown) muss der Referenzpreis täglich angepasst werden – der jeweils niedrigste der letzten 30 Tage.
- **Grundpreis vergessen**: Häufig bei Haushalts- und Drogerieprodukten; Fehlen des Grundpreises ist eigenständiger PAngV-Verstoß.
- **Versandkosten im Checkout**: Erst nach Eingabe der Adresse sichtbare Versandkosten verstoßen gegen § 6 PAngV.
- **B2B-Ausnahme zu schnell**: PAngV gilt nur gegenüber Verbrauchern (§ 1 Abs. 1 PAngV); bei gemischtem B2C/B2B-Shop: PAngV-Anforderungen für alle Produkte, die auch Verbrauchern angeboten werden.
- **Dokumentationspflicht unterschätzt**: Im UWG-Abmahnverfahren trägt der Händler die Darlegungs- und Beweislast für die Preishistorie; fehlende interne Preisaufzeichnungen sind prozessual riskant.

## Quellenpflicht

Alle Aussagen sind nach `references/zitierweise.md` zu belegen. Mindestens zwei Rspr.-Belege im BGH-Stil (EuGH C-330/23; BGH GRUR 2023, 162) und zwei Kommentarbelege im Bearbeiter-Stil. Bei Fragen zur PAngV 2022, die noch keine gefestigte höchstrichterliche Rspr. haben, ausdrücklich kennzeichnen und auf Kommentarliteratur und EuGH-Rspr. zu Art. 6a Preisangaben-RL verweisen.
