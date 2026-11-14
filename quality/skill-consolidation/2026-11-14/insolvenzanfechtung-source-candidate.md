# Insolvenzanfechtung: aktueller Quellkandidat ohne historischen Releasetausch

Datum: 14.11.2026. Der ausdrücklich mit `--candidate` gestartete CI-Build darf den aktuellen Fachanwalts-Parent verwenden, wenn Marketplace, Quellenpfad, Manifestversion und Komponentenroute exakt zusammenpassen. Der historische Standardpfad bleibt auf `445.35.4` festgelegt und bricht bei neueren Quellen vor der Paketerzeugung ab. `VERSION`, `TAG`, `PARENT_VERSION` und `PROOF` bleiben unverändert.

Ein Quellkandidat hat `tag: null` und `source_candidate_not_published`; der historische Releasebezug wird separat bezeichnet. `--candidate` und `--write-proof` bleiben gegenseitig ausgeschlossen. Die alten Proof- und Paketversionsdateien sind vor/nach dem echten Build bytegleich.

Die zwei bisherigen Candidate-Tests bleiben unverändert. Vier zusätzliche Tests prüfen aktuellen Buildinhalt, fehlende/falsche Route, falsches Manifest, doppelte Marketplaceeinträge, fremden Quellpfad, beliebige Versionen sowie den historischen Ausgabe- und Proofschutz. Alle sechs Tests bestehen. Die Quelltestsuite ist erfolgreich (neun Tests, davon der dist-abhängige Test zunächst ausgelassen); anschließend bestehen am tatsächlich gebauten Candidate-Dist alle neun Tests. Das Dist enthält 36 Dateien; der Parent ist als `445.36.0` manifestiert und zur `qualitaetsrunde-v445.36.0` geroutet.

Die 15 bestehenden Aktenassets wurden aus dem lokalen früheren Dist als Eingangsdaten wiederverwendet; die Testakten wurden in diesem Lauf nicht neu erzeugt. Keine Veröffentlichung und keine erneute juristische Vollprüfung. Einzelresultate, Schutzdatei-Hashes und Lognachweise stehen in der JSON-Beilage.
