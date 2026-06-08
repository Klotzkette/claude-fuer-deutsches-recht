---
name: chirurgie-und-op-robotik
description: "Prüft OP- und Chirurgierobotik: MDR-Klasse, klinische Bewertung, Vigilanz, Betreiber, Aufklärung, Wartung und Behandlungsfehlernähe."
---

# Chirurgie- und OP-Robotik

## Fachkern: Chirurgie- und OP-Robotik
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

OP- und Chirurgieroboter sind regelmäßig Medizinprodukte hoher Risikoklasse (MDR Klasse IIb/III). Ihr rechtlicher Rahmen ist die MDR VO (EU) 2017/745 und das nationale MPDG, ergänzt um den Behandlungsvertrag (§§ 630a ff. BGB), das ärztliche Berufsrecht, die KI-VO (bei autonomen oder unterstützenden KI-Funktionen), die DSGVO (Patientendaten) und das ProdHaftG/VO (EU) 2024/2853. Dieser Skill ordnet die Pflichten von Hersteller, Krankenhaus und Operateur sowie typische Risikofelder: Aufklärung über Roboter-Beteiligung, Schulungsstand des Operateurs, Wartungspflichten, Vigilanz-Meldungen, Behandlungsfehlernähe.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Krankenhausträger, Chefarzt/Operateur, MPDG-Beauftragter, Patient/Angehörige, Versicherer, BfArM, Notified Body.
2. **Robotertyp:** telemanipuliert (z. B. da-Vinci-Architektur), teilautonom, vollautonom für definierte Schritte; mit oder ohne KI-Unterstützung.
3. **Eingriffstyp:** Urologie, Gynäkologie, Allgemeinchirurgie, Orthopädie, Neurochirurgie.
4. **Anlass:** Inverkehrbringen, Vigilanz-Vorfall, Behandlungsfehlervorwurf, Schulungslücke, Wartungsversäumnis, BfArM-Inspektion.
5. **Unterlagen:** EU-Konformitätserklärung, klinische Bewertung, Vigilanz-Berichte, Wartungsprotokolle, Schulungsnachweise, OP-Berichte, Logs.

## Rechtlicher Rahmen

- **MDR** VO (EU) 2017/745: Art. 5 ff. Konformität, Art. 52 ff. Bewertung, Art. 87 ff. Vigilanz, Anhang VIII Klassifizierung.
- **MPDG** §§ 4 ff. Pflichten Wirtschaftsakteure, §§ 14 ff. Betreiber, §§ 35 ff. Vigilanz.
- **MPBetreibV** Pflichten Betreiber, insb. § 3 Einweisung, § 6 Bestandsverzeichnis, § 11 sicherheitstechnische Kontrollen.
- **BGB** §§ 630a, 630c, 630e (Aufklärung), 630f (Dokumentation), 630h (Beweislastregeln).
- **§§ 823, 831 BGB** und ärztliche Haftung; ständige Rspr. BGH (Aufklärung, voll beherrschbare Risiken).
- **KI-VO** Anhang III bei sicherheitskritischer KI-Funktion; integrierte Konformitätsbewertung mit MDR.
- **DSGVO** Art. 9 Patientendaten; § 22 BDSG.
- **VO (EU) 2024/2853** Produkthaftung.

## Schritt für Schritt

1. **MDR-Klassifizierung.** Klasse IIb/III? Software als Medizinprodukt (SaMD) gesondert? Kombiprodukt?
2. **Konformitätsbewertung.** Modul nach Anhang IX/X MDR; Benannte Stelle eingebunden.
3. **Klinische Bewertung** und ggf. klinische Prüfung Art. 62 ff. MDR.
4. **Vigilanz-System.** Schwere Vorkommnisse Art. 87 MDR binnen 15 Tagen; FSCA (Field Safety Corrective Actions); FSN (Field Safety Notice).
5. **Krankenhaus-Pflichten.** Einweisung der Anwender § 3 MPBetreibV; Wartungsplan; sicherheitstechnische Kontrollen; medizinprodukterechtliche Risikobewertung in der OP.
6. **Aufklärung des Patienten** §§ 630c, 630e BGB: Art und Tragweite des Eingriffs, Roboter-Beteiligung, Alternativen, spezifische Risiken; Erfahrung des Operateurs.
7. **Dokumentation** OP-Bericht inkl. Robotik-Parameter, Software-Version, Vorfälle.
8. **Schadenfall**. Spurensicherung der Logs, Wartungsdokumente, Schulungsnachweise.

