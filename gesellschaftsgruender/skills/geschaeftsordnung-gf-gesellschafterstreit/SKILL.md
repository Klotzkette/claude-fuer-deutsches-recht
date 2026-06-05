---
name: geschaeftsordnung-gf-gesellschafterstreit
description: "Geschaeftsordnung GF Gesellschafterstreit: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Geschaeftsordnung GF Gesellschafterstreit

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Geschaeftsordnung GF Gesellschafterstreit** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-geschaeftsordnung-gf` | Geschäftsordnung für GmbH-Geschäftsführung entwerfen: Ressortzuteilung, Zustimmungsvorbehalte, Berichtspflichten. Normen: §§ 35 37 GmbHG. Prüfraster: Kompetenzbereiche, interne Beschraenkungen, Zustimmungskataloge. Output: Geschäftsordnungs-Entwurf GF. Abgrenzung: nicht Gesellschaftsvertrag oder Beiratssatzung. |
| `gesellschaftsgruender-gesellschafterstreit-eilantraege` | Eilmassnahmen im Gesellschafterstreit der GmbH: einstweilige Verfuegung gegen Mitgesellschafter oder Geschäftsführer. Normen: §§ 935 940 ZPO, §§ 37 38 GmbHG. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Arrest vs. einstweilige Verfuegung. Output: Antragsschriftsatz einstweilige Verfuegung GmbH. Abgrenzung: nicht ordentliche Anfechtungsklage gegen Beschluss. |
| `gesellschaftsgruender-gesellschaftervereinbarung` | Gesellschaftervereinbarung (SHA) neben dem Gesellschaftsvertrag entwerfen: Vorkaufsrechte, Drag-Along, Tag-Along. Normen: §§ 705 ff. BGB, GmbHG. Prüfraster: schuldrechtliche Bindung, Satzungsrang, Durchsetzbarkeit, Vertragsstrafe. Output: SHA-Entwurf mit Kernklauseln. Abgrenzung: nicht Gesellschaftsvertrag (nur notariell). |
| `gesellschaftsgruender-gf-meeting-templates` | Vorlagen für Geschäftsführersitzungen und Protokolle erstellen: Tagesordnung, Beschlussprotokoll, Aktionsliste. Normen: §§ 35 ff. GmbHG. Prüfraster: Beschlussfähigkeit, Umlaufverfahren, Dokumentationspflichten. Output: Meeting-Templates für GF-Sitzungen. Abgrenzung: nicht Gesellschafterversammlungs-Protokoll. |
| `gesellschaftsgruender-ggmbh-gemeinnuetzigkeit` | Prüft gGmbH-Gründung, Satzungszweck, Mittelbindung und Finanzamt-Abstimmung. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Geschaeftsordnung GF Gesellschafterstreit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-geschaeftsordnung-gf`

**Fokus:** Geschäftsordnung für GmbH-Geschäftsführung entwerfen: Ressortzuteilung, Zustimmungsvorbehalte, Berichtspflichten. Normen: §§ 35 37 GmbHG. Prüfraster: Kompetenzbereiche, interne Beschraenkungen, Zustimmungskataloge. Output: Geschäftsordnungs-Entwurf GF. Abgrenzung: nicht Gesellschaftsvertrag oder Beiratssatzung.

# Geschäftsordnung Geschäftsführung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Geschäftsordnung Geschäftsführung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere vor Erstellung der Geschaeftsordnung:

1. **Anzahl Geschaeftsfuehrer?** Solo-GF: vereinfachte Version ausreichend; Multi-GF: Ressort-Verteilung und Patt-Mechanismus zwingend.
2. **Investor-Beteiligung?** SHA-Berichtspflichten und Zustimmungskataloge aus dem SHA in Geschaeftsordnung spiegeln.
3. **Beirat vorhanden?** Beirats-Zustimmungsvorbehalte mit GF-Katalog koordinieren.
4. **Erlassende Stelle?** Gesellschafterversammlung (empfohlen, § 46 Nr. 6 GmbHG) oder Geschaeftsfuehrer selbst? Aenderbarkeit unterscheidet sich.
5. **Schwellenwerte?** Fuer Zustimmungspflichtige Geschaefte: am Umsatz und Bilanzsumme orientieren; zu hohe Schwellen sind wirkungslos.

## Zentrale Normen

- **§ 37 I GmbHG** — GF ist an Gesetz, Satzung und Gesellschafterbeschluesse gebunden
- **§ 37 II GmbHG** — Bei Mehrgliedrigkeit: Gesamtgeschaeftsfuehrung als Grundsatz; Satzung / Geschaeftsordnung kann abweichen
- **§ 46 Nr. 6 GmbHG** — Zustaendigkeit der Gesellschafterversammlung fuer Geschaeftsordnung der GF (Erlass und Aenderung)
- **§ 43 GmbHG** — Sorgfaltspflicht des GF; verletzt er Zustimmungsvorbehalt: Haftung
- **§ 49 I GmbHG** — Einberufungspflicht GF bei gesellschafterwichtigem Anlass (Eskalationspflicht)
- **§§ 133, 157 BGB** — Auslegung der Zustimmungspflichten bei Streit

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Geschaeftsordnung-Qualitaet

| Schritt | Pruefpunkt | Norm | Ergebnis |
|---|---|---|---|
| 1 | Zustimmungskataloge am Umsatz/Bilanz orientiert? | § 37 GmbHG | Schwellen praxistauglich? |
| 2 | Patt-Mechanismus bei Multi-GF? | § 37 II GmbHG | Eskalation zur GV noetig |
| 3 | SHA-Berichtspflichten gespiegelt? | SHA | Investor-Infos rechtzeitig |
| 4 | Beirats-Zustimmungsvorbehalte koordiniert? | § 52 GmbHG | Doppel-Genehmigungen vermeiden |
| 5 | Erlass durch GV oder GF selbst? | § 46 Nr. 6 GmbHG | Aenderbarkeit festlegen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Schritt-fuer-Schritt-Workflow

1. **Ressort-Bedarf erfassen:** Wie viele GF, welche Ressorts, welche Zustimmungspunkte?
2. **SHA und Satzung lesen:** Bereits vorhandene Zustimmungs-Kataloge identifizieren; nicht doppeln.
3. **Schwellenwerte festlegen:** Am Jahresumsatz und geplanten Investitionen orientieren.
4. **Patt-Mechanismus:** Bei 2+ GF: Eskalationsregel formulieren.
5. **Meeting-Rhythmus:** Woechentlich, quartalsweise Investor-Meeting, jaehrliche Strategie.
6. **Beschluss der Gesellschafterversammlung:** Erlass der Geschaeftsordnung beschliessen (Paragraf 46 Nr. 6 GmbHG); Protokoll erstellen.
7. **Gelebte Praxis:** Jedes Quartal evaluieren; Schwellenwerte anpassen.
8. **Bei Aenderung:** Erneuter GV-Beschluss; alten Stand archivieren.

