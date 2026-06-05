---
name: bankrecht-buergschaft-aval-garantieabruf
description: "Bankrecht Buergschaft Aval Garantieabruf: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bankrecht Buergschaft Aval Garantieabruf

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bankrecht Buergschaft Aval Garantieabruf** im Plugin Fachanwalt Bank- und Kapitalmarktrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bankrecht-buergschaft-aval-garantie-routing` | Mandat zu Bürgschaft, Aval oder Bankgarantie im Bankrecht routen: Bürge, Bank, Begünstigter oder Kunde; §§ 765 ff. BGB, §§ 349 und 350 HGB, erstes Anfordern, Regress, Missbrauchseinwand und Beweislast. |
| `bankrecht-garantieabruf-eilrechtsschutz` | Eilrechtsschutz bei Abruf aus Bankgarantie, Aval oder Bürgschaft auf erstes Anfordern vorbereiten: Verfügungsanspruch, Verfügungsgrund, Missbrauchsbelege, Zustellung, Vollziehung und Bankkommunikation. |
| `bankrecht-kaufmaennische-buergschaft-hgb-349-350` | Kaufmännische Bürgschaft prüfen: Handelsgeschäft des Bürgen, § 349 HGB ohne Vorausklage, § 350 HGB ohne BGB-Schriftform, Abgrenzung zu privater Mithaftung, AGB und Prozessstrategie. |

## Arbeitsweg

Im Plugin Fachanwalt Bank- und Kapitalmarktrecht gilt für **Bankrecht Buergschaft Aval Garantieabruf**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bankrecht-buergschaft-aval-garantie-routing`

**Fokus:** Mandat zu Bürgschaft, Aval oder Bankgarantie im Bankrecht routen: Bürge, Bank, Begünstigter oder Kunde; §§ 765 ff. BGB, §§ 349 und 350 HGB, erstes Anfordern, Regress, Missbrauchseinwand und Beweislast.

# Bürgschaft, Aval und Bankgarantie routen

## Aufgabe

Führe ein bankrechtliches Mandat mit Bürgschaft, Aval oder Bankgarantie in den richtigen Prüfpfad. Der Skill ist bewusst praktisch: Erst Rolle und Dokument erkennen, dann Anspruch, Einwendungen, Eilbedarf und Beweise sortieren.

## Rollenklärung

| Mandantenrolle | Primärziel |
| --- | --- |
| Bank | Zahlungspflicht, Textauslegung, Regress, Sicherheiten, Prozessrisiko |
| Bürge/Garant | Inanspruchnahme abwehren, Form/Sittenwidrigkeit/Einreden prüfen |
| Hauptschuldner | Abruf stoppen, Regress vermeiden, Vergleich strukturieren |
| Begünstigter | Zahlung durchsetzen, formalen Abruf richtig stellen |

## Normenanker

- §§ 765 bis 778 BGB: Bürgschaft, Einreden, Vorausklage, Forderungsübergang.
- § 766 BGB: Schriftform der Bürgschaftserklärung.
- §§ 349, 350 HGB: kaufmännische Besonderheiten.
- §§ 780, 781 BGB: Schuldversprechen/Schuldanerkenntnis, wenn Garantie-/Zahlungsversprechen betroffen ist.
- §§ 305 ff., 138, 242 BGB: AGB, Sittenwidrigkeit, Treu und Glauben/Missbrauch.

## Intake

Fordere gezielt:

- Bürgschafts-/Garantie-/Avaltext vollständig.
- Grundvertrag und gesicherte Forderung.
- Abrufschreiben, Fristen, Zustellung, Anlagen.
- Rolle und wirtschaftliche Beziehung des Bürgen.
- bisherige Zahlungen, Sicherheiten, Korrespondenz.

## Ergebnis

Erzeuge eine **Mandats-Triage**:

1. Dokumenttyp.
2. Anspruchsgegner und Anspruchsziel.
3. Sofortfrist/Eilrechtsschutz.
4. stärkste Einwendung.
5. Beweislücken.
6. nächster Schriftsatz, Brief oder Vergleichsvorschlag.

## Anschluss-Skills

