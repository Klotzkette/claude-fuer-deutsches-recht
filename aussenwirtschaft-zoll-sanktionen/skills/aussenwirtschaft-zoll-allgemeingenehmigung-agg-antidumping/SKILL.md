---
name: aussenwirtschaft-zoll-allgemeingenehmigung-agg-antidumping
description: "Allgemeingenehmigung AGG Antidumping: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Allgemeingenehmigung AGG Antidumping

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Allgemeingenehmigung AGG Antidumping** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-allgemeingenehmigung-agg-finder` | Allgemeine Genehmigungen nach AWV: Auffinden und Pruefen der passenden Allgemeingenehmigung (AGG) fuer kontrollierte Ausfuhren ohne Einzelgenehmigung. Beruecksichtigt EU-Ausfuhrgenehmigungen (001-009 VO 2021/821), nationale AGGs der AWV und BAFA-Merkblaetter. Mandant liefert Ware/Technologie und Zielland; Skill ermittelt passende AGG, prueft Bedingungen und Registrierungspflichten. Output: AGG-Zuordnungsvermerk mit Nutzungsbedingungen. |
| `aussenwirtschaft-antidumping-ausgleich` | Antidumping-Ausgleichsmassnahmen nach EU-Grundverordnung (VO (EU) 2016/1036): Identifizierung von TARIC-Antidumping-Massnahmen, Berechnung endgueltiger Antidumping-Zoelle, Ueberpruefen von Ursprungsnachweis und Hersteller-TARIC-Code (Einzelzoll vs. Restzoll). Fallkonstellation: Importeur prueft Antidumping-Risiko bei Stahlimport aus China. Output: Antidumping-Belastungsuebersicht und Erlaeuterungsschreiben. |
| `aussenwirtschaft-antidumping-erstattung-review` | Erstattung zu viel gezahlter Antidumping-Zoelle und Auslosung von Revisionsverfahren nach Art. 11 VO (EU) 2016/1036: Rueckerstattungsantrag (Art. 11 Abs. 8), Interim-Review und Sunset-Review. Prueft Fristen beim Hauptzollamt und EU-Kommission. Fallkonstellation: Importeur hat ueberhohten Antidumping-Zoll gezahlt und moechte Erstattung oder Margenkorrektur. Output: Erstattungsantrag mit Kalkulationsnachweis. |
| `aussenwirtschaft-antidumping-taric-massnahmen` | Identifizierung und Anwendung handelspolitischer Schutzmassnahmen (Antidumping, Ausgleichszoll, Safeguards) im TARIC-System: Zuordnung der KN-Position, Ursprungsland und Hersteller zu geltenden Massnahmen. Ermittelt TARIC-Zusatzcode, Preisverpflichtungen und Schwellenwerte fuer relevante Waren. Output: TARIC-Massnahmen-Uebersicht mit Handlungsempfehlung fuer Zollabfertigung. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Allgemeingenehmigung AGG Antidumping**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-allgemeingenehmigung-agg-finder`

**Fokus:** Allgemeine Genehmigungen nach AWV: Auffinden und Pruefen der passenden Allgemeingenehmigung (AGG) fuer kontrollierte Ausfuhren ohne Einzelgenehmigung. Beruecksichtigt EU-Ausfuhrgenehmigungen (001-009 VO 2021/821), nationale AGGs der AWV und BAFA-Merkblaetter. Mandant liefert Ware/Technologie und Zielland; Skill ermittelt passende AGG, prueft Bedingungen und Registrierungspflichten. Output: AGG-Zuordnungsvermerk mit Nutzungsbedingungen.

# Allgemeine Genehmigungen: Finder und Nutzungsbedingungen fuer Exportkontrolle

## Mandantenfall

- Maschinenhersteller moechte Ersatzteile in USA liefern; Frage ob EU001 (NATO) anwendbar.
- Elektroniklieferant fragt, ob EU007 (Forschung und Entwicklung) fuer Technologielieferung in die Schweiz gilt.
- KMU prueft, ob nationale AGG 29 fuer Lieferung bestimmter Gueter nach Israel nutzbar ist.

## Erste Schritte

1. Gueterlistenklassifizierung feststellen (Anhang I VO 2021/821, ECCN, Dual-Use-Code).
2. Zielland und Endverwender (Regierung, Zivil, Militaer) bestimmen.
3. Alle EU-Allgemeingenehmigungen EU001-EU009 systematisch durchpruefen.
4. Nationale Allgemeingenehmigungen (AWV) fuer nicht von EU-Regelung erfasste Faelle pruefen.
5. Bedingungen der anwendbaren AGG pruefen: Ausschluesse, Exporteurdokumentation, Registrierung.
6. Registrierungspflicht beim BAFA beachten und Nutzungslog anlegen.