## Output-Template: Geschaeftsordnung GF

**Adressat:** Internes Fuehrungs-Dokument — Tonfall praezise-sachlich

```
GESCHAEFTSORDNUNG fuer die Geschaeftsfuehrung
der [FIRMA] GmbH
Stand: [DATUM] | Erlass: Gesellschafterversammlungs-Beschluss vom [DATUM]

§ 1 Geltungsbereich
Diese Geschaeftsordnung regelt die innere Organisation
der Geschaeftsfuehrung der Gesellschaft.

§ 2 Ressort-Verteilung (bei mehreren GF)
[GF-NAME A] (CEO): Strategie, Vertrieb, Business Development
[GF-NAME B] (CTO): Produkt, Technik, IT, Datenschutz
[GF-NAME C] (CFO): Finanzen, Controlling, HR, Recht

§ 3 Zustimmungspflichtige Geschaefte
(a) Zustimmung aller GF erforderlich:
 - Investitionen > [BETRAG] EUR
 - Personalentscheidungen: Gehalt > [BETRAG] EUR p.a.
 - Vertraege mit Laufzeit > [N] Jahre
 - Kreditaufnahme > [BETRAG] EUR

(b) Zustimmung der Gesellschafterversammlung erforderlich:
 - Investitionen > [BETRAG] EUR
 - Veraeusserung wesentlicher Aktiva (> 20 % Bilanz)
 - Beteiligungen an anderen Gesellschaften
 - Kreditaufnahme > [BETRAG] EUR

§ 4 Meeting-Rhythmus
(1) GF-Meeting: woechentlich [WOCHENTAG] [UHRZEIT]
(2) Investor-Reporting: quartalsweise (SHA-Annex)
(3) Jahres-Strategiemeeting: [MONAT]

§ 5 Berichtspflichten an GV
Quartalsbericht binnen 4 Wochen nach Quartalsende:
- Umsatz, EBITDA, Liquiditaet
- Wesentliche Risiken
- Personalveraenderungen

§ 6 Patt-Mechanismus
Bei Uneinigkeit der GF in Zustaendigkeitsfragen:
(1) Versuche bilateraler Einigung (48 Stunden)
(2) Eskalation an Gesellschafterversammlung
(3) GV entscheidet mit einfacher Mehrheit

§ 7 AEnderungen
AEnderungen dieser Geschaeftsordnung beduerfen eines
Beschlusses der Gesellschafterversammlung mit einfacher
Mehrheit (§ 46 Nr. 6 GmbHG).
```

## Rote Schwellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Patt ohne Mechanismus bei 2 GF: Gesellschaft handlungsunfaehig; GV-Einberufung nach § 49 GmbHG
- Keine Eskalationsregel: GF koennen wichtige Entscheidungen blocken -> teure Streitigkeiten
- Zu hohe Schwellen: Geschaeftsordnung faktisch leer; Kontrollzweck nicht erfullt

## Quellen und Vertiefung

- §§ 37, 43, 46 Nr. 6, 49 GmbHG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-gf-meeting-templates` — Tagesordnungen, Protokoll-Vorlagen
- `gesellschaftsgruender-geschaeftsfuehrervertrag` — Anstellungsvertrag; Ressortbezug
- `gesellschaftsgruender-gv-einladung-tagesordnung` — Gesellschafterversammlung
- `gesellschaftsgruender-beirat-advisory-board` — Koordination mit Beiratsbefugnissen

## 2. `gesellschaftsgruender-gesellschafterstreit-eilantraege`

**Fokus:** Eilmassnahmen im Gesellschafterstreit der GmbH: einstweilige Verfuegung gegen Mitgesellschafter oder Geschäftsführer. Normen: §§ 935 940 ZPO, §§ 37 38 GmbHG. Prüfraster: Verfuegungsanspruch, Verfuegungsgrund, Arrest vs. einstweilige Verfuegung. Output: Antragsschriftsatz einstweilige Verfuegung GmbH. Abgrenzung: nicht ordentliche Anfechtungsklage gegen Beschluss.

# Gesellschafterstreit — Eilanträge

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafterstreit — Eilanträge` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Gesellschafterstreitigkeiten eskalieren häufig an präzise definierten Ereignissen: ein Beschluss wird mit einfacher Mehrheit gefasst, der die Minderheit materiell schädigt (Kapitalerhöhung mit Bezugsrechtsausschluss, Abberufung des Gesellschafter-GF, Verwässerung durch Down-Round). Sobald ein solcher Beschluss ins Handelsregister eingetragen ist, ist die Rechtslage oft faktisch irreversibel. Der Eilrechtsschutz — einstweilige Verfügung beim Landgericht und Anmeldungs-Sperre beim Registergericht — ist daher in vielen Fällen der entscheidende Hebel. Er muss innerhalb von Stunden bis wenigen Tagen nach dem streitigen Ereignis eingeleitet werden.

Dieser Skill behandelt das vollständige Eilrechtsschutz-Werkzeugset für GmbH-Gesellschafterstreitigkeiten: Verfügungsantrag, Anmeldungs-Sperre, Anfechtungsklage, Streit-Eskalationspfad und präventive Klauseln.

## Kaltstart-Rückfragen

1. **Was ist passiert?** Welcher Beschluss wurde gefasst (Kapitalerhöhung, Abberufung GF, Satzungsänderung, Auflösung)?
2. **Datum des Beschlusses?** Anfechtungsfrist: 1 Monat ab Beschlussfassung (BGH-Linie analog § 246 AktG).
3. **Wurde Anmeldung beim Handelsregister bereits eingereicht?** Bei Ja: Anmeldungs-Sperre zeitkritisch (Tage bis Eintragung).
4. **Anteilsverhältnisse:** Wer hat welchen Anteil? Mehrheits- und Minderheitsgesellschafter?
5. **Stimmergebnis:** Wie wurde abgestimmt? Gab es Stimmverbote (§ 47 Abs. 4 GmbHG)?
6. **Vorhandene Klauseln:** Gibt es Schiedsklausel (DIS), Schlichtungspflicht vor Klage, Beirat?
7. **Wirtschaftlicher Schaden:** Wie hoch ist der drohende Schaden durch die angefochtene Maßnahme (für Streitwert und Glaubhaftmachung der Eilbedürftigkeit)?
8. **Versammlungsleiter-Problem:** Gibt es Streit über die Leitung der Gesellschafterversammlung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte mit Auszügen

**§§ 935 ff. ZPO — Einstweilige Verfügung**
> § 935 ZPO: Einstweilige Verfügungen sind auch zum Zwecke der Regelung eines einstweiligen Zustandes in Bezug auf ein streitiges Rechtsverhältnis zulässig, sofern diese Regelung nötig erscheint, insbesondere bei dauernden Rechtsverhältnissen, um wesentliche Nachteile abzuwenden.

