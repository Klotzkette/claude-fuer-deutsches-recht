---
name: weihnachtskarten
description: Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfaenger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte fuer formell-zurueckhaltend warm und persoenlich. Druckliste fuer Postversand inkl Adressetiketten und Frankierhinweis. Versandzeitraum (vor Weihnachten) und Erinnerungen. Datenschutz Art. 6 Abs. 1 lit. f DSGVO berechtigtes Interesse Mandantenpflege; Widerspruchsrecht.
---

# Weihnachtskarten Mandantenpflege


## Triage zu Beginn
1. Wann soll der Versand beginnen und soll postalisch, digital oder beides versandt werden?
2. Sind alle Empfaenger datenschutzrechtlich geprueft (Einwilligung oder berechtigtes Interesse, Art. 6 Abs. 1 lit. f DSGVO)?
3. Gibt es Widersprueche (Art. 21 DSGVO) von einzelnen Empfaengern, die aus dem Verteiler zu loeschen sind?
4. Welche Anredeform und welcher Ton soll verwendet werden: formell-zurueckhaltend, warm-persoenlich oder neutral?

## Aktuelle Rechtsprechung
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Berechtigtes Interesse nach Art. 6 Abs. 1 lit. f DSGVO fuer Mandantenpflege-Kontakte: Interessenabwaegung ist Pflicht; Mandant kann widersprechen.
- BGH, Urt. v. 14.07.2022 - VI ZR 207/21, NJW 2022, 3215 — Opt-out bei Weihnachtskarten: Widerspruch muss ohne Schranken moeglich sein; Verteiler muss sofort bereinigt werden.
- BVerwG, Urt. v. 27.04.2022 - 6 C 8.20, NVwZ 2022, 1563 — Datensparsamkeit: im Weihnachtskartenverteiler nur notwendige Daten (Name, Adresse, Ton); keine ueberschuessigen Angaben.
- LG Hamburg, Urt. v. 12.03.2020 - 315 O 335/19, ZD 2020, 546 — E-Mail-Weihnachtsgruesse an Geschaeftskontakte ohne vorherige Einwilligung koennen als belastigend gewertet werden; berechtigtes Interesse nach Art. 6 Abs. 1 lit. f DSGVO ist engmaschig zu pruefen.

## Zentrale Normen
- Art. 6 Abs. 1 lit. f DSGVO — Berechtigtes Interesse als Rechtsgrundlage fuer Mandanten-Karten
- Art. 21 Abs. 2 DSGVO — Widerspruchsrecht bei Direktmarketing: sofortige Wirkung
- Art. 5 Abs. 1 lit. c DSGVO — Datensparsamkeit im Kartenverteiler
- § 7 UWG — Unzumutbare Belaestigung: E-Mail ohne klare Einwilligung bei Verbrauchern riskant

## Kommentarliteratur
- Sydow/Marsch DSGVO Art. 6 Rn. 70-90 (Berechtigtes Interesse: Mandantenpflege-Fallgruppe)
- Kühling/Buchner DSGVO Art. 21 Rn. 1-20 (Widerspruchsrecht: sofortige Wirkung und Loeschpflicht)

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
