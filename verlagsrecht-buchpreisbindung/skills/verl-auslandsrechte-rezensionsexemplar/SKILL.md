---
name: verl-auslandsrechte-rezensionsexemplar
description: "Verl 038 Auslandsrechte Sanktionen Exportkontrolle, Verl 030 Rezensionsexemplar Influencer Und Steuer: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 038 Auslandsrechte Sanktionen Exportkontrolle, Verl 030 Rezensionsexemplar Influencer Und Steuer

## Arbeitsbereich

Dieser Skill bündelt **Verl 038 Auslandsrechte Sanktionen Exportkontrolle, Verl 030 Rezensionsexemplar Influencer Und Steuer** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-038-auslandsrechte-sanktionen-exportkontrolle` | Verlagsrecht: Auslandsrechte, Sanktionsregimes und Exportkontrolle — EU-Sanktionen, US-OFAC, verbotene Lizenznehmer, Due Diligence und Compliance-Anforderungen für internationale Lizenzverträge. |
| `verl-030-rezensionsexemplar-influencer-und-steuer` | Verlagsrecht: Rezensionsexemplare, Influencer-Kooperationen und steuerliche Behandlung — BuchPrG § 6, Einkommensteuer, Umsatzsteuer, Kennzeichnungspflichten (UWG, TMG). |

## Arbeitsweg

Für **Verl 038 Auslandsrechte Sanktionen Exportkontrolle, Verl 030 Rezensionsexemplar Influencer Und Steuer** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-038-auslandsrechte-sanktionen-exportkontrolle`

**Fokus:** Verlagsrecht: Auslandsrechte, Sanktionsregimes und Exportkontrolle — EU-Sanktionen, US-OFAC, verbotene Lizenznehmer, Due Diligence und Compliance-Anforderungen für internationale Lizenzverträge.

# Verl-038 · Auslandsrechte, Sanktionen und Exportkontrolle

## Zweck dieses Skills

Verlage, die Lizenzen an ausländische Verlage vergeben, müssen **Sanktionsrecht** und Exportkontrolle beachten. Lizenzen an Verlage in sanktionierten Ländern (z.B. Russland, Iran, Nordkorea) können gegen EU-Sanktionsverordnungen oder US-OFAC-Regelungen verstoßen. Dieser Skill klärt die Compliance-Anforderungen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| EU-Sanktionsverordnungen | z.B. VO (EU) Nr. 833/2014 (Russland), Nr. 267/2012 (Iran) | https://eur-lex.europa.eu |
| AWG § 4 | Außenwirtschaftsgesetz: Verbotene Geschäfte | https://www.gesetze-im-internet.de/awg/__4.html |
| AWV | Außenwirtschaftsverordnung: Genehmigungspflichten | https://www.gesetze-im-internet.de/awv/ |
| US OFAC Regulations | US-Sanktionslisten (SDN List) | https://ofac.treasury.gov |
| GWG §§ 10 ff. | Geldwäschegesetz: Sorgfaltspflichten | https://www.gesetze-im-internet.de/gwg_2017/ |
| StGB §§ 34, 18 | Außenwirtschaftsstrafrecht | https://dejure.org/gesetze/AWG/18.html |

## Sanktionsrecht und Buchrechte: Grundlagen

### Was sind Sanktionen?
- Sanktionen sind staatliche oder internationale Maßnahmen, die wirtschaftliche Transaktionen mit bestimmten Ländern, Unternehmen oder Personen verbieten.
- **EU-Sanktionen**: Verordnungen des Rates der EU; unmittelbar anwendbar in allen Mitgliedstaaten.
- **US-OFAC**: Office of Foreign Assets Control; US-Sanktionen haben extraterritoriale Wirkung (betreffen auch deutsche Verlage bei US-Dollar-Zahlungen oder US-Verträgen).

### Sind Buchlizenzen Sanktionsgegenstand?
- Grundsatz: Kulturelle Güter (Bücher, Lizenzen) sind häufig **ausgenommen** von Sanktionen.
- Ausnahmen:
 - Technologietransfer (Dual-Use-Güter: Bücher mit militärischen oder nuklearen Inhalten).
 - Lizenzen an sanktionierte Personen (SDN-Liste, EU-Sanktionsliste).
 - Zahlungen in sanktionierten Währungen oder über sanktionierten Finanzinstitute.

## EU-Sanktionen: Russland (Beispiel VO 833/2014)

### Verbotene Transaktionen
- Zahlungen an von der EU gelistete russische Personen und Organisationen.
- Technologietransfer (technische Spezifikationsbücher, Dual-Use-Materialien).