Voraussetzungen: Verfügungsanspruch (der materiell-rechtliche Anspruch, der gesichert werden soll) + Verfügungsgrund (Eilbedürftigkeit; Rechtsverlust oder wesentliche Nachteile wenn keine sofortige Regelung). Glaubhaftmachung durch Urkunden und eidesstattliche Versicherung (§ 920 ZPO).

**§ 16 Abs. 2 HGB — Registersperre analog**
> § 16 Abs. 2 HGB ermöglicht dem Registergericht, die Eintragung eines Beschlusses auszusetzen, wenn die Anfechtbarkeit oder Nichtigkeit glaubhaft gemacht wird.

In der Praxis wird die Registersperre durch Antrag beim zuständigen Amtsgericht (Handelsregistergericht) nach §§ 374 ff. FamFG beantragt. Das Registergericht kann die Eintragung aussetzen, bis über die Anfechtung entschieden ist.

**§§ 374 ff. FamFG — Registersachen**
> FamFG §§ 374 ff. regeln das Verfahren in Registersachen (Handelsregister). Antragsverfahren; amtswegige Prüfung durch das Gericht; keine strenge Parteidisposition wie im Zivilprozess.

**§§ 241, 243, 246 AktG analog GmbH**
> § 241 AktG (Nichtigkeitsgründe): Gesetzlich abschließend geregelte Fälle der Nichtigkeit (z.B. fehlende notarielle Form, Verstoß gegen Gläubigerschutz).
> § 243 AktG (Anfechtbarkeit): Beschluss anfechtbar bei Verstoß gegen Gesetz oder Satzung.
> § 246 Abs. 1 AktG (Anfechtungsfrist): 1 Monat ab Beschlussfassung.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§ 47 Abs. 4 GmbHG — Stimmverbot**
> "Ein Gesellschafter, welcher durch die Beschlußfassung entlastet oder von einer Verbindlichkeit befreit werden soll, hat hierbei kein Stimmrecht und darf ein solches auch nicht für andere ausüben."

Verstoß gegen Stimmverbot: Beschluss anfechtbar; ggf. kausal, wenn stimmbefangene Stimme das Ergebnis beeinflusst hat.

**§ 55 Abs. 4 GmbHG — Bezugsrecht bei Kapitalerhöhung**
> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§ 894 ZPO — Klage auf Abgabe einer Willenserklärung**
> Bei rechtskräftiger Verurteilung zur Abgabe einer Willenserklärung (z.B. Stimmabgabe) gilt die Erklärung als mit Rechtskraft des Urteils abgegeben. Im Eilverfahren kann das Gericht anordnen, dass der Gesellschafter eine bestimmte Stimme abgibt.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Eilrechtsschutz bei Gesellschafterstreit


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Beschluss analysieren | Welcher Beschluss? Kapitalerhöhung, Abberufung, Satzungsänderung, Auflösung? | Bestimmung des Angriffsmittels (Anfechtung vs. Nichtigkeit) |
| 2 | Nichtigkeit oder Anfechtbarkeit? | § 241 AktG analog: Nichtigkeitsgründe (fehlende Form, Gläubigerschutz)? oder § 243 AktG analog: Anfechtbarkeit (Gesetzes-/Satzungsverstoß)? | Nichtigkeit: keine Frist; Anfechtbarkeit: 1 Monat (§ 246 AktG analog) |
| 3 | Anfechtungsfrist prüfen | Datum des Beschlusses + 1 Monat? | Fristversäumnis = Beschluss wird endgültig wirksam (außer bei Nichtigkeit) |
| 4 | Handelsregister-Status | Ist Anmeldung beim HR bereits eingereicht? Noch nicht? Eintragung drohend? | Bei drohendem Eintrag: Anmeldungs-Sperre zeitkritisch (Priorität: Tage) |
| 5 | Stimmverbot geprüft? | § 47 Abs. 4 GmbHG: Hat stimmbefangenes Mitglied abgestimmt? War die Stimme kausal für das Ergebnis? | Kausalitätsprüfung: Ohne stimmbefangene Stimme — hätte das Ergebnis anders gelautet? |
| 6 | Bezugsrechtsausschluss gerechtfertigt? | Bei KE mit Bezugsrechtsausschluss: Sachliche Rechtfertigung (BGH Kali+Salz)? Verhältnismäßigkeit? Nicht diskriminierend? | Fehlt Rechtfertigung: Anfechtbarkeit; ggf. Unterlassungsklage |
| 7 | Verfügungsanspruch formulieren | Was genau wird beantragt (Unterlassung, Stimmabgabe, Unterlassung der Anmeldung)? | Präziser Antrag ist Grundvoraussetzung für einstweilige Verfügung |
| 8 | Verfügungsgrund glaubhaft machen | Eilbedürftigkeit: Würde Eintragung einen unwiderruflichen Schaden verursachen? Quantifizierung des drohenden Schadens? | Eidesstattliche Versicherung + Protokoll + Gutachten |
| 9 | Schiedsklausel prüfen | Enthält der Gesellschaftsvertrag eine DIS-Schiedsklausel? | Bei Schiedsklausel: Eilrechtsschutz beim staatlichen Gericht trotzdem möglich (vorläufige Maßnahmen nicht ausgeschlossen); aber: Hauptsache zum Schiedsgericht |
| 10 | Schlichtungspflicht prüfen | Gibt es eine Schlichtungspflicht vor Klage (Beirat)? Ausnahme bei Eilbedürftigkeit? | Eilanträge von Schlichtungspflicht regelmäßig ausgenommen |
| 11 | Anfechtungsklage einreichen | Fristwahrung: Klage beim LG des Gesellschaftssitzes binnen 1 Monat ab Beschluss | Parallel zu Eilverfahren; Hauptverfahren läuft unabhängig |
| 12 | Hauptverfahren | LG entscheidet über Anfechtbarkeit; typische Dauer: 6–18 Monate LG; ggf. OLG; BGH selten | Rechtskraft der Anfechtung beseitigt den Beschluss ex tunc |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Beschluss anfechtbar (§ 243 AktG analog) | Kläger (Gesellschafter) | Nachweis des Gesetzes-/Satzungsverstoßes; Kausalität für Beschlussergebnis |
| Beschluss nichtig (§ 241 AktG analog) | Kläger oder von Amts wegen | Nichtigkeitsgründe können jederzeit geltend gemacht werden |
| Sachliche Rechtfertigung des Bezugsrechtsausschlusses | Gesellschaft / Mehrheitsgesellschafter | Mehrheitsgesellschafter muss sachliche Gründe darlegen (BGH Kali+Salz) |
| Stimmverbot nicht verletzt (§ 47 Abs. 4 GmbHG) | Gesellschaft / Versammlungsleiter | Nachweis durch Protokoll (kein stimmbefangener Gesellschafter hat abgestimmt) |
| Verfügungsanspruch und Verfügungsgrund (§ 920 ZPO) | Antragsteller (Glaubhaftmachung ausreichend) | Glaubhaftmachung durch Urkunden und eidesstattliche Versicherung |
| Ordnungsgemäße Versammlungsleitung | Versammlungsleiter | Nachweis durch Protokoll; bei Streit über Leitungskompetenz: Mehrheitsbeschluss |

