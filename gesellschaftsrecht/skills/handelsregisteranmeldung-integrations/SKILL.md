---
name: handelsregisteranmeldung-integrations
description: "Handelsregisteranmeldung Integrations: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Handelsregisteranmeldung Integrations

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Handelsregisteranmeldung Integrations** im Plugin Gesellschaftsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `handelsregisteranmeldung` | Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen; Eintragungsgrundätze und Wirkung nach § 15 HGB. Lädt bei allen Registerpublizitätsfragen und Anmeldungspflichten. |
| `integrations-management` | Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste. Berücksichtigt § 613a BGB (Betriebsübergang), BetrVG-Mitbestimmung und gesellschaftsrechtliche Post-Closing-Pflichten nach UmwG/GmbHG/AktG. Lädt bei "Post-Merger-Integration", "Post-Closing", "Betriebsübergang", "Vertragsübertragung" oder "was ist noch offen". |
| `ki-werkzeug-uebergabe` | KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer "Luminance", "Kira", "KI-Prüfung", "automatische Extraktion" oder "Massenprüfung" erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die ein einheitliches Klausel-Extraktionsprofil erfordern. |
| `mandat-triage-gesellschaftsrecht` | Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert Mandantenrolle (Gesellschafter Geschäftsführer Aufsichtsrat Investor Kaeufer) und Rechtsform (GmbH AG UG GmbH&CoKG). Sofort-Fristen Insolvenzantragspflicht § 15a InsO drei Wochen Anfechtungsklage § 246 AktG ein Monat. Normen § 2 GmbHG Gründung § 48 GmbHG Gesellschafterversammlung § 241 AktG Beschlussmaengel. Eskalation Telefon-Sofort bei Insolvenznähe Gesellschafterversammlung morgen. Output Triage-Memo mit Fristen-Ampel und Routing zu Plugin-Skills. Abgrenzung zu gesellschaftsrecht-mandat-arbeitsbereich (Workspace-Verwaltung). |
| `rechtsabteilung-beirat-mit-vetorechten-in-der-gmbh` | Rechtsabteilungs-Fachmodul für Beirat mit Vetorechten in der GmbH: Beiratsrechte werden zwischen Beratung, Zustimmung, Weisung und faktischer Geschäftsführung abgegrenzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |

## Arbeitsweg

Im Plugin Gesellschaftsrecht gilt für **Handelsregisteranmeldung Integrations**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `handelsregisteranmeldung`

**Fokus:** Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen; Eintragungsgrundätze und Wirkung nach § 15 HGB. Lädt bei allen Registerpublizitätsfragen und Anmeldungspflichten.

# Handelsregisteranmeldung – HRB / HRA / GnR / PartGR

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Handelsregisteranmeldung – HRB / HRA / GnR / PartGR` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Handelsregisteranmeldung – HRB / HRA / GnR / PartGR
- **Spezialgegenstand:** Handelsregisteranmeldung – HRB / HRA / GnR / PartGR. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor der Anmeldungsvorbereitung klaeren:

1. **Anmeldungsgegenstand:** Was soll angemeldet werden? (Geschaeftsfuehrer-Wechsel, Prokura, Sitzverlegung, Kapitalerhoehung, Satzungsaenderung, Liquidation, Loeschung)
2. **Registerart:** HRB (GmbH/AG), HRA (OHG/KG), GnR (eG), PartGR (PartG)? Bei GmbH & Co. KG: sowohl HRB als auch HRA betroffen?
3. **Unterlagen vollstaendig?** Gesellschafterbeschluss (ggf. notariell beurkundet bei Satzungsaenderung § 53 GmbHG), Versicherung GF (§ 8 Abs. 3 GmbHG), Satzung aktuell?
4. **Notar beauftragt?** § 12 HGB: oeffentliche Beglaubigung erforderlich; Notar uebermittelt elektronisch (§ 12 Abs. 2 HGB). Ist der Notar bereits beauftragt?
5. **Mehrfache Aenderungen gleichzeitig?** Mehrere Aenderungen koennen in einer Anmeldung zusammengefasst werden; Voraussetzungen fuer jede Aenderung separat pruefen.
6. **§ 15 HGB-Risiko waehrend Wartezeit?** Wer vertritt die Gesellschaft bis zur Eintragung des neuen GF? Uebergangsregelungen (Vollmachten) treffen.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zweck

Dieser Skill unterstützt bei der Vorbereitung und Überprüfung von Anmeldungen
zum Handelsregister. Er erfasst alle Registerarten (HRB für Kapitalgesellschaften;
HRA für Personalhandelsgesellschaften; GnR für eingetragene Genossenschaften;
PartGR für Partnerschaftsgesellschaften) sowie die wesentlichen Pflichtanmeldungen
im laufenden Gesellschaftsleben. Zentrale Themen sind das Beurkundungs- und
Beglaubigungserfordernis (§ 12 HGB), Anmeldefristen, Eintragungsvoraussetzungen
und die Wirkung der Registereintragung (§ 15 HGB).

Mandatsbezug: Gesellschaft meldet Geschäftsführerwechsel an; Prokuraerteilung
oder -widerruf; Kapitalerhöhung oder Kapitalherabsetzung; Sitzverlegung;
Mandant fragt, ob ein nicht eingetragener Sachverhalt Dritten entgegengehalten
werden kann.

## Eingaben

1. **Registerart** – HRB (GmbH, AG, KGaA, SE), HRA (OHG, KG, GmbH & Co. KG),
 GnR (eG), PartGR (PartG).
2. **Anmeldungsgegenstand** – Art der Änderung: Geschäftsführer, Prokura, Sitz,
 Firma, Stammkapital, Satzungsänderung, Liquidation, Löschung.
3. **Unterlagen** – Gesellschafterbeschluss, Satzungsänderung, Versicherungen,
 Anstellungsvertrag (bei GF), Ausweiskopien.
4. **Zuständiges Registergericht** – Amtsgericht am Sitz der Gesellschaft
 (§ 8 HGB, §§ 13, 14 GmbHG); elektronische Einreichung über das
 Gemeinsame Registerportal der Länder (www.handelsregister.de).
5. **Vollmachten** – Notarielle Beglaubigung der Unterschrift des Anmeldenden
 erforderlich (§ 12 Abs. 1 Satz 1 HGB); bei GmbH: Unterschrift aller
 Geschäftsführer (§ 78 GmbHG).

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 8 HGB** – Inhalt und Führung des Handelsregisters; öffentliches Register.
- **§ 12 HGB** – Form der Anmeldungen: elektronisch in öffentlich beglaubigter
 Form (§ 12 Abs. 1 Satz 1 HGB); Notar übermittelt (§ 12 Abs. 2 HGB).
- **§ 13 HGB** – Örtliche Zuständigkeit: Gericht am Sitz der Niederlassung.
- **§ 15 HGB** – Wirkung der Eintragung und Bekanntmachung; negative Publizität
 (Abs. 1): nicht eingetragene und bekanntgemachte Tatsachen können Dritten
 nicht entgegengehalten werden; positive Publizität (Abs. 3): irrtümliche
 Eintragung kann gegenüber gutgläubigen Dritten wirken.
- **§ 39 GmbHG** – Anmeldung von Geschäftsführerwechseln; Muster-Versicherung;
 unverzügliche Anmeldung.
- **§ 53 HGB** – Erteilung, Änderung und Erlöschen der Prokura; Anmeldung zur
 Eintragung; keine konstitutive Wirkung, aber Publizitätswirkung § 15 HGB.
- **§§ 54–58 HGB** – Umfang der Prokura; Beschränkungen (Grundstücke § 49
 Abs. 2 HGB).
- **§ 78 GmbHG** – Zeichnung der Anmeldungen durch alle Geschäftsführer.
- **§§ 181 ff. AktG** – Satzungsänderung bei AG; Anmeldung durch Vorstand und
 Aufsichtsratsvorsitzenden.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Zum Eintragungserfordernis bei Prokura-Erteilung: Die Eintragung der Prokura
 hat keine konstitutive Wirkung; die Prokura entsteht durch Erteilung, nicht
 durch Eintragung. Aus § 15 Abs. 1 HGB folgt jedoch, dass der nicht eingetragene
 Widerruf der Prokura Dritten gegenüber unwirksam ist, wenn diese keine
 Kenntnis hatten.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Rn. 14 – Zur Zurückweisung einer Handelsregisteranmeldung wegen unzureichender
 Beglaubigung: § 12 HGB verlangt öffentliche Beglaubigung der Unterschrift;
 bloße notarielle Beglaubigung von Ablichtungen genügt nicht.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Sachverhalt klären** – Welcher Anmeldungsgegenstand liegt vor? Liegt ein
 neuer Geschäftsführer vor (§ 39 GmbHG), eine Prokura-Änderung (§ 53 HGB),
 eine Satzungsänderung (§ 54 GmbHG i. V. m. § 181 GmbHG) oder eine
 Kapitalmaßnahme?

2. **Unterlagen zusammenstellen** – Gesellschafterbeschluss (notariell beurkundet
 bei Satzungsänderung, § 53 Abs. 2 GmbHG); Anstellungsvertrag und ggf.
 Selbstauskunft des neuen Geschäftsführers nach § 8 Abs. 3 GmbHG; Satzung in
 aktueller Fassung.

3. **Anmeldung vorbereiten** – Entwurf der Anmeldeformulierung; Vorlage beim
 Notar zur Beglaubigung der Unterschrift nach § 12 HGB; Notar übermittelt
 elektronisch (§ 12 Abs. 2 HGB).

4. **Einreichungsfrist beachten:**
 - Geschäftsführerwechsel § 39 GmbHG: unverzüglich (keine Ausschlussfrist,
 aber Haftungsrisiko bei Verzögerung).
 - Prokura § 53 Abs. 1 HGB: unverzüglich nach Erteilung oder Erlöschen.
 - Satzungsänderung § 54 GmbHG: nach Beschluss unverzüglich, vor Wirksamkeit
 zur Eintragung anmelden (§ 54 Abs. 3 GmbHG).
 - Kapitalerhöhung AG: § 184 AktG; Anmeldung durch Vorstand und
 Aufsichtsratsvorsitzenden innerhalb angemessener Frist.

5. **Eintragung abwarten / § 15 HGB beachten** – Bis zur Eintragung und
 Bekanntmachung kann der geänderte Sachverhalt Dritten nicht entgegengehalten
 werden (§ 15 Abs. 1 HGB); in der Zwischenzeit Übergangsregelungen treffen
 (z. B. Vollmachten).

6. **Registerauszug prüfen** – Nach Eintragung aktuellen Handelsregisterauszug
 abrufen (www.handelsregister.de); fehlerhafte Eintragungen unverzüglich
 korrigieren (§ 395 FamFG, Berichtigungsantrag).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Handelsregisteranmeldung vorbereiten und einreichen | Anmeldung nach Checkliste; Template unten |
| Variante A — Eilbedarf Eintragung innerhalb Woche noetig | Vorlagenversion pruefen; Notarbeschleunigungs-Option |
| Variante B — Aenderungsanmeldung nicht Erstanmeldung | Aenderungsanmeldung-Subset des Templates verwenden |
| Variante C — Anmeldung wird vom Registergericht bemueckelt | Beschwerdeverfahren vorbereiten; Ergaenzung der Unterlagen zuerst |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Ausgabeformat

- **Anmeldungsschreiben** (Schriftsatz): Adressat Amtsgericht — Handelsregister; Bezeichnung der Gesellschaft mit HRB-Nummer; Gegenstand der Aenderung; Rechtsgrundlage; Anlage: notariell beglaubigte Unterschriften.
- **Checkliste Unterlagen** (Tabelle): Dokument | Erfordernis | Erledigt.
- **Memo negative Publizitaet** (Gutachtenstil): Risiken aus § 15 HGB bei verzoegerter Anmeldung.


## Output-Template

**Adressat:** Amtsgericht — Handelsregister — Tonfall: sachlich-juristisch, formbewusst

```
ANMELDUNG ZUM HANDELSREGISTER

