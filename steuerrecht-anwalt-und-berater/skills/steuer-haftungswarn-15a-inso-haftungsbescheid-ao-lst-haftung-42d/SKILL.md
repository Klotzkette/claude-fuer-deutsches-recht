---
name: steuer-haftungswarn-15a-inso-haftungsbescheid-ao-lst-haftung-42d
description: "Steuer Haftungswarn 15A Inso Haftungsbescheid AO LST Haftung 42D: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer Haftungswarn 15A Inso Haftungsbescheid AO LST Haftung 42D

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer Haftungswarn 15A Inso Haftungsbescheid AO LST Haftung 42D** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anw-haftungswarn-15a-inso-mandant` | Anwaltliche Beratung und Warnschreiben an GmbH-Geschäftsführung bei festgestellter Insolvenzreife nach §§ 17 19 InsO. Anwendungsfall GmbH-GF spricht beim Anwalt vor weil Steuerberater Krisensignale gemeldet hat. Antragspflicht § 15a InsO drei Wochen Zahlungsunfähigkeit sechs Wochen Überschuldung. Strafbarkeit Insolvenzverschleppung § 15a Abs. 4 InsO. GF-Haftung § 15b InsO nach SanInsFoG. Output Beratungsdokumentation Warnschreiben mit Belehrung Eingangsbestätigung. Abgrenzung zu stb-warnschreiben-krisensignale Steuerberater-Pflichthinweis und anw-insolvenzreife-prüfung-17-19-inso Gutachten. |
| `fa-stu-haftungsbescheid-69-191-ao` | Materielle Pruefung und Abwehr von Haftungsbescheiden — Geschaeftsfuehrerhaftung § 69 AO Steuerhinterzieherhaftung § 71 AO Lohnsteuerhaftung § 42d EStG und Verfahrensvorschriften § 191 AO. Anwendungsfall Geschaeftsfuehrer oder GmbH-Beirat erhaelt Haftungsbescheid wegen rueckstaendiger Steuern der Gesellschaft. Behandelt Tatbestandsvoraussetzungen Verschulden Kausalitaet quotale Befriedigung und Ermessensfehler. Output Pruefraster Haftung mit Erwiderungsmuster. Abgrenzung zu fa-stu-lst-haftung-42d-estg. |
| `fa-stu-lst-haftung-42d-estg` | Detaillierte Pruefung der Lohnsteuerhaftung — wann haftet der Arbeitgeber als Gesamtschuldner mit dem Arbeitnehmer welche Verteidigungsmoeglichkeiten gibt es. Anwendungsfall Lohnsteueraussenpruefung endet mit Haftungsbescheid wegen pauschaler Geldzuwendungen Sachzuwendungen oder Reisekostenproblemen. Behandelt Haftungstatbestand Auswahl- und Entschliessungsermessen Bruttoabsetzung Pauschalierung § 40 EStG und Anrechnung beim Arbeitnehmer. Output Pruefraster und Erwiderungsmuster. Abgrenzung zu fa-stu-haftungsbescheid-69-191-ao. |
| `stb-lohn-pruefungen-drv-bp-haftung-stb` | Prüfungen DRV-Prüfung Lohnsteuer-Aussenprüfung Steuerberater-Haftung. Anwendungsfall DRV-Prüfer kommt Prüfkriterien Nachforderung Haftungsrisiken Mandant. Methodik Vorbereitung Begleitung Reaktion. Output Prüfbericht Prüfverhandlung Massnahmen. |
| `stb-lohn-streitfaelle-bag-bsg-haftungsrisiko` | Lohn-Streitfaelle BAG-Linie BSG-Linie StB-Haftungsrisiko. Anwendungsfall typische Streitfaelle Werkvertrag versus AN Status arbeitsrechtlich vs sozialversicherungsrechtlich Klagerisiko. Methodik Rechtsprechungsanalyse Risikobewertung. Output Memo Haftungsrisiko. |
| `anw-akteneinsicht-steuerakte` | Akteneinsicht in die Steuerakte beantragen und auswerten — Einspruchsverfahren nach § 364 AO Klageverfahren nach § 78 FGO sowie ergaenzend Art. 15 DSGVO bei personenbezogenen Daten. Anwendungsfall Mandant will Prüfungsbericht Aktenvermerk oder Prüfungsakte einsehen um Einspruch oder Klage zu begründen. Behandelt Verwaltungsakten Prüfungsakten Aktenvermerke Aussenprüfungs-Berichte Schwaerzungen wegen Steuergeheimnis Dritter § 30 AO. Output Antragsvorlage und strukturiertes Auswertungsraster für die uebermittelte Akte. Abgrenzung zu anw-aussenprüfung-strategien Mitwirkungspflichten und anw-einspruch-finanzamt. |
| `anw-aussetzung-vollziehung` | Antrag auf Aussetzung der Vollziehung AdV stellen um Steuerzahlung bis zur Streitentscheidung auszusetzen. Anwendungsfall Mandant hat Einspruch eingelegt will aber Nachforderung nicht sofort zahlen. Zweistufig zuerst beim Finanzamt § 361 Abs. 2 AO bei ernstlichen Zweifeln an der Rechtmäßigkeit oder unbilliger Haerte dann bei Ablehnung beim Finanzgericht § 69 Abs. 3 FGO. Prüfung Anordnungsanspruch ernstliche Zweifel oder unbillige Haerte und Anordnungsgrund drohende Vollziehung. Inkludiert eidesstattliche Versicherung. Output AdV-Antrag an FA und Antrag an FG. Abgrenzung zu anw-einspruch-finanzamt und anw-stundung-erlass-vollstreckungsaufschub. |
| `anw-defi-lending-yield-farming-bmf-22-11-2024` | Steuerliche Behandlung von DeFi-Lending Yield Farming Liquidity Mining Staking nach BMF-Schreiben vom 22.11.2024. Anwendungsfall Mandant nutzt DeFi-Protokolle Aave Compound Curve Yearn Uniswap Lido EigenLayer und fragt nach steuerlicher Erklärungspflicht. Einkuenfte § 22 Nr. 3 EStG oder § 20 EStG Token-Tausch als Veraeusserung § 23 EStG Spekulationsfrist Wrapped Tokens LP-Tokens Yield Tokens. DAC8-Meldepflicht beachten. Wallet-Analyse Cointracking Steuererklarung. Output steuerliche Beurteilung Erklärungspflichtige Einkuenfte Beratungsmemo. Abgrenzung zu anw-dac7-dac8-plattformen-krypto. |
| `anw-einspruch-finanzamt` | Begründeten Einspruch gegen Steuerbescheid nach §§ 347 ff. AO formulieren. Anwendungsfall Mandant erhaelt Steuerbescheid und will Einspruch einlegen. Frist ein Monat ab Bekanntgabe § 355 Abs. 1 AO bzw. ein Jahr bei fehlender Rechtsbehelfsbelehrung § 356 AO Vier-Tage-Fiktion § 122 Abs. 2 AO seit 01.01.2025 PostModG. Angriffspunkte Rechtsverletzung Rechenfehler § 129 AO Schaetzung § 162 AO neue Tatsachen § 173 AO Festsetzungsverjährung § 169 AO Wiedereinsetzung § 110 AO. Output Einspruchsschriftsatz mit Antrag Begründung Beweisangebot AdV-Antrag § 361 Abs. 2 AO Akteneinsicht § 364 AO. Abgrenzung zu anw-klage-finanzgericht anw-steuerbescheid-analyse. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer Haftungswarn 15A Inso Haftungsbescheid AO LST Haftung 42D**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anw-haftungswarn-15a-inso-mandant`

**Fokus:** Anwaltliche Beratung und Warnschreiben an GmbH-Geschäftsführung bei festgestellter Insolvenzreife nach §§ 17 19 InsO. Anwendungsfall GmbH-GF spricht beim Anwalt vor weil Steuerberater Krisensignale gemeldet hat. Antragspflicht § 15a InsO drei Wochen Zahlungsunfähigkeit sechs Wochen Überschuldung. Strafbarkeit Insolvenzverschleppung § 15a Abs. 4 InsO. GF-Haftung § 15b InsO nach SanInsFoG. Output Beratungsdokumentation Warnschreiben mit Belehrung Eingangsbestätigung. Abgrenzung zu stb-warnschreiben-krisensignale Steuerberater-Pflichthinweis und anw-insolvenzreife-prüfung-17-19-inso Gutachten.

