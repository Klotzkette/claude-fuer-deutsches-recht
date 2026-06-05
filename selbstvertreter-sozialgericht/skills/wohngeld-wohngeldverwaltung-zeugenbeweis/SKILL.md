---
name: wohngeld-wohngeldverwaltung-zeugenbeweis
description: "Wohngeld Wohngeldverwaltung Zeugenbeweis: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wohngeld Wohngeldverwaltung Zeugenbeweis

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Wohngeld Wohngeldverwaltung Zeugenbeweis** im Plugin Selbstvertretung vor dem Sozialgericht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wohngeld-wohngeldverwaltung` | Wohngeld nach dem Wohngeldgesetz (WoGG). Skill erklaert die Mietzuschuss/Lastenzuschuss-Logik die Einkommens- und Mietobergrenzen Antragsverfahren und Wohngeldreform 2023. Liefert Pruefraster. |
| `zeugenbeweis-sozialgericht-373-zpo-analog` | Zeugen vor dem Sozialgericht. §§ 373 ff. ZPO analog. Beweisthema Adressen Zeugenvernehmung. Wann lohnt sich Zeugenbeweis für Buerger ohne Anwalt. |
| `zugunstenantrag-44-sgb-x-bestandskraft` | Zugunstenantrag nach § 44 SGB X: Antrag auf Aufhebung eines bestandskraeftigen rechtswidrigen Verwaltungsakts zugunsten des Buergers. Klaert Voraussetzungen Frist Rueckwirkung bis zu 4 Jahre. Skill liefert Antragsvorlage. |
| `zulassungsgrenzen-check-sozialgericht` | Zulassungs- und Rechtsmittelgrenzen im Sozialgerichtsverfahren: § 144 SGG 750 EUR, laufende Leistungen über ein Jahr, Erstattungsstreitigkeiten 10.000 EUR, Berufungszulassung, Nichtzulassungsbeschwerde, Revision, BSG-Anwaltszwang und Kostenrisiken. |

## Arbeitsweg

Im Plugin Selbstvertretung vor dem Sozialgericht gilt für **Wohngeld Wohngeldverwaltung Zeugenbeweis**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wohngeld-wohngeldverwaltung`

**Fokus:** Wohngeld nach dem Wohngeldgesetz (WoGG). Skill erklaert die Mietzuschuss/Lastenzuschuss-Logik die Einkommens- und Mietobergrenzen Antragsverfahren und Wohngeldreform 2023. Liefert Pruefraster.

# Wohngeld Wohngeldverwaltung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Wohngeld Wohngeldverwaltung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Anspruch

§ 3 WoGG:

- Mietzuschuss fuer Mieter.
- Lastenzuschuss fuer Eigentuemer.

## Voraussetzungen

- Wohnsitz in der gefoerderten Wohnung.
- Einkommen unter Hoechstgrenze.
- Miete (oder Lasten) innerhalb der Hoechstgrenze.

## Berechnungsformel

- Mietobergrenze nach Mietstufe (I-VII) und Haushaltsgroesse.
- Einkommen unter Hoechstgrenze nach Haushaltsgroesse.
- Wohngeld = Funktion von Miete und Einkommen.

## Reform 2023

- Wohngeld Plus mit erhoehten Saetzen.
- Heiz- und Klima-Komponente.
- Mehr Berechtigte.

## Antrag

- Bei der Wohngeldstelle (Stadt, Kreis).
- Mietvertrag, Einkommensnachweise, Personalien.

## Verhaeltnis zu Buergergeld

- Wohngeld vorrangig vor SGB II.
- Wenn Bedarf nicht gedeckt: SGB II ergaenzend.

## Pruefraster

1. Welcher Zuschuss?
2. Mietstufe und Hoechstgrenze?
3. Einkommen unter Grenze?
4. Antrag rechtzeitig (Rueckwirkung max. 1 Monat)?
5. Vorrang vor Buergergeld?

## 2. `zeugenbeweis-sozialgericht-373-zpo-analog`

**Fokus:** Zeugen vor dem Sozialgericht. §§ 373 ff. ZPO analog. Beweisthema Adressen Zeugenvernehmung. Wann lohnt sich Zeugenbeweis für Buerger ohne Anwalt.

# Zeugen vor dem Sozialgericht

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeugen vor dem Sozialgericht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es?

