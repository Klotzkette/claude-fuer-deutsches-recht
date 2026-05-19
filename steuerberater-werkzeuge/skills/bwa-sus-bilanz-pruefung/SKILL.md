---
name: bwa-sus-bilanz-pruefung
description: Prüft BWA (Betriebswirtschaftliche Auswertung), SuSa (Summen- und Saldenliste), Einzelbelege und Bilanzentwürfe einer GmbH/UG auf insolvenzrechtliche Krisensignale. Bewertet, ob bereits eine Überschuldung im Sinne des § 19 InsO oder eine Zahlungsunfähigkeit im Sinne des § 17 InsO vorliegt und ob die Warn- bzw. Hinweispflicht nach § 102 StaRUG ausgelöst ist. Lädt bei Bilanzerstellung, Jahresabschluss, BWA-Review, Krisenfrüherkennung, Fortbestehensprognose, Insolvenzreife-Indizien.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - BWA prüfen
  - Summen- und Saldenliste
  - SuSa Bilanz
  - Überschuldung § 19 InsO
  - Zahlungsunfähigkeit § 17 InsO
  - Fortbestehensprognose
  - § 102 StaRUG
  - Krisenfrüherkennung
  - Bilanzerstellung GmbH
  - Insolvenzreife Hinweispflicht
  - Steuerberater Warnpflicht
---

# BWA-, SuSa- und Bilanzprüfung mit Insolvenzreife-Check (§§ 17, 19 InsO, § 102 StaRUG)

## Zweck

Der Skill begleitet Steuerberater und Geschäftsleitungen kleiner Kapitalgesellschaften (GmbH, UG, GmbH & Co. KG) bei drei verzahnten Aufgaben:

1. **BWA-/SuSa-/Beleg-Plausibilisierung**: Erkennt buchhalterische Auffälligkeiten (Konteninkonsistenz, unübliche Salden, Periodenabgrenzungslücken, nicht aktivierte Posten, fehlerhafte Erlös-/Aufwandszuordnungen).
2. **Bilanzbezogene Krisenprüfung**: Wertet aus, ob bei Erstellung einer Bilanz oder eines Bilanzentwurfs Indizien für eine **Überschuldung (§ 19 Abs. 2 InsO)** oder **Zahlungsunfähigkeit (§ 17 Abs. 2 InsO)** vorliegen, einschließlich Fortbestehensprognose nach § 19 Abs. 2 Satz 1 InsO (12-Monats-Horizont, seit SanInsKG mit Stand 2026 in Geltung gemäß letzter Verlängerung – aktuelle Fassung prüfen).
3. **Warn- und Hinweispflicht nach § 102 StaRUG**: Prüft, ob der Steuerberater (oder ein anderer mit Jahresabschluss befasster Berufsträger) bei Anzeichen einer drohenden Zahlungsunfähigkeit, Zahlungsunfähigkeit oder Überschuldung **hinweisen muss**, und liefert ein dokumentationsfestes Hinweisschreiben.

Anwendungsfälle: Jahresabschlussvorbereitung, unterjährige BWA-Review, Mandantenkrise, ad-hoc Plausibilitätscheck, Vorbereitung Geschäftsführer-Pflichtenkreis (§ 15a InsO, § 15b InsO), Dokumentation der Hinweispflicht zur eigenen Haftungsvermeidung.

## Eingaben

Das Modell benötigt strukturiert oder unstrukturiert:

- **Rechtsform und Größenklasse** (UG/GmbH/AG/KGaA/GmbH & Co. KG; Größenklasse § 267 HGB).
- **BWA** (Standard-BWA, Bewegungs-BWA, kumulierte BWA) für den aktuellen Zeitraum, idealerweise mit Vorjahresvergleich und Plan-/Ist-Abweichung.
- **SuSa** (Summen- und Saldenliste) mit allen Sachkonten, Anfangsbestand, Bewegungen, Saldenwert.
- **Bilanzentwurf** (Aktiva, Passiva, mit Vorjahreswerten); optional Anlagenspiegel, Rückstellungsspiegel, Verbindlichkeitenspiegel (§ 268 Abs. 5 HGB).
- **Liquiditätsdaten**: kurzfristig fällige Verbindlichkeiten (≤ 3 Wochen), verfügbare Zahlungsmittel, zugesagte Kreditlinien.
- **Stille Lasten/Reserven**: Hinweise auf nicht aktivierte Vermögensgegenstände, drohende Verluste, Eventualverbindlichkeiten.
- **Rangrücktritte/Patronatserklärungen**: Texte oder mindestens Kerninhalt (qualifizierter Rangrücktritt im Sinne § 39 Abs. 2 InsO).
- **Belege bei Stichproben**: Eingangs-/Ausgangsrechnungen, Buchungsbelege, Kontoauszüge zu identifizierten Positionen.
- **Auftragsumfang**: Erstellung mit oder ohne umfassende Plausibilitätsbeurteilung? Vereinbarkeit mit der jeweiligen Verlautbarung (z.B. IDW S 7).

