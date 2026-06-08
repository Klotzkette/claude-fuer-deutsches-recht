---
name: entfristung-klageschrift-anwalt-laie
description: "Entfristung Klageschrift Anwalt Laie im Plugin Arbeitsrecht: prüft konkret Anwaltliche Klageschrift Entfristungsklage mit Hauptantrag, Schritt-für-Schritt Klageschrift Entfristungsklage für, Statusabfrage Entfristungsklage, Rechtsfolge unwirksamer Befristung nach § 16 Satz 1 TzBfG. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Entfristung Klageschrift Anwalt Laie

## Arbeitsbereich

**Entfristung Klageschrift Anwalt Laie** ordnet den Fall über die tragenden Prüfungslinien: Anwaltliche Klageschrift Entfristungsklage mit Hauptantrag, Schritt-für-Schritt Klageschrift Entfristungsklage für, Statusabfrage Entfristungsklage. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `entfristung-klageschrift-anwalt-baustein` | Anwaltliche Klageschrift Entfristungsklage mit Hauptantrag und Hilfsanträgen; Weiterbeschaeftigungsantrag; strukturierte Begründung nach § 14 Abs. 4 TzBfG und Sachgrundprüfung; Beweisangebote im BAG-Zitierstil. |
| `entfristung-klageschrift-laie-baustein` | Schritt-für-Schritt Klageschrift Entfristungsklage für Laien: Rubrum; Feststellungsantrag Unbefristetheit; Begründungsbausteine für Schriftformmangel und fehlenden Sachgrund; Beweisangebote; Pflicht-Disclaimer. |
| `entfristung-laie-oder-anwalt-frage` | Statusabfrage Entfristungsklage: Anwalt oder Laie; bei Laie Warnungen und Empfehlung anwaltlicher Beratung; kein Mandatsverhältnis; Hinweis auf § 17 TzBfG Drei-Wochen-Frist als kritischste Ausschlussfrist. |
| `entfristung-rechtsfolge-16-tzbfg-unbefristet` | Rechtsfolge unwirksamer Befristung nach § 16 Satz 1 TzBfG: Vertrag gilt als auf unbestimmte Zeit geschlossen; Möglichkeit der fruehesten ordentlichen Kündigung zum vereinbarten Ende nach § 16 Satz 2 TzBfG; Ansprüche Annahmeverzug; Weiterbeschaeftigungsantrag. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `entfristung-klageschrift-anwalt-baustein`

**Fokus:** Anwaltliche Klageschrift Entfristungsklage mit Hauptantrag und Hilfsanträgen; Weiterbeschaeftigungsantrag; strukturierte Begründung nach § 14 Abs. 4 TzBfG und Sachgrundprüfung; Beweisangebote im BAG-Zitierstil.

