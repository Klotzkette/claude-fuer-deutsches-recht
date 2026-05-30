# Aktenstück 10 — Empfehlungsalgorithmus HalmRank und Non-Profiling-Option (Art. 27 DSA)

**Az. Kanzlei:** KRS-2026-0318-DSA
**Bearbeitung:** RA Felix Wendland
**Stand:** 05. April 2026

---

## 1. Normgrundlage und BNetzA-Beanstandung

Art. 27 Abs. 1 DSA verpflichtet VLOPs, die Empfehlungssysteme einsetzen, mindestens eine Option anzubieten, die nicht auf Profiling im Sinne des Art. 4 Nr. 4 DSGVO basiert. Die Bundesnetzagentur hat im Mahnschreiben vom 02. April 2026 (Az. BNetzA-DSC-2026-188) beanstandet, dass Halmweise.de im Zeitraum bis März 2026 ausschließlich den personalisierten Empfehlungsalgorithmus HalmRank angeboten hat, ohne eine profilierungsfreie Alternative für Nutzer bereitzustellen.

---

## 2. Technische Beschreibung HalmRank

HalmRank ist der proprietäre Empfehlungsalgorithmus von Halmweise.de. Er bewertet und priorisiert Inhalte im Newsfeed, in der Suche und in der Entdecken-Funktion anhand folgender Signale:

| Signal | Gewichtung (ca.) | Profilingbasiert |
|---|---|---|
| Explizite Nutzerinteraktionen (Likes, Kommentare) | 35% | Ja |
| Verweildauer auf Content | 25% | Ja |
| Themen-Cluster (Nutzerinteressen-Modell) | 20% | Ja |
| Community-Engagement des Erstellers | 12% | Nein |
| Aktualität des Inhalts | 8% | Nein |

Das Themen-Cluster-Modell basiert auf einer langfristigen Analyse des Nutzerverhaltens und stellt Profiling im Sinne des Art. 4 Nr. 4 DSGVO dar. Die personalisierten Interaktions- und Verweilzeitsignale konstituieren ebenfalls Profiling.

---

## 3. Anforderungen an die Non-Profiling-Option (Art. 27 Abs. 1 lit. b DSA)

### 3.1 Definition "nicht auf Profiling basierend"

Art. 27 Abs. 1 lit. b DSA verlangt eine Option, die nicht auf der Analyse des individuellen Nutzerverhaltens basiert. Zulässige Kriterien für eine Non-Profiling-Option sind:

- Chronologische Reihenfolge (nach Veröffentlichungszeitpunkt)
- Popularität (aggregierte Engagement-Signale ohne Individualisierung)
- Zufallsprinzip (algorithmisch gestützte Diversität ohne Nutzermodell)
- Geographische oder thematische Filter ohne verhaltensbasiertes Profil

### 3.2 Zugänglichkeit und Transparenz

Art. 27 Abs. 1 DSA verlangt, dass die Non-Profiling-Option:
- leicht zugänglich (Art. 27 Abs. 2 DSA: in direkter Reichweite der Nutzer)
- klar beschrieben (Art. 27 Abs. 1 lit. a DSA: Hauptparameter des Empfehlungssystems)
- im Transparenzbericht dokumentiert ist (Art. 42 Abs. 2 lit. c DSA)

---

## 4. Implementierungsplan HalmRank Non-Profiling

### 4.1 Chronologische Timeline

**Bezeichnung:** "Halmweise Chronologisch"
**Ranking-Logik:** Beiträge aller abonnierten Accounts und Communities in umgekehrt chronologischer Reihenfolge; kein profilbasiertes Re-Ranking.
**Zulässige nicht-profiling Gewichtungen:** Kennzeichnung von gesponsorten Inhalten; Community-Moderationsstatus.

### 4.2 UI-Umsetzung

- Einstellungsmenü: Toggle "Chronologische Ansicht aktivieren" unter "Feed-Einstellungen"
- Persistent: Einstellung bleibt über Sessions gespeichert
- Onboarding-Hinweis für neue Nutzer auf die Wahlmöglichkeit

### 4.3 Zeitplan

| Meilenstein | Frist |
|---|---|
| Technisches Konzept abgeschlossen | 20.04.2026 |
| Entwicklung und Testphase | 21.04.–15.06.2026 |
| Rollout EU-weit | 15.06.2026 |
| Dokumentation für Transparenzbericht | 01.07.2026 |

---

## 5. Datenschutz-Schnittstelle

Die Non-Profiling-Option steht in engem Zusammenhang mit dem datenschutzrechtlichen Opt-out-Recht nach Art. 21 DSGVO (Widerspruch gegen Verarbeitung zu Direktmarketingzwecken) sowie dem Opt-out gegen personalisierte Werbung. Die Kanzlei empfiehlt, die Art. 27 DSA-Non-Profiling-Option technisch mit dem DSGVO-Widerspruchsrecht zu verknüpfen:

- Nutzer, die nach Art. 21 DSGVO widersprechen: werden automatisch auf chronologische Timeline umgestellt.
- Nutzer, die nur DSA-Non-Profiling wählen: weiterhin personalisierte Werbung (sofern hierfür separate DSGVO-Einwilligung vorliegt).

**Abstimmung erforderlich** mit DPO Dr. Kerstin Nolde-Braun.

---

## 6. Transparenzanforderungen nach Art. 27 Abs. 1 lit. a DSA

Für jedes eingesetzte Empfehlungssystem sind die Hauptparameter verständlich darzustellen. Für HalmRank bedeutet dies:

- Beschreibung der verwendeten Signale (Interaktionen, Verweildauer, Themen-Cluster)
- Möglichkeit des Nutzers, die Relevanz einzelner Parameter anzupassen (optional, aber empfohlen)
- Klare Unterscheidung zwischen HalmRank (personalisiert) und Chronologischer Timeline (nicht personalisiert)

---

## 7. Verhältnis zu Art. 35 DSA (Risikominderung)

Die Implementierung der Non-Profiling-Option dient auch der Risikominderung nach Art. 35 DSA: Durch die Abkehr von Engagement-maximierenden Algorithmen kann der Filterblasen-Effekt reduziert und die demokratische Debattenqualität gefördert werden.

---

## 8. Rechtsgrundlagen

- Art. 27 DSA (EU) 2022/2065 — Empfehlungssysteme und Non-Profiling-Pflicht
- Art. 4 Nr. 4 DSGVO (EU) 2016/679 — Definition Profiling
- Art. 21 DSGVO — Widerspruchsrecht

**Quellen:**
- Verordnung (EU) 2022/2065 (DSA), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2065
- Verordnung (EU) 2016/679 (DSGVO), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679

---

*Bearbeitung: RA Felix Wendland*
*Stand: 05. April 2026*
