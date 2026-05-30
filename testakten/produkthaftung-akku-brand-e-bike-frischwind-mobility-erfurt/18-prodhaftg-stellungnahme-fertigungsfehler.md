# 18 — ProdHaftG-Stellungnahme: Fertigungsfehler vs. Entwicklungsfehler und ChinaTech-Regress

**Dokument-Typ:** Interne Rechtliche Stellungnahme
**AZ Kanzlei:** MR-2026-0822
**Autor:** RAin Dr. Henrike Sattler-Böhm

---

## 1. Fehlerarten nach ProdHaftG

### 1.1 Entwicklungsfehler (§ 1 Abs. 2 Nr. 5 ProdHaftG)

Ein Entwicklungsfehler liegt vor, wenn der Fehler nach dem Stand der Wissenschaft und Technik zum Zeitpunkt des Inverkehrbringens nicht erkennbar war. Bei Entwicklungsfehlern ist der Hersteller nach § 1 Abs. 2 Nr. 5 ProdHaftG von der Haftung befreit.

**Bewertung Wind-X7:** Der BMS-Bug in Firmware V3.9.1 ist kein Entwicklungsfehler, da:
- Integer-Overflows in Embedded-Systemen seit Jahrzehnten bekannt sind.
- MISRA C (industriestandard für sicherheitskritische Embedded-Systeme) vorschreibt, dass Temperaturkompensationsalgorithmen gegen Überläufe gesichert sein müssen.
- ChinaTech hätte den Bug durch Standard-Unit-Tests (MISRA-konforme Firmware-Verifikation) entdecken müssen.
- Frischwind hätte den Bug durch Eingangsvalidierung (Firmware-Verifikation im Rahmen des Wareneingangsprozesses) erkennen können.

**Ergebnis: Kein Entwicklungsfehler-Privileg anwendbar.**

### 1.2 Fabrikationsfehler (§ 3 ProdHaftG)

Ein Fabrikationsfehler liegt vor, wenn das konkrete Produkt von der Herstellervorgabe abweicht. Vorliegend:
- Datenblatt ChinaTech: LiFePO4-Zellen → Serienprodukt: NMC-Zellen = **Fabrikationsfehler ChinaTech**
- Firmware-Bug V3.9.1: Fertigung einer fehlerhaften Firmware = **Fabrikationsfehler ChinaTech**
- Baumusterprüfung mit LiFePO4, Serienproduktion mit NMC ohne erneute Prüfung = **Organisationsfehler Frischwind** (Konstruktionsfehler i.w.S.)

### 1.3 Instruktionsfehler (§ 3 ProdHaftG)

Keine ausreichende Warnung in der Betriebsanleitung Wind-X7 vor Lagerung und Laden bei Temperaturen > 35 °C. Das Produkthandbuch enthält nur den Hinweis: „Nicht über 40 °C lagern" — keinen Hinweis auf erhöhtes Brandrisiko bei Laden in der Wärme. **Instruktionsfehler liegt vor.**

---

## 2. Gesamtergebnis Fehlerarten

Alle drei Fehlertypen sind vorliegend relevant. Frischwind haftet aus ProdHaftG gesamtschuldnerisch mit ChinaTech für Schäden des Endkunden. Intern (im Verhältnis Frischwind/ChinaTech) richtet sich die Haftungsverteilung nach dem Liefervertrag und dem Bürgerlichen Recht.

---

## 3. Regressanspruch gegen ChinaTech ShenZhen

### 3.1 Vertragliche Regressgrundlage

Der Rahmenliefervertrag (2022) enthält folgende relevante Klauseln:
- Art. 8: ChinaTech garantiert, dass die Akkus den vereinbarten Spezifikationen (Datenblatt CT-LI-45-X) entsprechen.
- Art. 9: Bei Spezifikationsabweichungen haftet ChinaTech für nachgewiesene Schäden bis zur Höhe des Lieferwertes der betroffenen Charge.
- **Haftungsbeschränkung Art. 9.3:** ChinaTech haftet nicht für mittelbare Schäden oder Folgeschäden. Maximale Haftung: Warenwert der betroffenen Lieferung.

**Bewertung:** Die Haftungsbeschränkung Art. 9.3 dürfte bei arglistig falschen Angaben zur Zellchemie (NMC statt LiFePO4) nach § 444 BGB i.V.m. Art. 3 Abs. 3 VO (EG) Nr. 593/2008 (Rom I) nicht wirksam sein. Arglist ist zu prüfen.

### 3.2 Deliktischer Regress

Nach §§ 823 Abs. 1, 831 BGB ist ChinaTech als Hersteller des fehlerhaften Komponenten (Akku) direkt gegenüber Raskolnikow deliktisch verantwortlich. Im Innenverhältnis ergibt sich daraus ein Regress Frischwind gegen ChinaTech in Höhe des ChinaTech-Verursachungsbeitrags.

### 3.3 Durchsetzbarkeit in China

**Risiko:** ChinaTech operiert in der VR China. Vollstreckung eines deutschen Urteils in China ist praktisch sehr schwierig (kein bilaterales Vollstreckungsabkommen DE–CN). Alternative: Klage vor chinesischen Gerichten (Volksgerichtshof ShenZhen) — aufwendig, teuer, unsichere Erfolgsaussichten.

**Strategie:** Zunächst außergerichtliche Einigung anstreben; ChinaTech im Rahmen des laufenden Liefervertrags (Laufzeit bis 2027) unter Druck setzen (Zahlungsverzögerung zukünftiger Rechnungen als Druckmittel, falls zulässig).
