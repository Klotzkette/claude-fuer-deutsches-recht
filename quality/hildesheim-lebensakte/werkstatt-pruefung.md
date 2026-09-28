# 1. Prüfbericht zur Bauwirtschaft-Werkstatt

Autor: Klotzkette. Prüfstand: 28.09.2026. Prüfer: Codex-Agent lebensakte_workflow.

## 1.1. Ergebnis und Umfang

Die neu aufgebaute Werkstatt enthält 100 fortlaufend verbundene Arbeitsstationen in 15 kanonischen Modulen. Native Word- und PDF-Fassung umfassen genau 100 Seiten. Der extrahierte PDF-Text einschließlich Überschriften, Kopf- und Fußzeilen enthält 35.435 Wörter; jede Seite enthält 319 bis 431 Wörter. Es gibt keine zusätzlich angelegten Skills: 29 bestehende Skilldateien behalten ihre Namen und Beschreibungen und verweisen gezielt auf passende Fachmodule.

Die 100 Stationen sind kein verpflichtendes Interview. Der Einstieg verwendet vorhandene Unterlagen, stellt nur entscheidungsrelevante Rückfragen und liefert den bereits möglichen Entwurf. Eingangsstand, neue Entscheidung, gespeichertes Ergebnis und Rückkehrpunkt sind an jeder Station beschrieben. Stationen 7 bis 60 führen durch LPH 1 bis 9. Die LV-, Vertrags-, Rechnungs- und Mängelvertiefungen kehren in den jeweiligen Hauptauftrag zurück. Der abgeschlossene Hauptweg geht von Station 60 nach Station 100; ein neuer Beleg setzt gezielt über Station 99 fort. Es wird kein automatischer Neustart aller Phasen verlangt.

## 1.2. Inhaltlich geprüfte Abgrenzungen

Vermietung bleibt Hauptfall. Stationen 73 bis 78 behandeln ausschließlich die unbeschlossene Verkaufsalternative zum 01.11.2027. Die alternative Kalkulation, Erwerberentwürfe und Raten erzeugen keine realen Käufer, Zahlungen, Grundbucheinträge oder Umsätze im Hauptfall. Verkäuferorientierte Gestaltung wird mit klaren Leistungsgrenzen, wirksamer Risikoverteilung und individuellen Abnahmewegen verbunden; die Unparteilichkeit des Notariats bleibt gewahrt.

Bautagebuch, Begehung und Mängelverfolgung unterscheiden Beobachtung, Unternehmermeldung, fehlende Information, Nachtrag und tatsächlich erledigte Kontrolle. Arbeitstage und arbeitsfreie Tage werden unterschieden. Eine digitale Bearbeitung erfindet weder Ortsbesichtigung noch Bildnachweis. Kumulierte Aufmaße, Rechnungen, tatsächliche Zahlungen und Buchung werden getrennt fortgeschrieben. Das Werk enthält echte Rechenbeispiele und vollständige Musterformulierungen; fehlende Tatsachen werden nicht durch Scheingenauigkeit ersetzt.

Rechtsprechung wird auf konkrete Tatsachen und Anspruchswege bezogen. Neun allgemeine Bauentscheidungsanker und elf ergänzende Bauträgeranker besitzen amtliche Originalverweise, geprüfte Passagen und Übertragungsgrenzen. Die gezielte Quellenlektüre ist keine behauptete Vollprüfung des gesamten Landesbau-, Steuer- oder Vergaberechts. Unbekanntes zukünftiges Recht im bis 2033 laufenden Übungsfall wird nicht erfunden. Die älteren Abrufprobleme im allgemeinen Quellenindex sind durch einen datierten Hinweis auf inzwischen gelesene PDF-Originale eingeordnet.

## 1.3. Native und visuelle Prüfung

Das Dokument wurde mit dem gebündelten headless LibreOffice über render_docx.py gerendert. Sämtliche 100 einzelnen vollständigen Seitenbilder der endgültigen Fassung wurden in aufsteigender Reihenfolge geöffnet und visuell geprüft, nicht lediglich eine Kontaktübersicht. Ergebnis: keine abgeschnittenen Texte, Überlappungen, fehlerhaften Glyphen, unvollständigen Stationen, Ausweich- oder Leerseiten. Jede Station beginnt auf der gleich nummerierten Seite. Überschriften und Fußzeilen sind konsistent. Schrift: Times New Roman 11 Punkt im Fließtext; A4.

