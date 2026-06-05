---
name: notar-paket-parteien-erfassen
description: "Notar Paket Parteien Erfassen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Notar Paket Parteien Erfassen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Notar Paket Parteien Erfassen** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notar-paket-uebermittlung` | Notarpaket für Beurkundungstermin bei Kapitalerhohung durch Wandlung zusammenstellen und uebermitteln. §§ 15 55 GmbHG BeurkG. Prüfraster: Vollständigkeit Beschluss Zeichnungsschein Gesellschafterliste Vollmachten Identitätsnachweise. Output: Notarpaket Checkliste Begleitschreiben. Abgrenzung: nicht für Handelsregisteranmeldung nach Beurkundung. |
| `parteien-erfassen` | Vertragsparteien eines Wandeldarlehens vollständig identifizieren und dokumentieren. §§ 13 17 GmbHG Gesellschafter §§ 305 ff. BGB AGB bei mehreren Darlehensgebern. Prüfraster: Darlehensgeberin Darlehensnehmerin vertretungsberechtigte Organe Handelsregisterstand. Output: Parteiendossier für Vertragskopf. Abgrenzung: Einstiegs-Skill; vor Vertragserstellung zu verwenden. |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Notar Paket Parteien Erfassen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `notar-paket-uebermittlung`

**Fokus:** Notarpaket für Beurkundungstermin bei Kapitalerhohung durch Wandlung zusammenstellen und uebermitteln. §§ 15 55 GmbHG BeurkG. Prüfraster: Vollständigkeit Beschluss Zeichnungsschein Gesellschafterliste Vollmachten Identitätsnachweise. Output: Notarpaket Checkliste Begleitschreiben. Abgrenzung: nicht für Handelsregisteranmeldung nach Beurkundung.

# Notar-Paket zur Handelsregister-Anmeldung

## Zweck

Dieser Skill stellt das vollständige Paket für den Notar zusammen, der die Kapitalerhöhung beim Handelsregister anmeldet. Phase D des Lebenszyklus.

## Eingaben

- Notariell beurkundeter Kapitalerhöhungsbeschluss (aus `gesellschafterbeschluss-kapitalerhoehung`)
- Sacheinlagebericht (aus `sacheinlagebericht-werthaltigkeit`)
- Aktuelle Gesellschafterliste (§ 40 GmbHG, aus `gesellschafterliste-aktualisieren`)
- Name und Anschrift des zuständigen Notars
- Handelsregisternummer und zuständiges Amtsgericht

## Rechtlicher Rahmen

### Primärnormen
- § 57 GmbHG (Anmeldung der Kapitalerhöhung – durch Geschäftsführerin beim Registergericht)
- § 57a GmbHG (Inhalt der Anmeldung: Betrag der Kapitalerhöhung, neue Gesellschafterliste)
- § 40 GmbHG (Gesellschafterliste – nach Kapitalerhöhung neue Liste beim Handelsregister)
- § 78 GmbHG (Notarielle Beglaubigung der Anmeldung)
- § 8 GmbHG (Inhalt der Anmeldung allgemein)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Vollständigkeitsprüfung des Notar-Pakets

| Dokument | Status |
|---|---|
| Notariell beurkundeter Kapitalerhöhungsbeschluss | [ ] |
| Notariell beurkundete Übernahmeerklärung Lender | [ ] |
| Sacheinlagebericht (unterschrieben) | [ ] |
| Neue Gesellschafterliste (§ 40 GmbHG) | [ ] |
| Anmeldung Kapitalerhöhung (§ 57 GmbHG, von Notar vorbereitet) | [ ] |
| Nachweis Leistung Sacheinlage (Forderungsabtretung oder Konfusionsnachweis) | [ ] |

### 2. Gesellschafterliste vorbereiten (§ 40 GmbHG)
Nach Kapitalerhöhung neue Liste mit: fortlaufender Nummer, Name, Geburtsdatum, Wohnanschrift, Anteilszahl, Nennwert, Datum Erwerb. Alle Gesellschafterinnen plus neuer Lender. Unterschrift: Notar (§ 40 Abs. 2 GmbHG nach Kapitalerhöhung bei Notar-Mitwirkung) oder Geschäftsführerin.