## Rechtsrahmen

- **Art. 12 VO (EU) 2021/821**: Rahmenbedingungen EU-Allgemeingenehmigungen (EU001-EU009).
- **Anhang II VO (EU) 2021/821**: Texte der einzelnen EU-Ausfuhrgenehmigungen.
- **§§ 2, 8 AWG**: Genehmigungstatbestand und Ausnahmen fuer genehmigte Ausfuhr.
- **§§ 8 ff. AWV**: Nationale Allgemeingenehmigungen.
- **BAFA-Merkblatt Allgemeine Genehmigungen**: Anwendungshinweise.

## Pruef-Raster

- [ ] Gueterlistencode vollstaendig ermittelt?
- [ ] Zielland-Ausschlusslisten jeder AGG einzeln geprueft?
- [ ] Endverwender-Einschraenkungen der AGG (kein Militaer, keine WMD-Nutzung) geprueft?
- [ ] Registrierungspflicht beim BAFA beachtet?
- [ ] Nachweisdokumentation fuer Compliance-Zwecke angelegt?
- [ ] AGG-Nutzung im Export-Management-System vermerkt?

## Typische Fallstricke

- EU-Allgemeingenehmigungen schliessen bestimmte Laender explizit aus; Ausschlusslisten aktuell pruefen.
- Registrierungspflicht bei EU002/EU003 wird oft vergessen.
- AGG deckt keine Embargosituationen ab; vorrangige Embargopruefen erforderlich.
- Nationale AWV-AGGs koennen durch spaeteres EU-Recht ueberholt sein.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

AGG-Zuordnungsvermerk mit anwendbarer Genehmigung, Nutzungsbedingungen, Ausschlussliste und Nachweis-Template fuer Compliance-Ordner.

## Quellen

