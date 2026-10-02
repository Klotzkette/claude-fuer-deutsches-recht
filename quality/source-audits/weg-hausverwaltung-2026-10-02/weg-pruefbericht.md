# WEG-Hausverwaltung: Quellen- und Skillprüfung am 02.10.2026

## Umfang

Alle 93 bestehenden Skills wurden inventarisiert sowie auf Struktur, Frontmatter, relative Markdownlinks und konkrete auffällige Norm-/Rechtsprechungsmuster durchsucht. 46 Skills wurden gezielt geändert; es wurden keine Skills hinzugefügt oder gelöscht. Elf Kernskills wurden in ihrem Fachtext neu geordnet; zwei weitere Abrechnungsskills erhielten eine ausführliche fallbezogene Mietüberleitung. Die Metadaten dieser 13 zentralen Skills nennen jetzt konkrete Auslöser und Ergebnisse.

Der Lauf ist keine vollständige Neuprüfung jeder technischen DIN-Vorgabe, jeder Förderkondition oder jedes landesrechtlichen Nebensatzes in allen 93 Skills. Er vertieft die beauftragten WEG-Verwaltungsfragen, korrigiert identifizierte Fehler und enthält überprüfbare Anwendungsgrenzen statt einer pauschalen Aktualitätsbescheinigung.

## Quellen und tatsächliche Lektüre

`weg-quellen.json` protokolliert 30 amtliche BGH-Entscheidungs-PDFs, darunter zehn Entscheidungen aus 2026, sowie 23 WEG-/Nebenrechtsnormen und sechs ergänzende Marketing-/Datenschutznormen. Jede PDF-Fundstelle enthält URL, Dateiname, Umfang, SHA-256, tatsächlich gelesene Randnummern, verwendete Aussage und Grenze. Ein Download allein wurde nicht als Volltextlektüre ausgegeben. Die bezeichneten Passagen wurden am amtlichen Text gelesen; bei V ZR 18/25 wurde der gesamte Text einschließlich Sachverhalt und rechtlicher Einordnung gelesen. Bibliografische Angaben aus dort zitierten Kommentaren wurden nicht als selbst gelesene Literatur übernommen.

Die älteren juris-Downloadrouten lieferten teils eine Sicherheitshinweisseite oder Fehler statt einer Entscheidung. In solchen Fällen wurden die amtlichen statischen BGH-PDFs abgerufen und anhand Aktenzeichen, Datum, Dokumentkopf und Text geprüft. Die heute tatsächlich verwendeten Quellen sind mit Hash protokolliert. Einzelne Norm-Browserabrufe scheiterten; die betreffenden amtlichen HTML-Dateien wurden zusätzlich erfolgreich abgerufen und gelesen. Der bestehende TDDDG-Normlink wurde von dem fehlerhaften Verzeichnis `tdddg` auf das amtliche Verzeichnis `ttdsg` berichtigt.

Die gesonderte Prüfung von Mietrecht, Befall und Datenschutz ist im unabhängigen Bericht `miet-datenschutz-quellen.md/.json` dokumentiert. Dessen 14 Quellenkarten wurden mit Aussagen und Grenzen in die installierbare Pluginreferenz `references/miete-befall-datenschutz-oktober-2026.md` übernommen. Diese Quellenkarten umfassen Gerichtsurteile, Normen und Behördeninformationen; sie sind nicht als 14 höchstrichterliche Entscheidungen zu zählen.

## Inhaltliche Verbesserungen

