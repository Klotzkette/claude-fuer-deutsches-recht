---
name: schweigen-erklaerungswert-stellvertretung
description: "Schweigen Erklaerungswert Stellvertretung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schweigen Erklaerungswert Stellvertretung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schweigen Erklaerungswert Stellvertretung** im Plugin Bgb At Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schweigen-und-erklaerungswert` | Prüft den Erklärungswert des Schweigens im BGB: Schweigen als Ausnahme von der Regel keine Willenserklärung, kaufmännisches Bestätigungsschreiben, vertraglich vereinbarter Erklärungswert, § 362 HGB und Sonderfälle im Verbraucherrecht. Klausurfall mit Subsumtionsraster. |
| `stellvertretung-routing-paragraphen-164-181` | Routing-Skill zur Stellvertretung nach §§ 164 bis 181 BGB: Vollmachtserteilung und -erlöschen, Offenkundigkeit des Handelns im fremden Namen, Duldungs- und Anscheinsvollmacht, Vertreter ohne Vertretungsmacht §§ 177 bis 179 BGB und Insichgeschäft § 181 BGB. Output: Prüfpfad und Verweis auf Teilskills. |
| `taeuschung-drohung-paragraph-123` | Klausurfall zur Anfechtung wegen arglistiger Täuschung oder widerrechtlicher Drohung nach § 123 BGB: Täuschungshandlung und Kausalität, Drohung mit dem versprochenen empfindlichen Übel, Anfechtungsfrist ein Jahr nach § 124 BGB und Ausschluss bei Täuschung durch Dritte. |

## Arbeitsweg

