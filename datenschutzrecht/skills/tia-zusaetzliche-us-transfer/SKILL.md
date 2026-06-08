---
name: tia-zusaetzliche-us-transfer
description: "TIA Zusaetzliche US Transfer im Datenschutzrecht: prüft konkret Zusaetzliche Schutzmassnahmen (Supplementary Measures) nach, US-Drittlandtransfer nach Art, Verzeichnis der Verarbeitungstätigkeiten nach Art."
---

# TIA Zusaetzliche US Transfer

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `tia-zusaetzliche-schutzmassnahmen-encryption-pseudonymisierung`

**Fokus:** Zusaetzliche Schutzmassnahmen (Supplementary Measures) nach EDPB-Empfehlung 01/2020 Annex 2. Technische Massnahmen Verschluesselung Pseudonymisierung Split Processing Key Management; vertragliche Massnahmen Transparenzpflichten Warrant Canary; organisatorische Massnahmen Schulung Policy. Mit Use-Case-Matrix und Anforderungen an starke Verschluesselung.

### Zusaetzliche Schutzmassnahmen für das TIA (Schritt 4 EDPB-Roadmap)

## Wann dieses Modul hilft

- Schritt 3 des TIA hat ergeben, dass Drittlandsrecht/Praxis das SCC-Schutzniveau nicht abdeckt.
- Vertragsverhandlung mit US-Anbieter; ergaenzende Schutzklauseln zu formulieren.
- Architekturentscheidung Cloud-Anbieter: technisch realisierbares Schutzmodell?
- Pruefung, ob Use Case 6 oder 7 vorliegt (keine wirksamen Massnahmen moeglich).
- Diskussion mit Anbieter, der nur vertragliche Massnahmen anbieten will.

## Rechtlicher Rahmen

- EuGH **C-311/18** Schrems II vom 16.07.2020.
- **EDPB Empfehlung 01/2020** Final 18.06.2021, **Annex 2**: Use Cases 1-7.
- Art. **32 DSGVO** (TOMs als Basisanforderung; bei Drittlandtransfer hoeher).
- Art. **25 DSGVO** (Datenschutz durch Technikgestaltung).

## Ablauf / Checkliste

### Use-Case-Bewertung Annex 2

| Use Case | Konstellation | Wirksamkeit moeglich? |
|---|---|---|
| 1 | Datenspeicherung mit Verschluesselung; Schluessel ausschliesslich beim Exporteur in der EU | Ja (effektiv) |
| 2 | Uebermittlung pseudonymisierter Daten ohne Moeglichkeit der Re-Identifizierung durch Importeur | Ja (effektiv) |
| 3 | Verschluesselter Transit für Empfaenger im Drittland mit gesetzlich geschuetztem Berufsgeheimnis | Bedingt |
| 4 | Geteilte Verarbeitung (Split Processing) mehrerer unabhaengiger Importeure | Bedingt |
| 5 | Importeur und Exporteur teilen Zugriff im EU-Gebiet; Drittlandimporteur erhaelt nur statistische Aggregate | Ja |
| 6 | Daten zur Klartextverarbeitung an Importeur im Drittland mit Zugriffsbefugnissen ohne adaequaten Schutz | Nein – keine wirksamen Massnahmen |
| 7 | Remote Access im Klartext durch Importeur im Drittland mit Zugriffsbefugnissen ohne adaequaten Schutz | Nein – keine wirksamen Massnahmen |

### Technische Massnahmen

- **Starke Verschluesselung at-rest und in-transit** (mindestens AES-256, TLS 1.3, geprueft anhand ENISA-/BSI-TR-02102).
- **Key Management ausserhalb des Drittlands**: Schluessel im EU/EWR-HSM; Importeur kann nicht entschluesseln.
- **Hold-Your-Own-Key (HYOK), Bring-Your-Own-Key (BYOK)** mit Vorbehalten – HYOK ist staerker.
- **Pseudonymisierung mit unkorrelierten Schluesseln** (Art. 4 Nr. 5 DSGVO; § 22 Abs. 2 Nr. 5 BDSG).
- **Anonymisierung**, soweit Re-Identifizierung im Drittland praktisch ausgeschlossen.
- **Split Processing / Confidential Computing** (Enclaves, TEEs) – Wirksamkeit von Implementation abhaengig.
- **Tokenisierung**, **Format-Preserving Encryption**.
- **Confidentiality Computing** (Intel SGX, AMD SEV) – noch nicht universell als alleiniger Schutz akzeptiert.

