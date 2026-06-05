---
name: drohende-zahlungsunfaehigkeit
description: "Drohende Zahlungsunfaehigkeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Drohende Zahlungsunfaehigkeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Drohende Zahlungsunfaehigkeit** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `drohende-zahlungsunfaehigkeit-paragraph-18-inso` | Drohende Zahlungsunfähigkeit nach § 18 InsO feststellen: Berater oder GF prüft ob StaRUG-Zugangsberechtigung besteht. Normen: § 18 InsO (drohende ZU), § 17 InsO (aktuelle ZU), § 19 InsO (Überschuldung), § 1 StaRUG (Zugangsberechtigung). Prüfraster: Prognosezeitraum 24 Monate, Wahrscheinlichkeitsmassstab ueberwiegend wahrscheinlich, Abgrenzung zu § 17 InsO. Output Prüf-Memo drohende ZU, StaRUG-Zugangsberechtigung-Nachweis. Abgrenzung: Fortbestehensprognose (§ 19 InsO) siehe fortbestehensprognose-zweistufig; Insolvenzantragspflicht siehe insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist. |
| `fortbestehensprognose-zweistufig` | Zweistufige Fortbestehensprognose nach IDW S 11 erstellen: Unternehmen ist möglicherweise ueberschuldet und braucht positive Fortführungsprognose. Normen: § 19 InsO (Überschuldungsbegriff modifiziert), IDW S 11 (Fortbestehensprognose-Standard). Prüfraster: Stufe 1 Fortführungswille, Stufe 2 Fortführungsfähigkeit (GuV/Liquiditaet 12 vs. 24 Monate), Dokumentationspflicht, Sanierungsgutachten. Output Zweistufige Fortbestehensprognose, IDW-S-11-konformes Gutachten-Geruest. Abgrenzung: Drohende ZU siehe drohende-zahlungsunfähigkeit-paragraph-18-inso; integrierte Planung siehe integrierte-planung-guv-bilanz-cashflow. |
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont architektieren: Unternehmen will § 1 StaRUG Krisenfrueherkennung implementieren. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW S 6 (Sanierungsstandard), IDW PS 340 n.F. (Risikomanagement-Prüfung). Prüfraster: Risiko-Inventar, KPI-Kaskade, Eskalationsstufen, Reporting-Frequenzen, Schwellenwerte, Organisationseinbettung. Output Fruehwarnsystem-Konzept, Implementierungsplan, Governance-Struktur. Abgrenzung: KPI-Set Ampelsystem siehe kennzahlenset-und-ampelsystem-starug-konform; Liquiditaetsplanung siehe rollierende-liquiditaetsplanung-24-monate-template. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **Drohende Zahlungsunfaehigkeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `drohende-zahlungsunfaehigkeit-paragraph-18-inso`

**Fokus:** Drohende Zahlungsunfähigkeit nach § 18 InsO feststellen: Berater oder GF prüft ob StaRUG-Zugangsberechtigung besteht. Normen: § 18 InsO (drohende ZU), § 17 InsO (aktuelle ZU), § 19 InsO (Überschuldung), § 1 StaRUG (Zugangsberechtigung). Prüfraster: Prognosezeitraum 24 Monate, Wahrscheinlichkeitsmassstab ueberwiegend wahrscheinlich, Abgrenzung zu § 17 InsO. Output Prüf-Memo drohende ZU, StaRUG-Zugangsberechtigung-Nachweis. Abgrenzung: Fortbestehensprognose (§ 19 InsO) siehe fortbestehensprognose-zweistufig; Insolvenzantragspflicht siehe insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist.

# Drohende Zahlungsunfähigkeit — § 18 InsO

§ 18 InsO ist das Tor zum StaRUG. Nur wer drohende Zahlungsunfähigkeit nachweist — nicht mehr, nicht weniger — erhält Zugang zu den modernen Sanierungswerkzeugen des Stabilisierungs- und Restrukturierungsrahmens. Wer zu früh kommt (noch keine drohende ZU), kann keinen Antrag stellen. Wer zu spät kommt (eingetretene ZU oder Überschuldung), hat die InsO-Pflicht ausgelöst. Das Timing ist alles — und das Timing hängt von einer validen 24-Monats-Liquiditätsplanung ab.

---

## Rechtsgrundlagen

- § 18 InsO (drohende Zahlungsunfähigkeit; Prognosezeitraum 24 Monate)
- § 17 InsO (Zahlungsunfähigkeit)
- § 19 InsO (Überschuldung; Prognosezeitraum 12 Monate seit 01.01.2024)
- § 29 Abs. 2 StaRUG (drohende ZU als Zugangsvoraussetzung)
- § 15a InsO (Insolvenzantragspflicht bei eingetretener ZU oder Überschuldung)
- **BVerfG 1 BvR 418/25 vom 28.02.2025** (VARTA) — bestätigt mittelbar die Tragfähigkeit der StaRUG-Eintrittsschwelle nach § 18 InsO bei börsennotierten Schuldnerinnen. <https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2025/02/rk20250228_1bvr041825.html>
- IDW S 11 Tz. 23 ff. (Liquiditätsstatus und -planung)
- IDW S 11 Tz. 50 ff. (drohende Zahlungsunfähigkeit)

