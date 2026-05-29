---
name: fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht
description: "Cyber-Versicherung bei Ransomware mit Sanktionsrisiko und Geldwäscherecht. Anwendungsfall Unternehmen erhaelt Erpressung durch Ransomware und prüft Lösegeldzahlung auf Versicherungsdeckung und Sanktionsrechtsverstoesse. Normen VVG Cyber-Deckung EU-Sanktions-VO 833/2014 269/2014 OFAC-Advisory § 261 StGB Geldwäsche AWG § 34 Aussenwirtschaftsstrafrecht. Prüfraster Deckungsschutz Versicherer Lösegeldzahlung Sanktionsprüfung Empfaenger OFAC-Screening Strafrechtsrisiko BaFin-Meldung. Output Cyber-Schadenprotokoll mit Sanktionsprüfung Deckungsanalyse und Handlungsempfehlung für oder gegen Lösegeldzahlung. Abgrenzung zu fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen und fachanwalt-versicherungsrecht-deckungsklage."
---

# Cyber-Lösegeld bei Ransomware mit Sanktions-Risiko

## Zweck

Spezial-Mandat: Mandant hat Cyber-Versicherung, wurde Opfer eines Ransomware-Angriffs. Eine Lösegeldzahlung wird erwogen oder wurde bereits geleistet. Der Versicherer verweigert Deckung mit Verweis auf Sanktionsrisiko (OFAC Specially Designated Nationals List, EU-Russland-Sanktionen, Lazarus Group Nordkorea). Dieser Skill begleitet sowohl die versicherungsrechtliche Deckungsklage als auch die strafrechtliche Risikobewertung.

## Kaltstart-Rückfragen

1. Liegt der vollständige Versicherungsvertrag (Cyber-Police) mit GDV-Musterbedingungen oder individuellen Klauseln vor — insbesondere: Enthält die Police eine Sanctions Limitation Clause?
2. Welche Indizien liegen zur Identität des Angreifers vor — Crypto-Wallet-Adresse, Tor-Adresse, Kommunikation, Malware-Signatur?
3. Wurde ein Chainalysis- oder Elliptic-Screening der Wallet-Adresse durchgeführt, und liegt ein Treffer auf der OFAC SDN List oder EU-Sanktionslisten vor?
4. Wann wurde das Lösegeld gezahlt (falls bereits erfolgt) oder wann wird die Zahlung erwogen?
5. Hat der Mandant Bezug zu den USA (US-Tochtergesellschaft, US-Kunden, US-Korrespondenzbank), der OFAC-Extraterritorialität auslösen könnte?
6. Wurde das BSI (bei KRITIS) und das LKA Cybercrime informiert?
7. Welche Backup-Optionen bestehen — wurde eine Datenwiederherstellung ohne Zahlung versucht?
8. Liegt das Ablehnungsschreiben des Versicherers vor und auf welche Klausel stützt dieser sich?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Sanktionsrecht

- **VO (EU) 833/2014** — Russland-Wirtschaftssanktionen (Sektorsanktionen, Finanztransaktionen mit Bezug zu Russland); zahlreiche Erweiterungspakete 2022–2025.
- **VO (EU) 269/2014** — Russland-Personensanktionen; Vermögenseinfrierung gelisteter Personen.
- **OFAC SDN List** (USA) — Specially Designated Nationals; 50-%-Regel: Unternehmen zu 50 % oder mehr im Eigentum einer SDN-gelisteten Person gilt selbst als SDN.
- **§§ 17, 18 AWG** — Embargo-Verstöße; Freiheitsstrafe bis 10 Jahre bei Vorsatz; Ordnungswidrigkeitenrahmen § 81 AWV.
- **OFAC Advisory vom 21.09.2021 zu Ransomware** — Lösegeld-Zahlungen an sanktionierte Akteure können selbst US-Sanktionsverstöße sein; strenge Haftung (strict liability) — guter Glaube keine Verteidigung.
- **Chainalysis Sanctions Screening** / **Elliptic** — forensische Tools zur Wallet-Rückverfolgung; Screening-Ergebnis ist dokumentationspflichtiger Compliance-Nachweis.

