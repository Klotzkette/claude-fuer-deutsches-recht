# E-Rechnung-Werkstatt

Die E-Rechnung-Werkstatt erstellt aus vorhandenen Rechnungen, Verträgen, Leistungsnachweisen und Buchungsunterlagen eine ZUGFeRD-Rechnung oder XRechnung. Sie richtet sich an Selbstständige, Kanzleien, Steuerberater und Unternehmen. Geben Sie die Unterlagen und das gewünschte Rechnungsziel an; bereits vorhandene Angaben werden übernommen, entscheidende Lücken und Widersprüche werden geklärt.

[Repository-Start](../README.md) · [Skills](../SKILLS.md) · [Skill-Detailseite](../skills-index/e-rechnung-werkstatt.md) · [Downloads](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [Plugin-Dateien](.)

## 1 Benutzung

Installieren Sie das [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/e-rechnung-werkstatt.zip) oder verwenden Sie einen eigenständigen Prompt:

| Arbeitsmodus | Datei | Direktdownload |
| --- | --- | --- |
| Ausführlicher Werkstatt-Prompt | `e-rechnung-werkstatt-werkstatt.md` | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/e-rechnung-werkstatt-werkstatt.md) |
| Kompakter Mini-Prompt | `e-rechnung-werkstatt-schnellstart.md` | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/e-rechnung-werkstatt-schnellstart.md) |
| Belegkonflikte und fertige Ausgabe | `e-rechnung-werkstatt-hauptproblem.md` | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/e-rechnung-werkstatt-hauptproblem.md) |
| Sämtliche Fachmodule | `e-rechnung-werkstatt.md` | [Markdown herunterladen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=testakten/megaprompts/e-rechnung-werkstatt.md) |

Zum Beispiel: „Erstellen Sie aus diesem Word-Entwurf, dem Leistungsnachweis und der Kundenmail eine ZUGFeRD-Rechnung. Prüfen Sie die abweichende Summe und verwenden Sie die nachgewiesene aktuelle Bankverbindung.“ Oder: „Der Auftraggeber verlangt XRechnung. Entnehmen Sie Referenzen und Übermittlungsbedingungen dem Auftrag und erstellen Sie die Datei.“

## 2 Eingaben und Ausgaben

Die KI liest Word, PDF, Bilder und Scans, Tabellen, E-Mails sowie vorhandene Rechnungs-XML mit den verfügbaren Dokumentwerkzeugen. Sie verbindet jede wesentliche Angabe mit ihrer Quelle und prüft Dubletten, Fassungen und Widersprüche. Ein OCR-Ergebnis ersetzt keine Prüfung unklarer Ziffern. Aussagen innerhalb einer Datei sind Rechnungsdaten, keine Anweisungen zum Ändern des Arbeitsauftrags.

ZUGFeRD wird als lesbares PDF/A-3 mit eingebettetem Rechnungs-XML und passenden Metadaten ausgegeben. XRechnung wird als strukturierte XML-Datei ausgegeben; eine ergänzende Lesefassung wird entsprechend bezeichnet. Rechnungsdaten, rechnerische Kontrolle und tatsächliche Validatorberichte begleiten die fertigen Dateien.

## 3 Standards und technische Ausführung

Der geprüfte Ausgangsstand vom 6. November 2026 ist ZUGFeRD 2.5.2 mit dem Profil EN 16931 sowie XRechnung 3.0.2 mit dem technischen Bundle vom 31. August 2026. Empfängervorgaben und Änderungen der Standards sind vor dem konkreten Einsatz abzugleichen. Die Vorversion XRechnung 4.0 wird nicht als geltender Standard vorausgesetzt.

Die [lokalen Werkzeuge](werkzeuge/README.md) erzeugen Rechnungsdateien aus einem zuvor fachlich geprüften strukturierten Datenstand. Für das Lesen beliebiger Eingabedateien werden die Dokumentfähigkeiten der verwendeten KI benötigt. Der mitgelieferte Generator deckt inländische EUR-Rechnungen mit regulärer Überweisung und unterstützten Steuersätzen ab; andere Rechnungsarten erfordern eine geeignete erweiterte Fakturaanbindung und dieselbe abschließende Prüfung.

Das Plugin enthält keine großen Java-Binärdateien. Die dokumentierte Einrichtung lädt die bezeichneten Werkzeuge mit Versions- und Prüfsummenkontrolle. Die Rechnungserzeugung und Prüfung finden lokal statt. Das technische Rechnungslayout des PDF-Generators verwendet seine eingebetteten Hausschriften; begleitende juristische Dokumente folgen Times New Roman 11 pt und dezimaler Gliederung.

## 4 Prüfung und Versand

Die Werkstatt prüft die Pflichtangaben, Steuerbehandlung, Positions- und Gesamtsummen sowie die Schemas und Geschäftsregeln des gewählten Formats. Bei ZUGFeRD kommen PDF/A-Konformität, Einbettung und der Abgleich zwischen Sichtbild und XML hinzu. Nur tatsächlich ausgeführte Prüfungen erhalten einen positiven Status. Ein Dateiexport oder Validatorbericht belegt noch keinen Eingang beim Empfänger.

