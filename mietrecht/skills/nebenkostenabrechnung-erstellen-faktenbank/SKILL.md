---
name: nebenkostenabrechnung-erstellen-faktenbank
description: "Nebenkostenabrechnung Erstellen Faktenbank: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nebenkostenabrechnung Erstellen Faktenbank

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Nebenkostenabrechnung Erstellen Faktenbank** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nebenkostenabrechnung-erstellen` | Betriebskostenabrechnung erstellen aus Vermieter- und Hausverwaltungssicht: Umlagevereinbarung, BetrKV-Kostenarten, HeizkostenV, CO2KostAufG, Abrechnungsfrist, Vorauszahlungen, Belegpaket, Zugangsnachweis und Versand-Qualitygate. |
| `nebenkostenabrechnung-pruefen` | Betriebskostenabrechnung prüfen aus Mietersicht: formelle Mindestangaben, Frist, Umlagefähigkeit, Belegeinsicht, Zahlungsbelege, HeizkostenV, CO2KostAufG, Rechenkontrolle, Einwendungen und temporäres Zurückbehaltungsrecht. |
| `rechtsstand-mai-2026-faktenbank` | Faktenbank und Quellen-Gate für aktuelle mietrechtliche und WEG-rechtliche Aussagen mit Stand 29.05.2026. Dieses Fachmodul dient als Quellen-Gate vor Ausgaben zu Mietpreisbremse, Mieterhöhung, Betriebskosten, Kündigung, Kaution, Steckersolargeräten, virtueller Eigentümerversammlung, WEG-Beschlussklage und baulichen Veränderungen. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **Nebenkostenabrechnung Erstellen Faktenbank**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nebenkostenabrechnung-erstellen`

**Fokus:** Betriebskostenabrechnung erstellen aus Vermieter- und Hausverwaltungssicht: Umlagevereinbarung, BetrKV-Kostenarten, HeizkostenV, CO2KostAufG, Abrechnungsfrist, Vorauszahlungen, Belegpaket, Zugangsnachweis und Versand-Qualitygate.

# Betriebskostenabrechnung erstellen

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebskostenabrechnung erstellen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Ziel

Dieser Skill erstellt keine pauschale Nebenkostenliste, sondern eine belastbare, versandfähige Betriebskostenabrechnung für Wohnraummiete oder gemischt genutzte Objekte. Er trennt streng:

- mietvertragliche Umlagevereinbarung,
- tatsächlich angefallene Gesamtkosten,
- umlagefähige Betriebskosten nach BetrKV,
- nicht umlagefähige Verwaltung, Instandhaltung und Instandsetzung,
- Heiz-/Warmwasserkosten nach HeizkostenV,
- CO2-Kostenaufteilung nach CO2KostAufG,
- Vorauszahlungen und Saldo.

## Einstieg

Nur diese Punkte abfragen, wenn sie nicht aus der Akte hervorgehen:

1. Abrechnungsjahr und Zugangsziel: Bis wann muss die Abrechnung beim Mieter sein?
2. Wohnraum, Gewerbe oder gemischt genutztes Objekt?
3. Mietvertragliche Betriebskostenklausel: pauschal, Vorauszahlung, Inklusivmiete oder konkrete Kostenliste?
4. Gibt es WEG-Jahresabrechnung, Heizkostenabrechnung, Rechnungen/Zahlungsbelege, Kontoauszüge und Mieter-Vorauszahlungskonto?
5. Sollen Nachforderung, Guthaben, Vorauszahlungsanpassung oder nur ein Entwurf ausgegeben werden?

## Rechts- und Quellenanker

- § 556 BGB: Betriebskostenvereinbarung, Abrechnungszeitraum, Abrechnungsfrist, Einwendungsfrist.
- § 556a BGB: Umlagemaßstab, soweit mietvertraglich nichts anderes gilt.
- § 560 Abs. 4 BGB: Anpassung der Vorauszahlungen nach Abrechnung.
- BetrKV §§ 1 und 2: Betriebskostenbegriff und Kostenarten.
- HeizkostenV §§ 6 bis 12: Verbrauchserfassung, Kostenverteilung und Kürzungsrecht.
- CO2KostAufG: Aufteilung der CO2-Kosten, bei Wohngebäuden regelmäßig Stufenmodell.
- BGH, Urteil vom 09.04.2008 - VIII ZR 84/07: Mindestangaben einer formell ordnungsgemäßen Betriebskostenabrechnung.
- BGH, Urteil vom 12.11.2014 - VIII ZR 112/14: Schätzungen und materielle Fragen kippen nicht automatisch die formelle Ordnung.
- BGH, Urteil vom 09.12.2020 - VIII ZR 118/19: Belegeinsicht umfasst auch Zahlungsbelege.

