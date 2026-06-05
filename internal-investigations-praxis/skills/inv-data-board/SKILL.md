---
name: inv-data-board
description: "Inv 022 Data Room For Counsel, Inv 023 Board Special Committee: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 022 Data Room For Counsel, Inv 023 Board Special Committee

## Arbeitsbereich

Dieser Skill bündelt **Inv 022 Data Room For Counsel, Inv 023 Board Special Committee** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-022-data-room-for-counsel` | Richtet einen sicheren virtuellen Data Room für externe Counsel, Behörden und US-Discovery ein – Zugang, Privilegierung, Protokollierung. |
| `inv-023-board-special-committee` | Richtet ein Sonderuntersuchungsausschuss des Vorstands oder Aufsichtsrats ein – Mandat, Besetzung, Unabhängigkeit und Berichtspflichten. |

## Arbeitsweg

Für **Inv 022 Data Room For Counsel, Inv 023 Board Special Committee** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-022-data-room-for-counsel`

**Fokus:** Richtet einen sicheren virtuellen Data Room für externe Counsel, Behörden und US-Discovery ein – Zugang, Privilegierung, Protokollierung.

# Sicherer Data Room für Counsel und Behörden

## Rechtlicher Rahmen

Der virtuelle Data Room (VDR) ist das zentrale Instrument für die kontrollierte Weitergabe von Untersuchungsdokumenten an externe Anwälte, Behörden, US-Counsel oder DOJ/SEC. Die Nutzung eines VDR ermöglicht Need-to-know-Zugangskontrolle, Zugriffsprotokollierung und Wasserzeichnung – alles kritisch für Privilegeschutz, DSGVO-Konformität und Beweiskettensicherheit. Die DSGVO verlangt für den Datentransfer in Drittstaaten nach Art. 46 eine geeignete Garantie (SCC, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)). Beschlagnahme von VDR-Inhalten ist möglich (§ 94 StPO), wenn der Anbieter oder seine Server in Deutschland oder der EU ansässig sind.

## Ziel dieses Skills

Dieser Skill stellt den technisch und rechtlich korrekten Aufbau und Betrieb eines VDR für Internal Investigations sicher.

## Arbeitsprogramm

### 1. Auswahl des VDR-Anbieters
- EU-basierter Anbieter bevorzugen (kein US-CLOUD-Act-Risiko bei EU-only-Hosting).
- Zertifizierungen: ISO 27001, SOC 2 Type II.
- Funktionen: Wasserzeichen, View-only-Modus (kein Download), granulare Zugangskontrolle, Audit Trail.
- DSGVO-Konformität: Auftragsverarbeitungsvertrag (Art. 28 DSGVO) abschließen.
- Drittstaatentransfer: wenn US-Anwälte oder DOJ Zugang erhalten, SCC oder anderes Schutzinstrument.

### 2. Zugangskontrolle und Benutzergruppen
- Benutzergruppen definieren: Interne Anwälte, Externe Anwälte, Forensiker, Behörden (nur Faktenbericht), US-Counsel.
- Jede Gruppe sieht nur die Dokumente, die für ihre Rolle bestimmt sind.
- Einzelpersonen-Zugang mit Audit Trail: wer hat wann welches Dokument wie lange geöffnet?
- Zeitlich befristeter Zugang: VDR-Zugang nach Abschluss der Untersuchung automatisch deaktivieren.

### 3. Dokumentenstruktur im VDR
- **Privilegiert – nur interne Anwälte**: Vollbericht, Interviewprotokolle, Rechtsgutachten.
- **Faktenbericht**: für Behörden und externe Berater ohne volles Privilege.
- **Forensik-Ergebnisse**: für IT-Forensiker und technische Berater.
- **Board Materials**: für Aufsichtsrat und Audit Committee.
- **Correspondence**: E-Mail-Verkehr mit Behörden.
- Klare Ordnerstruktur mit Versionsverwaltung; keine Dokumente in falsche Ordner hochladen.

### 4. Wasserzeichen und DRM
- Dynamische Wasserzeichen (Benutzername + Datum + IP) auf allen angezeigten Dokumenten.
- View-only-Modus: kein Download, kein Drucken ohne Genehmigung.
- Screenshot-Schutz: technisch schwer vollständig, aber dokumentiert, dass Schutzmaßnahmen ergriffen wurden.
- Print-Tracking: jeder Druckauftrag wird protokolliert.

