---
name: db-policy-db-abschlussmemo
description: "DB Policy DB Abschlussmemo: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# DB Policy DB Abschlussmemo

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **DB Policy DB Abschlussmemo** im Plugin Datenbankrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `db-063-datenbankrecht-compliance-policy` | Erstellung und Prüfung unternehmensinterner Compliance-Richtlinien für den Umgang mit fremden und eigenen Datenbanken: §§ 87a-87e UrhG (Herstellerrecht), § 4 UrhG (Datenbankwerk), RL 96/9/EG, TDM-Schranken §§ 44b, 60d UrhG, Data Act 2023/2854. Mandant benötigt eine rechtssichere Data-Governance-Policy, Nutzungsgenehmigungsverfahren, Schulungskonzept und internes Audit-Framework. Output: Policy-Entwurf, Freigabe-Workflow, Checkliste für Einkauf und IT. |
| `db-064-datenbankrecht-abschlussmemo` | Erstellung eines strukturierten Abschlussmemos nach Abschluss einer datenbankrechlichen Beratung: Zusammenfassung der Rechtslage nach §§ 87a-87e UrhG und § 4 UrhG, RL 96/9/EG, relevanter EuGH-Urteile (BHB/William Hill C-203/02, Apis/Lakorda C-545/07, Innoweb/Wegener C-202/12), getroffener Maßnahmen, offener Risiken und Empfehlungen. Output: mandantenfähiges Abschlussmemo mit Risikomatrix, Handlungsempfehlungen, Monitoring-Plan und Wiedervorlageterminen. |

## Arbeitsweg

Im Plugin Datenbankrecht gilt für **DB Policy DB Abschlussmemo**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `db-063-datenbankrecht-compliance-policy`

**Fokus:** Erstellung und Prüfung unternehmensinterner Compliance-Richtlinien für den Umgang mit fremden und eigenen Datenbanken: §§ 87a-87e UrhG (Herstellerrecht), § 4 UrhG (Datenbankwerk), RL 96/9/EG, TDM-Schranken §§ 44b, 60d UrhG, Data Act 2023/2854. Mandant benötigt eine rechtssichere Data-Governance-Policy, Nutzungsgenehmigungsverfahren, Schulungskonzept und internes Audit-Framework. Output: Policy-Entwurf, Freigabe-Workflow, Checkliste für Einkauf und IT.

# Datenbankrecht Compliance-Policy: Data Governance, Freigabeverfahren, Schulung

## Mandantenfall

- Ein Softwareunternehmen möchte eine unternehmensweite Richtlinie für den Zugriff auf externe Datenbanken und Daten-Feeds einführen, nachdem eine Abmahnung wegen unbefugten Scrapings eingegangen ist.
- Ein Konzern führt eine M&A-Integration durch und muss sicherstellen, dass die übernommene Datenbank-Nutzungspraxis des Targets mit den eigenen Compliance-Standards vereinbar ist.
- Ein Forschungsinstitut erstellt nach Förderauflagen eine Open-Data-Policy und muss das Verhältnis zwischen eigenen Datenbankrechten und Open-Access-Verpflichtungen klären.

## Erste Schritte

1. **Bestandsaufnahme Datenbanknutzung**: Inventarisierung aller genutzten externen Datenbanken, APIs, Daten-Feeds und Scraping-Prozesse; Erfassung vorhandener Lizenzverträge, Nutzungsbedingungen und interner Zugangstechnik.
2. **Rechtliche Risikoklassifizierung**: Jede Datenquelle nach Schutzstatus bewerten (Datenbankwerk § 4 UrhG, Herstellerrecht §§ 87a-87e UrhG, keine Schutzfähigkeit) und Nutzungsumfang gegen erlaubte Schranken prüfen (§§ 44b, 60d UrhG, eigene Lizenz).
3. **Freigabe-entwerfen**: Mehrstufiges Genehmigungsverfahren: (a) IT prüft technische Zugriffsmethode, (b) Legal prüft Schutzstatus und Lizenzabdeckung, (c) Freigabe durch Data-Owner dokumentiert in einem zentralen Register.
4. **Policy-Entwurf erstellen**: Gliederung mit Geltungsbereich, Definitionen (Datenbank, wesentliche Entnahme, TDM), verbotene Handlungen, erlaubte Nutzung, Meldepflichten intern, Sanktionen bei Verstoß.
5. **Schulungskonzept**: Awareness-Training für IT, Produkt, Einkauf und Legal; Fallbeispiele aus EuGH-Rechtsprechung (BHB/William Hill C-203/02, Innoweb/Wegener C-202/12); jährliche Auffrischung.
6. **Audit-Mechanismus**: Quartalsweise Stichproben aus Zugriffslogs; jährliche Vollprüfung durch Internal Audit; externe Rechtsanwaltsprüfung alle zwei Jahre.

