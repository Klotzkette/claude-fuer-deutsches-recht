# Quellen- und Redaktionsprüfung des Werkstattprompts zu § 138 InsO

## 1. Gegenstand und Zeitpunkt

Geprüft wurde am 15.11.2026 der eigenständig verwendbare Prompt [138-nahestehende-personen.md](../../../insolvenzanfechtung/werkstattprompts/138-nahestehende-personen.md). Die Prüfung umfasst tatsächlichen Abruf amtlicher Originalquellen, Lesen der entscheidungstragenden Passagen, normbezogene Übertragung und eine redaktionelle Gegenkontrolle. Sie ist kein vollständiger Rechtsprechungsbericht zu sämtlichen Nähebeziehungen und kein Ausführungstest eines Sprachmodells.

## 2. Quellenbestand

[audit-138.json](audit-138.json) enthält die exakten Abruf-URLs, HTTP-Ergebnisse, Rohdateigrößen, SHA-256-Werte, Lesebereiche und Aussagegrenzen. Die 18 erfolgreich abgerufenen Originaldateien liegen verlustfrei komprimiert unter [originale-138](originale-138). Der SHA-256-Wert bezieht sich jeweils auf die dekomprimierten Originalbytes. Die Archive wurden durch Rückdekomprimierung und Bytevergleich geprüft.

Fünf BGH-Entscheidungen tragen unterschiedliche Teile des Prompts:

- BGH, Urteil vom 21.05.2026 – Az. IX ZR 168/24, insbesondere Rn. 17–20 und 41–48, trennt § 133 Abs. 1 und 4 sowie interne Krisenkommunikation, äußere Zahlungseinstellung und die Indizienwirkung eines Gesellschaftergeschäfts.
- BGH, Urteil vom 06.03.2025 – Az. IX ZR 209/23, insbesondere Rn. 21–28 und 37–45, betrifft das AnfG. Der Prompt kennzeichnet diesen Kontext und begründet die Übertragung der Beweiswürdigungsgrundsätze. Er übernimmt keine allgemeine Urkundenvorlagepflicht aus einer sekundären Darlegungslast.
- BGH, Urteil vom 22.02.2024 – Az. IX ZR 106/21, insbesondere Rn. 9–14 und 21, belegt die Einbeziehung mittelbarer Beteiligungen sowie die Grenze der Kenntnisvermutung gegenüber objektiven Anfechtungsvoraussetzungen.
- BGH, Versäumnisurteil vom 22.12.2016 – Az. IX ZR 94/14, insbesondere Rn. 8–18, trägt die Verbindung zwischen Gesellschaften über Organpersonen und deren persönliche Beziehungen sowie die konkret zu prüfende gesetzliche Verschwiegenheitsausnahme. Die Entscheidungsform wurde zutreffend bezeichnet.
- BGH, Urteil vom 01.07.2010 – Az. IX ZR 58/09, insbesondere Rn. 9–16 und 18–24, trägt die besondere Vermutung subjektiver Merkmale und deren Widerlegung beim heutigen § 133 Abs. 4. Die alte Absatznummer und der güterrechtliche Kontext bleiben sichtbar.

Die Normen §§ 130–133, 137, 138 und 145 InsO, §§ 138, 142, 286 und 292 ZPO, § 16 AktG und Art. 103j EGInsO wurden in den amtlichen Einzelnormfassungen vollständig gelesen. Nicht bereitgestellte Literatur wurde nicht geprüft; Literaturzitate innerhalb der Urteile wurden nicht als selbst gelesene Quellen übernommen.

## 3. Fachliche Gegenkontrolle

Der Prompt unterscheidet die Definition der Nähe, die konkrete Verweisungsnorm und deren genaue Rechtsfolge. Die Kapitalgrenze lautet mehr als 25 Prozent. Bei mittelbaren Beteiligungen wird eine rechtliche Zurechnung geprüft und nicht ausschließlich die wirtschaftliche Prozentquote multipliziert. Der Kontrast zwischen dem tatsächlich entschiedenen vollständigen Beteiligungsstrang und einem eigenen didaktischen Mehrheitsbeispiel ist ausdrücklich angegeben.

Die Verschwiegenheitsausnahme wird nicht auf Berufsgeheimnisträger verengt. Konkrete gesetzliche Pflicht, sachlicher Geheimnisumfang, mögliche Aufgabe des Geheimhaltungsinteresses und andere selbständige Nähewege bleiben getrennt. Ebenso werden objektive Zahlungsunfähigkeit, Benachteiligung, Vorsatz und Kenntnis nicht aus einer Nähebeziehung pauschal abgeleitet.

§ 133 Abs. 1, der besondere Vertragstatbestand des Absatzes 4 und die Folgen für Rechtsnachfolger nach § 145 werden getrennt bearbeitet. Eine sekundäre Darlegungslast wird weder mit Beweislastumkehr noch mit einem vorprozessualen Dokumentenherausgabeanspruch gleichgesetzt. Der Prompt enthält ausgeführte Beispiele für die genaue Einwendungsebene und konkrete Zeugenfragen.

## 4. Nachweise und Grenzen

Die lokale Strukturprüfung bestätigt 20 fortlaufend nummerierte Fachabschnitte und 6.766 durch Leerraum getrennte Wörter. Alle 17 externen Links des Prompts zeigen auf tatsächlich heruntergeladene Quellen. Quellarchive, dezimale Überschriften und fehlende nachlaufende Leerzeichen wurden technisch geprüft. Die aktuelle Inhaltsdatei und ihr SHA-256-Wert sind in der JSON-Datei festgehalten.

Die 14 fachlichen Kontrollpunkte im JSON wurden redaktionell gegen Normen und gelesene Entscheidungsstellen geprüft. Es wurde kein ChatGPT- oder Claude-Ausführungsbenchmark durchgeführt. Die PDF-Satzprobe, Gesamtintegration und Veröffentlichung gehören zum übergeordneten Auftrag und werden durch diesen Teilbericht nicht als erledigt behauptet. Eine spätere Änderung der Inhaltsdatei verlangt eine entsprechende Aktualisierung ihrer Prüfsumme und Wortzahl; alte Quellenaudits wurden nicht umdatiert.