### Versicherungsrecht

- **§ 81 VVG** — Herbeiführung des Versicherungsfalls; Eigenverschulden des VN; quotale Kürzung bei grober Fahrlässigkeit.
- **§ 28 VVG** — Obliegenheitsverletzung; Kein-Backup-Vorwurf des Versicherers.
- **Sanctions Limitation Clause** in Cyber-Policen — typische Formulierung: "Der Versicherer erbringt keine Leistungen, die ihn oder seinen Rückversicherer einem Verstoß gegen Sanktionsrecht aussetzen würden." Prüfung auf Unwirksamkeit nach § 307 BGB Transparenzgebot.
- **GDV-Musterbedingungen Cyber AVB 2022** — Standarddeckung Ransomware als Versicherungsfall (§ 1 AVB Cyber); Deckungsausschluss nur bei vorsätzlicher Herbeiführung.

### Strafrecht

- **§ 261 StGB** — Geldwäsche; Lösegeld kann aus erpresserischer Bedrohung stammen (Vortat); Strafbarkeit auch bei Leichtfertigkeit.
- **§ 89c StGB** — Terrorismusfinanzierung (bei OFAC-gelisteten Gruppen: Hamas, Lazarus Group / Nordkorea, Hizballah).
- **§ 18 AWG** — Strafrechtliche Sanktionsverletzung bei Zahlung an SDN-gelistete Empfänger.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
| US: Travelers Ins. v. Universal Health | — | 2023 | Sanctions Exclusion; US-Gericht zur Wirksamkeit Ausschlussklausel |

## Prüfschema in Tabellenform


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Versicherungsfall Ransomware in AVB definiert? | GDV AVB Cyber; Police | Versicherungsfall "IT-Sicherheitsverletzung" umfasst Ransomware |
| 2 | Sanctions Limitation Clause vorhanden? | Police Individualklausel | Klausel prüfen auf Unwirksamkeit § 307 BGB |
| 3 | Erpresser auf OFAC SDN List? | OFAC SDN List; Chainalysis | SDN-Match → Zahlung verboten; kein Versicherungsschutz für verbotene Handlung |
| 4 | Erpresser auf EU-Sanktionslisten? | VO (EU) 269/2014; 833/2014 | EU-Sanktionsrecht unabhängig von US-OFAC |
| 5 | Kein SDN-Match — Sanktionsrisiko dennoch? | OFAC 50-%-Regel | Indirekte Sanktionierung prüfen; Compliance-Memo |
| 6 | US-Bezug des Mandanten? | AWG; OFAC-Jurisdiktion | Extraterritorialität bei US-Kunden/Bankkonto |
| 7 | Backup-Versuch vor Zahlung? | § 28 VVG Obliegenheit | Fehlender Backup-Versuch → Obliegenheitsverletzung-Risiko |
| 8 | BSI/LKA informiert? | § 8b BSIG; Polizei | Pflicht bei KRITIS; ggf. rechtfertigend für Zahlung |
| 9 | Lösegeldzahlung strafbar § 261 StGB? | § 261 StGB | Vortat Erpressung: Vortatanknüpfung ja; Strafbarkeit bei Leichtfertigkeit |
| 10 | § 89c StGB Terrorismusfinanzierung? | § 89c StGB | Bei OFAC-gelisteten Terrorgruppen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 12 | Grob fahrlässige Herbeiführung § 81 VVG? | § 81 VVG | Sicherheitspflichten verletzt? Kein Backup? |
| 13 | Deckungsklage LG-Sitz des Versicherers? | § 215 VVG; § 71 GVG | LG bei Streitwert ab EUR 10000 |
| 14 | Parallele Strafverteidigung nötig? | §§ 17, 18 AWG; § 261 StGB | Bei Zahlung an SDN: sofort Strafverteidiger |
| 15 | Compliance-Dokumentation für Akten? | AWG; OFAC Advisory | Screening-Ergebnis und Entscheidungsweg dokumentieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Cyber-Loesegeld-Zahlung und Sanktionsrecht pruefend | Sanktionspruefung + Deckungsanalyse nach Schema; Schriftsatz unten |
| Variante A — Zahlung bereits erfolgt Genehmigung nachtraeglich | OFAC-Antrag rueckwirkend stellen; Dokumentation sichern |
| Variante B — Versicherer verweigert Deckung wegen Sanktionsklausel | Deckungsklage parallel; Sanktionsrecht-Verteidigung separat |
| Variante C — Keine Zahlung geplant Wiederherstellung Vorrang | IT-Forensik und Wiederherstellung statt Loesegeldzahlung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Schadensanzeige und Deckungsanforderung

