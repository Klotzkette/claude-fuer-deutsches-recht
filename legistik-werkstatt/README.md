# Legistik-Werkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`legistik-werkstatt`) | [`legistik-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Elektronisches Pflichtpostfach** (`legistik-pflichtpostfach`) | [Gesamt-PDF lesen](../testakten/legistik-pflichtpostfach/gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) | [`testakte-legistik-pflichtpostfach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Elektronisches Pflichtpostfach** (`legistik-pflichtpostfach`) | [Gesamt-PDF lesen](../testakten/legistik-pflichtpostfach/gesamt-pdf/legistik-pflichtpostfach_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Vollständige Werkstatt für Legistinnen und Legisten in Bundesministerien, Bundestag, Fraktionen, Oppositionsarbeit, Landesministerien, Landtagen sowie kommunalen und kammerlichen Normgebern. Vom politischen Auftrag über Startbahn, Normhierarchie, Kompetenzprüfung, Normenkartierung und Terminologie zu Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Rechtsverordnung und Satzung. Mit Querschnittsprüfungen Verfassungsrecht Europarecht Folgenabschätzung Goldplating Bestimmtheit Zirkelschluss. Erzeugt am Ende ein DOCX und PDF im passenden offiziellen Layout - ministerieller Referentenentwurf-Stil, BT-/Landtagsdrucksachen-Stil oder Arbeitsfassung für Fraktion, Ausschuss und Normgeber.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Legistik-Werkstatt (`legistik-werkstatt`, dieses Plugin) | [legistik-werkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **- Elektronisches Pflichtpostfach** ([`testakten/legistik-pflichtpostfach/`](../testakten/legistik-pflichtpostfach/)).

