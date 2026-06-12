# Megaprompt: goae-gebuehrenordnung-aerzte

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 65 Skills des Plugins `goae-gebuehrenordnung-aerzte`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im GOÄ Gebührenordnung für Ärzte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen,…
2. **abschnitt-c-nichtgebietsbezogene-sonderleistungen** — Abschnitt C nichtgebietsbezogene Sonderleistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausna…
3. **anwendungsbereich-berufliche-abweichende** — GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahm…
4. **arbeitsunfaehigkeitsbescheinigung-privatpatient** — Arbeitsunfähigkeitsbescheinigung Privatpatient: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahme…
5. **goae-2-abweichende-vereinbarung-honorarvereinbarung** — GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Au…
6. **goae-3-verguetungen-gebuehren-entschaedigungen-auslagen** — GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und A…
7. **goae-6-gebuehren-fuer-andere-leistungen-analogbewertung** — GOÄ § 6 Gebühren für andere Leistungen Analogbewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und …
8. **goae-6a-stationaere-minderung-25-prozent-15-prozent** — GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Aus…
9. **goae-selbstaendige-aerztliche-bemessung** — GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risike…
10. **kosmetische-leistungen-medizinische-indikation** — Kosmetische Leistungen medizinische Indikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahme…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im GOÄ Gebührenordnung für Ärzte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor._

# GOÄ Gebührenordnung für Ärzte — Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Goae Gebuehrenordnung Aerzte** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

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

---

## Skill: `abschnitt-c-nichtgebietsbezogene-sonderleistungen`

_Abschnitt C nichtgebietsbezogene Sonderleistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnung A..._

# Abschnitt C nichtgebietsbezogene Sonderleistungen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Abschnitt C nichtgebietsbezogene Sonderleistungen
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Skill: `anwendungsbereich-berufliche-abweichende`

_GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnung Aer..._

# GOÄ § 1 Anwendungsbereich berufliche Leistungen

## Arbeitsbereich

GOÄ § 1 Anwendungsbereich berufliche Leistungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GOÄ § 1 Anwendungsbereich berufliche Leistungen
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Worum geht es konkret

§ 1 GOÄ definiert den Anwendungsbereich der Gebührenordnung für Ärzte: Berufliche Leistungen approbierter Ärzte gegenüber Privatpatienten und Selbstzahlern. GKV-Leistungen sind nicht von der GOÄ erfasst (EBM, § 87 SGB V). Abgrenzung: nichtärztliche Leistungen, IGel, Wahlleistungen Krankenhaus, telemedizinische Leistungen — alle haben ihre eigenen Spezialregeln, gehen aber im Grundsatz auf § 1 GOÄ zurück.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Erstellung einer Privatrechnung — Anwendungsbereich vorab klären.
- Streit, ob eine Leistung überhaupt nach GOÄ abrechenbar ist (z. B. IGel, Wahlleistung, Gutachten).
- Mandant ist nicht Privatversicherter, sondern Beihilfeberechtigter, Selbstzahler oder PKV-Patient.
- Honoraranspruch zu einem Auslandsbehandlungsfall.

Eingaben:
- Approbationsstatus der Ärztin/des Arztes.
- Patientenstatus (PKV, Beihilfe, GKV-Privatabrechnung, Selbstzahler, IGel).
- Behandlungsumfang und -gegenstand.
- Behandlungsvertrag (sofern schriftlich).
- ggf. Wahlleistungsvereinbarung.

## Rechtlicher Rahmen

- **§ 1 GOÄ:** Anwendungsbereich — berufliche Leistungen approbierter Ärzte.
- **§ 1 Abs. 1 GOÄ:** Die GOÄ gilt für die Vergütung beruflicher Leistungen approbierter Ärzte, soweit nicht durch Bundesgesetz andere Regelungen bestehen.
- **§ 2 GOÄ:** Abweichende Honorarvereinbarung — eng begrenzt zulässig.
- **§ 87 SGB V:** EBM für GKV-Vertragsärzte.
- **§§ 630a ff. BGB:** Behandlungsvertrag.
- **§ 12 GOÄ:** Fälligkeit und Rechnungspflicht.
- **Berufsordnung der Ärztekammern** (§ 12 MBO-Ä) — Verbot ungerechtfertigt hoher Liquidationen.
- BGH staend. Rspr. zur Abgrenzung Heilbehandlung / Begutachtung / IGel.