```
An [Versicherer Cyber]
Versicherungsnummer: [Nr]
Schadenummer: [neu]

Betr.: Ransomware-Vorfall vom [Datum]
       Deckungsanforderung und Compliance-Memo

Sehr geehrte Damen und Herren,

wir vertreten die [Unternehmen GmbH]. Am [Datum] wurde unsere
Mandantin Opfer eines Ransomware-Angriffs durch die Gruppe
[Bezeichnung], der zu Datenverschlüsselung und Betriebsausfall
führte. Einzelheiten ergeben sich aus dem Forensik-Bericht
vom [Datum], Anlage K1.

I. Versicherungsfall

Nach § [X] AVB Cyber liegt ein Versicherungsfall (IT-Sicherheits-
verletzung durch Cyber-Angriff) vor. Lösegeldforderung in Höhe
von EUR/USD [Betrag].

II. Sanctions-Compliance

Vor jeder Lösegeld-Entscheidung hat unsere Mandantin ein
Sanctions Screening durchgeführt:
- Wallet-Analyse durch Chainalysis Reactor am [Datum]:
  Kein direkter OFAC SDN-Match; Risikostufe [X] (Anlage K2).
- Keine Übereinstimmung mit EU-Sanktionslisten
  (VO (EU) 833/2014; VO (EU) 269/2014) (Anlage K3).
- Compliance-Memo der Rechtsabteilung vom [Datum] (Anlage K4).

Die Zahlung war daher rechtlich zulässig. Ihre Sanctions
Limitation Clause greift nicht ein, da kein sanktionierter
Empfänger vorliegt.

III. Deckungsanforderung

Wir fordern Sie auf, die Police-Leistungen wie folgt zu erbringen:
1. Lösegeldsumme EUR [X]
2. Betriebsunterbrechungsschaden EUR [Y] pro Tag × [Z] Tage
3. Forensik- und Wiederherstellungskosten EUR [Z]
4. Anwaltskosten EUR [...]

Bitte bestätigen Sie die Deckung bis [Datum + 2 Wochen].

[Rechtsanwälte]
```

### Baustein 2 — Deckungsklage: Sanctions Limitation Clause unwirksam

```
IV. SANCTIONS LIMITATION CLAUSE UNWIRKSAM

Die Beklagte stützt ihre Ablehnung auf die Sanctions Limitation
Clause in § [X] der Police, die lautet:
"[Wortlaut der Klausel]."

Diese Klausel ist unwirksam gemäß § 307 Abs. 1 Satz 2 BGB
(Transparenzgebot), weil ein durchschnittlicher Versicherungsnehmer
nicht erkennen kann,
a) welche Sanktionslisten konkret gemeint sind (US-OFAC, EU, UN,
   Bundesbank?),
b) welcher Standard für eine "Sanktionierung" gilt (SDN-Direkteintrag,
   50-%-Regel, Sektorsanktion?), und
c) ab welchem Grad der Verbindung zwischen Angreifer und Sanctions-Liste
   die Klausel auslöst.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
klar und verständlich formuliert sein; bei Unklarheit gilt
§ 305c Abs. 2 BGB zugunsten des Versicherungsnehmers.

Hilfsweise: Selbst wenn die Klausel wirksam wäre, greift sie im
Streitfall nicht ein, weil das Chainalysis-Screening eindeutig
keinen SDN-Match ergeben hat (Anlage K2).
```

### Baustein 3 — Compliance-Memo vor Lösegeldzahlung (Musterstruktur)

