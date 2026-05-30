# Aktenstück 03 — Einstufung: Hochrisiko-KI nach Anhang III Nr. 7 KI-VO / Medizinprodukt Klasse IIb MDR

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 14.03.2026  
**Bearbeitung:** RAin Dr. Henrietta Vellbruck-Steinheim  
**Rechtliche Grundlage:** Art. 6 Abs. 2 KI-VO (EU) 2024/1689; Anhang III Nr. 7 KI-VO; MDR (EU) 2017/745 Anhang VIII Regel 22

---

## 1. Rechtlicher Ausgangspunkt

Art. 6 Abs. 2 KI-VO bestimmt, dass KI-Systeme, die unter einen der in Anhang III genannten Anwendungsfälle fallen, als Hochrisiko-KI-Systeme eingestuft werden. Für solche Systeme gelten die Anforderungen der Art. 9–15 KI-VO unmittelbar. Die Einstufung als Hochrisiko-KI begründet zudem die Pflicht zur Konformitätsbewertung nach Art. 43 KI-VO sowie zur Registrierung in der EU-Datenbank nach Art. 49 KI-VO.

Davon zu unterscheiden ist die eigenständige Medizinprodukteeinstufung nach MDR (EU) 2017/745. Beide Rechtsregimes bestehen parallel; die KI-VO-Konformität ersetzt nicht die MDR-Konformität und umgekehrt (vgl. Erwägungsgrund 84 KI-VO sowie Art. 8 KI-VO zur Harmonisierung).

---

## 2. Prüfung Anhang III Nr. 7 KI-VO

Anhang III Nr. 7 KI-VO erfasst:

> „KI-Systeme, die für den Einsatz als Sicherheitskomponenten bei der Verwaltung und dem Betrieb von Straßenverkehr, Wasserversorgung, Gas, Wärme und Strom bestimmt sind, sowie KI-Systeme, die für den Einsatz im Bereich kritischer digitaler Infrastruktur bestimmt sind, **sowie KI-Systeme, die für den Einsatz in Notfalldiensten und für erste Reaktion auf Notfälle bestimmt sind**, einschließlich [...]"

### 2.1 Subsumtion

**Tatbestandsmerkmal „Notfalldienste":** MedAssist v4 dient der automatisierten Disposition von Notfallressourcen in Krankenhäusern. Es übernimmt die Klassifikation von Notrufen und schlägt Ressourcenverteilungen vor. Notrufe und die darauf aufbauende Ressourcenverteilung sind klassische Tätigkeiten von Notfalldiensten i.S.d. Anhang III Nr. 7. Der Begriff ist weit auszulegen und umfasst nicht nur Feuerwehr und Rettungsdienst im engeren Sinne, sondern auch krankenhausbetriebene Leitstellen (vgl. Kommissions-Leitfaden zur Auslegung von Anhang III, COM/2024/9812, Rn. 47 f.).

**Tatbestandsmerkmal „Sicherheitskomponente":** MedAssist v4 nimmt in der Prozesskette der Notfalldisposition eine sicherheitskritische Funktion ein: Eine fehlerhafte Klassifikation (insbesondere Unterklassifikation von Dringlichkeitsstufe 1) kann unmittelbar zu Patientengefährdung führen. Die False-Negative-Rate von 8,8 % für lebensbedrohliche Einsätze (s. Aktenstück 02, Abschn. 5) unterstreicht dies.

**Ergebnis:** MedAssist v4 fällt unter Anhang III Nr. 7 KI-VO. Es handelt sich um ein Hochrisiko-KI-System.

### 2.2 Keine Ausnahmetatbestände (Art. 6 Abs. 3 KI-VO)

Art. 6 Abs. 3 KI-VO sieht vor, dass Hochrisiko-KI-Systeme aus Anhang III unter bestimmten Voraussetzungen (kein erhebliches Risiko für Grundrechte, kein enger Bezug zu sicherheitskritischen Entscheidungen) aus der Hochrisiko-Kategorie herausgenommen werden können. Diese Ausnahme greift hier nicht:

- Die Funktion der Notrufdisposition hat unmittelbaren Bezug zu Leben und körperlicher Unversehrtheit (Art. 2 GRCh) der Patienten.
- MedAssist v4 trifft — trotz konzeptionell vorgesehener menschlicher Aufsicht — in der Praxis systemgesteuerte Weichenstellungen, die ohne vollständige Override-Kapazität getroffen werden (s. Aktenstück 09).
- Eine Selbsteinstufung außerhalb der Hochrisiko-Kategorie scheidet aus.

---

## 3. Prüfung Medizinprodukt Klasse IIb (MDR)

### 3.1 Medizinprodukterecht-Einordnung