## Rechtlicher Rahmen

### Primärnormen

- **§ 17 InsO – Zahlungsunfähigkeit**: Liquiditätslücke ≥ 10 %, die nicht innerhalb von **drei Wochen** geschlossen werden kann (st. Rspr. BGH); Abgrenzung zur Zahlungsstockung.
- **§ 19 InsO – Überschuldung**: Rechnerische Überschuldung (Vermögen deckt Verbindlichkeiten nicht), es sei denn, die Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich (**Fortbestehensprognose**, Zeitraum gemäß SanInsKG/zeitlich abgestuft, seit 09.11.2022 grundsätzlich 12 Monate; aktuelle Fassung prüfen).
- **§ 15a InsO – Insolvenzantragspflicht**: Drei Wochen bei Zahlungsunfähigkeit, sechs Wochen bei Überschuldung.
- **§ 15b InsO – Zahlungsverbote nach Insolvenzreife**.
- **§ 102 StaRUG – Hinweis- und Warnpflicht**: Verpflichtet Personen, die zur unabhängigen Ausübung eines rechts-, steuerberatenden oder wirtschaftsprüfenden Berufs befugt sind und Jahresabschlüsse erstellen, den Mandanten **auf das Vorliegen möglicher Insolvenzantragsgründe** und die sich daraus ergebenden Pflichten der Geschäftsleiter hinzuweisen, wenn entsprechende Anhaltspunkte offenkundig sind und ein Hinweis ohne weiteres erforderlich ist.
- **§ 1 StaRUG – Krisenfrüherkennung**: Pflicht der Geschäftsleitung zur fortlaufenden Überwachung bestandsgefährdender Entwicklungen.
- **§§ 252, 264 Abs. 2, 268 HGB**: Bilanzansatz- und Bewertungsgrundsätze, going concern.
- **§ 252 Abs. 1 Nr. 2 HGB**: Going-concern-Vermutung, soweit dem nicht tatsächliche oder rechtliche Gegebenheiten entgegenstehen.
- **§ 39 Abs. 2 InsO**: Qualifizierter Rangrücktritt – Verbindlichkeiten dahinter werden im Überschuldungsstatus nicht passiviert.

### Leitentscheidungen

1. BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 12–19: Definition der Zahlungsunfähigkeit; Liquiditätslücke ≥ 10 % und Drei-Wochen-Frist; Abgrenzung zur Zahlungsstockung. Bis heute Leitentscheidung für § 17 InsO.

2. BGH, Urt. v. 12.10.2006 – IX ZR 228/03, NJW 2007, 78 Rn. 16–22: Beweisanzeichen für Zahlungsunfähigkeit; Stundungsersuchen, Nichtzahlung gewerblicher Daueraufwendungen, Rücklastschriften.

3. BGH, Urt. v. 19.11.2019 – II ZR 233/18, NJW 2020, 1809 Rn. 17 ff.: Zur Fortbestehensprognose nach § 19 Abs. 2 InsO – tragfähiges Unternehmenskonzept und Finanzplan; Beurteilungsmaßstab überwiegende Wahrscheinlichkeit.

4. BGH, Urt. v. 26.01.2017 – IX ZR 285/14, BGHZ 213, 374 Rn. 26 ff.: Haftung des Steuerberaters bei Erstellung des Jahresabschlusses; Pflicht, auf Indizien einer Insolvenzreife hinzuweisen (Vorläufer der heutigen § 102 StaRUG-Pflicht; weiterhin maßgeblich für Vertragspflichten).

### Kommentarliteratur

1. K. Schmidt/Herchen, in: K. Schmidt, Insolvenzordnung, 20. Aufl. 2023, § 17 InsO Rn. 5–35 und § 19 InsO Rn. 30–90: Systematische Darstellung der Insolvenzgründe; Liquiditätsbilanz nach BGH-Konzept; zweistufige Überschuldungsprüfung mit Fortbestehensprognose; Wirkung qualifizierter Rangrücktritte.

