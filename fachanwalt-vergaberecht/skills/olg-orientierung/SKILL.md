---
name: olg-orientierung
description: "OLG Orientierung im Plugin Fachanwalt Vergaberecht: prüft konkret Sofortige Beschwerde gegen VK-Entscheidung beim, Orientierung im Fachanwaltsrecht Vergaberecht, Ruegeschriftsatz im Vergabeverfahren nach § 160 Abs, Sektorenvergabe nach SektVO durchfuehren und angreifen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# OLG Orientierung

## Arbeitsbereich

**OLG Orientierung** ordnet den Fall über die tragenden Prüfungslinien: Sofortige Beschwerde gegen VK-Entscheidung beim, Orientierung im Fachanwaltsrecht Vergaberecht, Ruegeschriftsatz im Vergabeverfahren nach § 160 Abs. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-vergaberecht-olg-sofortige-beschwerde` | Sofortige Beschwerde gegen VK-Entscheidung beim OLG-Vergabesenat erstellen: Bieter oder Auftraggeber will VK-Beschluss angreifen oder verteidigen. Normen: §§ 171-184 GWB (Beschwerde), § 172 GWB (Frist zwei Wochen ab Zustellung), § 173 GWB (aufschiebende Wirkung), § 176 GWB (Verlaengerung), § 178 GWB (Entscheidung). Pruefraster: Beschwerdebefugnis, Frist, Form, Begruendungstiefe, Antraege, aufschiebende Wirkung beantragen, Eilantrag § 173 Abs. 1 S. 3 GWB. Output Beschwerdeschriftsatz-Geruest, Fristenkalender, Antraege-Set. Abgrenzung: VK-Verfahren siehe fachanwalt-vergaberecht-nachpruefungsverfahren-vk; Schadensersatz siehe fachanwalt-vergaberecht-schadensersatz-181-gwb. |
| `fachanwalt-vergaberecht-orientierung` | Orientierung im Fachanwaltsrecht Vergaberecht: FAO-Voraussetzungen, EU-Schwellen, Nachprüfungsverfahren, Kernliteratur ueberblicken. Normen: GWB §§ 97 ff. (Vergaberecht), VgV, SektVO, KonzVgV, UVgO (Unterschwelle), VOB-A. Prüfraster: Schwellenwertabhaengigkeit, Auftragsarten, Verfahrenstypen (offen, nicht-offen, Verhandlung), Nachprüfungsorgane VK und OLG. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Mandats-Triage siehe mandat-triage-vergaberecht; Bau-Architektenrecht siehe fachanwalt-bau-architektenrecht-Plugin. |
| `fachanwalt-vergaberecht-ruegeschriftsatz-160-gwb` | Ruegeschriftsatz im Vergabeverfahren nach § 160 Abs. 3 GWB ausarbeiten: Bieter will Ruege inhaltlich stark begründen. Normen: § 160 Abs. 3 GWB (Ruege als Zulassigkeitsvoraussetzung), §§ 97 ff. GWB. Prüfraster: Konkrete Vergabestoerung, Norm-Bezeichnung, Beweismittel, Antrag auf Abhilfe, unverzuegliche Einreichung. Output Ruegeschriftsatz, Begleitschreiben. Abgrenzung: Ersteinschaetzung Ruege-Erfordernis siehe fachanwalt-vergaberecht-ruege-vor-zuschlag; Nachprüfungsantrag danach siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk. |
| `fachanwalt-vergaberecht-sektorenvergabe-sektvo` | Sektorenvergabe nach SektVO durchfuehren und angreifen: Sektorenauftraggeber Wasser/Energie/Verkehr/Post oder Bieter will SektVO-konformes Verfahren oder Ruege. Normen: §§ 100-104 GWB (Sektorenauftraggeber), SektVO, RL 2014/25/EU. Pruefraster: Sektorenauftraggeberbegriff § 100 GWB, ausschliesslicher/besonderer Recht, Schwellenwert EUR 432000 ab 01.01.2026, Verfahrenswahl § 13 SektVO, Verhandlungsspielraum, Praequalifikation § 48 SektVO. Output Verfahrensentwurf, Pruefvermerk Verfahrenswahl. Abgrenzung: Allgemein VgV siehe fachanwalt-vergaberecht-orientierung; Konzessionen siehe fachanwalt-vergaberecht-konzessionsvergabe-konzvgv. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-vergaberecht-olg-sofortige-beschwerde`