An das
Amtsgericht [ORT] — Handelsregister
[ADRESSE]

[ORT], [TT.MM.JJJJ]

Betreff: [FIRMA] — [HRB/HRA-NUMMER] — Anmeldung [GEGENSTAND]

Anmeldende Partei: [KANZLEI / NOTAR] fuer [GESELLSCHAFT]

Hiermit melden wir im Namen der [FIRMA] mit Sitz in [ORT], eingetragen im
Handelsregister des Amtsgerichts [ORT] unter [HRB/HRA-NUMMER], folgende
Aenderung zur Eintragung an:

I. ANMELDUNGSGEGENSTAND
[GENAUE BESCHREIBUNG DER AENDERUNG]
Rechtsgrundlage: [§ NORM]

II. ANMELDENDE PERSONEN (§ 78 GmbHG / § [NORM])
[NAME], [FUNKTION], wohnhaft [ADRESSE]
[Fuer alle anmeldepflichtigen Personen wiederholen]

III. ANLAGEN
1. Gesellschafterbeschluss vom [DATUM] [notariell beurkundet / oeffentlich beglaubigt]
2. [Anlage 2]
3. [Anlage 3 (z.B. Versicherung § 8 Abs. 3 GmbHG)]
4. Aktueller Gesellschaftsvertrag / Satzung [falls geaendert]

IV. ERKLAERUNGEN
[Falls GF-Wechsel: Versicherung des neuen Geschaeftsfuehrers nach § 8 Abs. 3 GmbHG
bei. Die antretenden Personen versichern, dass keine Bestellungshindernisse
gemaiß § 6 Abs. 2 GmbHG vorliegen.]

Die Unterschriften der Anmeldenden wurden notariell beglaubigt (§ 12 Abs. 1
HGB) und werden durch Notar [NAME] elektronisch uebermittelt (§ 12 Abs. 2 HGB).

Mit freundlichen Gruessen
[NOTAR / KANZLEI]
[NAME]
[ANSCHRIFT]

--- UNTERLAGEN-CHECKLISTE ---
| Dokument | Erfordernis | Erledigt |
|---|---|---|
| Gesellschafterbeschluss | § 46 GmbHG / [NORM] | [JA / OFFEN] |
| Versicherung GF | § 8 Abs. 3 GmbHG | [JA / ENTFAELLT] |
| Beglaubigung Unterschrift | § 12 Abs. 1 HGB | [JA / OFFEN] |
| Aktueller GV / Satzung | [§ 53 GmbHG] | [JA / ENTFAELLT] |
| Bekanntmachung vorbereitet | § 10 GmbHG | [JA / ENTFAELLT] |
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.



## Rote Schwellen

