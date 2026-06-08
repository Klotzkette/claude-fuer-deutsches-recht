---
name: ropa-richtlinien-monitor-art-controller-dsgvo
description: "Ropa Richtlinien Monitor ART Controller DSGVO im Datenschutzrecht: prüft konkret Datenschutzrichtlinien und Unternehmensanweisungen auf, Vollvorlage für das Verzeichnis von, Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten, RoPA-Besonderheiten bei besonderen Datenkategorien nach Art. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Ropa Richtlinien Monitor ART Controller DSGVO

## Arbeitsbereich

**Ropa Richtlinien Monitor ART Controller DSGVO** ordnet den Fall über die tragenden Prüfungslinien: Datenschutzrichtlinien und Unternehmensanweisungen auf, Vollvorlage für das Verzeichnis von, Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `richtlinien-monitor` | Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten gesetzliche Neuerungen Umsetzungsstatus. Output: Monitoring-Bericht Aenderungsliste. Abgrenzung: nicht für erstmalige Richtlinien-Erstellung. |
| `ropa-art-30-controller-deutsch-vorlage` | Vollvorlage für das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Tabellenstruktur mit allen sieben Mindestinhalten, ausgefuelltes Beispiel für Personalverwaltung, Mandantenakte, Kontaktformular, CRM. Direkt nutzbare Vorlage für Kanzleien und Unternehmen. |
| `ropa-art-30-dsgvo-grundlagen` | Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten nach Art. 30 DSGVO. Anwendungsbereich, Schwellenwert, Mindestinhalte Controller und Processor, Verhaeltnis zu § 70 BDSG, Vorlagepflicht gegenueber der Aufsichtsbehoerde. Einstiegs-Skill für das Records of Processing Activities (RoPA). |
| `ropa-bdsg-besondere-art-9-categories` | RoPA-Besonderheiten bei besonderen Datenkategorien nach Art. 9 DSGVO (Gesundheit, biometrische Daten, Religion, Gewerkschaftszugehoerigkeit), bei Beschaeftigtendaten § 26 BDSG und strafrechtlichen Verurteilungen Art. 10 DSGVO. Erhoehte Anforderungen an Zweckbestimmung, Erforderlichkeit, Rechtsgrundlage und TOMs. |
| `ropa-en-controller-template` | Full English-language template for the Records of Processing Activities (RoPA) of the controller under Article 30(1) GDPR. Seven mandatory contents, cover sheet, three worked examples (HR, client files, CRM with US sub-processor), and a versioning footer. Suitable for German law firms with international clients. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `richtlinien-monitor`

**Fokus:** Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten gesetzliche Neuerungen Umsetzungsstatus. Output: Monitoring-Bericht Aenderungsliste. Abgrenzung: nicht für erstmalige Richtlinien-Erstellung.

# Policy-Monitor – Drift-Monitoring Datenschutzerklärung

## Zweck

Zwei Modi: (1) **Sweep-Modus** – regelmäßiger Abgleich aller Datenschutz-Commitment-Flächen gegen aktuelle Verarbeitungspraxis, um Drift zu erkennen. (2) **Direkt-Modus** – für eine konkrete geplante Änderung prüfen, ob und wie die Datenschutzerklärung angepasst werden muss.

Typische Drifts: neue Tracking-Tool-Integration ohne Datenschutzerklärungsupdate, neuer Sub-AV ohne Empfängerlistenaktualisierung, verlängerte Speicherfristen ohne Ankündigung, neue Drittlandtransfers ohne Transfermechanismus in der Erklärung.

## Eingaben

- **Sweep-Modus:** Ausgabenordner aus `CLAUDE.md` (wo DSFAs, AVV-Reviews, Triage-Ergebnisse gespeichert sind), Datenschutzerklärungsquelle (URL oder Datei), Liste aktueller Verarbeitungstätigkeiten
- **Direkt-Modus:** Beschreibung der geplanten Änderung der Verarbeitungspraxis

## Ablauf – Sweep-Modus

1. **Commitment-Inventur.**
 Alle Datenschutz-Commitment-Flächen aus `CLAUDE.md` lesen:
 - Datenschutzerklärung (Haupt-URL / Dokument)
 - CMP / Cookie-Consent-Banner-Konfiguration
 - App-Store Privacy Labels
 - In-Produkt-Einwilligungsflows
 - Sektorspezifische Hinweise (TDDDG, KUG)

2. **Praxis-Inventur.**
 Aktuelle Verarbeitungspraxis aus Ausgaben des Plugins rekonstruieren:
 - Neueste AVV-Reviews (neue Sub-AVs, neue Drittlandtransfers)
 - Neueste DSFA-Ergebnisse (neue Verarbeitungstätigkeiten)
 - Neueste Triage-Ergebnisse (Rechtsgrundlagenänderungen)
 - Aus `CLAUDE.md` bekannte Systemliste und Drittlandsituation

3. **Drift-Analyse.**
 Für jede Commit-Fläche: Ist-Inhalt gegen Praxis-Inventur abgleichen.

 | Commit-Fläche | Praxis-Ist | Erklärung-Ist | Drift? | Schwere |
 |---|---|---|---|---|
 | Datenschutzerklärung – Empfänger | [aktuelle Liste] | [publizierte Liste] | Ja/Nein | 🔴/🟡/🟢 |
 | Cookie-Banner – Kategorien | [aktiv gesetzt] | [angekündigt] | Ja/Nein | … |
 | Speicherfristen | [tatsächlich] | [publiziert] | Ja/Nein | … |
 | Drittlandtransfer-Mechanismus | [aktuell] | [publiziert] | Ja/Nein | … |