**Fokus:** Sofortige Beschwerde gegen VK-Entscheidung beim OLG-Vergabesenat erstellen: Bieter oder Auftraggeber will VK-Beschluss angreifen oder verteidigen. Normen: §§ 171-184 GWB (Beschwerde), § 172 GWB (Frist zwei Wochen ab Zustellung), § 173 GWB (aufschiebende Wirkung), § 176 GWB (Verlaengerung), § 178 GWB (Entscheidung). Pruefraster: Beschwerdebefugnis, Frist, Form, Begruendungstiefe, Antraege, aufschiebende Wirkung beantragen, Eilantrag § 173 Abs. 1 S. 3 GWB. Output Beschwerdeschriftsatz-Geruest, Fristenkalender, Antraege-Set. Abgrenzung: VK-Verfahren siehe fachanwalt-vergaberecht-nachpruefungsverfahren-vk; Schadensersatz siehe fachanwalt-vergaberecht-schadensersatz-181-gwb.

### Sofortige Beschwerde OLG-Vergabesenat

## Aufgabe
Bereite eine sofortige Beschwerde gegen eine Vergabekammer-Entscheidung vor oder verteidige sie. Frist zwei Wochen ab Zustellung ist nicht verlaengerbar. Aufschiebende Wirkung muss separat beantragt werden.

## Einstieg
1. Wer hat verloren? (Bieter, Auftraggeber, Beigeladener)
2. Zustelldatum des VK-Beschlusses?
3. Wurde Zuschlag bereits erteilt? Wenn ja: nur noch Feststellungs- und Schadensersatzpfad.
4. Suspendiereffekt § 169 GWB noch wirksam? Aufschiebende Wirkung § 173 GWB?
5. Streitwert ueber EUR 30000 (PKH-Schwelle)? Anwaltszwang § 175 Abs. 2 GWB liegt vor.

## Fristen und Form
| Frist | Norm | Bemerkung |
|---|---|---|
| Beschwerde | § 172 Abs. 1 GWB | 2 Wochen ab Zustellung VK-Beschluss |
| Begruendung | § 172 Abs. 2 GWB | mit Beschwerdeschrift einzureichen |
| Verlaengerung | nicht moeglich | Frist ist Ausschlussfrist |
| Aufschiebende Wirkung | § 173 Abs. 1 S. 3 GWB | gesondert beantragen |
| Erweiterung Suspensiveffekt | § 173 Abs. 2 GWB | bei OLG bis Endentscheidung |

Form: Beim OLG-Vergabesenat, beim Gericht der Vergabekammer; Beschwerdeschrift mit Begruendung als ein Schriftsatz; Anwaltszwang.

## Antragsmodelle
### Bieter, der vor VK verloren hat
- Aufhebung VK-Beschluss
- Feststellung Rechtsverletzung
- Verpflichtung Auftraggeber zu konkretem Verhalten (z. B. neue Wertung)
- Aufschiebende Wirkung der Beschwerde
- Hilfsweise: Erweiterung Suspensiveffekt § 173 Abs. 2 GWB

### Auftraggeber, der vor VK verloren hat
- Aufhebung VK-Beschluss
- Verwerfung Nachpruefungsantrag als unzulaessig oder unbegruendet
- Antrag auf Aufhebung Suspensiveffekt § 169 Abs. 2 GWB

### Beigeladener Bestbieter
- Eigenstaendige Beschwerdebefugnis bejahen
- Hauptantrag: Aufhebung der ihn belastenden VK-Entscheidung
- Hilfsantrag: Beibehaltung Zuschlagschance

## Begruendungstiefe
- Beschwerdegrund: Rechtsfehler der VK; Tatsachen werden vom OLG nur eingeschraenkt geprueft.
- Subsumtion zu § 97 Abs. 6 GWB (Bieterrecht).
- Auseinandersetzung mit Begruendung der VK in voller Tiefe.
- Bei Wertungsfragen: konkrete Wertungsfehler und Kausalitaet zur Zuschlagschance.

## Aufschiebende Wirkung § 173 GWB
- Antrag auf Verlaengerung des Suspensiveffekts der VK zwingend stellen, sonst kann Zuschlag erteilt werden.
- Abwaegung Interessen Bieter vs. Auftraggeber/Allgemeinheit.
- Erfolgsaussichten der Hauptsache als Hauptkriterium.

