# 12 — Äquivalenzdoktrin-Prüfung (EP 3 218 922 B1 vs. IceFree v3)

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Stadter-Birkenhain | Stand: 24.02.2026

---

## 1. Rechtlicher Rahmen — Äquivalenz

Die Prüfung der Äquivalenz ist für den vorliegenden Fall ergänzend zur Wortlautanalyse relevant, da der Mandant mögliche Redesign-Optionen auf technisch abgewandelten Realisierungen aufbauen möchte, die in Aktenstück 17 bewertet werden.

Rechtsgrundlage: § 14 PatG (Schutzbereich), Art. 69 EPÜ i.V.m. Protokoll. Leitentscheidung Bundesgerichtshof: BGH X ZR 156/12 „Schafteinlage" (Äquivalenz-Dreifrage-Test, bestätigt durch BGH X ZR 109/04 „Schneidmesser I", X ZR 76/12 „Kommunikationskanal").

Der BGH-Dreifragen-Test (aus X ZR 156/12):

1. **Gleichwirkung**: Löst das abgewandelte Mittel die dem Patentanspruch zugrunde liegende Aufgabe mit objektiv gleichwertigen Mitteln?
2. **Naheliegen**: Orientieren sich Fachleute auf Basis ihrer Fachkenntnisse an dem abgewandelten Mittel als gleichwertige Lösung?
3. **Gleichwertigkeit**: Sind die Überlegungen, die der Fachmann anstellt, denjenigen so nahe, dass er das abgewandelte Mittel in Betracht zieht?

## 2. Äquivalenzprüfung: Redesign-Option 1 — Optische Eisdetektion

Vellbruck M4: „Kapazitive Sensoranordnung zur Eisdicken-Messung."

IceFree v3 Redesign-Option A: Ersatz der kapazitiven Sensoren durch optische Laser-Reflexionsmessung (Lidar-basiert, 905 nm).

**Dreifragen-Test:**
1. Gleichwirkung: Optische Messung bestimmt ebenfalls Eisdicke/Eisbedeckung. Gleichwirkung gegeben — die technische Aufgabe (Eisdetektion) wird gelöst.
2. Naheliegen: Optische Eisdetektion ist im Stand der Technik für Windkraftanlagen bekannt (z.B. NordBoxx Lidar-System). Für den Fachmann naheliegend.
3. Gleichwertigkeit: Der Fachmann würde optische Sensoren als Alternativmittel zur kapazitiven Messung in Betracht ziehen, da beide dasselbe Ergebnis liefern.

Ergebnis: Option A wäre nach BGH-Dreifragen-Test als äquivalent zu M4 anzusehen. **Kein Ausweg über Redesign-Option A.** Verletzung durch Äquivalenz trotz Wortlautabweichung.

## 3. Äquivalenzprüfung: Redesign-Option 2 — Vibrationssensorik statt kapazitiv

M4 Redesign-Option B: Ersatz durch Vibrationssensoren (MEMS-Beschleunigungssensor) zur Eis-Detektion via Schwingungsänderung.

**Dreifragen-Test:**
1. Gleichwirkung: Vibrationssensor misst nicht direkt Eisdicke, sondern indirekt Änderung der Rotorblatt-Schwingungscharakteristik. Andere physikalische Messgröße. Eisdicke wird nicht gemessen, sondern auf Eisbildung geschlossen. Gleichwirkung fraglich — Vellbruck-Anspruch spricht von „Messung der Eisdicke", nicht von „Detektion der Eisbildung".
2. Naheliegen: Vibrationssensorik ist eine prinzipiell andere Messmethode. Ob der Fachmann sie als Äquivalent zu kapazitiver Direktmessung ansähe, ist zweifelhaft.
3. Gleichwertigkeit: Deutlich andere physikalische Funktionsweise.

Ergebnis: Option B ist möglicherweise kein Äquivalent — Abweichung bei M4 könnte tragen. Verteidigungsargument möglich, aber nicht sicher. Risikoeinschätzung: 40 % Wahrscheinlichkeit, dass Gericht Vibrationssensorik als äquivalent zu kapazitiver Direktmessung ansieht. → **GELB-ROT**.

Hinweis: US 11 002 248 B2 (Vestas) schützt explizit kapazitive Sensorik + ML. Wechsel zu Vibrationssensor umgeht US-02, bleibt aber EP-Problem.

## 4. Äquivalenzprüfung: Redesign-Option 3 — Nicht-kohlenstoffbasiertes Material

M3 Redesign-Option C: Heizmatten aus Metallfolie (Nickel-Chrom-Legierung) statt Kohlefaservlies.

Dreifragen-Test:
1. Gleichwirkung: NiCr-Metallfolie ist Widerstandsheizelement, erwärmt Rotorblatt — Gleichwirkung gegeben.
2. Naheliegen: NiCr ist ältere Technologie (vgl. EP 2 462 344 B1 Vestas). Fachmann kennt sie als Alternative.
3. Gleichwertigkeit: Gleichwertiges Mittel technisch gegeben.

**Aber**: Beschränkung auf „kohlenstoffbasiertes" Material im Anspruchswortlaut ist — im Kontext der Beschreibung — als bewusste Einschränkung zu verstehen (Differenzierung zum Stand der Technik EP 2 462 344). BGH „Formstein-Einwand" (§ 6 PatG a.F., heute abgeleitet): Wenn das äquivalente Mittel selbst Stand der Technik ist, kann keine Äquivalenzverletzung bejaht werden. NiCr-Metallfolie = Stand der Technik (EP 2 462 344, prioritär früher). → **Kein Äquivalenz-Problem für Option C** wenn Formstein-Einwand greift.

Ergebnis Option C: Möglicherweise valider Design-Around-Weg für das Vellbruck-Patent, aber technisch rückschrittlich (NiCr hat höhere Masse, schlechtere Integration, geringere Dauerhaltbarkeit).

## 5. Bedeutung der BGH-Rechtsprechung X ZR 156/12

BGH X ZR 156/12 „Schafteinlage" (Leitsatz): „Bei der Prüfung, ob eine technische Ausführung unter den Schutzbereich eines Patents fällt, ist zu untersuchen, ob die beanspruchte Lehre mit der technischen Funktion der verwendeten Mittel übereinstimmt oder ob die abgewandelte Ausführung eine gleichwertige Funktion erfüllt, die der Fachmann aufgrund seines Fachwissens als gleichwirkend erkennen kann."

Anwendung: Für M4 (Sensorik) und M5 (Energieübertragung) ergibt sich nach dieser Maßgabe, dass beide Merkmale bei IceFree v3 nicht nur wörtlich, sondern auch funktional identisch verwirklicht sind. Eine Äquivalenzabweichung würde nur bei wirklich verschiedener physikalischer Funktionsweise (wie Vibrationssensor vs. Kapazitätsmessung) in Betracht kommen.

Quellen: [BGH X ZR 156/12](https://www.bundesgerichtshof.de) | [dejure.org — § 14 PatG](https://dejure.org/gesetze/PatG/14.html) | [EPO Art. 69 EPÜ Protokoll](https://www.epo.org/law-practice/legal-texts/epc/current-version-20130101/article/a69.html) | [BGH X ZR 109/04 Schneidmesser I](https://www.bundesgerichtshof.de)
