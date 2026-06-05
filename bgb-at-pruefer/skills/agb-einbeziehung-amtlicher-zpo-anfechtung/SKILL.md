---
name: agb-einbeziehung-amtlicher-zpo-anfechtung
description: "AGB Einbeziehung Amtlicher ZPO Anfechtung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AGB Einbeziehung Amtlicher ZPO Anfechtung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **AGB Einbeziehung Amtlicher ZPO Anfechtung** im Plugin Bgb At Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `agb-einbeziehung-schnittstelle-paragraphen-305-310` | Prüft AGB-Einbeziehung nach §§ 305 bis 310 BGB: ausdrücklicher und konkludenter Hinweis, zumutbare Kenntnisnahmemöglichkeit, Überraschungsklauseln § 305c BGB, Inhaltskontrolle §§ 307 bis 309 BGB. Klausurfall mit vollständiger Subsumtionskette. |
| `amtlicher-bgb-zpo-normcheck` | Amtlicher Normcheck für BGB-AT-Fälle: gleicht Geschäftsfähigkeit, Willenserklärung, Form, Zugang, Vertragsschluss, Stellvertretung, Fristen, Verjährung und ZPO-Schnittstellen gegen die aktuelle Gesetze-im-Internet-Fassung ab. |
| `anfechtung-routing` | Routing-Skill für Anfechtung nach §§ 119 bis 124 und § 142 BGB: Prüfsituation in Klausur oder Mandat — Anfechtungsgrund bestimmen, Anfechtungserklärung und Gegner prüfen, Frist berechnen, Ausschlüsse und Folgen nach §§ 122 und 142 BGB darstellen. |

## Arbeitsweg

Im Plugin Bgb At Pruefer gilt für **AGB Einbeziehung Amtlicher ZPO Anfechtung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `agb-einbeziehung-schnittstelle-paragraphen-305-310`

**Fokus:** Prüft AGB-Einbeziehung nach §§ 305 bis 310 BGB: ausdrücklicher und konkludenter Hinweis, zumutbare Kenntnisnahmemöglichkeit, Überraschungsklauseln § 305c BGB, Inhaltskontrolle §§ 307 bis 309 BGB. Klausurfall mit vollständiger Subsumtionskette.

# AGB-Einbeziehung und Inhaltskontrolle — §§ 305 bis 310 BGB

## Mandantenfall

- Mandant schließt Online-Kaufvertrag ab; AGB-Link war nur im Footer sichtbar — wirksam einbezogen?
- Unternehmer verwendet im B2B-Bereich AGB mit Haftungsausschluss; Gegenseite hatte eigene AGB — kollidierende AGB-Situation.
- Klausurkonstellation: Hotelgast akzeptiert Hausordnung beim Check-in — Einbeziehung nach § 305 Abs. 2 BGB.

## Erste Schritte

1. Anwendungsbereich prüfen: Verbraucher oder Unternehmer (§ 310 BGB beachten).
2. Einbeziehungsvoraussetzungen nach § 305 Abs. 2 BGB: ausdrücklicher Hinweis, Möglichkeit der Kenntnisnahme, Einverständnis.
3. Überraschungsklauseln nach § 305c Abs. 1 BGB identifizieren und aussondern.
4. Inhaltskontrolle: Klausel-Typ bestimmen (§ 308 oder § 309 BGB Katalog, Generalklausel § 307 BGB).
5. Bei Lücke durch unwirksame Klausel: § 306 BGB (Vertrag bleibt wirksam, gesetzliche Regelung tritt ein).
6. Ergebnis: Welche Klauseln sind einbezogen und wirksam?

## Rechtsrahmen

- § 305 Abs. 1 BGB: Definiton der AGB als einseitig gestellte Vertragsbedingungen.
- § 305 Abs. 2 BGB: Einbeziehungsvoraussetzungen — Hinweis und Kenntnisnahmemöglichkeit.
- § 305c BGB: Überraschende und mehrdeutige Klauseln werden nicht Vertragsbestandteil.
- § 307 BGB: Generalklausel — unangemessene Benachteiligung entgegen Treu und Glauben.
- §§ 308 und 309 BGB: Klauselverbote mit und ohne Wertungsmöglichkeit.
- § 310 BGB: Besonderheiten im unternehmerischen Verkehr — §§ 308 und 309 BGB nicht direkt anwendbar.

