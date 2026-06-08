---
name: adhaesionsverfahren-ermittlungsverfahren
description: "Adhaesionsverfahren Ermittlungsverfahren im Strafrecht: prüft konkret Red-Team Qualitygate im Plugin fachanwalt-strafrecht, Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten, Ermittlungsverfahren, Orientierung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Adhaesionsverfahren Ermittlungsverfahren

## Arbeitsbereich

**Adhaesionsverfahren Ermittlungsverfahren** ordnet den Fall über die tragenden Prüfungslinien: Red-Team Qualitygate im Plugin fachanwalt-strafrecht, Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten, Ermittlungsverfahren. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `fachanwalt-strafrecht-adhaesionsverfahren` | Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess. §§ 403-406c StPO Adhaesionsverfahren, § 823 BGB Schadensersatz, § 253 BGB Schmerzensgeld. Prüfraster Zulässigkeit im Strafverfahren, Antragsschrift-Anforderungen, Beweisangebot, taktische Abwaegung Adhaesion vs. separater Zivilprozess. Output Adhaesionsantrag mit Schadensaufstellung und taktischer Einordnung. Abgrenzung zu Taeter-Opfer-Ausgleich § 46a StGB und zu Verständigung § 257c StPO. |
| `spezial-ermittlungsverfahren-vergleich-eskalation` | Ermittlungsverfahren: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-orientierung-fristen-form-und-zuständigkeit` | Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `strafprozess-aktenlog-fristen-und-wiedervorlagen` | Aktenlog, Fristenbuch und Wiedervorlagen im Strafverfahren: erstellt aus Eingangspost, beA, EGVP, Verfügung, Ladung, Beschluss, Strafbefehl, Urteil und Aktennachlieferung eine robuste Fristen- und Aufgabensteuerung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

### Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin fachanwalt-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Strafrechts-Red-Team-Checks
- **Halluzinations-Check:** Keine erfundenen BGH/BVerfG-Az; bei staendiger Rspr. nur "BGH-Linie / staendige Rspr." schreiben.
- **Frist-Re-Check** alle Verfahrensschritte: Berufung § 314 StPO (1 Woche), Revision § 341 StPO (1 Woche) + § 345 StPO (1 Monat), Strafbefehl-Einspruch § 410 StPO (2 Wochen), Beschwerde § 311 StPO (sofortige 1 Woche; einfache § 304 StPO unbefristet), Wiedereinsetzung § 44 StPO (1 Woche ab Wegfall), Klageerzwingungsverfahren § 172 StPO.
- **Belehrungs-Re-Check:** § 136 StPO Beschuldigtenbelehrung; § 52 StPO Zeugnisverweigerung Angehoeriger; § 55 StPO Auskunftsverweigerung; § 257c V StPO Verstaendigungsbelehrung; qualifizierte Belehrung bei Wiederholung der Vernehmung.
- **Beweisverwertungs-Check:** § 136a StPO verbotene Vernehmungsmethoden; § 252 StPO Sperrwirkung; Beweisverwertungsverbote bei Belehrungsmaengeln (BGH-Linie).
- **Verfahrensruegen-Check für Revision:** absoluter Revisionsgrund § 338 StPO (Besetzung, Ausschlussgruende, Sachleitung); relativer § 337 StPO; Verstaendigungsmaengel § 257c StPO; Akteneinsichts-Verletzung § 147 StPO.
- **Vollmachts-Check:** Mandatsvollmacht; Vertretungsvollmacht für § 411 II StPO bei Strafbefehl, § 232 StPO bei Abwesenheitsverhandlung.
- **Konsequenzen-Re-Check:** BZRG-Eintrag, FZR-Eintrag, berufsrechtliche Konsequenzen (Beamtenrecht, Aerzte, Rechtsanwaelte), auslaendische Folgen (Visum, Niederlassung).
- **Mandantengeheimnis** § 43a Abs. 2 BRAO, § 203 StGB, § 53 I Nr. 2 StPO Zeugnisverweigerung.

## 2. `fachanwalt-strafrecht-adhaesionsverfahren`

**Fokus:** Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess. §§ 403-406c StPO Adhaesionsverfahren, § 823 BGB Schadensersatz, § 253 BGB Schmerzensgeld. Prüfraster Zulässigkeit im Strafverfahren, Antragsschrift-Anforderungen, Beweisangebot, taktische Abwaegung Adhaesion vs. separater Zivilprozess. Output Adhaesionsantrag mit Schadensaufstellung und taktischer Einordnung. Abgrenzung zu Taeter-Opfer-Ausgleich § 46a StGB und zu Verständigung § 257c StPO.

### Adhäsionsverfahren im Strafverfahren

## Kernsachverhalt & Mandantenfragen

Das Adhäsionsverfahren verbindet Strafprozess und Zivilrecht. Es spart der verletzten Person eine eigenständige Zivilklage. Gleichzeitig ist es für die Verteidigung ein Instrument zur Schadensminimierung: Ein Adhäsionsvergleich kann das Strafmaß erheblich beeinflussen (§ 46a StGB).

**8 Kaltstart-Rückfragen:**

1. Was ist die konkrete Straftat und wann wurde sie begangen? Liegt ein Aktenzeichen vor?
2. Welche zivilrechtlichen Schäden sind entstanden: Körperverletzung (Schmerzensgeld), Vermögensschaden (Betrug, Diebstahl), Sachschäden, Verdienstausfall?
3. Liegen ärztliche Atteste, Behandlungsberichte oder Gutachten zur Schadenshöhe vor?
4. Hat die Versicherung (z.B. Krankenversicherung, Unfallversicherung) bereits Leistungen erbracht? Forderungsübergang nach § 116 SGB X prüfen.
5. Ist der/die Angeklagte zahlungsfähig? Pfändbare Vermögenswerte vorhanden oder Insolvenz droht?
6. Besteht parallele Nebenklage oder soll der Adhäsionsantrag ohne Nebenklage gestellt werden?
7. Ist ein außergerichtlicher Vergleich mit dem/der Angeklagten bereits diskutiert oder gescheitert?
8. Welcher Betrag soll konkret geltend gemacht werden, oder soll das Schmerzensgeld dem Ermessen des Gerichts überlassen bleiben?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 403 StPO | Adhäsionsrecht: Verletzte kann vermögensrechtliche Ansprüche aus der Tat im Strafverfahren geltend machen |
| § 404 StPO | Form und Inhalt des Adhäsionsantrags; schriftlich oder zu Protokoll; bis Schluss der Beweisaufnahme |
| § 405 StPO | Adhäsionsvergleich als Vollstreckungstitel; Protokollierung in der Hauptverhandlung |
| § 406 StPO | Entscheidung durch Strafgericht; Grundurteil; Absehen von Entscheidung bei Verfahrensverzögerung |
| § 406a StPO | Rechtsmittel gegen Adhäsionsentscheidung; eingeschränkte Berufungsmöglichkeit |
| § 406b StPO | Vorläufige Vollstreckbarkeit des Adhäsionsurteils |
| § 406c StPO | Vollstreckbarerklärung des Vergleichs |
| § 472a StPO | Kosten des Adhäsionsverfahrens für Verletzte: grundsätzlich kostenfrei |
| § 46a StGB | Täter-Opfer-Ausgleich und Schadenswiedergutmachung als Strafmilderungsgrund |
| § 46 Abs. 2 StGB | Strafzumessung: Schadenswiedergutmachung berücksichtigungsfähig |
| § 253 Abs. 2 BGB | Schmerzensgeld bei Körper-, Gesundheits-, Freiheitsverletzung oder sexueller Selbstbestimmung |
| §§ 249–252 BGB | Art und Umfang des Schadensersatzes; Naturalrestitution, Wertersatz |
| §§ 823–826 BGB | Deliktsrecht: Grundlagen der Schadensersatzpflicht |
| § 830 BGB | Mittäter und Beteiligte haften als Gesamtschuldner |
| § 116 SGB X | Forderungsübergang bei Sozialleistungsträgern (Krankenkasse, Rentenversicherung) |

---

## Leitentscheidungen (Stand Mai 2026)

| Aktenzeichen | Gericht / Datum | Tragende Aussage | Offene Fundstelle |
|---|---|---|---|
| 3 StR 340/24 | BGH (3. Strafsenat), Beschluss 09.01.2025 | Adhäsionsentscheidung im Strafverfahren — Begründungsanforderungen an Schmerzensgeldzumessung; Strafgericht muss die maßgeblichen Zumessungsgesichtspunkte (Verletzungsbild, Dauer, Folgen) erkennbar machen | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.01.2025&Aktenzeichen=3+StR+340/24 |
| 4 StR 232/25 | BGH (4. Strafsenat), Beschluss 20.11.2025 | Zusammenspiel TOA / Schadenswiedergutmachung (§ 46a StGB) und Adhäsionsforderung — Strafmilderung setzt kommunikativen Aussöhnungsprozess voraus, nicht nur Zahlung | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25 |

Weitere Entscheidungen vor Verwendung live in dejure.org/openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Prüfschema Adhäsionsverfahren

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Anspruchsgrundlage prüfen: § 823 BGB (Körperverletzung, Sachschaden), § 826 BGB (sittenwidrige Schädigung bei Betrug), § 249/253 BGB (Schaden und Schmerzensgeld) | §§ 249, 253, 823 BGB |
| 2 | Verletzteneigenschaft prüfen: Nur unmittelbar Verletzte (§ 403 StPO); mittelbar Betroffene ausgeschlossen | § 403 StPO |
| 3 | Forderungsübergang prüfen: § 116 SGB X bei Krankenkassenleistungen; Eigenanteil ermitteln | § 116 SGB X |
| 4 | Schadenshöhe ermitteln: Schmerzensgeld nach Tabellen (Hacks/Slizyk); materieller Schaden beziffern; Feststellungsantrag für Zukunftsschäden | § 253 Abs. 2 BGB |
| 5 | Vollstreckungsperspektive prüfen: Zahlungsfähigkeit des/der Angeklagten; Insolvenzsituation; pfändbares Vermögen | §§ 704, 794 ZPO |
| 6 | Adhäsionsantrag formulieren: bestimmter Antrag (Zahlung, Feststellung, Herausgabe); Sachverhalt; Beweismittel | § 404 StPO |
| 7 | Fristwahrung: Antrag bis Beginn der Schlussvorträge (spätestens); frühzeitig einreichen | § 404 Abs. 1 StPO |
| 8 | Vergleichsstrategie aus Verteidigung: § 46a StGB als Strafmilderungsargument; Ratenvereinbarung vorbereiten | § 46a StGB |
| 9 | Vergleich nach § 405 StPO: In Hauptverhandlung protokollieren lassen; wird Vollstreckungstitel | § 405 StPO |
| 10 | Grundurteil und Folgeentscheidung: Bei Bezifferungsproblemen Grundurteil nach § 406 Abs. 1 S. 2 StPO; Quantifizierung im Zivilverfahren | § 406 Abs. 1 S. 2 StPO |
| 11 | Absehen-Antrag der Verteidigung: § 406 Abs. 1 S. 3–6 StPO – wenn Adhäsion Verfahren wesentlich verzögert | § 406 StPO |
| 12 | Vollstreckung: Titel nach § 794 ZPO; Gerichtsvollzieher, Forderungspfändung; bei Insolvenz: Tabellenanmeldung | § 794 ZPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Adhaesionsverfahren fuehren | Adhaesionsantrag; Template unten |
| Variante A — Mandant will Strafverfahren trennen | Zivilklage separat; Adhaesion entfaellt |
| Variante B — Strafgericht verweist Adhaesion | Nachfolge-Zivilklage; Bindungswirkung des Strafurteils |
| Variante C — Schadenshoehe unklar | Feststellungsklage zuerst; Leistungsklage nach Konkretisierung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Adhäsionsantrag auf Schmerzensgeld

```
An das [Gericht]
Aktenzeichen: [...]