```
COMPLIANCE-MEMO — RANSOMWARE LÖSEGELDZAHLUNG
Vertraulich — Anwaltlich vertretene Angelegenheit

Datum: [Datum]
Mandant: [Unternehmen]

I. Sachverhalt
[Datum/Uhrzeit Angriff], Verschlüsselung [X] Systeme,
Lösegeldforderung [Betrag] in Bitcoin an Wallet [Adresse].

II. Screening-Ergebnis
Chainalysis Reactor-Analyse vom [Datum]:
- Direkte OFAC SDN Prüfung: kein Match
- Indirekte Sanktionsverbindung (50-%-Regel): kein Befund
- EU-Sanktionslisten (VO 269/2014; VO 833/2014): kein Match
- UN-Sanktionslisten: kein Match
Ergebnis: Sanktionsrechtliches Risikolevel = NIEDRIG

III. Strafrechtliche Bewertung
§ 261 StGB Geldwäsche: Vortat Erpressung liegt vor;
Strafbarkeit bei Leichtfertigkeit denkbar. Keine Leichtfertigkeit,
da Screening-Pflichten erfüllt.

§ 89c StGB: Keine Anhaltspunkte für Terrorgruppe.

IV. AWG
§ 17/18 AWG: Bei fehlendem SDN-Match kein Verstoss;
US-Bezug gering (kein US-Konto/US-Tochter).

V. Empfehlung
Unter Berücksichtigung des Screener-Ergebnisses und der
mangelnden Backup-Verfügbarkeit für [X Systeme] ist eine
kontrollierte Lösegeldzahlung rechtlich vertretbar.
Dokumentation für Rückversicherer und BaFin anlegen.

[Rechtsanwälte / Compliance Officer]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Versicherungsfall (Ransomware als IT-Sicherheitsverletzung) | Kläger (VN) |
| Sanctions Limitation Clause anwendbar | Versicherer |
| SDN-Match tatsächlich vorhanden | Versicherer (muss konkrete Liste und Eintrag benennen) |
| Screening ordnungsgemäß durchgeführt | VN (Chainalysis-Bericht, Datum, Methodik) |
| Obliegenheitsverletzung (kein Backup-Versuch) | Versicherer |
| Sanctions Limitation Clause wirksam | Versicherer (Transparenztest) |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Schadensanzeige | unverzüglich (24–48 Stunden) | Angriffserkenntnis | Police; § 30 VVG |
| BSI-Meldung (KRITIS) | 24 Stunden Frühwarnung | Ersterkenntnis | § 8b BSIG |
| NIS2-Meldung | 72 Stunden | Ersterkenntnis | NIS2UmsuCG |
| Verjährung Versicherungsanspruch | 3 Jahre | Jahresende Kenntnis | §§ 195, 199 BGB |
| OFAC SDGT-Meldepflicht (US-Bezug) | 10 Werktage nach Zahlung | Zahlung | OFAC Reg. 31 CFR Part 501 |
| Verjährung AWG-Verstöße | 5 Jahre | §§ 17, 18 AWG | § 31 OWiG |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| SDN-Match vorhanden | Screening-Bericht vorlegen; konkrete Wallet-Rückverfolgung durch SV; Versicherer muss Match beweisen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Kein Backup = grobe Fahrlässigkeit | § 28 Abs. 3 VVG: Kausalität; Backup-Fehler muss kausal für konkrete Lösegeldhöhe sein |
| Lösegeld = Vorsatz § 81 VVG | Keine Vorsatz-Herbeiführung des Angriffs durch VN; Zahlung als Notreaktion |
| Kein Versicherungsfall — "vorsätzliche Tat Dritter" | Drittangriff ist Versicherungsfall; kein Vorsatz des VN |
| Deckung ausgeschlossen wegen § 261 StGB | § 261 StGB schützt VN nicht; Versicherer kann nicht auf Strafbarkeit des VN verweisen, die er durch eigene Deckungsverweigerung erst veranlasst hat |

## Streitwert und Kosten

- Versicherungsleistung: Lösegeld + Betriebsunterbrechung + Forensikkosten; oft EUR 100000 bis mehrere Mio. EUR.
- LG-Verfahren obligatorisch bei Streitwert über EUR 10000 (§ 71 GVG).
- Sachverständige für Blockchain-Forensik: EUR 5000–20000 je nach Umfang.
- OFAC-Lizenz für US-Bezug: Antragstellung bei OFAC, USD 150–500; Bearbeitung 30–90 Tage.

## Strategische Empfehlung

- **Vor Zahlung:** Immer Chainalysis-Screening; Compliance-Memo erstellen; Versicherer frühzeitig informieren.
- **Bei SDN-Match:** Keine Zahlung; Versicherer und BSI/LKA informieren; OFAC-Specific License beantragen falls US-Bezug.
- **Deckungsklage:** Sanctions Limitation Clause auf Transparenz angreifen; SV für Blockchain-Forensik beauftragen.
- **Strafverteidigung parallel:** Bei Verdacht eines AWG-Verstoßes sofort Parallelverteidiger beiziehen.

## Anschluss-Skills

- `deckungsanfrage-pruefen` — allgemeines Deckungsprüfschema
- `klage-versicherer-strategie` — Klagestrategie nach Ablehnung
- `fachanwalt-versicherungsrecht-deckungsklage` — Klageschrift

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 261 StGB (Geldwäsche, n.F. seit 2021) → § 16 AWG (Verstöße gegen Außenwirtschaftsgesetz bei Sanktionsbruch) → Art. 4 VO 833/2014, Art. 2 VO 269/2014 (Russland-Sanktionen, Bereitstellungsverbot) → OFAC SDN-Liste (US-Treasury, extraterritoriale Wirkung) → § 134 BGB (Nichtigkeit bei Gesetzesverstößen) → §§ 100 ff. VVG (Haftpflichtversicherung Cyber) → § 1 VVG i.V.m. Cyber-AVB (Versicherungsfall Definition) → § 81 VVG (Ausschluss vorsätzliche Schadenverursachung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Maßnahme | Frist | Rechtsgrundlage |
|---|---|---|
| Meldung Ransomware-Vorfall an BSI | unverzüglich (KRITIS-Unternehmen) | § 8b BSIG |
| Geldwäsche-Meldepflicht | unverzüglich | § 43 GwG |
| Schadensanzeige Cyber-Versicherer | laut AVB (meist 7-14 Tage) | AVB Cyber |
| OFAC-Meldepflicht bei sanktionierten Empfängern | unverzüglich | OFAC-Regularien |

## Triage — Sofortprüfung Ransomware / Cyber-Lösegeld

1. **Identität des Angreifers prüfen:** Bekannte Ransomware-Gruppe auf OFAC SDN-Liste (z.B. Evil Corp, Conti-Affiliates)? → Bei OFAC-Listing: Zahlung ohne Lizenz verboten; Versicherer verweigert ggf. Deckung.
2. **EU-Sanktionsrecht prüfen:** Empfänger auf VO 269/2014 oder VO 833/2014 gelistet? → § 134 BGB, § 16 AWG-Risiko.
3. **Cyber-Versicherungspolice prüfen:** Lösegeld-Zahlungen ausdrücklich gedeckt? Sanktions-Ausschlussklausel in AVB?
4. **Geldwäscheprüfung:** § 261 StGB n.F. — kennt oder muss Zahler wissen, dass Empfänger aus Straftaten stammt? Interne AML-Prüfung dokumentieren.
5. **Meldepflichten erfüllt:** BSI (KRITIS), BaFin (regulierte Unternehmen), Staatsanwaltschaft (§ 261 StGB)?

**Entscheidungsbaum:**
```
Ransomware-Angriff + Lösegeld-Forderung?
├─ Angreifer auf OFAC-SDN-Liste? → Zahlung ohne US-Lizenz verboten
│   └─ Versicherer: Deckungsausschluss prüfen (§ 134 BGB + AVB)
├─ Angreifer auf EU-Sanktionsliste? → § 16 AWG + VO 269/2014
│   └─ Behördliche Genehmigung (BAW) erforderlich?
├─ Angreifer nicht gelistet → Geldwäsche-Risiko § 261 StGB prüfen
│   └─ AML-Prüfung dokumentieren; Meldepflicht § 43 GwG?
└─ Cyber-AVB analysieren → Lösegeld gedeckt? Sanktions-Klausel?
```
