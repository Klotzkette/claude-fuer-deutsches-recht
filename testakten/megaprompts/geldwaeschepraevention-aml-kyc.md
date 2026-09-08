# Vollprüfung: geldwaeschepraevention-aml-kyc

## Zusammensetzung

Diese Vollprüfung enthält alle 20 Skills des Plugins `geldwaeschepraevention-aml-kyc`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Startet Geldwäscheprüfungen in Kanzlei, Notariat und Unternehmen aus vorhandenen Unterlagen. Wählt zwischen Verpflichtet…
2. **geldwaesche-schulung-awareness** — Plant rollenbezogene Geldwäscheschulungen und kontrolliert deren praktische Wirksamkeit. Nutzt getrennte Fallunterlagen …
3. **geldwaesche-kyc-onboarding** — Bearbeitet die Aufnahme oder Aktualisierung einer konkreten Kundenbeziehung: Identität, Vertretung, Geschäftszweck und f…
4. **geldwaesche-ubo-wirtschaftlich-berechtigte** — Entwirrt Beteiligungs- und Kontrollketten für die Feststellung wirtschaftlich Berechtigter. Prüft Stimmrechte, Treuhand …
5. **kanzleimandat-und-berufsgeheimnis** — Prüft Geldwäschepflichten bei anwaltlichem Mandatswechsel, Fremdgeld und Transaktionsberatung. Ordnet Informationen dem …
6. **geldwaesche-gruppenweite-compliance** — Prüft gruppenweite Geldwäschekontrollen und ausgelagerte Kundenprüfung. Ordnet Mutterunternehmen, Tochter, Kanzleinetzwe…
7. **geldwaesche-immobilien-gueterhaendler** — Prüft Schwellen und Zahlungswege bei Güterhandel, Kunstgeschaeften und Immobilienvermittlung. Unterscheidet Barzahlung, …
8. **interne-kontrollen-und-beauftragter** — Setzt konkrete Geldwäscherisiken in interne Kontrollen, Zuständigkeiten und Vertretungen um. Prüft Bestellungspflichten …
9. **notariat-immobilienzahlung-pruefen** — Prüft im Notariat Kaufpreisnachweise, Drittzahlungen und Eigentumsumschreibung nach GwG Paragraf 16a. Verbindet Beurkund…
10. **geldwaesche-risikoanalyse-unternehmen** — Erstellt oder aktualisiert eine betriebsbezogene GwG-Risikoanalyse aus Kundenmix, Leistungen, Zahlungswegen und Kontroll…
11. **geldwaesche-krypto-zahlungsdienstleister** — Ordnet Kryptotransfers und Zahlungsdienstleister nach Rolle, Transferdaten und selbst gehosteter Adresse ein. Trennt Tra…
12. **aml-verdachtsmeldung-fiu-leitfaden** — Prüft konkrete Verdachtstatsachen nach GwG Paragraf 43 und erstellt einen FIU-Meldeentwurf nach der seit März 2026 gelte…
13. **geldwaesche-transaktionsmonitoring** — Untersucht auffällige Zahlungen, Teilbeträge, Rückerstattungen und Warenströme im Vergleich zum Kundenprofil. Verknüpft …
14. **eu-geldwaescherecht-umstellung-2027** — Bereitet Kanzlei, Unternehmen und Notariat auf das EU-Geldwäschepaket vor. Trennt geltendes GwG und Meldeformat 2026 von…
15. **geldwaesche-behoerdenverfahren** — Bearbeitet Aufsichtsanfragen, Prüfungsfeststellungen und Bußgeldvorwürfe zum GwG. Trennt Mitwirkung, geschützte Informat…
16. **geldwaesche-verpflichteten-check** — Klärt den GwG-Verpflichtetenstatus für ein konkretes Mandat oder Geschäft. Trennt anwaltliche Katalogtätigkeit, Notariat…
17. **geldwaesche-pep-hochrisikoland-risikoanalyse** — Prüft PEP-Merkmale und Hochrisikostaaten anhand von Amt, Beziehung, Zeitraum und aktueller Quelle. Leitet passende verst…
18. **geldwaesche-transaktionsstopp-freeze** — Berechnet die Nichtdurchführung nach einer FIU-Meldung und die besondere notarielle Wartefrist. Trennt GwG-Aufschub, San…
19. **geldwaesche-transparenzregister** — Gleicht wirtschaftlich Berechtigte mit dem Transparenzregister ab. Trennt eigene Mitteilung, Unstimmigkeitsmeldung und F…
20. **geldwaesche-sanktionsscreening** — Bearbeitet konkrete Sanktionsnamens- und Kontrolltreffer. Prüft Identität, Eigentum, Rechtsakt und Bereitstellungsverbot…

---

## Skill: `einstieg-routing`

_Startet Geldwäscheprüfungen in Kanzlei, Notariat und Unternehmen aus vorhandenen Unterlagen. Wählt zwischen Verpflichtetenstatus, Kundenprüfung, Immobilienzahlung und akutem Meldefall, ohne einen allgemeinen Fragebogen vorzuschalten._

# 1. Geldwäschevorgang aufnehmen

## 1. Zweck und Anwendungsfall

Für einen neuen Ordner, Zahlungsalarm oder eine knappe Frage zur Prävention. Ein ausdrücklich verlangter Meldeentwurf beginnt unmittelbar im Meldeskill; dieser Einstieg ist keine Pflichtschleife.

## 2. Eingaben

Auftrag, jüngste Zahlungsnachricht und nötige Mandats- oder Kundendaten lesen. Höchstens fünf tragende Dateien im ersten Durchgang, bei Eigentumsketten gezielt Zwischenstufen ergänzen. Ohne Auftrag mit rechtlicher Rolle und nächster erkennbarer Handlung beginnen. Ohne verwertbares Material höchstens eine gebündelte Rückfrage zu Geschäft und Zeitpunkt.

## 3. Ablauf

### 3.1. Handlungsdruck erkennen

Eine heute anstehende Auszahlung, Grundbucheinreichung oder Meldung vor Organisationsarbeit behandeln. Zeitpunkt und Bearbeiter aus der Akte übernehmen. Fehlender Registerzugang bedeutet eine Nachforderung, nicht automatisch einen Verdacht.

### 3.2. Einen Fachweg wählen

| Eingang | Nächster Skill | Erstes Ergebnis |
| --- | --- | --- |
| Unklarer Verpflichteter | [Verpflichtetencheck](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/geldwaesche-verpflichteten-check/SKILL.md) | Begrenzter Pflichtenumfang |
| Beratungswissen oder Fremdgeld | [Kanzleimandat](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/kanzleimandat-und-berufsgeheimnis/SKILL.md) | Informations- und Rollenabgrenzung |
| Kaufpreis oder Umschreibung | [Notarielle Zahlung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/notariat-immobilienzahlung-pruefen/SKILL.md) | Nachweis und Vollzugsstand |
| Neue Geschäftsbeziehung | [KYC](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/geldwaesche-kyc-onboarding/SKILL.md) | Entscheidende Nachforderung |
| Verdachtstatsachen | [FIU-Meldeprüfung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/aml-verdachtsmeldung-fiu-leitfaden/SKILL.md) | Tatsachenkern und Meldeentscheidung |
| Bereits abgegangene Meldung | [Nichtdurchführung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/geldwaesche-transaktionsstopp-freeze/SKILL.md) | Frist und andere Hindernisse |
| Vorbereitung auf 2027 | [EU-Umstellung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/eu-geldwaescherecht-umstellung-2027/SKILL.md) | Datierter Änderungsplan |

Nur den einen passenden Fachskill und seine benötigte Referenz laden. Anschlussfragen dort bearbeiten, nicht erneut den Eingang durchlaufen.

### 3.3. Technischen Ausfall auffangen

Vorhandenen Auszug samt Datum nutzen; aktuelle Abfrage als Lücke notieren. Ohne Export ausformulierten Text liefern. Nach einem erfolglosen Alternativabruf nicht endlos wiederholen. Keine simulierte Freigabe oder erfundene goAML-Bestätigung.

## 4. Quellenpflicht

[Rechtsstand und Grenzen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md): GwG Paragraf 2, Paragraf 43 und Paragraf 46 sind unterschiedliche Weichen. Den Stichtag 10. Juli 2027 nicht vorziehen.

## 5. Ausgabeformat

Verlangtes Arbeitsprodukt in vollständigen Sätzen; ohne Formatwunsch kurzer Vermerk mit Vorgang, Handlung, Beleg und entscheidender Lücke. Times New Roman 11 pt, dezimale Gliederung. Kein vorgelagertes Inhaltsverzeichnis aller Skills.

## 6. Beispiele

„Verkäufer bestätigt Eingang, heute einreichen?“ führt zur notariellen Zahlungsprüfung. Ein Rückzahlungswunsch auf ein fremdes Konto führt zum Zahlungsbefund und gegebenenfalls zur Meldeprüfung, nicht zur Schulungsplanung.

---

## Skill: `geldwaesche-schulung-awareness`

_Plant rollenbezogene Geldwäscheschulungen und kontrolliert deren praktische Wirksamkeit. Nutzt getrennte Fallunterlagen für Empfang, Buchhaltung, Kanzlei und Notariat und dokumentiert Nachschulung und Kontrollbefunde ohne reale Meldungen aus Trainingsdaten._

# 1. Schulung und Wirksamkeitsprüfung

## 1. Zweck und Anwendungsfall

