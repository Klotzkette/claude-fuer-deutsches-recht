# Megaprompt: leasingrecht-praxis

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 59 Skills des Plugins `leasingrecht-praxis`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt …
2. **schieds-oder-gerichtsstand-leasing** — Streitbeilegung im Leasingrecht: Schiedsverfahren vs. staatliche Gerichte, Gerichtsstandsklausel, Verbraucherrecht, Medi…
3. **leasing-in-sanierungsgutachten** — Leasing im Sanierungsgutachten: Behandlung von Leasingverbindlichkeiten in IDW S6-Gutachten, Fortführungsprognose, Leasi…
4. **agb-klauseln-restwertgarantie** — AGB-Kontrolle im Leasingvertrag: Einbeziehung, Inhaltskontrolle nach §§ 305–310 BGB, BGH-Kernklauseln, Klauselkatalog fü…
5. **leasingvertrag-redline-fuer-leasingnehmer** — Leasingvertrag-Redline aus Leasingnehmersicht: Problematische Klauseln identifizieren, Gegenentwürfe formulieren, Verhan…
6. **konzernleasing-transfer-franchise** — Konzerninternes Leasing: Verrechnungspreise, § 1 AStG, BEPS-Aktionsplan, Fremdvergleichsgrundsatz, Dokumentationspflicht…
7. **grenzueberschreitendes-leasing-unidroit-und-rechtswahl** — Grenzüberschreitendes Leasing: UNIDROIT-Übereinkommen, Rechtswahl (Rom I-VO), internationales Mobiliar-Leasingrecht, Ste…
8. **diebstahl-totalschaden** — Diebstahl und Totalschaden im Leasing: Gefahrtragung, Ratenpflicht nach Untergang, Versicherungsabwicklung, Anzeigeoblie…
9. **kommunalleasing-vergaberecht-und-haushaltsrecht** — Kommunalleasing: Vergabepflicht, Wirtschaftlichkeitsnachweis, kreditähnliche Rechtsgeschäfte, Genehmigungspflicht und hi…
10. **start-up-equipment-leasing-covenants** — Start-up Equipment-Leasing: Kreditwürdigkeitsprüfung, Financial Covenants, persönliche Bürgschaft, Anlaufrisikoklauseln …
11. **datenschutz-telematik-esg-leasing-start** — Datenschutz und Telematik im Fahrzeugleasing: DSGVO, Verarbeitungszwecke, Beschäftigtendatenschutz § 26 BDSG, Nutzungspr…
12. **esg-leasing-taxonomie-und-green-lease** — ESG und Green Lease: EU-Taxonomie, SFDR, Nachhaltigkeitsklauseln, CO2-Reporting, Green-Finance-Strukturen und ESG-Anford…
13. **lieferant-leasinggeber-leasingnehmer-dreiecksverhaeltn** — Leasingdreieck: Rechtsverhältnisse Lieferant/Leasinggeber/Leasingnehmer, Abtretungskonstruktion, Kollisionsprobleme und …
14. **flugzeugleasing-register-schiffsleasing** — Flugzeug-Leasing: Luftfahrtregister, Kapstadt-Übereinkommen, Internationales Interesse, Wartung nach EASA, Rückgabe-Cond…
15. **lessons-learned-nach-rueckgabe** — Lessons Learned nach Leasingrückgabe: Analyse von Minderwertstreitigkeiten, Prozessverbesserungen, Vertragsoptimierungen…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext ordnet der Skill das Material eigen..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Leasingrecht Praxis** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Leasingrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen. Tragende Normen (BGB §§ 535 ff., AGB-Kontrolle §§ 305 ff. BGB, HGB) werden nicht aus Modellwissen finalisiert, sondern über die zugelassenen Live-Quellen geprüft.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Sofortrisiken zuerst markieren** — Fristen, Zustellung, Form, Zuständigkeit, Beweis-, Kosten- und Haftungsrisiken benennen.
2. **Aktenlandkarte bauen** — Welche Dateien sind Original, welche nur Behauptung; was fehlt für einen verwertbaren nächsten Schritt?
3. **Rolle klären** — Mandant, Gegner, Behörde, Gericht, betroffene Stelle; mit welchem Ziel und welcher Reichweite?
4. **Ziel bestimmen** — Prüfung, Entwurf, Antrag, Anmeldung, Schriftsatz, Verteidigung, Dashboard, Memo, Red-Team?
5. **Rechtsquellen trennen** — Normtext, Behördenpraxis, Rechtsprechung, Vertrag, technischer Standard und Praxisroutine getrennt halten.
6. **Fachmodule auswählen** — Drei bis sieben passende Skills aus diesem Plugin nennen mit Begründung, warum sie jetzt nützlich sind.
7. **Erste verwertbare Ausgabe liefern** — Kurze Lagekarte mit nächstem Schritt oder erstem Entwurf, statt einer langen abstrakten Abhandlung.

## Fachlicher Anker — Leasingrecht

Tragende Anker: BGB §§ 535 ff., AGB-Kontrolle §§ 305 ff. BGB, HGB. Tatsächliche Fundstellen werden über dejure.org, openJur, gesetze-im-internet.de, BGH-/BVerfG-/EuGH-/EuG-Datenbank live geprüft und nicht aus Modellwissen finalisiert.

---

## Skill: `schieds-oder-gerichtsstand-leasing`

_Streitbeilegung im Leasingrecht: Schiedsverfahren vs. staatliche Gerichte, Gerichtsstandsklausel, Verbraucherrecht, Mediation und internationale Schiedsgerichte im Leasingrecht._

# Schiedsverfahren und Gerichtsstand im Leasingrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Gerichtsstandsklauseln

### B2B (Unternehmensleasing)
- § 38 ZPO: Gerichtsstandsvereinbarung zwischen Kaufleuten zulässig
- Formerfordernis: Schriftlich oder in Textform (§ 40 ZPO analog)
- Wirkung: Ausschließlicher oder nicht-ausschließlicher Gerichtsstand

### B2C (Verbraucherleasing)
- § 29c ZPO: Beim Verbraucher nur Gerichtsstand am Wohnort des Verbrauchers
- Gerichtsstandsklauseln zulasten des Verbrauchers: AGB-widrig (§ 307 BGB)
- Ausnahme: Vereinbarung nach Entstehung des Rechtsstreits (§ 38 III ZPO)

### EU: EuGVO (VO 1215/2012)
- Art. 7 EuGVO: Besonderer Gerichtsstand am Erfüllungsort
- Art. 19 ff. EuGVO: Verbraucher hat besondere Schutzgerichtsstand (Wohnsitzland)
- Gerichtsstandsklauseln gegen Verbraucher: Nur eingeschränkt zulässig (Art. 25 EuGVO)

## Schiedsverfahren

### Vorteile
- Vertraulichkeit: Kein öffentliches Verfahren
- Schnelligkeit: Flexible Verfahrensordnung
- Internationale Vollstreckung: New Yorker Übereinkommen (1958) in 170+ Ländern
- Spezialisierung: Branchenkundige Schiedsrichter

### Nachteile
- Kosten: Höher als staatliche Gerichte (Schiedsrichterhonorar)
- Kein einstweiliger Rechtsschutz direkt (Schiedsgericht kann vorsorgliche Maßnahmen anordnen, aber staatliches Gericht vollstreckt)
- Kein gesetzlicher Instanzenzug

### Schiedsklausel (§ 1029 ZPO)
Formerfordernis: Schriftliche Vereinbarung (§ 1031 ZPO); Textform bei Verbrauchern (§ 1031 V ZPO).

Inhalt:
- Schiedsgerichtsordnung (DIS, ICC, LCIA)
- Schiedsort (maßgeblich für Anfechtungsverfahren)
- Schiedsrichteranzahl (1 oder 3)
- Schiedssprache

### DIS-Schiedsregeln (Deutsche Institution für Schiedsgerichtsbarkeit)
- Neue DIS-Regeln 2018
- Expedited Proceedings: Schnellverfahren für Ansprüche bis 2 Mio. €

### Verbraucher und Schiedsverfahren
- § 1031 V ZPO: Bei Verbrauchern muss Schiedsklausel separat unterzeichnet sein
- AGB-Einbeziehung reicht nicht; Überraschungsverbot (§ 305c BGB)
- Schiedsklausel in B2C-AGB praktisch unwirksam

## Mediation und ADR

### Mediationsklausel
- Vor Schiedsverfahren: Mediation (§ 36 VSBG: Verbraucherstreitbeilegungsgesetz)
- Freiwillig; schnell; günstig

### VSBG (Verbraucherstreitbeilegungsgesetz)
- LG muss Verbraucher über Möglichkeit der außergerichtlichen Streitbeilegung informieren (§ 36 VSBG)
- Keine Pflicht zur Teilnahme; aber Information ist Pflicht

## Prüfprogramm

1. B2B oder B2C? Verbraucher → eingeschränkte Gerichtsstandswahl
2. Gerichtsstandsklausel: Wirksam nach § 38 ZPO oder AGB-widrig?
3. Schiedsklausel: Formgültig (§ 1031 ZPO)? Verbraucher separat unterschrieben?
4. Schiedsgericht gewählt: DIS, ICC oder ad hoc? Schiedsort?
5. Einstweiliger Rechtsschutz: Staatliches Gericht parallel?
6. VSBG-Information: Auf Webseite und in AGB erteilt?

## Typische Fallen

- Gerichtsstandsklausel gegen Verbraucher: AGB-widrig; staatliche Gerichte zuständig
- Schiedsklausel in B2C-AGB ohne gesonderte Unterschrift: Unwirksam
- Kein einstweiliger Rechtsschutz über Schiedsgericht vorgesehen: Verzögerung
- VSBG-Informationspflicht verletzt: OLG-Urteile: Abmahnrisiko

## Normen und Quellen

- §§ 1029–1066 ZPO (Schiedsverfahren): https://www.gesetze-im-internet.de/zpo/__1029.html
- § 38 ZPO (Gerichtsstandsvereinbarung): https://www.gesetze-im-internet.de/zpo/__38.html
- EuGVO (VO 1215/2012): https://eur-lex.europa.eu
- New Yorker Übereinkommen 1958: https://www.uncitral.org
- VSBG (Verbraucherstreitbeilegungsgesetz): https://www.gesetze-im-internet.de/vsbg/
- DIS-Schiedsregeln 2018: https://www.dis-arb.de

## Output-Formate

- **Schiedsklausel-Muster B2B**: DIS-Schiedsklausel für Leasingverträge
- **Gerichtsstandsklausel-Muster B2B**: Ausschließlicher Gerichtsstand
- **VSBG-Informationstext**: Pflichthinweis für LG-Website und AGB
- **Mediationsklausel**: Stufenklausel (erst Mediation, dann Schiedsgericht)

---

## Skill: `leasing-in-sanierungsgutachten`

