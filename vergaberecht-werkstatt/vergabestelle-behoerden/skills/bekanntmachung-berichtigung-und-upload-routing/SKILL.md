---
name: bekanntmachung-berichtigung-und-upload-routing
description: "Bekanntmachung, Berichtigung, Fristverlängerung, Amtsblatt-, TED-, DVAL- oder Portalveröffentlichung nach Einwänden vorbereiten. Output Entscheidungsvorlage, eForms-/Portal-Feldliste, Uploadauftrag, Freigabecheck und Vergabeaktenvermerk."
---

# Bekanntmachung, Berichtigung und Upload-Routing

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


Einsatzlage: Die Vergabestelle muss nach Einwänden, Bieterfragen, Rügen, technischen Fehlern oder geänderten Unterlagen entscheiden, ob Berichtigung, Fristverlängerung, neue Bekanntmachung, Aufhebung oder Portalveröffentlichung erforderlich ist.

## Referenz

Bei technischen Formaten und Schnittstellen [FORMATE-UND-SCHNITTSTELLEN.md](../../references/FORMATE-UND-SCHNITTSTELLEN.md) laden. Bei SAP/ERP/AVA/DMS/Portal/API/MCP zusätzlich [LEGACY-SYSTEME-INTEGRATION.md](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden.

## Entscheidungslogik

1. Einwand erfassen: Wer, wann, welches Dokument, welche Datei, welche Position, welche Rechtsfolge.
2. Berechtigung prüfen: Unklarheit, Widerspruch, diskriminierende Spezifikation, falsches Format, fehlende Anlage, fehlerhafte Frist, falscher CPV oder Portalfehler.
3. Abhilfe wählen: Antwort ohne Änderung, Bieterinformation, Berichtigung, Fristverlängerung, neue Unterlagenversion, Aufhebung.
4. Fristwirkung dokumentieren: Angebotsfrist, Teilnahmefrist, Fragenfrist, Bindefrist, Stillhaltefristen.
5. Veröffentlichungsweg bestimmen: TED/eForms, DVAL, bund.de, Landesportal, kommunales Portal, Vergabeplattform.

## eForms und Portal-Feldliste

Vor Versand eine Feldliste erzeugen:

| Feldgruppe | Prüfung |
|---|---|
| Verfahren | Notice-ID, Verfahrensart, Lose, CPV, Rechtsgrundlage |
| Fristen | Angebots-/Teilnahmefrist, neue Frist, Zeitzone, Fristgrund |
| Unterlagen | Link, Version, geänderte Dateien, Lesefassung |
| Eignung/Zuschlag | Kriterien, Gewichtung, Mindestanforderungen |
| Kontakt | Vergabestelle, Kommunikationsweg, Fragenkanal |
| Nachweis | Portal-ID, TED-ID, Bestätigungsdatei, Zeitstempel |

## Uploadauftrag

Wenn ein Portal, Server oder MCP-Werkzeug angebunden ist oder vorbereitet wird:

1. Zielsystem und Aktion bestimmen: validieren, hochladen, ersetzen, veröffentlichen, stoppen.
2. Dateien mit Hash, Version und Freigabestatus listen.
3. Authentifizierung und Rollen klären: wer darf senden, wer gibt frei.
4. Trockenlauf verlangen, wenn das Zielsystem Validierung erlaubt.
5. Fehlerliste in Bearbeitungsliste umwandeln.
6. Versand erst nach ausdrücklicher Freigabe.
7. Bei Legacy-Systemen zusätzlich Mapping-Manifest erzeugen: Quellfeld, Zielfeld, Transformation, Delta, Import-/Export-ID und Rollback-Hinweis.

## Output

Liefere eine Entscheidungsvorlage:

- Kurzsachverhalt und Einwand.
- Bewertung berechtigt oder nicht berechtigt.
- Maßnahme: Berichtigung, Fristverlängerung, neue Unterlagen, Aufhebung oder keine Änderung.
- Feldliste für eForms/Portal.
- Uploadauftrag mit Freigabecheck.
- Vergabeaktenvermerk mit Datum, Bearbeiter, Version und Nachweis.
