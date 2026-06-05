---
name: uebertragende-sanierung-auslaendischer-office
description: "Uebertragende Sanierung Auslaendischer Office: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Uebertragende Sanierung Auslaendischer Office

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Uebertragende Sanierung Auslaendischer Office** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `uebertragende-sanierung-und-asset-deals` | Insolvenzverwalter will Geschäftsbetrieb verkaufen oder Investor kauft aus der Insolvenz und braucht Prüfung des Asset-Deals. Prüfraster uebertragende Sanierung Asset Deal im Regelverfahren Zustimmung Gläubigerausschuss § 160 InsO. Insolvenzplan § 254a InsO für gesellschaftsrechtliche Massnahmen Grundstuecke Marken Kundendaten. Aufschiebend versus auflösend bedingte Klauseln Haftungsabgrenzung. Output Kaufvertragsentwurf Checkliste Vollzugs-Voraussetzungen Gläubigerausschuss-Vorlage. Abgrenzung: insolvenzplan-starug-planwerkstatt für Insolvenzplan-Erstellung (anderes Plugin). |
| `auslaendischer-office-holder-register-und-grundbuch` | Prüft, ob und wie ein US debtor in possession, kanadischer trustee, receiver, monitor oder sonstiger ausländischer office holder in Deutschland handeln kann. |
| `vorsatzanfechtung-133-inso` | Prüffeld für vorsatzanfechtung 133 inso: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `zahlungsunfaehigkeit-pruefung-17-inso` | Erstellt ein strukturiertes Prüfgutachten zum Eröffnungsgrund der Zahlungsunfähigkeit nach § 17 InsO. Berechnet den Liquiditätsstatus zum Stichtag, wendet das 10-%-/3-Wochen-Schema des BGH an und würdigt Indizien der Zahlungseinstellung. Lädt, wenn der Nutzer Zahlungsunfähigkeit, Liquiditätsstatus, Insolvenzeröffnungsgrund oder § 17 InsO prüfen möchte. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Uebertragende Sanierung Auslaendischer Office**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `uebertragende-sanierung-und-asset-deals`

**Fokus:** Insolvenzverwalter will Geschäftsbetrieb verkaufen oder Investor kauft aus der Insolvenz und braucht Prüfung des Asset-Deals. Prüfraster uebertragende Sanierung Asset Deal im Regelverfahren Zustimmung Gläubigerausschuss § 160 InsO. Insolvenzplan § 254a InsO für gesellschaftsrechtliche Massnahmen Grundstuecke Marken Kundendaten. Aufschiebend versus auflösend bedingte Klauseln Haftungsabgrenzung. Output Kaufvertragsentwurf Checkliste Vollzugs-Voraussetzungen Gläubigerausschuss-Vorlage. Abgrenzung: insolvenzplan-starug-planwerkstatt für Insolvenzplan-Erstellung (anderes Plugin).