- `bankrecht-buergschaft-auf-erste-anforderung`
- `bankrecht-kaufmaennische-buergschaft-hgb-349-350`
- `bankrecht-privatbuergschaft-sittenwidrigkeit`
- `bankrecht-garantieabruf-eilrechtsschutz`

## 2. `bankrecht-garantieabruf-eilrechtsschutz`

**Fokus:** Eilrechtsschutz bei Abruf aus Bankgarantie, Aval oder Bürgschaft auf erstes Anfordern vorbereiten: Verfügungsanspruch, Verfügungsgrund, Missbrauchsbelege, Zustellung, Vollziehung und Bankkommunikation.

# Garantieabruf und Eilrechtsschutz

## Aufgabe

Bereite die schnelle gerichtliche oder außergerichtliche Reaktion vor, wenn ein Abruf aus Bankgarantie, Aval oder Bürgschaft droht. Ziel ist kein breiter Gutachtenaufsatz, sondern eine Eilakte, die in derselben Nacht funktionieren könnte.

## Sofortcheck

- Wann muss die Bank spätestens zahlen?
- Wer ist Antragsgegner: Begünstigter, Bank oder beide?
- Welche konkrete Handlung soll verboten werden?
- Welche Missbrauchstatsachen sind sofort belegbar?
- Ist Zustellung/Vollziehung realistisch?

## Rechtliche Prüfung

- Sicherungstext und Abrufmechanik.
- Verfügungsanspruch aus Grundverhältnis, § 242 BGB oder Unterlassungsanspruch je nach Lage.
- Verfügungsgrund wegen drohender Zahlung und später nur schwer korrigierbarer Liquiditäts-/Reputationsfolge.
- Beweis: Urkunden, E-Mails, Abnahmeprotokolle, Mängellisten, Zahlungsnachweise.
- Prozessrisiko: Gericht kann bloßen Grundvertragsstreit für unzureichend halten.

## Output

Erzeuge:

1. Eilbrief an Bank.
2. Eilbrief an Begünstigten.
3. Antragsgerüst einstweilige Verfügung.
4. Anlagenliste mit Beweisthema.
5. Risikoampel, ob Eilrechtsschutz tragfähig ist.

## 3. `bankrecht-kaufmaennische-buergschaft-hgb-349-350`

**Fokus:** Kaufmännische Bürgschaft prüfen: Handelsgeschäft des Bürgen, § 349 HGB ohne Vorausklage, § 350 HGB ohne BGB-Schriftform, Abgrenzung zu privater Mithaftung, AGB und Prozessstrategie.

# Kaufmännische Bürgschaft nach HGB

## Aufgabe

Prüfe, ob eine Bürgschaft im kaufmännischen Kontext steht und deshalb harte HGB-Folgen auslöst. Der Skill schützt vor dem häufigen Fehler, jede Geschäftsführer- oder Gesellschafterbürgschaft automatisch kaufmännisch zu behandeln.

## Kernprüfung

| Punkt | Frage |
| --- | --- |
| Kaufmannseigenschaft | Ist der Bürge selbst Kaufmann oder handelt er für einen kaufmännischen Betrieb? |
| Handelsgeschäft | Hat die Bürgschaft Betriebsbezug auf Seiten des Bürgen? |
| § 349 HGB | Ist die Einrede der Vorausklage ausgeschlossen? |
| § 350 HGB | Entfällt die BGB-Schriftform wirklich? |
| Privatnähe | Familien-/Ehegatten-/Gesellschaftermotiv statt Handelsgeschäft? |

## Normenanker

- §§ 343 ff. HGB für Handelsgeschäfte.
- § 349 HGB: keine Einrede der Vorausklage, wenn Bürgschaft für den Bürgen Handelsgeschäft ist.
- § 350 HGB: Formvorschriften des § 766 BGB, § 780 BGB und § 781 BGB gelten in den dort genannten kaufmännischen Fällen nicht.
- §§ 765 ff. BGB bleiben im Übrigen relevant.
- §§ 138, 242, 305 ff. BGB als Korrektive.

## Ergebnis

Erstelle:

- HGB-Anwendbarkeitsvermerk.
- stärkste Kläger-/Beklagtenargumente.
- Beweisliste zu Kaufmannseigenschaft und Betriebsbezug.
- Vergleichsfenster, falls Formangriff schwach, aber Überforderung/AGB stark ist.