_Leasing im Sanierungsgutachten: Behandlung von Leasingverbindlichkeiten in IDW S6-Gutachten, Fortführungsprognose, Leasingkosten und Restrukturierungsmaßnahmen im Leasingrecht._

# Leasing im Sanierungsgutachten (IDW S6)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## IDW S6: Grundstruktur des Sanierungsgutachtens

IDW S6 (Stand 2018) gliedert das Sanierungsgutachten in:
1. Auftragsumfang und Grundlagen
2. Beschreibung des Unternehmens
3. Analyse der Unternehmenskrise (Ursachen)
4. Leitbild des sanierten Unternehmens
5. Maßnahmenplan
6. Integrierter Sanierungsplan (GuV, Bilanz, Cashflow)
7. Fortführungsprognose

## Leasingverhältnisse in der Krisenanalyse

### Leasingkosten als Krisenursache
- Zu hohe Leasingverpflichtungen für Anlagegüter: Fixkostenblock in Krise
- Operating-Lease-Kosten (bei HGB-Bilanzierer): Nicht in Bilanz, aber in GuV
- IFRS 16 bilanzierende Unternehmen: Leasingverbindlichkeiten sichtbar in Bilanz

### Identifikation der Leasingverhältnisse
- Vollständige Liste aller Leasingverträge (Anlage zum Gutachten)
- Je Vertrag: Objekt, LG, Laufzeit, Rate, Restwert, Eigentümer
- Off-Balance-Verpflichtungen: Im Anhang des Jahresabschlusses (§ 285 Nr. 3a HGB)?

## Leasingkostenanalyse im Sanierungsplan

### Marktpreisvergleich
- Sind die aktuellen Leasingraten marktüblich?
- Wenn zu hoch (z.B. in Boomzeiten abgeschlossen): Neuverhandlung möglich?

### Kündbarkeit und Exit-Optionen
- Vorzeitige Kündigung: Schadensersatz nach BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Abzinsungspflicht)
- Sale-and-Lease-Back: Rückgabe und Neuleasing zu günstigeren Konditionen?
- Rückgabe nicht mehr benötigter Anlagegüter: Fristige Kündigung bei Änderung des Leasinggegenstands

### IFRS-16-Effekte
- Leasingverbindlichkeit als Schuld: Zählmetriken für Kreditgeber (Debt/EBITDA)
- Restrukturierungsmaßnahme: Vorzeitige Kündigung → Entschuldung (aber Schadensersatz)

## Fortführungsprognose: Leasingverpflichtungen

### Cashflow-Projektion
- Leasingraten im Plan-Cashflow erfassen
- Endfällige Zahlungen (Restwert) besonders kritisch: Fälligkeitsprofil prüfen

### Sanierungsmaßnahmen mit Leasingbezug
1. Kündigung von Verträgen für nicht mehr benötigte Objekte
2. Ratenreduktion durch Verlängerung der Laufzeit
3. Sale-and-Lease-Back für neue Liquidität
4. Stundungsvereinbarungen mit LG

### Integrierter Plan
- GuV: Leasingaufwand (HGB) oder Zins + AfA (IFRS 16)
- Bilanz: IFRS 16 – RoU und Verbindlichkeiten
- Cashflow: Leasingzahlungen als Operating-/Financing-Cashflow

## Regulatorische Pflichten

### § 285 Nr. 3a HGB: Anhangspflicht
Außerbilanzielle Verpflichtungen (incl. Operating-Leasing bei HGB) müssen im Anhang ausgewiesen werden, wenn wesentlich.

### IFRS 16 Disclosure
Detaillierte Angaben zu RoU, Leasingverbindlichkeiten, Laufzeiten und Cash-Auswirkungen.

## Prüfprogramm

1. Alle Leasingverträge identifiziert? Liste mit LG, Objekt, Rate, Laufzeit?
2. Off-Balance-Verpflichtungen im Anhang § 285 HGB ausgewiesen?
3. Leasingkosten im Marktvergleich: Angemessen oder zu hoch?
4. Kündigungsoptionen: Vorzeitige Kündigung wirtschaftlich sinnvoll?
5. Sale-and-Lease-Back möglich für neue Liquidität?
6. Integrierter Plan: Leasingraten korrekt erfasst?

## Typische Fallen

- Off-Balance-Leasing vergessen → Cashflow-Plan unterschätzt Fixkostenblock
- Vorzeitige Kündigung ohne Schadensersatzkalkulation → Liquiditätslücke
- IFRS 16 Umstellung in Sanierungsphase → Bilanzkennzahlen verändern sich unerwartet
- LG kooperiert nicht bei Stundung → Kündigung; Restforderung als InsO-Verbindlichkeit

## Normen und Quellen

- IDW S6 (Sanierungsgutachten): https://www.idw.de
- § 285 Nr. 3a HGB (Anhang): https://www.gesetze-im-internet.de/hgb/__285.html
- IFRS 16: https://eur-lex.europa.eu
- §§ 217 ff. InsO (Insolvenzplan): https://www.gesetze-im-internet.de/inso/__217.html
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz Kündigung): https://www.bgh.de
- § 3a EStG (Sanierungsgewinn): https://www.gesetze-im-internet.de/estg/__3a.html

## Output-Formate

- **Leasingvertrags-Liste**: Format für Gutachten-Anlage
- **Cashflow-Leasing**: Zahlungsplan alle Verträge (Rate, Restwert, Fälligkeit)
- **Sanierungsmaßnahmen-Matrix**: Option – Effekt – Kosten – Zeitplan
- **IFRS-16-vs-HGB-Vergleich**: Bilanzielle Darstellung im Plan

---

## Skill: `agb-klauseln-restwertgarantie`

_AGB-Kontrolle im Leasingvertrag: Einbeziehung, Inhaltskontrolle nach §§ 305–310 BGB, BGH-Kernklauseln, Klauselkatalog für Verbraucher- und Unternehmerleasing im Leasingrecht._

# AGB-Kontrolle im Leasingvertrag

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

- § 305 BGB: Einbeziehungsvoraussetzungen
- § 305c BGB: Überraschende und mehrdeutige Klauseln
- § 307 BGB: Generalklausel (unangemessene Benachteiligung)
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit
- § 310 BGB: Bereichsausnahmen (B2B, B2C)
- §§ 506–509 BGB: Verbraucherleasing-Pflichtangaben

## Einbeziehungskontrolle (§ 305 II BGB)

Voraussetzungen für wirksame AGB-Einbeziehung:
1. Ausdrücklicher Hinweis auf AGB bei Vertragsschluss (oder deutlich sichtbarer Aushang)
2. Zumutbare Möglichkeit der Kenntnisnahme
3. Einverständnis des Vertragspartners

Bei Verbrauchern (B2C) strenge Anforderungen. Bei Unternehmern (B2B, § 310 I BGB) erleichterte Einbeziehung; §§ 308, 309 BGB gelten nicht direkt, wirken aber als Indizien für § 307 BGB.

## Klauselkatalog

### 1. Gefahrtragungsklausel
**Typische Formulierung**: „Der Leasingnehmer trägt die Gefahr des zufälligen Untergangs und der zufälligen Verschlechterung des Leasingobjekts."

**Bewertung**: BGH – wirksam bei Finanzierungsleasing (BGH VIII ZR 71/93), da LN wirtschaftlicher Eigentümer ist. Bei Operating-Lease und gegenüber Verbrauchern problematisch (§ 309 Nr. 12 BGB).

### 2. Abtretungsklausel (Gewährleistung)
**Typische Formulierung**: „Der Leasinggeber tritt alle Gewährleistungsansprüche gegen den Lieferanten an den Leasingnehmer ab. Eigene Ansprüche des Leasingnehmers gegen den Leasinggeber sind ausgeschlossen."

**Bewertung**: Grundsätzlich wirksam, wenn die Abtretung tatsächlich erfolgt und LN klagebefugt wird. Unwirksam, wenn Abtretung ins Leere geht (Lieferant insolvent, Frist abgelaufen) und LN dann schutzlos steht (BGH, Urteil vom 13.11.2013 - VIII ZR 257/12).

### 3. Kündigungsklausel bei Zahlungsverzug
**Typische Formulierung**: „Der Leasinggeber kann bei Verzug mit mehr als einer Rate fristlos kündigen."

**Bewertung**: Zulässig im B2B. Im B2C muss Abmahnung vorausgehen (§ 543 III BGB analog). Voraussetzung: Verzug muss erheblich sein (§ 543 II Nr. 3 BGB).

### 4. Schadensersatzklausel nach Kündigung
**Typische Formulierung**: „Bei vorzeitiger Vertragsbeendigung schuldet der Leasingnehmer sämtliche ausstehende Leasingraten bis Vertragsende abzüglich eines Abzinsungsbetrags."

**Bewertung**: Zulässig als Schadensersatz (BGH, Urteil vom 14.03.2007 - VIII ZR 68/06), aber LN muss sich ersparte Aufwendungen und Verwertungserlös anrechnen lassen dürfen. Klauseln, die Anrechnung ausschließen, sind nach § 309 Nr. 5 BGB unwirksam.

### 5. Restwerthaftung
**Typische Formulierung**: „Unterschreitet der Verwertungserlös den kalkulierten Restwert, ist der Leasingnehmer zur Zahlung der Differenz verpflichtet."

**Bewertung**: Restwertgarantien können wirksam sein, müssen aber klar und transparent formuliert sein (§ 307 Abs. 1 Satz 2 BGB). Als frei prüfbare Anker zur Verbraucherleasing-Restwertgarantie kommen BGH, Urteile vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 in Betracht; Mehrerlösfragen gesondert anhand Vertragsmodell und Abrechnung prüfen.

### 6. Totalschadensklausel
**Typische Formulierung**: „Bei Totalschaden oder Verlust sind die ausstehenden Raten sofort fällig; Versicherungsleistung ist anzurechnen."

**Bewertung**: Grundsätzlich zulässig, aber Transparenz und angemessene Anrechnung der Versicherungsleistung erforderlich. Klauseln, die LN doppelt belasten (Raten + fehlende Versicherungsdeckung), sind unwirksam.

### 7. Rückgabeklausel / Minderwert
**Typische Formulierung**: „Das Leasingobjekt ist in einwandfreiem, gebrauchsüblichen Zustand zurückzugeben; Abweichungen werden dem Leasingnehmer berechnet."

**Bewertung**: Zulässig; Verschleiß muss sich auf normale Abnutzung beschränken (BGH VIII ZR 172/05). Klauseln, die auch normale Abnutzung dem LN anlasten, sind nach § 307 unwirksam.

## Prüfprogramm

1. Einbeziehungstatbestand prüfen (§ 305 II BGB): Hinweis + Kenntnisnahme + Einverständnis
2. Überraschende Klauseln identifizieren (§ 305c I BGB)
3. Mehrdeutigkeitsregel anwenden (§ 305c II BGB): Unklarheiten gegen Verwender
4. Für jede Kernklausel: Verbraucher oder Unternehmer? Katalogverbote (§§ 308, 309) oder Generalklausel (§ 307)?
5. Rechtsfolge unwirksamer Klausel: Klausel fällt weg, gesetzliche Regelung tritt ein (§ 306 II BGB)

