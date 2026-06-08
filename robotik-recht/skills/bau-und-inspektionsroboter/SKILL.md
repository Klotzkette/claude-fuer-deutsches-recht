---
name: bau-und-inspektionsroboter
description: "Prüft Bau-, Inspektions- und Wartungsroboter: Baustelle, Arbeitsschutz, Drittschäden, Betreiberorganisation und Beweissicherung."
---

# Bau- und Inspektionsroboter

## Fachkern: Bau- und Inspektionsroboter
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Bau- und Inspektionsroboter (Vermessungs-Roboter, Mauerwerks-, 3D-Druck-, Schweiß-, Tunnel-Inspektion, Rohrleitungs-Crawler, Drohnen-Vermessung, Fassaden-Reinigungsroboter) bewegen sich in einem Spannungsfeld zwischen BaustellV/SiGeKo, MaschinenVO, Arbeitsschutzrecht, Bauvertragsrecht (VOB/B), Versicherungsrecht und – bei Drittschäden – allgemeinem Deliktsrecht (§ 823 BGB) sowie Verkehrssicherungspflichten. Dieser Skill ordnet die Pflichten der Akteure (Bauherr, Generalunternehmer, Subunternehmer, Verleiher des Roboters), liefert Vorlagen für Baustellenanweisungen und gibt Hilfen zur Beweissicherung bei Vorfällen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Bauherr, Generalunternehmer, Subunternehmer, Verleiher des Roboters, Hersteller, SiGeKo, Versicherer, Geschädigter.
2. **Robotertyp:** 3D-Druck-Roboter Beton, Mauer-Robot, Tunnel-Inspektion, Brücken-Inspektion, Schweißroboter, Demontage-Roboter mit Hochdruckwasserstrahl.
3. **Standort:** Baustelle mit weiteren Gewerken, Tunnel, Brücke, Hochhaus, Industriestandort, öffentlicher Raum.
4. **Anlass:** Inverkehrbringen, Mietvertrag, Vorfall (Personenschaden, Sachbeschädigung am Bauwerk Dritter, Schaden am Baugrund), Schiedsverfahren, Versicherungsregress.
5. **Unterlagen:** Risikobeurteilung, SiGePlan, Bauvertrag, Liefer- und Mietverträge, Wartungs- und Inspektionsprotokolle, Telematik-Logs, Versicherungspolicen.

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 für Inverkehrbringen ab 20.01.2027 (vorher Maschinen-RL 2006/42/EG).
- **BaustellV** § 3 Koordinator (SiGeKo); RAB 31 (Regeln zum Arbeitsschutz auf Baustellen).
- **ArbSchG, BetrSichV, BauStellV, BGV/DGUV**: zu Baurobotik einschlägige Sicherheitsregelungen.
- **VOB/B** § 4 Ausführung, § 13 Mängelansprüche; ergänzend BGB Werkvertragsrecht §§ 631 ff., insb. § 633 Sach- und Rechtsmangel.
- **§ 823 BGB / § 836 BGB / § 906 BGB** für Drittschäden, Immissionen, Lärm, Erschütterungen.
- **ProdHaftG / VO (EU) 2024/2853** Hersteller, ggf. Quasi-Hersteller des Integrators.
- **KI-VO** bei autonomer Wahrnehmung; bei sicherheitskritischer Erkennung ggf. Hochrisiko Anhang III KI-VO.

## Schritt für Schritt

1. **Rollenmatrix.** Wer ist Hersteller, wer Integrator, wer Vermieter, wer Betreiber, wer Bauherr? Wer haftet im Außenverhältnis?
2. **Risikobeurteilung baustellenspezifisch.** Neben der Hersteller-Risikobeurteilung eine baustellenbezogene Beurteilung mit SiGeKo; Aufstellort, Bewegungsradius, Notabschaltung, Vandalismusrisiko.
3. **Koordination mit anderen Gewerken.** Schichtpläne, Sperrzonen, Lichtsignal, Funkkanäle, Eskalation.
4. **Drittschutz.** Absperrung; bei Außeneinsatz Verkehrssicherung; Lärm- und Erschütterungsmessungen vorab.
5. **Versicherung.** Bau-Betriebshaftpflicht prüfen; spezielle Robotik-Klausel; Selbstbehalt; Übermittlung der Risikoinformationen vor Einsatz.
6. **Vertragliche Pflichten.** Lieferverträge: Performance-Aufrüstung, Service-Level, Ersatzgeräte; Mietverträge: Wartungsstand, Übergabeprotokoll mit Fotos und Logauszug.
7. **Beweissicherung bei Vorfällen.** Logs unverzüglich sichern (Schreibsperre, Hash), Fotos, Augenzeugen, Notarprotokoll falls nötig, Sachverständiger zur Sicherung.
8. **Kommunikation.** Pressemeldung nur abgestimmt; gegenüber Polizei/Behörden sachlich und faktenbasiert.