## / Schritt für Schritt

1. **Approbation prüfen:** Approbationsurkunde Ärztin/Arzt vorhanden? Ohne Approbation kein GOÄ-Anwendungsbereich (Berufserlaubnis genügt im Einzelfall).
2. **Patientenstatus klären:**
 - PKV-Privatpatient: GOÄ-Anwendung vollumfänglich.
 - Beihilfeberechtigter: GOÄ + Beihilfeverordnung des Dienstherrn (Bund/Land).
 - GKV-Patient mit Privatbehandlung (z. B. IGel): GOÄ-Anwendung mit Hinweispflicht.
 - Selbstzahler: GOÄ-Anwendung.
 - Auslandsbehandlung: GOÄ-Anwendung nach deutschem Recht.
3. **Leistung klassifizieren:**
 - Heilbehandlung im engeren Sinn: GOÄ direkt.
 - Gutachten/Bescheinigung: GOÄ Abschnitt L (Sonderleistungen).
 - Wahlleistung Krankenhaus: GOÄ § 6a + Wahlleistungsvereinbarung.
 - Telemedizin: GOÄ + spezielle GOÄ-Ziffern (vom Anwender zu verifizieren — laufende Anpassungen).
4. **Abweichende Honorarvereinbarung:** § 2 GOÄ — nur in engen Grenzen zulässig.
5. **Schwellenwert/Höchstsatz:** § 5 GOÄ — Bemessung.
6. **Rechnungserstellung:** § 12 GOÄ — Fälligkeit erst nach formgerechter Rechnung.

## Trade-off-Matrix

| Patientenstatus | GOÄ-Anwendung | Besonderheit |
|---|---|---|
| PKV-Vollprivatpatient | direkt | Erstattung nach Tarif |
| Beihilfe-Berechtigter | direkt | Erstattungsgrenze Beihilfe + ggf. PKV |
| GKV mit IGel | nur für IGel | schriftliche Aufklärung Pflicht |
| GKV mit "Privatbehandlung" (Wunsch des Patienten) | direkt für Privatleistung | Hinweispflicht, dass GKV-Anspruch besteht |
| Selbstzahler ohne Versicherung | direkt | besondere Hinweispflicht Kosten |
| Auslandspatient | direkt nach deutschem Recht | Übersetzung Rechnung empfehlenswert |
| Werksarzt mit Anstellungsverhältnis | nicht GOÄ | Arbeitsrechtsvergütung |

## Praxistipps

- IGel-Aufklärung schriftlich, mit Kostenvoranschlag — sonst keine Anspruchsgrundlage gegen Patient.
- Bei "Privatbehandlung" eines GKV-Patienten: schriftliche Erklärung des Patienten verlangen, dass er Privatleistung wünscht und Kostenpflicht akzeptiert.
- Approbationsurkunde im Praxis-Stammbuch ablegen — bei Streit vorzeigbar.
- Bei Auslandspatient Rechnung in deutscher Sprache mit englischer Kurzfassung; Bezahlung in EUR.
- Wahlleistung Krankenhaus: § 17 KHEntgG i.V.m. § 6a GOÄ; Vereinbarung Wahlleistung notwendig.

## Mustertexte

### IGel-Aufklärung (Auszug)
"Sehr geehrte:r [Patient:in], die von Ihnen gewünschte Leistung [Bezeichnung] ist nicht im Leistungskatalog der gesetzlichen Krankenkasse enthalten. Sie wird als Individuelle Gesundheitsleistung (IGel) abgerechnet. Die Vergütung erfolgt nach der Gebührenordnung für Ärzte (GOÄ). Geschätzte Kosten: [EUR brutto]. Bei Mehrbedarf werden Sie vor Durchführung erneut informiert. Bitte bestätigen Sie nachstehend, dass Sie die Privatbehandlung wünschen und die Kosten selbst tragen."