## Prüfraster

1. AGB-Eigenschaft: Vorformulierte Bedingungen für Vielzahl von Verträgen einseitig gestellt?
2. Einbeziehung nach § 305 Abs. 2 BGB: Hinweis, Kenntnisnahmemöglichkeit und Einverständnis?
3. Bereichsausnahmen § 310 BGB: individuell ausgehandelte Klauseln, B2B-Sonderregeln?
4. § 305c BGB: Überraschungsklausel — ungewöhnlich für den Vertragstyp?
5. Inhaltskontrolle §§ 307 bis 309 BGB: Katalogverstoß oder unangemessene Benachteiligung?
6. Rechtsfolge unwirksamer Klausel: § 306 BGB — Lückenfüllung durch dispositives Recht.
7. Kollision zweier AGB: Theorie der engsten Verbindung / Kongruenzgeltung.

## Typische Fallstricke

- Einbeziehung und Inhaltskontrolle sind streng zu trennen; Klausel kann einbezogen, aber unwirksam sein.
- Im B2B-Verkehr gelten §§ 308 und 309 BGB nur als Indiz, nicht direkt.
- AGB-Recht gilt nicht für individuell ausgehandelte Klauseln (§ 305 Abs. 1 S. 3 BGB).
- Online-Einbeziehung: aktives Anklicken einer Checkbox genügt, bloßer Link im Footer reicht nicht immer.

## Output

- Einbeziehungsprüfung im Gutachtenstil mit Subsumtion zu § 305 Abs. 2 BGB
- Klausel-Screening-Tabelle: einbezogen / überraschend / unwirksam / Rechtsfolge
- Klausurlösungsskizze mit Schwerpunkt AGB-Recht
- Hinweise zu kollidierenden AGB im B2B-Bereich

## Quellen

