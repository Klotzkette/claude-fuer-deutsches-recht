---
name: anforderungsprofil-konstitutiv
description: "Anforderungsprofil Konstitutiv: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anforderungsprofil Konstitutiv

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anforderungsprofil Konstitutiv** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anforderungsprofil-konstitutiv-deklaratorisch` | Skill zur Unterscheidung konstitutives Anforderungsprofil und deklaratorisches Anforderungsprofil bei der beamtenrechtlichen Auswahlentscheidung. Klaert wann ein im Anforderungsprofil aufgestelltes Merkmal die Vergleichsbasis verengt und wann es nur als Auslegungshilfe der Beurteilungen dient. Liefert das Pruefschema zum Wegfall der Vergleichbarkeit bei willkuerlichem Anforderungsprofil und zur Rechtfertigung dienstpostenbezogener Eignungsanforderungen. Hilft bei Anfechtung der Auswahlentscheidung wenn der Mandant durch ein zugeschnittenes Profil ausgeschieden wird. |
| `anlassbeurteilung-vs-regelbeurteilung` | Klaert das Verhaeltnis von Regelbeurteilung und Anlassbeurteilung im Auswahlverfahren des oeffentlichen Dienstes. Skill pruef Beurteilungsstichtag Aktualitaet der Beurteilungsgrundlage und Vergleichbarkeit der konkurrierenden Beurteilungen. Behandelt die Konstellation einer Konkurrentensituation in der ein Bewerber eine Anlassbeurteilung erhaelt und ein anderer eine alte Regelbeurteilung. Liefert Argumente zur Frage wann Anlassbeurteilung Pflicht ist und wann sie unzulaessig waere. Verweist auf das Schwester-Skill plausibilisierung-gleicher-gesamtnoten und konkurrentenschutz-bestenauslese-art-33-ii-gg. |
| `anrechnung-55-beamtvg-mehrere-renten` | Skill zur Anrechnungsregelung von Renten auf die Beamtenversorgung nach § 55 BeamtVG. Klaert das Zusammenwirken der Beamtenversorgung mit gesetzlicher Rente Altersrente Erwerbsminderungsrente sowie Renten aus berufsstaendischer oder zwischenstaatlicher Versorgung. Behandelt das Verhaeltnis zum Hoechstgrenzenmodell die Behandlung von Kindererziehungszeiten und die unionsrechtlich gebotene Beruecksichtigung von EU-Renten. Liefert Berechnungstabelle und Antragsbausteine. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Anforderungsprofil Konstitutiv**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anforderungsprofil-konstitutiv-deklaratorisch`

**Fokus:** Skill zur Unterscheidung konstitutives Anforderungsprofil und deklaratorisches Anforderungsprofil bei der beamtenrechtlichen Auswahlentscheidung. Klaert wann ein im Anforderungsprofil aufgestelltes Merkmal die Vergleichsbasis verengt und wann es nur als Auslegungshilfe der Beurteilungen dient. Liefert das Pruefschema zum Wegfall der Vergleichbarkeit bei willkuerlichem Anforderungsprofil und zur Rechtfertigung dienstpostenbezogener Eignungsanforderungen. Hilft bei Anfechtung der Auswahlentscheidung wenn der Mandant durch ein zugeschnittenes Profil ausgeschieden wird.


# Anforderungsprofil — konstitutiv oder deklaratorisch

## 1. Zweck und Anwendungsfall

Skill fuer Konstellationen, in denen das Anforderungsprofil der Stellenausschreibung Merkmale enthaelt, die den Bewerberkreis einengen (typisch: Sprachzertifikat C1, mehrjaehrige Verwendung in einem Referat, Promotion, Auslandserfahrung, Personalfuehrungserfahrung).

## 2. Eingaben

- Wortlaut der Stellenausschreibung
- Anforderungskatalog mit Trennung "obligatorisch" / "fakultativ" / "wuenschenswert"
- Auswahlvermerk mit Begruendung des Ausschluss
- Stelleninhalt / Aufgabenkatalog der zu besetzenden Stelle

## 3. Ablauf / Checkliste

### a) Konstitutiv oder deklaratorisch
- Konstitutiv (auch: zwingend) ist ein Merkmal, dessen Fehlen ohne weitere Pruefung zum Ausschluss fuehrt. Es engt die Vergleichsgruppe ein.
- Deklaratorisch ist ein Merkmal, das nur die Auslegung der Beurteilung leitet und bei der Bewertung gewichtet wird.

### b) Rechtfertigungsanforderung
- Ein konstitutives Anforderungsprofil ist nur zulaessig, wenn es sachlich gerechtfertigt ist und einen Bezug zur konkreten Aufgabenwahrnehmung hat (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).
- Es darf nicht auf einen einzelnen Wunschbewerber zugeschnitten sein. Ein Zuschnittsverdacht ergibt sich aus Indizien (sehr enges Kriterienbuendel, Identitaet mit Vita des Wunschbewerbers, fehlende Vorgeschichte fuer solche Anforderungen).