PDF: `bauwirtschaft/materialien/bauwirtschaft-werkstatt-100-seiten.pdf`.

Word: `bauwirtschaft/materialien/bauwirtschaft-werkstatt-100-seiten.docx`.

Lokaler Renderordner: `/tmp/hildesheim-workflow-qa-final/`; Bilder `page-1.png` bis `page-100.png`.

Die maschinelle Vollständigkeitsprüfung bestätigte alle 1.192 Textblöcke einschließlich Zwischenüberschriften aus den kanonischen Modulen im DOCX sowie jeweils auf der richtigen PDF-Seite. Alle 16 nativen externen Dokumentlinks stimmen in Word und PDF überein. Sämtliche 29 Skilldateien bestanden quick_validate; relative Ressourcenlinks existieren und jede Skilldatei bleibt unter 500 Zeilen. Der Einzelnachweis mit Dateigrößen, Quellenlinks und SHA-256 jedes gerenderten PNG steht in [werkstatt-pruefung.json](werkstatt-pruefung.json).

## 1.4. Verbindliche Artefakthashes

Quellverbund-SHA-256 (sortierte Moduldateinamen, NUL-Trenner, Originalbytes): `5a543b2de0d0effed238b2b2217136358695c9e4772d3b386e39952453b0e0e6`.

- `bauwirtschaft/bauwirtschaft-werkstatt.md`: `404744e75bd9bc0884ec6070b9fd482983dfaaf0be0b7cdae5d6c5b8a49ef253`.
- `bauwirtschaft/materialien/bauwirtschaft-werkstatt-100-seiten.docx`: `5995fe6841cdf9264d47d45a849a581f62c3b1929d8e80926b114de5285fd30e`.
- `bauwirtschaft/materialien/bauwirtschaft-werkstatt-100-seiten.pdf`: `ecfe194b000d2ca4a4ef41dcc90f96fdc011789842060a9d02c355896bfc7cbe`.

## 1.5. Reproduktion und Prüfgrenze

Die kanonischen Texte liegen unter `bauwirtschaft/references/werkstatt/`. `scripts/build-bauwirtschaft-werkstatt-handbuch.py` erzeugt daraus die eigenständige Markdown-Fassung und das native Word-Dokument. Mit `--render --renderer <render_docx.py> --qa-dir <Prüfordner>` werden PDF und Seitenbilder erzeugt; der Builder stoppt bei abweichender Seitenzahl oder falscher Stationszuordnung. `--markdown-only` benötigt keinen Dokumentrenderer.

Dieser Bericht dokumentiert die redaktionelle, native und visuelle Prüfung der hier gehashten Fassung. Er behauptet keinen unabhängigen Live-Verhaltenstest; ein solcher wird separat mit frischem Kontext protokolliert. Eine nachträgliche Änderung einer kanonischen Moduldatei erfordert erneut passenden Build, Inhaltsabgleich und Sichtprüfung der betroffenen Seiten.

## 1.6. Gezielte RDG-Regressionskorrektur

Station 3 ergänzt ausdrücklich, dass ein als Erfüllungsgehilfe eingesetzter Rechtsanwalt oder bloßes anwaltliches Gegenlesen die eigene unerlaubte Rechtsberatungsverpflichtung des Architekten nicht heilt. Das unmittelbare anwaltliche Bauherrnmandat wird davon abgegrenzt. Die bestehende Regression `test_contract_work_checks_legal_authority_without_stopping_technical_work` besteht unverändert.

Nach Synchronisierung der kanonischen Quelle, Markdown-, Word- und PDF-Fassung wurde Seite 3 erneut vollständig visuell geprüft. Der SHA-256-Vergleich sämtlicher 100 Seitenbilder bestätigt: ausschließlich Seite 3 änderte sich; die übrigen 99 bereits vollständig gesichteten Seitenbilder sind bytegleich. Die erneute Textprüfung bestätigt 1.192 Textblöcke, 100 korrekt zugeordnete Seiten und 16 unveränderte native Quellenlinks. Die oben angegebenen Artefakthashes und das JSON-Manifest bezeichnen diese korrigierte Endfassung.
