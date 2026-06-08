---
name: securpharm-faelschungsschutz
description: "Securpharm Fälschungsschutz: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht im Apothekenrecht."
---

# Securpharm Fälschungsschutz

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Securpharm Fälschungsschutz
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Securpharm ist die deutsche Umsetzung der EU-Fälschungsrichtlinie (2011/62/EU) und der delegierten VO 2016/161/EU. Jede Rx-Packung trägt einen 2D-Datamatrix-Code mit Seriennummer und einen Erstöffnungsschutz (Tamper-Evident-Verschluss). Die Apotheke ist verpflichtet, vor Abgabe die Echtheit zu verifizieren und den Code zu deaktivieren. Verstösse sind sicherheits- und aufsichtsrelevant.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Packung trägt keinen Securpharm-Code oder Tamper-Evident-Verschluss fehlt.
- System meldet "Alarm" bei Code-Verifizierung — Verdacht Fälschung oder Doppelung.
- Beanstandung der Aufsicht wegen unzureichender Verifikation.
- Bezugsweg Grosshandel/Reimporteur scheint nicht sicher — Kontrolle.
- Schulung des Personals zur Workflow-Konformität.

Eingaben:
- Packung mit 2D-Code und Erstöffnungsschutz.
- Apotheken-Warenwirtschaftssystem mit NMVS-Anbindung (National Medicines Verification System, Securpharm GmbH).
- Lieferdokumentation Grosshandel.
- Alarmprotokoll der vergangenen 30 Tage.

## Rechtlicher Rahmen

- **Richtlinie 2011/62/EU** (Fälschungsschutz-Richtlinie).
- **Delegierte VO 2016/161/EU** (Securpharm-DurchführungsVO) — Pflicht zur Seriennummer + Tamper-Evident-Verschluss seit 09.02.2019.
- **§§ 47 ff. AMG:** Sicherheitsanforderungen, Vertriebsweg.
- **§ 18 ApBetrO:** Eingangsprüfung von Arzneimitteln.
- **§ 21 ApBetrO:** QM-System.
- **Securpharm-Vertragswerk** (Apotheker, Hersteller, Grosshandel) — Nutzungsvereinbarung mit NMVS.
- **§ 95 AMG:** Strafbarkeit Inverkehrbringen gefälschter Arzneimittel.
- BfArM-Bekanntmachungen zu konkreten Fälschungsfunden.

## / Schritt für Schritt

1. **Wareneingang:** Tamper-Evident-Verschluss Sichtkontrolle. Verdächtige Packungen sofort isolieren.
2. **Vor Abgabe:** 2D-Code scannen. NMVS-System gibt eine von drei Antworten:
 - **OK / Aktiv:** Packung verifiziert; mit Abgabe wird der Code deaktiviert.
 - **Alarm:** Code bereits deaktiviert (Doppelausgabe), unbekannt, oder anderweitig verdächtig. Packung darf nicht abgegeben werden, bis Alarm geklärt ist.
 - **Fehler:** Technischer Fehler — manueller nach Securpharm-SOP.
3. **Bei Alarm:** Packung mit Quarantäne-Etikett versehen, Lieferanten/Grosshandel kontaktieren, Aufsicht informieren falls Fälschungsverdacht.
4. **Beim Retournieren:** Zurückgesendete Ware vor erneuter Verifikation reaktivieren (sofern innerhalb des Zeitfensters möglich, regelmässig 10 Tage).
5. **Lagerumlagerung:** Innerhalb der Apotheke kein erneutes Scannen erforderlich, nur bei Eingang und Ausgang.
6. **BtM-Packungen** und einige andere haben spezielle Anforderungen (gesonderte Securpharm-Logik bzw. Ausnahme).
7. **Schulung Personal:** alle Apothekenmitarbeiter müssen Alarmkennen.

## Trade-off-Matrix

| Securpharm-Status | Aktion | Risiko |
|---|---|---|
| OK / aktiv | Abgabe + Deaktivierung | keine |
| Alarm "Code unbekannt" | Quarantäne + Klärung Hersteller | mittel |
| Alarm "bereits deaktiviert" | Quarantäne + interne Suche Doppelausgabe | hoch |
| Tamper-Verschluss verletzt | nicht abgeben | sehr hoch |
| Code unscannbar (Beschädigung) | manuelle Eingabe Seriennummer | gering |
| Fehlende 2D-Codierung (ältere Charge) | Übergangsregelung beachten | mittel |

## Praxistipps

- Erstöffnungsschutz **vor** Securpharm-Verifikation prüfen — manche Fälscher übernehmen Code, brechen aber Verschluss.
- Bei Alarm nicht impulsiv abgeben; lieber Patient bitten zurückzukommen und Klärung mit Hersteller suchen.
- Securpharm-Logfile bei Aufsichtskontrollen vorzeigbar halten (mindestens fünf Jahre Aufbewahrung).
- Bei Retoure innerhalb des Reaktivierungs-Zeitfensters (üblich zehn Tage) Re-Aktivierung — sonst Packung verloren.
- Nach Fälschungsverdacht meldepflichtige Sicherheitsmeldung an BfArM/PEI.

## Mustertexte

### Quarantäne-Etikett (Vorlage)
"QUARANTÄNE - DO NOT DISPENSE. Securpharm-Alarm Datum: [...] | Arzneimittel: [...] | PZN: [...] | Charge: [...] | Verfall: [...] | Alarmcode: [...] | Bearbeiter: [...] | Status: nicht abgabefähig bis Klärung."

### Meldung Fälschungsverdacht an BfArM (Auszug)
"Sehr geehrte Damen und Herren, wir melden hiermit einen begründeten Fälschungsverdacht gemäss § 63b AMG i.V.m. EU-VO 2016/161. Arzneimittel: [Name, Stärke]. PZN: [...]. Charge: [...]. Verfall: [...]. Bezugsweg: Grosshandel [Name], Lieferschein [Nr., Datum]. Verdachtsmomente: 1. Securpharm-Alarm 'Code unbekannt' am [Datum]; 2. Tamper-Evident-Verschluss bei Eingangskontrolle [intakt/verletzt]; 3. optische Auffälligkeiten [...]. Die Packung wurde in Quarantäne genommen (Foto Anlage). Wir bitten um Aufnahme und Rückmeldung zum weiteren Vorgehen."

## Typische Fehler

- Code wird erst bei Abgabe gescannt; bei Alarm sind Patient und Apotheker schon im Übergabe-— Stress, fehlerhafte Reaktion.
- Tamper-Verschluss wird nicht geprüft; gefälschte Inhalte in Originalpackung übersehen.
- Bei Alarm wird "trotzdem abgegeben" — strafrechtliches Risiko (§ 95 AMG).
- Retoure ohne Re-Aktivierung — Packung im Lager gesperrt, Verlust für Apotheke.
- Schulung nur einmalig; bei Personalwechsel keine Auffrischung.

## Quellen Stand 06/2026

- Richtlinie 2011/62/EU; Delegierte VO 2016/161/EU.
- AMG §§ 47, 63b, 95.
- Securpharm GmbH: Nutzervereinbarung NMVS (vom Anwender zu verifizieren — laufende technische Updates).
- BfArM-Bekanntmachungen zu Fälschungsfunden (Spotsystem).
- ABDA-Merkblätter zur Securpharm-Praxis (vom Anwender zu verifizieren).

