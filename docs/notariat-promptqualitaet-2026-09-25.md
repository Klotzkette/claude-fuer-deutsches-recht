# 1. Notariat, Werkstätten und Mini-Prompts – Prüfung vom 25. September 2026

## 1.1. Ergebnis und direkter Einstieg

Die [Bauwirtschaft](../bauwirtschaft/README.md) bietet weiterhin zwanzig Skills und vier Testakten für HOAI-Leistungsphasen, Vergabe, Projektsteuerung und Buchhaltung. Der [Workshop-Leitfaden](bauwirtschaft-workshop.md) enthält unmittelbar verwendbare Übungsaufträge. Die [Notariatswerkstatt](../notariat-alltag/README.md) ist in dieser Überarbeitung fachlich vertieft und um konkrete Folgeentwürfe ergänzt.

Alle 245 eigenständigen Werkstätten und 245 Minis wurden durch einen automatischen Bestandsscan erfasst. Dieser prüft Größe, Quellenzuordnung, Vorgaben für vollständige Arbeitsprodukte und Fortsetzung sowie den Schutz vor unbeabsichtigtem Überschreiben. Auffälligkeiten und die überarbeiteten Fachpassagen wurden gezielt nachgelesen; beim Notariat wurden alle zwanzig Skills und beide Prompts einzeln gelesen. Zusätzlich wurden die in den redaktionellen Qualitätsprofilen genannten Rechtsprechungsanker anhand ihrer Quellen abgeglichen. Der genaue Quellenstand wird im [Quellenregister](../quality/source-audits/2026-09-25/README.md) je Rechtsgebiet dokumentiert.

Diese Prüfung ist ein dokumentierter Redaktions- und Quellendurchgang. Sie ist keine Garantie für jeden möglichen Mandatsfall, keine vollständige Prüfung sämtlicher Aussagen aller einzelnen Spezialskills und kein ausgeführter Vergleich der Antworten verschiedener KI-Modelle. Ein korrekter Rechtsprechungsanker ersetzt nicht die Prüfung des aktuellen Normstands und der tatsächlichen Vergleichbarkeit im konkreten Auftrag.

## 1.2. Verbesserungen am Notariats-Plugin

Alle zwanzig Skills und beide Prompts wurden einzeln gelesen. Zwölf Fachskills wurden inhaltlich vertieft; weitere Änderungen betreffen die Gliederung und die Fortsetzung im Hauptworkflow. Die sieben zugeordneten Testakten bleiben unverändert. Für die sechs kompakten Vorgänge wurden die bestehenden zwölf ZIP-Varianten technisch geprüft.

| Gegenstand | Konkrete Verbesserung |
| --- | --- |
| GmbH-Gründung und Kapitalerhöhung | Besondere Form der Gründungsvollmacht, Mitwirkung sämtlicher erforderlicher Geschäftsführer und zeitliche Zuordnung bei Organwechseln; Gesellschaftsregister als Voraussetzung für die Aufnahme einer GbR in die Gesellschafterliste. |
| Grundstück und Grundschuld | Unbedingte Auflassung von Vollzugsweisungen trennen; schriftliche Bankänderung in alle betroffenen persönlichen Haftungserklärungen übernehmen; dingliche Mitwirkung und übrige Bankbedingungen gesondert prüfen. |
| Genehmigung und Ausland | Zweiwochenfrist nach BGB Paragraf 177 Absatz 2 an die richtige Aufforderung, deren Zugang und den Erklärungsempfänger knüpfen; Apostille und Vertretungsbefugnis auseinanderhalten. |
| Umwandlung | Verschmelzung und Spaltung mit unterschiedlicher Registerfolge, Bilanzstichtag und Betriebsratszuleitung bearbeiten. |
| Verwahrung, Geldwäsche und Kosten | Voraussetzungen zulässiger Verwahrung, besondere Vollzugsregeln des GwG und Gebührenübergang nach Auftragseingang konkretisieren. |
| Vorsorge und Familie | Gesundheitsvollmacht, eigene Behandlungsentscheidung, Freiheitsentziehung und Zwangsmaßnahmen getrennt behandeln; ehevertragliche Wirksamkeits- und Ausübungskontrolle unterscheiden. |