## Fristen und Verjährung

| Frist | Norm | Inhalt | Folge bei Versäumnis |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Einstweilige Verfügung — Dringlichkeit | § 935 ZPO (Selbstverwirkung) | Zu lange Wartezeit nach Beschluss weckt Zweifel an Eilbedürftigkeit (typisch: > 4–6 Wochen = Dringlichkeit problematisch) | Verfügungsantrag kann wegen fehlender Eilbedürftigkeit zurückgewiesen werden |
| Anmeldungs-Sperre | § 16 HGB; §§ 374 ff. FamFG | Unverzüglich nach Kenntnis der Anmeldungsabsicht | Nach Eintragung: Registersperre wirkungslos |
| Widerspruch gegen Registersperre | FamFG | 1 Monat ab Beschluss des Registergerichts (§ 22 FamFG) | Beschluss des Registergerichts wird bestandskräftig |
| Verjährung Schadensersatz aus Beschlussmangel | §§ 195, 199 BGB | 3 Jahre ab Kenntnis | Schadensersatzanspruch verjährt; Anfechtungsklage unabhängig |
| Schiedsverfahren — Eilmaßnahmen DIS | DIS-Schiedsordnung 2021, Art. 29 | Notschiedsverfahren: kurzfristig | Eilschutz über DIS möglich, aber ungewohnt; staatliches Gericht schneller |

## Typische Gegenargumente

| Einwand | Begründung Gegenseite | Erwiderung |
|---|---|---|
| Bezugsrechtsausschluss sachlich gerechtfertigt | Strategischer Investor bringt Mehrwert (Technologie, Netzwerk) | Sachliche Rechtfertigung muss substantiiert dargelegt werden; pauschale Aussagen reichen nicht (BGH Kali+Salz); Verhältnismäßigkeit prüfen: Warum kein Bezugsrecht mit gleichem Ausgabepreis? |
| Kein Verfügungsgrund, weil Hauptsache schnell entschieden | LG entscheidet zügig | Eintragung ins HR ist nicht rückgängig zu machen; unwiderrufliche Verwässerung ist irreversibler Schaden |
| Schiedsklausel schließt staatlichen Eilrechtsschutz aus | Schiedsklausel erfasst alle Streitigkeiten | Vorläufige Maßnahmen vor staatlichen Gerichten bleiben trotz Schiedsklausel zulässig (§ 1041 ZPO); Eilantrag ist kein Einwand gegen Schiedsklausel |
| Anfechtungsfrist abgelaufen | Beschluss vom Monat zurück | Prüfen, ob Nichtigkeitsgründe (§ 241 AktG analog) vorliegen — keine Frist; oder ob Frist wegen versteckten Beschlussmangels neu läuft |
| Stimmverbot-Verstoß war nicht kausal | Mehrheit hätte auch ohne stimmbefangene Stimme bestanden | Kausalitätsprüfung: Stimmergebnis ohne stimmbefangene Stimme neu berechnen; bei Ja: keine Kausalität |
| Versammlungsleiter war legitimiert | Mehrheitsbeschluss zur Wahl des Versammlungsleiters | Wenn kein wirksamer Mehrheitsbeschluss vor GV-Leiterwahl: Versammlungsleiter ohne Legitimation; Beschlüsse anfechtbar |

## Typische Streit-Konstellationen

| Konstellation | Eilmittel | Priorität |
|---|---|---|
| Kapitalerhöhung mit Bezugsrechtsausschluss vor Eintragung | eV beim LG + Anmeldungs-Sperre beim Registergericht | Innerhalb 48–72 Stunden |
| GF-Abberufung soll sofort vollzogen werden | eV auf Unterlassung der Eintragung + eV auf Unterlassung der Abberufungswirkungen | Sofort; Abberufung wirkt ab Beschluss |
| Versammlungsleiter umstritten | Neutralen Notar beauftragen; ggf. eV auf Besetzung | Vor Beginn der GV |
| Streit über Beschlussfähigkeit / fehlendes Quorum | Protokoll anfechten; Feststellungsklage | Bis 1 Monat nach Beschluss |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| StaRUG-Plan gegen Golden-Share-Veto | Golden Share greift nicht bei gesetzlicher Insolvenzantragspflicht; Klärung im StaRUG-Verfahren | Sofort bei StaRUG-Antrag |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Eilantrag im Gesellschafterstreit beantragen | Einstweilige Verfuegung nach Pruefschema; Template unten |
| Variante A — Gesellschafterstreit durch Mediator loesbar | Mediation oder Schiedsverfahren zuerst; Eilantrag nur bei Dringlichkeit |
| Variante B — Mehrheitsbeschluss wirksam aber schadlich | Anfechtungsklage statt Eilantrag; Eilantrag nur bei unmittelbarem Schaden |
| Variante C — GmbH droht Insolvenz durch Streit | Insolvenzrecht pruefen; parallele Handlungsoptionen koordinieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Antrag auf einstweilige Verfügung (Kapitalerhöhung mit Bezugsrechtsausschluss)