---

## Pflichten

### 1. Tatbestand der drohenden Zahlungsunfähigkeit

§ 18 Abs. 2 InsO: "Der Schuldner droht zahlungsunfähig zu werden, wenn er voraussichtlich nicht in der Lage sein wird, die bestehenden Zahlungspflichten im Zeitpunkt der Fälligkeit zu erfüllen."

**Drei Kernelemente:**

1. **Prognosezeitraum 24 Monate** (§ 18 Abs. 2 S. 2 InsO seit SanInsFoG 01.01.2021). Konkrete BGH-Linie zur Methodik der Liquiditätsprognose vor Ausgabe über dejure.org / openjur.de verifizieren.

2. **Wahrscheinlichkeitsmaßstab:** "überwiegend wahrscheinlich" — mehr als 50 % Wahrscheinlichkeit, dass die Zahlungsfähigkeit nicht aufrechterhalten werden kann. Kein Gewissheitsmaßstab erforderlich.

3. **Fälligkeitsbezug:** Es kommt auf die fälligen Zahlungen an, nicht auf alle bestehenden Verbindlichkeiten. Langfristige Schulden, die in den 24 Monaten nicht fällig werden, bleiben außen vor.

### 2. Abgrenzung zu § 17 InsO — Eingetretene Zahlungsunfähigkeit

| Merkmal | § 17 InsO | § 18 InsO |
|---|---|---|
| Zeitpunkt | Gegenwart | Zukunft (24 Monate) |
| Wahrscheinlichkeit | Eingetreten (Ist-Zustand) | Überwiegend wahrscheinlich |
| Wesentlichkeitsschwelle | Fälligkeitsrückstand ≥ 10 % der Gesamtverbindlichkeiten (BGH) | Keine feste Schwelle |
| InsO-Antragspflicht | Ja (§ 15a InsO) | Nein (nur Antragsrecht) |
| StaRUG-Zugang | Kein Zugang mehr | Zugang möglich |

**Kritische Praxisfrage:** Ist die Liquiditätslücke noch "vorübergehend" (dann keine ZU) oder nachhaltig (dann § 17 InsO)?
BGH-Maßstab: Rückstand < 10 % der Gesamtverbindlichkeiten = Vermutung für Vorübergehend; > 10 % = Vermutung für ZU.

### 3. Abgrenzung zu § 19 InsO — Überschuldung

| Merkmal | § 19 InsO | § 18 InsO |
|---|---|---|
| Prüfungsmaßstab | Bilanzielle Überschuldung + Fortführungsprognose | Liquiditätsorientiert |
| Fortführungsprognose | Zweistufig (IDW S 11) | Direkt liquiditätsbezogen |
| InsO-Antragspflicht | Ja (§ 15a InsO) | Nein |
| Hauptrelevanz | Verlustunternehmen, negatives EK | Liquiditätsgefährdete Unternehmen |

Ein Unternehmen kann bilanziell überschuldet und gleichzeitig noch zahlungsfähig sein (positiver Cashflow aus lfd. Geschäft). In diesem Fall droht § 19 InsO, aber noch keine § 18 InsO drohende ZU.

### 4. § 18 InsO als Zugangstor zum StaRUG

§ 29 Abs. 2 StaRUG setzt für die Inanspruchnahme des Restrukturierungsrahmens voraus:

- Drohende Zahlungsunfähigkeit nach § 18 InsO **muss vorliegen**
- Eingetretene Zahlungsunfähigkeit oder Überschuldung: Zugang zum StaRUG **ist versperrt**
- Ausnahme: § 29 Abs. 4 StaRUG — gerichtliche Bestätigung des Plans ist auch bei eingetretener ZU möglich, wenn die anderen Voraussetzungen erfüllt sind

**Konsequenz für die Praxis:** Wer früh genug erkennt, hat das volle StaRUG-Arsenal. Wer zu lange wartet, muss mit InsO-Instrumenten arbeiten — mit allen Nachteilen für Reputation, Gläubigerbeziehungen und Betrieb.

---

## Vorgehen

### Schritt 1: Liquiditätsstatus erstellen (IDW S 11 Tz. 23)

