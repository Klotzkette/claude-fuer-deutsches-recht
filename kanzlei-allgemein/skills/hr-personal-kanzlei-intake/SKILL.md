---
name: hr-personal-kanzlei-intake
description: "HR Personal Kanzlei Intake: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# HR Personal Kanzlei Intake

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **HR Personal Kanzlei Intake** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-hr-personal` | Verwaltung von Kanzlei-Personal mit Stammdaten Arbeitsvertraegen Onboarding und Offboarding. Anwendungsfall neue Kanzleimitarbeiterin wird eingestellt oder Mitarbeiter scheidet aus und HR-Dokumentation muss gepflegt werden. Normen BDSG § 26 Arbeitnehmerdatenschutz § 622 BGB Kündigungsfrist BRAO-Standesrecht Fortbildungspflicht. Prüfraster Stammdaten Vertraege Onboarding Datenschutz Fortbildungsnachweis Zielvereinbarungen Gratifikation Bonus Offboarding. Output HR-Akte Onboarding-Checkliste Offboarding-Protokoll Fortbildungsnachweis. Abgrenzung zu kanzlei-allgemein-lohn-sv und kanzlei-allgemein-abwesenheiten-urlaub. |
| `kanzlei-allgemein-intake` | Strukturiert jeden Kanzlei-Eingang aus Brief Fax beA E-Mail SMS iMessage WhatsApp Telegram Teams Screenshot Upload oder Telefonnotiz. Erkennt Absender Akte Aktenzeichen Fristen Action-Items Datenschutzrisiken und nächsten Schritt. Fragt bei Unsicherheit gezielt nach. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **HR Personal Kanzlei Intake**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-hr-personal`

**Fokus:** Verwaltung von Kanzlei-Personal mit Stammdaten Arbeitsvertraegen Onboarding und Offboarding. Anwendungsfall neue Kanzleimitarbeiterin wird eingestellt oder Mitarbeiter scheidet aus und HR-Dokumentation muss gepflegt werden. Normen BDSG § 26 Arbeitnehmerdatenschutz § 622 BGB Kündigungsfrist BRAO-Standesrecht Fortbildungspflicht. Prüfraster Stammdaten Vertraege Onboarding Datenschutz Fortbildungsnachweis Zielvereinbarungen Gratifikation Bonus Offboarding. Output HR-Akte Onboarding-Checkliste Offboarding-Protokoll Fortbildungsnachweis. Abgrenzung zu kanzlei-allgemein-lohn-sv und kanzlei-allgemein-abwesenheiten-urlaub.

# HR und Personalverwaltung


## Triage zu Beginn
1. Geht es um Neueinstellung (Vertrag, Onboarding), laufendes Beschaeftigungsverhaeltnis (Urlaub, Krankenstand) oder Beendigung (Kündigung, Offboarding)?
2. Welche Beschaeftigungsart liegt vor: Vollzeit, Teilzeit, Minijob, Werkstudent, freie Mitarbeit?
3. Ist ein Betriebsrat vorhanden (unwahrscheinlich bei Kleinkanzlei, aber pruefenswert ab 5 Beschaeftigten)?
4. Sind datenschutzrechtliche Anforderungen (Art. 88 DSGVO, § 26 BDSG) bei der Personalaktenfuehrung beachtet?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 620-630 BGB — Dienstvertrag: Kuendigung, Zeugnis, Grundpflichten
- § 23 KSchG — Geltungsbereich des Kuendigungsschutzgesetzes ab 10 Beschaeftigte
- § 3 BUrlG — Gesetzlicher Mindesturlaub (24 Werktage)
- § 26 BDSG — Datenverarbeitung fuer Zwecke des Beschaeftigungsverhaeltnisses

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt die interne Personalverwaltung der Kanzlei. Er ersetzt keine Personalsoftware, keine arbeitsrechtliche Prüfung und keine Lohnbuchhaltung, bereitet aber Daten, Entscheidungen und Dokumente so auf, dass die Kanzlei handlungsfähig bleibt.

## Personalakte

Für jede Person erfassen:

- Name.
- Rolle: Berufsträger, Referendar, wissenschaftlicher Mitarbeiter, Rechtsanwaltsfachangestellte, Assistenz, Buchhaltung, studentische Hilfskraft.
- Beschäftigungsart: Vollzeit, Teilzeit, Minijob, Werkstudent, Praktikum, freie Mitarbeit.
- Eintritt, Probezeit, Befristung, Austritt.
- Wochenarbeitszeit und Arbeitstage.
- Urlaubstage.
- Arbeitsort und Remote-Regel.
- Vergütung, Bonus, Gratifikation, Sachbezüge.
- Ansprechpartner, Notfallkontakt, Krankenkasse, Personalnummer.
- Zugänge: beA nur Berufsträger, E-Mail, DMS, Kanzleisoftware, Kalender, Telefon, Schlüssel.
- Vertraulichkeits- und Datenschutzpflichten.

## Workflows

1. Onboarding.
2. Arbeitsvertrag und Nachträge.
3. Rollen- und Rechtevergabe.
4. Probezeit- und Feedbacktermine.
5. Fortbildung und Kammerpflichten.
6. Bonus, Gratifikation und Zielvereinbarung.
7. Offboarding, Rückgabe von Geräten und Rechteentzug.

## Freundliche Führung

Wenn Daten fehlen:

> Das ist noch nicht vollständig, aber wir können schon eine Personalakte vorbereiten. Für die Lohnabrechnung fehlen später noch Steuer-ID, Sozialversicherungsdaten, Krankenkasse und ELStAM-Status.

