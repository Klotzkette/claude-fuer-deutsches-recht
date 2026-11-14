---
name: unterlagen-und-lv-datenformate-auslesen
description: "Vergabeunterlagen, LV und Preisblätter in GAEB, XML, Excel, PDF oder ZIP inventarisieren, Positionen auslesen, Widersprüche, Pflichtfelder, Rügepunkte und Abgabeformate markieren. Output Unterlagenmatrix, LV-Tabelle, Format-Risikoliste und nächster Angebotsarbeitsschritt."
---

# Unterlagen und LV-Datenformate auslesen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


Einsatzlage: Der Bewerber lädt Unterlagen, ein ZIP, ein Leistungsverzeichnis, GAEB-Dateien, XML, Excel-Preisblätter, PDF-Formulare oder Portalexporte hoch und braucht daraus eine belastbare Linie für Bewerbung, Rüge und Angebot.

## Referenz

Bei technischen Formaten [FORMATE-UND-SCHNITTSTELLEN.md](../../references/FORMATE-UND-SCHNITTSTELLEN.md) laden. Bei SAP/ERP/CRM/AVA/DMS/Portal/API/MCP zusätzlich [LEGACY-SYSTEME-INTEGRATION.md](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden.

## Sofortmodus

1. Akteninventar erstellen: Bekanntmachung, Bewerbungsbedingungen, Aufforderungsschreiben, Leistungsbeschreibung, LV, Preisblatt, Eignung, Zuschlagsmatrix, Vertragsentwurf, Anlagen, Fragen/Antworten.
2. Format je Datei bestimmen: GAEB D/P/X, XML, Excel, PDF, ZIP, Bild, E-Mail oder Portaltext.
3. Fristen und Rügepräklusion zuerst markieren: Angebots- oder Teilnahmefrist, Fragenfrist, Rügefrist, Bindefrist.
4. Angebotsrelevante Pflichtfelder extrahieren: Lose, CPV, Positionen, Mengen, Einheiten, Preisfelder, Eignungsnachweise, Erklärungen, Signaturform.
5. Widersprüche markieren: Bekanntmachung gegen Unterlagen, PDF gegen Excel, GAEB gegen Preisblatt, Mengen gegen Vertrag, Zuschlagskriterien gegen Matrix.
6. Produkt-, Material-, System- und Schnittstellenvorgaben markieren, wenn sie Gleichwertigkeit einschränken.
7. Externe Links, Live-Dashboards und Datenräume markieren: Was ist nur ergänzend und was muss als unveränderbarer Angebotsbestandteil hochgeladen werden?
8. Bei Systemexporten Quellschlüssel, Stichtag, Einheit, Transformation, Gültigkeit und Freeze-Bedarf bestimmen.
9. Nur echte Lücken fragen. Wenn die Datei die Information enthält, nicht nachfragen.

## GAEB und LV

- Phase nicht raten: D83/P83/X83 regelmäßig Angebotsaufforderung, D84/P84/X84 regelmäßig Angebot oder Preisangebot. Header und Portalhinweise prüfen.
- Wenn der Nutzer G48 nennt, als ungesicherte Formatangabe behandeln und anhand Datei, Header und Begleitschreiben aufklären.
- Positionen immer mit Ordnungszahl, Menge, Einheit, Kurztext, Langtext, Bedarfs-/Eventualposition, Los und Preisfeld ausgeben.
- Originaldatei nicht verändern. Zunächst eine normalisierte Arbeitstabelle erstellen.
- Wenn kein nativer GAEB-Schreiber verfügbar ist, klar trennen: fachliche Bepreisungsdaten ja, native Abgabedatei erst nach Konverter/Portalvalidierung.

## Rechtsprechungsanker

- EuGH, Urteil vom 16.04.2026, C-568/24, Sof Medica, ECLI:EU:C:2026:305: Typ-, Größen-, System- und Schnittstellenvorgaben müssen Gleichwertigkeit zulassen, sofern sie nicht unvermeidbar aus dem Auftragsgegenstand folgen. Detaillierte Pflichtfelder deshalb auf funktionale Alternativen prüfen.
- EuGH, Urteil vom 16.01.2025, C-424/23, DYKA Plastics: Bei LV- und Formatprüfung nicht nur den Text lesen, sondern prüfen, ob GAEB/XML/Excel/PDF eine gleichwertige Lösung praktisch zulässt.
- EuGH, Urteil vom 03.07.2025, C-534/23 P und C-539/23 P, Instituto Cervantes: unmittelbar EU-Eigenvergabe; im deutschen Verfahren nur Integritätsanker neben § 53 VgV und Portalvorgabe. Verlangte Unterlagen im vorgesehenen System hochladen.
- OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24: Bei behaupteter Bestandskompatibilität die eigene Alternative mit Schnittstelle, Migration, Systemsicherheit und Gewährleistungszuordnung belegen.
- OLG Düsseldorf, Beschluss vom 13.05.2019, Verg 47/18: verstreute, unvollständige oder nur auf Anforderung erreichbare technische Unterlagen als Zugangs- und Rügeproblem erfassen.

## Output

Liefer immer vier Blöcke:

1. Unterlagenmatrix mit Datei, Format, Zweck, Pflicht, Fristbezug, Risiko.
2. LV-/Preisblatt-Tabelle mit allen Angebotspositionen oder Hinweis, warum ein nativer Parser gebraucht wird.
3. Bewerber-To-do-Liste: Nachweise, Preise, Konzepte, Rückfragen, Rügepunkte, Uploadformat.
4. Nächster Arbeitsschritt: Angebot bauen, Rüge formulieren, Bieterfrage stellen oder Datei technisch validieren.
5. Bei Legacy-Anbindung: Anschlussmatrix, Hash- und Mapping-Manifest, Delta-Protokoll und Freigabeauftrag.
6. Angebotsfreeze-Hinweis: verbindlicher Upload, nur ergänzender Link, Freeze-Zeit, Hash und Portalquittung.

## Schnittstellen-Vorbereitung

Wenn ein MCP-, Portal- oder Serverwerkzeug angeschlossen werden soll, erstelle einen Schnittstellenauftrag mit Zielsystem, Aktion, Dateien, Hashes, Authentifizierung, Trockenlauf, Freigabe und erwarteter Rückmeldung. Kein Upload ohne ausdrückliche Freigabe.
