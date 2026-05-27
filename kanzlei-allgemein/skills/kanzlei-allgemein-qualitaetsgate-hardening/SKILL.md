---
name: kanzlei-allgemein-qualitaetsgate-hardening
description: "Haertet Kanzlei-Outputs mit mehrstufigen Qualitaetsgates fuer Anfaenger und Profis. Anwendungsfall Schriftsatz Vertrag oder beA-Versand soll vor Abgang auf Substanz Vollstaendigkeit und Haftungsrisiken geprueft werden. Normen § 51 BRAO Haftung § 43a BRAO Berufspflichten § 130a ZPO formelle Anforderungen. Pruefraster Substanz Beweise Anlagen Fristen Zustaendigkeit Antraege Vollmacht Datenschutz Zitate Versandweg Rechnung offene Risiken. Output Qualitaetsgate-Bericht mit Ampelstatus Maengelliste und Freigabeentscheidung. Abgrenzung zu versand-vor-check (unmittelbarer Pre-Check) und kanzlei-allgemein-schreibcanvas."
---

# Qualitätsgate und Hardening


## Triage zu Beginn
1. Welches Produkttyp soll geprueft werden: Klage, Replik, Antrag, Vertrag, Mandantenbrief, Rechnung oder beA-Versand?
2. Soll der Schnellcheck (nur rote Risiken), Normal- oder Profi-Modus (Taktik, Gegner-Argument, Kosten) eingesetzt werden?
3. Gibt es eine laufende Frist, die den Pruefumfang begrenzt?
4. Soll das Qualitaetsgate-Protokoll als Aktenbestandteil gespeichert werden?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Anwaltliches Qualitaetsgate als Sorgfaltspflicht: erkennbare Schwachstellen im Schriftsatz muessen vor dem Versand behoben werden.
- BVerfG, Beschl. v. 12.01.2016 - 2 BvR 2557/14, NJW 2016, 1155 — Effektive Prozessfuehrung erfordert, dass der Anwalt alle Arguments- und Beweismoeglichkeiten ausschoepft; Qualitaetsgate prueft dies.
- BGH, Urt. v. 29.06.2021 - IX ZR 232/19, NJW 2021, 3112 — Fehlende Beweisangebote in der Klage als Anwaltsfehler: Klaeger verliert bei mangelhafter Beweispraesentation auch begruendete Ansprueche.
- BGH, Urt. v. 26.10.2015 - II ZR 404/13, NJW 2016, 311 — Zitierprüfung als Teil anwaltlicher Sorgfalt: falsch zitierte Entscheidungen koennen Gegner und Gericht die Argumentation untergraben.

## Zentrale Normen
- § 43 BRAO — Sorgfaltspflicht: Qualitaetssicherung als Grundpflicht vor jedem Ausgang
- § 130 ZPO — Inhalt von Schriftsaetzen: Antraege und Begruendung muessen vollstaendig sein
- § 253 Abs. 2 ZPO — Klageschrift: Vollstaendigkeitspflicht bei Antraegen und Tatsachen
- § 51 BRAO — Haftung bei erkennbar lueckenhaftem oder fehlerhaftem Schriftsatz

## Kommentarliteratur
- Zöller/Greger ZPO §§ 130, 253 Rn. 1-25 (Anforderungen an Inhalt und Vollstaendigkeit)
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Sorgfaltspflicht bei Schriftsatzgestaltung und -pruefung)

## Zweck

Dieser Skill ist die letzte und wiederholbare Prüfstation für Kanzlei-Outputs. Er soll Anfänger auffangen und Profis nicht ausbremsen. Er prüft nicht abstrakt, sondern entlang des konkreten Produkts: Klage, Replik, Antrag, Vertrag, Mandantenbrief, Rechnung, beA-Versand, Handelsregisterabruf oder interne Entscheidung.

## Moduswahl

Zu Beginn anbieten:

1. `Schnellcheck`: nur rote Risiken und fehlende Pflichtpunkte.
2. `Normal`: Substanz, Beweise, Anlagen, Fristen, Versand.
3. `Profi`: zusätzlich Taktik, Gegenargumente, Zitierprüfung, Anlagenlogik, Kosten und Folgeprozesse.

## Allgemeine Gates

