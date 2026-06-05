---
name: verl-bibliothekslizenz-autor
description: "Verl 033 Bibliothekslizenz E Lending Und Zugriff, Verl 003 Autor Herausgeber Mitwirkende Rechtekette: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Verl 033 Bibliothekslizenz E Lending Und Zugriff, Verl 003 Autor Herausgeber Mitwirkende Rechtekette

## Arbeitsbereich

Dieser Skill bündelt **Verl 033 Bibliothekslizenz E Lending Und Zugriff, Verl 003 Autor Herausgeber Mitwirkende Rechtekette** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `verl-033-bibliothekslizenz-e-lending-und-zugriff` | Verlagsrecht: Bibliothekslizenzen für E-Books und E-Lending — UrhG § 27, Onleihe, OverDrive, Lizenzmodelle, EuGH Volksbank-Entscheidung und Zugangssteuerung. |
| `verl-003-autor-herausgeber-mitwirkende-rechtekette` | Verlagsrecht: Rechtekette bei Sammelwerken — Autor, Herausgeber, Mitwirkende, Übersetzer und Verlag; Klärung von Urheber-, Nutzungs- und Vergütungsrechten nach UrhG und VerlG. |

## Arbeitsweg

Für **Verl 033 Bibliothekslizenz E Lending Und Zugriff, Verl 003 Autor Herausgeber Mitwirkende Rechtekette** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `verlagsrecht-buchpreisbindung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `verl-033-bibliothekslizenz-e-lending-und-zugriff`

**Fokus:** Verlagsrecht: Bibliothekslizenzen für E-Books und E-Lending — UrhG § 27, Onleihe, OverDrive, Lizenzmodelle, EuGH Volksbank-Entscheidung und Zugangssteuerung.

# Verl-033 · Bibliothekslizenz, E-Lending und Zugriff

## Zweck dieses Skills

Öffentliche und wissenschaftliche Bibliotheken haben besondere Rechte und Lizenzanforderungen für die Bereitstellung von E-Books. Dieser Skill klärt die Rechtslage beim E-Lending, die verschiedenen Lizenzmodelle, Preisbindungsfragen und aktuelle EU-Rechtsprechung zur digitalen Ausleihe.

## Rechtsgrundlagen

| Norm | Inhalt | Quelle |
|------|--------|-------|
| UrhG § 27 | Bibliothekstantieme: Vergütung für Verleih (körperliche Exemplare) | https://dejure.org/gesetze/UrhG/27.html |
| UrhG § 19a | Recht der öffentlichen Zugänglichmachung (E-Book-Ausleihe) | https://dejure.org/gesetze/UrhG/19a.html |
| UrhG § 52b | Wiedergabe an elektronischen Leseplätzen in Bibliotheken | https://dejure.org/gesetze/UrhG/52b.html |
| BuchPrG §§ 5, 6 | Buchpreisbindung: Bibliotheken als Letztabnehmer | https://www.gesetze-im-internet.de/buchprg/ |
| EuGH C-174/15 | Volksbank Digitale Ausleihe: Pflicht der Mitgliedstaaten zur E-Lending-Regelung | https://eur-lex.europa.eu |
| DSM-RL Art. 8 | Vergriffene Werke und Bibliotheken | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Rechtslage E-Lending in Deutschland

### Grundprinzip
- E-Books sind keine körperlichen Gegenstände; das Erschöpfungsprinzip (§ 17 UrhG) gilt **nicht** für digitale Inhalte.
- Bibliothek darf E-Books nur ausleihen, wenn sie eine Lizenz vom Verlag hat.
- Keine gesetzliche „Bibliotheksschranke" für digitale Ausleihe vergleichbar der körperlichen Ausleihe (§ 27 UrhG).

### EuGH C-174/15 (Stichting Leenrecht / VOB, „Volksbank")
- EuGH hat 2016 entschieden: Mitgliedstaaten können die digitale Ausleihe von E-Books durch Bibliotheken unter bestimmten Bedingungen dem Verleihrecht analog regeln.
- Voraussetzungen: Bibliothek hat rechtmäßige Kopie; nur ein Nutzer gleichzeitig; nach Ausleihe kein Verbleib beim Nutzer; angemessene Vergütung.
- Deutschland: Hat diese Regelung bisher nicht vollständig umgesetzt; E-Lending basiert auf vertraglichen Lizenzen.

## E-Lending-Plattformen

### Onleihe (DiViBib / ekz)
- Größte E-Lending-Plattform in Deutschland; Konsortium öffentlicher Bibliotheken.
- Lizenzierungsmodell: Bibliothek kauft Lizenz pro E-Book-Exemplar (single-copy model).
- Ein Nutzer je Exemplar gleichzeitig; Ausleihdauer: 7, 14 oder 21 Tage.
- Rückgabe: Automatisch nach Ablauf; kein Kopieren möglich.

### OverDrive / Libby
- Internationaler Anbieter; in Deutschland v.a. für wissenschaftliche Bibliotheken.
- Verschiedene Lizenzmodelle: Per-Checkout, Metered Access (X Ausleihen gesamt), Perpetual Access.

### Wissenschaftliche Bibliotheken: PDA / Patron-Driven Acquisition
- Bibliothek lizenziert Pool von E-Books; Nutzer kann auf alle zugreifen; Bibliothek zahlt erst bei tatsächlicher Ausleihe.
- Lizenzmodell vom Verlag definiert.

## Lizenzmodelle für E-Lending

| Modell | Beschreibung | Kosten | Für wen |
|--------|-------------|--------|---------|
| Single Copy | Eine Lizenz = ein Nutzer gleichzeitig | Pro Exemplar | Öffentliche Bibliotheken |
| Multi-User | Mehrere Nutzer gleichzeitig (x gleichzeitige Nutzer) | Aufschlag auf Einzellizenz | Uni-Bibliotheken |
| Metered Access | X Ausleihen gesamt, dann abgelaufen | Pauschal | Mittel-Bibliotheken |
| Perpetual Access | Dauerhafter Zugang ohne Laufzeitbeschränkung | Einmalig | Große Bibliotheken |
| Subscription | Jährliche Abonnement-Lizenz | Jahresgebühr | Hochschulkonsortien |

## Preisbindung für Bibliothekslizenzen

- Bibliotheken kaufen E-Book-Lizenzen, keine körperlichen Bücher → Preisbindung (BuchPrG) gilt streng genommen nicht für Lizenzverträge (nur für Bücher i.S.d. § 2 BuchPrG).
- **Praxis**: Verlage setzen Bibliothekspreise für Lizenzen frei; keine BuchPrG-Bindung.
- Für physische Bücher, die Bibliotheken kaufen: BuchPrG gilt; Bibliothek ist Letztabnehmer (§ 5 BuchPrG).

## § 52b UrhG — Elektronische Leseplätze

- Bibliotheken dürfen auf Terminals in Bibliotheksräumen urheberrechtlich geschützte Werke anzeigen.
- Voraussetzung: Lizenzangebot des Verlags; Anzahl der Terminals ≤ Anzahl erworbener körperlicher Exemplare.
- BGH „Elektronische Leseplätze II", I ZR 69/11: Kontext bestätigt; nur körperlich vorhandene Exemplare dürfen gleichzeitig angezeigt werden.

## Vergriffene Werke und Bibliotheken (DSM-RL Art. 8)

- DSM-RL Art. 8–11: Bibliotheken dürfen vergriffene Werke digitalisieren und zugänglich machen, wenn Rechteklärung erfolgt ist.
- Deutschland: Umsetzung in § 61d ff. UrhG (Sonderregelung für Kultureinrichtungen).
- Verlag kann Opt-Out erklären: „Mein Werk ist nicht vergriffen; keine Bibliotheksdigitalisierung."

## Typische Fallen

- **E-Lending ohne Lizenz**: Bibliothek stellt E-Books ohne Verlagslizenz auf eigener Plattform bereit → Urheberrechtsverletzung (§ 97 UrhG).
- **Single-Copy-Lizenz mit Multi-Zugang**: Bibliothek implementiert Plattform, die mehrere gleichzeitige Nutzer erlaubt → Vertragsverletzung.
- **Preisbindung für physische Bücher an Bibliotheken**: Buchhandlung gewährt Bibliothek 15 % unter Ladenpreis ohne Verlagsfreigabe → Preisbindungsverstoß.
- **§ 52b-Überschreitung**: Bibliothek zeigt mehr Terminals an als Buchexemplare vorhanden → Urheberrechtsverletzung.

## Checkliste Bibliothekslizenz

- [ ] Lizenzvertrag mit E-Lending-Plattform abgeschlossen (Onleihe, OverDrive, etc.)
- [ ] Lizenzmodell und gleichzeitige Nutzer klar definiert
- [ ] Preisbindung für physische Bibliothekskäufe geprüft (Buchhandel als Zwischenstufe)
- [ ] § 52b-Compliance: Terminanzahl ≤ Exemplaranzahl
- [ ] Vergriffene Werke: Opt-Out gegenüber Bibliotheken erklärt (falls nötig)
- [ ] E-Lending-Plattformvertrag auf Datenschutz geprüft (DSGVO)

## Quellenreferenzen

- UrhG §§ 27, 52b: https://dejure.org/gesetze/UrhG/52b.html
- EuGH C-174/15 (Volksbank): https://eur-lex.europa.eu
- DSM-RL Art. 8: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- BGH „Elektronische Leseplätze II" I ZR 69/11: https://www.bgh.de
- Onleihe / DiViBib: https://www.onleihe.de

## Output-Formate

- **Lizenzmodell-Vergleich**: Single Copy, Multi-User, Metered Access
- **E-Lending-Vertragsprüfung**: Plattformvertrag auf Konformität
- **Preisbindungscheck für Bibliothekskäufe**
- **Vergriffene-Werke-Opt-Out-Erklärung**
- **§ 52b-Compliance-Protokoll**

## 2. `verl-003-autor-herausgeber-mitwirkende-rechtekette`

**Fokus:** Verlagsrecht: Rechtekette bei Sammelwerken — Autor, Herausgeber, Mitwirkende, Übersetzer und Verlag; Klärung von Urheber-, Nutzungs- und Vergütungsrechten nach UrhG und VerlG.

# Verl-003 · Autor, Herausgeber, Mitwirkende: Rechtekette im Sammelwerk

## Zweck dieses Skills

Verlagsprojekte mit mehreren Beteiligten — Herausgeberbände, Anthologien, wissenschaftliche Festschriften, Lehrwerke — erfordern eine sorgfältige **Rechtekette**: Wer hat welche Urheberrechte, wer hat welche Nutzungsrechte eingeräumt, wer hat welchen Vergütungsanspruch? Dieser Skill kartiert alle Beteiligten, ihre Rollen und ihre Rechtsposition systematisch.

## Rechtsgrundlagen

| Norm | Regelungsgehalt | Quelle |
|------|----------------|--------|
| UrhG § 2 | Schutzfähige Werke: Sprachwerke, Sammelwerke, Übersetzungen | https://dejure.org/gesetze/UrhG/2.html |
| UrhG § 4 | Sammelwerke und Datenbankwerke | https://dejure.org/gesetze/UrhG/4.html |
| UrhG § 8 | Miturheber: gemeinschaftliche Schöpfung | https://dejure.org/gesetze/UrhG/8.html |
| UrhG § 9 | Werkverbindung: selbständige Werke | https://dejure.org/gesetze/UrhG/9.html |
| UrhG § 31 | Nutzungsrechtseinräumung | https://dejure.org/gesetze/UrhG/31.html |
| UrhG § 32 | Angemessene Vergütung | https://dejure.org/gesetze/UrhG/32.html |
| UrhG § 32d | Auskunftsanspruch | https://dejure.org/gesetze/UrhG/32d.html |
| VerlG § 1 | Verlagsvertrag mit dem Urheber | https://www.gesetze-im-internet.de/verlg/__1.html |
| VerlG §§ 28 ff. | Honorar und Abrechnung | https://www.gesetze-im-internet.de/verlg/ |
| DSM-RL Art. 19 | Transparenzpflicht gegenüber Urhebern | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790 |

## Beteiligte Parteien und ihre Rollen

### 1. Alleinautor
- Einziger Schöpfer des Werks; alle Urheberrechte liegen bei ihm.
- Kann alle Nutzungsrechte im Verlagsvertrag vollständig einräumen.

### 2. Miturheber (§ 8 UrhG)
- Mehrere haben gemeinsam ein Werk geschaffen; Beiträge sind nicht trennbar.
- Nutzungsrechte können nur gemeinschaftlich eingeräumt werden; einzelne Miturheber können nicht allein handeln.
- Verfügungen über Anteile am Gesamtwerk erfordern Zustimmung aller.

### 3. Werkverbindung (§ 9 UrhG)
- Mehrere Autoren verbinden selbständige Werke zu einem gemeinsamen Werk (z.B. Text + Illustrationen).
- Jeder behält sein Urheberrecht; gemeinschaftliche Rechteausübung nach Vereinbarung.

### 4. Herausgeber eines Sammelwerks (§ 4 UrhG)
- Schöpferische Eigenleistung bei Auswahl und Anordnung der Beiträge → eigenes Urheberrecht an der Sammlung.
- Kein Urheberrecht an den Einzelbeiträgen der Autoren.
- Verlagsvertrag mit dem Herausgeber regelt Rechte an der Sammlung; separate Verträge mit Beitragsautoren nötig.

### 5. Beitragsautoren (Kapitelautoren, Essayisten)
- Jeder hält sein Urheberrecht am eigenen Beitrag.
- Nutzungsrechtseinräumung an Herausgeber oder Verlag durch separate Autorenverträge oder Erklärungen.
- Vergütungsanspruch nach § 32 UrhG; gemeinsame Vergütungsregeln anwendbar.

### 6. Übersetzer
- Übersetzung ist ein selbständiges Schutzwerk (§ 3 UrhG).
- Übersetzer benötigt Lizenz des Originalautors/Verlags; Verlagsvertrag für Übersetzung separat (VerlG § 35).
- Eigener Vergütungsanspruch; ggf. eigener Auskunftsanspruch nach § 32d UrhG.

### 7. Illustratoren, Fotografen, Kartografen
- Bildwerke (§ 2 Abs. 1 Nr. 5 UrhG) sind eigenständig geschützt.
- Nutzungsrechtseinräumung durch separate Bildrechte-Verträge oder Werk-/Dienstverträge.
- Bei Auftragsarbeiten: Kein automatischer Rechteübergang; schriftliche Einräumung erforderlich.

## Rechteketten-Analyse

### Schritt 1: Identifikation aller Werkteile
Liste alle Komponenten des Gesamtwerks:
- Haupttext (Autor/Autoren)
- Kapitel (ggf. verschiedene Autoren)
- Vorwort, Einleitung, Nachwort (Herausgeber oder Dritte)
- Abbildungen, Fotos, Grafiken
- Tabellen, Karten, Diagramme
- Übersetzungen
- Register, Index (Sonderfall: Leistungsschutz oder Datenbankrecht)

### Schritt 2: Prüfung jeder Nutzungsrechtseinräumung
Für jede Komponente prüfen:
- Liegt eine schriftliche Nutzungsrechtseinräumung vor?
- Welche Nutzungsarten sind erfasst (§ 31 Abs. 1 UrhG)?
- Exklusiv oder nicht-exklusiv?
- Zeitlich und räumlich begrenzt?
- Vergütung vereinbart und angemessen (§ 32 UrhG)?

### Schritt 3: Lücken und Risiken
- Fehlende Verträge mit Beitragsautoren → Verlag hat kein Recht zur Veröffentlichung
- Unklare Nutzungsarten → Zweckübertragungsregel (§ 31 Abs. 5 UrhG) schließt Lücken restriktiv
- Kein Auskunftsanspruch geregelt → Beitragsautoren können § 32d UrhG geltend machen
- Übersetzungsrechte nicht gesichert → Fremdsprachige Ausgabe rechtswidrig

## Vergütungsansprüche und Auskunft

### § 32 UrhG — Angemessene Vergütung
- Jeder Urheber hat Anspruch auf angemessene Vergütung.
- Unangemessene Vergütung → Anpassungsanspruch; ggf. Klage.
- Gemeinsame Vergütungsregeln (§ 36 UrhG) zwischen Verbänden schaffen Vermutungswirkung.

### § 32a UrhG — Nachvergütung (Bestseller-Paragraf)
- Stellt sich heraus, dass vereinbarte Vergütung in auffälligem Missverhältnis zu tatsächlichen Erträgen steht → Anspruch auf weitere Beteiligung.
- Gilt für alle Miturheber und Beitragsautoren anteilig.

### § 32d UrhG — Auskunftsanspruch
- Jeder Urheber kann jährlich Auskunft über Art und Umfang der Werknutzung sowie erzielte Vergütungen verlangen.
- DSM-RL Art. 19 gibt EU-rechtliche Grundlage für verstärkte Transparenzpflichten.

## Typische Fallen

- **Fehlende Verträge mit Beitragsautoren**: Häufig bei Tagungsbänden oder Festschriften; ohne schriftliche Nutzungsrechtseinräumung kein Veröffentlichungsrecht.
- **Herausgeber-Rolle überschätzt**: Herausgeber hat kein Recht, im Namen der Beitragsautoren Lizenzen zu vergeben, sofern keine Vollmacht vorliegt.
- **Übersetzungsrechte nicht separat gesichert**: Originalverlag hat oft keine Lizenz für alle Sprachversionen.
- **Bildrechte vergessen**: Fotos in der Originalveröffentlichung decken nicht automatisch die Nutzung in digitalen Ausgaben ab.
- **Miturheber-Blockade**: Bei § 8 UrhG-Situationen kann ein Miturheber die Verwertung blockieren.

## Checkliste Rechtekette

- [ ] Liste aller Werkteile mit Urhebern erstellt
- [ ] Für jeden Werkteil: schriftlicher Nutzungsrechtsvertrag vorhanden
- [ ] Nutzungsarten vollständig und klar benannt
- [ ] Vergütung angemessen und nachvollziehbar (§ 32 UrhG)
- [ ] Auskunftsklausel (§ 32d UrhG / DSM-RL Art. 19) vertraglich geregelt
- [ ] Drittmaterial (Bilder, Tabellen) mit eigenem Rechtenachweis

## Quellenreferenzen

- UrhG §§ 4, 8, 9: https://dejure.org/gesetze/UrhG/8.html
- UrhG § 32d: https://dejure.org/gesetze/UrhG/32d.html
- DSM-Richtlinie 2019/790 Art. 19: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790
- BGH, Urt. v. 20.01.1994 – I ZR 322/91 (Miturheber Sammelwerk): https://www.bgh.de
- VerlG §§ 28 ff.: https://www.gesetze-im-internet.de/verlg/

## Output-Formate

- **Rechtekettenmatrix**: Alle Werkteile × Nutzungsarten × Rechtsstatus
- **Lückenliste**: Fehlende Verträge, offene Nutzungsarten
- **Vergütungsübersicht**: Alle Beitragsautoren mit Vergütungsansprüchen
- **Muster-Beitragsautorenvertrag**: Standardisiertes Kurzformular für Sammelwerke
