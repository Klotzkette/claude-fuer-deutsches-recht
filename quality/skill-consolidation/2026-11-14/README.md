# 1. Skillordnung und technische Qualitätsprüfung

Die Runde betrifft die Auswahl und Erreichbarkeit der Fachinhalte in allen 315 Plugins. Die 224 zuvor größeren Plugins wurden auf höchstens 20 aktive Skills begrenzt. Alle übrigen Plugins bleiben eigenständig; insbesondere werden die im gemeinsamen Insolvenzrechtsordner aufgeführten Plugins nicht verschmolzen. Insgesamt sind 3.175 Skills auswählbar. 21.883 frühere Skills bleiben als vollständige Fachmodule erhalten.

## 1.1. Erhaltung und Auswahl

- [SourceMap](source-map.json): Originalhashes, aktuelle Pfade, umkehrbare Verweiskorrekturen und Bindung an die explizite Zuordnungsdatei. Die strenge Prüfung kontrolliert Fachtexte, lokale Werkzeuge und Referenzen. Die ursprüngliche Integrationsinventur bleibt ein historischer Snapshot; sie wird nicht nachträglich auf redaktionell überarbeitete READMEs und Prompts umgeschrieben.
- [Aktivierungsbeschreibungen](activation-description-followup.md): 621 neue Routen in 104 Plugins wurden auf konkrete Aufgaben und Rollen präzisiert. Nur die Frontmatter-Beschreibung änderte sich, der jeweilige Body blieb bytegleich. Der Aktivierungsaudit prüft alle 3.175 Skills ohne Befund; vorhandene Fachtexte wurden dafür nicht gekürzt.
- [Paketverweise](package-link-followup.json) und [zusätzlicher BVerfG-Verweis](package-link-additional-scope.json): relative Verweise verlassen das eigenständig installierte Paket nicht mehr unbemerkt. Historische Belege bleiben rekonstruierbar.
- [Historische Quellenlinks](historische-quelllinks.json): betroffene Auditlinks beziehen sich ausdrücklich auf ihren alten Commit. Protokollierte Aussagen, Prüfzeitpunkte und Hashes bleiben erhalten.

Die Regressionen verwerfen unter anderem einen 21. aktiven Skill, verlorene Fachmodule, nicht mehr existierende aktive Ziele, ausbrechende Verweise, falsche Prompt-/Skillhashbindungen und unvollständige Pakete. Gesonderte Rechtsfehlerprüfungen erfassen auch `FACHINHALT.md`; die Umbenennung darf diese Kontrollen nicht umgehen.

## 1.2. Prompts und Werkzeuge

Der [Prompt-Integrationsbericht](prompt-integration-followup.md) dokumentiert 21 erfolgreiche allgemeine Prüfläufe mit 251 gezählten Unittests sowie weiteren direkten Assertions. Die Generatoren lesen weiterhin den vollständigen ursprünglichen Fachbestand. Aktive Auswahlziele und erhaltene Fachtexte werden getrennt behandelt. Der Schwerpunktkatalog bindet die tatsächlich geprüfte Fokusauswahl.

Die [Vergabe-Nachprüfung](vergaberecht-followup.md) erhält die gegenläufigen Rollen von Auftraggeber, Bieter und Konkurrent. Der [Routingnachtrag](vergaberecht-role-routing-followup.json) dokumentiert die getrennte Zuordnung von ursprünglichem Fachmodul und aktivem Arbeitsweg. [KI-Kanzlei und Handbuch](../../ki-native-kanzlei/skill-buendelung-2026-11-14.md) bleiben mit allen dreißig Fachmodulen und vorhandenen lokalen Werkzeugen verbunden.

Der abschließende [Vergabe-Quick-Smoke](vergaberecht-followup/quick-smoke-final.log) besteht alle 16 ausgeführten Prüfgruppen. Im Quick-Modus wurden Git-Status und Testakten-Dateiformate ausgelassen; die zusätzliche GitHub-Release-Gruppe ist manuell vorgesehen. Diese drei Gruppen werden nicht als bestanden gezählt.

Die zentralen Prüfungen der 628 Gesamt-PDF-Akten und ihrer Downloadhinweise bleiben unverändert anwendbar. Diese Runde verändert keine Kontoauszüge, Schriftsätze oder sonstigen Aktenoriginale. Redaktionelle Linkanpassungen an Akten-READMEs und zentrale Megaprompt-Referenzen sind davon zu unterscheiden.

## 1.3. Juristische Prüfung und offene Altbefunde

Der [Quellenbericht](../../source-audits/2026-11-14/README.md) unterscheidet Bestands-/Metadatenkontrolle und tatsächlich gelesene amtliche Urteilspassagen. Die Migration ist keine erneute rechtliche Vollprüfung aller Fachtexte und kein Live-Modelltest. Vier bereits offene Profile mit 31 Dateireviews bleiben als `needs_review` gekennzeichnet.

Ein zusätzlicher [Vorbestandsbefund zu HOAI 1–3](hoai-prompt-limit-baseline.json) bleibt offen: Die drei unveränderten Werkstatt-Prompts überschreiten bereits im Ausgangscommit eine ältere lokale Testgrenze von 32.000 Bytes. Original- und aktuelle Hashes sind identisch. Der betroffene Umfangstest wird nicht als bestanden ausgegeben; die Grenze wurde nicht aufgeweicht. Dies betrifft nicht die neue Höchstzahl aktiver Skills oder die Vollständigkeit der Fachmodule.

Die veraltete Paketversionsausnahme für das frühere Fachanwalts-Insolvenzpaket wird mit der aktuellen exakten Komponentenroute nicht mehr benötigt. Die [vollständige frühere Ausnahmeregistrierung](previous-scoped-release-package-versions.json) und der ursprüngliche Paketnachweis bleiben erhalten. Es wurde kein neuer Hash für einen alten Download erfunden.

## 1.4. Veröffentlichungsnachweis

Die [Releasebeschreibung](../../../docs/releases/qualitaetsrunde-v445.36.0.md) erklärt den begrenzten Umfang von 733 Assets und die Freigabeschranken. Erst der Workflow am festen Main-Commit erzeugt den endgültigen, sauberen Releasebestand. Ein lokaler Probeaufbau im noch nicht committeten Arbeitsverzeichnis ist kein Veröffentlichungsnachweis. Tag, Quellcommit und Prüfsummen stehen im erzeugten Releaseinventar; sämtliche Assets werden vor der Freigabe unabhängig heruntergeladen und erneut geprüft.
