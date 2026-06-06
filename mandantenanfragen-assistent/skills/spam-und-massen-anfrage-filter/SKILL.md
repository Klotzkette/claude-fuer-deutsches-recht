---
name: spam-und-massen-anfrage-filter
description: "Sekretariat hat Anfrage erhalten die verdaechtig ausschaut. Spam-Erkennung Kanzlei-Eingang. Prüfraster: Spam Werbung 419-Scams automatisierte Recruiter-Mails Massen-Mandantenanfragen Phishing. Output: Spam-Einschaetzung mit Empfehlung Aussortierung oder Nachfrage. Abgrenzung zu anfrage-eingang-parser (echte Anfragen) und dringlichkeitsmarker im Mandantenanfragen Assistent: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Spam-und-Massen-Anfrage-Filter

## Arbeitsbereich

Sekretariat hat Anfrage erhalten die verdaechtig ausschaut. Spam-Erkennung Kanzlei-Eingang. Prüfraster: Spam Werbung 419-Scams automatisierte Recruiter-Mails Massen-Mandantenanfragen Phishing. Output: Spam-Einschaetzung mit Empfehlung Aussortierung oder Nachfrage. Abgrenzung zu anfrage-eingang-parser (echte Anfragen) und dringlichkeitsmarker. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieser Skill erkennt und kennzeichnet eingehende E-Mails, die keine legitimen Mandantenanfragen sind. Bei positiver Spam-Erkennung wird keine Erstantwort generiert; stattdessen erhält das Sekretariat eine Aussortierungsempfehlung.

## Triage zu Beginn
1. Zeigt die Anfrage klassische Spam-Muster (419-Scam, automatisierte Masse, Phishing, Werbung)?
2. Gibt es Hinweise auf massenhafte identische Einsendung (Template-Formulierungen, ungewoehnliche Absenderadressen)?
3. Soll die Anfrage zur Aussortierung markiert oder direkt verworfen werden?
4. Gibt es Zweifelsfaelle, bei denen die Sekretariatsmitarbeiterin manuell entscheiden soll?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 32 DSGVO — TOM: Spam-Filter als Sicherheitsmassnahme fuer Kanzleikommunikation
- § 263 StGB — Betrug: 419-Scam als strafrechtlich relevanter Betrugsversuch; Nichtbearbeitung ist pflichtgemaess
- § 43 BRAO — Sorgfaltspflicht: Ressourceneinsatz der Kanzlei darf auf legitime Anfragen beschraenkt werden
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: keine Verarbeitung von Spam-Daten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Spam-Muster-Katalog

### Kategorie 1: Klassischer 419-Scam (Vorschussbetrug)

Kennzeichen:
- Absender aus Drittländern, die nicht zum Sachverhalt passen
- Schilderung großer Summen, die "transferiert" werden sollen
- Anfrage nach Treuhandkonto, Bankkontodaten oder Vorleistungen
- Formulierungen: "millions of dollars", "strictly confidential", "God bless you"
- Regelmäßig schlechtes Deutsch oder maschinell übersetzter Text

Aktion: `SPAM — 419-SCAM`

### Kategorie 2: Automatisierte Massen-Mandantenanfragen

Kennzeichen:
- Identischer Wortlaut in mehreren eingehenden Mails
- Merkmale automatisierter Erstellung: fehlende Personalisierung, Template-Formulierungen
- Ungewöhnliche Absenderadressen (zufällige Zeichenfolgen, zahlreiche Ziffern)
- Keine konkreten Sachverhaltsdaten

Aktion: `SPAM — MASSEN-ANFRAGE`

### Kategorie 3: Werbung und Newsletter

Kennzeichen:
- Angebotscharakter: Dienstleistungen, Produkte, Software für die Kanzlei
- Opt-out-Link vorhanden
- "Unsubscribe"- oder "Abbestellen"-Hinweis
- Absender ist erkennbar ein Unternehmen, nicht eine Privatperson