Die Werkstatt enthält vollständige Bank- und Nachforderungsschreiben sowie ausdrücklich abgegrenzte Klauselbeispiele. Sie verlangt anschließend den gesamten zum Auftrag passenden Entwurf. Die Beispiele ersetzen keine fehlenden Falldaten und werden nicht als vollständige Urkunde ausgegeben.

Vier BGH-Entscheidungen sind im [Notariats-Quellenregister](../notariat-alltag/references/rechtsprechung-geprueft.md) mit amtlichem Volltext, Fundstelle, Aussage und Grenze dokumentiert. Die Entscheidungen von 2016 und 2017 verwenden teilweise frühere Betreuungsrechtsnormen; deren Nummern werden nicht als heutige Vorschriften übernommen. Der Mini umfasst 7.465 UTF-8-Bytes und bleibt damit innerhalb der gemeinsamen Grenze von 7.500 Bytes und Zeichen. Die Werkstatt umfasst 67.140 Bytes; sie wurde nicht auf eine vorgegebene Seitenzahl aufgefüllt.

Sechs zusätzliche Evaluationsfälle beschreiben die erwarteten Ergebnisse unter anderem bei Bankantwort, Gesundheitsvollmacht und Formfehlern. Das Profil enthält nun vierzehn Fälle. Diese Fälle sind Prüfvorgaben; sie werden hier nicht als ausgeführte Live-Modellläufe bezeichnet. Eine unabhängige Inhaltsprobe hat die Fortsetzung bei ausschließlich dinglicher Mitwirkung einer Miteigentümerin und bei einer Gesundheitsvollmacht ohne Zwangsbefugnis nachvollzogen.

## 1.3. Vollständige Werkstätten statt automatischem Textverlust

Die bisherige Generatorfunktion konnte bei Überschreitung von 48 KiB zunächst Musterbausteine und Abschlusskontrolle entfernen, danach Quellenlisten und Arbeitsweise verkürzen. Dieser Mechanismus ist beseitigt. Die Werkstatt bleibt vollständig; bei Überschreitung des Dateischutzes wird ein ausdrücklicher Fehler gemeldet.

Der gemeinsame Dateischutz beträgt 1 MiB für eine eigenständige Werkstatt. Das ist keine Zielgröße und kein Modellkontext-Versprechen. Die Grenze für Minis beträgt weiterhin 7.500 Bytes; der Generator verwendet hierfür einen Puffer bei 7.400 Bytes. Die Laufzeitbudgets installierter Skills, Routingdateien und Bewertungsanfragen werden dadurch nicht erweitert.

Normanker behalten die ganze ausgewählte Quellenzeile. Damit verschwinden ein zweiter Satz, eine Ausnahme oder eine zeitliche Einschränkung nicht allein wegen eines Satzpunkts. Die vollständige kuratierte Entscheidungsliste bleibt auch hinter Eintrag fünf erhalten. Im Mini darf die Auswahl zusätzlicher Anker geringer ausfallen; ein ausgewählter Rechtssatz wird dafür nicht mitten in seiner Einschränkung abgeschnitten. Individuell redigierte Prompts bleiben durch ihren überprüften Dateihash geschützt.

Der Fehlermechanismus wurde an langen Testtexten reproduziert. Bei der Rekonstruktion aller 245 aktuellen Generatorfassungen lag jedoch keine über der alten Grenze; die größte umfasste 48.028 Bytes. Keine bestehende Handfassung war mit der rekonstruierten Generatorfassung bytegleich. Deshalb lässt sich kein konkreter heutiger Fachverlust allein auf die frühere Größenkürzung zurückführen.

## 1.4. Quellenbefunde und ihre Grenzen

