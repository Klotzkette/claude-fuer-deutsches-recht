---
name: weihnachtskarten
description: Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfaenger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte für formell-zurückhaltend warm und persoenlich. Druckliste für Postversand inkl Adressetiketten und Frankierhinweis. Versandzeitraum (vor Weihnachten) und Erinnerungen. Datenschutz Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Mandantenpflege; Widerspruchsrecht.
---

# Weihnachtskarten Mandantenpflege


## Triage zu Beginn
1. Wann soll der Versand beginnen und soll postalisch, digital oder beides versandt werden?
2. Sind alle Empfaenger datenschutzrechtlich geprueft (Einwilligung oder berechtigtes Interesse, Art. 6 Abs. 1 lit. f DSGVO)?
3. Gibt es Widersprueche (Art. 21 DSGVO) von einzelnen Empfaengern, die aus dem Verteiler zu loeschen sind?
4. Welche Anredeform und welcher Ton soll verwendet werden: formell-zurueckhaltend, warm-persoenlich oder neutral?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 6 Abs. 1 lit. f DSGVO — Berechtigtes Interesse als Rechtsgrundlage fuer Mandanten-Karten
- Art. 21 Abs. 2 DSGVO — Widerspruchsrecht bei Direktmarketing: sofortige Wirkung
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit im Kartenverteiler
- § 7 UWG — Unzumutbare Belaestigung: E-Mail ohne klare Einwilligung bei Verbrauchern riskant

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verteilerpflege

```yaml
- name: Mueller, Hans
  anrede: foermlich
  empfaenger: Mueller GmbH (zu Hd. Hans Mueller)
  anschrift: ...
  e-mail: hmueller@mueller-gmbh.de
  versandweg: digital  # digital / post / beides
  beziehung: Mandant Aktenkreis 2026/0042
  ton: warm-foermlich
  letzte-karte: 2025-12-15
  widerspruch: false
```

## Texte

### Förmlich-zurückhaltend (Mandanten gemischter Branchen)

```
Sehr geehrter Herr [Nachname],

zum Ende dieses Jahres moechte ich Ihnen für die vertrauensvolle
Zusammenarbeit danken. Ich wünsche Ihnen ruhige besinnliche Feiertage
einen guten Übergang ins neue Jahr und vor allem Gesundheit.

Mit freundlichen Grüßen

[Anwalt]
Kanzlei XYZ
```

### Warm (langjaehrige Geschäftspartner Kollegen)

```
Liebe(r) [Vorname],

am Ende eines arbeitsreichen Jahres ein herzliches Dankeschoen für die
gute Zusammenarbeit. Ich wünsche Ihnen besinnliche Festtage einen
guten Rutsch und ein gesundes glückliches neues Jahr.

Beste Grüße
[Anwalt]
```

### Persönlich (engster Kreis)

Individuell formuliert — kein Templating; auf der persönlichen Beziehung aufbauend.

## Versandformen

### Postversand

- **Karten** mit handgeschriebener Unterschrift Pflicht.
- **Druckliste** für Adressetiketten oder Briefumschlag-Druck.
- **Frankierung** als Standardbrief oder Postkarte.
- **Versandzeitraum** zweite Dezemberwoche damit vor Weihnachten ankommt.

### Digitaler Versand

- **E-Mail** mit kurzer persönlicher Anrede.
- **Anhang** optional als PDF-Karte (Briefkopf der Kanzlei).
- **Versandzeitraum** kurz vor Weihnachten (z. B. 22./23. Dezember).
- **Massenversand vermeiden** — pro Empfänger einzeln im Bcc nicht zulässig wegen DSGVO; lieber serienmaessig versenden.

### Hybrid

- Engste Mandanten und Partner Postkarte plus zusätzlich kurze E-Mail.
- Sonstige nur digital.

## Druckliste für Postversand

CSV mit Spalten: Name Anschrift Stadt PLZ Land Ansprache.

## Versandkontrolle

- **Doppelversand** vermeiden (mit `letzte-karte`-Eintrag).
- **Verstorbene Empfänger** entfernen.
- **Mandate beendet im Streit** ggf. entfernen.
- **Widerspruch** dauerhaft beachten.

## Datenschutz

- Erläuterung im Mandantenintake auf mögliche Weihnachtsgrüße.
- Widerspruchsrecht jederzeit möglich (Art. 21 DSGVO).
- Löschung auf Widerspruch (Art. 17 DSGVO).

## Ausgabe

- Aktualisierter Verteiler.
- Druckliste (CSV).
- E-Mail-Entwuerfe zur Freigabe.
- Audit mit Versanddatum pro Empfänger.
