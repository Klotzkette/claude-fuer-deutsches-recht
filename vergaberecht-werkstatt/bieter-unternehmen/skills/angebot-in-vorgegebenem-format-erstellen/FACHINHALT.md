---
name: angebot-in-vorgegebenem-format-erstellen
description: 'Bewerbung, Teilnahmeantrag oder Angebot aus ERP, CRM, HR, AVA und DMS im verlangten GAEB-, XML-, Excel-, PDF-, ZIP- oder Portalformat erstellen. Sichert Angebotsfreeze, Nachweisgültigkeit, feste Uploads statt veränderlicher Links, Hashes, Freigaben, Roundtrip und Quittung.'
---

# Angebot im vorgegebenen Format erstellen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


Einsatzlage: Der Bewerber muss Teilnahmeantrag, Angebot, bepreistes LV, Excel-Preisblatt, PDF-Formular, XML-/GAEB-Datei, ZIP-Container oder Portalabgabe im verbindlichen Format liefern.

## Referenz

Bei technischen Formaten [FORMATE-UND-SCHNITTSTELLEN.md](../../references/FORMATE-UND-SCHNITTSTELLEN.md) laden. Bei SAP/ERP/CRM/AVA/DMS/Portal/API/MCP zusätzlich [LEGACY-SYSTEME-INTEGRATION.md](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden.

## Pflichtfragen

Stelle höchstens diese Fragen, wenn sie nicht aus den Unterlagen hervorgehen:

1. Welches Abgabeformat ist verbindlich: GAEB, XML, Excel, PDF, Portalformular oder Kombination?
2. Ist eine native Datei, eine Lesefassung oder beides einzureichen?
3. Welche Signatur- oder Textform verlangt das Portal?
4. Gibt es Dateigrößen, Namenskonventionen, ZIP-Struktur oder Uploadreihenfolge?
5. Erlaubt das Format gleichwertige Produkte, Nebenangebote oder technische Alternativen; falls nein, ist vor Abgabe eine Klarstellung oder Rüge nötig?

## Bau des Angebotsdatenpakets

1. Angebotsstruktur aus den Vergabeunterlagen spiegeln: Lose, Positionen, Nachweise, Konzepte, Formblätter, Anlagen.
2. Pflichtfelder füllen und Pflichtnachweise abhaken.
3. Preise nur in dafür vorgesehenen Feldern eintragen; keine Position löschen oder umnummerieren.
4. Excel: Blattnamen, Formeln, geschützte Zellen und Rundungen erhalten.
5. PDF: Formularfelder füllen oder bei Scan eine saubere Ausfüll-/Anlagenliste erzeugen.
6. XML/GAEB: Schema, Phase und Portalvorgabe prüfen; native Datei nur mit passendem Tool oder validiertem Export herstellen.
7. ZIP/Portal: Dateinamen, Ordnerstruktur, Hashes und Reihenfolge dokumentieren.
8. Legacy-IT: SAP/ERP/CRM/AVA/DMS/SharePoint/E-Mail/SFTP/API/MCP nur über ein Integrations-Cluster anbinden: Quelle, Objekt, Schlüssel, Version, Hash, Angebotsmapping, Freigabe, Rückmeldung.
9. Angebotsfreeze bilden: verbindliche Datei, Lesefassung, nur ergänzender Link, Version, Freeze-Zeit, Hash und fachliche Freigabe.
10. Nach Upload die vom Portal angenommene Dateiliste, Serverzeit und Quittung gegen den Freeze abgleichen.

## Format- und Produktneutralitätscheck

- Wenn die Leistungsbeschreibung oder das Rückgabeformat einen Typ, ein Produkt, Material, Fabrikat, Zertifikat oder proprietäres System erzwingt, EuGH, Urteil vom 16.04.2026, C-568/24, Sof Medica, und EuGH, Urteil vom 16.01.2025, C-424/23, DYKA Plastics, als Prüfanker einsetzen.
- Das Angebotspaket darf keine stillen Vorbehalte enthalten. Wenn Gleichwertigkeit nicht sauber abbildbar ist, getrennt liefern: Angebot nach Vorgabe, Bieterfrage/Rüge, Beiblatt zur gleichwertigen Lösung und Risikoentscheidung.
- EuGH, Urteil vom 03.07.2025, C-534/23 P und C-539/23 P, Instituto Cervantes, betrifft unmittelbar eine EU-Eigenvergabe. Im deutschen Verfahren nur als Integritätsanker neben § 53 VgV und Portalvorgabe nutzen; verlangte Bestandteile fristfest hochladen.
- Macht die Vergabestelle Bestandskompatibilität geltend, nach OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24, die eigene Anschluss-, Migrations-, Sicherheits- und Gewährleistungslösung konkret dokumentieren.

## Plausibilitätscheck

- Alle Lose und Positionen bepreist oder begründet nicht angeboten.
- Einheitspreis, Gesamtpreis, Nachlass, Umsatzsteuerlogik und Rundung konsistent.
- Keine unzulässigen Änderungen an Leistungsbeschreibung, Vertragsbedingungen oder Formblättern; zulässige Gleichwertigkeit nur dort erläutern, wo die Unterlagen es erlauben oder die Vergabestelle sie ausdrücklich zulässt.
- Eignungsnachweise aktuell, unterschrieben oder in Textform bestätigt.
- Bieterfragen, Rügen oder Vorbehalte getrennt vom Angebot behandeln.
- Uploadbestätigung als Beleg sichern.
- Portaldateiliste und Quittungshash stimmen mit dem Freeze-Manifest überein.

## Output

Liefere ein abgabereifes Paketverzeichnis:

| Bestandteil | Datei | Format | Status | Risiko | Aktion |
|---|---|---|---|---|---|
| Angebot/LV | [Datei] | GAEB/XML/Excel/PDF | offen/fertig | niedrig/mittel/hoch | prüfen/hochladen |

Dazu eine kurze Freigabe-Checkliste: Frist, Format, Signatur, Vollständigkeit, Portal, Bestätigung.

Bei Legacy-Anbindung zusätzlich Hash- und Mapping-Manifest, Delta-Protokoll, Geheimnisschutznotiz und Upload- oder Importauftrag ausgeben.

Zusätzlich die Vorlage `assets/templates/angebotsfreeze-systemuebergabe.md` ausfüllen.

## Schnittstellen-Vorbereitung

Wenn ein MCP-, Portal- oder Serverwerkzeug angebunden ist oder angebunden werden soll, bereite den Uploadauftrag vor: Zielsystem, Aktion, Dateien, Hashes, Freigabeperson, Trockenlauf, Uploadzeitpunkt und Rückmeldung. Kein Senden ohne ausdrückliche Freigabe.