### Vertragliche Massnahmen

- Berichtspflicht zu Behördenanfragen (Art und Anzahl, soweit zulaessig); **Warrant Canary**.
- Anfechtungspflicht des Importeurs ("challenge any legally available avenue").
- Erweiterte Audit-Rechte für Exporteur und Aufsichtsbehoerde.
- Sofortige Aussetzungspflicht bei Anweisung, die nicht abgewehrt werden kann.
- Klausel zur Mitteilung bei Aenderung der Rechtslage.
- Haftungs- und Schadensersatzregelungen verstaerken.

### Organisatorische Massnahmen

- Mitarbeiterschulung mit Schwerpunkt Behördenanfragen-Reaktion.
- Standardisierte interne Pruefprozesse für eingehende Government Requests.
- Veroeffentlichte Privacy Policy / Transparenzberichte des Importeurs.
- Datenminimierung an der Quelle.
- Klare Rollendefinition: wer entscheidet Aussetzung?

### Wirksamkeitspruefung

- Schutz greift sowohl rechtlich als auch praktisch?
- Massnahmen kumulativ ausreichend, um die Garantien A bis D zu kompensieren?
- Restrisiko dokumentiert und akzeptiert?

## Mustertext / Template

Vertragsbaustein – Behördenanfragen:

> Der Datenimporteur verpflichtet sich, jede Anfrage einer staatlichen Stelle oder einer Sicherheitsbehoerde, die auf Herausgabe der uebermittelten personenbezogenen Daten oder auf direkten Zugriff hierauf gerichtet ist, unverzueglich dem Datenexporteur mitzuteilen, soweit dies rechtlich zulaessig ist. Ist die Mitteilung gesetzlich untersagt, verpflichtet sich der Datenimporteur, sich auf rechtmäßigem Wege für eine Aufhebung oder Lockerung des Verbots einzusetzen und mindestens halbjaehrlich aggregierte Statistiken zu solchen Anfragen zu veröffentlichen. Der Datenimporteur stellt sicher, dass jede Anfrage auf ihre Rechtmaessigkeit, Notwendigkeit und Verhaeltnismaessigkeit geprueft wird und dass alle rechtlichen Mittel zur Begrenzung der Datenherausgabe ausgeschoepft werden.

Technischer Baustein:

> Vor jeder Uebermittlung wird der personenbezogene Datensatz anhand des Schluessels K1 verschluesselt; K1 wird im Hardware Security Module des Exporteurs in der EU verwaltet und nicht an den Importeur uebermittelt. Der Importeur erhaelt ausschliesslich verschluesselte Datenstroeme. Eine Entschluesselung ist ohne K1 nicht moeglich. Der Importeur fuehrt keine Klartextverarbeitung durch und besitzt keine Funktion zur Entschluesselung.

## Typische Fehler

- Nur vertragliche Massnahmen ohne technische Untermauerung – EDPB-konform unzureichend bei Use Case 6/7.
- "Cloud-Anbieter-Verschluesselung" akzeptiert, obwohl Schluessel beim Anbieter im Drittland liegen.
- Pseudonymisierung "vor Ort", aber Importeur erhaelt Zuordnungsschluessel.
- TEEs / Enclaves als alleiniger Schutz angesetzt, ohne dass die Konfiguration validiert ist.
- Use Case 6/7 vorliegend, aber dennoch "Schutzmassnahmen wirken" formuliert – sachwidrig.
- Restrisiko nicht dokumentiert; Entscheider-Sign-off fehlt.
- Warrant Canary versprochen, aber kein operatives Verfahren.

## Quellen Stand 06/2026