```
LIQUIDITÄTSSTATUS — STICHTAG [TT.MM.JJJJ]

VORHANDENE LIQUIDITÄT
 Kassenbestand: EUR [___]
 Bankguthaben: EUR [___]
 Verfügbare Kreditlinien: EUR [___]
 = Verfügbare Liquidität: EUR [___]

ABZUDECKENDE ZAHLUNGSPFLICHTEN
 Fällige Verbindlichkeiten Stichtag: EUR [___]
 Davon: Lieferanten: EUR [___]
 Davon: Steuern/SV: EUR [___]
 Davon: Banken (Zinsen/Tilgung): EUR [___]

SALDO: EUR [___]
 → Positiv: Zahlungsfähig (Stichtag)
 → Negativ: Zahlungsunfähig (Stichtag) → § 17 InsO prüfen
```

### Schritt 2: Liquiditätsprognose 24 Monate (§ 18 InsO-Test)

Auf Basis der rollierenden Liquiditätsplanung (24 Monate):

1. **Identifizierung kritischer Liquiditätsengpässe** — in welchem Monat droht erstmals Unterdeckung?
2. **Wahrscheinlichkeitsbewertung** — ist die Unterdeckung überwiegend wahrscheinlich (> 50 %)?
3. **Sensitivitätsanalyse** — unter welchen Szenarien (Base/Bear) tritt die Unterdeckung auf?
4. **Gegenmaßnahmen-Check** — welche Maßnahmen würden die Unterdeckung beseitigen?

### Schritt 3: StaRUG-Zugang prüfen

Wenn § 18 InsO bejaht:

- [ ] Ist noch kein Insolvenzantrag gestellt?
- [ ] Liegt noch keine eingetretene ZU (§ 17 InsO) vor?
- [ ] Liegt noch keine Überschuldung (§ 19 InsO) vor (oder: liegt positive FBP vor)?
- [ ] Hat das Unternehmen Gläubiger, mit denen eine Einigung sinnvoll ist?

Wenn alle Punkte bejaht: StaRUG-Verfahren eröffnen. Berater einschalten.

---

## Templates

### Muster: § 18 InsO-Prüfvermerk für GF-Akte

```
PRÜFVERMERK — DROHENDE ZAHLUNGSUNFÄHIGKEIT § 18 InsO

Gesellschaft: [Firma GmbH]
Datum der Prüfung: [TT.MM.JJJJ]
Erstellt von: [Name, Funktion]

1. LIQUIDITÄTSSTATUS STICHTAG
 Ergebnis: [zahlungsfähig / eingeschränkt zahlungsfähig / zahlungsunfähig]
 Saldo: EUR [+/-]

2. PROGNOSE 24 MONATE
 Planungsgrundlage: Liquiditätsplan vom [Datum], freigegeben von [GF-Name]
 Prognosezeitraum: [Datum] bis [Datum]
 Kritischer Engpass identifiziert: [ja / nein]
 Wenn ja: Zeitpunkt [Monat/JJJJ], Höhe EUR [___]

3. WAHRSCHEINLICHKEITSBEWERTUNG
 Wahrscheinlichkeit der Unterdeckung: [< 50 % / > 50 %]
 → Drohende ZU nach § 18 InsO: [ja / nein]
 Begründung: [___]

4. FOLGERUNG
 [ ] Keine drohende ZU — kein StaRUG-Handlungsbedarf
 [ ] Drohende ZU — StaRUG-Zugang prüfen
 [ ] Eingetretene ZU — § 15a InsO-Frist läuft

Unterschrift GF: ___________________
Hinweis: Dieser Prüfvermerk ersetzt keine rechtliche Beratung.
```

---

## Fallstricke

1. **Planungshorizont zu kurz** — wer nur zwölf statt 24 Monate plant, riskiert, die drohende ZU zu spät zu erkennen und den StaRUG-Zugang zu verlieren.

2. **Wahrscheinlichkeitsmaßstab falsch angewendet** — "überwiegend wahrscheinlich" bedeutet nicht Sicherheit. Wer erst bei Sicherheit handelt, ist regelmäßig zu spät.

3. **Verwechslung drohende ZU mit eingetretener ZU** — bei eingetretener ZU ist der StaRUG-Zugang gesperrt; die drei Wochen nach § 15a InsO laufen. Diese Grenze muss präzise bestimmt werden.

4. **Kreditlinien als sichere Liquidität eingerechnet** — eine Kreditlinie, die jederzeit kündbar oder bereits gezogen ist, ist keine belastbare Liquiditätsreserve für die Prognose.

5. **Keine externe Validierung** — in strittigen Fällen (z.B. Grenzbereich drohende/eingetretene ZU) ist ein IDW S 11-Gutachten unumgänglich. Eigeneinschätzung der GF allein genügt nicht.

---

## Querverweise