- **Formfehler § 12 HGB (fehlende Beglaubigung)** — Registergericht weist Anmeldung zurueck; erneute Vorlage mit Zeitverlust; Notar vor Einreichung pruefen lassen.
- **Versicherungspflicht § 8 Abs. 3 GmbHG fehlt** — Anmeldung ohne GF-Versicherung wird abgelehnt; Versicherung vor Notartermin einholen.
- **§ 15 Abs. 1 HGB: Verzoegerung > 2 Wochen** — Ausscheidender GF haftet ggf. weiterhin gegenueber Dritten; neuer GF kann Vertretungsmacht nicht aus Register beweisen; Anmeldung unverzueglich einreichen.
- **Satzungsaenderung ohne notarielle Beurkundung** — § 53 Abs. 2 GmbHG: Formnichtigkeit; Notar muss beurkunden (nicht nur beglaubigen).

## Beispiel

*Sachverhalt:* Gesellschafter-GF A scheidet aus. B wird neuer alleiniger GF.
Gesellschafterbeschluss vom 01.03.2025 liegt notariell beurkundet vor.

*Ablaufskizze (Urteilsstil):*

Der Abgang von A und die Bestellung von B sind unverzüglich nach § 39 Abs. 1
GmbHG zum Handelsregister anzumelden. Die Anmeldung muss von dem verbleibenden
Geschäftsführer B persönlich unterzeichnet werden (§ 78 GmbHG); bei mehreren
neuen GF müssen alle unterschreiben. Der Notar beglaubigt die Unterschrift
(§ 12 Abs. 1 HGB) und übermittelt die Anmeldung elektronisch (§ 12 Abs. 2 HGB).
Bis zur Eintragung kann Dritten gegenüber weder das Ausscheiden des A noch die
Vertretungsmacht des B aus dem Register entgegengehalten werden (§ 15 Abs. 1 HGB;
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
zu vermeiden, sollte B A sofort eine Löschungsvollmacht für etwaige von A noch
einzugehende Verbindlichkeiten entziehen.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken und typische Fehler

- **Formfehler § 12 HGB:** Bloße Kopienbeglaubigung oder fehlende Originalunterschrift
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - Literaturhinweis gesperrt: Kommentar-, Handbuch- und Aufsatzfundstellen nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- **Negative Publizität (§ 15 HGB):** Nicht eingetragene Änderungen können
 Dritten gegenüber nicht geltend gemacht werden; erhebliches Haftungsrisiko
 bei verspäteter Prokura-Widerrufseintragung.
- **Versicherungspflicht § 8 Abs. 3 GmbHG:** Fehlt die Versicherung des neuen GF
 über das Nichtvorliegen von Bestellungshindernissen, wird die Anmeldung
 zurückgewiesen.
- **Falsche Registerart:** Eintragung im falschen Register (z. B. HRB statt HRA)
 bei GmbH & Co. KG führt zu Verfahrensverzögerungen.
- **Berufsrecht:** § 43a Abs. 2 BRAO, § 203 StGB; Vertraulichkeit der
 Gesellschafterdaten und -beschlüsse.

## Quellenpflicht

Alle Aussagen zu Registerpublizität und Anmeldungsform nach `references/
zitierweise.md`. § 15 HGB-Wirkungen sind differenziert darzustellen (negative
vs. positive Publizität; Gutgläubigkeitsschutz). Bei Streitfragen zur
konstitutiven vs. deklaratorischen Wirkung von Eintragungen sind h. M. und
abweichende Literaturauffassungen kenntlich zu machen.

## 2. `integrations-management`

**Fokus:** Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste. Berücksichtigt § 613a BGB (Betriebsübergang), BetrVG-Mitbestimmung und gesellschaftsrechtliche Post-Closing-Pflichten nach UmwG/GmbHG/AktG. Lädt bei "Post-Merger-Integration", "Post-Closing", "Betriebsübergang", "Vertragsübertragung" oder "was ist noch offen".

# Post-Merger-Integrations-Management

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Post-Merger-Integrations-Management` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Post-Merger-Integrations-Management
- **Spezialgegenstand:** Post-Merger-Integrations-Management. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor dem Start des Integrations-Trackings klären:

1. **Closing-Datum:** Wann war das Closing? (Tag-1/Tag-30/Tag-90-Workstreams hängen davon ab)
2. **SPA-Dokument verfügbar?** Vollständiges SPA oder nur Deal-Zusammenfassung?
3. **Schwerpunkt Rechtliches vs. Operatives:** Ist der Skill für rechtlichen Workstream oder operative Integration?
4. **Betriebsübergang?** Ist § 613a BGB ausgelöst? Wurden Arbeitnehmer bereits informiert?
5. **CoC-Klauseln:** Sind Tier-3-Verträge mit CoC-Klauseln identifiziert?
6. **Gesellschaftsbereinigung:** Soll eine Zielgesellschaft aufgelöst, verschmolzen oder fortgeführt werden?

## Zentrale Normen

§ 613a BGB (Betriebsübergang; Informationspflicht Abs. 5; Widerspruchsrecht Abs. 6 — 1 Monat) — §§ 111 ff. BetrVG (Interessenausgleich und Sozialplan) — § 17 KSchG (Massenentlassung) — § 40 GmbHG (Gesellschafterliste aktualisieren) — §§ 17 ff. UmwG (Verschmelzung) — §§ 65 ff. GmbHG (Liquidation) — §§ 414 f. BGB (Schuldübernahme; Vertragsübernahme) — § 25 HGB (Firmenhaftung bei Betriebsübernahme) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Tool-Übergabe)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ist die Programmmanagement-Ebene für die rechtliche Post-Closing-Integration — nicht operative Geschäftsintegration oder IT-Systeme. Der rechtliche Workstream: Drittpartei-Zustimmungen, Vertragsübertragungen, Gesellschaftsbereinigung, IP-Umschreibungen, SPA-Pflichten, Betriebsübergang nach § 613a BGB, betriebliche Mitbestimmung nach BetrVG.

## Eingaben

- Unternehmenskaufvertrag (SPA/Anteilskaufvertrag) oder Auszüge
- deal-context.md (Mandatscode, Zielgesellschaft, Closing-Datum, Transaktionsleiter)
- Bestehende Abschluss-Checkliste, Vertragsbestand der Zielgesellschaft
- Statusmitteilungen von externem Berater, HR, Corporate Development

## Rechtlicher Rahmen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

Aufruf über Flag: `--init` (Modus 1) | `--verträge` (Modus 2) | `--bericht` (Modus 3) | `--update` (Modus 4) | `--export` (Modus 5).

### Modus 1: Initialisierung (`--init`)

deal-context.md lesen; ggf. anlegen. Abschluss-Checkliste importieren (Post-Closing-Punkte → Tag-1/30-Arbeitsplan).

Transaktionsunterlagen anfordern (Vollständiger SPA > Deal-Zusammenfassung > nichts). Phasenbasierten Arbeitsplan generieren:

**Tag 1 — rechtlich federführend:** Firmenname Handelsregister; Bankkonten-Bevollmächtigte; Gesellschafterliste § 40 GmbHG; D&O-Nachhaftungsdeckung; IP-Abtretungen.

**Tag 1 — rechtlich begleitend:** Mitarbeiterinformation § 613a Abs. 5 BGB (Frist beachten); Betriebsrat informieren; Kundenanschreiben prüfen.

**Tag 30:** Erster Zustimmungsanlauf (alle Gegenparteien); IP-Umschreibung DPMA; CoC-Vertragsanalyse (Tier 3).

**Tag 90:** Pflicht-Zustimmungen-Frist (SPA); Gesellschaftsbereinigungsentscheidung; HR-Harmonisierung (BetrVG).

**Tag 180:** Verschmelzungsanmeldung §§ 17 ff. UmwG oder Liquidationsanmeldung §§ 65 ff. GmbHG; Garantiefrist-Tracking.

### Modus 2: Vertragsübertragung (`--verträge`)

Vertragsbestand aus Datenraum, hochgeladener Liste oder SPA-Disclosure-Schedule importieren. Übertragungsmechanismus für jeden Vertrag klassifizieren:

| Mechanismus | Tier |
|---|---|
| Zustimmungserforderlich (ausdrückliche Klausel) | 1 (SPA-Pflicht) oder 2 |
| Change-of-Control-Klausel (ausgelöst durch Closing) | 3 — sofort handeln ⚠️ |
| Automatisch übertragbar (keine Beschränkung) | 4 |
| Keine Regelung (§§ 398 ff. BGB prüfen; § 354a HGB bei Kaufleuten) | 2 |

Tier-3-Verträge prominent ausweisen: CoC-Recht kann bereits mit Closing-Datum ausgelöst sein.

### Modus 3: Statusbericht (`--bericht`)

```
INTEGRATIONSSTATUS — [Mandatscode] / [Zielgesellschaft]
[Datum] — Tag [N] nach Closing

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO. Weitergabe nur nach Freigabe.

PFLICHT-ZUSTIMMUNGEN [Frist: DATUM — N Tage]
 Erhalten: [N] von [gesamt] ████░░ [%]
 Verweigert: [N] ⚠️

VERTRAGSÜBERTRAGUNG
 Tier 1–3: Status je Kategorie
 CoC offen: [N] ⚠️

ARBEITSPLAN — ÜBERFÄLLIG / DIESE WOCHE / ABGESCHLOSSEN

BLOCKIERER & ENTSCHEIDUNGSBEDARF
```

### Modus 4: Aktualisierung (`--update`)

Freitext oder hochgeladenes Statusdokument einlesen. Tracker-Einträge aktualisieren und Zusammenfassung der Änderungen zeigen.

### Modus 5: Export (`--export`)

Flaches CSV (Spalten: id, phase, beschreibung, prioritaet, frist, status, blockierer) oder Markdown-Tabelle. Formel-Injektionsschutz: Zellen aus Fremdquellen mit vorangestelltem Apostroph.

## Ausgabeformat

YAML-Tracker-Datei + strukturierter Statusbericht mit Arbeitsergebnis-Kopfzeile. Export als CSV.

## Output-Template

**Adressat:** Internes Transaktionsteam / Mandant — Tonfall: sachlich-strukturiert, handlungsorientiert

```
PMI-STATUSBERICHT
Mandat: [MANDATSCODE]
Zielgesellschaft: [ZIELGESELLSCHAFT GmbH]
Closing-Datum: [TT.MM.JJJJ]
Bericht-Datum: [TT.MM.JJJJ] — Tag [N] nach Closing
Erstellt von: [NAME], [KANZLEI]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Weitergabe nur nach ausdrücklicher Freigabe durch Transaktionsleiter.

--- PFLICHT-ZUSTIMMUNGEN (SPA-Anhang [X]) ---
Frist gemäß SPA: [TT.MM.JJJJ] ([N] Tage verbleibend)
Erhalten: [N] von [GESAMT] ████░░░░ [%]
Offen: [N] (Gegenpartei: [NAME]; kontaktiert: [DATUM])
Verweigert: [N] ⚠️ → SPA-Klausel [§/Ziff.] gefährdet

--- VERTRAGSÜBERTRAGUNGEN ---
Tier 1 (SPA-Pflicht): [N] offen / [N] abgeschlossen
Tier 2 (kein Sperrvermerk): [N] offen / [N] abgeschlossen
Tier 3 (CoC-Klausel ausgelöst): [N] ⚠️ — sofortiger Handlungsbedarf
Tier 4 (automatisch übertragen): [N] erledigt

--- GESELLSCHAFTSRECHTLICHE POST-CLOSING-PFLICHTEN ---
☐ Gesellschafterliste § 40 GmbHG beim Notar eingereicht [DATUM / OFFEN]
☐ Handelsregisteranmeldung [HRA/HRB-Nr.] aktualisiert [DATUM / OFFEN]
☐ IP-Umschreibung DPMA [DATUM / OFFEN]
☐ D&O-Nachhaftung bestätigt [DATUM / OFFEN]
☐ Bankkonten-Bevollmächtigte geändert [DATUM / OFFEN]

--- § 613a BGB / BETRIEBSÜBERGANG ---
☐ Arbeitnehmerinformation § 613a Abs. 5 BGB versandt [DATUM / OFFEN]
☐ Widerspruchsfrist (1 Monat ab Information) läuft bis: [TT.MM.JJJJ]
☐ Betriebsrat informiert (§§ 111 ff. BetrVG) [DATUM / OFFEN]
☐ Massenentlassung § 17 KSchG: [RELEVANT / NICHT RELEVANT]

--- NÄCHSTE SCHRITTE (7-Tage-Fenster) ---
1. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
2. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
3. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]

