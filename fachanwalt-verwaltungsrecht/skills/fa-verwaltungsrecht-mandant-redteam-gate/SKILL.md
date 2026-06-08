---
name: fa-verwaltungsrecht-mandant-redteam-gate
description: "FA Verwaltungsrecht Mandant Redteam Gate im Plugin Fachanwalt Verwaltungsrecht: prüft konkret Mandantenkommunikation im Plugin fachanwalt-verwaltungsrecht, Red-Team Qualitygate im Plugin fachanwalt-verwaltungsrecht, BImSchG-Genehmigung für Energieanlagen Wind, Biogas. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# FA Verwaltungsrecht Mandant Redteam Gate

## Arbeitsbereich

**FA Verwaltungsrecht Mandant Redteam Gate** ordnet den Fall über die tragenden Prüfungslinien: Mandantenkommunikation im Plugin fachanwalt-verwaltungsrecht, Red-Team Qualitygate im Plugin fachanwalt-verwaltungsrecht, BImSchG-Genehmigung für Energieanlagen (Wind. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-verwaltungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-verwaltungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `energieanlagen-bimschg-genehmigung-verfahren` | BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elektrolyseur) begleiten: Vorhabentraeger beantragt Genehmigung oder Drittbetroffener klagt dagegen. Normen: §§ 4 und 10 und 19 BImSchG (foermliches/vereinfachtes Verfahren), 4. BImSchV, TA Laerm, UmwRG (Verbandsklage). Prüfraster: Antragsunterlagen (Schallgutachten, Schattenwurf, saP), Drittanfechtung, UVP-Pflicht EuGH-Linie, Eilantrag § 80 Abs. 5 VwGO. Output Antragsunterlagen-Prüfung, Klageschrift-Entwurf oder Widerspruch. Abgrenzung: Planfeststellung Energietrassen siehe energietrassen-planfeststellung-rechtsschutz; Vergabe siehe fachanwalt-vergaberecht-Plugin. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-verwaltungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

### Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin fachanwalt-verwaltungsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-verwaltungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

### Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin fachanwalt-verwaltungsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Red-Team-Checks für Verwaltungsrechtsfälle

- **Klagebefugnis (§ 42 Abs. 2 VwGO):** Möglichkeit der Rechtsverletzung dargelegt? Nicht jede Beeinträchtigung genügt; Schutznorm-Theorie prüfen.
- **Statthaftigkeit:** Richtige Klageart (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage, Fortsetzungsfeststellung § 113 Abs. 1 S. 4 VwGO)?
- **Vorverfahren:** Widerspruch erforderlich (§ 68 VwGO) — in einigen Ländern für bestimmte Materien abgeschafft (z. B. NRW, Niedersachsen) — landesspezifisch prüfen.
- **Frist (§ 74 VwGO):** Ab Zustellung Widerspruchsbescheid bzw. — wo Vorverfahren entfällt — ab Bekanntgabe des VA; Rechtsbehelfsbelehrung fehlerhaft? Dann 1 Jahr (§ 58 Abs. 2 VwGO).
- **Sofortvollzug:** Bei § 80 Abs. 2 Nr. 4 VwGO Begründungspflicht der Anordnung (§ 80 Abs. 3 VwGO); fehlende Begründung führt regelmäßig zur Aussetzung.
- **Verhältnismäßigkeit/Ermessen:** Bei Ermessensverwaltungsakten Ermessensfehlerlehre (Nicht-, Unter-, Überschreitung, Fehlgebrauch) durchprüfen (§ 114 VwGO).
- **Keine erfundenen BVerwG-/OVG-Aktenzeichen** — jedes Az. live verifizieren.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `energieanlagen-bimschg-genehmigung-verfahren`