### Buchlizenzen in der Praxis
- Kulturelle Ausnahmen: Bücher als solche sind i.d.R. nicht verbotene Güter.
- **Zahlungsweg**: Auch wenn Buch erlaubt, kann Zahlungstransfer über russische Banken blockiert sein.
- **Listung des Lizenznehmers**: Wenn russischer Verlag auf SDN- oder EU-Sanktionsliste → Vertrag verboten.

### Sorgfaltspflichten (GWG § 10)
- Verlag muss Geschäftspartner auf Sanktionslisten prüfen (Know-Your-Customer, KYC).
- Screening-Tools: EU-Sanktionsliste (EUR-Lex), US-SDN-Liste (OFAC), nationale Sanktionslisten.
- Dokumentation: KYC-Prüfung dokumentieren; Ergebnis aufbewahren.

## US-OFAC: Extraterritoriale Wirkung

- Deutschen Verlage, die USD-Zahlungen empfangen oder US-Korrespondenzbanken nutzen, können US-Sanktionen unterfallen.
- **OFAC-SDN-Liste**: Specially Designated Nationals — jede Transaktion mit gelisteten Personen ist für US-Personen und oft auch Nicht-US-Personen verboten.
- Deutsche Verlage: Direkte Anwendbarkeit zweifelhaft; aber USD-Clearing durch US-Banken kann OFAC-Compliance erfordern.
- **Secondary Sanctions**: US kann Sanktionen gegen Nicht-US-Unternehmen verhängen, die mit sanktionierten Ländern Geschäfte machen.

## Due-Diligence-Checkliste für Auslandslizenzen

### Schritt 1: Ländercheck
- Ist das Zielland von EU- oder US-Sanktionen betroffen?
- Ist das Zielland auf FATF-Grauer oder -Schwarzer Liste (Geldwäscherisiko)?

### Schritt 2: Lizenznehmers-Screening
- Lizenznehmers-Name und Eigentümerstruktur prüfen.
- Screening gegen EU-Sanktionsliste, US-SDN-Liste, Interpol-Liste.
- PEP-Screening (Politically Exposed Persons).

### Schritt 3: Vertragsdokumentation
- Zahlungswährung und Zahlungsweg: EUR über SEPA sicher; USD über US-Korrespondenzbank prüfen.
- Vertragsklausel: „Lizenzgeber und Lizenznehmer bestätigen, keiner Sanktionsliste zu unterfallen. Bei Aufnahme auf Sanktionsliste: sofortige Vertragsauflösung."
- Sanktionsklausel: Vertrag erlischt automatisch bei Listung einer Partei.

### Schritt 4: Monitoring
- Laufende Überwachung: Sind Vertragsparteien nach Vertragsschluss gelistet worden?
- Jährliches Re-Screening.

## Dual-Use-Bücher

- Dual-Use: Waren, Software, Technologien, die zivil und militärisch genutzt werden können.
- Einschlägig für Verlage: Technische Handbücher, Chemie, Biotechnologie, Kryptographie-Bücher.
- EU-Dual-Use-VO (VO (EU) 2021/821): Ausführgenehmigungspflicht für gelistete Güter.
- Bücher als solche: Nur in Extremfällen Dual-Use; aber Know-how-Transfer kann relevant sein.

## Typische Fallen

- **Sanktions-Listing nach Vertragsschluss**: Russischer Verlag wird kurz nach LOI auf Sanktionsliste gesetzt → bestehender Vertrag muss beendet werden; aufgelaufene Advance-Zahlungen blockiert.
- **USD-Zahlungsweg und US-Banken**: Verlag akzeptiert USD-Advance; Zahlung über US-Korrespondenzbank → OFAC-Compliance-Problem.
- **KYC-Dokumentation fehlt**: Behördenprüfung zeigt, dass Verlag keine Sanktionsscreening-Dokumentation geführt hat → GWG-Bußgeld.
- **Dual-Use-Buch nicht erkannt**: Technisches Handbuch mit Anwendungen für Waffensysteme → Exportgenehmigung erforderlich.

## Checkliste Auslandslizenzen Sanktions-Compliance

- [ ] Zielland auf Sanktionsliste geprüft (EU, US-OFAC)
- [ ] Lizenznehmers-Screening: EU-Sanktionsliste, SDN-Liste, PEP
- [ ] Zahlungswährung und -weg geprüft (kein USD über US-Banken bei sanktioniertem Land)
- [ ] Sanktionsklausel im Lizenzvertrag
- [ ] KYC-Dokumentation aufbewahrt
- [ ] Dual-Use-Relevanz des Werkes geprüft
- [ ] Jahres-Re-Screening geplant

## Quellenreferenzen

- EU-Sanktionsliste: https://eur-lex.europa.eu/content/sanctions/sanctions.html
- US-OFAC SDN-Liste: https://ofac.treasury.gov/sanctions-list-search
- AWG: https://www.gesetze-im-internet.de/awg/
- EU Dual-Use-VO 2021/821: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821
- GWG: https://www.gesetze-im-internet.de/gwg_2017/

