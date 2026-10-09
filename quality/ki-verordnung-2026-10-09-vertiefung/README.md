# 1. KI-Verordnung: Normen, technische Nachweise und Fallprüfung

Stand: 09.10.2026; Komponentenfassung 445.35.1. Die fachliche Runde betrifft sechs KI-Kernkomponenten und 74 weitere Plugins mit einschlägigen Arbeitsabläufen oder fachlichen Hinweisen. Rein historische Prüfberichte und unveränderte fiktive Parteibehauptungen sind nicht als aktuelle Handlungsanweisung umgeschrieben worden. Eine allgemeine Stichwortnennung von Unionsrecht ohne eigenständige KI-Aussage löst keine Änderung des fremden Rechtsgebiets aus.

## 1.1. Quellen und Aussagegrenzen

- [Normargumente](normargumente.md): gelesener amtlicher Wortlaut, Merkmalsketten und Gegenpositionen.
- [Rechtsprechung](rechtsprechung.md) und [strukturierter Abrufvermerk](rechtsprechung.json): acht Entscheidungen mit gelesenen Randnummern, tragender Aussage und Grenze.
- [Technische Normen](technische-normen.md): veröffentlichte Ausgabe, Status, gelesener öffentlicher Kataloginhalt und fachlicher Prüfauftrag. Kein kostenpflichtiger Normvolltext wurde damit als gelesen ausgegeben.
- [Fachbezogene Zuordnung](peripherie.json): konkrete Frage, Arbeitsprodukt, betroffene Dateien, Entscheidungsauswahl und Übungsakte je Randkomponente.

Die Normprüfung knüpft an die [amtlichen Quellenkopien und Abrufnachweise](../ki-verordnung-2026-10-09/quellen/quellen.json) an. Die Auswahl verifizierter Rechtsprechung enthält tragende Entscheidungen bis September 2025; die Prüfung behauptet keine erschöpfende Rechtsprechungsrecherche 2026 und kein unmittelbar Artikel 6 KI-VO entscheidendes Urteil.

## 1.2. Inhaltliche Änderungen

Anbieterinformationen, Anleitung und Werbung werden zur Zweckbestimmung gemeinsam geprüft. Vorhersehbarer Fehlgebrauch begründet konkrete Risiko- und Aufsichtsfragen; er ist kein pauschaler zusätzlicher Hochrisikostatbestand. Datenanforderungen ohne Modelltraining werden auf die einschlägigen Testdaten bezogen, ohne aus fehlendem eigenem Nachtraining eine Ausnahme zu folgern.

Artikel 5 wird anhand seiner verschiedenen Merkmalsketten geprüft. Schädigungsvorsatz, Kontextwechsel oder eine zusätzliche Schadensschwelle werden nicht unterschiedslos ergänzt. Emotionserkennung wird von bloßer Absichts- und Zustandserfassung getrennt. Artikel 50 wird nach tatsächlicher Funktion, Ausgabepfad, Endfassung und Verantwortungsübernahme geprüft.

Die technischen Nachweise verbinden Systemversion, Zweck, Anforderung, Methode, tatsächliches Testergebnis und verbleibende Lücke. Ein Organisationszertifikat ist keine Systembescheinigung. Bei Artikel 40 sind Normausgabe, konkrete Amtsblattreferenz und gedeckter Anforderungsbereich erforderlich; eine Veröffentlichung im Normenkatalog genügt nicht. Der Normungsauftrag erweitert nicht von sich aus die Vermutungswirkung auf Artikel 17.

Die Rechtsprechungsanker liefern konkrete Arbeitsaufträge: tatsächlichen Entscheidungseinfluss belegen, verständliche Erklärung entwerfen, Geheimniseinwand konkret behandeln, Empfängersicht bei Pseudonymisierung untersuchen, Schaden und Kausalität getrennt prüfen. Der ursprüngliche Regelungsgegenstand jedes Urteils bleibt erkennbar.

## 1.3. Testmaterial

Die sechs KI-Kernkomponenten enthalten jeweils fünf konkrete Gegenproben. Diese redaktionell vorbereiteten Fälle sind keine bereits ausgeführten Modelltests. Zusätzlich liegen fünf vollständige native Akten mit zusammen 100 Dokumentdateien vor. Die Referenzen verknüpfen die geeignete Akte mit dem jeweiligen fachlichen Arbeitsauftrag. Der zugrunde liegende fremde Sachverhalt wird nicht unbesehen auf ein anderes Rechtsgebiet übertragen.

