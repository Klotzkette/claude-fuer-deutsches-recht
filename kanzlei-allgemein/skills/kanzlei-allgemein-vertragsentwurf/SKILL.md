---
name: kanzlei-allgemein-vertragsentwurf
description: "Erstellt Vertragsentwuerfe aus Term Sheet Mandantenangaben oder Vorlagen fuer jede Vertragsart. Anwendungsfall Mandant braucht Vertragsentwurf und Ausgangsmaterial liegt als Term Sheet Stichpunkte oder Muster vor. Normen §§ 305 ff. BGB AGB-Kontrolle § 134 BGB Gesetzesverstoesse § 311 BGB vorvertragliche Pflichten. Pruefraster Parteien Vertretung Handelsregister Leistungsbild Verguetung Laufzeit Haftung Datenschutz Anlagen Verhandlungspunkte. Output Kommentierter Vertragsentwurf mit Risikomarkierungen offenen Verhandlungspunkten und Qualitaetsgate-Freigabe. Abgrenzung zu vertragsausfueller-Plugin (ausfuellen bestehender Vorlagen) und kanzlei-allgemein-schriftsatz-turbo."
---

# Vertragsentwurf und Vertrags-Canvas


## Triage zu Beginn
1. Welcher Vertragstyp ist gefragt: Dienstleistung, Mandat, NDA, SaaS, Werkvertrag, Miet- oder Kooperationsvertrag?
2. Wer sind die Vertragsparteien und liegen Vertretungsnachweise vor (HR-Auszug, Vollmacht)?
3. Ist eine Partei Verbraucher (§ 13 BGB) oder durchgaengig B2B — wegen AGB-Kontrolle und Widerrufsrecht?
4. Gibt es Haftungsobergrenzen, Datenschutzklauseln (Art. 28 DSGVO AVV) oder IP-Regelungen, die benoetigt werden?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 25.11.2009 - VIII ZR 318/08, NJW 2010, 1061 — AGB-Unklarheitenregel § 305c Abs. 2 BGB: zweideutige Klauseln gehen zu Lasten des Verwenders; Vertragsentwurf muss eindeutig sein.
- BGH, Urt. v. 06.11.2013 - KZR 58/11, NJW 2014, 1230 — Haftungsfreizeichnung in B2B-Vertrag: AGB-Klausel zur Haftungsbegrenzung auf grobe Fahrlassigkeit ist zulässig, bei Vorsatz unwirksam (§ 309 Nr. 7 BGB).
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Auftragsverarbeitungsklausel nach Art. 28 DSGVO als Pflichtbestandteil, wenn personenbezogene Daten verarbeitet werden; fehlende AVV-Klausel begründet DSGVO-Verstoß.
- BGH, Urt. v. 16.01.2009 - V ZR 133/08, NJW 2009, 1061 — Auslegung nach §§ 133, 157 BGB: objektiver Empfaengerhorizont als Massstab; Vertragsentwurf muss aus Empfaengerperspektive klar sein.

## Zentrale Normen
- §§ 305-310 BGB — AGB-Recht: Einbeziehung, Inhaltskontrolle, Klauselverbote
- § 13 BGB — Verbraucher: hoehere Schutzstandards und Widerrufsrecht (§§ 355 ff. BGB)
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag: Pflichtbestandteil bei Datenweitergabe
- § 631 ff. BGB — Werkvertrag; § 611 ff. BGB — Dienstvertrag: Grundtypen-Abgrenzung

## Kommentarliteratur
- Grüneberg/Grüneberg BGB §§ 305-310 Rn. 1-80 (AGB: Kontrolle und Klauselverbote)
- MüKoBGB/Basedow §§ 305-310 Rn. 1-100 (AGB-Recht: Systematik und Fallgruppen)

## Zweck

Dieser Skill erzeugt schnell einen brauchbaren Vertragsentwurf oder eine Vertragsstruktur. Er hilft bei Dienstleistungsvertrag, Mandatsvereinbarung, NDA, SaaS, Kauf, Werkvertrag, Miet- oder Kooperationsvertrag. Er ist bewusst playbook-orientiert: erst die wirtschaftliche Logik, dann die Klauseln.