### Klageschrift Entfristungsklage — Anwaltliche Version

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Klageschrift Entfristungsklage — Anwaltliche Version` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor Erstellung der Klageschrift

1. Fristlage: Wann endet der Vertrag? § 17 TzBfG-Frist noch offen?
2. Welcher Unwirksamkeitsgrund? (Schriftformmangel § 14 Abs. 4 / kein Sachgrund § 14 Abs. 1 / Vorbeschäftigungsverbot § 14 Abs. 2 Satz 2)
3. Weiterbeschäftigungsantrag (GS BAG 27.02.1985) gewünscht?
4. Hilfsweise Auflösungsantrag (§§ 9, 10 KSchG i.V.m. § 17 Satz 2 TzBfG)?
5. Streitwert vorläufig 3 Bruttomonatsgehälter (§ 42 Abs. 2 GKG)
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- § 17 TzBfG — Klagefrist 3 Wochen ab vereinbartem Vertragsende
- § 14 Abs. 4 TzBfG i.V.m. § 126 BGB — Schriftformerfordernis
- § 16 Satz 1 TzBfG — Rechtsfolge unwirksamer Befristung (gilt als unbefristet)
- § 14 Abs. 1 TzBfG — Sachgrundprüfung (8 Sachgründe)
- §§ 9, 10 KSchG i.V.m. § 17 Satz 2 TzBfG — Auflösungsantrag auf Abfindung
- § 42 Abs. 2 GKG — Streitwert Befristungsklage (3 Monatsverdienste)
- § 12a ArbGG — kein Kostenerstattungsanspruch in erster Instanz

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Vorprüfung (Checkliste)

- [ ] Dreiwochenfrist § 17 TzBfG gewahrt
- [ ] Schriftform § 14 Abs. 4 TzBfG geprüft
- [ ] Sachgrund geprüft (§ 14 Abs. 1 TzBfG)
- [ ] Vorbeschäftigungsverbot geprüft (§ 14 Abs. 2 Satz 2 TzBfG)
- [ ] Mandant über Kostenrisiko belehrt (§ 12a ArbGG)
- [ ] Vollmacht liegt vor

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Entfristungsklage nach § 17 TzBfG | Klageschrift-Muster unten; Drei-Wochen-Frist beachten |
| Variante A — Mandant will keine Klage aber Abfindung | Aussergerichtliche Einigung als Alternative vor Klageerhebung |
| Variante B — Befristung offensichtlich unwirksam | Starkes Druckmittel; Vergleichsverhandlung vor Einreichung erwaegen |
| Variante C — Kettenbefristung mit mehreren Vertraegen | Gesamte Kette pruefen; ggf. mehrere Klagebaustein-Varianten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Klageschrift-Muster

---

An das

**Arbeitsgericht [ORT]**

**Klageschrift**

in dem Rechtsstreit

[NAME], [ANSCHRIFT]

— Kläger —

Prozessbevollmächtigte: Rechtsanwältin/Rechtsanwalt [NAME], [KANZLEI], Az.: [AZ]

gegen

[ARBEITGEBERIN], vertreten durch [VERTRETUNGSBERECHTIGTE], [ANSCHRIFT]

— Beklagte —

**Streitwert:** Vorläufig [3 × BMONAT] EUR (§ 42 Abs. 2 GKG)

---

**KLAGEANTRÄGE**

Der Kläger beantragt:

1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien nicht durch die in dem Arbeitsvertrag vom [DATUM] enthaltene Befristung zum [VEREINBARTES ENDE] beendet worden ist, sondern als unbefristetes Arbeitsverhältnis über diesen Zeitpunkt hinaus zu den bisherigen Bedingungen fortbesteht (§§ 17, 16 Satz 1 TzBfG).

2. Die Beklagte wird verurteilt, den Kläger bis zur rechtskräftigen Entscheidung über Klageantrag zu 1) zu den bisherigen Arbeitsbedingungen als [BERUFSBEZEICHNUNG] tatsächlich weiterzubeschäftigen.

[Hilfsweise:]
3. Das Arbeitsverhältnis der Parteien wird gegen Zahlung einer angemessenen Abfindung nach §§ 9, 10 KSchG i.V.m. § 17 Satz 2 TzBfG zum [DATUM] aufgelöst.

---

**BEGRÜNDUNG**

**A. Sachverhalt**

Der Kläger ist seit dem [DATUM] bei der Beklagten beschäftigt (Anlage K 1). Das monatliche Bruttogehalt beläuft sich auf [BETRAG] EUR. Der Arbeitsvertrag vom [DATUM] (Anlage K 2) enthält in § [X] eine Befristungsabrede bis zum [VEREINBARTES ENDE].

**B. Unwirksamkeit der Befristung**

**I. Schriftformmangel (§ 14 Abs. 4 TzBfG)**

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Rechtsfolge:** Gemäß § 16 Satz 1 TzBfG gilt der Arbeitsvertrag als auf unbestimmte Zeit geschlossen.

**II. Fehlender Sachgrund (hilfsweise) (§ 14 Abs. 1 TzBfG)**

[HILFSWEISE — SACHGRUNDPRÜFUNG:]

Selbst wenn die Schriftform gewahrt wäre, fehlt es an einem Sachgrund nach § 14 Abs. 1 TzBfG. [BEGRÜNDUNG NACH TATSACHEN].

**C. Frist (§ 17 TzBfG)**

Die Klage wird innerhalb der Dreiwochenfrist des § 17 Satz 1 TzBfG erhoben. Das vereinbarte Vertragsende ist der [DATUM]. Die Klage geht dem Gericht am [DATUM] zu.

**D. Beweisangebote**

- Anlage K 1: Arbeitsvertrag inkl. Befristungsabrede
- Anlage K 2: [E-Mail / Screenshot des Signier-Portals / sonstiger Nachweis der elektronischen Unterzeichnung]
- Zeugnis: [NAME] zum Beweis der Art der Vertragsunterzeichnung

---

[ORT], den [DATUM]

[ANWALTSUNTERSCHRIFT]

---

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

## 2. `entfristung-klageschrift-laie-baustein`

**Fokus:** Schritt-für-Schritt Klageschrift Entfristungsklage für Laien: Rubrum; Feststellungsantrag Unbefristetheit; Begründungsbausteine für Schriftformmangel und fehlenden Sachgrund; Beweisangebote; Pflicht-Disclaimer.

### Klageschrift Entfristungsklage — Laien-Baustein

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Klageschrift Entfristungsklage — Laien-Baustein` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor dem Ausfüllen der Vorlage