- EDPB Empfehlung 01/2020 Final 18.06.2021, insb. Annex 2 Use Cases.
- EDPB Empfehlung 02/2020 vom 10.11.2020 (EEG).
- EuGH C-311/18 (Schrems II) vom 16.07.2020.
- DSGVO, Art. 25, 32.
- BSI Technische Richtlinie TR-02102 (kryptografische Verfahren), aktueller Stand auf bsi.bund.de pruefen.
- ENISA Guidelines for SMEs on the security of personal data processing (Dezember 2016) und Folgepapiere.

## 2. `us-transfer-tia-dokumentation`

**Fokus:** US-Drittlandtransfer nach Art. 44 ff. DSGVO dokumentieren: EU-US Data Privacy Framework, DPF-Listing, Schrems I/II-Historie, SCC/BCR-Ausweichpfad, Transfer Impact Assessment, supplementary measures, Behördennachweis und Review-Kalender.

### US-Transfer-TIA-Dokumentation

## Zweck

Dieser Skill erstellt ein belastbares Dokumentationspaket für personenbezogene Datenübermittlungen in die USA. Er ist für Kanzleien, Datenschutzbeauftragte und Rechtsabteilungen gedacht, die gegenüber einer deutschen Aufsichtsbehörde zeigen müssen: Transfer identifiziert, Rechtsgrundlage gewählt, DPF-Listing geprüft, Alternativpfad SCC/BCR/TIA sauber dokumentiert, technische und organisatorische Maßnahmen bewertet, Wiedervorlage gesetzt.

**Wichtige Grundregel:** Safe Harbor und EU-US Privacy Shield sind keine aktuelle Transfergrundlage. Sie werden nur als historische Einordnung oder Altlastenprüfung dokumentiert. Aktuelle Pfade sind insbesondere Art. 45 DSGVO über den EU-US Data Privacy Framework-Angemessenheitsbeschluss bei teilnehmenden US-Organisationen, Art. 46 DSGVO mit Standardvertragsklauseln/BCR plus TIA oder im Ausnahmefall Art. 49 DSGVO.

## Wann verwenden?

- Ein US-SaaS-, Cloud-, KI-, Support- oder Analyseanbieter verarbeitet personenbezogene Daten.
- Ein Anbieter behauptet DPF-Zertifizierung, aber Produkt, Konzernunternehmen, HR-Daten oder Subprozessoren sind unklar.
- Eine Aufsichtsbehörde fragt nach Drittlandtransfer, Schrems-II-Prüfung oder ergänzenden Maßnahmen.
- Ein AVV, DPA, SaaS-Vertrag oder Einkaufsvorgang braucht ein dokumentiertes Transfer Impact Assessment.
- Ein Altsystem berief sich früher auf Safe Harbor oder Privacy Shield und muss bereinigt werden.

## Intake

Frage nur fehlende Punkte ab. Wenn Unterlagen vorliegen, zuerst aus den Dokumenten extrahieren.

| Punkt | Konkret abfragen oder extrahieren |
|---|---|
| Exporteur | Verantwortlicher/Auftragsverarbeiter, Sitz, zuständige Aufsichtsbehörde, Rolle im Transfer |
| Importeur | US-Rechtsträger, Adresse, Mutter-/Tochtergesellschaft, DPF-Name, Produktname |
| Daten | Kategorien personenbezogener Daten, besondere Kategorien Art. 9 DSGVO, Beschäftigtendaten, Mandantendaten |
| Zwecke | Hosting, Support, Fernwartung, Analyse, KI-Training, Ticketing, CRM, Sicherheit, Abrechnung |
| Zugriff | Speicherung USA, Remote Access, Subprozessoren, Support Level, Zugriff durch US-Personen |
| Transferpfad | DPF, SCC Modul 1-4, BCR, Art. 49, Kombination |
| Unterlagen | AVV/DPA, SCC, TOMs, Subprozessorliste, DPF-Auszug, Security Whitepaper, Datenschutzhinweise |
| Frist | Behördenfrist, Vertragsdeadline, Go-live, Incident, Audit-Termin |

## Prüf- und Arbeitsworkflow

### 1. Transferlandkarte

