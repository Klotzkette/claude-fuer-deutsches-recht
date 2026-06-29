---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Apothekenrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Fachmodule aus diesem Plugin vor."
---

# Apothekenrecht — Allgemein

## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Sofortstart
Dieses Allgemein-Skill ist der Empfangstresen und Projektleiter des Plugins **Apothekenrecht**. Es soll den Nutzer nicht belehren, sondern schnell arbeitsfähig machen: erst die Lage erfassen, dann den passenden Pfad wählen, dann direkt einen verwertbaren Output erzeugen.

**Plugin-Fokus:** Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

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
| `apothekenerlaubnis-apog-persönliche-voraussetzungen` | Apothekenerlaubnis ApoG persönliche Voraussetzungen |
| `fremd-und-mehrbesitzverbot-apothekenrecht` | Fremd- und Mehrbesitzverbot Apothekenrecht |
| `filialapotheke-hauptapotheke-leitung-vertretung` | Filialapotheke Hauptapotheke Leitung Vertretung |
| `apothekenbetriebsordnung-grundpflichten` | Apothekenbetriebsordnung Grundpflichten |
| `raeume-ausstattung-rezeptur-defektur-labor` | Räume Ausstattung Rezeptur Defektur Labor |
| `personal-pharmazeutisch-nichtpharmazeutisch-vertretung` | Personal pharmazeutisch nichtpharmazeutisch Vertretung |
| `dienstbereitschaft-notdienst-schliessung` | Dienstbereitschaft Notdienst Schließung |
| `rezeptsammelstelle-botendienst-versandhandel` | Rezeptsammelstelle Botendienst Versandhandel |
| `versandhandelserlaubnis-eu-versandapotheke` | Versandhandelserlaubnis EU Versandapotheke |
| `e-rezept-ti-gematik-apothekenprozess` | E-Rezept TI Gematik Apothekenprozess |
| `arzneimittelabgabe-verschreibungspflicht` | Arzneimittelabgabe Verschreibungspflicht |
| `substitution-rabattvertrag-aut-idem` | Substitution Rabattvertrag Aut-idem |
| `btm-rezept-betaeubungsmittel-dokumentation` | BtM-Rezept Betäubungsmittel Dokumentation |
| `t-rezept-besondere-arzneimittel` | T-Rezept besondere Arzneimittel |
| `rezeptur-plausibilitaetspruefung-herstellungsanweisung` | Rezeptur Plausibilitätsprüfung Herstellungsanweisung |
| `defektur-100er-regel-qualitaetssicherung` | Defektur 100er-Regel Qualitätssicherung |
| `arzneimittelpruefung-ausgangsstoffe-pruefprotokoll` | Arzneimittelprüfung Ausgangsstoffe Prüfprotokoll |
| `kuehlkette-temperaturmonitoring-gdp` | Kühlkette Temperaturmonitoring GDP |
| `arzneimittelrisiken-rueckruf-chargenrueckverfolgung` | Arzneimittelrisiken Rückruf Chargenrückverfolgung |
| `apothekenuebliche-waren-abgrenzung` | Apothekenübliche Waren Abgrenzung |
| `impfleistungen-in-apotheken` | Impfleistungen in Apotheken |
| `pharmazeutische-dienstleistungen-verguetung` | Pharmazeutische Dienstleistungen Vergütung |
| `amts-medikationsanalyse-beratungspflicht` | AMTS Medikationsanalyse Beratungspflicht |
| `datenschutz-in-apotheke-gesundheitsdaten` | Datenschutz in Apotheke Gesundheitsdaten |
| `schweigepflicht-berufsrecht-pta-approbation` | Schweigepflicht Berufsrecht PTA Approbation |
| `preisbindung-arzneimittel-ampreisv` | Preisbindung Arzneimittel AMPreisV |
| `skonti-boni-rabatte-zuweisungsverbot` | Skonti Boni Rabatte Zuweisungsverbot |
| `kooperation-arzt-apotheke-antikorruption` | Kooperation Arzt Apotheke Antikorruption |
| `heimversorgung-versorgungsvertrag` | Heimversorgung Versorgungsvertrag |
| `krankenhausversorgung-krankenhausapotheke` | Krankenhausversorgung Krankenhausapotheke |
| `blutprodukte-haemophilie-registerpflicht` | Blutprodukte Hämophilie Registerpflicht |
| `tierarzneimittel-apothekenabgabe-versand-ab-2026` | Tierarzneimittel Apothekenabgabe Versand ab 2026 |
| `cannabis-medizinalcannabis-abgabe-dokumentation` | Cannabis Medizinalcannabis Abgabe Dokumentation |
| `import-einzelimport-73-amg` | Import Einzelimport § 73 AMG |
| `gefahrstoffe-chemikalien-ausgangsstoffe` | Gefahrstoffe Chemikalien Ausgangsstoffe |