- [§ 305 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__305.html)
- [§ 307 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__307.html)
- [§ 305c BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__305c.html)
- [§ 310 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__310.html)
- [dejure.org § 307 BGB](https://dejure.org/gesetze/BGB/307.html)

## Vertiefung

### Stufenverhältnis der AGB-Prüfung

Die AGB-Prüfung erfolgt dreistufig: (1) Einbeziehung nach §§ 305 und 305a BGB, (2) Auslegung nach
§ 305c Abs. 2 BGB (Unklarheitenregel zulasten des Verwenders), (3) Inhaltskontrolle nach §§ 307 bis
309 BGB. Nur wirksam einbezogene Klauseln können der Inhaltskontrolle unterliegen.

### AGB im B2B-Bereich

Im unternehmerischen Verkehr gelten erleichterte Einbeziehungsanforderungen (§ 310 Abs. 1 BGB):
Kein Hinweis und keine Kenntnisnahmemöglichkeit nach § 305 Abs. 2 BGB erforderlich. Die branchenübliche
Klauselverwendung genügt. Allerdings bleibt die Inhaltskontrolle nach § 307 BGB anwendbar.

### Klausur-Checkliste AGB

- Sind AGB im Sinne von § 305 Abs. 1 BGB gegeben (vorformuliert, viele Verträge, einseitig gestellt)?
- Wurde ausdrücklich oder konkludent auf die AGB hingewiesen?
- Hatte die andere Partei zumutbare Kenntnisnahmemöglichkeit?
- Liegt eine überraschende Klausel nach § 305c Abs. 1 BGB vor?
- Verstößt die Klausel gegen § 307 oder §§ 308/309 BGB?

## 2. `amtlicher-bgb-zpo-normcheck`

**Fokus:** Amtlicher Normcheck für BGB-AT-Fälle: gleicht Geschäftsfähigkeit, Willenserklärung, Form, Zugang, Vertragsschluss, Stellvertretung, Fristen, Verjährung und ZPO-Schnittstellen gegen die aktuelle Gesetze-im-Internet-Fassung ab.

# Amtlicher BGB/ZPO-Normcheck

## Zweck

Dieser Skill ist der Faktenhygiene-Check für BGB-AT-Arbeit. Er wird zugeschaltet, wenn eine Normnummer, ein Formpfad, ein Fristenlauf oder eine ZPO-Schnittstelle tragend ist und nicht aus Gedächtnisformeln beantwortet werden darf.

## Arbeitsfolge

1. **Normcluster bestimmen:** Geschäftsfähigkeit, Willenserklärung, Form, Zugang, Vertragsschluss, Stellvertretung, Zustimmung, Fristen oder Verjährung.
2. **Aktuellen Normtext prüfen:** BGB bei Gesetze im Internet; bei Prozessbezug ZPO zusätzlich.
3. **Reformhinweis lesen:** Wenn die amtliche Fassung Änderungen als textlich nachgewiesen, aber dokumentarisch nicht abschließend bearbeitet markiert, diesen Unsicherheitsanker sichtbar machen.
4. **Schnittstelle trennen:** BGB-Formwirksamkeit, ZPO-Einreichung, Zustellung und Beweiswert getrennt prüfen.
5. **Arbeitsprodukt bauen:** Normenmatrix, Fristenrechnung, Formentscheidung oder kurzer Prüfvermerk.

## Normcluster

| Thema | Normen |
| --- | --- |
| Geschäftsfähigkeit | §§ 104-113 BGB |
| Willenserklärung/Irrtum | §§ 116-124 BGB |
| Form | §§ 125-129 BGB |
| Zugang | § 130 BGB |
| Auslegung/Nichtigkeit | §§ 133, 134, 138-141 BGB |
| Vertragsschluss/Dissens | §§ 145-157 BGB |
| Stellvertretung | §§ 164-181 BGB |
| Zustimmung/Nichtberechtigte | §§ 182-185 BGB |
| Fristen | §§ 186-193 BGB; § 222 ZPO |
| Verjährung | §§ 194-218 BGB; § 204 BGB und § 167 ZPO |
| Elektronisches Verfahren | §§ 130a, 130d, 130e, 173, 189, 371a ZPO |

## Output

Erzeuge eine Tabelle:

| Norm | Titel/Funktion | Tatsache | Beleg | Rechtsfolge | Live-Check |
| --- | --- | --- | --- | --- | --- |

Danach höchstens fünf Sätze Ergebnis. Keine Rechtsprechung ergänzen, wenn sie nicht ausdrücklich geprüft wurde.

## Referenz

Nutze `references/amtlicher-bgb-zpo-normkern.md`.

## 3. `anfechtung-routing`

**Fokus:** Routing-Skill für Anfechtung nach §§ 119 bis 124 und § 142 BGB: Prüfsituation in Klausur oder Mandat — Anfechtungsgrund bestimmen, Anfechtungserklärung und Gegner prüfen, Frist berechnen, Ausschlüsse und Folgen nach §§ 122 und 142 BGB darstellen.

# Anfechtung — Routing und Gesamtprüfung §§ 119 bis 124 BGB

## Mandantenfall

- Mandant hat Vertrag geschlossen und bemerkt nachträglich einen Irrtum über eine wesentliche Eigenschaft der Kaufsache — Anfechtung nach § 119 Abs. 2 BGB?
- Käufer wurde durch arglistige Täuschung zum Vertragsschluss bewogen — § 123 Abs. 1 Alt. 1 BGB, Fristwahrung?
- Klausurkonstellation: Erklärung unter Drohung — Verhältnis § 123 Abs. 1 Alt. 2 BGB zu § 138 BGB.

## Erste Schritte

1. Auslegung und Vertragsschluss zuerst prüfen — Anfechtung ist ultima ratio.
2. Anfechtungsgrund präzise zuordnen: § 119 Abs. 1 (Inhaltsirrtum), § 119 Abs. 1 Alt. 2 (Erklärungsirrtum), § 119 Abs. 2 (Eigenschaftsirrtum), § 120 (Übermittlungsirrtum), § 123 (Täuschung/Drohung).
3. Anfechtungserklärung: gegenüber dem richtigen Anfechtungsgegner (§ 143 BGB).
4. Anfechtungsfrist: § 121 BGB (unverzüglich) bei §§ 119 und 120; § 124 BGB (1 Jahr bzw. 10 Jahre) bei § 123.
5. Ausschluss prüfen: § 144 BGB (Bestätigung), Fristablauf, fehlende Kausalität.
6. Rechtsfolgen: § 142 BGB (Nichtigkeit ex tunc), § 122 BGB (Vertrauensschaden).

## Rechtsrahmen

- § 119 BGB: Irrtumsanfechtung — Inhalts- und Erklärungsirrtum sowie Eigenschaftsirrtum.
- § 120 BGB: Anfechtung bei fehlerhafter Übermittlung durch Boten oder Einrichtung.
- § 123 BGB: Anfechtung wegen arglistiger Täuschung oder widerrechtlicher Drohung.
- § 142 BGB: Rechtsfolge — angefochtenes Rechtsgeschäft als von Anfang an nichtig.
- § 122 BGB: Schadensersatzpflicht des Anfechtenden gegenüber dem Vertrauensschadensgläubiger.
- § 143 BGB: Anfechtungsgegner — bei Vertrag gegenüber dem anderen Teil.

## Prüfraster

1. Auslegung vor Anfechtung: Besteht ein Vertrag mit dem gewünschten oder einem anderen Inhalt?
2. Anfechtungsgrund: Welcher Irrtumstatbestand oder § 123 BGB ist einschlägig?
3. Anfechtungserklärung: Eindeutige Erklärung, kein Formzwang, richtiger Empfänger?
4. Anfechtungsfrist: Unverzüglich nach § 121 BGB oder Jahresfrist nach § 124 BGB?
5. Ausschlussgrund: Bestätigung nach § 144 BGB oder Fristablauf?
6. Rechtsfolge § 142 BGB: ex-tunc-Nichtigkeit, Rückabwicklung nach §§ 812 ff. BGB.
7. Vertrauensschaden § 122 BGB: Höhe und Abgrenzung vom Erfüllungsinteresse.

## Typische Fallstricke

- Motivirrtum ist grundsätzlich unbeachtlich; nur Eigenschaftsirrtum nach § 119 Abs. 2 BGB ist relevant.
- Die Frist des § 121 BGB läuft ab Kenntnis des Anfechtungsgrunds, nicht ab Vertragsschluss.
- § 123 BGB: arglistige Täuschung durch Dritten — nur wenn Erklärungsempfänger die Täuschung kannte oder kennen musste.
- Anfechtung neben Gewährleistungsrecht: Vorrang und Sperrwirkung beachten.

## Output

- Routing-Übersicht: Welcher Anfechtungsgrund liegt vor?
- Prüfungsraster-Tabelle: Grund / Erklärung / Frist / Ausschluss / Folgen
- Gutachtenstil-Abschnitt zur gewählten Anfechtungsnorm
- Schadensersatzberechnung nach § 122 BGB

## Quellen

- [§ 119 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__119.html)
- [§ 123 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__123.html)
- [§ 142 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__142.html)
- [§ 122 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__122.html)
- [dejure.org § 119 BGB](https://dejure.org/gesetze/BGB/119.html)

## Vertiefung

### Anfechtungs-Checkliste (Kurzform)

Die Anfechtung ist das letzte Mittel, nicht das erste. Prüfungsreihenfolge in der Klausur:
(1) Auslegung der Willenserklärung vorschalten — ist der Wille wirklich falsch erklärt worden?
(2) Dann den richtigen Anfechtungsgrund zuordnen: §§ 119 und 120 BGB (Irrtumsanfechtung,
Frist nach § 121 BGB), § 123 BGB (Täuschung/Drohung, Frist nach § 124 BGB).

### Konkurrenzen

Anfechtung nach § 119 BGB und Gewährleistung beim Kauf (§§ 434 ff. BGB) können nebeneinander
bestehen. Im Kaufrecht verdrängt der Eigenschaftsirrtum (§ 119 Abs. 2 BGB) nach BGH-Rechtsprechung
die Gewährleistungsrechte nicht vollständig, aber das Verhältnis ist klausurrelevant.

### Klausur-Checkliste Anfechtung

- Auslegung vorgelagert und abgeschlossen?
- Anfechtungsgrund konkret bezeichnet (§ 119 Abs. 1, § 119 Abs. 2, § 120 oder § 123 BGB)?
- Frist: unverzüglich (§ 121 BGB) oder ein Jahr (§ 124 BGB)?
- Anfechtungsgegner nach § 143 BGB korrekt?
- Rechtsfolge: § 142 BGB (Nichtigkeit ex tunc) und § 122 BGB (Schadensersatz) geprüft?
