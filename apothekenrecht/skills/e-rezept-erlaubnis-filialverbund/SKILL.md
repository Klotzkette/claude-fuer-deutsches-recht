---
name: e-rezept-erlaubnis-filialverbund
description: "E-Rezept TI Gematik Apothekenprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: ApoG, ApBetrO, AMG, AMPreisV, HWG, BtMG/BtMVV, SGB V, DSGVO, E-Rezept/TI-Hinweise, Landesaufsicht im Apothekenrecht."
---

# E-Rezept TI Gematik Apothekenprozess

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: E-Rezept TI Gematik Apothekenprozess
- **Normen-/Quellenanker:** ApoG, ApBetrO, AMG, BtMG, SGB V, Heilmittelwerberecht, Versandhandel, Rezept/Retaxation, Heimversorgung und Aufsicht.
- **Entscheidende Weiche:** Apothekenbetrieb, Abgabe, Rezept, Verantwortlichkeit, Dokumentation, Aufsicht, Retaxation und Patientensicherheit getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Worum geht es konkret

Seit dem 01.01.2024 ist das E-Rezept für apothekenpflichtige Fertigarzneimittel in der GKV-Versorgung verpflichtend (§ 360 SGB V). Der Skill behandelt: Einlösewege (eGK, Token-Ausdruck, App), TI-Konnektivität, Signaturprüfung, Ersatzverfahren bei Störung, Datenschutz, Apothekenpflichten gegenüber Gematik, Krankenkasse und Aufsicht. BtM- und T-Rezept sind bisher noch papierbasiert (Stand zu verifizieren).

## Wann dieses Modul hilft / Kaltstart-Fragen

- E-Rezept lässt sich nicht einlösen — TI-Störung oder Defekt der eGK.
- Retax wegen E-Rezept-Formfehler oder Doppelabgabe.
- Anfrage Aufsicht zur TI-Konformität.
- Schulung neuer Mitarbeiter zum E-Rezept-Workflow.
- Datenschutz: Patient verlangt Auskunft über E-Rezept-Verarbeitung.

Eingaben:
- E-Rezept-Token (QR-Code-Ausdruck oder über App), eGK des Patienten.
- Apothekenkartenlesegerät, Konnektor, gSMC-K, HBA.
- Apotheken-Warenwirtschaftssystem mit TI-Integration.
- TI-Störungsmeldung (sofern vorhanden) Gematik / IT-Dienstleister.

## Rechtlicher Rahmen

- **§ 360 SGB V:** E-Rezept-Pflicht ab 01.01.2024 für apothekenpflichtige Fertigarzneimittel zu Lasten GKV.
- **§§ 311 ff. SGB V:** Telematikinfrastruktur (TI), Gematik als Verantwortliche.
- **§ 312 SGB V:** Verarbeitung medizinischer Daten in der TI.
- **Gematik-Spezifikationen** (TI-Spec): Konnektor, eGK, HBA, gSMC-K, E-Rezept-Fachdienst.
- **DSGVO Art. 9:** Gesundheitsdaten — strengere Rechtfertigung erforderlich.
- **§ 7 ApBetrO:** Pharmazeutische Letztverantwortung; bei TI-Störung kein Ersatzweg ausserhalb der Regelungen.
- **§ 129 SGB V:** Rahmenvertrag, Retaxation bei formalen Fehlern.

## / Schritt für Schritt

1. **Einlösung:** Patient legt eGK ein, scannt Token (App), gibt Ausdruck mit QR-Code. Apothekensoftware ruft Rezept vom Fachdienst ab.
2. **Signaturprüfung:** Qualifizierte elektronische Signatur des Arztes wird automatisch verifiziert.
3. **Plausibilitätsprüfung** (analog Papierrezept, siehe `arzneimittelabgabe-verschreibungspflicht`).
4. **Aut-idem / Rabattvertrag** (siehe `substitution-rabattvertrag-aut-idem`).
5. **Aushändigung + Quittung:** Quittung über E-Rezept-Fachdienst zurück.
6. **Dokumentation:** Im Warenwirtschaftssystem; Token wird nach Einlösung im Fachdienst gesperrt.
7. **TI-Störung — Ersatzverfahren:** Bei Ausfall TI-Konnektor folgt nach Gematik-Vorgabe das "Ersatzverfahren" — Patient erhält ggf. Papierausdruck, Apotheke dokumentiert Ausfallzeitfenster. Bei länger andauerndem Ausfall: Rücksprache Krankenkasse zur Retaxprävention.
8. **Datenschutz:** Patient hat Auskunfts- und Löschanspruch (Art. 15, 17 DSGVO). E-Rezept-Token-Daten unterliegen Gesundheitsdatenschutz.