### 5. Herausgabe an Behörden
- Vor Herausgabe: Privilegierungsanalyse aller Dokumente in dem für die Behörde freigegebenen Ordner.
- Privilege-Log für alle zurückgehaltenen Dokumente.
- Keine Herausgabe von Dokumenten, die Inhouse-Counsel-Kommunikation enthalten (kein EU-Privilege nach Akzo Nobel, aber deutsches Recht schützt ggf. weitere Kategorien).
- Drittstaaten-Herausgabe (DOJ, SEC): DSGVO Art. 49 Abs. 1 lit. e (Strafverfolgungsausnahme) nur eng; vorher Rechtsberatung.

### 6. DSGVO-Konformität
- Personenbezogene Daten im VDR: Verzeichnis der Verarbeitungstätigkeiten (Art. 30 DSGVO) aktualisieren.
- Betroffenenrechte: Auskunftsrecht (Art. 15 DSGVO) – kann Betroffener VDR-Dokumente anfordern? § 29 BDSG ermöglicht Einschränkung während laufender Untersuchung.
- Löschplan: nach Abschluss der Untersuchung VDR-Daten nach DSGVO-Grundsätzen löschen.

### 7. Sicherheitsvorfälle
- VDR-Datenpanne: Art. 33 DSGVO – Meldung binnen 72 Stunden an Datenschutzbehörde.
- Verdacht auf unberechtigten Zugriff: sofortige Sperrung des verdächtigen Accounts; Forensik-Log prüfen.
- Backup: tägliches automatisches Backup; Wiederherstellungsplan dokumentieren.

## Red-Team-Fragen

- Ist der VDR-Anbieter DSGVO-konform und wurde ein Art. 28-Vertrag abgeschlossen?
- Werden alle Zugriffe im Audit Trail lückenlos protokolliert und regelmäßig ausgewertet?
- Haben Behörden Zugang zu privilegierten Dokumenten erhalten, ohne dass eine Waiver-Entscheidung getroffen wurde?
- Ist der Drittstaatentransfer (US-Counsel, DOJ) durch SCC oder eine andere DSGVO-Grundlage gedeckt?
- Wurden Wasserzeichen und View-only-Modus auf alle sensiblen Dokumente angewandt?
- Ist der VDR-Zugang nach Abschluss der Untersuchung deaktiviert und wurden die Daten gelöscht?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| Art. 28 DSGVO | Auftragsverarbeitung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 46 DSGVO | Drittstaatentransfer | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 33 DSGVO | Datenpannenmeldung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 94 StPO | Beschlagnahme | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__94.html) |
| EuGH C-550/07 P | Akzo Nobel Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |

## Ausgabeformate