## Trade-off-Matrix

| Frage | Konservativ | Aggressiv | Empfehlung |
|---|---|---|---|
| Aufklärung "Roboter" | ausführlich, mit Erfahrungsstand des Operateurs | knapp | ausführlich; insb. bei neuer Methode |
| Schulungspflicht | volle MDR-Einweisung + simulationsbasiert | Hersteller-Schulung mit Kurzeinweisung | mindestens nachweisbare Mindeststunden + Fallzahl |
| KI-Funktion an/aus | aus, wenn nicht zertifiziert | an im Pilotmodus | nur dokumentiert nach Risikobewertung |
| Vigilanz-Meldung | proaktiv | nur bei klarer Schwelle | proaktiv bei Verdacht; Risk-of-Underreporting |

## Praxistipps

- **Schulungsmatrix** pro Operateur mit Fallzahlen und Versionsstand.
- **Logs als ärztliche Dokumentation** archivieren – nach § 630f BGB 10 Jahre, MDR 15 Jahre Art. 10 Abs. 8.
- **Aufklärung 24 h vor Eingriff** dokumentieren.
- **OP-Team-Briefing** vor Robotik-OPs; Notfall-Konvertierung.
- **OT-Sicherheit**: Roboter-Netzsegment, kein Internet, NIS-2-Schnittstelle.

## Mustertexte

**Aufklärungsbogen Auszug:**

> Sie werden mit dem Operationsroboter Typ XY (Hersteller: ABC, Modell-/Versionsstand: …) operiert. Der Operateur Dr. Z hat im System bisher [n] Eingriffe Ihrer Art durchgeführt; die statistische Lernkurve dieses Eingriffs liegt nach Hersteller- und Studienangaben bei etwa [n] Eingriffen für stabile Komplikationsraten. Im seltenen Fall eines Roboter-Ausfalls wird auf den konventionellen offenen oder laparoskopischen Eingriff konvertiert. Spezifische Roboter-Risiken: thermische Verletzungen durch Elektrokoagulation, Trokar-Verletzungen, vorübergehende Position-Tracking-Verluste. Alternativen: offene OP, laparoskopisch konventionell.

**Vigilanz-Meldung (Auszug):**

> Schweres Vorkommnis nach Art. 87 MDR vom [Datum]: Während laparoskopischer Nephrektomie kam es zu einem unerwarteten Stillstand des Roboter-Arms 3 nach Software-Update vom [Datum-1]. Konventionelle Konvertierung erfolgreich; Patient ohne dauerhafte Folgen. Logs gesichert. Sofortige FSN an alle Kliniken mit gleichem Modell. Korrekturmaßnahme: Rückrollen auf vorherige Software-Version. Statusupdate folgt fristgerecht.

## Typische Fehler

- **Aufklärung pauschal** – BGH verlangt patienten-/eingriffsspezifisch.
- **Schulungsstand nicht dokumentiert** – Behandlungsfehlervorwurf einfach.
- **Wartungsversäumnis** kann zur Beweislastumkehr nach § 630h BGB führen.
- **Vigilanz-Meldung zu spät** – MPDG-Bußgeld.
- **KI-Funktion ohne Konformitätsbewertung** in laufendem Eingriff aktiv.

## Querverweise

- `accuracy-robustness-cybersecurity-ai`
- `betreiber-mitverschulden-und-fehlbedienung`
- Plugin-Nachbar `medizinrecht` für Behandlungsvertrag

## Quellen Stand 06/2026

- VO (EU) 2017/745 (MDR), Art. 5, 10, 52, 62, 87; Anhang VIII.
- MPDG; MPBetreibV.
- BGB §§ 630a-h.
- VO (EU) 2024/1689 (KI-VO), Anhang III.
- VO (EU) 2024/2853 (neue ProdHaftRL).
- DSGVO Art. 9; BDSG § 22.
- Live-Verifikation auf eur-lex.europa.eu, bfarm.de, dimdi/bfarm; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
