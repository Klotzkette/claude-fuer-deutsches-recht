---
name: kanzlei-automationen-bea-journal
description: "Automationen BEA Journal: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Automationen BEA Journal

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Automationen BEA Journal** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-automationen` | Plant und dokumentiert wiederkehrende Kanzlei-Routinen als sichere automatisierte Ablaeufe. Anwendungsfall Kanzlei will Postlauf Fristencheck UStVA-Vorbereitung oder Payroll automatisieren. Normen Art. 6 Art. 28 Art. 32 DSGVO Auftragsverarbeitung § 43 BRAO. Prüfraster Rechtsgrundlage Freigabe Datenschutzfolgeabschaetzung Art. 35 DSGVO TOM Konflikte mit bestehenden Prozessen. Output Automationsplan mit Triggern Verantwortlichen Freigabeprotokoll und Datenschutznachweis. Abgrenzung zu kanzlei-allgemein-kanzleitag-simulation und kanzlei-allgemein-postlauf. |
| `kanzlei-allgemein-bea-journal` | Dokumentation von beA-Verbindungen Nachrichten Versand und Empfangsbekenntnissen. Anwendungsfall beA-Eingang oder Versand muss nachvollziehbar protokolliert werden mit Screenshot ZIP-Export und EB-Workflow. Normen § 130a ZPO § 31a BRAO § 12 ERVV. Prüfraster Nachrichtenjournal Screenshots ZIP-Export eingegangene und versandte Nachrichten EB-Status Freigabe vor Versand. Output Versandjournal EB-Dokumentation ZIP-Archiv Screenshot-Ablage. Abgrenzung zu bea-versand-prüfen (Prüfung Versandweg) und kanzlei-allgemein-output-versand. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Automationen BEA Journal**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-automationen`

**Fokus:** Plant und dokumentiert wiederkehrende Kanzlei-Routinen als sichere automatisierte Ablaeufe. Anwendungsfall Kanzlei will Postlauf Fristencheck UStVA-Vorbereitung oder Payroll automatisieren. Normen Art. 6 Art. 28 Art. 32 DSGVO Auftragsverarbeitung § 43 BRAO. Prüfraster Rechtsgrundlage Freigabe Datenschutzfolgeabschaetzung Art. 35 DSGVO TOM Konflikte mit bestehenden Prozessen. Output Automationsplan mit Triggern Verantwortlichen Freigabeprotokoll und Datenschutznachweis. Abgrenzung zu kanzlei-allgemein-kanzleitag-simulation und kanzlei-allgemein-postlauf.

# Automationen und Routinen


## Triage zu Beginn
1. Welche Routine soll automatisiert werden: Postlauf, Zeitabfrage, Fristencheck, UStVA oder Tagesabschluss?
2. Ist eine echte Systemanbindung verfuegbar (beA-Connect, Outlook, DATEV) oder soll simuliert werden?
3. Wer muss die Automation freigeben und welche Datenschutzfolgeabschaetzung ist erforderlich (Art. 35 DSGVO)?
4. Gibt es Konflikte mit bestehenden Kanzlei-Prozessen oder Doppelzustaendigkeiten?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 DSGVO — Rechtsgrundlage fuer automatisierte Datenverarbeitung in der Kanzlei
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag bei Einsatz externer Dienstleister
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen fuer sichere Automation
- § 43 BRAO — Berufsrechtliche Pflichten bei Einsatz technischer Hilfsmittel

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill übersetzt Kanzlei-Routinen in sichere wiederkehrende Abläufe. Er richtet keine Automation ohne ausdrückliche Zustimmung ein.

## Typische Routinen

