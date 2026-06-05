---
name: ins-datenraum-kapitalerh
description: "Ins 017 Datenraum Transaktion, Ins 021 Kapitalerh Hung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Ins 017 Datenraum Transaktion, Ins 021 Kapitalerh Hung

## Arbeitsbereich

Dieser Skill bündelt **Ins 017 Datenraum Transaktion, Ins 021 Kapitalerh Hung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `ins-017-datenraum-transaktion` | Sichert Datenraum-Prozesse in Transaktionen (M&A, Anleihe, Kapitalerhoehung) gegen Insiderrecht-Risiken: Zugangskontrolle, Protokollierung und Exit-Management. |
| `ins-021-kapitalerh-hung` | Prueft Insiderrecht-Compliance bei Kapitalerhoehungen: Zeitpunkt der Insiderinformation, Market Sounding, Handelsverbot, Ad-hoc und Bezugsrecht. |

## Arbeitsweg

Für **Ins 017 Datenraum Transaktion, Ins 021 Kapitalerh Hung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `insiderrecht-compliance` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `ins-017-datenraum-transaktion`

**Fokus:** Sichert Datenraum-Prozesse in Transaktionen (M&A, Anleihe, Kapitalerhoehung) gegen Insiderrecht-Risiken: Zugangskontrolle, Protokollierung und Exit-Management.

# Datenraum-Management in Transaktionen – Insiderrechtliche Anforderungen

## Rechtlicher Rahmen

Der Zugang zu einem virtuellen Datenraum in M&A- oder Kapitalmarkttransaktionen begründet
regelmäßig eine Insiderinformation für die Zugangsberechtigten. Art. 10 und 18 MAR setzen
strenge Anforderungen an Informationskreis-Kontrolle, Protokollierung und Belehrung. Der
Emittent bleibt verantwortlich für MAR-Compliance aller Datenraum-Nutzer.

Rechtsgrundlagen:
- Art. 10, 18 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- Art. 17 Abs. 4 MAR (Aufschub): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden Kap. III: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill erstellt die Governance für Datenräume in kapitalmarktrelevanten Transaktionen
und stellt sicher, dass alle Zugangsberechtigten korrekt als Insider behandelt werden.

## Arbeitsprogramm

### Schritt 1 – Datenraum-Governance-Struktur

- Benenne einen Datenraum-Administrator (i.d.R. M&A-Kanzlei oder Investmentbank)
- Definiere Zugriffsebenen (Stufe 1: Non-Insider-Informationen, Stufe 2: Insiderinformationen)
- Führe separate Insiderlisten für jede Zugriffsebene
- Beauftrage Datenraum-Anbieter mit aktiviertem Zugangsprotokoll (Wer hat wann welche
 Dokumente geöffnet/heruntergeladen?)

### Schritt 2 – Aufnahme in Insiderliste bei Zugriffserteilung

- Jeder Nutzer der Insiderinformations-Ebene wird unverzüglich in die Insiderliste aufgenommen
- Belehrung vor Zugriffserteilung (schriftlich, mit Zeitstempel)
- Bestätigung des Nutzers, Belehrung empfangen zu haben

### Schritt 3 – Need-to-Know-Prinzip

- Zugriffserteilung nur für Personen, deren Rolle die Information erfordert
- Regelmäßige Überprüfung der Zugriffsberechtigungen (mind. bei jedem Meilenstein)
- Sofortige Zugangssperrung bei Ausscheiden aus dem Prozess

### Schritt 4 – Exit-Management

Nach Abschluss des Prozesses (Signing, Closing, Abbruch):
- Schließung des Datenraums für alle Nutzer
- Archivierung der Zugangsprotokolle (5 Jahre)
- Bestätigung der Datenvernichtung von allen externen Parteien einholen
- Insiderlisten-Eintrag: Austrittsdatum für alle Nutzer eintragen

### Schritt 5 – Aufschub-Integration

- Datenraum-Zugang und Aufschub nach Art. 17 Abs. 4 MAR sind parallel zu führen
- Bei Leak: Sofortmaßnahmen (Skill ins-011) aktivieren
- Bei Abbruch der Transaktion: Insiderinformation erlischt nur, wenn kein legitimes Interesse
 mehr an Aufschub besteht; Compliance prüft neuen Status der Information

## Red-Team-Fragen

- Sind alle Datenraum-Nutzer in der Insiderliste erfasst?
- Wurden alle Nutzer vor Zugriffserteilung belehrt?
- Wird das Need-to-Know-Prinzip bei jeder Zugriffserteilung geprüft?
- Sind Zugangsprotokolle vollständig und unveränderbar gespeichert?
- Wurden externe Parteien zur Datenvernichtung verpflichtet?
- Ist der Zusammenhang zwischen Datenraum-Zugang und Aufschubakte dokumentiert?

## Ausgabeformat

Erzeuge:
1. Datenraum-Governance-Policy
2. Zugriffsebenen-Matrix (Dokument × Stufe × Nutzerkreis)
3. Belehrungsvorlage für Datenraum-Nutzer
4. Exit-Checkliste (Datenraum-Schließung)

Belege ausschließlich mit: eur-lex.europa.eu, bafin.de, gesetze-im-internet.de, dejure.org.

