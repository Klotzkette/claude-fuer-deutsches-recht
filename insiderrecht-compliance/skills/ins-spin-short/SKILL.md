---
name: ins-spin-short
description: "Ins 037 Spin Off, Ins 041 Short Seller Attack: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 037 Spin Off, Ins 041 Short Seller Attack

## Arbeitsbereich

Dieser Skill bündelt **Ins 037 Spin Off, Ins 041 Short Seller Attack** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-037-spin-off` | Steuert Insiderrecht-Compliance bei Spin-offs: Insiderinformations-Zeitpunkte, Ad-hoc, Insiderlisten fuer Mutter und Tochter sowie Post-Separation-Pflichten. |
| `ins-041-short-seller-attack` | Steuert die Compliance-Reaktion auf Short-Seller-Berichte: Ad-hoc-Pflicht, Dementierungsgrenzen, BaFin-Zusammenarbeit und Marktmanipulationsvorwurf. |

## Arbeitsweg

Für **Ins 037 Spin Off, Ins 041 Short Seller Attack** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-037-spin-off`

**Fokus:** Steuert Insiderrecht-Compliance bei Spin-offs: Insiderinformations-Zeitpunkte, Ad-hoc, Insiderlisten fuer Mutter und Tochter sowie Post-Separation-Pflichten.

# Spin-off – Insiderrecht bei Unternehmensabspaltungen

## Rechtlicher Rahmen

Ein Spin-off (Abspaltung nach UmwG, Demerger) ist eine komplexe Transaktion mit mehreren
insiderrelevanten Meilensteinen: Strategieentscheidung, Board-Beschluss, Regulierungsgenehmigungen,
Erstnotiz der Tochter. Für Muttergesellschaft und die neu börsennotierte Tochter entstehen
eigenständige MAR-Pflichten. EuGH C-19/11 (Geltl/Daimler) erfordert Zwischenschritt-Prüfung.

Rechtsgrundlagen:
- Art. 7, 17, 18, 19 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- EuGH C-19/11 (Geltl/Daimler): https://curia.europa.eu/juris/document/document.jsf?docid=123755
- §§ 123 ff. UmwG (Abspaltung): https://www.gesetze-im-internet.de/umwg/__123.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die insiderrechtliche Compliance eines Spin-off-Prozesses für beide
Gesellschaften (Mutter und Tochter) von der Strategieentscheidung bis zur vollständigen
Trennung.

## Arbeitsprogramm

### Schritt 1 – Meilensteinprüfung (Geltl/Daimler-Test)

Meilensteine mit potenziellem Insiderinformations-Entstehungszeitpunkt:
- Strategische Entscheidung des Vorstands (Spin-off ernsthaft in Betracht ziehen)
- Board-Beschluss zur Vorbereitung
- Beauftragung von Beratern (Investment Bank, Kanzlei)
- Einholung regulatorischer Genehmigungen (Kartellamt, BaFin)
- HV-Einberufung mit Spin-off-Tagesordnungspunkt
- HV-Beschluss

### Schritt 2 – Insiderlisten für Mutter und Tochter

- Mutter: Alle Wissensträger des Spin-off-Projekts ab dem frühesten Insiderinformations-
 zeitpunkt in Insiderliste aufnehmen
- Zukünftige Tochter-Gesellschaft: Eigenständige Insiderliste aufbauen, sobald
 Management der Tochter über die Transaktion informiert wird
- Trennung der Informationsflüsse dokumentieren

### Schritt 3 – Ad-hoc-Pflichten

- Muttergesellschaft: Ad-hoc beim Board-Beschluss (oder bei erstem kursrelevantem
 Zwischenschritt)
- Tochtergesellschaft (nach Börsengang): Eigenständige Ad-hoc-Pflichten nach Art. 17 MAR
- Koordination: Beide Gesellschaften müssen simultane Veröffentlichung koordinieren

### Schritt 4 – Post-Separation-Compliance

- Trennung der Insiderlisten nach vollzogener Abspaltung
- PDMR-Status: Wer ist nach der Trennung in welcher Gesellschaft PDMR?
- Directors' Dealings: Neue Meldepflichten für Vorstands-/AR-Mitglieder der Tochtergesellschaft
- Informationsbarrieren zwischen Mutter und Tochter nach der Trennung

### Schritt 5 – Haftungsrisiken im Transitionszeitraum

- Welche Gesellschaft haftet für Compliance-Verstöße während der Transition?
- Vertragliche Regelung im Spin-off-Vertrag (Indemnification)
- Compliance-Übergabe: Insiderlisten, Aufschubakten, Directors'-Dealings-Register

## Red-Team-Fragen

- Wurden alle insiderrelevanten Meilensteine zeitpunktbezogen geprüft?
- Gibt es Informationsbarrieren zwischen Mutter und Tochter bereits vor der Trennung?
- Wurden Haftungsfragen im Spin-off-Vertrag geregelt?
- Sind die Insiderlisten beider Gesellschaften vollständig und getrennt?

## Ausgabeformat

