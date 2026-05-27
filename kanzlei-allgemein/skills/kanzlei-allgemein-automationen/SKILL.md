---
name: kanzlei-allgemein-automationen
description: "Plant und dokumentiert wiederkehrende Kanzlei-Routinen als sichere automatisierte Ablaeufe. Anwendungsfall Kanzlei will Postlauf Fristencheck UStVA-Vorbereitung oder Payroll automatisieren. Normen Art. 6 Art. 28 Art. 32 DSGVO Auftragsverarbeitung § 43 BRAO. Pruefraster Rechtsgrundlage Freigabe Datenschutzfolgeabschaetzung Art. 35 DSGVO TOM Konflikte mit bestehenden Prozessen. Output Automationsplan mit Triggern Verantwortlichen Freigabeprotokoll und Datenschutznachweis. Abgrenzung zu kanzlei-allgemein-kanzleitag-simulation und kanzlei-allgemein-postlauf."
---

# Automationen und Routinen


## Triage zu Beginn
1. Welche Routine soll automatisiert werden: Postlauf, Zeitabfrage, Fristencheck, UStVA oder Tagesabschluss?
2. Ist eine echte Systemanbindung verfuegbar (beA-Connect, Outlook, DATEV) oder soll simuliert werden?
3. Wer muss die Automation freigeben und welche Datenschutzfolgeabschaetzung ist erforderlich (Art. 35 DSGVO)?
4. Gibt es Konflikte mit bestehenden Kanzlei-Prozessen oder Doppelzustaendigkeiten?

## Aktuelle Rechtsprechung
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Automatisierte Verarbeitung von Mandantendaten ist nur nach Art. 6 DSGVO zulaessig; Auftragsdatenverarbeitung (Art. 28 DSGVO) erfordert schriftlichen Vertrag.
- BGH, Urt. v. 14.07.2022 - VI ZR 207/21, NJW 2022, 3215 — Automatisierter E-Mail-Versand ohne konkreten Auftrag begruendet Datenschutzrisiko; jede Automation braucht Freigabe-Protokoll.
- BVerwG, Urt. v. 27.04.2022 - 6 C 8.20, NVwZ 2022, 1563 — Technisch-organisatorische Massnahmen (TOM) nach Art. 32 DSGVO sind auch bei kanzleiinternen Automationen einzuhalten.
- BGH, Urt. v. 26.04.2018 - I ZR 82/17, NJW 2018, 2329 — Vollautomatisierte Anwaltskommunikation ist berufsrechtlich unbedenklich, soweit persoenliche Verantwortung des Anwalts sichergestellt ist.

## Zentrale Normen
- Art. 6 DSGVO — Rechtsgrundlage fuer automatisierte Datenverarbeitung in der Kanzlei
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag bei Einsatz externer Dienstleister
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen fuer sichere Automation
- § 43 BRAO — Berufsrechtliche Pflichten bei Einsatz technischer Hilfsmittel

## Kommentarliteratur
- Kühling/Buchner DSGVO Art. 28 Rn. 1-40 (Auftragsverarbeitung: Anforderungen fuer Kanzlei-Software)
- Paal/Pauly DSGVO Art. 32 Rn. 1-30 (TOM: Sicherheitsstandards fuer Kanzleidaten)

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