4. **Drift-Klassifikation.**
 - 🔴 **Sofortiger Handlungsbedarf:** Verarbeitung erfolgt, die in der Erklärung nicht angekündigt ist → Informationspflicht-Verstoß Art. 13/14 DSGVO, potenziell rechtswidrige Verarbeitung.
 - 🟠 **Hoch:** Wesentliche Erweiterung des Verarbeitungsumfangs nicht reflektiert (z.B. neuer Zweck, neues Empfänger-Land).
 - 🟡 **Mittel:** Aktualisierung empfohlen, keine unmittelbare Rechtswidrigkeit (z.B. neue Formulierung genauer als nötig, aber nicht falsch).
 - 🟢 **Gering:** Kosmetische Anpassung, kein Handlungsdruck.

5. **Änderungsentwürfe.**
 Für jede 🔴- und 🟠-Drift: konkreten Textvorschlag für die Datenschutzerklärung formulieren (nicht als Meta-Kommentar, sondern als fertiger Erklärungstext).

6. **Sweep-Bericht.**
 Zusammenfassung: [N] Drifts, davon [N] 🔴, [N] 🟠, [N] 🟡; Änderungsvorschläge inline; Folgeaktionen.

## Ablauf – Direkt-Modus

1. Geplante Änderung der Verarbeitungspraxis beschreiben lassen.
2. Prüfen: Welche Art. 13/14 DSGVO-Pflichtinformationen sind betroffen?
 - Neue Datenkategorie → Art. 13 Abs. 1 lit. c DSGVO
 - Neuer Zweck → Art. 13 Abs. 1 lit. c DSGVO
 - Neuer Empfänger → Art. 13 Abs. 1 lit. e DSGVO
 - Neue Speicherfrist → Art. 13 Abs. 2 lit. a DSGVO
 - Neues Drittland → Art. 13 Abs. 1 lit. f DSGVO
3. Prüfen: Ändert sich die Rechtsgrundlage (Art. 6/9 DSGVO)? Muss ggf. neue Einwilligung eingeholt werden?
4. Prüfen: Ist eine DSFA erforderlich? (Weiterleitung an `dsfa-erstellung` anbieten)
5. Änderungsentwurf für betroffene Abschnitte der Datenschutzerklärung erstellen.
6. Prüfen: Erfordern App-Store-Labels oder Cookie-Banner-Konfiguration Anpassung?

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 13 DSGVO (Informationspflicht bei Datenerhebung bei Betroffenen)
- Art. 14 DSGVO (Informationspflicht bei Datenerhebung nicht bei Betroffenen)
- Art. 5 Abs. 1 lit. a DSGVO (Transparenzgrundsatz)
- Art. 12 DSGVO (Transparente Information)
- §§ 19, 25 TDDDG (Einwilligung Endgerätezugriff, Cookie-Einwilligung)
- EDSA-Leitlinien 03/2022 zu Dunklen Designmustern (Consent-Flows)
- EDSA-Leitlinien 05/2020 zu Einwilligung
- Paal, in: Paal/Pauly, DSGVO/BDSG, 3. Aufl. 2021, Art. 13 Rn. 1 ff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

**Sweep-Modus:**
1. Sweep-Datum und geprüfte Quellen
2. Drift-Tabelle (alle Flächen × alle Dimensionen)
3. Drift-Klassifikation mit Schwere
4. Priorisierte Änderungsvorschläge (druckfertige Textbausteine, keine Kommentare im Erklärungstext)
5. Sweep-Folgeaktionen

**Direkt-Modus:**
1. Betroffene Art. 13/14-Pflichten
2. Rechtsgrundlagen-Check
3. DSFA-Hinweis (falls einschlägig)
4. Änderungsentwurf für Datenschutzerklärung (Textbausteine)

## Beispiel (Direkt-Modus)

**Geplante Änderung:** Das Unternehmen möchte einen neuen Analytics-Anbieter mit Sitz in den USA integrieren (bisher EU-only).

**Analyse:**
- Neue Datenkategorie: Nein (Nutzungsverhalten bereits erfasst).
- Neuer Empfänger (Drittland USA): **Ja** – Art. 13 Abs. 1 lit. f DSGVO (Drittlandtransfer mit Transfermechanismus angeben).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Consent-Management: Ist der Anbieter nur nach Einwilligung aktiv (§ 25 TDDDG)? Dann Cookie-Banner anpassen (neue Kategorie / neuer Anbieter).
- DSFA: `anwendungsfall-triage` empfehlen – bei umfangreichem Tracking ggf. DSFA nach Art. 35 DSGVO erforderlich.

**Änderungsentwurf (Datenschutzerklärung, Abschnitt "Drittlandsübermittlung"):**
> "[Neue Passage] Wir übermitteln Daten an [Anbieter] mit Sitz in den USA. Die Übermittlung erfolgt auf Grundlage von [Transfermechanismus: EU-Standardvertragsklauseln nach Beschluss 2021/914/EU / EU-US Data Privacy Framework]. Eine Transferfolgenabschätzung liegt vor. Weitere Informationen erhalten Sie auf Anfrage bei unserem Datenschutzbeauftragten."

## Risiken / typische Fehler