## Typische Fallen

- AGB nicht ordnungsgemäß einbezogen, weil nur auf Rückseite des Leasingscheins ohne Hinweis auf Vorderseite
- Mehrdeutige Restwertklausel: Verwender (LG) trägt das Risiko der Auslegung
- Schadensersatzklausel ohne Anrechnungsoption: nach § 309 Nr. 5 unwirksam
- Abtretungsklausel fehlt: LN hat keine Mängelrechte gegen Lieferant

## Normen und Quellen

- §§ 305–310 BGB: https://dejure.org/gesetze/BGB/305.html
- BGH VIII ZR 71/93 (Gefahrtragung Finanzierungsleasing): https://www.bgh.de
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12 (Abtretungsklausel): https://www.bgh.de
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz nach Kündigung): https://www.bgh.de
- BGH, Urteil vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 (Restwerthaftung): https://www.bgh.de
- openjur.de AGB-Leasingrecht: https://openjur.de

## Output-Formate

- **Klauselmatrix**: Klausel – Norm – BGH-Bewertung – Wirksam/Unwirksam
- **Redline-Empfehlung**: Geänderte Klauselfassung für AGB-Konformität
- **Prüfbericht**: Klausel-für-Klausel-Analyse mit Handlungsempfehlung

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 26 BDSG
- Art. 13 DSGVO
- Art. 28 DSGVO
- § 1 AStG
- § 3a EStG
- § 4h EStG
- § 5a EStG
- § 11 EStG
- § 6 EGBGB
- Art. 6 DSGVO
- § 36 VSBG
- Art. 101 AEUV

### Leitentscheidungen

- BGH VIII ZR 172/05
- BGH VIII ZR 71/93
- BFH IX R 14/15
- BGH XII ZR 18/08
- BGH XI ZR 59/17

---

## Skill: `leasingvertrag-redline-fuer-leasingnehmer`

_Leasingvertrag-Redline aus Leasingnehmersicht: Problematische Klauseln identifizieren, Gegenentwürfe formulieren, Verhandlungsstrategie und Risikoabsicherung im Leasingrecht._

# Leasingvertrag-Redline: Leasingnehmerperspektive

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Red-Flag-Klauseln aus LN-Sicht

### 1. Fehlende Mehrerlösklausel
**Problem**: Restwertgarantie des LN ohne Beteiligung am Mehrerlös bei Verwertung über Restwert.
**BGH-Anker:** Die Entscheidungen vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 betreffen die Wirksamkeit von Restwertgarantien im Verbraucherleasing. Ob eine fehlende Mehrerlösbeteiligung die konkrete Klausel angreifbar macht, ist gesondert anhand § 307 BGB, Vertragsmodell, Transparenz und Abrechnungspraxis zu prüfen.
**Forderung des LN**: Ergänzung: „Übersteigt der Verwertungserlös den kalkulierten Restwert, erhält der LN mindestens 75 % des Mehrerlöses."

### 2. Unbegrenzte Gefahrtragung
**Problem**: LN trägt das Risiko auch bei unverschuldetem Untergang; keine GAP-Versicherung.
**Risiko**: Totalschaden → LN zahlt Differenz zwischen Versicherung und offener Restschuld.
**Forderung des LN**: „Im Fall des Totalschadens oder Diebstahls deckt die gemäß Vertrag abzuschließende GAP-Versicherung die verbleibende Forderung des LG; eine darüber hinausgehende Haftung des LN ist ausgeschlossen."

### 3. Zu enge Rückgabekonditions-Definition
**Problem**: „Einwandfreier Zustand" ohne Definition normaler Abnutzung → LG kann nahezu jeden Gebrauchsspuren als Minderwert abrechnen.
**BGH VIII ZR 172/05**: Normale Abnutzung darf nicht dem LN angelastet werden.
**Forderung des LN**: Klarer Katalog normaler Abnutzung (Beispiele, Toleranzgrenzen) ins Vertragswerk aufnehmen.

### 4. Einseitige Kündigungsklausel
**Problem**: LG kann bei jeder kleinen Verzögerung ohne Abmahnung kündigen.
**AGB-Recht**: Bei Verbrauchern Abmahnung zwingend; bei Unternehmern kann unverhältnismäßige Klausel nach § 307 BGB unwirksam sein.
**Forderung des LN**: Abmahnung mit 14-tägiger Nachfrist immer vor Kündigung.

### 5. Überlange Nutzungsverantwortung
**Problem**: LN haftet für alle Schäden durch Dritte, auch wenn LN keine Möglichkeit hatte, diesen zu verhindern.
**Forderung des LN**: Beschränkung auf Schäden, die LN zu vertreten hat (§§ 276, 278 BGB).

### 6. Fehlende Rückgabe-Besichtigungsklausel
**Problem**: LG kann das Objekt nach Rückgabe besichtigen, ohne LN beizuziehen → einseitiges Gutachten.
**Forderung des LN**: „Die Besichtigung des Leasingobjekts bei Rückgabe erfolgt gemeinsam mit dem LN. Ein Minderwertgutachten wird LN vorab zugestellt; LN hat 14 Tage Zeit für ein Gegengutachten."

### 7. Fehlende Insolvenzregelung
**Problem**: Vertrag schweigt zur Lage bei Insolvenz des LG.
**Forderung des LN**: Klausel, dass bei Insolvenz des LG das Nutzungsrecht des LN fortbesteht (§ 566 BGB analog).

## Verhandlungsstrategie

### Prioritäten setzen
1. Erstpriorität: Klauseln, die wirtschaftlich maximal schaden (Gefahrtragung, Restwert)
2. Zweitpriorität: Klauseln, die Rechtsdurchsetzung erschweren (Gerichtsstand, Schiedsgericht)
3. Drittpriorität: Formelle Verbesserungen (Protokollklauseln, Fristen)

### Verhandlungstaktik
- „Paket"-Tausch: LN gibt bei Restwertverpflichtung nach, wenn LG GAP-Versicherung stellt
- Zeitdruck nutzen: LN hat Alternativangebote (konkurrierender LG)
- Wirtschaftlichkeitsargument: Klare Kalkulation des Risikos durch LN

## Risikoabsicherung für LN

- GAP-Versicherung: Pflicht oder Option im Vertrag?
- Betriebsunterbrechungsversicherung: Bei Maschinenleasing kritisch
- Sachverständigenklausel: Gegengutachtenrecht bei Minderwertabrechnung
- Sonderkündigungsrecht: Bei Insolvenz LN, betrieblichen Veränderungen, Force Majeure

## Prüfprogramm

1. Mehrerlösklausel bei Restwertgarantie? (Risikopunkt nach § 307 BGB, nicht schematisch als Pflicht behaupten)
2. GAP-Versicherung oder Beschränkung der Haftung nach Totalschaden?
3. Normaler Abnutzungs-Katalog definiert?
4. Abmahnpflicht vor Kündigung? Bei Verbraucher zwingend
5. Gemeinsame Rückgabebesichtigung und Gegengutachtenrecht?
6. § 566 BGB-Analog-Klausel für Insolvenz LG?

## Normen und Quellen

- BGH, Urteil vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 (Restwertgarantie; Mehrerlösfragen gesondert live prüfen): https://www.bgh.de
- BGH VIII ZR 172/05 (normale Abnutzung): https://www.bgh.de
- BGH VIII ZR 71/93 (Gefahrtragung): https://www.bgh.de
- § 566 BGB: https://dejure.org/gesetze/BGB/566.html
- §§ 276, 278 BGB (Verschulden): https://dejure.org/gesetze/BGB/276.html
- §§ 305–310 BGB: https://dejure.org/gesetze/BGB/305.html

## Output-Formate

- **Red-Flag-Liste**: 10 Klauseln die LN ablehnen oder ändern sollte
- **Gegenentwurf-Formulierungen**: Fertige Redline-Texte
- **Verhandlungsbrief**: LN fordert Änderungen mit Begründung
- **Risikoabsicherungsplan**: Welche Versicherungen, welche Klauseln

---

## Skill: `konzernleasing-transfer-franchise`

_Konzerninternes Leasing: Verrechnungspreise, § 1 AStG, BEPS-Aktionsplan, Fremdvergleichsgrundsatz, Dokumentationspflichten und länderbezogene Steuerrisiken im Leasingrecht._

# Konzerninternes Leasing: Transfer Pricing und Verrechnungspreise

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

- § 1 AStG (Einkünftekorrektur bei nahestehenden Personen): Fremdvergleich
- §§ 1a–1e AStG: Dokumentationspflichten, Angemessenheitsnachweis
- § 90 III AO, GAufzV: Aufzeichnungspflichten für Verrechnungspreise
- Art. 9 OECD-Musterabkommen: Verbundene Unternehmen
- BEPS-Aktionspläne 8–10 (OECD 2015): Gewinnkorrektur bei immateriellen Gütern und Dienstleistungen
- EU ATAD-Richtlinien: Hybrids, CFC, Exit Taxation

## Fremdvergleichsgrundsatz (§ 1 AStG)

### Grundsatz
Transaktionen zwischen nahestehenden Personen müssen zu Bedingungen erfolgen, wie sie fremde Dritte unter gleichen Umständen vereinbaren würden.

### Nahestehende Person (§ 1 II AStG)
- Unmittelbare oder mittelbare Beteiligung ≥ 25 % oder beherrschender Einfluss
- Gleiche Person oder Gesellschaft steht hinter beiden Transaktionspartnern

### Verrechnungspreismethoden (OECD-Transfer Pricing Guidelines)

**1. Preisvergleichsmethode (CUP)**
Vergleich mit Drittpreisen für gleichartige Leasingtransaktionen.
- Ideal, aber selten exakt vergleichbar (Custom Terms)

**2. Kostenaufschlagsmethode**
Herstellungskosten (Anschaffungskosten + Finanzierung) + Marktübliche Marge
- Geeignet für Routinetransaktionen (Routineleasing)

**3. TNMM (Transactional Net Margin Method)**
Vergleich der Nettomarge des Leasinggebers mit vergleichbaren Drittunternehmen.

## Dokumentationspflichten (§ 90 III AO, GAufzV)

### Pflicht zur Aufzeichnung
- Aufzeichnungen für alle Transaktionen mit nahestehenden Personen
- Inhalt: Sachverhalt, angewandte Methode, Vergleichsdaten
- Frist: Erstellung bei Abgabe der Steuererklärung; auf Anforderung innerhalb 60 Tage

### Sanktionen bei Nichtdokumentation
- § 162 III AO: Schätzungsbefugnis des Finanzamts
- Zuschläge: 5–10 % der Einkunftskorrektur (§ 162 IV AO)
- Außenprüfung: Besondere Prüfungsdichte bei konzerninternen Transaktionen

## Konzernleasing: Strukturüberlegungen