## Ausgabe

`assets/templates/personalstammblatt.md` und `assets/templates/hr-onboarding-offboarding.md` verwenden.

## 2. `kanzlei-allgemein-intake`

**Fokus:** Strukturiert jeden Kanzlei-Eingang aus Brief Fax beA E-Mail SMS iMessage WhatsApp Telegram Teams Screenshot Upload oder Telefonnotiz. Erkennt Absender Akte Aktenzeichen Fristen Action-Items Datenschutzrisiken und nächsten Schritt. Fragt bei Unsicherheit gezielt nach.

# Intake und Eingangstriage


## Triage zu Beginn
1. Ueber welchen Kanal ist der Eingang erfolgt: Brief, beA, E-Mail, Telefonnotiz, Messenger?
2. Gibt es ein bestehendes Mandat, dem der Eingang zugeordnet werden kann, oder handelt es sich um einen Neueingang?
3. Enthaelt der Eingang fristwahrendes Material (Klage, Bescheid, Urteil, EB)?
4. Sind Datenschutzrisiken oder Mandatsgeheimnis-relevante Informationen im Eingang enthalten?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 51 BRAO — Haftung fuer Organisationspflichtverletzungen im Kanzleibetrieb
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht: alle Eingaenge unterliegen dem Mandatsgeheimnis
- § 173 ZPO — Zustellungszeitpunkt bei beA-Eingang (massgebend fuer Fristbeginn)
- Art. 5 Abs. 1 lit. f DSGVO — Integritaet und Vertraulichkeit bei der Verarbeitung von Mandantendaten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill nimmt beliebige Eingänge entgegen und macht daraus eine geordnete Kanzlei-Entscheidung: zuordnen, neu anlegen, beantworten, fristen, delegieren oder zurückfragen.

## Unterstützte Eingangskanäle

- Brief, Scan, Foto, Fax.
- beA-Nachricht, EGVP-Ausdruck, Empfangsbekenntnis.
- E-Mail und Anhänge.
- SMS, iMessage, WhatsApp, Telegram, Teams.
- Screenshot, Audio-Notiz, Telefonnotiz.
- Ordnerdrop oder Datenraum-Upload.

## Ablauf

1. **Kanal bestimmen**: Quelle, Empfangsdatum, technische Metadaten, Zuverlässigkeit.
2. **Absender und Beteiligte extrahieren**: Mandant, Gegner, Gericht, Behörde, Versicherung, Dritte.
3. **Aktenbezug prüfen**: eigenes Aktenzeichen, fremdes Aktenzeichen, Name, Sache, Gericht.
4. **Fristen und Action-Items erkennen**: Rechtsbehelfsfrist, gerichtliche Verfügung, Antwortfrist, Wiedervorlage, Rückruf.
5. **Mandatsannahme/GwG-Indikatoren erkennen**: neue Anfrage, Unternehmensmandant, Immobilien, Gesellschaft, Transaktion, Ausweiskopie, Handelsregisterauszug, wirtschaftlich Berechtigte, PEP, Fremdgeld, Drittzahlung, abweichender Zahler.
6. **Datenschutz und Geheimnis prüfen**: Drittinhalte, Gesundheitsdaten, Bankdaten, Ausweiskopien, Kinder, Strafdaten, besondere Kategorien.
7. **Priorität setzen**: sofort, heute, diese Woche, warten, nur ablegen.
8. **Ausgabe erzeugen**: Intake-Karte plus vorgeschlagene Ablage.

## Kanalregeln

### Messenger und Screenshots

- Authentizität nicht unterstellen.
- Kontext erfassen: wer schreibt, wann, in welchem Thread.
- Keine privaten Drittinhalte unnötig übernehmen.
- Bei Screenshots immer prüfen, ob abgeschnittene Inhalte entscheidend sein könnten.

### beA

- Empfangstag und eventuelle Zustellung sauber dokumentieren.
- Empfangsbekenntnis nie ohne Freigabe abgeben.
- Keine beA-PIN, Zertifikate oder Token speichern.
- Bei beA-Connect immer `kanzlei-allgemein-bea-journal` verwenden: Nachrichtenjournal einsehen, Screenshot sichern, jede eingegangene Nachricht als ZIP exportieren oder herunterladen, ZIP entpacken und der Akte zuordnen.
- Wenn ein elektronisches Empfangsbekenntnis verlangt wird, EB-anbieten und vor Abgabe ausdrücklich warnen.

### Fax und Brief

- Eingangsstempel und Lesbarkeit prüfen.
- Bei Fristbezug Originaleingang und Scanzeit trennen.

## Ausgabeformat

```markdown
## Intake-Karte

- Kanal:
- Eingang am:
- Absender:
- Betroffene Akte:
- Externe Aktenzeichen:
- Kurzinhalt:
- Fristen:
- Action-Items:
- Risiken:
- Mandatsannahme/GwG:
- Vorschlag:
- Rückfragen:
```

## Übergabe

- Neue Sache: `kanzlei-allgemein-akte` und bei Annahme-/Identifizierungs-/GwG-Indikatoren `kanzlei-allgemein-mandatsannahme-gwg`.
- Unklare Aktenzeichen: `kanzlei-allgemein-aktenzeichen`.
- Frist oder Handlung: `kanzlei-allgemein-fristen-monitor`.
- Antwortentwurf oder Versand: `kanzlei-allgemein-output-versand`.
- beA-Journal, beA-ZIP oder elektronisches Empfangsbekenntnis: `kanzlei-allgemein-bea-journal`.