- → `fortbestehensprognose-zweistufig` — Verbindung zwischen § 18 und § 19 InsO
- → `rollierende-liquiditaetsplanung-24-monate-template` — Planungsgrundlage
- → `kennzahlenset-und-ampelsystem-starug-konform` — Liquiditätsreichweite als Schlüssel-KPI
- → `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — Triggerlogik § 15a InsO
- → `restrukturierungsplan-architektur-paragraph-7ff-starug` — StaRUG nach § 18 InsO


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

## 2. `fortbestehensprognose-zweistufig`

**Fokus:** Zweistufige Fortbestehensprognose nach IDW S 11 erstellen: Unternehmen ist möglicherweise ueberschuldet und braucht positive Fortführungsprognose. Normen: § 19 InsO (Überschuldungsbegriff modifiziert), IDW S 11 (Fortbestehensprognose-Standard). Prüfraster: Stufe 1 Fortführungswille, Stufe 2 Fortführungsfähigkeit (GuV/Liquiditaet 12 vs. 24 Monate), Dokumentationspflicht, Sanierungsgutachten. Output Zweistufige Fortbestehensprognose, IDW-S-11-konformes Gutachten-Geruest. Abgrenzung: Drohende ZU siehe drohende-zahlungsunfähigkeit-paragraph-18-inso; integrierte Planung siehe integrierte-planung-guv-bilanz-cashflow.

# Fortbestehensprognose — Zweistufiges Modell nach IDW S 11

Die Fortbestehensprognose ist der Schlüssel zwischen bilanzieller Überschuldung und Insolvenzantragspflicht. § 19 Abs. 2 InsO lässt bei positiver Fortführungsprognose Fortführungswerte in der Überschuldungsbilanz zu — was den Unterschied zwischen "noch sanierbar" und "Antragspflicht ausgelöst" machen kann. IDW S 11 formalisiert diesen Prüfungsprozess zweistufig. Wer die Fortbestehensprognose nicht aktuell und dokumentiert hält, riskiert die persönliche Haftung — auch wenn das Unternehmen de facto noch fortgeführt werden könnte.

---

## Rechtsgrundlagen

- § 19 InsO (Überschuldung als Insolvenzgrund); Prognosezeitraum **12 Monate** seit 01.01.2024 (SanInsKG-Verkürzung auf 4 Monate endete 31.12.2023).
- § 19 Abs. 2 InsO (modifizierter Überschuldungsbegriff: Fortführungswerte bei positiver FBP)
- § 252 Abs. 1 Nr. 2 HGB (Going-Concern-Prinzip in der Rechnungslegung)
- § 15a InsO (Insolvenzantragspflicht)
- IDW S 11 Tz. 65 ff. (Fortführungsprognose — Zweistufenmodell)
- IDW S 6 (Sanierungskonzept als Basis der positiven FBP)
- Konkrete BGH-Linie zur Fortbestehensprognose (insb. Anforderungen an Plausibilität, Sensitivitätsanalysen, qualifizierter Rangrücktritt § 19 Abs. 2 S. 2 InsO) vor Ausgabe über dejure.org / openjur.de verifizieren.

---

## Pflichten

### 1. Der modifizierte Überschuldungsbegriff — § 19 Abs. 2 InsO

Deutschland hat nach der Finanzmarktkrise 2008 dauerhaft den modifizierten Überschuldungsbegriff eingeführt:

```
ÜBERSCHULDUNG § 19 InsO:
 Schritt 1: Liegt eine rechnerische Überschuldung vor?
 (Passiva > Aktiva auf Liquidationsbasis)
 → Wenn NEIN: Kein Insolvenzgrund gem. § 19 InsO
 → Wenn JA: Weiter mit Schritt 2

 Schritt 2: Liegt eine positive Fortführungsprognose vor?
 → Wenn JA: Fortführungswerte zulässig; kein Insolvenzantrag
 (modifizierter Überschuldungsbegriff greift)
 → Wenn NEIN: Insolvenzantragspflicht § 15a InsO ausgelöst