## Typische Fehler
- Beschwerdefrist versaeumt (Wiedereinsetzung praktisch ausgeschlossen).
- Aufschiebende Wirkung nicht beantragt -> Zuschlag waehrend Beschwerde.
- Neue Tatsachen ohne § 174 GWB-Pruefung eingefuehrt.
- Anwaltszwang verletzt.
- Streitwertangabe fehlt.

## Output
- Beschwerdeschriftsatz-Geruest mit Saetzen, Antraegen, Begruendungsabschnitten.
- Fristenkalender (Zustellung, Beschwerde, Suspensiv-Antrag, Begruendung, Erwiderung).
- Pruefvermerk Erfolgsaussichten.

## Quellenregel
BGH X ZB 14/17 (Suspensiveffekt) und OLG-Linien nur mit Datum, Aktenzeichen und frei pruefbarer Quelle ueber dejure.org oder openjur.de zitieren.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 2. `fachanwalt-vergaberecht-orientierung`

**Fokus:** Orientierung im Fachanwaltsrecht Vergaberecht: FAO-Voraussetzungen, EU-Schwellen, Nachprüfungsverfahren, Kernliteratur ueberblicken. Normen: GWB §§ 97 ff. (Vergaberecht), VgV, SektVO, KonzVgV, UVgO (Unterschwelle), VOB-A. Prüfraster: Schwellenwertabhaengigkeit, Auftragsarten, Verfahrenstypen (offen, nicht-offen, Verhandlung), Nachprüfungsorgane VK und OLG. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Mandats-Triage siehe mandat-triage-vergaberecht; Bau-Architektenrecht siehe fachanwalt-bau-architektenrecht-Plugin.

### Fachanwalt für Vergaberecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 40 Fälle in den letzten drei Jahren, davon mindestens 20 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Vergaberecht Oberschwellig | GWB §§ 97 ff. (Vergaberecht) §§ 155 ff. (Nachprüfung) |
| Vergabeverordnung | VgV (Liefer- und Dienstleistungen) |
| Sektoren | SektVO |
| Konzessionen | KonzVgV |
| Bauleistungen oberschwellig | VgV-Baubereich VOB-A Abschnitt 2 |
| Unterschwellig | UVgO (Unterschwellenvergabeordnung) VOB-A Abschnitt 1 |
| EU-Schwellenwerte | Delegierte Verordnungen (alle zwei Jahre); ab 01.01.2026 (DelVO (EU) 2025/2150/2151/2152): Liefer-/Dienstleistung Kommunen EUR 216000 Bund EUR 140000 Sektoren EUR 432000 Bau und Konzessionen EUR 5404000; Soziale/besondere Dienstleistungen unverändert EUR 750000 (Bund) bzw. EUR 1000000 (Sektoren) |
| Verteidigung und Sicherheit | VSVgV |
| EU-RL | RL 2014/24 (allgemein) RL 2014/25 (Sektoren) RL 2014/23 (Konzessionen) RL 2007/66 Rechtsmittel |

## Typische Mandate

- Vertretung Bieter im Vergabeverfahren
- Ruege bei der Vergabestelle (§ 160 Abs. 3 GWB)
- Nachprüfungsantrag bei der Vergabekammer
- Beschwerde gegen Entscheidung der Vergabekammer beim OLG-Vergabesenat
- Vertretung Auftraggeber (Vergabestelle) bei Streitigkeiten
- Korruption und Compliance bei öffentlichen Aufträgen
- Schadensersatz nach § 181 GWB bei vergaberechtswidriger Vergabe

## Fristen

- **Ruegefrist** § 160 Abs. 3 GWB:
 - **erkannte Verstöße** unverzueglich nach Kenntnis (in der Praxis bis zu zehn Kalendertage).
 - **erkennbare Verstöße** vor Ablauf der Angebotsfrist.
 - **in der Bekanntmachung erkennbare Verstöße** bis zum Ablauf der Angebotsfrist.
- **Nachprüfungsantrag** § 160 GWB binnen 15 Kalendertagen nach Mitteilung der Vergabestelle dass der Ruege nicht abgeholfen wird.
- **Beschwerde** § 171 GWB binnen zwei Wochen nach Zustellung der Vergabekammer-Entscheidung.
- **Stillhaltefrist § 134 GWB** zehn Kalendertage (15 bei nicht-elektronischer Information) zwischen Vorinformation und Zuschlag.

