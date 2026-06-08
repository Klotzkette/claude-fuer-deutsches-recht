---
name: rueckfragen-mandant-depatisnet
description: "Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR. Liefert Anmeldetag Veröffentlichungstag Erteilungstag Schutzdauer-Ende Status (anhaengig erteilt zurückgenommen zurückgewiesen erloschen nichtig), Einspruchsverfahren laufend abgeschlossen, Nichtigkeitsverfahren laufend abgeschlossen, Jahresgebühren bezahlt offen, Validierungsstaaten bei EP-Patenten, SPC für Arzneimittel und Pflanzenschutzmittel. Quellen werden mit Datum des Abrufs vermerkt. Disclaimer Rechtsstand kann sich taeglich aendern Stichtag-Datum dokumentieren im Patentrecherche: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# rechtsstand-prüfen

## Arbeitsbereich

Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR. Liefert Anmeldetag Veröffentlichungstag Erteilungstag Schutzdauer-Ende Status (anhaengig erteilt zurückgenommen zurückgewiesen erloschen nichtig), Einspruchsverfahren laufend abgeschlossen, Nichtigkeitsverfahren laufend abgeschlossen, Jahresgebühren bezahlt offen, Validierungsstaaten bei EP-Patenten, SPC für Arzneimittel und Pflanzenschutzmittel. Quellen werden mit Datum des Abrufs vermerkt. Disclaimer Rechtsstand kann sich taeglich aendern Stichtag-Datum dokumentieren. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: EPÜ R. 36 Teilanmeldung, PatG § 41 Priorität 12 Monate, USPTO Provisional 12 Monate, EPO Recherchebericht typ. 6 Monate.
- Tragende Normen verifizieren: PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen, PCT, Espacenet-Datenbankzugriff, DEPATISnet-Bedingungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Patentanmelder, Patentanwalt, DPMA-Prüfer, EPO-Examiner, USPTO, WIPO, Wettbewerber.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Recherchebericht, FTO-Gutachten, Patentlandschaftsanalyse, Espacenet/DEPATISnet/Patentscope/PatFT-Ausdruck, IPC-Klassifikationsbaum — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Sicherstellen, dass ein Treffer aus der Recherche **noch in Kraft** ist und seine Schutzwirkung tatsächlich entfaltet. Ein abgelaufenes Patent blockiert keinen Markteintritt, eine zurückgenommene Anmeldung erzeugt keinen Stand-der-Technik-Effekt (außer für die Veröffentlichung als solche).

## Wichtige Begriffe

- **Anmeldetag** (filing date) — Datum der Einreichung, **Schutzdauer-Beginn**.
- **Prioritätstag** (priority date) — Datum einer früheren Erstanmeldung; **maßgeblich für Stand der Technik** (§ 4 PatG, Art. 89 EPÜ).
- **Veröffentlichungstag** (publication date) — i. d. R. **18 Monate** nach Prioritätstag (§ 32 Abs. 2 PatG, Art. 93 EPÜ).
- **Erteilungstag** (grant date) — Veröffentlichung der Erteilung; **ab diesem Tag** Verbietungsrecht.
- **Schutzdauer-Ende** — Anmeldetag + 20 Jahre (§ 16 PatG, Art. 63 EPÜ). Bei Arzneimittel / PSM: + maximal 5 Jahre SPC nach VO (EG) 469/2009 / VO (EG) 1610/96.
- **Status:**
 - **Anhängig / pending** — Anmeldung läuft noch.
 - **Erteilt / granted / in force** — Patent ist erteilt und in Kraft.
 - **Zurückgenommen / withdrawn** — Anmelder hat zurückgezogen.
 - **Zurückgewiesen / refused** — Amt hat zurückgewiesen.
 - **Erloschen / lapsed** — Schutzdauer abgelaufen oder Jahresgebühren nicht bezahlt.
 - **Nichtig / revoked** — durch Einspruch oder Nichtigkeitsverfahren beseitigt.

## Quellen

| Schutzrecht | Register | URL |
| --- | --- | --- |
| Deutsche Patente und Gebrauchsmuster | DPMAregister | `https://register.dpma.de` |
| Europäische Patente und Anmeldungen | EPO Register | `https://register.epo.org` |
| US-Patente und Anmeldungen | USPTO Patent Public Search + PAIR/PEDS | `https://ppubs.uspto.gov`, `https://patentcenter.uspto.gov` |
| PCT-Anmeldungen | WIPO PATENTSCOPE | `https://patentscope.wipo.int` |
| Japanische Patente | J-PlatPat | `https://www.j-platpat.inpit.go.jp` |
| Chinesische Patente | CNIPA | `https://english.cnipa.gov.cn` |
| Koreanische Patente | KIPRIS | `https://www.kipris.or.kr` |

## Ablauf

### Schritt 1: Veröffentlichungsnummer normalisieren

Eingabe: Veröffentlichungs- oder Anmeldenummer in einer der Standardnotationen:

- `DE 10 2018 005 432 A1` (deutsche Anmeldung)
- `DE 10 2018 005 432 B4` (deutsches Patent erteilt)
- `EP 3 456 789 A1` (EP-Anmeldung)
- `EP 3 456 789 B1` (EP-Patent erteilt)
- `US 10,876,543 B2` (US-Patent erteilt)
- `US 2021/0123456 A1` (US-Patentanmeldung)
- `WO 2019/127345 A1` (PCT-Anmeldung)

### Schritt 2: Im passenden Register abfragen

