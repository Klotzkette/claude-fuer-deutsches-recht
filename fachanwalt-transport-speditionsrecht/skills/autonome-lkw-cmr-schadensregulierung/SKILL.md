---
name: autonome-lkw-cmr-schadensregulierung
description: "Autonome LKW CMR Schadensregulierung im Plugin Fachanwalt Transport Speditionsrecht: prüft konkret Haftung bei autonomen LKW-Konvois nach § 1d StVG analysieren, Schadensregulierung im grenzüberschreitenden Gueterverkehr, Speditionshaftung nach HGB prüfen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Autonome LKW CMR Schadensregulierung

## Arbeitsbereich

**Autonome LKW CMR Schadensregulierung** ordnet den Fall über die tragenden Prüfungslinien: Haftung bei autonomen LKW-Konvois nach § 1d StVG analysieren, Schadensregulierung im grenzüberschreitenden Gueterverkehr, Speditionshaftung nach HGB prüfen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-transport-autonome-lkw-konvois-haftung-1d-stvg` | Haftung bei autonomen LKW-Konvois nach § 1d StVG analysieren: Fahrzeughalterhaftung, KI-Systemfehler. Normen: § 1d StVG, §§ 7 18 StVG, §§ 407 ff. HGB. Prüfraster: Halterhaftung, technisches Versagen, Konvoi-Führer, Regulierung. Output: Haftungsanalyse autonomer LKW. Abgrenzung: nicht klassische Frachtführerhaftung ohne Automatisierung. |
| `fachanwalt-transport-cmr-schadensregulierung` | Schadensregulierung im grenzüberschreitenden Gueterverkehr nach CMR durchführen. Normen: Art. 17 ff. 23 ff. CMR. Prüfraster: Schadensanzeige, Haftungsgrenzen 8.33 SZR je Kilogramm, Schadensberechnung, Fristen. Output: CMR-Schadensregulierungsschreiben. Abgrenzung: nicht nationales HGB-Recht. |
| `fachanwalt-transport-speditionshaftung-hgb` | Speditionshaftung nach HGB prüfen: Fixkostenspediteur, Sammelladungsspediteur, Haftungsgrenzen. Normen: §§ 454 ff. HGB. Prüfraster: Speditionsauftrag, Selbsteintritt, Haftungsregime, ADSP-Klauseln. Output: Speditionshaftungsanalyse. Abgrenzung: nicht Frachtführerhaftung §§ 407 ff. HGB. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-transport-autonome-lkw-konvois-haftung-1d-stvg`

**Fokus:** Haftung bei autonomen LKW-Konvois nach § 1d StVG analysieren: Fahrzeughalterhaftung, KI-Systemfehler. Normen: § 1d StVG, §§ 7 18 StVG, §§ 407 ff. HGB. Prüfraster: Halterhaftung, technisches Versagen, Konvoi-Führer, Regulierung. Output: Haftungsanalyse autonomer LKW. Abgrenzung: nicht klassische Frachtführerhaftung ohne Automatisierung.

### Autonome LKW-Konvois – Haftung § 1d StVG und CMR

## Kernsachverhalt & Mandantenfragen

Platooning – automatisierte LKW-Konvois mit V2V-Kommunikation (Vehicle-to-Vehicle) – ist technisch Realität und rechtlich noch weitgehend ungeklärt. § 1d StVG (eingefügt 2021) schafft einen Rahmen für hochautomatisiertes und vollautomatisiertes Fahren in Deutschland. Die haftungsrechtliche Gemengelage aus StVG (Gefährdungshaftung), Produkthaftungsgesetz (Herstellerhaftung) und CMR (Frachtführerhaftung) erfordert eine sorgfältige Schichtenanalyse.

**8 Kaltstart-Rückfragen:**