## Hauptforen

- **Vergabekammer** (Bund: BKartA Vergabekammer; Land: Vergabekammer der Bezirksregierung / Landesvergabekammer).
- **OLG-Vergabesenat** Beschwerdeinstanz.
- **BGH** (XIII. Zivilsenat seit 01.01.2021) bei Divergenzvorlage § 179 Abs. 2 GWB des OLG-Vergabesenats.
- **EuGH** bei EU-rechtlichen Vorabentscheidungen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Vergaberecht DAV.
- DVNW Deutsches Vergabenetzwerk.

## Schnittstellen

- **fachanwalt-bau-architektenrecht** bei Bauaufträgen.
- **regulatorisches-recht** bei Beihilferecht.
- **gesellschaftsrecht** bei Bieterkonsortien.
- **kanzlei-allgemein** Notfristen Versand.

## Vertiefung: Aktuelle Rechtsprechung und Normen

### Schluessel-Leitsaetze Vergaberecht 2020-2024

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ueberblick Vergaberecht
| Regelwerk | Anwendungsbereich |
|---|---|
| GWB §§ 97-131 | Grundsaetze (Oberschwelle) |
| GWB §§ 155-186 | Nachpruefungsverfahren |
| VgV | Liefer-/Dienstleistungen (Bund/Länder) |
| SektVO | Versorgungsunternehmen (Wasser/Energie/OEPNV) |
| KonzVgV | Konzessionsvergaben |
| UVgO | Unterschwellige Lieferungen/Dienstleistungen |
| VOB/A Abschnitt 1 | Unterschwellige Bauleistungen |
| VOB/A Abschnitt 2 | EU-Bauleistungen |

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 3. `fachanwalt-vergaberecht-ruegeschriftsatz-160-gwb`

**Fokus:** Ruegeschriftsatz im Vergabeverfahren nach § 160 Abs. 3 GWB ausarbeiten: Bieter will Ruege inhaltlich stark begründen. Normen: § 160 Abs. 3 GWB (Ruege als Zulassigkeitsvoraussetzung), §§ 97 ff. GWB. Prüfraster: Konkrete Vergabestoerung, Norm-Bezeichnung, Beweismittel, Antrag auf Abhilfe, unverzuegliche Einreichung. Output Ruegeschriftsatz, Begleitschreiben. Abgrenzung: Ersteinschaetzung Ruege-Erfordernis siehe fachanwalt-vergaberecht-ruege-vor-zuschlag; Nachprüfungsantrag danach siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk.

### Ruegeschriftsatz § 160 III GWB

## Zweck

Ruege als Pflicht-Vorstufe zum Nachprüfungsverfahren.

## 1) Voraussetzungen § 160 III GWB

### Frist

- **Unverzueglich nach Kenntnis** des Mangels
- Praxis-Faustregel: 5-10 Werktage
- Bei Erkennbarkeit aus Bekanntmachung: schon dort ruegen

### Form

- Schriftlich (E-Mail genuegt)
- An Vergabestelle

### Inhalt

- Konkreter Mangel benannt
- Begründung
- Antrag auf Abhilfe

## 2) Ruege-Inhalte (typische Mangel)

| Mangel | Beispiel |
|---|---|
| Wettbewerbs-Verzerrung | Insider-Information |
| Diskriminierung | Pflicht-Referenzen unangemessen |
| Eignungs-Kriterien | Mindest-Umsatz uneurthältnismaessig |
| Wertungs-Mangel | Bewertungs-Massstab unklar |
| Änderungs-Verbot | Wesentliche Vertrags-Änderung ohne Neu-Ausschreibung |

## 3) Präklusion

### Verlust der Anspruche

- Bei verspaeteter Ruege: **Präklusion**
- Späteres Nachprüfungsverfahren unzulaessig
- Strenge BGH-Linie

### Ausnahmen

- Mangel nicht erkennbar
- Bei Vertraulichkeits-Mangel
- Bei nicht-veröffentlichten Maßnahmen

## 4) Workflow

### Phase 1 — Kenntnis-Zeitpunkt

- Wann Mangel erkennbar?
- Frist 10 Werktage als Faustregel

### Phase 2 — Schriftsatz

- Klare Mangel-Beschreibung
- Konkrete Norm-Verweis (VgV, GWB)
- Antrag

### Phase 3 — Reaktion Vergabestelle