- Ziel und Adressat klar.
- Akte und Aktenzeichen korrekt.
- Sachverhalt mit Datum, Beteiligten und Quelle.
- Rechtliche Grundlage benannt.
- Antrag oder gewünschtes Ergebnis konkret.
- Beweis- und Glaubhaftmachungsmittel zugeordnet.
- Anlagen nummeriert und erwähnt.
- Fristen und Zustellung geprüft.
- Vollmacht, Signatur und Vertretung geprüft.
- Datenschutz und Mandatsgeheimnis geprüft.
- Kosten, Rechnung oder Zeitnarrativ vorgemerkt.
- Versandweg und Protokoll vorbereitet.
- Offene Risiken sichtbar.

## Stop-, Warn- und Durchlauf-Logik

Das Gate darf nicht alles gleich behandeln. Immer eine Einstufung ausgeben:

- `STOPP`: Ausgabe oder Versand wäre fachlich, fristlich, berufsrechtlich oder technisch gefährlich. Beispiel: falsche Partei, fehlender Antrag, ungeprüfte Frist, fehlende Vollmacht, ungeklärter beA-Versand.
- `WARNUNG`: Entwurf ist nutzbar, aber mit sichtbarem Risiko. Beispiel: Anspruchsgrundlage noch unsicher, Anlage fehlt, Streitwert nur geschätzt, Zustelladresse ungeprüft.
- `DURCHLAUF`: Output ist für den gewählten Arbeitsstand plausibel. Offene Punkte sind dokumentiert und nicht versandkritisch.

Für das Kommandocenter zusätzlich mappen:

- `STOPP` = Ampel `ROT`.
- `WARNUNG` = Ampel `GELB`.
- `DURCHLAUF` = Ampel `GRÜN`.

Bei `STOPP` höchstens drei konkrete Rettungsschritte nennen und keinen scheinbar fertigen Versand vorschlagen.

## Produktspezifische Pflichtgates

### Klage, Replik, Antrag

- Antrag vollstreckungsfähig oder bewusst als Entwurf markiert.
- Zuständigkeit, Frist und Streitwert geprüft.
- Rubrum mit Partei, Rechtsform, Vertreter und Anschrift geprüft.
- Anspruchsgrundlage, Tatsachen, Subsumtion und Beweise getrennt.
- Darlegungs- und Beweislast geprüft.
- Anlagen im Text erwähnt und im Anlagenverzeichnis geführt.
- Bei Replik: jeder erhebliche Gegenvortrag einzeln beantwortet.
- beA-Dateien, Signatur, Vollmacht und Versandprotokoll geprüft.

### Vertrag

- Parteien und Vertretung gegen Handelsregister oder Aktenquelle geprüft.
- Leistung, Gegenleistung, Fälligkeit und Laufzeit konkret.
- Haftung, Datenschutz, Vertraulichkeit, Berufsgeheimnis und IP bewusst geregelt.
- Kündigung, Leistungsstörung, Datenherausgabe und Nachvertragliches geregelt.
- Anlagen und Rangfolge der Vertragsdokumente festgelegt.
- Verhandlungspunkte und rote Linien sichtbar.

### Rechnung, E-Rechnung und Buchhaltung

- Leistungszeitraum, Steuersatz, Pflichtangaben und Rechnungsempfänger geprüft.
- GoBD-Änderungsprotokoll angelegt.
- XRechnung oder ZUGFeRD nur als technische Struktur ausgeben, wenn Daten vollständig sind.
- Zahlung, offener Posten und Konto-Matching vorbereitet.

## Anfänger-Auffangmodus

Wenn der Nutzer unsicher oder unsortiert arbeitet:

- Nicht bremsen.
- Erst eine brauchbare Struktur erzeugen.
- Fehlendes als kleine Checkliste darstellen.
- Maximal drei nächste Schritte anbieten.
- Formulierungsbausteine statt langer Theorie liefern.

## Profi-Modus

Wenn der Entwurf bereits gut ist:

- Gegenargumente antizipieren.
- Darlegungs- und Beweislast prüfen.
- Antragsfassung zuspitzen.
- Anlagenreihenfolge und Querverweise prüfen.
- Kosten- und Fristrisiken markieren.
- Stil verdichten.

## Ausgabeformat

Immer kurz und handlungsorientiert:

1. Status: `STOPP`, `WARNUNG` oder `DURCHLAUF`.
2. Die drei wichtigsten Befunde.
3. Nächste konkrete Schritte.
4. Offene Fragen, nur soweit nötig.
5. Verweis auf den passenden Folge-Skill.

## Ausgabe

`assets/templates/qualitaetsgate-checkliste.md` verwenden.