1. Auf welcher Automatisierungsstufe (SAE Level 2, 3, 4 oder 5) war das Fahrzeug zum Unfallzeitpunkt?
2. War der autonome Modus aktiviert oder fuhr das Fahrzeug manuell gesteuert?
3. Liegt ein Datenspeicher-Auslesungsprotokoll gemäß § 1g StVG vor (Black-Box-Daten)?
4. Wer war als Technische Aufsicht (Remote-Operator) nach § 1f StVG benannt und hat diese eine Übernahme-Aufforderung erhalten?
5. Welche Fahrzeugmarke und welches Assistenzsystem wurde eingesetzt (Mercedes, MAN, Scania, Volvo, Daimler Truck)?
6. Hat der Hersteller Rückrufe (Recalls) für das betreffende Fahrzeug oder das Assistenzsystem ausgesprochen?
7. War der Transport grenzüberschreitend (CMR anwendbar) oder innerdeutsch (HGB)?
8. Welche Schadensarten sind eingetreten: Personenschaden, Sachschaden an Drittfahrzeug, Ladungsschaden des Auftraggebers?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 1d StVG | Betrieb hochautomatisierter und vollautomatisierter Fahrzeuge; Genehmigungspflicht |
| § 1e StVG | Genehmigungsverfahren beim Kraftfahrt-Bundesamt (KBA) |
| § 1f StVG | Pflichten des Halters: Benennung Technische Aufsicht; Betriebsgebiet; Einsatzbedingungen |
| § 1g StVG | Datenspeicherungspflicht: Black-Box-Mindestdatensatz; Aufbewahrung 6 Monate |
| § 1h StVG | Auskunftspflichten gegenüber Behörden; Unfallmeldung an KBA |
| § 7 StVG | Gefährdungshaftung des Halters; unabhängig von Verschulden und autonomem Modus |
| § 12 StVG | Haftungsbegrenzung: Personenschäden bis 7.5 Mio. EUR; Sachschäden bis 1 Mio. EUR je Ereignis |
| § 18 StVG | Verschuldenshaftung des Fahrers; eingeschränkt bei aktivem autonomen Modus |
| § 1 ProdHaftG | Produkthaftung des Herstellers: verschuldensunabhängig bei Produktfehler |
| § 2 ProdHaftG | Produktbegriff: Hardware und Software als Produkt anerkannt |
| § 3 ProdHaftG | Produktfehler: Sicherheitserwartungen der Allgemeinheit nicht erfüllt |
| § 1 Abs. 2 PflVG | Versicherungspflicht für Kraftfahrzeuge; gilt auch für autonome Fahrzeuge |
| CMR Art. 17 | Frachtführerhaftung: unabhängig von autonomer Steuerung |
| CMR Art. 29 | Qualifiziertes Verschulden: Systemversagen kann Leichtfertigkeit begründen |
| VO (EU) 2022/1426 | Typgenehmigung vollautomatisierter Fahrzeuge (ALKS – Automated Lane Keeping System) |
| VO (EU) 2019/2144 | Allgemeine Sicherheitsanforderungen für Fahrzeuge |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Haftung autonomer LKW-Konvoi

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Automatisierungsstufe ermitteln: SAE Level 2 (Fahrer steuert), 3 (Systemsteuerung, Fahrer verfügbar), 4 (vollautom., kein Fahrer notwendig im Betriebsgebiet) | § 1d StVG |
| 2 | Aktivierungsstatus prüfen: War autonomer Modus zum Unfallzeitpunkt aktiv? Black-Box-Daten auswerten | § 1g StVG |
| 3 | Halterhaftung nach § 7 StVG: immer gegeben bei Betrieb des Fahrzeugs; keine Exkulpation möglich | § 7 StVG |
| 4 | Technische Aufsicht prüfen: § 1f StVG – war sie benannt? Hat sie auf Übergabeanforderung reagiert? | § 1f StVG |
| 5 | Fahrerhaftung § 18 StVG: Bei aktivem autonomen Modus nur bei Verletzung der Übergabepflicht | § 18 StVG |
| 6 | Herstellerhaftung ProdHaftG: Produktfehler Hard-/Software? Rückruf? Sicherheitserwartungen verletzt? | §§ 1–3 ProdHaftG |
| 7 | CMR-Haftung bei grenzüberschreitendem Transport: Frachtführerhaftung bleibt unabhängig vom Automatisierungsgrad | CMR Art. 17 |
| 8 | Datensicherung: § 1g StVG-Daten anfordern; Aufbewahrungsfrist 6 Monate; bei Löschung: Beweislastumkehr | § 1g StVG |
| 9 | V2V-Kommunikation auswerten: Daten zwischen Konvoi-Fahrzeugen bei Hersteller anfordern | VO 2022/1426 |
| 10 | Versicherungsdeckung prüfen: Kfz-Haftpflicht (PflVG) und ggf. Produkthaftpflichtversicherung des Herstellers | § 1 PflVG |
| 11 | Haftungsteilung ermitteln: Halter × Fahrer × Technische Aufsicht × Hersteller; anteilig nach § 254 BGB | § 254 BGB, § 17 StVG |
| 12 | CMR-Regress gegen Hersteller: Frachtführer haftet gegenüber Auftraggeber; Regress gegen Hersteller nach ProdHaftG möglich | CMR Art. 3, §§ 1 ff. ProdHaftG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Haftung autonome LKW-Konvois pruefen | Haftungsgutachten; Template unten |
| Variante A — Versicherungsfall klar | Direktklage gegen Versicherer § 115 VVG |
| Variante B — Herstellerdefekt des Fahrsystems | Produkthaftung § 1 ProdHaftG parallel zur StVG-Haftung |
| Variante C — Grenzueberschreitender Unfall EU | CMR-Haftung pruefen; auslaendisches Unfallort-Recht |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Sicherungsantrag Black-Box-Daten § 1g StVG