- Innerhalb 14 Tagen
- Abhilfe oder Ablehnung

### Phase 4 — Bei Ablehnung

- Nachprüfungs-Antrag VK § 160 GWB
- Frist 15 Tage nach Vergabestelle-Ablehnung

## 5) Typische Fehler

1. **Frist "unverzueglich" verpasst**
2. **Mangel zu pauschal** benannt
3. **Ruege an falsche Stelle** (z.B. Vergabe-Sachbearbeiter statt Vergabestelle-Vorstand)
4. **Beweismittel fehlen**

## 6) BGH-/OLG-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- OLG Duesseldorf-Linie zur "unverzueglich"-Auslegung

## Anschluss

- `fachanwalt-vergaberecht-nachpruefungsverfahren-vk` — bei Folge
- `ruegeschriftsatz-erstellen` (Power-Tool) — Schriftsatz-Hilfe
- `fachanwalt-vergaberecht-orientierung` — Triage

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Ruegeschriftsatz § 160 GWB | Ruegeschreiben; Template unten |
| Variante A — Ruegefrist verstrichen | Praeklusion; NPA trotzdem erwaegen wenn noch Spielraum |
| Variante B — Verstoss aus Zuschlagsinformation erkennbar | § 160 Abs. 3 Nr. 4 GWB; 15-Tage-Frist ab Info-Schreiben |
| Variante C — Mehrere Verstossgruende | Alle Ruegen in einem Schreiben; Praeklusion vermeiden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Vertiefung: Leitsaetze und Output-Template

### Triage — Bevor losgelegt wird, klaere:

1. Wann Kenntnis vom Verstoss? → Fristberechnung § 160 Abs. 3 GWB (10 Tage sonstige / Angebotsabgabe bei Bekanntmachung)
2. Oberschwellen- oder Unterschwellenauftrag? → § 106 GWB Schwellenwert pruefen
3. Welche konkrete Norm verletzt? → Wertung / Eignung / Vergabeunterlage / Zuschlagskriterien
4. Informationsschreiben § 134 GWB erhalten? → Stillhaltefrist 10 Tage vor Zuschlag
5. Zuschlag bereits erteilt? → Keine Ruege mehr sinnvoll; Schadensersatz § 181 GWB
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

### Ergaenzende Leitsaetze Ruegeschriftsatz

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Output-Template Ruegeschriftsatz § 160 GWB
**Adressat:** Vergabestelle [AUFTRAGGEBER] — Tonfall: sachlich-juristisch, fristsetzend