Erstelle zuerst eine Tabelle:

| Verarbeitung | Datenexporteur | Datenimporteur | Land | Datenarten | Zweck | Empfänger/Subprozessor | Transferinstrument | Status |
|---|---|---|---|---|---|---|---|---|

Markiere getrennt:

- Primärtransfer in die USA.
- Onward Transfers zu Subprozessoren.
- Reiner Zugriff aus den USA auf EU-gehostete Daten.
- Konzerninterne Transfers.
- Support-/Fernwartungssituationen.

### 2. DPF-Listing-Check

Prüfe und dokumentiere:

1. Exakter Name des US-Rechtsträgers in der offiziellen DPF-Liste.
2. Status aktiv/inaktiv, Zertifizierungsdatum und Re-Zertifizierungsdatum.
3. Abdeckung EU-US DPF, nicht nur Swiss-US oder UK Extension.
4. Abdeckung der relevanten Datenkategorien, insbesondere HR-Daten.
5. Abdeckung des konkreten Produkts oder Dienstes, soweit aus DPF-Eintrag, Datenschutzerklärung und Vertrag ersichtlich.
6. Beschwerdemechanismus, unabhängige Streitbeilegung und Kontaktstellen.
7. Onward-Transfer-Regeln und Subprozessoren.
8. Screenshot-/PDF-/Abrufnachweis mit Datum und Bearbeiter.

**Bewertung:**

- `DPF tragfähig`: Exakter Importeur ist aktiv gelistet und der konkrete Transfer ist abgedeckt.
- `DPF nur teilweise tragfähig`: Konzernmutter gelistet, Produkt/Tochter/HR-Daten/Subprozessoren unklar.
- `DPF nicht tragfähig`: Kein aktiver Eintrag oder Transfer außerhalb der Abdeckung.

### 3. Schrems-Historie sauber einordnen

Für die Akte:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EU-US Data Privacy Framework: aktueller Angemessenheitsbeschluss der EU-Kommission vom 10.07.2023; nutzbar nur für teilnehmende US-Organisationen im sachlichen Umfang der Zertifizierung.

Formuliere nie, dass Safe Harbor oder Privacy Shield heute eine gültige Rechtsgrundlage seien.

### 4. Alternativpfad SCC/BCR/TIA

Wenn DPF nicht eindeutig trägt, prüfe:

- SCC Modul 1: Verantwortlicher an Verantwortlichen.
- SCC Modul 2: Verantwortlicher an Auftragsverarbeiter.
- SCC Modul 3: Auftragsverarbeiter an Auftragsverarbeiter.
- SCC Modul 4: Auftragsverarbeiter an Verantwortlichen.
- BCR, wenn konzerninterne genehmigte Regeln nachweislich passen.
- Art. 49 DSGVO nur eng und ausnahmsweise; nicht als Dauerlösung.

Verweise für die konkrete SCC-Ausarbeitung auf `standardvertragsklauseln-scc-paket`.

### 5. Transfer Impact Assessment

Dokumentiere entlang dieser Struktur:

| Kapitel | Inhalt |
|---|---|
| A. Transferbeschreibung | Wer übermittelt was, wohin, zu welchem Zweck, wie oft und über welche Infrastruktur? |
| B. Transferinstrument | DPF, SCC/BCR oder Ausnahme; Begründung und Nachweise |
| C. Drittlandsrecht und Praxis | Relevante Zugriffsbefugnisse, Importeurangaben, Transparenzberichte, Warrant-Canary/Policy, tatsächliche Zugriffserfahrung |
| D. Risiko für Betroffene | Datenart, Sensibilität, Menge, Identifizierbarkeit, Schutzbedarf, mögliche Schäden |
| E. Ergänzende Maßnahmen | Verschlüsselung, Key Management in EU/EWR, Pseudonymisierung, Zugriffsbeschränkung, Logging, Challenge Policy, Transparenz |
| F. Restrestrisiko | Ampel, Begründung, offene Punkte, Entscheidungsträger |
| G. Wiedervorlage | Trigger: Zertifizierungsablauf, neue Subprozessoren, Produktänderung, Behördenpraxis, EuGH/EDSA-Update |