### Intra-Konzern-Leasinggesellschaft (Captive Lessor)
- Konzern gründet interne Leasinggesellschaft (oft in Niedrigsteuerland: Luxemburg, Irland, Niederlande)
- Captive verleast an Konzerngesellschaften weltweit
- Risiko: Verrechnungspreise müssen fremdvergleichskonform sein; Substanz im Sitzland

### Zinsabzug und BEPS
- BEPS Action 4: Zinsabzugsbeschränkungen (§ 4h EStG, § 8a KStG: Zinsschranke)
- Konzernleasing mit hoher Verschuldung beim LN: Zinsen ggf. nicht abzugsfähig

## Prüfprogramm

1. Liegt konzerninterne Leasing-Transaktion vor? Nahestehende Person (§ 1 II AStG)?
2. Verrechnungspreismethode: CUP, Kostenaufschlag, TNMM?
3. Dokumentation: GAufzV erfüllt? Aktuell und vollständig?
4. Zinsschranke (§ 4h EStG): Leasingrate enthält Zinsanteil; Grenze prüfen?
5. BEPS-Risiken: Substanz im Sitzland des LG? IP-Box-Regime?
6. Länderrisiken: DBA, Quellensteuer, Exit Tax?

## Typische Fallen

- Verrechnungspreise ohne Dokumentation → Schätzungsbefugnis des FA
- Captive Lessor ohne wirtschaftliche Substanz → BEPS-Angriff; Einkünfteverlagerung nicht anerkannt
- Zinsanteil in Leasingrate übersehen → § 4h EStG-Prüfung notwendig
- DBA-Quellensteuer nicht berücksichtigt → Effektive Rate höher als geplant

## Normen und Quellen

- § 1 AStG (Fremdvergleich): https://www.gesetze-im-internet.de/astg/__1.html
- § 90 III AO (Aufzeichnungspflichten): https://www.gesetze-im-internet.de/ao_1977/__90.html
- GAufzV (Aufzeichnungsverordnung Verrechnungspreise): https://www.gesetze-im-internet.de/aufzv/
- § 4h EStG (Zinsschranke): https://www.gesetze-im-internet.de/estg/__4h.html
- OECD Transfer Pricing Guidelines 2022: https://www.oecd.org
- BEPS-Aktionspläne 8-10: https://www.oecd.org

## Output-Formate

- **Verrechnungspreis-Dokumentation**: Vorlage für konzerninterne Leasingtransaktion
- **Methoden-Auswahl-Matrix**: CUP / Kostenaufschlag / TNMM – Eignung nach Transaktionsart
- **Zinsschranken-Memo**: Leasingrate, Zinsanteil, § 4h EStG-Prüfung
- **BEPS-Risikoeinschätzung**: Captive Lessor – Substanz, Verrechnungspreise, Quellensteuer

---

## Skill: `grenzueberschreitendes-leasing-unidroit-und-rechtswahl`

_Grenzüberschreitendes Leasing: UNIDROIT-Übereinkommen, Rechtswahl (Rom I-VO), internationales Mobiliar-Leasingrecht, Steuerstrukturierung und Valutafragen im Leasingrecht._

# Grenzüberschreitendes Leasing: UNIDROIT und Rechtswahl

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## UNIDROIT-Übereinkommen über internationales Finanzierungsleasing (Ottawa, 1988)

### Anwendungsbereich
- UNIDROIT-Übereinkommen: Gilt für Finanzierungsleasing, wenn LG und LN in verschiedenen Vertragsstaaten ansässig sind
- Deutschland ist kein Vertragsstaat → gilt nur, wenn Parteien Recht eines Vertragsstaats gewählt haben (z.B. England bis Brexit, Frankreich, USA/einzelne Staaten)
- Regelt: Rechte und Pflichten aus Leasingdreieck (Lieferant, LG, LN)

### Kernregeln UNIDROIT
- Art. 8: LN kann Ansprüche gegen Lieferant direkt geltend machen (wie §398 BGB)
- Art. 10: LN trägt Gefahrübergang wie Käufer
- Art. 13: Kündigung bei Nichterfüllung; Schadensersatz

## Rechtswahl nach Rom I-VO (EG 593/2008)

### Grundsatz: Freie Rechtswahl (Art. 3 Rom I-VO)
- Parteien können das anwendbare Recht frei wählen
- Empfehlung für internationale Leasingverträge: Wahl des Rechts eines Landes mit gut entwickeltem Leasingrecht (England/New York für Finanzierungs-Leasing; Deutschland für EU-Vertragspartner)

### Einschränkungen
- Verbraucher: Art. 6 Rom I-VO: Schutzrecht des Verbrauchers aus seinem Heimatland kann nicht abbedungen werden
- Zwingende Bestimmungen: Bestimmte Schutznormen (Verbraucherrecht, Arbeitsrecht) bleiben trotz Rechtswahl anwendbar (Art. 9 Rom I-VO)

### Anwendbares Recht ohne Rechtswahl (Art. 4 Rom I-VO)
- Leasingvertrag = Dienstleistungsvertrag → Recht des charakteristischen Leistungserbringers (LG) gilt
- LG in Deutschland → deutsches Recht anwendbar

## Internationaler Zahlungsverkehr

### Währungsrisiko
- Leasingrate in Fremdwährung (z.B. USD): LN trägt Währungsrisiko
- Absicherung: Devisentermingeschäfte, Währungsklausel im Vertrag

### Steuerstrukturierung: Cross-Border-Leasing

#### Typische Struktur
- LG in Niedrigsteuerland (z.B. Irland für Flugzeuge, Luxemburg für Finanzinstrumente)
- LN in Hochsteuerland: Leasingraten als Betriebsausgabe
- LG nutzt günstige Steuerregime; Steuervorteil geteilt

#### Risiken
- Doppelbesteuerungsabkommen (DBA): Quellensteuer auf Leasingraten?
- BEPS (Base Erosion and Profit Shifting, OECD): Anti-Gestaltungs-Regeln; Country-by-Country-Reporting
- § 8b KStG, §§ 1 ff. AStG: Verrechnungspreise bei Konzernleasing

### Zollrecht
- Grenzüberschreitende Verbringung von Leasingobjekten: Zollanmeldung erforderlich
- ATA-Carnet: Temporäre Einfuhr ohne Zoll (für Ausstellungen, vorübergehende Nutzung)
- Bei Finanzierungsleasing: Zoll auf Einfuhrwert bei Gestellung im Geltungsgebiet

## Insolvenz: Grenzüberschreitend

- EuInsVO (EG 2015/848): Hauptinsolvenzverfahren am Ort des COMI (Centre of Main Interests)
- Anerkennungspflicht in EU-Staaten
- Drittstaaten-Insolvenz: Anerkennung nach § 343 InsO

## Prüfprogramm

1. Wo sind LG und LN ansässig? UNIDROIT anwendbar?
2. Rechtswahlklausel: Welches Recht, warum?
3. Verbraucherleasing: Art. 6 Rom I-VO – Heimatrecht des Verbrauchers beachtet?
4. Währungsrisiko: Absicherung vereinbart?
5. Steuerstruktur: DBA-Quellensteuer? BEPS-Risiken?
6. Zollrecht: Einfuhr, temporäre Verbringung, ATA-Carnet?

## Typische Fallen

- Keine Rechtswahlklausel → Recht des LG-Landes gilt (möglicherweise unbekanntes Recht)
- Verbraucher im Ausland: Heimatrecht schützt ihn stärker → AGB des LG unwirksam
- Quellensteuer auf Leasingraten nicht eingeplant → Renditeminderung
- ATA-Carnet abgelaufen: Leasingobjekt im Ausland → Zollrisiko

## Normen und Quellen

- UNIDROIT Ottawa Convention 1988: https://www.unidroit.org
- Rom I-VO (EG 593/2008): https://eur-lex.europa.eu
- EuInsVO (EG 2015/848): https://eur-lex.europa.eu
- BEPS-Aktionsplan (OECD): https://www.oecd.org
- § 343 InsO (Ausländisches Insolvenzverfahren): https://www.gesetze-im-internet.de/inso/__343.html
- ATA-Carnet: https://www.ihk.de

## Output-Formate

- **Rechtswahl-Klausel-Muster**: Für internationale Leasingverträge
- **DBA-Quellensteuer-Matrix**: Ländervergleich für typische Leasingstruktur
- **Zoll-Checkliste**: Grenzüberschreitende Verbringung von Leasingobjekten
- **BEPS-Risikobewertung**: Konzernleasing und Verrechnungspreise

---

## Skill: `diebstahl-totalschaden`

_Diebstahl und Totalschaden im Leasing: Gefahrtragung, Ratenpflicht nach Untergang, Versicherungsabwicklung, Anzeigeobliegenheiten und Sorgfaltspflichten im Leasingrecht._

# Diebstahl und Totalschaden: Gefahrtragung im Leasingrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Gefahrtragung: Wer trägt den Untergang?

### Finanzierungsleasing (Regelfall)
- BGH-Linie zur Gefahrabwälzung bei Leasingverträgen live prüfen; als frei prüfbarer Anker kommt BGH, Urteil vom 15.07.1998 - VIII ZR 348/97 in Betracht
- Auch zufälliger Untergang: LN haftet
- Ausnahme: LG hat durch Pflichtverletzung zum Untergang beigetragen

### Operating-Lease
- LG trägt Untergangsrisiko (Verwertungsrisiko beim LG)
- AGB-Klausel, die Untergang auf LN überträgt: nach § 307 BGB zu prüfen

## Ratenpflicht nach Untergang

### Grundsatz
- Finanzierungsleasing: Leasingraten laufen trotz Untergang weiter
- Ratio: LN hat für die gesamte Amortisation einzustehen
- § 275 BGB (Unmöglichkeit): Gilt nicht für Geldschulden des LN

### Ausnahme: Versicherungsleistung tilgt Forderung
- Wenn Versicherungsleistung die Restschuld übersteigt: LG hat keinen Anspruch mehr
- Wenn Versicherungsleistung < Restschuld: LN zahlt Differenz

## Diebstahl: Besonderheiten

### Sorgfaltspflichten des LN
- LN ist zur sorgfältigen Aufbewahrung verpflichtet (§ 241 II BGB)
- Verschlossenes Fahrzeug, Diebstahlschutz (Lenkradschloss, Immobilizer)
- Schlüssel gesondert aufbewahren

### Obliegenheiten nach Diebstahl
- Unverzügliche Diebstahlsanzeige bei Polizei (Beweis für Versicherung)
- Meldung an Versicherung (Obliegenheit nach VVG)
- Meldung an LG (Vertragspflicht)

### Versicherungsabwicklung bei Diebstahl
- Kaskoversicherung (Teilkasko): Diebstahl gedeckt
- Wartezeit: Versicherung zahlt oft erst nach 6 Wochen (Fahrzeug könnte wiedergefunden werden)
- Wiederfindung: LN muss Fahrzeug wieder übernehmen (Versicherung zahlt nicht)