```
An das
Landgericht [Ort] — Kammer für Handelssachen
[Anschrift]

[Ort, Datum]

Antrag auf Erlass einer einstweiligen Verfügung
im einstweiligen Rechtsschutz

Antragsteller:
[Name des Minderheitsgesellschafters], [Anschrift]
— Verfügungskläger —
vertreten durch: [Kanzlei, Name]

Antragsgegnerin:
[Gesellschaft] GmbH, [Sitz, HRB]
vertreten durch Geschäftsführer [Name]
— Verfügungsbeklagte —

wird beantragt:

I. Der Verfügungsbeklagten wird es bei Meidung eines für jeden Fall der Zuwiderhandlung
festzusetzenden Ordnungsgeldes bis zu 250.000 EUR (ersatzweise Ordnungshaft) untersagt,
die Anmeldung der mit Beschluss der Gesellschafterversammlung vom [Datum] (TOP [N])
beschlossenen Kapitalerhöhung um [X] EUR mit Bezugsrechtsausschluss zugunsten der
[Investor GmbH] beim Handelsregister einzureichen oder dort eintragen zu lassen.

II. Hilfsweise: Das Registergericht [Ort] wird ersucht, die Eintragung der vorstehend
bezeichneten Kapitalerhöhung bis zur rechtskräftigen Entscheidung in der Hauptsache
auszusetzen.

Begründung:

A. Verfügungsanspruch

1. Der Beschluss der Gesellschafterversammlung vom [Datum] leidet an wesentlichen
Mängeln und ist auf Antrag des Verfügungsklägers für nichtig zu erklären (Anfechtungs-
klage ist beigefügt als Anlage K 1 / wird gleichzeitig eingereicht).

2. Der Bezugsrechtsausschluss zugunsten der [Investor GmbH] ist sachlich nicht
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
liegendes, sachliches Ziel gerechtfertigt sein und der Verhältnismäßigkeit entsprechen.
Die pauschale Behauptung eines "strategischen Mehrwerts" genügt diesen Anforderungen
nicht.

3. Der Antragsteller hält [X] % der Geschäftsanteile. Durch die Kapitalerhöhung würde
seine Beteiligung auf [X - Δ] % verwässert. Der wirtschaftliche Schaden beläuft sich
auf mindestens [EUR-Betrag] (vgl. Bewertungsgutachten Anlage K 2).

B. Verfügungsgrund (Eilbedürftigkeit)

4. Die [Gesellschaft] GmbH hat die Kapitalerhöhung bereits beim Handelsregister
angemeldet (Anlage K 3: Anmeldungsurkunde vom [Datum]). Die Eintragung ist für
die nächsten Tage zu erwarten.

5. Mit der Eintragung wäre die Verwässerung des Antragstellers unwiderruflich vollzogen.
Eine Rückabwicklung wäre nur unter erheblichen praktischen und rechtlichen
Schwierigkeiten möglich.

6. Die Eilbedürftigkeit ergibt sich aus der drohenden Eintragung. Der Antragsteller
hat unverzüglich nach Kenntnis der Anmeldung (am [Datum]) diesen Antrag gestellt.

Glaubhaftmachung:
- Anlage K 1: Protokoll der GV vom [Datum]
- Anlage K 2: Bewertungsgutachten [Sachverständiger] vom [Datum]
- Anlage K 3: Handelsregisteranmeldung vom [Datum] (Kopie)
- Anlage K 4: Eidesstattliche Versicherung des Antragstellers

[Ort, Datum]
[Kanzlei / Rechtsanwalt/-anwältin]
```

### Baustein 2: Antrag auf Anmeldungs-Sperre beim Registergericht

```
An das
Amtsgericht [Ort] — Registergericht
HRB [Nummer]

[Ort, Datum]

Antrag auf Aussetzung der Eintragung
nach §§ 374 ff. FamFG i.V.m. § 16 Abs. 2 HGB analog

Antragsteller: [Name], [Anschrift]
Beteiligte: [Gesellschaft] GmbH, [Sitz], HRB [Nummer]

Das Registergericht wird gebeten,

die Eintragung der Kapitalerhöhung der [Gesellschaft] GmbH gemäß Anmeldung des
Notars Dr. [Name] vom [Datum] (Urkundsrollen-Nr. [Nummer]) bis zur rechtskräftigen
Entscheidung über die beim Landgericht [Ort] (Az. [Nummer]) erhobene Anfechtungsklage
auszusetzen.

Begründung:

Der Beschluss der Gesellschafterversammlung vom [Datum] ist anfechtbar, weil:
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Das Stimmverbot nach § 47 Abs. 4 GmbHG nicht beachtet wurde (Gesellschafter
 [Name] hat trotz Stimmverbots abgestimmt; Protokoll-Anlage A).

Die Anfechtungsklage ist beim LG [Ort] erhoben worden (Anlage B: Klageschrift).

Die Eintragung würde die Verwässerung des Antragstellers unwiderruflich machen.

Glaubhaftmachung:
- Anlage A: Protokoll der GV vom [Datum]
- Anlage B: Anfechtungsklage LG [Ort]
- Anlage C: Eidesstattliche Versicherung

[Ort, Datum]
[Kanzlei / Name]
```

### Baustein 3: Anfechtungsklage (vollständige Klage)

