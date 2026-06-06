---
name: qualitaetsgate
description: "Verl Qualitaetsgate im Plugin Verlagsrecht Buchpreisbindung im Verlagsrecht/Buchpreisbindung: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Verl Qualitaetsgate

## Arbeitsbereich

**Verl Qualitaetsgate** priorisiert Aktenlage, Fristen, Zuständigkeit, Beweislast und gewünschten Output. Die Prüfung beginnt beim sachtragenden Prüfungslinie und endet mit einem verwertbaren Arbeitsergebnis.

## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `verl-050-qualitaetsgate-verlagsakte` | Qualitätsgate Verlagsakte: Abschluss-Checkliste für das gesamte Plugin verlagsrecht-buchpreisbindung. Vollständigkeitsprüfung aller 49 Vorgänger-Skills und Gesamt-Compliance-Kontrolle einer Verlagsakte. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `verl-050-qualitaetsgate-verlagsakte`

**Fokus:** Qualitätsgate Verlagsakte: Abschluss-Checkliste für das gesamte Plugin verlagsrecht-buchpreisbindung. Vollständigkeitsprüfung aller 49 Vorgänger-Skills und Gesamt-Compliance-Kontrolle einer Verlagsakte.

# Qualitätsgate Verlagsakte — Abschlusskontrolle

## Zweck dieses Skills

Dieser Skill ist der abschließende **Qualitätssicherungs-Skill** des Plugins `verlagsrecht-buchpreisbindung`. Er dient als systematisches Qualitätsgate, das alle 49 vorherigen Skills zusammenführt und für einen konkreten Verlagsvorgang (ein Buch, eine Reihe oder eine Verlagsperiode) eine Gesamt-Compliance-Kontrolle durchführt.

Das Qualitätsgate prüft, ob die **Verlagsakte** zu einem Titel oder Autor alle rechtlich notwendigen Dokumente enthält, ob die Preisbindungs-Compliance vollständig ist, ob Rechte sauber dokumentiert sind und ob kritische Fristen eingehalten wurden.

Der Skill ist für Verlagsjuristen, Lektoren, Controller und Qualitätsbeauftragte konzipiert, die am Ende eines Verlagsprojekts — oder im Rahmen eines internen Audits — sicherstellen wollen, dass keine rechtlichen Risiken verborgen bleiben.

## Architektur des Qualitätsgates

Das Qualitätsgate ist in **7 Prüfbereiche** gegliedert, die den wichtigsten Themenbereichen des Plugins entsprechen:

| Bereich | Skills | Prüfthema |
|---------|--------|-----------|
| A | verl-001 bis 008 | Verlagsvertrag, Rechtekette, Ablieferung, Honorar |
| B | verl-009 bis 014 | Buchpreisbindung (Grundlagen und Spezialfälle) |
| C | verl-015 bis 020 | Titelschutz, VG Wort, Bildrechte, KI, Plagiat |
| D | verl-021 bis 030 | Persönlichkeitsrecht, Sondervertragstypen |
| E | verl-031 bis 040 | Presserecht, Vertrieb, Spezialrechte, Internationales |
| F | verl-041 bis 049 | Abmahnung, Rückruf, Musterverträge, Preisdokumentation |
| G | — | Meta-Compliance und Prozessqualität |

## Bereich A: Verlagsvertrag und Rechtekette (Skills 001–008)

### A1 — Vertragsgrundlage
- [ ] Schriftlicher Verlagsvertrag vorhanden (VerlG § 1)
- [ ] Werk eindeutig beschrieben (Titel, Umfang, Gattung)
- [ ] Ablieferungstermin vereinbart und dokumentiert (verl-004)
- [ ] Manuskript-Abnahme-Protokoll vorhanden

### A2 — Rechteübertragung
- [ ] Nutzungsrechte explizit aufgelistet (§ 31 UrhG): Print, E-Book, Hörbuch, Übersetzung, …
- [ ] Unbekannte Nutzungsarten: § 31a-Widerrufsrecht geregelt?
- [ ] Rechtekette bei Sammelwerk: Beitragsautoren-Verträge vollständig? (verl-048)
- [ ] Übersetzervertrag vorhanden, falls Übersetzung geplant (verl-007)

