---
name: entscheidungsidentitaet-abgleichen
description: Prüft, ob Gericht, Entscheidungsform, Datum, Aktenzeichen, ECLI und Veröffentlichungsfundstelle wirklich dieselbe Entscheidung bezeichnen. Erkennt vermischte Nachweise und trennt eine echte Entscheidung von einer falschen Parallelfundstelle.
---

# Entscheidungsidentität abgleichen

## 1. Zweck und Anwendungsfall

Eine Fundstelle kann echt sein und trotzdem die falsche Entscheidung bezeichnen. Dieser Skill prüft deshalb die bibliographische Identität unabhängig davon, ob das gefundene Dokument ungefähr zum Thema passt. Er erkennt insbesondere Mischzitate, bei denen Gericht und Aktenzeichen aus einem Verfahren, Datum oder Entscheidungsform aus einem anderen Vorgang und eine Zeitschriftenseite aus einer weiteren Veröffentlichung zusammengefügt wurden.

Das Ergebnis lautet nicht bloß „gefunden“. Es benennt genau, welche Identitätsmerkmale bestätigt, widersprüchlich oder offen sind. Die Existenz irgendeiner Entscheidung unter einem Aktenzeichen reicht nicht aus: In einem Verfahren können verschiedene Entscheidungen, Berichtigungen und Verfahrensschritte vorkommen. Auch ein korrekt identifiziertes Urteil muss anschließend auf Fundpunkt, Aussage und Übertragbarkeit geprüft werden.

## 2. Eingaben

Übernehmen Sie die unveränderte Originalfundstelle mit F-Kennung, die zugehörigen Q- und A-Kennungen sowie das [Quellenprotokoll](../../references/quellenprotokoll.md). Benötigt werden der tatsächlich geöffnete amtliche Originalvolltext und die behaupteten bibliographischen Angaben. Fehlt der Volltext, kann allenfalls ein ausdrücklich begrenzter Metadatenvergleich stattfinden; eine vollständige Identitätsbestätigung bleibt offen.

Fehlende Entscheidungsform, mehrdeutige Datumsangaben und unvollständige Aktenzeichen werden nicht stillschweigend ergänzt. Wenn die Originalangabe mehrere Deutungen erlaubt, suchen und dokumentieren Sie diese als Kandidaten. Die Eingabe darf nicht durch eine passendere Quelle überschrieben werden.

## 3. Ablauf und Checkliste

### 3.1. Merkmale aus beiden Dokumenten gegenüberstellen

Lesen Sie die amtliche Dokumentüberschrift und die weiteren identifizierenden Angaben im Volltext. Vergleichen Sie Gericht, Spruchkörper soweit vorhanden, Entscheidungsform, Entscheidungsdatum, Aktenzeichen und ECLI mit dem Originalzitat. Erfassen Sie die Sprachfassung und gegebenenfalls eine amtliche Berichtigung. Unterscheiden Sie Entscheidungsdatum, Veröffentlichungsdatum, Abrufdatum und Datum einer Pressemitteilung.

Eine zulässige Normalisierung von Leerzeichen oder typographischen Strichen wird als Darstellungskorrektur behandelt. Ein veränderter Zahlenbestand, Gerichtsort oder Verfahrenstyp ist dagegen ein inhaltlicher Unterschied. Die Möglichkeit eines Tippfehlers ist eine Hypothese, keine Erlaubnis, das falsche Merkmal als bestätigt zu zählen.

### 3.2. Quellen- und Verfahrensketten auseinanderhalten

Trennen Sie Ausgangsentscheidung, Rechtsmittelentscheidung, Vorlageentscheidung, Schlussanträge, Beschluss, Urteil und spätere Berichtigung. Ein Dokument kann das Aktenzeichen einer Vorinstanz zitieren, ohne selbst deren Entscheidung zu sein. Ein amtlicher Volltext mit passendem Suchwort liefert noch keine Identitätsbestätigung für jede darin erwähnte Entscheidung.

Bei verbundenen Verfahren prüfen Sie, welche Aktenzeichen der Originaltext tatsächlich ausweist und ob die behauptete Aussage dem betreffenden Entscheidungsteil zugeordnet werden kann. Bei mehreren Entscheidungen desselben Datums und Gerichts prüfen Sie das vollständige Aktenzeichen. Thematische Nähe darf die eindeutigen Identitätsdaten nicht ersetzen.

### 3.3. Veröffentlichungsfundstellen separat prüfen

Eine beim Gericht verifizierte Entscheidung bestätigt nicht automatisch eine NJW-, NZA-, BeckRS-, juris- oder sonstige Veröffentlichungsnummer. Prüfen Sie solche Angaben nur am tatsächlich zugänglichen Original der jeweiligen Veröffentlichung. Ein zugänglicher Originalverlag ist für seine bibliographischen Angaben maßgeblich; er ersetzt in diesem Plugin nicht den amtlichen gerichtlichen Volltext.

Bestätigt der amtliche Text Gericht, Datum und Aktenzeichen, während die Zeitschriftenfundstelle nicht zugänglich ist, lautet das Ergebnis ausdrücklich: „Die Entscheidung ist identifiziert; die angegebene Parallelfundstelle bleibt ungeprüft.“ Zeigt das zugängliche Veröffentlichungsoriginal an der genannten Seite einen anderen Beitrag, wird diese Abweichung positiv dokumentiert. Entfernen Sie den falschen Nachweis nicht aus der Prüfspur.

### 3.4. Widersprüche als Befund formulieren

Unterscheiden Sie drei Situationen. Erstens: Die Merkmale sind widerspruchsfrei am amtlichen Volltext bestätigt. Zweitens: Ein tatsächlich geöffnetes Original zeigt eine konkrete andere Identität; nennen Sie beide Angaben und den Nachweis. Drittens: Die Suche bleibt erfolglos oder mehrere Kandidaten bleiben möglich; erklären Sie die Identität als ungeklärt.

