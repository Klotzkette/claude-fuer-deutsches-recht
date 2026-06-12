---
name: dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii
description: "Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art: 5 Abs. 2 DSGVO: Aktenstruktur Versionierung Aufbewahrung Beweiswert. Output: DSFA-Akte mit Aktenuebersicht und Aufbewahru..."
---

# Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO: Aktenstruktur Versionierung Aufbewahrung Beweiswert. Output: DSFA-Akte mit Aktenuebersicht und Aufbewahrungsregeln.

### DSFA-Dokumentation und Rechenschaftspflicht

## Wann dieses Modul hilft

- Nach Abschluss einer DSFA, vor Archivierung
- Bei Aufsichtsanfrage zur Vorlage der DSFA
- Bei Audit durch DSB oder externen Prüfer
- Bei Wechsel des DSB oder des Verantwortlichen — Aktenuebergabe
- Bei wesentlicher Änderung (Versionierung)

## Rechtlicher Rahmen

- Art. 5 Abs. 2 DSGVO: Rechenschaftspflicht — der Verantwortliche muss die Einhaltung der Grundsaetze nachweisen können.
- Art. 24 DSGVO: Verantwortung des für die Verarbeitung Verantwortlichen.
- Art. 30 DSGVO: Verzeichnis von Verarbeitungstaetigkeiten — DSFA-Verweis.
- Art. 35 Abs. 11 DSGVO: Re-Prüfungspflicht.
- Art. 58 Abs. 1 lit. a DSGVO: Auskunftsbefugnis der Aufsicht.
- § 257 HGB, § 147 AO für Aufbewahrungsfristen kaufmaennischer und steuerlicher Unterlagen — DSFA ist nicht kaufmaennisches Dokument, aber an die Verarbeitungstaetigkeit gekoppelt.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welcher Verarbeitungsvorgang? Eindeutige Akten-Identifikation (z. B. VV-Nummer, DSFA-Aktenzeichen).
2. **Verhältnismäßigkeitspruefung.** Prüfung welche Dokumente in die DSFA-Akte gehoeren — Vollstaendigkeit ohne Ueberfrachtung.
3. **Risikoanalyse.** Beweiswertrisiken prüfen — fehlende Unterschriften, fehlende Versionen, fehlende Datierungen, unklare Verantwortlichkeiten.
4. **Maßnahmen.** Strukturierte Aktenfuehrung in standardisierter Form (digital signiert, mit Datum und Versionierung).
5. **Restrisiko.** Beweiswertbeurteilung — wie sicher ist die DSFA bei Aufsichtsverfahren? Ergaenzungen oder Bekraeftigungen.
6. **Konsultation / Genehmigung.** DSB bestaetigt Vollstaendigkeit; Aufbewahrung und Zugriffsrechte regeln.

## Aktenstruktur DSFA

```
DSFA-AKTE Aktenzeichen: [VV-XX-DSFA-YYYY-NN]
Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]
DSB: [NAME]

01 Deckblatt mit Versionshistorie
02 Schwellwertanalyse / Triage-Vermerk (Skill dsfa-art-35-dsgvo-trigger-und-anwendungsbereich)
03 Listenabgleich (Skill dsfa-bfdi-und-laender-blacklist)
04 WP-248-Pruefung (Skill dsfa-edpb-leitlinien-9-19-anwendung)
05 Methodenwahl-Memo (Skill dsfa-methodik-cnil-pia-vs-bsfd-bsi)
06 Vollstaendige DSFA (Skill dsfa-template-deutsch-vollvorlage)
07 Risikomatrix (Skill dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden)
08 TIA falls Drittlandtransfer (Skill dsfa-für-internationale-datentransfers)
09 KI-FRIA falls Hochrisiko-KI (Skill dsfa-für-ki-systeme-schnittstelle-art-26-kivo)
10 Stakeholder-Konsultation (Skill dsfa-stakeholder-konsultation-art-35-9)
11 DSB-Stellungnahme
12 Vorabkonsultation Art. 36 (falls erfolgt)
13 Freigabe Verantwortlicher
14 Verweis Verarbeitungsverzeichnis Art. 30
15 Revisionsplan (Skill dsfa-update-bei-aenderungen-und-revision)
16 Korrespondenz mit Aufsichtsbehoerde (falls)
17 Beweismittel: Datenflussdiagramm, AVV, SCC, TOM-Konzept

Versionsverzeichnis
| Version | Datum | Aenderung | Autor | Freigabe |

Zugriffskonzept
- Lesend: [Liste der berechtigten Personen]
- Schreibend: [Verantwortlicher, DSB, dokumentierender Mitarbeiter]
- Aufsichtsbehoerde: auf Anforderung Vollzugriff
```

## Aufbewahrungsregeln

- DSFA muss waehrend der gesamten Dauer der Verarbeitungstaetigkeit aufbewahrt werden.
- Nach Ende der Verarbeitung mindestens für den Zeitraum etwaiger Anspruchsverjaehrungen (Art. 82 DSGVO; immaterieller Schaden) — Empfehlung: 5 Jahre nach Ende der Verarbeitung; bei öffentlichen Stellen oft 10 Jahre.
- Alte Versionen nicht loeschen, sondern archivieren.
- Bei Anbieterwechsel: Übergabe der Akte einschliesslich aller Versionen.
- Bei steuerlich relevanten Verarbeitungen ggf. § 147 AO 10 Jahre.

## Beweiswertkriterien

- Datierung und Unterschrift jedes Dokuments
- Versionierung und Änderungshistorie
- Klare Autorenschaft (Wer hat dokumentiert, wer hat beschlossen?)
- DSB-Anhörung dokumentiert mit Datum
- Quellenverzeichnis (Aufsichtshinweise, Leitlinien, Rechtsprechung)
- Verweis auf Verarbeitungsverzeichnis und AVV

## Typische Fehler

- DSFA wird im Mail-Anhang verteilt, aber nicht in einer strukturierten Akte gefuehrt.
- Versionen werden ueberschrieben — alte Versionen unwiederbringlich verloren.
- DSB-Stellungnahme nur muendlich — kein Nachweis.
- Aktenzeichen fehlt — DSFA nicht zuordenbar.
- Aufbewahrungsfrist nicht definiert — DSFA wird mit Mitarbeiter-Personalakte vernichtet.
- Zugriffsrechte ungeregelt — DSFA mit personenbezogenen Risikobeschreibungen offen einsehbar.
- Beweismittel (Datenflussdiagramm) nicht beigefuegt — DSFA bleibt abstrakt.

## Quellen Stand 06/2026

- Art. 5 Abs. 2 DSGVO
- Art. 24, 30, 35, 58, 82 DSGVO
- § 147 AO; § 257 HGB (Bezugsfristen)
- EDSA-Leitlinien WP 248 rev.01
- BfDI / Landesbehoerden — Hinweise zur Rechenschaftspflicht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