- **Sweep ohne konfigurierten Ausgabenordner:** Ohne Ordner-Pfad kann der Sweep keine Praxis-Inventur aus Plugin-Ausgaben erstellen; Direkt-Modus bleibt aber ohne Ausgabenordner vollständig nutzbar.
- **Datenschutzerklärungsversion nicht datiert:** Nutzer sollten publizierte Erklärungen immer mit Datum versehen; anderenfalls kann Drift nicht datiert werden.
- **Cookie-Banner ≠ Datenschutzerklärung:** TDDDG-Einwilligung (§ 25 TDDDG) ist unabhängig von der DSGVO-Rechtsgrundlage; eine korrekte Datenschutzerklärung ersetzt nicht den rechtskonformen Cookie-Banner.
- **Stillschweigendes Weglassen veralteter Klauseln:** Wenn eine Verarbeitung eingestellt wird, muss die Datenschutzerklärung aktiv aktualisiert werden – das Fehlen einer Praxis ist kein Automatismus für korrekte Erklärung.
- **Frequenz:** EDSA empfiehlt anlassbezogene Aktualisierung; ein rein jährliches Review ist bei schnell wachsenden Produkten nicht ausreichend.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen des TDDDG, neuen EDSA-Leitlinien zu Transparenz und Einwilligung sowie DSK-Orientierungshilfen zu Telemedien.

**Querverweise:**
- `datenschutzrecht/skills/regulierungs-luecken-analyse/SKILL.md` — Eingehende neue Anforderungen vs. Praxis-Drift
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Drittlandtransfer-Passagen in Datenschutzerklärungen
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Neue Verarbeitungstätigkeiten identifizieren

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz):** Seit 14.05.2024 (loest TTDSG ab); enthaelt §§ 24-25 zur Cookie- und Endgeraetezugriffs-Einwilligung. Quelle: gesetze-im-internet.de/tdddg.
- **EDSA-Guidelines Cookies / Tracking:** EDSA-Guidelines 02/2023 und Aktualisierungen (z.B. Dark Patterns) live ueber edpb.europa.eu pruefen.
- **DSK-Beschluesse (Datenschutzkonferenz Bund-Länder):** Aktuelle DSK-Beschluesse zu Cookies, Drittlandtransfer, KI, Beschaeftigtendatenschutz live ueber datenschutzkonferenz-online.de pruefen.
- **EuGH-Linie Cookies / Einwilligung:** Aktuelle EuGH-Verfahren zur Granularitaet, Freiwilligkeit, Pay-or-OK-Modellen live ueber curia.europa.eu pruefen.
- **DSA-Werbetransparenz:** Datenschutzerklaerung sollte bei Plattformen Hinweise auf DSA-Werbearchiv (Art. 39 DSA) und Empfehlungssysteme (Art. 38 DSA) enthalten.
- **KI-VO Art. 50:** Falls Webseite Chatbot oder KI-generierte Inhalte enthaelt — KI-VO-Transparenzpflichten ab 02.08.2026 in Datenschutzerklaerung / Impressum / Hinweise integrieren.

## Triage zu Beginn

1. Routinemonitor (wöchentlich/monatlich) oder konkreter Anlass (neue Verarbeitung, Systemwechsel)?
2. Welche Dokumente sollen geprüft werden? (Datenschutzerklärung Website / intern / beides)
3. Welche neuen Verarbeitungsvorgänge wurden seit dem letzten Monitor eingeführt?
4. Gibt es EDSA-Leitlinien oder DSK-Beschlüsse, die seit dem letzten Monitor in Kraft getreten sind?

## Output-Template — Monitor-Ergebnis

**Adressat:** DSB / Compliance — Tonfall: sachlich-strukturiert

```
Richtlinien-Monitor [DATUM]
Organisation: [NAME]
Geprüfte Dokumente: [LISTE]

Befunde:
| Nr. | Dokument | Abweichung / Drift | Prioritaet | Frist |
|-----|------------------|----------------------------------|------------|--------|
| 1 | Datenschutzerklärung | Cookie-Liste veraltet (3 neue) | HOCH | [DATUM]|
| 2 | Datenschutzerklärung | Empfaenger nicht konkret benannt| MITTEL | [DATUM]|
| 3 | Interne Richtlinie | KI-Tools noch nicht erwaehnt | HOCH | [DATUM]|

Keine Abweichungen: [LISTE GEPRÜFTER BEREICHE]

Empfehlung: Aktualisierung bis [DATUM]
Verantwortlich: [PERSON/ROLLE]
```

## 2. `ropa-art-30-controller-deutsch-vorlage`

**Fokus:** Vollvorlage für das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Tabellenstruktur mit allen sieben Mindestinhalten, ausgefuelltes Beispiel für Personalverwaltung, Mandantenakte, Kontaktformular, CRM. Direkt nutzbare Vorlage für Kanzleien und Unternehmen.

# RoPA-Vorlage Verantwortlicher (Controller) – Deutsch

## Zweck

Dieser Skill liefert eine ausfuellfertige Vorlage für das Verzeichnis von Verarbeitungstaetigkeiten des Verantwortlichen nach Art. 30 Abs. 1 DSGVO. Er enthaelt die Spaltenstruktur, ein Deckblatt, drei vollstaendig befuellte Beispiele und einen Versionierungs-Footer.

## Wann dieses Modul hilft

- Erstaufbau eines Verarbeitungsverzeichnisses in der Kanzlei oder im Mandantenunternehmen.
- Vorlage gegenueber Aufsichtsbehoerde gemaess Art. 30 Abs. 4 DSGVO.
- Auditvorbereitung; Lueckenanalyse eines bestehenden RoPA.
- Standardisierung mehrerer Standorte oder Mandantengruppen.

## Rechtlicher Rahmen

Art. 30 Abs. 1 DSGVO – Pflichtinhalte für Verantwortliche:

a) Name und Kontaktdaten des Verantwortlichen, ggf. gemeinsam Verantwortlicher, Vertreter und Datenschutzbeauftragter;
b) Zwecke der Verarbeitung;
c) Beschreibung der Kategorien betroffener Personen und der Kategorien personenbezogener Daten;
d) Kategorien von Empfaengern, gegenueber denen die personenbezogenen Daten offengelegt worden sind oder noch offengelegt werden, einschliesslich Empfaenger in Drittlaendern oder internationalen Organisationen;
e) ggf. Uebermittlungen in ein Drittland oder an eine internationale Organisation, einschliesslich der Angabe des betreffenden Drittlands sowie bei Uebermittlungen gemaess Art. 49 Abs. 1 Unterabs. 2 DSGVO Dokumentierung der geeigneten Garantien;
f) wenn moeglich, vorgesehene Fristen für die Loeschung der verschiedenen Datenkategorien;
g) wenn moeglich, allgemeine Beschreibung der TOMs gemaess Art. 32 Abs. 1 DSGVO.

## Ablauf / Checkliste

1. Deckblatt mit Verantwortlicher-Stammdaten anlegen.
2. Pro Geschaeftsprozess eine Zeile.
3. Spalten gemaess Vorlage befuellen.
4. Bei Drittlandtransfer Transferinstrument (SCC, DPF, BCR) eintragen.
5. Loeschfristen konkret, nicht "nach gesetzlichen Vorgaben".
6. TOMs in eigenes Anhangsdokument; im RoPA Verweis.
7. Versionierung am Fuss.
8. Jaehrlicher Review-Termin im Kalender.

## Mustertext / Template

### Deckblatt

```
Verantwortlicher: [Firmenname / Kanzleiname]
Anschrift: [...]
Vertreter (Art. 27): [falls anwendbar]
Datenschutzbeauftragter: [Name, Kontakt]
Aufsichtsbehoerde: [zuständige LDI / BfDI]
Erstellt: [Datum]
Letzte Aenderung: [Datum]
Version: [v1.0]
```

### Tabelle (Pflichtspalten)

| Nr. | Verarbeitungstaetigkeit | Zweck | Rechtsgrundlage | Kategorien Betroffene | Datenkategorien | Empfaengerkategorien | Drittland / Garantie | Loeschfrist | TOM-Verweis |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Personalverwaltung Beschaeftigte | Begruendung, Durchfuehrung und Beendigung des Arbeitsverhaeltnisses | Art. 6 Abs. 1 lit. b DSGVO, § 26 BDSG | Beschaeftigte, Bewerber | Stammdaten, Vertragsdaten, Lohndaten, Krankheitszeiten | Sozialversicherungstraeger, Finanzamt, Lohnbuchhaltungsdienstleister | nein | 10 Jahre nach Ausscheiden (§ 257 HGB, § 147 AO); Bewerberdaten 6 Monate | TOM-Anhang Ziff. 1, 3, 5 |
| 2 | Mandantenakte (Rechtsdienstleistung) | Anbahnung, Durchfuehrung und Abrechnung von Mandaten | Art. 6 Abs. 1 lit. b und f DSGVO; § 50 BRAO | Mandanten, Gegner, Zeugen | Stammdaten, Korrespondenz, Schriftsaetze, Honorardaten | Gerichte, Behörden, Gegenanwaelte, Versicherer | nein | 6 Jahre nach Mandatsende (§ 50 Abs. 1 BRAO); steuerlich relevante Belege 10 Jahre | TOM-Anhang Ziff. 1, 2, 4, 6 |
| 3 | Kontaktformular Website | Beantwortung von Anfragen | Art. 6 Abs. 1 lit. b oder f DSGVO | Interessenten, Mandanten | Name, E-Mail, Telefon, Anfrageinhalt | Hosting-Dienstleister (AVV) | nein | 6 Monate nach Erledigung | TOM-Anhang Ziff. 1, 5 |
| 4 | CRM Vertrieb | Kundenpflege, Akquise | Art. 6 Abs. 1 lit. b und f DSGVO | Bestandskunden, Interessenten | Stammdaten, Kontakthistorie, Umsatzdaten | CRM-SaaS-Anbieter (USA) | USA – EU-US DPF (Aktiv-Listing dokumentiert in Anhang DPF-Liste) | 3 Jahre nach letztem Kontakt | TOM-Anhang Ziff. 1, 2, 5 |

### Versionierungs-Footer

```
Version 1.0 – Erstanlage – [Datum, Bearbeiter]
Version 1.1 – [Aenderung] – [Datum, Bearbeiter]
```

## Typische Fehler