### c) Folge eines unzulaessigen Profils
- Die Auswahlentscheidung ist rechtswidrig; das gesamte Verfahren ist neu zu durchlaufen.
- Bei laufendem Auswahlverfahren: einstweilige Anordnung gegen Ernennung des Konkurrenten — Skill `konkurrentenklage-einstweiliger-rechtsschutz`.

### d) Schutz des Wettbewerbsverfahrens
- Auch wenn ein einzelnes Merkmal entfaellt, bleibt der Bestenauslese-Grundsatz erhalten; die uebrigen Anforderungen sind weiter pruefen.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; § 9 BeamtStG; §§ 32 ff. BLV.
- Rspr.: BVerwG zum Anforderungsprofil — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefvermerk: Tabelle "Merkmal — konstitutiv ja oder nein — Begruendung — Sachzusammenhang — Rechtsfolge".
- Eilantragsbaustein.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Stelle Referatsleiterin im BMI A16. Konstitutiv gefordert: Promotion im oeffentlichen Recht, Auslandserfahrung in einem englischsprachigen Land, einschlaegige Personalfuehrungserfahrung in mindestens zwei Bundesministerien. Skill liefert Argument: Profil ist passgenau auf eine bestimmte Person zugeschnitten, daher unzulaessig.

## 2. `anlassbeurteilung-vs-regelbeurteilung`

**Fokus:** Klaert das Verhaeltnis von Regelbeurteilung und Anlassbeurteilung im Auswahlverfahren des oeffentlichen Dienstes. Skill pruef Beurteilungsstichtag Aktualitaet der Beurteilungsgrundlage und Vergleichbarkeit der konkurrierenden Beurteilungen. Behandelt die Konstellation einer Konkurrentensituation in der ein Bewerber eine Anlassbeurteilung erhaelt und ein anderer eine alte Regelbeurteilung. Liefert Argumente zur Frage wann Anlassbeurteilung Pflicht ist und wann sie unzulaessig waere. Verweist auf das Schwester-Skill plausibilisierung-gleicher-gesamtnoten und konkurrentenschutz-bestenauslese-art-33-ii-gg.


# Anlassbeurteilung vs. Regelbeurteilung — Aktualitaet und Vergleichbarkeit

## 1. Zweck und Anwendungsfall

Skill fuer den haeufigen Streit, ob die Auswahlentscheidung auf einer ausreichend aktuellen, miteinander vergleichbaren Beurteilungsgrundlage beruht. Zwei zentrale Konstellationen: (a) Mandant hat alte Regelbeurteilung, Konkurrent eine frische Anlassbeurteilung; (b) Mandant hat juengere Anlassbeurteilung, Konkurrent steht in Regelbeurteilung. Skill liefert die Argumentationsbausteine.

## 2. Eingaben

- Beurteilungsstichtag der Regelbeurteilung des Dienstherrn (typisch dreijaehriger Turnus, laenderspezifisch)
- Datum der letzten Beurteilung Mandant und letzter Beurteilung des Konkurrenten
- Beurteilungsrichtlinie des Dienstherrn (Behoerden-RL, ZBR, VwV)
- Konkurrentenmitteilung samt Auswahlvermerk

## 3. Ablauf / Checkliste

### a) Aktualitaetsgrenze
- Eine Beurteilung gilt nach staendiger Rechtsprechung des BVerwG nur eine begrenzte Zeit als hinreichend aktuell. Faustregel: rund drei Jahre, Einzelfall pruefen. Bei Aelterer Regelbeurteilung ist eine Anlassbeurteilung in der Regel geboten.

### b) Anlassbeurteilung als Pflicht oder Verbot
- Pflicht: wenn seit der letzten Beurteilung relevanter Zeitraum verstrichen ist oder eine wesentliche Veraenderung der Verwendung eingetreten ist.
- Unzulaessig oder problematisch: wenn die Anlassbeurteilung zu einer Ungleichbehandlung der Konkurrenten fuehrt, weil nur einer eine neue Beurteilung erhaelt.

### c) Vergleichbarkeit
- Gleicher Beurteilungsmaszstab, gleicher Beurteilungszeitraum, gleiche Beurteilungsskala — sonst Auswahlfehler.
- Bei unterschiedlichen Beurteilungssystemen (z. B. nach Wechsel zwischen Bund und Land) ist eine "Umsetzungsbetrachtung" erforderlich; ständige Rechtsprechung, konkret vor Zitat frei prüfen.

### d) Beurteilungszeitraum
- Kein nahtloser Anschluss erforderlich, aber Luecke darf nicht groesser sein als der Regelturnus.
- Beurteilungen ueber sehr kurzen Zeitraum (unter sechs Monaten) sind in der Regel angreifbar; Substanz im Beurteilungszeitraum nicht gegeben.

### e) Verwertbarkeit
- Eine in einem anderen Auswahlverfahren erstellte Anlassbeurteilung kann im neuen Verfahren grundsaetzlich herangezogen werden, sofern weiterhin aktuell und vergleichbar.

## 4. Quellenpflicht