**Fokus:** BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elektrolyseur) begleiten: Vorhabentraeger beantragt Genehmigung oder Drittbetroffener klagt dagegen. Normen: §§ 4 und 10 und 19 BImSchG (foermliches/vereinfachtes Verfahren), 4. BImSchV, TA Laerm, UmwRG (Verbandsklage). Prüfraster: Antragsunterlagen (Schallgutachten, Schattenwurf, saP), Drittanfechtung, UVP-Pflicht EuGH-Linie, Eilantrag § 80 Abs. 5 VwGO. Output Antragsunterlagen-Prüfung, Klageschrift-Entwurf oder Widerspruch. Abgrenzung: Planfeststellung Energietrassen siehe energietrassen-planfeststellung-rechtsschutz; Vergabe siehe fachanwalt-vergaberecht-Plugin.

### Energieanlagen-BImSchG-Genehmigung-Verfahren

## Kernsachverhalt

Energieanlagen (Wind, Biogas, Wasserstoff, größere Solarthermie, KWK, Geothermie) bedürfen in der Regel einer BImSchG-Genehmigung nach §§ 4 ff. BImSchG, wenn sie eine bestimmte Schwelle nach der 4. BImSchV überschreiten. Das Skill bedient die Mandanten-Vertretung im förmlichen oder vereinfachten Verfahren — sowohl auf Vorhabenträger- als auch auf Nachbar-/Verbandsseite.

## Kaltstart-Rückfragen

1. Welcher Anlagen-Typ und welche installierte Leistung — Windkraftanlage, Biogas, KWK, Elektrolyseur, Geothermie, Freiflächen-PV?
2. Wo befindet sich der Standort, welche Behörde ist zuständig — untere Immissionsschutzbehörde, Regierungspräsidium, Bergamt?
3. Welcher Verfahrensstand — Voranfrage, laufender Antrag, Bescheid, Klage, Eilantrag?
4. In welcher Rolle ist der Mandant — Vorhabenträger, Drittbetroffener (Nachbar, Grundeigentümer), anerkannter Umweltverband?
5. Liegt UVP-Pflicht oder UVP-Vorprüfungspflicht nach UVPG vor?
6. Welche Gutachten existieren bereits — Schallgutachten, saP, Schattenwurf, UVP-Bericht?
7. Wurde Sofortvollzug angeordnet — Eilantrag nach § 80 Abs. 5 VwGO erforderlich?
8. Sind Verbandseinwendungen oder eine UmwRG-Klage bereits eingeleitet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 4 Abs. 1 BImSchG** — Genehmigungsbedürftige Anlagen dürfen nur errichtet und betrieben werden, wenn eine Genehmigung nach § 6 BImSchG erteilt worden ist.

**§ 5 Abs. 1 BImSchG** — Genehmigungsbedürftige Anlagen sind so zu errichten und zu betreiben, dass zur Gewährleistung eines hohen Schutzniveaus für die Umwelt insgesamt schädliche Umwelteinwirkungen und sonstige Gefahren, erhebliche Nachteile und erhebliche Belästigungen für die Allgemeinheit und die Nachbarschaft nicht hervorgerufen werden können (drittschützende Grundpflicht).

**§ 6 Abs. 1 BImSchG** — Die Genehmigung ist zu erteilen, wenn sichergestellt ist, dass die Grundpflichten des § 5 erfüllt werden und andere öffentlich-rechtliche Vorschriften und Belange des Arbeitsschutzes der Errichtung und dem Betrieb nicht entgegenstehen.

**§ 10 BImSchG** — Förmliches Genehmigungsverfahren mit Bekanntmachung, Auslegung, Erörterungstermin, Öffentlichkeitsbeteiligung bei Anlagen der Spalte 1 der 4. BImSchV.

**§ 19 BImSchG** — Vereinfachtes Verfahren ohne Öffentlichkeitsbeteiligung bei Anlagen der Spalte 2 der 4. BImSchV; Genehmigung durch Behörde von Amts wegen.

