# 1 Unabhängige Abschlussprüfung Bad Salzuflen

Prüfdatum: 6. Oktober 2026. Ergebnis: bestanden; keine offenen Befunde im geprüften Umfang.

Die Einzel-PDFs der neuen Unterlagen 58 bis 75 wurden vollständig auf Abschneiden, überlagerte Inhalte, unvollständige Tabellen und ungünstige Seitenumbrüche geprüft. Der Umfang beträgt 18 Dokumente mit 25 Seiten. Die fünf neuen Word-Dokumente 58, 61, 69, 70 und 71 wurden zusätzlich mit dem kanonischen `render_docx.py` und dem gebündelten LibreOffice gerendert. Alle fünf Renderseiten wurden betrachtet; ihr extrahierter Text stimmt mit den entsprechenden Einzel-PDFs überein.

| Unterlagen | Geprüfte Seiten |
|---|---:|
| 58 bis 71, jeweils einseitig | 14 |
| 72 Offene Posten mit Belegweg | 4 |
| 73 Projektstunden mit Kostenbrücke | 2 |
| 74 Mietbelege und Zahlungszuordnung | 2 |
| 75 Zahlungsplanung mit Freigaben | 3 |

# 2 Erledigte Befunde

1. Beleg 64 nennt den Abschluss der Sanitärarbeiten nun am 6. September, passend zu Rechnung 35 und Register 47. Für den 5. September ist ausdrücklich kein Einsatz erfasst. Der Ansatz bleibt bei 40 Personenstunden und 3.200,00 EUR.
2. Die letzte Notiz im Blatt „Belegweg“ der Mappe 72 war im PDF vertikal abgeschnitten. Nach Kürzung, Verschiebung in Zeile 26 und Verringerung der Datenzeilenhöhe von 48 auf 44 Punkt ist sie vollständig sichtbar. Die final neu erzeugten Seiten 3 und 4 wurden erneut geprüft.
3. In Mappe 73 stehen Summenzeile und Erläuterung nun auf derselben Seite wie die Personalstunden. Eine alleinstehende Summenseite verbleibt nicht.
4. Die Perspektive der Zahlungshinweise in 72 und 74 wurde auf ausgeführte Zahlungen berichtigt. Der Lohnbrief 71 verwendet „übergebener Stundenbestand“.

# 3 Inhaltlicher Abgleich

Die neuen Belegketten wurden gegen die zugehörigen Altunterlagen abgeglichen: Rethmar 1.071,00 EUR minus 500,00 EUR ergibt 571,00 EUR; die ungeklärte Weser-Zahlung über 1.785,00 EUR bleibt getrennt. Bei Bega gleichen 238,00 EUR Rechnungskorrektur und 2.618,00 EUR Zahlung die Rechnung über 2.856,00 EUR aus. Die Steinwerk-Zuordnung 2.142,00 EUR und 714,00 EUR ergibt genau die Sammelzahlung über 2.856,00 EUR. Lohnkosten und die drei belegten Bankabgänge ergeben jeweils 25.400,00 EUR. Die zusätzlichen Unterlagen erzeugen keine zweiten Rechnungen und nehmen offene Freigaben nicht vorweg.

# 4 Nachweise und Grenze

Der maschinenlesbare Sichtprüfungsnachweis einschließlich SHA-256 der 18 geprüften Einzel-PDFs liegt unter `/tmp/bauwirtschaft-vertiefung-20261006/bad/abschluss-sichtpruefung.json`. Die kanonischen Word-Render liegen in `canonical-docx-58`, `canonical-docx-61`, `canonical-docx-69`, `canonical-docx-70` und `canonical-docx-71` desselben Prüfverzeichnisses; der Textvergleich steht in `canonical-vergleich.json`.

Diese Prüfung betrifft die neuen Unterlagen. Unveränderte Altseiten wurden nicht erneut vollständig visuell geprüft. Native Formel- und Zelländerungstests sowie die abschließende gemeinsame Paketregression werden getrennt durch den Hauptprüfpfad dokumentiert. Es wurden keine Bad-Salzuflen-Aktenstücke durch den unabhängigen Prüfer verändert.