- Täglicher Postlauf um 11 Uhr.
- beA-Journallauf mit Screenshot, ZIP-Export, Entpacken, EB-Prüfung und Fristenübergabe, wenn der Nutzer beA-Connect ausdrücklich freigegeben hat.
- Stündliche Zeiterfassungsfrage.
- Ordner-Monitoring für neue Eingänge.
- Fristencheck morgens und nachmittags.
- Tagesabschluss mit offenen Action-Items.
- Nächste-beste-Aktion-Review aus dem Kommandocenter: Fristen, beA, GwG, Rechnungen, offene Posten, Recherche und HR priorisieren.
- Wochenreview für Rechnungen und ruhende Akten.
- Rechnungsreview mit offenen Narrativen, nicht abgerechneten Zeiten, Vorschüssen, Rechtsschutz, GoBD-Ablage und E-Rechnungsvalidierung.
- Geschäftskonto-Review mit neuen Zahlungseingängen, offenen Posten, Bankmatching, Klärfällen und Mahnvorschlägen.
- Monatliche UStVA-Vorbereitung mit Ausgangsrechnungen, Eingangsrechnungen, Betriebsausgaben, Vorsteuer, ELSTER- oder Steuerkanzlei-Übergabe.
- Monatliche Payroll-Vorbereitung mit Fehlzeiten, Bonus, Gratifikation, Lohnsoftware- oder Steuerkanzlei-Übergabe.
- Urlaubs- und Krankheitsreview mit Vertretungscheck für Fristen, beA, Postlauf und Telefon.
- Kanzleikalender-Tagesblick mit Terminen, Abwesenheiten, Payroll, UStVA und Jour fixe.
- Freundlicher Schreib-Canvas-Hinweis, wenn ein Entwurf juristisch unsubstantiiert, unvollständig oder versandnah ist.
- Qualitätsgate für Klagen, Repliken, Verträge und beA-Versand vor Fristablauf.
- Rechtsprechungsmonitor für freigegebene Suchfragen in amtlichen Quellen, OpenJur und dejure.org mit Aktenablage und Aktualitätsvermerk.
- Handelsregisterabruf-Erinnerung bei neuen Unternehmensgegnern, Vertragsparteien oder Rechnungsempfängern.
- Mandatsannahme-/GwG-Reminder für fehlende Identifizierung, wirtschaftlich Berechtigte, Handelsregister, Ausweiskopie, Mandatsvereinbarung, Vorschuss, PEP-Prüfung, Risikobewertung und periodische Aktualisierung.
- Acht-Stunden-Kanzleitag-Simulation für Training, Demo und Testakte.

## Vor jeder Automation fragen

1. Was soll geprüft werden?
2. Welche Akten oder Ordner sind umfasst?
3. Welche Daten dürfen verarbeitet werden?
4. Wer bekommt das Ergebnis?
5. Soll nur berichtet oder auch ein Entwurf vorbereitet werden?
6. Wie wird verhindert, dass echte Fristen nur im Modell hängen?
7. Wie wird verhindert, dass Rechnungen ohne Freigabe, Validierung oder Archivierung erzeugt werden?
8. Ist dies ein Echtlauf oder eine Simulation?
9. Wie werden Personal-, Lohn- und Gesundheitsdaten geschützt?

## Fallback ohne Automationsfunktion

Wenn keine technische Automation verfügbar ist:

- Checkliste erzeugen.
- Kalendertext formulieren.
- Manuelle Routine im Tagesbrief vormerken.

## Sicherheitsregel

Keine stille Überwachung von Messenger, E-Mail, beA oder lokalen Ordnern. Immer transparent machen, was geprüft wird.

Bei beA-Automationen nie PIN, Token, Zertifikatsdateien oder Passwörter entgegennehmen. Jeder EB, jeder Versand und jeder Nachrichtenexport braucht eine nachvollziehbare Einzelentscheidung oder einen vorher klar bestätigten, protokollierten Leselauf ohne Versand.

Bei Rechnungsautomationen nie automatisch finale Rechnungen versenden oder buchen. Zulässig sind offene Narrative, Rechnungsvorschläge, E-Rechnungsdatenblätter, GoBD-Prüfprotokolle und Erinnerungen an Validierung oder Freigabe.

Bei Bank- und Buchhaltungsautomationen nie Bankzugangsdaten entgegennehmen, keine Zahlungsaufträge auslösen und keine endgültige Buchung behaupten. Zulässig sind Kontoauszugsimport, Simulation, Matchingvorschläge, Klärfälle, Mahnvorschläge und Fachsystem-Übergabe.