- "Zweck" und "Rechtsgrundlage" vermischt – bitte trennen.
- Empfaengerkategorien als Einzelnamen ("Frau Mueller, Steuerberater") statt Kategorie ("Steuerberatung").
- Drittland nur "USA" ohne Transferinstrument.
- Loeschfristen pauschal "10 Jahre" ohne Differenzierung nach Datenkategorie.
- TOM-Spalte mit vollem Wortlaut der Anlage 32 DSGVO – besser Verweis.
- Kein DSB-Eintrag obwohl Bestellpflicht (§ 38 BDSG) besteht.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` für Rechtsrahmen.
- `ropa-art-30-processor-deutsch-vorlage` für Spiegel-Vorlage Processor.
- `ropa-bdsg-besondere-art-9-categories` für Gesundheits- und Beschaeftigtendaten.
- `avv-tom-art-32-dsgvo-anlage` für TOM-Konzept.
- `drittlandstransfer-pruefung` für Art. 44 ff. DSGVO.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 30 Abs. 1.
- BDSG, § 26 (Beschaeftigtendaten), § 38 (DSB-Pflicht).
- BRAO § 50 (Aktenaufbewahrung).
- HGB § 257, AO § 147 (handels-/steuerrechtliche Aufbewahrung).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `ropa-art-30-dsgvo-grundlagen`

**Fokus:** Grundlagen des Verzeichnisses von Verarbeitungstaetigkeiten nach Art. 30 DSGVO. Anwendungsbereich, Schwellenwert, Mindestinhalte Controller und Processor, Verhaeltnis zu § 70 BDSG, Vorlagepflicht gegenueber der Aufsichtsbehoerde. Einstiegs-Skill für das Records of Processing Activities (RoPA).

# Verzeichnis von Verarbeitungstaetigkeiten – Art. 30 DSGVO Grundlagen

## Zweck

Dieser Skill ordnet das Verzeichnis von Verarbeitungstaetigkeiten (Records of Processing Activities, kurz RoPA) nach Art. 30 DSGVO ein. Er erklaert Pflichtige, Inhalte, Form und Verhaeltnis zu anderen Dokumentationspflichten (DSFA, AVV, RoPA), damit Kanzleien und Datenschutzbeauftragte das richtige Werkzeug für das richtige Dokument waehlen.

## Wann dieses Modul hilft

- Mandant fragt: "Brauchen wir ein Verarbeitungsverzeichnis?"
- Aufsichtsbehoerde verlangt nach Art. 30 Abs. 4 DSGVO Vorlage des Verzeichnisses.
- Audit eines bestehenden Verzeichnisses auf Vollstaendigkeit.
- Erstaufbau eines RoPA in einer Kanzlei, einem Unternehmen oder einer öffentlichen Stelle.
- Abgrenzung Controller-Verzeichnis (Art. 30 Abs. 1 DSGVO) vs. Processor-Verzeichnis (Art. 30 Abs. 2 DSGVO).

## Rechtlicher Rahmen

### Art. 30 Abs. 1 DSGVO – Verzeichnis des Verantwortlichen (Controller)

Pflichtinhalte:

1. Name und Kontaktdaten des Verantwortlichen, ggf. gemeinsam Verantwortlicher, Vertreter und Datenschutzbeauftragter.
2. Zwecke der Verarbeitung.
3. Beschreibung der Kategorien betroffener Personen und der Kategorien personenbezogener Daten.
4. Kategorien von Empfaengern, denen offengelegt wurde oder noch offengelegt wird.
5. Drittlandtransfer: Empfaengerland und Dokumentation geeigneter Garantien (Art. 46 Abs. 2 DSGVO).
6. Vorgesehene Loeschfristen für die verschiedenen Datenkategorien.
7. Allgemeine Beschreibung der technischen und organisatorischen Massnahmen (TOMs) gemaess Art. 32 Abs. 1 DSGVO.

### Art. 30 Abs. 2 DSGVO – Verzeichnis des Auftragsverarbeiters (Processor)

Pflichtinhalte:

1. Name und Kontaktdaten des Auftragsverarbeiters und jedes Verantwortlichen, für den er taetig ist, ggf. Vertreter und DSB.
2. Kategorien der im Auftrag jedes Verantwortlichen durchgefuehrten Verarbeitungen.
3. Drittlandtransfer: Empfaengerland und geeignete Garantien.
4. Allgemeine Beschreibung der TOMs (Art. 32 Abs. 1 DSGVO).

### Art. 30 Abs. 3 DSGVO – Schriftform

Schriftlich oder elektronisch. In der Praxis: Excel, Datenbank, RoPA-Software, Word-Dokument. Wichtig: aktuell halten, datierte Versionen.

### Art. 30 Abs. 4 DSGVO – Vorlagepflicht

Auf Anforderung der Aufsichtsbehoerde vorzulegen.

### Art. 30 Abs. 5 DSGVO – Ausnahme für KMU

Unternehmen oder Einrichtungen mit weniger als 250 Mitarbeitern sind grundsaetzlich befreit, **es sei denn**:

- die Verarbeitung birgt ein Risiko für Rechte und Freiheiten;
- die Verarbeitung erfolgt nicht nur gelegentlich;
- die Verarbeitung umfasst besondere Datenkategorien (Art. 9 DSGVO) oder Daten ueber strafrechtliche Verurteilungen (Art. 10 DSGVO).

In der Praxis: praktisch jede Kanzlei, jede Arztpraxis, jedes HR-System eines Mittelstaendlers erfuellt mindestens einen Ausnahmegrund. Die KMU-Ausnahme ist daher weitgehend Theorie.

### § 70 BDSG – RoPA für Bundesbehoerden

Fuer Bundesbehoerden im Anwendungsbereich der JI-Richtlinie (Polizei und Justiz) gilt § 70 BDSG mit eigenen Mindestinhalten.

## Ablauf / Checkliste

1. **Rollenklaerung:** Ist die Stelle Verantwortlicher, gemeinsam Verantwortlicher (Art. 26 DSGVO), Auftragsverarbeiter (Art. 28 DSGVO) oder mehreres zugleich?
2. **Pflichtenpruefung:** Greift Art. 30 Abs. 5 DSGVO oder ist Verzeichnis ohnehin Pflicht?
3. **Inventar:** Welche Verarbeitungstaetigkeiten gibt es? Faustregel: pro Geschaeftsprozess eine Zeile.
4. **Mindestinhalte erfassen:** je nach Rolle 7 (Controller) oder 4 (Processor) Felder.
5. **Drittlandtransfer:** separate Spalte; Verweis auf SCC, BCR, DPF, Angemessenheitsbeschluss.
6. **Loeschfristen:** konkrete Fristen, nicht "nach gesetzlichen Vorgaben".
7. **TOM-Referenz:** Verweis auf TOM-Konzept; nicht jede Massnahme im RoPA wiederholen.
8. **Versionierung:** Datierte Snapshots für Audit-Trail.
9. **Review-Zyklus:** jaehrlich oder bei wesentlicher Aenderung.

## Mustertext / Template

Tabellenkopf (Controller):

| Lfd. Nr. | Verarbeitungstaetigkeit | Zweck | Rechtsgrundlage | Kategorien Betroffene | Datenkategorien | Empfaengerkategorien | Drittland / Garantie | Loeschfrist | TOM-Verweis |
|---|---|---|---|---|---|---|---|---|---|

Tabellenkopf (Processor):

| Lfd. Nr. | Auftraggeber | Verarbeitungskategorie | Drittland / Garantie | TOM-Verweis |
|---|---|---|---|---|

Konkrete Vorlagen liefern die Skills:

- `ropa-art-30-controller-deutsch-vorlage`
- `ropa-art-30-processor-deutsch-vorlage`
- `ropa-en-controller-template`
- `ropa-en-processor-template`

## Typische Fehler

- KMU-Ausnahme bejaht, obwohl regelmäßige Personalverarbeitung erfolgt.
- TOM-Spalte mit "Verschluesselung" abgespeist – zu pauschal, Aufsichtsbehoerde fordert Konkretion.
- Drittlandtransfer nicht erfasst, obwohl SaaS in den USA gehostet wird.
- Empfaengerkategorien fehlen oder werden mit Einzelempfaengern verwechselt.
- Kein Versionsstand; bei Audit unklar, welcher Stand zum Pruefzeitpunkt galt.
- Loeschfristen pauschal "10 Jahre"; ohne Differenzierung nach Datenkategorie.
- Doppelte Pflege RoPA / DSFA / TOM-Konzept ohne Querverweise.

## Querverweise

- `dsfa-erstellung` für hochrisikobehaftete Verarbeitungen.
- `avv-art-28-dsgvo-grundtatbestand` für Processor-Vertraege.
- `drittlandstransfer-pruefung` für Art. 44 ff. DSGVO.
- `dsb-bestellungspflicht-pruefung` für DSB-Verantwortlichkeiten.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), insbesondere Art. 30, Erwaegungsgrund 13, 82.
- BDSG, insbesondere § 70 für Bundesbehoerden.
- EDSA: Position Paper on Article 30(5) GDPR (vom 19.04.2018).
- Konferenz der unabhaengigen Datenschutzaufsichtsbehoerden des Bundes und der Länder (DSK): Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `ropa-bdsg-besondere-art-9-categories`

**Fokus:** RoPA-Besonderheiten bei besonderen Datenkategorien nach Art. 9 DSGVO (Gesundheit, biometrische Daten, Religion, Gewerkschaftszugehoerigkeit), bei Beschaeftigtendaten § 26 BDSG und strafrechtlichen Verurteilungen Art. 10 DSGVO. Erhoehte Anforderungen an Zweckbestimmung, Erforderlichkeit, Rechtsgrundlage und TOMs.

# RoPA bei besonderen Datenkategorien – Art. 9 DSGVO, § 26 BDSG, Art. 10 DSGVO

## Zweck

Dieser Skill behandelt die erhoehten Dokumentationsanforderungen im Verzeichnis von Verarbeitungstaetigkeiten bei besonderen Datenkategorien nach Art. 9 DSGVO (sensitive Daten), Beschaeftigtendaten nach § 26 BDSG und Daten ueber strafrechtliche Verurteilungen oder Straftaten nach Art. 10 DSGVO. Solche Verarbeitungen brechen die KMU-Ausnahme nach Art. 30 Abs. 5 DSGVO und ziehen ueblicherweise eine DSFA-Pflicht (Art. 35 DSGVO) nach sich.

## Wann dieses Modul hilft

- Arztpraxis, Krankenhaus, Pflegedienst, Apotheke baut RoPA auf.
- Personalabteilung dokumentiert Krankheitstage, BEM-Daten, Schwerbehindertenstatus.
- Kanzlei verarbeitet Mandantendaten mit Bezug zu Gesundheit, Religion, sexueller Orientierung, Strafverfahren.
- Versicherer dokumentiert Gesundheits- oder Schadendaten.
- Verein dokumentiert religioese oder gewerkschaftliche Zugehoerigkeit der Mitglieder.
- Biometrische Verfahren (Fingerprint-Login, Gesichtserkennung) im Einsatz.

## Rechtlicher Rahmen

### Art. 9 Abs. 1 DSGVO – Verbotsprinzip

Verarbeitung ist verboten, soweit sie ergibt:

- rassische und ethnische Herkunft,
- politische Meinungen,
- religioese oder weltanschauliche Ueberzeugungen,
- Gewerkschaftszugehoerigkeit,
- genetische Daten,
- biometrische Daten zur eindeutigen Identifizierung,
- Gesundheitsdaten,
- Daten zum Sexualleben oder der sexuellen Orientierung.

### Art. 9 Abs. 2 DSGVO – Ausnahmen

Verarbeitung zulaessig u. a. bei: ausdruecklicher Einwilligung (lit. a), Arbeitsrecht und Sozialrecht (lit. b), lebenswichtigem Interesse (lit. c), Vereinen und Religionsgemeinschaften (lit. d), oeffentlich gemachten Daten (lit. e), Rechtsanspruechen (lit. f), erhebliches öffentliches Interesse (lit. g), Gesundheits- und Sozialfürsorge (lit. h), öffentliche Gesundheit (lit. i), Archiv-/Forschungs-/Statistikzwecke (lit. j).

### § 26 BDSG – Beschaeftigtendaten

§ 26 BDSG bleibt nach Aufhebung durch BVerfG-Rechtsprechung und nachfolgende Gesetzgebung als Rechtsgrundlage praeskriptiv relevant; daneben kommen Kollektivvereinbarungen (§ 26 Abs. 4 BDSG) und Einwilligung (§ 26 Abs. 2 BDSG) in Betracht.

### § 22 BDSG

§ 22 BDSG regelt die Verarbeitung besonderer Datenkategorien zu im öffentlichen Interesse liegenden Zwecken, für Beschaeftigungszwecke, für praeventive Medizin u. a.; § 22 Abs. 2 BDSG verlangt **spezifische TOMs**, die im RoPA dokumentiert werden muessen.

### Art. 10 DSGVO

Daten ueber strafrechtliche Verurteilungen und Straftaten duerfen nur unter behoerdlicher Aufsicht oder aufgrund nationalen Rechts verarbeitet werden.

## Ablauf / Checkliste

1. **Identifikation:** Welche der oben genannten Kategorien faellt an? Pruefe sowohl direkte Erhebung als auch Rueckschluss (z. B. Fotos koennen ethnische oder gesundheitliche Hinweise enthalten).
2. **Rechtsgrundlage:** Doppelte Rechtsgrundlage erforderlich – Art. 6 Abs. 1 DSGVO **und** Art. 9 Abs. 2 DSGVO bzw. § 26 oder § 22 BDSG.
3. **Erforderlichkeit:** strenger Massstab; pruefe Alternativen (Pseudonymisierung, Aggregation).
4. **DSFA-Pruefung:** Art. 35 Abs. 3 lit. b DSGVO – DSFA in der Regel obligatorisch bei umfangreicher Verarbeitung besonderer Kategorien.
5. **TOMs:** § 22 Abs. 2 BDSG fordert spezifische Massnahmen (Pseudonymisierung, Zugriffsbeschraenkung, Auditing, Schulung).
6. **RoPA-Eintrag:** zusaetzliche Spalte oder Markierung "Art. 9 DSGVO" mit Verweis auf Rechtsgrundlage und DSFA.
7. **Loeschfristen:** restriktiv; Gesundheitsdaten oft 10 Jahre (§ 630f Abs. 3 BGB Patientenakte), aber nicht laenger.

## Mustertext / Template

### Zusatzspalten für besondere Datenkategorien

| Verarbeitung | Datenkategorie (Art. 9) | Doppelte Rechtsgrundlage | DSFA-Verweis | Spezifische TOMs (§ 22 Abs. 2 BDSG) |
|---|---|---|---|---|
| Patientenakte | Gesundheitsdaten | Art. 6 Abs. 1 lit. b + Art. 9 Abs. 2 lit. h DSGVO; § 22 Abs. 1 Nr. 1 lit. b BDSG | DSFA-Ziff. 3 | Rollenbasierter Zugriff, Pseudonymisierung Forschungsdatensatz, Verschluesselung at-rest |
| BEM-Verfahren | Gesundheitsdaten Beschaeftigte | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 26 Abs. 3 BDSG | DSFA-Ziff. 7 | Getrennte Akte, eingeschraenkter Personenkreis, dokumentierter Zugriff |
| Glaubensbekenntnis Lohnsteuer | Religioese Ueberzeugung | Art. 6 Abs. 1 lit. c + Art. 9 Abs. 2 lit. b DSGVO; § 39 EStG | DSFA-Ziff. 9 | Zugriff nur Lohnbuchhaltung, kein CRM-Sync |
| Biometrischer Zutritt | Biometrische Daten | Art. 6 Abs. 1 lit. f + Art. 9 Abs. 2 lit. a DSGVO (Einwilligung) | DSFA-Ziff. 11 | Lokale Speicherung Template, kein Bild, Loeschung bei Austritt |

### Erweiterung Versionierungs-Footer

Zusatzhinweis: "Diese Verarbeitung beinhaltet besondere Kategorien personenbezogener Daten. DSFA-Pflicht und § 22 Abs. 2 BDSG sind beachtet."

## Typische Fehler

- Nur Art. 6 DSGVO geprueft, Art. 9 DSGVO uebersehen.
- Schwerbehindertenstatus aus dem Personalstammdatensatz ohne gesonderte Markierung als Gesundheitsdatum gefuehrt.
- Biometrie-Login ohne ausdrueckliche Einwilligung und ohne Alternative.
- Keine DSFA, obwohl umfangreiche Gesundheitsdatenverarbeitung.
- "Sensible Daten" pauschal eingetragen ohne konkrete Kategorie.
- TOMs nach Art. 32 statt nach § 22 Abs. 2 BDSG (zusaetzliche Anforderungen).
- Religionszugehoerigkeit aus Lohnsteuerklasse abgeleitet und ungesichert im allgemeinen HR-System.

## Querverweise

- `ropa-art-30-dsgvo-grundlagen` für Basis.
- `ropa-art-30-controller-deutsch-vorlage` für Basisvorlage.
- `dsfa-erstellung` für Art. 35 DSGVO.
- `mitarbeiter-datenschutz-26-bdsg` (falls vorhanden) für Beschaeftigtenkontext.
- `avv-tom-art-32-dsgvo-anlage` für TOM-Anhang.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 9, Art. 10, Art. 30, Art. 35.
- BDSG, §§ 22, 26.
- BGB § 630f (Patientenakte).
- EStG § 39 (Lohnsteuermerkmale).
- EDSA: Leitlinien 03/2019 zur Verarbeitung personenbezogener Daten durch Videoeinrichtungen (Version 2.0 vom 29.01.2020).
- BVerfG, Beschluss vom 11.11.2020 – 1 BvR 3214/15 (Antiterrordatei-Folgeentscheidung) – bei Anpassung des § 22 BDSG sinngemaess beachten; vor Zitierung amtliche Fundstelle pruefen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `ropa-en-controller-template`

**Fokus:** Full English-language template for the Records of Processing Activities (RoPA) of the controller under Article 30(1) GDPR. Seven mandatory contents, cover sheet, three worked examples (HR, client files, CRM with US sub-processor), and a versioning footer. Suitable for German law firms with international clients.

# Records of Processing Activities (RoPA) – Controller Template (English)

## Purpose

This skill provides a ready-to-use English-language template for the Records of Processing Activities (RoPA) of a controller pursuant to Article 30(1) GDPR. It is intended for German law firms, in-house counsel, and data protection officers who need to provide a RoPA in English to international clients, US group entities, or supervisory authorities in cross-border investigations.

## When you need this skill

- A multinational client requires an English-language RoPA.
- A US parent company asks for the EU subsidiary's processing records.
- A supervisory authority requests the RoPA in English in a cross-border case.
- A vendor audit (SOC 2, ISO 27001) reviews the RoPA.
- A first-time build of a RoPA in an internationally facing organisation.

## Legal framework

Article 30(1) GDPR requires the controller to maintain a record containing:

a) the name and contact details of the controller and, where applicable, the joint controller, the controller's representative, and the Data Protection Officer;
b) the purposes of the processing;
c) a description of the categories of data subjects and of the categories of personal data;
d) the categories of recipients to whom the personal data have been or will be disclosed, including recipients in third countries or international organisations;
e) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
f) where possible, the envisaged time limits for erasure of the different categories of data;
g) where possible, a general description of the technical and organisational measures referred to in Article 32(1) GDPR.

Article 30(3) requires written or electronic form; Article 30(4) makes the RoPA available to the supervisory authority on request; Article 30(5) provides a narrow SME exemption that rarely applies in practice.

## / Checklist

1. Fill in the cover sheet with controller details, representative (if applicable), and DPO.
2. One row per processing activity (one business process = one row).
3. Populate the seven mandatory columns.
4. For third-country transfers, identify the transfer tool (Adequacy Decision, SCCs, BCRs, DPF).
5. State retention periods concretely; avoid "as required by law".
6. Keep TOMs in a separate annex; reference only.
7. Add a versioning footer.
8. Schedule annual review.

## Template

### Cover Sheet

```
Controller: [Company / Firm Name]
Address: [...]
Representative (Art. 27): [if applicable]
Data Protection Officer: [Name, contact]
Supervisory Authority: [competent DPA]
Created: [date]
Last amended: [date]
Version: [v1.0]
```

### Table (mandatory columns)

| No. | Processing activity | Purpose | Legal basis | Categories of data subjects | Categories of personal data | Categories of recipients | Third country / safeguards | Retention period | TOM reference |
|---|---|---|---|---|---|---|---|---|---|
| 1 | HR administration | Establishment, performance, and termination of employment | Art. 6(1)(b) GDPR; Sec. 26 BDSG | Employees, applicants | Master data, contract data, payroll, sick leave | Social security, tax authority, payroll provider | none | 10 years after termination (Sec. 257 HGB, Sec. 147 AO); applicants 6 months | TOM Annex 1, 3, 5 |
| 2 | Client matter administration | Engagement, performance, and billing of legal services | Art. 6(1)(b) and (f) GDPR; Sec. 50 BRAO | Clients, opposing parties, witnesses | Master data, correspondence, briefs, fee data | Courts, authorities, opposing counsel, insurers | none | 6 years after end of mandate (Sec. 50(1) BRAO); tax-relevant documents 10 years | TOM Annex 1, 2, 4, 6 |
| 3 | Website contact form | Responding to inquiries | Art. 6(1)(b) or (f) GDPR | Prospective clients | Name, email, phone, message | Hosting provider (DPA in place) | none | 6 months after closure | TOM Annex 1, 5 |
| 4 | CRM sales | Customer relationship, business development | Art. 6(1)(b) and (f) GDPR | Existing customers, prospects | Master data, contact history, revenue data | CRM SaaS provider (USA) | USA – EU-US Data Privacy Framework (active listing on file, see DPF Annex) | 3 years after last contact | TOM Annex 1, 2, 5 |

### Versioning footer

```
Version 1.0 – Initial draft – [date, author]
Version 1.1 – [change] – [date, author]
```

## Common mistakes

- Mixing "purpose" and "legal basis" in one column.
- Listing individual recipients ("Ms. Smith, accountant") instead of categories ("Tax advisory firms").
- Stating "USA" without naming the transfer tool.
- Generic retention "10 years" without differentiation by data category.
- Copying the full Art. 32 wording into the TOM column instead of referring to a TOM annex.
- Failing to list a DPO where one is mandatory under Sec. 38 BDSG.

## Cross-references

- `ropa-art-30-dsgvo-grundlagen` for the German-language framework.
- `ropa-en-processor-template` for the processor counterpart.
- `ropa-konzernumlauf-und-multi-entity` for multi-entity groups.
- `dpa-en-template-controller-processor` for English DPA templates.
- `tia-en-template-full` for the English Transfer Impact Assessment template.

## Sources as of 06/2026

- Regulation (EU) 2016/679 (GDPR), in particular Article 30(1), Recitals 13 and 82.
- BDSG (German Federal Data Protection Act), Sec. 26, 38.
- BRAO (Federal Lawyers' Act), Sec. 50.
- HGB Sec. 257; AO Sec. 147.
- DSK Short Paper No. 1 "Records of Processing Activities" (Status 17 December 2018).
- EDPB Position Paper on Article 30(5) GDPR (19 April 2018).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