--- BLOCKIERER & ENTSCHEIDUNGSBEDARF ---
⚠️ [BESCHREIBUNG BLOCKIERER] — benötigt Entscheidung von: [PERSON/GREMIUM]

--- RISIKOAMPEL ---
Gesamt: [GRÜN / GELB / ROT]
Begründung: [KURZBESCHREIBUNG]
```

## Rote Schwellen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Tier-3-CoC-Klausel ausgelöst, aber kein Kontakt** → Recht kann mit Closing-Datum zu laufen begonnen haben; Gegenseite sofort anschreiben.
- **SPA-Pflicht-Zustimmungen: Frist < 14 Tage, < 100 %** → Transaktionsleiter eskalieren; MAC-Klausel prüfen.
- **Gesellschafterliste § 40 GmbHG > 3 Wochen nach Closing nicht beim Notar** → Haftungsrisiko; sofort beauftragen.

## Beispiel

GmbH-Anteilskauf, Closing 01.03.2025, 15 Pflicht-Zustimmungen aus SPA-Anhang, 3 CoC-Verträge. Tag-30-Bericht: 8 von 15 Zustimmungen erhalten, 2 verweigert (SPA-Pflicht gefährdet), 3 CoC-Verträge zur sofortigen Kontaktaufnahme.

## Risiken und typische Fehler

- **§ 613a Abs. 5 BGB-Informationspflicht vergessen.** Widerspruchsfrist 1 Monat läuft ab ordnungsgemäßer Information.
- **CoC-Klauseln zu spät identifizieren.** Tier-3-Verträge prominent anzeigen — Recht kann ab Closing laufen.
- **Garantiefristen nicht differenzieren.** Allgemeine, fundamentale und Steuergarantien haben unterschiedliche Überlebensfristen — aus SPA einzeln extrahieren.
- **Earn-out nicht abgrenzen.** Nur Referenzdaten führen, Eigentümer = Finance.

## Quellenpflicht

- `§ 613a Abs. 5 BGB` (Information), `§ 613a Abs. 6 BGB` (Widerspruchsfrist)
- `§§ 17 ff. UmwG` (Verschmelzung), `§§ 65 ff. GmbHG` (Liquidation), `§ 40 GmbHG` (Gesellschafterliste)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 3. `ki-werkzeug-uebergabe`

**Fokus:** KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer "Luminance", "Kira", "KI-Prüfung", "automatische Extraktion" oder "Massenprüfung" erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die ein einheitliches Klausel-Extraktionsprofil erfordern.

# KI-Tool-Übergabe (Luminance / Kira)

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KI-Tool-Übergabe (Luminance / Kira)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: KI-Tool-Übergabe (Luminance / Kira)
- **Spezialgegenstand:** KI-Tool-Übergabe (Luminance / Kira). Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Vor der Tool-Ubergabe klaeren:

1. **Volumen:** Wie viele Dokumente sind im Datenraum? (< 50: manuelle Prüfung effizienter; 50-200: bedingt sinnvoll; > 200: KI-Tool empfohlen)
2. **Tool vorhanden?** Ist Luminance, Kira oder ein vergleichbares Tool bereits im Praxisprofil konfiguriert? Welches Vertrauensniveau ist eingestellt?
3. **Kategorien:** Sind die Verträge bereits grob kategorisiert (Lieferanten, Kunden, IP, Miet-, Arbeitsverträge)?
4. **AVV geklaert?** Liegt ein Auftragsverarbeitungsvertrag (Art. 28 DSGVO) mit dem Tool-Anbieter vor? Hat der Mandant der Weitergabe zugestimmt?
5. **Rechtsordnung:** Werden auch Verträge nach auslaendischem Recht gepüft? (gesondertes Profil erforderlich)
6. **QA-Ressourcen:** Wer fuehrt die Stichproben-QA durch? Wie viel Zeit steht zur Verfuegung?

## Zentrale Normen

§ 398 BGB (Forderungsabtretung) — § 399 BGB (Abtretungsverbot) — § 354a HGB (Abtretungsverbot unter Kaufleuten; ggf. unwirksam) — §§ 305 ff. BGB (AGB-Kontrolle) — § 307 BGB (unangemessene Benachteiligung) — § 613a BGB (Betriebsubergang; Vertragsuebergang) — §§ 69b, 43 UrhG (Arbeitnehmererfindung) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Datenweitergabe) — § 130 OWiG (Aufsichtspflichtverletzung bei Compliance-Verstoss)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

In M&A-Mandaten mit Datenräumen von 100+ Verträgen übersteigt manuelle Einzelprüfung das verfügbare Zeitbudget. Dieser Skill strukturiert die Übergabe an ein KI-Prüftool (Luminance, Kira oder vergleichbar), legt das Extraktionsprofil fest, QA-checkt die Ausgabe und steuert die Rückübernahme in den DD-Issue-Extraktion-Ablauf.

## Eingaben

- Praxisprofil: `## M&A → KI-gestützte Prüfung` (Tool-Name, Verwendungszweck, Vertrauensniveau, Übergabe-Ablauf)
- VDR-Inventar oder Ordnerliste mit Kategorien
- Klausel-Extraktionsprofil (Standardprofil unten oder Hausformat aus Praxisprofil)
- Anzahl Dokumente in der Übergabecharge
- Deal-Code und Datenraumstruktur

