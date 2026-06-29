# Liquiditätsplanung — Power-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Liquiditätsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Lücken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`liquiditaetsplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung-werkstatt.md" download><code>liquiditaetsplanung-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung-schnellstart.md" download><code>liquiditaetsplanung-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-beispielakte-edelholz-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beispielakte-edelholz-berlin.zip) (Edelholz Manufaktur Berlin GmbH — Liquiditäts- und Steuerakte); [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) (Forschungszulage Riedblick Sensorik GmbH); [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) (Fortbestehensprognose Paragrafix GmbH) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine belastbare Liquiditaetsplanung aufstellen und drohende Zahlungsunfaehigkeit fruehzeitig erkennen.
**Eigenständiges Power-Plugin** für wochenaktuelle Liquiditätsvorschauen nach deutschem Recht (§§ 17, 18, 19 InsO; § 1 StaRUG; BGH-Schema Passiva II). Funktioniert allein. Ergänzt sich optional mit `insolvenzrecht` und `steuerrecht-anwalt-und-berater`, hängt aber nicht von ihnen ab.

---

## Was ist drin

Vier Fachskills plus Allgemein-Skill, alle fachlich autark:

| Skill | Zweck | Horizont |
| --- | --- | --- |
| `idw-s6-integrierte-sanierungsplanung` | Brücke von Liquiditätsvorschau zu Sanierungskonzept: GuV, Planbilanz, Maßnahmenlog, Annahmenregister, Sensitivitäten und Sanierungsfähigkeits-Ampel. | 12-24 Monate |
| `liquiditaetsvorschau-3wochen` | Wochenaktuelle Vorprüfung § 17 InsO (Freitag-Stichtag), Verhältnis zu offenen Forderungen, Ampel. | 3 Wochen |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Planung mit Sensitivität (Best/Base/Worst), Fortbestehensprognose nach § 19 InsO und Übergabe in die Sanierungsplanung. | 13 / 26 / 52 Wochen |
| `liquiditaetsvorschau-insolvenzrechtlich` | Gerichtsfeste Liquiditätsbilanz nach BGH-Schema (Passiva II zwingend, Volumeneffekt der Quote, titulierte Forderungen mit Nennwert). | Stichtagsbezogen |

## Ergebnisformate

Jeder Skill liefert standardmäßig eine **Excel-Tabelle** nach der hinterlegten Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`, KW-Spalten × Kategorien-Zeilen, Freitag als Wochenstichtag). Zusätzlich auf Wahl:

- **Interaktives HTML-Padlet** (`assets/padlet/liquiditaets-padlet.html`) — single-file, autark, rechnet die Ampel live nach BGH-Schema, speichert in `localStorage`, exportiert/importiert JSON.
- **Markdown-Artefakt** (`assets/markdown/liquiditaets-artefakt-vorlage.md`) — Tabellen, Indizienliste, Kurzfazit; wird bei jeder Folgemeldung neu geschrieben.
- **Memo** im Gutachtenstil (DOCX oder Markdown) — **nur auf ausdrückliche Anfrage**.

Die Skills fragen einmal am Anfang nach Format und merken sich die Antwort.

## Banking

Jeder Skill fragt einmal nach der Datenquelle:

1. **Manuell** im Padlet/Artefakt/Chat.
2. **Datei-Import** — CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS.
3. **Connector** — PSD2/FinTS oder verfügbare Anbieter (per `list_external_tools`).

Mandatsgeheimnis (§§ 203/204 StGB, § 43e BRAO) und Drittlandtransfer (DSGVO Art. 44 ff.) werden adressiert.

## BGH-Schema (Passiva II)

```
Aktiva I   = Bank + Kasse + freier zugesagter Kontokorrent (Stichtag)
Aktiva II  = Σ Einzahlungen KW t..t+2
Passiva I  = am Stichtag fällig, eingefordert, nicht echt gestundet
Passiva II = binnen 3 Wochen fällig (KW t+1 + KW t+2)