```

### 2. IDW S 11 — Das Zweistufenmodell der Fortbestehensprognose

**Stufe 1: Zahlungsfähigkeitsprognose (primär)**

Die erste Stufe fragt: Kann das Unternehmen in den nächsten 12-24 Monaten seinen Zahlungspflichten nachkommen?

- Grundlage: Rollierende Liquiditätsplanung (mind. 24 Monate, wöchentliche Granularität für Kurzfrist)
- Maßstab: Überwiegend wahrscheinliche Zahlungsfähigkeit über den Prognosezeitraum
- Ergebnis: Wenn JA → Basis für positive FBP gelegt

**Stufe 2: Ertragsfähigkeitsprognose (sekundär, verstärkend)**

Die zweite Stufe fragt: Ist das Unternehmen nachhaltig ertragsfähig?

- Grundlage: Integrierte Unternehmensplanung (GuV, Bilanz, Cashflow)
- Maßstab: Nachhaltiges positives Ergebnis (kein dauerhafter Verlustvortrag)
- Ergebnis: Stützt und bestätigt die Zahlungsfähigkeitsprognose

**Kombination:** Erst wenn beide Stufen positiv sind, liegt eine belastbare positive Fortbestehensprognose vor, die den modifizierten Überschuldungsbegriff trägt.

### 3. Prognosezeitraum: 12 vs. 24 Monate

**12-Monate-Horizont** (Minimalstandard nach IDW S 11 n.F. 2021):
- Für die Zahlungsfähigkeitsprognose ist der Planungshorizont auf mindestens zwölf Monate ausgedehnt worden
- Begründet durch erhöhte Planungsunsicherheit bei längeren Zeiträumen

**24-Monate-Horizont** (Best Practice und § 18 InsO-Standard):
- Für § 18 InsO-konforme drohende ZU-Beurteilung sind 24 Monate erforderlich
- Kombination: Wer 24 Monate plant, ist sowohl für § 18 InsO als auch für § 19 InsO gerüstet

**Praxisempfehlung:** Immer 24 Monate planen. Der Mehraufwand ist gering, die Rechtssicherheit erheblich.

### 4. Wann braucht man ein IDW S 11-Gutachten?

Ein formales Gutachten durch einen Wirtschaftsprüfer nach IDW S 11 ist in folgenden Situationen unumgänglich:

- Im Grenzbereich drohende ZU / eingetretene ZU
- Wenn Banken oder Gläubiger eine externe Bestätigung verlangen
- Wenn die GF die Fortbestehensprognose als Enthaftungsargument einsetzen will
- Bei Aufstellung des Jahresabschlusses mit Going-Concern-Prämisse (§ 252 HGB)
- Bei Unsicherheit über Überschuldungsstatus (§ 19 InsO)

---

## Vorgehen

### Schritt 1: Rechnerische Überschuldungsprüfung

```
ÜBERSCHULDUNGSBILANZ (LIQUIDATIONSWERTE)

AKTIVA — zu Liquidationswerten
 Immaterielle VG (Marktwert): EUR [___]
 Sachanlagevermögen (Verwertungswert): EUR [___]
 Vorräte (Verwertungswert, ggf. Abschlag): EUR [___]
 Forderungen (abzgl. Ausfallwahrscheinlichkeit): EUR [___]
 Bankguthaben: EUR [___]
 Sonstige Aktiva: EUR [___]
= AKTIVA GESAMT: EUR [___]

PASSIVA — zu Nennwerten
 Bankverbindlichkeiten: EUR [___]
 Verbindlichkeiten L&L: EUR [___]
 Steuerverbindlichkeiten: EUR [___]
 Rückstellungen: EUR [___]
 Sonstige Verbindlichkeiten: EUR [___]
= PASSIVA GESAMT: EUR [___]

SALDO: EUR [___]
 → Positiv: Keine rechnerische Überschuldung
 → Negativ: Rechnerische Überschuldung — weiter mit FBP
```

### Schritt 2: Fortbestehensprognose erstellen

1. **Liquiditätsplanung validieren** (24 Monate, IDW S 11 Tz. 23 ff.)
2. **Ertragsplanung validieren** (GuV-Plan, Ertragsfähigkeit prüfen)
3. **Planprämissen dokumentieren** (nachvollziehbar, plausibel, extern prüfbar)
4. **Szenarioanalyse** (Base + Bear) — auch im Bear Case noch positiv?
5. **Ergebnis festhalten** — positive oder negative FBP

### Schritt 3: Dokumentation und Fortschreibung

- FBP wird mindestens quartalsweise aktualisiert
- Jede Verschlechterung der Planprämissen führt zur Ad-hoc-Überprüfung
- Alle Versionen der FBP werden archiviert (Zeitpunktnachweis für Haftung)

---

## Templates

### Muster: Fortbestehensprognose-Zusammenfassung

```
FORTBESTEHENSPROGNOSE — ZUSAMMENFASSUNG
Gesellschaft: [Firma GmbH]
Berichtsdatum: [TT.MM.JJJJ]
Erstellt: [Name, Funktion]
Grundlage: [eigene Analyse / IDW S 11-Gutachten von [WP-Kanzlei fiktiv]]

1. RECHNERISCHE ÜBERSCHULDUNG
 Aktiva (Liquidationswerte): EUR [___]
 Passiva (Nennwerte): EUR [___]
 Saldo: EUR [___]
 Ergebnis: [rechnerisch überschuldet JA/NEIN]

2. FORTBESTEHENSPROGNOSE — STUFE 1 (ZAHLUNGSFÄHIGKEIT)
 Planungshorizont: [x] Monate
 Kritischer Engpass im Planungszeitraum: [ja / nein]
 Wenn ja: [Beschreibung, Gegenmaßnahmen]
 Ergebnis Stufe 1: [positiv / negativ]

3. FORTBESTEHENSPROGNOSE — STUFE 2 (ERTRAGSFÄHIGKEIT)
 EBITDA-Planung Base Case: EUR [___] p.a.
 Ergebnis dauerhaft positiv erwartet: [ja / nein]
 Ergebnis Stufe 2: [positiv / negativ]