## Trade-off-Matrix

| Spannungsfeld | Konservativ | Aggressiv | Empfehlung |
|---|---|---|---|
| Sperrzone | groß | knapp | Sperrzone ausreichend für Worst-Case-Bewegung plus Reaktionszeit |
| Telematik-Daten an Bauherr | offen | restriktiv | Live-Dashboard für Sicherheit, datensparsam für Performance |
| Personalbesetzung | Operator vor Ort | Remote | Bei autonomem Betrieb mind. ein Operator im 30-Sekunden-Eingriff |
| Mietzeitraum kurz | flexibel, höhere Kosten | lang, billiger | bei häufigem Standortwechsel kurz, bei einem Großprojekt lang |

## Praxistipps

- **SiGeKo früh einbeziehen** – auch bei Sub-Sub-Verträgen.
- **Wartungsplan dokumentieren** – Lückenlosigkeit ist Beweismittel.
- **Notfallübung** je Standort.
- **DSGVO bei Kamera-Sensorik**: Hinweisschild und Speicher-Konzept.
- **Klimaeinflüsse**: Sensoren unter Regen/Schnee unzuverlässig – Stilllegungsschwellen festlegen.

## Mustertexte

**Baustellenanweisung (Auszug):**

> Für den Einsatz des Roboters Typ Z auf Baustelle [BV-Nr.] gilt: Aufstellbereich gemäß Anlage 1 markiert (rot). Während Betriebs in diesem Bereich kein anderes Gewerk; Sperrgitter und Warnleuchten. Notabschaltung am Bediengerät und an drei festen Pulten. Im Vorfeld jedes Einsatzes Logauslese und Sichtkontrolle dokumentieren. Ansprechpartner Operator: Hr. Müller (+49…); Ansprechpartner SiGeKo: Fr. Schulz (+49…).

**Vertragsklausel (Mietvertrag Roboter):**

> Der Vermieter stellt den Roboter in einem MaschinenVO-konformen Zustand zur Verfügung; die EU-Konformitätserklärung, die Risikobeurteilung und die Betriebsanleitung in deutscher Sprache sind Bestandteil dieses Vertrages. Der Mieter stellt sicher, dass nur unterwiesenes Personal den Roboter bedient. Bei Vorfall mit Personenschaden hat der Mieter binnen 24 Stunden alle Logs und Wartungsprotokolle zu sichern und dem Vermieter zur Verfügung zu stellen.

## Typische Fehler

- **Hersteller-Risikobeurteilung als Baustellen-Beurteilung** verwendet.
- **Keine Sperrzone**, sondern nur visuelle Markierung.
- **SiGeKo nicht eingebunden** bei kurzem Einsatz.
- **Logs überschrieben** nach 24 h – Beweisverlust.
- **Wartung extern, aber ohne Übergabeprotokoll**.

## Querverweise

- `arbeitsschutz-betrsichv-robotik`
- `betreiber-mitverschulden-und-fehlbedienung`
- `deliktische-haftung-paragraph-823-bgb`

## Quellen Stand 06/2026

- VO (EU) 2023/1230 (MaschinenVO).
- BaustellV; RAB 31; ArbSchG; BetrSichV.
- VOB/B; BGB §§ 631 ff., §§ 823 ff.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- VO (EU) 2024/1689 (KI-VO).
- Live-Verifikation auf baua.de, bundesanzeiger.de, eur-lex.europa.eu; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