### Klarstellung Rechnung an Patient (Auszug)
"Die berechnete Leistung [Ziffer] erfolgte als berufliche Leistung im Sinne des § 1 GOÄ. Sie sind als [PKV-Patient / Beihilfeberechtigter / Selbstzahler] Schuldner:in der Vergütung. Die Erstattung durch Ihre Versicherung obliegt Ihnen; wir leisten gerne unterstützend Auskunft."

## Typische Fehler

- GOÄ-Rechnung an GKV-Patienten ohne explizite Privatbehandlung — Forderung nicht durchsetzbar.
- IGel ohne schriftliche Aufklärung; § 630c BGB-Aufklärungspflicht verletzt — keine Vergütung.
- Werksarztleistung wird nach GOÄ abgerechnet — Vergütung über Arbeitsvertrag, nicht GOÄ.
- Bei Beihilfe wird Patient als Vollerstatter behandelt — Beihilfegrenze und PKV-Tarif beachten.
- Auslandspatient wird in dortiger Sprache abgerechnet — Verständnisproblem, Anspruchsdurchsetzung erschwert.

## Quellen Stand 06/2026

- GOÄ §§ 1, 2, 5, 12 — Stand zur Berechnung im amtlichen Bundesgesetzblatt prüfen.
- GOÄ-Reform 2024/2025 — vom Anwender zu verifizieren (laufende politische Anpassungen, ggf. neue Gebührenordnung).
- BGB §§ 630a–630h.
- KHEntgG § 17.
- Berufsordnung Ärztekammer (MBO-Ä § 12).
- BGH staend. Rspr. zur GOÄ-Anwendung.
- PKV-Verband — Erstattungsleitlinien (informativ, nicht verbindlich).

---

## Skill: `arbeitsunfaehigkeitsbescheinigung-privatpatient`

_Arbeitsunfähigkeitsbescheinigung Privatpatient: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnung Aerzte._

# Arbeitsunfähigkeitsbescheinigung Privatpatient

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Arbeitsunfähigkeitsbescheinigung Privatpatient
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Skill: `goae-2-abweichende-vereinbarung-honorarvereinbarung`

_GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnun..._

# GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung

## Arbeitsbereich

GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GOÄ § 2 abweichende Vereinbarung Honorarvereinbarung
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Worum geht es konkret

§ 2 GOÄ erlaubt eine vom Regelfall abweichende Honorarvereinbarung — typischer Anwendungsfall: Steigerungsfaktor über dem Schwellenwert (3,5-fach für persönliche, 2,5-fach für technische, 1,3-fach für Labor). Strikte Formvorgaben: vor Behandlungsbeginn, schriftlich, persönlich vom Patienten unterzeichnet, mit Hinweis auf abweichende Vereinbarung. Verstösse machen die Vereinbarung unwirksam — Erstattung durch PKV oder Beihilfe meist verweigert.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Praxis will Honorarvereinbarung über Schwellenwert hinaus treffen.
- PKV verweigert Erstattung wegen "fehlender Schriftform" der Vereinbarung.
- Patient widerruft Honorarvereinbarung.
- Streit über Wirksamkeit einer mündlichen Absprache.
- Wahlleistungsvereinbarung Krankenhaus + GOÄ-Honorar (Abgrenzung § 6a GOÄ vs. § 2 GOÄ).

Eingaben:
- Bestehende oder geplante Honorarvereinbarung (Vorlage).
- Datum der Behandlung / Unterzeichnung.
- Korrespondenz Patient–PKV.
- ggf. Aufklärungsdokumentation.

## Rechtlicher Rahmen

