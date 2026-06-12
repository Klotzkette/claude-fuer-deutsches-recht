---
name: bwa-aufbau-grundlagen
description: "Aufbau der Standard-BWA für Steuerberater erläutern und konfigurieren. Anwendungsfall monatliche oder quartalsweise BWA-Erstellung für GmbH oder Personenunternehmen mit SKR 03 oder SKR 04. Struktur Umsatzerlöse Material Personal sonstige betriebliche Aufwendungen Abschreibungen Zinsergebnis Steu"
---

# Aufbau der Standard-BWA — Grundlagen für Steuerberater

## Fachlicher Anker

- **Normen:** § 6a, § 238 HGB, § 240 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die Betriebswirtschaftliche Auswertung (BWA) ist das zentrale unterjaehrige Steuerungsinstrument. Steuerberater erstellen sie monatlich oder quartalsweise aus der Finanzbuchhaltung. Die Standard-BWA (DATEV-BWA-Form 01) liefert in fuenf Bloecken einen periodengerechten Erfolgsausweis: Umsatzerloese, Material- und Wareneinsatz, Personalkosten, sonstige betriebliche Aufwendungen, Abschreibungen sowie Zinsergebnis und Steuern. Der Skill leitet die Konfiguration und die korrekte Befuellung der Standard-BWA an und stellt sicher, dass die wirtschaftlich relevanten Aussagen sauber ablesbar sind.

## Kaltstart-Rueckfragen

1. Welcher Kontenrahmen liegt vor — SKR 03 oder SKR 04? Welche Standard-BWA-Form (BWA 01 kurz, BWA 01 lang, kumuliert)?
2. Welche Branche und Rechtsform — Industrie, Handel, Dienstleistung, Freiberufler, GmbH, Einzelunternehmen?
3. Welcher Auswertungszeitraum — Monat, Quartal, kumuliert seit Jahresbeginn?
4. Soll ein Vorjahresvergleich, Vormonatsvergleich oder Soll-Ist-Vergleich integriert werden?
5. Welche Periodenabgrenzungen sind vorgesehen — laufende Abgrenzungen (RAP) monatlich, vereinfacht jaehrlich oder gar nicht?
6. Sind die Personalkosten brutto oder mit Arbeitgeberanteilen erfasst? Liegen Daten aus dem Lohnprogramm zeitnah vor?
7. Ist eine kalkulatorische Position vorgesehen (kalkulatorischer Unternehmerlohn, kalkulatorischer Mietzins)?
8. Welche Empfaengerformatierung wuenscht der Mandant — knappe Übersicht, ausfuehrliche BWA, mit Grafiken?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht des Kaufmanns; Grundlage der BWA als unterjaehrige Auswertung der laufenden Buchfuehrung.

**§ 240 HGB** — Inventarpflicht; periodische Bestandsaufnahme fliesst in BWA-Aufwand "Bestandsveraenderung" ein.

**§ 252 HGB** — Allgemeine Bewertungsgrundsaetze (Going-concern, Stichtagsprinzip, Vorsicht); auch unterjaehrig zu beachten.

**§ 5b EStG** — E-Bilanz für Bilanzierer; BWA ist nicht direkt taxonomiepflichtig, soll aber die Brueckenposten zur E-Bilanz abbilden.

**§ 90 AO** — Mitwirkungspflicht des Steuerpflichtigen; betrifft die für die BWA noetige Belegabgabe.

**§ 33 StBerG** — Aufgaben des Steuerberaters; Erstellung der BWA ist Hilfeleistung in Steuersachen i.S.d. § 1 StBerG bzw. vereinbare Taetigkeit § 57 Abs. 3 StBerG.

### Leitentscheidungen und Verwaltungsanweisungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BFH-Rechtsprechung zur periodengerechten Zuordnung von Aufwand und Ertrag: massgeblich sind die allgemeinen Grundsaetze des § 252 HGB und die EStG-Periodenregelungen; konkrete BFH-Aktenzeichen zur Periodenabgrenzung in amtliche/freie Quellen oder lizenzierte Datenbanken unter den Suchbegriffen "Periodenabgrenzung Betriebsausgaben" abrufbar.
- BMF-Schreiben zu GoBD: massgeblich ist das BMF-Schreiben v. 28.11.2019, BStBl I 2019, 1269; etwaige Aktualisierungen über bundesfinanzministerium.de prüfen.
- IDW PS 480 — Grundsaetze für die Erstellung von Jahresabschluessen (analog für hochwertige BWA-Erstellung).

