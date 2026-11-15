# Bauträgervertrag-Prüfer

Prüfen Sie Bauträgerverträge, Raten und Sicherheiten, Bausoll, Abnahme und Mängel aus der beauftragten **Erwerber-, Bauträger-, GdWE- oder Verwalterperspektive**. Das Plugin liefert konkrete Urkundenänderungen, Zahlungsantworten, Mandantengutachten, Mängelschreiben und Beschlussentwürfe. Bei einer kompletten Akte beginnen Sie mit [Bauträgerprüfung steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bautraegerpruefung-steuern/SKILL.md); bei einer einzelnen Frage wählen Sie den passenden Arbeitsweg.

<!-- BEGIN direkt-loslegen (autogen) -->
## 1. Einstieg und Arbeitsdateien

[Skill-Gesamtübersicht](../SKILLS.md) · [Plugin-Dateien](.)

| Zugang | Verwendung |
| --- | --- |
| [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.5/bautraegervertrag-pruefer.zip) | Installierbares Paket mit zehn Skills, Fachvertiefungen und Referenzen. |
| [Skill-Verzeichnis](../skills-index/bautraegervertrag-pruefer.md) | Die auswählbaren Arbeitswege mit Beschreibungen. |
| [Werkstatt-Prompt als Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/bautraegervertrag-pruefer-werkstatt.md) | Eigenständiger ausführlicher Prompt für mehrstufige Vertrags- und Aktenbearbeitung. |
| [Mini-Prompt als Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/bautraegervertrag-pruefer-schnellstart.md) | Kompakter Einstieg in eine konkrete Raten-, Klausel- oder Mängelfrage. |
| [Fachbibliothek](FACHMODULE.md) | Alle 60 vollständigen Vertiefungen aus beiden bisherigen Fachbeständen. |

Werkstatt und Mini-Prompt sind eigenständige Arbeitsdateien, keine zusätzlichen Menü-Skills. Testakten werden separat geladen. Für ein Mandat genügt das gemeinsame Plugin `bautraegervertrag-pruefer`.

## In 30 Sekunden starten

> Prüfe die vorhandene Akte aus der bereits benannten Mandatsrolle und erstelle das konkret bestellte Dokument. Lies Urkunde, Anlagen und bisherige Korrespondenz zuerst. Stelle nur entscheidende offene Fragen, arbeite an unabhängigen Teilen weiter und verarbeite neue Angaben in derselben Fassung. Zeige bei Bedarf eine belegte Ratenübersicht, Klauselgegenüberstellung oder Abnahme-/Fristenachse und führe die Bearbeitung bis zum fertigen Text fort.

## Zugeordnete Testakten