## Ablauf

### Schritt 1: Kategorie-Triage

Nicht jede Kategorie ist für KI-Massenprüfung geeignet. Einschätzen:

| Kategorie | Eignet sich für KI-Tool | Begründung |
|---|---|---|
| Wesentliche Verträge (>50 gleichartige) | ✓ | Standardklauseln, hohes Volumen |
| Rahmenverträge / MSA | ✓ | Strukturierte Klauseln |
| IP-Lizenzverträge | Bedingt | Komplexe Terminologie; Stichproben-QA |
| Arbeitsverträge | Bedingt | Länderspezifische Normen; § 307 BGB |
| Gesellschaftsverträge / Satzungen | ✗ | Besprechungs- und Kontextbedarf |
| Side Letters / Anpassungsvereinbarungen | ✗ | Zu nuanciert für Bulk-Extraktion |

### Schritt 2: Extraktionsprofil erstellen

Für jede Vertragsart ein Extraktionsprofil mit den zu extraktierenden Klauseln erstellen:

**Standardprofil M&A – deutsches Recht:**

```yaml
extraktionsprofil:
 change_of_control:
 frage: "Gibt es eine Change-of-Control-Klausel? Ist Zustimmung erforderlich?"
 rechtsgrundlage: "Kein gesetzliches Zustimmungserfordernis; rein vertragliche Regelung"
 relevanz: "Zustimmungserfordernis vor Vollzug"
 kuendigungsrecht_abtretung:
 frage: "Gibt es ein Kündigungsrecht oder Abtretungsverbot bei Eigentümerwechsel?"
 rechtsgrundlage: "§ 398 BGB (Abtretung), § 613a BGB (Betriebsübergang)"
 relevanz: "Hemmt Vollzug oder Vertragsübertragung"
 wettbewerbsverbot:
 frage: "Enthält der Vertrag ein Wettbewerbs- oder Exklusivitätsverbot?"
 rechtsgrundlage: "§ 138 BGB (Sittenwidrigkeit), Bindung nach UWG"
 relevanz: "Schränkt Käufer-Geschäft ein"
 haftungsbegrenzung:
 frage: "Gibt es eine Haftungsobergrenze? In welcher Höhe? AGB oder Individualvereinbarung?"
 rechtsgrundlage: "§§ 305 ff. BGB (AGB-Kontrolle); § 309 Nr. 7 BGB"
 relevanz: "Risikoquantifizierung; AGB-Unwirksamkeit prüfen"
 ip_eigentum:
 frage: "Wer ist Eigentümer der erzeugten IP? Enthält der Vertrag eine Abtretung?"
 rechtsgrundlage: "§§ 69b, 43 UrhG (Arbeitnehmererfindung); § 7 ArbNErfG"
 relevanz: "IP-Kette zum Zielunternehmen"
 kuendigungsfristen:
 frage: "Wie sind ordentliche und außerordentliche Kündigung geregelt?"
 rechtsgrundlage: "§§ 314, 615 BGB; vertraglich oder gesetzlich"
 relevanz: "Risiko vorzeitiger Beendigung nach Vollzug"
 agb_kontrolle:
 frage: "Wurden die AGB einbezogen? Welcher Partei? Gültige Einbeziehung gem. §§ 305 ff. BGB?"
 rechtsgrundlage: "§§ 305, 307, 309 BGB"
 relevanz: "Unwirksame Klauseln trotz Vertragstext"
 compliance:
 frage: "Gibt es Compliance-Zusicherungen (Korruptionsverbote, Sanktionen, Exportkontrolle)?"
 rechtsgrundlage: "§ 130 OWiG; AWG/AWV; GwG"
 relevanz: "Compliance-Risiko des Zielunternehmens"
```

### Schritt 3: Tool-Übergabe-Paket erstellen

Das Übergabe-Paket enthält:

1. **Extraktionsprofil** (YAML oben, ggf. im Tool-nativen Format)
2. **Dokument-Inventar** (Liste aller Dokumente mit VDR-Pfad, Kategorie, Dateiname)
3. **Priorisierung** (Top-N nach Wert oder Relevanz zuerst)
4. **QA-Stichprobenplan** (welche %-QA für diesen Auftrag)

```markdown
## Übergabe-Paket – [Deal-Code] – [Datum]

**Tool:** [Luminance / Kira / anderes]
**Volumen:** [N] Dokumente
**Kategorien:** [Liste]
**Extraktionsprofil:** [Anlage-Link]
**Priorisierung:** [nach Wert >X EUR / Top-50 / vollständig]
**QA-Plan:** Stichprobe 10 % oder [N] Dokumente, gleichmäßig über Kategorien verteilt
**Erwartete Lieferzeit:** [N] Stunden/Tage
**Rückgabeformat:** [XLSX / CSV / Tool-API]
**Übergabe an:** [Tool-Administrator / externes Dienstleister]
```

### Schritt 4: QA-Schicht

Nach Erhalt der Tool-Ausgabe:

