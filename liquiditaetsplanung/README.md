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

Automatisch generierte Komplett-Liste aller 69 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ausgabengruppen-fristennotiz-naechster` | Ausgabengruppen: Fristennotiz und nächster Schritt: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `deutschem-dokumentationspaket-excel` | Deutschem Tatbestand Beweis Und Belege, Dokumentationspaket Compliance Dokumentation Und Akte, Excel Behörden Gericht Und Registerweg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den... |
| `export-forecast-fortbestehensprognose` | Export Schriftsatz Brief Und Memo Bausteine, Forecast Risikoampel Und Gegenargumente, Fortbestehensprognose International Schnittstellen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert d... |
| `fortbestehensprognose-international` | Fortbestehensprognose: Internationaler Bezug und Schnittstellen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `idw-s6-integrierte-sanierungsplanung` | Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen... |
| `insolvenzrecht-liqui-sonderfall` | Insolvenzrecht Formular Portal Und Einreichung, Liqui Sonderfall Und Edge Case, Liquiditaetsplanung Erstpruefung Und Mandatsziel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächs... |
| `interessen-verifikation-beweislast-vorschau` | Schnittstellen Mehrparteien Konflikt Und Interessen, Verifikation Beweislast Und Darlegungslast, Vorschau Dokumentenmatrix Und Lueckenliste: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefer... |
| `liqp-bankenreporting-leitfaden` | Leitfaden Bankenreporting bei Krise: Anforderungen Hausbank, Konsortium, KfW, Reportingfrequenz, Covenant-Reporting. Pruefraster fuer CFO und Berater. |
| `liqp-liquiditaetspool-cash-pooling-spezial` | Spezialfall Liquiditaetspool und Cash-Pooling im Konzern: § 30 GmbHG, BGH-Rechtsprechung, vollwertiger Rueckzahlungsanspruch. Pruefraster fuer Konzernmutter und Tochter. |
| `liqp-liquiditaetspool-cash-rollende-13wochen` | Liqp Liquiditaetspool Cash Pooling Spezial, Liqp Rollende 13wochen Bauleiter, Liqp Warenkredit Skonto Szenarien Spezial: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belas... |
| `liqp-rollende-13wochen-bauleiter` | Bauleiter rollende 13-Wochen-Liquiditaetsplanung: Einnahmen / Ausgaben / Saldo / kumulierter Saldo, Granularitaet, Update-Zyklen. Pruefraster Mittelstand und Konzerntochter. |
| `liqp-warenkredit-skonto-szenarien-spezial` | Spezialfall Warenkredit und Skontostrategien in der Krise: Lieferantenverhandlung, Vorkasse, verlaengerter Eigentumsvorbehalt, Factoring. Pruefraster fuer Treasury. |
| `liqui-ausgabengruppen-systematik` | Ausgabengruppen systematisch erfassen: Personal (Lohn, SV, LSt), Material/Wareneinsatz, Miete, Energie, Versicherungen, Beratungs-/Anwaltskosten, Steuerzahlungen, Investitionen, Zinsen, Tilgung. Vorlage Tabelle. |
| `liqui-bei-drohender-zahlungsunfaehigkeit` | Liquiditaetsplanung bei drohender Zahlungsunfaehigkeit § 18 InsO: 24-Monats-Planung, Zugang StaRUG-Restrukturierung, Geschaeftsleiterpflichten. Pruefraster und Schnittstelle Insolvenzantrag. |
| `liqui-bei-eingetretener-zahlungsunfaehigkeit` | Liquiditaetsplanung bei eingetretener Zahlungsunfaehigkeit § 17 InsO: 3-Wochen-Vorschau zur Pruefung Insolvenzantragspflicht, Liquiditaetsluecke kleiner 10 Prozent + Schliessung binnen 3 Wochen waere Liquiditaetsstockung. Pruefraster BGH... |
| `liqui-cash-pooling-konzern` | Cash-Pooling im Konzern: rechtliche Risiken Existenzvernichtung BGH II ZR 78/06, Sanierungstauglichkeit, Pruefung Avale gegen Konzerngesellschaften, Steuerrisiken § 8b KStG. Output: Cash-Pool-Risiko-Memo. |
| `liqui-drohender-zahlungsunfaehigkeit` | Liqui Bei Drohender Zahlungsunfaehigkeit, Liqui Bei Eingetretener Zahlungsunfaehigkeit, Liqui Für Bankgespraech: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren O... |
| `liqui-eingangsdaten-checkliste` | Eingangsdaten-Checkliste fuer Liquiditaetsplanung: BWA, OPOS Debitoren/Kreditoren, Kontoauszuege, Steuerkonten, SV-Konten, Personalkosten, Investitionsplanung. Pruefliste Quellen und Vollstaendigkeit. Output: standardisiertes Datentemplate. |
| `liqui-eingangsdaten-idw-s6-liqp` | Liqui Eingangsdaten Checkliste, Idw S6 Integrierte Sanierungsplanung, Liqp Bankenreporting Leitfaden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liqui-fuer-bankgespraech` | Liquiditaetsplanung fuer Bankgespraech: kompakte Vorlage 13 Wochen + Jahresansicht, Annahmen-Block, Sensitivitaet, Kreditlinien-Ausnutzung, Begleittext. Empfehlung: realistisch, nicht zu optimistisch, mit Fallback-Hebeln. |
| `liqui-grundbegriffe-cashflow` | Liquiditaetsplanung Grundbegriffe: Cashflow vs. Gewinn, indirekte vs. direkte Methode, Liquiditaet 1./2./3. Grades, Working Capital. Abgrenzung zur GuV-Planung. Empfehlung: direkte Methode fuer 13-Wochen-Forecast, indirekte fuer Jahrespl... |
| `liqui-grundbegriffe-cashflow-kreditlinien` | Liqui Grundbegriffe Cashflow, Liqui Kreditlinien Prüfen, Liqui Mahnstufen Debitoren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liqui-kreditlinien-pruefen` | Kreditlinien pruefen: Kontokorrent, Investitionskredit, Avalkredit, Factoring-Linie, Lieferantenkredit. Ausnutzungsgrade, Tilgungsplaene, Sicherheiten, Covenants. Pruefraster fuer Bankgespraech. |
| `liqui-leasing-lp-restrukturierungsplan-starug` | Liqui Mit Leasing Und Lp, Liqui Restrukturierungsplan Starug, Liqui Saisonalitaet Erkennen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liqui-mahnstufen-debitoren` | Debitorenseite optimieren: DSO-Kennzahl, Mahnstufen, Skontostrategie, Factoring-Optionen, Forderungsausfallversicherung. Empfehlung: 3-Wochen-Forecast getrennt nach Kategorie 'sicher / wahrscheinlich / fraglich'. |
| `liqui-mit-leasing-und-lp` | Leasing- und Lebenspartnerzahlungen in Liquiditaetsplan: operate lease als opex, finance lease wirkt sich auf Bilanz aus, vorzeitige Aufloesung kostenpflichtig. Empfehlung: Aufnahme nach Faelligkeit, Pruefung Beendigungskosten. |
| `liqui-restrukturierungsplan-starug` | Liquiditaetsplanung im Restrukturierungsplan StaRUG: Plan-Liquiditaet, Sanierungsbeitraege Glaeubiger, Working-Capital-Plan, Cash-Out-Termine. Output: integrierter Plan und Glaeubigerverteilungsschema. |
| `liqui-saisonalitaet-erkennen` | Saisonalitaet erkennen: Vorjahres-Kontodaten gegen Liquiditaetsplan abgleichen, Monats- und Wochenmuster, Sondereffekte (Inventur, Jahresabschluss, Ferien). Empfehlung: saisonale Korrekturfaktoren je Branche. |
| `liqui-sondereffekt-grossauftrag` | Sondereffekt Grossauftrag in Liquiditaetsplanung: Vorfinanzierung Material, Abschlagsrechnungen, Sicherheitseinbehalt § 17 VOB-B, MaBV-Raten bei Bauauftraegen. Liquiditaetsspitze pruefen, Zwischenfinanzierung organisieren. |
| `liqui-sondereffekt-grossauftrag-stundungs` | Liqui Sondereffekt Grossauftrag, Liqui Stundungs Strategie, Liqui Szenarien Aufbauen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liqui-sonderfall-edge-case` | Liqui: Sonderfall und Edge-Case-Prüfung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liqui-stundungs-strategie` | Stundungs-Strategie mit Finanzamt, Krankenkassen, Lieferanten: § 222 AO Stundung, Ratenzahlungsvereinbarung Krankenkasse, Lieferantenstundung. Pruefraster: wann beantragen, Mindestanforderungen Antrag, Reichweite (keine Glaeubigerbenacht... |
| `liqui-szenarien-aufbauen` | Szenarien aufbauen: Base Case, Best Case, Worst Case (mit Stresshebel: Umsatzeinbruch, Forderungsausfaelle, Lieferantenforderungen). Empfehlung: drei Szenarien mit dokumentierten Annahmen, Sensitivitaeten in Excel. |
| `liquiditaetsplanung-ampel-zahlen-schwellenwerte-berechnung` | Ampel: Zahlen, Schwellenwerte und Berechnung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `liquiditaetsplanung-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-deutschem-tatbestandsmerkmale-beweisfragen` | Deutschem: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-dokumentationspaket-bank` | Dokumentationspaket: Compliance-Dokumentation und Aktenvermerk: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `liquiditaetsplanung-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `liquiditaetsplanung-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `liquiditaetsplanung-excel` | Excel: Behörden-, Gerichts- oder Registerweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-export` | Export: Schriftsatz-, Brief- und Memo-Bausteine: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-forecast-risikoampel-gegenargumente` | Forecast: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-forecast-wochenplanung` | Liquiditaetsplanung: Erstprüfung, Rollenklärung und Mandatsziel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-fristen-und-risikoampel` | Fristen- und Risikoampel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-insolvenzrecht-formular-portal` | Insolvenzrecht: Formular, Portal und Einreichungslogik: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Liquiditaetsplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dok... |
| `liquiditaetsplanung-liquiditaetsvorschau-3wochen` | Liquiditaetsvorschau 3wochen / Liquiditaetsvorschau Insolvenzrechtlich / Spezial Ampel Zahlen Schwellen Berechnung: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren O... |
| `liquiditaetsplanung-live-mandantenkommunikation` | Live: Mandantenkommunikation und Entscheidungsvorlage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-mandantenkommunikation` | Mandantenkommunikation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation, Redteam Qualitygate, Ausgabengruppen Fristennotiz Und Naechster Schritt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liquiditaetsplanung-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `liquiditaetsplanung-quote-verhandlung-vergleich-eskalation` | Quote: Verhandlung, Vergleich und Eskalation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `liquiditaetsplanung-schnittstellen-mehrparteienkonflikt` | Schnittstellen: Mehrparteienkonflikt und Interessenmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-start-chronologie-fristen` | Kaltstart, Chronologie, Belegmatrix und Fristenampel, ...: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liquiditaetsplanung-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `liquiditaetsplanung-vorschau-dokumentenmatrix-lueckenliste` | Vorschau: Dokumentenmatrix, Lückenliste und Nachforderung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsplanung-wochen-fristen-form-zustaendigkeit-rechtsweg` | Wochen: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `liquiditaetsstatus-quellenbelege` | Liquiditätsstatus nur aus belastbaren Quellenbelegen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `liquiditaetsstatus-quellenbelege-live-quote` | Liquiditaetsstatus Quellenbelege, Live Mandantenkommunikation Entscheidungsvorlage, Quote Verhandlung Vergleich Und Eskalation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächste... |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau fuer 3/6/12 Monate mit Fortfuehrungsprognose, Wochenraster, Excel-Export und Quellenhygiene. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-3wochen` | Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Arbeitsmodul zu liquiditaetsvorschau insolvenzrechtlich: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `luecken-quellenkarte` | Luecken Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsprechung-fehlerkatalog` | Rechtsprechung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `verifikation-beweislast-darlegungslast` | Verifikation: Beweislast, Darlegungslast und Substantiierung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `wochen-liqui-ausgabengruppen-liqui-cash` | Wochen Fristen Form Und Zustaendigkeit, Liqui Ausgabengruppen Systematik, Liqui Cash Pooling Konzern: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