Direkt-Download als ZIP: [testakte-legistik-pflichtpostfach.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Was kann das Plugin?

Das Plugin deckt **alle Normebenen** ab:

- Bundesgesetz (Stammgesetz, Mantelgesetz, Änderungsgesetz)
- Landesgesetz
- Rechtsverordnung des Bundes und der Länder (Art. 80 GG, Landesverfassungen)
- Satzungen von Kommunen, Kammern und Hochschulen (Art. 28 Abs. 2 GG, Selbstverwaltung)
- Sekundärrechtsdurchführung und Notifizierung
- parlamentarischer Antrag, Entschließungsantrag, Änderungsantrag und Gesetzentwurf aus der Mitte des Bundestages oder Landtages

Das Plugin arbeitet mit **fünf Startbahnen**:

- Bundesressort / Bundesregierung: Referentenentwurf, Ressortabstimmung, NKR, Kabinett, Bundesrat, Bundestag
- Bundestag / Fraktion / Abgeordnete: Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Entschließungsantrag, Ausschussfassung
- Landesressort / Landesregierung: Landesreferentenentwurf, Landesverordnung, Kabinetts- und Landtagsweg
- Landtag / Landtagsfraktion: landesspezifischer Gesetzentwurf, Änderungsantrag, Antrag, Entschließungsantrag
- sonstiger Normgeber: kommunale Satzung, Kammerrecht, Hochschulsatzung, Beschlussvorlage, Bekanntmachung

Das Plugin prüft **immer**:

- Verfassungsrecht (GG, Landesverfassungen, BVerfG-Rechtsprechung)
- Europarecht (Primärrecht, Sekundärrecht, Notifizierung 2015/1535)
- Folgen (Erfüllungsaufwand, Bürokratiekosten, Nachhaltigkeit, KMU-Test)
- Goldplating und Wesentlichkeit
- Bestimmtheit, Terminologie und Zirkelschluss

Am Ende erzeugt es ein **lieferfertiges DOCX und PDF** im offiziellen Layout:

- **Referentenentwurf** (Arial 11pt, Bearbeitungsstand-Kopf, A-F-Vorblatt)
- **BT-Drucksache** (Times New Roman 11pt, Drucksachennummer + Wahlperiode in der Kopfzeile, Sperrsatz für Hauptüberschriften, Anschreiben des Bundeskanzlers)
- **Formulierungshilfe / parlamentarische Vorlage** (für Koalition, Opposition, Ausschuss oder Ministerialzulieferung)
- **Antrag / Entschließungsantrag** (beschlussreif, mit Begründung und Kurzvermerk)
- **Synopse** (dreispaltig)
- **Lesefassung** (konsolidiert nach Inkrafttreten)
- **Kabinettsmappe** (Deckblatt + Anlagenverzeichnis)

## Skill-Tabelle

| Phase | Skill | Zweck |
| --- | --- | --- |
| Auftrag | `legistik-auftragsaufnahme` | Startbahn, Institution, formalen Initiator und Regelungsauftrag übersetzen |
| Normhierarchie | `normhierarchie-routing` | Regierung vs Parlament; Gesetz vs Verordnung vs Satzung vs Antrag; Bund vs Land |
| Kompetenz | `gesetzgebungskompetenz-pruefen` | Art. 70 bis 74 GG, Erforderlichkeit |
| Kompetenz | `verordnungsermaechtigung-art80` | Inhalt Zweck Ausmass nach Art. 80 GG |
| Kompetenz | `satzungskompetenz-pruefen` | Art. 28 Abs. 2 GG, Kammern, Hochschulen |
| Mapping | `normenkartierung` | Verweisnetz und Änderungsstellen |
| Sprache | `terminologie-konsistenz` | Begriffsbrüche aufspüren |
| Sprache | `zirkelschluss-pruefen` | Verweisgraf zykelfrei |
| Entwurf | `referentenentwurf-bauen` | Vollformat des Bundes- oder Landes-Referentenentwurfs |
| Entwurf | `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Antrag oder Entschließungsantrag |
| Entwurf | `gesetzesentwurf-kabinett` | Kabinettsmappe |
| Entwurf | `begruendung-allgemein-und-besonders` | Teil A I-VII und Teil B |
| Entwurf | `synopse-erstellen` | Dreispaltige Synopse |
| Entwurf | `lesefassung-konsolidiert` | Konsolidierte Fassung nach Inkrafttreten |
| Entwurf | `xml-paralleldarstellung` | LegalDocML.de und eNorm |
| Prüfung | `europarechtskonformitaet` | Primärrecht Sekundärrecht Notifizierung |
| Prüfung | `goldplating-vermeiden` | Überschießende Umsetzung von Unionsrecht |
| Prüfung | `verfassungsmaessigkeit-quercheck` | Grundrechte Verhältnismäßigkeit Bestimmtheit |
| Folgen | `folgenabschaetzung-erfuellungsaufwand` | Erfüllungsaufwand quantifizieren |
| Folgen | `folgenabschaetzung-nachhaltigkeit` | SDGs Klima Generationengerechtigkeit |
| Inkrafttreten | `inkrafttreten-uebergangsrecht` | Zeitpunkt Übergang Verkündung |
| Beteiligung | `verbaendeanhoerung-ressortabstimmung` | Anhörung und Abstimmung |
| Beteiligung | `normenkontrollrat-kmu-check` | NKR-Stellungnahme einholen |
| Lieferung | `dokumente-rendern-docx-pdf` | DOCX und PDF im offiziellen Layout |
| Schulung | `schulung-legistik` | Trainerleitfaden für Schulungen |

Insgesamt **26 Skills**.

## Beispielprojekt - Pflichtpostfachgesetz

Das Repository enthält eine vollständige Arbeitsakte unter `testakten/legistik-pflichtpostfach/`. Sie simuliert den Weg von der politischen Vorgabe (Koalitionsvertrag) zum lieferfertigen Referentenentwurf eines neuen Stammgesetzes über das elektronische Pflichtpostfach für HReg-Gesellschaften und sehr große Online-Plattformen.

So erzeugen Sie die fertigen Dokumente:

```bash
cd claude-fuer-deutsches-recht
python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output

python3 legistik-werkstatt/skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format bt-drucksache \
  --eingabe testakten/legistik-pflichtpostfach/eingang \
  --ausgabe testakten/legistik-pflichtpostfach/output
```

Voraussetzung: `pip install python-docx pyyaml`. Für die PDF-Konvertierung zusätzlich LibreOffice (`soffice`).

## Disclaimer

Dieses Plugin ist ein Werkzeug zur Beschleunigung legistischer Arbeit. Es ersetzt nicht die juristische Prüfung durch verantwortliche Fachreferentinnen und Fachreferenten und nicht die Prüfung durch die Ressortleitung und das Bundesministerium der Justiz im Rahmen der Rechtsförmlichkeitsprüfung.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 177 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Legistik Werkstatt-Plugin für Bundesministerien, Bundestag, Fraktionen, Landesministerien, Landtage und sonstige Normgeber. Fragt Startbahn, Institution, Bundesland, Ressort, Fraktion, Verf... |
| `begruendung-allgemein-und-besonders` | Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil A Anlass und Ziel B... |
| `dokumente-rendern-docx-pdf` | Legistische Dokumente als DOCX oder PDF im offiziellen Erscheinungsbild der Bundesregierung, des Bundestages, eines Landes oder eines Landtags rendern. Anwendungsfall fertiger Entwurf soll als lieferfähiges Dokument nach Handbuch der Rec... |
| `europarechtskonformitaet` | Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht EUV AEUV Grundrechtec... |
| `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik Leitfaden BMJ BMI Statistis... |
| `folgenabschaetzung-nachhaltigkeit` | Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen Bewertung positiv ne... |
| `formulierungshilfe-bauen` | Formulierungshilfen, Aenderungsantraege, Gesetzentwuerfe aus der Mitte des Bundestages oder Landtages, Entschliessungsantraege und parlamentarische Antraege bauen. Anwendungsfall Bundesministerium liefert fachlich zu, Koalitionsfraktion... |
| `gesetzesentwurf-kabinett` | Kabinettsentwurf der Bundesregierung oder Landesregierung aus dem Referentenentwurf nach Ressortabstimmung erstellen. Anwendungsfall Ressortabstimmung und Verbandeanhoerung sind abgeschlossen Kabinettsvorlage muss fertiggestellt werden.... |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73 GG. Konkurrierende Ko... |
| `goldplating-vermeiden` | Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten. Anwendungsfall Referentenentwurf setzt EU-Richtlinie um und muss auf ueberschiessende nationale Regelungen über den Richtlinien-Mindeststandard hinaus geprü... |
| `inkrafttreten-uebergangsrecht` | Inkrafttretens- und Übergangsregelung für Gesetze und Verordnungen formulieren. Anwendungsfall Entwurf ist inhaltlich fertig Artikel Inkrafttreten und Übergangsrecht muessen noch ergaenzt werden. Standardformel Stichtagsregelung Altfaell... |
| `legistik-auftragsaufnahme` | Legistischen Auftrag strukturiert aufnehmen und in operationale Regelungsziele umwandeln. Anwendungsfall Erstkontakt zu einem neuen Vorhaben aus Bundesministerium, Bundestag, Fraktion, Landesministerium, Landtag, Kommune, Kammer oder Hoc... |
| `legw-aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension` | Sachbereich Ausfuhrkontrolle und Aussenwirtschaftsdimension im Geschaeftsbereich AA: Normbestand (AWG; AWV; KrWaffKG; Dual-Use-VO (EU); Sanktions-VO.); Akteure (BAFA; AA Politische Abteilung; BMWE.); EU-Bezug (Wassenaar; MTCR; NSG; Austr... |
| `legw-aa-eu-grundlagen-und-ratsverfahren` | Sachbereich EU-Grundlagen und Ratsverfahren im Geschaeftsbereich AA: Normbestand (EUV; AEUV; EUZBLG; EUZBBG; Lissabon-Begleitgesetzgebung.); Akteure (AA Europa-Abteilung; Bundeskanzleramt EU-Koordinator; Bundesministerien.); EU-Bezug (Ra... |
| `legw-aa-konsular-und-passrecht` | Sachbereich Konsularrecht und Passrecht im Geschaeftsbereich AA: Normbestand (KonsG; PassG; PAuswG; EWG-VO 1683/95 (Visa).); Akteure (Auslandsvertretungen; Bundesverwaltungsamt; BAMF (Visa).); EU-Bezug (Visa-Kodex; Schengen; ETIAS.); typ... |
| `legw-aa-sanktionsumsetzung-und-internationale-abkommen` | Sachbereich Sanktionsumsetzung und internationale Abkommen im Geschaeftsbereich AA: Normbestand (AWG; SanktDG; UN-Sicherheitsrat-Resolutionen; BGBl II.); Akteure (AA; BMWE-BAFA; BMF-Zoll; FIU; BaFin.); EU-Bezug (EU-Sanktionsregime gegen... |
| `legw-aa-voelkerrecht-und-vertragsgesetzgebung` | Sachbereich Voelkerrecht und Vertragsgesetzgebung im Geschaeftsbereich AA: Normbestand (GG Art. 32 und Art. 59; WVK; Vertragsgesetze; Ratifikationsgesetze; BGBl Teil II.); Akteure (AA Rechtsabteilung; Bundespraesidialamt; Bundestag; Bund... |
| `legw-bmas-arbeitsrecht-und-arbeitsschutz` | Sachbereich Arbeitsrecht und Arbeitsschutz im Geschaeftsbereich BMAS: Normbestand (BGB-Arbeitsrecht; KSchG; TzBfG; ArbZG; ArbSchG; BetrVG; SprAuG; MiLoG.); Akteure (BMAS; BAuA; ArbGericht; LAG; BAG; Arbeitsschutzbehoerden der Laender.);... |
| `legw-bmas-arbeitsschutz-und-arbeitssicherheit` | Sachbereich Arbeitsschutz und Arbeitssicherheit im Geschaeftsbereich BMAS: Normbestand (ArbSchG; ArbStaettV; BetrSichV; BiostoffV; LasthandhabV; PSA-BV; ArbMedVV.); Akteure (BAuA; UVT (Berufsgenossenschaften); Laender-Arbeitsschutzbehoer... |
| `legw-bmas-rente-und-altersvorsorgerecht` | Sachbereich Rente und Altersvorsorgerecht im Geschaeftsbereich BMAS: Normbestand (SGB VI; AVG (alt); FRG; ZRBG; Riester; Foerderhinweise Steuer (mit BMF).); Akteure (DRV Bund; Aufsicht ueber Pensionsfonds (BaFin Schnittstelle); ZfA (Zula... |
| `legw-bmas-sozialversicherungsrecht-sgb` | Sachbereich Sozialversicherungsrecht (SGB) im Geschaeftsbereich BMAS: Normbestand (SGB I bis SGB XII; ASVG-Aequivalent; AsylbLG (mit BMI).); Akteure (DRV Bund; BA; GKV-Spitzenverband; BAS (Bundesamt fuer Soziale Sicherung); SGericht.); E... |
| `legw-bmas-teilhabe-und-schwerbehindertenrecht-sgb-ix` | Sachbereich Teilhaberecht (SGB IX) im Geschaeftsbereich BMAS: Normbestand (SGB IX; SchwbAV; BTHG; SGB XII; AGG.); Akteure (Integrationsaemter; Reha-Traeger; Bundesagentur fuer Arbeit; Sozialgerichte.); EU-Bezug (UN-BRK; EU-Beschaeftigung... |
| `legw-bmbfsfj-familien-und-elterngeldrecht` | Sachbereich Familien- und Elterngeldrecht im Geschaeftsbereich BMBFSFJ: Normbestand (BEEG; BKGG; UnterhVG; FamFG (familienverfahrensrechtlich); MuSchG.); Akteure (Elterngeldstellen der Laender; BMBFSFJ; Familiengerichte.); EU-Bezug (Work... |
| `legw-bmbfsfj-gleichstellungs-und-antidiskriminierungsrecht` | Sachbereich Gleichstellungs- und Antidiskriminierungsrecht im Geschaeftsbereich BMBFSFJ: Normbestand (AGG; BGleiG; LGleiG; Lohngerechtigkeitsgesetz (EntgTranspG); StaatszielG GG Art. 3.); Akteure (Antidiskriminierungsstelle des Bundes; G... |
| `legw-bmbfsfj-kinder-und-jugendhilferecht-sgb-viii` | Sachbereich Kinder- und Jugendhilferecht (SGB VIII) im Geschaeftsbereich BMBFSFJ: Normbestand (SGB VIII; KJSG; BKSchG; AdoptionsG; UVG.); Akteure (Jugendaemter; Landesjugendaemter; Bundesjugendamt; Bundeszentrale fuer Kinder- und Jugend-... |
| `legw-bmbfsfj-schul-und-berufsbildungsrecht` | Sachbereich Schul- und Berufsbildungsrecht im Geschaeftsbereich BMBFSFJ: Normbestand (BAfoeG; AFBG; BBiG; HwO; Schulgesetze der Laender; AufstFoeG.); Akteure (BMBFSFJ; Laender-Kultusministerien; KMK; BIBB; Berufsverbaende.); EU-Bezug (Be... |
| `legw-bmbfsfj-senioren-und-pflegevorbeugungsrecht` | Sachbereich Seniorenrecht und Pflegevorbeugung im Geschaeftsbereich BMBFSFJ: Normbestand (SGB XI; ALeistungsG; Pflege-Bahr; HeimG der Laender; HGB-Bezuege.); Akteure (BMBFSFJ; BMG (Schnittstelle Pflege); Laender-Heimaufsichten.); EU-Bezu... |
| `legw-bmds-datenrecht-und-data-act` | Sachbereich Datenrecht und Data Act im Geschaeftsbereich BMDS: Normbestand (Data Act (EU); Data Governance Act (EU); BDSG; IFG; UIG.); Akteure (BMDS; BfDI; ggf. Datenmittlerdienste-Aufsicht; BNetzA.); EU-Bezug (Data Act; Data Governance... |
| `legw-bmds-digitale-verwaltung-ozg-und-egovg` | Sachbereich Digitale Verwaltung (OZG; EGovG) im Geschaeftsbereich BMDS: Normbestand (OZG; OZG-AeG; EGovG; EGovG-Laender; eIDAS-DurchG; XOeV.); Akteure (BMDS; ITZBund; FITKO; Laender-CIOs; Bundesdruckerei.); EU-Bezug (Single Digital Gatew... |
| `legw-bmds-it-sicherheit-und-bsig` | Sachbereich IT-Sicherheit (BSIG) im Geschaeftsbereich BMDS: Normbestand (BSIG; KritisDachG; SGRichtlinien; NIS2-UmsG; CER-UmsG.); Akteure (BSI; Bundesnetzagentur; BBK; Laender-Aufsichten.); EU-Bezug (NIS2-RL; CER-RL; Cyber Resilience Act... |
| `legw-bmds-ki-verordnung-und-aufsichtsstruktur` | Sachbereich KI-Verordnung und Aufsichtsstruktur im Geschaeftsbereich BMDS: Normbestand (KI-VO (EU); BDSG; ProdSG; ProdHaftG; einschlaegige Sektorgesetze.); Akteure (BMDS; BNetzA (Marktaufsicht KI; geplant); BSI; BfDI; Laenderbehoerden.);... |
| `legw-bmds-verwaltungsdigitalisierung-und-registermodernisierung` | Sachbereich Verwaltungsdigitalisierung und Registermodernisierung im Geschaeftsbereich BMDS: Normbestand (RegMoG; IDNrG; OZG; XOeV; Personenstandsrecht.); Akteure (BMDS; BMI (Personenstand); Bundesverwaltungsamt; Laender.); EU-Bezug (Sin... |
| `legw-bmf-finanzmarktaufsicht-bafin-kwg-wpig` | Sachbereich Finanzmarktaufsicht (BaFin; KWG; WpIG) im Geschaeftsbereich BMF: Normbestand (KWG; ZAG; WpIG; WpHG; KAGB; VAG; FinDAG; FinStabG; SAG; BörsG.); Akteure (BaFin; Deutsche Bundesbank; ESMA; EBA; EIOPA; FSB.); EU-Bezug (CRR; CRD;... |
| `legw-bmf-geldwaesche-und-sanktionsrecht` | Sachbereich Geldwaescherecht und Sanktionsrecht im Geschaeftsbereich BMF: Normbestand (GwG; KWG; AnzeigeV; SanktDG; AWG (Sanktionsumsetzung).); Akteure (FIU; BaFin; Zoll; Justiz; LKA.); EU-Bezug (EU-Geldwaescherichtlinie und kommende AML... |
| `legw-bmf-haushalts-und-zuwendungsrecht` | Sachbereich Haushaltsrecht und Zuwendungen im Geschaeftsbereich BMF: Normbestand (BHO; HG; VV-BHO; HGrG; ANBest-P; ANBest-I; Zuwendungsbescheid-Muster; SubvG.); Akteure (BMF Z-Abteilung; Bundesrechnungshof; zuwendende Bundesressorts; jur... |
| `legw-bmf-steuerrecht-und-fiskalnormen` | Sachbereich Steuerrecht und Fiskalnormen im Geschaeftsbereich BMF: Normbestand (AO; EStG; KStG; UStG; GewStG; ErbStG; SolZG; AStG; FVG.); Akteure (BZSt; Finanzaemter der Laender; BFH; FG; juris-Finanzrechtsprechung.); EU-Bezug (MwSt-Syst... |
| `legw-bmf-zoll-und-aussenwirtschaftsrecht` | Sachbereich Zollrecht und Aussenwirtschaftsrecht im Geschaeftsbereich BMF: Normbestand (AWG; AWV; ZollVG; UZK (EU); UStG (Einfuhrumsatzsteuer); KrWaffKG.); Akteure (Generalzolldirektion; Bundeszollverwaltung; BAFA (im BMWE); BMF Z-Abteil... |
| `legw-bmftr-biotechnologie-und-laborsicherheit` | Sachbereich Biotechnologie und Laborsicherheit im Geschaeftsbereich BMFTR: Normbestand (GenTG; GenTSV; GenTAufzV; ChemG; ArbSchG; BiostoffV; PflSchG.); Akteure (Zentrale Kommission fuer die Biologische Sicherheit (ZKBS); BVL; BfR; Laende... |
| `legw-bmftr-forschungsfoerderung-und-ressortforschung` | Sachbereich Forschungsfoerderung und Ressortforschung im Geschaeftsbereich BMFTR: Normbestand (BHO; ANBest-P; SubvG; AGVO (Forschung); AGVO; Rahmenprogramm.); Akteure (BMFTR; Projekttraeger (PT; PT-DLR; PT Juelich); Ressortforschungseinr... |
| `legw-bmftr-hochschul-und-wissenschaftsrecht` | Sachbereich Hochschulrecht und Wissenschaftsrecht im Geschaeftsbereich BMFTR: Normbestand (HRG; WissZeitVG; LHGs der Laender; WHG (Wissenschaft); ProfBesG.); Akteure (BMFTR; Wissenschaftsrat; DFG; HRK; Laenderministerien.); EU-Bezug (ERA... |
| `legw-bmftr-kuenstliche-intelligenz-und-technikregulierung` | Sachbereich Kuenstliche Intelligenz und Technikregulierung im Geschaeftsbereich BMFTR: Normbestand (KI-VO (EU); ProdHaftG; ProdSG; BSIG; SGB-Bezuege.); Akteure (BSI; Marktueberwachung der Laender; BNetzA; ggf. KI-Marktaufsicht.); EU-Bezu... |
| `legw-bmftr-raumfahrt-und-weltraumrecht-wrgg` | Sachbereich Raumfahrt- und Weltraumrecht im Geschaeftsbereich BMFTR: Normbestand (WRG (Weltraumgesetz; geplant); ATG; SatDSiG; WeltraumvertraegeBGBl II.); Akteure (BMFTR; DLR; Bundeswehr (sicherheitsrelevant); ESA.); EU-Bezug (EU Space A... |
| `legw-bmg-arzneimittel-und-medizinprodukterecht` | Sachbereich Arzneimittel- und Medizinprodukterecht im Geschaeftsbereich BMG: Normbestand (AMG; MPG; MPDG; ApBetrO; AMNOG; MedBVSV.); Akteure (BfArM; PEI; G-BA; DIMDI/BfArM; Laender-Aufsichten.); EU-Bezug (VO 726/2004; MDR; IVDR; EMA.); t... |
| `legw-bmg-berufsrecht-heilberufe-und-approbation` | Sachbereich Berufsrecht der Heilberufe und Approbation im Geschaeftsbereich BMG: Normbestand (BApO; BAeOAusbV; KrPflG; PflBG; PsychThG; HebG; ZahnHeilkundeG; AppO.); Akteure (Approbationsbehoerden der Laender; Aerzte- und Zahnaerztekamme... |
| `legw-bmg-infektionsschutz-und-pandemierecht` | Sachbereich Infektionsschutz und Pandemierecht im Geschaeftsbereich BMG: Normbestand (IfSG; IGV-AusfG; ImpfschadenAnerkennung; SGB V (Tests und Impfen).); Akteure (RKI; PEI; BMG; Laender-Gesundheitsbehoerden; Gesundheitsaemter; STIKO.);... |
| `legw-bmg-krankenhaus-und-versorgungsstrukturrecht` | Sachbereich Krankenhaus- und Versorgungsstrukturrecht im Geschaeftsbereich BMG: Normbestand (KHG; KHEntgG; BPflV; KHGes der Laender; KHVVG (Krankenhausreform).); Akteure (BMG; G-BA; InEK; Laender (Krankenhausplanung); KVen.); EU-Bezug (E... |
| `legw-bmg-krankenversicherungs-und-leistungsrecht-sgb-v` | Sachbereich Krankenversicherungs- und Leistungsrecht (SGB V) im Geschaeftsbereich BMG: Normbestand (SGB V; SGB IV (Beitragsrecht); KHEntgG; AMG-Bezuege; AMNOG.); Akteure (GKV-Spitzenverband; G-BA; KBV; KZBV; BAS; LSG.); EU-Bezug (EU-Pati... |
| `legw-bmi-auslaender-und-staatsangehoerigkeitsrecht` | Sachbereich Auslaender- und Staatsangehoerigkeitsrecht im Geschaeftsbereich BMI: Normbestand (AufenthG; AsylG; StAG; FreizuegG/EU; AZRG; AsylbLG (mit BMAS).); Akteure (BAMF; Auslaenderbehoerden; Bundespolizei.); EU-Bezug (GEAS; Dublin-VO... |
| `legw-bmi-bevoelkerungsschutz-und-katastrophenrecht` | Sachbereich Bevoelkerungsschutz und Katastrophenrecht im Geschaeftsbereich BMI: Normbestand (ZSKG; BBK-G; KritisDachG; THWG; BSIG (Krisen).); Akteure (BBK; THW; Laender-Katastrophenschutz; KRITIS-Aufsichten.); EU-Bezug (EU-Katastrophensc... |
| `legw-bmi-oeffentlicher-dienst-und-beamtenrecht` | Sachbereich Oeffentlicher Dienst und Beamtenrecht im Geschaeftsbereich BMI: Normbestand (BBG; BeamtStG; BBesG; BVwVfG; LRG; BLV; BUVO; SBG.); Akteure (BMI; Bundesverwaltungsamt; Bundespersonalausschuss; oberste Dienstbehoerden.); EU-Bezu... |
| `legw-bmi-sicherheits-und-polizeirecht` | Sachbereich Sicherheits- und Polizeirecht im Geschaeftsbereich BMI: Normbestand (BPolG; BKAG; BNDG; BVerfSchG; G10G; PassG; PStG; WaffG; SprengG; VersG.); Akteure (BPOL; BKA; BfV; BND; ZITiS; Bundespolizeipraesidium.); EU-Bezug (Schengen... |
| `legw-bmi-verwaltungsverfahren-und-bundesverwaltung` | Sachbereich Verwaltungsverfahren und Bundesverwaltung im Geschaeftsbereich BMI: Normbestand (VwVfG; VwGO; IFG; UIG (mit BMUKN); BVerwGG; BBG; BeamtStG.); Akteure (Bundesbehoerden des allgemeinen Verwaltungsrechts; BVerwG.); EU-Bezug (EU-... |
| `legw-bmjv-gerichtsverfassungs-und-prozessrecht` | Sachbereich Gerichtsverfassungs- und Prozessrecht im Geschaeftsbereich BMJV: Normbestand (GVG; ZPO; StPO; VwGO; SGG; FGO; ArbGG; EGGVG.); Akteure (BMJV; Bundesgerichte; Justizverwaltungen der Laender.); EU-Bezug (EuGVVO; EU-Zustellungs-V... |
| `legw-bmjv-rechtsstaatlichkeit-und-grundrechte-querschnitt` | Sachbereich Rechtsstaatlichkeit und Grundrechte-Querschnitt im Geschaeftsbereich BMJV: Normbestand (GG; BVerfGG; BBG; RiStBV; Konsulat- und Auslieferungsrecht; EuMRK.); Akteure (BMJV; BVerfG; BGH; Auslaenderbehoerden; Bundesrat.); EU-Bez... |
| `legw-bmjv-straf-und-strafprozessrecht-pflege` | Sachbereich Straf- und Strafprozessrecht-Pflege im Geschaeftsbereich BMJV: Normbestand (StGB; StPO; OWiG; JGG; GVG; EGStGB.); Akteure (BMJV; Generalbundesanwalt; BGH-Strafsenate; Staatsanwaltschaften; LKA und BKA.); EU-Bezug (Strafrechts... |
| `legw-bmjv-verbraucherschutz-und-unlauterer-wettbewerb` | Sachbereich Verbraucherschutz und Wettbewerbsrecht (UWG) im Geschaeftsbereich BMJV: Normbestand (UWG; UKlaG; BGB-Verbraucherrecht; ProdSG; PreisangabenV.); Akteure (BMJV; vzbv; Wettbewerbszentrale; Landesbehoerden Verbraucherschutz.); EU... |
| `legw-bmjv-zivilrecht-und-buergerliches-gesetzbuch-pflege` | Sachbereich Zivilrecht und BGB-Pflege im Geschaeftsbereich BMJV: Normbestand (BGB; HGB; EGBGB; BeurkG; AGG; AGB-Recht; Verbraucherregelungen.); Akteure (BMJV; BGH; OLGs; juristische Fakultaeten als Sachverstaendige.); EU-Bezug (Verbrauch... |
| `legw-bmleh-agrar-und-foerderungsrecht-gak-gap` | Sachbereich Agrar- und Foerderungsrecht (GAK; GAP) im Geschaeftsbereich BMLEH: Normbestand (GAKG; AgrarZahlG; InVeKoSV; DueV; OeLG; BWaldG-Bezuege; AgrarStatG.); Akteure (BLE; Laender-Landwirtschaftsministerien; Generaldirektion AGRI; BM... |
| `legw-bmleh-forst-und-jagdrecht` | Sachbereich Forst- und Jagdrecht im Geschaeftsbereich BMLEH: Normbestand (BWaldG; BJagdG; LJagdGes der Laender; FleischhygieneG; ForstWG.); Akteure (BLE; Laender-Forstaemter und Jagdbehoerden; BMLEH.); EU-Bezug (EUDR (Verordnung gegen En... |
| `legw-bmleh-lebensmittelrecht-und-futtermittelrecht` | Sachbereich Lebensmittel- und Futtermittelrecht im Geschaeftsbereich BMLEH: Normbestand (LFGB; ZusatzstoffzulV; LMHV; FFG; OekoKennzG; LMIV; FuttermittelV.); Akteure (BVL; BfR; Laender-Lebensmittelueberwachung; BMLEH; EFSA (EU).); EU-Bez... |
| `legw-bmleh-oekolandbau-und-pflanzenschutzrecht` | Sachbereich Oekolandbau und Pflanzenschutzrecht im Geschaeftsbereich BMLEH: Normbestand (OeLG; PflSchG; PflSchAnwV; SaatG; DueV; OeKo-VO (EU).); Akteure (BLE; BVL (Zulassung Pflanzenschutzmittel); Laender-Pflanzenschutzdienste.); EU-Bezu... |
| `legw-bmleh-tierschutz-und-tiergesundheitsrecht` | Sachbereich Tierschutz- und Tiergesundheitsrecht im Geschaeftsbereich BMLEH: Normbestand (TierSchG; TierSchNutztV; TierGesG; SchwarzwildG; VermarktungsNormG.); Akteure (BVL; FLI; Laender-Veterinaerbehoerden; Kommunale Veterinaeramter; BM... |
| `legw-bmukn-abfall-und-kreislaufwirtschaftsrecht` | Sachbereich Abfall- und Kreislaufwirtschaftsrecht im Geschaeftsbereich BMUKN: Normbestand (KrWG; ElektroG; VerpackG; BatterieG; ChemG; AbfallverbringungsV.); Akteure (UBA; Laender-Abfallbehoerden; Stiftung EAR; Zentrale Stelle Verpackung... |
| `legw-bmukn-atom-und-strahlenschutzrecht` | Sachbereich Atom- und Strahlenschutzrecht im Geschaeftsbereich BMUKN: Normbestand (AtG; StrlSchG; StrlSchV; EndlSiUntG; StandAG; AtVfV.); Akteure (BMUKN; BASE; BGE; BfS; Laender-Atomaufsichten; Reaktor-Sicherheitskommission.); EU-Bezug (... |
| `legw-bmukn-immissionsschutz-und-bimschg` | Sachbereich Immissionsschutz (BImSchG) im Geschaeftsbereich BMUKN: Normbestand (BImSchG; BImSchV (1-44; TA Luft; TA Laerm); BBodSchG; UVPG; UmwRG.); Akteure (UBA; BfS (Strahlen); Laender-Genehmigungsbehoerden; Bundesverwaltung Verkehr.);... |
| `legw-bmukn-naturschutz-und-artenschutzrecht` | Sachbereich Naturschutz- und Artenschutzrecht im Geschaeftsbereich BMUKN: Normbestand (BNatSchG; NatschGesetze der Laender; CITES; BJagdG (Schnittstelle).); Akteure (BfN; UBA; Laender-Naturschutzbehoerden; Untere Naturschutzbehoerden.);... |
| `legw-bmukn-wasser-und-bodenschutzrecht` | Sachbereich Wasser- und Bodenschutzrecht im Geschaeftsbereich BMUKN: Normbestand (WHG; LWGs; BBodSchG; BBodSchV; AwSV; DueV; KrWG-Bezuege.); Akteure (UBA; BfG; Laender-Wasserbehoerden; LAWA.); EU-Bezug (Wasserrahmen-RL; Grundwasser-RL; N... |
| `legw-bmv-luft-und-luftverkehrsrecht` | Sachbereich Luft- und Luftverkehrsrecht im Geschaeftsbereich BMV: Normbestand (LuftVG; LuftVO; LuftBO; LuftVZO; LuftSiG; EU-VO 2018/1139.); Akteure (Luftfahrt-Bundesamt; BAF; DFS; EASA (EU).); EU-Bezug (EU-Luftverkehrs-VO; Single Europea... |
| `legw-bmv-mobilitaets-und-fuehrerscheinrecht` | Sachbereich Mobilitaets- und Fuehrerscheinrecht im Geschaeftsbereich BMV: Normbestand (FeV; StVG; PBefG; CsgG (Carsharinggesetz); GVFG; ElektroMobG.); Akteure (KBA; Fahrerlaubnisbehoerden; Verkehrsministerien der Laender.); EU-Bezug (Fue... |
| `legw-bmv-schienen-und-bahnregulierung-aeg` | Sachbereich Schienen- und Bahnregulierung (AEG) im Geschaeftsbereich BMV: Normbestand (AEG; ERegG; BSchwAG; BNetzAG; EisbahnG; ERegV.); Akteure (EBA; BNetzA; DB-Konzern; Laender-Aufsicht; Schienenverkehrsbeirat.); EU-Bezug (4. Eisenbahnp... |
| `legw-bmv-schifffahrts-und-seeverkehrsrecht` | Sachbereich Schifffahrts- und Seeverkehrsrecht im Geschaeftsbereich BMV: Normbestand (SeeAufgG; SchSG; BinSchG; SeeFischG; Marpol-Ausfuehrungsgesetze.); Akteure (BSH; BG Verkehr; Wasser- und Schifffahrtsverwaltung des Bundes; HavarieKomm... |
| `legw-bmv-strassenverkehrsrecht-und-stvg-stvo` | Sachbereich Strassenverkehrsrecht (StVG; StVO) im Geschaeftsbereich BMV: Normbestand (StVG; StVO; FeV; FZV; StVZO; FStrG; PBefG.); Akteure (Kraftfahrt-Bundesamt; BMV; Strassenverkehrsbehoerden der Laender und Kommunen.); EU-Bezug (Typgen... |
| `legw-bmvg-militaerische-beschaffung-und-vergaberecht` | Sachbereich Militaerische Beschaffung und Vergaberecht im Geschaeftsbereich BMVg: Normbestand (BwBeschG; GWB; VgV; SektVO; KonzVgV; VSVgV (Verteidigungs- und Sicherheitsvergabe).); Akteure (BAAINBw; BMVg-Abteilungen Ausruestung; BMWE-Ver... |
| `legw-bmvg-nato-und-stationierungsrecht` | Sachbereich NATO-Recht und Stationierungsrecht im Geschaeftsbereich BMVg: Normbestand (NATO-Truppenstatut; ZA-NTS; Stationierungsstreitkraefte-Schutzgesetz; AwSV.); Akteure (BMVg; BMI; BMJV; Bundesbehoerden im NATO-Verbund.); EU-Bezug (E... |
| `legw-bmvg-reservisten-und-zivilschutzrecht` | Sachbereich Reservistenrecht und Zivilschutzrecht im Geschaeftsbereich BMVg: Normbestand (ResG; SG; ZSKG; KritisDachG; BBK-G.); Akteure (Kommando Territoriale Aufgaben; BBK; Verband der Reservisten.); EU-Bezug (EU-Katastrophenschutzmecha... |
| `legw-bmvg-verteidigungstechnologie-export` | Sachbereich Verteidigungstechnologie und Exportkontrolle im Geschaeftsbereich BMVg: Normbestand (KrWaffKG; AWG; AWV; Dual-Use-VO (EU); SicherungsG.); Akteure (BAFA; AA; BMVg; Bundessicherheitsrat; Bundeskanzleramt.); EU-Bezug (Common Pos... |
| `legw-bmvg-wehrrecht-und-soldatenstatus` | Sachbereich Wehrrecht und Soldatenstatus im Geschaeftsbereich BMVg: Normbestand (SG; WStG; SUG; ResG; WPflG; WDO; UZwGBw.); Akteure (BMVg; Wehrdisziplinaranwaltschaft; Bundeswehrgerichtsbarkeit (BVerwG-Wehrdienstsenat); BAPersBw.); EU-Be... |
| `legw-bmwe-aussenwirtschaft-und-investitionspruefung` | Sachbereich Aussenwirtschaft und Investitionspruefung im Geschaeftsbereich BMWE: Normbestand (AWG; AWV (Abschnitt 5); FDI-Screening-VO (EU); KrWaffKG.); Akteure (BMWE; BMI; AA; BMF; Bundeskanzleramt.); EU-Bezug (FDI-Screening-VO; sektora... |
| `legw-bmwe-energie-und-netzregulierung-enwg` | Sachbereich Energierecht und Netzregulierung (EnWG) im Geschaeftsbereich BMWE: Normbestand (EnWG; ARegV; NEV; NetzAusbBG; BBPlG; KOV.); Akteure (Bundesnetzagentur; Bundeskartellamt; Laender-Energieregulierer; BMWE Abteilung Energie.); EU... |
| `legw-bmwe-erneuerbare-energien-eeg-windbg` | Sachbereich Erneuerbare Energien (EEG; WindBG) im Geschaeftsbereich BMWE: Normbestand (EEG; WindBG; KWKG; SolarSpitzenG; BImSchG-Bezuege; ROG.); Akteure (Bundesnetzagentur; Bafa; Laenderbehoerden Genehmigung; Planungsbehoerden.); EU-Bezu... |
| `legw-bmwe-industriepolitik-foerderrecht-und-beihilfen` | Sachbereich Industriepolitik; Foerderrecht; EU-Beihilfen im Geschaeftsbereich BMWE: Normbestand (BHO; SubvG; AGVO; Notifizierungspflicht (Art. 108 AEUV); ggf. IPCEI-Regeln.); Akteure (BMWE; Bafa; Projekttraeger; EU-Kommission GD COMP.);... |
| `legw-bmwe-wettbewerb-und-kartellrecht-gwb` | Sachbereich Wettbewerbsrecht und Kartellrecht (GWB) im Geschaeftsbereich BMWE: Normbestand (GWB; UWG; FKVO (EU); EU-Wettbewerbsverfahrensregeln.); Akteure (Bundeskartellamt; Monopolkommission; OLG Duesseldorf; EU-Kommission GD COMP.); EU... |
| `legw-bmwsb-bau-und-planungsrecht-baugb-baunvo` | Sachbereich Bau- und Planungsrecht (BauGB; BauNVO) im Geschaeftsbereich BMWSB: Normbestand (BauGB; BauNVO; PlanZV; ROG; BNatSchG-Bezuege; UVPG.); Akteure (BMWSB; Laender-Bauaufsicht; Kommunen; OVG.); EU-Bezug (UVP-RL; SUP-RL; FFH-RL.); t... |
| `legw-bmwsb-bauproduktenrecht-und-technische-normen` | Sachbereich Bauproduktenrecht und technische Normen im Geschaeftsbereich BMWSB: Normbestand (BauPG; BauPVO (EU); BauProdRiL; MBO; Landesbauordnungen.); Akteure (DIBt; BMWSB; Notified Bodies; Laender-Bauaufsicht.); EU-Bezug (BauPVO 305/20... |
| `legw-bmwsb-energetische-sanierung-und-geg` | Sachbereich Energetische Sanierung (GEG) im Geschaeftsbereich BMWSB: Normbestand (GEG; EnEV (alt); BAFA-Foerderrichtlinien; KfW-Foerderbedingungen.); Akteure (BAFA; KfW; BMWSB; Bezirksregierungen; Schornsteinfeger.); EU-Bezug (EPBD; EU-E... |
| `legw-bmwsb-mietrecht-und-wohnungspolitik` | Sachbereich Mietrecht und Wohnungspolitik im Geschaeftsbereich BMWSB: Normbestand (BGB Mietrecht; WoBindG; WoFG; MietPrG; MiSchG; Wohngeldgesetz.); Akteure (BMWSB; Justiz; Kommunen; Mieterbund; Wohnungswirtschaft.); EU-Bezug (Energieefff... |
| `legw-bmwsb-stadtentwicklung-und-foerderprogramme` | Sachbereich Stadtentwicklung und Foerderprogramme im Geschaeftsbereich BMWSB: Normbestand (StaedteBauFoerdG; BauGB Saniserung; Konjunkturpaket; KfW-Foerderprogramme.); Akteure (BMWSB; KfW; Laender-Stadtentwicklung; Kommunen.); EU-Bezug (... |
| `legw-bmz-entwicklungszusammenarbeit-und-bilaterale-abkommen` | Sachbereich Entwicklungszusammenarbeit und bilaterale Abkommen im Geschaeftsbereich BMZ: Normbestand (Verwaltungsvereinbarungen; HG; BHO; Vertragsgesetze (BGBl II).); Akteure (BMZ; GIZ; KfW; Auslandshandelskammern; AA-Schnittstelle.); EU... |
| `legw-bmz-humanitaere-hilfe-und-krisenpraevention` | Sachbereich Humanitaere Hilfe und Krisenpraevention im Geschaeftsbereich BMZ: Normbestand (Internationaler Hilfsfonds; HG; HumanitaereLeitlinien.); Akteure (BMZ; AA (humanitaere Hilfe ueberlappend); GIZ; THW; nichtstaatliche Organisation... |
| `legw-bmz-internationale-klimafinanzierung` | Sachbereich Internationale Klimafinanzierung im Geschaeftsbereich BMZ: Normbestand (Pariser Abkommen; KSG; HG; bilaterale Klimavereinbarungen.); Akteure (BMZ; BMUKN; KfW; Green Climate Fund; AWB.); EU-Bezug (EU-Klimafinanzierungsziele; G... |
| `legw-bmz-menschenrechte-in-lieferketten-lksg` | Sachbereich Menschenrechte in Lieferketten (LkSG) im Geschaeftsbereich BMZ: Normbestand (LkSG; HinSchG; ProdHaftG; ggf. EU-CSDDD Umsetzung; AWG-Schnittstellen.); Akteure (BAFA; BMZ; BMWE; BMJV.); EU-Bezug (EU-CSDDD; UNGP; OECD-Leitsaetze... |
| `legw-bmz-multilaterale-zusammenarbeit-und-eu` | Sachbereich Multilaterale Zusammenarbeit und EU im Geschaeftsbereich BMZ: Normbestand (UN-Charta; UN-Konventionen; EUZBLG; Vertragsgesetze.); Akteure (BMZ; AA; BMF; EU-Generaldirektionen; multilaterale Banken.); EU-Bezug (NDICI; EFAD-Arc... |
| `legw-eu-richtlinienumsetzung-spezial` | Spezialfall EU-Richtlinienumsetzung im deutschen Recht: ueberschiessende Umsetzung, Gold Plating, fristgerecht, EuGH-Aufsichtspflicht. Pruefraster fuer Ministerium. |
| `legw-gesetzgebungsverfahren-bauleiter` | Bauleiter Gesetzgebungsverfahren Bund: Referentenentwurf, Kabinettsbeschluss, Bundesrat, Bundestag. Pruefraster fuer Verbandsstellungnahme. |
| `legw-rechtsbereinigung-spezial` | Spezialfall Rechtsbereinigung und Entbuerokratisierung: Wegfallpruefung, Konsolidierung, Befristung Sunset-Klausel. Pruefraster fuer Ministerien. |
| `legw-rechtsfolgenabschaetzung-leitfaden` | Leitfaden Gesetzesfolgenabschaetzung GFA: monetaer, nicht monetaer, KMU-Test, Nachhaltigkeitspruefung. Pruefraster fuer Ressort und Verband. |
| `legw-ressort-aa` | Heranfuehrung Ressort AA (Auswaertiges Amt). Schwerpunkt: Voelkerrecht; konsularische Aufgaben; Aussenwirtschaftsdimension; EU-Verfahren; Sanktionsumsetzung. Kernnormen: GG Art. 32 und Art. 59; WVK; KonsG; PassG; AWG; AWV; EUZBLG; IntZG.... |
| `legw-ressort-bmas` | Heranfuehrung Ressort BMAS (Bundesministerium fuer Arbeit und Soziales). Schwerpunkt: Arbeit und Tarif; Sozialversicherung; Rente; Arbeitsschutz; Teilhabe. Kernnormen: ArbZG; TVG; ArbSchG; SGB I bis SGB XII; SGB IX; SGB VI; BetrVG. Fuenf... |
| `legw-ressort-bmbfsfj` | Heranfuehrung Ressort BMBFSFJ (Bundesministerium fuer Bildung; Familie; Senioren; Frauen und Jugend). Schwerpunkt: Bildung; Familienleistungen; Jugendhilfe; Gleichstellung; Senioren. Kernnormen: BAfoeG; BBiG; KJHG (SGB VIII); BEEG; Unter... |
| `legw-ressort-bmds` | Heranfuehrung Ressort BMDS (Bundesministerium fuer Digitales und Staatsmodernisierung). Schwerpunkt: Verwaltungsdigitalisierung; IT-Sicherheit; Daten- und Registerrecht; KI-Aufsicht. Kernnormen: OZG; EGovG; BSIG; OnlineZugG; Data Act (EU... |
| `legw-ressort-bmf` | Heranfuehrung Ressort BMF (Bundesministerium der Finanzen). Schwerpunkt: Steuer- und Fiskalrecht; Haushalts- und Zuwendungsrecht; Finanzmarkt; Zoll und Aussenwirtschaft; Geldwaesche. Kernnormen: AO; EStG; KStG; UStG; BHO; FinStabG; KWG;... |
| `legw-ressort-bmftr` | Heranfuehrung Ressort BMFTR (Bundesministerium fuer Forschung; Technologie und Raumfahrt). Schwerpunkt: Hochschule und Wissenschaft; Raumfahrt; Forschungsfoerderung; KI; Biotechnologie. Kernnormen: HRG; WissZeitVG; WRG; WissTrAG; ATG; BN... |
| `legw-ressort-bmg` | Heranfuehrung Ressort BMG (Bundesministerium fuer Gesundheit). Schwerpunkt: Arzneimittel; gesetzliche Krankenversicherung; Infektionsschutz; Heilberufe; Krankenhaus. Kernnormen: AMG; MPG; MPDG; SGB V; SGB XI; IfSG; BApO; KHG; KHEntgG. Fu... |
| `legw-ressort-bmi` | Heranfuehrung Ressort BMI (Bundesministerium des Innern). Schwerpunkt: Innere Sicherheit; Migration; Verwaltung; Bevoelkerungsschutz; oeffentlicher Dienst. Kernnormen: BPolG; BKAG; AufenthG; StAG; VwVfG; ZSKG; BBG; BeamtStG; PassG; PStG.... |
| `legw-ressort-bmjv` | Heranfuehrung Ressort BMJV (Bundesministerium der Justiz und fuer Verbraucherschutz). Schwerpunkt: Pflege von BGB und StGB; Prozessrecht; Verbraucherschutz; Rechtsstaatlichkeit. Kernnormen: BGB; HGB; StGB; StPO; ZPO; GVG; UWG; UKlaG; BDS... |
| `legw-ressort-bmleh` | Heranfuehrung Ressort BMLEH (Bundesministerium fuer Landwirtschaft; Ernaehrung und Heimat). Schwerpunkt: Agrar; Tierschutz; Lebensmittel; Forst und Jagd; Oekolandbau. Kernnormen: GAKG; TierSchG; LFGB; BWaldG; BJagdG; OeLG; PflSchG; DueV;... |
| `legw-ressort-bmukn` | Heranfuehrung Ressort BMUKN (Bundesministerium fuer Umwelt; Klimaschutz; Naturschutz und nukleare Sicherheit). Schwerpunkt: Immissionsschutz; Wasser; Abfall und Kreislaufwirtschaft; Naturschutz; Nukleares. Kernnormen: BImSchG; WHG; KrWG;... |
| `legw-ressort-bmv` | Heranfuehrung Ressort BMV (Bundesministerium fuer Verkehr). Schwerpunkt: Strasse; Schiene; Luft; Wasser; Mobilitaet und Fuehrerschein. Kernnormen: StVG; StVO; FeV; AEG; ERegG; LuftVG; SeeAufgG; BinSchG; PBefG. Fuenf Spezialfelder: strass... |
| `legw-ressort-bmvg` | Heranfuehrung Ressort BMVg (Bundesministerium der Verteidigung). Schwerpunkt: Wehrrecht; militaerische Beschaffung; NATO-Bezuege; Verteidigungstechnologie; Reserve. Kernnormen: SG; WStG; UZwGBw; BwBeschG; NATO-Truppenstatut; AWG; KrWaffK... |
| `legw-ressort-bmwe` | Heranfuehrung Ressort BMWE (Bundesministerium fuer Wirtschaft und Energie). Schwerpunkt: Energie und Netze; Erneuerbare; Industriepolitik; Aussenwirtschaft; Wettbewerb. Kernnormen: EnWG; EEG; WindBG; KWKG; BEHG; AWG; AWV; GWB; UStG; AReg... |
| `legw-ressort-bmwsb` | Heranfuehrung Ressort BMWSB (Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen). Schwerpunkt: Bauplanung; Mietrecht; Stadtentwicklung; Bauprodukte; energetische Sanierung. Kernnormen: BauGB; BauNVO; BGB Mietrecht; StaedtebauFo... |
| `legw-ressort-bmz` | Heranfuehrung Ressort BMZ (Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung). Schwerpunkt: Entwicklungszusammenarbeit; humanitaere Hilfe; Klimafinanzierung; Lieferketten; Multilaterales. Kernnormen: Bilaterale Abkomm... |
| `legw-ressort-router` | Ressort-Router der Legistik-Werkstatt: leitet nach Auftragsaufnahme in das richtige Bundes-Ressort. Klaert Ressort-Kuerzel BMF; BMI; AA; BMVg; BMWE; BMFTR; BMJV; BMBFSFJ; BMAS; BMDS; BMV; BMUKN; BMG; BMLEH; BMZ und BMWSB. Pro Ressort: He... |
| `legw-ressortaufgaben-aa` | Ressortaufgaben AA: typische Legistik-Aufgaben im Geschaeftsbereich Auswaertiges Amt. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinetts- und Bundes... |
| `legw-ressortaufgaben-bmas` | Ressortaufgaben BMAS: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Arbeit und Soziales. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vo... |
| `legw-ressortaufgaben-bmbfsfj` | Ressortaufgaben BMBFSFJ: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Bildung; Familie; Senioren; Frauen und Jugend. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnu... |
| `legw-ressortaufgaben-bmds` | Ressortaufgaben BMDS: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Digitales und Staatsmodernisierung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabs... |
| `legw-ressortaufgaben-bmf` | Ressortaufgaben BMF: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium der Finanzen. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabine... |
| `legw-ressortaufgaben-bmftr` | Ressortaufgaben BMFTR: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Forschung; Technologie und Raumfahrt. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressort... |
| `legw-ressortaufgaben-bmg` | Ressortaufgaben BMG: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Gesundheit. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kab... |
| `legw-ressortaufgaben-bmi` | Ressortaufgaben BMI: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium des Innern. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabinett... |
| `legw-ressortaufgaben-bmjv` | Ressortaufgaben BMJV: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium der Justiz und fuer Verbraucherschutz. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabsti... |
| `legw-ressortaufgaben-bmleh` | Ressortaufgaben BMLEH: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Landwirtschaft; Ernaehrung und Heimat. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressor... |
| `legw-ressortaufgaben-bmukn` | Ressortaufgaben BMUKN: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Umwelt; Klimaschutz; Naturschutz und nukleare Sicherheit. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; M... |
| `legw-ressortaufgaben-bmv` | Ressortaufgaben BMV: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Verkehr. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; Kabine... |
| `legw-ressortaufgaben-bmvg` | Ressortaufgaben BMVg: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium der Verteidigung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR-Vorlage; K... |
| `legw-ressortaufgaben-bmwe` | Ressortaufgaben BMWE: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wirtschaft und Energie. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressortabstimmung; NKR... |
| `legw-ressortaufgaben-bmwsb` | Ressortaufgaben BMWSB: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer Wohnen; Stadtentwicklung und Bauwesen. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung; Ressor... |
| `legw-ressortaufgaben-bmz` | Ressortaufgaben BMZ: typische Legistik-Aufgaben im Geschaeftsbereich Bundesministerium fuer wirtschaftliche Zusammenarbeit und Entwicklung. Klaert Vorhabenart; Begruendungspflichten; Verbaendeanhoerung nach GGO Paragraf 47; Mitzeichnung;... |
| `legw-rmap-anschluss-an-legw` | Brueckenskill: Wie verzahnt sich die Rulemap-Arbeit mit der uebrigen Legistik-Werkstatt (Auftragsaufnahme; Ressort-Router; Heranfuehrung; Ressortaufgaben; Sachfeld-Spezialfelder; normhierarchie-routing; verfassungsmaessigkeit-quercheck;... |
| `legw-rmap-bestimmtheit-und-justitiabilitaet` | Verfassungsrechtliche Pruefung: hat die Rulemap-Modellierung die Bestimmtheit der Norm erhoeht (gut) oder unzulaessig verkuerzt (schlecht)? Justitiabilitaet und Begruendungspflicht im Verwaltungsverfahren. Output Bestimmtheits- und Justi... |
| `legw-rmap-entscheidungsbaum-validierung` | Simulation und Verifikation der Rulemap: Faelle generieren; Pfadabdeckung messen; Soll-Ist-Vergleich gegen juristische Erwartung. Werkzeuge im Rulemap Builder: Capture; Simulate; Verify. Output Validierungsprotokoll mit Pfaddeckung; Tref... |
| `legw-rmap-evaluierung-und-aenderung` | Lebenszyklus einer Rulemap-Norm: Versionierung; Aenderung im Builder per Drag-and-Drop; Evaluation nach NKRG und GGO; Wirkungskontrolle; Rueckkopplung aus dem Vollzug. Output Aenderungs- und Evaluationsplan mit Zustaendigkeiten; Auslaufd... |
| `legw-rmap-export-und-systemintegration` | Export der Rulemap aus dem Builder; Integration in Fachverfahren; Schnittstellen zur eAkte; OZG-Service; Registerlandschaft. Output Integrations-blueprint mit Datenflussskizze und Pruefpunkten. Anschluss legw-rmap-anschluss-an-legw fuer... |
| `legw-rmap-grundlagen` | Grundlagen der Rulemapping-Methode: Law as Code; Rulemap als visuelles Entscheidungsmodell; Wenn-Dann-Logik mit Tatbestand; Rechtsfolge; Ausnahme; Verweisung. Akteure (Rulemapping-Group; Prof. Breidenbach; SPRIN-D-Foerderung; BMJ als Anw... |
| `legw-rmap-norm-zu-rulemap` | Praxisleitfaden Norm in Rulemap ueberfuehren: Capture (Norm erfassen); Model (Logikmodell zeichnen); Simulate (Workflow durchspielen); Verify (Entscheidungen pruefen); Integrate (in System einbinden); Improve (weiterentwickeln). Liefert... |
| `legw-rmap-tatbestand-und-rechtsfolge` | Knotenmodellierung in der Rulemap: jeden Tatbestand als pruefbare Bedingung; jede Rechtsfolge als Aktionsknoten. Konjunktion; Disjunktion; Negation; Schwellenwerte sauber abbilden. Output Tatbestands-Rechtsfolge-Liste mit Knoten-IDs; Dat... |
| `legw-rmap-verweisungen-und-ausnahmen` | Verweisungen (statisch; dynamisch; Rueckverweisung) und Ausnahmen in der Rulemap sauber modellieren. Verkettung von Normen ueber Subrulemaps; Verweisungsketten dokumentieren; Ausnahmen als eigenstaendige Pfade. Output Verweisungs- und Au... |
| `legw-rmap-vollzugstauglichkeit` | Bruecke von der Rulemap in den Verwaltungsvollzug: Antragsverfahren; Bescheidstruktur; Akteneinsicht; Widerspruch und Klage; Schnittstelle zu Fachverfahren (z.B. Genehmigungsverfahren mit mehreren Fachbehoerden). Output Vollzugskarte mit... |
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Aenderung aussieht ohne Aenderungsmarkierungen. Einheitlich les... |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Aenderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten muessen identifiziert... |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten. KMU-Aspekt mittelstand... |
| `normhierarchie-routing` | Richtige Startbahn und Normebene für ein legistisches Vorhaben bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschliessungsantrag. Anwendungsfall politische Vorgab... |
| `referentenentwurf-bauen` | Vollständigen Referentenentwurf des Bundes oder Landes aufbauen. Anwendungsfall legistischer Auftrag ist aufgenommen, Startbahn und Normebene sind bestimmt und ein Bundes- oder Landesministerium braucht Entwurfstext und Begründung. Klaer... |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft werden. Kommunen Art. 28... |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder einer Woche Fortbild... |
| `spezial-aenderungs-formular-portal-und-einreichung` | Aenderungs: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-baut-livequellen-und-rechtsprechungscheck` | Baut: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bundestag-fristen-form-und-zustaendigkeit` | Bundestag: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-entschliessungsantraege-red-team-und-qualitaetskontrolle` | Entschliessungsantraege: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fraktionen-dokumentenmatrix-und-lueckenliste` | Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kabinettsentwuerfe-compliance-dokumentation-und-akte` | Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-laender-behoerden-gericht-und-registerweg` | Laender: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-landtage-schriftsatz-brief-und-memo-bausteine` | Landtage: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-legistik-erstpruefung-und-mandatsziel` | Legistik: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ministerien-tatbestand-beweis-und-belege` | Ministerien: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-mitte-internationaler-bezug-und-schnittstellen` | Mitte: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-normgeber-verhandlung-vergleich-und-eskalation` | Normgeber: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-normtext-begruendung-und-synopse` | Normtext, Begründung und Synopse als Gesetzgebungswerkstatt: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-opposition-risikoampel-und-gegenargumente` | Opposition: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-referenten-zahlen-schwellen-und-berechnung` | Referenten: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vorlagen-mehrparteien-konflikt-und-interessen` | Vorlagen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Aenderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Aenderungen schnell zu erfassen. Pro geaendertem Par... |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine ungewollten Abweichungen vo... |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu beteiligender Verbaende R... |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft eingegangenen Entwurf. G... |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist. Bestimmtheitstrias I... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin legistik-werkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin legistik-werkstatt: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin legistik-werkstatt: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin legistik-werkstatt: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin legistik-werkstatt: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin legistik-werkstatt: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin legistik-werkstatt: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin legistik-werkstatt: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert strukturierte XML-Ausgabe.... |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte Zirkel A verweist a... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
