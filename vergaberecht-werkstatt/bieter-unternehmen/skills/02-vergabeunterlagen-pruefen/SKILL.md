---
name: 02-vergabeunterlagen-pruefen
description: 'Vergabeunterlagen auf Vollständigkeit, direkten Zugang, Widersprüche, Typ-/Systembindung, Datenformate und Abgabeweg prüfen. Erfasst GAEB, XML, Excel, PDF, Portalfelder, Live-Links, Bestandskompatibilität und Angebotsfreeze. Output Prüfbericht, Fristen-, Rüge- und Angebotsroute.'
---

# Vergabeunterlagen prüfen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Rechtsgrundlage

§ 160 Abs. 3 GWB (Rügefristen), § 29 VgV (Vergabeunterlagen und Zahlung). Für vor dem 1. Juli 2026 begonnene Verfahren gilt nach § 187 Abs. 2 GWB die alte Fassung fort.

## Pflichtschritte

1. Bewerbungsbedingungen vorhanden
2. Leistungsbeschreibung eindeutig
3. Vertragsentwurf akzeptabel
4. ESPD oder Eigenerklärung
5. Bewertungsmatrix transparent
6. LV/Preisblatt und technische Formate auslesbar (GAEB, XML, Excel, PDF, ZIP)
7. Verbindliches Abgabeformat und Portalvorgaben bestimmt
8. Bekannte Risiken: Markenbezug, Materialvorgabe, proprietäre Schnittstelle, missverständliche Leistungsbeschreibung, unpassendes Rückgabeformat.
9. Externe Links und Datenräume: verbindlicher Upload oder nur ergänzende Information; Änderbarkeit nach Fristablauf prüfen.
10. Rügefristen vorgemerkt
11. In Neuverfahren Zahlungsbedingungen gegen § 29 Abs. 3 VgV prüfen: Zahlung nach Leistung und regelmäßig binnen 30 Tagen nach Eingang einer prüfbaren Rechnung; abweichende Regel, Abschlag oder Vorauszahlung wirtschaftlich und haushaltsrechtlich einordnen

## Format-Workflow

Bei GAEB/XML/Excel/PDF oder ZIP immer zuerst `unterlagen-und-lv-datenformate-auslesen` nutzen. Ziel ist eine Unterlagenmatrix mit Datei, Format, Zweck, Pflichtfeld, Rügepunkt und Angebotsaktion. Wenn die Vergabestelle ein natives Rückgabeformat verlangt, anschließend `angebot-in-vorgegebenem-format-erstellen` nutzen.

## Anker-Rechtsprechung

- EuGH C-336/12 'Manova' zur Heilung
- EuGH, Urteil vom 16.04.2026, C-568/24, Sof Medica: Typ-, Größen-, System- oder Schnittstellenvorgaben auf Unvermeidbarkeit und Gleichwertigkeit prüfen.
- EuGH, Urteil vom 16.01.2025, C-424/23, DYKA Plastics: Produkt-, Material- und Systemvorgaben sowie technische Spezifikationen müssen Wettbewerbsoffenheit wahren; Gleichwertigkeit darf auch im Datenformat nicht blockiert werden.
- EuGH, Urteil vom 03.07.2025, C-534/23 P und C-539/23 P, Instituto Cervantes: unmittelbar EU-Eigenvergabe; im deutschen Verfahren nur Integritätsanker neben § 53 VgV und Portalvorgabe. Verlangte Unterlagen fristfest hochladen.
- OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24: Bestandskompatibilität kann eine spezifische Beschaffung rechtfertigen; eigene Alternative technisch belastbar darstellen.
- OLG Düsseldorf, Beschluss vom 13.05.2019, Verg 47/18: Unterlagen müssen vollständig und direkt über den bekannt gemachten Weg erreichbar sein.

## Output

Prüfbericht plus Risikoliste. Bei wesentlichen Mängeln sofort eine Rügeweiche ausgeben: Verstoß, Aktenstelle, Frist, gewünschte Abhilfe, Angebotsfolge und Beleg.
