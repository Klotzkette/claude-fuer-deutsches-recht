---
name: drittlandstransfer-pruefung
description: "Prueft Datenuebermittlungen in Drittlaender nach Art. 44 ff. DSGVO: Angemessenheitsbeschluesse (USA: EU-US Data Privacy Framework 2023, UK, Schweiz), Standardvertragsklauseln (SCC 2021 Module 1 bis 4), Transfer Impact Assessment nach EuGH C-311/18 Schrems II, BCR und Ausnahmen nach Art. 49 DSGVO."
---

# Drittlandstransfer-Prüfung (Art. 44 ff. DSGVO)

## Zweck

Dieser Skill greift bei jeder Auslagerung personenbezogener Daten an Empfänger außerhalb der EU/des EWR: US-Cloud-Dienste, Konzernverbund-Transfer, KI-Provider, Sub-Auftragsverarbeiter in Drittstaaten. Er führt strukturiert durch die mehrstufige Prüfung gemäß Kapitel V DSGVO, berücksichtigt den Angemessenheitsbeschluss vom 10. Juli 2023 für die USA (EU-US Data Privacy Framework) sowie die Schrems-II-Anforderungen an Standardvertragsklauseln und ergänzende Maßnahmen.

Anwendungsfälle: Kanzlei oder Unternehmen moechte einen US-amerikanischen SaaS-Dienst einsetzen; Konzernmutter in der Schweiz soll Zugriff auf EU-Kundendaten erhalten; Auftragsverarbeiter setzt Sub-Auftragsverarbeiter in Indien ein; Drittlandbezug bei AVV-Prüfung erkannt.

## Eingaben

- Empfängerstaat (z.B. USA, Indien, UK, China)
- Empfänger: Verantwortlicher (Modul 1/3 SCC) oder Auftragsverarbeiter (Modul 2/4 SCC)
- Datenkategorien (Art. 4 Nr. 1 DSGVO; Art. 9/10 DSGVO-Sonderkategorien?)
- Art der Datenverarbeitung (Speicherung, Analyse, Support-Zugriff, Hosting, Backup)
- Liegt bereits ein Transfer Impact Assessment vor? Falls ja, als Dokument einreichen
- Sitz und DPF-Zertifizierungsstatus des Empfängers (für USA: data.privacyframework.gov prüfen)

## Rechtlicher Rahmen

### Primaernormen

- **Art. 44 DSGVO** – Allgemeines Prinzip: Kein Transfer ohne geeignete Garantien oder Ausnahme; gilt auch für Weiterverarbeitung nach Transfer
- **Art. 45 DSGVO** – Angemessenheitsbeschluss der Kommission; kein zusätzliches Genehmigungserfordernis bei positiver Entscheidung
- **Art. 46 DSGVO** – Geeignete Garantien: Standardvertragsklauseln (SCC), Binding Corporate Rules (BCR), Verhaltensregeln mit verbindlichen Verpflichtungen, Zertifizierungsmechanismen
- **Art. 47 DSGVO** – Verbindliche interne Datenschutzvorschriften (BCR); Genehmigung durch federführende Aufsichtsbehörde erforderlich
- **Art. 49 DSGVO** – Ausnahmen: Einwilligung (Art. 49 Abs. 1 lit. a), Vertragserfordernis (lit. b/c), wichtige Gründe des öffentlichen Interesses (lit. d), Rechtsansprueche (lit. e), lebenswichtige Interessen (lit. f), öffentliches Register (lit. g); Abs. 1 Satz 2: gelegentliche, nicht systematische Transfers bei zwingender Notwendigkeit
- **Art. 4 Nr. 23 DSGVO** – Definition „Internationale Organisation"
- **Art. 13 Abs. 1 lit. f, Art. 14 Abs. 1 lit. f DSGVO** – Informationspflicht über Drittlandtransfer und Transfermechanismus

### Rechtsprechung und Leitlinien

