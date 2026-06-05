---
name: rueckfragen-mandant-depatisnet
description: "Rueckfragen Mandant Depatisnet: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rueckfragen Mandant Depatisnet

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rueckfragen Mandant Depatisnet** im Plugin Patentrecherche (FTO, Validity). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsstand-pruefen` | Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR. Liefert Anmeldetag Veröffentlichungstag Erteilungstag Schutzdauer-Ende Status (anhaengig erteilt zurückgenommen zurückgewiesen erloschen nichtig), Einspruchsverfahren laufend abgeschlossen, Nichtigkeitsverfahren laufend abgeschlossen, Jahresgebühren bezahlt offen, Validierungsstaaten bei EP-Patenten, SPC für Arzneimittel und Pflanzenschutzmittel. Quellen werden mit Datum des Abrufs vermerkt. Disclaimer Rechtsstand kann sich taeglich aendern Stichtag-Datum dokumentieren. |
| `rueckfragen-mandant` | Generiert Rückfragen an den Mandanten wenn das vorgelegte Material für eine sinnvolle Recherche nicht ausreicht oder Abgrenzungsfragen offen sind. Pflichtfragen: Was ist der wesentliche Lösungsbeitrag der Erfindung gegenüber dem Stand der Technik den der Mandant kennt; Welcher Anspruch ist der wichtigste; Welcher Markt und welche Zielstaaten; Gibt es eigene fruehere Veröffentlichungen Anmeldungen Vortraege Messeauftritte (Eigenstand der Technik); Gibt es Konkurrenten die das Plugin in den Watch nehmen soll; Welcher Recherchezweck. Formuliert die Rückfragen als Brief oder als Frageliste die in eine Mandantenrückfrage uebernommen werden kann. Disclaimer keine Rechtsberatung Patentanwaeltin verantwortet die Mandantenkommunikation. |
| `spezial-depatisnet-verhandlung-vergleich-und-eskalation` | Depatisnet: Verhandlung, Vergleich und Eskalation im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Patentrecherche (FTO, Validity) gilt für **Rueckfragen Mandant Depatisnet**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsstand-pruefen`

**Fokus:** Prüft Rechtsstand eines Patents oder einer Anmeldung im jeweiligen Amts-Register. DPMAregister für DE-Schutzrechte EPO Register für EP-Schutzrechte USPTO PAIR PEDS für US-Patente nationale Register für JP CN KR. Liefert Anmeldetag Veröffentlichungstag Erteilungstag Schutzdauer-Ende Status (anhaengig erteilt zurückgenommen zurückgewiesen erloschen nichtig), Einspruchsverfahren laufend abgeschlossen, Nichtigkeitsverfahren laufend abgeschlossen, Jahresgebühren bezahlt offen, Validierungsstaaten bei EP-Patenten, SPC für Arzneimittel und Pflanzenschutzmittel. Quellen werden mit Datum des Abrufs vermerkt. Disclaimer Rechtsstand kann sich taeglich aendern Stichtag-Datum dokumentieren.

# rechtsstand-prüfen

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

> **EPA, Erweiterte Beschwerdekammer, G 1/10 (Widerruf nach Einspruch):** Ein durch Einspruch angegriffenes Patent bleibt bis zur abschliessenden Einspruchsentscheidung in Kraft; der Rechtsstand ist waehrend des Einspruchsverfahrens unsicher, und ein Lizenznehmer sollte Klauseln fuer den Fall des Widerrufs vorsehen.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `rueckfragen-mandant`

**Fokus:** Generiert Rückfragen an den Mandanten wenn das vorgelegte Material für eine sinnvolle Recherche nicht ausreicht oder Abgrenzungsfragen offen sind. Pflichtfragen: Was ist der wesentliche Lösungsbeitrag der Erfindung gegenüber dem Stand der Technik den der Mandant kennt; Welcher Anspruch ist der wichtigste; Welcher Markt und welche Zielstaaten; Gibt es eigene fruehere Veröffentlichungen Anmeldungen Vortraege Messeauftritte (Eigenstand der Technik); Gibt es Konkurrenten die das Plugin in den Watch nehmen soll; Welcher Recherchezweck. Formuliert die Rückfragen als Brief oder als Frageliste die in eine Mandantenrückfrage uebernommen werden kann. Disclaimer keine Rechtsberatung Patentanwaeltin verantwortet die Mandantenkommunikation.

# rückfragen-mandant