```
An das Kraftfahrt-Bundesamt (KBA)
Postfach 1263
38022 Wolfsburg

Anforderung von Datenspeicher-Daten gemäß § 1h StVG

In der Sache Unfall vom [Datum] auf [Straße, Ort]
bitte ich um Beauskunftung folgender Datenspeicherdaten
des Fahrzeugs [Kennzeichen, FIN-Nummer]:

Gemäß § 1g StVG i.V.m. § 1h StVG sind die Daten des
verpflichtenden Datenspeichers für 6 Monate aufzubewahren.

Ich bitte um:
1. Kompletten Datensatz § 1g StVG für Zeitraum [X Stunden]
 vor dem Unfall
2. V2V-Kommunikationsprotokolle des Konvois
3. Systemzustand (autonom / manuell) zum Unfallzeitpunkt
4. Übergabeanforderungen an Fahrer / Technische Aufsicht

Die Daten werden benötigt zur Klärung der Haftungsfrage
nach §§ 7, 18 StVG und § 1d ff. StVG in dem anhängigen
Verfahren [Aktenzeichen / Angaben].

[Ort, Datum]
[Unterschrift, Kanzlei]
```

### Baustein 2 – Klage Halterhaftung + Produkthaftung

```
AN DAS LANDGERICHT [...]

Klägerin: [Geschädigte/r, Anschrift]
Beklagte 1: [Halter des autonomen LKW]
Beklagte 2: [Hersteller des Assistenzsystems / Fahrzeugs]

Streitwert: EUR [Schadenbetrag]

KLAGEBEGRÜNDUNG

I. SACHVERHALT

Am [Datum] ereignete sich auf der [Straße] ein Unfall, bei
dem das autonome Konvoi-Fahrzeug der Beklagten 1 [Kennzeichen]
in das Fahrzeug der Klägerin fuhr.
Das Fahrzeug war auf SAE Level [3/4] eingestellt (Anlage K1:
Black-Box-Auszug). Der autonome Modus war aktiviert.

II. HAFTUNG BEKLAGTE 1 (Halter § 7 StVG)

Die Beklagte 1 haftet als Halterin gemäß § 7 StVG.
Halterhaftung ist unabhängig von Schuld oder Automatisie-
rungsgrad; sie entfällt nur bei höherer Gewalt. Höhere Gewalt
liegt nicht vor.

III. HAFTUNG BEKLAGTE 2 (Produkthaftung § 1 ProdHaftG)

Das Assistenzsystem (ALKS gemäß VO 2022/1426) wies zum
Unfallzeitpunkt einen Fehler im Bereich [Beschreibung] auf.
Dieser Fehler führte zu einer Fehlsteuerung des Fahrzeugs.

Der Fehler begründet ein Produktfehler gemäß § 3 ProdHaftG
da das System hinter den berechtigten Sicherheitserwartungen
der Allgemeinheit zurückbleibt.

Beweis: Sachverständigengutachten ist einzuholen.

IV. SCHADENSHÖHE

[Personenschaden: EUR X]
[Sachschaden Fahrzeug: EUR X]
[Verdienstausfall: EUR X]
[Gesamt: EUR X]

V. ANTRAG

Die Beklagten 1 und 2 werden als Gesamtschuldner verurteilt,
an die Klägerin EUR [Betrag] nebst Zinsen zu zahlen.

[Ort, Datum, Unterschrift]
```