- [VO (EU) 2021/821 mit Anhang II auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Allgemeine Genehmigungen](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Allgemeine_Genehmigungen/allgemeine_genehmigungen_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-antidumping-ausgleich`

**Fokus:** Antidumping-Ausgleichsmassnahmen nach EU-Grundverordnung (VO (EU) 2016/1036): Identifizierung von TARIC-Antidumping-Massnahmen, Berechnung endgueltiger Antidumping-Zoelle, Ueberpruefen von Ursprungsnachweis und Hersteller-TARIC-Code (Einzelzoll vs. Restzoll). Fallkonstellation: Importeur prueft Antidumping-Risiko bei Stahlimport aus China. Output: Antidumping-Belastungsuebersicht und Erlaeuterungsschreiben.

# Antidumping-Ausgleich: TARIC-Massnahmen und Herstellerzuordnung

## Mandantenfall

- Importeur kauft Solarpaneele aus China; TARIC-Abfrage zeigt Antidumping-Massnahmen. Welcher Zollsatz gilt?
- Stahlhaendler erhaelt Nachzollbescheid, weil Ursprungsnachweise des chinesischen Lieferanten nicht anerkannt.
- Unternehmen importiert Keramik aus Vietnam; fragt nach Antidumping-Risiko und Nullzoll-Optionen.

## Erste Schritte

1. TARIC-Datenbank (ec.europa.eu/taxation_customs/dds2/taric) aufrufen: Massnahmen fuer KN-Code und Ursprungsland pruefen.
2. Hersteller-ID und TARIC-Unternehmenscode (TARIC ADD-Code) des Lieferanten ermitteln.
3. Individualzoll vs. Restzoll klaeren; Ursprungszeugnis und EU-Anerkennungsstatus pruefen.
4. Antidumping-Zoll auf CIF-Wert berechnen; Vergleich mit eventueller Preisverpflichtung (Price Undertaking).
5. Ueberpruefen ob Befreiungsantrag moeglich (Art. 11 VO 2016/1036: Auslaufrevision).
6. Zollwertdeklaration und Ursprungsdokumentation fuer Audit-Compliance sicherstellen.

## Rechtsrahmen

- **VO (EU) 2016/1036**: EU-Antidumping-Grundverordnung (Methodik und Verfahren).
- **Art. 1-2 VO 2016/1036**: Dumping-Definition und Schadenstest.
- **UZK Art. 56-63**: Zolltarifanwendung und Praeferenzketten.
- **VO (EU) 952/2013 Art. 59-63**: Ursprungsbestimmung fuer Antidumpingzwecke.
- **AWG § 21**: Verfahrensbeteiligung bei Handelspolitikuntersuchungen.

## Pruef-Raster

- [ ] TARIC-Massnahmen fuer exakten KN-Code und Ursprungsland aktuell geprueft?
- [ ] Hersteller-TARIC-Code gueltig und anerkannt?
- [ ] Ursprungsnachweis zulaessig und nachweisbar?
- [ ] CIF-Wert korrekt fuer Antidumping-Berechnungsgrundlage?
- [ ] Preisverpflichtung (Price Undertaking) aktiv und nutzbar?
- [ ] Rueckerstattungsantrag bei Dumping-Margin-Review moeglich?

## Typische Fallstricke

- TARIC-Massnahmen aendern sich durch Revisionen und Auslaufverfahren laufend; immer tagesaktuelle Abfrage.
- Zusammengesetzte Waren: Antidumpingzoll kann an Bestandteil haengen, nicht am Endprodukt.
- Hersteller-ID des Lieferanten nicht geprueft: Restzoll statt Individualzoll wird faellig.
- Umgehungsrisiko bei Transhipment ueber Drittlaender.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Antidumping-Belastungsuebersicht mit Zollsatz je Hersteller, Ursprungsnachweis-Checkliste, Kalkulationsblatt und Strategieempfehlung (Review-Antrag/Umgehungsvermeidung).

## Quellen

- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [TARIC-Datenbank Europaeische Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Antidumping](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollrechtliche-Einfuhrbestimmungen/Besondere-Einfuhrabgaben/besondere-einfuhrabgaben_node.html)

## 3. `aussenwirtschaft-antidumping-erstattung-review`

**Fokus:** Erstattung zu viel gezahlter Antidumping-Zoelle und Auslosung von Revisionsverfahren nach Art. 11 VO (EU) 2016/1036: Rueckerstattungsantrag (Art. 11 Abs. 8), Interim-Review und Sunset-Review. Prueft Fristen beim Hauptzollamt und EU-Kommission. Fallkonstellation: Importeur hat ueberhohten Antidumping-Zoll gezahlt und moechte Erstattung oder Margenkorrektur. Output: Erstattungsantrag mit Kalkulationsnachweis.

# Antidumping-Erstattung und Review: Margenkorrektur und Rueckforderung

## Mandantenfall

- Importeur hat in den letzten drei Jahren Antidumping-Zoelle gezahlt; moechte pruefen, ob tatsaechliches Dumping nachgewiesen wurde.
- Hersteller in China hat Dumping-Marge signifikant reduziert; Lieferant moechte Review-Antrag stellen.
- Massnahme gegen bestimmten Warenwert laeuft in 12 Monaten aus; Frage nach Sunset-Review und Auswirkungen.

## Erste Schritte

1. Pruefen ob Erstattungsantrag nach Art. 11 Abs. 8 VO 2016/1036 in Frage kommt (Zoll bezahlt, Exportpreis gestiegen).
2. Antrag auf Erstattung beim Hauptzollamt (DE) und koordiniert mit EU-Kommission einreichen.
3. Interim-Review-Antrag (Art. 11 Abs. 3) bei geaenderter Dumping-Situation des Exporteurs.
4. Sunset-Review-Antrag (Art. 11 Abs. 2) bei Auslauf der Massnahme vorbereiten.
5. Preisvergleich und Dumping-Margin-Dokumentation fuer Review aufbereiten.
6. Fristen beachten: Erstattungsantrag innerhalb 6 Monate nach Zollzahlung.

## Rechtsrahmen

- **Art. 11 VO (EU) 2016/1036**: Erstattung, Interim-Review, Sunset-Review und Neuzulassung.
- **Art. 11 Abs. 8 VO 2016/1036**: Erstattungsantragsverfahren bei gesunkenem Exportpreis.
- **UZK Art. 116-123**: Allgemeines Zollerstattungsrecht.
- **Art. 21 UZK-IA**: Antragstellung und Fristen fuer Zollerstattung.
- **§ 21 ZollVG**: Nationale Kontrollbefugnisse.

## Pruef-Raster

- [ ] Zollzahlung dokumentiert und innerhalb der Erstattungsfrist (6 Monate)?
- [ ] Exportpreis nach Erhebung des Antidumping-Zolls gestiegen?
- [ ] Dumping-Margin-Berechnung und Preisvergleich aufbereitet?
- [ ] Interim-Review-Antrag oder Sunset-Review-Antrag sinnvoll?
- [ ] Koordination mit EU-Kommission eingeplant?
- [ ] Zollbescheide und Einfuhrdokumentation vollstaendig gesichert?

## Typische Fallstricke

- Erstattungsantrag muss koordiniert mit Hauptzollamt und Kommission gestellt werden.
- Sunset-Review-Antrag hat strenge Fristen; bei Versaeumnis bleiben Massnahmen automatisch in Kraft.
- Beweislast fuer gesunkenem Exportpreis liegt beim Importeur; unzureichende Dokumentation fuehrt zu Ablehnung.
- Preisverpflichtungsbruch des Exporteurs kann Erstattungsantrag gefaehrden.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Erstattungsantrag mit Exportpreisvergleich und Dumping-Kalkulation, Interim-Review-Antrag, Fristen-Uebersicht und Verfahrensstrategie.

## Quellen

- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [UZK Art. 116-123 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [EU Kommission Antidumping-Verfahren](https://ec.europa.eu/trade/policy/accessing-markets/trade-defence/actions-against-imports-into-the-eu/anti-dumping/)
- [Zoll.de Erstattungen](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollanmeldung-Zollverfahren/Erstattung-Erlass/erstattung-erlass_node.html)

## 4. `aussenwirtschaft-antidumping-taric-massnahmen`

**Fokus:** Identifizierung und Anwendung handelspolitischer Schutzmassnahmen (Antidumping, Ausgleichszoll, Safeguards) im TARIC-System: Zuordnung der KN-Position, Ursprungsland und Hersteller zu geltenden Massnahmen. Ermittelt TARIC-Zusatzcode, Preisverpflichtungen und Schwellenwerte fuer relevante Waren. Output: TARIC-Massnahmen-Uebersicht mit Handlungsempfehlung fuer Zollabfertigung.

# TARIC-Massnahmen: Antidumping und Ausgleichszoelle in der Zollabfertigung

## Mandantenfall

- Zollagent findet beim Import von Stahlrohren aus China drei konkurrierende Massnahmen-Codes in TARIC.
- Importeur zahlt falsche Antidumping-Zoelle weil Hersteller-TARIC-Code veraltet.
- Unternehmen importiert Fahrraeder aus Kambodscha; Frage ob EU-Antiumgehungsmassnahme greift.

## Erste Schritte

1. KN-8-Steller und Ursprungsland klar bestimmen; TARIC-Abfrage mit aktueller Fassung.
2. Alle gueltigen Massnahmen (ADD, CVD, Safeguard, Surveillance) fuer den Code auflisten.
3. Hersteller-Code (TARIC ADD-Zusatzcode) beim Lieferanten erfragen und validieren.
4. Preisverpflichtungen (Price Undertakings) und Mindestimportpreise pruefen.
5. Freimengen und Zollkontingente (TRQ) pruefen, falls Massnahme-Ausnahmen bestehen.
6. Massnahmen-Stand in Dokumentation vermerken (Datum, TARIC-Version).

## Rechtsrahmen

- **UZK Art. 56 Abs. 2**: Massnahmen des Gemeinsamen Zolltarifs inkl. Antidumping.
- **VO (EU) 2016/1036**: Antidumping-Grundverordnung.
- **VO (EU) 2016/1037**: Ausgleichszoll-Grundverordnung (Subventionen).
- **VO (EU) 2015/478**: Gemeinsame Einfuhrregelung und Safeguards.
- **Durchfuehrungsverordnungen**: Einzelne ADD- und CVD-Massnahmen per Durchfuehrungs-VO.

## Pruef-Raster

- [ ] KN-Code und Ursprungsland korrekt fuer TARIC-Abfrage?
- [ ] Alle aktiven Massnahmen (ADD, CVD, Safeguard) aufgelistet?
- [ ] Hersteller-TARIC-Code validiert und nicht gesperrt?
- [ ] Preisverpflichtungs-Compliance dokumentiert?
- [ ] Freimengen/Kontingente (TRQ) geprueft?
- [ ] Massnahmen-Stand mit Datum protokolliert?

## Typische Fallstricke

- TARIC-Datenbank mit Stand-Datum nutzen; keine Offline-Auszuege aus Vormonat.
- Mehrere parallele Massnahmen (ADD + CVD + Safeguard) sind kumulativ anwendbar.
- Hersteller-ID kann sich durch Fusionen oder Rueckzug der Anerkennung aendern.
- Massnahmen gelten per Einreihung; marginale Unterschiede im KN-Code vermeiden.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

TARIC-Massnahmen-Tabelle mit ADD-/CVD-Zusatzcodes, Hersteller-Zuordnung, Preisverpflichtungsstatus und Zollberechnungsblatt.

## Quellen

- [TARIC-Datenbank der EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [VO (EU) 2016/1037 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1037)
- [Zoll.de Besondere Einfuhrabgaben](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollrechtliche-Einfuhrbestimmungen/Besondere-Einfuhrabgaben/besondere-einfuhrabgaben_node.html)
