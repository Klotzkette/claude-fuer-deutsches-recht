---
name: vaf-altvertrag-nachziehen
description: "Altvertrag auf neue Vorlage nachziehen und aktualisieren: Anwendungsfall bestehendes Vertragsverhältnis soll auf neue Vertragsvorlage überführt werden wegen Parteienwechsel, aktualisierter Klauseln oder Gesetzesänderungen. §§ 305 ff. BGB AGB-Recht, § 622 BGB bei Arbeitsverträgen. Pruefraster Parteienänderungen erkennen, veraltete Klauseln identifizieren, Altlasten markieren, Gesetzesänderungen seit Vertragsschluss einpflegen. Output aktualiserter Vertragsentwurf mit Änderungsprotokoll und offenen Punkten. Abgrenzung zu Template-Erkennung fuer neue Vorlagen und zu Redline-QA."
---

# Altvertrag nachziehen


## Triage zu Beginn

1. Handelt es sich um ein deutsches oder grenzüberschreitendes Vertragsverhältnis?
2. Ist der Altvertrag noch vollständig gültig oder sind Änderungsvereinbarungen eingeflossen?
3. Welche Parteien haben seit dem Altvertrag gewechselt (Firmen, Kontaktpersonen)?
4. Gibt es gesetzliche Neuregelungen seit Abschluss des Altvertrags (z.B. Mietrecht, AGB-Recht)?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 09.01.2002 - VIII ZR 304/00, NJW 2002, 1651 — Bestätigungsschreiben mit abweichenden AGB-Klauseln: schweigendes Einverständnis des Kaufmanns kann Geltung der Klauseln bewirken; prüfe Altvertrag auf solche Konstellationen.
- BGH, Urt. v. 25.04.2018 - VIII ZR 176/17, NJW 2018, 2113 — Mieterhöhungsklausel in Altmietvertrag: Indexklausel muss transparenten Berechnungsmaßstab enthalten (§ 307 BGB); alte Formulierungen oft unwirksam.
- BGH, Urt. v. 17.03.2015 - II ZR 15/14, NJW 2015, 2041 — Altvertragsklauseln die nach Gesetzesänderung (z.B. Schuldrechtsreform 2002) obsolet wurden, sind nach neuem Recht auszulegen.
- BGH, Urt. v. 23.01.2003 - VII ZR 210/01, NJW 2003, 1805 — Fortgelten von AGB bei Vertragsverlängerung: Die ursprünglich vereinbarten AGB gelten auch bei stillschweigender Verlängerung fort.

## Zentrale Normen

- § 305, 305c BGB — Einbeziehung und Auslegung von AGB
- § 307 ff. BGB — AGB-Inhaltskontrolle (Generalklausel, Verbotslisten)
- § 550 BGB — Schriftformgebot bei langfristigen Mietverträgen (mehr als 1 Jahr)
- § 195 BGB — Verjährung (regelmäßig 3 Jahre)
- § 313 BGB — Störung der Geschäftsgrundlage (bei wesentlich veränderten Umständen)

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, § 305 Rn. 50-80 (AGB Einbeziehung und Kollision)
- MüKo-BGB/Basedow, 9. Aufl. 2022, § 307 Rn. 1-50 (Inhaltskontrolle)
- Schmidt-Futterer, Mietrecht, 15. Aufl. 2022, § 535 Rn. 1-30 (Mietvertragsinhalte)

## Aufgabe

Der Skill macht aus alten Verträgen neue Entwürfe. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Alten Vertrag als Datenquelle, nicht als unkritische Wahrheit behandeln.
2. Übernommene Werte mit Quelle und Vertrauensgrad markieren.
3. Altklauseln, die nicht zur neuen Vorlage passen, als Review-Punkt ausgeben.
4. Bei Konflikten zwischen Altvertrag und neuer Vorlage nachfragen.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.
