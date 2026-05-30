# Aktenstück 08 — Art. 13 KI-VO: Transparenz und Informationspflichten des Anbieters

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 01.04.2026  
**Bearbeitung:** RAin Dr. Henrietta Vellbruck-Steinheim  
**Rechtsgrundlage:** Art. 13 KI-VO (EU) 2024/1689

---

## 1. Anforderungen Art. 13 KI-VO

Art. 13 KI-VO verlangt, dass Hochrisiko-KI-Systeme so konzipiert und entwickelt werden, dass ihr Betrieb hinreichend transparent ist, um Betreibern zu ermöglichen, die Ausgaben des Systems zu verstehen und sachgerecht zu nutzen. Anbieter haben zudem Betreiber-Anleitungen beizufügen (Art. 13 Abs. 3), die mindestens enthalten:

- Identität und Kontaktdaten des Anbieters (Art. 13 Abs. 3 lit. a)
- Bestimmungsgemäße Zwecke, Leistungsmerkmale und Einsatzbeschränkungen (Art. 13 Abs. 3 lit. b)
- Genauigkeitsgrad, Robustheit und Cybersicherheitsgrenzen (Art. 13 Abs. 3 lit. c)
- Anforderungen an Inputdaten (Art. 13 Abs. 3 lit. d)
- Inbetriebnahme-, Betriebs- und Wartungsanweisungen (Art. 13 Abs. 3 lit. e)
- Informationen zur menschlichen Aufsicht (Art. 13 Abs. 3 lit. f)
- Maßnahmen bei Ausfällen (Art. 13 Abs. 3 lit. g)
- Rechte der Nutzer/betroffenen Personen (Art. 13 Abs. 3 lit. h)

---

## 2. Prüfung Benutzerhandbuch MedAssist v4.1

Das Benutzerhandbuch v4.1 (Stand August 2024, 68 Seiten) wurde von MedAssist AI GmbH am 08.03.2026 übermittelt. Es liegt nur auf Deutsch vor.

### 2.1 Checkliste Transparenzanforderungen

| Anforderung Art. 13 Abs. 3 | Vorhanden | Vollständig | Anmerkung |
|---|---|---|---|
| lit. a — Identität Anbieter | Ja | Ja | S. 2 des Handbuchs |
| lit. b — Bestimmungszweck, Leistungsmerkmale | Teilweise | Nein | Einsatzbeschränkungen fehlen |
| lit. c — Genauigkeitsgrad, Robustheit | Nein | — | Keinerlei Angaben zu Accuracy-Limits |
| lit. d — Inputdaten-Anforderungen | Teilweise | Nein | Nur Audioformat beschrieben; Sprachabdeckung unklar |
| lit. e — Inbetriebnahme, Betrieb, Wartung | Ja | Teilweise | Wartungsfenster nicht dokumentiert |
| lit. f — Menschliche Aufsicht | Teilweise | Nein | Override-Verfahren beschrieben, aber nicht verpflichtend formuliert |
| lit. g — Maßnahmen bei Ausfällen | Nein | — | Fallback-Verfahren nicht beschrieben |
| lit. h — Rechte betroffener Personen | Nein | — | Keine Information zu DSGVO-Rechten von Patienten |

### 2.2 Kritische Lücken

**Fehlende Einsatzbeschränkungen (lit. b):** Das Handbuch beschreibt MedAssist v4 als „entscheidungsunterstützendes" System, enthält aber keine ausdrückliche Aussage dazu, für welche Szenarien das System ausdrücklich nicht eingesetzt werden darf (z.B. Auslandsnotrufe, fremdsprachige Anrufer, technische Grenzfälle). Die Klärung von Einsatzgrenzen ist insbesondere angesichts der False-Negative-Rate von 8,8 % bei Dringlichkeit 1 dringend geboten.

**Keine Genauigkeitsangaben für Betreiber (lit. c):** Disponenten und Klinikverwaltungen haben keinen Zugang zu den im internen Testbericht MA-EVAL-2024-03 enthaltenen Accuracy-Daten. Sie können die Systemempfehlung damit nicht in ihren Unsicherheitskontext einordnen. Dies verletzt Art. 13 Abs. 1 KI-VO (Transparenz-Grundpflicht) und untergräbt die menschliche Aufsicht nach Art. 14 KI-VO erheblich.

**Kein Fallback-Verfahren (lit. g):** Bei einem Systemausfall — wie im Fall des 47-minütigen Ausfalls im Klinikum Freiburg-Süd (2025) — fehlt ein dokumentiertes Rückfall-Verfahren auf manuelle Disposition. Das Klinikum Freiburg-Süd hat im Nachgang berichtet, dass das Personal in diesem Zeitraum improvisieren musste, da kein analoges Backup-Protokoll existierte.

**Patientenrechte (lit. h):** Art. 22 DSGVO gewährt Patienten das Recht, nicht einer ausschließlich automatisierten Entscheidung unterworfen zu sein. Im Kontext von MedAssist v4 ist fraglich, ob die de-facto-Dispositionsentscheidung als „ausschließlich automatisiert" i.S.d. Art. 22 Abs. 1 DSGVO gilt — angesichts fehlender Override-Protokolle in 14 Kliniken ist dies nicht auszuschließen. Das Benutzerhandbuch enthält hierzu keinerlei Hinweise.

---

## 3. Anforderungen an Betreiber-Transparenz (Art. 13 Abs. 1)

Art. 13 Abs. 1 KI-VO verlangt darüber hinaus, dass das System selbst so konstruiert ist, dass es transparent operiert. In der Praxis bedeutet dies: Das System muss Ausgaben mit ausreichender Information versehen (z.B. Konfidenzwerte, Erklärungshinweise), damit Betreiber die Ausgabe sachgerecht beurteilen können.

MedAssist v4 gibt den Konfidenzwert aus, zeigt aber keine Erklärung für die Klassifikation (z.B. „Einordnung als Dringlichkeit 2 aufgrund: erkannte Schlüsselworte [Brustschmerz], Herzerkrankung in Vorgeschichte erkannt, Alter > 60"). Ohne eine solche Erklärung ist die menschliche Beurteilungskapazität des Disponenten erheblich eingeschränkt.

---

## 4. Handlungsempfehlungen

| Maßnahme | Priorität | Frist |
|---|---|---|
| Überarbeitung Benutzerhandbuch (v4.2) — Ergänzung alle lit. a–h | Kritisch | 31.05.2026 |
| Aufnahme Accuracy-Daten und Grenzen in Benutzerhandbuch | Hoch | 31.05.2026 |
| Entwicklung Fallback-Protokoll Manualmode + Schulung | Hoch | 30.04.2026 |
| Erklärbarkeits-Output in Dashboard implementieren | Hoch | 30.06.2026 |
| DSGVO-Betroffenenrechte-Hinweis in Patientenaufklärung klinikkumseitig | Mittel | 30.06.2026 |

---

## 5. Gesamtbewertung Art. 13

**Art. 13 KI-VO: Teilweise konform (mit wesentlichen Lücken).**  
Grundinfrastruktur eines Benutzerhandbuchs existiert. Kritische Lücken bei Einsatzgrenzen, Accuracy-Kommunikation, Fallback und Patientenrechten.

---

*Heidelberg, 01.04.2026*  
*RAin Dr. Henrietta Vellbruck-Steinheim — Az. 2026-V-0427*