# Übertragende Sanierung und Asset Deals — innerhalb wie außerhalb des Insolvenzplans

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Übertragende Sanierung und Asset Deals — innerhalb wie außerhalb des Insolvenzplans` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Die **übertragende Sanierung** ist in der Praxis der typische Weg, einen Betrieb aus der Insolvenz zu retten: der Insolvenzverwalter verkauft den Geschäftsbetrieb (oder Teile davon) an einen Erwerber oder eine Auffanggesellschaft. Sie kann auf zwei Wegen geschehen:

- **Im Regelverfahren** durch den Insolvenzverwalter — mit Zustimmung des Gläubigerausschusses bzw. der Gläubigerversammlung (§§ 160-162 InsO).
- **Über einen Insolvenzplan** — durch rechtsgestaltende Wirkung des bestätigten Plans (§§ 254, 254a InsO).

Dieser Skill behandelt beide Varianten und zeigt die drei zentralen Konstruktionsfragen, die in jeder Übertragungsklausel zu beantworten sind:

1. **Bedingungsfrage:** aufschiebend (§ 158 Abs. 1 BGB) oder auflösend (§ 158 Abs. 2 BGB) bedingt?
2. **Zustimmungsfrage:** Welche Zustimmungen sind nötig — Gläubigerausschuss (§ 160 InsO), Gläubigerversammlung (§ 162 InsO), Einzelzustimmung Sicherungsnehmer, datenschutzrechtliche Einwilligung Betroffener — oder genügt die rechtsgestaltende Wirkung des bestätigten Plans (§ 254 InsO)?
3. **Vollzugsfrage:** Wie wirkt der bestätigte Plan auf das jeweilige Übertragungsregime (Grundbuch, Markenregister, datenschutzrechtliche Zweckbindung)?

Dieser Skill liefert die Entscheidungsmatrix für drei typische Asset-Klassen: Grundstücke, gewerbliche Schutzrechte (insb. Marken), Kundendaten.

---

## PFLICHT-DISCLAIMER

**Keine Rechtsberatung. Mechanischer Workflow.** Konkrete Klauselformulierungen sind im Einzelfall mit Notar, IP-Anwalt und Datenschutzbeauftragtem abzustimmen.

---

## Teil A — Begrifflicher Rahmen

### A.1 Aufschiebende vs. auflösende Bedingung

| Konstruktion | § 158 Abs. | Wirkung |
|---|---|---|
| **Aufschiebend bedingt** | Abs. 1 | Wirkung tritt erst mit Bedingungseintritt ein. Vor Eintritt: Anwartschaft, kein Vollrecht beim Erwerber. |
| **Auflösend bedingt** | Abs. 2 | Wirkung tritt sofort mit Planbestätigung ein. Bei Bedingungseintritt entfällt sie rückwirkend (§ 159 BGB) oder ex nunc (je nach Klausel). |

**Praktische Folgen:**

| Frage | Aufschiebend | Auflösend |
|---|---|---|
| Wer trägt Untergangsrisiko vor Bedingungseintritt? | Schuldner/Masse | Erwerber |
| Wann Grundbuchumschreibung möglich? | erst mit Bedingungseintritt | sofort mit Bestätigung |
| Steuerliche Realisation (z.B. Veräußerungsgewinn) | mit Bedingungseintritt | mit Bestätigung |
| Anfechtungsrisiko nach §§ 129 ff. InsO bei Scheitern | gering | hoch (Rückabwicklung erforderlich) |
| Gläubigerschutz bei Scheitern | gut (kein Vollzug) | erfordert dingliche Rückabwicklung |

**Faustregel:** Aufschiebend bedingt, wenn Bedingung **vor** Vollzug eintreten muss (z.B. Kaufpreiszahlung, behördliche Genehmigung, Verzicht von Sicherungsnehmer). Auflösend bedingt, wenn schneller Vollzug operativ nötig ist und Bedingung nur als Sicherheitsventil dient (z.B. Nachhaftungs-Cap-Klausel).

### A.2 Typische Bedingungen in Übertragungsklauseln

| Bedingung | Häufig bei | Typische Konstruktion |
|---|---|---|
| Kaufpreiszahlung auf Treuhandkonto | Asset Deal über Plan | aufschiebend |
| Bestandskraft der Planbestätigung (§ 252 InsO) | jede Plan-Übertragung | aufschiebend |
| Kartell- bzw. Außenwirtschaftsfreigabe | großer Asset Deal | aufschiebend |
| Übergabe + Inventur bestätigt | Betriebsfortführung | aufschiebend |
| Erfolgreiche Datenmigration / Cut-over | IT-/SaaS-Übertragungen | aufschiebend |
| Schlussabrechnung Plan mit Quote x % | Earn-out an Gläubiger | auflösend (wenn nicht erreicht: Rückübertragung) |
| Datenschutz-Opt-in-Quote über Schwelle | Kundendaten-Pakete | aufschiebend |
| Insolvenzeröffnung über Erwerber | Erwerber selbst gefährdet | auflösend (Notausstieg) |

---

## Teil B — Zustimmung der Gläubiger

### B.0 Übertragende Sanierung im Regelverfahren (außerhalb des Plans)

Im **Regelverfahren** veräußert der Insolvenzverwalter den Geschäftsbetrieb durch privatrechtlichen Asset-Deal-Vertrag (Asset Purchase Agreement, APA) — meist mit einer Auffanggesellschaft. Die §§ 254, 254a InsO greifen **nicht**, weil kein Plan vorliegt. Stattdessen:

| Vorgang | Norm | Wirkung |
|---|---|---|
| Veräußerung Betrieb oder wesentlicher Teile | § 160 Abs. 2 Nr. 1 InsO | Zustimmung Gläubigerausschuss zwingend |
| Veräußerung an besonders Interessierte (z.B. Schuldner, Geschäftsleitung, naher Angehöriger, Gesellschafter mit > 20 %) | § 162 InsO | Zustimmung Gläubigerversammlung zusätzlich |
| Veräußerung eines Lagers im Ganzen | § 160 Abs. 2 Nr. 2 InsO | Zustimmung Gläubigerausschuss |
| Aufnahme Darlehen, das die Masse erheblich belastet | § 160 Abs. 2 Nr. 3 InsO | Zustimmung Gläubigerausschuss |
| Klage- oder Prozessführung von erheblicher Bedeutung | § 160 Abs. 2 Nr. 4 InsO | Zustimmung Gläubigerausschuss |

**Wichtig:** Das Fehlen der Zustimmung macht das Geschäft nach außen **nicht** unwirksam (§ 164 InsO) — der Verwalter haftet aber persönlich nach § 60 InsO. In der Praxis wird die Zustimmung daher immer eingeholt und im Sitzungsprotokoll des Gläubigerausschusses dokumentiert.

**Unterschiede der beiden Wege:**

| Aspekt | Regelverfahren (Asset Deal) | Insolvenzplan |
|---|---|---|
| Vehikel | privatrechtlicher Kaufvertrag | bestätigter Plan |
| Zustimmungs-Mechanik | § 160-162 InsO (Ausschuss/Versammlung) | §§ 244, 245 InsO (Gruppen + Cramdown) |
| Dingliche Wirkung | nur durch Erfüllungsgeschäft (Notar, Register) | § 254a InsO ersetzt Erklärungen |
| Lastenfreistellung | Verhandlung mit jedem Sicherungsnehmer | im Plan integrierbar |
| Geschwindigkeit | i.d.R. schneller (Wochen bis wenige Monate) | langsamer (mehrere Monate) |
| Anfechtungsrisiko | §§ 129 ff. InsO bleiben | durch Plan-Wirkung reduziert |
| Steuerliche Sanierungserleichterungen (§ 3a EStG) | nur eingeschränkt | umfassend bei Plan-Sanierung |
| Arbeitsverhältnisse | § 613a BGB volle Wirkung | § 613a BGB volle Wirkung; Sonderkündigungsrecht § 113 InsO bleibt |
| Restschuldbefreiung Inhaber | bleibt im Verfahren | über Plan möglich |

**Entscheidungs-Faustregeln:**

- **Asset Deal außerhalb Plan**, wenn: Zeitdruck, klare Erwerber-Konstellation, überschaubare Sicherheiten-Lage, einfache Strukturen.
- **Insolvenzplan**, wenn: viele Sicherheiten, komplexe Lastenfreistellung, steuerliche Sanierungsklausel-Bedarf, Erhalt der Schuldner-Rechtsform gewünscht, Rangrücktritt großer Gläubiger sinnvoll.

→ Skills im Plugin `insolvenzverwaltung`: `iv-massemehrung-asset-realisation`, `iv-sicherung-betriebsfortfuehrung`, `iv-eigenverwaltung-sachwaltung`.

### B.1 Grundsatz: Planbestätigung ersetzt Einzelzustimmung

Mit rechtskräftiger Bestätigung des Insolvenzplans treten die im **gestaltenden Teil** vorgesehenen Wirkungen für und gegen alle Beteiligten ein (§ 254 Abs. 1 InsO). Das gilt auch dann, wenn der einzelne Gläubiger gegen den Plan gestimmt hat — die Mehrheits- und Cramdown-Mechanismen der §§ 244, 245 InsO ersetzen die Einzelzustimmung.

**Konsequenz:** Eine **separate** zivilrechtliche Zustimmung der Gläubiger ist für die im Plan vorgesehenen Übertragungen grundsätzlich **nicht** erforderlich, wenn:

- die Wirkung im gestaltenden Teil eindeutig beschrieben ist (Bestimmtheitsgrundsatz, § 221 InsO)
- der betroffene Gläubiger in einer Gruppe abstimmungsberechtigt war (§§ 222, 237, 238 InsO)
- der Plan die gesetzlichen Mehrheiten erreicht hat (§ 244 InsO) oder Cramdown greift (§ 245 InsO)
- das Gericht den Plan bestätigt hat (§ 248 InsO)

### B.2 Erforderliche Mehrheiten

| Norm | Mehrheit | Bezugspunkt |
|---|---|---|
| § 244 Abs. 1 Nr. 1 InsO | Kopfmehrheit | Gruppe der abstimmenden Gläubiger |
| § 244 Abs. 1 Nr. 2 InsO | Summenmehrheit | Summe der Ansprüche |
| § 245 InsO | Obstruktionsverbot/Cramdown | Mindestquote, Schlechterstellungsverbot |
| § 247 InsO | Zustimmung Schuldner | außer Schlechterstellung |
| § 251 InsO | Minderheitenschutz | Antragsfrist im Termin |

**Wichtig:** Auch ohne klassische Gruppenzustimmung kann der Plan unter den Voraussetzungen des § 245 InsO bestätigt werden (Cramdown), wenn keine Gruppe schlechter steht als ohne Plan und die Gesamtwirtschaftlichkeit gewahrt bleibt. → Skill: `ips-cramdown-obstruktion`.

### B.3 Wann doch separate Zustimmung nötig ist

| Konstellation | Warum separate Zustimmung |
|---|---|
| Eingriff in **Absonderungsrecht** ohne Kompensation | § 223 InsO Sondergruppe + Schlechterstellungsverbot § 245 InsO |
| Vollverzicht durch **gesicherten** Gläubiger | regelmäßig Sondergruppe, ggf. Einzelverzicht |
| Übertragung eines vom Gläubiger sicherungsübereigneten Gegenstands | Zustimmung Sicherungsnehmer **oder** Ablösung |
| Übertragung mit Schuldübernahme Dritter | § 415 BGB Gläubiger-Zustimmung |
| Datenschutzrechtlich heikle Kundendaten-Übertragung | DSGVO-Einwilligung **Betroffener**, nicht Gläubiger (Teil C.3) |
| Personenbezogene Verträge ohne Übergangsklausel | § 415 BGB / § 613a BGB (Arbeitsverhältnisse, eigene Schiene) |

---

## Teil C — Anwendung auf drei Asset-Klassen

Die folgenden Klauseltypen lassen sich sowohl im Asset-Deal-Vertrag (Regelverfahren) als auch im gestaltenden Teil des Insolvenzplans verwenden. Wo § 254a InsO eingreift, ist das ausdrücklich vermerkt.

### C.1 Grundstücksübertragung

**Besonderheit:** § 254a InsO ist der entscheidende Hebel. Der Plan kann dingliche Erklärungen (Auflassung, Eintragungsbewilligung, sonstige Willenserklärungen) **ersetzen**.

| Element | Ohne Plan | Mit Plan (§ 254a InsO) |
|---|---|---|
| Auflassung (§ 925 BGB) | notarielle Auflassung erforderlich | im Plan enthaltene Erklärung gilt als abgegeben |
| Eintragungsbewilligung (§ 19 GBO) | separate Erklärung Schuldner | im Plan enthalten |
| Form § 311b BGB | notarielle Beurkundung | Plan-Form (§ 254a Abs. 2 InsO) |
| Gläubiger-Zustimmung | bei jeder einzelnen Verfügung | im Mehrheitsbeschluss erledigt |

**Anwendung in der Klausel:**

- **Aufschiebend bedingt** auf Bestandskraft des Bestätigungsbeschlusses + Kaufpreiszahlung: empfohlen, weil keine vorzeitige Buchposition geschaffen wird.
- **Auflösend bedingt** auf Nichtzahlung: möglich, aber Rückabwicklung über Grundbuch aufwändig — Sicherheit über Vormerkung/Treuhand vorziehen.

**Praktische Stolpersteine:**

- Grundbuchamt verlangt Vorlage des **rechtskräftigen** Plans plus Bestätigungsbeschluss (Plan im Original mit Eingangsstempel Gericht, Bescheinigung Rechtskraft).
- Bei Belastungen: Lastenfreistellungserklärungen der Grundpfandgläubiger müssen ebenfalls über den Plan oder separat herbeigeführt werden.
- Grunderwerbsteuer entsteht regelmäßig mit Wirksamkeit der Übertragung (§ 1 Abs. 1 Nr. 1 GrEStG) — beachten bei Bedingungs-Konstruktion.

**Muster (verkürzt):**

> Mit Bestandskraft der Bestätigung dieses Plans (§ 252 InsO) und Eingang des Kaufpreises in voller Höhe auf dem Notar-Anderkonto Nr. ... überträgt die Schuldnerin auflassend an die Erwerberin das im Grundbuch von X, Blatt Y eingetragene Grundstück, Flur Z, Flurstück W. Die Auflassung und die Eintragungsbewilligung gelten gemäß § 254a Abs. 2 InsO als mit Bestandskraft des Bestätigungsbeschlusses abgegeben.

→ Detailskill: `ips-gestaltender-teil`, `ips-sicherheiten-drittsicherheiten`.

### C.2 Marken- und IP-Übertragung

**Besonderheit:** Markenrechte (§ 27 MarkenG), Patente (§ 15 PatG), Designs (§ 29 DesignG), Gebrauchsmuster (§ 22 GebrMG) sind frei übertragbar — aber **registerpflichtig**.

| Schutzrecht | Übertragungsnorm | Register | Wirkung Plan |
|---|---|---|---|
| Marke (national) | § 27 Abs. 3 MarkenG | DPMA-Register | § 254a InsO ersetzt Übertragungserklärung |
| Unionsmarke | Art. 20 UMV | EUIPO | Plan reicht nicht; separate Anmeldung beim EUIPO |
| Patent | § 15 Abs. 1 PatG | DPMA-Register | § 254a InsO ersetzt |
| Europäisches Patent | Art. 71 EPÜ | nationale Validierung | gesonderte Übertragung je Staat |
| Design | § 29 DesignG | DPMA | § 254a InsO ersetzt |
| Urheberrechte | nicht übertragbar (§ 29 Abs. 1 UrhG) | — | Plan kann nur **Nutzungsrechte** übertragen (§ 31 UrhG) |
| Lizenzen | je nach Lizenzvertrag | — | § 103 InsO Wahlrecht beachten |

**Wichtige Sonderfälle:**

- **Konzernmarken-Lizenzkette:** Wenn die Schuldnerin Lizenznehmer einer Konzern-Mutter ist, kann der Plan die Lizenz nicht einseitig auf den Erwerber übertragen — § 415 BGB-Zustimmung des Lizenzgebers nötig oder neuer Lizenzvertrag.
- **Domainnamen:** keine Register-Schutzrechte, sondern schuldrechtliche Ansprüche gegen Registrare (DENIC etc.). Plan reicht; Mitwirkung des Registrars (KK-Antrag) operativ herbeiführen.
- **Open-Source-Lizenzen** in der Schuldner-Software: nicht übertragbar im klassischen Sinn, weil die Lizenz vom Urheber dem Endnutzer eingeräumt wird; aber Pflichtenkette (Quelltext-Verfügbarkeit, Lizenztexte) übergeht beim Erwerber.

**Anwendung in der Klausel:**

- **Aufschiebend bedingt** auf Bestandskraft + Kaufpreis: Markenrechtsübertragung nimmt bis zur DPMA-Umschreibung mehrere Wochen — Erwerber kann zwischenzeitlich Treuhand-Nutzungsrecht erhalten.
- **Auflösend bedingt** ist riskant: einmal beim DPMA umgeschrieben, ist Rückübertragung aufwändig und kostenpflichtig.

**Muster (verkürzt):**

> Mit Bestandskraft der Bestätigung dieses Plans überträgt die Schuldnerin sämtliche im Annex M aufgeführten Marken, Patente und Designs an die Erwerberin. Die Übertragungserklärungen und die Anträge auf Umschreibung im DPMA-Register gelten als mit Bestandskraft abgegeben (§ 254a Abs. 2 InsO). Die Erwerberin trägt die Kosten der Umschreibung. Bis zur Umschreibung räumt die Schuldnerin der Erwerberin eine unwiderrufliche, ausschließliche und kostenlose Nutzungslizenz ein.

### C.3 Kundendaten-Übertragung

**Besonderheit:** Hier wirkt § 254a InsO **nicht** — die Plan-Bestätigung **ersetzt nicht** die datenschutzrechtliche Rechtsgrundlage. Die Übertragung personenbezogener Daten ist ein eigener Vorgang nach DSGVO.

**Rechtsgrundlagen-Kaskade (Art. 6 Abs. 1 DSGVO):**

| Buchstabe | Tauglich bei Kundendaten? | Begründung |
|---|---|---|
| (a) Einwilligung | **ja, Goldstandard** | informierte, freiwillige, dokumentierte Einwilligung |
| (b) Vertragserfüllung | nur eingeschränkt | wenn Vertragsbeziehung zum Erwerber tatsächlich fortgeführt wird, sonst kein "erforderlich" |
| (c) rechtliche Verpflichtung | nein | Plan-Bestätigung schafft keine datenschutzrechtliche Pflicht |
| (d) lebenswichtige Interessen | nein | unpraktisch |
| (e) öffentliches Interesse | nein | bei privatwirtschaftlichem Asset Deal nicht einschlägig |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

**Empfehlung Praxisstandard "Opt-in mit Anreiz":**

1. **Information** aller Betroffenen vor Vollzug (Art. 13/14 DSGVO):
 - Identität bisheriger und künftiger Verantwortlicher
 - Zwecke der Verarbeitung beim Erwerber
 - Rechtsgrundlage
 - Empfänger / Kategorien
 - Dauer der Speicherung
 - Rechte der Betroffenen (Art. 15-22 DSGVO)
 - Beschwerderecht Aufsichtsbehörde

2. **Einwilligungs-Kampagne** ("Opt-in") mit Anreiz/Goodie:
 - Schreiben oder E-Mail an alle aktiven Kunden
 - klare Frage: "Sind Sie damit einverstanden, dass Ihre Daten an die Erwerberin übertragen werden?"
 - klare Abgrenzung: "Auch ohne Einwilligung haben Sie Anspruch auf [Ersatzleistung / Erstattung / vertragsabwicklung]."
 - Anreiz (Beispiele: 10-EUR-Gutschein, Verlängerung Garantie um 12 Monate, ein zusätzliches Servicepaket, Treuepunkte-Verdopplung, etc.)
 - Rückkanal: einfaches Antwortverfahren (Online-Formular mit DOI, postalisches Antwortkärtchen, E-Mail-Confirm-Link)
 - **Freiwilligkeit muss gewahrt sein** — keine Kopplung an unverzichtbare Leistungen (Art. 7 Abs. 4 DSGVO)
 - Dokumentation jeder Einwilligung mit Zeitstempel, Datenpunkt, Inhalt

3. **Übergangsmechanik im Plan:**
 - **aufschiebend bedingt** auf Erreichen einer Quote x % (z.B. 60 %) zugestimmter Datensätze
 - Daten ohne Zustimmung: bleiben bei Masse zur Restabwicklung, werden nach Restabwicklung gelöscht (Art. 17 DSGVO)
 - alternativ: Treuhand-Daten-Custodian, der Daten nur freigibt, wenn Zustimmung nachträglich erteilt

**Wichtige Schranken:**

| Datenkategorie | Besonderheit |
|---|---|
| besondere Kategorien (Art. 9 DSGVO) — Gesundheitsdaten, Religion, Gewerkschaft etc. | Einwilligung praktisch zwingend, Interessenabwägung Art. 6 Abs. 1 lit. f scheidet aus |
| Daten Minderjähriger | Art. 8 DSGVO: Einwilligung der Erziehungsberechtigten erforderlich |
| Bank-/Zahlungsdaten | aufsichtsrechtliche Sonderregeln (BaFin), ggf. KWG/ZAG |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Telekommunikationsdaten | § 3 TDDDG, § 9 TKG |
| Bestandskunden vs. Interessenten | Interessenten ohne abgeschlossenen Vertrag i.d.R. nur mit Einwilligung übertragbar |

**Aufsichtsbehörden-Kommunikation:**

- frühzeitige Konsultation der zuständigen Landesdatenschutzbehörde empfohlen (Art. 36 DSGVO bei DSFA), insbesondere bei großen Datenmengen oder sensitiven Kategorien
- DSFA (Art. 35 DSGVO) regelmäßig erforderlich
- bei Drittstaaten-Erwerber: zusätzlich Kapitel V DSGVO (Standardvertragsklauseln, Angemessenheitsbeschluss, etc.)

**Muster (verkürzt) — Opt-in-Schreiben:**

> Sehr geehrte Frau/Herr [Name], die [Schuldnerin] wird im Rahmen eines bestätigten Insolvenzplans an die [Erwerberin] übergehen. Die [Erwerberin] möchte Ihre Vertragsbeziehung nahtlos fortführen.
>
> Damit das möglich ist, müssen wir Ihre Kundendaten (Name, Anschrift, E-Mail, Bestellhistorie, Vertragsdaten) an die [Erwerberin] übertragen. Bitte teilen Sie uns mit, ob Sie damit einverstanden sind.
>
> Als Dankeschön für Ihre Rückmeldung erhalten Sie unabhängig von Ihrer Entscheidung [Goodie X — z.B. 15-EUR-Willkommensgutschein]. Der Gutschein ist nicht an Ihre Einwilligung gekoppelt (Art. 7 Abs. 4 DSGVO — Kopplungsverbot).
>
> [☐] Ja, ich bin damit einverstanden, dass meine Daten an die [Erwerberin] übertragen werden.
>
> [☐] Nein, ich möchte keine Übertragung. Meine Daten werden gelöscht, soweit keine gesetzlichen Aufbewahrungspflichten bestehen.
>
> Hinweise nach Art. 13/14 DSGVO: ... [vollständige Belehrung].
>
> Diese Einwilligung können Sie jederzeit widerrufen (Art. 7 Abs. 3 DSGVO).

**Muster (verkürzt) — Klausel im gestaltenden Teil:**

> Die Übertragung der in Annex K bezeichneten Kundendaten an die Erwerberin steht unter der aufschiebenden Bedingung, dass die jeweilige betroffene Person der Übertragung wirksam zugestimmt hat (Art. 6 Abs. 1 lit. a, Art. 7 DSGVO). Datensätze ohne Einwilligung werden nicht übertragen; sie verbleiben in der Masse und werden nach Abschluss der Restabwicklung, spätestens binnen sechs Monaten nach Bestandskraft dieses Plans, datenschutzkonform gelöscht. Der Insolvenzverwalter führt vor Vollzug eine Einwilligungskampagne nach Maßgabe der Anlage D durch.

---

## Teil D — Entscheidungsmatrix

| Asset | § 254a InsO ersetzt? | typische Bedingung | Gläubiger-Zustimmung |
|---|---|---|---|
| Inlands-Grundstück | ja, vollständig | aufschiebend (Bestandskraft + Kaufpreis) | im Plan-Beschluss erledigt |
| Auslands-Grundstück | nein | aufschiebend + ausländisches Formerfordernis | Mehrheitsbeschluss + ggf. ausländische Vollstreckbarerklärung |
| Nationale Marke / Patent | ja | aufschiebend (Bestandskraft) | im Plan-Beschluss erledigt |
| Unionsmarke / EPÜ-Patent | nein | aufschiebend + Register-Anmeldung | Plan-Beschluss + Mitwirkungspflicht Schuldner |
| Lizenz aus Drittvertrag | nein (§ 415 BGB) | aufschiebend + Lizenzgeber-Zustimmung | zusätzlich Lizenzgeber-Zustimmung |
| Kundendaten (nicht-sensitiv, Bestand) | nein | aufschiebend (Einwilligung Betroffene) | Plan-Beschluss + DSGVO-Einwilligung Betroffene |
| Kundendaten (sensitiv, Art. 9 DSGVO) | nein | aufschiebend (Einwilligung verpflichtend) | zwingend Einwilligung |
| Sicherungsübereignete Sache | nein | aufschiebend (Ablösung Sicherungsnehmer) | zusätzlich Sicherungsnehmer-Zustimmung oder Ablösung |
| Arbeitsverhältnisse | eigene Schiene § 613a BGB | je nach Konstruktion | Information der Beschäftigten |

---

## Teil E — Häufige Fehlerquellen

1. **Verwechslung § 254 mit § 254a InsO:** § 254 = allgemeine Rechtsgestaltungswirkung der Bestätigung; § 254a = Ersatz für dingliche und sonstige Erklärungen. Nur § 254a "ersetzt" Auflassung und Co.

2. **Annahme, DSGVO-Einwilligung sei durch Plan-Bestätigung erfasst.** Das ist falsch. Die Einwilligung muss von der **betroffenen Person** persönlich erteilt werden — nicht von der Gläubigerversammlung.

3. **Auflösend bedingte Grundstücksübertragung als "Sicherheit":** führt zu sperrigem Rückabwicklungsproblem. Besser: aufschiebend + Vormerkung + Treuhand-Kaufpreis.

4. **Lizenz aus Konzernvertrag ohne Lizenzgeber-Zustimmung übertragen:** Plan-Bestätigung wirkt nicht gegenüber dem Lizenzgeber außerhalb der Plan-Betroffenen — § 415 BGB bleibt.

5. **Kundendaten-Goodie als Kopplung ("Sie bekommen den Gutschein nur, wenn Sie zustimmen"):** kann Freiwilligkeit (Art. 7 Abs. 4 DSGVO) gefährden. Sauberer: Goodie für **alle**, Zustimmung als zusätzlicher Wert beim Erwerber.

6. **Mehrheiten verwechselt:** §§ 244, 245 InsO regeln die **Plan-Annahme**, nicht die einzelne Vermögens-Übertragung. Solange Plan ordnungsgemäß angenommen ist, bedarf einzelne Übertragung im gestaltenden Teil keiner weiteren Zustimmung — außer in den Ausnahmen aus B.3.

7. **DPMA-Umschreibungsantrag vergessen:** Plan-Bestätigung allein bewirkt keine automatische Register-Umschreibung. Antrag und Gebühr beim DPMA bleiben Aufgabe des Erwerbers (Mitwirkungspflicht Schuldner in der Klausel verankern).

8. **Auslands-Sachenrecht ignoriert:** Bei Grundstücken im EU-Ausland gilt lex rei sitae — § 254a InsO wirkt nicht. Lokalen Notar einschalten.

---

## Querverweise

Innerhalb des `insolvenzrecht`-Plugins:

- `mandat-triage-insolvenzrecht` — Eingangs-Triage
- `insolvenzrecht-kaltstart-interview` — Sachverhalts-Erfassung
- `anfechtungsrechte-pruefen` — Risiko Rückabwicklung
- `vorsatzanfechtung-133-inso` — Anfechtungs-Tiefencheck
- `glaeubigerausschuss-mitwirkung` — Zustimmung im Gremium
- `konzerninsolvenz-koordination` — bei konzerninternen Übertragungen

Für die volle Plan-Mechanik siehe Plugin `insolvenzplan-starug-planwerkstatt`:

- `ips-gestaltender-teil` — Aufbau gestaltender Teil
- `ips-darstellender-teil` — Begründung der Übertragung
- `ips-anlagenpaket` — Annexe und Listen
- `ips-planbetroffene-auswahl` — Wer ist betroffen
- `ips-gruppen-klassenbildung` — Gruppenbildung
- `ips-cramdown-obstruktion` — Mehrheits-Ersatz
- `ips-sicherheiten-drittsicherheiten` — Sicherheiten-Lastenfreistellung
- `ips-planvollzug-monitoring` — Vollzug
- `ips-steuern-bilanz-folgen` — steuerliche Folgen
- `ips-redteam-qualitygate` — Plausibilität

---

## Mini-Checkliste vor Vollzug (Plan-Einreichung oder Asset-Deal-Signing)

- [ ] Verfahrensweg gewählt (Regelverfahren-Asset-Deal vs. Insolvenzplan) und begründet
- [ ] Bei Regelverfahren: Zustimmung Gläubigerausschuss § 160 InsO eingeholt; bei besonders Interessierten zusätzlich Gläubigerversammlung § 162 InsO
- [ ] Asset-Inventar mit Zuordnung zu §-254a-fähig vs. nicht
- [ ] Bedingungs-Konstruktion gewählt (aufschiebend/auflösend) und begründet
- [ ] § 254a-Klauseln nach den drei Bestandteilen (Willenserklärung, Form, Register) durchformuliert
- [ ] Mehrheits-Strategie geprüft (§§ 244, 245, 247 InsO)
- [ ] Drittsicherheiten und Lizenzgeber-Zustimmungen separat eingeholt oder kompensiert
- [ ] DSGVO-Datenkategorien-Inventar erstellt
- [ ] DSFA durchgeführt (Art. 35 DSGVO)
- [ ] Opt-in-Kampagne mit Goodie konzipiert; Freiwilligkeit gewährleistet (Art. 7 Abs. 4 DSGVO)
- [ ] Information Betroffener nach Art. 13/14 DSGVO vorbereitet
- [ ] Treuhand-/Vormerkungs-Mechanik für Grundstücke geklärt
- [ ] Register-Anträge DPMA/EUIPO vorbereitet
- [ ] Steuerliche Realisationszeitpunkte abgestimmt
- [ ] Rote-Team-Review durch unabhängige Stelle (Notar, IP-Anwalt, DSB)

---

Hinweis: Keine Rechtsberatung. Mechanische Strukturhilfe für Insolvenz- und StaRUG-Pläne. Konkrete Klauseln sind im Einzelfall mit Notar, IP-Fachanwalt und Datenschutzbeauftragtem abzustimmen.

## Weitere Leitentscheidungen — Uebertragende Sanierung (Stand Mai 2026)

- **BGH IX ZR 122/23 vom 05.12.2024** — Bei Asset-Deals mit Sanierungsbezug: Unlauterkeit beim Bargeschäft (§ 142 Abs. 1 Hs. 2 InsO) konkret prüfen. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Bei Erwerber-Risiken: Vorsatzanfechtung nach § 133 InsO bei kongruenten Deckungen restriktiver. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- Konkrete BGH-Linien zu § 613a BGB (Betriebsübergang) im Insolvenzkontext und zu § 75 AO (Übernehmerhaftung Steuern) vor Ausgabe über dejure.org / openjur.de verifizieren.

## Output-Template Asset-Deal-Memo

**Adressat:** Insolvenzverwaltung (intern) — Tonfall: sachlich

```
ASSET-DEAL DOKUMENTATION
IV: [NAME] Verfahren: [AZ] Datum: [DATUM]

