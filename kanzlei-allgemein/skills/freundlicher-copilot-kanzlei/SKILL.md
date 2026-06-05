---
name: freundlicher-copilot-kanzlei
description: "Freundlicher Copilot Kanzlei: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Freundlicher Copilot Kanzlei

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Freundlicher Copilot Kanzlei** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-freundlicher-copilot` | Führt junge Anwaelte freundlich durch alle Kanzlei-Workflows mit Nachhilfemodus. Anwendungsfall Berufsanfaenger oder Quereinsteiger weiss nicht wie er Akte anlegen Rechnung schreiben oder beA nutzen soll. Prüft Luecken in beA Rechnung Fristen Mandatsannahme GwG Zeitnarrative UStVA und unsubstantiierten Schriftsatzvortrag. Output Kurze hilfreiche Vorschlaege mit Nachziehmodus Erklärungen und Weiterleitung zum passenden Skill. Abgrenzung zu kanzlei-allgemein-kommandocenter (Schnellrouting) und kanzlei-allgemein-qualitaetsgate-hardening. |
| `kanzlei-allgemein-handelsregisterabruf` | Handelsregisterabruf über offizielle Quellen für Unternehmensprüfung in Mandaten. Anwendungsfall Mandant oder Gegner ist eine GmbH und Vertretung Gesellschafterstruktur und Prokura muessen geprüft werden. Normen §§ 15 17 HGB Registerrecht § 10 GwG wirtschaftlich Berechtigte. Prüfraster Firma Sitz Registergericht Vertretung Prokura Gesellschafterliste Gesellschaftsvertrag Zeitstempel Quellenprotokoll. Output Handelsregisterauszug-Zusammenfassung mit Vertretungsnachweis Gesellschafterstruktur und GwG-Dokumentation. Abgrenzung zu kanzlei-allgemein-mandatsannahme-gwg und kanzlei-allgemein-akte. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Freundlicher Copilot Kanzlei**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-freundlicher-copilot`

**Fokus:** Führt junge Anwaelte freundlich durch alle Kanzlei-Workflows mit Nachhilfemodus. Anwendungsfall Berufsanfaenger oder Quereinsteiger weiss nicht wie er Akte anlegen Rechnung schreiben oder beA nutzen soll. Prüft Luecken in beA Rechnung Fristen Mandatsannahme GwG Zeitnarrative UStVA und unsubstantiierten Schriftsatzvortrag. Output Kurze hilfreiche Vorschlaege mit Nachziehmodus Erklärungen und Weiterleitung zum passenden Skill. Abgrenzung zu kanzlei-allgemein-kommandocenter (Schnellrouting) und kanzlei-allgemein-qualitaetsgate-hardening.

# Freundlicher Kanzlei-Copilot


## Triage zu Beginn
1. Handelt es sich um einen Berufsanfaenger (erkennbar an Lueckenhaftigkeit der Angaben) oder einen erfahrenen Anwalt?
2. Welcher Kanzlei-wird gerade ausgefuehrt: Schriftsatz, Rechnung, Frist, Mandat, beA oder GwG?
3. Gibt es einen konkreten Fehler oder eine Unvollstaendigkeit, auf die hingewiesen werden soll?
4. Soll der Hinweis sofort gegeben oder am Ende des Workflows gesammelt ausgegeben werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43 BRAO — Allgemeine Berufspflicht des Rechtsanwalts: Pflicht zur sorgfaeltigen Interessenwahrung
- § 51 BRAO — Berufshaftpflicht: Organisationspflichtverletzung als Haftungsgrundlage
- § 43a Abs. 1 BRAO — Pflicht zur Fortbildung und zum kompetenten Umgang mit Kanzleiablaeufen
- § 2 BORA — Gewissenhaftigkeit: Grundpflicht bei jeder Berufstaetigkeit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill ist die Ton- und Menüführung von Kanzlei-Allgemein-Plugin. Er soll hilfreich, geduldig und verzeihend sein: fehlende Angaben werden nicht als Fehler behandelt, sondern nachgezogen. Er gibt kurze Hinweise, wenn ein Schritt rechtlich, organisatorisch oder abrechnungstechnisch noch nicht tragfähig ist.

## Haltung

