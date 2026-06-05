---
name: krankenversicherung-pkv-vertrag-antrag-betriebliche
description: "PKV Vertrag Antrag Betriebliche: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PKV Vertrag Antrag Betriebliche

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **PKV Vertrag Antrag Betriebliche** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-028-pkv-vertrag-antrag-gesundheitsfragen-anzeigepflicht` | Vorvertragliche Anzeigepflicht in der PKV (§§ 19–22 VVG): Gesundheitsfragen, Risikoausschlüsse, Leistungsausschlüsse, Anfechtung wegen arglistiger Täuschung. |
| `kv-039-betriebliche-krankenversicherung-und-datenschutz` | Betriebliche Krankenversicherung (bKV): Gruppenverträge, Leistungsumfang, Arbeitgeber-Datenschutz, steuerliche Behandlung und Portabilität. |
| `kv-002-gkv-mitgliedschaft-pflicht-freiwillig-familienversicherun` | Versicherungspflicht (§ 5 SGB V), freiwillige Versicherung (§ 9 SGB V) und Familienversicherung (§ 10 SGB V) prüfen und abgrenzen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **PKV Vertrag Antrag Betriebliche**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-028-pkv-vertrag-antrag-gesundheitsfragen-anzeigepflicht`

**Fokus:** Vorvertragliche Anzeigepflicht in der PKV (§§ 19–22 VVG): Gesundheitsfragen, Risikoausschlüsse, Leistungsausschlüsse, Anfechtung wegen arglistiger Täuschung.

# PKV-Vertrag: Antrag, Gesundheitsfragen und Anzeigepflicht

## Skill-Zweck

Beim Abschluss eines PKV-Vertrags besteht eine **vorvertragliche Anzeigepflicht**: Wer Gesundheitsfragen falsch beantwortet, riskiert Vertragsanfechtung oder Leistungsausschluss. Dieser Skill klärt Pflichten, Grenzen und Rechtsbehelfe.

## Rechtlicher Rahmen

- **§ 19 VVG** – Anzeigepflicht vor Vertragsschluss (gefahrerhebliche Umstände)
- **§ 20 VVG** – Ausschluss der Anzeigepflichtverletzung bei Kenntnis des Versicherers
- **§ 21 VVG** – Rücktritt und Kündigung wegen Anzeigepflichtverletzung
- **§ 22 VVG** – Anfechtung wegen arglistiger Täuschung
- **§ 28 VVG** – Obliegenheiten, Kausalitätsprinzip
- **§ 194 VVG** – Leistungspflicht PKV (Grundsatz medizinische Notwendigkeit)
- **MB/KK 2009** §§ 1–10 (Musterbedingungen PKV)
- BGH IV ZR 91/14 (Anzeigepflichtverletzung, Kausalität), BGH IV ZR 311/14

## Prüfschema Anzeigepflichtverletzung

| Stufe | Versicherer-Recht | Voraussetzung |
|-------|------------------|---------------|
| Arglist (§ 22 VVG) | Anfechtung, Rückwirkend ex tunc | Vorsätzliche Täuschungsabsicht |
| Vorsatz (§ 21 Abs. 1 VVG) | Rücktritt ohne Frist | Bewusst unwahre Antwort |
| Grobe Fahrlässigkeit | Rücktritt; Leistungskürzung möglich | Hätte wissen müssen |
| Einfache Fahrlässigkeit | Nur Kündigung mit Frist | Versehen, ohne Gewissen |
| Keine Fahrlässigkeit | Kein Recht; nur Prämienanpassung | Unkenntnis ohne Verschulden |

## Prüfprogramm

### Schritt 1 – Gesundheitsfragen im Antrag analysieren
- Welche Fragen wurden gestellt? (Genaue Formulierung entscheidend)
- Zeitraum: Meist 3–5 Jahre, manchmal 10 Jahre rückwirkend
- Diagnosen, Behandlungen, Krankenhausaufenthalte, Medikamente
- Unbewusst vergessene Erkrankungen: kein Vorsatz, möglicherweise keine Fahrlässigkeit