## Rechtsrahmen

- **§ 87b Abs. 1 UrhG** — Verbot der Entnahme oder Weiterverwendung wesentlicher Teile der Datenbank ohne Zustimmung; Grundlage für interne Verbotskatalog der Policy.
- **§ 44b UrhG** — Text-und-Data-Mining als Schranke: erlaubt für alle Nutzer, sofern Rightsholders kein maschinenlesbares Opt-out gesetzt haben; Policy muss Opt-out-Prüfpflicht abbilden.
- **§ 60d UrhG** — TDM für wissenschaftliche Forschung: privilegiert, aber nur nicht-kommerzielle Zwecke; Policy für Forschungseinrichtungen muss Zweckbindung sicherstellen.
- **Art. 6 RL 96/9/EG** — Rechtmäßiger Nutzer darf unwesentliche Teile entnehmen; vertragliche Einschränkungen dieser Schranke sind unwirksam.
- **Data Act VO 2023/2854, Art. 4-6** — Zugangs- und Weitergaberechte für IoT-generierte Daten; Policy muss Data-Act-Pflichten bei vernetzten Produkten abdecken.
- **§ 307 BGB** — AGB-Kontrolle für in der Policy enthaltene Beschränkungen gegenüber Mitarbeitern und Lieferanten; unangemessene Benachteiligung ist unwirksam.

## Prüfraster

- Sind alle externen Datenquellen im zentralen Datenbankregister erfasst und mit Schutzstatus versehen?
- Existiert für jede Quelle eine schriftliche Lizenz oder eine dokumentierte Schrankenprüfung (§§ 44b, 60d UrhG)?
- Ist der Freigabe-klar definiert (wer genehmigt was, in welcher Frist, wie dokumentiert)?
- Bildet die Policy die Opt-out-Prüfpflicht nach § 44b Abs. 3 UrhG ab (robots.txt, maschinenlesbarer Hinweis)?
- Sind Sanktionen bei Policy-Verstößen (Abmahnung, Kündigung, Kostenerstattung) arbeitsrechtlich wirksam vereinbart?
- Wird die Policy mindestens jährlich auf neue Rechtsentwicklungen (EuGH-Urteile, Gesetzesänderungen) aktualisiert?
- Ist ein Eskalationspfad für Zweifelsfälle und Drittansprüche (Abmahnung, einstweilige Verfügung) definiert?
- Deckt die Policy auch die eigenen Datenbanken des Unternehmens ab (Schutz nach außen, Lizenzierung, Durchsetzung)?

## Typische Fallstricke

- **Shadow-IT-Lücken**: Fachbereiche greifen ohne Legal-Freigabe auf externe Daten-APIs zu; Policy muss explizit auch inoffizielle Tools (Browser-Extensions, No-Code-Plattformen) erfassen.
- **Schranken-Irrtum**: Mitarbeiter glauben, öffentlich zugängliche Daten seien frei verwendbar; Policy muss klar stellen, dass Öffentlichkeit keinen Schutz aufhebt.
- **Opt-out ignoriert**: TDM-Schranke (§ 44b UrhG) gilt nicht, wenn der Rechtsinhaber ein maschinenlesbares Opt-out gesetzt hat; fehlende robots.txt-Prüfroutine ist Compliance-Lücke.
- **Veraltete Lizenzregister**: Datenbanklizenzen laufen ab oder ändern sich; ohne Ablaufdaten im Register entstehen unbemerkt Rechtsverletzungen.
- **Fehlende Mitarbeiterkommunikation**: Eine Policy ohne Schulung und Awareness ist im Streitfall schwer als wirksam durchgesetzt nachzuweisen.

## Output

