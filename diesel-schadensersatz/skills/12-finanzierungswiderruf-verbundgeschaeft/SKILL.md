---
name: 12-finanzierungswiderruf-verbundgeschaeft
description: "Für Kfz-Kredit, Leasing, Widerruf oder verbundenes Geschäft. Prüft zuerst die Vollerfüllung, dann Originalvertrag, Norm, Muster und Pflichtangabe. Hält Widerrufs- und Herstellerdeliktsspur strikt getrennt."
---

# Finanzierungswiderruf und Verbundgeschäft

## Zweck und Anwendungsfall

Dieser Skill prüft eine eigenständige Angriffsspur beim finanzierten Fahrzeug: Besteht für den konkreten Darlehens- oder Leasingvertrag überhaupt ein gesetzliches oder vertragliches Widerrufsrecht, ist die Widerrufsfrist nach dem bei Vertragsschluss geltenden Recht abgelaufen und liegt ein verbundenes Geschäft nach § 358 BGB vor? Nicht jeder Leasingvertrag ist widerruflich und nicht jeder Fehler hält die Frist offen. Die Spur läuft strikt getrennt vom Deliktsanspruch gegen den Hersteller.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort einen vollständig ausformulierten internen Prüfstand: zuerst den begründeten Vollerfüllungs-Stop, danach Vertragstyp, Originalvollständigkeit, Musterschutz, Pflichtangabe, Frist und Verbund mit Ampel und klarer Freigabe- oder Sperrtendenz. Eine Prüfmatrix wird nur verwendet, wenn mindestens drei Prüfschritte oder wiederkehrende Felder gegenüberzustellen sind. Als konkrete Lücken werden insbesondere Datum und Beleg der letzten Rate, Vertragsnummer, finanzierende Bank sowie fehlende Seiten des Originalvertrags benannt (`[Datum der letzten Rate TT.MM.JJJJ]`, `[Vertragsnummer]`, `[finanzierende Bank]`, `[fehlende Vertragsseite]`); ein Außenprodukt entsteht in der ersten Antwort nie.

Verboten in der ersten Antwort: Theorie-Vorträge zum Widerrufsrecht, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche, mehr als drei Rückfragen sowie jede Rückfrage, wenn ein vorläufiges Ergebnis mit klar markierten Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Fehlt ein Skript oder ein Abgleichswerkzeug, wird ohne Meldungslärm manuell weitergearbeitet; ein Werkzeugfehler blockiert nie die Aktenaufnahme.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Darlehens- oder Leasingvertrag mit vollständiger Widerrufsinformation und Pflichtangaben.
- Kaufvertrag und Nachweis der Vermittlung über den Händler (Verbund-Indiz).
- Zahlungsverlauf aus Skill 02 (Anzahlung, Raten, Schlussrate, Ablösung) einschließlich Beleg, ob beide Seiten den Kreditvertrag vollständig erfüllt haben.

## Ablauf / Checkliste