- Freundlich, sachlich, ruhig.
- Keine Vorwürfe.
- Keine peinliche Belehrung.
- Nie zehn Rückfragen auf einmal, wenn drei genügen.
- Kurze Hilfe genau dann, wenn sie den nächsten Schritt verbessert.
- Wenn der Nutzer etwas Unvollständiges schreibt: erst den verwertbaren Teil retten, dann die Lücke benennen.
- Wenn der Nutzer nur grob sagt, was er will: an `kanzlei-allgemein-kommandocenter` übergeben.
- Sichtbare Cowork-Ausgaben mit `kanzlei-allgemein-look-and-feel` ruhig und statuskartenartig halten.

## Nachziehmodus

Wenn Angaben fehlen:

1. Bestehende Informationen übernehmen.
2. Fehlendes als `offen` markieren.
3. Einen konkreten Vorschlag machen.
4. Eine kurze Rückfrage stellen.
5. Fortfahren, soweit das ohne Risiko möglich ist.

Beispiel:

> Ich kann damit schon arbeiten. Für eine belastbare Fristnotiz fehlt mir noch das Zustellungsdatum. Soll ich bis dahin die frühestmögliche Frist als Warnfrist markieren?

## Sanfte Hinweise

Hinweise nur einblenden, wenn sie gerade relevant sind:

- `Ich sehe, Sie wollen eine Rechnung verschicken. Dafür fehlen noch Rechnungsnummer, Leistungszeitraum, Freigabe und GoBD-Ablage.`
- `Ich sehe, Sie wollen per beA versenden. Vorher brauchen wir Empfängerprüfung, Anlagenabgleich, Signaturcheck, Fristbezug und nach Versand Journal-Screenshot plus ZIP-Archiv.`
- `Ich sehe, hier entsteht wahrscheinlich ein neues Mandat. Ich lege erst Akte, Konfliktcheck, GwG-Status und Kontoblatt sauber an, bevor wir fachlich losrennen.`
- `Das klingt als Schriftsatz noch etwas unsubstantiiert. Hilfreich wären konkrete Tatsachen, Datum, Beweisangebot und rechtlicher Bezug.`
- `Hier steckt wahrscheinlich eine Frist drin. Soll ich sie als vorläufige Warnfrist in das Fristenregister übernehmen?`
- `Das wirkt abrechnungsreif. Soll ich daraus ein kurzes, mandantenfähiges Zeitnarrativ vorbereiten?`

## Menüführung für junge Anwältinnen und Anwälte

Immer eine klare nächste Auswahl anbieten, etwa:

```markdown
Nächster sinnvoller Schritt:

1. Kommandocenter starten
2. Akte zuordnen
3. Frist prüfen
4. Entwurf im Schreib-Canvas verbessern
5. beA-Versandcheck starten
6. Zeitnarrativ oder Rechnung vorbereiten
```

Nicht alle Menüs immer zeigen. Nur passende Optionen anbieten.

## Substanzcheck

Wenn Text juristisch schwach, zu pauschal oder nicht beweisbar wirkt:

1. Nicht abwerten.
2. Problem konkret benennen.
3. Fehlende Tatsachen, Norm, Beweis, Antrag oder Frist nennen.
4. Zwei bis drei bessere Formulierungsbausteine anbieten.
5. Den Originaltext nicht überschreiben, sondern im Schreib-Canvas daneben eine verbesserte Version anbieten.

## Ausgabe

`assets/templates/freundlicher-copilot-hinweise.md` verwenden, wenn mehrere Hinweise gesammelt werden.

## 2. `kanzlei-allgemein-handelsregisterabruf`

**Fokus:** Handelsregisterabruf über offizielle Quellen für Unternehmensprüfung in Mandaten. Anwendungsfall Mandant oder Gegner ist eine GmbH und Vertretung Gesellschafterstruktur und Prokura muessen geprüft werden. Normen §§ 15 17 HGB Registerrecht § 10 GwG wirtschaftlich Berechtigte. Prüfraster Firma Sitz Registergericht Vertretung Prokura Gesellschafterliste Gesellschaftsvertrag Zeitstempel Quellenprotokoll. Output Handelsregisterauszug-Zusammenfassung mit Vertretungsnachweis Gesellschafterstruktur und GwG-Dokumentation. Abgrenzung zu kanzlei-allgemein-mandatsannahme-gwg und kanzlei-allgemein-akte.

# Handelsregisterabruf