Für Mitarbeiterunterrichtung, Einführung neuer Abläufe und gezielte Kontrolle erkannter Schwächen. Nicht bei jedem Kundenfall automatisch aktivieren.

## 2. Eingaben

Rolle, konkrete Tätigkeit, letzte Schulung, beobachtete Fehler und vorhandene Arbeitsanweisung. Eine kurze Buchhaltungsunterrichtung braucht andere Fälle als ein Notariatstermin.

## 3. Ablauf

### 3.1. Tätigkeitsnahe Auswahl

Empfang: Identitätsunterlagen weiterleiten, keine Identifizierung vortäuschen. Buchhaltung: abweichenden Zahler und Rückzahlungsempfänger erkennen. Notariat: Zahlungsschlüssigkeit und Vollzugsstand auseinanderhalten. Berufsträger: Informationsschutz und unverzügliche Meldeprüfung. Nur einschlägige Fallunterlagen öffnen.

### 3.2. Schulung sicher abgrenzen

Schulungsauftrag ausdrücklich feststellen und Unterlagen getrennt von echten Mandaten halten. Keine reale Registermitteilung oder FIU-Meldung aus einem Übungsfall erzeugen oder absenden. Teilnehmerunterlagen enthalten Tatsachen, nicht vorab die Lösung. Besprechung nur auf ausdrücklichen Auswertungsauftrag.

### 3.3. Wirksamkeit beobachten

Teilnehmer soll den richtigen nächsten Schritt und fehlenden Beleg nennen können. Stichprobe echter Prozessnachweise nur bei entsprechender Berechtigung und mit erforderlicher Begrenzung. Befund, betroffene Kontrolle, Korrektur und Nachkontrolle dokumentieren; Teilnahme allein beweist keine wirksame Umsetzung.

### 3.4. Anlass zur Wiederholung

GwG Paragraf 6 Absatz 2 Nummer 6 und gegebenenfalls Nummer 7 zugrunde legen. Änderungen, neue Aufgaben und Fehlbefunde bestimmen den Schulungsbedarf; eine gesetzliche universelle Jahresfrequenz nicht erfinden.

## 4. Quellenpflicht