Aktenzeichen und Fundstellen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken gegenpruefen.

## Workflow

### Phase 1 — Datenbasis prüfen

- Vollstaendigkeit der Buchungen prüfen: Bank-Kontoauszuege bis zum Stichtag verbucht, Kassenbuch abgestimmt, OPOS-Listen Debitor und Kreditor aktualisiert.
- Vorlaeufige Sachkontenverteilung im Verrechnungskonto (z. B. SKR 03 Konto 1590/1599 bzw. SKR 04 Konto 1370/1379 — DATEV-Kontenrahmen aktuelle Fassung heranziehen) auf Null stellen oder klar dokumentieren.
- Lohnbuchungen aus dem Lohnprogramm uebernommen? Sozialversicherungs-Beitragsschulden zum Auswertungsstichtag erfasst (Konto SKR 03 1742 bzw. SKR 04 3740 für Verbindlichkeiten SV)?
- Belege chronologisch und vollstaendig verbucht; Cut-off-Datum festlegen (z. B. 5. Werktag des Folgemonats).
- DATEV-Klickpfad zur Prüfung: Rechnungswesen → Stammdaten → Buchungsstapel → Stapelverarbeitung → noch nicht festgeschriebene Buchungen vor BWA festschreiben.

### Phase 2 — Periodenabgrenzungen

- Aktive Rechnungsabgrenzungsposten (Versicherung, Miete, Kfz-Steuer) anteilig auf Monate verteilen.
- Rueckstellungen monatlich anteilig: Urlaubsrueckstellung, Tantiemen, Berufsgenossenschaft.
- Bestandsveraenderung Roh- Hilfs- Betriebsstoffe und unfertige Erzeugnisse — wenigstens quartalsweise schaetzen.
- Abschreibungen monatlich oder jahresanteilig (1/12-Methode) buchen.

### Phase 3 — BWA-Struktur befuellen

Die Standardgliederung in fuenf Bloecken (Kontennummern typische SKR-Bereiche, im Einzelfall mit aktueller DATEV-Kontenrahmenfassung abgleichen):

1. **Umsatzerloese und sonstige betriebliche Ertraege** — Erloesbereich SKR 03 8000-8999 bzw. SKR 04 4000-4999.
2. **Material- und Wareneinsatz** — Wareneingang, Roh-, Hilfs- und Betriebsstoffe, Fremdleistungen (SKR 03 ab 3000 bzw. SKR 04 ab 5000).
3. **Personalkosten** — Loehne und Gehaelter, Sozialversicherungsanteile AG, Berufsgenossenschaft, sonstige Personalnebenkosten (SKR 03 ab 4100 bzw. SKR 04 ab 6000).
4. **Sonstige betriebliche Aufwendungen** — Raumkosten, Betriebsbedarf, Kfz-Kosten, Werbe- und Reisekosten; Abschreibungen werden meist separat als eigene Position ausgewiesen.
5. **Zinsergebnis und Steuern** — Zinsaufwand, Zinsertrag, Gewerbesteuer-Rueckstellungen, Koerperschaftsteuer-Vorauszahlungen.

### Phase 4 — Plausibilisierung

- Umsatzerloese gegen Vorjahres-Monatsumsatz prüfen: Abweichung mehr als 20 Prozent (Daumenregel) inhaltlich klären.
- Materialquote (Materialeinsatz im Verhältnis zum Umsatz): branchentypisch ca. 30-50 Prozent in der Industrie, ca. 60-80 Prozent im Handel, ca. 0-20 Prozent bei Dienstleistung. Konkrete Branchenwerte aus DATEV-BBE-Branchenvergleich abrufen (BBE-Datenstand typischerweise 1-2 Jahre Zeitverzug).
- Personalquote (Personalkosten zu Umsatz): bei Dienstleistung typisch ca. 35-55 Prozent (Branchenrichtwert, Verifikation in BBE Branchenkennzahlen empfohlen).
- Ergebnis vor Steuern auf Konsistenz zur Summen- und Saldenliste prüfen — Endsaldo der Erfolgskonten muss mit BWA uebereinstimmen.

### Phase 5 — BWA-Ausgabe und Erläuterung