Die neuen Akten betreffen Regnitz Sorglosabo, Mainblick Bewerbung, Pegnesus Redaktion, Havelgrund Sozialamt und Eichengrund Logistik. Jede besteht aus sechs DOCX und sechs inhaltlich entsprechenden PDFs, sechs EML, einer mehrblättrigen XLSX und einer Chatdatei. Die Originalbelege und die zusätzlich eingebetteten Mailanhänge werden nicht als unabhängige Beweise doppelt gezählt.

## 1.4. Prüfstand

Die lokale Abschlussprüfung vom 09.10.2026 ist bestanden. `test-ki-verordnung-fachrunde.py --dist` prüfte alle acht Testgruppen ohne Überspringen: Quellenkopien, Versions- und Downloadzuordnung, Skillstruktur, Promptprofile, native Akten, MIME-Anhänge, PDF-Zuordnung, ZIP-Inhalte und Prüfsummen. Der Releasebau erzeugte 340 Dateien für 80 Plugins und 14 Testakten.

Die fünf neuen Akten enthalten 100 Originaldateien, darunter 30 E-Mails mit 46 bytegleichen Anhängen. Ihre Gesamt-PDFs umfassen 192 Seiten. Sämtliche Seiten wurden in Kontaktbögen visuell kontrolliert; die zusätzliche geometrische Prüfung fand keine Textblöcke außerhalb der Seiten. Der [Layoutnachweis](akten-layout.json) hält Dateinamen, Seitenzahlen und Hashes der lokalen Fassung fest. Die neun Handbuch- und Werkstatt-PDFs umfassen zusammen 505 Seiten und wurden entsprechend geprüft; siehe [Handbuchnachweis](handbuch-layout.json). Ein anderer Office-Renderer kann bei unverändertem Inhalt andere Tabellenumbrüche erzeugen.

Die fünf Arbeitsmappen wurden nach dem Export geprüft. Eingabeänderungen, fehlende Werte und Nullwerte sind mit konkreten Rechenproben dokumentiert: [Mainblick](hochrisiko-akte-formelpruefung.json), [Havelgrund und Eichengrund](standards-akten-formeln.json), [Regnitz und Pegnesus](dialog-akten-excelpruefung.md). Die nach der letzten Tabellenkorrektur erneuerten E-Mail-Anhänge stimmen wieder mit ihren Originaldateien überein; siehe [Dialogakten-Anhänge](dialog-akten-anhaenge.json). Die nativen Dateien der neun bisherigen Akten bleiben unverändert.

Zwei unabhängige Anwendungsproben wurden tatsächlich mit den Akten ausgeführt: [Mainblick Bewerbung](mainblick-anwendungsprobe.md) und [Havelgrund Sozialamt](havelgrund-anwendungsprobe.md). Sie benennen Arbeitsprodukte, offene Tatsachen und Entscheidungsgrenzen. Das künftige Vorfall-Planspiel wird nicht als aktueller Sachverhalt ausgegeben. Ein Live-Lauf in Claude Cowork, Codex oder ChatGPT mit angeschlossenen Konten war nicht Gegenstand dieser Prüfung.

## 1.5. Technische Prüfbefehle und verbleibende Grenzen

Folgende Prüfungen waren erfolgreich:

- `test-ki-verordnung-fachrunde.py --dist /tmp/ki351-dist`: acht Testgruppen ohne Skip.
- `test-ki-verordnung-hochrisiko-pruefer.py`: 15 Tests, davon eine erwartete optionale Auslassung.
- `test-office-resilience.py`, `test-scoped-release-routing.py`, `test-compatibility-release.py`, `test-marketplace-import.py`.
- `test-ki-native-kanzlei-source.py`: 30 Skills und die erneuerte Lesefassung; zulässige Promptgrößen und Profilhashes.
- `audit-skill-activation.py`, `validate-yaml-frontmatter.py`, `validate-markdown-structure.py`, `validate-plugin-structure.mjs`, `validate-marketplace-import.mjs`.
- `validate-root-readme-overview.py`, `validate-testakten-readme-downloads.py`: aktuelle Übersichten und Downloadhinweise.
- `validate-manufacturer-plugins.py`: alle 296 Plugins und der Marketplace; `quality-lab.py audit`: alle 296 Prüfprofile.
- `git diff --check`: keine Whitespace-Fehler.