- **EuGH, Urt. v. 16.07.2020 – C-311/18 (Data Protection Commissioner/Facebook Ireland und Maximillian Schrems), NJW 2020, 2945** (Schrems II): Der EuGH erklärt den EU-US-Privacy-Shield-Angemessenheitsbeschluss für ungültig (Rn. 201). Standardvertragsklauseln bleiben als Transfermechanismus gültig, jedoch nur dann, wenn der Verantwortliche oder Auftragsverarbeiter vor der Übermittlung sicherstellt, dass im Drittland ein dem Unionsrecht aequivalentes Schutzniveau gewaehrleistet ist (Rn. 134). Der Verantwortliche muss prüfen, ob das Rechtssystem des Empfängerlandes einen Schutz bietet, der dem in der Union garantierten Schutzniveau der Sache nach gleichwertig ist; ist dies nicht der Fall, ist die Übermittlung zu unterlassen (Rn. 142–146). `[Modellwissen – Vollzitat geprueft]`
- **EuGH, Urt. v. 06.10.2015 – C-362/14 (Maximillian Schrems/Data Protection Commissioner), NJW 2015, 3151** (Schrems I): Ungültigkeitserklärung des Safe-Harbor-Angemessenheitsbeschlusses; Grundlage für Schrems II
- **EDSA, Empfehlungen 01/2020 zu Maßnahmen zur Ergänzung von Übermittlungsinstrumenten**, angenommen am 18.06.2021 (Version 2.0): Sechsstufige Pruefmethodik für Transfer Impact Assessment (TIA); massgeblich für die Schrems-II-Umsetzung in der Praxis
- **EDSA, Leitlinien 05/2021 zum Zusammenwirken von Art. 3 und Kapitel V DSGVO**, angenommen am 18.11.2021: Klärung, wann der raeumliche Anwendungsbereich (Art. 3 DSGVO) und die Drittlandregeln (Kapitel V) kumulativ oder alternativ gelten
- **DSK Orientierungshilfe Drittstaatentransfer**: Handlungsempfehlungen für verantwortliche Stellen bei Transfers in Drittlaender; abrufbar auf dskonferenz.de `[Modellwissen – aktuellen Stand pruefen]`

### Aktuelle Angemessenheitsbeschlüsse (Stand 05/2026)

| Staat | Beschluss | Hinweis |
|---|---|---|
| **USA** | EU-US Data Privacy Framework, Beschluss der Kommission vom 10.07.2023 (C(2023) 4745 final) | Nur für zertifizierte Unternehmen auf der DPF-Liste; Prüfung auf data.privacyframework.gov erforderlich |
| **UK** | Angemessenheitsbeschluss vom 28.06.2021 (Beschluss 2021/1772/EU) | Gilt vorbehaltlich Überprüfung; nach Brexit-Änderungen des britischen Datenschutzrechts beobachten |
| **Schweiz** | Angemessenheitsbeschluss der Kommission; erneuert im Kontext des CH-Datenschutzgesetzes (nDSG, in Kraft ab 01.09.2023) | Teilweiser Angemessenheitsbeschluss; Praxis nach CH-DSG-Reform beachten |
| **Andorra** | Beschluss 2010/625/EU |  |
| **Argentinien** | Beschluss 2003/490/EG |  |
| **Faeroeer** | Beschluss 2010/146/EU |  |
| **Guernsey** | Beschluss 2003/821/EG |  |
| **Isle of Man** | Beschluss 2004/411/EG |  |
| **Israel** | Beschluss 2011/61/EU |  |
| **Japan** | Beschluss vom 23.01.2019 (2019/419/EU) | Mit gegenseitiger Anerkennung; Einschraenkungen beachten |
| **Jersey** | Beschluss 2008/393/EG |  |
| **Kanada** | Beschluss 2002/2/EG | Nur für Organisationen, die dem PIPEDA unterliegen; Bundesbehörden ausgenommen |
| **Neuseeland** | Beschluss 2013/65/EU |  |
| **Suedkorea** | Beschluss vom 17.12.2021 (2022/254/EU) | Erster Angemessenheitsbeschluss in Asien außerhalb Japan |
| **Uruguay** | Beschluss 2012/484/EU |  |

## Ablauf

### 1. Identifizierung des Drittlandstransfers

Prüfen, ob überhaupt ein Transfer i.S.d. Kapitel V DSGVO vorliegt:
- Findet eine Übermittlung an einen Empfänger außerhalb EU/EWR statt?
- Genügt ein „Zugriff" (z.B. Remote-Support, Administrationszugang) aus einem Drittland – nach EDSA-Leitlinien 05/2021 ja, wenn personenbezogene Daten im Zugriffsmittelpunkt stehen
- Art. 3 Abs. 2 DSGVO (extraterritoriale Anwendung): Liegt der Empfänger zwar im Drittland, faellt aber schon unter den raeumlichen Anwendungsbereich der DSGVO? Dann kein Kapitel-V-Transfer, aber Compliance-Prüfung nach Leitlinien 05/2021

### 2. Prüfung Angemessenheitsbeschluss (Art. 45 DSGVO)

