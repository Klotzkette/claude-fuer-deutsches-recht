# Megaprompt: datenbankrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 65 Skills des Plugins `datenbankrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt …
2. **abmahnung-pruefen-datenbankrecht** — Prüfung einer erhaltenen Datenbankrechts-Abmahnung: Berechtigungs-Check des Abmahnenden (§ 87a Abs. 2 UrhG), Verletzungs…
3. **agb-auskunft-rechnungslegung** — Gestaltung und Prüfung datenbankrechtsrelevanter AGB-Klauseln: § 307 BGB-Inhaltskontrolle für Nutzungsverbote, Scraping-…
4. **agrar-logistik-cyberincident** — Datenbankrecht für Agrar- und Sensordaten: §§ 87a-87e UrhG für Präzisionslandwirtschaftsdatenbanken und IoT-Sensornetzwe…
5. **api-nutzung-rate-limits-und-vertragsbruch** — Prüft die rechtliche Bewertung von API-Nutzung im Datenbankkontext: Vertragsbruch bei Überschreitung von Rate-Limits ode…
6. **auskunft-rechnungslegung-schadensschaetzung** — Auskunft, Rechnungslegung und Schadensschätzung im Datenbankrecht nach §§ 97 101 UrhG: Dreigliedrige Schadensberechnung …
7. **b2b-kundendaten-datenbank-insolvenz-als** — Analysiert Datenbankherstellerrecht (§§ 87a-87e UrhG) und GeschGehG bei CRM-Datenbankexporten durch ausscheidende Mitarb…
8. **backup-export-und-vendor-lock** — Datenbankrecht bei Backup-Rechten, Datenexport und Vendor-Lock-in: § 87c UrhG erlaubte Entnahmen für rechtmäßige Nutzer,…
9. **beweissicherung-durch-testcrawler** — Rechtssichere Beweissicherung durch Testcrawler bei Datenbankrechts-Verletzungen: Aufbau und Betrieb eines eigenen Testc…
10. **cease-and-abmahnung-pruefen-datenbankvergleich** — Cease-and-Desist-Letter (Abmahnung) im Datenbankrecht nach § 97a UrhG: Anforderungen an wirksame Abmahnung (Verletzungsh…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext ordnet der Skill das Material eig..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Datenbankrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Datenbankrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen. Tragende Normen (UrhG §§ 87a ff., Richtlinie 96/9/EG, Data Act) werden nicht aus Modellwissen finalisiert, sondern über die zugelassenen Live-Quellen geprüft.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Sofortrisiken zuerst markieren** — Fristen, Zustellung, Form, Zuständigkeit, Beweis-, Kosten- und Haftungsrisiken benennen.
2. **Aktenlandkarte bauen** — Welche Dateien sind Original, welche nur Behauptung; was fehlt für einen verwertbaren nächsten Schritt?
3. **Rolle klären** — Mandant, Gegner, Behörde, Gericht, betroffene Stelle; mit welchem Ziel und welcher Reichweite?
4. **Ziel bestimmen** — Prüfung, Entwurf, Antrag, Anmeldung, Schriftsatz, Verteidigung, Dashboard, Memo, Red-Team?
5. **Rechtsquellen trennen** — Normtext, Behördenpraxis, Rechtsprechung, Vertrag, technischer Standard und Praxisroutine getrennt halten.
6. **Fachmodule auswählen** — Drei bis sieben passende Skills aus diesem Plugin nennen mit Begründung, warum sie jetzt nützlich sind.
7. **Erste verwertbare Ausgabe liefern** — Kurze Lagekarte mit nächstem Schritt oder erstem Entwurf, statt einer langen abstrakten Abhandlung.

## Fachlicher Anker — Datenbankrecht

Tragende Anker: UrhG §§ 87a ff., Richtlinie 96/9/EG, Data Act. Tatsächliche Fundstellen werden über dejure.org, openJur, gesetze-im-internet.de, BGH-/BVerfG-/EuGH-/EuG-Datenbank live geprüft und nicht aus Modellwissen finalisiert.

---

## Skill: `abmahnung-pruefen-datenbankrecht`

_Prüfung einer erhaltenen Datenbankrechts-Abmahnung: Berechtigungs-Check des Abmahnenden (§ 87a Abs. 2 UrhG), Verletzungstatbestand (§ 87b UrhG), Vollständigkeitscheck der Unterlassungserklärung, Verjährung, Vertragsstrafe-Angemessenheit (§ 339 BGB) und Handlungsoptionen (Unterzeichnung, Widerspru..._

# Abmahnung prüfen im Datenbankrecht — Checkliste und Reaktionsoptionen

## Arbeitsbereich

Prüfung einer erhaltenen Datenbankrechts-Abmahnung: Berechtigungs-Check des Abmahnenden (§ 87a Abs. 2 UrhG), Verletzungstatbestand (§ 87b UrhG), Vollständigkeitscheck der Unterlassungserklärung, Verjährung, Vertragsstrafe-Angemessenheit (§ 339 BGB) und Handlungsoptionen (Unterzeichnung, Widerspruch, Schutzschrift). Erstellt Antwortschreiben und Risikoabwägung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Unternehmen hat heute Morgen eine Abmahnung wegen Datenbankrechts-Verletzung erhalten und muss innerhalb von 5 Tagen reagieren.
- Startup bezweifelt, dass der Abmahnende überhaupt Inhaber des behaupteten Datenbankherstellerrechts ist — wie prüft man das?
- Anwalt soll beurteilen, ob die geforderte Unterlassungserklärung zu weit gefasst ist und ob eine modifizierte Erklärung ausreicht.

## Erste Schritte

1. Abmahnenden identifizieren: Wer mahnt ab, und hat er Herstellerrecht am behaupteten Datenbankrecht (§ 87a Abs. 2 UrhG — Investition, Initiative, Risiko)?
2. Verletzungsvorwurf überprüfen: Welche konkrete Handlung wird als § 87b UrhG-Verletzung behauptet — ist sie tatsächlich erfolgt?
3. Unterlassungserklärung analysieren: Ist sie hinreichend bestimmt, zeitlich unbegrenzt, enthält sie eine angemessene Vertragsstrafe (§ 339 BGB)?
4. Verjährung prüfen: § 102 UrhG — ist der behauptete Verletzungszeitraum verjährt (3-Jahres-Frist)?
5. Schranken prüfen: Greift § 87c UrhG (erlaubte Handlungen), § 44b UrhG (TDM-Schranke) oder vertragliche Erlaubnis — liegt tatsächlich eine Verletzung vor?
6. Handlungsoptionen abwägen: Unterzeichnung, modifizierte Unterlassungserklärung, Widerspruch, Schutzschrift vor dem zuständigen Gericht.

## Rechtsrahmen

- § 87a Abs. 2 UrhG: Herstellereigenschaft des Abmahnenden — muss er Inhaber des Rechts sein?
- § 87b UrhG: Verletzungstatbestand — ist eine Entnahme wesentlicher Teile tatsächlich nachweisbar?
- § 87c UrhG: Erlaubte Handlungen als Einwand gegen Abmahnung (z. B. TDM-Schranke, rechtmäßige Nutzung).
- § 97a Abs. 4 UrhG: Kostenerstattung bei unberechtigter Abmahnung — Gegenanspruch des Abgemahnten.
- § 102 UrhG: Verjährung — 3 Jahre ab Kenntnis von Verletzung und Verletzer.
- § 339 BGB: Vertragsstrafe in der Unterlassungserklärung — Höhe auf Verhältnismäßigkeit prüfen.

## Prüfraster

- Ist der Abmahnende tatsächlich Inhaber des behaupteten Datenbankherstellerrechts (§ 87a Abs. 2 UrhG)?
- Liegt die behauptete Verletzungshandlung tatsächlich vor — welche Belege legt der Abmahnende vor?
- Greift eine Schranke (§ 87c UrhG, § 44b UrhG) oder liegt eine vertragliche Erlaubnis vor?
- Ist der behauptete Verletzungszeitraum verjährt (§ 102 UrhG)?
- Ist die geforderte Unterlassungserklärung zu weit gefasst — schließt sie erlaubte Nutzungen ein?
- Ist die Vertragsstrafe angemessen, oder ist sie übermäßig hoch — § 340 BGB-Herabsetzung möglich?
- Wurde die Abmahnung fristgerecht und formwirksam erteilt — greift § 97a Abs. 4 UrhG bei unberechtigter Abmahnung?

## Typische Fallstricke

- Versäumte Frist zur Abgabe der Unterlassungserklärung erzeugt keine automatische Rechtsverwirkung — aber erhöht Risiko einer einstweiligen Verfügung.
- Zu schnelles Unterzeichnen einer zu weit gefassten Unterlassungserklärung schränkt künftige erlaubte Aktivitäten ein.
- Abmahnender ohne Herstellerrecht (z. B. nur Lizenznehmer, nicht Hersteller) ist nicht abmahnberechtigt.
- Schutzschrift beim vermuteten Gericht einreichen, bevor die einstweilige Verfügung beantragt wird — Gericht muss sie berücksichtigen.
- TDM-Schranke (§ 44b UrhG) kann als Einwand gegen den Verletzungsvorwurf wirken — wurde Opt-out wirksam erklärt?

## Quellen

- [§ 97a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 102 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/102.html)
- [§ 339 BGB — dejure.org](https://dejure.org/gesetze/BGB/339.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 87a UrhG
- § 87b UrhG
- § 87a-87e UrhG
- § 44b UrhG
- § 4 UrhG
- § 60d UrhG
- § 97 UrhG
- § 87c UrhG
- § 87d UrhG
- § 97a UrhG
- § 202a StGB
- § 5 UrhG

### Leitentscheidungen

- EuGH C-203/02
- EuGH C-202/12
- EuGH C-545/07
- EuGH C-338/02
- EuGH C-170/12

---

## Skill: `agb-auskunft-rechnungslegung`

_Gestaltung und Prüfung datenbankrechtsrelevanter AGB-Klauseln: § 307 BGB-Inhaltskontrolle für Nutzungsverbote, Scraping-Verbote, Datenbankrechts-Zuweisung, Haftungsausschlüsse und TDM-Opt-out-Klauseln. Analysiert Wirksamkeit von Standardklauseln gegenüber Verbrauchern und B2B-Kunden sowie Schrank..._

# Datenbankrecht in AGB-Klauseln — Inhaltskontrolle und Gestaltung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber überarbeitet seine AGB und will datenbankrechtsrelevante Klauseln (Nutzungsverbote, Scraping-Verbot, TDM-Opt-out) rechtssicher formulieren.
- Anwalt soll bestehende AGB eines SaaS-Anbieters auf unwirksame Klauseln prüfen, die alle Datenbankrechte auf den Anbieter übertragen.
- Startup hat eine Abmahnung erhalten, weil seine AGB keine ausreichenden Scraping-Verbote enthalten, und muss sie überarbeiten.

## Erste Schritte

1. AGB-Anwendungsbereich bestimmen: Handelt es sich um B2C oder B2B-Verhältnis? Unterschiedliche Prüfmaßstäbe nach §§ 307-309 BGB vs. § 310 BGB.
2. Inhaltskontrolle nach § 307 BGB: Sind die Klauseln transparent (Verständlichkeitsgebot), klar und nicht unangemessen benachteiligend?
3. Scraping-Verbot-Klausel prüfen: Hinreichend bestimmt (welche automatisierten Zugriffe sind verboten?), verhältnismäßige Rechtsfolgen (Kündigung, Schadensersatz)?
4. TDM-Opt-out in AGB bewerten: Maschinenlesbarkeit nach § 44b Abs. 3 UrhG — AGB-Text allein reicht nicht; zusätzliche technische Erklärung erforderlich.
5. Datenbankrechts-Zuweisungsklausel prüfen: Überträgt die Klausel Herstellerrecht oder Nutzungsrechte an Kundendaten auf den Betreiber — § 307 BGB-Konformität?
6. Haftungsausschlussklausel gestalten: § 309 Nr. 7 BGB — Ausschluss für Vorsatz und grobe Fahrlässigkeit unzulässig; differenzierte Haftungsbegrenzung erforderlich.

## Rechtsrahmen

- § 307 BGB: Inhaltskontrolle — Klausel unwirksam bei unangemessener Benachteiligung oder fehlender Transparenz.
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit — z. B. einseitige Änderungsvorbehalte.
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit — Haftungsausschlüsse, Abtretungsverbote.
- § 87c UrhG: Zwingende gesetzliche Schranken — vertraglich nicht ausschließbar für rechtmäßige Nutzer.
- § 44b UrhG: TDM-Schranke — kommerzielles TDM kann durch AGB (mit technischem Opt-out) ausgeschlossen werden; wissenschaftliches nicht.
- § 87b UrhG: Verbotener Handlungsrahmen — AGB können Nutzung über das gesetzliche Verbot hinaus einschränken, müssen aber § 307 BGB standhalten.

## Prüfraster

- Sind alle datenbankrechtsrelevanten Verbote (Entnahme, Scraping, Weiterverwendung) in den AGB klar und abschließend formuliert?
- Ist das Scraping-Verbot hinreichend bestimmt — welche Arten automatisierten Zugriffs sind erfasst und welche Rechtsfolgen gelten?
- Hält die TDM-Opt-out-Klausel den Anforderungen des § 44b Abs. 3 UrhG stand (maschinenlesbar + separat technisch erklärt)?
- Sind Klauseln, die Datenbankherstellerrecht auf den Anbieter übertragen, nach § 307 BGB angemessen und transparent?
- Greifen zwingende Schranken (§ 87c UrhG) einem Verbotsumfang entgegen — Klausel insoweit unwirksam?
- Unterscheiden die Haftungsklauseln zwischen Vorsatz, grober und leichter Fahrlässigkeit — § 309 Nr. 7 BGB beachten?
- Gibt es einen wirksamen Gerichtsstand und anwendbares Recht in den AGB für grenzüberschreitende Datenbanknutzung?

## Typische Fallstricke

- Zu pauschale Scraping-Verbote, die auch zulässige Nutzungen einschließen, sind nach § 307 BGB unwirksam.
- AGB-TDM-Verbote ohne zusätzliche maschinenlesbare Opt-out-Erklärung wirken nicht als § 44b Abs. 3 UrhG-Opt-out.
- Klauseln, die dem Betreiber alle Rechte an Kundendaten zuweisen, sind in der Regel nach § 307 BGB unangemessen.
- Einseitige Leistungsänderungsvorbehalte des Betreibers (§ 308 Nr. 4 BGB) für Datenbankzugang sind begrenzt zulässig.
- Verbraucher-AGB unterliegen strengerer Kontrolle als B2B-AGB — für B2C immer zusätzlich §§ 308-309 BGB prüfen.

## Quellen

- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 309 BGB — dejure.org](https://dejure.org/gesetze/BGB/309.html)
- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 308 BGB — dejure.org](https://dejure.org/gesetze/BGB/308.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 87a UrhG
- § 87b UrhG
- § 87a-87e UrhG
- § 44b UrhG
- § 4 UrhG
- § 60d UrhG
- § 97 UrhG
- § 87c UrhG
- § 87d UrhG
- § 97a UrhG
- § 202a StGB
- § 5 UrhG

### Leitentscheidungen

- EuGH C-203/02
- EuGH C-202/12
- EuGH C-545/07
- EuGH C-338/02
- EuGH C-170/12

---

## Skill: `agrar-logistik-cyberincident`

_Datenbankrecht für Agrar- und Sensordaten: §§ 87a-87e UrhG für Präzisionslandwirtschaftsdatenbanken und IoT-Sensornetzwerke, Data Act (VO 2023/2854) Zugangsrechte für Landwirte, Verhältnis zu Geschäftsgeheimnissen (GeschGehG) bei Erntedaten und DSGVO-Anforderungen bei personenbezogenen Agrardaten..._

# Datenbankrecht für Agrar- und Sensordaten — Präzisionslandwirtschaft und IoT

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- AgTech-Unternehmen hat eine Bodenanalysedatenbank aus Sensordaten von 500 Betrieben aufgebaut und fragt, ob es Datenbankherstellerrecht hat und wie es die Daten lizenzieren kann.
- Landwirt möchte alle Sensordaten seines Smart-Farm-Equipments von einem AgTech-Anbieter zurückbekommen — Data-Act-Zugangsrecht prüfen.
- Saatgutunternehmen kauft von mehreren AgTech-Anbietern Ertragsdaten für KI-Modell-Training und fragt nach Datenbankrecht und TDM-Schranken.

## Erste Schritte

1. Datenbankherstellerrecht für Agrardatenbank: Wesentliche Investition in Sensorinfrastruktur, Datenqualitätsprüfung und Darstellung (§ 87a UrhG)?
2. BHB-Doktrin für Sensordaten: Sind die Sensordaten selbst erzeugte Daten (Messung der eigenen Felder) oder beschaffte Daten — Investitionstyp bestimmen.
3. Data Act für Landwirte: VO 2023/2854 Art. 4 — Landwirt als Nutzer des Smart-Farm-Equipments hat Zugangsrecht zu von seinem Gerät generierten Daten.
4. Geschäftsgeheimnisse bei Erntedaten: Agrardaten können Betriebsgeheimnisse sein — GeschGehG und Geheimhaltungsmaßnahmen.
5. TDM-Schranke für Saatgutunternehmen: § 44b UrhG — ist die Nutzung für KI-Modell-Training TDM-berechtigt, oder wurde Opt-out erklärt?
6. DSGVO bei personenbezogenen Agrardaten: Können Agrardaten (GPS-Positionsdaten von Landmaschinen) personenbezogen sein?

## Rechtsrahmen

- § 87a UrhG: AgTech-Datenbankherstellerrecht — Investition in Sensordaten-Beschaffung (Betriebsführung der Sensoren), Qualitätsprüfung und Darstellung.
- Data Act VO 2023/2854 Art. 4: Zugangsrecht des Landwirts zu Daten seines Smart-Farm-Equipments.
- GeschGehG § 2 Nr. 1: Ernte- und Ertragsdaten als Betriebsgeheimnisse — wenn angemessene Geheimhaltungsmaßnahmen.
- § 44b UrhG: TDM-Schranke für Saatgutunternehmen — kommerzielle Nutzung, Opt-out relevant.
- DSGVO Art. 4 Nr. 1: GPS-Standortdaten von Landmaschinen können personenbezogene Daten sein, wenn Betriebsinhaber identifizierbar.
- EuGH C-203/02 (BHB/William Hill): Sensorisches Messen von eigenen Feldern ist Datenerzeugung, nicht Datenbeschaffung — BHB-Einwand möglich.

## Prüfraster

- Beruht das AgTech-Herstellerrecht auf Investition in Sensordaten-Beschaffung von Dritten oder auf eigener Messung (BHB-Einwand)?
- Hat der Landwirt nach Data Act Art. 4 ein Zugangsrecht zu seinen Gerätedaten beim AgTech-Anbieter?
- Sind Erntedaten als Betriebsgeheimnisse schützenswert — wurden angemessene Geheimhaltungsmaßnahmen ergriffen?
- Hat der AgTech-Anbieter einen TDM-Opt-out nach § 44b Abs. 3 UrhG erklärt?
- Können GPS-Positionsdaten der Landmaschinen personenbezogene Daten nach DSGVO sein?
- Erlauben Lizenzbedingungen die Nutzung aggregierter Agrardaten für Saatgut-KI-Modell-Training?
- Schützt das Data Act Art. 4 Zugangsrecht den Landwirt auch gegen Einwände aus dem Geschäftsgeheimnisrecht des Anbieters?

## Typische Fallstricke

- AgTech-Anbieter, die Daten von den eigenen Sensoren auf Kundenfeldern sammeln, investieren in Datenerzeugung — BHB-Einwand greift.
- Data Act gibt dem Landwirt Zugangsrecht, hebt aber AgTech-Datenbankherstellerrecht an der Gesamtdatenbank nicht auf.
- Agrardaten aggregierter Betriebe können trotz Einzelanonymisierung in der Kombination re-identifizierbar sein.
- Geschäftsgeheimnisschutz für Erntedaten setzt angemessene Maßnahmen voraus — fehlende NDA oder offene API schwächt den Schutz.
- TDM-Schranke schützt den Saatgut-KI-Anbieter nur, wenn kein wirksamer Opt-out erklärt wurde.

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)
- [§ 44b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/44b.html)
- [EuGH C-203/02 BHB/William Hill — Curia](https://curia.europa.eu/juris/liste.jsf?num=C-203/02)
- [DSGVO Art. 4 — dejure.org](https://dejure.org/gesetze/DSGVO/4.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 87a UrhG
- § 87b UrhG
- § 87a-87e UrhG
- § 44b UrhG
- § 4 UrhG
- § 60d UrhG
- § 97 UrhG
- § 87c UrhG
- § 87d UrhG
- § 97a UrhG
- § 202a StGB
- § 5 UrhG

### Leitentscheidungen

- EuGH C-203/02
- EuGH C-202/12
- EuGH C-545/07
- EuGH C-338/02
- EuGH C-170/12

---

## Skill: `api-nutzung-rate-limits-und-vertragsbruch`

_Prüft die rechtliche Bewertung von API-Nutzung im Datenbankkontext: Vertragsbruch bei Überschreitung von Rate-Limits oder Nutzungsbedingungen, Verhältnis zu §§ 87a-87e UrhG, Schadensersatz bei unerlaubter Massenabfrage sowie Gestaltung wirksamer API-Nutzungsbedingungen. Bewertet Kündigungsrecht u..._

# API-Nutzung, Rate-Limits und Vertragsbruch im Datenbankrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- SaaS-Anbieter stellt fest, dass ein Geschäftskunde über seine API weit mehr Abfragen tätigt als vertraglich erlaubt, und will Schadenersatz und Kündigung prüfen.
- Startup hat eine API-Schnittstelle zu einer Fremddatenbank genutzt und überschreitet unbewusst die Rate-Limits — die Gegenseite droht mit Abmahnung.
- Unternehmen entwirft neue API-Nutzungsbedingungen und will sicherstellen, dass diese das Datenbankherstellerrecht wirksam ergänzen.

## Erste Schritte

1. Vertragliche Grundlage klären: API-Nutzungsvertrag, AGB, Developer-Agreement — welche Rate-Limits und Nutzungszwecke sind vereinbart?
2. Vertragsbruch bewerten: Überschreitung der Abfragelimits, unerlaubte Weiterverwendung, Verstoß gegen Zweckbindung — § 280 BGB, § 241 Abs. 2 BGB.
3. Urheberrechtliche Parallelprüfung: Erfüllt die Abfrageintensität den Tatbestand der wesentlichen Entnahme nach § 87b UrhG unabhängig vom Vertrag?
4. Kündigung und Sperre prüfen: Außerordentliche Kündigung (§ 314 BGB) bei schwerwiegendem Vertragsbruch; technische Sperre als berechtigte Maßnahme.
5. Schadensersatz berechnen: Überschussabfragen nach Lizenzanalogie bewerten; Nutzungsausfallschaden des Betreibers.
6. AGB-Wirksamkeit prüfen: Rate-Limit-Klauseln nach § 307 BGB; transparente Formulierung und klar definierte Folgen.

## Rechtsrahmen

- § 280 Abs. 1 BGB: Schadensersatz bei Pflichtverletzung aus dem Schuldverhältnis.
- § 314 BGB: Kündigung von Dauerschuldverhältnissen aus wichtigem Grund bei schwerwiegendem Vertragsbruch.
- § 307 BGB: AGB-Kontrolle — Rate-Limit-Klauseln müssen klar, verständlich und nicht unangemessen benachteiligend sein.
- § 87b UrhG: Urheberrechtlicher Anspruch neben dem Vertragsanspruch bei wesentlicher Entnahme.
- § 97 UrhG: Unterlassung und Schadensersatz bei Urheberrechtsverletzung — Lizenzanalogie als Berechnungsmethode.
- § 97a UrhG: Abmahnung als Voraussetzung für Erstattung von Rechtsanwaltsgebühren.

## Prüfraster

- Liegt ein wirksamer API-Nutzungsvertrag vor, und was regelt er zu Abfragevolumen, Zweck und Weiterverwendung?
- Überschreiten die tatsächlichen Abfragen die vertraglich vereinbarten Rate-Limits messbar?
- Sind die Rate-Limits technisch nachweisbar (Server-Logs, API-Gateway-Protokolle)?
- Erfüllen die Abfragen unabhängig vom Vertrag den urheberrechtlichen Verletzungstatbestand (§ 87b UrhG)?
- Hat der Betreiber vor der Kündigung abgemahnt oder eine Frist zur Abhilfe gesetzt (§ 314 Abs. 2 BGB)?
- Sind Rate-Limit-Klauseln in AGB nach § 307 BGB wirksam — sind Schwellenwerte und Rechtsfolgen transparent?
- Kann der Schaden nach Lizenzanalogie (übliche API-Lizenzgebühr) berechnet werden?

## Typische Fallstricke

- Rate-Limits ohne klare Rechtsfolge in den AGB lassen offen, ob Überschreitung Vertragsbruch oder nur technische Einschränkung ist.
- Urheberrechtliche Ansprüche laufen auch ohne Vertragsverletzung — der Betreiber kann beide Ansprüche nebeneinander geltend machen.
- Kündigung ohne vorherige Abmahnung bei erstmaligem Verstoß ist oft unwirksam (§ 314 Abs. 2 BGB).
- Technische Sperren ohne vorherige Abmahnung können ihrerseits Vertragsbruch des Betreibers darstellen (§ 280 BGB).
- Entwickler-Teams überschreiten Rate-Limits oft versehentlich — culpa levis reicht aber für vertraglichen Schadensersatzanspruch.

## Output

- Vertragsbruchanalyse mit Anspruchsübersicht (§ 280 BGB / § 97 UrhG)
- Rate-Limit-Klausel-Vorlage für wirksame AGB-Gestaltung
- Abmahnschreiben bei API-Missbrauch
- Schadensberechnung nach Lizenzanalogie
- Kündigung aus wichtigem Grund — Musterformulierung (§ 314 BGB)

## Quellen

- [§ 280 BGB — dejure.org](https://dejure.org/gesetze/BGB/280.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 87a UrhG
- § 87b UrhG
- § 87a-87e UrhG
- § 44b UrhG
- § 4 UrhG
- § 60d UrhG
- § 97 UrhG
- § 87c UrhG
- § 87d UrhG
- § 97a UrhG
- § 202a StGB
- § 5 UrhG

### Leitentscheidungen

- EuGH C-203/02
- EuGH C-202/12
- EuGH C-545/07
- EuGH C-338/02
- EuGH C-170/12

---

## Skill: `auskunft-rechnungslegung-schadensschaetzung`

_Auskunft, Rechnungslegung und Schadensschätzung im Datenbankrecht nach §§ 97 101 UrhG: Dreigliedrige Schadensberechnung (konkreter Schaden, Herausgabe Verletzergewinn, Lizenzanalogie), Auskunftsanspruch gegen Verletzer und ISP, Rechnungslegungsvollstreckung sowie Besonderheiten bei Datenbankschut..._

# Auskunft, Rechnungslegung und Schadensschätzung im Datenbankrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber hat eine einstweilige Verfügung erwirkt und will nun im Hauptsacheverfahren Schadensersatz geltend machen — Auskunftsanspruch und Schadensberechnung sind unklar.
- Verletzer hat Datenbankdaten für eigene kommerzielle Produkte genutzt — wie hoch ist der Schaden und welche Berechnungsmethode gilt?
- Anwalt muss den Auskunftsanspruch gegen einen unbekannten Scraper über den Internetdienstanbieter nach § 101 UrhG geltend machen.

## Erste Schritte

1. Auskunftsanspruch formulieren: § 101 UrhG gegen Verletzer — Umfang der Verletzung (Zeit, Volumen, Empfänger), Lieferkette der entnommenen Daten, Erlöse.
2. Auskunft gegen ISP prüfen: § 101 Abs. 2 UrhG gegen Internetdienstanbieter — Voraussetzung: gewerbliche Verletzung, Antrag bei Gericht erforderlich.
3. Schadensberechnungsmethode wählen: Konkreter Schaden, Herausgabe des Verletzergewinns oder Lizenzanalogie (§ 97 Abs. 2 UrhG) — welche Methode maximiert den Anspruch?
4. Lizenzanalogie berechnen: Übliche Lizenzgebühr für die entnommenen Datenbankteile ermitteln (Marktvergleich, eigene Lizenzpraxis).
5. Rechnungslegung vollstrecken: Wenn Verletzer Auskunft verweigert — Zwangsvollstreckung nach § 888 ZPO, Ordnungsgeld.
6. Verjährung prüfen: § 102 UrhG i.V.m. §§ 195-199 BGB — 3 Jahre ab Kenntnis, 10 Jahre Höchstfrist.

## Rechtsrahmen

- § 97 Abs. 1 UrhG: Unterlassung und Schadensersatz bei Datenbankrechts-Verletzung.
- § 97 Abs. 2 UrhG: Drei Berechnungsmethoden — konkreter Schaden, Verletzergewinnherausgabe, Lizenzanalogie.
- § 101 UrhG: Auskunftsanspruch gegen Verletzer und (bei gewerblicher Verletzung) gegen ISP.
- § 102 UrhG: Verjährung der Schadensersatzansprüche — 3 Jahre ab Kenntnis.
- § 888 ZPO: Erzwingung nicht vertretbarer Handlungen (Rechnungslegung) durch Ordnungsgeld.
- § 87b UrhG: Verletzungstatbestand als Grundlage aller Folgeansprüche.

## Prüfraster

- Liegt eine Verletzung nach § 87b UrhG als Grundlage des Schadensersatzes vor?
- Ist der Verletzer bekannt, oder muss der ISP-Auskunftsweg nach § 101 Abs. 2 UrhG beschritten werden?
- Welche der drei Berechnungsmethoden (§ 97 Abs. 2 UrhG) führt zu maximalem oder realistischstem Ergebnis?
- Lässt sich eine übliche Lizenzgebühr (Lizenzanalogie) aus eigenen Verträgen oder Marktvergleichen ableiten?
- Hat der Verletzer Gewinne aus der Nutzung der entnommenen Daten erzielt, die herausgegeben werden müssen?
- Ist die Verjährungsfrist nach § 102 UrhG noch offen — wann hatte der Gläubiger Kenntnis?
- Wann wurde Auskunft verlangt und noch nicht erfüllt — Rechnungslegungs-Klage und Vollstreckung planen?

## Typische Fallstricke

- Lizenzanalogie erfordert Nachweis einer „üblichen" Lizenzgebühr — ohne eigene Lizenzpraxis schwer zu begründen.
- ISP-Auskunft nach § 101 Abs. 2 UrhG setzt gewerbliche Verletzung voraus — private Nutzung scheidet aus.
- Verletzergewinnherausgabe ist oft schwer durchsetzbar, weil Verletzer keine separate Buchführung für Datenbanknutzung hat.
- Schadensberechnung ohne Sachverständigengutachten zu Datenbankwert und Lizenzüblichkeit wird von Gerichten oft gekürzt.
- Verjährung beginnt mit Kenntnis — nicht mit Entdeckung des vollen Schadensumfangs. Frühzeitige Klageerhebung oder Hemmung.

## Output

- Schadensberechnungsmatrix (alle drei Methoden nach § 97 Abs. 2 UrhG)
- Auskunftsklage-Muster gegen Verletzer (§ 101 UrhG)
- ISP-Auskunftsantrag nach § 101 Abs. 2 UrhG (gerichtlich)
- Lizenzanalogie-Berechnungsnachweis (Marktvergleich)
- Verjährungsprüfungsprotokoll mit Fristberechnung

## Quellen

- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 101 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/101.html)
- [§ 102 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/102.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 888 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/888.html)
- [§§ 195-199 BGB — dejure.org](https://dejure.org/gesetze/BGB/195.html)

---

## Skill: `b2b-kundendaten-datenbank-insolvenz-als`

_Analysiert Datenbankherstellerrecht (§§ 87a-87e UrhG) und GeschGehG bei CRM-Datenbankexporten durch ausscheidende Mitarbeiter: Verletzungstatbestände, arbeitsrechtliche Sanktionen, einstweilige Verfügung sowie DSGVO-Pflichten bei unrechtmäßiger Datenweitergabe. Erstellt Präventionskonzept mit tec..._

# B2B-Kundendaten und CRM-Export durch Mitarbeiter — Datenbankrecht und Arbeitsrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Vertriebsmitarbeiter verlässt das Unternehmen und nimmt dabei die vollständige CRM-Kundendatenbank auf einem USB-Stick mit zum Wettbewerber.
- Unternehmen fragt, welche Ansprüche gegen den ausgeschiedenen Mitarbeiter und den aufnehmenden Wettbewerber bestehen.
- Arbeitgeber will präventiv sicherstellen, dass CRM-Exporte technisch verhindert und vertraglich verboten werden.

## Erste Schritte

1. Datenbankherstellerrecht prüfen: Hat das Unternehmen eine wesentliche Investition in seine CRM-Kundendatenbank (Beschaffung, Überprüfung, Darstellung der Kundendaten) getätigt?
2. Geschäftsgeheimnisschutz prüfen: Sind die Kundendaten als Geschäftsgeheimnis nach § 2 Nr. 1 GeschGehG geschützt — geheim, wertvoll, Geheimhaltungsmaßnahmen vorhanden?
3. Verletzungshandlung bestimmen: § 87b UrhG (Entnahme wesentlicher Teile), § 4 GeschGehG (rechtswidrige Erlangung und Nutzung), Arbeitsvertragsverletzung.
4. Ansprüche gegen Mitarbeiter und Wettbewerber formulieren: Unterlassung, Herausgabe, Schadensersatz, Auskunft.
5. Einstweilige Verfügung prüfen: Dringlichkeit bejaht bei aktueller Verwendung beim Wettbewerber — Verfügungsanspruch und Verfügungsgrund.
6. DSGVO-Pflichten klären: Datenpanne nach Art. 33-34 DSGVO melden — wenn personenbezogene Kundendaten betroffen.

## Rechtsrahmen

- § 87a UrhG: CRM-Datenbank als Datenbank mit wesentlicher Investition in Kundendatenbeschaffung und -pflege.
- § 87b UrhG: Entnahme wesentlicher Teile durch den Mitarbeiter als Verletzung des Herstellerrechts.
- § 2 Nr. 1 GeschGehG: Kundendaten als Geschäftsgeheimnis, wenn nicht allgemein bekannt, wirtschaftlich wertvoll und angemessen geheim gehalten.
- § 4 GeschGehG: Verbotene Handlungen — rechtswidrige Erlangung, Nutzung und Offenlegung.
- Art. 33-34 DSGVO: Meldepflicht bei Datenpannen an Aufsichtsbehörde und betroffene Kunden.
- § 241 Abs. 2 BGB: Nebenpflicht des Arbeitnehmers zur Rücksicht auf Arbeitgeberinteressen — verletzt durch CRM-Export.

## Prüfraster

- Hat das Unternehmen angemessene Geheimhaltungsmaßnahmen für die CRM-Datenbank ergriffen (Zugangsbeschränkungen, NDA, Löschpflicht bei Ausscheiden)?
- Enthält der Arbeitsvertrag explizite Verbote zur Mitnahme von Kundendaten bei Ausscheiden?
- Weist die exportierte Datenmenge auf eine Entnahme wesentlicher Teile hin (§ 87b UrhG)?
- Verwendet der Wettbewerber die Daten bereits aktiv — besteht Dringlichkeit für einstweilige Verfügung?
- Sind personenbezogene Kundendaten betroffen — ist eine Datenpannen-Meldung nach Art. 33 DSGVO erforderlich?
- Kann technisch nachgewiesen werden, dass ein Export stattgefunden hat (USB-Logs, E-Mail-Forensik, Zugriffsprotokoll)?
- Ist der aufnehmende Wettbewerber gutgläubig oder wusste er von der rechtswidrigen Herkunft der Daten?

## Typische Fallstricke

- Fehlende technische Sperren (kein USB-Block, kein Export-Verbot im CRM) schwächen die Position im GeschGehG-Prozess erheblich.
- Ohne DSGVO-Datenpannen-Meldung droht zusätzliches Bußgeld durch die Datenschutzbehörde.
- Ansprüche gegen den Wettbewerber setzen Kenntnis oder fahrlässige Unkenntnis von der unrechtmäßigen Herkunft voraus.
- Arbeitsrechtliche Abmahnung und außerordentliche Kündigung müssen zeitnah erfolgen — keine Verwirkung.
- Berechnung des Schadens ist komplex: entgangene Aufträge, Lizenzanalogie oder pauschaler Schadensersatz nach § 97 Abs. 2 UrhG.

## Quellen

- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [§ 4 GeschGehG — dejure.org](https://dejure.org/gesetze/GeschGehG/4.html)
- [Art. 33 DSGVO — dejure.org](https://dejure.org/gesetze/DSGVO/33.html)
- [§ 241 BGB — dejure.org](https://dejure.org/gesetze/BGB/241.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [GeschGehG — gesetze-im-internet.de](https://www.gesetze-im-internet.de/geschgehg/index.html)

---

## Skill: `backup-export-und-vendor-lock`

_Datenbankrecht bei Backup-Rechten, Datenexport und Vendor-Lock-in: § 87c UrhG erlaubte Entnahmen für rechtmäßige Nutzer, vertragliche Backup-Klauseln, Data Act Art. 17 Wechselrecht, Exportformat-Anforderungen und rechtliche Mittel gegen Lock-in-Strategien. Bewertet AGB-Wirksamkeit von Export-Verb..._

# Backup, Export und Vendor-Lock-in — Datenbankrecht und Datenmitnahme

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Unternehmen hat entdeckt, dass sein Datenbankdienstleister in den AGB den Export der Daten in maschinenlesbarer Form ausschließt — ist das wirksam?
- SaaS-Anbieter verlangt nach Vertragsende eine hohe Gebühr für den Datenexport — darf er das und was sind die rechtlichen Mittel dagegen?
- IT-Leiter fragt, welche Vertragsklauseln beim Abschluss eines neuen Datenbankvertrags verhindern, dass das Unternehmen an einen Anbieter gebunden bleibt.

## Erste Schritte

1. Backup-Recht nach § 87c UrhG prüfen: Erlaubte Handlungen für rechtmäßige Datenbanknutzer — ist eine Sicherungskopie zulässig?
2. Vertragliche Export-Klausel analysieren: Verbietet die AGB den Datenexport — ist das Verbot nach § 307 BGB angemessen?
3. Data Act Art. 17 anwenden: Wechselrecht ab September 2025 — Anbieter müssen Datenmigration ohne unverhältnismäßige Hürden ermöglichen.
4. Exportformat-Standard prüfen: Offenes, maschinenlesbares Format erforderlich — proprietäre Formate können Lock-in begründen.
5. Gebühr für Export bewerten: Angemessene Gebühr nach Data Act Art. 17 zulässig, aber unverhältnismäßige Exportgebühren sind verboten.
6. Vertragsgestaltung für neuen Datenbankvertrag: Exit-Klausel mit Exportpflicht, Format-Anforderungen, Löschpflicht nach Herausgabe.

## Rechtsrahmen

- § 87c UrhG: Erlaubte Handlungen — rechtmäßige Nutzer dürfen Teile einer Datenbank für zulässige Zwecke nutzen; Sicherungskopie analog.
- § 307 BGB: AGB-Wirksamkeit von Export-Verboten — totalem Datenexport-Verbot widerspricht berechtigtem Interesse des Nutzers.
- Data Act VO 2023/2854 Art. 17: Wechselrecht — keine unverhältnismäßigen technischen oder wirtschaftlichen Hürden bei Anbieterwechsel.
- DSGVO Art. 20: Datenportabilität — gilt für personenbezogene Verbraucherdaten; kostenloses, strukturiertes Format.
- § 314 BGB: Außerordentliche Kündigung bei Verweigerung des Datenexports als wesentlicher Vertragspflicht.
- § 93 UrhG analog: Schutz gegen wesentliche Änderungen oder Vernichtung des Datenbankwerks.

## Prüfraster

- Schließen AGB den Datenexport vollständig aus — ist das nach § 307 BGB unverhältnismäßig benachteiligend?
- Besteht nach Data Act Art. 17 ein gesetzliches Wechselrecht — gilt die VO für den betreffenden Dienst?
- Hat der Nutzer ein Recht auf Backup nach § 87c UrhG oder vertraglich?
- Verlangt der Anbieter für den Export eine unangemessene Gebühr (> echte Kosten)?
- Stellt der Anbieter Daten in einem offenen Format bereit oder bindet er durch proprietäre Formate?
- Enthält der bestehende Vertrag eine Exit-Klausel mit Exportpflicht, und ist diese vollstreckbar?
- Umfasst der Export auch Metadaten, Konfigurationsdaten und Datenbankstruktur — oder nur Rohdaten?

## Typische Fallstricke

- AGB-Klauseln, die Datenexport gegen Entgelt erlauben, aber mit unangemessenen Gebühren belasten, sind nach § 307 BGB anfechtbar.
- Data Act Art. 17 Wechselrecht gilt erst ab September 2025 — für bestehende Verträge muss vertragliche Grundlage geprüft werden.
- Proprietäre Exportformate können faktisch den Datenwechsel verhindern, obwohl rechtlich ein Herausgabeanspruch besteht.
- Backup von Datenbankstrukturen ohne Genehmigung kann Herstellerrecht verletzen, wenn keine vertragliche Erlaubnis oder § 87c-Schranke eingreift.
- Löschpflicht nach Export — der alte Anbieter hat kein Recht, eine Kopie der Kundendaten nach Herausgabe zu behalten.

## Quellen

- [§ 87c UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87c.html)
- [§ 307 BGB — dejure.org](https://dejure.org/gesetze/BGB/307.html)
- [Data Act VO 2023/2854 — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R2854)
- [DSGVO Art. 20 — dejure.org](https://dejure.org/gesetze/DSGVO/20.html)
- [§ 314 BGB — dejure.org](https://dejure.org/gesetze/BGB/314.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)

---

## Skill: `beweissicherung-durch-testcrawler`

_Rechtssichere Beweissicherung durch Testcrawler bei Datenbankrechts-Verletzungen: Aufbau und Betrieb eines eigenen Testcrawlers zur Verletzungsdokumentation, Verwertbarkeit der Ergebnisse als Beweismittel, notarielle Begleitung und Verhältnis zu § 202a StGB und DSGVO. Erstellt Testcrawler-Protoko..._

# Beweissicherung durch Testcrawler — Zulässigkeit und Verwertbarkeit

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber will einen eigenen Testcrawler einsetzen, der die Verletzungen eines Wettbewerbers dokumentiert — ist das rechtlich zulässig?
- Anwalt fragt, ob durch einen Testcrawler gewonnene Beweise im Datenbankrechts-Prozess vor dem LG Hamburg verwertbar sind.
- IT-Abteilung soll einen Testcrawler entwickeln, der regelmäßig Wettbewerber-Websites auf Datenbankübereinstimmungen prüft.

## Erste Schritte

1. Zulässigkeit des Testcrawlers prüfen: Ist das Crawlen der Wettbewerber-Website erlaubt — AGB-Bindung, robots.txt, § 202a StGB bei Zugangssicherungen?
2. Beweisziel definieren: Was soll der Testcrawler nachweisen — Übernahme eigener Datenbankeinträge, systematische Entnahme, Honey-Pot-Treffer?
3. Testcrawler-Protokoll aufsetzen: Zeitstempel, Hashwerte der abgerufenen Daten, Vergleich mit eigener Datenbank, Abrufvolumen und Herkunft.
4. Notarielle oder technische Zertifizierung: Einsatz eines qualifizierten Zeitstempels (eIDAS-VO) oder notarielle Protokollierung des Crawling-Vorgangs.
5. Honey-Pot-Vergleich integrieren: Wenn eigene Datenbank Honey-Pot-Einträge enthält, können diese bei Wettbewerber nachgewiesen werden.
6. Verwertbarkeit im Prozess sichern: § 286 ZPO — technische Protokolle als Augenscheinsbeweis; Sachverständigen-Gutachten über die Vergleichsmethodik.

## Rechtsrahmen

- § 286 ZPO: Freie Beweiswürdigung — technische Protokolle und Crawl-Ergebnisse als Augenscheinsbeweis verwertbar.
- § 202a StGB: Ausspähen von Daten — Testcrawler darf keine Zugangssicherungen (Passwort, CAPTCHA, technische Sperre) überwinden.
- § 1 UWG: Unlautere Mittel — Testcrawler ohne Täuschung ist kein UWG-Verstoß, wenn nur öffentlich zugängliche Daten abgerufen werden.
- DSGVO Art. 6: Personenbezogene Daten — Testcrawler darf keine personenbezogenen Daten ohne Rechtsgrundlage erheben.
- eIDAS-VO Art. 41: Qualifizierter elektronischer Zeitstempel für Nachweis des Abrufzeitpunkts.
- § 87b UrhG: Verletzungstatbestand als Beweisziel — Testcrawler dokumentiert Entnahme von Teilen der eigenen Datenbank.

## Prüfraster

- Ist die Zielwebsite öffentlich zugänglich ohne Zugangssicherung (kein Login, kein CAPTCHA, keine technische Blockade)?
- Verletzt der Testcrawler die AGB der Zielwebsite — kann der Betreiber des Testcrawlers deshalb haftbar werden?
- Ist § 202a StGB ausgeschlossen — werden keine Zugangssicherungen überwunden?
- Enthält das Crawl-Protokoll alle für die Beweiswürdigung erforderlichen Daten (Zeitstempel, URLs, abgerufene Inhalte, Hashwerte)?
- Wurden Honey-Pot-Datensätze bei der Zielwebsite gefunden — sind diese eindeutig identifizierbar?
- Ist das Protokoll von einem neutralen Dritten (Notar, IT-Sachverständiger) zertifiziert?
- Enthält der Testcrawler-Abruf personenbezogene Daten — welche DSGVO-Rechtsgrundlage gilt?

## Typische Fallstricke

- Testcrawler, der robots.txt ignoriert, kann AGB-Verletzung begehen — Testcrawler-AGB-Compliance prüfen.
- Ohne neutrale Zertifizierung kann der Gegner die Authentizität der Crawl-Ergebnisse im Prozess angreifen.
- Honey-Pot-Datensätze müssen vor dem Verdachtsfall in der eigenen Datenbank vorhanden sein — nachträgliches Einpflegen entwertet den Beweis.
- DSGVO-Verletzung durch personenbezogene Datenabrufe im Testcrawler kann die Beweise unverwertbar machen.
- Sachverständiger muss die Crawl-Vergleichsmethodik vor Gericht erklären können — Briefing ist entscheidend.

## Quellen

- [§ 286 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/286.html)
- [§ 202a StGB — dejure.org](https://dejure.org/gesetze/StGB/202a.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [eIDAS-VO — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0910)
- [DSGVO Art. 6 — dejure.org](https://dejure.org/gesetze/DSGVO/6.html)
- [§ 371 ZPO — dejure.org](https://dejure.org/gesetze/ZPO/371.html)

---

## Skill: `cease-and-abmahnung-pruefen-datenbankvergleich`

_Cease-and-Desist-Letter (Abmahnung) im Datenbankrecht nach § 97a UrhG: Anforderungen an wirksame Abmahnung (Verletzungshandlung, Fristsetzung, Unterlassungsforderung, Schadensersatz), Kostenerstattung und Missbrauchsprüfung. Erstellt Abmahnschreiben für §§ 87a-87e UrhG-Verletzungen und bewertet G..._

# Cease-and-Desist-Letter (Abmahnung) im Datenbankrecht — § 97a UrhG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: UrhG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Datenbankbetreiber hat Nachweise für systematisches Scraping durch einen Wettbewerber und will eine förmliche Abmahnung mit Unterlassungsforderung senden.
- Unternehmen hat eine Abmahnung wegen behaupteter Datenbankrechts-Verletzung erhalten und muss kurzfristig entscheiden, ob es die Unterlassungserklärung unterzeichnet.
- Anwalt will überprüfen, ob eine erhaltene Abmahnung den gesetzlichen Anforderungen des § 97a UrhG entspricht und ob die Kostenerstattungspflicht besteht.

## Erste Schritte

1. Verletzungshandlung klar benennen: Welche konkreten Handlungen verletzen welche Normen (§ 87b UrhG) — Entnahme welcher Teile, durch wen, wann?
2. Unterlassungsforderung formulieren: Hinreichend bestimmt und vollständig — alle Verletzungshandlungen und Varianten erfassen.
3. Fristsetzung bestimmen: Üblicherweise kurze Frist (3-7 Tage) für Unterzeichnung der Unterlassungserklärung.
4. Kostenerstattungsanspruch prüfen: § 97a Abs. 3 UrhG — Kostenerstattung für Abmahnanwaltsgebühren bei Nicht-Verbraucher-Geschäftsbeziehung.
5. Missbrauchsprüfung vornehmen: § 97a Abs. 4 UrhG — unberechtigte Abmahnung kann Schadensersatzpflicht des Abmahnenden begründen.
6. Unterlassungserklärung entgegennehmen und prüfen: Ist sie ausreichend weit, zeitlich unbegrenzt und enthält sie eine angemessene Vertragsstrafe?

## Rechtsrahmen

- § 97a Abs. 1 UrhG: Abmahnung als Voraussetzung für Kostenerstattung — muss hinreichend deutlich sein.
- § 97a Abs. 3 UrhG: Ersatz der Rechtsanwaltsgebühren bei berechtigter Abmahnung — gilt auch im Datenbankrecht.
- § 97a Abs. 4 UrhG: Kostenerstattung für unberechtigte Abmahnung beim Abgemahnten.
- § 87b UrhG: Verletzungstatbestand — Grundlage für den Unterlassungsanspruch in der Abmahnung.
- § 97 Abs. 1 UrhG: Unterlassungsanspruch bei Datenbankherstellerrechts-Verletzung.
- § 339 BGB: Vertragsstrafe in Unterlassungserklärung — Höhe und Bestimmtheit.

## Prüfraster

- Ist die Verletzungshandlung in der Abmahnung konkret und vollständig beschrieben?
- Enthält die Abmahnung eine klare Unterlassungsforderung mit Fristsetzung?
- Ist der Abmahnende berechtigt — ist er tatsächlich Inhaber des Datenbankherstellerrechts (§ 87a Abs. 2 UrhG)?
- Entspricht der Kostenerstattungsanspruch dem § 97a Abs. 3 UrhG — liegt ein berechtigtes Interesse vor?
- Besteht Gefahr einer unberechtigten Abmahnung (§ 97a Abs. 4 UrhG) — muss der Abgemahnte Gegenabmahnung aussprechen?
- Ist die angeforderte Unterlassungserklärung ausreichend weit und zeitlich unbegrenzt?
- Ist die Vertragsstrafe in der beigefügten Unterlassungserklärung angemessen und vollstreckbar?

## Typische Fallstricke

- Zu eng gefasste Unterlassungserklärung des Abgemahnten beseitigt nicht alle Verletzungsformen — Gläubiger sollte ablehnen und klagen.
- Unberechtigte Abmahnung (kein tatsächliches Herstellerrecht) löst Kostenerstattung zugunsten des Abgemahnten aus (§ 97a Abs. 4 UrhG).
- Abmahnung zu kurzfristig (weniger als 3 Tage Frist) kann als unzumutbar angesehen werden.
- Wenn Verletzung bereits eingestellt wurde, besteht keine Wiederholungsgefahr mehr — Unterlassungsanspruch entfällt.
- Massenabmahnungen ohne konkrete Verletzungsanalyse sind rechtsmissbräuchlich nach § 8c UWG (analog).

## Output

- Abmahnschreiben-Vorlage für § 87b UrhG-Verletzung (vollständige Pflichtangaben)
- Unterlassungserklärung-Vorlage (mit Vertragsstrafe)
- Gegenabmahnung bei unberechtigter Abmahnung (§ 97a Abs. 4 UrhG)
- Abmahnung-Prüfcheckliste für Empfänger (Berechtigung, Vollständigkeit, Fristen)
- Antwortschreiben auf Abmahnung (Unterzeichnung / Widerspruch / modifizierte Erklärung)

## Quellen

- [§ 97a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97a.html)
- [§ 97 UrhG — dejure.org](https://dejure.org/gesetze/UrhG/97.html)
- [§ 87b UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87b.html)
- [§ 339 BGB — dejure.org](https://dejure.org/gesetze/BGB/339.html)
- [§ 87a UrhG — dejure.org](https://dejure.org/gesetze/UrhG/87a.html)
- [RL 96/9/EG — EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31996L0009)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

