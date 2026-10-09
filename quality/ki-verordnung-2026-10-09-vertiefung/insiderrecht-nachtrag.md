# 1. Insiderrecht: Korrektur der KI-Prognoseprüfung

Prüfdatum: 09.10.2026. Bearbeitet wurde ausschließlich der KI-bezogene Arbeitsweg in `insiderrecht-compliance/skills/ki-archivierung/SKILL.md`.

## 1.1. Tatsächlich geöffnete amtliche Quelle

Gelesen wurde die vollständige deutsche PDF-Datei der konsolidierten Verordnung (EU) Nr. 596/2014 mit Stand 05.06.2026, Kennung `02014R0596 — DE — 05.06.2026 — 005.001`, über den Publikationsdienst der Europäischen Union. Die Datei hat 70 Seiten und 733057 Bytes. Ihre SHA-256-Prüfsumme lautet `66bffe1ff85b97d0671b6e237a5123e54214d6a1f2c361385948535e816372d5`.

- [Amtlicher PDF-Volltext bei EU Publications/CELLAR](https://publications.europa.eu/resource/cellar/b5b43c29-3d97-11f1-814f-01aa75ed71a1.0006.03/DOC_1).
- [EUR-Lex-Dokument der konsolidierten Fassung](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02014R0596-20260605).
- [Amtlicher Metadatenzugang zur deutschen PDF-Fassung](https://publications.europa.eu/resource/consolidation/2014R0596%2F20260605.DEU.pdfa2a).

Der direkte EUR-Lex-Abruf war bei dieser Prüfung durch eine JavaScript-Abfrage eingeschränkt. Der amtliche Metadatenzugang führte zur oben verlinkten vollständigen PDF-Datei; deren Inhalt wurde anschließend unmittelbar gelesen. Der Befund beruht nicht nur auf Suchtreffern. Der konsolidierte Text ist ein Hilfsmittel zur Ermittlung des geltenden Wortlauts und ersetzt nicht die verbindlichen Amtsblattfassungen.

## 1.2. Gelesene Passagen und Folgerungen

| Gelesene Vorschrift | PDF-Seiten | Folgerung für den KI-Arbeitsweg |
| --- | --- | --- |
| Artikel 7 Absätze 1 bis 4 | 13–14 | Der konkrete Informationsinhalt ist anhand der Tatbestandsmerkmale zu prüfen. Präzision setzt keine festen Zahlenwerte und keine Gewissheit über ein künftiges Ereignis voraus. Modellkonfidenz ist kein Tatsachenbeleg. Der Anlegermaßstab ersetzt die übrigen Merkmale nicht. |
| Artikel 8 Absätze 1 bis 5 | 14–15 | Zugang zum Modell, Besitz konkreter Insiderinformationen, Nutzung und Handlung sind unterschiedliche Tatsachen. Die Merkmale der jeweiligen Handlung und Person bleiben erforderlich. |
| Artikel 9 Absätze 1 bis 6 | 15–17 | Wirksame Informationsbarrieren und weitere legitime Handlungen sind zu prüfen. Die Norm trägt kein generelles Verbot jedes Modellzugangs einer Handelsabteilung. |
| Artikel 10 Absätze 1 und 2 sowie Artikel 14 | 17, 25–26 | Offenlegung, Empfehlung und Handel haben gesonderte Voraussetzungen. Die Verbotsnorm darf nicht auf eine automatische Folge aus einem Modellkonto verkürzt werden. |
| Artikel 18 Absätze 1 bis 8 | 31–33 | Listenpflicht, verpflichtete Stelle, aufgabenbezogener Zugang, Einträge, Aktualisierung und besondere Anwendungsregeln sind zu trennen. Modellzugang allein ist kein Ersatz für diese Prüfung. |

## 1.3. Umfang und Kontrolle der Korrektur

Die pauschalen Schlüsse aus festen Zahlenwerten, Anlegerinteresse und Modellzugang wurden durch die vorstehende Normkette ersetzt. Unmittelbar widersprechende Verkürzungen zur Datenherkunft und zum internen Prognosesystem wurden angeglichen. Die KI-Verordnungsabgrenzung und die übrigen Arbeitsschritte bleiben erhalten. Es wurde keine neue Gerichtsentscheidung oder Randnummer eingefügt.

Die geänderten Markdown-Dateien wurden auf verbleibende Pauschalsätze und Formatfehler geprüft. `git diff --check` für die beiden zugewiesenen Dateien ist bestanden. Eine zusätzliche Bewertung anderer MAR-Pflichten oder eine vollständige Neubearbeitung des Plugins ist damit nicht verbunden.