- Liegt für das Empfängerland ein gültiger Angemessenheitsbeschluss der Kommission vor? (Tabelle oben)
- **USA:** Ist der Empfänger auf der DPF-Liste eingetragen und für die relevanten Datenkategorien zertifiziert? (data.privacyframework.gov)
- Wenn Angemessenheitsbeschluss vorhanden: Transfer grundsaetzlich zulässig; Art. 13/14 DSGVO-Hinweispflicht beachten
- **Hinweis:** Angemessenheitsbeschlüsse koennen durch den EuGH für ungültig erklärt werden (vgl. Schrems I und II); bei politisch sensiblen Ländern Monitoring empfehlen

### 3. Geeignete Garantien (Art. 46 DSGVO) – falls kein Angemessenheitsbeschluss

**a) Standardvertragsklauseln (SCC) nach Beschluss 2021/914/EU:**

| Modul | Konstellation | Typischer Anwendungsfall |
|---|---|---|
| Modul 1 | Verantwortlicher (EU) → Verantwortlicher (Drittland) | Konzerntransfer, gemeinsam Verantwortliche |
| Modul 2 | Verantwortlicher (EU) → Auftragsverarbeiter (Drittland) | Cloud-Dienst, Hosting, Analytics |
| Modul 3 | Auftragsverarbeiter (EU) → Auftragsverarbeiter (Drittland) | Sub-Auftragsverarbeiter |
| Modul 4 | Auftragsverarbeiter (Drittland) → Verantwortlicher (EU) | Ruecktransfer verarbeiteter Daten |

Prüfpunkte bei SCC: Richtiges Modul? Technische Anlage (Anhang I A–C und II) vollständig ausgefüllt? Technische Maßnahmen (Anhang II TOMs) konkret und nicht pauschal?

**b) Binding Corporate Rules (BCR):**
- Genehmigung durch federführende Aufsichtsbehörde nach Art. 47 DSGVO
- Umfang: alle Konzernunternehmen, die die BCR unterzeichnet haben
- BCR-Update nach Schrems II erforderlich; EDSA-Empfehlungen 01/2020 gelten auch für BCR

**c) Verhaltensregeln mit Verpflichtungen (Art. 46 Abs. 2 lit. e DSGVO):**
- Muss von zuständiger Aufsichtsbehörde genehmigt sein
- In der Praxis bisher wenig verbreitet

**d) Zertifizierungsmechanismen (Art. 46 Abs. 2 lit. f DSGVO):**
- Zertifizierungseinrichtung muss akkreditiert sein; Verpflichtung des Importeurs erforderlich

### 4. Transfer Impact Assessment (TIA) nach Schrems II

Nach EuGH C-311/18 Rn. 134 und EDSA-Empfehlungen 01/2020 muss bei SCC-Transfers geprüft werden, ob das Rechtssystem des Empfängerlandes die Wirksamkeit der SCC nicht untergrabt.

**TIA Sechsstufige Methodik (EDSA-Empfehlungen 01/2020):**

1. **Schritt 1:** Alle Übermittlungen kartieren (Zweck, Datenart, Empfänger, Empfängerland)
2. **Schritt 2:** Transfermechanismus identifizieren (SCC, BCR etc.)
3. **Schritt 3:** Rechtslage im Empfängerland beurteilen: Massengesetze (FISA Section 702, USA CLOUD Act), Behördenzugriffsrechte, Rechtsschutzmöglichkeiten für Betroffene, Zugang zu unabhängigen Gerichten
4. **Schritt 4:** Prüfen, ob Recht und Praxis die SCC-Schutzwirkung unterlaufen (Schrems-II-Kriterium: aequivalentes Schutzniveau)
5. **Schritt 5:** Ergänzende Maßnahmen identifizieren und umsetzen (s. Abschnitt 5)
6. **Schritt 6:** Formale Schritte (Vertrag schließen, ggf. Aufsichtsbehörde informieren, Dokumentation)

### 5. Ergänzende Maßnahmen (EDSA-Empfehlungen 01/2020)

Bei unzureichendem Schutzniveau im Empfängerland koennen ergänzende Maßnahmen die Schutzlücke schließen:

**Technische Maßnahmen:**
- Ende-zu-Ende-Verschlüsselung mit Schlüsselhoheit beim Verantwortlichen in der EU (Schlüsselmanagement-Standort entscheidend)
- Pseudonymisierung vor Transfer; Zuordnungsschlüssel verbleibt in der EU
- Zero-Knowledge-Architektur für Cloud-Dienste

**Vertragliche Maßnahmen:**
- Erweiterung der SCC um technische Spezifikation der Verschlüsselung
- Verpflichtung des Importeurs zur Benachrichtigung bei Behördenzugang
- Audit-Rechte für Drittland-Compliance