```
An das
Landgericht [Ort] — Kammer für Handelssachen

[Ort, Datum]

Klage

Kläger:
[Name], [Anschrift]
— Kläger —
vertreten durch: [Kanzlei, Name]

Beklagte:
[Gesellschaft] GmbH, [Sitz, HRB]
— Beklagte —

Klagantrag:

Es wird beantragt, festzustellen, dass der von der Gesellschafterversammlung der
Beklagten am [Datum] unter TOP [N] gefasste Beschluss über die Kapitalerhöhung um
[X] EUR mit Bezugsrechtsausschluss zugunsten der [Investor GmbH]

 n i c h t i g ist,

hilfsweise:

der Beschluss wird aufgehoben (Anfechtung).

Streitwert: [Y] EUR (entspricht dem wirtschaftlichen Interesse des Klägers an der
Aufhebung des Beschlusses, beziffert durch den Verwässerungsschaden von [EUR]).

Begründung:

I. Sachverhalt
[Beschreibung der GV, Beschluss, Anteilsverhältnisse]

II. Anfechtungsgrund
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Stimmverbot verletzt (§ 47 Abs. 4 GmbHG)
3. Verwässerungsschaden quantifiziert (Gutachten Anlage K 2)

III. Rechtsfolge
Der Beschluss ist gemäß §§ 241, 243 AktG analog nichtig / anfechtbar.
Frist: Monatsfrist nach § 246 AktG analog gewahrt (Beschluss: [Datum];
Klageerhebung: [Datum = heute]).

Beweismittel:
- Gesellschaftsvertrag (Anlage K 1)
- Protokoll der GV (Anlage K 2)
- Bewertungsgutachten (Anlage K 3)

[Kanzlei / Name]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Streitwert und Kosten

| Streitgegenstand | Streitwertansatz | Kosten (Richtwert) |
|---|---|---|
| Anfechtungsklage GmbH-Beschluss | Wirtschaftliches Interesse des Klägers; bei KE: Verwässerungsschaden | Bei 500.000 EUR: RA-Gebühren 3 × 3.459 EUR = ca. 10.400 EUR; Gericht ca. 5.200 EUR |
| Einstweilige Verfügung | Regelmäßig 1/3 bis 1/2 des Hauptsachestreitwerts | Bei 100.000 EUR: RA-Kosten ca. 1.700 EUR; Gericht ca. 850 EUR |
| Anmeldungs-Sperre Registergericht | Geringer; FamFG-Verfahren | Kostenfestsetzung nach FamFG; oft < 500 EUR |
| Schiedsverfahren DIS | Streitwertabhängig; DIS-Gebührenordnung | Bei 1 Mio. EUR: DIS-Verwaltungsgebühr ca. 15.000 EUR; Schiedsrichtergebühren additional |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Kapitalerhöhung mit Bezugsrechtsausschluss angekündigt | Sofort anwaltliche Prüfung der sachlichen Rechtfertigung; parallele Einreichung von Verfügungsantrag + Anmeldungs-Sperre |
| Gesellschafterstreit absehbar | Präventiv: Schiedsklausel (vertraulich), Schlichtungspflicht vor Klage, Beirat als Schlichter; Stimmverbots-Klauseln scharf definieren |
| GF-Abberufung überraschend | Sofortige eV auf Fortsetzung der Amtsstellung bis zur Klärung; parallel Anfechtungsklage |
| Kein schriftlicher Gesellschaftsvertrag (nur mündliche GbR) | Gesellschaftsvertrag dokumentieren; klare Beschlussmechanismen festlegen; Streitvermeidung durch schriftliche SHA |
| Schiedsklausel bereits vereinbart | Staatliche Eilmaßnahmen trotzdem möglich (§ 1041 ZPO); aber Hauptsache zum Schiedsgericht; Eilverfahren beim LG parallel einleiten |

## Präventive Klauseln (Streitvermeidung)

| Klausel | Wirkung | Empfehlung |
|---|---|---|
| Schlichtungspflicht vor Klage | Bezirksratspflicht beim Beirat; Ausnahme für Eilanträge | Senkt Eskalationskosten; Notarlösung als neutrale Schlichterrolle |
| DIS-Schiedsklausel | Vertrauliches Verfahren; fachkundige Schiedsrichter | Standard bei internationalem Gesellschafterkreis |
| Vorab-Bestellung neutraler Notar als Versammlungsleiter | Kein Streit über Versammlungsleitung | Bei absehbaren GV-Konflikten |
| Stimmverbots-Schärfung (SHA) | Klare Definition der Stimmverbotstatbestände jenseits § 47 Abs. 4 GmbHG | Individuelle Ergänzung möglich; aber Satzung hat Vorrang |
| Anti-Dilution-Klausel (SHA) | Schutz vor Down-Round-Verwässerung | Wichtigste präventive Maßnahme für Minderheitsinvestoren |

## Anschluss-Skills

- `gesellschaftsgruender-klauselkatalog-bilingual` — Stimmverbots-, Drag-Along-, Schiedsklauseln
- `gesellschaftsrecht:aufsichtsrat-protokoll` — Korrekte Dokumentation streitiger GV
- `gesellschaftsrecht:gesellschaftsrecht-mandat-arbeitsbereich` — Mandatsworkspace für Gesellschafterstreit
- `gesellschaftsgruender-rechtsformwahl` — Präventive Rechtsformwahl zur Streitvermeidung

## Quellen und Zitierweise

- §§ 935 ff. ZPO (Einstweilige Verfügung)
- § 16 Abs. 2 HGB analog (Registersperre)
- §§ 374 ff. FamFG (Registersachen)
- §§ 241, 243, 246 AktG analog (Beschlussmängel GmbH)
- § 47 Abs. 4 GmbHG (Stimmverbot)
- § 55 Abs. 4 GmbHG (Bezugsrecht bei Kapitalerhöhung)
- § 894 ZPO (Klage auf Willenserklärung)

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Scholz, GmbHG, 13. Aufl. 2024, § 47 Rn. 110 ff.; § 55 Rn. 80 ff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `gesellschaftsgruender-gesellschaftervereinbarung`

**Fokus:** Gesellschaftervereinbarung (SHA) neben dem Gesellschaftsvertrag entwerfen: Vorkaufsrechte, Drag-Along, Tag-Along. Normen: §§ 705 ff. BGB, GmbHG. Prüfraster: schuldrechtliche Bindung, Satzungsrang, Durchsetzbarkeit, Vertragsstrafe. Output: SHA-Entwurf mit Kernklauseln. Abgrenzung: nicht Gesellschaftsvertrag (nur notariell).

# Gesellschaftervereinbarung (Shareholder Agreement)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschaftervereinbarung (Shareholder Agreement)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der SHA

1. Handelt es sich um eine Gründer-interne SHA (ohne Investor) oder eine Investor-SHA nach Term Sheet?
2. Sind Vesting/Leaver-Klauseln für Gründer geplant — dann: Einziehungsmechanismus muss mit Satzung harmonieren (§ 34 GmbHG).
3. Existiert bereits eine Satzung — und stimmt die SHA mit ihr überein (Vinkulierung, Vorkaufsrechte)?
4. Sind bilinguale Klauseln erforderlich (internationaler Investor)?
5. Soll die SHA durch Schiedsklausel (DIS) oder vor staatlichem Gericht beigelegt werden?

## Zentrale Normen

- **§ 47 GmbHG** — Stimmrecht; Stimmbindungsvertrag wirkt nur schuldrechtlich, kein dinglicher Effekt auf GV-Beschlüsse.
- **§§ 34, 15 GmbHG** — Einziehung von Geschäftsanteilen; Grundlage für Vesting-/Leaver-Mechanismus.
- **§ 15 Abs. 5 GmbHG** — Vinkulierung: Anteilsübertragung nur mit Zustimmung; muss in Satzung geregelt sein.
- **§ 138 BGB** — Sittenwidrigkeit: Vesting- und Bad-Leaver-Klauseln können bei übermäßiger Härte nichtig sein.
- **§§ 74, 74a HGB** — Nachvertragliches Wettbewerbsverbot; § 74 Abs. 2 HGB: Karenzentschädigung 50 %.
- **§§ 1029 ff. ZPO** — Schiedsvereinbarung; DIS-SchO 2021 als Standard-Schiedsordnung.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## SHA-Baustein-Übersicht

| Klausel | Zweck | Satzungspflicht | BGH-Referenz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Vorkaufsrecht | Bestehende Gesellschafter haben Vorrang | Empfohlen in Satzung (§ 15 Abs. 5) | — |
| Drag-Along | Mehrheit zwingt Minderheit zum Mitverkauf | Satzung empfohlen | OLG Frankfurt |
| Tag-Along | Minderheit darf beim Mehrheitsverkauf mitfahren | Schuldrechtlich ausreichend | — |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Informationsrechte Investor | Quortalsbericht, Jahresabschluss | Schuldrechtlich ausreichend | — |
| Schiedsklausel DIS | Streitigkeiten vor Schiedsgericht | Formell: §§ 1029 ff. ZPO | — |

## Muster-Klauseln

### Vesting / Cliff

```
§ [X] Vesting und Leaver-Regelungen

(1) Die Anteile der Gründer ([Name 1], [Name 2]) unterliegen folgendem Vesting:
 - Cliff-Periode: 12 Monate ab Unterzeichnung
 - Nach Cliff: 25 % der Anteile unverzüglich vested
 - Danach: monatlich 1/48 der Gesamt-Anteile, über weitere 36 Monate

(2) Im Fall des Ausscheidens vor vollständigem Vesting:
 a) Good-Leaver-Situation: [Aufzählung Good-Leaver-Gruende]
 Gründer behält vested Anteile; non-vested Anteile werden zum Verkehrswert
 eingezogen. Verkehrswert = [Formel oder: fairer Marktwert laut Wirtschaftsprüfer].
 b) Bad-Leaver-Situation: [Aufzählung Bad-Leaver-Gruende]
 Non-vested Anteile werden zum Nominalwert eingezogen.