VERAEUSSERTES VERMÖGEN:
[Auflistung Assets, Grundstuecke, IP, Kundenstamm, Inventar]

KAUFPREIS: EUR [BETRAG]
ERWERBER: [NAME, Rechtsform]
CLOSING: [DATUM]

VERGLEICHSRECHNUNG:
Asset-Deal-Erloes: EUR [BETRAG]
Liquidationsalternative: EUR [BETRAG]
Insolvenzplan-Alternative: EUR [BETRAG]
EMPFEHLUNG: Asset-Deal [BEGRUENDUNG]

PERSONALAUFNAHME (§ 613a BGB):
[X] AN Erwerber uebernommen: [ANZAHL]
[X] Kuendigungen IV: [ANZAHL] (aus betrieblichen Gruenden, BA informiert)

STEUERN:
USt Asset-Deal: EUR [BETRAG] (Masseverbindlichkeit)
```

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

## 2. `auslaendischer-office-holder-register-und-grundbuch`

**Fokus:** Prüft, ob und wie ein US debtor in possession, kanadischer trustee, receiver, monitor oder sonstiger ausländischer office holder in Deutschland handeln kann.

# Ausländischer Insolvenzverwalter: inzidente Anerkennung, Register, Grundbuch und GmbH-Anteile

## Deutscher Ausgangspunkt
Deutschland kennt kein eigenes Anerkennungsverfahren nach Art eines US Chapter 15. Die Anerkennung ausländischer Insolvenzverfahren richtet sich für Drittstaaten vor allem nach § 343 InsO und wird praktisch oft inzident geprüft: durch Prozessgericht, Notar, Registergericht, Grundbuchamt, Bank, Verwahrer oder Vertragspartner.

## Prüfschritte
1. **EU oder Drittstaat:** EuInsVO 2015/848 bei EU-Verfahren (ohne Dänemark) von Drittstaatenfällen trennen.
2. **Ausländische Zuständigkeit:** COMI/Sitz/Verfahrensart nach deutschen Anerkennungsmaßstäben und ordre public prüfen.
3. **Person und Macht:** Office holder, debtor in possession, trustee, receiver, monitor, court approval, plan restrictions, ordinary course und konkrete Befugnis feststellen.
4. **Deutsches Asset:** GmbH-Anteil (§ 15 GmbHG, § 40 GmbHG), Grundstück (§§ 873, 925, 311b BGB, § 29 GBO), Konto, Forderung, IP-Recht, Prozessstandschaft.
5. **Nachweisform:** Apostille/Legalisation, beglaubigte Übersetzung, court order, certificate, register extract, notarial certification und grundbuchtaugliche Form.

## Output
Erzeuge ein Nachweispaket `ausländische Entscheidung / Amtsnachweis / Befugnis / deutsches Formrecht / Empfänger / Restzweifel` sowie einen Register-/Grundbuchanschreibensentwurf.

## 3. `vorsatzanfechtung-133-inso`

**Fokus:** Prüffeld für vorsatzanfechtung 133 inso: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Vorsatzanfechtung § 133 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorsatzanfechtung § 133 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Die Vorsatzanfechtung ist die häufigste und längste Anfechtungs-Art. Mandanten oft als Anfechtungs-Gegner — Lieferanten, Banken, Berater. Dieses Skill bedient Verteidigung und Anfechtungs-Geltendmachung.

## Eingaben

- Konstellation (Mandant Anfechtungs-Gegner oder Insolvenz-Verwalter?)
- Rechtsgeschäft / Zahlung mit Daten
- Zeit-Punkt Insolvenz-Ereignis
- Kenntnisstand Vertragspartner zum Tatzeitpunkt
- Sanierungs-Bezug der Transaktion
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Schritt 1 — Tatbestand § 133 Abs. 1 InsO


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Voraussetzungen

a) **Rechts-Handlung** des Schuldners innerhalb der maßgeblichen Anfechtungs-Frist (4 oder 10 Jahre — siehe unten) vor Antrag

b) **Vorsatz Schuldner** zur Gläubiger-Benachteiligung

c) **Kenntnis Vertragspartner** des Vorsatzes

### Frist-Spezifikation (seit Anfechtungsreform 5.4.2017, in Kraft 5.4.2017)

**ZUERST PRÜFEN: Welcher Tatbestand?**

- **4 Jahre — § 133 Abs. 2 InsO**: Deckungs- oder Befriedigungs-Handlungen, die dem Gläubiger **kongruent** eine Sicherung oder Befriedigung gewährt haben (z.B. Fälligkeits-Zahlung Lieferant, planmäßige Tilgung Bank-Kredit, vertraglich vereinbarte Sicherheits-Bestellung)
- **10 Jahre — § 133 Abs. 1 InsO**: alle anderen Rechts-Handlungen mit Gläubiger-Benachteiligungs-Vorsatz, insbesondere **Vermögens-Verschiebungen** (Schenkungen, Verkauf unter Wert, Übertragung auf nahe-stehende Personen, inkongruente Deckungen, Vermögens-Ausgliederungen)
- **Vor 5.4.2017** — einheitlich 10 Jahre für alle Tatbestände (Alt-Fälle, nur noch in extrem alten Verfahren relevant)
- **Unentgeltliche Leistungen** — separater Tatbestand § 134 InsO (4 Jahre)

### Praktische Erst-Sortierung

| Sachverhalt | Frist | Norm |
|---|---|---|
| Kongruente Fälligkeits-Zahlung | 4 Jahre | § 133 Abs. 2 |
| Vorzeitige Tilgung (inkongruent) | 10 Jahre | § 133 Abs. 1 |
| Verkauf unter Wert an Dritte | 10 Jahre | § 133 Abs. 1 |
| Übertragung auf Familie | 10 Jahre | § 133 Abs. 1 (+ § 138) |
| Schenkung | 4 Jahre | § 134 InsO |
| Bestellung Sicherheit nach Schuldgrund | 10 Jahre | § 133 Abs. 1 (inkongruent) |

### Beweislast Insolvenz-Verwalter

- Schuldner-Vorsatz und Gläubiger-Kenntnis darzulegen
- **Indizien-Beweis** zentral
- Bei § 133 Abs. 2 (4-Jahres-Frist) zusätzliche **Kenntnis-Vermutung**: nur wenn Gläubiger drohende Zahlungs-Unfähigkeit kannte

## Schritt 2 — Vorsatz des Schuldners

### Subjektive Voraussetzung

- **Bewusstsein der Gläubiger-Benachteiligung**
- **Wenigstens billigende Inkaufnahme** dolus eventualis
- **Nicht erforderlich:** Schädigungs-Absicht direkt

### Neuausrichtung der Vorsatzanfechtung (BGH-Linie seit 2021)

Seit der Grundsatzentscheidung **BGH IX ZR 72/20 vom 06.05.2021** verfolgt der IX. Zivilsenat eine deutlich anfechtungsfreundliche Restriktion bei kongruenten Deckungen. Bestätigt und konkretisiert durch:

- **BGH IX ZR 129/22 vom 18.04.2024**: Aus der bloßen objektiv festgestellten Zahlungsunfähigkeit darf nicht ohne weiteres auf einen Gläubigerbenachteiligungsvorsatz geschlossen werden. Maßgeblich ist, ob der Schuldner wusste oder zumindest billigend in Kauf nahm, dass er andere Gläubiger zu späterer Zeit nicht vollständig befriedigen kann. Bei Liquiditätsbehauptungen des Verwalters kann ein einfaches Bestreiten des außenstehenden Anfechtungsgegners genügen.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** (Schwesterentscheidung zu § 135 InsO Gesellschafterdarlehen): Verschärfung der Anforderungen an die Anfechtung wegen gesellschafterähnlicher Stellung.
 Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>

Typische Indizien des Vorsatzes (vor Ausgabe einzeln verifizieren):

- **Zahlungs-Unfähigkeit** zum Handlungs-Zeitpunkt (Liquiditätsstatus konkret darlegen, IX ZR 129/22)
- **Drohende Zahlungs-Unfähigkeit** mit Bewusstsein
- **Vorzugs-Behandlung** einzelner Gläubiger
- **Inkongruente Leistungs-Bedingungen**

### Reform 2017 Modifikation

- 4-Jahres-Frist für kongruente Deckungs- und Befriedigungs-Handlungen (§ 133 Abs. 2 InsO)
- Kenntnis der drohenden Zahlungs-Unfähigkeit allein nicht mehr ausreichend für die Vorsatz-Vermutung bei kongruenter Leistung — bestätigt durch BGH IX ZR 129/22 (18.04.2024)

## Schritt 3 — Kenntnis Vertragspartner

### Subjektive Voraussetzung

- Kenntnis des Vorsatzes Schuldner
- **Beweis-Erleichterung** wenn drohende Zahlungs-Unfähigkeit bekannt § 133 Abs. 1 Satz 2 InsO

### Indizien BGH-Linie

- **Mahnungen** durch andere Gläubiger
- **Zwangs-Vollstreckungs-Aktivität**
- **Bekannte Sanierungs-Bemühungen**
- **Bei Banken** Konto-Über-ziehungs-Vermerke
- **Bei Lieferanten** Vorkasse-Anforderung

Kenntnis nach BGH-Linie (vor Ausgabe konkretes Az. prüfen):

- Bei drohender Zahlungs-Unfähigkeit indiziert die Kenntnis des Gläubigers den Vorsatz
- Nach **BGH IX ZR 129/22 vom 18.04.2024** reicht bloße Kenntnis der Liquiditätsunterdeckung nicht ohne konkrete Indizien für die Erwartung dauerhafter Unterdeckung

## Schritt 4 — Bargeschäfts-Privileg § 142 InsO

### Voraussetzungen

- **Unmittelbarer Leistungs-Austausch** zwischen Schuldner und Gläubiger
- **Gleichwertige Gegenleistung**
- **Innerhalb 30 Tage** (keine starre Grenze; Bewertung des engen zeitlichen Zusammenhangs)
- **Im üblichen Geschäfts-Verlauf**

### Wirkung

- **Anfechtungs-Schutz** auch bei § 133 InsO
- **Ausnahme nach § 142 Abs. 1 Hs. 2 InsO** (Fassung seit 2017): Bei Vorliegen der Voraussetzungen der Vorsatzanfechtung gilt das Privileg nur, wenn der Schuldner *unlauter* handelte und der andere Teil dies erkannte.

### Unlauterkeit nach BGH IX ZR 122/23 vom 05.12.2024

Der IX. Zivilsenat hat erstmals höchstrichterlich präzisiert, wann der Schuldner bei einem Bargeschäft *unlauter* iSd § 142 Abs. 1 Hs. 2 InsO handelt:

- Unlauterkeit erfordert, dass es bei der Transaktion **weniger um die Abwicklung eines Bargeschäfts als vielmehr um gezielt schädigendes Verhalten** gegenüber den übrigen Gläubigern geht.
- Das Bargeschäft muss zusätzlich zu den Voraussetzungen der Vorsatzanfechtung **zu einer gezielten Benachteiligung anderer Gläubiger** führen oder den Empfänger gegenüber anderen gezielt **bevorzugen**.
- Allein dauerhafte Verlustsituation des Schuldners genügt **nicht** für die Annahme der Unlauterkeit.
- Bei Lohnzahlungen lehnt der Senat eine generelle Anbindung an die 30-Tage-Grenze ab und stellt auf den engen zeitlichen Zusammenhang ab.

Quelle: <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>; <https://www.osborneclarke.com/de/insights/bgh-zum-merkmal-der-unlauterkeit-im-rahmen-des-bargeschaeftsprivilegs>

Praxisfolge (Verteidigung): Der Anfechtungsgegner kann sich auf das Bargeschäft berufen, wenn die Transaktion betriebsüblich, gleichwertig und unmittelbar war; der Insolvenzverwalter muss die Unlauterkeit konkret darlegen.

### Beispiel

```
Lieferant verkauft Waren an Schuldner zum Markt-Preis.
Schuldner zahlt sofort bei Lieferung.

