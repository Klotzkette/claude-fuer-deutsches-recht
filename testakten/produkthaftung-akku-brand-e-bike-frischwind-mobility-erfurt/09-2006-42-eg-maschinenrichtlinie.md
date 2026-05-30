# 09 — Maschinenrichtlinie 2006/42/EG — Analyse und Anforderungen

**Dokument-Typ:** Rechtliche Analyse
**AZ Kanzlei:** MR-2026-0822
**Rechtsgrundlage:** Richtlinie 2006/42/EG des Europäischen Parlaments und des Rates vom 17. Mai 2006

---

## 1. Anwendbarkeit auf Wind-X7

Die Maschinenrichtlinie 2006/42/EG gilt für Maschinen i.S.d. Art. 2 lit. a) der Richtlinie. Pedelecs mit elektrischem Antriebssystem sind als „Maschinen" im Sinne der Richtlinie einzustufen, da sie nicht-handgekoppelte Kraftübertragungskomponenten aufweisen. Dies wird durch den Leitfaden der EU-Kommission zur Anwendung der Maschinenrichtlinie (Ausgabe 2019, Abschn. 42) bestätigt.

---

## 2. Wesentliche Sicherheitsanforderungen (Anhang I)

Für den Wind-X7 sind insbesondere relevant:

| Anforderung (Anhang I MRL) | Anforderungsinhalt | Status Wind-X7 |
|---|---|---|
| 1.1.2 (Sicherheitsprinzipien) | Konstruktion nach dem Stand der Technik | Eingeschränkt: BMS-Bug verletzt Sicherheitsprinzip |
| 1.5.1 (Stromversorgung) | Schutz vor gefährlichen Überspannungen | Verletzt: Überladen auf 4,35 V/Zelle |
| 1.5.6 (Brand und Explosion) | Konstruktion so, dass kein Brandrisiko entsteht | Verletzt: Thermisches Durchgehen dokumentiert |
| 1.7.4 (Betriebsanleitung) | Sicherheitshinweise Temperatur, Lagerung, Laden | Unvollständig: Keine Warnung bei Hitze |
| Anhang II A (Konformitätserklärung) | Vollständige und korrekte Konformitätserklärung | Teilweise fehlerhaft (Zellchemie) |

---

## 3. Technische Dokumentation (Anhang VII)

Die Maschinenrichtlinie verpflichtet den Hersteller zur Erstellung und Aufbewahrung einer technischen Dokumentation (Anhang VII MRL). Diese muss u.a. enthalten:
- Gesamtzeichnungen und Stücklisten
- Vollständige Beschreibung aller Schutzmaßnahmen
- Prüfberichte (intern und extern)
- Risikobeurteilung nach EN ISO 12100

Frischwind hat die technische Dokumentation erstellt. Im Rahmen der aktuellen Prüfung stellt Kanzlei Roosendaal fest:
- Risikobeurteilung (EN ISO 12100) bezieht sich auf LiFePO4-Zellen — nicht auf verwendete NMC-Zellen.
- Übertemperatur-Szenario bei > 38 °C wurde in der Risikobeurteilung als „unwahrscheinlich" eingestuft, ohne spezifische Abhilfemaßnahmen.
- Der BMS-Firmware-Bug war zum Zeitpunkt der Erstellung der technischen Dokumentation offenbar noch nicht bekannt — gleichwohl hätte eine vollständige FMEA (Fehlermöglichkeits- und Einflussanalyse) den Bug potenziell identifiziert.

**Handlungsempfehlung:** Technische Dokumentation unverzüglich aktualisieren; Risikobeurteilung auf NMC-Zellen neu erstellen; Firmware-Bug als identifiziertes Risiko dokumentieren.

---

## 4. Konformitätsverfahren nach 2006/42/EG

Für den Wind-X7 wurde das Konformitätsverfahren „Baumusterprüfung durch benannte Stelle" gewählt (Anhang IX MRL i.V.m. EN 15194:2017). Dies ist für Pedelecs mit Elektromotor der korrekte Weg.

Nach Art. 12 Abs. 3 MRL ist bei wesentlichen Änderungen der Bauart oder der Ausführung eines Produkts, für das eine Baumusterprüfbescheinigung ausgestellt wurde, eine erneute Prüfung durch die benannte Stelle erforderlich. Der Wechsel von LiFePO4 zu NMC-Zellen ist eine wesentliche Änderung im Sinne dieser Vorschrift.

Frischwind hat die erneute Prüfung nicht beantragt — **Verstoß gegen Art. 12 Abs. 3 MRL**.