## 2. `ins-021-kapitalerh-hung`

**Fokus:** Prueft Insiderrecht-Compliance bei Kapitalerhoehungen: Zeitpunkt der Insiderinformation, Market Sounding, Handelsverbot, Ad-hoc und Bezugsrecht.

# Kapitalerhöhung – Insiderrechtliche Anforderungen

## Rechtlicher Rahmen

Eine Kapitalerhöhung (ordentlich, genehmigtes Kapital, Bezugsrechtsausschluss) erzeugt
typischerweise eine Insiderinformation spätestens ab dem Board-Beschluss. Market Sounding
nach Art. 11 MAR kann vorgelagert sein. Die Ad-hoc-Meldung muss unmittelbar beim Board-
Beschluss erfolgen, sofern kein wirksamer Aufschub besteht.

Rechtsgrundlagen:
- Art. 7, 11, 17 MAR: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- DVO (EU) 2016/960 (Market Sounding): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0960
- §§ 182–191 AktG (Kapitalerhöhung): https://www.gesetze-im-internet.de/aktg/__182.html
- BaFin-Emittentenleitfaden Kap. VI: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill steuert die insiderrechtliche Compliance einer Kapitalerhöhung vom Beschluss
bis zur Ad-hoc-Veröffentlichung, inklusive Market Sounding und Post-Deal-Compliance.

## Arbeitsprogramm

### Schritt 1 – Entstehungszeitpunkt der Insiderinformation

- Prüfe, ob bereits die Entscheidung, eine Kapitalerhöhung zu prüfen, eine präzise Information
 darstellt (Geltl/Daimler-Test: Zwischenschritte)
- Typischer Insiderinformations-Zeitpunkt: Board-Beschluss zur Durchführung
- Dokumentiere Zeitpunkt und Wissensträger

### Schritt 2 – Market Sounding (Art. 11 MAR)

Falls potenzielle Investoren vor Ankündigung sondiert werden:
- Wall-Crossing-Verfahren nach Skill ins-008 einleiten
- Sounding-Skript genehmigen: Welche Informationen werden als UPSI offengelegt?
- Insiderlisten für alle gesoundeten Investoren führen

### Schritt 3 – Handelsverbote und Closed Periods

- Vorstands- und AR-Mitglieder: Kein Handel in Aktien des Emittenten ab Insiderinformationszeitpunkt
- Konsortialbanken: Chinese Wall zwischen Underwriting-Team und Eigenhandel
- Bezugsrechte-Ausübung durch PDMRs: Prüfung ob Safe Harbour nach Art. 9 MAR greift

### Schritt 4 – Ad-hoc-Veröffentlichung

- Unverzüglich nach Board-Beschluss (Art. 17 MAR)
- Inhalt: Volumen, Preis oder Preisrange (falls bestimmt), Verwendungszweck, Timeline
- Handelsaussetzung prüfen: Ggf. Antrag an Handelsplatz vor Beschluss
- Koordination mit Konsortialbank für gleichzeitige Pressemitteilung

### Schritt 5 – Post-Deal-Compliance

- Insiderlisten schließen (Austrittsdaten für alle Beteiligten eintragen)
- Directors' Dealings: Zeichnung durch PDMRs meldepflichtig nach Art. 19 MAR
- Stabilisierungsmaßnahmen: Nur unter DVO (EU) 2016/1052 (Bezug zu Skill ins-022)
- Lock-up-Vereinbarungen dokumentieren

## Red-Team-Fragen

- Wurde der frühestmögliche Entstehungszeitpunkt der Insiderinformation festgestellt?
- Wurden alle gesoundeten Investoren korrekt als Insider behandelt?
- Wurden Eigengeschäfte von PDMRs zwischen Beschluss und Ad-hoc ausgeschlossen?
- Enthält die Ad-hoc alle Pflichtangaben zur Kapitalerhöhung?
- Wurden Bezugsrechte-Ausübungen durch PDMRs auf Art. 19 MAR-Meldepflicht geprüft?

## Ausgabeformat

Erzeuge:
1. Zeitstrahl Insiderinformation → Market Sounding → Board-Beschluss → Ad-hoc
2. Market-Sounding-Dokumentation (Skill ins-008-konform)
3. Ad-hoc-Entwurf für Kapitalerhöhungsbeschluss
4. Post-Deal-Compliance-Checkliste

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, dejure.org.

## Weitere Hinweise

Eine Kapitalerhöhung unter Ausschluss des Bezugsrechts nach § 186 Abs. 3 S. 4 AktG
(vereinfachter Bezugsrechtsausschluss) ist besonders sensibel: Die Entscheidung liegt beim
Vorstand im Rahmen des genehmigten Kapitals und muss unverzüglich ad-hoc kommuniziert werden.
Die Marktpraxis folgt typischerweise einem beschleunigten Bookbuilding, bei dem die
Preisfindung innerhalb weniger Stunden abgeschlossen wird. Compliance und IR müssen ab
Beginn des Bookbuilding-Prozesses in höchster Alarmbereitschaft sein.

Weitere Quellen:
- §§ 182 ff. AktG: https://www.gesetze-im-internet.de/aktg/__182.html
- DVO (EU) 2016/960: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0960