### Baustein 3 – Regress des Frachtführers gegen Hersteller

```
An [Fahrzeughersteller]

Regressforderung nach § 1 ProdHaftG / § 426 BGB

Der Frachtführer [Name] hat gegenüber dem Auftraggeber
[Name] den Ladungsschaden aus dem Unfall vom [Datum]
gemäß CMR Art. 17 reguliert: EUR [Betrag].

Der Schaden wurde verursacht durch einen Fehler des in
dem Fahrzeug [Kennzeichen] eingebauten Assistenzsystems
[Bezeichnung] (Anlage: Sachverständigengutachten).

Wir fordern Sie auf, den regulierten Betrag von EUR [X]
an den Frachtführer zu erstatten (§ 1 ProdHaftG Abs. 3;
§ 426 BGB).

[Ort, Datum, Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Halterhaftung § 7 StVG | Keine Exkulpation möglich; Halter haftet verschuldensunabhängig |
| Fahrerhaftung § 18 StVG | Fahrer muss Verschuldensfreiheit beweisen; bei aktivem autonomem Modus erleichtert |
| Produktfehler § 1 ProdHaftG | Geschädigte/r: Nachweis des Fehlers, Schadens und Kausalität; Hersteller: Entlastungsbeweis nach § 1 Abs. 2/3 ProdHaftG |
| Technische Aufsicht Pflichtverletzung | Kläger muss belegen, dass Übergabeanforderung ausgelöst wurde und nicht (rechtzeitig) reagiert wurde; Black-Box-Daten entscheidend |
| CMR Art. 29 Qualifiziertes Verschulden | Anspruchsteller: Organisationsmangel oder Systemversagen mit Bewusstsein; Frachtführer: Exkulpation durch Wartungsnachweise |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort nach Unfall | Black-Box-Daten sichern (6 Monate Aufbewahrungspflicht) | § 1g StVG |
| 3 Jahre | ProdHaftG: Verjährung des Schadensersatzanspruchs | § 12 ProdHaftG |
| 10 Jahre | ProdHaftG: Ausschlussfrist für Haftungsansprüche ab Inverkehrbringen | § 13 ProdHaftG |
| 3 Jahre | StVG § 7: Verjährung nach §§ 195, 199 BGB | § 195 BGB |
| 1 Jahr | CMR Art. 32: Verjährung Frachtführerhaftung | CMR Art. 32 |
| 6 Monate | § 1g StVG: Aufbewahrungspflicht Datenspeicher; danach darf Frachtführer löschen | § 1g StVG |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Frachtführer haftet nicht wegen autonomen Systems" | CMR Art. 17 ist verschuldensunabhängige Obhutshaftung; autonomer Modus ändert Haftungsgrundlage nicht; Frachtführer muss Haftungsausschluss Art. 17 Abs. 2 CMR beweisen |
| "§ 7 StVG greift nicht weil autonomes Fahrzeug kein klassisches Kfz" | § 1d StVG ändert nichts an der Halterhaftung nach § 7 StVG; Halter haftet nach § 7 bei jedem Betrieb des Fahrzeugs |
| "Black-Box-Daten sind nicht zugänglich" | § 1g StVG: Pflicht zur Datenspeicherung; § 1h StVG: Auskunftspflicht gegenüber Behörden; gerichtlicher Herausgabeanspruch bei drohender Vernichtung möglich (§ 809 BGB) |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| "Fahrer hätte eingreifen müssen" | Bei Level 3/4: Fahrer ist nur zur Übernahme verpflichtet wenn System Übergabe anfordert; ohne Anforderung keine Eingreifpflicht |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Personenschaden (Halterhaftung § 7 StVG) | Bis 7.5 Mio. EUR/Ereignis nach § 12 StVG; voller Schadenersatz bei Produkthaftung |
| Sachschaden | Bis 1 Mio. EUR/Ereignis nach § 12 StVG; unbegrenzt bei ProdHaftG (§ 10 ProdHaftG gilt nicht für Sachschäden über EUR 500) |
| Ladungsschaden CMR | 8.33 SZR/kg Regelhaftung; unbegrenzt bei Art. 29 CMR |
| Produkthaftungsklage | Aufwändiges Sachverständigenverfahren; Gutachtenkosten EUR 20.000–100.000; als Verfahrenskosten ggf. erstattungsfähig |
| Versicherungsregress | Haftpflichtversicherung schöpft Haftungsgrenzen aus; Produkthaftpflicht des Herstellers separat |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Personenschaden durch autonomen LKW | Primär § 7 StVG (Halter), sekundär ProdHaftG (Hersteller); beide als Gesamtschuldner verklagen |
| Ladungsschaden des Frachtkunden | Direktanspruch gegen Frachtführer aus CMR Art. 17; Frachtführer nimmt Regress gegen Hersteller nach ProdHaftG |
| Black-Box-Daten drohen gelöscht zu werden | Einstweilige Verfügung auf Datensicherung nach § 809 BGB; Sicherungsantrag beim KBA nach § 1h StVG |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Technische Aufsicht hat nicht reagiert | Verschuldenshaftung der benannten Person; ggf. auch des Halters für Auswahl und Überwachung nach § 831 BGB |

---

## Anschluss-Skills

- `fachanwalt-transport-speditionsrecht-cmr-haftung` – grenzüberschreitende CMR-Haftung im Detail
- `frachtfuehrerhaftung-pruefen` – systematische Haftungsanalyse CMR/HGB
- `reklamationsschreiben-cmr-hgb` – Reklamation bei Ladungsschaden
- `fachanwalt-transport-speditionsrecht-ladungsschaden` – HGB-Ladungsschaden ohne autonome Komponente

---

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `fachanwalt-transport-cmr-schadensregulierung`

**Fokus:** Schadensregulierung im grenzüberschreitenden Gueterverkehr nach CMR durchführen. Normen: Art. 17 ff. 23 ff. CMR. Prüfraster: Schadensanzeige, Haftungsgrenzen 8.33 SZR je Kilogramm, Schadensberechnung, Fristen. Output: CMR-Schadensregulierungsschreiben. Abgrenzung: nicht nationales HGB-Recht.

### CMR-Schadensregulierung

## Zweck

Schaden an internationaler LKW-Lieferung nach CMR (UEbereinkommen über den Beförderungsvertrag im internationalen Straßengueterverkehr).

## 1) Anwendbarkeit Art. 1 CMR

- Straßentransport
- International (von / nach Vertragsstaat)
- Gegen Entgelt
- Eingeschlossen: kombiniert (Straße + Schiff)

## 2) CMR-Frachtbrief Art. 4-9 CMR

### Bedeutung Art. 9 CMR

- **Beweis** des Vertragsabschlusses
- **Beweis** der Überngabe in Wirklichkeit
- Bei Mangel-Vermerk: Vermutung Verkehrs-Schaden Frachtführer

### Pflichtinhalte Art. 6 CMR

- Absender, Empfänger
- Ware-Beschreibung
- Frachtführer
- Bestimmungs-Ort

## 3) Haftungs-Grenze Art. 23 III CMR

- **8,33 SZR / kg** (Sonderziehungs-Recht ca. 10 EUR)
- Pro Brutto-Kilogramm der verlorenen Ware
- Beispiel: 1.000 kg Ware bei vollem Verlust = 10.000 EUR Höchstgrenze

### Aufhebung Haftungsbegrenzung

- Bei qualifiziertem Verschulden Art. 29 CMR (Vorsatz / grobe Fahrlaessigkeit)
- Volle Schadensbegleichung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 4) Reklamation Art. 30 CMR

### Frist

- Bei aeusserlich sichtbaren Schäden: **bei Ablieferung**
- Bei verdeckten Schäden: **7 Tage** nach Ablieferung
- Bei Verspätung: 21 Tage

### Form

- Schriftlich
- Bei Versäumnis: Verlust der Anspruche (Vermutungs-Wirkung Art. 30)

## 5) Verjährung Art. 32 CMR

- **1 Jahr** ab Ablieferung
- Bei Vorsatz / grober Fahrlaessigkeit: **3 Jahre**
- Hemmung durch schriftliche Reklamation

## 6) Schadens-Regulierung

### Phase 1 — Schadens-Aufnahme

- Foto am Ablieferungs-Ort
- Bestätigung Empfänger
- CMR-Frachtbrief-Vermerk

### Phase 2 — Reklamation

- Schriftlich an Frachtführer
- Innerhalb 7 Tage (verdeckt)
- Schadens-Aufstellung

### Phase 3 — Versicherer

- Frachtführer-Versicherer
- Eigene Transport-Versicherung
- Zeitgleiche Geltendmachung

### Phase 4 — Klage

- Bei Verzug Versicherer: Klage AG / LG je Streitwert
- Sachliche Zuständigkeit Art. 31 CMR — Schädigungs-Ort, Empfänger-Ort

## 7) Beweisaufnahme

### Schaden-Beweis

- Foto-Dokumentation
- Sachverständigen-Gutachten
- Zeugen-Aussagen

### Verschuldens-Frage

- Frachtführer-Verhalten
- Bei Vorsatz / grober Fahrlaessigkeit: Aufhebung Begrenzung

## 8) Typische Fehler

1. **Reklamationsfrist 7 Tage versäumt**
2. **CMR-Frachtbrief-Vermerk fehlt** bei Mangel
3. **Verjährung 1 Jahr verpasst**
4. **Haftungs-Aufhebung Art. 29 CMR nicht geltend gemacht**

## 9) BGH-Linien

Stand 05/2026 — Rechtsprechung im Mandat live verifizieren über [bundesgerichtshof.de](https://www.bundesgerichtshof.de) (BGH I. Zivilsenat) sowie [openjur.de](https://openjur.de).

Aktuelle BGH-Linie zum Anwendungsbereich der CMR-Gerichtsstandsregelung (Art. 31 CMR): Ausweitung auf Direktklageansprüche gegen den Verkehrshaftungsversicherer ist Gegenstand jüngerer Entscheidungen — vor Ausgabe Aktenzeichen, Datum, Tenor live prüfen.

Bei Verlust mit Falschablieferung trägt der Frachtführer die Beweislast dafür, gleichwohl an einen berechtigten Empfänger abgeliefert zu haben (Linie der OLG-Rechtsprechung 2024/2025; konkrete Fundstelle im Schriftsatz verifizieren).

ADSp-Aktualität: Die ADSp 2017 sind weiterhin Branchenstandard (keine ADSp 2025 ausgewiesen; Stand der Recherche Mai 2026). Im Mandat über [dslv.org](https://www.dslv.org/de/adsp) auf Aktualität prüfen.

## Anschluss

- `frachtfuehrerhaftung-pruefen` — Prüfraster
- `fachanwalt-transport-speditionsrecht-orientierung` — Triage
- `deckungsanfrage-pruefen` — bei Versicherer

## 3. `fachanwalt-transport-speditionshaftung-hgb`

**Fokus:** Speditionshaftung nach HGB prüfen: Fixkostenspediteur, Sammelladungsspediteur, Haftungsgrenzen. Normen: §§ 454 ff. HGB. Prüfraster: Speditionsauftrag, Selbsteintritt, Haftungsregime, ADSP-Klauseln. Output: Speditionshaftungsanalyse. Abgrenzung: nicht Frachtführerhaftung §§ 407 ff. HGB.

### Speditions-Haftung §§ 453 ff. HGB

## Zweck

Schaden bei Spediteur-Vertrag — Pflichten, Haftung, Anspruchs-Grundlagen.

## 1) Vertrags-Arten

### Vermittlungs-Spedition § 453 HGB

- Vermittlung Frachtvertrag
- Spediteur ist nicht selbst Frachtführer
- Haftung nur für Sorgfaltspflichten

### Selbsteintritts-Spedition § 458 HGB

- Spediteur führt selbst aus
- Haftung wie Frachtführer (HGB / CMR)

### Sammellade-Spedition § 460 HGB

- Sammlung mehrerer Lieferungen
- Haftung wie Frachtführer (§ 460 II HGB)

### Festpreis-Spedition § 459 HGB

- Pauschal-Preis
- Haftung wie Frachtführer

## 2) Haftungs-Grenze § 461 HGB

- 8,33 SZR / kg analog CMR
- Bei Vorsatz / grober Fahrlaessigkeit: unbegrenzt
- ADSp 2017 / 2025 Sonderregelungen

## 3) ADSp (Allgemeine Deutsche Spediteur-Bedingungen)

### Inhalt 2017 / 2025

- Standardisierte Speditions-Bedingungen
- Mehrwert-Versicherung
- Haftungsbegrenzung detaillierter

### Einbeziehung

- Mit Frachtbrief / Auftragsbestätigung
- Kollisions-Klauseln mit Kunden-AGB

## 4) Reklamations-Fristen

| Schaden | Frist |
|---|---|
| Sichtbar | bei Ablieferung |
| Verdeckt | 7 Tage |
| Verspätung | 21 Tage |

## 5) Verjährung § 439 HGB

- 1 Jahr bei einfachem Verschulden
- 3 Jahre bei qualifiziertem Verschulden
- Beginn: Ablieferung

## 6) Workflow

### Phase 1 — Analyse Vertrags-Art

- Welche Spediteur-Form?
- Eigen-/Fremdleistung
- Selbsteintritt vorgesehen?

### Phase 2 — Reklamations-Schritte

- Schriftlich an Spediteur
- ADSp-Klauseln prüfen
- Versicherer-Mitteilung

### Phase 3 — Klage

- Bei Streit: HGB / ADSp / CMR
- Streitwert nach Schadenshöhe

## 7) Typische Fehler

1. **ADSp-Einbeziehung übersehen** -> Haftungs-Begrenzung
2. **Vertragsart falsch eingeordnet** -> falsche Anspruchsgrundlage
3. **Reklamationsfrist versäumt**
4. **Mehrwert-Versicherung nicht beachtet**

## 8) BGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-transport-cmr-schadensregulierung` — bei internationaler Straße
- `frachtfuehrerhaftung-pruefen` — Prüfraster
- `fachanwalt-transport-speditionsrecht-orientierung` — Triage

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 1d StVG
- § 1g StVG
- § 7 StVG
- § 1 ProdHaftG
- § 1h StVG
- § 1f StVG
- § 18 StVG
- § 12 StVG
- § 86 VVG
- § 3 ProdHaftG
- § 1 PflVG
- § 29 VwVfG