Manchmal weiss eine andere Person etwas Wichtiges fuer Ihre Sache. Diese Person kann als Zeuge / Zeugin auftreten. Diese Skill zeigt, wann das Sinn macht und wie Sie das beantragen.

## In einfacher Sprache

Andere Menschen koennen erzaehlen, was sie gesehen haben. Das nennt man Zeugen. Wir zeigen Ihnen, wie und wann das hilft.

## Wann brauchen Sie diese Skill?

- Sie haben Personen, die etwas Wichtiges fuer Sie wissen.
- Sie wollen wissen, wie Sie diese benennen.
- Sie ueberlegen, ob ein Zeuge die Sache klaeren kann.

## Fachbegriffe (kurz erklaert)

- **Zeuge**: Person mit eigener Wahrnehmung von Tatsachen.
- **Beweisthema**: Worueber soll der Zeuge aussagen.
- **Zeugnisverweigerungsrecht**: Manche Personen muessen / duerfen nicht aussagen (Familienangehoerige, Aerzte ohne Schweigepflichtsentbindung).
- **Sachverstaendiger Zeuge**: Person mit Fachwissen, die zugleich Beobachtungen gemacht hat (z.B. behandelnder Arzt).

## Rechtsgrundlagen

- **§§ 373 ff. ZPO analog (i.V.m. § 118 SGG)** — Zeugenbeweis.
- **§ 376 ZPO analog** — Auslagen / Verdienstausfall.
- **§§ 383, 384 ZPO analog** — Zeugnisverweigerungsrecht.

## Schritt-fuer-Schritt-Anleitung

### Schritt 1 — Wann lohnt sich Zeugenbeweis?

Im Sozialrecht selten allein entscheidend. Beweise meistens ueber Atteste / Gutachten. Aber gut bei:

- **Pflegestreit**: Angehoerige, die Pflege machen, als Zeugen.
- **GdB / Behinderung im Alltag**: Nachbarn, die taegliche Schwierigkeiten beobachten.
- **Berufsschutz**: Kollegen, die Arbeitsfaehigkeit kennen.
- **Sanktion SGB II**: Personen, die den Anlass beobachtet haben.
- **Unfallhergang**: Augenzeugen.

### Schritt 2 — Wer kann Zeuge sein?

- Jeder, der etwas selbst wahrgenommen hat.
- Familienangehoerige sind okay, haben aber Zeugnisverweigerungsrecht (§ 383 Abs. 1 Nr. 1-3 ZPO).
- Aerzte: brauchen Schweigepflichtsentbindung.

### Schritt 3 — Zeugenbenennung in der Klage

```
Beweisangebot:

Zeugin: Frau Anna Mueller, Beispielstr. 1, 12345 Stadt, Tel. 030/123456

Beweisthema: Frau Mueller hat in den vergangenen 6 Monaten taeglich an meiner Wohnung Pflege geleistet. Sie kann zum konkreten zeitlichen Umfang der Pflege (Koerperpflege, Mobilitaet, Nahrungszubereitung) Stellung nehmen.
```

### Schritt 4 — Mehrere Zeugen

Sie koennen mehrere Zeugen benennen. Jeder mit klarem Beweisthema.

### Schritt 5 — Was der Zeuge muss

- Vor Gericht erscheinen, wenn geladen.
- Wahr aussagen (Strafbarkeit § 153 StGB).
- Vorbereitet sein auf die Befragung.

### Schritt 6 — Was passiert vor Gericht?

- Vorsitzender Richter fragt den Zeugen zur Person.
- Belehrt ueber Wahrheitspflicht.
- Stellt Fragen zum Beweisthema.
- Sie koennen erlaeutern, was Sie noch wissen wollen.
- Behoerde kann fragen.
- Protokoll wird angefertigt.

### Schritt 7 — Auslagen-Erstattung fuer den Zeugen

Zeuge bekommt aus der Staatskasse (JVEG):

- Fahrtkosten
- Verdienstausfall
- Geringe Entschaedigung

Auch bei Sozialgericht (§ 1 JVEG i.V.m. § 197a SGG analog). Sagen Sie das dem Zeugen vorab.

## Worauf Sie besonders achten muessen

