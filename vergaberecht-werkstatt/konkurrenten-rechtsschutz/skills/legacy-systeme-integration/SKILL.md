---
name: legacy-systeme-integration
description: 'Konkurrenten sichern Portal-, TED-, eForms-, GAEB-, XML-, Excel-, DMS-, E-Mail-, API-, MCP- und eigene ERP-/AVA-Daten als zulässige Beweise. Bei Systemexport, Versionstreit, Uploadfehler, Produktbindung, Wertungsdaten, Akteneinsicht, Hash- oder Anlagenpaket automatisch einsetzen.'
---

# Systemexporte in einen zulässigen Konkurrentenbeweis überführen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Automatisch einsetzen

Dieser Skill ist der Erstpfad, sobald ein Konkurrentenordner Portalexporte, eForms/TED-Stände, GAEB/XML/Excel/PDF, Uploadlogs, E-Mails, Akteneinsichtsauszüge, eigene Kalkulationsdaten, APIs oder MCP-Werkzeugdaten enthält. Auch ein Versionsunterschied, Screenshot oder auffälliger Dateiname löst ihn aus.

Sofort [`LEGACY-SYSTEME-INTEGRATION.md`](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden. Bei Formatangriff zusätzlich `unterlagen-lv-formatangriff`, bei Portalereignis `beweisstrategie-und-portalnachweise`, bei Schwärzung `akteneinsicht-schwaerzung-belegmatrix` einsetzen.

## Erste 90 Sekunden

1. Herkunftszone festlegen: eigene Sphäre, öffentlich, Verfahrenszugang, befugter Dritter, nur Indiz oder unzulässig/ungeklärt.
2. Original sichern: Datei/URL/Endpunkt, Nutzerrolle, Zeit, Zeitzone, Version, ID, Hash und Signatur/Siegel.
3. Arbeitskopie und Transformation getrennt erfassen.
4. Tatsachenkern neutral formulieren: Was belegt die Quelle unmittelbar?
5. Angriff zuordnen: Zugang, Frist, Produkt-/Formatsperre, Wertung, Preis, Eignung, § 135 GWB oder Vertragsänderung.
6. Kausalität, Zuschlagschance und fehlenden Beleg bestimmen.
7. Einen ersten Output wählen: Rügeanlage, Belegmatrix, Akteneinsichtsziel, VK-Anlage oder OLG-Anlagenpaket.

## Beweisquellenkarte

| Quelle | unmittelbarer Tatsachenkern | typischer Angriff | Pflichtsicherung |
|---|---|---|---|
| TED/eForms/DVAL/Portal | veröffentlichter Stand, Frist, Link, Berichtigung | Bekanntmachung, Zugang, de-facto-Lage | ID, URL, Snapshot, Abrufzeit, Hash |
| eigener Portalaccount | Nachricht, Upload, Fehler, Serverzeit, Quittung | Frist, Gleichbehandlung, Abgabe | vollständiger Export, Supportticket, angenommene Dateiliste |
| GAEB/XML/Excel/PDF | OZ, Pflichtfeld, Sperre, Widerspruch, Version | Produkt-/Formatsperre, Transparenz | native Datei, Schema, Lesefassung, Delta |
| eigene ERP-/AVA-Kalkulation | eigene Alternative, Preis-/Aufwandswirkung | Gleichwertigkeit, Kausalität, Billigzuschlag | Leistungsidentität, Preisstand, Geheimnisschutz |
| Akteneinsicht/Wertungsmatrix | Punkt, Grund, Aufklärung, Nachweis | Wertung, Eignung, Preis, Dokumentation | Aktenstelle, Schwärzung, Seiten-/Zellbezug |
| E-Mail/DMS/Supportlog | Zugang, Antwort, Abhilfe, Zustellung | Kenntnis, Rügefrist, Portalstörung | Header, Verlauf, Originalpfad, Zeitstempel |

## Angriffsmapping

| Quelle/Fundstelle | Tatsachenkern | Gegenhypothese | Norm/Fallanker | Kausalität/Chance | Antrag/Anlage |
|---|---|---|---|---|---|
| [Datei, Seite/Zelle/OZ] | [neutral] | [mögliche Erwiderung] | [eintragen] | [konkret] | [Rüge/VK/Akteneinsicht] |

Kann der Tatsachenkern nicht sauber formuliert werden, keinen Schriftsatzvorwurf ausgeben. Stattdessen Beweislücke und rechtmäßigen Beschaffungsweg benennen.

## Rechtsprechungsgates

1. **Typ-/System-/Schnittstellenangriff:** § 31 VgV, EuGH, 16.04.2026, C-568/24, *Sof Medica*, und C-424/23, *DYKA Plastics*. Unvermeidbarkeit, fehlende Gleichwertigkeit, funktionale Alternative und konkrete Wettbewerbswirkung getrennt belegen.
2. **Bestandskompatibilität als Gegenargument:** OLG Düsseldorf, 10.07.2024, Verg 2/24. Migrationspfad, Schnittstelle, Systemsicherheit, Gewährleistung und Umstellungsaufwand der Alternative konkretisieren; pauschaler Offenheitsruf reicht nicht.
3. **Unterlagenzugang:** § 41 VgV, OLG Düsseldorf, 13.05.2019, Verg 47/18. Klickweg, fehlende Anlage, notwendige Registrierung/Anforderung, Abrufzeit und Fristwirkung sichern.
4. **Fristfester Upload:** EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, betrifft unmittelbar eine EU-Eigenvergabe. Im deutschen Verfahren nur als Integritätsanker neben § 53 VgV und der konkreten Portalvorgabe nutzen; eigene Uploadquittung und angenommene Dateien beweisen.
5. **Wertungsdaten:** § 8 VgV, OLG Düsseldorf, 24.03.2021, Verg 34/20. Punktzahl allein genügt nicht; Eingabedaten, konkrete Gründe, Antworten und Quervergleich als Akteneinsichtsziele angeben.
6. **Begrenzter Einblick:** OLG Düsseldorf, 12.06.2024, Verg 36/23. Redlich für wahrscheinlich gehaltener Vortrag ist möglich, braucht aber Indiz, Erkenntnisquelle, Tatsachenkern und plausible Folge.

## Beweiskette und Versand

1. Original und Arbeitskopie getrennt hashen.
2. Jede Transformation mit Werkzeug, Regel und Verantwortlichem protokollieren.
3. Geheimnisschutz und Schwärzung je Anlage prüfen.
4. Lücke in ein präzises Akteneinsichts- oder Ermittlungsziel übersetzen.
5. Anlagenzeichen, Schriftsatzfundstelle und Hash verbinden.
6. Rüge/VK/OLG-Übermittlung erst nach ausdrücklicher Freigabe.
7. Empfangsbestätigung, Server-/Gerichtszeit und angenommene Dateiliste sichern.

## Last- und Fortsetzungsregel

- Ab 50 Dateien oder 250 MB Metadaten vor Inhalten lesen und in Paketen von höchstens 20 Dateien oder 100 MB arbeiten.
- Große GAEB-, PDF- und Office-Dateien einzeln verarbeiten. Parallel nur Inventar- und Prüfschritte ausführen, die keine Vollkonvertierung benötigen.
- Für jedes Paket `Quelle | Hash | Status | Tatsachenkern | Fehler | Anlagenziel | nächster Lauf` speichern; unveränderte Quellen nicht erneut auslesen.
- Eine fehlerhafte Datei wird als Beweislücke oder Akteneinsichtsziel markiert. Fristsicherung und unabhängige Angriffslinien werden fortgesetzt.
- Nach Unterbrechung am letzten vollständigen Paket fortsetzen; Rüge-, VK- oder OLG-Versand nie automatisch wiederholen.

## Stoppsignale

- fremder interner Zugang oder ungeklärte Herkunft;
- Screenshot ohne Originalkontext;
- nicht protokollierte OCR-, Tabellen- oder Formatänderung;
- Schlussfolgerung weiter als Tatsachenkern;
- Geheimnisoffenlegung ohne Erforderlichkeit;
- Versand ohne Freigabe.

## Pflichtoutput

Liefere in dieser Reihenfolge:

1. Herkunftszonen- und Beweisinventar.
2. Hash- und Transformationsmanifest.
3. Tatsachenkern-/Gegenhypothesen-/Angriffsmatrix.
4. Akteneinsichts- und Ermittlungsziele.
5. Anlagenpaket mit Geheimnisschutz und Versandauftrag.
6. Ausgefüllte Vorlage [`beweiskette-systemexport.md`](../../assets/templates/beweiskette-systemexport.md).