### 3. Anmeldungstext § 57 GmbHG
"Die Geschäftsführerin der Sonnenglas Solartechnologie UG (haftungsbeschränkt) meldet zur Eintragung in das Handelsregister an: Die Kapitalerhöhung vom [Datum] in Höhe von EUR [Betrag] durch Ausgabe von [Anzahl] neuen Geschäftsanteilen mit einem Nennbetrag von je EUR 1,00 gegen Sacheinlage ist vollzogen. Der neue Gesellschafter hat die Sacheinlage vollständig erbracht." Notarielle Beglaubigung der Anmeldung.

### 4. Notar-Briefing
E-Mail an Notar mit: Kurzdarstellung des Vorgangs, Anlagen (Beschluss, Sacheinlagebericht, neue Gesellschafterliste), gewünschtes Datum der Einreichung, Kontakt für Rückfragen.

### 5. Bearbeitungsdauer abschätzen
Handelsregistereintragung in der Regel zwei bis acht Wochen nach Einreichung. Beschleunigte Eintragung auf Antrag in dringlichen Fällen möglich.

### 6. Transparenzregister-Folge-Anmeldung
Nach Kapitalerhöhung: Pflicht zur Aktualisierung des Transparenzregisters nach § 19 GwG (wirtschaftlich Berechtigte). Frist: unverzüglich. Notar erledigt dies regelmäßig mit.

## Inhaltsverzeichnis Notar-Paket

```
1. Beurkundetes Protokoll der außerordentlichen Gesellschafterversammlung
 vom [Datum], Urk.-Nr. [●] des Notars [●]
2. Beurkundete Übernahmeerklärung Northstar Pre-Seed Partners GmbH & Co. KG
 vom [Datum], Urk.-Nr. [●]
3. Sacheinlagebericht vom [Datum]
4. Neue Gesellschafterliste nach § 40 GmbHG
5. Anmeldung Kapitalerhöhung nach § 57 GmbHG
6. Nachweis Einbringung Sacheinlage (Forderungsabtretung)
[Gesamt: 6 Positionen]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sacheinlage vor Anmeldung nicht erbracht | § 57 GmbHG-Voraussetzung fehlt | Einbringungsnachweis unvollständig | Einbringung vollständig belegt |
| Gesellschafterliste nicht aktualisiert | § 16 GmbHG-Gutglaubenswirkung gefährdet | Liste in Erarbeitung | Aktuelle Liste beigefügt |
| Notar nicht in Beurkundungsbezirk | Zuständigkeitsproblem | Notar außerhalb prüfen | Zuständiger Notar |
| Transparenzregister nicht aktualisiert | GwG-Verstoß, Bußgeld | Frist läuft | Aktualisierung beauftragt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/handelsregisteranmeldung-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 57 ff. oder GwG § 19 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 53, 54, 55 GmbHG (Beurkundung Kapitalerhöhungsbeschluss + Übernahme) → § 56 Abs. 2 GmbHG (Sacheinlagebericht) → §§ 1-17 BeurkG (Beurkundungsgesetz, Pflichten Notar) → § 40 GmbHG (Gesellschafterliste nach Wandlung) → § 57 GmbHG (Handelsregisteranmeldung)

## 2. `parteien-erfassen`

**Fokus:** Vertragsparteien eines Wandeldarlehens vollständig identifizieren und dokumentieren. §§ 13 17 GmbHG Gesellschafter §§ 305 ff. BGB AGB bei mehreren Darlehensgebern. Prüfraster: Darlehensgeberin Darlehensnehmerin vertretungsberechtigte Organe Handelsregisterstand. Output: Parteiendossier für Vertragskopf. Abgrenzung: Einstiegs-Skill; vor Vertragserstellung zu verwenden.

# Parteien erfassen – KYC und Vertretungsmacht

## Zweck

Dieser Skill erfasst alle für den Wandeldarlehensvertrag erforderlichen Parteidaten vollständig und strukturiert. Er prüft Vertretungsmacht, dokumentiert Anschriften und bereitet die Vertragsparteien-Sektion vor. Außerdem initiiert er den Geldwäsche-Grundcheck (KYC). Phase A des Lebenszyklus.

## Eingaben

- Gesellschaft: Firmenname vollständig, Rechtsform, HRB-Nummer, Amtsgericht, Sitz, Geschäftsanschrift, Name Geschäftsführerin / Geschäftsführer mit Allein- oder Gesamtvertretung
- Gesellschafterin 1: Vor- und Nachname, Geburtsdatum, Wohnanschrift, Anteilszahl und Nennwert
- Gesellschafterin 2 (falls vorhanden): gleiche Daten
- Darlehensgeber: bei Privatperson Vor- und Nachname, Geburtsdatum, Wohnanschrift; bei juristischer Person Firma, HRB, Sitz, Vertreter mit Vollmachtsnachweis
- Sanktionslistenabfrage: EU-Amtsblatt Konsolidierte Liste, OFAC SDN, UN Security Council, HM Treasury

## Rechtlicher Rahmen

### Primärnormen
- § 164 BGB (Stellvertretung), § 167 BGB (Vollmacht)
- § 35 GmbHG (Vertretung GmbH durch Geschäftsführung)
- §§ 1, 2, 3, 4, 10, 11 GwG (KYC-Pflichten, wirtschaftlich Berechtigte, PEP)
- § 19 GwG (Transparenzregister)
- § 43 GmbHG (Pflichten der Geschäftsführung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Handelsregisterauszug anfordern / prüfen
Aktueller HR-Auszug nicht älter als drei Monate: Firma, Sitz, Stammkapital, Geschäftsführung, Vertretungsregelung, aktuelle Gesellschafterliste (§ 40 GmbHG).

### 2. Gesellschafterinnen identifizieren
Abgleich mit Gesellschafterliste. Vollständige Adressen und Geburtsdaten erfassen. Privatpersonen: Personalausweis oder Reisepass als Lichtbildausweis.

### 3. Darlehensgeber-KYC
Privatperson: Lichtbildausweis + ggf. Vollmacht. Juristische Person: HR-Auszug + Vertreternachweis + Gesellschafterliste für wirtschaftlich Berechtigte (§ 3 GwG: natürliche Person mit mehr als 25 Prozent).

### 4. Sanktionslistenabfrage
Alle Parteien gegen EU-Konsolidierte Liste (Art. 2 VO 765/2006), OFAC SDN, UN-Sicherheitsratsliste und HM Treasury Financial Sanctions screenen. Ergebnis dokumentieren.

### 5. PEP-Status prüfen
Politisch exponierte Person (§ 1 Abs. 12 GwG)? Prominente Amtsträger, Familienmitglieder? Erhöhte Sorgfalt bei Treffer.

### 6. Vertragsparteien-Sektion vorbereiten
Strukturierte Textblöcke für den Vertragskopf: Gesellschaft, Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber – mit allen Pflichtangaben.

## Beispiel-Parteiblock (DE)

```
(1) Sonnenglas Solartechnologie UG (haftungsbeschränkt)
 Geschäftsanschrift: Musterstraße 12, 10115 Berlin
 eingetragen im Handelsregister des Amtsgerichts Charlottenburg unter HRB 123456 B,
 vertreten durch ihre alleinvertretungsberechtigte Geschäftsführerin Dr. Mira Schoeneck,
 – nachstehend die "Gesellschaft" –