## Totalschaden: Vorgehensweise

### Unfallschaden = Totalschaden
- Reparaturkosten übersteigen Wiederbeschaffungswert × 130 %: Technischer Totalschaden
- Wirtschaftlicher Totalschaden: Reparaturkosten > Restwert

### Gutachterprozess
- Versicherung beauftragt Gutachter (DEKRA, TÜV, DA-Direkt)
- LN kann Gegengutachten beantragen
- Streit über Wiederbeschaffungswert: Häufiger Konflikt

### Fordforderung des LG nach Totalschaden
- LG erhält Versicherungsleistung (Wiederbeschaffungswert oder Restwert)
- Formel: LG-Forderung - Versicherungsleistung = LN-Differenzzahlung
- GAP-Versicherung: Deckt Differenz

## Verschuldensmaßstab: Wann haftet LN über Versicherung hinaus?

- Grobe Fahrlässigkeit: Versicherung kann Leistung kürzen (VVG § 81 II)
- Vorsatz: Versicherung zahlt gar nicht (VVG § 81 I)
- Wenn LN vorsätzlich Fahrzeug beschädigt: LN haftet persönlich; kein Versicherungsschutz

## Prüfprogramm

1. Finanzierungsleasing oder Operating-Lease? Gefahrtragung klar?
2. Versicherungsklausel: Vollkasko, Teilkasko, GAP vorhanden?
3. Obliegenheiten erfüllt: Polizei, Versicherung, LG unverzüglich informiert?
4. Gutachten: Wer hat beauftragt? LN Gegengutachter?
5. Versicherungsleistung vs. Restschuld: Differenz berechnet?
6. Grobe Fahrlässigkeit oder Vorsatz? Leistungskürzung durch Versicherung?

## Typische Fallen

- Diebstahlsmeldung zu spät → Versicherung kürzt Leistung (Obliegenheitsverletzung)
- GAP-Versicherung fehlt → LN schuldet Differenz aus eigener Tasche
- LG erhält keine Versicherungsleistung (nicht als Begünstigter eingetragen) → Abrechnungsproblem
- Grobe Fahrlässigkeit (z.B. Schlüssel im Fahrzeug gelassen) → Versicherung kürzt auf 50 %

## Normen und Quellen

- BGH VIII ZR 71/93: https://www.bgh.de
- § 241 II BGB (Sorgfaltspflicht): https://dejure.org/gesetze/BGB/241.html
- VVG § 81 (Obliegenheiten, Verschulden): https://www.gesetze-im-internet.de/vvg_2008/__81.html
- VVG §§ 43 ff.: https://www.gesetze-im-internet.de/vvg_2008/__43.html
- § 307 BGB: https://dejure.org/gesetze/BGB/307.html
- openjur.de Leasingdiebstahl-Urteile: https://openjur.de

## Output-Formate

- **Diebstahl-Sofortprotokoll**: Polizei, Versicherung, LG – Fristen und Schritte
- **Totalschaden-Abrechnung**: Formel mit GAP-Versicherung
- **Obliegenheits-Checkliste**: Was muss LN nach Schaden tun?
- **Gegengutachten-Antrag**: Muster für Widerspruch gegen Versicherungsgutachten

---

## Skill: `kommunalleasing-vergaberecht-und-haushaltsrecht`

_Kommunalleasing: Vergabepflicht, Wirtschaftlichkeitsnachweis, kreditähnliche Rechtsgeschäfte, Genehmigungspflicht und historisches Cross-Border-Leasing im Leasingrecht._

# Kommunalleasing: Vergaberecht und Haushaltsrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

- Gemeindeordnungen der Länder (GO NRW, GemO BW, GO BayGO etc.): Haushaltsgrundsätze
- §§ 97 ff. GWB: Vergaberecht
- VgV, UVgO: Vergabeordnungen
- §§ 7, 34 BHO / entsprechende LHO: Wirtschaftlichkeit und Sparsamkeit
- KommWirtschaftlichkeitsnachweis-Erlasse der Bundesländer

## Haushaltsrechtliche Schranken

### Wirtschaftlichkeit und Sparsamkeit (§ 7 BHO / LHO-Äquivalente)
Kommunen müssen nachweisen, dass Leasing wirtschaftlicher ist als Kauf:
- Kapitalwertvergleich: Gesamtkosten Leasing (Raten + NK) vs. Kauf (Finanzierungskosten + Abschreibung + Unterhalt)
- Zeitraum: Gleicher Betrachtungszeitraum
- Zinssatz: Marktüblich oder kommunaler Kreditmarkt
- Dokumentation: Schriftliche Wirtschaftlichkeitsberechnung

### Kreditähnliche Rechtsgeschäfte
Viele Gemeindeordnungen definieren Leasingverträge als kreditähnliche Rechtsgeschäfte (z.B. § 86 GO NRW).

Folgen:
- Genehmigungspflicht durch Rechtsaufsichtsbehörde (Landratsamt, Bezirksregierung)
- Einbeziehung in Haushaltssatzung und mittelfristige Finanzplanung
- Gemeinderatsbeschluss ab bestimmter Wertgrenze (z.B. 50.000 €)

### Sale-and-Lease-Back für Kommunen
- Besonders kritisch: Kommunen dürfen Vermögen nicht beliebig veräußern
- SLB kann als versteckter Kredit qualifiziert werden → Genehmigungspflicht
- Rechnungshöfe haben SLB-Konstruktionen wiederholt beanstandet

## Vergaberecht

### Schwellenwerte (§ 106 GWB)
- Liefer- und Dienstleistungsaufträge (inkl. Leasing): EU-Schwellenwert aktuell 215.000 € netto (Obere Kommunen), 140.000 € (Zentrale Regierungsstellen)
- Oberhalb: EU-weites Vergabeverfahren (VgV)
- Unterhalb: Nationale Verfahren (UVgO), beschränkte Ausschreibung

### Leasingvertrag als Liefer- oder Dienstleistungsauftrag?
- EuGH: Leasingvertrag überwiegend als Liefervertrag zu qualifizieren
- CPV-Codes: Leasing, Vermietung ohne Fahrer (CPV 71550000 ff.)

### Full-Service-Leasing: Gemischter Auftrag
- Wenn Leasing + Wartung + Service gebearbeitet: Gemischter Auftrag (§ 110 GWB)
- Hauptleistung bestimmt anzuwendendes Vergaberegime

### Produktneutralität (§ 31 VgV)
- Ausschreibung produktneutral (kein bestimmter Hersteller/Marke)
- Technische Anforderungen beschreiben, nicht Produkt benennen

## Cross-Border-Leasing (historisch)

In den 1990er–2000er Jahren haben viele Kommunen US-amerikanische Cross-Border-Leasing-Konstruktionen abgeschlossen (Sale-and-Lease-Back an US-Trust für US-Steuervorteile). Nach IRS-Reform (2004, § 470 IRC) brachen diese Konstruktionen zusammen. Lehren:
- Komplexe Steuerkonstruktionen mit Auslandsbezug haben erhebliches Risiko
- Kommunen zahlten erhebliche Abstandssummen
- Politischer und haushaltsrechtlicher Schaden langanhaltend

## Prüfprogramm

1. Ist Auftraggeber öffentlicher Auftraggeber (§ 99 GWB)?
2. Schwellenwert über EU-Grenze → EU-Vergabe erforderlich?
3. Wirtschaftlichkeitsnachweis nach § 7 BHO/LHO erstellt und dokumentiert?
4. Genehmigungspflicht nach GO? Antrag gestellt, Genehmigung erteilt?
5. Gemeinderatsbeschluss erforderlich und eingeholt?
6. Vergabeverfahren dokumentiert (Vergabevermerk § 8 VgV)?

## Typische Fallen

- Fehlender Wirtschaftlichkeitsnachweis → Rechtsaufsicht beanstandet; Vertrag ggf. schwebend unwirksam
- Schwellenwert übersehen: Mehrere Einzelverträge kumuliert → europarechtswidrig ohne EU-Ausschreibung
- Genehmigung fehlt → kreditähnliches Rechtsgeschäft unwirksam
- Politischer Beschluss fehlt → Bürgermeister handelt ohne Kompetenz

## Normen und Quellen

- §§ 97, 99, 106 GWB: https://www.gesetze-im-internet.de/gwb/__97.html
- VgV § 31 (Produktneutralität): https://www.gesetze-im-internet.de/vgv_2016/__31.html
- § 7 BHO (Wirtschaftlichkeit): https://www.gesetze-im-internet.de/bho/__7.html
- GO NRW § 86 (kreditähnliche Rechtsgeschäfte): https://www.gesetze-im-internet.de
- UVgO: https://www.gesetze-im-internet.de
- openjur.de Kommunalleasing: https://openjur.de

## Output-Formate

- **Wirtschaftlichkeitsvergleich-Vorlage**: Leasing vs. Kauf (Kapitalwertmethode)
- **Vergabe-Checkliste**: EU-Schwellenwert, CPV-Codes, Vergabevermerk
- **Genehmigungsantrag-Muster**: An Rechtsaufsichtsbehörde
- **Cross-Border-Leasing-Analyse**: Bestandsaufnahme historischer Risiken

---

## Skill: `start-up-equipment-leasing-covenants`

_Start-up Equipment-Leasing: Kreditwürdigkeitsprüfung, Financial Covenants, persönliche Bürgschaft, Anlaufrisikoklauseln und typische Verhandlungspunkte im Leasingrecht._

# Start-up Equipment-Leasing: Covenants und Risikoabsicherung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Bonitätsprüfung bei Start-ups

### Herausforderungen
- Keine Unternehmenshistorie → keine historischen Finanzberichte
- Negativer oder kein Cashflow → klassische Kreditwürdigkeitsprüfung scheitert
- Hohe Unsicherheit → LG kalkuliert hohes Ausfallrisiko ein

### Unterlagen, die LG verlangt
- Businessplan mit Finanzplanung (mind. 3 Jahre)
- Gesellschaftsvertrag und Handelsregisterauszug
- Gesellschafterstruktur und Gesellschafter-Bonität
- Ggf. Investoren-Letters (VC-Commitment)
- Kontoauszüge der letzten 3 Monate

## Sicherungsmechanismen des LG

### 1. Anzahlung / Sonderzahlung
- LG verlangt erhöhte Anzahlung (z.B. 3 Monatsraten voraus)
- Reduziert das Ausfallrisiko in der kritischen Anlaufphase

### 2. Bürgschaft der Gesellschafter/Gründer
- Persönliche Bürgschaft (§§ 765 ff. BGB): Gründer bürgen für Leasingverpflichtungen
- Selbstschuldnerische Bürgschaft (§ 773 BGB): LG kann sofort gegen Bürgen vorgehen
- AGB-Wirksamkeit: Bürgschaft in AGB? Gegenüber Verbrauchern/Gründern strenge Anforderungen