## Output-Formate

- **Sanktions-Screening-Protokoll**: Ergebnis je Vertragspartner dokumentiert
- **Sanktionsklausel-Muster** für Lizenzverträge
- **Länder-Risikomatrix**: Sanktions- und Exportkontrollrisiko je Zielmarkt
- **KYC-Dokumentationsvorlage**
- **Dual-Use-Prüfprotokoll** für technische Werke

## 2. `verl-030-rezensionsexemplar-influencer-und-steuer`

**Fokus:** Verlagsrecht: Rezensionsexemplare, Influencer-Kooperationen und steuerliche Behandlung — BuchPrG § 6, Einkommensteuer, Umsatzsteuer, Kennzeichnungspflichten (UWG, TMG).

# Verl-030 · Rezensionsexemplare, Influencer und Steuer

## Zweck dieses Skills

Verlage versenden **Rezensionsexemplare** an Presse, Buchblogger und Influencer. Diese Praxis berührt Buchpreisbindungsrecht (Ausnahme für Rezensenten), Steuerrecht (Sachzuwendungen) und Wettbewerbsrecht (Kennzeichnungspflichten). Dieser Skill klärt alle relevanten Dimensionen.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| BuchPrG § 6 | Ausnahmen; Rezensionsexemplare nicht ausdrücklich, aber nach h.M. erfasst | https://www.gesetze-im-internet.de/buchprg/__6.html |
| EStG § 37b | Pauschalsteuer auf Sachzuwendungen an Nichtarbeitnehmer | https://www.gesetze-im-internet.de/estg/__37b.html |
| EStG § 8 | Sachbezüge als geldwerte Vorteile | https://www.gesetze-im-internet.de/estg/__8.html |
| UStG § 3 Abs. 1b | Unentgeltliche Zuwendungen als steuerpflichtige Lieferung | https://www.gesetze-im-internet.de/ustg_1980/__3.html |
| UWG § 5a | Unlautere Geschäftspraktiken: fehlende Kennzeichnung | https://dejure.org/gesetze/UWG/5a.html |
| TMG § 6 | Werbung im Internet: Kennzeichnungspflicht | https://www.gesetze-im-internet.de/tmg/__6.html |
| MStV § 22 | Kennzeichnung kommerzieller Kommunikation (Medienstaatsvertrag) | https://www.gesetze-im-internet.de/mstv/ |

## Rezensionsexemplare und Buchpreisbindung

### Rechtliche Einordnung
- Rezensionsexemplare werden unentgeltlich an Rezensenten (Presse, Blogger) abgegeben.
- BuchPrG gilt für **entgeltliche** Abgabe; unentgeltliche Abgabe → kein Buchpreisbindungsverstoß.
- Aber: Wenn Verlag Buch formell kostenlos gibt, aber faktisch eine Gegenleistung erwartet (bezahlte Rezension) → kommerzielles Arrangement → andere steuerliche und wettbewerbsrechtliche Behandlung.

### Praktische Abgrenzung
- Echtes Rezensionsexemplar: Kein Preis; keine vertraglich vereinbarte Pflicht zur Rezension; Verlag akzeptiert auch negative Kritik.
- Influencer-Kooperation mit Publikationspflicht: Gegenleistung (Rezension) → Vertragsverhältnis; kein reines Rezensionsexemplar.

## Steuerliche Behandlung

### Sachzuwendung an Rezensenten (EStG § 37b)
- Bücher, die Verlag an externe Personen (Journalisten, Blogger) verschenkt: Grundsätzlich Sachzuwendung (EStG § 8 Abs. 2).
- **EStG § 37b**: Verlag kann auf Sachzuwendungen an Nichtarbeitnehmer Pauschalsteuer von 30 % übernehmen.
- Freigrenze: 10.000 € je Empfänger und Jahr für Pauschalsteuer nach § 37b EStG.
- Unterhalb der Freigrenze (§ 8 Abs. 3 EStG, 50 € / Monat): Kein steuerpflichtiger geldwerter Vorteil.

### Umsatzsteuerliche Behandlung
- Unentgeltliche Buchlieferung als Sachzuwendung: Grundsätzlich steuerpflichtige „unentgeltliche Lieferung" (UStG § 3 Abs. 1b).
- Ausnahme: Bücher als Werbemittel (keine Umsatzsteuer, wenn keine selbständige Nutzungsmöglichkeit).
- **Praktisch**: Buchhandels-Rezensionsexemplare im üblichen Umfang sind als Betriebsausgabe abzugsfähig; USt fällt nicht an, wenn Werbezweck dominiert.