### 6. Ergebnislogik

Gib immer ein klares Ergebnis aus:

- **Freigabe möglich:** Transferinstrument trägt, Dokumente vollständig, Restrestrisiko vertretbar.
- **Freigabe mit Auflagen:** Nachbesserungen nötig, z. B. SCC-Anlagen, Key Management, Subprozessor-Auskunft, DPF-Nachweis.
- **Stop bis Klärung:** Importeur nicht identifizierbar, DPF nicht tragfähig, keine SCC, hohes ungemindertes Risiko.
- **Legacy-Bereinigung:** Alte Safe-Harbor-/Privacy-Shield-Dokumentation ablösen, neue Grundlage festlegen.

## Output-Paket

Erzeuge auf Wunsch ein zusammenhängendes Paket:

1. **Kurzvermerk für Geschäftsführung oder Mandant** mit Entscheidung und Restfragen.
2. **Transferregister-Auszug** nach Verarbeitungstätigkeit.
3. **DPF-Prüfvermerk** mit Abrufdatum, Treffer, Scope und Lücken.
4. **TIA-Vollvermerk** mit Maßnahmenmatrix.
5. **SCC/BCR-Verweisblatt** mit Modulwahl und Anlagenstatus.
6. **TOM- und Supplementary-Measures-Anlage**.
7. **Antwortbaustein für Aufsichtsbehörde**.
8. **Wiedervorlage- und Monitoringplan**.

## Quellen und Aktualität

- Stand: 05/2026.
- DSGVO Art. 44-49.
- EU-Kommission: EU-US Data Privacy Framework, Angemessenheitsbeschluss vom 10.07.2023.
- Offizielle DPF-Liste: Data Privacy Framework Program, Participant Search.
- EU-Kommission: Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914.
- EDSA: Recommendations 01/2020 zu ergänzenden Maßnahmen, Final Version 18.06.2021.

## 3. `verarbeitungsverzeichnis-vvt-generator`

**Fokus:** Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren. Art. 30 DSGVO VVT-Pflicht. Prüfraster: Pflichtangaben Art. 30 Abs. 1 Verantwortlicher Zweck Kategorien Empfaenger Fristen Massnahmen. Output: vollständiges VVT je Verarbeitungstätigkeit. Abgrenzung: nicht für Datenschutz-Folgenabschaetzung (dsfa-erstellung).

### VVT — Verzeichnis von Verarbeitungstätigkeiten

## Eingaben

- Anzahl Beschäftigte
- Branche / Geschäftsmodell
- Existierende AVV-Verträge
- Existierende DSFA-Auswertungen
- Verarbeitungs-Übersicht (welche Prozesse?)
- Dienstleister-Liste (Auftragsverarbeiter)

## Schritt 1 — Anwendungsbereich Art. 30 Abs. 5 DSGVO

### Grundregel

- VVT-Pflicht für **alle** Verantwortlichen und Auftragsverarbeiter

### Ausnahme

- Unternehmen mit **weniger als 250 Beschäftigten**
- Wenn Verarbeitungs nicht **regelmäßig**
- Wenn keine **besonderen Kategorien** Art. 9 oder strafrechtlichen Daten
- Wenn kein **Risiko für Rechte und Freiheiten** der Betroffenen

### Praktische Konsequenz

- **Fast alle Unternehmen** ab eingen Beschäftigten — VVT Pflicht
- HR-Verarbeitung führt regelmäßig zu Pflicht
- Auch Kleinunternehmen oft pflichtig
- **Sicherer Weg:** VVT erstellen unabhängig von Schwellen

## Schritt 2 — Inhalts-Pflichten Verantwortlicher Art. 30 Abs. 1

### Pro Verarbeitungs-Tätigkeit

a) **Name und Kontaktdaten** Verantwortlicher (und ggf. gemeinsam Verantwortliche Vertreter DSB)

b) **Zwecke** der Verarbeitung

c) **Kategorien** Betroffener

d) **Kategorien** personenbezogene Daten