→ Bargeschäft § 142 InsO
→ Vorsatzanfechtung scheitert,
 außer der Verwalter weist die Unlauterkeit nach BGH IX ZR 122/23
 positiv nach.
```

## Schritt 5 — Sanierungs-Bemühungen als Verteidigung

Ein belastbares Sanierungskonzept (IDW S 6) mit überwiegender Erfolgsaussicht
kann den Vorsatz iSd § 133 Abs. 1 InsO entkräften. Anforderungen nach
BGH-Linie (vor Ausgabe konkrete Entscheidung über offene Quelle prüfen):

- **Sanierungs-Konzept** mit Aussicht auf Erfolg schließt Vorsatz aus
- **Mindeststandard IDW S 6**
- **Konkrete Maßnahmen**
- **Quantifizierte Erfolgs-Wahrscheinlichkeit**

### Konkrete Anforderungen

- **Sanierungs-Gutachten** schriftlich
- **Realistische Annahmen**
- **Mitwirkung Hauptgläubiger** (z.B. Bank Stundung)
- **Zeit-Plan**

### Bei Lieferanten / Banken

- Aufnahme in Sanierungs-Konzept
- Bewusstsein der Sanierungs-Maßnahmen
- Vergleichs-/Stundungs-Vereinbarung als Sanierungs-Bestandteil

## Schritt 6 — Treuhand-Konstellation

### Treuhand-Sicherheit

- Bei treuhänderischer Sicherheits-Konstellation
- Anfechtungs-festigkeit setzt wirksame Treuhand (offene Treuhand, Bestimmtheit, Aussonderungsrecht) voraus
- Konkrete BGH-Linie (insb. zur Doppeltreuhand) über dejure.org/openjur.de verifizieren

### Sicherheits-Treuhand

- Sicherheits-Übereignung Sicherheits-Abtretung
- Bei gleichwertiger Gegen-Sicherheit
- Anfechtungs-Schutz möglich

## Schritt 7 — Praktische Konstellationen

### Konstellation A — Lieferant erhält späte Zahlung

- Lieferant in Vorkasse-Konstellation
- Schuldner zahlt mit Verzögerung
- Bei Insolvenz-Eröffnung — Anfechtung möglich
- **Verteidigung:** Bargeschäft + üblicher Verlauf

### Konstellation B — Bank erhält Tilgungs-Zahlung

- Bei drohender Insolvenz Schuldner zahlt Bank-Kredit
- Inkongruent: vor Fälligkeit
- Konkrete BGH-Rechtsprechung zur Bankenanfechtung (insb. Konto-Überziehungs-Indizien) über dejure.org verifizieren
- **Verteidigung:** Bei Fälligkeit kongruente Deckung; Bargeschäft nur bei unmittelbarem Austausch; BGH IX ZR 122/23 (05.12.2024) zur Unlauterkeitsprüfung beachten

### Konstellation C — Berater erhält Honorar

- Anwalt / Steuer-Berater erhalten Vor-Honorar
- Bei Krise sensitiv
- **Verteidigung:** Bargeschäft mit klarer Leistungs-Zuordnung

### Konstellation D — Familien-Mitglieder erhalten Zahlungen

- Bei nahe-stehenden Personen § 138 InsO
- **Vermutung Kenntnis** zur Last des Anfechtungs-Gegners
- Schwere Verteidigung

### Konstellation E — Sanierungs-Beratung wird honoriert

- Honorar für Sanierungs-Versuch
- Konkrete BGH-Linie zum Sanierungsberater-Honorar (Bargeschäft, IDW S 6) über offene Quelle verifizieren
- **Verteidigung:** Beratungs-Erfolg-Aussicht IDW S 6; bei Beraterleistungen häufig Bargeschäft, sofern unmittelbarer Leistungs-Austausch dokumentiert

## Schritt 8 — Inkongruenz und Kongruenz

### § 130 InsO Kongruente Deckung

- Bei Fälligkeit
- In den letzten 3 Monaten
- Mit Kenntnis Zahlungs-Unfähigkeit

### § 131 InsO Inkongruente Deckung

- Vor Fälligkeit oder anders als geschuldet
- In den letzten 3 Monaten ohne Kenntnis-Anforderung
- Im 4. bis 6. Monat mit Kenntnis-Anforderung

### Abgrenzung § 133 InsO

- **§ 133 Abs. 1** — 10 Jahre Rückblick, Vermögens-Verschiebungs- und Inkongruenz-Tatbestände
- **§ 133 Abs. 2** — 4 Jahre Rückblick, kongruente Deckungs-/Befriedigungs-Handlungen
- Beide strenger als §§ 130/131: Vorsatz erforderlich, dafür deutlich längere Frist
- **§ 133 plus § 130/131** parallel möglich — Insolvenz-Verwalter wählt stärkste Norm

### Strategie Insolvenz-Verwalter

- Bei Zeitfenster überlappen alle drei prüfen
- Stärkste Anfechtungs-Norm verwenden

## Schritt 9 — Verfahrens-Aspekte

### Anfechtungs-Klage Insolvenz-Verwalter

- Gegen Anfechtungs-Gegner
- Klage am Insolvenz-Gericht oder AG/LG je Streitwert
- Forderungs-Inhalt: Rückgewähr Bereicherungs-Recht

### Verjährung Anfechtungs-Anspruch

- Drei Jahre seit Insolvenz-Eröffnung § 146 InsO
- Beweis-Sicherung wichtig

### Vergleich

- Häufig vor Klage
- Vergleichs-Quote 30-70 Prozent der Anfechtungs-Forderung

## Schritt 10 — Verteidigungs-Strategie Anfechtungs-Gegner

### Schritt 10a — Beweis-Lücke

- **Vorsatz Schuldner** bestritten
- **Kenntnis** bestritten
- **Indizien** entkräften

### Schritt 10b — Bargeschäft-Argument

- Leistungs-Austausch dokumentieren
- 30-Tage-Frist nachweisen
- Gleichwertigkeit darstellen

### Schritt 10c — Sanierungs-Bezug

- Sanierungs-Konzept-Beweis
- Konkrete Maßnahmen-Dokumentation
- Erfolgs-Wahrscheinlichkeit Sachverständigen-Gutachten

### Schritt 10d — Treuhand / Sicherheit

- Vertraglich klar dokumentiert
- Wirksamkeit prüfen

### Schritt 10e — Verfahrensrechtliche Punkte

- Verjährungs-Einwand
- Beweislast-Verteilung
- Hilfs-Beweisanträge

### Schritt 10f — Vergleichs-Verhandlung

- Bei schwacher Position
- Bei Streit-Wert-Reduktion sinnvoll
- Quoten-Verhandlung

## Schritt 11 — Versicherungs-Schutz

### Berufs-Haftpflicht

- Bei Anwalts-Anfechtungen
- Bei Berater-Anfechtungen
- Vor Klage Versicherer informieren

### D&O-Versicherung

- Geschäftsführer als Anfechtungs-Beteiligter
- Bei verdacht "selbst-Bedienung"

## Schritt 12 — Praktische Tipps Schuldner-Verteidigung

### Dokumentations-Standards

- Sanierungs-Konzept zeitnah erstellen
- IDW S 6 Mindest-Standard
- Mit Gläubiger-Kommunikation dokumentieren
- Zahlungs-Anlässe dokumentieren

### Compliance

- Bei Krise vorzeitig Anwaltsberatung
- Skill `mandat-triage-insolvenzrecht`
- Sanierungsmoderation § 94 StaRUG erwägen

### Bei Anfechtungs-Forderung

- Sofort Beweis-Sammlung
- Akten der Gegenseite einsehen
- Sachverständigen-Vorabbewertung

## Verzahnung mit anderen Skills

- `mandat-triage-insolvenzrecht` — Einstieg
- `anfechtungsrechte-pruefen` — andere Anfechtungs-Tatbestände
- `sanierungsmoderation-94-starug` — Sanierungs-Anschluss
- `do-versicherung-manager-haftung` — Geschäftsführer-Schutz
- `liquiditaetsvorschau-insolvenzrechtlich` — Zahlungs-Unfähigkeits-Prüfung
- `konzerninsolvenz-koordination` — Inter-Company-Anfechtung

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Vorsatzanfechtung § 133 InsO pruefen und Anfechtungsschreiben erstellen | Anfechtungsschreiben nach Pruefschema; Template unten |
| Variante A — Anfechtungsfrist 10 Jahre abgelaufen | Andere Anfechtungsgrundlagen pruefen §§ 129 ff InsO |
| Variante B — Anfektungsgegner zahlungsunfaehig | Wirtschaftlichkeitspruefung der Anfechtung; ggf. verzichten |
| Variante C — Glaeubigeranfechtung nach AnfG ausserhalb Insolvenz | AnfG als Alternative wenn Insolvenz noch nicht eroeffnet |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Ausgabe

- `vorsatzanfechtung-{az}.md` mit Sachverhalts-Klassifikation Tatbestands-Prüfung Verteidigungs-Strategie
- Beweis-Inventar
- Sachverständigen-Auftrag
- Vergleichs-Strategie
- Klage-/Antwort-Schriftsatz
- Frist im Fristenbuch (Verjährung drei Jahre)


## Quellen

- InsO §§ 129 130 131 132 133 138 142 143 146
- **BGH IX ZR 122/23 vom 05.12.2024** — Unlauterkeit beim Bargeschäft § 142 InsO
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=05.12.2024&Aktenzeichen=IX+ZR+122/23>
- **BGH IX ZR 129/22 vom 18.04.2024** — Neuausrichtung Vorsatzanfechtung § 133 InsO
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH IX ZR 239/22 vom 18.04.2024** — Anfechtung wegen gesellschafterähnlicher Stellung
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+239/22>
- Ältere Linie (BGH IX ZR 72/20 vom 06.05.2021 — Grundsatzentscheidung Neuausrichtung) und § 138-Konstellationen vor Ausgabe über dejure.org/openjur.de verifizieren.
- IDW S 6 (Sanierungskonzept)
- Literatur und Kommentarstellen nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


## Output-Template Anfechtungsschreiben § 133 InsO

**Adressat:** Anfechtungsgegner — Tonfall: scharf-fristsetzend

```
[KANZLEI] [DATUM]