Adhäsionsantrag gemäß §§ 403 ff. StPO

In der Strafsache gegen [Name Angeklagte/r]
wegen [Tatvorwurf]

beantragt die Verletzte [Name] durch ihre anwaltliche Vertretung:

1. Die/den Angeklagte/n wird verurteilt, an die Verletzte
 ein angemessenes Schmerzensgeld zu zahlen, dessen Höhe
 in das Ermessen des Gerichts gestellt wird, jedoch den
 Betrag von [z.B. 15.000 Euro] nicht unterschreiten sollte,
 nebst Zinsen in Höhe von fünf Prozentpunkten über dem
 Basiszinssatz seit Rechtshängigkeit dieses Antrags.

2. Es wird festgestellt, dass die/der Angeklagte verpflichtet
 ist, der Verletzten alle weiteren materiellen und immateriellen
 Schäden zu ersetzen, die aus der Tat vom [Datum] künftig noch
 entstehen, soweit Ansprüche nicht auf Dritte oder Sozial-
 versicherungsträger übergegangen sind.

Begründung:
Die Verletzte erlitt durch die Tat vom [Datum] folgende
Verletzungen: [konkret aufzählen]. Sie wurde [X Tage]
stationär behandelt und befand sich [X Wochen] in ambulanter
Therapie. Behandlungsunterlagen werden als Anlage 1 bis 3
beigefügt.