**Organisatorische Maßnahmen:**
- Datensparsamkeit: nur pseudonymisierte/aggregierte Daten übermitteln
- Trennung von Supportzugriff und Produktionsdaten

### 6. Dokumentation und Informationspflichten

- Verarbeitungsverzeichnis (Art. 30 DSGVO): Transfer, Empfängerland, Mechanismus, TIA vermerken
- Datenschutzerklärung (Art. 13 Abs. 1 lit. f DSGVO): Drittlandtransfer, Mechanismus und ggf. Kopienangebot der SCC erwaehnen
- AVV (Art. 28 Abs. 3 DSGVO): Sub-AV-Kette mit Drittlandsangaben; TIA als Anlage
- TIA als internes Dokument archivieren und bei Anfragen der Aufsichtsbehörde vorlegen koennen

## Pruefschema TIA (Checkliste)

- [ ] **Lokale Massengesetze:** Erlauben Gesetze des Empfängerlandes Massensammlung (z.B. FISA 702, EO 12333 für USA; Geheimdienstgesetze CN, RU)?
- [ ] **Behördenzugriff auf Daten:** Koennen Behörden ohne richterliche Kontrolle auf Daten zugreifen? Wie haeufig werden solche Befugnisse genutzt (Transparenzberichte)?
- [ ] **Verschlüsselung at rest:** Sind Daten beim Empfänger verschlüsselt gespeichert? Wer hat Zugriff auf Schlüssel?
- [ ] **Verschlüsselung in transit:** Wird TLS/mTLS verwendet? Zertifikate kontrolliert?
- [ ] **Schlüsselmanagement-Standort:** Befinden sich Schlüssel und HSMs in der EU? Oder Schlüsselhoheit beim Empfänger im Drittland?
- [ ] **Sub-Processor-Mapping:** Welche Sub-Auftragsverarbeiter des Empfängers befinden sich ebenfalls in Drittlaendern? TIA für Sub-Processor?
- [ ] **Rechtsschutz für Betroffene:** Haben EU-Betroffene Klagemöglichkeiten im Empfängerland oder über Rechtsbehelfsinstanz (z.B. Data Protection Review Court der USA)?
- [ ] **Transparenzberichte:** Veröffentlicht der Empfänger Behördenanfragen (Government Disclosure Reports)?

## Risikoampel

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| US-Cloud ohne DPF-Zertifizierung und ohne SCC | x | | |
| US-Cloud mit SCC, ohne TIA | | x | |
| US-Cloud mit DPF-zertifiziertem Anbieter | | | x (zzgl. SCC und TIA empfohlen als Doppelabsicherung) |
| US-Cloud mit SCC und positivem TIA (Verschlüsselung, Schlüssel EU) | | | x |
| UK (Angemessenheitsbeschluss 2021 gültig) | | | x (Monitoring erforderlich) |
| Schweiz nach nDSG (Angemessenheitsbeschluss bestätigt) | | | x |
| Indien ohne SCC | x | | |
| Indien mit SCC und TIA | | x | |
| China ohne Mechanismus | x | | |
| BCR-gedeckter Konzernverbund, TIA positiv | | | x |
| Art. 49 DSGVO Einwilligung, nicht systematisch | | x | |

## Vorlagen und Bausteine

### TIA-Bericht Musterstruktur

```
TIA – Transfer Impact Assessment
Datum: [DATUM]
Erstellt von: [DSB / Datenschutzbeauftragter]
Empfaengerland: [LAND]
Empfaenger: [NAME, Adresse]
Transfermechanismus: [SCC Modul X / BCR / DPF]
Datenkategorien: [Auflistung]

1. Kartierung der Uebermittlung
   [Zweck, Umfang, Haeufigkeit]

2. Rechtslage im Empfaengerland
   [Relevante Gesetze, Massengesetze, Behoerdenzugriffsrechte]
   Quellen: [Transparenzberichte, Rechtsgutachten, EDSA-Laenderanalysen]

3. Schutzlueckenanalyse
   [Unterlaefen lokale Gesetze die SCC-Schutzwirkung? Pruefung nach EuGH C-311/18 Rn. 134 ff.]

4. Ergaenzende Massnahmen
   [Verschluesselung, Pseudonymisierung, vertragliche Massnahmen]

5. Ergebnis und Restrisiko
   [Gruen / Orange / Rot – Begruendung]

6. Massnahmenplan
   [Bei Orange oder Rot: konkrete Abhilfemassnahmen mit Frist und Verantwortlichen]

Unterschrift DSB: _____________
Freigabe Datenschutzbeauftragter: _____________
```