MedAssist v4 verarbeitet Patientendaten mit dem Ziel, medizinische Entscheidungsunterstützung zu leisten. Nach Regel 11 Anhang VIII MDR sind Softwareprodukte, die zur Unterstützung klinischer Entscheidungen verwendet werden, und die zu Ergebnissen führen, die Auswirkungen auf Diagnose, Therapie oder medizinische Versorgung haben, als Medizinprodukte einzustufen.

Die Klassifizierung als Klasse IIb folgt aus Regel 22 Anhang VIII MDR: Software, die zur Kontrolle physiologischer Prozesse oder zur Therapieentscheidung verwendet wird, die mit erhöhten Risiken verbunden ist. Die Notrufdisposition (Triage, Ressourcenzuweisung bei lebensbedrohlichen Zuständen) stellt eine solche risikoerhöhende Funktion dar.

### 3.2 BfArM-Bescheid

Das Bundesinstitut für Arzneimittel und Medizinprodukte (BfArM) hat mit Bescheid vom 12.01.2026 (Az. MED-AI-2026-0319) festgestellt, dass MedAssist v4 die MDR-Grundlegenden Anforderungen (Anhang I MDR) erfüllt und die Konformitätsbewertung durch die benannte Stelle (Notified Body) TÜV SÜD Product Service GmbH (NB 0123) abgeschlossen worden ist. Das CE-Kennzeichen nach MDR wurde am 20.12.2025 angebracht.

Der BfArM-Bescheid enthält jedoch den expliziten Hinweis:

> „Die vorliegende Feststellung beschränkt sich auf die Anforderungen der Verordnung (EU) 2017/745. Anforderungen der Verordnung (EU) 2024/1689 (KI-VO) werden von diesem Bescheid nicht erfasst und sind gesondert zu erfüllen."

---

## 4. Parallelkonformität MDR / KI-VO

### 4.1 Grundsatz der Parallelgeltung

Weder KI-VO noch MDR sehen vor, dass die Konformität nach einem der Regime die andere ersetzt. Art. 8 KI-VO normiert ausdrücklich, dass die KI-VO sektorspezifische Rechtsvorschriften — darunter MDR — unberührt lässt, soweit diese höhere Schutzstandards vorsehen. Im Übrigen bestehen beide Pflichtenregime kumulativ.

### 4.2 Koordinationspunkte

| Pflicht | MDR-Regelung | KI-VO-Regelung | Koordinationsbedarf |
|---|---|---|---|
| Technische Dokumentation | Anhang II MDR | Art. 11 + Anhang IV KI-VO | Zusammenführung in einem Dokument möglich, aber Lücken möglich |
| Konformitätsbewertung | Art. 52–54 MDR (Notified Body) | Art. 43 KI-VO (intern oder Notified Body) | Koordination TÜV SÜD / interne Bewertung |
| CE-Kennzeichnung | Art. 20 MDR | Art. 48 KI-VO | Anbringungsort, Zeitpunkt zu klären (s. Aktenstück 14) |
| Marktüberwachung | Art. 83–89 MDR (BfArM) | Art. 74–80 KI-VO (BNetzA) | Parallele Behördenzuständigkeit — Koordination erforderlich |
| Vigilanz/Meldepflichten | Art. 87 MDR | Art. 73 KI-VO | Meldepflichten bei schwerwiegenden Vorfällen teilweise deckungsgleich |

### 4.3 Rechtliche Einschätzung

Die Doppelregulierung erhöht den Compliance-Aufwand erheblich. Eine koordinierte Dokumentationsstrategie (gemeinsamer Technischer Dossier-Ansatz) wird empfohlen. Für die CE-Kennzeichnung ist zu prüfen, ob das MDR-CE-Zeichen und das KI-VO-CE-Zeichen kombiniert angebracht werden können oder separate Anbringungen erforderlich sind (s. Aktenstück 14).

---

## 5. Ergebnis

**MedAssist v4 ist:**
- Hochrisiko-KI-System nach Art. 6 Abs. 2 KI-VO i.V.m. Anhang III Nr. 7 KI-VO — **eindeutig und ohne Ausnahmetatbestand**
- Medizinprodukt Klasse IIb nach MDR (EU) 2017/745 — **MDR-Konformität bescheinigt (BfArM MED-AI-2026-0319), KI-VO-Konformität ausstehend**

Die Einstufung als Hochrisiko-KI zieht alle Anforderungen der Art. 9–15 KI-VO nach sich. Die Frist zur vollständigen Konformität läuft gemäß Art. 113 Abs. 1 KI-VO zum 02.08.2026.

---

*Heidelberg, 14.03.2026*  
*RAin Dr. Henrietta Vellbruck-Steinheim — Az. 2026-V-0427*