1. Wann endet der Vertrag laut Urkunde? (§ 17 TzBfG-Frist läuft ab diesem Datum)
2. Welcher Unwirksamkeitsgrund liegt vor? (Schriftformmangel / kein Sachgrund / Vorbeschäftigung)
3. Hast du eine Kopie des Arbeitsvertrags? (als Anlage K 1 beifügen)
4. Hast du einen Beleg für die Art der Unterzeichnung? (E-Mail, Screenshot Signier-Portal)
5. Wie hoch ist dein monatliches Bruttogehalt? (Streitwert = 3 × Monatsgehalt)
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- § 17 TzBfG — Klagefrist 3 Wochen ab vereinbartem Vertragsende (absolute Ausschlussfrist)
- §§ 14 Abs. 4, 16 TzBfG — Schriftformerfordernis und Rechtsfolge Unwirksamkeit
- § 14 Abs. 2 Satz 2 TzBfG — Vorbeschäftigungsverbot
- § 42 Abs. 2 GKG — Streitwert (3 Monatsverdienste)
- § 11 Abs. 1 ArbGG — kein Anwaltszwang in erster Instanz

## Wichtige Rechtsprechung (für Begründung verwendbar)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill erzeugt eine ausfüllbare Klageschrift-Vorlage für die Befristungskontrollklage (Entfristungsklage) — für Arbeitnehmer ohne Anwalt.

**Vor Verwendung:** Prüfe die Dreiwochenfrist nach § 17 TzBfG. Hat dein Vertrag laut Urkunde bereits geendet? Dann läuft die Frist möglicherweise bereits.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Arbeitnehmer ohne Anwalt reicht Entfristungsklage ein | Vorlage unten vollstaendig ausfuellen |
| Variante A — unsicher ob Befristung unwirksam | Erst anwaltliche Erstberatung einholen; Frist aber sichern |
| Variante B — Mandant will Geld statt Weiterbeschaeftigung | Klageschrift als Druckmittel; Abfindungsgespraech anstreben |
| Variante C — Frist laeuft in wenigen Tagen ab | Formular sofort einreichen; Begruendung kann nachgeliefert werden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Klageschrift-Vorlage

---

**HAFTUNGSAUSSCHLUSS UND WARNUNG**

Dieses Dokument ist ein Entwurf. Es begründet kein Mandatsverhältnis. Das System übernimmt keine rechtliche Verantwortung.

**Drei-Wochen-Frist § 17 TzBfG:** Klage muss innerhalb von drei Wochen **nach dem vereinbarten Vertragsende** beim Arbeitsgericht eingehen. Fristversäumnis führt nach § 7 KSchG analog zur Wirksamkeit der Befristung.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

---

**Arbeitsgericht [GERICHT EINTRAGEN]**

**Klage**

des/der [DEIN NAME],
[DEINE ADRESSE]

— Kläger/Klägerin —

gegen

[ARBEITGEBER — vollständige Firma],
[ADRESSE DES ARBEITGEBERS]

— Beklagte/r —

**Streitwert:** Vorläufig [3 × MONATSLOHN] EUR (§ 42 Abs. 2 GKG)

---

**KLAGEANTRÄGE**

Ich beantrage:

1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien nicht durch die Befristung im Arbeitsvertrag vom [VERTRAGSdatum] zum [VEREINBARTES ENDE] beendet worden ist, sondern als unbefristetes Arbeitsverhältnis über diesen Zeitpunkt hinaus fortbesteht.

2. Die Beklagte wird verurteilt, mich als [BERUFSBEZEICHNUNG] zu unveränderten Arbeitsbedingungen weiterzubeschäftigen.

---

**BEGRÜNDUNG**

**I. Das Arbeitsverhältnis**

Ich bin seit dem [ARBEITSBEGINN] bei der Beklagten beschäftigt als [BERUFSBEZEICHNUNG]. Mein monatliches Bruttogehalt beträgt [BETRAG] EUR.

**II. Der befristete Arbeitsvertrag**

Dem Arbeitsverhältnis liegt ein Arbeitsvertrag vom [VERTRAGSdatum] zugrunde, in dem eine Befristung bis zum [VEREINBARTES ENDE] vereinbart wurde (Anlage K 1).

**III. Unwirksamkeit der Befristung**

Die Befristung ist aus folgendem Grund unwirksam:

[HIER BEGRÜNDUNG EINTRAGEN — Bausteine:]

**Option A — Schriftformmangel (§ 14 Abs. 4 TzBfG):**
Die Befristungsabrede wurde nicht in der nach § 14 Abs. 4 TzBfG erforderlichen Schriftform (§ 126 BGB) vereinbart. Der Arbeitsvertrag wurde [BESCHREIBUNG: z.B. per E-Mail zugesandt / über die Plattform DocuSign unterzeichnet / nur eingescannt übermittelt]. Eine eigenhändige Unterschrift auf einer Originalurkunde liegt nicht vor. Gemäß § 16 Satz 1 TzBfG gilt der Arbeitsvertrag daher als auf unbestimmte Zeit geschlossen.

**Option B — Fehlender Sachgrund (§ 14 Abs. 1 TzBfG):**
Ein Sachgrund für die Befristung nach § 14 Abs. 1 TzBfG liegt nicht vor. [ERLÄUTERN WARUM — z.B.: Ein vorübergehender Beschäftigungsbedarf war nicht gegeben; die Beklagte beschäftigt auch nach dem vereinbarten Vertragsende Arbeitnehmer in gleicher Position].

**Option C — Verstoß gegen Vorbeschäftigungsverbot (§ 14 Abs. 2 Satz 2 TzBfG):**
Ich war bereits vor diesem befristeten Vertrag bei der Beklagten beschäftigt ([ZEITRAUM DER VORBESCHÄFTIGUNG]), sodass das Vorbeschäftigungsverbot des § 14 Abs. 2 Satz 2 TzBfG verletzt ist.

**IV. Beweisangebote**

- Anlage K 1: Arbeitsvertrag vom [DATUM]
- [WEITERE ANLAGEN — z.B. E-Mail über digitale Unterzeichnung, Screenshot des Online-Portals]

---

[ORT], den [DATUM]

____________________________
[UNTERSCHRIFT / NAME]

---

## Einreichungshinweise

- **Frist:** Klage muss innerhalb von drei Wochen nach dem vereinbarten Vertragsende eingehen.
- **Gericht:** Arbeitsgericht am Betriebsort oder Wohnort.
- **Einreichung:** Persönlich zu Protokoll der Geschäftsstelle (kein Schreiben nötig) oder schriftlich.
- **Empfangsbestätigung** vom Gericht verlangen.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## 3. `entfristung-laie-oder-anwalt-frage`

**Fokus:** Statusabfrage Entfristungsklage: Anwalt oder Laie; bei Laie Warnungen und Empfehlung anwaltlicher Beratung; kein Mandatsverhältnis; Hinweis auf § 17 TzBfG Drei-Wochen-Frist als kritischste Ausschlussfrist.

