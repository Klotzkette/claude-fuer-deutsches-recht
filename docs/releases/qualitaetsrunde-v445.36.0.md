# 1. Qualitätsrunde 445.36.0

Die Auswahl innerhalb der Plugins wird auf höchstens 20 fachlich zusammenhängende Arbeitswege begrenzt. Die vollständigen bisherigen Fachtexte, Vorlagen, Rechner und Quellen bleiben erreichbar. Alle 315 Plugins behalten ihre Identität; auch die im Insolvenzrechtsordner gemeinsam verzeichneten Plugins bleiben separat.

## 1.1. Fachliche Ordnung

224 Plugins mit zu vielen Einzelskills wurden konsolidiert. Im gesamten Repository sind 3.175 Skills auswählbar, zuvor waren es 23.433. 21.883 bisherige Skills bleiben als vollständige `FACHINHALT.md`-Module erhalten. Die neuen Arbeitswege wählen die einschlägigen Module auftragsbezogen aus und lesen sie vor der Teilprüfung. Eine eigene Fachbibliothek pro betroffenem Plugin sowie aktualisierte Verzeichnisse machen diese Zuordnung sichtbar.

Der Quellenbestand ist durch ursprüngliche Hashes und invertierbare Verweiskorrekturen abgesichert. Pfadwechsel dürfen weder lokale Werkzeuge verlieren noch alte Aufrufe auf einen nicht mehr auswählbaren Skill richten. Regressionen prüfen unter anderem die 20er-Grenze, fehlende Fachmodule, verlorene Referenzen, falsche Hashbindungen und nicht portable Paketverweise.

## 1.2. Juristische Korrekturen

Die Bestandsprüfung erfasst alle 315 Pluginprofile. Elf Entscheidungen wurden gezielt anhand ihrer amtlichen Volltextpassagen eingeordnet. Aktualisiert wurden unter anderem die Reichweite der Vermittlungsauskunft beim Annahmeverzugslohn, DSGVO-Auskunft und Prozessdatenverwendung, Insolvenzfeststellungsbescheide sowie verfassungs- und unionsrechtliche Anker bis zum 12. November 2026.

Konkrete Fehler wurden berichtigt: etwa eine behauptete allgemeine Doppelanmeldungspflicht bei Abtretung einer Insolvenzforderung, unzutreffende insolvenzrechtliche Fristen, die falsche Grundlage der DSGVO-Fristberechnung und eine erfundene Nichtigerklärung des historischen § 370a AO. Der [Quellenbericht](../../quality/source-audits/2026-11-14/README.md) nennt Aussage, Grenze und Nachweis jeder gezielten Korrektur.

Die Runde ist keine neue juristische Volltextprüfung sämtlicher übernommener Fachmodule. Vier bereits offene Profile mit 31 Dateireviews bleiben entsprechend gekennzeichnet. Es werden keine neuen Live-Modelltests behauptet.

## 1.3. Releaseumfang

Das Komponentenrelease enthält genau 733 Dateien für 226 aktualisierte Plugins:

- 226 native Plugin-ZIPs und acht bereits bestehende portable Varianten;
- 495 vorhandene Werkstatt-, Schnellstart- und Schwerpunktdateien in Markdown bzw. TXT;
- das KI-Kanzlei-Handbuch und sein Einzel-PDF-ZIP mit allen 30 Fachmodulen, acht aktiven Arbeitswegen und 323 Gesamtseiten;
- `release-bestand.json` und `checksums-sha256.txt`.

Keine Testakte und kein bestehendes Release wird ersetzt. Der Quellstand bleibt mit den unveränderten Aktenrouten verbunden. Auch ältere Handbuchdateien bleiben erhalten.

## 1.4. Veröffentlichung und Prüfbarkeit

Der Workflow `.github/workflows/skill-quality-release.yml` verlangt den vollständigen geprüften Main-Commit. Der Builder vergleicht jedes ZIP-Mitglied mit dessen Quelldatei, prüft Manifestversionen, zulässige Skillzahlen, Fachmodule, lokale Verweise und Handbuchnachweise. Inventar und Prüfsummen werden vom Builder erzeugt.

Tag und Release werden erst nach den Prüfungen angelegt. Vor der Freigabe werden sämtliche Assets unabhängig heruntergeladen und erneut gegen Prüfsummen und Quellen verglichen. Bestehende veröffentlichte Tags und Releases werden nicht überschrieben; ein vorhandener Entwurf kann ausschließlich am identischen Commit fortgesetzt werden. Die Veröffentlichung berücksichtigt die API-Ratengrenzen.

[Bedienung, Umfang und Prüfgrenzen](../skill-ordnung-und-qualitaet.md) · [Download-Index](../../ASSET_INDEX.md)
