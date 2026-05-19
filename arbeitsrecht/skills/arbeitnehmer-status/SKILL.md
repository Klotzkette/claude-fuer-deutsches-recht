---
name: arbeitnehmer-status
description: "Statusfeststellung für eine geplante Beschäftigung – Abgrenzung Arbeitnehmer/Selbständiger nach § 611a BGB, Scheinselbständigkeit, Clearingverfahren § 7a SGB IV, AÜG-Abgrenzung (Leiharbeit vs. Werkvertrag). Ausschließlich prospektiv – für bestehende Verhältnisse Außenberater einschalten."
---

# /arbeitsrecht:arbeitnehmer-status

## Zweck

Scheinselbständigkeit ist eines der teuersten Risiken im deutschen Arbeitsrecht. Nachentrichtung von Sozialversicherungsbeiträgen bis zu 4 Jahren rückwirkend (§ 25 SGB IV), Steuernachzahlungen, Bußgelder – und das Arbeitsverhältnis entsteht kraft Gesetzes (§ 10 AÜG bei unerlaubter Überlassung; ggf. § 611a BGB analog bei fehlerhafter Klassifizierung). Dieser Skill prüft prospektiv, ob die geplante Struktur hält.

## Eingaben

- Beschreibung der geplanten Tätigkeit (Art, Umfang, Ort, Dauer)
- Entwurf des Honorar- oder Werkvertrags (falls vorhanden)
- Angaben zur Einbindung in betriebliche Abläufe (eigene Betriebsmittel? Weisungsabhängigkeit? Mehrere Auftraggeber?)
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Klassifizierungsrisiken

## Ablauf

### 1. Arbeitnehmereigenschaft (§ 611a BGB)

Seit 01.04.2017 kodifiziert (§ 611a BGB):

**Arbeitnehmer** ist, wer aufgrund eines privatrechtlichen Vertrags **im Dienste eines anderen** zu **weisungsgebundener, fremdbestimmter Arbeit** verpflichtet ist. Maßgeblich ist das Gesamtbild; kein einzelnes Merkmal ist allein entscheidend.

**Weisungsgebundenheit** (§ 611a Abs. 1 S. 2 BGB):
- Inhalt, Durchführung, Zeit, Dauer oder Ort der Tätigkeit
- In den Betrieb eingegliedert?
- Eigene unternehmerische Entscheidungsfreiheit? (eigene Betriebsmittel, eigenes unternehmerisches Risiko)

**Prüfkatalog (BAG-Kriterienliste, Gesamtbild):**

| Indiz für Arbeitnehmer | Indiz für Selbständigen |
|---|---|
| Weisungsbefugnis bzgl. Arbeitszeit/-ort | Freie Zeiteinteilung |
| Eingliederung in Betriebsorganisation | Eigene Betriebsmittel |
| Kein unternehmerisches Risiko | Mehrere Auftraggeber |
| Keine eigenen Mitarbeiter | Eigene Werbung / Auftreten am Markt |
| Persönliche Leistungspflicht | Vertretung durch Dritte möglich |
| Betriebsmittel werden gestellt | Eigene Haftung für Ergebnis |
| Vergütung als festes Gehalt | Vergütung nach Projektergebnis |

BAG, Urt. v. 21.05.2019 – 9 AZR 295/18, NZA 2019, 1558 (Gesamtbildbetrachtung `[Modellwissen – prüfen]`)
BAG, Urt. v. 14.06.2016 – 9 AZR 305/15, NZA 2016, 1331 (Freelancer IT-Bereich `[Modellwissen – prüfen]`)

**Kontraktion des Willens:** § 611a Abs. 1 S. 5 BGB: Nicht ausschlaggebend ist die Bezeichnung im Vertrag (Honorarvertrag, Werkvertrag, freier Mitarbeiter); maßgebend ist die tatsächliche Durchführung (BAG, Urt. v. 17.10.2017 – 9 AZR 792/16, NZA 2018, 173 Rn. 24 `[Modellwissen – prüfen]`).

