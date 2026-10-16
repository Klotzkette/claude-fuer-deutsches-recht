# 1. Phishing: Erstattung und späterer Rückgriff

Dieses Prüfprotokoll dokumentiert die Einordnung von EuGH, Urteil vom 15.10.2026, C-70/25, Tukowiecka, in die Arbeitsabläufe des Phishing-Vorfall-Prüfers und sechs fachlich passende Nachbarplugins. Geprüft am 16. Oktober 2026. Komponentenfassung 445.35.4.

## 2. Quellen und fachliche Grenzen

Der amtliche deutsche Urteilstext wurde in InfoCuria vollständig geöffnet und gelesen. Die [Quellenprüfung](eugh-c-70-25-quellen.md) benennt Randnummern, Normtexte und konkrete Folgerungen. Die Pressemitteilung ist ergänzende Orientierung; sie ersetzt keinen Entscheidungsgrund. Erstattung und spätere Verlusttragung bleiben getrennt. Ein begründeter Betrugsverdacht gegen den Zahler samt erforderlicher schriftlicher Behördenmitteilung ist etwas anderes als ein Vorwurf grober Fahrlässigkeit oder der Betrug eines Dritten.

Das Urteil belegt keine endgültige Haftungsfreiheit, kein allgemeines Aufrechnungsverbot und keine automatische Nichtautorisierung einer vom Zahler selbst veranlassten Überweisung. Historische BGH-Anker und andere Rechtsgebiete wurden durch diese Ergänzung nicht pauschal erneut vollständig verifiziert.

## 3. Konkrete Umsetzung

Im Phishing-Plugin verbinden Fachskills, Hauptworkflow, Werkstatt, Mini-Prompt und Vorlagen die Autorisierungsprüfung mit dem zeitlich vorrangigen Erstattungsverlangen. Der mögliche Bankgegenanspruch wird gesondert geprüft. Die Offline-Hilfe erteilt keine automatischen Prozessfreigaben und berechnet aus Fahrlässigkeitshinweisen keine Haftungsquote. Fehlende Beträge bleiben unbekannt. Ein Minutenabstand ist keine feste gesetzliche Unverzüglichkeitsgrenze.

| Angebot | Konkrete Verwendung |
| --- | --- |
| Phishing-Vorfall-Prüfer | Meldung, Beweise, Bankaufforderung, Schlichtung und Klage mit getrennter Rückgriffsbewertung. |
| Bank-Rechtsabteilung | Erstattung zeitnah bearbeiten; SCA, Beweislast und einen möglichen späteren Ersatzanspruch getrennt dokumentieren. |
| Fachanwalt Bank- und Kapitalmarktrecht | Kunden- und Bankseite, Arbeitsprodukt, Authentifizierung und Autorisierung auseinanderhalten. |
| BGB-BT-Prüfer | Zahlungsdiensterechtliche Anspruchsfolge und deutsche Umsetzung der Richtlinie konkretisieren. |
| AGB-Werkstatt | Klauseln prüfen, die Erstattung von einer abgeschlossenen Fahrlässigkeitsprüfung abhängig machen. |
| Betreuungsrecht | Verdächtige Kontobelastung prüfen, Rückforderungsschreiben erstellen und nicht vorschnell mit späteren Gegenforderungen verrechnen. |
| Commercial Courts | Zahlungsdiensterechtlichen Spezialabschnitt berichtigen; keine Aussage zur Zuständigkeit eines Commercial Court aus C-70/25 ableiten. |

## 4. Deutsche Testakte

Die [Akte Rabenstein](../../testakten/phishing-kleinanzeigen-rabenstein-halle/README.md) übersetzt den tatsächlichen Kern des Ausgangsverfahrens nach Halle (Saale). Sie enthält 28 Originale: sechs Word-Dateien, zehn PDFs, zehn E-Mails und zwei Excel-Arbeitsmappen. Der SMS-Code gehört zum Sachverhalt; sein nicht belegter Inhalt bleibt offen. Kaufpreis, streitiger Betrag und eine andere Kontogutschrift sind unterscheidbar. Bankanschreiben und Klageentwurf sind nicht versandt.

Der [Datei- und Layoutnachweis](testakte-pruefung.json) enthält Quellenhashes, Anhangsabgleich, Tabellenprüfungen und Sichtkontrollen. Originale, Einzel-PDFs und Gesamt-PDF werden aus denselben Unterlagen gebaut. Die Akte Mayer bleibt erhalten; ihre frühere Helferausgabe ist als historisch eingeordnet und bei Verwendung neu zu berechnen.

## 5. Prüfung und Veröffentlichung

Die [unabhängige Schlussprüfung](schlusspruefung.md) kontrolliert Helfer, Quellenidentität, Anhänge und Paketaufbau; der [Prompt-PDF-Nachweis](prompt-pdf-pruefung.json) dokumentiert alle zehn angesehenen Seiten. Die Prüfung umfasst die spezifischen Regressionen, Paket- und Quellenabgleich, Promptgrenzen, Marketplace, Navigation und Qualitätsprofile. Die ausgeführten Befehle und Ergebnisse stehen im [Prüflaufprotokoll](prueflaeufe.json). Ein grüner Strukturtest ist kein Nachweis einer vollständigen Rechtsprüfung und kein Live-Test in Claude, Codex oder ChatGPT. Die hinzugefügten Evaluationsfälle sind Sollkriterien; sie wurden nicht als neue Modellläufe ausgegeben.

Die installierbaren Pakete und portablen Kopien enthalten dieselben geprüften Quelldateien. Die separaten Markdown-Prompts sind eigenständige Downloads. Werkstatt und Mini des Phishing-Plugins werden zusätzlich als PDF mit Times New Roman 11 pt erzeugt, ersatzweise mit ausgewiesener Liberation Serif. Das Komponentenrelease ersetzt keine älteren Tags oder allgemeinen Sammelarchive.

[Plugin](../../phishing-vorfall-pruefer/README.md) · [Testakten](../../testakten/README.md) · [Download-Index](../../ASSET_INDEX.md)
