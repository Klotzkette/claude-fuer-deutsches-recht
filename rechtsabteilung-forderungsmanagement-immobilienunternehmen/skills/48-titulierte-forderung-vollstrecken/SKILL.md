---
name: 48-titulierte-forderung-vollstrecken
description: "Verwenden nach vorhandenem Urteil, Vergleich, Vollstreckungsbescheid oder KFB, wenn eine konkrete Vollstreckungsmaßnahme vorbereitet werden soll. Prüft Titel, Klausel, Zustellung, Restforderung, Zinsen und Kosten und strukturiert Gerichtsvollzieherauftrag, Vermögensauskunft oder PfÜB. Bei unbekannter Bank oder Arbeitgeber danach Skill 49."
---

# Titulierte Forderung vollstrecken

## Zweck und Anwendungsfall

Dieser Skill setzt nach Titelgewinn an: Zahlungstitel, Räumungstitel oder Kostenfestsetzungsbeschluss werden in einen vollstreckbaren Arbeitsauftrag übersetzt.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Titel mit Tenor.
- Klausel, Zustellung oder elektronische Nachweise.
- Forderungsberechnung mit Zinsen.
- Schuldnerdaten.
- Information zu Insolvenz, Ratenzahlung, Schonfristzahlung oder Zahlung nach Titel.
- Geplantes Auftrags- oder Antragsdatum, tatsächliche Einreicherrolle und verfügbarer elektronischer oder schriftlicher Weg.

## Ablauf / Checkliste

1. Titelart und Vollstreckungsvoraussetzungen prüfen: positiver Leistungsinhalt, vorläufige Vollstreckbarkeit oder Rechtskraft, richtige Gläubiger-/Schuldneridentität, Klauselbedarf oder gesetzliche klausellose Ausnahme, Zustellung und besondere Bedingungen. Urteil, Vergleich, Vollstreckungsbescheid und KFB haben nicht automatisch dieselben Klauselanforderungen.
2. Hauptforderung, Kosten, Zinsen und Zahlungen je Titel getrennt aktualisieren.
3. Vollstreckungsziel bestimmen: Zahlung, Räumung, Vermögensauskunft, Kontopfändung.
4. Normstichtagskarte vor der Wegwahl schließen: tatsächliches Auftrags- oder Antragsdatum, an diesem Tag geltende ZPO-Fassung, Einreicherrolle, Übermittlungsweg und Formularstand. Bis einschließlich 30.09.2026 dürfen die Erleichterungen des Gesetzes zur weiteren Digitalisierung der Zwangsvollstreckung nicht angewendet werden. Ab 01.10.2026 sind Paragrafen 754a und 829a ZPO live zu öffnen; erst dann dürfen elektronische Übertragungen von Titel, Klausel und weiteren Urkunden mit Übereinstimmungs- und Forderungsbestandsversicherung genutzt werden.
5. Gerichtsvollzieherauftrag oder PfÜB-Vorbereitung strukturieren.
6. Rollenfalle ab 01.10.2026 vermeiden: Die Vollmachts- und Geldempfangsvollmachtsversicherung nach Paragrafen 752a und 753a ZPO nennt nicht Beschäftigte nach Paragraf 79 Abs. 2 S. 2 Nr. 1 ZPO. Für die Renofa der privaten Konzerngesellschaft bleibt daher der konkret erforderliche Vollmachtsnachweis zu prüfen. Auch Paragraf 753 Abs. 4 ZPO begründet nicht allein wegen der privaten GmbH-Rechtsform eine elektronische Nutzungspflicht.
7. Datenschutz und Zweckbindung beachten.
8. Monitoring in Skill `50-vollstreckungsakte-monitoring` anlegen.
9. Vollstreckungskosten nach Paragraf 788 ZPO gesondert erfassen.
10. Bei Räumungstiteln Skill `25` und `26` für Frist, Schutzantrag und Berliner Modell einbeziehen.
11. Allgemeines Startgate nach Paragraf 750 ZPO dokumentieren: namentlich bezeichnete Parteien und bereits erfolgte oder gleichzeitige Zustellung des Titels; bei qualifizierter Klausel zusätzlich deren Zustellung samt erforderlichen Urkunden. Kalenderbedingungen und Sicherheitsleistung nach Paragraf 751 ZPO, vorläufige Vollstreckbarkeit und Schutzanordnungen nach Paragrafen 708 bis 711 ZPO sowie besondere Wartefristen vor Auftragserteilung gesondert prüfen.
12. Bei Insolvenz oder vorläufigem Vollstreckungsverbot stoppen und Skill `08-eskalation-an-anwalt` einschalten.
13. Teilzahlungen nach Tilgungsbestimmung auswerten. Reicht eine Zahlung für mehrere titulierte Forderungen oder Titel nicht aus, zuerst Paragraf 366 BGB anwenden; innerhalb der ausgewählten Schuld gilt grundsätzlich die Reihenfolge Kosten, Zinsen, Hauptleistung nach Paragraf 367 BGB. Titeltenor, wirksame Tilgungsbestimmung, Vergleich und Insolvenzlage gehen einer schematischen Verrechnung vor.
14. PfÜB nur mit korrektem Vollstreckungsgericht, Drittschuldnerdaten, Forderungsaufstellung und Datenschutzvermerk vorbereiten. Ab 01.10.2026 verlangt der elektronische Weg nach Paragraf 829a ZPO zusätzlich Übereinstimmungs- und Bestandsversicherung sowie bei Vollstreckungskosten eine nachprüfbare Aufstellung mit Belegen; spätere Urkundenänderungen sind unverzüglich mitzuteilen. PDF/XML nach Paragraf 829 Abs. 5 ZPO ist erst ab 01.01.2027 freigegeben.
15. Vollstreckung nur aus positivem, vollstreckbarem Tenor starten; bei abweisendem oder teilweise abweisendem Urteil Unterliegensanteil abtrennen.
16. Bei unklarem Titelumfang, Teilunterliegen, Rechtsmittelfrist oder fehlender Klausel rote Ampel setzen und Skill `08-eskalation-an-anwalt` einbeziehen.
17. Bei einem nicht auf das Urteil gesetzten Kostenfestsetzungsbeschluss die Zweiwochenfrist nach Paragraf 798 ZPO ab Zustellung einhalten. Diese Wartefrist nicht pauschal auf alle Titel übertragen.
18. Statusleiter vor jeder Maßnahme ausgeben: KFA noch offen -> Skill `46`; KFB ungeprüft -> Skill `47`; positiver Titel und titelartspezifische Startvoraussetzungen erfüllt -> Skill `48`; Konten oder Drittauskünfte erforderlich -> Skill `49`; Wiedervorlagen und Ratenüberwachung -> Skill `50`.
19. Getrennte Freigabekarte erstellen: positiver Tenor, Titelart und -version, Rechtskraft/vorläufige Vollstreckbarkeit, Klauselbedarf, Zustellung, Bedingung/Sicherheit, Wartefrist, Hauptforderung, Zinsen, Kosten, Zahlungen, Tilgung, Vollstreckungsziel, Schuldner- und Drittschuldnerdaten, Normstichtag, Einreicherrolle, Übermittlungsweg, Insolvenzstopp, Auftrag und Freigabeperson. Status bis zur realen Freigabe `ENTWURF - NICHT VERSENDEN/EINREICHEN`.