e) **Kategorien** Empfänger (auch in Drittländern und internationale Organisationen)

f) Bei **Drittland-Übermittlungen** — Drittland-Bezeichnung und ggf. Geeignete Garantien (Art. 46) oder Bezeichnung als Übermittlung nach Art. 49

g) **Geplante Lösch-Fristen** der Daten-Kategorien

h) **Allgemeine Beschreibung der technischen und organisatorischen Maßnahmen** Art. 32

## Schritt 3 — Inhalts-Pflichten Auftragsverarbeiter Art. 30 Abs. 2

### Pro Auftrag

a) **Name und Kontaktdaten** Auftragsverarbeiter und jedes Verantwortlichen für den der Auftragsverarbeiter tätig wird

b) **Kategorien** Verarbeitungs-Tätigkeiten im Auftrag

c) **Drittland-Übermittlungen** wie beim Verantwortlichen

d) **Allgemeine Beschreibung TOMs**

## Schritt 4 — VVT-Struktur und Format

### Schriftlich oder elektronisch

- **Schriftform** ausreichend
- **Elektronisch** häufiger (Excel CRM-Modul Datenschutz-Software)
- **Vorlage** bei Aufsichtsbehörde auf Anforderung Art. 30 Abs. 4 DSGVO

### Empfohlene Struktur

```
VVT [Unternehmens-Name]
Stand: [Datum]
Verantwortlicher: [Name Anschrift]
DSB: [Name]

Aufgenommen: [Datum]
Letzte Änderung: [Datum]

Verarbeitungs-Tätigkeit Nr. [N]:

Zweck der Verarbeitung:
[Konkrete Beschreibung]

Rechtsgrundlage (Art. 6 / 9 DSGVO) — EMPFOHLEN
(Art. 30 fordert das nicht ausdrücklich, ist aber
für Aufsichtsbehörden-Prüfung sehr hilfreich):
[Rechtsgrundlage]

Kategorien Betroffener:
[z.B. Beschäftigte, Kunden, Lieferanten, Bewerber]

Datenkategorien:
[z.B. Stammdaten, Vertragsdaten, Zahlungsdaten,
besondere Kategorien]

Empfänger:
[z.B. Dienstleister IT, Lohnbüro, Behörden]

Drittland-Übermittlung:
[Ja/Nein; bei Ja: Land und Garantien]

Lösch-Frist:
[z.B. 10 Jahre nach Vertragsende — gesetzliche
Aufbewahrungspflicht]

TOMs:
[Verweis auf TOMs-Dokument]
```

## Schritt 5 — Typische Verarbeitungs-Tätigkeiten

### Personalwesen

- **Bewerber-Management**
- **Personalakten**
- **Gehalts-Abrechnung**
- **Zeit-Erfassung**
- **Personalentwicklung**
- **Krankheits-Verwaltung**

### Kunden-Beziehung

- **Vertrags-Anbahnung**
- **Vertragsabwicklung**
- **Kundenservice**
- **Marketing / Newsletter**
- **Kundenbewertungen**

### Lieferanten

- **Vertragsanbahnung**
- **Vertragsabwicklung**
- **Zahlungs-Verkehr**
- **Sanktions-Screening**

### Eigene Verarbeitung

- **Buchhaltung**
- **Steuer-Erklärung**
- **Compliance**
- **Risk-Management**
- **IT-Security-Logs**

### Webseite und Online

- **Cookies und Tracking**
- **Web-Analyse**
- **Newsletter**
- **Kontakt-Formular**

## Schritt 6 — Drittland-Übermittlung im VVT

### Pflichten

- **Drittland bezeichnen**
- **Empfänger nennen**
- **Garantie nach Art. 46 DSGVO** spezifizieren:
 - SCC (Standard-Vertrags-Klauseln)
 - BCR (Binding Corporate Rules)
 - Verhaltens-Regeln Art. 40
 - Zertifizierung Art. 42
 - Internationales Abkommen (z.B. EU-US Data Privacy Framework)
- Bei Art. 49 Ausnahme bezeichnen (Einwilligung Vertrag Lebenswichtige Interessen etc.)