- Normen: §§ 21, 22 BBG; § 18 BLV; Beurteilungsrichtlinien des Bundes oder des jeweiligen Landes.
- Rspr.: BVerwG zur Aktualitaet und Vergleichbarkeit von Beurteilungen — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefvermerk in Memoform mit Spalten "Aktualitaet — Vergleichbarkeit — Massstab — Spielraum".
- Schriftsatzbaustein "Begruendung Anordnungsanspruch" fuer Konkurrenteneilantrag.

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Regelbeurteilung Mandant Stichtag vor 4 Jahren, Bewertung "uebertrifft die Anforderungen". Konkurrentin erhielt vor drei Monaten Anlassbeurteilung mit der gleichen Endnote. Skill liefert Argument: entweder Anlassbeurteilung auch fuer Mandant erforderlich oder Auswahlvergleich auf Basis veralteter Regelbeurteilung unzulaessig — Auswahlentscheidung aufzuheben.

## 3. `anrechnung-55-beamtvg-mehrere-renten`

**Fokus:** Skill zur Anrechnungsregelung von Renten auf die Beamtenversorgung nach § 55 BeamtVG. Klaert das Zusammenwirken der Beamtenversorgung mit gesetzlicher Rente Altersrente Erwerbsminderungsrente sowie Renten aus berufsstaendischer oder zwischenstaatlicher Versorgung. Behandelt das Verhaeltnis zum Hoechstgrenzenmodell die Behandlung von Kindererziehungszeiten und die unionsrechtlich gebotene Beruecksichtigung von EU-Renten. Liefert Berechnungstabelle und Antragsbausteine.


# Anrechnung Renten nach § 55 BeamtVG

## 1. Zweck und Anwendungsfall

Skill fuer Versorgungsempfaenger, die neben der Beamtenversorgung Renten aus der gesetzlichen Rentenversicherung, einer berufsstaendischen Versorgungseinrichtung oder einer auslaendischen Versorgung beziehen.

## 2. Eingaben

- Versorgungsbescheid mit Bruttobezuegen
- Rentenbescheide aller Versorgungstraeger
- Art der Renten (Altersrente, Witwerrente, EM-Rente, betriebliche Versorgung)
- Datum des Rentenbeginns

## 3. Ablauf / Checkliste

### a) Grundprinzip
- Die Summe aus Beamtenversorgung und anrechenbarer Rente darf eine Hoechstgrenze nicht uebersteigen. Die Hoechstgrenze entspricht im Regelfall den ruhegehaltfaehigen Dienstbezuegen nach einer fiktiven Hoechstdienstzeit.

### b) Anrechenbare Renten
- Gesetzliche Rente einschliesslich Anteile aus Kindererziehungszeiten.
- Hinterbliebenenrenten ggf. anteilig.
- Auslaendische Renten (EU-Mitgliedstaaten) sind nach EuGH-Rechtsprechung zu beruecksichtigen — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Berufsstaendische Versorgung (Aerztekammer, Rechtsanwaltskammer) grundsaetzlich anrechenbar, soweit beamtengleicher Ursprung.

### c) Nicht anrechenbar
- Renten aus privater Lebens- oder Rentenversicherung.
- Renten, die ohne Bezug zum Beamtenverhaeltnis aus eigenen Beitraegen finanziert wurden, in dem Umfang nicht.

### d) Hinausgeschobener Versorgungsbeginn
- Beim Hinausschieben des Eintritts in den Ruhestand entfallen Anrechnungen anteilig.

## 4. Quellenpflicht

- Normen: § 55 BeamtVG; landesrechtliche Aequivalente; Verordnung EG 883/2004 (Soziale Sicherheit).
- Rspr.: BVerwG und EuGH zu § 55 BeamtVG — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnung der Hoechstgrenze und der Anrechnungsbetraege.
- Antragsschreiben bei Nichtanrechnung pflichtiger Bestandteile.

## 6. Verifizierte Quellenanker

- BeamtVG und jeweiliges Landesversorgungsrecht sauber trennen; Versorgung ist bei Landesbeamten seit der Föderalismusreform grundsätzlich Landesrecht.
- BVerfG, 27.09.2005 - 2 BvR 1387/02: Versorgungsänderungsrecht und Alimentationsprinzip als verfassungsrechtlicher Anker.
- BVerfG, 20.03.2007 - 2 BvL 11/04: Versorgung aus dem letzten Amt und Wartefrist.
- BVerwG, 25.10.2018 - 2 C 33.17 sowie BVerwG, 30.10.2018 - 2 C 32.17 als verifizierte Anker für Besoldungs-/Versorgungsvorlagen; Reichweite auf konkrete Versorgungsfrage jeweils prüfen.
- Konkrete Berechnung nie aus Modellwissen: Bescheid, Dienstzeiten, Ruhensnormen, Rentenbescheide und Landesrecht in Tabelle nachziehen.

## 7. Beispiel (Kurzfassung)

Pensionierter Studiendirektor erhaelt Altersrente aus zehn Jahren Lehrertaetigkeit vor Verbeamtung und zusaetzlich eine schwedische Tjaenstepension. Skill liefert Hoechstgrenzenberechnung und EuGH-konforme Beruecksichtigung der EU-Rente.
