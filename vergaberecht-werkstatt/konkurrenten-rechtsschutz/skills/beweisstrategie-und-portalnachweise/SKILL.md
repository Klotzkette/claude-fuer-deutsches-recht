---
name: beweisstrategie-und-portalnachweise
description: 'Beweise, Portalnachweise, Nachrichten, Uploadquittungen, Hashes, Dateiversionen und Zeitstempel für Konkurrentenangriffe sichern: Friststreit, Formatfehler, Zugangsstörung und geänderte Unterlagen.'
---

# Beweisstrategie und Portalnachweise

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Sichern

- Originaldateien unverändert ablegen.
- Hash, Dateiname, Version, Downloadzeitpunkt und Portalpfad notieren.
- Nachrichtenverlauf exportieren.
- Screenshots nur ergänzend, nie als alleiniger Beleg.
- PDF-Lesefassung und native Datei zusammenhalten.
- E-Mail-Header und Zustellnachweis speichern.
- Bei SAP/ERP/AVA/DMS/SharePoint/SFTP/API/MCP [LEGACY-SYSTEME-INTEGRATION.md](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden und ein Beweis-Cluster mit Quelle, Version, Hash, Angriff, Geheimnisschutz und Rückmeldung erzeugen.
- Herkunftszone dokumentieren: eigene Sphäre, öffentlich, Verfahrenszugang, befugter Dritter, nur Indiz oder unzulässig/ungeklärt.
- Original, OCR-/Lesefassung und markierten Auszug getrennt hashen; jede Transformation protokollieren.
- Tatsachenkern und rechtliche Schlussfolgerung in getrennten Spalten führen.

## Belegmatrix

| Behauptung | Beleg | Datei | Datum | Risiko |
| --- | --- | --- | --- | --- |
| Unterlage wurde geändert | Portalversion | ZIP/PDF/XML | Zeitstempel | Fristverlängerung |
| Upload scheiterte | Plattformmeldung | Screenshot/Log | Zeitstempel | Zugangsstörung |
| Wertungsfehler | Matrix | Akteneinsicht | Datum | Rückversetzung |

## Rechtsprechungsweichen

- EuGH, Urteil vom 03.07.2025, C-534/23 P und C-539/23 P, Instituto Cervantes: unmittelbar EU-Eigenvergabe; im deutschen Verfahren nur Integritätsanker neben § 53 VgV und Portalvorgabe. Portaldateiliste und Quittung vorrangig sichern.
- OLG Düsseldorf, Beschluss vom 13.05.2019, Verg 47/18: Klickweg und fehlende technische Anlage können den vollständigen und direkten Unterlagenzugang widerlegen.
- OLG Düsseldorf, Beschluss vom 12.06.2024, Verg 36/23: Bei Vorgängen in der Sphäre der Vergabestelle oder eines Mitbewerbers dürfen belastbare Indizien genügen; Tatsachenkern, Erkenntnisquelle und plausible Folge müssen konkret bleiben.
- OLG Düsseldorf, Beschluss vom 24.03.2021, Verg 34/20: Bei Wertungsdaten nicht nur Punkte, sondern konkrete Gründe, Antworten/Eingaben und Quervergleich als Akteneinsichtsziele benennen.

## Output

Belegliste für Rüge, VK-Antrag oder OLG-Beschwerde.

Bei Legacy-Quellen zusätzlich Herkunftszonen-, Hash- und Transformationsmanifest, Tatsachenkern-/Gegenhypothesenmatrix, Akteneinsichtsziele, Anlagenverzeichnis und Schwärzungsvorschlag nach `assets/templates/beweiskette-systemexport.md`.