GwG Paragraf 6, Aufsichtsvorgaben und [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Den Unterschied zwischen GwGMeldV seit März 2026 und AMLR ab Juli 2027 ausdrücklich üben.

## 5. Ausgabeformat

Ausformulierter Ablauf mit konkretem Fall, Lernfrage, Verantwortlichem und Nachweis; Kontrollbericht mit festgestelltem Verhalten, nicht nur Häkchen. Times New Roman 11 pt, dezimale Gliederung.

## 6. Beispiele

Ein Mitarbeiter kennt die Meldefrist, aber der befugte Vertreter fehlt. Die Nachschulung wird um einen tatsächlichen Vertretungs- und Zugriffscheck ergänzt statt nur dieselben Folien erneut zu versenden.

---

## Skill: `geldwaesche-kyc-onboarding`

_Bearbeitet die Aufnahme oder Aktualisierung einer konkreten Kundenbeziehung: Identität, Vertretung, Geschäftszweck und fehlende Nachweise. Liefert gezielte Nachforderung und dokumentierten Bearbeitungsstand statt einer unbelegten KYC-Freigabe._

# 1. Kundenprüfung bis zum belegten Stand

## 1. Zweck und Anwendungsfall

Für neue Kunden, neue Mandate im erfassten Tätigkeitsbereich und maßgebliche Änderungen bestehender Beziehungen. Voraussetzung ist ein geklärter Verpflichtetenstatus; ein Routineaktualisierungswunsch startet nicht die gesamte Unternehmensanalyse.

## 2. Eingaben

Kundenbogen, Ausweisdaten, Registerauszug, Vertretungsnachweis und konkretes Geschäft lesen. Herkunft und Aktualität jedes Nachweises festhalten. Ausweisnummern nicht in unnötigen Berichten wiederholen.

## 3. Ablauf

### 3.1. Erheben und überprüfen

Vertragspartner, auftretende Person und Vertretungsmacht auseinanderhalten. Nach GwG Paragrafen 11 bis 13 unterscheiden, welche Angaben vorliegen und durch welches zulässige Verfahren sie überprüft wurden. Keine Identität allein aus einem unscharfen Ausweisfoto bestätigen. Bei Gesellschaften Name, Rechtsform, Sitz, Register und gesetzliche Vertreter abgleichen.

### 3.2. Zweck und Eigentümer klären

Art und Zweck der Geschäftsbeziehung aus Auftrag oder Vertrag übernehmen. Wirtschaftlich Berechtigte über den [Eigentümer-Skill](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/geldwaesche-ubo-wirtschaftlich-berechtigte/SKILL.md) ermitteln, wenn die Struktur nicht bereits nachvollziehbar dokumentiert ist. PEP- und Risikoprüfung anhand konkreter Person und Geschäft, nicht nach Staatsangehörigkeit pauschalisieren.

### 3.3. Lücke mit Rechtsfolge verbinden

Je fehlendem Beleg benennen, welche Pflicht nicht erfüllt werden kann. GwG Paragraf 10 Absatz 9 mit Rechtsberatungsausnahme und notariellen Sonderregeln prüfen. Eine fehlende Information ist nicht automatisch ein meldepflichtiger Verdacht; Tatsachen im Sinne des Paragraf 43 gesondert bewerten. Nur notwendige Angaben nachfordern, keine pauschale lebenslange Kontohistorie.

### 3.4. Aktualisierung statt Neustart

Geänderten Geschäftsführer, neue Beteiligung oder abweichendes Zahlungsprofil gezielt nachziehen. Vorhandene unveränderte Belege wiederverwenden, ihre Eignung prüfen und den nächsten risikobasierten Überprüfungsanlass festlegen.

## 4. Quellenpflicht

GwG Paragraf 10 bis Paragraf 15 und [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Eine Bankrichtlinie nicht ungeprüft als gesetzliche Pflicht einer Kanzlei behandeln.

## 5. Ausgabeformat

Ausformulierter Nachforderungsbrief und interne Feststellung mit überprüftem Punkt, Beleg, Restlücke und zuständiger Entscheidung. Times New Roman 11 pt, dezimale Gliederung. Nicht „identifiziert“ schreiben, wenn nur Daten erhoben wurden.

## 6. Beispiele

Ein neuer Geschäftsführer ist im aktuellen Register verzeichnet, aber der auftretende Einkäufer hat keine Vollmacht. Die Nachforderung betrifft die Vertretung; Eigentümerdaten nur bei einem Änderungsanlass erneut beschaffen.

---

## Skill: `geldwaesche-ubo-wirtschaftlich-berechtigte`

_Entwirrt Beteiligungs- und Kontrollketten für die Feststellung wirtschaftlich Berechtigter. Prüft Stimmrechte, Treuhand und beherrschenden Einfluss und trennt den heutigen GwG-Test von der ab 2027 vorgesehenen Eigentumsberechnung._

# 1. Wirtschaftlich Berechtigte ermitteln

## 1. Zweck und Anwendungsfall

Für mehrstufige Gesellschaften, Treuhand, Stimmrechtsbindungen und widersprüchliche Registerangaben. Nicht bloß die Gesellschafterliste abschreiben.

## 2. Eingaben

Aktuelle Beteiligungsliste, Satzung, Stimmrechtsvereinbarungen und Angaben zu zwischengeschalteten Einheiten. Prozente, Stichtag und Beleg je Kante übernehmen. Ausländische Rechtsformen nicht ohne Prüfung mit einer deutschen GmbH gleichsetzen.

## 3. Ablauf

### 3.1. Kette darstellen

Eine Tabelle mit Beteiligtem, Zielgesellschaft, Kapital, Stimmen, Sonderrechten und Fundstelle erstellen. Darunter ein lesbares Baumdiagramm als Text, das dieselben Beziehungen zeigt. Unbekannte Zwischenstufen ausdrücklich offen lassen; keine grafisch geschlossene Kette erfinden.

### 3.2. Heutigen Maßstab anwenden

GwG Paragraf 3 Absatz 2: mehr als 25 Prozent Kapital oder Stimmen sowie vergleichbare Kontrolle prüfen. Bei mittelbarer Kontrolle beherrschenden Einfluss und den Verweis auf HGB Paragraf 290 Absatz 2 bis 4 beachten. Eine Rechnung „60 Prozent mal 40 Prozent gleich 24 Prozent, deshalb kein wirtschaftlich Berechtigter“ ist kein vollständiger Kontrolltest. Treuhand und Handeln auf Veranlassung zusätzlich berücksichtigen.

### 3.3. Ersatzperson nicht vorschnell einsetzen

Gesetzlicher Vertreter als wirtschaftlich Berechtigter erst nach umfassender erfolgloser Prüfung und den gesetzlichen Voraussetzungen, insbesondere ohne Tatsachen nach Paragraf 43 Absatz 1. Dokumentiere die untersuchten Wege. Eine verweigerte Eigentümerauskunft nicht durch Eintragung des Geschäftsführers neutralisieren.

### 3.4. Zukunftsvergleich getrennt rechnen

Nur bei Umstellungsauftrag zusätzlich Verordnung (EU) 2024/1624 Artikel 51 bis 54 anwenden: grundsätzlich 25 Prozent oder mehr nach Artikel 52 und zusätzliche Kontrolle. Eigentumsquoten und Kontrolltest getrennt ausweisen. Spalte „ab 10. Juli 2027“ nicht zur heutigen Kundenentscheidung machen.

## 4. Quellenpflicht

[GwG Paragraf 3](https://www.gesetze-im-internet.de/gwg_2017/__3.html) und [EU-Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Registerzugangsrechtsprechung C-37/20 und C-601/20 hebt diese Ermittlungspflichten nicht auf.

## 5. Ausgabeformat

Begründeter Eigentümervermerk mit nachvollziehbarer Kette und einer gezielten Nachforderung je offener Kontrollstufe. Vollständige Sätze, Times New Roman 11 pt, dezimale Gliederung. Keine alleinige Namensliste ohne Herleitung.

## 6. Beispiele

Vier Gesellschafter zu je 25 Prozent ohne Sonderrechte: heutigen Schwellen- und Kontrolltest prüfen; für 2027 den geänderten Eigentumsmaßstab gesondert zeigen. Ein Stimmbindungsvertrag kann die heutige Einordnung verändern.

---

## Skill: `kanzleimandat-und-berufsgeheimnis`

_Prüft Geldwäschepflichten bei anwaltlichem Mandatswechsel, Fremdgeld und Transaktionsberatung. Ordnet Informationen dem Beratungs- oder Abwicklungsauftrag zu und grenzt Meldepflicht, Berufsgeheimnis und zulässige Kommunikation ab._

# 1. Kanzleimandat und geschützte Informationen

## 1. Zweck und Anwendungsfall

Beratungswissen, Prozessvertretung und Geschäftsdurchführung auseinanderhalten. Weder sämtliche Kanzleiinformationen für geschützt noch für meldepflichtig erklären.

## 2. Eingaben

Mandat, Auftragserweiterung, Zahlungsinstruktion und Informationsherkunft lesen. Ein Anderkontoauszug erklärt weder Zweck noch GwG-Rolle. Mandantenauskünfte nicht zu bewiesenen Tatsachen umformulieren.

## 3. Ablauf

### 3.1. Auftrag und Wissen zeitlich trennen

Für jede Information Zeitpunkt, Absender und Auftrag festhalten. GwG Paragraf 2 Absatz 1 Nummer 10 tätigkeitsbezogen anwenden. Ein Transaktionsauftrag macht nicht jedes frühere Verteidigungsgespräch weitergebbar; die Bezeichnung „Beratung“ schützt umgekehrt nicht jede Abwicklung.

### 3.2. Ausnahmen einzeln anwenden

Paragraf 43 Absatz 2 regelt die Meldeausnahme mit Rückausnahmen. Paragraf 10 Absatz 9 regelt die Folgen unerfüllbarer Sorgfaltspflichten mit eigener Rechtsberatungsausnahme. Kenntnis von missbräuchlicher Nutzung und Immobilienfälle nach Paragraf 43 Absatz 6 konkret behandeln. Geschützte Passagen isolieren und anwaltliche Prüfung veranlassen, ohne unverzügliche Meldungen unbestimmt aufzuschieben.

### 3.3. Fremdgeld plausibilisieren

Auftrag, Rechtsgrund, Einzahler, wirtschaftlich Berechtigter, Empfänger und Auszahlungsvoraussetzung vergleichen. Drittkontowünsche anhand Originalnachricht und Beleg prüfen. Keine Auszahlung allein deshalb, weil Geld bereits eingegangen ist. Berufsrechtliche Grenzen zusätzlich beachten; Sammelanderkonten weder pauschal verbieten noch von KYC freistellen.

### 3.4. Empfänger begrenzen

Vor Nachforderung prüfen, ob sie eine beabsichtigte Meldung offenlegt. Paragraf 47 und Ausnahmen adressatenbezogen anwenden. Intern nur erforderliche Informationen an befugte Empfänger, kein Rundschreiben an sämtliche Beteiligte.

## 4. Quellenpflicht

[Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md), GwG Paragraf 43 Absatz 2, Paragraf 10 Absatz 9, Paragraf 47. EuGH C-305/05 vom 26. Juni 2007 nur als Hintergrund zu Transaktionspflichten und Verfahrensschutz verwenden, nicht als heutige Generalausnahme.

## 5. Ausgabeformat

Ausformulierter interner Vermerk mit Informationszuordnung und nächstem zulässigen Schritt. Mandantenbrief getrennt und ohne Hinweis auf beabsichtigte Meldung, soweit keine gesetzliche Ausnahme greift. Times New Roman 11 pt, dezimale Gliederung.

## 6. Beispiele

Ein zunächst beklagter Unternehmer verlangt später die Abwicklung eines Anteilskaufs über Fremdgeld. Beide Aufträge getrennt prüfen, statt die ganze Prozessakte zu melden oder sämtliche Zahlungsbefunde zu verbergen.

---

## Skill: `geldwaesche-gruppenweite-compliance`

_Prüft gruppenweite Geldwäschekontrollen und ausgelagerte Kundenprüfung. Ordnet Mutterunternehmen, Tochter, Kanzleinetzwerk und Dienstleister getrennt ein und klärt Datenzugriff, Verantwortung und verbotene Informationsweitergabe._

# 1. Gruppe und Auslagerung steuern

## 1. Zweck und Anwendungsfall

Für zentrale KYC-Dienste, Tochtergesellschaften und grenzüberschreitende Netzwerke. Gemeinsame Marke ist nicht automatisch gesetzliche Gruppe; Dienstleistereinsatz beseitigt keine Verantwortung.

## 2. Eingaben

Gruppenstruktur, jeweilige Tätigkeiten und Rechtsräume, Leistungsvereinbarung, Zugriffskonzept und lokale Einschränkungen. Nicht bloß den Konzernnamen als Rechtsgrund übernehmen.

## 3. Ablauf

### 3.1. Anwendungsbereich

GwG Paragraf 9 einschließlich Mutterunternehmens- und Untergruppenregeln auf die tatsächlichen Einheiten anwenden. Berufsnetzwerk anhand gesetzlicher Merkmale prüfen. Finanz- und Nichtfinanzunternehmen nicht gleichsetzen.

### 3.2. Durchführung zuweisen

Paragraf 17: zulässige Durchführung durch Dritte, vertragliche Auslagerung und bloße technische Unterstützung unterscheiden. Verantwortlichkeit, sofortige Verfügbarkeit erforderlicher Informationen, Kontrollrecht und Nachweise regeln. Eine Bestätigung „KYC erledigt“ ersetzt nicht die gesetzlich erforderliche Verfügbarkeit.

### 3.3. Informationsgrenzen

Bei Verdachtsmeldungen GwG Paragraf 47 Absatz 2 nach Empfängerkategorie und Voraussetzungen prüfen. Kein pauschales weltweites Teilen der Mandatsakte. Drittstaatliche Hindernisse konkret benennen und zulässige zusätzliche Maßnahmen beziehungsweise Eskalation nach Paragraf 9 prüfen.

### 3.4. Änderungen vorbereiten

Künftige EU-Vorgaben, AMLA-Konsultationen und geltende Pflichten getrennt dokumentieren. Ein Entwurf zur Gruppenstruktur oder zu Sammelanderkonten ist noch kein geltendes Verbot.

## 4. Quellenpflicht

GwG Paragraf 9, Paragraf 17, Paragraf 47 und [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Berufsspezifische Aufsichtshinweise nicht durch allgemeine Bankstandards ersetzen.

## 5. Ausgabeformat

Ausformulierte Verantwortungs- und Zugriffsvorlage mit Einheit, Pflicht, Information, zulässigem Empfänger und Kontrollnachweis. Times New Roman 11 pt, dezimale Gliederung.

## 6. Beispiele

Eine Auslandsgesellschaft führt Kundenprüfung durch, kann aber Belege nicht rechtzeitig bereitstellen. Der Skill dokumentiert die konkrete Durchführungs- und Zugriffslücke statt eine pauschale Outsourcing-Freigabe zu erteilen.

---

## Skill: `geldwaesche-immobilien-gueterhaendler`

_Prüft Schwellen und Zahlungswege bei Güterhandel, Kunstgeschaeften und Immobilienvermittlung. Unterscheidet Barzahlung, verbundene Teilbeträge und Verdachtsanlass und vermeidet die Vermischung mit notariellen Kaufpreisnachweisen._

# 1. Händler- und Vermittlergeschäft prüfen

## 1. Zweck und Anwendungsfall

Für Unternehmen mit Güterhandel oder Immobilienvermittlung. Notarielle Umschreibung zum [Notariatsskill](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/notariat-immobilienzahlung-pruefen/SKILL.md) geben; Immobilienmakler und Notar haben nicht dieselben Pflichten.

## 2. Eingaben

Ware oder vermitteltes Geschäft, Einzel- und Teilbeträge, Zahlungsart, Parteien und Geschäftsbezug. Kaufpreis, Nettokaltmiete und Baranteil nicht als dieselbe Rechengröße verwenden.

## 3. Ablauf

### 3.1. Tätigkeitsart bestimmen

Güterhändler nach GwG Paragraf 2 Absatz 1 Nummer 16, Immobilienmakler nach Nummer 14 einordnen. Bei Kunsthandel und hochwertigen Gütern die konkrete Warenkategorie nach Paragraf 1 prüfen. Eine teure Maschine ist nicht deshalb ein Edelmetallgeschäft.

### 3.2. Schwellen berechnen

Paragraf 10 Absatz 6a: Kunstgeschäfte ab 10000 Euro; Edelmetallgeschäfte der dort bezeichneten Kategorie bei Barzahlungen ab 2000 Euro; sonstige Güter bei Barzahlungen ab 10000 Euro. Verbundene Teilvorgänge und Zahlungen Dritter mit betrachten. Bei Immobilienvermittlung Kaufgeschäft und Miet-/Pachtgeschäft mit mindestens 10000 Euro monatlicher Nettokaltmiete oder -pacht nach Absatz 6 unterscheiden.

### 3.3. Verdacht nicht wegschwellen

Verdachtstatsachen und Identitätszweifel nach Paragraf 10 Absatz 3 sowie Paragraf 43 unabhängig von betragsbezogenen Erleichterungen prüfen. Barausschluss in der Unternehmensrichtlinie und tatsächliche Kassenpraxis vergleichen. Kassenbestand, Vertragsnummer und Quittung sind wichtiger als eine bloße Zusicherung „nie Bargeld“.

### 3.4. Zukunftsrecht nicht vorziehen

Artikel 80 der Verordnung (EU) 2024/1624 begrenzt grundsätzlich ab 10. Juli 2027 bestimmte Barzahlungen auf maximal 10000 Euro. Heutige Identifizierungsschwelle und künftiges Verbot sind verschiedene Fragen. Strengere nationale Regeln und Ausnahmen gesondert prüfen.

## 4. Quellenpflicht

[GwG Paragraf 10](https://www.gesetze-im-internet.de/gwg_2017/__10.html), Paragraf 1 Absatz 5 und [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md).

## 5. Ausgabeformat

Ausformulierter Geschäftsvermerk mit Teilbetragsrechnung, Schwelle, Pflichten und Zahlungsentscheidung. Times New Roman 11 pt, dezimale Gliederung. Zahlen als Tabelle mit Quelle und Datum ausgeben.

## 6. Beispiele

Drei Baranzahlungen von 4000, 3500 und 3000 Euro für dieselbe Maschine ergeben 10500 Euro. Nicht drei getrennte Unterschwellenfälle annehmen; daneben abweichenden Zahler anhand der Akte klären.

---

## Skill: `interne-kontrollen-und-beauftragter`

_Setzt konkrete Geldwäscherisiken in interne Kontrollen, Zuständigkeiten und Vertretungen um. Prüft Bestellungspflichten und Aufsichtsanordnungen und entwickelt einen funktionsfähigen Meldeweg auch bei Urlaub oder Systemausfall._

# 1. Kontrollen und Verantwortlichkeit einrichten

## 1. Zweck und Anwendungsfall

Für Betrieb, Kanzlei oder Notariat, deren Analyse konkrete organisatorische Lücken zeigt. Keine Ernennung eines Beauftragten allein aufgrund der Unternehmensgröße erfinden.

## 2. Eingaben

Risikoanalyse, Personal- und Berechtigungsübersicht, bestehende Anweisungen, Aufsichtsanordnung und Vertretungsplan. Tatsächliche Funktionen statt bloßer Organigrammtitel erfassen.

## 3. Ablauf

### 3.1. Rechtsgrund der Organisation

GwG Paragraf 6 regelt interne Sicherungsmaßnahmen, Paragraf 7 den Geldwäschebeauftragten. Gesetzliche Kategorie, etwaige Befreiung und besondere Anordnung prüfen. Ein Betrieb ohne Bestellungspflicht benötigt gleichwohl Verantwortlichkeit für seine tatsächlich bestehenden Pflichten.

### 3.2. Kontrolle ausführbar beschreiben

Auslöser, Bearbeiter, Beleg, Entscheidungsbefugnis und Vertretung je Kontrolle festlegen. Beispiel: Abweichender Rückzahlungsempfänger führt zur dokumentierten Zahlungsprüfung vor Auszahlung. Vier Augen dort einsetzen, wo geboten; nicht jede Routineprüfung in eine endlose Freigabekette verwandeln.

### 3.3. Ausfallweg durchspielen

Vertreter muss Unterlagen und befugten Meldeweg erreichen können. Unverzügliche Meldung darf nicht auf die Rückkehr des Partners warten. Zugriffsprotokoll und vorhandenen Stand sichern; bei goAML-Störung amtlich vorgesehenen Ersatzweg prüfen. Technische Unterstützung erhält nicht automatisch Einsicht in geschützte Mandatsinhalte.

### 3.4. Dokumentation und Schulung

Paragraf 8 mit Fristbeginn, zulässiger Aufbewahrung und Löschentscheidung umsetzen. Beschäftigte funktionsbezogen unterrichten, Änderungen und Wirksamkeit nachhalten. Keine pauschale Pflicht zur jährlichen Vollschulung aus Paragraf 6 herauslesen.

## 4. Quellenpflicht

GwG Paragrafen 6 bis 8 und zuständige Kammer- oder Landesanordnungen; [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Für Auslagerung ergänzend Paragraf 17, für Gruppe Paragraf 9.

## 5. Ausgabeformat

Ausformulierte Arbeitsanweisung mit Verantwortlichem und Vertretung sowie beschlussfähige Bestellung nur bei geklärter Grundlage. Times New Roman 11 pt, dezimale Gliederung. Nicht bloß „Kontrollen implementieren“ schreiben.

## 6. Beispiele

Einziger Meldeberechtigter ist im Urlaub, die Buchhaltung entdeckt einen eiligen Zahlungsbefund. Die Anweisung benennt befugten Vertreter, Zugang und Nachweis statt „Geschäftsleitung informieren und abwarten“.

---

## Skill: `notariat-immobilienzahlung-pruefen`

_Prüft im Notariat Kaufpreisnachweise, Drittzahlungen und Eigentumsumschreibung nach GwG Paragraf 16a. Verbindet Beurkundungshindernisse, Immobilien-Meldetatbestände und besondere Wartefrist mit einer konkreten Vollzugsvorlage._

# 1. Immobilienzahlung und notarieller Vollzug

## 1. Zweck und Anwendungsfall

Für unvollständige Kaufpreisbelege, Drittzahlungen oder bevorstehende Grundbucheinreichung. Mitarbeiter bereiten vor; der Notar entscheidet rechtlich über den Vollzug.

## 2. Eingaben

Urkunde, Fälligkeit, Kaufpreisanpassung, Zahlungsbelege, Verkäufererklärung und Beteiligtenstruktur lesen. Zahlungsart, Zahler, Empfänger, Betrag, Buchungsdatum und Rest aus den Belegen übernehmen.

## 3. Ablauf

### 3.1. Beurkundung und Vollzug trennen

Bei Gesellschaften Eigentums- und Kontrollstruktur nach GwG Paragraf 12 Absatz 4 sowie gegebenenfalls ausländische Registerpflichten prüfen. Beurkundungshindernis nach Paragraf 10 Absatz 9 und spätere Zahlungsschlüssigkeit nicht vermischen.

### 3.2. Verbot und Nachweis unterscheiden

Paragraf 16a Absatz 1 erfasst bestimmte Zahlungsmittel, auch bei erfassten Anteilsgeschäften. Notarielle Nachweispflichten der Absätze 2 bis 4 betreffen die dort bezeichneten unmittelbaren Immobiliengeschäfte. Die Grenze von 10000 Euro in Absatz 5 erlaubt keine kleinere Barzahlung. Verkäuferbestätigung ersetzt nicht automatisch schlüssige Zahlungsnachweise. Teilsummen und Wege einzeln abgleichen.

### 3.3. Meldeanlass belegen

GwGMeldV-Immobilien Paragrafen 3 bis 6 einschließlich aktueller Einschränkungen und Paragraf 7 anwenden. Drittzahlung und Preisabweichung nicht nach alten pauschalen Alarmmustern behandeln. Entkräftung muss belegt sein; langjährige Bekanntschaft genügt nicht.

### 3.4. Einreichung vorbereiten

Fehlt in angemessener Zeit nach Fälligkeit ein schlüssiger Nachweis, Nachforderung und angemessene Frist dokumentieren. Bei meldepflichtigem Vorgang die besondere Fünf-Werktage-Regel nach Paragraf 16a Absatz 3 Nummer 2 prüfen, nicht die allgemeine Drei-Werktage-Regel. Zustimmung, Untersagung und sonstige Hindernisse separat feststellen. Später fällige Gegenleistungen nach Absatz 4 und dessen zeitlichen Grenzen bearbeiten. Keine automatische Grundbuchübermittlung.

## 4. Quellenpflicht

[Paragraf 16a](https://www.gesetze-im-internet.de/gwg_2017/__16a.html), [GwGMeldV-Immobilien](https://www.gesetze-im-internet.de/imgwgmeldv/), [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Für Meldedaten gilt seit 1. März 2026 zusätzlich die GwGMeldV.

## 5. Ausgabeformat

Zahlungsabgleich und ausformulierte Notarvorlage: „Der Eintragungsantrag ist derzeit …, weil …“. Offene Tatsachen, Nachforderung und Wartefrist nennen, keine bloße Ampel. Times New Roman 11 pt, dezimale Gliederung.

## 6. Beispiele

Kaufpreis 486000 Euro, Bankdarlehen 350000 Euro, Eigenmittel 128000 Euro und Rest 8000 Euro: abgleichen und Absatz 5 richtig einordnen. Ein Rest unter 10000 Euro macht eine belegte Barzahlung nicht zulässig.

---

## Skill: `geldwaesche-risikoanalyse-unternehmen`

_Erstellt oder aktualisiert eine betriebsbezogene GwG-Risikoanalyse aus Kundenmix, Leistungen, Zahlungswegen und Kontrollergebnissen. Bewertet konkrete Risiken und Wirksamkeit, ohne jede Kanzlei wie eine Großbank zu behandeln._

# 1. Risikoanalyse aus dem tatsächlichen Betrieb

## 1. Zweck und Anwendungsfall

Für eine erstmalige Analyse oder eine wesentliche Änderung von Geschäftsmodell, Vertrieb oder Zahlungswegen. Ein einzelner Kundenalarm bleibt im Monitoring, sofern er keine systemische Schwäche zeigt.

## 2. Eingaben

Verpflichtetenstatus, Geschäftsbereiche, Kundengruppen, Länder, Umsatz- und Transaktionsverteilung, bisherige Auffälligkeiten und Kontrollen. Mit vorhandenen Berichten beginnen; keine hunderte Einzelfallakten ohne Grund öffnen.

## 3. Ablauf

### 3.1. Umfang und Ausnahmen bestimmen

GwG Paragraf 4 und Paragraf 5 sowie sektorspezifische Ausnahmen prüfen. Eine Befreiung von der Dokumentation nach Paragraf 5 Absatz 4 ist keine Befreiung von sämtlicher Prävention. Reinen Güterhandel anhand eigener Regeln behandeln.

### 3.2. Risiken und Kontrollen verbinden

Jedes Risiko an eine tatsächliche Leistung knüpfen: Fremdgeldweiterleitung, Immobilienabwicklung, Bargeldannahme oder komplexe Eigentumskette. Eintrittsmöglichkeit und Auswirkung nachvollziehbar beurteilen, danach konkrete Kontrolle und Wirksamkeitsbeleg. Niedriges Volumen allein beseitigt kein hohes Einzelrisiko. Keine frei erfundenen Prozentwahrscheinlichkeiten.

### 3.3. Maßnahmen priorisieren

Erst Lücken mit unmittelbar möglichem Schaden schließen: ungeprüfte Auszahlungen, fehlende Vertretung im Meldeweg, unlesbare Identitätsbelege. Verantwortlichen, Umsetzungstermin und Nachweis festlegen. Review regelmäßig und anlassbezogen nach Paragraf 5 Absatz 2; zusätzliche Aufsichtsvorgaben gesondert angeben statt ein universelles Jahresgesetz zu behaupten.

## 4. Quellenpflicht

GwG Paragraf 5, Anlagen 1 und 2, nationale Risikoanalyse sowie zuständige Aufsicht. [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). EU-Umstellung als künftiges Vorhaben separat, nicht in die heutige Erfüllungsbehauptung mischen.

## 5. Ausgabeformat

Vollständig begründete Risikoanalyse mit knapper Tabelle zu Geschäft, Risiko, Kontrolle, Nachweis und verbleibender Lücke; Freigabevorlage an die Leitung. Times New Roman 11 pt, dezimale Gliederung.

## 6. Beispiele

Eine Kanzlei übernimmt erstmals regelmäßig Kaufpreisabwicklungen. Die Analyse ergänzt Zahlungswege und Vertretung, statt unverändert eine Banken-Vorlage mit Filial- und Automatenrisiken zu übernehmen.

---

## Skill: `geldwaesche-krypto-zahlungsdienstleister`

_Ordnet Kryptotransfers und Zahlungsdienstleister nach Rolle, Transferdaten und selbst gehosteter Adresse ein. Trennt Travel Rule, MiCAR-Erlaubnis und GwG-Prüfung und bewertet konkrete Lücken ohne Blockchain-Pauschalverdacht._

# 1. Kryptotransfer und Zahlungsdienst prüfen

## 1. Zweck und Anwendungsfall

Für verpflichtete Anbieter, einen Transferdatenmangel oder die Einordnung eines eingesetzten Dienstleisters. Ein Unternehmen wird durch gelegentlichen Kryptobesitz nicht automatisch Kryptowerte-Dienstleister.

## 2. Eingaben

Dienstleisterrolle, Erlaubnisangaben, Auftraggeber und Begünstigter, Transferbetrag, Zeitpunkt, Wallet-Adressen und vorhandene Transferdaten. Kein Seed, privater Schlüssel oder Zugangscode anfordern.

## 3. Ablauf

### 3.1. Rolle und Transfer trennen

GwG-Kategorie, Zahlungsdienst und Kryptowerte-Dienstleistung bestimmen. Die MiCAR-Erlaubnis beantwortet nicht, ob die konkreten Angaben zur Transaktion vollständig sind. Grenzüberschreitenden Anbieter und anwendbaren Rechtsraum dokumentieren.

### 3.2. Transferinformationen prüfen

Verordnung (EU) 2023/1113 gilt seit 30. Dezember 2024. Erforderliche Angaben zu Auftraggeber und Begünstigtem, fehlende Daten und Nachforderungsweg anhand der konkreten Transferart prüfen. Selbst gehostete Adressen nach einschlägigen Vorgaben und GwG Paragraf 15a behandeln. Keine erfundene allgemeine Pflicht, sämtliche Wallets öffentlich zuzuordnen.

### 3.3. Risiko aus Tatsachen

Kontrolle über eine Adresse, Herkunft des Vermögens und wirtschaftlichen Zweck unterscheiden. Ein Analyseanbieter-Label belegt nicht allein eine Straftat; Transaktionshash, Zeitpunkt und Methodengrenze offenlegen. Konkrete Verdachtstatsachen unverzüglich zum Meldeskill geben. Fehlende Transferdaten nicht mit einem simulierten Namen auffüllen.

## 4. Quellenpflicht

[Verordnung (EU) 2023/1113](https://eur-lex.europa.eu/eli/reg/2023/1113/oj/deu), [GwG Paragraf 15a](https://www.gesetze-im-internet.de/gwg_2017/__15a.html), [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Neue AMLR-Pflichten ab 2027 gesondert führen.

## 5. Ausgabeformat

Vollständiger Transfervermerk mit vorhandenen und fehlenden Daten, Rechtsgrund und zuständigem nächsten Schritt. Times New Roman 11 pt, dezimale Gliederung. Keine automatische Transferfreigabe oder Wallet-Sperre.

## 6. Beispiele

Anbieter liefert Hash und Betrag, aber keine belastbaren Begünstigtendaten. Der Entwurf fordert die konkret erforderlichen Angaben an; fehlende Angaben werden nicht aus einem ähnlichen öffentlichen Wallet-Namen ersetzt.

---

## Skill: `aml-verdachtsmeldung-fiu-leitfaden`

_Prüft konkrete Verdachtstatsachen nach GwG Paragraf 43 und erstellt einen FIU-Meldeentwurf nach der seit März 2026 geltenden GwGMeldV. Trennt Privileg, Meldedaten, Nachreichung, Übermittlungsnachweis und Transaktionsfolgen._

# 1. Verdachtsmeldung prüfen und vorbereiten

## 1. Zweck und Anwendungsfall

Für konkrete Tatsachen, die auf Geldwäsche oder Terrorismusfinanzierung hindeuten, oder die gesetzlich relevante Nichtoffenlegung wirtschaftlich Berechtigter. Kein Strafurteil und keine nachgewiesene Vortat voraussetzen.

## 2. Eingaben

Auslösende Originalnachricht, Zahlungsdaten, Beteiligte, Kenntniszeitpunkt und gegebenenfalls frühere Meldung. Sofort feststellen, ob eine noch ausführbare Transaktion bevorsteht. Unbekannte Informationen offen lassen.

## 3. Ablauf

### 3.1. Schwelle und Informationsschutz

GwG Paragraf 43 Absatz 1 anhand Tatsachen statt bloßer Schlagworte anwenden. Bei Kanzlei und Notariat Absatz 2 mit Rückausnahmen und gegebenenfalls Absatz 6 prüfen. Eine Kunden- oder Branchenzugehörigkeit allein ist kein Meldegrund. Interne Freigabewege dürfen Unverzüglichkeit nicht verzögern; Vertreter und Eskalationsweg festlegen.

### 3.2. Meldung strukturiert entwerfen

Seit 1. März 2026 GwGMeldV Paragrafen 2 und 3 beachten: eigenes Bezugskennzeichen, passende Meldegründe, zusammenhängender Sachverhalt, Personen und Rollen, Konten, Transaktionen und erforderliche Anlagen. Vorhandene relevante Daten in die vorgesehenen Felder eintragen, nicht bloß als Freitextanhang. Unbekannte Geburtsdaten, IBAN oder FIU-Zeichen niemals erfinden. Unverbundene Sachverhalte nicht in eine Sammelmeldung packen.

### 3.3. Tatsachen verständlich erzählen

Was geschah wann, durch wen, mit welchem Betrag, warum auffällig, welche plausible Erklärung liegt vor und welcher Beleg widerspricht ihr? Erkenntnis, Vermutung und Fremdangabe kennzeichnen. Nur erforderliche Anlagen, keine ungesichtete gesamte Beratungsakte.

### 3.4. Abgang und Nachreichung sichern

Registrierung nach GwG Paragraf 45, befugten Einreicher und verfügbaren Meldeweg prüfen. Technische Validierung und tatsächlichen Abgang unterscheiden. Zurückgewiesene Daten korrigieren; bei Störung aktuellen FIU-Ersatzweg anhand amtlicher Angaben prüfen, nicht beliebige E-Mail verwenden. Spätere Erkenntnisse mit Bezug auf Vorzeichen nachreichen. Der Skill sendet nichts selbst. [Nichtdurchführung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/geldwaesche-transaktionsstopp-freeze/SKILL.md) und Paragraf 47 sofort mitführen.

## 4. Quellenpflicht

[GwGMeldV](https://www.gesetze-im-internet.de/gwgmeldv/), [GwG Paragraf 43](https://www.gesetze-im-internet.de/gwg_2017/__43.html), [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Das [Meldeblatt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/assets/templates/verdachtsmeldung-goaml-entwurf.md) ist nur Vorbereitung, kein behördliches Formular.

## 5. Ausgabeformat

Ausformulierter interner Prüfvermerk und separat gekennzeichneter Meldeentwurf mit strukturierten Daten und Anlagenliste. Times New Roman 11 pt, dezimale Gliederung. Abgabe erst als erfolgt bezeichnen, wenn der Übermittlungsnachweis vorliegt.

## 6. Beispiele

Ein Kunde verweigert die Angabe, für wen er handelt, und verlangt sofortige Weiterzahlung. Fehlende Offenlegung, übrige Tatsachen und Privileg prüfen; nicht auf eine spätere Aufsichtskontrolle verschieben.

---

## Skill: `geldwaesche-transaktionsmonitoring`

_Untersucht auffällige Zahlungen, Teilbeträge, Rückerstattungen und Warenströme im Vergleich zum Kundenprofil. Verknüpft Kontoauszug, Vertrag und Beleg und bereitet begründete Erledigung oder zeitnahe Meldeprüfung vor._

# 1. Zahlungsauffälligkeit untersuchen

## 1. Zweck und Anwendungsfall

Für einen konkreten Alert oder ungewöhnlichen Zahlungslauf. Handelsbezogene Auffälligkeiten werden hier bearbeitet; kein eigener parallel laufender Einstieg.

## 2. Eingaben

Vertrag, Rechnung, Lieferbeleg, Kontoauszug und Kundenprofil. Stornos, Valuta und Buchungstag unterscheiden. Nicht aus einer Summenliste erfinden, wer tatsächlich gezahlt hat.

## 3. Ablauf

### 3.1. Zahlungsfluss rekonstruieren

Zahler, Empfänger, Zweck, Betrag, Währung, Zeit und Belegnummer aufeinander beziehen. Verbundene Teilzahlungen nach GwG Paragraf 1 Absatz 5 zusammen betrachten. Überzahlung und Rückzahlung nicht nur saldieren: Ein- und Ausgangskonten bleiben sichtbar.

### 3.2. Wirtschaftlichen Grund prüfen

Mit Kundenprofil und tatsächlicher Leistung vergleichen. Bei Warenhandel Menge, Einzelpreis, Lieferort, Vertragspartner und Transportdokument kontrollieren. Rechnungsberichtigung, Konzernzahlung oder Rückabwicklung können erklärbar sein, brauchen aber Belege. Kein Verdacht allein aufgrund internationaler Tätigkeit.

### 3.3. Verdacht rechtzeitig abzweigen

Ungewöhnliche komplexe Transaktion nach Paragraf 15 gesondert untersuchen. Sobald Tatsachen im Sinne des Paragraf 43 vorliegen, nicht auf eine abgeschlossene interne Untersuchung warten. [Meldeprüfung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/skills/aml-verdachtsmeldung-fiu-leitfaden/SKILL.md) übernimmt; keine Rückzahlung auf ein neu genanntes Drittkonto als automatische „Bereinigung“.

## 4. Quellenpflicht

GwG Paragraf 10 Absatz 1 Nummer 5, Paragraf 15, Paragraf 43 und [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Institutsbezogene Vorschriften wie KWG Paragraf 25h nur bei passender Verpflichtetenkategorie anwenden.

## 5. Ausgabeformat

Ausformulierter Zahlungsbefund mit chronologischer Tabelle, Beleg, plausibler Erklärung, Gegenbefund und offener Handlung. Times New Roman 11 pt, dezimale Gliederung. Keine Risikopunktzahl als alleinige Entscheidung.

## 6. Beispiele

Drei Baranzahlungen gehören zu einer Maschine; eine zusätzliche Überweisung stammt von einem anderen Unternehmen. Zusammengehörigkeit, Empfänger und gewünschte Rückerstattung aus den Originalen rekonstruieren.

---

## Skill: `eu-geldwaescherecht-umstellung-2027`

_Bereitet Kanzlei, Unternehmen und Notariat auf das EU-Geldwäschepaket vor. Trennt geltendes GwG und Meldeformat 2026 von AMLR-Anwendung 2027, Registerumsetzung, AMLA-Aufsicht und noch nicht verbindlichen Entwürfen._

# 1. EU-Umstellung mit belastbaren Stichtagen

## 1. Zweck und Anwendungsfall

Für einen Änderungsplan, neue Pflichtenkataloge und Anpassungen von KYC-Daten oder Kontrollen. Nicht die künftige Verordnung rückwirkend auf einen Vorgang von 2026 anwenden.

## 2. Eingaben

Verpflichtetenkategorie, bestehender Prozess, betroffene Datenfelder und gewünschter Zieltermin. Bereits erledigte Umstellungen anhand Nachweisen übernehmen.

## 3. Ablauf

### 3.1. Zeitachsen auseinanderhalten

Verordnung (EU) 2024/1624 Artikel 90 grundsätzlich ab 10. Juli 2027; Sonderregel bestimmter Fußballakteure separat. Richtlinie (EU) 2024/1640 Artikel 78 mit gestaffelten Umsetzungsfristen: Artikel 74 bis 2025, Artikel 11 bis 14 bis 2026, Artikel 18 bis 2029, grundsätzlich übrige Umsetzung 2027. Fristablauf beweist keine nationale Verkündung.

### 3.2. Konkrete Datenänderung

Heutige Eigentümerprüfung nach GwG Paragraf 3 mit künftigen Artikeln 51 bis 54 vergleichen. Heute mehr als 25 Prozent; künftig grundsätzlich 25 Prozent oder mehr nach Artikel 52. Mittelbare Eigentumsberechnung und Kontrolle getrennt umsetzen. Bei vier gleichen Gesellschaftern Datenerhebung vorbereiten, nicht heutige Einordnung ungeprüft überschreiben.

### 3.3. Zahlungs- und Meldeprozesse

Artikel 80 sieht grundsätzlich maximal 10000 Euro Barzahlung ab 2027 vor; verbundene Vorgänge, Ausnahmen und strengere nationale Regeln prüfen. Nicht mit heutiger Identifizierungsschwelle gleichsetzen. Die GwGMeldV gilt dagegen bereits seit 1. März 2026; fehlende strukturierte Meldedaten nicht bis 2027 aufschieben. Kryptotransferregeln nach Verordnung 2023/1113 gelten bereits seit Ende 2024.

### 3.4. Vorhaben sauber kennzeichnen

AMLA-Aufsicht ab 2028 betrifft ausgewählte Finanzunternehmen, nicht automatisch jede Kanzlei. Konsultation, finalisierter Standardentwurf und erlassener Rechtsakt getrennt führen. Zollfinanzgerechtigkeitsgesetz anhand des BMF-Kabinettsstands vom 12. August 2026 als Vorhaben behandeln, bis Verkündung und Anwendbarkeit belegt sind.

## 4. Quellenpflicht

[Amtliche EU- und deutsche Quellen mit Status](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Vor endgültiger Umsetzung Rechtsakt, Datum, zuständige Stelle und fachlichen Anwendungsbereich aktualisieren.

## 5. Ausgabeformat

Ausformulierter Umstellungsplan mit Tabelle: heutige Pflicht, künftige Änderung, Rechtsaktstatus, Datum, Daten-/Prozessänderung, Verantwortlicher und Abnahmenachweis. Times New Roman 11 pt, dezimale Gliederung. Keine diffuse „AMLA-Frist 2026“.

## 6. Beispiele

Ein Notariat will seine Eigentümerabfrage ändern. Der Plan trennt die neue 25-Prozent-Eigentumsschwelle von schon heute erforderlicher Kontrollprüfung und bestehenden Immobilien-Zahlungsnachweisen.

---

## Skill: `geldwaesche-behoerdenverfahren`

_Bearbeitet Aufsichtsanfragen, Prüfungsfeststellungen und Bußgeldvorwürfe zum GwG. Trennt Mitwirkung, geschützte Informationen, Tatbestand und Verschulden und erstellt eine belegte Antwort oder Rechtsbehelfsvorlage._

# 1. Aufsicht und Bußgeldverfahren bearbeiten

## 1. Zweck und Anwendungsfall

Für ein konkretes Schreiben von Aufsicht oder FIU sowie einen Bußgeldbescheid. Meldung an die FIU ist kein Ersatz für eine fristgebundene Antwort im Aufsichtsverfahren.

## 2. Eingaben

Vollständiges Schreiben, Zustellnachweis, Anlage, Aktenzeichen und bisherige Korrespondenz. Anfragende Stelle und Rechtsgrund aus dem Dokument bestimmen.

## 3. Ablauf

### 3.1. Verfahrensart und Termin

GwG Paragraf 50 zur Aufsicht, Paragraf 51 zu Befugnissen und Paragraf 52 zur Mitwirkung heranziehen. Eine bloße Unterlagenanforderung, belastender Verwaltungsakt und Bußgeldbescheid haben verschiedene Wege. Bei Bußgeldbescheid Einspruch nach OWiG Paragraf 67 grundsätzlich binnen zwei Wochen nach Zustellung prüfen; keine allgemeine Monatsfrist einsetzen.

### 3.2. Antwortumfang abgrenzen

Angeforderte Daten auf Pflichtbezug, Besitz und Schutz prüfen. Aussageverweigerungsrechte und berufsbezogene Grenzen anhand konkreter Norm berücksichtigen. Weder alles ungeprüft versenden noch sämtliche Mitwirkung mit „Schweigepflicht“ ablehnen. Unveränderbare Originale sichern.

### 3.3. Vorwurf substantiiert behandeln

Vorwurf, geltende Normfassung, Tatzeit, verantwortliche Person, Beleg und Gegenbeleg gegenüberstellen. Bußgeldtatbestand nach Paragraf 56, Verschulden und etwaige Unternehmenszurechnung getrennt prüfen. Nachbesserung dokumentieren, aber nicht als Eingeständnis eines unbewiesenen Verstoßes formulieren. Keine pauschale Beweislastumkehr zulasten des Betroffenen.

### 3.4. Außenwirkung begrenzen

Bekanntmachung nach Paragraf 57 von Presseanfrage unterscheiden. Eine externe Antwort enthält weder unnötige Mandatsdaten noch Informationen über beabsichtigte Meldungen. Rechtsbehelf und Sofortmaßnahmen fachlich abstimmen.

## 4. Quellenpflicht

GwG Paragrafen 50 bis 57, OWiG Paragraf 67 und [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Aktuelle Rechtsbehelfsbelehrung prüfen, nicht blind übernehmen.

## 5. Ausgabeformat

Vollständige behördliche Antwort oder gekennzeichneter Rechtsbehelfsentwurf mit Aktenzeichen, konkreten Anträgen, Belegen und Anlagen. Times New Roman 11 pt, dezimale Gliederung. Interne Risikobewertung separat.

## 6. Beispiele

Aufsicht verlangt eine Risikoanalyse; vorhanden ist nur eine unfreigegebene Fassung. Tatsächlichen Stand erklären und Nachreichung konkret terminieren, keinen rückdatierten Beschluss erfinden.

---

## Skill: `geldwaesche-verpflichteten-check`

_Klärt den GwG-Verpflichtetenstatus für ein konkretes Mandat oder Geschäft. Trennt anwaltliche Katalogtätigkeit, Notariat, Güterhandel und freiwillige Kundenkontrolle und erstellt einen begrenzten Pflichtenspiegel._

# 1. Verpflichtetenstatus und Pflichtenumfang

## 1. Zweck und Anwendungsfall

Wer trägt bei welchem Geschäft welche Pflichten? Nicht von „Kanzlei“ oder „GmbH“ unmittelbar auf sämtliche Pflichten schließen.

## 2. Eingaben

Mandatsgegenstand, tatsächliche Leistung, handelnde Person, Standort, Zahlungsart und gegebenenfalls Erlaubnis. Gemischte Tätigkeiten getrennt aufnehmen; nicht vor Klärung des Anwendungsbereichs eine vollständige KYC-Akte verlangen.

## 3. Ablauf

### 3.1. Tätigkeit zuordnen

GwG Paragraf 2 Absatz 1 anwenden. Bei Rechtsanwälten und Notaren Nummer 10 einschließlich einschlägigem Buchstaben prüfen: Transaktionsmitwirkung, Geschäfte im Namen und auf Rechnung des Mandanten und weitere Beratungsgegenstände unterscheiden. Beim Syndikus Paragraf 10 Absatz 8a als Zuordnung bestimmter Sorgfaltspflichten prüfen, nicht als pauschale Befreiung.

### 3.2. Status von Schwellen trennen

Ein Güterhändler kann Verpflichteter sein, obwohl eine konkrete Geschäftsschwelle nicht erreicht wird. Sorgfaltspflichten nach Paragraf 10 Absatz 6a, Risikomanagement nach Paragraf 4 und Meldepflicht nach Paragraf 43 getrennt prüfen. Einen Verdachtsfall nicht wegen kleinen Betrags aussortieren. Bei einem Dienstleistungsunternehmen ohne Katalogtätigkeit freiwillige Prüfung als solche bezeichnen.

### 3.3. Person und Aufsicht bestimmen

Berufsträger, Beschäftigungsform, Berufsausübungsgesellschaft und Niederlassung unterscheiden. Kammerhinweise und Paragraf 50 heranziehen. Nicht jede Konzerngesellschaft ist Finanzinstitut; nicht jede Kanzlei wird von der BaFin beaufsichtigt. Beauftragtenbestellung nach Paragraf 7 und einschlägiger Anordnung prüfen.

## 4. Quellenpflicht

[GwG Paragraf 2](https://www.gesetze-im-internet.de/gwg_2017/__2.html), [Paragraf 10](https://www.gesetze-im-internet.de/gwg_2017/__10.html), [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). EU-Änderungen separat ab 10. Juli 2027 ausweisen, nicht rückwirkend anwenden.

## 5. Ausgabeformat

Ausformulierter Pflichtenspiegel: „Für die Tätigkeit … ist … nach … verpflichtet. Ausgelöst sind …; noch nicht belegt ist …“. Tabelle mit Person, Tätigkeit, Norm, Pflicht und Aufsicht. Times New Roman 11 pt, dezimale Gliederung. Kein allgemeines Gütesiegel „GwG-konform“.

## 6. Beispiele

Maschinenverkauf gegen Überweisung: Händlerstatus und konkrete Sorgfaltspflicht getrennt prüfen. Wechsel von Zahlungsprozess zu Unternehmenskauf: neuen Mandatsumfang gesondert beurteilen.

---

## Skill: `geldwaesche-pep-hochrisikoland-risikoanalyse`

_Prüft PEP-Merkmale und Hochrisikostaaten anhand von Amt, Beziehung, Zeitraum und aktueller Quelle. Leitet passende verstärkte Sorgfaltspflichten ab und unterscheidet Risiko, Sanktion und meldepflichtige Tatsache._

# 1. PEP und Länderbezug differenzieren

## 1. Zweck und Anwendungsfall

Für einen PEP-Hinweis, ausländische Beteiligung, Mittelherkunft oder eine Änderung der EU-Hochrisikoliste. Ein ausländischer Pass ist weder PEP-Nachweis noch Geldwäschebeleg.

## 2. Eingaben

Konkrete Person, Amt, Amtszeit, Nähebeziehung, Länderbezug des Geschäfts und tatsächlicher Suchtreffer. Listenauszug mit Datum; kein bloßer Anbieter-Score ohne Treffergrundlage.

## 3. Ablauf

### 3.1. Person und Merkmal

Namensgleichheit mit Geburtsdaten und Funktion abgleichen. GwG Paragraf 1 zu PEP, Familienmitgliedern und bekanntermaßen nahestehenden Personen prüfen. Bei ehemaligen Amtsträgern Paragraf 15 Absatz 7 und verbleibendes Risiko beachten, nicht nach zwölf Monaten automatisch entwarnen.

### 3.2. Länderliste richtig lesen

Aktuellen EU-Rechtsakt zu Drittstaaten mit hohem Risiko und dessen Anwendungsdatum bestimmen. FATF-Listen und Länderhinweise können Risikoquellen sein, sind aber nicht dieselbe Rechtsgrundlage. Handelsbeziehung, Ansässigkeit, Zahlung und wirtschaftlichen Eigentümer getrennt zuordnen.

### 3.3. Maßnahmen passend wählen

Nach Paragraf 15 erforderliche Informationen, Zustimmung der Führungsebene und verstärkte Überwachung ableiten. Herkunft des konkreten Geldes und Herkunft des Vermögens unterscheiden. Nur zweckbezogene Nachweise anfordern; ein PEP-Fall führt nicht automatisch zur Ablehnung oder FIU-Meldung.

## 4. Quellenpflicht

[GwG Paragraf 15](https://www.gesetze-im-internet.de/gwg_2017/__15.html), aktuelle EU-Listenfassung und [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Nicht behaupten, eine Liste sei aktuell, wenn nur ein alter Export vorliegt.

## 5. Ausgabeformat

Vollständiger Risikovermerk mit geprüfter Person, Quelle, Merkmal, konkreter Zusatzmaßnahme und verantwortlicher Entscheidung. Times New Roman 11 pt, dezimale Gliederung. Sanktionsfrage und Verdachtstatsache in eigenen Absätzen.

## 6. Beispiele

Ein Geschäftsführer teilt den Namen eines ehemaligen Ministers, aber Geburtsdatum und Beruf passen nicht. Treffer dokumentiert auflösen statt alle Geschäfte allein wegen des Namens zu sperren.

---

## Skill: `geldwaesche-transaktionsstopp-freeze`

_Berechnet die Nichtdurchführung nach einer FIU-Meldung und die besondere notarielle Wartefrist. Trennt GwG-Aufschub, Sanktionssperre und unerfüllte Kundenprüfung und dokumentiert den frühesten zulässigen Vollzug._

# 1. Nichtdurchführung und Vollzugszeitpunkt

## 1. Zweck und Anwendungsfall

Für eine abgegangene Meldung, behördliche Untersagung oder die Frage, ob eine konkrete Transaktion schon ausgeführt werden darf. Nicht jeden offenen KYC-Punkt als allgemeines „Freeze“ behandeln.

## 2. Eingaben

Tatsächlicher Meldungsabgang mit Datum und Uhrzeit, technische Rückmeldung, Transaktion, zuständige Stelle, anwendbare Feiertage und jede Zustimmung oder Untersagung. Ein bloßer Entwurf löst keine berechenbare Abgangsfrist aus.

## 3. Ablauf

### 3.1. Rechtsgrund benennen

Vier getrennte Spalten: GwG Paragraf 46, notarielle Sonderregel des Paragraf 16a Absatz 3 Nummer 2, unerfüllbare Sorgfaltspflichten nach Paragraf 10 Absatz 9 und konkrete Sanktionsverbote. Ein Ereignis kann mehrere Hindernisse gleichzeitig betreffen.

### 3.2. Tage einzeln zählen

Allgemein Zustimmung der FIU oder Staatsanwaltschaft oder Ablauf des dritten Werktags nach Abgang ohne Untersagung. Samstag nicht mitzählen. Beim betroffenen notariellen Eintragungsantrag Fünf-Werktage-Regel prüfen. Abgangstag, jeden Zwischentag, Wochenende und Feiertag zeigen; Ausführung nicht bereits am Beginn des letzten Wartewerktags freigeben. Unklaren Feiertagsbezug klären statt blind einen Bankkalender verwenden.

### 3.3. Ausnahme nicht zur Routine machen

Paragraf 46 Absatz 2 nur bei tatsächlicher Unmöglichkeit des Aufschubs oder drohender Behinderung der Strafverfolgung prüfen; gewöhnlicher Termindruck reicht nicht. Unverzügliche Nachmeldung dokumentieren. Fristablauf ist keine Bestätigung der Unbedenklichkeit und beseitigt andere Hindernisse nicht.

### 3.4. Außenkommunikation

Vor jeder Kundennachricht GwG Paragraf 47 prüfen. Keine Erklärung „Wir haben Sie gemeldet“. Verantwortlicher entscheidet die tatsächliche Ausführung und hält Zeitpunkt, Grundlage und verbleibende Beschränkung fest.

## 4. Quellenpflicht

[Paragraf 46](https://www.gesetze-im-internet.de/gwg_2017/__46.html), [Paragraf 16a](https://www.gesetze-im-internet.de/gwg_2017/__16a.html), [Rechtsstand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). [Fristenblatt](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/assets/templates/transaktionsstopp-freeze-plan.md) nur mit tatsächlichem Abgang verwenden.

## 5. Ausgabeformat

Ausformulierter Vollzugsvermerk plus datierte Tageszählung. Times New Roman 11 pt, dezimale Gliederung. Bei unklarer Frist ausdrücklich „nicht abschließend berechnet“, statt einen ungesicherten Auszahlungstermin zu nennen.

## 6. Beispiele

Abgang Montag ohne Feiertag: Dienstag, Mittwoch, Donnerstag sind die drei Wartewerktage; ohne vorherige Zustimmung frühestens nach Ablauf des Donnerstags. Für die notarielle Sonderregel reicht derselbe Donnerstag nicht.

---

## Skill: `geldwaesche-transparenzregister`

_Gleicht wirtschaftlich Berechtigte mit dem Transparenzregister ab. Trennt eigene Mitteilung, Unstimmigkeitsmeldung und FIU-Verdacht und bereitet die konkret erforderliche Registerkorrektur oder Nachforderung vor._

# 1. Transparenzregister ohne falsche Gleichsetzung

## 1. Zweck und Anwendungsfall

Für fehlende Einträge, abweichende Beteiligungsverhältnisse, ausländische Erwerber und den zulässigen Umgang mit Registerauszügen.

## 2. Eingaben

Auszug mit Abrufdatum, ermittelte Eigentümerstruktur, Änderungsdatum und Angaben zum Rechtsträger. Nicht den Stand eines alten Auszugs mit einer späteren Satzungsänderung gleichsetzen.

## 3. Ablauf

### 3.1. Zuständigkeit der Mitteilung

Eigene Mitteilungspflicht der Vereinigung nach GwG Paragraf 20 beziehungsweise Rechtsgestaltung nach Paragraf 21 bestimmen. Ein KYC-Prüfer wird dadurch nicht selbst Organ des Kunden. Vertretungsbefugnis für eine Einreichung gesondert klären.

### 3.2. Abweichung belegen

Registerangabe, Aktenbefund und Stichtag nebeneinanderstellen. Schreibweise, Staatsangehörigkeit, Art und Umfang des Interesses, fehlende Person oder fehlende Eintragung konkret unterscheiden. Registerinhalt ersetzt nicht die eigene Ermittlung.

### 3.3. Meldungen auseinanderhalten

Unstimmigkeitsmeldung nach Paragraf 23a samt berufsbezogener Ausnahme prüfen. Korrekturanregung beim Kunden ersetzt eine geschuldete Meldung nicht. Zusätzlich nur bei entsprechenden Tatsachen eine FIU-Meldung prüfen; Registerabweichung allein nicht zum Strafverdacht erklären. Notarielle Hindernisse bei bestimmten ausländischen Beteiligten eigens benennen.

### 3.4. Zugriff und Nachweis

Auszug nur im erforderlichen Umfang weitergeben. EuGH C-37/20 und C-601/20 betrifft den allgemeinen öffentlichen Zugang, nicht die Abschaffung des Registers. Gegenwärtige Zugangsgrundlage und etwaige nationale Umsetzung der Richtlinie 2024/1640 prüfen.

## 4. Quellenpflicht

GwG Paragrafen 20, 21, 23 und 23a; [Rechtsprechungszuordnung und Stand](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Tatsächlich eingereichten Vorgang nur bei vorhandener Bestätigung so bezeichnen.

## 5. Ausgabeformat

Ausformulierter Abgleichvermerk, bei Bedarf getrennte Korrektur-Nachforderung und Entwurf einer Unstimmigkeitsmeldung. Times New Roman 11 pt, dezimale Gliederung. Keine aus einem Registerfehler abgeleitete automatische Verdachtsmeldung.

## 6. Beispiele

Register nennt den ausgeschiedenen Mehrheitsgesellschafter, die Akte enthält einen neueren Vollzugsnachweis. Änderungsdatum, neue Kontrolle und Meldeweg prüfen, nicht nur die Namen im Kundenbogen überschreiben.

---

## Skill: `geldwaesche-sanktionsscreening`

_Bearbeitet konkrete Sanktionsnamens- und Kontrolltreffer. Prüft Identität, Eigentum, Rechtsakt und Bereitstellungsverbot und trennt echte Sperren von Namensgleichheit, PEP-Hinweisen und Geldwäsche-Wartefristen._

# 1. Sanktionshinweis belastbar prüfen

## 1. Zweck und Anwendungsfall

Für Treffer bei Kunde, Zahlendem, Empfänger oder kontrollierender Person. Kein allgemeines Embargo-Gutachten ohne Bezug zum Geschäft.

## 2. Eingaben

Originaltreffer, Zeitpunkt, Liste, Personendaten, Eigentumsstruktur, Zahlungsweg und betroffener Gegenstand. Fehlender Zugriff auf aktuelle Listen bleibt eine Freigabelücke.

## 3. Ablauf

### 3.1. Identität statt bloßen Namen

Alias, Geburtsdatum, Anschrift und weitere Identifikatoren vergleichen. Treffer, Abweichungen und nicht verfügbare Daten festhalten. Ein unscharfer Treffer darf nicht automatisch zur Behauptung einer Listung werden; ein abweichender Name schließt Kontrolle durch eine gelistete Person nicht aus.

### 3.2. Rechtsfolge aus Rechtsakt

Aktuelle anwendbare Sanktionsverordnung und betroffenen Anhang feststellen. Eigentum und Kontrolle nach diesem Regime prüfen, nicht einfach die GwG-Schwelle für wirtschaftlich Berechtigte übernehmen. Bereitstellungsverbote, Einfrieren und gegebenenfalls Genehmigungstatbestand unterscheiden. Zuständige Genehmigungsstelle nach Finanz- oder Güterbezug bestimmen.

### 3.3. Handeln begrenzen

Bis zur notwendigen Klärung den konkreten Vorgang nicht als freigegeben bezeichnen. Keine eigenmächtige Kontosperre außerhalb bestehender Zuständigkeit auslösen. FIU-Meldeprüfung separat; Ablauf einer GwG-Wartefrist beseitigt kein Sanktionsverbot. Unberechtigte Kundenvorwürfe vermeiden.

## 4. Quellenpflicht

[EU-Sanktionsressourcen](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en), daraus konkreter Rechtsakt und [Quellenkarte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/geldwaeschepraevention-aml-kyc/references/rechtsstand-2026-und-eu-uebergang.md). Anbieterlisten sind Recherchehilfe, keine eigenständige Rechtsgrundlage.

## 5. Ausgabeformat

Ausformulierter Trefferentscheid mit überprüften Identifikatoren, Rechtsakt, Kontrollbeziehung, Entscheidungsträger und Wiedervorlage. Times New Roman 11 pt, dezimale Gliederung. Keine „grüne“ Gesamtfreigabe bei ungeprüfter Kontrollstruktur.

## 6. Beispiele

Kunde selbst nicht gelistet, Gesellschafterstruktur aber unvollständig: keine Entwarnung aus einem reinen Namenslauf. Ein nachweislich anderer gleichnamiger Kunde erhält einen begründeten Fehlertreffervermerk.

---

## Anwendungshinweise

1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.
4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.