### 2. Sozialversicherungsrechtliche Bewertung (§ 7 SGB IV)

Gem. § 7 Abs. 1 SGB IV ist Beschäftigung die **nichtselbständige Arbeit**, insbesondere in einem Arbeitsverhältnis. Anhaltspunkte: Weisungsgebundenheit und Eingliederung (§ 7 Abs. 1 S. 2 SGB IV). Der SV-Begriff deckt sich weitgehend mit § 611a BGB, ist aber eigenständig auszulegen.

**Clearingverfahren § 7a SGB IV:**
- Jede der Beteiligten (Arbeitnehmer, Auftraggeber) kann vor Aufnahme der Tätigkeit Feststellung des Erwerbsstatus bei der **Deutsche Rentenversicherung Bund (Clearingstelle)** beantragen.
- Dauer: ca. 3–6 Monate
- Bei negativem Bescheid (Scheinselbständigkeit festgestellt): Nachzahlung Sozialversicherungsbeiträge bis zu 4 Jahre rückwirkend (§ 25 SGB IV); bei Vorsatz: 30 Jahre.
- **Empfehlung bei Grenzfällen:** Clearingverfahren proaktiv nutzen, bevor Tätigkeit beginnt.

### 3. AÜG-Abgrenzung (§§ 1 ff. AÜG)

Falls Dienstleistung durch Dritte (Werkvertrag, Dienstleistungsvertrag):

**Echte Arbeitnehmerüberlassung (AÜG):**
- Erlaubnispflichtig (§ 1 AÜG)
- Höchstüberlassungsdauer: 18 Monate (§ 1 Abs. 1b AÜG)
- Equal Pay nach § 8 AÜG ab Monat 10 (tariflich verlängerbar bis 15 Monate)
- Kein „verdeckter" Arbeitnehmer – Offenlegungspflicht in Vertrag (§ 1 Abs. 1 S. 5 AÜG; BAG, Urt. v. 12.07.2016 – 9 AZR 352/15, NZA 2016, 1332 `[Modellwissen – prüfen]`)

**Scheinselbständigkeit bei Werkvertrag:**
Wenn der Auftragnehmer nach Weisungen des Auftraggebers in dessen Betrieb eingegliedert ist, liegt verdeckte Arbeitnehmerüberlassung vor. Bei fehlender AÜG-Erlaubnis: Arbeitsverhältnis entsteht kraft Gesetzes (§ 10 Abs. 1 AÜG).

**10 Prüfpunkte Werkvertrag vs. Arbeitnehmerüberlassung:**
1. Schuldet Auftragnehmer einen Werkerfolg oder Dienste?
2. Trägt er das unternehmerische Werkrisiko (Nachbesserungspflicht, Gewährleistung)?
3. Setzt er eigene Betriebsmittel ein?
4. Bestimmt er Arbeitszeit und -ort selbst?
5. Erhält er Weisungen zu Inhalt und Durchführung?
6. Ist er in Teambesprechungen, Schichtpläne, EDV-Systeme des Auftraggebers eingebunden?
7. Muss er persönlich tätig sein oder kann er Erfüllungsgehilfen einsetzen?
8. Hat er mehrere Auftraggeber (Indiz für echte Selbständigkeit)?
9. Wie lange besteht die Geschäftsbeziehung? (Dauerschuldverhältnisse sind verdächtig)
10. Wie hoch ist der Anteil des Auftraggebers am Gesamtumsatz des Auftragnehmers? (> 75 %: hohes Risiko)

### 4. Praktische Handlungsempfehlungen

🟢 Kein Risiko:
- Auftragnehmer hat mehrere Auftraggeber, eigene Betriebsmittel, trägt unternehmerisches Risiko, keine Eingliederung