### Anhang TIA (Transfer Impact Assessment)

- Bei jeder Drittland-Übermittlung
- Skill `drittlandstransfer-pruefung`

## Schritt 7 — Aktualisierungs-Management

### Anlässe für Aktualisierung

- **Neue Verarbeitungs-Tätigkeit** (z.B. neues Tool eingesetzt)
- **Geänderter Zweck** (z.B. Marketing-Verarbeitung)
- **Neuer Dienstleister** (AVV-Bezug)
- **Drittland-Wechsel**
- **Geänderte Lösch-Fristen**
- **Neue Datenkategorien**

### Frequenz

- **Bei jeder Änderung** zeitnah
- **Mindestens jährliche Vollprüfung**
- **Nach DSFA-Aktualisierung**

### Verantwortliche

- **DSB** koordinierend
- **Fachbereich** für inhaltliche Aktualisierung
- **IT** für TOMs-Bestätigung

## Schritt 8 — Verzahnung mit AVV Art. 28 DSGVO

### Auftragsverarbeitung in VVT

- Pro AVV → Eintrag in VVT
- AVV-Inhalt teilweise direkt übernehmbar
- Vertragsbeginn / -ende dokumentieren

### Sub-Verarbeiter

- Bei Genehmigung Sub-Auftragsverarbeiter — neue VVT-Position
- Bei Sub-Auftragsverarbeiter-Wechsel — VVT-Update

## Schritt 9 — Verzahnung mit DSFA Art. 35

### DSFA-Pflicht-Verarbeitungen

- Hohes Risiko für Rechte und Freiheiten
- Im VVT besonders zu markieren
- DSFA-Ergebnis dokumentieren
- TOMs aus DSFA übernehmen

### Bei Hochrisiko KI-System

- DSFA plus Grundrechte-Folgenabschätzung (Art. 27 KI-VO)
- Skill `ki-verordnung-compliance`

## Schritt 10 — Pflicht-Vorlage Aufsichtsbehörde

### Anlässe

- **Aufsichtsbehörden-Anfrage** Standard-Auskunft
- **Datenpanne-Meldung** mit VVT-Bezug
- **DSGVO-Prüfung** (Audit)
- **Bei Bußgeld-Verfahren**

### Form der Vorlage

- Schriftlich elektronisch
- Vollständigkeit
- Aktualität
- Sprache deutsch

### Bei Mangel

- Bußgeld nach Art. 83 Abs. 4 lit. a DSGVO (bis EUR 10 Mio oder 2 Prozent Konzernumsatz)
- Aufforderung zur Nach-besserung mit Frist

## Schritt 11 — Praktische Aufbau-Schritte

### Phase 1 — Bestandsaufnahme

- Workshop mit allen Fachbereichen
- Verarbeitungs-Inventar
- Daten-Fluss-Diagramm

### Phase 2 — Strukturierung

- Tätigkeits-Liste
- Kategorisierung
- Datenkategorien-Mapping

### Phase 3 — Dokumentation

- VVT-Vorlage ausfüllen
- DSB-Review
- Geschäftsführung-Freigabe

### Phase 4 — Aktualisierung

- Change-Management-Prozess
- Periodische Reviews
- Trigger-basierte Updates

## Schritt 12 — Tool-Empfehlung

### Excel-basiert

- Sinnvoll für kleinere Organisation
- Vorlagen vom BfDI / Aufsichtsbehörden

### Datenschutz-Software

- Otris
- DataGuard
- Activemind
- bestätigt durch BSI-Standards

### CRM-/IT-Integration

- Automatische Erkennung Verarbeitungen
- Anbindung an AVV-Datenbank
- Anbindung an DSFA-Tool

## Schritt 13 — Beispiel Verarbeitungs-Tätigkeit