### A3 — Honorar und Vergütung
- [ ] Vorschusshöhe und Fälligkeit vereinbart (verl-005)
- [ ] Absatzhonorar-Satz klar definiert (Netto/Brutto-Basis)
- [ ] Staffelhonorar ab Bestseller-Schwelle (§ 32a UrhG)
- [ ] Jährliche Abrechnung und Auskunft nach § 32d UrhG gesichert

### A4 — Open Access / CC-Lizenzen
- [ ] Falls OA: Lizenztyp dokumentiert (verl-008)
- [ ] VG-Wort-Kompatibilität bei CC-Lizenz geprüft

## Bereich B: Buchpreisbindung-Compliance (Skills 009–014)

### B1 — Grundlegende Preisbindungsdokumentation
- [ ] Ladenpreis festgesetzt und dokumentiert (BuchPrG § 3, verl-009)
- [ ] VLB-Meldung mit Zeitstempel archiviert (verl-049)
- [ ] Preisänderungen chronologisch dokumentiert

### B2 — Rabatte und Sonderkonditionen
- [ ] Bibliotheks-/Schulrabatte: Erlaubnis nach § 5 Abs. 1 BuchPrG geprüft (verl-010)
- [ ] Bundle-/Serien-Preise dokumentiert
- [ ] Subskriptions-/Einführungspreise mit Laufzeit belegt (verl-012)

### B3 — Spezialfälle
- [ ] Mängelexemplar-Protokoll vorhanden (verl-011, verl-049)
- [ ] E-Book-Plattformpreise pro Plattform dokumentiert (verl-013)
- [ ] Amazon/Marketplace-Monitoring-Protokoll (verl-014)

### B4 — Preisaufhebung
- [ ] Falls vergriffen: Aufhebungsdokument nach § 7 BuchPrG vorhanden (verl-049)
- [ ] VLB-Abmeldung bei Vergriffenheit archiviert
- [ ] Buchhandel informiert

## Bereich C: Titel, Metadaten, Verwertungsgesellschaften (Skills 015–020)

### C1 — Titelschutz und Metadaten
- [ ] Titelschutz-Recherche vor Veröffentlichung (verl-015)
- [ ] ISBN beantragt und korrekt im VLB gemeldet (verl-016)
- [ ] Metadaten vollständig: Autor, Verlag, Preis, BISAC/WGSneu, Erscheinungsdatum

### C2 — VG Wort
- [ ] Meldepflicht geprüft: Verlag hat Verlagsanteil angemeldet? (verl-017)
- [ ] Autor über VG-Wort-Eigenregistrierung informiert?
- [ ] METIS-Meldung für digitale Nutzung abgesetzt?

### C3 — Bildrechte und Drittmaterial
- [ ] Alle Abbildungen mit Rechtenachweisen dokumentiert (verl-018)
- [ ] Bildrechte-Clearance-Liste vorhanden (Bildtitel, Urheber, Lizenz, Laufzeit)
- [ ] KI-generierte Inhalte gekennzeichnet und Nutzungsrecht geprüft (verl-019)
- [ ] Plagiatsprüfung abgeschlossen, Protokoll vorhanden (verl-020)

## Bereich D: Persönlichkeitsrechte und Sondervertragstypen (Skills 021–030)

### D1 — Persönlichkeitsrecht
- [ ] Lebende Personen im Sachbuch: Zitate und Darstellungen rechtlich geprüft (verl-021)
- [ ] Abbildungen von Personen: Einwilligung oder § 23 KUG-Ausnahme dokumentiert

### D2 — Sondervertragstypen
- [ ] Redaktionsvertrag: Freelancer vs. Arbeitnehmer-Status geklärt (verl-023)
- [ ] Fachbuch/Loseblatt-Aktualisierungspflichten geregelt (verl-022)
- [ ] Schulbuch: Zulassungsverfahren dokumentiert (verl-028)
- [ ] Literaturagentureintrag: Agentur-Provision und Vollmacht geregelt (verl-027)
- [ ] Insolvenz-Sicherungsklausel im Verlagsvertrag? (verl-025)

