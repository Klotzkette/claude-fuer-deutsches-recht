---
name: krankenversicherung-widerspruch-gegen-leistungsablehnung
description: "Widerspruch Gegen Leistungsablehnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Widerspruch Gegen Leistungsablehnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Widerspruch Gegen Leistungsablehnung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-024-widerspruch-gegen-leistungsablehnung-frist-und-begruendun` | Widerspruchsverfahren nach §§ 83 ff. SGG: Fristen, Form, Begründungsanforderungen, Widerspruchsstellen und typische Fehler. |
| `kv-025-eilverfahren-sozialgericht-medizinische-dringlichkeit` | Einstweiliger Rechtsschutz nach § 86b SGG: Anordnungsanspruch, Anordnungsgrund, medizinische Dringlichkeit und Glaubhaftmachung. |
| `kv-049-unfallversicherung-oder-krankenkasse-zustaendigkeitsstrei` | Abgrenzung gesetzliche Unfallversicherung (SGB VII) und GKV bei Arbeitsunfällen: Zuständigkeit, Vorleistungspflicht der GKV, Erstattungsansprüche. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Widerspruch Gegen Leistungsablehnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-024-widerspruch-gegen-leistungsablehnung-frist-und-begruendun`

**Fokus:** Widerspruchsverfahren nach §§ 83 ff. SGG: Fristen, Form, Begründungsanforderungen, Widerspruchsstellen und typische Fehler.

# Widerspruch gegen Leistungsablehnung: Frist und Begründung

## Skill-Zweck

Der Widerspruch ist das erste Rechtsmittel gegen Ablehnungsbescheide der Krankenkasse. Dieser Skill sichert **Fristen, Form und Substanz** des Widerspruchs und bereitet eine verwertbare Begründung vor.

## Rechtlicher Rahmen

- **§ 83 SGG** – Statthaftigkeit des Widerspruchs
- **§ 84 SGG** – Widerspruchsfrist: 1 Monat ab Bekanntgabe
- **§ 85 SGG** – Widerspruchsbescheid
- **§ 86 SGG** – Aufschiebende Wirkung des Widerspruchs
- **§ 37 SGB X** – Bekanntgabe (3-Tage-Fiktion)
- **§ 36 SGB X** – Rechtsbehelfsbelehrung; ohne Belehrung: 1-Jahres-Frist (§ 66 SGG)
- **§ 78 SGG** – Vorverfahren als Zulässigkeitsvoraussetzung der Klage
- BSG B 1 KR 6/20 R (Begründungsanforderungen Widerspruch)

## Widerspruchs-Checkliste

| Schritt | Inhalt | Frist |
|---------|--------|-------|
| Zustellung feststellen | Datum der Zustellung, 3-Tage-Fiktion | Tag der Bekanntgabe |
| Widerspruchsfrist berechnen | 1 Monat ab Bekanntgabe | § 84 SGG |
| Widerspruch fristwahrend einlegen | Einfaches Schreiben reicht für Fristwahrung | Vor Fristablauf |
| Begründung nachreichen | Nach Akteneinsicht und Prüfung | Freigestellt, aber zeitnah |
| Widerspruchsbehörde | In der Regel die Kasse selbst oder Widerspruchsausschuss | – |

## Prüfprogramm

### Schritt 1 – Frist berechnen
- Bekanntgabedatum: Datum des Bescheids + 3 Tage (§ 37 Abs. 2 SGB X)
- Berechnung: Monatsfrist läuft ab; wenn Monatsende Wochenende/Feiertag → nächster Werktag
- Fristende verlegt sich wenn keine Rechtsbehelfsbelehrung: 1 Jahr
- Übersendungsnachweis sichern: Einschreiben bei Einreichung des Widerspruchs

### Schritt 2 – Fristwahrenden Widerspruch einlegen
- Widerspruch muss vor Fristablauf eingehen (nicht abgesandt werden)
- Form: schriftlich oder persönlich zu Protokoll (§ 84 Abs. 2 Satz 3 SGG)
- Mindestinhalt: Bezeichnung des angefochtenen Bescheids, Wille Widerspruch einzulegen
- Begründung kann nachgereicht werden: „Der Widerspruch wird gesondert begründet."

### Schritt 3 – Akteneinsicht und Prüfung
- § 25 SGB X: Akteneinsicht unmittelbar nach Widerspruchseinlegung beantragen
- Bescheid analysieren: Welcher Ablehnungsgrund? Normgrundlage? MDK-Gutachten vorhanden?
- Prüfprogramm: medizinisch, rechtlich, beweistechnisch

### Schritt 4 – Widerspruchsbegründung
- Gliederung: Sachverhalt → Rechtliche Begründung → Beweisangebote
- Medizinische Argumente: behandelnder Arzt, Leitlinien, Fachliteratur
- Rechtliche Argumente: Normtext, BSG-Rechtsprechung, G-BA-Richtlinien
- Beweisangebote: Arztbriefe, Befundberichte, eigenes Gutachten beifügen

### Schritt 5 – Widerspruchsbescheid abwarten
- Kasse muss „ohne unangemessene Verzögerung" entscheiden
- Keine gesetzliche Frist für Widerspruchsbescheid; bei Untätigkeit nach 3 Monaten: Untätigkeitsklage § 88 SGG
- Widerspruchsbescheid als Grundlage für Klage beim Sozialgericht

## Typische Fallen

- **Falsche Adressierung**: Widerspruch an Arzt oder Behörde geschickt statt Kasse → keine Fristwahrung.
- **Per E-Mail**: Nur wenn Kasse E-Mail als Eingangskanal bestätigt hat; unsichere Rechtslage.
- **Begründung statt Widerspruch**: Nur Begründung eingereicht, aber nicht explizit Widerspruch → Frist läuft weiter.
- **Abhilfebescheid**: Kasse heilt Bescheid teilweise → Rest bleibt angefochten; weiterverfolgen.

## Output-Formate

- Widerspruchsschreiben (fristwahrend, Muster)
- Vollständige Widerspruchsbegründung (Muster)
- Fristenkalender
- Akteneinsichtsantrag
- Untätigkeitsklage-Vorbereitung

## Quellen

- [§ 84 SGG – Widerspruchsfrist](https://www.gesetze-im-internet.de/sgg/__84.html)
- [§ 37 SGB X – Bekanntgabe](https://www.gesetze-im-internet.de/sgb_10/__37.html)
- [§ 83 SGG – Vorverfahren](https://www.gesetze-im-internet.de/sgg/__83.html)
- [§ 25 SGB X – Akteneinsicht](https://www.gesetze-im-internet.de/sgb_10/__25.html)
- [BSG Verfahrensrecht](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org SGG § 84](https://dejure.org/gesetze/SGG/84.html)

## 2. `kv-025-eilverfahren-sozialgericht-medizinische-dringlichkeit`

**Fokus:** Einstweiliger Rechtsschutz nach § 86b SGG: Anordnungsanspruch, Anordnungsgrund, medizinische Dringlichkeit und Glaubhaftmachung.

# Eilverfahren Sozialgericht: Medizinische Dringlichkeit

## Skill-Zweck

Bei drohender Gesundheitsverschlechterung kann nicht auf den Abschluss des Widerspruchsverfahrens gewartet werden. Dieser Skill bereitet den **Eilantrag beim Sozialgericht (§ 86b SGG)** vor: Anordnungsanspruch, Anordnungsgrund und Glaubhaftmachung.

## Rechtlicher Rahmen

- **§ 86b Abs. 2 SGG** – Einstweilige Anordnung: Anordnungsanspruch + Anordnungsgrund
- **§ 86b Abs. 1 SGG** – Anordnung der aufschiebenden Wirkung (bei Verwaltungsakten)
- **§ 192 SGG** – Missbrauchsgebühr (selten, aber Warnung)
- **Art. 19 Abs. 4 GG** – Effektiver Rechtsschutz
- **BVerfG 1 BvR 347/98** – Grundrechtsorientierte Auslegung: keine Ablehnung bei lebensbedrohlicher Erkrankung
- **BVerfGE 79, 69** – Einstweiliger Rechtsschutz muss effektiv sein
- BSG B 3 KR 6/14 R (einstweiliger Rechtsschutz Hilfsmittel), BSG B 1 KR 1/16 R (Eilanspruch Arzneimittel)

## Zwei-Säulen-Struktur Eilantrag

| Element | Inhalt | Nachweis |
|---------|--------|----------|
| Anordnungsanspruch | Materieller Leistungsanspruch besteht | Glaubhaftmachung, nicht Vollbeweis |
| Anordnungsgrund | Eilbedürftigkeit: unzumutbares Abwarten | Eidesstattliche Versicherung, ärztliches Attest |

## Prüfprogramm

### Schritt 1 – Eilbedürftigkeit feststellen
- Droht bei Zuwarten irreversibler Schaden (Gesundheitsverschlechterung, Invalidität, Todesgefahr)?
- Wartezeit auf Widerspruchsbescheid: typisch 3–6 Monate → zu lang bei medizinischer Dringlichkeit
- Konkrete Frist: Behandlungstermin, Operation, Therapiebeginn

### Schritt 2 – Anordnungsanspruch formulieren
- Leistungsanspruch aus SGB V skizzieren (§ 27, § 33, § 40 etc.)
- BSG-Maßstab: plausible Rechtspositionen, keine abschließende Prüfung im Eilverfahren
- Medizinische Notwendigkeit: ärztliches Attest mit konkreter Aussage über Dringlichkeit

### Schritt 3 – Glaubhaftmachung (§ 294 ZPO analog)
- Kein Vollbeweis nötig; überwiegende Wahrscheinlichkeit ausreichend
- Mittel: eidesstattliche Versicherung des Versicherten, ärztliches Attest, Befundberichte
- Kombination: mehrere Belege zur Absicherung

### Schritt 4 – Antragstellung beim SG
- Zuständiges Sozialgericht: am Wohnort des Versicherten
- Antrag schriftlich; keine Anwaltspflicht im Eilverfahren vor SG
- Inhalt: Antragstenor (was genau begehrt wird), Sachverhalt, Rechtliche Begründung, Glaubhaftmachungsmittel
- Beschleunigung: „dringend" kennzeichnen; telefonische Ankündigung möglich

### Schritt 5 – Besonderheiten bei bestimmten Leistungen
- Krankengeld: Eilantrag bei drohender Obdachlosigkeit, Zwangsräumung
- Hilfsmittel: Eilantrag wenn Grundbedürfnis (Mobilität, Kommunikation) betroffen
- Psychotherapie: Eilantrag nur bei akuter Suizidalität o.ä. (hohe Schwelle)
- Stationäre Behandlung: Krankenhaus-Aufnahme oft direkt; Kasse nachträglich konfrontiert

## Typische Fallen

- **Zu früh Eilantrag**: Noch kein Ablehnungsbescheid → kein Rechtsschutzbedürfnis; zuerst beantragen und abwarten (kurz).
- **Hauptsache vergessen**: Eilantrag sichert nur vorläufige Regelung; parallel Widerspruch und ggf. Klage führen.
- **Folgenabwägung**: Gericht wägt Folgen der Ablehnung gegen Folgen der Stattgabe ab → Folgen für Antragsteller müssen überwiegen.
- **BVerfG-Grundsatz**: Bei lebensbedrohlicher Erkrankung darf Gericht nicht mit formalen Gründen ablehnen.

## Output-Formate

- Eilantragsschreiben (§ 86b SGG, Muster)
- Eidesstattliche Versicherung (Muster)
- Ärztliches Attest-Briefing (Was muss drin stehen?)
- Checkliste Anordnungsanspruch/-grund
- Notfall-Aktionsplan (was tun wenn Kasse nicht reagiert)

## Quellen

- [§ 86b SGG – Einstweilige Anordnung](https://www.gesetze-im-internet.de/sgg/__86b.html)
- [BVerfG 1 BvR 347/98](https://www.bverfg.de/e/rs19990109_1bvr034798.html)
- [§ 294 ZPO – Glaubhaftmachung](https://www.gesetze-im-internet.de/zpo/__294.html)
- [BSG Eilrechtsprechung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 86b SGG](https://dejure.org/gesetze/SGG/86b.html)
- [Art. 19 Abs. 4 GG](https://www.gesetze-im-internet.de/gg/art_19.html)

## 3. `kv-049-unfallversicherung-oder-krankenkasse-zustaendigkeitsstrei`

**Fokus:** Abgrenzung gesetzliche Unfallversicherung (SGB VII) und GKV bei Arbeitsunfällen: Zuständigkeit, Vorleistungspflicht der GKV, Erstattungsansprüche.

# Unfallversicherung oder Krankenkasse: Zuständigkeitsstreit

## Skill-Zweck

Bei Arbeitsunfällen und Berufskrankheiten ist die Berufsgenossenschaft (BG) zuständig, nicht die GKV. Dieser Skill klärt die **Zuständigkeitsabgrenzung, Vorleistungspflicht der GKV und Erstattungsansprüche zwischen den Trägern**.

## Rechtlicher Rahmen

- **§ 8 SGB VII** – Arbeitsunfall: betrieblicher Bereich, innerer Zusammenhang
- **§ 9 SGB VII** – Berufskrankheit (BK-Liste der DGUV)
- **§ 11 SGB V** – GKV nachrangig gegenüber Unfallversicherung
- **§ 105 SGB X** – Erstattungsanspruch bei Vorleistung des nachrangigen Trägers
- **§ 16 SGB V** – Ruhen der GKV-Leistungen bei vorrangiger Leistung der UV
- **§ 34 SGB VII** – Heilbehandlung durch BG
- BSG B 2 U 23/14 R (Arbeitsunfall-Definition), BSG B 1 KR 8/04 R (Vorleistung GKV)

## Zuständigkeitsabgrenzung

| Situation | Zuständig | Rechtsgrundlage |
|-----------|---------|----------------|
| Arbeitsunfall während Arbeit | BG (SGB VII) | § 8 SGB VII |
| Wegeunfall (Arbeit ↔ Wohnung) | BG (SGB VII) | § 8 Abs. 2 SGB VII |
| Freizeitunfall | GKV (SGB V) | § 11 SGB V |
| Berufskrankheit (BK-Liste) | BG (SGB VII) | § 9 SGB VII |
| Private Erkrankung ähnlich BK | GKV | Kein SGB-VII-Bezug |
| Streitige Zuordnung | GKV muss vorleisten | § 105 SGB X |

## Prüfprogramm

### Schritt 1 – Arbeitsunfall-Definition (§ 8 SGB VII)
- Zeitlicher und örtlicher Zusammenhang mit versicherter Tätigkeit?
- Innerer Zusammenhang: Tätigkeit erfolgte zur Erfüllung arbeitsvertraglicher Pflichten
- Wegeunfall: direkter Weg Wohnung-Arbeit; Umwege prüfen (Kindertagesstätte erlaubt, § 8 Abs. 2 Nr. 2a SGB VII)

### Schritt 2 – Vorleistungspflicht GKV (§ 105 SGB X)
- GKV muss vorleisten wenn BG-Zuständigkeit unklar
- GKV-Träger informiert BG über Vorleistung; Erstattungsanspruch entsteht
- Versicherter muss GKV über möglichen Arbeitsunfall informieren

### Schritt 3 – Meldung an BG
- Arbeitgeber muss Arbeitsunfall der zuständigen BG melden (§ 193 SGB VII)
- Versicherter sollte direkt D-Arzt (Durchgangsarzt) aufsuchen; kein normaler Kassenarzt
- D-Arzt: vertragsarzt der BG; für Unfallbehandlung erforderlich

### Schritt 4 – BG-Leistungen
- Heilbehandlung: vollständig, keine Zuzahlung, keine Eigenbehalte
- Verletztenrente: bei dauerhafter Minderung der Erwerbsfähigkeit (MdE > 20 %)
- Verletztengeld: während Arbeitsunfähigkeit (höher als GKV-Krankengeld: 80 % des Regelentgelts)

### Schritt 5 – Streit über Zuordnung
- BG lehnt Arbeitsunfall-Anerkennung ab: Widerspruch bei BG; dann Klage beim SG
- GKV lehnt Vorleistung ab: Widerspruch bei GKV
- Gleichzeitig beiden Trägern Anzeige erstatten; nicht abwarten

## Typische Fallen

- **D-Arzt-Zwang**: Für BG-Leistungen muss D-Arzt konsultiert werden; normaler Kassenarzt nicht ausreichend.
- **Arbeitsweg-Umweg**: Umwege wegen Kinderbetreuung sind privilegiert; andere Umwege nicht.
- **Freizeitunfall in Betriebssportgruppe**: Nur wenn Betriebssport offiziell organisiert; nicht privater Sport.
- **Berufskrankheits-Anerkennung**: BK-Liste ist abschließend; neue Erkrankungen nur durch BK-Ergänzungsverfahren oder § 2 Abs. 2 SGB VII (Quasi-BK).

## Output-Formate

- Arbeitsunfall-Meldebogen
- D-Arzt-Überweisungsanforderung
- BG-Widerspruch (Anerkennung Arbeitsunfall)
- GKV-Vorleistungsanfrage
- Verletztengeld-Berechnung

## Quellen

- [§ 8 SGB VII – Arbeitsunfall](https://www.gesetze-im-internet.de/sgb_7/__8.html)
- [§ 105 SGB X – Vorleistung](https://www.gesetze-im-internet.de/sgb_10/__105.html)
- [§ 34 SGB VII – BG-Heilbehandlung](https://www.gesetze-im-internet.de/sgb_7/__34.html)
- [BSG B 2 U 23/14 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [DGUV – Deutsche Gesetzliche Unfallversicherung](https://www.dguv.de)
- [dejure.org § 8 SGB VII](https://dejure.org/gesetze/SGB_VII/8.html)
