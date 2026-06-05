---
name: zolltarif-vzta-zollwert-royalties-ursprung
description: "Zolltarif Vzta Zollwert Royalties Ursprung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zolltarif Vzta Zollwert Royalties Ursprung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Zolltarif Vzta Zollwert Royalties Ursprung** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-zolltarif-vzta` | Zolltarifrecht und verbindliche Zolltarifauskuenfte (vZTA) nach UZK Art. 33: Systematik der Kombinierten Nomenklatur EU-Zolltarif TARIC Allgemeine Praeferenzsystem (APS/GSP) und Zollaussetzungen. Verfahren zur Erlangung von Zollbeguenstigungen und deren Kumulierung. Output: Zolltarif-Optimierungsanalyse und vZTA-Strategie. |
| `aussenwirtschaft-zollwert-royalties-assists` | Zollwerterhöhungen durch Lizenzgebuehren (Royalties) und Assists nach UZK Art. 71: Pruefung ob Lizenz als Verkaufsbedingung gilt und Hinzurechnung zum Transaktionswert. Assists (unentgeltliche Beistellungen wie Werkzeuge Muster Technologie) und deren Bewertung. Risiko rueckwirkender Zollnacherhebung. Output: Zollwert-Analyse mit Royalty-Pruefpfad. |
| `aussenwirtschaft-zollwert-ursprung` | Zusammenhang von Zollwert und Ursprung bei der Einfuhr: Praeferenzieller und nichtpraeferenzieller Ursprung als Zollwert-Einflussfaktor und Nachweis-Anforderungen. Zollwertberichtigung bei nachtraeglichen Ursprungsnachweisen und REX-Erklaerungen. Kombinierte Pruefung Zollwert-Ursprung bei Zollaußenpruefungen. Output: Integrierte Zollwert-Ursprungs-Pruefmatrix. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Zolltarif Vzta Zollwert Royalties Ursprung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-zolltarif-vzta`

**Fokus:** Zolltarifrecht und verbindliche Zolltarifauskuenfte (vZTA) nach UZK Art. 33: Systematik der Kombinierten Nomenklatur EU-Zolltarif TARIC Allgemeine Praeferenzsystem (APS/GSP) und Zollaussetzungen. Verfahren zur Erlangung von Zollbeguenstigungen und deren Kumulierung. Output: Zolltarif-Optimierungsanalyse und vZTA-Strategie.

# Zolltarifrecht und vZTA: Systematik APS und Zolloptimierung

## Mandantenfall

- Importeur fragt ob Ursprungsland-Wechsel zu Praeferenzland Zollersparnis ermoeglicht.
- Unternehmen nutzt autonome Zollaussetzung nach VO (EU) 2021/2267; Antrag stellen oder verlaengern.
- Exporteur in Entwicklungsland fragt ob EU-APS-Praeferenz genutzt werden kann.

## Erste Schritte

1. TARIC-Abfrage: Zollsaetze Praeferenzregelungen Zollaussetzungen und Kontingente fuer HS-Code pruefen.
2. APS/GSP-Berechtigung pruefen: Ist Ursprungsland beguenstigtes Land? GSP Basis EBA DFQF?
3. Zollaussetzungen pruefen: Autonome Aussetzungen nach VO 2021/2267 fuer Industrierohstoffe.
4. Praeferenzkalkulation: Regel des hinreichenden Umwands und spezifische Listenregeln pruefen.
5. vZTA-Strategie: Bei Unsicherheit vZTA beantragen fuer Planungssicherheit.
6. Zolltarif-Optimierungsanalyse: Vergleich verschiedener Einreihungsoptionen und Praeferenzoptimierung.

## Rechtsrahmen

- **VO (EWG) 2658/87 (KN-VO)**: Kombinierte Nomenklatur als EU-Zolltarif.
- **VO (EU) 978/2012 (GSP-VO)**: Allgemeines Praeferenzsystem der EU.
- **UZK Art. 33-37**: Verbindliche Zolltarifauskuenfte.
- **VO (EU) 2021/2267**: Autonome Zollaussetzungen fuer bestimmte Industrieerzeugnisse.
- **UZK Art. 56-58**: Zolltarif und Anwendung von Praeferenzregelungen.

## Pruef-Raster

- [ ] TARIC-Abfrage durchgefuehrt und alle Praeferenzen erfasst?
- [ ] APS-Berechtigung des Ursprungslandes geprueft?
- [ ] Zollaussetzungen auf Anwendbarkeit geprueft?
- [ ] Praeferenzkalkulation durchgefuehrt?
- [ ] vZTA-Strategie fuer Unsicherheitsfaelle bewertet?
- [ ] Zolltarif-Optimierungspotenzial quantifiziert?

## Typische Fallstricke

- APS-Praeferenzen benoetigen korrekte Ursprungsnachweise; fehlende Dokumente kosten die Praeferenz.
- Zollaussetzungen sind jedes Jahr neu zu beantragen und nicht automatisch.
- Kumulierung von Praeferenzursprungsregeln zwischen Partnerlaendern komplex; Fehler kosten Praeferenz.
- TARIC aktualisiert sich taeglich; Abfrage vor jeder Anmeldung empfohlen.

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

Zolltarif-Optimierungsanalyse mit Praeferenzvergleich, Zollaussetzungs-Kalender und vZTA-Antragsberatung.

## Quellen

- [TARIC-Datenbank EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [VO (EU) 978/2012 (GSP) auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R0978)
- [UZK Art. 33 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Zolltarif](https://www.zoll.de/DE/Fachthemen/Zoelle/Zolltarif/zolltarif_node.html)

## 2. `aussenwirtschaft-zollwert-royalties-assists`

**Fokus:** Zollwerterhöhungen durch Lizenzgebuehren (Royalties) und Assists nach UZK Art. 71: Pruefung ob Lizenz als Verkaufsbedingung gilt und Hinzurechnung zum Transaktionswert. Assists (unentgeltliche Beistellungen wie Werkzeuge Muster Technologie) und deren Bewertung. Risiko rueckwirkender Zollnacherhebung. Output: Zollwert-Analyse mit Royalty-Pruefpfad.

# Zollwert: Lizenzgebuehren Assists und Hinzurechnungen nach UZK Art. 71

## Mandantenfall

- Konzern liefert Lizenzgebuehr an verbundene Markengesellschaft; Zollamt fordert Hinzurechnung zum Zollwert.
- Importeur stellt Produktionswerkzeuge dem Auslandslieferanten unentgeltlich bei; Zollwert pruefen.
- Markenlizenz fuer Wiederverkauf: Ist Lizenz als Verkaufsbedingung fuer Import zu qualifizieren?

## Erste Schritte

1. Vertragslage klaren: Welche Lizenzgebuehren werden im Zusammenhang mit der importierten Ware gezahlt?
2. Verkaufsbedingung-Test: Wuerde Verkauf ohne Lizenzzahlung stattfinden? UZK-DA Art. 136-140 anwenden.
3. Assists identifizieren: Welche Beistellungen (Werkzeuge Software Muster) erhaelt Lieferant unentgeltlich?
4. Bewertung der Assists: Kosten der Herstellung oder Anschaffung anteilig kalkulieren.
5. Hinzurechnungs-Kalkulation: Lizenz + Assists zum Transaktionswert addieren.
6. Rueckwirkungs-Risiko quantifizieren: Bisher nicht hinzugerechnete Betraege und Nacherhebungsfristen pruefen.

## Rechtsrahmen

- **UZK Art. 70**: Transaktionswert als primaere Zollwertmethode.
- **UZK Art. 71 Abs. 1 lit. c**: Hinzurechnung von Lizenzgebuehren.
- **UZK Art. 71 Abs. 1 lit. b**: Hinzurechnung von Assists.
- **UZK-DA Art. 136-141**: Detailregeln fuer Lizenzgebuehren-Hinzurechnung.
- **WTO-Bewertungsabkommen Art. 8**: Internationale Grundlage fuer Hinzurechnungen.

## Pruef-Raster

- [ ] Alle relevanten Lizenzgebuehren identifiziert?
- [ ] Verkaufsbedingung-Test nach UZK-DA Art. 136 angewendet?
- [ ] Assists vollstaendig erfasst und bewertet?
- [ ] Hinzurechnungs-Kalkulation erstellt?
- [ ] Rueckwirkungs-Risiko fuer Vorjahre quantifiziert?
- [ ] Ergebnis als Zollwert-Analyse dokumentiert?

## Typische Fallstricke

- Lizenzgebuehren an Konzernmutter gelten fast immer als Verkaufsbedingung.
- Markenlizenz fuer Weiterverkauf koennen ebenfalls hinzurechnungspflichtig sein.
- Assists werden haeufig vergessen; Konzerninterne Beistellungen besonders pruefanfaellig.
- Nacherhebung rueckwirkend bis zu 10 Jahre bei arglistiger Verschweigung.

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

Zollwert-Analyse mit Royalty-Pruefpfad, Assists-Bewertungsblatt, Hinzurechnungs-Kalkulation und Risikobewertung fuer Vorjahre.

## Quellen

- [UZK Art. 71 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA Art. 136 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de Zollwert](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollwert/zollwert_node.html)
- [WTO Valuation Agreement](https://www.wto.org/english/tratop_e/cusval_e/cusval_e.htm)

## 3. `aussenwirtschaft-zollwert-ursprung`

**Fokus:** Zusammenhang von Zollwert und Ursprung bei der Einfuhr: Praeferenzieller und nichtpraeferenzieller Ursprung als Zollwert-Einflussfaktor und Nachweis-Anforderungen. Zollwertberichtigung bei nachtraeglichen Ursprungsnachweisen und REX-Erklaerungen. Kombinierte Pruefung Zollwert-Ursprung bei Zollaußenpruefungen. Output: Integrierte Zollwert-Ursprungs-Pruefmatrix.

# Zollwert und Ursprung: Integrierte Pruefung und kombiniertes Nachweispaket

## Mandantenfall

- Importeur legt nachtraeglich EUR.1-Zertifikat vor; Zollwert-Erstattung und Praeferenz-Berichtigung.
- Zollaußenpruefung prueft gleichzeitig Zollwert und Praeferenz-Ursprung; Nachweispaket zusammenstellen.
- Unternehmen hat REX-Erklaerung erhalten aber Ursprungsvoraussetzungen nicht geprueft.

## Erste Schritte

1. Ursprungsnachweise fuer Einfuhrsendungen katalogisieren: EUR.1 EUR-MED REX ATR Form A GSP-Bescheinigung.
2. Zollwert-Kalkulation und Ursprungszuordnung fuer jede Lieferantenbeziehung abgleichen.
3. Nachtraegliche Ursprungsnachweise: Erstattungsantrag stellen Fristen nach Art. 121 UZK.
4. REX-System: Registrierter Exporteur pruefen; Erklaerungsinhalt auf Ursprungsvoraussetzungen.
5. Kombinierten Nachweispaket fuer Zollaußenpruefung vorbereiten.
6. Einheitliche Pruefmatrix erstellen: Zollwert Ursprung Praeferenz und Nachweis-Status.

## Rechtsrahmen

- **UZK Art. 59-76**: Ursprungsregeln praeferenziell und nichtpraeferenziell.
- **UZK Art. 70**: Transaktionswert als Zollwertbasis.
- **VO (EU) 952/2013 Art. 112-121**: Erstattung und Erlass von Einfuhrabgaben.
- **VO (EU) 1207/2001**: Ursprungsnachweisverfahren und REX.
- **UZK-DA Art. 69-112**: Detailregeln fuer Ursprung und Nachweise.

## Pruef-Raster

- [ ] Alle Ursprungsnachweise fuer relevante Einfuhren katalogisiert?
- [ ] Zollwert und Ursprungszuordnung konsistent?
- [ ] Nachtraegliche Ursprungsnachweise auf Erstattungspotenzial geprueft?
- [ ] REX-Erklaerungen auf Ursprungsvoraussetzungen verifiziert?
- [ ] Kombiniertes Nachweispaket fuer Pruefung bereit?
- [ ] Pruefmatrix aktuell und vollstaendig?

## Typische Fallstricke

- Fristen fuer Erstattungsantrag bei nachtraeglichem Ursprungsnachweis beachten (3 Jahre).
- REX-Erklaerungen des Lieferanten koennen falsch sein; Eigenverantwortung des Importeurs.
- Zollwert und Ursprung werden bei Pruefung oft kombiniert; Luecken in beiden Bereichen kumulieren sich.
- Nachtraegliche Ursprungs-Korrekturen erfordern Zollanmeldungs-Berichtigung.

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

Integrierte Zollwert-Ursprungs-Pruefmatrix mit Nachweis-Status-Tracking, Erstattungsantrags-Vorlage und Pruefungs-Vorberei tungscheckliste.

## Quellen

- [UZK Art. 59 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Praeferenz](https://www.zoll.de/DE/Fachthemen/Zoelle/Praeferenzrecht/praeferenzrecht_node.html)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [BAFA Ausfuhrkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