```
Verarbeitungs-Tätigkeit Nr. 5: Newsletter-Versand

Zweck: Information bestehender und potentieller
Kunden über Produkt-Updates und Branchen-Themen

Rechtsgrundlage: Art. 6 Abs. 1 lit. a DSGVO
(Einwilligung); § 7 Abs. 2 Nr. 3 UWG bei
Bestandskunden

Kategorien Betroffener: Kunden, Interessenten,
Newsletter-Abonnenten

Datenkategorien:
- E-Mail-Adresse
- Vor- und Nachname (optional)
- Einwilligungs-Datum und -Inhalt
- Anrede (optional)
- Click-Verhalten (Öffnungsrate, Click-Tracking)

Empfänger:
- Newsletter-Versand-Dienstleister Mailchimp Inc. (USA)
- Interne Vertriebs- und Marketing-Abteilung

Drittland-Übermittlung:
USA, Mailchimp Inc.
Garantie: EU-US Data Privacy Framework
(Aktualisierung 2023)
TIA durchgeführt: ja, Skill drittlandstransfer-pruefung

Lösch-Frist:
- Aktive Abonnenten: Bis zum Widerruf
- Nach Widerruf: 3 Jahre Aufbewahrung der
 Widerrufs-Information (Beweis-Funktion)
- Click-Verhalten: 13 Monate (Statistik-Auswertung)

TOMs:
- HTTPS-Verschlüsselung
- Pseudonymisiertes Tracking
- Mailchimp ISO 27001 zertifiziert
- AVV vorhanden gem. Art. 28 DSGVO
```

## Verzahnung mit anderen Skills

- `dsfa-erstellung` — bei DSFA-pflichtigen Verarbeitungen
- `avv-pruefung` — bei Auftragsverarbeitung
- `drittlandstransfer-pruefung` — bei Drittland-Bezug
- `ki-verordnung-compliance` — bei KI-Verarbeitung
- `anwendungsfall-triage` — bei neuem Anwendungsfall
- `datenpanne-meldung` — bei Vorfall

## Ausgabe

- `vvt-{unternehmen}.md` strukturierte VVT-Erstellung
- Erstausgabe Excel oder Markdown
- Aktualisierungs-Trigger-Liste
- Aufsichts-Behörden-Antwort-Vorbereitung
- Frist im Fristenbuch (jährlich Vollprüfung)

## Quellen

- DSGVO Art. 30 5 6 9 30 32 35 46 49
- BDSG-Anpassungen
- KI-VO Art. 27
- BfDI-Mustervorlagen
- DSK Kurzpapiere zur VVT
- EDSA Guidelines
- BVerfG-Linien zur Datenschutz-Verantwortung

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Erstmals anlegen oder bestehenden VVT aktualisieren?
2. Aus Sicht des Verantwortlichen (Art. 30 Abs. 1 DSGVO) oder Auftragsverarbeiters (Art. 30 Abs. 2)?
3. Unterliegt die Organisation der Pflicht? (Art. 30 Abs. 5 DSGVO: unter 250 Mitarbeiter nur bei bestimmten Verarbeitungen)
4. Welche Quellen stehen bereit? (bestehende Systemliste, AVV-Bestand, IT-Asset-Verzeichnis)

## Output-Template — VVT-Eintrag (Verantwortlicher)

**Adressat:** DSB / Aufsichtsbehörde — Tonfall: sachlich-strukturiert

```
VVT-Eintrag [DATUM]
Verantwortlicher: [NAME, ADRESSE, VERTRETER]
DSB: [NAME, KONTAKT] (falls bestellt)

Verarbeitungstätigkeit: [BEZEICHNUNG]
Zweck(e): [ZWECKE nach Art. 30 Abs. 1 lit. b]
Betroffene Gruppen: [GRUPPEN nach Art. 30 Abs. 1 lit. c]
Datenkategorien: [KATEGORIEN nach Art. 30 Abs. 1 lit. c]
Empfaenger (Kategorien): [EMPFAENGER nach Art. 30 Abs. 1 lit. d]
Drittlandtransfer: [LAND / Schutzmechanismus nach Art. 30 Abs. 1 lit. e]
Loeschfristen: [FRISTEN nach Art. 30 Abs. 1 lit. f]
TOM (Verweis): Art. 32 DSGVO — Anlage [X]
Rechtsgrundlage (Empfehlung): Art. [X] DSGVO [§ BDSG]
```

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

