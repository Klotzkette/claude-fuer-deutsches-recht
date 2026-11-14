# 1. Arbeitswege und Fachmodule

Die 315 Plugins bleiben eigenständige Werkzeuge für ihre jeweiligen Aufgaben. Jedes Plugin bietet höchstens 20 auswählbare Skills. Ein Skill führt durch einen zusammenhängenden Arbeitsweg und zieht dafür die passenden ausführlichen Fachmodule, Vorlagen und Hilfsprogramme heran.

Wer beispielsweise eine Insolvenzforderung prüft, wählt den Arbeitsweg für Forderungen und Sicherheiten. Dieser liest abhängig vom Fall die vollständigen Anweisungen zu Anmeldung, Abtretung, Bestreiten oder Sicherheiten und führt die Prüfung im selben Vorgang fort. Die Auswahl eines Arbeitswegs ersetzt weder die Lektüre der einschlägigen Fachmodule noch die aktuelle Quellenprüfung.

## 1.1. Fachliche Vertiefung finden

Die Plugin-README zeigt die auswählbaren Skills. Bei gebündelten Plugins erschließt zusätzlich `FACHMODULE.md` sämtliche bisherigen Fachtexte, gegliedert nach ihrem Arbeitsweg. Deren Dateien heißen `FACHINHALT.md` und bleiben mit lokalen Vorlagen, Rechnern und Referenzen verbunden. Sie erscheinen nicht zusätzlich als auswählbare Skills.

Die großen Werkstatt-Prompts und die Mini-Prompts bleiben eigenständige Arbeitsanweisungen. Für einen konkreten Auftrag genügt ein passender Einstieg. Es ist nicht erforderlich, sämtliche Vertiefungen gleichzeitig zu laden. Vorhandene Visualisierungs- und Dokumentworkflows bleiben erhalten; eine interaktive Ansicht setzt tatsächlich verfügbare Werkzeuge voraus.

Der [Insolvenzrechtsordner](../insolvenzrecht-plugins/README.md) bietet eine gemeinsame Navigation zu den eigenständigen Plugins. Forderungsanmelder, Insolvenzreifeprüfer, Planwerkstatt und die weiteren Insolvenzplugins werden dadurch nicht zusammengelegt.

## 1.2. Umfang der Ordnung vom 14. November 2026

| Bestandteil | Ergebnis |
| --- | ---: |
| Eigenständige Plugins | 315 |
| Überarbeitete Plugins mit zuvor mehr als 20 Skills | 224 |
| Auswählbare Skills im gesamten Repository | 3.175 statt 23.433 |
| Höchste aktive Skillzahl eines Plugins | 20 |
| Als vollständige Fachmodule erhaltene bisherige Skills | 21.883 |
| Plugins im Komponentenrelease einschließlich weiterer Quellenkorrekturen | 226 |

Die Konsolidierung ist keine Streichung der Fachtexte. Eine explizite [Zuordnungsdatei](../scripts/data/skill-cap-registry.json) weist jedem bisherigen Fachmodul seinen aktiven Arbeitsweg zu. Der [Quellnachweis](../quality/skill-consolidation/2026-11-14/source-map.json) hält ursprüngliche Hashes und reversible Verweiskorrekturen fest. Die Originaltexte lassen sich daraus bytegenau rekonstruieren. Fachliche Korrekturen erfolgten vor dieser Überführung und sind in den Quellenberichten gesondert dokumentiert.

## 1.3. Rechtsprechung und Grenzen der Prüfung

Die [Quellenprüfung vom 14. November 2026](../quality/source-audits/2026-11-14/README.md) trennt die Bestands- und Metadatenkontrolle aller 315 Pluginprofile von elf gezielt an amtlichen Volltextpassagen geprüften Entscheidungen. Sie dokumentiert unter anderem Berichtigungen im Insolvenz-, Datenschutz- und Steuerstrafrecht sowie aktuelle Anker aus Arbeits-, Verfassungs-, Europa- und Produktrecht. Pressemitteilungen und Leitsätze werden nicht als gelesene Urteilsgründe ausgegeben.

Die vier damals offenen Profile mit 31 Dateireviews wurden in der [gesonderten Nachprüfung vom 14./15. November 2026](../quality/source-audits/2026-11-14-nachpruefung/README.md) vollständig bearbeitet. Ihre Abschlussbelege binden jede zuvor offene Datei an den individuell geprüften Endstand und Fachbericht; historische Prüfprofile bleiben erhalten. Quellenzugriffsgrenzen sind weiterhin dokumentiert. Die strukturellen Prüfungen, Paketkontrollen und ergänzten Regressionen bestätigen keine erfolgreiche Ausführung sämtlicher Plugins in einem Live-Modell und keine vollständige juristische Prüfung aller übernommenen Fachtexte.

## 1.4. Pakete und Nachweise

Die vier nachgeprüften Plugins und ihre eigenständigen Prompts sind in [Qualitätsrunde 445.36.1](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/qualitaetsrunde-v445.36.1) veröffentlicht: vier ZIPs, fünfzehn Promptdateien, Inventar und Prüfsummen. Alle übrigen Pakete bleiben über ihre jeweiligen Versionen erreichbar.

Die betroffenen Pakete sind über [Qualitätsrunde 445.36.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/qualitaetsrunde-v445.36.0) und den [Download-Index](../ASSET_INDEX.md) erreichbar. Das Komponentenrelease umfasst 234 Plugin-ZIPs, 495 separate Promptdateien, zwei KI-Kanzlei-Handbuchdateien sowie Inventar und SHA-256-Prüfsummen: zusammen 733 Dateien. Der KI-Kanzlei-Gesamtband enthält weiterhin alle 30 Fachmodule auf 323 Seiten; seine acht auswählbaren Arbeitswege sind davon getrennt.

Der Veröffentlichungsworkflow baut nur einen festgelegten Main-Commit. Er prüft ZIP-Inhalte gegen die Quelldateien, vollständige Fachmodulerreichbarkeit, Versionen, Links und Prüfsummen. Vor der Freigabe des Releaseentwurfs werden alle Assets erneut heruntergeladen und geprüft. Vorhandene veröffentlichte Versionen bleiben unverändert. Testakten werden in dieser Runde nicht neu gebaut oder ersetzt; ihre bisherigen Downloads bleiben bestehen.
