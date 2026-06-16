---
name: erechnung
description: "Elektronische Kanzleirechnung in XRechnung oder ZUGFeRD vorbereiten und validieren. Anwendungsfall Mandant oder öffentliche Hand verlangt Rechnung im Format XRechnung oder ZUGFeRD. Normen EN 16931 GoBD § 14 UStG Rechnungspflichtangaben. Prüfraster Pflichtdaten EN 16931 XML-Strukturvalidierung PDF..."
---

# E-Rechnung, XRechnung, ZUGFeRD und GoBD

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Wer ist der Rechnungsempfaenger: Verbraucher (B2C), Unternehmen (B2B) oder öffentliche Stelle (B2G)?
2. Welches Format ist erforderlich oder gewuenscht: XRechnung, ZUGFeRD 2.3 oder klassisches PDF?
3. Liegt eine Leitweg-ID oder Buyer Reference des Empfaengers vor (Pflicht bei B2G)?
4. Welcher Versandweg ist vorgesehen: E-Mail, Peppol-Netzwerk, Portal oder Mandantenportal?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 14 UStG — Pflichtangaben auf Rechnungen; Pflicht zur E-Rechnung ab 2025 für B2B
- EN 16931 — Europaeische Norm für elektronische Kernrechnungen; Grundlage von XRechnung und ZUGFeRD
- § 14b UStG — Aufbewahrungspflicht für Rechnungen (10 Jahre, GoBD-konform)
- § 10 RVG — Pflichtangaben auf der anwaltlichen Honorarrechnung

## Grundentscheidung

Zuerst klären:

1. Rechnungsempfänger: Verbraucher, Unternehmer, öffentliche Stelle, Rechtsschutzversicherung, Dritter.
2. Bereich: B2B, B2G, B2C oder intern.
3. Formatwunsch oder Formatpflicht: XRechnung, ZUGFeRD, PDF, Papier, sonstiges Format.
4. Leitweg-ID oder Buyer Reference: nur erforderlich, wenn Empfänger oder B2G-Prozess sie verlangt.
5. Versandweg: E-Mail, Portal, Peppol, Mandantenportal, beA nur wenn passend.
6. Archivsystem: GoBD-konformes DMS, Kanzleisoftware, Dateisystem mit Verfahrensdokumentation oder Übergabe an Steuerkanzlei.

## Aktualitätscheck

Vor technischer Aussage zur Gültigkeit immer die aktuelle Format- und Validatorlage prüfen:

- XRechnung: aktuelle KoSIT-/XRechnung-Version und Validator-Konfiguration.
- B2G: aktuelle Vorgaben der jeweiligen Eingangsplattform, Leitweg-ID und Portal-/Peppol-Anforderungen.
- ZUGFeRD: aktuelles Profil, PDF/A-3-Anforderungen und XML-Profil.
- BMF-/USt-Hinweise zur E-Rechnung, soweit für B2B/B2G relevant.

Wenn diese Prüfung nicht durchgeführt wurde, nur `Validierung offen` ausgeben.

## Formate

### XRechnung

- Reines strukturiertes XML-Format.
- Für öffentliche Auftraggeber im B2G-Kontext zentral.
- Enthält keinen menschenlesbaren PDF-Rechnungsteil.
- Muss gegen den passenden XRechnung-Validator und die jeweils geltenden Geschäftsregeln geprüft werden.
- Bei B2G Empfängeranforderungen wie Leitweg-ID, Portal, Peppol und Attachments abfragen.

### ZUGFeRD

- Hybridformat aus PDF/A-3-Sichtrechnung und eingebetteter XML-Datei.
- Der strukturierte XML-Teil ist für E-Rechnungszwecke führend.
- Profil bewusst wählen: typischerweise EN 16931 oder ein zulässiges höheres Profil; MINIMUM und BASIC-WL nicht als vollwertige E-Rechnung behandeln.
- PDF und XML müssen inhaltlich konsistent sein.
- PDF/A-3-Validierung, XML-Validierung und Dateianhänge prüfen.

## Pflichtdaten

Für jede E-Rechnung eine Datenvollständigkeitsprüfung erstellen:

- Rechnungsnummer, Rechnungsdatum, Leistungsdatum oder Leistungszeitraum.
- Verkäufer: Name, Anschrift, Steuernummer oder USt-IdNr., Bankverbindung.
- Käufer: Name, Anschrift, Buyer Reference oder Leitweg-ID, soweit erforderlich.
- Akte, Mandant, Kostenschuldner und abweichender Rechnungsempfänger.
- Positionsdaten: Leistung, Menge oder Zeit, Einheit, Einzelpreis, Nettobetrag, Steuersatz, Steuerbetrag.
- RVG-Gebühren, Auslagen, Post- und Telekommunikationspauschale, Dokumentenpauschale, Gerichtskosten, Fremdgelder getrennt ausweisen.
- Vorschüsse, Zahlungen, Anrechnungen und Rechtsschutzanteile.
- Zahlungsziel, IBAN, Verwendungszweck.
- Steuerhinweise, Reverse Charge, Kleinunternehmer oder Steuerbefreiung nur nach Prüfung.

## GoBD-nahe Rechnungsakte

Vor Freigabe immer ein `GoBD-Prüfprotokoll` erzeugen:

1. Rechnungsversion eindeutig benennen.
2. Entwurfsfassung und freigegebene Fassung trennen.
3. Finales XML unverändert archivieren.
4. Bei ZUGFeRD zusätzlich PDF/A-3 und eingebettetes XML archivieren.
5. Validierungsbericht speichern.
6. Versandnachweis speichern.
7. Korrekturen nur als Storno, Gutschrift, Korrekturrechnung oder neue Rechnungsversion dokumentieren.
8. Zugriffsrechte, Änderungsprotokoll, Aufbewahrungsfrist und Exportfähigkeit notieren.

## Validierung

Keine finale E-Rechnung ohne:

- Formatentscheidung.
- Pflichtdatencheck.
- Summenprüfung netto, Steuer, brutto.
- Rundungsprüfung.
- Prüfung strukturierter Daten gegen die Sichtrechnung.
- Technische Validierung mit geeignetem Validator.
- Freigabe durch verantwortliche Person.

Wenn kein Validator verfügbar ist, nicht behaupten, dass die E-Rechnung gültig sei. Stattdessen einen `Validierung offen`-Vermerk und eine konkrete Tool-Anforderung ausgeben.

## Ausgabe

- `assets/templates/erechnung-datenblatt.md`.
- `assets/templates/gobd-rechnungsprotokoll.md`.
- Bei normaler Rechnungsarbeit zusätzlich `assets/templates/rechnungsdatenblatt.md`.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