## Zweck

Wenn das Material des Mandanten für eine seriöse Recherche nicht ausreicht — typische Fälle:

- Erfindung nur in einem Satz beschrieben
- Kein Anspruchsentwurf vorhanden
- Zielmarkt unklar
- Eigene frühere Veröffentlichungen des Mandanten nicht offengelegt
- Konkurrenten-Liste fehlt

— dann erzeugt dieses Skill eine Rückfrageliste oder einen Mandanten-Brief.

## Pflichtfragen

Jede Rückfrage muss diese Punkte abdecken:

### 1. Lösungsbeitrag

> Was ist Ihrer Einschätzung nach der **wesentliche Lösungsbeitrag** Ihrer Erfindung gegenüber dem Ihnen bekannten Stand der Technik?

Damit erschließt sich der Recherche-Fokus. Wenn der Mandant "alles ist neu" sagt: nachhaken — was ist das **eine** zentrale Merkmal, ohne das die Erfindung nicht funktioniert.

### 2. Anspruchsentwurf

> Welcher Anspruch ist aus Ihrer Sicht der **wichtigste Anspruch**? Liegt ein Anspruchsentwurf vor (auch als Stichwortliste reicht), oder soll die Anspruchsformulierung im Rahmen unserer Anmeldungsvorbereitung entwickelt werden?

### 3. Eigene frühere Veröffentlichungen

> Gibt es **eigene frühere Veröffentlichungen, Anmeldungen, Vorträge, Messeauftritte, Datenblätter, Produktbroschüren** zu dieser Erfindung oder zu eng verwandten Lösungen? Wenn ja: Datum, Ort, Inhalt.

Hintergrund: § 3 PatG kennt keine "eigene" Ausnahme. Eigene frühere Veröffentlichungen sind voll neuheitsschädlich. Sechs-Monats-Frist nach § 3 Abs. 5 PatG nur bei offensichtlichem Missbrauch oder amtlich anerkannter Ausstellung — eng auszulegen.

### 4. Zielmarkt / Territorien

> In welchen Ländern soll die Erfindung **vermarktet** werden? In welchen soll **Patentschutz** angestrebt werden? Sind US, JP, CN, KR relevant?

Bei FTO-Recherchen zwingend; bei Stand-der-Technik-Recherchen für die Klassenwahl und Sprachenstrategie wichtig.

### 5. Konkurrenten

> Welche **Konkurrenten** sehen Sie auf diesem Gebiet? Sollen wir laufendes Monitoring (Watch) einrichten?

### 6. Recherchezweck

> Welcher Zweck steht im Vordergrund — Patentanmeldung, FTO vor Markteintritt, Einspruchsstrategie, Nichtigkeitsstrategie, M&A-Due-Diligence, oder eine andere Konstellation?

### 7. Stand-der-Technik-Wissen des Mandanten

> Welche **Patente / Anmeldungen / Publikationen** kennen Sie selbst auf diesem Gebiet, die wir als Ausgangspunkt nehmen sollten?

Mandant hat oft mehr Branchen-Wissen als der Patentanwalt zur Technik. Diese Treffer **müssen** in die Recherche eingespeist werden.

### 8. Vertrauliche Hintergrundinformationen

> Gibt es Hintergrundinformationen, die für die Recherche relevant sind, aber **nicht in den schriftlichen Bericht** sollen? (Bezeichnung für interne Verwendung, Vertraulichkeitsstufe.)

### 9. Zeitrahmen

> Bis wann benötigen Sie das Ergebnis? Gibt es **eine bevorstehende Frist** (Anmeldetag, Einspruchsfrist, Markteinführungs-Stichtag)?

### 10. Honorar / Budget

> Soll die Recherche in einem **bestimmten Stunden- oder Budgetrahmen** bleiben, oder ist der Rechercheaufwand sachgerecht zu bemessen?

## Format

### Variante A: Frageliste (interne Akte)

Stichpunkte mit jeweils einer Frage und Platz für die Antwort des Mandanten.

### Variante B: Brief an den Mandanten

Brief mit Anrede, kurzer Einleitung ("wir bereiten die Recherche vor und benötigen folgende Klarstellungen"), Frageblock, Rückantwort-Bitte mit Frist, Schlussformel.

Vorlage:

```
[Kanzleibogen]

Aktenzeichen: [Aktenzeichen]
Datum: [TT.MM.JJJJ]

Sehr geehrte/r [Anrede Mandant],

zur Vorbereitung der angefragten Patentrecherche bitten wir Sie um folgende
Klarstellungen. Sie helfen uns, den Rechercheaufwand zielgerichtet zu steuern
und am Ende ein möglichst aussagekraeftiges Ergebnis vorzulegen.

1. [Frage 1 — Lösungsbeitrag]
2. [Frage 2 — Anspruchsentwurf]
3. [Frage 3 — eigene fruehere Veröffentlichungen]
4. [Frage 4 — Zielmarkt / Territorien]
5. [Frage 5 — Konkurrenten]
6. [Frage 6 — Recherchezweck]
7. [Frage 7 — Mandantenwissen zum Stand der Technik]
8. [Frage 8 — vertrauliche Hintergrundinformationen]
9. [Frage 9 — Zeitrahmen / Frist]
10. [Frage 10 — Honorar / Budget]

Bitte richten Sie Ihre Antworten an [Adresse] oder vereinbaren Sie einen Telefon-
oder Video-Termin mit unserem Sekretariat. Wir empfehlen eine Rückmeldung bis
zum [Datum], damit wir den vereinbarten Recherchetermin einhalten können.

Mit freundlichen Grüßen

[Patentanwältin / Patentanwalt]
```

## Hinweise

- **Verschwiegenheit.** Rückfragen können sensible Informationen aufdecken (frühere unveröffentlichte Anmeldungen, Konkurrenten-Liste). Kommunikationsweg nach § 39a PAO und § 203 StGB sicherstellen — verschlüsselter Mail-Versand, beA-äquivalente Patentanwalts-Kanäle (besonderes elektronisches Anwaltspostfach beA gilt nicht für Patentanwälte; aber äquivalente PAt-Kanäle prüfen).
- **Mandant ist Berufslaie.** Patentrechtliche Fachbegriffe sollten in Klammern erklärt werden, wenn der Mandant kein Patentprofi ist.
- **Mehrstufige Rückfragen.** Häufig ergeben sich aus der ersten Mandantenantwort Folgefragen — den Brief / die Frageliste als Living Document führen.

## Disclaimer

> **Hinweis zur Rückfrage.** Diese Rückfrageliste ist eine KI-gestützte Vorbereitung. Die Mandantenkommunikation verantwortet die Patentanwältin / der Patentanwalt — Inhalt, Sprache und Versandweg müssen vor Absendung kanzleiintern geprüft werden. Die Frageliste ersetzt nicht die individuelle Mandatsführung.

## Triage-Fragen vor Mandanten-Rueckfragen

Bevor die Rueckfrageliste erstellt wird, klaere:
1. Welches Rechercheprodukt benoetigt die Informationen — Neuheitspruefung, FTO, Pruefungsbescheid-Antwort oder Valorisierung?
2. Hat der Mandant bereits Unterlagen eingereicht (Anspruchsentwurf, Produktbeschreibung, Skizze)?
3. Besteht ein zeitlicher Druck (Patent-Frist, Messe-Neuheitsfrist, Vertragsverhandlung)?
4. Ist der Mandant technischer Fachmann oder berufslaie (Fragebogen-Sprachstil anpassen)?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `spezial-depatisnet-verhandlung-vergleich-und-eskalation`

**Fokus:** Depatisnet: Verhandlung, Vergleich und Eskalation im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Depatisnet: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Depatisnet: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** Depatisnet: Verhandlung, Vergleich und Eskalation / depatisnet verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO/WIPO/USPTO/DPMA sind Patentämter, INPADOC/CPC/IPC/Espacenet/DEPATISnet Recherchedatenbanken, FTO eine Arbeitsmethode — keine Rechtsquellen. Tragende Normen je nach Frage: PatG §§ 1–5 (Schutzfähigkeit, Neuheit), § 4 (erfinderische Tätigkeit), §§ 9, 10 (Schutzwirkung), §§ 34, 35, 37 (Anmeldung, Prioritäten), §§ 81 ff. (Nichtigkeit); EPÜ Art. 52–57 (Patentierbarkeit), Art. 54 (Neuheit), Art. 56 (erfinderische Tätigkeit), Art. 69 (Schutzbereich), Art. 87 ff. (Priorität); PCT Art. 1 ff.; UPCA. Quellen über DPMAregister, EPO Register, USPTO PatFT, WIPO Patentscope und WIPO Lex live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Depatisnet** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