Bei UStVA-Automationen nie automatisch übermitteln. Zulässig sind Belegsammlung, Summenblatt, Vorsteuer-Unsicherheiten, ELSTER-Checkliste, Steuerberater-Rückfragen und Erinnerung an das Übertragungsprotokoll.

Bei HR- und Payroll-Automationen keine Diagnosen, keine unnötigen Gesundheitsdaten und keine stille Lohn-, SV- oder Lohnsteuerübermittlung. Zulässig sind Register, Erinnerungen, Übergabelisten und Fachsystem-Checklisten.

Bei Rechtsprechungsmonitoring keine vertraulichen Mandatsdaten in öffentliche Suchfelder übernehmen und keine Fundstellen öffentlich ablegen. Zulässig sind pseudonymisierte Suchabfragen, Trefferlisten, Verwertungsnotizen und Ablageprotokolle nach Freigabe.

Bei Mandatsannahme- und GwG-Automationen keine Ausweisdokumente ungeschützt auslesen, keine Verdachtsmeldungen automatisch versenden und keine Mandatsannahme fingieren. Zulässig sind Erinnerungen, Checklisten, Dokumentationsentwürfe, Ablageprotokolle und Freigabeanforderungen.

## 2. `kanzlei-allgemein-bea-journal`

**Fokus:** Dokumentation von beA-Verbindungen Nachrichten Versand und Empfangsbekenntnissen. Anwendungsfall beA-Eingang oder Versand muss nachvollziehbar protokolliert werden mit Screenshot ZIP-Export und EB-Workflow. Normen § 130a ZPO § 31a BRAO § 12 ERVV. Prüfraster Nachrichtenjournal Screenshots ZIP-Export eingegangene und versandte Nachrichten EB-Status Freigabe vor Versand. Output Versandjournal EB-Dokumentation ZIP-Archiv Screenshot-Ablage. Abgrenzung zu bea-versand-prüfen (Prüfung Versandweg) und kanzlei-allgemein-output-versand.

# beA-Nachrichtenjournal und EB-Workflow


## Triage zu Beginn
1. Liegt ein frischer beA-Zugriff oder ein archivierter ZIP-Export vor?
2. Welche Nachrichten muessen der Akte zugeordnet werden (Eingang und Ausgang)?
3. Gibt es Empfangsbekenntnisse (EB), die aktuell zur Entscheidung anstehen?
4. Sind fristwahrende Dokumente dabei, die sofort ins Fristenbuch muessen?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 173 Abs. 2 ZPO — Zustellung per beA: Zustelldatum ist der Tag des EB-Klicks
- § 31a BRAO — Pflicht zur Einrichtung und Nutzung des beA
- § 174 Abs. 4 ZPO — Elektronisches Empfangsbekenntnis: Formerfordernis und Fristausloesung
- § 130a ZPO — Anforderungen an elektronische Dokumente und Uebermittlung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill wird genutzt, sobald eine technische beA-Verbindung, ein beA-Export oder ein beA-Screenshot vorliegt. Er macht aus beA-Zugriffen einen nachvollziehbaren Kanzleivorgang: Journal sichern, Nachrichten archivieren, Eingänge und Ausgänge der Akte zuordnen, Fristen erkennen und elektronische Empfangsbekenntnisse nur nach ausdrücklicher Freigabe vorbereiten oder abgeben.

## Sicherheitsstart

Vor jedem beA-Zugriff ausgeben:

> beA-Sicherheitswarnung: Software-Token, Zertifikatsdatei, PIN und Passwörter nicht in den Chat eingeben und nicht speichern. PIN nur in der lokalen beA-Komponente eingeben. Dieser Lauf dokumentiert Nachrichten, Archive, Screenshots und EB-Entscheidungen, ersetzt aber keine anwaltliche Fristen- und Versandkontrolle.

## Scope klären

1. Welches beA-Postfach wird bearbeitet?
2. Welcher Zeitraum wird geprüft?
3. Welche Akten oder Aktenzeichen sind umfasst?
4. Soll nur gelesen und archiviert oder auch ein Versand vorbereitet werden?
5. Wer ist berufsträgerseitig verantwortlich?
6. Wo sollen Journal, Screenshots, ZIP-Archive und entpackte Nachrichten abgelegt werden?