- BWA als PDF mit Mandantenkopf und Zeitstempel ausgeben.
- Kurz-Erläuterung unter die BWA setzen (max. 5-7 Saetze): wesentliche Abweichungen, Verfahrensschritte (z.B. Schaetzung Bestand), Hinweis auf offene Punkte.
- Mandantenbezogene Hinweise zu Steuervorauszahlungen und Liquiditaet.

### Phase 6 — Archivierung GoBD-konform

- BWA elektronisch im Mandanten-Ordner gesichert ablegen (revisionssicher, unveraenderbar).
- Aufbewahrungsfrist 10 Jahre nach § 257 HGB / § 147 AO beachten.

## Strategie und Praxis-Tipps

- Auswertungsstichtag spaetestens 30 Tage nach Ablauf des Auswertungsmonats vereinbaren — sonst verliert die BWA Steuerungswirkung.
- BWA monatlich konsistent strukturieren; Wechsel der Auswertungslogik verwirrt den Mandanten und macht Vergleiche unmoeglich.
- Mandant fruehzeitig auf typische Sondereffekte hinweisen (Sonderabschreibung, Investitionsabzugsbetrag § 7g EStG, Sonderzahlungen).
- Honorar nach StBVV § 33 (Buchfuehrung) und § 35 (Lohnbuchfuehrung) abrechnen, Zusatzleistung BWA-Auswertung gesondert.
- Bei wiederholten Buchungsfehlern Mandanten-Belegabgabe disziplinieren — Checkliste an Mandanten verteilen.
- Bei Krisensignalen aus BWA: Querverweis zu stb-bwa-sus-bilanz-pruefung und Hinweispflicht § 102 StaRUG prüfen.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 240, 252, 257.
- EStG § 5b (E-Bilanz).
- AO § 147 (Aufbewahrung).
- BMF-Schreiben zu GoBD (massgeblich: BMF v. 28.11.2019, BStBl I 2019, 1269; etwaige Folgeschreiben über bundesfinanzministerium.de abrufen).
- DATEV Standard-BWA Form 01.
- StBerG §§ 1, 33, 57 Abs. 3.
- Verifikations-Hinweis: Bei Reformen des Kontenrahmens (DATEV-Updates jaehrlich) Aktualisierung der BWA-Konfiguration prüfen. Aktenzeichen vor Mandantenversand in amtliche/freie Quellen oder lizenzierte Datenbanken gegenpruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 5 Marker aufgeloest: 1 bestaetigt (GoBD-Fundstelle BMF 28.11.2019 bestaetigt), 4 ersetzt (Formulierungen ohne Marker neu gefasst) -->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 8 AO (Wohnsitz, Aufenthalt)
- §§ 33, 34 AO (Steuerpflichtiger, gesetzliche Vertreter)
- § 42 AO (Gestaltungsmissbrauch)
- §§ 169-171 AO (Festsetzungsverjährung)
- §§ 233a, 235 AO (Verzinsung, Hinterziehungszinsen)
- § 370 AO (Steuerhinterziehung)
- §§ 153, 371 AO (Berichtigungserklärung, Selbstanzeige)
- §§ 15, 32a EStG (Einkünfte aus Gewerbebetrieb, Tarif)
- § 8 KStG, § 7 GewStG (Einkommen, Gewerbeertrag)
- §§ 1, 15 UStG (Steuerbare Umsätze, Vorsteuerabzug)

### Leitentscheidungen

- BFH I R 36/18 (Hinzurechnungsbesteuerung AStG)
- BFH XI R 11/22 (Reverse-Charge-Verfahren)
- BFH IX R 49/13 (Liebhaberei vs. Einkunftserzielungsabsicht)
- BVerfG 2 BvL 1/03 (Steuerfreistellung Existenzminimum)
- EuGH C-280/10 (Vorsteuerabzug bei wirtschaftlicher Tätigkeit)

### Anwendung im Skill

- Beraterhaftung gegen Mandantenpflicht (§§ 153, 154 AO) klar trennen; Selbstanzeige nach § 371 AO ist eine Strafnorm, kein Steueroptimierungs-Tool.
- Festsetzungsverjaehrung nach §§ 169-171 AO im Zweifel zugunsten des Steuerpflichtigen; Hemmung durch Aussenpruefung beachten.
- Bei Gestaltungsmissbrauch § 42 AO immer alternative Wirtschaftsgruende dokumentieren.