- **VDR-Setup-Checkliste** (Anbieterauswahl, Zugangskontrolle, Wasserzeichen)
- **Benutzergruppen-Matrix** (Rolle × Zugangsberechtigung × Dokumente)
- **Ordnerstruktur-Vorlage** für Untersuchungs-VDR
- **Art. 28-DSGVO-Checkliste** für VDR-Anbieter
- **Herausgabe-Protokoll** für Behörden

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-023-board-special-committee`

**Fokus:** Richtet ein Sonderuntersuchungsausschuss des Vorstands oder Aufsichtsrats ein – Mandat, Besetzung, Unabhängigkeit und Berichtspflichten.

# Board Special Committee und Sonderuntersuchungsausschuss

## Rechtlicher Rahmen

Ein Sonderuntersuchungsausschuss (Special Committee) ist ein Unterorgan des Vorstands oder Aufsichtsrats, das mit der unabhängigen Untersuchung eines spezifischen Sachverhalts beauftragt wird. Im deutschen Recht folgt die Befugnis des Aufsichtsrats zur Einrichtung von Ausschüssen aus § 107 Abs. 3 AktG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__107.html)), die des Vorstands aus § 77 AktG. Das Special Committee dient der Unabhängigkeit von der regulären Unternehmensführung und ist insbesondere dann erforderlich, wenn Vorstandsmitglieder selbst Gegenstand der Untersuchung sind.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass das Special Committee ordnungsgemäß eingerichtet wird, die richtigen Personen besetzt, ein klares Mandat hat und seine Ergebnisse verwertbar sind.

## Arbeitsprogramm

### 1. Wann ist ein Special Committee erforderlich?
- Vorstandsmitglieder sind selbst in den Untersuchungsgegenstand involviert (Interessenkonflikt).
- Betrag des potenziellen Schadens ist materiell (erhebliche D&O-Haftungsrisiken).
- US-Börsennotierung: SEC-Anforderungen und Delaware Corporate Law verlangen häufig Independent Committee für Derivative Actions.
- DOJ/SEC erwarten unabhängige Untersuchung als Teil einer Kooperationsstrategie.

### 2. Einrichtungsbeschluss
- Aufsichtsrat: Beschluss nach § 107 Abs. 3 AktG mit klarem Mandat (Untersuchungsgegenstand, Befugnisse, Berichtspflicht, Zeitrahmen).
- Vorstand: nur wenn kein Aufsichtsratsmitglied involviert; anderenfalls liegt die Initiative beim Aufsichtsrat.
- Dokumentation: Beschluss im Board-Protokoll mit vollständigem Mandat.

### 3. Besetzung und Unabhängigkeit
- Mindestens zwei unabhängige Mitglieder (ohne Interessenkonflikt zu Untersuchungsgegenstand).
- Unabhängigkeitskriterien: keine frühere Geschäftsbeziehung mit Beschuldigten, kein familiäres Verhältnis, keine anderen Loyalitätskonflikte.
- Externer Anwalt dem Special Committee direkt mandatiert (nicht dem Gesamtvorstand).
- Unabhängigkeit ist Voraussetzung für Glaubwürdigkeit bei DOJ, SEC und BaFin.

### 4. Mandat des Special Committee
- Klarer Scope: was darf/muss das Committee untersuchen?
- Befugnisse: Zugang zu allen Dokumenten, Recht zur Beauftragung externer Berater auf Unternehmenskosten, Interviewrecht gegenüber allen Mitarbeitern.
- Berichtspflicht: ausschließlich an Aufsichtsrat (nicht an Vorstand, wenn dieser involviert ist).
- Handlungskompetenzen: darf das Committee Sofortmaßnahmen veranlassen (z. B. Freistellung)?

### 5. Privilegeschutz des Special Committee
- Anwalt des Special Committee ist nur dem Committee verantwortlich; Kommunikation ist privilegiert.
- Vorstand hat keinen Anspruch auf Einsicht in Anwaltsdokumente des Special Committee.
- Attorney-Client Privilege: bei US-Bezug klären, ob Special-Committee-Privilege dem Unternehmen oder dem Committee selbst gehört.

### 6. Berichterstattung
- Zwischenberichte an Aufsichtsrat: regelmäßig und bei wesentlichen Ergebnissen.
- Abschlussbericht: analog zur allgemeinen Berichtsstruktur (vgl. inv-011-reporting), aber Adressat ist ausschließlich der Aufsichtsrat.
- Maßnahmenempfehlungen: klar benannte Verantwortlichkeiten, Fristen, Nachverfolgung.

### 7. Abberufung und Reorganisation
- Falls Vorstandsmitglied freigestellt werden soll: § 84 Abs. 3 AktG (Abberufung bei wichtigem Grund, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__84.html)).
- Special Committee kann Empfehlung zur Abberufung an Aufsichtsrat aussprechen.
- Interim-Management: wer führt die Geschäfte während der Freistellung?

## Red-Team-Fragen

- Ist das Special Committee tatsächlich unabhängig, oder gibt es versteckte Verbindungen zu Beschuldigten?
- Hat das Committee das nötige Mandat, um alle relevanten Dokumente und Personen zu erreichen?
- Sind die externen Anwälte dem Committee direkt mandatiert – oder faktisch dem CFO oder GC, der selbst involviert sein könnte?
- Genügt das Special Committee den Unabhängigkeitskriterien für ein US-DOJ/SEC-Kooperationsszenario?
- Ist der Privilegeschutz für Committee-Unterlagen gegenüber dem (involvierten) Vorstand gesichert?
- Wurde der Beschluss des Aufsichtsrats korrekt im Protokoll dokumentiert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 107 AktG | Ausschüsse des Aufsichtsrats | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__107.html) |
| § 84 AktG | Abberufung Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__84.html) |
| § 77 AktG | Geschäftsführung Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__77.html) |
| § 93 AktG | Sorgfaltspflicht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| BGH II ZR 234/09 | Siemens/Neubürger | [openjur.de](https://openjur.de/o/577696.html) |

## Ausgabeformate

- **Special-Committee-Beschlussvorlage** (Mandat, Besetzung, Befugnisse)
- **Unabhängigkeitsprüfungs-Matrix** für Committee-Mitglieder
- **Mandatierungsschreiben** für externen Anwalt des Committee
- **Berichtspflichten-Schema** (Häufigkeit, Format, Adressat)
- **Freistellungsbeschluss-Vorlage** (§ 84 AktG)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