4. GESAMTERGEBNIS
 Positive Fortbestehensprognose: [JA / NEIN]
 Folgerung:
 [ ] Fortführungswerte zulässig, keine Antragspflicht
 [ ] Negative FBP — § 15a InsO-Prüfung sofort einleiten

Unterschrift GF: ___________________
Hinweis: Dieser Vermerk ersetzt kein Sachverständigengutachten.
```

---

## Fallstricke

1. **Zu optimistische Planprämissen** für die FBP — Insolvenzverwalter prüfen ex post, ob die Annahmen im Erstellungszeitpunkt plausibel waren. Zu optimistische Annahmen = Haftung.

2. **Fehlende Datierung** der FBP — ohne Datum ist der Zeitpunkt des Vorliegens nicht beweisbar. Immer datieren und unterschreiben.

3. **FBP nur einmal erstellt** — sie ist dynamisch. Wenn sich die wirtschaftliche Lage verschlechtert, muss die FBP ad hoc aktualisiert werden.

4. **Verwechslung Liquidationswerte mit Fortführungswerten** — die Überschuldungsprüfung (Schritt 1) erfordert Liquidationswerte. Erst wenn die FBP positiv ist, dürfen Fortführungswerte angesetzt werden. Reihenfolge einhalten.

5. **Keine externe Validierung in Grenzfällen** — wenn der Saldo der Überschuldungsbilanz nur knapp negativ ist und die FBP fraglich erscheint, ist ein IDW S 11-Gutachten unverzichtbar.

---

## Querverweise

- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Abgrenzung § 18/§ 19 InsO
- → `integrierte-planung-guv-bilanz-cashflow` — Planungsgrundlage für FBP
- → `rollierende-liquiditaetsplanung-24-monate-template` — Liquiditätsplanung als FBP-Basis
- → `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — Folge negativer FBP
- → `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — Haftungsfolgen


## Weitere Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 285/14 vom 26.01.2017** — Hinweis- und Warnpflicht des Steuerberaters; bei verfehlter FBP kann Berater auf Insolvenzvertiefungsschaden haften. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
- **BGH IX ZR 56/22 vom 29.06.2023** — Drittschutzwirkung der Warnpflicht zugunsten des (faktischen) Geschäftsführers. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- **BGH II ZR 206/22 vom 23.07.2024** — Fortwirkende Haftung des ausgeschiedenen Geschäftsführers (Folgen bei negativer FBP nach Amtsniederlegung). <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- Konkrete BGH-Linie zur Plausibilität von Liquiditätsplänen und Sensitivitäten in der FBP vor Ausgabe über offene Quellen verifizieren.


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

## 3. `fruehwarnsystem-architektur-zwei-jahres-horizont`

**Fokus:** StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont architektieren: Unternehmen will § 1 StaRUG Krisenfrueherkennung implementieren. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW S 6 (Sanierungsstandard), IDW PS 340 n.F. (Risikomanagement-Prüfung). Prüfraster: Risiko-Inventar, KPI-Kaskade, Eskalationsstufen, Reporting-Frequenzen, Schwellenwerte, Organisationseinbettung. Output Fruehwarnsystem-Konzept, Implementierungsplan, Governance-Struktur. Abgrenzung: KPI-Set Ampelsystem siehe kennzahlenset-und-ampelsystem-starug-konform; Liquiditaetsplanung siehe rollierende-liquiditaetsplanung-24-monate-template.

# Frühwarnsystem-Architektur mit Zwei-Jahres-Horizont

Ein Frühwarnsystem nach § 1 StaRUG ist kein Excel-Sheet in einer Schublade — es ist eine lebende Governance-Struktur. IDW PS 340 n.F. und IDW S 6 geben die fachlichen Standards vor. Wer diesen Rahmen nicht in die operative Unternehmenssteuerung integriert, erfüllt die gesetzliche Pflicht nur auf dem Papier — und steht im Haftungsfall ohne belastbaren Nachweis da.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht)
- § 91 Abs. 2 AktG (Risikoüberwachungssystem für AG)
- IDW PS 340 n.F. (Anforderungen an Risikofrüherkennungssysteme, Stand 2020)
- IDW S 6 (Anforderungen an Sanierungskonzepte, Stand 2018)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen, Stand 2021)
- § 18 InsO (drohende Zahlungsunfähigkeit)

---

## Pflichten

### 1. Rechtliche Anforderungen an das Frühwarnsystem

Ein § 1 StaRUG-konformes Frühwarnsystem muss folgende Mindestanforderungen erfüllen:

**Formale Anforderungen:**
- Schriftlich dokumentiert und von der Geschäftsführung förmlich beschlossen
- Klar definierte Verantwortlichkeiten (wer meldet was an wen bis wann)
- Regelmäßige Überprüfung und Aktualisierung (mindestens jährlich)
- Nachweis der tatsächlichen Anwendung (Protokolle, Berichte)

**Inhaltliche Anforderungen (IDW PS 340 n.F.):**
- Risikoidentifikation, Risikobewertung und Risikoüberwachung
- Festlegung von Risikotoleranzgrenzen und Eskalationsschwellen
- Integration in die Unternehmensplanung (kein separates Silo)
- Bestandsgefährdungsrisiken besonders hervorheben

### 2. IDW PS 340 n.F. — Kernelemente

IDW PS 340 n.F. (Neufassung 2020) verlangt:

| Element | Inhalt |
|---|---|
| Risikoidentifikation | Vollständige Erfassung aller wesentlichen Risiken (intern + extern) |
| Risikobewertung | Eintrittswahrscheinlichkeit und Schadenshöhe quantifizieren |
| Risikoaggregation | Gesamtrisikoprofil — Wechselwirkungen berücksichtigen |
| Risikoüberwachung | KPIs, Meilensteine, Plan-Ist-Abweichungen |
| Berichterstattung | Regelkreis von GF zum Aufsichtsorgan |

---

## Vorgehen

### Schritt 1: Risiko-Inventar aufbauen

Das Risiko-Inventar ist die Basis des Frühwarnsystems. Typische Risikofelder:

**Finanzrisiken:**
- Liquiditätsrisiko (Zahlungsunfähigkeit, Refinanzierungsrisiko)
- Zinsänderungsrisiko (variabel verzinste Verbindlichkeiten)
- Währungsrisiko (Fremdwährungsgeschäfte)
- Forderungsausfallrisiko

**Operative Risiken:**
- Lieferkettenstörungen
- Kapazitätsengpässe
- IT-/Systemausfälle
- Personalabgänge in Schlüsselpositionen

**Marktrisiken:**
- Nachfragerückgang, Preisdruck
- Wettbewerberaktivitäten
- Regulatorische Änderungen

**Strategische Risiken:**
- Technologiedisruption
- Kundenkonzentration > 20 % des Umsatzes bei einem Kunden

### Schritt 2: KPI-Kaskade definieren

Die KPI-Kaskade verbindet strategische Ziele mit operativen Frühwarnindikatoren:

**Ebene 1 — Überlebensfähigkeit (täglich/wöchentlich):**
- Kassenbestand und Kreditlinien-Auslastung
- Fällige Zahlungen nächste 14 Tage vs. verfügbare Liquidität

**Ebene 2 — Liquiditätsstabilität (wöchentlich/monatlich):**
- 13-Wochen-Cashflow-Abweichung zum Plan
- Debitoren-Umschlagsdauer (DSO)
- Kreditoren-Umschlagsdauer (DPO)
- Working-Capital-Quote

**Ebene 3 — Ertragsstabilität (monatlich):**
- EBITDA-Marge vs. Vorjahr und Plan
- Deckungsbeitrag je Produkt/Segment
- Auftragseingang und Auftragsbestand

**Ebene 4 — Strukturelle Solidität (quartalsweise):**
- Net-Debt/EBITDA
- Eigenkapitalquote
- Covenant-Headroom (Puffer zu Finanzkennzahl-Anforderungen der Bank)
- DSCR (Debt Service Coverage Ratio)

### Schritt 3: Eskalationsstufen definieren

```
ESKALATIONSSYSTEM — DREISTUFIG