Das Schmerzensgeld ist nach den Grundsätzen der Ausgleichs-
und Genugtuungsfunktion (§ 253 Abs. 2 BGB) zu bemessen.
Vergleichbare Verletzungen werden in der Rechtsprechung mit
[Betragsbereich] bewertet (Slizyk, Beck'sche Schmerzensgeld-
tabelle, [aktuelle Auflage], Nr. [XX]).

[Ort, Datum]
[Unterschrift]
```

### Baustein 2 – Adhäsionsvergleich (Protokollvorlage)

```
In der Hauptverhandlung am [Datum]
Aktenzeichen: [...]

schließen die Parteien folgenden Vergleich gemäß § 405 StPO:

1. Die/der Angeklagte zahlt an die Verletzte [Name]
 zur Abgeltung sämtlicher Schmerzensgeld- und Schadens-
 ersatzansprüche aus der Tat vom [Datum] einen Betrag
 von [X Euro].

2. Zahlung erfolgt in monatlichen Raten von [X Euro]
 erstmals zum [Datum]; Gesamtfälligkeit bei Zahlungs-
 verzug mit einer Rate.

3. Mit Zahlung des Gesamtbetrags sind alle Ansprüche der
 Verletzten aus der Tat vom [Datum] abgegolten.

4. Die Gerichtskosten des Adhäsionsverfahrens trägt
 [je nach Vereinbarung].