🟡 Grenzfall – Gestaltungsempfehlungen:
- Vertrag überarbeiten: Werkvertrag mit klarem Werkerfolg und Gewährleistung
- Eingliederung reduzieren: keine fixen Arbeitszeiten, kein Büro beim Auftraggeber, eigene IT
- Clearingverfahren § 7a SGB IV einleiten

🔴 Blockierend – Neustrukturierung oder reguläre Einstellung:
- Vollständige Eingliederung in Betrieb, feste Arbeitszeiten, kein eigenes unternehmerisches Risiko
- Keine AÜG-Erlaubnis, aber Beschäftigung wie Leiharbeitnehmer

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-deutsches-recht.md`.

Wesentliche Quellen:
- Wank, in: ErfK, 24. Aufl. 2024, § 611a BGB Rn. 1 ff. (Arbeitnehmerbegriff)
- Thüsing, in: MüKoBGB, 9. Aufl. 2022, § 611a BGB Rn. 80 ff.
- Schüren, in: HWK, 10. Aufl. 2022, § 1 AÜG Rn. 1 ff.
- BAG, Urt. v. 21.05.2019 – 9 AZR 295/18, NZA 2019, 1558
- BAG, Urt. v. 17.10.2017 – 9 AZR 792/16, NZA 2018, 173
- BSG, Urt. v. 04.09.2018 – B 12 KR 11/17 R, NZA 2019, 275 (§ 7 SGB IV, Gesamtbild `[Modellwissen – prüfen]`)

## Ausgabeformat

```
STATUSFESTSTELLUNG – [Tätigkeitsbeschreibung] – [Datum]
VERTRAULICH – MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

Ergebnis: [🟢 Selbständig / 🟡 Grenzfall / 🔴 Arbeitnehmerstatus wahrscheinlich]

I.   § 611a BGB Gesamtbild         [Bewertung mit Indikatoren-Tabelle]
II.  § 7 SGB IV (SV-rechtlich)    [Bewertung]
III. AÜG-Relevanz (falls gegeben) [Bewertung]
IV.  Clearingverfahren empfohlen? [ja/nein – Begründung]
V.   Gestaltungsempfehlungen       [konkrete Maßnahmen]

Risikobewertung: [🔴 / 🟠 / 🟡 / 🟢]
Wie weiter? [Entscheidungsbaum]
```

## Beispiele

**Beispiel – IT-Freelancer:**

*Sachverhalt:* Softwareentwickler K soll als „freier Mitarbeiter" für 12 Monate ausschließlich für einen Auftraggeber tätig sein, arbeitet täglich im Büro des Auftraggebers, nutzt dessen Laptop, nimmt an Daily-Standup-Meetings teil, erhält Aufgaben über das Jira-Board des Auftraggebers.

*Ergebnis:* 🔴 Arbeitnehmerstatus sehr wahrscheinlich. Faktoren: Ausschließlichkeit, Eingliederung in Betriebsabläufe, kein eigenes unternehmerisches Risiko, Betriebsmittel gestellt. Clearingverfahren § 7a SGB IV dringend empfohlen. Alternativ: reguläres Arbeitsverhältnis oder AÜG-konforme Leiharbeit (mit Erlaubnis).

## Risiken / typische Fehler

- **Vertrag vs. Praxis:** § 611a Abs. 1 S. 5 BGB – Wie der Vertrag heißt, ist unerheblich; entscheidend ist die tatsächliche Durchführung.
- **Rückwirkende Sozialversicherungspflicht** – bis 4 Jahre (§ 25 SGB IV), bei Vorsatz 30 Jahre.
- **AÜG ohne Erlaubnis** – führt zur Entstehung eines Arbeitsverhältnisses kraft Gesetzes (§ 10 AÜG); erhebliche Haftungsrisiken.
- **Prospektiver Charakter** – dieses Plugin prüft nur geplante Strukturen; für bestehende Verhältnisse unbedingt Außenberater und ggf. Clearingstelle einschalten.
