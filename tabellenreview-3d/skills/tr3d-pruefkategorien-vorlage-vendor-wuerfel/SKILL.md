---
name: tr3d-pruefkategorien-vorlage-vendor-wuerfel
description: "Tr3d Pruefkategorien Vorlage Vendor Wuerfel: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Tr3d Pruefkategorien Vorlage Vendor Wuerfel

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Tr3d Pruefkategorien Vorlage Vendor Wuerfel** im Plugin Tabellenreview 3D. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tr3d-pruefkategorien-bauleiter` | Bauleiter Pruefkategorien fuer Insolvenztabellenreview: Forderungsgrund, Bewertung, Bestreitenshistorie, Verteilungsquote. Pruefraster fuer drei-dimensionalen Aufbau. |
| `vorlage-vendor-onboarding-3d` | Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output: Vendor-Onboarding-Prüftabelle. Abgrenzung: nicht allgemeine Vertragsprüfung. |
| `wuerfel-aufbauen` | 3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output: Wuerfelkonfigurationsdokument. Abgrenzung: nicht Prüfungsdurchführung. |

## Arbeitsweg

Im Plugin Tabellenreview 3D gilt für **Tr3d Pruefkategorien Vorlage Vendor Wuerfel**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tr3d-pruefkategorien-bauleiter`

**Fokus:** Bauleiter Pruefkategorien fuer Insolvenztabellenreview: Forderungsgrund, Bewertung, Bestreitenshistorie, Verteilungsquote. Pruefraster fuer drei-dimensionalen Aufbau.

# TR3D: Pruefkategorien Bauleiter

## Spezialwissen: TR3D: Pruefkategorien Bauleiter
- **Spezialgegenstand:** TR3D: Pruefkategorien Bauleiter / tr3d pruefkategorien bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `vorlage-vendor-onboarding-3d`

**Fokus:** Vorlagetabelle für Lieferanten-Onboarding-Review im 3D-Format: Vertrag, Compliance, Leistung. Normen: BGB, UWG, GWB. Prüfraster: Vertragskonformität, Compliance-Status, Leistungsindikatoren. Output: Vendor-Onboarding-Prüftabelle. Abgrenzung: nicht allgemeine Vertragsprüfung.

# /tabellenreview-3d:vorlage-vendor-onboarding-3d


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Beim Onboarding eines neuen Lieferanten (oder beim Bestands-Audit der vorhandenen) sind dieselben 17 Fragen aus 5 Perspektiven zu beantworten. Dieser Würfel liefert die Standardstruktur.

## Spalten (17 Datenpunkte)

### Stammdaten

1. Vendor-Name und Rechtsform
2. Branche und Hauptleistung
3. Sitz und Lieferketten-Region

### Datenschutz

4. AVV-Pflicht (DSGVO Artikel 28)
5. AVV-vorhanden und aktuelle Fassung
6. Drittlandtransfer (USA UK CH andere)
7. SCC vorhanden (Standardvertragsklauseln)

### IT und SLA

8. Verschlüsselung in Transit und at Rest
9. SLA-Reaktionszeit
10. SLA-Verfügbarkeit (Prozent / Jahr)
11. Subunternehmer-Liste vollständig

### Exit und Daten

12. Exit-Klausel (Vertragsende Pflichten)
13. Datenherausgabe-Format und Frist

### Compliance

14. Sanktionsliste gefiltert (EU US OFAC)
15. GwG-Prüfung wirtschaftlich Berechtigter
16. Lieferketten-Risiko nach LkSG (Branchen und Region)

### Wirtschaft

17. Versicherungssumme und Haftungsbegrenzung

## Arbeitsblatt-Perspektiven (5)

### Vertrag

- Zusatzspalten: AGB-Wirksamkeit (BGB Paragraph 305 ff.) / Gerichtsstand / Vertragsstrafe
- Prüfer: Vertragsanwalt
- Materialität rot: Haftungsausschluss für Vorsatz / grobe Fahrlaessigkeit

### Datenschutz

- Zusatzspalten: TIA (Transfer Impact Assessment) / Datenschutz-Folgenabschätzung-Pflicht / Joint-Controller
- Prüfer: Datenschutzbeauftragter
- Materialität rot: Auftragsverarbeitung ohne AVV; Drittlandtransfer ohne SCC + TIA

### IT-Sicherheit

- Zusatzspalten: ISO-27001-Zertifikat / SOC-2-Bericht / Penetrationstest-Bericht / Vulnerability-Disclosure-Policy
- Prüfer: CISO / IT-Sicherheit
- Materialität rot: keine ISO-27001 UND keine SOC-2 UND Verarbeitung sensibler Daten

### Compliance (GwG / LkSG)

- Zusatzspalten: GwG-Transparenzregister / Sanktionslisten-Treffer / Risiko nach LkSG Paragraph 5 / Beschwerdeverfahren-Anbindung
- Prüfer: Compliance-Officer
- Materialität rot: Sanktionslisten-Treffer; LkSG-Hochrisiko-Region ohne Pruefkette

### Wirtschaft

- Zusatzspalten: Vendor-Volumen / Lock-in-Risiko / Wechselkosten / Konzentrations-Risiko
- Prüfer: Einkauf / Risikomanagement
- Materialität rot: Vendor-Lock-in ohne Exit-Daten-Standard UND mehr als 30 Prozent Anteil an kritischer Leistung

## Normenrahmen