Dieser Vergleich wird als Prozessvergleich nach § 794 Abs. 1
Nr. 1 ZPO protokolliert.

[Unterschriften beider Seiten und Gericht]
```

### Baustein 3 – Verteidigung: Antrag auf Absehen von Entscheidung § 406 Abs. 1 S. 3 StPO

```
An das [Gericht]
Aktenzeichen: [...]

Antrag auf Absehen von der Entscheidung im Adhäsionsverfahren
gemäß § 406 Abs. 1 S. 3 StPO

In der Strafsache gegen [Name Angeklagte/r]

beantragt die Verteidigung,

von einer Entscheidung über den Adhäsionsantrag der Verletzten
abzusehen, da die Entscheidung eine dem Strafverfahren nicht
angemessene Beweisaufnahme erfordern würde und das Strafver-
fahren wesentlich verzögern würde (§ 406 Abs. 1 S. 5 StPO).

Begründung:
Zur Klärung der Schadenshöhe wäre ein medizinisches Sach-
verständigengutachten einzuholen. Der Adhäsionsantrag bezieht
sich auf Schäden in Höhe von [Betrag EUR]. Die Klärung der
Kausalität zwischen Tat und behaupteten Folgeschäden bedarf
einer umfangreichen medizinischen Beurteilung, die den Rahmen
des Strafprozesses sprengt.