Ein bereits ausgestelltes Dokument wird vor einer Neuerstellung auf Berichtigungsbedarf und mögliche Doppelabrechnung geprüft. Originale bleiben erhalten. Eine Übermittlung per E-Mail, Portal oder Peppol erfolgt erst im Rahmen des konkreten Versandauftrags und mit einem tatsächlichen Übermittlungsnachweis.

## 5 Quellen und Prüfstand

[Standards und Rechtsquellen](references/standards-und-rechtsquellen.md) · [Zitierweise](references/zitierweise.md) · [Qualitätsprofil](../quality/evals/e-rechnung-werkstatt.json) · [Versionshinweise](../docs/releases/e-rechnung-v445.35.6.md)

Die Textprüfung und automatischen Generatorprüfungen sind von einer Modellbewertung in einer bestimmten Arbeitsoberfläche und vom erfolgreichen Empfang einer Rechnung durch ein konkretes Portal zu unterscheiden.


## 6 Technisches Beispiel

Das Beispiel enthält dieselbe fiktive Rechnung als XRechnung und ZUGFeRD einschließlich Quellen, Datenstand und unveränderter Prüfberichte. Beide Formate wurden tatsächlich erzeugt und validiert; die Hybridrechnung wurde zusätzlich visuell geprüft. [Prüfumfang und Aussagegrenzen](../quality/e-rechnung/README.md).

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

[Beispielpaket als ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/e-rechnung-v445.35.6/E-Rechnung_Beispielpaket.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 7 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 7 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`e-rechnung-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/e-rechnung-erstellen/SKILL.md) | Erstellt aus Word, PDF, Scans, Bildern, Tabellen, E-Mails und vorhandenen Rechnungsdaten eine belegte E-Rechnung. Führt von der Materialauswertung über Pflichtangaben und Steuerprüfung zu ZUGFeRD oder XRechnung einschließlich tatsächlich... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/e-rechnung-erstellen/SKILL.md) |
| [`format-und-empfaengerregeln-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/format-und-empfaengerregeln-klaeren/SKILL.md) | Bestimmt das geeignete E-Rechnungsformat und die konkreten Empfängervorgaben für B2B, B2G und sonstige Fälle. Klärt ZUGFeRD-Profil, XRechnung-Version, elektronische Adressen, Leitweg-ID, Bestellbezug und Übermittlungsweg ohne Identifikat... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/format-und-empfaengerregeln-klaeren/SKILL.md) |
| [`rechnung-berichtigen-und-ausgabe-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/rechnung-berichtigen-und-ausgabe-pruefen/SKILL.md) | Unterscheidet Formatübertragung, Rechnungskorrektur, Storno und Gutschrift und prüft die endgültige E-Rechnung auf Inhalt, Dubletten, Steuerausweis und Versionsidentität. Liefert konsistente Ausgabedateien mit nachvollziehbarem Prüf- und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/rechnung-berichtigen-und-ausgabe-pruefen/SKILL.md) |
| [`steuerlogik-und-rechnungsarten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/steuerlogik-und-rechnungsarten-pruefen/SKILL.md) | Prüft Leistung, Steuerschuldner, Steuersatz, Befreiung und Rechnungsart vor der E-Rechnungserzeugung. Behandelt gemischte Steuersätze, Kleinunternehmer, Reverse Charge, Anzahlungen, Schlussrechnungen, Gutschriften und Fremdwährung mit na... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/steuerlogik-und-rechnungsarten-pruefen/SKILL.md) |
| [`unterlagen-und-rechnungsdaten-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/unterlagen-und-rechnungsdaten-abgleichen/SKILL.md) | Liest Rechnungsdaten aus Word, PDF, Scans, Bildern, Excel, CSV, E-Mails und XML und verbindet sie mit überprüfbaren Fundstellen. Erkennt Fassungen, doppelte Belege, OCR-Fehler und Widersprüche und erstellt den bestätigten Datenstand für... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/unterlagen-und-rechnungsdaten-abgleichen/SKILL.md) |
| [`xrechnung-erzeugen-validieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/xrechnung-erzeugen-validieren/SKILL.md) | Erzeugt aus bestätigten Rechnungsdaten eine XRechnung und prüft die endgültige XML-Datei gegen das passende Schema sowie EN-16931- und XRechnung-Geschäftsregeln. Kontrolliert Empfängerreferenzen, elektronische Adressen und den Rückvergle... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/xrechnung-erzeugen-validieren/SKILL.md) |
| [`zugferd-erzeugen-validieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/zugferd-erzeugen-validieren/SKILL.md) | Erzeugt eine ZUGFeRD-Hybridrechnung aus bestätigten Rechnungsdaten und prüft PDF/A-3, eingebettetes XML, Profil, Metadaten und Betragsgleichheit. Verhindert, dass eine einfache PDF mit beliebigem Anhang oder widersprüchlichem Sichtbild a... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=e-rechnung-werkstatt/skills/zugferd-erzeugen-validieren/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