## Pflichtablauf bei beA-Verbindung

Wenn ein beA-Connect technisch möglich ist:

1. Nachrichtenjournal öffnen und einsehen.
2. Nachrichtenjournal mit Zeitpunkt, Postfach, Filter und Bearbeiter protokollieren.
3. Screenshot des Nachrichtenjournals erstellen oder anfordern.
4. Wenn technisch möglich, Journal zusätzlich als PDF, HTML oder Exportdatei speichern.
5. Jede eingegangene beA-Nachricht als ZIP-Archiv herunterladen oder exportieren.
6. Jedes eingegangene ZIP-Archiv entpacken und die entpackten Dateien der Akte zuordnen.
7. Jede versandte beA-Nachricht nach Versand im Ausgangs- oder Gesendet-Journal öffnen.
8. Jede versandte beA-Nachricht als ZIP-Archiv herunterladen oder exportieren.
9. Jedes versandte ZIP-Archiv entpacken und Versandnachweis, Anlagen und Metadaten prüfen.
10. Für jede Nachricht Fristen, EB, Antwortbedarf und Ablageentscheidung an `kanzlei-allgemein-fristen-monitor` übergeben.

## Eingegangene Nachrichten

Für jeden Eingang erfassen:

- Empfangsdatum und Uhrzeit.
- Absender und SAFE-ID, soweit sichtbar.
- Betreff, Geschäftszeichen, Aktenzeichen, Gericht oder Behörde.
- Zustellart und Zustellnachweis.
- Anlagenliste.
- ZIP-Archivpfad.
- Entpackter Ablagepfad.
- Screenshot- oder Journalnachweis.
- Fristen und Action-Items.
- Ob ein elektronisches Empfangsbekenntnis verlangt oder sinnvoll ist.

## Versandte Nachrichten

Nach jedem beA-Versand:

1. Gesendet- oder Ausgangsjournal öffnen.
2. Versandstatus, Empfänger, Zeitpunkt, Nachrichtentyp, Aktenzeichen und Anlagen kontrollieren.
3. Screenshot des Versandstatus oder Nachrichtenjournals erstellen.
4. Versandte Nachricht als ZIP-Archiv herunterladen oder exportieren.
5. ZIP entpacken.
6. Versandnachweis, Prüfprotokoll, Schriftsatzfassung und Anlagen mit dem Versandauftrag abgleichen.
7. Ergebnis in `assets/templates/bea-nachrichtenjournal.md` und `assets/templates/output-versandprotokoll.md` dokumentieren.

## Elektronisches Empfangsbekenntnis

Wenn eine Nachricht ein EB verlangt oder nahelegt:

1. EB-Anforderung erkennen und Quelle zitieren.
2. Zustellungsdatum, Fristbeginn, Dokumentumfang und Akte prüfen.
3. Berufsträger fragen:

 > Soll ich für diese beA-Nachricht ein elektronisches Empfangsbekenntnis vorbereiten oder abgeben?

4. Vor Abgabe zusätzlich warnen:

 > EB-Abgabe bestätigt den Empfang und kann Fristen auslösen. Bitte erst nach Prüfung von Akte, Nachricht, Anlagen, Zustellungsdatum, Fristfolgen und Berufsträgerzuständigkeit freigeben.

5. Ohne ausdrückliche Einzelbestätigung kein EB abgeben.
6. Nach EB-Abgabe Journal erneut öffnen, Screenshot erstellen, EB-Nachweis speichern, ZIP-Export sichern und Fristenmonitor aktualisieren.

## Fallback ohne technische beA-Steuerung

Wenn das System beA nicht selbst bedienen kann:

- Schritt-für-Schritt-Checkliste für den Nutzer ausgeben.
- Den Nutzer bitten, Journal-Screenshot, Nachrichten-ZIP, Versand-ZIP oder EB-Nachweis hochzuladen.
- Keine Behauptung aufstellen, dass ein Versand, Download oder EB erfolgt sei.

## Ausgabe

`assets/templates/bea-nachrichtenjournal.md` verwenden.