Birkenpfuhl bietet Gesamt-PDF, Originaldateien-ZIP und Einzel-PDF-ZIP. Die beiden Vertragsvarianten Hohenwartshofen und Marewald bieten jeweils PDF, bearbeitbare DOCX-/Markdown-Originale und Einzel-PDF-ZIP; zusätzlich gibt es ihre gemeinsame Lesefassung.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Bauträgervertrag Birkenpfuhl - Wohnung 4.27](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/README.md) | [Gesamt-PDF](../testakten/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung/gesamt-pdf/bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung_gesamt.pdf) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung.zip) | [`testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bautraegervertrag-birkenpfuhl-quendel-verbraucherpruefung-einzelpdfs.zip) |
| [Hohenwartshofen](../bautraegervertragspruefer/testakte/bautraegervertrag/README.md) | [Vertrag als PDF](../bautraegervertragspruefer/testakte/bautraegervertrag/bautraegervertrag.pdf) | [Original-DOCX](../bautraegervertragspruefer/testakte/bautraegervertrag/bautraegervertrag.docx) · [Markdown](../bautraegervertragspruefer/testakte/bautraegervertrag/bautraegervertrag.md) | [Einzel-PDF-ZIP](../bautraegervertragspruefer/testakte/bautraegervertrag/bautraegervertrag-einzel-pdfs.zip) |
| [Marewald](../bautraegervertragspruefer/testakte/bautraegervertrag-marewald/README.md) | [Vertrag als PDF](../bautraegervertragspruefer/testakte/bautraegervertrag-marewald/bautraegervertrag-marewald.pdf) | [Original-DOCX](../bautraegervertragspruefer/testakte/bautraegervertrag-marewald/bautraegervertrag-marewald.docx) · [Markdown](../bautraegervertragspruefer/testakte/bautraegervertrag-marewald/bautraegervertrag-marewald.md) | [Einzel-PDF-ZIP](../bautraegervertragspruefer/testakte/bautraegervertrag-marewald/bautraegervertrag-marewald-einzel-pdfs.zip) |

[Gesamter lokaler Aktenbestand mit beiden Vertragsvarianten](../bautraegervertragspruefer/testakte/README.md) · [Alle Testakten und Fachzuordnungen](../testakten/README.md)

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

[Lokale Gesamt-PDF beider Vertragsvarianten](../bautraegervertragspruefer/testakte/gesamt-pdf/testakte_gesamt.pdf)

Die Originalunterlagen, ZIPs und Builder der beiden lokalen Vertragsakten bleiben an ihren bisherigen Pfaden. Birkenpfuhl bleibt in der zentralen Testaktensammlung. Die drei Akten werden separat von der Plugin-Installation verwendet.
<!-- END direkt-loslegen (autogen) -->

## 2. Die Mandatsrolle bestimmt die Bearbeitung

| Rolle | Typische Aufgabe |
| --- | --- |
| Erwerberin oder Erwerber | Fällige Rate, Vorleistungssicherung, Bausoll, Urkundenänderung und konkrete Mängelposition prüfen. |
| Bauträger | Leistung und Forderung belegen, Einwendungen und Sicherungsdefizite würdigen, Antwort oder tragfähigen Verhandlungsvorschlag ausarbeiten. |
| Gemeinschaft der Wohnungseigentümer | Individuelle Rechte, gemeinschaftliche Ausübung, Beschlussumfang, Vertretung und Fristwahrung getrennt prüfen. |
| Verwalterin oder Verwalter | Ausreichende Befugnis feststellen und beauftragte Gemeinschaftsentscheidung vorbereiten oder umsetzen. |

Der Hauptskill übernimmt eine bereits erkennbare Rolle. Er fragt nur nach einer tatsächlich entscheidenden Unklarheit und wechselt nicht ungefragt die Seite. Notarielle Neutralität, technische Begutachtung und anwaltliche Interessenvertretung bleiben unterscheidbar.

## 3. Arbeitslogik

1. [Bauträgerprüfung vom Auftrag bis zum fertigen Dokument](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bautraegerpruefung-steuern/SKILL.md)
2. [Bausoll, Vertragsklauseln und Urkundenänderungen prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/vertragssoll-bearbeiten/SKILL.md)
3. [Raten, Sicherheiten und Eigentumsverschaffung prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/raten-sicherheiten-eigentum-pruefen/SKILL.md)
4. [Bauzeit, Sonderwünsche und Verzugsfolgen bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bauablauf-bearbeiten/SKILL.md)
5. [Abnahme, Mängel, Gemeinschaft und Verjährung prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/abnahme-maengel-weg-pruefen/SKILL.md)
6. [Technische Nachweise und Haftung beteiligter Fachleute prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/architekt-bearbeiten/SKILL.md)
7. [Baugruppen, Sanierung und Nachzügler abgrenzen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/sonderfaelle-baugruppe-sanierung-pruefen/SKILL.md)
8. [Unterlagen, Förderversprechen und Rechtsquellen auswerten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md)
9. [Gutachten, Verhandlungsschreiben und Verfahrensentwürfe fertigstellen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/arbeitsprodukt-bearbeiten/SKILL.md)
10. [Juristischer Argumentationskern - Bauträgervertrag Prüfer](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/juristischer-argumentationskern/SKILL.md)

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **60 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

## 4. Belege und rechtliche Grenzen

Ratenrechnung und tatsächliche Fälligkeit sind unterschiedliche Fragen. Gleiches gilt für Übergabe und Abnahme, Individualanspruch und gemeinschaftliche Ausübung sowie Beschluss und Verjährungshemmung. Ein interner GdWE-Beschluss oder eine bloße einseitige Mängelanzeige wahrt für sich keine Verjährungsfrist.

Die [Rollen- und Quellenregeln](references/rechtsprechung-und-rollen.md) dokumentieren die gezielte amtliche Prüfung dieser Abgrenzung. Sie ersetzen keine vollständige Aktualitätskontrolle sämtlicher Fachmodule. Entscheidungen und Literatur nur nach tatsächlich verfügbarer Quelle mit belegtem Aussagegehalt verwenden. Fehlende technische Nachweise gezielt anfordern; keine durchgeführte Besichtigung, Zahlung oder Einreichung behaupten.

## 5. Vorhandene Einstiege und Fachbestände

Der [bisherige zweite Einstieg](../bautraegervertragspruefer/README.md) führt zum gemeinsamen Plugin. Die bisherigen Vertragsakten und ihre Originaldateien bleiben erreichbar. In der [Fachbibliothek](FACHMODULE.md) stehen beide vollständigen Vertiefungsbestände; ihre Detailanweisungen wurden nicht durch eine bloße Kurzfassung ersetzt.

[Repository-Start](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md)

English: Use the shared plugin for purchaser, developer, owners' association or property-manager assignments. Ten selectable workflows lead to the full specialist material. The three practice cases retain their existing locations and original files; they are separate from the installation package. Historical entry points remain available as guides.

## 6. Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abnahme-maengel-weg-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/abnahme-maengel-weg-pruefen/SKILL.md) | Trennt Übergabe, Abnahme, Mängelrechte und Verjährung; prüft die GdWE-Beschluss- und Vertretungslage und erstellt Mängelschreiben, Beschlussentwurf oder Fristenkalender. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/abnahme-maengel-weg-pruefen/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Führt geprüfte Bauträgerbefunde in Mandantenbrief, Gutachten, konkrete Urkundenänderung, Mängelschreiben, GdWE-Beschluss oder ausdrücklich bestellten Schriftsatz mit vollständiger Begründung über. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`architekt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/architekt-bearbeiten/SKILL.md) | Gleicht Bauzustand und technische Unterlagen mit geschuldeten Planungs-/Überwachungsleistungen ab; formuliert Gutachterfragen und prüft belegte Haftungs- und Regressansätze. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/architekt-bearbeiten/SKILL.md) |
| [`bauablauf-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bauablauf-bearbeiten/SKILL.md) | Ordnet vereinbarte Termine, Baufortschritt, Behinderungen und Sonderwünsche; prüft Kausalität und bezifferte Verzugsfolgen und erstellt das beauftragte Schreiben. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bauablauf-bearbeiten/SKILL.md) |
| [`bautraegerpruefung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bautraegerpruefung-steuern/SKILL.md) | Führt Erwerber-, Bauträger-, GdWE- oder Verwalteraufträge durch Vertrags-, Raten-, Abnahme- und Mängelprüfung bis zum bestellten Schreiben, Gutachten oder Beschlussentwurf; hält Rollen, Belege und offene Freigaben auseinander. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/bautraegerpruefung-steuern/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Bauträgervertrag Prüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`raten-sicherheiten-eigentum-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/raten-sicherheiten-eigentum-pruefen/SKILL.md) | Prüft MaBV-Zahlungsmodell, Bautenstand, Verbrauchersicherheit, Vormerkung und Lastenfreistellung; berechnet Rate und Saldo und formuliert Zahlungsantwort oder Sicherungsforderung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/raten-sicherheiten-eigentum-pruefen/SKILL.md) |
| [`sonderfaelle-baugruppe-sanierung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/sonderfaelle-baugruppe-sanierung-pruefen/SKILL.md) | Prüft Baugruppen-/GbR-Modelle, Bestands- und Sanierungserwerb sowie Nachzügler; ordnet Form, Vertragsregime, Finanzierung und gemeinschaftliche Risiken dem tatsächlichen Modell zu. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/sonderfaelle-baugruppe-sanierung-pruefen/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Erschließt widersprüchliche Bauträgerunterlagen, technische-/Fördernachweise und Rechtsquellen; stellt belastbare Belegketten her und führt fehlende Antworten in die laufende Bearbeitung zurück. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`vertragssoll-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/vertragssoll-bearbeiten/SKILL.md) | Gleicht Bauträgerurkunde, Baubeschreibung, Pläne, Fläche und Sonderwünsche ab; prüft AGB und Beurkundungsbezüge und formuliert konkrete rollenbezogene Klauseländerungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bautraegervertrag-pruefer/skills/vertragssoll-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