(3) Die Einziehung erfolgt gemäß § [Y] des Gesellschaftsvertrages (§ 34 GmbHG).
```

### Drag-Along

```
§ [X] Mitziehverpflichtung (Drag-Along)

(1) Sofern Gesellschafter, die zusammen mehr als 75 % der Stimmrechte halten
 (Dragging Shareholders), einen Verkauf sämtlicher Anteile an einen Dritten
 beschliessen, sind alle übrigen Gesellschafter verpflichtet, ihre Anteile
 unter denselben Konditionen und zum gleichen Preis an denselben Käufer zu
 veräussern (Mitziehverpflichtung).

(2) Die Dragging Shareholders müssen den übrigen Gesellschaftern mindestens
 [30] Tage vor dem Verkauf schriftlich Mitteilung machen.

(3) Alle Gesellschafter erhalten denselben Preis pro Anteil und dieselben
 Gewährleistungs- und Haftungsbedingungen.
```

## Schritt-für-Schritt-Workflow

1. **Triage** — 5 Triage-Fragen beantworten; Gründer-SHA oder Investor-SHA?
2. **Bausteine auswählen** — relevante Klauseln aus Übersichtstabelle ankreuzen.
3. **Vesting-Parameter** — Cliff-Dauer; Vesting-Periode; Good-/Bad-Leaver-Definitionen.
4. **Satzungs-Abgleich** — Einziehungsmechanismus (§ 34 GmbHG) und Vinkulierung (§ 15 Abs. 5 GmbHG) in Satzung einbauen.
5. **Schiedsklausel** — DIS-SchO 2021 empfehlen; schneller und diskreter als staatliches Gericht.
6. **Wettbewerbsverbot** — Dauer max. 2 Jahre; Karenzentschädigung min. 50 % letztes Gehalt.
7. **SHA finalisieren** — Entwurf mit allen Gründern abstimmen; ggf. bilingual.
8. **Unterzeichnung** — Schriftform (§ 126 BGB) oder elektronische Form; notarielle Beurkundung nicht zwingend, aber bei größeren Deals sinnvoll.

## Output-Template SHA-Eckdaten

**Adressat:** Gründer / Investor — Tonfall sachlich-präzise
```
SHA ECKDATEN [FIRMENNAME] GMBH
Parteien: [Namen aller Gesellschafter]
Datum: [Datum]
Version: [Nr.]

VESTING
Cliff: [X] Monate
Vesting-Dauer: [X] Monate nach Cliff
Good Leaver: [Auflistung]
Bad Leaver: [Auflistung]

LIQUIDATION PREFERENCE (falls Investor vorhanden)
Klasse: [Class A]
Präferenz: [1x non-participating / 1x participating]
Anti-Dilution: [Weighted Average broad-based]

VORKAUFSRECHT
Frist: [30] Tage
Preis: Drittangebot spiegeln

DRAG-ALONG-SCHWELLE: [75] % der Stimmrechte
TAG-ALONG: Ja / Nein

WETTBEWERBSVERBOT GF
Dauer: [X] Monate
Geografisch: [Deutschland / EU / weltweit]
Karenzentschädigung: [X] % letztes Grundgehalt

STREITBEILEGUNG: [DIS-Schiedsverfahren / Staatliches Gericht ORT]
SPRACHE: [Deutsch / Englisch / Bilingual]
```

## Rote Schwellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Stimmbindung ohne Einziehungsmechanismus in Satzung → kein dinglicher Effekt; nur Schadensersatz bei Verletzung.
- Wettbewerbsverbot ohne Karenzentschädigung → § 138 BGB Sittenwidrigkeitsrisiko; Schadensersatz statt Unterlassung.
- Drag-Along mit Schlechterstellung der Minderheit → treuwidrig (OLG Frankfurt); anfechtbar.
- SHA ohne Schiedsklausel → Streit vor staatlichem Gericht (öffentlich); DIS empfehlenswert.

## Quellen und Vertiefung

- §§ 15, 34, 47 GmbHG (Anteilsübertragung, Einziehung, Stimmrecht)
- §§ 74, 74a HGB (nachvertragliches Wettbewerbsverbot)
- §§ 1029 ff. ZPO / DIS-SchO 2021 (Schiedsverfahren)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Übergabe an andere Skills

- `gesellschaftsgruender-sha-satzung-stimmverpflichtung` — Abgleich SHA mit Satzung
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Einziehungsklausel § 34 GmbHG einbetten
- `gesellschaftsgruender-klauselkatalog-bilingual` — bilinguale SHA-Klauseln
- `gesellschaftsgruender-share-classes-a-b-c` — Klassensystem im SHA

## 4. `gesellschaftsgruender-gf-meeting-templates`

**Fokus:** Vorlagen für Geschäftsführersitzungen und Protokolle erstellen: Tagesordnung, Beschlussprotokoll, Aktionsliste. Normen: §§ 35 ff. GmbHG. Prüfraster: Beschlussfähigkeit, Umlaufverfahren, Dokumentationspflichten. Output: Meeting-Templates für GF-Sitzungen. Abgrenzung: nicht Gesellschafterversammlungs-Protokoll.

# GF-Meeting-Templates

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `GF-Meeting-Templates` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor jedem Meeting

1. Ist ein Beschluss zu fassen — dann BJR-konforme Dokumentation der Informationsgrundlage erforderlich (§ 43 GmbHG)?
2. Handelt es sich um ein reguläres Manage-Meeting oder einen außerordentlichen Anlass (Krise, Investor-Eintritt, Gesellschafterstreit)?
3. Sind externe Berater anwesend — dann Verschwiegenheitspflichten und Clean-Room-Anforderungen beachten.
4. Gibt es insiderinformationsrelevante Tagesordnungspunkte — dann Teilnehmerkreis einschränken.
5. Soll das Protokoll auf Deutsch, Englisch oder bilingual erstellt werden?

## Zentrale Normen

- **§ 43 GmbHG** — Sorgfaltspflicht GF: Entscheidungen müssen auf angemessener Informationsgrundlage beruhen; Protokoll als Haftungsschutz.
- **§ 48 GmbHG** — Gesellschafterversammlung und Umlaufbeschluss: schriftliche Abstimmung bei Einvernehmen aller.
- **§ 35 GmbHG** — Vertretung der Gesellschaft durch GF.
- **§ 51 GmbHG** — Form und Frist der GV-Einberufung: mindestens 1 Woche Vorlauf (abkürzbar durch Satzung).

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Meeting-Typen und Rhythmus

| Meeting-Typ | Rhythmus | Teilnehmer | Zweck |
|---|---|---|---|
| GF-Jour-Fixe | Wöchentlich | alle GF | Laufende Koordination, KPIs, Offene Punkte |
| Monatlicher Abschluss-Review | Monatlich | GF + Steuerberater | Finanzen, Liquidität, Steuern |
| Quartals-Review mit Beirat | Quartalsweise | GF + Beirat | Strategie, Performance, Risiken |
| Außerordentliches GF-Meeting | Bei Anlass | GF (ggf. Berater) | Krise, Investor, Gesellschafterstreit |
| Gesellschafterversammlung | Mindestens jährlich | Gesellschafter | Jahresabschluss, Beschlüsse (§ 46 GmbHG) |

## Template 1 — GF-Jour-Fixe Einladung (DE/EN)

**Deutsch**
```
Betreff: GF-Meeting [KW XX] — [Datum]