`validate-readme-navigation.py` meldet sieben bereits auf `origin/main` bei Commit `ac65d72bc9a0fac242a661f5c9e3cd2140334552` vorhandene Fehler: einen absoluten lokalen Verweis in der früheren KI-Kanzlei-Probe sowie sechs Markdown-Downloadbeschriftungen im Assetindex und bei Betreuungsrecht beziehungsweise Geldwäschebeauftragtem. Diese Prüfung ist deshalb ausdrücklich nicht als grün ausgewiesen; der neue KI-Downloadumfang erzeugt keinen weiteren Treffer.

Der Veröffentlichungsworkflow wiederholt die fachbezogenen Datei- und Paketprüfungen und vergleicht alle hochgeladenen Dateien durch erneuten Download, bevor er das Release freischaltet. Sein tatsächliches Ergebnis ist im zugehörigen Actions-Lauf nachzusehen. Die Prüfung von Dateien, Formeln und Übertragungsbytes ersetzt weder die Subsumtion im konkreten Mandat noch eine erschöpfende Rechtsprechungsrecherche.

## 1.6. CI-Nachlauf

Die erste GitHub-Prüfung fand eine übersehene sichtbare Versionsangabe in der Startup-README sowie einen Altvergleich der Bauwirtschafts-Manifeste mit der globalen Katalogversion. Die README nennt jetzt die tatsächliche Komponentenfassung. Der Bauwirtschaftstest vergleicht beide Manifeste mit dem jeweiligen Marketplace-Eintrag und prüft zusätzlich die registrierte Komponentenroute; die neun Tests bestehen. Der JavaScript-Marketplace-Validator besteht ebenfalls.

Beim ergänzenden Kompatibilitätspaketbau wurde die Überschneidung des Plugins `vergabestelle-behoerden` sichtbar: Seine kanonische, gleichversionierte Route gehört nun zur KI-Fachrunde. Der Paketbauer berücksichtigt jetzt diese ausdrücklich registrierte, gleichversionierte Route und protokolliert sie im Herkunftsbericht. Fehlende oder unpassende Routen werden weiter abgelehnt. Die neue Regression scheiterte zuerst; nach der Korrektur bestehen alle zwölf Kompatibilitätstests und der tatsächliche Paketbau. Fachtexte und Testakten werden dadurch nicht geändert.

Die ergänzenden Prüfungen zu Laufzeitprofilen, Bauvergabe, Immobilien-Rechtsabteilung, Vergaberecht-Import, App-Grenzen und portablen Starts bestehen. Die Grundstücksrecherche-Suite besteht mit 110 Tests und einer erwarteten Auslassung; zuvor fehlende lokale Bibliotheken wurden nur in der Prüfungsumgebung ergänzt.

Im eingebetteten Vergaberechtsbereich wurden Downloadroute, Referenzverzeichnis und die eine ergänzte Megaprompt-Zeile synchronisiert. Die gemeinsame Havelgrund-Akte ist als ausdrücklich zugelassene, lokal vorhandene externe Testakten-README registriert. Beliebige fremde Komponentenpfade bleiben unzulässig. Die 13 Integrationstests bestehen einschließlich Gegenproben für fehlende oder nicht deklarierte Ziele.

## 1.7. Redaktioneller Nachlauf vor Veröffentlichung

Die in dieser Runde neu ergänzten README-Überschriften wurden dezimal nummeriert; bisherige Sprungziele bleiben durch explizite Anker erreichbar. Die fünf neuen Akten-READMEs erhalten eine fortlaufende Untergliederung. Drei Referenz- beziehungsweise Berichtstitel und der neue Abschnitt der gemeinsamen Rechtsstandsreferenz sind entsprechend eingeordnet. Nur Nummerierungspräfixe und Navigationsanker wurden geändert; die fachlichen Aussagen, Zitate, Entscheidungsdaten und nativen Akten bleiben unverändert. Die versionsgegliederte Chronik bleibt als Changelog erhalten.