### Schritt 2 – Kausalitätsprüfung
- § 21 Abs. 2 VVG: Kein Rücktrittsrecht wenn verschwiegener Umstand für den Versicherungsfall nicht kausal war
- Beispiel: Rücken-Vorerkrankung verschwiegen → Herzinfarkt → kein Kausalzusammenhang → kein Rücktritt wegen Herzbehandlung
- Kausalität muss der Versicherer nachweisen

### Schritt 3 – Fristen prüfen
- Rücktrittsrecht: 1 Monat nach Kenntnis der Verletzung (§ 21 Abs. 1 Satz 2 VVG)
- Anfechtungsrecht Arglist: keine Verjährung, aber verwirkt bei langem Zuwarten
- Absolute Grenze: Vertrag besteht 10 Jahre → kein Rücktritt mehr, nur Kündigung

### Schritt 4 – Verteidigung gegen Rücktritt
- War Frage unklar formuliert? (ambigue Formulierungen gehen zu Lasten des Versicherers)
- Hat Versicherer Risiko von sich aus im Antragsgespräch ausgeblendet? (§ 20 VVG)
- Untersuchung durch Arzt des Versicherers: Arzt hätte Erkrankung feststellen müssen?
- Eigenrecherche: PKV durfte eigene Voruntersuchung vornehmen; Pflicht dann weniger streng

### Schritt 5 – Leistungsausschluss als Alternative
- Statt Rücktritt: Versicherer bietet Vertragserhaltung mit Risikoausschluss (§ 19 Abs. 4 VVG)
- Risikoausschluss: Versicherungsschutz ausgenommen für bestimmte Erkrankung
- Sollte bevorzugt werden: Versicherungsschutz bleibt für alles andere erhalten

## Typische Fallen

- **Bagatellerkrankungen vergessen**: Erkältungen, banale Beschwerden sind keine anzeigegefahrenerhebliche Umstände; nicht jede Arztbesuche muss angegeben werden.
- **Psychische Erkrankungen**: Besonders häufig Streitpunkt; Depression, Burnout gelten als anzeigeerheblich.
- **Rückwirkende Anfechtung**: Versicherer zahlt gar nichts zurück und verlangt alle Prämien; Klage auf Rückzahlung.
- **Maklerformular ≠ Versicherungsformular**: Angaben beim Makler binden nur wenn an Versicherer weitergeleitet.

## Output-Formate

- Anzeigepflicht-Checkliste (Antragsvorbereitung)
- Widerspruch gegen Vertragsanfechtung
- Kausalitätsanalyse (Erkrankung vs. Versicherungsfall)
- Klageschrift gegen PKV-Rücktritt
- Risikoausschluss-Verhandlungsstrategie

## Quellen