Liebe Kolleginnen und Kollegen,

hiermit lade ich zum wöchentlichen GF-Meeting ein:

Datum: [Wochentag], [Datum]
Uhrzeit: [Uhrzeit]
Ort: Videokonferenz [Link] / Konferenzraum [Ort]
Teilnehmer: [Namen, Funktionen]

TAGESORDNUNG
1. Begrüßung, Beschlussfähigkeit
2. Genehmigung Protokoll KW [X]
3. Kennzahlen / Status-Update (Dashboard Anlage [X])
4. [Konkreter Punkt 1]
5. [Konkreter Punkt 2 — Beschlussfassung]
6. Offene Punkte / TODO-Review
7. Sonstiges, Ausblick nächste Woche

Bitte Unterlagen bis [Datum T-1] an alle verteilen.
Bei Verhinderung: Umlaufbeschluss für eilbedürftige Themen.

[Name, Funktion]
```

**Englisch**
```
Subject: Management Meeting [CW XX] — [Date]

Dear colleagues,

I hereby invite you to the weekly management meeting:

Date: [Day], [Date]
Time: [Time] CET
Location: Video conference [Link] / Conference room [Location]
Attendees: [Names, Functions]

AGENDA
1. Welcome, quorum
2. Approval of minutes [CW X]
3. KPIs / status update (dashboard attached)
4. [Specific item 1]
5. [Specific item 2 — resolution]
6. Open items / TODO review
7. AOB, outlook next week

Please distribute documents by [Date T-1].
[Name, Function]
```

## Template 2 — GF-Protokoll (BJR-konform)

**Adressat:** Akte / Gesellschaft — Tonfall sachlich-juristisch
```
PROTOKOLL GESCHÄFTSFÜHRER-MEETING
Datum: [Datum]
Beginn: [Uhrzeit] Uhr / Ende: [Uhrzeit] Uhr
Ort: [Ort / Videokonferenz]
Protokollführer: [Name]

ANWESENDE
Name | Funktion | Anwesend
[Name 1] | CEO | Ja
[Name 2] | CTO | Ja (digital)
[Name 3] | CFO | Entschuldigt / Vertreten durch [Name]

BESCHLUSSFÄHIGKEIT: Ja / Nein — Begründung: [ggf.]

TOP 1: [TITEL]
Sachverhalt: [2-3 Sätze]
Informationsgrundlage: [Berater, Bericht, Marktdaten]
Alternativen erwogen: [kurz]
Beschluss: [Wortlaut des Beschlusses]
Abstimmung: [X] Ja / [X] Nein / [X] Enthaltung
Ergebnis: [angenommen / abgelehnt]
Verantwortlich: [Name]
Frist: [Datum]

TOP 2: [TITEL]
[wie oben]

OFFENE PUNKTE (TODO)
Nr. | Punkt | Owner | Frist | Priorität
1 | [Punkt] | [Name] | [Datum] | [hoch/mittel/niedrig]

NÄCHSTES MEETING: [Datum]

GENEHMIGUNG
Protokoll genehmigt: [ ] Ja am [Datum] / [ ] Nein (Einwände: [Einwand])
Unterschriften: [GF 1] ______________ [GF 2] ______________
```

## Template 3 — Umlaufbeschluss (§ 48 Abs. 2 GmbHG)

```
UMLAUFBESCHLUSS DER GESCHÄFTSFÜHRER
[Firmenname] GmbH

Datum: [Datum]
Beschlussgegenstand: [Thema]

Hiermit fassen die Geschäftsführer [Name 1] und [Name 2] folgenden Beschluss
im schriftlichen Verfahren gemäß § 48 Abs. 2 GmbHG:

BESCHLUSS:
[Wortlaut]

Informationsgrundlage: [Unterlage, Bericht, Beratungsergebnis]

ABSTIMMUNG
Geschäftsführer [Name 1]: [ ] Zustimmung [ ] Ablehnung [ ] Enthaltung
Geschäftsführer [Name 2]: [ ] Zustimmung [ ] Ablehnung [ ] Enthaltung

Annahme erfordert Einstimmigkeit bei § 48 Abs. 2 GmbHG.

Datum, Ort: __________ Unterschriften: __________
```

## Schritt-für-Schritt-Workflow

1. **Triage** — Meeting-Typ bestimmen; Beschlussbedarf identifizieren.
2. **Tagesordnung erstellen** — Punkte mit Informationsunterlagen verknüpfen.
3. **Einladung versenden** — mindestens 1 Woche Vorlauf (außerordentlich: kürzer möglich).
4. **Protokoll führen** — BJR-konform: Informationsgrundlage, Alternativen, Abstimmung.
5. **Offene Punkte** — TODO-Liste mit Owner und Frist aus Protokoll destillieren.
6. **Protokoll genehmigen** — Nächstes Meeting: TOP 1 immer Protokollgenehmigung.
7. **Archivieren** — Protokolle in Gesellschaftsakte; mindestens 10 Jahre aufbewahren.

## Rote Schwellen

- Protokoll fehlt bei wichtigem GF-Beschluss → kein Haftungsschutz BJR; GF trägt Beweislast (§ 43 Abs. 2 S. 2 GmbHG).
- Umlaufbeschluss ohne Einvernehmen aller GF → unwirksam (§ 48 Abs. 2 GmbHG).
- Informationsgrundlage nicht dokumentiert → BJR-Schutz entfällt.
- Protokoll nachträglich geändert ohne Genehmigungsvermerk → Beweiswert zweifelhaft.

## Quellen und Vertiefung

- §§ 35, 43, 48, 51 GmbHG (GF-Pflichten, Beschlussfähigkeit, Einberufung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Crezelius, GmbHG, § 43 Rn. 10-25

## Übergabe an andere Skills

- `gesellschaftsgruender-gv-protokoll-und-versammlungsleiter` — GV-Protokoll (Gesellschafterversammlung)
- `gesellschaftsgruender-gv-einladung-tagesordnung` — Gesellschafterversammlungs-Einladung
- `gesellschaftsgruender-beirat-advisory-board` — Beiratssitzungs-Templates

## 5. `gesellschaftsgruender-ggmbh-gemeinnuetzigkeit`

**Fokus:** Prüft gGmbH-Gründung, Satzungszweck, Mittelbindung und Finanzamt-Abstimmung.

# gGmbH und Gemeinnützigkeit

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `gGmbH und Gemeinnützigkeit` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Gemeinnützigkeitsklauseln, Zuwendungsbestätigung, Rücklagen.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.