- **DSGVO** — Artikel 28 (Auftragsverarbeitung) Artikel 35 (DSFA) Artikel 44 ff. (Drittlandtransfer)
- **BDSG** — Beschaeftigtendatenschutz
- **GwG** — Paragraph 10 Sorgfaltspflichten Paragraph 20 Transparenzregister
- **LkSG** — Paragraph 5 Risikoanalyse Paragraph 6 Präventionsmaßnahmen
- **BGB** — Paragraph 305 ff. AGB-Kontrolle
- **TKG / NIS2** — bei TK-/Cyber-bezogenen Vendoren

## Ausgabe

Würfel-Schema fix und fertig. Direkt einsatzbereit.

## 3. `wuerfel-aufbauen`

**Fokus:** 3D-Wuerfelstruktur für den Tabellenreview aufbauen: Zeilen, Spalten, Perspektiven verknuepfen. Normen: §§ 174 ff. InsO. Prüfraster: Dimensionen-Vollständigkeit, Verknuepfungslogik, Konfiguration. Output: Wuerfelkonfigurationsdokument. Abgrenzung: nicht Prüfungsdurchführung.

# /tabellenreview-3d:würfel-aufbauen


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Bevor ein Reviewlauf startet, muss die Würfel-Struktur stehen. Dieser Skill fragt die drei Achsen ab und schreibt sie in eine versionierte `wuerfel-schema.yaml`. Die Reviewlauf-Skills lesen ausschließlich diese Datei. Wer den Würfel ändern will ändert das Schema; nichts verschwindet still.

## Eingaben

- Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/tabellenreview-3d/CLAUDE.md`
- Projektname (kebab-case)
- Anwendungsfall (M&A-DD / Immobilien / Vendor / Arbeitsvertrag / Mietvertrag / Anlage / Eigenwürfel)
- Optional: Vorlage aus dem Plugin (siehe Skills `vorlage-*`)
- Optional: bestehende Spaltenprompt-Bibliothek

## Methodik

1. **Achse 1 — Spalten (Datenpunkte) definieren**
 - Jede Spalte ist ein Spaltenprompt: eine einzige präzise Frage, die für ALLE Dokumente gleich beantwortet wird.
 - Pflichtfelder pro Spalte: `id`, `titel`, `prompt`, `antworttyp` (Freitext / Zitat-mit-Fundstelle / ja-nein / Datum / Geldbetrag / Aufzählung), `pflichtfeld` (ja / nein), `ampel-regel` (wann rot / gelb / grün).
2. **Achse 2 — Zeilen (Dokumente) definieren**
 - Jede Zeile ist ein Dokument mit Quellpfad Hash und optionalem Zeilenprompt.
 - Pflichtfelder pro Zeile: `id`, `pfad`, `hash`, `dokumenttyp`, optional `zeilenprompt` für dokumentspezifische Sonderanweisungen.
3. **Achse 3 — Arbeitsblätter (Perspektiven) definieren**
 - Jedes Arbeitsblatt ist eine eigene Pruefperspektive die über denselben Dokumentenstapel läuft.
 - Beispiele: Recht (Anwaltsperspektive) / Steuer (Steuerberater) / Wirtschaft (Buyside) / Datenschutz (DSGVO) / IT (Architektur) / Betrieb (Operations)
 - Pflichtfelder pro Arbeitsblatt: `id`, `titel`, `perspektive`, `eigene-spalten-zusätze` (Arbeitsblatt-spezifische Zusatzspalten) und `auslassungen` (Spalten die für dieses Blatt nicht gelten).
4. **Risikoampel-Konsolidierung** je Achse festlegen: Wann ist eine Zelle rot? Wann eine ganze Zeile rot? Wann ein ganzes Arbeitsblatt rot?
5. **Belegkette-Konvention:** jedes Zitat in einer Zelle muss zurückverfolgbar sein auf Datei-Hash und Stelle (Seite Absatz Ziffer).
6. **Audit-Trail:** Prompt-Versionen Reviewlauf-Zeitstempel Prüfer-Abnahmen werden separat protokolliert.

## Ausgabe

- `wuerfel-schema.yaml` mit allen drei Achsen, vollständig definiert
- `wuerfel-vorschau.md` — menschenlesbare Übersicht zur Prüfer-Abnahme
- Optional: `spaltenprompt-bibliothek.yaml` als Referenz auf Standard-Spaltenprompts

## Quellenpflicht

Verbindlich gegen `references/zitierweise.md` im Repository. Jede juristische Anspielung im Spaltenprompt benötigt einen Verweis auf Norm Rechtsprechung oder Kommentarstelle.

## Beispiel

Würfel für M&A-DD bei Erwerb einer SaaS-GmbH:
- **Spalten:** 12 Datenpunkte (Vertragsart Laufzeit Kündigungsfrist Change-of-Control Abtretungsverbot Haftungsbegrenzung Service-Level Datenschutz-Auftragsverarbeitung Geheimhaltung Vergütung-Anpassungsklausel anwendbares Recht Gerichtsstand)
- **Zeilen:** 87 Verträge aus dem Datenraum (Kunden Lieferanten Banken Lizenzen Personal)
- **Arbeitsblätter:** 4 Perspektiven (Recht / Steuer / Wirtschaft / Datenschutz)
- Ergebnis: 12 mal 87 mal 4 = 4176 Zellen, jede mit wörtlichem Zitat und Fundstelle.

## Grenzen

Das Schema ist nur die Architektur. Der eigentliche Reviewlauf erfolgt im Skill `review-durchfuehren`. Wer das Schema nachträglich ändert nachdem schon ein Lauf erfolgt ist muss `prompt-versionierung` und `caching-und-teil-rerun` beachten.