- **Adresse exakt**: Ohne Adresse kann das Gericht nicht laden.
- **Beweisthema konkret**: Allgemeines "Frau X weiss alles" reicht nicht.
- **Familienangehoerige**: Pruefen, ob Aussage gewuenscht / moeglich.
- **Sachverstaendiger Zeuge** (Arzt): besser oft als reiner Zeuge.

## Typische Fehler

- Beweisthema zu allgemein → konkret
- Adresse fehlt → unwirksam
- Zeuge hat nur vom Hoeren-sagen Kenntnis → wenig wertvoll
- Zeuge unzuverlaessig → besser nicht benennen

## Querverweise

- `orientierung-selbstvertreter-sozialgericht` — Einstieg in das SG-Verfahren
- `beweismittel-im-sozialgericht-uebersicht` — Ueberblick
- `amtsermittlungsgrundsatz-103-sgg` — Amtsermittlung
- `medizinische-gutachten-strategie-laien` — bei medizinischen Fragen lieber Gutachten

## Quellen und Aktualitaet

Stand: 05/2026. § 118 SGG verweist auf ZPO. JVEG-Saetze fuer Zeugenentschaedigung pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `zugunstenantrag-44-sgb-x-bestandskraft`

**Fokus:** Zugunstenantrag nach § 44 SGB X: Antrag auf Aufhebung eines bestandskraeftigen rechtswidrigen Verwaltungsakts zugunsten des Buergers. Klaert Voraussetzungen Frist Rueckwirkung bis zu 4 Jahre. Skill liefert Antragsvorlage.