### Buchführung
- Rezensionsexemplar-Versand dokumentieren: Empfänger, Wert, Datum, Zweck.
- Betriebsausgabenabzug: Belege aufbewahren.

## Influencer-Kooperationen

### Kennzeichnungspflichten
- **UWG § 5a, TMG § 6, MStV § 22**: Werbung im Internet muss als solche erkennbar sein.
- Wenn Verlag Buch kostenlos (oder vergünstigt) zur Verfügung stellt und Influencer darüber postet:
 - Hat der Influencer eine vertraglich gesicherte Pflicht zur Rezension → Werbung; **Pflicht zur Kennzeichnung** als „#Werbung" oder „#Anzeige".
 - Verlag hat dem Influencer eine Publikation erleichtert oder empfohlen → möglicherweise Werbung.
 - Freiwillige Rezension ohne jede Absprache → keine Kennzeichnungspflicht.

### BGH-Rechtsprechung
- BGH, Urteil vom 09.09.2021 - I ZR 126/20: Influencer-/Instagram-Tap-Tag-Konstellation; Kennzeichnungspflichten hängen insbesondere von Gegenleistung, werblichem Überschuss und Erkennbarkeit des kommerziellen Zwecks ab. Nicht als „Burg Schreckenstein" oder pauschale Schleichwerbungsregel zitieren.
- Kennzeichnung erforderlich bei: kostenlosen Produkten, Vergünstigungen, Reiseeinladungen.

### Vertragsgestaltung mit Influencern
1. Kooperationsvertrag: Klare Pflichten (Anzahl Posts, Zeitraum, Inhalte).
2. **Kennzeichnungspflicht vertraglich festhalten**: Influencer verpflichtet sich zur korrekten Werbekennzeichnung.
3. Freistellungsklausel: Influencer stellt Verlag bei Kennzeichnungsverstößen frei.
4. Keine Pflicht zu positiver Kritik: Influencer darf das Buch negativ rezensieren.

## Presserechtliche Aspekte

- Klassische Pressekritiken unterliegen Meinungsfreiheit (GG Art. 5); kein Anspruch auf positive Bewertung.
- Verlag darf Rezensenten nicht wegen negativer Kritik abmahnen.
- Wenn Rezension unwahre Tatsachen enthält: Widerrufs- und Unterlassungsanspruch (§ 823 BGB i.V.m. § 824 BGB).

## Typische Fallen

- **Influencer kennzeichnet nicht**: Blogger erhält kostenloses Buch und postet ohne „Werbung"-Hinweis → UWG-Verstoß; Abmahnung durch Wettbewerber.
- **Steuer auf Rezensionsexemplare vergessen**: Verlag überschreitet 50-€-Freigrenze je Empfänger; steuerpflichtige Sachzuwendung nicht deklariert → Lohnsteuer-Nachprüfung.
- **Kooperationsvertrag fordert positive Kritik**: Klausel unwirksam; ggf. sittenwidrig und Schleichwerbungsrisiko.
- **Rezensionsexemplare für Bibliotheken zum Kauf angeboten**: Wenn Verlag Rezensionsexemplare über Plattform verkauft → Buchpreisbindung wieder einschlägig.

## Checkliste Rezensionsexemplar / Influencer

- [ ] Versandliste mit Empfänger, Titel, Datum gepflegt
- [ ] Kooperationsvertrag enthält Kennzeichnungspflicht
- [ ] Steuerliche Behandlung (§ 37b EStG) geprüft; ggf. Pauschalsteuer gewählt
- [ ] Keine Verpflichtung zur positiven Kritik im Kooperationsvertrag
- [ ] Influencer-Posts auf korrekte Kennzeichnung überprüft
- [ ] Betriebsausgabenabzug dokumentiert

## Quellenreferenzen

- EStG § 37b: https://www.gesetze-im-internet.de/estg/__37b.html
- UWG § 5a: https://dejure.org/gesetze/UWG/5a.html
- TMG § 6: https://www.gesetze-im-internet.de/tmg/__6.html
- BGH, Urteil vom 09.09.2021 - I ZR 126/20: Influencer-/Instagram-Tap-Tag-Konstellation; vor Zitat amtliche/frei zugängliche Quelle prüfen.
- MStV § 22: https://www.gesetze-im-internet.de/mstv/

## Output-Formate

- **Kooperationsvertrag-Muster**: Influencer, Pflichten, Kennzeichnung, Freistellung
- **Steuerberechnungssheet**: Sachzuwendungen × 30 % Pauschalsteuer
- **Kennzeichnungsleitfaden** für Influencer-Kooperationspartner
- **Rezensionsexemplar-Dokumentationsformular**
- **Compliance-Check** Social-Media-Posts auf korrekte Kennzeichnung