Stufe 1 — GRÜN (Normalbetrieb):
 Alle KPIs innerhalb Plankorridor
 Aktion: Routinereporting (monatlich an GF)

Stufe 2 — GELB (Frühwarnung):
 Mind. ein KPI außerhalb Plankorridor aber über Mindestschwelle
 Aktion: Sofortanalyse innerhalb 5 Werktagen
 Maßnahmenplan innerhalb 10 Werktagen
 Information AR/Gesellschafter innerhalb 15 Werktagen

Stufe 3 — ROT (Krisenalarm):
 Mindestschwelle unterschritten ODER Liquiditätsreichweite < 3 Monate
 Aktion: Sofortmaßnahmen (72 Stunden)
 Berater einschalten (RA, StB, Restrukturierungsberater)
 Information AR/Gesellschafter unverzüglich
 § 102 StaRUG Warnung empfangen/versenden
 StaRUG-Zugang prüfen
```

### Schritt 4: Reporting-Struktur festlegen

| Ebene | Frequenz | Inhalt | Empfänger |
|---|---|---|---|
| Tagesreport | Täglich | Kassenbestand, offene Zahlungen | CFO / Treasurer |
| Wochenreport | Wöchentlich | 13-Wochen-Cashflow, Abweichungen | Gesamte GF |
| Monatsbericht | Monatlich | Alle KPIs, Plan-Ist, Prognose | GF + Gesellschafter |
| Quartalsbericht | Quartalsweise | Strukturelle KPIs, Covenant-Check | GF + AR + Bank |
| Jahresbericht | Jährlich | Risiko-Inventar-Update, Systembewertung | GF + AR |

### Schritt 5: Systemdokumentation und -pflege

1. **Systemhandbuch** erstellen (Verantwortlichkeiten, Prozessablauf, Schwellenwerte)
2. **Jährliche Überprüfung** der Relevanz und Vollständigkeit des Risiko-Inventars
3. **Schulung** der beteiligten Mitarbeiter und GF
4. **Audit-Trail** — alle Reports und Eskalationen protokollieren

---

## Templates

### Muster: Risiko-Inventar (Tabellenstruktur)

```
Risiko-Inventar — [Firma GmbH] — Stand: [Datum]