```
[Kanzlei], [Datum]

[AUFTRAGGEBER / VERGABESTELLE]
[ANSCHRIFT]
Per beA / E-Mail mit Lesebestaetigung

Vergabeverfahren [BEZEICHNUNG], TED-Nr. [NR.]
Unsere Mandantschaft: [BIETER], [ANSCHRIFT]

R U E G E gemaess § 160 Abs. 3 GWB

Sehr geehrte Damen und Herren,

namens und in Vollmacht des oben genannten Bieters
ruegen wir folgenden Vergabeverstoss:

1. Sachverhalt / Verstoss:
 [Konkrete Beschreibung, z.B.:
 "Die Vergabeunterlagen sehen als Eignungskriterium
 [XYZ] vor, obwohl dieses Kriterium unverhaaltnismaessig
 und diskriminierend ist (§ 122 GWB i.V.m. § 45 VgV)."]

2. Verletzte Normen:
 - [§ 97 Abs. 2 GWB (Gleichbehandlung)]
 - [§ 122 GWB / § 45 VgV (Eignungskriterien)]
 - [EU-RL 2014/24/EU Art. 58]

3. Kenntnisdatum:
 [DATUM] — [Quelle, z.B. "Vergabeunterlagen"]
 Frist § 160 Abs. 3 GWB gewahrt.

4. Antrag:
 Wir fordern Sie auf, den Vergabeverstoss
 durch [Massnahme: Ergaenzung der Unterlagen /
 Aufhebung Eignungskriterium] zu beseitigen.

 Andernfalls beantragen wir umgehend Nachpruefung
 bei der Vergabekammer [NAME VK].

Mit freundlichen Gruessen
[Rechtsanwalt/-anwaeltin, Fachanwalt Vergaberecht]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 4. `fachanwalt-vergaberecht-sektorenvergabe-sektvo`

**Fokus:** Sektorenvergabe nach SektVO durchfuehren und angreifen: Sektorenauftraggeber Wasser/Energie/Verkehr/Post oder Bieter will SektVO-konformes Verfahren oder Ruege. Normen: §§ 100-104 GWB (Sektorenauftraggeber), SektVO, RL 2014/25/EU. Pruefraster: Sektorenauftraggeberbegriff § 100 GWB, ausschliesslicher/besonderer Recht, Schwellenwert EUR 432000 ab 01.01.2026, Verfahrenswahl § 13 SektVO, Verhandlungsspielraum, Praequalifikation § 48 SektVO. Output Verfahrensentwurf, Pruefvermerk Verfahrenswahl. Abgrenzung: Allgemein VgV siehe fachanwalt-vergaberecht-orientierung; Konzessionen siehe fachanwalt-vergaberecht-konzessionsvergabe-konzvgv.

### Sektorenvergabe (SektVO)

## Aufgabe
Sektorenvergabe nach SektVO strukturieren oder angreifen. Schluesselfragen: Ist der Auftraggeber Sektorenauftraggeber? Greift die SektVO statt der VgV? Welcher Schwellenwert?

## Einstieg
1. Taetigkeitsbereich: Wasser, Energie (Gas, Waerme, Elektrizitaet), Verkehr (Bus, Bahn, Hafen, Flughafen), Postdienste?
2. Rechtsform und Eigentuemerschaft (öffentlicher Auftraggeber, öffentliches Unternehmen, Privatunternehmen mit besonderen oder ausschliesslichen Rechten)?
3. Auftragswert oberhalb EUR 432000 (LD/DL) oder EUR 5404000 (Bau) ab 01.01.2026?
4. Gemischte Auftraege (sektorenfremd + sektorenbezogen)?
5. Bekanntmachung bereits erfolgt?

## Pruefraster
### Sektorenauftraggeber § 100 GWB
- Oeffentlicher Auftraggeber im Sektorenbereich, oder
- Oeffentliches Unternehmen (beherrschender Einfluss durch öffentliche Hand), oder
- Privatunternehmen, dem besondere oder ausschliessliche Rechte verliehen wurden (z. B. Konzessionen, Genehmigungen).

### Sektorentaetigkeit §§ 102 ff. GWB
- Gas/Waerme: Bereitstellung fester Netze.
- Elektrizitaet: Erzeugung, Fortleitung, Verteilung.
- Wasser: Trinkwasserversorgung.
- Verkehr: öffentlicher Personenverkehr, Flug-, See-, Binnenhaefen.
- Post: Postdienste i. S. Postdienste-RL.

### Verfahrenswahl § 13 SektVO
- Offenes Verfahren, nicht-offenes Verfahren, Verhandlungsverfahren mit TW, wettbewerblicher Dialog, Innovationspartnerschaft.
- Verhandlungsverfahren ohne TW in den Faellen § 14 SektVO.
- Mehr Flexibilitaet als VgV: Verhandlungsverfahren mit TW ohne zusaetzliche Voraussetzungen.

### Praequalifikation § 48 SektVO
- Bieterlisten/Praequalifikation moeglich; Anforderungen objektiv, transparent, diskriminierungsfrei.

### Wertung § 31 SektVO
- Wirtschaftlichstes Angebot, Lebenszykluskosten zulaessig (§ 32 SektVO).
- Strategische soziale/oekologische Kriterien.

## Schnittstellen
- Sektorenvergabe-RL 2014/25/EU.
- Konzessionen in Sektoren -> KonzVgV.
- Verteidigung und Sicherheit -> VSVgV.
- Sektorenfremde Auftraege desselben Auftraggebers -> VgV.

## Typische Fehler
- Sektorenauftraggeber wendet faelschlich VgV an (schliesst Verhandlungsspielraum unnoetig ein).
- VgV-Auftraggeber wendet SektVO an, obwohl Auftrag nicht sektorenbezogen.
- Schwellenwert verwechselt (EUR 432000 vs. EUR 216000/140000).
- Praequalifikationsbedingungen diskriminierend.

## Output
- Verfahrenswahl-Pruefvermerk.
- SektVO-Verfahrensplan mit Fristen.
- Praequalifikationsbedingungen-Entwurf.

## Quellenregel
EuGH- und OLG-Entscheidungen zur Sektorenabgrenzung ueber curia.europa.eu / dejure.org verifizieren.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.