## Erstellungsworkflow

### 1. Umlagegrundlage

Prüfe zuerst die Mietvertragslage. Ohne Umlagevereinbarung gibt es bei Wohnraum keine Nachforderung auf Betriebskosten. Ein Verweis auf die BetrKV genügt regelmäßig; "sonstige Betriebskosten" müssen als solche erkennbar vereinbart sein und dürfen nicht erst in der Abrechnung erfunden werden.

### 2. Abrechnungsperiode und Frist

- Abrechnungszeitraum höchstens zwölf Monate.
- Abrechnung muss dem Mieter spätestens zwölf Monate nach Ende des Abrechnungszeitraums zugehen.
- Nicht nur Versand, sondern Zugang beweissicher planen: Bote mit Zustellvermerk, Einwurf mit Zeuge, Portalzugang nur bei tragfähiger Vereinbarung und Zugangsnachweis.

### 3. Kostenarten-Matrix

Erzeuge eine Tabelle:

| Kostenart | Beleg | Zeitraum | Umlagefähig? | Schlüssel | Herauszurechnen |
| --- | --- | --- | --- | --- | --- |
| Grundsteuer | Bescheid | Jahr | ja, wenn vereinbart | Fläche/Vertrag | Nachzahlungen für andere Jahre erläutern |
| Wasser/Abwasser | Rechnung/Zähler | Jahr | ja | Verbrauch/Fläche | Leerstand prüfen |
| Hausmeister | Vertrag/Stunden | Jahr | nur Betrieb, nicht Reparatur/Verwaltung | Vertrag/Fläche | Reparaturanteile |
| Gartenpflege | Rechnung | Jahr | ja | Vertrag/Fläche | Neuanlage/Umgestaltung |
| Versicherung | Police/Rechnung | Jahr | Sach-/Haftpflicht ja | Vertrag/Fläche | Rechtsschutz/Verwaltung |
| Heizung/Warmwasser | Heizkostenabrechnung | Jahr | ja | HeizkostenV | CO2-Anteil, Kürzungsrecht |

### 4. Verteilerschlüssel

- Vertraglicher Schlüssel vor gesetzlichem Auffangmaßstab.
- Wenn nichts vereinbart ist: Wohnfläche nach § 556a Abs. 1 BGB, soweit Verbrauch oder Verursachung nicht erfasst wird.
- Heizkosten/Warmwasser nicht in die allgemeine Flächenlogik ziehen: HeizkostenV gesondert rechnen.
- Gemischt genutzte Objekte: Gewerbe-Vorwegabzug nur, wenn die Gewerbenutzung Mehrkosten verursacht oder der Vertrag/die Sachlage dies trägt; keine automatische Sonderbelastung ohne Begründung.

### 5. Heizkosten, Warmwasser und CO2

- Prüfen, ob Messgeräte fernablesbar sind und ob unterjährige Verbrauchsinformationen relevant sind.
- Verbrauchsanteil nach HeizkostenV grundsätzlich zwischen 50 und 70 Prozent.
- Bei Verstößen gegen HeizkostenV Kürzungsrecht nach § 12 HeizkostenV markieren.
- CO2-Kosten nicht als normale Brennstoffkosten ungeprüft vollständig auf den Mieter legen. Für Wohngebäude Stufe ermitteln; bei Nichtwohngebäuden aktuelle Sonderregel und Rechtsstand live prüfen.

### 6. Vorauszahlungen und Saldo

- Nur tatsächlich geschuldete und geleistete Vorauszahlungen für den Abrechnungszeitraum abziehen.
- Mieterwechsel taggenau abgrenzen.
- Guthaben und Nachforderung klar ausweisen.
- Anpassung der Vorauszahlungen nach § 560 Abs. 4 BGB separat erklären, nicht versteckt in die Abrechnung schreiben.

## Versand-Qualitygate

Vor Versand zwingend ausgeben:

1. formelle Mindestangaben vollständig,
2. alle Kostenarten mit Beleg und Umlagegrundlage,
3. Heizkosten/CO2 gesondert geprüft,
4. Vorauszahlungen gegen Mietkonto abgeglichen,
5. Nachforderung durch Zugangsnachweis abgesichert,
6. Belege kurzfristig einsichtsfähig,
7. Anschreiben mit Einwendungsfrist und Belegeinsichtshinweis.

## Output

- fertige Abrechnung als Tabelle,
- Begleitschreiben an den Mieter,
- Belegverzeichnis,
- Rechenkontrollblatt,
- Vorauszahlungsanpassung als separates Schreiben,
- Lückenliste, wenn die Abrechnung noch nicht versandfähig ist.

## Quellenregel

Normen live auf gesetze-im-internet.de prüfen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 2. `nebenkostenabrechnung-pruefen`

**Fokus:** Betriebskostenabrechnung prüfen aus Mietersicht: formelle Mindestangaben, Frist, Umlagefähigkeit, Belegeinsicht, Zahlungsbelege, HeizkostenV, CO2KostAufG, Rechenkontrolle, Einwendungen und temporäres Zurückbehaltungsrecht.

# Betriebskostenabrechnung prüfen

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebskostenabrechnung prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Ziel

Dieser Skill prüft eine konkrete Betriebskostenabrechnung so, dass daraus sofort ein Rückfrageschreiben, eine Zahlungsempfehlung, eine Einwendung oder eine Klage-/Verteidigungsnotiz entstehen kann. Er unterscheidet konsequent zwischen formellen Fehlern, materiellen Fehlern und bloßen Erläuterungslücken.

## Einstieg

Wenn die Abrechnung vorliegt, nicht lange fragen: zuerst auswerten. Nur diese Weichen klären:

1. Wann ging die Abrechnung zu und für welchen Zeitraum?
2. Welche Nachforderung oder welches Guthaben wird verlangt?
3. Welche Vorauszahlungen wurden wirklich geleistet?
4. Gibt es Mietvertrag, Vorjahresabrechnung, Heizkostenabrechnung, WEG-Abrechnung oder Belege?
5. Soll zunächst Belegeinsicht verlangt, gezahlt unter Vorbehalt, gekürzt oder bestritten werden?

## Rechts- und Rechtsprechungsanker

- § 556 Abs. 3 BGB: Abrechnungsfrist und Einwendungsfrist.
- § 556a BGB: Umlagemaßstab.
- § 259 BGB und § 242 BGB: Beleg- und Rechenschaftslogik.
- BetrKV §§ 1 und 2: Umlagefähige Kostenarten.
- HeizkostenV, insbesondere §§ 7, 8, 9a, 12.
- CO2KostAufG für Brennstoff-CO2-Kosten.
- BGH, Urteil vom 09.04.2008 - VIII ZR 84/07: Mindestangaben formeller Ordnung.
- BGH, Urteil vom 12.11.2014 - VIII ZR 112/14: formelle Ordnung trotz Schätzung möglich; Schätzung ist dann materiell zu prüfen.
- BGH, Urteil vom 09.12.2020 - VIII ZR 118/19: Einsicht auch in Zahlungsbelege.
- BGH, Urteil vom 15.12.2021 - VIII ZR 66/20: grundsätzlich Einsicht in Originalbelege; Kopien nur bei besonderem Grund oder Vereinbarung.

## Prüfraster

### 1. Frist und Zugang

- Nachforderung ausgeschlossen, wenn die Abrechnung nicht binnen zwölf Monaten nach Ende des Abrechnungszeitraums zugeht und der Vermieter die Verspätung zu vertreten hat.
- Einwendungen des Mieters binnen zwölf Monaten ab Zugang der Abrechnung.
- Zugangsnachweis des Vermieters kritisch prüfen: Datum im Schreiben reicht nicht.

### 2. Formelle Mindestangaben

Eine Abrechnung ist formell brauchbar, wenn der Mieter rechnerisch nachvollziehen kann:

- Gesamtkosten je Kostenart,
- angewendeter Verteilerschlüssel,
- Rechenweg zum eigenen Anteil,
- Abzug der Vorauszahlungen,
- Ergebnis als Nachforderung oder Guthaben.

Fehlt einer dieser Bausteine, kann die Nachforderung schon formal scheitern. Sind Bausteine vorhanden, aber falsch, ist meist materiell zu prüfen.

### 3. Umlagefähigkeit

Nicht umlagefähig sind typischerweise:

- Verwaltungskosten,
- Instandhaltung und Instandsetzung,
- Reparaturanteile im Hausmeister- oder Wartungsvertrag,
- Bank- und Finanzierungskosten ohne tragfähige Grundlage,
- Prozess-, Anwalts- oder Mahnkosten,
- Kosten, die nicht vereinbart oder nicht unter BetrKV/konkret vereinbarte sonstige Betriebskosten fallen.

### 4. Belege und Zahlungsbelege

Fordere gezielt an:

- Rechnungen,
- Verträge und Leistungsverzeichnisse,
- Zahlungsbelege/Kontoauszüge,
- Mess- und Ableseprotokolle,
- Dienstleisteraufschlüsselung bei Hausmeister, Reinigung, Wartung,
- Flächen-/Einheitenliste,
- Heizkosten- und CO2-Berechnung.

Solange berechtigte Belegeinsicht verweigert wird, kann gegen die Nachforderung ein temporäres Leistungsverweigerungsrecht bestehen.

### 5. Heizkosten und CO2

- Verbrauchsabhängige Abrechnung prüfen.
- Schätzungen nach § 9a HeizkostenV separat begründen lassen.
- Kürzungsrecht nach § 12 HeizkostenV prüfen.
- CO2-Aufteilung nach CO2KostAufG kontrollieren: Emissionsdaten, Gebäudestufe, Brennstoffrechnung, rechnerischer Vermieter-/Mieteranteil.

### 6. Rechenkontrolle

Erzeuge eine Tabelle:

| Position | Abgerechnet | Richtig? | Fehlerart | Beleg fehlt | Korrektur |
| --- | ---: | --- | --- | --- | ---: |
| Hausmeister | ... | prüfen | Reparaturanteil? | Vertrag/Stunden | ... |
| Heizung | ... | prüfen | HeizkostenV/CO2 | Messdaten | ... |
| Grundsteuer | ... | prüfen | Zeitraum | Bescheid | ... |

## Output

- Kurzbewertung: zahlen, teilweise zahlen, Belegeinsicht, Einwendung oder Klageabwehr.
- Einwendungsschreiben mit konkreten Positionen.
- Belegeinsichtsanfrage mit Liste der benötigten Belege.
- Korrigierte Saldenrechnung.
- Fristenblatt für Einwendungsfrist und etwaige Zahlung unter Vorbehalt.

## Quellenregel

Normen live auf gesetze-im-internet.de prüfen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 3. `rechtsstand-mai-2026-faktenbank`

**Fokus:** Faktenbank und Quellen-Gate für aktuelle mietrechtliche und WEG-rechtliche Aussagen mit Stand 29.05.2026. Dieses Fachmodul dient als Quellen-Gate vor Ausgaben zu Mietpreisbremse, Mieterhöhung, Betriebskosten, Kündigung, Kaution, Steckersolargeräten, virtueller Eigentümerversammlung, WEG-Beschlussklage und baulichen Veränderungen.

# Rechtsstand Mai 2026 — Faktenbank Mietrecht und WEG

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsstand Mai 2026 — Faktenbank Mietrecht und WEG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill ist das Quellen-Gate des Mietrecht-Plugins. Er wird geladen, wenn aktuelle Rechtslage, Mietpreisbremse, WEG-Reform, Betriebskosten, Kündigung, Kaution, bauliche Veränderung oder gerichtliche Durchsetzung relevant sind.

Stand dieser Faktenbank: **29.05.2026**. Bei konkreten Mietspiegeln, Landesverordnungen und Rechtsprechung immer live prüfen.

## Quellenregel

- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freiem/amtlichem Link.
- Mietspiegel nur aus amtlicher kommunaler Quelle oder aus `references/mietspiegel-quellen.md`.
- Landesverordnungen zur Mietpreisbremse/Kappungsgrenze immer für Bundesland, Gemeinde und Zeitpunkt prüfen.

## Verifizierte Rechtsstandsanker