## Argumentationsstandard

Der Vollstreckungsauftrag leitet jede Maßnahme aus einem genau bezeichneten positiven Tenor ab. Titel, Klausel oder Ausnahme, Zustellung, Bedingung, Wartefrist, aktueller Forderungsstand und Maßnahme stehen in einer durchgehenden Kette; mehrere Titel erhalten getrennte Konten. Vermutete Bank-, Arbeitgeber- oder Vermögensdaten werden als unbestätigte Ermittlungsansätze gekennzeichnet und nicht als feststehende Drittschuldnerangabe verwendet. Es gilt `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert. Für alle ab 2026 datierten Aufträge gilt zusätzlich die Stichtagsmatrix in `references/rechtsstand-2026-verfahren-vollstreckung.md`.

ZPO-Zwangsvollstreckung insbesondere mit Paragrafen 704, 724, 750, 751 und titelartspezifischen Ausnahmen, Paragrafen 366 und 367 BGB und Insolvenzstopp mit Normanker. Keine unzulässigen Ermittlungswege empfehlen.

## Ausgabeformat

Getrennte interne Freigabekarte, titelartspezifisches Startgate, Vollstreckungsauftrag, Forderungsaufstellung je positivem Titel, Kostenupdate, Tilgungsjournal, Anlagenliste, Datenschutzvermerk, Unterliegenssperre und Monitoringhinweise. Alles ausformuliert.

## Beispiele

- Urteil über Mietrückstand: Zahlungsbeitreibung und Vermögensauskunft.
- KFB: Kostenforderung separat vollstrecken.
- Teilabweisung im Urteil: nur positiven Tenor vollstreckbar vorbereiten, Unterliegensanteil an Skill 08.
- Elektronischer Gerichtsvollzieherauftrag am 20.09.2026: neue Paragraf-754a-Erleichterung noch nicht anwenden; Auftrag am 02.10.2026 nur nach live geprüftem Norm-, Rollen- und Formularstand.
