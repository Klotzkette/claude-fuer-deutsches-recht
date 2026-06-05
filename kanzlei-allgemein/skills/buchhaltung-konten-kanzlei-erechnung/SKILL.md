---
name: buchhaltung-konten-kanzlei-erechnung
description: "Buchhaltung Konten Kanzlei Erechnung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Buchhaltung Konten Kanzlei Erechnung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Buchhaltung Konten Kanzlei Erechnung** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-buchhaltung-konten` | Kanzlei-Buchhaltung mit Geschäftskonto offenen Posten Debitoren Kreditoren und Bankmatching. Anwendungsfall Anwalt oder Kanzleibuero will Zahlungseingang prüfen offene Posten abgleichen oder Buchhaltungsuebergabe an DATEV vorbereiten. Normen GoBD § 147 AO Aufbewahrung § 556b BGB. Prüfraster Kontenbewegungen Rechnungsalter Mahnwesen Bankmatching Klaerfaelle DATEV-Export. Output Offene-Posten-Liste Debitoren-Kreditoren-Übersicht Bankmatching-Protokoll DATEV-Übergabepaket. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-buchhaltung. |
| `kanzlei-allgemein-erechnung` | Elektronische Kanzleirechnung in XRechnung oder ZUGFeRD vorbereiten und validieren. Anwendungsfall Mandant oder öffentliche Hand verlangt Rechnung im Format XRechnung oder ZUGFeRD. Normen EN 16931 GoBD § 14 UStG Rechnungspflichtangaben. Prüfraster Pflichtdaten EN 16931 XML-Strukturvalidierung PDF-A-3-Hybrid bei ZUGFeRD GoBD-Aufbewahrung Rechnungskorrektur. Output Validierte XRechnung oder ZUGFeRD-Datei mit Freigabeprotokoll. Abgrenzung zu kanzlei-allgemein-rechnung (allgemeine Rechnungserstellung) und kanzlei-allgemein-ustva-buchhaltung. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Buchhaltung Konten Kanzlei Erechnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-buchhaltung-konten`

**Fokus:** Kanzlei-Buchhaltung mit Geschäftskonto offenen Posten Debitoren Kreditoren und Bankmatching. Anwendungsfall Anwalt oder Kanzleibuero will Zahlungseingang prüfen offene Posten abgleichen oder Buchhaltungsuebergabe an DATEV vorbereiten. Normen GoBD § 147 AO Aufbewahrung § 556b BGB. Prüfraster Kontenbewegungen Rechnungsalter Mahnwesen Bankmatching Klaerfaelle DATEV-Export. Output Offene-Posten-Liste Debitoren-Kreditoren-Übersicht Bankmatching-Protokoll DATEV-Übergabepaket. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-buchhaltung.

# Kanzlei-Buchhaltung, Konten und Zahlungsabgleich

## Triage zu Beginn
1. Geht es um Ausgangsrechnungen, Eingangsrechnungen, Fremdgeld/Anderkonto oder Bankmatching?
2. Ist eine echte Buchhaltungssoftware (DATEV, Lexware, sevDesk) angebunden oder wird im Simulationsmodus gearbeitet?
3. Sind offene Posten ueberfaellig und loest das Mahnwesen aus?
4. Werden Fremdgelder kanzleiintern von eigenen Geldern getrennt gefuehrt (§ 43a Abs. 5 BRAO)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 5 BRAO — Pflicht zur Trennung von Fremdgeld und eigenem Vermoegen
- §§ 238-241 HGB — Buchfuehrungspflicht: Grundsaetze ordnungsmaessiger Buchfuehrung
- § 147 AO — Aufbewahrungspflichten fuer Buchungsbelege (10 Jahre)
- § 286 BGB — Verzug: Voraussetzungen und Verzugszinsen bei offenen Posten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt die operative Kanzlei-Buchhaltung als Vorbereitung: Ausgangsrechnungen, Eingangsrechnungen, offene Posten, Geschäftskonto, Zahlungseingänge, Zahlungsausgänge, Bankmatching, Mahnwesen und Klärfälle. Er bucht nicht verbindlich und löst keine Bankzahlungen aus.

## Leitplanken

- Echte Geschäftskonto-Anbindung nur nach ausdrücklicher Freigabe.
- Keine Bankzugangsdaten, TANs, PINs oder API-Secrets im Chat speichern.
- Keine Zahlungsaufträge ohne separate Freigabe.
- Keine endgültige Buchung ohne Buchhaltungs- oder Steuerkanzlei-Fachsystem.
- Fremdgeld, Anderkonto, Gerichtskosten und Auslagen getrennt prüfen.
- DATEV-ähnliche Übergabe nur als strukturierte Exportvorbereitung oder Simulation, nicht als echte DATEV-Buchung behaupten.

## Datenquellen

- Ausgangsrechnungen und E-Rechnungen.
- Eingangsrechnungen.
- Kontoauszüge, CSV, CAMT, MT940, PDF oder Bank-Screenshot.
- Zahlungsavise.
- Rechtsschutz-Zahlungen.
- Fremdgeldvermerke.
- Mahnungen und Zahlungserinnerungen.
- Storno, Gutschrift, Korrekturrechnung.

## Offene-Posten-Workflow

1. Ausgangsrechnung in Debitorenregister übernehmen.
2. Fälligkeit, Zahlungsziel und Mahnstufe setzen.
3. Alterung berechnen: nicht fällig, 0-30, 31-60, 61-90, über 90 Tage.
4. Zahlungseingänge importieren oder simulieren.
5. Matching vorschlagen.
6. Klärfälle markieren.
7. Mahnvorschlag oder Rückfrage erzeugen.
8. Zahlungsstatus an Rechnung, UStVA und GoBD-Protokoll zurückgeben.

## Matching-Regeln

Starkes Match:

- Rechnungsnummer im Verwendungszweck.
- Betrag stimmt.
- Zahler passt zu Rechnungsempfänger oder Kostenschuldner.
- Zahlung innerhalb erwarteter Frist.

Schwaches Match:

- Betrag stimmt, aber Rechnungsnummer fehlt.
- Zahler ist abweichender Dritter, Rechtsschutz oder Mandant.
- Teilzahlung.
- Sammelzahlung.
- Rundungs- oder Bankgebührenabweichung.

Klärfall:

- Betrag passt zu keiner Rechnung.
- Zahlung auf falsche Akte.
- Doppelzahlung.
- Fremdgeldverdacht.
- Rücklastschrift.
- Name ähnlich, aber unsicher.

## Geschäftskonto-Simulation

Wenn kein Bankzugang besteht:

> Das Geschäftskonto ist nicht angeschlossen. Soll ich einen Import aus CSV/CAMT/MT940 vorbereiten, eine manuelle Kontoauszugsliste nutzen oder einen simulierten Zahlungslauf für die Testakte durchführen?

Im Simulationsmodus:

- Jede Zahlung als simuliert markieren.
- Keine echte Bankverbindung behaupten.
- Keine echten Kontostände behaupten.
- Matching-Entscheidungen nur als Vorschlag ausgeben.

## Ausgabe

- `assets/templates/buchhaltung-kontoauszug.md`.
- `assets/templates/offene-posten-debitoren.md`.
- `assets/templates/zahlungseingang-matching.md`.
- `assets/templates/mahn-und-klaerfallregister.md`.
- `assets/templates/datev-uebergabe-simulation.md`.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

## 2. `kanzlei-allgemein-erechnung`

**Fokus:** Elektronische Kanzleirechnung in XRechnung oder ZUGFeRD vorbereiten und validieren. Anwendungsfall Mandant oder öffentliche Hand verlangt Rechnung im Format XRechnung oder ZUGFeRD. Normen EN 16931 GoBD § 14 UStG Rechnungspflichtangaben. Prüfraster Pflichtdaten EN 16931 XML-Strukturvalidierung PDF-A-3-Hybrid bei ZUGFeRD GoBD-Aufbewahrung Rechnungskorrektur. Output Validierte XRechnung oder ZUGFeRD-Datei mit Freigabeprotokoll. Abgrenzung zu kanzlei-allgemein-rechnung (allgemeine Rechnungserstellung) und kanzlei-allgemein-ustva-buchhaltung.

# E-Rechnung, XRechnung, ZUGFeRD und GoBD


## Triage zu Beginn
1. Wer ist der Rechnungsempfaenger: Verbraucher (B2C), Unternehmen (B2B) oder oeffentliche Stelle (B2G)?
2. Welches Format ist erforderlich oder gewuenscht: XRechnung, ZUGFeRD 2.3 oder klassisches PDF?
3. Liegt eine Leitweg-ID oder Buyer Reference des Empfaengers vor (Pflicht bei B2G)?
4. Welcher Versandweg ist vorgesehen: E-Mail, Peppol-Netzwerk, Portal oder Mandantenportal?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 14 UStG — Pflichtangaben auf Rechnungen; Pflicht zur E-Rechnung ab 2025 fuer B2B
- EN 16931 — Europaeische Norm fuer elektronische Kernrechnungen; Grundlage von XRechnung und ZUGFeRD
- § 14b UStG — Aufbewahrungspflicht fuer Rechnungen (10 Jahre, GoBD-konform)
- § 10 RVG — Pflichtangaben auf der anwaltlichen Honorarrechnung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ergänzt `kanzlei-allgemein-rechnung`, sobald eine Rechnung als E-Rechnung erstellt, geprüft, archiviert oder versandt werden soll. Er erzeugt keine Steuerberatung und keine finale Buchung, sondern ein prüfbares Datenblatt, eine Formatentscheidung und eine Validierungs- und Archivierungscheckliste.

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