1. Vertragstyp und Normfassung bestimmen: Allgemein-Verbraucherdarlehen, verbundener Kfz-Kauf, Kilometer- oder Restwertleasing sowie Vertragsschlussdatum getrennt erfassen. Nicht jeder Leasingvertrag vermittelt ein Widerrufsrecht.
2. **Vollerfüllungs-Stop zuerst:** Fälligkeit und Zahlung der letzten Rate, Freigabe von Sicherheiten und sonstige offene gegenseitige Pflichten belegen. Ist der Kreditvertrag vollständig erfüllt, sperren EuGH `C-38/21`, `C-47/21`, `C-232/21` und BGH `XI ZR 162/21` den späteren Widerruf. Dann rote Ampel, Nichtfreigabevermerk und keine Außenproduktion.
3. Nur bei nicht vollständig erfülltem Kredit den Verbund feststellen: Finanzierung durch die herstellernahe Bank, Vermittlung über den Händler und wirtschaftliche Einheit nach § 358 BGB dokumentieren; Markenbezug allein genügt nicht.
4. Vollständige Originalunterlagen sichern. Aus einem isolierten oder nachgebildeten Belehrungsausschnitt wird weder ein Fehler noch fehlender Musterschutz abgeleitet.
5. Widerrufsinformation und Pflichtangaben gegen die bei Vertragsschluss geltenden §§ 355, 356b, 492 und 495 BGB sowie Art. 247 EGBGB prüfen: Normfassung, Muster und Gestaltungshinweise, konkrete Abweichung, Nachholung und Relevanz für Fristlauf und Verbraucherentscheidung jeweils einzeln ausweisen. BGH `XI ZR 258/22` verbietet einen Schlagwortautomatismus.
6. Fristfolge erst danach ableiten: Nur wenn die maßgebliche Vorschrift den konkret festgestellten relevanten Mangel mit fehlendem oder späterem Fristbeginn verknüpft und keine wirksame Nachholung vorliegt, kann ein Widerruf noch offen sein.
7. Rückabwicklung nur bei grüner anwaltlicher Freigabe rechnen: Anzahlung, Raten, Rückgabe, Vorleistung, Nutzungs- oder Wertersatz und Leistungsverweigerungsrechte anhand der konkreten Normfassung; Zahlen aus Skill 02/08 übernehmen.
8. Je nach Befund entweder Nichtfreigabevermerk oder Widerrufsschreiben erzeugen. Ein Außenentwurf nennt nur am vollständigen Originalvertrag verifizierte Abweichungen und wird über Skill 09 beweisfest zugestellt.
9. Spurvergleich bauen: Finanzierungswiderruf und Deliktsanspruch gegen den Hersteller mit eigenen Gegnern, Tatsachen, Fristen und Beweisrisiken getrennt führen. Eine gesperrte Widerrufsspur sagt nichts über die deliktische Betroffenheit.
10. Klageweg nur nach positiver Rechts- und Tatsachenfreigabe an Skill 13 übergeben.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Vertragserfüllung, Normfassung, Pflichtangabe, Musterschutz und Verbundfolge in dieser Reihenfolge prüfen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Ein Widerrufsprodukt ist gesperrt, solange Vollerfüllung, Originalvertrag oder Rechtsfolgenrechnung nicht belastbar geklärt sind.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

- **Anker:** EuGH, Urt. v. 21.12.2023 - verb. Rs. C-38/21, C-47/21 und C-232/21; BGH, Urt. v. 27.02.2024 - XI ZR 258/22; Urt. v. 28.01.2025 - XI ZR 162/21. Vollständige Vertragserfüllung ist das erste Stop-Gate. Nur bei noch nicht vollständig erfülltem Kredit werden Originalvertrag, Normfassung, Musterschutz, konkrete Pflichtangabe und deren Relevanz für den Fristbeginn geprüft; Schlagworte begründen keinen Widerrufsautomatismus. **Status:** Amtlich geprüft.

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

Baustein Widerrufserklärung gegenüber der Bank (nur nach grüner anwaltlicher Freigabe):

„Hiermit widerrufe ich meine auf den Abschluss des Darlehensvertrags vom [Datum TT.MM.JJJJ], Vertragsnummer [Vertragsnummer], gerichtete Willenserklärung. Die Widerrufsfrist ist nicht abgelaufen, weil die Widerrufsinformation des Vertrags von den Anforderungen der bei Vertragsschluss geltenden Fassung der §§ 355, 356b, 492, 495 BGB in Verbindung mit Art. 247 EGBGB abweicht; die konkrete Abweichung besteht darin, dass [am Originalvertrag verifizierte Abweichung]. Die Widerrufsfrist wurde daher nicht in Gang gesetzt; eine wirksame Nachholung liegt nicht vor. Ich fordere Sie auf, den Zugang dieser Erklärung schriftlich zu bestätigen und die Rückabwicklung bis zum [Datum TT.MM.JJJJ] einzuleiten."

