#!/usr/bin/env python3
"""Redaktionelle Fallbeschreibung und Phasenzuordnung."""
import json
from collections import Counter
from bauwirtschaft_hildesheim_common import ROOT, CASE, SLUG, euro
from readme_decimal_headings import normalize_decimal_headings
from testakte_download_notices import ensure_download_notices
from testakte_zip_common import working_dump_flat_pairs

def main():
    data=json.loads((ROOT/'quality/hildesheim-achtfamilienhaus/finanzdaten.json').read_text())
    registry_path=CASE/'069_Dokumentenregister.txt'
    registry_path.touch(exist_ok=True)
    originals=[p for p,_ in working_dump_flat_pairs(CASE,include_gesamt_pdf=False)]
    counts=Counter(p.suffix for p in originals)
    formats=', '.join(f'{v} {k[1:].upper()}' for k,v in sorted(counts.items()))
    text=f"""<!-- decimal-headings -->
<!-- reserved-example-contacts -->

# Achtfamilienhaus zur Vermietung in Hildesheim

## Umfang und Projektverlauf

Ein zusammenhängender Neubaufall über **alle neun HOAI-Leistungsphasen für Gebäude**: Grundstückserwerb und Projektbeginn im Oktober 2026, Planung und Genehmigung 2027, Bau und förmliche Bauabnahmen am 15. September 2028, Erstvermietung ab 1. Oktober 2028, spätere Mängelbewertung und Objektbetreuung bis September 2033 sowie kaufmännischer Abschluss am 5. Oktober 2033.

Der Bestand enthält **{len(originals)} native Originaldateien**: {formats}. Eine Rechnung kann sowohl als strukturierte XML-Datei als auch als lesbare PDF-Darstellung vorliegen. Das sind zwei Dateiformate desselben Belegs und keine zwei Forderungen. Autor: Klotzkette. Fallkennung: {SLUG}.

Das Grundstück hat 1.300 m², das Gebäude acht Mietwohnungen mit zusammen 600 m² Wohnfläche, drei Geschosse ohne Keller, einen Aufzug, acht Pkw-Stellplätze, Fahrrad- und Spielflächen, Wärmepumpen sowie eine PV-Anlage. Die privat finanzierte Vermietungs-GmbH ist Auftraggeberin. Die Akte gehört zum Plugin [bauwirtschaft](../../bauwirtschaft/README.md) und ergänzt die neun eigenständigen Phasenakten um einen durchgehenden Wohnungsneubau.

## Simulation und Quellenstand

**Recherche- und Redaktionsstand: 27. September 2026. Der Projektverlauf 2026–2033 ist simuliert.** Bereits verkündete Änderungen und Übergangsregeln werden berücksichtigt. Unbekanntes künftiges Recht wird nicht als feststehend behauptet.

Personen, Unternehmen, Grundstück, Adresse, Registerbezeichnungen, Steuernummern, Sicherheitsnummern, Abfrageergebnisse, Verwaltungsentscheidungen, Prüfbescheinigungen und technische Rechenwerte sind erfunden. Hildesheim und die verlinkten amtlichen Rechtsquellen sind real. Es fanden keine echten Grundbuch-, BZSt- oder Behördenabfragen statt. Die Bescheide sind keine tatsächlichen Verwaltungsakte und die Zeichnungen keine ausführungsreife Planung eines wirklichen Bauvorhabens. Die PNG-Dateien sind eigens erzeugte Ansichten einer fiktiven Projektablage und eines Baustellenchats. Reservierte Kontaktadressen mit **.example** verhindern die Verwechslung mit tatsächlichen Ansprechpartnern.

Quellenprüfung und Beurteilungskriterien liegen außerhalb der PDF- und ZIP-Arbeitsakten. Der [gesonderte Quellenbericht](../../quality/hildesheim-achtfamilienhaus/quellen.md) dokumentiert NBauO, Genehmigungsumfang, Energie- und Ladeinfrastruktur, Umsatzsteuer, Bauabzug, Notar- und Gerichtskosten sowie die Trennung von Bauabnahme und Architektenabnahme.

## Welche HOAI-Leistungsphase lässt sich prüfen?

| Leistungsphase | Enthaltene Unterlagen | Bearbeitbarer Projektstand |
| --- | --- | --- |
| **1 Grundlagenermittlung** | 001–006, 070–074, 149/170 | Bedarf, Auftrag, Grundstück, Ortsaufnahme, Baugrund und Fachplanerbedarf |
| **2 Vorplanung** | 007–008 und 120 | Varianten, vergleichbare Anforderungen, Auswahl und Kostenrahmen |
| **3 Entwurfsplanung** | 009–017 und 120 | Wohnungsgrößen, Grundrisse, Schnitt, Fachplanung, Energie und Entwässerung |
| **4 Genehmigungsplanung** | 018–022 und 075 | Bauantrag, Baubeschreibung, Nachforderung, Antwort und Genehmigung nach NBauO |
| **5 Ausführungsplanung** | 023–029, 150–151 | Schwellen, Durchbrüche, Fachplanerkollisionen, Planstand und Freigabe |
| **6 Vorbereitung der Vergabe** | 030–031 | Vergabetermine und bauteilbezogenes LV für sieben Lose |
| **7 Mitwirkung bei der Vergabe** | 032–048 | Acht Angebote, Vergleich, Vergabeentscheidung, direktes Anwaltsmandat und sieben Bauverträge |
| **8 Objektüberwachung und Dokumentation** | 049–062, 070–122, 146–148, 152, 162–179 | Bauablauf, Tagesberichte, Nachtrag, Aufmaß, Rechnungen, Zahlungen, Abnahmen und Betriebsübergabe |
| **9 Objektbetreuung** | 063–068, 083, 112/116 und 153 | Späterer Feuchtebefund, Bewertung, Vorfristbegehung, Sicherheit und gesonderte Planerabnahme |

Die Phasen greifen auf denselben Projektstand zu. Bei einer späteren Phase bleiben die erforderlichen früheren Verträge, Freigaben und Belege Teil des Arbeitsordners. Die Aktennummer ist eine stabile Zuordnung und nicht durchgehend ein chronologischer Sortierschlüssel.

Die sieben Plan-PDFs liegen im Originalformat-ZIP als A3-Zeichnungen vor. Der eingetragene Maßstab gilt bei unverändertem Ausdruck auf A3. Gesamt-PDF und Einzel-PDF-ZIP sind auf A4 normierte Lesefassungen; dort dürfen Maße nicht mit dem Lineal vom verkleinerten Blatt abgenommen werden. Maßzahlen und Planstände bleiben lesbar.

## Vermietung und Buchhaltung

Für alle acht Wohnungen liegen eigene Mietverträge, vorvertragliche Informationen und Übergabeprotokolle vor (130–145 und 154–161). Das Zählerregister 169 verbindet technische Daten mit den Wohnungsübergaben. **Vermietung ist ein zusätzlicher kaufmännischer Arbeitsstrang und keine weitere HOAI-Leistungsphase.**

Die Finanzunterlagen enthalten {len(data['invoices'])} Kostenbelege vom Grundstück über Erwerbsnebenkosten, Planung und Bau bis zur letzten Architektenrechnung. Hinzu kommen Darlehen, Eigenkapitalbeschluss, Projektkontoauszüge und drei bearbeitbare Arbeitsmappen 120–122. Rechnung, Auftrag, Nachtrag, Zahlung, Erstattung und verbleibendes Projektguthaben lassen sich miteinander abgleichen.

Der freigegebene Rahmen beträgt {euro(data['budget'])} EUR. Kosten und Liquidität sind getrennt: laufender Mietbetrieb, Kautionen und spätere Annuitäten gehören nicht ungeprüft in die Baukosten. Die Arbeitsmappen kontrollieren Projektmittel und Kosten. Sie sind keine fertige handels- oder steuerrechtliche Aktivierungs- und AfA-Rechnung. Gemischte Erwerbs- und Grundschuldkosten müssen dafür nach den Positionen der Belege getrennt zugeordnet werden. Die Unterlagen enthalten keine vollständige steuerliche Veranlagung der GmbH. PV-Anlage, Wohnungsvermietung und Einspeiseumsätze bleiben gesondert einzuordnen.

## Einstieg in den Workshop

> Bearbeite den Achtfamilienhaus-Neubau anhand der beigefügten Originalakte. Beginne mit der HOAI-Leistungsphase, die ich nenne. Lies die erforderlichen früheren Verträge und Freigaben mit. Erstelle das verlangte Ergebnis mit Belegbezug, führe Kosten und Termine fort und stelle nur entscheidende offene Fragen.

Für einen Buchhaltungslauf:

> Gleiche Aufträge, Rechnungen, Rechnungskorrekturen und Zahlungen ab. Trenne Investition, Liquidität und Mietbetrieb. Prüfe Umsatzsteuer und Bauabzug anhand der vorhandenen Belege. Liefere eine nachvollziehbare offene-Posten- und Zahlungsübersicht.

Die [neun Phasen-Skills und Werkstatt-Prompts](../../docs/bauwirtschaft-hoai-phasen.md) sind separat erreichbar. Die Testakte wird nicht mit dem Plugin installiert.
"""
    (CASE/'README.md').write_text(normalize_decimal_headings(ensure_download_notices(text)),encoding='utf-8')
    registry=['Steinbogen Wohnen GmbH · SW-HI-26-08 · Register 05.10.2033','']
    registry.extend(p.name for p in originals if not p.name.startswith('069_'))
    (CASE/'069_Dokumentenregister.txt').write_text('\n'.join(registry)+'\n',encoding='utf-8')

if __name__=='__main__':main()