1. Die Jahresabrechnung führt Rechnung, Duplikat, Gutschrift und Bankbewegung zum selben Geschäftsvorfall zusammen; interne Kontoumbuchungen werden nicht nochmals als Gebäudekosten verteilt. Beschlossene Soll-Vorschüsse, tatsächliche Zahlungen, alte Rückstände und neue Abrechnungsspitze sind getrennt. Vermögensbericht, Korrekturversion und möglicher neuer Beschluss werden mit einem verständlichen Eigentümerbrief verbunden.
2. V ZR 50/25 vom 24.04.2026 präzisiert angemessene Kostenverteilung; bloße Willkürkontrolle und ein universeller sachlicher Änderungsgrund wurden korrigiert. V ZR 7/25 vom 27.03.2026 beseitigt die starre Drei-Angebote-Regel, erhält aber die wirtschaftlich tragfähige Informationsgrundlage. Es wird nicht zu ungeprüfter Vergabe geraten.
3. V ZR 18/25 vom 27.02.2026 konkretisiert GdWE-Haftung über Pflichtverletzung, Reaktionszeit, Kausalität und hypothetischen Verlauf. Direkte deliktische Verwalterhaftung bleibt neben GdWE-Anspruch und Regress eine gesonderte Frage. Selbstbehalt, Schaden und Mietumlage werden getrennt.
4. Umlauf-Absenkungsbeschluss und Sachbeschluss werden anhand V ZR 190/25 vom 17.07.2026 mit eigenen Daten/Fristen behandelt. Stimmrechtsausschlüsse bei Bestellung und § 28-Entscheidungen werden anhand V ZR 189/24 vom 27.02.2026 geprüft. Klimasplit-Abwägung und Streetart-Bestimmtheit werden nur in passenden Fällen auf V ZR 162/25 beziehungsweise V ZR 165/25 gestützt.
5. Beschlussentwürfe bestimmen Entscheidung, Anlagenversion, Betrag, Kostenregel, Fälligkeit und Vertretung. Der frühere Entwurf, die GdWE solle einen Anspruch gegen sich selbst geltend machen, wurde entfernt. Verwaltervertragsunterzeichnung nach § 9b Abs. 2 und Höchstdauer der Bestellung nach § 26 Abs. 2 sind getrennt behandelt.
6. Falsche Aktenzeichen-/Gegenstandszuordnungen wurden berichtigt: V ZR 33/23 ist kein Fristenfall; V ZR 57/12 kein pauschaler Badabdichtungsfall; V ZR 251/21 stammt vom 16.06.2023 und betrifft Abrechnungskorrektur, nicht Sonderhonorar. VI ZR 1244/20 ist ein Hotelbewertungsfall. Die nicht tragfähige alte Jameda-Kombination wird nicht fortgeführt.
7. § 20 Abs. 2 Nr. 1/2 WEG (Barriereabbau/E-Mobilität), die selbständigen Alternativen des § 21 Abs. 2 WEG und das ZVG-Hausgeldvorrecht wurden korrigiert. Ein Wirtschaftsplanbeschluss wird nicht mehr als Vollstreckungstitel bezeichnet.
8. Mietüberleitung verwendet den tatsächlichen Mietvertrag, § 556a Abs. 3 BGB und gesonderte Fristen; elektronische Belegeinsicht nach § 556 Abs. 4 seit 2025, Zahlungs-/Verbrauchsbelege und VIII ZR 6/24 vom 20.05.2026 werden konkret eingearbeitet. Die CO2-Änderung 2026 wird nicht auf die erst 2028/2029 ansetzenden Kostenfolgen oder auf 2025 rückdatiert. Mietkürzungsrechte werden nicht auf Hausgeld übertragen.
9. Diebstahl und Bettwanzen führen zu belegtem Vorfall, Fachbefund, Auftrag, Nachkontrolle, Versicherungsprüfung und gesonderter Verschuldensprüfung. Meldende Bewohner gelten nicht als Verursacher. Kameraüberwachung erfordert Zweck, Alternativen, Ausschnitt, Zugriff und begründete Löschung; kein pauschaler 72-Stunden-Freibrief.
10. Datenschutzrollen und AVV werden funktional geprüft, keine automatische AVV-Pflicht allein wegen Zugriffs durch Steuerberatung/Inkasso. Pauschale Speicherfristen und automatische Schadenersatzbehauptungen wurden beseitigt. Persönlichkeitsbilder sind nach KunstUrhG/DSGVO zu prüfen; der falsche Verweis auf § 22 UrhG entfällt.

## Validierung

- Skill-creator `quick_validate.py`: alle 93 Skills bestanden.
- Eigene Prüfung: 93 eindeutige Namen, Frontmattergrenzen eingehalten, keine fehlenden Ziele relativer Markdownlinks innerhalb der Skills.
- `git diff --check` für die bearbeiteten Skills/Referenzen: bestanden.
- Repository-Strukturvalidator: zum Prüfzeitpunkt ausschließlich drei erwartete Integrationsmeldungen, weil die vier parallel erstellten neuen Testakten noch nicht in Tabelle/ZIP-Links von `testakten/README.md` eingetragen waren. Keine Skill-Strukturmeldung. Der abschließende Integrationslauf liegt beim Hauptagenten.

Die SHA-256-Werte der abschließend gelesenen Skilldateien stehen in `weg-skill-inventar.json`. Testakten, Standalone-Prompts, Releaseversionen und Repositoryübersichten wurden von diesem Arbeitszweig nicht geändert.
