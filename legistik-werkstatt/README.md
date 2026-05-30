# Legistik-Werkstatt

Vollständige Werkstatt für Legistinnen und Legisten in Bundesministerien, Bundestag, Fraktionen, Oppositionsarbeit, Landesministerien, Landtagen sowie kommunalen und kammerlichen Normgebern. Vom politischen Auftrag über Startbahn, Normhierarchie, Kompetenzprüfung, Normenkartierung und Terminologie zu Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Rechtsverordnung und Satzung. Mit Querschnittsprüfungen Verfassungsrecht Europarecht Folgenabschätzung Goldplating Bestimmtheit Zirkelschluss. Erzeugt am Ende ein DOCX und PDF im passenden offiziellen Layout - ministerieller Referentenentwurf-Stil, BT-/Landtagsdrucksachen-Stil oder Arbeitsfassung für Fraktion, Ausschuss und Normgeber.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **- Elektronisches Pflichtpostfach** ([`testakten/legistik-pflichtpostfach/`](../testakten/legistik-pflichtpostfach/)).

Direkt-Download als ZIP: [testakte-legistik-pflichtpostfach.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-legistik-pflichtpostfach.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Legistik-Werkstatt (`legistik-werkstatt`, dieses Plugin) | [legistik-werkstatt.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/legistik-werkstatt.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

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

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

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
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Aenderung aussieht ohne Aenderungsmarkierungen. Einheitlich les... |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Aenderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten muessen identifiziert... |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten. KMU-Aspekt mittelstand... |
| `normhierarchie-routing` | Richtige Startbahn und Normebene für ein legistisches Vorhaben bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschliessungsantrag. Anwendungsfall politische Vorgab... |
| `referentenentwurf-bauen` | Vollständigen Referentenentwurf des Bundes oder Landes aufbauen. Anwendungsfall legistischer Auftrag ist aufgenommen, Startbahn und Normebene sind bestimmt und ein Bundes- oder Landesministerium braucht Entwurfstext und Begründung. Klaer... |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft werden. Kommunen Art. 28... |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder einer Woche Fortbild... |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Aenderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Aenderungen schnell zu erfassen. Pro geaendertem Par... |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine ungewollten Abweichungen vo... |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu beteiligender Verbaende R... |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft eingegangenen Entwurf. G... |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist. Bestimmtheitstrias I... |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert strukturierte XML-Ausgabe.... |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte Zirkel A verweist a... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