**§ 44 BNatSchG** — Schädigungs- und Störungsverbote für besonders und streng geschützte Arten; Fang, Tötung, Störung, Zerstörung von Fortpflanzungs- und Ruhestätten verboten (artenschutzrechtliche Verbote, Prüfpflicht in saP).

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema BImSchG-Genehmigungsverfahren

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Anlagen-Klassifizierung 4. BImSchV | Nr. 1.6 WEA, Nr. 1.4 Biogas, Nr. 8 Feuerungsanlage; Spalte 1 (förmlich) oder Spalte 2 (vereinfacht)? | Verfahrensart bestimmt |
| 2 | UVP-Pflicht UVPG | Anhang 1 UVPG: ab 20 WEA UVP-Pflicht; 6–19 allgemeine Vorprüfung; 3–5 standortbezogene Vorprüfung | UVP-Umfang festgelegt |
| 3 | Antragsunterlagen vollständig | Formular, Beschreibung, Schallgutachten, Schattenwurf, saP, Lageplan, UVP-Bericht | Vollständigkeitsprüfung durch Behörde |
| 4 | Schallgutachten TA Lärm | Beurteilungspegel je Immissionsort; Tag-/Nachtwerte; Vorbelastung; WR 55/40 dB(A), MI 60/45 dB(A) | Einhaltung Immissionsrichtwerte |
| 5 | Schattenwurf-Prognose | Max. 30 h/Jahr astronomisch, max. 8 h/Jahr meteorologisch (LAI-Hinweise); Abschaltautomatik als Auflage | Auflageninhalt Nebenbestimmung |
| 6 | saP § 44 BNatSchG | Erfassungszeitraum, Methoden, Arten (Rotmilan, Fledermäuse, Mauersegler); Vermeidungs- und CEF-Maßnahmen | Verbotstatbestand ausgeschlossen? |
| 7 | Öffentlichkeitsbeteiligung § 10 BImSchG | Bekanntmachung, Auslegung 1 Monat, Einwendungen 1 Monat, Erörterungstermin | Verfahrensfehler rügen |
| 8 | Genehmigungstatbestand § 6 BImSchG | Grundpflichten § 5; entgegenstehende öffentlich-rechtliche Vorschriften; Bauleitplan | Tatbestand erfüllt? |
| 9 | Nebenbestimmungen Auflagen | Lärm-Nachtabschaltung, Schattenwurf-Modul, Artenschutz-Bauzeit-Fenster, Rückbau-Bürgschaft | Verhältnismäßigkeit der Auflagen |
| 10 | Sofortvollzug § 80 Abs. 2 Nr. 4 VwGO | Klimaschutz-Argument; Begründungserfordernis § 80 Abs. 3 VwGO | Eilantrag prüfen |
| 11 | Klage-Befugnis Drittbetroffener § 42 Abs. 2 VwGO | Möglichkeitstheorie; Verletzung subjektiver Rechte aus § 5 BImSchG (drittschützend) | Klagebefugnis bejahen/verneinen |
| 12 | Klagefrist § 74 VwGO | 1 Monat ab Bekanntgabe; bei UVP-pflichtigen Vorhaben analog; Verband UmwRG | Frist dokumentieren |
| 13 | UmwRG Verbandsklage | § 2 UmwRG; Vorab-Mitwirkung Pflichtvoraussetzung; UVP-Defizite, saP-Fehler | Prozessuale Stellung |
| 14 | Ausschluss-Fristen Einwendungen | § 10 Abs. 3 BImSchG Einwendungsfrist; Präklusion bei späterer Klage | Einwendungen rechtzeitig |
| 15 | Eilantrag § 80 Abs. 5 VwGO | Interessenabwägung; formelle Mängel Vollziehungsanordnung § 80 Abs. 3; Hauptsacheerfolgsaussicht | Antrag stellen bei sofortigem Vollzug |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Einhaltung Schallimmissionsrichtwerte | Vorhabenträger (im Verfahren), Behörde (im Klageverfahren) | Schallgutachten, Gegengutachten, Messung |
| saP methodische Ordnungsgemäßheit | Vorhabenträger | Erfassungsberichte, Gutachten, Kartierdaten |
| Erhebliche Schattenwurf-Beeinträchtigung | Drittbetroffener (im Eilverfahren) | Schattenwurf-Simulation, eigene Ermittlung |
| UVP-Fehler | Verband / Drittbetroffener | UVP-Bericht, Verfahrensunterlagen |
| Klagebefugnis Drittbetroffener | Antragsteller | Entfernung, Grundstücksplan, Schallprognose |
| Verhältnismäßigkeit Auflagen | Vorhabenträger bei Anfechtung | Alternativnachweis, Sachverständigengutachten |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Einwendungsfrist Auslegung | § 10 Abs. 3 BImSchG | 1 Monat nach Auslegungsende | Präklusion bei späterer Klage wenn kein Einwand erhoben |
| Klagefrist | § 74 VwGO | 1 Monat ab Bekanntgabe | Gilt auch bei UmwRG-Verbandsklagen |
| Beschwerde Eilentscheidung | § 146 Abs. 4 VwGO | 2 Wochen ab Beschluss, Begründung 1 Monat | OVG als Beschwerdegericht |
| Genehmigungsfiktion § 42a VwVfG | § 16 Abs. 1 BImSchG | Bei förmlichem Verfahren keine Fiktion; nur bei vereinfachtem Verfahren | Auf Fristeinhaltung achten |
| Gültigkeitsfrist Genehmigung | — | Genehmigung unbefristet; Nebenbestimmungen befristet | Auflagenfristen im Blick behalten |
| Verjährung Nachbar-Ansprüche | § 195 BGB | 3 Jahre ab Kenntnis | Privatrechtliche Ausgleichsansprüche |