- [§ 19 VVG – Anzeigepflicht](https://www.gesetze-im-internet.de/vvg_2008/__19.html)
- [§ 21 VVG – Rücktrittsrecht](https://www.gesetze-im-internet.de/vvg_2008/__21.html)
- [§ 22 VVG – Arglistanfechtung](https://www.gesetze-im-internet.de/vvg_2008/__22.html)
- [BGH IV ZR 91/14](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [MB/KK 2009 – PKV-Musterbedingungen](https://www.pkv.de)
- [dejure.org § 19 VVG](https://dejure.org/gesetze/VVG/19.html)
- [PKV-Ombudsmann](https://www.pkv-ombudsmann.de)

## 2. `kv-039-betriebliche-krankenversicherung-und-datenschutz`

**Fokus:** Betriebliche Krankenversicherung (bKV): Gruppenverträge, Leistungsumfang, Arbeitgeber-Datenschutz, steuerliche Behandlung und Portabilität.

# Betriebliche Krankenversicherung und Datenschutz

## Skill-Zweck

Die betriebliche Krankenversicherung (bKV) ist ein wachsendes Benefit-Instrument. Dieser Skill klärt **Vertragsstrukturen, Datenschutzpflichten des Arbeitgebers, steuerliche Behandlung und was bei Arbeitgeberwechsel passiert**.

## Rechtlicher Rahmen

- **§ 192 VVG** – PKV-Grundnorm (bKV als kollektiver PKV-Tarif)
- **§ 3 Nr. 62 EStG** – Steuerfreiheit AG-Zuschuss bis 600 €/Jahr
- **§ 26 BDSG** – Beschäftigtendatenschutz (AG darf keine Diagnosen aus bKV erhalten)
- **DSGVO Art. 9** – Gesundheitsdaten besonderer Schutz
- **§ 75 BetrVG** – Mitbestimmung Betriebsrat bei bKV-Einführung
- **HGB §§ 87 ff.** – Provisionen und Maklerrecht bei bKV-Vermittlung
- Versicherungsaufsicht: BaFin überwacht auch bKV-Gruppenverträge

## bKV-Grundstruktur

| Merkmal | Inhalt |
|---------|--------|
| Vertragstyp | Gruppenvertrag AG ↔ PKV; AN als versicherte Person |
| Leistungsumfang | Stationäre Zusatzleistungen, Zahnersatz, Vorsorgechecks, Sehhilfen |
| Risikoprüfung | Meist keine bei Gruppen (vereinfachte Annahmepolitik) |
| Beitrag | AG zahlt Prämie; ggf. AG-/AN-Anteil |
| Portabilität | Bei AG-Wechsel meist Einzelübertrag möglich |

## Prüfprogramm

### Schritt 1 – Vertragsanalyse
- Welche Leistungen deckt die bKV ab? (Stationär, Zahn, Vorsorge, Sehhilfen, alternativ)
- Ausschlusslisten: vorbestehende Erkrankungen oft ausgeschlossen
- Gruppenvertrag: alle AN oder selektiv (nur leitende AN)?

### Schritt 2 – Datenschutz (§ 26 BDSG, DSGVO Art. 9)
- AG hat kein Recht auf Kenntnisnahme von Diagnosen oder Behandlungen aus bKV
- bKV-Anbieter darf Daten nicht an AG weitergeben
- Anonymisierte Auswertungen (z.B. Inanspruchnahme-Statistiken): zulässig wenn nicht rückführbar auf Einzelperson
- Datenschutzerklärung der bKV prüfen

### Schritt 3 – Steuerliche Behandlung
- Beitrag AG als Arbeitslohn: Grundsatz (§ 19 EStG)
- Steuerfreiheit: § 3 Nr. 62 EStG → bis 600 €/Jahr steuerfrei (Sachzuwendung)
- Über 600 €: Sachbezug, zu versteuern; Pauschalbesteuerung (§ 40 EStG) möglich
- Sozialversicherungsfrei: bKV-Beiträge unter 50 €/Monat (Bagatellgrenze)

### Schritt 4 – Mitbestimmung Betriebsrat
- Betriebsrat hat Mitbestimmungsrecht (§ 87 Abs. 1 Nr. 8 BetrVG: betriebliche Lohngestaltung)
- Einführung, Änderung, Abschaffung der bKV: Zustimmung des BR erforderlich
- Betriebsvereinbarung empfohlen: Leistungsumfang, Beitragsteilung, Datenschutz

### Schritt 5 – Portabilität und AG-Wechsel
- Bei Kündigung/AG-Wechsel: AN kann Vertrag oft in Eigenfinanzierung übernehmen
- Neue Risikoprüfung: Je nach Vertrag; manche bKV erlauben nahtlose Weiterführung
- Optionsrecht: AN muss innerhalb definierter Frist Übernahme erklären

## Typische Fallen

- **Datenweitergabe durch Versicherer**: Wenn PKV Statistiken an AG liefert die Individual-Rückschlüsse erlauben → DSGVO-Verstoß.
- **Ausschlüsse vorbestehender Erkrankungen**: bKV-Antragsformular enthält vereinfachte Gesundheitsfragen; trotzdem Ausschlüsse möglich.
- **Steuerliche Falle bei Prämienbonus**: Wenn bKV Bonus zurückzahlt → zu versteuerndes Einkommen.
- **Betriebsrat-Zustimmung fehlt**: bKV-Einführung ohne BR-Mitbestimmung → anfechtbar.

## Output-Formate

- bKV-Datenschutzprüfungs-Protokoll
- Betriebsvereinbarung bKV (Muster)
- Steuervorteilsberechnung bKV
- Portabilitäts-Optionsschreiben
- BR-Anhörungsprotokoll bKV

## Quellen

- [§ 3 Nr. 62 EStG – Steuerfreiheit](https://www.gesetze-im-internet.de/estg/__3.html)
- [§ 26 BDSG – Beschäftigtendatenschutz](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)
- [§ 87 BetrVG – Mitbestimmung](https://www.gesetze-im-internet.de/betrvg/__87.html)
- [DSGVO Art. 9](https://dsgvo-gesetz.de/art-9-dsgvo/)
- [PKV-Verband bKV](https://www.pkv.de)
- [dejure.org § 26 BDSG](https://dejure.org/gesetze/BDSG/26.html)

## 3. `kv-002-gkv-mitgliedschaft-pflicht-freiwillig-familienversicherun`

**Fokus:** Versicherungspflicht (§ 5 SGB V), freiwillige Versicherung (§ 9 SGB V) und Familienversicherung (§ 10 SGB V) prüfen und abgrenzen.

# GKV-Mitgliedschaft: Pflicht, freiwillig, Familienversicherung

## Skill-Zweck

Dieser Skill klärt, **wie eine Person in der gesetzlichen Krankenversicherung versichert ist** – als Pflichtmitglied, freiwilliges Mitglied oder beitragsfrei über die Familienversicherung. Die Einordnung entscheidet über Beitraghöhe, Leistungsumfang und Wechselmöglichkeiten.

## Rechtlicher Rahmen

- **§ 5 SGB V** – Pflichtversicherung: Arbeitnehmer, Rentner, Bezieher von ALG, Studenten, Praktikanten
- **§ 6 SGB V** – Versicherungsfreiheit: Überschreiten der Jahresarbeitsentgeltgrenze (JAEG), Beamte, Selbstständige
- **§ 7 SGB V** – Versicherungsfreiheit geringfügig Beschäftigter
- **§ 9 SGB V** – Freiwillige Versicherung: Beitritt nach Ende der Pflichtversicherung, Fristen, Optionsgründe
- **§ 10 SGB V** – Familienversicherung: Voraussetzungen (kein eigenes Einkommen > Geringfügigkeitsgrenze, kein PKV-Schutz, kein Anspruch aus eigenem Versicherungsverhältnis)
- **§ 240 SGB V** – Beitragsbemessung freiwillig Versicherter (Einkommensmindestbeitrag)
- **§ 175 SGB V** – Ausübung des Kassenwahlrechts
- BSG B 12 KR 12/18 R (Familienversicherung und Einkommensgrenze)

## Abgrenzungsmatrix

| Status | Rechtsgrundlage | Beitragspflicht | Kassenwahlrecht |
|--------|----------------|-----------------|-----------------|
| Pflichtmitglied Arbeitnehmer | § 5 Abs. 1 Nr. 1 SGB V | AN- und AG-Anteil | Eingeschränkt (Bindungsfrist § 175 Abs. 4) |
| Pflichtmitglied Rentner (KVdR) | § 5 Abs. 1 Nr. 11 SGB V | Aus Rente + Versorgungsbezügen | Wie Arbeitnehmer |
| Freiwilliges Mitglied | § 9 SGB V | Mindestbeitrag § 240 | Jederzeit kündbar mit Frist |
| Familienversicherung | § 10 SGB V | Beitragsfrei | Kein eigenes Wahlrecht |
| Pflichtmitglied ALG-Bezieher | § 5 Abs. 1 Nr. 2 SGB V | Aus ALG-Bemessungsgrundlage | Eingeschränkt |

## Prüfprogramm

### Schritt 1 – Pflichtversicherung prüfen (§ 5 SGB V)
- Ist die Person Arbeitnehmer mit Entgelt unterhalb der JAEG (2025: 73.800 €/Jahr)?
- Renten-, ALG-, Krankengeld-, Elterngeld-Bezug, der Pflichtversicherung auslöst?
- Student an staatlich anerkannter Hochschule, Altersgrenze 25 Jahre beachten (§ 5 Abs. 1 Nr. 9)?
- Kein Ausschlussgrund nach § 6 SGB V (Beamter, hauptberuflich Selbstständiger)?

### Schritt 2 – Versicherungsfreiheit prüfen (§ 6 SGB V)
- JAEG-Überschreitung: Gilt grundsätzlich nur für Arbeitnehmer; Vorjahresentgelt maßgeblich
- Beamtenrecht: Landesbeamte meist beitrageberechtigungsfrei (Beihilfe)
- Kirchenbeamte, Richter: je nach Landesrecht

### Schritt 3 – Freiwillige Versicherung (§ 9 SGB V)
- Beitrittsfrist: 3 Monate nach Ende der Pflichtversicherung (§ 9 Abs. 2 Nr. 1 SGB V)
- Beitrittsmöglichkeit auch nach Ende der Familienversicherung (§ 9 Abs. 2 Nr. 2)
- Beitrag: Mindestbemessungsgrundlage 1.178,33 € (2025), tatsächliches Einkommen maßgeblich
- Einkommensnachweise: Steuerbescheid, Gewinn-und-Verlust-Rechnung, Kontoauszüge

### Schritt 4 – Familienversicherung (§ 10 SGB V)
- Voraussetzungen kumulativ: kein eigenes Einkommen > 505 €/mtl. (2025, Geringfügigkeitsgrenze), kein anderweitiger KV-Schutz, Hauptmitglied in GKV versichert
- Besonderheit: Ehegatte ohne eigenes Einkommen, studierende Kinder bis 25
- Ausschluss bei Überschreitung der Einkommensgrenze (auch geringfügige Beschäftigung kann schaden)

## Typische Fallen

- **JAEG-Überschreitung im Vorjahr**: Begründet Versicherungsfreiheit erst zum Folgejahr, nicht sofort.
- **Einkommensbegriff § 10 SGB V**: Gesamteinkommen (§ 16 SGB IV), nicht nur Arbeitslohn – Kapitaleinkünfte, Mieteinnahmen einrechnen.
- **Beitrittsfrist versäumt**: Nach 3 Monaten kein freiwilliger Beitritt mehr möglich – Wechsel in PKV oder Auffangpflichtversicherung (§ 5 Abs. 1 Nr. 13) prüfen.
- **Kindergeld und Familienversicherung**: Anspruch auf Kindergeld ist unabhängig; Familienversicherung gilt bis 25, bei Behinderung ohne Altersgrenze (§ 10 Abs. 2 Nr. 4 SGB V).

## Output-Formate

- Statusfeststellungs-Memo (Pflicht / freiwillig / Familie)
- Beitragsberechnung mit Einkommensnachweisliste
- Widerspruchsentwurf gegen falsche Statusfeststellung
- Fristenplan für Kassenwechsel oder freiwilligen Beitritt

## Quellen

- [§ 5 SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 9 SGB V](https://www.gesetze-im-internet.de/sgb_5/__9.html)
- [§ 10 SGB V](https://www.gesetze-im-internet.de/sgb_5/__10.html)
- [§ 240 SGB V](https://www.gesetze-im-internet.de/sgb_5/__240.html)
- [BSG – Familienversicherung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband – Beitragsbemessung](https://www.gkv-spitzenverband.de)
- [dejure.org SGB V § 10](https://dejure.org/gesetze/SGB_V/10.html)
## Hinweis: Beitragsrecht und Meldepflichten

- Pflichtversicherte: Beitrag aus Arbeitsentgelt, paritätisch geteilt (§ 249 SGB V)
- Freiwillig Versicherte: Gesamteinkommen maßgeblich (§ 240 SGB V), Nachweis gegenüber Kasse
- Familienversicherung endet automatisch bei Überschreiten der Einkommensgrenze → Kassenmeldepflicht
- Änderungsmeldung innerhalb von 2 Wochen (§ 175 Abs. 4 SGB V analog); Säumnis → rückwirkende Beitragsnachforderung

## Weiterführende Quellen

- [§ 9 SGB V – Freiwillige Versicherung](https://www.gesetze-im-internet.de/sgb_5/__9.html)
- [§ 10 SGB V – Familienversicherung](https://www.gesetze-im-internet.de/sgb_5/__10.html)
- [§ 240 SGB V – Beiträge freiwillig Versicherter](https://www.gesetze-im-internet.de/sgb_5/__240.html)
