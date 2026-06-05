---
name: normenkartierung-normenkontrollrat-kmu
description: "Normenkartierung Normenkontrollrat KMU: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Normenkartierung Normenkontrollrat KMU

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Normenkartierung Normenkontrollrat KMU** im Plugin Legistik Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Aenderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten muessen identifiziert werden. Such-Strategie BGBl-Online Bundesrecht.de Landesrecht-Portal Juris BeckOnline. Aenderungsliste je Norm Einfuegen Aendern Aufheben Folgeaenderung. Verweisketten Domino-Wirkungen Prüfung laufende Parallelverfahren. Output Aenderungsmatrix Grundlage für Referentenentwurf und Synopse. Anschluss terminologie-konsistenz zirkelschluss-prüfen. |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten. KMU-Aspekt mittelstandsrelevante Vorschriften. One-in-one-out-Regel Entlastungsnachweis. Statistik-Pflichten. Output NKR-Vorlage-Datei Anschreiben Erfuellungsaufwand-Tabelle KMU-Test One-in-one-out-Nachweis. Anschluss gesetzesentwurf-kabinett. Abgrenzung zu folgenabschaetzung-erfuellungsaufwand Methodik-Skill. |
| `normhierarchie-routing` | Richtige Startbahn und Normebene für ein legistisches Vorhaben bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschliessungsantrag. Anwendungsfall politische Vorgabe liegt vor und unklar ist, ob Bundesministerium, Bundestag, Landesministerium, Landtag oder sonstiger Normgeber handeln soll. Prüfkatalog Gesetzgebungskompetenz Bund Art. 70 bis 74 GG, Landeskompetenz, Verordnungsermaechtigung Art. 80 GG, Satzungskompetenz Art. 28 Abs. 2 GG, Wesentlichkeitstheorie, Vorbehalt des Gesetzes, GO-BT/Landtags-GO. Output Startbahn- und Normebenentscheidung mit Begründung und nächstem Skill. |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft werden. Kommunen Art. 28 Abs. 2 GG Gemeindeordnung Berufsstaendische Kammern BRAO IHK-Gesetz HwO Hochschulen Hochschulgesetz Sozialversicherungstraeger § 33 SGB IV. Vorbehalt des Gesetzes Wesentlichkeitstheorie BVerfGE 33/125 Ermaechtigungsgrundlage Inhalt Zweck Ausmass Genehmigungsvorbehalt Aufsichtsbehoerde Bekanntmachung richtiges Publikationsorgan. Output Empfehlung Satzung auf welcher Grundlage erlassbar. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Normenkartierung Normenkontrollrat KMU**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `normenkartierung`

**Fokus:** Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Aenderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten muessen identifiziert werden. Such-Strategie BGBl-Online Bundesrecht.de Landesrecht-Portal Juris BeckOnline. Aenderungsliste je Norm Einfuegen Aendern Aufheben Folgeaenderung. Verweisketten Domino-Wirkungen Prüfung laufende Parallelverfahren. Output Aenderungsmatrix Grundlage für Referentenentwurf und Synopse. Anschluss terminologie-konsistenz zirkelschluss-prüfen.


# Normenkartierung

> Ein Eingriff geschieht nie isoliert. Jede Norm steht in einem Verweisnetz.

## Schritt 1 - Hauptzielgesetz finden

Wo soll die neue Regelung leben? Stammgesetz identifizieren (z.B. HGB, BGB, ZPO, FamFG, GO, BauGB).

## Schritt 2 - Direkte Folgenormen suchen

In welchen anderen Gesetzen wird auf das Hauptzielgesetz verwiesen? Im Internet:

- gesetze-im-internet.de
- buzer.de (Änderungsgeschichte)
- DIP des Bundestages
- BeckOnline-Verweisindex
- Juris-Linkliste
- Landesrecht-Portale (Bayern, NRW etc.)

## Schritt 3 - Verordnungs- und Satzungsstrecke

Welche Verordnungen sind auf dem Hauptzielgesetz erlassen? Welche Satzungen rekurrieren auf das Gesetz?

## Schritt 4 - Begriffsdefinitionen

Wenn das Vorhaben einen Begriff einführt: existiert dieser Begriff schon woanders? Mit gleicher Definition? Mit abweichender Definition? Kollidiert?

## Schritt 5 - Änderungsmatrix aufbauen