2. Uhlenbruck/Mock, Insolvenzordnung, 16. Aufl. 2024, § 17 InsO Rn. 9–28 und § 19 InsO Rn. 47–95: Detaillierte Darlegung der Liquiditätsbilanz; Behandlung von Passiva-Streckung, Stundungen, Kreditlinien; Berechnung der 10-%-Lücke; Fortbestehensprognose anhand integrierter Planung.

3. Pape/Schaltke, in: Pape/Uhländer, StaRUG, 1. Aufl. 2021, § 102 StaRUG Rn. 8–35: Anwendungsbereich der Hinweispflicht; Adressatenkreis; Anhaltspunkte; Form, Dokumentation und Haftungsfolgen unterlassener Hinweise.

4. Skauradszun, in: BeckOK StaRUG, 8. Ed. (Stand 04.2025), § 102 StaRUG Rn. 10–22: Auslegung des Tatbestandsmerkmals „offenkundig"; Verhältnis zur vertraglichen Hinweispflicht aus BGH NJW 2017, 1611; praktische Anforderungen an die Dokumentation.

5. IDW S 11 (IDW, Beurteilung des Vorliegens von Insolvenzeröffnungsgründen, Stand 22.08.2016 zzgl. Aktualisierungen): Berufsständische Verlautbarung zu Prüfungstiefe, Liquiditätsstatus, Fortbestehensprognose und Dokumentation (kein Kommentar, aber für Berufsausübung maßgeblich; zu zitieren als „IDW S 11, Rn. ...").

## Ablauf

**Schritt 1 – Datenaufnahme und Konsistenzcheck**
- BWA, SuSa und Bilanzentwurf gegeneinander abgleichen (Schlusssalden SuSa = Bilanzposten; BWA-Erlös-/Aufwandskonten = G+V-Posten).
- Periodenabgrenzung prüfen (aktive/passive RAP, Rückstellungen).
- Auffälligkeiten in der SuSa identifizieren: ungewöhnliche Sollsalden auf Erlöskonten, Habensalden auf Aufwandskonten, hohe Verrechnungskonten („1590/1599"), nicht gebuchte Eingangsrechnungen (Erfahrungswert mit Vorjahres-WE-Quote).

**Schritt 2 – Belegstichprobe (risikoorientiert)**
- Bei Auffälligkeiten Stichprobe: Top-10-Eingangsrechnungen, Top-10-Ausgangsrechnungen, alle bargeldnahen Buchungen, Buchungen kurz vor Bilanzstichtag (Cut-off-Test).
- Plausibilität Kassenführung (§ 146 AO, § 158 AO – ordnungsgemäße Buchführung).

**Schritt 3 – Bilanzielle Krisenindikatoren auswerten**
- **Rechnerische Überschuldung**: Eigenkapital negativ? Wert nicht 1:1 maßgeblich – Liquidationswerte/Fortführungswerte sind in einem **Überschuldungsstatus** (gesonderte Aufstellung) zu ermitteln, nicht aus der Handelsbilanz.
- **Stille Lasten**: drohende Verluste aus schwebenden Geschäften, Bürgschaften, Garantien, anhängige Prozesse mit unsicherem Ausgang.
- **Stille Reserven**: nicht bilanzierte Vermögensgegenstände (selbstgeschaffene immaterielle WG, GuV-stille Reserven Sachanlagen).
- **Rangrücktritte**: qualifizierte Rangrücktritte (§ 39 Abs. 2 InsO) → Verbindlichkeit im Überschuldungsstatus passivseitig auszublenden.

**Schritt 4 – Fortbestehensprognose nach § 19 Abs. 2 InsO**
- Zeitraum: aktuell **12 Monate**, ggf. nach SanInsKG verlängert/verkürzt – aktuelle Gesetzesfassung prüfen.
- Grundlage: integrierte Unternehmensplanung (Ertrags-, Bilanz-, Liquiditätsplanung) auf Basis dokumentierter Annahmen.
- Maßstab: **überwiegende Wahrscheinlichkeit** der Fortführungsfähigkeit (BGH NJW 2020, 1809 Rn. 18).
- Ergebnis: positive Prognose → keine Überschuldung trotz rechnerischer Unterdeckung; negative Prognose → § 19 InsO bejaht.

**Schritt 5 – Zahlungsunfähigkeitsprüfung nach § 17 InsO**
- Liquiditätsstatus: fällige Verbindlichkeiten (Stichtagsbezogen) vs. liquide Mittel + binnen 3 Wochen verfügbare Mittel.
- Liquiditätslücke ≥ 10 % und nicht binnen 3 Wochen schließbar = Zahlungsunfähigkeit (BGH BGHZ 163, 134 Rn. 12 ff.).
- Indizienkatalog (BGH NJW 2007, 78 Rn. 18): Stundungsanträge, Mahnungen, Vollstreckungsversuche, Lastschriftrückgaben, eingestellte Zahlungen an Sozialversicherung/Finanzamt.
- Verweis an Schwester-Skill `liquiditaetsvorschau-3wochen` für die rollierende Wochenrechnung.

**Schritt 6 – Hinweispflicht nach § 102 StaRUG bewerten**
- Adressatenkreis: Berufsträger nach § 102 StaRUG mit Erstellungsauftrag Jahresabschluss.
- Tatbestand: **offenkundige Anhaltspunkte** für (drohende) Zahlungsunfähigkeit, Zahlungsunfähigkeit oder Überschuldung.
- Inhalt des Hinweises: (i) konkreter Anhaltspunkt, (ii) Hinweis auf Pflichten der Geschäftsleitung (§§ 15a, 15b InsO, § 1 StaRUG), (iii) Empfehlung Rechtsrat einzuholen.
- Form: schriftlich oder textförmlich, dokumentationsfest, mit Mandantenquittung.
- Rechtsfolge bei unterlassenem Hinweis: zivilrechtliche Haftung gegenüber Mandant und ggf. Insolvenzgläubigern (BGH NJW 2017, 1611 zu Vorgänger-Konstellation; § 102 StaRUG konkretisiert seit 2021).

**Schritt 7 – Dokumentation und Ausgabe**
- Auswertungs-Memo mit Befunden BWA/SuSa/Bilanz.
- Tabellarische Krisenmatrix (siehe Ausgabeformat).
- Vorlage Hinweisschreiben § 102 StaRUG, falls Tatbestand erfüllt.
- Empfehlungen für den Mandanten (Sanierungsberatung, Restrukturierungsbeauftragter, Insolvenzantrag).

## Ausgabeformat

1. **Befund-Tabelle BWA/SuSa** (Spalten: Konto/Bereich – Auffälligkeit – mögliche Ursache – empfohlene Korrektur).
2. **Krisenmatrix** (Spalten: Indikator – Ist-Wert – Schwellenwert/Norm – Bewertung – Rechtsfolge):
   - rechnerische Überschuldung HGB
   - Eigenkapitalquote
   - Liquidität 1. Grades
   - Stundungen/Mahnungen
   - Lieferantenzahlungsverhalten (Tage)
   - Sozialversicherungsabführung
   - Steuerrückstände
   - § 17 InsO (Zahlungsunfähigkeit)
   - § 19 InsO (Überschuldung + Prognose)
   - § 102 StaRUG (Hinweispflicht ausgelöst?)
3. **Gutachtliche Würdigung im Gutachtenstil** (Obersatz – Definition – Subsumtion – Ergebnis) für § 17 InsO, § 19 InsO und § 102 StaRUG.
4. **Hinweisschreiben § 102 StaRUG** (Mustertext mit Platzhaltern) bei positivem Befund.
5. **Empfehlungsteil**: konkrete nächste Schritte mit Frist (Insolvenzantrag binnen 3/6 Wochen § 15a InsO; Beauftragung Sanierungsberater; Erstellung integrierter Planung; StaRUG-Restrukturierungsverfahren prüfen).

## Beispiel

**Sachverhalt**: Steuerberater S erstellt den Jahresabschluss 2025 der „Holzwerk Müller GmbH". Eigenkapital nach Bilanzentwurf: −82.000 EUR. SuSa zeigt Verbindlichkeiten aus Lieferungen und Leistungen 410.000 EUR (Vorjahr 180.000 EUR), durchschnittliches Zahlungsziel von 18 auf 67 Tage gestiegen. Sozialversicherungsbeiträge der letzten drei Monate offen (45.000 EUR). Kontokorrent ausgeschöpft, keine zugesagte Linienerhöhung. Gesellschafterdarlehen 120.000 EUR ohne Rangrücktritt.

**Gutachtenstil**:

*Zahlungsunfähigkeit (§ 17 InsO)*: Fällige Verbindlichkeiten (LuL + SV-Beiträge fällig) ca. 220.000 EUR. Liquide Mittel und binnen 3 Wochen erzielbare Mittel ca. 150.000 EUR (Forderungseingänge laut DA-Liste). Lücke = 70.000 EUR / 220.000 EUR = **31,8 %** > 10 %. Indizien (eingestellte Sozialabgaben, gestrecktes Zahlungsverhalten) sprechen für nicht-vorübergehende Lücke (BGH NJW 2007, 78 Rn. 18). **Zahlungsunfähigkeit liegt vor**.

*Überschuldung (§ 19 InsO)*: Negatives EK lässt rechnerische Unterdeckung vermuten. Stille Reserven Maschinenpark werden geprüft, ein qualifizierter Rangrücktritt für das Gesellschafterdarlehen fehlt (§ 39 Abs. 2 InsO). Fortbestehensprognose: keine integrierte 12-Monats-Planung mit überwiegender Wahrscheinlichkeit darstellbar (BGH NJW 2020, 1809 Rn. 18). **Überschuldung indiziert**, abschließend nach Überschuldungsstatus zu bewerten.

*Hinweispflicht § 102 StaRUG*: S erstellt den Jahresabschluss als steuerberatender Berufsträger; offenkundige Anhaltspunkte (negatives EK + erkennbare Liquiditätskrise + SV-Rückstände) lösen die Hinweispflicht aus (Pape/Schaltke, in: Pape/Uhländer, StaRUG, 1. Aufl. 2021, § 102 StaRUG Rn. 19 ff.). **Hinweispflicht besteht**; schriftlicher Hinweis mit Empfehlung anwaltlicher Beratung und Hinweis auf §§ 15a, 15b InsO ist zu erteilen.

*Empfehlung*: Geschäftsführer hat Antragspflicht (3 Wochen bei § 17 InsO, 6 Wochen bei § 19 InsO, ab Eintritt). Parallel ggf. StaRUG-Restrukturierungsverfahren prüfen, wenn nur **drohende** Zahlungsunfähigkeit (§ 18 InsO) vorläge – hier bereits erfüllt.

## Risiken und typische Fehler

- **Handelsbilanz = Überschuldungsstatus verwechseln**: HGB-Bilanzwerte sind nicht 1:1 maßgeblich; Überschuldungsstatus separat (Fortführungs- oder Liquidationswerte je nach Prognose).
- **Going-concern unbesehen ansetzen**: § 252 Abs. 1 Nr. 2 HGB nur, soweit nichts entgegensteht; bei Krise schriftliche Begründung notwendig.
- **Rangrücktritt unkritisch akzeptieren**: Nur **qualifizierte** Rangrücktritte mit Bezug auf § 39 Abs. 2 InsO und Verzicht auf Geltendmachung im Insolvenzfall haben passivseitige Wirkung.
- **§ 102 StaRUG nicht dokumentiert**: Mündlicher Hinweis genügt rechtlich, ist aber praktisch nicht beweisbar – immer Textform mit Eingangsbestätigung.
- **„Drohende" mit „eingetretener" Zahlungsunfähigkeit verwechseln**: § 18 InsO (24-Monats-Horizont) ≠ § 17 InsO (Stichtag).
- **Drei-Wochen-Frist falsch berechnet**: Ab Eintritt der Insolvenzreife, nicht ab Erkenntnis durch Steuerberater (§ 15a InsO).
- **Indizienkatalog ignoriert**: Stundungen, SV-Rückstände, Lastschriftrückläufer sind keine Bagatellen, sondern starke Indizien (BGH NJW 2007, 78 Rn. 18).
- **SanInsKG-Übergangsregelung übersehen**: Der Prognosezeitraum nach § 19 Abs. 2 InsO wurde temporär verkürzt; aktuelle Fassung jeweils zum Bewertungsstichtag prüfen.

## Quellenpflicht

Alle Aussagen sind nach `references/zitierweise.md` zu belegen. Mindestens zwei Rspr.-Belege im BGH-Stil (BGHZ 163, 134; BGH NJW 2007, 78; BGH NJW 2020, 1809; BGHZ 213, 374) und zwei Kommentarbelege im Bearbeiter-Stil (K. Schmidt/Herchen; Uhlenbruck/Mock; Pape/Schaltke; BeckOK StaRUG/Skauradszun). Berufsständische Verlautbarungen (IDW S 11) sind als solche zu kennzeichnen. Bei laufender Gesetzgebung (SanInsKG-Verlängerungen, StaRUG-Reformen) ist die jeweils aktuell geltende Fassung zu zitieren und auf den Stichtag der Beurteilung zu beziehen.

Siehe ergänzend:
- `references/insolvenzreife-checkliste.md` – tabellarische Indikatorenliste
- `references/hinweisschreiben-102-starug.md` – Mustertext für den Pflichthinweis