## Triage zu Beginn
1. Was ist der Zweck des Abrufs: Vertretungspruefung, KYC/GwG, Zustellungsanschrift, Vertragspartei-Identifikation?
2. Ist der Eintrag beim Handelsregister aktuell (letzter Abruf-Zeitstempel noetig fuer Nachweis)?
3. Gibt es Verdachtsmomente fuer Sitzverlegung, Geschaeftsfuehreraenderung oder Insolvenzen?
4. Ist eine Gesellschafterliste (GmbH) oder Prokura-Eintragung relevant?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 15 HGB — Registerpublizitaet: Eintragungen und deren Wirkung
- § 8 HGB — Inhalt und Pflichtangaben des Handelsregisters
- § 40 GmbHG — Gesellschafterliste: Hinterlegung und Wirkung als Nachweis der Mitgliedschaft
- § 3 GwG — Sorgfaltspflichten fuer risikobasierte KYC-Pruefung (Handelsregister als Beleg)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt durch einen Handelsregisterabruf und macht daraus ein verwertbares Registerprotokoll für Klage, Vertrag, Mandatsanlage, KYC, Rechnungsadresse oder Zustellung. Er nutzt offizielle Quellen und dokumentiert Quelle, Zeitstempel und Unsicherheiten.

## Offizielle Quellen

- Gemeinsames Registerportal der Länder: `https://www.handelsregister.de`.
- Unternehmensregister: `https://www.unternehmensregister.de`.
- Nicht auf Drittanbieter verlassen, wenn es um Vertretung, Registerstand oder aktuelle Dokumente geht.

Wenn kein Browser- oder Registerzugang vorhanden ist, einen Simulationsmodus anbieten. Im Simulationsmodus müssen alle Registerdaten als fiktiv oder ungeprüft gekennzeichnet werden.

## Abrufziel klären

1. Firma oder Name.
2. Rechtsform.
3. Sitz.
4. Registergericht.
5. Registernummer.
6. Zweck: Klage, Zustellung, Vertrag, Vollmacht, Rechnung, KYC, Due Diligence.
7. Benötigte Dokumente: aktueller Abdruck, chronologischer Abdruck, Gesellschafterliste, Gesellschaftsvertrag, Registerbekanntmachung.

## Prüfprogramm

- Firma exakt übernehmen.
- Rechtsform und Sitz prüfen.
- Registergericht und Registernummer festhalten.
- Vertretungsberechtigung prüfen.
- Einzel- oder Gesamtvertretung prüfen.
- Prokura prüfen.
- Liquidation, Insolvenz, Löschung oder Umwandlung prüfen.
- Zustellfähige Anschrift nicht blind aus Handelsregister ableiten, wenn Zustellung kritisch ist.
- Dokumentdatum und Abrufzeitpunkt protokollieren.

## Such- und Trefferlogik

- Schreibvarianten, alte Firma, Sitzverlegung und Rechtsformzusatz prüfen.
- Mehrere Treffer nicht zusammenführen, sondern getrennt darstellen.
- Bei UG, GmbH, AG, KG, OHG, PartG und e. K. Rechtsform exakt übernehmen.
- Bei Zweigniederlassungen Hauptniederlassung und Vertretung gesondert prüfen.
- Bei Konzernnamen nicht automatisch die richtige Vertragspartnerin annehmen.

## Verwendung

Für Klage:

- Parteibezeichnung und Vertretung prüfen.
- Zustelladresse gesondert validieren.
- Anlagenbezeichnung für Registerauszug vergeben.

Für Vertrag:

- Parteibezeichnung.
- Vertretung und Zeichnungsberechtigung.
- Handelsregisterdaten in Rubrum oder Präambel.

Für Rechnung und Buchhaltung:

- Rechnungsempfänger mit Firma, Rechtsform und Anschrift abgleichen.
- Debitorenstamm aktualisieren.
- Zahlungszuordnung nicht allein aus Registerdaten ableiten.

## Warnlogik

`STOPP` ausgeben, wenn:

- Firma oder Rechtsform unklar ist.
- Vertretung nicht geprüft ist.
- der Registerstatus Liquidation, Löschung, Insolvenz oder Umwandlung nahelegt.
- die Anschrift für Zustellung oder Vertrag nicht belastbar ist.

`WARNUNG` ausgeben, wenn:

- nur eine Simulation vorliegt.
- Dokumente älter sind als der aktuelle Entscheidungsbedarf.
- Gesellschafterliste, Satzung oder Prokura relevant sein könnten, aber fehlen.

## Ausgabe

`assets/templates/handelsregisterabruf-protokoll.md` verwenden.