(2) Dr. Mira Schoeneck, geboren [Datum], Musterstraße 12, 10115 Berlin
 – nachstehend die "Gesellschafterin 1" –

(3) Lina Habersaat, geboren [Datum], Beispielweg 5, 20095 Hamburg
 – nachstehend die "Gesellschafterin 2" –

(4) Northstar Pre-Seed Partners GmbH & Co. KG
 Geschäftsanschrift: Venture-Allee 1, 60329 Frankfurt am Main
 eingetragen im Handelsregister des Amtsgerichts Frankfurt am Main unter HRA 99999,
 vertreten durch ihre Komplementärin Northstar Management GmbH, diese vertreten durch [●]
 – nachstehend der "Darlehensgeber" –
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sanktionslistentreffer | Vertrag nicht abschließen | Namensähnlichkeit ohne Treffer | Alle Checks negativ |
| PEP-Status | Verstärkte Sorgfaltspflichten, ggf. GF-Freigabe | Familienmitglied PEP | Kein PEP |
| Vollmacht fehlt | Vertrag schwebend unwirksam | Vollmacht in Vorbereitung | Vollmacht vorgelegt |
| HR-Auszug veraltet (über 3 Monate) | Vertretungsrisiko | 3 bis 6 Monate alt | Aktuell |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/kyc-aml-geldwaesche/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/mandat-triage-wandeldarlehen/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/bilinguale-vertragserstellung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GwG/GmbHG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 10, 11 GwG (Identifizierung wirtschaftlich Berechtigter) → §§ 18, 19 GwG (Transparenzregister) → § 40 GmbHG (Gesellschafterliste: Angaben Gesellschafter) → § 15 GmbHG (Abtretung, Übergang Anteile) → § 313 BGB (Identitätsbezeichnung in notariellen Urkunden)