Nur die zweite Situation trägt den Befund einer nachgewiesenen Fehlzuordnung. Aus der dritten folgt nicht, dass eine Entscheidung erfunden ist. Formulieren Sie etwa: „Ich weiß nicht, welche Entscheidung gemeint ist. Die geprüften amtlichen Zugänge erlauben keine eindeutige Zuordnung.“ Ein ECLI, der nur syntaktisch plausibel aussieht, wird ebenfalls nicht als vorhandene Entscheidung behandelt.

### 3.5. Korrekturvorschlag getrennt begründen

Ein möglicher Ersatz erhält eine eigene Q-Kennung und bleibt als Vorschlag erkennbar. Bestätigen Sie dessen Identität neu; lassen Sie anschließend Fundpunkt, Aussage und Übertragbarkeit prüfen. Die Formulierung „gemeint war offensichtlich“ ist ohne belastbare Anknüpfung zu vermeiden. Selbst bei einem klaren Zahlendreher dokumentieren Sie Original, Änderung, Beleg und verbleibende Unsicherheit.

Ein falsches Datum kann ein redaktioneller Fehler sein, ein andersartiger Beschluss eine wesentliche inhaltliche Verwechslung. Beschreiben Sie die Folge für die konkrete Verwendung, statt aus jedem Fehler einen Täuschungsvorwurf abzuleiten. Über die Entstehung des Fehlers entscheidet dieser Skill nicht.

### 3.6. Ergebnisse weiterreichen

Übergeben Sie bestätigte Identität und offene Teilangaben an [Zitate und Randnummern prüfen](../zitate-und-randnummern-pruefen/SKILL.md). Bei fehlendem amtlichem Original kehrt die Frage an [Amtliche Quellen erschließen](../amtliche-quellen-erschliessen/SKILL.md) zurück. Übernehmen Sie die F-Kennungen unverändert. Die einzelnen Vorkommen bleiben getrennt, selbst wenn derselbe bibliographische Fehler mehrfach auftritt.

### 3.7. Datum und Gerichtsname reichen nicht

Nutzen Sie den verifizierten [BAG-Beschluss vom 30.09.2026 – 2 AZN 339/26](https://www.bundesarbeitsgericht.de/entscheidung/2-azn-339-26/), Rn. 15, als Kontrollfall: Das Gericht unterscheidet eine tatsächlich vorhandene Entscheidung desselben Datums von dem falschen Aktenzeichen, falschen Senat und unpassenden Thema im Schriftsatz. **Trägt:** Ein zeitlich passender Gerichtstreffer heilt die gemischte Identität nicht. **Trägt nicht:** Der im BAG-Text genannte andere Treffer sei ohne eigene Lektüre bereits als Ersatz für die beabsichtigte Aussage geprüft.

Beim Anker selbst ist der 30.09.2026 das Entscheidungsdatum. Der 22.09.2026 in Rn. 8 bezeichnet den dortigen Abruf anderer Hinweise. Übernehmen Sie diesen Tag weder als Entscheidungsdatum noch als eigenen Abruf. Eine solche Verwechslung wird mit Originalwert, richtigem Wert und Änderungsgrund dokumentiert.

## 4. Quellenpflicht

Maßgeblich sind die strenge [Zitierweise](../../references/zitierweise.md) und der [Prüfvertrag](../../references/pruefvertrag.md). Gerichtliche Identität wird am tatsächlich zugänglichen amtlichen Originalvolltext geprüft. Suchtreffer, Sekundärdatenbanken, Pressemitteilungen und Nutzerdokumente allein bilden keinen vollständigen Nachweis. Ist nur amtliche Metadateninformation zugänglich, benennen Sie den beschränkten Beweisumfang. Keine reale Entscheidung wird aus Modellwissen ergänzt; abstrakte Übungen dürfen nicht als verifizierte Rechtsprechung erscheinen.

## 5. Ausgabeformat

Erstellen Sie für jede strittige Fundstelle eine Tabelle mit höchstens vier Spalten: Merkmal, Originalangabe, gelesene Quellenangabe, Befund. Fügen Sie einen vollständig ausformulierten Ergebnisabsatz hinzu. Er nennt bestätigte Merkmale, konkrete Widersprüche, offene Parallelfundstellen und den nächsten Prüfschritt. Inhaltliche Eignung darf nicht aus bibliographischer Übereinstimmung abgeleitet werden.

Ein geeigneter Warnsatz lautet: „Vorsicht: Die angegebene Fundstelle führt zu einer anderen Entscheidung. Der zitierte Rechtssatz ist damit noch nicht belegt.“ Formatierte Dokumente verwenden soweit technisch möglich Times New Roman, 11 pt und dezimale Gliederung; für Chat oder Markdown folgt ein getrennter Exporthinweis. Das Original bleibt unverändert, eine vorgeschlagene Zitierkorrektur steht daneben.

## 6. Beispiele

**Abstrakte Übungsannahme:** Das Register nennt ein OLG-Urteil. Am angegebenen amtlichen Fundort steht ein Beschluss desselben Gerichts zu einem anderen Aktenzeichen. Dokumentieren Sie beide Identitäten und die Fehlzuordnung. Ein ähnliches Stichwort im Beschluss heilt den Fehler nicht.

**Abstrakte Übungsannahme:** Gericht, Datum, Aktenzeichen und ECLI stimmen im amtlichen Urteil überein. Die angegebene Zeitschriftenseite ist mangels Originalzugang nicht lesbar. Bestätigen Sie ausschließlich die gerichtliche Identität; die Veröffentlichungsfundstelle bleibt ausdrücklich offen.
