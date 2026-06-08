---
name: versandhandel-e-versandhandelserlaubnis-eu
description: "zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Versandhandel und E-Rezept Intake im Apothekenrecht."
---

# Versandhandel und E-Rezept Intake

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Versandhandel und E-Rezept Intake
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Aufnahme eines Versandhandelsfalls: Bestelleingang einer Versandapotheke, Prüfung der gesetzlichen Voraussetzungen für den Versand verschreibungspflichtiger und apothekenpflichtiger Arzneimittel, Schnittstelle zum E-Rezept. Der Skill fasst die Pflichtangaben, Beratungsdokumentation und Verbots-Sortimente zusammen — insbesondere das Rx-Versandverbot (RxVV-Diskussion) und das Versandverbot für bestimmte Arzneimittel.

## Wann dieses Modul hilft / Kaltstart-Fragen

- Versandapotheke nimmt erstmals E-Rezept-Bestellungen entgegen.
- Beanstandung der Aufsicht wegen unzureichender Beratungsdokumentation oder Versand verbotener Arzneimittel.
- Patient bestellt rezeptpflichtiges Arzneimittel, das nicht versandt werden darf (z. B. bestimmte Kühlware, BtM, T-Rezept).
- Aufbau eines internen SOP-Pakets für Versandhandel.

Eingaben:
- Versandhandelserlaubnis (§ 11a ApoG) der inländischen Apotheke.
- Bei EU-Versandapotheke: Erlaubnis der jeweiligen EU-Behörde, Eintrag im DEAS-Register, deutsche Versandhandels-Sicherheitslogo.
- Bestelleingang (Bestellnummer, Patient, Arzneimittel, ggf. E-Rezept-Token).
- Beratungsprotokoll (telefonisch oder schriftlich), Identitätsnachweis Empfänger.

## Rechtlicher Rahmen

- **§ 11a ApoG:** Versandhandelserlaubnis für apothekenpflichtige Arzneimittel; Voraussetzungen — Apothekenerlaubnis, QM-System, Beratungsmöglichkeit, Transportbedingungen.
- **§ 73 AMG:** Verbringungsverbot, Ausnahmen.
- **§ 43 AMG:** Apothekenpflicht.
- **AMVV** und § 360 SGB V (E-Rezept-Pflicht).
- **VersandhandelsVO** (Rahmenvereinbarung GKV-Spitzenverband — Stand vom Anwender zu verifizieren).
- **Sicherheitslogo-VO** (DIMDI / BfArM-Register).
- **§ 7 HWG**, Werbeverbote.
- BGH und EuGH, staend. Rspr. zur grenzüberschreitenden Versand-Apotheke (DocMorris).

## / Schritt für Schritt

1. **Bestelleingang erfassen:** Datum, Patient, Arzneimittel, Lieferadresse, ggf. Rezept-Token.
2. **Verbots-Sortiment prüfen:**
 - BtM: kein Versand erlaubt (§ 11a Abs. 2 ApoG i.V.m. BtMG, ständige Praxis).
 - T-Rezept-Arzneimittel: kein Versand (vom Anwender zu verifizieren).
 - Bestimmte Kühlware bei nicht gesicherter Kühlkette: kein Versand.
3. **E-Rezept einlösen:** Token-Verarbeitung über TI-Anbindung (siehe Skill `e-rezept-ti-gematik-apothekenprozess`).
4. **Plausibilitätsprüfung:** Apotheker prüft Indikation, Dosierung, Kontraindikation.
5. **Beratung anbieten:** Bei jedem Versand muss Beratung erreichbar sein — Telefon, Chat, E-Mail; bei Rx Pflicht, bei OTC Angebot. Dokumentation muss revisionsfest sein.
6. **Aut-idem / Rabattvertrag** (siehe `substitution-rabattvertrag-aut-idem`).
7. **Versandvorgang:** Verpackung, Kühlkette, GDP-konformes Transportverfahren, Sendungsverfolgung.
8. **Lieferung:** Identitätsprüfung Empfänger bei Rx (Personalausweis-Foto, Kuriernachweis, Codeprüfung).
9. **Dokumentation:** Bestellnummer, Beratung, Versandbeleg, drei Jahre Aufbewahrung.