Insolvenzverfahren [FIRMA]
Amtsgericht [ORT], Az. [XX IN YY/ZZ]

Insolvenzanfechtung nach § 133 Abs. 1 InsO

Sehr geehrte Damen und Herren,

ich bin als Insolvenzverwalter im obengenannten Verfahren bestellt.

Hiermit fechte ich folgende Zahlungen nach § 133 Abs. 1 InsO an:

Datum Betrag Verwendungszweck
[DATUM] EUR [BETRAG] [ZWECK]
[...]

Begruendung Benachteiligungsvorsatz:
Die Schuldnerin war zum Zeitpunkt der Zahlungen zahlungsunfaehig. Dies ergibt sich aus:
[Konkrete Bedrohungslage: Ratenzahlungsangebote, Mahnungen, Vollstreckungen, Zahlungseinstellungen]

Begruendung Kenntnis des Anfechtungsgegners:
[Indizien: Stundungsanfragen, Mahnstufen, Kenntnis ZU-Anzeichen]

Ich fordere Sie auf, den Gesamtbetrag von EUR [BETRAG] zzgl. Zinsen
(§ 143 Abs. 1 i.V.m. § 819 BGB) bis zum [DATUM, 14 Tage] auf das
Massekonto [IBAN] zurueckzuueberweisen.