1. **Stichproben-QA**: [N] Dokumente manuell gegenlesen
 - Vollständigkeit: Alle extraktierten Klauseln vorhanden?
 - Richtigkeit: Klausel korrekt klassifiziert?
 - Falsch-Negative: Übersehene wesentliche Klauseln?
 - Falsch-Positive: Irrelevante Klauseln einbezogen?

2. **Fehler-Typen dokumentieren**:

```markdown
QA-Bericht – [Deal-Code]
- Geprüfte Dokumente: [N] von [M] ([%])
- Fehlerrate: [N] Fehler in [N] geprüften Dokumenten
- Häufige Fehler: [Beschreibung]
- Anpassung Extraktionsprofil: [ja / nein; wenn ja: was]
- Gesamtbewertung Vertrauensniveau: [hoch / mittel / niedrig]
```

3. **Vertrauensniveau aus Praxisprofil anwenden:**
 - `Ergebnis übernehmen`: Direkt in DD-Issues übernehmen, QA-Ergebnis vermerken
 - `Stichproben`: Mittleres Vertrauensniveau; alle 🔴-Issues manuell nachprüfen
 - `Vollständige Neuprüfung`: Nur Screening verwenden; alle Issues selbst extrahieren

### Schritt 5: Rückübergabe an DD-Issue-Extraktion

Tool-Ergebnisse im Standardformat für den `dd-findings-extraktion`-Skill übergeben:

```yaml
ki_tool_ergebnisse:
 tool: "Luminance"
 version: "2024.3"
 datum: "[DATUM]"
 vertrauensniveau: "mittel"
 qa_stichprobe_prozent: 10
 dokumente_gesamt: 312
 findings:
 - dokument: "VDR/02-Verträge/Acme-MSA-2021.pdf"
 kategorie: "Wesentliche Verträge"
 klausel: "change_of_control"
 extrakt: "§ 12 Abs. 3: Bei Kontrollwechsel hat [Vertragspartner] das Recht, fristlos zu kündigen."
 schweregrad_vorschlag: "🔴"
 ki_konfidenz: 0.92
 qa_geprueft: true
 qa_korrekt: true
```

## Quellen und Zitierweise

Normen-Basis für Extraktionsprofil: §§ 305 ff. BGB (AGB-Kontrolle), § 398 BGB (Abtretung), § 613a BGB (Betriebsübergang), §§ 69b, 43 UrhG, § 7 ArbNErfG, § 130 OWiG.

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

1. **Übergabe-Paket** (Markdown-Tabelle + YAML-Extraktionsprofil)
2. **QA-Bericht** (Markdown, nach Stichproben-QA)
3. **Rückgabe-Datensatz** (YAML/XLSX, für dd-findings-extraktion)

## Output-Template

**Adressat:** Tool-Administrator / DD-Team-intern — Tonfall: strukturiert, technisch-praezise

```
KI-TOOL-ÜBERGABE-PAKET
Mandat: [MANDATSCODE]
Deal-Code: [DEAL-CODE]
Datum: [TT.MM.JJJJ]
Tool: [LUMINANCE / KIRA / ANDERES]
Erstellt von: [NAME], [KANZLEI]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Weitergabe an Tool-Anbieter nur nach AVV gem. Art. 28 DSGVO und Mandantenzustimmung.

--- CHARGE-BESCHREIBUNG ---
Dokumente gesamt: [N]
Kategorien:
 - [KATEGORIE 1]: [N] Dokumente — Eignung: [HOCH / BEDINGT / NIEDRIG]
 - [KATEGORIE 2]: [N] Dokumente — Eignung: [HOCH / BEDINGT / NIEDRIG]
Ausgeschlossen (manuell zu prüfen): [N] Dokumente (Gesellschaftsvertraege, Side Letters)

--- EXTRAKTIONSPROFIL ---
Version: [v1.0]
Rechtsordnung: [Deutsches Recht / Englisches Recht / Gemischt]
Klauseln im Profil:
 1. change_of_control — [§ Vertrag; CoC-Recht]
 2. abtretungsverbot — [§ 399 BGB; § 354a HGB]
 3. haftungsbegrenzung — [§§ 305 ff. BGB]
 4. wettbewerbsverbot — [§ 138 BGB]
 5. kuendigungsfristen — [§§ 314, 615 BGB]
 [weitere nach Profil]

--- PRIORISIERUNG ---
Top-[N] nach [Vertragswert / Relevanz]: [LISTE]
Vollstaendige Prufung: [JA / NEIN]

--- QA-PLAN ---
Stichprobe: [N] % = [N] Dokumente
Vertrauensniveau Praxisprofil: [ERGEBNIS UEBERNEHMEN / 10-PROZENT-STICHPROBE / VOLLPRÜFUNG]
QA-Verantwortlich: [NAME]
QA-Frist: [TT.MM.JJJJ]

--- ERWARTETER ABLAUF ---
Uebergabe an Tool: [TT.MM.JJJJ]
Erwartete Lieferung: [TT.MM.JJJJ]
Rueckgabeformat: [XLSX / CSV / YAML]

--- QA-BERICHT (nach Lieferung auszufuellen) ---
Geprüfte Dokumente: [N] von [M] ([%])
Fehlerrate: [N] Fehler
Haeufige Fehlertypen: [BESCHREIBUNG]
Gesamtbewertung Vertrauensniveau: [HOCH / MITTEL / NIEDRIG]
Empfehlung: [ERGEBNIS DIREKT UEBERNEHMEN / NACHPRUEFUNG ERFORDERLICH FUER ROT-FINDINGS]
```

## Rote Schwellen

- **Kein AVV (Art. 28 DSGVO) vor Datenweitergabe** — Bussgeldhaftung; Weitergabe sofort stoppen bis AVV vorliegt.
- **KI-Vertrauensniveau "vollstaendige Neuprüfung" und kein QA-Budget** — KI-Tool liefert nur Screening; alle Findings sind manuell zu verifizieren bevor Garantien abgegeben werden.
- **Gesellschaftsvertraege / Side Letters in Batch** — ungeeignet fuer Bulk-Extraktion; sofort aus Charge herausnehmen und manuell prüfen.
- **Abtretungsverbote nicht klassifiziert** — Haftungsrisiko bei Garantien; § 354a HGB-Prüfung fuer Kaufleute-Vertraege immer separat durchfuehren.

## Beispiel

**Eingabe:** Datenraum enthält 280 Lieferantenverträge; Luminance konfiguriert.

**Ausgabe:** Übergabe-Paket mit Extraktionsprofil (8 Klauseln), Priorisierung Top-50 nach Vertragswert >100 TEUR, QA-Stichprobenplan 10 %. Nach QA: 15 🔴-Findings (davon 3 Change-of-Control mit Zustimmungserfordernis) → direkt an Vollzugscheckliste übergeben.

## Risiken / typische Fehler

- **Falsch-Negative bei AGB-Kontrolle:** KI-Tools übersehen oft die AGB-Einbeziehungs-Frage (§ 305 BGB). Immer manuell nachprüfen, ob AGB wirksam einbezogen wurden.
- **Change-of-Control ohne Zustimmungs-Prüfung:** Klausel extrahiert, aber nicht geprüft, ob bloßes Informationsrecht oder echtes Zustimmungserfordernis. Manuelle Klassifizierung erforderlich.
- **Jurisdiktion nicht erkannt:** Bei internationalen Verträgen (z. B. englisches Recht) falsche Klauselklassifizierung. Rechtsordnung im Profil explizit angeben.
- **Vertrauen ohne QA:** Kein Tool ist 100 % korrekt. QA-Stichproben sind nicht optional.
- **Mandantengeheimnis:** Dokumente an Drittanbieter weitergeben erfordert Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO und Zustimmung des Mandanten.

