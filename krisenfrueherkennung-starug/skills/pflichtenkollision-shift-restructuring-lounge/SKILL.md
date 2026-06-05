---
name: pflichtenkollision-shift-restructuring-lounge
description: "Pflichtenkollision Shift Restructuring Lounge: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pflichtenkollision Shift Restructuring Lounge

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pflichtenkollision Shift Restructuring Lounge** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pflichtenkollision-und-shift-of-fiduciary-duties` | Prüffeld für pflichtenkollision und shift of fiduciary duties: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `restructuring-lounge-impulsvortrag-toolkit` | Toolkit für Impulsvorträge zu Krisenfrüherkennung und StaRUG: Foliensatz-Gliederung, Talking-Points, juristische Kernbotschaften, Q-und-A-Fallnetz, Formathinweise für Veranstaltungen wie Branchenlounge-Formate. |
| `restrukturierungsbeauftragter-und-sachwalter` | Restrukturierungsbeauftragter und Sachwalter nach § 73 StaRUG: GF oder Gläubigervertreter prüft Bestellung und Aufgaben. Normen: § 73 StaRUG (Restrukturierungsbeauftragter), §§ 74-77 StaRUG (Pflichtbeauftragung), § 76 StaRUG (Sachwalter). Prüfraster: Bestellung (freiwillig vs. Pflicht), Aufgaben, Auswahlkriterien, Honorar-Festsetzung, Unterschied zum Insolvenzverwalter, gerichtliche Kontrolle. Output Bestellungs-Memo, Auswahlkriterien-Checkliste. Abgrenzung: Insolvenzverwalter InsO siehe insolvenzverwaltung-Plugin; Planarchitektur siehe restrukturierungsplan-architektur-paragraph-7ff-starug. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **Pflichtenkollision Shift Restructuring Lounge**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pflichtenkollision-und-shift-of-fiduciary-duties`

**Fokus:** Prüffeld für pflichtenkollision und shift of fiduciary duties: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Pflichtenkollision und Shift of Fiduciary Duties in der Krise