## Typische Gegenargumente

| Gegenargument | Gegenstrategie |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "TA-Lärm-Werte eingehalten" | Vorbelastungs-Korrektur prüfen: wurden alle vorhandenen Windkraftanlagen in der Umgebung als Vorbelastung berücksichtigt? Kumulationseffekte? |
| "Klimaschutz rechtfertigt sofortige Vollziehung" | § 80 Abs. 3 VwGO: Begründung muss auf Einzelfall eingehen; abstrakter Klimaschutzverweis reicht nicht (OVG-Ständige Rspr.) |
| "Einwendungen präkludiert" | Präklusion greift nicht gegenüber UmwRG-Verbänden bei UVP-pflichtigen Vorhaben; UVP-Defizite jederzeit rügefähig |
| "Drittbetroffener nicht klagebefugt" | § 5 Abs. 1 Nr. 1 BImSchG ist drittschützend; Nachbar im Einwirkungsbereich hat subjektives Recht; Möglichkeitstheorie großzügig |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Einwendungen nicht substantiiert" | Im BImSchG-Verfahren genügt allgemeine Darlegung der Betroffenheit; detaillierte Rüge erst in Klage erforderlich |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — BImSchG-Genehmigungsverfahren begleiten | Verfahrensbegleitung nach Pruefschema; Schriftsatz unten |
| Variante A — Genehmigung für Drittbetroffene anfechten | Anfechtungsklage VwGO statt Verfahrensbegleitung |
| Variante B — Foermliches Genehmigungsverfahren nicht noetig | Anzeigeverfahren § 15 BImSchG als Alternative pruefen |
| Variante C — Behörde zoegert Untaetigkeit moegliche Alternative | Untaetigkeitsklage § 75 VwGO vorbereiten bei Verzoegerung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Klagebegründung Drittbetroffener (Schallschutz)

