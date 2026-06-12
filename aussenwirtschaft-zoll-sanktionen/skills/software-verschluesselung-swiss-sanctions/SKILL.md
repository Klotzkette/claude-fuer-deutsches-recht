---
name: software-verschluesselung-swiss-sanctions
description: "Exportkontrolle für Verschluesselungssoftware und Kryptografieprodukte nach VO (EU) 2021/821 Kategorie 5 Teil 2 (Telekommunikation/Informationssicherheit): Klassifizierung von Algorithmen (AES 256 bit RSA ECC) Exportgenehmigungspflicht und Allgemeine Genehmigung EU001. Besonderheiten bei Open-Sou..."
---

# Exportkontrolle für Verschluesselungssoftware: Kryptografie und Dual-Use-Kategorie 5

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Softwarehaus moechte Produkt mit AES-256-Verschluesselung in Drittlaender exportieren; Genehmigungspflicht unklar.
- Cloud-Dienst mit Ende-zu-Ende-Verschluesselung wird von EU-Kunden an Endkunden in Embargo-Staaten bereitgestellt.
- Open-Source-Kryptobibliothek soll in Exportprodukt integriert werden; Klassifizierung prüfen.

## Erste Schritte

1. Kryptografische Parameter bestimmen: Algorithmus, Schlüssellaenge, Protokoll (TLS SSL VPN SSH).
2. Einreihung in Kategorie 5 Teil 2 der EU-Dual-Use-Liste (VO 2021/821 Anhang I) prüfen.
3. Ausnahmeregelungen prüfen: Massenmarktprodukt mit Standard-Kryptografie, Open-Source-Ausnahme.
4. Allgemeine Genehmigung EU001 auf Anwendbarkeit prüfen (Standard-Verschluesselung in Massenmarktsoftware).
5. Ziellaender und Endverwender auf Embargo und Catch-All prüfen.
6. Ergebnis als Klassifizierungsvermerk dokumentieren.

## Rechtsrahmen

- **VO (EU) 2021/821 Anhang I Kategorie 5 Teil 2**: EU-Dual-Use-Liste für Kryptografieprodukte.
- **Art. 9 VO (EU) 2021/821**: Allgemeine Genehmigungen (EU001) für bestimmte Kryptografieexporte.
- **AWG § 8**: Genehmigungsvorbehalt für kontrollierte Waren.
- **EAR Part 742.15 (US)**: US-spezifische Kryptografie-Exportkontrolle (als Risikoanker).
- **Art. 4 VO (EU) 2021/821**: Catch-All bei militaerischer Endverwendung von Kryptografietechnologie.

## Prüf-Raster

- [ ] Kryptografische Parameter vollstaendig erfasst (Algorithmus Schlüssellaenge Protokoll)?
- [ ] Einreihung in Kategorie 5 Teil 2 geprueft?
- [ ] Massenmarkt- oder Open-Source-Ausnahme anwendbar?
- [ ] Allgemeine Genehmigung EU001 greift?
- [ ] Zielland und Endverwender auf Embargo und Catch-All geprueft?
- [ ] Klassifizierungsvermerk mit Quellenangabe erstellt?

## Typische Fallstricke

- Standardmaessig eingebettete TLS-Bibliotheken fallen trotzdem unter Dual-Use-Kontrolle.
- Open-Source-Ausnahme gilt nicht für modifizierte oder proprietaer eingebettete Varianten.
- Cloud-Dienste: Technologie-Transfer durch Download von verschluesselter Software über Landesgrenze.
- US-Re-Export-Kontrollen (EAR) ueberlagern EU-Genehmigung bei US-Ursprungstechnologie.

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
- Output mandantentauglich: Kein Fachwort ohne Erläuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [VO (EU) 2021/821 Anhang I auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Dual-Use Allgemeine Genehmigungen](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Ausfuhrgenehmigungen/Allgemeine_Genehmigungen/allgemeine_genehmigungen_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
