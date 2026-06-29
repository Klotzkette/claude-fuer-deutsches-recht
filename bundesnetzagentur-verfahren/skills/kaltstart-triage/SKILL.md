---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Bundesnetzagentur-Verfahren-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor."
---

# Bundesnetzagentur-Verfahren — Allgemein

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 29 EnWG` — Festlegung und Genehmigung durch Regulierungsbehoerde.
- `§ 65 EnWG` — Aufsichtsmassnahmen.
- `§ 75 EnWG` — Beschwerde gegen Entscheidungen der Regulierungsbehoerde.
- `§ 80 EnWG` — Rechtsbeschwerde.
- `§ 67 TKG` — Anordnungen der Bundesnetzagentur.
- `§ 149 TKG` — Bussgeldvorschriften.
- `§ 40 PostG` — Aufsicht.
- `§ 44 VwVfG` — Nichtigkeit Verwaltungsakt.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Sofortstart
Dieses Allgemein-Skill ist der Empfangstresen und Projektleiter des Plugins **Bundesnetzagentur-Verfahren**. Es soll den Nutzer nicht belehren, sondern schnell arbeitsfähig machen: erst die Lage erfassen, dann den passenden Pfad wählen, dann direkt einen verwertbaren Output erzeugen.

**Plugin-Fokus:** Anwaltliche Verfahren mit der Bundesnetzagentur: Zuständigkeit, Beschlusskammern, Konsultationen, Auskünfte, Bußgelder, Beschwerden, Energie-, TK-, Post-, Eisenbahn- und DSA-Regulierung.

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
| `energie-netzanschluss-strom` | Energie: Netzanschluss Strom |
| `energie-netzanschluss-gas` | Energie: Netzanschluss Gas |
| `energie-netzentgelte-strom` | Energie: Netzentgelte Strom |
| `energie-netzentgelte-gas` | Energie: Netzentgelte Gas |
| `energie-anreizregulierung-erloesobergrenze` | Energie: Anreizregulierung Erlösobergrenze |
| `energie-unbundling-entflechtung` | Energie: Unbundling Entflechtung |
| `energie-messstellenbetrieb-msbg-smart-meter` | Energie: Messstellenbetrieb MsbG Smart Meter |
| `energie-redispatch-2-0` | Energie: Redispatch 2.0 |
| `energie-bilanzkreis-strom` | Energie: Bilanzkreis Strom |
| `energie-bilanzkreis-gas` | Energie: Bilanzkreis Gas |
| `energie-regelenergie` | Energie: Regelenergie |
| `energie-kapazitaetsvergabe-gas` | Energie: Kapazitätsvergabe Gas |
| `energie-wasserstoffnetz-regulierung` | Energie: Wasserstoffnetz Regulierung |
| `energie-ladesaeulen-elektromobilitaet` | Energie: Ladesäulen Elektromobilität |
| `energie-eeg-netzanschluss-einspeisemanagement` | Energie: EEG Netzanschluss Einspeisemanagement |
| `energie-kwkg-zuschlaege` | Energie: KWKG Zuschläge |
| `energie-offshore-netzanbindung` | Energie: Offshore-Netzanbindung |
| `energie-nabeg-planfeststellung` | Energie: NABEG Planfeststellung |
| `energie-bbplg-leitungsvorhaben` | Energie: BBPlG Leitungsvorhaben |
| `energie-versorgungssicherheit-monitoring` | Energie: Versorgungssicherheit Monitoring |
| `energie-remit-marktmissbrauch-energie` | Energie: REMIT Marktmissbrauch Energie |
| `energie-grosshandelsdaten-transparenz` | Energie: Großhandelsdaten Transparenz |
| `energie-energieverbraucher-beschwerde` | Energie: Energieverbraucher Beschwerde |
| `energie-lieferantenwechsel-energie` | Energie: Lieferantenwechsel Energie |
| `energie-grundversorgung-ersatzversorgung` | Energie: Grundversorgung Ersatzversorgung |
| `energie-fernwaerme-schnittstelle-soweit-bnetza-nicht-zuständig` | Energie: Fernwärme Schnittstelle soweit BNetzA nicht zuständig |
| `telekommunikation-frequenzzuteilung` | Telekommunikation: Frequenzzuteilung |
| `telekommunikation-frequenzauktion` | Telekommunikation: Frequenzauktion |
| `telekommunikation-nummernverwaltung` | Telekommunikation: Nummernverwaltung |
| `telekommunikation-rufnummernmissbrauch` | Telekommunikation: Rufnummernmissbrauch |
| `telekommunikation-tkg-marktregulierung-betraechtliche-marktmacht` | Telekommunikation: TKG Marktregulierung beträchtliche Marktmacht |
| `telekommunikation-zugangsregulierung-telekommunikation` | Telekommunikation: Zugangsregulierung Telekommunikation |
| `telekommunikation-entgeltgenehmigung-telekommunikation` | Telekommunikation: Entgeltgenehmigung Telekommunikation |
| `telekommunikation-universaldienst-telekommunikation` | Telekommunikation: Universaldienst Telekommunikation |
| `telekommunikation-netzneutralitaet-open-internet` | Telekommunikation: Netzneutralität Open Internet |

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `aktenzugang-geschaeftsgeheimnisse-schwaerzung` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Aktenzugang Geschäftsgeheimnisse Schwärzung. |
| `anhoerung-auskunftsbeschluss-fristenplan` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Anhörung Auskunftsbeschluss Fristenplan. |
| `beschwerde-verbraucher-unternehmen-verband` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Beschwerde Verbraucher Unternehmen Verband. |
| `digital-services-algorithmen-empfehlungssysteme-dsa` | Digital Services / Algorithmen Empfehlungssysteme DSA: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quel... |
| `digital-services-aussergerichtliche-streitbeilegungsstelle-dsa` | Digital Services / Außergerichtliche Streitbeilegungsstelle DSA: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzage... |
| `digital-services-dark-patterns-dsa-schnittstelle` | Digital Services / Dark Patterns DSA Schnittstelle: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellen... |
| `digital-services-datenzugang-forscher-dsa` | Digital Services / Datenzugang Forscher DSA: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker:... |
| `digital-services-digital-services-coordinator-ddg` | Digital Services / Digital Services Coordinator DDG: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quelle... |
| `digital-services-dsa-beschwerde-plattform` | Digital Services / DSA Beschwerde Plattform: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker:... |
| `digital-services-melde-und-abhilfeverfahren-notice-and-action` | Digital Services / Melde- und Abhilfeverfahren Notice and Action: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzag... |
| `digital-services-nationale-koordinierung-dsa-behoerden` | Digital Services / Nationale Koordinierung DSA Behörden: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Qu... |
| `digital-services-online-werbung-transparenz-dsa` | Digital Services / Online-Werbung Transparenz DSA: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellena... |
| `digital-services-transparenzberichte-online-plattformen` | Digital Services / Transparenzberichte Online-Plattformen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur.... |
| `digital-services-trusted-flagger-anerkennung` | Digital Services / Trusted Flagger Anerkennung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanke... |
| `digital-services-vlop-vlose-koordination-eu-kommission` | Digital Services / VLOP VLOSE Koordination EU-Kommission: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Q... |
| `eilverfahren-verwaltungsgericht-strategie` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Eilverfahren Verwaltungsgericht Strategie. |
| `eisenbahn-anreizsetzung-schiene` | Eisenbahn / Anreizsetzung Schiene: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG... |
| `eisenbahn-baumassnahmen-und-sperrpausen` | Eisenbahn / Baumaßnahmen und Sperrpausen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERe... |
| `eisenbahn-beschwerde-evu-gegen-infrastrukturbetreiber` | Eisenbahn / Beschwerde EVU gegen Infrastrukturbetreiber: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Qu... |
| `eisenbahn-eisenbahnregulierung-eregg` | Eisenbahn / Eisenbahnregulierung ERegG: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG... |
| `eisenbahn-entgeltregulierung-schiene` | Eisenbahn / Entgeltregulierung Schiene: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG... |
| `eisenbahn-kapazitaetskonflikt-fahrplan` | Eisenbahn / Kapazitätskonflikt Fahrplan: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EReg... |
| `eisenbahn-netznutzungsbedingungen` | Eisenbahn / Netznutzungsbedingungen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, A... |
| `eisenbahn-regulierungsvereinbarung-db-netz-infrago` | Eisenbahn / Regulierungsvereinbarung DB Netz InfraGO: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quell... |
| `eisenbahn-serviceeinrichtungen` | Eisenbahn / Serviceeinrichtungen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG,... |
| `eisenbahn-stationszugang` | Eisenbahn / Stationszugang: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Ei... |
| `eisenbahn-stilllegung-infrastruktur-schnittstelle` | Eisenbahn / Stilllegung Infrastruktur Schnittstelle: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quelle... |
| `eisenbahn-trassenzugang` | Eisenbahn / Trassenzugang: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eis... |
| `energie-anreizregulierung-erloesobergrenze` | Energie / Anreizregulierung Erlösobergrenze: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker:... |
| `energie-bbplg-leitungsvorhaben` | Energie / BBPlG Leitungsvorhaben: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV... |
| `energie-bilanzkreis-gas` | Energie / Bilanzkreis Gas: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, Strom... |
| `energie-bilanzkreis-strom` | Energie / Bilanzkreis Strom: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, Str... |
| `energie-eeg-netzanschluss-einspeisemanagement` | Energie / EEG Netzanschluss Einspeisemanagement: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenank... |
| `energie-energieverbraucher-beschwerde` | Energie / Energieverbraucher Beschwerde: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG... |
| `energie-fernwaerme-schnittstelle-soweit-bnetza-nicht-zuständig` | Energie / Fernwärme Schnittstelle soweit BNetzA nicht zuständig: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzage... |
| `energie-grosshandelsdaten-transparenz` | Energie / Großhandelsdaten Transparenz: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG,... |
| `energie-grundversorgung-ersatzversorgung` | Energie / Grundversorgung Ersatzversorgung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: E... |
| `energie-kapazitaetsvergabe-gas` | Energie / Kapazitätsvergabe Gas: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV,... |
| `energie-kwkg-zuschlaege` | Energie / KWKG Zuschläge: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, StromN... |
| `energie-ladesaeulen-elektromobilitaet` | Energie / Ladesäulen Elektromobilität: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG,... |
| `energie-lieferantenwechsel-energie` | Energie / Lieferantenwechsel Energie: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, A... |
| `energie-messstellenbetrieb-msbg-smart-meter` | Energie / Messstellenbetrieb MsbG Smart Meter: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker... |
| `energie-nabeg-planfeststellung` | Energie / NABEG Planfeststellung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV... |
| `energie-netzanschluss-gas` | Energie / Netzanschluss Gas: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, Str... |
| `energie-netzanschluss-strom` | Energie / Netzanschluss Strom: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, S... |
| `energie-netzentgelte-gas` | Energie / Netzentgelte Gas: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, Stro... |
| `energie-netzentgelte-strom` | Energie / Netzentgelte Strom: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, St... |
| `energie-offshore-netzanbindung` | Energie / Offshore-Netzanbindung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV... |
| `energie-redispatch-2-0` | Energie / Redispatch 2.0: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, StromN... |
| `energie-regelenergie` | Energie / Regelenergie: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: EnWG, ARegV, StromNEV... |
| `energie-regulierungsakte-anreizregulierung-erloesobergrenze-fris` | Anreizregulierung Erlösobergrenze: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-anreizregulierung-erloesobergrenze-rech` | Anreizregulierung Erlösobergrenze: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-anreizregulierung-erloesobergrenze-stel` | Anreizregulierung Erlösobergrenze: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-anreizregulierung-erloesobergrenze-unte` | Anreizregulierung Erlösobergrenze: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bbplg-leitungsvorhaben-fristen-und-besc` | BBPlG Leitungsvorhaben: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bbplg-leitungsvorhaben-rechtsmittel-che` | BBPlG Leitungsvorhaben: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bbplg-leitungsvorhaben-stellungnahme-en` | BBPlG Leitungsvorhaben: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bbplg-leitungsvorhaben-unterlagenanford` | BBPlG Leitungsvorhaben: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-gas-fristen-und-bescheidana` | Bilanzkreis Gas: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-gas-rechtsmittel-check` | Bilanzkreis Gas: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-gas-stellungnahme-entwurf` | Bilanzkreis Gas: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-gas-unterlagenanforderung` | Bilanzkreis Gas: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-strom-fristen-und-bescheida` | Bilanzkreis Strom: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-strom-rechtsmittel-check` | Bilanzkreis Strom: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-strom-stellungnahme-entwurf` | Bilanzkreis Strom: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-bilanzkreis-strom-unterlagenanforderung` | Bilanzkreis Strom: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-eeg-netzanschluss-einspeisemanagement-f` | EEG Netzanschluss Einspeisemanagement: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-eeg-netzanschluss-einspeisemanagement-r` | EEG Netzanschluss Einspeisemanagement: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-eeg-netzanschluss-einspeisemanagement-s` | EEG Netzanschluss Einspeisemanagement: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-eeg-netzanschluss-einspeisemanagement-u` | EEG Netzanschluss Einspeisemanagement: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-grosshandelsdaten-transparenz-fristen-u` | Großhandelsdaten Transparenz: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-grosshandelsdaten-transparenz-rechtsmit` | Großhandelsdaten Transparenz: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-grosshandelsdaten-transparenz-stellungn` | Großhandelsdaten Transparenz: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-grosshandelsdaten-transparenz-unterlage` | Großhandelsdaten Transparenz: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kapazitaetsvergabe-gas-fristen-und-besc` | Kapazitätsvergabe Gas: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kapazitaetsvergabe-gas-rechtsmittel-che` | Kapazitätsvergabe Gas: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kapazitaetsvergabe-gas-stellungnahme-en` | Kapazitätsvergabe Gas: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kapazitaetsvergabe-gas-unterlagenanford` | Kapazitätsvergabe Gas: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kwkg-zuschlaege-fristen-und-bescheidana` | KWKG Zuschläge: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kwkg-zuschlaege-rechtsmittel-check` | KWKG Zuschläge: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kwkg-zuschlaege-stellungnahme-entwurf` | KWKG Zuschläge: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-kwkg-zuschlaege-unterlagenanforderung` | KWKG Zuschläge: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-ladesaeulen-elektromobilitaet-fristen-u` | Ladesäulen Elektromobilität: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-ladesaeulen-elektromobilitaet-rechtsmit` | Ladesäulen Elektromobilität: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-ladesaeulen-elektromobilitaet-stellungn` | Ladesäulen Elektromobilität: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-ladesaeulen-elektromobilitaet-unterlage` | Ladesäulen Elektromobilität: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-fri` | Messstellenbetrieb MsbG Smart Meter: Fristen- und Bescheidanalyse für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-rec` | Messstellenbetrieb MsbG Smart Meter: Rechtsmittel-Check für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-ste` | Messstellenbetrieb MsbG Smart Meter: Stellungnahme-Entwurf für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |
| `energie-regulierungsakte-messstellenbetrieb-msbg-smart-meter-unt` | Messstellenbetrieb MsbG Smart Meter: Unterlagenanforderung für anwaltliche Arbeit mit BNetzA-Verfahren. Quellenanker: EnWG/ARegV/MsbG/NABEG. |

Weitere Skills: insgesamt 220 Anschluss-Skills in diesem Plugin.

<!-- END ACTUAL-SKILL-ROUTING -->