### 3. Financial Covenants
Typische Covenants:
- Mindesteigenkapital (z.B. Eigenkapital > 0 oder > definierter Betrag)
- Maximalverschuldung (Debt/Equity Ratio)
- Mindest-Cashflow (EBITDA > X)
- Jahresabschluss fristgerecht vorzulegen

Bei Verletzung: Kündigungsrecht des LG oder Sonderkündigungsrecht.

### 4. Abtretung von Forderungen / Rechten
- Start-up tritt Kundenverträge oder Fördergelder als Sicherheit ab
- § 398 BGB: Abtretung möglich, wenn Forderungen bestimmt oder bestimmbar

### 5. Verpfändung von Gesellschaftsanteilen
- GmbH-Anteile können verpfändet werden (§ 1274 BGB i.V.m. § 15 IV GmbHG: notarielle Form)
- LG erhält Stimmrechte bei Pfandfall (ggf. in Pfandvertrag)

## Anlaufrisikoklauseln

### Verlängerter Rücktritt
- Wenn Start-up erste Kundenzahlung nicht erhält: LG kann von Vertrag zurücktreten
- Selten; eher: Anpassungsklausel

### Change of Control
- Wenn Gründer das Unternehmen verlassen oder verkaufen: LG hat Sonderkündigungsrecht oder Nachbesicherungspflicht tritt ein

### Reporting-Pflichten
- Quartalsberichte (P&L, Cashflow)
- Sofortige Mitteilung von Covenant-Verletzungen
- Benachrichtigung bei wesentlichen Änderungen (Geschäftsführer, Investoren, Haftungsumfang)

## Verhandlungspositionen des Start-ups

### Gründer-Bürgschaft begrenzen
- Höchstbetrag vereinbaren
- Akzessorietät erhalten (Bürgschaft erlischt mit Hauptforderung)
- Nachhaftung ausschließen: Bürgschaft endet mit Vertragsbeendigung

### Covenants anpassen
- An realistische Unternehmensplanung (nicht an Erwachsenen-Unternehmen-Standards)
- Cure Period: Zeit zur Heilung einer Covenant-Verletzung

### Sicherheitenrückgabe
- Sicherheiten werden freigegeben wenn Track Record aufgebaut (z.B. nach 12 Monaten ohne Rückstand)

## Prüfprogramm

1. Bonitätslage: Businessplan, Finanzplanung, Gesellschafterstruktur?
2. Sicherheiten: Anzahlung, Bürgschaft, Covenants, Forderungsabtretung?
3. Bürgschaft: Selbstschuldnerisch, Höchstbetrag, Privatperson?
4. Covenants: Realistisch für Start-up? Cure Period?
5. Change of Control: Klausel vorhanden? Wann ausgelöst?
6. Verhandlung: Sicherheitenrückgabe vereinbart?

## Typische Fallen

- Bürgschaft ohne Höchstbetrag → unbegrenzte persönliche Haftung der Gründer
- Covenants zu streng → Verletzung bei erster Schwankung → sofortige Kündigung
- Keine Cure Period → sofortige Kündigung bei technischer Covenant-Verletzung
- Forderungsabtretung zu weit gefasst → Start-up kann eigene Forderungen nicht mehr einziehen

## Normen und Quellen

- §§ 765–778 BGB (Bürgschaft): https://dejure.org/gesetze/BGB/765.html
- § 773 BGB (selbstschuldnerische Bürgschaft): https://dejure.org/gesetze/BGB/773.html
- § 398 BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- § 15 IV GmbHG (Verpfändung GmbH-Anteile): https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 307 BGB (AGB-Inhaltskontrolle Bürgschaft): https://dejure.org/gesetze/BGB/307.html
- BGH IX ZR 48/15 (Bürgschaft AGB): https://www.bgh.de

## Output-Formate

- **Covenant-Template**: Financial Covenants für Start-up-Leasingvertrag
- **Bürgschafts-Vorlage**: Selbstschuldnerische Bürgschaft mit Höchstbetrag
- **Reporting-Pflichten-Anlage**: Quartalsbericht-Format
- **Verhandlungsmatrix**: LG-Anforderungen vs. Start-up-Gegenvorschläge

---

## Skill: `datenschutz-telematik-esg-leasing-start`

_Datenschutz und Telematik im Fahrzeugleasing: DSGVO, Verarbeitungszwecke, Beschäftigtendatenschutz § 26 BDSG, Nutzungsprofile und Betriebsvereinbarung im Leasingrecht._

# Datenschutz und Telematik im Fahrzeugleasing

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## DSGVO-Grundlagen

### Personenbezogene Daten
- GPS-Position + Uhrzeit + Fahrzeug-ID = personenbezogene Daten (identifizierbar über Fahrer)
- Fahrstildaten (Beschleunigung, Bremsung, Tempo): Personenbezug bei fester Fahrerzuordnung
- Telematik: Verarbeitung nach Art. 6 DSGVO erlaubnispflichtig

### Erlaubnistatbestände
- Art. 6 I b DSGVO: Vertragserfüllung (Flottenmanagement, Versicherungskalkulation)
- Art. 6 I f DSGVO: Berechtigte Interessen (Diebstahlschutz, Wartungsplanung)
- Art. 6 I a DSGVO: Einwilligung (für weitergehende Auswertung)

### Art. 6 I f: Interessenabwägung
Berechtigtes Interesse vs. Grundrechte des Betroffenen (Fahrer):
- Flottenmanagement: Berechtigtes Interesse bejaht
- Leistungsüberwachung einzelner Fahrer: Problematisch ohne BV oder Einwilligung
- Standortdaten in Echtzeit permanent: Sehr eingriffsintensiv; besonders zu rechtfertigen

## Beschäftigtendatenschutz (§ 26 BDSG)

### Anwendungsbereich
§ 26 BDSG gilt für die Datenverarbeitung im Beschäftigungsverhältnis.

- Firmenwagen mit Telematik: Fahrer = Beschäftigter → § 26 BDSG
- Zweck: Überwachung des Arbeitsverhältnisses erlaubt nur nach Verhältnismäßigkeitsprüfung

### Zulässige Verarbeitungszwecke (§ 26 I BDSG)
- Begründung, Durchführung und Beendigung des Beschäftigungsverhältnisses
- Straftaten im Beschäftigungsverhältnis aufdecken (§ 26 I 2 BDSG): Hohe Hürden (konkreter Anfangsverdacht)

### Betriebsvereinbarung (§ 26 IV BDSG)
- Kollektivrechtliche Regelung möglich: Betriebsrat + Arbeitgeber schließen BV über Telematik
- BV muss DSGVO-Anforderungen erfüllen (Art. 88 DSGVO)
- Inhalt: Zwecke, Datenkategorien, Auskunftsrechte, Löschfristen

## Telematik-Klauseln im Leasingvertrag

### LG-seitig
- LG darf Telematikdaten für: Fahrzeugdiagnose, Wartungsplanung, Diebstahlschutz
- Keine Übermittlung an Dritte ohne Rechtsgrundlage (Art. 28 DSGVO: AVV wenn Subunternehmer)

### LN-seitig (Flottenleasing)
- LN verarbeitet Daten der Fahrer für eigenes Flottenmanagement
- LN ist Verantwortlicher (Art. 4 Nr. 7 DSGVO) gegenüber Fahrern
- Informationspflicht gegenüber Fahrern (Art. 13 DSGVO)

## Auftragsverarbeitung (Art. 28 DSGVO)

Wenn LG oder Telematik-Dienstleister Daten im Auftrag des LN verarbeitet:
- Auftragsverarbeitungsvertrag (AVV) erforderlich
- Inhalt: Zweck, Kategorien, technisch-organisatorische Maßnahmen, Löschung

## Prüfprogramm

1. Welche Telematikdaten werden erhoben? GPS, Fahrstil, Diagnose?
2. Rechtsgrundlage für Verarbeitung: Art. 6 I b/f/a DSGVO?
3. Fahrer = Beschäftigter? § 26 BDSG und Betriebsvereinbarung?
4. AVV mit LG/Telematik-Dienstleister vorhanden?
5. Informationspflicht gegenüber Fahrern (Art. 13 DSGVO) erfüllt?
6. Löschkonzept: Telematikdaten nach welcher Frist gelöscht?

## Typische Fallen

- Telematik ohne Information der Fahrer → Verstoß Art. 13 DSGVO; Bußgeld
- BV fehlt → Betriebsrat kann Unterlassung der Telematikauswertung verlangen
- Leistungsüberwachung über Telematik ohne Rechtsgrundlage → Art. 83 IV DSGVO: bis 10 Mio. € Bußgeld
- AVV mit Telematik-Dienstleister fehlt → Bußgeldrisiko Art. 28 DSGVO

## Normen und Quellen

- DSGVO Art. 6, 13, 28: https://eur-lex.europa.eu
- § 26 BDSG (Beschäftigtendatenschutz): https://www.gesetze-im-internet.de/bdsg_2018/__26.html
- Art. 88 DSGVO (Beschäftigtendaten): https://eur-lex.europa.eu
- DSK (Datenschutzkonferenz) Kurzpapier Fahrzeugdaten: https://www.datenschutzkonferenz-online.de
- BAG 27.07.2017 – 2 AZR 681/16 (Überwachung, Beweisverwertungsverbot): https://openjur.de

## Output-Formate

- **Datenschutzfolgenabschätzung (DSFA)**: Telematik im Flottenleasing
- **Betriebsvereinbarungs-Muster**: Telematik-Nutzung Fahrzeuge
- **Informationsschreiben**: Art. 13 DSGVO für Fahrer
- **AVV-Klausel-Muster**: LN mit Telematik-Dienstleister

---

## Skill: `esg-leasing-taxonomie-und-green-lease`

_ESG und Green Lease: EU-Taxonomie, SFDR, Nachhaltigkeitsklauseln, CO2-Reporting, Green-Finance-Strukturen und ESG-Anforderungen für Leasingportfolios im Leasingrecht._

# ESG und Green Lease: Taxonomie und Nachhaltigkeit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## EU-Taxonomie-Verordnung (EU 2020/852)

### Grundkonzept
Die Taxonomie-VO definiert, welche wirtschaftlichen Aktivitäten als ökologisch nachhaltig gelten:
- Sechs Umweltziele (Klimaschutz, Klimaanpassung, Wasser, Kreislaufwirtschaft, Biodiversität, Schadstoffvermeidung)
- „Do No Significant Harm" (DNSH): Keine erhebliche Beeinträchtigung anderer Ziele
- Mindest-Sozialstandards (OECD, UN-Leitprinzipien)

### Leasing und Taxonomie
- Wenn LG Finanzprodukte anbietet oder investiert: Offenlegungspflicht (SFDR)
- Leasingobjekte können taxonomiefähig sein: PV-Anlagen, E-Fahrzeuge, effiziente Gebäude
- LG muss anteiligen Taxonomie-Anteil seines Portfolios offenlegen (Art. 8 Taxonomie-VO für Finanzunternehmen)