## 4. `mandat-triage-gesellschaftsrecht`

**Fokus:** Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert Mandantenrolle (Gesellschafter Geschäftsführer Aufsichtsrat Investor Kaeufer) und Rechtsform (GmbH AG UG GmbH&CoKG). Sofort-Fristen Insolvenzantragspflicht § 15a InsO drei Wochen Anfechtungsklage § 246 AktG ein Monat. Normen § 2 GmbHG Gründung § 48 GmbHG Gesellschafterversammlung § 241 AktG Beschlussmaengel. Eskalation Telefon-Sofort bei Insolvenznähe Gesellschafterversammlung morgen. Output Triage-Memo mit Fristen-Ampel und Routing zu Plugin-Skills. Abgrenzung zu gesellschaftsrecht-mandat-arbeitsbereich (Workspace-Verwaltung).

# Mandat-Triage Gesellschaftsrecht

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Gesellschaftsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Mandat-Triage Gesellschaftsrecht
- **Spezialgegenstand:** Mandat-Triage Gesellschaftsrecht. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Triage zu Beginn

Diese acht Fragen sind in der angegebenen Reihenfolge zu klaeren — Fragen 1 bis 4 bestimmen das Routing, Fragen 5 bis 8 die Mandatsstrategie:

1. **Eilbeduerftigkeit zuerst:** Laeuft eine der folgenden Fristen? — Insolvenzantragspflicht § 15a InsO (3 Wochen); Beschluss-Anfechtungsfrist § 246 AktG (1 Monat); Closing-Termin heute; HV morgen. Falls ja: direkt zu Eskalation.
2. **Mandantenrolle:** Wer ist der Mandant? (Gesellschafter / Geschaeftsfuehrer / Aufsichtsrat / Investor / Kaeufer / Verkaeufer / Zielgesellschaft / Glaeubiger)
3. **Rechtsform der betroffenen Gesellschaft:** GmbH / UG / AG / SE / GmbH & Co. KG / OHG / GbR / Stiftung / Verein
4. **Vorgang:** Was soll rechtlich geschehen oder was ist passiert?
5. **Stand des Verfahrens:** Beratung im Vorfeld / Vertrag in Verhandlung / Streit / Klage
6. **Wirtschaftliche Verhaeltnisse:** Gesellschaftsgroesse (Umsatz, Mitarbeiter, Bilanz)
7. **Fristen ausserhalb der akuten Eilbeduerftigkeit:** Verjaehrung Geschaeftsfuehrer-Haftung 5 Jahre (§ 43 Abs. 4 GmbHG)
8. **Interessenkonflikt-Check:** Vertritt die Kanzlei bereits eine andere Partei derselben Transaktion?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

§ 15a InsO (Insolvenzantragspflicht; 3 Wochen ab Ueberschuldung/Zahlungsunfaehigkeit) — § 43 GmbHG (Geschaeftsfuehrer-Haftung; Verjaehrung 5 Jahre) — § 93 AktG (Vorstandshaftung) — § 246 AktG (Anfechtungsklage; 1 Monat ab Beschlussfassung) — § 14 UmwG (Klagefrist Umwandlung; 1 Monat) — §§ 35 ff. GWB (Fusionskontrolle; Vollzugsverbot bis Freigabe) — § 43a Abs. 4 BRAO (Verbot widersteitender Interessen) — §§ 1 ff. GwG (Identifizierungspflicht vor Mandatsannahme)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Gesellschaftsrechts-Mandate sind heterogen — vom Beschluss-Streit bis zum M&A-Closing. Triage stellt die richtige Rechtsform und den richtigen Vorgang sicher.

## Ablauf — acht Fragen


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Frage 1 — Mandantenrolle?

- Gesellschafter / Aktionär
- Geschäftsführer / Vorstand
- Aufsichtsrat / Beirat
- Investor (Inbound Outbound)
- Käufer (M&A)
- Verkäufer (M&A)
- Zielgesellschaft
- Gläubiger
- Insolvenzverwalter

### Frage 2 — Rechtsform?

- GmbH
- UG (haftungsbeschränkt)
- AG
- SE (Societas Europaea)
- KGaA
- GmbH & Co. KG
- OHG / KG
- GbR
- eG (Genossenschaft)
- Stiftung (privat öffentlich)
- Verein eingetragener
- Personenhandels-Gesellschaft
- Auslandsgesellschaft

### Frage 3 — Vorgang?

- Gründung
- Satzungs-Änderung
- Kapitalerhöhung (effektiv genehmigt bedingt)
- Kapitalherabsetzung
- Gesellschafter-Beschluss
- Geschäftsführer-Bestellung / Abberufung
- Anstellungsvertrag Geschäftsführer
- Gesellschafter-Streit
- Geschäftsführer-Haftung
- Beschluss-Anfechtung
- Umwandlung (Verschmelzung Spaltung Formwechsel)
- M&A (Asset / Share Deal)
- Joint Venture / Kooperation
- Liquidation Auflösung
- Insolvenz (an `insolvenzrecht`-Plugin)
- Compliance Audit
- Dual-Use Sanktionsprüfung
- ESG-Bericht / CSRD
- Bilanzrecht HGB / IFRS

### Frage 4 — Akute Eilbedürftigkeit?

- **Insolvenzantragspflicht** § 15a InsO drei Wochen
- **Geschäftsführer-Abberufung** Versammlung morgen
- **Closing-Termin** binnen Tagen
- **Beschluss-Anfechtung** Frist
- **Kartellbehörden-Anmeldung**
- **Hauptversammlung-Termin** AG
- **Vertragsstrafe Closing**
- **Schadensersatzklage** verjährungsbedroht

### Frage 5 — Stand?

- Beratungsbedarf vor Maßnahme
- Vertrag in Verhandlung
- LOI / Term Sheet erstellt
- Due Diligence läuft
- Signing erfolgt — Closing offen
- Closing — laufende Vertrags-Durchführung
- Streit / Klage
- Schiedsverfahren

### Frage 6 — Wirtschaftliche Verhältnisse?

- Gesellschaftsgröße (Umsatz Mitarbeiter Bilanz)
- Konzern-Struktur
- Beteiligungsverhältnisse
- Streit-Volumen
- Versicherungs-Deckung D&O

### Frage 7 — Frist?

- **§ 15a InsO** drei Wochen Antragspflicht
- **§ 246 AktG** ein Monat Anfechtungsklage AG
- **§ 47 EGAktG / § 14 UmwG** Frist Umwandlung
- **GWB-Anmeldung** Kartellrecht — vor Vollzug
- **Verjährung Geschäftsführer-Haftung** fünf Jahre § 43 GmbHG / § 93 AktG
- **Closing-Vertrags-Fristen**

### Frage 8 — Konflikt?

- Konzern-Konstellation (Mehrere Tochtergesellschaften)
- Vertretungs-Beziehungen historisch
- Geschäftsführer / Gesellschafter beide Mandanten?

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| GmbH-Gründung | `gmbh-gruendung` |
| Gesellschafter-Beschluss | `gesellschafterbeschluss` |
| Schriftliche Beschlussfassung | `schriftliche-beschlussfassung` |
| Handelsregister-Anmeldung | `handelsregisteranmeldung` |
| Aufsichtsrat-Protokoll | `aufsichtsrat-protokoll` |
| Compliance | `gesellschafts-compliance` |
| Tabellenprüfung | `tabellenpruefung` |
| Vollzugs-Checkliste | `vollzugs-checkliste` |
| DD-Findings Extraktion | `dd-findings-extraktion` |
| DealTeam-Zusammenfassung | `dealteam-zusammenfassung` |
| Integrations-Management | `integrations-management` |
| Wesentliche Verträge Anlage | `wesentliche-vertraege-anlage` |
| KI-Werkzeug-Übergabe | `ki-werkzeug-uebergabe` |
| Geschäftsführer-Haftung | `geschaeftsfuehrer-haftung-43-gmbhg` |
| Anpassen | `anpassen` |
| Plugin-Konfiguration | `kaltstart-interview` |

