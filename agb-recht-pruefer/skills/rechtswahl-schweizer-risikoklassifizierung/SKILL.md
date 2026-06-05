---
name: rechtswahl-schweizer-risikoklassifizierung
description: "Rechtswahl Schweizer Risikoklassifizierung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtswahl Schweizer Risikoklassifizierung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Rechtswahl Schweizer Risikoklassifizierung** im Plugin AGB-Klausel- und Verbraucherschutzprüfung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `agb-rechtswahl-schweizer-recht-rom-i` | Rechtswahl Schweizer Recht in AGB als Versuch dem deutschen AGB-Recht zu entkommen. Skill klaert Rom-I-VO Art. 3 freie Rechtswahl Art. 6 zwingender Verbraucherschutz Art. 9 Eingriffsnormen sowie die Pruefung ob §§ 305-310 BGB international zwingend sind. Behandelt die Konstellation deutscher Verwender mit Schweizer Tochter Schweizer Verwender mit deutschen Kunden und gemischte Faelle. Liefert Pruefraster und Klauselentwurf fuer rechtssichere Rechtswahlklauseln in Schweiz-Deutschland-Mandaten. Verweist auf agb-und-242-bgb-eingriffsnorm. |
| `agb-risikoklassifizierung-ampel` | Einstiegs- und Prüffeld für AGB Risikoklassifizierung Ampel: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-transparenzgebot-307-abs-1-satz-2` | AGB Transparenzgebot § 307 Abs. 1 Satz 2 BGB. Skill arbeitet die BGH-Linie zum Transparenzgebot aus Bestimmtheitserfordernis Verstaendlichkeit Vorhersehbarkeit der Klauselwirkung und Schutz vor verschachtelten Verweisen. Behandelt typische Verstoesse Cookie-Banner Preisanpassung Schiedsklauseln. Liefert Pruefraster. |
| `agb-und-242-bgb-eingriffsnorm` | Diskussion um § 242 BGB als Eingriffsnorm im Sinne Art. 9 Rom-I-VO. Skill problematisiert die in der Literatur vereinzelt vertretene These das gesamte AGB-Recht greife international durch weil § 242 BGB ein verbindlicher Grundsatz von Treu und Glauben sei. Liefert Pro- und Contra-Argumente Bedeutung der EuGH-Rechtsprechung zur Eingriffsnorm-Definition (Unamar Rs. C-184/12) und praktische Konsequenz fuer internationale Kanzleimandate. |
| `agb-und-cookie-einwilligung-dsgvo` | AGB und Cookie-Einwilligung nach DSGVO und TTDSG / TDDDG. Skill klaert die Wechselwirkung von AGB-rechtlichen Klauseln und datenschutzrechtlicher Einwilligung Anforderungen an die Einwilligung Differenzierung notwendige Cookies und optionale Cookies sowie BGH-Linie zur Einwilligung im Plattformkontext. Behandelt EuGH-Linie Planet49 und Folgejudikate. Liefert Pruefraster und Bannerentwurf. |

## Arbeitsweg

Im Plugin AGB-Klausel- und Verbraucherschutzprüfung gilt für **Rechtswahl Schweizer Risikoklassifizierung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `agb-rechtswahl-schweizer-recht-rom-i`

**Fokus:** Rechtswahl Schweizer Recht in AGB als Versuch dem deutschen AGB-Recht zu entkommen. Skill klaert Rom-I-VO Art. 3 freie Rechtswahl Art. 6 zwingender Verbraucherschutz Art. 9 Eingriffsnormen sowie die Pruefung ob §§ 305-310 BGB international zwingend sind. Behandelt die Konstellation deutscher Verwender mit Schweizer Tochter Schweizer Verwender mit deutschen Kunden und gemischte Faelle. Liefert Pruefraster und Klauselentwurf fuer rechtssichere Rechtswahlklauseln in Schweiz-Deutschland-Mandaten. Verweist auf agb-und-242-bgb-eingriffsnorm.

# Agb Rechtswahl Schweizer Recht Rom I

## Fachkern: Agb Rechtswahl Schweizer Recht Rom I

- **Klauselproblem (Agb Rechtswahl Schweizer Recht Rom I):** Rechtswahl Schweizer Recht in AGB als Versuch dem deutschen AGB-Recht zu entkommen. Skill klaert Rom-I-VO Art. 3 freie Rechtswahl Art. 6 zwingender Verbraucherschutz Art. 9 Eingriffsnormen sowie die Pruefung ob §§ 305-310 BGB international zwingend sind. Behandelt die Konstellation deutscher Verwender mit Schweizer Tochter Schweizer Verwender mit deutschen Kunden und gemischte Faelle. Liefert Pruefraster und Klauselentwurf fuer rechtssichere Rechtswahlklauseln in Schweiz-Deutschland-Mandaten. Verweist auf agb-und-242-bgb-eingriffsnorm.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Sofortfragen

1. Wer ist Verwender, wer ist Vertragspartner?
2. B2C oder B2B?
3. Sitz und Wohnsitz der Parteien?
4. Vertragsabschlussort und Erfuellungsort?
5. Bezug zum deutschen Markt (Werbung, deutsche Sprache, deutsche Domain)?

## Rom-I-VO

### Art. 3 Rom-I — Freie Rechtswahl
- Grundsatz: Parteien koennen das anwendbare Recht waehlen.
- Auch Schweizer Recht (Drittstaat) ist waehlbar; Art. 2 Rom-I.

### Art. 6 Rom-I — Verbraucherschutz
- Bei Verbrauchervertrag mit Geschaeftspartner, der Taetigkeit auf den Wohnsitzstaat des Verbrauchers ausrichtet ("ausgerichtete Taetigkeit"): trotz Rechtswahl gelten zwingende Verbraucherschutznormen des Heimatrechts.
- §§ 305-310 BGB sind solche zwingenden Verbraucherschutznormen.
- BGH-Linie: deutsches AGB-Recht greift bei deutschem Verbraucher und ausgerichteter Schweizer Taetigkeit durch.

### Art. 9 Rom-I — Eingriffsnormen
- Eingriffsnormen sind zwingende Bestimmungen, deren Beachtung als so entscheidend fuer den Staat angesehen wird, dass sie ungeachtet des nach den Rom-I-VO-Regeln anwendbaren Rechts anzuwenden sind.
- Sind § 307 BGB oder § 242 BGB Eingriffsnormen?
- BGH und h.M.: **§§ 305-310 BGB sind keine Eingriffsnormen** im Sinne Art. 9. Sie sind Schutznormen, aber sie regeln nicht das oeffentliche Interesse, sondern die Wertung des Verbraucherschutzes — diese Wertung ist ueber Art. 6 Rom-I bereits abgesichert.
- **§ 242 BGB als Eingriffsnorm?** Vereinzelt vertreten, aber abzulehnen. § 242 ist kein international zwingender Anwendungsbefehl, sondern eine Generalklausel des deutschen Privatrechts. Die Konstruktion "ueber § 242 BGB greift das gesamte AGB-Recht international durch" ist nicht haltbar.

### Art. 21 Rom-I — Ordre Public
- Anwendung des fremden Rechts kann ausgeschlossen werden, soweit sie offensichtlich mit der oeffentlichen Ordnung Deutschlands unvereinbar ist.
- Nur Kerngehalte (Vorsatzhaftungsausschluss, Verzicht auf Personenschaden) sind ordre public.

## B2B-Konstellation

- **Art. 6 Rom-I greift nicht** (kein Verbraucher).
- Wahl Schweizer Recht ist im B2B grundsaetzlich wirksam, auch um deutsches AGB-Recht zu umgehen.
- Grenzen: Eingriffsnormen, ordre public, Sondervorschriften wie Art. 8 Rom-I bei Arbeitsvertraegen.

## Praxisempfehlung

- Bei B2C: Schweizer Recht als Rechtswahl ist effektiv nur Wahl der Auslegungsbasis, nicht der zwingenden Vorschriften.
- Bei B2B: rechtssicher; Schiedsabrede im Schweizer Recht plus Schweizer Schiedsort ist effiziente Kombination.
- Achtung: Schweizer OR Art. 8 (Allgemeine Geschaeftsbedingungen) ist deutlich grobschnittiger als BGB §§ 305-310 — was den Aufwand reduziert, aber bei deutschem Gegenueber zu Akzeptanzproblemen fuehren kann.

## Pruefraster

1. B2C oder B2B?
2. Ausgerichtete Taetigkeit im Sinne Art. 6 Abs. 1 Buchst. b Rom-I?
3. Wahl Schweizer Recht formgerecht?
4. Zwingende deutsche Vorschriften nach Art. 6 oder Art. 9 Rom-I?
5. Ordre public einschlaegig?
6. Schiedsabrede parallel?

## Output

- Rechtswahlklauselentwurf.
- Memo "Schweizer Recht als Ausweg aus dem deutschen AGB-Recht — was funktioniert, was nicht".
- Schriftsatzbaustein im Streitfall.

## 2. `agb-risikoklassifizierung-ampel`

**Fokus:** Einstiegs- und Prüffeld für AGB Risikoklassifizierung Ampel: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich.

# AGB Risikoklassifizierung Ampel

## Fachkern: AGB Risikoklassifizierung Ampel

- **Klauselproblem (AGB Risikoklassifizierung Ampel):** sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Minimal-Intake

- Rolle: Verwender, Kunde, Verbraucher, Unternehmer, Plattform, Händler, Verband oder Prozessgegner.
- Klausel: Wortlaut, Fundstelle, Überschrift, Kontext, Version und Einbeziehungsweg.
- Vertrag: Vertragstyp, Hauptleistung, Preis-/Risikomodell, Laufzeit und Vertriebskanal.
- Ziel: Wirksamkeit prüfen, Risiko senken, härter entwerfen, redlinen, verhandeln oder verteidigen.
- Nachweis: Screenshots, Checkout, E-Mail, Angebot, Auftragsbestätigung, Archivversion oder Kundendaten.

## Prüfpfad

1. **Normenstand sichern:** Vor tragenden Aussagen BGB §§ 305 bis 310 auf Gesetze im Internet prüfen; bei Verbandsrisiko UKlaG ergänzen.
2. **Anwendungsbereich:** AGB-Eigenschaft, Einbeziehung, Individualabrede, Verbraucher-/Unternehmerstatus und Sondermaterie klären.
3. **Auslegung:** kundenfeindlichste vertretbare Auslegung, Überraschung, Mehrdeutigkeit und Transparenz prüfen.
4. **Inhaltskontrolle:** § 307 BGB als Grundprüfung, danach einschlägige Klauselverbote aus §§ 308, 309 BGB und § 310 BGB einordnen.
5. **Spezialfokus:** Bei AGB Risikoklassifizierung Ampel besonders auf wirtschaftlichen Zweck, versteckte Belastung, Verständlichkeit, Nachweisbarkeit und praxistaugliche Durchführung achten.
6. **Rechtsfolge:** Unwirksamkeit, gesetzliche Ersatzregel, Rückzahlung, Vertragsfortbestand, Prozess- und UKlaG-Risiko prüfen.
7. **Verbesserung:** mindestens eine sichere Ersatzfassung und bei Bedarf eine verhandelbare Fallback-Fassung formulieren.

## Aktuelle BGH-Linie zur Risikobewertung

### Risikofaktoren mit BGH-Bezug
- **Rot**: § 309 BGB-Verstoss in B2C eindeutig (z. B. Haftungsausschluss Leben/Koerper/Gesundheit, Aufrechnungsverbot fuer unbestrittene Forderungen).
- **Gelb**: § 307 BGB-Verstoss wahrscheinlich (z. B. unklare Anpassungsklauseln, Schriftformklausel fuer Anzeigen, fehlendes Loesungsrecht bei Preisanpassung).
- **Gruen**: Klausel an Gesetzeswortlaut orientiert oder BGH-anerkannt.

### Klassische Rot-Klauseln (BGH-aktuell)
- Schriftformklausel im Verbraucherkontext: BGH VIII ZR 91/19.
- Aufrechnungs-/Zurueckbehaltungsverbot fuer unbestrittene Forderungen: BGH VIII ZR 67/17.
- Einseitige Preisanpassung ohne Loesungsrecht: BGH VIII ZR 178/08, BGH VIII ZR 244/10.
- Vorausverzichtsklauseln auf Schadensersatz: BGH VIII ZR 23/19.

### Aktuelle Diskussion
- DSGVO-konforme Einwilligungsklauseln, Cookie-Banner: BGH I ZR 7/16 ("Planet49"); BGH I ZR 26/19.
- AGB im Plattformhandel (Amazon, eBay) — BGH zur Marktstellung und § 307 BGB.
- Update-Klauseln (§ 327f BGB) seit 2022 — BGH-Folgejudikate im Aufbau.

### Pruefraster
1. Vertragsart und Rollencheck (B2C/B2B/B2B2C).
2. Klauseltyp (Haupt-/Nebenleistung/AGB-Modul).
3. § 309 BGB-Treffer? — Rot.
4. § 308 BGB Treffer mit Wertungsabwaegung? — Gelb.
5. § 307 BGB Generalklausel? — Pruefung im Einzelfall.
6. BGH-Linie konsultieren.

## Output

| Punkt | Befund |
| --- | --- |
| Klauselzweck | ... |
| AGB-Kontrolle | ja/nein/unklar, warum |
| Hauptangriff | ... |
| Verteidigung | ... |
| Risiko | Grün/Gelb/Rot |
| Bessere Fassung | ... |
| offene Tatsachen | ... |

## Qualitätsregeln

- Keine Scheinzitate. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine geltungserhaltende Reduktion als Standardlösung anbieten.
- Bei B2B nicht so tun, als sei alles frei verhandelbar; Transparenz und Leitbild bleiben wichtig.
- Bei B2C streng, verständlich und dokumentationsfähig formulieren.
- Wenn eine Klausel wirtschaftlich gewollt, aber rechtlich riskant ist: Risiko offen labeln und Fallback anbieten.

## Quellenanker

Siehe `references/QUELLEN.md`, `references/PRUEFLOGIK.md` und `references/KLAUSELFAMILIEN.md`.

## 3. `agb-transparenzgebot-307-abs-1-satz-2`

**Fokus:** AGB Transparenzgebot § 307 Abs. 1 Satz 2 BGB. Skill arbeitet die BGH-Linie zum Transparenzgebot aus Bestimmtheitserfordernis Verstaendlichkeit Vorhersehbarkeit der Klauselwirkung und Schutz vor verschachtelten Verweisen. Behandelt typische Verstoesse Cookie-Banner Preisanpassung Schiedsklauseln. Liefert Pruefraster.

# Agb Transparenzgebot 307 Abs 1 Satz 2

## Fachkern: Agb Transparenzgebot 307 Abs 1 Satz 2

- **Klauselproblem (Agb Transparenzgebot 307 Abs 1 Satz 2):** AGB Transparenzgebot § 307 Abs. 1 Satz 2 BGB. Skill arbeitet die BGH-Linie zum Transparenzgebot aus Bestimmtheitserfordernis Verstaendlichkeit Vorhersehbarkeit der Klauselwirkung und Schutz vor verschachtelten Verweisen. Behandelt typische Verstoesse Cookie-Banner Preisanpassung Schiedsklauseln. Liefert Pruefraster.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Norm

- § 307 Abs. 1 Satz 2 BGB: "Eine unangemessene Benachteiligung kann sich auch daraus ergeben, dass die Bestimmung nicht klar und verstaendlich ist."
- BGH staendige Rspr.: Klausel muss Vertragspartner die wirtschaftlichen Folgen klar erkennbar machen.

## Verstoesse

### Verschachtelte Verweise
- Klausel verweist auf "die jeweiligen Bestimmungen unter ziffer 8.3 Abs. 2" — bei mehrfacher Verschachtelung intransparent.

### Unklare Begriffe
- "Marktgaengiger Preis", "branchenueblich" — fuer Verbraucher schwer fassbar.

### Verbergung in Preislisten
- Wesentliche Bedingungen in Preisliste statt im Vertrag — intransparent.

## BGH-Linie

- BGH XI ZR 26/20 zu Banken-AGB.
- BGH I ZR 232/15 zu Werbeklauseln.
- BGH VIII ZR 178/08 zu Energiepreisanpassung.

## Pruefraster

1. Welche Klausel?
2. Bestimmtheit gegeben?
3. Verstaendlichkeit fuer typischen Vertragspartner?
4. Wirtschaftliche Folgen vorhersehbar?
5. Verschachtelung problematisch?

## Output

- Klauselentwurf "transparente Version".
- Schriftsatzbaustein.

## 4. `agb-und-242-bgb-eingriffsnorm`

**Fokus:** Diskussion um § 242 BGB als Eingriffsnorm im Sinne Art. 9 Rom-I-VO. Skill problematisiert die in der Literatur vereinzelt vertretene These das gesamte AGB-Recht greife international durch weil § 242 BGB ein verbindlicher Grundsatz von Treu und Glauben sei. Liefert Pro- und Contra-Argumente Bedeutung der EuGH-Rechtsprechung zur Eingriffsnorm-Definition (Unamar Rs. C-184/12) und praktische Konsequenz fuer internationale Kanzleimandate.

# Agb Und 242 Bgb Eingriffsnorm

## Aufgabe

Skill fuer Mandate mit internationalem Bezug, in denen die Frage gestellt wird, ob § 242 BGB als Eingriffsnorm (Art. 9 Rom-I-VO) das gesamte deutsche AGB-Recht international durchsetzt.

## Argumentation pro Eingriffsnormcharakter

- § 242 BGB ist seit dem Reichsgericht und BGH eine "Generalklausel mit Verfassungsrang" (so vereinzelte Stimmen).
- Treu und Glauben sei eine universale rechtsethische Wertung, ohne die das deutsche Privatrecht nicht denkbar ist.
- §§ 307 ff. BGB seien Konkretisierungen des § 242 BGB; wenn § 242 international zwingend ist, dann auch die Konkretisierungen.
- Faktischer Verbraucherschutz koennte sonst durch Rechtswahl ausgehebelt werden.

## Argumentation contra (herrschende Meinung)

- **EuGH "Unamar" (Rs. C-184/12, 17.10.2013)**: Eingriffsnormen werden eng definiert — sie muessen "fuer die Wahrung der politischen, sozialen oder wirtschaftlichen Organisation eines Mitgliedstaats als so entscheidend angesehen werden, dass ihre Befolgung [...] vorzunehmen ist".
- § 242 BGB ist eine Auslegungs- und Konkretisierungsregel, kein international zwingender Anwendungsbefehl.
- Art. 6 Rom-I-VO regelt den Verbraucherschutz autonom und abschliessend; die Spezialnorm verdraengt einen Rueckgriff auf Art. 9.
- BGH IX ZR 119/14 (Az im Digitalisat verifizieren): keine Erstreckung des AGB-Rechts via § 242 BGB auf fremdrechtliche Vertraege.
- Praktische Folge: Schweizer / englisches / US-Recht in B2B-Vertraegen ist wirksam, ohne dass deutsches AGB-Recht ueber § 242 BGB durchschlaegt.

## Praktische Folgen

- Verwender mit deutschen B2B-Mandanten koennen mit Rechtswahl Schweizer Recht erheblichen AGB-Spielraum gewinnen.
- Bei B2C bleibt Art. 6 Rom-I — der ist die einzige relevante Schutzklippe.
- Schiedsklauseln in B2B sind frei verwertbar.

## Pruefraster

1. Behauptet der Mandant § 242 BGB als Eingriffsnorm?
2. Welche Konstellation (B2C vs. B2B)?
3. Welche EuGH-Rechtsprechung gilt aktuell (Unamar, Da Silva Martins, etc.)?
4. Welche BGH-Linie ist einschlaegig?
5. Welche praxisnahe Loesung?

## Output

- Memo zur § 242-Eingriffsnorm-These mit Gegenargumenten.
- Schriftsatzbaustein "Replik: § 242 BGB ist nicht international zwingend".
- Verweis auf agb-rechtswahl-schweizer-recht-rom-i.

## 5. `agb-und-cookie-einwilligung-dsgvo`

**Fokus:** AGB und Cookie-Einwilligung nach DSGVO und TTDSG / TDDDG. Skill klaert die Wechselwirkung von AGB-rechtlichen Klauseln und datenschutzrechtlicher Einwilligung Anforderungen an die Einwilligung Differenzierung notwendige Cookies und optionale Cookies sowie BGH-Linie zur Einwilligung im Plattformkontext. Behandelt EuGH-Linie Planet49 und Folgejudikate. Liefert Pruefraster und Bannerentwurf.

# Agb Und Cookie Einwilligung Dsgvo

## Fachkern: Agb Und Cookie Einwilligung Dsgvo

- **Klauselproblem (Agb Und Cookie Einwilligung Dsgvo):** AGB und Cookie-Einwilligung nach DSGVO und TTDSG / TDDDG. Skill klaert die Wechselwirkung von AGB-rechtlichen Klauseln und datenschutzrechtlicher Einwilligung Anforderungen an die Einwilligung Differenzierung notwendige Cookies und optionale Cookies sowie BGH-Linie zur Einwilligung im Plattformkontext. Behandelt EuGH-Linie Planet49 und Folgejudikate. Liefert Pruefraster und Bannerentwurf.
- **AGB-Weiche:** Einbeziehung (§ 305 BGB), überraschende Klausel (§ 305c BGB), Transparenz (§ 307 Abs. 1 S. 2 BGB), Inhaltskontrolle (§§ 307-309 BGB), Rechtsfolge (§ 306 BGB) und Prozess-/Verbandsrisiko sauber trennen.
- **Beleglogik:** Originalklausel, Vertragsumfeld, Verwendungsnachweis, Verhandlungsspuren, Kundengruppe, Marktstandard und wirtschaftliche Wirkung als Matrix erfassen.
- **Arbeitsprodukt:** Klauselampel, Redline, Ersatzformulierung, Verhandlungsposition und gerichtsfeste Kurzbegründung mit Live-Check amtlicher Normenquellen.

## Norm

- DSGVO Art. 6 Abs. 1 Buchst. a (Einwilligung).
- DSGVO Art. 7 (Bedingungen fuer Einwilligung).
- TDDDG (Telekommunikation-Digitale-Dienste-Datenschutzgesetz, frueher TTDSG), insbesondere § 25.
- EuGH "Planet49" Rs. C-673/17 (01.10.2019): aktive Einwilligung erforderlich; Voreinstellung "ja" unzulaessig.

## Cookie-Banner-Anforderungen

### Notwendige Cookies
- Sitzungs- und Sicherheitscookies erfordern keine Einwilligung (Art. 5 Abs. 3 ePrivacy-RL).

### Tracking-Cookies
- Aktive Einwilligung erforderlich.
- "Akzeptieren" und "Ablehnen" muessen gleichwertig prominent sein.
- BGH I ZR 7/16 (Cookie-Einwilligung): Vorabauswahl mit Haekchen unwirksam.

### Dark Patterns
- Manipulative Gestaltung der Einwilligung ist DSGVO-Verstoss.
- LfDI BW und BfDI haben mehrfach Bussgelder verhaengt.

## Verhaeltnis zu AGB

- Einwilligung in Cookies ist nicht Bestandteil der AGB.
- AGB-Klausel "Mit Annahme dieser AGB stimmt der Kunde der Verwendung von Cookies zu" ist unwirksam (§ 7a UWG, fehlende Differenzierung).

## Pruefraster

1. Welche Cookies werden gesetzt?
2. Einwilligung aktiv und differenziert eingeholt?
3. Verhaeltnis zu AGB getrennt geregelt?
4. Bussgeldrisiko?
5. Werbliche Folgen?

## Output

- Cookie-Banner-Entwurf.
- AGB-Klausel zur Datenverarbeitung.
- Compliance-Memo.