## Aktuelle Anschluss-Skills

Diese Tabelle wird aus dem tatsächlichen Skillbestand des Plugins gebildet. Wenn ein Nutzer nach dem Einstieg weitergeleitet werden soll, nimm bevorzugt diese Namen.

| Skill | Wann einsetzen? |
| --- | --- |
| `amts-medikationsanalyse-beratungspflicht` | AMTS Medikationsanalyse Beratungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `apothekenbetrieb-dokumentenintake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Apothekenbetrieb Dokumentenintake. |
| `apothekenbetriebsordnung-grundpflichten` | Apothekenbetriebsordnung Grundpflichten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `apothekenerlaubnis-apog-persönliche-voraussetzungen` | Apothekenerlaubnis ApoG persönliche Voraussetzungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/Bt... |
| `apothekenrevision-vorbereitung-antwort` | Apothekenrevision Vorbereitung Antwort: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, D... |
| `apothekenuebliche-waren-abgrenzung` | Apothekenübliche Waren Abgrenzung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO,... |
| `arzneimittelabgabe-verschreibungspflicht` | Arzneimittelabgabe Verschreibungspflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `arzneimittelpruefung-ausgangsstoffe-pruefprotokoll` | Arzneimittelprüfung Ausgangsstoffe Prüfprotokoll: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV... |
| `arzneimittelrisiken-rueckruf-chargenrueckverfolgung` | Arzneimittelrisiken Rückruf Chargenrückverfolgung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMV... |
| `aufsicht-anhoerung-ordnungswidrigkeit` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Aufsicht Anhörung Ordnungswidrigkeit. |
| `beanstandung-durch-aufsichtsbehoerde-anhoerung` | Beanstandung durch Aufsichtsbehörde Anhörung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SG... |
| `beschwerdemanagement-patient-kunden` | Beschwerdemanagement Patient Kunden: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGV... |
| `blutprodukte-haemophilie-registerpflicht` | Blutprodukte Hämophilie Registerpflicht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `btm-rezept-betaeubungsmittel-dokumentation` | BtM-Rezept Betäubungsmittel Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V... |
| `btm-rezeptur-amts-schnellcheck` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema BtM Rezeptur AMTS Schnellcheck. |
| `cannabis-medizinalcannabis-abgabe-dokumentation` | Cannabis Medizinalcannabis Abgabe Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV,... |
| `compliance-audit-apothekenverbund` | Compliance-Audit Apothekenverbund: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO,... |
| `datenschutz-in-apotheke-gesundheitsdaten` | Datenschutz in Apotheke Gesundheitsdaten: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `defektur-100er-regel-qualitaetssicherung` | Defektur 100er-Regel Qualitätssicherung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `dienstbereitschaft-notdienst-schliessung` | Dienstbereitschaft Notdienst Schließung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `digitale-plattformen-marktplatz-apothekenrecht` | Digitale Plattformen Marktplatz Apothekenrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV,... |
| `e-rezept-ti-gematik-apothekenprozess` | E-Rezept TI Gematik Apothekenprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSG... |
| `erlaubnis-filialverbund-routing` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Erlaubnis Filialverbund Routing. |
| `filialapotheke-hauptapotheke-leitung-vertretung` | Filialapotheke Hauptapotheke Leitung Vertretung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV,... |
| `fremd-und-mehrbesitzverbot-apothekenrecht` | Fremd- und Mehrbesitzverbot Apothekenrecht: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB... |
| `gefahrstoffe-chemikalien-ausgangsstoffe` | Gefahrstoffe Chemikalien Ausgangsstoffe: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `heimversorgung-versorgungsvertrag` | Heimversorgung Versorgungsvertrag: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO,... |
| `hygiene-pandemie-infektionsschutz` | Hygiene Pandemie Infektionsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO,... |
| `impfleistungen-in-apotheken` | Impfleistungen in Apotheken: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rez... |
| `import-einzelimport-73-amg` | Import Einzelimport § 73 AMG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Re... |
| `inhaberwechsel-kauf-apothekenbetrieb` | Inhaberwechsel Kauf Apothekenbetrieb: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSG... |
| `kaltstart-apothekenrecht` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart Apothekenrecht. |
| `kooperation-arzt-apotheke-antikorruption` | Kooperation Arzt Apotheke Antikorruption: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V,... |
| `krankenhausversorgung-krankenhausapotheke` | Krankenhausversorgung Krankenhausapotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V... |
| `kuehlkette-temperaturmonitoring-gdp` | Kühlkette Temperaturmonitoring GDP: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO... |
| `lieferengpaesse-austausch-dokumentation` | Lieferengpässe Austausch Dokumentation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, D... |
| `livecheck-apog-apbetro-amg` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Livecheck ApoG ApBetrO AMG. |
| `mietvertrag-apothekenstandort-konkurrenzschutz` | Mietvertrag Apothekenstandort Konkurrenzschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV,... |
| `notfallkontrazeption-beratung` | Notfallkontrazeption Beratung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-R... |
| `onlinewerbung-hwg-apotheken` | Onlinewerbung HWG Apotheken: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rez... |
| `output-behoerdenbrief-sop-mandantenmemo` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Output Behördenbrief SOP Mandantenmemo. |
| `owi-strafrisiken-apog-amg-btmg` | OWi Strafrisiken ApoG AMG BtMG: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-... |
| `personal-pharmazeutisch-nichtpharmazeutisch-vertretung` | Personal pharmazeutisch nichtpharmazeutisch Vertretung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG... |
| `pharmazeutische-dienstleistungen-verguetung` | Pharmazeutische Dienstleistungen Vergütung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB... |
| `preisangaben-e-commerce-apotheke` | Preisangaben E-Commerce Apotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO,... |
| `preisbindung-arzneimittel-ampreisv` | Preisbindung Arzneimittel AMPreisV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO... |
| `qualitaetsmanagement-qms-sops` | Qualitätsmanagement QMS SOPs: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Re... |
| `raeume-ausstattung-rezeptur-defektur-labor` | Räume Ausstattung Rezeptur Defektur Labor: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V... |
| `rechnung-retaxation-krankenkasse` | Rechnung Retaxation Krankenkasse: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO,... |
| `retaxationsabwehr-nullretax-risiko` | Retaxationsabwehr Nullretax Risiko: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO... |
| `rezeptsammelstelle-botendienst-versandhandel` | Rezeptsammelstelle Botendienst Versandhandel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SG... |
| `rezeptur-plausibilitaetspruefung-herstellungsanweisung` | Rezeptur Plausibilitätsprüfung Herstellungsanweisung: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/B... |
| `schiedsstellen-krankenkassen-apotheke` | Schiedsstellen Krankenkassen Apotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DS... |
| `schweigepflicht-berufsrecht-pta-approbation` | Schweigepflicht Berufsrecht PTA Approbation: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB... |
| `securpharm-faelschungsschutz` | Securpharm Fälschungsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rez... |
| `skonti-boni-rabatte-zuweisungsverbot` | Skonti Boni Rabatte Zuweisungsverbot: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSG... |
| `substitution-rabattvertrag-aut-idem` | Substitution Rabattvertrag Aut-idem: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGV... |
| `t-rezept-besondere-arzneimittel` | T-Rezept besondere Arzneimittel: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E... |
| `telepharmazie-grenzen-chancen` | Telepharmazie Grenzen Chancen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-R... |
| `tierarzneimittel-apothekenabgabe-versand-ab-2026` | Tierarzneimittel Apothekenabgabe Versand ab 2026: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV... |
| `versandhandel-und-e-rezept-intake` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Versandhandel und E-Rezept Intake. |
| `versandhandelserlaubnis-eu-versandapotheke` | Versandhandelserlaubnis EU Versandapotheke: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB... |
| `versorgung-pflegeheim-schnittstelle` | Versorgung Pflegeheim Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGV... |
| `widerruf-ruecknahme-ruhen-apothekenerlaubnis` | Widerruf Rücknahme Ruhen Apothekenerlaubnis: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB... |

<!-- END ACTUAL-SKILL-ROUTING -->
