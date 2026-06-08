---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im GOÄ Gebührenordnung für Ärzte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor."
---

# GOÄ Gebührenordnung für Ärzte — Allgemein

## Sofortstart
Dieses Allgemein-Skill ist der Empfangstresen und Projektleiter des Plugins **GOÄ Gebührenordnung für Ärzte**. Es soll den Nutzer nicht belehren, sondern schnell arbeitsfähig machen: erst die Lage erfassen, dann den passenden Pfad wählen, dann direkt einen verwertbaren Output erzeugen.

**Plugin-Fokus:** Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

## Bei stummem Upload
Wenn der Nutzer nur ein Dokument, Bild, PDF, Vertrag, Bescheid, Tabellenwerk, E-Mail, Registerauszug oder Aktenkonvolut hochlädt, behandle das als Auftrag.

1. **Erkannt:** Dokumentart, Absender, Datum, Aktenzeichen, Beteiligte und Lebenssachverhalt nennen.
2. **Frist zuerst:** Zustellung, Rechtsbehelf, Behördenfrist, Zahlungsziel, Ausschlussfrist oder Verjährungsrisiko markieren.
3. **Einordnung:** Rechtsgebiet, Normengruppe, Behörde/Gericht und Arbeitstyp bestimmen.
4. **Primärer Pfad:** den wahrscheinlich passenden Fachmodul aus diesem Plugin nennen und bei eindeutigem Treffer direkt anwenden.
5. **Nur eine Rückfrage:** nur wenn ohne die Antwort ein falscher nächster Schritt droht.

## Intake in 60 Sekunden
- Wer fragt: Anwalt, Rechtsabteilung, Unternehmen, Patient, Apotheke, Krankenhaus, Verbraucher, Behörde, Soldat, Familie oder Verband?
- Was soll entstehen: Kurzprüfung, Memo, Schriftsatz, Antrag, Anzeige, Stellungnahme, Checkliste, Berechnung, Vertragsklausel, Behördenbrief oder Mandantenübersetzung?
- Was eilt: Frist, Termin, Zustellung, Anhörung, Ausschlussfrist, Verjährung, Bußgeld, Widerruf, Gebührenrisiko oder Verfahrensschritt?
- Welche Unterlagen liegen vor: Verträge, Bescheide, Rechnungen, Tabellen, Registerauszüge, Leitlinien, Formulare, E-Mails, Fotos, Chatverläufe?
- Was ist unsicher: Tatsachen, Zahlen, Zuständigkeit, Rechtslage, technische Daten, Marktdefinition, medizinischer Sachverhalt oder Familien-/Versorgungsverlauf?

## Arbeitsmodus
- **Schnelltriage:** Frist, Risiko, nächster Schritt.
- **Aktenmodus:** Dokumente sortieren, Timeline, Belegmatrix und Lückenliste.
- **Prüfmodus:** Tatbestand, Rechtsfolge, Gegenargumente, Risikoampel.
- **Entwurfsmodus:** Antrag, Schriftsatz, Vertragsklausel, Behördenbrief, Mandantenmail, Vorstandsvorlage.
- **Red-Team:** Ergebnis auf Halluzinationen, Quellen, Fristen, Zuständigkeit, Zahlen und Ton prüfen.