## SFDR (Sustainable Finance Disclosure Regulation, EU 2019/2088)

### Anwendungsbereich
- Finanzmarktteilnehmer und Finanzberater
- Leasinggesellschaften: Sofern Finanzdienstleistungsinstitut (KWG) → SFDR-Scope prüfen

### Offenlegungspflichten
- Art. 3 SFDR: Grundlegende ESG-Informationen auf Webseite
- Art. 7 SFDR: Adverse Sustainability Impacts (PAI) – Negative Nachhaltigkeitsauswirkungen
- Art. 8/9 SFDR: Produktklassifizierung (hellgrün/dunkelgrün)

## Green Lease: Vertragsklauseln

### Typische Green-Lease-Klauseln

**1. CO2-Monitoring-Klausel**
LN ist verpflichtet, Energieverbrauch und CO2-Ausstoß des Leasingobjekts jährlich zu berichten. LG kann Daten für ESG-Reporting verwenden.

**2. Instandhaltungsstandard**
LN hält das Objekt auf einem energetischen Standard X (z.B. Kfz: mind. Euro 6; Gebäude: Energieklasse A).

**3. Upgrade-Klausel**
LG bietet LN bei technischen Verbesserungen (effizientere Maschine, E-Fahrzeug) ein Upgrade-Angebot an.

**4. ESG-Kündigung**
Wenn LN dokumentierte ESG-Verstöße begeht (z.B. unrechtmäßige Entsorgung), kann LG außerordentlich kündigen.

**5. Green-Bond-Eligible**
Wenn LG Green Bonds emittiert: Leasingobjekte müssen Taxonomie-Kriterien erfüllen; LN kooperiert bei Nachweis-Erbringung.

## CO2-Flottenregulierung

### Kfz-Flottenleasing und CO2-Ziele
- EU-VO 2019/631: CO2-Flottengrenzwerte für Kfz-Hersteller
- PKW: 95 g CO2/km (2021), 0 g (Verbrenner-Neuzulassungsverbot ab 2035)
- Auswirkung auf Leasingportfolios: E-Fahrzeuge werden Pflicht; Restwert konventioneller Fahrzeuge sinkt

## Soziale und Governance-Anforderungen (S und G)

- Lieferkettensorgfaltspflichtengesetz (LkSG, ab 2023): Unternehmen mit > 1.000 MA
- Wenn Leasingobjekte aus Lieferketten mit Menschenrechtsverstößen: LkSG-Pflicht des LN
- Governance: Transparenz des LG in ESG-Berichterstattung (nfRB = nichtfinanzielle Berichterstattung, CSR-RUG)

## Prüfprogramm

1. Taxonomie-Konformität: Ist das Leasingobjekt taxonomiefähig? DNSH-Prüfung?
2. SFDR: Ist LG als Finanzmarktteilnehmer einzustufen?
3. Green-Lease-Klauseln: CO2-Monitoring, Upgrade, ESG-Kündigung vereinbart?
4. CO2-Flottenregulierung: E-Fahrzeuge im Portfolio? Restwert-Entwicklung?
5. LkSG: LN oder LG betroffen? Lieferkettencompliance?
6. ESG-Reporting: Welche Kennzahlen müssen ausgewiesen werden?

## Typische Fallen

- Taxonomie-Fähigkeit ohne DNSH-Prüfung deklariert → Greenwashing-Vorwurf
- SFDR-Offenlegungen fehlen → BaFin-Rüge
- Restwert konventioneller Fahrzeuge im Portfolio sinkt durch Verbrennerverbot schneller als kalkuliert
- Fehlende CO2-Daten vom LN → ESG-Reporting lückenhaft

## Normen und Quellen

- EU-Taxonomie-VO 2020/852: https://eur-lex.europa.eu
- SFDR 2019/2088: https://eur-lex.europa.eu
- EU-VO 2019/631 (CO2-Flottengrenzwerte): https://eur-lex.europa.eu
- LkSG (Lieferkettensorgfaltspflichtengesetz): https://www.gesetze-im-internet.de/lksg/
- CSR-RUG (nichtfinanzielle Berichterstattung): https://www.gesetze-im-internet.de/hgb/__289b.html

## Output-Formate

- **Green-Lease-Klauseln-Muster**: Fertige Textbausteine für Leasingvertrag
- **Taxonomie-Check**: Leasingobjekt taxonomiefähig ja/nein mit Begründung
- **CO2-Reporting-Vorlage**: Jährliches Monitoring-Formular für LN
- **SFDR-Disclosure-Muster**: Art. 3/7 SFDR für Leasinggesellschaft

---

## Skill: `lieferant-leasinggeber-leasingnehmer-dreiecksverhaeltn`

_Leasingdreieck: Rechtsverhältnisse Lieferant/Leasinggeber/Leasingnehmer, Abtretungskonstruktion, Kollisionsprobleme und Insolvenz eines Beteiligten im Leasingrecht._

# Das Leasingdreieck: Lieferant, Leasinggeber, Leasingnehmer

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtsverhältnisse im Überblick

### 1. Kaufvertrag: Lieferant → Leasinggeber (§ 433 BGB)
- LG kauft das Objekt vom Lieferant
- LG wird zivilrechtlicher Eigentümer
- Direktlieferung an LN möglich (§ 447 BGB analog: Gefahrübergang bei Übergabe an LN)
- Gewährleistungsansprüche entstehen beim LG

### 2. Leasingvertrag: Leasinggeber → Leasingnehmer (§§ 535 ff. BGB analog)
- LG überlässt LN die Nutzung gegen Leasingraten
- LG tritt Gewährleistungsansprüche gegen Lieferant an LN ab (§ 398 BGB)
- LN trägt Gefahrtragung (Finanzierungsleasing)
- LN haftet für Raten auch bei Schlechtleistung des Lieferanten

### 3. Abgeleitetes Verhältnis: Leasingnehmer → Lieferant
- Keine direkte vertragliche Verbindung
- LN hat nur abgetretene Ansprüche aus Kaufvertrag LG–Lieferant
- Klage im eigenen Namen kraft Abtretung (§ 398 BGB)

## Kollisionsprobleme

### Gefahrtragung bei Direktlieferung
- LG kauft, LN nimmt entgegen
- § 447 BGB: Gefahrübergang bei Übergabe an Transportperson, wenn LG als Versendungskäufer auftritt
- Im Leasingvertrag muss klargestellt sein, dass Gefahrübergang mit Übergabe an LN erfolgt

### Mängelrechte: Wer kann was?
| Anspruchsinhaber | Anspruch | Gegen wen |
|---|---|---|
| LG (vor Abtretung) | Nacherfüllung, Rücktritt, Minderung | Lieferant |
| LN (nach Abtretung) | Nacherfüllung, Schadensersatz | Lieferant |
| LN | Schadensersatz wegen Mangelfolge | Lieferant (Deliktsrecht §§ 823 ff.) |
| LN gegen LG | Grundsätzlich ausgeschlossen | n/a |

### Abtretung: Wirksamkeitserfordernisse
- Bestimmtheitsgrundsatz: Abtretungsklausel muss Ansprüche hinreichend bestimmt bezeichnen
- Zeitpunkt: Abtretung soll mit Leasingvertragsschluss oder Abnahme erfolgen
- Abtretungsverbot im Kaufvertrag (§ 399 BGB): Lieferant kann Abtretbarkeit ausschließen → LN bleibt ohne Durchgriff

## Insolvenz: Dreiecksfolgen

### Insolvenz des Lieferanten
- LG verliert Gewährleistungsansprüche praktisch (Masse deckt nicht)
- LN hat abgetretene Ansprüche → ebenfalls wertlos
- **Folge**: LN bleibt auf Leasingraten sitzen ohne Mängelabhilfe
- **BGH**: LG haftet subsidiär, wenn abgetretene Ansprüche nicht realisierbar (§ 307 BGB-Wertung)

### Insolvenz des Leasinggebers
- §§ 108, 109 InsO: Leasingvertrag läuft grundsätzlich fort
- LN hat Nutzungsrecht; kann Objekt behalten, solange Raten gezahlt werden
- Aussonderungsrecht von LG-Gläubigern: Wenn LG Objekt sicherungsübereignet hat, kann Sicherungsnehmer herausverlangen; LN hat ggf. Besitzrecht

### Insolvenz des Leasingnehmers
- §§ 108, 109 InsO: Insolvenzverwalter entscheidet über Fortführung
- § 47 InsO: LG kann aussondern (Eigentumsrecht)
- LG muss Antrag stellen; Verwalter hat Wahlrecht bis zur Entscheidung
- Offene Raten vor Insolvenzeröffnung = Insolvenzforderung; Raten danach = Masseverbindlichkeit

## Prüfprogramm

1. Kaufvertrag LG–Lieferant vorhanden und wirksam?
2. Abtretungsklausel vorhanden, wirksam, keine Abtretungsverbote (§ 399 BGB)?
3. Gefahrübergang: Wann und an wen?
4. Insolvenz eines Beteiligten: Welche Ansprüche laufen ins Leere?
5. Subsidiäre Haftung des LG bei wertloser Abtretung?
6. Prozessuale Vorbereitung: LN klagt gegen Lieferant – Klagebefugnis nachgewiesen?

## Typische Fallen

- Abtretungsverbot im Kaufvertrag zwischen LG und Lieferant übersehen → LN ohne Rechte
- Direktlieferung ohne Gefahrübergangsregelung → unklar wer haftet bei Transportschaden
- Insolvenz Lieferant: LN zahlt weiter Raten für fehlerhafte Ware ohne Abhilfemöglichkeit
- Kaufvertrag nicht aufbewahrt: LN kann Klagebefugnis nicht beweisen

## Normen und Quellen

- § 433 BGB: https://dejure.org/gesetze/BGB/433.html
- § 398 BGB: https://dejure.org/gesetze/BGB/398.html
- § 399 BGB (Abtretungsverbot): https://dejure.org/gesetze/BGB/399.html
- § 447 BGB (Versendungskauf): https://dejure.org/gesetze/BGB/447.html
- §§ 108, 109 InsO: https://www.gesetze-im-internet.de/inso/__108.html
- § 47 InsO (Aussonderung): https://www.gesetze-im-internet.de/inso/__47.html
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12: https://www.bgh.de

## Output-Formate

- **Dreiecks-Diagramm**: Vertragsfluss, Abtretung, Gefahrübergang
- **Insolvenz-Matrix**: Wer fällt aus – welche Ansprüche, welche Rechte
- **Klagebefugnis-Checkliste**: LN gegen Lieferant aus abgetretenem Recht

---

## Skill: `flugzeugleasing-register-schiffsleasing`

_Flugzeug-Leasing: Luftfahrtregister, Kapstadt-Übereinkommen, Internationales Interesse, Wartung nach EASA, Rückgabe-Condition und Leasingstruktur im Leasingrecht._

# Flugzeug-Leasing: Register, Pfand und Wartung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