Baustein Vortrag zum verbundenen Geschäft:

„Darlehensvertrag und Kaufvertrag bilden ein verbundenes Geschäft im Sinne des § 358 Abs. 3 BGB. Das Darlehen der [finanzierende Bank] diente vollständig der Finanzierung des Kaufpreises für das Fahrzeug mit der FIN [FIN]. Beide Verträge bilden eine wirtschaftliche Einheit, weil sich die Bank bei Vorbereitung und Abschluss des Darlehensvertrags der Mitwirkung des Händlers [Name des Händlers] bediente; Darlehensantrag und Kaufvertrag wurden am [Datum TT.MM.JJJJ] in dessen Geschäftsräumen gemeinsam vorbereitet und unterzeichnet. Der wirksame Widerruf der auf den Darlehensvertrag gerichteten Willenserklärung führt deshalb nach § 358 Abs. 2 BGB dazu, dass die Anspruchstellerin auch an den Kaufvertrag nicht mehr gebunden ist."

Baustein Nichtfreigabevermerk (Vollerfüllungs-Stop):

„Der Darlehensvertrag vom [Datum TT.MM.JJJJ] ist seit dem [Datum TT.MM.JJJJ] von beiden Seiten vollständig erfüllt; die Schlussrate ist gezahlt und die Sicherheiten sind freigegeben (Beleg: Anlage [Nummer]). Ein Widerruf ist nach den amtlich geprüften Ankern EuGH C-38/21, C-47/21 und C-232/21 sowie BGH XI ZR 162/21 ausgeschlossen. Die Widerrufsspur wird daher nicht freigegeben; ein Widerrufsschreiben oder eine Rückabwicklungsklage wird nicht erstellt. Die deliktische Spur gegen den Hersteller bleibt von dieser Sperre unberührt und wird gesondert geprüft."

### Rechenbeispiel Rückabwicklungsrahmen

Nur bei grüner anwaltlicher Freigabe wird gerechnet; der Rahmen sieht so aus:

1 Gezahlte Beträge erfassen

Anzahlung 4.500,00 EUR plus 42 gezahlte Raten zu je 315,00 EUR (42 mal 315,00 EUR gleich 13.230,00 EUR) ergeben Zahlungen der Anspruchstellerin in Höhe von 17.730,00 EUR; eine Schlussrate ist noch nicht fällig.

2 Gegenseitige Rückgewähr einstellen

Die Anspruchstellerin gibt das Fahrzeug an die Bank beziehungsweise nach deren Weisung heraus; ob und in welcher Höhe sie Wertersatz für den Wertverlust und Sollzinsen schuldet und welche Leistungsverweigerungsrechte bestehen, richtet sich nach der bei Vertragsschluss geltenden Normfassung und wird anwaltlich festgelegt, nicht pauschal geschätzt.

3 Ergebnis-Satz

Als vorläufiger Rückabwicklungsrahmen stehen 17.730,00 EUR gezahlte Beträge gegen Herausgabe des Fahrzeugs und einen noch anwaltlich zu beziffernden Wertersatzposten `[Betrag in EUR]`; erst diese Nettozahl trägt die Entscheidung, ob sich die Widerrufsspur wirtschaftlich lohnt.

### Prüftabelle Widerrufsinformation