[Ort, Datum]
[Unterschrift Verteidigung]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Anspruchsgrundlage (§ 823 BGB) | Verletzte trägt Tatbegehung, Verletzung, Kausalität; im Adhäsionsverfahren erleichtert durch Bindungswirkung des Strafurteils zur Tat |
| Schadenshöhe (Schmerzensgeld) | Verletzte muss Mindestbetrag darlegen; Gericht schätzt nach § 287 ZPO (analog) |
| Forderungsübergang § 116 SGB X | Sozialleistungsträger zeigt Übergang an; Verletzte muss nur Eigenanteil nachweisen |
| Adhäsionsvergleich | Einigung trägt sich selbst; Vollstreckungstitel durch Protokollierung |
| Absehen wegen Verfahrensverzögerung | Gericht entscheidet von Amts wegen; Verteidigung kann Sachverhalt darlegen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Bis Schluss der Beweisaufnahme | Adhäsionsantrag muss vor Schlussvorträgen gestellt sein | § 404 StPO |
| Ab Urteilszustellung: 1 Woche | Berufung/Revision gegen Adhäsionsausspruch | § 406a StPO |
| Ab Urteilsrechtskraft | Vollstreckung aus Adhäsionsurteil beginnt | § 704, § 794 ZPO |
| 3 Jahre | Verjährung deliktsrechtlicher Ansprüche (§ 195 BGB) ab Kenntnis | § 199 BGB |
| 30 Jahre | Verjährung des titulierten Anspruchs nach § 197 BGB | § 197 BGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Adhäsionsantrag verzögert das Strafverfahren" | § 406 Abs. 1 S. 6 StPO — Absehen nur bei wesentlicher Verzögerung; Schmerzensgeld-Antrag wird durch S. 6 a. F. besonders geschützt; aktuelle Begründungsanforderungen siehe BGH 09.01.2025 — 3 StR 340/24 |
| "Forderungsübergang nach § 116 SGB X schließt Adhäsion aus" | Nur soweit Anspruch übergegangen ist; Eigenbeteiligung (Schmerzensgeld soweit nicht gedeckt) verbleibt bei der Verletzten |
| "Angeklagte/r ist insolvent; Adhäsion sinnlos" | § 302 InsO schließt Restschuldbefreiung bei vorsätzlichen unerlaubten Handlungen aus; Titel hat langfristigen Wert |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Adhäsionsantrag kostenfrei für Verletzte | § 472a StPO: keine Gerichtskosten für Verletzte im Adhäsionsverfahren |
| Anwaltsgebühren (Verletztenvertretung) | VV-RVG Nr. 4143 (Verfahrensgebühr), Nr. 4145 (Terminsgebühr), Nr. 4146 (Vergleichsgebühr); Streitwert = Adhäsionsforderung |
| Bei Beiordnung § 397a StPO | Adhäsionsgebühren zusätzlich zur Nebenklagegebühr aus Staatskasse |
| Angeklagter zahlt Kosten bei Adhäsionsverurteilung | Kosten des Adhäsionsverfahrens als Nebenfolge im Strafurteil |
| Angeklagter bei Vergleich § 405 StPO | Kostenregelung im Vergleich frei vereinbar |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Schneller Vollstreckungstitel gewünscht | Adhäsionsantrag frühzeitig stellen; Vergleich nach § 405 StPO anstreben |
| Angeklagter will Strafmilderung | Schadenswiedergutmachung proaktiv anbieten; § 46a StGB nutzen; Vergleich vor Urteil |
| Hohe Schadensummen in Betrugsfall | Adhäsion kombinieren mit Verbleib im Strafverfahren für Bindungswirkung zur Tatbegehung |
| Angeklagter ist insolvent | Adhäsion trotzdem beantragen; § 302 InsO schließt Restschuldbefreiung aus; Titel 30 Jahre vollstreckbar |
| Gericht neigt zu § 406-Absehen | Beweise vorab vollständig vorlegen; Komplexität minimieren; Schmerzensgeld pauschal schätzen lassen |
| Schmerzensgeldzumessung im Strafurteil | Begründungsanforderungen nach BGH 09.01.2025 — 3 StR 340/24 beachten; Verletzungsbild, Dauer, Folgen erkennbar machen |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-nebenklage-opfervertretung` – Nebenklage und Adhäsion kombiniert führen
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – Adhäsionsforderung in der Insolvenz des Angeklagten
- `plaedoyer-vorbereitung-strafverteidigung` – Schadenswiedergutmachung als Strafmilderungsargument
- `fachanwalt-strafrecht-zeugenbeistand` – Begleitung der Verletzten als Zeugin

---

## Quellen (Stand Mai 2026)

- BGH 09.01.2025 — 3 StR 340/24 (Adhäsion / Schmerzensgeldbegründung): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.01.2025&Aktenzeichen=3+StR+340/24
- BGH 20.11.2025 — 4 StR 232/25 (TOA § 46a StGB, kommunikativer Prozess): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- §§ 403–406c StPO, § 472a StPO: https://dejure.org/gesetze/StPO/403.html
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; weitere Rechtsprechung vor Ausgabe in dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen und Aussage verifizieren.

## 3. `spezial-ermittlungsverfahren-vergleich-eskalation`

**Fokus:** Ermittlungsverfahren: Verhandlung, Vergleich und Eskalation im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

### Ermittlungsverfahren: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Ermittlungsverfahren: Verhandlung, Vergleich und Eskalation
- **Normen-/Quellenanker:** StPO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ermittlungsverfahren** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 4. `spezial-orientierung-fristen-form-und-zuständigkeit`

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

### Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** StPO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## Strafrecht-Orientierung Fristen / Form / Zuständigkeit Bausteine
- **Sachliche Zuständigkeit GVG:**
 - **Strafrichter § 25 GVG:** Privatklagen § 374 StPO; allgemein bis Freiheitsstrafe 2 Jahre, sofern nicht hoeher beantragt.
 - **Schoeffengericht § 28 GVG:** bis Freiheitsstrafe 4 Jahre; alle Strafsachen, die nicht zu hoher Strafkammer oder Strafrichter gehoeren.
 - **Grosse Strafkammer § 76 GVG:** alle Strafsachen ab 4 Jahre erwarteter Freiheitsstrafe; bestimmte Wirtschaftsstrafsachen.
 - **Schwurgericht § 74 II GVG:** Toetungsdelikte §§ 211 ff. StGB, Eingriff in Verkehr mit Todesfolge.
 - **Oberlandesgericht § 120 GVG:** Staatsschutzdelikte (Hochverrat, Landesverrat, Terror).
- **Oertliche Zuständigkeit StPO:**
 - **§ 7 StPO:** Tatort - regelmaessig massgeblich.
 - **§ 8 StPO:** Wohnsitz Beschuldigter.
 - **§ 9 StPO:** Ergreifungsort.
 - **§ 13 StPO:** Verbundene Verfahren.
- **Fristen-Uebersicht (StPO):**
 - **Einspruch Strafbefehl § 410 StPO: 2 Wochen** ab Zustellung.
 - **Berufung § 314 StPO: 1 Woche** ab Verkuendung; Begruendung optional.
 - **Revision § 341 StPO: 1 Woche** Einlegung + § 345 StPO **1 Monat** Begruendung ab Zustellung schriftliche Urteilsausfertigung.
 - **Beschwerde § 311 StPO: 1 Woche** sofortige; § 304 StPO einfache unbefristet.
 - **Wiedereinsetzung § 44 StPO: 1 Woche** ab Wegfall des Hindernisses.
 - **Klageerzwingungsverfahren § 172 II StPO: Antrag 1 Monat** ab Bescheid GenStA.
- **Form-Re-Check:**
 - **Schriftform** zwingend für Rechtsmittel (Berufung, Revision, Beschwerde) und Einspruch.
 - **Unterschrift** Verteidiger / Mandant.
 - **Vollmacht** bei Vertretung.
 - **Begruendungs-Pflicht** Revision (Sach- oder Verfahrensruege; § 344 II StPO Substantiierung Verfahrensruege).
- **Rechtsweg:**
 - AG -> LG (Berufung § 312 StPO) -> OLG (Revision § 333 StPO bei LG-Urteil 1. Instanz oder Berufungsurteil).
 - **Sprungrevision § 335 StPO** moeglich (Sprung Berufung).
 - **Wiederaufnahme § 359 StPO** bei neuen Tatsachen / Beweismitteln.
- **EMRK Art. 6:** angemessene Verfahrensdauer als Korrektiv (Strafmilderung BGH-Linie).

## 5. `strafprozess-aktenlog-fristen-und-wiedervorlagen`

**Fokus:** Aktenlog, Fristenbuch und Wiedervorlagen im Strafverfahren: erstellt aus Eingangspost, beA, EGVP, Verfügung, Ladung, Beschluss, Strafbefehl, Urteil und Aktennachlieferung eine robuste Fristen- und Aufgabensteuerung.

### Aktenlog, Fristen und Wiedervorlagen

## Zweck

Der Skill baut aus jeder Strafakte ein lebendes Register. Er ist besonders wichtig, wenn mehrere Verteidiger, Referendare, Sekretariat und Mandant parallel Informationen liefern.

## Eingang zuerst klassifizieren

| Eingang | Sofort prüfen |
| --- | --- |
| Strafbefehl | Einspruchsfrist § 410 StPO, Beschränkung möglich |
| Urteil | Berufung/Revision, Verkündung, Zustellung, Protokoll |
| Beschluss | einfache oder sofortige Beschwerde, Frist, Statthaftigkeit |
| Ladung | Anwesenheitspflicht, Entschuldigung, Vertretung, Terminskollision |
| Haftbefehl | dringender Tatverdacht, Haftgrund, Verhältnismäßigkeit, § 116 StPO |
| Aktennachlieferung | neue Beweise, neue Zeugen, neue Fristen, Reaktionsbedarf |
| Verfügung StA/Gericht | Stellungnahmefrist, Anhörung, Zuständigkeit |

## Fristen-Register

```text
Fristenregister