| Thema | Gesicherter Anker | Praktische Aussage | Freie Quelle |
|---|---|---|---|
| Mietpreisbremse | § 556d BGB; BGH, Urteil vom 18.12.2024, VIII ZR 16/23 | Mietpreisbremse immer dreistufig prüfen: Gebiet/Verordnung, Ausgangsmiete und Ausnahmen, dann Rüge/Rückforderung. Verfassungs- und Verordnungsfragen nicht aus Modellwissen behaupten. | https://www.gesetze-im-internet.de/bgb/__556d.html / https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&nr=140461 |
| Modernisierung und Mietpreisbremse | BGH, Urteil vom 27.11.2024, VIII ZR 36/23 | Modernisierungsausnahmen sauber nach Vor-/Nachmaßnahmen, Informationslage und konkreter Berechnung trennen; umfassende Modernisierung nicht pauschal unterstellen. | https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&nr=140073 |
| Steckersolargeräte Miete | § 554 BGB | Mieter können eine bauliche Veränderung für Steckersolargeräte verlangen; Interessenabwägung, Zumutbarkeit, technische Sicherheit und Rückbau dokumentieren. | https://www.gesetze-im-internet.de/bgb/__554.html |
| Steckersolargeräte WEG | § 20 Abs. 2 WEG | Wohnungseigentümer haben einen Anspruch auf angemessene bauliche Veränderungen u. a. für Steckersolargeräte; Ausführung bleibt ordnungsmäßig zu beschließen. | https://www.gesetze-im-internet.de/woeigg/__20.html |
| Virtuelle Eigentümerversammlung | § 23 Abs. 1a WEG; § 48 Abs. 6 WEG | Rein virtuelle Versammlung nur aufgrund Beschlusses mit qualifizierter Mehrheit und befristeter Wirkung; bis Ende 2028 Übergangsrecht mit Präsenzversammlung beachten. | https://www.gesetze-im-internet.de/woeigg/__23.html / https://www.gesetze-im-internet.de/woeigg/__48.html |
| Verwalterabberufung | § 26 Abs. 3 WEG | Verwalter kann jederzeit abberufen werden; der Verwaltervertrag endet spätestens sechs Monate nach Abberufung. "Nur bei wichtigem Grund" ist seit WEMoG falsch. | https://www.gesetze-im-internet.de/woeigg/__26.html |
| WEG bauliche Veränderung | BGH, Urteil vom 28.03.2025, V ZR 105/24 | Bei baulichen Veränderungen § 20 WEG und Kostenfolge § 21 WEG getrennt prüfen; § 20 Abs. 4 WEG bleibt Grenze bei grundlegender Umgestaltung/unbilliger Benachteiligung. | https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&nr=141815 |
| WEG Störerhaftung bei Mietern | BGH, Urteil vom 21.03.2025, V ZR 1/24 | Vermietende Wohnungseigentümer können gegenüber der Gemeinschaft als mittelbare Handlungsstörer haften, wenn ihr Mieter unzulässig in Gemeinschaftseigentum eingreift. | https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&nr=141725 |

## Workflow-Gate

1. **Rolle klären:** Mieter, Vermieter, WEG-Eigentümer, Gemeinschaft, Verwalter, Beirat.
2. **Objekt klären:** Wohnraum, Gewerbe, Mischmiete, Wohnungseigentum, Sonder-/Gemeinschaftseigentum.
3. **Eilfristen zuerst:** Kündigung, Räumung, Mieterhöhung, WEG-Beschlussklage (§ 45 WEG: Klage 1 Monat, Begründung 2 Monate), Betriebskostenfrist.
4. **Quelle auswählen:** Mietspiegel/Landesverordnung, BGB, WEG, BetrKV, BGH/Amts-/Landgericht nur wenn frei geprüft.
5. **Output anschließen:** `mieterhoehung-pruefen-widersprechen`, `mietsenkungsverlangen`, `nebenkostenabrechnung-pruefen`, `mahnung-zahlungsverzug-mieter`, `weg-beschluss-anfechten`, `klageentwurf-amtsgericht`.

## Kurzkorrekturen für bestehende Workflows

- WEG-Sachen nach §§ 43 ff. WEG gehen erstinstanzlich grundsätzlich zum Amtsgericht der Belegenheit; nicht nach allgemeiner Streitwertlogik zum Landgericht springen.
- Bauliche Veränderungen: Beschluss/Anspruch, ordnungsmäßige Ausführung, Grenzen des § 20 Abs. 4 WEG und Kostenverteilung § 21 WEG getrennt prüfen.
- Schonfristzahlung heilt die fristlose Kündigung wegen Zahlungsverzugs, nicht automatisch eine hilfsweise ordentliche Kündigung; konkrete BGH-Linie live verifizieren.
- Mietpreisbremse nie ohne lokale Landesverordnung, Mietspiegel und Ausnahmen prüfen.