- Compliance-Policy-Entwurf (Datenbankrecht und Data Governance) als Word-Dokument
- Zentrales Datenbankregister-Template (Excel/CSV: Quelle, Schutzstatus, Lizenz, Ablaufdatum, Freigabe)
- Freigabe-Workflow-Diagramm (Swimlane: IT, Legal, Data-Owner)
- Opt-out-Prüf-Checkliste für externe Datenquellen (robots.txt, AGB, maschinenlesbarer Hinweis)
- Schulungsfolien-Grundgerüst (10-15 Folien: Grundbegriffe, Fallbeispiele, Dos and Don'ts)
- Audit-Fragebogen für jährliche Compliance-Prüfung

## Quellen

- [§ 87b UrhG — Rechte des Datenbankherstellers (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__87b.html)
- [§ 44b UrhG — Text und Data Mining (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__44b.html)
- [§ 60d UrhG — TDM für Wissenschaft (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__60d.html)
- [RL 96/9/EG — Datenbankrichtlinie (eur-lex.europa.eu)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [Data Act VO 2023/2854 (eur-lex.europa.eu)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [EuGH C-202/12 Innoweb/Wegener — Meta-Suchdienst als Entnahme (curia.europa.eu)](https://curia.europa.eu/juris/liste.jsf?num=C-202/12)

## 2. `db-064-datenbankrecht-abschlussmemo`

**Fokus:** Erstellung eines strukturierten Abschlussmemos nach Abschluss einer datenbankrechlichen Beratung: Zusammenfassung der Rechtslage nach §§ 87a-87e UrhG und § 4 UrhG, RL 96/9/EG, relevanter EuGH-Urteile (BHB/William Hill C-203/02, Apis/Lakorda C-545/07, Innoweb/Wegener C-202/12), getroffener Maßnahmen, offener Risiken und Empfehlungen. Output: mandantenfähiges Abschlussmemo mit Risikomatrix, Handlungsempfehlungen, Monitoring-Plan und Wiedervorlageterminen.

# Datenbankrecht Abschlussmemo: Rechtslage, Maßnahmen, offene Risiken

## Mandantenfall

- Nach Abschluss eines Verletzungsverfahrens (Abmahnung, einstweilige Verfügung, Unterlassungsvertrag) möchte der Mandant eine schriftliche Zusammenfassung der Rechtslage, der getroffenen Maßnahmen und der verbleibenden Risiken.
- Am Ende einer M&A-Due-Diligence zu Datenbankrechten soll ein Abschlussmemo alle Feststellungen, Bewertungen und Deal-Bedingungen dokumentieren.
- Ein Forschungsprojekt endet; Drittmittelgeber und Hochschulleitung benötigen eine rechtliche Zusammenfassung der Datenbankrechte an den erhobenen Forschungsdaten sowie Empfehlungen zur weiteren Nutzung.

## Erste Schritte

1. **Sachverhalt strukturieren**: Ausgangslage, Mandanteninteressen, Verfahrens- oder Beratungsverlauf in chronologischer Reihenfolge darstellen; relevante Datenbanken und Parteien benennen.
2. **Rechtliche Bewertung zusammenfassen**: Schutzfähigkeit der Datenbank(en) nach §§ 87a, 4 UrhG, Verletzungshandlungen nach § 87b UrhG, angewandte EuGH-Maßstäbe und nationale Rechtsprechung kompakt darlegen.
3. **Maßnahmen dokumentieren**: Welche Schritte wurden unternommen (Abmahnung, Sicherung, Lizenzvertrag, technische Maßnahmen, Behördenmeldung)? Ergebnisse und Stand der Durchsetzung festhalten.
4. **Risikomatrix erstellen**: Verbleibende Risiken (laufende Verfahren, ungeklärte Rechtsfragen, vertragliche Restrisiken) nach Eintrittswahrscheinlichkeit und Schadenspotenzial klassifizieren.
5. **Handlungsempfehlungen formulieren**: Kurzfristige (sofort), mittelfristige (3-6 Monate) und langfristige (12+ Monate) Empfehlungen zu Prävention, Lizenzierung, Compliance-Maßnahmen, Monitoring.
6. **Wiedervorlagetermine setzen**: Fristen für Vertragsverlängerungen, Überprüfung von Unterlassungsverpflichtungen, Ablauf von Schutzfristen (15 Jahre § 87d UrhG), geplante Rechtsänderungen (Data Act-Umsetzung) kalendarisch festhalten.

## Rechtsrahmen

- **§ 87a UrhG** — Schutzvoraussetzungen: wesentliche Investition in Beschaffung, Überprüfung oder Darstellung; 15-jährige Schutzfrist nach § 87d UrhG.
- **§ 87b UrhG** — Verbotene Handlungen: Entnahme oder Weiterverwendung wesentlicher Teile; wiederholte systematische Entnahme unwesentlicher Teile.
- **§ 87e UrhG** — Unwirksamkeit vertraglicher Einschränkungen der Schranken für rechtmäßige Nutzer; relevant für Lizenzklauseln im Abschlussmemo.
- **Art. 7 RL 96/9/EG** — Europäische Grundlage des Herstellerrechts; EuGH-Auslegungshoheit bei Zweifelsfragen zu Investition und Entnahme.
- **EuGH C-203/02 BHB/William Hill** — Investition muss in Beschaffung/Überprüfung vorhandener Daten bestehen, nicht in Datenerzeugung; Maßstab für Schutzfähigkeitsanalyse im Memo.
- **§ 97 Abs. 2 UrhG** — Schadensersatz: tatsächlicher Schaden, Herausgabe des Verletzergewinns oder Lizenzanalogie; Berechnungsmethode im Memo dokumentieren.

## Prüfraster

- Ist die rechtliche Schutzfähigkeitsbewertung der Datenbank(en) abschließend dokumentiert (wesentliche Investition, Abgrenzung Datenerzeugung vs. Beschaffung)?
- Sind alle festgestellten Verletzungshandlungen mit Datum, Umfang und Beweismitteln erfasst?
- Ist die angewandte Schadensberechnungsmethode (Lizenzanalogie, Verletzergewinn, tatsächlicher Schaden) begründet und nachvollziehbar?
- Enthält das Memo alle getroffenen Vereinbarungen (Unterlassungsverträge, Lizenzverträge, Vergleiche) mit Vertragsparteien, Datum und wesentlichen Pflichten?
- Sind verbleibende offene Risiken (z.B. parallele Verfahren, unklar ob Opt-out nach § 44b UrhG wirksam) explizit als solche ausgewiesen?
- Sind Wiedervorlagetermine (Schutzfristablauf § 87d UrhG, Vertragslaufzeiten, gesetzliche Überprüfungsklauseln) im Memo kalendarisch hinterlegt?
- Ist das Memo mandantenseitig freigegeben und versioniert abgelegt?

## Typische Fallstricke

- **Schutzfristablauf übersehen**: Die 15-Jahres-Frist des § 87d UrhG beginnt neu bei wesentlichen Erweiterungen; ohne Monitoring entfällt der Schutz unbemerkt.
- **Unvollständige Maßnahmendokumentation**: Mündliche Absprachen oder informelle Einigungen fehlen im Memo; im Streitfall nicht nachweisbar.
- **Risiken als gelöst darstellen**: Offene Fragen (z.B. ob eine Handlung tatsächlich unwesentliche Teile betraf) sollten explizit als offen ausgewiesen werden, nicht verschwiegen.
- **Fehlende Anschlussberatung**: Abschlussmemo endet ohne klare Empfehlung zur nächsten Handlung; Mandant bleibt ohne Orientierung für Folgerisiken.
- **Vertraulichkeit**: Memos mit Risikoeinschätzungen dürfen nicht in Discovery oder behördlichen Verfahren auftauchen; Schutz durch Legal-Privilege prüfen und hinweisen.

## Output

- Abschlussmemo (8-15 Seiten): Sachverhalt, Rechtsbewertung, Maßnahmen, Ergebnis
- Risikomatrix (Tabelle: Risiko, Eintrittswahrscheinlichkeit, Schadenspotenzial, Maßnahme, Verantwortlich)
- Handlungsempfehlungen (kurzfristig, mittelfristig, langfristig)
- Wiedervorlage-Kalender (Fristen, Termine, Zuständigkeiten)
- Anlagenverzeichnis (Verträge, Beweismittel, Korrespondenz, gerichtliche Entscheidungen)

## Quellen

- [§ 87a UrhG — Datenbankherstellerrecht (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__87a.html)
- [§ 87d UrhG — Schutzdauer (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__87d.html)
- [§ 97 UrhG — Unterlassung und Schadensersatz (gesetze-im-internet.de)](https://www.gesetze-im-internet.de/urhg/__97.html)
- [RL 96/9/EG — Datenbankrichtlinie Art. 7 (eur-lex.europa.eu)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)
- [EuGH C-203/02 BHB/William Hill — Investitionsbegriff (curia.europa.eu)](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [EuGH C-545/07 Apis/Lakorda — Datenextraktion (curia.europa.eu)](https://curia.europa.eu/juris/liste.jsf?num=C-545/07)