## Trade-off-Matrix

| Versandkonstellation | Zulässig | Beratung | Risiko |
|---|---|---|---|
| OTC apothekenpflichtig inländisch | ja | Beratungsangebot Pflicht | gering |
| Rx-GKV inländisch | ja, mit Erlaubnis § 11a ApoG | Pflichtberatung dokumentiert | mittel (Retax) |
| Rx aus EU-Apotheke an Patient in D | ja, bei Eintrag DEAS-Register | wie inländisch | mittel |
| BtM-Versand | nein | — | strafbewehrt |
| T-Rezept Versand | grds. nein | — | hoch |
| Kühlware ohne Kühlkette | nein | — | hoch |

## Praxistipps

- Beratungsangebot muss tatsächlich erreichbar sein — Hotline mit Öffnungszeiten, Chat mit Apothekerinnen, E-Mail-Antwort binnen 24 h.
- Sendungsverfolgung als Anti-Retax-Beweis archivieren.
- Bei Kühlware: zwischenliegende Kontrollpunkte mit Temperaturlogger, Lieferquittung mit Temperaturnachweis.
- DEAS-Eintrag bei EU-Versand prüfen; nicht-eingetragene EU-Apotheken sind in Deutschland nicht zugelassen.
- Werbeauftritt prüfen — HWG-Vorgaben gelten auch im Versandhandel; Aktionen ("Schenken statt nehmen") oft heikel.

## Mustertexte

### Beratungsprotokoll Versandhandel (Vorlage)
"Datum / Bestell-Nr.: [...] / Patient: [...] / Arzneimittel: [Name, Stärke, Menge] / E-Rezept-Token: [...] / Beratungsangebot ausgesprochen: [ja/nein] / Beratungsweg: [Telefon/Chat/E-Mail] / Inhalte: [Dosierung / Kontraindikation / Aufbewahrung / Nebenwirkungen] / Apotheker:in: [Name] / Versandbeleg-Nr.: [...]"

### Hinweis an Patient bei Versandverbot (Auszug)
"Sehr geehrte:r [Patient:in], das von Ihnen bestellte Arzneimittel [Name] gehört zu den Betäubungsmitteln nach BtMG. Ein Versand ist gesetzlich ausgeschlossen. Wir empfehlen Ihnen, dieses Arzneimittel persönlich in einer nahegelegenen Apotheke abzuholen. Selbstverständlich beraten wir Sie unter [Telefonnummer] zu Alternativen."

## Typische Fehler

- BtM versendet — Strafbarkeitsrisiko nach § 29 BtMG.
- Beratung nur "auf Wunsch" angeboten, aber kein Beratungskanal mit dokumentierter Erreichbarkeit.
- Kühlkette nicht überwacht — Insulin oder Biologika werden inaktiviert.
- EU-Versandapotheke ohne DEAS-Eintrag — Patient kauft, Apotheke wird wegen unerlaubten Versands verfolgt.
- Identitätsprüfung Empfänger bei Rx-Versand fehlt — Doppelabgabe an Dritte.

## Quellen Stand 06/2026

- ApoG § 11a; AMG §§ 43, 73; AMVV; SGB V § 360.
- BfArM DIMDI-Sicherheitslogo-Register; DEAS-Register EU-Versandapotheken.
- BGH staend. Rspr. zum Apothekenversand und Wettbewerbsrecht.
- EuGH staend. Rspr. zur Grenzüberschreitung (DocMorris).
- ABDA-Hinweise zum Versandhandel (vom Anwender zu verifizieren).