Pro Veröffentlichungsnummer das richtige Register öffnen. Bei einer Familienanalyse für jedes Familienmitglied einzeln.

### Schritt 3: Rechtsstand-Eckdaten erfassen

Pro Schutzrecht:

```yaml
veroeffentlichungsnummer: EP 3 456 789 B1
familie:
 inpadoc_family_id: 12345678
 prioritaeten: [DE 15.03.2018]
anmeldetag: 14.03.2019
prioritaetstag: 15.03.2018
veroeffentlichungstag_anmeldung: 18.09.2019
erteilungstag: 12.09.2021
schutzdauer_ende: 14.03.2039
status: erteilt, in Kraft
anmelder_eingetragen: Siemens AG
einspruch:
 laufend: nein
 abgeschlossen: 12.06.2022 - Einspruch zurückgewiesen
nichtigkeit:
 laufend: nein
validierung_states: [DE, FR, GB, IT, NL]
jahresgebuehren_bezahlt_bis: 2026
abrufdatum: 20.05.2026
quelle: EPO Register
```

### Schritt 4: Status-Auswertung

- **Erteilt + Jahresgebühren bezahlt + Schutzdauer offen** → Patent wirkt voll. Für FTO **kritisch**.
- **Erteilt + Jahresgebühren offen** → kurzfristig vor Erlöschen, Achtung Rückzahlung mit Zuschlag (§ 17 Abs. 3 PatG sechs Monate, Art. 86 EPÜ sechs Monate).
- **Anhängig + noch nicht erteilt** → bisher kein Verbietungsrecht; **§ 33 PatG** Entschädigungsanspruch ab Veröffentlichung.
- **Zurückgenommen / zurückgewiesen / erloschen / nichtig** → keine Verbietungsrechte. Für Stand-der-Technik-Bewertung bleibt das Dokument relevant.
- **Einspruchsverfahren laufend** → Erteilung noch nicht stabil. Strategie-Frage: Einspruch selbst einlegen? Frist Art. 99 EPÜ neun Monate ab Erteilungs-Veröffentlichung.
- **Nichtigkeitsverfahren laufend** → vergleichbar mit Einspruch, vor BPatG.

### Schritt 5: Stichtag-Dokumentation

Jede Rechtsstandsabfrage erhält ein **Abrufdatum**. Der Rechtsstand kann sich täglich ändern — die Patentanwältin muss bei zeitkritischen Entscheidungen (Lizenzverhandlung, Markteintritt) eine **aktuelle** Direktabfrage durchführen.

### Schritt 6: Output

Tabelle mit Spalten: Veröff.-Nr., Status, Schutzdauer-Ende, Jahresgebühren bis, laufende Verfahren, Abrufdatum, Quelle.

## Hinweise

- **EP-Patente.** Das EPO Register zeigt die Erteilung und die Validierungsstaaten. **Für den Rechtsstand in jedem Validierungsstaat** ist das nationale Register maßgeblich — z. B. DPMAregister für DE-Validierung, INPI für FR, IPO für GB. EPO Register ist für Validierungs- und Übersetzungs-Stand zentral, aber nicht für die Jahresgebühren in jedem Staat.
- **Einheitliches Patent (UP).** Seit Juni 2023 — ein einziges Schutzrecht für alle Teilnehmer-Staaten. Jahresgebühren beim EPA. UPC zuständig für Streitfälle.
- **SPC** (Schutzzertifikat). Für Arzneimittel und Pflanzenschutzmittel — über das jeweilige nationale Register zu prüfen, weil SPCs national erteilt werden. Verlängerung der Schutzdauer um bis zu 5 Jahre.
- **Anmelder-Wechsel.** Bei einer Verletzungsklage zu beachten — Aktivlegitimation steht beim **eingetragenen** Inhaber. Bei FTO immer aktuellen Anmelder prüfen.
- **Lizenzen.** Eingetragen im Register, aber Eintragung ist deklaratorisch — auch nicht eingetragene Lizenzen können wirksam sein.

## Disclaimer

> **Hinweis zum Rechtsstand.** Diese Rechtsstandsprüfung beruht auf dem Datum des Abrufs (im Output explizit dokumentiert). Der Rechtsstand kann sich täglich ändern — Jahresgebuehren, Einspruchsverfahren, Nichtigkeitsverfahren, Anmelderwechsel. Bei zeitkritischen Entscheidungen ist eine aktuelle Direktabfrage im nationalen Register zwingend. Die Daten der Register können Verzoegerungen von einigen Tagen bis Wochen aufweisen.

## Triage-Fragen vor Rechtsstandpruefung

Bevor der Rechtsstand geprueft wird, klaere:
1. Welches Register ist massgeblich — DPMA, EPO, USPTO oder nationales Register des Validierungsstaats?
2. Wurden Jahresgebuehren-Zahlungen durch den Inhaber nachverfolgt (Zahlungsverzug = Patentverlust)?
3. Sind laufende Einspruchs- oder Nichtigkeitsverfahren bekannt (den Rechtsstand einschraenkend)?
4. Ist ein Einheitliches Patent (UP, seit 06/2023) vorhanden — andere Gebührenstruktur?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Erweiterte Beschwerdekammer, G 1/10 (Widerruf nach Einspruch):** Ein durch Einspruch angegriffenes Patent bleibt bis zur abschliessenden Einspruchsentscheidung in Kraft; der Rechtsstand ist waehrend des Einspruchsverfahrens unsicher, und ein Lizenznehmer sollte Klauseln für den Fall des Widerrufs vorsehen.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
