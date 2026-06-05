---
name: bautraeger-mabv-grundlagen-ratenplan
description: "Bautraeger Mabv Grundlagen Ratenplan: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bautraeger Mabv Grundlagen Ratenplan

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Bautraeger Mabv Grundlagen Ratenplan** im Plugin Fachanwalt Bau- und Architektenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bautraeger-mabv-grundlagen-1-2` | Makler- und Bautraegerverordnung (MaBV) Grundlagen. Skill behandelt das Anwendungsfeld der MaBV §§ 1 2 die definition Bautraeger und das Verhaeltnis zur Gewerbeordnung § 34c GewO. Liefert Pruefraster fuer Erwerber. |
| `bautraeger-mabv-ratenplan-3-mabv` | MaBV § 3 Ratenplan — 7 Raten nach Baufortschritt. Skill listet die einzelnen Raten in Prozent abhaengig vom Baufortschritt erkennt unzulaessige Vorausleistungen und gibt Tipps zur Pruefung. Liefert exakten Pruefraster. |
| `bautraeger-mabv-sicherheit-2-buergschaft` | MaBV § 2: Sicherheit fuer Vorausleistungen durch Buergschaft. Skill klaert die alternative Sicherheitsleistung statt Ratenzahlung nach Baufortschritt die Anforderungen an die Buergschaft (selbstschuldnerisch unbedingt unbefristet) und die Folgen ungueltiger Sicherheiten. Liefert Pruefraster. |
| `bautraeger-mabv-vermoegenstrennung` | MaBV Vermoegenstrennung — Bautraeger muss die Gelder der Erwerber separiert vom eigenen Vermoegen behandeln. Skill klaert die Trennungspflicht das Sonderkonto und die Folgen bei Vermischung Insolvenzrechtlich. Liefert Pruefraster. |

## Arbeitsweg

Im Plugin Fachanwalt Bau- und Architektenrecht gilt für **Bautraeger Mabv Grundlagen Ratenplan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bautraeger-mabv-grundlagen-1-2`

**Fokus:** Makler- und Bautraegerverordnung (MaBV) Grundlagen. Skill behandelt das Anwendungsfeld der MaBV §§ 1 2 die definition Bautraeger und das Verhaeltnis zur Gewerbeordnung § 34c GewO. Liefert Pruefraster fuer Erwerber.

# Bautraeger Mabv Grundlagen 1 2

## Anwendungsbereich

§ 1 MaBV: Die MaBV gilt fuer Gewerbetreibende mit Erlaubnis nach § 34c Abs. 1 GewO — Bautraeger sind erfasst nach § 34c Abs. 1 Satz 1 Nr. 4 GewO (Bauvorhaben als Bautraeger oder Baubetreuer).

## Bautraegerdefinition

Bautraeger ist, wer wirtschaftlich auf eigene Rechnung Bauvorhaben fuer fremde Rechnung durchfuehrt. Typisch: Erwerb des Grundstuecks im eigenen Namen, Bau, Verkauf von Wohnungs- oder Teileigentum an Endkunden.

## Verhaeltnis Bautraeger vs. Generaluebernehmer

- Bautraeger: verkauft an Erwerber, der danach Eigentuemer wird.
- Generaluebernehmer: fuehrt Bauvorhaben fuer fremden Auftraggeber durch, der bereits Eigentuemer ist.
- Wichtig: nur fuer Bautraeger gilt § 3 MaBV — der zentrale Erwerberschutz.

## Pruefraster fuer Erwerber

1. Ist der Vertragspartner ein Bautraeger im Sinne § 34c GewO?
2. Hat er eine gueltige Erlaubnis?
3. Bewerbung als "Bautraeger" oder Tarnung als "Baubetreuung" / "GU"?
4. Welche Schutzvorschriften greifen?

## Aktuelle BGH-Linie

- BGH-Linie staendige Rspr.: Verstoss gegen MaBV macht Klausel oder Zahlungsverlangen unwirksam — Erwerber kann zurueck.
- BGH-Az im Mandat live verifizieren.

## 2. `bautraeger-mabv-ratenplan-3-mabv`

**Fokus:** MaBV § 3 Ratenplan — 7 Raten nach Baufortschritt. Skill listet die einzelnen Raten in Prozent abhaengig vom Baufortschritt erkennt unzulaessige Vorausleistungen und gibt Tipps zur Pruefung. Liefert exakten Pruefraster.

# Bautraeger Mabv Ratenplan 3 Mabv

## Norm

§ 3 Abs. 2 MaBV: Maximal 7 Teilzahlungen nach Baufortschritt. Genauer Ratenkatalog vor Anwendung live verifizieren (juristische Stoffsammlung); typischerweise sieht der Katalog folgende Stufen vor:

- 30 % nach Beginn der Erdarbeiten.
- 28 % nach Rohbaufertigstellung einschliesslich Zimmererarbeiten.
- 5,6 % nach Herstellung der Dachflaechen und Dachrinnen.
- 2,1 % nach Rohinstallation Heizung.
- 2,1 % nach Rohinstallation Sanitaer.
- 2,1 % nach Rohinstallation Elektro.
- 7 % nach Fenstereinbau, Verglasung.
- 4,2 % nach Innenputz.
- 2,1 % nach Estricharbeiten.
- 2,8 % nach Fliesenarbeiten im Sanitaer.
- 8,4 % nach bezugsfertiger Herstellung und Zug-um-Zug-Uebergabe.
- 2,1 % nach Fassade.
- 3,5 % nach vollstaendiger Fertigstellung.

Summen koennen je nach Fassung der MaBV abweichen — Vor Mandatsmaessigen Beratung im aktuellen Gesetzestext im Detail pruefen.

## Verbot Vorausleistung

- Bautraeger darf nur Zahlungen nach Erreichen der jeweiligen Stufe verlangen.
- Vorausleistung ohne Sicherung ist nichtig.

## BGH-Linie

- BGH staendige Rspr.: zu hohe Raten oder vorgezogene Zahlung machen Klausel unwirksam.
- Erwerber kann zurueckhalten / zurueckfordern.

## Pruefraster

1. Welcher Stand?
2. Welche Rate verlangt?
3. Stand belegbar (Architektenbestaetigung, Photo)?
4. Hoehe rechtmaessig?

## Werkzeug Photo-Tagebuch

- Erwerber empfohlen: bei jedem Bauabschnitt eigene Fotos mit Datum und GPS.
- Wichtig fuer Beweisfuehrung.

## 3. `bautraeger-mabv-sicherheit-2-buergschaft`

**Fokus:** MaBV § 2: Sicherheit fuer Vorausleistungen durch Buergschaft. Skill klaert die alternative Sicherheitsleistung statt Ratenzahlung nach Baufortschritt die Anforderungen an die Buergschaft (selbstschuldnerisch unbedingt unbefristet) und die Folgen ungueltiger Sicherheiten. Liefert Pruefraster.

# Bautraeger Mabv Sicherheit 2 Buergschaft

## Norm

§ 2 MaBV (in Verbindung mit § 7 MaBV): Bautraeger kann statt Zahlung nach Baufortschritt (§ 3 MaBV) eine **Sicherheit** in Hoehe der gesamten Vertragssumme stellen. Erwerber zahlt dann gegen die Sicherheit.

## Anforderungen Buergschaft

- Selbstschuldnerisch.
- Unbedingt — keine Bedingungen, Einreden ausgeschlossen.
- Unbefristet (oder mit ausreichend langer Frist).
- Aussteller: Kreditinstitut oder Versicherer mit Sitz / Niederlassung im EWR.
- Verzicht auf Einreden nach §§ 770 771 BGB.

## Bestaetigung

- Originalbuergschaft an Erwerber ausgehaendigt.
- Pruefen: Vollstaendigkeit Wortlaut Auszahlung.

## Verstoss

- Sicherheit fehlt oder ist unzureichend = Vorausleistung unrechtmaessig.
- Erwerber kann zurueckhalten.

## Praxistipp

- Konkret pruefen: Wer ist Versicherer / Bank? Bonitaet?
- Inkraftsetzung der Buergschaft mit Vertragsunterzeichnung.

## Pruefraster

1. Buergschaft vorhanden?
2. Aussteller bonitaet?
3. Wortlaut korrekt (selbstschuldnerisch unbedingt unbefristet)?
4. Hoehe = Vertragssumme?
5. Vorlage an Erwerber?

## 4. `bautraeger-mabv-vermoegenstrennung`

**Fokus:** MaBV Vermoegenstrennung — Bautraeger muss die Gelder der Erwerber separiert vom eigenen Vermoegen behandeln. Skill klaert die Trennungspflicht das Sonderkonto und die Folgen bei Vermischung Insolvenzrechtlich. Liefert Pruefraster.

# Bautraeger Mabv Vermoegenstrennung

## Pflicht zur Vermoegenstrennung

§§ 3-8 MaBV: Bautraeger darf Erwerbergelder nur fuer das jeweilige Bauvorhaben verwenden. Trennung von eigenen Geldern ist Schutz vor Vermoegensvermischung.

## Sonderkonto

- Praxis: Eigene Konten pro Bauvorhaben.
- Aufzeichnungspflicht nach § 10 MaBV.

## Insolvenzschutz

- Bei Insolvenz: Erwerbergelder, die zweckgebunden gehalten wurden, sollen Erwerbern zukommen.
- Aber: keine echte Treuhand. Bei Vermischung Insolvenzmasse — Erwerber verlieren ggf.

## Praxis

- Mit Sicherungsmodell § 7 MaBV (gestelle Buergschaft) ist Vermoegensvermischung weniger riskant.
- Bei Ratenmodell § 3 MaBV ist Vermoegenstrennung kritisch.

## BGH-Linie

- BGH: Verstoss gegen § 3 MaBV macht Vertragsklausel unwirksam.
- Aktuelle Az im Mandat live verifizieren.

## Pruefraster

1. Welches Modell (§ 3 vs § 7)?
2. Trennung des Sonderkontos belegbar?
3. Bei Insolvenz: Glaeubigeranfechtung?