# Zugunstenantrag 44 Sgb X Bestandskraft

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zugunstenantrag 44 Sgb X Bestandskraft` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Anwendungsfall

Ein bestandskraeftiger Bescheid ist rechtswidrig — der Buerger hat Leistungen zu Unrecht nicht erhalten oder zu Unrecht erstattet. § 44 SGB X ermoeglicht Korrektur im Nachhinein.

## Voraussetzungen § 44 Abs. 1 SGB X

- Verwaltungsakt ist bestandskraeftig (Frist abgelaufen oder Rechtsbehelf verworfen).
- Bei Erlass des VA wurde das Recht unrichtig angewandt oder ist von einem Sachverhalt ausgegangen der sich als unrichtig erweist.
- Folge: Sozialleistung wurde nicht oder zu niedrig erbracht oder zu Unrecht Beitrag erhoben.

## Voraussetzungen § 44 Abs. 2 SGB X

- Verwaltungsakt mit Dauerwirkung — Aufhebung nach Ermessen.

## Frist

- Antrag jederzeit moeglich.
- Rueckwirkung der Leistung: bis zu 4 Jahre vor Antragstellung.

## Verhaeltnis zum Widerspruch

- Widerspruch ist die regelmaessige Korrekturschiene.
- Zugunstenantrag tritt erst nach Bestandskraft.

## Vorlage

"Hiermit beantrage ich nach § 44 SGB X die Aufhebung des bestandskraeftigen Bescheids vom [...] und Festsetzung der zu Unrecht nicht gewaehrten Sozialleistung. Begruendung: [...] Die Rueckwirkung bitte ich auf 4 Jahre festzusetzen."

## Pruefraster

1. Bescheid bestandskraeftig?
2. Rechtswidrigkeit (falsche Rechtsanwendung oder falscher Sachverhalt)?
3. Nicht oder zu niedrige Leistung?
4. Antrag schriftlich gestellt?
5. Rueckwirkungsfrist beruecksichtigt?

## 4. `zulassungsgrenzen-check-sozialgericht`

**Fokus:** Zulassungs- und Rechtsmittelgrenzen im Sozialgerichtsverfahren: § 144 SGG 750 EUR, laufende Leistungen über ein Jahr, Erstattungsstreitigkeiten 10.000 EUR, Berufungszulassung, Nichtzulassungsbeschwerde, Revision, BSG-Anwaltszwang und Kostenrisiken.

# Zulassungsgrenzen-Check Sozialgericht

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zulassungsgrenzen-Check Sozialgericht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill prüft, ob nach einem Urteil des Sozialgerichts die Berufung zum Landessozialgericht ohne Zulassung möglich ist, ob die Berufung zugelassen werden muss oder ob eine Nichtzulassungsbeschwerde in Betracht kommt. Er erklärt die Schwellen so, dass Bürger sie selbst nachvollziehen können.

## Kernwerte Stand Mai 2026

| Thema | Grenze | Norm |
|---|---:|---|
| Berufung bei Geld-, Dienst- oder Sachleistung | Zulassung nötig, wenn Beschwer 750 EUR nicht übersteigt | § 144 Abs. 1 S. 1 Nr. 1 SGG |
| Wiederkehrende oder laufende Leistungen | Berufung ohne Wertgrenze, wenn mehr als ein Jahr betroffen ist | § 144 Abs. 1 S. 2 SGG |
| Erstattungsstreit Behörden/juristische Personen öffentlichen Rechts | Zulassung nötig, wenn 10.000 EUR nicht überstiegen | § 144 Abs. 1 S. 1 Nr. 2 SGG |
| Zulassungsgründe | Grundsatz, Divergenz, Verfahrensmangel | § 144 Abs. 2 SGG |
| Berufungsfrist | 1 Monat | § 151 SGG |
| Nichtzulassungsbeschwerde | 1 Monat | § 145 SGG |
| Revision | Zulassung nötig | § 160 SGG |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfablauf

### 1. Entscheidung lesen

Prüfen Sie im Urteil:

- Wurde die Berufung zugelassen?
- Gibt es eine Rechtsmittelbelehrung?
- Welcher Betrag oder Zeitraum ist betroffen?
- Geht es um Geld, Sachleistung, Dienstleistung oder Status?

### 2. Beschwer berechnen

Beschwer bedeutet: Was fehlt Ihnen durch das Urteil?

Beispiele:

- Krankenkasse verweigert Hilfsmittel im Wert von 1.200 EUR: Berufung grundsätzlich möglich.
- Jobcenter-Sanktion 300 EUR: Berufung nur bei Zulassung oder Nichtzulassungsbeschwerde.
- Bürgergeld für 14 Monate: Berufung möglich, weil laufende Leistungen für mehr als ein Jahr betroffen sind.
- Pflegegrad-Streit mit monatlicher Dauerleistung: Zeitraum genau prüfen.

### 3. Zulassung prüfen

Wenn Wertgrenze nicht erreicht und keine laufenden Leistungen über mehr als ein Jahr betroffen sind, prüfen:

| Grund | Bedeutung |
|---|---|
| Grundsätzliche Bedeutung | Frage betrifft viele Fälle oder ungeklärte Rechtsfrage |
| Divergenz | SG weicht von LSG, BSG, Gemeinsamen Senat oder BVerfG ab |
| Verfahrensmangel | Zum Beispiel rechtliches Gehör, Beweisantrag, Amtsermittlung |

### 4. Vertretung prüfen

- SG und LSG: Bürger dürfen sich selbst vertreten.
- BSG: Vertretungszwang nach § 73 Abs. 4 SGG. Rechtzeitig Anwalt, Sozialverband oder zugelassene Vertretung prüfen.

## Ausgabeformat

**Rechtsmittel-Check**
| Frage | Ergebnis | Ampel |
|---|---|---|
| Berufung zugelassen? | | |
| Beschwer über 750 EUR? | | |
| Laufende Leistungen über mehr als 1 Jahr? | | |
| Zulassungsgrund erkennbar? | | |
| Frist gesichert? | | |
| Anwalt/Sozialverband nötig? | | |

**Konsequenz**
[Berufung einlegen, Nichtzulassungsbeschwerde prüfen, Urteil akzeptieren, PKH/Anwalt/Sozialverband einschalten.]

**Nächste Skills**
- `berufung-lsg-144-sgg-wertgrenze-750`
- `berufung-zulassung-besondere-bedeutung`
- `anwaltszwang-pruefen-73-sgg`
- `nichtzulassungsbeschwerde-bsg-160a-sgg` nur nach einem LSG-Urteil ohne Revisionszulassung.

## Qualitätsregeln

- Immer zwischen Berufung, Nichtzulassungsbeschwerde und Revision unterscheiden.
- Fristdatum konkret berechnen oder fehlende Zustellung markieren.
- Bei BSG-Verfahren nie suggerieren, dass Bürger allein handeln können.
- Bei Kostenfreiheit § 183 SGG trotzdem § 109 SGG, Mutwillenskosten und eigene Anwaltskosten erwähnen.