Erzeuge:
1. Spin-off-Meilensteinmatrix mit Insiderinformations-Prüfung
2. Doppeltes Insiderlisten-Framework (Mutter / Tochter)
3. Koordinierter Ad-hoc-Entwurf (Mutter und Tochter)
4. Post-Separation-Compliance-Roadmap

Belege ausschließlich mit: eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de,
bafin.de, bgh.de, dejure.org.

## 2. `ins-041-short-seller-attack`

**Fokus:** Steuert die Compliance-Reaktion auf Short-Seller-Berichte: Ad-hoc-Pflicht, Dementierungsgrenzen, BaFin-Zusammenarbeit und Marktmanipulationsvorwurf.

# Short-Seller-Angriff – Compliance-Reaktion

## Rechtlicher Rahmen

Wenn ein Short Seller einen detaillierten kritischen Bericht über einen Emittenten veröffentlicht,
entstehen mehrere Compliance-Fragen: (1) Muss der Emittent reagieren (Ad-hoc)? (2) Ist der
Short-Seller-Bericht Marktmanipulation nach Art. 12 MAR? (3) Wie kommuniziert der Emittent
ohne unzulässige Offenlegung von Insiderinformationen?

Rechtsgrundlagen:
- Art. 12, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 20 MAR (Anlageempfehlungen): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG (Marktmanipulation): https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die unmittelbare Compliance-Reaktion auf einen Short-Seller-Bericht
und koordiniert die Kommunikation mit der BaFin.

## Arbeitsprogramm

### Schritt 1 – Sofortbewertung (0–2 Stunden)

- Inhalt des Berichts: Welche konkreten Vorwürfe werden erhoben?
- Sind die Vorwürfe öffentlich bekannte Informationen oder neue Behauptungen?
- Kursbewegung: Wie stark ist die Reaktion des Marktes?
- Handelsaussetzung prüfen: Ist eine Aussetzung notwendig?

### Schritt 2 – Ad-hoc-Pflicht-Prüfung

- Enthält der Short-Seller-Bericht wesentlich neue Tatsachenbehauptungen?
- Hat der Emittent diese Informationen schon als Insiderinformation identifiziert?
- Wenn ja und Aufschub lief: Ist der Aufschub jetzt zu beenden?
- Wenn die Behauptungen falsch sind: Ad-hoc-Pflicht zur Richtigstellung nach Art. 17 MAR

### Schritt 3 – Grenzen der Reaktion

- Emittent darf nur auf Basis öffentlicher Informationen reagieren
- Kein Dementieren von Fakten, die Insiderinformationen sind (würde unzulässige Offenlegung
 bedeuten oder den Aufschub gefährden)
- Zulässig: Hinweis auf fehlerhafte Methodik, fehlende Kontext-Information

### Schritt 4 – BaFin-Kommunikation

- Proaktive Kontaktaufnahme mit BaFin (Marktüberwachung)
- Mitteilen: Short-Seller-Bericht, Kursbewegung, interne Einschätzung der Vorwürfe
- BaFin kann eigenständige Marktmanipulationsuntersuchung gegen Short Seller einleiten
 (Art. 12 MAR, § 119 WpHG)

### Schritt 5 – Marktmanipulationsanzeige gegen Short Seller

- Prüfung: Enthält der Bericht falsche Informationen, die den Kurs beeinflussen sollen?
 (Art. 12 Abs. 1 lit. c MAR: Verbreitung falscher oder irreführender Informationen)
- Wenn ja: Anzeige bei BaFin und Staatsanwaltschaft erwägen
- Dokumentation: Short-Seller-Bericht sichern, Kursverlauf dokumentieren

## Red-Team-Fragen

- Wurde die Ad-hoc-Pflicht vollständig geprüft (nicht nur reflexartig dementiert)?
- Werden durch die Reaktion des Emittenten unbeabsichtigt Insiderinformationen offengelegt?
- Ist die BaFin zeitnah informiert worden?
- Gibt es Anhaltspunkte für Marktmanipulation durch den Short Seller?

## Ausgabeformat

Erzeuge:
1. Sofortbewertungs-Checkliste (0–2 Stunden)
2. Ad-hoc-Entscheidungs-Matrix (Reaktionspflicht × Schweigen × Richtigstellung)
3. BaFin-Kommunikationsprotokoll
4. Marktmanipulationsanzeige-Vorlage (falls relevant)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Die BaFin unterscheidet zwischen legitimer kritischer Analyse (Meinungsfreiheit, Art. 20 MAR
für Anlageempfehlungen) und der Verbreitung wissentlich falscher Tatsachenbehauptungen
(Art. 12 Abs. 1 lit. c MAR). Kurse beeinflussende Short-Seller-Berichte auf Basis eigener
Research-Arbeit sind grundsätzlich zulässig; Berichte mit erfundenen Daten oder
manipulierten Screenshots sind Marktmanipulation. Diese Abgrenzung ist im Einzelfall
mit einer auf Kapitalmarktrecht spezialisierten Kanzlei zu analysieren.

Weitere Quellen:
- Art. 20 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