## Passende Einstiegsrouten
| Skill | Wann? |
| --- | --- |
| `goae-1-anwendungsbereich-berufliche-leistungen` | GOÄ § 1 Anwendungsbereich berufliche Leistungen |
| `goae-2-abweichende-vereinbarung-honorarvereinbarung` | GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung |
| `goae-3-verguetungen-gebuehren-entschaedigungen-auslagen` | GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen |
| `goae-4-selbstaendige-aerztliche-leistung-zielleistungsprinzip` | GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip |
| `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle` | GOÄ § 5 Bemessung Gebührenrahmen 2,3 1,8 1,15 Schwelle |
| `goae-5a-bemessung-im-basistarif` | GOÄ § 5a Bemessung im Basistarif |
| `goae-5b-standardtarif-pkv` | GOÄ § 5b Standardtarif PKV |
| `goae-6-gebuehren-für-andere-leistungen-analogbewertung` | GOÄ § 6 Gebühren für andere Leistungen Analogbewertung |
| `goae-6a-stationaere-minderung-25-prozent-15-prozent` | GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent |
| `goae-7-entschaedigungen` | GOÄ § 7 Entschädigungen |
| `goae-8-wegegeld` | GOÄ § 8 Wegegeld |
| `goae-9-reiseentschaedigung` | GOÄ § 9 Reiseentschädigung |
| `goae-10-ersatz-von-auslagen` | GOÄ § 10 Ersatz von Auslagen |
| `goae-12-faelligkeit-und-rechnungspflicht` | GOÄ § 12 Fälligkeit und Rechnungspflicht |
| `goae-14-zahlung-durch-öffentliche-leistungstraeger` | GOÄ § 14 Zahlung durch öffentliche Leistungsträger |
| `abschnitt-a-beratungen-und-untersuchungen` | Abschnitt A Beratungen und Untersuchungen |
| `abschnitt-b-grundleistungen-zuschlaege` | Abschnitt B Grundleistungen Zuschläge |
| `abschnitt-c-nichtgebietsbezogene-sonderleistungen` | Abschnitt C nichtgebietsbezogene Sonderleistungen |
| `laborleistungen-und-hoechstsatz-besonderheiten` | Laborleistungen und Höchstsatz Besonderheiten |
| `m-iii-m-iv-labor-delegation-speziallabor` | M III M IV Labor Delegation Speziallabor |
| `radiologie-schnittbild-zielleistung` | Radiologie Schnittbild Zielleistung |
| `op-komplexe-narkose-assistenz-zuschlaege` | OP-Komplexe Narkose Assistenz Zuschläge |
| `stationaere-privataerztliche-liquidation` | Stationäre privatärztliche Liquidation |
| `wahlleistungsvereinbarung-krankenhaus-goae` | Wahlleistungsvereinbarung Krankenhaus GOÄ |
| `belegarzt-und-konsiliararzt-abrechnung` | Belegarzt und Konsiliararzt Abrechnung |
| `igel-aufklaerung-kosteninformation` | IGeL Aufklärung Kosteninformation |
| `abrechnung-telemedizin-videosprechstunde-goae` | Abrechnung Telemedizin Videosprechstunde GOÄ |
| `materialkosten-auslagen-abgrenzung-10-goae` | Materialkosten Auslagen Abgrenzung § 10 GOÄ |
| `steigerungssatz-begruendung-individuell-patientenbezogen` | Steigerungssatz Begründung individuell patientenbezogen |
| `mehrfachansatz-ausschluesse-nebeneinanderberechnung` | Mehrfachansatz Ausschlüsse Nebeneinanderberechnung |
| `leistungskette-zielleistung-keine-aufspaltung` | Leistungskette Zielleistung keine Aufspaltung |
| `analoge-bewertung-neue-verfahren-innovation` | Analoge Bewertung neue Verfahren Innovation |
| `kosmetische-leistungen-medizinische-indikation` | Kosmetische Leistungen medizinische Indikation |
| `zahnaerztliche-schnittstelle-goz-goae` | Zahnärztliche Schnittstelle GOZ GOÄ |
| `psychotherapie-psychiatrie-gespraechsleistungen` | Psychotherapie Psychiatrie Gesprächsleistungen |

## Quellenregel
Vor tragenden Aussagen immer aktuelle Normtexte, amtliche Behördenseiten, EU-Texte oder frei zugängliche Entscheidungen prüfen. Keine BeckRS-/juris-/Kommentarzitate aus Modellwissen. Wenn eine Quelle nicht verifizierbar ist, deutlich sagen und nicht als Beleg verwenden.