- **§ 2 GOÄ:** Abweichende Vereinbarung über die Höhe der Vergütung — Schriftform, vor Erbringung, individuelle Vereinbarung; keine standardisierten Klauseln.
- **§ 2 Abs. 1 S. 2 GOÄ:** Mindestinhalt — Bezeichnung Leistung, abweichender Gebührensatz, Hinweis dass Vereinbarung über den Schwellenwert hinausgeht.
- **§ 2 Abs. 2 GOÄ:** Aushang Möglichkeit der abweichenden Vereinbarung in Praxis (vom Anwender Stand zu verifizieren).
- **§ 305c BGB:** Überraschende Klauseln in AGB unwirksam.
- **§§ 305 ff. BGB:** AGB-Kontrolle — Honorarvereinbarung als Individualabrede einzuordnen.
- **§ 5 GOÄ:** Bemessung — Regelfall innerhalb Schwellenwert.
- BGH staend. Rspr. zur Wirksamkeit § 2-Vereinbarungen, insb. Schriftform und vorheriger Abschluss.

## / Schritt für Schritt

1. **Geplanter Steigerungsfaktor:** Über oder unter Schwellenwert (2,3; 1,8; 1,15)?
2. **Falls darüber — § 2 GOÄ-Vereinbarung nötig.**
3. **Form:** Schriftlich, persönlich unterzeichnet — keine elektronische Signatur ohne qualifizierte Signatur des Patienten (vom Anwender zu verifizieren).
4. **Zeitpunkt:** Vor Erbringung der Leistung. Spätere Vereinbarung ist regelmässig unwirksam.
5. **Inhalt:**
 - Konkrete Leistung (Ziffer, Bezeichnung).
 - Steigerungsfaktor und resultierender Betrag.
 - Hinweis "Diese Vereinbarung weicht von den Gebührensätzen der GOÄ ab".
 - Hinweis auf voraussichtliche fehlende Erstattung durch PKV/Beihilfe oberhalb des Schwellenwerts.
6. **Individualität:** Keine Massentechnik — Patient muss konkret zustimmen.
7. **Erstattungsfähigkeit:** PKV/Beihilfe erstatten regelmässig nur bis Schwellenwert ohne Bedingung; Mehrbetrag oft nicht.
8. **Dokumentation:** Original in Patientenakte.

## Trade-off-Matrix

| Fallgruppe | § 2 GOÄ erforderlich | Erstattung | Risiko |
|---|---|---|---|
| Steigerung bis Schwellenwert (2,3) | nein | regelmässig voll | gering |
| Steigerung über Schwellenwert (3,5-fach) | ja, schriftlich | nur bei besonderer Begründung | hoch ohne Vereinbarung |
| Höchstsatz Labor (1,3) überschritten | ja | meist nicht | hoch |
| Wahlleistung Krankenhaus | gesondert § 6a + Wahlvereinbarung | nach Wahlvereinbarung | mittel |
| Wunschleistung (IGel) | gesondert IGel-Aufklärung | nicht durch Kasse | gering bei Doku |
| Auslandsbehandlung | wie inland | nach Tarif | mittel |

## Praxistipps

- Honorarvereinbarung niemals "blanket" — Patient muss verstehen, was er unterschreibt.
- Standardklauseln in Praxis-AGB sind regelmässig unwirksam (§ 305c BGB).
- Faktorenangabe konkret, keine "bis zu"-Formulierung.
- Patient ausdrücklich auf voraussichtliche fehlende PKV-Erstattung hinweisen (§ 630c BGB-Aufklärungspflicht).
- Kopie an Patient aushändigen, Original Praxis.
- Bei Beihilfe-Berechtigten: Beihilfe-Tarif kennt regelmässig nur den Schwellenwert; Mehrbetrag aus eigener Tasche.

## Mustertexte