```
Verwaltungsgericht [Ort]
Klagebegründung

In der Verwaltungsrechtssache
[Kläger]
gegen
[Beklagte: Immissionsschutzbehörde]
beigeladen: [Vorhabenträger]

Az. VG [Az]

I. Sachverhalt

Der Kläger ist Eigentümer des Grundstücks [Anschrift], das sich in
einer Entfernung von ca. [x] Metern zur nächsten geplanten
Windkraftanlage befindet. Das Grundstück liegt im
[Wohn-/Mischgebiet].

Die Beklagte erteilte mit Bescheid vom [Datum] eine BImSchG-
Genehmigung für [n] Windkraftanlagen des Typs [Typ] am
Standort [Standort].

II. Zulässigkeit

Die Anfechtungsklage ist zulässig. Der Kläger ist nach §§ 42 Abs. 2,
113 Abs. 1 VwGO klagebefugt, da die Verletzung des drittschützenden
§ 5 Abs. 1 Nr. 1 BImSchG möglich erscheint. Die Klagefrist von einem
Monat (§ 74 VwGO) ist gewahrt.

III. Begründetheit — Verletzung § 5 Abs. 1 Nr. 1 BImSchG

1. Methodische Fehler im Schallgutachten

Das dem Bescheid zugrundeliegende Schallgutachten des Büros [Name]
vom [Datum] weist folgende methodische Mängel auf:

a) Unterschätzung der Vorbelastung — das Gutachten berücksichtigt
 die bestehenden Windkraftanlagen [Bezeichnung] in der Umgebung
 nicht als Vorbelastung. Nach TA Lärm Nr. 2.4 ist die
 Vorbelastung am Immissionsort zu berücksichtigen. Ohne
 Korrektur dieser Lücke kann die Einhaltung des Immissions-
 richtwerts von [40/45] dB(A) nachts nicht festgestellt werden.

b) Unzureichende Messung Schallleistungspegel — der verwendete
 Schallleistungspegel des Anlagentyps basiert auf Messungen
 unter optimalen Bedingungen. Ein Zuschlag für Amplituden-
 modulation nach TA Lärm Nr. A.2.3.3 wurde nicht berücksichtigt.

2. Beweissicherungsantrag

Der Kläger beantragt die Einholung eines gerichtlichen
Sachverständigengutachtens zur Frage, ob die Schallimmissions-
richtwerte der TA Lärm am Grundstück des Klägers eingehalten
werden.

Anlagen: Privates Gegengutachten [Anlage K1], Lagepläne [K2]
```

### Baustein 2: Einwendung im BImSchG-Verfahren (Naturschutz)

```
An die [Immissionsschutzbehörde]
Verfahren: BImSchG-Genehmigung [Vorhaben]

Einwendungen nach § 10 Abs. 3 BImSchG

Einwender: [Name, Adresse]

Sehr geehrte Damen und Herren,

gegen das geplante Vorhaben erheben wir namens und in Vollmacht
des Einwenders folgende Einwendungen:

1. Artenschutzrechtliche Defizite der saP

Die ausgelegte saP des Büros [Name] vom [Datum] genügt den
methodischen Anforderungen nicht:

a) Unzureichender Erfassungszeitraum für Fledermäuse — die
 Transekt-Kartierung umfasste lediglich [n] Termine im
 Zeitraum [Monat – Monat]. Für eine ordnungsgemäße saP sind
 nach den LLUR-/LfU-Hinweisen der Länder mindestens [n]
 Detektorerhebungen über die gesamte Aktivitätssaison
 (April bis Oktober) erforderlich.

b) Rotmilan — im Radius von 1.500 m um den Standort wurden
 während des Erfassungszeitraums [n] Rotmilan-Individuen
 kartiert. Das Gutachten kommt zu dem Ergebnis, es bestehe
 kein signifikant erhöhtes Tötungsrisiko gem. § 44 Abs. 1
 Nr. 1 BNatSchG. Diese Bewertung ist angreifbar, da die
 Kartierung nicht in den Hauptaktivitätsstunden
 (08:00–12:00 Uhr) an mindestens 12 Termine erfolgte.

c) Fehlende CEF-Maßnahmen — für den nachgewiesenen Bestand
 der [Art] wurden keine vorgezogenen Ausgleichsmaßnahmen
 (CEF) benannt.

2. Schattenwurf

Die Schattenwurf-Simulation zeigt für das Grundstück des Einwenders
([Adresse]) eine theoretische Beschattungsdauer von [x] Stunden/Jahr.
Die angeordneten Auflagen genügen nicht, da eine Abschaltautomatik
fehlt.

Wir beantragen daher die Versagung der Genehmigung,
hilfsweise die Aufnahme konkreter Nebenbestimmungen.
```

### Baustein 3: Antrag auf Akteneinsicht und Vorbereitung Eilantrag

