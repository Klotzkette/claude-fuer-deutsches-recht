# Aktenstück 09 — Trusted Flagger nach Art. 22 DSA: Kooperationsabkommen

**Az. Kanzlei:** KRS-2026-0318-DSA
**Bearbeitung:** RAin Dr. Philippa Groth-Steinberg
**Stand:** 02. April 2026

---

## 1. Normgrundlage

Art. 22 DSA schafft das Institut des Trusted Flaggers (vertrauenswürdiger Hinweisgeber). Organisationen, die besondere Sachkunde in der Erkennung illegaler Inhalte besitzen, können beim zuständigen DSC (hier: BNetzA) als Trusted Flagger anerkannt werden. Meldungen von Trusted Flaggern sind von VLOPs vorrangig zu bearbeiten.

---

## 2. Anforderungen an Trusted Flagger (Art. 22 Abs. 2 DSA)

Ein Trusted Flagger muss:
- über spezifische Sachkunde und Kompetenz verfügen
- von den betreffenden Diensteanbietern unabhängig sein
- seine Tätigkeiten zeitnah, sorgfältig und sachlich ausführen

Die Anerkennung erfolgt durch den DSC auf Antrag der Organisation. Die BNetzA hat bislang folgende Organisationen als Trusted Flagger für Deutschland anerkannt (Stand März 2026):

- Deutsche Hass-Stopp e.V. (Hassrede)
- Jugendschutz.net (Inhalte, die Minderjährige gefährden)
- eco — Verband der Internetwirtschaft e.V. (CSAM, Kinderpornographie)

---

## 3. Kooperationsanfrage Deutsche Hass-Stopp e.V.

Am 12. April 2026 hat die Deutsche Hass-Stopp e.V. (anerkannter Trusted Flagger) eine Kooperationsanfrage an Halmweise.de gestellt (vgl. EML `emails/2026-04-12_trusted_flagger_kooperationsanfrage.eml`). Die Anfrage sieht folgendes Kooperationsmodell vor:

- Dedicated API-Schnittstelle für Meldungen (maschinenlesbar)
- Garantierte Bearbeitungszeit von max. 2 Werktagen für TF-Meldungen
- Monatlicher Austausch über Meldetrends
- Gemeinsame Schulungen der Trust & Safety Teams

---

## 4. Pflichten des Anbieters bei Trusted-Flagger-Meldungen

### 4.1 Vorrangige Bearbeitung (Art. 22 Abs. 1 DSA)

VLOPs müssen Meldungen von Trusted Flaggern vorrangig behandeln. Dies bedeutet strukturell kürzere Bearbeitungszeiten als bei Standardmeldungen. Empfohlene SLA: max. 24 Stunden für TF-Meldungen.

### 4.2 Keine automatische Entfernung

Art. 22 DSA begründet keine Automatik. Meldungen von TF müssen inhaltlich geprüft werden; eine automatische Entfernung allein aufgrund einer TF-Meldung ist unzulässig und würde die Nutzungsrechte des Inhaltserstellers verletzen.

### 4.3 Statistikpflichten

Art. 42 Abs. 2 DSA verlangt im VLOP-Transparenzbericht Angaben über:
- Anzahl erhaltener TF-Meldungen
- Anzahl ergriffener Maßnahmen auf Basis von TF-Meldungen
- Medianer Bearbeitungszeitraum für TF-Meldungen

---

## 5. Entwurf Kooperationsvertrag

Folgende Eckpunkte für den Kooperationsvertrag mit Deutsche Hass-Stopp e.V. werden vorgeschlagen:

| Punkt | Inhalt |
|---|---|
| Parteien | Körnerstrom Social GmbH und Deutsche Hass-Stopp e.V. |
| Laufzeit | 2 Jahre, mit automatischer Verlängerung |
| Kündigungsfrist | 3 Monate zum Jahresende |
| API-Zugang | Dedizierter Endpunkt, standardisiertes JSON-Format |
| SLA | 24 Stunden Bearbeitungszeit für TF-Meldungen |
| Rückmeldung | Automatisierte Statusmeldung nach Bearbeitung |
| Datenschutz | Gemeinsame Verantwortlichkeit nach Art. 26 DSGVO, soweit personenbezogene Daten ausgetauscht werden |
| Vertraulichkeit | Meldetrends können aggregiert veröffentlicht werden |
| Haftung | Haftungsausschluss für Meldefehler seitens TF; Körnerstrom haftet für fehlerhafte Entscheidungen |
| Streitbeilegung | Deutsches Recht, Berlin |

---

## 6. Weitere Trusted Flagger — Empfehlungen

Über Deutsche Hass-Stopp e.V. hinaus wird empfohlen, Kooperationsvereinbarungen mit folgenden anerkannten TF abzuschließen:

- **Jugendschutz.net** — relevant für Minderjährigenschutz-Fälle
- **eco e.V.** — relevant für CSAM (Child Sexual Abuse Material)

---

## 7. Abgrenzung: Meldestelle nach Art. 20 DSA

Art. 20 DSA verpflichtet VLOPs zur Einrichtung einer internen Beschwerdestelle für Nutzer, die Entscheidungen anfechten wollen. Diese interne Beschwerdestelle ist von der Trusted-Flagger-Zusammenarbeit (Art. 22 DSA) zu unterscheiden:

| | Art. 20 DSA | Art. 22 DSA |
|---|---|---|
| Wer | Betroffene Nutzer (Inhaltsersteller) | Externe akkreditierte Organisationen |
| Zweck | Anfechtung von Moderationsentscheidungen | Erstmeldung mutmaßlich illegaler Inhalte |
| Priorität | Standardmäßig | Vorrangig |

---

## 8. Rechtsgrundlagen

- Art. 22 DSA (EU) 2022/2065 — Trusted Flagger
- Art. 20 DSA — Interne Beschwerdestelle
- Art. 26 DSGVO (EU) 2016/679 — Gemeinsame Verantwortlichkeit

**Quellen:**
- Verordnung (EU) 2022/2065 (DSA), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2065

---

*Bearbeiterin: RAin Dr. Philippa Groth-Steinberg*
*Stand: 02. April 2026*