### Honorarvereinbarung § 2 GOÄ (Auszug)
"Honorarvereinbarung gemäss § 2 GOÄ. Zwischen [Patient, Anschrift, Geb.-Datum] und [Arzt, Anschrift] wird vereinbart: Die in der Anlage 1 aufgeführten Leistungen werden mit einem Gebührensatz von [Faktor], d. h. [EUR] berechnet. Dies weicht von den Regelsätzen der GOÄ ab (Schwellenwert 2,3 für persönliche, 1,8 für technische, 1,15 für Labor). Ich, der/die Patient:in, bin darüber aufgeklärt, dass meine Krankenversicherung diese erhöhte Vergütung ggf. nicht oder nicht vollständig erstattet. Eine Erstattungs- oder Kostenzusage liegt mir nicht vor. Die Vereinbarung ist vor Beginn der Behandlung individuell abgeschlossen. Ort, Datum, Unterschrift Patient:in / Arzt."

### Hinweis an Patient zur PKV-Erstattung (Auszug)
"Bitte beachten Sie: Die im Folgenden vereinbarten Honorare können den von Ihrer privaten Krankenversicherung erstatteten Betrag übersteigen. Wir empfehlen, die Erstattungsfähigkeit vor Behandlungsbeginn bei Ihrer Versicherung anzufragen. Die Differenz tragen Sie selbst."

## Typische Fehler

- Honorarvereinbarung erst nach Behandlung unterschrieben — unwirksam.
- Standardklausel in Praxis-AGB — Massentechnik, unwirksam.
- "Bis zu 3,5-fach"-Formulierung — nicht hinreichend bestimmt.
- Aufklärung über fehlende Erstattung fehlt — § 630c BGB-Verletzung.
- Vereinbarung ohne konkrete Leistungsangabe — unwirksam.
- Patient unterschreibt unter Zeitdruck im Empfang — Anfechtungsrisiko.

## Quellen Stand 06/2026

- GOÄ § 2, § 5, § 6a.
- BGB §§ 305 ff., 630a–630h.
- BGH staend. Rspr. zur Honorarvereinbarung (Schriftform, vorheriger Abschluss, Individualität).
- Berufsordnung Ärztekammer.
- GOÄ-Reform 2024/2025 — vom Anwender Aktualität zu verifizieren.
- PKV-Verband — Hinweise zur Erstattung von Honorarvereinbarungen (informativ).

---

## Skill: `goae-3-verguetungen-gebuehren-entschaedigungen-auslagen`

_GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnu..._

# GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen

## Arbeitsbereich

GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GOÄ § 3 Vergütungen Gebühren Entschädigungen Auslagen
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Skill: `goae-6-gebuehren-fuer-andere-leistungen-analogbewertung`

_GOÄ § 6 Gebühren für andere Leistungen Analogbewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordn..._

# GOÄ § 6 Gebühren für andere Leistungen Analogbewertung

## Arbeitsbereich

GOÄ § 6 Gebühren für andere Leistungen Analogbewertung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GOÄ § 6 Gebühren für andere Leistungen Analogbewertung
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Skill: `goae-6a-stationaere-minderung-25-prozent-15-prozent`

_GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnung..._

# GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent

## Arbeitsbereich

GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GOÄ § 6a stationäre Minderung 25 Prozent 15 Prozent
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Skill: `goae-selbstaendige-aerztliche-bemessung`

_GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebühr..._

# GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip

## Arbeitsbereich

GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: GOÄ § 4 selbständige ärztliche Leistung Zielleistungsprinzip
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Skill: `kosmetische-leistungen-medizinische-indikation`

_Kosmetische Leistungen medizinische Indikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, aktuelle GOÄ-Reformhinweise im Goae Gebührenordnung Aerzte._

# Kosmetische Leistungen medizinische Indikation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kosmetische Leistungen medizinische Indikation
- **Normen-/Quellenanker:** GOÄ, BGB-Behandlungsvertrag, ärztliches Berufsrecht, § 12 GOÄ-Rechnung, Analogbewertung, Honorarvereinbarung, Erstattung PKV/Beihilfe.
- **Entscheidende Weiche:** Prüfe Leistungsinhalt, Ziffer, Steigerungsfaktor, Begründung, Auslagen, Wahlleistung, Schuldner, Erstattungsfähigkeit und Einwendungsfrist.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