```
An die [Immissionsschutzbehörde]

Antrag auf Akteneinsicht § 29 VwVfG

Sehr geehrte Damen und Herren,

wir zeigen an, namens und in Vollmacht [des Mandanten]
tätig zu sein. Wir beantragen Einsicht in die gesamte
Genehmigungsakte des Verfahrens [Az.], einschließlich:

- aller eingereichten Gutachten und Stellungnahmen
- der Behördenkorrespondenz
- der Nebenbestimmungen und Prüfvermerke
- des UVP-Berichts und der Behördenentscheidung zur UVP-Pflicht

Sobald die Sofortvollziehung angeordnet wird, werden wir beim
Verwaltungsgericht [Ort] Eilantrag nach § 80 Abs. 5 VwGO stellen.
Die Akteneinsicht ist für die Begründung unabdingbar.

Wir bitten um Mitteilung des frühesten Termins für die Einsicht.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Drittbetroffener | § 52 Abs. 1 GKG; Orientierungswert nach Streitwertkatalog Verwaltungsgerichtsbarkeit: Nachbar-WEA typisch EUR 15.000–30.000 je nach Anlage | Konjunktur der Rspr. beachten; bei mehreren Klagepunkten Addierung |
| Streitwert Vorhabenträger (Genehmigungsklage) | Investitionsvolumen / Ertragserwartung; typisch EUR 50.000–200.000 | § 52 Abs. 1 GKG Abschätzung nach wirtschaftlichem Interesse |
| Gerichtskosten | GKG Anlage 1 Nr. 1210; bei EUR 20.000 Streitwert ca. EUR 1.888 | Bei VG-Verfahren drei Instanzen einkalkulieren |
| Sachverständigenkosten saP | EUR 5.000–20.000 je nach Artenspektrum und Erfassungsaufwand | Ggf. gerichtliches Gutachten auf Kosten der Gegenseite bei Obsiegen |
| Eilverfahren Streitwert | Halb des Hauptsache-Streitwerts | § 80 Abs. 5 VwGO-Beschluss = Bruchteil |

## Strategische Empfehlung

| Mandantenrolle | Situation | Empfehlung |
|---|---|---|
| Vorhabenträger | Antragsunterlagen unvollständig | Proaktive Abstimmung mit Behörde vor Einreichung; Gutachter-Auswahl nach behördlicher Praxis |
| Vorhabenträger | Klage Drittbetroffener | Sachverständige beiziehen; § 80 Abs. 3-Begründung präzise ausarbeiten; frühe Verhandlung anbieten |
| Drittbetroffener | Bescheid ergangen | Eigenes Schallgutachten in Auftrag geben; Einwendungs-Präklusion prüfen; Klagefrist sichern |
| Drittbetroffener | Sofortvollzug angeordnet | Eilantrag § 80 Abs. 5 VwGO; § 80 Abs. 3-Begründungsmangel angreifen; Hauptsache parallel einreichen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Anschluss-Skills

- `energietrassen-planfeststellung-rechtsschutz` — Planfeststellungsverfahren für Leitungen und Netzinfrastruktur
- `eilantrag-80-abs-5-vwgo` — Vertiefung Eilantragsstrategie und Schriftsatz
- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Grundlagen einstweiliger Rechtsschutz
- `fachanwalt-verwaltungsrecht-widerspruchsschrift` — Widerspruch gegen Genehmigungsbescheid

## Aktuelle Leitentscheidungen (v14.2 Ergaenzung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- BImSchG §§ 4, 5, 6, 10, 19
- 4. BImSchV Anhang 1 (Nrn. 1.4, 1.6, 8)
- TA Lärm (6. Allg. VwV BImSchG)
- TA Luft 2021
- UVPG Anhang 1
- BNatSchG §§ 13, 44
- VwGO §§ 42, 74, 80, 113
- UmwRG § 2
- EU-RED III (Beschleunigungsgebiete)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

<!-- AUDIT 27.05.2026 — Bundle 027 Halluzinations-Reparatur
-->
