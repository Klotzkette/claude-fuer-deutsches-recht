# 1. Qualitätsprüfung

Prüfstand: 22.09.2026. Dieser Nachweis betrifft das Plugin und sein eigenes Prüfprofil. Die zentrale Release-Erstellung und die Verhaltenstests sind davon getrennte Schritte.

## 1.1. Ausgeführte Prüfungen

- Es liegen genau zehn Skills vor. Jeder Skill hat sechs nummerierte Hauptabschnitte und gültige Metadaten. Namen und Beschreibungen sind ASCII; die deutschen Textkörper verwenden Umlaute und ß.
- Der Hauptskill `belege-bis-zur-abrechnung` umfasst 7.377 Zeichen einschließlich Metadaten. Er enthält die Beleg- und Rechenkette bis zur Abrechnung oder zum beauftragten Antwortbrief.
- Der Schnellstart umfasst 7.403 UTF-8-Bytes und bleibt unter 7.500 Bytes. Er enthält die konkreten Aussagen zu VIII ZR 156/11 und VIII ZR 249/15. Die Formulierung zur verweigerten berechtigt verlangten Belegeinsicht ist korrigiert.
- Die Werkstatt umfasst 21.906 UTF-8-Bytes. Beide Prompts liegen außerhalb des Skillverzeichnisses.
- Das [Prüfprofil](../quality/evals/betriebskosten-hausverwaltung.json) besteht die Strukturprüfung mit `validate_profile`. Es enthält zehn Fälle und die aus den endgültigen Promptdateien berechneten SHA-256-Werte. Beide Hashes wurden anschließend gegen die Dateien geprüft.
- Die Manifestbeschreibungen sind ASCII und höchstens 300 Zeichen lang. Die Autorenangabe lautet Klotzkette. Die Skillbeschreibungen liegen zwischen 80 und 1.024 Zeichen; Skillnamen sind höchstens 64 Zeichen lang.

## 1.2. Fachliche Quellenprüfung

Das [Quellenregister](references/betriebskosten-quellen.md) dokumentiert die live amtlich geprüften Normen, sechs gelesene BGH-Volltexte und deren Aussagegrenzen. Es umfasst insbesondere BGB 556, 556a und 560, BetrKV 1 und 2, HeizkostenV, CO2KostAufG, Berliner Grundsteuer, EnWG 42a und EStG 35a. Es werden keine Urteile aus 2026 behauptet.

Für Abrechnungen 2025 ist der damalige Rechtsstand maßgeblich. Die elektronische Bereitstellung nach BGB 556 Absatz 4 wird gegenüber älteren Originalbelegentscheidungen abgegrenzt. Öl wird nach bewertetem Bestandsverbrauch abgerechnet; CO2-Kosten bleiben den verbrauchten Lieferbeständen und ihren jeweiligen Lieferjahren zugeordnet. Die spätere Änderung des CO2KostAufG wird nicht auf 2025 übertragen. Warmwasser-Brennstoffmengen aus Q/Hi werden von dimensionslosen Anteilen relativer Wärmemessung unterschieden.

## 1.3. Gesicherte Prompt-Hashes

| Datei | SHA-256 |
| --- | --- |
| `betriebskosten-hausverwaltung-schnellstart.md` | `edbf2ae759a793a4ee79afa1e0271355ba140fb2d93fec09e4df786fa34d87e6` |
| `betriebskosten-hausverwaltung-werkstatt.md` | `43d4c2d41b5e7a858ae5996cc0184029e9b6a351a5d850b0202d0b530280760c` |

## 1.4. Prüfumfang und Weiterpflege

Die strukturelle Profilprüfung ist kein bestandener Modelltest. Die zehn fachlichen Fälle sind vorbereitet; ein vollständiger Modelllauf wurde nicht ausgeführt. Marketplace-Import, YAML-Metadaten und die strikte Plugin-CLI-Prüfung bestanden. Die beiden zugeordneten Akten wurden als Gesamt-PDF, flaches Originalformat-ZIP und flaches Einzel-PDF-ZIP gebaut. Originaldateien, Warnhinweise, Rechendaten und Dokumentgrenzen wurden gesondert geprüft.

Die README und die Manifeste nennen Version 444.7.0. Bei späteren Promptänderungen müssen die Hashes im Prüfprofil und in diesem Nachweis erneut aus den tatsächlichen Dateibytes berechnet werden. Die neun Regressionen in `scripts/test-betriebskosten-hausverwaltung.py` sichern Belegidentität, Steuerkette, Zahlungen, Messgrößen, native Dateien und gespeicherte Excel-Ergebnisse; sie ersetzen keine fachliche Kontrolle eines neuen Mandats.