## Schnellstart

1. Vertragstyp.
2. Parteien und Vertretung.
3. wirtschaftliches Ziel.
4. Leistung oder Gegenstand.
5. Preis, Honorar, Vergütung.
6. Laufzeit und Kündigung.
7. Haftung und Gewährleistung.
8. Datenschutz, Vertraulichkeit, IP.
9. Anlagen und Nachweise.
10. Verhandlungsspielraum.

## Produktionspfade

### Vertragsentwurf aus Stichworten

1. Wirtschaftliches Ziel in einem Absatz festhalten.
2. Parteien und Vertretung prüfen.
3. Leistungsbild als Anlage oder Klauselstruktur formulieren.
4. Zahlungslogik, Fälligkeit und Laufzeit festziehen.
5. Risiken in Verhandlungspunkte und rote Linien trennen.
6. Entwurf mit TODOs statt erfundenen Details ausgeben.

### Vertragsentwurf aus Term Sheet

1. Term Sheet in Klauselbereiche zerlegen.
2. Widersprüche markieren.
3. Offene Punkte in eine Verhandlungsliste überführen.
4. Vertragsrangfolge festlegen: Hauptvertrag, Anlagen, AGB, Leistungsbeschreibung.

### Vertragsprüfung

1. Abweichungen vom Mandantenziel markieren.
2. Einseitige Klauseln benennen.
3. Fehlende Klauseln ergänzen.
4. Handlungsvorschläge als `akzeptieren`, `ändern`, `verhandeln`, `ablehnen` ausgeben.

## Handelsregister-Verknüpfung

Bei Unternehmen immer prüfen, ob `kanzlei-allgemein-handelsregisterabruf` nötig ist:

- Firma, Rechtsform, Sitz.
- Registergericht und Registernummer.
- Vertretungsberechtigte Personen.
- Prokura.
- aktuelle Gesellschafterliste oder Satzung, wenn relevant.

Wenn kein echter Abruf möglich ist, Simulation anbieten und deutlich als Simulation kennzeichnen. Keine Registerdaten erfinden, ohne sie als Platzhalter zu markieren.

## Vertrags-Hardening

Vor Ausgabe prüfen:

- Parteien korrekt.
- Vertretung plausibel.
- Leistungsbeschreibung konkret.
- Zahlungs- und Fälligkeitslogik klar.
- Leistungsstörung geregelt.
- Haftungsbegrenzung bewusst.
- Datenschutz und Vertraulichkeit passend.
- Anlagen referenziert.
- Schriftform, Textform und elektronische Signatur bewusst gewählt.
- Gerichtsstand, Rechtswahl und salvatorische Klausel nicht blind übernommen.

## Anfängerführung

- Keine Vertragsdogmatik ausbreiten, wenn der Nutzer nur schnell einen Entwurf braucht.
- Stattdessen die nächste Klausel vorschlagen und erklären, warum sie gebraucht wird.
- Unsichere Punkte als freundliche Rückfrage formulieren.
- Bei riskanten Klauseln eine einfache Ampel ausgeben: grün, gelb, rot.

## Profi-Härtung

- Rangfolge der Dokumente sauber regeln.
- Leistungsstörungen, Change Requests, Abnahme und Exit-Szenarien konkretisieren.
- Haftungsbegrenzung auf Vorsatz, grobe Fahrlässigkeit, Kardinalpflichten, Datenverlust und Berufsgeheimnisse prüfen.
- Datenschutz, TOM, Unterauftragnehmer und Löschung als Anlagenlogik führen.
- Verhandlungsspielräume mit konkreten Formulierungsvorschlägen ausgeben.

## Ausgabe

- `assets/templates/vertragsentwurf-playbook.md`.
- `assets/templates/vertragsrisiken-matrix.md`.
- Danach `kanzlei-allgemein-qualitaetsgate-hardening`.