<!-- BEGIN ACTUAL-SKILL-ROUTING -->

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `abrechnung-telemedizin-videosprechstunde-goae` | Abrechnung Telemedizin Videosprechstunde GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§... |
| `abschnitt-a-beratungen-und-untersuchungen` | Abschnitt A Beratungen und Untersuchungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `abschnitt-b-grundleistungen-zuschlaege` | Abschnitt B Grundleistungen Zuschläge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a f... |
| `abschnitt-c-nichtgebietsbezogene-sonderleistungen` | Abschnitt C nichtgebietsbezogene Sonderleistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertr... |
| `abtretung-factoring-arzthonorar-datenschutz` | Abtretung Factoring Arzthonorar Datenschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§... |
| `analogabrechnung-intake-6-goae` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Analogabrechnung Intake § 6 GOÄ. |
| `analoge-bewertung-neue-verfahren-innovation` | Analoge Bewertung neue Verfahren Innovation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§... |
| `arbeitsunfaehigkeitsbescheinigung-privatpatient` | Arbeitsunfähigkeitsbescheinigung Privatpatient: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag... |
| `arztbrief-begruendung-nachfordern` | Arztbrief Begründung nachfordern: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., P... |
| `arzthonorarprozess-dokumentenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Arzthonorarprozess Dokumentenplan. |
| `auslandsbehandlung-deutsche-goae-anwendung` | Auslandsbehandlung deutsche GOÄ Anwendung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `begruendung-ueber-schwellenwert-redigieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Begründung über Schwellenwert redigieren. |
| `beihilfe-einwendungen-und-differenzbetrag` | Beihilfe Einwendungen und Differenzbetrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `belegarzt-und-konsiliararzt-abrechnung` | Belegarzt und Konsiliararzt Abrechnung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a... |
| `berufsrecht-ueberhoehte-liquidation` | Berufsrecht überhöhte Liquidation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.,... |
| `erstattung-pkv-vs-honoraranspruch-patient` | Erstattung PKV vs Honoraranspruch Patient: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `faelligkeit-verzug-mahnung-honorarklage` | Fälligkeit Verzug Mahnung Honorarklage: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a... |
| `gebuehrenrahmen-schwellenwert-ampel` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Gebührenrahmen Schwellenwert Ampel. |
| `goae-1-anwendungsbereich-berufliche-leistungen` | GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag... |
| `goae-10-ersatz-von-auslagen` | GOÄ § 10 Ersatz von Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/B... |
| `goae-12-faelligkeit-und-rechnungspflicht` | GOÄ § 12 Fälligkeit und Rechnungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630... |
| `goae-14-zahlung-durch-öffentliche-leistungstraeger` | GOÄ § 14 Zahlung durch öffentliche Leistungsträger: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvert... |
| `goae-2-abweichende-vereinbarung-honorarvereinbarung` | GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsve... |
| `goae-3-verguetungen-gebuehren-entschaedigungen-auslagen` | GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsv... |
| `goae-4-selbstaendige-aerztliche-leistung-zielleistungsprinzip` | GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behan... |
| `goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle` | GOÄ § 5 Bemessung Gebührenrahmen 2 und 3 1 und 8 1 und 15 Schwelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB... |
| `goae-5a-bemessung-im-basistarif` | GOÄ § 5a Bemessung im Basistarif: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., P... |
| `goae-5b-standardtarif-pkv` | GOÄ § 5b Standardtarif PKV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Bei... |
| `goae-6-gebuehren-für-andere-leistungen-analogbewertung` | GOÄ § 6 Gebühren für andere Leistungen Analogbewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungs... |
| `goae-6a-stationaere-minderung-25-prozent-15-prozent` | GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsver... |
| `goae-7-entschaedigungen` | GOÄ § 7 Entschädigungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihil... |
| `goae-8-wegegeld` | GOÄ § 8 Wegegeld: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Rege... |
| `goae-9-reiseentschaedigung` | GOÄ § 9 Reiseentschädigung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Bei... |
| `goae-rechnung-aus-pdf-extrahieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema GOÄ Rechnung aus PDF extrahieren. |
| `goae-reform-referentenentwuerfe-beobachten` | GOÄ Reform Referentenentwürfe beobachten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630... |
| `gutachten-atteste-bescheinigungen` | Gutachten Atteste Bescheinigungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.,... |
| `igel-aufklaerung-kosteninformation` | IGeL Aufklärung Kosteninformation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.,... |
| `kaltstart-goae-rechnung-pruefen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart GOÄ Rechnung prüfen. |
| `klageerwiderung-honorarprozess` | Klageerwiderung Honorarprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV... |
| `kosmetische-leistungen-medizinische-indikation` | Kosmetische Leistungen medizinische Indikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag... |
| `laborleistungen-und-hoechstsatz-besonderheiten` | Laborleistungen und Höchstsatz Besonderheiten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §... |
| `leistungskette-zielleistung-keine-aufspaltung` | Leistungskette Zielleistung keine Aufspaltung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §... |
| `livecheck-goae-text-und-reformstand` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck GOÄ Text und Reformstand. |
| `m-iii-m-iv-labor-delegation-speziallabor` | M III M IV Labor Delegation Speziallabor: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630... |
| `mandantenmail-patient-freundlich-klar` | Mandantenmail Patient freundlich klar: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a f... |
| `materialkosten-auslagen-abgrenzung-10-goae` | Materialkosten Auslagen Abgrenzung § 10 GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§... |
| `mehrfachansatz-ausschluesse-nebeneinanderberechnung` | Mehrfachansatz Ausschlüsse Nebeneinanderberechnung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvert... |
| `minderjaehrige-einwilligung-rechnung-schuldner` | Minderjährige Einwilligung Rechnung Schuldner: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §... |
| `notfall-behandlung-ausserhalb-sprechstunde` | Notfall Behandlung außerhalb Sprechstunde: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `op-komplexe-narkose-assistenz-zuschlaege` | OP-Komplexe Narkose Assistenz Zuschläge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a... |
| `patientenbrief-und-einwendung-formulieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Patientenbrief und Einwendung formulieren. |
| `plausibilitaetscheck-rechnung-mathematisch` | Plausibilitätscheck Rechnung mathematisch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `psychotherapie-psychiatrie-gespraechsleistungen` | Psychotherapie Psychiatrie Gesprächsleistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag... |
| `radiologie-schnittbild-zielleistung` | Radiologie Schnittbild Zielleistung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.... |
| `red-team-goae-rechnung-halluzinationscheck` | Red-Team GOÄ Rechnung Halluzinationscheck: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `sachverstaendigenfragen-goae-streit` | Sachverständigenfragen GOÄ Streit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.,... |
| `schlichtungsstelle-aerztekammer-honorarstreit` | Schlichtungsstelle Ärztekammer Honorarstreit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§... |
| `stationaere-privataerztliche-liquidation` | Stationäre privatärztliche Liquidation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a... |
| `steigerungssatz-begruendung-individuell-patientenbezogen` | Steigerungssatz Begründung individuell patientenbezogen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlung... |
| `tabellenexport-goae-pruefliste` | Tabellenexport GOÄ Prüfliste: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/B... |
| `verjaehrung-aerztlicher-honoraranspruch` | Verjährung ärztlicher Honoraranspruch: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a f... |
| `wahlleistungsvereinbarung-krankenhaus-goae` | Wahlleistungsvereinbarung Krankenhaus GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 63... |
| `wegegeld-besuch-mehrere-patienten` | Wegegeld Besuch mehrere Patienten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.,... |
| `zahnaerztliche-schnittstelle-goz-goae` | Zahnärztliche Schnittstelle GOZ GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff.... |

<!-- END ACTUAL-SKILL-ROUTING -->