Nach fruchtlosem Ablauf dieser Frist werde ich Klage erheben.

[UNTERSCHRIFT INSOLVENZVERWALTER]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.



## Quellenregel

Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Rechtsprechung aus offenen Quellen (dejure.org, openjur.de, bundesgerichtshof.de) mit Gericht, Datum, Aktenzeichen, Randnummer.

## 4. `zahlungsunfaehigkeit-pruefung-17-inso`

**Fokus:** Erstellt ein strukturiertes Prüfgutachten zum Eröffnungsgrund der Zahlungsunfähigkeit nach § 17 InsO. Berechnet den Liquiditätsstatus zum Stichtag, wendet das 10-%-/3-Wochen-Schema des BGH an und würdigt Indizien der Zahlungseinstellung. Lädt, wenn der Nutzer Zahlungsunfähigkeit, Liquiditätsstatus, Insolvenzeröffnungsgrund oder § 17 InsO prüfen möchte.

# Gerichtsfeste Prüfung des Eröffnungsgrundes § 17 InsO (Zahlungsunfähigkeit)

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gerichtsfeste Prüfung des Eröffnungsgrundes § 17 InsO (Zahlungsunfähigkeit)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill führt eine strukturierte, an der BGH-Rechtsprechung und IDW S 11 ausgerichtete
Prüfung durch, ob zum maßgeblichen Stichtag Zahlungsunfähigkeit i.S.d. § 17 InsO vorliegt.
Das Ergebnis ist ein dokumentierbares Gutachten, das vor Insolvenzgerichten, im Anfechtungs-
und Haftungsprozess sowie gegenüber dem vorläufigen Insolvenzverwalter Stand hält.

