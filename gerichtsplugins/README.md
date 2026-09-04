# Gerichtsplugins

[Hauptverzeichnis](../README.md) · [Skills](../SKILLS.md) · [Prompts](../docs/werkstatt-und-schnellstart-coverage.md) · [Downloads](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) · [Testakten](../testakten/README.md)

## 1 Überblick

Diese experimentelle Sammlung bündelt Plugins für gerichtliche Rollen, Staatsanwaltschaft und Amtsanwaltschaft sowie die Relationstechnik im Zivilrecht. Im Mittelpunkt stehen Aktenaufbereitung, Entscheidungsentwürfe und die Strukturierung von Arbeitsabläufen. Die Sammlung ist keine Produktivempfehlung.

## 2 Plugins von A bis Z

Die Tabelle folgt alphabetisch den bestehenden Marketplace-Quellpfaden unter `gerichtsplugins/`. Die verlinkten Plugin-READMEs führen zu den jeweiligen Skills, eigenständigen Prompts und Testmaterialien.

| Plugin | Rolle und Schwerpunkt |
| --- | --- |
| [`relationstechnik-zivilrecht`](./relationstechnik-zivilrecht/README.md) | Relationstechnik für richterliche, anwaltliche und ausbildungsbezogene Arbeit im Zivilrecht. |
| [`richter-amtsgericht-handelsregister`](./richter-amtsgericht-handelsregister/README.md) | Registerrichter und Rechtspfleger: Arbeit mit Registerakten. |
| [`richter-amtsgericht-insolvenz-restrukturierung`](./richter-amtsgericht-insolvenz-restrukturierung/README.md) | Gerichtliche Perspektive auf Insolvenz und Restrukturierung. |
| [`richter-amtsgericht-straf`](./richter-amtsgericht-straf/README.md) | Strafrichter und Schöffengericht am Amtsgericht. |
| [`richter-amtsgericht-zivil`](./richter-amtsgericht-zivil/README.md) | Richterliche Bearbeitung von Zivilsachen am Amtsgericht. |
| [`richter-arbeitsgericht`](./richter-arbeitsgericht/README.md) | Vorsitz und Kammerarbeit am Arbeitsgericht. |
| [`richter-bverfg-verfassungsbeschwerden`](./richter-bverfg-verfassungsbeschwerden/README.md) | Wissenschaftliche Mitarbeit und Berichterstattung zu Verfassungsbeschwerden. |
| [`richter-familiengericht`](./richter-familiengericht/README.md) | Richterliche Bearbeitung von Familiensachen. |
| [`richter-finanzgericht`](./richter-finanzgericht/README.md) | Einzelrichterliche Arbeit und Senatsarbeit am Finanzgericht. |
| [`richter-landgericht-strafkammer`](./richter-landgericht-strafkammer/README.md) | Vorsitz und Berichterstattung in Strafkammern des Landgerichts. |
| [`richter-landgericht-zivilkammer`](./richter-landgericht-zivilkammer/README.md) | Vorsitz und Berichterstattung in Zivilkammern des Landgerichts. |
| [`richter-sozialgericht`](./richter-sozialgericht/README.md) | Richterliche Arbeit und Kammerarbeit am Sozialgericht. |
| [`richter-verwaltungsgericht`](./richter-verwaltungsgericht/README.md) | Einzelrichterliche Arbeit und Kammerarbeit am Verwaltungsgericht. |
| [`staatsanwaltschaft-amtsanwaltschaft`](./staatsanwaltschaft-amtsanwaltschaft/README.md) | Staatsanwälte und Amtsanwälte: Ermittlungsarbeit und Verfahrensbearbeitung. |
| [`staatsanwaltschaft-praxis-einstieg`](./staatsanwaltschaft-praxis-einstieg/README.md) | Praxiseinstieg: Aktenführung, Verfügungen und tägliche Arbeitsabläufe. |

## 3 Quelldateien und Installationspakete

Das Quellverzeichnis eines Plugins enthält dessen Manifest, README, Skills und weitere Arbeitsdateien. Maßgeblich für den Skill-Bestand sind die vorhandenen Dateien unter `skills/<skill-name>/SKILL.md`; die aktuelle Übersicht steht im [Skill-Verzeichnis](../SKILLS.md). Es gibt keine zusätzlichen Schnellstart-Wrapper-Skills.

Ein installierbares Plugin-ZIP wird aus dem jeweiligen Marketplace-Quellpfad gebaut. Quellordner und ZIP haben nicht denselben Inhalt: Die eigenständigen Dateien `*-werkstatt.md` und `*-schnellstart.md` (Schnellstart- oder Mini-Prompts) sind keine Skills und bleiben ausdrücklich außerhalb des Plugin-ZIPs. Sie sind über die [Prompt-Übersicht](../docs/werkstatt-und-schnellstart-coverage.md) einzeln als Markdown verfügbar und können ohne Plugin-Installation verwendet werden.

Für die Installation dient das einzelne Plugin-ZIP aus den [Downloads](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest); die [Installationshilfe](../INSTALLATION_EINFACH.md) erläutert den Einstieg. Die separat angebotenen Fallpakete stehen in der [Testakten-Übersicht](../testakten/README.md).

## 4 Nutzungshinweise

Die übergreifenden Hinweise zu experimenteller Nutzung, Verantwortung, Datenschutz und regulatorischer Einordnung stehen zentral in der [Haupt-README](../README.md). Diese Übersicht dient der Navigation und enthält keine eigene rechtliche Einordnung.

## 5 English Help

Choose a role or topic in the alphabetical table, then open its README for skills and materials. Install an individual plugin ZIP from [downloads](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest), or use a standalone Markdown file from the [prompt index](../docs/werkstatt-und-schnellstart-coverage.md). Workshop and quick-start/mini prompts are not skills and are excluded from plugin ZIPs. See the [main README](../README.md) for usage context and the [case index](../testakten/README.md) for practice files.

## 6 Lizenz

Dual-lizenziert MIT und Apache-2.0.
