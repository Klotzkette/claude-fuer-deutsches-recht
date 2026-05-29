---
name: geburtstage-feiertage
description: Pflegt einen Mandanten- und Geschäftspartner-Geburtstagsverteiler. Reminders einige Tage vor dem Tag. Vorlagen für kurze persoenliche Glueckwunsch-E-Mail (formell-warm). Bei Geschäftspartnern auch Firmenjubilaeen. Geburtstagsverteiler getrennt von Mandantenfaellen — Pflege als Geschäftspartnerstamm. Datenschutz beachten Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Geburtstagsglueckwunsch zulässig; Widerspruchsrecht Mandant beachten.
---

# Geburtstage und Feiertage


## Triage zu Beginn
1. Liegt eine Einwilligung des Empfaengers vor, oder wird auf berechtigtes Interesse (Art. 6 Abs. 1 lit. f DSGVO) gestuetzt?
2. Sollen postalische Karten, E-Mails oder digitale Nachrichten versandt werden?
3. Gibt es einen Widerspruch (Art. 21 DSGVO) einzelner Empfaenger zu beruecksichtigen?
4. Betrifft der Versand Verbraucher (strenger Datenschutz) oder Geschaeftskunden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. f DSGVO — Berechtigtes Interesse als Rechtsgrundlage fuer Mandantenpflege-Kontakte
- Art. 21 DSGVO — Widerspruchsrecht: muss ohne Schranken moeglich sein
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit: nur notwendige Daten speichern
- § 7 UWG — Unzumutbare Belaestigung bei Werbung ohne Einwilligung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflege des Verteilers

### Quellen

- Mandantenstammdaten aus `mandantenakte-anlegen`.
- Geschäftspartner (Steuerberater Notar Sachverständige Kollegen).
- Eingangsbedingung: ausdrückliche oder konkludente Einwilligung des Empfängers.

### Datenmodell

```yaml
- name: Mueller, Hans
  geburtstag: 1972-08-15
  funktion: Geschäftsführer Mueller GmbH (Mandant Aktenkreis 2026/0042)
  ansprache: foermlich  # foermlich / vornamen / locker
  versandweg: e-mail
  e-mail: hmueller@mueller-gmbh.de
  vorlauf-tage: 2
  letzte-glueckwuensche: 2025-08-14
  widerspruch-eingelegt: false
```

### Datenschutz

- **Art. 6 Abs. 1 lit. f DSGVO** berechtigtes Interesse — Mandantenpflege ist allgemein zulässig.
- **Widerspruchsrecht** beachten — auf Widerspruch hin Eintrag deaktivieren.
- **Information bei Mandatsbeginn** (Datenschutzhinweis Art. 13 DSGVO) auf mögliche Glückwunschsendungen.
- **Verarbeitungsverzeichnis** nach Art. 30 DSGVO ergänzen.

## Tagesbrief-Integration

Im `sekretariats-tagesbrief` morgens Eintrag:

```
Heute / in den nächsten Tagen Geburtstag:
- 22.05.2026 Hans Mueller, Geschäftsführer Mueller GmbH — Glückwunsch vorbereiten
- 24.05.2026 RA Dr. Schulz, Kollege Kanzlei XYZ — kurze Mail
```

## Vorlagen

### Förmlich

```
Betreff: Herzliche Glückwünsche zum Geburtstag

Sehr geehrter Herr [Nachname],

zu Ihrem heutigen Geburtstag übermittle ich Ihnen meine besten persoenlichen
Glückwünsche. Ich wünsche Ihnen vor allem Gesundheit Zufriedenheit und
Erfolg im neuen Lebensjahr.

Mit freundlichen Grüßen
[Anwalt]
```

### Vertraut (langjaehriger Geschäftspartner)

```
Betreff: Alles Gute zum Geburtstag

Lieber [Vorname],

zu Ihrem heutigen Geburtstag herzliche Glückwünsche. Vielen Dank für die
gute und vertrauensvolle Zusammenarbeit im vergangenen Jahr.

Beste Grüße aus der Kanzlei
[Anwalt]
```

## Firmenjubiläen

- Erfassung des Gründungsdatums (Handelsregister) bei juristischen Personen als Mandanten.
- 10 25 50 75 100 Jahre als Schwellen.
- Bei runder Jahreszahl: persönliche Glückwunschkarte zusätzlich zur E-Mail.

## Feiertagsversand

- Weihnachten: siehe Skill `weihnachtskarten`.
- Ostern Neujahr: optional je nach Kanzlei.

## Sicherheits-Check

- Vor Versand: Empfänger noch aktiv? Lebt noch? Mandat nicht beendet im Streit?
- Bei Streit beendeten Mandaten: Eintrag manuell deaktivieren oder löschen.

## Audit

- Letzte Versendung dokumentiert (vermeidet Doppelversand und ermöglicht Auswertung).
- Bei Widerspruch unverzueglich löschen oder anonymisieren (DSGVO Art. 17).

## Ausgabe

- Aktualisierter Geburtstagsverteiler.
- Tagesbrief-Eintrag.
- Versand-E-Mails als Entwurf zur Freigabe.