| Wenn (Befund) | Dann (Rechtsfolge/Pfad) | Begründung | Nächster Schritt |
| --- | --- | --- | --- |
| Kreditvertrag beidseitig vollständig erfüllt | Rote Ampel, Nichtfreigabevermerk, keine Außenproduktion | Vollerfüllung sperrt den späteren Widerruf (C-38/21, C-47/21, C-232/21; XI ZR 162/21) | Rückverweis auf die Deliktsspur (Skill 06) |
| Nur Belehrungsausschnitt oder Vertragskopie in Teilen vorhanden | Gelbe Ampel, Prüfung angehalten | Aus einem isolierten Ausschnitt wird weder ein Fehler noch fehlender Musterschutz abgeleitet | Vollständigen Originalvertrag beschaffen |
| Widerrufsinformation entspricht dem gesetzlichen Muster der maßgeblichen Fassung | Rote Ampel für die Fehlerthese | Musterschutz deckt die Information; Schlagworte begründen keinen Automatismus (XI ZR 258/22) | Nichtfreigabevermerk oder andere Spur |
| Konkrete Pflichtangabe fehlt und die maßgebliche Norm knüpft den Fristbeginn daran, keine wirksame Nachholung | Grün-Kandidat, anwaltliche Freigabe einholen | Nur ein relevanter, fristbezogener Mangel hält den Widerruf offen | Rückabwicklung rechnen, dann Widerrufsschreiben |
| Kein Verbund-Indiz (freie Bank, keine Händlervermittlung) | § 358-Folge entfällt, Widerruf träfe nur den Kredit | Wirtschaftliche Einheit nach § 358 Abs. 3 BGB nicht belegbar; Markenbezug allein genügt nicht | Spurvergleich dokumentieren, Deliktsspur weiter |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Normzitate (§§ 355, 356b, 358, 492, 495 BGB, Art. 247 EGBGB) immer in der bei Vertragsschluss maßgeblichen Fassung prüfen; Widerrufs-Rechtsprechung nur mit Live-Verifikation, keine erfundenen Aktenzeichen. Für Vollerfüllung und Pflichtangaben stehen die amtlich geprüften Anker `C-38/21`, `C-47/21`, `C-232/21`, `XI ZR 258/22` und `XI ZR 162/21` in `references/gepruefte-anker-dieselgate.md`.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Prüfmatrix (Vollerfüllung, Vertragstyp, Originalvollständigkeit, Musterschutz, Pflichtangabe, Relevanz, Frist, Verbund, Rechtsfolge), Spurvergleich und eindeutige Freigabeentscheidung. Bei roter Ampel entsteht ein ausformulierter Nichtfreigabevermerk; nur bei positiver Prüfung ein Widerrufsschreiben. Skelette, erfundene Vertragsklauseln und Halbsätze sind als Endprodukt verboten.

## Beispiele

- Eingang: Tiguan-Finanzierung 2018, Kredit seit 2022 vollständig abgelöst. Kernbefund: Vollerfüllungs-Stop nach `XI ZR 162/21`. Erste Antwort: Prüfmatrix mit roter erster Zeile und vorläufigem, aber vollständig ausformuliertem Nichtfreigabevermerk; als einzige Lücke bleibt der Beleg der beiderseitigen Vollerfüllung, behauptete Pflichtangabenfehler werden nicht weiterverarbeitet.
- Eingang: laufender Kfz-Kredit, Beraterin vermutet eine fehlende Pflichtangabe. Kernbefund: nur Belehrungsausschnitt in der Akte. Erste Antwort: Prüfmatrix mit gelber Ampel, Lückenliste `[vollständiger Originalvertrag]` und Prüfpfad nach `XI ZR 258/22` ohne vorschnelle Fehlerthese.
- Eingang: Kilometerleasing über eine freie Bank ohne Händlervermittlung. Kernbefund: kein Verbund nach § 358 Abs. 3 BGB, Widerruflichkeit fraglich. Erste Antwort: Prüfmatrix mit verneinter Verbundzeile und dokumentiertem Rückverweis auf die Deliktsspur an Skill 06.
- Eingang: Bank beruft sich vorgerichtlich auf Verwirkung. Kernbefund: Einwand betrifft die Durchsetzung, nicht die Matrixprüfung. Erste Antwort: aktualisierte Prüfmatrix mit offen bewertetem Verwirkungsrisiko und anwaltlicher Eskalation für die Klageentscheidung.