Nr. | Risikokategorie | Risikobeschreibung | Eintrittswsk. | Schaden EUR | Risikoscore | Verantwortlich | KPI | Schwelle ROT
----|----------------|-------------------|--------------|------------|------------|---------------|-----|-------------
R01 | Liquidität | Refinanzierungsrisiko: Hausbankkredit läuft [Datum] aus | Mittel | [Betrag] | Hoch | CFO | Kredit-Restlaufzeit | < 6 Monate
R02 | Umsatz | Kundenkonzentration: Kunde X = [x]% Umsatz | Niedrig | [Betrag] | Mittel | CSO | Umsatzanteil Top-1-Kunde | > 25 %
R03 | Personal | Schlüsselpersonenrisiko: Geschäftsführer [Name] | Niedrig | [Betrag] | Mittel | GF | Nachfolgeplanung | Nicht vorhanden
```

### Muster: Frühwarnsystem-Beschluss der Geschäftsführung

```
Beschluss der Geschäftsführung — Frühwarnsystem § 1 StaRUG

Gesellschaft: [Firma GmbH]
Datum: [TT.MM.JJJJ]

Die Geschäftsführung beschließt:

1. Das vorliegende Frühwarnsystem (Systemhandbuch vom [Datum])
 wird als verbindliche Governance-Struktur eingeführt.
2. Verantwortlich für Pflege und Reporting: [Name, Funktion].
3. Die KPI-Schwellenwerte gemäß Anlage 1 gelten ab sofort.
4. Abweichungen von Stufe 2 (Gelb) werden unverzüglich protokolliert.
5. Das System wird jährlich, erstmals zum [Datum], überprüft.

[Unterschriften GF]
```

---

## Fallstricke

1. **Frühwarnsystem auf Papier ist kein Frühwarnsystem** — im Haftungsfall wird geprüft, ob das System tatsächlich gelebt wurde. Fehlende Reports, keine Protokolle, keine Eskalationen: Indizienbeweis für Pflichtverletzung.

2. **Schwellenwerte zu weit gefasst** schützen nicht. Wer "ROT erst ab Zahlungsunfähigkeit" definiert, hat kein Frühwarnsystem, sondern ein Brandmeldesystem nach dem Brand.

3. **Keine Integration in Planungsprozess** — das Frühwarnsystem muss mit der operativen Planung verbunden sein. Eigenständige Silo-Lösung ohne Rückkopplung erfüllt IDW PS 340 n.F. nicht.

4. **Outsourcing an Steuerberater ohne eigene Überwachung** reicht nicht. Der Steuerberater liefert Daten, die GF muss sie auswerten und auf Abweichungen reagieren.

5. **Jährliche statt rollierende Überprüfung** ist zu grob. Das Risiko-Inventar muss nach wesentlichen Veränderungen ad hoc überprüft werden.

---

## Querverweise

- → `paragraph-1-starug-pflichten-und-24-monats-horizont` — rechtliche Pflichtgrundlage
- → `rollierende-liquiditaetsplanung-24-monate-template` — konkrete Planungsstruktur
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Definitionen und Schwellen
- → `integrierte-planung-guv-bilanz-cashflow` — Drei-Statement-Modell
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Systemdokumentation


## Aktuelle Leitentscheidungen — Fruehwarnsystem und § 1 StaRUG

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Fruehwarnsystem

§ 1 StaRUG (Pflicht zur Fruehwarnung) → § 102 StaRUG (Rechtsberater-Warnpflicht) → § 43 GmbHG (Sorgfaltspflicht GF) → § 93 AktG (Vorstandshaftung) → § 91 Abs. 2 AktG (Fruehwarnsystem-Pflicht AG) → § 15a InsO (Antragspflicht bei erkannter ZU/Ueberschuldung)

## Triage — Fruehwarnsystem

1. **Kennzahlen-Set?** Welche Kennzahlen werden in welchem Rhythmus erhoben? (Liquiditaet, EBIT, Forderungslaufzeit, Eigenkapital-Quote)
2. **Ampelsystem vorhanden?** Gruene, gelbe, rote Schwellen definiert?
3. **Eskalationskette?** Wer wird bei roten Ampeln informiert? GF → Aufsichtsrat → Anwalt?
4. **Historische Daten?** 2 Jahre Ruckschau fuer Trend-Erkennung vorhanden?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