Im Plugin Bgb At Pruefer gilt für **Schweigen Erklaerungswert Stellvertretung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schweigen-und-erklaerungswert`

**Fokus:** Prüft den Erklärungswert des Schweigens im BGB: Schweigen als Ausnahme von der Regel keine Willenserklärung, kaufmännisches Bestätigungsschreiben, vertraglich vereinbarter Erklärungswert, § 362 HGB und Sonderfälle im Verbraucherrecht. Klausurfall mit Subsumtionsraster.

# Schweigen und Erklärungswert

## Mandantenfall

- Kaufmann erhält Bestätigungsschreiben und schweigt — gilt der Vertragsinhalt des Schreibens als vereinbart?
- Vertragsklausel: Ausbleiben der Antwort innerhalb von 14 Tagen gilt als Zustimmung — wirksam?
- Klausurkonstellation: Verbraucher erhält unbestellte Ware mit dem Hinweis, Schweigen sei Annahme.

## Erste Schritte

1. Grundregel: Schweigen ist grundsätzlich keine Willenserklärung — kein Rechtsbindungswille.
2. Ausnahmen prüfen: Gesetz, Vertrag oder Handelsbrauch können Schweigen Erklärungswert geben.
3. Kaufmännisches Bestätigungsschreiben: Erhält Kaufmann ein Bestätigungsschreiben und schweigt — wesentliche Inhalte gelten als angenommen (§ 346 HGB analog, Gewohnheitsrecht).
4. Vertraglich vereinbarter Erklärungswert: § 305c BGB-Überraschungsklausel und AGB-Inhaltskontrolle.
5. § 362 HGB: Kaufmann muss auf Antragsschreiben reagieren, wenn er Geschäfte dieser Art besorgt.
6. Verbraucherschutz: Unbestellte Ware begründet keinen Anspruch auf Bezahlung (§ 241a BGB).

## Rechtsrahmen

- §§ 116 ff. BGB: Willenserklärung setzt Rechtsbindungswillen voraus — Schweigen in der Regel keine WE.
- § 241a BGB: Unbestellte Leistungen — Schweigen begründet kein Schuldverhältnis.
- § 362 HGB: Kaufmännische Reaktionspflicht auf Antragsschreiben.
- §§ 305c und 307 BGB: AGB-Kontrolle bei vertraglich vereinbartem Erklärungswert des Schweigens.
- § 346 HGB: Handelsbräuche — Grundlage für kaufmännisches Bestätigungsschreiben.

## Prüfraster

1. Grundregel beachten: Ist Schweigen nach allgemeinen Grundsätzen keine Willenserklärung?
2. Gesetzliche Ausnahme: § 362 HGB oder § 241a BGB einschlägig?
3. Kaufmännisches Bestätigungsschreiben: Beide Kaufleute, vorhergehende Verhandlung, Schreiben zeitnah nach Vertragsschluss?
4. Vertraglich vereinbarter Erklärungswert: AGB-Kontrolle nach §§ 305c und 307 BGB?
5. Schweigen auf Vertragsangebot: Kein Annahmewert ohne Ausnahmegrundlage.
6. Verbraucher: § 241a BGB schließt Bezahlungspflicht aus.
7. Ergebnis: Schweigen als Zustimmung, Ablehnung oder bedeutungslos?

## Typische Fallstricke

- Kaufmännisches Bestätigungsschreiben gilt nur bei vorherigen Verhandlungen, nicht als erstes Angebot.
- § 241a BGB schützt Verbraucher nur — im B2B-Bereich andere Maßstäbe.
- AGB-Klauseln mit Schweigen als Zustimmung müssen § 307 BGB standhalten.
- Bloßes Unterlassen der Antwort auf ein Angebot ist nie Annahme im Verbraucherrecht.

## Output

- Gutachtenstil-Abschnitt zum Erklärungswert des Schweigens
- Entscheidungsbaum: Grundregel → gesetzliche Ausnahme → vertragliche Ausnahme
- Prüfampel: Schweigen als WE / keine WE / AGB-Problem
- Klausurlösungsskizze mit kaufmännischem Bestätigungsschreiben

## Quellen

- [§ 241a BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__241a.html)
- [§ 116 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__116.html)
- [§ 305c BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__305c.html)
- [dejure.org § 241a BGB](https://dejure.org/gesetze/BGB/241a.html)
- [dejure.org § 362 HGB](https://dejure.org/gesetze/HGB/362.html)

## Vertiefung

### Kaufmännisches Bestätigungsschreiben im Detail

Das kaufmännische Bestätigungsschreiben (kfm. BS) ist Gewohnheitsrecht: Nach Vertragsverhandlungen
bestätigt eine Seite den Vertragsinhalt schriftlich. Der Empfänger muss widersprechen, wenn der
Inhalt nicht dem Vereinbarten entspricht. Ohne Widerspruch gilt der Inhalt als vereinbart.

Voraussetzungen: (1) Beide Seiten Kaufleute, (2) vorangegangene Vertragsverhandlungen,
(3) Bestätigungsschreiben zeitnah nach Abschluss, (4) Inhalt nicht evident falsch.

### Schweigen als Annahme in AGB

AGB-Klauseln, die Schweigen als Zustimmung werten, unterliegen der Inhaltskontrolle nach § 307 BGB.
Im Verbraucherbereich sind solche Klauseln regelmäßig unwirksam (§ 308 Nr. 5 BGB).

### Klausur-Checkliste Schweigen

- Grundregel beachtet: Schweigen ist keine Willenserklärung?
- Ausnahme: § 362 HGB, § 241a BGB oder kaufmännisches Bestätigungsschreiben?
- Kfm. BS: Beide Kaufleute, vorangegangene Verhandlungen, zeitnah?
- Vertraglich vereinbarter Erklärungswert: AGB-Kontrolle nach § 307 BGB?
- Verbraucher: § 241a BGB schließt Zahlungspflicht bei unbestellter Ware aus?

## 2. `stellvertretung-routing-paragraphen-164-181`

**Fokus:** Routing-Skill zur Stellvertretung nach §§ 164 bis 181 BGB: Vollmachtserteilung und -erlöschen, Offenkundigkeit des Handelns im fremden Namen, Duldungs- und Anscheinsvollmacht, Vertreter ohne Vertretungsmacht §§ 177 bis 179 BGB und Insichgeschäft § 181 BGB. Output: Prüfpfad und Verweis auf Teilskills.

# Stellvertretung — Routing §§ 164 bis 181 BGB

## Mandantenfall

- Mitarbeiter schließt ohne ausdrückliche Vollmacht Vertrag ab — Vollmacht, Duldungs- oder Anscheinsvollmacht?
- Prokurist überschreitet seine Vollmacht — §§ 177 bis 179 BGB oder Missbrauch der Vertretungsmacht?
- Klausurkonstellation: Komplexes Stellvertretungsproblem mit mehreren Fragen — Routing zum richtigen Teilskill.

## Erste Schritte

1. Handeln in fremdem Namen prüfen: Offenkundigkeit nach § 164 Abs. 1 BGB gegeben?
2. Vollmacht identifizieren: Innen- oder Außenvollmacht, Prokura, gesetzliche Vertretung?
3. Vollmachtsumfang: Reicht die Vollmacht für das konkrete Geschäft aus?
4. Bei fehlender Vollmacht: Duldungs- oder Anscheinsvollmacht als Rechtsscheintatbestand?
5. Vollmachtsmissbrauch: Handeln im Außenverhältnis mit Vollmacht, aber gegen Innenverhältnis?
6. Vertreter ohne Vertretungsmacht: §§ 177 bis 179 BGB — schwebende Unwirksamkeit und Haftung.

## Rechtsrahmen

- § 164 BGB: Stellvertretung — Handeln im fremden Namen mit Vertretungsmacht.
- § 167 BGB: Vollmachtserteilung — Innen- und Außenvollmacht.
- § 168 BGB: Erlöschen der Vollmacht.
- §§ 177 bis 179 BGB: Vertretung ohne Vertretungsmacht und Haftung des Vertreters.
- § 181 BGB: Insichgeschäft — Selbstkontrahieren und Mehrfachvertretung.

## Prüfraster

1. Offenkundigkeit (§ 164 Abs. 1 BGB): Im fremden Namen oder im eigenen Namen gehandelt?
2. Vollmacht vorhanden: Innen- oder Außenvollmacht, Prokura oder gesetzliche Vertretung?
3. Vollmachtsumfang: Geschäft vom Umfang der Vollmacht gedeckt?
4. Duldungs- oder Anscheinsvollmacht: Rechtsscheintatbestand und Zurechenbarkeit?
5. Vollmachtsmissbrauch: Kenntnis/Kennenmüssen des Dritten vom Innenverhältnis-Verstoß?
6. § 177 BGB: Genehmigung schwebend unwirksamen Vertreterhandelns?
7. § 179 BGB: Haftung des vollmachtlosen Vertreters gegenüber Drittem?
8. § 181 BGB: Insichgeschäft — Ausnahmen beachten?

## Typische Fallstricke

- Offenkundigkeit nach § 164 BGB ist Voraussetzung — Namensnennung nicht immer erforderlich.
- Duldungsvollmacht setzt voraus, dass der Vertretene das Handeln kannte und duldete.
- Anscheinsvollmacht erfordert, dass der Vertretene das Erscheinungsbild hätte erkennen und verhindern können.
- § 181 BGB ist abdingbar durch ausdrückliche Gestattung — Ausnahme prüfen.

## Output

- Routing-Schema: Vollmacht vorhanden → Umfang → Missbrauch → vollmachtloser Vertreter
- Verweis auf Teilskills: vollmacht-erteilung-umfang-erloeschen, duldungs-anscheinsvollmacht, insichgeschaeft-paragraph-181
- Prüfampel: Vertretungswirkung eingetreten / schwebend unwirksam / Haftung des Vertreters
- Klausurlösungsskizze mit vollständigem Stellvertretungspfad

## Quellen

- [§ 164 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__164.html)
- [§ 167 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__167.html)
- [§ 179 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [dejure.org § 164 BGB](https://dejure.org/gesetze/BGB/164.html)
- [dejure.org § 181 BGB](https://dejure.org/gesetze/BGB/181.html)

## Vertiefung

### Prüfungsreihenfolge Stellvertretung

Empfohlene Reihenfolge: (1) Offenkundigkeit nach § 164 Abs. 1 BGB, (2) Vertretungsmacht
(Vollmacht, Prokura, gesetzliche Vertretung), (3) Vollmachtsumfang, (4) Handeln im Rahmen
der Vollmacht, (5) Ausnahmen: Duldungs-/Anscheinsvollmacht, (6) Vollmachtloser Vertreter
(§§ 177 bis 179 BGB), (7) Insichgeschäft (§ 181 BGB).

### Routing-Logik

Dieser Skill dient als Einstiegspunkt. Bei komplexen Stellvertretungsfragen werden die spezifischen
Teilskills aufgerufen: vollmacht-erteilung-umfang-erloeschen für Vollmachtsfragen,
duldungs-anscheinsvollmacht für Rechtsschein, insichgeschaeft-paragraph-181 für § 181 BGB.

### Klausur-Checkliste Routing

- Einstieg: Offenkundigkeit und Vollmacht als erste Prüfungspunkte?
- Vollmacht vorhanden: Umfang ausreichend für das konkrete Geschäft?
- Vollmacht fehlend: Rechtsschein (Duldung/Anschein) oder vollmachtloser Vertreter?
- Insichgeschäft: § 181 BGB mit Ausnahmen geprüft?
- Richtiger Teilskill für Detailprüfung ausgewählt?

## 3. `taeuschung-drohung-paragraph-123`

**Fokus:** Klausurfall zur Anfechtung wegen arglistiger Täuschung oder widerrechtlicher Drohung nach § 123 BGB: Täuschungshandlung und Kausalität, Drohung mit dem versprochenen empfindlichen Übel, Anfechtungsfrist ein Jahr nach § 124 BGB und Ausschluss bei Täuschung durch Dritte.

# Täuschung und Drohung — § 123 BGB

## Mandantenfall

- Verkäufer verschweigt arglistig Mängel des Kaufobjekts — Anfechtung nach § 123 BGB möglich?
- Arbeitnehmer unterschreibt Aufhebungsvertrag unter Drohung mit fristloser Kündigung — § 123 BGB?
- Klausurkonstellation: Täuschung durch Dritten, nicht Vertragspartner — Ausnahme bei Kenntnis oder Kennenmüssen.

## Erste Schritte

1. Täuschungsvariante: arglistige Täuschung durch aktives Tun oder Verschweigen pflichtwidriger Umstände.
2. Arglist prüfen: Wissenselement (Kenntnis der Unrichtigkeit) und Willensmerkmal (Täuschungsabsicht).
3. Drohungsvariante: Inaussichtstellen eines empfindlichen Übels als Mittel zur Willensbeeinflussung.
4. Widerrechtlichkeit der Drohung: Mittel oder Zweck widerrechtlich — BGH-Formel.
5. Kausalität: Täuschung oder Drohung war für Willenserklärung mitursächlich.
6. Anfechtungsfrist: § 124 BGB — ein Jahr ab Entdeckung der Täuschung oder Ende der Zwangslage.

## Rechtsrahmen

- § 123 Abs. 1 BGB: Anfechtung bei arglistiger Täuschung oder widerrechtlicher Drohung.
- § 123 Abs. 2 BGB: Täuschung durch Dritte — Anfechtung nur bei Kenntnis oder Kennenmüssen des Empfängers.
- § 124 BGB: Anfechtungsfrist — ein Jahr ab Entdeckung bzw. Ende der Zwangslage; zehn Jahre absolute Frist.
- § 142 BGB: Nichtigkeit ex tunc bei wirksamer Anfechtung.
- § 826 BGB: Schadensersatz bei vorsätzlicher sittenwidriger Schädigung als Auffangnorm.

## Prüfraster

1. Tatbestand Täuschung: aktive Irreführung oder arglistiges Verschweigen einer Aufklärungspflicht?
2. Arglist: Doppeltes Vorsatzelement — Kenntnis der Unrichtigkeit und Täuschungsabsicht?
3. Tatbestand Drohung: Inaussichtstellen eines empfindlichen Übels durch den Drohenden?
4. Widerrechtlichkeit: Ist das angedrohte Mittel oder der verfolgte Zweck widerrechtlich?
5. Kausalität: War Täuschung oder Drohung für die Willenserklärung mitursächlich?
6. Täuschung durch Dritte (§ 123 Abs. 2 BGB): Kannte oder musste Empfänger die Täuschung kennen?
7. Frist nach § 124 BGB: Ein Jahr gewahrt? Absolute Zehn-Jahres-Frist?
8. Rechtsfolge § 142 BGB: Nichtigkeit ex tunc — Rückabwicklung nach § 812 BGB?

## Typische Fallstricke

- Arglist erfordert Täuschungsabsicht — Fahrlässigkeit reicht nicht aus.
- Täuschung durch Dritte nach § 123 Abs. 2 BGB: Nur anfechtbar, wenn Empfänger Kenntnis hatte oder haben musste.
- Anfechtungsfrist § 124 BGB läuft ab Entdeckung, nicht ab Abschluss — wichtig für Fristberechnung.
- Drohung mit Ausübung eines Rechts kann dennoch widerrechtlich sein, wenn Zweck-Mittel-Verhältnis nicht stimmt.

## Output

- Gutachtenstil-Abschnitt zu § 123 BGB mit vollständiger Subsumtion
- Prüfampel: Täuschung / Drohung bejaht / Kausalität / Frist gewahrt
- Klausurlösungsskizze mit Dritte-Täuschung-Variante
- Rückfragenliste zu Arglist-Nachweis und Fristbeginn

## Quellen

- [§ 123 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__123.html)
- [§ 124 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__124.html)
- [§ 142 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__142.html)
- [dejure.org § 123 BGB](https://dejure.org/gesetze/BGB/123.html)
- [dejure.org § 124 BGB](https://dejure.org/gesetze/BGB/124.html)

## Vertiefung

### Verhältnis zu § 119 BGB

§ 123 BGB und § 119 BGB stehen grundsätzlich nebeneinander: Bei arglistiger Täuschung über
Eigenschaften (§ 119 Abs. 2 BGB) kann sowohl nach § 119 Abs. 2 als auch nach § 123 BGB angefochten
werden. Der Unterschied: § 119 BGB erfordert Kausalität und Unverzüglichkeit (§ 121 BGB),
§ 123 BGB die Jahresfrist (§ 124 BGB) und kein Verschuldenserfordernis beim Erklärungsempfänger.

### Drohung mit Ausübung eines Rechts

BGH: Drohung mit Ausübung eines Rechts (z.B. Strafanzeige) kann widerrechtlich sein, wenn
Mittel und Zweck in einem unangemessenen Verhältnis stehen. Klassischer Fall: Drohung mit
Strafanzeige, um Schulden einzutreiben.

### Klausur-Checkliste § 123 BGB

- Täuschungsvariante: Aktive Irreführung oder arglistiges Verschweigen?
- Arglist: Doppeltes Vorsatzelement (Kenntnis und Täuschungsabsicht)?
- Drohungsvariante: Empfindliches Übel in Aussicht gestellt?
- Widerrechtlichkeit der Drohung: Mittel oder Zweck rechtswidrig?
- Dritte-Täuschung (§ 123 Abs. 2 BGB): Empfänger kannte Täuschung?