## Eingaben

Der Nutzer stellt folgende Informationen bereit (fehlende Angaben werden abgefragt):

- **Stichtag**: konkretes Datum der Prüfung (i.d.R. Tag der Antragstellung oder ein früherer
 Zeitpunkt für Haftungszwecke)
- **Fällige Verbindlichkeiten (Passiva I)**: Betrag und Gläubiger aller zum Stichtag fälligen,
 nicht gestundeten Verbindlichkeiten
- **Liquide Mittel (Aktiva I)**: Kassenbestand, Bankguthaben, sofort verwertbare Aktiva
- **Zuflüsse innerhalb von 3 Wochen (Aktiva II. Stufe)**: konkret zu erwartende Zahlungseingänge
 aus bestehenden Forderungen, zugesagten Kreditlinien u.Ä.
- **Stundungsvereinbarungen**: ob schriftlich dokumentiert, glaubhaft und ernstlich gewollt
- **Indizien** (soweit vorhanden): Lohnrückstände, SV-Beitragsrückstände, Stundungsbitten,
 Wechselproteste, Pfändungsmaßnahmen, Insolvenzanträge anderer Gläubiger

## Rechtlicher Rahmen

### Gesetzliche Grundlagen

**§ 17 Abs. 1 InsO** bestimmt Zahlungsunfähigkeit als allgemeinen Eröffnungsgrund.

**§ 17 Abs. 2 S. 1 InsO** definiert: Der Schuldner ist zahlungsunfähig, wenn er nicht in der
Lage ist, die fälligen Zahlungspflichten zu erfüllen.

**§ 17 Abs. 2 S. 2 InsO** normiert die gesetzliche Vermutung: Zahlungsunfähigkeit ist in der
Regel anzunehmen, wenn der Schuldner seine Zahlungen eingestellt hat.

### Rechtsprechung (Pflichtpinpoints; Az. und Datum vor Ausgabe über dejure.org / openjur.de verifizieren)

**10-%-/3-Wochen-Schema:** Grundlegende BGH-Linie: Zahlungsunfähigkeit liegt vor, wenn der
Schuldner zum Stichtag seine fälligen Verbindlichkeiten nicht zu mindestens 90 % erfüllen kann
und die Lücke nicht innerhalb von 3 Wochen zu schließen ist. Eine Unterdeckung von weniger als
10 % begründet lediglich eine Zahlungsstockung, wenn die Lücke in absehbarer Zeit beseitigt
werden kann. Ab 10 % ist auch bei kurzfristiger Behebbarkeit Zahlungsunfähigkeit anzunehmen,
sofern die Unterdeckung mehr als 3 Wochen andauert. Konkretes Az. der grundlegenden Entscheidung vor Ausgabe in offener Quelle prüfen.

**Indizienkatalog § 17 Abs. 2 S. 2 InsO:** Als Indizien gelten insbesondere verspätete Lohnzahlungen, offene Sozialversicherungsbeiträge, erfolglose Stundungsbitten gegenüber Gläubigern, Wechselproteste, Pfändungsmaßnahmen von Gläubigern, Insolvenzanträge anderer Gläubiger sowie der eigene Insolvenzantrag des Schuldners. Die Zahlungseinstellung setzt kein allgemeines Unvermögen voraus; es genügt, dass der Schuldner den wesentlichen Teil seiner Verbindlichkeiten nicht mehr zahlt.

**Stundungen in der Liquiditätsbilanz:** In die Passiva I sind nur Verbindlichkeiten aufzunehmen, die tatsächlich fällig und nicht wirksam gestundet sind. Echter Stundung (beiderseitig gewollt, glaubhaft dokumentiert) ist Folge zu geben; sie beseitigt die Fälligkeit. Erzwungene oder faktische Stundungen — d.h. bloßes Dulden des Zahlungsverzugs durch den Gläubiger ohne Einigung — beseitigen die Fälligkeit nicht. Im Anfechtungsprozess trifft den Schuldner die Darlegungs- und Beweislast für das Vorliegen einer echten Stundungsvereinbarung.

**Verschulden bei Antragspflichtverletzung:** Kenntnis der Zahlungsunfähigkeit ist zu bejahen, wenn dem Schuldner die die Zahlungsunfähigkeit begründenden Tatsachen bekannt waren oder bekannt sein mussten. Berufung auf Unkenntnis schützt nicht.

**Aktuelle Entwicklungen (Stand Mai 2026):**
- **BGH IX ZR 129/22 vom 18.04.2024** — bei objektiv festgestellter Zahlungsunfähigkeit muss der Verwalter im Vorsatzanfechtungs-Prozess konkret darlegen, dass der Schuldner mit dauerhafter Nichtbefriedigung anderer Gläubiger gerechnet hat. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.04.2024&Aktenzeichen=IX+ZR+129/22>
- **BGH II ZR 206/22 vom 23.07.2024** — fortwirkende Haftung des ausgeschiedenen Geschäftsführers. <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.07.2024&Aktenzeichen=II+ZR+206/22>
- **BGH IV ZR 66/25 vom 19.11.2025** — D&O-Wissentlichkeitsausschluss erfordert positive Kenntnis pro Pflichtverletzung.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### IDW-Standard

**IDW S 11 (Stand 12.08.2021), Tz. 31 ff.** regelt die Beurteilung des Eröffnungsgrundes der
Zahlungsunfähigkeit durch den Sachverständigen oder Wirtschaftsprüfer: Aufzustellen ist ein
Liquiditätsstatus auf den Prüfungsstichtag, der liquide Mittel (Aktiva I, ggf. ergänzt um Aktiva II)
den fälligen Verbindlichkeiten (Passiva I) gegenüberstellt. Übersteigen Passiva I die Aktiva I und II
um mehr als 10 %, ist bei fehlender kurzfristiger Beseitigungsperspektive Zahlungsunfähigkeit
festzustellen (Tz. 31–37). IDW S 11 Tz. 16 f. zur Abgrenzung gegenüber Zahlungsstockung und
Überschuldung.

## Ablauf

Das Prüfgutachten folgt diesen sieben Schritten:

**Schritt 1 – Stichtagsbestimmung**
Festlegung des maßgeblichen Prüfungsstichtags. Bei Antragspflicht (§ 15a InsO) ist dies der Eintritt
der Zahlungsunfähigkeit; im Anfechtungsrecht (§§ 129 ff. InsO) kann ein früherer Zeitpunkt relevant
sein. Alle weiteren Prüfungsschritte erfolgen stichtagsbezogen.

**Schritt 2 – Erfassung fälliger Verbindlichkeiten (Passiva I)**
Vollständige Erfassung aller am Stichtag fälligen, nicht wirksam gestundeten Verbindlichkeiten.
Einzubeziehen sind: Lieferantenverbindlichkeiten, Darlehensverbindlichkeiten (inkl. gekündigter
oder fälliger Teile), Lohn- und Gehaltsrückstände, Sozialversicherungsbeiträge (SV-Beiträge),
Steuerschulden mit abgelaufener Zahlungsfrist, sonstige fällige Forderungen. Stundungen sind auf
ihre Echtheit zu prüfen (BGH-Linie zur echten Stundung; konkrete Az. vor Ausgabe verifizieren).

> **Aussetzung der Vollziehung (§ 361 AO / § 69 FGO) ist keine Stundung.** AdV-Verfügungen
> hemmen nur die Vollziehung, lassen die Fälligkeit der Steuerforderung aber unberührt. Im
> Liquiditätsstatus bleiben AdV-Beträge **Passiva I**, soweit nicht zusätzlich eine
> schriftliche Stundung nach § 222 AO mit Verschiebung der Fälligkeit über den Stichtag
> hinaus vorliegt. Sonst wird die Liquiditätslücke unterzeichnet und es droht eine
> falsche "nicht zahlungsunfähig"-Feststellung.

**Schritt 3 – Aktiva-Erfassung**
- *Aktiva I*: sofort verfügbare liquide Mittel zum Stichtag (Kassenbestand, Bankguthaben,
 debitorische Konten ohne Ausschöpfung des Rahmens)
- *Aktiva II. Stufe* (innerhalb 3 Wochen zugehend): konkret erwartete Zahlungseingänge aus
 bestehenden Forderungen (nach vorsichtiger Einschätzung der Ausfallwahrscheinlichkeit),
 freie Kreditlinien, erwartete Darlehensauszahlungen mit schriftlicher Zusage

**Schritt 4 – Aufstellung des Liquiditätsstatus**
Gegenüberstellung in tabellarischer Form:

```
Aktiva I (sofort verfügbar) EUR ______
+ Aktiva II (innerhalb 3 Wochen) EUR ______
= Summe liquide Mittel EUR ______

./. Passiva I (fällige Verbindlichkeiten) EUR ______

= Unterdeckung / Überdeckung EUR ______
```

**Schritt 5 – Quotenberechnung**
Berechnung der Liquiditätsquote:

 Quote = (Summe liquide Mittel / Passiva I) × 100

Eine Quote ≥ 100 % schließt Zahlungsunfähigkeit aus. Eine Quote zwischen 90 % und 99 %
(Unterdeckung < 10 %) begründet bei kurzfristiger Behebbarkeit nur Zahlungsstockung.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Unterdeckung < 10 % und Beseitigung innerhalb 3 Wochen absehbar → Zahlungsstockung,
 keine Zahlungsunfähigkeit