Aktion: `KEIN-SPAM — WERBUNG` (gesonderter Kanal; kein Erstantwort-Prozess)

### Kategorie 4: Automatisierte Recruiter-Mails

Kennzeichen:
- Angebot von Kandidaten für offene Stellen
- Formulierungen wie "Ich bin auf Ihr Unternehmen aufmerksam geworden"
- Anhänge mit Lebenslauf ohne Bezug zu einer Stellenausschreibung
- Häufig über LinkedIn- oder XING-Weiterleitungen

Aktion: `KEIN-SPAM — RECRUITER` (Weiterleitung an HR-Kanal)

### Kategorie 5: Phishing-Versuche

Kennzeichen:
- Links zu gefälschten Webseiten (URL-Check: Domain nicht zur angeblichen Organisation passend)
- Dringende Aufforderung, Zugangsdaten einzugeben
- Drohende Konsequenzen bei Nicht-Antwort innerhalb kurzer Frist
- Absender gibt sich als bekannte Institution aus (Finanzamt, Gericht, Strafverfolgungsbehörde)

Aktion: `SPAM — PHISHING` und: Hinweis an Kanzlei-IT

### Kategorie 6: Spamfilter-Umgehungsversuche

Kennzeichen:
- Wörter mit Ziffern statt Buchstaben: "R3cht", "An1walt"
- Unsichtbare Zeichen, übermäßige HTML-Formatierung
- Betreff-Zeile in Großbuchstaben: "DRINGEND!!!" ohne Substanz
- Mehrfache Leerzeichen oder Zeilenumbrüche zur Zeichentrennung

Aktion: `SPAM — FILTER-UMGEHUNG`

## Positive-Signal-Liste (kein Spam)

Die folgenden Merkmale sprechen gegen Spam:
- Konkreter Sachverhalt mit Datum, Personen, Ort
- Deutschsprachig oder in einer der unterstützten Sprachen (EN, FR, IT)
- Persönliche Anrede oder Selbstvorstellung
- Reale Absender-Domain (kein Wegwerf-Mail-Dienst)
- Anhang mit relevanten Dokumenten (Kündigung, Bescheid, Vertrag)

## Ausgabeformat

```
SPAM-CHECK ERGEBNIS
===================
Status: [KLAR / VERDÄCHTIG / SPAM — TYP]
Konfidenz: [HOCH / MITTEL / NIEDRIG]
Erkannte Muster: [Liste der erkannten Muster oder "keine"]
Empfehlung: [Normale Bearbeitung / Manuelle Prüfung / Aussortieren / IT-Meldung]
```

## Verhalten bei SPAM-Erkennung

1. Keine Erstantwort generieren.
2. Skeleton-Eintrag im CRM nur mit Status "SPAM" und Typ; keine vollständige Datenerfassung.
3. Sekretariat erhält Hinweis mit Aussortierungsempfehlung.
4. Bei Phishing: zusätzliche Meldung an die Kanzlei-IT.
5. Bei VERDÄCHTIG (nicht eindeutig): Empfehlung zur manuellen Prüfung durch Rechtsanwalt oder erfahrene Mitarbeitende vor Beantwortung.

## Falsch-Positiv-Schutz

Der Filter ist bewusst konservativ eingestellt. Im Zweifel lieber `VERDÄCHTIG` als `SPAM` — echte Anfragen dürfen nicht unbeantwortet aussortiert werden. Die Endentscheidung liegt immer beim Sekretariat.

## Verweise auf andere Skills

- `anfrage-eingang-parser` — liefert den geparsten Text für die Filter-Analyse
- `folgekorrespondenz-vorbereiten` — erhält den Spam-Status
- `dringlichkeitsmarker` — läuft nur bei KLAR-Status
- `erstantwort-generator` — wird nur bei KLAR-Status ausgeführt
