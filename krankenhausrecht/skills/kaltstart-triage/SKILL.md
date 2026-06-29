---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Krankenhausrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor."
---

# Krankenhausrecht — Allgemein

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

## Sofortstart
Dieses Allgemein-Skill ist der Empfangstresen und Projektleiter des Plugins **Krankenhausrecht**. Es soll den Nutzer nicht belehren, sondern schnell arbeitsfähig machen: erst die Lage erfassen, dann den passenden Pfad wählen, dann direkt einen verwertbaren Output erzeugen.

**Plugin-Fokus:** Krankenhausrecht zwischen KHG, KHEntgG, SGB V, Landeskrankenhausrecht, G-BA-Vorgaben, Krankenhausreform, MD-Prüfung, Budgetverhandlung und Klinik-Compliance.

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
| `krankenhausfinanzierungsgesetz-khg-grundstruktur` | Krankenhausfinanzierungsgesetz KHG Grundstruktur |
| `landeskrankenhausplan-aufnahme-herausnahme-aenderung` | Landeskrankenhausplan Aufnahme Herausnahme Änderung |
| `planfeststellungsbescheid-rechtsbehelf-und-eilrechtsschutz` | Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz |
| `investitionsfoerderung-einzelfoerderung-pauschalfoerderung` | Investitionsförderung Einzelförderung Pauschalförderung |
| `khentgg-budgetverhandlung-drg-pepp-abgrenzung` | KHEntgG Budgetverhandlung DRG PEPP Abgrenzung |
| `pflegebudget-vereinbarung-nachweis-risiken` | Pflegebudget Vereinbarung Nachweis Risiken |
| `vorhalteverguetung-leistungsgruppen-krankenhausreform` | Vorhaltevergütung Leistungsgruppen Krankenhausreform |
| `leistungsgruppen-und-qualitaetskriterien-reformlogik` | Leistungsgruppen und Qualitätskriterien Reformlogik |
| `sektorenuebergreifende-versorgung-level-ii-klinik` | Sektorenübergreifende Versorgung Level Ii Klinik |
| `hybrid-drg-115f-sgb-v` | Hybrid-DRG § 115f SGB V |
| `ambulantes-operieren-115b-sgb-v` | Ambulantes Operieren § 115b SGB V |
| `entlassmanagement-39-abs-1a-sgb-v` | Entlassmanagement § 39 Abs. 1a SGB V |
| `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung` | MD-Prüfung Krankenhausabrechnung Prüfverfahrensvereinbarung |
| `strukturpruefung-ops-und-md` | Strukturprüfung OPS und MD |
| `mindestmengen-g-ba-qualitaetssicherung` | Mindestmengen G-BA Qualitätssicherung |
| `notfallstufen-und-sicherstellungszuschlaege` | Notfallstufen und Sicherstellungszuschläge |
| `zentren-zuschlaege-besondere-aufgaben` | Zentren Zuschläge besondere Aufgaben |
| `krankenhausapotheke-arzneimittelversorgung` | Krankenhausapotheke Arzneimittelversorgung |
| `krankenhaushygiene-ifsg-landesrecht` | Krankenhaushygiene IfSG Landesrecht |
| `medizinprodukterecht-betreiberpflichten-mdr-mpbetreibv` | Medizinprodukterecht Betreiberpflichten MDR MPBetreibV |
| `patientenrechte-behandlungsvertrag-aufklaerung` | Patientenrechte Behandlungsvertrag Aufklärung |
| `wahlleistungsvereinbarung-chefarzt-leistungskette` | Wahlleistungsvereinbarung Chefarzt Leistungskette |
| `belegarzt-honorar-und-krankenhausvertrag` | Belegarzt Honorar und Krankenhausvertrag |
| `datenschutz-krankenhaus-patientenakte-forschung` | Datenschutz Krankenhaus Patientenakte Forschung |
| `telemedizin-im-krankenhaus-und-fernbehandlung` | Telemedizin im Krankenhaus und Fernbehandlung |
| `krankenhaus-mvz-gruendung-zulassung-compliance` | Krankenhaus-MVZ Gründung Zulassung Compliance |
| `zuweiserverguetung-antikorruption-299a-299b-stgb` | Zuweiservergütung Antikorruption §§ 299a 299b StGB |
| `vergaberecht-krankenhaus-einkauf-bau-it` | Vergaberecht Krankenhaus Einkauf Bau IT |
| `personaluntergrenzen-pflege-ppugv` | Personaluntergrenzen Pflege PpUGV |
| `arbeitszeit-bereitschaftsdienst-rufdienst` | Arbeitszeit Bereitschaftsdienst Rufdienst |
| `rettungsdienst-schnittstelle-aufnahme-pflicht` | Rettungsdienst Schnittstelle Aufnahme Pflicht |
| `triage-notaufnahme-ueberlastung-dokumentation` | Triage Notaufnahme Überlastung Dokumentation |
| `psychiatrie-psychkg-unterbringung-fixierung` | Psychiatrie PsychKG Unterbringung Fixierung |
| `kinder-und-jugendmedizin-besondere-versorgung` | Kinder- und Jugendmedizin besondere Versorgung |
| `geburtshilfe-haftung-hebammen-schnittstelle` | Geburtshilfe Haftung Hebammen Schnittstelle |

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `ambulantes-operieren-115b-sgb-v` | Ambulantes Operieren § 115b SGB V: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlin... |
| `arbeitszeit-bereitschaftsdienst-rufdienst` | Arbeitszeit Bereitschaftsdienst Rufdienst: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-... |
| `barrierefreiheit-krankenhauskommunikation` | Barrierefreiheit Krankenhauskommunikation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-... |
| `belegarzt-honorar-und-krankenhausvertrag` | Belegarzt Honorar und Krankenhausvertrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-R... |
| `blutprodukte-transfusionsrecht-dokumentation` | Blutprodukte Transfusionsrecht Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-... |
| `compliance-system-klinik-einkauf-forschung-spenden` | Compliance-System Klinik Einkauf Forschung Spenden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformsta... |
| `datenschutz-krankenhaus-patientenakte-forschung` | Datenschutz Krankenhaus Patientenakte Forschung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand,... |
| `dokumentation-aufbewahrung-beweislast` | Dokumentation Aufbewahrung Beweislast: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Rich... |
| `dora-und-it-dienstleister-soweit-einschlaegig` | DORA und IT-Dienstleister soweit einschlägig: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-... |
| `entlassmanagement-39-abs-1a-sgb-v` | Entlassmanagement § 39 Abs. 1a SGB V: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richt... |
| `forschung-studien-ethikkommission-datenschutz` | Forschung Studien Ethikkommission Datenschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `fristen-planung-budget-md-schiedsstelle` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fristen Planung Budget MD Schiedsstelle. |
| `geburtshilfe-haftung-hebammen-schnittstelle` | Geburtshilfe Haftung Hebammen Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-B... |
| `gewaltschutz-sicherheitsdienst-hausverbot` | Gewaltschutz Sicherheitsdienst Hausverbot: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-... |
| `haftpflichtfall-krankenhaus-gutachtenstrategie` | Haftpflichtfall Krankenhaus Gutachtenstrategie: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand,... |
| `hybrid-drg-115f-sgb-v` | Hybrid-DRG § 115f SGB V: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, Lande... |
| `insolvenz-eines-krankenhauses-versorgungssicherung` | Insolvenz eines Krankenhauses Versorgungssicherung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformsta... |
| `intensivmedizin-beatmung-verlegung` | Intensivmedizin Beatmung Verlegung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtli... |
| `investitionsfoerderung-einzelfoerderung-pauschalfoerderung` | Investitionsförderung Einzelförderung Pauschalförderung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Refo... |
| `kaltstart-krankenhausrecht` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart Krankenhausrecht. |
| `khentgg-budgetverhandlung-drg-pepp-abgrenzung` | KHEntgG Budgetverhandlung DRG PEPP Abgrenzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `kinder-und-jugendmedizin-besondere-versorgung` | Kinder- und Jugendmedizin besondere Versorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand,... |
| `klage-gegen-budgetbescheid-oder-schiedsstellenentscheidung` | Klage gegen Budgetbescheid oder Schiedsstellenentscheidung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/R... |
| `klinikakten-und-bescheide-sortieren` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Klinikakten und Bescheide sortieren. |
| `klinikverbund-fusion-kartell-vergabe-planungsrecht` | Klinikverbund Fusion Kartell Vergabe Planungsrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformsta... |
| `kommunale-klinik-beihilfe-und-eu-beihilfen` | Kommunale Klinik Beihilfe und EU-Beihilfen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA... |
| `krankenhaus-mvz-gruendung-zulassung-compliance` | Krankenhaus-MVZ Gründung Zulassung Compliance: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `krankenhausapotheke-arzneimittelversorgung` | Krankenhausapotheke Arzneimittelversorgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA... |
| `krankenhausdigitalisierung-khzg-it-sicherheit` | Krankenhausdigitalisierung KHZG IT-Sicherheit: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `krankenhausfinanzierungsgesetz-khg-grundstruktur` | Krankenhausfinanzierungsgesetz KHG Grundstruktur: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand... |
| `krankenhaushygiene-ifsg-landesrecht` | Krankenhaushygiene IfSG Landesrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtl... |
| `krankenhausreform-leistungsgruppen-routing` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Krankenhausreform Leistungsgruppen Routing. |
| `krankenhausseelsorge-besuchsrecht-hausrecht` | Krankenhausseelsorge Besuchsrecht Hausrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-B... |
| `kritis-krankenhaus-bsi-gesetz-nis2` | KRITIS Krankenhaus BSI-Gesetz NIS2: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtli... |
| `landesaufsicht-krankenhausaufsicht-beanstandung` | Landesaufsicht Krankenhausaufsicht Beanstandung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand,... |
| `landeskrankenhausplan-aufnahme-herausnahme-aenderung` | Landeskrankenhausplan Aufnahme Herausnahme Änderung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformst... |
| `landesrecht-und-bundesrecht-trennen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Landesrecht und Bundesrecht trennen. |
| `leistungsgruppen-und-qualitaetskriterien-reformlogik` | Leistungsgruppen und Qualitätskriterien Reformlogik: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformst... |
| `livequellen-g-ba-bmg-land-pruefen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livequellen G-BA BMG Land prüfen. |
| `md-pruefung-krankenhausabrechnung-pruefverfahrensvereinbarung` | MD-Prüfung Krankenhausabrechnung Prüfverfahrensvereinbarung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/... |
| `medizinprodukterecht-betreiberpflichten-mdr-mpbetreibv` | Medizinprodukterecht Betreiberpflichten MDR MPBetreibV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Refor... |
| `mindestmengen-g-ba-qualitaetssicherung` | Mindestmengen G-BA Qualitätssicherung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Rich... |
| `notfallstufen-und-sicherstellungszuschlaege` | Notfallstufen und Sicherstellungszuschläge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA... |
| `output-vorstandsvorlage-behoerdenbrief-klage` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Output Vorstandsvorlage Behördenbrief Klage. |
| `patientenbeschwerde-und-risikomanagement` | Patientenbeschwerde und Risikomanagement: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-R... |
| `patientenrechte-behandlungsvertrag-aufklaerung` | Patientenrechte Behandlungsvertrag Aufklärung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `personaluntergrenzen-pflege-ppugv` | Personaluntergrenzen Pflege PpUGV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlin... |
| `pflegebudget-vereinbarung-nachweis-risiken` | Pflegebudget Vereinbarung Nachweis Risiken: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA... |
| `planfeststellungsbescheid-rechtsbehelf-und-eilrechtsschutz` | Planfeststellungsbescheid Rechtsbehelf und Eilrechtsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/R... |
| `privatisierung-betriebsuebergang-traegerwechsel` | Privatisierung Betriebsübergang Trägerwechsel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `psychiatrie-psychkg-unterbringung-fixierung` | Psychiatrie PsychKG Unterbringung Fixierung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-B... |
| `qualitaets-und-strukturvorgaben-intake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Qualitäts- und Strukturvorgaben Intake. |
| `qualitaetsbericht-veroeffentlichungspflichten` | Qualitätsbericht Veröffentlichungspflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-B... |
| `rettungsdienst-schnittstelle-aufnahme-pflicht` | Rettungsdienst Schnittstelle Aufnahme Pflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `schiedsstellenverfahren-krankenhausentgelt` | Schiedsstellenverfahren Krankenhausentgelt: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA... |
| `sektorenuebergreifende-versorgung-level-ii-klinik` | Sektorenübergreifende Versorgung Level Ii Klinik: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand... |
| `strahlenschutz-radiologie-nuklearmedizin` | Strahlenschutz Radiologie Nuklearmedizin: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-R... |
| `strukturpruefung-ops-und-md` | Strukturprüfung OPS und MD: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtlinien, La... |
| `telemedizin-im-krankenhaus-und-fernbehandlung` | Telemedizin im Krankenhaus und Fernbehandlung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G... |
| `transplantationsrecht-koordination` | Transplantationsrecht Koordination: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richtli... |
| `triage-notaufnahme-ueberlastung-dokumentation` | Triage Notaufnahme Überlastung Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-... |
| `vergaberecht-krankenhaus-einkauf-bau-it` | Vergaberecht Krankenhaus Einkauf Bau IT: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Ri... |
| `vorhalteverguetung-leistungsgruppen-krankenhausreform` | Vorhaltevergütung Leistungsgruppen Krankenhausreform: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reforms... |
| `wahlleistungsvereinbarung-chefarzt-leistungskette` | Wahlleistungsvereinbarung Chefarzt Leistungskette: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstan... |
| `zentren-zuschlaege-besondere-aufgaben` | Zentren Zuschläge besondere Aufgaben: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformstand, G-BA-Richt... |
| `zuweiserverguetung-antikorruption-299a-299b-stgb` | Zuweiservergütung Antikorruption §§ 299a 299b StGB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: KHG, KHEntgG, BPflV, SGB V, KHVVG/Reformsta... |

<!-- END ACTUAL-SKILL-ROUTING -->

## Normen & Rechtsprechung

Konkret zu prüfen:

- §§ 1-23 KHG (Krankenhausfinanzierung)
- §§ 107-114 SGB V (Krankenhaus)
- KHEntgG (Entgeltgesetz)
- §§ 17a-17d KHG (DRG, Pflege, Investitionen)
