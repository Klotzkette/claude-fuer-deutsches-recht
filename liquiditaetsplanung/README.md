# Liquiditätsplanung — Power-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`liquiditaetsplanung`) | [`liquiditaetsplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Edelholz Manufaktur Berlin GmbH — Liquiditäts- und Steuerakte** (`beispielakte-edelholz-berlin`) | [Gesamt-PDF lesen](../testakten/beispielakte-edelholz-berlin/gesamt-pdf/beispielakte-edelholz-berlin_gesamt.pdf) | [`testakte-beispielakte-edelholz-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beispielakte-edelholz-berlin.zip) |
| **Forschungszulage Riedblick Sensorik GmbH** (`forschungszulage-sensorik-startup-taunus`) | [Gesamt-PDF lesen](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

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

Automatisch generierte Komplett-Liste aller 68 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampel-zahlen-schwellenwerte-berechnung` | Ampel: Zahlen, Schwellenwerte und Berechnung im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwel... |
| `anschluss-routing` | Anschluss-Routing für Liquiditätsplanung: wählt den nächsten Spezial-Skill nach Engpass (Rolling 13-week-Plan, Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste), dokumentiert Router-Entscheidung mit Begründung. |
| `ausgabengruppen-fristennotiz-naechster` | Ausgabengruppen: Fristennotiz und nächster Schritt im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `ausgabengruppen-systematik` | Ausgabengruppen systematisch erfassen: Personal (Lohn, SV, LSt), Material/Wareneinsatz, Miete, Energie, Versicherungen, Beratungs-/Anwaltskosten, Steuerzahlungen, Investitionen, Zinsen, Tilgung. Vorlage Tabelle. |
| `bei-drohender-zahlungsunfaehigkeit` | Liquiditaetsplanung bei drohender Zahlungsunfaehigkeit § 18 InsO: 24-Monats-Planung, Zugang StaRUG-Restrukturierung, Geschaeftsleiterpflichten. Pruefraster und Schnittstelle Insolvenzantrag. |
| `bei-eingetretener-zahlungsunfaehigkeit` | Liquiditaetsplanung bei eingetretener Zahlungsunfaehigkeit § 17 InsO: 3-Wochen-Vorschau zur Pruefung Insolvenzantragspflicht, Liquiditaetsluecke kleiner 10 Prozent + Schliessung binnen 3 Wochen waere Liquiditaetsstockung. Pruefraster BGH... |
| `cash-pooling-konzern` | Cash-Pooling im Konzern: rechtliche Risiken Existenzvernichtung BGH II ZR 78/06, Sanierungstauglichkeit, Pruefung Avale gegen Konzerngesellschaften, Steuerrisiken § 8b KStG. Output: Cash-Pool-Risiko-Memo. |
| `chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin Liquiditaetsplanung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege l... |
| `deutschem-dokumentationspaket-excel` | Deutschem Dokumentationspaket Excel im Plugin Liquiditaetsplanung: prüft konkret Deutschem, Dokumentationspaket, Excel. |
| `deutschem-tatbestandsmerkmale-beweisfragen` | Deutschem: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zust... |
| `dokumentationspaket-bank` | Dokumentationspaket: Compliance-Dokumentation und Aktenvermerk: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `dokumente-intake` | Dokumentenintake für Liquiditätsplanung: sortiert Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste, prüft Datum, Absender, Frist und Beweiswert (Bankbestätigungen, Eingangs-/Ausgangsrechnungen); markiert Lücken; berücksi... |
| `drohender-zahlungsunfaehigkeit` | Liqui Drohender Zahlungsunfaehigkeit im Plugin Liquiditaetsplanung: prüft konkret Liquiditaetsplanung bei drohender Zahlungsunfaehigkeit § 18, Liquiditaetsplanung bei eingetretener Zahlungsunfaehigkeit, Liquiditaetsplanung für Bankgespra... |
| `eingangsdaten-checkliste` | Eingangsdaten-Checkliste für Liquiditaetsplanung: BWA, OPOS Debitoren/Kreditoren, Kontoauszuege, Steuerkonten, SV-Konten, Personalkosten, Investitionsplanung. Pruefliste Quellen und Vollstaendigkeit. Output: standardisiertes Datentemplate. |
| `eingangsdaten-idw-s6-liqp` | Liqui Eingangsdaten IDW S6 Liqp im Plugin Liquiditaetsplanung: prüft konkret Eingangsdaten-Checkliste für Liquiditaetsplanung, Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungspla, Leitfaden Bankenreporting be... |
| `einstieg-routing` | Einstieg, Triage und Routing für Liquiditätsplanung: ordnet Rolle (Geschäftsführung, Finanzen/CFO, Bank), markiert Frist (Rolling 13-week-Plan), wählt Norm (IDW S 11 (Sanierung), § 18 InsO drohende ZU) und Zuständigkeit (Bank), leitet zu... |
| `excel` | Excel: Behörden-, Gerichts- oder Registerweg im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwel... |
| `export` | Export: Schriftsatz-, Brief- und Memo-Bausteine im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Sch... |
| `export-forecast-fortbestehensprognose` | Export Forecast Fortbestehensprognose im Plugin Liquiditaetsplanung: prüft konkret Export, Forecast, Fortbestehensprognose. |
| `forecast-risikoampel-gegenargumente` | Forecast: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Z... |
| `forecast-wochenplanung` | Liquiditaetsplanung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `fortbestehensprognose-international` | Fortbestehensprognose: Internationaler Bezug und Schnittstellen im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist,... |
| `fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin Liquiditaetsplanung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege lieg... |
| `fuer-bankgespraech` | Liquiditaetsplanung für Bankgespraech: kompakte Vorlage 13 Wochen + Jahresansicht, Annahmen-Block, Sensitivitaet, Kreditlinien-Ausnutzung, Begleittext. Empfehlung: realistisch, nicht zu optimistisch, mit Fallback-Hebeln. |
| `grundbegriffe-cashflow` | Liquiditaetsplanung Grundbegriffe: Cashflow vs. Gewinn, indirekte vs. direkte Methode, Liquiditaet 1./2./3. Grades, Working Capital. Abgrenzung zur GuV-Planung. Empfehlung: direkte Methode für 13-Wochen-Forecast, indirekte für Jahresplan... |
| `grundbegriffe-cashflow-kreditlinien` | Liqui Grundbegriffe Cashflow Kreditlinien im Plugin Liquiditaetsplanung: prüft konkret Liquiditaetsplanung Grundbegriffe, Kreditlinien pruefen, Debitorenseite optimieren. |
| `idw-s6-integrierte-sanierungsplanung` | Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen... |
| `insolvenzrecht-formular-portal` | Insolvenzrecht: Formular, Portal und Einreichungslogik im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellu... |
| `insolvenzrecht-liqui-sonderfall` | Insolvenzrecht Liqui Sonderfall im Plugin Liquiditaetsplanung: prüft konkret Insolvenzrecht, Liqui, Liquiditaetsplanung. |
| `interessen-verifikation-beweislast-vorschau` | Interessen Verifikation Beweislast Vorschau im Plugin Liquiditaetsplanung: prüft konkret Schnittstellen, Verifikation, Vorschau. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Liquiditaetsplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dok... |
| `kreditlinien-pruefen` | Kreditlinien pruefen: Kontokorrent, Investitionskredit, Avalkredit, Factoring-Linie, Lieferantenkredit. Ausnutzungsgrade, Tilgungsplaene, Sicherheiten, Covenants. Pruefraster für Bankgespraech. |
| `leasing-lp-restrukturierungsplan-starug` | Liqui Leasing LP Restrukturierungsplan Starug im Plugin Liquiditaetsplanung: prüft konkret Leasing- und Lebenspartnerzahlungen in Liquiditaetsplan, Liquiditaetsplanung im Restrukturierungsplan StaRUG, Saisonalitaet erkennen. |
| `liqp-bankenreporting-leitfaden` | Leitfaden Bankenreporting bei Krise: Anforderungen Hausbank, Konsortium, KfW, Reportingfrequenz, Covenant-Reporting. Pruefraster für CFO und Berater. |
| `liqp-liquiditaetspool-cash-pooling-spezial` | Spezialfall Liquiditaetspool und Cash-Pooling im Konzern: § 30 GmbHG, BGH-Rechtsprechung, vollwertiger Rueckzahlungsanspruch. Pruefraster für Konzernmutter und Tochter. |
| `liqp-liquiditaetspool-cash-rollende-13wochen` | Liqp Liquiditaetspool Cash Rollende 13wochen im Plugin Liquiditaetsplanung: prüft konkret Spezialfall Liquiditaetspool und Cash-Pooling im Konzern, Bauleiter rollende 13-Wochen-Liquiditaetsplanung, Spezialfall Warenkredit und Skontostrat... |
| `liqp-rollende-13wochen-bauleiter` | Bauleiter rollende 13-Wochen-Liquiditaetsplanung: Einnahmen / Ausgaben / Saldo / kumulierter Saldo, Granularitaet, Update-Zyklen. Pruefraster Mittelstand und Konzerntochter. |
| `liqp-warenkredit-skonto-szenarien-spezial` | Spezialfall Warenkredit und Skontostrategien in der Krise: Lieferantenverhandlung, Vorkasse, verlaengerter Eigentumsvorbehalt, Factoring. Pruefraster für Treasury. |
| `liquiditaetsstatus-quellenbelege` | Liquiditätsstatus nur aus belastbaren Quellenbelegen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `liquiditaetsstatus-quellenbelege-live-quote` | Liquiditaetsstatus Quellenbelege Live Quote im Plugin Liquiditaetsplanung: prüft konkret Liquiditätsstatus nur aus belastbaren Quellenbelegen, Live, Quote. |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau für 3/6/12 Monate mit Fortfuehrungsprognose, Wochenraster, Excel-Export und Quellenhygiene. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-3wochen` | Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Prüfungslinie für liquiditaetsvorschau insolvenzrechtlich im Liquiditaetsplanung. |
| `live-mandantenkommunikation` | Live: Mandantenkommunikation und Entscheidungsvorlage im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellun... |
| `luecken-quellenkarte` | Luecken Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mahnstufen-debitoren` | Debitorenseite optimieren: DSO-Kennzahl, Mahnstufen, Skontostrategie, Factoring-Optionen, Forderungsausfallversicherung. Empfehlung: 3-Wochen-Forecast getrennt nach Kategorie 'sicher / wahrscheinlich / fraglich'. |
| `mandantenkommunikation` | Mandantenkommunikation im Plugin Liquiditaetsplanung: 1. Wer fragt in welcher Rolle? 2. Was ist das gewünschte Ergebnis? 3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen? 4. Welche Unterlagen, Daten oder Belege liegen... |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate im Plugin Liquiditaetsplanung: prüft konkret Mandantenkommunikation im Plugin liquiditaetsplanung, Red-Team Qualitygate im Plugin liquiditaetsplanung, Ausgabengruppen. |
| `mit-leasing-und-lp` | Leasing- und Lebenspartnerzahlungen in Liquiditaetsplan: operate lease als opex, finance lease wirkt sich auf Bilanz aus, vorzeitige Aufloesung kostenpflichtig. Empfehlung: Aufnahme nach Faelligkeit, Pruefung Beendigungskosten. |
| `output-waehlen` | Output-Wahl für Liquiditätsplanung: stimmt Adressat (Geschäftsführung, Finanzen/CFO, Bank), Frist (Rolling 13-week-Plan) und Form auf den Zweck ab — typische Outputs: 13-Wochen-Plan, 24-Monats-Plan, Cash-Pool-Aufstellung. |
| `quellen-livecheck` | Quellen-Live-Check für Liquiditätsplanung: prüft Normen (IDW S 11 (Sanierung), § 18 InsO drohende ZU) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Bank und Quellenhygiene nach references/quellenhygiene.md. |
| `quote-verhandlung-vergleich-eskalation` | Quote: Verhandlung, Vergleich und Eskalation im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwel... |
| `rechtsprechung-fehlerkatalog` | Rechtsprechung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `restrukturierungsplan-starug` | Liquiditaetsplanung im Restrukturierungsplan StaRUG: Plan-Liquiditaet, Sanierungsbeitraege Glaeubiger, Working-Capital-Plan, Cash-Out-Termine. Output: integrierter Plan und Glaeubigerverteilungsschema. |
| `saisonalitaet-erkennen` | Saisonalitaet erkennen: Vorjahres-Kontodaten gegen Liquiditaetsplan abgleichen, Monats- und Wochenmuster, Sondereffekte (Inventur, Jahresabschluss, Ferien). Empfehlung: saisonale Korrekturfaktoren je Branche. |
| `schnittstellen-mehrparteienkonflikt` | Schnittstellen: Mehrparteienkonflikt und Interessenmatrix im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `sondereffekt-grossauftrag` | Sondereffekt Grossauftrag in Liquiditaetsplanung: Vorfinanzierung Material, Abschlagsrechnungen, Sicherheitseinbehalt § 17 VOB-B, MaBV-Raten bei Bauauftraegen. Liquiditaetsspitze pruefen, Zwischenfinanzierung organisieren. |
| `sondereffekt-grossauftrag-stundungs` | Liqui Sondereffekt Grossauftrag Stundungs im Plugin Liquiditaetsplanung: prüft konkret Sondereffekt Grossauftrag in Liquiditaetsplanung, Stundungs-Strategie mit Finanzamt, Krankenkassen, Lieferanten. |
| `sonderfall-edge-case` | Liqui: Sonderfall und Edge-Case-Prüfung im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Z... |
| `start-chronologie-fristen` | Start Chronologie Fristen im Plugin Liquiditaetsplanung: prüft konkret Einstieg, Schnelltriage und Fallrouting im Liquiditaetsplanung-Plugin, Chronologie und Belegmatrix im Plugin liquiditaetsplanung, Fristen- und Risikoampel im Plugin l... |
| `stundungs-strategie` | Stundungs-Strategie mit Finanzamt, Krankenkassen, Lieferanten: § 222 AO Stundung, Ratenzahlungsvereinbarung Krankenkasse, Lieferantenstundung. Pruefraster: wann beantragen, Mindestanforderungen Antrag, Reichweite (keine Glaeubigerbenacht... |
| `szenarien-aufbauen` | Szenarien aufbauen: Base Case, Best Case, Worst Case (mit Stresshebel: Umsatzeinbruch, Forderungsausfaelle, Lieferantenforderungen). Empfehlung: drei Szenarien mit dokumentierten Annahmen, Sensitivitaeten in Excel. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Liquiditätsplanung: trennt fehlende Tatsachen von fehlenden Belegen (Liquiditätsplan, Bankenstatus, Forderungs-/Verbindlichkeitenliste), nennt pro Lücke Beweisthema, Beschaffungsweg (Bank), Frist und Ers... |
| `verifikation-beweislast-darlegungslast` | Verifikation: Beweislast, Darlegungslast und Substantiierung im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zu... |
| `vorschau-dokumentenmatrix-lueckenliste` | Vorschau: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zuste... |
| `wochen-fristen-form-zustaendigkeit-rechtsweg` | Wochen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin Liquiditaetsplanung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung,... |
| `wochen-liqui-ausgabengruppen-cash` | Wochen Liqui Ausgabengruppen Cash im Plugin Liquiditaetsplanung: prüft konkret Wochen, Ausgabengruppen systematisch erfassen, Cash-Pooling im Konzern. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