Im Normalzustand schuldet der Geschäftsführer seine Loyalität den Gesellschaftern — er ist ihr Agent, ihr verlängerter Arm. In der Krise dreht sich das Koordinatensystem. Je tiefer das Unternehmen in die Insolvenzgefährdung gleitet, desto stärker verschiebt sich die Pflichtbindung vom Eigentümerinteresse zum Gläubigerinteresse. Dieser "Shift of Fiduciary Duties" ist keine anglistische Theorie, sondern gelebtes deutsches Recht — mit direkten Haftungsfolgen.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht)
- § 15a InsO (Insolvenzantragspflicht)
- § 15b InsO (Zahlungsverbote nach Insolvenzreife)
- § 43 GmbHG (Sorgfaltspflicht GF)
- § 93 AktG (Sorgfaltspflicht Vorstand)
- § 19 Abs. 2 InsO (Fortführungsprognose bei Überschuldung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EuInsVO Art. 3 Abs. 1 (COMI — Centre of Main Interests)

---

## Pflichten

### 1. Das normale Pflichtenbild — Eigentümerinteresse

Im Normalzustand ist der Geschäftsführer dem Gesellschafterinteresse verpflichtet:

- Gewinnmaximierung, Wachstum, Erhaltung des Unternehmenswertes
- Weisungsrecht der Gesellschafterversammlung (GmbH) beachten
- Unternehmerische Entscheidungen nach Business Judgment Rule treffen

Gläubiger sind in dieser Phase nur mittelbar geschützt — durch das Kapitalerhaltungsgebot (§§ 30, 31 GmbHG) und die allgemeinen Insolvenztatbestände.

### 2. Der Shift — Wann dreht sich das Koordinatensystem?

Der Pflichtenwandel vollzieht sich graduell, nicht schlagartig:

| Phase | Pflichtenschwerpunkt | Gläubigerschutz |
|---|---|---|
| Normalbetrieb | Eigentümerinteresse | Mittelbar |
| Strategiekrise | Eigentümer + Überwachung | Mittelbar, § 1 StaRUG |
| Ertragskrise | Eigentümer + Gläubiger gleichwertig | Aktiv: § 1 StaRUG |
| Liquiditätskrise | Gläubigerinteresse dominant | Direkter Schutz |
| Insolvenzreife | Ausschließlich Gläubigerinteresse | § 15a, § 15b InsO |

Der "tipping point" liegt regelmäßig beim Eintritt der drohenden Zahlungsunfähigkeit nach § 18 InsO: Ab diesem Moment sind Maßnahmen, die ausschließlich dem Gesellschafterinteresse dienen (Gewinnausschüttung, riskante Investitionen), haftungsrechtlich gefährlich.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

1. Das Recht des Niederlassungsstaates regelt die Haftung des Geschäftsführers nach Insolvenzreife.
2. Eine Flucht in ausländische Gesellschaftsformen (Limited, S.à r.l.) schützt nicht vor dem deutschen Haftungsregime, wenn das operative Zentrum in Deutschland liegt.
3. Der COMI (Centre of Main Interests) bestimmt das anwendbare Insolvenzrecht — und damit die Haftungsgrundlage.

### 4. COMI-Verlagerung — Verbote und Grenzen

Eine Verlagerung des COMI (z.B. von Deutschland nach Österreich oder Niederlande) zur Erschleichung eines anderen Insolvenzrechts ist nicht schlechthin verboten, aber an enge Voraussetzungen geknüpft:

- Die Verlagerung muss **tatsächlich** und **nachhaltig** sein (nicht nur formale Sitzverlegung)
- **§ 3 Abs. 1 EuInsVO** verlangt, dass der COMI für Dritte erkennbar und nachprüfbar am neuen Ort liegt
- **Timing**: Eine COMI-Verlagerung kurz vor Insolvenzantrag wird von Gerichten als Missbrauch gewertet und rückgängig gemacht
- Deutsche Gerichte können bei Rechtsmissbrauch weiterhin zuständig bleiben

**Praxiswarnung:** Mandanten, die eine schnelle COMI-Verlagerung als Ausweg aus dem deutschen Insolvenzregime erwägen, laufen in ein offenes Messer — die Rechtsprechung ist hier eindeutig restriktiv.

### 5. Pflichtenkollision — Gesellschafterweisung vs. Gläubigerschutz

In der Krise entsteht häufig eine direkte Pflichtenkollision:

- **Gesellschafter wollen:** Dividende, Finanzierungsmaßnahmen zugunsten anderer Gruppengesellschaften, Liquidation ohne Insolvenz
- **Gläubigerschutz verlangt:** Erhalt der Masse, keine masseschmälernden Zahlungen, § 15b InsO

**Lösung der Pflichtenkollision:**

1. **Vorrang des Gläubigerinteresses** bei Insolvenzreife — Gesellschafterweisung ist in diesem Fall unbeachtlich (§ 15a InsO ist zwingendes Recht)
2. **Business Judgment Rule** gilt nur noch eingeschränkt
3. **Transparenzpflicht** gegenüber allen Stakeholdern — kein selektives Informationsmanagement
4. **Externe Beratung** als Haftungspuffer: Wer nachweislich auf Basis eines validierten IDW S 11-Gutachtens gehandelt hat, ist besser gestellt

---

## Vorgehen

### Schritt 1: Pflichtenstatus-Check bei Kriseneintritt

Bei Auftreten erster Krisensignale sofort prüfen:

- [ ] In welchem Krisenstadium befindet sich das Unternehmen?
- [ ] Liegt drohende Zahlungsunfähigkeit vor? → Spezialisten hinzuziehen
- [ ] Wem gegenüber bin ich primär verpflichtet? (Shift prüfen)
- [ ] Welche Weisungen der Gesellschafter sind noch befolgbar?
- [ ] Gibt es laufende Intercompany-Zahlungen, die zu prüfen sind?

### Schritt 2: Dokumentation des Pflichtenrahmens

Sobald der Shift eingetreten ist, dokumentieren:

1. Zeitpunkt der Erkenntnis
2. Rechtliche Einschätzung (intern oder extern)
3. Änderung der internen Entscheidungsmatrix
4. Information an Gesellschafter über geänderte Pflichtenlage

### Schritt 3: Intercompany-Zahlungen prüfen

Zahlungen an verbundene Unternehmen in der Krise sind besonders gefährlich:

- Upstream-Garantien an Muttergesellschaft: Haftungsrisiko § 30 GmbHG, § 15b InsO
- Konzernumlagen: Marktüblichkeit prüfen
- Cash-Pooling: Rückforderbarkeit sicherstellen

---

## Templates

### Muster: Pflichtenstatus-Memo für Geschäftsführer-Akte

```
Internes Memo
Datum: [TT.MM.JJJJ]
Von: [Name GF]
Betreff: Pflichtenstatus-Analyse gem. § 1 StaRUG / Shift of Fiduciary Duties

1. AKTUELLES KRISENSTADIUM
 Einschätzung: [Strategiekrise / Ertragskrise / Liquiditätskrise / drohende ZU]
 Grundlage: [eigene Analyse / Beratereinschätzung / Gutachten]

2. PFLICHTENBINDUNG
 Primäre Pflichtenbindung aktuell: [Gesellschafter / Gläubiger / beides]
 Begründung:

3. GESELLSCHAFTERWEISUNGEN
 Laufende Weisungen: [Beschreibung]
 Befolgbarkeit: [ja / eingeschränkt / nein — Begründung]

4. INTERCOMPANY-MASSNAHMEN
 Laufende Intercompany-Zahlungen: [ja / nein]
 Überprüfung der Marktüblichkeit: [ja / nein / in Bearbeitung]

5. NÄCHSTE SCHRITTE
 [Maßnahmenplan]

Erstellt von: ___________________
```

---

## Fallstricke

1. **Der Shift kommt früher als gedacht** — viele GF gehen davon aus, erst bei Zahlungsunfähigkeit dem Gläubigerinteresse verpflichtet zu sein. Die Rechtsprechung zieht die Grenze früher: bereits bei drohender Zahlungsunfähigkeit sind masseschmälernde Maßnahmen haftungsträchtig.

2. **Gruppengesellschaften sind keine sichere Bank** — Zahlungen an verbundene Unternehmen, die nach Maßstab des Drittvergleichs nicht marktüblich sind, können nach Insolvenzanfechtungsrecht (§§ 129 ff. InsO) rückgefordert werden.

3. **COMI-Verlagerung als Haftungsflucht** ist regelmäßig gescheitert — Gerichte sind sensibilisiert und setzen hohe Anforderungen an echte operative Verlagerungen.

4. **Gesellschafterweisung entbindet nicht von § 15a InsO** — selbst wenn alle Gesellschafter Fortführung wollen und beauftragen: Die Insolvenzantragspflicht ist nicht disponibel.

5. **"Management by Delegation" in der Krise** ist kein Enthaftungsinstrument — Gesamtverantwortung aller GF-Mitglieder bleibt bestehen, auch bei formal getrennten Ressorts.

---

## Querverweise

- → `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — GF-Haftung im Überblick
- → `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — § 15a InsO
- → `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` — Krisenstadien-Diagnostik
- → `fortbestehensprognose-zweistufig` — Fortführungsprognose als Pflichtanker
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Beweissicherung


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

## 2. `restructuring-lounge-impulsvortrag-toolkit`

**Fokus:** Toolkit für Impulsvorträge zu Krisenfrüherkennung und StaRUG: Foliensatz-Gliederung, Talking-Points, juristische Kernbotschaften, Q-und-A-Fallnetz, Formathinweise für Veranstaltungen wie Branchenlounge-Formate.

# Impulsvortrag-Toolkit — StaRUG und Krisenfrüherkennung

Impulsvorträge zu § 1 StaRUG und Krisenfrüherkennung sind mehr als akademische Pflichtübung. Sie sind Mandantengewinnung, Reputationsaufbau und gesellschaftliche Aufgabe zugleich — denn die Mehrzahl der Unternehmen, die in die Insolvenz gehen, hätte mit früherem Handeln Alternativen gehabt. Das vorliegende Toolkit ist für Veranstaltungsformate konzipiert, bei denen Berater, Unternehmer und Sanierungsspezialisten in einer offenen Diskussionsatmosphäre zusammenkommen, wie sie etwa bei Branchen-Lounge-Formaten in Hamburg und anderen Standorten gepflegt wird — zum Beispiel im Format der Restructuring Lounge oder vergleichbarer regionaler Netzwerkveranstaltungen.

---

## Rechtsgrundlagen (Vortragsreferenzen)

- § 1 StaRUG (Krisenfrüherkennungspflicht)
- § 102 StaRUG (Warnpflicht der Berater)
- §§ 7 ff. StaRUG (Restrukturierungsplan)
- §§ 49-59 StaRUG (Stabilisierungsanordnung)
- §§ 15a, 15b InsO (Insolvenzantragspflicht und Zahlungsverbot)
- § 43 GmbHG, § 93 AktG (GF-Haftung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 6, IDW S 11, IDW PS 340 n.F.

---

## Pflichten

### 1. Vortragsdisziplin — Was ein guter Impulsvortrag leisten muss

Ein 20-Minuten-Impulsvortrag zu StaRUG und Krisenfrüherkennung muss:

1. **Eine klare Kernbotschaft** transportieren (nicht fünf, eine)
2. **Rechtliche Präzision** mit verständlicher Sprache verbinden — kein Kanzlei-Kauderwelsch
3. **Handlungsrelevanz** für die Anwesenden erzeugen — niemand kommt für abstrakte Paragrafenlesungen
4. **Haftungs-Brille** durchgehend anlegen — der GF im Publikum muss spüren: das betrifft mich persönlich
5. **Konkrete Werkzeuge** zeigen — mindestens ein Template, eine KPI-Tabelle, ein Protokoll

---

## Foliensatz-Gliederung (20 Minuten)

```
FOLIE 1 — TITELFOLIE (0:00 — 0:30)
 "Krisenfrüherkennung ist Pflicht, nicht Kür — § 1 StaRUG"
 [Name des Vortragenden, Datum, Veranstaltungsname]

FOLIE 2 — KERNBOTSCHAFT (0:30 — 1:30)
 "§ 1 StaRUG verlangt den 24-Monats-Horizont.
 Wer die Datenlage nicht im Griff hat, verliert das Heft des Handelns."
 [Visuell: Timeline — 24 Monate, 12 Monate, 3 Monate, Insolvenzantrag]

FOLIE 3 — DAS PROBLEM (1:30 — 3:00)
 "Wie Unternehmen in die Insolvenz gehen — fünf Stadien."
 Visuell: IDW S 6 Stufenpyramide
 Talking Point: "Stakeholderkrise bis Liquiditätskrise — der Weg dauert Jahre,
 aber die letzten Monate laufen im Eilzugtempo."

FOLIE 4 — § 1 StaRUG — WAS DAS GESETZ VERLANGT (3:00 — 5:00)
 Kerninhalt:
 - Haftungsbeschränkte Rechtsträger = Normadressaten
 - Fortlaufende Überwachung + Gegenmaßnahmen + Unterrichtung
 - 24-Monate-Liquiditätsplanung als Standard
 Talking Point: "Das ist kein Wunsch. Das ist Gesetz seit 2021."

FOLIE 5 — DER 24-MONATS-HORIZONT (5:00 — 7:00)
 Visuell: Planungsstruktur
 Woche 1-13: wöchentlich / Monat 14-24: monatlich
 KPI-Ampel (Liquiditätsreichweite, Net-Debt/EBITDA, DSCR)
 Talking Point: "Ohne diese Sicht können Sie bei drohender
 Zahlungsunfähigkeit keinen StaRUG-Antrag stellen."

FOLIE 6 — DIE HAFTUNG (7:00 — 9:30)
 § 43 GmbHG + § 93 Abs. 2 S. 2 AktG
 Business Judgment Rule — in der Krise eingeschränkt
 Beweislastumkehr: GF muss beweisen, dass er richtig gehandelt hat
 Kernbotschaft: "Ohne Protokoll kein Beweis. Ohne Beweis: Haftung."

FOLIE 7 — § 102 StaRUG — DIE BERATER-PFLICHT (9:30 — 11:00)
 Steuerberater, WP, RA: unaufgeforderter Warnhinweis bei Krisensignalen
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Dokumentationspflicht beider Seiten
 Talking Point: "Jede BWA, die der StB ausliest und schweigt — potenzielle Haftung."

FOLIE 8 — StaRUG-WERKZEUGKASTEN (11:00 — 13:00)
 Restrukturierungsplan §§ 7 ff.
 Stabilisierungsanordnung §§ 49-59 (drei Monate Schutz)
 Cross-Class-Cram-Down § 26 (Mehrheit gegen ablehnende Gruppen)
 Talking Point: "Das StaRUG ist das modernste Sanierungsgesetz Europas —
 aber es ist nur für den zugänglich, der rechtzeitig handelt."

FOLIE 9 — DIE ZEITKRITISCHE ENTSCHEIDUNG (13:00 — 15:00)
 Visuell: Entscheidungsbaum
 Drohende ZU (§ 18 InsO) → StaRUG oder freie Sanierung
 Eingetretene ZU (§ 17 InsO) → § 15a InsO, drei Wochen
 Überschuldung (§ 19 InsO) → negative FBP → § 15a InsO
 Talking Point: "Der Zug zum StaRUG fährt ab. Wer den verpasst,
 steht am Insolvenzbahnhof."

FOLIE 10 — PRAXIS-CHECKLISTE (15:00 — 17:00)
 "Was Sie diese Woche in Ihrem Unternehmen prüfen sollten:"
 1. Gibt es eine 24-Monats-Liquiditätsplanung?
 2. Gibt es ein dokumentiertes KPI-Ampelsystem?
 3. Wann wurde der Gesellschafter zuletzt über die wirtschaftliche
 Lage informiert?
 4. Wann hat Ihr StB zuletzt die Krisenthematik angesprochen?
 Talking Point: "Nicht drei von vier — alle vier."

FOLIE 11 — Q&A VORBEREITUNG (17:00 — 20:00)
 "Ihre Fragen — meine Antworten."
 [Moderiertes Gespräch]
```

---

## Talking-Points — Juristische Pointen für den Vortrag

### Point 1 — Die Pflicht ist alt, der Name ist neu
"Das Pflichtenprogramm der Krisenfrüherkennung ist nicht mit dem StaRUG 2021 neu erfunden worden. Es ergibt sich schon aus § 43 GmbHG, § 93 AktG, § 91 AktG. Das StaRUG hat es kodifiziert und mit einem Verfahren verbunden. Der Gesetzgeber hat nicht mehr Pflichten geschaffen — er hat bestehende Pflichten sichtbar gemacht."

### Point 2 — Beweislastumkehr als Schlüsselproblem
"§ 93 Abs. 2 S. 2 AktG, analog für GmbH-Geschäftsführer: Wenn der Insolvenzverwalter klagt, muss nicht er beweisen, dass der GF falsch gehandelt hat — sondern der GF muss beweisen, dass er richtig gehandelt hat. Das ist die Welt auf dem Kopf, verglichen mit normalen Haftungsprozessen. Deshalb: Kein Handeln ohne Protokoll."

### Point 3 — Das StaRUG als Versicherungspolice
"Das StaRUG ist keine Krisensanierungsmaschine für hoffnungslose Fälle. Es ist eine Versicherungspolice für das rechtzeitige Handeln. Wer früh genug einzahlt — mit valider Planung, mit Krisendiagnose, mit Beratereinbindung — der kann im Ernstfall auf moderne Instrumente zugreifen. Wer nicht einzahlt, steht im Regen."

### Point 4 — § 102 StaRUG als Doppelschneid
"§ 102 StaRUG schützt den Berater, der warnt. Und er schadet dem Berater, der schweigt. Es gibt keine sichere Mitte. Wer als Steuerberater monatlich die BWA liest und krisenrelevante Signale ignoriert, sitzt auf einer Zeitbombe."

### Point 5 — Die Kornhaas-Entscheidung als Warnung für Gesellschaftsform-Optimierer
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Q&A-Fallnetz — Häufige Fragen mit Antwortvorschlägen

**Frage: "Wie konkret muss die 24-Monats-Planung sein?"**
Antwort: "Konkret genug, um im Ernstfall vor dem Insolvenzgericht und dem Insolvenzverwalter zu bestehen. Das bedeutet: dokumentierte Planprämissen, wöchentliche Granularität für die ersten dreizehn Wochen, integrierter Cashflow — und vor allem: aktuell. Eine Planung, die sechs Monate alt ist, hilft im Krisenfall nicht."

**Frage: "Wir haben einen Steuerberater — reicht das?"**
Antwort: "Ihr Steuerberater ist nach § 102 StaRUG verpflichtet zu warnen, wenn er Krisensignale sieht. Aber er ist nicht der Krisenmanager. Die Krisenfrüherkennung bleibt Aufgabe der Geschäftsführung. Der Steuerberater liefert Daten — Sie müssen handeln. Delegation schützt nicht vor persönlicher Haftung."

**Frage: "Was kostet ein StaRUG-Verfahren?"**
Antwort: "Das hängt von der Komplexität ab. Für eine typische mittelständische Restrukturierung mit zwei bis vier Gläubigergruppen sind sechsstellige Beraterkosten realistisch. Das klingt viel — aber verglichen mit den Alternativkosten eines Insolvenzverfahrens (Reputation, Betriebsunterbrechung, Anfechtungsrisiken) ist es oft erheblich günstiger."

**Frage: "Können wir das StaRUG-Verfahren geheim halten?"**
Antwort: "Teilweise ja. Das StaRUG ist grundsätzlich nichtöffentlich. Die Restrukturierungssache wird im Restrukturierungsregister eingetragen — das ist öffentlich. Aber kein Insolvenzbekanntmachungsportal, keine Pressemitteilung des Gerichts. Für viele Mittelständler ist das ein erheblicher Vorteil."

**Frage: "Was passiert, wenn ich zu spät war und § 15a InsO gilt?"**
Antwort: "Dann sind Sie in einer der gefährlichsten Situationen des deutschen Rechts. Drei Wochen Frist. Strafbarkeit bei Verspätung. Persönliche Haftung für alle Zahlungen nach Insolvenzreife. Mein dringender Rat: Sofort einen Spezialisten für Insolvenz- und Sanierungsrecht einschalten — und das Datum der Erkenntnis des Insolvenzgrundes sofort protokollieren."

---

## Format-Hinweise für Branchenlounge-Veranstaltungen

Veranstaltungsformate, bei denen Impulsgespräche zu Restrukturierungsthemen im Vordergrund stehen — wie es der Restructuring Lounge-Ansatz oder vergleichbare regionale Vernetzungsveranstaltungen verkörpern —, funktionieren nach anderen Regeln als klassische Fachkonferenzen:

- **Kürze schlägt Vollständigkeit** — 15-20 Minuten Impuls, dann Diskussion. Kein Vorlesungsvortrag.
- **Fallbeispiele** (fiktiv) erzeugen mehr Resonanz als Paragrafenzitate. Konkret werden.
- **Einladung zur Diskussion** — in lockerer Atmosphäre fragen Teilnehmer Dinge, die sie im Seminar nie fragen würden. Dort liegt der echte Erkenntniswert.
- **Take-away sichern** — eine Checkliste, ein Template oder ein QR-Code mit Ressourcen erhöht die Erinnerungsrate erheblich.
- **Keine Kanzleiwerbung auf den Folien** — Kompetenz zeigt sich im Inhalt, nicht im Logo-Pflaster.

---

## Fallstricke bei Impulsvorträgen

1. **Zu viele Rechtsgrundlagen ohne Kontext** — sieben Paragrafen in drei Minuten abfeuern ist kein Vortrag, sondern ein Gesetzesvortrag. Kontext und Konsequenz interessieren, nicht die Norm allein.

2. **Angst vor zu konkreten Aussagen** — zu vorsichtige Formulierungen (alles ein Einzelfall, immer Anwalt fragen) nehmen dem Vortrag die Substanz. Konkret sein, Haftungshinweis am Ende genügt.

3. **Kein echtes Q&A** — der Wert einer Lounge-Veranstaltung entsteht im Austausch. Wer nach dem Vortrag sofort verschwindet, verschenkt den wichtigsten Teil.

4. **Fiktive Beispiele zu nah an realen Fällen** — Fallbeispiele sollten eindeutig fiktiv sein. Namen, Branchen und Zahlen so wählen, dass kein realer Bezug herstellbar ist.

5. **Technische Panne ohne Backup** — für Kurzvorträge reicht eine ausgedruckte Gliederung als Backup. Folienpräsentation ist Hilfsmittel, nicht Inhalt.

---

## Querverweise

- → `paragraph-1-starug-pflichten-und-24-monats-horizont` — Kernnorm des Vortrags
- → `paragraph-102-starug-warnpflicht-bei-rechtsberatern` — Berater-Pflichten für Fachpublikum
- → `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` — IDW S 6 Stadienmodell als Folie 3
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Ampel als Anschauungsbeispiel
- → `mandantenbrief-warnung-paragraph-102-starug-template` — Take-away für Berater im Publikum


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

## 3. `restrukturierungsbeauftragter-und-sachwalter`

**Fokus:** Restrukturierungsbeauftragter und Sachwalter nach § 73 StaRUG: GF oder Gläubigervertreter prüft Bestellung und Aufgaben. Normen: § 73 StaRUG (Restrukturierungsbeauftragter), §§ 74-77 StaRUG (Pflichtbeauftragung), § 76 StaRUG (Sachwalter). Prüfraster: Bestellung (freiwillig vs. Pflicht), Aufgaben, Auswahlkriterien, Honorar-Festsetzung, Unterschied zum Insolvenzverwalter, gerichtliche Kontrolle. Output Bestellungs-Memo, Auswahlkriterien-Checkliste. Abgrenzung: Insolvenzverwalter InsO siehe insolvenzverwaltung-Plugin; Planarchitektur siehe restrukturierungsplan-architektur-paragraph-7ff-starug.

# Restrukturierungsbeauftragter und Sachwalter — § 73 StaRUG

Der Restrukturierungsbeauftragte ist das externe Kontrollorgan des StaRUG-Verfahrens — kein Insolvenzverwalter, kein feindlicher Übernehmer, sondern ein gerichtlich bestellter Vermittler und Wächter der Verfahrensintegrität. Seine Bestellung ist in manchen Konstellationen obligatorisch, in anderen fakultativ. Wer ihn richtig einsetzt, gewinnt Glaubwürdigkeit bei Gläubigern und Gerichten. Wer ihn falsch einschätzt, verliert die Kontrolle über den Prozess.

---

## Rechtsgrundlagen

- §§ 73-83 StaRUG (Restrukturierungsbeauftragter)
- § 73 StaRUG (Bestellung)
- § 74 StaRUG (Aufgaben des Restrukturierungsbeauftragten)
- § 75 StaRUG (Obliegenheitspflichten des Beauftragten)
- § 76 StaRUG (Vergütung des Restrukturierungsbeauftragten)
- § 77 StaRUG (Haftung des Restrukturierungsbeauftragten)
- § 78 StaRUG (Pflichtbeauftragung bei Stabilisierungsanordnung)
- §§ 270a ff. InsO a.F. / §§ 270 ff. InsO n.F. (Vergleich: Sachwalter im Eigenverwaltungsverfahren)

---

## Pflichten

### 1. Typen externer Organe im StaRUG

Das StaRUG kennt zwei externe Organe, die in verschiedenen Konstellationen bestellt werden:

| Organ | Rechtsgrundlage | Kernaufgabe | Bestellung |
|---|---|---|---|
| Restrukturierungsbeauftragter | §§ 73-83 StaRUG | Vermittlung, Überwachung, Kontrolle im StaRUG-Verfahren | Gericht (§ 73 StaRUG) |
| Sachwalter | §§ 270-270f InsO | Überwachung der Eigenverwaltung im Insolvenzverfahren | Gericht im Insolvenzverfahren |

**Schlüsselunterschied:** Der Restrukturierungsbeauftragte ist kein Insolvenzverwalter — der Schuldner bleibt voll verfügungsbefugt. Der Sachwalter hingegen operiert im Insolvenzverfahren, wo die Eigenverwaltung bereits eröffnet ist.

### 2. Wann ist der Restrukturierungsbeauftragte obligatorisch?

**Pflichtbestellung (§ 78 StaRUG) in folgenden Fällen:**

1. **Stabilisierungsanordnung** ist erlassen (§ 78 Abs. 1 Nr. 1 StaRUG)
2. **Schutzschirmverfahren** ist beantragt (§ 78 Abs. 1 Nr. 3 StaRUG)
3. **Betroffene Kleingläubiger** (§ 78 Abs. 1 Nr. 2 StaRUG) — wenn der Plan auch die Rechte von Verbrauchern oder kleinen Unternehmen berührt
4. **Auf Antrag von Gläubigern** mit wesentlichem Stimmrecht (§ 73 Abs. 2 StaRUG)

**Fakultative Bestellung (§ 73 Abs. 1 StaRUG):**
- Auf Antrag des Schuldners
- Wenn das Gericht die Bestellung für sinnvoll erachtet

### 3. Aufgaben des Restrukturierungsbeauftragten

**Kernaufgaben (§ 74 StaRUG):**

1. **Überwachung** der Erfüllung der Schuldnerobliegenheiten (§ 52 StaRUG)
2. **Unterstützung** des Gerichts bei der Prüfung der Planvoraussetzungen
3. **Vermittlung** zwischen Schuldner und Gläubigern
4. **Berichterstattung** an das Gericht über Verfahrensfortschritt
5. **Prüfung** der Planbestandteile auf Richtigkeit und Vollständigkeit

**Erweiterter Aufgabenkatalog bei besonderen Verfahren:**
- Prüfung der Vergleichsrechnung auf Plausibilität
- Einholung von Markt- und Branchendaten zur Bewertung
- Stellungnahme zu strittigen Bewertungsfragen

### 4. Auswahl des Restrukturierungsbeauftragten

**Formelle Anforderungen (§ 74 Abs. 2 StaRUG):**
- Unabhängigkeit vom Schuldner und von den Gläubigern
- Fachliche Eignung für Restrukturierungsaufgaben
- Keine Befangenheit

**Vorschlagsrecht:**
- Schuldner hat Vorschlagsrecht (§ 73 Abs. 3 StaRUG)
- Gläubiger können Gegenkandidaten vorschlagen
- Gericht entscheidet — ist an Vorschlag des Schuldners nicht gebunden, wenn Eignungszweifel bestehen

**Praktische Auswahlkriterien:**
- Erfahrung im Restrukturierungsrecht (StaRUG, InsO, IDW S 6)
- Kanzleigröße und -ressourcen für die Aufgabe
- Keine Interessen-Konflikte (frühere Mandate für Gläubiger)
- Branchenkenntnisse (vorteilhaft)

### 5. Honorar-Festsetzung (§ 76 StaRUG)

**Vergütungsrahmen:**
- Vergütung wird vom Gericht festgesetzt (§ 76 Abs. 1 StaRUG)
- Stundensatzbasis oder pauschaliertes Honorar möglich
- Träger: Schuldner (nicht Gläubiger)

**Orientierungswerte (aus der Praxis):**
- Einfache Verfahren (kleine Unternehmen): EUR 200-350 pro Stunde
- Komplexe Verfahren (mittelständisch): EUR 350-500 pro Stunde
- Gesamthonorare variieren stark je nach Verfahrensdauer

**Vergütungsantrag:**
- Restrukturierungsbeauftragter stellt Vergütungsantrag
- Gericht setzt Vergütung fest — kein freies Verhandlungsmandat

---

## Vorgehen

### Schritt 1: Entscheidung über Einbeziehung eines Restrukturierungsbeauftragten

- [ ] Liegt ein Fall vor, der Pflichtbeauftragung erfordert?
- [ ] Ist freiwillige Bestellung sinnvoll (Glaubwürdigkeitsgewinn bei Gläubigern)?
- [ ] Welche Qualifikationen muss der Beauftrage haben?

### Schritt 2: Kandidaten identifizieren und Vorschlag vorbereiten

```
VORSCHLAG RESTRUKTURIERUNGSBEAUFTRAGTER

Vorgeschlagene Person: [Name — fiktiv]
Qualifikationen: [Restrukturierungsrechtler, Fachanwalt für Insolvenzrecht, x Jahre Erfahrung]
Unabhängigkeitserklärung: beigefügt
Honorarvorstellung: EUR [___] pro Stunde, max. EUR [___] Gesamthonorar
Kein Mandat für beteiligte Gläubiger: bestätigt

Begründung der Eignung: [___]
```

### Schritt 3: Zusammenarbeit mit dem Beauftragten

- Vollständige Dokumentation übergeben (Finanzplan, IDW S 6-Gutachten, Gläubigerliste)
- Regelmäßige Statusgespräche vereinbaren
- Transparenz bei allen Verfahrenshandlungen

---

## Templates

### Muster: Informationspaket für Restrukturierungsbeauftragten

```
INFORMATIONSPAKET — RESTRUKTURIERUNGSBEAUFTRAGTER

Gesellschaft: [Firma GmbH]
Übergabedatum: [Datum]
Erstellt von: [GF-Name]

DOKUMENTE (übergeben am [Datum]):

Rechtliche Grundlagen:
 [ ] Gesellschaftsvertrag, letzte Fassung
 [ ] Handelsregisterauszug (aktuell)
 [ ] GF-Bestellungsurkunde

Wirtschaftliche Unterlagen:
 [ ] Letzte drei Jahresabschlüsse
 [ ] Aktuelle BWA ([Monat/Jahr])
 [ ] Liquiditätsplanung 24 Monate
 [ ] Integrierter Finanzplan

Verfahrensunterlagen:
 [ ] Restrukturierungsplan (aktueller Entwurf)
 [ ] Gläubigerliste mit Forderungshöhen
 [ ] Korrespondenz mit Gläubigern
 [ ] Stabilisierungsanordnung (falls erteilt)

Sonstiges:
 [ ] IDW S 11 / IDW S 6 Gutachten
 [ ] Protokolle GF-Sitzungen (letzte 12 Monate)
```

---

## Fallstricke

1. **Vorschlag eines parteiischen Kandidaten** — wenn der vorgeschlagene Beauftragte früher für den Schuldner oder einen Hauptgläubiger gearbeitet hat, ist die Unabhängigkeit zweifelhaft. Das Gericht wird ablehnen, Verfahren verzögert sich.

2. **Informationsblockade gegenüber dem Beauftragten** — mangelnde Kooperation des Schuldners führt zum Verlust des Vertrauens beim Gericht und kann Aufhebung der Stabilisierungsanordnung bewirken.

3. **Honorar unterschätzt** — bei komplexen Verfahren kann das Honorar des Restrukturierungsbeauftragten erheblich sein. Liquiditätsplan muss diese Kosten vorsehen.

4. **Verwechslung mit Insolvenzverwalter** — der Restrukturierungsbeauftragte hat keine Verfügungsgewalt über das Unternehmensvermögen. Falsche Kommunikation gegenüber Mitarbeitern oder Gläubigern kann Unruhe stiften.

5. **Kein Beauftragter bei obligatorischem Fall** — wer bei Stabilisierungsanordnung keinen Restrukturierungsbeauftragten beantragt, riskiert die Ablehnung der Anordnung durch das Gericht.

---

## Querverweise

- → `stabilisierungsanordnung-und-vollstreckungssperre` — Pflichtbeauftragung bei Anordnung
- → `restrukturierungsplan-architektur-paragraph-7ff-starug` — Aufgaben im Planverfahren
- → `cross-class-cram-down-und-absolute-priority` — Rolle im Bestätigungsverfahren
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Informationspflichten
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Zugangsvoraussetzung für das Verfahren


## Aktuelle Leitentscheidungen — Restrukturierungsbeauftragter und Sachwalter

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

§§ 270-270f InsO (Eigenverwaltung und Sachwalter) → § 274 InsO (Pflichten Sachwalter) → § 275 InsO (Mitwirkung bei Kassengeschaeften) → §§ 73-90 StaRUG (Restrukturierungsbeauftragter) → § 73 Abs. 2 StaRUG (Unabhaengigkeit)

## Triage — Beauftragter / Sachwalter

1. **Eigenverwaltung oder StaRUG?** Sachwalter (InsO § 270 ff.) vs. Restrukturierungsbeauftragter (StaRUG §§ 73 ff.) — unterschiedliche Befugnisse.
2. **Unabhaengigkeit geprueft?** Frueherer Berater des Schuldners → Problematisch.
3. **Interessen-Konflikt?** Sachwalter darf kein eigenes Interesse an Verwertungs-Ergebnis haben.
4. **Pflichten-Umfang?** § 274 InsO: Kassenprueung, Zahlungsverkehr-Kontrolle, Bericht an Gericht und Ausschuss.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