## Mandatsannahme

- **Konflikt-Check** sehr strikt — bei Konzern-Konstellationen Mehrfach-Berücksichtigung
- **Streitwert** bei M&A Kaufpreis bei Anfechtungsklage AG-Bedeutung
- **Honorarvereinbarung** häufig Festpreis oder Stundensatz
- **Versicherungs-Deckung** D&O Berufshaftpflicht Anwalt

## Eskalation

- **Telefon-Sofort** Insolvenznähe Gesellschafter-Versammlung morgen Closing
- **Binnen einer Stunde** Beschluss-Anfechtung Frist heute
- **Heute** Insolvenz-Antrag-Vorbereitung Sondersitzung
- **Diese Woche** Vertragsentwurf DD-Bericht

## Schritt-fuer-Schritt-Workflow

1. **Eilbeduerftigkeit pruefen (30 Sekunden):** Laeuft eine der oben genannten Fristen? Falls ja: sofortige Eskalation — nicht weiter triagieren.
2. **Acht Triage-Fragen stellen** (in der Reihenfolge oben): Rolle, Rechtsform, Vorgang, Eilbeduerftigkeit, Stand, Wirtschaft, Frist, Konflikt.
3. **Routing-Matrix anwenden:** Folge-Skill aus der Matrix auswaehlen und direkt starten.
4. **Fristenbuch befuellen:** Alle identifizierten Fristen sofort im Kanzlei-Fristenbuch mit Wiedervorlage eintragen.
5. **Mandatsanlage:** Mandat-Slug generieren, `mandat.md` anlegen (→ `gesellschaftsrecht-mandat-arbeitsbereich`).
6. **GwG-Identifizierung:** Bei neuem Mandanten Identifizierungspflicht (§§ 10 ff. GwG) vor Beratungsbeginn abarbeiten.
7. **Interessenkonflikt-Check:** Kanzlei-internes System pruefen; bei Zweifeln Mandat ablehnen oder aufteilen (§ 43a Abs. 4 BRAO).
8. **Ausgabe erzeugen:** Triage-Protokoll + Folge-Skill-Empfehlung.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Gesellschaftsrechtliches Mandat triagieren | Triage nach acht Fragen-Schema; Output unten |
| Variante A — Mandant beschreibt Problem unklar Beratung zuerst | Erstberatung und Sachverhaltsaufklaerung vor Triage |
| Variante B — Mehrere Gesellschaften betroffen | Triage fuer jede Gesellschaft separat durchfuehren |
| Variante C — Nur Dokumentencheck keine Mandatierung gewuenscht | Kurzgutachten statt Vollmandat |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template

**Adressat:** Bearbeitender Anwalt / Kanzlei-intern — Tonfall: sachlich-strukturiert, fristen-orientiert

```
TRIAGE-PROTOKOLL GESELLSCHAFTSRECHT
Mandat: [SLUG]
Datum: [TT.MM.JJJJ]
Bearbeitender Anwalt: [NAME]

--- EILSTATUS ---
Akute Frist: [JA — BESCHREIBUNG / NEIN]
Eskalationsstufe: [SOFORT-TELEFON / HEUTE / DIESE WOCHE / KEIN HANDLUNGSBEDARF]

--- MANDANT ---
Rolle: [GESELLSCHAFTER / GESCHAEFTSFUEHRER / KAEUFER / VERKAEUFER / etc.]
Name / Firma: [NAME]
Rechtsform der Gesellschaft: [GmbH / AG / etc.]
Gesellschaft: [FIRMA, HRB, REGISTERGERICHT]

--- VORGANG ---
[BESCHREIBUNG DES VORGANGS — ein bis zwei Saetze]
Rechtliche Einordnung: [§§ NORMEN]

--- FRISTEN (KRITISCHE PFADE) ---
| Frist | Norm | Ablauf | Wiedervorlage | Im Fristenbuch |
|---|---|---|---|---|
| [FRISTBEZEICHNUNG] | [§ NORM] | [TT.MM.JJJJ] | [TT.MM.JJJJ] | [JA / NEIN] |

--- FOLGE-SKILL ---
Empfehlung: [SKILL-NAME]
Begruendung: [EIN SATZ]

--- MANDATSANLAGE ---
Slug: [SLUG]
GwG-Identifizierung: [ABGESCHLOSSEN / AUSSTEHEND]
Interessenkonflikt geprueft: [JA / NEIN — ERGEBNIS]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — Frist: [DATUM]
2. [AKTION] — Frist: [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Rote Schwellen

- **Insolvenzantragspflicht § 15a InsO bereits ausgeloest** — 3-Wochen-Frist laeuft; Geschaeftsfuehrer persoenlich haftbar; sofortige Eskalation an Insolvenzrechts-Spezialisten.
- **Beschluss-Anfechtungsfrist § 246 AktG < 5 Tage** — Klage sofort vorbereiten; Fristversaeumung fuehrt zur Bestandskraft auch fehlerhafter Beschluesse.
- **Interessenkonflikt erkannt** — Mandat nicht annehmen oder aufteilen; § 43a Abs. 4 BRAO.
- **GwG-Identifizierung nicht abgeschlossen** — keine Beratungsleistung vor Identifizierung; Bussgeldhaftung bei Verstoss.

## Ausgabe

- `triage-protokoll-gesellschaftsrecht.md`
- Aktenanlage
- Frist im Fristenbuch (§ 15a InsO Anfechtungsfrist Closing)
- Mandatsvereinbarung
- Empfehlung Folge-Skill

## Quellen

- GmbHG AktG HGB UmwG GenG VereinsG
- InsO § 15a
- BGB
- BGH II. Zivilsenat
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Hueffer/Koch AktG
- Scholz GmbHG

## 5. `rechtsabteilung-beirat-mit-vetorechten-in-der-gmbh`

**Fokus:** Rechtsabteilungs-Fachmodul für Beirat mit Vetorechten in der GmbH: Beiratsrechte werden zwischen Beratung, Zustimmung, Weisung und faktischer Geschäftsführung abgegrenzt. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: Beirat mit Vetorechten in der GmbH

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechtsabteilung: Beirat mit Vetorechten in der GmbH` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Rechtsabteilung: Beirat mit Vetorechten in der GmbH
- **Spezialgegenstand:** Rechtsabteilung: Beirat mit Vetorechten in der GmbH. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Spezialkern: Rechtsabteilung: Beirat mit Vetorechten in der GmbH

- **Konkretes Problem:** Beiratsrechte werden zwischen Beratung, Zustimmung, Weisung und faktischer Geschäftsführung abgegrenzt.
- **Norm-/Quellenanker:** GmbHG, AktG, MoPeG/BGB-Gesellschaftsrecht, HGB, UmwG, Registerrecht, Treuepflicht, Organhaftung und Beschlussmängelrecht.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

GmbHG §§ 45, 46, 52; § 242 BGB; Rechtsprechung zu Beiräten live prüfen

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

Beiratsrechte werden zwischen Beratung, Zustimmung, Weisung und faktischer Geschäftsführung abgegrenzt.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.
