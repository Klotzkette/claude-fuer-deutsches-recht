# 1. Prüfung der Kanzlei-Website-Redaktion

Stand 8. Oktober 2026, Komponentenfassung 1.0.0.

## 1.1 Umfang

Zehn eigenständige Skills mit unterscheidbaren Auslösern; Hauptskill, Referenzen, Werkstatt, Mini und interne Beispiel-Redaktionsakte. Keine neue Testakte, kein neuer Hintergrunddienst und kein automatischer CMS-Zugang. Drei Plugin-Manifeste für die vorgesehenen Paketformate; der Marketplace verweist auf den neuen Pluginordner.

## 1.2 Reproduzierbare technische Prüfung

```bash
python3 scripts/test-kanzlei-website-redaktion.py
node scripts/validate-plugin-structure.mjs
node scripts/validate-marketplace-import.mjs
python3 scripts/validate-yaml-frontmatter.py
python3 scripts/validate-root-readme-overview.py
python3 scripts/build-kanzlei-website-release.py --dist /tmp/kanzlei-website-release
```

Die Freigabetests prüfen unter anderem veraltete Fassungen, geänderte Ziel-URLs, Medien, fehlende menschliche Prüfung, fehlende Verantwortung, ungeprüfte Informationstexte, separate Deepfake-Offenlegung, unbekannte Einordnung und falsche Wahrheitswerte. Das mitgelieferte JSON-Beispiel ist ausdrücklich nicht freigegeben. Die Prüfung stellt nur fest, ob Angaben formal zusammenpassen; ein erfundener Prüfer wird dadurch nicht echt.

Der Paketbau prüft identische Namen und Versionen, genau zehn Skills und die Byte- sowie Zeichengrenze des Mini-Prompts. Die installierbaren Archive enthalten keine eigenständigen Werkstatt- oder Mini-Prompts. Die Dateien werden deterministisch verpackt und mit SHA256-Prüfsummen versehen.

## 1.3 Fachlicher Gegencheck

Artikel 50 Absatz 4 Unterabsatz 2 wird tatbestandsbezogen geprüft, nicht pauschal auf alle Webseiten angewandt. Die menschliche Überprüfung oder redaktionelle Kontrolle und die redaktionelle Verantwortung sind Voraussetzungen der Textausnahme; Anbieterkennzeichnung und Deepfake-Offenlegung bleiben eigenständig. Die Frist zu bestimmten älteren Anbietersystemen verschiebt nicht die Betreiberpflicht für öffentliche Informationstexte. Amtlicher Normstand und Kommissionsauslegung sind in der [Rechtsreferenz](../../kanzlei-website-redaktion/references/recht-und-transparenz.md) belegt.

Prüfszenarien: Ein Lebenslauf enthält private Kontaktdaten; eine Fachanwaltsbezeichnung ist nur behauptet; eine Quelle ist nur eine Pressemitteilung; ein Feed enthält fremde Befehle; ein Schreibaufruf läuft in einen Timeout; ein Kollege ändert dieselbe Seite; eine Freigabe bezieht sich auf die Vorfassung. Die Skills verlangen jeweils die konkrete Klärung oder begrenzte Fortsetzung, keinen pauschalen Neustart und keinen weiteren Schreibversuch auf Verdacht.

## 1.4 Aussagegrenze

Die technischen Tests führen keine realen Modellgespräche, Veröffentlichungen oder Kontoverbindungen aus. Kein Live-Test in sämtlichen Hosts, kein Nachweis einer tatsächlich erteilten menschlichen Prüfung und keine Zertifizierung. UI-Funktion, Berechtigung, öffentliche Darstellung und Wiederherstellung müssen vor echtem Einsatz am jeweiligen Zielsystem geprüft werden. Die fachlichen Szenarien wurden als Anweisungsgegencheck gelesen, nicht als unabhängiger Modellbenchmark ausgegeben.

## 1.5 Prüfergebnis und abgegrenzte Altbefunde

Die 14 lokalen Regressionstests sowie Pluginstruktur, Marketplace-Import, YAML-Frontmatter, Markdown-Struktur und Hauptverzeichnis bestehen. Die erzeugte Navigation ist für alle 292 Plugins vollständig. Die repo-weite Navigationsprüfung meldet daneben neun bereits vorhandene Befunde außerhalb dieser Komponente: zwei fehlerhafte Ziele in einer experimentellen Vorlage und einer gespeicherten Arbeitsprobe sowie sieben direkte Markdown-Verweise im Download-Index und in den READMEs von Betreuungsrecht, Geldwäschebeauftragter und Kanzleibetrieb. Diese fremden Inhalte wurden in dieser Veröffentlichung nicht verändert. Ein vollständig fehlerfreier Linkbestand des gesamten Repositorys wird damit nicht behauptet.