Der Abgleich umfasst 343 Quellenzuordnungen in 245 Profilen mit 288 verschiedenen URLs. Mehrere URLs können dieselbe Entscheidung bezeichnen; diese Zahl wird deshalb nicht als Anzahl verschiedener Urteile ausgegeben. Das Register hält die Aussage und Grenze jeder Zuordnung sowie den tatsächlich verwendeten Nachweis fest.

Das Datum von BAG, Urteil, 5 AZR 347/21 wurde von 23.02.2022 auf **09.02.2022** berichtigt. Die [amtlichen Gründe](https://www.bundesarbeitsgericht.de/entscheidung/5-azr-347-21/) tragen die Gesamtberechnung des Annahmeverzugs. Vier zuvor nur im Qualitätsprofil erfasste Arbeitsrechtsanker stehen jetzt auch in der Werkstatt, jeweils mit Aussage und Grenze. Bei BAG 5 AZR 37/25 bleibt ausdrücklich erkennbar, dass der hier geprüfte Nachweis eine Pressemitteilung ist.

Die Bankrechtswerkstatt erhält den überprüften Beschluss BGH XI ZR 71/25 mit engem Aussageumfang: Die Entscheidung lässt das Verhältnis der angesprochenen Anspruchsgrundlagen offen und verneint die Kausalität im entschiedenen Fall. Daraus wird kein allgemeiner Ausschluss eines DSGVO-Schadensersatzanspruchs abgeleitet.

Im Strafbefehls-Prompt wurde bei BVerfG 2 BvR 1351/23 „Auslieferungshaft“ durch „Abschiebehaft“ ersetzt. Bei der PrALR-Zitierung wurde die Entscheidungsart ergänzt; im Insolvenzplan-Mini wird IX ZB 13/16 durchgehend zutreffend als Beschluss bezeichnet. Einzelne überholte Abrufvermerke wurden gezielt korrigiert. Ein erfolgreich heruntergeladener Text wird erst nach Abgleich der tatsächlich zitierten Passage als inhaltlich geprüft erfasst. Pressemitteilungen, historische Juristentexte und lediglich indexiert lesbare Entscheidungsgründe bleiben als solche unterscheidbar. Das Quellenregister enthält keine neu erfundenen Randnummern für unnummerierte Originale.

## 1.5. Technische Prüfung

Die Regressionen prüfen insbesondere die vollständige Erhaltung einer Werkstatt oberhalb von 128 KiB, die ausdrückliche Ablehnung oberhalb von 1 MiB, vollständige Normeinschränkungen, die Entscheidungsliste, individuelle Hashkontrolle sowie begrenzte Minis. Die isolierte Renderprobe erzeugte alle 490 Texte im Speicher ohne Fehler. Sie schrieb keine Handfassung um.

Die abschließenden Repositoryprüfungen erfassen Plugin- und Marketplace-Struktur, YAML-Frontmatter, Laufzeitbudgets, Auswahlbeschreibungen, Qualitätsprofile, Prompt-Hygiene und Navigation. Die Veröffentlichung enthält die konsistent neu erzeugten Übersichten. Prüfsummen beziehen sich jeweils auf den dokumentierten Arbeitsstand; spätere Änderungen erfordern eine neue Prüfung der betroffenen Inhalte.

Die parallel auf `main` ergänzte Arbeitszeugnisprüfung ist vollständig übernommen. Ihre fünf aktuellen Quellenzuordnungen sind ebenfalls abgeglichen. Ein erneuter Generatorlauf verändert keine erzeugte Markdown-Datei. Die 27 erfolgreichen technischen Prüfaufrufe am integrierten Stand sind im [Prüfprotokoll](../quality/source-audits/2026-09-25/technical-checks.json) aufgeführt. Das Auswahl-Audit meldet außerdem 1.162 Gruppen gleichnamiger Skilltitel als fachliche Prüfanlässe; diese sind weder als bestätigte Doppelungen noch als vollständig bereinigt ausgewiesen.