### D3 — Rezensionsexemplare und Steuer
- [ ] Rezensionsexemplar-Versandprotokoll (verl-030)
- [ ] Steuerliche Behandlung von Belegexemplaren und Rezensionsexemplaren dokumentiert

## Bereich E: Vertrieb, Spezialrechte, Internationales (Skills 031–040)

### E1 — Buchhandelsvertrieb
- [ ] Buchhandelsvertrag: Konditionenblatt aktuell (verl-032)
- [ ] Remissions-Protokoll: Abwicklung und Preisbindungstreue bei Remittenden (verl-011)
- [ ] Bibliothekslizenz-Verträge dokumentiert (verl-033)

### E2 — Spezialrechte
- [ ] Hörbuch-Sprechervertrag: Leistungsschutzrechte geregelt (verl-034)
- [ ] Podcast/Content-Recycling: Nutzungsrechte für Sekundärverwertung (verl-035)
- [ ] Online-Portal/Paywall/Datenbankrecht: Lizenzstruktur dokumentiert (verl-036)

### E3 — Internationales
- [ ] Auslandslizenzen: Agenten- oder Direktverträge dokumentiert (verl-007)
- [ ] Sanctions-Compliance bei Export (verl-038)
- [ ] NDA für Buchmesse-Verhandlungen (verl-037)

### E4 — Presserecht
- [ ] Gegendarstellungs- und Unterlassungsrisiken eingeschätzt (verl-031)
- [ ] Presserecht-Krisenplan vorhanden?

## Bereich F: Abmahnung, Rückruf, Vertragsende (Skills 041–049)

### F1 — Preisbindungs-Compliance
- [ ] Abmahnungs-Risiko periodisch geprüft (verl-041)
- [ ] Unterlassungserklärung: Falls frühere Abmahnung, Compliance-Monitoring aktiv (verl-042)

### F2 — Vertragsbeendigung
- [ ] Kündigungsrecht nach § 41 UrhG bei Nichtausübung geprüft (verl-045)
- [ ] Rückruf-Verfahren bei Vergriffenheit dokumentiert (verl-046)
- [ ] Rechte-Rückfall nach Verlagsinsolvenz geregelt (verl-025)

### F3 — Vertragsqualität
- [ ] Autorenvertrag: Red-Team-Prüfung abgeschlossen (verl-047)
- [ ] Herausgebervertrag (falls zutreffend): Red-Team-Prüfung abgeschlossen (verl-048)

## Bereich G: Meta-Compliance und Prozessqualität

### G1 — Dokumenten-Vollständigkeit
- [ ] Alle wesentlichen Verträge schriftlich vorhanden und unterzeichnet
- [ ] Alle Vertragsänderungen (Addenda) chronologisch dokumentiert
- [ ] Auslieferungsaufträge und Preismeldungen archiviert

### G2 — Fristen-Monitoring
- [ ] Ablieferungsfristen (VerlG § 7) kalendarisch erfasst
- [ ] Abrechnungszyklen (§ 32d UrhG) terminiert
- [ ] Verjährungsfristen für Honoraransprüche (3 Jahre, § 195 BGB) bekannt
- [ ] VG-Wort-Meldefristen (30. Juni jedes Jahres) im Kalender

### G3 — Risikobewertung
- [ ] Risikoeinschätzung für den Titel erstellt (Haftungsrisiken, Preisbindungsrisiken)
- [ ] Versicherungsschutz geprüft (Verlegerrechtsschutzversicherung)

### G4 — Datenschutz und DSGVO
- [ ] Autorenstammdaten: DSGVO-konform gespeichert?
- [ ] Newsletter-/Marketing-Einwilligung des Autors vorhanden?
- [ ] Belegversand-Adressen gelöscht nach Zweckerfüllung?

## Normenübersicht: Alle zentralen Gesetze des Plugins