## Trade-off-Matrix

| Einlöseweg | Technischer Aufwand | Datenschutz | Verfügbarkeit |
|---|---|---|---|
| eGK direkt am Lesegerät | gering | strikt geschützt | nur in Apotheke |
| Token-Ausdruck | sehr gering | OK | überall |
| App (gematik) | mittel | OK | Smartphone notwendig |
| Vorabreservierung Online-Apotheke | hoch | DSGVO-pflichtig | Patient bestimmt |

## Praxistipps

- TI-Konnektor und HBA-Karte regelmässig aktualisieren — Zertifikate laufen ab. Verlängerung rechtzeitig planen.
- Bei TI-Ausfall: Tagesprotokoll mit Beginn/Ende der Störung und betroffenen Vorgängen. Krankenkasse nachweisen können.
- Patient-App: Apotheke benötigt keinen Zugriff auf personenbezogene App-Daten. Token-Scan reicht.
- Datenschutzdokumentation: TI-Verarbeitung im Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO) anlegen.
- BtM und T-Rezept bleiben aktuell papierbasiert; E-BtM ist angekündigt — Anwender muss aktuellen Stand verifizieren.

## Mustertexte

### Dokumentation TI-Ausfall (Auszug)
"TI-Störung am [Datum, Beginn ... Ende]. Apotheke konnte E-Rezept-Einlösung nicht durchführen. Patienten wurden gebeten, Token-Ausdruck mitzubringen / Folge-Termin zu vereinbaren. Notfallabgaben nach § 4 AMVV erfolgten in [N] Fällen; Folgerezepte werden eingefordert. Störung wurde an IT-Dienstleister [Name] um [Uhrzeit] gemeldet, Ticket-Nummer [X]."

### Auskunft an Patient nach Art. 15 DSGVO (Auszug)
"Sehr geehrte:r Frau/Herr [Patient:in], hiermit erhalten Sie auf Ihren Antrag vom [Datum] Auskunft zu den über Sie in unserer Apotheke gespeicherten Daten: 1. E-Rezept-Abrufdaten im Zeitraum [...], 2. abgegebene Arzneimittel und Beratung, 3. Speicherdauer und Rechtsgrundlage (§ 312 SGB V, Art. 9 Abs. 2 lit. h DSGVO). Eine Datenkopie ist beigefügt (Anlage [Nr.])."

## Typische Fehler

- Papierrezept gelangt nach gestelltem E-Rezept zur Einlösung — Doppelabgabe, Retax.
- Apotheke löst Rezept zu früh ein (Pre-Lock); System lässt Patient nicht mehr wechseln — DSGVO- und Wettbewerbsproblem.
- TI-Störung nicht dokumentiert; Krankenkasse retaxiert wegen "ungültiger" Abgabe.
- HBA-Zertifikat abgelaufen — Apotheker:in kann keine eigenen Quittungen signieren.
- Patient erteilt App-Zustimmung zur "Vorabreservierung" bei einer bestimmten Versandapotheke; lokale Apotheke fängt Patient nicht ab — Wettbewerbsfrage.

## Quellen Stand 06/2026

- SGB V §§ 311, 312, 360 — aktueller Stand im BMG-Veröffentlichungsverzeichnis.
- Gematik-Spezifikationen TI-Konnektor und E-Rezept-Fachdienst (vom Anwender zu verifizieren — Versionsstand).
- BfArM und BSI-Hinweise zur TI-Sicherheit.
- DSGVO Art. 9, 30; BDSG-neu §§ 22, 26 (vom Anwender zu verifizieren — laufende Anpassungen).
- ABDA-Rundschreiben zur E-Rezept-Praxis (vom Anwender zu verifizieren).