| Lfd | Norm | Paragraf | Änderungsart | Inhalt | Grund |
|---|---|---|---|---|---|
| 1 | HGB | 33 | Änderung | Pflicht-Postfach | Hauptregelung |
| 2 | HGB | 13d | Änderung | Zweigniederlassungen einbezogen | Folgeaenderung |
| 3 | ZPO | Normtext, amtliche Hinweise, verifizierte Rechtsprechung |
| 4 | FamFG | 14 | Änderung | Bekanntgabe an Postfach | Anpassung |
| 5 | DSGVO-Anpassungs-G | - | - | Verweis prüfen | Datenschutz |

## Schritt 6 - Verweisketten prüfen

Wenn Norm A auf Norm B verweist und sich B aendert, muss Norm A prüfen, ob der Verweis noch passt. Verweisketten über mehrere Gesetze sind heimtueckisch.

## Schritt 7 - Paralleles Gesetzgebungsverfahren?

Wird eine der zu aendernden Normen zur gleichen Zeit in einem anderen Gesetzgebungsverfahren geändert? Dann Abstimmung mit dem anderen Verfahren über Reihenfolge oder Änderungsbefehl.

## Schritt 8 - EU-Normen, internationale Bezüge

Welche EU-Richtlinien oder Verordnungen werden beruehrt? Welche völkerrechtlichen Verträge sind betroffen?

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 42-44 GGO (Normenkartierung im Referentenentwurf, Pflichten) — Art. 3 Abs. 1 GG (Gleichheitssatz bei inkonsistenter Normgebung) — Art. 20 Abs. 3 GG (Normenklarheit als Rechtsstaat-Gebot) — § 1 EGBGB (Kollisionsrecht bei Normenkonkurrenz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Änderungsmatrix als Markdown- und Excel-Vorlage. Eintrag in das Auftragsblatt: Liste der zu aendernden Normen.

## Anschluss

`terminologie-konsistenz`, `zirkelschluss-pruefen`, dann `referentenentwurf-bauen`.

## 2. `normenkontrollrat-kmu-check`

**Fokus:** Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten. KMU-Aspekt mittelstandsrelevante Vorschriften. One-in-one-out-Regel Entlastungsnachweis. Statistik-Pflichten. Output NKR-Vorlage-Datei Anschreiben Erfuellungsaufwand-Tabelle KMU-Test One-in-one-out-Nachweis. Anschluss gesetzesentwurf-kabinett. Abgrenzung zu folgenabschaetzung-erfuellungsaufwand Methodik-Skill.


# Normenkontrollrat / KMU-Check

> Der NKR ist die wichtigste Pruefinstanz für Erfüllungsaufwand.

## Nationaler Normenkontrollrat (NKR)

Unabhängiges Beratungsgremium der Bundesregierung. Einrichtung durch NKRG (Gesetz über den Nationalen Normenkontrollrat) 2006.

### Aufgabe

Prüfung des Erfüllungsaufwands und der Folgekosten von Bundesgesetzen, Verordnungen und Allgemeinverwaltungsvorschriften.

### Pruefberichte

Der NKR erstellt einen Pruefbericht, der dem Kabinettsentwurf als Anlage beigefügt wird. Negative Berichte erschweren das parlamentarische Verfahren.

## KMU-Test

Mittelstandsrelevante Vorschriften müssen einen besonderen KMU-Check bestehen:

- Welche Adressaten sind Unternehmen mit weniger als 250 Beschaeftigten?
- Welche Umsetzungskosten?
- Welche Alternativen sind milder?
- Welche Ausnahmen / Schwellenwerte?

## One-in-one-out

Seit 2015 Bundesregierungsregel: Jeder neue Bürokratieaufwand für die Wirtschaft muss durch Entlastung an anderer Stelle ausgeglichen werden.

### Prüfraster

- Pro neuem Aufwand: identifizieren Sie das Pendant zur Entlastung
- Methodische Hilfe: SKK Standard-Kostenmodell

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1-8 NKRG (Normenkontrollrat-Gesetz) — § 62 Abs. 1 GGO (NKR-Beteiligung Pflicht) — Art. 5 EUV (EU-Verhaeltnismaessigkeit, KMU-Test) — Leitlinien KMU-Test Europaeische Kommission COM 2009 (SME-Test)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- NKR-Vorlagedatei
- Anschreiben
- Anlagen:
 - Erfüllungsaufwand-Tabelle
 - KMU-Test-Bericht
 - One-in-one-out-Nachweis

## Anschluss

`gesetzesentwurf-kabinett`.

## 3. `normhierarchie-routing`

**Fokus:** Richtige Startbahn und Normebene für ein legistisches Vorhaben bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschliessungsantrag. Anwendungsfall politische Vorgabe liegt vor und unklar ist, ob Bundesministerium, Bundestag, Landesministerium, Landtag oder sonstiger Normgeber handeln soll. Prüfkatalog Gesetzgebungskompetenz Bund Art. 70 bis 74 GG, Landeskompetenz, Verordnungsermaechtigung Art. 80 GG, Satzungskompetenz Art. 28 Abs. 2 GG, Wesentlichkeitstheorie, Vorbehalt des Gesetzes, GO-BT/Landtags-GO. Output Startbahn- und Normebenentscheidung mit Begründung und nächstem Skill.


# Normhierarchie-Routing

> Entscheidet: Wer kann handeln, auf welcher Ebene und in welchem Verfahren?

## Eingabe

Auftragsblatt aus `legistik-auftragsaufnahme`.

## Prüfraster

### Vorfrage - Welcher institutionelle Pfad?

| Pfad | Wann naheliegend? | Nächster Skill |
|---|---|---|
| Bundesministerium / Bundesregierung | Bundeskompetenz, Regierungsprogramm, Kabinettspfad, Rechtsverordnung des Bundes | `referentenentwurf-bauen`, `gesetzesentwurf-kabinett`, `verordnungsermaechtigung-art80` |
| Bundestag / Fraktion / Abgeordnete | Parlamentarischer Gesetzentwurf, Änderungsantrag, Entschließungsantrag oder Antrag | `formulierungshilfe-bauen` |
| Landesministerium / Landesregierung | Landeskompetenz, Landesvollzug, Landesverordnung, Landesgesetz | `referentenentwurf-bauen`, danach landesspezifische Kabinetts-/Landtagsprüfung |
| Landtag / Landtagsfraktion | Landesparlamentarischer Antrag oder Gesetzentwurf aus der Mitte des Landtags | `formulierungshilfe-bauen` |
| Kommune / Kammer / Hochschule / sonstige Körperschaft | Selbstverwaltungs- oder Fachsatzung, Beschlussvorlage, Bekanntmachung | `satzungskompetenz-pruefen` |

Wenn ein Vorhaben nur eine politische Position, Prüfbitte oder Aufforderung an Regierung/Verwaltung enthält, kann ein Antrag oder Entschließungsantrag richtiger sein als ein Gesetz.

### A - Ist es überhaupt eine zu kodifizierende Materie?

Wenn die politische Vorgabe nur Verwaltungspraxis aendern soll, reicht ein Erlass / eine Verwaltungsvorschrift. Kein Norm-Schritt noetig.

### B - Wenn Gesetz: Bund oder Land?

1. Prüfung **ausschließliche Gesetzgebung Bund** (Art. 71 und 73 GG): auswärtige Angelegenheiten, Verteidigung, Staatsangehoerigkeit, Wahrungseinheit, Bundeseisenbahnen, Luftverkehr, Postwesen, Telekommunikation, Bundeskriminalpolizei, Zoelle, Schutz deutsches Kulturgut.
2. Prüfung **konkurrierende Gesetzgebung** (Art. 72 und 74 GG): Bürgerliches Recht, Strafrecht, Gerichtsverfassung, Aufenthaltsrecht, Sozialrecht, Wirtschaftsrecht, Arbeitsrecht, Straßenverkehr, öffentliche Fürsorge, Recht der Wirtschaft, etc. Prüfung **Erforderlichkeitsklausel** Art. 72 Abs. 2 GG bei den dort genannten Materien.
3. Wenn weder Art. 71 noch Art. 73 noch Art. 74: **Landeszustaendigkeit** Art. 70 Abs. 1 GG (Auffangkompetenz).

Bei Landeszuständigkeit:

- Bundesland ausdrücklich benennen.
- Landesverfassung, Geschäftsordnung der Landesregierung und Geschäftsordnung des Landtags als Prüfquellen markieren.
- Prüfen, ob eine landesrechtliche Verordnung oder Satzung genügt oder ein Landesgesetz erforderlich ist.

### C - Wenn Gesetz oder Rechtsverordnung?

- **Wesentlichkeitstheorie BVerfG**: Grundrechtsrelevante Regelungen müssen vom parlamentarischen Gesetzgeber selbst getroffen werden. Faustregel: Wer betrifft den Bürger in seinen Grundrechten erheblich, muss als Gesetz geregelt werden.
- **Strafgesetz und Bußgeldgesetz**: nur Gesetz (Art. 103 Abs. 2 GG iVm Wesentlichkeitstheorie).
- **Detailregelungen technischer Art**: Rechtsverordnung kommt in Betracht.

### D - Wenn Rechtsverordnung Bund: Gibt es Ermaechtigungsgrundlage Art. 80 GG?

Prüfen mit Skill `verordnungsermaechtigung-art80`. Wenn keine ausreichende Ermaechtigung vorhanden: zunächst Gesetz aendern, um Ermaechtigung zu schaffen, dann VO erlassen.

### E - Wenn Satzung: Gibt es Satzungskompetenz?

- Kommunale Satzungen: Selbstverwaltungsgarantie Art. 28 Abs. 2 GG plus Gemeindeordnung des Landes plus ggf. spezielle Fachgesetze (z.B. BauGB für Bebauungspläne, KAG für Beitragssatzungen, BImSchG für Laermsatzungen).
- Berufsstaendische Satzungen: Kammerngesetz (z.B. BRAO, BAeO, IHK-Gesetz) plus Vorbehalt des Gesetzes BVerfG E 33 / 125 (Facharzt).
- Hochschulsatzungen: Hochschulgesetz Land plus Selbstverwaltung Art. 5 Abs. 3 GG.
- Sozialversicherungsträger: Satzungsbefugnis nach SGB IV.
- Rundfunkanstalten: Rundfunkstaatsvertrag plus Landesrundfunkgesetze.

### F - Wenn Mehrebenen-Vorhaben

Manchmal braucht es: Bundesgesetz (Rahmen), Bundesverordnung (Details), Landesgesetz (Umsetzung), Verwaltungsvorschrift (Vollzug). Dann ist eine Tabelle der Ebenen zu erstellen.

### G - Wenn parlamentarischer Antrag ohne Normtext

Ein Antrag, Entschließungsantrag oder Prüfauftrag ist naheliegend, wenn:

- das Parlament die Regierung zu einem Bericht, Entwurf oder Verhalten auffordern soll,
- ein politischer Alternativvorschlag ohne sofortigen Normtext gebraucht wird,
- die Gesetzgebungskompetenz unsicher ist und zuerst ein Prüfauftrag sinnvoller ist,
- eine Oppositionsfraktion ein Thema parlamentarisch sichtbar machen will.

Dann zu `formulierungshilfe-bauen` routen, aber als Antrag/Entschließungsantrag, nicht als Normtext.

## Arbeitsgrundlagen

- Art. 70-74 GG: Kompetenzverteilung Bund/Länder.
- Art. 76-78 GG: Bundesgesetzgebungsverfahren und Einbringungswege.
- Art. 80 GG: Anforderungen an Rechtsverordnungsermächtigungen.
- Art. 28 Abs. 2 GG: Kommunale Selbstverwaltung als Ausgangspunkt für Satzungen.
- Art. 31 GG: Bundesrecht bricht Landesrecht.
- GO-BT und Landtags-Geschäftsordnungen: parlamentarische Vorlagen, Anträge und Änderungsanträge.
- Landesverfassungen und Verkündungsrecht: landesspezifischer Pfad.
- EU-Recht: Anwendungsvorrang und Umsetzungsbedarf im jeweiligen Fachskill prüfen.

## Zentrale Normen (Paragrafenkette)

Art. 70-74 GG — Art. 76-78 GG — Art. 80 GG — Art. 28 Abs. 2 GG — Art. 31 GG — Art. 1 Abs. 3 GG — Art. 93 Abs. 1 Nr. 2 GG — Art. 100 GG — Art. 288 AEUV — GO-BT — jeweilige Landesverfassung und Landtags-GO

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

- Entscheidung institutionelle Startbahn
- Entscheidung Norm-Ebene oder parlamentarischer Antragstyp
- drei Sätze Begründung
- offene landesspezifische oder geschäftsordnungsrechtliche Punkte
- Verweis auf nächsten Skill `gesetzgebungskompetenz-pruefen`, `verordnungsermaechtigung-art80`, `satzungskompetenz-pruefen`, `referentenentwurf-bauen` oder `formulierungshilfe-bauen`

## Stolperfallen

- Goldplating durch Wahl der falschen Ebene (Bund regelt, was Land regeln duerfte): prüfen unter `goldplating-vermeiden`
- Wesentlichkeitstheorie wird oft übersehen, wenn das Ministerium "schnell per VO" regeln will
- Subsidiaritaetsprinzip EU bei Kompetenzfragen mitdenken

## 4. `satzungskompetenz-pruefen`

**Fokus:** Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft werden. Kommunen Art. 28 Abs. 2 GG Gemeindeordnung Berufsstaendische Kammern BRAO IHK-Gesetz HwO Hochschulen Hochschulgesetz Sozialversicherungstraeger § 33 SGB IV. Vorbehalt des Gesetzes Wesentlichkeitstheorie BVerfGE 33/125 Ermaechtigungsgrundlage Inhalt Zweck Ausmass Genehmigungsvorbehalt Aufsichtsbehoerde Bekanntmachung richtiges Publikationsorgan. Output Empfehlung Satzung auf welcher Grundlage erlassbar.


# Satzungskompetenz prüfen

> Satzungen sind autonome Rechtssetzung. Sie brauchen aber immer eine staatliche Ermaechtigung.

## Pruefstation 1 - Welche Koerperschaft erlaesst die Satzung?

- Gemeinde / Landkreis (kommunale Satzung)
- Rechtsanwaltskammer (berufsstaendische Satzung)
- Ärztekammer
- Industrie- und Handelskammer
- Handwerkskammer
- Universität (Grundordnung, Prüfungsordnung, Habilitationsordnung)
- Sozialversicherungsträger (Krankenkassen-Satzung, BG-Satzung)
- Öffentlich-rechtliche Rundfunkanstalt

## Pruefstation 2 - Welche Ermaechtigung gibt es?

| Koerperschaft | Ermaechtigung |
|---|---|
| Gemeinde | Art. 28 Abs. 2 GG iVm Gemeindeordnung des Landes (BayGO, NRW-GO etc.) plus ggf. Fachgesetz |
| Landkreis | Landkreisordnung des Landes |
| Rechtsanwaltskammer | BRAO Paragraf 89 |
| Ärztekammer | Landes-Heilberufekammergesetz |
| IHK | IHK-Gesetz Paragraf 4 |
| Handwerkskammer | HwO Paragraf 106 |
| Hochschule | Hochschulgesetz des Landes |
| Krankenkasse | SGB IV Paragraf 33 plus SGB V |
| BG | SGB VII Paragraf 33 ff. |
| ARD-Anstalt | Landesrundfunkgesetz |

## Pruefstation 3 - Vorbehalt des Gesetzes

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Faustregel: je tiefer der Grundrechtseingriff, desto mehr muss das ermaechtigende Gesetz selbst regeln.

## Pruefstation 4 - Bestimmtheit der Ermaechtigung

Art. 80 GG gilt nicht direkt für Satzungen, aber sinngemäß: Inhalt Zweck Ausmass müssen aus dem ermaechtigenden Gesetz erkennbar sein.

## Pruefstation 5 - Verfahren des Erlasses

| Koerperschaft | Verfahren |
|---|---|
| Gemeinde | Beschluss Gemeinderat plus öffentliche Bekanntmachung im Amtsblatt der Gemeinde |
| Kammer | Beschluss Vertreterversammlung plus Bekanntmachung im Kammer-Mitteilungsblatt |
| Hochschule | Beschluss Senat plus Bekanntmachung in der amtlichen Bekanntmachung der Hochschule |
| Krankenkasse | Beschluss Verwaltungsrat plus Genehmigung BVA / LSA |

## Pruefstation 6 - Aufsichtsgenehmigung

Manche Satzungen brauchen vor Bekanntmachung Genehmigung der Aufsichtsbehoerde (z.B. Friedhofssatzungen ggf. nach Landesrecht; Beitragssatzungen oft anzeigepflichtig).

## Pruefstation 7 - Bekanntmachung

Die Satzung muss im richtigen Publikationsorgan bekanntgemacht werden. Fehlerhafte Bekanntmachung kann zur Nichtigkeit führen.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 28 Abs. 2 GG (Selbstverwaltungsgarantie) — §§ 1-5 GO (jeweilige Gemeindeordnung, Satzungs-Ermaechtigungen) — Art. 80 GG (analog Verordnungs-Ermaechtigungs-Grundsaetze fuer Satzungen) — § 47 VwGO (Normenkontrolle gegen Satzungen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

| Frage | Antwort |
|---|---|
| Erlassende Koerperschaft | |
| Ermaechtigungsgrundlage | |
| Vorbehalt des Gesetzes gewahrt | |
| Bestimmtheit der Ermaechtigung | |
| Erlass-Verfahren | |
| Aufsichtsgenehmigung erforderlich | |
| Bekanntmachung wo | |

## Anschluss

`normenkartierung` und entweder `referentenentwurf-bauen` (wenn Satzung Volltext kommt) oder direkt Ausgabe-Format Satzung.