# Haftungswarn an GmbH-Geschäftsführung bei Insolvenzreife (Anwaltliche Sicht)

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Haftungswarn an GmbH-Geschäftsführung bei Insolvenzreife (Anwaltliche Sicht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Anwaltliche Beratung und schriftliche Dokumentation gegenüber der Geschäftsführung einer GmbH/UG, wenn die Mandantin (häufig nach Hinweis des Steuerberaters via `stb-warnschreiben-krisensignale`) bei dem Anwalt vorspricht und sich Insolvenzreife verdichtet. Anders als der Steuerberater **darf und muss** der Anwalt die rechtliche Beurteilung der Antragspflicht treffen — und sich dabei selbst absichern.

> ℹ️ **Rollenabgrenzung zu `anw-insolvenzreife-pruefung-17-19-inso`:** Dieser Skill ist **präventiv-belehrend** — erstellt das schriftliche Warn-/Belehrungsschreiben an den GF nach erfolgter Reife-Analyse. Die vorgeschaltete **analytische** Prüfung der Insolvenzreife (§§ 17, 19 InsO Subsumtion, Beweiswürdigung) leistet `anw-insolvenzreife-pruefung-17-19-inso`. Standardablauf: erst `anw-insolvenzreife-pruefung-17-19-inso` (Diagnose), dann dieser Skill (Mandantenbelehrung + Dokumentation).

> Dieses Schreiben dokumentiert die Beratungsleistung. Es ist **kein** anwaltliches Mahn-/Warnschreiben gegen den Mandanten, sondern eine schriftliche **Belehrung über die Antragspflicht und ihre Folgen** mit Bestätigung der Beratung — Pflicht aus § 11 BORA und Selbstschutz vor späteren Regressansprüchen.

## Eingaben

- Mandant (GmbH/UG, vollständige Firma, HRB, Stammkapital, GF mit Vertretungsbefugnis)
- Anlass (Steuerberater-Hinweis, eigener Anstoß, Gesellschafterbeschluss)
- Datenlage: Bilanz, BWA, Liquidität — vom Steuerberater oder GF übergeben
- Bisherige interne Krisenmaßnahmen (§ 102 StaRUG-Dokumentation)
- Rangrücktritte, Patronate, Bürgschaften bekannt?
- Mandatsumfang: nur Beratung Antragspflicht oder Vollmandat Sanierung/Antrag?
- Vergütungsvereinbarung (Stundenhonorar, Pauschale, RVG nach Wert)

## Rechtlicher Rahmen

### Primärnormen

- **§ 15a Abs. 1 Satz 1 InsO** — Insolvenzantragspflicht. Zahlungsunfähigkeit (§ 17 InsO) → drei Wochen. Überschuldung (§ 19 InsO) → sechs Wochen.
- **§ 15a Abs. 4 InsO** — Strafbarkeit Insolvenzverschleppung (Freiheitsstrafe bis 3 Jahre / Geldstrafe; bei Fahrlässigkeit bis 1 Jahr).
- **§ 15b InsO** — Zahlungsverbote nach Insolvenzreife. Geschäftsführerhaftung gegen die Gesellschaft (löste § 64 GmbHG a.F. ab; SanInsFoG, 1.1.2021).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 19 InsO** — Überschuldung (zweistufig: rechnerisch und Fortbestehensprognose; vgl. `stb-ueberschuldungspruefung-19-inso`).
- **§ 18 InsO** — Drohende Zahlungsunfähigkeit (24-Monats-Horizont; Antragsrecht, keine Pflicht — Zugangstor StaRUG).
- **§ 102 StaRUG** — Krisenfrüherkennungspflicht GF; ergänzt § 91 Abs. 2 AktG analog auf alle haftungsbeschränkten Gesellschaften.
- **§ 64 StBerG / § 43a Abs. 5 BRAO** — bei Honorarrückständen Berücksichtigung; keine Beratung ohne Vergütungsvereinbarung in Hochrisikofällen.
- **§ 826 BGB / § 823 Abs. 2 BGB i.V.m. § 15a InsO** — Außenhaftung GF gegenüber Neugläubigern bei Insolvenzverschleppung.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### Schritt 1 — Sachverhalt klären

- Zahlungsunfähigkeit (§ 17 InsO) oder nur Zahlungsstockung? Liquiditätslücke berechnen (Aktiva I + II vs. Passiva I + II, BGH-Schema). Vgl. `stb-liquiditaetsvorschau-3wochen` oder `liquiditaetsplanung`.
- Überschuldung (§ 19 InsO): zweistufige Prüfung (Fortbestehensprognose + rechnerischer Status). Vgl. `stb-ueberschuldungspruefung-19-inso`.
- Drohende Zahlungsunfähigkeit (§ 18 InsO): 24-Monats-Liquidität. Wenn ja → StaRUG-Option offen, **noch keine Pflicht**, aber Strategie-Frage.

### Schritt 2 — Frist-Trigger feststellen

| Tatbestand | Frist § 15a InsO | Trigger |
|---|---|---|
| Zahlungsunfähigkeit § 17 | 3 Wochen | objektives Eintreten — nicht subjektive Kenntnis |
| Überschuldung § 19 | 6 Wochen | objektives Eintreten — nicht subjektive Kenntnis |
| Drohende Zahlungsunfähigkeit § 18 | keine Pflicht | nur Antragsrecht; StaRUG-Zugang |

Aussagen klar dokumentieren: **wann** ist die Insolvenzreife objektiv eingetreten — nicht wann sie der GF erkannt hat. Wenn umstritten, IDW-S-11-Stichtagsanalyse beauftragen.

### Schritt 3 — Optionen mit dem Mandanten besprechen

1. **Insolvenzantrag** — Regelverfahren, Eigenverwaltung (§ 270b InsO), Schutzschirm (§ 270d InsO).
2. **StaRUG-Restrukturierungsverfahren** — nur bei drohender Zahlungsunfähigkeit (§ 18 InsO), nicht bei manifester Insolvenzreife.
3. **Außergerichtliche Sanierung** — nur möglich bei kurzfristiger Stockung (< 3 Wochen) oder gesichertem Kapital-/Liquiditätszufluss.
4. **Sanierungskonzept nach IDW S 6** als Voraussetzung positiver Fortbestehensprognose.
5. **Mandatsniederlegung** bei eklatanter Insolvenzverschleppung und Weigerung des GF.

### Schritt 4 — Schriftliche Belehrung

Pflicht aus § 11 BORA (Schriftform-Pflicht bei wichtigen Mandantenhinweisen) und § 49b Abs. 5 BRAO (Belehrung über Honorarauslösung bei Mandatsumfang).

### Schritt 5 — Eigene Aktendokumentation

- Aktennotiz: Sachverhalt, Beratungsinhalt, Empfehlung, Mandantenreaktion.
- Schriftliche Belehrung samt Eingangsbestätigung.
- Folge-Schritte (Wiedervorlage; ggf. weitere Honorarvereinbarung).
- Versendung beA an Mandanten-Anwalt (sofern vorhanden) bzw. Einschreiben.

## Muster — Anwaltliches Belehrungs-/Hinweisschreiben (verkürzt)

```
[Kanzlei-Briefkopf] [Datum]

PERSÖNLICH UND VERTRAULICH

[Mandant — GmbH, z. Hd. Geschaeftsfuehrer/in Name]
[Anschrift]

vorab per beA / Einschreiben mit Rueckschein

In dem Mandat [Aktenzeichen] / Beratung zur Insolvenzantragspflicht

Sehr geehrte/r Frau / Herr [Name],

ich nehme Bezug auf unsere Besprechung am [Datum] und auf die mir
ueberlassenen Unterlagen (Bilanz zum [Stichtag], BWA, SuSa,
Liquiditaetsuebersicht der Steuerkanzlei [Name]).

Nach einer ersten Pruefung des Sachverhalts ist davon auszugehen, dass
zum Zeitpunkt [Datum] [Zahlungsunfaehigkeit gemaess § 17 InsO /
Ueberschuldung gemaess § 19 Abs. 2 InsO] vorliegt. Die Einzelheiten der
rechtlichen Wuerdigung entnehmen Sie bitte dem beigefuegten Vermerk.

Daraus folgt eine **Pflicht zur Insolvenzantragstellung** gemaess
§ 15a Abs. 1 Satz 1 InsO. Die Hoechstfrist betraegt
[drei Wochen ab Eintritt der Zahlungsunfaehigkeit /
sechs Wochen ab Eintritt der Ueberschuldung].

**Risiken bei Verstoss gegen die Antragspflicht:**

1. Strafrechtliche Verantwortung nach § 15a Abs. 4 InsO
 (Freiheitsstrafe bis zu drei Jahren oder Geldstrafe; bei
 fahrlaessiger Verschleppung bis zu einem Jahr).
2. Persoenliche zivilrechtliche Haftung gegenueber der Gesellschaft
 gemaess § 15b InsO (verbotene Zahlungen nach Insolvenzreife).
3. Persoenliche Haftung gegenueber Neuglaeubigern aus § 823 Abs. 2
 BGB i.V.m. § 15a InsO bzw. § 826 BGB (Quotenschaden Altglaeubiger,
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Empfehlung:**

Ich empfehle Ihnen mit Nachdruck:

- saemtliche an Glaeubiger gerichteten Zahlungen unverzueglich auf
 Insolvenzkonformitaet zu pruefen (vgl. § 15b InsO);
- saemtliche an die Gesellschaft eingehenden Zahlungen auf einem
 gesonderten Konto zu sammeln;
- den Insolvenzantrag innerhalb der oben genannten Frist zu stellen,
 sofern eine Sanierungsperspektive ausserhalb des Insolvenzverfahrens
 nicht zeitnah belegt werden kann;
- alternative Verfahrenswege (Eigenverwaltung § 270b InsO,
 Schutzschirm § 270d InsO, StaRUG-Restrukturierung soweit erst
 drohende Zahlungsunfaehigkeit) gegen das Regelinsolvenzverfahren
 abzuwaegen.

Ich stehe zur Mandatsuebernahme fuer das Insolvenzantragsverfahren oder
fuer ein Sanierungsverfahren auf Grundlage einer gesonderten
Verguetungsvereinbarung zur Verfuegung.

Bitte bestaetigen Sie den Eingang dieses Schreibens und teilen Sie mir
Ihre Entscheidung binnen drei Werktagen mit. Sollte ich von Ihnen keine
Reaktion erhalten, gehe ich davon aus, dass Sie meine Beratung nicht
in Anspruch nehmen wollen, und werde das Mandat in Bezug auf die
Insolvenzantragstellung niederlegen.

Mit freundlichen Gruessen
[Unterschrift]
Rechtsanwalt/-anwaeltin
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| GF kennt Insolvenzreife, verweigert Antrag | Beihilfe-/Anstiftungsrisiko? Mandat niederlegen | Aufklärung erneut, schriftlich | Antrag wird gestellt |
| Keine Schriftform der Belehrung | § 11 BORA-Pflichtverstoß, Regressrisiko | mündliche Belehrung dokumentiert | beA + Einschreiben |
| Anwalt selbst zahlt Honorar aus Mandantenkonto nach Insolvenzreife | § 15b InsO-Pflichtverstoß GF, Risiko Anwaltsregress | nach Verfahrenseröffnung | Honorar vor Insolvenzreife oder als Massevorab |
| Beratung ohne Aktenlage | Sorgfaltsverstoß; Beweislastumkehr bei Schaden | bei kurzfristigem Hinweis | nach umfassender Akteneinsicht |

## Querverweise

- `stb-warnschreiben-krisensignale` — vorgelagerte StB-Warnschreiben
- `stb-ueberschuldungspruefung-19-inso` — technische Vorprüfung
- `stb-liquiditaetsvorschau-3wochen` — Liquidität § 17 InsO
- `liquiditaetsplanung` (Power-Plugin) — gerichtsfeste insolvenzrechtliche Bilanz
- `fachanwalt-insolvenz-sanierungsrecht` — bei Vollmandat zur Sanierung/Antragstellung
- `anw-selbstanzeige-371` — wenn parallel Steuer-Hinterziehungsproblematik (Selbstanzeige kann § 15b-Schutz nicht ersetzen)

## Quellen und Updates

Stand: 05/2026. SanInsFoG (§ 15b InsO statt § 64 GmbHG a.F., 1.1.2021), SanInsKG (24-Monats-Prognose § 19 InsO bis 31.12.2026) berücksichtigt. § 11 BORA-Schriftformpflicht zentral. Bei Änderung InsO/BORA aktualisieren.

<!-- AUDIT 27.05.2026 bundle_043
Maßnahme: Beschreibung des AZ korrigiert auf tatsächliches Thema: § 64 GmbHG a.F. — Zahlungsverbot nach Insolvenzreife; Aktiventausch und Rückgewähranspruch des GF. Das AZ ist damit thematisch passend für diesen Insolvenzreife-Skill und bleibt erhalten.
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=04.07.2017&Aktenzeichen=II+ZR+319%2F15
-->

## 2. `fa-stu-haftungsbescheid-69-191-ao`

**Fokus:** Materielle Pruefung und Abwehr von Haftungsbescheiden — Geschaeftsfuehrerhaftung § 69 AO Steuerhinterzieherhaftung § 71 AO Lohnsteuerhaftung § 42d EStG und Verfahrensvorschriften § 191 AO. Anwendungsfall Geschaeftsfuehrer oder GmbH-Beirat erhaelt Haftungsbescheid wegen rueckstaendiger Steuern der Gesellschaft. Behandelt Tatbestandsvoraussetzungen Verschulden Kausalitaet quotale Befriedigung und Ermessensfehler. Output Pruefraster Haftung mit Erwiderungsmuster. Abgrenzung zu fa-stu-lst-haftung-42d-estg.

# Haftungsbescheid — § 69 AO § 71 AO und Verfahren § 191 AO

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Haftungsbescheid — § 69 AO § 71 AO und Verfahren § 191 AO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Wer ist Haftungsschuldner und welcher Tatbestand wird herangezogen (§ 69 § 71 § 73 § 74 AO oder § 42d EStG)?
2. Sind die rueckstaendigen Steuern bereits bestandskraeftig festgesetzt oder noch offen?
3. Liegt zumindest grobe Fahrlaessigkeit oder Vorsatz vor (§ 69 AO setzt grobe Fahrlaessigkeit voraus)?
4. Wurde der Grundsatz quotaler Befriedigung gegenueber dem Fiskus verletzt?
5. Ermessensausuebung des FA pruefen — Auswahl- und Entschliessungsermessen § 191 Abs. 1 AO?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 69 AO** — Haftung der Vertreter.
- **§ 71 AO** — Haftung des Steuerhinterziehers.
- **§ 73 AO** — Haftung bei Organschaft.
- **§ 74 AO** — Haftung des Eigentuemers.
- **§ 75 AO** — Haftung bei Betriebsuebernahme.
- **§ 42d EStG** — Lohnsteuerhaftung des Arbeitgebers.
- **§ 191 AO** — Verfahren zum Erlass von Haftungsbescheiden.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 69 AO · § 71 AO · § 73 AO · § 74 AO · § 75 AO · § 191 AO · § 219 AO (Inanspruchnahme nach erfolgloser Vollstreckung) · § 42d EStG

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 3. `fa-stu-lst-haftung-42d-estg`

**Fokus:** Detaillierte Pruefung der Lohnsteuerhaftung — wann haftet der Arbeitgeber als Gesamtschuldner mit dem Arbeitnehmer welche Verteidigungsmoeglichkeiten gibt es. Anwendungsfall Lohnsteueraussenpruefung endet mit Haftungsbescheid wegen pauschaler Geldzuwendungen Sachzuwendungen oder Reisekostenproblemen. Behandelt Haftungstatbestand Auswahl- und Entschliessungsermessen Bruttoabsetzung Pauschalierung § 40 EStG und Anrechnung beim Arbeitnehmer. Output Pruefraster und Erwiderungsmuster. Abgrenzung zu fa-stu-haftungsbescheid-69-191-ao.

# Lohnsteuerhaftung des Arbeitgebers — § 42d EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lohnsteuerhaftung des Arbeitgebers — § 42d EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor der Bearbeitung

1. Wurde Lohnsteuer nicht oder zu niedrig einbehalten und abgefuehrt?
2. Wurde der Arbeitnehmer beim Finanzamt nachveranlagt — dann nur restliche Haftung?
3. Greift Pauschalierung § 40 § 40a § 40b EStG und befreit insoweit von der Haftung?
4. Wurde Ermessen nach § 42d Abs. 3 EStG fehlerfrei ausgeuebt — Auswahl Arbeitnehmer Arbeitgeber Dritter?
5. Bruttoabwaelzung oder Nettoabwaelzung im Falle einer Pauschalierung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 42d EStG** — Haftung des Arbeitgebers.
- **§ 41a EStG** — Lohnsteuer-Anmeldung.
- **§ 40 EStG** — Pauschalierung der Lohnsteuer.
- **§ 40a EStG** — Pauschalierung bei Teilzeit und geringfuegig Beschaeftigten.
- **§ 40b EStG** — Pauschalierung bei Direktversicherungen.
- **§ 191 AO** — Verfahren Haftungsbescheid.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 42d EStG · § 41a EStG · § 40 EStG · § 40a EStG · § 40b EStG · § 191 AO · § 219 AO

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.

## 4. `stb-lohn-pruefungen-drv-bp-haftung-stb`

**Fokus:** Prüfungen DRV-Prüfung Lohnsteuer-Aussenprüfung Steuerberater-Haftung. Anwendungsfall DRV-Prüfer kommt Prüfkriterien Nachforderung Haftungsrisiken Mandant. Methodik Vorbereitung Begleitung Reaktion. Output Prüfbericht Prüfverhandlung Massnahmen.

# DRV-Pruefung, Lohnsteuer-Aussenpruefung, StB-Haftung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DRV-Pruefung, Lohnsteuer-Aussenpruefung, StB-Haftung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die DRV-Sozialversicherungspruefung (alle 4 Jahre) und Lohnsteuer-Aussenpruefung des FA (anlassbezogen oder routinemaessig) sind die zentralen externen Pruefungen der Lohnbuchhaltung. Pruefthemen: SV-Status-Klassifikation, BBG-Einhaltung, Sachbezuege, Pauschalierungen, Aufzeichnungspflichten, Reisekosten. Der Steuerberater bereitet vor, begleitet die Pruefung und prueft Nachforderungen. Bei Pruefungsfehlern haftet der StB aus Mandantenvertrag (§ 280 BGB).

## Kaltstart-Rueckfragen

1. Welche Pruefung wird angekuendigt — DRV, Lohnsteuer-Aussenpruefung, BG-Pruefung, Zoll?
2. Welcher Pruefzeitraum (in der Regel 4 Jahre)?
3. Welche Pruefthemen sind erkennbar?
4. Liegen vorherige Pruefungs-Beanstandungen vor?
5. Welche kritischen Lohn-Themen im Mandantenbetrieb (Werkvertrag, Sachbezug, GGF-Status)?
6. Welche Unterlagen muessen vorgelegt werden?
7. Welcher Pruefer ist zustaendig?
8. Welche Mandantenkommunikation zur Pruefungsbegleitung?

## Rechtlicher Rahmen

### Primaernormen

**§ 28p SGB IV** — DRV-Pruefung (Pruefung der ordnungsgemaessen Beitragsleistung; in der Regel im 4-Jahres-Rhythmus).

**§ 42f EStG** — Lohnsteuer-Aussenpruefung (Pruefung beim AG durch das FA).

**§§ 193-203 AO** — Allgemeine Pruefungsbefugnis (subsidiaer; § 42f EStG ist lex specialis fuer LSt).

**§ 280 BGB** — Schadensersatz Pflichtverletzung (Anspruchsgrundlage Mandant gegen StB).

**§ 67 StBerG** — StB-Berufshaftpflicht (Pflicht-Versicherung).

**§ 33 StBVV** — Honorar Pruefungsbegleitung (Gegenstandswert Pruefungsergebnis).

### Verwaltungsanweisungen

- DRV-Rundschreiben zur Pruefung.
- BMF zu Lohnsteuer-Aussenpruefung.

## Workflow

### Phase 1 — Pruefungsankuendigung

- Schriftliche Ankuendigung mit Pruefzeitraum.
- Pruefungs-Inhalt grob benannt.
- Vorlage-Frist Unterlagen.
- Pruefdauer (in der Regel 3-5 Tage vor Ort).

### Phase 2 — Vorbereitung

| Unterlage | Pruefer-Anfrage |
|---|---|
| Lohnbuecher Sachkonten | Buchungs-Belege |
| AN-Stammdaten | Vertraege, ELStAM-Daten |
| Arbeitsvertraege | Vertragstexte |
| Sachbezugsdokumentation | Belege, Gutschein-Konfigurationen |
| Reisekosten-Belege | Belege, Erstattungsformulare |
| Dienstwagen | Listenpreis, Fahrtenbuch falls vorhanden |
| MiLoG-Aufzeichnungen | Stundenzettel |
| ELSTER-Quittungen | Lohnsteuer-Anmeldungen |
| DEUEV-Quittungen | SV-Meldungen |

### Phase 3 — Pruefungs-Themenschwerpunkte

| Thema | Risiko |
|---|---|
| Statusfeststellung GGF, Werkvertrag, Aushilfe | Nachforderung SV bis 4 Jahre |
| Minijob-Schwelle dauerhaft eingehalten? | Nachforderung |
| Sachbezuege ueber 50 EUR | Nachversteuerung LSt + SV |
| Dienstwagen 1-Prozent korrekt? | Lohnsteuer-Nachforderung |
| Pauschalierungen § 40 EStG | Nachversteuerung |
| Steuerfreie Auslagenerstattung Reisekosten | Pauschalbetraege Pruefung |
| § 3b EStG Sonn-/Nacht-Zuschlaege | Hoechstsatz und Grundlohngrenze |

### Phase 4 — Begleitung der Pruefung

- StB als Bevollmaechtigter vor Ort.
- Auf Fragen sachlich-fachlich antworten.
- Bei strittigen Punkten: nicht ueberhasten zustimmen; auf Pruefbericht warten.
- Dokumentation aller Pruefgespraeche.

### Phase 5 — Pruefbericht und Schlussbesprechung

- Pruefbericht mit Beanstandungen und Nachforderungen.
- Schlussbesprechung mit Pruefer und Mandant: strittige Punkte klaeren.
- Bei Streitpunkten: Einspruch (§ 347 AO) im Pruefungsbescheid.

### Phase 6 — Reaktion und Haftungs-Pruefung

- Bei Nachforderung: Mandant trgt SV oder LSt nach.
- Bei Fehler durch StB (z.B. falsche Klassifikation): Pruefung Berufshaftpflicht.
- Mandanten-Schadensersatzanspruch nach § 280 BGB pruefen.

## Output

- Pruefbericht in Mandantenakte.
- Nachforderungsbescheide.
- Massnahmen-Plan zur Vermeidung wiederholter Beanstandungen.

## Strategie und Praxis-Tipps

- DRV-Pruefung alle 4 Jahre Routine — Mandant rechtzeitig vorbereiten.
- Bei Lohnsteuer-Aussenpruefung haeufig Anlass aus E-Bilanz-Auffaelligkeiten oder Pruefung beim Unterauftragnehmer.
- StB-Haftungsrisiko hoch bei Sachbezugs-, GGF-Status-, Minijob-Fehlern — sorgfaeltige Dokumentation Standard.
- Pruefer-Argumente nicht vorschnell akzeptieren — bei zweifelhaften Rechtsfragen Anwalt einschalten.
- StBVV: Pruefungsbegleitung nach Gegenstandswert Pruefungsergebnis oder Zeithonorar.
- DATEV-Tipp: DATEV LODAS Pruefer-Sicht-Modus mit Pruefer-Datenexport.

## Querverweise

- `stb-drv-sozialversicherungspruefung` — DRV-Pruefung detailliert.
- `stb-lohn-gesellschafter-geschaeftsfuehrer-sv` — GGF-Status.
- `stb-lohn-streitfaelle-bag-bsg-haftungsrisiko` — BAG/BSG-Linien.
- `anw-aussenpruefung-strategien` — Aussenpruefung allgemein.

## Quellen und Updates

Stand: 05/2026.

- SGB IV § 28p.
- EStG § 42f.
- AO §§ 193-203.
- BGB § 280.
- StBerG § 67; StBVV § 33.
- DRV-Rundschreiben.
- BMF zu Lohnsteuer-Aussenpruefung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-lohn-streitfaelle-bag-bsg-haftungsrisiko`

**Fokus:** Lohn-Streitfaelle BAG-Linie BSG-Linie StB-Haftungsrisiko. Anwendungsfall typische Streitfaelle Werkvertrag versus AN Status arbeitsrechtlich vs sozialversicherungsrechtlich Klagerisiko. Methodik Rechtsprechungsanalyse Risikobewertung. Output Memo Haftungsrisiko.

# Lohn-Streitfaelle — BAG, BSG, Haftungsrisiken

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lohn-Streitfaelle — BAG, BSG, Haftungsrisiken` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Streitfaelle in der Lohnbuchhaltung haben oft zwei Streitlinien parallel: arbeitsrechtlich vor dem Arbeitsgericht (BAG-Linie) und sozialversicherungsrechtlich vor dem Sozialgericht (BSG-Linie). Die Klassifikation als AN, Werkvertrag, Selbstaendiger, Werkstudent oder GGF kann sich in beiden Spuren unterschiedlich darstellen. Der Steuerberater haftet bei Fehlklassifikation aus Mandantenvertrag.

## Kaltstart-Rueckfragen

1. Welche Lohn-Klassifikation ist strittig — AN/Werkvertrag, AN/Werkstudent, GGF-Status?
2. Liegt arbeitsgerichtliches oder sozialgerichtliches Verfahren?
3. Welche DRV-Statusfeststellung wurde durchgefuehrt?
4. Welche Vertragstexte und tatsaechliche Ausgestaltung?
5. Welche AN-Lebensumstaende (Familieneinbettung, Mehrfachbeschaeftigung)?
6. Welcher Pruefzeitraum?
7. Welche Hoehe Nachforderung?
8. Welche Versicherungs-Deckung (BHV des StB)?

## Rechtlicher Rahmen

### Primaernormen

**§ 611a BGB** — Arbeitsvertragsdefinition.

**§ 7 SGB IV** — Beschaeftigung.

**§ 1 ArbGG** — Arbeitsgerichtsbarkeit.

**§ 51 SGG** — Sozialgerichtsbarkeit.

**§ 280 BGB** — StB-Haftung.

**§ 67 StBerG** — Berufshaftpflicht.

### Leitentscheidungen BAG (Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen)

| Aktenzeichen | Leitsatz |
|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich |

### Leitentscheidungen BSG (Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen)

| Aktenzeichen | Leitsatz |
|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich |

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Workflow

### Phase 1 — Streit-Klassifikation

| Streit | Verfahren | Rechtsfolge |
|---|---|---|
| AN klagt auf Festanstellung | Arbeitsgericht | BAG-Linie |
| DRV stellt nachtraeglich SV-Pflicht fest | Sozialgericht | BSG-Linie |
| FA stellt nachtraeglich LSt-Pflicht fest | Finanzgericht | BFH-Linie |
| GGF-Status | DRV-Statusfeststellung | BSG-Linie |

### Phase 2 — Pruefung Gesamtbild

- Eingliederung in den Betrieb (Direktionsrecht).
- Weisungsgebundenheit (Zeit, Ort, Inhalt).
- Eigenes unternehmerisches Risiko.
- Eigenes Kapital.
- Eigene Mitarbeiter.
- Mehrere Auftraggeber.

### Phase 3 — Werkvertrag vs. AN

- Werkvertrag = bestimmtes Werk geschuldet, eigenverantwortliche Erbringung.
- AN = Diensttaetigkeit nach Weisung.
- Bei Scheinselbstaendigkeit: nachtraeglich AN-Status mit Nachforderung SV und LSt.

### Phase 4 — Werkstudent vs. AN

- Werkstudent: SV-vereinfachung; max. 20 Wochenstunden Vorlesungszeit.
- Bei Verlust des Studierenden-Status oder Ueberschreiten der Stundengrenze: AN-Status.

### Phase 5 — GGF-Status

- Mehrheits-GGF (>50 Prozent): selbstaendig.
- Mehrheits-GGF mit Sperrminoritaet: selbstaendig.
- Familien-GGF: Einzelfallpruefung.
- Fremd-GGF: in der Regel abhaengig.

### Phase 6 — Haftungsanalyse StB

- Bei Falsch-Klassifikation: Mandant-Nachforderung SV/LSt.
- AG-Anteil und AN-Anteil rueckwirkend 4 Jahre.
- Saeumniszuschlaege.
- Bei Vorsatz: § 266a StGB strafrechtlich.
- StB-Haftungsrisiko (§ 280 BGB): wenn StB hatte Veranlassung der Klassifikation.
- Berufshaftpflicht-Anmeldung pruefen.

## Output

- Memo zu Streitfall und Risikobewertung.
- Anwaltliche Begleitung empfohlen.
- Berufshaftpflicht-Anzeige falls relevant.

## Strategie und Praxis-Tipps

- Bei strittigen Klassifikationen frueh DRV-Statusfeststellung beantragen.
- Bei AN-Klage auf Festanstellung: Arbeitsrechtsanwalt einschalten.
- Bei DRV-Nachforderung: Anwaltliche Vertretung im SG-Verfahren.
- Bei BFH-Linie (Lohnsteuer): Steuerberater oder Anwalt mit Steuerrecht.
- StB-Haftungsrisiko bei "ich habe nur weiterabgerechnet" begrenzt — bei aktiver Beratung erheblich.
- StBVV: Streitfall-Begleitung nach Zeithonorar oder Streitwert.
- StB-BHV rechtzeitig informieren bei drohendem Haftungsanspruch.

## Querverweise

- `stb-lohn-gesellschafter-geschaeftsfuehrer-sv` — GGF-Status.
- `stb-lohn-pruefungen-drv-bp-haftung-stb` — DRV-Pruefung.
- `stb-lohn-werkstudent-pauschalen` — Werkstudent.
- `stb-drv-sozialversicherungspruefung` — DRV-Pruefung.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- BGB §§ 280, 611a.
- SGB IV § 7.
- ArbGG § 1; SGG § 51.
- StBerG § 67.
- StGB § 266a.
- BAG- und BSG-Linien; aktuelle Entscheidungen in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 1 bestaetigt (BAG 9 AZR 102/20 v. 01.12.2020 recherchiert), 3 ersetzt (Pruefhinweise ohne Marker) -->

## 6. `anw-akteneinsicht-steuerakte`

**Fokus:** Akteneinsicht in die Steuerakte beantragen und auswerten — Einspruchsverfahren nach § 364 AO Klageverfahren nach § 78 FGO sowie ergaenzend Art. 15 DSGVO bei personenbezogenen Daten. Anwendungsfall Mandant will Prüfungsbericht Aktenvermerk oder Prüfungsakte einsehen um Einspruch oder Klage zu begründen. Behandelt Verwaltungsakten Prüfungsakten Aktenvermerke Aussenprüfungs-Berichte Schwaerzungen wegen Steuergeheimnis Dritter § 30 AO. Output Antragsvorlage und strukturiertes Auswertungsraster für die uebermittelte Akte. Abgrenzung zu anw-aussenprüfung-strategien Mitwirkungspflichten und anw-einspruch-finanzamt.

# Akteneinsicht in Steuerakten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Akteneinsicht in Steuerakten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor dem Antrag

1. In welchem Verfahrensabschnitt befindet sich das Mandat? (Einspruchsverfahren → § 364 AO / Klageverfahren → § 78 FGO)
2. Wurde der Einspruch bereits eingelegt und das Aktenzeichen des Einspruchsverfahrens benannt?
3. Gibt es konkrete Hinweise auf Kontrollmitteilungen, Drittauskünfte oder Prüfungsnotizen, die zur Bescheidbegründung beitragen?
4. Hat das Finanzamt schon Tatsachen bezeichnet auf die es seine Entscheidung stützt (§ 364 Satz 1 AO)?
5. Ist eine einstweilige Sicherung (AdV) bereits beantragt oder erforderlich — dann Akteneinsicht parallel anfordern.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 364 AO** Akteneinsicht im Einspruchsverfahren — wesentlicher Aspekt des rechtlichen Gehörs; Behörde teilt die Tatsachen mit auf die sie ihre Entscheidung stützen will.
- **§ 78 FGO** Akteneinsicht im Klageverfahren vor dem Finanzgericht.
- **§ 71 Abs. 2 FGO** Beiziehung der Verwaltungsakten durch das Gericht.
- **Art. 15 DSGVO** Auskunft über eigene personenbezogene Daten — ergänzend nutzbar.
- **§ 88 AO** Untersuchungsgrundsatz im Verwaltungsverfahren.
- **§ 30 AO** Steuergeheimnis — Grenze der Einsicht in Drittdaten.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

§ 364 AO (Akteneinsicht Einspruch) · § 78 FGO (Klageverfahren) · § 71 Abs. 2 FGO (Beiziehung VA) · Art. 15 DSGVO · § 30 AO (Steuergeheimnis) · § 93a AO (Kontrollmitteilungen) · § 87a Abs. 1 S. 2 AO n.F. (ELSTER-Pflicht gegenüber FA)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Antrag im Einspruchsverfahren (§ 364 AO)

```
An das Finanzamt [ORT]
- Steuernummer [NUMMER] -

In dem Einspruchsverfahren über den [STEUERART]-Bescheid [JAHR]
vom [DATUM], Az. [AKTENZEICHEN]

beantragt der Einspruchsführer [NAME MANDANT],
vertreten durch RA/StB [KANZLEI]:

Akteneinsicht in die vollständige Steuerakte gemäß § 364 AO
einschließlich:
- Veranlagungsakten der Prüfungsjahre [JAHRE]
- Außenprüfungs-Berichte und Prüfungsnotizen (§§ 193 ff. AO)
- Aktenvermerke und interne Prüferkommunikation
- Korrespondenz mit Dritten (Kontrollmitteilungen § 93a AO)
- DAC7/CRS-Daten soweit entscheidungserheblich
- Daten aus dem automatischen Informationsaustausch

Bevorzugte Übermittlung: elektronisch über Mein ELSTER;
alternativ Papierform. Eine Übersendung per beA ist seit
6.12.2024 unzulässig (§ 87a Abs. 1 S. 2 AO n.F.).

[ORT], [DATUM] [UNTERSCHRIFT]
```

## Antrag im Klageverfahren (§ 78 FGO)

Antrag beim Finanzgericht auf Akteneinsicht (§ 78 FGO) kombiniert mit Beiziehungsantrag (§ 71 Abs. 2 FGO):

```
An das Finanzgericht [BUNDESLAND]
- Abt. [SENAT] / Az. [FG-AKTENZEICHEN] -

In der Streitsache [NAME] ./. Finanzamt [ORT] beantragen wir:

1. Die vollständige Steuerakte betreffend [STEUERART] [JAHRE]
 gemäß § 71 Abs. 2 FGO beizuziehen.
2. Dem Kläger Einsicht gemäß § 78 FGO in die beigezogene
 Verwaltungsakte zu gewähren, einschließlich interner
 Prüfernotizen und Kontrollmitteilungen.
3. Geschwärzten Aktenteilen ist eine Begründung der Schwärzung
 beizufügen; bei Streit beantragen wir gerichtliche Prüfung.
```

## Schritt-für-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Aktenlage klären:** Liegt Einspruchsentscheidung vor? → Klageverfahren → § 78 FGO; sonst → § 364 AO.
2. **Antrag formulieren** (Vorlage oben anpassen, Steuerart, Az, Mandantendaten).
3. **Versand:** an FA über ELSTER/ERiC oder per Briefpost/Fax (kein beA an FA); an FG über beA (§ 52d FGO).
4. **Frist überwachen:** FA hat keine gesetzliche Antwortfrist; bei Untätigkeit nach 4 Wochen Erinnerung; bei FG-Verfahren Beiziehungsantrag spätestens mit Klageeinreichung.
5. **Akteneingang prüfen:** Vollständigkeit anhand Aktendeckel-Übersicht; bei Lücken schriftlich nachhaken.
6. **Schwärzungen dokumentieren:** Position in Akte, Umfang, Begründung des FA — für spätere gerichtliche Prüfung.
7. **Auswertung** nach unten stehendem Raster.

## Sonderfälle

### Steuergeheimnis Dritter (§ 30 AO)

- Akten enthalten häufig Daten Dritter (Zeugenangaben, Kontrollmitteilungen, Anzeigen).
- Schwärzung zulässig wenn Drittdatenschutz dies erfordert.
- Bei umfangreicher Schwärzung: Antrag auf Begründung; ggf. gerichtliche Prüfung (§ 86 FGO).
- Prüfen ob die geschwärzten Teile entscheidungserheblich sein könnten → ggf. förmlicher Beweisantrag.

### Prüfungsanmerkungen und interne Vermerke

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Kontrollmitteilungen aus § 93a AO, DAC7-Meldedaten, FATCA-Daten ggf. relevant.

### Internationaler Datenaustausch

- Bei Auslandssachverhalten: Hinweise auf CRS-Daten, DAC-Auskünfte, FATCA — Akteneinsicht auch hierauf erstrecken.
- DAC7-Plattformdaten: seit 2024 im Einsatz, können Grundlage von Betriebsprüfungen sein.

## Entscheidungsbaum

Liegt Einspruchsentscheidung bereits vor?
→ **Ja:** Klageverfahren eingeleitet? → Ja: § 78 FGO + § 71 Abs. 2 FGO / Nein: ggf. noch § 364 AO im letzten Schritt des Einspruchsverfahrens
→ **Nein:** Einspruch eingelegt? → Ja: § 364 AO → Antrag oben / Nein: Einspruch einlegen, dann Akteneinsicht kombinieren

Akte vollständig?
→ **Ja:** Weiter zu Auswertungsraster
→ **Nein:** Fehlendes schriftlich nachfordern; bei anhaltender Weigerung im FG-Verfahren Richter zur Beiziehung bewegen (§ 76 FGO Amtsermittlung)

## Auswertung der eingegangenen Akte

Pro Aktenbestandteil:

| Nr. | Datum | Verfasser | Inhalt kurz | Relevanz | Verwendung |
|---|---|---|---|---|---|
| 1 | | | | entscheidend / hilfreich / neutral / belastend | Schriftsatz Rn. [X] |

Anschluss an Skill `anw-steuerbescheid-analyse` und Folge-Schriftsatz.

## Datenschutz

- Steuerakte enthält besonders sensible Daten (Vermögen, Einkommen, Familie, Konten).
- Verarbeitung nur in Tools mit AVV (Art. 28 DSGVO).
- Mandantenakte unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/steuerrecht-anwalt-und-berater/mandate/<az>/`.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Akteneinsicht in Steuerakte beantragen | Anschreiben nach Schema; Template unten |
| Variante A — Akteneinsicht fuer Dritte nicht Steuerpflichtigen | Vollmacht pruefen; Akteneinsicht nur mit Bevollmaechtigten-Nachweis |
| Variante B — Akteneinsicht im Strafverfahren StPO | Strafprozessuale Akteneinsicht § 147 StPO; anderer Antrag noetig |
| Variante C — Behoerde verweigert Akteneinsicht | Klage auf Akteneinsicht vor Finanzgericht; Widerspruch zuerst |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Anschreiben Mandant

**Adressat:** Mandant — Tonfall: verständlich-erklärend
```
Betreff: Akteneinsicht in Steuerakte [STEUERART] [JAHR]

Sehr geehrte/r [NAME MANDANT],

wir haben beim Finanzamt [ORT] Akteneinsicht gemäß § 364 AO
beantragt. Sobald die Akte eingeht, werten wir sie für Sie aus
und informieren Sie über die Ergebnisse, insbesondere über:

- Welche Unterlagen das Finanzamt als Entscheidungsgrundlage
 herangezogen hat
- Ob Kontrollmitteilungen Dritter die Festsetzung beeinflusst haben
- Welche Schwärzungen vorgenommen wurden und ob wir dagegen
 vorgehen sollten

[KANZLEI], [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Ausgabe

- Akteneinsichtsantrag `akteneinsichtsantrag-<az>-<datum>.docx`.
- Aktenchronik nach Eingang `aktenchronik-<az>.md`.
- Prüfkatalog mit `[prüferflag]`-Einträgen.
- Eintrag im Fristenbuch (Reaktionsfrist FA beobachten — Skill `anw-fristenbuch-steuerrecht`).

## 7. `anw-aussetzung-vollziehung`

**Fokus:** Antrag auf Aussetzung der Vollziehung AdV stellen um Steuerzahlung bis zur Streitentscheidung auszusetzen. Anwendungsfall Mandant hat Einspruch eingelegt will aber Nachforderung nicht sofort zahlen. Zweistufig zuerst beim Finanzamt § 361 Abs. 2 AO bei ernstlichen Zweifeln an der Rechtmäßigkeit oder unbilliger Haerte dann bei Ablehnung beim Finanzgericht § 69 Abs. 3 FGO. Prüfung Anordnungsanspruch ernstliche Zweifel oder unbillige Haerte und Anordnungsgrund drohende Vollziehung. Inkludiert eidesstattliche Versicherung. Output AdV-Antrag an FA und Antrag an FG. Abgrenzung zu anw-einspruch-finanzamt und anw-stundung-erlass-vollstreckungsaufschub.

# Aussetzung der Vollziehung (AdV)

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aussetzung der Vollziehung (AdV)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor dem Antrag

1. Ist ein Einspruch bereits eingelegt? (Voraussetzung für FA-Antrag nach § 361 AO)
2. Wie hoch ist der strittige Steuerbetrag? (Proportionalität der Begründungstiefe)
3. Hat das FA bereits eine AdV-Entscheidung getroffen? → Ja: direkt Stufe 2 (FG § 69 Abs. 3 FGO)
4. Droht unmittelbare Vollstreckung (Pfändungsankündigung, Kontopfändung)? → Eilantrag beim FG möglich
5. Liegt ein Fall unbilliger Härte vor (Existenzbedrohung, Insolvenz bei Zahlung)?
6. Soll hilfsweise Aufhebung der Vollziehung beantragt werden (bereits gezahlte Steuer zurückfordern)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Hintergrund

Einspruch und Klage gegen Steuerbescheide haben **keine aufschiebende Wirkung** (§ 361 Abs. 1 AO / § 69 Abs. 1 FGO). Die Steuer ist trotz Rechtsmittel zur Fälligkeit zu zahlen. Wer das nicht will: Antrag auf Aussetzung der Vollziehung.

## Zweistufiges Verfahren

### Stufe 1 — Antrag an das Finanzamt (§ 361 Abs. 2 AO)

Im laufenden Einspruchsverfahren stellt das FA die Vollziehung aus auf Antrag wenn:
- **ernstliche Zweifel** an der Rechtmäßigkeit des Bescheids bestehen, **oder**
- die Vollziehung für den Steuerpflichtigen eine **unbillige, nicht durch überwiegende öffentliche Interessen gebotene Härte** zur Folge hätte.

### Stufe 2 — Antrag an das Finanzgericht (§ 69 Abs. 3 FGO)

- Antrag zulässig wenn das FA den AdV-Antrag ganz oder teilweise abgelehnt hat **oder** über den Antrag nicht in angemessener Frist entschieden hat (§ 69 Abs. 4 FGO).
- Im Klageverfahren auch erstmals direkt an das FG möglich.

## Zentrale Anspruchsgrundlagen & Normen

- § 361 Abs. 2 AO — AdV durch das Finanzamt im Einspruchsverfahren
- § 69 Abs. 3 und 4 FGO — AdV durch das Finanzgericht im Klageverfahren
- § 361 Abs. 2 Satz 3 AO / § 69 Abs. 2 Satz 3 FGO — Sicherheitsleistung
- § 237 AO i.V.m. § 238 Abs. 1 S. 1 AO — Aussetzungszinsen 0,5 % pro vollem Monat / 6 % pro Jahr bei Verlust (Achtung: BFH-Vorlage BVerfG 1 BvL 8/24 anhaengig zur Verfassungsmaessigkeit, Zeitraum 01.01.2019 - 15.04.2021)
- § 155 Satz 1 FGO i.V.m. § 294 ZPO — Glaubhaftmachung durch eidesstattliche Versicherung
- § 69 Abs. 4 FGO — direkter FG-Antrag nach FA-Ablehnung oder FA-Untätigkeit

## Aktuelle Rechtsprechung

- **BFH, Vorlagebeschluss vom 08.05.2024 — VIII R 9/23** an das BVerfG (anhaengig BVerfG 1 BvL 8/24): Der Zinssatz fuer Aussetzungszinsen nach § 237 i.V.m. § 238 Abs. 1 S. 1 AO in Hoehe von 0,5 Prozent pro Monat ist nach Auffassung des BFH fuer den Zeitraum 01.01.2019 bis 15.04.2021 verfassungswidrig. Konsequenz fuer die Praxis: AdV-Antraege fuer betroffene Zeitraeume sollten den anhaengigen Vorlagebeschluss mitfuehren; ggf. AdV der Aussetzungszinsen selbst beantragen. Volltext BFH ueber die BFH-Datenbank (Vorlagebeschluss VIII R 9/23, STRE202410144).
- **BFH, Beschluss vom 21.03.2025 — X B 21/25 (AdV)** zu Saeumniszuschlaegen: Keine ernstlichen verfassungsrechtlichen Zweifel an der Hoehe der Saeumniszuschlaege nach § 240 Abs. 1 S. 1 AO fuer Zeitraeume nach dem 31.12.2018; gestuetzt auf das nachhaltig erhoehte Zinsumfeld seit Februar 2022. Volltext ueber BFH-Datenbank.
- **BFH, Beschluss vom 27.10.2025 — II B 47/25 (AdV)** zu Grunderwerbsteuer-Doppelfestsetzung nach § 1 Abs. 2b und § 1 Abs. 3 Nr. 1 GrEStG bei zeitlich getrenntem Signing und Closing eines GmbH-Anteilserwerbs: ernstliche Zweifel an der Rechtmaessigkeit bejaht; Vollziehung ausgesetzt. Volltext ueber BFH-Datenbank.
- **BFH, Beschluss vom 09.07.2025 — II B 13/25 (AdV)**: Massstab "ernstliche Zweifel" — gegeben, wenn bei summarischer Pruefung neben fuer die Rechtmaessigkeit sprechenden Umstaenden gewichtige gegen die Rechtmaessigkeit sprechende Gruende zutage treten, die Unsicherheit oder Unentschiedenheit in der rechtlichen oder tatsaechlichen Beurteilung bewirken. Volltext ueber BFH-Datenbank.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Einspruch prüfen:** Einspruch eingelegt und Frist gewahrt? Falls nicht → zuerst Einspruch.
2. **Begründung AdV zusammenstellen:** Ernstliche Zweifel (materielle Angriffspunkte aus Bescheidanalyse) oder unbillige Härte (Liquiditätslage, Existenzgefährdung).
3. **Stufe 1 — FA-Antrag:** Formulieren (Vorlage unten), versenden per ELSTER/ERiC oder Briefpost (kein beA an FA).
4. **FA-Antwort-Frist beobachten:** Angemessene Frist ca. 4 Wochen; bei Untätigkeit → Stufe 2.
5. **Stufe 2 — FG-Antrag:** Wenn FA ablehnt oder untätig → Antrag nach § 69 Abs. 3 FGO über beA.
6. **Eidesstattliche Versicherung:** Bei wirtschaftlicher Härte — Mandant unterschreibt.
7. **Sicherheitsleistung:** Hilfsantrag ohne / hilfsweise gegen Sicherheitsleistung formulieren.
8. **Fristenbuch:** AdV-Status und FA-Reaktionsfrist eintragen (Skill `anw-fristenbuch-steuerrecht`).

## Entscheidungsbaum

FA-Antrag gestellt?
→ **Nein:** FA-Antrag formulieren (§ 361 AO) → Stufe 1
→ **Ja:** FA hat entschieden? → Abgelehnt: FG-Antrag § 69 Abs. 3 FGO / Untätig (> 4 Wochen): FG-Antrag § 69 Abs. 4 FGO / Bewilligt: Fertig; Aussetzungszinsen beachten

Grundlage der AdV?
→ **Ernstliche Zweifel:** Substanz aus Einspruchsbegründung, BFH-Rechtsprechung zur Streitfrage
→ **Unbillige Härte:** Vermögens- und Liquiditätslage, Existenzgefährdung, Belege (Kontoauszüge, BWA)

## Antragsaufbau Stufe 1 (FA)

**Adressat:** Finanzamt — Tonfall: sachlich-juristisch

```
An das Finanzamt [ORT]
Steuernummer [NUMMER]

In dem Einspruchsverfahren über den [STEUERART]-Bescheid
[JAHR] vom [DATUM], Az. [AKTENZEICHEN]

Antrag auf Aussetzung der Vollziehung gemäß § 361 Abs. 2 AO

Wir zeigen die Vertretung des Einspruchsführers [NAME]
an und beantragen, die Vollziehung des o.g. Bescheids
bis zur Bekanntgabe der Einspruchsentscheidung auszusetzen.

Begründung:
[Ernstliche Zweifel: ...]
[Unbillige Härte: ...]

Ohne Sicherheitsleistung; hilfsweise gegen Sicherheitsleistung.

[KANZLEI], [DATUM]
```

## Antragsaufbau Stufe 2 (FG)

**Adressat:** Finanzgericht — Tonfall: sachlich-juristisch

```
An das Finanzgericht [BUNDESLAND]
[ANSCHRIFT]

In der Streitsache
[NAME MANDANT] — Antragsteller —
gegen
Finanzamt [ORT] — Antragsgegner —

Antrag auf Aussetzung der Vollziehung gemäß § 69 Abs. 3 FGO

1. Die Vollziehung des [STEUERART]-Bescheids [JAHR] vom
 [DATUM] in Gestalt der FA-Ablehnung vom [DATUM] wird
 bis zum rechtskräftigen Abschluss des Klageverfahrens
 (Az. FG [AKTENZEICHEN]) ausgesetzt.
 Hilfsweise wird die Aufhebung der Vollziehung beantragt.
2. Ohne Sicherheitsleistung; hilfsweise gegen Sicherheits-
 leistung nach richterlichem Ermessen.

Begründung:
A. Verfahrensgeschichte: [...]
B. Ernstliche Zweifel: [...]
C. Unbillige Härte (hilfsweise): [...]

Beweis: Eidesstattliche Versicherung Anlage Ast 1

[KANZLEI], [DATUM]
```

## Folge der AdV

- **Aussetzung:** Vollziehung bis Bekanntgabe Einspruchsentscheidung bzw. bis Rechtskraft.
- **Aussetzungszinsen** § 237 AO bei Verlust des Einspruchs / der Klage. **Aktueller gesetzlicher Zinssatz: 0,5 % pro vollem Monat / 6 % pro Jahr** (§ 238 Abs. 1 S. 1 AO; der durch das ZinsAnpG vom 12.07.2022 fuer Nachzahlungs- und Erstattungszinsen § 233a AO abgesenkte Satz von 0,15 % pro Monat = 1,8 % pro Jahr gilt **nicht** fuer Aussetzungszinsen). **Achtung**: BFH-Vorlagebeschluss vom 08.05.2024 (VIII R 9/23) an das BVerfG (anhaengig 1 BvL 8/24) — Zinssatz fuer Aussetzungszinsen 0,5 % pro Monat fuer den Zeitraum 01.01.2019 bis 15.04.2021 verfassungswidrig; betroffene Verfahren ggf. offenhalten und auf die BVerfG-Entscheidung warten.
- **Aufhebung Vollziehung** bei bereits gezahlter Steuer — Rückerstattung.
- **Teilaussetzung** möglich wenn nur ein Teil des Bescheids streitig ist.

## Frist

Keine gesetzliche Antragsfrist. Empfehlung: zusammen mit Einspruch oder Klage einreichen, spätestens vor Fälligkeit der Steuerschuld.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Aussetzung der Vollziehung beantragen | Mandantenschreiben nach Schema; Template unten |
| Variante A — AdV bei Finanzamt erfolglos Finanzgericht noetig | FG-Antrag nach § 69 Abs. 3 FGO als naechster Schritt |
| Variante B — Mandant will Bescheid akzeptieren nur Rate stunden | Stundungsantrag statt AdV; einfacher Weg |
| Variante C — Betrag sehr hoch Sicherheitsleistung gefordert | Sicherheitsleistungs-Verhandlung parallel; ggf. Buergschaft |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Mandantenschreiben

**Adressat:** Mandant — Tonfall: verständlich-erklärend

```
Betreff: Antrag auf Aussetzung der Vollziehung [STEUERART] [JAHR]

Sehr geehrte/r [NAME MANDANT],

wir haben heute beim Finanzamt [ORT] beantragt, die
Vollziehung des [STEUERART]-Bescheids vom [DATUM]
auszusetzen. Das bedeutet, dass Sie die streitige Steuer
von [BETRAG] Euro vorerst nicht zahlen müssen.

Wichtig: Falls wir im Einspruch unterliegen, fallen
Aussetzungszinsen an (gesetzlich 0,5 % pro vollem Monat /
6 % pro Jahr auf den ausgesetzten Betrag, § 237 i.V.m.
§ 238 Abs. 1 S. 1 AO; ein BFH-Vorlagebeschluss zur Ver-
fassungsmaessigkeit ist beim BVerfG anhaengig). Wir
informieren Sie über den weiteren Verfahrensgang.

[KANZLEI], [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Ausgabe

- `adv-antrag-<az>-<datum>.docx` (Stufe 1 FA oder Stufe 2 FG).
- Eidesstattliche Versicherung als Anlage.
- Eintrag im Fristenbuch: FA-Reaktionsfrist beobachten — bei Überschreitung Stufe 2 FG (`anw-fristenbuch-steuerrecht`).

## Versand

AdV-Antrag beim **Finanzamt** (§ 361 AO): über ELSTER/ERiC, Briefpost oder Telefax. **beA an Finanzamt unzulässig** seit 6.12.2024 (§ 87a Abs. 1 S. 2 AO n.F.). AdV-Antrag beim **Finanzgericht** (§ 69 Abs. 3 FGO): über beA (§ 52d FGO). Vor Versand `versand-vor-check` aus `kanzlei-allgemein`.

## 8. `anw-defi-lending-yield-farming-bmf-22-11-2024`

**Fokus:** Steuerliche Behandlung von DeFi-Lending Yield Farming Liquidity Mining Staking nach BMF-Schreiben vom 22.11.2024. Anwendungsfall Mandant nutzt DeFi-Protokolle Aave Compound Curve Yearn Uniswap Lido EigenLayer und fragt nach steuerlicher Erklärungspflicht. Einkuenfte § 22 Nr. 3 EStG oder § 20 EStG Token-Tausch als Veraeusserung § 23 EStG Spekulationsfrist Wrapped Tokens LP-Tokens Yield Tokens. DAC8-Meldepflicht beachten. Wallet-Analyse Cointracking Steuererklarung. Output steuerliche Beurteilung Erklärungspflichtige Einkuenfte Beratungsmemo. Abgrenzung zu anw-dac7-dac8-plattformen-krypto.

# DeFi-Lending / Yield Farming — Steuerliche Behandlung (BMF-Schreiben)

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DeFi-Lending / Yield Farming — Steuerliche Behandlung (BMF-Schreiben)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Wichtiger Hinweis zum Skill-Namen

Der Skill-Name verweist auf ein BMF-Schreiben vom 22.11.2024. Massgebend fuer die DeFi-Besteuerung ist nach gegenwaertigem Stand:

- **BMF-Schreiben vom 06.03.2025**, GZ IV C 1 - S 2256/00042/064/043 — Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte; ersetzt das BMF-Schreiben vom 10.05.2022 (IV C 1 - S 2256/19/10003 :001, BStBl 2022 I S. 668). Volltext auf bundesfinanzministerium.de (Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte).
- Ein gesondertes BMF-Schreiben mit Datum 22.11.2024 zu DeFi-Spezifika ist im offenen Recherchekreis (BMF-Webseite, NWB, dejure.org) **nicht verifizierbar**; das BMF-Schreiben vom 06.03.2025 enthaelt Aktualisierungen zu Staking, Lending, Liquidity-Mining, Bridging, NFTs sowie zu Mitwirkungs- und Aufzeichnungspflichten.

Bei Nutzung des Skills daher: BMF v. 06.03.2025 zugrundelegen; Skill-Name dokumentationshalber bestehen lassen.

## Zweck

Spezial-Mandat: Mandant nutzt DeFi-Protokolle (Aave, Compound, Curve, Yearn, Uniswap V3, Lido, EigenLayer) für Lending, Yield Farming, Liquidity Mining, Staking. Anwaltliche Beratung zur **steuerlichen Erklärung** nach **BMF-Schreiben vom 06.03.2025** (ersetzt BMF v. 10.05.2022). DeFi-Komplexität: jeder Token-Tausch ist potenziell Veräußerung; LP-Token-Einlage = Tausch; Rewards = Einnahmen.

## Eingaben

- Genutzte Protokolle (Aave, Compound, Uniswap, Lido, EigenLayer)
- Aktivitäten (Lending, Borrowing, LP, Staking, Restaking)
- Bestand Wallets (Adressen für Blockchain-Analyse)
- Tax-Tool im Einsatz? (Cointracking, Accointing, Koinly, Crypto Tax)
- Veranlagungszeitraum
- Einkünfte-Höhe (Steuersatz-Relevanz)

## Rechtlicher Rahmen

- **BMF-Schreiben vom 10.05.2022**, GZ IV C 1 - S 2256/19/10003 :001, BStBl 2022 I S. 668 — Grundlinien Krypto-Besteuerung (ersetzt durch BMF v. 06.03.2025).
- **BMF-Schreiben vom 06.03.2025**, GZ IV C 1 - S 2256/00042/064/043 — Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte (massgebend; siehe Hinweis oben). Volltext unter bundesfinanzministerium.de.
- **§ 22 Nr. 3 EStG** — Sonstige Einkünfte (Staking-Rewards, Lending-Zinsen, soweit nicht § 20).
- **§ 20 Abs. 1 Nr. 7 EStG** — Kapitalvermögen (Zinsähnliche Rewards).
- **§ 23 EStG** — Privates Veräußerungsgeschäft (Spekulationsfrist 1 Jahr; Hinweis: Die in einem fruehen Entwurf des BMF-Schreibens 2022 angedachte Verlaengerung auf 10 Jahre wurde nicht umgesetzt; aktuell gilt 1 Jahr fuer Krypto im Privatvermoegen).
- **§ 15 EStG** — Gewerbliche Einkünfte bei Daytrading-Charakter.
- **DAC8 (KryptoStG)** — KryptoStG vom 27.12.2024 (BGBl. 2024 I Nr. 449, in Kraft 01.01.2026); Meldepflicht der CASP; Erstmeldung 31.01.2027 fuer 2026.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BFH-Verfahren zu DeFi-Spezifika sind anhaengig — aktuellen Stand ueber dejure.org / BFH-Datenbank pruefen.

## Steuerliche Behandlung pro Aktivität

### A — Lending (Aave, Compound)

- Einzahlung in Lending-Pool: kein Steuer-Tatbestand (gleicher Token; BMF 22.11.2024 anders sieht es bei Wrapped Tokens aWETH ≠ ETH)
- **Wrapped Token (aWETH, cUSDC)**: BMF 22.11.2024 sieht Tausch ETH→aWETH als steuerbar an (Veräußerung § 23 EStG)
- **Lending-Zinsen** (variabel): § 20 Abs. 1 Nr. 7 EStG (Kapitalvermögen) — KapitalErtragsteuer 25 % + Soli + KiSt
- **Rückzug aWETH→ETH**: erneut steuerbar (Tausch zurück)

### B — Liquidity Mining (Uniswap V3, Curve, Balancer)

- Einzahlung Token-Paar in Pool gegen LP-Token: **Tausch § 23 EStG**
- Rewards (UNI, CRV, BAL): **§ 22 Nr. 3 EStG**
- Impermanent Loss: nicht steuerlich abzugsfähig (BMF-Linie)
- LP-Auflösung: erneut Tausch

### C — Staking (Lido, EigenLayer)

- Einzahlung in Staking-Vertrag (z. B. ETH→stETH): **Tausch § 23 EStG** (BMF 22.11.2024 hält stETH ≠ ETH)
- Rewards: § 22 Nr. 3 EStG
- Spekulationsfrist 1 Jahr (JStG 2022 hat 10-Jahres-Frist aus BMF 2022 wieder zurückgenommen)

### D — Restaking (EigenLayer)

- Doppel-Tausch: ETH→stETH→reSt-Token; jeder Schritt steuerbar
- Rewards aus Restaking: § 22 Nr. 3 EStG
- Slashing-Verlust: steuerlich abzugsfähig (Verlust-Verrechnung mit § 22 Nr. 3 EStG-Einkünften)

### E — Bridging (zwischen Chains)

- BMF 22.11.2024 differenziert: Funktional gleicher Token = kein Tausch; technisch Wrapped Token = Tausch
- Beispiel: ETH→WETH (Ethereum) = nicht-tauschbar (Liquidator/User-Identität); ETH→cbETH = Tausch
- Polygon-, Optimism-, Arbitrum-Bridges typisch nicht steuerbar (User-Identität bleibt)

## Workflow

### Phase 1 — Wallet- und Protokoll-Inventur

- Alle genutzten Wallet-Adressen sammeln (MetaMask, Ledger, Argent)
- Blockchain-Analyse (Etherscan, Arbiscan, Polygonscan)
- Protokoll-Liste mit Beträgen

### Phase 2 — Datenaufbereitung Tax-Tool

- Cointracking / Accointing / Koinly Import via API
- Manuelle Korrekturen (LP-Token-Tausch, Slashing-Verlust)
- BMF-Schreiben-konforme Bewertung (Tageskurs bei Tausch)

### Phase 3 — Steuererklärung

- **Anlage SO** für § 22 Nr. 3 EStG (Staking, Lending-Rewards bei nicht-Kapitalvermögen-Auslegung)
- **Anlage KAP** für § 20 EStG (Kapitalvermögen Lending-Zinsen)
- **Anlage V** für § 23 EStG (Veräußerungsgeschäfte)
- DAC8-konforme Mitwirkung mit CASP-Daten

### Phase 4 — Bei Selbstanzeige § 371 AO

- Bei nicht erklärtem DeFi-Vermögen aus Vorjahren: Selbstanzeige sinnvoll
- Vor DAC8-Erstmeldung 31.1.2027 dringend (Sperrwirkung droht)
- Vollständigkeit zwingend (10 Jahre rückwärts)

### Phase 5 — Bei Außenprüfung

- Steuerberater + Anwalt parallel
- BMF-Schreiben-Konformität nachweisen
- Beweissicherung Blockchain-Daten (Off-Chain-Logs schwer reproduzierbar)

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Nicht erklärtes DeFi-Vermögen ab 2024 | DAC8 deckt es 2027 auf; § 371 AO-Selbstanzeige vor Tatentdeckung | Selbstanzeige läuft | rechtzeitig erklärt |
| Wrapped-Token-Tausch nicht erfasst | Steuerverkürzung bei jedem aWETH→ETH-Move | Korrektur § 153 AO | volle Erfassung |
| Daytrading-Niveau | § 15 EStG (Gewerblich) statt § 23 — höherer Steuersatz | Klärung Gewinn-/Volumen-Schwelle | klar privat |
| Liquidity-Mining-Rewards in nicht-€ | Kursbewertung Tageskurs Pflicht | Tool-Bewertung | korrekt bewertet |

## Querverweise

- `anw-selbstanzeige-371` — bei nachträglicher Erklärung
- `anw-dac7-dac8-plattformen-krypto` — DAC8-Meldepflichten
- `anw-steuerbescheid-analyse` — Bescheid-Auswertung
- `anw-aussenpruefung-strategien` — bei BP
- `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig` — bei Krypto-Erbschaft

## Quellen und Updates

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 9. `anw-einspruch-finanzamt`

**Fokus:** Begründeten Einspruch gegen Steuerbescheid nach §§ 347 ff. AO formulieren. Anwendungsfall Mandant erhaelt Steuerbescheid und will Einspruch einlegen. Frist ein Monat ab Bekanntgabe § 355 Abs. 1 AO bzw. ein Jahr bei fehlender Rechtsbehelfsbelehrung § 356 AO Vier-Tage-Fiktion § 122 Abs. 2 AO seit 01.01.2025 PostModG. Angriffspunkte Rechtsverletzung Rechenfehler § 129 AO Schaetzung § 162 AO neue Tatsachen § 173 AO Festsetzungsverjährung § 169 AO Wiedereinsetzung § 110 AO. Output Einspruchsschriftsatz mit Antrag Begründung Beweisangebot AdV-Antrag § 361 Abs. 2 AO Akteneinsicht § 364 AO. Abgrenzung zu anw-klage-finanzgericht anw-steuerbescheid-analyse.

# Einspruch beim Finanzamt

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Einspruch beim Finanzamt` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor dem Einspruch

1. Wann ist der Bescheid zugegangen? (Bekanntgabefiktion § 122 Abs. 2 AO beachten — vier Tage seit 1.1.2025)
2. Ist die Einspruchsfrist (ein Monat § 355 AO) noch offen oder läuft sie heute/morgen ab?
3. Ist die Rechtsbehelfsbelehrung vorhanden und vollständig? (Ja → 1 Monat / Nein oder fehlerhaft → 1 Jahr § 356 AO)
4. Soll gleichzeitig AdV beantragt werden? → Liquiditätslage klären
5. Besteht Verbösserungsrisiko (§ 367 Abs. 2 AO) — hat das FA Anhaltspunkte auf höhere Steuer?
6. Liegt dem Bescheid eine Außenprüfung oder ein Schätzungsbescheid zugrunde? → andere Angriffsstrategien

## Eingaben

- Analyseprotokoll aus `anw-steuerbescheid-analyse`.
- Steuererklärung des Veranlagungsjahres und Belege.
- Bescheid im Original.

## Kaltstart-Rückfragen

1. Welcher Bescheid (Einkommensteuer, Umsatzsteuer, …) und welches Steuerjahr?
2. Datum der Bekanntgabe des Bescheids?
3. Konkrete Streitpunkte (Werbungskosten, Betriebsausgaben, Schätzung, Hinzuschätzung, …)?
4. Ist eine Aussetzung der Vollziehung (AdV) erforderlich?
5. Liegt eine Außenprüfung zugrunde?

## Anspruchsgrundlagen und Verfahrensrecht

- **Einspruch:** § 347 Abs. 1 Nr. 1 AO — Einspruch ist statthaft gegen Verwaltungsakte in Abgabenangelegenheiten.
- **Frist:** § 355 Abs. 1 AO — ein Monat ab Bekanntgabe. Bekanntgabe bei Postzustellung nach § 122 Abs. 2 Nr. 1 AO **am vierten Tag** nach Aufgabe zur Post (seit 01.01.2025 durch Postrechtsmodernisierungsgesetz PostModG; vorher dritter Tag); fällt der Vier-Tage-Tag auf Samstag, Sonntag oder Feiertag, verschiebt er sich auf den nächsten Werktag.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Verböserungsverbot — nicht absolut:** § 367 Abs. 2 S. 2 AO; bei beabsichtigter Verböserung Hinweis und Gelegenheit zur Rücknahme.
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr (§ 356 AO).

## Aktuelle Rechtsprechung

- **BFH, Beschluss vom 30.04.2025 — XI R 15/23** (E-Mail-Vorlagepflicht und Erstqualifikationsrecht des Steuerpflichtigen in der Aussenpruefung) — relevant fuer Einspruchsbegruendungen gegen Pruefungsfeststellungen und Bescheide. Volltext: dejure.org (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BFH&Datum=30.04.2025&Aktenzeichen=XI+R+15/23) / BFH-Datenbank.
- **BFH, Vorlagebeschluss vom 08.05.2024 — VIII R 9/23** (anhaengig BVerfG 1 BvL 8/24) — Verfassungsmaessigkeit der Aussetzungszinsen (§ 237 AO); fuer AdV-Antraege im Einspruchsverfahren relevant.
- **BFH, Beschluss vom 21.03.2025 — X B 21/25 (AdV)** zu Saeumniszuschlaegen § 240 AO — keine verfassungsrechtlichen Zweifel an der Hoehe fuer Zeitraeume nach 31.12.2018.
- Im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über dejure.org / BFH-Datenbank verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Beweislast

- Beweislast für steuermindernde Tatsachen (Betriebsausgaben, Werbungskosten): Steuerpflichtiger.
- Beweislast für steuererhöhende Tatsachen: Finanzbehörde.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema

```
1. Statthaftigkeit § 347 AO
 - Verwaltungsakt in Abgabenangelegenheit?
2. Form § 357 AO
 - Schriftlich oder elektronisch über § 87a AO?
3. Frist § 355 AO + Bekanntgabefiktion § 122 Abs. 2 AO (vier Tage seit 01.01.2025)
 - Bekanntgabedatum + 1 Monat (Wochenend-/Feiertagsregel beachten).
4. Beschwer
 - Steuerpflichtiger durch Bescheid in seinen Rechten beeinträchtigt?
5. AdV § 361 AO erforderlich?
 - Ernstliche Zweifel an Rechtmäßigkeit oder unbillige Härte?
6. Begründung
 - Streitige Punkte einzeln; Tatsachen, Beweismittel, Rechtsgrundlagen.
7. Rechtsschutz nach Einspruchsentscheidung
 - Klage FG § 47 FGO (1 Monat).
```

## Struktur des Einspruchsschreibens

### 1. Rubrum

- Einspruchsführer (Steuerpflichtiger) mit Anschrift und Steuernummer.
- Vertreter (RA mit ELSTER-Zugang als Bevollmächtigter).
- Empfangsfinanzamt mit Aktenzeichen / Steuernummer.
- Bezug: Bescheid vom (Datum) über (Steuerart) (Veranlagungsjahr).

### 2. Antrag

"Hiermit lege ich Einspruch gegen den Bescheid vom (Datum) über (Steuerart) (Jahr) ein und beantrage:

1. den angefochtenen Bescheid aufzuheben;
2. die Steuer wie folgt festzusetzen: ... EUR;
3. hilfsweise Aussetzung der Vollziehung gemäß § 361 Abs. 2 AO;
4. Akteneinsicht in die Steuerakten gemäß § 364 AO im Einspruchsverfahren."

### 3. Begründung

- Formale Mängel zuerst (Bekanntgabe Begründung Adressat).
- Materielle Mängel:
 - Sachverhaltsfehler (Einkünftezuordnung Werbungskosten Sonderausgaben Außergewöhnliche Belastungen).
 - Rechtsanwendungsfehler.
 - Schätzung unrealistisch (§ 162 AO).
- BFH-Rechtsprechung mit Pinpoint.
- Verweis auf BMF-Schreiben falls einschlägig.
- Bei Schätzungsbescheid: bestreitete Schätzungsgrundlagen plus eigene plausible Berechnung.

### 4. Belege

- Anlagen mit Sigel E1 E2 E3.
- Vollständige Belegliste (Belegart Datum Inhalt).

## Schreibvorlage

```
[Briefkopf Kanzlei]

Finanzamt [Ort]
[Anschrift]

vorab per Telefax oder ELSTER (beA an Finanzamt seit 6.12.2024 unzulässig, § 87a Abs. 1 S. 2 AO n.F.)
 [Ort], [Datum]

Steuernummer: [SteuerNr]
Bescheid: [Bescheidart, z. B. Einkommensteuerbescheid 2024]
Datum: [Bescheiddatum]

Einspruch und Antrag auf Aussetzung der Vollziehung

Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft, [Name], [Anschrift], legen wir gegen den oben bezeichneten Bescheid

 Einspruch (§ 347 AO)

ein und beantragen die

 Aussetzung der Vollziehung gemäß § 361 AO

in Höhe des streitigen Steuerbetrags von EUR [Betrag].

Begründung:

I. Sachverhalt
[Kurzdarstellung, Hinweis auf vorgelegte Belege/Anlagen]

II. Rechtliche Bewertung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. [Streitpunkt 2] – …

III. Antrag auf Aussetzung der Vollziehung
An der Rechtmäßigkeit des Bescheids bestehen ernstliche Zweifel iSd § 361 Abs. 2 S. 2 AO, weil […]. Die Vollziehung würde zudem eine unbillige Härte begründen, weil […].

IV. Akteneinsicht
Im Einspruchsverfahren wird Akteneinsicht gemäß § 364 AO beantragt.

Wir bitten um Bestätigung der Einspruchsbearbeitung und um Mitteilung über die AdV-Entscheidung binnen zwei Wochen.

Anlagen:
- Vollmacht
- [Belege]

Mit freundlichen Grüßen
[Anwalt, Fachanwalt für Steuerrecht]
```

## Verfahrensgang

1. **Einspruch eingelegt** → Finanzamt prüft.
2. **Hinweis nach § 367 Abs. 2 AO** wenn das FA die Steuer verbösern (Verschlechtern) will → der Einspruch kann zurückgenommen werden um Verboeserung zu vermeiden.
3. **Einspruchsentscheidung** mit Rechtsbehelfsbelehrung → bei Ablehnung Klage zum FG (Skill `anw-klage-finanzgericht`).
4. **Untätigkeit** des FA: nach sechs Monaten kann Klage erhoben werden (§ 46 FGO).
5. Bei Teilabhilfe: prüfen, ob neuer Bescheid Inhalt des Einspruchsverfahrens wird (§ 365 Abs. 3 AO).

## Ausgabe

- `einspruch-<az>-<datum>.docx` und Markdown-Spiegel.
- Eintrag im Fristenbuch (`anw-fristenbuch-steuerrecht`).
- Eintrag im Postausgang.

## Versand

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Zitierweise nach `zitierweise-deutsches-recht` v3.0 (Az.-Marker, Hierarchie + Chronologie).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