- Unterdeckung < 10 %, aber Beseitigung nicht innerhalb 3 Wochen → Zahlungsunfähigkeit
- Unterdeckung ≥ 10 % → Zahlungsunfähigkeit unabhängig von der Perspektive der Beseitigung

**Schritt 7 – Würdigung der Indizien für Zahlungseinstellung (§ 17 Abs. 2 S. 2 InsO)**
Liegen rechnerisch Zweifelsfälle vor oder fehlen vollständige Daten, sind die Indizien
nach BGH-Linie heranzuziehen: verspätete Lohnzahlungen, offene SV-Beiträge, erfolglose
Stundungsbitten, Wechselproteste, Pfändungen, Insolvenzanträge anderer Gläubiger, eigener
Antrag. Häufen sich mehrere Indizien, ist Zahlungseinstellung und damit Zahlungsunfähigkeit
zu bejahen. Die Vermutung des § 17 Abs. 2 S. 2 InsO ist widerlegbar; die Beweislast liegt beim Schuldner. Konkrete Aktenzeichen der einschlägigen BGH-Entscheidungen vor Ausgabe über offene Quellen verifizieren.

## Ausgabeformat

Das Gutachten wird im Gutachtenstil formuliert:

1. **Sachverhalt** (kurze Sachverhaltsdarstellung)
2. **Rechtliche Grundlagen** (§ 17 Abs. 2 S. 1 und S. 2 InsO, BGH-Schema)
3. **Liquiditätsstatus** (Tabelle nach Schritt 4)
4. **Quotenberechnung** (Schritt 5)
5. **Subsumtion** (Schritt 6 mit Zwischenergebnis)
6. **Indizienanalyse** (Schritt 7, wenn relevant)
7. **Ergebnis** (Feststellung: Zahlungsunfähigkeit liegt vor / liegt nicht vor / Zahlungsstockung)
8. **Quellennachweis** (BGH-Entscheidungen, IDW S 11, Kommentare mit Randnummern)

## Beispiel

### Sachverhalt

Die Muster GmbH (Schuldnerin) weist zum Stichtag 31.03.2025 folgende Situation auf:

**Variante A** (Zahlungsstockung):
- Liquide Mittel (Aktiva I): 25.000 EUR (Bankguthaben)
- Zuflüsse innerhalb 3 Wochen (Aktiva II): 0 EUR (keine gesicherten Eingänge)
- Fällige Verbindlichkeiten (Passiva I): 320.000 EUR

**Variante B** (Zahlungsunfähigkeit):
- Liquide Mittel (Aktiva I): 40.000 EUR
- Zuflüsse innerhalb 3 Wochen (Aktiva II): 0 EUR
- Fällige Verbindlichkeiten (Passiva I): 320.000 EUR
- Keine Aussicht auf Schließung der Lücke innerhalb von 3 Wochen

---

### Subsumtion Variante A

**Liquiditätsstatus:**

```
Aktiva I 25.000 EUR
+ Aktiva II 0 EUR
= Summe liquide Mittel 25.000 EUR
./. Passiva I 320.000 EUR
= Unterdeckung 295.000 EUR
```

**Quote:** 25.000 / 320.000 × 100 = **7,8 %**

Die Unterdeckung beträgt 92,2 % und übersteigt damit nicht die 10-%-Schwelle im Sinne der ständigen BGH-Linie (konkrete Az. vor Ausgabe verifizieren).

**Zwischenergebnis:** Die Unterdeckung liegt unter 10 %. Es ist zu prüfen, ob die Lücke von
295.000 EUR innerhalb von 3 Wochen zu schließen ist. Fehlen konkrete Zuflüsse, liegt nach Ablauf
der 3-Wochen-Frist Zahlungsunfähigkeit vor. Bestehen hinreichend konkrete Zuflusserwartungen
(Aktiva II), ist lediglich Zahlungsstockung anzunehmen; die Prüfung ist in 3 Wochen zu wiederholen.

---

### Subsumtion Variante B

**Liquiditätsstatus:**

```
Aktiva I 40.000 EUR
+ Aktiva II 0 EUR
= Summe liquide Mittel 40.000 EUR
./. Passiva I 320.000 EUR
= Unterdeckung 280.000 EUR
```

**Quote:** 40.000 / 320.000 × 100 = **12,5 %**

Die Unterdeckung beläuft sich auf 87,5 % und übersteigt die 10-%-Schwelle.

Nach ständiger BGH-Linie ist bei einer Unterdeckung von ≥ 10 % Zahlungsunfähigkeit anzunehmen, sobald keine kurzfristige Beseitigung in Sicht ist (konkrete Az. vor Ausgabe verifizieren). Die Schuldnerin kann keine Zuflüsse innerhalb von 3 Wochen nachweisen.
Die Unterdeckung wird nicht innerhalb von 3 Wochen beseitigt.

**Ergebnis:** Die Muster GmbH ist zum Stichtag 31.03.2025 zahlungsunfähig i.S.d. § 17 Abs. 2
S. 1 InsO. Die Pflicht zur Stellung eines Insolvenzantrags nach § 15a InsO ist ausgelöst.

## Risiken und typische Fehler

**1. Faktische Stundung statt echter Stundung**
Häufig wird ein bloßes Nichtklagen des Gläubigers als Stundung gewertet. Nach ständiger BGH-Linie (konkrete Az. vor Ausgabe verifizieren) beseitigt eine erzwungene oder faktische Duldung des Zahlungsverzuges die Fälligkeit nicht. Nur beiderseitig vereinbarte, schriftlich belegbare echte Stundungen dürfen aus den Passiva I herausgenommen werden. Ohne Dokumentation besteht das Risiko, dass das Insolvenzgericht oder ein Sachverständiger die Fälligkeit gleichwohl bejaht und eine frühere Zahlungsunfähigkeit feststellt.

**2. Vergessene Sozialversicherungsbeiträge**
SV-Beiträge werden in der Praxis häufig nicht in die Passiva I aufgenommen, obwohl sie
gesetzlich sofort fällig sind (§ 23 SGB IV). Rückständige SV-Beiträge sind zugleich ein gewichtiges
Indiz für die Zahlungseinstellung iSd § 17 Abs. 2 S. 2 InsO (st. BGH-Linie; Az. vor Ausgabe verifizieren). Fehler hier führen sowohl zur Unterschätzung der Passiva I als auch zur Übersehung eines
Zahlungseinstellungsindizes.

**3. Unzulässige Berücksichtigung künftiger Forderungen (Aktiva III. Stufe)**
Erlöse aus erst künftig abzuschließenden Verträgen, erhoffte Investorengelder ohne verbindliche
Zusage oder hypothetische Verwertungserlöse gehören nicht in die Liquiditätsbilanz (Aktiva I oder II),
sondern allenfalls in eine Liquiditätsplanung (Aktiva III. Stufe). Ihre Einbeziehung in die
Liquiditätsbilanz ist methodisch unzulässig und führt zu einer unzutreffend negativen Feststellung
Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

**4. Stichtagsverschiebung im Haftungskontext**
Im Anfechtungs- und Haftungsprozess ist nicht der Antragstag, sondern der tatsächliche Eintritt
der Zahlungsunfähigkeit maßgeblich. Wird der Stichtag zu spät angesetzt, werden Haftungs-
oder Anfechtungszeiträume unzutreffend verkürzt (Schmerbach, in: K. Schmidt, InsO, 20. Aufl.
2023, § 17 Rn. 32).

**5. Fehlende Indiziengesamtwürdigung**
Einzelne Indizien (z.B. nur eine verspätete Lohnzahlung) begründen für sich allein noch keine
Zahlungseinstellung. Erst das Zusammentreffen mehrerer Indizien aus dem Katalog des BGH
IX ZR 81/06 Rn. 36 ff. rechtfertigt die Vermutung des § 17 Abs. 2 S. 2 InsO. Eine isolierte
Betrachtung führt zu Fehlsubsumtionen.

## Quellenpflicht

Jedes auf diesem Skill basierende Gutachten muss mindestens folgende Quellen ausweisen:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Schmerbach, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 Rn. 5 ff., 22 ff., 32
- IDW S 11 (Stand 12.08.2021), Tz. 16 f., 31–37

---

*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*


## Triage — ZU-Pruefung § 17 InsO

Bevor losgelegt wird, klaere:

1. **Liquiditaetsstatus erstellen?** Faellige und nicht zahlbare Verbindlichkeiten vs. liquide Mittel (Direct-Method).
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Zahlungsstockung oder ZU?** Zahlungsstockung: voruibergehend, Beseitigung absehbar. ZU: strukturell, keine Beseitigung ohne Aussenfinanzierung.
4. **Datum festlegen?** Tag-genaue Bestimmung fuer Anfechtungsfristen §§ 130-133 InsO.
5. **Antragspflicht?** § 15a InsO Frist 3 Wochen ab ZU-Eintritt.

## Output-Template ZU-Memo (Liquiditaetsstatus)

**Adressat:** Intern / Gericht — Tonfall: sachlich-betriebswirtschaftlich

```
LIQUIDITAETSSTATUS (§ 17 InsO-Pruefung)
Gesellschaft: [FIRMA] Stichtag: [DATUM]

FAELLIGE VERBINDLICHKEITEN:
- Lieferantenverbindlichkeiten: EUR [BETRAG]
- Steuern und SV: EUR [BETRAG]
- Bankdarlehen (faellig): EUR [BETRAG]
- Sonstige: EUR [BETRAG]
GESAMT FAELLIG: EUR [SUMME]

LIQUIDE MITTEL:
- Kassabetrag: EUR [BETRAG]
- Bankguthaben: EUR [BETRAG]
- Innerhalb 3 Wochen eingehende Zahlungen: EUR [BETRAG]
GESAMT LIQUIDE: EUR [SUMME]

LIQUIDITAETSLUECKE: EUR [SUMME] = [X%] der faelligen Verbindlichkeiten
ERGEBNIS: [Zahlungsunfaehigkeit i.S.d. § 17 InsO: JA / NEIN / ZAHLUNGSSTOCKUNG]
```