Fristart:
Norm:
Auslösendes Ereignis:
Zustellung/Verkündung:
Fristende:
Vorfrist:
Verantwortlich:
Erledigt:
Beleg:
```

## Wiedervorlagen

Lege mindestens an:

- Akteneinsicht nachhalten.
- Nachlieferungen prüfen.
- Mandantenrückmeldung.
- Staatsanwaltschaft/Gericht erinnern.
- Haftprüfung/Haftbeschwerde bewerten.
- HV-Vorbereitung starten.
- Rechtsmittelentscheidung nach Urteil.

## Fehlervermeidung

- Fristbeginn nicht raten: Zustellung, Verkündung, Bekanntgabe und Empfangsbekenntnis trennen.
- Nicht jedes Rechtsmittel ist sofortige Beschwerde; Statthaftigkeit prüfen.
- Revisionsbegründung nicht mit Revisionseinlegung verwechseln.
- Strafbefehl kann beschränkt angegriffen werden, aber Beschränkung muss strategisch sitzen.

## Output

- `Aktenlog`
- `Fristenregister`
- `Wiedervorlagenliste`
- `Rot-Liste heute`
- `Nächste Kanzleihandlung`

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46a StGB
- § 263 StGB
- § 49 StGB
- § 177 StGB
- § 46 StGB
- § 46b StGB
- § 35 BtMG
- § 261 StGB
- § 249 StGB
- § 212 StGB
- § 31 BtMG
- § 240 StGB

### Leitentscheidungen

- EuGH C-610/15
- EuGH C-527/15
- EuGH C-128/11
- EuGH C-145/10
- EuGH C-355/12