### Entfristung: Laie oder Anwalt?

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Entfristung: Laie oder Anwalt?` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zentrale Normen

- § 11 Abs. 1 ArbGG — kein Anwaltszwang in erster Instanz vor dem Arbeitsgericht
- § 17 TzBfG — Klagefrist 3 Wochen ab vereinbartem Vertragsende (absolute Ausschlussfrist)
- § 7 KSchG (analog) — Fiktionswirkung: Befristung gilt bei Fristversäumnis als wirksam
- § 5 KSchG (analog) — Nachträgliche Zulassung bei unverschuldeter Fristversäumnis
- § 14 Abs. 4 TzBfG — Schriftformerfordernis (häufig übersehener Unwirksamkeitsgrund)
- § 12a ArbGG — kein Kostenerstattungsanspruch für gegnerischen Anwalt in erster Instanz

## Warum anwaltliche Beratung besonders wichtig ist

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Wie im KüSchK-Bündel muss auch im Entfristungs-zunächst geklärt werden, wer den Skill nutzt. Die Warnstufe und die Art der Ausgaben richten sich danach.

## Pflicht-Eröffnungsfrage

> "Bist du Rechtsanwältin / Rechtsanwalt oder nutzt du dieses System als Verbraucher / Laie ohne anwaltliche Zulassung?"

## Pfad A: Anwalt / Anwältin

- Vollständige Werkzeugpalette ohne dauernden Warnkopf
- Zugang zu anwaltlichen Klageschrift-Bausteinen (`entfristung-klageschrift-anwalt-baustein`)
- Hinweis: Fristprüfung § 17 TzBfG trotzdem sofort

## Pfad B: Verbraucher / Laie

---

**WICHTIGE WARNUNG — BITTE GENAU LESEN**

Du bist dabei, eine Befristungskontrollklage einzuleiten, ohne Anwalt zu sein. Das ist in der ersten Instanz vor dem Arbeitsgericht zulässig (§ 11 Abs. 1 ArbGG — kein Anwaltszwang). Die Risiken sind jedoch erheblich:

1. **Drei-Wochen-Frist § 17 TzBfG**: Klagst du nicht innerhalb von drei Wochen **nach dem vereinbarten Vertragsende**, gilt die Befristung nach § 17 Satz 2 TzBfG i.V.m. § 7 KSchG als wirksam — auch wenn sie rechtswidrig war.

2. **Schriftform-Falle**: Der häufigste Fehler ist nicht das, was du glaubst — sondern dass du nicht erkennst, ob dein Vertrag wirklich wirksam befristet war. Zum Beispiel: Wurde der Vertrag per DocuSign oder E-Mail unterschrieben? Dann könnte die Befristungsabrede nach § 14 Abs. 4 TzBfG unwirksam sein, obwohl alles "normal" aussieht.

3. **Kein Mandatsverhältnis**: Dieses System ist kein Anwalt und haftet nicht.

4. **Mechanische Prüfung**: Nur das, was du eingibst, wird geprüft. Falsche Angaben führen zu falschen Ergebnissen.

**Dringende Empfehlung**: Suche sofort anwaltliche Beratung. Gewerkschaftsmitglieder können die Rechtsschutzstelle ihrer Gewerkschaft kontaktieren.

---

## Besonderheit: Entfristungsklage ist oft unterschätzt

Viele Arbeitnehmer wissen nicht, dass ihr befristeter Vertrag möglicherweise von Anfang an unwirksam befristet war — wegen eines Schriftformfehlers (§ 14 Abs. 4 TzBfG). Das System hilft, diese Möglichkeit zu erkennen. Aber nur ein Anwalt kann die Lage endgültig beurteilen.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.

## 4. `entfristung-rechtsfolge-16-tzbfg-unbefristet`

**Fokus:** Rechtsfolge unwirksamer Befristung nach § 16 Satz 1 TzBfG: Vertrag gilt als auf unbestimmte Zeit geschlossen; Möglichkeit der fruehesten ordentlichen Kündigung zum vereinbarten Ende nach § 16 Satz 2 TzBfG; Ansprüche Annahmeverzug; Weiterbeschaeftigungsantrag.

### Rechtsfolge der unwirksamen Befristung — § 16 TzBfG

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsfolge der unwirksamen Befristung — § 16 TzBfG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn — kläre vor der Rechtsfolgenprüfung

1. Liegt bereits ein rechtskräftiges Urteil über die Unwirksamkeit der Befristung vor?
2. Oder wird die Unwirksamkeit noch streitig festgestellt (läuft Klage)?
3. Wurde der Arbeitnehmer nach dem vereinbarten Ende weiterbeschäftigt?
4. Hat der Arbeitgeber zwischenzeitlich eine ordentliche Kündigung ausgesprochen?
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 16 Satz 1 TzBfG — Vertrag gilt als auf unbestimmte Zeit geschlossen (Hauptrechtsfolge)
- § 16 Satz 2 TzBfG — Früheste ordentliche Kündigung erst zum vereinbarten Ende möglich
- § 15 Abs. 3 TzBfG — Ordentliche Kündigung wenn vertraglich vereinbart
- § 15 Abs. 5 TzBfG — Weiterbeschäftigung über vereinbartes Ende hinaus ohne Widerspruch: neues unbefristetes AV
- § 615 BGB — Annahmeverzugslohn des Arbeitgebers bei Weigerung der Weiterbeschäftigung
- §§ 9, 10 KSchG i.V.m. § 17 Satz 2 TzBfG — Auflösungsantrag des Arbeitnehmers auf Abfindung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt: Was folgt aus § 16 TzBfG?

### Schritt 1: Feststellung der Rechtsfolge

§ 16 Satz 1 TzBfG ordnet an: Der Vertrag gilt **als auf unbestimmte Zeit geschlossen**. Konsequenzen:
- Das Arbeitsverhältnis besteht über das vereinbarte Ende hinaus fort
- Der Arbeitnehmer hat Anspruch auf Weiterbeschäftigung
- Das AV kann nur durch wirksame Kündigung oder Aufhebungsvertrag beendet werden
- Der Arbeitgeber schuldet das vereinbarte Entgelt auch nach dem "vereinbarten Ende"
- Nur die Befristungsklausel wird ersetzt — der restliche Vertrag bleibt wirksam

### Schritt 2: Kündigungsschutz nach § 16 Satz 2 TzBfG

Der Arbeitgeber kann frühestens **zum vereinbarten Ende** ordentlich kündigen:
```
Vereinbartes Ende: 31.03.2025
Früheste ordentliche Kündigung mit gesetzlicher Frist (§ 622 BGB):
→ Bei 2 Jahren Beschäftigung: 1 Monat → Kündigung bis spätestens 28.02.2025 zum 31.03.2025
→ Bei 5 Jahren: 2 Monate → Kündigung bis 31.01.2025 zum 31.03.2025
```

### Schritt 3: Annahmeverzugslohn (§ 615 BGB)

Falls Arbeitgeber die Weiterbeschäftigung verweigert:
- Anspruch auf Lohnfortzahlung als Annahmeverzugslohn (§ 615 Satz 1 BGB)
- Arbeitnehmer muss sich anderweitig erzielten Verdienst anrechnen lassen (§ 615 Satz 2 BGB)
- Arbeitnehmer muss angebotene zumutbare Arbeit nicht annehmen; Verweigerung schadet aber

### Schritt 4: Weiterbeschäftigungsantrag

Gleichzeitig mit der Entfristungsklage Weiterbeschäftigungsantrag stellen:
- Begründet nach GS BAG 27.02.1985 wenn Klageerfolg überwiegend wahrscheinlich
- Vollstreckbar nach Urteil
- Druckmittel in Vergleichsverhandlungen

## Entscheidungsbaum — Rechtsfolgen

```
Befristung unwirksam (§ 16 Satz 1 TzBfG):
├── Arbeitgeber beschäftigt freiwillig weiter → Normales unbefristetes AV
├── Arbeitgeber verweigert Weiterbeschäftigung →
│ ├── Annahmeverzugslohn (§ 615 BGB) verlangen
│ └── Weiterbeschäftigungsantrag vollstrecken
└── Arbeitgeber kündigt ordentlich →
 ├── Kündigung vor vereinbartem Ende → § 16 Satz 2 TzBfG: zu früh → unwirksam
 └── Kündigung zum/nach vereinbartem Ende → KSchG-Prüfung (§ 1 KSchG, § 102 BetrVG)
```

## Klageziel

Der Feststellungsantrag lautet:

> "Es wird festgestellt, dass das Arbeitsverhältnis der Parteien nicht durch Befristung zum [VEREINBARTES ENDE] beendet worden ist, sondern über diesen Zeitpunkt hinaus als unbefristetes Arbeitsverhältnis fortbesteht."

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