### SCC-Modul-Auswahl-Matrix (Entscheidungsbaum)

```
Wer ist Exporteur?
├─ Verantwortlicher in EU
│  ├─ Importeur = Verantwortlicher im Drittland → Modul 1
│  └─ Importeur = Auftragsverarbeiter im Drittland → Modul 2
└─ Auftragsverarbeiter in EU
   ├─ Importeur = Auftragsverarbeiter im Drittland (Sub-AV) → Modul 3
   └─ Importeur = Verantwortlicher im Drittland (Ruecktransfer) → Modul 4
```

### Datenschutzerklärungsbaustein Drittlandtransfer

> „Wir übermitteln personenbezogene Daten an Empfänger in [LAND]. Die Übermittlung erfolgt auf Grundlage von [EU-Standardvertragsklauseln nach Beschluss 2021/914/EU, Modul X / Angemessenheitsbeschluss der Kommission vom [DATUM]]. Für die USA gilt: der Empfänger ist unter dem EU-US Data Privacy Framework zertifiziert. Eine Transferfolgenabschätzung (TIA) liegt vor. Auf Anfrage stellen wir Ihnen eine Kopie der Standardvertragsklauseln zur Verfügung (Kontakt: [DSB])."

## Querverweise

- `datenschutzrecht/skills/avv-pruefung/SKILL.md` – Drittlandtransfer-Prüfung im AVV-Kontext (Schritt 5)
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` – DSFA bei Hochrisiko-Drittlandtransfers
- `datenschutzrecht/skills/mandantendaten-ki/SKILL.md` – Drittlandtransfer bei KI-Diensten für Berufsgeheimnisträger
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` – Datenpannen bei Drittlandempfaengern
- `datenschutzrecht/skills/regulierungs-luecken-analyse/SKILL.md` – Neue Angemessenheitsbeschlüsse in Gap-Analyse einspielen

## Risiken und typische Fehler

- **DPF-Prüfung vergessen:** DPF-Zertifizierung ist nicht permanent; Unternehmen koennen ihre Zertifizierung verlieren. Vor jedem Transfer auf data.privacyframework.gov prüfen und erneut prüfen bei Vertragserneuerung.
- **Falsches SCC-Modul:** Ein Verantwortlicher, der SCC-Modul 3 (AV-zu-AV) verwendet, obwohl er selbst Verantwortlicher ist, erzeugt keine schutzwirkende Grundlage. Konstellation vor Unterzeichnung zwingend prüfen.
- **TIA als Formalie:** EuGH C-311/18 Rn. 134: Die Prüfung muss ehrlich und konkret sein; pauschal „Risiko akzeptabel" ohne Begründung genuegt nicht. Transparenzberichte auswerten.
- **Art. 49 DSGVO als Regelfall:** Die Ausnahmen des Art. 49 DSGVO sind auf Einzelfälle beschraenkt; systematische und regelmäßige Transfers auf dieser Basis sind nicht zulaessig (EDSA-Leitlinien 2/2018).
- **Sub-Processor-Kette übersehen:** SCC Modul 2/3 legt dem Importeur Pflichten für Sub-Auftragsverarbeiter auf; deren Drittlandstatus muss ebenfalls abgesichert sein (Art. 28 Abs. 4 DSGVO).
- **Schlüsselhoheit nicht geprüft:** Verschlüsselung schuetzt nur dann, wenn Schlüssel nicht im Drittland liegen. Cloud-Dienste mit US-Schlüsselmanagement bieten keinen vollständigen Schutz gegen FISA 702-Zugriffe.
- **Angemessenheitsbeschluss validitaet nicht geprüft:** Nach Schrems I und II koennen Angemessenheitsbeschlüsse wegfallen. Monitoring-Pflicht für sensible Verarbeitungen.

## Quellen und Updates

Stand: 05/2026. Aktualität bei folgenden Ereignissen prüfen und Skill aktualisieren:
- Neue Angemessenheitsbeschlüsse der Europaeischen Kommission
- EuGH-Urteile zu Kapitel V DSGVO
- Änderungen am DPF (data.privacyframework.gov – politische und rechtliche Entwicklungen USA)
- Neue BCR-Anerkennungen durch Aufsichtsbehörden
- Aktualisierungen der EDSA-Empfehlungen 01/2020
- Örtliche Datenschutzgesetze in Drittlaendern (z.B. CLOUD Act Amendments, neue chinesische Datenschutzgesetze PIPL)

Nächste geplante Überprüfung: 05/2027 oder bei wesentlichen Änderungen.