- **Cape Town Convention (Kapstadt-Übereinkommen, 2001)**: Internationales Übereinkommen über mobile Ausrüstungen; Protokoll Luftfahrzeuge (2001); Deutschland ratifiziert 2015
- **LuftVG, LuftVZO**: Deutsches Luftfahrzeugrecht; Eintragungspflicht im Luftfahrzeugregister
- **EASA-VO (EG) 2018/1139**: Lufttüchtigkeit und Wartung
- **ICAO Annex 7**: Nationalitätskennzeichen; Eigentumsnachweis
- §§ 101 ff. LuftVG: Luftfahrzeugpfandrecht

## Luftfahrzeugregister

### Nationales Register (LBA / Luftfahrt-Bundesamt)
- Eintragung der Luftfahrzeuge nach Nationalitätskennzeichen (§ 3 LuftVZO)
- Eintragung des Eigentümers (oder Leasinggebers) und Betreibers (Leasingnehmer/Airline)
- Keine automatische Sicherungsrechts-Transparenz

### Kapstadt-Register: Internationales Interesse
- Kapstadt-Protokoll schafft internationales Interesse an Luftfahrzeugen
- Registrierung im International Registry (IR, Dublin): Priorität nach Registrierungsdatum
- Schutz des registrierten Gläubigers (LG / Refinanzierer) vor späteren Rechten Dritter

### Priorität der Sicherungsrechte
- First registered, first protected: Kapstadt-Prinzip
- LG muss „prospective international interest" anmelden, bevor LN das Luftfahrzeug erhält
- Ohne Registrierung: Kein Schutz nach Kapstadt-Übereinkommen

## Wartung nach EASA

### Kontinuierliche Lufttüchtigkeit (CAMO)
- EASA Part-M/Part-CAMO: Halter und/oder Betreiber müssen CAMO-Organisation aufbauen
- CAMO verantwortlich für: Wartungsplanung, AD/SB-Compliance, Gewichts- und Schwerpunktdokumentation
- Im Leasingvertrag: Wer ist CAMO-Verantwortlicher? LN als Betreiber

### Maintenance Reserve (MR)
- Leasingverträge enthalten oft Maintenance-Reserve-Klauseln: LN zahlt monatlich MR in Treuhandkonto
- MR deckt: Triebwerksüberholung, Fahrwerk-Overhaul, C-Check
- Bei Vertragsende: MR wird für Reparaturen verwendet; verbleibend zurück an LN

### Return Conditions (Rückgabebedingungen)
Typische Rückgabezustand-Anforderungen:
- Mindest-Triebwerkszeit bis nächstem Shop-Visit (z.B. 4.000 Flight Hours)
- Mindest-Airframe-Zeit
- No open MEL items (Minimum Equipment List)
- Vollständige technische Dokumentation (Log Books, AD Status)
- Exterieur: Keine Dellen/Risse über bestimmten Toleranzen

### Lease Return Compensation
- Wenn LN Rückgabebedingungen nicht erfüllt: Compensation Payment (vertraglich pauschaliert oder nach Gutachten)
- Andersherum: Übererfüllung → LN erhält Gutschrift aus MR-Rückstand

## Steuern: Dry-Lease vs. Wet-Lease

- **Dry Lease**: Nur Flugzeug geleast; Besatzung und Betrieb durch LN
- **Wet Lease** (ACMI): Flugzeug + Crew + Maintenance + Insurance; kurzfristig, hohe Rates
- Steuerliche Unterschiede: Wet-Lease kann als Dienstleistung (USt auf Gesamtleistung) eingestuft werden

## Insolvenz einer Airline

- Cape Town Convention Art. XI (Alternative A/B): Schutz des LG bei Insolvenz LN (Airline)
- Alternative A: LG kann Flugzeug innerhalb von 60 Tagen nach Insolvenzeröffnung zurückholen, sofern keine Zahlung durch Insolvenzverwalter
- Deutschland: Alternative A umgesetzt (§ 108a InsO)

## Prüfprogramm

1. Kapstadt-Registrierung: Internationales Interesse angemeldet?
2. Wartungsorganisation: Wer ist CAMO? LN verantwortlich?
3. Maintenance Reserve: Korrekte Einzahlungen, Treuhänder, Verwendung?
4. Rückgabebedingungen: Vertragsklauseln klar? Gutachtenverfahren vereinbart?
5. Insolvenz: Cape Town Alternative A aktiv? 60-Tage-Frist bekannt?
6. USt: Dry vs. Wet-Lease? Welcher USt-Satz/Leistungsort?

## Typische Fallen

- Kapstadt-Registrierung versäumt → kein Prioritätsschutz gegenüber Gläubigern
- MR-Konten nicht ordnungsgemäß geführt → Rückgabe-Dispute
- Rückgabebedingungen unklar → Langwieriger technischer Streit
- Insolvenz Airline: 60-Tage-Frist nach Alternative A verpasst → Masse behält Flugzeug länger

## Normen und Quellen

- Kapstadt-Übereinkommen / Cape Town Convention: https://www.unidroit.org
- LuftVG §§ 101 ff. (Luftfahrzeugpfandrecht): https://www.gesetze-im-internet.de/luftvg/
- EASA-VO (EG) 2018/1139: https://eur-lex.europa.eu
- § 108a InsO (Cape Town, Insolvenz Airline): https://www.gesetze-im-internet.de/inso/__108a.html
- ICAO Annex 7: https://www.icao.int
- LuftVZO: https://www.gesetze-im-internet.de/luftvzo/

## Output-Formate

- **Kapstadt-Registrierungsablauf**: Schritt-für-Schritt zum International Registry
- **Return-Conditions-Checkliste**: Technische Anforderungen bei Rückgabe
- **MR-Berechnung**: Monatliche Reserve nach Flight Hours und Cycle
- **Insolvenz-Airline-Plan**: Sofortmaßnahmen für LG nach Insolvenzantrag

---

## Skill: `lessons-learned-nach-rueckgabe`

_Lessons Learned nach Leasingrückgabe: Analyse von Minderwertstreitigkeiten, Prozessverbesserungen, Vertragsoptimierungen und Portfolioentwicklung im Leasingrecht._

# Lessons Learned nach der Leasingrückgabe

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Analyse nach der Rückgabe

### Checkliste der Rückgabepunkte
- War das Rückgabeprotokoll vollständig? Fotos und Unterschriften vorhanden?
- Hat LN das Objekt in korrektem Zustand zurückgegeben?
- War der vereinbarte Rückgabezeitpunkt eingehalten?
- War das Objekt vollständig (Zubehör, Schlüssel, Dokumentation)?
- Gibt es Streit über Minderwert?

### Ursachenanalyse bei Minderwertstreit
- Klausel unklar: „Normaler Abnutzung" nicht präzise definiert?
- Gutachtenprozess: Einseitig oder kontradiktorisch?
- Keine gemeinsame Besichtigung: Protokoll fehlt
- § 548 BGB: Wurde die 6-Monate-Frist fast versäumt?

## Häufige Fehlerquellen

### Vertragliche Lücken
| Fehler | Ursache | Verbesserung |
|---|---|---|
| Minderwert unklar | Keine Toleranzdefinition | Katalog normaler Abnutzung einführen |
| Mehrkilometer streitig | Meilensteine nicht verifiziert | Km-Stand bei Übergabe dokumentiert |
| Rückgabeort unklar | Nicht im Vertrag | Rückgabeort explizit benennen |
| Restwert-Überraschung | LN wusste nicht | Bessere Aufklärung bei Vertragsschluss |
| Versicherungsnachweis vergessen | Kein System | Regelmäßiger Check (jährlich) |

### Prozessschwächen
- Rückgabeprotokoll ohne Fotos → Beweis fehlt
- Gutachter zu spät beauftragt → § 548 BGB-Frist knapp
- Kommunikationslücken zwischen LG-Abteilungen

## Vertragsoptimierungen

### Änderungen im Leasingvertrag
1. Normaler Abnutzungs-Katalog mit Beispielen (inkl. Fotos als Anlage)
2. Minderwert-Schwellenwerte (z.B. Kratzer < 10 cm: keine Nachforderung)
3. Gemeinsame Besichtigungsklausel
4. Vorabgutachten 3 Monate vor Vertragsende
5. Kfz: Km-Stand-Dokumentation bei Rückgabe

### Prozessverbesserungen
1. Erinnerungssystem: 3 Monate vor Vertragsende Besichtigung ankündigen
2. Standardisierte Rückgabeprotokolle (digital, mit Fotoplätzen)
3. 6-Monate-Frist-Alarm § 548 BGB automatisch im System
4. Gutachter-Rahmenvertrag: Schnelle Beauftragung ohne Ausschreibung

## Portfolioentwicklung

### Datenauswertung
- Wie viele Verträge haben Minderwert-Nachforderungen? (Quote)
- Welche Objekte haben häufig Streit? (Schadensklasse)
- Welche LN-Segmente sind problematisch? (Verbraucher, Gewerbe)
- Ø Minderwert je Objekt und Vertrag

### Kalkulationsanpassung
- Wenn Rückgabe-Erlöse systematisch unter Restwert: Restwert-Kalkulation anpassen
- Wenn Minderwert-Quote hoch: Rücklage oder Versicherung?

## Kundenbindung

### Kommunikation mit LN
- Streit bei Rückgabe: Fundstelle für zukünftige Beziehung?
- Wenn LN regelmäßiger Kunde: Kulanz bei kleinen Streitigkeiten sinnvoll?
- Anschlussprojekt: Neue Leasingvertrag besprechen

## Prüfprogramm

1. Rückgabeprotokoll vollständig analysiert?
2. Minderwert-Streit: Ursache identifiziert (Klausel, Prozess, Gutachten)?
3. Vertragsklausel überarbeitet (Normalabnutzungs-Katalog, gemeinsame Besichtigung)?
4. Prozessanpassung (Frist-Alarm, Protokoll-Standard)?
5. Portfolio-Daten: Minderwertquote, Rückgabeerlöse ausgewertet?
6. Kundenbindung: Feedback-Gespräch mit LN geführt?

## Normen und Quellen

- § 548 BGB (Verjährung): https://dejure.org/gesetze/BGB/548.html
- BGH VIII ZR 172/05 (normale Abnutzung): https://www.bgh.de
- § 307 BGB (AGB Inhaltskontrolle): https://dejure.org/gesetze/BGB/307.html
- openjur.de Rückgabe-Rechtsprechung: https://openjur.de
- BGH, Urteil vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 (Restwertgarantie): https://www.bgh.de

## Output-Formate

- **Lessons-Learned-Protokoll**: Analyse je Rückgabe-Fall
- **Klausel-Update-Liste**: Welche Klauseln nach Erfahrung anpassen
- **Prozess-Verbesserungsplan**: Maßnahmen, Verantwortliche, Fristen
- **Portfolio-Auswertung**: Minderwertquote, Rückgabeerlöse, Trends

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