Lücke abs. = max(0, (Passiva I + Passiva II) − (Aktiva I + Aktiva II))
Quote      = Lücke abs. ÷ (Passiva I + Passiva II)
```

**Ampel**: 🟢 Quote < 10 % und Liquidität KW t+2 ≥ 0 und < 2 Indizien. 🟡 Quote ≥ 10 %, KW t+2 ≥ 0, < 2 Indizien (schließbar). 🔴 sonst — § 17 InsO indiziert.

## Leitentscheidungen und Livecheck

Diese Entscheidungen sind als frei prüfbare Arbeitsanker gedacht; vor einer Mandatsausgabe immer Gericht, Datum, Aktenzeichen, Randnummer/Sachverhalt und Aussage anhand einer amtlichen oder frei zugänglichen Quelle nachziehen.

1. **BGH, Urteil vom 24.05.2005 - IX ZR 123/04**: Abgrenzung Zahlungsstockung/Zahlungsunfähigkeit; Liquiditätslücke von 10 Prozent oder mehr regelmäßig kritisch, wenn sie nicht kurzfristig nahezu vollständig geschlossen werden kann.
2. **BGH, Urteil vom 19.12.2017 - II ZR 88/16**: Liquiditätsstatus und Liquiditätsbilanz; Einbeziehung der innerhalb von drei Wochen fällig werdenden Verbindlichkeiten (Passiva II) in die Prüfung des § 17 InsO.
3. **BGH, Urteil vom 28.06.2022 - II ZR 112/21**: Zahlungsunfähigkeit kann mit geordneter Liquiditätsgegenüberstellung und Buchhaltungsunterlagen dargelegt werden; keine mechanische Scheingenauigkeit, sondern belegbare Zahlenbasis.
4. **Aktualitätsregel**: Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Wenn weitere Rechtsprechung gebraucht wird, erst live über `bundesgerichtshof.de`, `dejure.org` oder eine vom Nutzer bereitgestellte Quelle verifizieren.

Berufsständischer Hintergrund: Methodenrahmen zu Insolvenzeröffnungsgründen und Sanierungskonzepten; nicht als Ersatz für Gesetz, Rechtsprechung und konkrete Subsumtion zitieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 73 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampel-zahlen-schwellenwerte-berechnung` | Ampel: Zahlen, Schwellenwerte und Berechnung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Ver... |
| `anschluss-routing` | Anschluss-Routing für Liquiditätsplanung: wählt den nächsten Spezial-Skill nach Engpass (Rolling 13-week-Plan, Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste), dokumentiert Router-Entscheidung mit Begründung. |
| `ausgabengruppen-fristennotiz-naechster` | Ausgabengruppen: Fristennotiz und nächster Schritt: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion od... |
| `ausgabengruppen-systematik` | Ausgabengruppen systematisch erfassen: Personal (Lohn, SV, LSt), Material/Wareneinsatz, Miete, Energie, Versicherungen, Beratungs-/Anwaltskosten, Steuerzahlungen, Investitionen, Zinsen, Tilgung. Vorlage Tabelle. |
| `bei-drohender-zahlungsunfaehigkeit` | Liquiditaetsplanung bei drohender Zahlungsunfaehigkeit § 18 InsO: 24-Monats-Planung, Zugang StaRUG-Restrukturierung, Geschäftsleiterpflichten. Prüfraster und Schnittstelle Insolvenzantrag. |
| `bei-eingetretener-zahlungsunfaehigkeit` | Liquiditaetsplanung bei eingetretener Zahlungsunfaehigkeit § 17 InsO: 3-Wochen-Vorschau zur Prüfung Insolvenzantragspflicht, Liquiditaetsluecke kleiner 10 Prozent + Schliessung binnen 3 Wochen waere Liquiditaetsstockung. Prüfraster BGH I... |
| `cash-pooling-konzern` | Cash-Pooling im Konzern: rechtliche Risiken Existenzvernichtung BGH II ZR 78/06, Sanierungstauglichkeit, Prüfung Avale gegen Konzerngesellschaften, Steuerrisiken § 8b KStG. Output: Cash-Pool-Risiko-Memo. |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix der Liquiditätsplanung: Kontostände, OP-Listen, Fälligkeiten, Planannahmen, Krisenentscheidungen und Nachweisfähigkeit zusammenführen. |
| `deutschem-dokumentationspaket-excel` | Deutschem Dokumentationspaket Excel: prüft konkret Deutschem, Dokumentationspaket, Excel. |
| `deutschem-tatbestandsmerkmale-beweisfragen` | Deutschem: Tatbestandsmerkmale, Beweisfragen und Beleglage: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, San... |
| `dokumentationspaket-bank` | Dokumentationspaket: Compliance-Dokumentation und Aktenvermerk: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `dokumente-intake` | Dokumentenintake für Liquiditätsplanung: sortiert Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste, prüft Datum, Absender, Frist und Beweiswert (Bankbestätigungen, Eingangs-/Ausgangsrechnungen); markiert Lücken; berücksi... |
| `drohender-zahlungsunfaehigkeit` | Liqui Drohender Zahlungsunfaehigkeit: prüft konkret Liquiditaetsplanung bei drohender Zahlungsunfaehigkeit § 18, Liquiditaetsplanung bei eingetretener Zahlungsunfaehigkeit, Liquiditaetsplanung für Bankgespraech. |
| `eingangsdaten-checkliste` | Eingangsdaten-Checkliste für Liquiditaetsplanung: BWA, OPOS Debitoren/Kreditoren, Kontoauszuege, Steuerkonten, SV-Konten, Personalkosten, Investitionsplanung. Prüfliste Quellen und Vollstaendigkeit. Output: standardisiertes Datentemplate. |
| `eingangsdaten-idw-s6-liqp` | Liqui Eingangsdaten IDW S6 Liqp: prüft konkret Eingangsdaten-Checkliste für Liquiditaetsplanung, Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungspla, Leitfaden Bankenreporting bei Krise. |
| `einstieg-routing` | Einstieg, Triage und Routing für Liquiditätsplanung: ordnet Rolle (Geschäftsführung, Finanzen/CFO, Bank), markiert Frist (Rolling 13-week-Plan), wählt Norm (IDW S 11 (Sanierung), § 18 InsO drohende ZU) und Zuständigkeit (Bank), leitet zu... |
| `excel` | Excel: Behörden-, Gerichts- oder Registerweg: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Ver... |
| `export` | Export: Schriftsatz-, Brief- und Memo-Bausteine: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder... |
| `export-forecast-fortbestehensprognose` | Export Forecast Fortbestehensprognose: prüft konkret Export, Forecast, Fortbestehensprognose. |
| `forecast-risikoampel-gegenargumente` | Forecast: Risikoampel, Gegenargumente und Verteidigungslinien: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung,... |
| `forecast-wochenplanung` | Liquiditaetsplanung: Erstprüfung, Rollenklärung und Mandatsziel: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung... |
| `fortbestehensprognose-international` | Fortbestehensprognose: Internationaler Bezug und Schnittstellen: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel der Liquiditätsplanung: Insolvenzreife, Antragspflicht, Steuer-/SV-Fälligkeiten, Lohnrisiken, Bankfristen und Maßnahmenplan. |
| `fuer-bankgespraech` | Liquiditaetsplanung für Bankgespraech: kompakte Vorlage 13 Wochen + Jahresansicht, Annahmen-Block, Sensitivitaet, Kreditlinien-Ausnutzung, Begleittext. Empfehlung: realistisch, nicht zu optimistisch, mit Fallback-Hebeln. |
| `grundbegriffe-cashflow` | Liquiditaetsplanung Grundbegriffe: Cashflow vs. Gewinn, indirekte vs. direkte Methode, Liquiditaet 1./2./3. Grades, Working Capital. Abgrenzung zur GuV-Planung. Empfehlung: direkte Methode für 13-Wochen-Forecast, indirekte für Jahresplan... |
| `grundbegriffe-cashflow-kreditlinien` | Liqui Grundbegriffe Cashflow Kreditlinien: prüft konkret Liquiditaetsplanung Grundbegriffe, Kreditlinien prüfen, Debitorenseite optimieren. |
| `idw-s6-integrierte-sanierungsplanung` | Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen... |
| `insolvenzrecht-formular-portal` | Insolvenzrecht: Formular, Portal und Einreichungslogik: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktio... |
| `insolvenzrecht-liqui-sonderfall` | Insolvenzrecht Liqui Sonderfall: prüft konkret Insolvenzrecht, Liqui, Liquiditaetsplanung. |
| `interessen-verifikation-beweislast-vorschau` | Interessen Verifikation Beweislast Vorschau: prüft konkret Schnittstellen, Verifikation, Vorschau. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Liquiditaetsplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dok... |
| `kreditlinien-pruefen` | Kreditlinien prüfen: Kontokorrent, Investitionskredit, Avalkredit, Factoring-Linie, Lieferantenkredit. Ausnutzungsgrade, Tilgungsplaene, Sicherheiten, Covenants. Prüfraster für Bankgespraech. |
| `leasing-lp-restrukturierungsplan-starug` | Liqui Leasing LP Restrukturierungsplan Starug: prüft konkret Leasing- und Lebenspartnerzahlungen in Liquiditaetsplan, Liquiditaetsplanung im Restrukturierungsplan StaRUG, Saisonalitaet erkennen. |
| `liqp-bankenreporting-leitfaden` | Leitfaden Bankenreporting bei Krise: Anforderungen Hausbank, Konsortium, KfW, Reportingfrequenz, Covenant-Reporting. Prüfraster für CFO und Berater. |
| `liqp-liquiditaetspool-cash-pooling-spezial` | Spezialfall Liquiditaetspool und Cash-Pooling im Konzern: § 30 GmbHG, BGH-Rechtsprechung, vollwertiger Rueckzahlungsanspruch. Prüfraster für Konzernmutter und Tochter. |
| `liqp-liquiditaetspool-cash-rollende-13wochen` | Liqp Liquiditaetspool Cash Rollende 13wochen: prüft konkret Spezialfall Liquiditaetspool und Cash-Pooling im Konzern, Bauleiter rollende 13-Wochen-Liquiditaetsplanung, Spezialfall Warenkredit und Skontostrategien in der Krise. |
| `liqp-rollende-13wochen-bauleiter` | Bauleiter rollende 13-Wochen-Liquiditaetsplanung: Einnahmen / Ausgaben / Saldo / kumulierter Saldo, Granularitaet, Update-Zyklen. Prüfraster Mittelstand und Konzerntochter. |
| `liqp-warenkredit-skonto-szenarien-spezial` | Spezialfall Warenkredit und Skontostrategien in der Krise: Lieferantenverhandlung, Vorkasse, verlaengerter Eigentumsvorbehalt, Factoring. Prüfraster für Treasury. |
| `liqui-fuer-bankgespraech` | Liquiditaetsplanung fuer Bankgespraech: kompakte Vorlage 13 Wochen + Jahresansicht, Annahmen-Block, Sensitivitaet, Kreditlinien-Ausnutzung, Begleittext. Empfehlung: realistisch, nicht zu optimistisch, mit Fallback-Hebeln. |
| `liquiditaetsstatus-quellenbelege` | Liquiditätsstatus nur aus belastbaren Quellenbelegen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `liquiditaetsstatus-quellenbelege-live-quote` | Liquiditaetsstatus Quellenbelege Live Quote: prüft konkret Liquiditätsstatus nur aus belastbaren Quellenbelegen, Live, Quote. |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau für 3/6/12 Monate mit Fortfuehrungsprognose, Wochenraster, Excel-Export und Quellenhygiene. Rechtsprechung nur nach Live-Prüfung. |
| `liquiditaetsvorschau-3wochen` | Drei-Wochen-Liquiditätsvorschau nach Paragraf 17 InsO mit Wochenraster, Excel-Export, Quote, Lücken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Prüfung. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Prüft insolvenzrechtliche Liquiditätsbilanz und Liquiditätsvorschau mit Passiva-Logik, streitigen Forderungen, Titeln, Stundungen und Sanierungsübergabe. |
| `live-mandantenkommunikation` | Live: Mandantenkommunikation und Entscheidungsvorlage: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion... |
| `luecken-quellenkarte` | Luecken Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mahnstufen-debitoren` | Debitorenseite optimieren: DSO-Kennzahl, Mahnstufen, Skontostrategie, Factoring-Optionen, Forderungsausfallversicherung. Empfehlung: 3-Wochen-Forecast getrennt nach Kategorie 'sicher / wahrscheinlich / fraglich'. |
| `mandantenkommunikation` | Mandantenkommunikation in der Liquiditätsplanung: Zahlenanforderung, Annahmen, Krisenfristen, Geschäftsleiterpflichten und klare Entscheidungsnotiz ohne unnötige Rollenabfragen. |
| `mandantenkommunikation-redteam-qualitygate` | Red-Team und Quality-Gate für Liquiditätskommunikation: Plausibilitätscheck, Haftungsrisiken, Zahlenlücken, Sanierungsannahmen und versandfähige Mandanten-/Geschäftsleiternotiz. |
| `mit-leasing-und-lp` | Leasing- und Lebenspartnerzahlungen in Liquiditaetsplan: operate lease als opex, finance lease wirkt sich auf Bilanz aus, vorzeitige Aufloesung kostenpflichtig. Empfehlung: Aufnahme nach Faelligkeit, Prüfung Beendigungskosten. |
| `output-waehlen` | Output-Wahl für Liquiditätsplanung: stimmt Adressat (Geschäftsführung, Finanzen/CFO, Bank), Frist (Rolling 13-week-Plan) und Form auf den Zweck ab — typische Outputs: 13-Wochen-Plan, 24-Monats-Plan, Cash-Pool-Aufstellung. |
| `quellen-livecheck` | Quellen-Live-Check für Liquiditätsplanung: prüft Normen (IDW S 11 (Sanierung), § 18 InsO drohende ZU) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Bank und Quellenhygiene nach references/quellenhygiene.md. |
| `quote-verhandlung-vergleich-eskalation` | Quote: Verhandlung, Vergleich und Eskalation: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Ver... |
| `rechtsprechung-fehlerkatalog` | Rechtsprechung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `redteam-qualitygate` | Red-Team Qualitygate für Liquiditätsplanung: prüft Fristen, Zuständigkeit, Beweislast, Quellen, Planmechanik, Insolvenznähe, Haftungsrisiken und taktische Risiken vor Abgabe, Banktermin, Gesellschafterrunde oder Versand. |
| `restrukturierungsplan-starug` | Liquiditaetsplanung im Restrukturierungsplan StaRUG: Plan-Liquiditaet, Sanierungsbeitraege Gläubiger, Working-Capital-Plan, Cash-Out-Termine. Output: integrierter Plan und Gläubigerverteilungsschema. |
| `saisonalitaet-erkennen` | Saisonalitaet erkennen: Vorjahres-Kontodaten gegen Liquiditaetsplan abgleichen, Monats- und Wochenmuster, Sondereffekte (Inventur, Jahresabschluss, Ferien). Empfehlung: saisonale Korrekturfaktoren je Branche. |
| `schnittstellen-mehrparteienkonflikt` | Schnittstellen: Mehrparteienkonflikt und Interessenmatrix: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sank... |
| `sondereffekt-grossauftrag` | Sondereffekt Grossauftrag in Liquiditaetsplanung: Vorfinanzierung Material, Abschlagsrechnungen, Sicherheitseinbehalt § 17 VOB-B, MaBV-Raten bei Bauauftraegen. Liquiditaetsspitze prüfen, Zwischenfinanzierung organisieren. |
| `sondereffekt-grossauftrag-stundungs` | Liqui Sondereffekt Grossauftrag Stundungs: prüft konkret Sondereffekt Grossauftrag in Liquiditaetsplanung, Stundungs-Strategie mit Finanzamt, Krankenkassen, Lieferanten. |
| `sonderfall-edge-case` | Liqui: Sonderfall und Edge-Case-Prüfung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahre... |
| `spezial-luecken-livequellen-und-rechtsprechungscheck` | Luecken: Livequellen- und Rechtsprechungscheck. |
| `spezial-rechtsprechung-red-team-und-qualitaetskontrolle` | Rechtsprechung: Red-Team und Qualitätskontrolle. |
| `start-chronologie-fristen` | Start, Chronologie und Fristen der Liquiditätsvorschau: Aktenaufnahme, 13-Wochen-Sicht, InsO-/StaRUG-Schwellen, Zahlungskalender und Sofortmaßnahmen. |
| `stundungs-strategie` | Stundungs-Strategie mit Finanzamt, Krankenkassen, Lieferanten: § 222 AO Stundung, Ratenzahlungsvereinbarung Krankenkasse, Lieferantenstundung. Prüfraster: wann beantragen, Mindestanforderungen Antrag, Reichweite (keine Gläubigerbenachtei... |
| `szenarien-aufbauen` | Szenarien aufbauen: Base Case, Best Case, Worst Case (mit Stresshebel: Umsatzeinbruch, Forderungsausfaelle, Lieferantenforderungen). Empfehlung: drei Szenarien mit dokumentierten Annahmen, Sensitivitaeten in Excel. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Liquiditätsplanung: trennt fehlende Tatsachen von fehlenden Belegen (Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste), nennt pro Lücke Beweisthema, Beschaffungsweg (Bank), Frist und Ers... |
| `verifikation-beweislast-darlegungslast` | Verifikation: Beweislast, Darlegungslast und Substantiierung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, S... |
| `vorschau-dokumentenmatrix-lueckenliste` | Vorschau: Dokumentenmatrix, Lückenliste und Nachforderung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sank... |
| `wochen-fristen-form-zustaendigkeit-rechtsweg` | Wochen: Fristen, Form, Zuständigkeit und Rechtsweg: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion od... |
| `wochen-liqui-ausgabengruppen-cash` | Wochen Liqui Ausgabengruppen Cash: prüft konkret Wochen, Ausgabengruppen systematisch erfassen, Cash-Pooling im Konzern. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