| Gesetz | Kernbedeutung im Plugin | Quelle |
|--------|------------------------|--------|
| VerlG 1901 | Grundnormen des Verlagsvertrags (§§ 1, 7, 17, 30) | https://www.gesetze-im-internet.de/verlg/ |
| UrhG | Nutzungsrechte, Vergütung, Rückruf (§§ 31, 32, 32a, 32d, 41, 42) | https://www.gesetze-im-internet.de/urhg/ |
| BuchPrG | Ladenpreisbindung (§§ 3–7, 9, 13) | https://www.gesetze-im-internet.de/buchprg/ |
| VGG | Verwertungsgesellschaften (VG Wort) | https://www.gesetze-im-internet.de/vgg/ |
| BGB | Vertragsrecht, AGB-Kontrolle (§§ 305 ff., 195) | https://www.gesetze-im-internet.de/bgb/ |
| DSM-RL 2019/790 | Faire Vergütung, Transparenz (Art. 18–22) | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790 |
| KUG | Recht am eigenen Bild (§§ 22, 23) | https://dejure.org/gesetze/KUG |
| UWG | Wettbewerbsrecht (Preisbindungsabmahnungen) | https://www.gesetze-im-internet.de/uwg_2004/ |

## Typische Fallen (Gesamtblick)

- **Fehlende Schriftform**: Mündliche Absprachen zu Honoraren oder Rechteänderungen sind nicht beweisbar.
- **Rechteketten-Lücken**: Bei Sammelwerken, Übersetzungen oder bearbeiteten Werken fehlen Beitrags-/Bearbeiter-Verträge.
- **VLB-Inkonsistenz**: Ladenpreis im VLB weicht von tatsächlichem Buchhandelspreis ab → Preisbindungsrisiko.
- **§ 32d-Vergessen**: Autor erhält keine Jahresabrechnung → Auskunftsklage droht.
- **§ 41-Übersehen**: Verlag merkt nicht, dass ein Autor das Rückrufrecht ausgeübt hat und verwertet weiter.
- **VG-Wort-Fristen verpasst**: Meldung bis 30. Juni vergessen → Ausschüttungsverlust.
- **Keine Nachlassregelung**: Autor verstirbt; unklar, wer Erbe der Urheberrechte ist → Verlag kann Vertrag nicht fortführen.

## Verwendung des Qualitätsgates

### Wann einsetzen?

| Anlass | Prüfumfang |
|--------|-----------|
| Neuerscheinung (Titelstart) | Bereiche A, B, C vollständig; D–F nach Bedarf |
| Jahres-Compliance-Audit | Alle Bereiche A–G |
| Vertragsende / Autorenwechsel | Bereiche A, F vollständig |
| Preisbindungs-Audit | Bereich B vollständig |
| Vorbereitung Buchmesse-Verhandlung | Bereiche A, E (Internationales) |
| Vorbereitung Verlagsverkauf/-fusion | Alle Bereiche A–G |

## Quellenreferenzen

- VerlG: https://www.gesetze-im-internet.de/verlg/
- UrhG: https://www.gesetze-im-internet.de/urhg/
- BuchPrG: https://www.gesetze-im-internet.de/buchprg/
- VGG: https://www.gesetze-im-internet.de/vgg/
- DSM-RL 2019/790: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L0790
- BGB AGB-Recht: https://www.gesetze-im-internet.de/bgb/__305.html
- KUG: https://dejure.org/gesetze/KUG
- dejure.org Übersicht Urheberrecht: https://dejure.org/gesetze/UrhG

## Output-Formate

- Vollständige Qualitätsgate-Checkliste (alle 7 Bereiche, pro Titel ausfüllbar)
- Compliance-Ampel-Bericht (Grün/Gelb/Rot je Bereich)
- Risikoprotokoll (offene Punkte mit Prioritäten und Verantwortlichen)
- Jahres-Audit-Bericht für Verlagsleitung
- Onboarding-Checkliste für neue Titel (Kurzversion Bereiche A + B + C)
